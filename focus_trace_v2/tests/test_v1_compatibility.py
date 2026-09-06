"""V1 contract restoration. Synthetic fixtures and read-only historical checks only."""

import copy
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from focus_trace_v2 import workflow as w
from test_workflow import fixture_packet
from test_inline_reader import runner


def packet_fixture():
    raw = json.dumps(fixture_packet(), ensure_ascii=False)
    for old, new in (("root_focus", "root_000001"), ("root_shared", "root_000002"), ("root_missing", "root_000003")):
        raw = raw.replace(old, new)
    return json.loads(raw)


def trace(ref="2:1", root="أ ث ر", mapped="root_000001"):
    return {"source_ref": ref, "root": root, "source_word_indices": ["1"],
            "mapped_root_id": mapped, "branch_id": "B001", "role": "Synthetic branch contribution."}


def response_fixture(job):
    return {"protocol": w.RESPONSE_PROTOCOL, "reader_id": job["reader_id"], "focus_ref": job["focus_ref"],
            "trace_kind": "reconstructed", "baseline_models": [{"model_id": "B1", "confidence": "strong",
                "focus_anchor": "A prose description of the focal construction, as v1 permits.",
                "mechanism": "Synthetic baseline mechanism.", "activation_trace": [trace()],
                "changed_reading": {"before": "Synthetic initial reading.", "after": "Synthetic baseline change."}}],
            "context_deltas": [{"model_id": "D1", "status": "new", "confidence": "exploratory",
                "trigger_roots": ["ط ر ق"], "mechanism": "Synthetic context mechanism.",
                "activation_trace": [trace("2:2", "ط ر ق", "root_000002")],
                "structural_cues": ["A free-text structural cue, as v1 permits."],
                "reader_inference": "Synthetic supplied/inferred distinction.",
                "changed_reading": {"before": "Synthetic baseline.", "after": "Synthetic contextual change."}}],
            "surprising_valid_outliers": [{"outlier_id": "O1", "confidence": "exploratory",
                "containment": "Synthetic, anchored, exploratory example only.", "focus_anchor": "Focal root.",
                "activation_trace": [trace(mapped="root_000002")],
                "changed_reading": {"before": "Synthetic baseline.", "after": "Synthetic unusual change."}}],
            "summary": {"strongest_changes": ["Synthetic change."], "what_was_special": "Synthetic discovery.",
                        "remaining_uncertainties": ["Not model output."]}}


