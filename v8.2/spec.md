# V8.2 Cold Orchestration Specification

This file is the executable orchestration contract for running V8.2 on one
surah from a cold context. It tells the orchestrator how to select inputs,
create the run, isolate production agents, sequence the four turns, and hand
off the resulting artifacts.

The four files under `v8.2/prompts/` are authoritative for semantic behavior.
Do not reproduce, summarize, or improvise their instructions in place of
having each production agent read the relevant prompt completely.

For orchestration, this file governs if `v8.2/README.md`, an older run task, or
an earlier pilot convention differs from it.

## 1. Required invocation

The orchestrator must be given:

- a surah number;
- optionally, an explicit V3 input-bundle path;
- optionally, a run label.

Normalize a single surah number to three digits for paths. For example, Surah
1 becomes `s001`, Surah 96 becomes `s096`, and Surah 112 becomes `s112`.

Use the repository root as the working directory. All paths below are relative
to that root unless an absolute path is required by the available tools.

## 2. Canonical agent settings

Every newly spawned production agent must use these exact settings:

```json
{
  "agent_type": "worker",
  "fork_context": false,
  "model": "gpt-5.6-sol",
  "reasoning_effort": "max"
}
```

Use `multi_agent_v1.spawn_agent` when it is available. Put the self-contained
task message in the tool's task or message field in addition to the settings
above. Do not pass the surrounding conversation to either production agent.

If only `collaboration.spawn_agent` is available, set `fork_turns` to `none`
and provide the same self-contained task message. That interface guarantees a
cold context but does not expose worker role, model, or reasoning-effort
selection. Use this fallback only when the user has permitted the available
tool, and report the three unselectable settings as a procedural deviation.
Do not insert a claim about the model into the semantic task message and do not
silently call the fallback an exact-settings run.

Do not set a service tier unless the user separately requests one.

## 3. Architecture and session identity

One surah uses two production roles and four prompt turns:

```text
Agent 1 — one persistent session
  Turn 1: branch-seeded formation discovery
  Turn 2: recursive reopening
  Turn 3: reciprocal scaffold integration

Agent 2 — one fresh session
  Turn 4: compositional semantic synthesis
```

Spawn Agent 1 once for Turn 1. Save its returned agent/session identifier.
Deliver Turns 2 and 3 as follow-up tasks to that same identifier. A new worker
for either follow-up does not satisfy the persistent-author design.

Spawn Agent 2 only after Agent 1 has completed Turn 3. Agent 2 must be a newly
spawned cold worker with `fork_context: false`; do not reuse Agent 1 or another
surah's agent.

There is no within-surah parallel discovery in this version. Different surahs
may be orchestrated in parallel, but every surah must have its own Agent 1,
Agent 2, input boundary, and run root.

## 4. Resolve the authorized input bundle

An authorized bundle contains exactly these required materials:

```text
passage-arabic.txt
morphology.tsv
syntax.tsv
lexical-branches.jsonl
primary-scaffold.md
```

Resolve the bundle as follows:

1. If the user supplied an explicit bundle path, use that path.
2. Otherwise search only for `v3/run/sNNN-*/inputs/` matching the normalized
   surah.
3. If exactly one matching `sNNN-full-*` bundle exists, use it.
4. If no full bundle exists and exactly one candidate bundle exists, use that
   candidate.
5. If no candidate bundle exists, stop and ask the user for an explicit bundle
   path.
6. If selection remains ambiguous, stop and ask the user which bundle to use.
   Do not choose by modification time and do not silently prefer a pilot,
   composite, or earlier analysis run.

Confirm that all five required files exist and are non-empty. This is an
orchestration precondition, not a semantic audit.

Only the five files inside the selected `inputs/` directory are production
material. Other files beside that directory—including V3 discovery notebooks,
mechanism maps, publications, and task files—are comparison material and must
not be shown to production agents.

Do not copy or transform the bundle. V8.2 reads the existing input materials in
place.

## 5. Create a non-destructive run root

