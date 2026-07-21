# Cold-agent orchestration: Neo open-channel discovery

Use this workflow to generate open-ended semantic-channel candidate families;
it does not classify evidence into the eight predefined `slm_local` domains.

## Scope and safety

- Read `../quran-slm` and `../quran-roots`; never modify either sibling repo.
- Write corpus outputs only under `network/v3/experiments/corpus_neo_min5/`.
- Run exactly one surah at a time because uncapped long-surah runs can consume
  more than 10 GB of memory.
- Do not launch review agents during corpus generation.
- Before starting or resuming, make sure another v3 corpus process is not
  already active; the runner lock prevents duplicate runner instances, but it
  cannot detect an older ad-hoc shell loop.

## Current corpus policy

- Network: `../quran-slm/artifacts/surah_networks_global_ensemble/s001…s114`.
- Dense candidate cap: none (`--candidate-limit 0`).
- Sparse path cap: none (`--path-limit 0`).
- Minimum ayah span: 5, except a three- or four-ayah surah uses its full length.
- Output: `network/v3/experiments/corpus_neo_min5/s###/`.
- Failure handling: record the failed stage, skip that surah, and continue.
- Review handling: generate families only; agent adjudication happens later.

## Resume the whole corpus

From the repository root run:

```bash
python3 network/v3/run_corpus_candidates.py
```

The runner processes S1 through S114 sequentially and resumes at stage level;
existing completion markers are authoritative, so already completed work is
not regenerated.

A `s###/stage_failure.json` marker prevents a known resource failure from being
retried on every ordinary resume; retry one deliberately only with
`--retry-failures` and a narrow surah range.

Useful controls:

```bash
python3 network/v3/run_corpus_candidates.py --start-surah 3
python3 network/v3/run_corpus_candidates.py --start-surah 30 --end-surah 57
python3 network/v3/run_corpus_candidates.py --start-surah 2 --end-surah 2 --retry-failures
python3 network/v3/run_corpus_candidates.py --dry-run
```

Do not split ranges among concurrent workers; range controls exist for manual
resume and diagnosis, not parallel generation.

## Stage checkpoints

For `s###`, the runner skips a stage only when its final summary exists:

1. Dense discovery: `s###/summary.json`.
2. Dense consolidation: `s###/families/consolidation_summary.json`.
3. Sparse assembly: `s###/paths/path_summary.json`.
4. Sparse consolidation: `s###/paths/path_families/path_family_summary.json`.

An interrupted stage may leave partial files; rerunning is safe because the
missing final summary causes that stage to be rebuilt while completed earlier
stages remain untouched.

S2 is a known exception: its uncapped assembly produced 190,625 deduplicated
paths, but sparse consolidation exited `137` under memory pressure; preserve
its completed dense and sparse-assembly checkpoints and leave its failure
marker in place until a more memory-efficient consolidator is available.

The runner appends command attempts to `dense.log`, `dense_consolidate.log`,
`sparse.log`, and `sparse_consolidate.log`, and writes aggregate progress to
`corpus_run_state.json`.

## Run one surah manually

Use the same output root and Neo ensemble as the corpus runner:

```bash
S=100
TAG=$(printf 's%03d' "$S")
OUT=network/v3/experiments/corpus_neo_min5

python3 network/v3/discover_surah_channels.py \
  --surah "$S" --min-ayahs 5 --candidate-limit 0 \
  --network-artifact-dir artifacts/surah_networks_global_ensemble \
  --output-dir "$OUT"

python3 network/v3/consolidate_channel_families.py \
  --input-dir "$OUT/$TAG"

python3 network/v3/assemble_semantic_paths.py \
  --surah "$S" --min-ayahs 5 --path-limit 0 \
  --network-artifact-dir artifacts/surah_networks_global_ensemble \
  --family-input-dir "$OUT" --output-dir "$OUT"

python3 network/v3/consolidate_semantic_paths.py \
  --input-dir "$OUT/$TAG/paths"
```

For a surah shorter than five ayat, replace `--min-ayahs 5` with its full ayah
count; the corpus runner does this automatically.

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
