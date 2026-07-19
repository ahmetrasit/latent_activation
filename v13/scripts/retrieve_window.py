#!/usr/bin/env python3
"""Retrieve deterministic v13 dynamic context packets.

v13 keeps the v12 evidence semantics but changes delivery: a reader asks for the
current focus ayah's five-ayah local window, and this script returns only newly
unseen ayat/root branches as a delta while recording all retrievals in a state
file.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
V12_SCRIPTS = REPO_ROOT / "v12" / "scripts"
sys.path.insert(0, str(V12_SCRIPTS))

from build_packets import (  # noqa: E402
    DEFAULT_BRANCH_DB,
    DEFAULT_QAC,
    load_ayat,
    ordered_unique,
    parse_refs,
    sha256,
)
from build_full_context_packet import (  # noqa: E402
    BASMALAH_TEMPLATE_REF,
    first_seen_roots,
    is_basmalah_ref,
    load_branches_with_missing,
    make_basmalah_ayah,
    refs_for_surah,
    root_refs,
)


PROTOCOL = "v13-dynamic-retrieval-packet-v1"
STATE_PROTOCOL = "v13-dynamic-retrieval-state-v1"
DEFAULT_RADIUS = 2


def parse_surah(raw: str) -> int:
    if not raw.isdigit() or int(raw) < 1:
        raise argparse.ArgumentTypeError("expected a positive surah number")
    return int(raw)


def rel(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(REPO_ROOT))
    except ValueError:
        return str(resolved)


def ref_sort_key(ref: str) -> tuple[int, int]:
    surah_raw, ayah_raw = ref.split(":", 1)
    return int(surah_raw), int(ayah_raw)


def ordered_refs_for_source(args: argparse.Namespace) -> list[str]:
    if args.surah is not None:
        return refs_for_surah(args.qac, args.surah)
    return args.run_window


def focus_window(selected_refs: list[str], focus_ref: str, radius: int) -> list[str]:
    if focus_ref not in selected_refs:
        raise ValueError(f"focus ref {focus_ref} is outside selected window")
    index = selected_refs.index(focus_ref)
    start = max(0, index - radius)
    end = min(len(selected_refs), index + radius + 1)
    return selected_refs[start:end]


def load_ayat_with_basmalah(qac_path: Path, refs: Iterable[str]) -> list[dict[str, Any]]:
    ordered_refs = list(refs)
    basmalah_refs = [ref for ref in ordered_refs if is_basmalah_ref(ref)]
    real_refs = [ref for ref in ordered_refs if not is_basmalah_ref(ref)]
    load_refs = set(real_refs)
    if basmalah_refs:
        load_refs.add(BASMALAH_TEMPLATE_REF)
    ayat_by_ref = load_ayat(qac_path, load_refs)
    for ref in basmalah_refs:
        ayat_by_ref[ref] = make_basmalah_ayah(
            ayat_by_ref[BASMALAH_TEMPLATE_REF],
            ref,
        )
    return [ayat_by_ref[ref] for ref in ordered_refs]


def empty_state(
    *,
    selected_refs: list[str],
    radius: int,
    resource_hashes: dict[str, str],
) -> dict[str, Any]:
    return {
        "protocol": STATE_PROTOCOL,
        "selected_window": selected_refs,
        "radius": radius,
        "seen_ayat": [],
        "seen_roots": [],
        "available_roots": [],
        "missing_roots": [],
        "retrievals": [],
        "provenance": {
            "resource_sha256": resource_hashes,
            "branch_filter": {
                "status": "accepted",
                "contaminated": "no",
                "origin_corpus": ["furuq", "quranic"],
            },
        },
    }


def load_state(
    path: Path,
    *,
    selected_refs: list[str],
    radius: int,
    resource_hashes: dict[str, str],
) -> dict[str, Any]:
    if not path.exists():
        return empty_state(
            selected_refs=selected_refs,
            radius=radius,
            resource_hashes=resource_hashes,
        )
    state = json.loads(path.read_text(encoding="utf-8"))
    if state.get("protocol") != STATE_PROTOCOL:
        raise ValueError(f"state protocol is not {STATE_PROTOCOL}")
    if state.get("selected_window") != selected_refs:
        raise ValueError("state selected_window differs from requested source")
    if state.get("radius") != radius:
        raise ValueError("state radius differs from requested radius")
    existing_hashes = state.get("provenance", {}).get("resource_sha256")
    if existing_hashes != resource_hashes:
        raise ValueError("state resource hashes differ from current resources")
    return state


def state_summary(state: dict[str, Any]) -> dict[str, int]:
    return {
        "seen_ayah_count": len(state["seen_ayat"]),
        "seen_root_count": len(state["seen_roots"]),
        "available_root_count": len(state["available_roots"]),
        "missing_root_count": len(state["missing_roots"]),
        "retrieval_count": len(state["retrievals"]),
    }


def update_ordered_unique(existing: list[str], additions: Iterable[str]) -> list[str]:
    return ordered_unique([*existing, *additions])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--surah", type=parse_surah, help="surah number, e.g. 100")
    source.add_argument(
        "--run-window",
        type=parse_refs,
        help="comma-separated selected run ayah refs",
    )
    parser.add_argument("--focus", required=True, help="fixed/focus ayah ref")
    parser.add_argument("--state", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--radius", type=int, default=DEFAULT_RADIUS)
    parser.add_argument("--qac", type=Path, default=DEFAULT_QAC)
    parser.add_argument("--branches", type=Path, default=DEFAULT_BRANCH_DB)
    parser.add_argument(
        "--retrospective-sweep",
        action="store_true",
        help="retrieve the entire selected run window for final retrospective review",
    )
    parser.add_argument(
        "--strict-branches",
        action="store_true",
        help="fail when a newly requested root lacks accepted branch inventory",
    )
    args = parser.parse_args()

    if args.radius < 0:
        parser.error("--radius must be non-negative")
    for path in (args.qac, args.branches):
        if not path.is_file():
            parser.error(f"resource not found: {path}")

    selected_refs = ordered_refs_for_source(args)
    if args.focus not in selected_refs:
        parser.error("--focus must be inside the selected source")
    resource_hashes = {
        rel(path): sha256(path)
        for path in (args.qac, args.branches)
    }
    state = load_state(
        args.state,
        selected_refs=selected_refs,
        radius=args.radius,
        resource_hashes=resource_hashes,
    )

    active_window = (
        selected_refs
        if args.retrospective_sweep
        else focus_window(selected_refs, args.focus, args.radius)
    )
    active_ayat = load_ayat_with_basmalah(args.qac, active_window)
    active_roots = first_seen_roots(active_ayat)
    seen_ayat_before = set(state["seen_ayat"])
    seen_roots_before = set(state["seen_roots"])
    new_ayah_refs = [ref for ref in active_window if ref not in seen_ayat_before]
    new_roots = [root for root in active_roots if root not in seen_roots_before]

    branches: dict[str, list[dict[str, Any]]] = {}
    missing_roots: list[str] = []
    if new_roots:
        branches, missing_roots = load_branches_with_missing(args.branches, new_roots)
        if args.strict_branches and missing_roots:
            raise ValueError(
                "no accepted, non-contaminated branch inventory for roots: "
                f"{missing_roots}"
            )
    refs_by_root = root_refs(active_ayat)
    new_branch_inventories = [
        {"root": root, "branches": branches[root]}
        for root in new_roots
        if branches.get(root)
    ]
    new_missing_branch_inventories = [
        {
            "root": root,
            "refs": refs_by_root.get(root, []),
            "reason": "no accepted, non-contaminated branch inventory in resource",
        }
        for root in missing_roots
    ]

    packet = {
        "protocol": PROTOCOL,
        "mode": "retrospective_sweep" if args.retrospective_sweep else "focus",
        "focus_ref": args.focus,
        "radius": args.radius,
        "selected_window_size": len(selected_refs),
        "active_window": active_window,
        "active_ayat": active_ayat,
        "new_ayah_refs": new_ayah_refs,
        "active_roots": active_roots,
        "new_roots": new_roots,
        "cached_roots": [root for root in active_roots if root in seen_roots_before],
        "cached_available_roots": [
            root
            for root in active_roots
            if root in set(state["available_roots"])
        ],
        "cached_missing_roots": [
            root
            for root in active_roots
            if root in set(state["missing_roots"])
        ],
        "new_branch_inventories": new_branch_inventories,
        "new_missing_branch_inventories": new_missing_branch_inventories,
        "state_before": state_summary(state),
        "provenance": {
            "branch_filter": state["provenance"]["branch_filter"],
            "resource_sha256": resource_hashes,
            "synthetic_ayat": [
                {
                    "ref": ref,
                    "kind": "basmalah",
                    "source_ref": BASMALAH_TEMPLATE_REF,
                }
                for ref in active_window
                if is_basmalah_ref(ref)
            ],
        },
    }

    state["seen_ayat"] = update_ordered_unique(state["seen_ayat"], active_window)
    state["seen_roots"] = update_ordered_unique(state["seen_roots"], new_roots)
    state["available_roots"] = update_ordered_unique(
        state["available_roots"],
        [item["root"] for item in new_branch_inventories],
    )
    state["missing_roots"] = update_ordered_unique(state["missing_roots"], missing_roots)
    retrieval_record = {
        "focus_ref": args.focus,
        "mode": packet["mode"],
        "output": rel(args.output),
        "active_window": active_window,
        "new_ayah_refs": new_ayah_refs,
        "new_roots": new_roots,
        "new_missing_roots": missing_roots,
    }
    state["retrievals"].append(retrieval_record)
    packet["state_after"] = state_summary(state)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(packet, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    args.state.parent.mkdir(parents=True, exist_ok=True)
    args.state.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"v13 retrieval packet: {args.output}")
    print(f"v13 retrieval state: {args.state}")


if __name__ == "__main__":
    main()
