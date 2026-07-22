#!/usr/bin/env python3
"""Validate an audited v3 delta draft and inject the fixed target baseline."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from finalize_publication import (
    FinalizationError,
    load_repairs,
    load_word_root_index,
    materialize_finding_anchors,
    validate_database_anchors,
    write_word_branch_view,
)
from workflow_common import (
    REPO_ROOT,
    atomic_write_compact_json,
    require_compact_json,
    sha256_file,
)


AUDIT_CHECKS = {
    "target_language_only",
    "baseline_delta_only",
    "activated_and_retrospective_coverage",
    "atomic_findings",
    "fixed_ayah_anchors",
    "valid_grades",
}
PUBLICATION_OUTPUT_ROOT = REPO_ROOT / "_status" / "v12_cross_run" / "output"
PUBLICATION_FILENAME_RE = re.compile(r"^[1-9][0-9]*_ayah_findings_publication\.json$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument("--package-index", type=Path)
    parser.add_argument("--repair-ledger", type=Path)
    return parser.parse_args()


def validate_finding(finding: Any, location: str) -> list[str]:
    if not isinstance(finding, dict) or set(finding) != {"text", "grade", "anchors"}:
        raise FinalizationError(f"{location}: finding fields differ from v3 contract")
    if not isinstance(finding["text"], str) or not finding["text"].strip():
        raise FinalizationError(f"{location}: text must be nonempty")
    if finding["grade"] not in {"strong", "weak", "reject"}:
        raise FinalizationError(f"{location}: invalid grade")
    anchors = finding["anchors"]
    if (
        not isinstance(anchors, list)
        or not anchors
        or any(not isinstance(key, str) for key in anchors)
        or len(anchors) != len(set(anchors))
    ):
        raise FinalizationError(f"{location}: anchors must be nonempty unique keys")
    return anchors


def validate_draft(
    draft: Any, surah: int, language: str, roster: list[str]
) -> set[str]:
    if not isinstance(draft, dict) or set(draft) != {"protocol", "language", "surah", "ayat"}:
        raise FinalizationError("draft fields differ from publication-draft-v3")
    if (
        draft["protocol"] != "v12-cross-run-publication-draft-v3"
        or draft["language"] != language
        or draft["surah"] != surah
    ):
        raise FinalizationError("draft protocol, language, or surah mismatch")
    if not isinstance(draft["ayat"], list):
        raise FinalizationError("draft ayat must be an array")
    actual_refs = [row.get("ayah_ref") for row in draft["ayat"] if isinstance(row, dict)]
    if actual_refs != roster or len(actual_refs) != len(draft["ayat"]):
        raise FinalizationError("draft ayah refs do not equal roster in exact order")
    used: set[str] = set()
    for ayah_index, row in enumerate(draft["ayat"]):
        if set(row) != {"ayah_ref", "findings"} or not isinstance(row["findings"], list):
            raise FinalizationError(f"ayat[{ayah_index}] differs from v3 ayah contract")
        for finding_index, finding in enumerate(row["findings"]):
            used.update(
                validate_finding(finding, f"ayat[{ayah_index}].findings[{finding_index}]")
            )
    return used


def validate_audit(
    audit: Any,
    draft_path: Path,
    baseline_sha256: str,
    language: str,
    roster: list[str],
) -> None:
    if not isinstance(audit, dict):
        raise FinalizationError("self-audit must be an object")
    if (
        audit.get("protocol") != "v12-cross-run-self-audit-v3"
        or audit.get("draft_sha256") != sha256_file(draft_path)
        or audit.get("baseline_sha256") != baseline_sha256
        or audit.get("language") != language
        or audit.get("checked_ayah_refs") != roster
        or audit.get("completed") is not True
    ):
        raise FinalizationError("self-audit does not bind this v3 draft and baseline")
    checks = audit.get("checks")
    if not isinstance(checks, dict) or set(checks) != AUDIT_CHECKS:
        raise FinalizationError("self-audit has unknown or missing v3 checks")
    failed = sorted(key for key, value in checks.items() if value is not True)
    if failed:
        raise FinalizationError(f"self-audit has incomplete checks: {failed}")


def finalize(
    workspace: Path,
    repair_path: Path | None = None,
    package_index_path: Path | None = None,
) -> dict[str, Any]:
    workspace = workspace.resolve()
    index_path = (package_index_path or workspace / "package_index.v3.json").resolve()
    index = require_compact_json(index_path)
    if index.get("protocol") != "v12-cross-run-publication-package-v3":
        raise FinalizationError("package index does not use publication-package-v3")
    surah = int(index["surah"])
    language = str(index["language"])
    baseline_sha256 = str(index["baseline_sha256"])
    expected_final_path = (
        PUBLICATION_OUTPUT_ROOT
        / language
        / f"{surah}_ayah_findings_publication.json"
    ).resolve()
    legacy_output_path = (
        PUBLICATION_OUTPUT_ROOT
        / language
        / f"{surah}_aya_findings_publication.json"
    ).resolve()
    declared_final_path = (REPO_ROOT / index["final_output"]).resolve()
    if declared_final_path != expected_final_path:
        raise FinalizationError(
            "final publication path differs from the clean output contract"
        )
    output_directory = expected_final_path.parent
    if output_directory.exists():
        invalid_entries = sorted(
            entry.name
            for entry in output_directory.iterdir()
            if (
                entry.resolve() != legacy_output_path
                and (
                    not entry.is_file()
                    or PUBLICATION_FILENAME_RE.fullmatch(entry.name) is None
                )
            )
        )
        if invalid_entries:
            raise FinalizationError(
                f"publication output directory contains non-output entries: {invalid_entries}"
            )
    for raw_path, expected_hash in index["hashes"].items():
        path = REPO_ROOT / raw_path
        if not path.exists() or sha256_file(path) != expected_hash:
            raise FinalizationError(f"package input missing or hash-drifted: {raw_path}")

    roster_doc = require_compact_json(
        REPO_ROOT / index["publisher_inputs"]["ayah_roster"]
    )
    if (
        roster_doc.get("protocol") != "v12-cross-run-ayah-roster-v3"
        or roster_doc.get("language") != language
        or roster_doc.get("baseline_sha256") != baseline_sha256
        or roster_doc.get("columns")
        != ["ayah_ref", "text_ar", "baseline_source_ref", "baseline"]
    ):
        raise FinalizationError("ayah roster has an unknown or mismatched v3 contract")
    roster_rows = roster_doc["rows"]
    roster = [row[0] for row in roster_rows]
    baseline_by_ref = {row[0]: row[3] for row in roster_rows}

    draft_path = REPO_ROOT / index["draft_output"]
    draft = require_compact_json(draft_path)
    used_keys = validate_draft(draft, surah, language, roster)
    audit_path = REPO_ROOT / index["self_audit_output"]
    validate_audit(
        require_compact_json(audit_path), draft_path, baseline_sha256, language, roster
    )

    anchor_doc = require_compact_json(
        REPO_ROOT / index["publisher_inputs"]["anchor_map"]
    )
    anchors = {row[0]: row for row in anchor_doc["rows"]}
    if not used_keys <= set(anchors):
        raise FinalizationError(f"draft contains unknown anchor keys: {sorted(used_keys-set(anchors))}")
    db_path = Path(index["coordinator_only"]["branch_database"])
    db_path = db_path if db_path.is_absolute() else REPO_ROOT / db_path
    if repair_path is not None:
        require_compact_json(repair_path)
    repairs = load_repairs(repair_path, db_path)
    resolved: dict[str, tuple[str, str]] = {}
    unresolved: list[str] = []
    meaning_change: list[str] = []
    for key in sorted(used_keys):
        row = anchors[key]
        if str(row[5]).startswith("resolved_"):
            resolved[key] = (str(row[3]), str(row[4]))
            continue
        repair = repairs.get(key)
        if repair is None or repair.get("resolution") == "unresolved":
            unresolved.append(key)
        elif repair.get("resolution") == "meaning_change":
            meaning_change.append(key)
        elif repair.get("resolution") == "resolved":
            resolved[key] = (str(repair["root_id"]), str(repair["branch_id"]))
        else:
            raise FinalizationError(f"invalid repair resolution for {key}")
    if unresolved or meaning_change:
        raise FinalizationError(
            f"anchor repair incomplete: unresolved={unresolved}, meaning_change={meaning_change}"
        )

    validate_database_anchors(set(resolved.values()), db_path)
    words_by_ayah_root, word_id_by_binding = load_word_root_index(workspace)
    final: dict[str, Any] = {
        "protocol": "v12-cross-run-publication-v3",
        "language": language,
        "surah": surah,
        "ayat": [],
    }
    filtered_contextual_anchor_uses = 0
    finding_count = 0
    anchor_row_count = 0
    branch_link_count = 0
    for ayah in draft["ayat"]:
        output_ayah: dict[str, Any] = {
            "ayah_ref": ayah["ayah_ref"],
            "baseline": baseline_by_ref[ayah["ayah_ref"]],
            "findings": [],
        }
        for finding_index, finding in enumerate(ayah["findings"]):
            anchor_rows, filtered = materialize_finding_anchors(
                finding["anchors"],
                resolved,
                words_by_ayah_root,
                ayah["ayah_ref"],
                f"{ayah['ayah_ref']}.findings[{finding_index}]",
            )
            filtered_contextual_anchor_uses += filtered
            finding_count += 1
            anchor_row_count += len(anchor_rows)
            branch_link_count += sum(len(anchor[2]) for anchor in anchor_rows)
            output_ayah["findings"].append(
                {"text": finding["text"], "grade": finding["grade"], "anchors": anchor_rows}
            )
        final["ayat"].append(output_ayah)

    final_path = expected_final_path
    atomic_write_compact_json(final_path, final)
    view_path, view_rows = write_word_branch_view(
        REPO_ROOT / index["word_branch_output"], final, word_id_by_binding
    )
    manifest = {
        "protocol": "v12-cross-run-final-manifest-v3",
        "surah": surah,
        "language": language,
        "baseline_sha256": baseline_sha256,
        "package_index_sha256": sha256_file(index_path),
        "semantic_draft_sha256": sha256_file(draft_path),
        "self_audit_sha256": sha256_file(audit_path),
        "repair_ledger_sha256": sha256_file(repair_path) if repair_path else None,
        "publication_sha256": sha256_file(final_path),
        "finding_word_branches_sha256": sha256_file(view_path),
        "counts": {
            "ayat": len(final["ayat"]),
            "findings": finding_count,
            "used_anchor_keys": len(resolved),
            "publication_anchor_rows": anchor_row_count,
            "publication_branch_links": branch_link_count,
            "filtered_contextual_anchor_uses": filtered_contextual_anchor_uses,
            "finding_word_branch_rows": view_rows,
        },
    }
    atomic_write_compact_json(REPO_ROOT / index["final_manifest_output"], manifest)
    legacy_final_path = workspace / "publication.v3.json"
    if legacy_final_path.exists() and legacy_final_path.resolve() != final_path:
        legacy_final_path.unlink()
    if legacy_output_path.exists() and legacy_output_path != final_path:
        legacy_output_path.unlink()
    return manifest


def main() -> int:
    args = parse_args()
    try:
        manifest = finalize(args.workspace, args.repair_ledger, args.package_index)
    except (OSError, ValueError, FinalizationError) as error:
        print(json.dumps({"complete": False, "error": str(error)}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
