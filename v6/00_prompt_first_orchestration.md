# GSLS V6 Prompt-First Orchestration

## Objective

Produce a passage-scale lexical synthesis that is exploratory enough to
develop surprising role-complete coalitions and composed enough to become
natural Turkish for both reading and sustained listening.

V6 is a prompt pilot. The semantic and editorial behavior is under test; no
new validation or audit layer is part of this version.

## Model Contract

Use `gpt-5.6-sol` with reasoning effort `max` for every turn.

- Leave service tier unset.
- Do not use a priority tier.
- Do not let any production agent spawn subagents.
- Preserve the required session continuity.
- Do not steer an agent while it is reasoning.

## Evidence Boundary

Use only the files named in each task.

The gold reference, prior publications, operator evaluations, translations,
the `v1/` through `v5/` prompt packages, and remembered conventional
interpretations are not production evidence.

The primary scaffold enters only in Turn 3. Turns 1 and 2 deliberately explore
the passage and supplied lexical branches before a direct scaffold can become
a premature local-sense gate.

## Intellectual Flow

```text
branch facets and passage cues
  -> brave live discoveries
  -> coalition resurrection
  -> contextual coexistence
  -> gold synthesis
  -> narrative architecture
  -> continuous Turkish publication
  -> audio-oriented recomposition
```

## Turns and Sessions

| Turn | Session | Prompt | Output |
| --- | --- | --- | --- |
| 1 | fresh Agent 1 | `01_brave_discovery.md` | `a1/discovery.md` |
| 2 | same Agent 1 | `02_coalition_resurrection.md` | `a1/discovery-resurrected.md` |
| 3 | same Agent 1 | `03_scaffold_integration.md` | `a1/discovery-integrated.md` |
| 4 | same Agent 1 | `04_gold_synthesis.md` | `a1/gold-synthesis.md` |
| 5 | fresh Agent 2 | `05_narrative_architecture.md` | `a2/narrative-architecture.md` |
| 6 | fresh Agent 3 | `06_publication_tr.md` | `a3/publication.md` |
| 7 | same Agent 3 | `07_audio_recomposition.md` | `a3/publication-audio.md` |

## Agent 1: Semantic Continuity

Agent 1 remains the sole semantic author through Turns 1-4.

This is the main V6 correction. GPT models often become more conservative when
a fresh agent encounters another model's exploratory finding. The fresh agent
mistakes novelty for weakness, literal surface absence for negative evidence,
or a secondary branch for an alternative translation. Keeping one semantic
author prevents that handoff loss.

Turn 2 is a mandatory resurrection search, not a review. Turn 3 introduces the
scaffold as a direct foundation without reopening the discovered field for
routine downgrading. Turn 4 writes the strongest coherent synthesis supported
by the live field.

## Agent 2: Architecture Without Adjudication

Agent 2 receives the exact passage, scaffold, integrated discovery, and gold
synthesis. It does not receive a mandate to check whether the findings are
reasonable.

Its task is editorial:

- find the central curiosity or tension;
- group discoveries into a small number of developing movements;
- preserve independent channels without giving each observation a separate
  subsection;
- decide where a concrete image, delayed reveal, callback, or reversal creates
  recognition;
- make the ending earn a changed hearing of the opening.

Agent 2 may compress exposition and combine related material. It may not
weaken, reject, rescore, or replace the semantic findings.

## Agent 3: Publication Before Segmentation

Agent 3 receives the exact passage, direct scaffold, gold synthesis, and
narrative architecture.

Turn 6 writes the publication as one composed work. It must not think in JSONL
records, TTS chunks, finding quotas, or evidence discharge units.

Turn 7 begins only after the publication exists. The same author recomposes it
for listening by adjusting transitions, sentence cadence, paragraph length,
Arabic introductions, and spoken headings. It does not summarize or reduce the
work.

## Prompt-Development Rule

Do not patch a failed output by adding another isolated prohibition to the
publication prompt. Diagnose whether the failure arose from:

- semantic premature closure;
- weak narrative architecture;
- Turkish composition;
- or audio segmentation.

Revise the prompt responsible for that layer. V6 deliberately keeps these
responsibilities separate.

## Pilot Evaluation

For the initial prompt pilot, inspect only:

- whether important V3 and gold-like opportunities survive semantic synthesis;
- whether the narrative has a developing spine rather than a finding catalog;
- whether the Turkish sounds authored rather than rendered;
- whether the audio version remains intelligible and engaging in one pass.

Do not add validators or formal gates until the prompt architecture shows a
clear qualitative gain on S1 and at least one compact canary.
