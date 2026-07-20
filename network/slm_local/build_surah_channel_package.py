#!/usr/bin/env python3
"""Build channel candidates from quran-slm local affinity bundles plus Qnet."""

from __future__ import annotations

import argparse
import ast
import collections
import csv
import json
import math
import struct
from pathlib import Path
from typing import Any


PRIMARY_OR_NOISE_TERMS = {
    "adoration",
    "antiquity",
    "blade",
    "condiment",
    "creed",
    "deity",
    "devotion",
    "divinity",
    "grammar",
    "hawk",
    "monotheism",
    "particle",
    "paste",
    "preposition",
    "raptor",
    "religion",
    "syrup",
    "theology",
    "worship",
}

GENERIC_THEME_FRAGMENTS = {
    "animal_life/animal",
    "animal_life/habitat_ecology",
    "condition_force_change/abundance_scarcity",
    "condition_force_change/agency_action",
    "condition_force_change/capacity_ability",
    "condition_force_change/change_transition",
    "condition_force_change/force_power",
    "condition_force_change/growth_decay",
    "condition_force_change/loss_absence",
    "condition_force_change/stability_endurance",
    "condition_force_change/support_dependence",
    "condition_force_change/value_quality",
    "emotion_ethics/emotion",
    "emotion_ethics/ethics_morality",
    "emotion_ethics/fear_grief",
    "emotion_ethics/honor_shame",
    "emotion_ethics/suffering_hardship",
    "emotion_ethics/trust_loyalty",
}


DOMAIN_RULES = [
    {
        "domain_id": "D01",
        "label": "motion / force / incursion / center",
        "terms": {
            "attack",
            "centering",
            "center",
            "dust",
            "eruption",
            "force",
            "gallop",
            "gathering",
            "incursion",
            "insertion",
            "locomotion",
            "middle",
            "motion",
            "movement",
            "raid",
            "rising",
            "run",
            "running",
            "speed",
            "sprint",
            "stirring",
            "transport",
        },
        "specific_themes": {
            "movement_travel/motion",
            "movement_travel/travel",
            "movement_travel/transport",
        },
    },
    {
        "domain_id": "D02",
        "label": "fire / ignition / light / daybreak",
        "terms": {
            "combustion",
            "dawn",
            "day",
            "daybreak",
            "daytime",
            "fire",
            "flame",
            "ignition",
            "illumination",
            "lamp",
            "light",
            "morning",
            "scorching",
            "spark",
        },
        "specific_themes": {
            "land_water_sky/fire_heat",
            "land_water_sky/light_darkness",
        },
    },
    {
        "domain_id": "D03",
        "label": "conflict / redress / judgment / restraint",
        "terms": {
            "appeal",
            "conflict",
            "compensation",
            "contract",
            "covenant",
            "justice",
            "law",
            "obligation",
            "punishment",
            "redress",
            "restraint",
            "sanction",
            "testimony",
            "violence",
        },
        "specific_themes": {
            "conflict_security/conflict",
            "conflict_security/danger_harm",
            "conflict_security/protection_security",
            "conflict_security/violence_warfare",
            "law_governance/justice_judgment",
            "law_governance/law",
            "law_governance/obligation_contract",
        },
    },
    {
        "domain_id": "D04",
        "label": "favor / wealth / attachment / ingratitude",
        "terms": {
            "attachment",
            "benefit",
            "blessing",
            "bounty",
            "commerce",
            "desire",
            "favor",
            "generosity",
            "good",
            "gratitude",
            "hospitality",
            "ingratitude",
            "miserliness",
            "property",
            "wealth",
            "withholding",
        },
        "specific_themes": {
            "economy_property/provision_resource",
            "economy_property/wealth_property",
            "emotion_ethics/desire_appetite",
            "kinship_society/hospitality_welfare",
        },
    },
    {
        "domain_id": "D05",
        "label": "concealment / extraction / knowledge / testimony",
        "terms": {
            "burial",
            "chest",
            "concealment",
            "disclosure",
            "extraction",
            "grave",
            "hiddenness",
            "inner",
            "knowledge",
            "proof",
            "testimony",
            "uncovering",
        },
        "specific_themes": {
            "cognition_perception/knowledge_learning",
            "cognition_perception/proof_uncertainty",
            "language_communication/concealment_disclosure",
        },
    },
    {
        "domain_id": "D06",
        "label": "water / growth / fertility / barrenness",
        "terms": {
            "agriculture",
            "barren",
            "botany",
            "cloud",
            "cultivation",
            "ecology",
            "fertility",
            "fruit",
            "growth",
            "herbage",
            "moisture",
            "plant",
            "water",
        },
        "specific_themes": {
            "agriculture_food/agriculture",
            "agriculture_food/pasture_forage",
            "agriculture_food/plant_vegetation",
            "land_water_sky/water_hydrology",
            "land_water_sky/weather_climate",
        },
    },
    {
        "domain_id": "D07",
        "label": "guidance / road / direction",
        "terms": {
            "direction",
            "guidance",
            "journey",
            "navigation",
            "path",
            "road",
            "route",
            "straightness",
        },
        "specific_themes": {
            "movement_travel/navigation_route",
            "movement_travel/orientation_direction",
        },
    },
    {
        "domain_id": "D08",
        "label": "authority / obedience / hierarchy",
        "terms": {
            "authority",
            "dominion",
            "hierarchy",
            "kingship",
            "obedience",
            "servitude",
            "sovereignty",
            "submission",
        },
        "specific_themes": {
            "kinship_society/hierarchy_status",
            "law_governance/authority_governance",
        },
    },
]


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")))
            handle.write("\n")


