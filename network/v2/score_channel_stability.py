#!/usr/bin/env python3
"""Compress S1 image-facet review groups into stability-scored channels."""

from __future__ import annotations

import argparse
import collections
import csv
import json
import math
from pathlib import Path
from typing import Any


BROAD_OR_PRIMARY_FACETS = {
    "kw:adoration",
    "kw:creed",
    "kw:deity",
    "kw:devotion",
    "kw:divinity",
    "kw:gratitude",
    "kw:monotheism",
    "kw:pity",
    "kw:praise",
    "kw:religion",
    "kw:submission",
    "kw:obedience",
    "kw:theology",
    "kw:worship",
    "theme:ritual_belief/religion_worship",
    "theme:ritual_belief/ritual",
    "theme:ritual_belief/belief_revelation",
}


NOISE_FACET_TERMS = {
    "antiquity",
    "blade",
    "ceiling",
    "condiment",
    "duration",
    "falcon",
    "grammar",
    "hawk",
    "indemnity",
    "ingestion",
    "palm",
    "particle",
    "paste",
    "preposition",
    "raptor",
    "restitution",
    "sword",
    "swallowing",
    "syrup",
}


DOMAIN_RULES = [
    {
        "domain_id": "D01",
        "label": "guidance / road / deviation",
        "terms": {
            "direction",
            "guidance",
            "journey",
            "landmark",
            "navigation",
            "path",
            "paving",
            "rectitude",
            "road",
            "straightness",
            "travel",
        },
    },
    {
        "domain_id": "D02",
        "label": "mercy / blessing / provision",
        "terms": {
            "benefit",
            "blessing",
            "bounty",
            "compassion",
            "gift",
            "grace",
            "hospitality_welfare",
            "kindness",
            "kinship",
            "provision",
            "repair",
            "tenderness",
            "welfare",
        },
    },
    {
        "domain_id": "D03",
        "label": "authority / obedience / standing",
        "terms": {
            "authority",
            "chattel",
            "dominion",
            "hierarchy",
            "kingship",
            "law_governance",
            "obligation_contract",
            "politics_order",
            "property",
            "servitude",
            "sovereignty",
            "standing",
        },
    },
    {
        "domain_id": "D04",
        "label": "anger / honor / rejection",
        "terms": {
            "anger",
            "defiance",
            "fear_grief",
            "fury",
            "honor",
            "honor_shame",
            "jealousy",
            "mourning",
            "opposition",
            "protectiveness",
            "resentment",
            "wrath",
            "zeal",
        },
    },
    {
        "domain_id": "D05",
        "label": "name / invocation / obligation",
        "terms": {
            "address",
            "appellation",
            "designation",
            "identity_personhood",
            "invocation",
            "language",
            "name",
            "oath",
            "semiotics",
        },
    },
    {
        "domain_id": "D06",
        "label": "sign / knowledge / marker",
        "terms": {
            "banner",
            "classification",
            "education",
            "heraldry",
            "knowledge",
            "knowledge_learning",
            "landmark",
            "marker",
            "proof_uncertainty",
            "sage",
            "scholar",
            "semiotics",
        },
    },
    {
        "domain_id": "D07",
        "label": "verticality / sky / concealment",
        "terms": {
            "ascent",
            "astronomy",
            "burial",
            "canopy",
            "daylight",
            "disappearance",
            "elevation",
            "eminence",
            "height",
            "hiddenness",
            "light",
            "loftiness",
            "overhead",
            "sky",
            "sky_astronomy",
        },
    },
    {
        "domain_id": "D08",
        "label": "aid / intention / undertaking",
        "terms": {
            "agency",
            "aid",
            "assistance",
            "commitment",
            "cooperation",
            "endeavor",
            "initiative",
            "intent",
            "undertaking",
        },
    },
    {
        "domain_id": "D09",
        "label": "substitution / replacement / loss",
        "terms": {
            "alteration",
            "change_transition",
            "disappearance",
            "equivalence",
            "error",
            "hiddenness",
            "misguidance",
            "proxy",
            "replacement",
            "representation",
            "substitution",
        },
    },
    {
        "domain_id": "D10",
        "label": "animal / herd trace",
        "terms": {
            "animal",
            "ewe",
            "herd",
            "husbandry",
            "livestock",
            "sheep",
            "stray",
            "uterus",
        },
    },
]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")))
            handle.write("\n")


