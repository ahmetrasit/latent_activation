#!/usr/bin/env python3
"""Build minimal per-ayah target lists from NEO and reviewed inter-ayah data."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
from typing import Any, Mapping, Sequence

import numpy as np


ARTIFACT_SHAPE = "ayah-target-list-v1"
ALGORITHM_VERSION = "neo-reviewed-target-union-v2"
COLLECTION_SCHEMA_VERSION = "ayah-target-list-collection-v1"
NEO_RRF_OFFSET = 10.0
NEO_LIMIT = 50
NEO_MIN_AFFINITY = 0.003
ACCEPTED_REVIEW_STRENGTHS = ("strong", "medium")
ACCEPTED_REVIEW_STRENGTH_SET = frozenset(ACCEPTED_REVIEW_STRENGTHS)
KNOWN_REVIEW_STRENGTHS = frozenset(
    {"strong", "medium", "weak", "no value", "reject", "contrast"}
)
AYAH_REF_RE = re.compile(
    r"^(?P<surah>[1-9]\d*):(?P<start>[1-9]\d*)(?:-(?P<end>[1-9]\d*))?$"
)

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
DEFAULT_QURAN_SLM_ROOT = PROJECT_ROOT.parent / "quran-slm"
DEFAULT_AYAH_MAP_DIR = DEFAULT_QURAN_SLM_ROOT / "artifacts/ayah_semantic_map/v1"
DEFAULT_REVIEW_DIR = DEFAULT_QURAN_SLM_ROOT / "inter-ayah/outputs"
DEFAULT_OUTPUT_DIR = SCRIPT_DIR / "outputs"


class NeighborBuildError(ValueError):
    """Raised when an input or generated target-list artifact is inconsistent."""


@dataclass(frozen=True, slots=True)
class AyahRecord:
    global_index: int
    node_id: str
    surah: int
    ayah: int
    ayah_ref: str
    repeat_group_id: str | None
    repeat_group_size: int


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def json_sha256(value: Any) -> str:
    encoded = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def canonical_ref_key(value: str) -> tuple[int, int]:
    match = AYAH_REF_RE.fullmatch(value)
    if match is None or match.group("end") is not None:
        raise NeighborBuildError(f"not a canonical ayah reference: {value!r}")
    return int(match.group("surah")), int(match.group("start"))


def expand_reviewed_ref(value: str) -> tuple[str, ...]:
    """Expand accepted same-surah review ranges into canonical ayah refs."""

    match = AYAH_REF_RE.fullmatch(value.strip())
    if match is None:
        raise NeighborBuildError(f"invalid reviewed ayah reference: {value!r}")
    surah = int(match.group("surah"))
    start = int(match.group("start"))
    end = int(match.group("end") or start)
    if end < start:
        raise NeighborBuildError(f"descending reviewed ayah range: {value!r}")
    return tuple(f"{surah}:{ayah}" for ayah in range(start, end + 1))


def _artifact_record(manifest: Mapping[str, Any], name: str) -> Mapping[str, Any]:
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, Mapping):
        raise NeighborBuildError("ayah-map manifest lacks an artifacts object")
    record = artifacts.get(name)
    if not isinstance(record, Mapping):
        raise NeighborBuildError(f"ayah-map manifest lacks artifact {name!r}")
    return record


class NeoIndex:
    """Authenticated read-only access to canonical ayahs and raw NEO ranks."""

    def __init__(self, ayah_map_dir: Path) -> None:
        self.ayah_map_dir = ayah_map_dir.resolve()
        manifest_path = self.ayah_map_dir / "manifest.json"
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise NeighborBuildError(f"cannot load {manifest_path}: {error}") from error
        if (
            manifest.get("schema_version") != 1
            or manifest.get("algorithm_version") != "ayah-semantic-map-v1.2"
        ):
            raise NeighborBuildError("ayah-map manifest contract differs")
        rank_contract = manifest.get("rank_contract")
        if not isinstance(rank_contract, Mapping):
            raise NeighborBuildError("ayah-map manifest lacks rank contract")
        expected_transform = "0.5 * (1/(10+rank(i->j)) + 1/(10+rank(j->i)))"
        if (
            rank_contract.get("dtype") != "<u2"
            or rank_contract.get("self_and_exact_repeat_sentinel") != 0
            or rank_contract.get("symmetric_transform") != expected_transform
        ):
            raise NeighborBuildError("NEO rank contract differs from symmetric raw RRF")

        nodes_record = _artifact_record(manifest, "nodes")
        ranks_record = _artifact_record(manifest, "ranks_neo_raw")
        nodes_path = self.ayah_map_dir / str(nodes_record.get("file", ""))
        ranks_path = self.ayah_map_dir / str(ranks_record.get("file", ""))
        self._authenticate(nodes_path, nodes_record)
        self._authenticate(ranks_path, ranks_record)

        self.nodes = self._load_nodes(nodes_path)
        self.by_ref = {node.ayah_ref: node for node in self.nodes}
        surah_working: dict[int, list[str]] = {}
        repeat_working: dict[str, list[str]] = {}
        for node in self.nodes:
            surah_working.setdefault(node.surah, []).append(node.ayah_ref)
            if node.repeat_group_id:
                repeat_working.setdefault(node.repeat_group_id, []).append(node.ayah_ref)
        self.refs_by_surah = {
            surah: tuple(refs) for surah, refs in surah_working.items()
        }
        self.refs_by_repeat_group = {
            group: tuple(refs) for group, refs in repeat_working.items()
        }

        shape = rank_contract.get("shape")
        expected_shape = [len(self.nodes), len(self.nodes)]
        if shape != expected_shape:
            raise NeighborBuildError(
                f"NEO rank shape {shape!r} differs from {expected_shape!r}"
            )
        expected_bytes = len(self.nodes) ** 2 * np.dtype("<u2").itemsize
        if ranks_path.stat().st_size != expected_bytes:
            raise NeighborBuildError("NEO rank byte size differs from its square shape")
        self.ranks = np.memmap(
            ranks_path,
            mode="r",
            dtype=np.dtype("<u2"),
            shape=(len(self.nodes), len(self.nodes)),
            order="C",
        )
        self.provenance = {
            "manifest_path": str(manifest_path.resolve()),
            "manifest_sha256": sha256_file(manifest_path),
            "nodes_path": str(nodes_path.resolve()),
            "nodes_sha256": nodes_record["sha256"],
            "ranks_path": str(ranks_path.resolve()),
            "ranks_sha256": ranks_record["sha256"],
            "rank_basis": "raw NEO directional ranks",
            "symmetric_transform": expected_transform,
        }

    @staticmethod
    def _authenticate(path: Path, record: Mapping[str, Any]) -> None:
        if not path.is_file():
            raise NeighborBuildError(f"missing authenticated artifact {path}")
        if path.stat().st_size != record.get("bytes"):
            raise NeighborBuildError(f"artifact byte count differs for {path}")
        if sha256_file(path) != record.get("sha256"):
            raise NeighborBuildError(f"artifact SHA-256 differs for {path}")

    @staticmethod
    def _load_nodes(path: Path) -> tuple[AyahRecord, ...]:
        required = {
            "global_index",
            "node_id",
            "surah",
            "ayah",
            "ayah_ref",
            "repeat_group_id",
            "repeat_group_size",
        }
        nodes: list[AyahRecord] = []
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            if reader.fieldnames is None or not required.issubset(reader.fieldnames):
                raise NeighborBuildError("ayah-map nodes TSV lacks required columns")
            for expected_index, row in enumerate(reader):
                try:
                    global_index = int(row["global_index"])
                    surah = int(row["surah"])
                    ayah = int(row["ayah"])
                    repeat_group_size = int(row["repeat_group_size"])
                except (TypeError, ValueError) as error:
                    raise NeighborBuildError("ayah-map node has invalid integers") from error
                ayah_ref = f"{surah}:{ayah}"
                if (
                    global_index != expected_index
                    or row["node_id"] != f"quran:{ayah_ref}"
                    or row["ayah_ref"] != ayah_ref
                ):
                    raise NeighborBuildError("ayah-map node identity is not canonical")
                group = row["repeat_group_id"] or None
                if bool(group) != (repeat_group_size > 1):
                    raise NeighborBuildError("ayah-map repeat identity is inconsistent")
                nodes.append(
                    AyahRecord(
                        global_index=global_index,
                        node_id=row["node_id"],
                        surah=surah,
                        ayah=ayah,
                        ayah_ref=ayah_ref,
                        repeat_group_id=group,
                        repeat_group_size=repeat_group_size,
                    )
                )
        if len(nodes) != 6236 or len({node.ayah_ref for node in nodes}) != 6236:
            raise NeighborBuildError("ayah-map node catalog is not 6,236 unique ayat")
        return tuple(nodes)

    def neo_neighbor_refs(self, focus_ref: str) -> tuple[str, ...]:
        """Return up to 50 qualified same-surah refs; scores remain internal."""

        focus = self.by_ref[focus_ref]
        candidate_indices = np.asarray(
            [
                self.by_ref[ref].global_index
                for ref in self.refs_by_surah[focus.surah]
                if ref != focus_ref
            ],
            dtype=np.intp,
        )
        outgoing = np.asarray(
            self.ranks[focus.global_index, candidate_indices], dtype=np.uint16
        )
        incoming = np.asarray(
            self.ranks[candidate_indices, focus.global_index], dtype=np.uint16
        )
        if not np.array_equal(outgoing == 0, incoming == 0):
            raise NeighborBuildError(f"NEO exclusion mask is asymmetric for {focus_ref}")
        supported = outgoing != 0
        indices = candidate_indices[supported]
        scores = np.float32(0.5) * (
            np.float32(1.0)
            / (np.float32(NEO_RRF_OFFSET) + outgoing[supported].astype(np.float32))
            + np.float32(1.0)
            / (np.float32(NEO_RRF_OFFSET) + incoming[supported].astype(np.float32))
        )
        order = np.lexsort((indices, -scores))
        qualified = order[scores[order] >= np.float32(NEO_MIN_AFFINITY)][
            :NEO_LIMIT
        ]
        return tuple(
            self.nodes[int(indices[position])].ayah_ref for position in qualified
        )

    def exact_same_surah_repetitions(self, focus_ref: str) -> tuple[str, ...]:
        focus = self.by_ref[focus_ref]
        if not focus.repeat_group_id:
            return ()
        return tuple(
            ref
            for ref in self.refs_by_repeat_group[focus.repeat_group_id]
            if ref != focus_ref and self.by_ref[ref].surah == focus.surah
        )


def review_path_for(review_dir: Path, focus_ref: str) -> Path:
    surah, ayah = canonical_ref_key(focus_ref)
    return review_dir / f"focus_{surah}_{ayah}_cutoff_100.tsv"


def load_reviewed_targets(
    review_dir: Path,
    focus_ref: str,
    known_refs: Mapping[str, AyahRecord],
) -> tuple[set[str], dict[str, Any]]:
    path = review_path_for(review_dir, focus_ref)
    if not path.is_file():
        raise NeighborBuildError(f"missing reviewed inter-ayah output {path}")
    accepted: set[str] = set()
    ignored_strengths: dict[str, int] = {}
    accepted_input_rows = 0
    expanded_output_refs = 0
    normalized_ref_first_rows = 0
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle, delimiter="\t")
        for row_number, row in enumerate(reader, start=1):
            if not row or row == [""]:
                continue
            if len(row) != 3:
                raise NeighborBuildError(
                    f"{path}:{row_number} has {len(row)} fields instead of 3"
                )
            first, second, explanation = (value.strip() for value in row)
            if AYAH_REF_RE.fullmatch(first) and second in KNOWN_REVIEW_STRENGTHS:
                reviewed_ref, strength = first, second
                normalized_ref_first_rows += 1
            else:
                strength, reviewed_ref = first, second
            if strength not in ACCEPTED_REVIEW_STRENGTH_SET:
                ignored_strengths[strength] = ignored_strengths.get(strength, 0) + 1
                continue
            if not explanation:
                raise NeighborBuildError(f"{path}:{row_number} has an empty explanation")
            accepted_input_rows += 1
            expanded_refs = expand_reviewed_ref(reviewed_ref)
            expanded_output_refs += len(expanded_refs)
            for candidate_ref in expanded_refs:
                if candidate_ref not in known_refs:
                    raise NeighborBuildError(
                        f"{path}:{row_number} references unknown ayah {candidate_ref}"
                    )
                if candidate_ref != focus_ref:
                    accepted.add(candidate_ref)
    return accepted, {
        "path": str(path.resolve()),
        "sha256": sha256_file(path),
        "accepted_input_row_count": accepted_input_rows,
        "accepted_canonical_ref_count": len(accepted),
        "expanded_output_ref_count": expanded_output_refs,
        "normalized_ref_first_row_count": normalized_ref_first_rows,
        "ignored_strength_counts": dict(sorted(ignored_strengths.items())),
    }


def build_artifact(
    focus_ref: str,
    *,
    neo: NeoIndex,
    review_dir: Path,
) -> dict[str, Any]:
    if focus_ref not in neo.by_ref:
        raise NeighborBuildError(f"unknown focus ayah {focus_ref!r}")
    reviewed, _ = load_reviewed_targets(review_dir, focus_ref, neo.by_ref)
    targets = (
        set(neo.neo_neighbor_refs(focus_ref))
        | set(neo.exact_same_surah_repetitions(focus_ref))
        | reviewed
    )
    targets.discard(focus_ref)
    payload = {
        "ayah_ref": focus_ref,
        "target_ayat": sorted(
            targets, key=lambda ref: neo.by_ref[ref].global_index
        ),
    }
    validate_artifact(payload, neo=neo)
    return payload


def validate_artifact(
    artifact: Mapping[str, Any],
    *,
    neo: NeoIndex,
    expected_focus_ref: str | None = None,
) -> None:
    if set(artifact) != {"ayah_ref", "target_ayat"}:
        raise NeighborBuildError("target-list artifact must contain exactly two fields")
    focus_ref = artifact.get("ayah_ref")
    targets = artifact.get("target_ayat")
    if not isinstance(focus_ref, str) or focus_ref not in neo.by_ref:
        raise NeighborBuildError("target-list artifact has an unknown focus")
    if expected_focus_ref is not None and focus_ref != expected_focus_ref:
        raise NeighborBuildError("target-list focus differs from its filename")
    if not isinstance(targets, list) or any(
        not isinstance(ref, str) or ref not in neo.by_ref for ref in targets
    ):
        raise NeighborBuildError("target-list artifact contains an unknown target")
    if focus_ref in targets or len(targets) != len(set(targets)):
        raise NeighborBuildError("target-list artifact contains self or duplicates")
    expected_order = sorted(targets, key=lambda ref: neo.by_ref[ref].global_index)
    if targets != expected_order:
        raise NeighborBuildError("target-list artifact is not in Quran order")


def write_json_atomic(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        temporary.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        temporary.replace(path)
    finally:
        if temporary.exists():
            temporary.unlink()


def output_path_for(output_dir: Path, focus_ref: str) -> Path:
    surah, ayah = canonical_ref_key(focus_ref)
    return output_dir / f"ayah_{surah}_{ayah}.neighbors.json"


def generation_contract(neo: NeoIndex) -> dict[str, Any]:
    return {
        "artifact_shape": ARTIFACT_SHAPE,
        "algorithm_version": ALGORITHM_VERSION,
        "neo_limit": NEO_LIMIT,
        "neo_min_symmetric_rrf_affinity": NEO_MIN_AFFINITY,
        "neo_candidate_scope": "same surah, excluding self and exact repetitions",
        "exact_repetition_scope": "same surah",
        "reviewed_strengths": list(ACCEPTED_REVIEW_STRENGTHS),
        "target_order": "canonical Quran order",
        "neo_provenance_sha256": json_sha256(neo.provenance),
    }


def audit_collection(
    output_dir: Path,
    *,
    neo: NeoIndex,
    review_dir: Path,
) -> dict[str, Any]:
    """Exactly rederive a complete flat collection before publishing it."""

    expected_paths = {
        output_path_for(output_dir, node.ayah_ref).resolve(): node
        for node in neo.nodes
    }
    actual_paths = {path.resolve() for path in output_dir.glob("ayah_*_*.neighbors.json")}
    if actual_paths != set(expected_paths):
        missing = sorted(str(path) for path in set(expected_paths) - actual_paths)
        extra = sorted(str(path) for path in actual_paths - set(expected_paths))
        raise NeighborBuildError(
            "flat output collection differs from the canonical catalog: "
            f"missing={missing[:3]}, extra={extra[:3]}"
        )

    output_records: list[dict[str, Any]] = []
    review_records: list[dict[str, str]] = []
    for ordinal, node in enumerate(neo.nodes, start=1):
        path = output_path_for(output_dir, node.ayah_ref).resolve()
        raw = path.read_bytes()
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as error:
            raise NeighborBuildError(f"invalid generated JSON {path}: {error}") from error
        validate_artifact(payload, neo=neo, expected_focus_ref=node.ayah_ref)
        expected_payload = build_artifact(
            node.ayah_ref,
            neo=neo,
            review_dir=review_dir,
        )
        if payload != expected_payload:
            raise NeighborBuildError(
                f"output does not exactly rederive from current inputs for {path}"
            )
        review_path = review_path_for(review_dir, node.ayah_ref).resolve()
        review_sha256 = sha256_file(review_path)
        output_records.append(
            {
                "ayah_ref": node.ayah_ref,
                "file": path.name,
                "bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest(),
            }
        )
        review_records.append(
            {"ayah_ref": node.ayah_ref, "sha256": review_sha256}
        )
        if ordinal % 500 == 0 or ordinal == len(neo.nodes):
            print(f"[audit {ordinal}/{len(neo.nodes)}] {node.ayah_ref}", flush=True)

    return {
        "schema_version": COLLECTION_SCHEMA_VERSION,
        "status": "complete",
        "generation_contract": generation_contract(neo),
        "expected_ayah_count": len(neo.nodes),
        "expected_ayah_refs_sha256": json_sha256(
            [node.ayah_ref for node in neo.nodes]
        ),
        "reviewed_inputs_sha256": json_sha256(review_records),
        "output_count": len(output_records),
        "output_bytes": sum(record["bytes"] for record in output_records),
        "output_records_sha256": json_sha256(output_records),
        "outputs": output_records,
    }


def invalidate_collection_manifest(output_dir: Path) -> None:
    (output_dir / "collection_manifest.json").unlink(missing_ok=True)


def write_run_state(
    output_dir: Path,
    *,
    mode: str,
    selected_refs: Sequence[str],
    contract: Mapping[str, Any],
    status: str = "in_progress",
) -> None:
    write_json_atomic(
        output_dir / "collection_run_state.json",
        {
            "schema_version": COLLECTION_SCHEMA_VERSION,
            "status": status,
            "mode": mode,
            "selected_ayah_count": len(selected_refs),
            "selected_ayah_refs_sha256": json_sha256(list(selected_refs)),
            "generation_contract": dict(contract),
        },
    )


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--focus", help="one canonical S:A focus reference")
    selection.add_argument("--all", action="store_true", help="build all 6,236 ayat")
    parser.add_argument("--start-at", help="inclusive S:A suffix for a resumable --all run")
    parser.add_argument("--ayah-map-dir", type=Path, default=DEFAULT_AYAH_MAP_DIR)
    parser.add_argument("--review-dir", type=Path, default=DEFAULT_REVIEW_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args(argv)
    if args.start_at and not args.all:
        parser.error("--start-at requires --all")
    return args


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    neo = NeoIndex(args.ayah_map_dir)
    if args.focus:
        focus_refs = [args.focus]
    else:
        focus_refs = [node.ayah_ref for node in neo.nodes]
        if args.start_at:
            if args.start_at not in neo.by_ref:
                raise NeighborBuildError(f"unknown --start-at ayah {args.start_at!r}")
            focus_refs = focus_refs[neo.by_ref[args.start_at].global_index :]

    args.output_dir.mkdir(parents=True, exist_ok=True)
    contract = generation_contract(neo)
    invalidate_collection_manifest(args.output_dir)
    mode = "focus" if args.focus else ("all_suffix" if args.start_at else "all")
    write_run_state(
        args.output_dir,
        mode=mode,
        selected_refs=focus_refs,
        contract=contract,
    )
    for ordinal, focus_ref in enumerate(focus_refs, start=1):
        payload = build_artifact(
            focus_ref,
            neo=neo,
            review_dir=args.review_dir,
        )
        path = output_path_for(args.output_dir, focus_ref)
        write_json_atomic(path, payload)
        if len(focus_refs) == 1 or ordinal % 500 == 0 or ordinal == len(focus_refs):
            print(f"[{ordinal}/{len(focus_refs)}] {focus_ref} -> {path}", flush=True)
    if args.all:
        manifest = audit_collection(
            args.output_dir,
            neo=neo,
            review_dir=args.review_dir,
        )
        write_json_atomic(args.output_dir / "collection_manifest.json", manifest)
        (args.output_dir / "collection_run_state.json").unlink()
    else:
        write_run_state(
            args.output_dir,
            mode=mode,
            selected_refs=focus_refs,
            contract=contract,
            status="partial_generation",
        )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except NeighborBuildError as error:
        raise SystemExit(f"error: {error}") from error
