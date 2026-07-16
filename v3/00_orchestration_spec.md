# GSLS V3 Orchestration Specification

## Objective

Produce a gold-level Turkish synthesis in which accepted Arabic root branches form passage-specific coalitions, governing channels, spatial or sensory axes, transformations, rings, and retrospective activations. The synthesis must explain why the passage uses these words, in this order, and why it closes where it does while preserving its direct contextual meaning. Its final presentation is designed first for sustained listening by a curious Turkish listener with no Arabic or linguistic training.

This is open-ended linguistic discovery. The prompts guide attention and composition; they are not compliance checklists.

## Cold-start contract

Run from the repository root with a unique run directory under `v3/run/`. Before starting, supply an independent primary scaffold for the exact passage scope. The scaffold states the passage's direct contextual proposition; it must not be copied from a gold reference or prior synthesis.

Production uses three native agent sessions and four intellectual turns with `gpt-5.6-sol` at maximum reasoning depth. A1 performs its two turns in one continuing session; the mechanism mapper and gold renderer each use a separate fresh session. Use the environment's native spawn, send, wait, and close operations, and set `fork_context: false` for every spawn so no agent inherits operator conversation history. Leave `service_tier` unset; do not request or override a priority tier when spawning any agent. Do not use `codex exec` to emulate an agent, and do not let a production agent spawn further agents.

The local source files are:

```text
resources/quran/surah_<surah>.json  Arabic passage
resources/qac.sqlite                positioned morphology and syntax
resources/attachments.tsv           syntax relation labels
resources/furuq_v4.sqlite            lexical branches
```

Preparation requires no model call. It emits only the evidence used by the four production turns. Publication validation and Markdown rendering are also deterministic and occur after Turn 4 without adding an intellectual turn.

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
| 4 | fresh gold renderer | `tasks/04-a2-publish.md` | `<surah>-publication.jsonl` |

All paths in this table are relative to `v3/run/<run-id>/`.

After Turn 4, deterministic finalization validates the JSONL and writes its prose-only Markdown derivative:

```bash
python3 v3/scripts/render_publication.py \
  v3/run/<run-id>/<surah>-publication.jsonl
```

This creates:

```text
v3/run/<run-id>/<surah>-publication.md
```

The JSONL remains canonical. The Markdown file is a human-readable derivative and is not another model output.

The normative presentation contract is:

```text
prompts/a2-publication-tr-audio-first.md
schemas/publication-record.schema.json
```

The prompt governs prose and finding fidelity. The schema and `scripts/publication_contract.py` govern only record shape and deterministic presentation constraints; they do not discover, score, merge, or adjudicate findings.

## Agent runbook

1. Spawn a fresh, context-free A1 agent for `tasks/01-a1-discover.md`. Tell it to read and execute that task, write only its assigned output, and not spawn subagents. Wait until it reports completion; do not steer it while it is reasoning.
2. Send `tasks/02-a1-integrate.md` to that same A1 session. Wait for completion, then close A1. Session continuity is required because this turn integrates rather than rediscovers A1's field.
3. Spawn a fresh, context-free A2 agent for `tasks/03-a2-map.md`. Give it no conversation history or unlisted material. Wait until it reports completion without intermediate feedback, then close A2.
4. Spawn a fresh, context-free gold renderer for `tasks/04-a2-publish.md`. It receives only the listed passage, scaffold, integrated discovery, and mechanism map. The task instructs it to run the deterministic checker after writing and to resolve structural or content-contract errors before reporting completion. Wait without intermediate feedback, then close it after it reports a valid artifact.
5. Run `v3/scripts/render_publication.py` on the resulting numbered publication JSONL to write Markdown. Style warnings are evaluation signals, not permission for the operator to rewrite prose after the production session.

Do not inspect against gold, rank findings, request revisions, or inject operator commentary between these turns. Maximum-depth turns can be long; a quiet interval is not a failure.

If a wait call times out or the operator interface is interrupted, first wait on the existing agent id again. Do not resend the task or spawn a duplicate while that agent may still be running. If an agent actually fails before writing its assigned artifact, restart only the incomplete turn. Preserve A1 continuity for Turn 2 whenever its session remains available; A2 and the renderer are independent fresh single-turn sessions.

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

### Turn 4: fresh Turkish gold renderer

A third, context-free agent receives the exact passage, primary scaffold, integrated discovery, and completed mechanism map. Using `prompts/a2-publication-tr-audio-first.md`, it turns those materials into the canonical structured publication:

```text
<surah>-publication.jsonl
```

The filename uses the numeric surah in the prepared passage, for example `1-publication.jsonl` or `100-publication.jsonl`, and is written in the run root. The renderer is the final presentation author, not a reviewer, auditor, validator, or new discovery agent. It preserves the established grading and breadth and does not reopen or rescore the mechanism map.

