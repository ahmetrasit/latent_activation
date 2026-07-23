# Whole-Surah Target-Language Baseline-Delta Publisher Contract (v3)

You own one complete surah. Open the assigned v3 package index exactly as
given. Read only its `publisher_inputs` and an existing v3 draft/checkpoint for
the same package. The two English analytical reader files are evidence; they
are not publication-language exemplars. The package declares the target
language and supplies its editorial profile. The roster supplies the fixed
Arabic text, the immutable ordinary target-language baseline, and its
target-token/QAC map. The anchor map translates source citations into compact
keys.

Write the semantic draft to `draft_output`, conforming exactly to the supplied
v3 draft schema. Emit every roster ayah exactly once and in exact order. The
draft contains only `ayah_ref` plus one flat `findings` array. Do not copy,
rewrite, improve, summarize, or otherwise emit the baseline: deterministic
finalization injects it verbatim from the hash-bound roster.

Serialize the draft and self-audit as canonical compact UTF-8 JSON: one line
per complete document, separators `,` and `:`, no insignificant whitespace,
plus one final newline. These are schema-bound JSON documents, not JSONL.

The roster may contain a canonical ayah absent from both analytical readers
because it has no rooted activation (for example `2:1`). Emit that roster ayah
with `findings: []`. Do not omit it, invent a finding, or treat the absence as a
source-coverage failure.

## Governing distinction

The baseline is the fixed ayah's ordinary target-language translation. A finding is
only the surprising difference made visible by v12's contextual root
activation. It may add a spatial, bodily, causal, relational, material,
temporal, compositional, or other secondary dimension; sharpen or correct an
initial reading; or record a later ayah's retrospective activation. It must not
replace the ordinary translation or retell the whole ayah.

Use this subtraction test before emitting any finding:

> If a target-language reader could derive the proposed sentence from the fixed
> baseline alone, without the contextual root activation, it is not a finding.

A source passage that only restates ordinary meaning is baseline-covered and
is omitted. That omission is not a rejection and does not violate source
coverage. A source passage that proposes a genuine addition or change remains
a candidate even when weak or ultimately rejected.

## Ayah procedure

For each roster ayah:

1. Read its fixed target-language baseline.
2. Read that ayah's `Activated readings` and `Retrospective surprises` from
   both analytical readers.
3. Identify each distinct baseline addition or change and the fixed-ayah roots
   that anchor it.
4. Exclude ordinary paraphrase, source derivation notes, broad surrounding
   themes, and mechanisms that cannot return to the fixed ayah.
5. Merge only true duplicate deltas. Shared branches, topic, or imagery alone
   do not make two deltas equivalent. When uncertain, keep them separate.
6. Render each surviving delta in the package's target language, following its
   language profile. Do not leave source-language English words or sentences.
   Do not write root-inventory prose.
7. Assign exactly one finding-level grade and supplied fixed-ayah anchor keys.

Each finding must be atomic enough that its grade and anchors apply to the
complete sentence. Do not flatten several different surprises into a smooth
summary paragraph. Necessary reference to the baseline is allowed, but the
finding's informational content must be the addition or change, not a new
translation.

## Grades

- `strong`: a clearly anchored contextual or retrospective activation that
  materially changes, organizes, or deepens the baseline reading;
- `weak`: a distinct anchored addition with real but indirect, limited, or
  tentative force;
- `reject`: a genuine proposed addition/change retained for audit, but whose
  mechanism is too speculative, incomplete, or misleading for default display.

Never use `strong` merely because a sentence accurately states the baseline.
Never delete a `reject` candidate or move it to another collection.

## Target language and register

Write findings in the declared target language, not translated analytical
English. Follow the hash-bound language profile for tokenizer, orthography,
register, loanword, terminology, and editorial decisions. The fixed baseline's
terminology is authoritative for referring to the ayah, but findings may use
clearer ordinary wording when explaining their added dimension. A future target
language changes the profile and baseline artifact, not this publication
method.

## Anchors

Each finding contains only `text`, `grade`, and `anchors`. Copy or combine only
supplied anchor keys. Do not invent, rewrite, or resolve keys. Use only roots
that occur in the fixed ayah and actually anchor that finding. A surrounding
ayah may activate the finding but is not a publication anchor.

Do not emit source IDs, primary/secondary roles, lexical or translation roles,
branch-level labels, scores, derivation notes, or prose outside the JSON
contract.

## Mandatory second-pass audit

After saving the complete draft, reopen it and audit one ayah at a time against
the baseline and both source sections. Correct the draft and recheck every
affected ayah. Confirm all of the following:

- roster coverage and order are exact;
- every finding is in the declared target language;
- every finding passes the baseline subtraction test;
- distinct activated and retrospective surprises were not flattened or lost;
- baseline-only prose was not emitted as a finding;
- duplicates were merged only by delta equivalence;
- every finding retains its fixed-ayah anchor keys;
- every finding has exactly one allowed grade;
- every rejected candidate remains present.

When stable, compute the draft SHA-256 and write `self_audit_output`:

```json
{
  "protocol": "v12-cross-run-self-audit-v3",
  "draft_sha256": "<64 lowercase hex characters>",
  "baseline_sha256": "<the package baseline hash>",
  "language": "<package BCP-47 language code>",
  "checked_ayah_refs": ["<every roster ref in exact order>"],
  "checks": {
    "target_language_only": true,
    "baseline_delta_only": true,
    "activated_and_retrospective_coverage": true,
    "atomic_findings": true,
    "fixed_ayah_anchors": true,
    "valid_grades": true
  },
  "completed": true
}
```

Resume only from a v3 draft belonging to the same surah, roster, baseline hash,
and source package. Repeat the complete audit before declaring completion.
