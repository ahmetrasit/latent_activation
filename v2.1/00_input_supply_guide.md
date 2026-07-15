# GSLS 2.1 Input Supply Guide

## Resource profile

`profiles/v1-local-resources.json` maps the workflow to the repository's existing resources:

| Purpose | Preferred resource | Fallback |
|---|---|---|
| Exact passage | `resources/quran/surah_{surah}.json` | none |
| Morphology | `resources/qac.sqlite` | `resources/qac_root_ayah.tsv` |
| Syntax annotations | `resources/attachments.tsv` | none |
| Lexical branches | `resources/furuq_v4.sqlite` | `resources/v4_branches.tsv` |

The operator also supplies an independently authored primary scaffold outside `resources/`, `v1/`, and other prohibited output locations.

## Prepared input set

`prepare_run.py` writes:

```text
inputs/run-card.json
inputs/passage-arabic.txt
inputs/primary-scaffold.md
inputs/morphology.tsv
inputs/syntax.tsv
inputs/lexical-branches.jsonl
inputs/input-summary.json
```

These prepared files are the frozen evidence boundary. Tasks list the subset each role may read. No source manifest or hash ledger is created.

## QAC adapter

When `resources/qac.sqlite` is present, the builder reads positioned rows directly from `qac_morphemes` through a read-only SQLite connection. The TSV fallback is used only when the database is unavailable. Missing morphology fields remain empty and must not be reconstructed by an agent.

## V4 adapter and contamination

When `resources/furuq_v4.sqlite` is present, passage roots are matched against the V4 `roots` table. Branch selection is limited to the requested statuses and includes this mandatory SQL predicate:

```sql
AND b.contaminated = 'no'
```

The adapter then rejects any returned row whose contamination value is not exactly `no` before writing `lexical-branches.jsonl`. Every prepared lexical record also carries `"contaminated": false`, and input preflight rejects any other value.

The workflow does not reopen and rescan the complete V4 database during every later state. Preparation owns source selection; downstream roles use the frozen prepared inventory.

## Source limitations

Current V4 branch prose is composite editorial evidence. Source-family labels are routing metadata, not independent attestations. Runs using this adapter remain `source-limited` and are not gold-release eligible.
