#!/usr/bin/env python3
"""Build one hash-bound, publisher-visible whole-surah package."""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from collections import defaultdict
from contextlib import closing
from pathlib import Path
from typing import Any

from workflow_common import (
    REPO_ROOT,
    atomic_write_json,
    ayah_sort_key,
    discover_runs,
    read_json,
    repo_relative,
    sha256_file,
)


BRANCH_DB_PATH = REPO_ROOT / "resources" / "furuq_v4.sqlite"
PROMPT_PATH = REPO_ROOT / "_status" / "v12_cross_run" / "prompts" / "publish_whole_surah.md"
SCHEMA_PATH = REPO_ROOT / "_status" / "v12_cross_run" / "model_schemas" / "publication_draft.json"
HEADING_RE = re.compile(r"^##\s+([1-9][0-9]*:[0-9]+)(?=\s|:|\||—|-|$)")
ROOT_RE = re.compile(
    r"(?<![\u0621-\u064a])((?:[\u0621-\u064a]\s+){2,3}[\u0621-\u064a]"
    r"|[\u0621-\u064a]{3,4}(?=\s*/?\s*B[0-9]))"
    r"(?![\u0621-\u064a])"
)
BRANCH_LIKE_RE = re.compile(r"(?<![A-Za-z0-9])B([0-9]{1,4})(?![0-9])")


class PackageError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("surah", type=int, choices=range(1, 115), metavar="SURAH")
    parser.add_argument(
        "--workspace",
        type=Path,
        help="default: _status/v12_cross_run/s###",
    )
    parser.add_argument(
        "--variant",
        help="optional lowercase model/run label used in every output filename",
    )
    return parser.parse_args()


def normalized_root(value: str) -> str:
    root = " ".join(str(value or "").split())
    if " " not in root and 3 <= len(root) <= 4 and all(
        "\u0621" <= character <= "\u064a" for character in root
    ):
        return " ".join(root)
    return root


def canonical_root(value: str) -> str:
    return "".join(
        {
            "آ": "ا",
            "أ": "ا",
            "إ": "ا",
            "ٱ": "ا",
            "ء": "ا",
            "ى": "ي",
            "ؤ": "و",
            "ئ": "ي",
        }.get(character, character)
        for character in normalized_root(value)
        if character != " "
    )


def heading_refs(path: Path) -> list[str]:
    refs: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = HEADING_RE.match(line)
        if match:
            refs.append(match.group(1))
    return refs


def verify_coverage(path: Path, expected_refs: list[str]) -> None:
    actual = heading_refs(path)
    if actual != expected_refs:
        missing = [ref for ref in expected_refs if ref not in actual]
        extras = [ref for ref in actual if ref not in expected_refs]
        duplicates = sorted({ref for ref in actual if actual.count(ref) > 1}, key=ayah_sort_key)
        raise PackageError(
            f"{repo_relative(path)} heading roster differs from packet: "
            f"missing={missing}, extra={extras}, duplicate={duplicates}, order_match=false"
        )


def connect_branch_db() -> sqlite3.Connection:
    connection = sqlite3.connect(
        f"{BRANCH_DB_PATH.resolve().as_uri()}?mode=ro", uri=True
    )
    connection.execute("PRAGMA query_only = ON")
    connection.row_factory = sqlite3.Row
    return connection


def branch_indexes(
    connection: sqlite3.Connection,
) -> tuple[
    dict[tuple[str, str], list[tuple[str, str]]],
    dict[tuple[str, str], list[tuple[str, str]]],
    dict[tuple[str, str], list[tuple[str, str]]],
]:
    by_source: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
    by_normalized: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
    by_canonical: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
    for row in connection.execute(
        """
        SELECT b.root_id, b.branch_id, r.source_root_norm, r.root_norm
        FROM branch_images b JOIN roots r USING(root_id)
        ORDER BY r.source_root_norm, r.root_norm, b.branch_id, b.root_id
        """
    ):
        value = (str(row["root_id"]), str(row["branch_id"]))
        branch_id = str(row["branch_id"])
        for index, root in (
            (by_source, row["source_root_norm"]),
            (by_normalized, row["root_norm"]),
            (by_canonical, row["root_norm"]),
        ):
            root_key = (
                canonical_root(str(root))
                if index is by_canonical
                else normalized_root(str(root))
            )
            key = (root_key, branch_id)
            if value not in index[key]:
                index[key].append(value)
    return dict(by_source), dict(by_normalized), dict(by_canonical)


