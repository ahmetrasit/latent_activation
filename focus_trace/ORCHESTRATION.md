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

## Packet generation

Generate one packet per focus ayah with a whole-surah window:

```bash
python3 focus_trace/scripts/build_focus_trace_packet.py \
  --focus <S>:<A> \
  --surah-window \
  --output focus_trace/runs/s<S>/packets/<S>_<A>.packet.json
```

Validate each packet before spawning a worker:

```bash
python3 -B focus_trace/scripts/validate_focus_trace.py \
  focus_trace/runs/s<S>/packets/<S>_<A>.packet.json
```

The packet builder uses:

```text
../quran-data/data/bridges/qac-furuq-v4-root-map.sqlite.gz
```

Resource paths in packet provenance must stay repo-relative where possible.
Generated packets must not be written under `../quran-data`.

Branch policy for this HFT workflow:

- include all `contaminated = 'no'` branch rows;
- ignore `status` for inclusion, so both `accepted` and `review` rows are
  available;
- exclude every `contaminated = 'yes'` row.

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
- whole-surah boundary after S89: 82 jobs.

Prefer the whole-surah boundary unless there is a capacity reason to stop at
exactly 80.

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
