#!/usr/bin/env python3
"""Discover label-free semantic channel candidates from surah-local SLM networks.

v3 deliberately avoids the v2/slm_local fixed domain gates.  It mines graph
neighborhoods first, scores them as candidate channel objects, and only then
attaches Qnet keywords/themes as descriptive labels for review.
"""

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


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")))
            handle.write("\n")


def read_npy_flat(path: Path) -> tuple[list[float], tuple[int, int], str]:
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
    shape = tuple(header["shape"])
    descr = header["descr"]
    if header.get("fortran_order"):
        raise ValueError("Fortran-order .npy is not supported")
    if len(shape) != 2 or shape[0] != shape[1]:
        raise ValueError(f"expected square 2D matrix, got {shape}")
    if descr != "<f4":
        raise ValueError(f"expected little-endian float32 matrix, got {descr}")
    count = int(shape[0]) * int(shape[1])
    values = struct.unpack("<" + "f" * count, data[offset + header_len : offset + header_len + count * 4])
    return [float(v) for v in values], (int(shape[0]), int(shape[1])), descr


def matrix_get(values: list[float], width: int, row: int, col: int) -> float:
    return values[row * width + col]


def load_tsv(path: Path, key: str) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return {row[key]: row for row in csv.DictReader(handle, delimiter="\t")}


def parse_node_id(node_id: str) -> tuple[str, str]:
    _, root_id, branch_id = node_id.split(":")
    return root_id, branch_id


def load_qnet_facets(quran_roots: Path) -> tuple[dict[tuple[str, str], list[dict[str, Any]]], dict[str, float]]:
    facets: dict[tuple[str, str], list[dict[str, Any]]] = collections.defaultdict(list)
    facet_nodes: dict[str, set[tuple[str, str]]] = collections.defaultdict(set)

    keyword_path = quran_roots / "_corpus/activation/Qnet/v2/network/incidence_full/branch_keywords.tsv"
    with keyword_path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            key = (row["root_id"], row["branch_id"])
            votes = int(row["replicate_votes"])
            if votes < 2:
                continue
            facet = f"kw:{row['keyword']}"
            facets[key].append({"facet": facet, "kind": "keyword", "score": votes})
            facet_nodes[facet].add(key)

    theme_path = quran_roots / "_corpus/activation/Qnet/v2/network/bridge_theme_full/branch_theme_inventory.tsv"
    with theme_path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            key = (row["root_id"], row["branch_id"])
            facet = f"theme:{row['parent_theme']}/{row['theme']}"
            score = int(row["raw_keyword_count"])
            facets[key].append({"facet": facet, "kind": "theme", "score": score})
            facet_nodes[facet].add(key)

    total_nodes = len(set().union(*facet_nodes.values())) if facet_nodes else 0
    idf = {
        facet: math.log((1 + total_nodes) / (1 + len(nodes))) + 1.0
        for facet, nodes in facet_nodes.items()
    }
    return facets, idf


def branch_facets(
    node_id: str,
    qnet_facets: dict[tuple[str, str], list[dict[str, Any]]],
    facet_idf: dict[str, float],
) -> list[dict[str, Any]]:
    out = []
    for item in qnet_facets.get(parse_node_id(node_id), []):
        weight = float(item["score"]) * facet_idf.get(item["facet"], 1.0)
        out.append({**item, "weight": round(weight, 6)})
    out.sort(key=lambda row: (-row["weight"], row["facet"]))
    return out[:24]


