from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import numpy as np
import pytest


SCRIPT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPT_DIR))

import build_ayah_neighbors as subject


def ayah(
    index: int,
    ref: str,
    *,
    repeat_group: str | None = None,
    repeat_size: int = 1,
) -> subject.AyahRecord:
    surah, number = subject.canonical_ref_key(ref)
    return subject.AyahRecord(
        global_index=index,
        node_id=f"quran:{ref}",
        surah=surah,
        ayah=number,
        ayah_ref=ref,
        repeat_group_id=repeat_group,
        repeat_group_size=repeat_size,
    )


def test_expand_reviewed_ref_accepts_canonical_refs_and_ranges() -> None:
    assert subject.expand_reviewed_ref("2:7") == ("2:7",)
    assert subject.expand_reviewed_ref("102:1-3") == ("102:1", "102:2", "102:3")
    with pytest.raises(subject.NeighborBuildError, match="descending"):
        subject.expand_reviewed_ref("2:9-7")
    with pytest.raises(subject.NeighborBuildError, match="invalid"):
        subject.expand_reviewed_ref("2:1,2")


def test_review_loader_filters_strengths_and_normalizes_legacy_rows(
    tmp_path: Path,
) -> None:
    nodes = {
        node.ayah_ref: node
        for node in (
            ayah(0, "2:1"),
            ayah(1, "2:2"),
            ayah(2, "3:1"),
            ayah(3, "3:2"),
        )
    }
    path = tmp_path / "focus_2_1_cutoff_100.tsv"
    path.write_text(
        "strong\t2:2\tdirect\n"
        "medium\t3:1-2\tparallel range\n"
        "weak\t2:1\tignored\n"
        "reject\t9:9\tignored before reference validation\n"
        "3:2\tstrong\tlegacy reversed columns\n",
        encoding="utf-8",
    )

    reviewed, provenance = subject.load_reviewed_targets(tmp_path, "2:1", nodes)

    assert reviewed == {"2:2", "3:1", "3:2"}
    assert provenance["accepted_input_row_count"] == 3
    assert provenance["expanded_output_ref_count"] == 4
    assert provenance["normalized_ref_first_row_count"] == 1
    assert provenance["ignored_strength_counts"] == {"reject": 1, "weak": 1}


def test_neo_selection_is_same_surah_and_excludes_exact_repetitions() -> None:
    nodes = (
        ayah(0, "2:1", repeat_group="repeat:x", repeat_size=2),
        ayah(1, "2:2"),
        ayah(2, "2:3"),
        ayah(3, "2:4", repeat_group="repeat:x", repeat_size=2),
        ayah(4, "3:1"),
    )
    ranks = np.zeros((5, 5), dtype=np.uint16)
    ranks[0, 1], ranks[1, 0] = 2, 2
    ranks[0, 2], ranks[2, 0] = 5, 1
    ranks[0, 4], ranks[4, 0] = 1, 1
    neo = subject.NeoIndex.__new__(subject.NeoIndex)
    neo.nodes = nodes
    neo.by_ref = {node.ayah_ref: node for node in nodes}
    neo.refs_by_surah = {2: ("2:1", "2:2", "2:3", "2:4"), 3: ("3:1",)}
    neo.refs_by_repeat_group = {"repeat:x": ("2:1", "2:4")}
    neo.ranks = ranks

    assert neo.neo_neighbor_refs("2:1") == ("2:2", "2:3")
    assert neo.exact_same_surah_repetitions("2:1") == ("2:4",)


def test_neo_cutoff_is_exactly_50_with_stable_ties() -> None:
    nodes = tuple(ayah(index, f"2:{index + 1}") for index in range(53))
    ranks = np.zeros((53, 53), dtype=np.uint16)
    ranks[0, 1:] = 1
    ranks[1:, 0] = 1
    neo = subject.NeoIndex.__new__(subject.NeoIndex)
    neo.nodes = nodes
    neo.by_ref = {node.ayah_ref: node for node in nodes}
    neo.refs_by_surah = {2: tuple(node.ayah_ref for node in nodes)}
    neo.ranks = ranks

    selected = neo.neo_neighbor_refs("2:1")

    assert len(selected) == 50
    assert selected == tuple(f"2:{ayah_number}" for ayah_number in range(2, 52))


