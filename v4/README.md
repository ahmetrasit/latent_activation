# GSLS-1A 4.0 — One Author, Three Stateful Passes

This package uses one persistent synthesis agent in one continuous session.

The agent receives three prompts in sequence:

1. `01_constructive_discovery_prompt.md` — recursive lexical discovery, coalition building, and backward reactivation.
2. `02_gold_synthesis_continuation.md` — passage-scale synthesis and the gold research document.
3. `03_publication_continuation.md` — publication prose by the same author while the synthesis remains active.

There is no critic, audit agent, frozen manifest, JSONL finding database, semantic QC stage, or separate renderer.

`00_same_agent_orchestration.md` explains execution. `04_input_packet_template.md` defines the evidence supplied to the agent. Furūq v4 semantic access is restricted to `branch_image_ar` and `what_is_ar`; `root_norm` and `branch_id` are identifiers only.
