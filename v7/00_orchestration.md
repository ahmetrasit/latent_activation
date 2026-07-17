# V7 Production Semantic Orchestration

## Objective

Produce a canonical semantic master in which secondary, non-mainstream lexical
resonances form from a closed supplied field, strengthen one another through
recursive rereading, and reveal new dimensions of the passage's direct
contextual meaning.

The output is a discovery and synthesis artifact. Publication voice,
target-language polish, listening cadence, and TTS rendering are separate
downstream work.

## Runtime

Use native agent sessions with:

```text
model: gpt-5.6-sol
reasoning effort: max
service tier: unset
```

Start both agents without inherited operator conversation. Do not use prior
outputs, gold references, translations, commentary, or model memory as run
inputs. Do not let either production agent spawn another agent.

## Authorized input bundle

Reuse one prepared V3 bundle for the exact passage scope:

```text
inputs/passage-arabic.txt
inputs/morphology.tsv
inputs/syntax.tsv
inputs/lexical-branches.jsonl
inputs/primary-scaffold.md
```

Turns 1 and 2 do not receive `primary-scaffold.md`. It enters in Turn 3.

## Production sequence

### Agent 1: persistent formation session

1. `01_activation_reservoir.md`
2. `02_recursive_formation_maturation.md`
3. `03_reciprocal_primary_integration.md`

Turn 2 continues the session from Turn 1. Turn 3 continues the same session
and receives the primary scaffold for the first time. Agent 1 keeps incomplete
material available for later recruitment and lets completed formations change
the force of their own earlier pieces.

### Agent 2: fresh independent synthesis session

4. `04_independent_mechanism_recomposition.md`
5. `05_semantic_master_tr.md`

Agent 2 starts without Agent 1's conversational state. It receives the full
raw bundle, primary scaffold, activation reservoir, and reciprocal field. It
must read the raw field before either Agent 1 artifact and construct its own
topology first. Agent 1's artifacts are generative material, not a ceiling,
scorecard, or canonical grouping.

Turn 5 continues Agent 2's session and writes the canonical semantic master.
No third agent is required for the production semantic workflow.

## Production artifacts

For semantic prompt version `<version>`, use version-bearing filenames:

```text
a1/01-activation-reservoir-<version>.md
a1/02-mature-formations-<version>.md
a1/03-reciprocal-field-<version>.md
a2/04-independent-mechanism-map-<version>.md
a2/05-semantic-master-tr-<version>.md
```

The last file is the canonical production deliverable. The preceding artifacts
preserve the cognitive route and make prompt versions reproducible; they are
not competing final outputs.

## Semantic output contract

This contract guides authorship. It is not a validator or admission gate.

The semantic master should make the following reconstructable in prose:

- the exact passage carrier or carrier set;
- the unexpected supplied facet that becomes active;
- the differentiated role it performs with surrounding material;
- any retroactive strengthening after the larger formation is complete;
- the new consequence produced by interaction between formations;
- the resulting change in how the direct passage is heard.

Several resonances of one lexical field may remain simultaneously active when
they perform different roles. Do not select one as the hidden true sense. Do
not downgrade a completed formation because one part began weakly. Do not
reduce the task to branch coverage, thematic similarity, or disambiguation.

Length is not a semantic criterion. Additional material is valuable when it
forms a differentiated operation, strengthens another formation, or changes
the primary reading. Repetition or editorial roughness can be handled in a
later publication fork.

## Optional downstream fork

A publication workflow may start a fresh author from only:

```text
passage-arabic.txt
primary-scaffold.md
a2/05-semantic-master-tr-<semantic-version>.md
```

That author may perform narrative ordering, target-language rendering,
editorial revision, or TTS adaptation. Those changes receive their own prompt
and output version. They do not alter the accepted semantic master and do not
cause Turns 1-5 to rerun.

V7.4.1 is a recorded example of this optional fork.

## Version discipline

1. Create an immutable prompt directory for the new semantic version.
2. Create matching versioned task wrappers and output paths.
3. Commit the prompt version before running it.
4. Run Turns 1-5 without operator steering between turns.
5. Preserve and commit the resulting versioned outputs.
6. If a semantic prompt changes, create a new version instead of editing the
   version that produced existing outputs.
7. Version downstream editorial prompts independently from the frozen semantic
   baseline.

No semantic audit or validator is part of this workflow. Prompt evolution is
based on deep reading of complete pilot outputs and whether their formed
resonances produce stronger, more coherent primary understanding.
