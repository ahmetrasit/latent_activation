#!/usr/bin/env python3
"""Consolidate overlapping sparse semantic paths into reviewable channel hypotheses."""

from __future__ import annotations

import argparse
import bisect
import collections
import csv
import heapq
import json
import math
from array import array
from pathlib import Path
from typing import Any, NamedTuple

from consolidate_channel_families import idf_weights, weighted_label_propagation
from discover_surah_channels import write_jsonl


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_json_atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp")
    tmp_path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    tmp_path.replace(path)


def path_sort_key(path_id: str) -> tuple[int, str]:
    suffix = path_id[1:] if path_id.startswith("P") else path_id
    try:
        return int(suffix), path_id
    except ValueError:
        return 10**12, path_id


def features(path: dict[str, Any]) -> dict[str, set[str]]:
    return {
        "branches": {branch["node_id"] for branch in path["branches"]},
        "edges": {edge["edge_key"] for edge in path["tree_edges"]},
        "roots": set(path["roots"]),
        "ayahs": {str(ayah) for ayah in path["ayahs"]},
    }


class PathFeatures(NamedTuple):
    path_id: str
    branches: frozenset[str]
    edges: frozenset[str]
    roots: frozenset[str]
    ayahs: frozenset[str]
    path_score: float
    source_offset: int


def compact_features(
    path: dict[str, Any],
    pools: dict[str, dict[str, str]],
    *,
    source_offset: int = 0,
) -> PathFeatures:
    def intern_all(kind: str, values: set[str]) -> frozenset[str]:
        pool = pools[kind]
        return frozenset(pool.setdefault(value, value) for value in values)

    row = features(path)
    return PathFeatures(
        path_id=str(path["path_id"]),
        branches=intern_all("branches", row["branches"]),
        edges=intern_all("edges", row["edges"]),
        roots=intern_all("roots", row["roots"]),
        ayahs=intern_all("ayahs", row["ayahs"]),
        path_score=float(path["path_score"]),
        source_offset=source_offset,
    )


def index_jsonl(path: Path) -> tuple[list[PathFeatures], dict[str, array]]:
    indexed: list[PathFeatures] = []
    postings: dict[str, array] = collections.defaultdict(lambda: array("I"))
    pools: dict[str, dict[str, str]] = {
        "branches": {},
        "edges": {},
        "roots": {},
        "ayahs": {},
    }
    seen_ids: set[str] = set()
    with path.open("rb") as handle:
        line_number = 0
        while True:
            source_offset = handle.tell()
            line = handle.readline()
            if not line:
                break
            line_number += 1
            if not line.strip():
                continue
            row = compact_features(
                json.loads(line), pools, source_offset=source_offset
            )
            if row.path_id in seen_ids:
                raise ValueError(f"duplicate path_id {row.path_id!r} at line {line_number}")
            seen_ids.add(row.path_id)
            index = len(indexed)
            indexed.append(row)
            for kind, values in (
                ("branch", row.branches),
                ("edge", row.edges),
                ("root", row.roots),
                ("ayah", row.ayahs),
            ):
                for value in values:
                    postings[f"{kind}:{value}"].append(index)
    return indexed, dict(postings)


def containment(left: set[str], right: set[str]) -> float:
    return len(left & right) / min(len(left), len(right)) if left and right else 0.0


def stable_weighted_jaccard(
    left: frozenset[str], right: frozenset[str], weights: dict[str, float]
) -> float:
    """Return a hash-seed-independent weighted Jaccard score."""
    union = left | right
    if not union:
        return 0.0
    denominator = math.fsum(weights.get(item, 1.0) for item in sorted(union))
    numerator = math.fsum(
        weights.get(item, 1.0) for item in sorted(left & right)
    )
    return numerator / denominator if denominator else 0.0


def build_similarity_edges(
    paths: list[dict[str, Any]],
    *,
    mutual_k: int,
    min_similarity: float,
    containment_threshold: float,
) -> list[dict[str, Any]]:
    pools = {kind: {} for kind in ("branches", "edges", "roots", "ayahs")}
    indexed = [compact_features(path, pools) for path in paths]
    postings: dict[str, array] = collections.defaultdict(lambda: array("I"))
    for index, row in enumerate(indexed):
        for kind, values in (
            ("branch", row.branches),
            ("edge", row.edges),
            ("root", row.roots),
            ("ayah", row.ayahs),
        ):
            for value in values:
                postings[f"{kind}:{value}"].append(index)
    return build_similarity_edges_indexed(
        indexed,
        dict(postings),
        mutual_k=mutual_k,
        min_similarity=min_similarity,
        containment_threshold=containment_threshold,
    )


