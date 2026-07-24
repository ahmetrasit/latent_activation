# Blind Hierarchical Candidate Review Prompt

You are doing a first-pass blind semantic-channel discovery review for one v3
surah.

Use only this input file:

- `network/v3/experiments/corpus_neo_adaptive/SURAH_TAG/review_bundle.json`

Do not inspect gold findings, prior reports, old channel lists, predefined
domain targets, full JSONL files, summaries, source repositories, or external
sources. Do not consult `label_hint` until the branch-first micro-motif and scene
inventory is complete. Afterward, use family labels only as a recall check,
never as primary evidence or as the starting vocabulary for channel names.
Judge by micro-motif coherence, surface context, root/ayah coverage, and
whether dense or sparse constructions make semantic sense. Resolve family
branch IDs against the bundle's unique `branches` table. Read
`branch_image_ar` and `what_is_ar` together as the branch evidence. Use
`surface_context` to understand Arabic ayah text, exact root/token usage, and
surface anchors without exposing gold channels.

Treat data-attested lexical imagery as review evidence. Do not demote a channel
merely because it is latent, surprising, concrete, or not visible in the surface
translation. If the bundle shows coherent branch evidence across rows,
roots, or ayahs, surface it as a candidate channel. This is a discovery and
extraction task, not an audit, grading, validation, or caution task.

Core ontology:

1. Atomic micro-motif: one precise, source-attested image, action, role, object,
   state, function, or relation. A branch ID is an evidence container and may
   hold more than one micro-motif.
2. Subchannel: a coherent scene, process, mechanism, social frame, or discourse
   relation supported by several atomic micro-motifs.
3. Parent channel: related subchannels sharing an underlying semantic
   invariant.
4. Resonance bridge: the exact relation connecting otherwise distinct
   subchannels.
5. Lexical resonance: a branch sense that meaningfully extends a formed or
   emerging channel even when it does not constitute a complete scene.
6. Surprise probe: a suggestive or unexpected relation whose scene remains
   incomplete or ambiguous but should remain visible for later synthesis.

A subchannel may stand alone. Create a parent channel only when at least two
distinct subchannels share a defensible semantic invariant.

Discovery is intentionally recall-oriented. Parent channels, subchannels,
bridges, lexical resonances, and surprise probes are organizational forms, not
acceptance grades. Weak recurrence, reused support, overlap with another
channel, or a tentative bridge must not by itself suppress a coherent or
suggestive resonance. A later QC/audit stage will assess overreach.

Task:

1. Extract before clustering. Without consulting `label_hint`, inventory atomic
   micro-motifs from branch images, `what_is_ar`, construction edges, and
   surface context. Treat each branch ID as an evidence container, not
   necessarily as one atomic motif. When the combined evidence in
   `branch_image_ar` and `what_is_ar` distinguishes senses that differ
   materially in entity, action, function, relation, semantic role, or scene
   participation, represent them as separate micro-motifs sharing the branch
   ID. Give every micro-motif a stable local identifier such as
   `root:B###/m01`; the suffix is review-local provenance, not a new bundle ID.
   Do not split mere synonyms or invent distinctions, but do split
   source-attested alternatives that could belong to different scenes,
   processes, mechanisms, social frames, or discourse relations. Do not start
   by naming broad domains.
2. Preserve each micro-motif's branch ID and a concise supporting phrase from
   `branch_image_ar` or `what_is_ar`. Assign every micro-motif a semantic role:
   object, component, material, action, setting, agent, state, relation, or
   outcome. Use more than one role only when the branch evidence requires it.
   Do not treat every clause, synonym, modifier, entailment, or illustrative
   example as a separate micro-motif. Preserve such wording as source glosses
   under one micro-motif unless it changes semantic role or scene participation.
3. Search systematically for these structural resonance types:
   - same-root semantic transformations;
   - cross-root object-part, tool, or mechanism assemblies;
   - causal and functional sequences;
   - analogies of shape, motion, or function;
   - contrasts and role reversals;
   - social-frame extensions.
4. Follow shared branch hinges and connected construction edges within and
   across rows. For every emerging scene, build an internal role map covering
   setting, participant or agent, object, component, material, tool, action or
   process, state, relation, and outcome. Search connected rows, paths, and
   shared hinges for compatible micro-motifs that complete or extend the scene.
   This role map is a recall aid, not a completeness requirement: a scene need
   not contain every role. A coherent scene or mechanism may be distributed
   across several families; no single row or all-to-all edge structure needs to
   contain every component. A complete multi-part scene can be meaningful even
   when it appears only once.
5. Build subchannels with the one-scene test: micro-motifs belong together when
   they can participate in one intelligible scene, process, mechanism, social
   frame, or discourse relation. Whenever a branch contributes to a channel,
   identify the active micro-motif. Do not cite only the branch ID or substitute
   an umbrella paraphrase that obscures the active entity, function, or
   relation. Different micro-motifs from the same branch may independently
   contribute to different channels.
6. For every proposed subchannel or internal bridge, determine the connecting
   invariant and resonance type when one is visible. When the relation is
   currently associative, topical, or based mainly on co-occurrence, preserve
   it internally as a lexical resonance or surprise probe. Integrate it into
   channel prose only when it materially clarifies a parent or subchannel.
7. Consolidate subchannels into parent channels only when at least two distinct
   subchannels share a concise semantic invariant. Otherwise retain the formed
   material as a standalone subchannel.
