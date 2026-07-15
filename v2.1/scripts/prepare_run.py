#!/usr/bin/env python3
"""Build a canonical GSLS 2.1 run package from the local V1 resources."""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import sqlite3
import sys
from collections import defaultdict
from contextlib import closing
from pathlib import Path
from typing import Any, Iterable

from common import (
    DEFAULT_PROFILE,
    REPO_ROOT,
    WORKFLOW_ID,
    ContractError,
    assert_within,
    atomic_write_text,
    canonical_root,
    ensure_new_directory,
    load_json,
    require_regular_file,
    resolve_repo_path,
    split_aligned,
    strip_encoding_marker,
    write_json,
    write_jsonl,
    write_tsv,
)
from schema_validation import validate_instance


MORPHOLOGY_FIELDS = (
    "surah",
    "ayah",
    "word_index",
    "morpheme_index",
    "qac_ref",
    "surface_ar",
    "lemma_ar",
    "root_ar",
    "root_norm",
    "root_key",
    "pos",
    "morpheme_role",
    "morph_features",
    "aspect",
    "mood",
    "voice",
    "measure",
    "person",
    "number",
    "gender",
    "context_role",
    "source_ref",
    "data_quality",
)

SYNTAX_FIELDS = (
    "edge_id",
    "source_position",
    "target_position",
    "edge_type",
    "direction",
    "confidence",
    "annotation_source",
    "exact_surface_span",
    "evidence",
    "reason",
    "source_ref",
)

