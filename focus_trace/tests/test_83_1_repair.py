import copy
import json
import sys
import unittest
import sqlite3
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_focus_trace_packet as builder
from repair_83_1_input import repaired_packet
from build_alignment_repairs import accepted_target, checked_database


class ReviewedRepairTests(unittest.TestCase):
    def setUp(self):
        self.repair = json.loads(builder.ROOT_MAPPING_REPAIRS.read_text())["repairs"][0]
        self.record = {"qac_root": "ط ف ف", **self.repair["expected_mapping"], "targets": []}

    def test_missing_mapping_recovers_exact_target(self):
        mappings = {"ط ف ف": self.record}
        builder.apply_root_mapping_repairs(mappings)
        self.assertEqual(self.record["targets"], [self.repair["target"]])

    def test_does_not_rewrite_existing_split_mapping(self):
        self.record["targets"] = [{"furuq_root_id": "root_000940"}, {"furuq_root_id": "root_000999"}]
        before = copy.deepcopy(self.record)
        builder.apply_root_mapping_repairs({"ط ف ف": self.record})
        self.assertEqual(before, self.record)

    def test_changed_or_ambiguous_occurrence_count_fails(self):
        self.record["qac_total_occurrences"] = 2
        with self.assertRaisesRegex(ValueError, "precondition changed"):
            builder.apply_root_mapping_repairs({"ط ف ف": self.record})

    def test_other_unmapped_roots_are_untouched(self):
        mappings = {"غ م ز": copy.deepcopy(self.record)}
        before = copy.deepcopy(mappings)
        builder.apply_root_mapping_repairs(mappings)
        self.assertEqual(before, mappings)

    def test_wrong_ayah_or_inflection_is_not_generalized(self):
        mappings = {"ط ف ف": self.record}
        builder.apply_root_mapping_repairs(mappings)
        occurrence = {"root": "ط ف ف", **self.repair["packet_occurrence"]}
        for ref, surface in [("83:2", occurrence["surfaces_ar"]), ("83:1", ["مطفف"])]:
            with self.assertRaisesRegex(ValueError, "QAC occurrence changed"):
                builder.validate_repair_occurrences([
                    {"ref": ref, "root_occurrences": [{**occurrence, "surfaces_ar": surface}]},
                ], mappings)

    def test_real_packet_retains_unrelated_evidence_and_is_idempotent(self):
        original = json.loads((ROOT / "repairs/83_1/original.packet.json").read_text())
        repaired = repaired_packet(original)
        for key in ["focus_ayah", "context_ayat", "context_root_cues", "window", "context_order"]:
            self.assertEqual(original[key], repaired[key])
        branches = repaired["focus_branch_inventories"][0]["branches"]
        self.assertEqual(len(branches), 10)
        self.assertEqual({row["mapped_root_id"] for row in branches}, {"root_000940"})
        self.assertTrue(all(row["scope_ar"] for row in branches))
        self.assertEqual(repaired, repaired_packet(repaired))

    def test_generated_record_uses_accepted_bridge_not_surface_guess(self):
        self.assertEqual(self.repair["target"]["furuq_resolution"], "accepted_masaq_qac_edges_then_exact_source_root_norm")
        edge = self.repair["evidence"]["accepted_edges"][0]
        self.assertEqual(edge["qac_morpheme_ref"], "83:1:2:3")
        self.assertEqual(edge["masaq_segment_ref"], "83:1:3")

    def test_bridge_checksum_mismatch_fails_before_reading_database(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary)
            (path / "bridge.gz").write_bytes(b"changed artifact")
            (path / "CHECKSUMS.sha256").write_text("0" * 64 + "  bridge.gz\n")
            with self.assertRaisesRegex(ValueError, "checksum mismatch"):
                checked_database(path, "bridge.gz")

    def test_accepted_edges_reject_wrong_root_and_prefix_carrier(self):
        bridge = sqlite3.connect(":memory:")
        lexical = sqlite3.connect(":memory:")
        bridge.row_factory = lexical.row_factory = sqlite3.Row
        bridge.executescript('''
            CREATE TABLE accepted_masaq_qac_edges(masaq_segment_ref, qac_morpheme_ref, target_order);
            CREATE TABLE masaq_segments(masaq_segment_ref, root_ar, stem_ar, tag, role);
            CREATE TABLE qac_morphemes(qac_morpheme_ref, surface_ar, morpheme_role);
            INSERT INTO accepted_masaq_qac_edges VALUES ('83:1:3','83:1:2:3',2);
            INSERT INTO masaq_segments VALUES ('83:1:3','ط ف ف','مطفف','N','N');
            INSERT INTO qac_morphemes VALUES ('83:1:2:3','مُطَفِّفِينَ','STEM');
        ''')
        lexical.executescript('''CREATE TABLE roots(root_id, root_norm, source_root_norm);
            INSERT INTO roots VALUES ('root_000940','ط ف ف','ط ف ف');''')
        self.assertEqual(accepted_target(bridge, lexical, '83:1:2:3', 'ط ف ف')[0]['root_id'], 'root_000940')
        with self.assertRaises(ValueError):
            accepted_target(bridge, lexical, '83:1:2:3', 'و ل ي')
        bridge.execute("UPDATE qac_morphemes SET morpheme_role='PREFIX'")
        with self.assertRaises(ValueError):
            accepted_target(bridge, lexical, '83:1:2:3', 'ط ف ف')
        bridge.close()
        lexical.close()


if __name__ == "__main__":
    unittest.main()
