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

A1 uses one continuing agent session for its two turns. A fresh A2 agent creates the mechanism map in one turn. A third, context-free agent renders the completed work into compact Turkish prose. The renderer is a synthesis author, not a reviewer or validator, and it does not reopen discovery or grading.

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

The final product is `<surah>-publication.md` in the run root, using the numeric surah from the prepared passage, for example `1-publication.md`.

For an existing run that already has `a1/discovery-integrated.md` and `a2/mechanism-map.md`, rerun `make_tasks.py` and execute only task 04 with a fresh renderer. The new task writes `<surah>-publication.md` and leaves an older `publication.md` untouched. The earlier agents do not need to run again unless their artifacts change.

## Deliberate omissions

V3 has no state machine, review agent, output JSON schema, hashes, manifests, provenance ledger, branch-coverage report, failed-seed record, or generic validation stage. Its final renderer is a production writing turn, not a control layer. Preparation and task emission do not call a model provider.

See `00_orchestration_spec.md` and `00_input_supply_guide.md` for the complete workflow.
