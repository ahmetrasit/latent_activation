# GSLS V3 Orchestration Specification

## Objective

Produce a gold-level Turkish synthesis in which accepted Arabic root branches form passage-specific coalitions, governing channels, spatial or sensory axes, transformations, rings, and retrospective activations. The synthesis must explain why the passage uses these words, in this order, and why it closes where it does while preserving its direct contextual meaning.

This is open-ended linguistic discovery. The prompts guide attention and composition; they are not compliance checklists.

## Cold-start contract

Run from the repository root with a unique run directory under `v3/run/`. Before starting, supply an independent primary scaffold for the exact passage scope. The scaffold states the passage's direct contextual proposition; it must not be copied from a gold reference or prior synthesis.

Production uses two native multi-agent sessions with `gpt-5.6-sol` at maximum reasoning depth. Use the environment's native spawn, send, wait, and close operations, and set `fork_context: false` for both spawns so neither agent inherits conversation history. Do not use `codex exec` to emulate an agent, and do not let either production agent spawn further agents.

The local source files are:

```text
resources/quran/surah_<surah>.json  Arabic passage
resources/qac.sqlite                positioned morphology and syntax
resources/attachments.tsv           syntax relation labels
resources/furuq_v4.sqlite            lexical branches
```

Preparation requires no model call. It emits only the evidence used by the four production turns.

## Whole-passage rule

The workflow moves in this direction:

```text
local lexical discoveries
  -> cross-root coalitions
  -> governing channels and interacting axes
  -> whole-passage activation field
  -> Turkish synthesis
```

It must never move from pericope summaries to a stitched passage summary. Ayah or pericope boundaries may reveal a transition, contrast, delay, return, or closure, but they are not independent composition containers. Local findings may remain visible at medium or weak confidence without becoming section commentary.

## Evidence

Prepared inputs are:

```text
inputs/passage-arabic.txt
inputs/morphology.tsv
inputs/syntax.tsv
inputs/lexical-branches.jsonl
inputs/primary-scaffold.md
```

The lexical records contain exactly `root_id`, `root_norm`, `branch_id`, `what_is_ar`, `branch_image_ar`, and `source_phrase_ar`. Preparation reads `resources/furuq_v4.sqlite` and emits only accepted branches whose contamination value is exactly `no`.

The gold reference, prior outputs, translations, the `v1/` tree, and model memory are not production evidence.

## Prepare a run

Choose the surah, inclusive ayah range, scaffold, and a new run id:

```bash
python3 v3/scripts/prepare_run.py \
  --run-root v3/run/<run-id> \
  --surah <surah> \
  --ayah-start <first-ayah> \
  --ayah-end <last-ayah> \
  --primary-scaffold /absolute/path/to/primary-scaffold.md

python3 v3/scripts/make_tasks.py v3/run/<run-id>
```

Use `--include-opening-context` only when the selected scope deliberately includes the Quran resource's opening context. Do not change passage scope between turns. `prepare_run.py` creates the input and output directories; `make_tasks.py` binds each prompt to the run's evidence and assigned output path.

The resulting production artifacts are:

| Turn | Session | Task | Output |
| --- | --- | --- | --- |
| 1 | fresh A1 | `tasks/01-a1-discover.md` | `a1/discovery.md` |
| 2 | same A1 | `tasks/02-a1-integrate.md` | `a1/discovery-integrated.md` |
| 3 | fresh A2 | `tasks/03-a2-map.md` | `a2/mechanism-map.md` |
| 4 | same A2 | `tasks/04-a2-publish.md` | `publication.md` |

All paths in this table are relative to `v3/run/<run-id>/`.

## Agent runbook

1. Spawn a fresh, context-free A1 agent for `tasks/01-a1-discover.md`. Tell it to read and execute that task, write only its assigned output, and not spawn subagents. Wait until it reports completion; do not steer it while it is reasoning.
2. Send `tasks/02-a1-integrate.md` to that same A1 session. Wait for completion, then close A1. Session continuity is required because this turn integrates rather than rediscovers A1's field.
3. Spawn a fresh, context-free A2 agent for `tasks/03-a2-map.md`. Give it no conversation history or unlisted material. Wait until it reports completion without intermediate feedback.
4. Send `tasks/04-a2-publish.md` to that same A2 session. Wait for completion, then close A2. Session continuity is required because the publication must realize the mechanism map rather than independently summarize the passage.

Do not inspect against gold, rank findings, request revisions, or inject operator commentary between these turns. Maximum-depth turns can be long; a quiet interval is not a failure.

If a wait call times out or the operator interface is interrupted, first wait on the existing agent id again. Do not resend the task or spawn a duplicate while that agent may still be running. If an agent actually fails before writing its assigned artifact, restart only the incomplete turn while preserving the required A1 or A2 session continuity whenever the session remains available.

## Flow

### Turn 1: A1 discovery

A fresh high-depth agent reads the passage, positioned morphology, local syntax, and complete lexical inventory. It follows the passage forward, gives every supplied branch one attentive reading, develops specific coalitions selectively, and then performs a backward replay. It writes:

```text
a1/discovery.md
```

The primary scaffold is not supplied during this turn.

### Turn 2: A1 scaffold integration

The same A1 session receives the independent direct scaffold. It preserves the discoveries, places them against the contextual proposition, and rewrites the notebook as a whole-passage discovery field:

```text
a1/discovery-integrated.md
```

The scaffold grounds contextual meaning. It does not impose a local-sense gate on secondary root resonance.

### Turn 3: A2 mechanism map

A fresh high-depth agent receives the integrated discovery, scaffold, exact passage, and prepared linguistic evidence. Before writing publication prose, it constructs the passage-scale mechanism:

```text
a2/mechanism-map.md
```

The map preserves central, medium, weak, conditional, rival, and incomplete material when each contributes a real lexical or compositional insight.

### Turn 4: A2 Turkish publication

The same A2 session turns the mechanism map into the final work:

```text
publication.md
```

The publication uses labeled finding paragraphs and a final ordered replay. It is not organized by ayah, pericope, or section.

## Confidence language

The final synthesis uses two separate dimensions:

- `GÜÇLÜ / ORTA / ZAYIF`: how explicitly the supplied lexical record supports the branch image used in the finding.
- `A / B / C / C-koşullu`: how strongly the passage activates that image or coalition.

The first dimension does not claim source chronology, independent dictionary counts, or majority derivational opinion. Those facts are not available in the six-field input.

Activation strength comes from specific cross-root convergence, complementary roles, passage order, adjacency, recurrence, and contribution to the whole. A latent scene does not become weak merely because no surface word names that scene literally. Preserving the direct contextual meaning is sufficient; surface literalization is not an activation requirement.

## Orchestration boundary

The runtime only prepares evidence and emits four task files. It does not score, approve, reject, promote, or close agent work. The operator's role is limited to preserving the two-session sequence and allowing each turn to finish.

The production run is complete when A2 has written `publication.md` and reported completion. A blind gold comparison may begin only afterward, outside both production sessions. It is an evaluation of the finished work, not a fifth workflow turn, and its findings are never retroactively supplied as production evidence.
