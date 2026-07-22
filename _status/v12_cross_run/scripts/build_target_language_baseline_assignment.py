#!/usr/bin/env python3
"""Build one hash-bound target-language baseline authoring assignment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from workflow_common import (
    REPO_ROOT,
    atomic_write_compact_json,
    read_json,
    repo_relative,
    sha256_file,
)


BASELINE_ROOT = REPO_ROOT / "_status" / "v12_cross_run" / "baseline"
AUTHOR_PROMPT_PATH = BASELINE_ROOT / "prompts" / "author_baseline.md"
METHODOLOGY_PATH = BASELINE_ROOT / "methodology" / "ordinary_baseline_v1.md"
SCHEMA_PATH = (
    REPO_ROOT
    / "_status"
    / "v12_cross_run"
    / "model_schemas"
    / "target_language_baseline_v1.json"
)
VALIDATOR_PATH = (
    REPO_ROOT
    / "_status"
    / "v12_cross_run"
    / "scripts"
    / "validate_target_language_baseline.py"
)
DOWNSTREAM_ARABIC_PATH = REPO_ROOT / "resources" / "quran" / "complete-quran.txt"
DOWNSTREAM_QAC_PATH = REPO_ROOT / "resources" / "qac.sqlite"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("surah", type=int, choices=range(1, 115), metavar="SURAH")
    parser.add_argument("--language", required=True)
    parser.add_argument("--arabic", type=Path, required=True)
    parser.add_argument("--qac", type=Path, required=True)
    parser.add_argument("--assignment", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--resume", action="store_true")
    return parser.parse_args()


def bound_path(path: Path) -> dict[str, str]:
    resolved = path.resolve()
    if not resolved.is_file():
        raise ValueError(f"assignment input does not exist: {resolved}")
    try:
        rendered = repo_relative(resolved)
    except ValueError:
        rendered = str(resolved)
    return {"path": rendered, "sha256": sha256_file(resolved)}


def build(args: argparse.Namespace) -> tuple[Path, dict]:
    tag = f"s{args.surah:03d}"
    workspace = REPO_ROOT / "_status" / "v12_cross_run" / tag
    assignment_path = (
        args.assignment.resolve()
        if args.assignment
        else workspace / f"baseline_assignment.{args.language}.json"
    )
    output_path = (
        args.output.resolve()
        if args.output
        else BASELINE_ROOT
        / "artifacts"
        / f"quran-{args.language}-baseline-v1-{tag}.json"
    )
    repo_relative(assignment_path)
    repo_relative(output_path)

    profile_path = BASELINE_ROOT / "language_profiles" / f"{args.language}.json"
    profile = read_json(profile_path)
    if profile.get("language") != args.language:
        raise ValueError("language profile does not match requested language")
    if sha256_file(args.arabic.resolve()) != sha256_file(DOWNSTREAM_ARABIC_PATH):
        raise ValueError(
            "Arabic authoring source differs from the project-owned downstream mirror"
        )
    if sha256_file(args.qac.resolve()) != sha256_file(DOWNSTREAM_QAC_PATH):
        raise ValueError(
            "QAC authoring source differs from the project-owned downstream mirror"
        )

    assignment = {
        "protocol": "target-language-baseline-assignment-v1",
        "scope": {"surah": args.surah},
        "language": args.language,
        "inputs": {
            "author_prompt": bound_path(AUTHOR_PROMPT_PATH),
            "methodology": bound_path(METHODOLOGY_PATH),
            "language_profile": bound_path(profile_path),
            "arabic_source": bound_path(args.arabic),
            "qac": bound_path(args.qac),
            "schema": bound_path(SCHEMA_PATH),
            "validator": bound_path(VALIDATOR_PATH),
        },
        "output": repo_relative(output_path),
        "checkpoint": repo_relative(
            workspace / f"baseline_checkpoint.{args.language}.json"
        ),
        "read_existing_output": args.resume,
        "validation_command": [
            "python3",
            repo_relative(VALIDATOR_PATH),
            repo_relative(output_path),
            "--surah",
            str(args.surah),
            "--qac",
            str(args.qac.resolve()),
        ],
    }
    atomic_write_compact_json(assignment_path, assignment)
    return assignment_path, assignment


def main() -> int:
    args = parse_args()
    try:
        assignment_path, assignment = build(args)
    except (OSError, ValueError) as error:
        print(json.dumps({"ready": False, "error": str(error)}, ensure_ascii=False))
        return 1
    print(
        json.dumps(
            {
                "ready": True,
                "assignment": repo_relative(assignment_path),
                "output": assignment["output"],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
