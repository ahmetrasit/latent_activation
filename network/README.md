# Semantic network workflow

The current production workflow is `network/slm_local/`.

Use it to build reviewable semantic-channel candidate packages from existing
`quran-slm` surah-local affinity bundles plus existing Qnet branch facets.

Experimental open-ended discovery work lives in `network/v3/`.

Use `network/v3/ORCHESTRATION.md` for the complete cold-agent generation,
resume, and later review procedure.

## Production workflow

Run one surah:

```bash
python3 network/slm_local/build_surah_channel_package.py --surah 100
```

Run the current test set:

```bash
python3 network/slm_local/build_surah_channel_package.py --surah 1
python3 network/slm_local/build_surah_channel_package.py --surah 100
python3 network/slm_local/build_surah_channel_package.py --surah 103
python3 network/slm_local/build_surah_channel_package.py --surah 48
```

Outputs are written to:

```text
network/slm_local/output/s###/
```

Use these files for normal review:

- `summary.json`
- `domain_channel_candidates.jsonl`
- `domain_channel_candidates.tsv`

Avoid loading `slm_edges.jsonl` into a review agent unless edge-level debugging
is required; it can be large, especially for S48.

Cold-agent instructions live in:

- `network/slm_local/ORCHESTRATION.md`
- `network/slm_local/README.md`

## Required local inputs

This repo does not own the source lexical/network artifacts.

Required sibling repositories:

- `../quran-slm`
- `../quran-roots`

The workflow reads these inputs and must not modify either sibling repo.

## Current generated packages

- S1: `network/slm_local/output/s001/`
- S100: `network/slm_local/output/s100/`
- S103: `network/slm_local/output/s103/`
- S48: `network/slm_local/output/s048/`

Known interpretation caveats:

- S48 `ن و س` is resolved upstream through canonical `ء ن س` alignment.
- S48 channel packages are over-broad and should be treated as recall-heavy.
- Contextual sense selection is unresolved, so one root occurrence can support
  multiple dictionary branch readings.

## Legacy experiments

These folders are retained for audit/history, not as the current workflow:

- `network/output/s1_min5_strong_v0/`: old S1 path-family candidate package.
- `network/v1/`: old S1 Qnet-enriched review-index experiment.
- `network/v2/`: old S1 channel-stability consolidation experiment.
- `network/scripts/build_s1_candidate_package.py`: old S1-only builder.

Do not start new production runs from these legacy folders unless explicitly
testing the older S1 methodology.

## Experimental discovery

Use `network/v3/` when the goal is open-ended channel discovery rather than
checking support for the predefined `slm_local` domains.

```bash
python3 network/v3/run_corpus_candidates.py
```

The corpus runner uses the Neo ensemble, a five-ayah minimum where possible,
no candidate/path caps, stage-level resume, and exactly one surah worker at a
time; outputs go to `network/v3/experiments/corpus_neo_min5/` and no agents are
launched during generation.

`v3` first mines graph clusters from the surah-local SLM network, attaches Qnet
facets as labels, consolidates dense families, and separately assembles sparse
cross-family paths; its final packages still require later agent or human
adjudication, so `slm_local` remains the stable predefined-domain validator.

Current blind validation shows that the sparse-path package can recover role-progressive channels such as S1 road/travel, but related pieces may remain split across several path families and require reviewer consolidation.

## Review labels

Use these labels when a human or agent reviews `slm_local` candidates:

- `strong`: coherent channel with enough roots, branches, ayah coverage, and
  interpretable branch images.
- `conditional`: partly coherent but composite, thin, generic, or dependent on
  one root/facet.
- `reject`: too narrow, over-broad, mislabeled, or mostly generic support.
