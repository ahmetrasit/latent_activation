#!/usr/bin/env python3
"""Collect all prepared-surah anchor exceptions for one surgical repair pass."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from workflow_common import REPO_ROOT, atomic_write_json, read_json, repo_relative, sha256_file


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--workspace-root",
        type=Path,
        default=REPO_ROOT / "_status" / "v12_cross_run",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "_status" / "v12_cross_run" / "anchor_exceptions.json",
    )
    parser.add_argument(
        "--allow-partial",
        action="store_true",
        help="permit a pilot subset without completed drafts/self-audits",
    )
    return parser.parse_args()


def collect(
    workspace_root: Path, output: Path, *, allow_partial: bool = False
) -> dict[str, Any]:
    rows: list[list[Any]] = []
    hashes: dict[str, str] = {}
    keys: set[str] = set()
    workspaces = sorted(workspace_root.glob("s[0-9][0-9][0-9]"))
    prepared = [
        workspace
        for workspace in workspaces
        if (workspace / "anchor_map.json").exists()
    ]
    if not allow_partial:
        expected = {f"s{surah:03d}" for surah in range(1, 115)}
        actual = {workspace.name for workspace in prepared}
        if actual != expected:
            missing = sorted(expected - actual)
            raise RuntimeError(
                "global repair requires all 114 packages; "
                f"missing_count={len(missing)}, first_missing={missing[:10]}"
            )
        for workspace in prepared:
            index = read_json(workspace / "package_index.json")
            if index.get("protocol") != "v12-cross-run-publication-package-v2":
                raise RuntimeError(f"{workspace.name}: package index is not v2")
            draft_path = workspace / "publication.draft.json"
            audit_path = workspace / "self_audit.json"
            if not draft_path.exists() or not audit_path.exists():
                raise RuntimeError(f"{workspace.name}: draft/self-audit is incomplete")
            audit = read_json(audit_path)
            draft = read_json(draft_path)
            if (
                draft.get("protocol") != "v12-cross-run-publication-draft-v2"
                or audit.get("protocol") != "v12-cross-run-self-audit-v2"
                or audit.get("completed") is not True
                or audit.get("draft_sha256") != sha256_file(draft_path)
                or len(audit.get("checked_ayah_refs", []))
                != int(index["coverage"]["ayah_count"])
            ):
                raise RuntimeError(f"{workspace.name}: self-audit does not bind its draft")
    for workspace in prepared:
        map_path = workspace / "anchor_map.json"
        if not map_path.exists():
            continue
        document = read_json(map_path)
        state_by_key = {row[0]: row[5] for row in document["rows"]}
        identity_by_key = {row[0]: (row[1], row[2]) for row in document["rows"]}
        review_rows = document.get("review_rows", [])
        for occurrence in review_rows:
            key, source_path, line, ayah_ref, excerpt = occurrence
            source_root, source_branch = identity_by_key[key]
            rows.append(
                [
                    key,
                    int(workspace.name[1:]),
                    source_root,
                    source_branch,
                    state_by_key[key],
                    source_path,
                    line,
                    ayah_ref,
                    excerpt,
                ]
            )
            keys.add(key)
        hashes[repo_relative(map_path)] = sha256_file(map_path)
    result = {
        "protocol": "v12-cross-run-anchor-exceptions-v1",
        "branch_database": "resources/furuq_v4.sqlite",
        "branch_database_sha256": sha256_file(REPO_ROOT / "resources" / "furuq_v4.sqlite"),
        "columns": [
            "anchor_key",
            "surah",
            "source_root",
            "source_branch",
            "state",
            "source_path",
            "line",
            "ayah_ref",
            "source_excerpt",
        ],
        "rows": rows,
        "summary": {
            "prepared_surahs": len(prepared),
            "exception_keys": len(keys),
            "occurrences": len(rows),
        },
        "anchor_map_hashes": hashes,
    }
    atomic_write_json(output, result)
    return result


def main() -> int:
    args = parse_args()
    result = collect(
        args.workspace_root.resolve(),
        args.output.resolve(),
        allow_partial=args.allow_partial,
    )
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
