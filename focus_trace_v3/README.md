Hermetic Focus Trace v3

V3 starts from v1 (`focus_trace/`), with the accepted-alignment 83:1 input repair.
The copied files and their hashes are recorded in [V1_BASE.json](V1_BASE.json).
There are no imports, copied implementations, or runtime inputs from HFT v2.
V1's existing shared `v12/scripts/build_packets.py` utility and canonical resources
remain dependencies; v3 does not import the live `focus_trace/` implementation.

The default remains one sealed packet, one fresh reader, one response. Preparation,
rendering, compilation, validation, and export are offline. They launch no models.
No fallback, automatic retry, semantic repair, or production promotion is built in.

**What changed from the v1 base**

- V1's Reader Posture and Core Task are preserved verbatim: discovery first,
  focus-only baseline, competing mechanisms, unusual grounded readings, and
  reconstructed focus traces.
- V1's explicit instruction not to collapse split roots to the dominant target
  is restored. The extra [integration instruction](prompts/integration.md) is now
  opt-in with `--integration`; the default follows v1's discovery task more closely.
  This is a candidate improvement under evaluation, not established quality parity.
  `--prompt-revision initial --integration` reproduces the prior v3 prompt.
  Existing jobs without a prompt revision still validate against archived initial
  templates; their frozen inputs and outputs are unchanged.
- The reader selects `occurrence_id`, `branch_key`, and `role`. The compiler
  expands exact v1 citations and derives `trigger_roots`. It never chooses another
  source, adds a citation, changes a reading, or corrects a semantic error.
- The focus-first grouped input layout remains. Focus branches retain their full
  Arabic scopes and distinct paired variants. Context cues now use v1's compact
  images by default, following the user's rollback after the first 29:38 test:
  its context inventory is again exactly 171,474 bytes, versus 540,569 with scopes.
  `--context-scopes` restores the larger projection as an explicit ablation.
  English glosses remain an explicit `--english` option. Every full source row,
  including context scopes, English, and provenance, remains in coordinator
  `source.json`; omitted context scopes are not part of the default reader input.
- All mapped targets remain available. QAC annotation gaps and missing inventories
  stay explicit. A rooted focus with no usable branch inventory stops preparation.
- The final [ledger schema](schemas/focus-trace-response.schema.json) is a
  byte-for-byte copy of v1's schema. Its `focus-trace-hermetic-response-v4` protocol
  names the existing response format; it does not refer to a different workflow.

The input repair derives ط ف ف → root_000940 from quran-data's
`accepted_masaq_qac_edges` and the lexical database's exact source-root identity.
The generator verifies the bridge checksum, schema version, accepted audit, release
metadata, and released QAC input. Its generated correction is pinned in
[data/root_mapping_repairs.json](data/root_mapping_repairs.json). Existing mapped
or split roots are never replaced by this scoped correction. To refresh it from
the authoritative bridge, run `python3 -B focus_trace_v3/scripts/build_alignment_repairs.py`
before preparing new jobs; already prepared inputs remain frozen.

**Prepare a fresh reader job**

```sh
python3 -B focus_trace_v3/workflow.py prepare \
  --focus 83:1 --surah-window \
  --model gpt-5.6-luna --effort max \
  --job focus_trace_v3/runs/my-luna-run/83_1
```

Use `--model gpt-5.6-sol` for the v1 model profile. Sol/max is the default.
Use `--window 83:1,83:2,83:3` for a deliberately selected local window. Preserve
the same evidence window in a comparison; a short-window result is not a
whole-surah result. Existing job directories are never overwritten.

The prepared files are:

| File | Role |
|---|---|
| `prompt.md`, `packet.json`, `reader.schema.json` | The reader's only linguistic/instructional inputs. |
| `job.json` | Coordinator assignment, explicit profile, options, frozen input hashes, implementation hashes. |
| `source.json` | Complete source snapshot for projection checks; coordinator-only. |
| `ledger.schema.json` | Frozen downstream v1 output contract; coordinator-only. |

**Generate with one isolated reader**

```sh
python3 -B focus_trace_v3/workflow.py render \
  focus_trace_v3/runs/my-luna-run/83_1 > /private/tmp/hft-v3-reader-input.txt
```

The rendered input contains the exact prompt, assigned reader ID, schema, and
complete inline packet. Launch one fresh reader on the explicit model and effort
in `job.json`, without inherited conversation, previous findings, or repository
access. Do not add a service-tier override. Capture the reader's final JSON as
`reader.response.json` inside the job. The reader does not manage files or tools.
If the exact profile cannot run, stop; do not substitute a model. This workflow
does not claim to verify an external launch from the model's self-report.

**Compile and validate**

```sh
python3 -B focus_trace_v3/workflow.py compile focus_trace_v3/runs/my-luna-run/83_1
python3 -B focus_trace_v3/workflow.py validate focus_trace_v3/runs/my-luna-run/83_1
```

Compilation produces `response.json` in the original v1 ledger format,
`evidence.json` with the cited ayah and every supplied branch variant, and
`compilation.json` with hashes and validation results. The raw reader response is
unchanged. Invalid IDs, incorrect root/branch joins, context citations in a baseline,
and deltas without branch-backed context all fail. Trigger-root lists and complete
occurrence indices are generated from selected evidence, including repeated roots
within an ayah. Existing different outputs are never overwritten.

Validation checks frozen hashes, the complete source-to-packet projection, and
recompilation equality. The original v1 validator checks a compatibility view of
the packet and the compiled ledger. This view is only for validation; the reader
sees the selected compact or scope-rich input. Resolution proves citation identity and artifact
consistency, not interpretive adequacy, model execution, or quality parity.

**Verification and first experiment**

```sh
python3 -B -m unittest discover -s focus_trace/tests -v
python3 -B -m unittest discover -s focus_trace_v3/tests -v
```

The offline tests cover the actual 83:1 repair, split roots, paired variants,
repeated occurrences, annotation gaps, wrong-root citations, outside-window
citations, baseline/context boundaries, frozen-input tampering, output consistency,
and preservation of the v1 semantic instructions and ledger schema. A separate
offline check converted the original v1 29:38 ledger to handles and back without
changing its content; only trigger-root list order was normalized.

Start by comparing Sol/max and Luna/max on identical full-surah 83:1 inputs, then
test integration on/off while holding language and evidence fixed. Use unseen
ayat and repeated samples before making a model-quality claim. Evaluate distinct
grounded mechanisms, integration, alternatives, unusual discoveries, containment,
artifact acceptance, and cost. Candidate count alone is not a quality metric.
The first scope-rich 29:38 Sol/Luna outputs and their comparison are recorded in
[runs/compare-20260906/comparison.md](runs/compare-20260906/comparison.md).
The compact-context rerun is tracked under `runs/rerun-20260906-compact/`.
The repeated fresh-v1/current-v3/revised-v3 comparison is tracked under
[runs/discovery-control-20260906/](runs/discovery-control-20260906/README.md).
All six usable Sol/max outputs passed. Both revised samples recovered counting,
but lost the developed crisis/relapse mechanism retained by both current samples.
Fresh v1 also varied. The [comparison](runs/discovery-control-20260906/comparison.md)
does not establish overall superiority or Luna parity.

In compact context cues, the reader forms `branch_key` from the supplied target
`mapped_root_id` and local `branch_id`, separated by `/`. Focus branches retain
explicit keys. Omitting the repeated context key restores the exact v1 context
inventory size without changing any root/branch choices. The compiler still
checks the combined identity against the selected occurrence.
