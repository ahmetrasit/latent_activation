#!/usr/bin/env python3
"""Build the QAC root to furuq_v4 root gateway SQLite DB."""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path


def find_repo_root() -> Path:
    start = Path(__file__).resolve()
    for candidate in (start.parent, *start.parents):
        if (candidate / ".git").exists():
            return candidate
    return Path.cwd()


ROOT = find_repo_root()
QURAN_DATA_INPUT = ROOT / "data" / "bridges" / "qac-furuq-v4-root-map.tsv"
LATENT_INPUT = ROOT / "_status" / "v12_cross_run" / "audits" / "frozen-qac-root-authoritative-map.tsv"
DEFAULT_INPUT = QURAN_DATA_INPUT if QURAN_DATA_INPUT.exists() else LATENT_INPUT
DEFAULT_OUTPUT = (
    ROOT / "data" / "bridges" / "qac-furuq-v4-root-map.sqlite"
    if QURAN_DATA_INPUT.exists()
    else ROOT / "_status" / "v12_cross_run" / "audits" / "qac-furuq-v4-root-map.sqlite"
)
DEFAULT_FURUQ_DB = ROOT / "resources" / "furuq_v4.sqlite"
DEFAULT_AUDIT_SUMMARY = ROOT / "_status" / "v12_cross_run" / "audits" / "frozen-qac-root-bridge-summary.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def join_key(root_norm: str) -> str:
    return (root_norm or "").replace(" ", "")


def parse_target(raw: str) -> tuple[str, str, str, str, str, int]:
    target, _, count_text = raw.rpartition(":")
    parts = target.split("=>")
    if len(parts) != 5:
        raise ValueError(f"bad target encoding: {raw}")
    frozen_root, root_id, furuq_root, source_root, resolution = parts
    return frozen_root, root_id, furuq_root, source_root, resolution, int(count_text)


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(
            "input TSV not found; pass --input explicitly. Checked defaults: "
            f"{QURAN_DATA_INPUT} and {LATENT_INPUT}"
        )
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def create_schema(conn: sqlite3.Connection) -> None:
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(
        """
        DROP VIEW IF EXISTS furuq_to_qac;
        DROP VIEW IF EXISTS qac_to_furuq_mapped;
        DROP VIEW IF EXISTS qac_to_furuq;
        DROP TABLE IF EXISTS metadata;
        DROP TABLE IF EXISTS qac_furuq_targets;
        DROP TABLE IF EXISTS qac_root_map;

        CREATE TABLE metadata (
          key TEXT PRIMARY KEY,
          value TEXT NOT NULL
        );

        CREATE TABLE qac_root_map (
          qac_root_norm TEXT PRIMARY KEY,
          qac_root_join_key TEXT NOT NULL,
          qac_total_occurrences INTEGER NOT NULL,
          matched_occurrences INTEGER NOT NULL,
          mapping_status TEXT NOT NULL,
          dominant_frozen_root_norm TEXT NOT NULL,
          dominant_frozen_root_join_key TEXT NOT NULL,
          dominant_furuq_root_id TEXT NOT NULL,
          dominant_furuq_root_norm TEXT NOT NULL,
          dominant_furuq_root_join_key TEXT NOT NULL,
          dominant_furuq_source_root_norm TEXT NOT NULL,
          dominant_resolution TEXT NOT NULL,
          dominant_occurrences INTEGER NOT NULL,
          targets_raw TEXT NOT NULL,
          status_counts TEXT NOT NULL,
          sample_refs TEXT NOT NULL,
          sample_surfaces TEXT NOT NULL
        );

        CREATE TABLE qac_furuq_targets (
          qac_root_norm TEXT NOT NULL,
          qac_root_join_key TEXT NOT NULL,
          target_rank INTEGER NOT NULL,
          frozen_root_norm TEXT NOT NULL,
          frozen_root_join_key TEXT NOT NULL,
          furuq_root_id TEXT NOT NULL,
          furuq_root_norm TEXT NOT NULL,
          furuq_root_join_key TEXT NOT NULL,
          furuq_source_root_norm TEXT NOT NULL,
          furuq_resolution TEXT NOT NULL,
          occurrences INTEGER NOT NULL,
          is_dominant INTEGER NOT NULL CHECK (is_dominant IN (0, 1)),
          PRIMARY KEY (qac_root_norm, target_rank),
          FOREIGN KEY (qac_root_norm) REFERENCES qac_root_map(qac_root_norm)
        );

        CREATE INDEX idx_qac_root_map_join_key ON qac_root_map(qac_root_join_key);
        CREATE INDEX idx_qac_root_map_dominant_id ON qac_root_map(dominant_furuq_root_id);
        CREATE INDEX idx_qac_furuq_targets_qac_join ON qac_furuq_targets(qac_root_join_key);
        CREATE INDEX idx_qac_furuq_targets_furuq_id ON qac_furuq_targets(furuq_root_id);
        CREATE INDEX idx_qac_furuq_targets_furuq_norm ON qac_furuq_targets(furuq_root_norm);
        CREATE INDEX idx_qac_furuq_targets_furuq_join ON qac_furuq_targets(furuq_root_join_key);
        CREATE INDEX idx_qac_furuq_targets_source_norm ON qac_furuq_targets(furuq_source_root_norm);

        CREATE VIEW qac_to_furuq AS
        SELECT
          m.qac_root_norm,
          m.qac_root_join_key,
          m.mapping_status,
          m.qac_total_occurrences,
          m.matched_occurrences,
          t.target_rank,
          t.frozen_root_norm,
          NULLIF(t.furuq_root_id, '') AS furuq_root_id,
          t.furuq_root_norm,
          t.furuq_source_root_norm,
          t.furuq_resolution,
          t.occurrences AS target_occurrences,
          COALESCE(t.is_dominant, 0) AS is_dominant,
          CASE WHEN t.furuq_root_id IS NOT NULL AND t.furuq_root_id != '' THEN 1 ELSE 0 END AS has_furuq_root,
          CASE
            WHEN t.qac_root_norm IS NULL THEN m.mapping_status
            WHEN t.furuq_root_id IS NULL OR t.furuq_root_id = '' THEN t.furuq_resolution
            ELSE ''
          END AS unmapped_reason
        FROM qac_root_map m
        LEFT JOIN qac_furuq_targets t USING(qac_root_norm);

        CREATE VIEW qac_to_furuq_mapped AS
        SELECT *
        FROM qac_to_furuq
        WHERE has_furuq_root = 1;

        CREATE VIEW furuq_to_qac AS
        SELECT
          furuq_root_id,
          furuq_root_norm,
          furuq_source_root_norm,
          frozen_root_norm,
          qac_root_norm,
          qac_root_join_key,
          mapping_status,
          qac_total_occurrences,
          matched_occurrences,
          target_rank,
          furuq_resolution,
          target_occurrences,
          is_dominant
        FROM qac_to_furuq_mapped;
        """
    )


