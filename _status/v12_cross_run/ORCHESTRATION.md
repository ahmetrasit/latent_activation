# v12 Cross-Run v3 Orchestration Specification

This is the normative cold-start workflow for publishing v12 contextual-root
findings against a fixed ordinary target-language baseline. v2 files remain
historical calibration artifacts; never run v2 package, prompt, or finalizer
commands for v3 production.

## 1. Publication contract

Every publication ayah contains:

- its immutable ordinary target-language baseline;
- one flat `findings` array containing only what contextual or retrospective
  v12 activation adds to or changes in that baseline;
- one grade per finding: `strong`, `weak`, or `reject`;
- anchors materialized as `[qac_word_ref, root_id, branch_ids]`.

Pure baseline restatements are omitted before grading. A genuine proposed delta
is retained even when graded `reject`. Lexical overlap with the baseline is not
itself grounds for omission.

The publication agent writes only semantic findings with compact anchor keys.
Deterministic finalization injects the baseline and materializes public anchors.
Generated artifacts are never hand-edited, manually minified, renamed, or
repaired. Correct the responsible prompt, profile, schema, assignment, or
script; then regenerate every hash-dependent output.

## 2. Cold-start invariants

Operate from the repository root on `main`. Do not create another branch. Do
not infer inputs or state from conversation history.

The canonical source families already exist for S001-S114:

- regular v12: `v12/runs/s###/full_context_control/`;
- ±5 v12: `v12/runs_11ayah/s###/full_context_control/`.

The target language is selected by a BCP-47 profile. Turkish uses
`_status/v12_cross_run/baseline/language_profiles/tr.json`.

All generated v3 JSON is canonical compact UTF-8: one complete object on one
line, separators `,` and `:`, no insignificant whitespace, and one trailing
newline. These files are JSON, not JSONL.

Final publications are isolated in
`_status/v12_cross_run/output/<language>/`. That directory contains publication
JSON files only. The exact filename is
`<surah>_ayah_findings_publication.json`.

## 3. Coverage authority

The project-owned ordinary baseline and canonical Quran source control
publication ayah coverage. Analytical packets and readers control only which
ayat have v12 findings.

Therefore a canonical ayah absent from both readers still appears with its
baseline and `findings: []`. S2 is the required test: its packet contains 286
analytical rows (`2:0`, `2:2` through `2:286`) and omits rootless `2:1`. Its
publication must contain 287 rows: synthetic `2:0` plus canonical `2:1` through
`2:286`.

QAC has no `N:0` IDs. A synthetic Basmalah aliases the canonical `1:1`
baseline and its `1:1:*` QAC word references. S9 has no synthetic Basmalah.
Every other canonical ayah is authored in its own surah baseline, including an
ayah with no lexical root.

## 4. Minimal agent assignments

Every semantic agent receives exactly two entry-point paths:

```text
Prompt: `PROMPT_PATH`
Input bundle: `INPUT_BUNDLE_PATH`
```

Do not copy prompt text, source excerpts, baseline rows, schemas, summaries,
grading guidance, or coordinator commentary into the task. A resume receives
the same two paths. One agent owns one complete surah; never delegate individual
ayat.

Baseline-author prompt:

```text
_status/v12_cross_run/baseline/prompts/author_baseline.md
```

Publisher prompt:

```text
_status/v12_cross_run/prompts/publish_whole_surah_v3.md
```

Anchor-repair prompt, only when exceptions exist:

```text
_status/v12_cross_run/prompts/repair_anchor_exceptions.md
```

## 5. Exact S2 cold-test runbook

### 5.1 Build the baseline-author input bundle

Run:

```bash
python3 _status/v12_cross_run/scripts/build_target_language_baseline_assignment.py \
  2 \
  --language tr \
  --arabic /Volumes/OZTURK/_projects/quran-roots/quran/complete-quran.txt \
  --qac /Volumes/OZTURK/_projects/quran-roots/_corpus/qac/qac.sqlite
```

This creates only the assignment, not the translation:

```text
_status/v12_cross_run/s002/baseline_assignment.tr.json
```

