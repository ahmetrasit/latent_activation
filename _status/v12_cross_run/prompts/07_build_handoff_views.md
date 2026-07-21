# Optional Maintenance Note — Build Derived Views

This is an optional deterministic maintenance operation. Run it only when the
user requests derived views. It does not modify canonical TSVs or invoke a
model, and it does not require a separate audit stage.

## Inputs

- validated `claims.tsv`;
- validated `branch_evidence.tsv`;
- validated `claim_sources.tsv`;
- validated `coverage.tsv`.

## Derived Outputs

Create:

1. `commentary_view.tsv`:
   - accepted primary and secondary claims;
   - accepted exploratory claims clearly marked;
   - all labeled resonance evidence needed to explain them;
2. `translation_view.tsv`:
   - only evidence with `translation_role=governing` or `modifier`;
   - no analogical-resonance wording in any hidden notes;
3. `evidence_archive.tsv`:
   - every evidence and claim row, including unlicensed, evidence-only,
     deferred, conflict, and rejected material.

## Guardrails

- Derived views never replace canonical files.
- Strong resonance may enter commentary but never translation.
- Rejected and unlicensed rows must remain present in the archive view.
- Every derived row retains stable source, claim, and evidence IDs.
