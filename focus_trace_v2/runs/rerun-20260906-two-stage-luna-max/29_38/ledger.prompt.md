Continue in this same conversation with the same sealed packet. Discovery is
complete; this is the reporting pass. No new evidence or target readings are
being supplied. Your discovery notes are a record of candidates, not an additional
evidentiary source. Use the original packet to verify the final citations.

Convert the notes into the v1 ledger specified below. Preserve each distinct
candidate's meaning and ID, including competing and exploratory readings. Use
the candidate's `id` as its `model_id` or `outlier_id`. Do not silently merge,
drop, rank down, or replace candidates, and do not start a new discovery round.
Use the existing fields to qualify interpretations without erasing their change
to the focus reading.

If a candidate cannot survive v1's anchoring or changed-reading requirements,
record it in `discarded_or_unchanged` as `ID: specific reason`. Every discovery ID
must occur exactly once, either as a retained finding or in such a withdrawal.
Do not invent a citation to retain a candidate. An unconventional but grounded
reading is not a reason for withdrawal. Put other uncertainties in `summary`.

Return only the final response JSON. The coordinator saves `response.json` and
performs formatting-only compaction; do not call tools or modify files yourself.
The following original v1 reporting sections govern this pass, with compaction
handled by the coordinator as stated above.

## Required Evidence Discipline

For every `activation_trace` entry, whether baseline, context delta, or outlier,
use exactly this compact resolvable citation shape:

- `source_ref`;
- `root`;
- `source_word_indices`;
- `mapped_root_id`;
- `branch_id`;
- `role`.

For context-triggered deltas, every non-focus citation must include the compact
resolvable citation key:

- `source_ref`;
- `root`;
- `source_word_indices`;
- `mapped_root_id`;
- `branch_id`;
- `role`, a concise sentence explaining the cited branch image's contribution
  to the mechanism.

Do not repeat `source_phrase_ar`, `branch_image_ar`, or `mapped_root_norm` in
the response. The validator and downstream loader resolve those from the packet
using `source_ref`, `root`, `source_word_indices`, `mapped_root_id`, and
`branch_id`. Use the exact `source_word_indices` supplied by the packet. If a
context root has no branch inventory, cite it only as a `structural_cues` item
rather than inventing a branch ID. In v4, a retained `context_delta` must still
include at least one branch-backed context citation in `activation_trace`;
branchless structural cues may support that delta but may not be its only
trigger.

QAC roots are resolved to Furuq root IDs before you receive the packet. If a QAC
root maps to multiple Furuq roots, all mapped roots and all non-contaminated
branch inventories are present. Branch IDs are local to a
Furuq root, so cite `mapped_root_id` with every `branch_id`. Do not collapse a
split root to the dominant target only. Non-dominant mapped roots are legitimate
activation material when they visibly change the focus reading.

If the packet protocol is `focus-trace-pericope-lean-v1`, branch inventories are
grouped under `targets` instead of repeating mapped identity on every branch.
Resolve each branch citation from `root -> targets[].mapped_root_id ->
branches[].branch_id`. In this lean schema, `context_ayat.root_occurrences` is
the authoritative source-occurrence record. A context occurrence whose root is
already present in `focus_branch_inventories` may use that focus inventory for
branch resolution even when that root is omitted from `context_root_cues`.
`remote_orientation` is not branch-citable when it says `citable: false`; use it
only to orient candidate readings, never as a citation source.

If a branch entry contains `variants`, the same packet branch ID represents
multiple non-contaminated source rows. You may cite the shared branch ID, but be clear
which image or scope is doing the work.

Whenever you infer that one element causes, enables, blocks, reveals, preserves,
or reverses another, distinguish the elements supplied by the packet from the
directional arrow supplied by you. Such moves are allowed. Hidden moves are not.
Use `reader_inference` for this distinction in each context delta. Keep it
short, but include: what the packet supplies, the reader-supplied assumption or
arrow, and any materially live alternative.

## Output

Write one JSON object conforming to:

```text
focus_trace/schemas/focus-trace-response.schema.json
```

The top-level `protocol` must be:

```text
focus-trace-hermetic-response-v4
```

Use this order:

1. `protocol`
2. `reader_id`
3. `focus_ref`
4. `trace_kind`
5. `baseline_models`
6. `context_deltas`
7. `surprising_valid_outliers`
8. optional `discarded_or_unchanged`
9. `summary`

For v4 compact output:

- omit baseline `status`; membership in `baseline_models` implies it;
- use one trace `role` field instead of separate `literal_contribution` and
  `assigned_role`; this must combine the branch image's literal contribution
  and its functional role in the mechanism;
- use one `reader_inference` string instead of `abductive_moves`;
- omit `trigger_refs` by default; if included, they must exactly match the
  non-focus citations in `activation_trace`;
- omit `minimal_triggers`, `ablation`, and `discarded_or_unchanged` unless a
  debug note materially changes confidence or status;
- for outliers, use one `containment` field instead of separate
  `why_surprising`, `why_still_valid`, and `rendering_caution`; it must state
  why the outlier is surprising, why it remains anchored or valid, and how
  downstream prose should qualify it.

Every `model_id` value must be unique across both `baseline_models` and
`context_deltas`. If a context delta revises a baseline model, use a related but
distinct ID rather than reusing the baseline ID.

For `surprising_valid_outliers`, record readings that are odd, branch-distant,
cross-domain, or likely to be lost in a conservative synthesis, while still
meeting the anchoring rule. These are not final interpretations. They are live
exploratory activations that downstream commentary may choose to render with
proper containment.

Keep fields concise and diagnostic. The goal is not a catalog of every branch;
the goal is to recover the surprising changed-reading trace that whole-surah
reader prose tends to collapse.

After writing valid JSON, compact the stored output with `jq -c` before final
validation. The compaction is formatting-only: it must not change any field or
value. If compacting fails, fix the JSON and compact again before validating.