The builder fails if the supplied Arabic or QAC source differs byte-for-byte
from the project-owned downstream mirror. It hash-binds the author prompt,
methodology, language profile, Arabic source, QAC database, schema, and
validator, and declares the generated baseline output:

```text
_status/v12_cross_run/baseline/artifacts/quran-tr-baseline-v1-s002.json
```

### 5.2 Run one cold baseline author

Give the baseline author only:

```text
Prompt: `_status/v12_cross_run/baseline/prompts/author_baseline.md`
Input bundle: `_status/v12_cross_run/s002/baseline_assignment.tr.json`
```

The author may checkpoint only at the assignment's checkpoint path. The final
artifact contains exactly `language` and `ayat`; each ayah contains only
`ayah_ref`, `baseline_text`, and target tuples
`[surface, [qac_word_ref, ...]]`. It contains no notes, target-language IDs,
offsets, alignment groups, morpheme ledgers, statuses, or audit prose.

The initial assignment has `read_existing_output: false`; the author must not
read or transform a pre-existing output. To resume an interrupted author, rerun
the assignment builder with `--resume`, then give the replacement author the
same two paths.

### 5.3 Validate the S2 baseline

Run the exact `validation_command` stored in the assignment, or equivalently:

```bash
python3 _status/v12_cross_run/scripts/validate_target_language_baseline.py \
  _status/v12_cross_run/baseline/artifacts/quran-tr-baseline-v1-s002.json \
  --surah 2 \
  --qac /Volumes/OZTURK/_projects/quran-roots/_corpus/qac/qac.sqlite
```

Required result:

- 286 canonical baseline ayat;
- every Turkish token has one or more valid same-ayah QAC word references;
- the union covers every S2 QAC word with no missing or foreign ID;
- compact serialization passes.

Structural validity does not certify Turkish quality. Complete the baseline
author's Arabic/QAC fidelity and Turkish-language review before packaging.

### 5.4 Build deterministic linguistic bindings

Run:

```bash
python3 _status/v12_cross_run/scripts/build_linguistic_bindings.py \
  _status/v12_cross_run/s002 \
  --packet v12/runs/s002/full_context_packet.json
```

Do not give the linguistic cache to the publisher. It is coordinator-only and
is used during final anchor materialization. Any blocking binding warning must
be resolved mechanically before final close.

### 5.5 Build the v3 publication package

Run:

```bash
python3 _status/v12_cross_run/scripts/build_publication_package_v3.py \
  2 \
  --baseline \
    _status/v12_cross_run/baseline/artifacts/quran-tr-baseline-v1-s002.json \
  --basmalah-baseline \
    _status/v12_cross_run/baseline/artifacts/quran-tr-baseline-v1-s001-pilot.json
```

The package builder validates both baselines, binds their combined hash, checks
both complete readers against the analytical packet, adds canonical rootless
ayat from `resources/quran/complete-quran.txt`, resolves cited branches, and
writes:

```text
_status/v12_cross_run/s002/package_index.v3.json
```

The S2 package coverage must be:

```json
{"ayah_count":287,"analytical_ayah_count":286,"baseline_ayah_count":287,"standard_heading_count":286,"wide_heading_count":286}
```

Do not launch the publisher unless package `state` is `ready` or
`ready_with_anchor_exceptions` and these counts match.

### 5.6 Run one cold whole-surah publisher

Give the publisher only:

```text
Prompt: `_status/v12_cross_run/prompts/publish_whole_surah_v3.md`
Input bundle: `_status/v12_cross_run/s002/package_index.v3.json`
```

The publisher may read only `publisher_inputs` plus its same-package draft
while auditing/resuming. It must not read `coordinator_only`, v2 publications,
other surahs, tafsir, web sources, or existing Turkish Quran translations.

It writes both declared files:

```text
_status/v12_cross_run/s002/publication.v3.draft.json
_status/v12_cross_run/s002/self_audit.v3.json
```

The draft contains every roster ayah exactly once and in order. `2:1` must have
`findings: []`. The second pass reopens both readers, the saved draft, and each
baseline row; it removes baseline-only prose, restores missed activated or
retrospective deltas, preserves distinct findings, retains rejects, and binds
the stable draft hash.

### 5.7 Repair anchor exceptions only if present

