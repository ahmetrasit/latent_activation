"""Offline artifact validation and execution metadata; never repairs reader content."""
import copy
from collections import Counter
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "focus_trace_v3"))
import workflow as w


def runtime(directory):
    launch = w.read(directory / "launch.json")
    events = [json.loads(line) for line in (directory / "events.jsonl").read_text().splitlines()]
    thread = next(e["thread_id"] for e in events if e["type"] == "thread.started")
    paths = list((Path.home() / ".codex/sessions").glob(f"*/*/*/*{thread}.jsonl"))
    w.require(len(paths) == 1, "cannot locate unique session metadata")
    contexts, user_inputs, ambient, tool_counts, counts = [], [], [], Counter(), Counter()
    base, usage = None, None
    # Select configuration/input metadata and numerical counters only. Reasoning
    # items and assistant analysis text are never inspected, printed, or exported.
    with paths[0].open() as stream:
        for line in stream:
            row = json.loads(line)
            p = row.get("payload", {})
            if row["type"] == "session_meta":
                base = p["base_instructions"]
                base = base["text"] if isinstance(base, dict) else base
            elif row["type"] == "turn_context":
                contexts.append({k: p.get(k) for k in ("model", "effort", "cwd", "approval_policy", "sandbox_policy")})
            elif row["type"] == "compacted":
                counts["compacted"] += 1
            elif row["type"] == "event_msg":
                if p.get("type") in ("task_started", "task_complete", "token_count"):
                    counts[p["type"]] += 1
                if p.get("type") == "token_count" and p.get("info"):
                    usage = p["info"]
            elif row["type"] == "response_item":
                if p.get("type") in ("function_call", "custom_tool_call", "web_search_call", "local_shell_call"):
                    tool_counts[p.get("name", p["type"])] += 1
                if p.get("role") not in ("user", "developer"):
                    continue
                for content in p.get("content", []):
                    text = content.get("text", "")
                    if text.startswith("Assigned reader_id:"):
                        user_inputs.append({"sha256": w.digest(text.encode()), "bytes": len(text.encode())})
                    elif p["role"] == "developer":
                        ambient.append({"sha256": w.digest(text.encode()), "bytes": len(text.encode())})
    completed = [e for e in events if e["type"] == "turn.completed"]
    finals = [e["item"].get("text", "") for e in events
              if e["type"] == "item.completed" and e.get("item", {}).get("type") == "agent_message"]
    final_path = directory / ("reader.final.txt" if launch["delivery"] == "assigned-files" else "reader.response.json")
    commands = [{k: e["item"].get(k) for k in ("id", "command", "exit_code", "status")}
                for e in events if e["type"] == "item.completed" and e.get("item", {}).get("type") == "command_execution"]
    return {"thread_id": thread, "launch": launch, "turn_contexts": contexts,
            "profile_matches": bool(contexts) and all(c["model"] == "gpt-5.6-sol" and c["effort"] == "max" for c in contexts),
            "base_prompt_matches": base == (directory / "prompt.md").read_text().rstrip(),
            "assignment_matches": len(user_inputs) == 1 and user_inputs[0]["sha256"] == launch["stdin_sha256"],
            "input_messages": user_inputs, "ambient_developer_metadata": ambient,
            "tool_call_counts": dict(tool_counts), "completed_commands": commands,
            "event_counts": dict(counts), "completed_turns": len(completed),
            "usage": usage, "cli_completed_events": completed,
            "startup_warnings": [e["item"]["message"] for e in events if e.get("item", {}).get("type") == "error"],
            "final_message_matches_event": final_path.exists() and bool(finals) and final_path.read_text().strip() == finals[-1].strip(),
            "raw_output_sha256": w.digest((directory / "reader.response.json").read_bytes()) if (directory / "reader.response.json").exists() else None}


def validate(directory):
    result = {"semantic_quality_certified": False, "independent_json_schema_engine_run": False}
    raw_path = directory / "reader.response.json"
    if not raw_path.exists():
        return {**result, "status": "failed", "error": "assigned reader output missing"}
    try:
        raw = w.read(raw_path)
        packet = w.read(directory / "packet.json")
        job = w.read(directory / "job.json")
        for filename, checksum in job["inputs"].items():
            w.require(w.digest((directory / filename).read_bytes()) == checksum, "frozen input changed")
        w.require(raw.get("reader_id") == job["reader_id"], "wrong reader assignment")
        if directory.parent.name.startswith("v1-"):
            w.validator.validate_packet(packet)
            w.validator.validate_response(packet, raw)
            final = raw
            output = directory / "response.json"
            w.require(not output.exists() or output.read_bytes() == raw_path.read_bytes(), "existing output differs")
            output.write_bytes(raw_path.read_bytes())
            result["raw_output_preserved_exactly"] = True
        else:
            w.compile_job(directory)
            w.validate_job(directory)
            final = w.read(directory / "response.json")
            stripped = copy.deepcopy(final)
            stripped["protocol"] = raw["protocol"]
            for section in w.SECTIONS:
                for source, target in zip(raw[section], stripped[section], strict=True):
                    target["activation_trace"] = source["activation_trace"]
                    if section == "context_deltas":
                        del target["trigger_roots"]
            w.require(stripped == raw, "compiler changed reader prose")
            result["prose_and_findings_preserved_exactly"] = True
        cites = [c for section in w.SECTIONS for f in final[section] for c in f["activation_trace"]]
        result.update(status="passed", counts={s: len(final[s]) for s in w.SECTIONS},
                      resolved_citations=len(cites),
                      distinct_cited_branches=len({(c["mapped_root_id"], c["branch_id"]) for c in cites}),
                      distinct_cited_ayat=len({c["source_ref"] for c in cites}))
    except (ValueError, KeyError, TypeError) as error:
        result.update(status="failed", error=str(error))
    return result


if __name__ == "__main__":
    executions, validations = {}, {}
    for directory in sorted(HERE.glob("*/29_38")):
        name = directory.parent.name
        if not (directory / "launch.json").exists():
            continue
        if w.read(directory / "launch.json")["state"] == "running":
            print(f"{name}: still running")
            continue
        executions[name] = runtime(directory)
        validations[name] = validate(directory)
        print(name, validations[name])
    (HERE / "runtime.json").write_text(json.dumps(executions, indent=2) + "\n")
    (HERE / "validation.json").write_text(json.dumps(validations, indent=2) + "\n")
