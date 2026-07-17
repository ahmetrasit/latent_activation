# GSLS V7

V7 is a prompt-only workflow for forming and synthesizing latent lexical
resonances from a closed supplied field. Initially slight associations may
recruit surrounding material, become complete formations, and send new force
back into the passage's direct contextual meaning.

The frozen workflow has two versioned components:

```text
V7.4.0 Tasks 1-5  semantic discovery and synthesis
V7.4.1 Tasks 6-8  fresh rendering of the semantic synthesis
```

V7.4.1 does not replace V7.4.0. It consumes the V7.4.0 semantic master.

## Current operating rule

Run the complete V7.4.0 plus V7.4.1 sequence while generalizing the workflow to
new passages. The semantic master remains the authority, but the rendered essay
is needed to reveal whether the master supports one coherent account rather
than only an analytical inventory.

Judge the render for semantic transport:

- do formed resonances survive the handoff;
- do their differentiated roles remain audible;
- do interactions still alter the direct reading;
- can one governing synthesis organize the passage without flattening smaller
  formations?

Do not use word count, recurring provenance phrases, editorial elegance,
target-language polish, or TTS performance to judge the semantic workflow.
Those surfaces can be revised later without rerunning discovery.

## Frozen components

The semantic component is V7.4.0, Tasks 1-5:

```text
v7/prompts/v7.4.0/01_activation_reservoir.md
v7/prompts/v7.4.0/02_recursive_formation_maturation.md
v7/prompts/v7.4.0/03_reciprocal_primary_integration.md
v7/prompts/v7.4.0/04_independent_mechanism_recomposition.md
v7/prompts/v7.4.0/05_semantic_master_tr.md
```

The rendering component is V7.4.1, Tasks 6-8:

```text
v7/prompts/v7.4.1/06_oral_narrative_rehearsal.md
v7/prompts/v7.4.1/07_canonical_publication_tr.md
v7/prompts/v7.4.1/08_dual_medium_revision.md
```

Neither prompt set should be edited. A semantic change requires a new semantic
version. A later editorial change can receive its own rendering version without
changing V7.4.0.

## Cognitive flow

```text
closed supplied lexical field
  -> Agent 1 activation reservoir
  -> recursive formation maturation
  -> reciprocal integration with the primary scaffold
  -> fresh Agent 2 raw-field topology
  -> independent mechanism recomposition
  -> canonical Turkish semantic master
  -> fresh Agent 3 oral narrative rehearsal
  -> complete Turkish publication draft
  -> rendered canonical essay
```

The primary scaffold is withheld until Agent 1's third turn. Agent 2 starts
fresh and rereads the raw field before opening Agent 1's artifacts. Agent 3
starts fresh from only the exact passage, primary scaffold, and semantic
master. These boundaries prevent the first author's hierarchy from becoming a
ceiling and prevent the renderer from returning to raw branch selection.

## Semantic objective

This is not disambiguation. The direct contextual meaning remains the primary
subject while several secondary, non-mainstream resonances remain active at
once. A useful formation gives supplied facets differentiated roles around
exact passage carriers, lets them strengthen one another, and changes how the
direct passage is heard.

A branch that looks slight in isolation may become central after the
surrounding formation is complete. Do not downgrade a completed formation
because one component began weakly. Additional resonance is valuable when it
forms a distinct operation, strengthens another formation, or shifts the
primary reading.

## Native sessions

Run every turn with `gpt-5.6-sol` at reasoning effort `max`. Leave service tier
unset.

- Agent 1 remains in one session for Tasks 1-3.
- Agent 2 starts fresh and remains in one session for Tasks 4-5.
- Agent 3 starts fresh and remains in one session for Tasks 6-8.
- No production agent spawns subagents.
- Do not steer an agent between turns in its persistent session.

## Specifications

- `00_orchestration.md` defines the cognitive and interpretive contract.
- `01_composite_run_spec.md` is the operator-ready, passage-agnostic execution
  specification.

## Reference pilot

The complete S001 reference run is split across the two frozen components:

```text
v7/run/s001-pilot-20260716/v7.4.0/
v7/run/s001-pilot-20260716/v7.4.1/
```

Its principal outputs are:

```text
v7.4.0/a2/05-semantic-master-tr-v7.4.0.md
v7.4.1/1-publication-tr-v7.4.1.md
```

## Version discipline

Prompt versions are immutable after they have produced a run. Every task and
output filename includes its component version. A prompt change creates a new
version directory and a commit before the next model run. New passage bindings
reuse the frozen prompts through versioned task wrappers; they do not copy or
modify prompt text.

The S001 binding exists only in its task wrappers. Reusable prompt files contain
no S1-specific word, image, coalition, hook, or expected finding.
