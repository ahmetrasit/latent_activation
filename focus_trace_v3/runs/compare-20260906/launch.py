"""Launch the two frozen 29:38 jobs once; no retries or output repair."""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "focus_trace_v3"))
from workflow import load_job


def run(profile):
    directory = ROOT / "focus_trace_v3/runs" / f"compare-20260906-{profile}-max/29_38"
    job, _ = load_job(directory)
    if (directory / "launch.json").exists():
        raise RuntimeError(f"Refusing to overwrite launch: {directory}")
    assignment = f"Assigned reader_id: {job['reader_id']}\nReturn only the reader response JSON.\n"
    payload = (assignment + "<response_schema>\n" + (directory / "reader.schema.json").read_text()
               + "</response_schema>\n<sealed_packet>\n" + (directory / "packet.json").read_text()
               + "</sealed_packet>\n").encode()
    isolated = tempfile.mkdtemp(prefix=f"hft-v3-29-38-{profile}-")
    args = ["codex", "-a", "never", "exec", "--ignore-user-config", "--strict-config",
            "--skip-git-repo-check", "-s", "read-only", "-C", isolated,
            "-m", job["profile"]["model"],
            "-c", 'model_reasoning_effort="max"',
            "-c", "model_instructions_file=" + json.dumps(str(directory / "prompt.md")),
            "-c", "project_doc_max_bytes=0", "-c", 'web_search="disabled"',
            "--enable", "skip_host_skill_discovery"]
    for feature in ["apps", "plugins", "shell_tool", "multi_agent", "multi_agent_v2",
                    "browser_use", "computer_use", "image_generation", "view_image",
                    "memories", "hooks", "skill_search", "code_mode_host", "sleep_tool",
                    "goals", "shell_snapshot", "unbounded_connection_retries"]:
        args += ["--disable", feature]
    args += ["--json", "--color", "never", "-o", str(directory / "reader.response.json"), "-"]
    record = {"started_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "argv": args, "stdin_sha256": hashlib.sha256(payload).hexdigest(),
              "stdin_bytes": len(payload), "profile": job["profile"],
              "service_tier_override": None, "fresh_session": True,
              "inputs": job["inputs"], "state": "running"}
    (directory / "launch.json").write_text(json.dumps(record, indent=2) + "\n")
    print(f"Started {profile}/max", flush=True)
    start = time.monotonic()
    with (directory / "events.jsonl").open("wb") as events, (directory / "stderr.log").open("wb") as errors:
        result = subprocess.run(args, input=payload, stdout=events, stderr=errors)
    record.update(exit_code=result.returncode, elapsed_seconds=time.monotonic() - start,
                  finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  state="completed" if result.returncode == 0 else "failed")
    (directory / "launch.json").write_text(json.dumps(record, indent=2) + "\n")
    print(f"Finished {profile}/max: exit {result.returncode}, {record['elapsed_seconds']:.1f}s", flush=True)
    return result.returncode


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(run, ["sol", "luna"]))
    sys.exit(int(any(results)))
