#!/usr/bin/env python3
"""Validate an audited semantic draft and materialize QAC-attached anchors."""

from __future__ import annotations

import argparse
import csv
import json
import sqlite3
from collections import defaultdict
from contextlib import closing
from pathlib import Path
from typing import Any

from workflow_common import REPO_ROOT, atomic_write_json, atomic_write_text, read_json, sha256_file


class FinalizationError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument(
        "--package-index",
        type=Path,
        help="default: WORKSPACE/package_index.json",
    )
    parser.add_argument("--repair-ledger", type=Path)
    return parser.parse_args()


def read_tsv_untyped(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle, delimiter="\t")]


def validate_finding(finding: Any, location: str) -> list[str]:
    if not isinstance(finding, dict):
        raise FinalizationError(f"{location}: finding must be an object")
    expected = {"text", "grade", "anchors"}
    if set(finding) != expected:
        raise FinalizationError(
            f"{location}: fields must be {sorted(expected)}, got {sorted(finding)}"
        )
    if not isinstance(finding["text"], str) or not finding["text"].strip():
        raise FinalizationError(f"{location}: text must be nonempty")
    anchors = finding["anchors"]
    if (
        not isinstance(anchors, list)
        or not anchors
        or any(not isinstance(key, str) for key in anchors)
        or len(anchors) != len(set(anchors))
    ):
        raise FinalizationError(f"{location}: anchors must be nonempty unique strings")
    if finding["grade"] not in {"strong", "weak", "reject"}:
        raise FinalizationError(f"{location}: invalid finding grade")
    return anchors


def validate_draft(draft: Any, surah: int, roster: list[str]) -> set[str]:
    if not isinstance(draft, dict) or set(draft) != {"protocol", "surah", "ayat"}:
        raise FinalizationError("draft has fields outside the publication-draft contract")
    if draft["protocol"] != "v12-cross-run-publication-draft-v2" or draft["surah"] != surah:
        raise FinalizationError("draft protocol or surah mismatch")
    if not isinstance(draft["ayat"], list):
        raise FinalizationError("draft ayat must be an array")
    actual_refs = [row.get("ayah_ref") for row in draft["ayat"] if isinstance(row, dict)]
    if actual_refs != roster or len(actual_refs) != len(draft["ayat"]):
        raise FinalizationError("draft ayah refs do not equal roster in exact order")
    used: set[str] = set()
    for ayah_index, row in enumerate(draft["ayat"]):
        if set(row) != {"ayah_ref", "findings"}:
            raise FinalizationError(f"ayat[{ayah_index}] has forbidden or missing fields")
        if not isinstance(row["findings"], list):
            raise FinalizationError(f"ayat[{ayah_index}].findings must be an array")
        for finding_index, finding in enumerate(row["findings"]):
            used.update(
                validate_finding(
                    finding, f"ayat[{ayah_index}].findings[{finding_index}]"
                )
            )
    return used


def load_repairs(
    path: Path | None, db_path: Path
) -> dict[str, dict[str, Any]]:
    if path is None or not path.exists():
        return {}
    ledger = read_json(path)
    if ledger.get("protocol") != "v12-cross-run-anchor-repair-v1":
        raise FinalizationError(f"invalid repair-ledger protocol: {path}")
    exception_path = path.parent / "anchor_exceptions.json"
    if (
        not exception_path.exists()
        or ledger.get("exception_ledger_sha256") != sha256_file(exception_path)
    ):
        raise FinalizationError("repair ledger does not bind anchor_exceptions.json")
    if ledger.get("branch_database_sha256") != sha256_file(db_path):
        raise FinalizationError("repair ledger does not bind the package branch database")
    result: dict[str, dict[str, Any]] = {}
    for row in ledger.get("resolutions", []):
        key = row.get("anchor_key")
        if not key or key in result:
            raise FinalizationError(f"duplicate or missing repair anchor_key: {key!r}")
        result[key] = row
    return result


def validate_database_anchors(anchors: set[tuple[str, str]], db_path: Path) -> None:
    with closing(
        sqlite3.connect(f"{db_path.resolve().as_uri()}?mode=ro", uri=True)
    ) as connection:
        connection.execute("PRAGMA query_only = ON")
        existing = {
            (str(root_id), str(branch_id))
            for root_id, branch_id in connection.execute(
                "SELECT root_id, branch_id FROM branch_images"
            )
        }
    missing = sorted(anchors - existing)
    if missing:
        raise FinalizationError(f"materialized anchors absent from branch database: {missing}")


