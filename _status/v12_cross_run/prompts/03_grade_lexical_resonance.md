# Prompt 03 — Lexical License and Resonance Grading

You adjudicate claim-specific branch occurrences. Your task is lexical and
mechanistic grading, not publication selection.

## Inputs

Read only:

- the assigned full-context packet;
- `runs.tsv`;
- `source_findings.tsv`;
- `claims.tsv`;
- `claim_sources.tsv`;
- analytical source lines reached through pointers;
- the assigned QAC word/morpheme bindings, attachment edges, and mechanical
  root-cooccurrence rows;
- the TSV schema and this prompt.

## Automated Output Contract

Do not edit canonical files. Write only the JSON object conforming to
`model_schemas/grade.json` at the assigned result path. The orchestrator
resolves word and morpheme IDs, surface, lemma, POS, inventory membership,
inventory pointer, evidence IDs, score totals, and strength buckets; it rejects
any response that conflicts with those deterministic facts.

QAC is the morphology authority. Attachment enrichment supplies syntax and
construction evidence. Root co-occurrence counts are descriptive corpus facts,
not semantic collocation judgments. Do not re-bind or recalculate them. Return
`linguistic_support_ids` only for supplied syntax/co-occurrence rows that
materially support or constrain an evidence item; otherwise return an empty
array.

## Permanent Retention

Record every cited branch, including branches that are missing, mismatched,
unlicensed, contradicted, or ultimately useless. `unlicensed` is a retained
classification, never an instruction to delete the row.

Add the direct lexical floor when a reader mechanism cites only a resonance.
Explain that addition in `decision_reason`; do not pretend the reader cited it.

## Lexical Classification

For each evidence item:

1. identify exact ayah, word index, root, and branch;
2. compare derivational form and construction with branch scope;
3. assign `evidence_role`;
4. assign exactly one `lexical_status`:
   - `direct`;
   - `contextually_activated`;
   - `analogical_resonance`;
   - `unlicensed`;
5. assign translation role;
6. record counterevidence and a concise decision reason.

Root identity alone is insufficient for `direct` or
`contextually_activated`.

`direct` and `contextually_activated` both require `form_fit` and
`construction_fit` to be `exact` or `compatible`. If either gate is `mismatch`
or `unknown`, use `analogical_resonance` when its full gate passes; otherwise
use `unlicensed`. Never label an item `direct` while recording a failed fit.

## Resonance Eligibility Gate

An analogical resonance requires:

- an accepted branch;
- an exact root anchor in the fixed ayah or an explicitly named contextual
  occurrence;
- a named activator;
- an explicit structural relation;
- a coherent reading change;
- an explicit reason the branch does not govern the ordinary lexical selection;
- any morphology/construction mismatch acknowledged when present.

If this gate fails, assign `unlicensed`, retain the row, leave scores blank,
and explain the failed gate.

## Resonance Scores

For eligible `analogical_resonance`, score each 0–2:

1. trigger specificity;
2. contextual proximity;
3. structural coupling;
4. reading gain;
5. robustness against alternatives and counterevidence.

The orchestrator sums the components and assigns:

- 8–10 `strong`;
- 5–7 `moderate`;
- 0–4 `weak`.

Cross-run agreement contributes zero points. Reader eloquence contributes zero
points. An explicit exploratory label is preserved as evidence about
robustness, not treated as an automatic rejection.

Return `null` for every component score that is not applicable. Do not return
the total or strength bucket; the orchestrator calculates both.

## Translation Rule

- Only evidence whose `occurrence_ref` is the fixed claim ayah may receive
  `governing` or `modifier`. Every support-ayah occurrence is `none`, even when
  its lexical status is `direct` in its own construction.
- `direct`: `governing`, `modifier`, or `none` according to claim relation;
- `contextually_activated`: `modifier` or `none`;
- `analogical_resonance`: always `none`;
- `unlicensed`: always `none`.

## Completion Checks

- Every branch used by every provisional claim has a retained row.
- Every primary lexical floor is present.
- Every resonance score is arithmetically correct.
- Every analogy and unlicensed row is blocked from translation.
- Every support-ayah row is blocked from translation.
- Every direct/contextual row passes both form and construction gates.
- The structural validator passes.
