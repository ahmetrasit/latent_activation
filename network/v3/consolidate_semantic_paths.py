#!/usr/bin/env python3
"""Consolidate overlapping sparse semantic paths into reviewable channel hypotheses."""

from __future__ import annotations

import argparse
import collections
import csv
import json
from pathlib import Path
from typing import Any

from consolidate_channel_families import idf_weights, weighted_jaccard, weighted_label_propagation
from discover_surah_channels import write_jsonl


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def features(path: dict[str, Any]) -> dict[str, set[str]]:
    return {
        "branches": {branch["node_id"] for branch in path["branches"]},
        "edges": {edge["edge_key"] for edge in path["tree_edges"]},
        "roots": set(path["roots"]),
        "ayahs": {str(ayah) for ayah in path["ayahs"]},
    }


def containment(left: set[str], right: set[str]) -> float:
    return len(left & right) / min(len(left), len(right)) if left and right else 0.0


def build_similarity_edges(
    paths: list[dict[str, Any]],
    *,
    mutual_k: int,
    min_similarity: float,
    containment_threshold: float,
) -> list[dict[str, Any]]:
    by_id = {path["path_id"]: features(path) for path in paths}
    branch_weights = idf_weights([row["branches"] for row in by_id.values()])
    edge_weights = idf_weights([row["edges"] for row in by_id.values()])
    root_weights = idf_weights([row["roots"] for row in by_id.values()])
    postings: dict[str, list[str]] = collections.defaultdict(list)
    for path_id, row in by_id.items():
        for branch in row["branches"]:
            postings[branch].append(path_id)

    possible_pairs: set[tuple[str, str]] = set()
    for path_ids in postings.values():
        for left_index, left in enumerate(path_ids):
            for right in path_ids[left_index + 1 :]:
                possible_pairs.add(tuple(sorted((left, right))))

    nearest: dict[str, list[tuple[float, str, dict[str, float]]]] = collections.defaultdict(list)
    for left_id, right_id in possible_pairs:
        left = by_id[left_id]
        right = by_id[right_id]
        edge_j = weighted_jaccard(left["edges"], right["edges"], edge_weights)
        branch_j = weighted_jaccard(left["branches"], right["branches"], branch_weights)
        root_j = weighted_jaccard(left["roots"], right["roots"], root_weights)
        ayah_j = len(left["ayahs"] & right["ayahs"]) / len(left["ayahs"] | right["ayahs"])
        score = 0.45 * edge_j + 0.35 * branch_j + 0.10 * root_j + 0.10 * ayah_j
        metrics = {
            "score": score,
            "edge_jaccard": edge_j,
            "branch_jaccard": branch_j,
            "root_jaccard": root_j,
            "ayah_jaccard": ayah_j,
            "branch_containment": containment(left["branches"], right["branches"]),
            "edge_containment": containment(left["edges"], right["edges"]),
        }
        nearest[left_id].append((score, right_id, metrics))
        nearest[right_id].append((score, left_id, metrics))

    top_neighbors = {}
    for path_id, rows in nearest.items():
        rows.sort(key=lambda item: (-item[0], item[1]))
        top_neighbors[path_id] = {neighbor for _score, neighbor, _metrics in rows[:mutual_k]}

    edges = []
    seen = set()
    for left_id, rows in nearest.items():
        for score, right_id, metrics in rows:
            key = tuple(sorted((left_id, right_id)))
            if key in seen:
                continue
            seen.add(key)
            mutual = right_id in top_neighbors.get(left_id, set()) and left_id in top_neighbors.get(right_id, set())
            contained = (
                metrics["branch_containment"] >= containment_threshold
                and metrics["edge_containment"] >= 0.45
                and metrics["root_jaccard"] >= 0.55
            )
            if not ((mutual and score >= min_similarity) or contained):
                continue
            edges.append({
                "left": key[0],
                "right": key[1],
                **{name: round(value, 6) for name, value in metrics.items()},
                "edge_type": "mutual_knn" if mutual and score >= min_similarity else "containment",
            })
    edges.sort(key=lambda row: (-row["score"], row["left"], row["right"]))
    return edges


