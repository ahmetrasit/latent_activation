#!/usr/bin/env python3
"""Consolidate v3 raw channel candidates into branch-preserving families."""

from __future__ import annotations

import argparse
import collections
import csv
import json
import math
from pathlib import Path
from typing import Any


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")))
            handle.write("\n")


def write_json_atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp")
    tmp_path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    tmp_path.replace(path)


def weighted_jaccard(left: set[str], right: set[str], weights: dict[str, float]) -> float:
    if not left and not right:
        return 0.0
    union = left | right
    intersection = left & right
    denom = math.fsum(weights.get(item, 1.0) for item in sorted(union))
    numer = math.fsum(weights.get(item, 1.0) for item in sorted(intersection))
    return numer / denom if denom else 0.0


def weighted_containment(left: set[str], right: set[str], weights: dict[str, float]) -> float:
    left_weight = math.fsum(weights.get(item, 1.0) for item in sorted(left))
    right_weight = math.fsum(weights.get(item, 1.0) for item in sorted(right))
    smaller = left if left_weight <= right_weight else right
    denom = min(left_weight, right_weight)
    numer = math.fsum(weights.get(item, 1.0) for item in sorted(left & right))
    return numer / denom if denom else 0.0


def cosine(left: list[float], right: list[float]) -> float:
    dot = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(a * a for a in left))
    right_norm = math.sqrt(sum(b * b for b in right))
    return dot / (left_norm * right_norm) if left_norm and right_norm else 0.0


def idf_weights(feature_sets: list[set[str]]) -> dict[str, float]:
    count = len(feature_sets)
    df: collections.Counter[str] = collections.Counter()
    for features in feature_sets:
        df.update(features)
    return {feature: math.log((1 + count) / (1 + freq)) + 1.0 for feature, freq in df.items()}


def candidate_features(candidate: dict[str, Any], windows: list[dict[str, int]]) -> dict[str, Any]:
    branches = {branch["node_id"] for branch in candidate["branches"]}
    roots = set(candidate["roots"])
    ayahs = {int(ayah) for ayah in candidate["ayahs"]}
    root_ayah = {
        f"{branch['root']}@{ayah}"
        for branch in candidate["branches"]
        for ayah in branch.get("ayahs", [])
    }
    edges = {edge["edge_key"] for edge in candidate.get("branch_edges", [])}
    edge_mass_by_branch: collections.Counter[str] = collections.Counter()
    for edge in candidate.get("branch_edges", []):
        mass = float(edge.get("affinity", 0.0))
        edge_mass_by_branch[edge["left"]["node_id"]] += mass
        edge_mass_by_branch[edge["right"]["node_id"]] += mass
    window_profile = []
    for window in windows:
        lower = window["from"]
        upper = window["to"]
        window_profile.append(float(sum(1 for ayah in ayahs if lower <= ayah <= upper)))
    return {
        "candidate_id": candidate["candidate_id"],
        "branches": branches,
        "roots": roots,
        "ayahs": ayahs,
        "root_ayah": root_ayah,
        "edges": edges,
        "edge_mass_by_branch": dict(edge_mass_by_branch),
        "window_profile": window_profile,
    }


def build_windows(candidates: list[dict[str, Any]], *, window_size: int, window_step: int) -> list[dict[str, int]]:
    if window_size < 1:
        raise ValueError("window_size must be positive")
    if window_step < 1:
        raise ValueError("window_step must be positive")
    ayahs = sorted({int(ayah) for candidate in candidates for ayah in candidate["ayahs"]})
    if not ayahs:
        return []
    lower = min(ayahs)
    upper = max(ayahs)
    windows = []
    start = lower
    while start <= upper:
        end = min(upper, start + window_size - 1)
        windows.append({"window_id": f"W{len(windows)+1:03d}", "from": start, "to": end})
        if end == upper:
            break
        start += window_step
    return windows