class V1CompatibilityTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="hft-v1-compat-")
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.directory = self.root / "runs/fixture/2_1"
        self.source = packet_fixture()
        self.job = w.write_job(self.directory, self.source, [])
        self.packet_name, self.schema_name = w.reader_filenames(self.job)
        self.packet = w.read_json(self.directory / self.packet_name)
        self.schema = w.read_json(self.directory / self.schema_name)
        self.response = response_fixture(self.job)

    def validate(self):
        w.validate_response(self.response, self.packet, self.job, self.schema)

    def test_prompt_schema_and_paths_match_original_v1_exactly(self):
        self.assertEqual((self.directory / "prompt.md").read_bytes(), w.V1_PROMPT.read_bytes())
        self.assertEqual((self.directory / self.schema_name).read_bytes(), w.V1_SCHEMA.read_bytes())
        self.assertEqual(self.packet_name, "focus_trace_packet.json")
        self.assertEqual(self.schema_name, "focus_trace/schemas/focus-trace-response.schema.json")
        self.assertFalse((self.directory / "packet.json").exists())
        self.assertEqual(w.load_job(self.directory, require_response=False)[1], self.packet)

    def test_layout_is_focus_first_and_root_led_with_all_variants(self):
        self.assertEqual([item["root"] for item in self.packet["focus_branch_inventories"]], ["أ ث ر"])
        self.assertEqual([item["root"] for item in self.packet["context_root_cues"]], ["ط ر ق", "غ ي ب"])
        self.assertNotIn("branch_inventory", self.packet)
        self.assertEqual(self.packet["focus_branch_inventories"][0]["source_phrases"], [{"source_phrase_ar": "أَثَرٌ"}])
        projected = w.packet_index(self.packet)[2]
        original = w.packet_index(self.source)[2]
        self.assertEqual(set(projected), set(original))
        for key, variant in original.items():
            self.assertEqual(projected[key], {field: variant[field] for field in ("variant_id", *w.LINGUISTIC_VARIANT_FIELDS)})
        self.assertEqual([target["mapped_root_id"] for target in self.packet["focus_branch_inventories"][0]["targets"]],
                         ["root_000001", "root_000002", "root_000003"])

    def test_packet_keeps_linguistic_gaps_but_not_run_audits(self):
        def keys(value):
            if isinstance(value, dict):
                for key, child in value.items():
                    yield key
                    yield from keys(child)
            elif isinstance(value, list):
                for child in value:
                    yield from keys(child)
        banned = {"reader_id", "input_identity", "source_path", "sha256", "target_rank", "is_dominant",
                  "matched_occurrences", "branch_count", "variant_count", "mapping_status"}
        self.assertFalse(banned & set(keys(self.packet)))
        self.assertEqual(self.packet["source_gaps"]["roots_without_branches"], ["غ ي ب"])
        gap_ayah = self.packet["context_ayat"][-1]
        self.assertTrue(gap_ayah["rootless"])
        self.assertEqual(gap_ayah["rootless_reason"], self.source["ayat"][-1]["rootless_reason"])

    def test_v1_fields_work_without_v2_qualification_requirements(self):
        self.validate()
        self.assertNotIn("reading", self.response["baseline_models"][0])
        self.assertNotIn("reader_inference", self.response["surprising_valid_outliers"][0])
        self.assertIsInstance(self.response["context_deltas"][0]["structural_cues"][0], str)
        for status in ("new", "strengthened", "weakened", "revised", "discarded"):
            self.response["context_deltas"][0]["status"] = status
            self.validate()
        self.response["discarded_or_unchanged"] = ["Synthetic debug note."]
        self.response["context_deltas"][0].update(minimal_triggers=["Synthetic trigger."], ablation="Synthetic ablation.")
        self.validate()

    def test_v1_shared_branch_citation_exports_every_variant_not_a_guessed_selection(self):
        self.validate()
        evidence = w.evidence_payload(self.job, self.source, self.response)
        self.assertEqual(evidence["response"], self.response)
        self.assertEqual(len(evidence["resolved_evidence"]), 3)
        resolved = evidence["resolved_evidence"][1]["branches"][0]
        self.assertNotIn("variant", resolved)
        self.assertEqual([variant["scope_ar"] for variant in resolved["variants"]], ["نطاق أول", "نطاق ثان"])
        self.assertEqual([variant["variant_id"] for variant in resolved["variants"]], ["V001", "V002"])
        self.assertTrue(all(variant["source_path"] for variant in resolved["variants"]))
        self.assertEqual(evidence["resolved_evidence"][1]["structural_cues"], self.response["context_deltas"][0]["structural_cues"])

    def test_v1_does_not_accept_null_changes_or_structural_only_deltas(self):
        original = copy.deepcopy(self.response)
        for section in w.SECTIONS:
            self.response = copy.deepcopy(original)
            self.response[section][0]["changed_reading"] = None
            with self.assertRaises(ValueError):
                self.validate()
        self.response = copy.deepcopy(original)
        self.response["context_deltas"][0]["activation_trace"] = [trace()]
        with self.assertRaisesRegex(ValueError, "branch-backed context"):
            self.validate()

    def test_v1_rejects_wrong_occurrences_targets_and_trigger_roots(self):
        original = copy.deepcopy(self.response)
        for key, value in (("source_word_indices", ["2"]), ("source_ref", "2:5"),
                           ("mapped_root_id", "root_000003"), ("branch_id", "B999"), ("root", "غ ي ب")):
            with self.subTest(key=key):
                self.response = copy.deepcopy(original)
                self.response["context_deltas"][0]["activation_trace"][0][key] = value
                with self.assertRaises(ValueError):
                    self.validate()
        self.response = copy.deepcopy(original)
        self.response["context_deltas"][0]["trigger_roots"] = ["أ ث ر"]
        with self.assertRaisesRegex(ValueError, "trigger_roots"):
            self.validate()
        self.response = copy.deepcopy(original)
        self.response["context_deltas"][0]["trigger_refs"] = ["2:3"]
        with self.assertRaisesRegex(ValueError, "trigger_refs"):
            self.validate()
        self.response = copy.deepcopy(original)
        self.response["baseline_models"][0]["activation_trace"] = [trace("2:2", "ط ر ق", "root_000002")]
        with self.assertRaisesRegex(ValueError, "baseline cites context"):
            self.validate()

    def test_v1_rejects_wrong_reader_duplicate_ids_and_false_rootlessness(self):
        original = copy.deepcopy(self.response)
        self.response["reader_id"] = "wrong_reader"
        with self.assertRaisesRegex(ValueError, "reader mismatch"):
            self.validate()
        self.response = copy.deepcopy(original)
        self.response["context_deltas"][0]["model_id"] = "B1"
        with self.assertRaisesRegex(ValueError, "duplicate finding"):
            self.validate()
        for value in (True, 1, False):
            self.response = copy.deepcopy(original)
            self.response["rootless_focus"] = value
            with self.assertRaises(ValueError):
                self.validate()
        self.response = copy.deepcopy(original)
        self.response["baseline_models"][0]["activation_trace"] = []
        with self.assertRaises(ValueError):
            self.validate()

    def test_original_schema_rootless_exception_still_works_only_for_annotation_gap(self):
        source = copy.deepcopy(self.source)
        source["focus_ref"] = "2:4"
        directory = self.root / "rootless"
        job = w.write_job(directory, source, [])
        packet = w.load_job(directory, require_response=False)[1]
        response = response_fixture(job)
        response.update(rootless_focus=True, context_deltas=[], surprising_valid_outliers=[])
        response["baseline_models"][0]["activation_trace"] = []
        w.validate_response(response, packet, job, self.schema)

    def test_explicit_profiles_change_only_the_v1_profile_block(self):
        self.assertEqual(self.job["requested_profile"], {"model": "gpt-5.6-sol", "reasoning_effort": "max"})
        for model, effort in (("gpt-5.6-luna", "max"), ("gpt-6-astra", "max"), ("gpt-5.6-sol", "medium")):
            directory = self.root / f"profile-{model}-{effort}"
            job = w.write_job(directory, self.source, [], model=model, reasoning_effort=effort)
            prompt = (directory / "prompt.md").read_bytes()
            self.assertEqual(prompt.replace(f"model: {model}\nreasoning_effort: {effort}\n".encode(),
                                            b"model: gpt-5.6-sol\nreasoning_effort: max\n"), w.V1_PROMPT.read_bytes())
            self.assertEqual(job["input_identity"]["packet_sha256"], self.job["input_identity"]["packet_sha256"])
            self.assertEqual(job["input_identity"]["schema_sha256"], self.job["input_identity"]["schema_sha256"])
            self.assertNotIn("service_tier", job["requested_profile"])
            w.load_job(directory, require_response=False)
            job["requested_profile"]["model"] = "gpt-5.6-terra"
            (directory / "job.json").write_bytes(w.json_bytes(job))
            with self.assertRaisesRegex(ValueError, "frozen prompt profile"):
                w.load_job(directory, require_response=False)
        with self.assertRaisesRegex(ValueError, "unsupported model"):
            w.write_job(self.root / "unavailable", self.source, [], model="unavailable")

    def test_restored_inline_request_delivers_exact_files_and_reader_assignment(self):
        _, args, body = runner.request(self.directory)
        self.assertEqual(args[args.index("--model") + 1], "gpt-5.6-sol")
        self.assertIn('model_reasoning_effort="max"', args)
        for filename in (self.packet_name, self.schema_name):
            supplied = body.split(f"<{filename}>\n", 1)[1].split(f"</{filename}>", 1)[0]
            self.assertEqual(supplied.encode(), (self.directory / filename).read_bytes())
        self.assertIn("assigned reader_id is reader_hft_a", body)
        self.assertNotIn("input_identity", body)
        self.assertNotIn("source.packet.json", body)
        self.assertFalse(any("service_tier" in arg for arg in args))

    def test_frozen_restored_inputs_and_source_projection_cannot_be_replaced(self):
        with mock.patch.object(w, "WORKFLOW_ROOT", self.root / "missing-templates"):
            w.load_job(self.directory, require_response=False)
        altered = copy.deepcopy(self.packet)
        altered["focus_branch_inventories"][0]["targets"].pop()
        data = w.json_bytes(altered)
        (self.directory / self.packet_name).write_bytes(data)
        self.job["input_identity"]["packet_sha256"] = w.digest(data)
        (self.directory / "job.json").write_bytes(w.json_bytes(self.job))
        with self.assertRaisesRegex(ValueError, "complete source projection"):
            w.load_job(self.directory, require_response=False)

    def test_new_prepare_validate_export_is_offline_lossless_and_no_overwrite(self):
        (self.directory / "response.json").write_bytes(w.json_bytes(self.response))
        self.assertEqual(w.load_job(self.directory)[2], self.response)
        with mock.patch.object(w, "WORKFLOW_ROOT", self.root):
            output = w.export_job(self.directory)
            before = output.read_bytes()
            self.assertEqual(w.export_job(self.directory).read_bytes(), before)
            self.assertEqual(w.read_json(output)["response"], self.response)
        with self.assertRaises(FileExistsError):
            w.write_job(self.directory, self.source, [])

    def test_prepare_cli_uses_v1_filenames_and_profile_without_model_invocation(self):
        for filename, original in (("prompts/discovery.md", w.V1_PROMPT), ("schemas/response.schema.json", w.V1_SCHEMA)):
            path = self.root / filename
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(original.read_bytes())
        with mock.patch.object(w, "WORKFLOW_ROOT", self.root), \
             mock.patch.object(w, "build_packet", return_value=(self.source, [])), \
             mock.patch("sys.argv", ["workflow.py", "prepare", "--ayah", "2:1", "--window", "2:1-4", "--run", "cli"]), \
             mock.patch("sys.stdout", new_callable=io.StringIO) as stdout:
            w.main()
        report = json.loads(stdout.getvalue())
        self.assertEqual(report["profile"], {"model": "gpt-5.6-sol", "reasoning_effort": "max"})
        directory = self.root / "runs/cli/2_1"
        self.assertEqual(report["packet_bytes"], (directory / self.packet_name).stat().st_size)
        self.assertIsNone(w.load_job(directory, require_response=False)[2])

    def test_inline_compaction_is_formatting_only_and_failure_does_not_retry(self):
        # The subprocess is mocked: this test never starts Codex or a model.
        for valid in (True, False):
            with self.subTest(valid=valid):
                directory = self.root / "runs" / ("compact-valid" if valid else "compact-invalid")
                w.write_job(directory, self.source, [])
                raw = json.dumps(self.response, ensure_ascii=False, indent=2) if valid else '{"duplicate":1,"duplicate":2}'

                def fake_run(*args, **kwargs):
                    (directory / "response.json").write_text(raw)
                    return mock.Mock(returncode=0)

                with mock.patch.object(w, "WORKFLOW_ROOT", self.root), \
                     mock.patch("sys.argv", ["run_inline_reader.py", str(directory)]), \
                     mock.patch.object(runner.subprocess, "run", side_effect=fake_run) as launch, \
                     mock.patch("sys.stdout", new_callable=io.StringIO), \
                     self.assertRaises(SystemExit) as stopped:
                    runner.main()
                self.assertEqual(stopped.exception.code, 0 if valid else 1)
                launch.assert_called_once()
                if valid:
                    self.assertEqual((directory / "response.json").read_bytes(), w.json_bytes(self.response))
                else:
                    self.assertEqual((directory / "response.json").read_text(), raw)
                    self.assertIn("compaction_error", w.read_json(directory / "inline.result.json"))