def pair_metrics(
    left: PathFeatures,
    right: PathFeatures,
    branch_weights: dict[str, float],
    edge_weights: dict[str, float],
    root_weights: dict[str, float],
) -> dict[str, float]:
    edge_j = stable_weighted_jaccard(left.edges, right.edges, edge_weights)
    branch_j = stable_weighted_jaccard(left.branches, right.branches, branch_weights)
    root_j = stable_weighted_jaccard(left.roots, right.roots, root_weights)
    ayah_union = left.ayahs | right.ayahs
    ayah_j = len(left.ayahs & right.ayahs) / len(ayah_union) if ayah_union else 0.0
    score = 0.45 * edge_j + 0.35 * branch_j + 0.10 * root_j + 0.10 * ayah_j
    return {
        "score": score,
        "edge_jaccard": edge_j,
        "branch_jaccard": branch_j,
        "root_jaccard": root_j,
        "ayah_jaccard": ayah_j,
        "branch_containment": containment(left.branches, right.branches),
        "edge_containment": containment(left.edges, right.edges),
    }


def edge_record_from_metrics(
    left: PathFeatures,
    right: PathFeatures,
    metrics: dict[str, float],
    edge_type: str,
) -> dict[str, Any]:
    left_id, right_id = sorted((left.path_id, right.path_id), key=path_sort_key)
    return {
        "left": left_id,
        "right": right_id,
        **{name: round(value, 6) for name, value in metrics.items()},
        "edge_type": edge_type,
    }


def build_similarity_edges_indexed(
    indexed: list[PathFeatures],
    postings: dict[str, array],
    *,
    mutual_k: int,
    min_similarity: float,
    containment_threshold: float,
) -> list[dict[str, Any]]:
    """Build exact mutual-kNN edges without materializing every possible pair."""
    if mutual_k < 0:
        raise ValueError("mutual_k must be non-negative")
    branch_weights = idf_weights([row.branches for row in indexed])
    edge_weights = idf_weights([row.edges for row in indexed])
    root_weights = idf_weights([row.roots for row in indexed])
    lexical_rank = {
        path_id: rank
        for rank, path_id in enumerate(
            sorted((row.path_id for row in indexed), key=path_sort_key)
        )
    }
    nearest: list[list[tuple[float, int, int]]] = [[] for _row in indexed]
    contained_edges: dict[tuple[int, int], dict[str, Any]] = {}

    def offer(owner: int, neighbor: int, score: float) -> None:
        if mutual_k == 0:
            return
        quality = (score, -lexical_rank[indexed[neighbor].path_id], neighbor)
        heap = nearest[owner]
        if len(heap) < mutual_k:
            heapq.heappush(heap, quality)
        elif quality[:2] > heap[0][:2]:
            heapq.heapreplace(heap, quality)

    for left_index, left in enumerate(indexed):
        candidates: set[int] = set()
        for kind, values in (
            ("branch", left.branches),
            ("edge", left.edges),
            ("root", left.roots),
            ("ayah", left.ayahs),
        ):
            for value in values:
                feature_postings = postings[f"{kind}:{value}"]
                start = bisect.bisect_right(feature_postings, left_index)
                candidates.update(feature_postings[start:])
        for right_index in candidates:
            right = indexed[right_index]
            metrics = pair_metrics(left, right, branch_weights, edge_weights, root_weights)
            score = metrics["score"]
            offer(left_index, right_index, score)
            offer(right_index, left_index, score)
            if (
                metrics["branch_containment"] >= containment_threshold
                and metrics["edge_containment"] >= 0.45
                and metrics["root_jaccard"] >= 0.55
            ):
                contained_edges[(left_index, right_index)] = edge_record_from_metrics(
                    left, right, metrics, "containment"
                )

    top_neighbors = [{item[2] for item in heap} for heap in nearest]
    edges_by_pair = contained_edges
    for left_index, neighbors in enumerate(top_neighbors):
        for right_index in neighbors:
            if right_index <= left_index or left_index not in top_neighbors[right_index]:
                continue
            left = indexed[left_index]
            right = indexed[right_index]
            metrics = pair_metrics(left, right, branch_weights, edge_weights, root_weights)
            if metrics["score"] >= min_similarity:
                edges_by_pair[(left_index, right_index)] = edge_record_from_metrics(
                    left, right, metrics, "mutual_knn"
                )

    edges = list(edges_by_pair.values())
    edges.sort(
        key=lambda row: (
            -row["score"],
            path_sort_key(row["left"]),
            path_sort_key(row["right"]),
        )
    )
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
        "path_ids": sorted(member_ids, key=path_sort_key),
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


