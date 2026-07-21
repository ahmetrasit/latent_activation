#!/usr/bin/env python3
"""Assemble sparse semantic channels as branch paths across v3 families.

Dense candidate families recover themes whose branches resemble one another as
a group.  This complementary pass recovers channels whose evidence forms a
connected semantic script: every new branch needs one supported attachment,
not similarity to every branch already in the channel.

Candidate generation is label-free.  Qnet facets are attached only after a
path has been assembled, for compact review labels.
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import math
from pathlib import Path
from typing import Any

from discover_surah_channels import (
    branch_facets,
    load_qnet_facets,
    load_tsv,
    matrix_get,
    read_json,
    read_npy_flat,
    restrict_catalog_ayah_range,
    write_jsonl,
)


def rank_graph(
    catalog: dict[str, Any],
    affinity: list[float],
    width: int,
    eligible: set[int],
    *,
    top_k: int,
    max_partner_rank: int,
    min_affinity: float,
) -> tuple[dict[int, list[dict[str, Any]]], list[dict[str, Any]]]:
    branches = catalog["branches"]
    ranks: dict[int, dict[int, int]] = {}
    maxima: dict[int, float] = {}
    for left in sorted(eligible):
        ranked = sorted(
            (
                (matrix_get(affinity, width, left, right), right)
                for right in eligible
                if left != right and branches[left]["root"] != branches[right]["root"]
            ),
            key=lambda item: (-item[0], branches[item[1]]["display_key"], branches[item[1]]["node_id"]),
        )
        ranks[left] = {right: rank for rank, (_score, right) in enumerate(ranked, start=1)}
        maxima[left] = ranked[0][0] if ranked else 0.0

    graph: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
    edges = []
    for left in sorted(eligible):
        for right in sorted(eligible):
            if left >= right or branches[left]["root"] == branches[right]["root"]:
                continue
            affinity_score = matrix_get(affinity, width, left, right)
            left_rank = ranks[left][right]
            right_rank = ranks[right][left]
            if affinity_score <= min_affinity:
                continue
            if min(left_rank, right_rank) > top_k or max(left_rank, right_rank) > max_partner_rank:
                continue
            rank_support = 0.5 * (
                1.0 / math.log2(left_rank + 1.0)
                + 1.0 / math.log2(right_rank + 1.0)
            )
            relative_affinity = 0.5 * (
                affinity_score / max(maxima[left], 1e-12)
                + affinity_score / max(maxima[right], 1e-12)
            )
            strength = 0.70 * rank_support + 0.30 * min(1.0, relative_affinity)
            edge = {
                "left": left,
                "right": right,
                "affinity": float(affinity_score),
                "left_rank": left_rank,
                "right_rank": right_rank,
                "strength": float(strength),
            }
            graph[left].append(edge)
            graph[right].append(edge)
            edges.append(edge)

    for node in graph:
        graph[node].sort(key=lambda edge: (-edge["strength"], -edge["affinity"], edge["left"], edge["right"]))
    edges.sort(key=lambda edge: (-edge["strength"], -edge["affinity"], edge["left"], edge["right"]))
    return graph, edges


def other_node(edge: dict[str, Any], node: int) -> int:
    return int(edge["right"] if int(edge["left"]) == node else edge["left"])


def state_score(state: dict[str, Any], catalog: dict[str, Any], total_ayahs: int, max_roots: int) -> float:
    strengths = [float(edge["strength"]) for edge in state["tree_edges"]]
    ayahs = {
        int(ayah)
        for node in state["nodes"]
        for ayah in catalog["branches"][node].get("ayahs", [])
    }
    mean_strength = sum(strengths) / max(1, len(strengths))
    weakest = min(strengths, default=0.0)
    ayah_coverage = len(ayahs) / max(1, total_ayahs)
    root_progress = len(state["nodes"]) / max(1, max_roots)
    return 0.55 * mean_strength + 0.20 * weakest + 0.15 * ayah_coverage + 0.10 * root_progress


def beam_paths_from_seed(
    seed: int,
    graph: dict[int, list[dict[str, Any]]],
    catalog: dict[str, Any],
    *,
    min_roots: int,
    max_roots: int,
    min_ayahs: int,
    beam_width: int,
    extension_width: int,
) -> list[dict[str, Any]]:
    branches = catalog["branches"]
    total_ayahs = len(catalog.get("ayahs", []))
    states = [{"nodes": (seed,), "tree_edges": tuple(), "seed": seed}]
    completed = []

    for _size in range(2, max_roots + 1):
        expanded: dict[tuple[int, ...], dict[str, Any]] = {}
        for state in states:
            node_set = set(state["nodes"])
            roots = {branches[node]["root"] for node in node_set}
            attachments: dict[int, dict[str, Any]] = {}
            for node in state["nodes"]:
                for edge in graph.get(node, []):
                    target = other_node(edge, node)
                    if target in node_set or branches[target]["root"] in roots:
                        continue
                    current = attachments.get(target)
                    if current is None or (edge["strength"], edge["affinity"]) > (current["strength"], current["affinity"]):
                        attachments[target] = edge
            choices = sorted(
                attachments.items(),
                key=lambda item: (-item[1]["strength"], -item[1]["affinity"], branches[item[0]]["display_key"]),
            )[:extension_width]
            for target, edge in choices:
                nodes = tuple(sorted((*state["nodes"], target)))
                new_state = {
                    "nodes": nodes,
                    "tree_edges": (*state["tree_edges"], edge),
                    "seed": seed,
                }
                new_state["search_score"] = state_score(new_state, catalog, total_ayahs, max_roots)
                old = expanded.get(nodes)
                if old is None or new_state["search_score"] > old["search_score"]:
                    expanded[nodes] = new_state
        states = sorted(
            expanded.values(),
            key=lambda state: (-state["search_score"], state["nodes"]),
        )[:beam_width]
        for state in states:
            ayahs = {
                int(ayah)
                for node in state["nodes"]
                for ayah in branches[node].get("ayahs", [])
            }
            if len(state["nodes"]) >= min_roots and len(ayahs) >= min_ayahs:
                completed.append(state)
        if not states:
            break
    return completed


def edge_record(edge: dict[str, Any], branches: list[dict[str, Any]], branch_rows: dict[str, dict[str, str]]) -> dict[str, Any]:
    left = branches[int(edge["left"])]
    right = branches[int(edge["right"])]
    return {
        "edge_key": " -- ".join(sorted([left["node_id"], right["node_id"]])),
        "strength": round(float(edge["strength"]), 6),
        "affinity": round(float(edge["affinity"]), 8),
        "ranks": [int(edge["left_rank"]), int(edge["right_rank"])],
        "left": {
            "node_id": left["node_id"],
            "root": left["root"],
            "branch_id": left["branch_id"],
            "ayahs": left.get("ayahs", []),
            "image_ar": branch_rows[left["node_id"]].get("branch_image_ar", ""),
        },
        "right": {
            "node_id": right["node_id"],
            "root": right["root"],
            "branch_id": right["branch_id"],
            "ayahs": right.get("ayahs", []),
            "image_ar": branch_rows[right["node_id"]].get("branch_image_ar", ""),
        },
    }


def path_record(
    state: dict[str, Any],
    catalog: dict[str, Any],
    branch_rows: dict[str, dict[str, str]],
    facets_by_node: dict[str, list[dict[str, Any]]],
) -> dict[str, Any]:
    branches = catalog["branches"]
    nodes = list(state["nodes"])
    ayahs = sorted({int(ayah) for node in nodes for ayah in branches[node].get("ayahs", [])})
    roots = sorted({branches[node]["root"] for node in nodes})
    facet_hits: collections.Counter[str] = collections.Counter()
    for node in nodes:
        for facet in facets_by_node.get(branches[node]["node_id"], [])[:8]:
            facet_hits[facet["facet"]] += float(facet["weight"])
    top_facets = [(facet, round(score, 4)) for facet, score in facet_hits.most_common(16)]
    label_terms = [facet.split(":", 1)[-1] for facet, _score in top_facets[:4]]
    tree_edges = [edge_record(edge, branches, branch_rows) for edge in state["tree_edges"]]
    strengths = [edge["strength"] for edge in tree_edges]
    return {
        "path_id": "pending",
        "label_hint": " / ".join(label_terms) if label_terms else "unlabeled semantic path",
        "path_score": round(float(state["search_score"]), 4),
        "mean_edge_strength": round(sum(strengths) / max(1, len(strengths)), 6),
        "weakest_edge_strength": round(min(strengths, default=0.0), 6),
        "seed_node_id": branches[state["seed"]]["node_id"],
        "ayahs": ayahs,
        "ayah_count": len(ayahs),
        "roots": roots,
        "root_count": len(roots),
        "branches": [
            {
                "node_id": branches[node]["node_id"],
                "root": branches[node]["root"],
                "branch_id": branches[node]["branch_id"],
                "ayahs": branches[node].get("ayahs", []),
                "image_ar": branch_rows[branches[node]["node_id"]].get("branch_image_ar", ""),
            }
            for node in nodes
        ],
        "tree_edges": tree_edges,
        "top_facets": top_facets,
    }


def jaccard(left: set[str], right: set[str]) -> float:
    return len(left & right) / len(left | right) if left or right else 0.0


def containment(left: set[str], right: set[str]) -> float:
    return len(left & right) / min(len(left), len(right)) if left and right else 0.0


def dedupe_paths(rows: list[dict[str, Any]], *, branch_jaccard: float, branch_containment: float, limit: int) -> list[dict[str, Any]]:
    kept = []
    signatures = []
    branch_index: dict[str, set[int]] = collections.defaultdict(set)
    for row in sorted(rows, key=lambda item: (-item["path_score"], -item["root_count"], item["seed_node_id"])):
        branches = {branch["node_id"] for branch in row["branches"]}
        edges = {edge["edge_key"] for edge in row["tree_edges"]}
        roots = set(row["roots"])
        duplicate = False
        possible_matches: set[int] = set()
        for branch in branches:
            possible_matches.update(branch_index.get(branch, set()))
        for existing_index in possible_matches:
            existing = signatures[existing_index]
            if (
                jaccard(branches, existing["branches"]) >= branch_jaccard
                or (
                    containment(branches, existing["branches"]) >= branch_containment
                    and jaccard(roots, existing["roots"]) >= 0.70
                )
                or (
                    jaccard(edges, existing["edges"]) >= 0.55
                    and jaccard(roots, existing["roots"]) >= 0.65
                )
            ):
                duplicate = True
                break
        if duplicate:
            continue
        row = {**row, "path_id": f"P{len(kept)+1:04d}"}
        kept.append(row)
        signatures.append({"branches": branches, "edges": edges, "roots": roots})
        kept_index = len(signatures) - 1
        for branch in branches:
            branch_index[branch].add(kept_index)
        if limit > 0 and len(kept) >= limit:
            break
    return kept


def load_family_memberships(input_dir: Path | None) -> dict[str, list[str]]:
    memberships: dict[str, list[str]] = collections.defaultdict(list)
    if input_dir is None:
        return memberships
    path = input_dir / "families" / "family_branch_inventory.tsv"
    if not path.exists():
        return memberships
    with path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            memberships[row["node_id"]].append(row["family_id"])
    return memberships


def write_review_queue(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["rank", "path_id", "path_score", "label_hint", "ayahs", "roots", "branch_chain"])
        for rank, row in enumerate(rows, start=1):
            branch_chain = " | ".join(
                f"{branch['root']}:{branch['branch_id']}:{branch['image_ar']}"
                for branch in row["branches"]
            )
            writer.writerow([
                rank,
                row["path_id"],
                row["path_score"],
                row["label_hint"],
                ",".join(map(str, row["ayahs"])),
                " ".join(row["roots"]),
                branch_chain,
            ])


def build(args: argparse.Namespace) -> dict[str, Any]:
    surah_tag = f"s{args.surah:03d}"
    quran_slm = Path(args.quran_slm)
    quran_roots = Path(args.quran_roots)
    network_dir = quran_slm / args.network_artifact_dir / surah_tag
    resource_dir = quran_slm / args.surah_resource_dir / surah_tag
    output_dir = Path(args.output_dir) / surah_tag / "paths"
    output_dir.mkdir(parents=True, exist_ok=True)

    catalog = read_json(network_dir / "catalog.json")
    eligible = restrict_catalog_ayah_range(catalog, args.ayah_from, args.ayah_to)
    affinity, shape, _dtype = read_npy_flat(network_dir / "affinity.npy")
    branch_rows = load_tsv(resource_dir / "branches_ar.tsv", "node_id")
    qnet_facets, facet_idf = load_qnet_facets(quran_roots)
    facets_by_node = {
        branch["node_id"]: branch_facets(branch["node_id"], qnet_facets, facet_idf)
        for branch in catalog["branches"]
    }
    graph, graph_edges = rank_graph(
        catalog,
        affinity,
        shape[1],
        eligible,
        top_k=args.top_k,
        max_partner_rank=args.max_partner_rank,
        min_affinity=args.min_affinity,
    )

    raw_states = []
    for seed in sorted(eligible):
        raw_states.extend(
            beam_paths_from_seed(
                seed,
                graph,
                catalog,
                min_roots=args.min_roots,
                max_roots=args.max_roots,
                min_ayahs=args.min_ayahs,
                beam_width=args.beam_width,
                extension_width=args.extension_width,
            )
        )
    unique_states: dict[tuple[int, ...], dict[str, Any]] = {}
    for state in raw_states:
        old = unique_states.get(state["nodes"])
        if old is None or state["search_score"] > old["search_score"]:
            unique_states[state["nodes"]] = state
    raw_records = [path_record(state, catalog, branch_rows, facets_by_node) for state in unique_states.values()]
    paths = dedupe_paths(
        raw_records,
        branch_jaccard=args.dedupe_jaccard,
        branch_containment=args.subset_overlap,
        limit=args.path_limit,
    )

    memberships = load_family_memberships(Path(args.family_input_dir) / surah_tag if args.family_input_dir else None)
    for row in paths:
        family_counts: collections.Counter[str] = collections.Counter()
        for branch in row["branches"]:
            family_counts.update(memberships.get(branch["node_id"], []))
        row["source_families"] = [family for family, _count in family_counts.most_common()]

    write_jsonl(output_dir / "semantic_path_candidates.jsonl", paths)
    write_review_queue(output_dir / "path_review_queue.tsv", paths)
    summary = {
        "version": "v3_sparse_semantic_path_assembly_v0",
        "surah": args.surah,
        "generation_policy": "label-free branch paths; Qnet facets attached after assembly",
        "parameters": {
            "ayah_from": args.ayah_from,
            "ayah_to": args.ayah_to,
            "top_k": args.top_k,
            "max_partner_rank": args.max_partner_rank,
            "min_affinity": args.min_affinity,
            "min_roots": args.min_roots,
            "max_roots": args.max_roots,
            "min_ayahs": args.min_ayahs,
            "beam_width": args.beam_width,
            "extension_width": args.extension_width,
            "path_limit": args.path_limit,
        },
        "counts": {
            "eligible_branches": len(eligible),
            "path_graph_edges": len(graph_edges),
            "raw_path_states": len(raw_states),
            "unique_path_states": len(unique_states),
            "deduped_paths": len(paths),
        },
        "top_paths": [
            {
                "path_id": row["path_id"],
                "path_score": row["path_score"],
                "label_hint": row["label_hint"],
                "ayahs": row["ayahs"],
                "roots": row["roots"],
            }
            for row in paths[:30]
        ],
    }
    (output_dir / "path_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--quran-slm", default="../quran-slm")
    parser.add_argument("--quran-roots", default="../quran-roots")
    parser.add_argument("--network-artifact-dir", default="artifacts/surah_networks_global")
    parser.add_argument("--surah-resource-dir", default="artifacts/corpus_network/surah_resources")
    parser.add_argument("--family-input-dir", help="optional v3 output base containing s###/families")
    parser.add_argument("--output-dir", default="network/v3/output")
    parser.add_argument("--ayah-from", type=int)
    parser.add_argument("--ayah-to", type=int)
    parser.add_argument("--top-k", type=int, default=20)
    parser.add_argument("--max-partner-rank", type=int, default=80)
    parser.add_argument("--min-affinity", type=float, default=0.0)
    parser.add_argument("--min-roots", type=int, default=3)
    parser.add_argument("--max-roots", type=int, default=10)
    parser.add_argument("--min-ayahs", type=int, default=3)
    parser.add_argument("--beam-width", type=int, default=96)
    parser.add_argument("--extension-width", type=int, default=16)
    parser.add_argument("--dedupe-jaccard", type=float, default=0.60)
    parser.add_argument("--subset-overlap", type=float, default=0.85)
    parser.add_argument("--path-limit", type=int, default=0, help="maximum paths to write; 0 means no cap")
    return parser.parse_args()


def main() -> None:
    print(json.dumps(build(parse_args()), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
