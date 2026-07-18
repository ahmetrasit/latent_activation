#!/usr/bin/env python3
"""Build one all-material packet for v12 full-context reader runs."""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import shutil
import sqlite3
import tempfile
from pathlib import Path
from typing import Any, Iterable

from build_packets import (
    DEFAULT_BRANCH_DB,
    DEFAULT_QAC,
    DEFAULT_TRANSLATIONS,
    REPO_ROOT,
    load_ayat,
    ordered_unique,
    parse_refs,
    sha256,
)


def parse_surah(raw: str) -> int:
    if not raw.isdigit() or int(raw) < 1:
        raise argparse.ArgumentTypeError("expected a positive surah number")
    return int(raw)


def refs_for_surah(qac_path: Path, surah: int) -> list[str]:
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
    return sorted(refs, key=lambda ref: int(ref.split(":", 1)[1]))


def first_seen_roots(ayat: Iterable[dict]) -> list[str]:
    return ordered_unique(
        occurrence["root"]
        for ayah in ayat
        for occurrence in ayah["root_occurrences"]
    )


def load_branches_with_missing(
    branch_db_gz: Path,
    roots: list[str],
) -> tuple[dict[str, list[dict[str, str]]], list[str]]:
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
        for row in connection.execute(query, roots):
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

    missing = [root for root in roots if not branches[root]]
    return branches, missing


def root_refs(ayat: Iterable[dict[str, Any]]) -> dict[str, list[str]]:
    refs: dict[str, list[str]] = {}
    for ayah in ayat:
        for occurrence in ayah["root_occurrences"]:
            root = occurrence["root"]
            refs.setdefault(root, [])
            if ayah["ref"] not in refs[root]:
                refs[root].append(ayah["ref"])
    return refs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--surah", type=parse_surah, help="surah number, e.g. 100")
    source.add_argument("--window", type=parse_refs, help="comma-separated ayah refs")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--qac", type=Path, default=DEFAULT_QAC)
    parser.add_argument("--branches", type=Path, default=DEFAULT_BRANCH_DB)
    parser.add_argument("--translations", type=Path, default=DEFAULT_TRANSLATIONS)
    parser.add_argument(
        "--strict-branches",
        action="store_true",
        help="fail if any root lacks an accepted, non-contaminated branch inventory",
    )
    args = parser.parse_args()

    paths = [args.qac, args.branches, args.translations]
    for path in paths:
        if not path.is_file():
            parser.error(f"resource not found: {path}")

    window = refs_for_surah(args.qac, args.surah) if args.surah else args.window
    ayat_by_ref = load_ayat(args.qac, set(window))
    with args.translations.open(encoding="utf-8") as handle:
        translations = json.load(handle)
    for ref in window:
        ayat_by_ref[ref]["translation_en"] = translations.get(ref, "")

    ayat = [ayat_by_ref[ref] for ref in window]
    roots = first_seen_roots(ayat)
    branches, missing_roots = load_branches_with_missing(args.branches, roots)
    if args.strict_branches and missing_roots:
        raise ValueError(
            "no accepted, non-contaminated branch inventory for roots: "
            f"{missing_roots}"
        )
    refs_by_root = root_refs(ayat)
    resource_hashes = {str(path.relative_to(REPO_ROOT)): sha256(path) for path in paths}

    packet = {
        "protocol": "v12-full-context-v1",
        "window": window,
        "ayah_count": len(window),
        "ayat": ayat,
        "branch_inventories": [
            {"root": root, "branches": branches[root]} for root in roots
            if branches[root]
        ],
        "missing_branch_inventories": [
            {
                "root": root,
                "refs": refs_by_root[root],
                "reason": "no accepted, non-contaminated branch inventory in resource",
            }
            for root in missing_roots
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

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(packet, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"full-context packet: {args.output}")


if __name__ == "__main__":
    main()
