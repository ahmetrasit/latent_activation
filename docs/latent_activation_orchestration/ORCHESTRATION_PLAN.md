# Complete Branch Distance Matrices: Cold-Agent Orchestration Plan

Status: execution-ready matrix-build plan

Prepared: 2026-07-19

Implementation namespace: `v14/`

## 0. Executive Decision

Build complete reusable pairwise distance matrices for the 10,820 clean accepted
Quranic branch records. Do not build an ayah-analysis system.

The canonical deliverables are:

1. one stable 10,820-row node inventory;
2. four normalized 384-dimensional embedding arrays;
3. one complete semantic distance matrix;
4. one complete thematic-proxy distance matrix;
5. one complete fixed 50/50 combined distance matrix;
6. deterministic validation reports and a content-addressed manifest.

Every matrix is `10,820 x 10,820`, symmetric, float32, and aligned to the same
node order. Nothing is pruned. Downstream consumers may construct graphs,
threshold neighborhoods, run iterative activation, or perform other searches
without requiring this project to choose those policies.

Do not train an SLM or encoder in the first treatment. Do not use Qnet. Do not
reuse a branch loader that merges source rows or combines origin corpora.

## 1. Correct Scope

### 1.1 In scope

- canonical export of the quranic branch subset;
- stable and auditable node identity;
- deterministic text-view construction;
- fixed multilingual encoding;
- exact blockwise all-pairs cosine computation;
- complete matrix persistence;
- engineering and gold-free representation checks;
- immutable manifests, hashes, and reproducibility evidence;
- an external interface for downstream consumers to read a row or submatrix.

### 1.2 Out of scope

- resolving roots for a passage or ayah window;
- choosing branches for a passage;
- threshold selection;
- nearest-neighbor index production as a canonical artifact;
- sparse graph construction;
- diffusion, spreading activation, or random walks;
- depth-first, beam, or coalition search;
- scene or mechanism extraction;
- interpreting Quranic text;
- prose generation;
- supervised, self-supervised, or SLM training;
- tuning against known motifs, gold coalitions, or prior outputs.

Diagnostic nearest-neighbor calculations are allowed only as ephemeral matrix
checks. They must not replace or modify the complete matrices.

### 1.3 Why the full matrix is the correct first artifact

For `n = 10,820`, all pairwise entries total:

```text
n^2 = 117,072,400
```

This is large enough to make manual combinatorial reasoning impractical but
small enough to compute and persist exactly. A full matrix preserves:

- every weak or unexpected relation;
- arbitrary thresholds selected later;
- consumer-specific top-K values;
- exact comparisons between representation treatments;
- reproducibility without rebuilding an approximate index.

A sparse graph would prematurely encode a threshold, neighborhood size,
symmetrization rule, and connectivity policy. Those choices belong to consuming
workflows, not this reusable foundation.

## 2. What “Distance” Means

The artifacts are symmetric dissimilarity matrices, not guaranteed mathematical
metrics. They have zero diagonals and finite values in `[0, 2]`, but triangle
inequality is not claimed.

Three channels are materialized:

### Semantic distance

Derived from the Arabic and English `branch_image` fields. It asks whether two
branch images express nearby meanings.

### Thematic-proxy distance

Derived from the Arabic and English `what_is` scope fields. It asks whether two
branches occupy nearby explanatory or situational domains.

The name includes `proxy` because scope-text embedding does not guarantee
complementary scene roles. It is an explicit hypothesis, not a hidden claim.

### Combined distance

The fixed primary convenience treatment:

```text
D_combined = 0.5 * D_semantic + 0.5 * D_thematic_proxy
```

The separate component matrices remain canonical. Consumers are free to use
either one or define a new combination without rebuilding embeddings.

## 3. Scientific Boundary

### 3.1 What this build can establish

- all intended source rows are represented exactly once;
- every matrix index maps to a stable branch record;
- multilingual views align above a fixed permutation null;
- matrices are finite, symmetric, stable, and non-degenerate;
- the build is reproducible from pinned sources and model artifacts.

### 3.2 What this build cannot establish without a reference

