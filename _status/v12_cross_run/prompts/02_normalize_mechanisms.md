# Prompt 02 — Mechanism Normalization and Cross-Run Clustering

You normalize extracted source findings into provisional claims. You do not
decide lexical validity or publication priority.

## Inputs

Read only:

- `runs.tsv`;
- `source_findings.tsv`;
- the analytical reader lines reached through source pointers;
- the TSV schema and this prompt.

## Automated Output Contract

Do not edit canonical files. Write only the JSON object conforming to
`model_schemas/normalize.json` at the assigned result path. The orchestrator
assigns final claim IDs, writes claim and lineage TSV rows, and derives
source-finding merge/split dispositions atomically.

Use a short, stable `claim_key` slug that describes the mechanism rather than
its publication role. New claims remain unreviewed until later stages.

## Non-Loss Rule

Every source finding must remain represented. A finding that seems invalid,
remote, or unpublishable still receives a provisional claim or an explicit
lineage link to such a claim. Do not reject at this stage.

## Clustering Standard

Cluster by mechanism, not wording. Two findings belong together only when they
substantially agree on:

1. fixed ayah;
2. lexical/root material;
3. contextual activators;
4. causal, spatial, functional, temporal, social, legal, or material topology;
5. resulting reading change.

Use:

- `shared_mechanism` when both runs express substantially the same topology;
- `compatible_refinement` when one adds a compatible causal or material layer;
- `standard_only` or `eleven_ayah_only` for genuine one-run findings;
- `material_conflict` when causal direction or reading outcome conflicts.

Silence in the other run is neutral. Agreement is stability, not independent
confidence.

## Split Rule

Split a source finding when it contains mechanisms that may receive different
lexical or publication decisions. Preserve one `claim_sources.tsv` link from
the source finding to every resulting claim with
`source_relation=split_component`.

## Completion Checks

- Every source finding is linked to at least one provisional claim.
- Every claim has at least one source-finding link.
- One-run findings remain present.
- Conflicts remain separate or explicitly marked.
- No lexical, resonance, translation, or publication decision was invented.
