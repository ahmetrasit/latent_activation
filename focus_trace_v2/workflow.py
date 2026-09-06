#!/usr/bin/env python3
"""Offline HFT v2: prepare a sealed job, validate it, or export resolved evidence."""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import re
from pathlib import Path
from typing import Any

WORKFLOW_ROOT = Path(__file__).resolve().parent
REPO_ROOT = WORKFLOW_ROOT.parent
SOURCE_LOADER = REPO_ROOT / "focus_trace/scripts/build_focus_trace_packet.py"
spec = importlib.util.spec_from_file_location("hft_v2_sources", SOURCE_LOADER)
sources = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sources)

PACKET_PROTOCOL = "hft-v2-packet-v1"
RESPONSE_PROTOCOL = "focus-trace-hermetic-response-v4"
JOB_PROTOCOL = "hft-v2-job-v3"
PREVIOUS_RESPONSE_PROTOCOL = "hft-v2-response-v2"
PREVIOUS_JOB_PROTOCOL = "hft-v2-job-v2"
LEGACY_JOB_PROTOCOL = "hft-v2-job-v1"
V1_PACKET_PROTOCOL = "focus-trace-pericope-lean-v1"
V1_PROMPT = REPO_ROOT / "focus_trace/prompts/focus_trace_hermetic.md"
V1_SCHEMA = REPO_ROOT / "focus_trace/schemas/focus-trace-response.schema.json"
EVIDENCE_PROTOCOL = "hft-v2-evidence-v1"
MODELS = ("gpt-5.6-luna", "gpt-5.6-terra", "gpt-5.6-sol", "gpt-6-astra")
REASONING_EFFORTS = ("medium", "max")
SECTIONS = ("baseline_models", "context_deltas", "surprising_valid_outliers")
TWO_STAGE_PROMPTS = ("discovery.prompt.md", "ledger.prompt.md")
VARIANT_FIELDS = ("root_id", "source_path", "image_ar", "image_en", "scope_ar", "scope_en")
LINGUISTIC_VARIANT_FIELDS = ("image_ar", "image_en", "scope_ar", "scope_en")
SCHEMA_KEYWORDS = {"$schema", "$id", "$defs", "$ref", "title", "description", "type", "const", "enum",
                   "properties", "required", "additionalProperties", "items", "minItems", "uniqueItems", "minLength", "pattern",
                   "allOf", "if", "then", "not"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path) -> Any:
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, f"{path}: duplicate JSON key {key!r}")
            result[key] = value
        return result

    def invalid_constant(value):
        raise ValueError(f"{path}: invalid JSON constant {value}")

    return json.loads(path.read_bytes(), object_pairs_hook=pairs, parse_constant=invalid_constant)


def snapshot(paths: list[Path]) -> list[dict[str, str]]:
    return [{"path": str(path.resolve()), "sha256": sources.sha256(path)} for path in paths]


def parse_window(value: str) -> list[str]:
    """Accept S:A, S:A-B, and comma-separated combinations; never silently dedup."""
    refs = []
    for part in value.split(","):
        match = re.fullmatch(r"([1-9][0-9]*):([0-9]+)(?:-([0-9]+))?", part.strip())
        require(match is not None, f"invalid window segment: {part!r}")
        surah, start, end = match.groups()
        start, end = int(start), int(end if end is not None else start)
        require(start <= end <= 286 and int(surah) <= 114, f"invalid window bounds: {part}")
        refs.extend(f"{int(surah)}:{ayah}" for ayah in range(start, end + 1))
    require(len(refs) == len(set(refs)), "window contains duplicate references")
    return refs


def project_inventory(mappings: dict, raw_branches: dict) -> tuple[list, list, dict]:
    """One inventory per mapped root, retaining image/scope pairs from every row."""
    inventories: dict[str, dict] = {}
    roots_without_branches = []
    targets_without_branches = []
    missing_fields = []
    for qac_root, mapping in mappings.items():
        if not raw_branches[qac_root]:
            roots_without_branches.append({
                "qac_root": qac_root,
                "reason": mapping["unmapped_reason"] or "no non-contaminated inventory for mapped targets",
            })
        for target in mapping["targets"]:
            root_id = target["furuq_root_id"]
            rows = [row for row in raw_branches[qac_root] if row["mapped_root_id"] == root_id]
            if not rows:
                targets_without_branches.append({"qac_root": qac_root, "mapped_root_id": root_id,
                                                 "reason": "no non-contaminated branch rows for mapped root_id"})
                continue
            branches = []
            for row in rows:
                variants = []
                seen = set()
                for variant in row["variants"]:
                    record = {key: variant[key] for key in VARIANT_FIELDS}
                    identity = json_bytes(record)
                    if identity in seen:
                        continue  # Exact repeated rows only; never merge distinct scopes.
                    seen.add(identity)
                    variants.append({"variant_id": f"V{len(variants) + 1:03d}", **record})
                branches.append({"branch_id": row["branch_id"], "variants": variants})
            inventory = {"mapped_root_id": root_id, "branches": branches}
            require(root_id not in inventories or inventories[root_id] == inventory,
                    f"inconsistent inventory shared by QAC mappings: {root_id}")
            inventories[root_id] = inventory
    for inventory in inventories.values():
        for branch in inventory["branches"]:
            for variant in branch["variants"]:
                fields = [field for field in ("image_ar", "scope_ar") if not variant[field]]
                if fields:
                    missing_fields.append({"mapped_root_id": inventory["mapped_root_id"],
                                           "branch_id": branch["branch_id"],
                                           "variant_id": variant["variant_id"], "fields": fields})
    # Keep the complete source mapping, including frozen roots and non-dominant targets.
    projected_mappings = copy.deepcopy(list(mappings.values()))
    for mapping in projected_mappings:
        for target in mapping["targets"]:
            branches = inventories.get(target["furuq_root_id"], {}).get("branches", [])
            target["branch_count"] = len(branches)
            target["variant_count"] = sum(len(branch["variants"]) for branch in branches)
    return projected_mappings, list(inventories.values()), {
        "roots_without_branches": roots_without_branches,
        "targets_without_branches": targets_without_branches,
        "missing_arabic_fields": missing_fields,
    }


