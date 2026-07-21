# v12 Cross-Run Agent Orchestration Specification

Use this specification when a fresh orchestrator continues or starts v12
cross-run production. The orchestrator follows this document directly, runs
deterministic helper scripts, and spawns fresh stage workers. No Python program
owns the workflow or invokes the workers.

## 1. Objective

Integrate the standard v12 reader and the eleven-ayah/±5 reader into one
ayah-level ledger while keeping these decisions independent:

1. lexical status;
2. resonance strength;
3. publication role;
4. translation role;
5. retained disposition.

All findings remain stored, including unlicensed evidence and rejected claims.
Multiple primary and multiple secondary claims are allowed for one ayah.

## 2. Authority Boundary

The root orchestrator owns:

- scope selection and stage order;
- worker creation and task assignment;
- the only writes to canonical TSVs;
- one repair attempt for malformed worker output;
- stage status and concise progress reporting.

Stage workers own only the reasoning requested by their assigned prompt. They
must not edit canonical TSVs, choose the next stage, inspect unrelated analyses,
or spawn their own adjudication chain.

Scripts are deterministic utilities only. They may discover and hash inputs,
parse source blocks, build task payloads, validate JSON shape, enrich packet
facts, calculate score totals, and write TSV rows atomically. A script must not:

- invoke a model or agent;
- select publication or lexical decisions;
- sequence the workflow;
- retry a task;
- run the whole corpus.

## 3. Evidence Boundary

Production workers may use only:

- the regular v12 run whose packet actually contains only the focus ayah plus
  up to two ayat on each side;
- the wide v12 run whose packet actually contains only the focus ayah plus up
  to five ayat on each side;
- the assigned accepted-clean packet and branch inventory;
- canonical rows and exact source lines supplied for their scope;
- the schema and their stage prompt.

Window boundaries are clipped at surah boundaries. Each treatment is a fresh,
focus-specific run with a frozen prompt, packet, output, focus ref, and
visible-ref list. Visibility must be enforced by the packet. A whole-surah
packet paired with a prompt that merely describes ±2 or ±5 is a control run,
not a production window treatment.

Do not use translations, tafsir, web sources, compact synthesis files, older
project versions, or another worker's unpublished reasoning.

Historical calibration may retain a missing ±5 manifest with
`provenance_status=reconstructed_unverified`; do not treat that limitation as
evidence against an individual finding. Production must not start a paired
scope unless both focus-specific manifests and reader outputs exist. If either
reader output is absent, leave the paired integration pending unless the user
explicitly permits a single-run treatment.

## 4. Canonical and Temporary State

The independently writable unit is one surah workspace:

```text
_status/v12_cross_run/s###/
```

Canonical semantic state consists only of:

```text
runs.tsv
source_findings.tsv
claims.tsv
claim_sources.tsv
branch_evidence.tsv
coverage.tsv
stage_status.tsv
decisions.md
```

The orchestrator may create disposable task artifacts under:

```text
s###/automation/tasks/<stage>/<task_id>.json
s###/automation/results/<stage>/<task_id>.json
```

Worker result files are not canonical. The normalized TSVs remain the source of
truth; a database or prose view is derived later.

Before grading, build the deterministic linguistic cache under
`s###/linguistic/` with `scripts/build_linguistic_bindings.py`. It contains QAC
word/morpheme bindings, attachment units and syntax edges, and descriptive
root-cooccurrence counts. The cache is reproducible from hashed resources; it
does not contain agent classifications.

Attachment IDs are never joined directly to QAC word indices. The binder
cross-walks observed attachment positions through normalized surface, root,
sequence, and clitic evidence, preserving both identifier systems. Safe
fallbacks remain labeled; any unresolved endpoint is written to the manifest
and blocks grading for that scope.

Only one orchestrator may write a surah workspace at a time. Workers may reason
in parallel because they do not write canonical data. Canonical commits to one
surah are serialized.

## 5. Unit of Reasoning and Stage Graph

The normal reasoning unit is one ayah. The required graph is:

```text
bootstrap + linguistic binding (deterministic, once per surah)
  -> extract (fresh worker per ayah)
  -> normalize (fresh worker per ayah)
  -> grade (fresh worker per ayah or disjoint claim partition)
  -> publish (fresh worker per ayah)
  -> close (deterministic minimal checks)
```

There is no corpus-wide barrier. As soon as one ayah has its extraction result,
it may advance while workers process other ayahs.

Reconciliation is an exception path, not a routine stage. Spawn a targeted
worker with `prompts/04_reconcile_after_grading.md` only when grading reveals a
material conflict, a non-atomic claim, or a necessary split/merge. Re-grade any
new or materially changed claim before publication.

