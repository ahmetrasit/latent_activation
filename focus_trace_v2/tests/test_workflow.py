"""Offline contracts and loss regressions. All reader findings here are synthetic."""

import copy
import gzip
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from focus_trace_v2 import workflow as w


def target(root_id, rank=1):
    return {"target_rank": rank, "frozen_root_norm": "fixture", "furuq_root_id": root_id,
            "furuq_root_norm": "fixture", "furuq_source_root_norm": "fixture",
            "furuq_resolution": "fixture", "target_occurrences": 1, "is_dominant": rank == 1}


def mapping(root, targets):
    return {"qac_root": root, "mapping_status": "fixture", "qac_total_occurrences": 1,
            "matched_occurrences": 1 if targets else 0, "unmapped_reason": "" if targets else "fixture unmapped",
            "targets": targets}


def variant(root_id, image="صورة", scope="نطاق", source="fixture/source"):
    return {"root_id": root_id, "source_path": source, "image_ar": image,
            "image_en": "image", "scope_ar": scope, "scope_en": "scope"}


def occurrence(root, surface):
    return {"root": root, "occurrence_count": 1, "word_indices": ["1"],
            "surfaces_ar": [surface], "lemmas_ar": [surface], "pos_tags": ["N"]}


def fixture_packet():
    mappings = {"أ ث ر": mapping("أ ث ر", [target("root_focus"), target("root_shared", 2), target("root_missing", 3)]),
                "ط ر ق": mapping("ط ر ق", [target("root_shared")]),
                "غ ي ب": mapping("غ ي ب", [])}
    shared = {"mapped_root_id": "root_shared", "branch_id": "B001",
              "variants": [variant("root_shared", "طريق", "نطاق أول"),
                           variant("root_shared", "طريق", "نطاق ثان", "fixture/second"),
                           variant("root_shared", "طريق", "نطاق أول")]}
    raw = {"أ ث ر": [{"mapped_root_id": "root_focus", "branch_id": "B001", "variants": [variant("root_focus")]}, shared],
           "ط ر ق": [copy.deepcopy(shared)], "غ ي ب": []}
    root_mappings, inventory, gaps = w.project_inventory(mappings, raw)
    ayat = [{"ref": "2:1", "text_ar": "أَثَرٌ ظَاهِرٌ", "root_sequence": ["أ ث ر"],
             "root_occurrences": [occurrence("أ ث ر", "أَثَرٌ")]},
            {"ref": "2:2", "text_ar": "طَرِيقٌ مُمْتَدٌّ", "root_sequence": ["ط ر ق"],
             "root_occurrences": [occurrence("ط ر ق", "طَرِيقٌ")]},
            {"ref": "2:3", "text_ar": "غَيْبٌ", "root_sequence": ["غ ي ب"],
             "root_occurrences": [occurrence("غ ي ب", "غَيْبٌ")]},
            {"ref": "2:4", "text_ar": "حَرْفٌ", "root_sequence": [], "root_occurrences": [],
             "rootless": True, "rootless_reason": "synthetic fixture"}]
    gaps["ayat_without_qac_roots"] = ["2:4"]
    return {"protocol": w.PACKET_PROTOCOL, "focus_ref": "2:1", "window": [a["ref"] for a in ayat],
            "ayat": ayat, "root_mappings": root_mappings, "branch_inventory": inventory,
            "source_gaps": gaps, "orientation": {"citable": False,
                "out_of_window_ayat": [{"ref": "2:5", "text_ar": "خَارِجٌ"}], "legacy_remote_snapshot": None}}


def finding(packet, model_id="B1"):
    focus = next(a for a in packet["ayat"] if a["ref"] == packet["focus_ref"])
    return {"model_id": model_id, "reading": "Synthetic test reading, not model output.", "status": "supported",
            "focus_anchor": {"quote_ar": focus["text_ar"], "role": "Synthetic focus anchor."},
            "activation_trace": [], "structural_cues": [], "mechanism": "Synthetic mechanism.",
            "changed_reading": None, "reader_inference": "Synthetic assumption boundary.",
            "containment": "Test fixture only; no semantic-quality claim."}


