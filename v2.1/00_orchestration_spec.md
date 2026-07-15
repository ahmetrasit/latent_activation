# GSLS 2.1 Orchestration Specification

## Purpose

Produce a source-bounded lexical synthesis that explains how passage structure, positioned morphology, and admissible lexical branches combine into interpretive findings. The workflow coordinates editorial roles; it is not an artifact-integrity audit system.

## Roles

- **Agent A:** sole author of draft and final synthesis findings.
- **Agent B:** independent substantive reviewer. It tests evidence, reasoning, calibration, and omissions without writing the synthesis.
- **Agent C:** optional publication renderer. It cannot introduce or upgrade claims.
- **Orchestrator:** prepares inputs, emits bounded task files, checks minimal output shape, and promotes a clean draft.

## Evidence boundary

Agents may use only the prepared files listed in their task. Raw `resources/`, the `v1/` tree, translations, prior target prose, evaluation documents, network retrieval, and model memory are not production evidence.

Each prepared lexical record has exactly six authoritative fields: `root_id`, `root_norm`, `branch_id`, `what_is_ar`, `branch_image_ar`, and `source_phrase_ar`. Agents use no other lexical metadata. Contaminated V4 branches are excluded during preparation.

## Flow

```text
PRECHECK
  -> A_SYNTHESIZE
       complete -> B_REVIEW
       evidence_blocked -> BLOCKED_EVIDENCE

B_REVIEW
  -> clean -> FINALIZE
  -> revision_required -> A_REVISE -> FINALIZE
  -> human_needed -> HUMAN_NEEDED
  -> evidence_blocked -> BLOCKED_EVIDENCE

FINALIZE
  -> DONE
  -> C_RENDER -> DONE_WITH_PUBLICATION
```

On a clean review, the orchestrator copies the draft synthesis to the final paths unchanged. Agent A is called again only when Agent B requires a substantive revision.

## Work products

Agent A draft:

```text
agent-a/draft/draft-synthesis.jsonl
agent-a/draft/draft-synthesis.md
```

Agent B review:

```text
agent-b/review.md
```

Final synthesis:

```text
agent-a/final/final-synthesis.jsonl
agent-a/final/final-synthesis.md
```

Optional rendering:

```text
agent-c/publication.md
```

## Minimal gates

- Prepared inputs exist, parse, and agree on passage scope.
- Prepared lexical records have exactly the six authorized fields, and accepted branches cover the passage roots.
- Each synthesis finding contains anchors, lexical evidence, trigger, relation, bridge, effect, counterfactual, boundary, sense status, activation, confidence, role, and limitations.
- Agent B's first line states a usable verdict; revision-required reviews identify a target and required change.
- Required synthesis and prose files are non-empty.

The runtime does not hash files, freeze outputs again, maintain provenance ledgers, score findings, require closure artifacts, record agent sessions, or re-audit the complete SQLite databases after preparation.