def build_packet(focus_ref: str, window: list[str], *,
                 qac: Path = sources.DEFAULT_QAC,
                 quran_dir: Path = sources.DEFAULT_QURAN_DIR,
                 branches: Path = sources.DEFAULT_BRANCH_DB,
                 root_map: Path = sources.DEFAULT_QAC_FURUQ_ROOT_MAP,
                 remote_orientation: dict | None = None) -> tuple[dict, list]:
    """Build the complete coordinator source snapshot, NOT the reader projection."""
    require(re.fullmatch(r"[1-9][0-9]*:[1-9][0-9]*", focus_ref) is not None, "invalid numbered focus ref")
    surah = int(focus_ref.split(":")[0])
    quran = sources.load_quran_surah(quran_dir, surah)
    allowed = {f"{surah}:{ayah}" for ayah in quran}
    if surah not in {1, 9}:
        allowed.add(f"{surah}:0")
    require(window and len(window) == len(set(window)), "window must be nonempty and unique")
    require(set(window) <= allowed and focus_ref in window, "window must contain focus and valid same-surah refs")
    require(window == sorted(window, key=lambda ref: int(ref.split(":")[1])), "window must be in ayah order")
    input_paths = [qac, branches, root_map, sources.quran_surah_path(quran_dir, surah)]
    if f"{surah}:0" in window:
        input_paths.append(sources.quran_surah_path(quran_dir, 1))
    before = snapshot(input_paths)
    ayat_by_ref = sources.load_window_ayat(qac, quran_dir, window)
    ayat = [ayat_by_ref[ref] for ref in window]
    for ayah in ayat:
        if ayah.get("rootless"):
            ayah["rootless_reason"] = "No rooted rows in supplied QAC resource; not proof of morphological rootlessness."
        if not ayah["ref"].endswith(":0"):
            expected = quran[int(ayah["ref"].split(":")[1])]
            require(sources.canonical_arabic(ayah["text_ar"]) == sources.canonical_arabic(expected),
                    f"QAC/Quran text mismatch at {ayah['ref']}")
    roots = sources.first_seen_roots(ayat)
    mappings = sources.load_root_mappings(root_map, roots)
    raw_branches, _, _ = sources.load_branches_for_mapped_roots(branches, mappings)
    root_mappings, inventory, gaps = project_inventory(mappings, raw_branches)
    gaps["ayat_without_qac_roots"] = [ayah["ref"] for ayah in ayat if not ayah["root_occurrences"]]
    packet = {
        "protocol": PACKET_PROTOCOL,
        "focus_ref": focus_ref,
        "window": window,
        "ayat": ayat,
        "root_mappings": root_mappings,
        "branch_inventory": inventory,
        "source_gaps": gaps,
        "orientation": {
            "citable": False,
            "out_of_window_ayat": [{"ref": f"{surah}:{ayah}", "text_ar": text}
                                    for ayah, text in quran.items() if f"{surah}:{ayah}" not in window],
            "legacy_remote_snapshot": copy.deepcopy(remote_orientation),
        },
    }
    require(before == snapshot(input_paths), "source changed during preparation; retry in a new job")
    validate_packet(packet)
    return packet, before


def distinct_root_forms(parent_root: str, values: list) -> list[str]:
    return list(dict.fromkeys(value for value in values if value and value != parent_root))


def reader_orientation(orientation: dict) -> dict:
    """Keep legacy orientation evidence without copying pipeline labels or audits."""
    result = {"citable": False, "out_of_window_ayat": copy.deepcopy(orientation["out_of_window_ayat"])}
    remote = orientation.get("legacy_remote_snapshot")
    if not remote:
        return result
    # Current legacy reader packets use this flat shape. Fail on an unfamiliar
    # shape rather than silently stripping potentially linguistic evidence.
    require(set(remote) <= {"citable", "refs", "root_cues"}, "unrecognized remote orientation fields")
    if remote.get("refs"):
        result["remote_refs"] = copy.deepcopy(remote["refs"])
    cues = []
    for cue in remote.get("root_cues", []):
        require(set(cue) <= {"root", "source_refs", "targets"}, "unrecognized remote cue fields")
        projected = {"root": cue["root"], "source_refs": copy.deepcopy(cue["source_refs"]), "targets": []}
        for target in cue["targets"]:
            require(set(target) <= {"mapped_root_id", "mapped_root_norm", "branches"}, "unrecognized remote target fields")
            item = {"mapped_root_id": target["mapped_root_id"], "branches": []}
            forms = distinct_root_forms(cue["root"], [target.get("mapped_root_norm")])
            if forms:
                item["root_forms_ar"] = forms
            for branch in target["branches"]:
                require(set(branch) <= {"branch_id", "branch_image_ar", "branch_image_en", "scope_ar", "scope_en", "what_is_ar", "what_is_en"},
                        "unrecognized remote branch fields")
                item["branches"].append(copy.deepcopy(branch))
            projected["targets"].append(item)
        cues.append(projected)
    if cues:
        result["root_cues"] = cues
    return result


def reader_packet(source_packet: dict) -> dict:
    """A linguistic-only view. Provenance and coverage data stay in source.packet.json."""
    ayat = [{key: copy.deepcopy(ayah[key])
             for key in ("ref", "text_ar", "root_sequence", "root_occurrences", "synthetic_source_ref") if key in ayah}
            for ayah in source_packet["ayat"]]
    mappings = []
    for mapping in source_packet["root_mappings"]:
        targets = []
        for target in mapping["targets"]:
            projected = {"furuq_root_id": target["furuq_root_id"]}
            forms = distinct_root_forms(mapping["qac_root"], [target.get(key) for key in
                ("furuq_root_norm", "furuq_source_root_norm", "frozen_root_norm")])
            if forms:
                projected["root_forms_ar"] = forms
            targets.append(projected)
        mappings.append({"qac_root": mapping["qac_root"], "targets": targets})
    inventory = [{"mapped_root_id": inv["mapped_root_id"], "branches": [
        {"branch_id": branch["branch_id"], "variants": [
            {key: copy.deepcopy(variant[key]) for key in ("variant_id", *LINGUISTIC_VARIANT_FIELDS)}
            for variant in branch["variants"]]} for branch in inv["branches"]]}
        for inv in source_packet["branch_inventory"]]
    gaps = source_packet["source_gaps"]
    availability = {
        "roots_without_branches": [gap["qac_root"] for gap in gaps["roots_without_branches"]],
        "targets_without_branches": [{key: gap[key] for key in ("qac_root", "mapped_root_id")}
                                     for gap in gaps["targets_without_branches"]],
        "missing_arabic_fields": copy.deepcopy(gaps["missing_arabic_fields"]),
        "ayat_without_qac_roots": copy.deepcopy(gaps["ayat_without_qac_roots"]),
    }
    return {"focus_ref": source_packet["focus_ref"], "window": copy.deepcopy(source_packet["window"]),
            "ayat": ayat, "root_mappings": mappings, "branch_inventory": inventory,
            "source_gaps": {key: value for key, value in availability.items() if value},
            "orientation": reader_orientation(source_packet["orientation"])}