def validate_targets(
    rows: list[dict[str, str]],
    target_rows: list[tuple[object, ...]],
    furuq_db: Path | None,
) -> dict[str, str]:
    issues: list[str] = []
    target_counts: dict[str, int] = {}
    for target in target_rows:
        qac_root = str(target[0])
        root_id = str(target[5])
        resolution = str(target[9])
        count = int(target[10])
        target_counts[qac_root] = target_counts.get(qac_root, 0) + count
        if not root_id and resolution != "missing_furuq_root":
            issues.append(f"{qac_root}: blank furuq_root_id with resolution={resolution}")

    for row in rows:
        target_sum = target_counts.get(row["qac_root_norm"], 0)
        matched = int(row["matched_occurrences"] or "0")
        if target_sum != matched:
            issues.append(
                f"{row['qac_root_norm']}: target occurrence sum {target_sum} != matched_occurrences {matched}"
            )
        if row["targets"]:
            first_target = row["targets"].split("|", 1)[0]
            frozen_root, root_id, furuq_root, source_root, resolution, count = parse_target(first_target)
            expected = (
                row["dominant_frozen_root_norm"],
                row["dominant_furuq_root_id"],
                row["dominant_furuq_root_norm"],
                row["dominant_furuq_source_root_norm"],
                row["dominant_resolution"],
                int(row["dominant_occurrences"] or "0"),
            )
            actual = (frozen_root, root_id, furuq_root, source_root, resolution, count)
            if actual != expected:
                issues.append(f"{row['qac_root_norm']}: first target does not match dominant fields")

    metadata: dict[str, str] = {}
    if furuq_db and furuq_db.exists():
        with sqlite3.connect(furuq_db) as furuq_conn:
            furuq_conn.row_factory = sqlite3.Row
            root_rows = {
                row["root_id"]: row
                for row in furuq_conn.execute(
                    "SELECT root_id, root_norm, source_root_norm FROM roots"
                )
            }
            for target in target_rows:
                root_id = str(target[5])
                if not root_id:
                    continue
                furuq_root = str(target[6])
                source_root = str(target[8])
                root = root_rows.get(root_id)
                if root is None:
                    issues.append(f"{target[0]}: furuq_root_id does not exist: {root_id}")
                elif root["root_norm"] != furuq_root or root["source_root_norm"] != source_root:
                    issues.append(
                        f"{target[0]}: furuq root mismatch for {root_id}: "
                        f"target=({furuq_root}, {source_root}) db=({root['root_norm']}, {root['source_root_norm']})"
                    )
            metadata["furuq_db_path"] = str(furuq_db)
            metadata["furuq_db_sha256"] = sha256_file(furuq_db)
            metadata["furuq_roots_count"] = str(len(root_rows))
    elif furuq_db:
        metadata["furuq_db_path"] = str(furuq_db)
        metadata["furuq_db_sha256"] = ""
        metadata["furuq_roots_count"] = ""

    if issues:
        raise SystemExit("target validation failed:\n- " + "\n- ".join(issues[:50]))
    return metadata