def response_for(packet, job):
    response = {"focus_ref": packet["focus_ref"], "trace_kind": "reconstructed",
            "baseline_models": [finding(packet)], "context_deltas": [], "surprising_valid_outliers": [],
            "summary": {"ordinary_reading": "Synthetic test summary.", "coexisting_readings": [], "unresolved_limits": []}}
    if job["protocol"] == w.LEGACY_JOB_PROTOCOL:
        response.update(protocol="hft-v2-response-v1", reader_id=job["reader_id"],
                        input_identity=copy.deepcopy(job["input_identity"]))
    return response


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="hft-v2-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.job_dir = self.root / "runs" / "fixture" / "2_1"
        self.packet = fixture_packet()
        self.job = w.write_job(self.job_dir, self.packet, [])
        self.reader_packet = w.read_json(self.job_dir / "packet.json")
        self.schema = w.read_json(self.job_dir / "response.schema.json")
        self.response = response_for(self.packet, self.job)

    def validate(self, response=None):
        w.validate_response(self.response if response is None else response, self.reader_packet, self.job, self.schema)

    def write_response(self):
        (self.job_dir / "response.json").write_bytes(w.json_bytes(self.response))

    def context_delta(self, *, branch=False):
        delta = finding(self.packet, "D1")
        delta["changed_reading"] = {"before": "Synthetic before.", "after": "Synthetic after."}
        if branch:
            delta["activation_trace"] = [{"source_ref": "2:2", "root": "ط ر ق", "source_word_indices": ["1"],
                "mapped_root_id": "root_shared", "branch_id": "B001", "variant_id": "V002", "role": "Synthetic role."}]
        else:
            delta["structural_cues"] = [{"source_ref": "2:3", "quote_ar": "غَيْبٌ", "role": "Synthetic structural trigger."}]
        return delta

    def test_split_targets_variants_and_shared_inventory(self):
        w.validate_packet(self.packet)
        self.assertEqual(len(self.packet["root_mappings"][0]["targets"]), 3)
        self.assertFalse(self.packet["root_mappings"][0]["targets"][1]["is_dominant"])
        self.assertEqual(len(self.packet["branch_inventory"]), 2)
        variants = self.packet["branch_inventory"][1]["branches"][0]["variants"]
        self.assertEqual([v["scope_ar"] for v in variants], ["نطاق أول", "نطاق ثان"])
        self.assertEqual([v["variant_id"] for v in variants], ["V001", "V002"])
        self.assertEqual(variants[1]["source_path"], "fixture/second")
        gaps = self.packet["source_gaps"]
        self.assertEqual(gaps["roots_without_branches"][0]["qac_root"], "غ ي ب")
        self.assertEqual(gaps["targets_without_branches"][0]["mapped_root_id"], "root_missing")

    def test_branchless_rooted_baseline_is_valid(self):
        self.validate()

    def test_structural_only_context_delta_is_valid(self):
        self.response["context_deltas"] = [self.context_delta()]
        self.validate()

    def test_rootless_context_is_citable_as_text(self):
        delta = self.context_delta()
        delta["structural_cues"][0].update(source_ref="2:4", quote_ar="حَرْفٌ")
        self.response["context_deltas"] = [delta]
        self.validate()

    def test_exact_variant_resolution_in_export_preserves_all_findings(self):
        self.response["context_deltas"] = [self.context_delta(branch=True)]
        outlier = finding(self.packet, "O1")
        outlier["status"] = "exploratory"
        self.response["surprising_valid_outliers"] = [outlier]
        self.validate()
        evidence = w.evidence_payload(self.job, self.packet, self.response)
        self.assertEqual(evidence["response"], self.response)
        self.assertEqual(len(evidence["resolved_evidence"]), 3)
        resolved = evidence["resolved_evidence"][1]["branches"][0]
        self.assertEqual(resolved["variant"]["scope_ar"], "نطاق ثان")
        self.assertEqual(resolved["source_occurrence"]["surfaces_ar"], ["طَرِيقٌ"])
        self.assertEqual(resolved["source_ayah_ar"], "طَرِيقٌ مُمْتَدٌّ")
        self.assertEqual(evidence["source_gaps"], self.packet["source_gaps"])
        self.assertFalse(evidence["execution_verified"])

    def test_non_dominant_target_is_citable(self):
        self.response["baseline_models"][0]["activation_trace"] = [{"source_ref": "2:1", "root": "أ ث ر",
            "source_word_indices": ["1"], "mapped_root_id": "root_shared", "branch_id": "B001",
            "variant_id": "V002", "role": "Synthetic non-dominant activation."}]
        self.validate()
        resolved = w.evidence_payload(self.job, self.packet, self.response)["resolved_evidence"][0]["branches"][0]
        self.assertFalse(resolved["mapping_target"]["is_dominant"])

    def test_reject_bad_citations(self):
        for field, value in [("source_ref", "2:5"), ("root", "أ ث ر"), ("source_word_indices", ["2"]),
                             ("mapped_root_id", "root_focus"), ("branch_id", "B999"), ("variant_id", "V999")]:
            with self.subTest(field=field):
                delta = self.context_delta(branch=True)
                delta["activation_trace"][0][field] = value
                self.response["context_deltas"] = [delta]
                with self.assertRaises(ValueError):
                    self.validate()

    def test_reject_inexact_quotes_and_orientation_citations(self):
        for ref, quote in [("2:3", "غيب"), ("2:5", "خَارِجٌ")]:
            delta = self.context_delta()
            delta["structural_cues"][0].update(source_ref=ref, quote_ar=quote)
            self.response["context_deltas"] = [delta]
            with self.assertRaises(ValueError):
                self.validate()
        self.response["context_deltas"] = []
        self.response["baseline_models"][0]["focus_anchor"]["quote_ar"] = "غَيْبٌ"
        with self.assertRaisesRegex(ValueError, "focus anchor"):
            self.validate()

    def test_baseline_cannot_borrow_context_branch(self):
        self.response["baseline_models"][0]["activation_trace"] = self.context_delta(branch=True)["activation_trace"]
        with self.assertRaisesRegex(ValueError, "baseline cites context"):
            self.validate()

    def test_delta_needs_context_and_actual_before_after(self):
        delta = self.context_delta()
        delta["structural_cues"] = []
        self.response["context_deltas"] = [delta]
        with self.assertRaisesRegex(ValueError, "no context evidence"):
            self.validate()
        delta["structural_cues"] = self.context_delta()["structural_cues"]
        delta["changed_reading"] = None
        with self.assertRaisesRegex(ValueError, "before/after"):
            self.validate()
        delta["changed_reading"] = {"before": "same", "after": "same"}
        with self.assertRaisesRegex(ValueError, "unchanged"):
            self.validate()

    def test_unique_ids_and_exploratory_outliers(self):
        outlier = finding(self.packet, "B1")
        outlier["status"] = "exploratory"
        self.response["surprising_valid_outliers"] = [outlier]
        with self.assertRaisesRegex(ValueError, "duplicate model_id"):
            self.validate()
        outlier.update(model_id="O1", status="supported")
        with self.assertRaisesRegex(ValueError, "exploratory"):
            self.validate()

    def test_reader_bookkeeping_and_legacy_response_rejected(self):
        for field, value in [("input_identity", self.job["input_identity"]), ("reader_id", "reader_fixture"),
                             ("protocol", w.RESPONSE_PROTOCOL)]:
            with self.subTest(field=field):
                response = copy.deepcopy(self.response)
                response[field] = value
                with self.assertRaisesRegex(ValueError, "unexpected fields"):
                    self.validate(response)
        legacy = copy.deepcopy(self.response)
        legacy["protocol"] = "focus-trace-hermetic-response-v4"
        with self.assertRaises(ValueError):
            self.validate(legacy)

    def test_changed_frozen_inputs_fail_before_response_validation(self):
        for filename in ["packet.json", "source.packet.json", "prompt.md", "response.schema.json"]:
            with self.subTest(filename=filename):
                path = self.job_dir / filename
                original = path.read_bytes()
                path.write_bytes(original + b" ")
                with self.assertRaisesRegex(ValueError, "frozen input changed"):
                    w.load_job(self.job_dir, require_response=False)
                path.write_bytes(original)
        w.load_job(self.job_dir, require_response=False)

    def test_missing_inventories_variants_roots_text_and_gaps_rejected(self):
        mutations = [
            lambda p: p.update(branch_inventory=[]),
            lambda p: p["branch_inventory"][1]["branches"][0]["variants"].pop(),
            lambda p: p["branch_inventory"][1]["branches"][0]["variants"][0].pop("scope_ar"),
            lambda p: p.update(root_mappings=[]),
            lambda p: p["ayat"][0].update(text_ar=""),
            lambda p: p["ayat"][0].update(root_occurrences=[]),
            lambda p: p["source_gaps"].update(roots_without_branches=[]),
            lambda p: p["source_gaps"].update(targets_without_branches=[]),
        ]
        for i, mutate in enumerate(mutations):
            with self.subTest(mutation=i):
                packet = copy.deepcopy(self.packet)
                mutate(packet)
                with self.assertRaises((ValueError, KeyError)):
                    w.validate_packet(packet)

    def test_changed_scope_with_same_ids_rejected_by_job_hash(self):
        altered = copy.deepcopy(self.reader_packet)
        altered["branch_inventory"][0]["branches"][0]["variants"][0]["scope_ar"] = "متغير"
        (self.job_dir / "packet.json").write_bytes(w.json_bytes(altered))
        with self.assertRaisesRegex(ValueError, "frozen input changed"):
            w.load_job(self.job_dir, require_response=False)

    def test_no_overwrite_and_missing_response_does_not_pass(self):
        with self.assertRaises(FileExistsError):
            w.write_job(self.job_dir, self.packet, [])
        self.assertIsNone(w.load_job(self.job_dir, require_response=False)[2])
        with self.assertRaises(FileNotFoundError):
            w.load_job(self.job_dir)
        (self.job_dir / "response.json").write_text("{}")
        with self.assertRaises(ValueError):
            w.load_job(self.job_dir, require_response=False)

    def test_model_profile_outside_frozen_reader_inputs(self):
        other_dir = self.root / "runs" / "sol" / "2_1"
        other = w.write_job(other_dir, self.packet, [], model="gpt-5.6-sol")
        self.assertEqual(other["input_identity"], self.job["input_identity"])
        for filename in ["packet.json", "prompt.md", "response.schema.json"]:
            self.assertEqual((self.job_dir / filename).read_bytes(), (other_dir / filename).read_bytes())
        self.assertFalse((self.job_dir / "assignment.json").exists())
        self.assertEqual(self.job["requested_profile"], {"model": "gpt-5.6-luna", "reasoning_effort": "max"})
        self.assertFalse(self.job["execution_verified"])

    def test_template_changes_do_not_change_frozen_job(self):
        with mock.patch.object(w, "WORKFLOW_ROOT", self.root / "nonexistent-templates"):
            w.load_job(self.job_dir, require_response=False)

    def test_reader_has_no_audit_metadata_but_coordinator_keeps_it(self):
        banned = {"protocol", "source_path", "root_id", "text_norm_ar", "rootless_reason", "mapping_status",
                  "qac_total_occurrences", "matched_occurrences", "unmapped_reason", "target_rank", "is_dominant",
                  "furuq_resolution", "target_occurrences", "branch_count", "variant_count", "frozen_root_norm",
                  "furuq_root_norm", "furuq_source_root_norm", "reader_id", "input_identity"}
        def keys(value):
            if isinstance(value, dict):
                for key, child in value.items():
                    yield key
                    yield from keys(child)
            elif isinstance(value, list):
                for child in value:
                    yield from keys(child)
        self.assertFalse(banned & set(keys(self.reader_packet)))
        self.assertEqual(w.read_json(self.job_dir / "source.packet.json"), self.packet)
        self.assertEqual(self.reader_packet["source_gaps"]["roots_without_branches"], ["غ ي ب"])
        self.assertEqual(self.reader_packet["source_gaps"]["targets_without_branches"],
                         [{"qac_root": "أ ث ر", "mapped_root_id": "root_missing"}])
        for name in ("prompt.md", "response.schema.json"):
            contents = (self.job_dir / name).read_text()
            for field in ("input_identity", "reader_id", "assignment.json", "sha256", "source_path"):
                self.assertNotIn(field, contents)

    def test_reader_keeps_english_all_variants_and_distinct_root_forms(self):
        projected = w.packet_index(self.reader_packet)[2]
        original = w.packet_index(self.packet)[2]
        self.assertEqual(set(projected), set(original))
        for key, variant in original.items():
            self.assertEqual(projected[key], {k: variant[k] for k in ("variant_id", *w.LINGUISTIC_VARIANT_FIELDS)})
        source = copy.deepcopy(self.packet)
        source["root_mappings"][0]["targets"][0].update(
            furuq_root_norm="أ ث ر", furuq_source_root_norm="غ ر ب", frozen_root_norm="غ ر ب")
        target = w.reader_packet(source)["root_mappings"][0]["targets"][0]
        self.assertEqual(target, {"furuq_root_id": "root_focus", "root_forms_ar": ["غ ر ب"]})

    def test_reader_projection_does_not_depend_on_audit_values(self):
        altered = copy.deepcopy(self.packet)
        altered["root_mappings"][0]["targets"][0].update(is_dominant=False, target_rank=999, target_occurrences=999)
        altered["root_mappings"][0].update(matched_occurrences=999, mapping_status="audit-only-change")
        altered["branch_inventory"][0]["branches"][0]["variants"][0]["source_path"] = "different/path"
        self.assertEqual(w.reader_packet(altered), self.reader_packet)

    def test_projection_check_catches_deletion_even_if_reader_hash_is_updated(self):
        altered = copy.deepcopy(self.reader_packet)
        altered["branch_inventory"].pop()
        data = w.json_bytes(altered)
        (self.job_dir / "packet.json").write_bytes(data)
        changed_job = copy.deepcopy(self.job)
        changed_job["input_identity"]["packet_sha256"] = w.digest(data)
        (self.job_dir / "job.json").write_bytes(w.json_bytes(changed_job))
        with self.assertRaisesRegex(ValueError, "complete source projection"):
            w.load_job(self.job_dir, require_response=False)

    def test_remote_orientation_retains_linguistic_evidence_without_repeated_labels(self):
        source = copy.deepcopy(self.packet)
        source["orientation"]["legacy_remote_snapshot"] = {
            "citable": False, "refs": ["2:5"], "root_cues": [{"root": "خ ر ج", "source_refs": ["2:5"],
                "targets": [{"mapped_root_id": "root_remote", "mapped_root_norm": "خ ر ج", "branches": [
                    {"branch_id": "B001", "branch_image_ar": "خروج", "scope_ar": "نطاق", "scope_en": "scope"}]}]}]}
        orientation = w.reader_packet(source)["orientation"]
        self.assertEqual(orientation["remote_refs"], ["2:5"])
        target = orientation["root_cues"][0]["targets"][0]
        self.assertNotIn("root_forms_ar", target)
        self.assertEqual(target["branches"][0]["scope_en"], "scope")
        source["orientation"]["legacy_remote_snapshot"]["unexpected"] = "unclassified content"
        with self.assertRaisesRegex(ValueError, "unrecognized remote"):
            w.reader_packet(source)

    def test_export_is_idempotent_refuses_overwrite_and_stays_isolated(self):
        self.write_response()
        with self.assertRaisesRegex(ValueError, "stay under"):
            w.export_job(self.job_dir)
        with mock.patch.object(w, "WORKFLOW_ROOT", self.root):
            output = w.export_job(self.job_dir)
            evidence = w.read_json(output)
            self.assertEqual(evidence["reader_id"], self.job["reader_id"])
            self.assertEqual(evidence["input_identity"], self.job["input_identity"])
            self.assertEqual(evidence["source_packet_sha256"], self.job["source_packet_sha256"])
            self.assertEqual(evidence["response"], self.response)
            before = output.read_bytes()
            self.assertEqual(w.export_job(self.job_dir).read_bytes(), before)
            self.response["summary"]["ordinary_reading"] = "Different synthetic summary."
            self.write_response()
            with self.assertRaisesRegex(ValueError, "different content"):
                w.export_job(self.job_dir)
            self.assertEqual(output.read_bytes(), before)

    def test_json_and_schema_fail_closed(self):
        for raw in ['{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}']:
            path = self.root / "invalid.json"
            path.write_text(raw)
            with self.assertRaises(ValueError):
                w.read_json(path)
        self.response["summary"]["unexpected"] = "not allowed"
        with self.assertRaisesRegex(ValueError, "unexpected fields"):
            self.validate()
        with self.assertRaisesRegex(ValueError, "unsupported schema"):
            w.validate_shape("value", {"type": "string", "maxLength": 1})
        with self.assertRaisesRegex(ValueError, "unsupported schema"):
            w.validate_shape([], {"type": "array", "items": {"type": "string", "maxLength": 1}})

    def test_window_parser_rejects_ambiguous_scope(self):
        self.assertEqual(w.parse_window("29:35-38"), ["29:35", "29:36", "29:37", "29:38"])
        self.assertEqual(w.parse_window("2:0,2:1-2"), ["2:0", "2:1", "2:2"])
        for value in ["29:38,29:38", "29:40-38", "../29:38", "29:1-999999999", "115:1"]:
            with self.assertRaises(ValueError):
                w.parse_window(value)

    def test_loader_retains_distinct_rows_and_excludes_contaminated_rows(self):
        db = self.root / "fixture.sqlite"
        with sqlite3.connect(db) as conn:
            conn.execute("CREATE TABLE branch_images (id INTEGER PRIMARY KEY, root_norm TEXT, root_id TEXT, source_path TEXT, branch_id TEXT, branch_image_ar TEXT, branch_image_en TEXT, what_is_ar TEXT, what_is_en TEXT, contaminated TEXT)")
            for i, (scope, contaminated) in enumerate([("نطاق أول", "no"), ("نطاق ثان", "no"), ("نطاق أول", "no"), ("ملوث", "yes")], 1):
                conn.execute("INSERT INTO branch_images VALUES (?,?,?,?,?,?,?,?,?,?)",
                             (i, "ج ذ ر", "root_fixture", "fixture/source", "B001", "صورة", "image", scope, "scope", contaminated))
        compressed = self.root / "fixture.sqlite.gz"
        with gzip.open(compressed, "wb") as handle:
            handle.write(db.read_bytes())
        mappings = {"ج ذ ر": mapping("ج ذ ر", [target("root_fixture"), target("root_absent", 2)])}
        raw, missing_roots, missing_targets = w.sources.load_branches_for_mapped_roots(compressed, mappings)
        _, inventory, gaps = w.project_inventory(mappings, raw)
        self.assertEqual(missing_roots, [])
        self.assertEqual(missing_targets[0]["furuq_root_id"], "root_absent")
        self.assertEqual([v["scope_ar"] for v in inventory[0]["branches"][0]["variants"]], ["نطاق أول", "نطاق ثان"])
        self.assertEqual(gaps["targets_without_branches"][0]["mapped_root_id"], "root_absent")


