# V8.4.4 Controlled Orchestration Specification

This is the controlling cold-run specification for V8.4.4. Before taking any
orchestration action, read `v8.4/spec.md` completely. Its invocation, bundle
resolution, non-destructive run-root, isolation, task-construction, restart,
and assessment rules are incorporated here with these global substitutions:

- substitute `v8.4.4` for `v8.4` in prompt, run, and artifact paths;
- treat the synthesis role as three persistent turns rather than two;
- apply the Turn 5 and Turn 6 boundaries below instead of V8.4's Turn 5;
- use the six-artifact completion contract below.

V8.4.4 otherwise inherits the V8.4 cold workflow, agent isolation, input
boundaries, and Turn 1–4 semantics. The versioned copies in
`v8.4.4/prompts/` keep those semantics unchanged. It preserves V8.4.2's
two-turn recovery/recomposition boundary. Turn 5 adds an exact-carrier
collision traversal and then performs a form-status eligibility pass before
inherited-draft ranking. Turn 6 makes exact locks the spines of broader
mechanisms, assigns publication rank and scale by nonredundant passage work,
and calibrates source-example evidence without suppressing it. After forming a
provisional final, Turn 6 must complete the separate evidence-form,
morphology-entailment, and load-bearing-survival passes before writing the
publication artifact.

Every newly spawned production agent must use these exact settings when the
available interface exposes them:

```json
{
  "agent_type": "worker",
  "fork_context": false,
  "model": "gpt-5.6-sol",
  "reasoning_effort": "max"
}
```

Use `multi_agent_v1.spawn_agent` when available. If only
`collaboration.spawn_agent` is available, use `fork_turns: "none"`; that
fallback does not expose worker role, model, or reasoning-effort selection, so
report those three settings as unselectable rather than calling the run an
exact-settings run. Do not supply a service tier unless the user explicitly
requests one.

## Author sequence

For a full cold run:

1. one persistent formation author executes Turns 1–3;
2. one fresh synthesis author executes Turn 4;
3. the same synthesis author executes Turn 5 without leaving the session;
4. the same synthesis author executes Turn 6 as the final publication.

Use these prompts in order:

```text
v8.4.4/prompts/01_branch_seeded_formation-v8.4.4.md
v8.4.4/prompts/02_recursive_reopening-v8.4.4.md
v8.4.4/prompts/03_reciprocal_scaffold_integration-v8.4.4.md
v8.4.4/prompts/04_compositional_semantic_synthesis-v8.4.4.md
v8.4.4/prompts/05_postdraft_recovery_field-v8.4.4.md
v8.4.4/prompts/06_selective_final_recomposition-v8.4.4.md
```

Write every generated artifact with `v8.4.4` in its filename. The synthesis
paths are:

```text
a2/04-compositional-semantic-synthesis-v8.4.4.md
a2/05-postdraft-recovery-field-v8.4.4.md
a2/06-selective-final-recomposition-v8.4.4.md
```

## Turn boundaries

Turn 4 receives only the raw bundle, primary scaffold, and three formation
artifacts.

Turn 5 receives those same authorized materials plus that author's own Turn 4
synthesis. It produces an intermediate recovery field, not publication prose.
Its inherited floor is established only after the prompt's form-status pass.

Turn 6 receives the complete authorized field, Turn 4, and Turn 5. It produces
the sole final synthesis. The author must keep the release passes internal and
write only the resulting self-standing publication.

All three synthesis turns must prohibit prior versions, comparisons,
assessments, other surahs, project documentation, outside commentary, and
remembered benchmark diagnoses. Do not name known omissions or suggest a
passage architecture. README examples and benchmark findings are assessment
context only and must never enter an author task.

## Controlled development run

For S103, S112, and S1, reuse the frozen formation artifacts because
Turns 1–3 remain semantically unchanged. Spawn a new cold synthesis author for
each passage. Do not reuse any earlier-version author or draft. Give each
author the versioned Turn 4 prompt, then deliver Turns 5 and 6 as follow-ups in
the same session.

## Cold-run paths and input matrix

Resolve the authorized bundle and create a non-destructive run root exactly as
specified in `v8.4/spec.md`, using `v8.4.4/run/` as the version root. A full
production run creates `a1/` and `a2/` beneath that run root and writes all six
canonical artifacts. Do not overwrite a populated run root.

The closed-field input matrix is:

| Turn | Author | Raw passage, morphology, syntax, branches | Scaffold | Earlier artifacts |
|---|---|---|---|---|
| 1 | persistent formation author | yes | no | none |
| 2 | same formation author | yes | no | Turn 1 |
| 3 | same formation author | yes | yes, first exposure | Turns 1–2 |
| 4 | fresh synthesis author | yes | yes | Turns 1–3 |
| 5 | same synthesis author | yes | yes | Turns 1–4 |
| 6 | same synthesis author | yes | yes | Turns 1–5 |

For every turn, the task message must tell the agent to read the complete
versioned prompt, list every authorized input and output path, prohibit all
other project or outside material, require `apply_patch`, and request only the
completed path plus a concise structural count in the agent's response.

For Turn 5, say explicitly that it is producing the intermediate recovery
field, not final publication. For Turn 6, say explicitly that it is producing
the sole self-standing final synthesis. Do not summarize what the orchestrator
or any assessment believes the passage is missing.

An exact V8.4.4 run is complete only when one persistent formation author wrote
Turns 1–3, first saw the scaffold in Turn 3, one fresh cold synthesis author
wrote Turns 4–6 in a single persistent session, and all six canonical artifacts
exist and are non-empty. If the synthesis session is lost after Turn 4 or Turn
5, do not splice in a new author. Preserve the formation reservoir, abandon the
partial synthesis run, and restart Turns 4–6 with one new cold synthesis author
under a non-overwriting run root, following the restart rules in
`v8.4/spec.md`.

Assessment begins only after Turn 6. First compare Turn 4 with the recovery
field and final synthesis while blind to predecessors. Fix whether recovery
was real, whether final inclusion was selective, whether governing coverage
survived, whether every participant-role statement is entailed by the supplied
morphology, whether explicitly different forms stayed non-governing without
being automatically discarded, and whether any claim lost its evidence. Only
then consult V8.4.3, V8.4.2, V8.4.1, V8.3, V3, or the S1 audio reference.

S96 remains prohibited until S103, S112, and S1 establish production
readiness. On a production run, do not supply development assessments or
known benchmark formations to any author.
