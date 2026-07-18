#!/usr/bin/env python3
"""Report branch-inventory coverage for a v12 surah or ayah window."""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import tempfile
from pathlib import Path

from build_full_context_packet import main as build_main


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--surah", help="surah number, e.g. 100")
    source.add_argument("--window", help="comma-separated ayah refs")
    args = parser.parse_args()

    with tempfile.TemporaryDirectory() as tmpdir:
        packet_path = Path(tmpdir) / "full_context_packet.json"
        import sys

        previous_argv = sys.argv
        try:
            sys.argv = [
                "build_full_context_packet.py",
                "--output",
                str(packet_path),
            ]
            if args.surah:
                sys.argv.extend(["--surah", args.surah])
            else:
                sys.argv.extend(["--window", args.window])
            with contextlib.redirect_stdout(io.StringIO()):
                build_main()
        finally:
            sys.argv = previous_argv

        packet = json.loads(packet_path.read_text(encoding="utf-8"))

    missing = packet.get("missing_branch_inventories", [])
    print(f"window ayat: {packet['ayah_count']}")
    print(f"roots with branch inventory: {len(packet['branch_inventories'])}")
    print(f"roots missing branch inventory: {len(missing)}")
    for item in missing:
        refs = ",".join(item["refs"])
        print(f"- {item['root']}: {refs}")


if __name__ == "__main__":
    main()
