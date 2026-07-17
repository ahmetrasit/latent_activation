# V7.4.0 + V7.4.1 Composite Run Specification

## Status

This is the canonical operator specification for new V7 generalization runs.
It composes frozen semantic prompts from V7.4.0 with frozen rendering prompts
from V7.4.1. It is passage-agnostic.

## Fixed constants

```text
MODEL = gpt-5.6-sol
REASONING_EFFORT = max
SERVICE_TIER = unset
SEMANTIC_VERSION = v7.4.0
RENDER_VERSION = v7.4.1
SUBAGENTS = forbidden
```

## Run variables

Set these values for each prepared passage:

```text
PASSAGE_ID = <stable passage identifier>
RUN_ID = <passage identifier plus run date or attempt>
INPUT_ROOT = <prepared V3 run>/inputs
RUN_ROOT = v7/run/<RUN_ID>
SEMANTIC_ROOT = <RUN_ROOT>/v7.4.0
RENDER_ROOT = <RUN_ROOT>/v7.4.1
```

`PASSAGE_ID` is used in the final publication filename. `RUN_ID` distinguishes
separate attempts without changing prompt versions.

## Required inputs

The input bundle must contain exactly the prepared passage scope:

```text
P = <INPUT_ROOT>/passage-arabic.txt
M = <INPUT_ROOT>/morphology.tsv
Y = <INPUT_ROOT>/syntax.tsv
L = <INPUT_ROOT>/lexical-branches.jsonl
S = <INPUT_ROOT>/primary-scaffold.md
```

Do not add gold references, prior publications, commentary, translations,
outside sources, or outputs from another passage.

## Required directories

Create version-separated task and artifact locations:

```text
<SEMANTIC_ROOT>/tasks/
<SEMANTIC_ROOT>/a1/
<SEMANTIC_ROOT>/a2/
<RENDER_ROOT>/tasks/
<RENDER_ROOT>/a3/
```

Task wrappers bind paths only. They reference the frozen reusable prompts and
must not copy or modify their instructions.

## Pre-run commit boundary

Before Session A starts:

1. Create all eight task wrappers with their final versioned paths.
2. Confirm that every required input and frozen prompt path exists.
3. Confirm that no wrapper authorizes a prohibited input.
4. Commit the passage binding without staging unrelated worktree files.
5. Push that commit to the shared remote.

Do not create the first model output until this boundary is complete. A new
passage binding does not create a new prompt version.

## Session A: Agent 1

Start one fresh native session and preserve it through Tasks 1-3.

### Task 1: activation reservoir

```text
prompt: v7/prompts/v7.4.0/01_activation_reservoir.md
inputs: P, M, Y, L
withheld: S
output: <SEMANTIC_ROOT>/a1/01-activation-reservoir-v7.4.0.md
```

### Task 2: recursive formation maturation

Continue Session A without operator steering.

```text
prompt: v7/prompts/v7.4.0/02_recursive_formation_maturation.md
inputs: P, M, Y, L, Task 1 output
withheld: S
output: <SEMANTIC_ROOT>/a1/02-mature-formations-v7.4.0.md
```

### Task 3: reciprocal primary integration

Continue Session A. Introduce the primary scaffold for the first time.

```text
prompt: v7/prompts/v7.4.0/03_reciprocal_primary_integration.md
inputs: P, M, Y, L, S, Task 1 output, Task 2 output
output: <SEMANTIC_ROOT>/a1/03-reciprocal-field-v7.4.0.md
```

End Session A after Task 3.

## Session B: Agent 2

Start one fresh native session and preserve it through Tasks 4-5.

### Task 4: independent mechanism recomposition

```text
prompt: v7/prompts/v7.4.0/04_independent_mechanism_recomposition.md
inputs: P, M, Y, L, S, Task 1 output, Task 3 output
excluded: Task 2 output
output: <SEMANTIC_ROOT>/a2/04-independent-mechanism-map-v7.4.0.md
```

