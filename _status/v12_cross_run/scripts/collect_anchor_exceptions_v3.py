#!/usr/bin/env python3
"""Collect v3 anchor exceptions after selected publisher audits complete."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from workflow_common import (
    REPO_ROOT,
    atomic_write_compact_json,
    repo_relative,
    require_compact_json,
    sha256_file,
)


BRANCH_DATABASE = REPO_ROOT / "resources" / "furuq_v4.sqlite"
DEFAULT_OUTPUT = REPO_ROOT / "_status" / "v12_cross_run" / "anchor_exceptions.json"
REPAIR_SCHEMA = (
    REPO_ROOT
    / "_status"
    / "v12_cross_run"
    / "model_schemas"
    / "anchor_repair.json"
)
REPAIR_OUTPUT = REPO_ROOT / "_status" / "v12_cross_run" / "anchor_repair.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah", type=int, action="append", choices=range(1, 115))
    parser.add_argument(
        "--workspace-root",
        type=Path,
        default=REPO_ROOT / "_status" / "v12_cross_run",
    )
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--require-all-surahs", action="store_true")
    return parser.parse_args()


def validate_completed_workspace(workspace: Path) -> tuple[dict, dict]:
    index_path = workspace / "package_index.v3.json"
    map_path = workspace / "anchor_map.v3.json"
    draft_path = workspace / "publication.v3.draft.json"
    audit_path = workspace / "self_audit.v3.json"
    for path in (index_path, map_path, draft_path, audit_path):
        if not path.is_file():
            raise RuntimeError(f"{workspace.name}: required v3 file is missing: {path.name}")
    index = require_compact_json(index_path)
    anchor_map = require_compact_json(map_path)
    draft = require_compact_json(draft_path)
    audit = require_compact_json(audit_path)
    if index.get("protocol") != "v12-cross-run-publication-package-v3":
        raise RuntimeError(f"{workspace.name}: package index is not v3")
    if index["hashes"].get(repo_relative(map_path)) != sha256_file(map_path):
        raise RuntimeError(f"{workspace.name}: anchor map is not bound by package index")
    roster_path = REPO_ROOT / index["publisher_inputs"]["ayah_roster"]
    roster = require_compact_json(roster_path)
    roster_refs = [row[0] for row in roster["rows"]]
    if (
        draft.get("protocol") != "v12-cross-run-publication-draft-v3"
        or [row.get("ayah_ref") for row in draft.get("ayat", [])] != roster_refs
        or audit.get("protocol") != "v12-cross-run-self-audit-v3"
        or audit.get("draft_sha256") != sha256_file(draft_path)
        or audit.get("baseline_sha256") != index["baseline_sha256"]
        or audit.get("checked_ayah_refs") != roster_refs
        or audit.get("completed") is not True
    ):
        raise RuntimeError(f"{workspace.name}: self-audit does not bind the v3 draft")
    return index, anchor_map


def collect(args: argparse.Namespace) -> dict[str, Any]:
    workspace_root = args.workspace_root.resolve()
    if args.surah:
        surahs = sorted(set(args.surah))
    else:
        surahs = sorted(
            int(path.name[1:])
            for path in workspace_root.glob("s[0-9][0-9][0-9]")
            if (path / "package_index.v3.json").is_file()
        )
    if args.require_all_surahs and surahs != list(range(1, 115)):
        missing = sorted(set(range(1, 115)) - set(surahs))
        raise RuntimeError(
            f"complete repair collection lacks {len(missing)} surahs: {missing[:10]}"
        )
    if not surahs:
        raise RuntimeError("no completed v3 workspaces selected")

    rows: list[list[Any]] = []
    hashes: dict[str, str] = {}
    keys: set[str] = set()
    for surah in surahs:
        workspace = workspace_root / f"s{surah:03d}"
        _, anchor_map = validate_completed_workspace(workspace)
        map_path = workspace / "anchor_map.v3.json"
        state_by_key = {row[0]: row[5] for row in anchor_map["rows"]}
        identity_by_key = {row[0]: (row[1], row[2]) for row in anchor_map["rows"]}
        for occurrence in anchor_map.get("review_rows", []):
            key, source_path, line, ayah_ref, excerpt = occurrence
            source_root, source_branch = identity_by_key[key]
            rows.append(
                [
                    key,
                    surah,
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
        "branch_database": repo_relative(BRANCH_DATABASE),
        "branch_database_sha256": sha256_file(BRANCH_DATABASE),
        "repair_schema": repo_relative(REPAIR_SCHEMA),
        "repair_output": repo_relative(REPAIR_OUTPUT),
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
            "prepared_surahs": len(surahs),
            "exception_keys": len(keys),
            "occurrences": len(rows),
        },
        "anchor_map_hashes": hashes,
    }
    atomic_write_compact_json(args.output.resolve(), result)
    return result


def main() -> int:
    args = parse_args()
    try:
        result = collect(args)
    except (OSError, ValueError, RuntimeError) as error:
        print(json.dumps({"ready": False, "error": str(error)}, ensure_ascii=False))
        return 1
    print(json.dumps(result["summary"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
