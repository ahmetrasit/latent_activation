#!/usr/bin/env python3
"""Lean state controller and task emitter for GSLS 2.1."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

from common import PACKAGE_ROOT, WORKFLOW_ID, ContractError, atomic_write_text, load_json, utc_now, write_json
from validate_run import (
    validate_draft,
    validate_final,
    validate_inputs,
    validate_publication,
    validate_review,
)


MACHINE_PATH = PACKAGE_ROOT / "orchestrator-state-machine.json"

AGENT_INPUTS = {
    "A_SYNTHESIZE": (
        "inputs/run-card.json",
        "inputs/passage-arabic.txt",
        "inputs/primary-scaffold.md",
        "inputs/morphology.tsv",
        "inputs/syntax.tsv",
        "inputs/lexical-branches.jsonl",
        "inputs/input-summary.json",
    ),
    "B_REVIEW": (
        "inputs/run-card.json",
        "inputs/passage-arabic.txt",
        "inputs/primary-scaffold.md",
        "inputs/morphology.tsv",
        "inputs/syntax.tsv",
        "inputs/lexical-branches.jsonl",
        "inputs/input-summary.json",
    ),
    "A_REVISE": (
        "inputs/run-card.json",
        "inputs/passage-arabic.txt",
        "inputs/primary-scaffold.md",
        "inputs/morphology.tsv",
        "inputs/syntax.tsv",
        "inputs/lexical-branches.jsonl",
        "inputs/input-summary.json",
    ),
    "C_RENDER": (
        "inputs/run-card.json",
        "inputs/passage-arabic.txt",
    ),
}

UPSTREAM_OUTPUTS = {
    "B_REVIEW": (
        "agent-a/draft/draft-synthesis.jsonl",
        "agent-a/draft/draft-synthesis.md",
    ),
    "A_REVISE": (
        "agent-a/draft/draft-synthesis.jsonl",
        "agent-a/draft/draft-synthesis.md",
        "agent-b/review.md",
    ),
    "C_RENDER": (
        "agent-a/final/final-synthesis.jsonl",
        "agent-a/final/final-synthesis.md",
    ),
}

CONTROL_SCHEMAS = {
    "A_SYNTHESIZE": ("schemas/synthesis-finding.schema.json",),
    "B_REVIEW": ("schemas/synthesis-finding.schema.json",),
    "A_REVISE": ("schemas/synthesis-finding.schema.json",),
    "C_RENDER": (),
}

TASK_NAMES = {
    "A_SYNTHESIZE": "a-synthesize.md",
    "B_REVIEW": "b-review.md",
    "A_REVISE": "a-revise.md",
    "C_RENDER": "c-render.md",
}


def machine() -> dict[str, Any]:
    value = load_json(MACHINE_PATH)
    if not isinstance(value, dict) or value.get("workflow_id") != WORKFLOW_ID:
        raise ContractError("State-machine workflow mismatch")
    return value


def state_path(run_root: Path) -> Path:
    return run_root.resolve() / "logs" / "orchestrator-state.json"


def load_state(run_root: Path) -> dict[str, Any]:
    run_root = run_root.resolve()
    path = state_path(run_root)
    if not path.is_file():
        raise ContractError(f"Orchestrator is not initialized: {path}")
    value = load_json(path)
    if not isinstance(value, dict):
        raise ContractError("Orchestrator state must be a JSON object")
    required = {"workflow_id", "run_id", "state", "quality_tier", "optional_product"}
    if required - value.keys():
        raise ContractError("Orchestrator state is incomplete")
    card = load_json(run_root / "inputs" / "run-card.json")
    if value.get("workflow_id") != WORKFLOW_ID or value.get("run_id") != card.get("run_id"):
        raise ContractError("Orchestrator state does not match the run card")
    if value.get("quality_tier") != card.get("quality_tier"):
        raise ContractError("Orchestrator quality tier does not match the run card")
    if value.get("optional_product") != card.get("optional_product"):
        raise ContractError("Orchestrator optional product does not match the run card")
    config = machine()
    if value.get("state") not in set(config["states"]) | set(config["terminal"]):
        raise ContractError(f"Unknown orchestrator state: {value.get('state')}")
    return value


def save_state(run_root: Path, value: dict[str, Any]) -> None:
    value["updated_at"] = utc_now()
    write_json(state_path(run_root), value)


def initialize(run_root: Path) -> dict[str, Any]:
    run_root = run_root.resolve()
    path = state_path(run_root)
    if path.exists():
        raise ContractError(f"Orchestrator is already initialized: {path}")
    report = validate_inputs(run_root)
    card = load_json(run_root / "inputs" / "run-card.json")
    now = utc_now()
    state = {
        "workflow_id": WORKFLOW_ID,
        "run_id": card["run_id"],
        "state": "A_SYNTHESIZE" if report.passed else "BLOCKED_INPUT",
        "quality_tier": card["quality_tier"],
        "optional_product": card["optional_product"],
        "created_at": now,
        "updated_at": now,
    }
    save_state(run_root, state)
    return state


def _existing_paths(run_root: Path, relative_paths: tuple[str, ...], label: str) -> list[Path]:
    paths = [run_root / relative for relative in relative_paths]
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise ContractError(f"Missing {label}: {', '.join(missing)}")
    return paths


def emit_task(run_root: Path) -> Path:
    run_root = run_root.resolve()
    state = load_state(run_root)
    state_name = state["state"]
    config = machine()
    if state_name in config["terminal"]:
        raise ContractError(f"Terminal state has no task: {state_name}")
    state_config = config["states"].get(state_name)
    if not state_config or state_config.get("agent") is None:
        raise ContractError(f"State has no agent task: {state_name}")

    prompt = PACKAGE_ROOT / state_config["prompt"]
    if not prompt.is_file():
        raise ContractError(f"Missing role prompt: {prompt}")
    evidence = _existing_paths(run_root, AGENT_INPUTS[state_name], "prepared inputs")
    upstream = _existing_paths(run_root, UPSTREAM_OUTPUTS.get(state_name, ()), "upstream outputs")
    controls = _existing_paths(PACKAGE_ROOT, CONTROL_SCHEMAS[state_name], "control schemas")

    task_path = run_root / "tasks" / TASK_NAMES[state_name]
    lines = [
        f"WORKFLOW_ID: {WORKFLOW_ID}",
        f"RUN_ID: {state['run_id']}",
        f"AGENT_ID: {state_config['agent']}",
        f"STATE: {state_name}",
        f"RUN_ROOT: {run_root}",
        f"ROLE_PROMPT: {prompt}",
        "",
        "Read the role prompt in full.",
        "",
        "## Evidence inputs",
        "",
        *[f"- {path}" for path in evidence],
        "",
        "## Work products to review or revise",
        "",
        *([f"- {path}" for path in upstream] or ["- none"]),
        "",
        "## Control files",
        "",
        *([f"- {path}" for path in controls] or ["- none"]),
        "",
        "Control files define output shape; they are not evidence.",
        "Raw resources, V1 outputs, translations, prior target prose, and unlisted files are prohibited.",
        "",
    ]
    atomic_write_text(task_path, "\n".join(lines))
    return task_path


def _validate_transition_output(run_root: Path, state_name: str, event: str) -> None:
    report = None
    if state_name == "A_SYNTHESIZE" and event == "complete":
        report = validate_draft(run_root)
    elif state_name == "B_REVIEW":
        report = validate_review(run_root, expected_verdict=event.replace("_", "-"))
    elif state_name == "A_REVISE" and event == "complete":
        report = validate_final(run_root)
    elif state_name == "C_RENDER" and event == "complete":
        report = validate_publication(run_root)
    if report is not None:
        if not report.passed:
            raise ContractError(f"{state_name} output failed: {'; '.join(report.errors[:3])}")


def _finalize(run_root: Path, state: dict[str, Any], promote_draft: bool) -> None:
    final_dir = run_root / "agent-a" / "final"
    final_dir.mkdir(parents=True, exist_ok=True)
    if promote_draft:
        draft_dir = run_root / "agent-a" / "draft"
        shutil.copyfile(draft_dir / "draft-synthesis.jsonl", final_dir / "final-synthesis.jsonl")
        shutil.copyfile(draft_dir / "draft-synthesis.md", final_dir / "final-synthesis.md")
    report = validate_final(run_root)
    if not report.passed:
        raise ContractError(f"Final synthesis failed: {'; '.join(report.errors[:3])}")
    state["state"] = "C_RENDER" if state["optional_product"] == "publication-essay" else "DONE"


def transition(run_root: Path, event: str) -> dict[str, Any]:
    run_root = run_root.resolve()
    state = load_state(run_root)
    config = machine()
    source = state["state"]
    source_config = config["states"].get(source)
    if source_config is None or source_config.get("agent") is None:
        raise ContractError(f"Cannot transition state: {source}")
    transitions = source_config.get("transitions", {})
    if event not in transitions:
        raise ContractError(f"Invalid event {event!r} for {source}; expected {sorted(transitions)}")

    _validate_transition_output(run_root, source, event)
    target = transitions[event]
    state["state"] = target
    if target == "FINALIZE":
        _finalize(run_root, state, promote_draft=source == "B_REVIEW" and event == "clean")
    save_state(run_root, state)
    return state


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("init", "status", "task"):
        item = subparsers.add_parser(command)
        item.add_argument("run_root", type=Path)
    advance = subparsers.add_parser("transition")
    advance.add_argument("run_root", type=Path)
    advance.add_argument("event")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_root = args.run_root.resolve()
    try:
        if args.command == "init":
            result: Any = initialize(run_root)
        elif args.command == "status":
            result = load_state(run_root)
        elif args.command == "task":
            result = {"task_path": str(emit_task(run_root))}
        elif args.command == "transition":
            result = transition(run_root, args.event)
        else:
            raise AssertionError(args.command)
    except (ContractError, OSError, ValueError, json.JSONDecodeError) as error:
        print(f"orchestrate: ERROR: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
