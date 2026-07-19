# Unsupervised Latent Activation Graph: Cold-Agent Orchestration Plan

Status: execution-ready research and engineering plan
Prepared: 2026-07-19
Current repository: `latent_activation`
Working implementation name: `v14` (not yet created; `v13` is already assigned)
Primary method: zero-gold, multi-view branch graph with iterative activation
Optional escalation: self-supervised domain and graph adaptation

## 0. Executive Decision

This project is doable.

The repository contains the complete scholarly source data needed for the first
experiment. It does not currently contain the neural runtime or a pretrained
embedding checkpoint. The current machine also has too little free disk for a
safe local neural installation and has no useful local training GPU.

The shortest scientifically defensible route is:

1. Select the 10,820 accepted, uncontaminated `quranic` branches from the local
   Furūq database.
2. Preserve each branch's Arabic and English fields as separate views.
3. Build sparse lexical and fixed-pretrained dense representations without
   using any gold reading.
4. Compute global neighbor statistics blockwise; do not persist a dense matrix
   unless explicitly useful.
5. For each ayah window, compute the exact local branch-to-branch affinities
   among branches belonging to surface roots.
6. Seed every branch and run restart-based spreading activation with
   independent-root aggregation.
7. Extract several overlapping, bounded coalitions for every seed branch.
8. Freeze code, data hashes, model revision, configuration, and outputs.
9. Only after freezing, open sealed reference readings and measure recovery.
10. Add self-supervised adaptation only if the fixed-encoder graph demonstrably
    lacks candidate recall.

Do not begin by training an SLM, reproducing Qnet, designing more discovery
prompts, or manually encoding the motivating S1 scenes.

## 1. Ultimate Goal

Given a Quran ayah window:

1. Resolve every surface root and load all accepted lexical branches for those
   roots.
2. Preserve the primary contextual reading.
3. Test every branch, including secondary and remote facets, for activation by
   the other roots and structures in the same window.
4. Recover multiple coexisting branch coalitions that form coherent material,
   spatial, causal, social, temporal, embodied, legal, ecological, ritual, or
   other mechanisms.
5. Recover distributed images whose components are complementary rather than
   synonymous, such as a route assembled from road, marker, guide, support,
   prior walker, provision, and deviation roles.
6. Return auditable evidence paths: exact roots, branch IDs, source fields,
   graph edges, activation contributors, and any inferred relation.
7. Avoid turning a secondary coalition into an alternative translation or an
   ungrounded total metaphor.

The operational target is not literal enumeration of every subset. It is:

```text
For every passage branch b, return the top K diverse, bounded coalitions
containing b, or explicitly report that no supported coalition was found.
```

This produces branch-level opportunity coverage without enumerating an
astronomical assignment space.

## 2. Why This Project Started

### 2.1 The linguistic object

Each surface Quranic root has multiple accepted lexical branches. A branch may
contain a direct contextual sense, a secondary physical image, an instrument,
a participant arrangement, a motion, a material property, a social relation,
or a failure mode.

The research target is not ordinary word-sense disambiguation. Multiple
branches can remain active at different levels. A secondary reading may emerge
only when branches belonging to several different surface roots fill different
roles in one scene.

Examples that motivated the project include:

- a water/well/provision structure assembled from a body of water, collected
  water, well apparatus, and water as a travel-enabling resource;
- a road/traveler structure assembled from a prepared surface, road marker,
  leading guide, course, straightness/support, prior people, and deviation.

These names are recorded here as historical motivation. They must not become
hard-coded frames, search queries, prompt examples, training labels, threshold
targets, or feature-engineering targets in the zero-gold build.

### 2.2 Why pairwise and prompt methods plateaued

Earlier workflows correctly recognized that a coalition is the unit of
discovery. However, that principle was largely executed through prompting.
Prompting can expose a model to all branches or ask it to resurrect dormant
roles, but it does not implement reproducible search over branch sets.

The v11 mechanical layer creates pair edges from shared leaf themes, shared raw
keywords, or Q2 relations. This mainly captures homophily: branches that look
similar or share wording. The target often requires heterophily or
complementarity: an instrument is not synonymous with its operation, a resource
is not synonymous with its user, and a marker is not synonymous with a road.

The v12 full-context method gives a frontier model all accepted branch records
for a passage and asks for sequential reasoning. This avoids mechanical pruning
but leaves the set search implicit in attention. It can recover local pieces
while missing complete distributed coalitions.

The new project promotes branch affinity, iterative activation, coalition state,
and evidence traces into explicit computational objects.

### 2.3 Why a small language model is not the first solution

The branch inventory is a knowledge base, not a sufficient language-model
pretraining corpus. Training an autoregressive model on branch prose would
mostly teach reconstruction and memorization. It would not define which branch
sets are coherent or solve the combinatorial search objective.

A fixed general encoder can supply broad semantic priors. A graph can constrain
runtime evidence to the local branch inventory. A small graph or set model can
later learn iterative activation if self-supervised objectives provide useful
signal. Natural-language generation should remain downstream of candidate
discovery.

## 3. Verified Repository Findings

All facts in this section were checked locally on 2026-07-19.

### 3.1 Repository state

- Repository branch at inspection: `main`.
- Audit-base commit: `c18a412 Add synthesis publications and coverage audits`.
- Current upstream commit after the documentation rebase:
  `1443cac Add v13 dynamic retrieval workflow`.
- Worktree was clean before this plan file was added.
- Repository size was approximately 2.0 GiB.
- `.git` was approximately 407 MiB.
- `resources` was approximately 387 MiB.
- `v11` was approximately 399 MiB.
- `v12` was approximately 9.4 MiB.

The existing `v13/` is a deterministic five-ayah dynamic-retrieval workflow.
It reuses v12 QAC/branch loading and incrementally reveals unseen root
inventories to a reader. It does **not** implement embeddings, a global branch
graph, restart diffusion, or coalition search. Its current provenance declares
both `furuq` and `quranic` origins. Therefore:

- do not overwrite or repurpose `v13/`;
- reserve `v14/` for the graph system in this plan;
- reuse v13 retrieval code only behind an adapter and tests;
- override its combined-origin policy for the frozen 10,820-branch quranic-only
  first treatment.

### 3.2 Authoritative local inputs

The following required resources exist:

```text
resources/furuq_v4.sqlite       164 MiB
resources/furuq_v4.sqlite.gz     26 MiB
resources/qac.sqlite            113 MiB
resources/qac.sqlite.gz          26 MiB
resources/v4_branches.tsv       9.3 MiB
resources/qac_root_ayah.tsv      29 MiB
resources/quran/                114 surah JSON files plus 4 corpus/source files
resources/attachments.tsv        17 MiB
```

`resources/furuq_v4.sqlite` contains a `branch_images` table with these relevant
fields:

```text
root_id
root_norm
branch_id
branch_image_ar
branch_image_en
what_is_ar
what_is_en
what_is_not_ar
source_refs
source_phrase_ar
status
origin_corpus
contaminated
```

### 3.3 Exact branch counts

For `status='accepted' AND contaminated='no'`:

