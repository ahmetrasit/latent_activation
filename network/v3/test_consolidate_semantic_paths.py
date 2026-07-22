from __future__ import annotations

import collections
import json
import math
import os
import subprocess
import sys
import threading
from pathlib import Path


V3_DIR = Path(__file__).resolve().parent
if str(V3_DIR) not in sys.path:
    sys.path.insert(0, str(V3_DIR))

import consolidate_semantic_paths as subject
import run_corpus_candidates as runner
from consolidate_channel_families import idf_weights, weighted_jaccard


def branch(node_id: str, root: str, ayah: int) -> dict[str, object]:
    return {
        "node_id": node_id,
        "root": root,
        "branch_id": node_id.rsplit(":", 1)[-1],
        "ayahs": [ayah],
        "image_ar": f"image {node_id}",
    }


def path_row(index: int, nodes: list[tuple[str, str, int]]) -> dict[str, object]:
    branches = [branch(*node) for node in nodes]
    tree_edges = []
    for left, right in zip(branches, branches[1:]):
        tree_edges.append(
            {
                "edge_key": " -- ".join(sorted((left["node_id"], right["node_id"]))),
                "left": left,
                "right": right,
                "strength": 0.8,
            }
        )
    return {
        "path_id": f"P{index:04d}",
        "path_score": round(0.5 + index / 100, 4),
        "label_hint": f"label {index}",
        "roots": sorted({root for _node, root, _ayah in nodes}),
        "ayahs": sorted({ayah for _node, _root, ayah in nodes}),
        "branches": branches,
        "tree_edges": tree_edges,
        "top_facets": [[f"theme:t{index % 3}", 0.75]],
    }


def fixture_paths() -> list[dict[str, object]]:
    a = ("q:r1:B001", "r1", 1)
    b = ("q:r2:B001", "r2", 2)
    c = ("q:r3:B001", "r3", 3)
    d = ("q:r4:B001", "r4", 4)
    e = ("q:r5:B001", "r5", 5)
    f = ("q:r6:B001", "r6", 6)
    return [
        path_row(1, [a, b, c]),
        path_row(2, [a, b, c, d]),
        path_row(3, [a, b, d]),
        path_row(4, [b, c, d]),
        path_row(5, [d, e, f]),
        path_row(6, [d, e]),
        path_row(7, [a, e, f]),
        path_row(8, [a, b, c]),
    ]


def legacy_similarity_edges(
    paths: list[dict[str, object]],
    *,
    mutual_k: int,
    min_similarity: float,
    containment_threshold: float,
) -> list[dict[str, object]]:
    by_id = {path["path_id"]: subject.features(path) for path in paths}
    branch_weights = idf_weights([row["branches"] for row in by_id.values()])
    edge_weights = idf_weights([row["edges"] for row in by_id.values()])
    root_weights = idf_weights([row["roots"] for row in by_id.values()])
    postings: dict[str, list[str]] = collections.defaultdict(list)
    for path_id, row in by_id.items():
        for node_id in row["branches"]:
            postings[node_id].append(path_id)
    possible_pairs = {
        tuple(sorted((left, right)))
        for path_ids in postings.values()
        for left_index, left in enumerate(path_ids)
        for right in path_ids[left_index + 1 :]
    }
    nearest: dict[str, list[tuple[float, str, dict[str, float]]]] = (
        collections.defaultdict(list)
    )
    for left_id, right_id in possible_pairs:
        left = by_id[left_id]
        right = by_id[right_id]
        edge_j = weighted_jaccard(left["edges"], right["edges"], edge_weights)
        branch_j = weighted_jaccard(left["branches"], right["branches"], branch_weights)
        root_j = weighted_jaccard(left["roots"], right["roots"], root_weights)
        ayah_j = len(left["ayahs"] & right["ayahs"]) / len(
            left["ayahs"] | right["ayahs"]
        )
        score = 0.45 * edge_j + 0.35 * branch_j + 0.10 * root_j + 0.10 * ayah_j
        metrics = {
            "score": score,
            "edge_jaccard": edge_j,
            "branch_jaccard": branch_j,
            "root_jaccard": root_j,
            "ayah_jaccard": ayah_j,
            "branch_containment": subject.containment(
                left["branches"], right["branches"]
            ),
            "edge_containment": subject.containment(left["edges"], right["edges"]),
        }
        nearest[left_id].append((score, right_id, metrics))
        nearest[right_id].append((score, left_id, metrics))
    top_neighbors = {}
    for path_id, rows in nearest.items():
        rows.sort(key=lambda item: (-item[0], item[1]))
        top_neighbors[path_id] = {
            neighbor for _score, neighbor, _metrics in rows[:mutual_k]
        }
    edges = []
    seen = set()
    for left_id, rows in nearest.items():
        for score, right_id, metrics in rows:
            key = tuple(sorted((left_id, right_id)))
            if key in seen:
                continue
            seen.add(key)
            mutual = right_id in top_neighbors.get(
                left_id, set()
            ) and left_id in top_neighbors.get(right_id, set())
            contained = (
                metrics["branch_containment"] >= containment_threshold
                and metrics["edge_containment"] >= 0.45
                and metrics["root_jaccard"] >= 0.55
            )
            if not ((mutual and score >= min_similarity) or contained):
                continue
            edges.append(
                {
                    "left": key[0],
                    "right": key[1],
                    **{name: round(value, 6) for name, value in metrics.items()},
                    "edge_type": (
                        "mutual_knn"
                        if mutual and score >= min_similarity
                        else "containment"
                    ),
                }
            )
    edges.sort(key=lambda row: (-row["score"], row["left"], row["right"]))
    return edges


