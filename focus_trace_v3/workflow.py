#!/usr/bin/env python3
"""Prepare sealed v1-derived reader inputs and compile evidence handles offline."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_focus_trace_packet as base
import build_pericope_focus_trace_packet as lean
import validate_focus_trace as validator

PACKET_PROTOCOL = "focus-trace-v3-packet-v1"
READER_PROTOCOL = "focus-trace-v3-reader-response-v1"
SECTIONS = ("baseline_models", "context_deltas", "surprising_valid_outliers")
MODELS = ("gpt-5.6-sol", "gpt-5.6-luna")
PROMPT_REVISIONS = ("initial", "v1-discovery")


def read(path: Path) -> dict:
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_keys)


def encode(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False) + "\n").encode()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def build_source(focus: str, window: list[str]) -> dict:
    """Read linguistic data using the copied v1 loaders, retaining source variants."""
    require(len(window) == len(set(window)), "duplicate window reference")
    base.validate_window_refs(base.DEFAULT_QURAN_DIR, focus, window)
    require(all(base.surah_of(ref) == base.surah_of(focus) for ref in window), "cross-surah window")
    by_ref = base.load_window_ayat(base.DEFAULT_QAC, base.DEFAULT_QURAN_DIR, window)
    focus_ayah = by_ref[focus]
    context = [by_ref[ref] for ref in window if ref != focus]
    roots = base.ordered_packet_roots([focus_ayah], context)
    mappings = base.load_root_mappings(base.DEFAULT_QAC_FURUQ_ROOT_MAP, roots)
    base.validate_repair_occurrences([focus_ayah, *context], mappings)
    branches, missing, missing_targets = base.load_branches_for_mapped_roots(base.DEFAULT_BRANCH_DB, mappings)
    files = [base.DEFAULT_QAC, base.DEFAULT_BRANCH_DB, base.DEFAULT_QAC_FURUQ_ROOT_MAP,
             base.ROOT_MAPPING_REPAIRS, base.quran_surah_path(base.DEFAULT_QURAN_DIR, base.surah_of(focus))]
    return {
        "focus_ref": focus, "window": window, "focus_ayah": focus_ayah,
        "context_ayat": context, "root_mappings": mappings, "branches": branches,
        "missing_roots": missing, "missing_targets": missing_targets,
        "surah_text": base.surah_text_context(base.DEFAULT_QURAN_DIR, base.surah_of(focus)),
        "resource_sha256": {base.resource_key(path): base.sha256(path) for path in files},
    }


def branch_projection(branch: dict, english: bool, *, compact: bool = False) -> dict:
    # The v1 loader retains original paired rows even when display fields are combined.
    fields = {"image_ar": "branch_image_ar", "scope_ar": "scope_ar"}
    if english:
        fields.update(image_en="branch_image_en", scope_en="scope_en")
    if compact:
        fields.pop("scope_ar")
        fields.pop("scope_en", None)
    variants = []
    for row in branch["variants"]:
        variant = {output: row.get(source) or "" for source, output in fields.items()}
        if variant not in variants:
            variants.append(variant)
    require(bool(variants) and all(v["branch_image_ar"] for v in variants), "missing Arabic branch image")
    result = {"branch_id": branch["branch_id"], "branch_key": f"{branch['mapped_root_id']}/{branch['branch_id']}"}
    if compact:
        del result["branch_key"]
    if len(variants) == 1:
        result.update(variants[0])
    else:
        # A display label is not a selected source variant. Keep every original pair.
        result["branch_image_ar"] = branch["image_ar"]
        result["variants"] = variants
    return result


def project_packet(source: dict, *, english: bool = False, context_scopes: bool = False) -> dict:
    def ayah(row):
        result = lean.lean_ayah(copy.deepcopy(row))
        for index, occurrence in enumerate(result["root_occurrences"], 1):
            occurrence["occurrence_id"] = f"{row['ref']}/r{index:02d}"
        return result

    def inventory(root, *, compact=False):
        groups = {}
        for branch in source["branches"][root]:
            group = groups.setdefault(branch["mapped_root_id"], {
                "mapped_root_id": branch["mapped_root_id"],
                "mapped_root_norm": branch["mapped_root_norm"], "branches": [],
            })
            group["branches"].append(branch_projection(branch, english, compact=compact))
        return {"root": root, "targets": list(groups.values())}

    focus_roots = base.first_seen_roots([source["focus_ayah"]])
    context_roots = base.first_seen_roots(source["context_ayat"])
    focus_inventories = [inventory(root) for root in focus_roots if source["branches"][root]]
    require(not focus_roots or bool(focus_inventories), "rooted focus has no branch-backed baseline; repair its input first")
    packet = {
        "protocol": PACKET_PROTOCOL, "focus_ref": source["focus_ref"], "window": source["window"],
        "context_order": [row["ref"] for row in source["context_ayat"]], "ayah_count": len(source["window"]),
        "focus_ayah": ayah(source["focus_ayah"]), "context_ayat": [ayah(row) for row in source["context_ayat"]],
        "surah_text": lean.lean_surah_text(source["surah_text"]),
        "focus_branch_inventories": focus_inventories,
        "context_root_cues": [inventory(root, compact=not context_scopes) for root in context_roots if root not in focus_roots and source["branches"][root]],
        "remote_orientation": {"citable": False, "refs": [], "root_cues": []},
        "source_gaps": {
            "roots_without_inventory": source["missing_roots"],
            "mapped_targets_without_inventory": [
                {key: row[key] for key in ("qac_root", "furuq_root_id", "reason")}
                for row in source["missing_targets"]
            ],
        },
    }
    validator.validate_packet(validation_view(packet))
    evidence_index(packet)
    return packet


def validation_view(packet: dict) -> dict:
    """A compatibility view for the original validator, not a reader projection."""
    result = copy.deepcopy(packet)
    require(result.pop("source_gaps", None) is not None, "missing source-gap record")
    require(result["protocol"] == PACKET_PROTOCOL, "wrong packet protocol")
    result["protocol"] = lean.PROTOCOL
    for ayah in [result["focus_ayah"], *result["context_ayat"]]:
        for occurrence in ayah["root_occurrences"]:
            occurrence.pop("occurrence_id")
    for collection in ("focus_branch_inventories", "context_root_cues"):
        for inv in result[collection]:
            for target in inv["targets"]:
                for branch in target["branches"]:
                    for key in ("branch_key", "variants", "branch_image_en", "scope_en"):
                        branch.pop(key, None)
    return result


def evidence_index(packet: dict) -> tuple[dict, dict]:
    occurrences, branches = {}, {}
    for ayah in [packet["focus_ayah"], *packet["context_ayat"]]:
        for occurrence in ayah["root_occurrences"]:
            key = occurrence["occurrence_id"]
            require(key not in occurrences, "duplicate occurrence identifier")
            occurrences[key] = {"source_ref": ayah["ref"], "root": occurrence["root"],
                                "source_word_indices": occurrence["word_indices"]}
    for collection in ("focus_branch_inventories", "context_root_cues"):
        for inv in packet[collection]:
            for target in inv["targets"]:
                for branch in target["branches"]:
                    expected_key = f"{target['mapped_root_id']}/{branch['branch_id']}"
                    key = (inv["root"], expected_key)
                    require(key not in branches, "duplicate root/branch handle")
                    require(branch.get("branch_key", expected_key) == expected_key, "branch handle mismatch")
                    branches[key] = {"mapped_root_id": target["mapped_root_id"], "branch_id": branch["branch_id"], "evidence": branch}
    return occurrences, branches


def compile_response(draft: dict, packet: dict, reader_id: str) -> dict:
    require(draft.get("protocol") == READER_PROTOCOL, "wrong reader response protocol")
    require(draft.get("reader_id") == reader_id, "wrong reader assignment")
    require(draft.get("focus_ref") == packet["focus_ref"], "wrong focus assignment")
    result = copy.deepcopy(draft)
    result["protocol"] = validator.RESPONSE_PROTOCOL_V4
    occurrences, branches = evidence_index(packet)
    for section in SECTIONS:
        validator.require_list(result.get(section), section)
        for finding in result[section]:
            validator.require_object(finding, section)
            require("trigger_roots" not in finding and "trigger_refs" not in finding, "reader must not supply derived trigger lists")
            expanded = []
            for citation in validator.require_list(finding.get("activation_trace"), "activation_trace"):
                validator.require_object(citation, "citation")
                require(set(citation) == {"occurrence_id", "branch_key", "role"}, "citation must contain only occurrence_id, branch_key, role")
                for key in citation:
                    validator.require_string(citation[key], key)
                require(citation["occurrence_id"] in occurrences, "unknown or out-of-window occurrence")
                occurrence = occurrences[citation["occurrence_id"]]
                key = (occurrence["root"], citation["branch_key"])
                require(key in branches, "branch is not mapped to the selected occurrence's root")
                branch = branches[key]
                expanded.append({**copy.deepcopy(occurrence), "mapped_root_id": branch["mapped_root_id"],
                                 "branch_id": branch["branch_id"], "role": citation["role"]})
            finding["activation_trace"] = expanded
            if section == "context_deltas":
                finding["trigger_roots"] = base.ordered_unique(
                    row["root"] for row in expanded if row["source_ref"] != packet["focus_ref"]
                )
    validator.validate_response(validation_view(packet), result)
    return result


def render_prompt(model: str, effort: str, integration: bool, *, context_scopes: bool = False,
                  prompt_revision: str = "v1-discovery") -> str:
    require(model in MODELS and effort in ("medium", "high", "xhigh", "max"), "unsupported explicit model profile")
    require(prompt_revision in PROMPT_REVISIONS, "unsupported prompt revision")
    stem = "reader-scope-rich" if context_scopes else "reader"
    suffix = "-initial" if prompt_revision == "initial" else ""
    prompt = (ROOT / "prompts" / f"{stem}{suffix}.md").read_text()
    require(prompt.count("model: gpt-5.6-sol\nreasoning_effort: max") == 1, "profile template drift")
    prompt = prompt.replace("model: gpt-5.6-sol\nreasoning_effort: max", f"model: {model}\nreasoning_effort: {effort}")
    require(prompt.count("{{INTEGRATION}}") == 1, "integration template drift")
    return prompt.replace("{{INTEGRATION}}", (ROOT / "prompts/integration.md").read_text() if integration else "")


def prepare(job_dir: Path, focus: str, window: list[str], *, model: str = "gpt-5.6-sol", effort: str = "max",
            english: bool = False, integration: bool = False, context_scopes: bool = False,
            prompt_revision: str = "v1-discovery") -> dict:
    require(not job_dir.exists(), "job directory already exists; choose a new job")
    require(job_dir.resolve().is_relative_to(ROOT.resolve()) or job_dir.resolve().is_relative_to(Path('/private/tmp')), "prepare jobs under focus_trace_v3 or /private/tmp")
    source = build_source(focus, window)
    packet = project_packet(source, english=english, context_scopes=context_scopes)
    reader_id = f"reader_{focus.replace(':', '_')}_{model.removeprefix('gpt-5.6-')}"
    payloads = {
        "source.json": encode(source), "packet.json": encode(packet),
        "prompt.md": render_prompt(model, effort, integration, context_scopes=context_scopes,
                                   prompt_revision=prompt_revision).encode(),
        "reader.schema.json": (ROOT / "schemas/reader-response.schema.json").read_bytes(),
        "ledger.schema.json": (ROOT / "schemas/focus-trace-response.schema.json").read_bytes(),
    }
    job = {"protocol": "focus-trace-v3-job-v1", "focus_ref": focus, "reader_id": reader_id,
           "profile": {"model": model, "reasoning_effort": effort},
           "options": {"english": english, "integration": integration, "context_scopes": context_scopes,
                       "prompt_revision": prompt_revision},
           "inputs": {name: digest(data) for name, data in payloads.items()},
           "implementation_sha256": implementation_hashes(),
           "generation_state": "prepared"}
    job_dir.mkdir(parents=True)
    for name, data in payloads.items():
        (job_dir / name).write_bytes(data)
    (job_dir / "job.json").write_bytes(encode(job))
    return job


def implementation_hashes() -> dict:
    paths = [ROOT / "workflow.py", *sorted((ROOT / "prompts").glob("reader*.md")), ROOT / "prompts/integration.md",
             *sorted((ROOT / "scripts").glob("*.py"))]
    return {str(path.relative_to(ROOT)): digest(path.read_bytes()) for path in paths}


def load_job(job_dir: Path) -> tuple[dict, dict]:
    job = read(job_dir / "job.json")
    require(job["protocol"] == "focus-trace-v3-job-v1", "wrong job protocol")
    require(set(job["inputs"]) == {"source.json", "packet.json", "prompt.md", "reader.schema.json", "ledger.schema.json"}, "incomplete frozen inputs")
    for name, checksum in job["inputs"].items():
        require(digest((job_dir / name).read_bytes()) == checksum, f"frozen input changed: {name}")
    source, packet = read(job_dir / "source.json"), read(job_dir / "packet.json")
    context_scopes = job["options"].get("context_scopes", True)
    require(packet == project_packet(source, english=job["options"]["english"], context_scopes=context_scopes), "packet differs from full source projection")
    require(job["focus_ref"] == packet["focus_ref"], "job/packet focus mismatch")
    require((job_dir / "prompt.md").read_text() == render_prompt(
        job["profile"]["model"], job["profile"]["reasoning_effort"], job["options"]["integration"],
        context_scopes=context_scopes, prompt_revision=job["options"].get("prompt_revision", "initial")),
        "job/prompt configuration mismatch")
    require((job_dir / "reader.schema.json").read_bytes() == (ROOT / "schemas/reader-response.schema.json").read_bytes(), "unsupported frozen reader schema")
    require((job_dir / "ledger.schema.json").read_bytes() == (ROOT / "schemas/focus-trace-response.schema.json").read_bytes(), "unsupported frozen ledger schema")
    return job, packet


def evidence_export(response: dict, packet: dict) -> dict:
    _, branches = evidence_index(packet)
    ayat = {row["ref"]: row for row in [packet["focus_ayah"], *packet["context_ayat"]]}
    findings = []
    for section in SECTIONS:
        for finding in response[section]:
            resolved = []
            for citation in finding["activation_trace"]:
                key = (citation["root"], f"{citation['mapped_root_id']}/{citation['branch_id']}")
                resolved.append({"citation": citation, "source_ayah_ar": ayat[citation["source_ref"]]["text_ar"],
                                 "branch": branches[key]["evidence"]})
            findings.append({"section": section, "finding": finding, "resolved_evidence": resolved})
    return {"protocol": "focus-trace-v3-evidence-v1", "focus_ref": packet["focus_ref"], "findings": findings}


def compile_job(job_dir: Path) -> dict:
    job, packet = load_job(job_dir)
    draft_bytes = (job_dir / "reader.response.json").read_bytes()
    response = compile_response(read(job_dir / "reader.response.json"), packet, job["reader_id"])
    outputs = {"response.json": encode(response), "evidence.json": encode(evidence_export(response, packet))}
    receipt = {"protocol": "focus-trace-v3-compilation-v1", "reader_response_sha256": digest(draft_bytes),
               "job_sha256": digest((job_dir / "job.json").read_bytes()),
               "outputs": {name: digest(data) for name, data in outputs.items()},
               "implementation_sha256": implementation_hashes(),
               "validation": "passed", "model_execution_verified": False,
               "semantic_quality_verified": False}
    outputs["compilation.json"] = encode(receipt)
    # Never overwrite an accepted artifact with a different result or leave it silently stale.
    for name, data in outputs.items():
        existing = job_dir / name
        require(not existing.exists() or existing.read_bytes() == data, f"output already exists with different content: {name}")
    for name, data in outputs.items():
        (job_dir / name).write_bytes(data)
    return receipt


def validate_job(job_dir: Path) -> None:
    job, packet = load_job(job_dir)
    receipt = read(job_dir / "compilation.json")
    require(receipt["job_sha256"] == digest((job_dir / "job.json").read_bytes()), "compilation job changed")
    require(receipt["reader_response_sha256"] == digest((job_dir / "reader.response.json").read_bytes()), "reader response changed")
    expected = compile_response(read(job_dir / "reader.response.json"), packet, job["reader_id"])
    require(read(job_dir / "response.json") == expected, "compiled ledger changed")
    require(read(job_dir / "evidence.json") == evidence_export(expected, packet), "resolved evidence changed")
    require(set(receipt["outputs"]) == {"response.json", "evidence.json"}, "incomplete output receipt")
    for name, checksum in receipt["outputs"].items():
        require(digest((job_dir / name).read_bytes()) == checksum, f"compiled output changed: {name}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--job", type=Path, required=True)
    p.add_argument("--focus", type=base.parse_ref, required=True)
    scope = p.add_mutually_exclusive_group(required=True)
    scope.add_argument("--window", type=base.parse_refs)
    scope.add_argument("--surah-window", action="store_true")
    p.add_argument("--model", choices=MODELS, default=MODELS[0])
    p.add_argument("--effort", choices=("medium", "high", "xhigh", "max"), default="max")
    p.add_argument("--english", action="store_true", help="include paired English glosses as an explicit ablation")
    integration_group = p.add_mutually_exclusive_group()
    integration_group.add_argument("--integration", dest="integration", action="store_true",
                                   help="opt into the additional peripheral-branch integration instruction")
    integration_group.add_argument("--no-integration", dest="integration", action="store_false")
    p.set_defaults(integration=False)
    p.add_argument("--prompt-revision", choices=PROMPT_REVISIONS, default="v1-discovery",
                   help="use initial to reproduce the original v3 split-root wording")
    p.add_argument("--context-scopes", action="store_true", help="restore the larger context-scope input as an explicit ablation")
    for name in ("render", "compile", "validate"):
        command = sub.add_parser(name)
        command.add_argument("job", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            window = args.window or base.window_for_surah(base.DEFAULT_QURAN_DIR, args.focus, False)
            job = prepare(args.job, args.focus, window, model=args.model, effort=args.effort,
                          english=args.english, integration=args.integration, context_scopes=args.context_scopes,
                          prompt_revision=args.prompt_revision)
            print(json.dumps({"job": str(args.job), "reader_id": job["reader_id"], "state": "prepared"}))
        elif args.command == "compile":
            print(json.dumps(compile_job(args.job)))
        elif args.command == "validate":
            validate_job(args.job)
            print("valid v3 compilation; semantic quality and model execution are not certified")
        else:
            job, _ = load_job(args.job)
            print((args.job / "prompt.md").read_text())
            print(f"\nAssigned reader_id: {job['reader_id']}\nReturn only the reader response JSON.\n")
            print("<response_schema>\n" + (args.job / "reader.schema.json").read_text() + "</response_schema>")
            print("<sealed_packet>\n" + (args.job / "packet.json").read_text() + "</sealed_packet>")
    except (ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"error: {error}\n")


if __name__ == "__main__":
    main()
