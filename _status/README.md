# Project Status Workspace

Last updated: 2026-07-21

This directory is the durable control point for active integration work. It
records what is being compared, which decisions govern the merge, what remains
unverified, and the next executable step. It is not a replacement for canonical
source artifacts under `v12/` or publication artifacts under `_prose/`.

## Active Workstream

The historical S1 calibration integrates these two v12 readings:

- standard v12 frozen control:
  `v12/runs/s001/full_context_control/reader_s001_b_ayah_walk.md`;
- eleven-ayah/±5 treatment output:
  `v12/runs_11ayah/s001/full_context_control/reader_s001_a_ayah_walk.md`.

The governing workflow is [V12_CROSS_RUN_WORKFLOW.md](V12_CROSS_RUN_WORKFLOW.md).
The exact restart point and production-readiness decision are in
[v12_cross_run/STATUS.md](v12_cross_run/STATUS.md).

## Current Checkpoint

Status: integration machinery is ready for a controlled pilot, but not yet for
corpus-wide production. S1 extraction is complete; 1:0, 1:2, 1:5, and 1:6 are
graded, while only 1:6 has a terminal publication decision.

Verified:

- the standard S1 run is pinned by `frozen_run.json`;
- its packet validates against the current QAC and accepted,
  non-contaminated Furūq resource hashes;
- both historical reader outputs walk the same visible S1 references:
  `1:0, 1:2, 1:3, 1:4, 1:5, 1:6, 1:7`;
- the ±5 prompt differs from the standard prompt in its declared default focus
  radius, but both readers actually received the same whole-surah S1 packet;
- primary commentary and translation-governing lexical activation must be
  adjudicated independently.
- 80 atomic source findings are retained across the two runs;
- the current ledger has 20 claims and 113 classified evidence rows;
- the 1:6 calibration has 7 claims and 40 evidence rows;
- swallowing/disappearance is a strong secondary analogical resonance and is
  excluded from translation input;
- the production architecture now uses a root orchestrator and fresh stage
  workers; no workflow CLI invokes agents;
- normal validation is limited to schema, lineage, score arithmetic, and
  translation guardrails.

Open production issues:

- the ±5 S1 directory has no `frozen_run.json` and no local packet copy;
- its use of the standard S1 packet is strongly indicated by the output, but
  the historical packet hash is not recorded;
- until resolved, it is a reconstructed reader/protocol variant, not a fully
  frozen independent replication.
- production must use actual focus-specific packets: regular v12 sees only
  focus ±2 ayat and wide v12 sees only focus ±5 ayat, clipped at boundaries;
- prompt wording alone does not enforce this visibility boundary;
- source discovery does not yet select paired per-focus manifests;
- S1 still needs publication for 1:0, 1:2, and 1:5 and full processing for
  1:3, 1:4, and 1:7.

## Next Action

Resume from the exact task matrix in
[v12_cross_run/STATUS.md](v12_cross_run/STATUS.md). The immediate S1 tasks are
publication for 1:0, 1:2, and 1:5, plus normalization for 1:3, 1:4, and 1:7.
In parallel at the design layer, add frozen per-focus ±2/±5 source inputs before
calling any result a production window comparison.

The normative production package is
[v12_cross_run/README.md](v12_cross_run/README.md).
