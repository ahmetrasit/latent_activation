# Same-Agent Orchestration

## Governing design

Use one persistent semantic agent as the sole interpreter and author. Do not hand the work to a critic, adjudicator, manifest editor, QC reviewer, or separate renderer.

The workflow has three stateful passes, all in the same conversation or logical agent session:

```text
Pass 1 — constructive discovery and backward reactivation
Pass 2 — gold-standard synthesis
Pass 3 — publication prose
```

These are continuation prompts, not separate agents. The agent that discovers the relations must remain the agent that decides the passage architecture and writes the prose.

## Deterministic orchestration duties

The orchestrator may do only the following:

- prepare the authorized input packet;
- restrict Furūq v4 extraction to the permitted fields;
- deliver lexical dossiers in complete batches when the full inventory does not fit at once;
- preserve the same agent session across all batches and passes;
- track mechanically which branch records have been delivered;
- save the agent's Markdown outputs;
- verify that quoted Arabic spans occur exactly in the supplied passage or branch prose.

The orchestrator must not approve, suppress, downgrade, rank, rewrite, or delete semantic claims.

## V4 access boundary

For each accepted, uncontaminated passage-root branch, expose only:

```text
root_norm          # identifier only
branch_id          # identifier only
branch_image_ar    # semantic evidence
what_is_ar         # semantic evidence
```

Filtering by acceptance and contamination happens outside the agent. Do not expose status fields, source ratings, themes, keywords, network labels, English glosses, editorial notes, provenance summaries, hidden taxonomies, confidence labels, or other V4 columns.

## Input order

At the start of Pass 1, supply:

1. exact sacred Arabic passage with positions and ayah boundaries;
2. recitational opening context and basmala policy, when applicable;
3. an independent primary contextual scaffold;
4. positioned morphology;
5. verified syntax and discourse edges, when available;
6. the complete lexical branch inventory for every passage root under the V4 access boundary.

Do not supply a gold answer, exemplar, evaluation, prior synthesis, thematic network, keyword hierarchy, or proposed hidden architecture.

## Large inventories

When the complete branch inventory cannot fit safely in one context:

1. start Pass 1 with the passage, scaffold, morphology, syntax, and the first complete root-dossier batch;
2. keep the same agent session;
3. send further complete root dossiers with the instruction `CONTINUE PASS 1 WITH THE NEXT AUTHORIZED DOSSIERS`;
4. never summarize or replace a dossier with keywords;
5. do not begin Pass 2 until every authorized branch dossier has been delivered and the agent has completed backward replay.

The agent may update one concise live notebook after each batch. Do not require a disposition table for every branch.

## Pass sequence

### Pass 1

Send `01_constructive_discovery_prompt.md` with the task variables and authorized inputs. Reuse the same prompt in continuation mode for additional lexical batches.

Expected output:

```text
discovery-notebook.md
```

This is a living synthesis notebook, not a final report and not an audit ledger.

### Pass 2

In the same session, send `02_gold_synthesis_continuation.md`. The agent retains the active models from Pass 1 and may reopen the supplied evidence whenever a higher-order relation exposes a new question.

Expected output:

```text
gold-synthesis.md
```

This is the primary research product.

### Pass 3

Immediately afterward, in the same session, send `03_publication_continuation.md`.

Expected output:

```text
publication.md
```

The publication is written by the same author. It is not generated from a frozen manifest by a constrained renderer.

## Completion rule

The run is complete when the same agent has produced both `gold-synthesis.md` and `publication.md` after receiving the complete authorized evidence.

No semantic audit or adversarial review follows. Mechanical quotation checking may run without changing the analysis.