Every distinct graded finding in the mechanism map remains present. The renderer does not merge independent findings merely to shorten the work. A record may carry several grade strings only when those components are inseparable in the mechanism map.

Each physical JSONL line is one `opening`, `finding`, or `closing` record with exactly:

```text
kind
grades
title
paragraphs
```

Each finding is an independent machine-readable and listenable section. It normally uses two prose paragraphs: a concrete discovery beat followed by the decisive lexical grounding and passage-wide consequence. Line order is narration order. Grades remain metadata and are never embedded in spoken titles or prose.

The renderer uses exact Arabic script selectively for decisive Quranic surface words from the passage. It does not speak bare spaced roots, recite branch inventories, or introduce non-passage branch forms merely to prove evidence. Root relations are explained in ordinary Turkish as relationships within a word family. Turkish carries the complete explanation, and Arabic supplies limited, repeated familiarity with the words the listener actually hears in the Quran.

The prose creates movement through its objects, actions, returns, contrasts, and changes of scale. It never exposes production language such as camera, frame, shot, zoom, or close-up. It sounds conversational and human without becoming a sermon, classroom lesson, announcer script, or imitation of a named speaker.

Successive findings must not fall into one repeated rhetorical mold. The renderer varies titles, openings, sentence cadence, transitions, and conclusions; it does not repeatedly begin with `Metin`, lexical inventory, or a negative disclaimer, and it does not repeatedly close with `Böylece`, `Bu yüzden`, or equivalent stock language. Negative evidence remains available when a finding depends on exclusion, but the positive relation normally becomes perceptible before its boundary is stated.

When a numbered publication JSONL exists, TTS preparation reads that JSONL directly. Each record title and each string in `paragraphs` becomes its own playback unit. Grades remain available in app metadata but are never spoken. The derived Markdown file must not be reparsed as the source for production audio.

## Re-render an existing run

If a completed run already contains `inputs/passage-arabic.txt`, `inputs/primary-scaffold.md`, `a1/discovery-integrated.md`, and `a2/mechanism-map.md` for the same frozen passage scope, its upstream work is sufficient. Run `make_tasks.py` for that run root and execute only `tasks/04-a2-publish.md` in a fresh, context-free renderer session. The regenerated task writes `<surah>-publication.jsonl`. Then run `render_publication.py` to create `<surah>-publication.md`. Older Markdown publications remain historical artifacts until the new JSONL is successfully rendered. Do not rerun A1 or the mechanism mapper unless one of those upstream artifacts is intentionally changed.

## Confidence language

Each finding record preserves two separate grading dimensions in its `grades` array:

- `GÜÇLÜ / ORTA / ZAYIF`: how explicitly the supplied lexical record supports the branch image used in the finding.
- `A / B / C / C-koşullu`: how strongly the passage activates that image or coalition.

The first dimension does not claim source chronology, independent dictionary counts, or majority derivational opinion. Those facts are not available in the six-field input.

Activation strength comes from specific cross-root convergence, complementary roles, passage order, adjacency, recurrence, and contribution to the whole. A latent scene does not become weak merely because no surface word names that scene literally. Preserving the direct contextual meaning is sufficient; surface literalization is not an activation requirement.

## Orchestration boundary

The runtime prepares evidence, emits four task files, validates the final JSONL contract, and renders Markdown deterministically. It does not score, approve, reject, promote, rediscover, or close intellectual findings. The operator's role is limited to preserving the three-agent, four-turn sequence, allowing each turn to finish, and running deterministic finalization.

The production run is complete when the fresh renderer has written valid `<surah>-publication.jsonl`, reported completion, and deterministic finalization has written `<surah>-publication.md`. A blind gold or listening comparison may begin only afterward, outside all production sessions. It is an evaluation of the finished work, not a fifth workflow turn, and its findings are never retroactively supplied as production evidence.

## Batch-production gate

A new publication prompt or presentation contract is ready for unrestricted batch production only after fresh, context-free Turn 4 canaries for both S1 and S112:

1. write valid numbered publication JSONL from their frozen upstream artifacts;
2. pass deterministic validation and render numbered Markdown;
3. preserve every graded finding and grade without addition, omission, merging, or rescoring;
4. contain no spoken confidence codes, bare spaced roots, or exposed production vocabulary;
5. keep each finding intelligible at normal listening speed without relying on visual backtracking;
6. demonstrate varied human cadence across successive findings rather than a repeated subsection template;
7. pass an after-production listening review without feeding that review back into either production session.

Only after both canaries pass may the same frozen prompt, schema, validator, and TTS contract be used for wider regeneration. A failed canary returns the presentation package to development; it does not reopen A1 discovery or the A2 mechanism map.
