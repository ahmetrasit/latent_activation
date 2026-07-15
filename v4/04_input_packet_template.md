# Input Packet and Task Template

Fill the variables below and send this packet with `01_constructive_discovery_prompt.md`.

## Task variables

```text
TARGET_PASSAGE:
FINAL_LANGUAGE:
OUTPUT_DIRECTORY:
DISCOVERY_NOTEBOOK_PATH:
GOLD_SYNTHESIS_PATH:
PUBLICATION_PATH:
BASMALA_POLICY:
```

## Required evidence

### 1. Exact passage

Supply the sacred Arabic text with stable positions and ayah boundaries.

Recommended fields:

```text
surah
ayah
word_position
surface_ar
```

### 2. Primary contextual scaffold

Supply a concise, independent direct reading based on the passage's primary contextual meanings. It should state participants, assertions, requests, sequence, and ordinary grammatical relations without secondary branch synthesis.

### 3. Positioned morphology

Supply available positioned fields such as:

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

Empty or unavailable fields should remain empty.

### 4. Verified syntax and discourse

Supply verified edges when available, for example:

```text
edge_id
source_position
target_position
relation
notes
```

Do not ask the agent to reconstruct a missing edge channel as if it were verified.

### 5. Lexical branch inventory

For every accepted, uncontaminated branch of every root occurring in the passage, supply exactly:

```text
root_norm
branch_id
branch_image_ar
what_is_ar
```

`root_norm` and `branch_id` are identifiers only. `branch_image_ar` and `what_is_ar` are the only V4 semantic fields visible to the agent.

Do not supply:

- themes or keywords;
- network labels or edge weights;
- source ratings or dictionary names;
- English glosses;
- editorial notes;
- contamination or status fields;
- preselected local-sense labels;
- confidence scores;
- proposed passage axes;
- prior outputs or a gold exemplar.

## Initial task message

```text
Read and execute:
[ABSOLUTE PATH]/01_constructive_discovery_prompt.md

Remain the same synthesis author for the entire run.

Authorized inputs:
- exact passage: [PATH]
- primary scaffold: [PATH]
- positioned morphology: [PATH]
- verified syntax: [PATH or UNAVAILABLE]
- verified discourse: [PATH or UNAVAILABLE]
- lexical branch inventory: [PATH or BATCH PATH]

Task variables:
- TARGET_PASSAGE: [VALUE]
- FINAL_LANGUAGE: [VALUE]
- DISCOVERY_NOTEBOOK_PATH: [PATH]
- GOLD_SYNTHESIS_PATH: [PATH]
- PUBLICATION_PATH: [PATH]
- BASMALA_POLICY: [VALUE]

Use no other evidence. Write the current discovery notebook to the declared path.
```

## Additional Pass 1 batch message

Use only when the full lexical inventory does not fit at once, and send it in the same session:

```text
CONTINUE PASS 1 WITH THE NEXT AUTHORIZED DOSSIERS.

Read the next complete branch-dossier batch at:
[PATH]

Preserve the live models, unresolved roles, and backward reactivations already developed. Integrate these dossiers into the existing constructive search and update the same discovery notebook. Do not restart.
```

## Pass 2 continuation message

Send in the same session after all authorized branch dossiers have been delivered:

```text
Read and execute:
[ABSOLUTE PATH]/02_gold_synthesis_continuation.md

Continue as the same synthesis author. Every authorized lexical dossier has now been supplied. Use the live Pass 1 state and the original authorized evidence. Write the gold research document to:
[GOLD_SYNTHESIS_PATH]
```

## Pass 3 continuation message

Send immediately afterward in the same session:

```text
Read and execute:
[ABSOLUTE PATH]/03_publication_continuation.md

Continue as the same synthesis author. Write the publication prose in [FINAL_LANGUAGE] to:
[PUBLICATION_PATH]
```
