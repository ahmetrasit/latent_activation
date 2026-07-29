#!/usr/bin/env python3
"""Validate a hermetic focus-trace packet and optional reader response."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

WORKFLOW_ROOT = Path(__file__).resolve().parents[1]
LATENT_ROOT = WORKFLOW_ROOT.parent
V12_SCRIPTS = LATENT_ROOT / "v12" / "scripts"
if str(V12_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(V12_SCRIPTS))

from build_packets import REPO_ROOT, ordered_unique, sha256


PACKET_PROTOCOL = "focus-trace-hermetic-packet-v2"
PACKET_PROTOCOL_V1 = "focus-trace-hermetic-packet-v1"
LEGACY_PACKET_PROTOCOL = "v12-hermetic-focus-trace-packet-v1"
PACKET_PROTOCOLS = {PACKET_PROTOCOL, PACKET_PROTOCOL_V1, LEGACY_PACKET_PROTOCOL}
RESPONSE_PROTOCOL_V1 = "focus-trace-hermetic-response-v1"
RESPONSE_PROTOCOL_V2 = "focus-trace-hermetic-response-v2"
RESPONSE_PROTOCOL_V3 = "focus-trace-hermetic-response-v3"
RESPONSE_PROTOCOL_V4 = "focus-trace-hermetic-response-v4"
LEGACY_RESPONSE_PROTOCOL_V1 = "v12-hermetic-focus-trace-response-v1"
LEGACY_RESPONSE_PROTOCOL_V2 = "v12-hermetic-focus-trace-response-v2"
RESPONSE_PROTOCOLS = {
    RESPONSE_PROTOCOL_V1,
    RESPONSE_PROTOCOL_V2,
    RESPONSE_PROTOCOL_V3,
    RESPONSE_PROTOCOL_V4,
    LEGACY_RESPONSE_PROTOCOL_V1,
    LEGACY_RESPONSE_PROTOCOL_V2,
}
BRANCH_ID_PREFIX = "B"
BRANCH_ID_LENGTH = 4
CONFIDENCES = {"strong", "medium", "exploratory"}
DELTA_STATUSES = {"new", "strengthened", "weakened", "revised", "discarded"}


def require_object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{label}: expected object")
    return value


def require_list(value: Any, label: str, *, non_empty: bool = False) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{label}: expected list")
    if non_empty and not value:
        raise ValueError(f"{label}: expected non-empty list")
    return value


def require_keys(
    record: dict[str, Any],
    required: set[str],
    label: str,
    *,
    allowed: set[str] | None = None,
) -> None:
    missing = required - record.keys()
    if missing:
        raise ValueError(f"{label}: missing keys {sorted(missing)}")
    if allowed is not None:
        extra = record.keys() - allowed
        if extra:
            raise ValueError(f"{label}: unexpected keys {sorted(extra)}")


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}: expected non-empty string")
    return value


def require_branch_id(value: Any, label: str) -> str:
    branch_id = require_string(value, label)
    if (
        not branch_id.startswith(BRANCH_ID_PREFIX)
        or len(branch_id) != BRANCH_ID_LENGTH
        or not branch_id[1:].isdigit()
    ):
        raise ValueError(f"{label}: invalid branch ID")
    return branch_id


def require_root_id(value: Any, label: str) -> str:
    root_id = require_string(value, label)
    if not root_id.startswith("root_") or len(root_id) != 11 or not root_id[5:].isdigit():
        raise ValueError(f"{label}: invalid mapped root ID")
    return root_id


def require_int(value: Any, label: str, *, minimum: int | None = None) -> int:
    if not isinstance(value, int):
        raise ValueError(f"{label}: expected integer")
    if minimum is not None and value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def ayah_roots(ayah: dict[str, Any]) -> list[str]:
    occurrences = require_list(ayah.get("root_occurrences"), f"{ayah.get('ref')}.root_occurrences", non_empty=True)
    return ordered_unique(require_string(occurrence.get("root"), "occurrence.root") for occurrence in occurrences)


def occurrence_phrase(occurrence: dict[str, Any]) -> str:
    surfaces = occurrence.get("surfaces_ar", [])
    if not isinstance(surfaces, list):
        raise ValueError("occurrence.surfaces_ar: expected list")
    return " ".join(surfaces)


def occurrence_key(occurrence: dict[str, Any]) -> tuple[str, tuple[str, ...], tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    return (
        occurrence_phrase(occurrence),
        tuple(occurrence.get("surfaces_ar", [])),
        tuple(occurrence.get("word_indices", [])),
        tuple(occurrence.get("lemmas_ar", [])),
        tuple(occurrence.get("pos_tags", [])),
    )


def phrase_key(phrase: dict[str, Any]) -> tuple[str, tuple[str, ...], tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    return (
        phrase["source_phrase_ar"],
        tuple(phrase["source_surfaces_ar"]),
        tuple(phrase["source_word_indices"]),
        tuple(phrase["source_lemmas_ar"]),
        tuple(phrase["source_pos_tags"]),
    )


def source_occurrence_index(packet: dict[str, Any]) -> dict[tuple[str, str], set[tuple[str, tuple[str, ...], tuple[str, ...], tuple[str, ...], tuple[str, ...]]]]:
    index: dict[tuple[str, str], set[tuple[str, tuple[str, ...], tuple[str, ...], tuple[str, ...], tuple[str, ...]]]] = {}
    ayat = [packet["focus_ayah"], *packet["context_ayat"]]
    for ayah in ayat:
        ref = ayah["ref"]
        for occurrence in require_list(ayah.get("root_occurrences"), f"{ref}.root_occurrences", non_empty=True):
            root = require_string(occurrence.get("root"), f"{ref}.root_occurrences.root")
            index.setdefault((ref, root), set()).add(occurrence_key(occurrence))
    return index


def validate_source_phrase(
    phrase: dict[str, Any],
    label: str,
    allowed_refs: set[str],
    root: str,
    occurrences: dict[tuple[str, str], set[tuple[str, tuple[str, ...], tuple[str, ...], tuple[str, ...], tuple[str, ...]]]],
) -> None:
    require_keys(
        phrase,
        {
            "source_ref",
            "source_phrase_ar",
            "source_surfaces_ar",
            "source_word_indices",
            "source_lemmas_ar",
            "source_pos_tags",
        },
        label,
        allowed={
            "source_ref",
            "source_phrase_ar",
            "source_surfaces_ar",
            "source_word_indices",
            "source_lemmas_ar",
            "source_pos_tags",
        },
    )
    source_ref = require_string(phrase["source_ref"], f"{label}.source_ref")
    if source_ref not in allowed_refs:
        raise ValueError(f"{label}.source_ref outside packet window: {source_ref}")
    require_string(phrase["source_phrase_ar"], f"{label}.source_phrase_ar")
    for key in ("source_surfaces_ar", "source_word_indices", "source_lemmas_ar", "source_pos_tags"):
        require_list(phrase[key], f"{label}.{key}")
    if phrase["source_phrase_ar"] != " ".join(phrase["source_surfaces_ar"]):
        raise ValueError(f"{label}.source_phrase_ar does not match source_surfaces_ar")
    if phrase_key(phrase) not in occurrences.get((source_ref, root), set()):
        raise ValueError(f"{label}: source phrase does not match packet occurrence for {source_ref}/{root}")


def validate_root_mapping(mapping: dict[str, Any], label: str) -> str:
    require_keys(
        mapping,
        {
            "qac_root",
            "mapping_status",
            "qac_total_occurrences",
            "matched_occurrences",
            "unmapped_reason",
            "targets",
        },
        label,
    )
    qac_root = require_string(mapping["qac_root"], f"{label}.qac_root")
    require_string(mapping["mapping_status"], f"{label}.mapping_status")
    if mapping["qac_total_occurrences"] is not None:
        require_int(mapping["qac_total_occurrences"], f"{label}.qac_total_occurrences", minimum=0)
    require_int(mapping["matched_occurrences"], f"{label}.matched_occurrences", minimum=0)
    if not isinstance(mapping["unmapped_reason"], str):
        raise ValueError(f"{label}.unmapped_reason: expected string")
    seen_ranks: set[int] = set()
    seen_target_ids: set[str] = set()
    for target_index, target in enumerate(require_list(mapping["targets"], f"{label}.targets")):
        target_label = f"{label}.targets[{target_index}]"
        record = require_object(target, target_label)
        require_keys(
            record,
            {
                "target_rank",
                "furuq_root_id",
                "furuq_root_norm",
                "furuq_source_root_norm",
                "furuq_resolution",
                "target_occurrences",
                "is_dominant",
            },
            target_label,
        )
        rank = require_int(record["target_rank"], f"{target_label}.target_rank", minimum=1)
        if rank in seen_ranks:
            raise ValueError(f"{label}.targets has duplicate target_rank {rank}")
        seen_ranks.add(rank)
        require_root_id(record["furuq_root_id"], f"{target_label}.furuq_root_id")
        if record["furuq_root_id"] in seen_target_ids:
            raise ValueError(f"{label}.targets has duplicate furuq_root_id {record['furuq_root_id']}")
        seen_target_ids.add(record["furuq_root_id"])
        require_string(record["furuq_root_norm"], f"{target_label}.furuq_root_norm")
        require_string(record["furuq_source_root_norm"], f"{target_label}.furuq_source_root_norm")
        require_string(record["furuq_resolution"], f"{target_label}.furuq_resolution")
        require_int(record["target_occurrences"], f"{target_label}.target_occurrences", minimum=0)
        if not isinstance(record["is_dominant"], bool):
            raise ValueError(f"{target_label}.is_dominant: expected boolean")
    return qac_root


def validate_branch(
    branch: dict[str, Any],
    label: str,
    *,
    focus: bool,
    require_mapping: bool,
) -> None:
    if require_mapping:
        require_root_id(branch.get("mapped_root_id"), f"{label}.mapped_root_id")
        require_string(branch.get("mapped_root_norm"), f"{label}.mapped_root_norm")
        require_string(branch.get("mapped_source_root_norm"), f"{label}.mapped_source_root_norm")
        require_int(branch.get("mapped_target_rank"), f"{label}.mapped_target_rank", minimum=1)
        require_int(branch.get("mapped_target_occurrences"), f"{label}.mapped_target_occurrences", minimum=0)
        if not isinstance(branch.get("mapped_is_dominant"), bool):
            raise ValueError(f"{label}.mapped_is_dominant: expected boolean")
    require_branch_id(branch.get("branch_id"), f"{label}.branch_id")
    require_string(branch.get("branch_image_ar"), f"{label}.branch_image_ar")
    if focus:
        require_string(branch.get("branch_image_en"), f"{label}.branch_image_en")
        require_string(branch.get("scope_ar"), f"{label}.scope_ar")
        require_string(branch.get("scope_en"), f"{label}.scope_en")


def validate_branch_mapping_against_root_mapping(
    branch: dict[str, Any],
    mapping: dict[str, Any],
    label: str,
) -> tuple[str, str]:
    targets = {
        target["furuq_root_id"]: target
        for target in require_list(mapping.get("targets"), f"{label}.root_mapping.targets")
    }
    mapped_root_id = require_root_id(branch.get("mapped_root_id"), f"{label}.mapped_root_id")
    if mapped_root_id not in targets:
        raise ValueError(f"{label}.mapped_root_id is not a target of root_mapping")
    target = targets[mapped_root_id]
    expected = {
        "mapped_root_norm": target["furuq_root_norm"],
        "mapped_source_root_norm": target["furuq_source_root_norm"],
        "mapped_target_rank": target["target_rank"],
        "mapped_target_occurrences": target["target_occurrences"],
        "mapped_is_dominant": target["is_dominant"],
    }
    for key, value in expected.items():
        if branch.get(key) != value:
            raise ValueError(f"{label}.{key} does not match root_mapping target")
    return mapped_root_id, require_branch_id(branch.get("branch_id"), f"{label}.branch_id")


def register_source_phrase_key(
    source_index: dict[tuple[str, str, tuple[str, ...]], tuple[str, tuple[str, ...], tuple[str, ...]]],
    root: str,
    phrase: dict[str, Any],
    label: str,
) -> None:
    key = (
        require_string(phrase["source_ref"], f"{label}.source_ref"),
        root,
        tuple(require_list(phrase["source_word_indices"], f"{label}.source_word_indices")),
    )
    value = (
        require_string(phrase["source_phrase_ar"], f"{label}.source_phrase_ar"),
        tuple(require_list(phrase["source_lemmas_ar"], f"{label}.source_lemmas_ar")),
        tuple(require_list(phrase["source_pos_tags"], f"{label}.source_pos_tags")),
    )
    previous = source_index.get(key)
    if previous is not None and previous != value:
        raise ValueError(f"{label}: conflicting duplicate source citation key {key}")
    source_index[key] = value


def register_branch_key(
    branch_index: dict[tuple[str, str, str], str],
    root: str,
    branch: dict[str, Any],
    label: str,
) -> None:
    mapped_root_id = branch.get("mapped_root_id")
    if mapped_root_id is None:
        return
    key = (
        root,
        require_root_id(mapped_root_id, f"{label}.mapped_root_id"),
        require_branch_id(branch.get("branch_id"), f"{label}.branch_id"),
    )
    branch_image_ar = require_string(branch.get("branch_image_ar"), f"{label}.branch_image_ar")
    previous = branch_index.get(key)
    if previous is not None and previous != branch_image_ar:
        raise ValueError(f"{label}: conflicting duplicate branch citation key {key}")
    branch_index[key] = branch_image_ar


def validate_packet(packet: dict[str, Any]) -> None:
    if packet.get("protocol") not in PACKET_PROTOCOLS:
        raise ValueError(f"packet protocol is not one of {sorted(PACKET_PROTOCOLS)}")
    require_mapping = packet.get("protocol") == PACKET_PROTOCOL
    focus_ref = require_string(packet.get("focus_ref"), "packet.focus_ref")
    window = require_list(packet.get("window"), "packet.window", non_empty=True)
    if focus_ref not in window:
        raise ValueError("focus_ref is not in packet.window")
    if packet.get("ayah_count") != len(window):
        raise ValueError("ayah_count does not match window length")
    allowed_refs = set(window)

    focus_ayah = require_object(packet.get("focus_ayah"), "packet.focus_ayah")
    if focus_ayah.get("ref") != focus_ref:
        raise ValueError("focus_ayah.ref does not match focus_ref")
    context_ayat = require_list(packet.get("context_ayat"), "packet.context_ayat")
    context_order = require_list(packet.get("context_order"), "packet.context_order")
    if [ayah.get("ref") for ayah in context_ayat] != context_order:
        raise ValueError("context_ayat order does not match context_order")
    if context_order != [ref for ref in window if ref != focus_ref]:
        raise ValueError("context_order must be window order excluding focus_ref")

    focus_roots = ayah_roots(focus_ayah)
    context_roots = ordered_unique(root for ayah in context_ayat for root in ayah_roots(ayah))
    all_roots = ordered_unique([*focus_roots, *context_roots])
    occurrences = source_occurrence_index(packet)
    packet_source_index: dict[tuple[str, str, tuple[str, ...]], tuple[str, tuple[str, ...], tuple[str, ...]]] = {}
    packet_branch_index: dict[tuple[str, str, str], str] = {}

    if require_mapping:
        root_mappings = require_list(packet.get("root_mappings"), "packet.root_mappings")
        actual_mapping_roots = [
            validate_root_mapping(require_object(mapping, f"root_mappings[{mapping_index}]"), f"root_mappings[{mapping_index}]")
            for mapping_index, mapping in enumerate(root_mappings)
        ]
        if actual_mapping_roots != all_roots:
            raise ValueError("root_mappings do not match packet root order")

    focus_inventories = require_list(
        packet.get("focus_branch_inventories"),
        "packet.focus_branch_inventories",
    )
    actual_focus_roots = [require_string(item.get("root"), "focus inventory root") for item in focus_inventories]
    if len(actual_focus_roots) != len(set(actual_focus_roots)):
        raise ValueError("duplicate root in focus_branch_inventories")
    for inventory_index, inventory in enumerate(focus_inventories):
        label = f"focus_branch_inventories[{inventory_index}]"
        required = {"root", "source_phrases", "branches"}
        if require_mapping:
            required.add("root_mapping")
        require_keys(inventory, required, label)
        root = require_string(inventory["root"], f"{label}.root")
        if root not in focus_roots:
            raise ValueError(f"{label}.root is not in focus ayah: {root}")
        if require_mapping:
            root_mapping = require_object(inventory["root_mapping"], f"{label}.root_mapping")
            mapping_root = validate_root_mapping(root_mapping, f"{label}.root_mapping")
            if mapping_root != root:
                raise ValueError(f"{label}.root_mapping.qac_root does not match root")
        for phrase_index, phrase in enumerate(require_list(inventory["source_phrases"], f"{label}.source_phrases", non_empty=True)):
            phrase_record = require_object(phrase, f"{label}.source_phrases[{phrase_index}]")
            phrase_label = f"{label}.source_phrases[{phrase_index}]"
            validate_source_phrase(phrase_record, phrase_label, allowed_refs, root, occurrences)
            register_source_phrase_key(packet_source_index, root, phrase_record, phrase_label)
            if phrase["source_ref"] != focus_ref:
                raise ValueError(f"{label}.source_phrases[{phrase_index}] is not from focus_ref")
        seen_branch_keys: set[tuple[str, str] | tuple[str]] = set()
        for branch_index, branch in enumerate(require_list(inventory["branches"], f"{label}.branches", non_empty=True)):
            branch_record = require_object(branch, f"{label}.branches[{branch_index}]")
            branch_label = f"{label}.branches[{branch_index}]"
            validate_branch(branch_record, branch_label, focus=True, require_mapping=require_mapping)
            if require_mapping:
                branch_key = validate_branch_mapping_against_root_mapping(branch_record, root_mapping, branch_label)
            else:
                branch_key = (require_branch_id(branch_record.get("branch_id"), f"{branch_label}.branch_id"),)
            if branch_key in seen_branch_keys:
                raise ValueError(f"{label}.branches duplicate branch key: {branch_key}")
            seen_branch_keys.add(branch_key)
            register_branch_key(packet_branch_index, root, branch_record, branch_label)

    context_cues = require_list(packet.get("context_root_cues"), "packet.context_root_cues")
    actual_context_roots = [require_string(item.get("root"), "context root") for item in context_cues]
    if len(actual_context_roots) != len(set(actual_context_roots)):
        raise ValueError("duplicate root in context_root_cues")
    for cue_index, cue in enumerate(context_cues):
        label = f"context_root_cues[{cue_index}]"
        required = {"root", "source_phrases", "branch_inventory_mode", "branches"}
        if require_mapping:
            required.add("root_mapping")
        require_keys(cue, required, label)
        root = require_string(cue["root"], f"{label}.root")
        if root not in context_roots:
            raise ValueError(f"{label}.root is not in context ayat: {root}")
        if require_mapping:
            root_mapping = require_object(cue["root_mapping"], f"{label}.root_mapping")
            mapping_root = validate_root_mapping(root_mapping, f"{label}.root_mapping")
            if mapping_root != root:
                raise ValueError(f"{label}.root_mapping.qac_root does not match root")
        for phrase_index, phrase in enumerate(require_list(cue["source_phrases"], f"{label}.source_phrases", non_empty=True)):
            phrase_record = require_object(phrase, f"{label}.source_phrases[{phrase_index}]")
            phrase_label = f"{label}.source_phrases[{phrase_index}]"
            validate_source_phrase(phrase_record, phrase_label, allowed_refs, root, occurrences)
            register_source_phrase_key(packet_source_index, root, phrase_record, phrase_label)
            if phrase["source_ref"] == focus_ref:
                raise ValueError(f"{label}.source_phrases[{phrase_index}] unexpectedly cites focus_ref")
        seen_branch_keys: set[tuple[str, str] | tuple[str]] = set()
        for branch_index, branch in enumerate(require_list(cue["branches"], f"{label}.branches", non_empty=True)):
            branch_record = require_object(branch, f"{label}.branches[{branch_index}]")
            branch_label = f"{label}.branches[{branch_index}]"
            validate_branch(branch_record, branch_label, focus=False, require_mapping=require_mapping)
            if require_mapping:
                branch_key = validate_branch_mapping_against_root_mapping(branch_record, root_mapping, branch_label)
            else:
                branch_key = (require_branch_id(branch_record.get("branch_id"), f"{branch_label}.branch_id"),)
            if branch_key in seen_branch_keys:
                raise ValueError(f"{label}.branches duplicate branch key: {branch_key}")
            seen_branch_keys.add(branch_key)
            register_branch_key(packet_branch_index, root, branch_record, branch_label)

    missing = require_list(packet.get("missing_branch_inventories", []), "packet.missing_branch_inventories")
    missing_roots = [require_string(item.get("root"), "missing root") for item in missing]
    if len(missing_roots) != len(set(missing_roots)):
        raise ValueError("duplicate root in missing_branch_inventories")
    for missing_index, item in enumerate(missing):
        label = f"missing_branch_inventories[{missing_index}]"
        required = {"root", "refs", "source_phrases", "reason"}
        if require_mapping:
            required.add("root_mapping")
        require_keys(item, required, label)
        if require_mapping:
            mapping_root = validate_root_mapping(require_object(item["root_mapping"], f"{label}.root_mapping"), f"{label}.root_mapping")
            if mapping_root != item["root"]:
                raise ValueError(f"{label}.root_mapping.qac_root does not match root")
        refs = require_list(item["refs"], f"{label}.refs", non_empty=True)
        for ref in refs:
            if ref not in allowed_refs:
                raise ValueError(f"{label}.refs outside packet window: {ref}")
        for phrase_index, phrase in enumerate(require_list(item["source_phrases"], f"{label}.source_phrases", non_empty=True)):
            phrase_record = require_object(phrase, f"{label}.source_phrases[{phrase_index}]")
            phrase_label = f"{label}.source_phrases[{phrase_index}]"
            validate_source_phrase(phrase_record, phrase_label, allowed_refs, item["root"], occurrences)
            register_source_phrase_key(packet_source_index, item["root"], phrase_record, phrase_label)

    expected_focus_available = [root for root in focus_roots if root not in set(missing_roots)]
    if actual_focus_roots != expected_focus_available:
        raise ValueError("focus branch inventories do not match focus root order")
    expected_context_available = [root for root in context_roots if root not in set(missing_roots)]
    if actual_context_roots != expected_context_available:
        raise ValueError("context root cues do not match context root order")

    provenance = require_object(packet.get("provenance"), "packet.provenance")
    resource_hashes = require_object(provenance.get("resource_sha256"), "packet.provenance.resource_sha256")
    for resource, expected_hash in resource_hashes.items():
        path = Path(resource)
        if not path.is_absolute():
            path = REPO_ROOT / path
        if sha256(path) != expected_hash:
            raise ValueError(f"resource hash changed: {resource}")


def packet_citations(
    packet: dict[str, Any],
    collections: tuple[str, ...],
) -> tuple[
    dict[str, dict[str, str]],
    dict[str, dict[tuple[str, str], str]],
    set[tuple[str, str, str]],
    set[tuple[str, str, tuple[str, ...]]],
]:
    branches: dict[str, dict[str, str]] = {}
    mapped_branches: dict[str, dict[tuple[str, str], str]] = {}
    phrases: set[tuple[str, str, str]] = set()
    source_keys: set[tuple[str, str, tuple[str, ...]]] = set()
    for collection in collections:
        for inventory in packet.get(collection, []):
            root = inventory["root"]
            branches.setdefault(root, {})
            mapped_branches.setdefault(root, {})
            for branch in inventory["branches"]:
                branch_id = branch["branch_id"]
                branches[root][branch_id] = branch["branch_image_ar"]
                mapped_root_id = branch.get("mapped_root_id")
                if mapped_root_id:
                    mapped_branches[root][(mapped_root_id, branch_id)] = branch["branch_image_ar"]
            for phrase in inventory["source_phrases"]:
                phrases.add((phrase["source_ref"], root, phrase["source_phrase_ar"]))
                source_keys.add((phrase["source_ref"], root, tuple(phrase["source_word_indices"])))
    return branches, mapped_branches, phrases, source_keys


def validate_trace_entry(
    trace: dict[str, Any],
    label: str,
    branches: dict[str, dict[str, str]],
    mapped_branches: dict[str, dict[tuple[str, str], str]],
    phrases: set[tuple[str, str, str]],
    source_keys: set[tuple[str, str, tuple[str, ...]]],
    require_mapped_root_id: bool,
    compact_response: bool,
) -> tuple[str, str]:
    required = {
        "source_ref",
        "root",
        "branch_id",
    }
    allowed = set(required)
    if compact_response:
        required.update({"source_word_indices", "role"})
        allowed.update({"source_word_indices", "role", "mapped_root_id"})
    else:
        required.update({"source_phrase_ar", "branch_image_ar", "literal_contribution", "assigned_role"})
        allowed.update({"source_phrase_ar", "branch_image_ar", "literal_contribution", "assigned_role", "mapped_root_id", "mapped_root_norm"})
    if require_mapped_root_id:
        required.add("mapped_root_id")
    require_keys(
        trace,
        required,
        label,
        allowed=allowed,
    )
    source_ref = require_string(trace["source_ref"], f"{label}.source_ref")
    root = require_string(trace["root"], f"{label}.root")
    phrase = trace.get("source_phrase_ar")
    if phrase is not None:
        phrase = require_string(phrase, f"{label}.source_phrase_ar")
    source_word_indices = trace.get("source_word_indices")
    if source_word_indices is not None:
        source_word_indices = tuple(
            require_string(item, f"{label}.source_word_indices[]")
            for item in require_list(source_word_indices, f"{label}.source_word_indices", non_empty=True)
        )
    branch_id = require_branch_id(trace["branch_id"], f"{label}.branch_id")
    mapped_root_id = trace.get("mapped_root_id")
    if mapped_root_id is not None:
        mapped_root_id = require_root_id(mapped_root_id, f"{label}.mapped_root_id")
    branch_image_ar = trace.get("branch_image_ar")
    if branch_image_ar is not None:
        branch_image_ar = require_string(branch_image_ar, f"{label}.branch_image_ar")
    if compact_response:
        require_string(trace["role"], f"{label}.role")
    else:
        require_string(trace["literal_contribution"], f"{label}.literal_contribution")
        require_string(trace["assigned_role"], f"{label}.assigned_role")
    if root not in branches:
        raise ValueError(f"{label}: root {root!r} has no branch inventory in packet")
    if mapped_root_id is not None:
        branch_key = (mapped_root_id, branch_id)
        if branch_key not in mapped_branches.get(root, {}):
            raise ValueError(f"{label}: branch {root}/{mapped_root_id}/{branch_id} was not in packet")
        if branch_image_ar is not None and branch_image_ar != mapped_branches[root][branch_key]:
            raise ValueError(
                f"{label}: branch_image_ar does not match packet branch "
                f"{root}/{mapped_root_id}/{branch_id}"
            )
    else:
        if branch_id not in branches[root]:
            raise ValueError(f"{label}: branch {root}/{branch_id} was not in packet")
        if branch_image_ar is not None and branch_image_ar != branches[root][branch_id]:
            raise ValueError(f"{label}: branch_image_ar does not match packet branch {root}/{branch_id}")
    matching_phrases = [item for item in phrases if item[0] == source_ref and item[1] == root]
    if not matching_phrases:
        raise ValueError(f"{label}: source ref/root was not in packet for {source_ref}/{root}")
    if source_word_indices is not None and (source_ref, root, source_word_indices) not in source_keys:
        raise ValueError(f"{label}: source word indices were not in packet for {source_ref}/{root}")
    if phrase is not None and (source_ref, root, phrase) not in phrases:
        raise ValueError(f"{label}: source phrase was not in packet for {source_ref}/{root}")
    return source_ref, root


def validate_changed_reading(value: Any, label: str) -> None:
    record = require_object(value, label)
    require_keys(record, {"before", "after"}, label, allowed={"before", "after"})
    require_string(record["before"], f"{label}.before")
    require_string(record["after"], f"{label}.after")


def validate_baseline_model(
    model: dict[str, Any],
    label: str,
    branches: dict[str, dict[str, str]],
    mapped_branches: dict[str, dict[tuple[str, str], str]],
    phrases: set[tuple[str, str, str]],
    source_keys: set[tuple[str, str, tuple[str, ...]]],
    require_mapped_root_id: bool,
    compact_response: bool,
) -> str:
    allowed_keys = {
        "model_id",
        "confidence",
        "focus_anchor",
        "mechanism",
        "activation_trace",
        "changed_reading",
    }
    if not compact_response:
        allowed_keys.add("status")
    require_keys(
        model,
        allowed_keys,
        label,
        allowed=allowed_keys,
    )
    model_id = require_string(model["model_id"], f"{label}.model_id")
    if not compact_response and model["status"] != "baseline":
        raise ValueError(f"{label}.status must be baseline")
    if model["confidence"] not in CONFIDENCES:
        raise ValueError(f"{label}.confidence has invalid value")
    require_string(model["focus_anchor"], f"{label}.focus_anchor")
    require_string(model["mechanism"], f"{label}.mechanism")
    for trace_index, trace in enumerate(require_list(model["activation_trace"], f"{label}.activation_trace", non_empty=True)):
        validate_trace_entry(require_object(trace, f"{label}.activation_trace[{trace_index}]"), f"{label}.activation_trace[{trace_index}]", branches, mapped_branches, phrases, source_keys, require_mapped_root_id, compact_response)
    validate_changed_reading(model["changed_reading"], f"{label}.changed_reading")
    return model_id


def validate_context_delta(
    delta: dict[str, Any],
    label: str,
    branches: dict[str, dict[str, str]],
    mapped_branches: dict[str, dict[tuple[str, str], str]],
    phrases: set[tuple[str, str, str]],
    source_keys: set[tuple[str, str, tuple[str, ...]]],
    context_refs: set[str],
    context_roots: set[str],
    require_mapped_root_id: bool,
    compact_response: bool,
) -> str:
    allowed_keys = {
        "model_id",
        "status",
        "confidence",
        "trigger_roots",
        "mechanism",
        "activation_trace",
        "structural_cues",
        "changed_reading",
    }
    if compact_response:
        allowed_keys.update({"reader_inference", "trigger_refs", "minimal_triggers", "ablation"})
    else:
        allowed_keys.update({"trigger_refs", "abductive_moves", "minimal_triggers", "ablation"})
    required_keys = set(allowed_keys)
    if compact_response:
        required_keys -= {"trigger_refs", "minimal_triggers", "ablation"}
    require_keys(
        delta,
        required_keys,
        label,
        allowed=allowed_keys,
    )
    model_id = require_string(delta["model_id"], f"{label}.model_id")
    if delta["status"] not in DELTA_STATUSES:
        raise ValueError(f"{label}.status has invalid value")
    if delta["confidence"] not in CONFIDENCES:
        raise ValueError(f"{label}.confidence has invalid value")
    trigger_refs = require_list(delta["trigger_refs"], f"{label}.trigger_refs", non_empty=True) if "trigger_refs" in delta else None
    if trigger_refs is not None:
        if len(trigger_refs) != len(set(trigger_refs)):
            raise ValueError(f"{label}.trigger_refs contains duplicates")
        for ref in trigger_refs:
            if not isinstance(ref, str):
                raise ValueError(f"{label}.trigger_refs: expected string refs")
            if ref not in context_refs:
                raise ValueError(f"{label}.trigger_refs contains ref outside context: {ref}")
    trigger_roots = require_list(delta["trigger_roots"], f"{label}.trigger_roots", non_empty=True)
    if len(trigger_roots) != len(set(trigger_roots)):
        raise ValueError(f"{label}.trigger_roots contains duplicates")
    for root in trigger_roots:
        if not isinstance(root, str):
            raise ValueError(f"{label}.trigger_roots: expected string roots")
        if root not in context_roots:
            raise ValueError(f"{label}.trigger_roots contains root outside context: {root}")
    require_string(delta["mechanism"], f"{label}.mechanism")
    resolved_context_refs: set[str] = set()
    resolved_context_roots: set[str] = set()
    for trace_index, trace in enumerate(require_list(delta["activation_trace"], f"{label}.activation_trace", non_empty=True)):
        source_ref, root = validate_trace_entry(require_object(trace, f"{label}.activation_trace[{trace_index}]"), f"{label}.activation_trace[{trace_index}]", branches, mapped_branches, phrases, source_keys, require_mapped_root_id, compact_response)
        if source_ref in context_refs:
            resolved_context_refs.add(source_ref)
            resolved_context_roots.add(root)
    if compact_response:
        if not resolved_context_refs:
            raise ValueError(f"{label}.activation_trace must include at least one context citation")
        if trigger_refs is not None and set(trigger_refs) != resolved_context_refs:
            raise ValueError(f"{label}.trigger_refs do not match context citations")
        if set(trigger_roots) != resolved_context_roots:
            raise ValueError(f"{label}.trigger_roots do not match context citations")
    for cue_index, cue in enumerate(require_list(delta["structural_cues"], f"{label}.structural_cues", non_empty=True)):
        require_string(cue, f"{label}.structural_cues[{cue_index}]")
    if compact_response:
        require_string(delta["reader_inference"], f"{label}.reader_inference")
    else:
        for move_index, move in enumerate(require_list(delta["abductive_moves"], f"{label}.abductive_moves")):
            move_label = f"{label}.abductive_moves[{move_index}]"
            record = require_object(move, move_label)
            require_keys(record, {"assumption", "packet_supplies", "reader_infers", "alternatives"}, move_label)
            require_string(record["assumption"], f"{move_label}.assumption")
            require_string(record["packet_supplies"], f"{move_label}.packet_supplies")
            require_string(record["reader_infers"], f"{move_label}.reader_infers")
            require_list(record["alternatives"], f"{move_label}.alternatives")
    validate_changed_reading(delta["changed_reading"], f"{label}.changed_reading")
    if "minimal_triggers" in delta:
        for trigger_index, trigger in enumerate(require_list(delta["minimal_triggers"], f"{label}.minimal_triggers")):
            require_string(trigger, f"{label}.minimal_triggers[{trigger_index}]")
    if "ablation" in delta:
        require_string(delta["ablation"], f"{label}.ablation")
    return model_id


def validate_surprising_valid_outlier(
    outlier: dict[str, Any],
    label: str,
    branches: dict[str, dict[str, str]],
    mapped_branches: dict[str, dict[tuple[str, str], str]],
    phrases: set[tuple[str, str, str]],
    source_keys: set[tuple[str, str, tuple[str, ...]]],
    require_mapped_root_id: bool,
    compact_response: bool,
) -> str:
    allowed_keys = {
        "outlier_id",
        "confidence",
        "focus_anchor",
        "activation_trace",
        "changed_reading",
    }
    if compact_response:
        allowed_keys.add("containment")
    else:
        allowed_keys.update({"why_surprising", "why_still_valid", "rendering_caution"})
    require_keys(outlier, allowed_keys, label, allowed=allowed_keys)
    outlier_id = require_string(outlier["outlier_id"], f"{label}.outlier_id")
    if outlier["confidence"] not in {"medium", "exploratory"}:
        raise ValueError(f"{label}.confidence has invalid value")
    if compact_response:
        require_string(outlier["containment"], f"{label}.containment")
    else:
        require_string(outlier["why_surprising"], f"{label}.why_surprising")
        require_string(outlier["why_still_valid"], f"{label}.why_still_valid")
    require_string(outlier["focus_anchor"], f"{label}.focus_anchor")
    for trace_index, trace in enumerate(require_list(outlier["activation_trace"], f"{label}.activation_trace", non_empty=True)):
        validate_trace_entry(require_object(trace, f"{label}.activation_trace[{trace_index}]"), f"{label}.activation_trace[{trace_index}]", branches, mapped_branches, phrases, source_keys, require_mapped_root_id, compact_response)
    validate_changed_reading(outlier["changed_reading"], f"{label}.changed_reading")
    if not compact_response:
        require_string(outlier["rendering_caution"], f"{label}.rendering_caution")
    return outlier_id


def validate_response(packet: dict[str, Any], response: dict[str, Any]) -> None:
    protocol = response.get("protocol")
    if protocol not in RESPONSE_PROTOCOLS:
        raise ValueError(
            "response protocol is not one of "
            f"{sorted(RESPONSE_PROTOCOLS)}"
        )
    if response.get("focus_ref") != packet["focus_ref"]:
        raise ValueError("response focus_ref does not match packet")
    require_mapped_root_id = protocol in {RESPONSE_PROTOCOL_V3, RESPONSE_PROTOCOL_V4}
    compact_response = protocol == RESPONSE_PROTOCOL_V4
    require_string(response.get("reader_id"), "response.reader_id")
    if compact_response:
        allowed_top_level = {
            "protocol",
            "reader_id",
            "focus_ref",
            "trace_kind",
            "baseline_models",
            "context_deltas",
            "surprising_valid_outliers",
            "discarded_or_unchanged",
            "summary",
        }
        required_top_level = allowed_top_level - {"discarded_or_unchanged"}
        require_keys(response, required_top_level, "response", allowed=allowed_top_level)
        if response.get("trace_kind") != "reconstructed":
            raise ValueError("response.trace_kind must be reconstructed")
    else:
        hermeticity = require_object(response.get("hermeticity"), "response.hermeticity")
        require_keys(hermeticity, {"method", "limitations"}, "response.hermeticity")
        require_string(hermeticity["method"], "response.hermeticity.method")
        require_string(hermeticity["limitations"], "response.hermeticity.limitations")

    focus_branches, focus_mapped_branches, focus_phrases, focus_source_keys = packet_citations(packet, ("focus_branch_inventories",))
    all_branches, all_mapped_branches, all_phrases, all_source_keys = packet_citations(
        packet,
        ("focus_branch_inventories", "context_root_cues"),
    )
    context_refs = set(packet["context_order"])
    context_roots = {cue["root"] for cue in packet.get("context_root_cues", [])}
    model_ids: set[str] = set()
    baseline_models = require_list(
        response.get("baseline_models"),
        "response.baseline_models",
        non_empty=compact_response,
    )
    for index, model in enumerate(baseline_models):
        model_id = validate_baseline_model(
            require_object(model, f"baseline_models[{index}]"),
            f"baseline_models[{index}]",
            focus_branches,
            focus_mapped_branches,
            focus_phrases,
            focus_source_keys,
            require_mapped_root_id,
            compact_response,
        )
        if model_id in model_ids:
            raise ValueError(f"duplicate model_id: {model_id}")
        model_ids.add(model_id)
    for index, delta in enumerate(require_list(response.get("context_deltas"), "response.context_deltas")):
        model_id = validate_context_delta(
            require_object(delta, f"context_deltas[{index}]"),
            f"context_deltas[{index}]",
            all_branches,
            all_mapped_branches,
            all_phrases,
            all_source_keys,
            context_refs,
            context_roots,
            require_mapped_root_id,
            compact_response,
        )
        if model_id in model_ids:
            raise ValueError(f"duplicate model_id: {model_id}")
        model_ids.add(model_id)
    outlier_ids: set[str] = set()
    outliers = response.get("surprising_valid_outliers", [])
    if protocol in {RESPONSE_PROTOCOL_V2, RESPONSE_PROTOCOL_V3, RESPONSE_PROTOCOL_V4, LEGACY_RESPONSE_PROTOCOL_V2}:
        outliers = require_list(
            response.get("surprising_valid_outliers"),
            "response.surprising_valid_outliers",
        )
    elif outliers is not None:
        outliers = require_list(outliers, "response.surprising_valid_outliers")
    for index, outlier in enumerate(outliers):
        outlier_id = validate_surprising_valid_outlier(
            require_object(outlier, f"surprising_valid_outliers[{index}]"),
            f"surprising_valid_outliers[{index}]",
            all_branches,
            all_mapped_branches,
            all_phrases,
            all_source_keys,
            require_mapped_root_id,
            compact_response,
        )
        if outlier_id in outlier_ids:
            raise ValueError(f"duplicate outlier_id: {outlier_id}")
        outlier_ids.add(outlier_id)
    if compact_response:
        if "discarded_or_unchanged" in response:
            for index, item in enumerate(require_list(response.get("discarded_or_unchanged"), "response.discarded_or_unchanged")):
                require_string(item, f"response.discarded_or_unchanged[{index}]")
    else:
        for index, item in enumerate(require_list(response.get("discarded_or_unchanged"), "response.discarded_or_unchanged")):
            require_string(item, f"response.discarded_or_unchanged[{index}]")
    summary = require_object(response.get("summary"), "response.summary")
    require_keys(
        summary,
        {"strongest_changes", "what_was_special", "remaining_uncertainties"},
        "response.summary",
        allowed={"strongest_changes", "what_was_special", "remaining_uncertainties"},
    )
    for index, item in enumerate(require_list(summary["strongest_changes"], "response.summary.strongest_changes")):
        require_string(item, f"response.summary.strongest_changes[{index}]")
    require_string(summary["what_was_special"], "response.summary.what_was_special")
    for index, item in enumerate(require_list(summary["remaining_uncertainties"], "response.summary.remaining_uncertainties")):
        require_string(item, f"response.summary.remaining_uncertainties[{index}]")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    parser.add_argument("response", nargs="?", type=Path)
    args = parser.parse_args()

    packet = json.loads(args.packet.read_text(encoding="utf-8"))
    validate_packet(packet)
    if args.response:
        response = json.loads(args.response.read_text(encoding="utf-8"))
        validate_response(packet, response)
        print(f"valid focus-trace response: {args.response}")
    else:
        print(f"valid focus-trace packet: {args.packet}")


if __name__ == "__main__":
    main()