def resolve_anchor(
    source_root: str,
    source_branch: str,
    by_source: dict[tuple[str, str], list[tuple[str, str]]],
    by_normalized: dict[tuple[str, str], list[tuple[str, str]]],
    by_canonical: dict[tuple[str, str], list[tuple[str, str]]],
) -> tuple[str | None, str | None, str]:
    key = (normalized_root(source_root), source_branch)
    matches = by_source.get(key, [])
    method = "source_exact"
    if not matches:
        matches = by_normalized.get(key, [])
        method = "normalized_exact"
    if not matches:
        matches = by_canonical.get((canonical_root(source_root), source_branch), [])
        method = "canonical_fallback"
    if len(matches) == 1:
        return matches[0][0], matches[0][1], f"resolved_{method}"
    if not matches:
        return None, None, "review_nonexistent"
    return None, None, f"review_ambiguous_{method}"


def line_ayah_refs(lines: list[str]) -> dict[int, str]:
    current = ""
    result: dict[int, str] = {}
    for line_number, line in enumerate(lines, start=1):
        match = HEADING_RE.match(line)
        if match:
            current = match.group(1)
        result[line_number] = current
    return result


def discover_citations(
    source_paths: list[Path],
    by_source: dict[tuple[str, str], list[tuple[str, str]]],
    by_normalized: dict[tuple[str, str], list[tuple[str, str]]],
    by_canonical: dict[tuple[str, str], list[tuple[str, str]]],
    surah: int,
) -> tuple[dict[str, Any], dict[str, Any]]:
    citations: list[dict[str, Any]] = []
    for source_path in source_paths:
        lines = source_path.read_text(encoding="utf-8").splitlines()
        refs = line_ayah_refs(lines)
        for line_number, line in enumerate(lines, start=1):
            root_matches = list(ROOT_RE.finditer(line))
            claimed_branch_spans: set[tuple[int, int]] = set()
            for ordinal, root_match in enumerate(root_matches):
                end = root_matches[ordinal + 1].start() if ordinal + 1 < len(root_matches) else len(line)
                segment = line[root_match.end():end]
                for branch_match in BRANCH_LIKE_RE.finditer(segment):
                    absolute_span = (
                        root_match.end() + branch_match.start(),
                        root_match.end() + branch_match.end(),
                    )
                    claimed_branch_spans.add(absolute_span)
                    digits = branch_match.group(1)
                    citations.append(
                        {
                            "source_root": normalized_root(root_match.group(1)),
                            "source_branch": f"B{digits}",
                            "state_override": (
                                "" if len(digits) == 3 else "review_malformed_branch"
                            ),
                            "source_path": repo_relative(source_path),
                            "line": line_number,
                            "ayah_ref": refs[line_number],
                            "source_excerpt": line.strip(),
                        }
                    )
            for branch_match in BRANCH_LIKE_RE.finditer(line):
                if branch_match.span() in claimed_branch_spans:
                    continue
                citations.append(
                    {
                        "source_root": "",
                        "source_branch": branch_match.group(0),
                        "state_override": "review_branch_without_root",
                        "source_path": repo_relative(source_path),
                        "line": line_number,
                        "ayah_ref": refs[line_number],
                        "source_excerpt": line.strip(),
                        "identity_suffix": (
                            f"{repo_relative(source_path)}:{line_number}:{branch_match.start()}"
                        ),
                    }
                )

    unique_identities = sorted(
        {
            (
                row["source_root"],
                row["source_branch"],
                row["state_override"],
                row.get("identity_suffix", "")
                if row["state_override"] == "review_branch_without_root"
                else "",
            )
            for row in citations
        },
        key=lambda identity: (identity[0], identity[1], identity[2], identity[3]),
    )
    key_by_identity = {
        identity: f"a-s{surah:03d}-{ordinal:04d}"
        for ordinal, identity in enumerate(unique_identities, start=1)
    }
    anchor_rows: list[list[Any]] = []
    states: dict[str, str] = {}
    for identity in unique_identities:
        source_root, source_branch, state_override, _ = identity
        if state_override:
            root_id, branch_id, state = None, None, state_override
        else:
            root_id, branch_id, state = resolve_anchor(
                source_root, source_branch, by_source, by_normalized, by_canonical
            )
        anchor_key = key_by_identity[identity]
        states[anchor_key] = state
        anchor_rows.append(
            [anchor_key, source_root or None, source_branch, root_id, branch_id, state]
        )
    occurrence_rows = [
        [
            key_by_identity[
                (
                    row["source_root"],
                    row["source_branch"],
                    row["state_override"],
                    row.get("identity_suffix", "")
                    if row["state_override"] == "review_branch_without_root"
                    else "",
                )
            ],
            row["source_path"],
            row["line"],
            row["ayah_ref"],
            row["source_excerpt"],
        ]
        for row in citations
    ]
    exceptions = [
        {
            "anchor_key": row[0],
            "source_root": row[1],
            "source_branch": row[2],
            "state": row[5],
            "occurrences": sum(1 for item in occurrence_rows if item[0] == row[0]),
        }
        for row in anchor_rows
        if not str(row[5]).startswith("resolved_")
    ]
    anchor_map = {
        "protocol": "v12-cross-run-anchor-map-v1",
        "columns": [
            "anchor_key",
            "source_root",
            "source_branch",
            "root_id",
            "branch_id",
            "state",
        ],
        "rows": anchor_rows,
        "review_columns": [
            "anchor_key",
            "source_path",
            "line",
            "ayah_ref",
            "raw_excerpt",
        ],
        "review_rows": [
            row
            for row in occurrence_rows
            if not states[row[0]].startswith("resolved_")
        ],
    }
    occurrence_map = {
        "protocol": "v12-cross-run-anchor-occurrences-v1",
        "columns": [
            "anchor_key",
            "source_path",
            "line",
            "ayah_ref",
            "source_excerpt",
        ],
        "rows": occurrence_rows,
        "exceptions": exceptions,
        "summary": {
            "citation_occurrences": len(occurrence_rows),
            "unique_anchor_keys": len(anchor_rows),
            "resolved_anchor_keys": sum(
                state.startswith("resolved_") for state in states.values()
            ),
            "review_anchor_keys": sum(
                not state.startswith("resolved_") for state in states.values()
            ),
            "malformed_or_unattached_occurrences": sum(
                bool(row["state_override"]) for row in citations
            ),
        },
    }
    return anchor_map, occurrence_map


