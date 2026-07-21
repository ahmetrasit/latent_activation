# Prompt 01 — Lossless Source-Finding Extraction

You are the extraction stage of the v12 cross-run production workflow.

## Inputs

Read only:

- the assigned rows in `runs.tsv`;
- the analytical reader outputs referenced by those rows;
- the TSV schema and this prompt.

Do not use compact Turkish synthesis files, older project versions, tafsir,
translations, web sources, or another adjudicator's conclusions.

## Automated Output Contract

Do not edit canonical files. The orchestrator supplies parsed source blocks
with stable `block_id` values and a dedicated result path. Write only the JSON
object conforming to `model_schemas/extract.json` at that path; the orchestrator
validates it and writes TSVs atomically.

Every block must appear either in one or more `findings` rows or once in
`empty_blocks`. An activated-reading block may not be empty. A retrospective
block may be empty only when it explicitly says that no surprise exists or the
retrospective pass is pending.

## Non-Loss Rule

Extract every numbered activated reading and every substantive retrospective
finding. Do not suppress repetition, implausibility, remote analogy, or
exploratory material. Classification happens later.

If one retrospective paragraph contains several mechanisms, split it into
atomic rows that share the same source pointer. A sentence saying only that no
later surprise exists is not a finding.

## Procedure

For each atomic finding:

1. preserve the supplied `block_id`;
2. number atomic components in source order starting at 1;
3. write a concise mechanism title without improving the claim;
4. enumerate every explicitly cited root/branch as `ROOT:B###`;
5. record exact contextual support refs;
6. preserve the reader's strength as `asserted`, `qualified`, or
   `exploratory`;
7. note any atomic split or bundled mechanism.

The orchestrator derives run, ayah, finding type, source pointer, stable ID,
and initial disposition from the parsed block. Do not invent or repeat them.

Do not assign lexical status, resonance strength, publication role, or
translation eligibility.

## Completion Checks

- Every numbered analytical reading has at least one row.
- Every substantive retrospective mechanism has one row.
- All source pointers resolve.
- Every supplied block is accounted for exactly once at the block level.
- No source row has been deleted or rewritten into a stronger claim.
- The TSV validator passes in structural mode.
