# Input Contract and Same-Agent Task Templates

Use all messages in the same semantic-agent session.

## Task variables

```text
TARGET_PASSAGE:
FINAL_LANGUAGE:
DISCOVERY_NOTEBOOK_PATH:
GOLD_SYNTHESIS_PATH:
PUBLICATION_PATH:
BASMALA_POLICY:
```

## Required evidence

### Exact passage

Supply sacred Arabic with stable positions and ayah boundaries, preferably:

```text
surah
ayah
word_position
surface_ar
```

### Primary contextual scaffold

Supply a concise independent direct reading based only on primary contextual meanings and verified grammar. Include participants, assertions, requests, sequence, and ordinary relations. Do not include secondary synthesis.

### Positioned morphology

Supply available fields such as:

```text
surah
ayah
word_position
surface_ar
root_norm
lemma_ar
part_of_speech
pattern_or_measure
voice
person
number
gender
case_or_mood
```

Unavailable fields remain empty.

### Verified syntax and discourse

Supply verified edges when available:

```text
edge_id
source_position
target_position
relation
notes
```

An unavailable evidence channel remains unavailable; the agent must not present a reconstruction as verified data.

### Lexical branch inventory

For every accepted, uncontaminated branch of every passage root, supply exactly:

```text
root_norm
branch_id
branch_image_ar
what_is_ar
```

Do not supply themes, keywords, networks, hidden labels, edge weights, source ratings, dictionary names, English glosses, editorial notes, status or contamination fields, confidence scores, proposed axes, prior outputs, evaluations, or gold exemplars.

## Pass 1A initial message

```text
Read and execute:
[ABSOLUTE PATH]/01_activation_discovery_prompt.md

Remain the same synthesis author for the entire run.

Authorized inputs:
- exact passage: [PATH]
- primary scaffold: [PATH]
- positioned morphology: [PATH]
- verified syntax: [PATH or UNAVAILABLE]
- verified discourse: [PATH or UNAVAILABLE]
- lexical branch inventory: [PATH or FIRST COMPLETE ROOT-DOSSIER BATCH]

Task variables:
- TARGET_PASSAGE: [VALUE]
- FINAL_LANGUAGE: [VALUE]
- DISCOVERY_NOTEBOOK_PATH: [PATH]
- GOLD_SYNTHESIS_PATH: [PATH]
- PUBLICATION_PATH: [PATH]
- BASMALA_POLICY: [VALUE]

Use no other evidence. Write the living notebook to:
[DISCOVERY_NOTEBOOK_PATH]
```

## Additional Pass 1A dossier batch

Send only when necessary, in the same session:

```text
CONTINUE PASS 1A WITH THE NEXT AUTHORIZED COMPLETE ROOT DOSSIERS.

Read:
[PATH]

Preserve the live activation channels, rivals, incomplete roles, backward
reactivations, and dormant-role reservoir. Integrate the new Arabic prose into
the same constructive search and update:
[DISCOVERY_NOTEBOOK_PATH]

Do not restart from the primary baseline.
```

## Pass 1B continuation

Send only after every authorized branch record has been delivered, in the same session:

```text
ALL AUTHORIZED BRANCH DOSSIERS HAVE NOW BEEN DELIVERED.

Read and execute:
[ABSOLUTE PATH]/02_coalition_resurrection_continuation.md

Continue as the same synthesis author. Perform the mandatory dormant-role,
primary-anchor-first, cross-definition/ring/transition, inversion, and conditional
constellation searches. Rewrite the completed notebook to:
[DISCOVERY_NOTEBOOK_PATH]
```

## Pass 2 continuation

```text
Read and execute:
[ABSOLUTE PATH]/03_gold_synthesis_continuation.md

Continue as the same synthesis author. Use the complete authorized evidence and
completed live discovery state. Write the activation-centered gold research
document to:
[GOLD_SYNTHESIS_PATH]
```

## Pass 3 continuation

```text
Read and execute:
[ABSOLUTE PATH]/04_publication_continuation.md

Continue as the same synthesis author. Write the activation-centered publication
prose in [FINAL_LANGUAGE] to:
[PUBLICATION_PATH]
```
