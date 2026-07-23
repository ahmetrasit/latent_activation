#!/usr/bin/env python3
"""Build a nonredundant blind-review bundle from v3 candidate families."""

from __future__ import annotations

import argparse
import csv
import json
import sqlite3
from pathlib import Path
from typing import Any, Iterable


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def branch_ref(branch: dict[str, Any]) -> str:
    return f"{branch['root']}:{branch['branch_id']}"


def register_branch(
    branches: dict[str, dict[str, Any]],
    branch: dict[str, Any],
) -> str:
    ref = branch_ref(branch)
    row = branches.setdefault(
        ref,
        {
            "id": ref,
            "root": branch["root"],
            "branch_id": branch["branch_id"],
            "ayahs": set(),
        },
    )
    row["ayahs"].update(int(ayah) for ayah in branch.get("ayahs", []))
    return ref


def register_many(
    branches: dict[str, dict[str, Any]],
    rows: Iterable[dict[str, Any]],
) -> list[str]:
    return [register_branch(branches, row) for row in rows]


def edge_refs(
    branches: dict[str, dict[str, Any]],
    edge: dict[str, Any],
) -> list[str]:
    return [
        register_branch(branches, edge["left"]),
        register_branch(branches, edge["right"]),
    ]


def family_support_summary(family: dict[str, Any]) -> dict[str, Any]:
    return {
        "member_count": family["member_count"],
        "root_count": family.get("root_count", len(family.get("roots", []))),
        "ayah_count": len(family.get("ayahs", [])),
        "branch_count": family.get("branch_count"),
        "candidate_count": len(family.get("candidate_ids", [])),
        "variant_candidate_count": len(family.get("variant_candidate_ids", [])),
    }


