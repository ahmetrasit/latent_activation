# GSLS V3

GSLS V3 is a prompt-led workflow for whole-passage latent lexical discovery and Turkish synthesis. It is designed to recover interacting root-branch channels, axes, images, and retrospective activations without reducing the passage to verse, pericope, or section summaries.

For a cold run, follow `00_orchestration_spec.md` from **Cold-start contract** through **Agent runbook**. It contains the complete preparation, native multi-agent session, interruption, and post-publication benchmark sequence.

## Intellectual flow

```text
prepared evidence
  -> A1 discovery
  -> A1 scaffold integration
  -> A2 mechanism map
  -> fresh gold renderer
```

A1 uses one continuing agent session for its two turns. A fresh A2 agent creates the mechanism map in one turn. A third, context-free agent renders the completed work into audio-first Turkish publication JSONL. The renderer is a presentation author, not a reviewer or validator, and it does not reopen discovery or grading.

For gold-workflow runs, use `gpt-5.6-sol` at maximum reasoning depth for all three agents.

## Prepare a run

```bash
python3 v3/scripts/prepare_run.py \
  --run-root v3/run/s1-pilot \
  --surah 1 \
  --ayah-start 1 \
  --ayah-end 7 \
  --primary-scaffold /absolute/path/to/primary-scaffold.md
```

The script reads the local Quran, QAC, attachment, and V4 resources. V4 selection is restricted to accepted rows with `contaminated = 'no'`. The prepared lexical file contains exactly six fields.

## Emit tasks

```bash
python3 v3/scripts/make_tasks.py v3/run/s1-pilot
```

Run the emitted tasks in order:

1. `tasks/01-a1-discover.md` in a fresh A1 session.
2. `tasks/02-a1-integrate.md` in the same A1 session.
3. `tasks/03-a2-map.md` in a fresh A2 session.
4. `tasks/04-a2-publish.md` in a fresh, context-free gold renderer session.

Turn 4 writes canonical `<surah>-publication.jsonl` in the run root, using the numeric surah from the prepared passage, for example `1-publication.jsonl`.

Validate it and generate the prose-only Markdown derivative:

```bash
python3 v3/scripts/render_publication.py \
  v3/run/s1-pilot/1-publication.jsonl
```

The resulting `1-publication.md` is deterministic. Each finding remains a separate JSONL record with grading, a spoken title, and one to three prose paragraphs.

For an existing run that already has `a1/discovery-integrated.md` and `a2/mechanism-map.md`, rerun `make_tasks.py` and execute only task 04 with a fresh renderer. The new task writes `<surah>-publication.jsonl`; render it only after validation succeeds. The earlier agents do not need to run again unless their artifacts change.

## S1 audio-renderer pilots

The run `v3/run/s001-full-20260716/` contains an isolated comparison of two
audio-first Stage 4 designs. These files are evaluation artifacts, not a change
to the canonical orchestration described above.

### Archived pilot v1

The first audio-oriented result is preserved as:

```text
1-publication-pilot-v1.jsonl
1-publication-pilot-v1.md
```

It produced 16 synthesized findings. It restored the compact renderer's
hierarchy after an earlier atomized 47-finding attempt, but recurring lexical
carrier language remained too audible for sustained TTS listening.

### Revised single-pass renderer

The current single-pass prompt, `prompts/a2-publication-tr-audio-first.md`,
produced:

```text
1-publication.jsonl
1-publication.md
```

The result contains 15 findings. It passed the deterministic contract check,
used only exact Arabic surface substrings from the supplied passage, and spoke
no bare roots. It substantially reduced lexical bookkeeping in the prose, but
still compressed some synthesis details and developed a repeated explanatory
carrier of its own.

### Frozen-synthesis two-pass pilot

The alternative pilot separates synthesis from rendering while keeping both
turns in the same third-agent session:

```text
prompts/a2-publication-tr-compact-v2.md
  -> 1-synthesis-master-pilot-v2.md
  -> prompts/a2-publication-tr-audio-followup.md
  -> 1-publication-two-pass-pilot-v2.jsonl
  -> 1-publication-two-pass-pilot-v2.md
```

The pilot tasks are:

```text
tasks/04a-a2-synthesis-master-pilot-v2.md
tasks/04b-a2-audio-followup-pilot-v2.md
```

The unchanged compact production prompt first wrote a frozen synthesis master.
The renderer-only follow-up then treated every grade-bearing master unit as
exactly one JSONL finding, without merging, splitting, reordering, or
rescoring. It produced 19 findings, matching the master's nine governing and
ten complementary units, and passed the deterministic contract check.

This experiment supports the two-pass architecture for synthesis preservation.
The written master, rather than conversational memory, must remain the
auditable source of truth for the follow-up. The follow-up prose still needs a
further canary for repeated Arabic-gloss phrasing and strict use of the primary
scaffold's Quranic names and titles.

Neither pilot can restore discoveries already absent from
`a2/mechanism-map.md`. Comparison with `s1-bulgular-tr.md` found that the
governing synthesis was retained, while several reference details had been
lost upstream or reduced before publication rendering.

The canonical task generator and orchestration specification remain
single-pass. Promote the two-pass design only after the follow-up prompt passes
fresh S1 and S112 canaries and the production task generator, runbook, and
batch-production gate are updated together.

## Deliberate omissions

V3 has no state machine, review agent, hashes, provenance ledger, branch-coverage report, or failed-seed record. Its small publication schema validates presentation shape only; it does not adjudicate findings. Its final renderer is a production writing turn, not a control layer. Preparation, task emission, validation, and Markdown rendering do not call a model provider.

See `00_orchestration_spec.md` and `00_input_supply_guide.md` for the complete workflow.