def test_build_artifact_emits_only_focus_and_quran_order_targets(
    tmp_path: Path,
) -> None:
    nodes = (
        ayah(0, "2:1", repeat_group="repeat:x", repeat_size=2),
        ayah(1, "2:2"),
        ayah(2, "2:3", repeat_group="repeat:x", repeat_size=2),
        ayah(3, "3:1"),
        ayah(4, "3:2"),
    )
    neo = SimpleNamespace(
        by_ref={node.ayah_ref: node for node in nodes},
        neo_neighbor_refs=lambda _focus: ("2:2",),
        exact_same_surah_repetitions=lambda _focus: ("2:3",),
    )
    (tmp_path / "focus_2_1_cutoff_100.tsv").write_text(
        "strong\t2:2\toverlap\nmedium\t3:1-2\trange\n",
        encoding="utf-8",
    )

    artifact = subject.build_artifact("2:1", neo=neo, review_dir=tmp_path)

    assert artifact == {
        "ayah_ref": "2:1",
        "target_ayat": ["2:2", "2:3", "3:1", "3:2"],
    }


def test_validator_rejects_extra_fields_duplicates_and_noncanonical_order() -> None:
    nodes = (ayah(0, "1:1"), ayah(1, "1:2"), ayah(2, "2:1"))
    neo = SimpleNamespace(by_ref={node.ayah_ref: node for node in nodes})
    subject.validate_artifact(
        {"ayah_ref": "1:1", "target_ayat": ["1:2", "2:1"]}, neo=neo
    )
    with pytest.raises(subject.NeighborBuildError, match="exactly two"):
        subject.validate_artifact(
            {"ayah_ref": "1:1", "target_ayat": [], "scores": []}, neo=neo
        )
    with pytest.raises(subject.NeighborBuildError, match="self or duplicates"):
        subject.validate_artifact(
            {"ayah_ref": "1:1", "target_ayat": ["1:2", "1:2"]}, neo=neo
        )
    with pytest.raises(subject.NeighborBuildError, match="Quran order"):
        subject.validate_artifact(
            {"ayah_ref": "1:1", "target_ayat": ["2:1", "1:2"]}, neo=neo
        )


def test_collection_audit_rejects_a_nonrederived_target_list(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    nodes = (ayah(0, "1:1"), ayah(1, "1:2"))
    neo = SimpleNamespace(
        nodes=nodes,
        by_ref={node.ayah_ref: node for node in nodes},
        provenance={"neo": "sealed"},
    )
    review_dir = tmp_path / "reviews"
    output_dir = tmp_path / "outputs"
    review_dir.mkdir()
    expected_payloads = {
        "1:1": {"ayah_ref": "1:1", "target_ayat": ["1:2"]},
        "1:2": {"ayah_ref": "1:2", "target_ayat": ["1:1"]},
    }
    for node in nodes:
        subject.review_path_for(review_dir, node.ayah_ref).write_text(
            "", encoding="utf-8"
        )
        subject.write_json_atomic(
            subject.output_path_for(output_dir, node.ayah_ref),
            expected_payloads[node.ayah_ref],
        )
    monkeypatch.setattr(
        subject,
        "build_artifact",
        lambda focus_ref, **_kwargs: copy.deepcopy(expected_payloads[focus_ref]),
    )

    manifest = subject.audit_collection(
        output_dir, neo=neo, review_dir=review_dir
    )

    assert manifest["status"] == "complete"
    assert manifest["output_count"] == 2
    altered_path = subject.output_path_for(output_dir, "1:2")
    altered = json.loads(altered_path.read_text(encoding="utf-8"))
    altered["target_ayat"] = []
    subject.write_json_atomic(altered_path, altered)
    with pytest.raises(subject.NeighborBuildError, match="exactly rederive"):
        subject.audit_collection(output_dir, neo=neo, review_dir=review_dir)
