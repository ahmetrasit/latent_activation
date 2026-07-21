#!/usr/bin/env python3
"""Compute the canonical ordered-path-and-bytes fingerprint for stage files."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    digest = hashlib.sha256()
    for raw_path in args.paths:
        path = raw_path.resolve()
        content = path.read_bytes()
        name = raw_path.as_posix().encode("utf-8")
        digest.update(len(name).to_bytes(8, "big"))
        digest.update(name)
        digest.update(len(content).to_bytes(8, "big"))
        digest.update(content)
    print(digest.hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
