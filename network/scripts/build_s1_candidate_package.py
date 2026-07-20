#!/usr/bin/env python3
"""Build consolidated S1 semantic-network candidate packages.

This script reads the S1 graph artifacts from quran-slm and writes a candidate
package into this repository. It does not mutate quran-slm.
"""

from __future__ import annotations

import argparse
import collections
import csv
import gzip
import json
import math
from pathlib import Path
from typing import Any, Iterable


Occurrence = tuple[int, int, str, str]
Position = tuple[int, int, int, int]


def read_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")))
            handle.write("\n")


def gzip_copy(path: Path) -> None:
    data = path.read_bytes()
    with gzip.open(path.with_suffix(path.suffix + ".gz"), "wb") as handle:
        handle.write(data)


def load_branches(source_repo: Path) -> tuple[dict[str, dict[str, str]], collections.Counter[str]]:
    branches: dict[str, dict[str, str]] = {}
    root_branch_count: collections.Counter[str] = collections.Counter()
    path = source_repo / "resources/derived/s1_branches_ar.tsv"
    with path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            branches[row["node_id"]] = row
            root_branch_count[row["surface_root"]] += 1
    return branches, root_branch_count


def load_edge_scores(source_repo: Path) -> dict[str, dict[str, Any]]:
    """Return compact score/evidence records keyed by semantic edge id."""

    path = source_repo / "artifacts/s1_ar3_v1/scores/selected_pair_evidence.jsonl"
    scores: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return scores

    for row in read_jsonl(path):
        edge_id = row["edge_id"]
        ranks: list[int] = []
        span_pairs: list[dict[str, Any]] = []
        for direction in ("left_to_right", "right_to_left"):
            direction_record = (row.get("evidence") or {}).get(direction) or {}
            score = direction_record.get("score") or {}
            rank = score.get("combined_rank")
            if rank is not None:
                ranks.append(int(rank))

            source_match = direction_record.get("dense_source_match") or {}
            if source_match:
                span_pairs.append(
                    {
                        "direction": direction,
                        "left_text": source_match.get("left_text"),
                        "right_text": source_match.get("right_text"),
                        "similarity": source_match.get("similarity"),
                        "left_families": source_match.get("left_source_families"),
                        "right_families": source_match.get("right_source_families"),
                    }
                )

        scores[edge_id] = {
            "combined_ranks": ranks,
            "best_combined_rank": min(ranks) if ranks else None,
            "mutual_combined_rank_max": max(ranks) if len(ranks) == 2 else None,
            "evidence_span_pairs": span_pairs[:2],
        }
    return scores


def edge_passes(
    edge_id: str,
    scores: dict[str, dict[str, Any]],
    *,
    best_rank_threshold: int,
    mutual_rank_threshold: int,
) -> bool:
    score = scores.get(edge_id)
    if not score:
        return False

    best = score.get("best_combined_rank")
    mutual_max = score.get("mutual_combined_rank_max")
    return (
        best is not None
        and int(best) <= best_rank_threshold
    ) or (
        mutual_max is not None
        and int(mutual_max) <= mutual_rank_threshold
    )


