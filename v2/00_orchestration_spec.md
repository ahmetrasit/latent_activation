# Three-Agent Gold-Standard Lexical Synthesis Orchestration

**Workflow ID:** `GSLS-3A-2.0`  
**Maximum logical agents:** `3`  
**Gold author:** `Agent A only`  
**Primary product:** `final-gold-notebook.md`  
**Optional product:** `publication-essay.md`

## 1. Feasibility decision

A three-agent ceiling is compatible with gold-standard synthesis. The essential condition is not a large agent count. It is that one agent owns the complete semantic trajectory from primary reading through secondary activation, recursive search, temporal replay, and final synthesis.

The architecture therefore does not split discovery among many specialists. It uses:

- one persistent synthesis agent;
- one independent adversarial auditor;
- one optional publication renderer.

The gold document is drafted and finalized by the same synthesis agent. The auditor can expose omissions and errors, but cannot rewrite the gold. The renderer can compose a publication view, but cannot discover, delete, merge, or regrade findings.

## 2. Agent topology

### Agent A — Integrated Synthesis Agent

Agent A is the only production role permitted to:

- interpret dictionary branches;
- model the passage;
- generate secondary activation hypotheses;
- build coalitions and hyperedges;
- perform progressive recitation and backward replay;
- form passage-scale channels;
- decide the primary effect of a resonance;
- author the draft gold notebook;
- adjudicate the audit;
- author the final gold notebook.

Agent A is a persistent logical agent. Prefer one continuous session. When context limits require continuation, use the same role prompt, the same agent identity, and a frozen state snapshot. A continuation is not a new analytical role and may not start an independent interpretation.

### Agent B — Adversarial Audit Agent

Agent B receives the full authorized evidence and Agent A's frozen draft. It:

- rechecks every finding;
- searches for missed supported relations;
- tests whether a branch was wrongly discarded for not being the local gloss;
- tests temporal leakage and overfitting;
- proposes exact actions.

Agent B does not write or edit the gold notebook. Its product is an audit action queue.

### Agent C — Publication Agent

Agent C is optional. It receives only the final frozen gold manifest, final gold notebook, exact passage, and render policy. It:

- selects compact or full publication architecture;
- writes the reader-facing essay;
- produces a paragraph-to-finding source map;
- verifies render closure.

Agent C may not alter the gold record. Omission from the optional essay never removes a finding from the gold notebook.

## 3. What counts as an agent

An agent is a distinct semantic role with its own conversational context and authority.

These do not count as additional agents:

- deterministic file validation;
- database queries with fixed read-only contracts;
- hashing;
- batching;
- sorting;
- exact-string verification;
- schema validation;
- queue construction from already recorded open roles;
- mechanical concatenation of immutable artifacts.

The orchestrator must not use hidden subagents, map-reduce semantic workers, independent branch analysts, or separate synthesis shards authored by different agents.

## 4. Production isolation

During production, Agents A, B, and C must not read:

- the gold document;
- prior evaluations;
- prior comparison reports;
- prior reader-facing outputs for the same passage;
- prompts containing the target answer;
- external commentary not declared in the source manifest;
- hidden semantic-network theme labels.

The quarantined gold may be used only after all production outputs are frozen, and only by a human or a separate non-production regression process.

## 5. Required run directory

```text
RUN/
  inputs/
    source-manifest.json
    source-manifest.md
    run-card.json
    run-card.md
    passage-arabic.txt
    primary-scaffold.md
    morphology.tsv
    syntax.tsv
    discourse.tsv                  # optional
    attachments.tsv                # optional
    lexical-branches.jsonl
    semantic-network.jsonl         # optional, retrieval-only
    acoustic-features.tsv          # optional
    controls/                      # optional
  agent-a/
    state/
      synthesis-state.json
      branch-frames.jsonl
      passage-events.jsonl
      progressive-trajectory.jsonl
      candidate-cards.jsonl
      coverage-ledger.jsonl
      query-history.jsonl
    draft/
      draft-gold-manifest.jsonl
      draft-gold-notebook.md
      draft-closure.md
    final/
      final-gold-manifest.jsonl
      final-gold-notebook.md
      adjudication-log.md
      final-closure.md
  agent-b/
    audit-report.md
    audit-actions.jsonl
    missed-candidate-proposals.jsonl
    audit-closure.md
  agent-c/
    publication-architecture.md
    publication-essay.md
    publication-map.jsonl
    render-closure.md
  logs/
    artifact-hashes.tsv
    stage-status.tsv
    file-access-audit.tsv
    model-sessions.tsv
    schema-validation.tsv
```

