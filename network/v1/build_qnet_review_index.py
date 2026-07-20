#!/usr/bin/env python3
"""Build a compact Qnet-enriched review index from S1 path candidates."""

from __future__ import annotations

import argparse
import collections
import csv
import json
import math
from pathlib import Path
from typing import Any


BranchKey = tuple[str, str]
ThemeKey = tuple[str, str]

PRIMARY_READING_FACETS = {
    "theme:ritual_belief/religion_worship",
    "theme:ritual_belief/ritual",
    "theme:ritual_belief/belief_revelation",
    "kw:adoration",
    "kw:creed",
    "kw:deity",
    "kw:devotion",
    "kw:divinity",
    "kw:monotheism",
    "kw:religion",
    "kw:theology",
    "kw:worship",
}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")))
            handle.write("\n")


def parse_node_id(node_id: str) -> BranchKey:
    # quranic:root_001040:B002
    _, root_id, branch_id = node_id.split(":")
    return root_id, branch_id


def load_qnet_themes(path: Path) -> tuple[
    dict[BranchKey, list[dict[str, Any]]],
    dict[ThemeKey, float],
    dict[ThemeKey, int],
    int,
]:
    by_branch: dict[BranchKey, list[dict[str, Any]]] = collections.defaultdict(list)
    theme_branches: dict[ThemeKey, set[BranchKey]] = collections.defaultdict(set)

    with path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            key = (row["root_id"], row["branch_id"])
            theme = (row["parent_theme"], row["theme"])
            raw_count = int(row["raw_keyword_count"])
            by_branch[key].append(
                {
                    "parent_theme": theme[0],
                    "theme": theme[1],
                    "raw_keyword_count": raw_count,
                    "votes2_keyword_count": int(row["votes2_keyword_count"]),
                    "votes1_keyword_count": int(row["votes1_keyword_count"]),
                }
            )
            theme_branches[theme].add(key)

    total_branches = len(set().union(*theme_branches.values())) if theme_branches else 0
    theme_df = {theme: len(branches) for theme, branches in theme_branches.items()}
    theme_idf = {
        theme: math.log((1 + total_branches) / (1 + df)) + 1.0
        for theme, df in theme_df.items()
    }
    return by_branch, theme_idf, theme_df, total_branches


def load_qnet_keywords(path: Path) -> tuple[
    dict[BranchKey, dict[str, list[dict[str, Any]]]],
    dict[str, float],
    dict[str, int],
    int,
]:
    out: dict[BranchKey, dict[str, list[dict[str, Any]]]] = collections.defaultdict(
        lambda: {"core": [], "bridge": []}
    )
    keyword_branches: dict[str, set[BranchKey]] = collections.defaultdict(set)
    with path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            key = (row["root_id"], row["branch_id"])
            typ = row["keyword_type"]
            if typ not in {"core", "bridge"}:
                continue
            keyword_branches[row["keyword"]].add(key)
            out[key][typ].append(
                {
                    "keyword": row["keyword"],
                    "replicate_votes": int(row["replicate_votes"]),
                }
            )
    for record in out.values():
        for typ in ("core", "bridge"):
            record[typ].sort(key=lambda item: (-item["replicate_votes"], item["keyword"]))

    total_branches = len(set().union(*keyword_branches.values())) if keyword_branches else 0
    keyword_df = {keyword: len(branches) for keyword, branches in keyword_branches.items()}
    keyword_idf = {
        keyword: math.log((1 + total_branches) / (1 + df)) + 1.0
        for keyword, df in keyword_df.items()
    }
    return out, keyword_idf, keyword_df, total_branches


