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
- `ayat`: every processed ayah in packet order.

The agent does not emit run provenance or source-finding IDs. The orchestrator
records source file paths and hashes outside the publication content.

## Ayah Object

```json
{
  "ayah_ref": "1:6",
  "primary": [],
  "secondary": []
}
```

- `ayah_ref`: fixed ayah reference;
- `primary`: zero or more primary contextual findings;
- `secondary`: zero or more non-primary contextual findings.

All source findings must be represented substantively in one of these two
collections. Exploratory source findings become secondary.

## Primary Finding

```json
{
  "text": "contextual reading",
  "anchors": [
    {"root_id": "root_000000", "branch_id": "B001"}
  ]
}
```

Required fields:

- `text`: publication-ready contextual reading;
- `anchors`: one or more assigned root/branch anchors.

A primary finding has no grade.

## Secondary Finding

```json
{
  "text": "contextual reading",
  "grade": "strong",
  "anchors": [
    {"root_id": "root_000000", "branch_id": "B005"}
  ]
}
```

Required fields:

- `text`: publication-ready contextual reading;
- `grade`: `strong`, `weak`, or `reject`;
- `anchors`: one or more assigned root/branch anchors.

`Reject` is a retained secondary grade. It does not create a rejected
collection and never removes the finding's text or anchors.

## Anchor

```json
{"root_id": "root_000000", "branch_id": "B001"}
```

Only these fields belong to an anchor:

- `root_id`: stable root inventory identifier;
- `branch_id`: branch identifier within that root.

Anchors do not carry lexical status, translation role, evidence role,
resonance class, confidence, or any other context-independent label. A branch
may contribute differently to different contextual readings.

The orchestrator validates anchors mechanically against the assigned packet and
accepted inventory snapshot.

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
- a third exploratory or rejected collection;
- evidence-score components;
- agent-assigned QAC or attachment IDs.

If downstream systems need stable row IDs, scripts assign them after the
publication is complete.

## Deterministic Linguistic Cache

The linguistic cache is separate from the publication content and is generated
by `scripts/build_linguistic_bindings.py`.

- `words.tsv`: QAC-aligned orthographic words and stable `word_id` values;
- `morphemes.tsv`: QAC segments, morphology, and stable `morpheme_id` values;
- `attachment_units.tsv`: observed attachment units cross-walked to QAC words
  and morphemes;
- `syntax_edges.tsv`: attachment edges with resolved QAC endpoints;
- `root_cooccurrences.tsv`: mechanical descriptive root-pair counts;
- `manifest.json`: resource hashes, target-to-QAC ref mapping, counts, protocol,
  and unresolved warnings.

Attachment and QAC index equality is never assumed. Alignment uses position,
normalized surface, root, sequence, and clitic evidence. Binding statuses
preserve word-only and fallback cautions; unresolved endpoints remain explicit.

The agent reads this cache as needed but never creates or repairs its IDs.

## Minimal Validation

The final surah output must satisfy:

- one valid surah number;
- unique, ordered ayah refs belonging to the surah;
- arrays named only `primary` and `secondary` at finding level;
- nonempty finding text and anchors;
- no grade on primary;
- exactly one allowed grade on every secondary;
- every anchor resolves to the assigned root/branch inventory;
- no forbidden publication fields;
- no unresolved blocking linguistic warnings.
