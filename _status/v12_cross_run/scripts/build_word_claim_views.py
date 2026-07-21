#!/usr/bin/env python3
"""Build granular word and claim-use views from one cross-run workspace."""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

from workflow_common import atomic_write_text, join_scalar, read_tsv


WORD_FIELDS = (
    "word_id",
    "ayah_ref",
    "word_index",
    "surface_ar",
    "qac_ayah_ref",
    "qac_word_ref",
    "lemma_ar",
    "root",
    "pos",
    "aspect",
    "mood",
    "voice",
    "measure",
    "morpheme_ids",
    "qac_morpheme_refs",
    "morph_features",
    "attachment_unit_ids",
    "syntax_edge_ids",
    "evidence_ids",
    "claim_ids",
)

USE_FIELDS = (
    "focus_ayah_ref",
    "occurrence_ref",
    "word_id",
    "morpheme_id",
    "surface_ar",
    "root",
    "branch",
    "evidence_id",
    "evidence_role",
    "lexical_status",
    "resonance_strength",
    "translation_role",
    "linguistic_support_ids",
    "claim_id",
    "publication_role",
    "claim_disposition",
    "mechanism",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    return parser.parse_args()


def write_table(path: Path, fields: tuple[str, ...], rows: Iterable[dict[str, Any]]) -> None:
    lines = ["\t".join(fields)]
    for row in rows:
        values: list[str] = []
        for field in fields:
            value = str(row.get(field, "") or "")
            if any(character in value for character in "\t\r\n"):
                raise ValueError(f"{path.name}: {field} contains a tab or newline")
            values.append(value)
        lines.append("\t".join(values))
    atomic_write_text(path, "\n".join(lines) + "\n")


def build(workspace: Path) -> tuple[Path, Path]:
    workspace = workspace.resolve()
    linguistic = workspace / "linguistic"
    words = read_tsv(linguistic / "words.tsv")
    morphemes = read_tsv(linguistic / "morphemes.tsv")
    attachment_units = read_tsv(linguistic / "attachment_units.tsv")
    syntax = read_tsv(linguistic / "syntax_edges.tsv")
    evidence = read_tsv(workspace / "branch_evidence.tsv")
    claims = {row["claim_id"]: row for row in read_tsv(workspace / "claims.tsv")}

    morphemes_by_word: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in morphemes:
        morphemes_by_word[row["word_id"]].append(row)
    units_by_word: dict[str, list[str]] = defaultdict(list)
    for row in attachment_units:
        if row["word_id"]:
            units_by_word[row["word_id"]].append(row["attachment_unit_id"])
    syntax_by_word: dict[str, list[str]] = defaultdict(list)
    for row in syntax:
        for field in ("source_word_id", "target_word_id", "prep_word_id"):
            if row[field]:
                syntax_by_word[row[field]].append(row["syntax_edge_id"])
    evidence_by_word: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in evidence:
        evidence_by_word[row["word_id"]].append(row)

    word_rows: list[dict[str, str]] = []
    for word in words:
        pieces = morphemes_by_word[word["word_id"]]
        uses = evidence_by_word[word["word_id"]]
        word_rows.append(
            {
                **word,
                "morpheme_ids": join_scalar(row["morpheme_id"] for row in pieces),
                "qac_morpheme_refs": join_scalar(row["qac_ref"] for row in pieces),
                "morph_features": " | ".join(
                    row["morph_features"] for row in pieces if row["morph_features"]
                ),
                "attachment_unit_ids": join_scalar(units_by_word[word["word_id"]]),
                "syntax_edge_ids": join_scalar(syntax_by_word[word["word_id"]]),
                "evidence_ids": join_scalar(row["evidence_id"] for row in uses),
                "claim_ids": join_scalar(row["claim_id"] for row in uses),
            }
        )

    use_rows: list[dict[str, str]] = []
    for row in evidence:
        claim = claims[row["claim_id"]]
        use_rows.append(
            {
                "focus_ayah_ref": claim["ayah_ref"],
                "occurrence_ref": row["occurrence_ref"],
                "word_id": row["word_id"],
                "morpheme_id": row["morpheme_id"],
                "surface_ar": row["surface"],
                "root": row["root"],
                "branch": row["branch"],
                "evidence_id": row["evidence_id"],
                "evidence_role": row["evidence_role"],
                "lexical_status": row["lexical_status"],
                "resonance_strength": row["resonance_strength"],
                "translation_role": row["translation_role"],
                "linguistic_support_ids": row["linguistic_support_ids"],
                "claim_id": row["claim_id"],
                "publication_role": claim["publication_role"],
                "claim_disposition": claim["disposition"],
                "mechanism": claim["mechanism"],
            }
        )

    output_root = workspace / "derived"
    words_path = output_root / "ayah_words.tsv"
    uses_path = output_root / "word_branch_uses.tsv"
    write_table(words_path, WORD_FIELDS, word_rows)
    write_table(uses_path, USE_FIELDS, use_rows)
    return words_path, uses_path


def main() -> int:
    words_path, uses_path = build(parse_args().workspace)
    print(words_path)
    print(uses_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
