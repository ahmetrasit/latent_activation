# Branch Distance Matrix Documentation

Status: corrected execution plan; implementation has not started.

## Project Boundary

This project builds a reusable, complete distance representation for the 10,820
clean accepted Quranic branch records:

```text
stable node inventory
  + four fixed branch embeddings
  + 10,820 x 10,820 semantic distance matrix
  + 10,820 x 10,820 thematic-proxy distance matrix
  + 10,820 x 10,820 fixed combined distance matrix
  + validation and provenance manifests
```

It does not analyze ayat. It does not perform activation, traversal, depth-first
search, coalition extraction, interpretation, or prose generation. It does not
build a sparse graph. Those are downstream workflows that may consume the
matrices after the artifacts are frozen.

The complete matrices are canonical. A consumer may later derive a thresholded
graph or top-K index without forcing that information-losing decision on every
other consumer.

## Read By Role

Coordinator:

- [ORCHESTRATION_PLAN.md](ORCHESTRATION_PLAN.md)
- [REPOSITORY_AUDIT.md](REPOSITORY_AUDIT.md)
- [REVIEW_RESOLUTION.md](REVIEW_RESOLUTION.md)

Builder:

- [BUILDER_PROTOCOL.md](BUILDER_PROTOCOL.md)
- [MATRIX_CONTRACT.md](MATRIX_CONTRACT.md)
- [REPOSITORY_AUDIT.md](REPOSITORY_AUDIT.md)

Evaluator, only after the build manifest is frozen:

- [SEALED_EVALUATION_CONTEXT.md](SEALED_EVALUATION_CONTEXT.md)
- the frozen matrices and independently frozen reference specification

The builder must not read `SEALED_EVALUATION_CONTEXT.md`, prior run outputs, or
gold/reference material. The coordinator must enforce this with a history-free
export or a filesystem allowlist that also denies `.git/`. A normal checkout
with readable history is insufficient because earlier commits contain the
unsanitized plan. An honor-system prompt is insufficient.

## Fixed Decisions

1. Matrix rows and columns represent 10,820 source branch records.
2. Source identity and surface-root grouping remain separate.
3. The first treatment uses only rows with `origin_corpus='quranic'`,
   `status='accepted'`, and `contaminated='no'`.
4. Arabic and English image fields produce semantic representations.
5. Arabic and English scope fields produce a thematic-proxy representation.
6. Semantic and thematic-proxy matrices remain separately available.
7. A 50/50 combined matrix is materialized as a fixed convenience treatment.
8. All matrices are complete, symmetric, float32, and directly indexable.
9. No top-K pruning, thresholding, graph construction, or model training occurs.
10. A fixed multilingual encoder is the first treatment. Any adapted encoder is
    a separately frozen future treatment.

This treatment is zero-gold for the project, not pretraining-free. The fixed
encoder is an external learned prior whose original training exposure is not
fully auditable. A corpus-only sparse lexical baseline may be built later under
a different treatment ID, but it is not a substitute for the requested semantic
matrix.

## Important Limitation

A complete matrix solves the combinatorial storage and access problem. It does
not prove that a general encoder represents every desired secondary resonance.
The thematic matrix is explicitly a proxy derived from branch scope text.
Scientific utility must be tested later against an independently frozen blind
reference or by downstream workflows. Gold-free checks can establish integrity,
alignment, stability, and non-degeneracy, not interpretive truth.

## Resource Gate

At the latest check on 2026-07-19, the current filesystem had about 4.1 GiB
free. That is below the plan's execution gate.

Move or clone the repository to a filesystem with:

- at least 5 GiB free after checkout for the fixed-encoder matrix build;
- at least 15 GiB free only if a later treatment trains or adapts a model.

The three canonical float32 matrices require about 1.31 GiB in total. Model
weights, four embedding arrays, the Python environment, temporary blocks, and
atomic output copies account for the rest of the safety margin.

## Implementation Location

The implementation belongs under `v14/`. Existing `v13/` is a separate dynamic
retrieval workflow and must not be overwritten or imported as the branch loader.

The next action is Phase 0 of the orchestration plan. No full embedding or matrix
run should begin until storage, isolation, environment locking, source hashes,
and the canonical node-count gates pass.
