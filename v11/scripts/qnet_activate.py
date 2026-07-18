#!/usr/bin/env python3
"""
v11 Qnet latent activation candidate generator.

This script is intentionally recall-first:
- it emits broad and weak candidates instead of pruning them;
- it keeps branches as labels on root-to-root edges;
- it prepares agent review packets but does not pretend to decide final meaning.
"""

from __future__ import annotations

import argparse
import gzip
import itertools
import json
import shutil
import sqlite3
import tempfile
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_QAC = REPO_ROOT / "resources" / "qac.sqlite.gz"
DEFAULT_FURUQ = REPO_ROOT / "resources" / "furuq_v4.sqlite.gz"
DEFAULT_QNET = (
    REPO_ROOT.parent
    / "quran-roots"
    / "_corpus"
    / "activation"
    / "Qnet"
    / "v2"
    / "network"
    / "bridge_theme_full"
    / "bridge_theme_staging.sqlite"
)
DEFAULT_Q2_RUNS = REPO_ROOT.parent / "quran-roots" / "_corpus" / "activation" / "Q2" / "runs"


def connect_sqlite(path: Path, temp_dir: Path) -> sqlite3.Connection:
    """Connect to a SQLite file, transparently decompressing .gz into temp_dir."""
    if not path.exists():
        raise FileNotFoundError(path)
    db_path = path
    if path.suffix == ".gz":
        db_path = temp_dir / path.name.removesuffix(".gz")
        with gzip.open(path, "rb") as src, db_path.open("wb") as dst:
            shutil.copyfileobj(src, dst)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


def ensure_out_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def norm_root(text: str) -> str:
    return " ".join(text.replace("\u200c", "").split())


def compact_root(text: str) -> str:
    return norm_root(text).replace(" ", "")


def strip_arabic_marks(text: str) -> str:
    return "".join(
        ch for ch in unicodedata.normalize("NFKD", text)
        if unicodedata.category(ch) != "Mn" and ch != "\u0640"
    )


def root_lookup_variants(text: str) -> list[str]:
    """Return robust root lookup keys.

    QAC and Furūq/Qnet can disagree on hamza seats:
    - QAC may use ءله while a source field has أله
    - QAC may use كفء while a source field has كفأ

    We keep exact keys first, then add hamza-seat-normalized variants. This
    prevents silently losing roots while preserving an audit trail.
    """
    raw = compact_root(strip_arabic_marks(text))
    if not raw:
        return []
    variants: list[str] = []

    def add(value: str) -> None:
        if value and value not in variants:
            variants.append(value)

    add(raw)
    hamza_to_bare = str.maketrans({
        "أ": "ء",
        "إ": "ء",
        "ؤ": "ء",
        "ئ": "ء",
        "آ": "ء",
    })
    add(raw.translate(hamza_to_bare))
    alif_to_plain = str.maketrans({
        "أ": "ا",
        "إ": "ا",
        "آ": "ا",
        "ٱ": "ا",
    })
    add(raw.translate(alif_to_plain))
    add(raw.replace("ى", "ي"))
    return variants


def split_csvish(value: str) -> list[str]:
    if not value:
        return []
    for sep in [";", ",", "|"]:
        if sep in value:
            return [x.strip() for x in value.split(sep) if x.strip()]
    return [value.strip()] if value.strip() else []


@dataclass(frozen=True)
class PassageArgs:
    surah: int
    ayah_start: int
    ayah_end: int | None
    include_basmala: bool