def read_npy_2d(path: Path) -> tuple[list[list[float]], tuple[int, int], str]:
    """Small no-NumPy reader for little-endian float32/float64 2D .npy files."""

    data = path.read_bytes()
    if not data.startswith(b"\x93NUMPY"):
        raise ValueError(f"not a .npy file: {path}")
    major = data[6]
    if major == 1:
        header_len = struct.unpack("<H", data[8:10])[0]
        offset = 10
    elif major in {2, 3}:
        header_len = struct.unpack("<I", data[8:12])[0]
        offset = 12
    else:
        raise ValueError(f"unsupported .npy version: {major}")
    header = ast.literal_eval(data[offset : offset + header_len].decode("latin1").strip())
    descr = header["descr"]
    shape = tuple(header["shape"])
    if header.get("fortran_order"):
        raise ValueError("Fortran-order .npy is not supported")
    if len(shape) != 2:
        raise ValueError(f"expected 2D matrix, got {shape}")
    if descr == "<f4":
        code = "f"
        size = 4
    elif descr == "<f8":
        code = "d"
        size = 8
    else:
        raise ValueError(f"unsupported dtype: {descr}")
    count = shape[0] * shape[1]
    values = struct.unpack("<" + code * count, data[offset + header_len : offset + header_len + count * size])
    matrix = [
        [float(values[row * shape[1] + col]) for col in range(shape[1])]
        for row in range(shape[0])
    ]
    return matrix, (int(shape[0]), int(shape[1])), descr


def load_branches(path: Path) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return {row["node_id"]: row for row in csv.DictReader(handle, delimiter="\t")}


def load_qnet_keywords(path: Path) -> tuple[dict[tuple[str, str], list[dict[str, Any]]], dict[str, float]]:
    by_branch: dict[tuple[str, str], list[dict[str, Any]]] = collections.defaultdict(list)
    keyword_branches: dict[str, set[tuple[str, str]]] = collections.defaultdict(set)
    with path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            key = (row["root_id"], row["branch_id"])
            votes = int(row["replicate_votes"])
            by_branch[key].append(
                {
                    "facet": f"kw:{row['keyword']}",
                    "keyword": row["keyword"],
                    "score": votes,
                    "support_count": 1,
                    "support": [f"{row['root_id']}:{row['branch_id']}"],
                }
            )
            keyword_branches[row["keyword"]].add(key)
    total = len(set().union(*keyword_branches.values())) if keyword_branches else 0
    idf = {
        keyword: math.log((1 + total) / (1 + len(branches))) + 1.0
        for keyword, branches in keyword_branches.items()
    }
    return by_branch, idf