| `origin_corpus` | Branches | Roots |
| --- | ---: | ---: |
| `quranic` | 10,820 | 1,688 |
| `furuq` | 7,961 | 1,652 |
| Total | 18,781 | 3,340 |

The database contains 3,470 root registry rows in total across all statuses.

The intended approximately 11K corpus corresponds exactly to the 10,820 clean,
accepted `quranic` branches. Use this subset for the first experiment. Do not
silently include the additional 7,961 `furuq` branches. A later experiment may
compare the union, but it is a separate treatment.

Every one of the 18,781 clean accepted rows has nonempty:

- Arabic branch image;
- Arabic scope/explanation;
- English branch image;
- English scope/explanation.

This means the first multi-view experiment does not require translation or
manual gloss creation.

Canonical selection query:

```sql
SELECT
  root_id,
  root_norm,
  branch_id,
  branch_image_ar,
  branch_image_en,
  what_is_ar,
  what_is_en,
  what_is_not_ar,
  source_refs,
  source_phrase_ar,
  origin_corpus
FROM branch_images
WHERE status = 'accepted'
  AND contaminated = 'no'
  AND origin_corpus = 'quranic'
ORDER BY root_id, branch_id;
```

Hard gate: the export must contain exactly 10,820 unique
`root_id:branch_id` keys. A mismatch stops the run.

### 3.4 S1 scale and combinatorics

The v12 S1 full-context packet contains:

- 18 surface roots;
- 144 accepted branches;
- per-root branch counts:

```text
8, 2, 4, 5, 17, 6, 8, 3, 7, 11, 8, 11, 3, 20, 13, 5, 8, 5
```

For those 144 branches:

- all unordered branch pairs: 10,296;
- cross-root unordered pairs: 9,591;
- assignments choosing exactly one branch from every root:
  828,055,388,160,000;
- arbitrary branch subsets: `2^144`, approximately `2.23e43`.

Pair scoring is tractable. Exhaustive full-depth assignment or subset search is
not. A smaller language model does not change this fact.

The v11 S1 artifact uses a larger 151-branch union inventory and contains:

- 3,533 retained candidate bridges;
- 3,211 cross-root candidates;
- 322 same-root candidates;
- 108 candidates carrying one or more Q2 relations;
- an agent-facing global subset of only 80 candidates.

The full v11 S1 bridge JSON is approximately 9.7 MiB. The v12 full-context S1
packet is approximately 172 KiB. Pairwise serialization, not pair computation,
creates much of the v11 input bulk.

Inspection of known S1 scene members in the global top-80 subset showed branch
starvation. Several important route preparation, marker, and leading-guide
branches had zero exposed top-80 edges, while only a few direct road/straightness
or water edges remained. This is evidence against a single global top-N queue.
Use per-branch and per-relation coverage instead.

### 3.5 Qnet findings

The configured live path was:

```text
../quran-roots/_corpus/activation/Qnet/v2/network/
  bridge_theme_full/bridge_theme_staging.sqlite
```

The entire sibling path `../quran-roots/_corpus/activation` is absent in the
current workspace. Attempting a fresh v11 S1 build failed with
`FileNotFoundError` at that Qnet SQLite path.

The live Qnet corpus was therefore not inspected. Qnet-derived v11 artifacts and
integration code were inspected. Candidate creation depends on:

```text
shared leaf theme OR shared raw keyword OR in-scope Q2 relation
```

The cached S1 Q2 relation evidence was dominated by:

- 86 formal-overlap relation instances;
- 36 semantic-candidate relation instances;
- channels described as exact-form overlap or cohesive lexical cliques.

This is useful for lexical neighborhood recall but does not reliably represent
complementary scene roles. Qnet is excluded from the core design. It may later
be tested as a separately weighted ablation channel. It must never be required
for a successful run.

### 3.6 Existing output and reference material

The repository contains extensive prior outputs, including:

- `s1-bulgular-tr.md`;
- v3, v4, v5, v6, v8, v9, v11, and v12 run artifacts;
- multiple gold-synthesis files;
- adjudication templates and frozen-run tooling;
- S1, S100, S103, S108, S112, S113, and other passage analyses.

There are approximately 505 Markdown run files across the inspected output
trees and approximately 41,985 raw root/branch-ID mentions. These are highly
duplicated and include intermediate, rejected, rendered, and derivative
material. They are not automatically clean training examples.

The structured v11 material includes:

- 48 `05-activation-pass.json` files;
- 48 `07-secondary-expansion.json` files;
- 32 `09-final-report.md` files;
- approximately 2,518 A/B/C/C-B/S branch labels;
- 326 alternate-mechanism entries across the secondary-expansion files;
- approximately 274 object-shaped alternate mechanisms with usable branch
  paths after excluding schema variants and string-only entries.

This is enough for later blind evaluation and diagnostic reference. It is not
used during the zero-gold build. It is also not automatically adequate
supervision because coalition membership does not imply that every member pair
is a direct positive edge.

### 3.7 Current machine and runtime

Verified host characteristics:

```text
macOS 15.7.7
x86_64 Intel Haswell
4 physical CPU cores
8 logical CPU cores
16 GiB RAM
```

Current disk state at the final check:

```text
filesystem size: 113 GiB
available:       2.4 GiB
utilization:     98%
~/.cache:        39 MiB
```

Python/runtime findings:

- Python 3.14.5 exists and has NumPy and pandas.
- Python 3.10.19 exists and is the preferred ML environment base.
- Python 3.10 currently has none of NumPy, SciPy, scikit-learn, PyTorch,
  Transformers, SentenceTransformers, FAISS, NetworkX, or pandas installed.
- No PyTorch installation exists, so CUDA/MPS runtime checks cannot run.
- The Intel Mac has no expected local CUDA or Apple-Silicon MPS training path.
- No Hugging Face or SentenceTransformers model checkpoint is cached.
- No `pyproject.toml`, requirements file, lockfile, or environment file was
  found at repository level.
- SQLite 3.43.2 is available.

The machine can run sparse lexical baselines and CPU fixed-encoder inference
after dependencies are installed. It is not the intended machine for meaningful
self-supervised neural training.

## 4. Storage and Compute Findings

### 4.1 Intended 10,820-branch corpus

For `n = 10,820`:

```text
n^2 entries                   117,072,400
dense float16 matrix bytes    234,144,800  (~223 MiB)
dense float32 matrix bytes    468,289,600  (~447 MiB)
384-d float32 embeddings       16,619,520  (~16 MiB)
768-d float32 embeddings       33,239,040  (~32 MiB)
top-64 directed edges             692,480
top-64 int32+float16 payload     4,154,880  (~4 MiB before metadata)
```

The dense matrix is feasible but unnecessary for production. Compute cosine
similarities blockwise and retain:

- top-K neighbor IDs and scores;
- local density/threshold statistics;
- hubness and degree diagnostics;
- embeddings needed for exact passage-local matrices.

### 4.2 Full 18,781-branch accepted corpus

For comparison:

```text
n^2 entries                   352,725,961
dense float16 matrix bytes    705,451,922  (~673 MiB)
dense float32 matrix bytes  1,410,903,844  (~1.31 GiB)
```