def rank_existing_facets(
    path_branches: list[dict[str, Any]],
    enriched_path: list[dict[str, Any]],
    keywords: dict[BranchKey, dict[str, list[dict[str, Any]]]],
    theme_df: dict[ThemeKey, int],
    keyword_idf: dict[str, float],
    keyword_df: dict[str, int],
    *,
    max_theme_df_ratio: float = 0.06,
    max_keyword_df_ratio: float = 0.04,
) -> list[dict[str, Any]]:
    """Score only existing Qnet themes/keywords; this invents no new labels."""

    branch_count = max(1, len(path_branches))
    max_theme_df = max(1, int(11275 * max_theme_df_ratio))
    max_keyword_df = max(1, int(11275 * max_keyword_df_ratio))
    scores: dict[str, float] = collections.defaultdict(float)
    support: dict[str, set[str]] = collections.defaultdict(set)
    kind_by_facet: dict[str, str] = {}

    if len(path_branches) != len(enriched_path):
        raise ValueError("path branch count and enriched branch count differ")

    for source_branch, qnet_branch in zip(path_branches, enriched_path):
        branch_key = parse_node_id(source_branch["node_id"])
        support_key = f"{source_branch['root']}:{source_branch['branch_id']}"

        for theme in qnet_branch["qnet_top_themes"]:
            parent, leaf = theme["theme_key"].split("/", 1)
            if theme_df.get((parent, leaf), max_theme_df + 1) > max_theme_df:
                continue
            facet = f"theme:{theme['theme_key']}"
            kind_by_facet[facet] = "theme"
            support[facet].add(support_key)
            scores[facet] += float(theme["specificity"]) * (
                1.0 + min(int(theme["raw_keyword_count"]), 4) / 4.0
            )

        for typ in ("core", "bridge"):
            for keyword_row in keywords.get(branch_key, {"core": [], "bridge": []})[typ]:
                keyword = keyword_row["keyword"]
                votes = int(keyword_row["replicate_votes"])
                df = keyword_df.get(keyword, max_keyword_df + 1)
                idf = keyword_idf.get(keyword, 0.0)
                if votes < 2 or df > max_keyword_df:
                    continue
                facet = f"kw:{keyword}"
                kind_by_facet[facet] = "keyword"
                support[facet].add(support_key)
                scores[facet] += idf * (1.0 + 0.5 * (votes - 1))

    ranked = []
    for facet, base_score in scores.items():
        support_count = len(support[facet])
        # Multi-branch support is the main signal; single-branch rare labels remain visible but lower.
        coherence = 1.0 + math.log1p(support_count) / math.log1p(branch_count)
        ranked.append(
            {
                "facet": facet,
                "kind": kind_by_facet[facet],
                "support_count": support_count,
                "support": sorted(support[facet]),
                "score": round(base_score * coherence, 6),
            }
        )

    ranked.sort(
        key=lambda item: (
            -item["support_count"],
            -item["score"],
            item["kind"],
            item["facet"],
        )
    )
    return ranked


def facet_signature(
    ranked_facets: list[dict[str, Any]],
    *,
    min_support_count: int,
    limit: int,
    fallback_limit: int,
) -> list[str]:
    supported = [
        item["facet"]
        for item in ranked_facets
        if int(item["support_count"]) >= min_support_count
    ]
    if supported:
        return supported[:limit]
    return [item["facet"] for item in ranked_facets[:fallback_limit]]


def top_themes(
    branch_key: BranchKey,
    branch_themes: dict[BranchKey, list[dict[str, Any]]],
    theme_idf: dict[ThemeKey, float],
    *,
    limit: int,
) -> list[dict[str, Any]]:
    rows = []
    for theme in branch_themes.get(branch_key, []):
        theme_key = (theme["parent_theme"], theme["theme"])
        specificity = theme_idf.get(theme_key, 0.0)
        rows.append(
            {
                **theme,
                "theme_key": f"{theme_key[0]}/{theme_key[1]}",
                "specificity": round(specificity, 6),
                "weighted_specificity": round(
                    specificity * max(1, theme["raw_keyword_count"]), 6
                ),
            }
        )
    rows.sort(
        key=lambda row: (
            -row["weighted_specificity"],
            -row["specificity"],
            row["parent_theme"],
            row["theme"],
        )
    )
    return rows[:limit]