def v1_reader_packet(source_packet: dict) -> dict:
    """Restore v1's focus-first/root-cue layout without its lossy lean projection.

    Source images/scopes remain paired, including every English gloss and split
    target. Source paths, mapping ranks, and coverage bookkeeping stay outside.
    """
    clean = reader_packet(source_packet)
    ayat = {ayah["ref"]: ayah for ayah in clean["ayat"]}
    for original in source_packet["ayat"]:
        if not original["root_occurrences"]:
            # These are v1's QAC-gap markers, not a claim of morphological
            # rootlessness. Keep the source's explicit qualification.
            ayat[original["ref"]].update(rootless=True, rootless_reason=original["rootless_reason"])
    focus = ayat[clean["focus_ref"]]
    context = [ayah for ayah in clean["ayat"] if ayah["ref"] != clean["focus_ref"]]
    mappings = {mapping["qac_root"]: mapping for mapping in clean["root_mappings"]}
    source_mappings = {mapping["qac_root"]: mapping for mapping in source_packet["root_mappings"]}
    inventory = {inv["mapped_root_id"]: inv["branches"] for inv in clean["branch_inventory"]}

    def root_inventory(root: str) -> dict:
        targets = []
        for target, original in zip(mappings[root]["targets"], source_mappings[root]["targets"]):
            item = {"mapped_root_id": target["furuq_root_id"],
                    "mapped_root_norm": original.get("furuq_root_norm") or root, "branches": []}
            if target.get("root_forms_ar"):
                item["root_forms_ar"] = copy.deepcopy(target["root_forms_ar"])
            for branch in inventory.get(target["furuq_root_id"], []):
                variants = [{"branch_image_ar": variant["image_ar"], "branch_image_en": variant["image_en"],
                             "scope_ar": variant["scope_ar"], "scope_en": variant["scope_en"]}
                            for variant in branch["variants"]]
                entry = {"branch_id": branch["branch_id"]}
                if len(variants) == 1:
                    entry.update(variants[0])
                else:
                    # The v1 prompt permits a shared branch ID with distinct
                    # variants. Never manufacture one merged scope or gloss.
                    entry.update(branch_image_ar=variants[0]["branch_image_ar"], variants=variants)
                item["branches"].append(entry)
            targets.append(item)
        return {"root": root, "targets": targets}

    focus_inventories = []
    for occurrence in focus["root_occurrences"]:
        item = root_inventory(occurrence["root"])
        item["source_phrases"] = [{"source_phrase_ar": " ".join(occurrence["surfaces_ar"])}]
        focus_inventories.append(item)
    focus_roots = set(focus["root_sequence"])
    context_roots = dict.fromkeys(root for ayah in context for root in ayah["root_sequence"] if root not in focus_roots)
    orientation = clean["orientation"]
    remote = {"citable": False, "refs": orientation.get("remote_refs", []),
              "root_cues": orientation.get("root_cues", []),
              "out_of_window_ayat": orientation["out_of_window_ayat"]}
    return {"protocol": V1_PACKET_PROTOCOL, "focus_ref": clean["focus_ref"], "window": clean["window"],
            "focus_ayah": focus, "context_ayat": context,
            "context_order": [ayah["ref"] for ayah in context],
            "focus_branch_inventories": focus_inventories,
            "context_root_cues": [root_inventory(root) for root in context_roots],
            "remote_orientation": remote, "source_gaps": clean["source_gaps"]}


def reader_filenames(job: dict) -> tuple[str, str]:
    """Use the paths named by the frozen prompt; never rewrite old job inputs."""
    if job["protocol"] == JOB_PROTOCOL:
        return "focus_trace_packet.json", "focus_trace/schemas/focus-trace-response.schema.json"
    return "packet.json", "response.schema.json"


def packet_index(packet: dict) -> tuple[dict, dict, dict]:
    if packet.get("protocol") == V1_PACKET_PROTOCOL:
        ayat = {ayah["ref"]: ayah for ayah in [packet["focus_ayah"], *packet["context_ayat"]]}
        mappings, variants = {}, {}
        for item in [*packet["focus_branch_inventories"], *packet["context_root_cues"]]:
            mappings[item["root"]] = {"qac_root": item["root"], "targets": [
                {"furuq_root_id": target["mapped_root_id"]} for target in item["targets"]]}
            for target in item["targets"]:
                for branch in target["branches"]:
                    for i, row in enumerate(branch.get("variants", [branch]), 1):
                        key = (target["mapped_root_id"], branch["branch_id"], f"V{i:03d}")
                        value = {"variant_id": key[2], "image_ar": row["branch_image_ar"],
                                 "image_en": row["branch_image_en"], "scope_ar": row["scope_ar"], "scope_en": row["scope_en"]}
                        require(key not in variants or variants[key] == value, "inconsistent shared branch variants")
                        variants[key] = value
        return ayat, mappings, variants
    ayat = {ayah["ref"]: ayah for ayah in packet["ayat"]}
    mappings = {mapping["qac_root"]: mapping for mapping in packet["root_mappings"]}
    variants = {(inv["mapped_root_id"], branch["branch_id"], variant["variant_id"]): variant
                for inv in packet["branch_inventory"] for branch in inv["branches"] for variant in branch["variants"]}
    return ayat, mappings, variants