Do not begin with this larger treatment.

### 4.3 Disk required by stage

Approximate additional disk needs:

| Stage | Additional disk |
| --- | ---: |
| Code, schemas, unit tests | under 100 MiB |
| Sparse lexical prototype | 100-500 MiB |
| Embeddings and sparse graph | under 100 MiB |
| Optional dense float16 matrix | about 223 MiB |
| Python ML environment | roughly 1-2 GiB |
| Multilingual-E5-small weights | about 471 MiB |
| Safe fixed-encoder baseline | 3 GiB minimum, 5 GiB recommended |
| Self-supervised checkpoints | 8-15 GiB |
| Heavy/multiple model treatments | 10-20+ GiB |

The current 2.4 GiB free space is enough to write code and run a non-neural
prototype. It is unsafe for installing a local neural stack and checkpoint.

After moving the repository, require:

- at least 5 GiB free for the fixed-encoder experiment;
- at least 15 GiB free if local checkpoints will be produced;
- preferably set `HF_HOME`, `TRANSFORMERS_CACHE`, and virtual-environment paths
  to the roomy volume.

## 5. Definitions

### Branch

One accepted `root_id:branch_id` lexical record. Branch IDs are only unique
inside a root.

### Facet

One concrete object, action, role, material, participant arrangement, state, or
outcome inside a branch record. A branch may contain several facets.

### Passage inventory

All accepted branch records belonging to roots actually present in the selected
ayah window, with surface occurrences and order attached.

### Semantic similarity

Substitutive or descriptive nearness: two branches describe similar objects,
actions, properties, or meanings.

### Scene compatibility

Two branches can perform different but mutually useful roles in the same
mechanism. This need not be metric, symmetric, or transitive.

### Activation

Passage-conditioned support for a branch supplied by other passage branches,
surface morphology/order, and bounded inference.

### Coalition

A set of branches from multiple passage roots forming one connected and
auditable mechanism. Coalitions can overlap and can compete.

### Supplied relation

A relation explicitly recoverable from branch prose, Quran wording,
morphology, syntax, or order.

### Inferred relation

A directional or causal link supplied by a model or algorithm rather than
stated by the source. It must be labeled and assigned an inference cost.

### Gold/reference

Any prior human, agent, or synthesis output that states target activations or
coalitions. Gold is sealed during development and may be used only after the
system is frozen, unless a later supervised treatment is explicitly declared.

## 6. Scientific Contract

### 6.1 Zero-gold treatment

The first complete treatment must not read, parse, embed, train on, prompt with,
or tune against prior interpretation outputs.

Allowed development inputs:

```text
resources/furuq_v4.sqlite
resources/qac.sqlite
resources/quran/
resource schemas
mechanical source-resolution code
this orchestration plan
general pretrained model weights
```

Sealed during implementation and tuning:

```text
s1-bulgular-tr.md
v3/run/**
v4/run/**
v5/run/**
v6/run/**
v8*/run/**
v9.0/run/**
v11/run/** agent-produced interpretation files
v12/runs/** reader/adjudication outputs
test/** synthesized prose/reference files
```

Mechanical v11/v12 scripts may be read for resource handling. Their
interpretive outputs may not be used.

### 6.2 External priors are not gold

A fixed pretrained encoder introduces general language/world bias. This is
permitted in the practical zero-gold treatment because it has not been trained
on the project's target coalitions. Its model ID and immutable revision must be
recorded.

Run at least one corpus-derived sparse baseline so the contribution of the
external encoder can be measured.

### 6.3 Evidence and inference must remain separate

Every retained coalition must record:

- exact member branch IDs;
- exact source fields used;
- passage roots and occurrences;
- direct graph edges;
- activation contributors;
- inferred edges, if any;
- score components rather than only a total score;
- missing or weak roles.

### 6.4 No forced disambiguation

Do not require one branch per root. Several branches of one root can remain
active. Use per-root caps only to prevent inventory-size domination during
message aggregation.

### 6.5 Completeness is bounded

The system may claim coverage only relative to declared limits:

```text
passage roots included
branch selection policy
neighbor policy
maximum activation hops
maximum coalition size
minimum distinct roots
beam/state limits
inference budget
```

It must never claim to have enumerated all meaningful human readings.

## 7. Non-Goals

- Do not produce tafsir.
- Do not replace direct Quranic meanings with secondary images.
- Do not train an autoregressive SLM from scratch.
- Do not make Qnet a dependency.
- Do not use themes as proof of activation.
- Do not make every same-coalition pair a positive edge.
- Do not use a global top-N queue that leaves branches unvisited.
- Do not force coalitions to be cliques; many valid mechanisms are chains or
  sparse role graphs.
- Do not force all findings into one totalizing metaphor.
- Do not use a language model's prose quality as evidence that search worked.
- Do not add a UI before the mechanical feasibility result exists.

## 8. Architecture Overview

```text
Furūq clean quranic branches (10,820)
          |
          v
canonical branch export + deterministic views/facets
          |
          +-----------------------+
          |                       |
          v                       v
sparse Arabic/English views   fixed dense multilingual views
          |                       |
          +----------+------------+
                     v
        separate global neighbor graphs/statistics
                     |
QAC + Quran window -> passage branch inventory
                     |
                     v
       exact passage-local multi-view affinities
                     |
                     v
 restart diffusion + independent-root aggregation
                     |
                     v
     per-seed activation traces and contributors
                     |
                     v
 bounded overlapping coalition extraction
                     |
                     v
 internal controls -> freeze -> blind reference evaluation
                     |
          optional self-supervised escalation
```

## 9. Proposed Implementation Layout

The cold agent should create a new isolated package rather than modifying v11
or v12 in place:

```text
v14/
  README.md
  pyproject.toml
  configs/
    baseline.yaml
    lexical_only.yaml
    dense_fixed.yaml
    self_supervised.yaml
  schemas/
    branch-record.schema.json
    graph-edge.schema.json
    passage-inventory.schema.json
    activation-trace.schema.json
    coalition.schema.json
    frozen-run.schema.json
  src/latent_activation/
    __init__.py
    corpus.py
    passage.py
    views.py
    sparse_embed.py
    dense_embed.py
    neighbors.py
    graph.py
    activation.py
    coalitions.py
    controls.py
    freeze.py
    evaluate.py
    io.py
  scripts/
    export_corpus.py
    build_views.py
    embed_corpus.py
    build_neighbors.py
    build_passage.py
    activate_passage.py
    extract_coalitions.py
    run_controls.py
    freeze_run.py
    evaluate_frozen_run.py
  tests/
  artifacts/             # ignored; reproducible derived data
  runs/                  # run manifests and compact outputs
```

Expected size:

- feasibility prototype: 500-900 lines;
- clean reusable baseline: 1,500-2,500 production lines;
- self-supervised training, evaluation, and tests: 3,000-5,000 total lines.

Do not copy large model caches or dense matrices into Git.

## 10. Canonical Data Contracts

### 10.1 Branch record

Minimum JSONL record:

