#!/usr/bin/env python3
"""Validate and hash a completed cold-reader run for later blind adjudication."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from validate_response import validate


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROMPT = REPO_ROOT / "v12" / "prompts" / "reader.md"
DEFAULT_SCHEMA = REPO_ROOT / "v12" / "schemas" / "reader-response.schema.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet-manifest", required=True, type=Path)
    parser.add_argument("--responses", required=True, type=Path)
    parser.add_argument("--readers", required=True, help="comma-separated reader IDs")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--reader-prompt", type=Path, default=DEFAULT_PROMPT)
    parser.add_argument("--response-schema", type=Path, default=DEFAULT_SCHEMA)
    args = parser.parse_args()

    args.packet_manifest = args.packet_manifest.resolve()
    args.responses = args.responses.resolve()
    args.output = args.output.resolve()
    args.reader_prompt = args.reader_prompt.resolve()
    args.response_schema = args.response_schema.resolve()

    readers = [item.strip() for item in args.readers.split(",") if item.strip()]
    if not readers or len(readers) != len(set(readers)):
        parser.error("--readers must contain unique reader IDs")

    packet_manifest = json.loads(args.packet_manifest.read_text(encoding="utf-8"))
    packet_dir = args.packet_manifest.parent
    frozen_readers: dict[str, list[dict[str, str | int]]] = {}
    for reader in readers:
        records: list[dict[str, str | int]] = []
        for stage, packet_name in enumerate(packet_manifest["stage_files"]):
            packet_path = packet_dir / packet_name
            response_path = args.responses / reader / f"stage_{stage:02d}.json"
            if not response_path.is_file():
                raise ValueError(f"missing response: {response_path}")
            packet = json.loads(packet_path.read_text(encoding="utf-8"))
            response = json.loads(response_path.read_text(encoding="utf-8"))
            if response["reader_id"] != reader:
                raise ValueError(f"reader ID mismatch: {response_path}")
            validate(packet, response)
            records.append(
                {
                    "stage": stage,
                    "path": str(response_path.relative_to(REPO_ROOT)),
                    "sha256": sha256(response_path),
                }
            )
        frozen_readers[reader] = records

    frozen = {
        "protocol": "cold-reading-v1",
        "packet_manifest": str(args.packet_manifest.relative_to(REPO_ROOT)),
        "packet_manifest_sha256": sha256(args.packet_manifest),
        "reader_prompt": str(args.reader_prompt.relative_to(REPO_ROOT)),
        "reader_prompt_sha256": sha256(args.reader_prompt),
        "response_schema": str(args.response_schema.relative_to(REPO_ROOT)),
        "response_schema_sha256": sha256(args.response_schema),
        "readers": frozen_readers,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(frozen, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"frozen run: {args.output}")


if __name__ == "__main__":
    main()