Unless the user supplies a run label, use `pilot`. Build the run root as
`v8.2/run/sNNN-<label>-YYYYMMDD/` using the local calendar date. The default is:

```text
v8.2/run/sNNN-pilot-YYYYMMDD/
```

Create these directories, where `<RUN_ROOT>` is the exact root resolved above:

```text
<RUN_ROOT>/a1/
<RUN_ROOT>/a2/
```

If that run root already contains any production artifact, do not overwrite
it. Select a new explicit suffix such as `-02`, or ask the user when the
intended identity is unclear.

The four canonical artifact paths are:

```text
a1/01-branch-seeded-formations-v8.2.md
a1/02-recursively-expanded-field-v8.2.md
a1/03-reciprocal-formation-field-v8.2.md
a2/04-compositional-semantic-synthesis-v8.2.md
```

Production agents must write with `apply_patch`. They must not add process
notes, self-evaluations, grades, run logs, or summaries to the artifacts.

## 6. Closed-field input matrix

The input boundary is part of the experiment and must be enforced exactly.

| Turn | Agent | Prompt | Raw passage, morphology, syntax, branches | Scaffold | Earlier artifacts |
|---|---|---|---|---|---|
| 1 | persistent Agent 1 | `01_branch_seeded_formation-v8.2.md` | yes | no | none |
| 2 | same Agent 1 | `02_recursive_reopening-v8.2.md` | yes | no | Turn 1 |
| 3 | same Agent 1 | `03_reciprocal_scaffold_integration-v8.2.md` | yes | yes, first exposure | Turns 1–2 |
| 4 | fresh Agent 2 | `04_compositional_semantic_synthesis-v8.2.md` | yes | yes | Turns 1–3 |

For Turns 1 and 2, do not list `primary-scaffold.md` as an authorized input and
do not mention its contents. The task message may name its exact path only in
the explicit prohibition against reading it. The scaffold enters Agent 1's
session for the first time in Turn 3.

Agent 2 receives the scaffold from the beginning, but its prompt requires a
specific reading order: it must inspect the raw passage, morphology, syntax,
branches, and scaffold for itself before opening Agent 1's three artifacts.

## 7. Global production isolation

Every production task message must state that the agent may read only:

- the prompt for its current turn;
- the authorized bundle files for that turn;
- the authorized earlier artifacts for that turn.

Production agents must not read:

- `v8.2/README.md` or this orchestration specification;
- any other V8.2 run;
- any other surah's material;
- V3 or V7 discovery, synthesis, publication, task, or evaluation artifacts;
- S1 or `_audio` reference outputs;
- project observations, prior assessments, or documentation;
- external commentary, translations, web material, or remembered reference
  analyses.

The orchestrator may inspect prior work after production is complete for a
separate assessment. Such material must never be fed back into the four
production turns.

## 8. Turn 1 — spawn persistent Agent 1

Spawn Agent 1 with the canonical settings and a self-contained task based on
this template. Substitute the exact surah, bundle, and output paths.

```text
You are the persistent V8.2 formation author for Surah <N>. This is Turn 1 of
three turns in the same session.

Read `v8.2/prompts/01_branch_seeded_formation-v8.2.md` completely and follow it.

Authorized inputs:
- <BUNDLE>/passage-arabic.txt
- <BUNDLE>/morphology.tsv
- <BUNDLE>/syntax.tsv
- <BUNDLE>/lexical-branches.jsonl

The primary scaffold is intentionally withheld. Do not read
<BUNDLE>/primary-scaffold.md.

Do not read documentation, prior V3/V7/V8.2 analyses, publications, reference
outputs, or any other passage material. Work only inside the authorized closed
field.

Write the artifact with apply_patch to:
<RUN_ROOT>/a1/01-branch-seeded-formations-v8.2.md

Do not put process commentary or self-assessment in the artifact. On
completion, report only the path and a concise structural count.
```

Wait for the worker to report completion. Confirm only that the expected file
exists and is non-empty. Do not tune a prompt or redirect the author's semantic
choices between turns.

## 9. Turn 2 — follow up with the same Agent 1