If `anchor_summary.review_anchor_keys` and
`malformed_or_unattached_occurrences` are both zero, skip this step.

Otherwise collect the completed S2 exceptions:

```bash
python3 _status/v12_cross_run/scripts/collect_anchor_exceptions_v3.py --surah 2
```

Give one repair agent only:

```text
Prompt: `_status/v12_cross_run/prompts/repair_anchor_exceptions.md`
Input bundle: `_status/v12_cross_run/anchor_exceptions.json`
```

The ledger names the branch database, repair schema, and output path. A repair
may only identify an existing root/branch pair. `unresolved` blocks the affected
surah. `meaning_change` returns the affected ayah to the publisher; it is never
silently materialized.

### 5.8 Finalize mechanically

With no exceptions:

```bash
python3 _status/v12_cross_run/scripts/finalize_publication_v3.py \
  _status/v12_cross_run/s002
```

With a completed repair ledger:

```bash
python3 _status/v12_cross_run/scripts/finalize_publication_v3.py \
  _status/v12_cross_run/s002 \
  --repair-ledger _status/v12_cross_run/anchor_repair.json
```

Finalization verifies every package hash, draft/audit binding, roster row,
grade, anchor key, database branch, and fixed-ayah QAC occurrence. It injects
the baseline verbatim and writes only this publication into the clean output
space:

```text
_status/v12_cross_run/output/tr/2_ayah_findings_publication.json
```

Drafts, audits, manifests, ledgers, logs, assignments, and derived TSVs remain
outside the output directory.

### 5.9 Required S2 acceptance checks

Run:

```bash
test "$(wc -l < \
  _status/v12_cross_run/output/tr/2_ayah_findings_publication.json)" -eq 1

jq -e '
  .protocol == "v12-cross-run-publication-v3" and
  .language == "tr" and
  .surah == 2 and
  (.ayat | length) == 287 and
  ([.ayat[].ayah_ref] | length == (unique | length)) and
  ([.ayat[] | select(.ayah_ref == "2:1") | .findings] == [[]]) and
  (all(.ayat[].findings[];
    (.grade == "strong" or .grade == "weak" or .grade == "reject") and
    (.anchors | length > 0)))
' _status/v12_cross_run/output/tr/2_ayah_findings_publication.json

find _status/v12_cross_run/output/tr \
  -maxdepth 1 -mindepth 1 \
  \( ! -type f -o \
  -type f ! -name '*_ayah_findings_publication.json' \)
```

The final `find` command must print nothing. Also inspect the Turkish findings
ayah by ayah for baseline restatement, English leakage, flattened multi-claim
prose, missed retrospective activation, and grade/anchor mismatch. A mechanical
pass alone does not promote the S2 pilot to production.

## 6. Resume and invalidation

- Never resume from a draft whose package inputs or baseline hash changed.
- A baseline wording or token-map change requires baseline regeneration,
  package regeneration, publisher regeneration, audit regeneration, and final
  close.
- A publisher-prompt, language-profile, reader, roster, or anchor-map change
  requires package regeneration and a fresh publisher/audit run.
- A purely identifying anchor repair does not require semantic regeneration.
- A meaning-changing repair invalidates the affected ayah and its audit.
- Reformatting, renaming, or relocating generated files is a workflow change;
  never patch the artifact directly.

## 7. General production expansion

After S1 and S2 receive editorial approval, repeat the same baseline assignment,
validation, package, publisher, repair, and finalization sequence for every
surah. Surah baselines are independent canonical shards. Synthetic Basmalahs
always reuse the approved S1 `1:1` baseline through `--basmalah-baseline`.

Corpus production is ready only when:

- all 6,236 canonical ayat have validated ordinary target-language baselines;
- all 114 final publication files exist under the clean language directory;
- every final file is compact JSON with the required filename;
- publication coverage includes rootless ayat and the permitted synthetic
  Basmalah rows;
- every finding is a target-language baseline delta with one allowed grade;
- every public anchor resolves to a same-ayah QAC word, stable root, and one or
  more branch IDs;
- every final manifest and downstream database import reconciles file hashes,
  ayah counts, finding counts, and anchor counts.
