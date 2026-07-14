#!/usr/bin/env python3
"""Export grep-friendly V4 branch and QAC root-by-ayah TSV resources."""

from __future__ import annotations

import csv
import json
import os
import sqlite3
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Iterable, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
RESOURCES_DIR = REPO_ROOT / "resources"
V4_DB = RESOURCES_DIR / "furuq_v4.sqlite"
QAC_DB = RESOURCES_DIR / "qac.sqlite"
QURAN_DIR = RESOURCES_DIR / "quran"
BRANCHES_TSV = RESOURCES_DIR / "v4_branches.tsv"
ROOT_AYAH_TSV = RESOURCES_DIR / "qac_root_ayah.tsv"

BRANCH_COLUMNS = (
    "root_id",
    "root_norm",
    "source_root_norm",
    "branch_id",
    "status",
    "branch_image_ar",
    "what_is_ar",
    "source_phrase_ar",
)

ROOT_AYAH_COLUMNS = (
    "root_norm",
    "surah",
    "ayah",
    "ayah_ref",
    "occurrence_count",
    "qac_refs",
    "word_indices",
    "surfaces_ar",
    "lemmas_ar",
    "pos_tags",
    "measures",
    "ayah_text_ar",
    "ayah_text_norm_ar",
    "ayah_root_sequence",
)

ALEF_TRANSLATION = str.maketrans(
    {
        "آ": "ا",
        "أ": "ا",
        "إ": "ا",
        "ٱ": "ا",
        "ٲ": "ا",
        "ٳ": "ا",
        "ى": "ي",
    }
)

QURAN_ANNOTATION_RANGES = (
    (0x0610, 0x061A),
    (0x064B, 0x065F),
    (0x0670, 0x0670),
    (0x06D6, 0x06ED),
    (0x08D3, 0x08FF),
)


def clean_cell(value: object) -> str:
    """Keep each record on one physical TSV line."""
    if value is None:
        return ""
    return " ".join(str(value).replace("\t", " ").splitlines())


def normalize_arabic(text: str) -> str:
    """Create a search form while preserving the sacred form separately."""
    text = unicodedata.normalize("NFKC", text.replace("\ufeff", "")).translate(
        ALEF_TRANSLATION
    )
    text = text.replace("ـ", "")
    text = "".join(
        char
        for char in text
        if unicodedata.category(char) != "Mn"
        and not any(start <= ord(char) <= end for start, end in QURAN_ANNOTATION_RANGES)
    )
    return " ".join(text.split())


def write_tsv(path: Path, columns: Sequence[str], rows: Iterable[Sequence[object]]) -> int:
    temp_path = path.with_suffix(path.suffix + ".tmp")
    count = 0
    try:
        with temp_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
            writer.writerow(columns)
            for row in rows:
                writer.writerow(clean_cell(value) for value in row)
                count += 1
        os.replace(temp_path, path)
    finally:
        temp_path.unlink(missing_ok=True)
    return count


def export_branches() -> int:
    query = """
        SELECT
            b.root_id,
            b.root_norm,
            r.source_root_norm,
            b.branch_id,
            b.status,
            b.branch_image_ar,
            b.what_is_ar,
            b.source_phrase_ar
        FROM branch_images AS b
        JOIN roots AS r ON r.root_id = b.root_id
        WHERE b.contaminated = 'no'
        ORDER BY b.root_id, b.branch_id
    """
    with sqlite3.connect(V4_DB) as connection:
        rows = connection.execute(query)
        return write_tsv(BRANCHES_TSV, BRANCH_COLUMNS, rows)


def load_ayah_texts() -> dict[tuple[int, int], str]:
    texts: dict[tuple[int, int], str] = {}
    for path in sorted(QURAN_DIR.glob("surah_*.json")):
        with path.open(encoding="utf-8") as handle:
            document = json.load(handle)
        surah = int(document["index"])
        for key, text in document["verse"].items():
            if key == "verse_0":
                continue
            ayah = int(key.removeprefix("verse_"))
            text = text.removeprefix("\ufeff")
            location = (surah, ayah)
            if location in texts:
                raise ValueError(f"Duplicate Quran ayah: {surah}:{ayah}")
            texts[location] = text
    return texts


def export_root_ayahs() -> int:
    ayah_texts = load_ayah_texts()
    query = """
        SELECT
            qac_ref,
            surah,
            ayah,
            word_index,
            morpheme_index,
            surface_ar,
            lemma_ar,
            root_ar,
            pos,
            measure
        FROM qac_morphemes
        WHERE root_ar <> ''
        ORDER BY surah, ayah, word_index, morpheme_index
    """

    grouped: dict[tuple[int, int], list[sqlite3.Row]] = defaultdict(list)
    with sqlite3.connect(QAC_DB) as connection:
        connection.row_factory = sqlite3.Row
        for row in connection.execute(query):
            grouped[(row["surah"], row["ayah"])].append(row)

    def rows() -> Iterable[Sequence[object]]:
        for (surah, ayah), morphemes in sorted(grouped.items()):
            try:
                ayah_text = ayah_texts[(surah, ayah)]
            except KeyError as error:
                raise ValueError(f"Missing Quran text for QAC ayah {surah}:{ayah}") from error

            root_sequence = ";".join(row["root_ar"] for row in morphemes)
            by_root: dict[str, list[sqlite3.Row]] = defaultdict(list)
            for row in morphemes:
                by_root[row["root_ar"]].append(row)

            for root_norm in sorted(by_root):
                occurrences = by_root[root_norm]
                yield (
                    root_norm,
                    surah,
                    ayah,
                    f"{surah}:{ayah}",
                    len(occurrences),
                    ";".join(row["qac_ref"] for row in occurrences),
                    ";".join(str(row["word_index"]) for row in occurrences),
                    ";".join(row["surface_ar"] for row in occurrences),
                    ";".join(row["lemma_ar"] for row in occurrences),
                    ";".join(row["pos"] for row in occurrences),
                    ";".join(row["measure"] for row in occurrences),
                    ayah_text,
                    normalize_arabic(ayah_text),
                    root_sequence,
                )

    return write_tsv(ROOT_AYAH_TSV, ROOT_AYAH_COLUMNS, rows())


def main() -> None:
    branch_count = export_branches()
    root_ayah_count = export_root_ayahs()
    print(f"Wrote {branch_count} rows to {BRANCHES_TSV.relative_to(REPO_ROOT)}")
    print(f"Wrote {root_ayah_count} rows to {ROOT_AYAH_TSV.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
