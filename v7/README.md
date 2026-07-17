# GSLS V7

V7 is a prompt-only workflow for forming and synthesizing latent lexical
resonances from a closed supplied field. Its production deliverable is a
semantic master, not a publication, translation, or text-to-speech script.

The workflow adds no schema, validator, audit agent, confidence score, or
deterministic semantic gate. It gives initially slight associations time to
recruit surrounding material, become complete formations, and send new force
back into the passage's direct contextual meaning.

## Production baseline

The production semantic baseline is V7.4.0, Turns 1-5:

```text
v7/prompts/v7.4.0/01_activation_reservoir.md
v7/prompts/v7.4.0/02_recursive_formation_maturation.md
v7/prompts/v7.4.0/03_reciprocal_primary_integration.md
v7/prompts/v7.4.0/04_independent_mechanism_recomposition.md
v7/prompts/v7.4.0/05_semantic_master_tr.md
```

For the S001 pilot, the canonical semantic output is:

```text
v7/run/s001-pilot-20260716/v7.4.0/a2/05-semantic-master-tr-v7.4.0.md
```

The semantic master preserves the complete discoveries and their passage-wide
interactions. It is intentionally allowed to retain analytical and provenance
language. Editorial polish can be derived later without rerunning discovery.

## Semantic objective

This is not disambiguation. The direct contextual meaning remains the primary
subject while several secondary, non-mainstream resonances can remain active
at once. They may give different words or repeated words distinct operational
roles, material realizations, directions, durations, and consequences.

A useful formation does more than collect related branches. Its supplied
facets perform differentiated roles around exact passage carriers, alter one
another through interaction, and strengthen or shift how the direct passage is
heard. A branch that looks slight in isolation may become central after the
surrounding formation is complete.

## Cognitive flow

```text
closed supplied lexical field
  -> Agent 1 activation reservoir
  -> recursive formation maturation
  -> reciprocal integration with the primary scaffold
  -> fresh Agent 2 raw-field topology
  -> independent mechanism recomposition
  -> canonical semantic master
```

The primary scaffold is withheld until Agent 1's third turn. Agent 2 then
starts fresh and rereads the raw field before opening Agent 1's artifacts. This
preserves both recursive maturation and independent recomposition: Agent 1 can
let weak pieces strengthen over time, while Agent 2 is not trapped inside the
first author's hierarchy.

## Native sessions

Run every turn with `gpt-5.6-sol` at reasoning effort `max`. Leave service tier
unset.

- Agent 1 remains in one session for Turns 1-3.
- Agent 2 starts fresh and remains in one session for Turns 4-5.
- Neither production agent spawns subagents.

See `00_orchestration.md` for the exact runbook and artifact contract.

## Optional editorial fork

Publication, target-language styling, listening cadence, and TTS adaptation are
downstream forks from the frozen semantic master. They are not semantic
acceptance criteria and do not require the formation or synthesis turns to run
again.

V7.4.1 records one such publication experiment:

```text
v7/run/s001-pilot-20260716/v7.4.1/
```

Its result demonstrates that the semantic master can support a continuous
essay. It is not part of the production semantic topology.

## Version discipline

Prompt versions are immutable after they have produced a run:

```text
prompts/<version>/
run/<run-id>/<version>/
```

Every task and output filename includes its version. A prompt change creates a
new version directory and a commit before the next model run. Earlier prompts
and outputs remain available for direct comparison. A downstream editorial
fork may advance its own version without changing the frozen semantic version.

## Pilot binding

The pilot binds the prepared V3 S1 evidence package without copying or
altering it:

```text
v3/run/s001-full-20260716/inputs/
```

That binding exists only in pilot task wrappers. Reusable prompt files contain
no S1-specific word, image, coalition, hook, or expected finding.
