#!/usr/bin/env python3
"""Build one hermetic focus-trace packet for a single focus ayah."""

from __future__ import annotations

import argparse
import copy
import csv
import json
import sys
from pathlib import Path
from typing import Any, Iterable

WORKFLOW_ROOT = Path(__file__).resolve().parents[1]
LATENT_ROOT = WORKFLOW_ROOT.parent
V12_SCRIPTS = LATENT_ROOT / "v12" / "scripts"
if str(V12_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(V12_SCRIPTS))

from build_full_context_packet import load_branches_with_missing
from build_packets import (
    DEFAULT_BRANCH_DB,
    DEFAULT_QAC,
    REPO_ROOT,
    load_ayat,
    ordered_unique,
    parse_refs,
    sha256,
)


BASMALAH_TEMPLATE_REF = "1:1"
BASMALAH_EXCLUDED_SURAHS = {9}
PROTOCOL = "focus-trace-hermetic-packet-v1"


def parse_ref(raw: str) -> str:
    refs = parse_refs(raw)
    if len(refs) != 1:
        raise argparse.ArgumentTypeError("expected exactly one ayah reference")
    if refs[0].endswith(":0"):
        raise argparse.ArgumentTypeError("focus ayah cannot be a synthetic basmalah ref")
    return refs[0]


def parse_radius(raw: str) -> int:
    try:
        value = int(raw)
    except ValueError as error:
        raise argparse.ArgumentTypeError("radius must be an integer") from error
    if value < 0:
        raise argparse.ArgumentTypeError("radius must be non-negative")
    return value


def surah_of(ref: str) -> int:
    return int(ref.split(":", 1)[0])


def ayah_of(ref: str) -> int:
    return int(ref.split(":", 1)[1])


def is_basmalah_ref(ref: str) -> bool:
    return ayah_of(ref) == 0


def resource_key(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(REPO_ROOT))
    except ValueError:
        return str(resolved)


def output_in_quran_data(path: Path) -> bool:
    return "quran-data" in path.resolve().parts


def numbered_refs_for_surah(qac_path: Path, surah: int) -> list[str]:
    prefix = f"{surah}:"
    refs: set[str] = set()
    with qac_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            ref = row["ayah_ref"]
            if ref.startswith(prefix):
                refs.add(ref)
    if not refs:
        raise ValueError(f"no ayat found for surah {surah}")
    return sorted(refs, key=ayah_of)


def add_basmalah_if_requested(
    refs: list[str],
    surah: int,
    include_basmalah: bool,
) -> list[str]:
    if not include_basmalah or surah in BASMALAH_EXCLUDED_SURAHS:
        return refs
    synthetic_ref = f"{surah}:0"
    if surah == 1:
        return [synthetic_ref, *[ref for ref in refs if ref != BASMALAH_TEMPLATE_REF]]
    return [synthetic_ref, *refs]


def window_for_radius(
    qac_path: Path,
    focus_ref: str,
    radius: int,
    include_basmalah: bool,
) -> list[str]:
    surah = surah_of(focus_ref)
    focus_ayah = ayah_of(focus_ref)
    refs = numbered_refs_for_surah(qac_path, surah)
    numbers = [ayah_of(ref) for ref in refs]
    start = max(min(numbers), focus_ayah - radius)
    end = min(max(numbers), focus_ayah + radius)
    window = [ref for ref in refs if start <= ayah_of(ref) <= end]
    if start == min(numbers):
        window = add_basmalah_if_requested(window, surah, include_basmalah)
    return window


def window_for_surah(qac_path: Path, focus_ref: str, include_basmalah: bool) -> list[str]:
    surah = surah_of(focus_ref)
    return add_basmalah_if_requested(
        numbered_refs_for_surah(qac_path, surah),
        surah,
        include_basmalah,
    )


def make_basmalah_ayah(template: dict[str, Any], target_ref: str) -> dict[str, Any]:
    ayah = copy.deepcopy(template)
    ayah["ref"] = target_ref
    ayah["synthetic_source_ref"] = BASMALAH_TEMPLATE_REF
    return ayah


def load_window_ayat(qac_path: Path, window: list[str]) -> dict[str, dict[str, Any]]:
    basmalah_refs = [ref for ref in window if is_basmalah_ref(ref)]
    real_refs = [ref for ref in window if not is_basmalah_ref(ref)]
    load_refs = set(real_refs)
    if basmalah_refs:
        load_refs.add(BASMALAH_TEMPLATE_REF)
    ayat = load_ayat(qac_path, load_refs)
    for ref in basmalah_refs:
        ayat[ref] = make_basmalah_ayah(ayat[BASMALAH_TEMPLATE_REF], ref)
    return ayat


