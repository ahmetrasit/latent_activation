#!/usr/bin/env python3
"""Derive the scoped 83:1 root-map repair from quran-data's accepted QAC/MASAQ edges."""

import gzip
import hashlib
import json
import sqlite3
from pathlib import Path

import build_focus_trace_packet as builder

QURAN_DATA = builder.PROJECTS_ROOT / "quran-data"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def checked_database(base: Path, relative: str) -> sqlite3.Connection:
    expected = {}
    for line in (base / "CHECKSUMS.sha256").read_text().splitlines():
        checksum, name = line.split(maxsplit=1)
        expected[name.lstrip("*").removeprefix("./")] = checksum
    payload = (base / relative).read_bytes()
    if expected.get(relative) != digest(payload):
        raise ValueError(f"release checksum mismatch: {relative}")
    connection = sqlite3.connect(":memory:")
    connection.deserialize(gzip.decompress(payload))
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA query_only = ON")
    return connection


def accepted_target(bridge: sqlite3.Connection, lexical: sqlite3.Connection, qac_ref: str, root: str) -> tuple[dict, list[dict]]:
    rows = [dict(row) for row in bridge.execute(
        """SELECT e.masaq_segment_ref, e.qac_morpheme_ref, e.target_order,
                  m.root_ar, m.stem_ar, m.tag, m.role,
                  q.surface_ar, q.morpheme_role
           FROM accepted_masaq_qac_edges e
           JOIN masaq_segments m USING (masaq_segment_ref)
           JOIN qac_morphemes q USING (qac_morpheme_ref)
           WHERE e.qac_morpheme_ref = ?""", (qac_ref,),
    )]
    if not rows or any(row["morpheme_role"] != "STEM" or row["root_ar"] != root for row in rows):
        raise ValueError("missing or conflicting accepted STEM alignment")
    targets = [dict(row) for row in lexical.execute(
        "SELECT root_id, root_norm, source_root_norm FROM roots WHERE source_root_norm = ?", (root,),
    )]
    if len(targets) != 1:
        raise ValueError("aligned root has no unique lexical source-root identity")
    return targets[0], rows


def build_repair() -> dict:
    root, qac_ref = "ط ف ف", "83:1:2:3"
    bridge_path = "data/bridges/qac-masaq.sqlite.gz"
    qac_path = "data/morphology/qac.sqlite.gz"
    with checked_database(QURAN_DATA, bridge_path) as bridge, checked_database(QURAN_DATA, qac_path) as qac:
        meta = dict(bridge.execute("SELECT key, value FROM metadata").fetchall())
        release_bytes = (QURAN_DATA / "RELEASE.json").read_bytes()
        audit_bytes = (QURAN_DATA / "data/bridges/qac-masaq-audit.json").read_bytes()
        if (bridge.execute("PRAGMA user_version").fetchone()[0] != 4
            or meta["schema_version"] != "qac-masaq-bridge-v1"
            or meta["quran_data_release_manifest_sha256"] != digest(release_bytes)
            or meta["quran_data_release_id"] != json.loads(release_bytes)["release_id"]
            or meta["audit_sha256"] != digest(audit_bytes)
            or meta["qac_sha256"] != digest((QURAN_DATA / qac_path).read_bytes())
            or json.loads(audit_bytes)["status"] != "accepted"):
            raise ValueError("bridge schema/release/audit metadata mismatch")
        qac_rows = [dict(row) for row in qac.execute(
            "SELECT qac_ref, surface_ar, lemma_ar, root_ar FROM qac_morphemes WHERE root_ar = ?", (root,),
        )]
        if len(qac_rows) != 1 or qac_rows[0]["qac_ref"] != qac_ref:
            raise ValueError("83:1 repair scope no longer matches the QAC corpus")
        lexical = sqlite3.connect(":memory:")
        lexical.deserialize(gzip.decompress(builder.DEFAULT_BRANCH_DB.read_bytes()))
        lexical.row_factory = sqlite3.Row
        try:
            target, edges = accepted_target(bridge, lexical, qac_ref, root)
        finally:
            lexical.close()
    if any(edge["surface_ar"] != qac_rows[0]["surface_ar"] for edge in edges):
        raise ValueError("bridge and released QAC surfaces disagree")
    occurrence = next(row for row in builder.load_window_ayat(
        builder.DEFAULT_QAC, builder.DEFAULT_QURAN_DIR, ["83:1"],
    )["83:1"]["root_occurrences"] if row["root"] == root)
    if (occurrence["word_indices"] != [qac_ref.split(":")[2]]
        or occurrence["surfaces_ar"] != [qac_rows[0]["surface_ar"]]
        or occurrence["lemmas_ar"] != [qac_rows[0]["lemma_ar"]]):
        raise ValueError("local v1 QAC projection differs from released QAC")
    return {
        "protocol": "hft-accepted-alignment-root-repairs-v1",
        "repairs": [{
            "id": "83-1-accepted-masaq-alignment-20260906", "qac_root": root,
            "expected_mapping": {
                "mapping_status": "no_frozen_rooted_surface_match", "qac_total_occurrences": 1,
                "matched_occurrences": 0, "unmapped_reason": "no_frozen_rooted_surface_match",
            },
            "packet_occurrence": {"ref": "83:1", **{key: occurrence[key] for key in ("word_indices", "surfaces_ar", "lemmas_ar")}},
            "target": {
                "target_rank": 1, "frozen_root_norm": root,
                "furuq_root_id": target["root_id"], "furuq_root_norm": target["root_norm"],
                "furuq_source_root_norm": target["source_root_norm"],
                "furuq_resolution": "accepted_masaq_qac_edges_then_exact_source_root_norm",
                "target_occurrences": 1, "is_dominant": True,
            },
            "evidence": {
                "accepted_edges": edges, "bridge_schema_version": meta["schema_version"],
                "release_id": meta["quran_data_release_id"],
                "source_sha256": {str(path): digest(path.read_bytes()) for path in (
                    QURAN_DATA / bridge_path, QURAN_DATA / qac_path,
                    QURAN_DATA / "RELEASE.json", QURAN_DATA / "data/bridges/qac-masaq-audit.json",
                    builder.DEFAULT_BRANCH_DB, builder.DEFAULT_QAC_FURUQ_ROOT_MAP,
                )},
            },
        }],
    }


if __name__ == "__main__":
    result = build_repair()
    builder.ROOT_MAPPING_REPAIRS.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Derived {builder.ROOT_MAPPING_REPAIRS} from accepted quran-data alignment")