def load_graph(
    source_repo: Path,
    scores: dict[str, dict[str, Any]],
    *,
    best_rank_threshold: int,
    mutual_rank_threshold: int,
) -> tuple[
    dict[Occurrence, list[Occurrence]],
    dict[Occurrence, tuple[str, str, Position]],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
]:
    """Load the filtered occurrence graph.

    Returns:
        adjacency, occurrence node metadata, all edge groups, kept edge groups.
    """

    adjacency: dict[Occurrence, list[Occurrence]] = collections.defaultdict(list)
    nodes: dict[Occurrence, tuple[str, str, Position]] = {}
    all_edge_groups: dict[str, dict[str, Any]] = {}
    kept_edge_groups: dict[str, dict[str, Any]] = {}

    path = source_repo / "artifacts/s1_ar3_v1/graphs/occurrence_edges.jsonl"
    for edge in read_jsonl(path):
        edge_id = edge["semantic_edge_id"]
        source = tuple(edge["source_occurrence_id"])
        target = tuple(edge["target_occurrence_id"])
        source_pos = tuple(edge["source_position"])
        target_pos = tuple(edge["target_position"])

        group = all_edge_groups.setdefault(
            edge_id,
            {
                "semantic_edge_id": edge_id,
                "source_node_id": edge["source_node_id"],
                "target_node_id": edge["target_node_id"],
                "source_root": edge["source_root_key"],
                "target_root": edge["target_root_key"],
                "occurrence_count": 0,
                "ayah_pairs": set(),
                "ayahs": set(),
            },
        )
        group["occurrence_count"] += 1
        group["ayah_pairs"].add((source_pos[1], target_pos[1]))
        group["ayahs"].update((source_pos[1], target_pos[1]))

        if not edge_passes(
            edge_id,
            scores,
            best_rank_threshold=best_rank_threshold,
            mutual_rank_threshold=mutual_rank_threshold,
        ):
            continue

        kept = kept_edge_groups.setdefault(
            edge_id,
            {
                "semantic_edge_id": edge_id,
                "source_node_id": edge["source_node_id"],
                "target_node_id": edge["target_node_id"],
                "source_root": edge["source_root_key"],
                "target_root": edge["target_root_key"],
                "occurrence_count": 0,
                "ayah_pairs": set(),
                "ayahs": set(),
            },
        )
        kept["occurrence_count"] += 1
        kept["ayah_pairs"].add((source_pos[1], target_pos[1]))
        kept["ayahs"].update((source_pos[1], target_pos[1]))

        nodes[source] = (edge["source_node_id"], edge["source_root_key"], source_pos)
        nodes[target] = (edge["target_node_id"], edge["target_root_key"], target_pos)
        adjacency[source].append(target)

    for source, targets in adjacency.items():
        targets.sort(key=lambda occurrence: (nodes[occurrence][2], nodes[occurrence][0]))

    return adjacency, nodes, all_edge_groups, kept_edge_groups


