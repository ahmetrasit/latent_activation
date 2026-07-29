#!/usr/bin/env python3
"""Audit QAC root spellings against furuq_v4 stable root ids."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
import unicodedata
from collections import defaultdict
from contextlib import closing
from pathlib import Path
from typing import Any, Iterable

from workflow_common import atomic_write_json, atomic_write_text, sha256_file, utc_now


SCRIPT_ROOT = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_ROOT.parents[2]
QAC_PATH = REPO_ROOT / "resources" / "qac.sqlite"
FURUQ_PATH = REPO_ROOT / "resources" / "furuq_v4.sqlite"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "_status" / "v12_cross_run" / "audits"

ROOT_AUDIT_FIELDS = (
    "qac_root_join_key",
    "qac_root_ar",
    "qac_root_norm",
    "qac_root_canonical",
    "occurrences",
    "surah_count",
    "surahs",
    "example_refs",
    "example_surfaces",
    "example_lemmas",
    "status",
    "audit_class",
    "chosen_method",
    "chosen_root_ids",
    "source_exact_root_ids",
    "normalized_exact_root_ids",
    "canonical_root_ids",
    "legacy_root_norm_extra_root_ids",
    "legacy_root_norm_extra_branch_count",
    "chosen_branch_count",
    "notes",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--qac", type=Path, default=QAC_PATH)
    parser.add_argument("--furuq", type=Path, default=FURUQ_PATH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--prefix",
        default="qac-furuq-root-id-audit",
        help="output filename prefix",
    )
    return parser.parse_args()


def normalized_root(value: str) -> str:
    root = " ".join(str(value or "").split())
    if " " not in root and 3 <= len(root) <= 4 and all(
        "\u0621" <= character <= "\u064a" for character in root
    ):
        return " ".join(root)
    return root


def canonical_arabic(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    output: list[str] = []
    for character in normalized:
        if unicodedata.category(character) in {"Mn", "Me", "Cf"}:
            continue
        if character == "ـ":
            continue
        output.append(
            {
                "آ": "ا",
                "أ": "ا",
                "إ": "ا",
                "ٱ": "ا",
                "ى": "ي",
                "ؤ": "و",
                "ئ": "ي",
            }.get(character, character)
        )
    return "".join(output).replace(" ", "")


def canonical_root(value: str) -> str:
    return canonical_arabic(value).replace("ء", "ا")


def split_semicolon(value: str) -> list[str]:
    return [item for item in str(value or "").split(";") if item]


def ordered_unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for raw in values:
        value = str(raw)
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def join_values(values: Iterable[str]) -> str:
    return ";".join(ordered_unique(values))


def sort_root_ids(root_ids: Iterable[str]) -> list[str]:
    def key(root_id: str) -> tuple[int, str]:
        match = re.search(r"([0-9]+)$", root_id)
        return (int(match.group(1)) if match else 10**9, root_id)

    return sorted(ordered_unique(root_ids), key=key)


def connect_readonly(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    return connection


def load_qac_roots(path: Path) -> list[dict[str, Any]]:
    roots: dict[tuple[str, str], dict[str, Any]] = {}
    with closing(connect_readonly(path)) as connection:
        for row in connection.execute(
            """
            SELECT qac_ref, surah, ayah, word_index, surface_ar, lemma_ar,
                   root_ar, root_join_key
            FROM qac_morphemes
            WHERE root_join_key <> ''
            ORDER BY surah, ayah, word_index, morpheme_index
            """
        ):
            root_ar = normalized_root(str(row["root_ar"]))
            root_join_key = str(row["root_join_key"])
            key = (root_join_key, root_ar)
            record = roots.setdefault(
                key,
                {
                    "qac_root_join_key": root_join_key,
                    "qac_root_ar": root_ar,
                    "occurrences": 0,
                    "surahs": set(),
                    "refs": [],
                    "surfaces": [],
                    "lemmas": [],
                },
            )
            record["occurrences"] += 1
            record["surahs"].add(str(row["surah"]))
            ref = f"{row['surah']}:{row['ayah']}:{row['word_index']}"
            if len(record["refs"]) < 8:
                record["refs"].append(ref)
            if len(record["surfaces"]) < 8:
                record["surfaces"].append(str(row["surface_ar"]))
            if len(record["lemmas"]) < 8:
                record["lemmas"].append(str(row["lemma_ar"]))
    return sorted(
        roots.values(),
        key=lambda item: (-int(item["occurrences"]), item["qac_root_ar"]),
    )


def load_furuq_indexes(path: Path) -> dict[str, Any]:
    by_source: dict[str, list[str]] = defaultdict(list)
    by_normalized: dict[str, list[str]] = defaultdict(list)
    by_canonical: dict[str, list[str]] = defaultdict(list)
    root_info: dict[str, dict[str, str]] = {}
    branch_counts: dict[str, int] = defaultdict(int)

    with closing(connect_readonly(path)) as connection:
        for row in connection.execute(
            """
            SELECT root_id, root_norm, source_root_norm, registry_status, covered_by
            FROM roots
            ORDER BY root_id
            """
        ):
            root_id = str(row["root_id"])
            source = normalized_root(str(row["source_root_norm"]))
            norm = normalized_root(str(row["root_norm"]))
            canon = canonical_root(norm)
            root_info[root_id] = {
                "root_id": root_id,
                "source_root_norm": source,
                "root_norm": norm,
                "canonical_root": canon,
                "registry_status": str(row["registry_status"]),
                "covered_by": str(row["covered_by"]),
            }
            by_source[source].append(root_id)
            by_normalized[norm].append(root_id)
            by_canonical[canon].append(root_id)

        for row in connection.execute(
            """
            SELECT root_id, COUNT(*) AS branch_count
            FROM branch_images
            WHERE status = 'accepted'
              AND contaminated = 'no'
            GROUP BY root_id
            """
        ):
            branch_counts[str(row["root_id"])] = int(row["branch_count"])

    return {
        "by_source": {key: sort_root_ids(value) for key, value in by_source.items()},
        "by_normalized": {
            key: sort_root_ids(value) for key, value in by_normalized.items()
        },
        "by_canonical": {
            key: sort_root_ids(value) for key, value in by_canonical.items()
        },
        "root_info": root_info,
        "branch_counts": dict(branch_counts),
    }


def branch_count(root_ids: Iterable[str], branch_counts: dict[str, int]) -> int:
    return sum(branch_counts.get(root_id, 0) for root_id in root_ids)


def classify(
    qac_root: dict[str, Any],
    furuq: dict[str, Any],
) -> dict[str, Any]:
    root_norm = normalized_root(str(qac_root["qac_root_ar"]))
    root_canonical = canonical_root(root_norm)
    source_ids = furuq["by_source"].get(root_norm, [])
    normalized_ids = furuq["by_normalized"].get(root_norm, [])
    canonical_ids = furuq["by_canonical"].get(root_canonical, [])

    chosen_method = ""
    chosen_ids: list[str] = []
    notes: list[str] = []
    if source_ids:
        chosen_method = "source_exact"
        chosen_ids = source_ids
    elif normalized_ids:
        chosen_method = "normalized_exact"
        chosen_ids = normalized_ids
    elif canonical_ids:
        chosen_method = "canonical_fallback"
        chosen_ids = canonical_ids

    if not chosen_ids:
        status = "error_unresolved"
    elif len(chosen_ids) > 1:
        status = f"error_ambiguous_{chosen_method}"
    elif chosen_method == "source_exact":
        status = "ok_source_exact"
    elif chosen_method == "normalized_exact":
        status = "ok_normalized_unique"
    else:
        status = "review_canonical_only"

    source_set = set(source_ids)
    normalized_set = set(normalized_ids)
    canonical_set = set(canonical_ids)
    chosen_set = set(chosen_ids)
    legacy_extra = sort_root_ids(normalized_set - chosen_set)

    if source_ids and normalized_set and normalized_set != source_set:
        if legacy_extra:
            status = "error_legacy_root_norm_overinclude"
        notes.append("root_norm lookup returns different root_id set than source_exact")
    if chosen_method == "source_exact" and canonical_set and canonical_set != source_set:
        notes.append("canonical fallback would return different root_id set")
    if chosen_method != "source_exact" and source_ids:
        notes.append("unexpected source ids present outside source_exact")
    if not normalized_ids and canonical_ids:
        notes.append("no root_norm match; canonical fallback only")
    if not source_ids and normalized_ids:
        notes.append("no source_root_norm exact match")

    branch_counts = furuq["branch_counts"]
    row = {
        "qac_root_join_key": qac_root["qac_root_join_key"],
        "qac_root_ar": qac_root["qac_root_ar"],
        "qac_root_norm": root_norm,
        "qac_root_canonical": root_canonical,
        "occurrences": qac_root["occurrences"],
        "surah_count": len(qac_root["surahs"]),
        "surahs": join_values(sorted(qac_root["surahs"], key=lambda raw: int(raw))),
        "example_refs": join_values(qac_root["refs"]),
        "example_surfaces": join_values(qac_root["surfaces"]),
        "example_lemmas": join_values(qac_root["lemmas"]),
        "status": status,
        "audit_class": (
            "error"
            if status.startswith("error_")
            else "review"
            if status.startswith("review_")
            else "ok"
        ),
        "chosen_method": chosen_method,
        "chosen_root_ids": join_values(chosen_ids),
        "source_exact_root_ids": join_values(source_ids),
        "normalized_exact_root_ids": join_values(normalized_ids),
        "canonical_root_ids": join_values(canonical_ids),
        "legacy_root_norm_extra_root_ids": join_values(legacy_extra),
        "legacy_root_norm_extra_branch_count": branch_count(legacy_extra, branch_counts),
        "chosen_branch_count": branch_count(chosen_ids, branch_counts),
        "notes": join_values(notes),
    }
    return row


def write_tsv(path: Path, fields: tuple[str, ...], rows: Iterable[dict[str, Any]]) -> None:
    lines = ["\t".join(fields)]
    for row in rows:
        values: list[str] = []
        for field in fields:
            value = row.get(field, "")
            rendered = "" if value is None else str(value)
            if "\t" in rendered or "\n" in rendered or "\r" in rendered:
                raise ValueError(f"{path}: field {field} has unsafe whitespace")
            values.append(rendered)
        lines.append("\t".join(values))
    atomic_write_text(path, "\n".join(lines) + "\n")


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_status: dict[str, int] = defaultdict(int)
    by_audit_class: dict[str, int] = defaultdict(int)
    occurrence_by_status: dict[str, int] = defaultdict(int)
    occurrence_by_audit_class: dict[str, int] = defaultdict(int)
    for row in rows:
        status = str(row["status"])
        audit_class = str(row["audit_class"])
        by_status[status] += 1
        by_audit_class[audit_class] += 1
        occurrence_by_status[status] += int(row["occurrences"])
        occurrence_by_audit_class[audit_class] += int(row["occurrences"])

    return {
        "root_rows": len(rows),
        "qac_root_keys": len({row["qac_root_join_key"] for row in rows}),
        "qac_root_spellings": len({row["qac_root_ar"] for row in rows}),
        "total_rooted_morpheme_occurrences": sum(
            int(row["occurrences"]) for row in rows
        ),
        "status_counts": dict(sorted(by_status.items())),
        "audit_class_counts": dict(sorted(by_audit_class.items())),
        "occurrence_counts_by_status": dict(sorted(occurrence_by_status.items())),
        "occurrence_counts_by_audit_class": dict(
            sorted(occurrence_by_audit_class.items())
        ),
        "non_ok_root_rows": sum(
            count for audit_class, count in by_audit_class.items() if audit_class != "ok"
        ),
        "non_ok_occurrences": sum(
            count
            for audit_class, count in occurrence_by_audit_class.items()
            if audit_class != "ok"
        ),
    }


def markdown_report(summary: dict[str, Any], rows: list[dict[str, Any]]) -> str:
    review_rows = [
        row
        for row in rows
        if row["audit_class"] != "ok"
    ]
    priority = {
        "error_legacy_root_norm_overinclude": 0,
        "error_ambiguous_source_exact": 1,
        "error_ambiguous_normalized_exact": 2,
        "error_ambiguous_canonical_fallback": 3,
        "review_canonical_only": 4,
        "error_unresolved": 5,
    }
    review_rows.sort(
        key=lambda row: (
            priority.get(str(row["status"]), 99),
            -int(row["occurrences"]),
            str(row["qac_root_ar"]),
        )
    )

    lines = [
        "# QAC to furuq_v4 root-id audit",
        "",
        f"Generated UTC: `{utc_now()}`",
        "",
        "## Summary",
        "",
        f"- QAC rooted rows audited: `{summary['root_rows']}`",
        f"- QAC root keys audited: `{summary['qac_root_keys']}`",
        f"- Rooted morpheme occurrences: `{summary['total_rooted_morpheme_occurrences']}`",
        f"- Non-ok root rows: `{summary['non_ok_root_rows']}`",
        f"- Non-ok rooted morpheme occurrences: `{summary['non_ok_occurrences']}`",
        "",
        "## Status Counts",
        "",
        "| status | roots | occurrences |",
        "| --- | ---: | ---: |",
    ]
    occurrence_counts = summary["occurrence_counts_by_status"]
    for status, count in summary["status_counts"].items():
        lines.append(f"| `{status}` | {count} | {occurrence_counts.get(status, 0)} |")

    lines.extend(
        [
            "",
            "## Audit Class Counts",
            "",
            "| class | roots | occurrences |",
            "| --- | ---: | ---: |",
        ]
    )
    occurrence_class_counts = summary["occurrence_counts_by_audit_class"]
    for audit_class, count in summary["audit_class_counts"].items():
        lines.append(
            f"| `{audit_class}` | {count} | {occurrence_class_counts.get(audit_class, 0)} |"
        )

    lines.extend(
        [
            "",
            "## Non-OK Rows",
            "",
            "| class | status | qac root | occ | chosen | source_exact | normalized_exact | canonical | examples | notes |",
            "| --- | --- | --- | ---: | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in review_rows:
        lines.append(
            "| `{audit_class}` | `{status}` | `{root}` | {occ} | `{chosen}` | `{source}` | `{norm}` | `{canon}` | {examples} | {notes} |".format(
                audit_class=row["audit_class"],
                status=row["status"],
                root=row["qac_root_ar"],
                occ=row["occurrences"],
                chosen=row["chosen_root_ids"],
                source=row["source_exact_root_ids"],
                norm=row["normalized_exact_root_ids"],
                canon=row["canonical_root_ids"],
                examples=row["example_refs"],
                notes=row["notes"],
            )
        )
    if not review_rows:
        lines.append("| ok | ok | none | 0 |  |  |  |  |  |  |")

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- `ok_source_exact`: QAC `root_ar` exactly resolves to one furuq `source_root_norm`.",
            "- `ok_normalized_unique`: no exact source root exists, but furuq `root_norm` uniquely matches.",
            "- `error_legacy_root_norm_overinclude`: exact source mapping is known, but a `root_norm`-only lookup pulls extra root_ids.",
            "- `review_canonical_only`: only the lossy canonical fallback matches.",
            "- `error_ambiguous_*`: the resolver returns multiple root_ids at that stage.",
            "- `error_unresolved`: no furuq root_id is reachable from the audited QAC spelling.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    args = parse_args()
    for path in (args.qac, args.furuq):
        if not path.is_file():
            raise SystemExit(f"missing input: {path}")

    qac_roots = load_qac_roots(args.qac)
    furuq = load_furuq_indexes(args.furuq)
    rows = [classify(root, furuq) for root in qac_roots]
    summary = summarize(rows)
    summary.update(
        {
            "protocol": "qac-furuq-root-id-audit-v1",
            "generated_utc": utc_now(),
            "inputs": {
                "qac_path": args.qac.relative_to(REPO_ROOT).as_posix(),
                "qac_sha256": sha256_file(args.qac),
                "furuq_path": args.furuq.relative_to(REPO_ROOT).as_posix(),
                "furuq_sha256": sha256_file(args.furuq),
            },
        }
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    tsv_path = args.output_dir / f"{args.prefix}.tsv"
    json_path = args.output_dir / f"{args.prefix}.json"
    md_path = args.output_dir / f"{args.prefix}.md"
    write_tsv(tsv_path, ROOT_AUDIT_FIELDS, rows)
    atomic_write_json(json_path, {"summary": summary, "rows": rows})
    atomic_write_text(md_path, markdown_report(summary, rows))
    print(f"wrote {tsv_path}")
    print(f"wrote {json_path}")
    print(f"wrote {md_path}")
    print(json.dumps(summary["status_counts"], ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
