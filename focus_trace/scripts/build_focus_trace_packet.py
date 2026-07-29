#!/usr/bin/env python3
"""Build one hermetic focus-trace packet for a single focus ayah."""

from __future__ import annotations

import argparse
import copy
import csv
import gzip
import json
import os
import shutil
import sqlite3
import sys
import tempfile
from pathlib import Path
from typing import Any, Iterable

WORKFLOW_ROOT = Path(__file__).resolve().parents[1]
LATENT_ROOT = WORKFLOW_ROOT.parent
PROJECTS_ROOT = LATENT_ROOT.parent
V12_SCRIPTS = LATENT_ROOT / "v12" / "scripts"
if str(V12_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(V12_SCRIPTS))

from build_packets import (
    DEFAULT_BRANCH_DB,
    DEFAULT_QAC,
    REPO_ROOT,
    canonical_arabic,
    load_ayat,
    ordered_unique,
    parse_refs,
    sha256,
)


BASMALAH_TEMPLATE_REF = "1:1"
BASMALAH_EXCLUDED_SURAHS = {9}
DEFAULT_QAC_FURUQ_ROOT_MAP = (
    PROJECTS_ROOT
    / "quran-data"
    / "data"
    / "bridges"
    / "qac-furuq-v4-root-map.sqlite.gz"
)
DEFAULT_QURAN_DIR = REPO_ROOT / "resources" / "quran"
PROTOCOL = "focus-trace-hermetic-packet-v2"
ROOTLESS_REASON = "QAC has no rooted morphemes for this ayah"


def parse_ref(raw: str) -> str:
    refs = parse_refs(raw)
    if len(refs) != 1:
        raise argparse.ArgumentTypeError("expected exactly one ayah reference")
    if refs[0].endswith(":0"):
        raise argparse.ArgumentTypeError("focus ayah cannot be a synthetic basmalah ref")
    return refs[0]


def parse_radius(raw: str) -> int:
    try:
        value = int(raw)
    except ValueError as error:
        raise argparse.ArgumentTypeError("radius must be an integer") from error
    if value < 0:
        raise argparse.ArgumentTypeError("radius must be non-negative")
    return value


def surah_of(ref: str) -> int:
    return int(ref.split(":", 1)[0])


def ayah_of(ref: str) -> int:
    return int(ref.split(":", 1)[1])


def is_basmalah_ref(ref: str) -> bool:
    return ayah_of(ref) == 0


def resource_key(path: Path) -> str:
    resolved = path.resolve()
    return os.path.relpath(resolved, REPO_ROOT)


def output_in_quran_data(path: Path) -> bool:
    return "quran-data" in path.resolve().parts


def quran_surah_path(quran_dir: Path, surah: int) -> Path:
    return quran_dir / f"surah_{surah}.json"


def load_quran_surah(quran_dir: Path, surah: int) -> dict[int, str]:
    path = quran_surah_path(quran_dir, surah)
    if not path.is_file():
        raise ValueError(f"Quran surah resource not found: {path}")
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    verses = data.get("verse")
    if not isinstance(verses, dict):
        raise ValueError(f"{path}: missing verse object")
    count = int(data.get("count", 0))
    ayat: dict[int, str] = {}
    for ayah in range(1, count + 1):
        key = f"verse_{ayah}"
        text = verses.get(key)
        if not isinstance(text, str) or not text.strip():
            raise ValueError(f"{path}: missing text for {key}")
        ayat[ayah] = text
    if not ayat:
        raise ValueError(f"{path}: no numbered ayat found")
    return ayat


def numbered_refs_for_surah(quran_dir: Path, surah: int) -> list[str]:
    ayat = load_quran_surah(quran_dir, surah)
    return [f"{surah}:{ayah}" for ayah in sorted(ayat)]


def qac_refs_present(qac_path: Path, refs: set[str]) -> set[str]:
    if not refs:
        return set()
    present: set[str] = set()
    with qac_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            ref = row["ayah_ref"]
            if ref in refs:
                present.add(ref)
    return present


def rootless_ayah(quran_dir: Path, ref: str) -> dict[str, Any]:
    surah = surah_of(ref)
    ayah = ayah_of(ref)
    text = load_quran_surah(quran_dir, surah).get(ayah)
    if text is None:
        raise ValueError(f"Quran text missing for rootless ayah {ref}")
    return {
        "ref": ref,
        "text_ar": text,
        "text_norm_ar": canonical_arabic(text),
        "root_sequence": [],
        "root_occurrences": [],
        "rootless": True,
        "rootless_reason": ROOTLESS_REASON,
    }


