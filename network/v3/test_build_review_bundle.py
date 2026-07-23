import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from build_review_bundle import build_bundle


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
    )


class ReviewBundleTest(unittest.TestCase):
    def test_bundle_hydrates_branch_details_once(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            dense_path = tmp_path / "dense.jsonl"
            sparse_path = tmp_path / "sparse.jsonl"
            database = tmp_path / "furuq.sqlite"
            branch = {
                "node_id": "quranic:root_1:B012",
                "root": "ق و م",
                "branch_id": "B012",
                "ayahs": [6],
                "image_ar": "compressed",
            }
            write_jsonl(
                dense_path,
                [
                    {
                        "family_id": "F001",
                        "family_score": 0.5,
                        "label_hint": "tool",
                        "structural_type": "distributed",
                        "member_count": 2,
                        "ayahs": [6],
                        "core_branches": [branch],
                        "optional_branches": [],
                        "rare_branches": [],
                    }
                ],
            )
            write_jsonl(
                sparse_path,
                [
                    {
                        "path_family_id": "PF0001",
                        "family_score": 0.6,
                        "label_hint": "tool",
                        "member_count": 1,
                        "ayahs": [6],
                        "core_branches": [branch],
                        "optional_branches": [],
                        "construction_paths": [
                            {
                                "path_id": "P001",
                                "branches": [branch],
                                "tree_edges": [
                                    {"left": branch, "right": branch}
                                ],
                            }
                        ],
                    }
                ],
            )
            with sqlite3.connect(database) as connection:
                connection.execute(
                    """
                    CREATE TABLE branch_images (
                        root_norm TEXT,
                        branch_id TEXT,
                        branch_image_ar TEXT,
                        what_is_ar TEXT
                    )
                    """
                )
                connection.execute(
                    "INSERT INTO branch_images VALUES (?, ?, ?, ?)",
                    (
                        "ق و م",
                        "B012",
                        "آلة قائمة",
                        "البكرة أو أداتها عند البئر",
                    ),
                )

            bundle = build_bundle(
                surah_tag="s001",
                dense_path=dense_path,
                sparse_path=sparse_path,
                database=database,
            )

            self.assertEqual(
                bundle["branches"],
                [
                    {
                        "id": "ق و م:B012",
                        "ayahs": [6],
                        "branch_image_ar": "آلة قائمة",
                        "what_is_ar": "البكرة أو أداتها عند البئر",
                    }
                ],
            )
            self.assertEqual(
                bundle["surface_context"],
                {"ayahs": [], "root_occurrences": []},
            )
            self.assertEqual(
                bundle["dense_families"][0]["support_summary"],
                {
                    "member_count": 2,
                    "root_count": 0,
                    "ayah_count": 1,
                    "branch_count": None,
                    "candidate_count": 0,
                    "variant_candidate_count": 0,
                },
            )
            self.assertEqual(
                bundle["sparse_path_families"][0]["support_summary"],
                {
                    "member_count": 1,
                    "root_count": 0,
                    "ayah_count": 1,
                    "branch_count": None,
                    "path_count": 0,
                    "construction_path_count": 1,
                    "unique_edge_count": 1,
                    "repeated_edge_count": 0,
                    "reused_edges": [],
                },
            )
            self.assertEqual(
                bundle["dense_families"][0]["branches"]["core"],
                ["ق و م:B012"],
            )
            self.assertEqual(
                bundle["sparse_path_families"][0]["branches"]["core"],
                ["ق و م:B012"],
            )

    def test_bundle_adds_surface_context_from_qac_rows(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            dense_path = tmp_path / "dense.jsonl"
            sparse_path = tmp_path / "sparse.jsonl"
            database = tmp_path / "furuq.sqlite"
            qac_path = tmp_path / "qac.tsv"
            branch = {
                "node_id": "quranic:root_1:B012",
                "root": "ق و م",
                "branch_id": "B012",
                "ayahs": [6],
                "image_ar": "compressed",
            }
            write_jsonl(
                dense_path,
                [
                    {
                        "family_id": "F001",
                        "family_score": 0.5,
                        "label_hint": "tool",
                        "structural_type": "distributed",
                        "member_count": 2,
                        "ayahs": [6],
                        "core_branches": [branch],
                        "optional_branches": [],
                        "rare_branches": [],
                    }
                ],
            )
            write_jsonl(
                sparse_path,
                [
                    {
                        "path_family_id": "PF0001",
                        "family_score": 0.6,
                        "label_hint": "tool",
                        "member_count": 1,
                        "ayahs": [6],
                        "core_branches": [branch],
                        "optional_branches": [],
                        "construction_paths": [],
                    }
                ],
            )
            with sqlite3.connect(database) as connection:
                connection.execute(
                    """
                    CREATE TABLE branch_images (
                        root_norm TEXT,
                        branch_id TEXT,
                        branch_image_ar TEXT,
                        what_is_ar TEXT
                    )
                    """
                )
                connection.execute(
                    "INSERT INTO branch_images VALUES (?, ?, ?, ?)",
                    (
                        "ق و م",
                        "B012",
                        "آلة قائمة",
                        "البكرة أو أداتها عند البئر",
                    ),
                )
            qac_path.write_text(
                "\t".join(
                    [
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
                    ]
                )
                + "\n"
                + "\t".join(
                    [
                        "ق و م",
                        "1",
                        "6",
                        "1:6",
                        "1",
                        "1:6:3:2",
                        "3",
                        "مُسْتَقِيمَ",
                        "مُّسْتَقِيم",
                        "ADJ",
                        "X",
                        "ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ",
                        "اهدنا الصرط المستقيم",
                        "ه د ي;ص ر ط;ق و م",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            bundle = build_bundle(
                surah_tag="s001",
                dense_path=dense_path,
                sparse_path=sparse_path,
                database=database,
                qac_root_ayah_path=qac_path,
            )

            self.assertEqual(
                bundle["surface_context"]["ayahs"],
                [
                    {
                        "ayah": 6,
                        "ayah_ref": "1:6",
                        "text_ar": "ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ",
                        "text_norm_ar": "اهدنا الصرط المستقيم",
                        "root_sequence": ["ه د ي", "ص ر ط", "ق و م"],
                    }
                ],
            )
            self.assertEqual(
                bundle["surface_context"]["root_occurrences"],
                [
                    {
                        "root": "ق و م",
                        "ayah": 6,
                        "ayah_ref": "1:6",
                        "occurrence_count": 1,
                        "qac_refs": ["1:6:3:2"],
                        "word_indices": [3],
                        "surfaces_ar": ["مُسْتَقِيمَ"],
                        "lemmas_ar": ["مُّسْتَقِيم"],
                        "pos_tags": ["ADJ"],
                        "measures": ["X"],
                    }
                ],
            )


if __name__ == "__main__":
    unittest.main()