def similarity(
    left: dict[str, Any],
    right: dict[str, Any],
    branch_weights: dict[str, float],
    edge_weights: dict[str, float],
    root_ayah_weights: dict[str, float],
) -> dict[str, float]:
    edge_j = weighted_jaccard(left["edges"], right["edges"], edge_weights)
    branch_j = weighted_jaccard(left["branches"], right["branches"], branch_weights)
    root_ayah_j = weighted_jaccard(left["root_ayah"], right["root_ayah"], root_ayah_weights)
    window_c = cosine(left["window_profile"], right["window_profile"])
    score = 0.50 * edge_j + 0.30 * branch_j + 0.10 * root_ayah_j + 0.10 * window_c
    branch_cont = weighted_containment(left["branches"], right["branches"], branch_weights)
    edge_cont = weighted_containment(left["edges"], right["edges"], edge_weights)
    return {
        "score": score,
        "edge_jaccard": edge_j,
        "branch_jaccard": branch_j,
        "root_ayah_jaccard": root_ayah_j,
        "window_cosine": window_c,
        "branch_containment": branch_cont,
        "edge_containment": edge_cont,
    }


def build_similarity_edges(
    features: list[dict[str, Any]],
    *,
    mutual_k: int,
    min_similarity: float,
    containment_similarity: float,
) -> list[dict[str, Any]]:
    branch_weights = idf_weights([row["branches"] for row in features])
    edge_weights = idf_weights([row["edges"] for row in features])
    root_ayah_weights = idf_weights([row["root_ayah"] for row in features])
    nearest: dict[str, list[tuple[float, str, dict[str, float]]]] = collections.defaultdict(list)

    for left_index, left in enumerate(features):
        for right in features[left_index + 1 :]:
            metrics = similarity(left, right, branch_weights, edge_weights, root_ayah_weights)
            if metrics["score"] <= 0.0 and metrics["branch_containment"] <= 0.0:
                continue
            nearest[left["candidate_id"]].append((metrics["score"], right["candidate_id"], metrics))
            nearest[right["candidate_id"]].append((metrics["score"], left["candidate_id"], metrics))

    top_neighbors: dict[str, set[str]] = {}
    for candidate_id, rows in nearest.items():
        rows.sort(key=lambda item: (-item[0], item[1]))
        top_neighbors[candidate_id] = {neighbor for _score, neighbor, _metrics in rows[:mutual_k]}

    edges = []
    seen = set()
    for candidate_id, rows in nearest.items():
        for score, neighbor, metrics in rows:
            key = tuple(sorted([candidate_id, neighbor]))
            if key in seen:
                continue
            seen.add(key)
            is_mutual = neighbor in top_neighbors.get(candidate_id, set()) and candidate_id in top_neighbors.get(neighbor, set())
            is_containment = (
                metrics["branch_containment"] >= containment_similarity
                and metrics["edge_containment"] >= 0.70
                and metrics["window_cosine"] >= 0.70
            )
            if not ((is_mutual and score >= min_similarity) or is_containment):
                continue
            edges.append(
                {
                    "left": key[0],
                    "right": key[1],
                    **{name: round(value, 6) for name, value in metrics.items()},
                    "edge_type": "mutual_knn" if is_mutual and score >= min_similarity else "containment",
                }
            )
    edges.sort(key=lambda row: (-row["score"], row["left"], row["right"]))
    return edges


def weighted_label_propagation(candidate_ids: list[str], edges: list[dict[str, Any]], *, rounds: int) -> dict[str, str]:
    graph: dict[str, list[tuple[str, float]]] = collections.defaultdict(list)
    for edge in edges:
        graph[edge["left"]].append((edge["right"], edge["score"]))
        graph[edge["right"]].append((edge["left"], edge["score"]))

    labels = {candidate_id: candidate_id for candidate_id in candidate_ids}
    for round_index in range(rounds):
        changed = False
        order = sorted(candidate_ids, reverse=bool(round_index % 2))
        for candidate_id in order:
            if not graph.get(candidate_id):
                continue
            label_scores: collections.Counter[str] = collections.Counter()
            for neighbor, weight in graph[candidate_id]:
                label_scores[labels[neighbor]] += weight
            best_label, best_score = max(label_scores.items(), key=lambda item: (item[1], -int(item[0][1:])))
            if best_score > 0 and labels[candidate_id] != best_label:
                labels[candidate_id] = best_label
                changed = True
        if not changed:
            break

    normalized = {}
    groups: dict[str, list[str]] = collections.defaultdict(list)
    for candidate_id, label in labels.items():
        groups[label].append(candidate_id)
    for members in groups.values():
        family_label = sorted(members)[0]
        for member in members:
            normalized[member] = family_label
    return normalized