def load_word_root_index(
    workspace: Path,
) -> tuple[
    dict[tuple[str, str], list[tuple[str, str, int]]],
    dict[tuple[str, str, str], str],
]:
    manifest_path = workspace / "linguistic" / "manifest.json"
    roots_path = workspace / "linguistic" / "word_roots.tsv"
    words_path = workspace / "linguistic" / "words.tsv"
    if not manifest_path.exists() or not roots_path.exists() or not words_path.exists():
        raise FinalizationError("linguistic manifest/words.tsv/word_roots.tsv is missing")
    manifest = read_json(manifest_path)
    if manifest.get("warnings"):
        raise FinalizationError(
            f"linguistic cache has unresolved warnings: {manifest['warnings']}"
        )
    words = {row["word_id"]: row for row in read_tsv_untyped(words_path)}
    words_by_ayah_root: dict[tuple[str, str], list[tuple[str, str, int]]] = defaultdict(list)
    word_id_by_binding: dict[tuple[str, str, str], str] = {}
    for row in read_tsv_untyped(roots_path):
        word_id = row["word_id"]
        word = words.get(word_id)
        if word is None:
            raise FinalizationError(f"word_roots.tsv references unknown word_id: {word_id}")
        qac_word_ref = word.get("qac_word_ref", "")
        if not qac_word_ref:
            raise FinalizationError(f"words.tsv has no qac_word_ref for {word_id}")
        value = (word_id, qac_word_ref, int(word["word_index"]))
        key = (word["ayah_ref"], row["root_id"])
        if value not in words_by_ayah_root[key]:
            words_by_ayah_root[key].append(value)
        binding = (word["ayah_ref"], qac_word_ref, row["root_id"])
        previous = word_id_by_binding.setdefault(binding, word_id)
        if previous != word_id:
            raise FinalizationError(f"duplicate QAC/root binding: {binding}")
    for values in words_by_ayah_root.values():
        values.sort(key=lambda value: (value[2], value[1], value[0]))
    return dict(words_by_ayah_root), word_id_by_binding


def materialize_finding_anchors(
    anchor_keys: list[str],
    resolved: dict[str, tuple[str, str]],
    words_by_ayah_root: dict[tuple[str, str], list[tuple[str, str, int]]],
    ayah_ref: str,
    location: str,
) -> tuple[list[list[Any]], int]:
    grouped: dict[tuple[str, str, int], list[str]] = {}
    filtered_contextual = 0
    for key in anchor_keys:
        root_id, branch_id = resolved[key]
        word_bindings = words_by_ayah_root.get((ayah_ref, root_id), [])
        if not word_bindings:
            filtered_contextual += 1
            continue
        for _, qac_word_ref, word_index in word_bindings:
            branch_ids = grouped.setdefault((qac_word_ref, root_id, word_index), [])
            if branch_id not in branch_ids:
                branch_ids.append(branch_id)
    anchors = [
        [qac_word_ref, root_id, grouped[(qac_word_ref, root_id, word_index)]]
        for qac_word_ref, root_id, word_index in sorted(
            grouped, key=lambda value: (value[2], value[0], value[1])
        )
    ]
    if not anchors:
        raise FinalizationError(
            f"{location}: finding has no anchor root in fixed ayah {ayah_ref}"
        )
    return anchors, filtered_contextual


