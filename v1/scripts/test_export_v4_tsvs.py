#!/usr/bin/env python3
"""Contract tests for the grep-friendly V4 and QAC TSV exports."""

from __future__ import annotations

import csv
import hashlib
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import export_v4_tsvs as exporter  # noqa: E402


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


class ExportContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp_dir = tempfile.TemporaryDirectory()
        temp_path = Path(cls.temp_dir.name)
        cls.fresh_branches_path = temp_path / "v4_branches.tsv"
        cls.fresh_root_ayah_path = temp_path / "qac_root_ayah.tsv"

        with mock.patch.object(exporter, "BRANCHES_TSV", cls.fresh_branches_path):
            exporter.export_branches()
        with mock.patch.object(exporter, "ROOT_AYAH_TSV", cls.fresh_root_ayah_path):
            exporter.export_root_ayahs()

        cls.branch_header, cls.branches = read_tsv(cls.fresh_branches_path)
        cls.root_ayah_header, cls.root_ayahs = read_tsv(cls.fresh_root_ayah_path)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp_dir.cleanup()

    def test_headers_are_fixed(self) -> None:
        self.assertEqual(list(exporter.BRANCH_COLUMNS), self.branch_header)
        self.assertEqual(list(exporter.ROOT_AYAH_COLUMNS), self.root_ayah_header)

    def test_checked_artifacts_match_fresh_exports(self) -> None:
        self.assertEqual(sha256(self.fresh_branches_path), sha256(exporter.BRANCHES_TSV))
        self.assertEqual(sha256(self.fresh_root_ayah_path), sha256(exporter.ROOT_AYAH_TSV))

    def test_branch_export_matches_all_clean_source_values(self) -> None:
        with sqlite3.connect(exporter.V4_DB) as connection:
            expected = list(
                connection.execute(
                    """
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
                )
            )
        self.assertEqual(len(expected), len(self.branches))
        for index, (source, exported) in enumerate(zip(expected, self.branches)):
            actual = tuple(exported[column] for column in exporter.BRANCH_COLUMNS)
            wanted = tuple(exporter.clean_cell(value) for value in source)
            self.assertEqual(wanted, actual, f"branch row {index + 2}")

    def test_root_ayah_export_matches_all_qac_keys(self) -> None:
        actual = {
            (row["root_norm"], int(row["surah"]), int(row["ayah"]))
            for row in self.root_ayahs
        }
        self.assertEqual(len(actual), len(self.root_ayahs))

        with sqlite3.connect(exporter.QAC_DB) as connection:
            expected = set(
                connection.execute(
                    """
                    SELECT DISTINCT root_ar, surah, ayah
                    FROM qac_morphemes
                    WHERE root_ar <> ''
                    """
                )
            )
        self.assertEqual(expected, actual)

    def test_occurrence_fields_remain_aligned(self) -> None:
        with sqlite3.connect(exporter.QAC_DB) as connection:
            connection.row_factory = sqlite3.Row
            source_rows = list(
                connection.execute(
                    """
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
                )
            )

        by_root_ayah: dict[tuple[str, int, int], list[sqlite3.Row]] = {}
        roots_by_ayah: dict[tuple[int, int], list[str]] = {}
        for source in source_rows:
            by_root_ayah.setdefault(
                (source["root_ar"], source["surah"], source["ayah"]), []
            ).append(source)
            roots_by_ayah.setdefault((source["surah"], source["ayah"]), []).append(
                source["root_ar"]
            )

        for row in self.root_ayahs:
            location = (int(row["surah"]), int(row["ayah"]))
            occurrences = by_root_ayah[(row["root_norm"], *location)]
            label = f"{row['ayah_ref']} {row['root_norm']}"

            self.assertEqual(int(row["occurrence_count"]), len(occurrences), label)
            self.assertEqual(
                row["qac_refs"],
                ";".join(source["qac_ref"] for source in occurrences),
                label,
            )
            self.assertEqual(
                row["word_indices"],
                ";".join(str(source["word_index"]) for source in occurrences),
                label,
            )
            self.assertEqual(
                row["surfaces_ar"],
                ";".join(source["surface_ar"] for source in occurrences),
                label,
            )
            self.assertEqual(
                row["lemmas_ar"],
                ";".join(source["lemma_ar"] for source in occurrences),
                label,
            )
            self.assertEqual(
                row["pos_tags"],
                ";".join(source["pos"] for source in occurrences),
                label,
            )
            self.assertEqual(
                row["measures"],
                ";".join(source["measure"] for source in occurrences),
                label,
            )
            self.assertEqual(
                row["ayah_root_sequence"],
                ";".join(roots_by_ayah[location]),
                label,
            )

    def test_ayah_text_has_no_bom_and_normalization_is_reproducible(self) -> None:
        ayah_texts = exporter.load_ayah_texts()
        for row in self.root_ayahs:
            location = (int(row["surah"]), int(row["ayah"]))
            self.assertEqual(row["ayah_ref"], f"{location[0]}:{location[1]}")
            self.assertEqual(row["ayah_text_ar"], ayah_texts[location])
            self.assertNotIn("\ufeff", row["ayah_text_ar"])
            self.assertNotIn("\ufeff", row["ayah_text_norm_ar"])
            self.assertEqual(
                exporter.normalize_arabic(row["ayah_text_ar"]),
                row["ayah_text_norm_ar"],
            )
if __name__ == "__main__":
    unittest.main()
