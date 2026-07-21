# network/v3: label-free channel discovery

This is the first workflow in this repo that treats channel detection as discovery instead of classification.

Cold-agent run and review instructions are in `network/v3/ORCHESTRATION.md`.

## What changed from `slm_local`

`network/slm_local` answers: “which of these predefined 8 domains are supported?”

`network/v3` answers: “which dense branch/root families and sparse role-progressive paths emerge from the surah-local SLM graph?”

Qnet keywords/themes are still used, but only after candidate generation, as labels for a blind reviewer.

## Inputs

The corpus workflow reads the Neo ensemble surah-local dense networks from
`../quran-slm`:

- `artifacts/surah_networks_global_ensemble/s###/affinity.npy`
- `artifacts/surah_networks_global_ensemble/s###/catalog.json`
- `artifacts/surah_networks_global_ensemble/s###/build_report.json`
- `artifacts/corpus_network/surah_resources/s###/branches_ar.tsv`

It also reads Qnet labels from `../quran-roots`:

- `_corpus/activation/Qnet/v2/network/incidence_full/branch_keywords.tsv`
- `_corpus/activation/Qnet/v2/network/bridge_theme_full/branch_theme_inventory.tsv`

## Method

1. Build a branch-level top-k graph from the SLM affinity matrix.
2. Mine ego-neighborhood clusters without semantic domain gates.
3. Optionally restrict to an ayah range before mining.
4. Require each candidate to span at least 3 roots and 3 ayahs by default.
5. Score candidates by graph cohesion, edge density, reciprocal support, strong-rank ratio, root diversity, and ayah span.
6. Attach Qnet facets as `label_hint` and `top_facets` after the cluster already exists.
7. Deduplicate near-identical candidates by branch/root/ayah overlap and subset containment.
8. Consolidate candidates into branch-preserving families with a mutual-kNN candidate-similarity graph.
9. Assemble sparse branch paths for channels whose evidence progresses through different semantic roles.
10. Consolidate overlapping paths into channel hypotheses for agent review.

Both consolidation layers preserve branch meanings; they group repeated graph objects and retain same-root branch alternatives for final review.

## Whole-corpus generation and resume

The current no-cap corpus run uses a five-ayah minimum where possible, the
Neo ensemble network, one surah at a time, and stage-level checkpoints:

```bash
python3 network/v3/run_corpus_candidates.py
```

Outputs go to `network/v3/experiments/corpus_neo_min5/s001…s114`; completed
stage summaries are reused, failures are recorded and skipped, and no review
agents are launched by the runner.

See `network/v3/ORCHESTRATION.md` before starting or resuming, especially to
avoid launching a second worker while an older corpus process is active.

## Candidate discovery

Run one surah with the default review cap against the Neo ensemble:

```bash
python3 network/v3/discover_surah_channels.py --surah 1 \
  --network-artifact-dir artifacts/surah_networks_global_ensemble
```

Run without a candidate cap:

```bash
python3 network/v3/discover_surah_channels.py --surah 18 --min-ayahs 5 \
  --candidate-limit 0 \
  --network-artifact-dir artifacts/surah_networks_global_ensemble
```

Run a passage:

```bash
python3 network/v3/discover_surah_channels.py \
  --surah 18 \
  --ayah-from 83 \
  --ayah-to 110 \
  --min-ayahs 5 \
  --candidate-limit 0 \
  --network-artifact-dir artifacts/surah_networks_global_ensemble \
  --output-dir network/v3/experiments/s18_083_110_min5_full
```

Candidate outputs:

- `channel_candidates.jsonl`: full candidate graph objects, including all induced branch edges.
- `channel_candidates.tsv`: compact review table.
- `summary.json`: run metadata and counts.

## Family consolidation

Run consolidation on any v3 candidate output directory:

```bash
python3 network/v3/consolidate_channel_families.py \
  --input-dir network/v3/experiments/s18_083_110_min5_full/s018
```

Family outputs are written under `families/`:

- `candidate_graphs.jsonl`: branch nodes/edges and seed provenance per candidate.
- `candidate_similarity_edges.tsv`: mutual-kNN candidate-similarity graph.
- `channel_families.jsonl`: branch-preserving family cards.
- `candidate_family_membership.tsv`: every candidate-to-family assignment.
- `family_branch_inventory.tsv`: core/optional/rare branch inventory.
- `review_queue.tsv`: ranked compact family review queue.
- `passage_windows.json`: ayah windows used for similarity profiles.
- `consolidation_summary.json`: counts and top-family metadata.

The default `--min-similarity 0.20` was chosen empirically because S18:83–110 stabilizes around 75–77 families at 0.20–0.15 without using a hard output target.

## Interpretation

A v3 raw candidate is not a final named channel; it is a graph-mined object that needs family consolidation.

A v3 family is still not a final judgment; it is the intended review unit for an agent or human.

## Sparse path assembly

Dense families can miss a channel when its branches form a connected script rather than one mutually similar cluster; path assembly therefore requires only a supported attachment for each new root.

```bash
python3 network/v3/assemble_semantic_paths.py \
  --surah 1 \
  --min-ayahs 5 \
  --path-limit 0 \
  --network-artifact-dir artifacts/surah_networks_global_ensemble \
  --family-input-dir network/v3/experiments/corpus_neo_min5 \
  --output-dir network/v3/experiments/corpus_neo_min5

python3 network/v3/consolidate_semantic_paths.py \
  --input-dir network/v3/experiments/corpus_neo_min5/s001/paths
```

Generation remains label-free: it searches the production SLM affinity graph using reciprocal rank support, distinct roots, and ayah coverage, while Qnet facets are attached only afterward as review labels.

Path outputs:

- `semantic_path_candidates.jsonl`: complete branch paths and attachment edges.
- `path_review_queue.tsv`: compact ungrouped path queue.
- `path_summary.json`: parameters and counts.

Consolidated outputs under `path_families/`:

- `semantic_path_families.jsonl`: complete path-family cards with branch alternatives by root.
- `path_family_review_queue.tsv`: compact blind-review package with branch-level ayah routing and representative/variant edge constructions.
- `path_similarity_edges.tsv`: evidence for path consolidation.
- `path_family_summary.json`: parameters and counts.

The dense-family and sparse-path passes are complementary: repeated-theme channels should survive the former, while route-like, causal, or role-progressive channels should survive the latter.

## Current validation

The Neo no-cap S1 path run produced 106,509 raw states, 5,598 deduplicated
paths, and 221 path families in a review queue of about 50K tokens.

A fresh blind agent using only that queue recovered 11 reasonable primary or latent channels, including the extended road/travel architecture, while rejecting recurrent anatomical, animal, and tool-sense noise.

The road architecture was recovered across related proposals rather than as one automatic nine-root card: worship/help → rectitude, paving → straight road, guidance ↔ straying, sign → guidance, praiseworthy goal → road, and walking/travel extensions.

The same Neo settings ran on S100 without S1-specific rules, producing 2,558
deduplicated paths and 126 path families.

## Known limitation

Path-family consolidation improves recall but does not make the final semantic decision: one channel may remain distributed across several PF rows, so the reviewing agent must merge related constructions and distinguish primary readings from latent lexical extensions.