def validate_window_refs(quran_dir: Path, focus_ref: str, window: list[str]) -> None:
    surah = surah_of(focus_ref)
    canonical_refs = set(numbered_refs_for_surah(quran_dir, surah))
    for ref in window:
        if is_basmalah_ref(ref):
            continue
        if ref not in canonical_refs:
            raise ValueError(f"window ref is not in Quran surah resource: {ref}")


def rooted_numbered_refs_for_surah(qac_path: Path, surah: int) -> list[str]:
    prefix = f"{surah}:"
    refs: set[str] = set()
    with qac_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            ref = row["ayah_ref"]
            if ref.startswith(prefix):
                refs.add(ref)
    if not refs:
        raise ValueError(f"no ayat found for surah {surah}")
    return sorted(refs, key=ayah_of)


def add_basmalah_if_requested(
    refs: list[str],
    surah: int,
    include_basmalah: bool,
) -> list[str]:
    if not include_basmalah or surah in BASMALAH_EXCLUDED_SURAHS:
        return refs
    synthetic_ref = f"{surah}:0"
    if surah == 1:
        return [synthetic_ref, *[ref for ref in refs if ref != BASMALAH_TEMPLATE_REF]]
    return [synthetic_ref, *refs]


def window_for_radius(
    quran_dir: Path,
    focus_ref: str,
    radius: int,
    include_basmalah: bool,
) -> list[str]:
    surah = surah_of(focus_ref)
    focus_ayah = ayah_of(focus_ref)
    refs = numbered_refs_for_surah(quran_dir, surah)
    numbers = [ayah_of(ref) for ref in refs]
    start = max(min(numbers), focus_ayah - radius)
    end = min(max(numbers), focus_ayah + radius)
    window = [ref for ref in refs if start <= ayah_of(ref) <= end]
    if start == min(numbers):
        window = add_basmalah_if_requested(window, surah, include_basmalah)
    return window


def window_for_surah(quran_dir: Path, focus_ref: str, include_basmalah: bool) -> list[str]:
    surah = surah_of(focus_ref)
    return add_basmalah_if_requested(
        numbered_refs_for_surah(quran_dir, surah),
        surah,
        include_basmalah,
    )


def make_basmalah_ayah(template: dict[str, Any], target_ref: str) -> dict[str, Any]:
    ayah = copy.deepcopy(template)
    ayah["ref"] = target_ref
    ayah["synthetic_source_ref"] = BASMALAH_TEMPLATE_REF
    return ayah


def load_window_ayat(qac_path: Path, quran_dir: Path, window: list[str]) -> dict[str, dict[str, Any]]:
    basmalah_refs = [ref for ref in window if is_basmalah_ref(ref)]
    real_refs = [ref for ref in window if not is_basmalah_ref(ref)]
    qac_present = qac_refs_present(qac_path, set(real_refs))
    load_refs = set(qac_present)
    if basmalah_refs:
        load_refs.add(BASMALAH_TEMPLATE_REF)
    ayat = load_ayat(qac_path, load_refs)
    for ref in basmalah_refs:
        ayat[ref] = make_basmalah_ayah(ayat[BASMALAH_TEMPLATE_REF], ref)
    for ref in real_refs:
        if ref not in ayat:
            ayat[ref] = rootless_ayah(quran_dir, ref)
    return ayat


def occurrence_phrase(occurrence: dict[str, Any]) -> str:
    surfaces = occurrence.get("surfaces_ar", [])
    if surfaces:
        return " ".join(surfaces)
    return ""


def source_phrases(
    ayat: Iterable[dict[str, Any]],
    root: str,
) -> list[dict[str, Any]]:
    phrases: list[dict[str, Any]] = []
    seen: set[tuple[str, str, tuple[str, ...]]] = set()
    for ayah in ayat:
        for occurrence in ayah["root_occurrences"]:
            if occurrence["root"] != root:
                continue
            phrase = occurrence_phrase(occurrence)
            key = (ayah["ref"], phrase, tuple(occurrence.get("word_indices", [])))
            if key in seen:
                continue
            seen.add(key)
            phrases.append(
                {
                    "source_ref": ayah["ref"],
                    "source_phrase_ar": phrase,
                    "source_surfaces_ar": occurrence.get("surfaces_ar", []),
                    "source_word_indices": occurrence.get("word_indices", []),
                    "source_lemmas_ar": occurrence.get("lemmas_ar", []),
                    "source_pos_tags": occurrence.get("pos_tags", []),
                }
            )
    return phrases


