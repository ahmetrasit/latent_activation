# Latent Activation Orchestration Documentation

Status: planning and repository audit complete; the graph implementation
described here has not started. The existing `v13/` dynamic-retrieval workflow
is a separate predecessor.

## Start Here

Read [ORCHESTRATION_PLAN.md](ORCHESTRATION_PLAN.md) in full before changing the
repository. It is the authoritative cold-agent handoff and contains:

- the problem history and intended interpretive outcome;
- verified repository, corpus, runtime, storage, and Qnet findings;
- the zero-gold scientific contract;
- the proposed graph, activation, and coalition architecture;
- schemas, equations, controls, gates, stop conditions, and acceptance criteria;
- a phase-by-phase implementation and evaluation sequence;
- multi-agent orchestration boundaries and a cold-start runbook;
- risks, failure diagnoses, decision records, and primary references.

## Fixed Starting Decisions

1. Begin with the 10,820 clean accepted `quranic` branches, not all 18,781
   accepted Quranic and Furuq branches.
2. Do not train a small language model first.
3. Build a deterministic multi-view baseline, a fixed multilingual dense
   baseline, a sparse graph, restart diffusion, and bounded coalition search.
4. Do not make Qnet a runtime or data dependency.
5. Keep existing synthesis and gold material sealed until configuration is
   frozen. Gold is initially a blind reference, not a training target.
6. Escalate to self-supervised encoder or graph adaptation only if the frozen
   fixed-encoder baseline fails its declared diagnostics.

## Migration Requirement

The inspected machine had only about 2.4 GiB free. Move or clone the repository
to a filesystem with at least:

- 5 GiB free for the fixed-encoder baseline;
- 15 GiB free before producing local training checkpoints.

The dense 10,820 by 10,820 matrix is computationally feasible, but it is not a
required persistent artifact. Blockwise exact similarity plus top-K retention is
the default.

## Execution Boundary

The next graph implementation should live under the proposed `v14/` layout
described in the plan. Do not write generated embeddings, matrices, caches, or model
checkpoints into this documentation directory.

Any agent taking over should first execute Phase 0 and reproduce the hard corpus
counts. A mismatch is a stop condition, not an invitation to silently revise the
inventory.