def root_from_support_key(key: str) -> str:
    return key.split(":", 1)[0]


def is_noise_facet(facet: str) -> bool:
    tail = facet.split(":", 1)[-1].lower()
    return any(term in tail for term in NOISE_FACET_TERMS)


def facet_matches_terms(facet: str, terms: set[str]) -> bool:
    text = facet.split(":", 1)[-1].lower()
    return any(term in text for term in terms)


def useful_facets(row: dict[str, Any], *, min_support: int) -> list[dict[str, Any]]:
    out = []
    for item in row["scored_facets_top"]:
        facet = item["facet"]
        if facet in BROAD_OR_PRIMARY_FACETS or is_noise_facet(facet):
            continue
        if int(item["support_count"]) < min_support:
            continue
        out.append(item)
    return out


def jaccard(left: set[str], right: set[str]) -> float:
    if not left and not right:
        return 1.0
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def build_facet_components(
    rows: list[dict[str, Any]],
    *,
    min_support: int,
    min_groups_per_facet: int,
    min_cooccurrence: int,
) -> list[set[str]]:
    facet_to_groups: dict[str, set[str]] = collections.defaultdict(set)
    group_facets: dict[str, set[str]] = {}

    for row in rows:
        facets = {item["facet"] for item in useful_facets(row, min_support=min_support)}
        group_facets[row["review_id"]] = facets
        for facet in facets:
            facet_to_groups[facet].add(row["review_id"])

    anchors = {
        facet
        for facet, groups in facet_to_groups.items()
        if len(groups) >= min_groups_per_facet
    }

    adjacency: dict[str, set[str]] = {facet: set() for facet in anchors}
    cooccur: collections.Counter[tuple[str, str]] = collections.Counter()
    for facets in group_facets.values():
        kept = sorted(facets & anchors)
        for i, left in enumerate(kept):
            for right in kept[i + 1 :]:
                cooccur[(left, right)] += 1

    for (left, right), count in cooccur.items():
        if count >= min_cooccurrence or jaccard(facet_to_groups[left], facet_to_groups[right]) >= 0.18:
            adjacency[left].add(right)
            adjacency[right].add(left)

    seen: set[str] = set()
    components: list[set[str]] = []
    for facet in sorted(anchors):
        if facet in seen:
            continue
        stack = [facet]
        comp: set[str] = set()
        seen.add(facet)
        while stack:
            cur = stack.pop()
            comp.add(cur)
            for nxt in sorted(adjacency[cur]):
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        components.append(comp)

    components.sort(key=lambda comp: (-sum(len(facet_to_groups[f]) for f in comp), sorted(comp)))
    return components


def facet_support_after_dropping_root(item: dict[str, Any], dropped_root: str) -> int:
    return sum(1 for key in item["support"] if root_from_support_key(key) != dropped_root)


def group_survives_facets(
    row: dict[str, Any],
    anchors: set[str],
    *,
    min_support: int,
    dropped_facet: str | None = None,
    dropped_root: str | None = None,
) -> bool:
    for item in useful_facets(row, min_support=min_support):
        facet = item["facet"]
        if facet not in anchors or facet == dropped_facet:
            continue
        if dropped_root is not None:
            if facet_support_after_dropping_root(item, dropped_root) >= min_support:
                return True
        else:
            return True
    return False


