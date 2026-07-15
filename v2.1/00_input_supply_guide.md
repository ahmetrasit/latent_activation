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

The adapter then rejects any returned row whose contamination value is not exactly `no` before writing `lexical-branches.jsonl`. Contamination and status are preparation controls; they are not exposed to agents.

The workflow does not reopen and rescan the complete V4 database during every later state. Preparation owns source selection; downstream roles use the frozen prepared inventory.

## Agent-facing lexical record

Every emitted record contains exactly:

```text
root_id
root_norm
branch_id
what_is_ar
branch_image_ar
source_phrase_ar
```

These six fields are the complete lexical evidence contract. No dictionary-entry join, source-family expansion, source-reference ledger, or additional provenance field is required. A run using both restored SQLite databases is `gold-ready`; fallback mode remains `source-limited` because the QAC fallback is rooted aggregate data.
