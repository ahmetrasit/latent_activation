#!/usr/bin/env python3
"""Build one hash-bound v3 baseline-delta publication package."""

from __future__ import annotations

import argparse
import json
import re
from contextlib import closing
from pathlib import Path
from typing import Any

from build_publication_package import (
    BRANCH_DB_PATH,
    PackageError,
    branch_indexes,
    connect_branch_db,
    discover_citations,
    verify_coverage,
)
from validate_target_language_baseline import (
    BaselineValidationError,
    validate as validate_baseline,
)
from workflow_common import (
    REPO_ROOT,
    atomic_write_json,
    discover_runs,
    read_json,
    repo_relative,
    sha256_file,
)


PROMPT_PATH = REPO_ROOT / "_status" / "v12_cross_run" / "prompts" / "publish_whole_surah_v3.md"
DRAFT_SCHEMA_PATH = (
    REPO_ROOT / "_status" / "v12_cross_run" / "model_schemas" / "publication_draft_v3.json"
)
FINAL_SCHEMA_PATH = (
    REPO_ROOT / "_status" / "v12_cross_run" / "model_schemas" / "publication_final_v3.json"
)
AUDIT_SCHEMA_PATH = (
    REPO_ROOT / "_status" / "v12_cross_run" / "model_schemas" / "self_audit_v3.json"
)
BASELINE_SCHEMA_PATH = (
    REPO_ROOT
    / "_status"
    / "v12_cross_run"
    / "model_schemas"
    / "target_language_baseline_v1.json"
)
BASELINE_ROOT = REPO_ROOT / "_status" / "v12_cross_run" / "baseline"
BASELINE_METHODOLOGY_PATH = BASELINE_ROOT / "methodology" / "ordinary_baseline_v1.md"
QAC_PATH = REPO_ROOT / "resources" / "qac.sqlite"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("surah", type=int, choices=range(1, 115), metavar="SURAH")
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--workspace", type=Path)
    parser.add_argument("--variant")
    return parser.parse_args()


def canonical_baseline_ref(ayah_ref: str) -> str:
    _, ayah = ayah_ref.split(":", 1)
    return "1:1" if ayah == "0" else ayah_ref


def public_baseline(row: dict[str, Any], source_ref: str) -> dict[str, Any]:
    return {
        "source_ref": source_ref,
        "text": row["baseline_text"],
        "target_tokens": row["target_tokens"],
    }