def label_from_facets(facets: set[str]) -> str:
    text = " ".join(sorted(facets))
    label_rules = [
        (("guidance", "direction", "navigation", "straightness", "road"), "guidance / road / deviation"),
        (("blessing", "bounty", "grace", "hospitality_welfare", "benefit"), "mercy / blessing / provision"),
        (("authority", "kingship", "dominion", "hierarchy", "obligation_contract"), "authority / obedience / standing"),
        (("anger", "wrath", "jealousy", "honor", "fear_grief"), "anger / honor / rejection"),
        (("substitution", "replacement", "proxy", "change_transition"), "substitution / replacement / hiddenness"),
        (("name", "language", "invocation", "oath", "semiotics"), "name / invocation / obligation"),
        (("sky", "daytime", "weather", "light", "astronomy"), "sky / day / verticality"),
        (("aid", "assistance", "agency", "commitment", "undertaking"), "aid / intention / undertaking"),
        (("family", "kinship", "marriage_genealogy", "womb"), "kinship / family"),
        (("knowledge", "landmark", "semiotics", "banner", "heraldry"), "sign / knowledge / marker"),
    ]
    for terms, label in label_rules:
        if any(term in text for term in terms):
            return label
    return " / ".join(f.split(":", 1)[-1] for f in sorted(facets)[:3])


def score_component(
    component_id: int,
    anchors: set[str],
    rows: list[dict[str, Any]],
    *,
    min_support: int,
    min_groups_for_channel: int,
) -> dict[str, Any] | None:
    member_rows = [
        row for row in rows if group_survives_facets(row, anchors, min_support=min_support)
    ]
    if len(member_rows) < min_groups_for_channel:
        return None

    ayahs: set[int] = set()
    roots: collections.Counter[str] = collections.Counter()
    candidate_count = 0
    path_count = 0
    anchor_hits: collections.Counter[str] = collections.Counter()
    support_roots: collections.Counter[str] = collections.Counter()
    noise_facets = 0
    total_facets = 0

    for row in member_rows:
        ayahs.update(int(a) for a in row["distinct_ayahs"])
        candidate_count += int(row["candidate_count"])
        path_count += int(row["path_count_total"])
        roots.update(row["representative_root_signature"])
        for item in row["scored_facets_top"]:
            total_facets += 1
            if item["facet"] in BROAD_OR_PRIMARY_FACETS or is_noise_facet(item["facet"]):
                noise_facets += 1
            if item["facet"] in anchors:
                anchor_hits[item["facet"]] += 1
                for key in item["support"]:
                    support_roots[root_from_support_key(key)] += 1

    roots_set = set(roots)
    anchor_group_survival = []
    if len(anchors) > 1:
        for facet in anchors:
            survivors = sum(
                1
                for row in member_rows
                if group_survives_facets(
                    row,
                    anchors,
                    min_support=min_support,
                    dropped_facet=facet,
                )
            )
            anchor_group_survival.append(survivors / len(member_rows))
    else:
        anchor_group_survival.append(1.0)

    root_group_survival = []
    for root in roots_set:
        survivors = sum(
            1
            for row in member_rows
            if group_survives_facets(
                row,
                anchors,
                min_support=min_support,
                dropped_root=root,
            )
        )
        root_group_survival.append(survivors / len(member_rows))

    ayah_score = len(ayahs) / 7.0
    root_score = min(1.0, len(roots_set) / 7.0)
    group_score = min(1.0, math.log1p(len(member_rows)) / math.log1p(35))
    coherence = sum(anchor_hits.values()) / max(1, len(member_rows) * max(1, len(anchors)))
    coherence = min(1.0, coherence * 2.5)
    root_ablation = min(root_group_survival) if root_group_survival else 0.0
    facet_ablation = min(anchor_group_survival) if anchor_group_survival else 0.0
    noise_ratio = noise_facets / max(1, total_facets)
    bloat_penalty = max(0.0, (len(member_rows) - 35) / 65)

    stability_score = (
        0.20 * group_score
        + 0.15 * ayah_score
        + 0.15 * root_score
        + 0.20 * coherence
        + 0.15 * root_ablation
        + 0.15 * facet_ablation
        - 0.20 * noise_ratio
        - 0.15 * bloat_penalty
    )
    stability_score = max(0.0, min(1.0, stability_score))

    representative_rows = sorted(
        member_rows,
        key=lambda row: (-int(row["candidate_count"]), -int(row["path_count_total"]), row["review_id"]),
    )[:5]

    status = "stable"
    warnings = []
    if root_ablation < 0.25:
        warnings.append("root_critical")
    if facet_ablation < 0.35:
        warnings.append("facet_critical")
    if noise_ratio > 0.35:
        warnings.append("high_noise")

    if stability_score >= 0.68 and noise_ratio <= 0.35 and len(member_rows) >= 5:
        status = "stable"
    elif stability_score >= 0.55 and noise_ratio <= 0.50:
        status = "mixed"
    else:
        status = "unstable"

    return {
        "channel_id": f"CH{component_id:03d}",
        "status": status,
        "label": label_from_facets(anchors),
        "stability_score": round(stability_score, 4),
        "group_count": len(member_rows),
        "candidate_count_total": candidate_count,
        "path_count_total": path_count,
        "ayahs": sorted(ayahs),
        "roots": sorted(roots_set),
        "anchor_facets": sorted(anchors),
        "top_anchor_hits": anchor_hits.most_common(12),
        "support_roots": support_roots.most_common(12),
        "noise_ratio": round(noise_ratio, 4),
        "root_ablation_min_survival": round(root_ablation, 4),
        "facet_ablation_min_survival": round(facet_ablation, 4),
        "coherence": round(coherence, 4),
        "warnings": warnings,
        "member_review_ids": [row["review_id"] for row in member_rows],
        "representative_examples": [
            {
                "review_id": row["review_id"],
                "candidate_count": row["candidate_count"],
                "path_count_total": row["path_count_total"],
                "facets": row["image_scored_facet_signature"],
                "roots": row["representative_root_signature"],
                "branches": [
                    f"{item['root']}:{item['branch_id']}:{item['branch_image_ar']}"
                    for item in row["representative_path"]
                ],
            }
            for row in representative_rows
        ],
    }


