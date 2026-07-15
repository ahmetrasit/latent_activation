# GSLS 2.1 Schema Contract

Schemas describe evidence records and the epistemic shape of synthesis findings. They do not encode orchestration history or administrative closure.

## Prepared inputs

| Schema | Artifact |
|---|---|
| `run-card.schema.json` | `inputs/run-card.json` |
| `input-summary.schema.json` | `inputs/input-summary.json` |
| `morphology-row.schema.json` | morphology row shape produced by the adapter |
| `syntax-edge.schema.json` | normalized syntax edge shape |
| `lexical-branch.schema.json` | each prepared lexical branch |
| `source-profile.schema.json` | resource profile |

## Synthesis finding

`synthesis-finding.schema.json` applies to every line of the draft and final JSONL files. Its required fields preserve the analytical distinctions that matter:

- proposition, primary passage anchors, and secondary carriers;
- exact lexical evidence identifiers;
- local trigger and typed relations;
- relational bridge and interpretive effect;
- counterfactual value and linguistic boundary;
- branch-specific sense status;
- passage activation, lexical evidence strength, activation confidence, epistemic status, and narrative role;
- limitations and publication policy.

The schema allows additional properties so Agent A can represent a richer synthesis without failing on harmless extensions. The Markdown notebook remains the primary intellectual product; JSONL is its compact evidence map.

Agent B and Agent C write prose rather than ledgers. Their minimal machine-readable control is the review verdict line and the expected output path.
