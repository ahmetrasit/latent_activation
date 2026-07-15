# Task Message Templates

Fill only `{...}` placeholders. Do not append gold, evaluations, or prior target prose.

## 1. Agent A — full integrated run

Use one continuous Agent A session when all evidence fits.

```text
Read and execute:
{PROMPTS}/01_agent_a_integrated_synthesis_prompt.md

WORKFLOW_ID: GSLS-3A-2.0
AGENT_ID: A
TASK_MODE: FULL
RUN_ROOT: {RUN}
SCHEMA_CONTRACT: {PROMPTS}/05_schema_contract.md

Authorized inputs:
- {RUN}/inputs/source-manifest.json
- {RUN}/inputs/source-manifest.md
- {RUN}/inputs/run-card.json
- {RUN}/inputs/run-card.md
- {RUN}/inputs/passage-arabic.txt
- {RUN}/inputs/primary-scaffold.md
- {RUN}/inputs/morphology.tsv
- {RUN}/inputs/syntax.tsv
- {optional discourse, attachments, acoustic, network, and controls}
- {RUN}/inputs/lexical-branches.jsonl

You are the sole discovery agent and sole author of the gold notebook.
Perform complete integrated discovery, dynamic open-role retrieval,
progressive recitation, backward replay, internal validation, and draft
gold generation. Do not delegate or create subagents.

Write every Agent A state and draft artifact required by the prompt under:
{RUN}/agent-a/

Final reply: output paths, closure status, and unresolved human adjudications.
```

## 2. Agent A — initialize persistent-cycle mode

Send to a new Agent A session and retain that same session for every later Agent A task.

```text
Read and execute:
{PROMPTS}/01_agent_a_integrated_synthesis_prompt.md

WORKFLOW_ID: GSLS-3A-2.0
AGENT_ID: A
TASK_MODE: INITIALIZE
RUN_ROOT: {RUN}
SCHEMA_CONTRACT: {PROMPTS}/05_schema_contract.md

Authorized inputs:
{complete input list}

Build the complete primary passage model, relational branch frames,
progressive recitation baseline, seed universe, initial query state, and
coverage ledger. Do not draft the gold yet.

Write:
- {RUN}/agent-a/state/synthesis-state.json
- {RUN}/agent-a/state/branch-frames.jsonl
- {RUN}/agent-a/state/passage-events.jsonl
- {RUN}/agent-a/state/progressive-trajectory.jsonl
- {RUN}/agent-a/state/candidate-cards.jsonl
- {RUN}/agent-a/state/coverage-ledger.jsonl
- {RUN}/agent-a/state/query-history.jsonl

Final reply: paths, initialization closure, and the first exact evidence batch requested.
```

## 3. Agent A — discovery cycle

Send to the same Agent A session.

```text
Continue the same Agent A run under:
{PROMPTS}/01_agent_a_integrated_synthesis_prompt.md

WORKFLOW_ID: GSLS-3A-2.0
AGENT_ID: A
TASK_MODE: DISCOVERY_CYCLE
CYCLE_ID: {cycle_id}
RUN_ROOT: {RUN}

Read:
- current frozen Agent A state
- exact deterministic evidence batch: {batch paths}
- all source sidecars referenced by active queries
- whole-passage run card and passage-event index

Process every supplied branch, occurrence seed, construction seed, open
role, and replay request. Update candidates, open roles, coverage,
progressive trajectory, backward replay, and query history.

Do not draft or close the run unless the closure conditions are met.
Do not start a new independent interpretation.

Write versioned state artifacts and:
{RUN}/agent-a/state/cycle-{cycle_id}-report.md

Final reply: paths, novelty counts, remaining coverage, and next exact batch request or `READY-FOR-DRAFT`.
```

## 4. Agent A — draft gold

Send to the same Agent A session only after deterministic closure checks pass.

```text
Continue the same Agent A run under:
{PROMPTS}/01_agent_a_integrated_synthesis_prompt.md

WORKFLOW_ID: GSLS-3A-2.0
AGENT_ID: A
TASK_MODE: DRAFT_GOLD
RUN_ROOT: {RUN}

Inputs:
- complete frozen Agent A state
- every evidence sidecar referenced by live candidates
- deterministic closure report

Write:
- {RUN}/agent-a/draft/draft-gold-manifest.jsonl
- {RUN}/agent-a/draft/draft-gold-notebook.md
- {RUN}/agent-a/draft/draft-closure.md

The notebook must preserve independent channels, conditional candidates,
defeated alternatives, primary effects, boundaries, and temporal
reactivations. Final reply: paths and closure lines.
```

## 5. Agent B — adversarial audit

Use a fresh Agent B session.

```text
Read and execute:
{PROMPTS}/02_agent_b_adversarial_audit_prompt.md

WORKFLOW_ID: GSLS-3A-2.0
AGENT_ID: B
RUN_ROOT: {RUN}
SCHEMA_CONTRACT: {PROMPTS}/05_schema_contract.md

Authorized inputs:
- complete clean evidence package
- all frozen Agent A state artifacts
- draft-gold-manifest.jsonl
- draft-gold-notebook.md
- deterministic coverage and hash indexes

Do not read gold, evaluation, prior prose, or Agent C output.
Do not edit or rewrite the gold.

Write:
- {RUN}/agent-b/audit-report.md
- {RUN}/agent-b/audit-actions.jsonl
- {RUN}/agent-b/missed-candidate-proposals.jsonl
- {RUN}/agent-b/audit-closure.md

Final reply: paths, required-action count, and human-adjudication count.
```

## 6. Agent A — adjudication and final gold

Send to the same Agent A logical session. When the original context has expired, resume with the same Agent A prompt, exact frozen state, and session continuity record.

```text
Read and execute:
{PROMPTS}/03_agent_a_adjudication_revision_prompt.md

WORKFLOW_ID: GSLS-3A-2.0
AGENT_ID: A
TASK_MODE: ADJUDICATE
RUN_ROOT: {RUN}

Inputs:
- complete frozen Agent A state
- Agent A draft artifacts
- Agent B audit report
- Agent B action queue
- Agent B missed-candidate proposals
- exact evidence referenced by every audit action

Resolve every action independently. Reopen the dynamic search when a valid
audit proposal creates a new role, coalition, or backward reactivation.

Write:
- {RUN}/agent-a/final/final-gold-manifest.jsonl
- {RUN}/agent-a/final/final-gold-notebook.md
- {RUN}/agent-a/final/adjudication-log.md
- {RUN}/agent-a/final/final-closure.md

Final reply: paths, action closure, and unresolved human adjudications.
```

## 7. Agent C — optional publication

Use a fresh Agent C session.

```text
Read and execute:
{PROMPTS}/04_agent_c_publication_renderer_prompt.md

WORKFLOW_ID: GSLS-3A-2.0
AGENT_ID: C
RUN_ROOT: {RUN}
OUTPUT_LANGUAGE: {language}
AUDIENCE: {audience}
LENGTH_POLICY: {policy}

Inputs:
- run card
- exact passage
- final-gold-manifest.jsonl
- final-gold-notebook.md
- final closure report

No raw discovery, no regrading, no deletion from gold.

Write:
- {RUN}/agent-c/publication-architecture.md
- {RUN}/agent-c/publication-essay.md
- {RUN}/agent-c/publication-map.jsonl
- {RUN}/agent-c/render-closure.md

Final reply: paths, selected publication mode, and render closure.
```