- that a desired secondary resonance is close;
- that thematic complementarity is represented;
- that a downstream traversal will recover a coherent scene;
- that any interpretation is valid.

The build may be labeled `ENGINEERING_VALID` after its internal gates pass. It
must not be labeled `SEMANTICALLY_SUCCESSFUL` or `THEMATICALLY_SUCCESSFUL` until
an independent evaluator tests the frozen matrices.

The first treatment is zero-gold but not pretraining-free. Multilingual E5 is an
external learned prior and may have unknown exposure to Quranic or translated
material. Record this limitation in every evaluation report. A strict
corpus-only representation would be a separate treatment, not a silent claim
about this one.

### 3.3 No target leakage

The builder receives generic matrix objectives only. Motivating examples,
target-aware failure analyses, prior generated readings, and gold/reference
sets are sealed.

Enforcement:

1. Start the builder from a history-free export or restricted worktree that
   denies `.git/` as well as sealed files.
2. Give it only the paths listed in `BUILDER_PROTOCOL.md`.
3. Record every readable input path and SHA-256 hash.
4. Do not use the same target-aware agent to implement or tune the treatment.
5. Freeze code, configuration, source hashes, model revision, embeddings, and
   matrices before an evaluator gains access.

## 4. Authoritative Inputs

The only branch source for treatment `fixed-e5-small-v1` is:

```text
resources/furuq_v4.sqlite
```

Canonical predicate:

```sql
status = 'accepted'
AND contaminated = 'no'
AND origin_corpus = 'quranic'
```

The export must contain:

```text
source branch nodes             10,820
distinct source_root_id values   1,688
distinct surface_root_key values 1,677
surface roots with >1 source ID     11
repeated surface-root/branch labels 47
duplicate canonical node IDs         0
missing required text fields         0
```

`resources/qac.sqlite`, v12, v13, Qnet, and prior output directories are not
inputs to the matrix build.

## 5. Identity Contract

The earlier plan incorrectly treated source root IDs as passage-facing root
identity. This plan separates them:

```text
source_root_id
    source record family, such as root_000090

surface_root_display
    branch_images.root_norm, preserving spaced Arabic form

surface_root_key
    root_norm with ASCII spaces removed, compatible with the QAC join convention

branch_id
    root-local label such as B001

node_id
    "quranic:" + source_root_id + ":" + branch_id

matrix_index
    stable zero-based row and column index
```

The 47 repeated `(surface_root_key, branch_id)` labels remain separate nodes
because they belong to different source root IDs. They must never be merged.
Surface-root grouping is metadata for downstream consumers; it does not change
matrix node count.

The exact record and ordering contract is in `MATRIX_CONTRACT.md`.

## 6. Representation Contract

Treatment `fixed-e5-small-v1` uses:

```text
model: intfloat/multilingual-e5-small
revision: c007d7ef6fd86656326059b28395a7a03a7c5846
mode: evaluation
output dtype: float32
embedding dimension: 384
normalization: L2
prefix for every symmetric-similarity input: "query: "
```

The model card directs symmetric similarity tasks to use the `query:` prefix.
The revision is fixed rather than following a mutable `main`.

Four arrays are produced:

```text
image_ar.npy
image_en.npy
scope_ar.npy
scope_en.npy
```

Input fields:

```text
image_ar = branch_image_ar
image_en = branch_image_en
scope_ar = what_is_ar
scope_en = what_is_en
```

Text preprocessing is intentionally narrow:

1. require a string;
2. normalize to Unicode NFC;
3. collapse Unicode whitespace runs to one ASCII space;
4. trim leading and trailing whitespace;
5. prepend `query: `;
6. do not stem, translate, strip Arabic letters, remove diacritics, or inject
   root labels.

`what_is_not_ar`, `source_phrase_ar`, translations from other resources, ayah
text, and prior outputs are excluded from this treatment.

## 7. Matrix Equations

Let each row of the four embedding arrays be L2-normalized:

```text
E_image_ar
E_image_en
E_scope_ar
E_scope_en
```

For view `v`:

```text
C_v = clip(E_v @ E_v.T, -1, 1)
```

Then:

```text
S_semantic =
    0.5 * C_image_ar
  + 0.5 * C_image_en

S_thematic_proxy =
    0.5 * C_scope_ar
  + 0.5 * C_scope_en

D_semantic       = clip(1 - S_semantic,       0, 2)
D_thematic_proxy = clip(1 - S_thematic_proxy, 0, 2)

D_combined =
    0.5 * D_semantic
  + 0.5 * D_thematic_proxy
```

Set all three diagonals to positive float32 zero after computation.

There is no threshold, top-K operation, rank normalization, local scaling,
hubness correction, CSLS correction, edge direction, symmetrization heuristic,
or learned fusion. The equations above fully determine the matrices.

## 8. Persistence Contract

Canonical matrix format:

```text
NumPy .npy
dtype little-endian float32 (`<f4`)
C-order
shape (10820, 10820)
full square storage
```

Files:

```text
v14/artifacts/fixed-e5-small-v1/
  nodes.jsonl
  nodes.tsv
  views.jsonl
  embeddings/
    image_ar.npy
    image_en.npy
    scope_ar.npy
    scope_en.npy
  matrices/
    semantic_distance.f32.npy
    thematic_proxy_distance.f32.npy
    combined_distance.f32.npy
  diagnostics/
    corpus.json
    embeddings.json
    matrices.json
    cross_language_alignment.json
    null_tests.json
  config.json
  environment.json
  manifest.json
```

`nodes.jsonl` is authoritative. `nodes.tsv` is a convenience export generated
from it and hash-linked in the manifest.

Write each matrix to a `.partial` path with `numpy.lib.format.open_memmap`.
Only rename it to the canonical path after validation. A failed run must not
leave a partial artifact under a canonical filename.

## 9. Exact Computation

At this scale, exact blocked multiplication is sufficient.

Default block size:

```text
B = 512
```

For every block pair `(I, J)` where `J >= I`:

1. compute the four float32 cosine blocks;
2. apply the equations in Section 7;
3. write `(I, J)` to each output memmap;
4. write its exact transpose to `(J, I)`;
5. flush at declared checkpoints;
6. record completed blocks in a resumable journal tied to input hashes.

Tie-breaking is irrelevant because no ranking enters construction.

The builder may change `B` only after a canary proves that `512` cannot run on
the target machine. Freeze the chosen value before the full run. Block size does
not change the scientific treatment, but it may change low-order floating-point
bits through BLAS kernel selection; therefore it creates a new `build_id`, must
not reuse an old journal, and must pass the same tolerance checks. Byte-identical
reconstruction is required only for the same environment and build configuration.

## 10. Storage and Compute

For `n = 10,820`:

```text
entries per full matrix            117,072,400
float32 payload per matrix         468,289,600 bytes
float32 payload per matrix         about 446.6 MiB
three float32 matrix payloads      about 1.31 GiB
four 384-d float32 embedding sets  about 63.4 MiB
one 512 x 512 float32 block        exactly 1.0 MiB
four cosine plus three result blocks about 7.0 MiB
```

Allow additional space for:

- model and tokenizer cache;
- locked Python environment;
- node exports and diagnostics;
- partial files during atomic completion;
- temporary package downloads;
- one failed or comparison treatment.

Execution gate:

```text
minimum free after checkout: 5 GiB
recommended free:            8 GiB
training/adaptation work:   15 GiB or more
```

The current filesystem had about 4.1 GiB free at the latest audit and is below
the minimum.

CPU construction is feasible. A GPU may shorten embedding time but is not
required. Full matrix multiplication at this size does not justify FAISS,
approximate nearest-neighbor infrastructure, or a vector database.

## 11. Environment and Reproducibility

Use Python 3.10 on the inspected Intel macOS host. The implementation must add:

```text
v14/requirements.in
v14/requirements.lock
v14/pyproject.toml
```

The lock file must:

- pin every transitive dependency;
- include hashes;
- install successfully into a fresh Python 3.10 environment;
- include a tested Intel-macOS resolution or document that the canonical run
  moved to a different platform.

Before a full run, record:

```text
OS and architecture
Python version
package lock SHA-256
NumPy, BLAS, PyTorch, and transformers versions
thread environment variables
model repository and revision
hashes of downloaded model/tokenizer files
source database SHA-256
git commit and dirty-state patch hash
random seeds
```