def candidate_similarity_lookup(edges: list[dict[str, Any]]) -> dict[tuple[str, str], float]:
    return {tuple(sorted([edge["left"], edge["right"]])): float(edge["score"]) for edge in edges}


def pair_similarity(left: str, right: str, lookup: dict[tuple[str, str], float]) -> float:
    if left == right:
        return 1.0
    return lookup.get(tuple(sorted([left, right])), 0.0)


def family_structural_type(members: list[dict[str, Any]]) -> str:
    branch_counter: collections.Counter[str] = collections.Counter()
    root_counter: collections.Counter[str] = collections.Counter()
    edge_mass_by_root: collections.Counter[str] = collections.Counter()
    for candidate in members:
        for branch in candidate["branches"]:
            branch_counter[branch["node_id"]] += 1
            root_counter[branch["root"]] += 1
        for edge in candidate.get("branch_edges", []):
            mass = float(edge.get("affinity", 0.0))
            edge_mass_by_root[edge["left"]["root"]] += mass
            edge_mass_by_root[edge["right"]["root"]] += mass
    total_branches = sum(branch_counter.values())
    if not total_branches:
        return "distributed"
    top_root, top_count = root_counter.most_common(1)[0]
    if top_count / total_branches >= 0.40:
        return "root_centered"
    total_mass = sum(edge_mass_by_root.values())
    if total_mass and edge_mass_by_root[top_root] / total_mass >= 0.50:
        return "root_bridge"
    return "distributed"


def choose_representative(member_ids: list[str], candidates_by_id: dict[str, dict[str, Any]], lookup: dict[tuple[str, str], float]) -> str:
    best = None
    for candidate_id in member_ids:
        mean_similarity = sum(pair_similarity(candidate_id, other, lookup) for other in member_ids) / max(1, len(member_ids))
        score = 0.65 * mean_similarity + 0.35 * float(candidates_by_id[candidate_id].get("channel_score", 0.0))
        if best is None or (score, -int(candidate_id[1:])) > best:
            best = (score, -int(candidate_id[1:]), candidate_id)
    return best[2] if best else member_ids[0]