def first_seen_roots(ayat: Iterable[dict[str, Any]]) -> list[str]:
    return ordered_unique(
        occurrence["root"]
        for ayah in ayat
        for occurrence in ayah["root_occurrences"]
    )


def refs_by_root(ayat: Iterable[dict[str, Any]]) -> dict[str, list[str]]:
    refs: dict[str, list[str]] = {}
    for ayah in ayat:
        for occurrence in ayah["root_occurrences"]:
            root = occurrence["root"]
            refs.setdefault(root, [])
            if ayah["ref"] not in refs[root]:
                refs[root].append(ayah["ref"])
    return refs


def bool_from_sql(value: Any) -> bool:
    return value in {1, "1", True, "true", "yes"}


def root_mapping_summary(mapping: dict[str, Any]) -> dict[str, Any]:
    return {
        "qac_root": mapping["qac_root"],
        "mapping_status": mapping["mapping_status"],
        "qac_total_occurrences": mapping["qac_total_occurrences"],
        "matched_occurrences": mapping["matched_occurrences"],
        "unmapped_reason": mapping["unmapped_reason"],
        "targets": [
            {
                "target_rank": target["target_rank"],
                "furuq_root_id": target["furuq_root_id"],
                "furuq_root_norm": target["furuq_root_norm"],
                "furuq_source_root_norm": target["furuq_source_root_norm"],
                "furuq_resolution": target["furuq_resolution"],
                "target_occurrences": target["target_occurrences"],
                "is_dominant": target["is_dominant"],
            }
            for target in mapping["targets"]
        ],
    }


def load_root_mappings(
    root_map_db_gz: Path,
    roots: list[str],
) -> dict[str, dict[str, Any]]:
    mappings: dict[str, dict[str, Any]] = {
        root: {
            "qac_root": root,
            "mapping_status": "missing_in_root_map",
            "qac_total_occurrences": None,
            "matched_occurrences": 0,
            "unmapped_reason": "root not present in qac-furuq-v4-root-map",
            "targets": [],
        }
        for root in roots
    }
    if not roots:
        return mappings

    with tempfile.NamedTemporaryFile(suffix=".sqlite") as temp_db:
        with gzip.open(root_map_db_gz, "rb") as source:
            shutil.copyfileobj(source, temp_db)
        temp_db.flush()
        connection = sqlite3.connect(temp_db.name)
        connection.row_factory = sqlite3.Row
        placeholders = ",".join("?" for _ in roots)
        query = f"""
            SELECT qac_root_norm, mapping_status, qac_total_occurrences,
                   matched_occurrences, target_rank, frozen_root_norm,
                   furuq_root_id, furuq_root_norm, furuq_source_root_norm,
                   furuq_resolution, target_occurrences, is_dominant,
                   has_furuq_root, unmapped_reason
            FROM qac_to_furuq
            WHERE qac_root_norm IN ({placeholders})
            ORDER BY qac_root_norm, target_rank
        """
        for row in connection.execute(query, roots):
            record = mappings[row["qac_root_norm"]]
            record["mapping_status"] = row["mapping_status"]
            record["qac_total_occurrences"] = row["qac_total_occurrences"]
            record["matched_occurrences"] = row["matched_occurrences"]
            record["unmapped_reason"] = row["unmapped_reason"] or ""
            if not bool_from_sql(row["has_furuq_root"]):
                continue
            record["targets"].append(
                {
                    "target_rank": int(row["target_rank"]),
                    "frozen_root_norm": row["frozen_root_norm"],
                    "furuq_root_id": row["furuq_root_id"],
                    "furuq_root_norm": row["furuq_root_norm"],
                    "furuq_source_root_norm": row["furuq_source_root_norm"],
                    "furuq_resolution": row["furuq_resolution"],
                    "target_occurrences": int(row["target_occurrences"] or 0),
                    "is_dominant": bool_from_sql(row["is_dominant"]),
                }
            )
        connection.close()
    return mappings


def combine_variant_field(branch: dict[str, Any], field: str) -> str:
    values = ordered_unique(
        variant[field]
        for variant in branch["variants"]
        if variant.get(field)
    )
    if len(values) == 1:
        return values[0]
    return "\n".join(f"{index}. {value}" for index, value in enumerate(values, start=1))