Set model evaluation mode and disable dropout. Run the canonical build with one
declared thread configuration. Cross-platform reproduction may use tolerance;
same-environment reconstruction from frozen embeddings must produce
byte-identical matrix hashes.

## 12. Gold-Free Validation

These checks validate the artifact without target examples.

### Corpus gates

Require every count in Section 4. Reject:

- duplicate `node_id`;
- unstable order;
- missing fields;
- any non-quranic row;
- any contaminated or non-accepted row;
- any merged source row.

### Embedding gates

For all four arrays:

```text
shape = (10820, 384)
dtype = float32
finite values = 100%
L2 norm absolute error <= 1e-5
```

Record token-length and truncation distributions. Any empty post-normalization
view stops the run.

### Cross-language alignment

Compute, without persisting as a canonical artifact:

```text
A_image = E_image_ar @ E_image_en.T
A_scope = E_scope_ar @ E_scope_en.T
```

For each array, the correct match is the same `matrix_index` on the diagonal.
Rank by descending cosine, then ascending `node_id` for exact ties. Report MRR
and Recall@1/10/50.

Use exactly 1,000 deterministic permutations of the English row identities.
Generate them with NumPy `PCG64(1729)` and apply the same tie rule.
The observed MRR for both image and scope must exceed every permutation-null
MRR (`empirical p <= 0.001`). This tests alignment, not interpretive quality.

### Matrix gates

For all three matrices:

```text
shape = (10820, 10820)
dtype = float32
finite values = 100%
minimum >= 0
maximum <= 2
diagonal exactly +0.0
symmetry byte-exact
```

Recompute 10,000 seeded random entries directly from embeddings and require
absolute error `<= 1e-6`.

Require:

```text
max_abs(
  D_combined
  - 0.5 * D_semantic
  - 0.5 * D_thematic_proxy
) <= 1e-6
```

The semantic and thematic-proxy matrices must not be byte-identical. Report
their Spearman correlation on one million unique unordered off-diagonal pairs
sampled without replacement by `PCG64(1729)`; do not tune a weight based on that
result.

### Reconstruction gate

Delete only a disposable canary copy, rebuild it from the frozen embeddings,
and require identical SHA-256 matrix hashes on the canonical environment.

## 13. External Blind Utility Evaluation

External evaluation is not part of matrix construction, but it is required
before claiming that the representation is useful for the motivating problem.

Protocol:

1. A curator who has not seen matrix neighborhoods freezes reference branch
   pairs or groups.
2. Record provenance and separate human-adjudicated gold from model-derived
   pseudo-reference.
3. Hash the references and the complete metric specification.
4. Freeze the builder treatment.
5. A fresh evaluator reads matrices plus the sealed reference.
6. The evaluator computes ranks and distances only. It does not reinterpret
   ayat or modify references.
7. No result-dependent change may retain the same treatment ID.

For the primary cross-root utility metric, rank candidates by ascending distance,
then ascending `node_id` for exact ties. Exclude the query node and every
candidate with the same `surface_root_key`. A reference member is eligible only
if its group contains at least one member from another surface root. Report any
same-root reference structure separately as a secondary diagnostic.

Primary statistical check:

- use `combined_distance.f32.npy` as the preregistered primary matrix;
- compare within-reference nearest-member reciprocal rank against 10,000
  size- and surface-root-matched random reference sets under the same cross-root
  eligibility rule;
- require permutation `p <= 0.01`.

Primary practical pilot check:

- at least 50% of eligible reference members have another member within their
  cross-root top 100 entries in the combined matrix;
- semantic and thematic-proxy results are secondary diagnostics and cannot
  rescue a failed primary result.

These are pilot success thresholds, not theological or interpretive validation.
If the project proceeds to a formal study, the evaluator must preregister a
larger passage count, uncertainty intervals, multiplicity handling, and any
stronger domain threshold.

## 14. Execution Phases

### Phase 0: move, isolate, and preflight

Actions:

1. Move or clone to a filesystem with at least 5 GiB free after checkout.
2. Record `git status --short`; preserve unrelated changes.
3. Create a history-free builder bundle or enforce a sandbox that denies
   `.git/`, sealed documents, and prior versions.