SOURCE_FAMILIES = {
    "maqayis": "Maqayis",
    "tahdhib": "Tahdhib",
    "sihah": "Sihah",
    "ayn": "Ayn",
    "mufradat": "Mufradat",
    "jamhara": "Jamhara",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--surah", type=int, required=True, choices=range(1, 115))
    parser.add_argument("--ayah-start", type=int, required=True)
    parser.add_argument("--ayah-end", type=int, required=True)
    parser.add_argument("--primary-scaffold", type=Path, required=True)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output-language", default="Turkish")
    parser.add_argument(
        "--basmala-policy",
        choices=("canonical-only", "include-opening-context"),
        default="canonical-only",
    )
    parser.add_argument(
        "--optional-product",
        choices=("none", "publication-essay"),
        default="none",
    )
    parser.add_argument("--include-review-branches", action="store_true")
    parser.add_argument(
        "--allow-source-limited",
        action="store_true",
        help="Permit composite lexical evidence or aggregate TSV fallbacks. The run will not be gold-release eligible.",
    )
    return parser.parse_args()


def extract_passage(
    quran_path: Path,
    surah: int,
    ayah_start: int,
    ayah_end: int,
    basmala_policy: str,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    document = load_json(quran_path)
    if int(document.get("index", 0)) != surah:
        raise ContractError(f"Quran file index does not match S{surah}: {quran_path}")
    verses = document.get("verse")
    if not isinstance(verses, dict):
        raise ContractError(f"Quran file has no verse mapping: {quran_path}")

    rows: list[dict[str, Any]] = []
    if basmala_policy == "include-opening-context" and surah not in (1, 9):
        opening = verses.get("verse_0")
        if not opening:
            raise ContractError(f"Opening context requested but verse_0 is absent: {quran_path}")
        rows.append(
            {
                "surah": surah,
                "ayah": 0,
                "context_role": "opening-context",
                "text": strip_encoding_marker(opening),
            }
        )

    for ayah in range(ayah_start, ayah_end + 1):
        key = f"verse_{ayah}"
        if key not in verses:
            raise ContractError(f"Missing S{surah}:{ayah} in {quran_path}")
        rows.append(
            {
                "surah": surah,
                "ayah": ayah,
                "context_role": "in-scope",
                "text": strip_encoding_marker(verses[key]),
            }
        )

    metadata = {
        "opening_context_included": any(row["ayah"] == 0 for row in rows),
    }
    return rows, metadata


def _available_columns(connection: sqlite3.Connection, table: str) -> set[str]:
    return {row[1] for row in connection.execute(f"PRAGMA table_info({table})")}


def connect_readonly(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(f"{path.resolve().as_uri()}?mode=ro", uri=True)
    connection.execute("PRAGMA query_only = ON")
    return connection


def load_qac_database(
    path: Path,
    surah: int,
    ayah_start: int,
    ayah_end: int,
) -> list[dict[str, Any]]:
    desired = (
        "surah",
        "ayah",
        "word_index",
        "morpheme_index",
        "qac_ref",
        "surface_ar",
        "lemma_ar",
        "root_ar",
        "pos",
        "morpheme_role",
        "morph_features",
        "aspect",
        "mood",
        "voice",
        "measure",
        "person",
        "number",
        "gender",
    )
    with closing(connect_readonly(path)) as connection:
        connection.row_factory = sqlite3.Row
        available = _available_columns(connection, "qac_morphemes")
        mandatory = {"surah", "ayah", "word_index", "morpheme_index", "qac_ref", "surface_ar"}
        if not mandatory.issubset(available):
            raise ContractError(f"qac_morphemes lacks required columns: {sorted(mandatory - available)}")
        select = [column if column in available else f"'' AS {column}" for column in desired]
        query = f"""
            SELECT {', '.join(select)}
            FROM qac_morphemes
            WHERE surah = ? AND ayah BETWEEN ? AND ?
            ORDER BY ayah, word_index, morpheme_index
        """
        source_rows = list(connection.execute(query, (surah, ayah_start, ayah_end)))

    rows: list[dict[str, Any]] = []
    for index, source in enumerate(source_rows, 1):
        root = source["root_ar"] or ""
        rows.append(
            {
                **{field: source[field] for field in desired},
                "root_norm": root,
                "root_key": canonical_root(root),
                "context_role": "in-scope",
                "source_ref": f"raw-qac-database:row:{index}",
                "data_quality": "full-morpheme-database",
            }
        )
    return rows


def load_qac_fallback(
    path: Path,
    surah: int,
    ayah_start: int,
    ayah_end: int,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for line_number, source in enumerate(reader, 2):
            if int(source["surah"]) != surah:
                continue
            ayah = int(source["ayah"])
            if not ayah_start <= ayah <= ayah_end:
                continue

            aligned = {
                "qac_ref": split_aligned(source["qac_refs"]),
                "word_index": split_aligned(source["word_indices"]),
                "surface_ar": split_aligned(source["surfaces_ar"]),
                "lemma_ar": split_aligned(source["lemmas_ar"]),
                "pos": split_aligned(source["pos_tags"]),
                "measure": split_aligned(source["measures"]),
            }
            expected = int(source["occurrence_count"])
            bad = {key: len(values) for key, values in aligned.items() if len(values) != expected}
            if bad:
                raise ContractError(f"Misaligned QAC fallback row {line_number}: {bad}, expected {expected}")

            for occurrence in range(expected):
                qac_ref = aligned["qac_ref"][occurrence]
                parts = qac_ref.split(":")
                morpheme_index = parts[-1] if len(parts) >= 4 else ""
                root = source["root_norm"]
                rows.append(
                    {
                        "surah": surah,
                        "ayah": ayah,
                        "word_index": aligned["word_index"][occurrence],
                        "morpheme_index": morpheme_index,
                        "qac_ref": qac_ref,
                        "surface_ar": aligned["surface_ar"][occurrence],
                        "lemma_ar": aligned["lemma_ar"][occurrence],
                        "root_ar": root,
                        "root_norm": root,
                        "root_key": canonical_root(root),
                        "pos": aligned["pos"][occurrence],
                        "morpheme_role": "",
                        "morph_features": "",
                        "aspect": "",
                        "mood": "",
                        "voice": "",
                        "measure": aligned["measure"][occurrence],
                        "person": "",
                        "number": "",
                        "gender": "",
                        "context_role": "in-scope",
                        "source_ref": f"raw-qac-fallback:line:{line_number}",
                        "data_quality": "rooted-aggregate-fallback",
                    }
                )
    rows.sort(key=lambda row: (int(row["ayah"]), int(row["word_index"]), int(row["morpheme_index"] or 0)))
    return rows


def filter_attachments(
    path: Path,
    surah: int,
    ayah_start: int,
    ayah_end: int,
) -> tuple[int, list[dict[str, str]]]:
    raw_count = 0
    syntax_rows: list[dict[str, str]] = []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for line_number, row in enumerate(reader, 2):
            if int(row["sura"]) != surah:
                continue
            ayah = int(row["ayah"])
            if not ayah_start <= ayah <= ayah_end:
                continue
            raw_count += 1
            head = row.get("head_unit_id") or f"q:{surah}:{ayah}:{row.get('head_wid', '')}"
            dependent = row.get("dep_unit_id") or f"q:{surah}:{ayah}:{row.get('dep_wid', '')}"
            surfaces = [value for value in (row.get("head_surface"), row.get("dep_surface")) if value]
            syntax_rows.append(
                {
                    "edge_id": row["unit_id"],
                    "source_position": head,
                    "target_position": dependent,
                    "edge_type": row["relation"],
                    "direction": "head-to-dependent",
                    "confidence": row["confidence"],
                    "annotation_source": f"attachments:{row['source_pass']}:{row['source_rtype']}",
                    "exact_surface_span": " | ".join(surfaces),
                    "evidence": row["evidence"],
                    "reason": row["reason"],
                    "source_ref": f"raw-attachments:line:{line_number}",
                }
            )
    return raw_count, syntax_rows


def source_families(source_phrase: str) -> list[str]:
    families: set[str] = set()
    for tag in re.findall(r"\(([^)]+)\)", source_phrase.lower()):
        for prefix, display in SOURCE_FAMILIES.items():
            if tag == prefix or tag.startswith(prefix + "-") or tag.startswith(prefix + "_"):
                families.add(display)
    return sorted(families)


def source_families_from_refs(source_refs: str) -> list[str]:
    families: set[str] = set()
    for source_ref in source_refs.split(";"):
        prefix = source_ref.strip().split(":", 1)[0].lower()
        display = SOURCE_FAMILIES.get(prefix)
        if display:
            families.add(display)
    return sorted(families)


def lexical_record(
    source: dict[str, str],
    line_number: int,
    passage_roots: dict[str, set[str]],
) -> dict[str, Any]:
    root_key = canonical_root(source["root_norm"])
    root_id = source["root_id"]
    families = source_families(source["source_phrase_ar"])
    return {
        "root_norm": source["root_norm"],
        "root_key": root_key,
        "passage_root_norms": sorted(passage_roots[root_key]),
        "branch_id": source["branch_id"],
        "source_id": f"furuq-v4-composite:{root_id}",
        "source_name": "furuq-v4 composite editorial inventory",
        "source_entry_id": f"{root_id}:{source['branch_id']}:line-{line_number}",
        "source_ar_exact": source["source_phrase_ar"],
        "branch_image_ar": source["branch_image_ar"],
        "what_is_ar": source["what_is_ar"],
        "lexical_unit_or_form": None,
        "derivation_or_pattern": None,
        "status": source["status"],
        "contaminated": False,
        "editorial_notes": "Composite V1 record; source-family agreement must not be inferred.",
        "provenance_granularity": "composite-tagged" if families else "composite-untagged",
        "source_families": families,
        "source_refs": [f"raw-lexical:line:{line_number}"],
    }


def load_lexical_fallback(
    path: Path,
    passage_root_rows: Iterable[dict[str, Any]],
    include_review: bool,
) -> list[dict[str, Any]]:
    passage_roots: dict[str, set[str]] = defaultdict(set)
    for row in passage_root_rows:
        if row["root_key"]:
            passage_roots[row["root_key"]].add(row["root_norm"])
    allowed_statuses = {"accepted", "review"} if include_review else {"accepted"}
    records: list[dict[str, Any]] = []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for line_number, source in enumerate(reader, 2):
            root_keys = {canonical_root(source["root_norm"]), canonical_root(source["source_root_norm"])}
            matched = sorted(root_keys.intersection(passage_roots))
            if not matched or source["status"] not in allowed_statuses:
                continue
            normalized = dict(source)
            normalized["root_norm"] = next(key for key in (source["root_norm"], source["source_root_norm"]) if canonical_root(key) in matched)
            records.append(lexical_record(normalized, line_number, passage_roots))
    records.sort(key=lambda row: (row["root_key"], row["source_entry_id"], row["source_id"]))
    return records


def load_lexical_database(
    path: Path,
    passage_root_rows: Iterable[dict[str, Any]],
    include_review: bool,
) -> tuple[list[dict[str, Any]], int]:
    passage_roots: dict[str, set[str]] = defaultdict(set)
    for row in passage_root_rows:
        root_norm = str(row.get("root_norm", ""))
        root_key = str(row.get("root_key", ""))
        if root_key:
            passage_roots[root_key].add(root_norm)
    if not passage_roots:
        raise ContractError("No passage roots are available for V4 branch selection")

    allowed_statuses = ("accepted", "review") if include_review else ("accepted",)
    with closing(connect_readonly(path)) as connection:
        connection.row_factory = sqlite3.Row
        branch_required = {
            "id",
            "root_id",
            "root_norm",
            "branch_id",
            "branch_image_ar",
            "what_is_ar",
            "source_refs",
            "source_phrase_ar",
            "status",
            "contaminated",
        }
        root_required = {"root_id", "root_norm", "source_root_norm"}
        missing_branch = branch_required - _available_columns(connection, "branch_images")
        missing_root = root_required - _available_columns(connection, "roots")
        if missing_branch or missing_root:
            raise ContractError(
                "V4 database schema is incomplete: "
                f"branch_images={sorted(missing_branch)}, roots={sorted(missing_root)}"
            )

        root_key_by_id: dict[str, str] = {}
        for root in connection.execute(
            "SELECT root_id, root_norm, source_root_norm FROM roots"
        ):
            matches = {
                canonical_root(str(root[field]))
                for field in ("root_norm", "source_root_norm")
                if root[field]
            }.intersection(passage_roots)
            if matches:
                root_key_by_id[str(root["root_id"])] = sorted(matches)[0]
        if not root_key_by_id:
            raise ContractError("No V4 roots match the rooted passage morphology")

        branch_rows: list[sqlite3.Row] = []
        excluded_contaminated = 0
        root_ids = sorted(root_key_by_id)
        for start in range(0, len(root_ids), 800):
            chunk = root_ids[start : start + 800]
            root_placeholders = ",".join("?" for _ in chunk)
            status_placeholders = ",".join("?" for _ in allowed_statuses)
            parameters = [*chunk, *allowed_statuses]
            branch_rows.extend(
                connection.execute(
                    f"""
                    SELECT
                        b.id, b.root_id, b.root_norm, r.source_root_norm, b.branch_id,
                        b.branch_image_ar, b.what_is_ar, b.source_refs, b.source_phrase_ar,
                        b.status, b.contaminated
                    FROM branch_images AS b
                    JOIN roots AS r ON r.root_id = b.root_id
                    WHERE b.root_id IN ({root_placeholders})
                      AND b.status IN ({status_placeholders})
                      AND b.contaminated = 'no'
                    """,
                    parameters,
                )
            )
            excluded_contaminated += int(
                connection.execute(
                    f"""
                    SELECT COUNT(*)
                    FROM branch_images AS b
                    WHERE b.root_id IN ({root_placeholders})
                      AND b.status IN ({status_placeholders})
                      AND COALESCE(b.contaminated, '') <> 'no'
                    """,
                    parameters,
                ).fetchone()[0]
            )

    records: list[dict[str, Any]] = []
    for source in branch_rows:
        if source["contaminated"] != "no":
            raise ContractError(
                f"Contaminated V4 branch escaped the SQL filter: {source['root_id']}:{source['branch_id']}"
            )
        root_id = str(source["root_id"])
        root_key = root_key_by_id[root_id]
        raw_refs = [
            value.strip()
            for value in str(source["source_refs"]).split(";")
            if value.strip()
        ]
        families = sorted(
            set(source_families(str(source["source_phrase_ar"])))
            | set(source_families_from_refs(str(source["source_refs"])))
        )
        records.append(
            {
                "root_norm": sorted(passage_roots[root_key])[0],
                "root_key": root_key,
                "passage_root_norms": sorted(passage_roots[root_key]),
                "branch_id": str(source["branch_id"]),
                "source_id": "furuq-v4-sqlite",
                "source_name": "furuq-v4 SQLite composite branch inventory",
                "source_entry_id": f"branch_images:{root_id}:{source['branch_id']}",
                "source_ar_exact": str(source["source_phrase_ar"]),
                "branch_image_ar": str(source["branch_image_ar"]),
                "what_is_ar": str(source["what_is_ar"]),
                "lexical_unit_or_form": None,
                "derivation_or_pattern": None,
                "status": str(source["status"]),
                "contaminated": False,
                "editorial_notes": (
                    "Selected directly from branch_images with contaminated='no'; "
                    "branch prose remains a composite editorial record."
                ),
                "provenance_granularity": "composite-tagged" if families else "composite-untagged",
                "source_families": families,
                "source_refs": [
                    f"raw-lexical:branch_images:id:{source['id']}",
                    *raw_refs,
                ],
            }
        )
    records.sort(key=lambda row: (row["root_key"], row["source_entry_id"]))
    return records, excluded_contaminated


def prepare(args: argparse.Namespace) -> dict[str, Any]:
    if args.ayah_start < 1 or args.ayah_end < args.ayah_start:
        raise ContractError("Invalid ayah interval")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", args.run_id):
        raise ContractError("run_id must contain only letters, digits, dot, underscore, or hyphen")
    if not args.output_language.strip() or "\n" in args.output_language or "\r" in args.output_language:
        raise ContractError("output_language must be one non-empty line")
    profile_path = args.profile.resolve()
    require_regular_file(profile_path, "source profile")
    profile = load_json(profile_path)
    profile_errors = validate_instance(profile, "source-profile")
    if profile_errors:
        raise ContractError("Invalid source profile: " + "; ".join(profile_errors[:5]))
    if profile.get("workflow_id") != WORKFLOW_ID:
        raise ContractError(f"Profile workflow mismatch: {profile.get('workflow_id')}")
    if profile.get("repository_root") != ".":
        raise ContractError("V2.1 source profiles must use repository_root '.'")

    resources = profile.get("resources")
    if not isinstance(resources, dict):
        raise ContractError("Profile resources must be an object")
    required_resources = {
        "quran_surah_pattern",
        "qac_database",
        "qac_fallback_tsv",
        "attachments_tsv",
        "lexical_database",
        "lexical_fallback_tsv",
    }
    missing_resources = required_resources - resources.keys()
    if missing_resources:
        raise ContractError(f"Profile is missing resource mappings: {sorted(missing_resources)}")
    inactive_resources = profile.get("inactive_resources", {})
    if not isinstance(inactive_resources, dict):
        raise ContractError("Profile inactive_resources must be an object")
    resources_root = (REPO_ROOT / "resources").resolve()
    for key, value in {**resources, **inactive_resources}.items():
        if not isinstance(value, str):
            raise ContractError(f"Profile resource path must be a string: {key}")
        candidate = resolve_repo_path(value.format(surah=1) if "{surah}" in value else value)
        assert_within(candidate, resources_root, f"profile resource {key}")
    quran_path = resolve_repo_path(resources["quran_surah_pattern"].format(surah=args.surah))
    qac_db_path = resolve_repo_path(resources["qac_database"])
    qac_fallback_path = resolve_repo_path(resources["qac_fallback_tsv"])
    attachments_path = resolve_repo_path(resources["attachments_tsv"])
    lexical_db_path = resolve_repo_path(resources["lexical_database"])
    lexical_fallback_path = resolve_repo_path(resources["lexical_fallback_tsv"])
    scaffold_path = args.primary_scaffold.resolve()
    prohibited_values = profile.get("prohibited_paths")
    if not isinstance(prohibited_values, list) or not prohibited_values:
        raise ContractError("Profile must declare prohibited_paths")
    prohibited_paths = [resolve_repo_path(value) for value in prohibited_values]

    for blocked in prohibited_paths:
        if scaffold_path == blocked or blocked in scaffold_path.parents:
            raise ContractError(f"Primary scaffold is inside a prohibited path: {scaffold_path}")
    if scaffold_path == resources_root or resources_root in scaffold_path.parents:
        raise ContractError(f"Primary scaffold may not originate in raw resources: {scaffold_path}")

    for path, label in (
        (quran_path, "Quran source"),
        (attachments_path, "attachment source"),
        (scaffold_path, "primary scaffold"),
    ):
        require_regular_file(path, label)

    qac_mode = "database" if qac_db_path.is_file() and qac_db_path.stat().st_size else "fallback"
    lexical_mode = "database" if lexical_db_path.is_file() and lexical_db_path.stat().st_size else "fallback"
    if qac_mode == "fallback":
        require_regular_file(qac_fallback_path, "QAC fallback")
    if lexical_mode == "fallback":
        require_regular_file(lexical_fallback_path, "lexical fallback")
    if not args.allow_source_limited:
        raise ContractError(
            "The current lexical adapter supplies composite branch evidence. "
            "Re-run with --allow-source-limited for a non-release pilot."
        )
    passage_rows, passage_metadata = extract_passage(
        quran_path, args.surah, args.ayah_start, args.ayah_end, args.basmala_policy
    )
    if qac_mode == "database":
        morphology_rows = load_qac_database(qac_db_path, args.surah, args.ayah_start, args.ayah_end)
    else:
        morphology_rows = load_qac_fallback(qac_fallback_path, args.surah, args.ayah_start, args.ayah_end)
    if not morphology_rows:
        raise ContractError("No morphology rows were found for the selected passage")
    attachment_count, syntax_rows = filter_attachments(
        attachments_path, args.surah, args.ayah_start, args.ayah_end
    )
    if lexical_mode == "database":
        lexical_rows, excluded_contaminated = load_lexical_database(
            lexical_db_path,
            morphology_rows,
            args.include_review_branches,
        )
        contamination_filter = "database-contaminated-equals-no"
    else:
        lexical_rows = load_lexical_fallback(
            lexical_fallback_path,
            morphology_rows,
            args.include_review_branches,
        )
        excluded_contaminated = 0
        contamination_filter = "fallback-reviewed-clean-export"
    if not lexical_rows:
        raise ContractError("No lexical branches matched the passage roots")

    run_root = args.run_root.resolve()
    for blocked in prohibited_paths:
        if run_root == blocked or blocked in run_root.parents:
            raise ContractError(f"Run directory is inside a prohibited path: {run_root}")
    if run_root == resources_root or resources_root in run_root.parents:
        raise ContractError(f"Run directory may not be inside raw resources: {run_root}")
    ensure_new_directory(run_root)
    inputs = run_root / "inputs"
    logs = run_root / "logs"
    for directory in (
        inputs,
        logs,
        run_root / "tasks",
        run_root / "agent-a" / "draft",
        run_root / "agent-a" / "final",
        run_root / "agent-b",
        run_root / "agent-c",
    ):
        directory.mkdir(parents=True, exist_ok=True)

    passage_path = inputs / "passage-arabic.txt"
    atomic_write_text(
        passage_path,
        "".join(
            f"{row['surah']}:{row['ayah']}\t{row['context_role']}\t{row['text']}\n"
            for row in passage_rows
        ),
    )
    scaffold_target = inputs / "primary-scaffold.md"
    shutil.copyfile(scaffold_path, scaffold_target)

    morphology_path = inputs / "morphology.tsv"
    write_tsv(morphology_path, MORPHOLOGY_FIELDS, morphology_rows)

    syntax_target = inputs / "syntax.tsv"
    write_tsv(syntax_target, SYNTAX_FIELDS, syntax_rows)

    lexical_target = inputs / "lexical-branches.jsonl"
    write_jsonl(lexical_target, lexical_rows)

    quality_tier = "source-limited"
    summary = {
        "workflow_id": WORKFLOW_ID,
        "run_id": args.run_id,
        "quality_tier": quality_tier,
        "source_profile": profile["profile_id"],
        "passage": {
            "surah": args.surah,
            "ayah_start": args.ayah_start,
            "ayah_end": args.ayah_end,
            "positions": len(passage_rows),
            **passage_metadata,
        },
        "morphology": {
            "mode": qac_mode,
            "rows": len(morphology_rows),
            "rooted_only": qac_mode == "fallback",
        },
        "syntax": {"source_rows": attachment_count, "edges": len(syntax_rows)},
        "lexical": {
            "mode": lexical_mode,
            "rows": len(lexical_rows),
            "review_rows_included": args.include_review_branches,
            "contamination_filter": contamination_filter,
            "excluded_contaminated_rows": excluded_contaminated,
        },
        "limitations": [
            "QAC fallback contains rooted aggregate rows rather than the complete morpheme stream."
            if qac_mode == "fallback"
            else "",
            "Lexical records combine source-family prose and cannot establish dictionary-level agreement.",
        ],
    }
    summary["limitations"] = [item for item in summary["limitations"] if item]
    summary_path = inputs / "input-summary.json"
    write_json(summary_path, summary)

    run_card = {
        "workflow_id": WORKFLOW_ID,
        "run_id": args.run_id,
        "passage_id": f"S{args.surah}:{args.ayah_start}-{args.ayah_end}",
        "scope": {"surah": args.surah, "ayah_start": args.ayah_start, "ayah_end": args.ayah_end},
        "basmala_policy": args.basmala_policy,
        "output_language": args.output_language,
        "source_profile": profile["profile_id"],
        "quality_tier": quality_tier,
        "gold_release_eligible": False,
        "lexicon_policy": (
            "accepted-evidence-with-review-candidates-composite-editorial"
            if args.include_review_branches
            else "accepted-clean-composite-editorial"
        ),
        "evidence_policy": "prepared-inputs-only",
        "optional_product": args.optional_product,
    }
    run_card_path = inputs / "run-card.json"
    write_json(run_card_path, run_card)

    return {
        "run_root": str(run_root),
        "run_id": args.run_id,
        "quality_tier": quality_tier,
        "morphology_mode": qac_mode,
        "lexical_mode": lexical_mode,
        "morphology_rows": len(morphology_rows),
        "syntax_edges": len(syntax_rows),
        "lexical_branches": len(lexical_rows),
        "excluded_contaminated_branches": excluded_contaminated,
    }


def main() -> int:
    try:
        result = prepare(parse_args())
    except (ContractError, OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(f"prepare_run: ERROR: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