def enrich_path_family(
    row: dict[str, Any],
    branch_themes: dict[BranchKey, list[dict[str, Any]]],
    theme_idf: dict[ThemeKey, float],
    keywords: dict[BranchKey, dict[str, list[dict[str, Any]]]],
    theme_df: dict[ThemeKey, int],
    keyword_idf: dict[str, float],
    keyword_df: dict[str, int],
    *,
    top_theme_limit: int,
    keyword_limit: int,
) -> dict[str, Any]:
    enriched_path = []
    top_theme_signature = []
    theme_set: set[str] = set()
    rare_theme_set: set[str] = set()
    keyword_set: set[str] = set()
    votes2_keyword_set: set[str] = set()

    for branch in row["representative_path"]:
        branch_key = parse_node_id(branch["node_id"])
        themes = top_themes(
            branch_key,
            branch_themes,
            theme_idf,
            limit=top_theme_limit,
        )
        top_theme = themes[0]["theme_key"] if themes else "NO_QNET_THEME"
        top_theme_signature.append(top_theme)
        theme_set.update(theme["theme_key"] for theme in themes)
        rare_theme_set.update(
            theme["theme_key"]
            for theme in themes
            if theme["specificity"] >= 4.0
        )

        kw = keywords.get(branch_key, {"core": [], "bridge": []})
        core = kw["core"][:keyword_limit]
        bridge = kw["bridge"][:keyword_limit]
        keyword_set.update(item["keyword"] for item in core + bridge)
        votes2_keyword_set.update(
            item["keyword"]
            for item in core + bridge
            if item["replicate_votes"] >= 2
        )

        enriched_path.append(
            {
                "ayah": branch["ayah"],
                "root": branch["root"],
                "branch_id": branch["branch_id"],
                "branch_image_ar": branch["branch_image_ar"],
                "node_id": branch["node_id"],
                "qnet_top_themes": themes,
                "qnet_core_keywords": core,
                "qnet_bridge_keywords": bridge,
            }
        )

    scored_facets = rank_existing_facets(
        row["representative_path"],
        enriched_path,
        keywords,
        theme_df,
        keyword_idf,
        keyword_df,
    )
    image_scored_facets = [
        item for item in scored_facets if item["facet"] not in PRIMARY_READING_FACETS
    ]
    enriched = {
        **row,
        "qnet_top_theme_signature": top_theme_signature,
        "qnet_theme_set": sorted(theme_set),
        "qnet_rare_theme_set": sorted(rare_theme_set),
        "qnet_keyword_set_sample": sorted(keyword_set)[:40],
        "qnet_votes2_keyword_set_sample": sorted(votes2_keyword_set)[:40],
        "qnet_scored_facets_top": scored_facets[:40],
        "qnet_scored_facet_signature": facet_signature(
            scored_facets,
            min_support_count=2,
            limit=8,
            fallback_limit=4,
        ),
        "qnet_image_scored_facets_top": image_scored_facets[:40],
        "qnet_image_scored_facet_signature": facet_signature(
            image_scored_facets,
            min_support_count=2,
            limit=8,
            fallback_limit=4,
        ),
        "representative_path_qnet": enriched_path,
    }
    return enriched


def rare_facet_signature(row: dict[str, Any], *, max_items: int = 8) -> tuple[str, ...]:
    """Return a compact existing-facet signature, using no invented roles."""

    facets = []
    for theme in row["qnet_rare_theme_set"]:
        facets.append(("theme", theme))
    for keyword in row["qnet_votes2_keyword_set_sample"]:
        facets.append(("kw", keyword))

    # Prefer explicitly existing rare themes, then strong consensus keywords.
    ordered = [f"{kind}:{value}" for kind, value in sorted(facets)]
    if not ordered:
        ordered = [f"theme:{theme}" for theme in row["qnet_theme_set"][:max_items]]
    return tuple(ordered[:max_items])


def group_by_theme_signature(rows: list[dict[str, Any]], *, cap: int) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, ...], dict[str, Any]] = {}
    for row in rows:
        signature = tuple(row["qnet_top_theme_signature"])
        group = grouped.setdefault(
            signature,
            {
                "theme_signature": list(signature),
                "candidate_ids": [],
                "root_signatures": [],
                "path_count_total": 0,
                "distinct_ayahs": set(),
                "theme_set": set(),
                "keyword_set": set(),
                "representative": row,
            },
        )
        group["candidate_ids"].append(row["candidate_id"])
        group["root_signatures"].append(row["ordered_root_signature"])
        group["path_count_total"] += int(row["path_count_exact_dp"])
        group["distinct_ayahs"].update(row["distinct_ayahs_union"])
        group["theme_set"].update(row["qnet_theme_set"])
        group["keyword_set"].update(row["qnet_keyword_set_sample"])
        if row["score"] > group["representative"]["score"]:
            group["representative"] = row

    records = []
    for index, group in enumerate(grouped.values(), start=1):
        rep = group["representative"]
        records.append(
            {
                "review_id": f"QR{index:04d}",
                "theme_signature": group["theme_signature"],
                "candidate_count": len(group["candidate_ids"]),
                "candidate_ids": group["candidate_ids"],
                "path_count_total": group["path_count_total"],
                "distinct_ayahs": sorted(group["distinct_ayahs"]),
                "theme_set": sorted(group["theme_set"]),
                "keyword_set_sample": sorted(group["keyword_set"])[:60],
                "representative_candidate_id": rep["candidate_id"],
                "representative_root_signature": rep["ordered_root_signature"],
                "representative_path": rep["representative_path_qnet"],
                "review_instruction": "Judge/merge/split using existing Qnet themes, keywords, and branch text only.",
            }
        )

    records.sort(
        key=lambda row: (
            -row["candidate_count"],
            -row["path_count_total"],
            -len(row["theme_set"]),
            row["theme_signature"],
        )
    )
    for index, row in enumerate(records, start=1):
        row["review_id"] = f"QR{index:04d}"
    return records[:cap]


