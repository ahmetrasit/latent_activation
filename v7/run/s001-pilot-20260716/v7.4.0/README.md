# S001 Prompt Pilot: V7.4.0

This run tests the immutable V7.4.0 prompts against the existing frozen V3
input bundle:

```text
v3/run/s001-full-20260716/inputs/
```

Runtime for every turn:

```text
MODEL: gpt-5.6-sol
REASONING_EFFORT: max
SERVICE_TIER: unset
```

Agent 1 executes Tasks 01-03 in one persistent formation session. Agent 2
starts fresh and executes Tasks 04-05 in one persistent independent synthesis
session, reading the raw bundle before Agent 1's reservoir and reciprocal field
and treating neither artifact as a ceiling.
Agent 3 starts fresh and executes Tasks 06-08 in one persistent Turkish
publication session. No prompt receives the gold reference, a prior V7 output,
or another S1 publication.

Expected outputs:

```text
a1/01-activation-reservoir-v7.4.0.md
a1/02-mature-formations-v7.4.0.md
a1/03-reciprocal-field-v7.4.0.md
a2/04-independent-mechanism-map-v7.4.0.md
a2/05-semantic-master-tr-v7.4.0.md
a3/06-oral-rehearsal-tr-v7.4.0.md
a3/07-publication-draft-tr-v7.4.0.md
1-publication-tr-v7.4.0.md
```
