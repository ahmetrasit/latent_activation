#!/usr/bin/env python3
"""Freeze an approved target-language baseline and its complete source bindings."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from validate_target_language_baseline import BaselineValidationError, validate
from workflow_common import atomic_write_json, read_json, sha256_file


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--qac", type=Path, required=True)
    parser.add_argument("--arabic", type=Path, required=True)
    parser.add_argument("--language-profile", type=Path, required=True)
    parser.add_argument("--methodology", type=Path, required=True)
    parser.add_argument(
        "--allow-partial-pilot",
        action="store_true",
        help="write an explicitly noncanonical pilot manifest without corpus completeness",
    )
    return parser.parse_args()


def freeze(
    baseline_path: Path,
    output_path: Path,
    qac_path: Path,
    arabic_path: Path,
    profile_path: Path,
    methodology_path: Path,
    *,
    partial_pilot: bool,
) -> dict:
    baseline_path = baseline_path.resolve()
    qac_path = qac_path.resolve()
    arabic_path = arabic_path.resolve()
    profile_path = profile_path.resolve()
    methodology_path = methodology_path.resolve()
    document = read_json(baseline_path)
    report = validate(
        baseline_path,
        qac_path,
        require_complete=not partial_pilot,
    )
    profile = read_json(profile_path)
    if profile.get("language") != document["language"]:
        raise BaselineValidationError("language profile and baseline language differ")
    manifest = {
        "protocol": "target-language-baseline-freeze-v1",
        "state": "partial_pilot" if partial_pilot else "canonical",
        "language": document["language"],
        "baseline_path": str(baseline_path),
        "baseline_sha256": sha256_file(baseline_path),
        "inputs": {
            "methodology": {"path": str(methodology_path), "sha256": sha256_file(methodology_path)},
            "language_profile": {"path": str(profile_path), "sha256": sha256_file(profile_path)},
            "arabic": {"path": str(arabic_path), "sha256": sha256_file(arabic_path)},
            "qac": {"path": str(qac_path), "sha256": sha256_file(qac_path)},
        },
        "validation": report,
    }
    atomic_write_json(output_path.resolve(), manifest)
    return manifest


def main() -> int:
    args = parse_args()
    try:
        manifest = freeze(
            args.baseline,
            args.output,
            args.qac,
            args.arabic,
            args.language_profile,
            args.methodology,
            partial_pilot=args.allow_partial_pilot,
        )
    except (OSError, ValueError, BaselineValidationError) as error:
        print(json.dumps({"frozen": False, "error": str(error)}, ensure_ascii=False, indent=2))
        return 1
    print(
        json.dumps(
            {
                "frozen": True,
                "state": manifest["state"],
                "language": manifest["language"],
                "baseline_sha256": manifest["baseline_sha256"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