def dense_review_rows(
    families: list[dict[str, Any]],
    branches: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    rows = []
    for family in families:
        branch_groups = {
            "core": register_many(branches, family["core_branches"]),
            "optional": register_many(branches, family["optional_branches"]),
            "rare": register_many(branches, family["rare_branches"]),
        }
        rows.append(
            {
                "family_id": family["family_id"],
                "family_score": family.get(
                    "family_score", family.get("family_score_raw")
                ),
                "label_hint": family["label_hint"],
                "structural_type": family["structural_type"],
                "member_count": family["member_count"],
                "ayahs": family["ayahs"],
                "branches": branch_groups,
                "support_summary": family_support_summary(family),
            }
        )
    return rows


def sparse_support_summary(
    family: dict[str, Any],
    constructions: list[dict[str, Any]],
) -> dict[str, Any]:
    edge_counts: dict[tuple[str, str], int] = {}
    for construction in constructions:
        for left, right in construction["edges"]:
            key = tuple(sorted((left, right)))
            edge_counts[key] = edge_counts.get(key, 0) + 1

    reused_edges = [
        {"edge": list(edge), "count": count}
        for edge, count in sorted(edge_counts.items())
        if count > 1
    ]
    return {
        "member_count": family["member_count"],
        "root_count": family.get("root_count", len(family.get("roots", []))),
        "ayah_count": len(family.get("ayahs", [])),
        "branch_count": family.get("branch_count"),
        "path_count": len(family.get("path_ids", [])),
        "construction_path_count": len(constructions),
        "unique_edge_count": len(edge_counts),
        "repeated_edge_count": sum(count - 1 for count in edge_counts.values()),
        "reused_edges": reused_edges[:20],
    }


def sparse_review_rows(
    families: list[dict[str, Any]],
    branches: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    rows = []
    for family in families:
        constructions = []
        for path in family["construction_paths"]:
            register_many(branches, path["branches"])
            constructions.append(
                {
                    "path_id": path["path_id"],
                    "edges": [
                        edge_refs(branches, edge) for edge in path["tree_edges"]
                    ],
                }
            )
        branch_groups = {
            "core": register_many(branches, family["core_branches"]),
            "optional": register_many(branches, family["optional_branches"]),
        }
        rows.append(
            {
                "path_family_id": family["path_family_id"],
                "family_score": family["family_score"],
                "label_hint": family["label_hint"],
                "member_count": family["member_count"],
                "ayahs": family["ayahs"],
                "branches": branch_groups,
                "construction_paths": constructions,
                "support_summary": sparse_support_summary(family, constructions),
            }
        )
    return rows


def hydrate_branches(
    database: Path,
    branches: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    with sqlite3.connect(database) as connection:
        details = {
            f"{root}:{branch_id}": (branch_image_ar, what_is_ar)
            for root, branch_id, branch_image_ar, what_is_ar in connection.execute(
                """
                SELECT root_norm, branch_id, branch_image_ar, what_is_ar
                FROM branch_images
                """
            )
        }

    missing = sorted(set(branches) - set(details))
    if missing:
        preview = ", ".join(missing[:10])
        raise ValueError(f"branch details missing from {database}: {preview}")

    output = []
    for ref in sorted(branches):
        row = branches[ref]
        branch_image_ar, what_is_ar = details[ref]
        output.append(
            {
                "id": ref,
                "ayahs": sorted(row["ayahs"]),
                "branch_image_ar": branch_image_ar,
                "what_is_ar": what_is_ar,
            }
        )
    return output


def split_field(value: str) -> list[str]:
    if not value:
        return []
    return [item for item in value.split(";") if item]


def read_qac_context(
    path: Path,
    surah_number: int,
    branch_refs: set[str],
) -> dict[str, Any]:
    if not path.exists():
        return {"ayahs": [], "root_occurrences": []}

    wanted_roots = {ref.split(":", 1)[0] for ref in branch_refs}
    ayahs: dict[int, dict[str, Any]] = {}
    occurrences = []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if int(row["surah"]) != surah_number:
                continue

            ayah = int(row["ayah"])
            ayahs.setdefault(
                ayah,
                {
                    "ayah": ayah,
                    "ayah_ref": row["ayah_ref"],
                    "text_ar": row["ayah_text_ar"],
                    "text_norm_ar": row["ayah_text_norm_ar"],
                    "root_sequence": split_field(row["ayah_root_sequence"]),
                },
            )

            if row["root_norm"] not in wanted_roots:
                continue

            occurrences.append(
                {
                    "root": row["root_norm"],
                    "ayah": ayah,
                    "ayah_ref": row["ayah_ref"],
                    "occurrence_count": int(row["occurrence_count"]),
                    "qac_refs": split_field(row["qac_refs"]),
                    "word_indices": [
                        int(index) for index in split_field(row["word_indices"])
                    ],
                    "surfaces_ar": split_field(row["surfaces_ar"]),
                    "lemmas_ar": split_field(row["lemmas_ar"]),
                    "pos_tags": split_field(row["pos_tags"]),
                    "measures": split_field(row["measures"]),
                }
            )

    return {
        "ayahs": [ayahs[key] for key in sorted(ayahs)],
        "root_occurrences": sorted(
            occurrences, key=lambda row: (row["ayah"], row["root"])
        ),
    }


def build_bundle(
    *,
    surah_tag: str,
    dense_path: Path,
    sparse_path: Path,
    database: Path,
    qac_root_ayah_path: Path | None = None,
) -> dict[str, Any]:
    branches: dict[str, dict[str, Any]] = {}
    dense = dense_review_rows(read_jsonl(dense_path), branches)
    sparse = sparse_review_rows(read_jsonl(sparse_path), branches)
    branch_refs = set(branches)
    surah_number = int(surah_tag.removeprefix("s"))
    surface_context = (
        read_qac_context(qac_root_ayah_path, surah_number, branch_refs)
        if qac_root_ayah_path is not None
        else {"ayahs": [], "root_occurrences": []}
    )
    return {
        "surah_tag": surah_tag,
        "surface_context": surface_context,
        "branches": hydrate_branches(database, branches),
        "dense_families": dense,
        "sparse_path_families": sparse,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah-tag", required=True, help="surah tag such as s001")
    parser.add_argument(
        "--experiment-dir",
        default="network/v3/experiments/corpus_neo_adaptive",
    )
    parser.add_argument("--branch-db", default="resources/furuq_v4.sqlite")
    parser.add_argument("--qac-root-ayah", default="resources/qac_root_ayah.tsv")
    parser.add_argument("--output")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    surah_dir = Path(args.experiment_dir) / args.surah_tag
    output = Path(args.output) if args.output else surah_dir / "review_bundle.json"
    bundle = build_bundle(
        surah_tag=args.surah_tag,
        dense_path=surah_dir / "families" / "channel_families.jsonl",
        sparse_path=(
            surah_dir
            / "paths"
            / "path_families"
            / "semantic_path_families.jsonl"
        ),
        database=Path(args.branch_db),
        qac_root_ayah_path=Path(args.qac_root_ayah),
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(bundle, ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    print(output)


if __name__ == "__main__":
    main()
