# S1 Cross-Run Decisions

Last updated: 2026-07-23

## Phase Status

- Phase 0 — provenance: complete.
- Phase 1 — atomic source extraction: complete; 80 findings retained.
- Ayah 1:6 — normalization through closed audit: complete.
- Remaining S1 ayahs — superseded by whole-surah v3 publication close.
- Corpus handoff: complete through the 114-surah Turkish v3 publication corpus.

## D001 — TSVs are canonical

The normalized TSV files in this directory are the hand-edited source of truth.
Any later SQLite database is generated from them and must not be edited
directly.

## D002 — Standard run provenance

The standard packet and output hashes match its frozen manifest. The manifest's
prompt hash no longer matches the current working-tree `reader.md`, but the
exact historical prompt is recoverable at git revision
`67b9f4ce1103ba46970cf0a441e0e087b0aa2623` and matches the recorded hash.
Therefore the run remains `frozen`; current prompt drift is recorded rather than
silently ignored.

## D003 — ±5 run provenance

The ±5 prompt and reader output were introduced together at git revision
`0dae8f970f799fe40f3ec1032ed94fa8831621ae`. The output visibly covers the same
S1 references and is consistent with the standard S1 packet. No run-time
manifest binds it to that packet hash, so its status is
`reconstructed_unverified`.

This run may contribute findings, but agreement with the standard run is
reader-stability evidence rather than a fully frozen experimental replication.

## D004 — Sources remain immutable

No source file under `v12/` will be rewritten during integration. Corrections,
classifications, merges, and exclusions are recorded here with source pointers.

## D005 — Non-loss treatment of unsuccessful material

Unlicensed evidence and rejected claims are permanent ledger outcomes, not
deletion instructions. Every such row must retain source lineage,
counterevidence, and a decision reason. Coverage must account for it.

## D006 — Resonance replaces the broad echo label

The production lexical status is `analogical_resonance`. Eligible resonance is
graded on trigger, proximity, structure, reading gain, and robustness. Failed
eligibility is recorded as `unlicensed`; it is never disguised as weak
resonance. Cross-run agreement contributes no score.

## D007 — 1:6 contained transit is secondary, not discarded

`ص ر ط:B002` swallowing and `ض ل ل:B002` hidden disappearance each score 9/10
(`strong`). Together with direct road/straightness and licensed loss evidence,
they support the accepted secondary contained-transit mechanism. Their
translation role remains `none`.

## D008 — Calibration audit

The 1:6 slice passes the strict validator with zero failures. The sole warning
is the already documented working-tree drift of the standard reader prompt;
the exact historical prompt remains hash-valid at the recorded git revision.
