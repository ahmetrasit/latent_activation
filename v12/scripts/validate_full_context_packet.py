#!/usr/bin/env python3
"""Validate a v12 full-context packet against its own provenance."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_packets import REPO_ROOT, ordered_unique, sha256


AYAH_KEYS = {
    "ref",
    "text_ar",
    "text_norm_ar",
    "translation_en",
    "root_sequence",
    "root_occurrences",
}
OCCURRENCE_KEYS = {
    "root",
    "occurrence_count",
    "word_indices",
    "surfaces_ar",
    "lemmas_ar",
    "pos_tags",
}
BRANCH_KEYS = {"branch_id", "image_ar", "image_en", "scope_ar", "scope_en"}
MISSING_KEYS = {"root", "refs", "reason"}


def require_keys(record: dict, keys: set[str], label: str) -> None:
    missing = keys - record.keys()
    if missing:
        raise ValueError(f"{label}: missing keys {sorted(missing)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    args = parser.parse_args()

    packet = json.loads(args.packet.read_text(encoding="utf-8"))
    if packet.get("protocol") != "v12-full-context-v1":
        raise ValueError("packet protocol is not v12-full-context-v1")

    window = packet.get("window")
    ayat = packet.get("ayat")
    if not isinstance(window, list) or not window:
        raise ValueError("window must be a non-empty list")
    if not isinstance(ayat, list) or len(ayat) != len(window):
        raise ValueError("ayat must match window length")
    if [ayah.get("ref") for ayah in ayat] != window:
        raise ValueError("ayah refs do not match window order")
    if packet.get("ayah_count") != len(window):
        raise ValueError("ayah_count does not match window")
    for index, ayah in enumerate(ayat):
        require_keys(ayah, AYAH_KEYS, f"ayat[{index}]")
        if not isinstance(ayah["translation_en"], str):
            raise ValueError(f"ayat[{index}].translation_en must be a string")
        if not isinstance(ayah["root_occurrences"], list) or not ayah["root_occurrences"]:
            raise ValueError(f"ayat[{index}].root_occurrences must be a non-empty list")
        for occurrence_index, occurrence in enumerate(ayah["root_occurrences"]):
            require_keys(
                occurrence,
                OCCURRENCE_KEYS,
                f"ayat[{index}].root_occurrences[{occurrence_index}]",
            )

    expected_roots = ordered_unique(
        occurrence["root"]
        for ayah in ayat
        for occurrence in ayah["root_occurrences"]
    )
    inventories = packet.get("branch_inventories")
    if not isinstance(inventories, list):
        raise ValueError("branch_inventories must be a list")
    actual_roots = [item.get("root") for item in inventories]
    if len(actual_roots) != len(set(actual_roots)):
        raise ValueError("duplicate root in branch_inventories")

    for inventory_index, inventory in enumerate(inventories):
        require_keys(inventory, {"root", "branches"}, f"branch_inventories[{inventory_index}]")
        branches = inventory.get("branches")
        if not isinstance(branches, list) or not branches:
            raise ValueError(f"empty branch inventory for {inventory.get('root')}")
        ids = [branch.get("branch_id") for branch in branches]
        if len(ids) != len(set(ids)):
            raise ValueError(f"duplicate branch ID for {inventory.get('root')}")
        for branch_index, branch in enumerate(branches):
            require_keys(
                branch,
                BRANCH_KEYS,
                f"branch_inventories[{inventory_index}].branches[{branch_index}]",
            )

    missing = packet.get("missing_branch_inventories", [])
    if not isinstance(missing, list):
        raise ValueError("missing_branch_inventories must be a list")
    missing_roots = [item.get("root") for item in missing]
    if len(missing_roots) != len(set(missing_roots)):
        raise ValueError("duplicate root in missing_branch_inventories")
    for missing_index, item in enumerate(missing):
        require_keys(item, MISSING_KEYS, f"missing_branch_inventories[{missing_index}]")
        if not isinstance(item["refs"], list) or not item["refs"]:
            raise ValueError(f"missing_branch_inventories[{missing_index}].refs must be non-empty")
        invalid_refs = [ref for ref in item["refs"] if ref not in window]
        if invalid_refs:
            raise ValueError(
                f"missing_branch_inventories[{missing_index}].refs outside window: {invalid_refs}"
            )

    expected_available = [root for root in expected_roots if root not in set(missing_roots)]
    if actual_roots != expected_available:
        raise ValueError("branch inventories do not match first-seen available root order")
    if [root for root in expected_roots if root not in set(actual_roots)] != missing_roots:
        raise ValueError("missing roots do not match first-seen missing root order")

    resource_hashes = packet["provenance"]["resource_sha256"]
    for resource, expected_hash in resource_hashes.items():
        path = REPO_ROOT / resource
        if sha256(path) != expected_hash:
            raise ValueError(f"resource hash changed: {resource}")

    print(f"valid full-context packet: {args.packet}")


if __name__ == "__main__":
    main()
