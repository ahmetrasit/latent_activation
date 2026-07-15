#!/usr/bin/env python3
"""Shared deterministic helpers for the GSLS 2.1 runtime."""

from __future__ import annotations

import csv
import json
import os
import tempfile
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping, Sequence


WORKFLOW_ID = "GSLS-3A-2.1"
PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PACKAGE_ROOT.parent
DEFAULT_PROFILE = PACKAGE_ROOT / "profiles" / "v1-local-resources.json"

ALEF_TO_HAMZA = str.maketrans(
    {
        "\u0622": "\u0621",
        "\u0623": "\u0621",
        "\u0625": "\u0621",
        "\u0671": "\u0621",
        "\u0672": "\u0621",
        "\u0673": "\u0621",
        "\u0649": "\u064a",
    }
)


class ContractError(RuntimeError):
    """Raised when a deterministic workflow contract is violated."""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def canonical_root(value: str) -> str:
    text = unicodedata.normalize("NFKC", value).translate(ALEF_TO_HAMZA)
    text = text.replace("\u0640", "")
    return "".join(
        char
        for char in text
        if not char.isspace() and unicodedata.category(char) != "Mn"
    )


def strip_encoding_marker(value: str) -> str:
    return value.removeprefix("\ufeff")


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        os.replace(temp_name, path)
    finally:
        Path(temp_name).unlink(missing_ok=True)


def write_json(path: Path, value: Any) -> None:
    atomic_write_text(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> int:
    materialized = list(rows)
    text = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in materialized)
    atomic_write_text(path, text)
    return len(materialized)


def iter_jsonl(path: Path) -> Iterator[tuple[int, dict[str, Any]]]:
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ContractError(f"{path}:{line_number}: JSONL record is not an object")
            yield line_number, value


def write_tsv(path: Path, fieldnames: Sequence[str], rows: Iterable[Mapping[str, Any]]) -> int:
    materialized = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            for row in materialized:
                writer.writerow({field: row.get(field, "") for field in fieldnames})
        os.replace(temp_name, path)
    finally:
        Path(temp_name).unlink(missing_ok=True)
    return len(materialized)


def resolve_repo_path(value: str, repo_root: Path = REPO_ROOT) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (repo_root / path).resolve()


def require_regular_file(path: Path, label: str) -> None:
    if not path.is_file():
        raise ContractError(f"Missing {label}: {path}")
    if path.stat().st_size == 0:
        raise ContractError(f"Empty {label}: {path}")


def ensure_new_directory(path: Path) -> None:
    if path.exists() and any(path.iterdir()):
        raise ContractError(f"Run directory is not empty: {path}")
    path.mkdir(parents=True, exist_ok=True)


def assert_within(path: Path, parent: Path, label: str) -> None:
    try:
        path.resolve().relative_to(parent.resolve())
    except ValueError as error:
        raise ContractError(f"{label} escapes {parent}: {path}") from error


def split_aligned(value: str) -> list[str]:
    return value.split(";") if value != "" else [""]
