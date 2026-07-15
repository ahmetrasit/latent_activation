# Agent A: Targeted Revision

Continue as the same logical author of the draft. Revise the synthesis only where Agent B identified a material issue.

## Authority boundary

Use only the evidence inputs and work products listed in the task. Agent B's review is criticism, not evidence. Verify every proposed correction against the prepared inputs. Preserve the original source limitations and the distinction between local sense and passage activation.

## Revision method

1. Address every `REQUIRED CHANGE` in the review.
2. Recheck evidence only where the review identifies a concrete gap.
3. Keep stable finding IDs when the finding remains the same; add or remove a finding only when the substantive review requires it.
4. Preserve valid draft material outside the review's scope.
5. Ensure the final Markdown remains a coherent synthesis rather than a change log.

## Output

Write:

```text
agent-a/final/final-synthesis.jsonl
agent-a/final/final-synthesis.md
```

Use the same core JSONL shape and allowed values defined in `synthesis-finding.schema.json` and the original synthesis prompt. The Markdown file is the primary final synthesis.

Return event `complete` with the two output paths. Return `human_needed` for a genuine authority conflict or `evidence_blocked` when the required correction cannot be supported by the authorized evidence. Do not write adjudication records or closure files.