def load_qnet_themes(path: Path) -> tuple[dict[tuple[str, str], list[dict[str, Any]]], dict[str, float]]:
    by_branch: dict[tuple[str, str], list[dict[str, Any]]] = collections.defaultdict(list)
    theme_branches: dict[str, set[tuple[str, str]]] = collections.defaultdict(set)
    with path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            key = (row["root_id"], row["branch_id"])
            theme = f"{row['parent_theme']}/{row['theme']}"
            by_branch[key].append(
                {
                    "facet": f"theme:{theme}",
                    "theme": theme,
                    "score": int(row["raw_keyword_count"]),
                    "support_count": 1,
                    "support": [f"{row['root_id']}:{row['branch_id']}"],
                }
            )
            theme_branches[theme].add(key)
    total = len(set().union(*theme_branches.values())) if theme_branches else 0
    idf = {
        theme: math.log((1 + total) / (1 + len(branches))) + 1.0
        for theme, branches in theme_branches.items()
    }
    return by_branch, idf


def parse_node_id(node_id: str) -> tuple[str, str]:
    _, root_id, branch_id = node_id.split(":")
    return root_id, branch_id


def facet_text(facet: str) -> str:
    return facet.split(":", 1)[-1].lower()


def is_ignored_facet(facet: str) -> bool:
    text = facet_text(facet)
    return any(term in text for term in PRIMARY_OR_NOISE_TERMS)


def branch_facets(
    node_id: str,
    keywords: dict[tuple[str, str], list[dict[str, Any]]],
    keyword_idf: dict[str, float],
    themes: dict[tuple[str, str], list[dict[str, Any]]],
    theme_idf: dict[str, float],
) -> list[dict[str, Any]]:
    key = parse_node_id(node_id)
    out = []
    for item in keywords.get(key, []):
        if item["score"] < 2:
            continue
        facet = item["facet"]
        if is_ignored_facet(facet):
            continue
        out.append({**item, "weight": round(keyword_idf.get(item["keyword"], 1.0) * item["score"], 6)})
    for item in themes.get(key, []):
        facet = item["facet"]
        if is_ignored_facet(facet):
            continue
        out.append({**item, "weight": round(theme_idf.get(item["theme"], 1.0) * item["score"], 6)})
    out.sort(key=lambda row: (-row["weight"], row["facet"]))
    return out[:24]


def facet_matches(facet: str, terms: set[str]) -> bool:
    text = facet_text(facet)
    return any(term in text for term in terms)


def domain_facet_hits(facets: list[dict[str, Any]], rule: dict[str, Any]) -> tuple[list[dict[str, Any]], float]:
    terms = rule["terms"]
    specific_themes = rule.get("specific_themes", set())
    hits = []
    score = 0.0
    for item in facets:
        facet = item["facet"]
        text = facet_text(facet)
        is_keyword = facet.startswith("kw:")
        is_specific_theme = facet.startswith("theme:") and text in specific_themes
        if facet.startswith("theme:") and text in GENERIC_THEME_FRAGMENTS:
            continue
        if not (facet_matches(facet, terms) or is_specific_theme):
            continue
        weight = float(item.get("weight", item.get("score", 1.0)))
        if is_keyword:
            adjusted = weight
        elif is_specific_theme:
            adjusted = weight * 0.75
        else:
            adjusted = weight * 0.35
        hits.append({**item, "domain_weight": round(adjusted, 6)})
        score += adjusted
    hits.sort(key=lambda row: (-row["domain_weight"], row["facet"]))
    return hits, score


def ayah_pairs(source_ayahs: list[int], target_ayahs: list[int], *, skip_n: int) -> list[tuple[int, int]]:
    out = []
    max_distance = skip_n + 1
    for left in source_ayahs:
        for right in target_ayahs:
            if right < left:
                continue
            if right == left or right - left <= max_distance:
                out.append((left, right))
    return out


