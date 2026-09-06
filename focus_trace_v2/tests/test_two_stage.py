"""Two-pass checks are offline; every model subprocess is mocked."""

import copy
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from focus_trace_v2 import workflow as w
from test_inline_reader import runner
from test_v1_compatibility import packet_fixture, response_fixture


THREAD = "00000000-0000-0000-0000-000000000001"


def notes_fixture():
    return {section: [{"id": identifier, "discovery": "Synthetic focus anchor and changed reading.",
                       "cues": "Synthetic ayah/root/branch pointers; not quality evidence."}]
            for section, identifier in zip(w.SECTIONS, ("B1", "D1", "O1"))}


class TwoStageTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="hft-two-stage-")
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.directory = self.root / "runs/fixture/2_1"
        self.job = w.write_job(self.directory, packet_fixture(), [], two_stage=True,
                               model="gpt-5.6-luna", reasoning_effort="max")
        self.notes = notes_fixture()
        self.response = response_fixture(self.job)
        patcher = mock.patch.object(runner, "runtime_check", return_value={"synthetic_runtime": True})
        self.runtime = patcher.start()
        self.addCleanup(patcher.stop)

    def run_stage(self, stage, output=None, thread=THREAD, exit_code=0, events=None):
        if output is None:
            output = self.notes if stage == "discovery" else self.response
        raw = json.dumps(output, ensure_ascii=False, indent=2) if not isinstance(output, str) else output

        def fake_run(command, **kwargs):
            output_path = Path(command[command.index("--output-last-message") + 1])
            output_path.write_text(raw)
            records = events if events is not None else [
                {"type": "thread.started", "thread_id": thread},
                {"type": "turn.started"}, {"type": "turn.completed", "usage": {}},
            ]
            for record in records:
                kwargs["stdout"].write(w.json_bytes(record))
            return mock.Mock(returncode=exit_code)

        with mock.patch.object(w, "WORKFLOW_ROOT", self.root), \
             mock.patch("sys.argv", ["run_inline_reader.py", str(self.directory), "--stage", stage]), \
             mock.patch.object(runner.subprocess, "run", side_effect=fake_run) as launch, \
             mock.patch("sys.stdout", new_callable=io.StringIO), \
             self.assertRaises(SystemExit) as stopped:
            runner.main()
        launch.assert_called_once()
        return stopped.exception.code, launch.call_args

    def test_v1_structure_posture_and_core_are_protected(self):
        original = w.prompt_sections((self.directory / "prompt.md").read_bytes())
        discovery = w.prompt_sections((self.directory / "discovery.prompt.md").read_bytes())
        self.assertEqual(list(original), list(discovery))
        for section in ("intro", b"## Reader Posture\n", b"## Core Task\n"):
            self.assertEqual(original[section], discovery[section])
        reporting = (self.directory / "prompt.md").read_bytes().split(b"## Required Evidence Discipline\n", 1)[1]
        self.assertTrue((self.directory / "ledger.prompt.md").read_bytes().endswith(reporting))
        goal = reporting.split(b"For `surprising_valid_outliers`, record readings", 1)[1].split(b"\nAfter writing valid JSON", 1)[0]
        self.assertIn(goal, (self.directory / "discovery.prompt.md").read_bytes())
        self.assertEqual((self.directory / w.reader_filenames(self.job)[1]).read_bytes(), w.V1_SCHEMA.read_bytes())

    def test_one_pass_still_has_identical_packet_schema_and_prompt(self):
        other = self.root / "one-pass"
        job = w.write_job(other, packet_fixture(), [], model="gpt-5.6-luna", reasoning_effort="max")
        self.assertEqual(job["input_identity"], self.job["input_identity"])
        self.assertNotIn("two_stage_inputs", job)
        self.assertEqual((other / "source.packet.json").read_bytes(), (self.directory / "source.packet.json").read_bytes())
        self.assertFalse((other / "discovery.prompt.md").exists())

    def copy_templates(self):
        for filename in ("prompts/discovery.md", "prompts/discovery_two_stage.md", "prompts/ledger_followup.md", "schemas/response.schema.json"):
            target = self.root / filename
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((w.WORKFLOW_ROOT / filename).read_bytes())

    def test_protected_v1_prompt_drift_fails_before_writing_job(self):
        self.copy_templates()
        path = self.root / "prompts/discovery_two_stage.md"
        path.write_text(path.read_text().replace("Your role is a discovery reader, not a conservative auditor.",
                                                "Your role is a conservative auditor."))
        with mock.patch.object(w, "WORKFLOW_ROOT", self.root), self.assertRaisesRegex(ValueError, "protected v1 section"):
            w.write_job(self.root / "must-not-exist", packet_fixture(), [], two_stage=True)
        self.assertFalse((self.root / "must-not-exist").exists())

    def test_prepare_cli_is_offline_and_freezes_two_stage_option(self):
        self.copy_templates()
        with mock.patch.object(w, "WORKFLOW_ROOT", self.root), \
             mock.patch.object(w, "build_packet", return_value=(packet_fixture(), [])), \
             mock.patch("sys.argv", ["workflow.py", "prepare", "--ayah", "2:1", "--window", "2:1-4", "--run", "cli", "--two-stage"]), \
             mock.patch.object(runner.subprocess, "run") as launch, \
             mock.patch("sys.stdout", new_callable=io.StringIO):
            w.main()
        launch.assert_not_called()
        job, _, response = w.load_job(self.root / "runs/cli/2_1", require_response=False)
        self.assertEqual(set(job["two_stage_inputs"]), set(w.TWO_STAGE_PROMPTS))
        self.assertIsNone(response)

    def test_all_requested_profiles_keep_same_discovery_instructions(self):
        for model, effort in (("gpt-5.6-luna", "max"), ("gpt-5.6-terra", "max"), ("gpt-5.6-sol", "max"),
                              ("gpt-6-astra", "medium"), ("gpt-6-astra", "max")):
            directory = self.root / f"{model}-{effort}"
            job = w.write_job(directory, packet_fixture(), [], two_stage=True, model=model, reasoning_effort=effort)
            self.assertEqual(job["input_identity"]["packet_sha256"], self.job["input_identity"]["packet_sha256"])
            prompt = (directory / "discovery.prompt.md").read_bytes()
            self.assertEqual(prompt.replace(f"model: {model}\nreasoning_effort: {effort}\n".encode(),
                                            b"model: gpt-5.6-sol\nreasoning_effort: max\n"),
                             (w.WORKFLOW_ROOT / "prompts/discovery_two_stage.md").read_bytes())

    def test_frozen_stage_prompts_cannot_change(self):
        for filename in w.TWO_STAGE_PROMPTS:
            with self.subTest(filename=filename):
                path = self.directory / filename
                original = path.read_bytes()
                path.write_bytes(original + b"changed")
                with self.assertRaisesRegex(ValueError, "frozen input changed"):
                    runner.request(self.directory, "discovery")
                path.write_bytes(original)

    def test_discovery_delivers_all_packet_bytes_but_no_ledger_schema(self):
        _, command, body = runner.request(self.directory, "discovery")
        self.assertTrue(body.startswith(runner.EXISTING_OUTPUTS_LIMIT))
        packet = (self.directory / "focus_trace_packet.json").read_text()
        self.assertIn("<focus_trace_packet.json>\n" + packet + "</focus_trace_packet.json>", body)
        self.assertNotIn("<focus_trace/schemas/", body)
        self.assertNotIn('"$defs"', body)
        self.assertNotIn("source.packet.json", body)
        self.assertNotIn("input_identity", body)
        self.assertNotIn("resume", command)
        self.assertIn('model_reasoning_effort="max"', command)
        self.assertEqual(command[command.index("--model") + 1], "gpt-5.6-luna")
        self.assertTrue(command[command.index("--output-last-message") + 1].endswith("discovery.json"))

    def test_stage_selection_is_explicit_and_inspect_never_launches(self):
        with self.assertRaisesRegex(ValueError, "two-stage jobs need"):
            runner.request(self.directory)
        before = sorted(str(p) for p in self.directory.rglob("*"))
        with mock.patch.object(w, "WORKFLOW_ROOT", self.root), \
             mock.patch("sys.argv", ["run_inline_reader.py", str(self.directory), "--stage", "discovery", "--inspect"]), \
             mock.patch.object(runner.subprocess, "run") as launch, \
             mock.patch("sys.stdout", new_callable=io.StringIO):
            runner.main()
        launch.assert_not_called()
        self.assertEqual(before, sorted(str(p) for p in self.directory.rglob("*")))
        with self.assertRaises(OSError):
            runner.request(self.directory, "ledger")

    def test_neutral_followup_resumes_exact_session_and_pinned_profile(self):
        self.assertEqual(self.run_stage("discovery")[0], 0)
        _, command, body = runner.request(self.directory, "ledger")
        self.assertTrue(body.startswith(runner.EXISTING_OUTPUTS_LIMIT))
        self.assertIn("resume", command)
        self.assertEqual(command[-2:], [THREAD, "-"])
        self.assertNotIn("--last", command)
        self.assertNotIn("fork", command)
        self.assertEqual(command[command.index("--model") + 1], "gpt-5.6-luna")
        self.assertIn('model_reasoning_effort="max"', command)
        self.assertFalse(any("service_tier" in arg for arg in command))
        self.assertIn("--ignore-user-config", command)
        self.assertIn("assigned reader_id is reader_hft_a", body)
        schema = (self.directory / w.reader_filenames(self.job)[1]).read_text()
        self.assertIn(schema, body)
        self.assertNotIn("<focus_trace_packet.json>", body)  # Retained in this conversation, not resent/pruned.
        self.assertNotIn("Synthetic focus anchor", body)  # No coordinator rewrite of the notes.

    def test_two_calls_keep_notes_and_export_complete_v1_ledger(self):
        self.assertEqual(self.run_stage("discovery")[0], 0)
        frozen_notes = (self.directory / "discovery.json").read_bytes()
        self.assertFalse((self.directory / "response.json").exists())
        self.assertFalse((self.directory / "ledger.launch.json").exists())
        self.assertEqual(self.run_stage("ledger")[0], 0)
        self.assertEqual((self.directory / "discovery.json").read_bytes(), frozen_notes)
        self.assertEqual((self.directory / "response.json").read_bytes(), w.json_bytes(self.response))
        self.assertEqual(w.load_job(self.directory)[2], self.response)
        with mock.patch.object(w, "WORKFLOW_ROOT", self.root):
            exported = w.read_json(w.export_job(self.directory))
        self.assertEqual(exported["discovery_notes"], self.notes)
        self.assertEqual(exported["response"], self.response)
        self.assertEqual(exported["two_stage_inputs"], self.job["two_stage_inputs"])

    def test_bad_discovery_is_preserved_and_never_followed_automatically(self):
        bad = '{"baseline_models":[]}'
        self.assertEqual(self.run_stage("discovery", bad)[0], 1)
        self.assertEqual((self.directory / "discovery.json").read_text(), bad)
        self.assertIn("validation_error", w.read_json(self.directory / "discovery.result.json"))
        self.assertFalse((self.directory / "ledger.launch.json").exists())
        with self.assertRaises(ValueError):
            runner.request(self.directory, "ledger")

    def test_missing_completed_turn_blocks_handoff(self):
        self.assertEqual(self.run_stage("discovery", events=[{"type": "thread.started", "thread_id": THREAD}])[0], 1)
        with self.assertRaisesRegex(ValueError, "did not complete"):
            runner.request(self.directory, "ledger")

    def test_changed_notes_events_or_profile_block_handoff(self):
        self.run_stage("discovery")
        for filename in ("discovery.json", "discovery.events.jsonl"):
            path = self.directory / filename
            original = path.read_bytes()
            path.write_bytes(original + b"\n")
            with self.assertRaisesRegex(ValueError, "changed"):
                runner.request(self.directory, "ledger")
            path.write_bytes(original)
        receipt = w.read_json(self.directory / "discovery.result.json")
        receipt["requested_profile"]["model"] = "gpt-5.6-sol"
        (self.directory / "discovery.result.json").write_bytes(w.json_bytes(receipt))
        with self.assertRaisesRegex(ValueError, "profile mismatch"):
            runner.request(self.directory, "ledger")

    def test_compacted_history_blocks_followup_before_any_model_call(self):
        self.run_stage("discovery")
        self.runtime.side_effect = ValueError("reader context was compacted")
        with mock.patch.object(runner.subprocess, "run") as launch, self.assertRaisesRegex(ValueError, "compacted"):
            runner.request(self.directory, "ledger")
        launch.assert_not_called()

    def test_invalid_ledger_stays_unaccepted_and_is_not_repaired(self):
        self.run_stage("discovery")
        invalid = copy.deepcopy(self.response)
        invalid["context_deltas"][0]["activation_trace"][0]["root"] = "WRONG"
        self.assertEqual(self.run_stage("ledger", invalid)[0], 1)
        self.assertEqual(w.read_json(self.directory / "response.json"), invalid)
        self.assertFalse((self.directory / "evidence.json").exists())
        self.assertIn("root does not occur", w.read_json(self.directory / "ledger.result.json")["validation_error"])

    def test_wrong_resumed_session_is_rejected(self):
        self.run_stage("discovery")
        self.assertEqual(self.run_stage("ledger", thread="00000000-0000-0000-0000-000000000002")[0], 1)
        self.assertIn("did not resume", w.read_json(self.directory / "ledger.result.json")["validation_error"])
        with self.assertRaisesRegex(ValueError, "ledger did not complete"):
            w.load_job(self.directory)
        with mock.patch.object(w, "WORKFLOW_ROOT", self.root), self.assertRaises(ValueError):
            w.export_job(self.directory)
        self.assertFalse((self.directory / "evidence.json").exists())

    def test_ledger_without_successful_receipt_or_changed_afterward_cannot_export(self):
        self.run_stage("discovery")
        self.run_stage("ledger")
        path = self.directory / "response.json"
        path.write_bytes(path.read_bytes() + b"\n")
        with self.assertRaisesRegex(ValueError, "ledger changed after completion"):
            w.load_job(self.directory)

    def test_valid_ledger_without_completion_receipt_is_not_an_accepted_job(self):
        self.run_stage("discovery")
        (self.directory / "response.json").write_bytes(w.json_bytes(self.response))
        with self.assertRaises(OSError):
            w.load_job(self.directory)

    def test_missing_candidate_fails_ledger_completion_not_just_helper(self):
        self.run_stage("discovery")
        self.response["surprising_valid_outliers"] = []
        self.assertEqual(self.run_stage("ledger")[0], 1)
        self.assertIn("candidate coverage", w.read_json(self.directory / "ledger.result.json")["validation_error"])
        with mock.patch.object(w, "WORKFLOW_ROOT", self.root), self.assertRaises(ValueError):
            w.export_job(self.directory)

    def test_missing_extra_or_duplicated_candidates_are_detected(self):
        for mutation in ("missing", "extra", "duplicate"):
            response = copy.deepcopy(self.response)
            if mutation == "missing":
                response["surprising_valid_outliers"] = []
            elif mutation == "extra":
                response["surprising_valid_outliers"][0]["outlier_id"] = "NEW"
            else:
                response["discarded_or_unchanged"] = ["O1: duplicate withdrawal."]
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                w.validate_candidate_coverage(self.notes, response)

    def test_explicit_withdrawal_preserves_candidate_accounting(self):
        self.run_stage("discovery")
        self.response["surprising_valid_outliers"] = []
        self.response["discarded_or_unchanged"] = ["O1: the candidate has no changed reading beyond the baseline."]
        self.assertEqual(self.run_stage("ledger")[0], 0)
        for note in ("O1:", "No candidate ID", "UNKNOWN: unsupported."):
            response = copy.deepcopy(self.response)
            response["discarded_or_unchanged"] = [note]
            with self.assertRaises(ValueError):
                w.validate_candidate_coverage(self.notes, response)

    def test_frozen_files_and_existing_launches_are_never_overwritten(self):
        with self.assertRaises(FileExistsError):
            w.write_job(self.directory, packet_fixture(), [], two_stage=True)
        self.run_stage("discovery")
        with mock.patch.object(w, "WORKFLOW_ROOT", self.root), \
             mock.patch("sys.argv", ["run_inline_reader.py", str(self.directory), "--stage", "discovery"]), \
             mock.patch.object(runner.subprocess, "run") as launch:
            with self.assertRaisesRegex(ValueError, "existing artifact"):
                runner.main()
        launch.assert_not_called()

    def test_minimal_note_validation_does_not_require_full_ledger_fields(self):
        self.assertEqual(w.validate_discovery(self.notes), {"B1", "D1", "O1"})
        for field in ("id", "discovery", "cues"):
            broken = copy.deepcopy(self.notes)
            broken["baseline_models"][0][field] = ""
            with self.assertRaises(ValueError):
                w.validate_discovery(broken)
        broken = copy.deepcopy(self.notes)
        broken["context_deltas"][0]["id"] = "B1"
        with self.assertRaisesRegex(ValueError, "duplicate discovery"):
            w.validate_discovery(broken)