def legacy_families(
    paths: list[dict[str, object]], edges: list[dict[str, object]], rounds: int
) -> list[dict[str, object]]:
    labels = subject.weighted_label_propagation(
        [path["path_id"] for path in paths], edges, rounds=rounds
    )
    members: dict[str, list[str]] = collections.defaultdict(list)
    for path_id, label in labels.items():
        members[label].append(path_id)
    graph: dict[str, list[tuple[str, float]]] = collections.defaultdict(list)
    for edge in edges:
        graph[edge["left"]].append((edge["right"], float(edge["score"])))
        graph[edge["right"]].append((edge["left"], float(edge["score"])))
    paths_by_id = {path["path_id"]: path for path in paths}
    families = [
        subject.family_record(index, sorted(member_ids), paths_by_id, graph)
        for index, (_label, member_ids) in enumerate(
            sorted(members.items(), key=lambda item: (-len(item[1]), min(item[1]))),
            start=1,
        )
    ]
    families.sort(key=lambda row: (-row["family_score"], row["path_family_id"]))
    return [
        {**row, "path_family_id": f"PF{index:04d}"}
        for index, row in enumerate(families, start=1)
    ]


def write_paths(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def test_memory_bounded_edges_match_legacy_algorithm() -> None:
    paths = fixture_paths()
    parameters = {
        "mutual_k": 3,
        "min_similarity": 0.16,
        "containment_threshold": 0.65,
    }
    assert subject.build_similarity_edges(paths, **parameters) == legacy_similarity_edges(
        paths, **parameters
    )


def test_streamed_family_records_match_legacy_algorithm(tmp_path: Path) -> None:
    paths = fixture_paths()
    for name, ordered_paths in (("ordered", paths), ("reversed", list(reversed(paths)))):
        source = tmp_path / f"{name}.jsonl"
        write_paths(source, ordered_paths)
        indexed, postings = subject.index_jsonl(source)
        edges = subject.build_similarity_edges_indexed(
            indexed,
            postings,
            mutual_k=3,
            min_similarity=0.16,
            containment_threshold=0.65,
        )
        labels = subject.weighted_label_propagation(
            [row.path_id for row in indexed], edges, rounds=12
        )
        assert subject.streamed_family_records(
            source, indexed, labels, edges
        ) == legacy_families(ordered_paths, edges, rounds=12)


def test_index_rejects_duplicate_path_ids(tmp_path: Path) -> None:
    source = tmp_path / "semantic_path_candidates.jsonl"
    row = path_row(
        1,
        [
            ("q:r1:B001", "r1", 1),
            ("q:r2:B001", "r2", 2),
        ],
    )
    write_paths(source, [row, row])
    try:
        subject.index_jsonl(source)
    except ValueError as error:
        assert "duplicate path_id" in str(error)
    else:
        raise AssertionError("duplicate path IDs must be rejected")


def test_adaptive_min_ayahs_boundaries() -> None:
    assert [
        (count, runner.adaptive_min_ayahs(count))
        for count in (1, 3, 4, 40, 41, 99, 100, 101, 286)
    ] == [
        (1, 4),
        (3, 4),
        (4, 4),
        (40, 4),
        (41, 5),
        (99, 10),
        (100, 10),
        (101, 10),
        (286, 10),
    ]


def test_runner_wires_adaptive_minimum_into_generation(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    runner_root = tmp_path / "latent_activation"
    catalog = (
        tmp_path
        / "quran-slm"
        / "artifacts/surah_networks_global_ensemble/s001/catalog.json"
    )
    catalog.parent.mkdir(parents=True)
    catalog.write_text('{"ayah_max": 7}', encoding="utf-8")
    runner_root.mkdir()
    monkeypatch.setattr(runner, "REPO_ROOT", runner_root)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "run_corpus_candidates.py",
            "--start-surah",
            "1",
            "--end-surah",
            "1",
            "--dry-run",
        ],
    )
    assert runner.main() == 0
    output = capsys.readouterr().out
    assert "s001 START ayahs=7 min_ayahs=4" in output
    assert "--min-ayahs 4" in output


