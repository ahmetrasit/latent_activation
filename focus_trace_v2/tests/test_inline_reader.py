"""Offline checks only: no Codex invocation or paid model request."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from focus_trace_v2 import workflow as w
from test_workflow import fixture_packet, write_previous_job

spec = importlib.util.spec_from_file_location("hft_inline_reader", w.WORKFLOW_ROOT / "run_inline_reader.py")
runner = importlib.util.module_from_spec(spec)
with mock.patch.dict("sys.modules", {"workflow": w}):
    spec.loader.exec_module(runner)


class InlineReaderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="hft-inline-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.packet = fixture_packet()

    def test_profiles_are_explicit_without_tier_or_history(self):
        bodies = []
        for model, effort in [("gpt-5.6-luna", "max"), ("gpt-5.6-terra", "max"),
                              ("gpt-5.6-sol", "max"), ("gpt-6-astra", "medium"), ("gpt-6-astra", "max")]:
            with self.subTest(model=model, effort=effort):
                directory = self.root / f"{model}-{effort}"
                write_previous_job(directory, self.packet, [], model=model, reasoning_effort=effort)
                _, args, body = runner.request(directory)
                self.assertEqual(args[args.index("--model") + 1], model)
                self.assertIn("model_reasoning_effort=" + json.dumps(effort), args)
                self.assertIn("--ignore-user-config", args)
                self.assertEqual(args[args.index("--sandbox") + 1], "read-only")
                self.assertNotIn("resume", args)
                self.assertNotIn("fork", args)
                self.assertFalse(any("service_tier" in arg for arg in args))
                bodies.append(body)
        self.assertEqual(len(set(bodies)), 1)

    def test_complete_frozen_files_not_coordinator_metadata_are_delivered(self):
        directory = self.root / "reader"
        write_previous_job(directory, self.packet, [])
        _, args, body = runner.request(directory)
        for filename in ("packet.json", "response.schema.json"):
            supplied = body.split(f"<{filename}>\n", 1)[1].split(f"</{filename}>", 1)[0]
            self.assertEqual(supplied.encode("utf-8"), (directory / filename).read_bytes())
        self.assertIn("model_instructions_file=" + json.dumps(str(directory / "prompt.md")), args)
        self.assertNotIn("source.packet.json", body)
        self.assertNotIn("input_identity", body)
        self.assertFalse((directory / "response.json").exists())

    def test_changed_input_fails_before_request(self):
        directory = self.root / "reader"
        write_previous_job(directory, self.packet, [])
        (directory / "packet.json").write_bytes(b"{}\n")
        with self.assertRaisesRegex(ValueError, "frozen input changed"):
            runner.request(directory)

    def test_existing_launch_is_not_retried(self):
        directory = self.root / "runs" / "reader"
        write_previous_job(directory, self.packet, [])
        (directory / "inline.launch.json").write_bytes(b"{}\n")
        with mock.patch.object(w, "WORKFLOW_ROOT", self.root), \
             mock.patch("sys.argv", ["run_inline_reader.py", str(directory)]), \
             mock.patch.object(runner.subprocess, "run") as launch:
            with self.assertRaisesRegex(ValueError, "existing artifact"):
                runner.main()
            launch.assert_not_called()