def extract_passage(qac: sqlite3.Connection, args: PassageArgs) -> dict[str, Any]:
    clauses = ["surah = ?", "ayah >= ?"]
    params: list[Any] = [args.surah, args.ayah_start]
    if args.ayah_end is not None:
        clauses.append("ayah <= ?")
        params.append(args.ayah_end)

    words = qac.execute(
        f"""
        SELECT qac_word_ref, surah, ayah, word_index, surface_ar,
               root_join_keys, lemmas_ar, pos_tags, measures
        FROM qac_words
        WHERE {' AND '.join(clauses)}
        ORDER BY ayah, word_index
        """,
        params,
    ).fetchall()

    morphemes = qac.execute(
        f"""
        SELECT qac_ref, qac_word_ref, surah, ayah, word_index, morpheme_index,
               surface_ar, stem_ar, lemma_ar, root_ar, root_join_key, pos, measure,
               morph_features
        FROM qac_morphemes
        WHERE {' AND '.join(clauses)}
          AND root_join_key != ''
        ORDER BY ayah, word_index, morpheme_index
        """,
        params,
    ).fetchall()

    root_order: list[str] = []
    root_seen: set[str] = set()
    root_occurrences: dict[str, list[dict[str, Any]]] = defaultdict(list)
    root_join_keys_by_root: dict[str, list[str]] = defaultdict(list)
    for row in morphemes:
        root = norm_root(row["root_ar"])
        if root not in root_seen:
            root_seen.add(root)
            root_order.append(root)
        root_join_key = row["root_join_key"]
        if root_join_key and root_join_key not in root_join_keys_by_root[root]:
            root_join_keys_by_root[root].append(root_join_key)
        root_occurrences[root].append(
            {
                "qac_ref": row["qac_ref"],
                "word_ref": row["qac_word_ref"],
                "position": [row["surah"], row["ayah"], row["word_index"], row["morpheme_index"]],
                "surface_ar": row["surface_ar"],
                "stem_ar": row["stem_ar"],
                "lemma_ar": row["lemma_ar"],
                "root_join_key": row["root_join_key"],
                "pos": row["pos"],
                "measure": row["measure"],
                "morph_features": row["morph_features"],
            }
        )

    return {
        "schema": "v11.passage.v1",
        "passage": {
            "surah": args.surah,
            "ayah_start": args.ayah_start,
            "ayah_end": args.ayah_end,
            "include_basmala": args.include_basmala,
            "note": "include_basmala is recorded but this extractor uses QAC ayah rows only.",
        },
        "words": [dict(row) for row in words],
        "roots_in_order": root_order,
        "root_occurrences": root_occurrences,
        "root_join_keys_by_root": root_join_keys_by_root,
        "root_count": len(root_order),
    }


def root_id_map(furuq: sqlite3.Connection, passage: dict[str, Any]) -> tuple[dict[str, dict[str, str]], list[dict[str, Any]]]:
    out: dict[str, dict[str, str]] = {}
    audit: list[dict[str, Any]] = []
    roots = passage["roots_in_order"]

    wanted_variants: dict[str, list[str]] = {}
    for root in roots:
        variants: list[str] = []
        for key in passage.get("root_join_keys_by_root", {}).get(root, []):
            for variant in root_lookup_variants(key):
                if variant not in variants:
                    variants.append(variant)
        for variant in root_lookup_variants(root):
            if variant not in variants:
                variants.append(variant)
        wanted_variants[root] = variants

    rows = furuq.execute(
        """
        SELECT root_id, root_norm, source_root_norm
        FROM roots
        """
    ).fetchall()
    index: dict[str, list[sqlite3.Row]] = defaultdict(list)
    for row in rows:
        keys = []
        keys.extend(root_lookup_variants(row["root_norm"]))
        keys.extend(root_lookup_variants(row["source_root_norm"]))
        for key in keys:
            if row not in index[key]:
                index[key].append(row)

    for root in roots:
        matches: list[sqlite3.Row] = []
        matched_variant = None
        for variant in wanted_variants[root]:
            candidates = index.get(variant, [])
            if candidates:
                matches = candidates
                matched_variant = variant
                break

        unique: dict[str, sqlite3.Row] = {row["root_id"]: row for row in matches}
        if len(unique) == 1:
            row = next(iter(unique.values()))
            out[root] = {
                "root_id": row["root_id"],
                "root_norm": norm_root(row["root_norm"]),
                "source_root_norm": norm_root(row["source_root_norm"]),
                "matched_variant": matched_variant or "",
                "qac_root_join_keys": passage.get("root_join_keys_by_root", {}).get(root, []),
            }
            status = "resolved"
        elif len(unique) > 1:
            status = "ambiguous"
        else:
            status = "missing"
        audit.append(
            {
                "qac_root": root,
                "qac_root_join_keys": passage.get("root_join_keys_by_root", {}).get(root, []),
                "lookup_variants": wanted_variants[root],
                "status": status,
                "matched_variant": matched_variant,
                "matches": [
                    {
                        "root_id": row["root_id"],
                        "root_norm": norm_root(row["root_norm"]),
                        "source_root_norm": norm_root(row["source_root_norm"]),
                    }
                    for row in unique.values()
                ],
            }
        )
    return out, audit