def path_record(
    path: list[Occurrence],
    nodes: dict[Occurrence, tuple[str, str, Position]],
    branches: dict[str, dict[str, str]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for occurrence in path:
        node_id, root, position = nodes[occurrence]
        branch = branches[node_id]
        rows.append(
            {
                "ayah": position[1],
                "position": list(position),
                "node_id": node_id,
                "root": root,
                "branch_id": branch["branch_id"],
                "branch_image_ar": branch["branch_image_ar"],
                "what_is_ar": branch["what_is_ar"],
                "source_phrase_ar": branch.get("source_phrase_ar"),
            }
        )
    return rows


def build_path_groups(
    adjacency: dict[Occurrence, list[Occurrence]],
    nodes: dict[Occurrence, tuple[str, str, Position]],
    *,
    min_ayahs: int,
    max_len: int,
) -> tuple[
    collections.Counter[tuple[str, ...]],
    dict[tuple[str, ...], list[Occurrence]],
    dict[tuple[str, ...], set[int]],
    collections.Counter[tuple[str, ...]],
    dict[tuple[str, ...], list[Occurrence]],
    dict[tuple[str, ...], set[int]],
]:
    """Dynamic-program ordered root-signature and root-set groups."""

    order = sorted(nodes, key=lambda occurrence: (nodes[occurrence][2], nodes[occurrence][0]))
    state: dict[
        Occurrence,
        dict[tuple[tuple[str, ...], frozenset[int]], tuple[int, list[Occurrence]]],
    ] = {
        occurrence: {
            ((nodes[occurrence][1],), frozenset([nodes[occurrence][2][1]])): (
                1,
                [occurrence],
            )
        }
        for occurrence in order
    }

    root_sig_counts: collections.Counter[tuple[str, ...]] = collections.Counter()
    root_sig_rep: dict[tuple[str, ...], list[Occurrence]] = {}
    root_sig_ayahs: dict[tuple[str, ...], set[int]] = {}
    root_set_counts: collections.Counter[tuple[str, ...]] = collections.Counter()
    root_set_rep: dict[tuple[str, ...], list[Occurrence]] = {}
    root_set_ayahs: dict[tuple[str, ...], set[int]] = {}

    for occurrence in order:
        for (signature, ayahs), (count, path) in list(state.get(occurrence, {}).items()):
            if len(signature) >= 3 and len(ayahs) >= min_ayahs:
                root_sig_counts[signature] += count
                root_sig_rep.setdefault(signature, path)
                root_sig_ayahs.setdefault(signature, set()).update(ayahs)

                root_set = tuple(sorted(set(signature)))
                root_set_counts[root_set] += count
                root_set_rep.setdefault(root_set, path)
                root_set_ayahs.setdefault(root_set, set()).update(ayahs)

            if len(signature) >= max_len:
                continue

            used_node_ids = {nodes[item][0] for item in path}
            for target in adjacency.get(occurrence, []):
                target_node_id, target_root, target_position = nodes[target]
                if target_node_id in used_node_ids:
                    continue

                next_signature = signature + (target_root,)
                next_ayahs = frozenset(set(ayahs) | {target_position[1]})
                next_key = (next_signature, next_ayahs)
                target_state = state.setdefault(target, {})
                if next_key in target_state:
                    old_count, old_path = target_state[next_key]
                    target_state[next_key] = (old_count + count, old_path)
                else:
                    target_state[next_key] = (count, path + [target])

    return (
        root_sig_counts,
        root_sig_rep,
        root_sig_ayahs,
        root_set_counts,
        root_set_rep,
        root_set_ayahs,
    )


def jaccard(left: Iterable[str], right: Iterable[str]) -> float:
    left_set = set(left)
    right_set = set(right)
    return len(left_set & right_set) / len(left_set | right_set)


def candidate_score(
    signature: tuple[str, ...],
    count: int,
    root_branch_count: collections.Counter[str],
) -> float:
    roots = set(signature)
    rarity = sum(1.0 / root_branch_count[root] for root in roots)
    return (
        3.0 * len(roots)
        + 0.75 * len(signature)
        + 1.8 * rarity
        + 0.6 * math.log10(count + 1)
    )


def select_path_families(
    root_sig_counts: collections.Counter[tuple[str, ...]],
    root_branch_count: collections.Counter[str],
    *,
    cap: int,
    diversity_first_pass: int,
    per_root_guarantee: int,
) -> list[tuple[str, ...]]:
    ranked = sorted(
        root_sig_counts,
        key=lambda signature: (
            -candidate_score(signature, root_sig_counts[signature], root_branch_count),
            -root_sig_counts[signature],
            signature,
        ),
    )

    selected: list[tuple[str, ...]] = []
    selected_sets: list[set[str]] = []

    for signature in ranked:
        if len(selected) >= diversity_first_pass:
            break
        if root_sig_counts[signature] < 50 and len(set(signature)) < 5:
            continue
        root_set = set(signature)
        if all(jaccard(root_set, previous) < 0.82 for previous in selected_sets):
            selected.append(signature)
            selected_sets.append(root_set)

    for root in sorted(root_branch_count):
        added = 0
        for signature in ranked:
            if root not in signature or signature in selected:
                continue
            selected.append(signature)
            added += 1
            if added >= per_root_guarantee:
                break

    for signature in ranked:
        if len(selected) >= cap:
            break
        if signature not in selected and len(set(signature)) >= 4:
            selected.append(signature)

    return selected[:cap]


def select_channel_seeds(
    root_set_counts: collections.Counter[tuple[str, ...]],
    root_branch_count: collections.Counter[str],
    *,
    cap: int,
) -> list[tuple[str, ...]]:
    ranked = sorted(
        root_set_counts,
        key=lambda root_set: (
            -(
                3.0 * len(root_set)
                + math.log10(root_set_counts[root_set] + 1)
                + sum(1.0 / root_branch_count[root] for root in root_set)
            ),
            -root_set_counts[root_set],
            root_set,
        ),
    )

    selected: list[tuple[str, ...]] = []
    selected_sets: list[set[str]] = []
    for root_set in ranked:
        if len(selected) >= cap:
            break
        if all(jaccard(root_set, previous) < 0.78 for previous in selected_sets) or len(
            selected
        ) < 40:
            selected.append(root_set)
            selected_sets.append(set(root_set))
    return selected


def build_package(args: argparse.Namespace) -> dict[str, Any]:
    source_repo = Path(args.source_repo)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    branches, root_branch_count = load_branches(source_repo)
    scores = load_edge_scores(source_repo)
    adjacency, nodes, all_edge_groups, kept_edge_groups = load_graph(
        source_repo,
        scores,
        best_rank_threshold=args.best_rank_threshold,
        mutual_rank_threshold=args.mutual_rank_threshold,
    )

    (
        root_sig_counts,
        root_sig_rep,
        root_sig_ayahs,
        root_set_counts,
        root_set_rep,
        root_set_ayahs,
    ) = build_path_groups(
        adjacency,
        nodes,
        min_ayahs=args.min_ayahs,
        max_len=args.max_len,
    )

    selected_path_sigs = select_path_families(
        root_sig_counts,
        root_branch_count,
        cap=args.path_family_cap,
        diversity_first_pass=min(args.path_family_cap, args.diversity_first_pass),
        per_root_guarantee=args.per_root_guarantee,
    )
    selected_channel_sets = select_channel_seeds(
        root_set_counts,
        root_branch_count,
        cap=args.channel_seed_cap,
    )

    atomic_rows: list[dict[str, Any]] = []
    for index, (edge_id, group) in enumerate(sorted(kept_edge_groups.items()), start=1):
        source_branch = branches[group["source_node_id"]]
        target_branch = branches[group["target_node_id"]]
        score = scores.get(edge_id, {})
        atomic_rows.append(
            {
                "candidate_id": f"AR{index:04d}",
                "type": "atomic_branch_relation_inventory",
                "semantic_edge_id": edge_id,
                "source": {
                    "node_id": group["source_node_id"],
                    "root": group["source_root"],
                    "branch_id": source_branch["branch_id"],
                    "branch_image_ar": source_branch["branch_image_ar"],
                    "what_is_ar": source_branch["what_is_ar"],
                },
                "target": {
                    "node_id": group["target_node_id"],
                    "root": group["target_root"],
                    "branch_id": target_branch["branch_id"],
                    "branch_image_ar": target_branch["branch_image_ar"],
                    "what_is_ar": target_branch["what_is_ar"],
                },
                "occurrence_count": group["occurrence_count"],
                "ayah_pairs": [list(pair) for pair in sorted(group["ayah_pairs"])],
                "distinct_ayahs_across_occurrences": sorted(group["ayahs"]),
                "best_combined_rank": score.get("best_combined_rank"),
                "mutual_combined_rank_max": score.get("mutual_combined_rank_max"),
                "evidence_span_pairs": score.get("evidence_span_pairs", []),
                "review_use": "supporting evidence inventory; not a standalone chain finding",
            }
        )

    path_rows: list[dict[str, Any]] = []
    for index, signature in enumerate(selected_path_sigs, start=1):
        count = root_sig_counts[signature]
        path_rows.append(
            {
                "candidate_id": f"PF{index:04d}",
                "type": "ordered_path_family",
                "ordered_root_signature": list(signature),
                "root_set": sorted(set(signature)),
                "path_count_exact_dp": count,
                "length": len(signature),
                "distinct_root_count": len(set(signature)),
                "distinct_ayahs_union": sorted(root_sig_ayahs[signature]),
                "score": round(candidate_score(signature, count, root_branch_count), 4),
                "representative_path": path_record(root_sig_rep[signature], nodes, branches),
                "review_questions": [
                    "Does this configured-ayah-span chain form a coherent finding/channel?",
                    "Should it merge with other path families?",
                    "Label PRIMARY / INTERESTING / STRUCTURAL / WEAK / REJECT / SPLIT / MERGE.",
                ],
            }
        )

    channel_rows: list[dict[str, Any]] = []
    for index, root_set in enumerate(selected_channel_sets, start=1):
        channel_rows.append(
            {
                "candidate_id": f"CS{index:04d}",
                "type": "root_set_channel_seed",
                "root_set": list(root_set),
                "path_count_exact_dp": root_set_counts[root_set],
                "distinct_root_count": len(root_set),
                "distinct_ayahs_union": sorted(root_set_ayahs[root_set]),
                "representative_path": path_record(root_set_rep[root_set], nodes, branches),
                "review_use": "high-level grouping seed for merge/split/channel review",
            }
        )

    write_jsonl(output_dir / "atomic_relations_inventory.jsonl", atomic_rows)
    write_jsonl(output_dir / "path_family_candidates.jsonl", path_rows)
    write_jsonl(output_dir / "channel_seed_candidates.jsonl", channel_rows)

    summary = {
        "package_version": "semantic_candidate_package_v1",
        "source_repo": str(source_repo),
        "configuration": {
            "min_ayahs": args.min_ayahs,
            "max_len": args.max_len,
            "best_rank_threshold": args.best_rank_threshold,
            "mutual_rank_threshold": args.mutual_rank_threshold,
            "path_family_cap": args.path_family_cap,
            "channel_seed_cap": args.channel_seed_cap,
            "diversity_first_pass": args.diversity_first_pass,
            "per_root_guarantee": args.per_root_guarantee,
        },
        "graph_counts": {
            "filtered_branch_occurrence_nodes": len(nodes),
            "filtered_occurrence_edges": sum(len(targets) for targets in adjacency.values()),
            "all_semantic_edges_in_occurrence_graph": len(all_edge_groups),
            "kept_semantic_edges": len(kept_edge_groups),
        },
        "raw_group_space_after_filters": {
            "ordered_root_signature_groups_len_3_to_max": len(root_sig_counts),
            "root_set_groups_len_3_to_max": len(root_set_counts),
            "ordered_path_count_exact_dp": sum(root_sig_counts.values()),
        },
        "package_counts": {
            "atomic_relation_inventory": len(atomic_rows),
            "ordered_path_family_review_candidates": len(path_rows),
            "root_set_channel_seed_candidates": len(channel_rows),
        },
        "selection_policy": {
            "edge_filter": "keep if best combined_rank <= threshold OR mutual combined_rank <= threshold",
            "path_families": "capped diversified ordered root signatures with per-root coverage",
            "channel_seeds": "capped diversified unordered root sets",
            "not_claimed": "candidate package, not accepted findings",
        },
    }
    (output_dir / "package_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (output_dir / "README.md").write_text(
        "# Candidate package\n\n"
        "Generated by `network/scripts/build_s1_candidate_package.py`.\n\n"
        "The package is a review input, not a final finding set.\n",
        encoding="utf-8",
    )

    if args.gzip:
        for name in (
            "atomic_relations_inventory.jsonl",
            "path_family_candidates.jsonl",
            "channel_seed_candidates.jsonl",
            "package_summary.json",
            "README.md",
        ):
            gzip_copy(output_dir / name)

    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-repo", default="../quran-slm")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--min-ayahs", type=int, default=5)
    parser.add_argument("--max-len", type=int, default=7)
    parser.add_argument("--best-rank-threshold", type=int, default=8)
    parser.add_argument("--mutual-rank-threshold", type=int, default=12)
    parser.add_argument("--path-family-cap", type=int, default=1000)
    parser.add_argument("--channel-seed-cap", type=int, default=200)
    parser.add_argument("--diversity-first-pass", type=int, default=350)
    parser.add_argument("--per-root-guarantee", type=int, default=12)
    parser.add_argument("--gzip", action=argparse.BooleanOptionalAction, default=True)
    return parser.parse_args()


def main() -> None:
    summary = build_package(parse_args())
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