def family_record(
    family_index: int,
    member_ids: list[str],
    candidates_by_id: dict[str, dict[str, Any]],
    lookup: dict[tuple[str, str], float],
) -> dict[str, Any]:
    members = [candidates_by_id[candidate_id] for candidate_id in member_ids]
    member_count = len(members)
    branch_counter: collections.Counter[str] = collections.Counter()
    edge_counter: collections.Counter[str] = collections.Counter()
    facet_counter: collections.Counter[str] = collections.Counter()
    branch_rows: dict[str, dict[str, Any]] = {}
    edge_rows: dict[str, dict[str, Any]] = {}
    ayahs = set()
    roots = set()

    for candidate in members:
        ayahs.update(int(ayah) for ayah in candidate["ayahs"])
        roots.update(candidate["roots"])
        for branch in candidate["branches"]:
            branch_counter[branch["node_id"]] += 1
            branch_rows[branch["node_id"]] = branch
        for edge in candidate.get("branch_edges", []):
            edge_counter[edge["edge_key"]] += 1
            edge_rows[edge["edge_key"]] = edge
        for facet, score in candidate.get("top_facets", []):
            facet_counter[facet] += float(score)

    core_branches = [branch_rows[node_id] for node_id, count in branch_counter.items() if count / member_count >= 0.60]
    optional_branches = [
        branch_rows[node_id]
        for node_id, count in branch_counter.items()
        if 0.20 <= count / member_count < 0.60
    ]
    rare_branches = [branch_rows[node_id] for node_id, count in branch_counter.items() if count / member_count < 0.20]
    core_edges = [edge_rows[edge_key] for edge_key, count in edge_counter.items() if count / member_count >= 0.50]
    representative_id = choose_representative(member_ids, candidates_by_id, lookup)
    representative = candidates_by_id[representative_id]
    pair_scores = [
        pair_similarity(left, right, lookup)
        for left_index, left in enumerate(member_ids)
        for right in member_ids[left_index + 1 :]
    ]

    variant_ids = []
    representative_branches = {branch["node_id"] for branch in representative["branches"]}
    for candidate in members:
        candidate_branches = {branch["node_id"] for branch in candidate["branches"]}
        unique = candidate_branches - representative_branches
        if not unique:
            continue
        total_mass = sum(float(edge.get("affinity", 0.0)) for edge in candidate.get("branch_edges", []))
        unique_mass = 0.0
        for edge in candidate.get("branch_edges", []):
            if edge["left"]["node_id"] in unique or edge["right"]["node_id"] in unique:
                unique_mass += float(edge.get("affinity", 0.0))
        if total_mass and unique_mass / total_mass >= 0.10:
            variant_ids.append(candidate["candidate_id"])

    cohesion = sum(pair_scores) / max(1, len(pair_scores))
    edge_reliability = sum(float(candidate.get("reciprocal_edge_ratio", 0.0)) for candidate in members) / member_count
    strong_reliability = sum(float(candidate.get("strong_rank_ratio", 0.0)) for candidate in members) / member_count
    ablation = sum(float(candidate.get("root_ablation_min_survival", 0.0)) for candidate in members) / member_count
    family_stability = min(1.0, len(core_branches) / max(1, len(branch_counter)))
    ayah_span = max(ayahs) - min(ayahs) + 1 if ayahs else 1
    passage_locality = len(ayahs) / ayah_span
    base_score = (
        0.30 * cohesion
        + 0.20 * ((edge_reliability + strong_reliability) / 2)
        + 0.15 * ablation
        + 0.15 * family_stability
        + 0.10 * passage_locality
        + 0.10 * min(1.0, len(variant_ids) / max(1, member_count))
    )

    top_facets = [(facet, round(score, 4)) for facet, score in facet_counter.most_common(12)]
    label_terms = [facet.split(":", 1)[-1] for facet, _score in top_facets[:4]]
    label_hint = " / ".join(label_terms) if label_terms else representative.get("label_hint", "")

    return {
        "family_id": f"F{family_index:03d}",
        "label_hint": label_hint,
        "family_score_raw": round(base_score, 4),
        "member_count": member_count,
        "representative_candidate_id": representative_id,
        "variant_candidate_ids": sorted(set(variant_ids)),
        "candidate_ids": sorted(member_ids),
        "structural_type": family_structural_type(members),
        "ayahs": sorted(ayahs),
        "roots": sorted(roots),
        "root_count": len(roots),
        "branch_count": len(branch_counter),
        "core_branch_count": len(core_branches),
        "optional_branch_count": len(optional_branches),
        "rare_branch_count": len(rare_branches),
        "core_edge_count": len(core_edges),
        "cohesion": round(cohesion, 4),
        "edge_reliability": round(edge_reliability, 4),
        "strong_rank_reliability": round(strong_reliability, 4),
        "ablation_robustness": round(ablation, 4),
        "family_stability": round(family_stability, 4),
        "passage_locality": round(passage_locality, 4),
        "top_facets": top_facets,
        "core_branches": sorted(core_branches, key=lambda row: (row["root"], row["branch_id"], row["node_id"])),
        "optional_branches": sorted(optional_branches, key=lambda row: (row["root"], row["branch_id"], row["node_id"])),
        "rare_branches": sorted(rare_branches, key=lambda row: (row["root"], row["branch_id"], row["node_id"])),
        "core_edges": core_edges,
    }


