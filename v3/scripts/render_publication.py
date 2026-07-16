#!/usr/bin/env python3
"""Validate a V3 publication JSONL file and render its Markdown derivative."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from publication_contract import (
    PublicationError,
    load_publication,
    render_markdown,
    style_warnings,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--strict-style", action="store_true")
    return parser.parse_args()


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, path)


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    output = (args.output or source.with_suffix(".md")).resolve()
    try:
        records = load_publication(source)
        warnings = style_warnings(records)
    except (PublicationError, OSError) as error:
        print(f"render_publication: ERROR: {error}", file=sys.stderr)
        return 1

    report = {
        "source": str(source),
        "output": None if args.check else str(output),
        "records": len(records),
        "findings": sum(record["kind"] == "finding" for record in records),
        "warnings": warnings,
    }
    if args.strict_style and warnings:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 2
    if not args.check:
        atomic_write_text(output, render_markdown(records))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
