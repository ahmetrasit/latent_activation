#!/usr/bin/env python3
"""Prepare the minimal evidence package for a GSLS V3 run."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import sqlite3
import sys
import unicodedata
from contextlib import closing
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PACKAGE_ROOT.parent
RESOURCES_ROOT = REPO_ROOT / "resources"

QAC_DATABASE = RESOURCES_ROOT / "qac.sqlite"
ATTACHMENTS_TSV = RESOURCES_ROOT / "attachments.tsv"
LEXICAL_DATABASE = RESOURCES_ROOT / "furuq_v4.sqlite"
QURAN_DIRECTORY = RESOURCES_ROOT / "quran"

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

SYNTAX_FIELDS = (
    "edge_id",
    "source_position",
    "target_position",
    "edge_type",
    "direction",
    "confidence",
    "exact_surface_span",
    "evidence",
    "reason",
)

LEXICAL_FIELDS = (
    "root_id",
    "root_norm",
    "branch_id",
    "what_is_ar",
    "branch_image_ar",
    "source_phrase_ar",
)

ALEF_TO_HAMZA = str.maketrans(
    {
        "\u0622": "\u0621",
        "\u0623": "\u0621",
        "\u0625": "\u0621",
        "\u0671": "\u0621",
        "\u0672": "\u0621",
        "\u0673": "\u0621",
        "\u0649": "\u064a",
    }
)


class PreparationError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--surah", type=int, required=True, choices=range(1, 115))
    parser.add_argument("--ayah-start", type=int, required=True)
    parser.add_argument("--ayah-end", type=int, required=True)
    parser.add_argument("--primary-scaffold", type=Path, required=True)
    parser.add_argument("--include-opening-context", action="store_true")
    return parser.parse_args()


def canonical_root(value: str) -> str:
    text = unicodedata.normalize("NFKC", value).translate(ALEF_TO_HAMZA)
    text = text.replace("\u0640", "")
    return "".join(
        char
        for char in text
        if not char.isspace() and unicodedata.category(char) != "Mn"
    )


def require_file(path: Path, label: str) -> None:
    if not path.is_file() or path.stat().st_size == 0:
        raise PreparationError(f"Missing or empty {label}: {path}")


def connect_readonly(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(f"{path.resolve().as_uri()}?mode=ro", uri=True)
    connection.execute("PRAGMA query_only = ON")
    return connection


def available_columns(connection: sqlite3.Connection, table: str) -> set[str]:
    return {str(row[1]) for row in connection.execute(f"PRAGMA table_info({table})")}


def prepare_run_root(path: Path) -> None:
    if path.exists() and any(path.iterdir()):
        raise PreparationError(f"Run directory is not empty: {path}")
    for relative in ("inputs", "tasks", "a1", "a2"):
        (path / relative).mkdir(parents=True, exist_ok=True)


def load_passage(
    surah: int,
    ayah_start: int,
    ayah_end: int,
    include_opening_context: bool,
) -> list[dict[str, Any]]:
    path = QURAN_DIRECTORY / f"surah_{surah}.json"
    require_file(path, "Quran source")
    with path.open(encoding="utf-8-sig") as handle:
        document = json.load(handle)
    if int(document.get("index", 0)) != surah or not isinstance(document.get("verse"), dict):
        raise PreparationError(f"Unexpected Quran document for S{surah}: {path}")

    verses = document["verse"]
    rows: list[dict[str, Any]] = []
    if include_opening_context and surah not in (1, 9):
        opening = verses.get("verse_0")
        if not opening:
            raise PreparationError(f"Opening context is unavailable for S{surah}")
        rows.append(
            {
                "surah": surah,
                "ayah": 0,
                "role": "opening-context",
                "text": str(opening).removeprefix("\ufeff"),
            }
        )

    for ayah in range(ayah_start, ayah_end + 1):
        text = verses.get(f"verse_{ayah}")
        if not text:
            raise PreparationError(f"Missing S{surah}:{ayah} in {path}")
        rows.append(
            {
                "surah": surah,
                "ayah": ayah,
                "role": "in-scope",
                "text": str(text).removeprefix("\ufeff"),
            }
        )
    return rows


def load_morphology(surah: int, ayah_start: int, ayah_end: int) -> list[dict[str, Any]]:
    require_file(QAC_DATABASE, "QAC database")
    with closing(connect_readonly(QAC_DATABASE)) as connection:
        connection.row_factory = sqlite3.Row
        available = available_columns(connection, "qac_morphemes")
        mandatory = {
            "surah",
            "ayah",
            "word_index",
            "morpheme_index",
            "qac_ref",
            "surface_ar",
            "root_ar",
        }
        if not mandatory.issubset(available):
            raise PreparationError(
                f"qac_morphemes lacks columns: {sorted(mandatory - available)}"
            )
        desired = tuple(field for field in MORPHOLOGY_FIELDS if field != "root_norm")
        selections = [field if field in available else f"'' AS {field}" for field in desired]
        rows = list(
            connection.execute(
                f"""
                SELECT {', '.join(selections)}
                FROM qac_morphemes
                WHERE surah = ? AND ayah BETWEEN ? AND ?
                ORDER BY ayah, word_index, morpheme_index
                """,
                (surah, ayah_start, ayah_end),
            )
        )

    result: list[dict[str, Any]] = []
    for source in rows:
        row = {field: source[field] for field in desired}
        row["root_norm"] = source["root_ar"] or ""
        result.append(row)
    if not result:
        raise PreparationError("No positioned QAC morphology found for the passage")
    return result


def load_syntax(surah: int, ayah_start: int, ayah_end: int) -> list[dict[str, str]]:
    require_file(ATTACHMENTS_TSV, "attachment source")
    result: list[dict[str, str]] = []
    with ATTACHMENTS_TSV.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if int(row["sura"]) != surah:
                continue
            ayah = int(row["ayah"])
            if not ayah_start <= ayah <= ayah_end:
                continue
            head = row.get("head_unit_id") or f"q:{surah}:{ayah}:{row.get('head_wid', '')}"
            dependent = row.get("dep_unit_id") or f"q:{surah}:{ayah}:{row.get('dep_wid', '')}"
            surfaces = [value for value in (row.get("head_surface"), row.get("dep_surface")) if value]
            result.append(
                {
                    "edge_id": row["unit_id"],
                    "source_position": head,
                    "target_position": dependent,
                    "edge_type": row["relation"],
                    "direction": "head-to-dependent",
                    "confidence": row.get("confidence", ""),
                    "exact_surface_span": " | ".join(surfaces),
                    "evidence": row.get("evidence", ""),
                    "reason": row.get("reason", ""),
                }
            )
    return result


def load_lexical_branches(
    morphology: Iterable[Mapping[str, Any]],
) -> tuple[list[dict[str, str]], int]:
    require_file(LEXICAL_DATABASE, "V4 lexical database")
    passage_roots = {
        canonical_root(str(row.get("root_norm", "")))
        for row in morphology
        if canonical_root(str(row.get("root_norm", "")))
    }
    if not passage_roots:
        raise PreparationError("The passage has no rooted morphology for V4 selection")

    with closing(connect_readonly(LEXICAL_DATABASE)) as connection:
        connection.row_factory = sqlite3.Row
        required_branches = set(LEXICAL_FIELDS) | {"status", "contaminated"}
        required_roots = {"root_id", "root_norm", "source_root_norm"}
        missing_branches = required_branches - available_columns(connection, "branch_images")
        missing_roots = required_roots - available_columns(connection, "roots")
        if missing_branches or missing_roots:
            raise PreparationError(
                "V4 schema is incomplete: "
                f"branch_images={sorted(missing_branches)}, roots={sorted(missing_roots)}"
            )

        root_ids: list[str] = []
        for row in connection.execute("SELECT root_id, root_norm, source_root_norm FROM roots"):
            candidates = {
                canonical_root(str(row[field]))
                for field in ("root_norm", "source_root_norm")
                if row[field]
            }
            if candidates.intersection(passage_roots):
                root_ids.append(str(row["root_id"]))
        root_ids.sort()
        if not root_ids:
            raise PreparationError("No V4 roots match the passage morphology")

        source_rows: list[sqlite3.Row] = []
        excluded_contaminated = 0
        for start in range(0, len(root_ids), 800):
            chunk = root_ids[start : start + 800]
            placeholders = ",".join("?" for _ in chunk)
            source_rows.extend(
                connection.execute(
                    f"""
                    SELECT {', '.join(LEXICAL_FIELDS)}, contaminated
                    FROM branch_images AS b
                    WHERE b.root_id IN ({placeholders})
                      AND b.status = 'accepted'
                      AND b.contaminated = 'no'
                    """,
                    chunk,
                )
            )
            excluded_contaminated += int(
                connection.execute(
                    f"""
                    SELECT COUNT(*)
                    FROM branch_images AS b
                    WHERE b.root_id IN ({placeholders})
                      AND b.status = 'accepted'
                      AND COALESCE(b.contaminated, '') <> 'no'
                    """,
                    chunk,
                ).fetchone()[0]
            )

    records: list[dict[str, str]] = []
    for row in source_rows:
        if row["contaminated"] != "no":
            raise PreparationError(
                f"Contaminated branch escaped selection: {row['root_id']}:{row['branch_id']}"
            )
        records.append({field: str(row[field]) for field in LEXICAL_FIELDS})
    records.sort(key=lambda row: (row["root_id"], row["branch_id"]))
    if not records:
        raise PreparationError("No accepted uncontaminated V4 branches matched the passage")
    return records, excluded_contaminated


def write_tsv(
    path: Path,
    fields: Sequence[str],
    rows: Iterable[Mapping[str, Any]],
) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def prepare(args: argparse.Namespace) -> dict[str, Any]:
    if args.ayah_start < 1 or args.ayah_end < args.ayah_start:
        raise PreparationError("Invalid ayah interval")
    scaffold = args.primary_scaffold.resolve()
    require_file(scaffold, "primary scaffold")

    passage = load_passage(
        args.surah,
        args.ayah_start,
        args.ayah_end,
        args.include_opening_context,
    )
    morphology = load_morphology(args.surah, args.ayah_start, args.ayah_end)
    syntax = load_syntax(args.surah, args.ayah_start, args.ayah_end)
    lexical, excluded_contaminated = load_lexical_branches(morphology)

    run_root = args.run_root.resolve()
    prepare_run_root(run_root)
    inputs = run_root / "inputs"

    (inputs / "passage-arabic.txt").write_text(
        "".join(
            f"{row['surah']}:{row['ayah']}\t{row['role']}\t{row['text']}\n"
            for row in passage
        ),
        encoding="utf-8",
    )
    shutil.copyfile(scaffold, inputs / "primary-scaffold.md")
    write_tsv(inputs / "morphology.tsv", MORPHOLOGY_FIELDS, morphology)
    write_tsv(inputs / "syntax.tsv", SYNTAX_FIELDS, syntax)
    write_jsonl(inputs / "lexical-branches.jsonl", lexical)

    return {
        "run_root": str(run_root),
        "passage": f"S{args.surah}:{args.ayah_start}-{args.ayah_end}",
        "passage_positions": len(passage),
        "morphology_rows": len(morphology),
        "syntax_edges": len(syntax),
        "lexical_branches": len(lexical),
        "excluded_contaminated_branches": excluded_contaminated,
    }


def main() -> int:
    try:
        result = prepare(parse_args())
    except (PreparationError, OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(f"prepare_run: ERROR: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