def add_novelty_scores(families: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selected_branch_sets: list[set[str]] = []
    scored = []
    for family in sorted(families, key=lambda row: (-row["family_score_raw"], row["family_id"])):
        branch_set = {branch["node_id"] for branch in family["core_branches"] + family["optional_branches"] + family["rare_branches"]}
        max_similarity = 0.0
        for selected in selected_branch_sets:
            if branch_set or selected:
                max_similarity = max(max_similarity, len(branch_set & selected) / len(branch_set | selected))
        novelty = 1.0 - max_similarity
        final_score = 0.80 * family["family_score_raw"] + 0.20 * novelty
        scored.append(
            {
                **family,
                "novelty": round(novelty, 4),
                "family_score": round(final_score, 4),
            }
        )
        selected_branch_sets.append(branch_set)
    scored.sort(key=lambda row: (-row["family_score"], row["family_id"]))
    return [{**row, "family_id": f"F{index:03d}"} for index, row in enumerate(scored, start=1)]


def write_similarity_tsv(path: Path, edges: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            delimiter="\t",
            lineterminator="\n",
            fieldnames=[
                "left",
                "right",
                "score",
                "edge_jaccard",
                "branch_jaccard",
                "root_ayah_jaccard",
                "window_cosine",
                "branch_containment",
                "edge_containment",
                "edge_type",
            ],
        )
        writer.writeheader()
        writer.writerows(edges)


def write_membership_tsv(path: Path, families: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["candidate_id", "family_id", "representative_candidate_id", "membership"])
        for family in families:
            for candidate_id in family["candidate_ids"]:
                membership = "representative" if candidate_id == family["representative_candidate_id"] else "variant" if candidate_id in family["variant_candidate_ids"] else "member"
                writer.writerow([candidate_id, family["family_id"], family["representative_candidate_id"], membership])


def write_branch_inventory_tsv(path: Path, families: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["family_id", "branch_status", "node_id", "root", "branch_id", "ayahs", "image_ar"])
        for family in families:
            for status in ["core_branches", "optional_branches", "rare_branches"]:
                branch_status = status.replace("_branches", "")
                for branch in family[status]:
                    writer.writerow(
                        [
                            family["family_id"],
                            branch_status,
                            branch["node_id"],
                            branch["root"],
                            branch["branch_id"],
                            ",".join(map(str, branch.get("ayahs", []))),
                            branch.get("image_ar", ""),
                        ]
                    )


def write_review_queue_tsv(path: Path, families: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "rank",
                "family_id",
                "family_score",
                "label_hint",
                "structural_type",
                "member_count",
                "variant_count",
                "ayah_count",
                "root_count",
                "branch_count",
                "core_branch_count",
                "ayahs",
                "top_facets",
                "representative_candidate_id",
            ]
        )
        for rank, family in enumerate(families, start=1):
            writer.writerow(
                [
                    rank,
                    family["family_id"],
                    family["family_score"],
                    family["label_hint"],
                    family["structural_type"],
                    family["member_count"],
                    len(family["variant_candidate_ids"]),
                    len(family["ayahs"]),
                    family["root_count"],
                    family["branch_count"],
                    family["core_branch_count"],
                    ",".join(map(str, family["ayahs"])),
                    "; ".join(f"{facet}({score})" for facet, score in family["top_facets"][:8]),
                    family["representative_candidate_id"],
                ]
            )


def write_candidate_graphs(path: Path, candidates: list[dict[str, Any]]) -> None:
    rows = []
    for candidate in candidates:
        rows.append(
            {
                "candidate_id": candidate["candidate_id"],
                "seed_provenance": candidate.get("seed_provenance"),
                "branch_nodes": candidate["branches"],
                "branch_edges": candidate.get("branch_edges", []),
                "ayahs": candidate["ayahs"],
                "roots": candidate["roots"],
            }
        )
    write_jsonl(path, rows)


