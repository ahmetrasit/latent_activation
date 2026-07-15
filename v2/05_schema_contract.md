# Human-Readable Schema Contract

**Workflow:** `GSLS-3A-2.0`

Machine-readable JSON Schemas are in `schemas/`.

## 1. Source manifest

Required top-level fields:

```text
workflow_id
run_id
created_at
sources[]
prohibited_paths[]
gold_quarantine
```

Each source records:

```text
source_id
path
source_type
required
evidence_class
version
sha256
access
permitted_agents
query_contract
contamination_status
```

## 2. Run card

Required fields:

```text
workflow_id
run_id
passage_id
scope
basmala_policy
output_language
agent_limit
agent_a_session_policy
production_mode
network_use_policy
external_evidence_policy
gold_quarantine
output_paths
```

`agent_limit` must be `3`.

## 3. Branch frame

Required fields:

```text
frame_id
root_norm
branch_id
source_id
source_name
source_quote_ar
frame_status
predicate
roles
direction
medium
force
state_before
state_after
result
polarity
derivation_distance
source_refs
```

A branch without a usable frame receives `frame_status: reviewed-no-frame`.

## 4. Passage event

Required fields:

```text
event_id
position
recitation_index
surface_ar
root_norm
lemma_ar
morphology
syntax_edges
discourse_edges
primary_proposition_ids
participants
primary_contextual_sense
opening_hinge_closure_role
```

## 5. Synthesis state

Required fields:

```text
workflow_id
run_id
agent_id
phase
cycle_id
no_novelty_cycles
last_passage_position
coverage
active_queries
candidate_ids
open_roles
human_adjudications
input_hashes
state_hash_parent
```

## 6. Candidate card

Mandatory semantic fields:

```text
candidate_id
version
source_lanes
primary_proposition
primary_anchors
secondary_carriers
local_trigger
relation_edges
relational_bridge
primary_effect
counterfactual
linguistic_boundary
generating_set
unused_at_freeze
corroborators
constraints
rivals
open_roles
temporal_trajectory
local_sense_status
activation_status
narrative_role
epistemic_status
lexical_evidence_strength
activation_confidence
validation_tests
source_refs
status
```

A candidate is invalid when `primary_effect`, `local_trigger`, `relation_edges`, or `linguistic_boundary` is empty.

## 7. Gold finding

A final finding extends a candidate with:

```text
finding_id
title
level
channel_id
confidence
validation
notebook_order
publication_policy
subsumed_by
```

Allowed levels:

- `I-core`
- `II-distributed`
- `III-conditional`
- `appendix-resonance`
- `defeated`

## 8. Audit action

Required fields:

```text
action_id
target_id
verdict
issue_type
severity
required
evidence_refs
reason
proposed_change
reopen_discovery
status
```

## 9. Publication map

Required fields:

```text
paragraph_id
finding_ids
primary_positions
branch_sense_force
activation_force
epistemic_force
limitations_realized
new_claims
```

`new_claims` must be empty at final closure.


## 9A. Branch disposition

Required fields:

```text
root_norm
branch_id
source_id
disposition
reason
tested_activation_channels
finding_ids
source_refs
```

A branch marked `inactive-under-current-evidence` must record the activation channels tested. Failure to be an established local gloss is never sufficient.

## 9B. Dynamic query job

Required fields:

```text
query_id
cycle_id
source_candidate_ids
open_role
required_relation_types
eligible_scope
evidence_paths
status
result_candidate_ids
```

## 9C. Agent A adjudication record

Required fields:

```text
action_id
target_id
decision
reason
evidence_refs
candidate_versions_changed
discovery_reopened
resulting_artifacts
```

## 10. Cross-file closure

The validator must prove:

```text
all eligible branches
= used + support-only + reviewed-no-distinct-finding
  + inactive-under-current-evidence + defeated-by-form
  + pending-evidence + source-blocked

all live candidates
= final findings + defeated register + pending register
  + human adjudication register

all required audit actions
= accepted + accepted-with-modification + rejected-with-reason
  + human-adjudication

all required publication findings
= paragraph map coverage
```

## 11. Prohibited inference rule

The following implication is invalid:

```text
local_sense_status != sense-established
→ activation_status = untriggered
```

The validator must flag any terminal record that implements this logic without an independent activation analysis.

## 12. Relation basis

Every relation edge must use a typed predicate and at least one admissible basis:

- explicit definition;
- documented derivation or variant;
- shared narrow concrete operation;
- same-dimension opposition;
- verified passage contact;
- verified form;
- verified order or repetition;
- verified backward reactivation.

Broad theme or network topology alone is invalid.
