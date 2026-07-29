#!/usr/bin/env python3
"""Audit QAC roots against the frozen MASAQ/Quran corpus by word reference.

The frozen corpus has one row per QAC/TSV word aligned to MASAQ segment refs and
includes a corrected ``root_arabic``. This script joins that row to QAC
morphemes at the same ``sura:ayah:word`` and resolves the frozen root to
``furuq_v4.roots.root_id`` using ``source_root_norm`` first.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import re
import sqlite3
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_QAC_DB = ROOT / "resources" / "qac.sqlite"
DEFAULT_FURUQ_DB = ROOT / "resources" / "furuq_v4.sqlite"
DEFAULT_FROZEN = ROOT.parent / "quran-roots" / "_corpus" / "sources" / "frozen" / "corpus.tsv.gz"
DEFAULT_OUT_DIR = ROOT / "_status" / "v12_cross_run" / "audits"

TATWEEL = "\u0640"
DIACRITICS_RE = re.compile("[\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed]")
ROOT_IDENTITY_NORMALIZATION = str.maketrans(
    {
        "أ": "ء",
        "إ": "ء",
        "آ": "ء",
        "ؤ": "ء",
        "ئ": "ء",
        "ى": "ي",
        "ة": "ه",
    }
)
HAMZA_NORMALIZATION = str.maketrans(
    {
        "أ": "ا",
        "إ": "ا",
        "آ": "ا",
        "ٱ": "ا",
        "ؤ": "و",
        "ئ": "ي",
        "ى": "ي",
        "ة": "ه",
    }
)


def normalize_root(root: str) -> str:
    root = DIACRITICS_RE.sub("", root or "").replace(TATWEEL, "")
    root = root.translate(ROOT_IDENTITY_NORMALIZATION)
    return " ".join(re.findall(r"[\u0600-\u06ff]", root))


def normalize_arabic(text: str) -> str:
    text = DIACRITICS_RE.sub("", text or "").replace(TATWEEL, "")
    text = text.translate(HAMZA_NORMALIZATION)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def root_join_key(root_norm: str) -> str:
    return root_norm.replace(" ", "")


def sample_add(samples: list[str], value: str, limit: int = 8) -> None:
    if value and value not in samples and len(samples) < limit:
        samples.append(value)


@dataclass(frozen=True)
class FuruqRoot:
    root_id: str
    root_norm: str
    source_root_norm: str


def load_furuq_roots(path: Path) -> tuple[dict[str, FuruqRoot], dict[str, list[FuruqRoot]]]:
    by_source: dict[str, FuruqRoot] = {}
    by_norm: dict[str, list[FuruqRoot]] = defaultdict(list)
    with sqlite3.connect(path) as conn:
        conn.row_factory = sqlite3.Row
        for row in conn.execute(
            "SELECT root_id, root_norm, source_root_norm FROM roots ORDER BY root_id"
        ):
            root = FuruqRoot(
                root_id=row["root_id"],
                root_norm=row["root_norm"],
                source_root_norm=row["source_root_norm"],
            )
            by_source[root.source_root_norm] = root
            by_norm[root.root_norm].append(root)
    return by_source, by_norm


def resolve_furuq(
    frozen_root_norm: str,
    by_source: dict[str, FuruqRoot],
    by_norm: dict[str, list[FuruqRoot]],
) -> tuple[str, str, str, str]:
    source_match = by_source.get(frozen_root_norm)
    if source_match:
        return (
            source_match.root_id,
            source_match.root_norm,
            source_match.source_root_norm,
            "source_root_norm",
        )
    norm_matches = by_norm.get(frozen_root_norm, [])
    if len(norm_matches) == 1:
        root = norm_matches[0]
        return root.root_id, root.root_norm, root.source_root_norm, "root_norm_unique"
    if len(norm_matches) > 1:
        return (
            "|".join(root.root_id for root in norm_matches),
            frozen_root_norm,
            "|".join(root.source_root_norm for root in norm_matches),
            "root_norm_ambiguous",
        )
    return "", "", "", "missing_furuq_root"


def load_qac_by_ayah(path: Path) -> tuple[dict[tuple[int, int], list[dict[str, str]]], Counter[str]]:
    by_ayah: dict[tuple[int, int], list[dict[str, str]]] = defaultdict(list)
    root_counts: Counter[str] = Counter()
    with sqlite3.connect(path) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            """
            SELECT qac_ref, qac_word_ref, surface_ar, stem_ar, lemma_ar,
                   root_ar, root_join_key, pos, morpheme_role
            FROM qac_morphemes
            WHERE root_join_key != ''
            ORDER BY surah, ayah, word_index, morpheme_index
            """
        )
        ayah_ordinals: Counter[tuple[int, int]] = Counter()
        for row in rows:
            key = (int(row["qac_ref"].split(":")[0]), int(row["qac_ref"].split(":")[1]))
            ayah_ordinals[key] += 1
            rec = dict(row)
            rec["ayah_morpheme_ordinal"] = str(ayah_ordinals[key])
            by_ayah[key].append(rec)
            root_counts[normalize_root(row["root_ar"])] += 1
    return by_ayah, root_counts


def iter_frozen_rows(path: Path):
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            frozen_root_norm = normalize_root(row.get("root_arabic", ""))
            if not frozen_root_norm:
                continue
            yield row, frozen_root_norm


def split_refs(value: str) -> list[str]:
    return [part for part in (value or "").split("|") if part]


def frozen_search_keys(row: dict[str, str]) -> set[str]:
    keys: set[str] = set()
    for field in (
        "tsv_arabic_search_key",
        "masaq_arabic_search_key",
        "arabic_no_diacritics_search_key",
        "arabic_folded_search_key",
        "tsv_arabic_uthmani",
        "masaq_joined_stems",
    ):
        for part in split_refs(row.get(field, "")):
            key = normalize_arabic(part)
            if key:
                keys.add(key)
    return keys


def select_qac_rows(
    qac_by_ayah: dict[tuple[int, int], list[dict[str, str]]],
    frozen: dict[str, str],
) -> tuple[list[dict[str, str]], str, str]:
    ayah_key = (int(frozen["sura"]), int(frozen["ayah"]))
    rooted = [
        row for row in qac_by_ayah.get(ayah_key, []) if normalize_root(row["root_ar"])
    ]
    keys = frozen_search_keys(frozen)
    matched = [
        row
        for row in rooted
        if {
            normalize_arabic(row["surface_ar"]),
            normalize_arabic(row["stem_ar"]),
            normalize_arabic(row["lemma_ar"]),
        }
        & keys
    ]
    if not matched:
        return [], "", "no_surface_or_stem_match_in_ayah"

    roots = {normalize_root(row["root_ar"]) for row in matched}
    if len(matched) == 1 or len(roots) == 1:
        return matched, "|".join(row["qac_word_ref"] for row in matched), "surface_or_stem_match"

    try:
        frozen_ordinal = int(frozen.get("tsv_word_id", "0") or "0")
    except ValueError:
        frozen_ordinal = 0
    nearest_distance = min(
        abs(int(row["ayah_morpheme_ordinal"]) - frozen_ordinal) for row in matched
    )
    nearest = [
        row
        for row in matched
        if abs(int(row["ayah_morpheme_ordinal"]) - frozen_ordinal) == nearest_distance
    ]
    return nearest, "|".join(row["qac_word_ref"] for row in nearest), "surface_or_stem_match_position_tie_break"


def classify(qac_roots: list[str], frozen_root_norm: str) -> str:
    if not qac_roots:
        return "no_qac_root_at_word"
    unique = set(qac_roots)
    if frozen_root_norm in unique:
        return "same_word_same_root"
    if len(unique) > 1:
        return "same_word_qac_multi_root_diff"
    return "same_word_root_diff"


def build(
    args: argparse.Namespace,
) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]], dict[str, object]]:
    qac_by_ayah, all_qac_root_counts = load_qac_by_ayah(args.qac_db)
    by_source, by_norm = load_furuq_roots(args.furuq_db)

    occurrences: list[dict[str, str]] = []
    grouped: dict[tuple[str, str, str], dict[str, object]] = {}
    status_counts: Counter[str] = Counter()
    frozen_root_occurrences: Counter[str] = Counter()
    qac_root_occurrences: Counter[str] = Counter()

    for frozen, frozen_root_norm in iter_frozen_rows(args.frozen_corpus):
        ref = frozen["tsv_word_ref"]
        qac_rows, qac_word_refs, qac_match_mode = select_qac_rows(qac_by_ayah, frozen)
        qac_roots = [normalize_root(row["root_ar"]) for row in qac_rows if normalize_root(row["root_ar"])]
        qac_root_values = sorted(set(qac_roots))
        qac_root_norm = "|".join(qac_root_values)
        status = classify(qac_roots, frozen_root_norm)
        status_counts[status] += 1
        frozen_root_occurrences[frozen_root_norm] += 1
        for qac_root in qac_root_values:
            qac_root_occurrences[qac_root] += 1

        root_id, furuq_root_norm, furuq_source_root_norm, resolution = resolve_furuq(
            frozen_root_norm, by_source, by_norm
        )

        occurrence = {
            "status": status,
            "word_ref": ref,
            "qac_word_refs": qac_word_refs,
            "qac_match_mode": qac_match_mode,
            "masaq_segment_refs": frozen.get("masaq_segment_refs", ""),
            "alignment_group_id": frozen.get("alignment_group_id", ""),
            "surface_ar": frozen.get("tsv_arabic_uthmani", ""),
            "masaq_joined_arabic": frozen.get("masaq_joined_arabic", ""),
            "frozen_root_norm": frozen_root_norm,
            "frozen_root_raw": frozen.get("root_arabic", ""),
            "frozen_tsv_root_raw": frozen.get("tsv_root_arabic", ""),
            "root_correction_status": frozen.get("root_correction_status", ""),
            "root_correction_rule_id": frozen.get("root_correction_rule_id", ""),
            "qac_root_norm": qac_root_norm,
            "qac_root_ar": "|".join(sorted({row["root_ar"] for row in qac_rows if row["root_ar"]})),
            "qac_ref": "|".join(row["qac_ref"] for row in qac_rows),
            "qac_surface_ar": "|".join(row["surface_ar"] for row in qac_rows),
            "qac_stem_ar": "|".join(row["stem_ar"] for row in qac_rows),
            "qac_lemma_ar": "|".join(row["lemma_ar"] for row in qac_rows),
            "qac_pos": "|".join(row["pos"] for row in qac_rows),
            "furuq_root_id": root_id,
            "furuq_root_norm": furuq_root_norm,
            "furuq_source_root_norm": furuq_source_root_norm,
            "furuq_resolution": resolution,
        }
        occurrences.append(occurrence)

        key = (qac_root_norm or "(none)", frozen_root_norm, root_id)
        rec = grouped.setdefault(
            key,
            {
                "qac_root_norm": qac_root_norm or "(none)",
                "frozen_root_norm": frozen_root_norm,
                "furuq_root_id": root_id,
                "furuq_root_norm": furuq_root_norm,
                "furuq_source_root_norm": furuq_source_root_norm,
                "furuq_resolution": resolution,
                "occurrences": 0,
                "statuses": Counter(),
                "root_correction_statuses": Counter(),
                "sample_refs": [],
                "sample_surfaces": [],
                "sample_qac_lemmas": [],
                "qac_match_modes": Counter(),
            },
        )
        rec["occurrences"] = int(rec["occurrences"]) + 1
        rec["statuses"][status] += 1
        rec["root_correction_statuses"][frozen.get("root_correction_status", "")] += 1
        rec["qac_match_modes"][qac_match_mode] += 1
        sample_add(rec["sample_refs"], ref)
        sample_add(rec["sample_surfaces"], frozen.get("tsv_arabic_uthmani", ""))
        sample_add(rec["sample_qac_lemmas"], occurrence["qac_lemma_ar"])

    grouped_rows: list[dict[str, str]] = []
    qac_map_acc: dict[str, dict[str, object]] = {}
    for rec in grouped.values():
        grouped_row = {
            "qac_root_norm": str(rec["qac_root_norm"]),
            "frozen_root_norm": str(rec["frozen_root_norm"]),
            "furuq_root_id": str(rec["furuq_root_id"]),
            "furuq_root_norm": str(rec["furuq_root_norm"]),
            "furuq_source_root_norm": str(rec["furuq_source_root_norm"]),
            "furuq_resolution": str(rec["furuq_resolution"]),
            "occurrences": str(rec["occurrences"]),
            "statuses": "|".join(f"{k}:{v}" for k, v in sorted(rec["statuses"].items())),
            "root_correction_statuses": "|".join(
                f"{k or '(blank)'}:{v}" for k, v in sorted(rec["root_correction_statuses"].items())
            ),
            "qac_match_modes": "|".join(
                f"{k}:{v}" for k, v in sorted(rec["qac_match_modes"].items())
            ),
            "sample_refs": "|".join(rec["sample_refs"]),
            "sample_surfaces": "|".join(rec["sample_surfaces"]),
            "sample_qac_lemmas": "|".join(rec["sample_qac_lemmas"]),
        }
        grouped_rows.append(grouped_row)

        qac_root = grouped_row["qac_root_norm"]
        if qac_root == "(none)" or "|" in qac_root:
            continue
        map_rec = qac_map_acc.setdefault(
            qac_root,
            {
                "matched_occurrences": 0,
                "targets": Counter(),
                "status_counts": Counter(),
                "sample_refs": [],
                "sample_surfaces": [],
            },
        )
        count = int(grouped_row["occurrences"])
        map_rec["matched_occurrences"] = int(map_rec["matched_occurrences"]) + count
        target_key = "\u001f".join(
            [
                grouped_row["frozen_root_norm"],
                grouped_row["furuq_root_id"],
                grouped_row["furuq_root_norm"],
                grouped_row["furuq_source_root_norm"],
                grouped_row["furuq_resolution"],
            ]
        )
        map_rec["targets"][target_key] += count
        for part in grouped_row["statuses"].split("|"):
            status, _, value = part.partition(":")
            if status:
                map_rec["status_counts"][status] += int(value or "0")
        for ref in split_refs(grouped_row["sample_refs"]):
            sample_add(map_rec["sample_refs"], ref)
        for surface in split_refs(grouped_row["sample_surfaces"]):
            sample_add(map_rec["sample_surfaces"], surface)

    qac_map_rows: list[dict[str, str]] = []
    for qac_root, total_count in sorted(all_qac_root_counts.items()):
        rec = qac_map_acc.get(qac_root)
        if not rec:
            qac_map_rows.append(
                {
                    "qac_root_norm": qac_root,
                    "qac_total_occurrences": str(total_count),
                    "matched_occurrences": "0",
                    "mapping_status": "no_frozen_rooted_surface_match",
                    "dominant_frozen_root_norm": "",
                    "dominant_furuq_root_id": "",
                    "dominant_furuq_root_norm": "",
                    "dominant_furuq_source_root_norm": "",
                    "dominant_resolution": "",
                    "dominant_occurrences": "0",
                    "targets": "",
                    "status_counts": "",
                    "sample_refs": "",
                    "sample_surfaces": "",
                }
            )
            continue
        targets = rec["targets"]
        dominant_key, dominant_count = targets.most_common(1)[0]
        frozen_root, root_id, furuq_root, source_root, resolution = dominant_key.split("\u001f")
        qac_map_rows.append(
            {
                "qac_root_norm": qac_root,
                "qac_total_occurrences": str(total_count),
                "matched_occurrences": str(rec["matched_occurrences"]),
                "mapping_status": "unique" if len(targets) == 1 else "split",
                "dominant_frozen_root_norm": frozen_root,
                "dominant_furuq_root_id": root_id,
                "dominant_furuq_root_norm": furuq_root,
                "dominant_furuq_source_root_norm": source_root,
                "dominant_resolution": resolution,
                "dominant_occurrences": str(dominant_count),
                "targets": "|".join(
                    f"{key.replace(chr(31), '=>')}:{count}"
                    for key, count in targets.most_common()
                ),
                "status_counts": "|".join(
                    f"{key}:{count}" for key, count in sorted(rec["status_counts"].items())
                ),
                "sample_refs": "|".join(rec["sample_refs"]),
                "sample_surfaces": "|".join(rec["sample_surfaces"]),
            }
        )

    grouped_rows.sort(
        key=lambda row: (
            0 if "diff" in row["statuses"] or "no_qac" in row["statuses"] else 1,
            row["qac_root_norm"],
            row["frozen_root_norm"],
        )
    )
    occurrences.sort(key=lambda row: (row["status"], row["word_ref"]))

    summary = {
        "frozen_rooted_occurrences": len(occurrences),
        "frozen_distinct_roots": len(frozen_root_occurrences),
        "qac_distinct_roots_seen_at_frozen_words": len(qac_root_occurrences),
        "qac_distinct_roots_total": len(all_qac_root_counts),
        "qac_roots_without_frozen_rooted_surface_match": sum(
            1 for row in qac_map_rows if row["mapping_status"] == "no_frozen_rooted_surface_match"
        ),
        "qac_roots_with_split_mapping": sum(
            1 for row in qac_map_rows if row["mapping_status"] == "split"
        ),
        "pair_groups": len(grouped_rows),
        "status_counts": dict(status_counts),
        "frozen_roots_missing_furuq": sorted(
            {
                row["frozen_root_norm"]
                for row in occurrences
                if row["furuq_resolution"] == "missing_furuq_root"
            }
        ),
        "qac_roots_with_diff_occurrences": sorted(
            {
                root
                for row in occurrences
                if row["status"] in {"same_word_root_diff", "same_word_qac_multi_root_diff"}
                for root in row["qac_root_norm"].split("|")
                if root
            }
        ),
    }
    return occurrences, grouped_rows, qac_map_rows, summary


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--qac-db", type=Path, default=DEFAULT_QAC_DB)
    parser.add_argument("--furuq-db", type=Path, default=DEFAULT_FURUQ_DB)
    parser.add_argument("--frozen-corpus", type=Path, default=DEFAULT_FROZEN)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    args = parser.parse_args()

    occurrences, grouped_rows, qac_map_rows, summary = build(args)

    occurrence_path = args.out_dir / "frozen-qac-root-bridge-occurrences.tsv"
    grouped_path = args.out_dir / "frozen-qac-root-bridge-groups.tsv"
    qac_map_path = args.out_dir / "frozen-qac-root-authoritative-map.tsv"
    summary_path = args.out_dir / "frozen-qac-root-bridge-summary.json"
    write_tsv(occurrence_path, occurrences)
    write_tsv(grouped_path, grouped_rows)
    write_tsv(qac_map_path, qac_map_rows)
    summary_path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(f"wrote {occurrence_path}")
    print(f"wrote {grouped_path}")
    print(f"wrote {qac_map_path}")
    print(f"wrote {summary_path}")
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