def validate_packet(packet: dict) -> None:
    require(packet["protocol"] == PACKET_PROTOCOL, "not an HFT v2 packet")
    window = packet["window"]
    require(window and len(window) == len(set(window)) and packet["focus_ref"] in window, "invalid window/focus")
    require([ayah["ref"] for ayah in packet["ayat"]] == window, "missing, duplicate, or reordered ayat")
    roots = []
    for ayah in packet["ayat"]:
        require(isinstance(ayah["text_ar"], str) and bool(ayah["text_ar"].strip()), f"empty ayah text: {ayah['ref']}")
        occurrences = ayah["root_occurrences"]
        occurrence_roots = [occ["root"] for occ in occurrences]
        require(len(occurrence_roots) == len(set(occurrence_roots)), "duplicate root occurrence record")
        require(set(ayah["root_sequence"]) == set(occurrence_roots), "root sequence/occurrences mismatch")
        require(bool(occurrences) or ayah.get("rootless") is True, "missing occurrences without explicit QAC gap")
        for occurrence in occurrences:
            indices = occurrence["word_indices"]
            require(indices and len(indices) == len(set(indices)) and all(re.fullmatch(r"[1-9][0-9]*", x) for x in indices),
                    "invalid occurrence word indices")
            require(occurrence["occurrence_count"] == len(indices), "occurrence count mismatch")
            for field in ("surfaces_ar", "lemmas_ar", "pos_tags"):
                require(len(occurrence[field]) == len(indices), f"occurrence {field} mismatch")
            if occurrence["root"] not in roots:
                roots.append(occurrence["root"])
    require([mapping["qac_root"] for mapping in packet["root_mappings"]] == roots, "missing, extra, or reordered root mappings")
    inventory = {}
    empty_fields = []
    for inv in packet["branch_inventory"]:
        root_id = inv["mapped_root_id"]
        require(root_id not in inventory and inv["branches"], "duplicate or empty inventory")
        inventory[root_id] = inv
        branch_ids = set()
        for branch in inv["branches"]:
            require(branch["branch_id"] not in branch_ids and branch["variants"], "duplicate branch or missing variants")
            branch_ids.add(branch["branch_id"])
            variant_contents = set()
            for i, variant in enumerate(branch["variants"], 1):
                require(variant["variant_id"] == f"V{i:03d}" and variant["root_id"] == root_id, "bad variant identity")
                require(all(key in variant and (variant[key] is None or isinstance(variant[key], str))
                            for key in VARIANT_FIELDS), "missing or malformed branch variant fields")
                content = json_bytes({key: variant[key] for key in VARIANT_FIELDS})
                require(content not in variant_contents, "exact duplicate variant")
                variant_contents.add(content)
                fields = [field for field in ("image_ar", "scope_ar") if not variant[field]]
                if fields:
                    empty_fields.append({"mapped_root_id": root_id, "branch_id": branch["branch_id"],
                                         "variant_id": variant["variant_id"], "fields": fields})
    expected_targets, missing_targets, missing_roots = set(), set(), set()
    for mapping in packet["root_mappings"]:
        target_ids = [target["furuq_root_id"] for target in mapping["targets"]]
        require(len(target_ids) == len(set(target_ids)), "duplicate mapped target")
        if not any(root_id in inventory for root_id in target_ids):
            missing_roots.add(mapping["qac_root"])
        for target in mapping["targets"]:
            root_id = target["furuq_root_id"]
            expected_targets.add(root_id)
            branches = inventory.get(root_id, {}).get("branches", [])
            require(target["branch_count"] == len(branches), f"missing branches for {root_id}")
            require(target["variant_count"] == sum(len(b["variants"]) for b in branches), f"missing variants for {root_id}")
            if not branches:
                missing_targets.add((mapping["qac_root"], root_id))
    require(set(inventory) <= expected_targets, "unmapped inventory")
    gaps = packet["source_gaps"]
    require({gap["qac_root"] for gap in gaps["roots_without_branches"]} == missing_roots, "missing root gap diagnostics")
    require({(gap["qac_root"], gap["mapped_root_id"]) for gap in gaps["targets_without_branches"]} == missing_targets,
            "missing target gap diagnostics")
    require(gaps["missing_arabic_fields"] == empty_fields, "missing Arabic field diagnostics")
    require(gaps["ayat_without_qac_roots"] == [a["ref"] for a in packet["ayat"] if not a["root_occurrences"]],
            "missing QAC gap diagnostics")
    require(packet["orientation"]["citable"] is False, "orientation must be non-citable")


def check_schema_keywords(schema: dict) -> None:
    require(set(schema) <= SCHEMA_KEYWORDS, f"unsupported schema keywords: {set(schema) - SCHEMA_KEYWORDS}")
    for keyword in ("$defs", "properties"):
        for child in schema.get(keyword, {}).values():
            check_schema_keywords(child)
    if "items" in schema:
        check_schema_keywords(schema["items"])
    for keyword in ("if", "then", "not"):
        if keyword in schema:
            check_schema_keywords(schema[keyword])
    for child in schema.get("allOf", []):
        check_schema_keywords(child)