8. Do not consolidate through topical similarity alone. Before finalizing,
   assign each proposed subchannel a scene signature consisting of its semantic
   invariant, active micro-motifs, participants, setting, objects or components,
   operation or process, central relations, and state or outcome. Reconcile
   proposals with substantially the same signature: define the scene once and
   retain any additional relation internally as a bridge or resonance. Mention
   that relation only inside the relevant channel synthesis when useful. Shared
   branches alone do not require merging. Keep scenes separate when their active
   senses, operations, or outcomes differ materially.
   After scene signatures are available, perform within-branch consolidation.
   Merge candidate micro-motifs when they share the same semantic role,
   function, scene signature, and canonical channel placement. Retain their
   source wording as grouped glosses under one micro-motif. Keep candidates
   separate when they materially change the scene, role, mechanism, operation,
   outcome, or channel placement.
9. Allow dense `F###` rows and sparse `PF###` rows to function as bridges. A row
   does not need to become a channel merely because it joins two formed
   channels.
10. Inspect support structure internally without using it as an inclusion gate.
    Use each row's `support_summary` to understand roots, ayahs, path reuse, and
    repeated edges. Reused support must not hide or demote a coherent scene.
11. Preserve coherent singletons. A complete intelligible scene may become a
    standalone subchannel regardless of frequency. Use a surprise probe for an
    incomplete but suggestive relation, not as a holding category for formed
    material.
12. Distinguish surface-primary readings from latent lexical channels without
    treating latent lexical material as weaker by default.
13. Do not exclude a concrete image class simply because it is lexical,
    concrete, or absent from surface translation.
14. After the branch-first construction is complete, consult `label_hint` only
    to check whether a supported micro-motif or scene was overlooked. Do not
    rename channels merely to match a hint.
15. Perform the final coverage sweep at the micro-motif level, not merely at the
    branch-ID level. Revisit every unassigned micro-motif and test whether an
    umbrella label has concealed a compatible same-root or cross-root scene,
    process, mechanism, social frame, or discourse relation. A branch is not
    fully covered merely because one of its micro-motifs has been assigned.
    Assign every materially supported micro-motif to a parent subchannel,
    standalone subchannel, bridge, lexical resonance, surprise probe, or
    residual class. Reserve residual status for material that remains
    unintelligible after reading its branch evidence; weak, overlapping, reused,
    or unexpected material must remain visible elsewhere. This assignment is an
    internal discovery ledger, not a required set of output sections.

Output a Markdown report to:

`network/v3/reviews/SURAH_TAG/reader_a_pilot.md`

Do not impose an arbitrary cap on parent channels or subchannels. Keep the
micro-motif inventory, role maps, scene signatures, support analysis, bridges,
lexical resonances, surprise probes, coverage accounting, and residual
classification as internal discovery work. Do not reproduce those working
ledgers as report sections.

The report is a channel synthesis, not an audit. Output only:

- parent channels with their nested subchannels; and
- standalone subchannels that do not defensibly share a parent invariant.

Do not output a separate atomic inventory, confidence assessment, evidence
breadth assessment, support-row or path listing, resonance-bridge section,
lexical-resonance section, surprise-probe section, residual section, coverage
accounting, or validation commentary. Integrate a bridge, lexical resonance, or
surprising relation into the relevant parent or subchannel synthesis only when
it materially clarifies that channel.

Do not mention the prompt, the agent, the review process, earlier reports,
revisions, previously missed findings, coverage performance, or why an item was
accepted. Avoid grading, auditing, and self-evaluative language.

Use the detailed micro-motif and role ledger internally. In the report, group
sibling micro-motifs compactly when they share a scene signature and canonical
placement. Expand only distinctions that materially change channel meaning or
placement. Identify active motifs concisely by name and micro-motif ID without
copying full branch definitions or queue rows.

Before writing a parent or subchannel, inspect the relevant dense and sparse
rows' core, optional, rare, and construction-path branches internally. Carry
into the synthesis every active micro-motif that materially belongs to the
channel. Do not import sibling senses merely because they share a branch ID,
and do not include unrelated branch tails merely because they appear in the
same row.

For every ayah span or ayah-coverage field, use the actual surface occurrences
of the cited evidence roots from `surface_context`. Do not use the union of all
ayahs attached to a supporting row when some of those ayahs do not contribute
branch evidence to the channel.

When you finish, report branch coverage in your completion message, not inside
the Markdown report. Calculate coverage mechanically as:

1. Count the unique branch IDs in the bundle's top-level `branches` table. Each
   `branches[].id` value has the form `root:B###`; this is the denominator.
2. Count the unique `root:B###` branch IDs you cited in the Markdown report's
   active motifs; this is the numerator. Count each branch at most once even if
   it appears in multiple subchannels.
3. Coverage percent is `100 * cited_unique_branch_count / bundle_branch_count`.

Report the numerator, denominator, and percent in the completion message.

Report format:

```markdown
# SURAH_TAG Semantic Channel Discovery

## Parent Channels

### 1. Parent Channel Title
- Semantic invariant:
- Surface relation: direct | indirect | none; give ayah refs and anchors when
  direct or indirect
- Surprising reach:

#### Subchannel A. Short Subchannel Title
- Reading type: surface-primary | latent/lexical | mixed
- Scene or process:
- Active motifs: concise names with root:B###/m## identifiers
- Ayah anchors: actual surface occurrences of cited evidence roots
- Synthesis: coherent explanatory prose showing how the motifs form one scene,
  process, mechanism, social frame, or discourse relation; include the
  unexpected resonance where material

## Standalone Subchannels

### S1. Standalone Subchannel Title
- Reading type: surface-primary | latent/lexical | mixed
- Scene or process:
- Active motifs: concise names with root:B###/m## identifiers
- Ayah anchors: actual surface occurrences of cited evidence roots
- Synthesis:
```

Keep the report focused on channel discovery and synthesis. Do not include an
audit trail, command transcript, file inventory, repeated source data, grading
language, validation cautions, or any section outside the parent/subchannel
hierarchy shown above.
