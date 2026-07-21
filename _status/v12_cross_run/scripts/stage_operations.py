"""Deterministic payload and commit operations for an agent orchestrator.

This module does not select stages, invoke models, spawn agents, or retry work.
The root orchestrator owns those decisions through ORCHESTRATION.md.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

from workflow_common import (
    PROMPT_ROOT,
    MODEL_SCHEMA_ROOT,
    REPO_ROOT,
    PacketIndex,
    SourceBlock,
    atomic_write_json,
    atomic_write_text,
    ayah_sort_key,
    begin_stage,
    discover_runs,
    end_stage,
    ensure_workspace_tables,
    join_scalar,
    latest_stage_row,
    normalize_branch_key,
    read_source_blocks,
    read_tsv,
    remap_blocks_to_established_runs,
    render_stage_prompt,
    repo_relative,
    run_validator,
    split_scalar,
    same_run_artifacts,
    utc_now,
    word_id_for,
    write_source_blocks,
    write_tsv,
)


PROMPT_BY_STAGE = {
    "extract": PROMPT_ROOT / "01_extract_source_findings.md",
    "normalize": PROMPT_ROOT / "02_normalize_mechanisms.md",
    "grade": PROMPT_ROOT / "03_grade_lexical_resonance.md",
    "reconcile": PROMPT_ROOT / "04_reconcile_after_grading.md",
    "publish": PROMPT_ROOT / "05_assign_publication_roles.md",
    "audit": PROMPT_ROOT / "06_audit_coverage.md",
    "handoff": PROMPT_ROOT / "07_build_handoff_views.md",
}

RESULT_SCHEMA_BY_STAGE = {
    "extract": MODEL_SCHEMA_ROOT / "extract.json",
    "normalize": MODEL_SCHEMA_ROOT / "normalize.json",
    "grade": MODEL_SCHEMA_ROOT / "grade.json",
    "reconcile": MODEL_SCHEMA_ROOT / "reconcile.json",
    "publish": MODEL_SCHEMA_ROOT / "publish.json",
}

CLAIM_TERMINAL = {"accepted", "evidence_only", "deferred", "rejected", "conflict"}
PUBLIC_ROLES = {"primary", "secondary", "exploratory", "evidence_only", "none"}


class WorkflowError(RuntimeError):
    pass


def snapshot_tables(workspace: Path, filenames: Iterable[str]) -> dict[str, bytes]:
    return {
        filename: (workspace / filename).read_bytes()
        for filename in filenames
        if (workspace / filename).exists()
    }


def restore_tables(workspace: Path, snapshot: dict[str, bytes]) -> None:
    for filename, content in snapshot.items():
        atomic_write_text(workspace / filename, content.decode("utf-8"))


def require_object_keys(value: Any, expected: set[str], context: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise WorkflowError(f"{context} must be an object")
    actual = set(value)
    if actual != expected:
        raise WorkflowError(
            f"{context} keys differ: expected {sorted(expected)}, got {sorted(actual)}"
        )
    return value


def require_list(value: Any, context: str) -> list[Any]:
    if not isinstance(value, list):
        raise WorkflowError(f"{context} must be an array")
    return value


def table_rows(workspace: Path, filename: str) -> list[dict[str, str]]:
    return read_tsv(workspace / filename)


def scope_claim_ids(workspace: Path, scope: str) -> set[str]:
    return {
        row["claim_id"]
        for row in table_rows(workspace, "claims.tsv")
        if row["ayah_ref"] == scope
    }


def append_note(existing: str, note: str) -> str:
    existing = existing.strip()
    return f"{existing} {note}".strip() if existing else note


def initialize_workspace(
    *,
    surah: int,
    output_root: Path,
    allow_single_run: bool,
    refresh_provenance: bool,
) -> tuple[Path, list[SourceBlock]]:
    tag = f"s{surah:03d}"
    workspace = output_root / tag
    ensure_workspace_tables(workspace)
    automation_root = workspace / "automation"
    source_blocks_path = automation_root / "source_blocks.json"

    discovered_rows, discovered_blocks = discover_runs(surah, allow_single_run)
    existing_rows = table_rows(workspace, "runs.tsv")
    if existing_rows and existing_rows != discovered_rows and same_run_artifacts(
        existing_rows, discovered_rows
    ):
        discovered_blocks = remap_blocks_to_established_runs(
            discovered_blocks, discovered_rows, existing_rows
        )
        discovered_rows = existing_rows
    if existing_rows:
        if existing_rows != discovered_rows:
            if not refresh_provenance:
                raise WorkflowError(
                    f"{tag}: discovered run provenance differs from existing runs.tsv; "
                    "set refresh_provenance=True only after reviewing the source change"
                )
            if table_rows(workspace, "source_findings.tsv"):
                raise WorkflowError(
                    f"{tag}: cannot refresh provenance after extraction has written findings"
                )
            write_tsv(workspace / "runs.tsv", discovered_rows)
    else:
        write_tsv(workspace / "runs.tsv", discovered_rows)

    if source_blocks_path.exists():
        current = [block.__dict__ for block in read_source_blocks(source_blocks_path)]
        discovered = [block.__dict__ for block in discovered_blocks]
        if current != discovered:
            if table_rows(workspace, "source_findings.tsv"):
                raise WorkflowError(
                    f"{tag}: parsed source blocks changed after extraction; preserve the "
                    "existing workspace and initialize a new treatment"
                )
            write_source_blocks(source_blocks_path, discovered_blocks)
    else:
        write_source_blocks(source_blocks_path, discovered_blocks)

    provenance = latest_stage_row(workspace, tag, "provenance")
    if provenance is None or provenance["status"] != "complete":
        artifact_paths: list[Path] = []
        for row in discovered_rows:
            for field in (
                "prompt_path",
                "packet_path",
                "output_path",
                "frozen_manifest_path",
            ):
                if row[field]:
                    path = REPO_ROOT / row[field]
                    if path not in artifact_paths:
                        artifact_paths.append(path)
        stage_row = begin_stage(
            workspace,
            scope=tag,
            stage="provenance",
            prompt_path=None,
            input_paths=artifact_paths,
        )
        end_stage(
            workspace,
            stage_row["stage_id"],
            status="complete",
            output_paths=[workspace / "runs.tsv", source_blocks_path],
            notes="Deterministic discovery, hashing, historical revision lookup, and source-block parsing.",
        )

    valid, output = run_validator(workspace)
    if not valid:
        raise WorkflowError(f"{tag}: initialized workspace failed validation\n{output}")
    return workspace, discovered_blocks


def stage_is_complete(workspace: Path, scope: str, stage: str) -> bool:
    row = latest_stage_row(workspace, scope, stage)
    return bool(row and row["status"] == "complete")


def stage_is_failed(workspace: Path, scope: str, stage: str) -> bool:
    row = latest_stage_row(workspace, scope, stage)
    return bool(row and row["status"] == "failed")


def render_task_only(
    *,
    workspace: Path,
    scope: str,
    stage: str,
    payload: dict[str, Any],
) -> Path:
    task_path = workspace / "automation" / "tasks" / scope.replace(":", "_") / f"{stage}-dry-run.md"
    prompt = render_stage_prompt(
        PROMPT_BY_STAGE[stage],
        stage=stage,
        scope=scope,
        runtime_payload=payload,
    )
    atomic_write_text(task_path, prompt)
    return task_path


def write_task_envelope(
    *,
    workspace: Path,
    scope: str,
    stage: str,
    payload: dict[str, Any],
    attempt: int | None = None,
) -> Path:
    """Write one deterministic worker task; never select or sequence stages."""
    if stage not in RESULT_SCHEMA_BY_STAGE:
        raise WorkflowError(f"no result schema for stage {stage!r}")
    task_dir = workspace / "automation" / "tasks" / stage
    scope_key = scope.replace(":", "_")
    prefix = f"{workspace.name}-{scope_key}-{stage}-"
    if attempt is None:
        existing_attempts = []
        for path in task_dir.glob(f"{prefix}*.json"):
            suffix = path.stem.removeprefix(prefix)
            if suffix.isdigit():
                existing_attempts.append(int(suffix))
        attempt = max(existing_attempts, default=0) + 1
    task_id = f"{prefix}{attempt:03d}"
    result_path = workspace / "automation" / "results" / stage / f"{task_id}.json"

    if stage == "normalize":
        expected_ids = [
            row["source_finding_id"] for row in payload.get("source_findings", [])
        ]
    elif stage in {"grade", "publish", "reconcile"}:
        expected_ids = [row["claim_id"] for row in payload.get("claims", [])]
    elif stage == "extract":
        expected_ids = [row["block_id"] for row in payload.get("blocks", [])]
    else:
        expected_ids = []

    envelope = {
        "task_id": task_id,
        "stage": stage,
        "scope_ref": scope,
        "workspace": repo_relative(workspace),
        "prompt_path": repo_relative(PROMPT_BY_STAGE[stage]),
        "result_schema_path": repo_relative(RESULT_SCHEMA_BY_STAGE[stage]),
        "result_path": repo_relative(result_path),
        "input_paths": [],
        "expected_ids": expected_ids,
        "payload": payload,
    }
    task_path = task_dir / f"{task_id}.json"
    atomic_write_json(task_path, envelope)
    return task_path


def extraction_payload(blocks: list[SourceBlock], scope: str) -> dict[str, Any]:
    return {
        "scope": scope,
        "blocks": [block.__dict__ for block in blocks if block.fixed_ayah_ref == scope],
        "normalization_rules": {
            "claimed_branch_format": "ROOT:B###",
            "source_order_required": True,
            "block_coverage_required": True,
        },
    }


def apply_extraction(
    *, workspace: Path, scope: str, blocks: list[SourceBlock], result: dict[str, Any]
) -> None:
    result = require_object_keys(result, {"findings", "empty_blocks"}, "extract result")
    findings = require_list(result["findings"], "findings")
    empty_blocks = require_list(result["empty_blocks"], "empty_blocks")
    scoped_blocks = {block.block_id: block for block in blocks if block.fixed_ayah_ref == scope}
    if not scoped_blocks:
        raise WorkflowError(f"no source blocks for {scope}")

    findings_by_block: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for raw in findings:
        item = require_object_keys(
            raw,
            {
                "block_id",
                "component_index",
                "finding_title",
                "claimed_branches",
                "support_refs",
                "reader_strength",
                "notes",
            },
            "finding",
        )
        block_id = str(item["block_id"])
        if block_id not in scoped_blocks:
            raise WorkflowError(f"extract returned unknown block_id {block_id}")
        findings_by_block[block_id].append(item)

    empty_reasons: dict[str, str] = {}
    for raw in empty_blocks:
        item = require_object_keys(raw, {"block_id", "reason"}, "empty block")
        block_id = str(item["block_id"])
        if block_id not in scoped_blocks:
            raise WorkflowError(f"extract returned unknown empty block_id {block_id}")
        if block_id in empty_reasons:
            raise WorkflowError(f"duplicate empty block_id {block_id}")
        empty_reasons[block_id] = str(item["reason"]).strip()

    overlap = set(findings_by_block) & set(empty_reasons)
    if overlap:
        raise WorkflowError(f"blocks are both findings and empty: {sorted(overlap)}")
    missing = set(scoped_blocks) - set(findings_by_block) - set(empty_reasons)
    if missing:
        raise WorkflowError(f"source blocks disappeared from extraction: {sorted(missing)}")
    for block_id in empty_reasons:
        if scoped_blocks[block_id].finding_type == "activated_reading":
            raise WorkflowError(f"activated block cannot be empty: {block_id}")

    new_rows: list[dict[str, str]] = []
    extraction_coverage: dict[str, Any] = {"scope": scope, "blocks": []}
    for block_id, block in scoped_blocks.items():
        components = findings_by_block.get(block_id, [])
        indexes = sorted(int(item["component_index"]) for item in components)
        if indexes and indexes != list(range(1, len(indexes) + 1)):
            raise WorkflowError(f"{block_id}: component indexes must be consecutive from 1")
        source_ids: list[str] = []
        for item in sorted(components, key=lambda value: int(value["component_index"])):
            component = int(item["component_index"])
            source_id = f"sf-{block_id.removeprefix('blk-')}-c{component:02d}"
            source_ids.append(source_id)
            branches = [normalize_branch_key(str(value)) for value in item["claimed_branches"]]
            support_refs = [str(value) for value in item["support_refs"]]
            for ref in support_refs:
                if not re.fullmatch(r"[1-9][0-9]*:[0-9]+", ref):
                    raise WorkflowError(f"{source_id}: invalid support ref {ref!r}")
            strength = str(item["reader_strength"])
            if strength not in {"asserted", "qualified", "exploratory"}:
                raise WorkflowError(f"{source_id}: invalid reader_strength {strength}")
            new_rows.append(
                {
                    "source_finding_id": source_id,
                    "run_id": block.run_id,
                    "fixed_ayah_ref": block.fixed_ayah_ref,
                    "finding_type": block.finding_type,
                    "source_pointer": block.source_pointer,
                    "finding_title": str(item["finding_title"]).strip(),
                    "claimed_branches": join_scalar(branches),
                    "support_refs": join_scalar(support_refs),
                    "reader_strength": strength,
                    "disposition": "unreviewed",
                    "notes": str(item["notes"]).strip(),
                }
            )
        extraction_coverage["blocks"].append(
            {
                "block_id": block_id,
                "raw_sha256": block.raw_sha256,
                "source_finding_ids": source_ids,
                "empty_reason": empty_reasons.get(block_id, ""),
            }
        )

    rows = table_rows(workspace, "source_findings.tsv")
    rows = [row for row in rows if row["fixed_ayah_ref"] != scope]
    rows.extend(new_rows)
    rows.sort(key=lambda row: (ayah_sort_key(row["fixed_ayah_ref"]), row["run_id"], row["source_finding_id"]))
    write_tsv(workspace / "source_findings.tsv", rows)
    coverage_path = workspace / "automation" / "extraction" / f"{scope.replace(':', '_')}.json"
    atomic_write_json(coverage_path, extraction_coverage)


def normalization_payload(workspace: Path, scope: str, blocks: list[SourceBlock]) -> dict[str, Any]:
    source_rows = [
        row
        for row in table_rows(workspace, "source_findings.tsv")
        if row["fixed_ayah_ref"] == scope
    ]
    block_map = {block.source_pointer: block.text for block in blocks}
    return {
        "scope": scope,
        "runs": table_rows(workspace, "runs.tsv"),
        "source_findings": [
            {**row, "source_text": block_map.get(row["source_pointer"], "")}
            for row in source_rows
        ],
        "requirements": {
            "every_source_finding_linked": True,
            "one_mechanism_per_claim": True,
            "silence_is_neutral": True,
            "agreement_adds_no_lexical_confidence": True,
        },
    }


def apply_normalization(workspace: Path, scope: str, result: dict[str, Any]) -> None:
    result = require_object_keys(result, {"claims"}, "normalize result")
    raw_claims = require_list(result["claims"], "claims")
    if not raw_claims:
        raise WorkflowError("normalization returned no claims")
    source_rows = [
        row
        for row in table_rows(workspace, "source_findings.tsv")
        if row["fixed_ayah_ref"] == scope
    ]
    source_ids = {row["source_finding_id"] for row in source_rows}
    if not source_ids:
        raise WorkflowError(f"no extracted findings for {scope}")

    new_claims: list[dict[str, str]] = []
    new_links: list[dict[str, str]] = []
    seen_keys: set[str] = set()
    linked_sources: Counter[str] = Counter()
    for raw in raw_claims:
        claim = require_object_keys(
            raw,
            {"claim_key", "mechanism", "cross_run_relation", "source_links"},
            "claim",
        )
        key = str(claim["claim_key"])
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", key):
            raise WorkflowError(f"invalid claim_key {key!r}")
        if key in seen_keys:
            raise WorkflowError(f"duplicate claim_key {key}")
        seen_keys.add(key)
        claim_id = f"s{int(scope.split(':')[0]):03d}-{scope.replace(':', '_')}-{key}"
        relation = str(claim["cross_run_relation"])
        if relation not in {
            "shared_mechanism",
            "standard_only",
            "eleven_ayah_only",
            "compatible_refinement",
            "material_conflict",
        }:
            raise WorkflowError(f"{claim_id}: invalid cross_run_relation {relation}")
        links = require_list(claim["source_links"], f"{claim_id} source_links")
        if not links:
            raise WorkflowError(f"{claim_id}: no source links")
        seen_link_sources: set[str] = set()
        for raw_link in links:
            link = require_object_keys(
                raw_link,
                {"source_finding_id", "source_relation", "notes"},
                "source link",
            )
            source_id = str(link["source_finding_id"])
            if source_id not in source_ids:
                raise WorkflowError(f"{claim_id}: unknown source_finding_id {source_id}")
            if source_id in seen_link_sources:
                raise WorkflowError(f"{claim_id}: duplicate source link {source_id}")
            seen_link_sources.add(source_id)
            linked_sources[source_id] += 1
            new_links.append(
                {
                    "claim_id": claim_id,
                    "source_finding_id": source_id,
                    "source_relation": str(link["source_relation"]),
                    "notes": str(link["notes"]).strip(),
                }
            )
        new_claims.append(
            {
                "claim_id": claim_id,
                "ayah_ref": scope,
                "mechanism": str(claim["mechanism"]).strip(),
                "cross_run_relation": relation,
                "publication_role": "unreviewed",
                "disposition": "unreviewed",
                "decision_reason": "",
            }
        )
    if set(linked_sources) != source_ids:
        raise WorkflowError(
            f"normalization failed source coverage: missing {sorted(source_ids - set(linked_sources))}"
        )

    existing_claims = table_rows(workspace, "claims.tsv")
    old_claim_ids = {
        row["claim_id"] for row in existing_claims if row["ayah_ref"] == scope
    }
    existing_claims = [row for row in existing_claims if row["ayah_ref"] != scope]
    existing_claims.extend(new_claims)
    existing_claims.sort(key=lambda row: (ayah_sort_key(row["ayah_ref"]), row["claim_id"]))
    write_tsv(workspace / "claims.tsv", existing_claims)

    links = [
        row
        for row in table_rows(workspace, "claim_sources.tsv")
        if row["claim_id"] not in old_claim_ids
    ]
    links.extend(new_links)
    links.sort(key=lambda row: (row["claim_id"], row["source_finding_id"], row["source_relation"]))
    write_tsv(workspace / "claim_sources.tsv", links)

    if old_claim_ids:
        retained_evidence = [
            row
            for row in table_rows(workspace, "branch_evidence.tsv")
            if row["claim_id"] not in old_claim_ids
        ]
        write_tsv(workspace / "branch_evidence.tsv", retained_evidence)
        retained_coverage = [
            row
            for row in table_rows(workspace, "coverage.tsv")
            if row["source_finding_id"] not in source_ids
        ]
        write_tsv(workspace / "coverage.tsv", retained_coverage)

    sources_per_claim = Counter(row["claim_id"] for row in new_links)
    all_sources = table_rows(workspace, "source_findings.tsv")
    for source in all_sources:
        source_id = source["source_finding_id"]
        if source_id not in source_ids:
            continue
        source_claims = [row["claim_id"] for row in new_links if row["source_finding_id"] == source_id]
        if len(source_claims) > 1:
            disposition = "split"
        elif sources_per_claim[source_claims[0]] > 1:
            disposition = "merged"
        else:
            disposition = "accepted"
        source["disposition"] = disposition
        source["notes"] = append_note(
            source["notes"], f"Agent-orchestrated normalization: {disposition}."
        )
    write_tsv(workspace / "source_findings.tsv", all_sources)


def source_text_by_pointer(workspace: Path) -> dict[str, str]:
    path = workspace / "automation" / "source_blocks.json"
    if not path.exists():
        return {}
    return {block.source_pointer: block.text for block in read_source_blocks(path)}


def linguistic_context(
    workspace: Path,
    target_ref: str,
    refs: set[str],
    cited_roots: set[str],
) -> dict[str, Any]:
    root = workspace / "linguistic"
    required = (
        "words.tsv",
        "morphemes.tsv",
        "attachment_units.tsv",
        "syntax_edges.tsv",
        "root_cooccurrences.tsv",
    )
    missing = [name for name in required if not (root / name).exists()]
    if missing:
        raise WorkflowError(
            f"linguistic binding layer is incomplete; missing {', '.join(missing)}"
        )
    all_words = [
        row for row in read_tsv(root / "words.tsv") if row["ayah_ref"] in refs
    ]
    words_by_id = {row["word_id"]: row for row in all_words}
    selected_word_ids = {
        row["word_id"]
        for row in all_words
        if row["ayah_ref"] == target_ref
        or any(
            " ".join(value.split()) in cited_roots
            for value in row["root"].split(";")
            if value
        )
    }
    all_syntax = [
        row
        for row in read_tsv(root / "syntax_edges.tsv")
        if row["ayah_ref"] in refs
    ]
    syntax = [
        row
        for row in all_syntax
        if row["ayah_ref"] == target_ref
        or row["source_word_id"] in selected_word_ids
        or row["target_word_id"] in selected_word_ids
        or row["prep_word_id"] in selected_word_ids
    ]
    for row in syntax:
        selected_word_ids.update(
            value
            for value in (
                row["source_word_id"],
                row["target_word_id"],
                row["prep_word_id"],
            )
            if value
        )
    words = [row for row in all_words if row["word_id"] in selected_word_ids]
    all_cooccurrences = [
        row
        for row in read_tsv(root / "root_cooccurrences.tsv")
        if row["ayah_ref"] in refs
    ]
    return {
        "words": words,
        "morphemes": [
            row
            for row in read_tsv(root / "morphemes.tsv")
            if row["word_id"] in selected_word_ids
        ],
        "syntax_edges": syntax,
        "root_cooccurrences": [
            row
            for row in all_cooccurrences
            if row["ayah_ref"] == target_ref
        ],
        "cooccurrence_caveat": (
            "These are mechanical intra-ayah root co-occurrences with corpus counts, "
            "not semantic collocation judgments."
        ),
    }


def evidence_binding(
    workspace: Path, occurrence_ref: str, word_index: int, root: str
) -> tuple[str, str]:
    linguistic_root = workspace / "linguistic"
    word_id = word_id_for(occurrence_ref, word_index)
    words = {
        row["word_id"]: row for row in read_tsv(linguistic_root / "words.tsv")
    }
    if word_id not in words:
        raise WorkflowError(f"linguistic layer has no word binding {word_id}")
    normalized_root = " ".join(root.split())
    candidates = [
        row
        for row in read_tsv(linguistic_root / "morphemes.tsv")
        if row["word_id"] == word_id and " ".join(row["root"].split()) == normalized_root
    ]
    if len(candidates) != 1:
        raise WorkflowError(
            f"{word_id}: expected one QAC morpheme for root {root}, got {len(candidates)}"
        )
    return word_id, candidates[0]["morpheme_id"]


def valid_linguistic_support_ids(workspace: Path) -> set[str]:
    root = workspace / "linguistic"
    return {
        row["syntax_edge_id"] for row in read_tsv(root / "syntax_edges.tsv")
    } | {
        row["cooccurrence_id"]
        for row in read_tsv(root / "root_cooccurrences.tsv")
    }


def grading_payload(workspace: Path, scope: str, packet: PacketIndex) -> dict[str, Any]:
    claims = [row for row in table_rows(workspace, "claims.tsv") if row["ayah_ref"] == scope]
    claim_ids = {row["claim_id"] for row in claims}
    links = [
        row for row in table_rows(workspace, "claim_sources.tsv") if row["claim_id"] in claim_ids
    ]
    source_ids = {row["source_finding_id"] for row in links}
    sources = [
        row
        for row in table_rows(workspace, "source_findings.tsv")
        if row["source_finding_id"] in source_ids
    ]
    source_text = source_text_by_pointer(workspace)
    enriched_sources = [
        {**row, "source_text": source_text.get(row["source_pointer"], "")}
        for row in sources
    ]
    packet_context = packet.compact_context(scope, sources)
    context_refs = {ayah["ref"] for ayah in packet_context["ayat"]}
    cited_roots = {
        normalize_branch_key(key).rsplit(":", 1)[0]
        for source in sources
        for key in split_scalar(source["claimed_branches"])
    }
    return {
        "scope": scope,
        "claims": claims,
        "claim_sources": links,
        "source_findings": enriched_sources,
        "packet_context": packet_context,
        "linguistic_context": linguistic_context(
            workspace, scope, context_refs, cited_roots
        ),
        "requirements": {
            "retain_every_cited_branch": True,
            "add_direct_lexical_floor": True,
            "inventory_membership_does_not_prove_form_fit": True,
            "unlicensed_is_retained": True,
            "cross_run_agreement_score": 0,
            "linguistic_binding_is_mechanical": True,
            "cite_only_material_linguistic_support": True,
            "translation_visible_only_in_fixed_ayah": True,
            "direct_and_contextual_require_compatible_form_and_construction": True,
        },
    }


def expected_strength(total: int) -> str:
    if total >= 8:
        return "strong"
    if total >= 5:
        return "moderate"
    return "weak"


def apply_grading(
    workspace: Path, scope: str, packet: PacketIndex, result: dict[str, Any]
) -> None:
    result = require_object_keys(result, {"evidence"}, "grade result")
    raw_evidence = require_list(result["evidence"], "evidence")
    claims = [row for row in table_rows(workspace, "claims.tsv") if row["ayah_ref"] == scope]
    claim_ids = {row["claim_id"] for row in claims}
    if not claim_ids:
        raise WorkflowError(f"no normalized claims for {scope}")
    by_claim: Counter[str] = Counter()
    seen_evidence: set[tuple[str, str, int, str, str]] = set()
    new_rows: list[dict[str, str]] = []
    sequence_by_claim: Counter[str] = Counter()
    allowed_linguistic_support_ids = valid_linguistic_support_ids(workspace)

    required_keys = {
        "claim_id",
        "occurrence_ref",
        "word_index",
        "root",
        "branch",
        "evidence_role",
        "form_fit",
        "construction_fit",
        "lexical_status",
        "translation_role",
        "resonance_eligible",
        "trigger_score",
        "proximity_score",
        "structure_score",
        "reading_gain_score",
        "robustness_score",
        "support_refs",
        "linguistic_support_ids",
        "counterevidence",
        "decision_reason",
    }
    score_fields = (
        "trigger_score",
        "proximity_score",
        "structure_score",
        "reading_gain_score",
        "robustness_score",
    )
    for raw in raw_evidence:
        item = require_object_keys(raw, required_keys, "evidence item")
        claim_id = str(item["claim_id"])
        if claim_id not in claim_ids:
            raise WorkflowError(f"evidence references unknown claim {claim_id}")
        occurrence_ref = str(item["occurrence_ref"])
        word_index = int(item["word_index"])
        root = " ".join(str(item["root"]).split())
        branch = str(item["branch"])
        occurrence = packet.occurrence(occurrence_ref, word_index, root)
        if occurrence is None:
            raise WorkflowError(
                f"{claim_id}: packet has no {occurrence_ref} word {word_index} root {root}"
            )
        duplicate_key = (claim_id, occurrence_ref, word_index, root, branch)
        if duplicate_key in seen_evidence:
            raise WorkflowError(f"duplicate claim-specific evidence {duplicate_key}")
        seen_evidence.add(duplicate_key)
        inventory_pointer = packet.inventory_pointer(root, branch)
        inventory_match = "yes" if inventory_pointer else "no"
        lexical_status = str(item["lexical_status"])
        if inventory_match == "no" and lexical_status != "unlicensed":
            raise WorkflowError(
                f"{claim_id} {root}:{branch}: missing inventory branch must be unlicensed"
            )

        score_values = [item[field] for field in score_fields]
        if lexical_status == "analogical_resonance":
            if any(value is None for value in score_values):
                raise WorkflowError(f"{claim_id} {root}:{branch}: resonance scores are incomplete")
            scores = [int(value) for value in score_values]
            if any(value < 0 or value > 2 for value in scores):
                raise WorkflowError(f"{claim_id} {root}:{branch}: scores must be 0-2")
            total = sum(scores)
            strength = expected_strength(total)
            rendered_scores = [str(value) for value in scores]
            rendered_total = str(total)
        else:
            if any(value is not None for value in score_values):
                raise WorkflowError(
                    f"{claim_id} {root}:{branch}: non-resonance scores must be null"
                )
            rendered_scores = ["", "", "", "", ""]
            rendered_total = ""
            strength = "none"

        word_id, morpheme_id = evidence_binding(
            workspace, occurrence_ref, word_index, root
        )
        support_ids = [str(value) for value in item["linguistic_support_ids"]]
        unknown_support = set(support_ids) - allowed_linguistic_support_ids
        if unknown_support:
            raise WorkflowError(
                f"{claim_id} {root}:{branch}: unknown linguistic support IDs "
                f"{sorted(unknown_support)}"
            )

        sequence_by_claim[claim_id] += 1
        evidence_id = f"e-{claim_id}-{sequence_by_claim[claim_id]:03d}"
        new_rows.append(
            {
                "evidence_id": evidence_id,
                "claim_id": claim_id,
                "occurrence_ref": occurrence_ref,
                "word_index": str(word_index),
                "word_id": word_id,
                "morpheme_id": morpheme_id,
                "surface": occurrence["surface"],
                "lemma": occurrence["lemma"],
                "pos": occurrence["pos"],
                "root": root,
                "branch": branch,
                "inventory_pointer": inventory_pointer,
                "inventory_match": inventory_match,
                "form_fit": str(item["form_fit"]),
                "construction_fit": str(item["construction_fit"]),
                "evidence_role": str(item["evidence_role"]),
                "lexical_status": lexical_status,
                "translation_role": str(item["translation_role"]),
                "resonance_eligible": str(item["resonance_eligible"]),
                "trigger_score": rendered_scores[0],
                "proximity_score": rendered_scores[1],
                "structure_score": rendered_scores[2],
                "reading_gain_score": rendered_scores[3],
                "robustness_score": rendered_scores[4],
                "resonance_score": rendered_total,
                "resonance_strength": strength,
                "support_refs": join_scalar(str(value) for value in item["support_refs"]),
                "linguistic_support_ids": join_scalar(support_ids),
                "counterevidence": str(item["counterevidence"]).strip(),
                "decision_reason": str(item["decision_reason"]).strip(),
            }
        )
        by_claim[claim_id] += 1
    missing_claims = claim_ids - set(by_claim)
    if missing_claims:
        raise WorkflowError(f"claims without evidence: {sorted(missing_claims)}")

    links = [
        row for row in table_rows(workspace, "claim_sources.tsv") if row["claim_id"] in claim_ids
    ]
    claims_by_source: dict[str, set[str]] = defaultdict(set)
    for link in links:
        claims_by_source[link["source_finding_id"]].add(link["claim_id"])
    evidence_branches_by_claim: dict[str, set[str]] = defaultdict(set)
    for row in new_rows:
        evidence_branches_by_claim[row["claim_id"]].add(f"{row['root']}:{row['branch']}")
    sources = {
        row["source_finding_id"]: row
        for row in table_rows(workspace, "source_findings.tsv")
        if row["fixed_ayah_ref"] == scope
    }
    for source_id, source in sources.items():
        represented: set[str] = set()
        for claim_id in claims_by_source.get(source_id, set()):
            represented.update(evidence_branches_by_claim.get(claim_id, set()))
        cited = {normalize_branch_key(value) for value in split_scalar(source["claimed_branches"])}
        if cited - represented:
            raise WorkflowError(
                f"{source_id}: cited branches disappeared from grading: {sorted(cited - represented)}"
            )

    existing = table_rows(workspace, "branch_evidence.tsv")
    existing = [row for row in existing if row["claim_id"] not in claim_ids]
    existing.extend(new_rows)
    existing.sort(key=lambda row: (row["claim_id"], row["evidence_id"]))
    write_tsv(workspace / "branch_evidence.tsv", existing)


def reconciliation_payload(workspace: Path, scope: str) -> dict[str, Any]:
    claims = [row for row in table_rows(workspace, "claims.tsv") if row["ayah_ref"] == scope]
    claim_ids = {row["claim_id"] for row in claims}
    evidence = [
        row for row in table_rows(workspace, "branch_evidence.tsv") if row["claim_id"] in claim_ids
    ]
    return {
        "scope": scope,
        "claims": claims,
        "branch_evidence": evidence,
        "rule": "Keep, reject, defer, or mark conflict. Never delete. Use defer if a new split or merge would be required.",
    }


def apply_reconciliation(workspace: Path, scope: str, result: dict[str, Any]) -> None:
    result = require_object_keys(result, {"decisions"}, "reconcile result")
    decisions = require_list(result["decisions"], "decisions")
    claims = table_rows(workspace, "claims.tsv")
    scoped = {row["claim_id"]: row for row in claims if row["ayah_ref"] == scope}
    returned: set[str] = set()
    for raw in decisions:
        item = require_object_keys(raw, {"claim_id", "action", "reason"}, "decision")
        claim_id = str(item["claim_id"])
        if claim_id not in scoped:
            raise WorkflowError(f"reconcile returned unknown claim {claim_id}")
        if claim_id in returned:
            raise WorkflowError(f"duplicate reconcile decision for {claim_id}")
        returned.add(claim_id)
        action = str(item["action"])
        reason = str(item["reason"]).strip()
        if action == "keep":
            scoped[claim_id]["decision_reason"] = reason
        elif action in {"reject", "defer", "conflict"}:
            disposition = {"reject": "rejected", "defer": "deferred", "conflict": "conflict"}[action]
            scoped[claim_id]["publication_role"] = "none"
            scoped[claim_id]["disposition"] = disposition
            scoped[claim_id]["decision_reason"] = reason
        else:
            raise WorkflowError(f"{claim_id}: invalid reconcile action {action}")
    if returned != set(scoped):
        raise WorkflowError(f"reconcile omitted claims: {sorted(set(scoped) - returned)}")
    write_tsv(workspace / "claims.tsv", claims)


def publication_payload(workspace: Path, scope: str) -> dict[str, Any]:
    claims = [row for row in table_rows(workspace, "claims.tsv") if row["ayah_ref"] == scope]
    claim_ids = {row["claim_id"] for row in claims}
    evidence = [
        row for row in table_rows(workspace, "branch_evidence.tsv") if row["claim_id"] in claim_ids
    ]
    links = [
        row for row in table_rows(workspace, "claim_sources.tsv") if row["claim_id"] in claim_ids
    ]
    source_ids = {row["source_finding_id"] for row in links}
    sources = [
        {
            field: row[field]
            for field in (
                "source_finding_id",
                "run_id",
                "finding_type",
                "finding_title",
                "reader_strength",
                "claimed_branches",
                "support_refs",
                "notes",
            )
        }
        for row in table_rows(workspace, "source_findings.tsv")
        if row["source_finding_id"] in source_ids
    ]
    return {
        "scope": scope,
        "claims": claims,
        "claim_sources": links,
        "source_findings": sources,
        "branch_evidence": evidence,
        "requirements": {
            "multiple_primary_allowed": True,
            "multiple_secondary_allowed": True,
            "role_independent_of_lexical_status": True,
            "primary_requires_fixed_ayah_licensed_anchor": True,
            "analogical_and_unlicensed_translation_role": "none",
        },
    }


def _derive_source_dispositions_and_coverage(workspace: Path, scope: str) -> None:
    claims = {row["claim_id"]: row for row in table_rows(workspace, "claims.tsv")}
    scoped_claim_ids = {claim_id for claim_id, row in claims.items() if row["ayah_ref"] == scope}
    links = table_rows(workspace, "claim_sources.tsv")
    scoped_links = [row for row in links if row["claim_id"] in scoped_claim_ids]
    claims_by_source: dict[str, list[str]] = defaultdict(list)
    sources_by_claim: Counter[str] = Counter()
    for link in scoped_links:
        claims_by_source[link["source_finding_id"]].append(link["claim_id"])
        sources_by_claim[link["claim_id"]] += 1
        if claims[link["claim_id"]]["disposition"] == "rejected":
            link["source_relation"] = "rejected_basis"
    write_tsv(workspace / "claim_sources.tsv", links)

    source_rows = table_rows(workspace, "source_findings.tsv")
    scoped_sources: dict[str, dict[str, str]] = {}
    for source in source_rows:
        if source["fixed_ayah_ref"] != scope:
            continue
        source_id = source["source_finding_id"]
        scoped_sources[source_id] = source
        claim_ids = claims_by_source.get(source_id, [])
        dispositions = {claims[claim_id]["disposition"] for claim_id in claim_ids}
        if dispositions == {"rejected"}:
            disposition = "rejected"
        elif dispositions == {"deferred"}:
            disposition = "deferred"
        elif "conflict" in dispositions and not dispositions & {"accepted", "evidence_only"}:
            disposition = "conflict"
        elif len(claim_ids) > 1:
            disposition = "split"
        elif claim_ids and sources_by_claim[claim_ids[0]] > 1:
            disposition = "merged"
        elif dispositions == {"evidence_only"}:
            disposition = "evidence_only"
        else:
            disposition = "accepted"
        source["disposition"] = disposition
        source["notes"] = append_note(
            source["notes"], f"Agent-orchestrated terminal disposition: {disposition}."
        )
    write_tsv(workspace / "source_findings.tsv", source_rows)

    evidence_by_claim: dict[str, list[dict[str, str]]] = defaultdict(list)
    for evidence in table_rows(workspace, "branch_evidence.tsv"):
        if evidence["claim_id"] in scoped_claim_ids:
            evidence_by_claim[evidence["claim_id"]].append(evidence)

    existing_coverage = [
        row
        for row in table_rows(workspace, "coverage.tsv")
        if row["source_finding_id"] not in scoped_sources
    ]
    new_coverage: list[dict[str, str]] = []
    for source_id, source in scoped_sources.items():
        claim_ids = claims_by_source[source_id]
        cited = {normalize_branch_key(value) for value in split_scalar(source["claimed_branches"])}
        matching_translation = False
        for claim_id in claim_ids:
            for evidence in evidence_by_claim.get(claim_id, []):
                key = f"{evidence['root']}:{evidence['branch']}"
                if key in cited and evidence["translation_role"] in {"governing", "modifier"}:
                    matching_translation = True
        roles = [claims[claim_id]["publication_role"] for claim_id in claim_ids]
        if matching_translation:
            visibility = "commentary_and_translation"
        elif any(role in {"primary", "secondary", "exploratory"} for role in roles):
            visibility = "commentary_only"
        elif "evidence_only" in roles:
            visibility = "evidence_only"
        else:
            visibility = "none"
        new_coverage.append(
            {
                "source_finding_id": source_id,
                "claim_ids": join_scalar(claim_ids),
                "disposition": source["disposition"],
                "publication_roles": join_scalar(roles),
                "translation_visibility": visibility,
                "notes": "Deterministically generated from source, claim, and evidence lineage.",
            }
        )
    existing_coverage.extend(new_coverage)
    existing_coverage.sort(key=lambda row: row["source_finding_id"])
    write_tsv(workspace / "coverage.tsv", existing_coverage)


def apply_publication(workspace: Path, scope: str, result: dict[str, Any]) -> None:
    result = require_object_keys(result, {"decisions"}, "publish result")
    decisions = require_list(result["decisions"], "decisions")
    claims = table_rows(workspace, "claims.tsv")
    scoped = {row["claim_id"]: row for row in claims if row["ayah_ref"] == scope}
    returned: set[str] = set()
    for raw in decisions:
        item = require_object_keys(
            raw,
            {"claim_id", "publication_role", "disposition", "decision_reason"},
            "publication decision",
        )
        claim_id = str(item["claim_id"])
        if claim_id not in scoped:
            raise WorkflowError(f"publication returned unknown claim {claim_id}")
        if claim_id in returned:
            raise WorkflowError(f"duplicate publication decision for {claim_id}")
        returned.add(claim_id)
        role = str(item["publication_role"])
        disposition = str(item["disposition"])
        if role not in PUBLIC_ROLES or disposition not in CLAIM_TERMINAL:
            raise WorkflowError(f"{claim_id}: invalid role/disposition {role}/{disposition}")
        existing_disposition = scoped[claim_id]["disposition"]
        if existing_disposition in {"rejected", "deferred", "conflict"}:
            if disposition != existing_disposition or role != "none":
                raise WorkflowError(
                    f"{claim_id}: reconciliation outcome {existing_disposition} must be preserved"
                )
        if disposition == "accepted" and role not in {"primary", "secondary", "exploratory"}:
            raise WorkflowError(f"{claim_id}: accepted requires primary/secondary/exploratory")
        if disposition == "evidence_only" and role != "evidence_only":
            raise WorkflowError(f"{claim_id}: evidence_only disposition/role must match")
        if disposition in {"rejected", "deferred", "conflict"} and role != "none":
            raise WorkflowError(f"{claim_id}: terminal non-promotion requires role=none")
        scoped[claim_id]["publication_role"] = role
        scoped[claim_id]["disposition"] = disposition
        scoped[claim_id]["decision_reason"] = str(item["decision_reason"]).strip()
    if returned != set(scoped):
        raise WorkflowError(f"publication omitted claims: {sorted(set(scoped) - returned)}")

    evidence_by_claim: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in table_rows(workspace, "branch_evidence.tsv"):
        if row["claim_id"] in scoped:
            evidence_by_claim[row["claim_id"]].append(row)
    for claim_id, claim in scoped.items():
        if claim["publication_role"] != "primary":
            continue
        has_anchor = any(
            row["occurrence_ref"] == scope
            and row["evidence_role"] == "lexical_anchor"
            and row["lexical_status"] in {"direct", "contextually_activated"}
            for row in evidence_by_claim[claim_id]
        )
        if not has_anchor:
            raise WorkflowError(
                f"{claim_id}: primary publication requires a fixed-ayah direct/contextual anchor"
            )
    write_tsv(workspace / "claims.tsv", claims)
    _derive_source_dispositions_and_coverage(workspace, scope)


def apply_task_result(task_path: Path, *, strict_close: bool = False) -> str:
    """Commit one named worker result with rollback on deterministic failure."""
    task = json.loads(task_path.read_text(encoding="utf-8"))
    workspace = REPO_ROOT / task["workspace"]
    scope = str(task["scope_ref"])
    stage = str(task["stage"])
    result_path = REPO_ROOT / task["result_path"]
    if not result_path.is_file():
        raise WorkflowError(f"worker result does not exist: {result_path}")
    result = json.loads(result_path.read_text(encoding="utf-8"))
    affected = {
        "normalize": (
            "claims.tsv",
            "claim_sources.tsv",
            "source_findings.tsv",
            "branch_evidence.tsv",
            "coverage.tsv",
        ),
        "grade": ("branch_evidence.tsv",),
        "reconcile": ("claims.tsv",),
        "publish": (
            "claims.tsv",
            "claim_sources.tsv",
            "source_findings.tsv",
            "coverage.tsv",
        ),
    }.get(stage)
    if affected is None:
        raise WorkflowError(f"task-result commit is unsupported for stage {stage!r}")
    snapshot = snapshot_tables(workspace, affected)
    try:
        if stage == "normalize":
            apply_normalization(workspace, scope, result)
        elif stage == "grade":
            run_rows = table_rows(workspace, "runs.tsv")
            packet_paths = {row["packet_path"] for row in run_rows}
            if len(packet_paths) != 1:
                raise WorkflowError(
                    f"expected one packet path, got {sorted(packet_paths)}"
                )
            apply_grading(
                workspace,
                scope,
                PacketIndex(REPO_ROOT / next(iter(packet_paths))),
                result,
            )
        elif stage == "reconcile":
            apply_reconciliation(workspace, scope, result)
        elif stage == "publish":
            apply_publication(workspace, scope, result)
        valid, output = run_validator(
            workspace, strict=(strict_close and stage == "publish"), scope=scope
        )
        if not valid:
            raise WorkflowError(output)
    except Exception:
        restore_tables(workspace, snapshot)
        raise
    return output


def _generic_tsv(path: Path, header: list[str], rows: Iterable[dict[str, Any]]) -> None:
    lines = ["\t".join(header)]
    for row in rows:
        values: list[str] = []
        for field in header:
            value = str(row.get(field, ""))
            if any(character in value for character in "\t\r\n"):
                raise WorkflowError(f"derived {path.name} field {field} contains tab/newline")
            values.append(value)
        lines.append("\t".join(values))
    atomic_write_text(path, "\n".join(lines) + "\n")


def build_handoff_views(workspace: Path, scope: str) -> list[Path]:
    claims = {
        row["claim_id"]: row
        for row in table_rows(workspace, "claims.tsv")
        if row["ayah_ref"] == scope
    }
    claim_ids = set(claims)
    links = [
        row for row in table_rows(workspace, "claim_sources.tsv") if row["claim_id"] in claim_ids
    ]
    source_ids_by_claim: dict[str, list[str]] = defaultdict(list)
    for link in links:
        source_ids_by_claim[link["claim_id"]].append(link["source_finding_id"])
    evidence = [
        row for row in table_rows(workspace, "branch_evidence.tsv") if row["claim_id"] in claim_ids
    ]
    evidence_by_claim: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in evidence:
        evidence_by_claim[row["claim_id"]].append(row)

    output_dir = workspace / "derived" / scope.replace(":", "_")
    commentary_path = output_dir / "commentary_view.tsv"
    translation_path = output_dir / "translation_view.tsv"
    archive_path = output_dir / "evidence_archive.tsv"

    commentary_rows: list[dict[str, str]] = []
    for claim_id, claim in claims.items():
        if claim["disposition"] != "accepted" or claim["publication_role"] not in {
            "primary",
            "secondary",
            "exploratory",
        }:
            continue
        claim_evidence = evidence_by_claim[claim_id]
        commentary_rows.append(
            {
                "ayah_ref": scope,
                "claim_id": claim_id,
                "publication_role": claim["publication_role"],
                "mechanism": claim["mechanism"],
                "lexical_anchor_ids": join_scalar(
                    row["evidence_id"]
                    for row in claim_evidence
                    if row["evidence_role"] == "lexical_anchor"
                    and row["lexical_status"] in {"direct", "contextually_activated"}
                ),
                "resonance_evidence": join_scalar(
                    f"{row['evidence_id']}:{row['resonance_strength']}"
                    for row in claim_evidence
                    if row["lexical_status"] == "analogical_resonance"
                ),
                "source_finding_ids": join_scalar(source_ids_by_claim[claim_id]),
                "decision_reason": claim["decision_reason"],
            }
        )
    _generic_tsv(
        commentary_path,
        [
            "ayah_ref",
            "claim_id",
            "publication_role",
            "mechanism",
            "lexical_anchor_ids",
            "resonance_evidence",
            "source_finding_ids",
            "decision_reason",
        ],
        commentary_rows,
    )

    grouped_translation: dict[tuple[str, str, str, str, str, str, str, str], dict[str, Any]] = {}
    for row in evidence:
        if row["translation_role"] not in {"governing", "modifier"}:
            continue
        key = (
            row["occurrence_ref"],
            row["word_index"],
            row["surface"],
            row["lemma"],
            row["pos"],
            row["root"],
            row["branch"],
            row["lexical_status"],
        )
        group = grouped_translation.setdefault(
            key,
            {
                "ayah_ref": scope,
                "occurrence_ref": row["occurrence_ref"],
                "word_index": row["word_index"],
                "surface": row["surface"],
                "lemma": row["lemma"],
                "pos": row["pos"],
                "root": row["root"],
                "branch": row["branch"],
                "lexical_status": row["lexical_status"],
                "translation_roles": [],
                "evidence_ids": [],
                "claim_ids": [],
            },
        )
        group["translation_roles"].append(row["translation_role"])
        group["evidence_ids"].append(row["evidence_id"])
        group["claim_ids"].append(row["claim_id"])
    translation_rows: list[dict[str, str]] = []
    for group in grouped_translation.values():
        role = "governing" if "governing" in group["translation_roles"] else "modifier"
        translation_rows.append(
            {
                **{key: str(value) for key, value in group.items() if not isinstance(value, list)},
                "translation_role": role,
                "evidence_ids": join_scalar(group["evidence_ids"]),
                "claim_ids": join_scalar(group["claim_ids"]),
            }
        )
    translation_rows.sort(key=lambda row: (int(row["word_index"]), row["root"], row["branch"]))
    _generic_tsv(
        translation_path,
        [
            "ayah_ref",
            "occurrence_ref",
            "word_index",
            "surface",
            "lemma",
            "pos",
            "root",
            "branch",
            "lexical_status",
            "translation_role",
            "evidence_ids",
            "claim_ids",
        ],
        translation_rows,
    )

    archive_rows: list[dict[str, str]] = []
    for row in evidence:
        claim = claims[row["claim_id"]]
        archive_rows.append(
            {
                "claim_id": row["claim_id"],
                "ayah_ref": claim["ayah_ref"],
                "mechanism": claim["mechanism"],
                "cross_run_relation": claim["cross_run_relation"],
                "publication_role": claim["publication_role"],
                "claim_disposition": claim["disposition"],
                "claim_decision_reason": claim["decision_reason"],
                **{field: value for field, value in row.items()},
                "source_finding_ids": join_scalar(source_ids_by_claim[row["claim_id"]]),
            }
        )
    archive_header = [
        "claim_id",
        "ayah_ref",
        "mechanism",
        "cross_run_relation",
        "publication_role",
        "claim_disposition",
        "claim_decision_reason",
        *[field for field in table_rows_header("branch_evidence.tsv") if field != "claim_id"],
        "source_finding_ids",
    ]
    _generic_tsv(archive_path, archive_header, archive_rows)
    return [commentary_path, translation_path, archive_path]


def table_rows_header(filename: str) -> list[str]:
    from workflow_common import template_header

    return template_header(filename)


def write_audit_report(workspace: Path, scope: str, validator_output: str) -> Path:
    source_rows = [
        row for row in table_rows(workspace, "source_findings.tsv") if row["fixed_ayah_ref"] == scope
    ]
    claims = [row for row in table_rows(workspace, "claims.tsv") if row["ayah_ref"] == scope]
    claim_ids = {row["claim_id"] for row in claims}
    evidence = [
        row for row in table_rows(workspace, "branch_evidence.tsv") if row["claim_id"] in claim_ids
    ]
    lexical = Counter(row["lexical_status"] for row in evidence)
    resonance = Counter(row["resonance_strength"] for row in evidence)
    roles = Counter(row["publication_role"] for row in claims)
    dispositions = Counter(row["disposition"] for row in claims)
    report_path = workspace / "automation" / "audits" / f"{scope.replace(':', '_')}.md"
    lines = [
        f"# Automated Closed Audit — {scope}",
        "",
        f"Generated: {utc_now()}",
        "",
        "Result: PASS",
        "",
        f"- source findings: {len(source_rows)}",
        f"- claims: {len(claims)}",
        f"- evidence rows: {len(evidence)}",
        f"- lexical status: {json.dumps(dict(sorted(lexical.items())), ensure_ascii=False)}",
        f"- resonance strength: {json.dumps(dict(sorted(resonance.items())), ensure_ascii=False)}",
        f"- publication roles: {json.dumps(dict(sorted(roles.items())), ensure_ascii=False)}",
        f"- claim dispositions: {json.dumps(dict(sorted(dispositions.items())), ensure_ascii=False)}",
        f"- retained unlicensed evidence: {lexical.get('unlicensed', 0)}",
        f"- retained rejected claims: {dispositions.get('rejected', 0)}",
        "",
        "## Validator",
        "",
        "```text",
        validator_output.rstrip(),
        "```",
    ]
    atomic_write_text(report_path, "\n".join(lines) + "\n")
    return report_path


def run_deterministic_audit(workspace: Path, scope: str) -> None:
    inputs = [
        workspace / name
        for name in (
            "runs.tsv",
            "source_findings.tsv",
            "claims.tsv",
            "claim_sources.tsv",
            "branch_evidence.tsv",
            "coverage.tsv",
        )
    ]
    stage_row = begin_stage(
        workspace,
        scope=scope,
        stage="audit",
        prompt_path=PROMPT_BY_STAGE["audit"],
        input_paths=inputs,
    )
    valid, output = run_validator(workspace, strict=True, scope=scope)
    if not valid:
        end_stage(
            workspace,
            stage_row["stage_id"],
            status="failed",
            output_paths=[],
            error_summary=output,
            notes="Deterministic strict audit failed; no canonical repair was attempted.",
        )
        raise WorkflowError(output)
    report_path = write_audit_report(workspace, scope, output)
    end_stage(
        workspace,
        stage_row["stage_id"],
        status="complete",
        output_paths=[workspace / "coverage.tsv", report_path],
        notes="Deterministic coverage and strict audit passed with zero errors.",
    )


def run_deterministic_handoff(workspace: Path, scope: str) -> None:
    inputs = [
        workspace / name
        for name in ("claims.tsv", "claim_sources.tsv", "branch_evidence.tsv", "coverage.tsv")
    ]
    stage_row = begin_stage(
        workspace,
        scope=scope,
        stage="handoff",
        prompt_path=PROMPT_BY_STAGE["handoff"],
        input_paths=inputs,
    )
    try:
        outputs = build_handoff_views(workspace, scope)
    except Exception as exc:
        end_stage(
            workspace,
            stage_row["stage_id"],
            status="failed",
            output_paths=[],
            error_summary=str(exc),
        )
        raise
    end_stage(
        workspace,
        stage_row["stage_id"],
        status="complete",
        output_paths=outputs,
        notes="Commentary, translation, and full evidence archive views generated deterministically.",
    )


def selected_refs(
    surah: int, blocks: list[SourceBlock], start_ayah: int | None, end_ayah: int | None
) -> list[str]:
    refs = sorted({block.fixed_ayah_ref for block in blocks}, key=ayah_sort_key)
    result: list[str] = []
    for ref in refs:
        ref_surah, ref_ayah = ayah_sort_key(ref)
        if ref_surah != surah:
            continue
        if start_ayah is not None and ref_ayah < start_ayah:
            continue
        if end_ayah is not None and ref_ayah > end_ayah:
            continue
        result.append(ref)
    return result