def group_by_rare_facets(rows: list[dict[str, Any]], *, cap: int) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, ...], dict[str, Any]] = {}
    for row in rows:
        signature = rare_facet_signature(row)
        group = grouped.setdefault(
            signature,
            {
                "rare_facet_signature": list(signature),
                "candidate_ids": [],
                "root_signatures": [],
                "path_count_total": 0,
                "distinct_ayahs": set(),
                "theme_set": set(),
                "rare_theme_set": set(),
                "keyword_set": set(),
                "representative": row,
            },
        )
        group["candidate_ids"].append(row["candidate_id"])
        group["root_signatures"].append(row["ordered_root_signature"])
        group["path_count_total"] += int(row["path_count_exact_dp"])
        group["distinct_ayahs"].update(row["distinct_ayahs_union"])
        group["theme_set"].update(row["qnet_theme_set"])
        group["rare_theme_set"].update(row["qnet_rare_theme_set"])
        group["keyword_set"].update(row["qnet_votes2_keyword_set_sample"])
        if row["score"] > group["representative"]["score"]:
            group["representative"] = row

    records = []
    for index, group in enumerate(grouped.values(), start=1):
        rep = group["representative"]
        records.append(
            {
                "review_id": f"RF{index:04d}",
                "rare_facet_signature": group["rare_facet_signature"],
                "candidate_count": len(group["candidate_ids"]),
                "candidate_ids": group["candidate_ids"],
                "path_count_total": group["path_count_total"],
                "distinct_ayahs": sorted(group["distinct_ayahs"]),
                "theme_set": sorted(group["theme_set"]),
                "rare_theme_set": sorted(group["rare_theme_set"]),
                "keyword_set_sample": sorted(group["keyword_set"])[:60],
                "representative_candidate_id": rep["candidate_id"],
                "representative_root_signature": rep["ordered_root_signature"],
                "representative_path": rep["representative_path_qnet"],
                "review_instruction": "Judge/merge/split using existing rare Qnet themes, consensus keywords, and branch text only.",
            }
        )

    records.sort(
        key=lambda row: (
            -len(row["rare_theme_set"]),
            -row["candidate_count"],
            -row["path_count_total"],
            row["rare_facet_signature"],
        )
    )
    for index, row in enumerate(records, start=1):
        row["review_id"] = f"RF{index:04d}"
    return records[:cap]