def test_runner_skips_three_ayah_surah_before_creating_output(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    runner_root = tmp_path / "latent_activation"
    catalog = (
        tmp_path
        / "quran-slm"
        / "artifacts/surah_networks_global_ensemble/s103/catalog.json"
    )
    catalog.parent.mkdir(parents=True)
    catalog.write_text('{"ayah_max": 3}', encoding="utf-8")
    runner_root.mkdir()
    monkeypatch.setattr(runner, "REPO_ROOT", runner_root)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "run_corpus_candidates.py",
            "--start-surah",
            "103",
            "--end-surah",
            "103",
            "--workers",
            "4",
            "--skip-three-ayah-surahs",
            "--dry-run",
        ],
    )
    assert runner.main() == 0
    assert "s103 SKIP canonical_ayahs=3" in capsys.readouterr().out
    assert not (runner_root / "network/v3/experiments/corpus_neo_adaptive/s103").exists()


def test_runner_bounds_parallel_surah_workers(tmp_path: Path, monkeypatch) -> None:
    runner_root = tmp_path / "latent_activation"
    runner_root.mkdir()
    barrier = threading.Barrier(4)
    state_lock = threading.Lock()
    active: set[int] = set()
    maximum_active = 0

    def fake_process_surah(*, surah: int, **_kwargs):
        nonlocal maximum_active
        with state_lock:
            active.add(surah)
            maximum_active = max(maximum_active, len(active))
        barrier.wait(timeout=5)
        with state_lock:
            active.remove(surah)
        return "completed", None

    monkeypatch.setattr(runner, "REPO_ROOT", runner_root)
    monkeypatch.setattr(runner, "process_surah", fake_process_surah)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "run_corpus_candidates.py",
            "--start-surah",
            "1",
            "--end-surah",
            "4",
            "--workers",
            "4",
            "--dry-run",
        ],
    )
    assert runner.main() == 0
    assert maximum_active == 4


def test_parallel_runner_records_unexpected_worker_exception(
    tmp_path: Path, monkeypatch
) -> None:
    runner_root = tmp_path / "latent_activation"
    runner_root.mkdir()

    def fake_process_surah(*, surah: int, **_kwargs):
        if surah == 2:
            raise OSError("synthetic worker error")
        return "completed", None

    monkeypatch.setattr(runner, "REPO_ROOT", runner_root)
    monkeypatch.setattr(runner, "process_surah", fake_process_surah)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "run_corpus_candidates.py",
            "--start-surah",
            "1",
            "--end-surah",
            "3",
            "--workers",
            "2",
        ],
    )
    assert runner.main() == 1
    output_dir = runner_root / "network/v3/experiments/corpus_neo_adaptive"
    state = json.loads((output_dir / "corpus_run_state.json").read_text())
    assert state["completed_this_run"] == [1, 3]
    assert state["failures_this_run"] == [
        {
            "surah": 2,
            "stage": "runner",
            "reason": "OSError: synthetic worker error",
            "recorded_at": state["failures_this_run"][0]["recorded_at"],
        }
    ]
    assert (output_dir / "s002/stage_failure.json").is_file()


def test_consolidation_is_independent_of_python_hash_seed(tmp_path: Path) -> None:
    input_dir = tmp_path / "input"
    input_dir.mkdir()
    write_paths(input_dir / "semantic_path_candidates.jsonl", fixture_paths())
    outputs = []
    for seed in ("1", "987654"):
        output_dir = tmp_path / f"output-{seed}"
        environment = dict(os.environ, PYTHONHASHSEED=seed)
        subprocess.run(
            [
                sys.executable,
                str(V3_DIR / "consolidate_semantic_paths.py"),
                "--input-dir",
                str(input_dir),
                "--output-dir",
                str(output_dir),
            ],
            check=True,
            capture_output=True,
            env=environment,
        )
        outputs.append(
            {
                path.name: path.read_bytes()
                for path in sorted(output_dir.iterdir())
            }
        )
    assert outputs[0] == outputs[1]


def test_weighted_jaccard_uses_stable_full_precision_sums() -> None:
    left = frozenset(("shared", "large-a", "large-b"))
    right = frozenset(("large-a",))
    weights = {
        "shared": 9.096616778579569e-21,
        "large-a": 1.6303130223691518e21,
        "large-b": 6.309910392472112e20,
    }
    expected = weights["large-a"] / math.fsum(weights[feature] for feature in left)
    assert subject.stable_weighted_jaccard(left, right, weights) == expected