def build_top_graph(
    catalog: dict[str, Any],
    affinity: list[float],
    width: int,
    *,
    top_k: int,
    min_affinity: float,
    eligible_indices: set[int] | None = None,
) -> tuple[dict[int, dict[int, dict[str, Any]]], list[dict[str, Any]]]:
    branches = catalog["branches"]
    if eligible_indices is None:
        eligible_indices = {int(branch["index"]) for branch in branches}
    undirected: dict[tuple[int, int], dict[str, Any]] = {}

    for source in branches:
        i = int(source["index"])
        if i not in eligible_indices:
            continue
        ranked = []
        for target in branches:
            j = int(target["index"])
            if j not in eligible_indices:
                continue
            if i == j or source["root"] == target["root"]:
                continue
            score = matrix_get(affinity, width, i, j)
            if score > min_affinity:
                ranked.append((score, j, target))
        ranked.sort(key=lambda item: (-item[0], branches[item[1]]["display_key"], branches[item[1]]["node_id"]))
        for rank, (score, j, target) in enumerate(ranked[:top_k], start=1):
            a, b = sorted((i, j))
            key = (a, b)
            existing = undirected.get(key)
            if existing is None:
                undirected[key] = {
                    "left": a,
                    "right": b,
                    "affinity": float(score),
                    "rank_left_to_right": rank if i == a else None,
                    "rank_right_to_left": rank if i == b else None,
                }
            else:
                existing["affinity"] = max(existing["affinity"], float(score))
                if i == a:
                    existing["rank_left_to_right"] = min(existing["rank_left_to_right"] or rank, rank)
                else:
                    existing["rank_right_to_left"] = min(existing["rank_right_to_left"] or rank, rank)

    edges = sorted(
        undirected.values(),
        key=lambda row: (-row["affinity"], row["left"], row["right"]),
    )
    graph: dict[int, dict[int, dict[str, Any]]] = collections.defaultdict(dict)
    for edge in edges:
        left = int(edge["left"])
        right = int(edge["right"])
        graph[left][right] = edge
        graph[right][left] = edge
    return graph, edges


def restrict_catalog_ayah_range(catalog: dict[str, Any], ayah_from: int | None, ayah_to: int | None) -> set[int]:
    if ayah_from is None and ayah_to is None:
        return {int(branch["index"]) for branch in catalog["branches"]}

    all_ayahs = [int(ayah) for ayah in catalog.get("ayahs", [])]
    lower = ayah_from if ayah_from is not None else min(all_ayahs)
    upper = ayah_to if ayah_to is not None else max(all_ayahs)
    if lower > upper:
        raise ValueError(f"invalid ayah range: {lower}..{upper}")

    kept_ayahs = [ayah for ayah in all_ayahs if lower <= ayah <= upper]
    kept_indices = set()
    for branch in catalog["branches"]:
        branch["ayahs"] = [int(ayah) for ayah in branch.get("ayahs", []) if lower <= int(ayah) <= upper]
        if branch["ayahs"]:
            kept_indices.add(int(branch["index"]))

    catalog["ayahs"] = kept_ayahs
    if "ayah_roots" in catalog:
        catalog["ayah_roots"] = {
            str(ayah): roots
            for ayah, roots in catalog["ayah_roots"].items()
            if lower <= int(ayah) <= upper
        }
    if "ayah_pool_sizes" in catalog:
        catalog["ayah_pool_sizes"] = {
            str(ayah): size
            for ayah, size in catalog["ayah_pool_sizes"].items()
            if lower <= int(ayah) <= upper
        }
    return kept_indices


def connected_components(nodes: set[int], graph: dict[int, dict[int, dict[str, Any]]]) -> list[set[int]]:
    remaining = set(nodes)
    components = []
    while remaining:
        start = remaining.pop()
        stack = [start]
        component = {start}
        while stack:
            current = stack.pop()
            for neighbor in graph.get(current, {}):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    stack.append(neighbor)
        components.append(component)
    return components


def candidate_from_seed(
    seed: int,
    graph: dict[int, dict[int, dict[str, Any]]],
    *,
    ego_k: int,
    expand_min_links: int,
    expand_min_mean: float,
) -> set[int]:
    seed_neighbors = sorted(
        graph.get(seed, {}).items(),
        key=lambda item: (-item[1]["affinity"], item[0]),
    )
    core = {seed} | {neighbor for neighbor, _edge in seed_neighbors[:ego_k]}

    neighbor_pool = set()
    for node in core:
        neighbor_pool.update(graph.get(node, {}))
    neighbor_pool -= core

    additions = []
    for node in neighbor_pool:
        scores = [graph[node][core_node]["affinity"] for core_node in core if core_node in graph.get(node, {})]
        if len(scores) >= expand_min_links and sum(scores) / len(scores) >= expand_min_mean:
            additions.append((sum(scores) / len(scores), node))
    additions.sort(reverse=True)
    core.update(node for _score, node in additions[:ego_k])

    return core