def representative(member_ids: list[str], paths_by_id: dict[str, dict[str, Any]], graph: dict[str, list[tuple[str, float]]]) -> str:
    return max(
        member_ids,
        key=lambda path_id: (
            sum(weight for neighbor, weight in graph.get(path_id, []) if neighbor in member_ids),
            paths_by_id[path_id]["path_score"],
            -int(path_id[1:]),
        ),
    )


def family_record(index: int, member_ids: list[str], paths_by_id: dict[str, dict[str, Any]], graph: dict[str, list[tuple[str, float]]]) -> dict[str, Any]:
    members = [paths_by_id[path_id] for path_id in member_ids]
    count = len(members)
    branch_counter: collections.Counter[str] = collections.Counter()
    edge_counter: collections.Counter[str] = collections.Counter()
    facet_counter: collections.Counter[str] = collections.Counter()
    branch_rows = {}
    edge_rows = {}
    ayahs = set()
    roots = set()
    for path in members:
        ayahs.update(path["ayahs"])
        roots.update(path["roots"])
        for branch in path["branches"]:
            branch_counter[branch["node_id"]] += 1
            branch_rows[branch["node_id"]] = branch
        for edge in path["tree_edges"]:
            edge_counter[edge["edge_key"]] += 1
            edge_rows[edge["edge_key"]] = edge
        for facet, score in path.get("top_facets", []):
            facet_counter[facet] += float(score)

    core = [branch_rows[node_id] for node_id, hits in branch_counter.items() if hits / count >= 0.50]
    optional = [branch_rows[node_id] for node_id, hits in branch_counter.items() if 0.15 <= hits / count < 0.50]
    alternatives: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for node_id, hits in branch_counter.items():
        branch = branch_rows[node_id]
        alternatives[branch["root"]].append({
            **branch,
            "path_support": hits,
            "support_ratio": round(hits / count, 4),
        })
    for root in alternatives:
        alternatives[root].sort(key=lambda row: (-row["path_support"], row["branch_id"], row["node_id"]))

    representative_id = representative(member_ids, paths_by_id, graph)
    construction_ids = [representative_id]
    covered_branches = {branch["node_id"] for branch in paths_by_id[representative_id]["branches"]}
    while len(construction_ids) < 4:
        choices = []
        for path_id in member_ids:
            if path_id in construction_ids:
                continue
            path_branches = {branch["node_id"] for branch in paths_by_id[path_id]["branches"]}
            new_count = len(path_branches - covered_branches)
            if new_count:
                choices.append((new_count, float(paths_by_id[path_id]["path_score"]), -int(path_id[1:]), path_id))
        if not choices:
            break
        selected = max(choices)[-1]
        construction_ids.append(selected)
        covered_branches.update(branch["node_id"] for branch in paths_by_id[selected]["branches"])
    internal_weights = [
        weight
        for left in member_ids
        for right, weight in graph.get(left, [])
        if right in member_ids and left < right
    ]
    cohesion = sum(internal_weights) / max(1, len(internal_weights))
    mean_path_score = sum(float(path["path_score"]) for path in members) / count
    stable_branch_ratio = len(core) / max(1, len(branch_counter))
    family_score = 0.45 * mean_path_score + 0.35 * cohesion + 0.20 * stable_branch_ratio
    top_facets = [(facet, round(score, 4)) for facet, score in facet_counter.most_common(16)]
    label = " / ".join(facet.split(":", 1)[-1] for facet, _score in top_facets[:4])
    return {
        "path_family_id": f"PF{index:04d}",
        "label_hint": label or paths_by_id[representative_id]["label_hint"],
        "family_score": round(family_score, 4),
        "member_count": count,
        "representative_path_id": representative_id,
        "construction_paths": [
            {
                "path_id": path_id,
                "path_score": paths_by_id[path_id]["path_score"],
                "branches": paths_by_id[path_id]["branches"],
                "tree_edges": paths_by_id[path_id]["tree_edges"],
            }
            for path_id in construction_ids
        ],
        "path_ids": sorted(member_ids),
        "ayahs": sorted(ayahs),
        "roots": sorted(roots),
        "root_count": len(roots),
        "branch_count": len(branch_counter),
        "core_branches": sorted(core, key=lambda row: (row["root"], row["branch_id"])),
        "optional_branches": sorted(optional, key=lambda row: (row["root"], row["branch_id"])),
        "branch_alternatives_by_root": dict(sorted(alternatives.items())),
        "core_edges": [edge_rows[key] for key, hits in edge_counter.items() if hits / count >= 0.40],
        "cohesion": round(cohesion, 4),
        "mean_path_score": round(mean_path_score, 4),
        "top_facets": top_facets,
    }


