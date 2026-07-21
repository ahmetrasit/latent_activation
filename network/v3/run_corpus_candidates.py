#!/usr/bin/env python3
"""Build or resume Neo v3 candidate families for a sequential surah range."""

from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run_stage(name: str, command: list[str], log_path: Path, dry_run: bool) -> int:
    rendered = " ".join(command)
    print(f"  {name}: {rendered}", flush=True)
    if dry_run:
        return 0
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"\n[{timestamp}] {rendered}\n")
        log.flush()
        completed = subprocess.run(
            command,
            cwd=REPO_ROOT,
            stdout=log,
            stderr=subprocess.STDOUT,
            check=False,
        )
    return completed.returncode


def stage_specs(
    *,
    surah: int,
    min_ayahs: int,
    output_dir: Path,
    quran_slm: Path,
    quran_roots: Path,
    network_artifact_dir: str,
    surah_resource_dir: str,
) -> list[tuple[str, Path, Path, list[str]]]:
    tag = f"s{surah:03d}"
    surah_dir = output_dir / tag
    common = [
        "--surah", str(surah),
        "--min-ayahs", str(min_ayahs),
        "--quran-slm", str(quran_slm),
        "--quran-roots", str(quran_roots),
        "--network-artifact-dir", network_artifact_dir,
        "--surah-resource-dir", surah_resource_dir,
    ]
    python = sys.executable
    return [
        (
            "dense discovery",
            surah_dir / "summary.json",
            surah_dir / "dense.log",
            [python, "network/v3/discover_surah_channels.py", *common,
             "--candidate-limit", "0", "--output-dir", str(output_dir)],
        ),
        (
            "dense consolidation",
            surah_dir / "families" / "consolidation_summary.json",
            surah_dir / "dense_consolidate.log",
            [python, "network/v3/consolidate_channel_families.py",
             "--input-dir", str(surah_dir)],
        ),
        (
            "sparse assembly",
            surah_dir / "paths" / "path_summary.json",
            surah_dir / "sparse.log",
            [python, "network/v3/assemble_semantic_paths.py", *common,
             "--path-limit", "0", "--family-input-dir", str(output_dir),
             "--output-dir", str(output_dir)],
        ),
        (
            "sparse consolidation",
            surah_dir / "paths" / "path_families" / "path_family_summary.json",
            surah_dir / "sparse_consolidate.log",
            [python, "network/v3/consolidate_semantic_paths.py",
             "--input-dir", str(surah_dir / "paths")],
        ),
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-surah", type=int, default=1)
    parser.add_argument("--end-surah", type=int, default=114)
    parser.add_argument("--min-ayahs", type=int, default=5)
    parser.add_argument("--output-dir", default="network/v3/experiments/corpus_neo_min5")
    parser.add_argument("--quran-slm", default="../quran-slm")
    parser.add_argument("--quran-roots", default="../quran-roots")
    parser.add_argument("--network-artifact-dir", default="artifacts/surah_networks_global_ensemble")
    parser.add_argument("--surah-resource-dir", default="artifacts/corpus_network/surah_resources")
    parser.add_argument("--retry-failures", action="store_true")
    parser.add_argument("--stop-on-error", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not 1 <= args.start_surah <= args.end_surah <= 114:
        raise SystemExit("surah range must satisfy 1 <= start <= end <= 114")

    output_dir = (REPO_ROOT / args.output_dir).resolve()
    quran_slm = (REPO_ROOT / args.quran_slm).resolve()
    quran_roots = (REPO_ROOT / args.quran_roots).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    lock_path = output_dir / ".corpus_candidates.lock"
    state_path = output_dir / "corpus_run_state.json"

    with lock_path.open("a+", encoding="utf-8") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print(f"another corpus runner holds {lock_path}", file=sys.stderr)
            return 2

        completed_surahs: list[int] = []
        failures: list[dict[str, Any]] = []
        for surah in range(args.start_surah, args.end_surah + 1):
            tag = f"s{surah:03d}"
            catalog_path = quran_slm / args.network_artifact_dir / tag / "catalog.json"
            if not catalog_path.exists():
                failure = {"surah": surah, "stage": "catalog", "reason": f"missing {catalog_path}"}
                failures.append(failure)
                print(f"{tag} FAIL catalog missing", flush=True)
                if args.stop_on_error:
                    break
                continue

            ayah_max = int(read_json(catalog_path)["ayah_max"])
            effective_min = min(args.min_ayahs, ayah_max)
            surah_dir = output_dir / tag
            surah_dir.mkdir(parents=True, exist_ok=True)
            failure_marker = surah_dir / "stage_failure.json"
            print(f"{tag} START ayahs={ayah_max} min_ayahs={effective_min}", flush=True)

            if failure_marker.exists() and not args.retry_failures:
                known_failure = read_json(failure_marker)
                failures.append({"surah": surah, "stage": "known failure", "detail": known_failure})
                print(f"{tag} SKIP known_failure={failure_marker}", flush=True)
                continue

            failed = False
            for name, marker, log_path, command in stage_specs(
                surah=surah,
                min_ayahs=effective_min,
                output_dir=output_dir,
                quran_slm=quran_slm,
                quran_roots=quran_roots,
                network_artifact_dir=args.network_artifact_dir,
                surah_resource_dir=args.surah_resource_dir,
            ):
                if marker.exists():
                    print(f"  {name}: SKIP checkpoint={marker}", flush=True)
                    continue
                returncode = run_stage(name, command, log_path, args.dry_run)
                if returncode:
                    failure = {
                        "surah": surah,
                        "stage": name,
                        "returncode": returncode,
                        "recorded_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                    }
                    failures.append(failure)
                    if not args.dry_run:
                        write_json(failure_marker, failure)
                    print(f"{tag} FAIL stage={name!r} rc={returncode}", flush=True)
                    failed = True
                    break

            if not failed and not args.dry_run:
                failure_marker.unlink(missing_ok=True)
                completed_surahs.append(surah)
                print(f"{tag} DONE", flush=True)
            if not args.dry_run:
                write_json(state_path, {
                    "updated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                    "range": [args.start_surah, args.end_surah],
                    "completed_this_run": completed_surahs,
                    "failures_this_run": failures,
                    "policy": {
                        "one_surah_at_a_time": True,
                        "candidate_limit": 0,
                        "path_limit": 0,
                        "requested_min_ayahs": args.min_ayahs,
                        "short_surah_rule": "min(requested_min_ayahs, ayah_max)",
                        "network_artifact_dir": args.network_artifact_dir,
                    },
                })
            if failed and args.stop_on_error:
                break

        if args.dry_run:
            return 0
        print(f"COMPLETE completed={len(completed_surahs)} failures={len(failures)}", flush=True)
        return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