class V1ResourceCompatibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.previous = w.WORKFLOW_ROOT / "runs/compare-20260905-sol-max"
        if not (cls.previous / "29_38/source.packet.json").exists():
            raise unittest.SkipTest("frozen comparison snapshots unavailable")

    def test_all_four_snapshots_keep_every_variant_mapping_and_ayah_in_v1_layout(self):
        for ref in ("29_38", "83_1", "100_1", "96_2"):
            with self.subTest(ref=ref):
                source = w.read_json(self.previous / ref / "source.packet.json")
                projected = w.v1_reader_packet(source)
                old_index, new_index = w.packet_index(source), w.packet_index(projected)
                self.assertEqual(set(old_index[2]), set(new_index[2]))
                for key, variant in old_index[2].items():
                    self.assertEqual(new_index[2][key], {field: variant[field] for field in ("variant_id", *w.LINGUISTIC_VARIANT_FIELDS)})
                self.assertEqual(set(old_index[0]), set(new_index[0]))
                for ref, original in old_index[0].items():
                    for field in ("ref", "text_ar", "root_sequence", "root_occurrences"):
                        self.assertEqual(new_index[0][ref][field], original[field])
                for root, mapping in old_index[1].items():
                    self.assertEqual([target["furuq_root_id"] for target in mapping["targets"]],
                                     [target["furuq_root_id"] for target in new_index[1][root]["targets"]])
                focus_roots = old_index[0][source["focus_ref"]]["root_sequence"]
                self.assertEqual([item["root"] for item in projected["focus_branch_inventories"]], focus_roots)

    def test_stored_v1_29_38_response_is_accepted_without_copying_or_rebinding_it(self):
        source = w.read_json(self.previous / "29_38/source.packet.json")
        packet = w.v1_reader_packet(source)
        response = w.read_json(w.REPO_ROOT / "focus_trace/runs/s29/readers/reader_hft_a/29_38.focus_trace.json")
        job = {"protocol": w.JOB_PROTOCOL, "reader_id": response["reader_id"]}
        w.validate_response(response, packet, job, w.read_json(w.V1_SCHEMA))
        # Also exercise the existing v1 response validator, read-only. Its old
        # lean PACKET validator intentionally bans restored English; do not use it.
        legacy_dir = w.REPO_ROOT / "focus_trace/scripts"
        with mock.patch.object(sys, "path", [str(legacy_dir), *sys.path]):
            spec = importlib.util.spec_from_file_location("hft_v1_response_check", legacy_dir / "validate_focus_trace.py")
            legacy = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(legacy)
            legacy.validate_response(packet, response)
        web = w.packet_index(packet)[2][("root_000672", "B010", "V001")]
        self.assertIn("العنكبوت", web["scope_ar"])
        self.assertIn("webbing", web["image_en"])

    def test_exact_v1_blocks_83_1_missing_focus_inventory_without_faking_rootlessness(self):
        source = w.read_json(self.previous / "83_1/source.packet.json")
        with tempfile.TemporaryDirectory(prefix="hft-v1-missing-focus-") as temp:
            directory = Path(temp) / "83_1"
            with self.assertRaisesRegex(ValueError, "rooted focus has no branch inventory"):
                w.write_job(directory, source, [])
            self.assertFalse(directory.exists())

    def test_all_20_existing_responses_and_exports_still_match_without_writes(self):
        jobs = sorted(w.WORKFLOW_ROOT.glob("runs/compare-20260905-*/*/job.json"))
        self.assertEqual(len(jobs), 20)
        for path in jobs:
            with self.subTest(job=str(path)):
                job, packet, response = w.load_job(path.parent)
                source = w.read_json(path.parent / "source.packet.json")
                evidence = w.evidence_payload(job, source, response)
                evidence.update(reader_id=job["reader_id"], response_protocol=job["response_protocol"],
                                source_packet_sha256=job["source_packet_sha256"], binding="coordinator_job_directory")
                self.assertEqual(w.json_bytes(evidence), (path.parent / "evidence.json").read_bytes())


if __name__ == "__main__":
    unittest.main()
