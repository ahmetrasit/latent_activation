import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import workflow as w


def sample_draft(packet, reader_id="test_reader"):
    occurrences, branches = w.evidence_index(packet)
    focus_id = next(key for key, value in occurrences.items() if value["source_ref"] == packet["focus_ref"])
    focus_root = occurrences[focus_id]["root"]
    focus_key = next(key for root, key in branches if root == focus_root)
    context_id = next(key for key, value in occurrences.items() if value["source_ref"] != packet["focus_ref"] and any(root == value["root"] for root, _ in branches))
    context_root = occurrences[context_id]["root"]
    context_key = next(key for root, key in branches if root == context_root)
    trace = lambda occurrence, branch: {"occurrence_id": occurrence, "branch_key": branch, "role": "Test fixture evidence role."}
    return {
        "protocol": w.READER_PROTOCOL, "reader_id": reader_id, "focus_ref": packet["focus_ref"], "trace_kind": "reconstructed",
        "baseline_models": [{"model_id": "baseline", "confidence": "medium", "focus_anchor": "Test fixture anchor.",
            "mechanism": "Test fixture mechanism.", "activation_trace": [trace(focus_id, focus_key)],
            "changed_reading": {"before": "Before fixture.", "after": "After fixture."}}],
        "context_deltas": [{"model_id": "delta", "status": "new", "confidence": "medium", "mechanism": "Test fixture context mechanism.",
            "activation_trace": [trace(focus_id, focus_key), trace(context_id, context_key)],
            "structural_cues": ["Test fixture structural cue."], "reader_inference": "Test fixture inference and alternative.",
            "changed_reading": {"before": "Before context fixture.", "after": "After context fixture."}}],
        "surprising_valid_outliers": [],
        "summary": {"strongest_changes": [], "what_was_special": "Test fixture only; not a model reading.", "remaining_uncertainties": []},
    }


class WorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = w.build_source("83:1", ["83:1", "83:2", "83:3"])

    def setUp(self):
        self.packet = w.project_packet(self.source)
        self.draft = sample_draft(self.packet)

    def test_repaired_input_and_compact_context_default(self):
        inventory = self.packet["focus_branch_inventories"][0]
        self.assertEqual(inventory["targets"][0]["mapped_root_id"], "root_000940")
        self.assertEqual(len(inventory["targets"][0]["branches"]), 10)
        for inv in self.packet["context_root_cues"]:
            for target in inv["targets"]:
                for branch in target["branches"]:
                    self.assertNotIn("branch_key", branch)
                    self.assertTrue(all("scope_ar" not in row for row in branch.get("variants", [branch])))

    def test_context_scope_ablation_preserves_all_branch_choices(self):
        rich = w.project_packet(self.source, context_scopes=True)
        self.assertEqual(set(w.evidence_index(self.packet)[1]), set(w.evidence_index(rich)[1]))
        self.assertEqual(self.packet["focus_branch_inventories"], rich["focus_branch_inventories"])
        for inv in rich["context_root_cues"]:
            for target in inv["targets"]:
                for branch in target["branches"]:
                    self.assertTrue(all("scope_ar" in row for row in branch.get("variants", [branch])))
        self.assertEqual(w.compile_response(self.draft, self.packet, "test_reader"), w.compile_response(self.draft, rich, "test_reader"))

    def test_compiler_preserves_semantics_and_derives_metadata(self):
        before = copy.deepcopy(self.draft)
        result = w.compile_response(self.draft, self.packet, "test_reader")
        self.assertEqual(self.draft, before)
        self.assertEqual(result["summary"], self.draft["summary"])
        for section in w.SECTIONS:
            for raw, compiled in zip(self.draft[section], result[section]):
                for key, value in raw.items():
                    if key != "activation_trace":
                        self.assertEqual(value, compiled[key])
        delta = result["context_deltas"][0]
        self.assertEqual(delta["trigger_roots"], list(dict.fromkeys(c["root"] for c in delta["activation_trace"] if c["source_ref"] != "83:1")))
        w.validator.validate_response(w.validation_view(self.packet), result)

    def test_full_occurrence_group_derived(self):
        self.packet["focus_ayah"]["root_occurrences"][0]["word_indices"] = ["2", "5"]
        result = w.compile_response(self.draft, self.packet, "test_reader")
        self.assertEqual(result["baseline_models"][0]["activation_trace"][0]["source_word_indices"], ["2", "5"])

    def test_unknown_and_remote_occurrences_rejected(self):
        for key in ("29:61/r01", "83:99/r01"):
            self.draft["context_deltas"][0]["activation_trace"][1]["occurrence_id"] = key
            with self.assertRaisesRegex(ValueError, "unknown or out-of-window"):
                w.compile_response(self.draft, self.packet, "test_reader")

    def test_wrong_root_branch_pair_rejected(self):
        focus_trace = self.draft["baseline_models"][0]["activation_trace"][0]
        context_trace = self.draft["context_deltas"][0]["activation_trace"][1]
        focus_trace["branch_key"] = context_trace["branch_key"]
        with self.assertRaisesRegex(ValueError, "not mapped"):
            w.compile_response(self.draft, self.packet, "test_reader")

    def test_baseline_cannot_borrow_context(self):
        self.draft["baseline_models"][0]["activation_trace"] = [self.draft["context_deltas"][0]["activation_trace"][1]]
        with self.assertRaises(ValueError):
            w.compile_response(self.draft, self.packet, "test_reader")

    def test_delta_requires_branch_backed_context(self):
        self.draft["context_deltas"][0]["activation_trace"].pop()
        with self.assertRaises(ValueError):
            w.compile_response(self.draft, self.packet, "test_reader")

    def test_reader_cannot_supply_redundant_metadata(self):
        self.draft["context_deltas"][0]["trigger_roots"] = ["ط ف ف"]
        with self.assertRaisesRegex(ValueError, "derived trigger"):
            w.compile_response(self.draft, self.packet, "test_reader")

    def test_wrong_profile_assignment_and_extra_fields_rejected(self):
        with self.assertRaises(ValueError):
            w.compile_response(self.draft, self.packet, "different_reader")
        self.draft["baseline_models"][0]["invented_field"] = "no"
        with self.assertRaises(ValueError):
            w.compile_response(self.draft, self.packet, "test_reader")

    def test_duplicate_finding_ids_rejected(self):
        self.draft["context_deltas"][0]["model_id"] = "baseline"
        with self.assertRaises(ValueError):
            w.compile_response(self.draft, self.packet, "test_reader")

    def test_variants_keep_paired_scopes_and_optional_english(self):
        branch = copy.deepcopy(self.source["branches"]["ط ف ف"][0])
        variant = copy.deepcopy(branch["variants"][0])
        variant.update(image_ar="SECOND IMAGE", scope_ar="SECOND SCOPE", image_en="second", scope_en="second scope")
        branch["variants"].append(variant)
        projected = w.branch_projection(branch, english=True)
        self.assertEqual(projected["variants"][1]["scope_ar"], "SECOND SCOPE")
        self.assertEqual(projected["variants"][1]["branch_image_en"], "second")
        arabic = w.branch_projection(branch, english=False)
        self.assertNotIn("scope_en", arabic["variants"][1])
        self.assertEqual(len(arabic["variants"]), 2)

    def test_split_root_targets_remain_citable(self):
        source = copy.deepcopy(self.source)
        branch = copy.deepcopy(source["branches"]["ط ف ف"][0])
        branch["mapped_root_id"] = "root_999999"
        branch["mapped_root_norm"] = "ط ف ف"
        source["branches"]["ط ف ف"].append(branch)
        packet = w.project_packet(source)
        self.draft["baseline_models"][0]["activation_trace"][0]["branch_key"] = "root_999999/" + branch["branch_id"]
        result = w.compile_response(self.draft, packet, "test_reader")
        self.assertEqual(result["baseline_models"][0]["activation_trace"][0]["mapped_root_id"], "root_999999")

    def test_missing_focus_inventory_stops_preparation(self):
        source = copy.deepcopy(self.source)
        source["branches"]["ط ف ف"] = []
        with self.assertRaisesRegex(ValueError, "no branch-backed baseline"):
            w.project_packet(source)

    def test_qac_annotation_gap_preserves_text_and_empty_baseline(self):
        source = copy.deepcopy(self.source)
        source["focus_ayah"].update(root_sequence=[], root_occurrences=[], rootless=True, rootless_reason="QAC annotation gap")
        packet = w.project_packet(source)
        self.draft["rootless_focus"] = True
        self.draft["baseline_models"][0]["activation_trace"] = []
        self.draft["context_deltas"] = []
        result = w.compile_response(self.draft, packet, "test_reader")
        self.assertTrue(result["rootless_focus"])
        self.assertEqual(packet["focus_ayah"]["text_ar"], self.source["focus_ayah"]["text_ar"])

    def test_v1_discovery_sections_and_ledger_schema_are_preserved(self):
        base = (ROOT / "prompts/focus_trace_hermetic.md").read_text()
        active = (ROOT / "prompts/reader.md").read_text()
        for heading, following in [("## Reader Posture", "## Core Task"), ("## Core Task", "## Required Evidence Discipline")]:
            section = base.split(heading, 1)[1].split(following, 1)[0].strip()
            self.assertIn(section, active)
        self.assertEqual((ROOT / "schemas/focus-trace-response.schema.json").read_bytes(), (ROOT.parent / "focus_trace/schemas/focus-trace-response.schema.json").read_bytes())
        self.assertNotIn("Revisit and integrate", w.render_prompt("gpt-5.6-luna", "max", False))
        self.assertIn("Revisit and integrate", w.render_prompt("gpt-5.6-luna", "max", True))

    def test_sealed_job_compile_roundtrip_and_tamper_detection(self):
        with tempfile.TemporaryDirectory(dir="/private/tmp") as temporary:
            job_dir = Path(temporary) / "job"
            job = w.prepare(job_dir, "83:1", ["83:1", "83:2", "83:3"], model="gpt-5.6-luna")
            self.assertFalse(job["options"]["integration"])
            self.assertEqual(job["options"]["prompt_revision"], "v1-discovery")
            _, packet = w.load_job(job_dir)
            (job_dir / "reader.response.json").write_bytes(w.encode(sample_draft(packet, job["reader_id"])))
            receipt = w.compile_job(job_dir)
            self.assertFalse(receipt["model_execution_verified"])
            w.validate_job(job_dir)
            self.assertEqual(receipt, w.compile_job(job_dir))
            stored = (job_dir / "response.json").read_bytes()
            changed = w.read(job_dir / "response.json")
            changed["summary"]["what_was_special"] = "Unrecorded edit."
            (job_dir / "response.json").write_bytes(w.encode(changed))
            with self.assertRaisesRegex(ValueError, "compiled ledger changed"):
                w.validate_job(job_dir)
            with self.assertRaisesRegex(ValueError, "output already exists"):
                w.compile_job(job_dir)
            (job_dir / "response.json").write_bytes(stored)
            packet["focus_branch_inventories"][0]["targets"][0]["branches"].pop()
            (job_dir / "packet.json").write_bytes(w.encode(packet))
            with self.assertRaisesRegex(ValueError, "frozen input changed"):
                w.load_job(job_dir)

    def test_initial_jobs_remain_valid_and_prompt_change_is_scoped(self):
        for scope in (False, True):
            old = w.render_prompt("gpt-5.6-sol", "max", True, context_scopes=scope,
                                  prompt_revision="initial")
            new = w.render_prompt("gpt-5.6-sol", "max", True, context_scopes=scope)
            sentence = "\nDo not collapse a split root to the dominant target only."
            self.assertEqual(new.replace(sentence, ""), old)
        for run in ("compare-20260906-sol-max", "rerun-20260906-compact-sol-max"):
            job_dir = ROOT / "runs" / run / "29_38"
            w.validate_job(job_dir)

    def test_source_projection_detects_pruning_even_with_updated_packet_hash(self):
        with tempfile.TemporaryDirectory(dir="/private/tmp") as temporary:
            path = Path(temporary) / "job"
            job = w.prepare(path, "83:1", ["83:1", "83:2", "83:3"])
            packet = w.read(path / "packet.json")
            packet["context_root_cues"].pop()
            (path / "packet.json").write_bytes(w.encode(packet))
            job["inputs"]["packet.json"] = w.digest((path / "packet.json").read_bytes())
            (path / "job.json").write_bytes(w.encode(job))
            with self.assertRaisesRegex(ValueError, "full source projection"):
                w.load_job(path)


if __name__ == "__main__":
    unittest.main()
