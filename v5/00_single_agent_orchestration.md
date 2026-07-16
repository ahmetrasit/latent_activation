# Single-Agent Orchestration Specification — Activation-Centered Version

## 1. Identity and continuity

Use one persistent semantic agent as the sole interpreter and author.

The agent must run on `gpt-5.6-sol` with reasoning effort `max` for the
entire orchestration. This requirement applies to every continuation phase,
including resumed or retried passes. Do not downgrade, switch models, or split
the run across agents with different model or reasoning settings.

When spawning or resuming the agent, do not set a service tier or priority tier.
Leave service-tier selection unset/default. The required runtime constraint is
the model and reasoning effort, not a priority override.

The four prompts are continuation phases inside the same conversation or preserved logical state:

```text
Pass 1A — activation discovery
Pass 1B — coalition resurrection
Pass 2  — gold synthesis
Pass 3  — publication prose
```

They are not separate agents. Do not start a fresh semantic session between them. The same author must retain the passage, branch prose, live models, unresolved roles, and backward reactivations.

No critic, reviewer, adjudicator, manifest editor, semantic QC agent, or separate renderer is used.

## 2. What the orchestrator may do

The orchestrator is mechanical only. It may:

- prepare the authorized evidence packet;
- filter accepted and uncontaminated V4 rows before model access;
- expose only the permitted V4 fields;
- deliver complete root dossiers in one or more batches;
- preserve the same agent session across every batch and pass;
- track which authorized branch records have been delivered;
- save the Markdown outputs;
- verify that quoted Arabic spans occur exactly in the authorized passage or branch prose.

The orchestrator must not approve, suppress, rank, reinterpret, merge, delete, or rewrite semantic claims.

## 3. V4 evidence boundary

For each accepted, uncontaminated branch of each passage root, expose only:

```text
root_norm
branch_id
branch_image_ar
what_is_ar
```

`root_norm` and `branch_id` are lookup identifiers, not semantic evidence.

Do not expose themes, keywords, networks, hidden labels, edge weights, English glosses, source ratings, dictionary names, editorial notes, provenance summaries, status fields, contamination fields, confidence scores, or proposed meanings.

## 4. Authorized initial evidence

Supply the validated core evidence packet:

1. exact sacred Arabic with stable word positions and ayah boundaries;
2. recitational opening context and basmala policy, when applicable;
3. a concise primary contextual scaffold independent of secondary branches;
4. positioned morphology;
5. verified syntax and discourse edges, when available;
6. complete V4 branch dossiers under the four-field boundary.

Run metadata such as `run-card.json`, `input-summary.json`, or legacy
`source-manifest.*` files may be supplied when present, but they are not
semantic evidence and are not required by this workflow. Absence of manifest
files is not a blocker when the prepared input package validates and the core
evidence files above are present.

Do not supply a gold answer, exemplar, evaluation, prior synthesis, thematic network, semantic hierarchy, proposed axis, or preselected local-sense labels.

## 5. Large inventories

When all dossiers cannot fit safely at once, send complete root-dossier batches to the same session.

Never replace the Arabic branch prose with keywords, embeddings, themes, or summaries. Pass 1B may begin only after every authorized branch record has been delivered.

If context rollover is unavoidable, restore the same logical author with the complete living notebook plus the exact authorized evidence required by every live and unresolved model. Do not replace the notebook with an administrative digest.

## 6. Cognitive sequence

### Pass 1A — activation discovery

The author performs the fixed activation loop:

```text
branch or textual cue
→ concrete operation or relation
→ open roles
→ complementary retrieval
→ provisional model
→ prediction of unused passage features
→ test against later/unused evidence
→ backward reactivation
→ changed primary perception
```

Output:

```text
discovery-notebook.md
```

### Pass 1B — coalition resurrection

The same author stops testing unused branches only against the already successful models. It combines dormant branches through complementary roles, primary-anchor queries, cross-definitions, inverse operations, rings, and conditional constellations.

Output: the same rewritten and completed `discovery-notebook.md`.

### Pass 2 — gold synthesis

The same author writes the primary research product. Discovery remains open while writing.

The gold document is organized by activation channels or relational findings, not by ayah ranges, pericopes, or passage sections.

Output:

```text
gold-synthesis.md
```

### Pass 3 — publication prose

The same author writes the publication while the complete synthesis is still active.

The prose is organized by activation events and transformations, not by sequential section summaries.

Output:

```text
publication.md
```

## 7. Anti-pericope rule

Passage divisions may be used internally to detect changes of participant, voice, agency, direction, or domain. They are not default output units.

A gold section or publication paragraph is invalid when its main function is merely:

```text
summarize this ayah or pericope
+ append one or more lexical observations
```

A valid unit must perform at least one of these operations:

- show a secondary branch changing a primary proposition;
- show several branches forming one complementary activation coalition;
- carry an operation between distant passage positions;
- show a later cue changing the hearing of an earlier expression;
- distinguish or interlock independent channels;
- explain why a vivid form is necessary for a later judgment.

No output heading should be based only on verse numbers, “opening/middle/ending,” or passage-section labels.

## 8. Completion conditions

The run is complete only after the same author has produced all three files and the following are true in substance:

- at least one major proposition depends materially on V4 evidence whenever the supplied evidence supports one;
- every major channel states its activation route and changed primary perception;
- coalition-dependent findings have received a dedicated resurrection search;
- later cues alter earlier readings rather than merely echoing them;
- no major channel disappears because one global reading is already coherent;
- the gold and publication are not pericope-by-pericope summaries.

These are instructions to the same author, not a separate semantic audit stage.