Send a follow-up task to the saved Agent 1 identifier. Do not spawn another
worker.

```text
Continue the same persistent Surah <N> formation session with Turn 2 only.

Read `v8.2/prompts/02_recursive_reopening-v8.2.md` completely and follow it.

Authorized materials:
- <BUNDLE>/passage-arabic.txt
- <BUNDLE>/morphology.tsv
- <BUNDLE>/syntax.tsv
- <BUNDLE>/lexical-branches.jsonl
- <RUN_ROOT>/a1/01-branch-seeded-formations-v8.2.md

The primary scaffold remains withheld. Do not read
<BUNDLE>/primary-scaffold.md.

Do not read documentation, prior V3/V7/V8.2 analyses, publications, reference
outputs, other surahs, or outside material.

Write the artifact with apply_patch to:
<RUN_ROOT>/a1/02-recursively-expanded-field-v8.2.md

Do not put process commentary or self-assessment in the artifact. On
completion, report only the path and a concise structural count.
```

Wait for completion and confirm only that the expected artifact exists and is
non-empty. Preserve the same author even if Turn 1 was unusually large or
untidy; reorganization is the purpose of Turn 2.

## 10. Turn 3 — introduce the scaffold to Agent 1

Send another follow-up task to the same saved Agent 1 identifier.

```text
Continue the same persistent Surah <N> formation session with Turn 3 only.

Read `v8.2/prompts/03_reciprocal_scaffold_integration-v8.2.md` completely and follow
it.

Authorized materials:
- <BUNDLE>/passage-arabic.txt
- <BUNDLE>/morphology.tsv
- <BUNDLE>/syntax.tsv
- <BUNDLE>/lexical-branches.jsonl
- <BUNDLE>/primary-scaffold.md
- <RUN_ROOT>/a1/01-branch-seeded-formations-v8.2.md
- <RUN_ROOT>/a1/02-recursively-expanded-field-v8.2.md

The primary scaffold enters this session now for the first time. Let it enter
reciprocal contact with the formation field. Preserve formations that remain
autonomous rather than forcing everything under one master account.

Do not read documentation, prior V3/V7/V8.2 analyses, publications, reference
outputs, other surahs, or outside material.

Write the artifact with apply_patch to:
<RUN_ROOT>/a1/03-reciprocal-formation-field-v8.2.md

Do not put process commentary or self-assessment in the artifact. On
completion, report only the path and a concise structural count.
```

Wait for completion and confirm only that the expected artifact exists and is
non-empty. Agent 1's work is now complete.

## 11. Turn 4 — spawn fresh Agent 2

Spawn a new worker with the canonical settings and `fork_context: false`. Do
not follow up Agent 1. Use this task template:

```text
You are a fresh independent V8.2 synthesis author for Surah <N>. You did not
write the formation artifacts and have no cross-passage context.

Read `v8.2/prompts/04_compositional_semantic_synthesis-v8.2.md` completely and follow it.

Authorized raw inputs:
- <BUNDLE>/passage-arabic.txt
- <BUNDLE>/morphology.tsv
- <BUNDLE>/syntax.tsv
- <BUNDLE>/lexical-branches.jsonl
- <BUNDLE>/primary-scaffold.md

Authorized formation artifacts:
- <RUN_ROOT>/a1/01-branch-seeded-formations-v8.2.md
- <RUN_ROOT>/a1/02-recursively-expanded-field-v8.2.md
- <RUN_ROOT>/a1/03-reciprocal-formation-field-v8.2.md

Follow the prompt's independent-entry order: inspect all raw inputs and the
scaffold for yourself before opening the three formation artifacts. Treat the
artifacts as generative material, not a canonical hierarchy. Let the prompt
determine hierarchy; add no quota or preselected passage architecture in the
task message.

Do not read documentation, prior V3/V7/V8.2 analyses, publications, reference
outputs, other surahs, or outside material.

Write the artifact with apply_patch to:
<RUN_ROOT>/a2/04-compositional-semantic-synthesis-v8.2.md

Do not put process commentary or self-assessment in the artifact. On
completion, report only the path and a concise structural count.
```