def write_edges(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = ["left", "right", "score", "edge_jaccard", "branch_jaccard", "root_jaccard", "ayah_jaccard", "branch_containment", "edge_containment", "edge_type"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", lineterminator="\n", fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_review(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["rank", "path_family_id", "family_score", "label_hint", "members", "ayahs", "roots", "core_branches", "optional_branches", "representative_path_id", "construction_paths"])
        for rank, row in enumerate(rows, start=1):
            render = lambda branches: " | ".join(
                f"{branch['root']}:{branch['branch_id']}@{','.join(map(str, branch.get('ayahs', [])))}:{branch['image_ar']}"
                for branch in branches
            )
            constructions = []
            for construction in row["construction_paths"]:
                edges = " ; ".join(
                    f"{edge['left']['root']}:{edge['left']['branch_id']}→{edge['right']['root']}:{edge['right']['branch_id']}"
                    for edge in construction["tree_edges"]
                )
                constructions.append(f"{construction['path_id']}[{edges}]")
            writer.writerow([
                rank, row["path_family_id"], row["family_score"], row["label_hint"], row["member_count"],
                ",".join(map(str, row["ayahs"])), " ".join(row["roots"]), render(row["core_branches"]),
                render(row["optional_branches"]), row["representative_path_id"], " | ".join(constructions),
            ])


def build(args: argparse.Namespace) -> dict[str, Any]:
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir) if args.output_dir else input_dir / "path_families"
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = read_jsonl(input_dir / "semantic_path_candidates.jsonl")
    edges = build_similarity_edges(
        paths,
        mutual_k=args.mutual_k,
        min_similarity=args.min_similarity,
        containment_threshold=args.containment_threshold,
    )
    labels = weighted_label_propagation([path["path_id"] for path in paths], edges, rounds=args.label_rounds)
    members: dict[str, list[str]] = collections.defaultdict(list)
    for path_id, label in labels.items():
        members[label].append(path_id)
    graph: dict[str, list[tuple[str, float]]] = collections.defaultdict(list)
    for edge in edges:
        graph[edge["left"]].append((edge["right"], float(edge["score"])))
        graph[edge["right"]].append((edge["left"], float(edge["score"])))
    paths_by_id = {path["path_id"]: path for path in paths}
    families = [
        family_record(index, sorted(member_ids), paths_by_id, graph)
        for index, (_label, member_ids) in enumerate(sorted(members.items(), key=lambda item: (-len(item[1]), min(item[1]))), start=1)
    ]
    families.sort(key=lambda row: (-row["family_score"], row["path_family_id"]))
    families = [{**row, "path_family_id": f"PF{index:04d}"} for index, row in enumerate(families, start=1)]
    write_jsonl(output_dir / "semantic_path_families.jsonl", families)
    write_edges(output_dir / "path_similarity_edges.tsv", edges)
    write_review(output_dir / "path_family_review_queue.tsv", families)
    summary = {
        "version": "v3_sparse_semantic_path_consolidation_v0",
        "parameters": {
            "mutual_k": args.mutual_k,
            "min_similarity": args.min_similarity,
            "containment_threshold": args.containment_threshold,
            "label_rounds": args.label_rounds,
        },
        "counts": {"paths": len(paths), "similarity_edges": len(edges), "path_families": len(families)},
        "top_families": [
            {key: row[key] for key in ["path_family_id", "family_score", "label_hint", "member_count", "roots"]}
            for row in families[:30]
        ],
    }
    (output_dir / "path_family_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir")
    parser.add_argument("--mutual-k", type=int, default=10)
    parser.add_argument("--min-similarity", type=float, default=0.16)
    parser.add_argument("--containment-threshold", type=float, default=0.65)
    parser.add_argument("--label-rounds", type=int, default=40)
    return parser.parse_args()


def main() -> None:
    print(json.dumps(build(parse_args()), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
