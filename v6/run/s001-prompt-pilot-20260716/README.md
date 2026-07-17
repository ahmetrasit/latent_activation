# S1 V6 Prompt Pilot

This run reuses the frozen evidence from:

```text
v3/run/s001-full-20260716/
```

Run the task files in numeric order.

- Tasks 01-04 use the same Agent 1 session.
- Task 05 uses a fresh Agent 2 session.
- Tasks 06-07 use the same fresh Agent 3 session.
- Every agent uses `gpt-5.6-sol` at maximum reasoning depth.
- Leave service tier unset and do not allow subagents.

Expected outputs:

```text
a1/discovery.md
a1/discovery-resurrected.md
a1/discovery-integrated.md
a1/gold-synthesis.md
a2/narrative-architecture.md
a3/publication.md
a3/publication-audio.md
```

This pilot has no automated validation or grading step. Preserve the raw
outputs for blind comparison after all turns finish.