def plan_families(
    indexed: list[PathFeatures],
    labels: dict[str, str],
    edges: list[dict[str, Any]],
) -> tuple[list[str], dict[str, dict[str, Any]]]:
    by_id = {row.path_id: row for row in indexed}
    members: dict[str, list[str]] = collections.defaultdict(list)
    for row in indexed:
        members[labels[row.path_id]].append(row.path_id)
    graph: dict[str, list[tuple[str, float]]] = collections.defaultdict(list)
    for edge in edges:
        graph[edge["left"]].append((edge["right"], float(edge["score"])))
        graph[edge["right"]].append((edge["left"], float(edge["score"])))

    ordered_labels = [
        label
        for label, _member_ids in sorted(
            members.items(),
            key=lambda item: (
                -len(item[1]),
                min(path_sort_key(path_id) for path_id in item[1]),
            ),
        )
    ]
    plans: dict[str, dict[str, Any]] = {}
    for index, label in enumerate(ordered_labels, start=1):
        member_ids = sorted(members[label], key=path_sort_key)
        member_set = set(member_ids)
        representative_id = max(
            member_ids,
            key=lambda path_id: (
                sum(
                    weight
                    for neighbor, weight in graph.get(path_id, [])
                    if neighbor in member_set
                ),
                by_id[path_id].path_score,
                -int(path_id[1:]),
            ),
        )
        construction_ids = [representative_id]
        covered_branches = set(by_id[representative_id].branches)
        while len(construction_ids) < 4:
            choices = []
            for path_id in member_ids:
                if path_id in construction_ids:
                    continue
                new_count = len(by_id[path_id].branches - covered_branches)
                if new_count:
                    choices.append(
                        (new_count, by_id[path_id].path_score, -int(path_id[1:]), path_id)
                    )
            if not choices:
                break
            selected = max(choices)[-1]
            construction_ids.append(selected)
            covered_branches.update(by_id[selected].branches)
        internal_weights = [
            weight
            for left in member_ids
            for right, weight in graph.get(left, [])
            if right in member_set and left < right
        ]
        plans[label] = {
            "index": index,
            "member_ids": member_ids,
            "member_count": len(member_ids),
            "representative_id": representative_id,
            "construction_ids": construction_ids,
            "construction_id_set": set(construction_ids),
            "cohesion": sum(internal_weights) / max(1, len(internal_weights)),
            "mean_path_score": sum(by_id[path_id].path_score for path_id in member_ids)
            / len(member_ids),
        }
    return ordered_labels, plans