def build(
    surah: int,
    workspace: Path | None = None,
    variant: str | None = None,
) -> dict[str, Any]:
    tag = f"s{surah:03d}"
    workspace = (workspace or REPO_ROOT / "_status" / "v12_cross_run" / tag).resolve()
    workspace.mkdir(parents=True, exist_ok=True)
    if variant is not None and not re.fullmatch(r"[a-z0-9][a-z0-9.-]*", variant):
        raise PackageError(
            "variant must contain only lowercase letters, digits, dots, and hyphens"
        )
    suffix = f".{variant}" if variant else ""
    runs, _ = discover_runs(surah, allow_single_run=False)
    if len(runs) != 2:
        raise PackageError(f"{tag}: expected two canonical reader runs, got {len(runs)}")
    packet_path = REPO_ROOT / runs[0]["packet_path"]
    if any(row["packet_path"] != runs[0]["packet_path"] for row in runs):
        raise PackageError(f"{tag}: selected readers do not share one packet")
    packet = read_json(packet_path)
    ayat = packet.get("ayat", [])
    expected_refs = [str(ayah["ref"]) for ayah in ayat]
    if len(expected_refs) != len(set(expected_refs)):
        raise PackageError(f"{tag}: packet contains duplicate ayah refs")
    expected_surah = {int(ref.split(":", 1)[0]) for ref in expected_refs}
    if expected_surah != {surah}:
        raise PackageError(f"{tag}: packet refs belong to {sorted(expected_surah)}")

    source_paths = [REPO_ROOT / row["output_path"] for row in runs]
    for source_path in source_paths:
        verify_coverage(source_path, expected_refs)

    roster = {
        "protocol": "v12-cross-run-ayah-roster-v1",
        "surah": surah,
        "columns": ["ayah_ref", "text_ar"],
        "rows": [
            [str(ayah["ref"]), str(ayah["text_ar"])]
            for ayah in ayat
        ],
    }
    roster_path = workspace / "ayah_roster.json"
    atomic_write_json(roster_path, roster)

    with closing(connect_branch_db()) as connection:
        by_source, by_normalized, by_canonical = branch_indexes(connection)
        anchor_map, occurrences = discover_citations(
            source_paths, by_source, by_normalized, by_canonical, surah
        )
    anchor_path = workspace / "anchor_map.json"
    occurrence_path = workspace / "anchor_occurrences.json"
    atomic_write_json(anchor_path, anchor_map)
    atomic_write_json(occurrence_path, occurrences)

    input_paths = source_paths + [
        packet_path,
        roster_path,
        anchor_path,
        occurrence_path,
        BRANCH_DB_PATH,
        PROMPT_PATH,
        SCHEMA_PATH,
    ]
    index = {
        "protocol": "v12-cross-run-publication-package-v2",
        "surah": surah,
        "variant": variant,
        "state": (
            "ready_with_anchor_exceptions"
            if occurrences["summary"]["review_anchor_keys"]
            or occurrences["summary"]["malformed_or_unattached_occurrences"]
            else "ready"
        ),
        "publisher_inputs": {
            "standard_reader": runs[0]["output_path"],
            "wide_reader": runs[1]["output_path"],
            "ayah_roster": repo_relative(roster_path),
            "anchor_map": repo_relative(anchor_path),
            "prompt": repo_relative(PROMPT_PATH),
            "output_schema": repo_relative(SCHEMA_PATH),
        },
        "coordinator_only": {
            "packet": repo_relative(packet_path),
            "anchor_occurrences": repo_relative(occurrence_path),
            "branch_database": repo_relative(BRANCH_DB_PATH),
        },
        "hashes": {repo_relative(path): sha256_file(path) for path in input_paths},
        "coverage": {
            "ayah_count": len(expected_refs),
            "standard_heading_count": len(heading_refs(source_paths[0])),
            "wide_heading_count": len(heading_refs(source_paths[1])),
        },
        "anchor_summary": occurrences["summary"],
        "draft_output": repo_relative(workspace / f"publication{suffix}.draft.json"),
        "self_audit_output": repo_relative(workspace / f"self_audit{suffix}.json"),
        "final_output": repo_relative(workspace / f"publication{suffix}.json"),
        "final_manifest_output": repo_relative(
            workspace / f"publication_manifest{suffix}.json"
        ),
        "word_branch_output": repo_relative(
            workspace / "derived" / f"finding_word_branches{suffix}.tsv"
        ),
    }
    atomic_write_json(workspace / f"package_index{suffix}.json", index)
    return index


def main() -> int:
    args = parse_args()
    index = build(args.surah, args.workspace, args.variant)
    print(json.dumps(index, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