def validate_shape(value: Any, schema: dict, root: dict | None = None, path: str = "response") -> None:
    """Validate the small JSON Schema subset used by our checked-in response contract.

    No dependency install is needed. Unknown keywords fail closed, not silently.
    This is not a general-purpose JSON Schema implementation.
    """
    if root is None:
        check_schema_keywords(schema)  # Also inspect definitions for empty response arrays.
        root = schema
    if "$ref" in schema:
        require(set(schema) == {"$ref"} and schema["$ref"].startswith("#/$defs/"), f"{path}: unsupported schema ref")
        validate_shape(value, root["$defs"][schema["$ref"].split("/")[-1]], root, path)
        return
    for child in schema.get("allOf", []):
        validate_shape(value, child, root, path)
    if "not" in schema:
        try:
            validate_shape(value, schema["not"], root, path)
        except ValueError:
            pass
        else:
            raise ValueError(f"{path}: forbidden schema condition")
    if "if" in schema:
        try:
            validate_shape(value, schema["if"], root, path)
        except ValueError:
            pass
        else:
            if "then" in schema:
                validate_shape(value, schema["then"], root, path)
    if "type" in schema:
        types = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        checks = {"object": isinstance(value, dict), "array": isinstance(value, list),
                  "string": isinstance(value, str), "null": value is None}
        require(all(kind in checks for kind in types) and any(checks[kind] for kind in types), f"{path}: expected {types}")
    if "const" in schema:
        require(value == schema["const"], f"{path}: incorrect constant")
    if "enum" in schema:
        require(value in schema["enum"], f"{path}: invalid value")
    if isinstance(value, dict):
        require(set(schema.get("required", [])) <= value.keys(), f"{path}: missing required fields")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            require(value.keys() <= properties.keys(), f"{path}: unexpected fields: {value.keys() - properties.keys()}")
        for key, item in value.items():
            if key in properties:
                validate_shape(item, properties[key], root, f"{path}.{key}")
    elif isinstance(value, list):
        require(len(value) >= schema.get("minItems", 0), f"{path}: too few items")
        if schema.get("uniqueItems"):
            require(len({json_bytes(item) for item in value}) == len(value), f"{path}: duplicate items")
        for i, item in enumerate(value):
            if "items" in schema:
                validate_shape(item, schema["items"], root, f"{path}[{i}]")
    elif isinstance(value, str):
        require(len(value.strip()) >= schema.get("minLength", 0), f"{path}: empty string")
        if "pattern" in schema:
            require(re.search(schema["pattern"], value) is not None, f"{path}: invalid string format")


def resolve_branch(citation: dict, index: tuple[dict, dict, dict]) -> dict:
    ayat, mappings, variants = index
    ref, root = citation["source_ref"], citation["root"]
    require(ref in ayat, f"branch source is outside citable window: {ref}")
    occurrence = next((occ for occ in ayat[ref]["root_occurrences"] if occ["root"] == root), None)
    require(occurrence is not None, f"root does not occur at {ref}: {root}")
    indices = citation["source_word_indices"]
    require(indices == occurrence["word_indices"], f"incorrect source_word_indices at {ref}: {root}")
    target = next((t for t in mappings.get(root, {}).get("targets", [])
                   if t["furuq_root_id"] == citation["mapped_root_id"]), None)
    require(target is not None, f"mapped root is not a target of {root}")
    if "variant_id" not in citation:
        matches = [variant for key, variant in variants.items()
                   if key[:2] == (citation["mapped_root_id"], citation["branch_id"])]
        require(matches, f"unknown branch: {citation['mapped_root_id']}/{citation['branch_id']}")
        # A v1 citation identifies the branch, not a machine-selected variant.
        # Preserve ALL candidate rows and the reader's role; never guess V001.
        return {"citation": copy.deepcopy(citation), "source_ayah_ar": ayat[ref]["text_ar"],
                "source_occurrence": copy.deepcopy(occurrence), "mapping_target": copy.deepcopy(target),
                "variants": copy.deepcopy(matches)}
    key = (citation["mapped_root_id"], citation["branch_id"], citation["variant_id"])
    require(key in variants, f"unknown branch variant: {key}")
    return {"citation": copy.deepcopy(citation), "source_ayah_ar": ayat[ref]["text_ar"],
            "source_occurrence": copy.deepcopy(occurrence), "mapping_target": copy.deepcopy(target),
            "variant": copy.deepcopy(variants[key])}


def validate_response(response: dict, packet: dict, job: dict, schema: dict) -> None:
    validate_shape(response, schema)
    require(response["focus_ref"] == packet["focus_ref"], "response focus mismatch")
    if job["protocol"] == JOB_PROTOCOL:
        validate_v1_response(response, packet, job)
        return
    if job["protocol"] == LEGACY_JOB_PROTOCOL:
        require(response["reader_id"] == job["reader_id"], "response reader mismatch")
        require(response["input_identity"] == job["input_identity"], "response is not bound to these frozen inputs")
    index = packet_index(packet)
    ayat = index[0]
    focus = packet["focus_ref"]
    ids = set()
    for section in SECTIONS:
        for finding in response[section]:
            require(finding["model_id"] not in ids, "duplicate model_id across retained findings")
            ids.add(finding["model_id"])
            require(finding["focus_anchor"]["quote_ar"] in ayat[focus]["text_ar"], "focus anchor is not an exact focus quotation")
            refs = []
            for citation in finding["activation_trace"]:
                resolve_branch(citation, index)
                refs.append(citation["source_ref"])
            for citation in finding["structural_cues"]:
                ref = citation["source_ref"]
                require(ref in ayat, f"text source is outside citable window: {ref}")
                require(citation["quote_ar"] in ayat[ref]["text_ar"], f"inexact Arabic quote at {ref}")
                refs.append(ref)
            if section == "baseline_models":
                require(all(ref == focus for ref in refs), "baseline cites context")
                require(finding["changed_reading"] is None, "baseline must have null changed_reading")
            if section == "context_deltas":
                require(any(ref != focus for ref in refs), "context delta has no context evidence")
                require(finding["changed_reading"] is not None, "context delta needs before/after")
            if finding["changed_reading"] is not None:
                change = finding["changed_reading"]
                require(change["before"].strip() != change["after"].strip(), "unchanged before/after")
            if section == "surprising_valid_outliers":
                require(finding["status"] == "exploratory", "outliers must remain exploratory")


