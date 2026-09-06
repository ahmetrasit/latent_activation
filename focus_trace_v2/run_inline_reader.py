#!/usr/bin/env python3
"""Run one approved sealed reader with complete inline inputs and no retry."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import workflow as w


EXISTING_OUTPUTS_LIMIT = (
    "Do not read or use existing outputs from earlier runs or other agents; "
    "the only permitted prior output is your own discovery notes from this run.\n\n"
)


def discovery_thread(job_dir: Path, job: dict) -> str:
    _, receipt = w.completed_discovery(job_dir, job)
    events_path = job_dir / "discovery.events.jsonl"
    w.require(w.digest(events_path.read_bytes()) == receipt["events_sha256"], "discovery events changed")
    w.require(completed_thread(events_path) == receipt["thread_id"], "discovery session mismatch")
    runtime_check(receipt["thread_id"], job["requested_profile"], turns=1)
    return receipt["thread_id"]


def runtime_check(thread: str, profile: dict, *, turns: int, session_root: Path | None = None) -> dict:
    """Read runtime metadata only. No model call or reasoning text is exposed."""
    if session_root is None:
        session_root = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "sessions"
    paths = list(session_root.glob(f"*/*/*/*-{thread}.jsonl"))
    w.require(len(paths) == 1, "cannot verify the exact local reader session")
    profiles, starts, completions, compactions = set(), 0, 0, 0
    for line in paths[0].read_text().splitlines():
        if not line.strip():
            continue
        event = json.loads(line)
        payload = event.get("payload", {})
        if not isinstance(payload, dict):
            payload = {}
        if event["type"] == "turn_context":
            profiles.add((payload.get("model"), payload.get("effort")))
        if event["type"] == "event_msg":
            starts += payload.get("type") == "task_started"
            completions += payload.get("type") == "task_complete"
        compactions += event["type"] == "compacted" or payload.get("type") == "context_compacted"
    w.require(profiles == {(profile["model"], profile["reasoning_effort"])}, "observed reader profile differs from requested profile")
    w.require(starts == completions == turns, "unexpected intervening or incomplete reader turns")
    w.require(compactions == 0, "reader context was compacted; two-stage continuation requires the full packet")
    return {"observed_profile": profile, "completed_turns": completions, "context_compactions": compactions}


def completed_thread(path: Path) -> str:
    events = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    threads = [event["thread_id"] for event in events if event["type"] == "thread.started"]
    w.require(len(threads) == 1 and sum(event["type"] == "turn.completed" for event in events) == 1,
              "expected one completed reader turn and explicit session")
    w.require(not any(event["type"] in {"error", "turn.failed", "compacted"} for event in events),
              "reader turn failed or compacted")
    w.require(re.fullmatch(r"[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}", threads[0]) is not None,
              "reader session must be an explicit UUID")
    return threads[0]


def request(job_dir: Path, stage: str = "single") -> tuple[dict, list[str], str]:
    job, _, _ = w.load_job(job_dir, require_response=False)
    w.require(stage in {"single", "discovery", "ledger"}, "unknown reader stage")
    w.require(("two_stage_inputs" in job) == (stage != "single"), "two-stage jobs need --stage discovery or --stage ledger; one-pass jobs use single")
    profile = job["requested_profile"]
    w.require(profile["model"] in w.MODELS, "unsupported requested model")
    w.require(profile["reasoning_effort"] in w.REASONING_EFFORTS, "unsupported requested effort")
    # The frozen discovery prompt replaces the coding-agent base instructions.
    # All semantic evidence is delivered intact; no paging or summarization.
    config = [
        f'model_reasoning_effort={json.dumps(profile["reasoning_effort"])}',
        f'model_instructions_file={json.dumps(str(job_dir / ("prompt.md" if stage == "single" else "discovery.prompt.md")))}',
        'web_search="disabled"',
        "features.multi_agent=false", "features.apps=false", "features.plugins=false",
        "features.shell_tool=false", "features.browser_use=false",
        "features.computer_use=false", "features.image_generation=false",
        "features.view_image=false", "features.sleep_tool=false", "features.goals=false",
    ]
    args = ["codex", "-a", "never", "exec", "--ignore-user-config", "--strict-config",
            "--model", profile["model"], "--sandbox", "read-only", "--cd", str(job_dir),
            "--json", "--output-last-message", str(job_dir / ("discovery.json" if stage == "discovery" else "response.json"))]
    if stage == "ledger":
        thread = discovery_thread(job_dir, job)
        args = ["codex", "-a", "never", "exec", "--sandbox", "read-only", "--cd", str(job_dir),
                "resume", "--ignore-user-config", "--strict-config", "--model", profile["model"],
                "--json", "--output-last-message", str(job_dir / "response.json")]
    for value in config:
        args.extend(["-c", value])
    if stage == "ledger":
        args.append(thread)
    args.append("-")
    if stage == "discovery":
        filename = w.reader_filenames(job)[0]
        text = (EXISTING_OUTPUTS_LIMIT +
                "This is the discovery pass. The complete sealed packet follows. Follow the supplied "
                "discovery instructions and return only the lightweight discovery JSON. "
                "Do not call tools or read files; all evidence is included. The coordinator saves discovery.json.\n\n"
                f"<{filename}>\n" + (job_dir / filename).read_text() + f"</{filename}>\n")
        return job, args, text
    if stage == "ledger":
        filename = w.reader_filenames(job)[1]
        text = (EXISTING_OUTPUTS_LIMIT + (job_dir / "ledger.prompt.md").read_text() +
                f"\nThe assigned reader_id is {job['reader_id']}.\n\n" +
                f"<{filename}>\n" + (job_dir / filename).read_text() + f"</{filename}>\n")
        return job, args, text
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
    parser.add_argument("--stage", choices=("single", "discovery", "ledger"), default="single",
                        help="one explicit call only; ledger resumes the completed discovery session")
    args = parser.parse_args()
    job_dir = args.job_dir.resolve()
    w.require(job_dir.is_relative_to((w.WORKFLOW_ROOT / "runs").resolve()), "job must stay under HFT v2 runs")
    job, command, text = request(job_dir, args.stage)
    if args.inspect:
        print(json.dumps({"command": command, "stdin_bytes": len(text.encode("utf-8")),
                          "input_identity": job["input_identity"]}, ensure_ascii=False))
        return
    prefix = "inline" if args.stage == "single" else args.stage
    output_name = "discovery.json" if args.stage == "discovery" else "response.json"
    protected = [output_name, *(f"{prefix}.{suffix}" for suffix in ("launch.json", "events.jsonl", "stderr.log", "result.json"))]
    if args.stage == "discovery":
        protected.extend(["response.json", "evidence.json", "ledger.launch.json"])
    for name in protected:
        w.require(not (job_dir / name).exists(), f"refusing an existing artifact: {name}")
    launch = {"started_at": datetime.now(timezone.utc).isoformat(), "command": command,
              "input_identity": job["input_identity"], "stdin_sha256": w.digest(text.encode("utf-8")),
              "requested_profile": job["requested_profile"], "harness": "complete-inline-codex",
              "launcher_sha256": w.digest(Path(__file__).read_bytes()), "automatic_retry": False}
    if args.stage != "single":
        launch.update(stage=args.stage, two_stage_inputs=job["two_stage_inputs"])
    if args.stage == "ledger":
        launch.update(thread_id=discovery_thread(job_dir, job),
                      discovery_sha256=w.digest((job_dir / "discovery.json").read_bytes()))
    with (job_dir / f"{prefix}.launch.json").open("xb") as stream:
        stream.write(w.json_bytes(launch))
    with (job_dir / f"{prefix}.events.jsonl").open("xb") as events, (job_dir / f"{prefix}.stderr.log").open("xb") as errors:
        result = subprocess.run(command, input=text.encode("utf-8"), stdout=events, stderr=errors, check=False)
    receipt = {"finished_at": datetime.now(timezone.utc).isoformat(), "exit_code": result.returncode}
    if result.returncode == 0 and job["protocol"] == w.JOB_PROTOCOL and args.stage != "discovery":
        response_path = job_dir / "response.json"
        # V1 requests formatting-only compaction. The original model text also
        # remains in inline.events.jsonl; do not change fields or repair JSON.
        try:
            response_path.write_bytes(w.json_bytes(w.read_json(response_path)))
        except (ValueError, OSError) as error:
            receipt.update(exit_code=1, compaction_error=str(error))
    if receipt["exit_code"] == 0 and args.stage != "single":
        try:
            thread = completed_thread(job_dir / f"{prefix}.events.jsonl")
            if args.stage == "discovery":
                w.validate_discovery(w.read_json(job_dir / "discovery.json"))
                runtime = runtime_check(thread, job["requested_profile"], turns=1)
                receipt.update(thread_id=thread, discovery_sha256=w.digest((job_dir / "discovery.json").read_bytes()),
                               events_sha256=w.digest((job_dir / "discovery.events.jsonl").read_bytes()),
                               input_identity=job["input_identity"], two_stage_inputs=job["two_stage_inputs"],
                               requested_profile=job["requested_profile"], runtime=runtime)
            else:
                w.require(thread == launch["thread_id"], "ledger did not resume the discovery session")
                runtime = runtime_check(thread, job["requested_profile"], turns=2)
                # Content validation precedes the completion receipt; normal
                # validate/export also require that successful same-thread receipt.
                w.load_job(job_dir, require_ledger_completion=False)
                receipt.update(thread_id=thread, response_valid=True,
                               response_sha256=w.digest((job_dir / "response.json").read_bytes()), runtime=runtime)
        except (ValueError, OSError, KeyError, TypeError) as error:
            receipt.update(exit_code=1, validation_error=str(error))
    with (job_dir / f"{prefix}.result.json").open("xb") as stream:
        stream.write(w.json_bytes(receipt))
    print(json.dumps({"job_dir": str(job_dir), **receipt}))
    raise SystemExit(receipt["exit_code"])


if __name__ == "__main__":
    main()
