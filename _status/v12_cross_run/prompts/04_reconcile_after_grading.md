# Prompt 04 — Targeted Adjudication After Lexical Grading

This is an exception-stage prompt. Use it only for the graded claims named by
the orchestrator because a material conflict, non-atomic claim, or necessary
split/merge blocks publication.

## Inputs

- `source_findings.tsv`;
- provisional `claims.tsv`;
- `claim_sources.tsv`;
- graded `branch_evidence.tsv`;
- source lines reached through pointers;
- the TSV schema and this prompt.

## Automated Output Contract

Do not edit canonical files. Write only the JSON object conforming to
`model_schemas/reconcile.json` at the assigned result path, with exactly one
decision per supplied claim.

- `keep`: sufficient support remains for publication review;
- `reject`: the mechanism fails after grading;
- `defer`: a split, merge, unavailable datum, or other unresolved operation is
  still required;
- `conflict`: material evidence remains genuinely opposed.

The orchestrator writes terminal reject/defer/conflict outcomes without
deleting source, claim, or evidence rows.

## Retention Rules

- A mechanism that fails all lexical/resonance support remains as a rejected
  claim rather than disappearing.

If the claim is not atomic enough to decide safely, use `defer`; do not perform
an undocumented split or merge in prose.

Do not assign publication roles in this stage. Successor claims use
`publication_role=unreviewed`.

## Completion Checks

- Every supplied claim receives exactly one action.
- Material conflicts remain visible.
- The structural validator passes.