def build_domain_channels(
    rows: list[dict[str, Any]],
    *,
    min_support: int,
    min_groups_for_channel: int,
) -> list[dict[str, Any]]:
    channels = []
    for rule in DOMAIN_RULES:
        anchors: set[str] = set()
        for row in rows:
            for item in useful_facets(row, min_support=min_support):
                if facet_matches_terms(item["facet"], rule["terms"]):
                    anchors.add(item["facet"])
        if not anchors:
            continue

        record = score_component(
            int(rule["domain_id"][1:]),
            anchors,
            rows,
            min_support=min_support,
            min_groups_for_channel=min_groups_for_channel,
        )
        if record:
            record["channel_id"] = rule["domain_id"]
            record["label"] = rule["label"]
            record["selection_method"] = "strict_existing_facet_family"
            channels.append(record)

    channels.sort(
        key=lambda row: (
            {"stable": 0, "mixed": 1, "unstable": 2}[row["status"]],
            -row["stability_score"],
            -row["group_count"],
            row["channel_id"],
        )
    )
    return channels


def write_tsv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "channel_id",
                "status",
                "label",
                "stability_score",
                "group_count",
                "candidate_count_total",
                "path_count_total",
                "ayahs",
                "roots",
                "anchor_facets",
                "noise_ratio",
                "root_ablation_min_survival",
                "facet_ablation_min_survival",
                "representative_ids",
                "warnings",
            ]
        )
        for row in rows:
            writer.writerow(
                [
                    row["channel_id"],
                    row["status"],
                    row["label"],
                    row["stability_score"],
                    row["group_count"],
                    row["candidate_count_total"],
                    row["path_count_total"],
                    ",".join(map(str, row["ayahs"])),
                    " ".join(row["roots"]),
                    " | ".join(row["anchor_facets"]),
                    row["noise_ratio"],
                    row["root_ablation_min_survival"],
                    row["facet_ablation_min_survival"],
                    ",".join(row["member_review_ids"][:20]),
                    ",".join(row.get("warnings", [])),
                ]
            )


