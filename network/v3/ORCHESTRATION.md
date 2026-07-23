# Cold-agent orchestration: Neo open-channel discovery

Use this workflow to generate open-ended semantic-channel candidate families;
it does not classify evidence into the eight predefined `slm_local` domains.

## Scope and safety

- Read `../quran-slm` and `../quran-roots`; never modify either sibling repo.
- Write corpus outputs only under `network/v3/experiments/corpus_neo_adaptive/`.
- Default to one surah at a time because uncapped long-surah generation is
  resource intensive even though sparse consolidation is now memory bounded.
  Bounded parallelism may be used for audited short-surah ranges.
- Do not launch review agents during corpus generation.
- Before starting or resuming, make sure another v3 corpus process is not
  already active; the runner lock prevents duplicate runner instances, but it
  cannot detect an older ad-hoc shell loop.

## Current corpus policy

- Network: `../quran-slm/artifacts/surah_networks_global_ensemble/s001…s114`.
- Dense candidate cap: none (`--candidate-limit 0`).
- Sparse path cap: none (`--path-limit 0`).
- Minimum ayah span: `max(min(ceil(0.10 * canonical_ayah_count), 10), 4)`.
- Output: `network/v3/experiments/corpus_neo_adaptive/s###/`.
- Failure handling: record the failed stage, skip that surah, and continue.
- Review handling: generate families only; agent adjudication happens later.
  Review-agent spawns must leave priority tier / `service_tier` unset.

## Current checkpoint status (2026-07-23)

The adaptive corpus is generated for all 111 eligible surahs:

- S1 through S102.
- S104 through S107.
- S109.
- S111 through S114.

The three canonical three-ayah surahs, S103, S108, and S110, are intentionally
excluded and are not pending work.

Completion is defined by the four final summaries for each eligible surah:

1. Dense discovery: `s###/summary.json`.
2. Dense consolidation: `s###/families/consolidation_summary.json`.
3. Sparse assembly: `s###/paths/path_summary.json`.
4. Sparse consolidation: `s###/paths/path_families/path_family_summary.json`.

Current aggregate generated counts:

- 89,199 dense candidates.
- 11,572 dense families.
- 4,157,715 sparse paths.
- 457,281 sparse path families.

No corpus-generation stages are currently pending. The next project step is
blind hierarchical review/adjudication using hydrated review bundles.

For an ordinary verification or resume pass, run:

```bash
python3 network/v3/run_corpus_candidates.py --skip-three-ayah-surahs
```

Historical `stage_failure.user_stop.json` markers may remain in S9 through S14
from the 2026-07-22 interrupted run, but they are superseded by the final
summary checkpoints and are retained only as audit records.

## General resume behavior

From the repository root run:

```bash
python3 network/v3/run_corpus_candidates.py
```

The runner processes S1 through S114 sequentially by default and resumes at
stage level; existing completion markers are authoritative, so already
completed work is not regenerated. Use `--skip-three-ayah-surahs` for normal
whole-corpus verification so S103, S108, and S110 are not rebuilt.

A `s###/stage_failure.json` marker prevents a known resource failure from being
retried on every ordinary resume; retry one deliberately only with
`--retry-failures` and a narrow surah range.

Useful controls:

```bash
python3 network/v3/run_corpus_candidates.py --start-surah 3
python3 network/v3/run_corpus_candidates.py --start-surah 30 --end-surah 57
python3 network/v3/run_corpus_candidates.py --start-surah 2 --end-surah 2 --retry-failures
python3 network/v3/run_corpus_candidates.py --start-surah 80 --end-surah 114 \
  --workers 4 --skip-three-ayah-surahs
python3 network/v3/run_corpus_candidates.py --dry-run
```

`--workers N` runs at most `N` surahs concurrently while keeping each surah's
four stages sequential. Use one worker for long-surah rebuilds unless the range
has been audited for memory use. Do not launch multiple runner processes; the
single runner owns the output lock and coordinates its workers.

`--skip-three-ayah-surahs` reads the canonical catalog and excludes S103, S108,
and S110 before creating their output directories.

## Stage checkpoints

For `s###`, the runner skips a stage only when its final summary exists:

1. Dense discovery: `s###/summary.json`.
2. Dense consolidation: `s###/families/consolidation_summary.json`.
3. Sparse assembly: `s###/paths/path_summary.json`.
4. Sparse consolidation: `s###/paths/path_families/path_family_summary.json`.

An interrupted stage may leave partial files; rerunning is safe because the
missing final summary causes that stage to be rebuilt while completed earlier
stages remain untouched.