def validate_v1_response(response: dict, packet: dict, job: dict) -> None:
    """V1's response semantics, without v2's extra finding/quotation requirements."""
    require(response["protocol"] == RESPONSE_PROTOCOL, "response protocol mismatch")
    require(response["reader_id"] == job["reader_id"], "response reader mismatch")
    index = packet_index(packet)
    focus = packet["focus_ref"]
    rootless = not index[0][focus]["root_occurrences"]
    require("rootless_focus" not in response or response["rootless_focus"] is True,
            "rootless_focus must be true when present")
    require((response.get("rootless_focus") is True) == rootless, "rootless_focus must match QAC annotation gap")
    model_ids, outlier_ids = set(), set()
    for section in SECTIONS:
        for finding in response[section]:
            is_outlier = section == "surprising_valid_outliers"
            identifier = finding["outlier_id" if is_outlier else "model_id"]
            seen = outlier_ids if is_outlier else model_ids
            require(identifier not in seen, "duplicate finding ID")
            seen.add(identifier)
            context_refs, context_roots = set(), set()
            for citation in finding["activation_trace"]:
                resolve_branch(citation, index)
                ref = citation["source_ref"]
                if section == "baseline_models":
                    require(ref == focus, "baseline cites context")
                if ref != focus:
                    context_refs.add(ref)
                    context_roots.add(citation["root"])
            if section == "context_deltas":
                require(context_refs, "v1 context delta needs a branch-backed context citation")
                require(set(finding["trigger_roots"]) == context_roots, "trigger_roots do not match context citations")
                if "trigger_refs" in finding:
                    require(set(finding["trigger_refs"]) == context_refs, "trigger_refs do not match context citations")


def profile_prompt(prompt: bytes, model: str, reasoning_effort: str) -> bytes:
    """Change only the coordinator's explicit profile block, never discovery text."""
    require(model in MODELS, "unsupported model profile")
    require(reasoning_effort in REASONING_EFFORTS, "unsupported reasoning effort")
    original = b"model: gpt-5.6-sol\nreasoning_effort: max\n"
    require(prompt.count(original) == 1, "original v1 profile block is missing or ambiguous")
    requested = f"model: {model}\nreasoning_effort: {reasoning_effort}\n".encode("utf-8")
    return prompt.replace(original, requested, 1)


def prompt_sections(prompt: bytes) -> dict[str | bytes, bytes]:
    parts = re.split(rb"(?m)^(## [^\n]+\n)", prompt)
    headings = parts[1::2]
    require(len(headings) == len(set(headings)), "duplicate prompt heading")
    return {"intro": parts[0], **dict(zip(headings, parts[2::2]))}


def two_stage_prompts(prompt: bytes, model: str, effort: str) -> dict[str, bytes]:
    discovery = profile_prompt((WORKFLOW_ROOT / "prompts/discovery_two_stage.md").read_bytes(), model, effort)
    original, staged = prompt_sections(prompt), prompt_sections(discovery)
    require(list(original) == list(staged), "two-stage prompt must preserve v1 heading order")
    for section in ("intro", b"## Reader Posture\n", b"## Core Task\n"):
        require(staged[section] == original[section], f"two-stage changed protected v1 section: {section}")
    discovery_goal = prompt.split(b"For `surprising_valid_outliers`, record readings", 1)[1].split(b"\nAfter writing valid JSON", 1)[0]
    require(b"For `surprising_valid_outliers`, record readings" + discovery_goal in discovery,
            "two-stage changed v1's discovery goal in Output")
    reporting = b"## Required Evidence Discipline\n" + prompt.split(b"## Required Evidence Discipline\n", 1)[1]
    followup = (WORKFLOW_ROOT / "prompts/ledger_followup.md").read_bytes() + b"\n" + reporting
    return dict(zip(TWO_STAGE_PROMPTS, (discovery, followup)))


def validate_discovery(notes: dict) -> set[str]:
    """Check lightweight handoff structure, not interpretation or discovery quality."""
    require(isinstance(notes, dict) and set(notes) == set(SECTIONS), "discovery needs the three v1 finding arrays")
    identifiers = set()
    for section in SECTIONS:
        require(isinstance(notes[section], list), f"discovery {section} must be an array")
        for item in notes[section]:
            require(isinstance(item, dict) and set(item) == {"id", "discovery", "cues"}, "discovery entry needs id, discovery, cues only")
            require(all(isinstance(value, str) and value.strip() for value in item.values()), "empty discovery note")
            require(re.fullmatch(r"[A-Za-z0-9_-]+", item["id"]) is not None, "unsafe discovery ID")
            require(item["id"] not in identifiers, "duplicate discovery ID")
            identifiers.add(item["id"])
    require(notes["baseline_models"], "discovery needs a focus-only baseline")
    return identifiers


def completed_discovery(job_dir: Path, job: dict) -> tuple[dict, dict]:
    notes = read_json(job_dir / "discovery.json")
    validate_discovery(notes)
    receipt = read_json(job_dir / "discovery.result.json")
    require(receipt["exit_code"] == 0, "discovery did not complete successfully")
    require(receipt["discovery_sha256"] == digest((job_dir / "discovery.json").read_bytes()), "discovery notes changed after completion")
    require(receipt["input_identity"] == job["input_identity"] and receipt["two_stage_inputs"] == job["two_stage_inputs"],
            "discovery receipt belongs to different inputs")
    require(receipt["requested_profile"] == job["requested_profile"], "discovery profile mismatch")
    require(re.fullmatch(r"[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}", receipt["thread_id"]) is not None,
            "discovery needs an explicit session UUID")
    return notes, receipt


def validate_candidate_coverage(notes: dict, response: dict) -> None:
    expected = validate_discovery(notes)
    accounted = []
    for section in SECTIONS:
        accounted.extend(item["outlier_id" if section == "surprising_valid_outliers" else "model_id"] for item in response[section])
    for note in response.get("discarded_or_unchanged", []):
        match = re.fullmatch(r"([A-Za-z0-9_-]+):\s*(\S[\s\S]*)", note)
        require(match is not None, "two-stage withdrawal needs ID: specific reason")
        accounted.append(match[1])
    require(len(accounted) == len(set(accounted)), "candidate retained or withdrawn more than once")
    require(set(accounted) == expected,
            f"candidate coverage mismatch; missing={sorted(expected - set(accounted))}, extra={sorted(set(accounted) - expected)}")


