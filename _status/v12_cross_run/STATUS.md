# v12 Cross-Run Publication Status

Checkpoint: 2026-07-22

Read [ORCHESTRATION.md](ORCHESTRATION.md) first when resuming. It contains the
current whole-surah direct-publication design.

## Decisions Now Fixed

- Canonical regular v12 is complete for S001-S114.
- ±5 v12 is complete for S001-S114.
- No new v12 reader runs are pending.
- An integration agent owns an entire surah, never one ayah.
- The agent reads the two complete source outputs on demand plus a compact
  packet-derived ayah roster and database-derived prevalidated anchor map. The
  full packet and linguistic cache remain coordinator-side.
- Agent A directly writes the semantic publication draft and then performs a mandatory,
  separate whole-surah self-audit against both source outputs.
- Every cited branch present in the assigned database is anchorable regardless
  of `status` or `contaminated`; those fields are coordinator-side audit
  metadata and never determine a finding grade.
- Malformed, nonexistent, or ambiguous citations receive stable `anchor_key`
  placeholders and enter one global post-draft repair pass; they do not pause
  Agent A. Final materialization remains blocked only for affected unresolved
  keys.
- There is no separate integration-review agent.
- There are no separate extraction, normalization, lexical-grading, or
  translation-eligibility stages in production.

## Final Finding Model

For each ayah:

- `findings`: zero or more same-class contextual readings, each with exactly one
  grade (`strong`, `weak`, or `reject`) and one or more
  `[qac_word_ref, root_id, branch_ids]` anchors.

An exploratory finding remains in the same array and is distinguished by its
grade. A finding graded `reject` remains fully stored; it is not moved to
another category and is not deleted.

Only rooted QAC words used as fixed-ayah anchors are published. Unrooted words,
unused roots, the complete QAC sentence spine, and context-only activator roots
are omitted. Multiple used branches for one word/root are grouped in the third
array slot.

The output does not carry source-finding IDs, translation roles, lexical
statuses, branch roles, or branch-level grades. Original v12 files remain the
provenance source.

Deduplication uses contextual-reading equivalence only. Shared roots or branches
never justify merging. Two readings with the same anchors remain separate when
their contextual mechanisms or reading changes differ.

## Mechanical Linguistic Work

`scripts/build_linguistic_bindings.py` already performs the required mechanical
alignment:

- assigns stable QAC word IDs;
- assigns QAC morpheme IDs and morphology;
- maps packet refs, including synthetic Basmalah refs, to QAC refs;
- cross-walks attachment units and syntax-edge endpoints to QAC words and
  morphemes without assuming equal indices;
- records binding methods, cautions, and unresolved warnings.

It already emits a QAC root string for every rooted word and morpheme, but it
now also emits `source_tokens.tsv` and `word_roots.tsv`. The source-token
crosswalk handles 37:130 explicitly: both displayed tokens in
`إِلْ يَاسِينَ` point to the same QAC word with
`many_source_to_one_qac`. A 114-surah in-memory audit aligned all 77,853 source
tokens to 77,852 QAC words and 128,976 morphemes.

The branch database is not a complete QAC root registry. Exact
`source_root_norm` matching resolves normalized-root collisions without an
arbitrary choice, and normalized/canonical fallback covers many remaining
spelling differences. The previously blocking binder-warning roots are now
covered by QAC-only registry rows: `ك ي ف`, `ل ف و`, `ء د د`, `ث ب ي`,
`س ن ه`, `ش م ز`, `ق ض ض`, and `ل و ت`. S1 and S10 linguistic caches are
currently materialized under this workspace.

This work remains script-owned and coordinator-side. The publication agent
does not consume, create, or align QAC and attachment identifiers.

## Current Implementation State

Implemented now:

- whole-surah v12 source files;
- deterministic package discovery, exact heading coverage, hashing, compact
  ayah roster, atomic anchor rows, and stable review keys;
- Agent A's whole-surah prompt, semantic-draft schema, and mandatory self-audit
  record contract;
- one global exception collector plus repair-agent prompt and schema;
- deterministic finalization, audit/hash checks, complete-database anchor
  checks, fixed-ayah QAC materialization, contextual-anchor filtering, and
  `finding_word_branches.tsv` derivation;
- linguistic binder protocol v2 with source-token, word, morpheme, root,
  attachment, and syntax crosswalks;
- the historical S1 calibration as a reference fixture.

Verified:

- all 6,326 packet ayat occur exactly once and in exact order in both selected
  reader families across S001-S114;
- all 73,225 raw `B...` citation occurrences enter anchor parsing;
- 30,327 of 30,417 unique citation keys resolve mechanically against the full
  database, with no `status` or `contaminated` filter;
- 90 keys across 29 surahs require surgical review; 54 source occurrences are
  malformed or omit a machine-associated root.

Still to execute before production:

1. run Agent A on fresh whole-surah S1 and S2 packages;
2. validate actual model output and resume behavior;
3. resolve the eight missing QAC root-registry entries and any binder warnings;
4. run the global anchor repair after all desired drafts;
5. quarantine legacy production helpers only after output parity is demonstrated.

## Publisher-Visible Size Audit

Counting every file Agent A can see (both readers, row-array roster, row-array
anchor map, prompt, schema, and package index), the corpus median is 178,720
bytes. S1 is 62,892 bytes; the largest case, S2, is 873,793 bytes. A byte/4
planning heuristic gives roughly 45k, 16k, and 218k tokens respectively, but
those are not tokenizer measurements. Agent A is instructed to read and save
one ayah at a time, so the complete file set need not be active context at once.

Do not resume the prepared S1 ayah tasks. They belong to the superseded design.

## Next Test

After the implementation is aligned with the new documentation:

1. build/refresh S1 linguistic bindings mechanically;
2. give Agent A the complete S1 source package;
3. have Agent A write the complete S1 publication;
4. have Agent A reread both sources against the saved draft ayah by ayah and
   correct its self-audit findings in place;
5. record self-audit completion against the semantic draft hash;
6. resolve any exception keys through the repair ledger;
7. materialize and validate final anchors and linguistic bindings;
8. commit the whole S1 result atomically.

After S1 closes, test the same whole-surah pattern on S2. S2 is the largest
practical input case and should use file access and incremental output, not
ayah-agent sharding.

## Production Readiness

The deterministic contract is implemented and its corpus-wide source/anchor
discovery passes. Production readiness now depends on the S1/S2 Agent A trials,
closing the known root-registry/binder warnings, and exercising the global
repair plus finalizer on real audited drafts.