def build_timestamp(explicit: str | None) -> str:
    if explicit:
        return explicit
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch:
        return datetime.fromtimestamp(int(epoch), tz=timezone.utc).isoformat()
    return datetime.now(timezone.utc).isoformat()


def insert_rows(
    conn: sqlite3.Connection,
    rows: list[dict[str, str]],
    source_path: Path,
    furuq_db: Path | None,
    audit_summary: Path | None,
    built_at: str,
) -> None:
    conn.executemany(
        """
        INSERT INTO qac_root_map (
          qac_root_norm, qac_root_join_key, qac_total_occurrences,
          matched_occurrences, mapping_status, dominant_frozen_root_norm,
          dominant_frozen_root_join_key, dominant_furuq_root_id,
          dominant_furuq_root_norm, dominant_furuq_root_join_key,
          dominant_furuq_source_root_norm, dominant_resolution,
          dominant_occurrences, targets_raw, status_counts, sample_refs,
          sample_surfaces
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                row["qac_root_norm"],
                join_key(row["qac_root_norm"]),
                int(row["qac_total_occurrences"] or "0"),
                int(row["matched_occurrences"] or "0"),
                row["mapping_status"],
                row["dominant_frozen_root_norm"],
                join_key(row["dominant_frozen_root_norm"]),
                row["dominant_furuq_root_id"],
                row["dominant_furuq_root_norm"],
                join_key(row["dominant_furuq_root_norm"]),
                row["dominant_furuq_source_root_norm"],
                row["dominant_resolution"],
                int(row["dominant_occurrences"] or "0"),
                row["targets"],
                row["status_counts"],
                row["sample_refs"],
                row["sample_surfaces"],
            )
            for row in rows
        ],
    )

    target_rows: list[tuple[object, ...]] = []
    for row in rows:
        targets = [part for part in row["targets"].split("|") if part]
        for index, target in enumerate(targets, start=1):
            frozen_root, root_id, furuq_root, source_root, resolution, count = parse_target(target)
            target_rows.append(
                (
                    row["qac_root_norm"],
                    join_key(row["qac_root_norm"]),
                    index,
                    frozen_root,
                    join_key(frozen_root),
                    root_id,
                    furuq_root,
                    join_key(furuq_root),
                    source_root,
                    resolution,
                    count,
                    1 if index == 1 else 0,
                )
            )

    conn.executemany(
        """
        INSERT INTO qac_furuq_targets (
          qac_root_norm, qac_root_join_key, target_rank, frozen_root_norm,
          frozen_root_join_key, furuq_root_id, furuq_root_norm,
          furuq_root_join_key, furuq_source_root_norm, furuq_resolution,
          occurrences, is_dominant
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        target_rows,
    )

    validation_metadata = validate_targets(rows, target_rows, furuq_db)

    metadata = {
        "schema": "qac-furuq-v4-root-map.v1",
        "built_at": built_at,
        "source_tsv": str(source_path),
        "source_tsv_sha256": sha256_file(source_path),
        "qac_root_rows": str(len(rows)),
        "target_rows": str(len(target_rows)),
        "builder_script": str(Path(__file__).resolve()),
        "builder_script_sha256": sha256_file(Path(__file__).resolve()),
        "argv": " ".join(sys.argv),
    }
    metadata.update(validation_metadata)
    if audit_summary and audit_summary.exists():
        metadata["audit_summary"] = str(audit_summary)
        metadata["audit_summary_sha256"] = sha256_file(audit_summary)
    conn.executemany("INSERT INTO metadata(key, value) VALUES (?, ?)", metadata.items())
    fk_errors = conn.execute("PRAGMA foreign_key_check").fetchall()
    if fk_errors:
        raise SystemExit(f"foreign key check failed: {fk_errors[:10]}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--furuq-db", type=Path, default=DEFAULT_FURUQ_DB if DEFAULT_FURUQ_DB.exists() else None)
    parser.add_argument(
        "--audit-summary",
        type=Path,
        default=DEFAULT_AUDIT_SUMMARY if DEFAULT_AUDIT_SUMMARY.exists() else None,
    )
    parser.add_argument("--built-at", default=None)
    args = parser.parse_args()

    rows = read_rows(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(args.output) as conn:
        create_schema(conn)
        insert_rows(
            conn,
            rows,
            args.input,
            args.furuq_db,
            args.audit_summary,
            build_timestamp(args.built_at),
        )
        conn.commit()

    print(f"wrote {args.output}")
    print(f"qac_roots={len(rows)}")


if __name__ == "__main__":
    main()