def occurrence_phrase(occurrence: dict[str, Any]) -> str:
    surfaces = occurrence.get("surfaces_ar", [])
    if surfaces:
        return " ".join(surfaces)
    return ""


def source_phrases(
    ayat: Iterable[dict[str, Any]],
    root: str,
) -> list[dict[str, Any]]:
    phrases: list[dict[str, Any]] = []
    seen: set[tuple[str, str, tuple[str, ...]]] = set()
    for ayah in ayat:
        for occurrence in ayah["root_occurrences"]:
            if occurrence["root"] != root:
                continue
            phrase = occurrence_phrase(occurrence)
            key = (ayah["ref"], phrase, tuple(occurrence.get("word_indices", [])))
            if key in seen:
                continue
            seen.add(key)
            phrases.append(
                {
                    "source_ref": ayah["ref"],
                    "source_phrase_ar": phrase,
                    "source_surfaces_ar": occurrence.get("surfaces_ar", []),
                    "source_word_indices": occurrence.get("word_indices", []),
                    "source_lemmas_ar": occurrence.get("lemmas_ar", []),
                    "source_pos_tags": occurrence.get("pos_tags", []),
                }
            )
    return phrases


def first_seen_roots(ayat: Iterable[dict[str, Any]]) -> list[str]:
    return ordered_unique(
        occurrence["root"]
        for ayah in ayat
        for occurrence in ayah["root_occurrences"]
    )


def refs_by_root(ayat: Iterable[dict[str, Any]]) -> dict[str, list[str]]:
    refs: dict[str, list[str]] = {}
    for ayah in ayat:
        for occurrence in ayah["root_occurrences"]:
            root = occurrence["root"]
            refs.setdefault(root, [])
            if ayah["ref"] not in refs[root]:
                refs[root].append(ayah["ref"])
    return refs


def focus_branch(branch: dict[str, Any]) -> dict[str, Any]:
    result = {
        "branch_id": branch["branch_id"],
        "branch_image_ar": branch["image_ar"],
        "branch_image_en": branch["image_en"],
        "scope_ar": branch["scope_ar"],
        "scope_en": branch["scope_en"],
    }
    if branch.get("variants"):
        result["variants"] = [
            {
                "root_id": variant["root_id"],
                "source_path": variant["source_path"],
                "branch_image_ar": variant["image_ar"],
                "branch_image_en": variant["image_en"],
                "scope_ar": variant["scope_ar"],
                "scope_en": variant["scope_en"],
            }
            for variant in branch["variants"]
        ]
    return result


def compact_branch(branch: dict[str, Any], mode: str) -> dict[str, Any]:
    result = {
        "branch_id": branch["branch_id"],
        "branch_image_ar": branch["image_ar"],
    }
    if mode in {"images_en", "full"}:
        result["branch_image_en"] = branch["image_en"]
    if mode == "full":
        result["scope_ar"] = branch["scope_ar"]
        result["scope_en"] = branch["scope_en"]
        if branch.get("variants"):
            result["variant_count"] = len(branch["variants"])
    return result


