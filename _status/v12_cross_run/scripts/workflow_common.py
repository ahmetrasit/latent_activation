#!/usr/bin/env python3
"""Shared deterministic utilities for the agent-orchestrated workflow."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import subprocess
import tempfile
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


SCRIPT_ROOT = Path(__file__).resolve().parent
PACKAGE_ROOT = SCRIPT_ROOT.parent
REPO_ROOT = PACKAGE_ROOT.parents[1]
TEMPLATE_ROOT = PACKAGE_ROOT / "schema" / "templates"
PROMPT_ROOT = PACKAGE_ROOT / "prompts"
MODEL_SCHEMA_ROOT = PACKAGE_ROOT / "model_schemas"

TABLE_NAMES = (
    "runs.tsv",
    "source_findings.tsv",
    "claims.tsv",
    "claim_sources.tsv",
    "branch_evidence.tsv",
    "coverage.tsv",
    "stage_status.tsv",
)

AYAH_RE = re.compile(r"^[1-9][0-9]*:[0-9]+$")
AYAH_HEADING_RE = re.compile(r"^##\s+([1-9][0-9]*:[0-9]+)(?:\s+—.*)?$")
NUMBERED_READING_RE = re.compile(r"^\s*([0-9]+)\.\s+(.*)$")
BRANCH_KEY_RE = re.compile(r"^(.+):B([0-9]{3})$")


@dataclass(frozen=True)
class SourceBlock:
    block_id: str
    run_id: str
    fixed_ayah_ref: str
    finding_type: str
    source_pointer: str
    source_end_pointer: str
    raw_sha256: str
    text: str


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repo_relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_text(
        path, json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False) + "\n"
    )


def compact_json_text(value: Any) -> str:
    return json.dumps(
        value, ensure_ascii=False, separators=(",", ":"), sort_keys=False
    ) + "\n"


def atomic_write_compact_json(path: Path, value: Any) -> None:
    atomic_write_text(path, compact_json_text(value))


def require_compact_json(path: Path) -> Any:
    raw = path.read_text(encoding="utf-8")
    value = json.loads(raw)
    if raw != compact_json_text(value):
        raise ValueError(f"generated JSON is not canonical compact JSON: {path}")
    return value


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def template_header(filename: str) -> list[str]:
    with (TEMPLATE_ROOT / filename).open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle, delimiter="\t"))
    if len(rows) != 1:
        raise ValueError(f"template must have one row: {filename}")
    return rows[0]


def ensure_workspace_tables(workspace: Path) -> None:
    workspace.mkdir(parents=True, exist_ok=True)
    for filename in TABLE_NAMES:
        path = workspace / filename
        if not path.exists():
            header = "\t".join(template_header(filename)) + "\n"
            atomic_write_text(path, header)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return [dict(row) for row in reader]


def write_tsv(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    header = template_header(path.name)
    buffer: list[str] = ["\t".join(header)]
    for row in rows:
        values: list[str] = []
        for field in header:
            value = row.get(field, "")
            if value is None:
                value = ""
            rendered = str(value)
            if "\t" in rendered or "\n" in rendered or "\r" in rendered:
                raise ValueError(
                    f"{path.name}: field {field} contains a tab or newline: {rendered!r}"
                )
            values.append(rendered)
        buffer.append("\t".join(values))
    atomic_write_text(path, "\n".join(buffer) + "\n")


def split_scalar(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def join_scalar(values: Iterable[str]) -> str:
    seen: set[str] = set()
    ordered: list[str] = []
    for raw in values:
        value = str(raw).strip()
        if value and value not in seen:
            seen.add(value)
            ordered.append(value)
    return ";".join(ordered)


def normalize_branch_key(value: str) -> str:
    match = BRANCH_KEY_RE.fullmatch(value.strip())
    if match is None:
        raise ValueError(f"invalid branch key {value!r}; expected ROOT:B###")
    root = " ".join(match.group(1).split())
    return f"{root}:B{match.group(2)}"


def ayah_sort_key(ref: str) -> tuple[int, int]:
    surah, ayah = ref.split(":", 1)
    return int(surah), int(ayah)


def word_id_for(ref: str, word_index: int) -> str:
    surah, ayah = (int(value) for value in ref.split(":", 1))
    return f"w-s{surah:03d}-a{ayah:03d}-w{word_index:03d}"


def fingerprint_paths(paths: Iterable[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        raw_name = repo_relative(path).encode("utf-8")
        content = path.read_bytes()
        digest.update(len(raw_name).to_bytes(8, "big"))
        digest.update(raw_name)
        digest.update(len(content).to_bytes(8, "big"))
        digest.update(content)
    return digest.hexdigest()


def git_blob(revision: str, raw_path: str) -> bytes | None:
    result = subprocess.run(
        ["git", "show", f"{revision}:{raw_path}"],
        cwd=REPO_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.stdout if result.returncode == 0 else None


def find_revision_with_hash(raw_path: str, target_hash: str) -> str:
    history = subprocess.run(
        ["git", "log", "--format=%H", "--", raw_path],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if history.returncode:
        return ""
    for revision in history.stdout.splitlines():
        blob = git_blob(revision, raw_path)
        if blob is not None and sha256_bytes(blob) == target_hash:
            return revision
    return ""


def parse_reader_blocks(path: Path, run_id: str) -> list[SourceBlock]:
    lines = path.read_text(encoding="utf-8").splitlines()
    raw_path = repo_relative(path)
    current_ref = ""
    section = ""
    active_start = 0
    active_lines: list[str] = []
    retrospective_heading_line = 0
    retrospective_start = 0
    retrospective_lines: list[str] = []
    blocks: list[SourceBlock] = []
    ordinals: dict[tuple[str, str], int] = {}

    def add_block(
        finding_type: str, start: int, end: int, content_lines: list[str]
    ) -> None:
        if not current_ref:
            return
        text = "\n".join(content_lines).strip()
        if not text and finding_type == "retrospective_surprise":
            start = retrospective_heading_line or start
            end = start
            text = "[empty retrospective section]"
        if not text:
            return
        key = (current_ref, finding_type)
        ordinals[key] = ordinals.get(key, 0) + 1
        kind = "a" if finding_type == "activated_reading" else "r"
        ref_key = current_ref.replace(":", "_")
        block_id = f"blk-{run_id}-{ref_key}-{kind}{ordinals[key]:03d}"
        blocks.append(
            SourceBlock(
                block_id=block_id,
                run_id=run_id,
                fixed_ayah_ref=current_ref,
                finding_type=finding_type,
                source_pointer=f"{raw_path}:{start}",
                source_end_pointer=f"{raw_path}:{end}",
                raw_sha256=sha256_bytes(text.encode("utf-8")),
                text=text,
            )
        )

    def flush_active(end_line: int) -> None:
        nonlocal active_start, active_lines
        if active_lines:
            add_block("activated_reading", active_start, end_line, active_lines)
        active_start = 0
        active_lines = []

    def flush_retrospective(end_line: int) -> None:
        nonlocal retrospective_start, retrospective_lines
        start = retrospective_start or retrospective_heading_line
        add_block(
            "retrospective_surprise",
            start,
            max(start, end_line),
            retrospective_lines,
        )
        retrospective_start = 0
        retrospective_lines = []

    for line_number, line in enumerate(lines, start=1):
        ayah_match = AYAH_HEADING_RE.match(line)
        if ayah_match:
            if section == "activated":
                flush_active(line_number - 1)
            elif section == "retrospective":
                flush_retrospective(line_number - 1)
            current_ref = ayah_match.group(1)
            section = ""
            retrospective_heading_line = 0
            continue

        normalized = line.strip().lower()
        if normalized == "### activated readings":
            if section == "retrospective":
                flush_retrospective(line_number - 1)
            section = "activated"
            continue
        if normalized == "### retrospective surprises":
            if section == "activated":
                flush_active(line_number - 1)
            section = "retrospective"
            retrospective_heading_line = line_number
            retrospective_start = 0
            retrospective_lines = []
            continue

        if section == "activated":
            numbered = NUMBERED_READING_RE.match(line)
            if numbered:
                flush_active(line_number - 1)
                active_start = line_number
                active_lines = [line]
            elif active_lines:
                active_lines.append(line)
        elif section == "retrospective":
            if line.strip() and not retrospective_start:
                retrospective_start = line_number
            retrospective_lines.append(line)

    if section == "activated":
        flush_active(len(lines))
    elif section == "retrospective":
        flush_retrospective(len(lines))
    return blocks


def _run_row(
    *,
    run_id: str,
    treatment: str,
    prompt_path: Path,
    packet_path: Path,
    output_path: Path,
    manifest_path: Path | None,
    visible_refs: list[str],
    provenance_status: str,
    notes: str,
) -> dict[str, str]:
    prompt_raw = repo_relative(prompt_path)
    packet_raw = repo_relative(packet_path)
    output_raw = repo_relative(output_path)
    prompt_hash = sha256_file(prompt_path)
    output_hash = sha256_file(output_path)
    manifest_raw = repo_relative(manifest_path) if manifest_path else ""
    return {
        "run_id": run_id,
        "treatment": treatment,
        "reader_id": output_path.stem.removesuffix("_ayah_walk"),
        "prompt_path": prompt_raw,
        "prompt_sha256": prompt_hash,
        "prompt_revision": find_revision_with_hash(prompt_raw, prompt_hash),
        "packet_path": packet_raw,
        "packet_sha256": sha256_file(packet_path),
        "output_path": output_raw,
        "output_sha256": output_hash,
        "output_revision": find_revision_with_hash(output_raw, output_hash),
        "frozen_manifest_path": manifest_raw,
        "frozen_manifest_sha256": sha256_file(manifest_path) if manifest_path else "",
        "visible_refs": join_scalar(visible_refs),
        "provenance_status": provenance_status,
        "notes": notes,
    }


def discover_runs(surah: int, allow_single_run: bool) -> tuple[list[dict[str, str]], list[SourceBlock]]:
    tag = f"s{surah:03d}"
    standard_root = REPO_ROOT / "v12" / "runs" / tag
    packet_path = standard_root / "full_context_packet.json"
    control_root = standard_root / "full_context_control"
    if not packet_path.is_file():
        raise FileNotFoundError(f"missing packet: {packet_path}")

    rows: list[dict[str, str]] = []
    blocks: list[SourceBlock] = []
    manifest_path = control_root / "frozen_run.json"
    if manifest_path.is_file():
        manifest = read_json(manifest_path)
        output_path = REPO_ROOT / manifest["output_file"]
        prompt_path = REPO_ROOT / manifest["prompt"]
        if sha256_file(packet_path) != manifest["packet_sha256"]:
            raise ValueError(f"packet hash differs from frozen manifest: {manifest_path}")
        if sha256_file(output_path) != manifest["output_file_sha256"]:
            raise ValueError(f"output hash differs from frozen manifest: {manifest_path}")
        prompt_hash = manifest["prompt_sha256"]
        prompt_revision = find_revision_with_hash(manifest["prompt"], prompt_hash)
        standard_blocks = parse_reader_blocks(output_path, f"{tag}_standard")
        visible = sorted(
            {block.fixed_ayah_ref for block in standard_blocks}, key=ayah_sort_key
        )
        row = _run_row(
            run_id=f"{tag}_standard",
            treatment="standard_v12_full_context",
            prompt_path=prompt_path,
            packet_path=packet_path,
            output_path=output_path,
            manifest_path=manifest_path,
            visible_refs=visible,
            provenance_status="frozen",
            notes="Packet and output are frozen by manifest; historical prompt revision is resolved when available.",
        )
        row["prompt_sha256"] = prompt_hash
        row["prompt_revision"] = prompt_revision
        rows.append(row)
        blocks.extend(standard_blocks)
    else:
        candidates = sorted(control_root.glob("*_ayah_walk.md"))
        if len(candidates) != 1:
            raise ValueError(
                f"cannot choose standard output for {tag}: found {len(candidates)} candidates"
            )
        output_path = candidates[0]
        prompt_path = REPO_ROOT / "v12" / "prompts" / "reader.md"
        standard_blocks = parse_reader_blocks(output_path, f"{tag}_standard")
        visible = sorted(
            {block.fixed_ayah_ref for block in standard_blocks}, key=ayah_sort_key
        )
        rows.append(
            _run_row(
                run_id=f"{tag}_standard",
                treatment="standard_v12_full_context",
                prompt_path=prompt_path,
                packet_path=packet_path,
                output_path=output_path,
                manifest_path=None,
                visible_refs=visible,
                provenance_status="reconstructed_unverified",
                notes="No frozen manifest; the sole analytical output is used with explicit reconstructed provenance.",
            )
        )
        blocks.extend(standard_blocks)

    eleven_root = REPO_ROOT / "v12" / "runs_11ayah" / tag / "full_context_control"
    eleven_candidates = sorted(eleven_root.glob("*_ayah_walk.md")) if eleven_root.exists() else []
    if eleven_candidates:
        if len(eleven_candidates) != 1:
            raise ValueError(
                f"cannot choose eleven-ayah output for {tag}: found {len(eleven_candidates)} candidates"
            )
        output_path = eleven_candidates[0]
        prompt_path = REPO_ROOT / "v12" / "prompts" / "reader_11ayah.md"
        eleven_blocks = parse_reader_blocks(output_path, f"{tag}_eleven")
        visible = sorted(
            {block.fixed_ayah_ref for block in eleven_blocks}, key=ayah_sort_key
        )
        pending_count = sum(
            "pending retrospective pass" in block.text.lower()
            for block in eleven_blocks
            if block.finding_type == "retrospective_surprise"
        )
        packet_refs = set(read_json(packet_path).get("window", []))
        missing_count = len(packet_refs - set(visible))
        notes = (
            "No run-time manifest binds this reader output to a packet; provenance is reconstructed. "
            f"Detected {pending_count} pending retrospective section(s) and {missing_count} packet ref(s) without output headings."
        )
        rows.append(
            _run_row(
                run_id=f"{tag}_eleven",
                treatment="eleven_ayah_p5_full_context",
                prompt_path=prompt_path,
                packet_path=packet_path,
                output_path=output_path,
                manifest_path=None,
                visible_refs=visible,
                provenance_status="reconstructed_unverified",
                notes=notes,
            )
        )
        blocks.extend(eleven_blocks)
    elif not allow_single_run:
        raise FileNotFoundError(f"no eleven-ayah reader output for {tag}")

    return rows, blocks


def same_run_artifacts(
    established: list[dict[str, str]], discovered: list[dict[str, str]]
) -> bool:
    identity_fields = (
        "treatment",
        "packet_path",
        "packet_sha256",
        "output_path",
        "output_sha256",
    )
    established_keys = {
        tuple(row[field] for field in identity_fields) for row in established
    }
    discovered_keys = {
        tuple(row[field] for field in identity_fields) for row in discovered
    }
    return len(established) == len(discovered) and established_keys == discovered_keys


def remap_blocks_to_established_runs(
    blocks: list[SourceBlock],
    discovered_runs: list[dict[str, str]],
    established_runs: list[dict[str, str]],
) -> list[SourceBlock]:
    established_by_output = {
        row["output_path"]: row["run_id"] for row in established_runs
    }
    run_map = {
        row["run_id"]: established_by_output[row["output_path"]]
        for row in discovered_runs
    }
    remapped: list[SourceBlock] = []
    for block in blocks:
        run_id = run_map[block.run_id]
        remapped.append(
            SourceBlock(
                block_id=block.block_id.replace(block.run_id, run_id, 1),
                run_id=run_id,
                fixed_ayah_ref=block.fixed_ayah_ref,
                finding_type=block.finding_type,
                source_pointer=block.source_pointer,
                source_end_pointer=block.source_end_pointer,
                raw_sha256=block.raw_sha256,
                text=block.text,
            )
        )
    return remapped


def write_source_blocks(path: Path, blocks: list[SourceBlock]) -> None:
    atomic_write_json(path, {"blocks": [asdict(block) for block in blocks]})


def read_source_blocks(path: Path) -> list[SourceBlock]:
    return [SourceBlock(**item) for item in read_json(path)["blocks"]]


def hydrate_existing_source_blocks(
    workspace: Path, surah: int, *, allow_single_run: bool = False
) -> list[SourceBlock]:
    """Rebuild disposable source blocks without changing established run IDs."""
    discovered_runs, blocks = discover_runs(surah, allow_single_run)
    established_runs = read_tsv(workspace / "runs.tsv")
    if not same_run_artifacts(established_runs, discovered_runs):
        raise ValueError("discovered reader artifacts differ from established runs.tsv")
    remapped = remap_blocks_to_established_runs(
        blocks, discovered_runs, established_runs
    )
    block_pointers = {block.source_pointer for block in remapped}
    missing = {
        row["source_pointer"]
        for row in read_tsv(workspace / "source_findings.tsv")
        if row["source_pointer"] not in block_pointers
    }
    if missing:
        raise ValueError(
            f"cannot hydrate source text for finding pointers: {sorted(missing)}"
        )
    write_source_blocks(workspace / "automation" / "source_blocks.json", remapped)
    return remapped


class PacketIndex:
    def __init__(self, packet_path: Path) -> None:
        self.path = packet_path
        self.raw_path = repo_relative(packet_path)
        self.data = read_json(packet_path)
        self.ayahs: dict[str, dict[str, Any]] = {
            ayah["ref"]: ayah for ayah in self.data.get("ayat", [])
        }
        self.occurrences: dict[tuple[str, int, str], dict[str, str]] = {}
        for ayah in self.data.get("ayat", []):
            ref = ayah["ref"]
            for occurrence in ayah.get("root_occurrences", []):
                root = " ".join(occurrence["root"].split())
                indices = occurrence.get("word_indices", [])
                surfaces = occurrence.get("surfaces_ar", [])
                lemmas = occurrence.get("lemmas_ar", [])
                tags = occurrence.get("pos_tags", [])
                for position, raw_index in enumerate(indices):
                    key = (ref, int(raw_index), root)
                    self.occurrences[key] = {
                        "surface": surfaces[position],
                        "lemma": lemmas[position],
                        "pos": tags[position],
                    }
        self.inventories: dict[str, dict[str, dict[str, Any]]] = {}
        for inventory in self.data.get("branch_inventories", []):
            root = " ".join(inventory["root"].split())
            self.inventories[root] = {
                branch["branch_id"]: branch for branch in inventory.get("branches", [])
            }
        self.inventory_lines = self._inventory_lines()

    def _inventory_lines(self) -> dict[tuple[str, str], int]:
        lines = self.path.read_text(encoding="utf-8").splitlines()
        inside = False
        root = ""
        result: dict[tuple[str, str], int] = {}
        root_pattern = re.compile(r'^\s*"root":\s*"([^"]+)"')
        branch_pattern = re.compile(r'^\s*"branch_id":\s*"(B[0-9]{3})"')
        for line_number, line in enumerate(lines, start=1):
            if '"branch_inventories"' in line:
                inside = True
                continue
            if not inside:
                continue
            root_match = root_pattern.match(line)
            if root_match:
                root = " ".join(root_match.group(1).split())
                continue
            branch_match = branch_pattern.match(line)
            if branch_match and root:
                result[(root, branch_match.group(1))] = line_number
        return result

    def occurrence(self, ref: str, word_index: int, root: str) -> dict[str, str] | None:
        return self.occurrences.get((ref, word_index, " ".join(root.split())))

    def branch(self, root: str, branch: str) -> dict[str, Any] | None:
        return self.inventories.get(" ".join(root.split()), {}).get(branch)

    def inventory_pointer(self, root: str, branch: str) -> str:
        line = self.inventory_lines.get((" ".join(root.split()), branch))
        return f"{self.raw_path}:{line}" if line else ""

    def compact_context(
        self, target_ref: str, source_rows: list[dict[str, str]]
    ) -> dict[str, Any]:
        refs = {target_ref}
        cited_by_root: dict[str, set[str]] = {}
        for row in source_rows:
            refs.update(split_scalar(row["support_refs"]))
            for key in split_scalar(row["claimed_branches"]):
                normalized = normalize_branch_key(key)
                root, branch = normalized.rsplit(":", 1)
                cited_by_root.setdefault(root, set()).add(branch)
        target = self.ayahs.get(target_ref, {})
        target_roots: set[str] = set()
        for occurrence in target.get("root_occurrences", []):
            target_roots.add(" ".join(occurrence["root"].split()))
        roots = set(cited_by_root) | target_roots

        inventories: list[dict[str, Any]] = []
        for root in sorted(roots):
            branches = self.inventories.get(root, {})
            if root in target_roots:
                selected = list(branches.values())
                selection = "full_target_root_inventory"
            else:
                selected = [
                    branches[branch]
                    for branch in sorted(cited_by_root.get(root, set()))
                    if branch in branches
                ]
                selection = "cited_support_branches_only"
            inventories.append(
                {"root": root, "selection": selection, "branches": selected}
            )
        return {
            "protocol": self.data.get("protocol"),
            "target_ref": target_ref,
            "ayat": [self.ayahs[ref] for ref in sorted(refs, key=ayah_sort_key) if ref in self.ayahs],
            "branch_inventories": inventories,
            "missing_branch_inventories": [
                item
                for item in self.data.get("missing_branch_inventories", [])
                if " ".join(str(item.get("root", "")).split()) in roots
            ],
        }


def render_stage_prompt(
    prompt_path: Path,
    *,
    stage: str,
    scope: str,
    runtime_payload: dict[str, Any],
    prior_errors: str = "",
) -> str:
    base = prompt_path.read_text(encoding="utf-8")
    error_section = (
        "\n## Repair Feedback\n\nThe prior attempt failed deterministic validation:\n\n"
        f"```text\n{prior_errors}\n```\n\nCorrect every listed failure.\n"
        if prior_errors
        else ""
    )
    payload = json.dumps(runtime_payload, ensure_ascii=False, indent=2)
    return (
        f"{base}\n\n## Runtime Assignment\n\n"
        f"Stage: `{stage}`\n\nScope: `{scope}`\n\n"
        "This task is assigned to a fresh stage worker. Use only the evidence embedded below or the exact local paths it names. "
        "Do not inspect other project analyses. Do not edit canonical files. Write only the assigned schema-governed result JSON.\n"
        f"{error_section}\n```json\n{payload}\n```\n"
    )


def run_validator(
    workspace: Path, *, strict: bool = False, scope: str = ""
) -> tuple[bool, str]:
    command = [
        os.fspath(Path(os.sys.executable)),
        os.fspath(SCRIPT_ROOT / "validate_workspace.py"),
        os.fspath(workspace),
    ]
    if scope:
        command.extend(["--scope", scope])
    if strict:
        command.append("--strict")
    completed = subprocess.run(
        command,
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return completed.returncode == 0, completed.stdout


def latest_stage_row(
    workspace: Path, scope: str, stage: str
) -> dict[str, str] | None:
    rows = read_tsv(workspace / "stage_status.tsv")
    candidates = [
        row for row in rows if row["scope_ref"] == scope and row["stage"] == stage
    ]
    if not candidates:
        return None
    return max(candidates, key=lambda row: int(row["attempt"]))


def begin_stage(
    workspace: Path,
    *,
    scope: str,
    stage: str,
    prompt_path: Path | None,
    input_paths: list[Path],
) -> dict[str, str]:
    path = workspace / "stage_status.tsv"
    rows = read_tsv(path)
    attempts = [
        int(row["attempt"])
        for row in rows
        if row["scope_ref"] == scope and row["stage"] == stage
    ]
    attempt = max(attempts, default=0) + 1
    prompt_raw = repo_relative(prompt_path) if prompt_path else ""
    row = {
        "stage_id": f"st-{workspace.name}-{scope.replace(':', '_')}-{stage}-{attempt:03d}",
        "scope_ref": scope,
        "stage": stage,
        "status": "running",
        "attempt": str(attempt),
        "prompt_path": prompt_raw,
        "prompt_sha256": sha256_file(prompt_path) if prompt_path else "",
        "prompt_revision": (
            find_revision_with_hash(prompt_raw, sha256_file(prompt_path))
            if prompt_path
            else ""
        ),
        "input_fingerprint": fingerprint_paths(input_paths),
        "output_fingerprint": "",
        "started_at": utc_now(),
        "completed_at": "",
        "error_summary": "",
        "notes": "Agent-orchestrated stage; the worker returns JSON and canonical writes stay centralized.",
    }
    rows.append(row)
    write_tsv(path, rows)
    return row


def end_stage(
    workspace: Path,
    stage_id: str,
    *,
    status: str,
    output_paths: list[Path],
    error_summary: str = "",
    notes: str = "",
) -> None:
    path = workspace / "stage_status.tsv"
    rows = read_tsv(path)
    matched = False
    for row in rows:
        if row["stage_id"] != stage_id:
            continue
        matched = True
        row["status"] = status
        row["completed_at"] = utc_now()
        row["output_fingerprint"] = (
            fingerprint_paths(output_paths) if status == "complete" else ""
        )
        row["error_summary"] = error_summary.replace("\t", " ").replace("\n", " ")[:1000]
        if notes:
            row["notes"] = notes.replace("\t", " ").replace("\n", " ")
    if not matched:
        raise KeyError(f"unknown stage_id {stage_id}")
    write_tsv(path, rows)


def snapshot_tables(workspace: Path, filenames: Iterable[str]) -> dict[str, bytes]:
    return {filename: (workspace / filename).read_bytes() for filename in filenames}


def restore_tables(workspace: Path, snapshot: dict[str, bytes]) -> None:
    for filename, content in snapshot.items():
        path = workspace / filename
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{path.name}.", suffix=".restore", dir=path.parent
        )
        temporary = Path(temporary_name)
        try:
            with os.fdopen(descriptor, "wb") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)
