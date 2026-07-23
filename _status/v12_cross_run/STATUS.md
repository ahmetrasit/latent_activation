# v12 Cross-Run Publication Status

Checkpoint: 2026-07-23

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

## Current Turkish Publication State

As of this checkpoint, the Turkish v3 publication run has all 114 final
publication files under `_status/v12_cross_run/output/tr/`.

Complete and pushed:

- S001-S009;
- S010-S035;
- S036;
- S037-S114.

No surah remains unfinalized.

The final three completed publications were:

- S005: 121 ayat, 190 findings, publication SHA-256
  `f0fc70834a72d3ab8ea163c657cc6b1437a14d7b4d99b90a14044506a33bf7f0`;
- S009: 129 ayat, 220 findings, publication SHA-256
  `d9b3f75ea675142650e517a6daed4f761b942a5b0ce422419a4bbc3b5b19f3f7`;
- S036: 84 ayat, 194 findings, publication SHA-256
  `71b1958ac3dc0e9bda76806a0b08de8d9beab431f90327b4c45eb08933d899b7`.

Their worker IDs were:

- S005: `019f8d73-10af-78c2-a7da-f495fc6b6fbe`;
- S009: `019f8d73-0f6b-7181-8c93-c0daeb7192e8`;
- S036: `019f8d1b-1c01-7c30-9d6b-f603d2073768`.

These worker sessions are closed. Continue using the multi-agent connector only;
do not use `codex exec` for worker spawning. Production semantic workers use
`gpt-5.6-sol` with high reasoning effort and no priority or service-tier
override.

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

Corpus close is complete:

- final S005, S009, and S036 artifacts plus status documentation are committed
  and pushed;
- completed publication and QA worker sessions are closed;
- full corpus reconciliation passed over output counts, manifest hashes, ayah
  coverage, finding counts, and anchor materialization.

## Publisher-Visible Size Audit

Counting every file Agent A can see (both readers, row-array roster, row-array
anchor map, prompt, schema, and package index), the corpus median is 178,720
bytes. S1 is 62,892 bytes; the largest case, S2, is 873,793 bytes. A byte/4
planning heuristic gives roughly 45k, 16k, and 218k tokens respectively, but
those are not tokenizer measurements. Agent A is instructed to read and save
one ayah at a time, so the complete file set need not be active context at once.

Do not resume the prepared S1 ayah tasks. They belong to the superseded design.

## Current Resume Point

The Turkish v3 publication corpus is closed. Resume from downstream prose,
dictionary, import, or presentation work rather than from publication
orchestration.

The full 114-file corpus close audit verified:

- every expected output file exists exactly once;
- `_status/v12_cross_run/output/tr/` contains only
  `*_ayah_findings_publication.json` files;
- every final file is compact one-line JSON;
- each final manifest hash matches its final publication and derived TSV;
- aggregate ayah, finding, anchor-row, and branch-link counts reconcile.

## Production Readiness

The deterministic contract is implemented and has been exercised across the
complete Turkish publication run. The Turkish v3 publication corpus is
production-ready as a finalized artifact set.
