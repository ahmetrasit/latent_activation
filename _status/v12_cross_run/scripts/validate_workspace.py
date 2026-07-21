#!/usr/bin/env python3
"""Validate a v12 cross-run surah workspace.

Structural mode permits incomplete production but rejects malformed or
internally inconsistent rows. Strict mode additionally closes lineage,
coverage, lexical, publication, and non-loss invariants.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Iterable


SCRIPT_PATH = Path(__file__).resolve()
PACKAGE_ROOT = SCRIPT_PATH.parents[1]
REPO_ROOT = SCRIPT_PATH.parents[3]
TEMPLATE_ROOT = PACKAGE_ROOT / "schema" / "templates"

REQUIRED_TABLES = (
    "runs.tsv",
    "source_findings.tsv",
    "claims.tsv",
    "claim_sources.tsv",
    "branch_evidence.tsv",
    "coverage.tsv",
)
OPTIONAL_TABLES = ("stage_status.tsv",)

AYAH_RE = re.compile(r"^[1-9][0-9]*:[0-9]+$")
BRANCH_RE = re.compile(r"^B[0-9]{3}$")
HASH_RE = re.compile(r"^[0-9a-f]{64}$")

PROVENANCE = {"frozen", "reconstructed_verified", "reconstructed_unverified"}
FINDING_TYPES = {"activated_reading", "retrospective_surprise"}
READER_STRENGTHS = {"asserted", "qualified", "exploratory"}
DISPOSITIONS = {
    "unreviewed",
    "accepted",
    "merged",
    "split",
    "evidence_only",
    "deferred",
    "rejected",
    "conflict",
}
CROSS_RUN_RELATIONS = {
    "shared_mechanism",
    "standard_only",
    "eleven_ayah_only",
    "compatible_refinement",
    "material_conflict",
}
PUBLICATION_ROLES = {
    "unreviewed",
    "primary",
    "secondary",
    "exploratory",
    "evidence_only",
    "none",
}
SOURCE_RELATIONS = {
    "supports",
    "refines",
    "reinforces",
    "split_component",
    "counterevidence",
    "rejected_basis",
}
INVENTORY_MATCH = {"yes", "no", "unknown"}
FIT_VALUES = {"exact", "compatible", "mismatch", "unknown"}
EVIDENCE_ROLES = {
    "lexical_anchor",
    "context_support",
    "target_root_resonance",
    "counterevidence",
}
LEXICAL_STATUSES = {
    "direct",
    "contextually_activated",
    "analogical_resonance",
    "unlicensed",
}
TRANSLATION_ROLES = {"governing", "modifier", "none"}
RESONANCE_ELIGIBILITY = {"yes", "no", "not_applicable"}
RESONANCE_STRENGTHS = {"strong", "moderate", "weak", "none"}
TRANSLATION_VISIBILITY = {
    "commentary_and_translation",
    "commentary_only",
    "evidence_only",
    "none",
}
STAGES = {
    "provenance",
    "extract",
    "normalize",
    "grade",
    "reconcile",
    "publish",
    "audit",
    "handoff",
}
STAGE_STATUSES = {"pending", "running", "complete", "failed"}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def label(table: str, row: dict[str, str]) -> str:
    return f"{table}:{row.get('_line', '?')}"


def split_scalar(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def enum_value(
    report: Report,
    table: str,
    row: dict[str, str],
    field: str,
    allowed: set[str],
) -> None:
    value = row[field]
    if value not in allowed:
        report.error(
            f"{label(table, row)}: {field}={value!r}; expected one of "
            f"{', '.join(sorted(allowed))}"
        )


def require_fields(
    report: Report,
    table: str,
    row: dict[str, str],
    fields: Iterable[str],
) -> None:
    for field in fields:
        if not row[field].strip():
            report.error(f"{label(table, row)}: required field {field} is blank")


def expected_header(filename: str, report: Report) -> list[str]:
    path = TEMPLATE_ROOT / filename
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle, delimiter="\t"))
    except OSError as exc:
        report.error(f"cannot read schema template {path}: {exc}")
        return []
    if len(rows) != 1:
        report.error(f"schema template {path} must contain exactly one header row")
        return rows[0] if rows else []
    return rows[0]


def load_table(
    workspace: Path,
    filename: str,
    report: Report,
    required: bool,
) -> list[dict[str, str]]:
    path = workspace / filename
    if not path.exists():
        if required:
            report.error(f"missing required table: {path}")
        return []

    wanted = expected_header(filename, report)
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            raw_rows = list(csv.reader(handle, delimiter="\t"))
    except (OSError, UnicodeError) as exc:
        report.error(f"cannot read {path}: {exc}")
        return []

    if not raw_rows:
        report.error(f"{path}: file is empty")
        return []
    if raw_rows[0] != wanted:
        report.error(
            f"{path}: header differs from canonical template;\n"
            f"  actual:   {raw_rows[0]}\n  expected: {wanted}"
        )

    rows: list[dict[str, str]] = []
    for line_number, values in enumerate(raw_rows[1:], start=2):
        if not any(values):
            report.error(f"{filename}:{line_number}: blank row is not allowed")
            continue
        if len(values) != len(wanted):
            report.error(
                f"{filename}:{line_number}: has {len(values)} columns; "
                f"expected {len(wanted)}"
            )
        padded = (values + [""] * len(wanted))[: len(wanted)]
        row = dict(zip(wanted, padded))
        row["_line"] = str(line_number)
        rows.append(row)
    return rows


def index_unique(
    report: Report,
    table: str,
    rows: list[dict[str, str]],
    field: str,
) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row[field]
        if not value:
            continue
        if value in result:
            report.error(
                f"{label(table, row)}: duplicate {field}={value!r}; first seen at "
                f"line {result[value]['_line']}"
            )
        else:
            result[value] = row
    return result


def resolve_repo_path(raw: str, report: Report, context: str) -> Path | None:
    if not raw:
        return None
    path = Path(raw)
    if path.is_absolute():
        report.error(f"{context}: path must be repository-relative: {raw}")
        return None
    resolved = (REPO_ROOT / path).resolve()
    try:
        resolved.relative_to(REPO_ROOT.resolve())
    except ValueError:
        report.error(f"{context}: path escapes repository: {raw}")
        return None
    return resolved


def parse_pointer(raw: str) -> tuple[str, int] | None:
    path, separator, line_text = raw.rpartition(":")
    if not separator or not path or not line_text.isdigit():
        return None
    line_number = int(line_text)
    if line_number < 1:
        return None
    return path, line_number


def validate_pointer(
    raw: str,
    report: Report,
    context: str,
    line_counts: dict[Path, int],
) -> None:
    parsed = parse_pointer(raw)
    if parsed is None:
        report.error(f"{context}: expected repository/path:line pointer, got {raw!r}")
        return
    raw_path, line_number = parsed
    path = resolve_repo_path(raw_path, report, context)
    if path is None:
        return
    if not path.is_file():
        report.error(f"{context}: pointer target does not exist: {raw_path}")
        return
    if path not in line_counts:
        try:
            with path.open("r", encoding="utf-8") as handle:
                line_counts[path] = sum(1 for _ in handle)
        except (OSError, UnicodeError) as exc:
            report.error(f"{context}: cannot count lines in {raw_path}: {exc}")
            return
    if line_number > line_counts[path]:
        report.error(
            f"{context}: line {line_number} exceeds {raw_path} "
            f"({line_counts[path]} lines)"
        )


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_blob(revision: str, raw_path: str) -> bytes | None:
    result = subprocess.run(
        ["git", "show", f"{revision}:{raw_path}"],
        cwd=REPO_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return result.stdout if result.returncode == 0 else None


def validate_hash(
    report: Report,
    context: str,
    raw_path: str,
    recorded_hash: str,
    revision: str = "",
) -> None:
    if bool(raw_path) != bool(recorded_hash):
        report.error(f"{context}: path and sha256 must either both be set or both be blank")
        return
    if not raw_path:
        return
    if not HASH_RE.fullmatch(recorded_hash):
        report.error(f"{context}: invalid SHA-256 value {recorded_hash!r}")
        return

    historical_match = False
    if revision:
        blob = git_blob(revision, raw_path)
        if blob is None:
            report.error(f"{context}: cannot resolve {raw_path} at git revision {revision}")
        else:
            actual = sha256_bytes(blob)
            if actual != recorded_hash:
                report.error(
                    f"{context}: historical hash mismatch at {revision}; "
                    f"recorded {recorded_hash}, actual {actual}"
                )
            else:
                historical_match = True

    path = resolve_repo_path(raw_path, report, context)
    if path is None:
        return
    if not path.is_file():
        if not historical_match:
            report.error(f"{context}: artifact does not exist: {raw_path}")
        else:
            report.warn(f"{context}: artifact exists only at recorded revision {revision}")
        return
    try:
        current_hash = sha256_file(path)
    except OSError as exc:
        report.error(f"{context}: cannot hash {raw_path}: {exc}")
        return
    if current_hash != recorded_hash:
        if historical_match:
            report.warn(
                f"{context}: working-tree artifact has drifted; recorded revision "
                f"{revision} preserves the expected hash"
            )
        else:
            report.error(
                f"{context}: hash mismatch; recorded {recorded_hash}, "
                f"actual {current_hash}"
            )


def validate_ayah_list(report: Report, raw: str, context: str) -> None:
    for ref in split_scalar(raw):
        if not AYAH_RE.fullmatch(ref):
            report.error(f"{context}: invalid ayah reference {ref!r}")


def normalize_branch(root: str, branch: str) -> str:
    return f"{' '.join(root.split())}:{branch.strip()}"


def claimed_branch(raw: str) -> str | None:
    root, separator, branch = raw.rpartition(":")
    if not separator or not root.strip() or not BRANCH_RE.fullmatch(branch):
        return None
    return normalize_branch(root, branch)


def validate_runs(
    rows: list[dict[str, str]], report: Report
) -> dict[str, dict[str, str]]:
    runs = index_unique(report, "runs.tsv", rows, "run_id")
    for row in rows:
        context = label("runs.tsv", row)
        require_fields(
            report,
            "runs.tsv",
            row,
            (
                "run_id",
                "treatment",
                "reader_id",
                "prompt_path",
                "prompt_sha256",
                "packet_path",
                "packet_sha256",
                "output_path",
                "output_sha256",
                "visible_refs",
                "provenance_status",
            ),
        )
        enum_value(report, "runs.tsv", row, "provenance_status", PROVENANCE)
        validate_ayah_list(report, row["visible_refs"], f"{context} visible_refs")
        validate_hash(
            report,
            f"{context} prompt",
            row["prompt_path"],
            row["prompt_sha256"],
            row["prompt_revision"],
        )
        validate_hash(
            report,
            f"{context} packet",
            row["packet_path"],
            row["packet_sha256"],
        )
        validate_hash(
            report,
            f"{context} output",
            row["output_path"],
            row["output_sha256"],
            row["output_revision"],
        )
        validate_hash(
            report,
            f"{context} frozen manifest",
            row["frozen_manifest_path"],
            row["frozen_manifest_sha256"],
        )

        if row["provenance_status"] == "frozen":
            if not row["frozen_manifest_path"]:
                report.error(f"{context}: frozen provenance requires a frozen manifest")
            else:
                manifest_path = resolve_repo_path(
                    row["frozen_manifest_path"], report, f"{context} manifest"
                )
                if manifest_path and manifest_path.is_file():
                    try:
                        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
                        report.error(f"{context}: cannot parse frozen manifest: {exc}")
                    else:
                        expected = {
                            "reader_id": row["reader_id"],
                            "packet": row["packet_path"],
                            "packet_sha256": row["packet_sha256"],
                            "prompt": row["prompt_path"],
                            "prompt_sha256": row["prompt_sha256"],
                            "output_file": row["output_path"],
                            "output_file_sha256": row["output_sha256"],
                        }
                        for field, value in expected.items():
                            if manifest.get(field) != value:
                                report.error(
                                    f"{context}: manifest {field} mismatch; "
                                    f"expected {value!r}, got {manifest.get(field)!r}"
                                )
        if row["provenance_status"] == "reconstructed_unverified" and not row[
            "notes"
        ].strip():
            report.error(f"{context}: unverified provenance requires explanatory notes")
    return runs


def validate_source_findings(
    rows: list[dict[str, str]],
    runs: dict[str, dict[str, str]],
    report: Report,
    strict: bool,
    line_counts: dict[Path, int],
) -> dict[str, dict[str, str]]:
    findings = index_unique(report, "source_findings.tsv", rows, "source_finding_id")
    for row in rows:
        context = label("source_findings.tsv", row)
        require_fields(
            report,
            "source_findings.tsv",
            row,
            (
                "source_finding_id",
                "run_id",
                "fixed_ayah_ref",
                "finding_type",
                "source_pointer",
                "finding_title",
                "reader_strength",
                "disposition",
            ),
        )
        if row["run_id"] not in runs:
            report.error(f"{context}: unknown run_id {row['run_id']!r}")
        if row["fixed_ayah_ref"] and not AYAH_RE.fullmatch(row["fixed_ayah_ref"]):
            report.error(f"{context}: invalid fixed_ayah_ref {row['fixed_ayah_ref']!r}")
        enum_value(report, "source_findings.tsv", row, "finding_type", FINDING_TYPES)
        enum_value(
            report, "source_findings.tsv", row, "reader_strength", READER_STRENGTHS
        )
        enum_value(report, "source_findings.tsv", row, "disposition", DISPOSITIONS)
        if row["source_pointer"]:
            validate_pointer(row["source_pointer"], report, context, line_counts)
        validate_ayah_list(report, row["support_refs"], f"{context} support_refs")
        for item in split_scalar(row["claimed_branches"]):
            if claimed_branch(item) is None:
                report.error(f"{context}: invalid claimed branch {item!r}")
        if strict and row["disposition"] == "unreviewed":
            report.error(f"{context}: strict audit forbids unreviewed findings")
        if row["disposition"] in {"rejected", "deferred", "conflict"} and not row[
            "notes"
        ].strip():
            report.error(f"{context}: {row['disposition']} finding requires notes")
    return findings


def validate_claims(
    rows: list[dict[str, str]], report: Report, strict: bool
) -> dict[str, dict[str, str]]:
    claims = index_unique(report, "claims.tsv", rows, "claim_id")
    for row in rows:
        context = label("claims.tsv", row)
        require_fields(
            report,
            "claims.tsv",
            row,
            (
                "claim_id",
                "ayah_ref",
                "mechanism",
                "cross_run_relation",
                "publication_role",
                "disposition",
            ),
        )
        if row["ayah_ref"] and not AYAH_RE.fullmatch(row["ayah_ref"]):
            report.error(f"{context}: invalid ayah_ref {row['ayah_ref']!r}")
        enum_value(
            report, "claims.tsv", row, "cross_run_relation", CROSS_RUN_RELATIONS
        )
        enum_value(report, "claims.tsv", row, "publication_role", PUBLICATION_ROLES)
        enum_value(report, "claims.tsv", row, "disposition", DISPOSITIONS)

        role = row["publication_role"]
        disposition = row["disposition"]
        if disposition == "rejected" and role != "none":
            report.error(f"{context}: rejected claim must use publication_role=none")
        if disposition == "accepted" and role in {"none", "unreviewed"}:
            report.error(f"{context}: accepted claim requires a public or evidence role")
        if disposition == "evidence_only" and role != "evidence_only":
            report.error(
                f"{context}: evidence_only disposition requires "
                "publication_role=evidence_only"
            )
        if (disposition != "unreviewed" or role != "unreviewed") and not row[
            "decision_reason"
        ].strip():
            report.error(f"{context}: reviewed claim requires decision_reason")
        if strict and (disposition == "unreviewed" or role == "unreviewed"):
            report.error(f"{context}: strict audit forbids unreviewed claims")
    return claims


def validate_claim_sources(
    rows: list[dict[str, str]],
    claims: dict[str, dict[str, str]],
    findings: dict[str, dict[str, str]],
    report: Report,
) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    claims_by_source: dict[str, set[str]] = defaultdict(set)
    sources_by_claim: dict[str, set[str]] = defaultdict(set)
    seen: set[tuple[str, str, str]] = set()
    for row in rows:
        context = label("claim_sources.tsv", row)
        require_fields(
            report,
            "claim_sources.tsv",
            row,
            ("claim_id", "source_finding_id", "source_relation"),
        )
        enum_value(
            report, "claim_sources.tsv", row, "source_relation", SOURCE_RELATIONS
        )
        claim_id = row["claim_id"]
        finding_id = row["source_finding_id"]
        if claim_id not in claims:
            report.error(f"{context}: unknown claim_id {claim_id!r}")
        if finding_id not in findings:
            report.error(f"{context}: unknown source_finding_id {finding_id!r}")
        key = (claim_id, finding_id, row["source_relation"])
        if key in seen:
            report.error(f"{context}: duplicate claim/source/relation row {key}")
        seen.add(key)
        claims_by_source[finding_id].add(claim_id)
        sources_by_claim[claim_id].add(finding_id)
    return claims_by_source, sources_by_claim


def score_bucket(score: int) -> str:
    if score >= 8:
        return "strong"
    if score >= 5:
        return "moderate"
    return "weak"


def validate_branch_evidence(
    rows: list[dict[str, str]],
    claims: dict[str, dict[str, str]],
    report: Report,
    line_counts: dict[Path, int],
) -> tuple[dict[str, list[dict[str, str]]], dict[str, set[str]]]:
    index_unique(report, "branch_evidence.tsv", rows, "evidence_id")
    evidence_by_claim: dict[str, list[dict[str, str]]] = defaultdict(list)
    branches_by_claim: dict[str, set[str]] = defaultdict(set)
    score_fields = (
        "trigger_score",
        "proximity_score",
        "structure_score",
        "reading_gain_score",
        "robustness_score",
    )

    for row in rows:
        context = label("branch_evidence.tsv", row)
        require_fields(
            report,
            "branch_evidence.tsv",
            row,
            (
                "evidence_id",
                "claim_id",
                "occurrence_ref",
                "word_index",
                "word_id",
                "morpheme_id",
                "surface",
                "lemma",
                "pos",
                "root",
                "branch",
                "inventory_match",
                "form_fit",
                "construction_fit",
                "evidence_role",
                "lexical_status",
                "translation_role",
                "resonance_eligible",
                "resonance_strength",
                "decision_reason",
            ),
        )
        claim_id = row["claim_id"]
        claim = claims.get(claim_id)
        if claim is None:
            report.error(f"{context}: unknown claim_id {claim_id!r}")
        else:
            evidence_by_claim[claim_id].append(row)
        if not AYAH_RE.fullmatch(row["occurrence_ref"]):
            report.error(f"{context}: invalid occurrence_ref {row['occurrence_ref']!r}")
        try:
            word_index = int(row["word_index"])
            if word_index < 1:
                raise ValueError
        except ValueError:
            report.error(f"{context}: word_index must be a positive integer")
        else:
            if AYAH_RE.fullmatch(row["occurrence_ref"]):
                surah, ayah = (
                    int(value) for value in row["occurrence_ref"].split(":", 1)
                )
                expected_word_id = (
                    f"w-s{surah:03d}-a{ayah:03d}-w{word_index:03d}"
                )
                if row["word_id"] != expected_word_id:
                    report.error(
                        f"{context}: word_id={row['word_id']!r}; expected {expected_word_id}"
                    )
                if not row["morpheme_id"].startswith(f"m-{expected_word_id}-"):
                    report.error(
                        f"{context}: morpheme_id does not belong to {expected_word_id}"
                    )
        if not BRANCH_RE.fullmatch(row["branch"]):
            report.error(f"{context}: invalid branch {row['branch']!r}")
        else:
            branches_by_claim[claim_id].add(normalize_branch(row["root"], row["branch"]))
        if row["inventory_pointer"]:
            validate_pointer(row["inventory_pointer"], report, context, line_counts)
        enum_value(
            report, "branch_evidence.tsv", row, "inventory_match", INVENTORY_MATCH
        )
        enum_value(report, "branch_evidence.tsv", row, "form_fit", FIT_VALUES)
        enum_value(report, "branch_evidence.tsv", row, "construction_fit", FIT_VALUES)
        enum_value(
            report, "branch_evidence.tsv", row, "evidence_role", EVIDENCE_ROLES
        )
        enum_value(
            report, "branch_evidence.tsv", row, "lexical_status", LEXICAL_STATUSES
        )
        enum_value(
            report, "branch_evidence.tsv", row, "translation_role", TRANSLATION_ROLES
        )
        enum_value(
            report,
            "branch_evidence.tsv",
            row,
            "resonance_eligible",
            RESONANCE_ELIGIBILITY,
        )
        enum_value(
            report,
            "branch_evidence.tsv",
            row,
            "resonance_strength",
            RESONANCE_STRENGTHS,
        )
        validate_ayah_list(report, row["support_refs"], f"{context} support_refs")
        for support_id in split_scalar(row["linguistic_support_ids"]):
            if not re.fullmatch(r"(?:sx|co)-[A-Za-z0-9_-]+", support_id):
                report.error(
                    f"{context}: invalid linguistic_support_id {support_id!r}"
                )

        status = row["lexical_status"]
        translation = row["translation_role"]
        if row["inventory_match"] == "yes" and not row["inventory_pointer"]:
            report.error(f"{context}: inventory_match=yes requires inventory_pointer")
        if status in {"direct", "contextually_activated", "analogical_resonance"}:
            if row["inventory_match"] != "yes":
                report.error(f"{context}: {status} requires inventory_match=yes")
        if status in {"direct", "contextually_activated"}:
            if row["form_fit"] not in {"exact", "compatible"}:
                report.error(f"{context}: {status} requires exact/compatible form_fit")
            if row["construction_fit"] not in {"exact", "compatible"}:
                report.error(
                    f"{context}: {status} requires exact/compatible construction_fit"
                )
            if row["resonance_eligible"] != "not_applicable":
                report.error(
                    f"{context}: {status} requires resonance_eligible=not_applicable"
                )
            if row["resonance_strength"] != "none":
                report.error(f"{context}: {status} requires resonance_strength=none")
        if status == "analogical_resonance":
            if row["resonance_eligible"] != "yes":
                report.error(
                    f"{context}: analogical_resonance requires resonance_eligible=yes"
                )
            if translation != "none":
                report.error(f"{context}: analogical resonance cannot enter translation")
            if not row["counterevidence"].strip():
                report.error(
                    f"{context}: analogical resonance requires explicit counterevidence"
                )
            values: list[int] = []
            for field in score_fields:
                try:
                    value = int(row[field])
                except ValueError:
                    report.error(f"{context}: {field} must be an integer from 0 to 2")
                    continue
                if value < 0 or value > 2:
                    report.error(f"{context}: {field} must be from 0 to 2")
                values.append(value)
            if len(values) == len(score_fields):
                total = sum(values)
                try:
                    recorded_total = int(row["resonance_score"])
                except ValueError:
                    report.error(f"{context}: resonance_score must be an integer")
                else:
                    if recorded_total != total:
                        report.error(
                            f"{context}: resonance_score={recorded_total}, "
                            f"but components sum to {total}"
                        )
                expected_strength = score_bucket(total)
                if row["resonance_strength"] != expected_strength:
                    report.error(
                        f"{context}: score {total} requires "
                        f"resonance_strength={expected_strength}"
                    )
        elif status == "unlicensed":
            if row["resonance_eligible"] != "no":
                report.error(f"{context}: unlicensed requires resonance_eligible=no")
            if translation != "none":
                report.error(f"{context}: unlicensed evidence cannot enter translation")
            if row["resonance_strength"] != "none":
                report.error(f"{context}: unlicensed requires resonance_strength=none")
            if not row["counterevidence"].strip():
                report.error(f"{context}: unlicensed evidence requires counterevidence")

        if status != "analogical_resonance":
            for field in (*score_fields, "resonance_score"):
                if row[field].strip():
                    report.error(f"{context}: {status} must leave {field} blank")

        if translation == "governing" and status != "direct":
            report.error(f"{context}: governing translation requires direct evidence")
        if translation == "modifier" and status not in {
            "direct",
            "contextually_activated",
        }:
            report.error(
                f"{context}: modifier translation requires direct/contextual evidence"
            )
        if claim is not None and translation != "none" and row["occurrence_ref"] != claim[
            "ayah_ref"
        ]:
            report.error(
                f"{context}: translation-visible evidence must occur in the claim ayah"
            )
        if claim is not None and row["evidence_role"] == "lexical_anchor" and row[
            "occurrence_ref"
        ] != claim["ayah_ref"]:
            report.error(f"{context}: lexical_anchor must occur in the claim ayah")
    return evidence_by_claim, branches_by_claim


def validate_coverage(
    rows: list[dict[str, str]],
    findings: dict[str, dict[str, str]],
    claims: dict[str, dict[str, str]],
    claims_by_source: dict[str, set[str]],
    report: Report,
    strict: bool,
) -> dict[str, dict[str, str]]:
    coverage = index_unique(report, "coverage.tsv", rows, "source_finding_id")
    for row in rows:
        context = label("coverage.tsv", row)
        require_fields(
            report,
            "coverage.tsv",
            row,
            ("source_finding_id", "disposition", "translation_visibility"),
        )
        finding_id = row["source_finding_id"]
        if finding_id not in findings:
            report.error(f"{context}: unknown source_finding_id {finding_id!r}")
        enum_value(report, "coverage.tsv", row, "disposition", DISPOSITIONS)
        enum_value(
            report,
            "coverage.tsv",
            row,
            "translation_visibility",
            TRANSLATION_VISIBILITY,
        )
        claim_ids = set(split_scalar(row["claim_ids"]))
        for claim_id in claim_ids:
            if claim_id not in claims:
                report.error(f"{context}: unknown claim_id {claim_id!r}")
        for role in split_scalar(row["publication_roles"]):
            if role not in PUBLICATION_ROLES:
                report.error(f"{context}: invalid publication role {role!r}")

        if strict and finding_id in findings:
            if not claim_ids:
                report.error(f"{context}: strict audit requires retained claim lineage")
            lineage_ids = claims_by_source.get(finding_id, set())
            if claim_ids != lineage_ids:
                report.error(
                    f"{context}: coverage claim_ids {sorted(claim_ids)} differ from "
                    f"claim_sources lineage {sorted(lineage_ids)}"
                )
            if row["disposition"] != findings[finding_id]["disposition"]:
                report.error(
                    f"{context}: coverage disposition differs from source finding "
                    f"({findings[finding_id]['disposition']})"
                )
            expected_roles = {
                claims[claim_id]["publication_role"]
                for claim_id in claim_ids
                if claim_id in claims
            }
            actual_roles = set(split_scalar(row["publication_roles"]))
            if actual_roles != expected_roles:
                report.error(
                    f"{context}: publication_roles {sorted(actual_roles)} differ from "
                    f"linked claims {sorted(expected_roles)}"
                )
    if strict:
        missing = sorted(set(findings) - set(coverage))
        extra = sorted(set(coverage) - set(findings))
        for finding_id in missing:
            report.error(f"coverage.tsv: missing source finding {finding_id}")
        for finding_id in extra:
            report.error(f"coverage.tsv: extraneous source finding {finding_id}")
    return coverage


def validate_stage_status(
    rows: list[dict[str, str]], report: Report
) -> None:
    index_unique(report, "stage_status.tsv", rows, "stage_id")
    seen_attempts: set[tuple[str, str, str]] = set()
    running_by_scope: Counter[str] = Counter()
    for row in rows:
        context = label("stage_status.tsv", row)
        require_fields(
            report,
            "stage_status.tsv",
            row,
            ("stage_id", "scope_ref", "stage", "status", "attempt"),
        )
        enum_value(report, "stage_status.tsv", row, "stage", STAGES)
        enum_value(report, "stage_status.tsv", row, "status", STAGE_STATUSES)
        try:
            if int(row["attempt"]) < 1:
                raise ValueError
        except ValueError:
            report.error(f"{context}: attempt must be a positive integer")
        key = (row["scope_ref"], row["stage"], row["attempt"])
        if key in seen_attempts:
            report.error(f"{context}: duplicate scope/stage/attempt {key}")
        seen_attempts.add(key)
        if row["status"] == "running":
            running_by_scope[row["scope_ref"]] += 1
        if row["prompt_path"] or row["prompt_sha256"]:
            validate_hash(
                report,
                f"{context} prompt",
                row["prompt_path"],
                row["prompt_sha256"],
                row["prompt_revision"],
            )
        for field in ("input_fingerprint", "output_fingerprint"):
            if row[field] and not HASH_RE.fullmatch(row[field]):
                report.error(f"{context}: {field} must be a SHA-256 digest")
        for field in ("started_at", "completed_at"):
            if row[field]:
                try:
                    datetime.fromisoformat(row[field].replace("Z", "+00:00"))
                except ValueError:
                    report.error(f"{context}: invalid ISO 8601 timestamp in {field}")
        if row["status"] == "complete":
            require_fields(
                report,
                "stage_status.tsv",
                row,
                (
                    "input_fingerprint",
                    "output_fingerprint",
                    "started_at",
                    "completed_at",
                ),
            )
        if row["status"] == "running" and not row["started_at"]:
            report.error(f"{context}: running stage requires started_at")
        if row["status"] == "failed" and not row["error_summary"].strip():
            report.error(f"{context}: failed stage requires error_summary")
    for scope, count in running_by_scope.items():
        if count > 1:
            report.error(f"stage_status.tsv: scope {scope} has {count} running writers")


def run_kinds_for_claim(
    source_ids: set[str],
    findings: dict[str, dict[str, str]],
    runs: dict[str, dict[str, str]],
) -> set[str]:
    kinds: set[str] = set()
    for source_id in source_ids:
        finding = findings.get(source_id)
        if finding is None:
            continue
        treatment = runs.get(finding["run_id"], {}).get("treatment", "").lower()
        if "eleven" in treatment or "11" in treatment:
            kinds.add("eleven")
        elif "standard" in treatment:
            kinds.add("standard")
        else:
            kinds.add("other")
    return kinds


def validate_strict_invariants(
    report: Report,
    runs: dict[str, dict[str, str]],
    findings: dict[str, dict[str, str]],
    claims: dict[str, dict[str, str]],
    claims_by_source: dict[str, set[str]],
    sources_by_claim: dict[str, set[str]],
    evidence_by_claim: dict[str, list[dict[str, str]]],
    branches_by_claim: dict[str, set[str]],
) -> None:
    for finding_id, finding in findings.items():
        linked_claims = claims_by_source.get(finding_id, set())
        if not linked_claims:
            report.error(f"strict: source finding {finding_id} has no retained claim link")
            continue
        cited = {
            parsed
            for item in split_scalar(finding["claimed_branches"])
            if (parsed := claimed_branch(item)) is not None
        }
        represented: set[str] = set()
        for claim_id in linked_claims:
            represented.update(branches_by_claim.get(claim_id, set()))
        for missing_branch in sorted(cited - represented):
            report.error(
                f"strict: source finding {finding_id} cites {missing_branch}, but no "
                "linked claim retains that branch as evidence"
            )
        if finding["disposition"] == "split" and len(linked_claims) < 2:
            report.error(f"strict: split finding {finding_id} links to fewer than two claims")
        if finding["disposition"] == "rejected" and not any(
            claims.get(claim_id, {}).get("disposition") == "rejected"
            for claim_id in linked_claims
        ):
            report.error(
                f"strict: rejected finding {finding_id} lacks a retained rejected claim"
            )

    for claim_id, claim in claims.items():
        sources = sources_by_claim.get(claim_id, set())
        evidence = evidence_by_claim.get(claim_id, [])
        if not sources:
            report.error(f"strict: claim {claim_id} has no source lineage")
        if not evidence:
            report.error(f"strict: claim {claim_id} has no retained branch evidence")
        if claim["disposition"] in {"accepted", "evidence_only"} and evidence and all(
            row["lexical_status"] == "unlicensed" for row in evidence
        ):
            report.error(
                f"strict: promoted/evidence-only claim {claim_id} has only unlicensed evidence"
            )
        if claim["publication_role"] == "primary":
            has_anchor = any(
                row["occurrence_ref"] == claim["ayah_ref"]
                and row["evidence_role"] == "lexical_anchor"
                and row["lexical_status"] in {"direct", "contextually_activated"}
                for row in evidence
            )
            if not has_anchor:
                report.error(
                    f"strict: primary claim {claim_id} lacks a fixed-ayah direct/contextual "
                    "lexical anchor"
                )
        if claim["disposition"] == "rejected":
            if not claim["decision_reason"].strip():
                report.error(f"strict: rejected claim {claim_id} lacks a decision reason")
            if not sources or not evidence:
                report.error(
                    f"strict: rejected claim {claim_id} must retain both source and evidence "
                    "lineage"
                )

        kinds = run_kinds_for_claim(sources, findings, runs)
        relation = claim["cross_run_relation"]
        if relation in {"shared_mechanism", "compatible_refinement", "material_conflict"}:
            if not {"standard", "eleven"}.issubset(kinds):
                report.error(
                    f"strict: {relation} claim {claim_id} lacks both standard and "
                    "eleven-ayah source lineage"
                )
        elif relation == "standard_only" and "eleven" in kinds:
            report.error(f"strict: standard_only claim {claim_id} has eleven-ayah lineage")
        elif relation == "eleven_ayah_only" and "standard" in kinds:
            report.error(f"strict: eleven_ayah_only claim {claim_id} has standard lineage")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path, help="surah workspace directory")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="require closed coverage and terminal adjudication",
    )
    parser.add_argument(
        "--scope",
        metavar="AYAH_REF",
        help="validate one calibration ayah, for example 1:6",
    )
    return parser.parse_args()


def apply_ayah_scope(
    tables: dict[str, list[dict[str, str]]], scope: str
) -> dict[str, list[dict[str, str]]]:
    """Return a closed ayah slice while retaining cross-table boundary errors."""
    scoped = dict(tables)
    scoped_findings = {
        row["source_finding_id"]
        for row in tables["source_findings.tsv"]
        if row["fixed_ayah_ref"] == scope
    }
    scoped_claims = {
        row["claim_id"] for row in tables["claims.tsv"] if row["ayah_ref"] == scope
    }
    scoped["source_findings.tsv"] = [
        row
        for row in tables["source_findings.tsv"]
        if row["source_finding_id"] in scoped_findings
    ]
    scoped["claims.tsv"] = [
        row for row in tables["claims.tsv"] if row["claim_id"] in scoped_claims
    ]
    scoped["claim_sources.tsv"] = [
        row
        for row in tables["claim_sources.tsv"]
        if row["claim_id"] in scoped_claims
        or row["source_finding_id"] in scoped_findings
    ]
    scoped["branch_evidence.tsv"] = [
        row
        for row in tables["branch_evidence.tsv"]
        if row["claim_id"] in scoped_claims
    ]
    scoped["coverage.tsv"] = [
        row
        for row in tables["coverage.tsv"]
        if row["source_finding_id"] in scoped_findings
    ]
    surah_scope = f"s{int(scope.split(':', 1)[0]):03d}"
    scoped["stage_status.tsv"] = [
        row
        for row in tables["stage_status.tsv"]
        if row["scope_ref"] in {scope, surah_scope}
    ]
    return scoped


def main() -> int:
    args = parse_args()
    workspace = args.workspace.resolve()
    report = Report()
    if not workspace.is_dir():
        print(f"ERROR workspace is not a directory: {workspace}", file=sys.stderr)
        return 2

    tables: dict[str, list[dict[str, str]]] = {}
    for filename in REQUIRED_TABLES:
        tables[filename] = load_table(workspace, filename, report, required=True)
    for filename in OPTIONAL_TABLES:
        tables[filename] = load_table(workspace, filename, report, required=False)

    if args.scope:
        if not AYAH_RE.fullmatch(args.scope):
            report.error(f"--scope must be an ayah reference such as 1:6, got {args.scope!r}")
        else:
            tables = apply_ayah_scope(tables, args.scope)

    line_counts: dict[Path, int] = {}
    runs = validate_runs(tables["runs.tsv"], report)
    findings = validate_source_findings(
        tables["source_findings.tsv"],
        runs,
        report,
        args.strict,
        line_counts,
    )
    claims = validate_claims(tables["claims.tsv"], report, args.strict)
    claims_by_source, sources_by_claim = validate_claim_sources(
        tables["claim_sources.tsv"], claims, findings, report
    )
    evidence_by_claim, branches_by_claim = validate_branch_evidence(
        tables["branch_evidence.tsv"], claims, report, line_counts
    )
    validate_coverage(
        tables["coverage.tsv"],
        findings,
        claims,
        claims_by_source,
        report,
        args.strict,
    )
    validate_stage_status(tables["stage_status.tsv"], report)

    if args.strict:
        validate_strict_invariants(
            report,
            runs,
            findings,
            claims,
            claims_by_source,
            sources_by_claim,
            evidence_by_claim,
            branches_by_claim,
        )

    counts = {
        filename: len(rows)
        for filename, rows in tables.items()
        if rows or (workspace / filename).exists()
    }
    print(f"workspace: {workspace}")
    mode = "strict" if args.strict else "structural"
    if args.scope:
        mode += f" (scope {args.scope})"
    print(f"mode: {mode}")
    print("rows: " + ", ".join(f"{name}={count}" for name, count in counts.items()))
    for warning in report.warnings:
        print(f"WARNING {warning}")
    for error in report.errors:
        print(f"ERROR {error}")
    print(f"result: {len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
