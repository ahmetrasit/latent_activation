# v12 Cross-Run Publication Workflow

Status: deterministic workflow implemented; Turkish v3 publication corpus closed

Scope: canonical regular v12 plus ±5 v12, both complete for S001-S114

Normative references:

- [orchestration](v12_cross_run/ORCHESTRATION.md);
- [current status](v12_cross_run/STATUS.md);
- [publication schema](v12_cross_run/schema/SCHEMA.md).

## Workflow

The orchestrator prepares one whole-surah package containing paths to both v12
outputs plus a compact packet-derived ayah roster and database-derived,
prevalidated anchor map.
The full packet and linguistic cache remain coordinator-side inputs.

Agent A reads the complete package on demand and directly writes the surah
semantic draft. It then begins a distinct second pass, rereads both source outputs
against the saved draft ayah by ayah, and corrects coverage, merging, anchor,
and grade-structure problems before deterministic close.

Agent A's semantic draft uses short anchor keys. Malformed, nonexistent, or
ambiguous keys are collected without pausing Agent A. After all drafts finish,
one global repair agent resolves the exception ledger and deterministic
materialization writes final `root_id` + `branch_id` anchors.

Every packet ayah must appear exactly once in packet order, including an ayah
whose `primary` and `secondary` arrays are both empty.

There are no production extraction, normalization, lexical-grading, or
translation-eligibility agents, and there is no separate integration-review
agent.

## Finding Model

- Semantic draft primary: contextual reading text plus compact anchor keys.
- Semantic draft secondary: contextual reading text, anchor keys, and `strong`,
  `weak`, or `reject`.
- Final publication: deterministic expansion of those keys to `root_id` +
  `branch_id` anchors.
- Every non-primary and exploratory finding becomes secondary.
- `Reject` is a retained grade, not deletion or a separate category.
- Source-finding IDs and branch-level labels are omitted.

Deduplication depends only on contextual-reading equivalence. Two different
contextual readings remain separate even when they cite identical branches.

## Mechanical Work

Scripts select and hash files, assign QAC word/morpheme IDs, align attachment
identifiers to QAC identifiers, map rooted words to stable database roots,
materialize anchors, derive finding/word/branch links, validate structure, and
commit the whole surah atomically. Scripts do not reason about findings or spawn
agents.

## Legacy S1

The current S1 ayah-scoped ledger is a historical calibration. Do not resume
its prepared ayah tasks. The whole-surah publication pattern has completed
across S001-S114, including S2 as the largest practical input case.
