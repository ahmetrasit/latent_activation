#!/usr/bin/env python3
"""Generate pericope-scoped Hermetic Focus Trace packets in batch."""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from pathlib import Path
from typing import Any, Iterable

import numpy as np

WORKFLOW_ROOT = Path(__file__).resolve().parents[1]
LATENT_ROOT = WORKFLOW_ROOT.parent
PROJECTS_ROOT = LATENT_ROOT.parent
QURAN_SLM_ROOT = PROJECTS_ROOT / "quran-slm"

if str(WORKFLOW_ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(WORKFLOW_ROOT / "scripts"))
if str(QURAN_SLM_ROOT) not in sys.path:
    sys.path.insert(0, str(QURAN_SLM_ROOT))

import build_focus_trace_packet as packet_builder
from build_focus_trace_packet import (  # noqa: E402
    PROTOCOL,
    ROOTLESS_REASON,
    first_seen_roots,
    focus_branch,
    compact_branch,
    out_of_window_branch,
    occurrence_phrase,
    refs_by_root,
    root_mapping_summary,
    source_phrases,
)
from build_packets import canonical_arabic, ordered_unique, sha256, split_semicolon  # noqa: E402
from experiments.ayah_branch_potential.branch_potential import (  # noqa: E402
    load_production_engine,
)
from validate_focus_trace import validate_packet  # noqa: E402
from build_pericope_focus_trace_packet import (  # noqa: E402
    PROTOCOL as LEAN_PACKET_PROTOCOL,
    lean_packet,
    validate_lean_packet,
)
from quran_slm.corpus_underlay import RANK_DTYPE, symmetric_rrf_row  # noqa: E402


