# Optional Maintenance Note — Coverage and Retention Audit

This is an optional deterministic maintenance operation, not a production
stage and not a model-writing task. Run it only when the user explicitly asks
for a closed audit. It must not repair source, claim, lineage, or evidence rows
merely to make an audit pass.

## Inputs

Read:

- `runs.tsv`;
- `source_findings.tsv`;
- `claims.tsv`;
- `claim_sources.tsv`;
- `branch_evidence.tsv`;
- `stage_status.tsv` when present;
- the TSV schema and this prompt.

## Outputs

- complete `coverage.tsv`, one row per source finding;
- `audit_report.md` containing counts, failures, warnings, and exact row IDs.

## Non-Loss Audit

Fail if any source finding:

- lacks a coverage row;
- lacks a claim link unless explicitly deferred/rejected with a reason;
- disappeared during merge or split;
- is rejected without retained evidence or a retained claim;
- is represented only in prose and not in the ledger.

Unlicensed evidence and rejected claims count as retained only when their rows,
source links, and reasons remain resolvable.

## Lexical and Resonance Audit

Fail if:

- an inventory claim cannot be resolved;
- an analogical resonance lacks component scores;
- a score sum or strength bucket is incorrect;
- a failed gate is represented as weak resonance rather than `unlicensed`;
- analogical or unlicensed evidence has translation access;
- a primary claim lacks a direct/contextual fixed-ayah anchor.

## Publication Audit

Fail if:

- any claim remains `unreviewed`;
- a rejected claim has a public role;
- an accepted claim has `publication_role=none`;
- a merge or split lacks predecessor lineage;
- cross-run agreement was used as automatic confidence inflation;
- one-run silence was used as rejection evidence.

## Report Counts

Report counts by:

- source run and finding type;
- source disposition;
- lexical status;
- resonance strength;
- publication role;
- claim disposition;
- translation visibility;
- retained unlicensed evidence;
- retained rejected claims.

An explicitly requested audit closes only with zero failures. Normal production
does not depend on this operation.