def ordered_packet_roots(focus_ayat: list[dict[str, Any]], context_ayat: list[dict[str, Any]]) -> list[str]:
    return ordered_unique([*first_seen_roots(focus_ayat), *first_seen_roots(context_ayat)])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--focus", required=True, type=parse_ref, help="focus ayah, e.g. 100:1")
    context = parser.add_mutually_exclusive_group(required=True)
    context.add_argument("--window", type=parse_refs, help="comma-separated ayah refs")
    context.add_argument("--surah-window", action="store_true", help="use the focus ayah's whole numbered surah")
    context.add_argument("--radius", type=parse_radius, help="use N ayat before and after the focus ayah")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--qac", type=Path, default=DEFAULT_QAC)
    parser.add_argument("--branches", type=Path, default=DEFAULT_BRANCH_DB)
    parser.add_argument(
        "--include-basmalah",
        action="store_true",
        help="add a synthetic {surah}:0 basmalah when the selected window touches the start of a surah",
    )
    parser.add_argument(
        "--non-focus-branch-mode",
        choices=["images", "images_en", "full"],
        default="images",
        help="branch detail shared for context roots; all modes include branch_image_ar",
    )
    parser.add_argument(
        "--strict-branches",
        action="store_true",
        help="fail if any packet root lacks an accepted, non-contaminated branch inventory",
    )
    args = parser.parse_args()

    for path in (args.qac, args.branches):
        if not path.is_file():
            parser.error(f"resource not found: {path}")

    if args.window:
        window = args.window
    elif args.surah_window:
        window = window_for_surah(args.qac, args.focus, args.include_basmalah)
    else:
        window = window_for_radius(args.qac, args.focus, args.radius, args.include_basmalah)

    if args.focus not in window:
        parser.error("--focus must be present in the selected window")
    if any(surah_of(ref) != surah_of(args.focus) for ref in window):
        parser.error("all window refs must be in the focus surah")
    if output_in_quran_data(args.output):
        parser.error("--output must not write generated data under quran-data")

    ayat_by_ref = load_window_ayat(args.qac, window)
    ayat = [ayat_by_ref[ref] for ref in window]
    focus_ayah = ayat_by_ref[args.focus]
    context_ayat = [ayah for ayah in ayat if ayah["ref"] != args.focus]
    focus_roots = first_seen_roots([focus_ayah])
    context_roots = first_seen_roots(context_ayat)
    all_roots = ordered_packet_roots([focus_ayah], context_ayat)
    branches, missing_roots = load_branches_with_missing(args.branches, all_roots)
    if args.strict_branches and missing_roots:
        raise ValueError(
            "no accepted, non-contaminated branch inventory for roots: "
            f"{missing_roots}"
        )

    refs_for_missing = refs_by_root(ayat)
    resource_hashes = {
        resource_key(path): sha256(path)
        for path in (args.qac, args.branches)
    }

    packet = {
        "protocol": PROTOCOL,
        "focus_ref": args.focus,
        "window": window,
        "context_order": [ref for ref in window if ref != args.focus],
        "ayah_count": len(window),
        "model_profile": {
            "model": "gpt-5.6-sol",
            "reasoning_effort": "max",
        },
        "selection_policy": {
            "window_policy": (
                "The coordinator selects a fixed window. Roots are never selected "
                "or pruned by the reader."
            ),
            "focus_root_policy": (
                "All roots occurring in the focus ayah are included in first-seen "
                "focus order with full accepted, non-contaminated branch inventories."
            ),
            "context_root_policy": (
                "All roots occurring in non-focus context ayat are included in "
                "packet order and root order. Each occurrence includes source_phrase_ar."
            ),
            "non_focus_branch_policy": (
                f"Every context root with an accepted inventory includes all branch IDs "
                f"in {args.non_focus_branch_mode!r} mode; this always includes branch_image_ar."
            ),
            "source_phrase_policy": (
                "source_phrase_ar is deterministically derived from QAC surfaces_ar "
                "for the root occurrence in that source ayah."
            ),
        },
        "focus_ayah": focus_ayah,
        "context_ayat": context_ayat,
        "focus_branch_inventories": [
            {
                "root": root,
                "source_phrases": source_phrases([focus_ayah], root),
                "branches": [focus_branch(branch) for branch in branches[root]],
            }
            for root in focus_roots
            if branches[root]
        ],
        "context_root_cues": [
            {
                "root": root,
                "source_phrases": source_phrases(context_ayat, root),
                "branch_inventory_mode": args.non_focus_branch_mode,
                "branches": [
                    compact_branch(branch, args.non_focus_branch_mode)
                    for branch in branches[root]
                ],
            }
            for root in context_roots
            if branches[root]
        ],
        "missing_branch_inventories": [
            {
                "root": root,
                "refs": refs_for_missing[root],
                "source_phrases": source_phrases(ayat, root),
                "reason": "no accepted, non-contaminated branch inventory in resource",
            }
            for root in missing_roots
        ],
        "provenance": {
            "branch_filter": {
                "status": "accepted",
                "contaminated": "no",
                "origin_corpus": ["furuq", "quranic"],
            },
            "resource_sha256": resource_hashes,
            "synthetic_ayat": [
                {
                    "ref": ref,
                    "kind": "basmalah",
                    "source_ref": BASMALAH_TEMPLATE_REF,
                }
                for ref in window
                if is_basmalah_ref(ref)
            ],
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(packet, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"focus-trace packet: {args.output}")


if __name__ == "__main__":
    main()