def cluster_edges(nodes: set[int], graph: dict[int, dict[int, dict[str, Any]]]) -> list[dict[str, Any]]:
    out = []
    for left in sorted(nodes):
        for right, edge in graph.get(left, {}).items():
            if right in nodes and left < right:
                out.append(edge)
    out.sort(key=lambda row: (-row["affinity"], row["left"], row["right"]))
    return out


def node_ayahs(branch: dict[str, Any]) -> set[int]:
    return {int(ayah) for ayah in branch.get("ayahs", [])}


def root_ablation_survival(nodes: set[int], edges: list[dict[str, Any]], branches: list[dict[str, Any]]) -> float:
    roots = {branches[node]["root"] for node in nodes}
    if not roots or not edges:
        return 0.0
    survivals = []
    for root in roots:
        remaining = {
            node
            for node in nodes
            if branches[node]["root"] != root
        }
        remaining_edges = [edge for edge in edges if edge["left"] in remaining and edge["right"] in remaining]
        if not remaining:
            survivals.append(0.0)
            continue
        largest = max((len(component) for component in connected_components(remaining, edge_subgraph(remaining_edges))), default=0)
        survivals.append(largest / max(1, len(nodes)))
    return min(survivals) if survivals else 0.0


def edge_subgraph(edges: list[dict[str, Any]]) -> dict[int, dict[int, dict[str, Any]]]:
    graph: dict[int, dict[int, dict[str, Any]]] = collections.defaultdict(dict)
    for edge in edges:
        left = int(edge["left"])
        right = int(edge["right"])
        graph[left][right] = edge
        graph[right][left] = edge
    return graph


def branch_edge_record(edge: dict[str, Any], branches: list[dict[str, Any]], branch_rows: dict[str, dict[str, str]]) -> dict[str, Any]:
    left = branches[int(edge["left"])]
    right = branches[int(edge["right"])]
    left_row = branch_rows[left["node_id"]]
    right_row = branch_rows[right["node_id"]]
    return {
        "edge_key": " -- ".join(sorted([left["node_id"], right["node_id"]])),
        "affinity": round(edge["affinity"], 8),
        "ranks": [edge["rank_left_to_right"], edge["rank_right_to_left"]],
        "left": {
            "node_id": left["node_id"],
            "ayahs": left["ayahs"],
            "root": left["root"],
            "branch_id": left["branch_id"],
            "image_ar": left_row.get("branch_image_ar", ""),
        },
        "right": {
            "node_id": right["node_id"],
            "ayahs": right["ayahs"],
            "root": right["root"],
            "branch_id": right["branch_id"],
            "image_ar": right_row.get("branch_image_ar", ""),
        },
    }