def streamed_family_records(
    source_path: Path,
    indexed: list[PathFeatures],
    labels: dict[str, str],
    edges: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    ordered_labels, plans = plan_families(indexed, labels, edges)
    accumulators: dict[str, dict[str, Any]] = {
        label: {
            "branch_counter": collections.Counter(),
            "edge_counter": collections.Counter(),
            "facet_counter": collections.Counter(),
            "branch_rows": {},
            "edge_rows": {},
            "ayahs": set(),
            "roots": set(),
            "construction_paths": {},
            "representative_label": "",
        }
        for label in ordered_labels
    }
    with source_path.open("rb") as handle:
        for indexed_path in sorted(indexed, key=lambda row: path_sort_key(row.path_id)):
            handle.seek(indexed_path.source_offset)
            path = json.loads(handle.readline())
            path_id = str(path["path_id"])
            label = labels[path_id]
            plan = plans[label]
            acc = accumulators[label]
            acc["ayahs"].update(path["ayahs"])
            acc["roots"].update(path["roots"])
            for branch in path["branches"]:
                node_id = branch["node_id"]
                acc["branch_counter"][node_id] += 1
                acc["branch_rows"][node_id] = branch
            for edge in path["tree_edges"]:
                edge_key = edge["edge_key"]
                acc["edge_counter"][edge_key] += 1
                acc["edge_rows"][edge_key] = edge
            for facet, score in path.get("top_facets", []):
                acc["facet_counter"][facet] += float(score)
            if path_id == plan["representative_id"]:
                acc["representative_label"] = path["label_hint"]
            if path_id in plan["construction_id_set"]:
                acc["construction_paths"][path_id] = {
                    "path_id": path_id,
                    "path_score": path["path_score"],
                    "branches": path["branches"],
                    "tree_edges": path["tree_edges"],
                }

    families = []
    for label in ordered_labels:
        plan = plans[label]
        acc = accumulators[label]
        count = plan["member_count"]
        branch_counter = acc["branch_counter"]
        edge_counter = acc["edge_counter"]
        branch_rows = acc["branch_rows"]
        edge_rows = acc["edge_rows"]
        core = [
            branch_rows[node_id]
            for node_id, hits in branch_counter.items()
            if hits / count >= 0.50
        ]
        optional = [
            branch_rows[node_id]
            for node_id, hits in branch_counter.items()
            if 0.15 <= hits / count < 0.50
        ]
        alternatives: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
        for node_id, hits in branch_counter.items():
            branch = branch_rows[node_id]
            alternatives[branch["root"]].append(
                {
                    **branch,
                    "path_support": hits,
                    "support_ratio": round(hits / count, 4),
                }
            )
        for root in alternatives:
            alternatives[root].sort(
                key=lambda row: (-row["path_support"], row["branch_id"], row["node_id"])
            )
        top_facets = [
            (facet, round(score, 4))
            for facet, score in acc["facet_counter"].most_common(16)
        ]
        label_hint = " / ".join(
            facet.split(":", 1)[-1] for facet, _score in top_facets[:4]
        )
        stable_branch_ratio = len(core) / max(1, len(branch_counter))
        family_score = (
            0.45 * plan["mean_path_score"]
            + 0.35 * plan["cohesion"]
            + 0.20 * stable_branch_ratio
        )
        families.append(
            {
                "path_family_id": f"PF{plan['index']:04d}",
                "label_hint": label_hint or acc["representative_label"],
                "family_score": round(family_score, 4),
                "member_count": count,
                "representative_path_id": plan["representative_id"],
                "construction_paths": [
                    acc["construction_paths"][path_id]
                    for path_id in plan["construction_ids"]
                ],
                "path_ids": plan["member_ids"],
                "ayahs": sorted(acc["ayahs"]),
                "roots": sorted(acc["roots"]),
                "root_count": len(acc["roots"]),
                "branch_count": len(branch_counter),
                "core_branches": sorted(
                    core, key=lambda row: (row["root"], row["branch_id"])
                ),
                "optional_branches": sorted(
                    optional, key=lambda row: (row["root"], row["branch_id"])
                ),
                "branch_alternatives_by_root": dict(sorted(alternatives.items())),
                "core_edges": [
                    edge_rows[key]
                    for key, hits in edge_counter.items()
                    if hits / count >= 0.40
                ],
                "cohesion": round(plan["cohesion"], 4),
                "mean_path_score": round(plan["mean_path_score"], 4),
                "top_facets": top_facets,
            }
        )
    families.sort(key=lambda row: (-row["family_score"], row["path_family_id"]))
    return [
        {**row, "path_family_id": f"PF{index:04d}"}
        for index, row in enumerate(families, start=1)
    ]


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
    source_path = input_dir / "semantic_path_candidates.jsonl"
    indexed, postings = index_jsonl(source_path)
    edges = build_similarity_edges_indexed(
        indexed,
        postings,
        mutual_k=args.mutual_k,
        min_similarity=args.min_similarity,
        containment_threshold=args.containment_threshold,
    )
    labels = weighted_label_propagation(
        [row.path_id for row in indexed], edges, rounds=args.label_rounds
    )
    families = streamed_family_records(source_path, indexed, labels, edges)
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
        "counts": {"paths": len(indexed), "similarity_edges": len(edges), "path_families": len(families)},
        "top_families": [
            {key: row[key] for key in ["path_family_id", "family_score", "label_hint", "member_count", "roots"]}
            for row in families[:30]
        ],
    }
    write_json_atomic(output_dir / "path_family_summary.json", summary)
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
