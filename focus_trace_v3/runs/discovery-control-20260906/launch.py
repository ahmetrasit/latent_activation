"""Six frozen Sol/max sessions: v1, prior compact v3, and revised compact v3."""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "focus_trace_v3"))
import workflow as w

NAMES = [f"{condition}-{replicate}" for replicate in (1, 2)
         for condition in ("v1", "v3-current", "v3-revised")]


def preflight():
    jobs = {}
    old = ROOT / "focus_trace_v3/runs/rerun-20260906-compact-sol-max/29_38"
    for name in NAMES:
        directory = HERE / name / "29_38"
        job = w.read(directory / "job.json")
        w.require(not (directory / "launch.json").exists(), f"already launched: {name}")
        w.require(job["profile"] == {"model": "gpt-5.6-sol", "reasoning_effort": "max"}, "profile drift")
        for filename, checksum in job["inputs"].items():
            w.require(w.digest((directory / filename).read_bytes()) == checksum, f"frozen input changed: {name}/{filename}")
        if name.startswith("v1-"):
            originals = {"prompt.md": "focus_trace/prompts/focus_trace_hermetic.md",
                         "packet.json": "focus_trace/runs/s29/packets/29_38.packet.json",
                         "reader.schema.json": "focus_trace/schemas/focus-trace-response.schema.json"}
            for filename, original in originals.items():
                w.require((directory / filename).read_bytes() == (ROOT / original).read_bytes(), "v1 source drift")
            w.validator.validate_packet(w.read(directory / "packet.json"))
        else:
            w.load_job(directory)
            for filename in ("source.json", "packet.json", "reader.schema.json", "ledger.schema.json"):
                w.require((directory / filename).read_bytes() == (old / filename).read_bytes(), "v3 evidence/schema drift")
            if name.startswith("v3-current"):
                w.require((directory / "prompt.md").read_bytes() == (old / "prompt.md").read_bytes(), "current prompt drift")
        jobs[name] = job
    current = (HERE / "v3-current-1/29_38/prompt.md").read_text()
    revised = (HERE / "v3-revised-1/29_38/prompt.md").read_text()
    expected = current.replace((ROOT / "focus_trace_v3/prompts/integration.md").read_text(), "")
    expected = expected.replace("activation material, including non-dominant split-root targets.",
                                "activation material, including non-dominant split-root targets.\n"
                                "Do not collapse a split root to the dominant target only.")
    w.require(revised == expected, "unexpected revised prompt change")
    return jobs


def run(name, job, git_head, git_status):
    directory = HERE / name / "29_38"
    is_v1 = name.startswith("v1-")
    isolated = Path(tempfile.mkdtemp(prefix=f"hft-discovery-{name}-", dir="/private/tmp"))
    if is_v1:
        schema_path = isolated / "focus_trace/schemas/focus-trace-response.schema.json"
        schema_path.parent.mkdir(parents=True)
        shutil.copyfile(directory / "reader.schema.json", schema_path)
        shutil.copyfile(directory / "packet.json", isolated / "focus_trace_packet.json")
        payload = (f"Assigned reader_id: {job['reader_id']}\n"
                   "Assigned focus: 29:38.\n"
                   "Assigned packet: focus_trace_packet.json\n"
                   "Assigned schema: focus_trace/schemas/focus-trace-response.schema.json\n"
                   "Assigned output: response.json\n"
                   "Follow the supplied Hermetic Focus Trace prompt. Read only the assigned inputs. "
                   "Write and compact your assigned JSON output with jq as instructed. "
                   "The coordinator will validate it after your session. Return a short completion note.\n").encode()
        final_path = directory / "reader.final.txt"
    else:
        payload = (f"Assigned reader_id: {job['reader_id']}\nReturn only the reader response JSON.\n"
                   + "<response_schema>\n" + (directory / "reader.schema.json").read_text()
                   + "</response_schema>\n<sealed_packet>\n" + (directory / "packet.json").read_text()
                   + "</sealed_packet>\n").encode()
        final_path = directory / "reader.response.json"
    args = ["codex", "-a", "never", "exec", "--ignore-user-config", "--strict-config",
            "--skip-git-repo-check", "-s", "workspace-write" if is_v1 else "read-only", "-C", str(isolated),
            "-m", "gpt-5.6-sol", "-c", 'model_reasoning_effort="max"',
            "-c", "model_instructions_file=" + json.dumps(str(directory / "prompt.md")),
            "-c", "project_doc_max_bytes=0", "-c", 'web_search="disabled"',
            "--enable", "skip_host_skill_discovery"]
    for feature in ["apps", "plugins", "multi_agent", "multi_agent_v2", "browser_use",
                    "computer_use", "image_generation", "view_image", "memories", "hooks",
                    "skill_search", "code_mode_host", "sleep_tool", "goals", "shell_snapshot",
                    "unbounded_connection_retries"]:
        args += ["--disable", feature]
    args += ["--enable" if is_v1 else "--disable", "shell_tool"]
    args += ["--json", "--color", "never", "-o", str(final_path), "-"]
    record = {"started_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "argv": args, "stdin_sha256": hashlib.sha256(payload).hexdigest(),
              "stdin_bytes": len(payload), "profile": job["profile"], "condition": name,
              "delivery": "assigned-files" if is_v1 else "complete-inline",
              "service_tier_override": None, "fresh_session": True,
              "git_head_before_launch": git_head, "git_status_before_launch": git_status,
              "inputs": job["inputs"], "state": "running"}
    (directory / "launch.json").write_bytes(w.encode(record))
    print(f"Started {name}: Sol/max", flush=True)
    start = time.monotonic()
    try:
        with (directory / "events.jsonl").open("wb") as events, (directory / "stderr.log").open("wb") as errors:
            result = subprocess.run(args, input=payload, stdout=events, stderr=errors)
        record.update(exit_code=result.returncode, state="completed" if result.returncode == 0 else "failed")
        if is_v1:
            inputs_unchanged = ((isolated / "focus_trace_packet.json").read_bytes() == (directory / "packet.json").read_bytes()
                                and schema_path.read_bytes() == (directory / "reader.schema.json").read_bytes())
            record["assigned_files_unchanged"] = inputs_unchanged
            output = isolated / "response.json"
            record["assigned_output_exists"] = output.exists()
            if output.exists():
                shutil.copyfile(output, directory / "reader.response.json")
    except Exception as error:
        record.update(state="failed", error=str(error), exit_code=1)
    record.update(elapsed_seconds=time.monotonic() - start,
                  finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
    (directory / "launch.json").write_bytes(w.encode(record))
    print(f"Finished {name}: {record['state']}, {record['elapsed_seconds']:.1f}s", flush=True)
    return record["exit_code"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    jobs = preflight()
    if args.check:
        print("Six frozen jobs checked; evidence and intended prompt differences verified. No models launched.")
        sys.exit(0)
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    status = subprocess.check_output(["git", "status", "--short"], cwd=ROOT, text=True)
    w.require(not status, "commit the prepared experiment before launching")
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(lambda name: run(name, jobs[name], head, status), NAMES))
    sys.exit(int(any(results)))
