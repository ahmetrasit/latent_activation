# Whole-Surah Publication Schema

This document defines the target publication data model. Existing TSV templates
and staged worker JSON schemas in this directory belong to the legacy S1
calibration and are not the production output contract.

## Surah Object

```json
{
  "surah": 1,
  "ayat": []
}
```

- `surah`: integer surah number;
- `ayat`: exactly every packet ayah, once each and in packet order. It must
  equal the compact ayah roster; a row is required even when its `findings`
  array is empty.

The agent does not emit run provenance or source-finding IDs. The orchestrator
records source file paths and hashes outside the publication content.

## Ayah Object

```json
{
  "ayah_ref": "1:6",
  "findings": []
}
```

- `ayah_ref`: fixed ayah reference;
- `findings`: zero or more contextual findings with one common structure.

All substantive source findings must be represented without forcing a
primary/secondary hierarchy. Exploratory findings remain ordinary findings and
are distinguished by grade.

## Finalized Finding

```json
{
  "text": "contextual reading",
  "grade": "strong",
  "anchors": [
    ["1:6:1", "root_000000", ["B001"]]
  ]
}
```

Required fields:

- `text`: publication-ready contextual reading;
- `grade`: `strong`, `weak`, or `reject`;
- `anchors`: one or more materialized
  `[qac_word_ref, root_id, branch_ids]` rows. The semantic draft carries the
  corresponding compact anchor-key array instead.

`Reject` is a retained finding grade. It does not create a rejected collection
and never removes the finding's text or anchors.

## Anchor

Agent A uses compact anchor keys in its semantic draft:

```json
"anchors": ["a0001", "a0002"]
```

The agent-facing map is a column-described array of atomic rows. Independent
parallel arrays are forbidden because insertion, omission, or sorting can
silently associate the wrong root and branch.

After global exception repair, deterministic materialization replaces each key
with the public anchor form:

```json
["1:6:1", "root_000000", ["B001"]]
```

Anchor tuple slots are:

- slot 0: QAC word reference in sentence order;
- slot 1: stable database `root_id` mechanically bound to that QAC word;
- slot 2: one or more branch IDs from that root used by the finding.

Only rooted QAC words actually anchoring the finding are emitted. The final
publication does not contain a complete QAC word spine, unrooted words, unused
roots, or context-only anchors. Multiple used branches for one QAC word/root
are grouped in slot 2. When the same rooted word occurs more than once in the
ayah, a root-level source citation expands deterministically to each matching
QAC occurrence.

Surrounding-ayah roots may activate a finding and remain part of its prose, but
they are not publication anchors for the fixed ayah. Finalization filters those
contextual citation keys. A finding with no remaining fixed-ayah anchor fails
close and must be reviewed.

Anchors do not carry lexical status, translation role, evidence role,
resonance class, confidence, or any other context-independent label. A branch
may contribute differently to different contextual readings.

The orchestrator validates anchors mechanically against the complete assigned
`branch_images` snapshot. Branch `status` and `contaminated` metadata neither
remove an anchor nor affect a finding's presence or grade.

Malformed, nonexistent, or ambiguous source citations remain stable keys and
enter a coordinator-side exception ledger. When used as fixed-ayah anchors they
remain in the semantic draft and do not pause Agent A. A final publication
cannot contain an unresolved used key.

## Contextual Deduplication

Findings may be merged only when they express the same fixed-ayah contextual
reading, mechanism, structural/causal relation, and reading change.

- Same anchors with different contextual readings remain separate.
- Different anchors with the same contextual reading may be merged and their
  anchors combined.
- Similar themes with different mechanisms remain separate.
- Paraphrases or compatible elaborations of the same mechanism may merge.

When equivalence is uncertain, keep separate entries.

## Forbidden Publication Fields

The agent output must not contain:

- source-finding IDs or source lineage arrays;
- translation eligibility or translation roles;
- direct/contextual/analogical/unlicensed labels;
- branch-level grades or roles;
- primary/secondary roles or a separate exploratory/rejected collection;
- evidence-score components;
- agent-assigned QAC or attachment IDs.

If downstream systems need stable row IDs, scripts assign them after the
publication is complete.

## Deterministic Linguistic Cache

The linguistic cache is separate from the publication content and is generated
by `scripts/build_linguistic_bindings.py`.

- `source_tokens.tsv`: every whitespace-delimited Arabic token from packet text
  with a stable token ID and its one-to-one or many-to-one QAC `word_id`
  crosswalk;
- `words.tsv`: QAC-aligned orthographic words and stable `word_id` values;
- `morphemes.tsv`: QAC segments, morphology, and stable `morpheme_id` values;
- `word_roots.tsv`: normalized one-row-per-word/root bindings from QAC roots to
  stable database `root_id` values; words with no QAC root remain represented
  in `words.tsv` and receive no invented root;
- `attachment_units.tsv`: observed attachment units cross-walked to QAC words
  and morphemes;
- `syntax_edges.tsv`: attachment edges with resolved QAC endpoints;
- `root_cooccurrences.tsv`: mechanical descriptive root-pair counts;
- `manifest.json`: resource hashes, non-identity target-to-QAC ref overrides,
  counts, protocol, and unresolved warnings;
- `finding_word_branches.tsv`: post-publication rows expanding each finalized
  QAC/root anchor's branch list into exact finding/QAC/root/branch links.

Attachment and QAC index equality is never assumed. Alignment uses position,
normalized surface, root, sequence, and clitic evidence. Binding statuses
preserve word-only and fallback cautions; unresolved endpoints remain explicit.
Displayed-token and QAC-word equality is also never assumed: multiple displayed
tokens may bind to one QAC word, but every displayed token must have a row.

The coordinator uses this cache for mechanical and downstream checks. It is not
part of the publisher-visible package, and the agent never creates or repairs
its IDs.

## Minimal Validation

The final surah output must satisfy:

- one valid surah number;
- ayah refs exactly equal to the assigned packet roster, with no omission,
  duplicate, extra ref, or reordering;
- one `findings` array per ayah;
- nonempty finding text and anchors;
- exactly one allowed grade on every finding;
- every anchor resolves to the complete assigned root/branch snapshot and an
  actual rooted QAC word in the fixed ayah;
- anchors contain only `[qac_word_ref, root_id, branch_ids]` rows for roots used
  by that finding;
- no forbidden publication fields;
- no unresolved blocking linguistic warnings.
