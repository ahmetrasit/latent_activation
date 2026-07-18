#!/usr/bin/env python3
"""Hash a v12 adjudication report and the frozen reader runs it compares."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_packets import REPO_ROOT, sha256


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--adjudicator-prompt", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--reader-runs", required=True, help="comma-separated frozen_run.json paths")
    parser.add_argument("--freeze", required=True, type=Path)
    args = parser.parse_args()

    reader_runs = [Path(item.strip()) for item in args.reader_runs.split(",") if item.strip()]
    if not reader_runs:
        parser.error("--reader-runs must include at least one frozen run")

    for path in [args.adjudicator_prompt, args.report, *reader_runs]:
        if not path.is_file():
            parser.error(f"file not found: {path}")

    frozen = {
        "protocol": "v12-adjudication-report-v1",
        "adjudicator_prompt": rel(args.adjudicator_prompt),
        "adjudicator_prompt_sha256": sha256(args.adjudicator_prompt),
        "report": rel(args.report),
        "report_sha256": sha256(args.report),
        "reader_runs": [
            {
                "path": rel(path),
                "sha256": sha256(path),
            }
            for path in reader_runs
        ],
    }
    args.freeze.parent.mkdir(parents=True, exist_ok=True)
    args.freeze.write_text(
        json.dumps(frozen, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"frozen adjudication report: {args.freeze}")


if __name__ == "__main__":
    main()
