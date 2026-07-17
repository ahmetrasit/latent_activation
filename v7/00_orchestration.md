# V7.4 Composite Orchestration

## Objective

Produce a canonical semantic master in which secondary, non-mainstream lexical
resonances form from a closed supplied field, strengthen one another through
recursive rereading, and reveal new dimensions of the passage's direct
contextual meaning. Then give that master to a fresh author so its synthesis is
rendered as one continuous Turkish account.

The rendering turn is part of current generalization runs because it makes the
quality of integration observable. It is not a new source of semantic
authority and it is not an editorial or TTS acceptance test.

## Frozen version composition

```text
semantic component:  v7.4.0, Tasks 1-5
rendering component: v7.4.1, Tasks 6-8
```

V7.4.1 begins only after V7.4.0 has produced its semantic master. The two
components keep independent version numbers so later editorial work cannot
silently change the accepted semantic prompts.

## Runtime

Use native agent sessions with:

```text
model: gpt-5.6-sol
reasoning effort: max
service tier: unset
```

Start every agent without inherited operator conversation. Do not use prior
outputs, gold references, translations, commentary, or model memory as run
inputs. Do not let any production agent spawn another agent.

## Authorized input bundle

Reuse one prepared V3 bundle for the exact passage scope:

```text
inputs/passage-arabic.txt
inputs/morphology.tsv
inputs/syntax.tsv
inputs/lexical-branches.jsonl
inputs/primary-scaffold.md
```

Tasks 1 and 2 do not receive `primary-scaffold.md`. It enters in Task 3.

## Agent 1: persistent formation session

1. `v7.4.0/01_activation_reservoir.md`
2. `v7.4.0/02_recursive_formation_maturation.md`
3. `v7.4.0/03_reciprocal_primary_integration.md`

Task 2 continues the session from Task 1. Task 3 continues the same session and
receives the primary scaffold for the first time. Agent 1 keeps incomplete
material available for later recruitment and lets completed formations change
the force of their own earlier pieces.

## Agent 2: fresh independent synthesis session

4. `v7.4.0/04_independent_mechanism_recomposition.md`
5. `v7.4.0/05_semantic_master_tr.md`

Agent 2 starts without Agent 1's conversational state. It receives the full raw
bundle, primary scaffold, activation reservoir, and reciprocal field. It reads
the raw field before opening either Agent 1 artifact and constructs its own
topology first. Agent 1's artifacts are generative material, not a ceiling,
scorecard, or canonical grouping.

Task 5 continues Agent 2's session and writes the canonical semantic master.
The semantic master is the authority for every downstream rendering decision.

## Agent 3: fresh persistent rendering session

6. `v7.4.1/06_oral_narrative_rehearsal.md`
7. `v7.4.1/07_canonical_publication_tr.md`
8. `v7.4.1/08_dual_medium_revision.md`

Agent 3 receives only the exact passage, primary scaffold, and V7.4.0 semantic
master. It does not receive the raw lexical branches, morphology, syntax,
formation reservoir, mechanism map, prior publication, or gold reference.

Tasks 7 and 8 continue the same session as Task 6. The rehearsal discovers a
human route through the master, the draft renders that route, and the final
turn revises the whole account. Agent 3 may organize and articulate established
meaning but may not reopen branch discovery or narrow simultaneous resonances
into disambiguation.

## Artifact roles

The composite run produces:

```text
v7.4.0/a1/01-activation-reservoir-v7.4.0.md
v7.4.0/a1/02-mature-formations-v7.4.0.md
v7.4.0/a1/03-reciprocal-field-v7.4.0.md
v7.4.0/a2/04-independent-mechanism-map-v7.4.0.md
v7.4.0/a2/05-semantic-master-tr-v7.4.0.md
v7.4.1/a3/06-oral-rehearsal-tr-v7.4.1.md
v7.4.1/a3/07-publication-draft-tr-v7.4.1.md
v7.4.1/<passage-id>-publication-tr-v7.4.1.md
```

The semantic master is the canonical discovery artifact. The last file is the
canonical rendering of that master for the run. The rehearsal and draft retain
the publication session's route but are not competing semantic authorities.

## Semantic contract

This contract guides deep reading. It is not a validator or admission gate.

The semantic master should make the following reconstructable:

- the exact passage carrier or carrier set;
- the unexpected supplied facet that becomes active;
- the differentiated role it performs with surrounding material;
- retroactive strengthening after the larger formation becomes complete;
- new consequences produced by interactions between formations;
- the resulting change in how the direct passage is heard.

Several resonances of one lexical field may remain simultaneously active when
they perform different roles. Do not select one as the hidden true sense. Do
not downgrade a completed formation because one part began weakly. Do not
reduce the task to branch coverage, thematic similarity, or disambiguation.

## Why the rendering is required now

The semantic master is already readable Turkish analysis, but its analytical
structure can conceal whether the discoveries form one intelligible account.
A fresh Agent 3 provides a stronger observation:

- a governing formation must organize a continuous route;
- autonomous formations must retain their distinct contribution;
- passage-wide interactions must survive outside the research structure;
- the direct meaning must emerge changed rather than merely accompanied by a
  branch inventory.

Read the semantic master first and the final rendering second. Use both to
understand the synthesis. Do not judge the semantic workflow by the render's
length, repeated provenance language, stylistic elegance, target-language
finish, or TTS cadence.

## Interpreting outcomes

If the semantic master and rendering both preserve differentiated formations
and a changed primary reading, continue rolling out the frozen composite.

If the semantic master is strong but the rendering loses formations or
connections, the issue is downstream handoff or editorial treatment. Do not
create V7.5 for that reason.

If the semantic master itself repeatedly produces branch piles, loses
retroactive strengthening, or fails to change the direct reading across new
passages, then a new semantic version may be warranted. One local or
passage-specific weakness is not sufficient reason to change the architecture.

## Version discipline

1. Bind a prepared passage bundle through new task wrappers.
2. Keep semantic prompts fixed at V7.4.0 and rendering prompts fixed at V7.4.1.
3. Commit the task binding before running agents.
4. Run Tasks 1-8 without operator steering inside persistent sessions.
5. Commit every versioned output after the corresponding component completes.
6. Never edit a prompt version that has already produced output.
7. Use a new semantic version only for a semantic cognitive change.
8. Use a new rendering version only for downstream authorship or editorial
   changes.

No automated semantic audit, validator, confidence grading, or word-count gate
is part of this workflow. The operator-ready binding and execution details are
specified in `01_composite_run_spec.md`.
