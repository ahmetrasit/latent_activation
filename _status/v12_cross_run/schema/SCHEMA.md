# Cross-Run TSV Schema v2

All files are UTF-8 TSV with one header row, no embedded tabs, and no embedded
newlines. Lists inside a scalar field use semicolons. Stable IDs are never
reused.

The exact headers are stored in `templates/` and enforced by the validator.

## `runs.tsv`

One row per source reader run.

```text
run_id
treatment
reader_id
prompt_path
prompt_sha256
prompt_revision
packet_path
packet_sha256
output_path
output_sha256
output_revision
frozen_manifest_path
frozen_manifest_sha256
visible_refs
provenance_status
notes
```

`provenance_status`:

- `frozen`;
- `reconstructed_verified`;
- `reconstructed_unverified`.

## `source_findings.tsv`

One row per atomic activated reading or retrospective finding. Extraction is
lossless; later rejection does not remove the row.

```text
source_finding_id
run_id
fixed_ayah_ref
finding_type
source_pointer
finding_title
claimed_branches
support_refs
reader_strength
disposition
notes
```

Allowed values:

- `finding_type`: `activated_reading`, `retrospective_surprise`;
- `reader_strength`: `asserted`, `qualified`, `exploratory`;
- `disposition`: `unreviewed`, `accepted`, `merged`, `split`,
  `evidence_only`, `deferred`, `rejected`, `conflict`.

`claimed_branches` uses `ROOT:B###`, separated by semicolons.

## `claims.tsv`

One row per normalized mechanism. Rejected mechanisms remain as rows.

```text
claim_id
ayah_ref
mechanism
cross_run_relation
publication_role
disposition
decision_reason
```

`word_id` and `morpheme_id` are deterministic foreign keys into the QAC layer.
`linguistic_support_ids` may cite supplied `sx-*` syntax edges or `co-*`
root-cooccurrence rows. It is empty when no such feature materially supports the
claim-specific judgment.

Allowed values:

- `cross_run_relation`: `shared_mechanism`, `standard_only`,
  `eleven_ayah_only`, `compatible_refinement`, `material_conflict`;
- `publication_role`: `unreviewed`, `primary`, `secondary`, `exploratory`,
  `evidence_only`, `none`;
- `disposition`: `unreviewed`, `accepted`, `merged`, `split`,
  `evidence_only`, `deferred`, `rejected`, `conflict`.

Rules:

- `rejected` claims use `publication_role=none`;
- `accepted` claims must use a non-`none`, non-`unreviewed` publication role;
- multiple primary and multiple secondary claims per ayah are allowed;
- primary claims require at least one fixed-ayah `direct` or
  `contextually_activated` lexical anchor.

## `claim_sources.tsv`

Many-to-many lineage between normalized claims and source findings.

```text
claim_id
source_finding_id
source_relation
notes
```

`source_relation`: `supports`, `refines`, `reinforces`, `split_component`,
`counterevidence`, `rejected_basis`.

Every claim, including a rejected claim, requires at least one source link.

## `branch_evidence.tsv`

One row per claim-specific branch occurrence. This is where lexical status and
resonance strength are adjudicated.

```text
evidence_id
claim_id
occurrence_ref
word_index
word_id
morpheme_id
surface
lemma
pos
root
branch
inventory_pointer
inventory_match
form_fit
construction_fit
evidence_role
lexical_status
translation_role
resonance_eligible
trigger_score
proximity_score
structure_score
reading_gain_score
robustness_score
resonance_score
resonance_strength
support_refs
linguistic_support_ids
counterevidence
decision_reason
```

Allowed values:

- `inventory_match`: `yes`, `no`, `unknown`;
- `form_fit`, `construction_fit`: `exact`, `compatible`, `mismatch`, `unknown`;
- `evidence_role`: `lexical_anchor`, `context_support`,
  `target_root_resonance`, `counterevidence`;
- `lexical_status`: `direct`, `contextually_activated`,
  `analogical_resonance`, `unlicensed`;
- `translation_role`: `governing`, `modifier`, `none`;
- `resonance_eligible`: `yes`, `no`, `not_applicable`;
- `resonance_strength`: `strong`, `moderate`, `weak`, `none`.

Lexical rules:

- `direct`: ordinary form/construction realization;
- `contextually_activated`: licensed nuance made live by context;
- `analogical_resonance`: the accepted root image materially changes the
  commentary mechanism but does not govern this form's ordinary sense;
- `unlicensed`: fails inventory, anchoring, morphology/construction, or
  mechanism support. The row remains retained.

Translation rules:

- `governing` is available only to `direct` evidence;
- `modifier` is available only to `direct` or `contextually_activated`
  evidence;
- `analogical_resonance` and `unlicensed` always use `none`.

