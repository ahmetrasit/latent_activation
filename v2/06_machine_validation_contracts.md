# Machine Validation Contracts

**Workflow:** `GSLS-3A-2.0`

## 1. Agent-count contract

Reject a run when:

- more than three logical agent IDs appear;
- a production prompt delegates semantic work;
- Agent A outputs reference independent semantic subagents;
- branch or passage shards were authored by different semantic agents;
- Agent B or Agent C authors or directly edits the gold notebook.

Allowed agent IDs:

```text
A
B
C
```

Agent C may be absent.

## 2. Universal artifact headers

Every Markdown model artifact begins with:

```text
WORKFLOW_ID: GSLS-3A-2.0
AGENT_ID:
TASK_MODE:
MODEL_ID:
SESSION_ID:
CREATED_AT:
SOURCE_ARTIFACTS:
GLOBAL_CLOSURE:
```

Every JSONL record includes:

```text
workflow_id
run_id
agent_id
schema_version
source_refs
```

## 3. Session continuity

For Agent A continuation:

- `agent_id` remains `A`;
- `session_id` remains the same when technically possible;
- otherwise `continuation_of_session_id` is required;
- the new state must name `state_hash_parent`;
- no independent reset is allowed.

## 4. Input preflight

Block when:

- lexical source is missing or zero bytes;
- morphology is missing or zero rows;
- passage roots lack branch coverage;
- exact Arabic cannot be verified;
- a required source hash is absent;
- a prohibited gold/evaluation path is readable.

## 5. Branch coverage

Every eligible branch has exactly one terminal disposition:

```text
used-in-finding
support-only
reviewed-no-distinct-finding
inactive-under-current-evidence
defeated-by-form
pending-evidence
source-blocked
```

“Not the local gloss” is not a terminal disposition reason.

## 6. Passage coverage

Require one passage-event record for every positioned occurrence and one disposition for every supplied syntax/discourse edge.

## 7. Candidate validity

Reject a live candidate when any is empty:

```text
primary_proposition
primary_anchors
secondary_carriers
local_trigger
relation_edges
relational_bridge
primary_effect
counterfactual
linguistic_boundary
source_refs
```

## 8. Relation validation

Flag when:

- network membership is the only basis;
- a broad theme is the only basis;
- carriers are not incident to relation edges;
- removing a carrier leaves the claim unchanged;
- a relation type is unrecognized and undefined.

## 9. Local-gloss gate

Flag any terminal logic equivalent to:

```text
non-local branch
→ background only
→ no passage role
```

A record may conclude `untriggered` only after testing:

- local construction;
- order;
- repetition;
- coalition;
- role correspondence;
- backward reactivation.

## 10. Progressive integrity

Progressive records are monotonic in passage position.

Reject when a progressive step cites a later position. Later evidence must appear in a backward-replay record with both trigger and earlier node.

## 11. Dynamic closure

Draft closure requires:

```text
active_queries == 0
no_novelty_cycles >= 2
branches_without_disposition == 0
occurrence_branch_seeds_without_disposition == 0
construction_seeds_without_disposition == 0
live_candidates_without_primary_effect == 0
live_candidates_without_boundary == 0
unresolved_open_roles_without_status == 0
```

## 12. Audit closure

Every required Agent B action must receive an Agent A adjudication.

Reject final gold when:

- a required action is absent from the adjudication log;
- Agent A accepts a missed candidate without rerunning the relevant search;
- Agent A rejects an action without evidence references;
- unresolved action count is non-zero and final status is `accepted`.

## 13. Gold closure

Every final finding must map to:

- a notebook section;
- a channel;
- source references;
- a branch disposition;
- a candidate version.

Conditional and pending findings may not silently disappear.

## 14. Publication closure

Every `required-body` finding maps to at least one essay paragraph.

`publication-map.jsonl` must contain:

```text
new_claims: []
```

for every paragraph.

## 15. File access audit

Reject production when an agent reads:

- gold;
- evaluation;
- comparison;
- prior target prose;
- hidden network labels;
- unlisted external commentary.

## 16. Immutability

After each accepted state:

1. compute SHA-256 outside the model;
2. record byte size and unit count;
3. freeze the artifact;
4. require the exact hash downstream.

## 17. Required stage-status rows

```text
state
agent_id
session_id
task_mode
input_hash_set
output_paths
output_hash_set
schema_status
closure_status
blocking_errors
warnings
accepted_at
```

## 18. Final terminal gate

`DONE-GOLD` requires:

```text
preflight_passed
agent_a_draft_closed
agent_b_audit_closed
agent_a_adjudication_closed
final_gold_schema_valid
final_gold_coverage_valid
file_access_clean
artifact_hashes_complete
```

`DONE-GOLD-AND-PUBLICATION` additionally requires publication closure.