def build_slm_edges(
    catalog: dict[str, Any],
    affinity: list[list[float]],
    branch_rows: dict[str, dict[str, str]],
    *,
    top_k: int,
    skip_n: int,
) -> list[dict[str, Any]]:
    branches = catalog["branches"]
    index_to_branch = {int(row["index"]): row for row in branches}
    edges: dict[tuple[int, int, int, int], dict[str, Any]] = {}

    for source in branches:
        source_index = int(source["index"])
        ranked_by_target_ayah: dict[int, list[tuple[float, dict[str, Any]]]] = collections.defaultdict(list)
        for target in branches:
            target_index = int(target["index"])
            if source_index == target_index or source["root"] == target["root"]:
                continue
            score = affinity[source_index][target_index]
            if score <= 0:
                continue
            for left_ayah, right_ayah in ayah_pairs(source["ayahs"], target["ayahs"], skip_n=skip_n):
                ranked_by_target_ayah[right_ayah].append((score, target))

        for target_ayah, items in ranked_by_target_ayah.items():
            items.sort(key=lambda item: (-item[0], item[1]["display_key"], item[1]["node_id"]))
            for rank, (score, target) in enumerate(items[:top_k], start=1):
                for source_ayah in source["ayahs"]:
                    if (source_ayah, target_ayah) not in ayah_pairs([source_ayah], target["ayahs"], skip_n=skip_n):
                        continue
                    key = (source_index, int(target["index"]), source_ayah, target_ayah)
                    source_row = branch_rows[source["node_id"]]
                    target_row = branch_rows[target["node_id"]]
                    edges[key] = {
                        "edge_id": f"E{len(edges)+1:06d}",
                        "source_index": source_index,
                        "target_index": int(target["index"]),
                        "source_ayah": source_ayah,
                        "target_ayah": target_ayah,
                        "source_node_id": source["node_id"],
                        "target_node_id": target["node_id"],
                        "source_root": source["root"],
                        "target_root": target["root"],
                        "source_branch_id": source["branch_id"],
                        "target_branch_id": target["branch_id"],
                        "source_branch_image_ar": source_row["branch_image_ar"],
                        "target_branch_image_ar": target_row["branch_image_ar"],
                        "affinity": round(float(score), 8),
                        "rank_for_source_target_ayah": rank,
                    }
    return sorted(edges.values(), key=lambda row: (row["source_ayah"], row["target_ayah"], row["rank_for_source_target_ayah"], row["edge_id"]))


