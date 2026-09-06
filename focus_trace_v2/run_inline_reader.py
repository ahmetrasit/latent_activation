#!/usr/bin/env python3
"""Run one approved sealed reader with complete inline inputs and no retry."""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import workflow as w


def request(job_dir: Path) -> tuple[dict, list[str], str]:
    job, _, _ = w.load_job(job_dir, require_response=False)
    profile = job["requested_profile"]
    w.require(profile["model"] in w.MODELS, "unsupported requested model")
    w.require(profile["reasoning_effort"] in w.REASONING_EFFORTS, "unsupported requested effort")
    # The frozen discovery prompt replaces the coding-agent base instructions.
    # All semantic evidence is delivered intact; no paging or summarization.
    config = [
        f'model_reasoning_effort={json.dumps(profile["reasoning_effort"])}',
        f'model_instructions_file={json.dumps(str(job_dir / "prompt.md"))}',
        'web_search="disabled"',
        "features.multi_agent=false", "features.apps=false", "features.plugins=false",
        "features.shell_tool=false", "features.browser_use=false",
        "features.computer_use=false", "features.image_generation=false",
        "features.view_image=false", "features.sleep_tool=false", "features.goals=false",
    ]
    args = ["codex", "-a", "never", "exec", "--ignore-user-config", "--strict-config",
            "--model", profile["model"], "--sandbox", "read-only", "--cd", str(job_dir),
            "--json", "--output-last-message", str(job_dir / "response.json")]
    for value in config:
        args.extend(["-c", value])
    args.append("-")
    # No service-tier override, no inherited conversation, no old findings.
    text = ("The complete frozen packet and response schema follow. Follow the supplied "
            "discovery instructions. Do not call tools or read files: all evidence is already "
            "included here. Return only the response JSON; the coordinator saves your final "
            "message as the assigned response.json.\n\n")
    if job["protocol"] == w.JOB_PROTOCOL:
        text += f"The assigned reader_id is {job['reader_id']}. The coordinator performs the required formatting-only JSON compaction.\n\n"
    for filename in w.reader_filenames(job):
        text += f"<{filename}>\n" + (job_dir / filename).read_bytes().decode("utf-8") + f"</{filename}>\n"
    return job, args, text


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("job_dir", type=Path)
    parser.add_argument("--inspect", action="store_true", help="print request sizes/settings without generation or writes")
    args = parser.parse_args()
    job_dir = args.job_dir.resolve()
    w.require(job_dir.is_relative_to((w.WORKFLOW_ROOT / "runs").resolve()), "job must stay under HFT v2 runs")
    job, command, text = request(job_dir)
    if args.inspect:
        print(json.dumps({"command": command, "stdin_bytes": len(text.encode("utf-8")),
                          "input_identity": job["input_identity"]}, ensure_ascii=False))
        return
    for name in ("response.json", "inline.launch.json", "inline.events.jsonl", "inline.stderr.log", "inline.result.json"):
        w.require(not (job_dir / name).exists(), f"refusing an existing artifact: {name}")
    launch = {"started_at": datetime.now(timezone.utc).isoformat(), "command": command,
              "input_identity": job["input_identity"], "stdin_sha256": w.digest(text.encode("utf-8")),
              "requested_profile": job["requested_profile"], "harness": "complete-inline-codex",
              "launcher_sha256": w.digest(Path(__file__).read_bytes()), "automatic_retry": False}
    with (job_dir / "inline.launch.json").open("xb") as stream:
        stream.write(w.json_bytes(launch))
    with (job_dir / "inline.events.jsonl").open("xb") as events, (job_dir / "inline.stderr.log").open("xb") as errors:
        result = subprocess.run(command, input=text.encode("utf-8"), stdout=events, stderr=errors, check=False)
    receipt = {"finished_at": datetime.now(timezone.utc).isoformat(), "exit_code": result.returncode}
    if result.returncode == 0 and job["protocol"] == w.JOB_PROTOCOL:
        response_path = job_dir / "response.json"
        # V1 requests formatting-only compaction. The original model text also
        # remains in inline.events.jsonl; do not change fields or repair JSON.
        try:
            response_path.write_bytes(w.json_bytes(w.read_json(response_path)))
        except (ValueError, OSError) as error:
            receipt.update(exit_code=1, compaction_error=str(error))
    with (job_dir / "inline.result.json").open("xb") as stream:
        stream.write(w.json_bytes(receipt))
    print(json.dumps({"job_dir": str(job_dir), **receipt}))
    raise SystemExit(receipt["exit_code"])


if __name__ == "__main__":
    main()
