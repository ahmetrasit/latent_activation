#!/usr/bin/env python3
"""Build or transform a lean pericope focus-trace packet."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable

WORKFLOW_ROOT = Path(__file__).resolve().parents[1]
if str(WORKFLOW_ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(WORKFLOW_ROOT / "scripts"))

import build_focus_trace_packet as rich  # noqa: E402
from build_packets import ordered_unique  # noqa: E402


PROTOCOL = "focus-trace-pericope-lean-v1"


def strip_text_norm(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: strip_text_norm(item)
            for key, item in value.items()
            if key != "text_norm_ar"
        }
    if isinstance(value, list):
        return [strip_text_norm(item) for item in value]
    return value


def lean_ayah(ayah: dict[str, Any]) -> dict[str, Any]:
    keep = {
        "ref": ayah["ref"],
        "text_ar": ayah["text_ar"],
        "root_sequence": ayah.get("root_sequence", []),
        "root_occurrences": ayah.get("root_occurrences", []),
    }
    if ayah.get("rootless") is True:
        keep["rootless"] = True
        if ayah.get("rootless_reason"):
            keep["rootless_reason"] = ayah["rootless_reason"]
    return strip_text_norm(keep)


def lean_surah_text(surah_text: dict[str, Any]) -> dict[str, Any]:
    return {
        "surah": surah_text["surah"],
        "ayat": [
            {
                "ref": ayah["ref"],
                "text_ar": ayah["text_ar"],
            }
            for ayah in surah_text.get("ayat", [])
        ],
    }


def lean_source_phrases(phrases: Iterable[dict[str, Any]]) -> list[dict[str, str]]:
    return [
        {"source_phrase_ar": phrase["source_phrase_ar"]}
        for phrase in phrases
        if phrase.get("source_phrase_ar")
    ]


def lean_branch(branch: dict[str, Any], include_scope_ar: bool) -> dict[str, Any]:
    item = {
        "branch_id": branch["branch_id"],
        "branch_image_ar": branch["branch_image_ar"],
    }
    if include_scope_ar and branch.get("scope_ar"):
        item["scope_ar"] = branch["scope_ar"]
    return item


def grouped_targets(
    branches: Iterable[dict[str, Any]],
    *,
    include_scope_ar: bool,
) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], dict[str, Any]] = {}
    for branch in branches:
        mapped_root_id = branch.get("mapped_root_id")
        mapped_root_norm = branch.get("mapped_root_norm")
        if not mapped_root_id or not mapped_root_norm:
            raise ValueError("branch is missing mapped_root_id or mapped_root_norm")
        key = (mapped_root_id, mapped_root_norm)
        group = groups.setdefault(
            key,
            {
                "mapped_root_id": mapped_root_id,
                "mapped_root_norm": mapped_root_norm,
                "branches": [],
            },
        )
        branch_item = lean_branch(branch, include_scope_ar)
        branch_key = (
            branch_item["branch_id"],
            branch_item["branch_image_ar"],
            branch_item.get("scope_ar", ""),
        )
        existing = {
            (
                item["branch_id"],
                item["branch_image_ar"],
                item.get("scope_ar", ""),
            )
            for item in group["branches"]
        }
        if branch_key not in existing:
            group["branches"].append(branch_item)
    return [group for group in groups.values() if group["branches"]]


def lean_focus_inventory(inventory: dict[str, Any]) -> dict[str, Any]:
    item: dict[str, Any] = {"root": inventory["root"]}
    phrases = lean_source_phrases(inventory.get("source_phrases", []))
    if phrases:
        item["source_phrases"] = phrases
    item["targets"] = grouped_targets(
        inventory.get("branches", []),
        include_scope_ar=True,
    )
    return item


def lean_context_cues(
    cues: Iterable[dict[str, Any]],
    focus_roots: set[str],
) -> list[dict[str, Any]]:
    result = []
    for cue in cues:
        root = cue["root"]
        if root in focus_roots:
            continue
        targets = grouped_targets(cue.get("branches", []), include_scope_ar=False)
        if targets:
            result.append({"root": root, "targets": targets})
    return result


def merge_remote_cue(
    by_root: dict[str, dict[str, Any]],
    cue: dict[str, Any],
    window: set[str],
) -> None:
    root = cue.get("root")
    if not root:
        return
    source_refs = [
        ref for ref in cue.get("source_refs", [])
        if ref not in window
    ]
    if not source_refs:
        return
    item = by_root.setdefault(root, {"root": root, "source_refs": [], "targets": []})
    item["source_refs"] = ordered_unique([*item["source_refs"], *source_refs])
    merged_targets = {
        (target["mapped_root_id"], target["mapped_root_norm"]): target
        for target in item["targets"]
    }
    for target in grouped_targets(cue.get("branches", []), include_scope_ar=False):
        key = (target["mapped_root_id"], target["mapped_root_norm"])
        current = merged_targets.setdefault(
            key,
            {
                "mapped_root_id": target["mapped_root_id"],
                "mapped_root_norm": target["mapped_root_norm"],
                "branches": [],
            },
        )
        existing = {
            (branch["branch_id"], branch["branch_image_ar"])
            for branch in current["branches"]
        }
        for branch in target["branches"]:
            key_branch = (branch["branch_id"], branch["branch_image_ar"])
            if key_branch not in existing:
                current["branches"].append(branch)
                existing.add(key_branch)
    item["targets"] = list(merged_targets.values())


def lean_remote_orientation(remote: dict[str, Any], window: Iterable[str]) -> dict[str, Any]:
    refs: list[str] = []
    by_root: dict[str, dict[str, Any]] = {}
    window_set = set(window)

    slm = remote.get("slm_same_surah_reviewed") or {}
    neo = remote.get("neo_same_surah_branch_potential") or {}
    refs.extend(ref for ref in slm.get("neighbor_refs", []) or [] if ref not in window_set)
    refs.extend(ref for ref in neo.get("selected_refs", []) or [] if ref not in window_set)

    for cue in slm.get("root_cues", []) or []:
        merge_remote_cue(by_root, cue, window_set)
    for cue in neo.get("cross_root_cues", []) or []:
        merge_remote_cue(by_root, cue, window_set)

    return {
        "citable": False,
        "refs": ordered_unique(refs),
        "root_cues": [
            cue
            for cue in by_root.values()
            if cue["source_refs"] and cue["targets"]
        ],
    }


def lean_packet(packet: dict[str, Any]) -> dict[str, Any]:
    if packet.get("protocol") == PROTOCOL:
        validate_lean_packet(packet)
        return packet

    focus_inventories = [
        lean_focus_inventory(inventory)
        for inventory in packet.get("focus_branch_inventories", [])
    ]
    focus_roots = {inventory["root"] for inventory in focus_inventories}
    result = {
        "protocol": PROTOCOL,
        "focus_ref": packet["focus_ref"],
        "window": packet["window"],
        "context_order": packet["context_order"],
        "ayah_count": packet["ayah_count"],
        "focus_ayah": lean_ayah(packet["focus_ayah"]),
        "context_ayat": [
            lean_ayah(ayah)
            for ayah in packet.get("context_ayat", [])
        ],
        "surah_text": lean_surah_text(packet["surah_text"]),
        "focus_branch_inventories": focus_inventories,
        "context_root_cues": lean_context_cues(
            packet.get("context_root_cues", []),
            focus_roots,
        ),
        "remote_orientation": lean_remote_orientation(
            packet.get("remote_orientation", {}),
            packet["window"],
        ),
    }
    validate_lean_packet(result)
    return result


def _walk_keys(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from _walk_keys(item)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_keys(item)


def _validate_targets(targets: Any, label: str) -> None:
    if not isinstance(targets, list) or not targets:
        raise ValueError(f"{label}.targets must be a non-empty list")
    for index, target in enumerate(targets):
        target_label = f"{label}.targets[{index}]"
        if not isinstance(target, dict):
            raise ValueError(f"{target_label} must be an object")
        for key in ("mapped_root_id", "mapped_root_norm"):
            if not isinstance(target.get(key), str) or not target[key]:
                raise ValueError(f"{target_label}.{key} is required")
        branches = target.get("branches")
        if not isinstance(branches, list) or not branches:
            raise ValueError(f"{target_label}.branches must be a non-empty list")
        for branch_index, branch in enumerate(branches):
            branch_label = f"{target_label}.branches[{branch_index}]"
            for key in ("branch_id", "branch_image_ar"):
                if not isinstance(branch.get(key), str) or not branch[key]:
                    raise ValueError(f"{branch_label}.{key} is required")


def validate_lean_packet(packet: dict[str, Any]) -> None:
    if packet.get("protocol") != PROTOCOL:
        raise ValueError(f"packet protocol must be {PROTOCOL}")
    window = packet.get("window")
    if not isinstance(window, list) or not window:
        raise ValueError("packet.window must be a non-empty list")
    if packet.get("focus_ref") not in window:
        raise ValueError("focus_ref is not in packet.window")
    if packet.get("ayah_count") != len(window):
        raise ValueError("ayah_count does not match packet.window")
    if packet.get("context_order") != [ref for ref in window if ref != packet["focus_ref"]]:
        raise ValueError("context_order does not match packet.window")

    banned_keys = {
        "text_norm_ar",
        "branch_image_en",
        "scope_en",
        "what_is_en",
        "source_path",
        "root_mapping",
        "root_mappings",
        "mapped_source_root_norm",
        "mapped_target_rank",
        "mapped_is_dominant",
        "mapped_target_occurrences",
        "qac_total_occurrences",
        "matched_occurrences",
        "target_occurrences",
        "selection_policy",
        "provenance",
        "model_profile",
    }
    present_banned = sorted(set(_walk_keys(packet)) & banned_keys)
    if present_banned:
        raise ValueError(f"lean packet contains stripped fields: {present_banned}")

    focus = packet.get("focus_ayah")
    if not isinstance(focus, dict) or focus.get("ref") != packet["focus_ref"]:
        raise ValueError("focus_ayah is missing or has wrong ref")
    context_refs = [ayah.get("ref") for ayah in packet.get("context_ayat", [])]
    if context_refs != packet["context_order"]:
        raise ValueError("context_ayat refs do not match context_order")
    surah_text = packet.get("surah_text", {})
    if not isinstance(surah_text.get("ayat"), list) or not surah_text["ayat"]:
        raise ValueError("surah_text.ayat must be a non-empty list")

    focus_roots: set[str] = set()
    for index, inventory in enumerate(packet.get("focus_branch_inventories", [])):
        label = f"focus_branch_inventories[{index}]"
        root = inventory.get("root")
        if not isinstance(root, str) or not root:
            raise ValueError(f"{label}.root is required")
        if root in focus_roots:
            raise ValueError(f"duplicate focus root: {root}")
        focus_roots.add(root)
        _validate_targets(inventory.get("targets"), label)

    context_roots: set[str] = set()
    for index, cue in enumerate(packet.get("context_root_cues", [])):
        label = f"context_root_cues[{index}]"
        root = cue.get("root")
        if not isinstance(root, str) or not root:
            raise ValueError(f"{label}.root is required")
        if root in focus_roots:
            raise ValueError(f"{label}.root duplicates a focus inventory root")
        if root in context_roots:
            raise ValueError(f"duplicate context root: {root}")
        context_roots.add(root)
        _validate_targets(cue.get("targets"), label)

    remote = packet.get("remote_orientation")
    if not isinstance(remote, dict) or remote.get("citable") is not False:
        raise ValueError("remote_orientation.citable must be false")
    remote_refs = remote.get("refs", [])
    if not isinstance(remote_refs, list):
        raise ValueError("remote_orientation.refs must be a list")
    overlap = set(remote_refs) & set(window)
    if overlap:
        raise ValueError(f"remote_orientation.refs overlap packet window: {sorted(overlap)}")
    for index, cue in enumerate(remote.get("root_cues", [])):
        label = f"remote_orientation.root_cues[{index}]"
        source_refs = cue.get("source_refs")
        if not isinstance(source_refs, list) or not source_refs:
            raise ValueError(f"{label}.source_refs must be a non-empty list")
        _validate_targets(cue.get("targets"), label)


def selected_window(args: argparse.Namespace, parser: argparse.ArgumentParser) -> list[str]:
    if args.window:
        window = args.window
        try:
            rich.validate_window_refs(args.quran_dir, args.focus, window)
        except ValueError as error:
            parser.error(str(error))
        return window
    if args.surah_window:
        return rich.window_for_surah(args.quran_dir, args.focus, args.include_basmalah)
    return rich.window_for_radius(args.quran_dir, args.focus, args.radius, args.include_basmalah)


def build_lean_from_sources(
    args: argparse.Namespace,
    parser: argparse.ArgumentParser,
) -> dict[str, Any]:
    for path in (args.qac, args.branches, args.root_map):
        if not path.is_file():
            parser.error(f"resource not found: {path}")
    if not args.quran_dir.is_dir():
        parser.error(f"resource directory not found: {args.quran_dir}")

    window = selected_window(args, parser)
    if args.focus not in window:
        parser.error("--focus must be present in the selected window")
    if any(rich.surah_of(ref) != rich.surah_of(args.focus) for ref in window):
        parser.error("all window refs must be in the focus surah")
    if rich.output_in_quran_data(args.output):
        parser.error("--output must not write generated data under quran-data")

    ayat_by_ref = rich.load_window_ayat(args.qac, args.quran_dir, window)
    ayat = [ayat_by_ref[ref] for ref in window]
    focus_ayah = ayat_by_ref[args.focus]
    context_ayat = [ayah for ayah in ayat if ayah["ref"] != args.focus]
    focus_roots = rich.first_seen_roots([focus_ayah])
    context_roots = rich.first_seen_roots(context_ayat)
    all_roots = rich.ordered_packet_roots([focus_ayah], context_ayat)
    root_mappings = rich.load_root_mappings(args.root_map, all_roots)
    branches, missing_roots, _missing_targets = rich.load_branches_for_mapped_roots(
        args.branches,
        root_mappings,
    )
    packet_missing_roots = [root for root in all_roots if root in set(missing_roots)]
    if args.strict_branches and packet_missing_roots:
        raise ValueError(
            "no non-contaminated branch inventory for roots: "
            f"{packet_missing_roots}"
        )

    rich_packet = {
        "protocol": rich.PROTOCOL,
        "focus_ref": args.focus,
        "window": window,
        "context_order": [ref for ref in window if ref != args.focus],
        "ayah_count": len(window),
        "focus_ayah": focus_ayah,
        "context_ayat": context_ayat,
        "focus_branch_inventories": [
            {
                "root": root,
                "source_phrases": rich.source_phrases([focus_ayah], root),
                "branches": [rich.focus_branch(branch) for branch in branches[root]],
            }
            for root in focus_roots
            if branches[root]
        ],
        "context_root_cues": [
            {
                "root": root,
                "branches": [
                    rich.compact_branch(branch, "images")
                    for branch in branches[root]
                ],
            }
            for root in context_roots
            if branches[root]
        ],
        "surah_text": rich.surah_text_context(args.quran_dir, rich.surah_of(args.focus)),
        "remote_orientation": {},
    }
    return lean_packet(rich_packet)


def parse_args() -> tuple[argparse.Namespace, argparse.ArgumentParser]:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--from-rich",
        type=Path,
        help="transform an existing rich packet instead of building from resources",
    )
    parser.add_argument("--focus", type=rich.parse_ref, help="focus ayah, e.g. 10:89")
    context = parser.add_mutually_exclusive_group()
    context.add_argument("--window", type=rich.parse_refs, help="comma-separated ayah refs")
    context.add_argument("--surah-window", action="store_true", help="use the focus ayah's whole numbered surah")
    context.add_argument("--radius", type=rich.parse_radius, help="use N ayat before and after the focus ayah")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--qac", type=Path, default=rich.DEFAULT_QAC)
    parser.add_argument("--quran-dir", type=Path, default=rich.DEFAULT_QURAN_DIR)
    parser.add_argument("--branches", type=Path, default=rich.DEFAULT_BRANCH_DB)
    parser.add_argument("--root-map", type=Path, default=rich.DEFAULT_QAC_FURUQ_ROOT_MAP)
    parser.add_argument("--include-basmalah", action="store_true")
    parser.add_argument("--strict-branches", action="store_true")
    args = parser.parse_args()
    if args.from_rich:
        if args.focus or args.window or args.surah_window or args.radius is not None:
            parser.error("--from-rich cannot be combined with source window arguments")
    else:
        if not args.focus:
            parser.error("--focus is required unless --from-rich is used")
        if not (args.window or args.surah_window or args.radius is not None):
            parser.error("one of --window, --surah-window, or --radius is required")
    return args, parser


def main() -> None:
    args, parser = parse_args()
    if args.from_rich:
        packet = json.loads(args.from_rich.read_text(encoding="utf-8"))
        lean = lean_packet(packet)
    else:
        lean = build_lean_from_sources(args, parser)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(lean, ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    print(f"lean pericope focus-trace packet: {args.output}")


if __name__ == "__main__":
    main()