def channel_record(
    rule: dict[str, Any],
    catalog: dict[str, Any],
    branch_rows: dict[str, dict[str, str]],
    edges: list[dict[str, Any]],
    facets_by_node: dict[str, list[dict[str, Any]]],
) -> dict[str, Any] | None:
    anchor_min_score = 8.0
    anchor_nodes: set[str] = set()
    anchor_hits_by_node: dict[str, list[dict[str, Any]]] = {}
    branch_by_node = {branch["node_id"]: branch for branch in catalog["branches"]}

    for branch in catalog["branches"]:
        hits, score = domain_facet_hits(facets_by_node.get(branch["node_id"], []), rule)
        if score >= anchor_min_score:
            anchor_nodes.add(branch["node_id"])
            anchor_hits_by_node[branch["node_id"]] = hits[:8]

    if not anchor_nodes:
        return None

    anchor_roots: set[str] = set()
    anchor_branches: set[str] = set()
    anchor_ayahs: set[int] = set()
    per_ayah: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
    facet_hits: collections.Counter[str] = collections.Counter()

    for node_id in sorted(anchor_nodes, key=lambda node: (branch_by_node[node]["ayahs"], branch_by_node[node]["display_key"])):
        branch = branch_by_node[node_id]
        row = branch_rows[node_id]
        anchor_roots.add(branch["root"])
        anchor_branches.add(branch["display_key"])
        for ayah in branch["ayahs"]:
            anchor_ayahs.add(ayah)
            per_ayah[int(ayah)].append(
                {
                    "root": branch["root"],
                    "branch_id": branch["branch_id"],
                    "branch_image_ar": row["branch_image_ar"],
                    "matched_facets": [item["facet"] for item in anchor_hits_by_node[node_id][:5]],
                }
            )
        for item in anchor_hits_by_node[node_id][:5]:
            facet_hits[item["facet"]] += 1

    if len(anchor_branches) < 3 or len(anchor_roots) < 3 or len(anchor_ayahs) < 3:
        return None

    anchor_edges = []
    bridge_edges = []
    bridge_nodes: set[str] = set()
    bridge_roots: set[str] = set()
    scores = []
    bridge_scores = []
    support_examples = []

    for edge in edges:
        source_anchor = edge["source_node_id"] in anchor_nodes
        target_anchor = edge["target_node_id"] in anchor_nodes
        if source_anchor and target_anchor:
            anchor_edges.append(edge)
            scores.append(edge["affinity"])
        elif (source_anchor or target_anchor) and edge["rank_for_source_target_ayah"] <= 3:
            bridge_edges.append(edge)
            bridge_scores.append(edge["affinity"])
            other = edge["target_node_id"] if source_anchor else edge["source_node_id"]
            bridge_nodes.add(other)
            bridge_roots.add(branch_by_node[other]["root"])

    example_source = sorted(anchor_edges, key=lambda row: (-row["affinity"], row["rank_for_source_target_ayah"]))[:8]
    if len(example_source) < 8:
        example_source += sorted(bridge_edges, key=lambda row: (-row["affinity"], row["rank_for_source_target_ayah"]))[: 8 - len(example_source)]
    for edge in example_source:
        matched_nodes = [node for node in (edge["source_node_id"], edge["target_node_id"]) if node in anchor_nodes]
        support_examples.append(
            {
                "edge_id": edge["edge_id"],
                "rank": edge["rank_for_source_target_ayah"],
                "affinity": edge["affinity"],
                "ayahs": [edge["source_ayah"], edge["target_ayah"]],
                "chain": [
                    f"{edge['source_root']}:{edge['source_branch_id']}:{edge['source_branch_image_ar']}",
                    f"{edge['target_root']}:{edge['target_branch_id']}:{edge['target_branch_image_ar']}",
                ],
                "matched_facets": sorted(
                    {
                        item["facet"]
                        for node_id in matched_nodes
                        for item in anchor_hits_by_node.get(node_id, [])[:4]
                    }
                ),
                "edge_type": "anchor" if edge in anchor_edges else "bridge",
            }
        )

    edge_roots: collections.Counter[str] = collections.Counter()
    for edge in anchor_edges:
        edge_roots[edge["source_root"]] += 1
        edge_roots[edge["target_root"]] += 1
    if anchor_edges:
        root_ablation = min(
            sum(1 for edge in anchor_edges if root not in {edge["source_root"], edge["target_root"]}) / len(anchor_edges)
            for root in anchor_roots
        )
    else:
        root_ablation = 0.0
    mean_affinity = sum(scores) / max(1, len(scores))
    strong_edge_ratio = sum(1 for edge in anchor_edges if edge["rank_for_source_target_ayah"] <= 3) / max(1, len(anchor_edges))
    ayah_span_ratio = len(anchor_ayahs) / max(1, len(set(a for edge in edges for a in (edge["source_ayah"], edge["target_ayah"]))))
    continuity = len(anchor_edges) / max(1, len(anchor_branches))
    stability = (
        0.25 * min(1.0, math.log1p(len(anchor_edges)) / math.log1p(40))
        + 0.20 * min(1.0, len(anchor_roots) / 6)
        + 0.20 * ayah_span_ratio
        + 0.15 * strong_edge_ratio
        + 0.10 * root_ablation
        + 0.10 * min(1.0, continuity)
    )
    status = "stable" if stability >= 0.62 and len(anchor_edges) >= 3 else "mixed" if stability >= 0.45 else "weak"

    return {
        "channel_id": rule["domain_id"],
        "label": rule["label"],
        "status": status,
        "stability_score": round(stability, 4),
        "anchor_edge_count": len(anchor_edges),
        "bridge_edge_count": len(bridge_edges),
        "strong_edge_ratio": round(strong_edge_ratio, 4),
        "mean_affinity": round(mean_affinity, 8),
        "bridge_mean_affinity": round(sum(bridge_scores) / max(1, len(bridge_scores)), 8),
        "root_ablation_min_survival": round(root_ablation, 4),
        "ayahs": sorted(anchor_ayahs),
        "roots": sorted(anchor_roots),
        "unique_branch_count": len(anchor_branches),
        "bridge_roots": sorted(bridge_roots - anchor_roots),
        "bridge_branch_count": len(bridge_nodes - anchor_nodes),
        "top_facets": facet_hits.most_common(16),
        "per_ayah_build": {str(ayah): rows for ayah, rows in sorted(per_ayah.items())},
        "support_examples": support_examples,
    }


