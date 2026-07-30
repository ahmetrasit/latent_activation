# Hermetic Focus Trace Orchestration

Status: active HFT reader-generation runbook.

This document is the normative orchestration spec for Hermetic Focus Trace
reader generation. Do not use `_status/v12_cross_run/ORCHESTRATION.md` for this
workflow; that file governs the older v12 Turkish publication/finalization
pipeline.

## Workflow boundary

Hermetic Focus Trace is not the old v12 publication workflow. It does not run
baseline authors, whole-surah publishers, anchor repair agents, publication
finalizers, or raw finding ledgers.

One HFT job is one focus ayah:

```text
prompt + schema + one packet -> one focus-trace response JSON
```

Each worker owns exactly one output file. Do not give one worker a whole surah
or a batch of ayat.

## Required reader inputs

Each worker receives only these three inputs:

- `focus_trace/prompts/focus_trace_hermetic.md`
- `focus_trace/schemas/focus-trace-response.schema.json`
- exactly one assigned packet, for example
  `focus_trace/runs/s89/packets/89_28.packet.json`

Do not include source excerpts, old reader outputs, prose outputs, tafsir, gold
readings, previous agent results, coordinator commentary, or broad repo context.
If a worker needs to resume, resend the same three paths.

## Required reader output

Default output path:

```text
focus_trace/runs/s<S>/readers/reader_hft_a/<S>_<A>.focus_trace.json
```

Example:

```text
focus_trace/runs/s89/readers/reader_hft_a/89_28.focus_trace.json
```

The response protocol must be:

```text
focus-trace-hermetic-response-v4
```

The stored JSON must be compacted with `jq -c` before validation.

## Agent profile

For Codex multi-agent runs:

```text
agent_type: worker
model: gpt-5.6-sol
reasoning_effort: max
fork_context: false
```

Do not set a `service_tier` override. Use the default service tier.

If the exact model profile is unavailable, stop rather than silently using a
fallback model or lower reasoning setting.

## Worker assignment template

Use this template for each ayah, substituting `S`, `A`, and the paths:

```text
Work in the `latent_activation` repository root.

Read only:
- focus_trace/prompts/focus_trace_hermetic.md
- focus_trace/schemas/focus-trace-response.schema.json
- focus_trace/runs/s<S>/packets/<S>_<A>.packet.json

Generate focus ayah <S>:<A> only. Write valid JSON to:
focus_trace/runs/s<S>/readers/reader_hft_a/<S>_<A>.focus_trace.json

Use response protocol focus-trace-hermetic-response-v4. Preserve surprise,
latent activation, changed readings, abductive reasoning, and multiple
coexisting readings. Do not behave as a conservative audit reader.

Every branch citation must include `source_ref`, `root`,
`source_word_indices`, `mapped_root_id`, `branch_id`, and `role`. Do not repeat
`source_phrase_ar`, `branch_image_ar`, or `mapped_root_norm` in v4 outputs;
these resolve from the packet.

If a packet lists a root under `missing_branch_inventories`, you may use that
root only as a structural cue. Do not invent `mapped_root_id` or `branch_id`
for it.

Compact the stored JSON before validation:
jq -c . \
  focus_trace/runs/s<S>/readers/reader_hft_a/<S>_<A>.focus_trace.json \
  > /tmp/<S>_<A>.focus_trace.compact.json && \
  mv /tmp/<S>_<A>.focus_trace.compact.json \
  focus_trace/runs/s<S>/readers/reader_hft_a/<S>_<A>.focus_trace.json

Validate:
python3 -B focus_trace/scripts/validate_focus_trace.py \
  focus_trace/runs/s<S>/packets/<S>_<A>.packet.json \
  focus_trace/runs/s<S>/readers/reader_hft_a/<S>_<A>.focus_trace.json

Do not edit any other file.
```

## Rootless focus ayat

Some ayat exist in the Quran text but have no QAC-rooted morphemes. These
packets mark the focus ayah with:

```text
rootless: true
root_occurrences: []
```

Do not skip these jobs. For a rootless focus ayah, add this heads-up to the
worker assignment:

```text
The focus ayah is rootless in this packet: QAC supplies no rooted morphemes for
the focus words. Still analyze the focus ayah within the given packet context,
using ordinary model knowledge of the focus words where needed. Do not fabricate
root, mapped_root_id, or branch_id citations for the rootless focus words.
Set top-level `rootless_focus` to `true` in the response. Baseline
activation_trace may be empty only for this rootless focus case. Any non-empty
branch citation must still resolve to a branch actually present in the packet.
```