class ExistingRerunPreservationTests(unittest.TestCase):
    def test_restored_reruns_remain_one_pass_with_unchanged_outputs(self):
        audit_path = w.WORKFLOW_ROOT / "runs/rerun-20260906-v1.runtime.json"
        if not audit_path.exists():
            self.skipTest("preserved rerun audit unavailable")
        for row in w.read_json(audit_path)["jobs"]:
            directory = w.REPO_ROOT / row["job_dir"]
            job = w.read_json(directory / "job.json")
            self.assertNotIn("two_stage_inputs", job)
            self.assertEqual(w.digest((directory / "response.json").read_bytes()), row["response_sha256"])
            if row["validation"] == "passed":
                self.assertIsNotNone(w.load_job(directory)[2])
            else:
                with self.assertRaisesRegex(ValueError, "root does not occur"):
                    w.load_job(directory)


class RuntimeContinuityTests(unittest.TestCase):
    def test_only_pinned_complete_uncompacted_history_is_accepted(self):
        profile = {"model": "gpt-5.6-luna", "reasoning_effort": "max"}
        with tempfile.TemporaryDirectory(prefix="hft-runtime-fixture-") as temp:
            root = Path(temp)
            path = root / "2026/09/06" / f"rollout-test-{THREAD}.jsonl"
            path.parent.mkdir(parents=True)
            events = [
                {"type": "turn_context", "payload": {"model": profile["model"], "effort": "max"}},
                {"type": "event_msg", "payload": {"type": "task_started"}},
                {"type": "event_msg", "payload": {"type": "task_complete"}},
            ]
            path.write_bytes(b"".join(w.json_bytes(event) for event in events))
            self.assertEqual(runner.runtime_check(THREAD, profile, turns=1, session_root=root)["completed_turns"], 1)
            for mutation in ("wrong-profile", "compacted", "intervening-turn", "incomplete"):
                changed = copy.deepcopy(events)
                if mutation == "wrong-profile":
                    changed[0]["payload"]["model"] = "gpt-5.6-sol"
                elif mutation == "compacted":
                    changed.append({"type": "compacted", "payload": {}})
                elif mutation == "intervening-turn":
                    changed.extend(copy.deepcopy(events[1:]))
                else:
                    changed.pop()
                path.write_bytes(b"".join(w.json_bytes(event) for event in changed))
                with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                    runner.runtime_check(THREAD, profile, turns=1, session_root=root)
            with self.assertRaisesRegex(ValueError, "cannot verify"):
                runner.runtime_check("missing", profile, turns=1, session_root=root)


if __name__ == "__main__":
    unittest.main()