def summarize_candidate(
    candidate_id: str,
    seed: int,
    nodes: set[int],
    graph: dict[int, dict[int, dict[str, Any]]],
    catalog: dict[str, Any],
    branch_rows: dict[str, dict[str, str]],
    facets_by_node: dict[str, list[dict[str, Any]]],
    *,
    edge_affinity_floor: float,
    min_roots: int,
    min_ayahs: int,
) -> dict[str, Any] | None:
    branches = catalog["branches"]
    roots = {branches[node]["root"] for node in nodes}
    ayahs = sorted({ayah for node in nodes for ayah in node_ayahs(branches[node])})
    if len(roots) < min_roots or len(ayahs) < min_ayahs:
        return None

    internal_edges = [edge for edge in cluster_edges(nodes, graph) if edge["affinity"] >= edge_affinity_floor]
    if len(internal_edges) < max(2, len(nodes) - 2):
        return None

    possible = 0
    for left in nodes:
        for right in nodes:
            if left < right and branches[left]["root"] != branches[right]["root"]:
                possible += 1

    mean_affinity = sum(edge["affinity"] for edge in internal_edges) / max(1, len(internal_edges))
    density = len(internal_edges) / max(1, possible)
    reciprocal_ratio = sum(1 for edge in internal_edges if edge["rank_left_to_right"] and edge["rank_right_to_left"]) / len(internal_edges)
    strong_rank_ratio = sum(
        1
        for edge in internal_edges
        if min(edge["rank_left_to_right"] or 9999, edge["rank_right_to_left"] or 9999) <= 3
    ) / len(internal_edges)
    root_counts = collections.Counter(branches[node]["root"] for node in nodes)
    root_balance = 1.0 - (max(root_counts.values()) / max(1, len(nodes)))
    ablation = root_ablation_survival(nodes, internal_edges, branches)

    cohesion_score = (
        0.25 * min(1.0, density * 3.0)
        + 0.20 * min(1.0, mean_affinity / 0.09)
        + 0.15 * reciprocal_ratio
        + 0.15 * strong_rank_ratio
        + 0.15 * min(1.0, len(roots) / 8)
        + 0.10 * root_balance
    )
    span_score = min(1.0, len(ayahs) / max(3, len(catalog.get("ayahs", [])) or 3))
    channel_score = 0.82 * cohesion_score + 0.18 * span_score

    facet_hits: collections.Counter[str] = collections.Counter()
    for node in nodes:
        node_id = branches[node]["node_id"]
        for facet in facets_by_node.get(node_id, [])[:8]:
            facet_hits[facet["facet"]] += float(facet["weight"])

    examples = []
    for edge in internal_edges[:10]:
        examples.append(branch_edge_record(edge, branches, branch_rows))

    per_ayah = {}
    for ayah in ayahs:
        rows = []
        for node in sorted(nodes):
            branch = branches[node]
            if ayah not in node_ayahs(branch):
                continue
            row = branch_rows[branch["node_id"]]
            rows.append(
                {
                    "root": branch["root"],
                    "branch_id": branch["branch_id"],
                    "image_ar": row.get("branch_image_ar", ""),
                    "top_facets": [item["facet"] for item in facets_by_node.get(branch["node_id"], [])[:4]],
                }
            )
        per_ayah[str(ayah)] = rows

    label_terms = [facet.split(":", 1)[1] for facet, _score in facet_hits.most_common(6)]
    label_hint = " / ".join(label_terms[:4]) if label_terms else "unlabeled graph cluster"

    return {
        "candidate_id": candidate_id,
        "seed_provenance": {
            "seed_index": seed,
            "seed_node_id": branches[seed]["node_id"],
            "seed_root": branches[seed]["root"],
            "seed_branch_id": branches[seed]["branch_id"],
            "seed_ayahs": branches[seed]["ayahs"],
        },
        "label_hint": label_hint,
        "channel_score": round(channel_score, 4),
        "cohesion_score": round(cohesion_score, 4),
        "span_score": round(span_score, 4),
        "edge_count": len(internal_edges),
        "node_count": len(nodes),
        "root_count": len(roots),
        "branch_count": len(nodes),
        "ayah_count": len(ayahs),
        "ayahs": ayahs,
        "roots": sorted(roots),
        "branches": [
            {
                "node_id": branches[node]["node_id"],
                "root": branches[node]["root"],
                "branch_id": branches[node]["branch_id"],
                "ayahs": branches[node]["ayahs"],
                "image_ar": branch_rows[branches[node]["node_id"]].get("branch_image_ar", ""),
            }
            for node in sorted(nodes)
        ],
        "mean_affinity": round(mean_affinity, 8),
        "density": round(density, 4),
        "reciprocal_edge_ratio": round(reciprocal_ratio, 4),
        "strong_rank_ratio": round(strong_rank_ratio, 4),
        "root_balance": round(root_balance, 4),
        "root_ablation_min_survival": round(ablation, 4),
        "top_facets": [(facet, round(score, 4)) for facet, score in facet_hits.most_common(16)],
        "branch_edges": [branch_edge_record(edge, branches, branch_rows) for edge in internal_edges],
        "per_ayah_build": per_ayah,
        "support_examples": examples,
    }


def jaccard(left: set[Any], right: set[Any]) -> float:
    union = len(left | right)
    return len(left & right) / union if union else 0.0


def containment(left: set[Any], right: set[Any]) -> float:
    smaller = min(len(left), len(right))
    return len(left & right) / smaller if smaller else 0.0


