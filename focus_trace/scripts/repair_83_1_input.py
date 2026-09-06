#!/usr/bin/env python3
"""Repair the saved v1 83:1 packet without changing unrelated packet evidence."""

import copy
import json
from pathlib import Path

import build_focus_trace_packet as builder
import validate_focus_trace as validator


def repaired_packet(original: dict) -> dict:
    if original["focus_ref"] != "83:1" or original["protocol"] != builder.PROTOCOL:
        raise ValueError("expected the rich v1 83:1 packet")
    root = "ط ف ف"
    mappings = builder.load_root_mappings(builder.DEFAULT_QAC_FURUQ_ROOT_MAP, [root])
    builder.validate_repair_occurrences([original["focus_ayah"]], mappings)
    branches, missing, missing_targets = builder.load_branches_for_mapped_roots(
        builder.DEFAULT_BRANCH_DB, mappings,
    )
    if missing or missing_targets or len(branches[root]) != 10:
        raise ValueError("reviewed target must supply its ten non-contaminated branches")
    result = copy.deepcopy(original)
    inventory = {
        "root": root,
        "root_mapping": builder.root_mapping_summary(mappings[root]),
        "source_phrases": builder.source_phrases([result["focus_ayah"]], root),
        "branches": [builder.focus_branch(branch) for branch in branches[root]],
    }
    if result["focus_branch_inventories"] and result["focus_branch_inventories"] != [inventory]:
        raise ValueError("unexpected existing focus inventory; review before replacing")
    result["focus_branch_inventories"] = [inventory]
    result["root_mappings"] = [
        builder.root_mapping_summary(mappings[root]) if row["qac_root"] == root else row
        for row in result["root_mappings"]
    ]
    result["missing_branch_inventories"] = [
        row for row in result["missing_branch_inventories"] if row["root"] != root
    ]
    result["provenance"]["resource_sha256"][builder.resource_key(builder.ROOT_MAPPING_REPAIRS)] = (
        builder.sha256(builder.ROOT_MAPPING_REPAIRS)
    )
    result["provenance"]["reviewed_input_repair"] = "83-1-accepted-masaq-alignment-20260906"
    validator.validate_packet(result)
    return result


def main() -> None:
    path = builder.WORKFLOW_ROOT / "runs/s83/packets/83_1.packet.json"
    archive = builder.WORKFLOW_ROOT / "repairs/83_1/original.packet.json"
    original_bytes = path.read_bytes()
    # The archived original is the baseline even when refreshing a derived repair.
    original = json.loads(archive.read_bytes() if archive.exists() else original_bytes)
    repaired = repaired_packet(original)
    if repaired == json.loads(original_bytes):
        print("83:1 input is already repaired")
        return
    archive.parent.mkdir(parents=True, exist_ok=True)
    if archive.exists():
        # Refuse to erase unrelated edits made since the previous scoped repair.
        current = json.loads(original_bytes)
        def outside_repair(packet):
            remaining = copy.deepcopy(packet)
            for collection, root_key in (("focus_branch_inventories", "root"), ("root_mappings", "qac_root"), ("missing_branch_inventories", "root")):
                remaining[collection] = [row for row in remaining[collection] if row[root_key] != "ط ف ف"]
            remaining["provenance"].pop("reviewed_input_repair", None)
            remaining["provenance"]["resource_sha256"].pop(builder.resource_key(builder.ROOT_MAPPING_REPAIRS), None)
            return remaining
        if outside_repair(current) != outside_repair(original):
            raise ValueError("packet changed outside the ط ف ف repair scope")
    else:
        archive.write_bytes(original_bytes)
    path.write_text(json.dumps(repaired, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"Repaired {path}: ط ف ف -> root_000940, ten branches; original saved at {archive}")


if __name__ == "__main__":
    main()
