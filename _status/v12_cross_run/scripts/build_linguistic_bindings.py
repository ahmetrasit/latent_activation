#!/usr/bin/env python3
"""Build deterministic word, morpheme, syntax, and root-cooccurrence bindings."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
import unicodedata
from collections import defaultdict
from contextlib import closing
from pathlib import Path
from typing import Any, Iterable

from workflow_common import (
    atomic_write_compact_json,
    atomic_write_text,
    read_tsv,
    sha256_file,
    word_id_for,
    write_tsv,
)


SCRIPT_ROOT = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_ROOT.parents[2]
QAC_PATH = REPO_ROOT / "resources" / "qac.sqlite"
ATTACHMENTS_PATH = REPO_ROOT / "resources" / "attachments.tsv"
BRANCH_DB_PATH = REPO_ROOT / "resources" / "furuq_v4.sqlite"

SOURCE_TOKEN_FIELDS = (
    "source_token_id",
    "ayah_ref",
    "source_token_index",
    "surface_ar",
    "word_ids",
    "qac_word_refs",
    "binding_status",
)

WORD_FIELDS = (
    "word_id",
    "ayah_ref",
    "qac_ayah_ref",
    "word_index",
    "qac_word_ref",
    "surface_ar",
    "lemma_ar",
    "root",
    "pos",
    "aspect",
    "mood",
    "voice",
    "measure",
    "morphology_summary",
)

MORPHEME_FIELDS = (
    "morpheme_id",
    "word_id",
    "qac_ref",
    "morpheme_index",
    "surface_ar",
    "stem_ar",
    "lemma_ar",
    "root",
    "root_join_key",
    "pos",
    "morpheme_role",
    "morph_features",
    "aspect",
    "mood",
    "voice",
    "measure",
    "person",
    "gender",
    "number",
    "grammatical_case",
)

WORD_ROOT_FIELDS = (
    "word_id",
    "morpheme_ids",
    "root_id",
    "binding_status",
)

ATTACHMENT_UNIT_FIELDS = (
    "attachment_unit_id",
    "ayah_ref",
    "qac_ayah_ref",
    "unit_index",
    "word_id",
    "qac_word_ref",
    "morpheme_ids",
    "attachment_surfaces",
    "attachment_roots",
    "prep_bases",
    "binding_method",
    "binding_status",
)

SYNTAX_FIELDS = (
    "syntax_edge_id",
    "attachment_edge_id",
    "ayah_ref",
    "source_word_id",
    "target_word_id",
    "prep_word_id",
    "source_morpheme_id",
    "target_morpheme_id",
    "prep_morpheme_id",
    "source_qac_ref",
    "target_qac_ref",
    "prep_qac_ref",
    "source_attachment_unit_id",
    "target_attachment_unit_id",
    "prep_attachment_unit_id",
    "source_position",
    "target_position",
    "prep_position",
    "relation",
    "status",
    "confidence",
    "source_part",
    "target_part",
    "source_form_tag",
    "target_form_tag",
    "object_type",
    "prep_base",
    "binding_status",
    "evidence",
    "reason",
    "source_pointer",
)

COOCCURRENCE_FIELDS = (
    "cooccurrence_id",
    "ayah_ref",
    "left_word_id",
    "right_word_id",
    "left_root",
    "right_root",
    "word_distance",
    "root_distance_min",
    "root_distance_max",
    "local_pair_count",
    "corpus_window_count",
    "corpus_pair_count",
    "source_pair_id",
)


class BindingError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path, help="surah workspace")
    parser.add_argument("--packet", type=Path, help="override packet path")
    return parser.parse_args()


def canonical_arabic(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    output: list[str] = []
    for character in normalized:
        # QAC often writes long /a:/ with dagger alif, while attachment-
        # enrichment commonly writes a full alif. Preserve that value before
        # dropping other combining marks.
        if character == "\u0670":
            output.append("ا")
            continue
        if unicodedata.category(character) in {"Mn", "Me", "Cf"}:
            continue
        if character == "ـ":
            continue
        output.append(
            {
                "آ": "ا",
                "أ": "ا",
                "إ": "ا",
                "ٱ": "ا",
                "ى": "ي",
                "ؤ": "و",
                "ئ": "ي",
            }.get(character, character)
        )
    return "".join(output).replace(" ", "")


def canonical_surface_variants(value: str) -> set[str]:
    """Comparable spellings for dagger-alif and standalone-hamza variation."""
    primary = canonical_arabic(value)
    normalized = unicodedata.normalize("NFKD", value or "")
    without_dagger = "".join(
        {
            "آ": "ا",
            "أ": "ا",
            "إ": "ا",
            "ٱ": "ا",
            "ى": "ي",
            "ؤ": "و",
            "ئ": "ي",
        }.get(character, character)
        for character in normalized
        if character != "ـ"
        and character != "\u0670"
        and unicodedata.category(character) not in {"Mn", "Me", "Cf"}
    ).replace(" ", "")
    result = {primary, without_dagger}
    result.update(value.replace("ء", "ا") for value in tuple(result))
    result.update(re.sub("ا+", "ا", value) for value in tuple(result))
    return {item for item in result if item}


def canonical_root(value: str) -> str:
    return canonical_arabic(value).replace("ء", "ا")


def packet_word_tokens(text_ar: str) -> list[str]:
    """Drop standalone pause/ornament tokens while retaining Arabic words."""
    return [
        token
        for token in text_ar.split()
        if any(unicodedata.category(character).startswith("L") for character in token)
    ]


def align_source_tokens_to_qac_words(
    target_ref: str,
    source_tokens: list[str],
    qac_words: list[sqlite3.Row],
) -> list[dict[str, str]]:
    """Cross-walk displayed whitespace tokens to QAC orthographic words.

    Most spans are one-to-one. The aligner also preserves cases where either
    representation groups a surface differently, such as 37:130 where the
    displayed `إِلْ يَاسِينَ` tokens form one QAC proper-name word.
    """
    rows: list[dict[str, str]] = []
    source_index = 0
    qac_index = 0
    while source_index < len(source_tokens) and qac_index < len(qac_words):
        source_start = source_index
        qac_start = qac_index
        source_surface = canonical_arabic(source_tokens[source_index])
        qac_surface = canonical_arabic(str(qac_words[qac_index]["surface_ar"]))
        source_index += 1
        qac_index += 1

        while source_surface != qac_surface:
            if qac_surface.startswith(source_surface) and source_index < len(source_tokens):
                source_surface += canonical_arabic(source_tokens[source_index])
                source_index += 1
                continue
            if source_surface.startswith(qac_surface) and qac_index < len(qac_words):
                qac_surface += canonical_arabic(str(qac_words[qac_index]["surface_ar"]))
                qac_index += 1
                continue
            raise BindingError(
                f"{target_ref}: displayed/QAC token alignment failed at "
                f"source token {source_start + 1} and QAC word {qac_start + 1}"
            )

        source_span = source_tokens[source_start:source_index]
        qac_span = qac_words[qac_start:qac_index]
        if len(source_span) == 1 and len(qac_span) == 1:
            status = "one_to_one"
        elif len(source_span) > 1 and len(qac_span) == 1:
            status = "many_source_to_one_qac"
        elif len(source_span) == 1 and len(qac_span) > 1:
            status = "one_source_to_many_qac"
        else:
            status = "many_to_many"
        word_ids = ";".join(
            word_id_for(target_ref, int(word["word_index"])) for word in qac_span
        )
        qac_word_refs = ";".join(str(word["qac_word_ref"]) for word in qac_span)
        for offset, surface in enumerate(source_span):
            token_index = source_start + offset + 1
            rows.append(
                {
                    "source_token_id": (
                        f"t-{word_id_for(target_ref, token_index).removeprefix('w-')}"
                    ),
                    "ayah_ref": target_ref,
                    "source_token_index": str(token_index),
                    "surface_ar": surface,
                    "word_ids": word_ids,
                    "qac_word_refs": qac_word_refs,
                    "binding_status": status,
                }
            )

    if source_index != len(source_tokens) or qac_index != len(qac_words):
        raise BindingError(
            f"{target_ref}: displayed/QAC token alignment ended with unmatched items "
            f"({len(source_tokens) - source_index} source, {len(qac_words) - qac_index} QAC)"
        )
    return rows


def normalized_root_spelling(value: str) -> str:
    return " ".join(str(value or "").split())


def load_root_id_registry() -> dict[str, dict[str, list[str]]]:
    """Load exact source spellings before lossy normalized fallbacks.

    `roots.root_norm` is not unique: distinct source roots can collapse onto the
    same normalized spelling. QAC roots should therefore match the original
    `source_root_norm` first, which resolves cases such as ج ي ء versus ج ي أ
    without making an arbitrary choice.
    """
    registries: dict[str, dict[str, list[str]]] = {
        "source": defaultdict(list),
        "normalized": defaultdict(list),
        "canonical": defaultdict(list),
    }
    with closing(connect_readonly(BRANCH_DB_PATH)) as connection:
        for row in connection.execute(
            """
            SELECT root_id, root_norm, source_root_norm
            FROM roots
            ORDER BY root_norm, source_root_norm, root_id
            """
        ):
            root_id = str(row["root_id"])
            keys = {
                "source": normalized_root_spelling(row["source_root_norm"]),
                "normalized": normalized_root_spelling(row["root_norm"]),
                "canonical": canonical_root(str(row["root_norm"])),
            }
            for registry_name, key in keys.items():
                if root_id not in registries[registry_name][key]:
                    registries[registry_name][key].append(root_id)
    return {name: dict(values) for name, values in registries.items()}


def build_word_roots(
    morphemes: list[dict[str, str]],
    root_registry: dict[str, dict[str, list[str]]],
) -> tuple[list[dict[str, str]], list[str]]:
    by_word_root: dict[tuple[str, str], list[str]] = defaultdict(list)
    for morpheme in morphemes:
        raw_root = str(morpheme.get("root", ""))
        if not raw_root:
            continue
        key = (morpheme["word_id"], normalized_root_spelling(raw_root))
        if morpheme["morpheme_id"] not in by_word_root[key]:
            by_word_root[key].append(morpheme["morpheme_id"])

    rows: list[dict[str, str]] = []
    warnings: list[str] = []
    for (word_id, root_spelling), morpheme_ids in sorted(by_word_root.items()):
        root_ids = root_registry["source"].get(root_spelling, [])
        resolution = "source_exact"
        if not root_ids:
            root_ids = root_registry["normalized"].get(root_spelling, [])
            resolution = "normalized_exact"
        if not root_ids:
            root_ids = root_registry["canonical"].get(
                canonical_root(root_spelling), []
            )
            resolution = "canonical_fallback"
        if not root_ids:
            warnings.append(
                f"{word_id}: QAC root {root_spelling!r} has no database root_id"
            )
            continue
        status = (
            f"resolved_{resolution}"
            if len(root_ids) == 1
            else f"ambiguous_{resolution}"
        )
        if len(root_ids) > 1:
            warnings.append(
                f"{word_id}: QAC root {root_spelling!r} resolves to multiple "
                f"root_ids via {resolution}: {','.join(root_ids)}"
            )
        for root_id in root_ids:
            rows.append(
                {
                    "word_id": word_id,
                    "morpheme_ids": ";".join(morpheme_ids),
                    "root_id": root_id,
                    "binding_status": status,
                }
            )
    return rows, warnings


def write_table(path: Path, fields: tuple[str, ...], rows: Iterable[dict[str, Any]]) -> None:
    lines = ["\t".join(fields)]
    for row in rows:
        values: list[str] = []
        for field in fields:
            rendered = str(row.get(field, "") or "")
            if any(character in rendered for character in "\t\r\n"):
                raise BindingError(f"{path.name}: {field} contains a tab or newline")
            values.append(rendered)
        lines.append("\t".join(values))
    atomic_write_text(path, "\n".join(lines) + "\n")


def connect_readonly(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(f"{path.resolve().as_uri()}?mode=ro", uri=True)
    connection.execute("PRAGMA query_only = ON")
    connection.row_factory = sqlite3.Row
    return connection


def packet_path_for(workspace: Path, override: Path | None) -> Path:
    if override is not None:
        return override.resolve()
    rows = read_tsv(workspace / "runs.tsv")
    packet_paths = {row["packet_path"] for row in rows if row.get("packet_path")}
    if len(packet_paths) != 1:
        raise BindingError(f"expected one packet path in runs.tsv, got {sorted(packet_paths)}")
    return (REPO_ROOT / next(iter(packet_paths))).resolve()


def load_source_rows(
    connection: sqlite3.Connection, source_refs: set[str]
) -> tuple[dict[str, list[sqlite3.Row]], dict[str, list[sqlite3.Row]]]:
    words: dict[str, list[sqlite3.Row]] = {}
    morphemes: dict[str, list[sqlite3.Row]] = {}
    for source_ref in sorted(source_refs):
        surah, ayah = (int(value) for value in source_ref.split(":", 1))
        word_rows = list(
            connection.execute(
                """
                SELECT * FROM qac_words
                WHERE surah = ? AND ayah = ?
                ORDER BY word_index
                """,
                (surah, ayah),
            )
        )
        morpheme_rows = list(
            connection.execute(
                """
                SELECT * FROM qac_morphemes
                WHERE surah = ? AND ayah = ?
                ORDER BY word_index, morpheme_index
                """,
                (surah, ayah),
            )
        )
        if not word_rows or not morpheme_rows:
            raise BindingError(f"QAC has no positioned morphology for {source_ref}")
        words[source_ref] = word_rows
        morphemes[source_ref] = morpheme_rows
    return words, morphemes


def first_value(rows: list[sqlite3.Row], field: str) -> str:
    for row in rows:
        value = str(row[field] or "").strip()
        if value:
            return value
    return ""


def joined_unique(rows: list[sqlite3.Row], field: str) -> str:
    result: list[str] = []
    for row in rows:
        value = str(row[field] or "").strip()
        if value and value not in result:
            result.append(value)
    return ";".join(result)


def parsed_grammar(features: str) -> dict[str, str]:
    """Extract stable person/gender/number/case tags without replacing raw QAC."""
    tokens = [token.strip() for token in features.split("|") if token.strip()]
    person = ""
    gender = ""
    number = ""
    grammatical_case = ""
    for token in tokens:
        tag = token.rsplit(":", 1)[-1]
        match = re.fullmatch(r"([123])([MF]?)([SDP])", tag)
        if match:
            person = match.group(1)
            gender = match.group(2)
            number = {"S": "singular", "D": "dual", "P": "plural"}[match.group(3)]
            continue
        match = re.fullmatch(r"([MF])([SDP])", tag)
        if match:
            gender = match.group(1)
            number = {"S": "singular", "D": "dual", "P": "plural"}[match.group(2)]
            continue
        if tag in {"NOM", "ACC", "GEN"}:
            grammatical_case = tag
    return {
        "person": person,
        "gender": gender,
        "number": number,
        "grammatical_case": grammatical_case,
    }


def build_words_and_morphemes(
    packet: dict[str, Any],
    source_words: dict[str, list[sqlite3.Row]],
    source_morphemes: dict[str, list[sqlite3.Row]],
) -> tuple[
    list[dict[str, str]],
    list[dict[str, str]],
    list[dict[str, str]],
    dict[str, dict[int, dict[str, str]]],
    dict[str, str],
]:
    source_token_rows: list[dict[str, str]] = []
    word_rows: list[dict[str, str]] = []
    morpheme_rows: list[dict[str, str]] = []
    words_by_ref: dict[str, dict[int, dict[str, str]]] = {}
    source_by_target: dict[str, str] = {}

    for ayah in packet.get("ayat", []):
        target_ref = str(ayah["ref"])
        source_ref = str(ayah.get("synthetic_source_ref") or target_ref)
        source_by_target[target_ref] = source_ref
        by_word: dict[int, list[sqlite3.Row]] = defaultdict(list)
        for row in source_morphemes[source_ref]:
            by_word[int(row["word_index"])].append(row)

        qac_words = source_words[source_ref]
        surface_tokens = packet_word_tokens(str(ayah["text_ar"]))
        source_token_rows.extend(
            align_source_tokens_to_qac_words(target_ref, surface_tokens, qac_words)
        )

        target_index: dict[int, dict[str, str]] = {}
        for qac_word in qac_words:
            word_index = int(qac_word["word_index"])
            qac_surface = str(qac_word["surface_ar"])
            pieces = by_word[word_index]
            stems = [row for row in pieces if str(row["morpheme_role"]) == "STEM"] or pieces
            word_id = word_id_for(target_ref, word_index)
            root = joined_unique(stems, "root_ar")
            lemma = joined_unique(stems, "lemma_ar")
            pos = joined_unique(stems, "pos")
            aspect = first_value(stems, "aspect")
            mood = first_value(stems, "mood")
            voice = first_value(stems, "voice")
            measure = first_value(stems, "measure")
            morphology_summary = " | ".join(
                str(row["morph_features"] or "") for row in pieces if row["morph_features"]
            )
            output = {
                "word_id": word_id,
                "ayah_ref": target_ref,
                "qac_ayah_ref": source_ref,
                "word_index": str(word_index),
                "qac_word_ref": str(qac_word["qac_word_ref"]),
                "surface_ar": qac_surface,
                "lemma_ar": lemma,
                "root": root,
                "pos": pos,
                "aspect": aspect,
                "mood": mood,
                "voice": voice,
                "measure": measure,
                "morphology_summary": morphology_summary,
            }
            word_rows.append(output)
            target_index[word_index] = output
            for piece in pieces:
                morpheme_index = int(piece["morpheme_index"])
                grammar = parsed_grammar(str(piece["morph_features"] or ""))
                morpheme_rows.append(
                    {
                        "morpheme_id": f"m-{word_id}-{morpheme_index:02d}",
                        "word_id": word_id,
                        "qac_ref": str(piece["qac_ref"]),
                        "morpheme_index": str(morpheme_index),
                        "surface_ar": str(piece["surface_ar"] or ""),
                        "stem_ar": str(piece["stem_ar"] or ""),
                        "lemma_ar": str(piece["lemma_ar"] or ""),
                        "root": str(piece["root_ar"] or ""),
                        "root_join_key": str(piece["root_join_key"] or ""),
                        "pos": str(piece["pos"] or ""),
                        "morpheme_role": str(piece["morpheme_role"] or ""),
                        "morph_features": str(piece["morph_features"] or ""),
                        "aspect": str(piece["aspect"] or ""),
                        "mood": str(piece["mood"] or ""),
                        "voice": str(piece["voice"] or ""),
                        "measure": str(piece["measure"] or ""),
                        **grammar,
                    }
                )
        words_by_ref[target_ref] = target_index

        for occurrence in ayah.get("root_occurrences", []):
            wanted_root = canonical_root(str(occurrence["root"]))
            for raw_index in occurrence.get("word_indices", []):
                word_index = int(raw_index)
                actual = words_by_ref[target_ref].get(word_index)
                if actual is None or wanted_root not in {
                    canonical_root(value) for value in actual["root"].split(";") if value
                }:
                    raise BindingError(
                        f"{target_ref} word {word_index}: packet root {occurrence['root']!r} "
                        "does not resolve to QAC"
                    )
    return source_token_rows, word_rows, morpheme_rows, words_by_ref, source_by_target


def build_derived_attachment_units(
    words_by_ref: dict[str, dict[int, dict[str, str]]],
    morphemes: list[dict[str, str]],
    source_by_target: dict[str, str],
) -> tuple[list[dict[str, str]], dict[str, dict[int, dict[str, Any]]]]:
    """Reproduce the enrichment tokenizer from QAC morpheme boundaries."""
    by_word: dict[str, list[dict[str, str]]] = defaultdict(list)
    for morpheme in morphemes:
        by_word[morpheme["word_id"]].append(morpheme)

    output: list[dict[str, str]] = []
    units_by_ref: dict[str, dict[int, dict[str, Any]]] = {}
    for target_ref, words in words_by_ref.items():
        source_ref = source_by_target[target_ref]
        target_units: dict[int, dict[str, Any]] = {}
        unit_index = 0
        for word_index in sorted(words):
            word = words[word_index]
            pieces = sorted(
                by_word[word["word_id"]], key=lambda row: int(row["morpheme_index"])
            )
            groups: list[list[dict[str, str]]] = []
            main_group: list[dict[str, str]] = []
            for piece in pieces:
                if (
                    piece["morpheme_role"] == "PREFIX"
                    and piece["pos"] != "DET"
                ):
                    groups.append([piece])
                else:
                    main_group.append(piece)
            if main_group:
                groups.append(main_group)

            for group in groups:
                unit_index += 1
                row: dict[str, Any] = {
                    "attachment_unit_id": (
                        f"au-{target_ref.replace(':', '_')}-u{unit_index:03d}"
                    ),
                    "ayah_ref": target_ref,
                    "qac_ayah_ref": source_ref,
                    "unit_index": str(unit_index),
                    "source_unit_id": f"q:{source_ref}:{unit_index}",
                    "word_id": word["word_id"],
                    "qac_word_ref": word["qac_word_ref"],
                    "morpheme_ids": join_unique(
                        piece["morpheme_id"] for piece in group
                    ),
                    "surface_ar": "".join(piece["surface_ar"] for piece in group),
                    "root": join_unique(piece["root"] for piece in group),
                    "pos": join_unique(piece["pos"] for piece in group),
                    "binding_method": "qac_morpheme_tokenization_v1",
                    "_morphemes": group,
                }
                output.append(row)
                target_units[unit_index] = row
        units_by_ref[target_ref] = target_units
    return output, units_by_ref


def join_unique(values: Iterable[str]) -> str:
    output: list[str] = []
    for raw in values:
        value = str(raw).strip()
        if value and value not in output:
            output.append(value)
    return ";".join(output)


def attachment_position_map(
    raw_rows: list[dict[str, str]], words: dict[int, dict[str, str]]
) -> dict[int, int]:
    surfaces: dict[int, list[str]] = defaultdict(list)
    surface_prefixes: dict[int, list[str]] = defaultdict(list)
    roots: dict[int, list[str]] = defaultdict(list)
    positions: set[int] = set()
    for row in raw_rows:
        for prefix in ("head", "dep", "prep"):
            raw_position = row.get(f"{prefix}_wid", "")
            if not raw_position:
                continue
            position = int(raw_position)
            positions.add(position)
            raw_surface = row.get(f"{prefix}_surface", "")
            surface_keys = canonical_surface_variants(raw_surface)
            root = canonical_root(row.get(f"{prefix}_root_norm", ""))
            for surface in surface_keys:
                if surface not in surfaces[position]:
                    surfaces[position].append(surface)
            if root and root not in roots[position]:
                roots[position].append(root)
            if (
                prefix == "dep"
                and not surface_keys
                and row.get("dep_part") == "pronoun_suffix"
                and row.get("prep_base")
            ):
                prep_base = canonical_arabic(row["prep_base"])
                if prep_base and prep_base not in surface_prefixes[position]:
                    surface_prefixes[position].append(prep_base)
            if prefix == "prep" and row.get("prep_base"):
                prep_base = canonical_arabic(row["prep_base"])
                if prep_base and prep_base not in surface_prefixes[position]:
                    surface_prefixes[position].append(prep_base)

    all_positions = sorted(positions)
    mapping: dict[int, int] = {}
    previous = 0
    for position in all_positions:
        candidates: list[int] = []
        for word_index, word in words.items():
            word_surfaces = canonical_surface_variants(word["surface_ar"])
            word_lemmas = {
                variant
                for lemma in word["lemma_ar"].split(";")
                for variant in canonical_surface_variants(lemma)
                if lemma
            }
            word_roots = {
                canonical_root(value) for value in word["root"].split(";") if value
            }
            if surfaces[position] and word_surfaces.intersection(surfaces[position]):
                candidates.append(word_index)
            elif surface_prefixes[position] and (
                any(
                    value in word_surface[:3]
                    for value in surface_prefixes[position]
                    for word_surface in word_surfaces
                )
                or any(
                    value == lemma
                    for value in surface_prefixes[position]
                    for lemma in word_lemmas
                )
            ):
                candidates.append(word_index)
            elif roots[position] and word_roots.intersection(roots[position]):
                candidates.append(word_index)
        if not candidates:
            continue
        later = [candidate for candidate in candidates if candidate >= previous]
        selected = min(later or candidates)
        mapping[position] = selected
        previous = selected

    # Suffix-only nodes have no independent surface or root. Resolve one only
    # when secure neighboring anchors leave a single monotonic word slot.
    for position in [item for item in all_positions if item not in mapping]:
        lower = [item for item in mapping.items() if item[0] < position]
        upper = [item for item in mapping.items() if item[0] > position]
        lower_index = max(lower)[1] if lower else 0
        upper_index = min(upper)[1] if upper else max(words) + 1
        candidates = [
            index
            for index in sorted(words)
            if lower_index <= index <= upper_index and index not in mapping.values()
        ]
        if len(candidates) == 1:
            mapping[position] = candidates[0]
    return mapping


def load_attachments_for_sources(
    source_refs: set[str],
) -> dict[str, list[dict[str, str]]]:
    wanted = {
        tuple(int(value) for value in ref.split(":", 1)): ref for ref in source_refs
    }
    result: dict[str, list[dict[str, str]]] = defaultdict(list)
    with ATTACHMENTS_PATH.open(encoding="utf-8", newline="") as handle:
        for line_number, row in enumerate(csv.DictReader(handle, delimiter="\t"), start=2):
            key = (int(row["sura"]), int(row["ayah"]))
            source_ref = wanted.get(key)
            if source_ref is None:
                continue
            item = dict(row)
            item["_line"] = str(line_number)
            result[source_ref].append(item)
    return result


def resolve_endpoint_morpheme(
    raw: dict[str, str], prefix: str, unit: dict[str, Any] | None
) -> dict[str, str] | None:
    if unit is None:
        return None
    pieces: list[dict[str, str]] = unit["_morphemes"]
    part = raw.get(f"{prefix}_part", "")
    root = canonical_root(raw.get(f"{prefix}_root_norm", ""))
    form_tag = raw.get(f"{prefix}_form_tag", "")

    if part in {"object_suffix", "pronoun_suffix"}:
        candidates = [piece for piece in pieces if piece["morpheme_role"] == "SUFFIX"]
        if len(candidates) == 1:
            return candidates[0]
        candidates = [piece for piece in pieces if piece["pos"] in {"PRON", "REL"}]
        if len(candidates) == 1:
            return candidates[0]
    if prefix == "prep" and raw.get("prep_base"):
        prep_keys = canonical_surface_variants(raw["prep_base"])
        candidates = [
            piece
            for piece in pieces
            if piece["pos"] in {"P", "PRP"}
            and (
                canonical_surface_variants(piece["surface_ar"]).intersection(prep_keys)
                or canonical_surface_variants(piece["lemma_ar"]).intersection(prep_keys)
            )
        ]
        if len(candidates) == 1:
            return candidates[0]
        candidates = [piece for piece in pieces if piece["pos"] in {"P", "PRP"}]
        if len(candidates) == 1:
            return candidates[0]
    if root:
        candidates = [piece for piece in pieces if canonical_root(piece["root"]) == root]
        if len(candidates) == 1:
            return candidates[0]
    pos_hint = {"PREP": "P", "CONJ": "CONJ"}.get(form_tag)
    if pos_hint:
        candidates = [piece for piece in pieces if piece["pos"] == pos_hint]
        if len(candidates) == 1:
            return candidates[0]
    if len(pieces) == 1:
        return pieces[0]
    stems = [piece for piece in pieces if piece["morpheme_role"] == "STEM"]
    if len(stems) == 1:
        return stems[0]
    return None


def index_morphemes_by_word(
    morphemes: list[dict[str, str]],
) -> dict[str, list[dict[str, str]]]:
    result: dict[str, list[dict[str, str]]] = defaultdict(list)
    for morpheme in morphemes:
        result[morpheme["word_id"]].append(morpheme)
    for rows in result.values():
        rows.sort(key=lambda row: int(row["morpheme_index"]))
    return result


def word_as_unit(
    word: dict[str, str], morphemes_by_word: dict[str, list[dict[str, str]]]
) -> dict[str, Any]:
    return {"word_id": word["word_id"], "_morphemes": morphemes_by_word[word["word_id"]]}


def resolve_attachment_word(
    position: int,
    position_map: dict[int, int],
    words: dict[int, dict[str, str]],
    derived_units: dict[int, dict[str, Any]],
) -> tuple[dict[str, str] | None, str]:
    word_index = position_map.get(position)
    if word_index is None:
        return None, "unresolved"
    word = words[word_index]
    derived = derived_units.get(position)
    if derived is not None and derived["word_id"] == word["word_id"]:
        return word, "position_crosswalk"
    return word, "surface_root_sequence_fallback"


def build_attachment_crosswalk(
    words_by_ref: dict[str, dict[int, dict[str, str]]],
    morphemes: list[dict[str, str]],
    source_by_target: dict[str, str],
    attachments: dict[str, list[dict[str, str]]],
    derived_units_by_ref: dict[str, dict[int, dict[str, Any]]],
) -> tuple[list[dict[str, str]], list[str]]:
    morphemes_by_word = index_morphemes_by_word(morphemes)
    output: list[dict[str, str]] = []
    warnings: list[str] = []
    for target_ref, source_ref in source_by_target.items():
        raw_rows = attachments.get(source_ref, [])
        position_map = attachment_position_map(raw_rows, words_by_ref[target_ref])
        annotations: dict[int, list[tuple[dict[str, str], str]]] = defaultdict(list)
        for raw in raw_rows:
            for prefix in ("head", "dep", "prep"):
                if raw.get(f"{prefix}_wid"):
                    annotations[int(raw[f"{prefix}_wid"])].append((raw, prefix))
        for position in sorted(annotations):
            word, method = resolve_attachment_word(
                position,
                position_map,
                words_by_ref[target_ref],
                derived_units_by_ref[target_ref],
            )
            pairs = annotations[position]
            raw_unit_ids = join_unique(
                raw.get(f"{prefix}_unit_id", "") for raw, prefix in pairs
            )
            if not raw_unit_ids:
                raw_unit_ids = f"q:{source_ref}:{position}"
            if word is None:
                warnings.append(
                    f"{target_ref}:{raw_unit_ids}: unresolved attachment unit position {position}"
                )
                morpheme_ids = ""
                binding_status = "unresolved"
            else:
                unit = word_as_unit(word, morphemes_by_word)
                resolved_morphemes = [
                    resolved
                    for raw, prefix in pairs
                    if (resolved := resolve_endpoint_morpheme(raw, prefix, unit))
                    is not None
                ]
                morpheme_ids = join_unique(
                    row["morpheme_id"] for row in resolved_morphemes
                )
                binding_status = (
                    "morpheme_aligned" if morpheme_ids else "word_aligned"
                )
            output.append(
                {
                    "attachment_unit_id": raw_unit_ids,
                    "ayah_ref": target_ref,
                    "qac_ayah_ref": source_ref,
                    "unit_index": str(position),
                    "word_id": word["word_id"] if word else "",
                    "qac_word_ref": word["qac_word_ref"] if word else "",
                    "morpheme_ids": morpheme_ids,
                    "attachment_surfaces": join_unique(
                        raw.get(f"{prefix}_surface", "") for raw, prefix in pairs
                    ),
                    "attachment_roots": join_unique(
                        raw.get(f"{prefix}_root_norm", "") for raw, prefix in pairs
                    ),
                    "prep_bases": join_unique(raw.get("prep_base", "") for raw, _ in pairs),
                    "binding_method": method,
                    "binding_status": binding_status,
                }
            )
    return output, warnings


def build_syntax(
    words_by_ref: dict[str, dict[int, dict[str, str]]],
    source_by_target: dict[str, str],
    attachments: dict[str, list[dict[str, str]]],
    morphemes: list[dict[str, str]],
    derived_units_by_ref: dict[str, dict[int, dict[str, Any]]],
) -> tuple[list[dict[str, str]], list[str]]:
    output: list[dict[str, str]] = []
    warnings: list[str] = []
    morphemes_by_word = index_morphemes_by_word(morphemes)
    for target_ref, source_ref in source_by_target.items():
        raw_rows = attachments.get(source_ref, [])
        position_map = attachment_position_map(raw_rows, words_by_ref[target_ref])
        for raw in raw_rows:
            head_position = int(raw["head_wid"]) if raw.get("head_wid") else 0
            dep_position = int(raw["dep_wid"]) if raw.get("dep_wid") else 0
            prep_position = int(raw["prep_wid"]) if raw.get("prep_wid") else 0
            source_word, source_status = resolve_attachment_word(
                head_position,
                position_map,
                words_by_ref[target_ref],
                derived_units_by_ref[target_ref],
            )
            target_word, target_status = resolve_attachment_word(
                dep_position,
                position_map,
                words_by_ref[target_ref],
                derived_units_by_ref[target_ref],
            )
            if prep_position:
                prep_word, prep_status = resolve_attachment_word(
                    prep_position,
                    position_map,
                    words_by_ref[target_ref],
                    derived_units_by_ref[target_ref],
                )
            else:
                prep_word, prep_status = None, "not_present"
            source_unit = (
                word_as_unit(source_word, morphemes_by_word) if source_word else None
            )
            target_unit = (
                word_as_unit(target_word, morphemes_by_word) if target_word else None
            )
            prep_unit = word_as_unit(prep_word, morphemes_by_word) if prep_word else None
            source_morpheme = resolve_endpoint_morpheme(raw, "head", source_unit)
            target_morpheme = resolve_endpoint_morpheme(raw, "dep", target_unit)
            prep_morpheme = resolve_endpoint_morpheme(raw, "prep", prep_unit)
            if (
                source_word is None
                or target_word is None
                or (prep_position and prep_word is None)
            ):
                warnings.append(
                    f"{target_ref}:{raw['unit_id']}: unresolved attachment endpoints "
                    f"head={head_position} dep={dep_position} prep={prep_position or '-'}"
                )
            binding_states = [source_status, target_status]
            if prep_position:
                binding_states.append(prep_status)
            if "unresolved" in binding_states:
                binding_status = "unresolved"
            else:
                used_fallback = "surface_root_sequence_fallback" in binding_states
                morphemes_complete = (
                    source_morpheme is not None
                    and target_morpheme is not None
                    and (not prep_position or prep_morpheme is not None)
                )
                binding_status = (
                    ("fallback_" if used_fallback else "position_")
                    + ("morpheme_aligned" if morphemes_complete else "word_aligned")
                )
            output.append(
                {
                    "syntax_edge_id": f"sx-{target_ref.replace(':', '_')}-{len(output)+1:05d}",
                    "attachment_edge_id": raw["unit_id"],
                    "ayah_ref": target_ref,
                    "source_word_id": source_word["word_id"] if source_word else "",
                    "target_word_id": target_word["word_id"] if target_word else "",
                    "prep_word_id": prep_word["word_id"] if prep_word else "",
                    "source_morpheme_id": source_morpheme["morpheme_id"] if source_morpheme else "",
                    "target_morpheme_id": target_morpheme["morpheme_id"] if target_morpheme else "",
                    "prep_morpheme_id": prep_morpheme["morpheme_id"] if prep_morpheme else "",
                    "source_qac_ref": source_morpheme["qac_ref"] if source_morpheme else (source_word["qac_word_ref"] if source_word else ""),
                    "target_qac_ref": target_morpheme["qac_ref"] if target_morpheme else (target_word["qac_word_ref"] if target_word else ""),
                    "prep_qac_ref": prep_morpheme["qac_ref"] if prep_morpheme else (prep_word["qac_word_ref"] if prep_word else ""),
                    "source_attachment_unit_id": raw.get("head_unit_id", ""),
                    "target_attachment_unit_id": raw.get("dep_unit_id", ""),
                    "prep_attachment_unit_id": raw.get("prep_unit_id", ""),
                    "source_position": str(head_position) if head_position else "",
                    "target_position": str(dep_position) if dep_position else "",
                    "prep_position": str(prep_position) if prep_position else "",
                    "relation": raw["relation"],
                    "status": raw["status"],
                    "confidence": raw["confidence"],
                    "source_part": raw.get("head_part", ""),
                    "target_part": raw.get("dep_part", ""),
                    "source_form_tag": raw.get("head_form_tag", ""),
                    "target_form_tag": raw.get("dep_form_tag", ""),
                    "object_type": raw.get("obj_type", ""),
                    "prep_base": raw.get("prep_base", ""),
                    "binding_status": binding_status,
                    "evidence": raw.get("evidence", ""),
                    "reason": raw.get("reason", ""),
                    "source_pointer": f"resources/attachments.tsv:{raw['_line']}",
                }
            )
    return output, warnings


def build_cooccurrences(
    connection: sqlite3.Connection,
    words_by_ref: dict[str, dict[int, dict[str, str]]],
    source_by_target: dict[str, str],
) -> list[dict[str, str]]:
    global_counts = {
        (str(row["left_key"]), str(row["right_key"])): (
            int(row["window_count"]),
            int(row["pair_count"]),
        )
        for row in connection.execute(
            """
            SELECT left_key, right_key,
                   COUNT(DISTINCT window_id) AS window_count,
                   SUM(pair_count) AS pair_count
            FROM qac_cooccurrence_pairs
            WHERE left_key_type = 'root' AND right_key_type = 'root'
            GROUP BY left_key, right_key
            """
        )
    }
    result: list[dict[str, str]] = []
    for target_ref, source_ref in source_by_target.items():
        window_id = f"intra_ayah:{source_ref}"
        pairs = list(
            connection.execute(
                """
                SELECT * FROM qac_cooccurrence_pairs
                WHERE window_id = ? AND left_key_type = 'root' AND right_key_type = 'root'
                ORDER BY pair_id
                """,
                (window_id,),
            )
        )
        key_to_words: dict[str, list[dict[str, str]]] = defaultdict(list)
        for word in words_by_ref[target_ref].values():
            for root in word["root"].split(";"):
                if root:
                    key_to_words[canonical_root(root)].append(word)
        for pair in pairs:
            left_key = canonical_root(str(pair["left_key"]))
            right_key = canonical_root(str(pair["right_key"]))
            left_words = key_to_words.get(left_key, [])
            right_words = key_to_words.get(right_key, [])
            window_count, corpus_pair_count = global_counts.get(
                (str(pair["left_key"]), str(pair["right_key"])), (0, 0)
            )
            for left in left_words:
                for right in right_words:
                    result.append(
                        {
                            "cooccurrence_id": f"co-{target_ref.replace(':', '_')}-{len(result)+1:05d}",
                            "ayah_ref": target_ref,
                            "left_word_id": left["word_id"],
                            "right_word_id": right["word_id"],
                            "left_root": left["root"],
                            "right_root": right["root"],
                            "word_distance": str(
                                abs(int(left["word_index"]) - int(right["word_index"]))
                            ),
                            "root_distance_min": str(pair["distance_min"]),
                            "root_distance_max": str(pair["distance_max"]),
                            "local_pair_count": str(pair["pair_count"]),
                            "corpus_window_count": str(window_count),
                            "corpus_pair_count": str(corpus_pair_count),
                            "source_pair_id": str(pair["pair_id"]),
                        }
                    )
    return result


def enrich_existing_evidence_bindings(
    workspace: Path, morphemes: list[dict[str, str]]
) -> int:
    path = workspace / "branch_evidence.tsv"
    if not path.exists():
        return 0
    rows = read_tsv(path)
    if not rows:
        return 0
    by_word_root: dict[tuple[str, str], list[str]] = defaultdict(list)
    for morpheme in morphemes:
        root = " ".join(morpheme["root"].split())
        if root:
            by_word_root[(morpheme["word_id"], root)].append(
                morpheme["morpheme_id"]
            )
    for row in rows:
        word_id = word_id_for(row["occurrence_ref"], int(row["word_index"]))
        candidates = by_word_root.get((word_id, " ".join(row["root"].split())), [])
        if len(candidates) != 1:
            raise BindingError(
                f"{row['evidence_id']}: expected one root morpheme for {word_id}, "
                f"got {len(candidates)}"
            )
        row["word_id"] = word_id
        row["morpheme_id"] = candidates[0]
        row.setdefault("linguistic_support_ids", "")
    write_tsv(path, rows)
    return len(rows)


def build(workspace: Path, packet_override: Path | None = None) -> dict[str, Any]:
    workspace = workspace.resolve()
    packet_path = packet_path_for(workspace, packet_override)
    packet = json.loads(packet_path.read_text(encoding="utf-8"))
    source_refs = {
        str(ayah.get("synthetic_source_ref") or ayah["ref"])
        for ayah in packet.get("ayat", [])
    }
    with closing(connect_readonly(QAC_PATH)) as connection:
        source_words, source_morphemes = load_source_rows(connection, source_refs)
        (
            source_tokens,
            words,
            morphemes,
            words_by_ref,
            source_by_target,
        ) = build_words_and_morphemes(packet, source_words, source_morphemes)
        _, derived_units_by_ref = build_derived_attachment_units(
            words_by_ref, morphemes, source_by_target
        )
        attachments = load_attachments_for_sources(source_refs)
        attachment_units, unit_warnings = build_attachment_crosswalk(
            words_by_ref,
            morphemes,
            source_by_target,
            attachments,
            derived_units_by_ref,
        )
        syntax, syntax_warnings = build_syntax(
            words_by_ref,
            source_by_target,
            attachments,
            morphemes,
            derived_units_by_ref,
        )
        root_registry = load_root_id_registry()
        word_roots, root_warnings = build_word_roots(morphemes, root_registry)
        warnings = unit_warnings + syntax_warnings + root_warnings
        cooccurrences = build_cooccurrences(connection, words_by_ref, source_by_target)

    output_root = workspace / "linguistic"
    output_root.mkdir(parents=True, exist_ok=True)
    write_table(output_root / "source_tokens.tsv", SOURCE_TOKEN_FIELDS, source_tokens)
    write_table(output_root / "words.tsv", WORD_FIELDS, words)
    write_table(output_root / "morphemes.tsv", MORPHEME_FIELDS, morphemes)
    write_table(output_root / "word_roots.tsv", WORD_ROOT_FIELDS, word_roots)
    write_table(
        output_root / "attachment_units.tsv",
        ATTACHMENT_UNIT_FIELDS,
        attachment_units,
    )
    write_table(output_root / "syntax_edges.tsv", SYNTAX_FIELDS, syntax)
    write_table(
        output_root / "root_cooccurrences.tsv", COOCCURRENCE_FIELDS, cooccurrences
    )
    enriched_evidence = enrich_existing_evidence_bindings(workspace, morphemes)
    manifest = {
        "protocol": "v12-cross-run-linguistic-bindings-v2",
        "packet_path": packet_path.relative_to(REPO_ROOT).as_posix(),
        "packet_sha256": sha256_file(packet_path),
        "qac_path": QAC_PATH.relative_to(REPO_ROOT).as_posix(),
        "qac_sha256": sha256_file(QAC_PATH),
        "attachments_path": ATTACHMENTS_PATH.relative_to(REPO_ROOT).as_posix(),
        "attachments_sha256": sha256_file(ATTACHMENTS_PATH),
        "branch_db_path": BRANCH_DB_PATH.relative_to(REPO_ROOT).as_posix(),
        "branch_db_sha256": sha256_file(BRANCH_DB_PATH),
        "counts": {
            "source_tokens": len(source_tokens),
            "words": len(words),
            "morphemes": len(morphemes),
            "word_roots": len(word_roots),
            "attachment_units": len(attachment_units),
            "syntax_edges": len(syntax),
            "root_cooccurrences": len(cooccurrences),
            "existing_evidence_bindings_enriched": enriched_evidence,
        },
        "target_to_qac_ref_overrides": {
            target: source
            for target, source in source_by_target.items()
            if target != source
        },
        "warnings": warnings,
    }
    atomic_write_compact_json(output_root / "manifest.json", manifest)
    return manifest


def main() -> int:
    args = parse_args()
    manifest = build(args.workspace, args.packet)
    manifest_path = args.workspace.resolve() / "linguistic" / "manifest.json"
    print(
        json.dumps(
            {
                "manifest": manifest_path.relative_to(REPO_ROOT).as_posix(),
                "state": "ready" if not manifest["warnings"] else "review_required",
                "counts": manifest["counts"],
                "warning_count": len(manifest["warnings"]),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if not manifest["warnings"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