DEFAULT_PERICOPES = (
    PROJECTS_ROOT
    / "quran-data"
    / "data"
    / "analysis"
    / "channels"
    / "network-v3"
    / "pericopes"
    / "surah_pericopes.jsonl"
)
DEFAULT_SEMANTIC_DIR = QURAN_SLM_ROOT / "artifacts" / "ayah_semantic_map" / "v1"
DEFAULT_SLM_OUTPUTS = QURAN_SLM_ROOT / "inter-ayah" / "outputs"
DEFAULT_REPORT = WORKFLOW_ROOT / "runs" / "pericope_packet_size_report.json"
PACKET_SIZE_REPORT_BYTES = 350 * 1024
LARGE_PACKET_BYTES = 500 * 1024
S2_FRAGMENTS = (
    (1, 7, "Guidance and initial human types"),
    (8, 20, "Hypocrisy and warning parables"),
    (21, 29, "Worship and creation signs"),
    (30, 39, "Adam, naming, and descent"),
    (40, 46, "Israelite covenant opening"),
    (47, 53, "Deliverance and the book"),
    (54, 61, "Calf, repentance, and provision"),
    (62, 66, "Covenant breaches"),
    (67, 74, "The cow and disclosed killing"),
    (75, 82, "Distortion and false security"),
    (83, 86, "Broken pledges and exchange"),
    (87, 96, "Rejected messengers"),
    (97, 103, "Gabriel, scripture, and magic"),
    (104, 110, "Revelation etiquette and forgiveness"),
    (111, 121, "Communal claims and direction"),
    (122, 129, "Abraham's covenant"),
    (130, 141, "Abraham's legacy and community"),
    (142, 147, "Qiblah turn"),
    (148, 152, "Direction and remembrance"),
    (153, 157, "Patience and trial"),
    (158, 162, "Rites and concealment"),
    (163, 167, "Unity and signs"),
    (168, 177, "Consumption, following, and righteousness"),
    (178, 182, "Retaliation and bequests"),
    (183, 187, "Fasting"),
    (188, 203, "Property, moons, fighting, and hajj"),
    (204, 210, "Sincerity and corrupt speech"),
    (211, 220, "Struggle, questioning, and welfare"),
    (221, 223, "Marriage boundaries"),
    (224, 230, "Oaths and divorce limits"),
    (231, 242, "Family duties after divorce"),
    (243, 245, "Death, revival, and loan"),
    (246, 253, "Kingship and messengers"),
    (254, 257, "Divine sovereignty"),
    (258, 260, "Life, death, and proof"),
    (261, 266, "Spending parables"),
    (267, 274, "Charity and hidden giving"),
    (275, 281, "Usury and final return"),
    (282, 283, "Debt and testimony"),
    (284, 286, "Final faith and supplication"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah-start", type=int, default=2)
    parser.add_argument("--surah-end", type=int, default=79)
    parser.add_argument(
        "--surah-list",
        default="",
        help="optional comma/range list of surahs, e.g. 44,49,61-64",
    )
    parser.add_argument(
        "--window-mode",
        choices=["pericope", "surah"],
        default="pericope",
        help="generate reference pericope windows or one whole-surah window per listed surah",
    )
    parser.add_argument("--pericopes", type=Path, default=DEFAULT_PERICOPES)
    parser.add_argument("--semantic-dir", type=Path, default=DEFAULT_SEMANTIC_DIR)
    parser.add_argument("--slm-outputs", type=Path, default=DEFAULT_SLM_OUTPUTS)
    parser.add_argument("--output-root", type=Path, default=WORKFLOW_ROOT / "runs")
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--validate", action="store_true")
    parser.add_argument(
        "--packet-schema",
        choices=["pericope-lean", "rich"],
        default="pericope-lean",
        help="emit lean pericope packets by default; rich preserves the older full packet shape",
    )
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--no-slm", action="store_true")
    parser.add_argument("--no-neo", action="store_true")
    parser.add_argument("--neo-top-k", type=int, default=20)
    parser.add_argument("--branch-potential-roots-per-ayah", type=int, default=2)
    parser.add_argument(
        "--fragment-dense-pericopes",
        action="store_true",
        help=(
            "split dense reference pericopes into smaller coordinator windows; "
            "without this, each source pericope is emitted as one window"
        ),
    )
    parser.add_argument("--dense-fragment-min-length", type=int, default=26)
    parser.add_argument("--dense-fragment-target-length", type=int, default=18)
    args = parser.parse_args()
    try:
        explicit_surahs = parse_surah_list(args.surah_list)
    except ValueError as error:
        parser.error(str(error))
    if args.window_mode == "surah" and not explicit_surahs:
        parser.error("--window-mode surah requires --surah-list")
    if explicit_surahs:
        args.surah_start = min(explicit_surahs)
        args.surah_end = max(explicit_surahs)
    args.explicit_surahs = explicit_surahs
    args.requested_surahs = (
        explicit_surahs
        if explicit_surahs
        else list(range(args.surah_start, args.surah_end + 1))
    )
    return args


def parse_surah_list(raw: str) -> list[int]:
    if not raw.strip():
        return []
    surahs: list[int] = []
    for part in raw.split(","):
        item = part.strip()
        if not item:
            continue
        if "-" in item:
            start_raw, end_raw = item.split("-", 1)
            start = int(start_raw)
            end = int(end_raw)
            if end < start:
                raise ValueError(f"invalid descending surah range: {item}")
            surahs.extend(range(start, end + 1))
        else:
            surahs.append(int(item))
    unique: list[int] = []
    seen: set[int] = set()
    for surah in surahs:
        if surah not in seen:
            seen.add(surah)
            unique.append(surah)
    return unique


def surah_of(ref: str) -> int:
    return int(ref.split(":", 1)[0])


def ayah_of(ref: str) -> int:
    return int(ref.split(":", 1)[1])


def ordered_refs(surah: int, start: int, end: int) -> list[str]:
    return [f"{surah}:{ayah}" for ayah in range(start, end + 1)]


def relpath(path: Path) -> str:
    try:
        return os.path.relpath(path.resolve(), LATENT_ROOT)
    except ValueError:
        return str(path)


def load_pericopes(
    path: Path,
    surah_start: int,
    surah_end: int,
    allowed_surahs: set[int] | None = None,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        row = json.loads(line)
        row["_source_line"] = line_number
        surah = int(row["surah"])
        start = int(row["ayah_from"])
        end = int(row["ayah_to"])
        if end < start:
            raise ValueError(
                f"invalid pericope ayah range at {path}:{line_number}: {surah}:{start}-{end}"
            )
        if allowed_surahs is not None:
            keep = surah in allowed_surahs
        else:
            keep = surah_start <= surah <= surah_end
        if keep:
            rows.append(row)
    return rows


def synthetic_surah_windows(surahs: list[int]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for surah in surahs:
        count = len(packet_builder.numbered_refs_for_surah(packet_builder.DEFAULT_QURAN_DIR, surah))
        rows.append(
            {
                "surah": surah,
                "pericope": None,
                "ayah_from": 1,
                "ayah_to": count,
                "label": "Whole surah window",
                "_source_line": None,
                "_window_source": "surah_window_explicit",
            }
        )
    return rows


def fragment_pericope(row: dict[str, Any], min_length: int, target_length: int) -> list[dict[str, Any]]:
    surah = int(row["surah"])
    start = int(row["ayah_from"])
    end = int(row["ayah_to"])
    if surah == 2:
        fragments = [
            (frag_start, frag_end, label)
            for frag_start, frag_end, label in S2_FRAGMENTS
            if start <= frag_start and frag_end <= end
        ]
        if fragments and fragments[0][0] == start and fragments[-1][1] == end:
            return [
                {
                    "ayah_from": frag_start,
                    "ayah_to": frag_end,
                    "label": label,
                    "fragment_index": index,
                    "fragment_count": len(fragments),
                    "fragment_policy": "s2_manual_dense_discourse",
                }
                for index, (frag_start, frag_end, label) in enumerate(fragments, start=1)
            ]
    length = end - start + 1
    if length < min_length:
        return [
            {
                "ayah_from": start,
                "ayah_to": end,
                "label": row["label"],
                "fragment_index": 1,
                "fragment_count": 1,
                "fragment_policy": "reference_pericope",
            }
        ]
    count = max(2, (length + target_length - 1) // target_length)
    base = length // count
    remainder = length % count
    fragments = []
    cursor = start
    for index in range(1, count + 1):
        size = base + (1 if index <= remainder else 0)
        frag_start = cursor
        frag_end = cursor + size - 1
        cursor = frag_end + 1
        fragments.append(
            {
                "ayah_from": frag_start,
                "ayah_to": frag_end,
                "label": f"{row['label']} [{frag_start}-{frag_end}]",
                "fragment_index": index,
                "fragment_count": count,
                "fragment_policy": "long_dense_reference_pericope_split",
            }
        )
    return fragments


def reference_pericope_fragment(row: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "ayah_from": int(row["ayah_from"]),
            "ayah_to": int(row["ayah_to"]),
            "label": row["label"],
            "fragment_index": 1,
            "fragment_count": 1,
            "fragment_policy": "reference_pericope",
        }
    ]


def fragments_for_parent(
    args: argparse.Namespace,
    parent: dict[str, Any],
) -> list[dict[str, Any]]:
    if args.window_mode == "surah":
        return [
            {
                "ayah_from": parent["ayah_from"],
                "ayah_to": parent["ayah_to"],
                "label": parent["label"],
                "fragment_index": 1,
                "fragment_count": 1,
                "fragment_policy": "whole_surah_window",
            }
        ]
    if args.fragment_dense_pericopes:
        return fragment_pericope(
            parent,
            args.dense_fragment_min_length,
            args.dense_fragment_target_length,
        )
    return reference_pericope_fragment(parent)


def planned_windows(
    args: argparse.Namespace,
    pericopes: list[dict[str, Any]],
) -> list[tuple[dict[str, Any], dict[str, Any], list[str]]]:
    jobs: list[tuple[dict[str, Any], dict[str, Any], list[str]]] = []
    seen_focus_refs: dict[str, dict[str, Any]] = {}
    for parent in pericopes:
        surah = int(parent["surah"])
        max_ayah = len(packet_builder.numbered_refs_for_surah(packet_builder.DEFAULT_QURAN_DIR, surah))
        for fragment in fragments_for_parent(args, parent):
            start = int(fragment["ayah_from"])
            end = int(fragment["ayah_to"])
            if start < 1 or end > max_ayah or end < start:
                raise ValueError(
                    f"invalid planned window for S{surah}: {start}-{end}; surah has {max_ayah} ayat"
                )
            window = ordered_refs(surah, start, end)
            descriptor = {
                "surah": surah,
                "source_line": parent.get("_source_line"),
                "parent": f"{parent['ayah_from']}-{parent['ayah_to']}",
                "fragment": f"{start}-{end}",
                "fragment_policy": fragment["fragment_policy"],
            }
            for ref in window:
                previous = seen_focus_refs.get(ref)
                if previous is not None:
                    raise ValueError(
                        "overlapping planned packet windows for "
                        f"{ref}: {previous} and {descriptor}"
                    )
                seen_focus_refs[ref] = descriptor
            jobs.append((parent, fragment, window))
    return jobs


def load_quran_texts(quran_dir: Path, surahs: Iterable[int]) -> dict[str, dict[str, Any]]:
    texts: dict[str, dict[str, Any]] = {}
    for surah in surahs:
        ayat = packet_builder.load_quran_surah(quran_dir, surah)
        for ayah, text in ayat.items():
            texts[f"{surah}:{ayah}"] = {
                "ref": f"{surah}:{ayah}",
                "text_ar": text,
                "text_norm_ar": canonical_arabic(text),
                "root_sequence": [],
                "root_occurrences": [],
                "rootless": True,
                "rootless_reason": ROOTLESS_REASON,
            }
    return texts


def load_qac_ayat(qac_path: Path, quran_texts: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    rows_by_ref: dict[str, list[dict[str, str]]] = {}
    wanted = set(quran_texts)
    with qac_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            ref = row["ayah_ref"]
            if ref in wanted:
                rows_by_ref.setdefault(ref, []).append(row)
    ayat = dict(quran_texts)
    for ref, rows in rows_by_ref.items():
        first = rows[0]
        sequence = split_semicolon(first["ayah_root_sequence"])
        row_by_root = {row["root_norm"]: row for row in rows}
        roots = ordered_unique(sequence)
        root_occurrences = []
        for root in roots:
            row = row_by_root[root]
            root_occurrences.append(
                {
                    "root": root,
                    "occurrence_count": int(row["occurrence_count"]),
                    "word_indices": split_semicolon(row["word_indices"]),
                    "surfaces_ar": split_semicolon(row["surfaces_ar"]),
                    "lemmas_ar": split_semicolon(row["lemmas_ar"]),
                    "pos_tags": split_semicolon(row["pos_tags"]),
                }
            )
        ayat[ref] = {
            "ref": ref,
            "text_ar": first["ayah_text_ar"],
            "text_norm_ar": first["ayah_text_norm_ar"],
            "root_sequence": sequence,
            "root_occurrences": root_occurrences,
        }
    return ayat


def roots_for_all_ayat(ayat_by_ref: dict[str, dict[str, Any]]) -> list[str]:
    return ordered_unique(
        occurrence["root"]
        for ayah in ayat_by_ref.values()
        for occurrence in ayah["root_occurrences"]
    )


def load_semantic_nodes(semantic_dir: Path) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    nodes: list[dict[str, Any]] = []
    by_ref: dict[str, dict[str, Any]] = {}
    with (semantic_dir / "nodes.tsv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            item = {
                "global_index": int(row["global_index"]),
                "node_id": row["node_id"],
                "surah": int(row["surah"]),
                "ayah": int(row["ayah"]),
                "ayah_ref": row["ayah_ref"],
                "repeat_group_id": row["repeat_group_id"],
            }
            nodes.append(item)
            by_ref[item["ayah_ref"]] = item
    return nodes, by_ref


def parse_slm_rows(path: Path) -> list[tuple[str, str]]:
    if not path.is_file():
        return []
    rows: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        parts = line.split("\t", 2)
        if len(parts) != 3:
            continue
        label, ref, _note = [part.strip() for part in parts]
        rows.append((label, ref))
    return rows


class BatchContext:
    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args
        self.quran_texts = load_quran_texts(
            packet_builder.DEFAULT_QURAN_DIR,
            args.requested_surahs,
        )
        self.ayat_by_ref = load_qac_ayat(packet_builder.DEFAULT_QAC, self.quran_texts)
        self.all_roots = roots_for_all_ayat(self.ayat_by_ref)
        self.root_mappings = packet_builder.load_root_mappings(
            packet_builder.DEFAULT_QAC_FURUQ_ROOT_MAP,
            self.all_roots,
        )
        (
            self.branches,
            self.missing_roots,
            self.missing_mapped_targets,
        ) = packet_builder.load_branches_for_mapped_roots(
            packet_builder.DEFAULT_BRANCH_DB,
            self.root_mappings,
        )
        self.missing_root_set = set(self.missing_roots)
        self.resource_hashes = {
            relpath(packet_builder.DEFAULT_QAC): sha256(packet_builder.DEFAULT_QAC),
            relpath(packet_builder.DEFAULT_BRANCH_DB): sha256(packet_builder.DEFAULT_BRANCH_DB),
            relpath(packet_builder.DEFAULT_QAC_FURUQ_ROOT_MAP): sha256(
                packet_builder.DEFAULT_QAC_FURUQ_ROOT_MAP
            ),
        }
        self.quran_hashes = {
            surah: sha256(packet_builder.quran_surah_path(packet_builder.DEFAULT_QURAN_DIR, surah))
            for surah in args.requested_surahs
        }
        self.slm_cache: dict[str, list[tuple[str, str]]] = {}
        self.nodes: list[dict[str, Any]] = []
        self.node_by_ref: dict[str, dict[str, Any]] = {}
        self.neo_ranks: Any | None = None
        self.branch_engine: Any | None = None
        if not args.no_neo:
            self.nodes, self.node_by_ref = load_semantic_nodes(args.semantic_dir)
            self.neo_ranks = np.memmap(
                args.semantic_dir / "neo_raw_directional_rank.u16le",
                mode="r",
                dtype=RANK_DTYPE,
                shape=(len(self.nodes), len(self.nodes)),
            )
            self.branch_engine = load_production_engine(validate_rank_invariants=False)

    def close(self) -> None:
        if self.branch_engine is not None:
            self.branch_engine.close()

    def ensure_roots(self, roots: Iterable[str]) -> None:
        missing = [root for root in ordered_unique(roots) if root not in self.root_mappings]
        if not missing:
            return
        mappings = packet_builder.load_root_mappings(
            packet_builder.DEFAULT_QAC_FURUQ_ROOT_MAP,
            missing,
        )
        branches, missing_roots, missing_targets = packet_builder.load_branches_for_mapped_roots(
            packet_builder.DEFAULT_BRANCH_DB,
            mappings,
        )
        self.root_mappings.update(mappings)
        self.branches.update(branches)
        self.missing_roots.extend(root for root in missing_roots if root not in self.missing_root_set)
        self.missing_root_set.update(missing_roots)
        self.missing_mapped_targets.extend(missing_targets)

    def slm_rows(self, focus_ref: str) -> list[tuple[str, str]]:
        cached = self.slm_cache.get(focus_ref)
        if cached is None:
            cached = parse_slm_rows(
                self.args.slm_outputs / f"focus_{focus_ref.replace(':', '_')}_cutoff_100.tsv"
            )
            self.slm_cache[focus_ref] = cached
        return cached

    def branch_cues(
        self,
        roots: Iterable[str],
        ayat: list[dict[str, Any]],
        mode: str = "branch_image_ar",
    ) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        roots = ordered_unique(roots)
        self.ensure_roots(roots)
        refs_for_root = refs_by_root(ayat)
        cues: list[dict[str, Any]] = []
        unmatched: list[dict[str, Any]] = []
        for root in roots:
            mapping = self.root_mappings[root]
            root_branches = self.branches.get(root, [])
            if not root_branches:
                unmatched.append(root_mapping_summary(mapping))
                continue
            cues.append(
                {
                    "root": root,
                    "root_mapping": root_mapping_summary(mapping),
                    "source_refs": refs_for_root.get(root, []),
                    "branch_inventory_mode": mode,
                    "orientation_only": True,
                    "citable": False,
                    "branches": [
                        out_of_window_branch(branch, mode)
                        for branch in root_branches
                    ],
                }
            )
        return cues, unmatched

    def selected_neo_refs(
        self,
        focus_ref: str,
        window: set[str],
        ranking_source_refs: list[str],
    ) -> tuple[list[str], list[str], str]:
        assert self.neo_ranks is not None
        focus_node = self.node_by_ref[focus_ref]
        source_nodes = [
            self.node_by_ref[ref]
            for ref in ranking_source_refs
            if ref in self.node_by_ref
        ]
        if not source_nodes:
            source_nodes = [focus_node]
        rows = [
            symmetric_rrf_row(self.neo_ranks, int(node["global_index"]))
            for node in source_nodes
        ]
        if len(rows) == 1:
            affinity = rows[0]
            ranking_basis = source_nodes[0]["ayah_ref"]
        else:
            affinity = np.mean(np.stack(rows), axis=0)
            ranking_basis = "rooted_packet_context_mean"
        allowed = []
        focus_surah = surah_of(focus_ref)
        for node in self.nodes:
            ref = node["ayah_ref"]
            if node["surah"] != focus_surah or ref in window or ref == focus_ref:
                continue
            score = float(affinity[int(node["global_index"])])
            if score > 0.0:
                allowed.append((score, int(node["global_index"]), ref))
        allowed.sort(key=lambda item: (-item[0], item[1]))
        top_refs = [ref for _score, _index, ref in allowed[: self.args.neo_top_k]]
        repeat_groups = ordered_unique(
            node["repeat_group_id"]
            for node in [focus_node, *source_nodes]
            if node["repeat_group_id"]
        )
        repeats = []
        if repeat_groups:
            for node in self.nodes:
                ref = node["ayah_ref"]
                if (
                    node["surah"] == focus_surah
                    and ref not in window
                    and ref != focus_ref
                    and node["repeat_group_id"] in repeat_groups
                ):
                    repeats.append(ref)
        return top_refs, ordered_unique(repeats), ranking_basis

    def nominate_branch_potential_roots(
        self,
        source_refs: list[str],
        candidate_ref: str,
        excluded_roots: set[str],
    ) -> dict[str, Any]:
        if self.branch_engine is None:
            return {"ref": candidate_ref, "nominated_candidate_only_roots": []}
        try:
            candidate = self.branch_engine._focus(candidate_ref)
        except Exception as error:  # pragma: no cover - defensive for artifact drift
            return {
                "ref": candidate_ref,
                "nominated_candidate_only_roots": [],
                "status": f"candidate_lookup_failed: {error}",
            }
        if not candidate.roots:
            return {
                "ref": candidate_ref,
                "nominated_candidate_only_roots": [],
                "status": "candidate_ayah_has_no_branch_backed_roots",
            }
        rows_by_root: dict[str, dict[str, Any]] = {}
        for source_ref in source_refs:
            try:
                source = self.branch_engine._focus(source_ref)
            except Exception:
                continue
            if not source.roots:
                continue
            semantic, exact, semantic_detail, _exact_detail = self.branch_engine._pair_scores(
                source,
                candidate,
            )
            for row in semantic_detail.get("right_to_left", []):
                root = row.get("source_root")
                if not root or root in excluded_roots:
                    continue
                current = rows_by_root.get(root)
                contribution = float(row.get("weighted_contribution", 0.0))
                if current is None or contribution > float(current.get("weighted_contribution", 0.0)):
                    rows_by_root[root] = {
                        "root": root,
                        "weighted_contribution": contribution,
                        "best_affinity": float(row.get("best_affinity", 0.0)),
                        "source_ref": source_ref,
                        "branch_semantic_coverage": semantic,
                        "exact_root_coverage": exact,
                    }
        ranked = sorted(
            rows_by_root.values(),
            key=lambda row: (
                -float(row["weighted_contribution"]),
                -float(row["best_affinity"]),
                str(row["root"]),
            ),
        )
        picked = ranked[: self.args.branch_potential_roots_per_ayah]
        return {
            "ref": candidate_ref,
            "nominated_candidate_only_roots": [row["root"] for row in picked],
            "nomination_evidence": picked,
        }


def packet_roots(ayat: Iterable[dict[str, Any]]) -> list[str]:
    return ordered_unique(
        occurrence["root"]
        for ayah in ayat
        for occurrence in ayah["root_occurrences"]
    )


def surah_text_context(context: BatchContext, surah: int) -> dict[str, Any]:
    refs = sorted(
        (ref for ref in context.quran_texts if surah_of(ref) == surah),
        key=ayah_of,
    )
    return {
        "surah": surah,
        "ayat": [
            {
                "ref": ref,
                "text_ar": context.quran_texts[ref]["text_ar"],
                "text_norm_ar": context.quran_texts[ref]["text_norm_ar"],
            }
            for ref in refs
        ],
    }


def build_packet(
    context: BatchContext,
    focus_ref: str,
    window_refs: list[str],
    parent: dict[str, Any],
    fragment: dict[str, Any],
) -> dict[str, Any]:
    ayat = [context.ayat_by_ref[ref] for ref in window_refs]
    focus_ayah = context.ayat_by_ref[focus_ref]
    context_ayat = [ayah for ayah in ayat if ayah["ref"] != focus_ref]
    focus_roots = first_seen_roots([focus_ayah])
    context_roots = first_seen_roots(context_ayat)
    all_roots = ordered_unique([*focus_roots, *context_roots])
    packet_root_set = set(all_roots)
    packet_missing_roots = [root for root in all_roots if root in context.missing_root_set]
    refs_for_missing = refs_by_root(ayat)
    missing_targets = [
        item
        for item in context.missing_mapped_targets
        if item["qac_root"] in packet_root_set
    ]
    rootless_ayat = [
        {"ref": ayah["ref"], "reason": ayah["rootless_reason"]}
        for ayah in ayat
        if ayah.get("rootless") is True
    ]
    surah = surah_of(focus_ref)
    packet = {
        "protocol": PROTOCOL,
        "focus_ref": focus_ref,
        "window": window_refs,
        "context_order": [ref for ref in window_refs if ref != focus_ref],
        "ayah_count": len(window_refs),
        "model_profile": {
            "model": "gpt-5.6-sol",
            "reasoning_effort": "max",
        },
        "selection_policy": {
            "window_policy": (
                "The coordinator selects a fixed pericope or pericope-fragment window. "
                "Roots are never selected or pruned by the reader."
            ),
            "focus_root_policy": (
                "All roots occurring in the focus ayah are included in first-seen "
                "focus order with full non-contaminated branch inventories."
            ),
            "context_root_policy": (
                "All roots occurring in non-focus context ayat are included in packet "
                "order and root order. Each occurrence includes source_phrase_ar. "
                "Rootless context ayat are retained as text-only context and have no "
                "branch-citable roots."
            ),
            "non_focus_branch_policy": (
                "Every context root with a non-contaminated inventory includes all "
                "branch IDs in 'images' mode; this always includes branch_image_ar."
            ),
            "remote_orientation_policy": (
                "The packet includes full surah text and may include SLM-reviewed "
                "same-surah and NEO same-surah remote orientation cues. Remote cues "
                "are non-citable; reader branch citations must resolve from "
                "focus_branch_inventories or context_root_cues."
            ),
            "root_mapping_policy": (
                "QAC roots are resolved through qac-furuq-v4-root-map.sqlite.gz. "
                "If a QAC root maps to multiple Furuq root_ids, every mapped root "
                "and its non-contaminated branches are included in target_rank order. "
                "Branch IDs are root-local, so reader citations must pair branch_id "
                "with mapped_root_id."
            ),
            "source_phrase_policy": (
                "source_phrase_ar is deterministically derived from QAC surfaces_ar "
                "for the root occurrence in that source ayah."
            ),
        },
        "root_mappings": [
            root_mapping_summary(context.root_mappings[root]) for root in all_roots
        ],
        "focus_ayah": focus_ayah,
        "context_ayat": context_ayat,
        "focus_branch_inventories": [
            {
                "root": root,
                "root_mapping": root_mapping_summary(context.root_mappings[root]),
                "source_phrases": source_phrases([focus_ayah], root),
                "branches": [
                    focus_branch(branch)
                    for branch in context.branches.get(root, [])
                ],
            }
            for root in focus_roots
            if context.branches.get(root)
        ],
        "context_root_cues": [
            {
                "root": root,
                "root_mapping": root_mapping_summary(context.root_mappings[root]),
                "source_phrases": source_phrases(context_ayat, root),
                "branch_inventory_mode": "images",
                "branches": [
                    compact_branch(branch, "images")
                    for branch in context.branches.get(root, [])
                ],
            }
            for root in context_roots
            if context.branches.get(root)
        ],
        "missing_branch_inventories": [
            {
                "root": root,
                "root_mapping": root_mapping_summary(context.root_mappings[root]),
                "refs": refs_for_missing[root],
                "source_phrases": source_phrases(ayat, root),
                "reason": "no non-contaminated branch inventory in resource",
            }
            for root in packet_missing_roots
        ],
        "surah_text": surah_text_context(context, surah),
        "out_of_window_root_cues": [],
        "remote_orientation": {
            "orientation_only": True,
            "citable": False,
            "reader_citation_policy": (
                "Remote material may orient analysis but does not authorize branch "
                "citations. Cite only packet focus/context branch inventories."
            ),
        },
        "provenance": {
            "branch_filter": {
                "status": "any",
                "contaminated": "no",
                "origin_corpus": ["furuq", "quranic"],
            },
            "missing_mapped_targets": missing_targets,
            "out_of_window_roots": {
                "branch_inventory_mode": "none",
                "roots_with_branch_cues": [],
                "missing_branch_inventory_roots": [],
            },
            "rootless_ayat": rootless_ayat,
            "resource_sha256": {
                **context.resource_hashes,
                relpath(packet_builder.quran_surah_path(packet_builder.DEFAULT_QURAN_DIR, surah)): context.quran_hashes[surah],
            },
            "synthetic_ayat": [],
            "pericope": {
                "source_path": relpath(context.args.pericopes),
                "source_line": parent["_source_line"],
                "surah": parent["surah"],
                "pericope": parent["pericope"],
                "ayah_from": parent["ayah_from"],
                "ayah_to": parent["ayah_to"],
                "label": parent["label"],
                "fragment": {
                    "ayah_from": fragment["ayah_from"],
                    "ayah_to": fragment["ayah_to"],
                    "label": fragment["label"],
                    "fragment_index": fragment["fragment_index"],
                    "fragment_count": fragment["fragment_count"],
                    "fragment_policy": fragment["fragment_policy"],
                },
            },
        },
    }
    if not context.args.no_slm:
        add_slm_orientation(context, packet, packet_root_set)
    if not context.args.no_neo:
        add_neo_orientation(context, packet, packet_root_set)
    validate_remote_orientation(packet)
    if parent.get("_window_source") == "surah_window_explicit":
        packet["selection_policy"]["window_policy"] = (
            "The coordinator selected the whole surah as the packet window. "
            "Roots are never selected or pruned by the reader."
        )
        packet["provenance"]["window_source"] = {
            "kind": "surah_window_explicit",
            "surah": parent["surah"],
            "ayah_from": parent["ayah_from"],
            "ayah_to": parent["ayah_to"],
            "label": parent["label"],
        }
    return packet


def add_slm_orientation(
    context: BatchContext,
    packet: dict[str, Any],
    packet_roots_set: set[str],
) -> None:
    focus_ref = packet["focus_ref"]
    surah = surah_of(focus_ref)
    window = set(packet["window"])
    refs = ordered_unique(
        ref
        for label, ref in context.slm_rows(focus_ref)
        if label in {"strong", "medium"} and ref.startswith(f"{surah}:")
        and ref not in window
        and ref in context.ayat_by_ref
    )
    ayat = [context.ayat_by_ref[ref] for ref in refs if ref in context.ayat_by_ref]
    roots = [
        root
        for root in first_seen_roots(ayat)
        if root not in packet_roots_set
    ]
    cues, unmatched = context.branch_cues(roots, ayat)
    packet["remote_orientation"]["slm_same_surah_reviewed"] = {
        "orientation_only": True,
        "citable": False,
        "source": relpath(context.args.slm_outputs),
        "labels_included": ["strong", "medium"],
        "candidate_scope": "same_surah_outside_packet_window",
        "delta_against": "packet_window_roots",
        "neighbor_refs": refs,
        "root_cues": cues,
        "unmatched_root_mappings": unmatched,
    }


def add_neo_orientation(
    context: BatchContext,
    packet: dict[str, Any],
    packet_roots_set: set[str],
) -> None:
    focus_ref = packet["focus_ref"]
    window = set(packet["window"])
    focus_ayah = packet["focus_ayah"]
    context_ayat = packet["context_ayat"]
    if focus_ayah.get("rootless"):
        ranking_sources = [
            ayah["ref"]
            for ayah in context_ayat
            if ayah.get("root_occurrences")
        ]
        rootless_focus_fallback = True
    else:
        ranking_sources = [focus_ref]
        rootless_focus_fallback = False
    neo_refs, exact_repeats, ranking_basis = context.selected_neo_refs(
        focus_ref,
        window,
        ranking_sources,
    )
    selected_refs = ordered_unique([*neo_refs, *exact_repeats])
    selected_ayat = [
        context.ayat_by_ref[ref]
        for ref in selected_refs
        if ref in context.ayat_by_ref
    ]
    shared_roots = [
        root
        for root in sorted(packet_roots_set)
        if source_phrases(selected_ayat, root)
    ]
    shared_sources = [
        {
            "root": root,
            "orientation_only": True,
            "citable": False,
            "remote_source_phrases": source_phrases(selected_ayat, root),
            "local_branch_inventory_reused": True,
        }
        for root in shared_roots
    ]
    nominations = []
    nominated_roots = []
    for ref in selected_refs:
        nomination = context.nominate_branch_potential_roots(
            ranking_sources,
            ref,
            packet_roots_set,
        )
        nominations.append(nomination)
        nominated_roots.extend(nomination["nominated_candidate_only_roots"])
    delta_roots = [
        root
        for root in ordered_unique(nominated_roots)
        if root not in packet_roots_set
    ]
    slm_section = packet["remote_orientation"].get("slm_same_surah_reviewed", {})
    slm_roots = {
        cue["root"]
        for cue in slm_section.get("root_cues", [])
    } | {
        mapping["qac_root"]
        for mapping in slm_section.get("unmatched_root_mappings", [])
    }
    delta_roots = [root for root in delta_roots if root not in slm_roots]
    cues, unmatched = context.branch_cues(delta_roots, selected_ayat)
    packet["remote_orientation"]["neo_same_surah_branch_potential"] = {
        "orientation_only": True,
        "citable": False,
        "candidate_scope": "same_surah_outside_packet_window",
        "rank_method": "neo_raw_complete_candidate_universe_symmetric_rrf_top_20",
        "neo_top_k": context.args.neo_top_k,
        "ranking_basis": ranking_basis,
        "rootless_focus_fallback": rootless_focus_fallback,
        "exact_repetitions_added_separately": exact_repeats,
        "selected_refs": selected_refs,
        "shared_focus_or_context_root_remote_sources": shared_sources,
        "branch_potential_root_nomination": {
            "max_candidate_only_roots_per_selected_ayah": context.args.branch_potential_roots_per_ayah,
            "selection_basis": (
                "candidate right_to_left weighted_contribution, excluding roots "
                "already present in the packet window"
            ),
            "per_ayah": nominations,
        },
        "cross_root_cues": cues,
        "unmatched_root_mappings": unmatched,
    }


def validate_remote_orientation(packet: dict[str, Any]) -> None:
    remote = packet.get("remote_orientation", {})
    if remote.get("orientation_only") is not True or remote.get("citable") is not False:
        raise ValueError(f"{packet['focus_ref']}: remote_orientation must be non-citable")
    window = set(packet["window"])
    slm = remote.get("slm_same_surah_reviewed")
    if slm:
        if slm.get("orientation_only") is not True or slm.get("citable") is not False:
            raise ValueError(f"{packet['focus_ref']}: SLM remote section must be non-citable")
        overlap = sorted(set(slm.get("neighbor_refs", [])) & window, key=ayah_of)
        if overlap:
            raise ValueError(
                f"{packet['focus_ref']}: SLM remote refs overlap packet window: {overlap}"
            )
        for cue in slm.get("root_cues", []):
            if cue.get("orientation_only") is not True or cue.get("citable") is not False:
                raise ValueError(f"{packet['focus_ref']}: SLM root cue must be non-citable")
    neo = remote.get("neo_same_surah_branch_potential")
    if neo:
        if neo.get("orientation_only") is not True or neo.get("citable") is not False:
            raise ValueError(f"{packet['focus_ref']}: NEO remote section must be non-citable")
        overlap = sorted(set(neo.get("selected_refs", [])) & window, key=ayah_of)
        if overlap:
            raise ValueError(
                f"{packet['focus_ref']}: NEO remote refs overlap packet window: {overlap}"
            )
        for cue in neo.get("cross_root_cues", []):
            if cue.get("orientation_only") is not True or cue.get("citable") is not False:
                raise ValueError(f"{packet['focus_ref']}: NEO cross-root cue must be non-citable")


def write_packet(path: Path, packet: dict[str, Any]) -> int:
    payload = json.dumps(packet, ensure_ascii=False, separators=(",", ":")) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(payload, encoding="utf-8")
    return len(payload.encode("utf-8"))


def main() -> None:
    args = parse_args()
    if args.window_mode == "surah":
        pericopes = synthetic_surah_windows(args.requested_surahs)
    else:
        pericopes = load_pericopes(
            args.pericopes,
            args.surah_start,
            args.surah_end,
            set(args.explicit_surahs) if args.explicit_surahs else None,
        )
    jobs = planned_windows(args, pericopes)
    pericope_surahs = {int(row["surah"]) for row in pericopes}
    missing_pericope_surahs = [
        {
            "surah": surah,
            "ayah_count": len(packet_builder.numbered_refs_for_surah(packet_builder.DEFAULT_QURAN_DIR, surah)),
            "reason": "surah has no rows in pericope source",
        }
        for surah in args.requested_surahs
        if args.window_mode == "pericope" and surah not in pericope_surahs
    ]
    context = BatchContext(args)
    report: dict[str, Any] = {
        "packet_generation": {
            "surah_start": args.surah_start,
            "surah_end": args.surah_end,
            "surah_list": args.explicit_surahs,
            "requested_surahs": args.requested_surahs,
            "window_mode": args.window_mode,
            "packet_schema": args.packet_schema,
            "pericope_source": relpath(args.pericopes),
            "fragment_dense_pericopes": args.fragment_dense_pericopes,
            "slm_orientation": not args.no_slm,
            "neo_orientation": not args.no_neo,
            "overwrite": args.overwrite,
        },
        "missing_pericope_surahs": missing_pericope_surahs,
        "missing_pericope_ayah_count": sum(row["ayah_count"] for row in missing_pericope_surahs),
        "threshold_bytes": PACKET_SIZE_REPORT_BYTES,
        "large_packet_bytes": LARGE_PACKET_BYTES,
        "packet_count": 0,
        "over_350kb_count": 0,
        "over_500kb_count": 0,
        "surah_summary": [],
        "pericope_summary": [],
        "over_350kb_packets": [],
        "over_500kb_packets": [],
        "skipped_existing": [],
    }
    processed = 0
    try:
        for parent, fragment, window in jobs:
            sizes = []
            for focus_ref in window:
                if args.limit and processed >= args.limit:
                    raise KeyboardInterrupt
                output = (
                    args.output_root
                    / f"s{parent['surah']}"
                    / "packets"
                    / f"{focus_ref.replace(':', '_')}.packet.json"
                )
                if output.exists() and not args.overwrite:
                    report["skipped_existing"].append(str(output))
                    continue
                packet = build_packet(context, focus_ref, window, parent, fragment)
                if args.packet_schema == "pericope-lean":
                    packet = lean_packet(packet)
                if args.validate:
                    if packet.get("protocol") == LEAN_PACKET_PROTOCOL:
                        validate_lean_packet(packet)
                    else:
                        validate_packet(packet)
                size = write_packet(output, packet)
                sizes.append(size)
                processed += 1
                report["packet_count"] += 1
                if size > PACKET_SIZE_REPORT_BYTES:
                    report["over_350kb_count"] += 1
                    report["over_350kb_packets"].append(
                        {"ref": focus_ref, "path": relpath(output), "size_bytes": size}
                    )
                if size > LARGE_PACKET_BYTES:
                    report["over_500kb_count"] += 1
                    report["over_500kb_packets"].append(
                        {"ref": focus_ref, "path": relpath(output), "size_bytes": size}
                    )
            if sizes:
                report["pericope_summary"].append(
                    {
                        "surah": parent["surah"],
                        "pericope": parent["pericope"],
                        "parent_ayah_from": parent["ayah_from"],
                        "parent_ayah_to": parent["ayah_to"],
                        "parent_label": parent["label"],
                        "fragment": fragment,
                        "packet_count": len(sizes),
                        "min_size_bytes": min(sizes),
                        "max_size_bytes": max(sizes),
                        "over_350kb_count": sum(size > PACKET_SIZE_REPORT_BYTES for size in sizes),
                        "over_500kb_count": sum(size > LARGE_PACKET_BYTES for size in sizes),
                    }
                )
        by_surah: dict[int, list[dict[str, Any]]] = {}
        for row in report["pericope_summary"]:
            by_surah.setdefault(int(row["surah"]), []).append(row)
        report["surah_summary"] = [
            {
                "surah": surah,
                "packet_count": sum(row["packet_count"] for row in rows),
                "max_size_bytes": max(row["max_size_bytes"] for row in rows),
                "over_350kb_count": sum(row["over_350kb_count"] for row in rows),
                "over_500kb_count": sum(row["over_500kb_count"] for row in rows),
            }
            for surah, rows in sorted(by_surah.items())
        ]
    except KeyboardInterrupt:
        report["interrupted_after_packet_count"] = processed
    finally:
        context.close()
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(
        "generated "
        f"{report['packet_count']} packets; "
        f"{report['over_350kb_count']} over 350 KiB; "
        f"{report['over_500kb_count']} over 500 KiB; "
        f"report {args.report}"
    )


if __name__ == "__main__":
    main()