def build(
    surah: int,
    baseline_path: Path,
    workspace: Path | None = None,
    variant: str | None = None,
) -> dict[str, Any]:
    tag = f"s{surah:03d}"
    workspace = (workspace or REPO_ROOT / "_status" / "v12_cross_run" / tag).resolve()
    workspace.mkdir(parents=True, exist_ok=True)
    baseline_path = baseline_path.resolve()
    try:
        repo_relative(baseline_path)
    except ValueError as error:
        raise PackageError("v3 baseline artifact must be stored inside this repository") from error
    if variant is not None and not re.fullmatch(r"[a-z0-9][a-z0-9.-]*", variant):
        raise PackageError("variant must contain only lowercase letters, digits, dots, and hyphens")
    suffix = f".{variant}" if variant else ""

    baseline_report = validate_baseline(baseline_path, QAC_PATH, surah=surah)
    baseline_doc = read_json(baseline_path)
    baseline_rows = {str(row["ayah_ref"]): row for row in baseline_doc["ayat"]}
    language = str(baseline_doc["language"])
    profile_path = BASELINE_ROOT / "language_profiles" / f"{language}.json"
    methodology_path = BASELINE_METHODOLOGY_PATH
    if not profile_path.is_file():
        raise PackageError(f"v3 has no project-owned language profile for {language}")
    profile_doc = read_json(profile_path)
    if profile_doc.get("language") != language:
        raise PackageError("v3 language profile and baseline language differ")

    runs, _ = discover_runs(surah, allow_single_run=False)
    if len(runs) != 2:
        raise PackageError(f"{tag}: expected two canonical reader runs, got {len(runs)}")
    packet_path = REPO_ROOT / runs[0]["packet_path"]
    if any(row["packet_path"] != runs[0]["packet_path"] for row in runs):
        raise PackageError(f"{tag}: selected readers do not share one packet")
    packet = read_json(packet_path)
    ayat = packet.get("ayat", [])
    expected_refs = [str(ayah["ref"]) for ayah in ayat]
    if len(expected_refs) != len(set(expected_refs)):
        raise PackageError(f"{tag}: packet contains duplicate ayah refs")
    if {int(ref.split(":", 1)[0]) for ref in expected_refs} != {surah}:
        raise PackageError(f"{tag}: packet contains refs from another surah")

    source_paths = [REPO_ROOT / row["output_path"] for row in runs]
    for source_path in source_paths:
        verify_coverage(source_path, expected_refs)

    roster_rows: list[list[Any]] = []
    for ayah in ayat:
        ayah_ref = str(ayah["ref"])
        baseline_ref = canonical_baseline_ref(ayah_ref)
        baseline_row = baseline_rows.get(baseline_ref)
        if baseline_row is None:
            raise PackageError(f"{tag}: baseline lacks required canonical ref {baseline_ref}")
        roster_rows.append(
            [
                ayah_ref,
                str(ayah["text_ar"]),
                baseline_ref,
                public_baseline(baseline_row, baseline_ref),
            ]
        )
    roster = {
        "protocol": "v12-cross-run-ayah-roster-v3",
        "surah": surah,
        "language": language,
        "baseline_sha256": sha256_file(baseline_path),
        "columns": ["ayah_ref", "text_ar", "baseline_source_ref", "baseline"],
        "rows": roster_rows,
    }
    roster_path = workspace / f"ayah_roster.v3{suffix}.json"
    atomic_write_json(roster_path, roster)

    with closing(connect_branch_db()) as connection:
        by_source, by_normalized, by_canonical = branch_indexes(connection)
        anchor_map, occurrences = discover_citations(
            source_paths, by_source, by_normalized, by_canonical, surah
        )
    anchor_path = workspace / f"anchor_map.v3{suffix}.json"
    occurrence_path = workspace / f"anchor_occurrences.v3{suffix}.json"
    atomic_write_json(anchor_path, anchor_map)
    atomic_write_json(occurrence_path, occurrences)

    input_paths = source_paths + [
        packet_path,
        baseline_path,
        profile_path,
        roster_path,
        anchor_path,
        occurrence_path,
        BRANCH_DB_PATH,
        PROMPT_PATH,
        DRAFT_SCHEMA_PATH,
        FINAL_SCHEMA_PATH,
        AUDIT_SCHEMA_PATH,
        BASELINE_SCHEMA_PATH,
        methodology_path,
        QAC_PATH,
    ]
    index = {
        "protocol": "v12-cross-run-publication-package-v3",
        "surah": surah,
        "variant": variant,
        "language": language,
        "baseline_sha256": baseline_report["baseline_sha256"],
        "state": (
            "ready_with_anchor_exceptions"
            if occurrences["summary"]["review_anchor_keys"]
            or occurrences["summary"]["malformed_or_unattached_occurrences"]
            else "ready"
        ),
        "publisher_inputs": {
            "standard_reader": runs[0]["output_path"],
            "wide_reader": runs[1]["output_path"],
            "ayah_roster": repo_relative(roster_path),
            "language_profile": repo_relative(profile_path),
            "anchor_map": repo_relative(anchor_path),
            "prompt": repo_relative(PROMPT_PATH),
            "output_schema": repo_relative(DRAFT_SCHEMA_PATH),
            "self_audit_schema": repo_relative(AUDIT_SCHEMA_PATH),
        },
        "coordinator_only": {
            "packet": repo_relative(packet_path),
            "baseline": repo_relative(baseline_path),
            "anchor_occurrences": repo_relative(occurrence_path),
            "branch_database": repo_relative(BRANCH_DB_PATH),
            "final_schema": repo_relative(FINAL_SCHEMA_PATH),
        },
        "hashes": {repo_relative(path): sha256_file(path) for path in input_paths},
        "coverage": {
            "ayah_count": len(expected_refs),
            "baseline_ayah_count": len(roster_rows),
            "standard_heading_count": len(expected_refs),
            "wide_heading_count": len(expected_refs),
        },
        "anchor_summary": occurrences["summary"],
        "draft_output": repo_relative(workspace / f"publication.v3{suffix}.draft.json"),
        "self_audit_output": repo_relative(workspace / f"self_audit.v3{suffix}.json"),
        "final_output": repo_relative(workspace / f"publication.v3{suffix}.json"),
        "final_manifest_output": repo_relative(
            workspace / f"publication_manifest.v3{suffix}.json"
        ),
        "word_branch_output": repo_relative(
            workspace / "derived" / f"finding_word_branches.v3{suffix}.tsv"
        ),
    }
    index_path = workspace / f"package_index.v3{suffix}.json"
    atomic_write_json(index_path, index)
    return index


def main() -> int:
    args = parse_args()
    try:
        index = build(args.surah, args.baseline, args.workspace, args.variant)
    except (OSError, ValueError, BaselineValidationError, PackageError) as error:
        print(json.dumps({"ready": False, "error": str(error)}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps(index, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
