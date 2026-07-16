#!/usr/bin/env python3
"""Emit the four static task files for a prepared GSLS V3 run."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable


PACKAGE_ROOT = Path(__file__).resolve().parents[1]


class TaskError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_root", type=Path)
    return parser.parse_args()


def require_files(paths: Iterable[Path], label: str) -> list[Path]:
    materialized = list(paths)
    missing = [str(path) for path in materialized if not path.is_file()]
    if missing:
        raise TaskError(f"Missing {label}: {', '.join(missing)}")
    return materialized


def passage_surah(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        location = line.partition("\t")[0]
        surah, separator, _ayah = location.partition(":")
        if separator and surah.isdigit():
            return str(int(surah))
    raise TaskError(f"Cannot determine surah from passage input: {path}")


def task_text(
    title: str,
    session: str,
    prompt: Path,
    inputs: Iterable[Path],
    output: Path,
) -> str:
    lines = [
        f"# {title}",
        "",
        f"SESSION: {session}",
        f"ROLE_PROMPT: {prompt}",
        "",
        "Read the role prompt in full and follow it as the intellectual method for this turn.",
        "Use only the evidence and work products listed below. Do not read the gold reference, prior target outputs, translations, the v1 tree, or unlisted repository files.",
        "",
        "## Inputs",
        "",
        *[f"- {path}" for path in inputs],
        "",
        "## Output",
        "",
        f"- {output}",
        "",
        "Write the complete artifact directly to the output path.",
        "",
    ]
    if output.suffix == ".jsonl":
        validator = PACKAGE_ROOT / "scripts" / "render_publication.py"
        lines.extend(
            [
                "## Deterministic Check",
                "",
                "After writing the JSONL, run:",
                "",
                "```bash",
                f"python3 {validator} {output} --check",
                "```",
                "",
                "Resolve every structural or content-contract error before reporting completion. Resolve actionable style warnings through presentation-only rewriting. Preserve the established synthesis hierarchy, complete graded finding coverage, and exact grades; never split a synthesized finding into evidence-sized records merely to satisfy formatting or style checks.",
                "",
            ]
        )
    return "\n".join(lines)


def emit(run_root: Path) -> list[Path]:
    run_root = run_root.resolve()
    inputs_root = run_root / "inputs"
    passage, morphology, syntax, lexical, scaffold = require_files(
        (
            inputs_root / "passage-arabic.txt",
            inputs_root / "morphology.tsv",
            inputs_root / "syntax.tsv",
            inputs_root / "lexical-branches.jsonl",
            inputs_root / "primary-scaffold.md",
        ),
        "prepared input",
    )

    prompts = {
        "discover": PACKAGE_ROOT / "prompts" / "a1-discovery.md",
        "integrate": PACKAGE_ROOT / "prompts" / "a1-scaffold-integration.md",
        "map": PACKAGE_ROOT / "prompts" / "a2-mechanism-map.md",
        "publish": PACKAGE_ROOT / "prompts" / "a2-publication-tr-audio-first.md",
    }
    require_files(prompts.values(), "role prompt")

    tasks_root = run_root / "tasks"
    tasks_root.mkdir(parents=True, exist_ok=True)
    discovery = run_root / "a1" / "discovery.md"
    integrated = run_root / "a1" / "discovery-integrated.md"
    mechanism = run_root / "a2" / "mechanism-map.md"
    publication = run_root / f"{passage_surah(passage)}-publication.jsonl"

    definitions = (
        (
            tasks_root / "01-a1-discover.md",
            "A1 Turn 1: Whole-Passage Latent Discovery",
            "fresh A1 agent session",
            prompts["discover"],
            (passage, morphology, syntax, lexical),
            discovery,
        ),
        (
            tasks_root / "02-a1-integrate.md",
            "A1 Turn 2: Scaffold Integration",
            "continue the same A1 session used for task 01",
            prompts["integrate"],
            (passage, morphology, syntax, lexical, discovery, scaffold),
            integrated,
        ),
        (
            tasks_root / "03-a2-map.md",
            "A2 Turn 1: Passage-Scale Mechanism Map",
            "fresh A2 agent session",
            prompts["map"],
            (passage, morphology, syntax, lexical, scaffold, integrated),
            mechanism,
        ),
        (
            tasks_root / "04-a2-publish.md",
            "Fresh Gold Renderer: Audio-First Turkish Publication",
            "fresh context-free gold renderer agent session; do not continue the A2 session",
            prompts["publish"],
            (passage, scaffold, integrated, mechanism),
            publication,
        ),
    )

    written: list[Path] = []
    for path, title, session, prompt, inputs, output in definitions:
        path.write_text(task_text(title, session, prompt, inputs, output), encoding="utf-8")
        written.append(path)
    return written


def main() -> int:
    try:
        paths = emit(parse_args().run_root)
    except (TaskError, OSError, ValueError) as error:
        print(f"make_tasks: ERROR: {error}", file=sys.stderr)
        return 1
    print(json.dumps({"tasks": [str(path) for path in paths]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