4. Verify Python 3.10.
5. Hash the source database.
6. Freeze model ID and revision.
7. Create a small environment canary.

Gate:

- storage passes;
- builder cannot read sealed paths;
- no model or full artifact download has started;
- source and model identifiers are frozen.

### Phase 1: package and lock

Actions:

1. Create `v14/` layout.
2. Add package metadata and locked dependencies.
3. Add schemas, config validation, hashing, atomic writers, and tests.
4. Add a treatment manifest format.

Gate:

- fresh environment installs from lock;
- unit tests pass without gold or prior outputs;
- generated artifacts are Git-ignored.

### Phase 2: canonical node export

Actions:

1. Execute the exact SQL in `MATRIX_CONTRACT.md`.
2. construct identities without merging;
3. assign stable matrix indices;
4. write node exports and corpus diagnostics;
5. hash the result.

Gate: every corpus and identity count in Section 4 passes exactly.

### Phase 3: embedding canary

Actions:

1. Encode 64 deterministically selected records;
2. validate all four text views;
3. measure tokens, truncation, RSS, time, and disk;
4. project the full run;
5. run the canary twice.

Gate:

- shapes, dtypes, norms, and finite checks pass;
- same-environment outputs match;
- projected peak disk remains below available space with 1 GiB reserve.

### Phase 4: full embeddings

Actions:

1. Encode all records in stable index order;
2. persist float32 arrays atomically;
3. run embedding and cross-language alignment gates;
4. hash every array.

Gate: all Section 12 embedding and alignment checks pass.

### Phase 5: full matrices

Actions:

1. allocate the three partial memmaps;
2. execute exact block pairs;
3. write symmetric transposes;
4. resume safely if interrupted;
5. set diagonals;
6. validate and atomically rename.

Gate: all Section 12 matrix checks pass.

### Phase 6: freeze and handoff

Actions:

1. create diagnostics and environment reports;
2. hash all source, code, config, model, embedding, and matrix artifacts;
3. record git commit and dirty patch;
4. mark treatment `ENGINEERING_VALID`;
5. expose a read-only loader and index lookup example.

Gate:

- manifest verifies from a fresh process;
- a consumer can retrieve a full row and arbitrary submatrix by `node_id`;
- no sealed reference was exposed to the builder.

### Phase 7: optional external blind evaluation

This phase is run by a different role and repository access profile. It does not
change the frozen matrices. Its output decides whether this treatment is useful
enough for downstream workflows.

## 15. Orchestration Responsibilities

### Coordinator

- establish access separation;
- create and hash the history-free builder bundle;
- prepare storage and environment approval;
- freeze treatment configuration;
- assign builder work without target examples;
- audit manifests and gates;
- start external evaluation only after freeze;
- reject result-dependent changes under an existing treatment ID.

### Builder

- read only builder-safe inputs;
- implement export, embedding, matrices, tests, and manifests;
- never read prior analyses or references;
- never add graph, activation, or interpretation features;
- stop on a failed hard gate.

### Evaluator

- begin after the treatment is frozen;
- verify reference hashes predate prediction access;
- report matrix-level metrics without changing references;
- keep semantic and thematic-proxy results separate;
- never request a same-treatment patch after seeing outcomes.

The same agent may coordinate and build only if it has never received the sealed
context or readable Git history containing it. A target-aware coordinator must
delegate the builder to a genuinely fresh context.

## 16. Failure Diagnosis

| Observation | Classification | Next action |
| --- | --- | --- |
| Export count mismatch | data contract failure | stop; inspect predicate and identity |
| 10,773 nodes after export | accidental surface-label merge | stop; preserve all source IDs |
| Cross-language alignment fails null | representation failure | reject treatment before matrices |
| Matrix is asymmetric or non-finite | implementation failure | fix without changing treatment semantics |
| Semantic and thematic matrices identical | view construction failure | inspect fields/config |
| Blind ranks equal null | representation not useful | freeze negative result; define new treatment |
| Semantic passes, thematic fails | scope proxy inadequate | new thematic representation treatment |
| Downstream workflow needs top-K | consumer requirement | derive from matrix outside canonical build |
| Disk falls below reserve | operational failure | stop and move artifacts |

