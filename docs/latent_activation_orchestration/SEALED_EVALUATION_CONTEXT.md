# Sealed Evaluation Context

Classification: evaluator-only

**The matrix builder must not read this file.**

This file preserves why the project began and the target-aware findings needed
for later blind evaluation. It is deliberately separated from implementation.

## 1. Original Problem

For a given ayah window, a root may have many accepted branches. The intended
downstream task is to consider how branches across all roots can become active
together without reducing the search to direct lexical matches.

The motivating cases include:

- recovery of a water/well image through secondary resonances rather than only
  direct water vocabulary;
- recovery of a complete road-and-traveler image rather than only direct road
  words;
- semantic nearness and thematic or functional compatibility across different
  root branches.

Prompting, pair queues, Qnet relations, and several staged search procedures
were tried and eventually plateaued. The proposed matrix separates the
representation problem from later search: first determine whether desired
branches are actually near in a complete reusable space.

## 2. Why This Context Is Sealed

An implementer who knows the named target images can:

- choose text fields that happen to favor them;
- alter fusion weights after inspecting their neighborhoods;
- add target synonyms or relations;
- choose thresholds or encoders based on target recovery.

That would make a nominally unsupervised matrix target-supervised in practice.
The builder therefore receives only generic cross-view and matrix requirements.

## 3. S1 Scale

The v12 S1 full-context packet contains:

```text
surface roots: 18
accepted branches: 144
per-root branch counts:
8, 2, 4, 5, 17, 6, 8, 3, 7, 11, 8, 11, 3, 20, 13, 5, 8, 5
```

Combinatorics:

```text
all unordered pairs:                         10,296
cross-root unordered pairs:                   9,591
one branch chosen from every root: 828,055,388,160,000
arbitrary subsets: 2^144, about 2.23e43
```

This explains the need for a reusable proximity artifact. It does not justify
showing S1 target memberships to the builder.

## 4. Prior Qnet Findings

The live sibling Qnet database was unavailable. Cached v11 S1 material showed:

```text
formal-overlap relation instances: 86
semantic-candidate relation instances: 36
```

The evidence was dominated by exact-form overlap and cohesive lexical cliques.
That helped lexical recall but did not reliably represent complementary scene
roles. The earlier global top-80 bridge subset also starved several branches of
exposed edges.

The complete matrix avoids top-N starvation, but a general semantic encoder may
still fail to encode complementarity. That is what blind evaluation must test.

## 5. Prior Output Inventory

At the initial audit, prior material included approximately:

```text
Markdown run files:                         505
raw root/branch-ID mentions:             41,985
v11 activation-pass JSON files:              48
v11 secondary-expansion JSON files:           48
v11 final reports:                            32
A/B/C/C-B/S labels:                        2,518
alternate mechanism entries:                326
object-shaped usable mechanisms: about      274
```

These artifacts are duplicated, mixed-quality, and partly model-generated.
They are not automatically human gold.

## 6. Reference Tiers

Every evaluation item must declare one tier:

```text
HUMAN_GOLD
    independently curated branch pair/group with provenance and uncertainty

ADJUDICATED_REFERENCE
    prior candidate reviewed and accepted by independent domain curators

MODEL_PSEUDO_REFERENCE
    branch membership inferred only from prior model outputs
```

Never combine these tiers into one headline metric. Report them separately.

## 7. Independent Curation

Before any curator sees matrix rows, neighborhoods, or ranks:

1. select passages and reference source material;
2. map each reference member to canonical `node_id`;
3. record unmapped and ambiguous cases;
4. preserve multiple acceptable mappings where identity is uncertain;
5. obtain two independent mappings where practical;
6. adjudicate disagreements without matrix access;
7. freeze JSONL, schema, metrics, thresholds, and SHA-256 hashes;
8. timestamp the reference manifest.

The evaluator must verify that the reference manifest predates matrix access.

## 8. Matrix-Only Evaluation

The evaluator may compute:

- exact pair distance;
- rank of one reference member from another;
- reciprocal rank of the nearest other group member;
- Recall@10/50/100;
- macro results per reference group;
- matched random-set null distributions;
- separate results for semantic, thematic-proxy, and combined matrices.

Primary rankings are cross-root. For each query member:

1. exclude the query node;
2. exclude every candidate sharing its `surface_root_key`;
3. rank by ascending distance and then ascending `node_id` for exact ties;
4. mark the query eligible only if another reference member has a different
   surface root.

Same-root reference structure may be reported separately but cannot satisfy the
primary cross-root utility gate.

The evaluator must not:

- write or revise interpretations;
- add reference members after inspecting neighborhoods;
- tune matrix weights;
- hide unmapped references;
- report pseudo-reference results as human gold;
- ask the builder to patch the same treatment after unsealing.

## 9. Pilot Utility Decision

The initial preregistered pilot uses:

```text
random matched sets: 10,000
permutation significance: p <= 0.01
practical coverage: at least 50% of eligible members have another reference
                    member in the combined matrix's cross-root top 100
primary matrix: combined_distance.f32.npy
```

Semantic and thematic-proxy matrices are secondary diagnostics and cannot be
selected post hoc to rescue a failed combined-matrix primary result.

Allowed outcomes:

```text
UTILITY_PASS
UTILITY_PARTIAL
UTILITY_FAIL
REFERENCE_INSUFFICIENT
```

A failure identifies a representation problem. It does not authorize
target-specific modification. A new encoder, field treatment, or unsupervised
adaptation receives a new treatment ID and repeats the blind protocol.

## 10. Scope Reminder

Even the evaluator assesses matrix proximity only. Passage analysis, activation,
coalition search, and interpretation belong to later consumer projects.
