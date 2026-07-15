# GSLS V3 Input Supply Guide

## Local resources

V3 reads these repository resources directly:

| Purpose | Resource |
|---|---|
| Exact Arabic passage | `resources/quran/surah_{surah}.json` |
| Positioned morphology | `resources/qac.sqlite` |
| Local syntax | `resources/attachments.tsv` |
| Lexical branches | `resources/furuq_v4.sqlite` |

V3 intentionally has no TSV fallback for QAC or V4. The restored SQLite databases are the production sources.

## Primary scaffold

The operator supplies an independently authored direct reading as `--primary-scaffold`. It must not be copied from the gold reference or a prior latent-synthesis output.

The scaffold is withheld from A1's first discovery turn. It becomes available in A1's second turn and remains available to A2. Its role is to preserve the primary contextual proposition after discovery, not to decide in advance which secondary branches may activate.

## Prepared files

`prepare_run.py` writes:

```text
inputs/passage-arabic.txt
inputs/morphology.tsv
inputs/syntax.tsv
inputs/lexical-branches.jsonl
inputs/primary-scaffold.md
```

It also creates the empty task and output directories used by the four turns. It creates no run card, source manifest, input summary, hash ledger, or validation report.

## V4 selection

Passage roots come from positioned QAC morphology. They are matched to V4 roots, after which branch selection uses both predicates:

```sql
b.status = 'accepted'
AND b.contaminated = 'no'
```

Contamination and status stay inside preparation. Every agent-facing record contains exactly:

```text
root_id
root_norm
branch_id
what_is_ar
branch_image_ar
source_phrase_ar
```

No hidden lexical metadata may be reconstructed or imported by an agent.
