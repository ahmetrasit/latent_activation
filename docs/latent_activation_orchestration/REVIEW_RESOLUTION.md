# Independent Review Resolution

Review date: 2026-07-19

The initial plan was reviewed independently and found to have seven
high-severity and three medium-severity gaps. This document records how the
corrected matrix-only plan resolves them.

## 1. Target Leakage

Finding: the builder-facing plan disclosed motivating images and prior
target-aware S1 diagnostics.

Resolution:

- target material moved to `SEALED_EVALUATION_CONTEXT.md`;
- builder receives an exact file allowlist;
- a history-free export or sandbox denying `.git/` is required because earlier
  commits contain unsanitized context;
- exposure invalidates the treatment and requires a fresh builder.

## 2. Root Identity Conflation

Finding: 1,688 source root IDs were treated as if they were 1,677 normalized
surface roots.

Resolution:

- `source_root_id`, `surface_root_key`, `branch_id`, `node_id`, and
  `matrix_index` are separate;
- matrix nodes preserve all 10,820 source rows;
- 11 surface-root collisions and 47 repeated surface-root/branch groups are hard
  fixtures;
- no source rows are merged.

## 3. v12/v13 Loader Conflict

Finding: existing loaders combine origin corpora and merge repeated branch
labels.

Resolution:

- builder protocol explicitly prohibits importing v12/v13 branch loaders;
- the canonical SQL includes `origin_corpus='quranic'`;
- quranic-only and no-merge assertions are hard gates;
- v13 remains a separate downstream workflow.

## 4. Undefined Activation Estimand

Finding: diffusion and root aggregation did not precisely model the stated
combinatorial problem.

Resolution:

- activation, diffusion, root aggregation, coalition search, and passage work
  were removed entirely;
- the project ends with complete matrices;
- consumers define their own estimand using the unpruned values.

## 5. Underspecified Graph and Search

Finding: graph fusion, symmetrization, pruning, and search ordering were not
reproducible.

Resolution:

- no graph or search is constructed;
- exact matrix equations, weights, dtype, ordering, block writes, and output
  formats are normative in `MATRIX_CONTRACT.md`;
- there are no thresholds or ranking tie-breakers in construction.

## 6. Subjective PASS/FAIL Gates

Finding: terms such as “meaningful” and “useful” permitted post-result choices.

Resolution:

- engineering gates are numerical and deterministic;
- cross-language alignment uses exactly 1,000 fixed null permutations;
- utility uses a separately frozen evaluator specification, 10,000 matched
  random sets, `p <= 0.01`, and a declared pilot coverage threshold;
- engineering validity and scientific utility are separate statuses.

## 7. Prediction-Aware References

Finding: the evaluator could construct references after seeing predictions.

Resolution:

- curator freezes identity mappings, schema, metrics, thresholds, and hashes
  before matrix access;
- human, adjudicated, and model pseudo-reference tiers are separate;
- reference manifest time and hash must predate evaluator access.

## 8. Conflicting Internal Contracts

Finding: root caps, coalition counts, schema fields, and reproducibility rules
conflicted.

Resolution:

- downstream contracts were removed;
- one normative node/matrix contract now controls shape, identity, formulas,
  status, and versioning;
- same-environment matrices must reconstruct byte-identically.

## 9. Storage Underestimation

Finding: the initial plan sized one view while requiring many.

Resolution:

- four embeddings and all three materialized float32 matrices are counted;
- canonical matrix payload is about 1.31 GiB;
- environment, model, partial files, and reserve are included in the 5 GiB
  minimum and 8 GiB recommendation;
- a 64-node canary projects peak resource use before the full run.

## 10. Environment Reproducibility

Finding: dependencies were unpinned and bootstrap was not operationally gated.

Resolution:

- v14 must provide `pyproject.toml`, `requirements.in`, and a transitive
  hash-locked `requirements.lock`;
- fresh Python 3.10 installation is a Phase 1 gate;
- OS, CPU, BLAS, threads, packages, model files, source, Git state, and seeds are
  recorded;
- model repository revision is pinned.

## 11. Scope Correction

The independent review exposed a larger issue: the original plan had drifted
from a complete 10,820 x 10,820 distance matrix into a sparse graph and analysis
pipeline.

The corrected boundary is:

```text
nodes + embeddings + complete matrices + validation + manifest
```

Everything involving passages, activations, graphs, searches, coalitions, or
interpretation is downstream and absent from v14.
