# S1 Ayah 1:6 Closed Audit

Audit date: 2026-07-21

Scope: `1:6`

Schema: v1

## Result

`PASS` — zero structural, lineage, lexical, resonance, publication,
translation, or retention failures.

The validator reports one provenance warning: the current standard
`v12/prompts/reader.md` has drifted, while the exact recorded prompt remains
recoverable and hash-valid at revision
`67b9f4ce1103ba46970cf0a441e0e087b0aa2623`. This is documented provenance,
not an audit failure.

## Counts

- source runs: 2;
- source findings: 13 — 8 activated readings, 5 retrospective findings;
- source dispositions: 1 accepted, 5 split, 7 merged;
- claims: 7 — 2 primary, 3 secondary, 1 exploratory, 1 evidence-only;
- claim dispositions: 6 accepted, 1 evidence-only;
- evidence rows: 40 — 25 direct, 2 contextually activated, 13 analogical
  resonances;
- resonance strength: 7 strong, 4 moderate, 2 weak, 27 not applicable;
- translation role: 13 governing, 27 none;
- coverage: 13 of 13 source findings;
- retained unlicensed evidence: 0 in this calibration slice;
- retained rejected claims: 0 in this calibration slice.

Zero unlicensed or rejected rows here is an observed result, not a filtering
rule. The schema, prompts, and validator require both categories to remain when
they occur.

## Material Decisions

- Swallowing (`ص ر ط:B002`) and hidden disappearance (`ض ل ل:B002`) score
  `9/10`, `strong`, and support the accepted secondary contained-transit
  mechanism. Both remain `analogical_resonance` with `translation_role=none`.
- Gift (`ه د ي:B004`), leading-front (`ه د ي:B003`), supported walking
  (`ه د ي:B008`), maintenance (`ق و م:B004`), and mainstay (`ق و م:B009`) are
  retained and graded separately from their direct lexical floors.
- Offering (`ه د ي:B005`) remains weak evidence-only resonance; sword, rock,
  and hide imagery remains moderate exploratory material.

## Reproduction

```bash
python3 _status/v12_cross_run/scripts/validate_workspace.py \
  _status/v12_cross_run/s001 --scope 1:6 --strict
```
