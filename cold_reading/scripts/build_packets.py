#!/usr/bin/env python3
"""Build cumulative, non-leaking packets for staged cold-reader experiments."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import shutil
import sqlite3
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_QAC = REPO_ROOT / "resources" / "qac_root_ayah.tsv"
DEFAULT_BRANCH_DB = REPO_ROOT / "resources" / "furuq_v4.sqlite.gz"
DEFAULT_TRANSLATIONS = REPO_ROOT / "resources" / "quran" / "quran-en.json"


def parse_refs(raw: str) -> list[str]:
    refs = [item.strip() for item in raw.split(",") if item.strip()]
    if not refs:
        raise argparse.ArgumentTypeError("expected at least one ayah reference")
    for ref in refs:
        pieces = ref.split(":")
        if len(pieces) != 2 or not all(piece.isdigit() for piece in pieces):
            raise argparse.ArgumentTypeError(f"invalid ayah reference: {ref}")
    if len(set(refs)) != len(refs):
        raise argparse.ArgumentTypeError("ayah references must be unique")
    return refs


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def split_semicolon(value: str) -> list[str]:
    return [item for item in value.split(";") if item]


def ordered_unique(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def load_ayat(qac_path: Path, wanted_refs: set[str]) -> dict[str, dict[str, Any]]:
    rows_by_ref: dict[str, list[dict[str, str]]] = defaultdict(list)
    with qac_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if row["ayah_ref"] in wanted_refs:
                rows_by_ref[row["ayah_ref"]].append(row)

    missing = wanted_refs - rows_by_ref.keys()
    if missing:
        raise ValueError(f"references absent from QAC resource: {sorted(missing)}")

    ayat: dict[str, dict[str, Any]] = {}
    for ref, rows in rows_by_ref.items():
        first = rows[0]
        sequence = split_semicolon(first["ayah_root_sequence"])
        row_by_root = {row["root_norm"]: row for row in rows}
        roots = ordered_unique(sequence)
        root_occurrences: list[dict[str, Any]] = []
        for root in roots:
            row = row_by_root[root]
            root_occurrences.append(
                {
                    "root": root,
                    "occurrence_count": int(row["occurrence_count"]),
                    "word_indices": split_semicolon(row["word_indices"]),
                    "surfaces_ar": split_semicolon(row["surfaces_ar"]),
                    "lemmas_ar": split_semicolon(row["lemmas_ar"]),
                    "pos_tags": split_semicolon(row["pos_tags"]),
                }
            )
        ayat[ref] = {
            "ref": ref,
            "text_ar": first["ayah_text_ar"],
            "text_norm_ar": first["ayah_text_norm_ar"],
            "root_sequence": sequence,
            "root_occurrences": root_occurrences,
        }
    return ayat


def load_branches(branch_db_gz: Path, roots: set[str]) -> dict[str, list[dict[str, str]]]:
    branches: dict[str, list[dict[str, str]]] = {root: [] for root in roots}
    with tempfile.NamedTemporaryFile(suffix=".sqlite") as temp_db:
        with gzip.open(branch_db_gz, "rb") as source:
            shutil.copyfileobj(source, temp_db)
        temp_db.flush()
        connection = sqlite3.connect(temp_db.name)
        connection.row_factory = sqlite3.Row
        placeholders = ",".join("?" for _ in roots)
        query = f"""
            SELECT root_norm, branch_id, branch_image_ar, branch_image_en,
                   what_is_ar, what_is_en
            FROM branch_images
            WHERE root_norm IN ({placeholders})
              AND status = 'accepted'
              AND contaminated = 'no'
            ORDER BY root_norm, CAST(SUBSTR(branch_id, 2) AS INTEGER)
        """
        for row in connection.execute(query, sorted(roots)):
            branches[row["root_norm"]].append(
                {
                    "branch_id": row["branch_id"],
                    "image_ar": row["branch_image_ar"],
                    "image_en": row["branch_image_en"],
                    "scope_ar": row["what_is_ar"],
                    "scope_en": row["what_is_en"],
                }
            )
        connection.close()

    absent = [root for root, records in branches.items() if not records]
    if absent:
        raise ValueError(f"no canonical branch inventory for roots: {absent}")
    return branches


def stage_filename(stage: int, ref: str, focus: bool) -> str:
    role = "focus" if focus else "reveal"
    return f"stage_{stage:02d}_{role}_{ref.replace(':', '_')}.json"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--focus", required=True, help="focus ayah, e.g. 103:2")
    parser.add_argument("--window", required=True, type=parse_refs, help="comma-separated ayah refs")
    parser.add_argument(
        "--reveal-order",
        required=True,
        type=parse_refs,
        help="all non-focus window refs in the order shown to the reader",
    )
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--qac", type=Path, default=DEFAULT_QAC)
    parser.add_argument("--branches", type=Path, default=DEFAULT_BRANCH_DB)
    parser.add_argument("--translations", type=Path, default=DEFAULT_TRANSLATIONS)
    args = parser.parse_args()

    if args.focus not in args.window:
        parser.error("--focus must be present in --window")
    expected_reveals = [ref for ref in args.window if ref != args.focus]
    if set(args.reveal_order) != set(expected_reveals) or len(args.reveal_order) != len(expected_reveals):
        parser.error("--reveal-order must contain every non-focus window ref exactly once")

    paths = [args.qac, args.branches, args.translations]
    for path in paths:
        if not path.is_file():
            parser.error(f"resource not found: {path}")

    ayat = load_ayat(args.qac, set(args.window))
    with args.translations.open(encoding="utf-8") as handle:
        translations = json.load(handle)
    for ref in args.window:
        ayat[ref]["translation_en"] = translations.get(ref, "")

    all_roots = {
        occurrence["root"]
        for ref in args.window
        for occurrence in ayat[ref]["root_occurrences"]
    }
    branches = load_branches(args.branches, all_roots)

    args.output.mkdir(parents=True, exist_ok=True)
    resource_hashes = {
        str(path.relative_to(REPO_ROOT)): sha256(path)
        for path in paths
    }
    reveal_sequence = [args.focus, *args.reveal_order]
    stage_files: list[str] = []

    for stage, new_ref in enumerate(reveal_sequence):
        revealed_refs = reveal_sequence[: stage + 1]
        revealed_roots = ordered_unique(
            occurrence["root"]
            for ref in revealed_refs
            for occurrence in ayat[ref]["root_occurrences"]
        )
        filename = stage_filename(stage, new_ref, focus=(stage == 0))
        packet = {
            "protocol": "cold-reading-v1",
            "focus_ref": args.focus,
            "stage": stage,
            "is_final_stage": stage == len(reveal_sequence) - 1,
            "newly_revealed_ref": new_ref,
            "revealed_refs": revealed_refs,
            "hidden_ref_count": len(reveal_sequence) - stage - 1,
            "ayat": [ayat[ref] for ref in revealed_refs],
            "branch_inventories": [
                {"root": root, "branches": branches[root]}
                for root in revealed_roots
            ],
            "provenance": {
                "branch_filter": {
                    "status": "accepted",
                    "contaminated": "no",
                    "origin_corpus": ["furuq", "quranic"],
                },
                "resource_sha256": resource_hashes,
            },
        }
        output_path = args.output / filename
        output_path.write_text(
            json.dumps(packet, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        stage_files.append(filename)

    manifest = {
        "protocol": "cold-reading-v1",
        "focus_ref": args.focus,
        "window": args.window,
        "reveal_order": args.reveal_order,
        "stage_files": stage_files,
        "resource_sha256": resource_hashes,
    }
    (args.output / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