def old_channel_record(
    rule: dict[str, Any],
    edges: list[dict[str, Any]],
    facets_by_node: dict[str, list[dict[str, Any]]],
) -> dict[str, Any] | None:
    terms = rule["terms"]
    kept = []
    facet_hits: collections.Counter[str] = collections.Counter()
    roots: set[str] = set()
    branches: set[str] = set()
    ayahs: set[int] = set()
    scores = []
    support_examples = []

    for edge in edges:
        source_facets = [f for f in facets_by_node.get(edge["source_node_id"], []) if facet_matches(f["facet"], terms)]
        target_facets = [f for f in facets_by_node.get(edge["target_node_id"], []) if facet_matches(f["facet"], terms)]
        if not source_facets and not target_facets:
            continue
        # Prefer edges where at least one endpoint is directly in-domain and the
        # other endpoint is either in-domain or a strong SLM neighbor.
        if not (source_facets and target_facets) and edge["rank_for_source_target_ayah"] > 5:
            continue
        kept.append(edge)
        roots.update([edge["source_root"], edge["target_root"]])
        branches.update([f"{edge['source_root']}:{edge['source_branch_id']}", f"{edge['target_root']}:{edge['target_branch_id']}"])
        ayahs.update([edge["source_ayah"], edge["target_ayah"]])
        scores.append(edge["affinity"])
        for item in source_facets[:3] + target_facets[:3]:
            facet_hits[item["facet"]] += 1
        if len(support_examples) < 8:
            support_examples.append(
                {
                    "edge_id": edge["edge_id"],
                    "rank": edge["rank_for_source_target_ayah"],
                    "affinity": edge["affinity"],
                    "ayahs": [edge["source_ayah"], edge["target_ayah"]],
                    "chain": [
                        f"{edge['source_root']}:{edge['source_branch_id']}:{edge['source_branch_image_ar']}",
                        f"{edge['target_root']}:{edge['target_branch_id']}:{edge['target_branch_image_ar']}",
                    ],
                    "matched_facets": sorted({item["facet"] for item in source_facets[:4] + target_facets[:4]}),
                }
            )

    if len(kept) < 3 or len(roots) < 3 or len(ayahs) < 3:
        return None

    edge_roots: collections.Counter[str] = collections.Counter()
    for edge in kept:
        edge_roots[edge["source_root"]] += 1
        edge_roots[edge["target_root"]] += 1
    root_ablation = min(
        sum(1 for edge in kept if root not in {edge["source_root"], edge["target_root"]}) / len(kept)
        for root in roots
    )
    mean_affinity = sum(scores) / max(1, len(scores))
    strong_edge_ratio = sum(1 for edge in kept if edge["rank_for_source_target_ayah"] <= 3) / len(kept)
    ayah_span_ratio = len(ayahs) / max(1, len(set(a for edge in edges for a in (edge["source_ayah"], edge["target_ayah"]))))
    stability = (
        0.30 * min(1.0, math.log1p(len(kept)) / math.log1p(80))
        + 0.20 * min(1.0, len(roots) / 8)
        + 0.20 * ayah_span_ratio
        + 0.15 * strong_edge_ratio
        + 0.15 * root_ablation
    )
    status = "stable" if stability >= 0.62 and root_ablation >= 0.15 else "mixed" if stability >= 0.45 else "weak"

    return {
        "channel_id": rule["domain_id"],
        "label": rule["label"],
        "status": status,
        "stability_score": round(stability, 4),
        "edge_count": len(kept),
        "strong_edge_ratio": round(strong_edge_ratio, 4),
        "mean_affinity": round(mean_affinity, 8),
        "root_ablation_min_survival": round(root_ablation, 4),
        "ayahs": sorted(ayahs),
        "roots": sorted(roots),
        "unique_branch_count": len(branches),
        "top_facets": facet_hits.most_common(16),
        "support_examples": support_examples,
    }