def group_by_scored_facets(rows: list[dict[str, Any]], *, cap: int) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, ...], dict[str, Any]] = {}
    for row in rows:
        signature = tuple(row["qnet_scored_facet_signature"])
        group = grouped.setdefault(
            signature,
            {
                "scored_facet_signature": list(signature),
                "candidate_ids": [],
                "root_signatures": [],
                "path_count_total": 0,
                "distinct_ayahs": set(),
                "theme_set": set(),
                "keyword_set": set(),
                "scored_facets": {},
                "representative": row,
            },
        )
        group["candidate_ids"].append(row["candidate_id"])
        group["root_signatures"].append(row["ordered_root_signature"])
        group["path_count_total"] += int(row["path_count_exact_dp"])
        group["distinct_ayahs"].update(row["distinct_ayahs_union"])
        group["theme_set"].update(row["qnet_theme_set"])
        group["keyword_set"].update(row["qnet_votes2_keyword_set_sample"])
        for facet in row["qnet_scored_facets_top"][:16]:
            acc = group["scored_facets"].setdefault(
                facet["facet"],
                {"facet": facet["facet"], "score": 0.0, "support": set()},
            )
            acc["score"] += float(facet["score"])
            acc["support"].update(facet["support"])
        if row["score"] > group["representative"]["score"]:
            group["representative"] = row

    records = []
    for index, group in enumerate(grouped.values(), start=1):
        rep = group["representative"]
        scored_facets = [
            {
                "facet": item["facet"],
                "score": round(item["score"], 6),
                "support_count": len(item["support"]),
                "support": sorted(item["support"]),
            }
            for item in group["scored_facets"].values()
        ]
        scored_facets.sort(
            key=lambda item: (-item["support_count"], -item["score"], item["facet"])
        )
        records.append(
            {
                "review_id": f"SF{index:04d}",
                "scored_facet_signature": group["scored_facet_signature"],
                "candidate_count": len(group["candidate_ids"]),
                "candidate_ids": group["candidate_ids"],
                "path_count_total": group["path_count_total"],
                "distinct_ayahs": sorted(group["distinct_ayahs"]),
                "theme_set": sorted(group["theme_set"]),
                "keyword_set_sample": sorted(group["keyword_set"])[:60],
                "scored_facets_top": scored_facets[:24],
                "representative_candidate_id": rep["candidate_id"],
                "representative_root_signature": rep["ordered_root_signature"],
                "representative_path": rep["representative_path_qnet"],
                "review_instruction": "Judge/merge/split using existing Qnet labels ranked by path-local support and corpus rarity.",
            }
        )

    records.sort(
        key=lambda row: (
            -row["candidate_count"],
            -row["path_count_total"],
            -len(row["scored_facets_top"]),
            row["scored_facet_signature"],
        )
    )
    for index, row in enumerate(records, start=1):
        row["review_id"] = f"SF{index:04d}"
    return records[:cap]


def group_by_image_scored_facets(rows: list[dict[str, Any]], *, cap: int) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, ...], dict[str, Any]] = {}
    for row in rows:
        signature = tuple(row["qnet_image_scored_facet_signature"])
        group = grouped.setdefault(
            signature,
            {
                "image_scored_facet_signature": list(signature),
                "candidate_ids": [],
                "root_signatures": [],
                "path_count_total": 0,
                "distinct_ayahs": set(),
                "scored_facets": {},
                "representative": row,
            },
        )
        group["candidate_ids"].append(row["candidate_id"])
        group["root_signatures"].append(row["ordered_root_signature"])
        group["path_count_total"] += int(row["path_count_exact_dp"])
        group["distinct_ayahs"].update(row["distinct_ayahs_union"])
        for facet in row["qnet_image_scored_facets_top"][:16]:
            acc = group["scored_facets"].setdefault(
                facet["facet"],
                {"facet": facet["facet"], "score": 0.0, "support": set()},
            )
            acc["score"] += float(facet["score"])
            acc["support"].update(facet["support"])
        if row["score"] > group["representative"]["score"]:
            group["representative"] = row

    records = []
    for index, group in enumerate(grouped.values(), start=1):
        rep = group["representative"]
        scored_facets = [
            {
                "facet": item["facet"],
                "score": round(item["score"], 6),
                "support_count": len(item["support"]),
                "support": sorted(item["support"]),
            }
            for item in group["scored_facets"].values()
        ]
        scored_facets.sort(
            key=lambda item: (-item["support_count"], -item["score"], item["facet"])
        )
        records.append(
            {
                "review_id": f"IF{index:04d}",
                "image_scored_facet_signature": group["image_scored_facet_signature"],
                "candidate_count": len(group["candidate_ids"]),
                "candidate_ids": group["candidate_ids"],
                "path_count_total": group["path_count_total"],
                "distinct_ayahs": sorted(group["distinct_ayahs"]),
                "scored_facets_top": scored_facets[:24],
                "representative_candidate_id": rep["candidate_id"],
                "representative_root_signature": rep["ordered_root_signature"],
                "representative_path": rep["representative_path_qnet"],
                "review_instruction": "Judge/merge/split using existing non-primary Qnet labels ranked by path-local support and corpus rarity.",
            }
        )

    records.sort(
        key=lambda row: (
            -row["candidate_count"],
            -row["path_count_total"],
            -len(row["scored_facets_top"]),
            row["image_scored_facet_signature"],
        )
    )
    for index, row in enumerate(records, start=1):
        row["review_id"] = f"IF{index:04d}"
    return records[:cap]