### Resonance grading

Only `analogical_resonance` receives component scores. Score every dimension
from 0–2:

- `trigger_score`: thematic association / clear cue / exact activating cue;
- `proximity_score`: distant / local / adjacent or same construction;
- `structure_score`: loose association / coherent link / explicit sequence,
  syntax, repetition, or contrast;
- `reading_gain_score`: decorative / useful nuance / material reading change;
- `robustness_score`: fragile / plausible with limits / survives alternatives
  and counterevidence.

`resonance_score` is the sum:

- 8–10: `strong`;
- 5–7: `moderate`;
- 0–4: `weak`.

Direct and contextually activated rows use blank component scores,
`resonance_eligible=not_applicable`, and `resonance_strength=none`.

Failed resonance gates use `lexical_status=unlicensed`,
`resonance_eligible=no`, blank scores, `resonance_strength=none`, and a required
reason. A failed gate is not disguised as a weak score.

Cross-run agreement is never a component score. The orchestrator, not the
worker, computes both `resonance_score` and `resonance_strength`.

### Retaining failed evidence and claims

An `unlicensed` row is complete only when it preserves:

- the attempted occurrence/root/branch identification;
- inventory, form, and construction results;
- `resonance_eligible=no` with blank component scores;
- `translation_role=none`;
- explicit counterevidence and a decision reason;
- its claim and source-finding lineage.

An accepted claim may retain an unlicensed branch beside stronger evidence; the
failed branch simply contributes nothing to lexical or translation selection.
If the proposed mechanism has no surviving licensed or eligible resonance
support, retain the mechanism with `disposition=rejected` and
`publication_role=none`. Its `claim_sources.tsv` link normally uses
`rejected_basis`, and its coverage visibility is `none`.

These are terminal, queryable classifications. Neither row may be removed in a
cleanup or handoff stage.

## Deterministic linguistic layer

`linguistic/` is a reproducible cache generated before grading. It is not agent
judgment and does not replace the semantic ledger.

- `words.tsv`: every orthographic word, with analysis ref, QAC ref, root/POS,
  aspect, mood, voice, measure, and raw morphology summary;
- `morphemes.tsv`: every QAC segment, including prefixes, stems, and suffixes,
  plus raw features and parsed person/gender/number/case when available;
- `attachment_units.tsv`: one row per attachment unit observed in an edge,
  cross-walked to its QAC word/morpheme by normalized surface, root, sequence,
  and clitic information;
- `syntax_edges.tsv`: attachment relations with resolved word and morpheme
  endpoints, original status/confidence, and source pointer;
- `root_cooccurrences.tsv`: local root-pair rows with corpus counts. These are
  descriptive co-occurrences, not semantic collocation judgments;
- `manifest.json`: resource paths, hashes, mappings, counts, and unresolved
  warnings. Production requires zero unresolved warnings for the active scope.

Attachment/QAC index equality is never assumed. `position_crosswalk` records a
directly reconstructed match; `surface_root_sequence_fallback` records a safe
cross-tokenizer recovery. Syntax edges distinguish exact morpheme alignment,
word-only alignment, fallback alignment, and `unresolved`. Word-only alignment
is retained as a caution; `unresolved` is a blocking warning.

The packet's synthetic Basmala ref remains `1:0`; its QAC source ref is `1:1`.
Standalone Qur'anic pause and ornament symbols in packet display text are not
counted as orthographic words.
Unrooted words and morphemes remain in this layer but receive no dummy branch
evidence.

`primary`, `secondary`, and `exploratory` belong to claims. A per-word dossier
joins claim roles through `branch_evidence`; it must never store those roles as
intrinsic properties of a branch.

## `coverage.tsv`

Derived review ledger with one row per source finding.

```text
source_finding_id
claim_ids
disposition
publication_roles
translation_visibility
notes
```

`translation_visibility`: `commentary_and_translation`, `commentary_only`,
`evidence_only`, `none`.

Rejected and unlicensed material must still resolve through coverage.

## `stage_status.tsv`

Resumable orchestration state.

```text
stage_id
scope_ref
stage
status
attempt
prompt_path
prompt_sha256
prompt_revision
input_fingerprint
output_fingerprint
started_at
completed_at
error_summary
notes
```

- `stage`: `provenance`, `extract`, `normalize`, `grade`, `publish`, plus
  exception/optional states `reconcile`, `audit`, and `handoff`;
- `status`: `pending`, `running`, `complete`, `failed`.

`prompt_revision` records a git revision containing the exact prompt hash when
available. This lets historical stages remain verifiable after prompt changes.

The root orchestrator is the sole canonical writer for a surah workspace.
Workers return JSON only; separate surah workspaces may run independently.
