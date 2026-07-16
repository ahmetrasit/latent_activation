# V7 Prompt-Only Orchestration

## Objective

Produce a Turkish lexical synthesis in which partial resonances are allowed to
form, recruit one another, and become stronger through recursive rereading.
The final publication must reveal how those mature configurations deepen the
passage's primary contextual meaning while remaining natural both on the page
and through text-to-speech.

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

The first two turns do not receive `primary-scaffold.md`. It enters in Turn 3.

## Agent sequence

### Agent 1: one persistent semantic session

1. `01_activation_reservoir.md`
2. `02_recursive_configuration_maturation.md`
3. `03_reciprocal_primary_integration.md`
4. `04_semantic_master_tr.md`

Turn 2 is a continuation of Turn 1, and Turns 3 and 4 continue the same
session. Never replace conversational continuity with a fresh semantic agent.

### Agent 2: one fresh persistent publication session

5. `05_oral_narrative_rehearsal.md`
6. `06_canonical_publication_tr.md`
7. `07_dual_medium_revision.md`

Agent 2 receives the exact passage, primary scaffold, and semantic master. The
master is its sole semantic authority. It does not receive the reciprocal
working field or raw branch inventory because its task is authorship, not a
return to discovery. Turns 6 and 7 continue the same session as Turn 5.

## Production artifacts

For prompt version `<version>`, use version-bearing filenames:

```text
a1/01-activation-reservoir-<version>.md
a1/02-mature-configurations-<version>.md
a1/03-reciprocal-field-<version>.md
a1/04-semantic-master-tr-<version>.md
a2/05-oral-rehearsal-tr-<version>.md
a2/06-publication-draft-tr-<version>.md
<passage-id>-publication-tr-<version>.md
```

The last file is the canonical production publication. The draft remains as a
trace of the auditory revision; it is not a competing deliverable.

## Version discipline

1. Create a complete immutable prompt directory for the new version.
2. Create matching versioned task wrappers and output paths.
3. Commit the prompt version before running it.
4. Run all turns without operator steering between turns.
5. Preserve and commit the resulting versioned outputs.
6. If prompts change, create a new version rather than editing the version that
   produced existing outputs.

No semantic audit or validator is part of this workflow. Prompt evolution is
based on reading complete pilot outputs and identifying whether the cognitive
sequence and publication behavior moved toward the objective.
