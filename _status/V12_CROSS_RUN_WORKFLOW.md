# v12 Cross-Run Integration Workflow

Status: controlled integration pilot ready; corpus production not yet ready

Scope: standard v12 plus eleven-ayah/±5 reader outputs

The normative instructions are:

- [agent orchestration](v12_cross_run/ORCHESTRATION.md);
- [current checkpoint and production gates](v12_cross_run/STATUS.md);
- [canonical schema](v12_cross_run/schema/SCHEMA.md);
- [stage prompts](v12_cross_run/prompts/);
- [worker result schemas](v12_cross_run/model_schemas/).

## Objective

Build one granular TSV ledger from both runs without confusing commentary
importance with lexical meaning. Preserve every source finding, including
unlicensed, deferred, conflicting, evidence-only, and rejected material.

## Decision Axes

1. `lexical_status`: `direct`, `contextually_activated`,
   `analogical_resonance`, or `unlicensed`;
2. `resonance_strength`: `strong`, `moderate`, `weak`, or `none`;
3. `publication_role`: `primary`, `secondary`, `exploratory`,
   `evidence_only`, or `none`;
4. `translation_role`: `governing`, `modifier`, or `none`;
5. `disposition`: retained editorial outcome, including `rejected`.

Multiple primary and secondary claims are allowed. Analogical resonance may be
important secondary commentary without becoming a translation sense.

## Agent-Orchestrated Flow

```text
bootstrap -> extract -> normalize -> grade -> publish -> close
```

The root orchestrator chooses scope and order, spawns fresh workers, receives
schema-governed JSON, and serializes canonical TSV commits. Scripts perform
only deterministic operations and never invoke agents or run the workflow.

Reconciliation is an exception path for a real conflict or necessary
split/merge. Strict audits and handoff views are optional.

## Production Source Pair

For each focus ayah, regular v12 must receive an actual focus ±2 packet and the
wide treatment an actual focus ±5 packet, both clipped at surah boundaries.
Each prompt/packet/output triple is independently frozen. Existing whole-surah
control packets remain useful calibration material but do not establish a
clean window comparison.

## Resonance Rubric

Eligible analogical resonance receives five 0–2 scores: trigger specificity,
contextual proximity, structural coupling, reading gain, and robustness.

- 8–10: strong;
- 5–7: moderate;
- 0–4: weak.

A failed gate is retained as `unlicensed`, not weak. Cross-run agreement scores
zero; silence in the other run is neutral.

## Current S1 Checkpoint

- both S1 reader outputs are extracted into 80 retained findings;
- 1:6 is the completed calibration example;
- 1:0, 1:2, and 1:5 are normalized and graded but await publication;
- swallowing/disappearance is retained as strong secondary analogical
  resonance with no translation access;
- 1:3, 1:4, and 1:7 await normalization, grading, and publication;
- the current ledger has 20 claims and 113 evidence rows with zero structural
  validation errors.

The exact task IDs, resume procedure, and source-layer blockers are maintained
in [v12_cross_run/STATUS.md](v12_cross_run/STATUS.md); do not infer them from
this summary.