def build(args: argparse.Namespace) -> dict[str, Any]:
    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    rows = read_jsonl(input_path)
    components = build_facet_components(
        rows,
        min_support=args.min_support,
        min_groups_per_facet=args.min_groups_per_facet,
        min_cooccurrence=args.min_cooccurrence,
    )
    channels = []
    for index, anchors in enumerate(components, start=1):
        record = score_component(
            index,
            anchors,
            rows,
            min_support=args.min_support,
            min_groups_for_channel=args.min_groups_for_channel,
        )
        if record:
            channels.append(record)

    channels.sort(
        key=lambda row: (
            {"stable": 0, "mixed": 1, "unstable": 2}[row["status"]],
            -row["stability_score"],
            -row["group_count"],
            row["label"],
        )
    )
    for index, row in enumerate(channels, start=1):
        row["channel_id"] = f"CH{index:03d}"

    stable = [row for row in channels if row["status"] == "stable"]
    mixed = [row for row in channels if row["status"] == "mixed"]
    unstable = [row for row in channels if row["status"] == "unstable"]

    write_jsonl(output_dir / "channel_candidates.jsonl", channels)
    write_tsv(output_dir / "channel_candidates.tsv", channels)
    write_tsv(output_dir / "low_stability_or_noise.tsv", mixed + unstable)

    domain_channels = build_domain_channels(
        rows,
        min_support=args.min_support,
        min_groups_for_channel=args.min_groups_for_channel,
    )
    domain_stable = [row for row in domain_channels if row["status"] == "stable"]
    domain_mixed = [row for row in domain_channels if row["status"] == "mixed"]
    domain_unstable = [row for row in domain_channels if row["status"] == "unstable"]
    write_jsonl(output_dir / "domain_channel_candidates.jsonl", domain_channels)
    write_tsv(output_dir / "domain_channel_candidates.tsv", domain_channels)

    assigned_groups = set()
    for row in stable + mixed:
        assigned_groups.update(row["member_review_ids"])

    summary = {
        "version": "network_v2_channel_stability",
        "policy": "Compress v1 groups using existing facets only; require multi-branch support and test ablation stability.",
        "input": str(input_path),
        "parameters": {
            "min_support": args.min_support,
            "min_groups_per_facet": args.min_groups_per_facet,
            "min_cooccurrence": args.min_cooccurrence,
            "min_groups_for_channel": args.min_groups_for_channel,
        },
        "counts": {
            "input_groups": len(rows),
            "facet_components": len(components),
            "channels_total": len(channels),
            "stable_channels": len(stable),
            "mixed_channels": len(mixed),
            "unstable_channels": len(unstable),
            "groups_in_stable_or_mixed_channels": len(assigned_groups),
            "unassigned_or_reject_like_groups": len(rows) - len(assigned_groups),
            "domain_channels_total": len(domain_channels),
            "domain_stable_channels": len(domain_stable),
            "domain_mixed_channels": len(domain_mixed),
            "domain_unstable_channels": len(domain_unstable),
        },
        "top_channels": [
            {
                "channel_id": row["channel_id"],
                "status": row["status"],
                "label": row["label"],
                "stability_score": row["stability_score"],
                "group_count": row["group_count"],
                "anchor_facets": row["anchor_facets"][:8],
            }
            for row in channels[:12]
        ],
        "top_domain_channels": [
            {
                "channel_id": row["channel_id"],
                "status": row["status"],
                "label": row["label"],
                "stability_score": row["stability_score"],
                "group_count": row["group_count"],
                "anchor_facets": row["anchor_facets"][:8],
            }
            for row in domain_channels[:12]
        ],
    }
    (output_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        default="network/v1/output/image_facet_review_index.jsonl",
    )
    parser.add_argument("--output-dir", default="network/v2/output")
    parser.add_argument("--min-support", type=int, default=2)
    parser.add_argument("--min-groups-per-facet", type=int, default=3)
    parser.add_argument("--min-cooccurrence", type=int, default=2)
    parser.add_argument("--min-groups-for-channel", type=int, default=3)
    return parser.parse_args()


def main() -> None:
    print(json.dumps(build(parse_args()), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
