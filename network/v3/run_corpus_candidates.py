#!/usr/bin/env python3
"""Build or resume Neo v3 candidate families for a sequential surah range."""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import fcntl
import json
import math
import subprocess
import sys
import threading
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
PRINT_LOCK = threading.Lock()


def status_print(message: str, *, file: Any = None) -> None:
    """Keep concurrent worker status messages on separate lines."""
    with PRINT_LOCK:
        print(message, file=file, flush=True)


def adaptive_min_ayahs(canonical_ayah_count: int) -> int:
    """Clamp ten percent of canonical surah length to the inclusive range 4..10."""
    if canonical_ayah_count < 1:
        raise ValueError("canonical ayah count must be positive")
    return max(min(math.ceil(0.10 * canonical_ayah_count), 10), 4)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp")
    tmp_path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    tmp_path.replace(path)


def valid_json_marker(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        read_json(path)
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return False
    return True


def runner_failure_detail(surah: int, error: BaseException) -> dict[str, Any]:
    return {
        "surah": surah,
        "stage": "runner",
        "reason": f"{type(error).__name__}: {error}",
        "recorded_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    }


def persist_runner_failure(
    output_dir: Path,
    surah: int,
    detail: dict[str, Any],
    *,
    dry_run: bool,
) -> None:
    status_print(f"s{surah:03d} FAIL stage='runner' reason={detail['reason']}")
    if not dry_run:
        write_json(output_dir / f"s{surah:03d}" / "stage_failure.json", detail)


def run_stage(name: str, command: list[str], log_path: Path, dry_run: bool) -> int:
    rendered = " ".join(command)
    status_print(f"  {name}: {rendered}")
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
    parser.add_argument("--output-dir", default="network/v3/experiments/corpus_neo_adaptive")
    parser.add_argument("--quran-slm", default="../quran-slm")
    parser.add_argument("--quran-roots", default="../quran-roots")
    parser.add_argument("--network-artifact-dir", default="artifacts/surah_networks_global_ensemble")
    parser.add_argument("--surah-resource-dir", default="artifacts/corpus_network/surah_resources")
    parser.add_argument("--retry-failures", action="store_true")
    parser.add_argument("--stop-on-error", action="store_true")
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="number of surahs to process concurrently (each surah's stages remain sequential)",
    )
    parser.add_argument(
        "--skip-three-ayah-surahs",
        action="store_true",
        help="skip surahs whose canonical catalog contains exactly three ayahs",
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def process_surah(
    *,
    surah: int,
    output_dir: Path,
    quran_slm: Path,
    quran_roots: Path,
    network_artifact_dir: str,
    surah_resource_dir: str,
    retry_failures: bool,
    skip_three_ayah_surahs: bool,
    dry_run: bool,
) -> tuple[str, dict[str, Any] | None]:
    tag = f"s{surah:03d}"
    surah_dir = output_dir / tag
    failure_marker = surah_dir / "stage_failure.json"
    catalog_path = quran_slm / network_artifact_dir / tag / "catalog.json"
    if not catalog_path.exists():
        failure = {"surah": surah, "stage": "catalog", "reason": f"missing {catalog_path}"}
        if not dry_run:
            write_json(failure_marker, failure)
        status_print(f"{tag} FAIL catalog missing")
        return "failed", failure

    ayah_max = int(read_json(catalog_path)["ayah_max"])
    if skip_three_ayah_surahs and ayah_max == 3:
        status_print(f"{tag} SKIP canonical_ayahs=3")
        return "skipped", {"surah": surah, "reason": "canonical_ayahs=3"}

    effective_min = adaptive_min_ayahs(ayah_max)
    surah_dir.mkdir(parents=True, exist_ok=True)
    status_print(f"{tag} START ayahs={ayah_max} min_ayahs={effective_min}")

    specs = stage_specs(
        surah=surah,
        min_ayahs=effective_min,
        output_dir=output_dir,
        quran_slm=quran_slm,
        quran_roots=quran_roots,
        network_artifact_dir=network_artifact_dir,
        surah_resource_dir=surah_resource_dir,
    )

    if all(valid_json_marker(marker) for _name, marker, _log_path, _command in specs):
        if not dry_run:
            failure_marker.unlink(missing_ok=True)
        status_print(f"{tag} DONE checkpoints complete")
        return "completed", None

    if failure_marker.exists() and not retry_failures:
        known_failure = read_json(failure_marker)
        failure = {"surah": surah, "stage": "known failure", "detail": known_failure}
        status_print(f"{tag} SKIP known_failure={failure_marker}")
        return "failed", failure

    for name, marker, log_path, command in specs:
        if valid_json_marker(marker):
            status_print(f"  {tag} {name}: SKIP checkpoint={marker}")
            continue
        returncode = run_stage(f"{tag} {name}", command, log_path, dry_run)
        if returncode:
            failure = {
                "surah": surah,
                "stage": name,
                "returncode": returncode,
                "recorded_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            }
            if not dry_run:
                write_json(failure_marker, failure)
            status_print(f"{tag} FAIL stage={name!r} rc={returncode}")
            return "failed", failure

    if not dry_run:
        failure_marker.unlink(missing_ok=True)
    status_print(f"{tag} DONE")
    return "completed", None


def main() -> int:
    args = parse_args()
    if not 1 <= args.start_surah <= args.end_surah <= 114:
        raise SystemExit("surah range must satisfy 1 <= start <= end <= 114")
    if args.workers < 1:
        raise SystemExit("workers must be at least 1")
    if args.workers > 1 and args.stop_on_error:
        raise SystemExit("--stop-on-error is only supported with --workers 1")

    output_dir = (REPO_ROOT / args.output_dir).resolve()
    allowed_output_root = (
        REPO_ROOT / "network/v3/experiments/corpus_neo_adaptive"
    ).resolve()
    if output_dir != allowed_output_root:
        raise SystemExit(f"--output-dir must be {allowed_output_root}")
    quran_slm = (REPO_ROOT / args.quran_slm).resolve()
    quran_roots = (REPO_ROOT / args.quran_roots).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    lock_path = output_dir / ".corpus_candidates.lock"
    state_path = output_dir / "corpus_run_state.json"

    with lock_path.open("a+", encoding="utf-8") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            status_print(f"another corpus runner holds {lock_path}", file=sys.stderr)
            return 2

        completed_surahs: list[int] = []
        failures: list[dict[str, Any]] = []
        skipped_surahs: list[dict[str, Any]] = []

        def record_result(status: str, detail: dict[str, Any] | None, surah: int) -> bool:
            if status == "completed":
                if not args.dry_run:
                    completed_surahs.append(surah)
            elif status == "skipped":
                assert detail is not None
                skipped_surahs.append(detail)
            else:
                assert detail is not None
                failures.append(detail)

            completed_surahs.sort()
            skipped_surahs.sort(key=lambda row: int(row["surah"]))
            failures.sort(key=lambda row: int(row["surah"]))
            if not args.dry_run:
                write_json(state_path, {
                    "updated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                    "range": [args.start_surah, args.end_surah],
                    "completed_this_run": completed_surahs,
                    "skipped_this_run": skipped_surahs,
                    "failures_this_run": failures,
                    "policy": {
                        "workers": args.workers,
                        "one_surah_at_a_time_per_worker": True,
                        "skip_three_ayah_surahs": args.skip_three_ayah_surahs,
                        "candidate_limit": 0,
                        "path_limit": 0,
                        "min_ayahs_formula": (
                            "max(min(ceil(0.10 * canonical_ayah_count), 10), 4)"
                        ),
                        "network_artifact_dir": args.network_artifact_dir,
                    },
                })
            return status == "failed"

        process_kwargs = {
            "output_dir": output_dir,
            "quran_slm": quran_slm,
            "quran_roots": quran_roots,
            "network_artifact_dir": args.network_artifact_dir,
            "surah_resource_dir": args.surah_resource_dir,
            "retry_failures": args.retry_failures,
            "skip_three_ayah_surahs": args.skip_three_ayah_surahs,
            "dry_run": args.dry_run,
        }
        surahs = range(args.start_surah, args.end_surah + 1)
        if args.workers == 1:
            for surah in surahs:
                try:
                    status, detail = process_surah(surah=surah, **process_kwargs)
                except Exception as error:
                    detail = runner_failure_detail(surah, error)
                    persist_runner_failure(
                        output_dir,
                        surah,
                        detail,
                        dry_run=args.dry_run,
                    )
                    status = "failed"
                failed = record_result(status, detail, surah)
                if failed and args.stop_on_error:
                    break
        else:
            with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
                futures = {
                    executor.submit(process_surah, surah=surah, **process_kwargs): surah
                    for surah in surahs
                }
                for future in concurrent.futures.as_completed(futures):
                    surah = futures[future]
                    try:
                        status, detail = future.result()
                    except Exception as error:
                        detail = runner_failure_detail(surah, error)
                        status = "failed"
                        persist_runner_failure(
                            output_dir,
                            surah,
                            detail,
                            dry_run=args.dry_run,
                        )
                    record_result(status, detail, surah)

        if args.dry_run:
            return 0
        status_print(
            f"COMPLETE completed={len(completed_surahs)} "
            f"skipped={len(skipped_surahs)} failures={len(failures)}"
        )
        return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
