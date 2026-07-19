# QAC→Qnet coverage fix manifest — 2026-07-19

This fix fills Qnet coverage for QAC roots that already resolved to Furūq root/branch IDs but lacked Qnet node/theme rows. It uses leaf themes only; parent theme bridges are not used as evidence.

## Summary

- `missing_branch_ports_fixed`: `448`
- `affected_roots`: `305`
- `qnetless_roots_seeded`: `17`
- `partial_gap_roots_completed`: `291`
- `generated_keyword_count`: `120`
- `fallback_value_quality_only`: `2`
- `baseline_fk_failures_preserved`: `52`

## Qnetless roots seeded

- `root_002011` `ت ر ق` / QAC `ترق`: 2 Furūq branches, 1 QAC occurrences
- `root_002046` `ت و ر` / QAC `تور`: 3 Furūq branches, 2 QAC occurrences
- `root_002765` `ذ خ ر` / QAC `ذخر`: 3 Furūq branches, 1 QAC occurrences
- `root_003789` `ع ض و` / QAC `عضو`: 2 Furūq branches, 1 QAC occurrences
- `root_004186` `ق س ر` / QAC `قسر`: 8 Furūq branches, 1 QAC occurrences
- `root_004482` `ل د ن` / QAC `لدن`: 3 Furūq branches, 18 QAC occurrences
- `root_004914` `ن ف ي` / QAC `نفي`: 8 Furūq branches, 1 QAC occurrences
- `root_005216` `و س ن` / QAC `وسن`: 4 Furūq branches, 1 QAC occurrences
- `root_005229` `و ش ي` / QAC `وشي`: 11 Furūq branches, 1 QAC occurrences
- `root_005302` `و ن ي` / QAC `وني`: 3 Furūq branches, 1 QAC occurrences
- `root_005348` `ه ل ل` / QAC `هلل`: 9 Furūq branches, 5 QAC occurrences
- `root_005351` `س ط و` / QAC `سطو`: 4 Furūq branches, 1 QAC occurrences
- `root_005406` `ع ن و` / QAC `عنو`: 1 Furūq branches, 1 QAC occurrences
- `root_005440` `ء ل ل` / QAC `ءلل`: 19 Furūq branches, 2 QAC occurrences
- `root_005713` `ع ص و` / QAC `عصو`: 10 Furūq branches, 12 QAC occurrences
- `root_005748` `غ ل و` / QAC `غلو`: 10 Furūq branches, 2 QAC occurrences
- `root_005754` `ف ء ي` / QAC `فءي`: 3 Furūq branches, 11 QAC occurrences

## Generated keyword policy

Generated keyword prefix: `furuq_qac_sweep__`. Each generated keyword maps to a valid leaf theme in `theme_taxonomy`; all inserted memberships use `replicate_votes=2` because the source is deterministic Furūq branch evidence rather than a single human pass.

Full per-branch assignments are in the JSON manifest next to this file.
