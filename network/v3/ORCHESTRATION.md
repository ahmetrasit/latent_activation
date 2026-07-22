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

## Current checkpoint status (2026-07-22)

The adaptive corpus has 94 fully completed surahs:

- S1 and S8.
- S20 through S102.
- S104 through S107, S109, and S111 through S114.

The three canonical three-ayah surahs, S103, S108, and S110, are intentionally
excluded and are not pending work.

Seventeen surahs remain: S2 through S7 and S9 through S19. Their checkpoints
are:

- S2 and S15 through S19: no completed stages.
- S3 through S7: dense discovery and dense consolidation are complete; sparse
  assembly was killed with return code `-9` during the six-worker run. Their
  `stage_failure.json` files are genuine resource-failure records.
- S9 through S13: both dense stages are complete; sparse assembly was stopped
  by the user before its summary checkpoint was written.
- S14: dense discovery is complete; dense consolidation was stopped before its
  summary checkpoint was written.

Run every remaining surah with exactly one worker. Do not use parallel workers
for this range: six-worker sparse assembly produced the S3–S7 OOM failures.

```bash
python3 network/v3/run_corpus_candidates.py \
  --start-surah 2 --end-surah 19 --workers 1 --retry-failures
```

The runner will reuse every completed stage, retry the genuine S3–S7 failure
markers, skip completed S8, and resume or start the other pending surahs. The
same command is safe to rerun after an interruption.

## General resume behavior

From the repository root run:

```bash
python3 network/v3/run_corpus_candidates.py
```

The runner processes S1 through S114 sequentially by default and resumes at
stage level; existing completion markers are authoritative, so already
completed work is not regenerated. For the current pending inventory, use the
single-worker S2–S19 command above rather than a whole-corpus invocation.

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
four stages sequential. Parallelism was used for already completed shorter
ranges, but must not be used for the remaining S2–S19 work. Do not launch
multiple runner processes; the single runner owns the output lock and
coordinates its workers.

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
adaptive S2 build, which uses `min_ayahs=10`, is still pending and must run
alone as the first item in the single-worker remaining range.

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

After generation is complete, give a blind reviewer only these compact queues:

- `s###/families/review_queue.tsv`.
- `s###/paths/path_families/path_family_review_queue.tsv`.

Do not give the reviewer gold findings, old channel lists, or predefined domain
targets during the first pass.

## Blind review prompt

```text
Use only the supplied review queues; do not inspect gold findings or prior reports.
Discover reasonable semantic channels, allowing either a dense repeated theme or a sparse progression through different semantic roles.
Consolidate related F/PF rows into channels and report title, supporting IDs, selected root:branch evidence, ayah span, construction, confidence, and reading type.
Reject dictionary-side-sense noise and do not assume every family is valid.
```

## Required review report

For every accepted channel report its title, supporting F/PF IDs, selected
root:branch evidence, distinct root and branch counts, ayah span, one-sentence
construction, confidence, and reading type (`primary`, `latent/lexical`, or
`mixed`).

Also report rejected noise classes, plausible fragmented channels, and any
accepted channel that depends on an inferred bridge absent from the supplied
construction paths.

## Large files

Uncompressed corpus `semantic_path_candidates.jsonl` files are ignored because
they can exceed 100 MB; retain them locally and commit a tested `.jsonl.gz`
copy only when explicitly requested.

## Interpretation

Dense and sparse families are candidate evidence, not final findings; a blind
agent or human performs the semantic consolidation only after generation.