S2 was the largest historical min-5 exception: its uncapped assembly produced
190,625 deduplicated paths and the old all-pairs consolidator exited `137`.
The memory-bounded consolidator completed that historical checkpoint with
685,764 similarity edges and 25,617 path families; the obsolete failure marker
is retained only as `stage_failure.pre_memory_fix.json` for audit. The current
adaptive S2 build uses `min_ayahs=10` and is complete in
`network/v3/experiments/corpus_neo_adaptive/s002/`.

The runner appends command attempts to `dense.log`, `dense_consolidate.log`,
`sparse.log`, and `sparse_consolidate.log`, and writes aggregate progress to
`corpus_run_state.json`.

## Run one surah manually

Use the same output root and Neo ensemble as the corpus runner:

```bash
S=100
TAG=$(printf 's%03d' "$S")
OUT=network/v3/experiments/corpus_neo_adaptive
CATALOG=../quran-slm/artifacts/surah_networks_global_ensemble/$TAG/catalog.json
AYAH_COUNT=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["ayah_max"])' "$CATALOG")
MIN_AYAHS=$(( (AYAH_COUNT + 9) / 10 ))
if [ "$MIN_AYAHS" -lt 4 ]; then MIN_AYAHS=4; fi
if [ "$MIN_AYAHS" -gt 10 ]; then MIN_AYAHS=10; fi

python3 network/v3/discover_surah_channels.py \
  --surah "$S" --min-ayahs "$MIN_AYAHS" --candidate-limit 0 \
  --network-artifact-dir artifacts/surah_networks_global_ensemble \
  --output-dir "$OUT"

python3 network/v3/consolidate_channel_families.py \
  --input-dir "$OUT/$TAG"

python3 network/v3/assemble_semantic_paths.py \
  --surah "$S" --min-ayahs "$MIN_AYAHS" --path-limit 0 \
  --network-artifact-dir artifacts/surah_networks_global_ensemble \
  --family-input-dir "$OUT" --output-dir "$OUT"

python3 network/v3/consolidate_semantic_paths.py \
  --input-dir "$OUT/$TAG/paths"
```

The corpus runner performs this calculation automatically. Without an explicit
skip, a three-ayah surah receives the minimum value `4` and yields no qualifying
channel. Pass `--skip-three-ayah-surahs` when those surahs must not be rebuilt.

## Blind review inputs

After generation is complete, build the hydrated review bundle:

```bash
python3 network/v3/build_review_bundle.py --surah-tag s###
```

Give a blind reviewer only `s###/review_bundle.json`. It contains unique branch
records with `branch_image_ar` and `what_is_ar`, surface ayah/root-token
context, compact support summaries, and dense/sparse candidate-family
references.

Do not give the reviewer gold findings, old channel lists, or predefined domain
targets during the first pass.

The first-pass prototype runbook is `network/v3/REVIEW_ORCHESTRATION.md`.
The reusable prompt is `network/v3/prompts/blind_candidate_review.md`.

## Blind review prompt

```text
Use only the supplied review bundle; do not inspect gold findings or prior reports.
Extract atomic motifs before clustering. Build subchannels through a one-scene test, consolidate parent channels only through explicit semantic invariants, and name resonance bridges between otherwise distinct subchannels.
Preserve coherent rare images as surprise probes. Do not flatten the report into one accepted-channel list and do not cap the number of parents, subchannels, bridges, or probes.
Surface coherent lexical imagery when the supplied branch evidence supports it. This is discovery and synthesis, not audit, grading, validation, or caution work.
```

## Required review report

For every parent channel report its semantic invariant, surface anchor,
supporting F/PF IDs, subchannels, bridge relations, lexical resonances,
surprise probes, branch evidence, ayah span, coherent prose synthesis, and
confidence dimensions. Confidence is reported separately for nucleus coherence,
evidence breadth, bridge clarity, and distinctness.

For every subchannel report its one-scene frame, atomic motifs, root:branch
evidence, surface token/root context, supporting rows, evidence breadth, reading
type (`surface-primary`, `latent/lexical`, or `mixed`), and coherent prose
synthesis. The prose should explain the scene or process, not list evidence as
a catalog.

Prototype reports are written to `network/v3/reviews/s###/reader_a_pilot.md`. There
is no artificial length limit. Cite F/PF IDs and branch evidence, but do not
copy full queue rows, file inventories, command transcripts, or audit records.
Do not summarize so strongly that concrete branch images supporting a parent,
subchannel, bridge, or surprise probe are lost. Do not demote coherent latent
lexical imagery merely because it is concrete, surprising, or not visible in
the surface translation.

## Large files

Uncompressed corpus `semantic_path_candidates.jsonl` files are ignored because
they can exceed 100 MB; retain them locally and commit a tested `.jsonl.gz`
copy only when explicitly requested.

## Interpretation

Dense and sparse families are candidate evidence, not final findings; a blind
agent or human performs the semantic consolidation only after generation.
