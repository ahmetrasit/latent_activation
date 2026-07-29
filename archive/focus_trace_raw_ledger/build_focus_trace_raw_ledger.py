#!/usr/bin/env python3
"""Build a compact raw ledger from focus trace reader outputs.

The ledger is intentionally mechanical: it copies only compact comparison
fields that are already present in the source response JSON and emits one row
per finding/model for downstream review.
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = "focus_trace_ledger.raw.v1"
CANONICAL_BASENAME_RE = re.compile(r"^\d+_\d+\.focus_trace\.json$")
CATEGORY_SPECS = (
    ("baseline_models", "baseline_model", "model_id"),
    ("context_deltas", "context_delta", "model_id"),
    ("surprising_valid_outliers", "surprising_valid_outlier", "outlier_id"),
)
DISCARDED_CATEGORY = "discarded_or_unchanged"
ACTIVATION_SUMMARY_KEYS = (
    "source_ref",
    "root",
    "source_phrase_ar",
    "mapped_root_id",
    "mapped_root_norm",
    "branch_id",
    "assigned_role",
    "role",
)
REPO_ROOT = Path(__file__).resolve().parents[1]


class LedgerError(ValueError):
    """Raised for validation or input errors."""


def natural_key(value: str) -> list[object]:
    """Sort strings with embedded digit runs numerically."""
    parts: list[object] = []
    for part in re.split(r"(\d+)", value):
        if part.isdigit():
            parts.append(int(part))
        elif part:
            parts.append(part)
    return parts


def has_glob_magic(raw: str) -> bool:
    return any(char in raw for char in "*?[")


def expand_inputs(raw_inputs: Iterable[str]) -> list[Path]:
    paths: list[Path] = []
    errors: list[str] = []
    seen: set[Path] = set()

    for raw in raw_inputs:
        matches = glob.glob(raw) if has_glob_magic(raw) else [raw]
        if not matches:
            errors.append(f"input pattern matched no files: {raw}")
            continue
        for match in matches:
            path = Path(match)
            if not path.exists():
                errors.append(f"input source does not exist: {match}")
                continue
            if not path.is_file():
                errors.append(f"input source is not a file: {match}")
                continue
            resolved = path.resolve()
            if resolved not in seen:
                seen.add(resolved)
                paths.append(resolved)

    if errors:
        raise LedgerError("; ".join(errors))
    return paths


def filter_canonical(paths: Iterable[Path]) -> list[Path]:
    return [path for path in paths if CANONICAL_BASENAME_RE.match(path.name)]


def repo_relative(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(resolved)


def sha256_bytes(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def load_source(path: Path) -> tuple[dict[str, Any], str]:
    source_bytes = path.read_bytes()
    try:
        loaded = json.loads(source_bytes)
    except json.JSONDecodeError as error:
        raise LedgerError(f"{repo_relative(path)}: invalid JSON: {error}") from error
    if not isinstance(loaded, dict):
        raise LedgerError(f"{repo_relative(path)}: expected top-level JSON object")
    return loaded, sha256_bytes(source_bytes)


def require_list(value: Any, label: str) -> list[Any]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise LedgerError(f"{label}: expected list")
    return value


def compact_activation_summary(item: dict[str, Any]) -> list[dict[str, Any]]:
    trace = require_list(item.get("activation_trace"), "activation_trace")
    summary: list[dict[str, Any]] = []
    for trace_item in trace:
        if not isinstance(trace_item, dict):
            continue
        compact = {
            key: trace_item[key]
            for key in ACTIVATION_SUMMARY_KEYS
            if key in trace_item
        }
        if compact:
            summary.append(compact)
    return summary


def first_present(record: dict[str, Any], keys: Iterable[str]) -> Any:
    for key in keys:
        value = record.get(key)
        if value not in (None, ""):
            return value
    return None


def changed_reading_parts(record: dict[str, Any]) -> tuple[Any, Any]:
    changed = record.get("changed_reading")
    before = record.get("changed_reading_before")
    after = record.get("changed_reading_after")
    if isinstance(changed, dict):
        before = changed.get("before", before)
        after = changed.get("after", after)
    return before, after


def add_if_present(row: dict[str, Any], key: str, value: Any) -> None:
    if value is not None:
        row[key] = value


def build_finding_row(
    *,
    source_file: str,
    source_hash: str,
    source_data: dict[str, Any],
    category: str,
    finding_id: str,
    item: dict[str, Any],
    source_item_index: int,
    include_activation_summary: bool,
) -> dict[str, Any]:
    focus_ref = source_data.get("focus_ref")
    row: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "source_file": source_file,
        "source_hash": source_hash,
        "reader_id": source_data.get("reader_id"),
        "protocol": source_data.get("protocol"),
        "focus_ref": focus_ref,
        "category": category,
        "finding_id": finding_id,
        "finding_key": f"{source_file}::{category}::{finding_id}",
        "source_item_index": source_item_index,
    }

    for key in (
        "status",
        "confidence",
        "trigger_refs",
        "trigger_roots",
        "focus_anchor",
        "mechanism",
    ):
        add_if_present(row, key, item.get(key))

    before, after = changed_reading_parts(item)
    add_if_present(row, "changed_reading_before", before)
    add_if_present(row, "changed_reading_after", after)

    if category == "surprising_valid_outlier":
        for key in (
            "why_surprising",
            "why_still_valid",
            "rendering_caution",
            "containment",
        ):
            add_if_present(row, key, item.get(key))

    if include_activation_summary:
        summary = compact_activation_summary(item)
        if summary:
            row["activation_summary"] = summary

    return row


def build_discarded_row(
    *,
    source_file: str,
    source_hash: str,
    source_data: dict[str, Any],
    entry: Any,
    source_item_index: int,
) -> dict[str, Any]:
    if isinstance(entry, str):
        finding_id = f"{DISCARDED_CATEGORY}_{source_item_index + 1:03d}"
        note = entry
    elif isinstance(entry, dict):
        found_id = first_present(entry, ("finding_id", "model_id", "outlier_id", "id"))
        finding_id = str(found_id) if found_id is not None else f"{DISCARDED_CATEGORY}_{source_item_index + 1:03d}"
        note = first_present(entry, ("note", "reason", "summary", "text"))
    else:
        finding_id = f"{DISCARDED_CATEGORY}_{source_item_index + 1:03d}"
        note = str(entry)

    row: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "source_file": source_file,
        "source_hash": source_hash,
        "reader_id": source_data.get("reader_id"),
        "protocol": source_data.get("protocol"),
        "focus_ref": source_data.get("focus_ref"),
        "category": DISCARDED_CATEGORY,
        "finding_id": finding_id,
        "finding_key": f"{source_file}::{DISCARDED_CATEGORY}::{finding_id}",
        "source_item_index": source_item_index,
    }
    add_if_present(row, "note", note)
    if isinstance(entry, dict):
        for key in ("status", "confidence", "trigger_refs", "trigger_roots"):
            add_if_present(row, key, entry.get(key))
    return row


def rows_for_source(
    path: Path,
    *,
    include_discarded: bool,
    include_activation_summary: bool,
) -> list[dict[str, Any]]:
    source_data, source_hash = load_source(path)
    source_file = repo_relative(path)
    rows: list[dict[str, Any]] = []

    for source_key, category, id_key in CATEGORY_SPECS:
        items = require_list(source_data.get(source_key), f"{source_file}.{source_key}")
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                raise LedgerError(f"{source_file}.{source_key}[{index}]: expected object")
            found_id = first_present(item, (id_key, "model_id"))
            if found_id is None:
                raise LedgerError(f"{source_file}.{source_key}[{index}]: missing {id_key}")
            rows.append(
                build_finding_row(
                    source_file=source_file,
                    source_hash=source_hash,
                    source_data=source_data,
                    category=category,
                    finding_id=str(found_id),
                    item=item,
                    source_item_index=index,
                    include_activation_summary=include_activation_summary,
                )
            )

    if include_discarded:
        discarded = require_list(
            source_data.get(DISCARDED_CATEGORY),
            f"{source_file}.{DISCARDED_CATEGORY}",
        )
        for index, entry in enumerate(discarded):
            rows.append(
                build_discarded_row(
                    source_file=source_file,
                    source_hash=source_hash,
                    source_data=source_data,
                    entry=entry,
                    source_item_index=index,
                )
            )

    return rows


def validate_rows(rows: list[dict[str, Any]]) -> None:
    required = ("source_file", "focus_ref", "category", "finding_id", "finding_key")
    seen_keys: set[str] = set()
    errors: list[str] = []

    for index, row in enumerate(rows):
        for key in required:
            if row.get(key) in (None, ""):
                errors.append(f"row {index}: missing required field {key}")
        finding_key = row.get("finding_key")
        if finding_key in seen_keys:
            errors.append(f"row {index}: duplicate finding_key {finding_key}")
        elif isinstance(finding_key, str):
            seen_keys.add(finding_key)

    if errors:
        raise LedgerError("; ".join(errors))


def write_rows(path: Path, rows: list[dict[str, Any]], *, pretty: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            if pretty:
                handle.write(json.dumps(row, ensure_ascii=False))
            else:
                handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")))
            handle.write("\n")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a compact raw JSONL ledger from focus trace output JSON files."
    )
    parser.add_argument(
        "--inputs",
        nargs="+",
        required=True,
        help="Input focus_trace JSON files or glob patterns.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Output ledger path. Parent directories are created.",
    )
    parser.add_argument(
        "--canonical-only",
        action="store_true",
        help="Include only basenames matching ^\\d+_\\d+\\.focus_trace\\.json$.",
    )
    parser.add_argument(
        "--include-discarded",
        action="store_true",
        help="Also emit discarded_or_unchanged notes, off by default.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Use readable JSON separators while preserving one object per line.",
    )
    parser.add_argument(
        "--no-activation-summary",
        action="store_true",
        help="Omit compact activation_summary rows.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        input_paths = expand_inputs(args.inputs)
        if args.canonical_only:
            input_paths = filter_canonical(input_paths)
            variants = [path for path in input_paths if not CANONICAL_BASENAME_RE.match(path.name)]
            if variants:
                variant_list = ", ".join(repo_relative(path) for path in variants)
                raise LedgerError(f"canonical-only validation failed; variant files included: {variant_list}")
        if not input_paths:
            raise LedgerError("no input files remained after selection")

        input_paths = sorted(input_paths, key=lambda path: natural_key(repo_relative(path)))
        rows: list[dict[str, Any]] = []
        for path in input_paths:
            rows.extend(
                rows_for_source(
                    path,
                    include_discarded=args.include_discarded,
                    include_activation_summary=not args.no_activation_summary,
                )
            )
        validate_rows(rows)
        write_rows(args.output, rows, pretty=args.pretty)
    except LedgerError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
