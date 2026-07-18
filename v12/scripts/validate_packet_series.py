#!/usr/bin/env python3
"""Check cumulative reveal order, branch coverage, and hashes for a packet series."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]


def ordered_unique(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    base = args.manifest.parent
    expected_sequence = [manifest["focus_ref"], *manifest["reveal_order"]]
    if len(manifest["stage_files"]) != len(expected_sequence):
        raise ValueError("manifest stage count does not match reveal sequence")

    for resource, expected_hash in manifest["resource_sha256"].items():
        path = REPO_ROOT / resource
        if sha256(path) != expected_hash:
            raise ValueError(f"resource hash changed: {resource}")

    for stage, filename in enumerate(manifest["stage_files"]):
        packet = json.loads((base / filename).read_text(encoding="utf-8"))
        expected_refs = expected_sequence[: stage + 1]
        if packet["stage"] != stage:
            raise ValueError(f"{filename}: incorrect stage number")
        if packet["revealed_refs"] != expected_refs:
            raise ValueError(f"{filename}: future leak or incorrect reveal order")
        if packet["newly_revealed_ref"] != expected_sequence[stage]:
            raise ValueError(f"{filename}: incorrect newly revealed ayah")
        if packet["hidden_ref_count"] != len(expected_sequence) - stage - 1:
            raise ValueError(f"{filename}: incorrect hidden ref count")
        if [ayah["ref"] for ayah in packet["ayat"]] != expected_refs:
            raise ValueError(f"{filename}: ayah payload does not match revealed refs")

        expected_roots = ordered_unique(
            occurrence["root"]
            for ayah in packet["ayat"]
            for occurrence in ayah["root_occurrences"]
        )
        actual_roots = [item["root"] for item in packet["branch_inventories"]]
        if actual_roots != expected_roots:
            raise ValueError(f"{filename}: branch inventories do not match revealed roots")
        for inventory in packet["branch_inventories"]:
            ids = [branch["branch_id"] for branch in inventory["branches"]]
            if not ids:
                raise ValueError(f"{filename}: empty inventory for {inventory['root']}")
            if len(ids) != len(set(ids)):
                raise ValueError(f"{filename}: duplicate branch ID for {inventory['root']}")
        if packet["provenance"]["resource_sha256"] != manifest["resource_sha256"]:
            raise ValueError(f"{filename}: provenance differs from manifest")

    print(f"valid packet series: {args.manifest}")


if __name__ == "__main__":
    main()
