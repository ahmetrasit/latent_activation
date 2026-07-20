# Semantic network candidate pipeline

This workspace turns the S1 branch-proximity graph from `../quran-slm` into
reviewable candidate packages.

The working assumption is:

```text
weighted branch graph
→ diversified path-family candidates
→ channel-level consolidation seeds
→ agent adjudication
→ later validation
```

The graph is useful as a candidate underlay, not as a final finding ranker.
Raw path traversal overgenerates; candidates must be consolidated before agent
review.

## Current package builder

```bash
python3 network/scripts/build_s1_candidate_package.py \
  --source-repo ../quran-slm \
  --output-dir network/output/s1_min5_strong_v0 \
  --min-ayahs 5 \
  --best-rank-threshold 8 \
  --mutual-rank-threshold 12 \
  --path-family-cap 1000 \
  --channel-seed-cap 200
```

Inputs are read from `../quran-slm`; outputs are written under `network/output/`.

## Review layers

- `path_family_candidates.jsonl`: ordered root-signature families satisfying
  the configured ayah-span and edge-strength rules.
- `channel_seed_candidates.jsonl`: higher-level unordered root-set seeds for
  merge/split review.
- `atomic_relations_inventory.jsonl`: supporting branch-pair evidence only.
  Atomic edges are not standalone chain findings when `min_ayahs > 2`.
- `package_summary.json`: build counts and policy.

## Agent labels

Use these during review:

- `PRIMARY`: supports a plain or primary reading.
- `INTERESTING`: non-obvious but coherent lexical resonance.
- `STRUCTURAL`: ring, contrast, sequence, or architecture.
- `WEAK`: coherent but thin/generic.
- `REJECT`: noisy/accidental.
- `SPLIT`: packet contains multiple findings.
- `MERGE`: same finding/channel as another packet.
