"""Extract execution metadata without copying private reasoning into artifacts."""
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def audit(profile):
    directory = ROOT / "focus_trace_v3/runs" / f"compare-20260906-{profile}-max/29_38"
    launch = json.loads((directory / "launch.json").read_text())
    events = [json.loads(line) for line in (directory / "events.jsonl").read_text().splitlines()]
    thread = next(x["thread_id"] for x in events if x["type"] == "thread.started")
    paths = list((Path.home() / ".codex/sessions/2026/09/06").glob(f"*{thread}.jsonl"))
    assert len(paths) == 1
    rows = [json.loads(line) for line in paths[0].read_text().splitlines()]
    meta = next(x["payload"] for x in rows if x["type"] == "session_meta")
    base = meta["base_instructions"]
    base = base["text"] if isinstance(base, dict) else base
    contexts, user_inputs, ambient, tools, counts, usage = [], [], [], [], Counter(), None
    for row in rows:
        p = row.get("payload", {})
        if row["type"] == "turn_context":
            contexts.append({k: p.get(k) for k in ("model", "effort", "cwd", "approval_policy", "sandbox_policy")})
        if row["type"] == "event_msg":
            counts[p.get("type")] += 1
            if p.get("type") == "token_count" and p.get("info"):
                usage = p["info"]
        if row["type"] == "compacted":
            counts["compacted"] += 1
        if row["type"] == "response_item":
            if p.get("type") in ("function_call", "custom_tool_call", "web_search_call", "local_shell_call"):
                tools.append({"type": p["type"], "name": p.get("name")})
            if p.get("role") in ("user", "developer"):
                texts = [c.get("text", "") for c in p.get("content", [])]
                for text in texts:
                    if text.startswith("Assigned reader_id:"):
                        user_inputs.append({"sha256": digest(text), "bytes": len(text.encode())})
                    elif p.get("role") == "developer":
                        ambient.append({"prefix": text[:90], "sha256": digest(text), "characters": len(text)})
    completed = [e for e in events if e["type"] == "turn.completed"]
    raw = directory / "reader.response.json"
    finals = [e["item"].get("text", "") for e in events
              if e["type"] == "item.completed" and e.get("item", {}).get("type") == "agent_message"]
    result = {"thread_id": thread, "launch": launch, "turn_contexts": contexts,
              "profile_matches": bool(contexts) and all(c["model"] == launch["profile"]["model"] and c["effort"] == launch["profile"]["reasoning_effort"] for c in contexts),
              "base_prompt_matches": base == (directory / "prompt.md").read_text().rstrip(),
              "base_prompt_normalization": "CLI strips the terminal newline; all other prompt text is identical",
              "inline_inputs": user_inputs,
              "complete_inline_delivery": len(user_inputs) == 1 and user_inputs[0]["sha256"] == launch["stdin_sha256"],
              "ambient_developer_messages": ambient, "tool_calls": tools,
              "event_counts": dict(counts), "completed_turns": len(completed),
              "usage": usage, "cli_completed_events": completed,
              "startup_warnings": [e["item"]["message"] for e in events
                                   if e.get("item", {}).get("type") == "error"],
              "raw_final_matches_event": raw.exists() and len(finals) == 1 and raw.read_text().strip() == finals[0].strip()}
    if raw.exists():
        result["raw_sha256"] = hashlib.sha256(raw.read_bytes()).hexdigest()
    return result


if __name__ == "__main__":
    results = {profile: audit(profile) for profile in ("sol", "luna")}
    (Path(__file__).parent / "runtime.json").write_text(json.dumps(results, indent=2) + "\n")
    for profile, result in results.items():
        print(profile, {k: result[k] for k in ("base_prompt_matches", "complete_inline_delivery", "completed_turns", "tool_calls", "raw_final_matches_event")})