Rootless context ayat are retained as text-only context. They may inform the
reader's prose analysis, but they cannot by themselves supply `trigger_roots` or
branch-cited activation trace entries.

## Pericope-based packet generation

Generate one packet per focus ayah with a pericope window, not a whole-surah
window. The normative pericope inventory is:

```text
../quran-data/data/analysis/channels/network-v3/pericopes/surah_pericopes.jsonl
```

Each JSONL row supplies:

```text
surah, pericope, ayah_from, ayah_to, label
```

Treat each pericope as the packet window for every focus ayah inside that
pericope. In other words, if S2 has sixteen reference pericopes, S2 is not one
reader window; each reference pericope is handled as its own local window.

For each focus ayah `<S>:<A>`, expand the containing pericope range into an
ordered ayah-ref list and generate:

```bash
python3 focus_trace/scripts/build_pericope_focus_trace_packet.py \
  --focus <S>:<A> \
  --window <S>:<FROM>,<S>:<FROM+1>,...,<S>:<TO> \
  --output focus_trace/runs/s<S>/packets/<S>_<A>.packet.json
```

Do not use `--surah-window` for pericope-scoped production runs.

Rootless ayat in a pericope are expected and are not missing-data errors. Keep
them in the packet when the packet format supports text-only/rootless ayat, and
follow the rootless-focus instructions above for rootless focus jobs. Do not
invent roots or branch citations for rootless focus words.

Validate each packet before spawning a worker:

```bash
python3 -B focus_trace/scripts/validate_focus_trace.py \
  focus_trace/runs/s<S>/packets/<S>_<A>.packet.json
```

The packet builder uses:

```text
../quran-data/data/bridges/qac-furuq-v4-root-map.sqlite.gz
```

Generated packets must not be written under `../quran-data`.

Pericope source rows, resource hashes, packet-size measurements, and other
audit/provenance details are recorded in coordinator reports, not in lean reader
packets.

Branch policy for this HFT workflow:

- include all `contaminated = 'no'` branch rows;
- ignore `status` for inclusion, so both `accepted` and `review` rows are
  available;
- exclude every `contaminated = 'yes'` row.

### Lean pericope packet schema

Pericope-scoped production packets use the lean schema:

```text
focus-trace-pericope-lean-v1
```

The lean packet keeps only information needed by the Arabic
semantic/linguistic reader task. Audit, provenance, ranking-method, resource
hash, English, and debug fields are excluded from reader packets and belong in
coordinator reports when needed.

Top-level packet fields:

```text
protocol, focus_ref, window, context_order, ayah_count,
focus_ayah, context_ayat, surah_text,
focus_branch_inventories, context_root_cues, remote_orientation
```

Text policy:

- keep original Arabic `text_ar`;
- remove `text_norm_ar` from ayah records and full-surah text;
- keep root morphology on `focus_ayah` and `context_ayat`;
- keep full-surah Arabic text as `{ref, text_ar}` only.

Branch inventory policy:

- keep no English fields;
- keep no source paths, variants, branch ranks, dominance flags, occurrence
  totals, mapping diagnostics, or full root-mapping objects;
- because `branch_id` is local to a mapped Furuq root, every branch inventory
  must preserve compact mapped-target identity;
- group branches under mapped targets instead of repeating mapped identity on
  every branch.

Focus branch shape:

```json
{
  "root": "ق و ل",
  "source_phrases": [{"source_phrase_ar": "..."}],
  "targets": [
    {
      "mapped_root_id": "root_001272",
      "mapped_root_norm": "ق و ل",
      "branches": [
        {
          "branch_id": "B001",
          "branch_image_ar": "...",
          "scope_ar": "..."
        }
      ]
    }
  ]
}
```

Context and remote branch shapes are the same target grouping, but their branch
records keep only:

```text
branch_id, branch_image_ar
```

Context-root policy:

- omit context `source_phrases`; the retained `context_ayat.root_occurrences`
  are the authoritative occurrence/source-word record;
- omit context cue records whose root already appears in
  `focus_branch_inventories`; those context occurrences still remain in
  `context_ayat.root_occurrences`, and their branch inventory resolves through
  the focus inventory;
- a reader may use focus inventory branches for same-root context activations
  when the source occurrence is present in `context_ayat.root_occurrences`.

Remote orientation policy:

- remote material is orientation-only and not branch-citable;
- keep one section-level marker:

```json
{"citable": false}
```

- keep `refs`, the same-surah ayat for which extra orientation/root material is
  supplied;
- every remote root cue must keep `source_refs`, so the reader can see which
  remote ayat anchor that root cue;