def write_channel_tsv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "channel_id",
                "status",
                "label",
                "stability_score",
                "anchor_edge_count",
                "bridge_edge_count",
                "strong_edge_ratio",
                "mean_affinity",
                "root_ablation_min_survival",
                "ayahs",
                "roots",
                "unique_branch_count",
                "top_facets",
                "example_chain",
            ]
        )
        for row in rows:
            writer.writerow(
                [
                    row["channel_id"],
                    row["status"],
                    row["label"],
                    row["stability_score"],
                    row["anchor_edge_count"],
                    row["bridge_edge_count"],
                    row["strong_edge_ratio"],
                    row["mean_affinity"],
                    row["root_ablation_min_survival"],
                    ",".join(map(str, row["ayahs"])),
                    " ".join(row["roots"]),
                    row["unique_branch_count"],
                    "; ".join(f"{facet}({count})" for facet, count in row["top_facets"][:10]),
                    " → ".join(row["support_examples"][0]["chain"]) if row["support_examples"] else "",
                ]
            )


def build(args: argparse.Namespace) -> dict[str, Any]:
    surah_tag = f"s{args.surah:03d}"
    source_repo = Path(args.quran_slm)
    qnet_repo = Path(args.quran_roots)
    output_dir = Path(args.output_dir) / surah_tag
    output_dir.mkdir(parents=True, exist_ok=True)

    catalog = read_json(source_repo / "artifacts/surah_networks" / surah_tag / "catalog.json")
    report = read_json(source_repo / "artifacts/surah_networks" / surah_tag / "build_report.json")
    affinity, shape, dtype = read_npy_2d(source_repo / "artifacts/surah_networks" / surah_tag / "affinity.npy")
    branch_rows = load_branches(source_repo / "resources/surahs" / surah_tag / "branches_ar.tsv")

    keywords, keyword_idf = load_qnet_keywords(
        qnet_repo / "_corpus/activation/Qnet/v2/network/incidence_full/branch_keywords.tsv"
    )
    themes, theme_idf = load_qnet_themes(
        qnet_repo / "_corpus/activation/Qnet/v2/network/bridge_theme_full/branch_theme_inventory.tsv"
    )
    facets_by_node = {
        branch["node_id"]: branch_facets(branch["node_id"], keywords, keyword_idf, themes, theme_idf)
        for branch in catalog["branches"]
    }

    edges = build_slm_edges(
        catalog,
        affinity,
        branch_rows,
        top_k=args.top_k,
        skip_n=int(catalog.get("policy", {}).get("skip_n", args.skip_n)),
    )
    channels = [
        record
        for rule in DOMAIN_RULES
        if (record := channel_record(rule, catalog, branch_rows, edges, facets_by_node)) is not None
    ]
    channels.sort(key=lambda row: ({"stable": 0, "mixed": 1, "weak": 2}[row["status"]], -row["stability_score"], row["channel_id"]))

    write_jsonl(output_dir / "slm_edges.jsonl", edges)
    write_jsonl(output_dir / "domain_channel_candidates.jsonl", channels)
    write_channel_tsv(output_dir / "domain_channel_candidates.tsv", channels)

    summary = {
        "version": "slm_local_qnet_channel_adapter_v0",
        "surah": args.surah,
        "inputs": {
            "slm_algorithm_version": report.get("algorithm_version"),
            "catalog_branch_count": len(catalog["branches"]),
            "affinity_shape": shape,
            "affinity_dtype": dtype,
            "qnet_policy": "existing keywords/themes only",
        },
        "parameters": {"top_k": args.top_k, "skip_n": catalog.get("policy", {}).get("skip_n", args.skip_n)},
        "counts": {
            "slm_edges": len(edges),
            "channels_total": len(channels),
            "stable_channels": sum(1 for row in channels if row["status"] == "stable"),
            "mixed_channels": sum(1 for row in channels if row["status"] == "mixed"),
            "weak_channels": sum(1 for row in channels if row["status"] == "weak"),
        },
        "channels": [
            {
                "channel_id": row["channel_id"],
                "status": row["status"],
                "label": row["label"],
                "stability_score": row["stability_score"],
                "anchor_edge_count": row["anchor_edge_count"],
                "bridge_edge_count": row["bridge_edge_count"],
                "ayahs": row["ayahs"],
                "roots": row["roots"],
                "unique_branch_count": row["unique_branch_count"],
            }
            for row in channels
        ],
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--quran-slm", default="../quran-slm")
    parser.add_argument("--quran-roots", default="../quran-roots")
    parser.add_argument("--output-dir", default="network/slm_local/output")
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--skip-n", type=int, default=1)
    return parser.parse_args()


def main() -> None:
    print(json.dumps(build(parse_args()), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