def write_job(job_dir: Path, packet: dict, source_files: list, *, model: str = "gpt-5.6-sol",
              reasoning_effort: str = "max", reader_id: str = "reader_hft_a",
              selection: dict | None = None, two_stage: bool = False) -> dict:
    """Freeze a NEW job. Refuse every overwrite, including partial prior preparation."""
    require(model in MODELS, "unsupported model profile")
    require(reasoning_effort in REASONING_EFFORTS, "unsupported reasoning effort")
    require(re.fullmatch(r"[A-Za-z0-9_-]+", reader_id) is not None, "unsafe reader ID")
    validate_packet(packet)
    prompt = (WORKFLOW_ROOT / "prompts/discovery.md").read_bytes()
    schema = (WORKFLOW_ROOT / "schemas/response.schema.json").read_bytes()
    require(prompt == V1_PROMPT.read_bytes(), "v1 discovery prompt must remain unchanged")
    require(schema == V1_SCHEMA.read_bytes(), "v1 response schema must remain unchanged")
    prompt = profile_prompt(prompt, model, reasoning_effort)
    projected = v1_reader_packet(packet)
    focus = projected["focus_ayah"]
    require(not focus["root_occurrences"] or any(target["branches"] for item in projected["focus_branch_inventories"]
            for target in item["targets"]),
            "v1 requires a branch-backed baseline, but the rooted focus has no branch inventory; do not invent a branch or label it rootless")
    packet_name, schema_name = reader_filenames({"protocol": JOB_PROTOCOL})
    frozen = {packet_name: json_bytes(projected), "source.packet.json": json_bytes(packet),
              "prompt.md": prompt, schema_name: schema}
    identity = {"packet_sha256": digest(frozen[packet_name]), "prompt_sha256": digest(prompt), "schema_sha256": digest(schema)}
    job = {
        "protocol": JOB_PROTOCOL,
        "response_protocol": RESPONSE_PROTOCOL,
        "focus_ref": packet["focus_ref"],
        "reader_id": reader_id,
        "requested_profile": {"model": model, "reasoning_effort": reasoning_effort},
        "execution_verified": False,
        "input_identity": identity,
        "source_packet_sha256": digest(frozen["source.packet.json"]),
        "source_files": source_files,
        "builder_files": snapshot([Path(__file__), SOURCE_LOADER, REPO_ROOT / "v12/scripts/build_packets.py"]),
        "selection": selection or {"mode": "explicit_window"},
    }
    if two_stage:
        extra = two_stage_prompts(prompt, model, reasoning_effort)
        frozen.update(extra)
        job["two_stage_inputs"] = {name: digest(data) for name, data in extra.items()}
    frozen["job.json"] = json_bytes(job)
    job_dir.mkdir(parents=True, exist_ok=False)
    for name, data in frozen.items():
        path = job_dir / name
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as handle:
            handle.write(data)
    return job


def load_job(job_dir: Path, *, require_response: bool = True,
             require_ledger_completion: bool = True) -> tuple[dict, dict, dict | None]:
    job = read_json(job_dir / "job.json")
    require(job["protocol"] in {JOB_PROTOCOL, PREVIOUS_JOB_PROTOCOL, LEGACY_JOB_PROTOCOL}, "not an HFT v2 job")
    require(set(job["input_identity"]) == {"packet_sha256", "prompt_sha256", "schema_sha256"}, "incomplete input identity")
    packet_name, schema_name = reader_filenames(job)
    for filename, key in ((packet_name, "packet_sha256"), ("prompt.md", "prompt_sha256"), (schema_name, "schema_sha256")):
        require(digest((job_dir / filename).read_bytes()) == job["input_identity"][key], f"frozen input changed: {filename}")
    if "two_stage_inputs" in job:
        require(job["protocol"] == JOB_PROTOCOL and set(job["two_stage_inputs"]) == set(TWO_STAGE_PROMPTS), "invalid two-stage job")
        for filename, expected in job["two_stage_inputs"].items():
            require(digest((job_dir / filename).read_bytes()) == expected, f"frozen input changed: {filename}")
        if (job_dir / "discovery.json").exists():
            validate_discovery(read_json(job_dir / "discovery.json"))
    packet = read_json(job_dir / packet_name)
    if job["protocol"] == LEGACY_JOB_PROTOCOL:
        assignment = read_json(job_dir / "assignment.json")
        require(assignment == {"focus_ref": job["focus_ref"], "reader_id": job["reader_id"],
                               "input_identity": job["input_identity"], "response_file": "response.json"}, "assignment mismatch")
        validate_packet(packet)
    else:
        source_path = job_dir / "source.packet.json"
        require(digest(source_path.read_bytes()) == job["source_packet_sha256"], "frozen input changed: source.packet.json")
        source_packet = read_json(source_path)
        validate_packet(source_packet)
        projection = v1_reader_packet if job["protocol"] == JOB_PROTOCOL else reader_packet
        require(packet == projection(source_packet), "reader packet differs from complete source projection")
        expected_protocol = RESPONSE_PROTOCOL if job["protocol"] == JOB_PROTOCOL else PREVIOUS_RESPONSE_PROTOCOL
        require(job["response_protocol"] == expected_protocol, "unexpected coordinator response protocol")
        if job["protocol"] == JOB_PROTOCOL:
            profile = job["requested_profile"]
            require(profile["model"] in MODELS and profile["reasoning_effort"] in REASONING_EFFORTS,
                    "unsupported frozen profile")
            block = f"model: {profile['model']}\nreasoning_effort: {profile['reasoning_effort']}\n".encode("utf-8")
            require((job_dir / "prompt.md").read_bytes().count(block) == 1,
                    "frozen prompt profile does not match requested runtime profile")
    require(job["focus_ref"] == packet["focus_ref"], "job focus mismatch")
    response = None
    response_path = job_dir / "response.json"
    if require_response or response_path.exists():
        response = read_json(response_path)
        validate_response(response, packet, job, read_json(job_dir / schema_name))
        if "two_stage_inputs" in job:
            notes, discovery = completed_discovery(job_dir, job)
            validate_candidate_coverage(notes, response)
            if require_ledger_completion:
                receipt = read_json(job_dir / "ledger.result.json")
                require(receipt["exit_code"] == 0 and receipt.get("response_valid") is True, "ledger did not complete successfully")
                require(receipt["thread_id"] == discovery["thread_id"], "ledger session differs from discovery")
                require(receipt["response_sha256"] == digest(response_path.read_bytes()), "ledger changed after completion")
    return job, packet, response