- strip all remote ranking, method, selection evidence, labels, scores, and
  reader-policy prose.

## Oversized pericope fragmentation

Use reference pericopes first. Fragment only when the generated packets for a
reference pericope prove too large.

Generation-time size policy:

1. Generate or simulate every focus packet for the reference pericope.
2. Measure the compact JSON packet size after generation.
3. If every packet in that reference pericope is `<= 500 KiB`, keep the
   reference pericope unchanged.
4. If any packet in that reference pericope is `> 500 KiB`, fragment that
   reference pericope into smaller contiguous semantic windows and regenerate
   only that pericope's packets from the fragments.
5. Re-measure the fragmented packets. Continue fragmenting only the windows
   that still produce packets over `500 KiB`.

Fragmentation rules:

- preserve the reference pericope as the parent boundary; never pull ayat from
  outside the source pericope merely to reduce size;
- prefer semantic discourse boundaries over fixed-size chopping;
- keep fragments contiguous, ordered, and non-overlapping;
- cover every ayah from the parent pericope exactly once, except for any
  rootless/text-only handling required by the packet format;
- record both the parent reference pericope and the fragment range in packet
  provenance;
- if a single-focus packet remains over `500 KiB`, report it as intrinsically
  oversized under the current packet schema rather than dropping branch
  inventory or weakening validation.

For S2, this policy means the first reference pericope `2:1-20` can remain
whole, while later reference pericopes should be fragmented only because their
measured packets exceed `500 KiB`. Fragmenting should follow local discourse
units such as Adam narrative, Israelite episodes, qiblah, fasting, hajj,
marriage/divorce, spending/usury/debt, and final creed, not arbitrary equal
chunks.

## S2-S79 Packet Scope

For the current S2-S79 package-building pass, use lean canonical pericope
packets only for these surahs:

```text
S2-S12,
S14-S30,
S33-S34,
S36-S43,
S51,
S54,
S56
```

Compact range form:

```text
2-12,14-30,33-34,36-43,51,54,56
```

Agents can identify these as pericope-based because their packet windows must
come from:

```text
../quran-data/data/analysis/channels/network-v3/pericopes/surah_pericopes.jsonl
```

and their generation report should record:

```text
window_mode: pericope
packet_schema: pericope-lean
fragment_dense_pericopes: false
```

The following S2-S79 surahs are whole-surah lean packets, not pericope packets:

```text
S13, S31, S32, S35, S44-S50,
S52-S53,
S55,
S57-S79 except S56
```

Do not infer packet scope only from surah number. Check this section first, then
check the generation report for the packet set being used.

## Current production queue

Current prepared scope:

```text
S1 + S87-S114
```

Total packet inputs:

```text
295 ayat
```

If preserving already completed S100 reader outputs, remaining new reader jobs:

```text
284 ayat
```

Queue order:

1. S1
2. S87
3. S88
4. S89
5. continue through S114

Within each surah, process ayat in numeric ayah order.

For an approximately 80-job first batch:

- exact 80th item: `89:28`;
- surah boundary after S89: 82 jobs.

Prefer the surah boundary unless there is a capacity reason to stop at exactly
80. This is a queue boundary only; packet windows are still pericope-scoped.

## Post-worker validation

After workers finish:

1. Confirm each expected output file exists.
2. If a file exists, validate it before considering respawn.
3. Compact each JSON with `jq -c` if the worker did not already do it.
4. Validate each response against its packet:

```bash
python3 -B focus_trace/scripts/validate_focus_trace.py \
  focus_trace/runs/s<S>/packets/<S>_<A>.packet.json \
  focus_trace/runs/s<S>/readers/reader_hft_a/<S>_<A>.focus_trace.json
```

If validation fails, fix by resuming/replacing the worker for that ayah. Do not
hand-edit generated reader JSON except for mechanical JSON compaction.

## Retired raw-ledger workflow

Do not build a raw focus-trace ledger as part of normal HFT orchestration. That
prototype is archived under:

```text
archive/focus_trace_raw_ledger/
```

The preferred surah-level consolidation input is downstream ayah prose, after
`prose_generation` has consumed the validated HFT reader outputs. Use prose
outputs to discover surah-wide channels, repeated mechanisms, ayah-specific
developments, and missing connective tissue.

## Downstream prose and surah consolidation

After validated reader outputs are available, `prose_generation` consumes them
as ayah-level evidence under:

```text
v12_focus_trace_hermetic
```

Surah-wide consolidation should happen after ayah prose generation, using the
ayah prose outputs as the primary substrate. HFT reader JSON remains the
evidence source for validation and debugging, not the default surah-level
pattern-discovery payload.
