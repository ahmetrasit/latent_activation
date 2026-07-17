# V6 Input and Task Template

## Model

Use:

```text
MODEL: gpt-5.6-sol
REASONING_EFFORT: max
SERVICE_TIER: unset
```

Keep the same model and reasoning setting for every agent and continuation.

## Required Inputs

Reuse a prepared V3 evidence package during the prompt pilot:

```text
passage-arabic.txt
morphology.tsv
syntax.tsv
lexical-branches.jsonl
primary-scaffold.md
```

An optional Turkish listener-context file may later supply approved public
context and preferred terminology. Do not introduce it during a matched pilot
unless both compared workflows receive the same file.

## Output Paths

```text
A1_DISCOVERY:
A1_RESURRECTED:
A1_INTEGRATED:
A1_GOLD_SYNTHESIS:
A2_NARRATIVE_ARCHITECTURE:
A3_PUBLICATION:
A3_AUDIO_PUBLICATION:
```

## Turn 1: Fresh Agent 1

```text
Read and execute:
[V6_ROOT]/01_brave_discovery.md

You are Agent 1, the semantic author for Turns 1-4. Remain in this same
session for every continuation. Do not spawn subagents.

Use only:
- exact passage: [PATH]
- morphology: [PATH]
- syntax: [PATH]
- lexical branches: [PATH]

The primary scaffold is deliberately withheld.

Write:
[A1_DISCOVERY]
```

## Turn 2: Same Agent 1

```text
Continue as the same semantic author.

Read and execute:
[V6_ROOT]/02_coalition_resurrection.md

Use the complete live state from Turn 1 and:
- Turn 1 notebook: [A1_DISCOVERY]
- exact passage: [PATH]
- morphology: [PATH]
- syntax: [PATH]
- lexical branches: [PATH]

Write:
[A1_RESURRECTED]
```

## Turn 3: Same Agent 1

```text
Continue as the same semantic author.

Read and execute:
[V6_ROOT]/03_scaffold_integration.md

The primary scaffold is now available for the first time.

Use:
- resurrected discovery: [A1_RESURRECTED]
- primary scaffold: [PATH]
- exact passage: [PATH]
- morphology: [PATH]
- syntax: [PATH]
- lexical branches: [PATH]

Write:
[A1_INTEGRATED]
```

## Turn 4: Same Agent 1

```text
Continue as the same semantic author.

Read and execute:
[V6_ROOT]/04_gold_synthesis.md

Use:
- integrated discovery: [A1_INTEGRATED]
- resurrected discovery: [A1_RESURRECTED]
- primary scaffold: [PATH]
- exact passage: [PATH]
- morphology: [PATH]
- syntax: [PATH]
- lexical branches: [PATH]

Write:
[A1_GOLD_SYNTHESIS]
```

## Turn 5: Fresh Agent 2

```text
Read and execute:
[V6_ROOT]/05_narrative_architecture.md

You are a fresh narrative architect. Do not spawn subagents. Do not review,
rescore, weaken, or rediscover the semantic findings.

Use only:
- exact passage: [PATH]
- primary scaffold: [PATH]
- integrated discovery: [A1_INTEGRATED]
- gold synthesis: [A1_GOLD_SYNTHESIS]

Write:
[A2_NARRATIVE_ARCHITECTURE]
```

## Turn 6: Fresh Agent 3

```text
Read and execute:
[V6_ROOT]/06_publication_tr.md

You are the Turkish publication author. Remain in this session for Turn 7. Do
not spawn subagents and do not re-adjudicate the semantic findings.

Use only:
- exact passage: [PATH]
- primary scaffold: [PATH]
- gold synthesis: [A1_GOLD_SYNTHESIS]
- narrative architecture: [A2_NARRATIVE_ARCHITECTURE]
- optional listener context: [PATH or omitted]

Write:
[A3_PUBLICATION]
```

## Turn 7: Same Agent 3

```text
Continue as the same Turkish publication author.

Read and execute:
[V6_ROOT]/07_audio_recomposition.md

Use:
- written publication: [A3_PUBLICATION]
- exact passage: [PATH]
- primary scaffold: [PATH]
- gold synthesis: [A1_GOLD_SYNTHESIS]
- narrative architecture: [A2_NARRATIVE_ARCHITECTURE]

Write:
[A3_AUDIO_PUBLICATION]
```

## Pilot Discipline

During a matched prompt pilot:

- do not show any agent the gold reference or prior V6 output;
- do not inject operator evaluations between turns;
- do not replace a continuation agent after it has begun its assigned session;
- preserve every generated artifact, including failed outputs;
- evaluate the written and audio-oriented publications only after Turn 7.
