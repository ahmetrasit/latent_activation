from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Iterator


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PACKAGE_ROOT.parent
SCRIPTS_ROOT = PACKAGE_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_ROOT))

import common  # noqa: E402
import orchestrate  # noqa: E402
import prepare_run  # noqa: E402
import schema_validation  # noqa: E402
import validate_run  # noqa: E402


def walk_objects(value: Any) -> Iterator[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for nested in value.values():
            yield from walk_objects(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from walk_objects(nested)


def valid_finding() -> dict[str, Any]:
    return {
        "finding_id": "F01",
        "title": "Bounded relation",
        "primary_proposition": "The positioned relation changes the local reading.",
        "primary_anchors": ["passage-arabic.txt:1:1"],
        "secondary_carriers": [],
        "lexical_evidence": ["entry-1"],
        "local_trigger": "The form occurs in the governing construction.",
        "relation_edges": [
            {
                "edge_type": "role-complement",
                "source": "entry-1",
                "target": "S1:1",
                "basis": ["verified-passage-contact"],
                "evidence_refs": ["S1:1", "entry-1"],
            }
        ],
        "relational_bridge": "The lexical operation is activated by the positioned construction.",
        "primary_effect": "The relation narrows how the passage movement is perceived.",
        "counterfactual": "Without the relation, the narrowing is unexplained.",
        "linguistic_boundary": "The branch is not a replacement gloss.",
        "local_sense_status": {"entry-1": "sense-compatible"},
        "activation_status": "locally-triggered",
        "lexical_evidence_strength": "medium",
        "activation_confidence": "medium",
        "narrative_role": "supporting",
        "epistemic_status": "accepted",
        "limitations": ["Composite lexical evidence."],
        "publication_policy": "required-body",
    }


def valid_lexical_record(contaminated: bool = False) -> dict[str, Any]:
    return {
        "root_norm": "ك ت ب",
        "root_key": "كتب",
        "passage_root_norms": ["ك ت ب"],
        "branch_id": "B001",
        "source_id": "fixture",
        "source_name": "fixture lexical inventory",
        "source_entry_id": "entry-1",
        "source_ar_exact": "الكتابة",
        "branch_image_ar": "ضم الحروف",
        "what_is_ar": "أثر مكتوب",
        "lexical_unit_or_form": None,
        "derivation_or_pattern": None,
        "status": "accepted",
        "contaminated": contaminated,
        "editorial_notes": "Fixture composite record.",
        "provenance_granularity": "composite-untagged",
        "source_families": [],
        "source_refs": ["fixture:1"],
    }


def make_run(root: Path, optional_product: str = "none") -> None:
    for directory in (
        root / "inputs",
        root / "logs",
        root / "tasks",
        root / "agent-a" / "draft",
        root / "agent-a" / "final",
        root / "agent-b",
        root / "agent-c",
    ):
        directory.mkdir(parents=True, exist_ok=True)
    common.write_json(
        root / "inputs" / "run-card.json",
        {
            "workflow_id": common.WORKFLOW_ID,
            "run_id": "fixture-run",
            "passage_id": "S1:1-1",
            "scope": {"surah": 1, "ayah_start": 1, "ayah_end": 1},
            "basmala_policy": "canonical-only",
            "output_language": "Turkish",
            "source_profile": "fixture",
            "quality_tier": "source-limited",
            "gold_release_eligible": False,
            "lexicon_policy": "accepted-clean-composite-editorial",
            "evidence_policy": "prepared-inputs-only",
            "optional_product": optional_product,
        },
    )
    common.write_json(
        root / "inputs" / "input-summary.json",
        {
            "workflow_id": common.WORKFLOW_ID,
            "run_id": "fixture-run",
            "quality_tier": "source-limited",
            "source_profile": "fixture",
            "passage": {
                "surah": 1,
                "ayah_start": 1,
                "ayah_end": 1,
                "positions": 1,
                "opening_context_included": False,
            },
            "morphology": {"mode": "fallback", "rows": 1, "rooted_only": True},
            "syntax": {"source_rows": 0, "edges": 0},
            "lexical": {
                "mode": "fallback",
                "rows": 1,
                "review_rows_included": False,
                "contamination_filter": "fallback-reviewed-clean-export",
                "excluded_contaminated_rows": 0,
            },
            "limitations": ["Fixture composite evidence."],
        },
    )
    (root / "inputs" / "passage-arabic.txt").write_text("1:1\tin-scope\tكتب\n", encoding="utf-8")
    (root / "inputs" / "primary-scaffold.md").write_text("# Direct reading\n", encoding="utf-8")
    common.write_tsv(
        root / "inputs" / "morphology.tsv",
        ("surah", "ayah", "qac_ref", "surface_ar", "root_norm", "root_key", "context_role"),
        [
            {
                "surah": 1,
                "ayah": 1,
                "qac_ref": "1:1:1:1",
                "surface_ar": "كتب",
                "root_norm": "ك ت ب",
                "root_key": "كتب",
                "context_role": "in-scope",
            }
        ],
    )
    common.write_tsv(
        root / "inputs" / "syntax.tsv",
        ("edge_id", "source_position", "target_position", "edge_type"),
        [],
    )
    common.write_jsonl(root / "inputs" / "lexical-branches.jsonl", [valid_lexical_record()])


class SchemaAndPromptTests(unittest.TestCase):
    def test_json_documents_parse_and_schema_refs_resolve(self) -> None:
        paths = [
            path
            for path in PACKAGE_ROOT.rglob("*.json")
            if "run" not in path.relative_to(PACKAGE_ROOT).parts
        ]
        ids: dict[str, Path] = {}
        for path in paths:
            document = json.loads(path.read_text(encoding="utf-8"))
            for item in walk_objects(document):
                schema_id = item.get("$id")
                if isinstance(schema_id, str):
                    self.assertNotIn(schema_id, ids)
                    ids[schema_id] = path
                ref = item.get("$ref")
                if isinstance(ref, str) and not ref.startswith(("#", "http://", "https://")):
                    self.assertTrue((path.parent / ref.split("#", 1)[0]).is_file())
        self.assertIn("synthesis-finding.schema.json", ids)
        self.assertNotIn("audit-closure.schema.json", ids)

    def test_synthesis_schema_preserves_epistemic_shape(self) -> None:
        finding = valid_finding()
        self.assertEqual([], schema_validation.validate_instance(finding, "synthesis-finding"))
        finding.pop("linguistic_boundary")
        errors = schema_validation.validate_instance(finding, "synthesis-finding")
        self.assertTrue(any("linguistic_boundary" in error and "required" in error for error in errors))

    def test_agent_a_prompt_names_every_required_core_field(self) -> None:
        schema = common.load_json(PACKAGE_ROOT / "schemas" / "synthesis-finding.schema.json")
        prompt = (PACKAGE_ROOT / "prompts" / "agent-a-synthesis.md").read_text(encoding="utf-8")
        for field in schema["required"]:
            self.assertIn(f'"{field}"', prompt)
        self.assertIn("genuine synthesis", prompt)
        self.assertNotIn("hash", prompt.lower())

    def test_python_scripts_compile(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "py_compile", *map(str, sorted(SCRIPTS_ROOT.glob("*.py")))],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stderr)


class LeanRuntimeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="gsls-v21-lean-test-")
        self.addCleanup(self.temp.cleanup)
        self.run_root = Path(self.temp.name) / "run"
        make_run(self.run_root)

    def write_draft(self, finding: dict[str, Any] | None = None) -> None:
        draft = self.run_root / "agent-a" / "draft"
        common.write_jsonl(draft / "draft-synthesis.jsonl", [finding or valid_finding()])
        (draft / "draft-synthesis.md").write_text("# Draft synthesis\n\nA bounded argument.\n", encoding="utf-8")

    def write_final(self) -> None:
        final = self.run_root / "agent-a" / "final"
        common.write_jsonl(final / "final-synthesis.jsonl", [valid_finding()])
        (final / "final-synthesis.md").write_text("# Final synthesis\n\nA revised argument.\n", encoding="utf-8")

    def advance_to_review(self) -> None:
        orchestrate.initialize(self.run_root)
        self.write_draft()
        state = orchestrate.transition(self.run_root, "complete")
        self.assertEqual("B_REVIEW", state["state"])

    def test_task_is_idempotent_and_has_no_integrity_ledger(self) -> None:
        orchestrate.initialize(self.run_root)
        first = orchestrate.emit_task(self.run_root)
        first_text = first.read_text(encoding="utf-8")
        second = orchestrate.emit_task(self.run_root)
        self.assertEqual(first, second)
        self.assertEqual(first_text, second.read_text(encoding="utf-8"))
        self.assertIn("## Evidence inputs", first_text)
        self.assertIn("## Control files", first_text)
        self.assertNotIn("HASH", first_text)
        self.assertNotIn("SESSION", first_text)

    def test_invalid_synthesis_does_not_advance(self) -> None:
        orchestrate.initialize(self.run_root)
        finding = valid_finding()
        finding.pop("counterfactual")
        self.write_draft(finding)
        with self.assertRaises(common.ContractError):
            orchestrate.transition(self.run_root, "complete")
        self.assertEqual("A_SYNTHESIZE", orchestrate.load_state(self.run_root)["state"])

    def test_clean_review_promotes_draft_and_finishes(self) -> None:
        self.advance_to_review()
        draft_jsonl = (self.run_root / "agent-a" / "draft" / "draft-synthesis.jsonl").read_text(encoding="utf-8")
        (self.run_root / "agent-b" / "review.md").write_text(
            "VERDICT: clean\n\nThe synthesis is bounded; no material omission was found.\n",
            encoding="utf-8",
        )
        state = orchestrate.transition(self.run_root, "clean")
        self.assertEqual("DONE", state["state"])
        final_jsonl = (self.run_root / "agent-a" / "final" / "final-synthesis.jsonl").read_text(encoding="utf-8")
        self.assertEqual(draft_jsonl, final_jsonl)
        self.assertFalse((self.run_root / "agent-a" / "final" / "final-closure.json").exists())

    def test_revision_path_uses_review_memo_without_action_ledger(self) -> None:
        self.advance_to_review()
        (self.run_root / "agent-b" / "review.md").write_text(
            "VERDICT: revision-required\n\n## Issue\nTARGET: F01\nISSUE: Boundary too broad.\n"
            "REASON: The branch is compatible only.\nREQUIRED CHANGE: Narrow the boundary.\n"
            "EVIDENCE: entry-1\n",
            encoding="utf-8",
        )
        state = orchestrate.transition(self.run_root, "revision_required")
        self.assertEqual("A_REVISE", state["state"])
        task = orchestrate.emit_task(self.run_root).read_text(encoding="utf-8")
        self.assertIn(str(self.run_root / "agent-b" / "review.md"), task)
        self.assertNotIn("audit-actions", task)
        self.write_final()
        state = orchestrate.transition(self.run_root, "complete")
        self.assertEqual("DONE", state["state"])

    def test_review_verdict_must_match_transition(self) -> None:
        self.advance_to_review()
        (self.run_root / "agent-b" / "review.md").write_text("VERDICT: clean\n", encoding="utf-8")
        with self.assertRaises(common.ContractError):
            orchestrate.transition(self.run_root, "revision_required")
        self.assertEqual("B_REVIEW", orchestrate.load_state(self.run_root)["state"])

    def test_optional_publication_has_one_output(self) -> None:
        shutil.rmtree(self.run_root)
        make_run(self.run_root, optional_product="publication-essay")
        self.advance_to_review()
        (self.run_root / "agent-b" / "review.md").write_text("VERDICT: clean\n", encoding="utf-8")
        state = orchestrate.transition(self.run_root, "clean")
        self.assertEqual("C_RENDER", state["state"])
        (self.run_root / "agent-c" / "publication.md").write_text("# Publication\n", encoding="utf-8")
        state = orchestrate.transition(self.run_root, "complete")
        self.assertEqual("DONE_WITH_PUBLICATION", state["state"])

    def test_preflight_rejects_contaminated_prepared_branch(self) -> None:
        common.write_jsonl(
            self.run_root / "inputs" / "lexical-branches.jsonl",
            [valid_lexical_record(contaminated=True)],
        )
        report = validate_run.validate_inputs(self.run_root)
        self.assertFalse(report.passed)
        self.assertTrue(any("contaminated" in error for error in report.errors))


class RestoredDatabaseIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = tempfile.TemporaryDirectory(prefix="gsls-v21-db-test-")
        cls.root = Path(cls.temp.name)
        scaffold = cls.root / "primary-scaffold.md"
        scaffold.write_text("# Independent S1 reading\n\nA direct structural reading.\n", encoding="utf-8")
        cls.run_root = cls.root / "run"
        cls.result = prepare_run.prepare(
            argparse.Namespace(
                run_root=cls.run_root,
                run_id="db-integration",
                surah=1,
                ayah_start=1,
                ayah_end=7,
                primary_scaffold=scaffold,
                profile=prepare_run.DEFAULT_PROFILE,
                output_language="Turkish",
                basmala_policy="canonical-only",
                optional_product="none",
                include_review_branches=False,
                allow_source_limited=True,
            )
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp.cleanup()

    def test_restored_sqlite_sources_are_used_and_contamination_is_excluded(self) -> None:
        self.assertEqual("database", self.result["morphology_mode"])
        self.assertEqual("database", self.result["lexical_mode"])
        self.assertGreater(self.result["excluded_contaminated_branches"], 0)
        records = [record for _, record in common.iter_jsonl(self.run_root / "inputs" / "lexical-branches.jsonl")]
        entry_ids = {record["source_entry_id"] for record in records}
        self.assertNotIn("branch_images:root_000973:B002", entry_ids)
        self.assertTrue(all(record["contaminated"] is False for record in records))

    def test_prepared_database_run_passes_lean_preflight_without_ledgers(self) -> None:
        report = validate_run.validate_inputs(self.run_root)
        self.assertTrue(report.passed, "\n".join(report.errors))
        self.assertFalse((self.run_root / "inputs" / "run-card.md").exists())
        self.assertFalse((self.run_root / "inputs" / "source-manifest.json").exists())
        self.assertFalse((self.run_root / "logs" / "artifact-hashes.tsv").exists())
        self.assertFalse((self.run_root / "logs" / "inputs-validation.json").exists())


if __name__ == "__main__":
    unittest.main()