Audit and handoff are optional maintenance operations. Do not run an audit
agent, strict audit loop, or derived-view build during normal production unless
the user explicitly requests it.

### Deterministic helper map

`scripts/stage_operations.py` is an importable function library and deliberately
has no `main` or run-all command. The orchestrator calls only the function for
the current explicit task:

| Need | Function |
|---|---|
| initialize provenance and source blocks | `initialize_workspace` |
| build QAC/attachment/co-occurrence bindings | `scripts/build_linguistic_bindings.py` |
| build/commit extraction | `extraction_payload` / `apply_extraction` |
| build/commit normalization | `normalization_payload` / `apply_normalization` |
| build/commit grading | `grading_payload` / `apply_grading` |
| targeted exception decision | `reconciliation_payload` / `apply_reconciliation` |
| build/commit publication | `publication_payload` / `apply_publication` |

`scripts/workflow_common.py` provides packet lookup, atomic TSV I/O, hashes,
and stage-state helpers. Neither module may spawn a worker or decide what runs
next.

## 6. Worker Task Envelope

Before spawning a worker, the orchestrator creates a task envelope containing:

```json
{
  "task_id": "s001-1_6-grade-001",
  "stage": "grade",
  "scope_ref": "1:6",
  "workspace": "_status/v12_cross_run/s001",
  "prompt_path": "_status/v12_cross_run/prompts/03_grade_lexical_resonance.md",
  "result_schema_path": "_status/v12_cross_run/model_schemas/grade.json",
  "result_path": "_status/v12_cross_run/s001/automation/results/grade/s001-1_6-grade-001.json",
  "input_paths": [],
  "expected_ids": [],
  "payload": {}
}
```

The actual `payload` is stage-specific. Include the smallest complete evidence
slice; do not make the worker search the repository for missing context.

Use this spawn instruction, followed by the exact task path:

```text
You are a fresh v12 cross-run stage worker.

Read the assigned stage prompt and result schema completely. Use only the task
envelope and the local evidence paths it names. Do not inspect unrelated project
analysis. Do not edit canonical TSVs. Preserve unlicensed, rejected, deferred,
and conflicting material. Write one JSON object conforming exactly to the
result schema at result_path, then report only completion or a concrete blocker.
```

Use a fresh worker for each stage. Do not ask the extraction worker to grade its
own findings or the grader to assign publication roles.

## 7. Stage Instructions

### 7.1 Bootstrap

The orchestrator runs deterministic source discovery and parsing once per
surah:

1. resolve the focus-specific ±2 output from its frozen manifest and verify its
   visible refs;
2. resolve the focus-specific ±5 output from its frozen manifest and verify its
   visible refs;
3. record paths and hashes in `runs.tsv`;
4. parse reader outputs into stable source blocks;
5. initialize missing TSVs from `schema/templates/`;
6. build the linguistic cache and require zero unresolved binding warnings;
7. run structural validation once.

Bootstrap performs no interpretive classification.

### 7.2 Extract

Prompt: `prompts/01_extract_source_findings.md`
Schema: `model_schemas/extract.json`

Spawn one worker per ayah. Give it all activated-reading and retrospective
blocks from both available runs, each retaining its stable `run_id` and source
pointer. The worker must account for every supplied block and split bundled
mechanisms atomically without clustering across runs.

After the worker returns, the orchestrator commits the results to
`source_findings.tsv` in source order. Do not cluster, reject, or grade during
extraction.

### 7.3 Normalize

Prompt: `prompts/02_normalize_mechanisms.md`
Schema: `model_schemas/normalize.json`

Spawn one fresh worker for the ayah with findings from both runs. It clusters by
mechanism rather than wording and returns provisional claims plus complete
source lineage.

Cross-run silence is neutral. Agreement is stability information, not an
independent confidence point. One-run findings remain present.

The orchestrator assigns stable claim IDs and commits `claims.tsv`,
`claim_sources.tsv`, and finding merge/split dispositions atomically.

### 7.4 Grade

Prompt: `prompts/03_grade_lexical_resonance.md`
Schema: `model_schemas/grade.json`

Give the worker the provisional claims, their source lines, exact packet
occurrences, relevant accepted-clean inventory branches, and the mechanically
bound QAC/attachment slice. For a long ayah,
the orchestrator may partition by disjoint claim IDs; no claim may be graded by
two workers in the same attempt.

Keep that slice lean: provide full inventories for roots occurring in the
focus ayah (so the worker can establish the direct lexical floor), but only the
explicitly cited branch records for roots that occur solely in support ayahs.
Include linguistic rows only for the focus and cited support refs.