Agent 2 must read `P`, `M`, `Y`, `L`, and `S` before opening either Agent 1
artifact. Agent 1's organization is generative material, not the starting
ontology or upper bound.

### Task 5: canonical Turkish semantic master

Continue Session B without operator steering.

```text
prompt: v7/prompts/v7.4.0/05_semantic_master_tr.md
inputs retained in session: P, M, Y, L, S, Task 1 output, Task 3 output
new input: Task 4 output
output: <SEMANTIC_ROOT>/a2/05-semantic-master-tr-v7.4.0.md
```

End Session B after Task 5. Commit the V7.4.0 outputs before beginning the
rendering component.

## Session C: Agent 3

Start one fresh native session and preserve it through Tasks 6-8.

Agent 3's entire semantic authority is limited to:

```text
P
S
Task 5 semantic master
```

Do not provide `M`, `Y`, `L`, Tasks 1-4, a prior publication, or a gold
reference.

### Task 6: oral narrative rehearsal

```text
prompt: v7/prompts/v7.4.1/06_oral_narrative_rehearsal.md
inputs: P, S, Task 5 semantic master
output: <RENDER_ROOT>/a3/06-oral-rehearsal-tr-v7.4.1.md
```

### Task 7: complete Turkish publication draft

Continue Session C without operator steering.

```text
prompt: v7/prompts/v7.4.1/07_canonical_publication_tr.md
inputs retained in session: P, S, Task 5 semantic master
new input: Task 6 output
output: <RENDER_ROOT>/a3/07-publication-draft-tr-v7.4.1.md
```

### Task 8: canonical rendered essay

Continue Session C without operator steering.

```text
prompt: v7/prompts/v7.4.1/08_dual_medium_revision.md
inputs retained in session: P, S, Task 5 semantic master, Task 6 output
new input: Task 7 output
output: <RENDER_ROOT>/<PASSAGE_ID>-publication-tr-v7.4.1.md
```

End Session C after Task 8. Commit all V7.4.1 outputs.

## Required task-wrapper metadata

Every wrapper must state:

```text
MODEL: gpt-5.6-sol
REASONING_EFFORT: max
SERVICE_TIER: unset
SESSION: fresh or continue, with the exact task range
SUBAGENTS: forbidden
PROMPT: exact frozen prompt path
INPUTS: exact authorized paths
OUTPUT: one exact versioned path
```

## Session recovery

Never replace a required persistent session with a fresh agent midway through
its task range. If a session is lost before its final task completes, create a
new `RUN_ID` attempt and restart that session from its first task. Preserve the
failed attempt; do not overwrite or splice its outputs into the new attempt.

Operational failure does not create a new prompt version. Only a prompt change
does.

## Reading the completed run

Read in this order:

1. `<SEMANTIC_ROOT>/a2/05-semantic-master-tr-v7.4.0.md`
2. `<RENDER_ROOT>/<PASSAGE_ID>-publication-tr-v7.4.1.md`

The semantic master shows the complete formation topology. The rendered essay
shows whether that topology supports a coherent human account outside the
research structure.

Look for differentiated lexical roles, retroactive strengthening, new
interaction-level consequences, simultaneous secondary resonances, and a
changed hearing of the direct passage. In the render, look for preservation and
integration of those properties.

Do not use word count, gold-item coverage, recurring provenance phrases,
stylistic elegance, target-language finish, or TTS quality as decision rules.
Do not turn the reading into disambiguation, confidence grading, or branch
admission.

## Completion condition

A composite run is complete only when all eight versioned artifacts exist and
the three session boundaries were preserved. During current generalization
work, do not declare a passage run complete after Task 5 alone.

V7.5 is not planned. Consider a new semantic version only if the same upstream
semantic failure recurs across multiple new passage runs. A rendering-only
problem belongs to a later rendering version, not V7.5.