def write_word_branch_view(
    output_path: Path,
    final: dict[str, Any],
    word_id_by_binding: dict[tuple[str, str, str], str],
) -> tuple[Path, int]:

    fields = (
        "finding_id",
        "ayah_ref",
        "finding_ordinal",
        "grade",
        "anchor_ordinal",
        "branch_ordinal",
        "qac_word_ref",
        "root_id",
        "branch_id",
        "word_id",
    )
    lines = ["\t".join(fields)]
    row_count = 0
    for ayah in final["ayat"]:
        ref_key = ayah["ayah_ref"].replace(":", "_")
        for finding_ordinal, finding in enumerate(ayah["findings"], start=1):
            finding_id = f"f-{ref_key}-{finding_ordinal:03d}"
            for anchor_ordinal, anchor in enumerate(finding["anchors"], start=1):
                qac_word_ref, root_id, branch_ids = anchor
                binding = (ayah["ayah_ref"], qac_word_ref, root_id)
                word_id = word_id_by_binding.get(binding)
                if word_id is None:
                    raise FinalizationError(
                        f"final anchor has no linguistic word binding: {binding}"
                    )
                for branch_ordinal, branch_id in enumerate(branch_ids, start=1):
                    values = (
                        finding_id,
                        ayah["ayah_ref"],
                        str(finding_ordinal),
                        finding["grade"],
                        str(anchor_ordinal),
                        str(branch_ordinal),
                        qac_word_ref,
                        root_id,
                        branch_id,
                        word_id,
                    )
                    lines.append("\t".join(values))
                    row_count += 1
    atomic_write_text(output_path, "\n".join(lines) + "\n")
    return output_path, row_count


def finalize(
    workspace: Path,
    repair_path: Path | None = None,
    package_index_path: Path | None = None,
) -> dict[str, Any]:
    workspace = workspace.resolve()
    index_path = (package_index_path or workspace / "package_index.json").resolve()
    index = read_json(index_path)
    if index.get("protocol") != "v12-cross-run-publication-package-v2":
        raise FinalizationError("package index does not use publication-package-v2")
    surah = int(index["surah"])
    for raw_path, expected_hash in index["hashes"].items():
        path = REPO_ROOT / raw_path
        if not path.exists() or sha256_file(path) != expected_hash:
            raise FinalizationError(f"package input missing or hash-drifted: {raw_path}")

    roster_doc = read_json(REPO_ROOT / index["publisher_inputs"]["ayah_roster"])
    if roster_doc.get("columns") != ["ayah_ref", "text_ar"]:
        raise FinalizationError("ayah roster has an unknown column contract")
    roster = [row[0] for row in roster_doc["rows"]]
    draft_path = REPO_ROOT / index["draft_output"]
    draft = read_json(draft_path)
    used_keys = validate_draft(draft, surah, roster)

    audit_path = REPO_ROOT / index["self_audit_output"]
    audit = read_json(audit_path)
    if (
        audit.get("protocol") != "v12-cross-run-self-audit-v2"
        or audit.get("completed") is not True
        or audit.get("draft_sha256") != sha256_file(draft_path)
        or audit.get("checked_ayah_refs") != roster
    ):
        raise FinalizationError("self-audit record does not bind this complete draft")

    anchor_doc = read_json(REPO_ROOT / index["publisher_inputs"]["anchor_map"])
    anchors = {row[0]: row for row in anchor_doc["rows"]}
    if not used_keys <= set(anchors):
        raise FinalizationError(
            f"draft contains unknown anchor keys: {sorted(used_keys-set(anchors))}"
        )
    db_path = Path(index["coordinator_only"]["branch_database"])
    db_path = db_path if db_path.is_absolute() else REPO_ROOT / db_path
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
    final = {
        "protocol": "v12-cross-run-publication-v2",
        "surah": surah,
        "ayat": [],
    }
    words_by_ayah_root, word_id_by_binding = load_word_root_index(workspace)
    filtered_contextual_anchor_uses = 0
    finding_count = 0
    anchor_row_count = 0
    branch_link_count = 0
    for ayah in draft["ayat"]:
        output_ayah: dict[str, Any] = {
            "ayah_ref": ayah["ayah_ref"],
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
                {
                    "text": finding["text"],
                    "grade": finding["grade"],
                    "anchors": anchor_rows,
                }
            )
        final["ayat"].append(output_ayah)

    final_path = REPO_ROOT / index["final_output"]
    atomic_write_json(final_path, final)
    view_path, view_rows = write_word_branch_view(
        REPO_ROOT / index["word_branch_output"], final, word_id_by_binding
    )
    manifest = {
        "protocol": "v12-cross-run-final-manifest-v2",
        "surah": surah,
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
    atomic_write_json(REPO_ROOT / index["final_manifest_output"], manifest)
    return manifest


def main() -> int:
    args = parse_args()
    manifest = finalize(args.workspace, args.repair_ledger, args.package_index)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
