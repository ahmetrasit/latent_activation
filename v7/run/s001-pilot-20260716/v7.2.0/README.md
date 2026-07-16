# S001 Prompt Pilot: V7.2.0

This run tests the immutable V7.2.0 prompts against the existing frozen V3
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

Agent 1 executes tasks 01-04 in one persistent session. Agent 2 starts fresh
and executes tasks 05-07 in one persistent session, using the semantic master
as its sole semantic authority. No prompt receives the gold reference or prior
S1 publications.

Expected outputs:

```text
a1/01-activation-reservoir-v7.2.0.md
a1/02-mature-configurations-v7.2.0.md
a1/03-reciprocal-field-v7.2.0.md
a1/04-semantic-master-tr-v7.2.0.md
a2/05-oral-rehearsal-tr-v7.2.0.md
a2/06-publication-draft-tr-v7.2.0.md
1-publication-tr-v7.2.0.md
```
