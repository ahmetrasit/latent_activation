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
RESPONSE_PROTOCOL = "hft-v2-response-v2"
JOB_PROTOCOL = "hft-v2-job-v2"
LEGACY_JOB_PROTOCOL = "hft-v2-job-v1"
EVIDENCE_PROTOCOL = "hft-v2-evidence-v1"
MODELS = ("gpt-5.6-luna", "gpt-5.6-sol", "gpt-6-astra")
SECTIONS = ("baseline_models", "context_deltas", "surprising_valid_outliers")
VARIANT_FIELDS = ("root_id", "source_path", "image_ar", "image_en", "scope_ar", "scope_en")
LINGUISTIC_VARIANT_FIELDS = ("image_ar", "image_en", "scope_ar", "scope_en")
SCHEMA_KEYWORDS = {"$schema", "$id", "$defs", "$ref", "title", "description", "type", "const", "enum",
                   "properties", "required", "additionalProperties", "items", "minItems", "uniqueItems", "minLength", "pattern"}


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


def packet_index(packet: dict) -> tuple[dict, dict, dict]:
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
    key = (citation["mapped_root_id"], citation["branch_id"], citation["variant_id"])
    require(key in variants, f"unknown branch variant: {key}")
    return {"citation": copy.deepcopy(citation), "source_ayah_ar": ayat[ref]["text_ar"],
            "source_occurrence": copy.deepcopy(occurrence), "mapping_target": copy.deepcopy(target),
            "variant": copy.deepcopy(variants[key])}


def validate_response(response: dict, packet: dict, job: dict, schema: dict) -> None:
    validate_shape(response, schema)
    require(response["focus_ref"] == packet["focus_ref"], "response focus mismatch")
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


def write_job(job_dir: Path, packet: dict, source_files: list, *, model: str = MODELS[0],
              reader_id: str = "reader_hft_v2_a", selection: dict | None = None) -> dict:
    """Freeze a NEW job. Refuse every overwrite, including partial prior preparation."""
    require(model in MODELS, "unsupported model profile")
    require(re.fullmatch(r"[A-Za-z0-9_-]+", reader_id) is not None, "unsafe reader ID")
    validate_packet(packet)
    prompt = (WORKFLOW_ROOT / "prompts/discovery.md").read_bytes()
    schema = (WORKFLOW_ROOT / "schemas/response.schema.json").read_bytes()
    frozen = {"packet.json": json_bytes(reader_packet(packet)), "source.packet.json": json_bytes(packet),
              "prompt.md": prompt, "response.schema.json": schema}
    identity = {"packet_sha256": digest(frozen["packet.json"]), "prompt_sha256": digest(prompt), "schema_sha256": digest(schema)}
    job = {
        "protocol": JOB_PROTOCOL,
        "response_protocol": RESPONSE_PROTOCOL,
        "focus_ref": packet["focus_ref"],
        "reader_id": reader_id,
        "requested_profile": {"model": model, "reasoning_effort": "max"},
        "execution_verified": False,
        "input_identity": identity,
        "source_packet_sha256": digest(frozen["source.packet.json"]),
        "source_files": source_files,
        "builder_files": snapshot([Path(__file__), SOURCE_LOADER, REPO_ROOT / "v12/scripts/build_packets.py"]),
        "selection": selection or {"mode": "explicit_window"},
    }
    frozen["job.json"] = json_bytes(job)
    job_dir.mkdir(parents=True, exist_ok=False)
    for name, data in frozen.items():
        with (job_dir / name).open("xb") as handle:
            handle.write(data)
    return job


def load_job(job_dir: Path, *, require_response: bool = True) -> tuple[dict, dict, dict | None]:
    job = read_json(job_dir / "job.json")
    require(job["protocol"] in {JOB_PROTOCOL, LEGACY_JOB_PROTOCOL}, "not an HFT v2 job")
    require(set(job["input_identity"]) == {"packet_sha256", "prompt_sha256", "schema_sha256"}, "incomplete input identity")
    for filename, key in (("packet.json", "packet_sha256"), ("prompt.md", "prompt_sha256"), ("response.schema.json", "schema_sha256")):
        require(digest((job_dir / filename).read_bytes()) == job["input_identity"][key], f"frozen input changed: {filename}")
    packet = read_json(job_dir / "packet.json")
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
        require(packet == reader_packet(source_packet), "reader packet differs from complete source projection")
        require(job["response_protocol"] == RESPONSE_PROTOCOL, "unexpected coordinator response protocol")
    require(job["focus_ref"] == packet["focus_ref"], "job focus mismatch")
    response = None
    response_path = job_dir / "response.json"
    if require_response or response_path.exists():
        response = read_json(response_path)
        validate_response(response, packet, job, read_json(job_dir / "response.schema.json"))
    return job, packet, response


def evidence_payload(job: dict, packet: dict, response: dict) -> dict:
    """Resolve ALL retained citations; do not rank, prune, or synthesize findings."""
    index = packet_index(packet)
    resolved = []
    for section in SECTIONS:
        for finding in response[section]:
            resolved.append({
                "section": section, "model_id": finding["model_id"],
                "focus_ayah_ar": index[0][packet["focus_ref"]]["text_ar"],
                "branches": [resolve_branch(citation, index) for citation in finding["activation_trace"]],
                "structural_cues": [{"citation": copy.deepcopy(citation),
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
    source_packet = read_json(job_dir / "source.packet.json") if job["protocol"] == JOB_PROTOCOL else packet
    evidence = evidence_payload(job, source_packet, response)
    if job["protocol"] == JOB_PROTOCOL:
        evidence.update(reader_id=job["reader_id"], response_protocol=job["response_protocol"],
                        source_packet_sha256=job["source_packet_sha256"], binding="coordinator_job_directory")
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
    prepare.add_argument("--run", required=True, help="new run name, e.g. pilot-luna")
    scope = prepare.add_mutually_exclusive_group()
    scope.add_argument("--window", help="e.g. 29:1-69 or 29:35,29:36,29:37,29:38")
    scope.add_argument("--window-from", type=Path, help="reuse only an old packet's window and non-citable remote orientation")
    prepare.add_argument("--model", choices=MODELS, default=MODELS[0])
    prepare.add_argument("--reader-id", default="reader_hft_v2_a")
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
            job = write_job(job_dir, packet, source_files, model=args.model, reader_id=args.reader_id, selection=selection)
            load_job(job_dir, require_response=False)
            print(json.dumps({"prepared": str(job_dir), "profile": job["requested_profile"],
                              "packet_bytes": (job_dir / "packet.json").stat().st_size,
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
