# S112 V7.5.0 Semantic Benchmark

This run binds the prepared S112 input bundle to V7.5.0 Tasks 1-5.

```text
semantic component: V7.5.0
passage id:         112
input root:         v3/run/s112-full-20260716/inputs/
```

Runtime for every task:

```text
MODEL: gpt-5.6-sol
REASONING_EFFORT: max
SERVICE_TIER: unset
SUBAGENTS: forbidden
```

Run the five task wrappers in numeric order with one Agent 1 session for Tasks
1-3 and a fresh Agent 2 session for Tasks 4-5. Generation is closed to the
listed input bundle and prior semantic outputs. V3 and V7.4 are used only after
completion for benchmark comparison.

Principal output:

```text
v7.5.0/a2/05-semantic-master-tr-v7.5.0.md
```