def append_mapped_branch_row(branches: list[dict[str, Any]], row: dict[str, Any]) -> None:
    for branch in branches:
        if (
            branch["mapped_root_id"] == row["mapped_root_id"]
            and branch["branch_id"] == row["branch_id"]
        ):
            branch["variants"].extend(row["variants"])
            for field in ("image_ar", "image_en", "scope_ar", "scope_en"):
                branch[field] = combine_variant_field(branch, field)
            return
    branches.append(row)


def load_branches_for_mapped_roots(
    branch_db_gz: Path,
    root_mappings: dict[str, dict[str, Any]],
) -> tuple[dict[str, list[dict[str, Any]]], list[str], list[dict[str, Any]]]:
    branches: dict[str, list[dict[str, Any]]] = {
        qac_root: [] for qac_root in root_mappings
    }
    targets_by_root_id: dict[str, list[tuple[str, dict[str, Any]]]] = {}
    for qac_root, mapping in root_mappings.items():
        for target in mapping["targets"]:
            targets_by_root_id.setdefault(target["furuq_root_id"], []).append(
                (qac_root, target)
            )

    if not targets_by_root_id:
        return branches, list(root_mappings), []

    branch_rows_by_root_id: dict[str, list[sqlite3.Row]] = {
        root_id: [] for root_id in targets_by_root_id
    }
    with tempfile.NamedTemporaryFile(suffix=".sqlite") as temp_db:
        with gzip.open(branch_db_gz, "rb") as source:
            shutil.copyfileobj(source, temp_db)
        temp_db.flush()
        connection = sqlite3.connect(temp_db.name)
        connection.row_factory = sqlite3.Row
        root_ids = sorted(targets_by_root_id)
        placeholders = ",".join("?" for _ in root_ids)
        query = f"""
            SELECT root_norm, root_id, source_path, branch_id,
                   branch_image_ar, branch_image_en, what_is_ar, what_is_en
            FROM branch_images
            WHERE root_id IN ({placeholders})
              AND contaminated = 'no'
            ORDER BY root_id, CAST(SUBSTR(branch_id, 2) AS INTEGER), id
        """
        for row in connection.execute(query, root_ids):
            branch_rows_by_root_id[row["root_id"]].append(row)
        connection.close()

    for qac_root, mapping in root_mappings.items():
        for target in mapping["targets"]:
            rows = branch_rows_by_root_id.get(target["furuq_root_id"], [])
            for row in rows:
                append_mapped_branch_row(
                    branches[qac_root],
                    {
                        "mapped_root_id": target["furuq_root_id"],
                        "mapped_root_norm": target["furuq_root_norm"],
                        "mapped_source_root_norm": target["furuq_source_root_norm"],
                        "mapped_target_rank": target["target_rank"],
                        "mapped_is_dominant": target["is_dominant"],
                        "mapped_target_occurrences": target["target_occurrences"],
                        "branch_id": row["branch_id"],
                        "image_ar": row["branch_image_ar"],
                        "image_en": row["branch_image_en"],
                        "scope_ar": row["what_is_ar"],
                        "scope_en": row["what_is_en"],
                        "variants": [
                            {
                                "root_id": row["root_id"],
                                "source_path": row["source_path"],
                                "image_ar": row["branch_image_ar"],
                                "image_en": row["branch_image_en"],
                                "scope_ar": row["what_is_ar"],
                                "scope_en": row["what_is_en"],
                            }
                        ],
                    },
                )

    missing = [qac_root for qac_root, items in branches.items() if not items]
    target_missing = []
    for qac_root, mapping in root_mappings.items():
        for target in mapping["targets"]:
            if not branch_rows_by_root_id.get(target["furuq_root_id"]):
                target_missing.append(
                    {
                        "qac_root": qac_root,
                        "furuq_root_id": target["furuq_root_id"],
                        "furuq_root_norm": target["furuq_root_norm"],
                        "reason": "no non-contaminated branch rows for mapped root_id",
                    }
                )
    return branches, missing, target_missing


def branch_mapping_fields(branch: dict[str, Any]) -> dict[str, Any]:
    return {
        "mapped_root_id": branch["mapped_root_id"],
        "mapped_root_norm": branch["mapped_root_norm"],
        "mapped_source_root_norm": branch["mapped_source_root_norm"],
        "mapped_target_rank": branch["mapped_target_rank"],
        "mapped_is_dominant": branch["mapped_is_dominant"],
        "mapped_target_occurrences": branch["mapped_target_occurrences"],
    }


