# HFT status and version decision

Decision date: 2026-09-06.

**Continue Hermetic Focus Trace with v1 in `focus_trace/`, using
`gpt-5.6-sol` at `max` effort. HFT v2 and v3 failed and are retired.**

The HFT version labels here refer to the following workflow directories:

| HFT version | Directory | Status |
|---|---|---|
| v1 | [`focus_trace/`](README.md) | Active; use for new HFT generation and improvements. |
| v2 | [`focus_trace_v2/`](../focus_trace_v2/README.md) | Failed experiment; retired. |
| v3 | [`focus_trace_v3/`](../focus_trace_v3/README.md) | Failed experiment; retired. |

## Why the experiments are closed

The objectives were to improve on v1 and/or obtain almost the same output quality
with Luna. Neither v2 nor v3 established enough improvement or reliable quality
retention to justify replacing v1, and near-v1 Luna quality was not established.

V2's successive prompt, input, and two-stage changes recovered some findings and
expanded output, but left discovery/integration gaps and, in later comparisons,
invalid ledgers. V3 improved evidence assembly and recovered some specific
readings, but the compact and repeated tests still showed mixed gains and losses.
Restoring the split-root instruction while disabling the added integration step
recovered counting in both revised samples but lost developed crisis/relapse
readings found in both unchanged-v3 samples.

Fresh v1 also varied and did not reproduce every historical finding. The failure
decision means the experiments did not meet the project's adoption goals; it
does not claim that every v1 output beats every v2 or v3 output.

## Continuing work

- Use v1's existing prompt, packet builders, response contract, and validation
  workflow in [README.md](README.md).
- Keep the accepted [83:1 input repair](repairs/83_1/README.md). It is already
  applied to v1 and remains valid independently of the retired experiments.
- Continue HFT generation and improvements from v1. Luna is not the adopted HFT
  reader profile.
- Preserve v2/v3 code, frozen inputs, outputs, and reports for historical review
  and reproduction. Their proposed follow-up tests and prepared, unrun jobs are
  archived work, not an active queue.
- Treat this decision as superseding earlier plans to continue or promote v2/v3.
  No v2/v3 prompt, compiler, or execution changes are adopted into v1 by this
  documentation decision.

## Evidence retained

- [Initial v2 comparison](../focus_trace_v2/runs/compare-20260905.comparison.md).
- [V2 with the restored v1 contract](../focus_trace_v2/runs/rerun-20260906-v1.md).
- [V2 two-stage comparison](../focus_trace_v2/runs/rerun-20260906-two-stage.md).
- [Initial v3 Sol/Luna comparison](../focus_trace_v3/runs/compare-20260906/comparison.md).
- [Compact v3 Sol/Luna rerun](../focus_trace_v3/runs/rerun-20260906-compact/comparison.md).
- [Repeated fresh-v1/current-v3/revised-v3 comparison](../focus_trace_v3/runs/discovery-control-20260906/comparison.md).