```json
{
  "branch_key": "root_001444:B007",
  "root_id": "root_001444",
  "root_norm": "...",
  "branch_id": "B007",
  "origin_corpus": "quranic",
  "image_ar": "...",
  "scope_ar": "...",
  "image_en": "...",
  "scope_en": "...",
  "what_is_not_ar": "...",
  "source_phrase_ar": "...",
  "source_refs": "...",
  "views": [],
  "source_hash": "sha256:..."
}
```

Never use only `root_norm + branch_id` as global identity. Preserve `root_id`.

### 10.2 Deterministic views

Initial views must be derivable without interpretive examples:

```text
image_ar
scope_ar
image_ar + scope_ar
image_en
scope_en
image_en + scope_en
source_phrase_ar
deterministic clause/facet segments
```

Do not concatenate every field into one long embedding and discard the
individual vectors. Concrete facets can disappear through mean pooling.

Initial facetization should be deterministic:

- split on semicolons and strong clause separators;
- retain the parent branch ID and facet index;
- discard no source text;
- hash the exact source substring;
- do not summarize or invent roles in Phase 1.

### 10.3 Graph edge

```json
{
  "source_branch_key": "...",
  "target_branch_key": "...",
  "view": "dense_scope_ar",
  "relation": "similarity",
  "directed": false,
  "raw_score": 0.0,
  "local_scaled_score": 0.0,
  "source_rank": 0,
  "target_rank": 0,
  "mutual_knn": true,
  "provenance": "fixed_encoder:model@revision"
}
```

Keep view-specific graphs separate. Do not prematurely average Arabic lexical,
English lexical, dense semantic, and later role-compatibility scores.

### 10.4 Passage inventory

Must contain:

- surah and ayah range;
- Arabic text;
- QAC word/morpheme order;
- root-bearing occurrences;
- resolved root IDs;
- all clean quranic branches for those roots;
- absent/missing root records;
- resource hashes.

Reuse QAC-first root-resolution principles from v11/v12 where possible, but do
not import Qnet requirements.

### 10.5 Activation trace

```json
{
  "seed_branch_key": "...",
  "target_branch_key": "...",
  "iteration": 0,
  "activation": 0.0,
  "restart_component": 0.0,
  "root_support": [
    {
      "supporting_root_id": "...",
      "supporting_branch_key": "...",
      "edge_view": "...",
      "contribution": 0.0
    }
  ],
  "backpointers": [],
  "configuration_hash": "..."
}
```

### 10.6 Coalition

```json
{
  "coalition_id": "...",
  "seed_branch_key": "...",
  "members": [],
  "distinct_roots": [],
  "edges": [],
  "score_vector": {
    "connectivity": 0.0,
    "root_diversity": 0.0,
    "view_agreement": 0.0,
    "activation_support": 0.0,
    "stability": 0.0,
    "passage_structure": 0.0,
    "hub_penalty": 0.0,
    "redundancy_penalty": 0.0,
    "inference_cost": 0.0
  },
  "supplied_relations": [],
  "inferred_relations": [],
  "open_roles": [],
  "rank_for_seed": 0
}
```

The baseline does not need to name a scene. Scene naming is downstream and
must not influence coalition search.

## 11. Representation Plan

### 11.1 Sparse corpus-derived baselines

Build these before downloading a dense model:

1. Arabic word and character n-gram TF-IDF.
2. English word and character n-gram TF-IDF.
3. Rare-content-token overlap with inverse branch frequency.
4. Exact shared source forms as a diagnostic channel, not a decisive score.

Sparse baselines establish what can be recovered from the branch corpus alone.
They also expose translation-view disagreements and generic hub terms.

### 11.2 Fixed dense baseline

Recommended first checkpoint: `intfloat/multilingual-e5-small`.

Verified public model facts:

- 12 layers;
- hidden size 384;
- approximately 471 MiB weights;
- multilingual model card lists 94 languages;
- MIT license.

Comparison checkpoint if resources permit:

- `intfloat/multilingual-e5-base`;
- 12 layers;
- 768-dimensional embeddings;
- approximately 0.3B parameters and 1.11 GiB weights;
- model card notes potential degradation for lower-resource languages.

Optional heavier comparison:

- `BAAI/bge-m3`;
- 1,024-dimensional dense output;
- supports dense, sparse, and multi-vector modes;
- approximately 2.27 GiB weights;
- not the first local target.

Record the exact model revision, tokenizer revision, pooling method, prefixes,
maximum length, truncation count, dtype, normalization, and batch size.

For E5, use the model-card-required `query:`/`passage:` prefixes consistently.
Because this is symmetric branch matching, run and document at least one
consistent symmetric prefix treatment rather than silently mixing roles.

### 11.3 Multi-vector branch representation

For each branch, retain one vector per field/view and optionally one per
deterministic facet. Candidate generation should use union or late interaction,
not only an average branch vector.

Initial candidate rule:

```text
candidate(i, j) if j is top-K for i in any allowed view
                 or i/j form a mutual local passage neighbor
```

Do not use a single global threshold. Embedding neighborhoods have variable
density and hubness.

### 11.4 Local scaling and hub control

For each view:

1. L2-normalize embeddings.
2. Compute exact cosine scores blockwise.
3. Retain top `K in {32, 64, 128}` during robustness experiments.
4. Compute per-node local density from its Kth neighbor or mean top-K score.
5. Produce a locally scaled score such as a CSLS-style correction.
6. Mark mutual KNN edges.
7. Record node degree, reciprocal degree, and hubness.

Never delete broad branches merely for being broad. Preserve their edges but
penalize or normalize their dominance during ranking.

## 12. Passage-Local Graph Construction

The global 10,820-node graph is useful for density and general neighborhood
statistics. The actual evidence set for a passage is much smaller.

For each passage:

1. Resolve surface roots through QAC.
2. Load every clean quranic branch belonging to those root IDs.
3. Compute the exact local all-pairs score for each representation view from
   stored embeddings. This is cheap even for 144-500 branches.
4. Exclude same-root edges in the primary cross-root graph; retain same-root
   edges as a separately labeled channel.
5. Create per-branch local top-K edges, not a global top-N list.
6. Preserve at least a small candidate budget per branch and per other root so
   rare branches are not starved.

Two propagation treatments must remain distinct:

### Evidence-closed treatment

Only passage branches can be intermediate or returnable nodes. This is the
primary treatment and has the cleanest evidence interpretation.

### Global-bridge treatment

All 10,820 nodes may act as semantic intermediate nodes, but only passage
branches may be returned as activated evidence. Intermediate branches are never
reported as passage evidence. This is an optional ablation because it imports
lexical material belonging to absent roots into the propagation path.

Do not mix results from these treatments.

## 13. Iterative Activation

### 13.1 Linear restart baseline

Let `W` be a nonnegative, degree-normalized sparse affinity matrix and `s` a
seed vector.

```text
a(t+1) = (1 - alpha) * s + alpha * W * a(t)
```

Initial untuned grid:

```text
alpha in {0.75, 0.85, 0.90}
max_iterations = 100
convergence_tolerance = 1e-7
```

This sums support over weighted walks without explicit DFS. Restart limits
semantic drift.

