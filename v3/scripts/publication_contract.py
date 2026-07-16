#!/usr/bin/env python3
"""Shared contract, rendering, and listenability checks for V3 publications."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


RECORD_FIELDS = ("kind", "grades", "title", "paragraphs")
RECORD_KINDS = {"opening", "finding", "closing"}
GRADE_PATTERN = re.compile(
    r"^(GÜÇLÜ|ORTA|ZAYIF)\s*/\s*(A|B|C|C-koşullu)(?:\s+.+)?$"
)
SPOKEN_GRADE_PATTERN = re.compile(
    r"\b(?:GÜÇLÜ|ORTA|ZAYIF)\s*/\s*(?:A|B|C(?:-koşullu)?)\b"
)
BARE_ROOT_PATTERN = re.compile(
    r"(?<![\u0600-\u06ff])"
    r"[\u0621-\u064a][\u064b-\u065f\u0670]*"
    r"(?:\s+[\u0621-\u064a][\u064b-\u065f\u0670]*){2,3}"
    r"(?![\u0600-\u06ff])"
)
ARABIC_RUN_PATTERN = re.compile(r"[\u0600-\u06ff]+(?:\s+[\u0600-\u06ff]+)*")
PRODUCTION_VOCABULARY_PATTERN = re.compile(
    r"\b(?:kamera|kameraya|kameranın|kameradan|camera|kadraj|kadrajda|zoom|"
    r"yakın plan|close-up|sahne geçişi|sinematik)\b",
    re.IGNORECASE,
)
MECHANICAL_OPENING_PATTERN = re.compile(
    r"^(?:metin\b|bu bulgu\b|bu gözlem\b)|"
    r"\b(?:yapmaz|söylemez|değildir|bulunmaz|yerine geçmez|"
    r"üretmez|dönüşmez|kılmaz|ortadan kaldırmaz)\b",
    re.IGNORECASE,
)
LEXICAL_INVENTORY_OPENING_PATTERN = re.compile(
    r"^[^.!?]{0,140}\banlamındaki\b[^.!?]{0,140}\b(?:kök|dal|kelime)",
    re.IGNORECASE,
)
STOCK_CLOSING_PATTERN = re.compile(
    r"^(?:böylece|bu yüzden|sonuç olarak)\b",
    re.IGNORECASE,
)


class PublicationError(RuntimeError):
    pass


def _is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _record_label(index: int, record: Mapping[str, Any] | None = None) -> str:
    kind = record.get("kind") if isinstance(record, Mapping) else None
    return f"record {index + 1}" + (f" ({kind})" if kind else "")


def load_publication(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open(encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as error:
                raise PublicationError(
                    f"{path}:{line_number}: invalid JSON: {error.msg}"
                ) from error
            if not isinstance(value, dict):
                raise PublicationError(
                    f"{path}:{line_number}: each JSONL record must be an object"
                )
            records.append(value)

    errors = validate_records(records)
    if errors:
        raise PublicationError("\n".join(f"{path}: {error}" for error in errors))
    return records


def validate_records(records: Sequence[Mapping[str, Any]]) -> list[str]:
    errors: list[str] = []
    if not records:
        return ["publication must contain at least one record"]

    if records[0].get("kind") != "opening":
        errors.append("the first record must have kind 'opening'")
    if records[-1].get("kind") != "closing":
        errors.append("the final record must have kind 'closing'")

    opening_count = sum(record.get("kind") == "opening" for record in records)
    closing_count = sum(record.get("kind") == "closing" for record in records)
    finding_count = sum(record.get("kind") == "finding" for record in records)
    if opening_count != 1:
        errors.append(f"publication must contain exactly one opening; found {opening_count}")
    if closing_count != 1:
        errors.append(f"publication must contain exactly one closing; found {closing_count}")
    if finding_count == 0:
        errors.append("publication must contain at least one finding")

    for index, record in enumerate(records):
        label = _record_label(index, record)
        keys = set(record)
        expected = set(RECORD_FIELDS)
        missing = sorted(expected - keys)
        extra = sorted(keys - expected)
        if missing:
            errors.append(f"{label}: missing fields: {', '.join(missing)}")
        if extra:
            errors.append(f"{label}: unexpected fields: {', '.join(extra)}")

        kind = record.get("kind")
        if kind not in RECORD_KINDS:
            errors.append(f"{label}: kind must be opening, finding, or closing")
            continue
        if 0 < index < len(records) - 1 and kind != "finding":
            errors.append(f"{label}: every middle record must have kind 'finding'")

        title = record.get("title")
        if not _is_nonempty_string(title):
            errors.append(f"{label}: title must be a non-empty string")
        elif "\n" in title or "\r" in title:
            errors.append(f"{label}: title must not contain line breaks")

        grades = record.get("grades")
        if not isinstance(grades, list):
            errors.append(f"{label}: grades must be an array")
        else:
            if kind == "finding" and not grades:
                errors.append(f"{label}: a finding must have at least one grade")
            if kind != "finding" and grades:
                errors.append(f"{label}: opening and closing grades must be empty")
            if len(grades) != len(set(map(str, grades))):
                errors.append(f"{label}: grades must not contain duplicates")
            for grade_index, grade in enumerate(grades, start=1):
                if not _is_nonempty_string(grade) or not GRADE_PATTERN.fullmatch(grade):
                    errors.append(
                        f"{label}: grade {grade_index} does not match "
                        "'GÜÇLÜ|ORTA|ZAYIF / A|B|C|C-koşullu [qualifier]'"
                    )

        paragraphs = record.get("paragraphs")
        if not isinstance(paragraphs, list):
            errors.append(f"{label}: paragraphs must be an array")
            continue
        maximum = 3 if kind == "finding" else 2
        if not 1 <= len(paragraphs) <= maximum:
            errors.append(
                f"{label}: paragraphs must contain between 1 and {maximum} items"
            )
        for paragraph_index, paragraph in enumerate(paragraphs, start=1):
            if not _is_nonempty_string(paragraph):
                errors.append(
                    f"{label}: paragraph {paragraph_index} must be a non-empty string"
                )
                continue
            if "\n" in paragraph or "\r" in paragraph:
                errors.append(
                    f"{label}: paragraph {paragraph_index} must not contain line breaks"
                )

        text_fields: list[tuple[str, str]] = []
        if isinstance(title, str):
            text_fields.append(("title", title))
        if isinstance(paragraphs, list):
            text_fields.extend(
                (f"paragraph {paragraph_index}", paragraph)
                for paragraph_index, paragraph in enumerate(paragraphs, start=1)
                if isinstance(paragraph, str)
            )
        for field, text in text_fields:
            if "`" in text or "```" in text or text.lstrip().startswith("#"):
                errors.append(f"{label}: {field} must not contain Markdown syntax")
            if SPOKEN_GRADE_PATTERN.search(text):
                errors.append(f"{label}: {field} must not contain spoken grade codes")
            if BARE_ROOT_PATTERN.search(text):
                errors.append(f"{label}: {field} contains a bare spaced Arabic root")
            if PRODUCTION_VOCABULARY_PATTERN.search(text):
                errors.append(
                    f"{label}: {field} exposes cinematic production vocabulary"
                )
    return errors


def _words(text: str) -> list[str]:
    return re.findall(r"[^\W\d_]+", text.casefold(), flags=re.UNICODE)


def _first_sentence(text: str) -> str:
    return re.split(r"(?<=[.!?])\s+", text.strip(), maxsplit=1)[0]


def _last_sentence(text: str) -> str:
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return sentences[-1]


def style_warnings(records: Sequence[Mapping[str, Any]]) -> list[str]:
    warnings: list[str] = []
    findings = [record for record in records if record.get("kind") == "finding"]
    opening_keys: list[tuple[int, str]] = []
    first_words: Counter[str] = Counter()
    finding_titles: Counter[str] = Counter()
    stock_closings: Counter[str] = Counter()

    for index, record in enumerate(records):
        label = _record_label(index, record)
        title = str(record.get("title", ""))
        title_words = _words(title)
        if len(title_words) > 14:
            warnings.append(f"{label}: title is long for a spoken section")

        paragraphs = record.get("paragraphs")
        if not isinstance(paragraphs, list):
            continue
        if record.get("kind") == "finding" and len(paragraphs) != 2:
            warnings.append(
                f"{label}: findings normally use two paragraphs; found {len(paragraphs)}"
            )

        for paragraph_index, paragraph in enumerate(paragraphs, start=1):
            if not isinstance(paragraph, str):
                continue
            word_count = len(paragraph.split())
            if word_count > 110:
                warnings.append(
                    f"{label}: paragraph {paragraph_index} has {word_count} words"
                )
            arabic_runs = ARABIC_RUN_PATTERN.findall(paragraph)
            if len(arabic_runs) > 3:
                warnings.append(
                    f"{label}: paragraph {paragraph_index} contains "
                    f"{len(arabic_runs)} Arabic spans"
                )

        if record.get("kind") != "finding" or not paragraphs:
            continue
        finding_titles[title.casefold()] += 1
        first = _first_sentence(str(paragraphs[0]))
        first_tokens = _words(first)
        if first_tokens:
            first_words[first_tokens[0]] += 1
            opening_keys.append((index, " ".join(first_tokens[:3])))
        if MECHANICAL_OPENING_PATTERN.search(first):
            warnings.append(f"{label}: first sentence opens through a mechanical boundary")
        if LEXICAL_INVENTORY_OPENING_PATTERN.search(first):
            warnings.append(f"{label}: first sentence opens as a lexical inventory")

        final = _last_sentence(str(paragraphs[-1]))
        closing_match = STOCK_CLOSING_PATTERN.match(final)
        if closing_match:
            stock_closings[closing_match.group(0).casefold()] += 1

    for (left_index, left), (right_index, right) in zip(
        opening_keys, opening_keys[1:]
    ):
        if left and left == right:
            warnings.append(
                f"records {left_index + 1} and {right_index + 1}: "
                f"adjacent findings share the opening frame {left!r}"
            )

    finding_total = len(findings)
    for title, count in finding_titles.items():
        if count > 1:
            warnings.append(f"finding title {title!r} repeats {count} times")
    for word, count in first_words.items():
        if count >= 3 and finding_total and count / finding_total >= 0.25:
            warnings.append(
                f"finding openings repeat {word!r} {count} times "
                f"across {finding_total} findings"
            )
    for phrase, count in stock_closings.items():
        if count > 2:
            warnings.append(f"finding conclusions repeat {phrase!r} {count} times")
    return warnings


def render_markdown(records: Sequence[Mapping[str, Any]]) -> str:
    lines: list[str] = []
    for record in records:
        heading = "#" if record["kind"] == "opening" else "##"
        lines.append(f"{heading} {record['title'].strip()}")
        lines.append("")
        for paragraph in record["paragraphs"]:
            lines.append(paragraph.strip())
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def publication_sections(
    records: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    sections: list[dict[str, Any]] = []
    for record in records:
        title = str(record["title"]).strip()
        paragraphs = [{"kind": "section_title", "text": title}]
        paragraphs.extend(
            {"kind": "paragraph", "text": str(paragraph).strip()}
            for paragraph in record["paragraphs"]
        )
        sections.append(
            {
                "title": title,
                "kind": record["kind"],
                "grades": list(record["grades"]),
                "paragraphs": paragraphs,
            }
        )
    return sections


def write_jsonl(path: Path, records: Iterable[Mapping[str, Any]]) -> None:
    path.write_text(
        "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in records),
        encoding="utf-8",
    )