def load_branch_inventory(
    furuq: sqlite3.Connection,
    qnet: sqlite3.Connection,
    passage: dict[str, Any],
) -> dict[str, Any]:
    roots = passage["roots_in_order"]
    ids, root_resolution_audit = root_id_map(furuq, passage)

    inventory: dict[str, Any] = {
        "schema": "v11.branch_inventory.v1",
        "root_resolution_policy": "qac_first_with_hamza_variant_audit",
        "root_resolution_audit": root_resolution_audit,
        "roots": {},
        "missing_roots": [r for r in roots if r not in ids],
    }

    for root in roots:
        info = ids.get(root)
        if not info:
            continue
        root_id = info["root_id"]
        qnet_node_rows = qnet.execute(
            """
            SELECT branch_id
            FROM nodes
            WHERE root_id = ?
            ORDER BY branch_id
            """,
            [root_id],
        ).fetchall()
        qnet_branch_ids = {row["branch_id"] for row in qnet_node_rows}
        image_rows = furuq.execute(
            """
            SELECT branch_id
            FROM branch_images
            WHERE root_id = ?
            ORDER BY branch_id
            """,
            [root_id],
        ).fetchall()
        furuq_branch_ids = {row["branch_id"] for row in image_rows}
        branch_ids = sorted(qnet_branch_ids | furuq_branch_ids)
        branches: dict[str, Any] = {}
        for branch_id in branch_ids:
            image = furuq.execute(
                """
                SELECT branch_image_ar, branch_image_en, what_is_ar, what_is_en,
                       status, contaminated
                FROM branch_images
                WHERE root_id = ? AND branch_id = ?
                """,
                [root_id, branch_id],
            ).fetchone()
            keyword_rows = qnet.execute(
                """
                SELECT parent_theme, theme, raw_keyword, replicate_votes
                FROM theme_keyword_nodes
                WHERE root_id = ? AND branch_id = ?
                ORDER BY theme, raw_keyword
                """,
                [root_id, branch_id],
            ).fetchall()
            themes: dict[str, Any] = {}
            parent_themes: set[str] = set()
            raw_keywords: list[str] = []
            for kw in keyword_rows:
                theme = kw["theme"]
                parent = kw["parent_theme"]
                parent_themes.add(parent)
                raw_keywords.append(kw["raw_keyword"])
                themes.setdefault(
                    theme,
                    {
                        "parent_theme": parent,
                        "keywords": [],
                        "max_votes": 0,
                    },
                )
                themes[theme]["keywords"].append(
                    {
                        "raw_keyword": kw["raw_keyword"],
                        "replicate_votes": kw["replicate_votes"],
                    }
                )
                themes[theme]["max_votes"] = max(themes[theme]["max_votes"], kw["replicate_votes"])

            branches[branch_id] = {
                "branch_id": branch_id,
                "root": root,
                "root_id": root_id,
                "image": dict(image) if image else None,
                "integrity": "ok" if image else "missing_branch_image",
                "qnet_membership": "present" if branch_id in qnet_branch_ids else "absent_from_bridge_theme_current",
                "theme_count": len(themes),
                "parent_theme_count": len(parent_themes),
                "keyword_count": len(set(raw_keywords)),
                "themes": themes,
                "parent_themes": sorted(parent_themes),
                "raw_keywords": sorted(set(raw_keywords)),
            }
        inventory["roots"][root] = {
            **info,
            "surface_occurrences": passage["root_occurrences"].get(root, []),
            "branch_count": len(branches),
            "qnet_branch_count": len(qnet_branch_ids),
            "furuq_branch_count": len(furuq_branch_ids),
            "branches_without_qnet_themes": sorted(furuq_branch_ids - qnet_branch_ids),
            "branches": branches,
        }

    return inventory


