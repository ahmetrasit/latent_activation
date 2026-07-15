#!/usr/bin/env python3
"""Lightweight validation for GSLS 2.1 prepared inputs and work products."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from common import WORKFLOW_ID, ContractError, canonical_root, iter_jsonl, load_json, utc_now
from schema_validation import validate_instance


REQUIRED_INPUT_FILES = (
    "run-card.json",
    "passage-arabic.txt",
    "primary-scaffold.md",
    "morphology.tsv",
    "syntax.tsv",
    "lexical-branches.jsonl",
    "input-summary.json",
)

MORPHOLOGY_COLUMNS = {
    "surah",
    "ayah",
    "qac_ref",
    "surface_ar",
    "root_norm",
    "root_key",
    "context_role",
}

SYNTAX_COLUMNS = {"edge_id", "source_position", "target_position", "edge_type"}
REVIEW_VERDICTS = {"clean", "revision-required", "human-needed", "evidence-blocked"}


@dataclass
class Report:
    stage: str
    checks: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.errors

    def check(self, message: str) -> None:
        self.checks.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def to_dict(self) -> dict[str, Any]:
        return {
            "workflow_id": WORKFLOW_ID,
            "stage": self.stage,
            "validated_at": utc_now(),
            "status": "pass" if self.passed else "fail",
            "checks": self.checks,
            "warnings": self.warnings,
            "errors": self.errors,
        }


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def _schema(report: Report, path: Path, line_number: int, value: Any, name: str) -> None:
    for error in validate_instance(value, name):
        report.error(f"{path}:{line_number}: {error}")


def _load_object(report: Report, path: Path, schema_name: str) -> dict[str, Any] | None:
    try:
        value = load_json(path)
    except (OSError, json.JSONDecodeError) as error:
        report.error(f"Cannot read {path}: {error}")
        return None
    if not isinstance(value, dict):
        report.error(f"{path} must contain a JSON object")
        return None
    _schema(report, path, 1, value, schema_name)
    return value


def _passage_positions(report: Report, path: Path) -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
    all_positions: set[tuple[int, int]] = set()
    in_scope: set[tuple[int, int]] = set()
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        parts = line.split("\t", 2)
        if len(parts) != 3 or ":" not in parts[0] or not parts[2].strip():
            report.error(f"Invalid passage line {line_number}")
            continue
        try:
            position = tuple(int(value) for value in parts[0].split(":", 1))
        except ValueError:
            report.error(f"Invalid passage position at line {line_number}")
            continue
        if len(position) != 2 or position in all_positions:
            report.error(f"Duplicate or invalid passage position at line {line_number}")
            continue
        role = parts[1]
        if role not in {"in-scope", "opening-context"}:
            report.error(f"Invalid passage role at line {line_number}: {role}")
        all_positions.add(position)
        if role == "in-scope":
            in_scope.add(position)
    return all_positions, in_scope


def validate_inputs(run_root: Path) -> Report:
    run_root = run_root.resolve()
    report = Report("inputs")
    inputs = run_root / "inputs"
    for name in REQUIRED_INPUT_FILES:
        path = inputs / name
        if not path.is_file() or path.stat().st_size == 0:
            report.error(f"Missing or empty required input: {path}")
    if report.errors:
        return report

    card = _load_object(report, inputs / "run-card.json", "run-card")
    summary = _load_object(report, inputs / "input-summary.json", "input-summary")
    if card is None or summary is None:
        return report
    if card.get("workflow_id") != WORKFLOW_ID or summary.get("workflow_id") != WORKFLOW_ID:
        report.error("Prepared input workflow mismatch")
    if summary.get("run_id") != card.get("run_id"):
        report.error("Input summary run_id differs from the run card")
    if summary.get("quality_tier") != card.get("quality_tier"):
        report.error("Input summary quality tier differs from the run card")

    all_positions, in_scope_positions = _passage_positions(report, inputs / "passage-arabic.txt")
    scope = card.get("scope", {})
    try:
        expected_positions = {
            (int(scope["surah"]), ayah)
            for ayah in range(int(scope["ayah_start"]), int(scope["ayah_end"]) + 1)
        }
    except (KeyError, TypeError, ValueError):
        expected_positions = set()
        report.error("Run-card scope is invalid")
    if in_scope_positions != expected_positions:
        report.error("Passage positions do not match the run-card scope")
    passage_summary = summary.get("passage", {})
    if isinstance(passage_summary, dict):
        summary_scope = (
            passage_summary.get("surah"),
            passage_summary.get("ayah_start"),
            passage_summary.get("ayah_end"),
        )
        card_scope = (scope.get("surah"), scope.get("ayah_start"), scope.get("ayah_end"))
        if summary_scope != card_scope or passage_summary.get("positions") != len(all_positions):
            report.error("Input summary passage metadata differs from the prepared passage")
    report.check(f"Read {len(all_positions)} passage positions")

    try:
        morphology_header, morphology_rows = read_tsv(inputs / "morphology.tsv")
    except (OSError, csv.Error) as error:
        report.error(f"Cannot read morphology.tsv: {error}")
        morphology_header, morphology_rows = [], []
    missing_morphology = MORPHOLOGY_COLUMNS - set(morphology_header)
    if missing_morphology:
        report.error("morphology.tsv missing columns: " + ", ".join(sorted(missing_morphology)))
    passage_roots: set[str] = set()
    qac_refs: set[str] = set()
    for row_number, row in enumerate(morphology_rows, 2):
        try:
            position = (int(row.get("surah", "")), int(row.get("ayah", "")))
        except ValueError:
            report.error(f"morphology.tsv:{row_number}: invalid position")
            continue
        if position not in all_positions:
            report.error(f"morphology.tsv:{row_number}: position is outside the passage")
        qac_ref = row.get("qac_ref", "")
        if not qac_ref or qac_ref in qac_refs:
            report.error(f"morphology.tsv:{row_number}: missing or duplicate qac_ref")
        qac_refs.add(qac_ref)
        root_key = row.get("root_key", "")
        if root_key:
            passage_roots.add(root_key)
            if root_key != canonical_root(row.get("root_norm", "")):
                report.error(f"morphology.tsv:{row_number}: noncanonical root_key")
    if not morphology_rows or not passage_roots:
        report.error("Prepared morphology has no rooted passage rows")
    report.check(f"Read {len(morphology_rows)} morphology rows across {len(passage_roots)} roots")

    try:
        syntax_header, syntax_rows = read_tsv(inputs / "syntax.tsv")
    except (OSError, csv.Error) as error:
        report.error(f"Cannot read syntax.tsv: {error}")
        syntax_header, syntax_rows = [], []
    missing_syntax = SYNTAX_COLUMNS - set(syntax_header)
    if missing_syntax:
        report.error("syntax.tsv missing columns: " + ", ".join(sorted(missing_syntax)))
    edge_ids = [row.get("edge_id", "") for row in syntax_rows]
    if any(not edge_id for edge_id in edge_ids) or len(edge_ids) != len(set(edge_ids)):
        report.error("syntax.tsv contains a missing or duplicate edge_id")
    report.check(f"Read {len(syntax_rows)} syntax edges")

    lexical_records: list[dict[str, Any]] = []
    lexical_ids: set[tuple[str, str]] = set()
    accepted_roots: set[str] = set()
    try:
        for line_number, record in iter_jsonl(inputs / "lexical-branches.jsonl"):
            lexical_records.append(record)
            _schema(report, inputs / "lexical-branches.jsonl", line_number, record, "lexical-branch")
            root_id = record.get("root_id")
            branch_id = record.get("branch_id")
            lexical_id = (str(root_id or ""), str(branch_id or ""))
            if not all(lexical_id) or lexical_id in lexical_ids:
                report.error(f"lexical-branches.jsonl:{line_number}: missing or duplicate root_id/branch_id")
            else:
                lexical_ids.add(lexical_id)
            root_norm = record.get("root_norm")
            if isinstance(root_norm, str):
                accepted_roots.add(canonical_root(root_norm))
    except (OSError, json.JSONDecodeError, ContractError) as error:
        report.error(str(error))
    missing_roots = passage_roots - accepted_roots
    if missing_roots:
        report.error("Passage roots without accepted lexical branches: " + ", ".join(sorted(missing_roots)))
    lexical_summary = summary.get("lexical", {})
    if not isinstance(lexical_summary, dict):
        report.error("Input summary lexical section is invalid")
    else:
        expected_filter = (
            "database-contaminated-equals-no"
            if lexical_summary.get("mode") == "database"
            else "fallback-accepted-clean-export"
        )
        if lexical_summary.get("contamination_filter") != expected_filter:
            report.error("Input summary has the wrong lexical contamination filter")
        if lexical_summary.get("rows") != len(lexical_records):
            report.error("Input summary lexical count differs from lexical-branches.jsonl")
    report.check(f"Read {len(lexical_records)} accepted lexical branches")

    if card.get("quality_tier") == "source-limited":
        report.warn("A fallback source is active; this run remains source-limited")
    return report


def _validate_synthesis(run_root: Path, stage: str, jsonl_name: str, markdown_name: str) -> Report:
    report = Report(stage)
    directory = run_root / "agent-a" / ("draft" if stage == "draft" else "final")
    jsonl_path = directory / jsonl_name
    markdown_path = directory / markdown_name
    findings: list[dict[str, Any]] = []
    try:
        for line_number, finding in iter_jsonl(jsonl_path):
            findings.append(finding)
            _schema(report, jsonl_path, line_number, finding, "synthesis-finding")
    except (OSError, json.JSONDecodeError, ContractError) as error:
        report.error(str(error))
    if not findings:
        report.error(f"No synthesis findings in {jsonl_path}")
    finding_ids = [finding.get("finding_id") for finding in findings]
    if any(not isinstance(value, str) or not value for value in finding_ids):
        report.error("Every synthesis finding requires a finding_id")
    elif len(finding_ids) != len(set(finding_ids)):
        report.error("Synthesis finding IDs must be unique")
    if not markdown_path.is_file() or not markdown_path.read_text(encoding="utf-8").strip():
        report.error(f"Missing or empty synthesis notebook: {markdown_path}")
    report.check(f"Read {len(findings)} substantive synthesis findings")
    return report


def validate_draft(run_root: Path) -> Report:
    return _validate_synthesis(run_root.resolve(), "draft", "draft-synthesis.jsonl", "draft-synthesis.md")


def validate_review(run_root: Path, expected_verdict: str | None = None) -> Report:
    report = Report("review")
    path = run_root.resolve() / "agent-b" / "review.md"
    if not path.is_file():
        report.error(f"Missing review: {path}")
        return report
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        report.error(f"Empty review: {path}")
        return report
    first_line = text.splitlines()[0].strip()
    verdict = first_line.removeprefix("VERDICT:").strip() if first_line.startswith("VERDICT:") else ""
    if verdict not in REVIEW_VERDICTS:
        report.error("Review must begin with VERDICT: clean, revision-required, human-needed, or evidence-blocked")
    if expected_verdict is not None and verdict != expected_verdict:
        report.error(f"Review verdict {verdict!r} does not match transition {expected_verdict!r}")
    if verdict == "revision-required" and ("TARGET:" not in text or "REQUIRED CHANGE:" not in text):
        report.error("A revision-required review must identify a target and required change")
    report.check(f"Read substantive review with verdict {verdict or 'invalid'}")
    return report


def validate_final(run_root: Path) -> Report:
    return _validate_synthesis(run_root.resolve(), "final", "final-synthesis.jsonl", "final-synthesis.md")


def validate_publication(run_root: Path) -> Report:
    run_root = run_root.resolve()
    report = Report("publication")
    final_report = validate_final(run_root)
    report.errors.extend(f"Final prerequisite: {error}" for error in final_report.errors)
    path = run_root / "agent-c" / "publication.md"
    if not path.is_file() or not path.read_text(encoding="utf-8").strip():
        report.error(f"Missing or empty publication rendering: {path}")
    else:
        report.check("Read publication rendering")
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_root", type=Path)
    parser.add_argument(
        "--stage",
        choices=("inputs", "draft", "review", "final", "publication", "all"),
        default="all",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_root = args.run_root.resolve()
    validators = {
        "inputs": validate_inputs,
        "draft": validate_draft,
        "review": validate_review,
        "final": validate_final,
        "publication": validate_publication,
    }
    selected = list(validators) if args.stage == "all" else [args.stage]
    results: list[dict[str, Any]] = []
    passed = True
    try:
        for stage in selected:
            report = validators[stage](run_root)
            results.append(report.to_dict())
            passed = passed and report.passed
    except (ContractError, OSError, ValueError, json.JSONDecodeError) as error:
        print(f"validate_run: ERROR: {error}", file=sys.stderr)
        return 1
    print(json.dumps(results[0] if len(results) == 1 else results, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