def focus_branch(branch: dict[str, Any]) -> dict[str, Any]:
    result = {
        **branch_mapping_fields(branch),
        "branch_id": branch["branch_id"],
        "branch_image_ar": branch["image_ar"],
        "branch_image_en": branch["image_en"],
        "scope_ar": branch["scope_ar"],
        "scope_en": branch["scope_en"],
    }
    if branch.get("variants"):
        result["variants"] = [
            {
                "root_id": variant["root_id"],
                "source_path": variant["source_path"],
                "branch_image_ar": variant["image_ar"],
                "branch_image_en": variant["image_en"],
                "scope_ar": variant["scope_ar"],
                "scope_en": variant["scope_en"],
            }
            for variant in branch["variants"]
        ]
    return result


def compact_branch(branch: dict[str, Any], mode: str) -> dict[str, Any]:
    result = {
        **branch_mapping_fields(branch),
        "branch_id": branch["branch_id"],
        "branch_image_ar": branch["image_ar"],
    }
    if mode in {"images_en", "full"}:
        result["branch_image_en"] = branch["image_en"]
    if mode == "full":
        result["scope_ar"] = branch["scope_ar"]
        result["scope_en"] = branch["scope_en"]
        if branch.get("variants"):
            result["variant_count"] = len(branch["variants"])
    return result


