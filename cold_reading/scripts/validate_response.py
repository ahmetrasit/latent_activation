#!/usr/bin/env python3
"""Validate a cold-reader response against the packet actually revealed."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


TOP_LEVEL_REQUIRED = {
    "reader_id",
    "focus_ref",
    "stage",
    "revealed_refs",
    "models",
    "surprise_reading",
}
TOP_LEVEL_KEYS = TOP_LEVEL_REQUIRED | {
    "discarded_or_unchanged",
}
MODEL_KEYS = {
    "model_id",
    "status",
    "confidence",
    "mechanism",
    "activation_trace",
    "structural_cues",
    "abductive_moves",
    "changed_reading",
    "minimal_triggers",
    "ablation",
}
TRACE_KEYS = {"root", "branch_id", "literal_contribution", "assigned_role"}
MOVE_KEYS = {"assumption", "why_invoked", "causal_direction", "alternatives"}
CHANGE_KEYS = {"before", "after"}
STATUSES = {"provisional", "new", "strengthened", "weakened", "revised", "discarded"}
CONFIDENCES = {"strong", "medium", "exploratory"}


def require_keys(
    record: dict[str, Any],
    required: set[str],
    label: str,
    allowed: set[str] | None = None,
) -> None:
    if allowed is None:
        allowed = required
    missing = required - record.keys()
    extra = record.keys() - allowed
    if missing:
        raise ValueError(f"{label}: missing keys {sorted(missing)}")
    if extra:
        raise ValueError(f"{label}: unexpected keys {sorted(extra)}")


def require_string(value: Any, label: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}: expected a non-empty string")


def validate(packet: dict[str, Any], response: dict[str, Any]) -> None:
    require_keys(response, TOP_LEVEL_REQUIRED, "response", TOP_LEVEL_KEYS)
    require_string(response["reader_id"], "reader_id")
    if response["focus_ref"] != packet["focus_ref"]:
        raise ValueError("focus_ref does not match packet")
    if response["stage"] != packet["stage"]:
        raise ValueError("stage does not match packet")
    if response["revealed_refs"] != packet["revealed_refs"]:
        raise ValueError("revealed_refs do not match packet order")
    if not isinstance(response["models"], list):
        raise ValueError("models must be a list")
    require_string(response["surprise_reading"], "surprise_reading")
    discarded = response.get("discarded_or_unchanged", [])
    if not isinstance(discarded, list) or not all(
        isinstance(item, str) for item in discarded
    ):
        raise ValueError("discarded_or_unchanged must be a string list")

    available = {
        inventory["root"]: {branch["branch_id"] for branch in inventory["branches"]}
        for inventory in packet["branch_inventories"]
    }
    model_ids: set[str] = set()
    for index, model in enumerate(response["models"]):
        label = f"models[{index}]"
        require_keys(model, MODEL_KEYS, label)
        require_string(model["model_id"], f"{label}.model_id")
        if model["model_id"] in model_ids:
            raise ValueError(f"duplicate model_id: {model['model_id']}")
        model_ids.add(model["model_id"])
        if model["status"] not in STATUSES:
            raise ValueError(f"{label}.status: invalid value")
        if model["confidence"] not in CONFIDENCES:
            raise ValueError(f"{label}.confidence: invalid value")
        require_string(model["mechanism"], f"{label}.mechanism")
        if not isinstance(model["activation_trace"], list):
            raise ValueError(f"{label}.activation_trace: expected list")
        for trace_index, trace in enumerate(model["activation_trace"]):
            trace_label = f"{label}.activation_trace[{trace_index}]"
            require_keys(trace, TRACE_KEYS, trace_label)
            root = trace["root"]
            branch_id = trace["branch_id"]
            if root not in available:
                raise ValueError(f"{trace_label}: root {root!r} was not revealed")
            if branch_id not in available[root]:
                raise ValueError(
                    f"{trace_label}: branch {root}/{branch_id} was not in the packet"
                )
            require_string(trace["literal_contribution"], f"{trace_label}.literal_contribution")
            require_string(trace["assigned_role"], f"{trace_label}.assigned_role")
        if not isinstance(model["structural_cues"], list) or not all(
            isinstance(item, str) for item in model["structural_cues"]
        ):
            raise ValueError(f"{label}.structural_cues: expected string list")
        if not isinstance(model["abductive_moves"], list):
            raise ValueError(f"{label}.abductive_moves: expected list")
        for move_index, move in enumerate(model["abductive_moves"]):
            move_label = f"{label}.abductive_moves[{move_index}]"
            require_keys(move, MOVE_KEYS, move_label)
            for key in ("assumption", "why_invoked", "causal_direction"):
                require_string(move[key], f"{move_label}.{key}")
            if not isinstance(move["alternatives"], list) or not all(
                isinstance(item, str) for item in move["alternatives"]
            ):
                raise ValueError(f"{move_label}.alternatives: expected string list")
        require_keys(model["changed_reading"], CHANGE_KEYS, f"{label}.changed_reading")
        for key in CHANGE_KEYS:
            require_string(model["changed_reading"][key], f"{label}.changed_reading.{key}")
        if not isinstance(model["minimal_triggers"], list) or not all(
            isinstance(item, str) for item in model["minimal_triggers"]
        ):
            raise ValueError(f"{label}.minimal_triggers: expected string list")
        require_string(model["ablation"], f"{label}.ablation")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    parser.add_argument("response", type=Path)
    args = parser.parse_args()
    packet = json.loads(args.packet.read_text(encoding="utf-8"))
    response = json.loads(args.response.read_text(encoding="utf-8"))
    validate(packet, response)
    print(f"valid: {args.response}")


if __name__ == "__main__":
    main()