Run every passage branch as a seed, in batches. Do not seed only the presumed
primary branch.

### 13.2 Independent-root aggregation

A root with 20 branches must not contribute 20 times more activation merely
because its inventory is large.

For target branch `j` and supporting root `r`:

```text
root_support(r, j) = max over branch i belonging to r
                     of W(i, j) * activation(i)
```

Then aggregate only the strongest distinct-root supports:

```text
diverse_support(j) = sum of top q root_support(r, j)
```

Initial `q` grid:

```text
q in {2, 3, 4}
```

This is the first explicit approximation to combinatorial activation: a branch
rises when several independent roots converge on it.

Keep the linear diffusion score and root-diverse score as separate components.
Do not immediately collapse them into one scalar.

### 13.3 Backpointers

For every high activation, retain:

- top contributing roots;
- top branch from each root;
- edge view and score;
- hop count;
- restart versus propagated mass;
- alternative contributors.

These traces are required for coalition reconstruction and audit.

### 13.4 Why raw DFS is not the primary algorithm

Threshold DFS can drift through a chain where each local pair is close but the
endpoints do not form one scene. It also enumerates the same set in many orders.

Diffusion evaluates all bounded walks efficiently. Explicit set search begins
only after diffusion narrows and scores candidate members.

## 14. Coalition Extraction

### 14.1 Search unit

Search states are sets, not paths:

```text
state = {
  selected branch keys,
  distinct roots,
  connecting edges,
  activation contributors,
  score vector,
  optional open roles
}
```

### 14.2 Initial bounds

Declare these before gold evaluation:

```text
coalition size:             3 to 8 branches
minimum distinct roots:    3
maximum branches per root: 2
beam width:                 200
top coalitions per seed:    10
maximum expansion depth:    8
diversity Jaccard ceiling:  0.70
```

These are engineering defaults, not truth claims. Robustness runs vary them
without looking at gold.

### 14.3 Expansion rule

A new member may enter when at least one of these holds:

- it has a strong edge to a selected member in any representation view;
- it receives strong activation from at least two selected roots;
- it connects two previously disconnected selected components;
- in a later proposition-graph treatment, it fills an explicit open role.

Require cumulative coalition coherence. Do not accept indefinite chains solely
because each latest hop exceeds a local threshold.

### 14.4 Unsupervised score vector

Keep a vector through search and use Pareto or lexicographic pruning before
experimenting with scalar weights:

```text
connectivity             weighted connectedness / spanning support
root_diversity           number and balance of independent roots
view_agreement           support across Arabic/English/sparse/dense views
activation_support       diffusion and root-diverse activation
edge_rarity              preference for informative rather than ubiquitous edges
passage_structure        adjacency, repetition, order, and occurrence support
stability                survival across K/alpha/view perturbations
hub_penalty              generic high-degree domination
redundancy_penalty       members adding no new connection or role
inference_cost           unsupported or model-supplied glue
```

Passage structure may rank already discovered coalitions. It must not invent a
lexical edge absent from all representation views.

### 14.5 Overlap and multiplicity

Coalitions can overlap. Do not use a partitioning algorithm that forces every
branch into exactly one cluster. Return several diverse candidates and preserve
rival realizations.

### 14.6 Branch coverage output

For every passage branch, report:

```text
top diverse coalitions
top independent-root activators
best score vector
whether it was isolated
whether it was suppressed only by a bound
whether evidence was lexical, dense, structural, or inferred
```

This coverage index is closer to the ultimate goal than a single passage-level
ranking.

## 15. Zero-Gold Self-Supervised Escalation

Do not execute this section until the fixed baseline is frozen and diagnosed.

### 15.1 What unsupervised learning can and cannot learn

Self-supervision can improve representation of signals already present in:

- branch wording;
- Arabic/English paired views;
- dictionary propositions;
- branch-to-concept graph structure;
- repeated lexical relations.

It cannot infer an arbitrary relation between two branches when the complete
available corpus contains no lexical, structural, relational, or general-world
signal connecting them.

There are only four sources for such a connection:

1. evidence inside the branch corpus;
2. general knowledge inside a pretrained model;
3. a larger external corpus;
4. human/gold supervision.

Every treatment must state which sources it uses.

### 15.2 TSDAE-style domain adaptation

An optional text-encoder adaptation may corrupt branch text and reconstruct the
original through an embedding bottleneck. This uses no coalition labels.

Purpose:

- adapt a pretrained encoder to short Arabic/English lexicographic prose;
- improve robustness to clause deletion and field variation.

Risk:

- reconstruction can improve branch identity without improving cross-branch
  compatibility;
- the small corpus can overfit;
- training checkpoints require external GPU/storage.

Compare fixed versus adapted encoders using only internal stability controls
before unsealing gold.

### 15.3 Heterogeneous proposition graph

If dense similarity misses complementary roles, construct a graph with node
types such as:

```text
branch
facet
entity/material
action/process
instrument
agent/recipient
location
state/property
outcome
```

Allowed relation types may include:

```text
contains
used_for
acts_on
instrument_of
located_in
supports
precedes
moves_toward
produces
blocks
contrasts_with
```

Initial relation extraction must be source-grounded. Options, in increasing
order of external prior:

1. deterministic lexical/concept extraction;
2. frozen off-the-shelf parser;
3. frozen language model constrained to a fixed extraction schema.

Any model-extracted proposition must retain the exact source substring and be
auditable. The extractor must not see Quran windows or gold scenes.

### 15.4 Masked graph autoencoding

Once the proposition graph exists, self-supervised graph learning can mask
branch-concept, node-feature, or relation edges and reconstruct them.

This may learn multi-hop role compatibility without direct coalition labels.
It still cannot repair a wrongly constructed source graph.

### 15.5 Contrastive-learning warning

Do not treat every other branch in a batch as a negative. Complementary branches
are precisely the pairs that may be semantically different but scene-compatible.
Standard instance discrimination can push them apart.

Safe positive views include:

- Arabic and English fields of the same branch;
- image and scope fields of the same branch;
- independently corrupted views of the same facet.

Use cross-branch negatives only when the relation is known from source structure
or as a separately declared heuristic treatment.

## 16. Internal Evaluation Without Gold

Gold-free development cannot establish interpretive truth. It can establish
representation health, robustness, and nontriviality.

### 16.1 Corpus checks

- exactly 10,820 records;
- unique branch keys;
- all required fields nonempty;
- deterministic stable hashes;
- no review/contaminated/non-quranic rows;
- no truncation without a recorded flag.

### 16.2 Embedding checks

- finite vector for every view;
- expected dimension;
- L2 norm after normalization approximately 1;
- repeated run hash equality;
- Arabic/English same-branch retrieval diagnostics;
- facet-to-parent consistency;
- no single vector repeated across many unrelated branches.

### 16.3 Graph checks

- degree distributions per view;
- reciprocal-edge rate;
- connected component sizes;
- giant-component share;
- isolated-node share;
- hub concentration;
- root-level degree bias;
- stability across K = 32/64/128;
- stability across Arabic-only, English-only, and combined treatments.

### 16.4 Null controls

Run at least:

1. shuffled branch-text-to-ID assignment;
2. shuffled root membership;
3. random passage root sets matched by inventory size;
4. edge-weight permutation preserving degree;
5. field-drop perturbations;
6. Arabic-only versus English-only disagreement analysis.

Meaningful coalitions should weaken under destructive controls and remain
reasonably stable under benign perturbations.

### 16.5 Search checks

- every seed branch was processed;
- no set emitted twice in different member order;
- all returned members belong to passage roots in the evidence-closed treatment;
- all edges refer to existing branch keys;
- every score component is reproducible;
- bounds and suppressed candidates are recorded;
- no scene label or prose affects ranking.

## 17. Freeze and Gold Protocol

### 17.1 Why gold is retained

Without any external reference, the system can optimize stable but irrelevant
structure. Gold is therefore retained as a blind measurement, not a target.

### 17.2 Before unsealing

Freeze:

- Git commit or complete patch hash;
- branch-corpus SHA-256;
- QAC and Quran resource hashes;
- exact model and tokenizer revisions;
- dependency lockfile;
- all configuration values;
- random seeds;
- graph artifact hashes;
- passage packages;
- activation and coalition outputs;
- internal-control report;
- explicit statement that gold paths were not read.

Use a script patterned after v12 frozen-run manifests.

### 17.3 Blind evaluation roles

Use a fresh evaluation agent or human after freeze. That evaluator may read:

- frozen mechanical outputs;
- sealed reference files;
- evaluation rubric.

The builder/orchestrator must not modify the frozen treatment after seeing
reference results. Any change creates a new treatment and requires a separate
held-out reference set.

### 17.4 Reference metrics

Where reference branch coalitions can be extracted:

```text
gold-member recall@20 and recall@50 per seed
rank of each reference member
coalition connectivity within 2 and 3 hops
best top-10 coalition overlap
reference coalition recall@10 and @20
unsupported-member rate
activation lift from seed-only to multi-root propagation
```

Human assessment should separately score:

- lexical grounding;
- passage specificity;
- complementary role completion;
- reading change;
- unsupported inference;
- generic thematic drift;
- novelty without target imitation.

### 17.5 Diagnostic use of gold

After evaluation, gold may identify generic failure classes:

```text
candidate edge absent
edge present but diffusion failed
activation present but coalition search failed
coalition found but ranking failed
evidence trace incomplete
```

Fix the generic layer, not the specific scene. Evaluate the new treatment on a
different sealed surah/root split.

### 17.6 Supervised fallback

Only if zero-gold approaches fail and the user explicitly authorizes it:

1. partition reference material by entire surah and preferably root family;
2. use one partition for training/calibration;
3. use a second for model selection;
4. keep a final partition sealed;
5. never randomly split pair rows from the same coalition across partitions.

This fallback is a new project treatment, not a continuation of the zero-gold
claim.

## 18. Detailed Execution Phases

Each phase has deliverables and a hard gate. The coordinator must not skip a
failed gate.

### Phase 0: Move and preflight

Purpose: create a safe execution environment.

Actions:

1. Move/clone the repository to a volume with adequate free space.
2. Run `git status --short` and preserve user changes.
3. Require `df -h .` to show at least 5 GiB free for the fixed baseline.
4. Use Python 3.10, not the current Python 3.14, for ML compatibility.
5. Create an isolated virtual environment.
6. Set model/cache paths to the roomy volume.
7. Install dependencies with pinned versions.
8. Download one small fixed embedding checkpoint only after approval.

Suggested initial dependencies:

```text
numpy
scipy
scikit-learn
pandas
torch
transformers
sentence-transformers
networkx
jsonschema or pydantic
pytest
```

FAISS is optional and unnecessary at 10,820 nodes. Exact block matrix
multiplication is sufficient.

Gate:

- enough disk;
- Python 3.10 environment imports successfully;
- model loads and embeds a three-record canary;
- no sealed reference file was opened.

### Phase 1: Package and contracts

Purpose: create the minimal `v14` package, schemas, configuration loader, and
tests before model work.

Actions:

1. Create the layout in Section 9.
2. Add `pyproject.toml` and lock dependencies.
3. Add schema validation and atomic JSONL writers.
4. Add deterministic hashing helpers.
5. Add tests for identity, Unicode, stable ordering, duplicate detection, and
   invalid rows.

Gate:

- tests pass without model download;
- no large artifacts are tracked by Git;
- generated paths are ignored appropriately.

### Phase 2: Canonical corpus export

Purpose: freeze the 10,820-branch source inventory.

Actions:

1. Execute the exact SQL selection in Section 3.3.
2. Build canonical JSONL records.
3. Create deterministic facets/views.
4. Emit summary statistics and field-length distributions.
5. Hash source DB and export.

Gate:

```text
records = 10,820
unique branch keys = 10,820
roots = 1,688
missing required fields = 0
wrong origin/status/contamination = 0
```

### Phase 3: Sparse lexical baseline

Purpose: establish corpus-only recovery before external semantic priors.

Actions:

1. Fit Arabic character/word TF-IDF.
2. Fit English character/word TF-IDF.
3. Compute blockwise top-K similarities.
4. Produce view-specific mutual-KNN graphs and diagnostics.
5. Run null controls.

Gate:

- all branch nodes represented;
- graph statistics are finite and reproducible;
- no catastrophic single hub or all-node component caused solely by stopwords;
- destructive nulls materially reduce stable structure.

### Phase 4: Fixed dense baseline

Purpose: add general semantic priors without target supervision.

Actions:

1. Pin and record `multilingual-e5-small` revision.
2. Embed every separate branch view and facet.
3. Record truncations and batch timing.
4. Normalize and save compact arrays.
5. Build top-K graphs blockwise.
6. Compare Arabic/English/combined graph health.

Gate:

- all 10,820 records embedded;
- no NaN/Inf;
- deterministic output within declared tolerance;
- same-branch cross-view retrieval is nontrivial;
- graph is not dominated by a few generic branches.

### Phase 5: Passage builder

Purpose: create clean passage-local evidence packages without Qnet.

Actions:

1. Reuse/port QAC root resolution from v12 where appropriate.
2. Build arbitrary surah/ayah-window packages.
3. Attach all clean quranic branches for resolved roots.
4. Compute exact local affinity matrices from stored representations.
5. Emit per-view passage graphs and branch-coverage diagnostics.

Gate:

- S1 package contains the expected 18 surface roots and 144 accepted branches
  under the v12 selection policy;
- all returned branches map to surface root IDs;
- no Qnet dependency;
- missing roots are explicit.

### Phase 6: Activation engine

Purpose: seed every passage branch and compute iterative support.

Actions:

1. Implement restart diffusion.
2. Implement degree normalization.
3. Implement independent-root max aggregation.
4. Batch all seed vectors.
5. Store compact top activations and backpointers.
6. Run K/alpha/q robustness grid.

Gate:

- every passage branch seeded;
- convergence or declared iteration limit reached;
- same input/config produces same output;
- root inventory size does not linearly dominate support;
- shuffled controls reduce coherent convergence.

### Phase 7: Coalition search

Purpose: turn activation neighborhoods into overlapping branch sets.