def write_compact_outputs(output_dir: Path, review_rows: list[dict[str, Any]]) -> None:
    tsv_path = output_dir / "compact_review_index.tsv"
    with tsv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "review_id",
                "candidate_count",
                "path_count_total",
                "ayahs",
                "theme_signature",
                "representative_roots",
                "representative_branches",
                "theme_set_sample",
                "keyword_sample",
            ]
        )
        for row in review_rows:
            writer.writerow(
                [
                    row["review_id"],
                    row["candidate_count"],
                    row["path_count_total"],
                    ",".join(map(str, row["distinct_ayahs"])),
                    " → ".join(row["theme_signature"]),
                    " → ".join(row["representative_root_signature"]),
                    " | ".join(
                        f'{item["root"]}:{item["branch_id"]}:{item["branch_image_ar"]}'
                        for item in row["representative_path"]
                    ),
                    "; ".join(row["theme_set"][:12]),
                    ", ".join(row["keyword_set_sample"][:20]),
                ]
            )

    md_path = output_dir / "compact_review_index.md"
    with md_path.open("w", encoding="utf-8") as handle:
        handle.write("# Compact Qnet review index\n\n")
        for row in review_rows:
            handle.write(
                f"## {row['review_id']} — {row['candidate_count']} candidates, "
                f"{row['path_count_total']} paths\n\n"
            )
            handle.write(f"- Ayahs: {','.join(map(str, row['distinct_ayahs']))}\n")
            handle.write(f"- Theme signature: {' → '.join(row['theme_signature'])}\n")
            handle.write(
                f"- Roots: {' → '.join(row['representative_root_signature'])}\n"
            )
            handle.write(
                "- Branches: "
                + " | ".join(
                    f'{item["root"]}:{item["branch_id"]}:{item["branch_image_ar"]}'
                    for item in row["representative_path"]
                )
                + "\n"
            )
            handle.write(f"- Theme sample: {'; '.join(row['theme_set'][:12])}\n")
            handle.write(f"- Keyword sample: {', '.join(row['keyword_set_sample'][:20])}\n\n")


def write_rare_facet_outputs(output_dir: Path, review_rows: list[dict[str, Any]]) -> None:
    tsv_path = output_dir / "rare_facet_review_index.tsv"
    with tsv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "review_id",
                "candidate_count",
                "path_count_total",
                "ayahs",
                "rare_facet_signature",
                "representative_roots",
                "representative_branches",
                "rare_theme_set",
                "keyword_sample",
            ]
        )
        for row in review_rows:
            writer.writerow(
                [
                    row["review_id"],
                    row["candidate_count"],
                    row["path_count_total"],
                    ",".join(map(str, row["distinct_ayahs"])),
                    " | ".join(row["rare_facet_signature"]),
                    " → ".join(row["representative_root_signature"]),
                    " | ".join(
                        f'{item["root"]}:{item["branch_id"]}:{item["branch_image_ar"]}'
                        for item in row["representative_path"]
                    ),
                    "; ".join(row["rare_theme_set"][:16]),
                    ", ".join(row["keyword_set_sample"][:24]),
                ]
            )

    md_path = output_dir / "rare_facet_review_index.md"
    with md_path.open("w", encoding="utf-8") as handle:
        handle.write("# Rare-facet Qnet review index\n\n")
        for row in review_rows:
            handle.write(
                f"## {row['review_id']} — {row['candidate_count']} candidates, "
                f"{row['path_count_total']} paths\n\n"
            )
            handle.write(f"- Ayahs: {','.join(map(str, row['distinct_ayahs']))}\n")
            handle.write(f"- Rare facets: {' | '.join(row['rare_facet_signature'])}\n")
            handle.write(
                f"- Roots: {' → '.join(row['representative_root_signature'])}\n"
            )
            handle.write(
                "- Branches: "
                + " | ".join(
                    f'{item["root"]}:{item["branch_id"]}:{item["branch_image_ar"]}'
                    for item in row["representative_path"]
                )
                + "\n"
            )
            handle.write(f"- Rare themes: {'; '.join(row['rare_theme_set'][:16])}\n")
            handle.write(f"- Keyword sample: {', '.join(row['keyword_set_sample'][:24])}\n\n")


