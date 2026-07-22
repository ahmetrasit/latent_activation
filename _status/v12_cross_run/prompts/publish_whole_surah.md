# Whole-Surah Publisher Contract (Agent A)

You own one complete surah. Open the assigned package-index path exactly as
given by the orchestrator, verify that every listed publisher input exists, and
read only the files under `publisher_inputs` plus an existing draft/checkpoint
for this same package. Do not read the coordinator-only packet, linguistic
cache, branch database, legacy S1 ledgers, web sources, or other surahs.

Write `publication.draft.json` to the path in `draft_output`, conforming exactly
to the listed schema. The two reader files are evidence, the roster is the
mandatory output order, and `anchor_map.json` translates source citations into
compact keys. A key in `review_*` state is still usable: preserve it and never
guess its repair.

Keep active context bounded: load the compact roster and anchor map once, then
process one ayah's sections from both reader files together, save that draft
row, and continue. File access does not require holding both complete readers
in context simultaneously.

For every roster ayah, emit exactly one row in exact order. Consolidate the two
readers into one flat `findings` array. Findings have no primary/secondary role.
Merge only true contextual duplicates; shared branches or topic alone do not
make readings duplicates. When uncertain, keep them separate.

Each finding contains only publication text, one grade, and supplied anchor
keys for roots in the fixed ayah that anchor that reading. Copy or combine only
supplied keys; do not invent, rewrite, or resolve them. Do not include a key
solely because it names a surrounding-ayah activator. Every finding has exactly
one grade:

- `strong`: clear anchored mechanism that materially organizes or changes the reading;
- `weak`: distinct anchored reading with limited, indirect, or tentative force;
- `reject`: retained fully but not recommended for the default layer.

Never delete a rejected reading or create a separate rejection collection. Do
not emit source IDs, primary/secondary roles, lexical/translation/branch roles,
scores, reasoning notes, or prose outside the JSON contract.

After the full draft is saved, start a distinct self-audit. Reopen the saved
draft and, ayah by ayah, compare only that ayah's two source sections with its
draft row. Check roster coverage/order, substantive-reading coverage, duplicate
handling, preservation of the fixed-ayah anchor keys used by each finding, and
grade validity for every finding. Correct the file and recheck affected rows.
Do not certify from memory or invent new evidence.

When the corrected draft is stable, compute its SHA-256 and write
`self_audit.json` at the path in `self_audit_output`:

```json
{
  "protocol": "v12-cross-run-self-audit-v2",
  "draft_sha256": "<64 lowercase hex characters>",
  "checked_ayah_refs": ["<every roster ref in exact order>"],
  "completed": true
}
```

Resume rule: if a draft or audit exists, first verify it belongs to this surah
and roster. Continue from the first incomplete or invalid ayah, then repeat the
full self-audit before declaring completion.
