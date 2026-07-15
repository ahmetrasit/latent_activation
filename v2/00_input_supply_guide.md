# Input Supply Guide

**Workflow:** `GSLS-3A-2.0`

## 1. Required operator inputs

### 1.1 Passage and scope

Supply:

```text
PASSAGE_ID
SURAH
AYAH_START
AYAH_END
BASMALA_POLICY
EXACT_ARABIC_SOURCE
OUTPUT_LANGUAGE
PRIMARY_PRODUCT
OPTIONAL_PRODUCT
```

`passage-arabic.txt` must preserve exact characters, ayah boundaries, and any opening context that is in scope.

### 1.2 Primary scaffold

`primary-scaffold.md` must state only the direct contextual layer:

- primary propositions;
- participants;
- speaker and addressee;
- grammatical roles;
- explicit source–recipient or agent–patient relations;
- clause and ayah order;
- established ambiguities;
- exact primary glosses where authorized.

Do not place the desired secondary synthesis, the gold answer, or external commentary in this file.

### 1.3 Positioned morphology

Recommended `morphology.tsv` columns:

```text
surah
ayah
word_index
morpheme_index
surface_ar
lemma_ar
root_ar
root_norm
pos
morpheme_role
morph_features
aspect
mood
voice
measure
person
number
gender
```

Every rooted occurrence in the passage must be represented.

### 1.4 Syntax or attachments

Recommended `syntax.tsv` columns:

```text
edge_id
source_position
target_position
edge_type
direction
confidence
annotation_source
exact_surface_span
```

If a syntax class is unavailable, declare it unavailable. Do not let the model silently re-derive an absent verified resource.

### 1.5 Clean lexical branch inventory

Supply `lexical-branches.jsonl` or a database plus an exact read-only query contract.

Required information per source branch:

```text
root_norm
branch_id
source_id
source_name
source_entry_id
source_ar_exact
branch_image_ar
what_is_ar
lexical_unit_or_form
derivation_or_pattern
status
contaminated
editorial_notes
```

For a Maqāyīs-based dictionary enriched by Tahdhīb, Ṣiḥāḥ, Mufradāt, and Jamharah:

- preserve each source separately;
- preserve exact Arabic source prose;
- do not merge sources into one synthetic gloss;
- preserve source agreement and disagreement;
- include every accepted branch for every passage root;
- do not rank branches as primary or secondary in the input.

A missing branch is an evidence-availability failure, not an inactive branch.

### 1.6 Source manifest

Supply both:

- `source-manifest.json`, validated by schema;
- `source-manifest.md`, readable by agents.

Declare:

- authorized sources;
- prohibited sources;
- file paths;
- source versions;
- contamination policy;
- exact-query contracts;
- whether discourse, network, acoustic, and control channels are available;
- which agent may read each source.

### 1.7 Run card

Supply both:

- `run-card.json`;
- `run-card.md`.

Declare:

```text
WORKFLOW_ID
RUN_ID
PASSAGE_ID
SCOPE
BASMALA_POLICY
OUTPUT_LANGUAGE
AGENT_LIMIT: 3
AGENT_A_SESSION_POLICY
PRODUCTION_MODE
LEXICON_POLICY
NETWORK_USE_POLICY
EXTERNAL_EVIDENCE_POLICY
GOLD_QUARANTINE
OUTPUT_PATHS
```

## 2. Optional inputs

### 2.1 Discourse evidence

Useful for:

- pronoun resolution;
- speaker/addressee continuity;
- oath scope;
- exception scope;
- participant changes;
- cross-ayah dependencies;
- opening/closing relations.

### 2.2 Acoustic and recitational evidence

May include:

- exact repetition;
- rhyme or ending pattern;
- pause positions;
- recitation grouping;
- verified sound correspondences.

Sound resemblance is corroborative unless a lexical or structural relation independently supports it.

### 2.3 Semantic network

A semantic network may route attention only.

Recommended fields:

```text
network_id
node_branch_ids
edge_branch_ids
documented_edge_type
routing_score
hidden_label_omitted
```

Do not supply thematic labels to production agents. Topology is never semantic proof.

### 2.4 Controls

Useful controls:

- shuffled passage order;
- matched passages with similar roots;
- branch or root base-rate statistics;
- held-out later cues;
- control roots;
- independent seed convergence.

### 2.5 Human adjudication notes

Supply only when source prose is genuinely ambiguous. Human notes must name the exact evidence dispute and may not insert the desired synthesis.

## 3. Information supplied to Agent A

Agent A receives:

- run card;
- source manifest;
- passage;
- primary scaffold;
- full morphology;
- full syntax and available discourse;
- complete clean branch inventory;
- optional retrieval-only network;
- optional controls;
- current Agent A state during continuation;
- Agent B audit during adjudication only.

Agent A must never receive the gold during production.

## 4. Information supplied to Agent B

Agent B receives:

- the same clean evidence supplied to Agent A;
- all frozen Agent A draft artifacts;
- deterministic coverage and hash indexes.

Agent B does not receive:

- gold;
- prior evaluations;
- prior prose;
- Agent C outputs;
- unlisted external commentary.

## 5. Information supplied to Agent C

Agent C receives:

- run card;
- exact passage;
- final gold manifest;
- final gold notebook;
- render policy;
- output language and audience.

Agent C does not receive raw unused branch inventories unless the final manifest explicitly points to an evidence sidecar needed for faithful wording. Agent C is not a discovery agent.

## 6. Minimal complete package

```text
inputs/
  source-manifest.json
  source-manifest.md
  run-card.json
  run-card.md
  passage-arabic.txt
  primary-scaffold.md
  morphology.tsv
  syntax.tsv
  lexical-branches.jsonl
```

A run without complete lexical branches is not a complete gold-synthesis run.

## 7. Input quality checks

Before dispatch:

- no required file is missing or zero bytes;
- every passage root has branch coverage;
- every branch has exact source prose;
- passage positions align across text and morphology;
- syntax edges point to existing positions;
- no gold/evaluation path is readable;
- hashes are recorded;
- source versions are declared.

## 8. What not to supply

Do not place these in a production-readable directory:

- `bulgular.md`;
- gold excerpts;
- evaluation reports;
- target-specific prompt demonstrations;
- prior target outputs;
- hidden network labels;
- tafsir, hadith, translations, or commentary unless explicitly authorized as an evidence class.

## 9. Output policy information

The operator must state:

```text
GOLD_NOTEBOOK_LANGUAGE
NOTEBOOK_REGISTER
PUBLICATION_ESSAY_REQUIRED: yes | no
PUBLICATION_AUDIENCE
PUBLICATION_LANGUAGE
PUBLICATION_LENGTH_POLICY
CONDITIONAL_FINDINGS_POLICY
```

The final gold notebook is complete regardless of whether a publication essay is requested.
