# Hermetic Focus Trace Integration

## Why This Workflow Exists

`reader_m_ayah_walk.md` for S100 showed the strongest version of the v12 reader
effect: a whole-surah walk with enough freedom to preserve surprise, abductive
movement, changed reading, and multiple coexisting readings. It did not behave
like an audit. It let a later ayah change how an earlier ayah was read, then
wrote that change in a compact reader voice.

The older per-ayah focus runs were also valuable for this reason. They showed an
ayah before its neighbors, then showed how later context activated or revised
latent readings. The problem was cost: a strict staged reveal needs repeated
coordinator turns and repeated context payloads. Running that for the whole
Quran is too expensive in both time and input tokens.

Hermetic Focus Trace is the cheaper substitute. It sends one sealed packet and
asks one `gpt-5.6-sol` max reader to reconstruct:

- a focus-only baseline;
- context-triggered deltas;
- surprising but still anchored outliers;
- discarded or unchanged material.

It is not a blind staged transcript. The packet contains the focus ayah and the
context at the same time, so the output must label itself as a reconstructed
trace. Its value is not experimental purity; its value is whether it recovers
the latent, surprising changed-readings that ordinary whole-surah readers tend
to collapse.

## What Gets Generated Here

The `focus_trace/` package owns generation. `quran-data` is frozen storage, not
a workspace for generation.

For each focus ayah, the builder deterministically creates:

- one packet under `focus_trace/runs/sNNN/packets/`;
- one or more reader outputs under `focus_trace/runs/sNNN/readers/<reader_id>/`;
- optional reports comparing the run to older readers such as `reader_m`.

The packet root policy is deterministic:

- QAC root identity is resolved through
  `../quran-data/data/bridges/qac-furuq-v4-root-map.sqlite.gz`;
- every focus root is included in first-seen order with full branch inventory;
- every non-focus context root is included in packet order;
- every non-focus root occurrence carries `source_phrase_ar`;
- every non-focus branch record carries `branch_image_ar`.

Split roots are not reduced to their dominant Furuq target. If one QAC root maps
to multiple Furuq `root_id` values, the packet includes every mapped target and
every non-contaminated branch inventory for those targets. Since
`branch_id` values are local to each Furuq root, reader responses cite
`mapped_root_id` with every `branch_id`. The bridge is stored in `quran-data`,
but generation remains here; `quran-data` is frozen data storage.

The model profile for reader generation is fixed:

```text
model: gpt-5.6-sol
reasoning_effort: max
```

## How Prose Generation Uses It

`prose_generation` consumes Hermetic Focus Trace as ayah-level evidence, not as
replacement prose and not as a strict staged focus run.

The intended bundle field is:

```text
v12_focus_trace_hermetic
```

That field carries the focus-only baseline, context deltas, and
`surprising_valid_outliers` for the requested ayah. Layer 2 should use it where
the latest ayah prompt previously wanted staged before/after material:

- `baseline_models` show what the focus ayah can yield on its own;
- `context_deltas` show what later context changes;
- `surprising_valid_outliers` preserve live, odd, branch-distant readings that a
  conservative synthesis might drop;
- `discarded_or_unchanged` is review context, not prose fuel.

If old staged `v12_reader_responses` and Hermetic Focus Trace both exist, the
old staged response is the truer reveal transcript. Hermetic Focus Trace remains
the cheaper reconstructed trace. The two should be labeled separately.

## Reader_m Comparison Standard

For S100, compare Hermetic Focus Trace against `reader_m_ayah_walk.md` on these
quality questions:

- Does it preserve genuine surprise rather than merely restating the surah
  theme?
- Does it expose changed readings, especially where later ayat alter 100:1-5?
- Does it keep multiple coexisting readings alive without forcing synthesis?
- Does it make abductive moves visible enough for commentary to render them?
- Does it recover the reader_m-level latent activations, or only the safe core?

Good enough does not mean better than `reader_m`. It means strong enough to feed
Layer 2 with surprising, grounded material at whole-Quran cost.