Actions:

1. Implement canonical set-state identity.
2. Implement bounded beam/best-first expansion.
3. Retain score vectors and evidence edges.
4. Enforce root and size bounds.
5. Apply diversity filtering.
6. Emit top coalitions per seed plus silence/suppression records.

Gate:

- every member is valid and passage-scoped;
- no duplicate member set in different order;
- every coalition is connected under declared edge semantics;
- every score is reconstructable;
- no scene name or reference prose affected search.

### Phase 8: Internal controls and freeze

Purpose: finish the zero-gold treatment before any target comparison.

Actions:

1. Run all internal controls in Section 16.
2. Produce graph, activation, and search diagnostics.
3. Decide whether the treatment is stable enough to evaluate.
4. Freeze code/config/resources/model/artifacts.
5. Create a signed or hashed frozen-run manifest.

Gate:

- all declared artifacts hashed;
- working tree state recorded;
- no gold/reference access occurred;
- evaluator can reproduce compact outputs from the manifest.

### Phase 9: Blind evaluation

Purpose: determine whether the unsupervised treatment approaches the intended
phenomenon.

Actions:

1. Start a fresh evaluator.
2. Provide frozen outputs and sealed references.
3. Extract reference branch sets without changing the treatment.
4. Compute mechanical metrics.
5. Conduct domain review of top candidates and false activations.
6. Classify failures by pipeline layer.

Gate/outcome:

- `PASS`: known distributed coalitions are reachable and rank usefully;
- `PARTIAL`: candidate recall exists but activation/search/ranking needs work;
- `FAIL-REPRESENTATION`: decisive reference members are absent from candidate
  neighborhoods;
- `FAIL-EVIDENCE`: recovered sets rely on unsupported glue.

### Phase 10: Conditional self-supervised escalation

Enter only for `FAIL-REPRESENTATION` or systematic domain mismatch.

Actions:

1. Choose TSDAE-style text adaptation, proposition graph, or masked graph
   reconstruction based on the diagnosed missing signal.
2. Use external GPU/storage.
3. Keep gold sealed for the new treatment.
4. Repeat Phases 4-9 with a new treatment ID.

Do not self-supervise merely because a neural stage was planned. The baseline
may already be adequate.

## 19. Orchestration Instructions for a Cold Agent

### 19.1 Coordinator responsibilities

The primary orchestrator owns:

- scientific-contract enforcement;
- sealed-reference discipline;
- phase gates;
- task assignment and file ownership;
- integration and code review;
- test execution;
- artifact and model provenance;
- freezing and handoff to evaluation;
- final feasibility judgment.

The coordinator must read this entire plan before editing.

### 19.2 Recommended agent decomposition

When multiple agents are available, use bounded ownership:

#### Agent A: corpus and contracts

Owns:

```text
corpus.py
views.py
branch/passsage schemas
export/build scripts
data-integrity tests
```

May read raw SQLite/Quran/QAC resources. May not read sealed outputs.

#### Agent B: representations and graph

Owns:

```text
sparse_embed.py
dense_embed.py
neighbors.py
graph.py
representation tests and diagnostics
```

Consumes only Agent A's canonical export and schemas.

#### Agent C: activation and coalition search

Owns:

```text
activation.py
coalitions.py
activation/search tests
compact trace outputs
```

Consumes frozen toy fixtures first, then Agent B's graph contract.

#### Coordinator: controls, freeze, integration

Owns:

```text
controls.py
freeze.py
evaluate.py scaffolding
configuration
CI/test orchestration
documentation
```

A separate fresh evaluator handles gold only after freeze.

### 19.3 Parallelism rules

- Do not have agents edit the same files.
- Freeze schemas before parallel implementation depends on them.
- Agents may create fixtures conforming to schemas, not private variants.
- Coordinator reviews every merge and runs the full test suite.
- At most one agent owns dependency/environment changes.
- No implementation agent opens reference outputs.
- Do not parallelize interpretive analysis before mechanical outputs are frozen.

### 19.4 User updates

The orchestrator should report:

- current phase;
- facts learned, not generic progress;
- gate pass/fail;
- artifact paths;
- blockers requiring disk, network, model download, or GPU approval;
- any deviation from the zero-gold contract.

### 19.5 Git discipline

- Inspect `git status` before work.
- Preserve user changes.
- Never reset or overwrite unrelated work.
- Keep generated arrays, caches, dense matrices, and checkpoints out of Git.
- Commit code/config/schema separately from generated experiment manifests when
  publishing is requested.
- Record exact diffs in the frozen manifest.

## 20. Failure Diagnosis Matrix

| Symptom | Likely layer | Required response |
| --- | --- | --- |
| Same-branch Arabic/English views do not align | representation | inspect field construction, prefixes, truncation, encoder suitability |
| Generic branches dominate every neighborhood | graph | local scaling, degree normalization, stopword/content handling |
| Reference members absent after blind evaluation | representation/candidate generation | add role/proposition channel or self-supervised adaptation |
| Members present but activation ranks them low | activation | inspect restart, root-diverse aggregation, view combination |
| Activations are good but sets are fragmented | coalition search | adjust set expansion/connectivity without changing embeddings |
| Every passage yields similar scenes | external-prior/hub bias | null controls, passage specificity, hub penalty, evidence closure |
| Arabic and English treatments disagree strongly | translation/domain issue | preserve separate views; audit source fields; do not average blindly |
| Long semantic chains drift | activation/search | stronger restart, hop bound, cumulative coherence, inference cost |
| Valid chain rejected for not being a clique | search objective | allow connected sparse role graphs |
| Root with many branches dominates | aggregation | max/top-q support per distinct root |
| Self-supervision improves reconstruction only | training objective | stop; do not infer compatibility gain from loss alone |
| Gold result improves only after target-specific edits | leakage | invalidate treatment; move to a different sealed test split |
| Disk fills during setup | environment | stop; relocate cache/venv; never delete user data without approval |

## 21. Major Risks and Mitigations

### Risk: similarity is not complementarity

Mitigation: separate representation views; later add source-grounded role graph;
evaluate chains rather than only cliques.

### Risk: classical Arabic lexicographic domain shift

Mitigation: Arabic and English views; sparse baselines; truncation audit;
conditional TSDAE-style adaptation.

### Risk: whole-branch embedding dilutes facets

Mitigation: deterministic multi-vector facets; late-interaction candidate union.

### Risk: global KNN excludes passage-relevant neighbors

Mitigation: retain global density statistics but compute exact passage-local
pair scores.

### Risk: hubness creates generic thematic soup

Mitigation: mutual KNN, local scaling, degree normalization, per-root support,
hub diagnostics, score-vector penalties.

### Risk: gold leakage

Mitigation: denylist, separate builder/evaluator, freeze before reference access,
new treatment and new held-out split after any diagnostic change.

### Risk: unsupervised stability is mistaken for truth

Mitigation: blind post-freeze reference evaluation and domain review.

### Risk: proposition extractor hallucinates relations

Mitigation: source-span requirement, typed schema, inference labeling, human
sampling, and no extractor access to passage/gold context.