def dedupe_candidates(
    rows: list[dict[str, Any]],
    *,
    max_jaccard: float,
    subset_overlap: float,
    limit: int,
) -> list[dict[str, Any]]:
    kept = []
    kept_signatures: list[dict[str, set[Any]]] = []
    for row in sorted(rows, key=lambda item: (-item["channel_score"], -item["edge_count"], item["candidate_id"])):
        signature = {
            "roots": set(row["roots"]),
            "ayahs": set(row["ayahs"]),
            "branches": {item["node_id"] for item in row["branches"]},
        }
        too_close = False
        for existing in kept_signatures:
            branch_overlap = jaccard(signature["branches"], existing["branches"])
            root_overlap = jaccard(signature["roots"], existing["roots"])
            ayah_overlap = jaccard(signature["ayahs"], existing["ayahs"])
            branch_containment = containment(signature["branches"], existing["branches"])
            root_containment = containment(signature["roots"], existing["roots"])
            ayah_containment = containment(signature["ayahs"], existing["ayahs"])
            if (
                branch_overlap >= 0.60
                or (root_overlap >= 0.75 and ayah_overlap >= 0.75)
                or (
                    branch_containment >= subset_overlap
                    and root_containment >= 0.65
                    and ayah_containment >= 0.65
                )
                or (
                    root_containment >= subset_overlap
                    and ayah_containment >= subset_overlap
                    and branch_overlap >= 0.35
                )
            ):
                too_close = True
                break
        if too_close:
            continue
        kept.append({**row, "candidate_id": f"C{len(kept)+1:03d}"})
        kept_signatures.append(signature)
        if limit > 0 and len(kept) >= limit:
            break
    return kept


def write_tsv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "candidate_id",
                "channel_score",
                "label_hint",
                "ayah_count",
                "root_count",
                "branch_count",
                "edge_count",
                "mean_affinity",
                "density",
                "reciprocal_edge_ratio",
                "strong_rank_ratio",
                "ayahs",
                "roots",
                "top_facets",
                "example_edge",
            ]
        )
        for row in rows:
            example = row["support_examples"][0] if row["support_examples"] else {}
            if example:
                example_text = (
                    f"{example['left']['root']}:{example['left']['branch_id']}:{example['left']['image_ar']}"
                    " → "
                    f"{example['right']['root']}:{example['right']['branch_id']}:{example['right']['image_ar']}"
                )
            else:
                example_text = ""
            writer.writerow(
                [
                    row["candidate_id"],
                    row["channel_score"],
                    row["label_hint"],
                    row["ayah_count"],
                    row["root_count"],
                    row["branch_count"],
                    row["edge_count"],
                    row["mean_affinity"],
                    row["density"],
                    row["reciprocal_edge_ratio"],
                    row["strong_rank_ratio"],
                    ",".join(map(str, row["ayahs"])),
                    " ".join(row["roots"]),
                    "; ".join(f"{facet}({score})" for facet, score in row["top_facets"][:8]),
                    example_text,
                ]
            )


