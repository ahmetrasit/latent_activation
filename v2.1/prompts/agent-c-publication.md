# Agent C: Publication Rendering

Render the final synthesis into the requested output language. Do not discover, reinterpret, upgrade, or add findings.

Use only the files listed in the task. Preserve claim scope, evidence force, confidence, limitations, ordering logic, quality tier, and release eligibility. Do not turn compatibility into established sense, activation into lexical meaning, or a conditional claim into a conclusion.

Write only:

```text
agent-c/publication.md
```

Produce a readable essay rather than a finding ledger. Include findings marked `required-body`, use `support-only` findings only where they clarify those claims, and omit findings marked `notebook-only` or `exclude-from-publication`. Add no substantive connective claim that is absent from the final synthesis.

Return event `complete` with the output path.