Artifacts are immutable after acceptance. A correction creates a new version or moves the run back to an earlier state; it never silently overwrites a frozen accepted artifact.

## 6. Operator-supplied evidence

The operator must supply:

1. exact Arabic passage text;
2. target scope and basmala/opening policy;
3. positioned morphology;
4. verified syntax or attachments;
5. a primary contextual scaffold;
6. every accepted clean branch for every passage root, with exact source prose and provenance;
7. source authorization rules;
8. output language and product policy.

Optional evidence includes discourse edges, acoustic observations, semantic-network routing hints, corpus controls, and verified cross-passage data.

A missing or empty lexical branch source blocks a lexical-synthesis run. The system may produce a separately labelled structural analysis, but must not call it a branch-activation result.

## 7. Source hierarchy

Evidence classes are distinct:

1. exact sacred text and position;
2. verified morphology, syntax, attachment, discourse, order, repetition, and voice;
3. exact clean dictionary prose;
4. documented definitions, derivations, variants, oppositions, and examples;
5. semantic-network topology as a retrieval lead only;
6. controls and corpus statistics.

Network membership, shared themes, root co-occurrence, conventional translation, or model familiarity never proves a relation.

## 8. Status dimensions

Never infer one dimension from another.

### Local sense status

- `sense-established`
- `sense-compatible`
- `sense-underdetermined`
- `sense-disfavored`
- `sense-incompatible`

### Activation status

- `untriggered`
- `locally-triggered`
- `coalition-triggered`
- `retrospectively-triggered`
- `conditional`
- `defeated`
- `pending-evidence`

### Narrative role

- `governing`
- `connective`
- `supporting`
- `incidental`
- `none`

### Epistemic status

- `accepted`
- `pattern-candidate`
- `pending-control`
- `defeated`
- `human-adjudication`

A branch may be non-established as a local gloss and still be a governing coalition-triggered resonance. A locally compatible branch may remain narratively irrelevant.

## 9. State machine

```text
PRECHECK
  ↓
A_INITIALIZE
  ↓
A_DISCOVERY
  ├─ new roles/candidates/replays → A_DISCOVERY
  └─ two complete no-novelty cycles → A_DRAFT
  ↓
B_AUDIT
  ↓
A_ADJUDICATE
  ├─ audit reopens discovery → A_DISCOVERY
  └─ all actions closed → A_FINAL
  ↓
C_RENDER_OPTIONAL
  ↓
VALIDATE
  ↓
DONE
```

Terminal states:

- `DONE-GOLD`
- `DONE-GOLD-AND-PUBLICATION`
- `BLOCKED-INPUT`
- `BLOCKED-EVIDENCE`
- `HUMAN-ADJUDICATION-REQUIRED`

## 10. Deterministic precheck

Before Agent A starts, the orchestrator must:

- verify all required paths exist;
- reject zero-byte lexical or morphology sources;
- verify the passage roots are covered by the lexical inventory;
- verify exact Arabic is anchorable;
- hash every input;
- validate `source-manifest.json` and `run-card.json`;
- quarantine gold/evaluation paths;
- create initial coverage rows for every occurrence, branch, and supplied edge.

Precheck performs no interpretation.

## 11. Agent A lifecycle

### 11.1 Full-context mode

Use `TASK_MODE: FULL` when all authorized evidence fits safely in one context. Agent A performs initialization, recursive discovery, internal validation, and draft generation in one continuous session.

### 11.2 Persistent-cycle mode

Use `TASK_MODE: INITIALIZE`, followed by one or more `DISCOVERY_CYCLE` messages, then `DRAFT_GOLD`, when the evidence is too large for one call.

All cycle messages go to the same Agent A session. The orchestrator supplies deterministic evidence batches and the frozen `synthesis-state.json`. Batching controls context; it does not distribute semantic interpretation.

A batch may be organized by:

- root dossier;
- occurrence × branch seed range;
- construction seed range;
- unresolved open role;
- passage-native macroblock.

The same agent must retain a whole-passage map and revisit earlier conclusions after every batch.