### Risk: compute/storage overengineering

Mitigation: 10,820 exact corpus; blockwise top-K; no vector database; one small
checkpoint; external GPU only after a failed fixed baseline.

## 22. Acceptance Criteria

### Baseline engineering acceptance

- Exact 10,820 clean quranic branches exported.
- Every branch has all declared views and hashes.
- Sparse and dense embeddings are reproducible.
- Every passage branch receives per-view local neighbors.
- Every passage branch is used as an activation seed.
- Root-diverse support is recorded.
- Top-K diverse coalitions or explicit silence exist for every seed.
- All outputs validate against schemas.
- No Qnet dependency.
- No gold/reference input before freeze.

### Scientific feasibility acceptance

After blind evaluation, at least one fixed treatment must show:

- nontrivial recovery beyond sparse lexical overlap;
- multi-root activation lift;
- connected recovery of known distributed coalition members;
- stability across benign perturbations;
- collapse under destructive null controls;
- acceptable unsupported-inference rate;
- findings that differ across passages rather than repeating generic scenes.

Do not set numerical pass thresholds from known S1 results before the first
freeze. The evaluator may report metrics and recommend thresholds for a new,
separately held-out treatment.

## 23. Stop Conditions

Stop and report rather than silently weakening the experiment when:

- the canonical branch count is not 10,820;
- required source fields are missing;
- root resolution is ambiguous or incomplete;
- model revision cannot be pinned;
- free disk is below the phase requirement;
- a download/install fails because of restricted network access;
- a sealed reference was accidentally read before freeze;
- graph outputs contain NaN/Inf or unstable branch identity;
- generated edges cannot cite source views;
- the only way to recover a target is to name or encode it explicitly;
- training would require unavailable GPU/storage.

Accidental gold exposure invalidates the zero-gold treatment for that agent and
configuration. Start a fresh builder treatment or classify the run honestly as
reference-informed.

## 24. Cold-Start Runbook

A cold orchestrator should follow this exact order:

1. Read this plan completely.
2. Read root `README.md`, v11/v12 mechanical resource documentation, and source
   schemas only. Do not read run interpretations.
3. Run `git status --short` and record branch/commit.
4. Run `df -h .`; require phase-appropriate space.
5. Verify `resources/furuq_v4.sqlite`, `resources/qac.sqlite`, and
   `resources/quran/` exist.
6. Execute the branch-count SQL and require 10,820 quranic clean branches.
7. Create the `v14` package and schemas.
8. Implement and test canonical corpus export.
9. Implement sparse lexical views and internal diagnostics.
10. Obtain approval for dependencies/model download.
11. Create Python 3.10 environment on the roomy volume.
12. Pin/download one fixed small multilingual encoder.
13. Build dense multi-view embeddings and blockwise neighbor graphs.
14. Build the passage package without Qnet.
15. Implement exact passage-local graph construction.
16. Implement batched restart diffusion and root-diverse aggregation.
17. Implement bounded coalition extraction and branch coverage outputs.
18. Run null controls and robustness grids without gold.
19. Freeze everything and produce a manifest.
20. Start a fresh evaluator and only then open reference outputs.
21. Classify the result as pass, partial, representation failure, search
    failure, or evidence failure.
22. Escalate to self-supervised learning only when the diagnosis warrants it.

## 25. Initial Decision Log

These decisions are already made unless the user explicitly changes them:

1. Initial corpus is the 10,820 clean accepted `quranic` branches.
2. Qnet is not a dependency.
3. Gold is blind evaluation, not initial training or tuning.
4. A fixed pretrained encoder is permitted as a declared external prior.
5. Sparse corpus-only baselines are mandatory.
6. Multi-view representations remain separate through candidate generation.
7. Dense global matrices are not persisted by default.
8. Passage-local exact affinities are computed from stored embeddings.
9. Every branch is seeded; no global top-N starvation.
10. Diffusion precedes explicit coalition search.
11. Independent-root aggregation prevents large-root domination.
12. Coalitions are overlapping connected sets, not necessarily cliques.
13. Self-supervised training is conditional, not automatic.
14. An SLM is not trained from scratch.
15. Natural-language explanation is downstream of frozen mechanical discovery.

## 26. Handoff Report Template

At the end of each treatment, the orchestrator should produce:

```text
Treatment ID:
Git commit/diff hash:
Corpus hash and record count:
QAC/Quran hashes:
Model ID and immutable revision:
Dependency lock hash:
Configuration hash:
Allowed inputs:
Sealed inputs:
Gold exposure declaration:
Representation views:
Graph policy:
Activation policy:
Coalition bounds:
Internal controls:
Artifact paths and hashes:
Runtime and peak storage:
Gate results:
Blind evaluation status:
Failure classification:
Recommended next treatment:
```

## 27. Feasibility Summary

### Technically

High feasibility. Ten thousand eight hundred twenty branches are small enough
for exact blockwise similarity, sparse graph storage, batched diffusion, and
passage-local connected-set search on one workstation.

### Scientifically

Moderate uncertainty. Off-the-shelf embeddings optimize semantic relevance or
similarity, not necessarily complementary scene roles. The first frozen
experiment must determine whether the raw branch prose and general pretrained
semantics already connect the desired coalitions. If not, source-grounded
proposition structure or self-supervised graph learning is the justified next
step.

### Operationally on the current machine

Code development is possible. A safe local fixed-encoder run is blocked by
free disk and missing dependencies/model weights. Self-supervised training
should occur after moving to a larger volume and preferably on an external GPU.

### Expected elapsed work after code exists

- automated corpus, embedding, graph, and passage runs: hours;
- initial result and feasibility review: one to three days;
- representative blind domain evaluation: several additional days;
- full human audit is optional and can take substantially longer.

## 28. Primary Technical References

- Multilingual E5 technical report:
  <https://arxiv.org/abs/2402.05672>
- Multilingual-E5-small model card:
  <https://huggingface.co/intfloat/multilingual-e5-small>
- Multilingual-E5-base model card:
  <https://huggingface.co/intfloat/multilingual-e5-base>
- BGE-M3 paper:
  <https://arxiv.org/abs/2402.03216>
- BGE-M3 model card:
  <https://huggingface.co/BAAI/bge-m3>
- TSDAE unsupervised sentence-embedding adaptation:
  <https://aclanthology.org/2021.findings-emnlp.59/>
- Deep Graph Infomax:
  <https://arxiv.org/abs/1809.10341>
- Masked graph autoencoder:
  <https://arxiv.org/abs/2201.02534>
- GraphMAE2:
  <https://arxiv.org/abs/2304.04779>
- Set Transformer, if a later candidate-set reranker is trained:
  <https://arxiv.org/abs/1810.00825>

## 29. Final Instruction to the Cold Agent

Treat this as a candidate-recall and structured-search research project, not as
a prose-generation project. Build the smallest frozen zero-gold system that can
demonstrate whether branch representations contain the required multi-root
connectivity. Preserve every decision and every failure. Do not make the result
look successful by importing the motivating images. The first honest negative
result is valuable because it identifies whether the missing ingredient is
representation, activation, coalition search, or evidence itself.
