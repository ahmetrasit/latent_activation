# GSLS V7

V7 is a prompt-only workflow for recursive latent-activation formation and
dual-medium Turkish publication. It treats a lexical resonance as something
that can acquire its force only after other supplied details complete it and
the completed configuration sends meaning back into its parts.

The workflow reuses prepared V3 input bundles. It adds no schema, validator,
audit agent, scoring system, or deterministic semantic gate.

## Cognitive flow

```text
closed supplied field
  -> activation reservoir
  -> recursive configuration maturation
  -> reciprocal primary integration
  -> Turkish semantic master
  -> oral narrative rehearsal
  -> canonical Turkish draft
  -> dual-medium production revision
```

The primary contextual scaffold enters only after configurations have had room
to form. It then participates in a reciprocal rereading: the configurations
change perception of the primary propositions, and the primary propositions
reveal new roles and force inside the configurations.

## Sessions

Run every turn with `gpt-5.6-sol` at reasoning effort `max`. Leave service tier
unset.

- Agent 1 remains in one session for Turns 1-4.
- Agent 2 starts fresh and remains in one session for Turns 5-7.
- Neither agent spawns subagents.

The semantic author keeps formations alive across recursive rereadings. The
publication author owns narrative order, prose, and auditory revision in one
continuous session, so a separate renderer cannot flatten the analysis.

See `00_orchestration.md` for the runbook.

## Prompt versions

Prompt versions are immutable after they have produced a run.

```text
prompts/<version>/
run/<run-id>/<version>/
```

Every task and output filename includes the same version. A prompt change
creates a new complete version directory and a commit before the next model
run. Earlier prompts and outputs remain available for direct comparison.

## Initial pilot

The first pilot binds the frozen V3 S1 evidence package without copying or
altering it:

```text
v3/run/s001-full-20260716/inputs/
```

The S1 binding exists only in the pilot task wrappers. Reusable prompt files
contain no S1-specific words, images, coalitions, hooks, or expected findings.
