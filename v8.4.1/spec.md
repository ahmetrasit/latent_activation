# V8.4.1 Controlled Orchestration Specification

V8.4.1 inherits the V8.4 cold workflow, agent isolation, input boundaries,
canonical settings, and Turn 1–4 semantics from `v8.4/spec.md`. The versioned
copies under `v8.4.1/prompts/` differ only in their version headings. Turn 5 is
the only semantic change.

For a full cold run, execute V8.4 Turns 1–4 with one persistent formation author
and one fresh synthesis author exactly as specified there. Give the same
synthesis author the V8.4.1 Turn 5 prompt:

```text
v8.4.1/prompts/05_postdraft_recomposition-v8.4.1.md
```

Write all newly produced files with `v8.4.1` in the filename. The final path is:

```text
a2/05-postdraft-recomposition-v8.4.1.md
```

The Turn 5 task must authorize only the raw bundle, scaffold, three formation
artifacts, and that author's own Turn 4 synthesis. It must prohibit prior
versions, comparisons, assessments, other surahs, documentation, and outside
material. Do not name known omissions or suggest a passage architecture.

For the controlled S103, S112, and S1 experiment, the formation prompts and
reservoirs are unchanged. Reuse the same frozen formation reservoirs used by
V8.4, but spawn a new cold synthesis author for each passage. That author must
write a fresh versioned Turn 4 using
`v8.4.1/prompts/04_compositional_semantic_synthesis-v8.4.1.md`, then receive Turn 5
as a follow-up in the same session. Do not reuse a V8.4 Turn 4 draft or author.

Use the canonical settings from `v8.4/spec.md`. If only
`collaboration.spawn_agent` is available, use `fork_turns: "none"` and report
that worker role, model, and reasoning effort were not selectable.

Assessment begins only after Turn 5. Compare fresh Turn 4 with Turn 5 before
opening V8.4, V8.3, V3, S1 reference, or any review. S96 remains prohibited
until the development passages establish production readiness.
