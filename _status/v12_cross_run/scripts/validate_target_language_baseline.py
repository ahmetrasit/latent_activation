#!/usr/bin/env python3
"""Validate a compact ordinary baseline and its no-orphan QAC word map."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any


class BaselineValidationError(RuntimeError):
    pass


LANGUAGE_RE = re.compile(r"^[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})*$")
INTERNAL_JOINERS = {"'", "’", "-", "‐", "‑"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path)
    parser.add_argument("--qac", type=Path, required=True)
    parser.add_argument("--surah", type=int, choices=range(1, 115))
    parser.add_argument("--require-complete", action="store_true")
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require_keys(value: Any, expected: set[str], location: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise BaselineValidationError(f"{location}: expected object")
    actual = set(value)
    if actual != expected:
        raise BaselineValidationError(
            f"{location}: fields differ; missing={sorted(expected-actual)}, "
            f"extra={sorted(actual-expected)}"
        )
    return value


def is_word_character(character: str) -> bool:
    category = unicodedata.category(character)
    return category[0] in {"L", "N"} or category[0] == "M"


def word_tokens(text: str) -> list[str]:
    """Return orthographic words while excluding surrounding punctuation."""
    result: list[str] = []
    index = 0
    while index < len(text):
        if not is_word_character(text[index]):
            index += 1
            continue
        start = index
        index += 1
        while index < len(text):
            if is_word_character(text[index]):
                index += 1
                continue
            if (
                text[index] in INTERNAL_JOINERS
                and index + 1 < len(text)
                and is_word_character(text[index + 1])
            ):
                index += 1
                continue
            break
        result.append(text[start:index])
    return result


def load_qac_words(path: Path) -> dict[str, list[str]]:
    uri = f"{path.resolve().as_uri()}?mode=ro"
    words_by_ayah: dict[str, list[str]] = defaultdict(list)
    with sqlite3.connect(uri, uri=True) as connection:
        connection.execute("PRAGMA query_only = ON")
        for qac_word_ref, surah, ayah in connection.execute(
            "SELECT qac_word_ref, surah, ayah FROM qac_words "
            "ORDER BY surah, ayah, word_index"
        ):
            words_by_ayah[f"{surah}:{ayah}"].append(str(qac_word_ref))
    if not words_by_ayah:
        raise BaselineValidationError(f"QAC database contains no words: {path}")
    return dict(words_by_ayah)


def validate_ayah(
    ayah: Any,
    index: int,
    words_by_ayah: dict[str, list[str]],
) -> dict[str, int]:
    location = f"ayat[{index}]"
    row = require_keys(
        ayah,
        {"ayah_ref", "baseline_text", "target_tokens"},
        location,
    )
    ayah_ref = row["ayah_ref"]
    if not isinstance(ayah_ref, str) or ayah_ref not in words_by_ayah:
        raise BaselineValidationError(
            f"{location}.ayah_ref: absent from canonical QAC: {ayah_ref!r}"
        )

    baseline_text = row["baseline_text"]
    if not isinstance(baseline_text, str) or not baseline_text.strip():
        raise BaselineValidationError(f"{location}.baseline_text: must be nonempty")
    if unicodedata.normalize("NFC", baseline_text) != baseline_text:
        raise BaselineValidationError(f"{location}.baseline_text: must use NFC")

    tokens = row["target_tokens"]
    if not isinstance(tokens, list) or not tokens:
        raise BaselineValidationError(f"{location}.target_tokens: must be nonempty")

    surfaces: list[str] = []
    cited_words: set[str] = set()
    qac_links = 0
    expected_words = set(words_by_ayah[ayah_ref])
    for token_index, token in enumerate(tokens):
        token_location = f"{location}.target_tokens[{token_index}]"
        if not isinstance(token, list) or len(token) != 2:
            raise BaselineValidationError(
                f"{token_location}: expected [surface, [qac_word_ref, ...]]"
            )
        surface, word_refs = token
        if not isinstance(surface, str) or not surface or any(char.isspace() for char in surface):
            raise BaselineValidationError(f"{token_location}[0]: invalid token surface")
        if unicodedata.normalize("NFC", surface) != surface:
            raise BaselineValidationError(f"{token_location}[0]: must use NFC")
        if (
            not isinstance(word_refs, list)
            or not word_refs
            or any(not isinstance(item, str) for item in word_refs)
        ):
            raise BaselineValidationError(
                f"{token_location}[1]: expected nonempty QAC word-ref array"
            )
        if len(word_refs) != len(set(word_refs)):
            raise BaselineValidationError(f"{token_location}[1]: duplicate QAC word refs")
        foreign = set(word_refs) - expected_words
        if foreign:
            raise BaselineValidationError(
                f"{token_location}[1]: foreign or unknown QAC refs: {sorted(foreign)}"
            )
        surfaces.append(surface)
        cited_words.update(word_refs)
        qac_links += len(word_refs)

    expected_surfaces = word_tokens(baseline_text)
    if surfaces != expected_surfaces:
        raise BaselineValidationError(
            f"{location}: target token surfaces differ from baseline words; "
            f"expected={expected_surfaces}, actual={surfaces}"
        )
    if cited_words != expected_words:
        raise BaselineValidationError(
            f"{location}: QAC word coverage differs; "
            f"missing={sorted(expected_words-cited_words)}, "
            f"foreign={sorted(cited_words-expected_words)}"
        )
    return {
        "target_tokens": len(tokens),
        "qac_words": len(expected_words),
        "qac_links": qac_links,
    }


def canonical_sort_key(ayah_ref: str) -> tuple[int, int]:
    surah, ayah = ayah_ref.split(":", 1)
    return int(surah), int(ayah)


def validate(
    baseline_path: Path,
    qac_path: Path,
    *,
    surah: int | None = None,
    require_complete: bool = False,
) -> dict[str, Any]:
    baseline_path = baseline_path.resolve()
    qac_path = qac_path.resolve()
    document = json.loads(baseline_path.read_text(encoding="utf-8"))
    root = require_keys(document, {"language", "ayat"}, "baseline")
    language = root["language"]
    if not isinstance(language, str) or LANGUAGE_RE.fullmatch(language) is None:
        raise BaselineValidationError("baseline.language: invalid BCP-47 language tag")

    words_by_ayah = load_qac_words(qac_path)
    ayat = root["ayat"]
    if not isinstance(ayat, list) or not ayat:
        raise BaselineValidationError("baseline.ayat: must be nonempty")
    refs = [row.get("ayah_ref") for row in ayat if isinstance(row, dict)]
    if len(refs) != len(ayat) or any(not isinstance(ref, str) for ref in refs):
        raise BaselineValidationError("baseline.ayat: invalid ayah rows")
    if len(refs) != len(set(refs)):
        raise BaselineValidationError("baseline.ayat: duplicate ayah refs")
    if refs != sorted(refs, key=canonical_sort_key):
        raise BaselineValidationError("baseline.ayat: must use canonical Quran order")

    if surah is not None:
        expected_refs = [
            ref for ref in words_by_ayah if int(ref.split(":", 1)[0]) == surah
        ]
        expected_refs.sort(key=canonical_sort_key)
        if refs != expected_refs:
            raise BaselineValidationError(
                f"baseline does not exactly cover S{surah}; "
                f"missing={sorted(set(expected_refs)-set(refs))}, "
                f"extra={sorted(set(refs)-set(expected_refs))}"
            )
    if require_complete and set(refs) != set(words_by_ayah):
        raise BaselineValidationError(
            f"baseline is not corpus-complete: "
            f"missing={len(set(words_by_ayah)-set(refs))}, "
            f"extra={len(set(refs)-set(words_by_ayah))}"
        )

    totals: dict[str, int] = defaultdict(int)
    for index, ayah in enumerate(ayat):
        counts = validate_ayah(ayah, index, words_by_ayah)
        for key, value in counts.items():
            totals[key] += value
    return {
        "protocol": "target-language-baseline-validation-v1",
        "language": language,
        "baseline_sha256": sha256_file(baseline_path),
        "qac_sha256": sha256_file(qac_path),
        "ayat": len(ayat),
        "counts": dict(totals),
        "complete_required": require_complete,
        "valid": True,
    }


def main() -> int:
    args = parse_args()
    try:
        report = validate(
            args.baseline,
            args.qac,
            surah=args.surah,
            require_complete=args.require_complete,
        )
    except (OSError, TypeError, ValueError, sqlite3.Error, BaselineValidationError) as error:
        print(json.dumps({"valid": False, "error": str(error)}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