def write_scored_facet_outputs(output_dir: Path, review_rows: list[dict[str, Any]]) -> None:
    tsv_path = output_dir / "scored_facet_review_index.tsv"
    with tsv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "review_id",
                "candidate_count",
                "path_count_total",
                "ayahs",
                "scored_facet_signature",
                "representative_roots",
                "representative_branches",
                "top_scored_facets",
            ]
        )
        for row in review_rows:
            writer.writerow(
                [
                    row["review_id"],
                    row["candidate_count"],
                    row["path_count_total"],
                    ",".join(map(str, row["distinct_ayahs"])),
                    " | ".join(row["scored_facet_signature"]),
                    " → ".join(row["representative_root_signature"]),
                    " | ".join(
                        f'{item["root"]}:{item["branch_id"]}:{item["branch_image_ar"]}'
                        for item in row["representative_path"]
                    ),
                    "; ".join(
                        f'{item["facet"]}({item["support_count"]})'
                        for item in row["scored_facets_top"][:16]
                    ),
                ]
            )

    md_path = output_dir / "scored_facet_review_index.md"
    with md_path.open("w", encoding="utf-8") as handle:
        handle.write("# Scored-facet Qnet review index\n\n")
        for row in review_rows:
            handle.write(
                f"## {row['review_id']} — {row['candidate_count']} candidates, "
                f"{row['path_count_total']} paths\n\n"
            )
            handle.write(f"- Ayahs: {','.join(map(str, row['distinct_ayahs']))}\n")
            handle.write(f"- Scored facets: {' | '.join(row['scored_facet_signature'])}\n")
            handle.write(
                f"- Roots: {' → '.join(row['representative_root_signature'])}\n"
            )
            handle.write(
                "- Branches: "
                + " | ".join(
                    f'{item["root"]}:{item["branch_id"]}:{item["branch_image_ar"]}'
                    for item in row["representative_path"]
                )
                + "\n"
            )
            handle.write(
                "- Top scored facets: "
                + "; ".join(
                    f'{item["facet"]}({item["support_count"]})'
                    for item in row["scored_facets_top"][:16]
                )
                + "\n\n"
            )


def write_image_facet_outputs(output_dir: Path, review_rows: list[dict[str, Any]]) -> None:
    tsv_path = output_dir / "image_facet_review_index.tsv"
    with tsv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "review_id",
                "candidate_count",
                "path_count_total",
                "ayahs",
                "image_scored_facet_signature",
                "representative_roots",
                "representative_branches",
                "top_image_facets",
            ]
        )
        for row in review_rows:
            writer.writerow(
                [
                    row["review_id"],
                    row["candidate_count"],
                    row["path_count_total"],
                    ",".join(map(str, row["distinct_ayahs"])),
                    " | ".join(row["image_scored_facet_signature"]),
                    " → ".join(row["representative_root_signature"]),
                    " | ".join(
                        f'{item["root"]}:{item["branch_id"]}:{item["branch_image_ar"]}'
                        for item in row["representative_path"]
                    ),
                    "; ".join(
                        f'{item["facet"]}({item["support_count"]})'
                        for item in row["scored_facets_top"][:16]
                    ),
                ]
            )

    md_path = output_dir / "image_facet_review_index.md"
    with md_path.open("w", encoding="utf-8") as handle:
        handle.write("# Image-facet Qnet review index\n\n")
        for row in review_rows:
            handle.write(
                f"## {row['review_id']} — {row['candidate_count']} candidates, "
                f"{row['path_count_total']} paths\n\n"
            )
            handle.write(f"- Ayahs: {','.join(map(str, row['distinct_ayahs']))}\n")
            handle.write(
                f"- Image facets: {' | '.join(row['image_scored_facet_signature'])}\n"
            )
            handle.write(
                f"- Roots: {' → '.join(row['representative_root_signature'])}\n"
            )
            handle.write(
                "- Branches: "
                + " | ".join(
                    f'{item["root"]}:{item["branch_id"]}:{item["branch_image_ar"]}'
                    for item in row["representative_path"]
                )
                + "\n"
            )
            handle.write(
                "- Top image facets: "
                + "; ".join(
                    f'{item["facet"]}({item["support_count"]})'
                    for item in row["scored_facets_top"][:16]
                )
                + "\n\n"
            )


