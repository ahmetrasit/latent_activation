# S112 V7.4 Composite Run

This run binds the prepared S112 input bundle to the frozen composite:

```text
semantic component:  V7.4.0 Tasks 1-5
rendering component: V7.4.1 Tasks 6-8
passage id:          112
```

Input root:

```text
v3/run/s112-full-20260716/inputs/
```

Runtime for every task:

```text
MODEL: gpt-5.6-sol
REASONING_EFFORT: max
SERVICE_TIER: unset
SUBAGENTS: forbidden
```

Run the task wrappers in numeric order while preserving the three native
session boundaries defined in `v7/01_composite_run_spec.md`.

Principal outputs:

```text
v7.4.0/a2/05-semantic-master-tr-v7.4.0.md
v7.4.1/112-publication-tr-v7.4.1.md
```
