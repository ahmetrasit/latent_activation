# v12 Cross-Run Publication Status

Checkpoint: 2026-07-21

Read [ORCHESTRATION.md](ORCHESTRATION.md) first when resuming. It contains the
current whole-surah direct-publication design.

## Decisions Now Fixed

- Canonical regular v12 is complete for S001-S114.
- ±5 v12 is complete for S001-S114.
- No new v12 reader runs are pending.
- An integration agent owns an entire surah, never one ayah.
- The agent reads complete files on demand, following the original v12 access
  pattern; source files are not embedded into a large prompt payload.
- Agent A directly writes the publication output.
- Agent B performs only a narrow whole-surah integration review.
- There are no separate extraction, normalization, lexical-grading, or
  translation-eligibility stages in production.

## Final Finding Model

For each ayah:

- `primary`: contextual reading text plus assigned `root_id` + `branch_id`
  anchors; no grade;
- `secondary`: contextual reading text, assigned anchors, and exactly one grade:
  `strong`, `weak`, or `reject`.

Every non-primary or exploratory finding becomes secondary. A secondary graded
`reject` remains fully stored; it is not moved to another category and is not
deleted.

The output does not carry source-finding IDs, translation roles, lexical
statuses, branch roles, or branch-level grades. Original v12 files remain the
provenance source.

Deduplication uses contextual-reading equivalence only. Shared roots or branches
never justify merging. Two readings with the same anchors remain separate when
their contextual mechanisms or reading changes differ.

## Mechanical Linguistic Work

`scripts/build_linguistic_bindings.py` already performs the required mechanical
alignment:

- assigns stable QAC word IDs;
- assigns QAC morpheme IDs and morphology;
- maps packet refs, including synthetic Basmalah refs, to QAC refs;
- cross-walks attachment units and syntax-edge endpoints to QAC words and
  morphemes without assuming equal indices;
- records binding methods, cautions, and unresolved warnings.

This work remains script-owned. The publication agent only consumes the result;
it does not align QAC and attachment identifiers.

## Current Implementation State

Only documentation was updated for this decision. The existing production
implementation still reflects the superseded ayah-sharded, multi-stage
calibration workflow.

Reusable now:

- whole-surah v12 source files;
- linguistic binder protocol v2;
- QAC word/morpheme and attachment-alignment cache;
- source discovery, hashing, atomic file primitives, and packet lookup;
- the historical S1 calibration as a reference fixture.

Still to implement:

1. a compact whole-surah package index containing source paths and hashes;
2. the whole-surah publisher prompt and simplified publication schema;
3. the whole-surah integration-review prompt;
4. direct whole-surah result commit and minimal structural validation;
5. derived downstream views for the simplified primary/secondary model.

Do not resume the prepared S1 ayah tasks. They belong to the superseded design.

## Next Test

After the implementation is aligned with the new documentation:

1. build/refesh S1 linguistic bindings mechanically;
2. give Agent A the complete S1 source package;
3. have Agent A write the complete S1 publication;
4. have Agent B review the complete S1 result once;
5. give Agent A one repair pass only if needed;
6. run minimal structural and anchor validation;
7. commit the whole S1 result atomically.

After S1 closes, test the same whole-surah pattern on S2. S2 is the largest
practical input case and should use file access and incremental output, not
ayah-agent sharding.

## Production Readiness

The source runs and QAC/attachment binder are ready. The simplified
whole-surah publisher is not production-ready until the old task boundary and
output contracts are replaced and S1/S2 pass the new workflow.