def build(args: argparse.Namespace) -> dict[str, Any]:
    surah_tag = f"s{args.surah:03d}"
    quran_slm = Path(args.quran_slm)
    quran_roots = Path(args.quran_roots)
    output_dir = Path(args.output_dir) / surah_tag
    output_dir.mkdir(parents=True, exist_ok=True)

    network_dir = quran_slm / args.network_artifact_dir / surah_tag
    resource_dir = quran_slm / args.surah_resource_dir / surah_tag
    catalog = read_json(network_dir / "catalog.json")
    report = read_json(network_dir / "build_report.json")
    eligible_indices = restrict_catalog_ayah_range(catalog, args.ayah_from, args.ayah_to)
    affinity, shape, dtype = read_npy_flat(network_dir / "affinity.npy")
    branch_rows = load_tsv(resource_dir / "branches_ar.tsv", "node_id")
    qnet_facets, facet_idf = load_qnet_facets(quran_roots)
    facets_by_node = {
        branch["node_id"]: branch_facets(branch["node_id"], qnet_facets, facet_idf)
        for branch in catalog["branches"]
    }

    graph, edges = build_top_graph(
        catalog,
        affinity,
        shape[1],
        top_k=args.top_k,
        min_affinity=args.min_affinity,
        eligible_indices=eligible_indices,
    )
    edge_floor = args.edge_affinity_floor
    if edge_floor is None:
        ranked_scores = sorted((edge["affinity"] for edge in edges), reverse=True)
        if ranked_scores:
            edge_floor = ranked_scores[min(len(ranked_scores) - 1, max(0, int(len(ranked_scores) * args.edge_floor_quantile)))]
        else:
            edge_floor = 0.0

    raw_candidates = []
    seen_node_sets: set[tuple[int, ...]] = set()
    for seed in sorted(eligible_indices):
        nodes = candidate_from_seed(
            seed,
            graph,
            ego_k=args.ego_k,
            expand_min_links=args.expand_min_links,
            expand_min_mean=edge_floor,
        )
        key = tuple(sorted(nodes))
        if key in seen_node_sets:
            continue
        seen_node_sets.add(key)
        record = summarize_candidate(
            f"raw_{len(raw_candidates)+1:05d}",
            seed,
            nodes,
            graph,
            catalog,
            branch_rows,
            facets_by_node,
            edge_affinity_floor=edge_floor,
            min_roots=args.min_roots,
            min_ayahs=args.min_ayahs,
        )
        if record is not None:
            raw_candidates.append(record)

    candidates = dedupe_candidates(
        raw_candidates,
        max_jaccard=args.dedupe_jaccard,
        subset_overlap=args.subset_overlap,
        limit=args.candidate_limit,
    )
    write_jsonl(output_dir / "channel_candidates.jsonl", candidates)
    write_tsv(output_dir / "channel_candidates.tsv", candidates)

    summary = {
        "version": "v3_label_free_graph_channel_discovery_v0",
        "surah": args.surah,
        "inputs": {
            "slm_algorithm_version": report.get("algorithm_version"),
            "network_artifact_dir": str(network_dir),
            "surah_resource_dir": str(resource_dir),
            "catalog_branch_count": len(catalog["branches"]),
            "eligible_branch_count": len(eligible_indices),
            "affinity_shape": shape,
            "affinity_dtype": dtype,
            "qnet_policy": "descriptive labels only; not used as candidate gates",
        },
        "parameters": {
            "top_k": args.top_k,
            "ayah_from": args.ayah_from,
            "ayah_to": args.ayah_to,
            "ego_k": args.ego_k,
            "min_affinity": args.min_affinity,
            "edge_affinity_floor": round(edge_floor, 8),
            "edge_floor_quantile": args.edge_floor_quantile,
            "expand_min_links": args.expand_min_links,
            "dedupe_jaccard": args.dedupe_jaccard,
            "subset_overlap": args.subset_overlap,
            "candidate_limit": args.candidate_limit,
            "minimum_filter": f">={args.min_roots} roots and >={args.min_ayahs} ayahs",
        },
        "counts": {
            "graph_edges": len(edges),
            "raw_candidates": len(raw_candidates),
            "deduped_candidates": len(candidates),
        },
        "top_candidates": [
            {
                "candidate_id": row["candidate_id"],
                "channel_score": row["channel_score"],
                "label_hint": row["label_hint"],
                "ayahs": row["ayahs"],
                "root_count": row["root_count"],
                "branch_count": row["branch_count"],
                "edge_count": row["edge_count"],
            }
            for row in candidates[:20]
        ],
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--quran-slm", default="../quran-slm")
    parser.add_argument("--quran-roots", default="../quran-roots")
    parser.add_argument("--network-artifact-dir", default="artifacts/surah_networks_global_ensemble")
    parser.add_argument("--surah-resource-dir", default="artifacts/corpus_network/surah_resources")
    parser.add_argument("--output-dir", default="network/v3/output")
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--ayah-from", type=int)
    parser.add_argument("--ayah-to", type=int)
    parser.add_argument("--ego-k", type=int, default=8)
    parser.add_argument("--min-affinity", type=float, default=0.0)
    parser.add_argument("--edge-affinity-floor", type=float)
    parser.add_argument("--edge-floor-quantile", type=float, default=0.35)
    parser.add_argument("--expand-min-links", type=int, default=2)
    parser.add_argument("--dedupe-jaccard", type=float, default=0.72)
    parser.add_argument("--subset-overlap", type=float, default=0.85)
    parser.add_argument("--candidate-limit", type=int, default=40, help="maximum candidates to write; use 0 for no cap")
    parser.add_argument("--min-roots", type=int, default=3)
    parser.add_argument("--min-ayahs", type=int, default=3)
    return parser.parse_args()


def main() -> None:
    print(json.dumps(build(parse_args()), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