def evidence_payload(job: dict, packet: dict, response: dict) -> dict:
    """Resolve ALL retained citations; do not rank, prune, or synthesize findings."""
    index = packet_index(packet)
    resolved = []
    for section in SECTIONS:
        for finding in response[section]:
            resolved.append({
                "section": section, "model_id": finding.get("model_id", finding.get("outlier_id")),
                "focus_ayah_ar": index[0][packet["focus_ref"]]["text_ar"],
                "branches": [resolve_branch(citation, index) for citation in finding["activation_trace"]],
                "structural_cues": copy.deepcopy(finding.get("structural_cues", [])) if job["protocol"] == JOB_PROTOCOL else [
                                    {"citation": copy.deepcopy(citation),
                                     "source_ayah_ar": index[0][citation["source_ref"]]["text_ar"]}
                                    for citation in finding["structural_cues"]],
            })
    return {"protocol": EVIDENCE_PROTOCOL, "focus_ref": packet["focus_ref"],
            "input_identity": copy.deepcopy(job["input_identity"]),
            "requested_profile": copy.deepcopy(job["requested_profile"]),
            "execution_verified": False,
            "response_sha256": digest(json_bytes(response)), "response_hash_encoding": "compact-utf8-json-with-lf",
            "response": copy.deepcopy(response), "resolved_evidence": resolved,
            "source_gaps": copy.deepcopy(packet["source_gaps"]),
            "source_files": copy.deepcopy(job["source_files"])}


def export_job(job_dir: Path) -> Path:
    require((WORKFLOW_ROOT / "runs").resolve().is_relative_to(WORKFLOW_ROOT.resolve()), "runs path escapes HFT v2")
    require(job_dir.resolve().is_relative_to((WORKFLOW_ROOT / "runs").resolve()), "CLI exports must stay under focus_trace_v2/runs")
    job, packet, response = load_job(job_dir)
    output = job_dir / "evidence.json"
    # Resolve provenance from the verified coordinator snapshot, never ask the
    # reader to repeat it. Preserve old export behavior for already-frozen jobs.
    source_packet = read_json(job_dir / "source.packet.json") if job["protocol"] != LEGACY_JOB_PROTOCOL else packet
    evidence = evidence_payload(job, source_packet, response)
    if job["protocol"] != LEGACY_JOB_PROTOCOL:
        evidence.update(reader_id=job["reader_id"], response_protocol=job["response_protocol"],
                        source_packet_sha256=job["source_packet_sha256"], binding="coordinator_job_directory")
    if "two_stage_inputs" in job:
        notes, _ = completed_discovery(job_dir, job)
        evidence.update(discovery_notes=notes, two_stage_inputs=copy.deepcopy(job["two_stage_inputs"]))
    data = json_bytes(evidence)
    if output.exists():
        require(output.read_bytes() == data, "evidence.json already exists with different content; use a new job")
    else:
        with output.open("xb") as handle:
            handle.write(data)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prepare = commands.add_parser("prepare", help="prepare inputs only; never launch a model")
    prepare.add_argument("--ayah", required=True)
    prepare.add_argument("--run", required=True, help="new run name, e.g. v1-compatible-sol")
    scope = prepare.add_mutually_exclusive_group()
    scope.add_argument("--window", help="e.g. 29:1-69 or 29:35,29:36,29:37,29:38")
    scope.add_argument("--window-from", type=Path, help="reuse only an old packet's window and non-citable remote orientation")
    prepare.add_argument("--model", choices=MODELS, default="gpt-5.6-sol")
    prepare.add_argument("--reasoning-effort", choices=REASONING_EFFORTS, default="max")
    prepare.add_argument("--reader-id", default="reader_hft_a")
    prepare.add_argument("--two-stage", action="store_true", help="opt in to discovery notes, then same-session v1 ledger; no generation")
    validate = commands.add_parser("validate", help="validate frozen inputs AND response")
    validate.add_argument("job_dir", type=Path)
    validate.add_argument("--inputs-only", action="store_true", help="allow no response; still check it if one exists")
    export = commands.add_parser("export", help="write resolved evidence.json; no V5 cutover")
    export.add_argument("job_dir", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            require(re.fullmatch(r"[A-Za-z0-9_-]+", args.run) is not None, "unsafe run name")
            refs = parse_window(args.ayah)
            require(len(refs) == 1 and not refs[0].endswith(":0"), "--ayah requires one numbered reference")
            focus = refs[0]
            job_dir = WORKFLOW_ROOT / "runs" / args.run / focus.replace(":", "_")
            require(job_dir.resolve().is_relative_to(WORKFLOW_ROOT.resolve()), "run path escapes HFT v2")
            require(not job_dir.exists(), f"job already exists; use a new --run: {job_dir}")
            remote = None
            selection = {"mode": "explicit_window"}
            if args.window:
                window = parse_window(args.window)
            else:
                old_path = args.window_from or (REPO_ROOT / "focus_trace/runs" / f"s{focus.split(':')[0]}" / "packets" / f"{focus.replace(':', '_')}.packet.json")
                old_data = old_path.read_bytes()
                old = read_json(old_path)
                require(old.get("focus_ref") == focus, "window source belongs to a different focus ayah")
                window, remote = old["window"], old.get("remote_orientation")
                require(old_path.read_bytes() == old_data, "window source changed during preparation")
                selection = {"mode": "legacy_window_only", "path": str(old_path.resolve()), "sha256": digest(old_data)}
            packet, source_files = build_packet(focus, window, remote_orientation=remote)
            job = write_job(job_dir, packet, source_files, model=args.model,
                            reasoning_effort=args.reasoning_effort, reader_id=args.reader_id, selection=selection,
                            two_stage=args.two_stage)
            load_job(job_dir, require_response=False)
            print(json.dumps({"prepared": str(job_dir), "profile": job["requested_profile"],
                              "packet_bytes": (job_dir / reader_filenames(job)[0]).stat().st_size,
                              "source_gaps": packet["source_gaps"]}, ensure_ascii=False))
        elif args.command == "validate":
            _, packet, response = load_job(args.job_dir, require_response=not args.inputs_only)
            print(json.dumps({"valid": True, "focus_ref": packet["focus_ref"],
                              "response_checked": response is not None}, ensure_ascii=False))
        else:
            print(export_job(args.job_dir))
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f"HFT v2: {error}\n")


if __name__ == "__main__":
    main()
