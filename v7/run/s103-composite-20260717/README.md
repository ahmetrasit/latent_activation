# S103 V7.4 Composite Run

This run binds the prepared S103 input bundle to the frozen composite:

```text
semantic component:  V7.4.0 Tasks 1-5
rendering component: V7.4.1 Tasks 6-8
passage id:          103
```

Input root:

```text
v3/run/s103-pilot-20260715/inputs/
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
v7.4.1/103-publication-tr-v7.4.1.md
```
