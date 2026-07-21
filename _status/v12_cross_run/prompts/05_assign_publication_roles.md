# Prompt 05 — Publication and Disposition Assignment

You assign claim-level publication roles after lexical and resonance grading.
You do not rewrite source findings or delete unsuccessful claims.

## Inputs

Read only:

- `source_findings.tsv`;
- `claims.tsv`;
- `claim_sources.tsv`;
- `branch_evidence.tsv`;
- source lines reached through pointers;
- the TSV schema and this prompt.

## Automated Output Contract

Do not edit canonical files. Write only the JSON object conforming to
`model_schemas/publish.json` at the assigned result path, with exactly one
decision per supplied claim. The orchestrator updates only publication role,
disposition, and decision reason, then derives coverage deterministically.

Claims already marked rejected, deferred, or conflict by targeted adjudication
must retain `publication_role=none` and the same disposition.

## Independent Axes

Do not infer publication role directly from lexical status or resonance score.

- lexical status answers whether a branch is directly licensed;
- resonance strength answers how strongly context activates an image;
- publication role answers how important the mechanism is for understanding
  the ayah;
- translation role answers what can affect rendering.

## Publication Rules

Assign `primary` when the mechanism:

- materially organizes the main ayah reading;
- has at least one direct or contextually activated fixed-ayah anchor;
- survives counterevidence;
- is not merely a decorative association.

Strong analogical resonance may support a primary commentary claim but can
never be its sole lexical anchor.

Assign `secondary` when the mechanism:

- materially enriches understanding without governing the base reading;
- normally has strong or moderate resonance, or a genuine contextual nuance;
- has explicit activators and a coherent reading change.

Assign `exploratory` when the mechanism:

- remains plausible but requires extra abductive moves;
- has weak or contested support;
- retains unresolved alternatives;
- was explicitly qualified by a reader and has not overcome that limitation.

Assign `evidence_only` when the record is valid and worth preserving but is
redundant, remote, too technical, or unsuitable for public prose.

Assign `publication_role=none` and `disposition=rejected` when the claim fails
its evidential or lexical mechanism. The claim, its sources, its evidence, and
the rejection reason all remain stored.

Use `deferred` for a decision requiring unavailable evidence and `conflict` for
an unresolved material disagreement.

Multiple primary and multiple secondary claims per ayah are allowed.

## Guardrails

- Run agreement does not automatically raise role.
- Run silence does not lower role.
- A high resonance score does not override morphology.
- `analogical_resonance` and `unlicensed` never receive translation access.
- Do not turn every interesting image into public commentary.

## Completion Checks

- No assigned claim remains `unreviewed`.
- Every decision has a reason.
- Rejected claims remain linked and queryable.
- Primary claims pass the direct/contextual anchor rule.