def write_theme_specificity(
    output_dir: Path,
    theme_idf: dict[ThemeKey, float],
    theme_df: dict[ThemeKey, int],
    total_branches: int,
) -> None:
    path = output_dir / "theme_specificity.tsv"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["parent_theme", "theme", "branch_df", "total_branches", "idf"])
        for theme in sorted(theme_idf, key=lambda item: (-theme_idf[item], item)):
            writer.writerow(
                [theme[0], theme[1], theme_df[theme], total_branches, f"{theme_idf[theme]:.6f}"]
            )


def build(args: argparse.Namespace) -> dict[str, Any]:
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    path_rows = read_jsonl(Path(args.path_families))
    branch_themes, theme_idf, theme_df, total_theme_branches = load_qnet_themes(
        Path(args.qnet_branch_themes)
    )
    keywords, keyword_idf, keyword_df, total_keyword_branches = load_qnet_keywords(
        Path(args.qnet_branch_keywords)
    )

    enriched = [
        enrich_path_family(
            row,
            branch_themes,
            theme_idf,
            keywords,
            theme_df,
            keyword_idf,
            keyword_df,
            top_theme_limit=args.top_theme_limit,
            keyword_limit=args.keyword_limit,
        )
        for row in path_rows
    ]
    review_rows = group_by_theme_signature(enriched, cap=args.review_cap)
    rare_review_rows = group_by_rare_facets(enriched, cap=args.review_cap)
    scored_review_rows = group_by_scored_facets(enriched, cap=args.review_cap)
    image_review_rows = group_by_image_scored_facets(enriched, cap=args.review_cap)

    write_jsonl(output_dir / "qnet_enriched_path_families.jsonl", enriched)
    write_jsonl(output_dir / "compact_review_index.jsonl", review_rows)
    write_jsonl(output_dir / "rare_facet_review_index.jsonl", rare_review_rows)
    write_jsonl(output_dir / "scored_facet_review_index.jsonl", scored_review_rows)
    write_jsonl(output_dir / "image_facet_review_index.jsonl", image_review_rows)
    write_compact_outputs(output_dir, review_rows)
    write_rare_facet_outputs(output_dir, rare_review_rows)
    write_scored_facet_outputs(output_dir, scored_review_rows)
    write_image_facet_outputs(output_dir, image_review_rows)
    write_theme_specificity(output_dir, theme_idf, theme_df, total_theme_branches)

    summary = {
        "version": "network_v1_qnet_review_index",
        "policy": "Use existing Qnet bridge themes and raw keywords only; no new role ontology.",
        "inputs": {
            "path_families": args.path_families,
            "qnet_branch_themes": args.qnet_branch_themes,
            "qnet_branch_keywords": args.qnet_branch_keywords,
        },
        "counts": {
            "input_path_families": len(path_rows),
            "enriched_path_families": len(enriched),
            "theme_signature_groups_selected": len(review_rows),
            "rare_facet_groups_selected": len(rare_review_rows),
            "scored_facet_groups_selected": len(scored_review_rows),
            "image_facet_groups_selected": len(image_review_rows),
            "qnet_theme_branches": total_theme_branches,
            "qnet_leaf_themes": len(theme_idf),
            "qnet_keyword_branches": total_keyword_branches,
            "qnet_keywords": len(keyword_idf),
        },
        "parameters": {
            "review_cap": args.review_cap,
            "top_theme_limit": args.top_theme_limit,
            "keyword_limit": args.keyword_limit,
        },
    }
    (output_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--path-families",
        default="network/output/s1_min5_strong_v0/path_family_candidates.jsonl",
    )
    parser.add_argument(
        "--qnet-branch-themes",
        default="../quran-roots/_corpus/activation/Qnet/v2/network/bridge_theme_full/branch_theme_inventory.tsv",
    )
    parser.add_argument(
        "--qnet-branch-keywords",
        default="../quran-roots/_corpus/activation/Qnet/v2/network/incidence_full/branch_keywords.tsv",
    )
    parser.add_argument("--output-dir", default="network/v1/output")
    parser.add_argument("--review-cap", type=int, default=200)
    parser.add_argument("--top-theme-limit", type=int, default=3)
    parser.add_argument("--keyword-limit", type=int, default=5)
    return parser.parse_args()


def main() -> None:
    print(json.dumps(build(parse_args()), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
