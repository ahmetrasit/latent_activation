# GSLS V3 Orchestration Specification

## Objective

Produce a gold-level Turkish synthesis in which accepted Arabic root branches form passage-specific coalitions, governing channels, spatial or sensory axes, transformations, rings, and retrospective activations. The synthesis must explain why the passage uses these words, in this order, and why it closes where it does while preserving its direct contextual meaning.

This is open-ended linguistic discovery. The prompts guide attention and composition; they are not compliance checklists.

## Whole-passage rule

The workflow moves in this direction:

```text
local lexical discoveries
  -> cross-root coalitions
  -> governing channels and interacting axes
  -> whole-passage activation field
  -> Turkish synthesis
```

It must never move from pericope summaries to a stitched passage summary. Ayah or pericope boundaries may reveal a transition, contrast, delay, return, or closure, but they are not independent composition containers. Local findings may remain visible at medium or weak confidence without becoming section commentary.

## Evidence

Prepared inputs are:

```text
inputs/passage-arabic.txt
inputs/morphology.tsv
inputs/syntax.tsv
inputs/lexical-branches.jsonl
inputs/primary-scaffold.md
```

The lexical records contain exactly `root_id`, `root_norm`, `branch_id`, `what_is_ar`, `branch_image_ar`, and `source_phrase_ar`. Preparation reads `resources/furuq_v4.sqlite` and emits only accepted branches whose contamination value is exactly `no`.

The gold reference, prior outputs, translations, the `v1/` tree, and model memory are not production evidence.

## Flow

### Turn 1: A1 discovery

A fresh high-depth agent reads the passage, positioned morphology, local syntax, and complete lexical inventory. It follows the passage forward, gives every supplied branch one attentive reading, develops specific coalitions selectively, and then performs a backward replay. It writes:

```text
a1/discovery.md
```

The primary scaffold is not supplied during this turn.

### Turn 2: A1 scaffold integration

The same A1 session receives the independent direct scaffold. It preserves the discoveries, places them against the contextual proposition, and rewrites the notebook as a whole-passage discovery field:

```text
a1/discovery-integrated.md
```

The scaffold grounds contextual meaning. It does not impose a local-sense gate on secondary root resonance.

### Turn 3: A2 mechanism map

A fresh high-depth agent receives the integrated discovery, scaffold, exact passage, and prepared linguistic evidence. Before writing publication prose, it constructs the passage-scale mechanism:

```text
a2/mechanism-map.md
```

The map preserves central, medium, weak, conditional, rival, and incomplete material when each contributes a real lexical or compositional insight.

### Turn 4: A2 Turkish publication

The same A2 session turns the mechanism map into the final work:

```text
publication.md
```

The publication uses labeled finding paragraphs and a final ordered replay. It is not organized by ayah, pericope, or section.

## Confidence language

The final synthesis uses two separate dimensions:

- `GÜÇLÜ / ORTA / ZAYIF`: how explicitly the supplied lexical record supports the branch image used in the finding.
- `A / B / C / C-koşullu`: how strongly the passage activates that image or coalition.

The first dimension does not claim source chronology, independent dictionary counts, or majority derivational opinion. Those facts are not available in the six-field input.

Activation strength comes from specific cross-root convergence, complementary roles, passage order, adjacency, recurrence, and contribution to the whole. A latent scene does not become weak merely because no surface word names that scene literally. Preserving the direct contextual meaning is sufficient; surface literalization is not an activation requirement.

## Orchestration boundary

The runtime only prepares evidence and emits four task files. It does not score, approve, reject, promote, or close agent work. The operator runs the two continuing agent sessions and decides when a draft is ready for a blind benchmark.
