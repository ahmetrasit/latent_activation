#!/usr/bin/env python3
"""Hash a completed v12 full-context reader run for later comparison."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_packets import REPO_ROOT, sha256
from validate_full_context_packet import main as validate_main


def validate_packet(path: Path) -> None:
    import sys

    previous_argv = sys.argv
    try:
        sys.argv = ["validate_full_context_packet.py", str(path)]
        validate_main()
    finally:
        sys.argv = previous_argv


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", required=True, type=Path)
    parser.add_argument("--prompt", required=True, type=Path)
    parser.add_argument("--output-file", required=True, type=Path)
    parser.add_argument("--freeze", required=True, type=Path)
    parser.add_argument("--reader-id", default="")
    args = parser.parse_args()

    for path in (args.packet, args.prompt, args.output_file):
        if not path.is_file():
            parser.error(f"file not found: {path}")

    validate_packet(args.packet)
    frozen = {
        "protocol": "v12-full-context-run-v1",
        "reader_id": args.reader_id,
        "packet": rel(args.packet),
        "packet_sha256": sha256(args.packet),
        "prompt": rel(args.prompt),
        "prompt_sha256": sha256(args.prompt),
        "output_file": rel(args.output_file),
        "output_file_sha256": sha256(args.output_file),
    }
    args.freeze.parent.mkdir(parents=True, exist_ok=True)
    args.freeze.write_text(
        json.dumps(frozen, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"frozen full-context run: {args.freeze}")


if __name__ == "__main__":
    main()