class ResourceRegressions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        required = [w.sources.DEFAULT_QAC, w.sources.DEFAULT_BRANCH_DB, w.sources.DEFAULT_QAC_FURUQ_ROOT_MAP,
                    w.sources.DEFAULT_QURAN_DIR / "surah_29.json", w.sources.DEFAULT_QURAN_DIR / "surah_83.json"]
        if not all(path.is_file() for path in required):
            raise unittest.SkipTest("local Quran/QAC/Furuq resources unavailable")
        cls.packets = {}
        for focus, window in [("29:38", "29:1-69"), ("83:1", "83:1-36")]:
            cls.packets[focus] = w.build_packet(focus, w.parse_window(window))

    def test_29_38_scopes_and_split_targets_are_retained(self):
        packet, _ = self.packets["29:38"]
        ayat, mappings, variants = w.packet_index(packet)
        eye = variants[("root_000672", "B010", "V001")]
        self.assertIn("العين", eye["image_ar"])
        self.assertIn("العنكبوت", eye["scope_ar"])
        self.assertIn("root_000989", {t["furuq_root_id"] for t in mappings["ع و د"]["targets"]})
        self.assertGreater(len(mappings["ع و د"]["targets"]), 1)
        focus_roots = {occ["root"] for occ in ayat["29:38"]["root_occurrences"]}
        context_targets = {t["furuq_root_id"] for root, m in mappings.items() if root not in focus_roots for t in m["targets"]}
        context_variants = [v for key, v in variants.items() if key[0] in context_targets]
        self.assertGreater(len(context_variants), 1000)
        self.assertTrue(all(v["scope_ar"] for v in context_variants))
        self.assertEqual({g["qac_root"] for g in packet["source_gaps"]["roots_without_branches"]}, {"ك ي ف", "ع ث و", "خ ط ط"})
        self.assertEqual(packet["source_gaps"]["ayat_without_qac_roots"], ["29:1"])

    def test_every_source_variant_and_mapping_survives_projection(self):
        for focus, (packet, _) in self.packets.items():
            with self.subTest(focus=focus):
                _, mappings, projected = w.packet_index(packet)
                original_mappings = w.sources.load_root_mappings(w.sources.DEFAULT_QAC_FURUQ_ROOT_MAP, list(mappings))
                raw, _, _ = w.sources.load_branches_for_mapped_roots(w.sources.DEFAULT_BRANCH_DB, original_mappings)
                expected = {(row["mapped_root_id"], row["branch_id"], w.json_bytes({k: v[k] for k in w.VARIANT_FIELDS}))
                            for rows in raw.values() for row in rows for v in row["variants"]}
                actual = {(key[0], key[1], w.json_bytes({k: v[k] for k in w.VARIANT_FIELDS})) for key, v in projected.items()}
                self.assertEqual(actual, expected)
                for root, original in original_mappings.items():
                    restored = copy.deepcopy(mappings[root])
                    for target in restored["targets"]:
                        target.pop("branch_count")
                        target.pop("variant_count")
                    self.assertEqual(restored, original)

    def test_reader_projection_preserves_all_29_38_and_83_1_linguistic_data(self):
        for focus, (source, _) in self.packets.items():
            with self.subTest(focus=focus):
                reader = w.reader_packet(source)
                self.assertEqual(reader["focus_ref"], source["focus_ref"])
                self.assertEqual(reader["window"], source["window"])
                for a, b in zip(source["ayat"], reader["ayat"]):
                    for key in ("ref", "text_ar", "root_sequence", "root_occurrences"):
                        self.assertEqual(a[key], b[key])
                original = w.packet_index(source)[2]
                projected = w.packet_index(reader)[2]
                self.assertEqual(set(original), set(projected))
                for key, variant in original.items():
                    self.assertEqual(projected[key], {k: variant[k] for k in ("variant_id", *w.LINGUISTIC_VARIANT_FIELDS)})
                for a, b in zip(source["root_mappings"], reader["root_mappings"]):
                    self.assertEqual(a["qac_root"], b["qac_root"])
                    self.assertEqual([t["furuq_root_id"] for t in a["targets"]], [t["furuq_root_id"] for t in b["targets"]])
                    for at, bt in zip(a["targets"], b["targets"]):
                        expected = {at[k] for k in ("frozen_root_norm", "furuq_root_norm", "furuq_source_root_norm") if at[k]}
                        self.assertLessEqual(expected, {a["qac_root"], *bt.get("root_forms_ar", [])})

    def test_original_frozen_v2_inputs_and_binding_are_still_supported(self):
        for ref in ("29_38", "83_1"):
            job_dir = w.WORKFLOW_ROOT / "runs/pilot-luna" / ref
            if not job_dir.is_dir():
                self.skipTest("original frozen v2 pilot inputs unavailable")
            job, packet, _ = w.load_job(job_dir, require_response=False)
            self.assertEqual(job["protocol"], w.LEGACY_JOB_PROTOCOL)
            schema = w.read_json(job_dir / "response.schema.json")
            response = response_for(packet, job)
            w.validate_response(response, packet, job, schema)
            response["input_identity"]["packet_sha256"] = "0" * 64
            with self.assertRaisesRegex(ValueError, "bound"):
                w.validate_response(response, packet, job, schema)

    def test_83_1_missing_inventory_allows_focus_text_not_borrowed_baseline_branch(self):
        packet, files = self.packets["83:1"]
        self.assertIn("ط ف ف", {g["qac_root"] for g in packet["source_gaps"]["roots_without_branches"]})
        with tempfile.TemporaryDirectory(prefix="hft-v2-83-1-") as temp:
            job_dir = Path(temp) / "83_1"
            job = w.write_job(job_dir, packet, files)
            response = response_for(packet, job)
            schema = w.read_json(job_dir / "response.schema.json")
            w.validate_response(response, packet, job, schema)
            response["context_deltas"] = [finding(packet, "D1")]
            delta = response["context_deltas"][0]
            delta["changed_reading"] = {"before": "Synthetic before.", "after": "Synthetic after."}
            delta["structural_cues"] = [{"source_ref": "83:2", "quote_ar": packet["ayat"][1]["text_ar"], "role": "Synthetic trigger."}]
            w.validate_response(response, packet, job, schema)
            response["baseline_models"][0]["structural_cues"] = delta["structural_cues"]
            with self.assertRaisesRegex(ValueError, "baseline cites context"):
                w.validate_response(response, packet, job, schema)

    def test_real_prepare_validate_export_pipeline_without_model(self):
        packet, files = self.packets["29:38"]
        with tempfile.TemporaryDirectory(prefix="hft-v2-e2e-") as temp:
            root = Path(temp)
            job_dir = root / "runs" / "fixture" / "29_38"
            job = w.write_job(job_dir, packet, files)
            response = response_for(packet, job)
            response["baseline_models"][0]["activation_trace"] = [{"source_ref": "29:38", "root": "س ب ل",
                "source_word_indices": ["14"], "mapped_root_id": "root_000672", "branch_id": "B010",
                "variant_id": "V001", "role": "Synthetic citation-resolution test, not an interpretation."}]
            (job_dir / "response.json").write_bytes(w.json_bytes(response))
            w.load_job(job_dir)
            with mock.patch.object(w, "WORKFLOW_ROOT", root):
                evidence = w.read_json(w.export_job(job_dir))
            self.assertIn("العنكبوت", evidence["resolved_evidence"][0]["branches"][0]["variant"]["scope_ar"])
            self.assertTrue(evidence["resolved_evidence"][0]["branches"][0]["variant"]["source_path"])
            self.assertEqual(evidence["response"], response)


if __name__ == "__main__":
    unittest.main()