def ordered_packet_roots(focus_ayat: list[dict[str, Any]], context_ayat: list[dict[str, Any]]) -> list[str]:
    return ordered_unique([*first_seen_roots(focus_ayat), *first_seen_roots(context_ayat)])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--focus", required=True, type=parse_ref, help="focus ayah, e.g. 100:1")
    context = parser.add_mutually_exclusive_group(required=True)
    context.add_argument("--window", type=parse_refs, help="comma-separated ayah refs")
    context.add_argument("--surah-window", action="store_true", help="use the focus ayah's whole numbered surah")
    context.add_argument("--radius", type=parse_radius, help="use N ayat before and after the focus ayah")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--qac", type=Path, default=DEFAULT_QAC)
    parser.add_argument("--quran-dir", type=Path, default=DEFAULT_QURAN_DIR)
    parser.add_argument("--branches", type=Path, default=DEFAULT_BRANCH_DB)
    parser.add_argument("--root-map", type=Path, default=DEFAULT_QAC_FURUQ_ROOT_MAP)
    parser.add_argument(
        "--include-basmalah",
        action="store_true",
        help="add a synthetic {surah}:0 basmalah when the selected window touches the start of a surah",
    )
    parser.add_argument(
        "--non-focus-branch-mode",
        choices=["images", "images_en", "full"],
        default="images",
        help="branch detail shared for context roots; all modes include branch_image_ar",
    )
    parser.add_argument(
        "--strict-branches",
        action="store_true",
        help="fail if any packet root lacks a non-contaminated branch inventory",
    )
    args = parser.parse_args()

    for path in (args.qac, args.branches, args.root_map):
        if not path.is_file():
            parser.error(f"resource not found: {path}")
    if not args.quran_dir.is_dir():
        parser.error(f"resource directory not found: {args.quran_dir}")
    quran_path = quran_surah_path(args.quran_dir, surah_of(args.focus))

    if args.window:
        window = args.window
        try:
            validate_window_refs(args.quran_dir, args.focus, window)
        except ValueError as error:
            parser.error(str(error))
    elif args.surah_window:
        window = window_for_surah(args.quran_dir, args.focus, args.include_basmalah)
    else:
        window = window_for_radius(args.quran_dir, args.focus, args.radius, args.include_basmalah)

    if args.focus not in window:
        parser.error("--focus must be present in the selected window")
    if any(surah_of(ref) != surah_of(args.focus) for ref in window):
        parser.error("all window refs must be in the focus surah")
    if output_in_quran_data(args.output):
        parser.error("--output must not write generated data under quran-data")

    ayat_by_ref = load_window_ayat(args.qac, args.quran_dir, window)
    ayat = [ayat_by_ref[ref] for ref in window]
    focus_ayah = ayat_by_ref[args.focus]
    context_ayat = [ayah for ayah in ayat if ayah["ref"] != args.focus]
    focus_roots = first_seen_roots([focus_ayah])
    context_roots = first_seen_roots(context_ayat)
    all_roots = ordered_packet_roots([focus_ayah], context_ayat)
    root_mappings = load_root_mappings(args.root_map, all_roots)
    branches, missing_roots, missing_mapped_targets = load_branches_for_mapped_roots(
        args.branches,
        root_mappings,
    )
    if args.strict_branches and missing_roots:
        raise ValueError(
            "no non-contaminated branch inventory for roots: "
            f"{missing_roots}"
        )

    refs_for_missing = refs_by_root(ayat)
    resource_hashes = {
        resource_key(path): sha256(path)
        for path in (args.qac, args.branches, args.root_map, quran_path)
    }
    rootless_ayat = [
        {
            "ref": ayah["ref"],
            "reason": ayah["rootless_reason"],
        }
        for ayah in ayat
        if ayah.get("rootless") is True
    ]

    packet = {
        "protocol": PROTOCOL,
        "focus_ref": args.focus,
        "window": window,
        "context_order": [ref for ref in window if ref != args.focus],
        "ayah_count": len(window),
        "model_profile": {
            "model": "gpt-5.6-sol",
            "reasoning_effort": "max",
        },
        "selection_policy": {
            "window_policy": (
                "The coordinator selects a fixed window. Roots are never selected "
                "or pruned by the reader."
            ),
            "focus_root_policy": (
                "All roots occurring in the focus ayah are included in first-seen "
                "focus order with full non-contaminated branch inventories."
            ),
            "context_root_policy": (
                "All roots occurring in non-focus context ayat are included in "
                "packet order and root order. Each occurrence includes source_phrase_ar. "
                "Rootless context ayat are retained as text-only context and have no "
                "branch-citable roots."
            ),
            "non_focus_branch_policy": (
                f"Every context root with a non-contaminated inventory includes all branch IDs "
                f"in {args.non_focus_branch_mode!r} mode; this always includes branch_image_ar."
            ),
            "root_mapping_policy": (
                "QAC roots are resolved through qac-furuq-v4-root-map.sqlite.gz. "
                "If a QAC root maps to multiple Furuq root_ids, every mapped root "
                "and its non-contaminated branches are included in "
                "target_rank order. Branch IDs are root-local, so reader citations "
                "must pair branch_id with mapped_root_id."
            ),
            "source_phrase_policy": (
                "source_phrase_ar is deterministically derived from QAC surfaces_ar "
                "for the root occurrence in that source ayah."
            ),
        },
        "root_mappings": [
            root_mapping_summary(root_mappings[root]) for root in all_roots
        ],
        "focus_ayah": focus_ayah,
        "context_ayat": context_ayat,
        "focus_branch_inventories": [
            {
                "root": root,
                "root_mapping": root_mapping_summary(root_mappings[root]),
                "source_phrases": source_phrases([focus_ayah], root),
                "branches": [focus_branch(branch) for branch in branches[root]],
            }
            for root in focus_roots
            if branches[root]
        ],
        "context_root_cues": [
            {
                "root": root,
                "root_mapping": root_mapping_summary(root_mappings[root]),
                "source_phrases": source_phrases(context_ayat, root),
                "branch_inventory_mode": args.non_focus_branch_mode,
                "branches": [
                    compact_branch(branch, args.non_focus_branch_mode)
                    for branch in branches[root]
                ],
            }
            for root in context_roots
            if branches[root]
        ],
        "missing_branch_inventories": [
            {
                "root": root,
                "root_mapping": root_mapping_summary(root_mappings[root]),
                "refs": refs_for_missing[root],
                "source_phrases": source_phrases(ayat, root),
                "reason": "no non-contaminated branch inventory in resource",
            }
            for root in missing_roots
        ],
        "provenance": {
            "branch_filter": {
                "status": "any",
                "contaminated": "no",
                "origin_corpus": ["furuq", "quranic"],
            },
            "missing_mapped_targets": missing_mapped_targets,
            "rootless_ayat": rootless_ayat,
            "resource_sha256": resource_hashes,
            "synthetic_ayat": [
                {
                    "ref": ref,
                    "kind": "basmalah",
                    "source_ref": BASMALAH_TEMPLATE_REF,
                }
                for ref in window
                if is_basmalah_ref(ref)
            ],
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(packet, ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    print(f"focus-trace packet: {args.output}")


if __name__ == "__main__":
    main()
