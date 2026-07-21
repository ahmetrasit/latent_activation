# v12 Cross-Run Production Status

Checkpoint: 2026-07-21

Read this file first when resuming. Then read
[ORCHESTRATION.md](ORCHESTRATION.md) and inspect the target surah's
`stage_status.tsv`. The orchestration specification is normative; this file is
the disposable operational checkpoint.

## Readiness Decision

The integration machinery is ready for a controlled pilot. It is **not yet
ready for corpus-wide production**.

Two gates remain:

1. finish S1 through publication and close it with zero structural errors;
2. create and freeze genuinely focus-constrained source runs for the two
   treatments used in production.

Do not begin unattended corpus production merely because the schema and stage
workers exist.

## Production Source Treatments

For every focus ayah, production must compare two independent, focus-specific
reader runs:

| Treatment | Material actually visible to reader |
|---|---|
| regular v12 | focus ayah, up to 2 preceding, and up to 2 following ayat |
| wide v12 | focus ayah, up to 5 preceding, and up to 5 following ayat |

Both windows are clipped at surah boundaries. The packet—not only the prose
prompt—must enforce the visibility boundary. Each treatment needs its own
packet hash, output hash, prompt hash, focus ref, and visible-ref list. The
integration worker still reasons about one focus ayah at a time.

The existing `v12/runs/s###/full_context_packet.json` files are whole-surah
control packets. Existing `v12/runs_11ayah/` outputs do not by themselves prove
that the reader was blind outside a focus-specific ±5 window. They are useful
discovery/control material, but are not substitutes for constrained production
inputs.

S1 used the same seven-ayah whole-surah packet for both readers. Therefore S1
tests extraction, normalization, grading, publication, retention, morphology,
and attachment alignment, but it must not be presented as a clean
five-versus-eleven-ayah window comparison. A production S1 result requires
focus-specific reruns too.

Upstream source work still required:

- define a stable per-focus directory and manifest convention for ±2 and ±5;
- build the two actual window packets for each focus;
- use fresh readers restricted to the assigned packet and focus output;
- freeze every prompt/packet/output triple;
- extend source discovery to select these manifests instead of silently
  selecting a whole-surah control.

## Completed Machinery

- normative agent orchestration, prompts, and JSON result contracts;
- canonical non-loss TSV schema with independent lexical, resonance,
  publication, translation, and disposition axes;
- deterministic QAC word/morpheme binding and attachment crosswalk;
- deterministic task construction and atomic result application;
- derived word/claim views for downstream commentary and translation;
- S1 extraction: 80 retained findings across all seven assigned scopes;
- complete 1:6 calibration: 7 claims, 18 source links, 40 branch-evidence rows,
  and 13 coverage rows;
- linguistic binder protocol v2 rebuilt for S1 with 29 words, 48 morphemes,
  30 attachment units, 23 syntax edges, 28 root-cooccurrence rows, and zero
  unresolved warnings.

The binder was also stress-tested transiently against S18: 1,583 words, 2,582
morphemes, 1,525 observed attachment units, 1,258 syntax edges, 5,950
root-cooccurrence rows, and zero unresolved endpoints. Three contracted forms
resolved at word rather than morpheme level; they remain visibly labeled, not
discarded. This was a binder test only and was not persisted as a canonical S18
cross-run workspace.

## S1 Checkpoint

| Scope | Extract | Normalize | Grade | Publish |
|---|---|---|---|---|
| 1:0 | complete | complete | complete | pending |
| 1:2 | complete | complete | complete | pending |
| 1:3 | complete | task prepared | pending | pending |
| 1:4 | complete | task prepared | pending | pending |
| 1:5 | complete | complete | complete | pending |
| 1:6 | complete | complete | complete | complete |
| 1:7 | complete | task prepared | pending | pending |

The two completed grading repairs enforced core invariants only: support-ayah evidence
cannot enter translation, and a `direct` classification cannot retain a failed
construction gate. Use one repair attempt, as specified; do not add an audit
agent.

Current canonical totals are 80 findings, 20 claims, 54 claim-source links, 113
branch-evidence rows, and 13 terminal coverage rows. Normal structural
validation reports zero errors. Its five warnings are expected provenance
notices for historically frozen prompt content. No stage is currently marked
`running`.

Durable task identities at this checkpoint:

| Scope | Stage/task | Stage ID | Result |
|---|---|---|---|
| 1:0 | `s001-1_0-grade-001` | `st-s001-1_0-grade-001` | committed after one invariant repair |
| 1:2 | `s001-1_2-grade-002` | `st-s001-1_2-grade-002` | committed |
| 1:5 | `s001-1_5-grade-001` | `st-s001-1_5-grade-001` | committed after one invariant repair |

Prepared but unstarted normalization envelopes:

- `automation/tasks/normalize/s001-1_3-normalize-001.json`
- `automation/tasks/normalize/s001-1_4-normalize-001.json`
- `automation/tasks/normalize/s001-1_7-normalize-001.json`

## Resume Procedure

1. Read `s001/stage_status.tsv`; never infer durable state from an old chat or
   agent name.
2. For a `running` row, inspect the exact task envelope and its named
   `result_path`.
3. If a valid repaired result exists, call `apply_task_result(task_path)` and
   then `end_stage(...)` for that exact stage ID.
4. If no result exists and no worker is alive, mark that attempt failed with a
   concrete note, create the next numbered task, and spawn one fresh worker.
5. After grading, create a fresh publication task for that ayah. Do not let the
   grader publish its own claims.
6. The immediate next tasks are publication for 1:0, 1:2, and 1:5, plus
   normalization for 1:3, 1:4, and 1:7.
7. Continue 1:3, 1:4, and 1:7 through normalize → grade → publish. Canonical
   commits within S1 stay serialized even when workers reason in parallel.
8. Rebuild derived word views only after the semantic rows are terminal.

Example deterministic close commands:

```bash
python3 _status/v12_cross_run/scripts/build_linguistic_bindings.py \
  _status/v12_cross_run/s001

python3 _status/v12_cross_run/scripts/validate_workspace.py \
  _status/v12_cross_run/s001

python3 _status/v12_cross_run/scripts/build_word_claim_views.py \
  _status/v12_cross_run/s001
```

Normal structural validation is the production gate. Strict validation and a
separate audit agent are not required.

## Gate for Corpus Production

Corpus production may start only when:

- the source resolver accepts only frozen, actual ±2 and ±5 focus packets;
- every S1 scope has terminal publication decisions;
- S1 has zero unresolved linguistic warnings and zero structural errors;
- a fresh paired-window pilot demonstrates the revised source layer end to end.

After those gates, process surah by surah and ayah by ayah. A large surah does
not go to one integration agent: only deterministic bootstrap is surah-wide;
interpretive workers receive one compact ayah task.