def theme_frequency(branch_inventory: dict[str, Any]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for root_info in branch_inventory["roots"].values():
        for branch in root_info["branches"].values():
            for theme in branch["themes"]:
                counts[theme] += 1
    return counts


def keyword_frequency(branch_inventory: dict[str, Any]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for root_info in branch_inventory["roots"].values():
        for branch in root_info["branches"].values():
            for keyword in branch["raw_keywords"]:
                counts[keyword] += 1
    return counts


def iter_branch_records(branch_inventory: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for root, root_info in branch_inventory["roots"].items():
        for branch_id, branch in root_info["branches"].items():
            out.append(
                {
                    "root": root,
                    "root_id": root_info["root_id"],
                    "branch_id": branch_id,
                    "branch_key": f"{root} {branch_id}",
                    "branch": branch,
                }
            )
    return out


def relation_key(root_a: str, branch_a: str, root_b: str, branch_b: str) -> tuple[str, str]:
    keys = sorted([f"{root_a} {branch_a}", f"{root_b} {branch_b}"])
    return keys[0], keys[1]


def load_q2_relations(q2_runs: Path, passage: dict[str, Any]) -> dict[tuple[str, str], list[dict[str, Any]]]:
    surah = passage["passage"]["surah"]
    path = q2_runs / f"s{surah:03d}" / "q2-branch-projection-v1" / "branch-relations.jsonl"
    if not path.exists():
        return {}
    rels: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            item = json.loads(line)
            branches = item.get("branches") or []
            if len(branches) < 2:
                continue
            for a, b in itertools.combinations(branches, 2):
                a_parts = a.rsplit(" ", 1)
                b_parts = b.rsplit(" ", 1)
                if len(a_parts) != 2 or len(b_parts) != 2:
                    continue
                key = relation_key(a_parts[0], a_parts[1], b_parts[0], b_parts[1])
                rels[key].append(
                    {
                        "surah_relation_id": item.get("surah_relation_id"),
                        "relation_class": item.get("relation_class"),
                        "primary_channel": item.get("primary_channel"),
                        "score": item.get("score"),
                        "cross_root": item.get("cross_root"),
                        "evidence": item.get("evidence"),
                    }
                )
    return rels


def build_candidate_bridges(
    branch_inventory: dict[str, Any],
    passage: dict[str, Any],
    q2_runs: Path,
    include_same_root: bool,
) -> dict[str, Any]:
    records = iter_branch_records(branch_inventory)
    theme_counts = theme_frequency(branch_inventory)
    keyword_counts = keyword_frequency(branch_inventory)
    q2 = load_q2_relations(q2_runs, passage)

    candidates: list[dict[str, Any]] = []
    seen_keys: set[tuple[str, str]] = set()

    for left, right in itertools.combinations(records, 2):
        if left["root"] == right["root"] and not include_same_root:
            continue

        left_branch = left["branch"]
        right_branch = right["branch"]
        shared_themes = sorted(set(left_branch["themes"]) & set(right_branch["themes"]))
        shared_parents = sorted(set(left_branch["parent_themes"]) & set(right_branch["parent_themes"]))
        shared_keywords = sorted(set(left_branch["raw_keywords"]) & set(right_branch["raw_keywords"]))
        key = relation_key(left["root"], left["branch_id"], right["root"], right["branch_id"])
        q2_hits = q2.get(key, [])

        if not shared_themes and not shared_keywords and not q2_hits:
            continue

        seen_keys.add(key)
        rare_themes = [theme for theme in shared_themes if theme_counts[theme] <= 2]
        evidence_score = (
            2 * len(shared_themes)
            + len(shared_parents)
            + 4 * len(shared_keywords)
            + len(rare_themes)
            + 5 * len(q2_hits)
        )
        if left["root"] == right["root"]:
            evidence_score -= 1

        evidence_profile = []
        if shared_themes:
            evidence_profile.append("shared_theme")
        if shared_keywords:
            evidence_profile.append("shared_keyword")
        if q2_hits:
            evidence_profile.append("q2_relation")
        if left["root"] == right["root"]:
            evidence_profile.append("same_root_cluster")
        else:
            evidence_profile.append("cross_root_bridge")

        discovery_value_hint, discovery_reasons = discovery_value(
            source_branch=left["branch_id"],
            target_branch=right["branch_id"],
            cross_root=left["root"] != right["root"],
            shared_themes=shared_themes,
            shared_keywords=shared_keywords,
            rare_themes=rare_themes,
            q2_hits=q2_hits,
        )

        candidates.append(
            {
                "source": left["root"],
                "target": right["root"],
                "source_branch": left["branch_id"],
                "target_branch": right["branch_id"],
                "source_branch_key": left["branch_key"],
                "target_branch_key": right["branch_key"],
                "cross_root": left["root"] != right["root"],
                "shared_themes": shared_themes,
                "shared_parent_themes": shared_parents,
                "shared_keywords": shared_keywords,
                "rare_shared_themes": rare_themes,
                "q2_relations": q2_hits,
                "evidence_profile": evidence_profile,
                "evidence_score_hint": evidence_score,
                "discovery_value_hint": discovery_value_hint,
                "discovery_reasons": discovery_reasons,
                "activation_hint": "latent_candidate",
                "review_bias": "preserve_unless_data_invalid",
            }
        )

    # Preserve Q2 relations even when current branch/theme extraction missed them.
    for key, hits in q2.items():
        if key in seen_keys:
            continue
        a, b = key
        a_root, a_branch = a.rsplit(" ", 1)
        b_root, b_branch = b.rsplit(" ", 1)
        candidates.append(
            {
                "source": a_root,
                "target": b_root,
                "source_branch": a_branch,
                "target_branch": b_branch,
                "source_branch_key": a,
                "target_branch_key": b,
                "cross_root": a_root != b_root,
                "shared_themes": [],
                "shared_parent_themes": [],
                "shared_keywords": [],
                "rare_shared_themes": [],
                "q2_relations": hits,
                "evidence_profile": ["q2_relation"],
                "evidence_score_hint": 5 * len(hits),
                "discovery_value_hint": 7 + 5 * len(hits),
                "discovery_reasons": ["q2_relation_preserved_even_without_theme_overlap"],
                "activation_hint": "latent_candidate",
                "review_bias": "preserve_unless_data_invalid",
            }
        )

    candidates.sort(
        key=lambda x: (
            x["cross_root"],
            x["evidence_score_hint"],
            len(x["shared_keywords"]),
            len(x["q2_relations"]),
            len(x["rare_shared_themes"]),
        ),
        reverse=True,
    )

    by_branch: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for cand in candidates:
        by_branch[cand["source_branch_key"]].append(cand)
        by_branch[cand["target_branch_key"]].append(cand)

    return {
        "schema": "v11.candidate_bridges.v1",
        "activation_bias": "recall_first",
        "rules": [
            "theme overlap may create C candidates",
            "shared keyword and Q2 relation raise review priority",
            "broad themes are retained and labeled, not pruned",
            "branches remain edge labels, not nodes",
        ],
        "candidate_count": len(candidates),
        "candidates": candidates,
        "by_branch": by_branch,
    }


def build_graph(passage: dict[str, Any], bridges: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "v11.root_port_graph.v1",
        "node_semantics": "roots_only",
        "edge_semantics": "candidate branch/port activation bridges",
        "nodes": [{"id": root, "type": "root"} for root in passage["roots_in_order"]],
        "edges": [
            {
                "source": cand["source"],
                "target": cand["target"],
                "source_branch": cand["source_branch"],
                "target_branch": cand["target_branch"],
                "shared_themes": cand["shared_themes"],
                "shared_keywords": cand["shared_keywords"],
                "q2_relations": [
                    rel.get("surah_relation_id") for rel in cand.get("q2_relations", [])
                ],
                "evidence_score_hint": cand["evidence_score_hint"],
                "discovery_value_hint": cand.get("discovery_value_hint", 0),
                "activation_hint": cand["activation_hint"],
            }
            for cand in bridges["candidates"]
        ],
    }


SURPRISE_THEMES = {
    "measurement",
    "quantity_number",
    "commerce_exchange",
    "finance_debt",
    "wealth_property",
    "provision_resource",
    "growth_decay",
    "life_stage_aging",
    "reproduction_birth",
    "sexuality",
    "body",
    "physiology",
    "food_nutrition",
    "agriculture",
    "plant_vegetation",
    "weather_climate",
    "sky_astronomy",
    "force_power",
    "substance_texture",
    "storage_vessels",
    "surface_shape",
    "support_dependence",
    "protection_security",
    "trust_loyalty",
    "identity_personhood",
}


def discovery_value(
    source_branch: str,
    target_branch: str,
    cross_root: bool,
    shared_themes: list[str],
    shared_keywords: list[str],
    rare_themes: list[str],
    q2_hits: list[dict[str, Any]],
) -> tuple[int, list[str]]:
    """Rank likely surprise, not truth.

    This deliberately does not prune broad bridges. It highlights candidates that may
    add a non-obvious underlay to the primary surface reading.
    """
    score = 0
    reasons: list[str] = []

    if cross_root:
        score += 4
        reasons.append("cross_root_activation")
    else:
        score += 1
        reasons.append("same_root_branch_cluster")

    if q2_hits:
        score += 6 + len(q2_hits)
        reasons.append("q2_relation")

    if shared_keywords:
        score += 4 + min(4, len(shared_keywords))
        reasons.append("shared_raw_keyword")

    if rare_themes:
        score += 3 + min(3, len(rare_themes))
        reasons.append("rare_theme_bridge")

    surprising_themes = sorted(set(shared_themes) & SURPRISE_THEMES)
    if surprising_themes:
        score += min(6, len(surprising_themes))
        reasons.append("material_or_surprising_underlay_theme")

    if source_branch != "B001":
        score += 1
        reasons.append("source_secondary_branch")
    if target_branch != "B001":
        score += 1
        reasons.append("target_secondary_branch")

    if len(shared_themes) >= 5 and not shared_keywords and not q2_hits:
        reasons.append("broad_theme_cluster_preserved")

    return score, reasons


def build_discovery_ranking(
    passage: dict[str, Any],
    branch_inventory: dict[str, Any],
    bridges: dict[str, Any],
    top_n: int,
) -> dict[str, Any]:
    ranked = sorted(
        bridges["candidates"],
        key=lambda item: (
            item.get("discovery_value_hint", 0),
            len(item.get("q2_relations", [])),
            len(item.get("shared_keywords", [])),
            item.get("evidence_score_hint", 0),
        ),
        reverse=True,
    )

    by_branch: dict[str, dict[str, Any]] = {}
    for cand in ranked:
        for side in ("source", "target"):
            root = cand[side]
            branch_id = cand[f"{side}_branch"]
            branch_key = f"{root} {branch_id}"
            branch = branch_inventory["roots"].get(root, {}).get("branches", {}).get(branch_id, {})
            image = branch.get("image") or {}
            item = by_branch.setdefault(
                branch_key,
                {
                    "root": root,
                    "branch": branch_id,
                    "branch_image_ar": image.get("branch_image_ar"),
                    "max_discovery_value_hint": 0,
                    "bridge_count": 0,
                    "top_bridge_keys": [],
                    "discovery_reasons": [],
                },
            )
            item["bridge_count"] += 1
            item["max_discovery_value_hint"] = max(
                item["max_discovery_value_hint"],
                cand.get("discovery_value_hint", 0),
            )
            if len(item["top_bridge_keys"]) < 8:
                other_key = cand["target_branch_key"] if side == "source" else cand["source_branch_key"]
                item["top_bridge_keys"].append(other_key)
            for reason in cand.get("discovery_reasons", []):
                if reason not in item["discovery_reasons"]:
                    item["discovery_reasons"].append(reason)

    branch_rank = sorted(
        by_branch.values(),
        key=lambda item: (item["max_discovery_value_hint"], item["bridge_count"]),
        reverse=True,
    )

    return {
        "schema": "v11.discovery_ranking.v1",
        "activation_bias": "recall_first",
        "ranking_semantics": "Ranks likely surprise/discovery value; does not prune the candidate reservoir.",
        "passage": passage["passage"],
        "top_candidate_bridges": ranked[:top_n],
        "top_branch_candidates": branch_rank[:top_n],
    }


def write_agent_packet(
    path: Path,
    passage: dict[str, Any],
    branches: dict[str, Any],
    bridges: dict[str, Any],
    top_n: int,
) -> None:
    lines: list[str] = []
    p = passage["passage"]
    lines.append(f"# v11 Activation Packet — S{p['surah']}:{p['ayah_start']}-{p['ayah_end']}")
    lines.append("")
    lines.append("Bias: recall-first. Preserve latent candidates with labels instead of pruning.")
    lines.append("")
    lines.append("## Surface roots")
    lines.append("")
    lines.append(" → ".join(passage["roots_in_order"]))
    lines.append("")
    lines.append("## Branch inventory summary")
    lines.append("")
    for root in passage["roots_in_order"]:
        root_info = branches["roots"].get(root)
        if not root_info:
            lines.append(f"- {root}: missing root mapping")
            continue
        lines.append(
            f"- {root}: {root_info['branch_count']} branches "
            f"({root_info.get('qnet_branch_count', 0)} with Qnet bridge-theme nodes; "
            f"{len(root_info.get('branches_without_qnet_themes', []))} Furūq-only)"
        )
    lines.append("")
    lines.append("## QAC-first root resolution audit")
    lines.append("")
    for item in branches.get("root_resolution_audit", []):
        matches = ", ".join(m["root_id"] for m in item["matches"]) or "—"
        qac_keys = ", ".join(item["qac_root_join_keys"]) or "—"
        lines.append(
            f"- {item['qac_root']} | qac_keys={qac_keys} | status={item['status']} | matches={matches}"
        )
    furq_only_roots = [
        root
        for root in passage["roots_in_order"]
        if branches["roots"].get(root, {}).get("branch_count", 0) > 0
        and branches["roots"].get(root, {}).get("qnet_branch_count", 0) == 0
    ]
    if furq_only_roots:
        lines.append("")
        lines.append("Furūq-only roots in this run: " + ", ".join(furq_only_roots))
        lines.append("These roots have branch images but no bridge-theme memberships in the current Qnet layer.")
    lines.append("")
    lines.append("## Top candidate bridges")
    lines.append("")
    for cand in bridges["candidates"][:top_n]:
        themes = ", ".join(cand["shared_themes"][:8]) or "—"
        keywords = ", ".join(cand["shared_keywords"][:8]) or "—"
        q2_ids = ", ".join(
            rel.get("surah_relation_id") or "q2" for rel in cand.get("q2_relations", [])
        ) or "—"
        lines.append(
            f"- `{cand['source_branch_key']}` ↔ `{cand['target_branch_key']}` "
            f"| score_hint={cand['evidence_score_hint']} "
            f"| discovery_hint={cand.get('discovery_value_hint', 0)} "
            f"| themes={themes} | keywords={keywords} | q2={q2_ids}"
        )
    lines.append("")
    lines.append("## Per-root candidate activations")
    lines.append("")
    for root in passage["roots_in_order"]:
        root_info = branches["roots"].get(root)
        if not root_info:
            continue
        lines.append(f"### {root}")
        lines.append("")
        for branch_id, branch in root_info["branches"].items():
            key = f"{root} {branch_id}"
            image = branch["image"] or {}
            branch_title = image.get("branch_image_ar") or "(missing image)"
            hits = bridges["by_branch"].get(key, [])
            if not hits:
                if branch.get("qnet_membership") == "absent_from_bridge_theme_current":
                    lines.append(f"- `{key}` — {branch_title}")
                    lines.append("  - activated_by_or_with: no Qnet bridge-theme memberships in this layer")
                    lines.append("  - themes: —")
                    lines.append("  - keywords: —")
                continue
            other_roots = sorted(
                {
                    h["target"] if h["source"] == root else h["source"]
                    for h in hits
                    if h["source"] != h["target"]
                }
            )
            themes = sorted({t for h in hits for t in h["shared_themes"]})
            keywords = sorted({k for h in hits for k in h["shared_keywords"]})
            lines.append(f"- `{key}` — {branch_title}")
            lines.append(f"  - activated_by_or_with: {', '.join(other_roots) or 'same-root only'}")
            lines.append(f"  - themes: {', '.join(themes[:12]) or '—'}")
            lines.append(f"  - keywords: {', '.join(keywords[:12]) or '—'}")
        lines.append("")
    lines.append("## Agent instruction")
    lines.append("")
    lines.append("Classify branches as A/B/C/S/X, but use discovery bias:")
    lines.append("")
    lines.append("- uncertain S vs C => C")
    lines.append("- uncertain C vs B => C/B")
    lines.append("- broad bridge => preserve with evidence profile")
    lines.append("- only data-invalid branches => X")
    lines.append("- after broad activation, rank by discovery value: surprise, hidden material underlay, and added mechanism")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build v11 Qnet latent activation candidates.")
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--ayah-start", type=int, required=True)
    parser.add_argument("--ayah-end", type=int)
    parser.add_argument("--include-basmala", action="store_true")
    parser.add_argument("--qac", type=Path, default=DEFAULT_QAC)
    parser.add_argument("--furuq", type=Path, default=DEFAULT_FURUQ)
    parser.add_argument("--qnet", type=Path, default=DEFAULT_QNET)
    parser.add_argument("--q2-runs", type=Path, default=DEFAULT_Q2_RUNS)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--include-same-root", action="store_true", default=True)
    parser.add_argument("--allow-unresolved-roots", action="store_true")
    parser.add_argument("--allow-qnetless-roots", action="store_true")
    parser.add_argument("--top-n", type=int, default=80)
    return parser.parse_args()


def main() -> None:
    ns = parse_args()
    out_dir = ns.out_dir
    if not out_dir.is_absolute():
        out_dir = REPO_ROOT / out_dir
    ensure_out_dir(out_dir)

    with tempfile.TemporaryDirectory(prefix="v11-qnet-") as tmp:
        temp_dir = Path(tmp)
        qac = connect_sqlite(ns.qac, temp_dir)
        furuq = connect_sqlite(ns.furuq, temp_dir)
        qnet = connect_sqlite(ns.qnet, temp_dir)

        passage_args = PassageArgs(
            surah=ns.surah,
            ayah_start=ns.ayah_start,
            ayah_end=ns.ayah_end,
            include_basmala=ns.include_basmala,
        )
        passage = extract_passage(qac, passage_args)
        branches = load_branch_inventory(furuq, qnet, passage)
        write_json(
            out_dir / "00-root-resolution-audit.json",
            {
                "schema": "v11.root_resolution_audit.v1",
                "policy": "qac_first_with_hamza_variant_audit",
                "qnet_source": str(ns.qnet),
                "audit": branches.get("root_resolution_audit", []),
                "missing_roots": branches.get("missing_roots", []),
            },
        )

        unresolved = [
            item for item in branches.get("root_resolution_audit", [])
            if item.get("status") != "resolved"
        ]
        if unresolved and not ns.allow_unresolved_roots:
            unresolved_roots = ", ".join(item["qac_root"] for item in unresolved)
            raise SystemExit(
                f"Refusing to continue before agents: unresolved/ambiguous QAC roots: {unresolved_roots}. "
                "Use --allow-unresolved-roots only for diagnostics."
            )

        qnetless_roots = [
            root
            for root, info in branches["roots"].items()
            if info.get("branch_count", 0) > 0 and info.get("qnet_branch_count", 0) == 0
        ]
        if qnetless_roots and not ns.allow_qnetless_roots:
            raise SystemExit(
                "Refusing to continue before agents: roots have Furūq branches but zero Qnet branch nodes "
                f"in the selected Qnet layer: {', '.join(qnetless_roots)}. "
                "Use bridge_theme_full or --allow-qnetless-roots only for diagnostics."
            )

        bridges = build_candidate_bridges(
            branches,
            passage,
            ns.q2_runs,
            include_same_root=ns.include_same_root,
        )
        discovery = build_discovery_ranking(passage, branches, bridges, ns.top_n)
        graph = build_graph(passage, bridges)

        write_json(out_dir / "01-passage.json", passage)
        write_json(out_dir / "02-branches.json", branches)
        write_json(out_dir / "03-candidate-bridges.json", bridges)
        write_agent_packet(out_dir / "04-agent-activation-packet.md", passage, branches, bridges, ns.top_n)
        write_json(out_dir / "08-graph.json", graph)
        write_json(out_dir / "10-discovery-ranking.json", discovery)

    print(f"wrote {out_dir}")
    print(f"roots={passage['root_count']} branches={sum(r['branch_count'] for r in branches['roots'].values())} candidates={bridges['candidate_count']} discovery_ranked={len(discovery['top_candidate_bridges'])}")


if __name__ == "__main__":
    main()