Wait for completion and confirm that the expected synthesis exists and is
non-empty.

## 12. Minimal completion contract

The production run is complete when all four conditions hold:

1. The three Agent 1 artifacts originated from one persistent session across
   Turns 1–3.
2. Agent 1 first saw the scaffold in Turn 3.
3. Agent 2 was a fresh, non-forked worker.
4. All four canonical artifacts exist at the selected run root.

Report the run root and four artifact paths. Also report any model, context,
session, or input-boundary deviation. Do not create a validation report,
branch ledger, confidence table, or traceability package.

Do not commit or push the run automatically unless the user requested version
control. Preserve unrelated worktree changes.

## 13. Failure and restart behavior

If Agent 1 fails during a turn, inspect only whether the expected artifact path
exists. If it is absent and the session remains usable, send a concise
follow-up asking it to finish that same turn at the same path. Do not change
the semantic objective.

If the persistent Agent 1 session is lost before Turn 3, do not splice a new
author into the old reservoir and call it an exact V8.2 run. Start a new Agent 1
from Turn 1 in a new run root, or clearly label the run as a procedural
deviation.

If Agent 2 fails and its expected path is absent, a newly spawned cold
replacement may repeat Turn 4 from the same authorized inputs because that
role is intentionally fresh. The two-agent architecture describes successful
production roles, not the number of failed spawn attempts.

If a failed turn leaves uncertain or partial material at its expected path,
preserve it and abandon that run root rather than overwriting it. For an Agent
1 failure, restart from Turn 1 with a new persistent author in a new run root.
For an Agent 2 failure, create a new run root, copy the three completed Agent 1
artifacts byte-for-byte into its canonical `a1/` paths, and spawn a new cold
Agent 2 against that unchanged reservoir. Report the restart. The copy is an
orchestration recovery operation, not a new semantic turn.

Never repair a failure by exposing the scaffold during Turns 1 or 2, feeding
an earlier publication to an agent, or merging material from another surah.

## 14. Prompt-change boundary

Do not edit or retune prompts in the middle of a surah run. A passage run must
measure one stable prompt set.

If behavior suggests a prompt change, finish or explicitly abandon the
current run. Make the prompt change outside production, preserve it as a new
baseline when version control is requested, and start a new run root. Never
silently regenerate only the weak turn with changed instructions.

## 15. Post-run assessment, when requested

Assessment is separate from production and is performed by the orchestrator,
not by either production agent. Read the four completed artifacts directly.
Previous V3, V7, S1, or other V8.2 outputs may be used only now as comparison
material.

Focus the assessment on agent behavior and synthesis quality:

- Did complete Arabic `source_phrase_ar` prose produce exact cross-root
  lexical bridges rather than only short-label associations?
- Did formations assign differentiated roles, operations, directions, or
  consequences rather than merely share a theme?
- Did Turn 2 reorganize and discover, or mostly restate Turn 1?
- Did scaffold contact work in both directions without becoming an admission
  test or master explanation?
- Did autonomous material formations remain alive when they changed a
  different dimension of the passage?
- Did the synthesis preserve precise lexical surprises that make surface wording
  sound different?
- Did optional open pulls remain genuinely optional, or become formulaic
  paragraph endings?
- On a large bundle, did one persistent author maintain breadth, or flatten
  the field into familiar abstractions?

Treat these as qualitative reading questions, not a scoring rubric. The goal
is to improve prompts and agent behavior, not to audit the accepted branch
bundle or demand bug-free interpretive certainty.

## 16. Parallel orchestration of several surahs

When the user requests several surahs in parallel:

- resolve each bundle independently;
- create a different run root for each;
- spawn a different persistent Agent 1 for each with no forked context;
- never mention another active surah in a production task;
- start each fresh Agent 2 only after that surah's own Turn 3 completes;
- keep every artifact path passage-specific.

Parallelism changes scheduling only. It does not change the four-turn semantic
workflow or authorize cross-passage transfer during production.
