# Builder Protocol: Fixed Full-Matrix Treatment

Role: builder

Treatment ID: `fixed-e5-small-v1`

This is a builder-safe document. Implement the complete branch distance
matrices and nothing downstream of them.

## 1. Access Boundary

Readable repository paths:

```text
docs/latent_activation_orchestration/BUILDER_PROTOCOL.md
docs/latent_activation_orchestration/MATRIX_CONTRACT.md
docs/latent_activation_orchestration/REPOSITORY_AUDIT.md
resources/furuq_v4.sqlite
v14/
```

Additional readable inputs:

- the pinned model/tokenizer files for
  `intfloat/multilingual-e5-small` at revision
  `c007d7ef6fd86656326059b28395a7a03a7c5846`;
- the Python standard library and packages installed from the frozen v14 lock;
- operating-system metadata needed for the environment manifest.

The coordinator should provide these as a history-free export. `.git/` is not a
builder input.

Do not read:

```text
docs/latent_activation_orchestration/SEALED_EVALUATION_CONTEXT.md
v1/ through v13/ except for the empty name check performed by the coordinator
scratch/
test/ when it contains prior experiment material
root-level synthesis or findings documents
prior run outputs
gold, evaluation, adjudication, or reader artifacts
../quran-roots/
.git/
```

Do not browse the web for Quranic content, tafsir, interpretations, motifs, or
candidate answers. The only allowed network use is dependency and pinned-model
retrieval approved by the coordinator.

If any prohibited content is exposed, stop and report the exact exposure. The
treatment must restart with a fresh builder context.

The builder returns a patch or completed `v14/` tree to the coordinator. The
coordinator, not the builder, reintegrates it into the full repository and
records the Git commit and dirty-state hash.

## 2. Deliverable

Create:

```text
v14/
  README.md
  pyproject.toml
  requirements.in
  requirements.lock
  config/
  src/latent_matrix/
  schemas/
  scripts/
  tests/
  artifacts/                 # ignored by Git
```

The frozen treatment artifact contains:

```text
10,820 nodes
4 x (10,820, 384) float32 normalized embeddings
3 x (10,820, 10,820) float32 complete distance matrices
diagnostics
environment record
SHA-256 manifest
```

No sparse graph, top-K table, activation result, passage package, coalition, or
interpretive output is a deliverable.

## 3. Primary Configuration

Create a validated `config.json` with these immutable scientific fields:

```json
{
  "treatment_id": "fixed-e5-small-v1",
  "source": {
    "path": "resources/furuq_v4.sqlite",
    "status": "accepted",
    "contaminated": "no",
    "origin_corpus": "quranic"
  },
  "model": {
    "id": "intfloat/multilingual-e5-small",
    "revision": "c007d7ef6fd86656326059b28395a7a03a7c5846",
    "dimension": 384,
    "prefix": "query: ",
    "max_length": 512,
    "output_dtype": "float32",
    "l2_normalize": true
  },
  "views": {
    "image_ar": "branch_image_ar",
    "image_en": "branch_image_en",
    "scope_ar": "what_is_ar",
    "scope_en": "what_is_en"
  },
  "matrices": {
    "semantic": {
      "image_ar": 0.5,
      "image_en": 0.5
    },
    "thematic_proxy": {
      "scope_ar": 0.5,
      "scope_en": 0.5
    },
    "combined": {
      "semantic": 0.5,
      "thematic_proxy": 0.5
    }
  },
  "matrix_dtype": "<f4",
  "block_size": 512,
  "permutation_seed": 1729,
  "permutation_replicates": 1000
}
```

Do not add or tune weights after seeing neighborhoods or evaluation results.
Operational batch size may differ from matrix block size and is recorded
separately. Freeze block size before the full matrix run.

## 4. Required Components

Implement modules with narrow responsibilities:

```text
config.py
    parse and validate immutable treatment configuration

identity.py
    construct node_id and surface_root_key

export.py
    execute canonical SQL and produce stable nodes/views

embed.py
    normalize text, encode four views, validate embeddings

matrix.py
    compute exact complete matrices blockwise and resume safely

validate.py
    corpus, embedding, alignment, matrix, and reconstruction gates

manifest.py
    environment capture, file hashing, and treatment freeze

reader.py
    read-only node lookup, row access, and submatrix access
```

Do not import branch-loading code from v12 or v13.

## 5. Canonical Command Surface

Phase 1 may resolve dependencies in a disposable environment. Record and pin
the resolver version, review the resulting transitive hashes, then discard that
environment. The canonical environment installs only from the reviewed lock:

```bash
python3.10 -m venv v14/.venv
v14/.venv/bin/python -m pip install \
  --require-hashes \
  -r v14/requirements.lock
v14/.venv/bin/python -m pytest -q v14/tests
```

The package must provide this command surface:

```bash
v14/.venv/bin/python -m latent_matrix export \
  --config v14/config/fixed-e5-small-v1.json

v14/.venv/bin/python -m latent_matrix canary \
  --config v14/config/fixed-e5-small-v1.json

v14/.venv/bin/python -m latent_matrix embed \
  --config v14/config/fixed-e5-small-v1.json

v14/.venv/bin/python -m latent_matrix build \
  --config v14/config/fixed-e5-small-v1.json

v14/.venv/bin/python -m latent_matrix validate \
  --config v14/config/fixed-e5-small-v1.json

v14/.venv/bin/python -m latent_matrix freeze \
  --config v14/config/fixed-e5-small-v1.json
```

Commands must fail closed: a failed prerequisite gate prevents later commands
from running against a canonical artifact path.

## 6. Implementation Order

1. Add schemas and config validation.
2. Add identity tests, including all 11 surface-root collisions.
3. Export nodes from the uncompressed SQLite database.
4. Assert all exact corpus counts.
5. Freeze and hash `nodes.jsonl`.
6. Build a deterministic 64-node canary spanning the ordered inventory.
7. Download/load only the pinned model revision.
8. Encode the canary twice.
9. Project full runtime, memory, and disk.
10. Encode all four views.
11. Run cross-language alignment and null checks.
12. Stop if either alignment check fails.
13. Build all three complete matrices.
14. Validate matrix formulas and storage invariants.
15. Reconstruct a disposable canary matrix and compare hashes.
16. Write the final manifest.
17. Test the read-only consumer API from a fresh process.
18. Stop.

## 7. Testing Requirements

### Identity tests

- canonical `node_id` is unique;
- source rows with repeated `(surface_root_key, branch_id)` remain distinct;
- exactly 11 surface roots map to more than one source root ID;
- exactly 47 repeated surface-root/branch groups exist;
- no ordering depends on Python hash iteration or locale.

### Export tests

- source predicate is exact;
- all required fields are nonempty;
- order is byte-stable;
- JSONL to TSV round-trip preserves identity and index;
- a second export has the same SHA-256.

### Text tests

- NFC is applied;
- whitespace collapse is deterministic;
- Arabic characters are not transliterated or stripped;
- the literal `query: ` prefix appears exactly once;
- empty normalized text is rejected;
- source fields remain unchanged in `nodes.jsonl`.

### Embedding tests

- model revision is not `main`;
- model is in evaluation mode;
- output is float32;
- shape and norm gates pass;
- record order matches matrix index;
- canary outputs reproduce in the locked environment.

### Matrix tests

Use hand-constructed normalized arrays with known dot products. Require:

- exact expected semantic and thematic blocks;
- exact 50/50 combined formula;
- exact transpose writes;
- exact positive-zero diagonal;
- range clipping;
- interrupted block journal resumes without rewriting completed blocks;
- mismatched embedding hashes invalidate a journal;
- canonical rename occurs only after validation;
- loader returns correct rows and submatrices.

### Prohibited-feature test

The v14 package must not depend on QAC, Qnet, v12, v13, ayah references,
passage windows, graph libraries, activation schemas, or prior outputs.

## 8. Atomicity and Resume Rules

Every partial matrix is tied to:

```text
treatment config SHA-256
nodes SHA-256
four embedding SHA-256 values
shape
dtype
block size
completed block coordinates
```

On resume, reject any mismatch. Write the journal atomically after matrix data
is flushed. A block is complete only after both upper and lower symmetric
positions are written.

Do not hash a multi-gigabyte matrix after every block. Hash it once after final
validation and canonical rename.

## 9. Builder Completion Report

Return:

```text
treatment ID
history-free builder-bundle hash
coordinator-recorded base commit and reintegration commit
source hash
model revision and model-file hashes
node counts and identity collision counts
environment lock hash
canary projections
embedding shapes and hashes
cross-language metrics and null p-values
matrix shapes, ranges, symmetry, formula checks, and hashes
artifact byte totals
manifest path and hash
prohibited-input exposure declaration
```

Do not include nearest-neighbor examples from the motivating domain. The
builder's work ends when the frozen artifact is `ENGINEERING_VALID`.