## 17. Stop Conditions

Stop immediately if:

- free disk is below 5 GiB after checkout;
- builder access includes sealed material;
- source hash changes after export;
- canonical count is not 10,820;
- source-root or surface-root counts differ from the frozen audit;
- any source row is merged;
- model revision is mutable or unrecorded;
- a full run begins before canary projection;
- alignment fails the fixed null gate;
- a partial output appears under a canonical filename;
- an evaluator asks for treatment changes after unsealing.

A failed representation is a valid research result. Do not rescue it by changing
weights, fields, thresholds, or encoders under the same treatment ID.

## 18. Acceptance Criteria

The matrix build is complete only when:

- `nodes.jsonl` has 10,820 stable unique nodes;
- all identity collision fixtures pass;
- four embedding arrays satisfy their contract;
- three complete float32 matrices satisfy their contract;
- cross-language alignment beats the fixed permutation null;
- reconstruction produces byte-identical matrix hashes;
- all artifacts and environment inputs are hashed;
- the consumer loader retrieves rows and submatrices correctly;
- no prohibited input was exposed;
- no graph, activation, coalition, or ayah-analysis code was added.

At this point the result is `ENGINEERING_VALID`.

Only an independent external result may add:

```text
UTILITY_PASS
UTILITY_PARTIAL
UTILITY_FAIL
```

## 19. Cold-Start Runbook

1. Read this plan as coordinator.
2. Read `REPOSITORY_AUDIT.md`.
3. Confirm current storage with `df -h .`.
4. Move the checkout if free space is below 5 GiB.
5. Create a fresh builder context.
6. Restrict it to the allowlist in `BUILDER_PROTOCOL.md`.
7. Freeze model revision and source hash.
8. Create `v14/` package and dependency lock.
9. Run tests without model download.
10. Export nodes with the exact SQL.
11. Require all identity counts.
12. Run the 64-node embedding canary twice.
13. Review projected disk, RSS, and time.
14. Build four full embedding arrays.
15. Run cross-language null checks.
16. Allocate and build three complete matrices.
17. Validate exact symmetry, formulas, samples, and hashes.
18. Freeze the manifest and mark `ENGINEERING_VALID`.
19. Hand matrices to consumers or a fresh blind evaluator.
20. Never retrofit a sparse graph into the canonical artifact.

## 20. Feasibility

Engineering feasibility is high. The matrix payload is modest for a workstation,
the node count is small enough for exact blocked multiplication, and no custom
model training is required.

Scientific utility is uncertain. The full matrix is still the correct first
artifact because it cleanly separates representation quality from downstream
search policy. If a blind consumer cannot recover useful proximity, the next
experiment changes the representation while keeping the node and matrix
contracts stable.

Expected implementation size:

```text
production package and CLI code: about 1,200-2,000 lines
tests, fixtures, and schemas:     about   800-1,500 lines
total expected codebase:          about 2,000-3,500 lines
```

After the code exists, the source export and matrix multiplication should take
minutes to a small number of hours. Encoding 43,280 text views is likely the
longest automated stage on the inspected CPU. The Phase 3 canary, not this
estimate, is authoritative. Environment setup, artifact review, and optional
blind evaluation add human elapsed time but no matrix-construction complexity.

## 21. Primary References

- Multilingual E5 technical report:
  <https://arxiv.org/abs/2402.05672>
- Pinned multilingual-E5-small model repository:
  <https://huggingface.co/intfloat/multilingual-e5-small/tree/c007d7ef6fd86656326059b28395a7a03a7c5846>
- Current model card, including the symmetric-task prefix instruction:
  <https://huggingface.co/intfloat/multilingual-e5-small>
- NumPy `.npy` format and memory mapping:
  <https://numpy.org/doc/stable/reference/generated/numpy.lib.format.open_memmap.html>

## 22. Final Instruction

Build the complete matrices and stop. Preserve every pairwise value, every node
identity, every input hash, and every failed validation. Do not solve a
downstream analysis problem inside the representation artifact.