def build(args: argparse.Namespace) -> dict[str, Any]:
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir) if args.output_dir else input_dir / "families"
    output_dir.mkdir(parents=True, exist_ok=True)
    candidates = read_jsonl(input_dir / "channel_candidates.jsonl")
    windows = build_windows(candidates, window_size=args.window_size, window_step=args.window_step)
    features = [candidate_features(candidate, windows) for candidate in candidates]
    edges = build_similarity_edges(
        features,
        mutual_k=args.mutual_k,
        min_similarity=args.min_similarity,
        containment_similarity=args.containment_similarity,
    )
    labels = weighted_label_propagation([row["candidate_id"] for row in features], edges, rounds=args.label_rounds)

    family_members: dict[str, list[str]] = collections.defaultdict(list)
    for candidate_id, label in labels.items():
        family_members[label].append(candidate_id)

    candidates_by_id = {candidate["candidate_id"]: candidate for candidate in candidates}
    lookup = candidate_similarity_lookup(edges)
    family_rows = []
    for index, (_label, member_ids) in enumerate(
        sorted(family_members.items(), key=lambda item: (-len(item[1]), sorted(item[1])[0])),
        start=1,
    ):
        family_rows.append(family_record(index, sorted(member_ids), candidates_by_id, lookup))
    families = add_novelty_scores(family_rows)

    write_candidate_graphs(output_dir / "candidate_graphs.jsonl", candidates)
    write_similarity_tsv(output_dir / "candidate_similarity_edges.tsv", edges)
    write_jsonl(output_dir / "channel_families.jsonl", families)
    write_membership_tsv(output_dir / "candidate_family_membership.tsv", families)
    write_branch_inventory_tsv(output_dir / "family_branch_inventory.tsv", families)
    write_review_queue_tsv(output_dir / "review_queue.tsv", families)
    write_json_atomic(output_dir / "passage_windows.json", windows)

    size_counts = collections.Counter(
        "singleton" if family["member_count"] == 1 else "small_2_4" if family["member_count"] <= 4 else "medium_5_14" if family["member_count"] <= 14 else "large_15_plus"
        for family in families
    )
    type_counts = collections.Counter(family["structural_type"] for family in families)
    summary = {
        "version": "v3_branch_preserving_family_consolidation_v0",
        "input_dir": str(input_dir),
        "output_dir": str(output_dir),
        "parameters": {
            "mutual_k": args.mutual_k,
            "min_similarity": args.min_similarity,
            "containment_similarity": args.containment_similarity,
            "label_rounds": args.label_rounds,
            "window_size": args.window_size,
            "window_step": args.window_step,
            "no_hard_output_target": True,
        },
        "counts": {
            "candidates": len(candidates),
            "similarity_edges": len(edges),
            "families": len(families),
            "family_size_buckets": dict(size_counts),
            "structural_type_counts": dict(type_counts),
        },
        "top_families": [
            {
                "family_id": family["family_id"],
                "family_score": family["family_score"],
                "label_hint": family["label_hint"],
                "member_count": family["member_count"],
                "structural_type": family["structural_type"],
                "ayah_count": len(family["ayahs"]),
                "root_count": family["root_count"],
                "branch_count": family["branch_count"],
            }
            for family in families[:30]
        ],
    }
    write_json_atomic(output_dir / "consolidation_summary.json", summary)
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir")
    parser.add_argument("--mutual-k", type=int, default=8)
    parser.add_argument("--min-similarity", type=float, default=0.20)
    parser.add_argument("--containment-similarity", type=float, default=0.75)
    parser.add_argument("--label-rounds", type=int, default=40)
    parser.add_argument("--window-size", type=int, default=5)
    parser.add_argument("--window-step", type=int, default=3)
    return parser.parse_args()


def main() -> None:
    print(json.dumps(build(parse_args()), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
