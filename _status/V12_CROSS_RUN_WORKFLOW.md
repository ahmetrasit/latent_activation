# v12 Cross-Run Publication Workflow

Status: whole-surah direct-publication design fixed; implementation pending

Scope: canonical regular v12 plus ±5 v12, both complete for S001-S114

Normative references:

- [orchestration](v12_cross_run/ORCHESTRATION.md);
- [current status](v12_cross_run/STATUS.md);
- [publication schema](v12_cross_run/schema/SCHEMA.md).

## Workflow

The orchestrator prepares one whole-surah package containing paths to both v12
outputs, the packet, and the deterministic linguistic cache.

Agent A reads the complete package on demand and directly writes the final
surah publication. Agent B checks the complete result for coverage,
over-merging, anchor validity, and grade structure. If necessary, Agent A gets
one repair pass.

There are no production extraction, normalization, lexical-grading, or
translation-eligibility agents.

## Finding Model

- Primary: contextual reading text plus `root_id` + `branch_id` anchors.
- Secondary: contextual reading text, anchors, and `strong`, `weak`, or
  `reject`.
- Every non-primary and exploratory finding becomes secondary.
- `Reject` is a retained grade, not deletion or a separate category.
- Source-finding IDs and branch-level labels are omitted.

Deduplication depends only on contextual-reading equivalence. Two different
contextual readings remain separate even when they cite identical branches.

## Mechanical Work

Scripts select and hash files, assign QAC word/morpheme IDs, align attachment
identifiers to QAC identifiers, validate anchors and structure, and commit the
whole surah atomically. Scripts do not reason about findings or spawn agents.

## Legacy S1

The current S1 ayah-scoped ledger is a historical calibration. Do not resume
its prepared ayah tasks. The first new test is one fresh whole-surah S1
publication followed by S2 as the largest input case.
