# Repeated 29:38 discovery comparison

Prepared after the user accepted a fresh-v1 control and a v3 recovery candidate.
Two fresh Sol/max reader sessions per condition; six sessions total. No Luna
runs in this experiment. All use the same 69-ayah window, Arabic-only evidence,
and a context inventory byte-identical to v1 (171,474 bytes).

| Condition | Prompt | Evidence/citations | Execution |
|---|---|---|---|
| `v1` | Unmodified v1 | Original packet and full citation fields | Assigned files, shell available, writes and compacts its output |
| `v3-current` | Original compact v3, integration on | Frozen compact v3 packet and handles | Complete inline input, tools disabled |
| `v3-revised` | Integration off; explicit v1 split-root prohibition restored | Same compact v3 packet and handles | Same inline launcher as current v3 |

The two v3 conditions differ in exactly those two prompt changes. This tests a
bundled recovery candidate, not the separate causal effect of either change.
The v1 condition tests the documented workflow as a whole; it is not an isolated
citation-format or delivery-mode experiment. The original v1 run lacks a runtime
receipt, so its exact historical tool behavior cannot be reproduced knowingly.
The coordinator validates v1 after the session; the reader receives no validator
source, comparison rubric, historical output, or follow-up repair instruction.

V3 current inputs, including the prompt, are byte-identical to the prior compact
Sol job. Revised v3 changes only the prompt; full source, packet, and both schemas
are byte-identical. V1's prompt, packet, and schema are exact copies of the existing
29:38 inputs. The original v1 result remains an additional historical reference,
not an unquestioned gold answer. Earlier v3 runs are supplementary observations,
not part of the balanced two-per-condition comparison.

`launch.py` requires a clean working tree and records the commit before launching
all six sessions concurrently. Each uses `gpt-5.6-sol`, `max`, fresh context, no
model fallback, no service-tier override, no automatic retry, and no semantic repair.
Existing launch records are never overwritten. V1 reader tools are confined by
instructions to its isolated assigned files; its write sandbox is the isolated
temporary directory. V3 readers have no tools. Tool availability is recorded as
an intentional between-workflow difference.

## Evaluation fixed before generation

The coordinator-only [rubric](rubric.md) evaluates retention, coherent integration,
new grounded mechanisms, speculative containment, and artifact correctness.
Finding and citation counts are descriptive, not a quality score. Two samples
per condition cannot establish population-level superiority or omission rates.

Prepare and inspect inputs, run offline tests, and commit before running:

```sh
python3 -B focus_trace_v3/runs/discovery-control-20260906/launch.py --check
python3 -B focus_trace_v3/runs/discovery-control-20260906/launch.py
```

Outputs, runtime receipts, validation, and the comparison will be retained here.

## Execution-host correction

The first two v1 sessions could not read any input: shell access was enabled but
the execution host was disabled. Both returned a failure note and no response
JSON. Their artifacts remain under `v1-1` and `v1-2`; they are infrastructure
failures, not semantic samples. [host-recovery.json](host-recovery.json) records
the diagnosis and the two replacements, `v1-host-1` and `v1-host-2`.

The replacement launcher enables the installed execution host and uses exactly
the same frozen v1 prompt, packet, schema, model, and effort. The correction and
replacement inputs are committed before launch. Because the original four v3
readers are already running, their untracked runtime files are the only permitted
working-tree changes at replacement launch; code and inputs must be committed.
This explicit infrastructure correction does not retry or replace a semantic
output. Run it with `launch.py --recover-v1-host`.
