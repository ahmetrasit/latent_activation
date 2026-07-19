# Canonical Node and Matrix Contract

Version: `latent-matrix-contract-v1`

This document is normative. If another document conflicts with it, stop and
resolve the conflict before implementation.

## 1. Source Query

Run against `resources/furuq_v4.sqlite` in read-only mode:

```sql
SELECT
  id AS source_row_id,
  root_id AS source_root_id,
  root_norm AS surface_root_display,
  branch_id,
  branch_image_ar,
  branch_image_en,
  image_en_fit,
  image_en_gap_note,
  what_is_ar,
  what_is_en,
  what_is_not_ar,
  source_refs,
  source_phrase_ar,
  source_path,
  status,
  origin_corpus,
  contaminated
FROM branch_images
WHERE status = 'accepted'
  AND contaminated = 'no'
  AND origin_corpus = 'quranic'
ORDER BY
  root_norm COLLATE BINARY,
  root_id COLLATE BINARY,
  branch_id COLLATE BINARY,
  id;
```

Do not use the compressed database through a temporary loader. Do not omit the
origin predicate. Do not group rows.

## 2. Derived Identity

For each ordered source row:

```text
matrix_index
    zero-based position in the SQL result

surface_root_key
    remove ASCII U+0020 spaces from surface_root_display

node_id
    "quranic:" + source_root_id + ":" + branch_id
```

Reject a row if:

- `source_root_id`, `surface_root_display`, or `branch_id` is empty;
- `node_id` is duplicated;
- `surface_root_key` is empty;
- `origin_corpus`, `status`, or `contaminated` differs from the predicate.

Do not use `(surface_root_key, branch_id)` as identity. It is non-unique.

## 3. Node Record

`nodes.jsonl` contains one object per line in matrix order:

```json
{
  "contract": "latent-matrix-node-v1",
  "matrix_index": 0,
  "node_id": "quranic:root_000003:B001",
  "source_row_id": 3439,
  "source_root_id": "root_000003",
  "surface_root_display": "ء ب ب",
  "surface_root_key": "ءبب",
  "branch_id": "B001",
  "origin_corpus": "quranic",
  "branch_image_ar": "...",
  "branch_image_en": "...",
  "image_en_fit": "close",
  "image_en_gap_note": "...",
  "what_is_ar": "...",
  "what_is_en": "...",
  "what_is_not_ar": "...",
  "source_refs": "...",
  "source_phrase_ar": "...",
  "source_path": "..."
}
```

JSON serialization:

- UTF-8 without BOM;
- one compact JSON object per line;
- `ensure_ascii=false`;
- keys emitted in the schema order above;
- LF line endings;
- final newline required;
- no NaN or Infinity;
- no dynamically generated timestamp in this file.

`nodes.tsv` uses the same row order and fields. Newlines and tabs inside text
must be quoted using a standards-compliant TSV/CSV writer.

## 4. View Record

`views.jsonl` contains:

```json
{
  "contract": "latent-matrix-views-v1",
  "matrix_index": 0,
  "node_id": "quranic:root_000003:B001",
  "image_ar": "query: ...",
  "image_en": "query: ...",
  "scope_ar": "query: ...",
  "scope_en": "query: ..."
}
```

Text preparation:

```text
prepared(x) =
    "query: "
  + collapse_unicode_whitespace_to_ascii_space(NFC(x)).strip()
```

Reject empty prepared bodies. Preserve original fields only in `nodes.jsonl`;
never overwrite them with prepared strings.

## 5. Embedding Arrays

Each `.npy` array:

```text
shape: (10820, 384)
dtype: little-endian float32 (`<f4`)
row order: matrix_index
finite: required
L2 normalized: required
```

Names:

```text
embeddings/image_ar.npy
embeddings/image_en.npy
embeddings/scope_ar.npy
embeddings/scope_en.npy
```

No quantized embedding is canonical. A consumer may create a derived copy under
a different manifest.

## 6. Canonical Matrix Arrays

Names and definitions:

```text
matrices/semantic_distance.f32.npy
    1 - mean(cosine(image_ar), cosine(image_en))

matrices/thematic_proxy_distance.f32.npy
    1 - mean(cosine(scope_ar), cosine(scope_en))

matrices/combined_distance.f32.npy
    mean(semantic_distance, thematic_proxy_distance)
```

Every matrix:

```text
shape: (10820, 10820)
dtype: little-endian float32 (`<f4`)
layout: full square, C-order
index meaning: nodes.jsonl matrix_index
diagonal: exact positive 0.0
symmetry: exact
range: [0.0, 2.0]
missing values: forbidden
```

The matrix payload has 117,072,400 entries and 468,289,600 float32 data bytes.
The `.npy` header adds a small fixed-format overhead.

Distance is lower-is-nearer. Consumers must not assume triangle inequality.

## 7. Block Journal

Journal protocol: `latent-matrix-block-journal-v1`.

Required fields:

```json
{
  "contract": "latent-matrix-block-journal-v1",
  "treatment_id": "fixed-e5-small-v1",
  "config_sha256": "...",
  "nodes_sha256": "...",
  "embedding_sha256": {
    "image_ar": "...",
    "image_en": "...",
    "scope_ar": "...",
    "scope_en": "..."
  },
  "shape": [10820, 10820],
  "dtype": "float32",
  "block_size": 512,
  "completed_upper_blocks": [[0, 0], [0, 1]]
}
```

Block coordinates refer to block ordinals, not row indices. Sort coordinates
lexicographically before writing. A mismatched field invalidates resume.

## 8. Manifest

Manifest protocol: `latent-matrix-manifest-v1`.

It records:

- treatment configuration and hash;
- source path, bytes, and SHA-256;
- canonical SQL text and hash;
- node/view file bytes, row counts, and hashes;
- model ID, revision, file inventory, bytes, and hashes;
- environment lock and runtime metadata;
- embedding shape, dtype, bytes, and hash;
- matrix shape, dtype, bytes, formula, and hash;
- validation report paths and hashes;
- coordinator-recorded base/reintegration commits and dirty patch hash;
- build start/end timestamps;
- final status.

Allowed final statuses:

```text
ENGINEERING_VALID
ENGINEERING_FAILED
```

Scientific utility status belongs to a separate evaluator manifest and must not
be written into the builder manifest.

## 9. Read-Only Consumer Interface

The implementation must expose:

```python
artifact = MatrixArtifact.open(path, verify_manifest=True)
node = artifact.node("quranic:root_000003:B001")
row = artifact.row("combined", node.node_id)
submatrix = artifact.submatrix("semantic", node_ids)
distance = artifact.distance("thematic_proxy", left_id, right_id)
```

Requirements:

- matrices are opened with read-only memory mapping;
- node ID lookup is deterministic;
- returned row index matches `matrix_index`;
- unknown node IDs raise an explicit error;
- matrix names are an enum, not arbitrary paths;
- manifest verification may be skipped only through an explicit unsafe flag;
- the API does not perform thresholding, ranking, graph construction, or
  passage lookup.

## 10. Hard Count Fixtures

The build tests must freeze:

```text
rows                                      10,820
distinct source_root_id                    1,688
distinct surface_root_key                  1,677
surface_root_key with multiple source IDs     11
duplicate node_id                              0
repeated (surface_root_key, branch_id) groups 47
extra rows in those repeated groups            47
```

The 11 collision fixtures are:

```text
ب د ء
ب ر ء
ب ك ي
ب و ء
ج ي ء
د ر ء
ش ي ء
ض و ء
ط ف ء
ق ر ء
م ر ء
```

Tests must obtain expected source IDs for these roots from a checked-in fixture
generated during Phase 2 and reviewed before embedding.

## 11. Versioning

Any change to the following creates a new treatment ID:

- source predicate or source hash;
- node identity or ordering;
- source text field selection;
- text preprocessing;
- encoder or model revision;
- view weights;
- matrix formulas;
- output precision.

Changing only operational batch size or matrix block size does not create a new
scientific treatment. A changed matrix block size creates a new `build_id`,
invalidates existing block journals, and must pass the same numerical tolerance
checks. Byte-identical reconstruction is required only for the same environment,
block size, and build configuration.