The worker classifies every cited or necessary branch as:

- `direct`;
- `contextually_activated`;
- `analogical_resonance`;
- `unlicensed`.

Eligible analogical resonance receives five 0–2 component scores. The script,
not the worker, calculates the total and strength bucket:

- 8–10: `strong`;
- 5–7: `moderate`;
- 0–4: `weak`.

A failed eligibility gate becomes retained `unlicensed` evidence with no
score. Cross-run agreement contributes zero points. Analogical and unlicensed
evidence always receives `translation_role=none`.

The orchestrator enriches deterministic packet fields and commits all evidence
rows atomically. It also supplies `word_id`/`morpheme_id`, calculates score and
strength, and validates cited linguistic feature IDs. Workers interpret the
relevance of supplied morphology/syntax; they never bind QAC tokens or compute
collocations. Missing, mismatched, and failed branches remain in the ledger.

### 7.5 Publish

Prompt: `prompts/05_assign_publication_roles.md`
Schema: `model_schemas/publish.json`

Spawn one fresh worker for the ayah after grading is complete. It assigns one
terminal disposition and publication role to every claim.

Publication role is independent of lexical status. A strong analogical
resonance may materially support a primary mechanism, but it cannot become a
translation sense or serve as the sole lexical anchor of a primary claim.

More than one `primary` and more than one `secondary` are allowed. Claims not
promoted remain queryable as `exploratory`, `evidence_only`, `deferred`,
`conflict`, or `rejected`/`none` as warranted.

The orchestrator commits claim decisions and derives `coverage.tsv`
deterministically.

## 8. Commit Protocol

For each worker result, the orchestrator performs only these checks:

1. the JSON matches the named result schema;
2. returned IDs equal the assigned IDs or blocks—none missing or extra;
3. referenced source, claim, occurrence, and branch IDs resolve;
4. resonance arithmetic and bucket mapping are correct;
5. analogical/unlicensed evidence has no translation access;
6. a published primary claim has a fixed-ayah `direct` or
   `contextually_activated` anchor.

If these pass, write the affected TSVs atomically and mark the stage complete.
Do not require a second opinion, prose audit, cross-run agreement, or strict
workspace audit.

If the result is malformed, send the concrete validation errors back to that
worker once. If the repair still fails, mark only that task failed and continue
unrelated ayahs. Do not silently repair a worker's interpretive decision in a
script.

Run the normal structural validator after a stage commit:

```bash
python3 _status/v12_cross_run/scripts/validate_workspace.py \
  _status/v12_cross_run/s001 --scope 1:6
```

`--strict` is optional and is not a production gate.

## 9. Parallelism and Resume

- Parallelize workers across disjoint ayahs.
- Never run two workers that will decide the same claim in one attempt.
- Do not let workers write shared TSVs.
- Serialize commits within each surah workspace.
- Respect the dependency graph per ayah; do not wait for the entire surah.
- Resume from the first incomplete stage in `stage_status.tsv`.
- A completed stage is reused unless one of its canonical inputs changed.
- When an input changed, append a new attempt; never overwrite stage history.

## 10. Non-Loss and Translation Invariants

- No evidential outcome authorizes deletion.
- `unlicensed` means not lexically available, not discarded.
- `rejected` means not promoted, not discarded.
- Merged and split predecessors retain source lineage.
- Every source finding reaches at least one claim or an explicit retained
  terminal outcome.
- Every cited branch receives an evidence row, including failed branches.
- Only `direct` may govern translation.
- Only `direct` or `contextually_activated` may modify translation.
- Analogical resonance may enter commentary but never translation.

## 11. Completion Definition

An ayah is complete when:

- every source block from both assigned runs is accounted for;
- every finding has claim lineage;
- every cited branch is retained and classified;
- all eligible resonance scores are arithmetically closed;
- every claim has a terminal publication decision;
- coverage is derived;
- the six commit checks pass.

A surah is complete when every assigned ayah is complete or explicitly marked
blocked with a concrete missing input. No separate audit stage is required.

The user-facing structure is a derived join, not another hand-edited ledger:

```text
ayah
  words/morphemes -> QAC morphology + attachment links
  branch uses -> evidence ID + lexical/translation status + claim ID/role
  claims -> mechanism + publication role + source lineage
```

Publication role remains claim-specific. Never flatten it into an intrinsic
`word -> primary branch` label.

## 12. Resume and Production Checkpoint

Read [STATUS.md](STATUS.md) for the exact live task IDs, completed S1 scopes,
remaining stages, source-window limitation, and corpus-production gates. Do not
copy a stale next-ayah instruction from this specification; resume from
`stage_status.tsv` and the exact task envelope named there.