### 11.3 Integrated internal phases

Agent A performs these duties as one reasoning trajectory:

1. preflight confirmation;
2. primary passage model;
3. relational branch-frame extraction;
4. progressive recitation state;
5. primary-anchor-first search;
6. occurrence × branch seed search;
7. construction and form seed search;
8. coalition and hyperedge formation;
9. same-root branch transitions;
10. cross-root definitional and operational relations;
11. open-role retrieval;
12. backward reactivation;
13. rival models and ablation;
14. draft gold manifest and notebook.

No stage may treat “not the local gloss” as “inactive.”

## 12. Dynamic discovery loop

The same agent repeatedly executes:

```text
candidate
→ typed relation
→ primary effect
→ open roles
→ targeted retrieval
→ coalition test
→ progressive or backward replay
→ revised earlier node
→ new candidate or defeat
```

Every discovery that creates a new role must create a targeted query. Typical roles include:

- source;
- recipient;
- leader;
- collective;
- instrument;
- target interior;
- container;
- contents;
- force;
- resistance;
- standard;
- measure;
- direction;
- reversal;
- agency holder;
- result state;
- knower;
- closure demand.

The orchestrator may materialize the query queue mechanically from Agent A's recorded open roles, but only Agent A interprets the returned evidence.

## 13. Discovery closure

Agent A may draft the gold only when all are true:

- every passage occurrence has been modeled;
- every eligible branch has a disposition;
- every construction seed has a disposition;
- the active query queue is empty;
- two complete cycles generated no new candidate, open role, reactivation, or changed earlier interpretation;
- every live candidate has a typed relation, primary effect, boundary, counterfactual, and source references;
- every unresolved item is explicitly pending or sent to human adjudication.

## 14. Draft products

Agent A writes:

- structured state;
- branch frames;
- passage events;
- progressive trajectory;
- candidate cards;
- coverage ledger;
- draft gold manifest;
- draft gold notebook;
- draft closure report.

The notebook is not a single-axis essay. It is a ranked, multi-channel research synthesis that explains how each accepted secondary activation changes a primary reading.

## 15. Agent B audit

Agent B receives:

- all authorized source evidence;
- Agent A's frozen state and draft products;
- deterministic coverage indexes;
- no gold or prior evaluation.

Agent B must:

- verify exact evidence;
- test every relation edge;
- test branch-sense and activation independence;
- search for missed coalition-triggered findings;
- test progressive-lane integrity;
- test counterfactuals and ablations;
- identify overjoined or theme-only claims;
- test whether one vivid channel suppressed independent channels;
- test base-rate and generic-root-field risks;
- propose exact actions.

Agent B outputs actions only. It does not rewrite the gold.

## 16. Agent A adjudication

The same Agent A receives the frozen audit and:

- accepts, modifies, or rejects every action;
- cites exact evidence and reasoning;
- reopens discovery when an audit proposal creates a valid new role;
- updates candidate versions;
- preserves an adjudication log;
- writes the final gold manifest and final gold notebook.

The final gold notebook remains Agent A's product.

## 17. Agent C optional publication

Agent C selects publication mode from positive structural evidence.

### Compact mode

Use when:

- the passage is compact;
- one stable discourse situation dominates;
- one hinge performs most backward reactivation;
- no early role-complete scene is transferred into a later domain.

### Full mode

Use when:

- several role-complete macroblocks exist;
- participants, voice, agency, domain, or epistemic status change substantially;
- an early operation is later applied, reversed, or exposed;
- several independent cross-block bridges are required.

Agent C renders only findings authorized by the final manifest and records all essay omissions without altering gold coverage.

## 18. Machine gates

The orchestrator must enforce:

- schema validity;
- file hashes;
- exact source coverage;
- no missing branch dispositions;
- no candidate without `primary_effect`;
- no terminal local-gloss gate;
- no theme-only relation;
- no progressive use of later evidence;
- audit action closure;
- final notebook coverage;
- publication source-map closure.

## 19. Quality principle

The workflow preserves the advantage of a single gold-producing agent while adding two safeguards:

- Agent B prevents unnoticed evidence failure and omission.
- Agent C prevents publication style from corrupting research discovery.

The agent limit is therefore not a compromise in principle. It is a deliberate concentration of synthesis authority.
