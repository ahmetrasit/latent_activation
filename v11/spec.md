# v11 Specification — Recall-First Branch Activation

## Goal

Given a surah or ayah group, generate a repeatable, auditable candidate network that exposes possible primary and secondary Qnet branch activations.

The workflow is designed for discovery. Conservative filters should be relaxed unless they protect against data corruption.

## Hard pre-agent gate: QAC-first root resolution

Every run must start from QAC, not from Qnet.

```text
QAC passage words
  → QAC morpheme roots/root_join_keys
  → Furūq root_id resolution
  → Qnet node/theme lookup
```

This is a hard gate because Arabic root keys can differ across layers, especially with hamza:

```text
ء ل ه / أ ل ه
ك ف ء / ك ف أ
ٱ / ا / أ / إ / آ
```

The script must emit a root-resolution audit containing:

```text
QAC root
QAC root_join_key
lookup variants
matched Furūq root_id
matched root_norm/source_root_norm
resolution status
```

Agents must not start if any surface root is unresolved or ambiguous. Missing Qnet theme membership is different from missing root resolution; if Furūq branches exist but a Qnet layer lacks theme nodes, switch to a fuller Qnet layer before running agents.

The default script behavior must enforce this:

```text
unresolved/ambiguous root id => stop
resolved root with Furūq branches but zero Qnet branch nodes => stop
```

Override flags are allowed only for diagnostics, not normal workflow.

## Non-goals

- Do not collapse every candidate into a final interpretation.
- Do not require proof-level certainty for secondary branches.
- Do not turn branches into graph nodes in the final graph.
- Do not hide weak candidates; label them.

## Evidence families

The script emits evidence. Agents interpret it.

### Direct

- surface root present
- surface word/lemma/morphology
- repeated form

### Relational

- shared leaf theme
- shared parent theme
- shared raw keyword
- Q2 branch relation

### Passage-structural

- ayah order
- repeated construction
- contrast frame
- local adjacency

### Discovery-functional

- branch supplies a possible hidden role
- branch explains a secondary underlay not visible in the surface gloss
- branch creates a coherent pathway with two or more passage roots

## Relaxed discovery rules

1. Theme overlap alone may create a `C` candidate.
2. Broad themes are not discarded; they are marked broad.
3. One-hop root-to-root activation is enough to preserve a candidate.
4. Same-root branch clusters are preserved, but marked as weaker than cross-root bridges unless the passage requires them.
5. Q2 candidates are always preserved.
6. Missing or mismatched branch data becomes `X`; this is the one hard conservative gate.

## Suggested scoring hints

Scores are not judgments. They only sort review queues.

```text
shared raw keyword        +4
Q2 relation               +5
shared leaf theme         +2
shared parent theme       +1
rare theme bonus          +1
same-root bridge          -1
high-connectivity branch  no penalty; add "high-connectivity" flag only
```

The key design choice is not to subtract away broad possibilities. Instead, keep them and expose their evidence profile.

## Discovery-value ranking

Activation and discovery are different.

```text
activation = this branch may be live in the passage
discovery value = this branch adds surprise or hidden explanatory force
```

Do not use discovery value to delete candidates. Use it to focus the final report.

High discovery value signals:

1. the branch is not the obvious surface branch;
2. another root activates it;
3. there is a Q2 relation or shared raw keyword;
4. it opens a material/metaphorical underlay such as measurement, yield, body, life-stage, pressure, containment, weather, provision, or social dependency;
5. it changes the passage mechanism rather than merely repeating the surface gloss.

Low discovery value signals:

1. the branch paraphrases the surface reading;
2. the bridge is only a generic ethical/social/cognitive field;
3. the branch adds coherence but no surprise.

Low discovery value does not mean silent.

## Agent classification contract

```text
A = direct/surface/structural activation
B = strong latent activation, likely doing passage work
C = exploratory latent activation; preserve for inspection
S = no visible current bridge
X = data/inventory problem
```

## Required output discipline

For every `A`, `B`, or `C/B` branch, include:

```text
branch id
functional role
evidence trace
what activates it
what it activates
what surface reading misses without it
```

For every `C`, include only a compact evidence trace.

For every `S`, do not elaborate unless it is surprising.

For every `X`, identify the data issue.

## Final integration/report agent

The final report is an agent-produced artifact.

The orchestrator's role is to:

```text
prepare the clean packet
verify the pre-agent gate passed
start the final integration agent
save the returned report
validate file shape
```

The orchestrator should not manually decide the final synthesis when an agent workflow is being used. If a report language is requested, pass that language directly to the final integration agent. Turkish final reports should preserve the technical labels (`A`, `B`, `C/B`, `C`, `S`, `X`) while explaining the mechanism in Turkish.
