# Builder-Safe Repository Audit

Audit date: 2026-07-19

This document contains repository facts needed to build the matrices. It
contains no motivating target examples or reference answers.

## 1. Repository State

At the last synchronized baseline:

```text
branch: main
upstream baseline: 5a0df8d Add S48 v12 v13 comparison runs
repository size: about 2.0 GiB
.git: about 409 MiB
resources: about 387 MiB
v11: about 403 MiB
v12: about 11 MiB
v13: about 2.6 MiB
```

The matrix-plan correction is replayed after that upstream baseline. Every
actual build must record its own base and reintegration commits rather than
treating this audit snapshot as current.

## 2. Relevant Resources

```text
resources/furuq_v4.sqlite       about 164 MiB
resources/furuq_v4.sqlite.gz    about 26 MiB
resources/qac.sqlite            about 113 MiB
resources/qac.sqlite.gz         about 26 MiB
resources/v4_branches.tsv       about 9.3 MiB
resources/qac_root_ayah.tsv     about 29 MiB
resources/quran/                114 surah JSON files plus 4 corpus/source files
resources/attachments.tsv       about 17 MiB
```

Only `resources/furuq_v4.sqlite` is an input to treatment
`fixed-e5-small-v1`.

## 3. Branch Table

Relevant `branch_images` fields:

```text
id
root_id
root_norm
branch_id
branch_image_ar
branch_image_en
image_en_fit
image_en_gap_note
what_is_ar
what_is_en
what_is_not_ar
source_refs
source_phrase_ar
source_path
status
origin_corpus
contaminated
```

For `status='accepted' AND contaminated='no'`:

| Origin | Branch rows | Source root IDs |
| --- | ---: | ---: |
| `quranic` | 10,820 | 1,688 |
| `furuq` | 7,961 | 1,652 |
| Total | 18,781 | 3,340 |

The first treatment uses only the 10,820 quranic rows.

All 18,781 clean accepted rows have nonempty Arabic/English image and
Arabic/English scope fields.

For the quranic subset:

```text
distinct root_id                               1,688
distinct root_norm                             1,677
root_norm values with two root_id values          11
repeated (root_norm, branch_id) groups             47
extra rows across repeated groups                  47
duplicate (origin_corpus, root_id, branch_id)       0
```

English image-fit labels:

| Label | Rows |
| --- | ---: |
| `close` | 9,113 |
| `partial` | 1,035 |
| `exact` | 644 |
| `lossy` | 25 |
| `unsafe` | 3 |

Field lengths for the quranic subset:

| Field | Minimum | Mean | Maximum |
| --- | ---: | ---: | ---: |
| `branch_image_ar` | 4 | 19.2 | 49 |
| `branch_image_en` | 3 | 27.9 | 76 |
| `what_is_ar` | 6 | 79.4 | 238 |
| `what_is_en` | 4 | 97.1 | 293 |

These lengths are well below the selected encoder's 512-token maximum in
ordinary cases, but token-level truncation must still be measured rather than
assumed.

## 4. Surface Identity and QAC

Removing ASCII spaces from `root_norm` produces the QAC-style compact join key.
Of 1,677 quranic surface roots:

```text
present in qac_morphemes root_join_key  1,612
absent from qac_morphemes                  65
```

QAC is not needed to construct the global branch matrix. These counts matter
only to future passage consumers and must not reduce the matrix node inventory.

## 5. Existing v13

`v13/` already exists and implements deterministic dynamic retrieval using v12
loaders. Its branch provenance includes both quranic and furuq origins, and its
loader merges repeated reader-facing `(root_norm, branch_id)` labels into
variants.

That behavior is useful for its own reader workflow but violates this matrix
treatment's quranic-only, source-row-preserving identity contract. Do not import
the v12/v13 branch loader. `v14/` is reserved for the matrix build.

## 6. Qnet

The previously configured sibling path:

```text
../quran-roots/_corpus/activation
```

was absent at inspection. Qnet is not a required input and has no role in this
matrix treatment. New v11 Qnet audit/repair artifacts are present in the
repository after the latest upstream sync, but the live sibling activation path
remains absent and all such artifacts remain outside the builder allowlist.

## 7. Host and Runtime

Inspected host:

```text
macOS 15.7.7
x86_64 Intel
16 GiB RAM
4 physical / 8 logical CPUs
Python 3.14.5 available
Python 3.10.19 available at /usr/local/bin/python3.10
```

The inspected Python 3.10 environment had none of these packages installed:

```text
numpy
scipy
scikit-learn
torch
transformers
sentence-transformers
zarr
h5py
```

No project `pyproject.toml`, requirements file, or model cache was available at
the initial audit. The v14 build must create and test its own locked environment.

## 8. Disk

At the latest check:

```text
filesystem size: 113 GiB
available: about 4.1 GiB
capacity used: 96%
```

Disk is volatile. `df -h .` at Phase 0 is authoritative. Do not begin the full
run below 5 GiB free after checkout.

## 9. Matrix Arithmetic

For 10,820 nodes:

```text
n^2 float entries               117,072,400
one float32 matrix              468,289,600 bytes
one float32 matrix              about 446.6 MiB
three float32 matrices          about 1.31 GiB
one 384-d float32 embedding set about 15.8 MiB
four embedding sets            about 63.4 MiB
```

The full square matrices are feasible. Their storage becomes problematic only
when mixed with model caches, environments, partial outputs, and multiple
treatments on the nearly full current volume.

## 10. Expected Implementation Scale

The corrected matrix-only scope is expected to require approximately:

```text
production package and CLI code: 1,200-2,000 lines
tests, fixtures, and schemas:       800-1,500 lines
total:                            2,000-3,500 lines
```

The main automated runtime is four-view encoding. Exact blocked all-pairs
matrix construction at 10,820 nodes is workstation-scale. The required canary
must replace these estimates with measured projections before a full run.

## 11. Audit Reproduction Queries

All hard counts must be recomputed from the source database during Phase 2.
The normative query and identities are in `MATRIX_CONTRACT.md`; this audit is
not a substitute for runtime validation.
