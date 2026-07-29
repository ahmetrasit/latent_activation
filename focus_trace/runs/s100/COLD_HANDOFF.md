# S100 Hermetic Focus Trace Cold Handoff

Purpose: continue the live S100 worth-it test without rediscovering the plan.

## Current Test

Run one Hermetic Focus Trace reader output per numbered ayah of S100.

Inputs:

- prompt: `focus_trace/prompts/focus_trace_hermetic.md`
- schema: `focus_trace/schemas/focus-trace-response.schema.json`
- packets: `focus_trace/runs/s100/packets/100_{1..11}.packet.json`

Required model profile:

```text
model: gpt-5.6-sol
reasoning_effort: max
```

Expected outputs:

```text
focus_trace/runs/s100/readers/reader_hft_a/100_1.focus_trace.json
focus_trace/runs/s100/readers/reader_hft_a/100_2.focus_trace.json
...
focus_trace/runs/s100/readers/reader_hft_a/100_11.focus_trace.json
```

If some files are missing, create only the missing files. Each model call should
receive exactly the prompt, schema, and its assigned packet. The method is
hermetic: do not send follow-up reveal messages.

## Spawn / Orchestration Contract

Spawn one worker per missing ayah output. Do not give one worker the whole
surah. Do not ask a worker to compare quality or rebuild bundles while it is
writing a focus response.

For Codex multi-agent runs, use:

```text
agent_type: worker
model: gpt-5.6-sol
reasoning_effort: max
fork_context: false
```

Worker ownership is one output file only:

```text
focus_trace/runs/s100/readers/reader_hft_a/{S}_{A}.focus_trace.json
```

Assignment template:

```text
Work in the `latent_activation` repository root.

Read:
- focus_trace/prompts/focus_trace_hermetic.md
- focus_trace/schemas/focus-trace-response.schema.json
- focus_trace/runs/s100/packets/{S}_{A}.packet.json

Generate focus ayah {S}:{A} only. Write valid JSON to:
focus_trace/runs/s100/readers/reader_hft_a/{S}_{A}.focus_trace.json

Use response protocol focus-trace-hermetic-response-v4. Preserve surprise,
latent activation, changed readings, abductive reasoning, and multiple
coexisting readings. Do not behave as a conservative audit reader. Every branch
citation must include `source_ref`, `root`, `source_word_indices`,
`mapped_root_id`, `branch_id`, and `role`. Do not repeat `source_phrase_ar`,
`branch_image_ar`, or `mapped_root_norm` in v4 outputs; these resolve from the
packet.

Compact the stored JSON before validation:
jq -c . \
  focus_trace/runs/s100/readers/reader_hft_a/{S}_{A}.focus_trace.json \
  > /tmp/{S}_{A}.focus_trace.compact.json && \
  mv /tmp/{S}_{A}.focus_trace.compact.json \
  focus_trace/runs/s100/readers/reader_hft_a/{S}_{A}.focus_trace.json

Validate:
python3 -B focus_trace/scripts/validate_focus_trace.py \
  focus_trace/runs/s100/packets/{S}_{A}.packet.json \
  focus_trace/runs/s100/readers/reader_hft_a/{S}_{A}.focus_trace.json

Do not edit any other file.
```

If an agent is interrupted or closed before writing its file, either resume it
and resend the same assignment or spawn a replacement for that ayah. Before
restarting an ayah, check whether its output file already exists; if it exists,
validate it instead of overwriting it.

## Validate Reader Outputs

From `../latent_activation`:

```bash
for i in 1 2 3 4 5 6 7 8 9 10 11; do
  python3 -B focus_trace/scripts/validate_focus_trace.py \
    focus_trace/runs/s100/packets/100_$i.packet.json \
    focus_trace/runs/s100/readers/reader_hft_a/100_$i.focus_trace.json
done
```

Every trace citation using a branch must include both `mapped_root_id` and
`branch_id`. This matters for split QAC roots:

- `ع د و`: `root_000993`, `root_000989`, `root_001058`
- `ث و ر`: `root_000210`, `root_000011`
- `ر ب ب`: `root_000532`, `root_000537`

## Rebuild S100 Bundles

From `../prose_generation` after reader JSON validates:

```bash
python3 -B scripts/build_bundle.py --surah 100 --out bundles/s100
```

Quick check:

```bash
jq '.coverage.v12_focus_trace_hermetic' bundles/s100/100_1.ayah.json
```

Expected after reader outputs exist:

- `packet_present: true`
- `present: true`
- reader count greater than zero

## Instantiate S100 Commentary Prompts

From `../prose_generation`:

```bash
python3 -B scripts/instantiate.py \
  --surah 100 \
  --layer ayah \
  --profile v2.5.6-sol-high \
  --language tr \
  --date 2026-07-29 \
  --out _commentary/inputs/s100-hft-test
```

Use `v2.5.6-sol-high` for the commentary test unless the user explicitly asks
for a different commentary profile. The focus trace reader itself remains
`gpt-5.6-sol` max.

## Compare Against Reader_M

Baseline file:

```text
focus_trace/runs/s100/READER_M_BASELINE.md
```

Primary comparator:

```text
../quran-data/data/analysis/ayah-activation/v12-tr/s100/full_context_control/reader_m_ayah_walk.md
```

Judge the new focus outputs on:

- surprise;
- latent activation;
- changed readings;
- abductive reasoning;
- multiple coexisting readings;
- whether Layer 2 prose can use the material without flattening it.

The test does not require beating `reader_m` as prose. It needs to show that
Hermetic Focus Trace gives enough surprising, anchored ayah-level material to
justify whole-Quran generation.

## Remaining Final Deliverables

After the commentary test runs, write a short findings report in this S100 run
directory. It should answer:

- Is Hermetic Focus Trace worth continuing?
- Which ayat match or trail `reader_m`?
- Are surprise/latent readings substantially better than ordinary whole-surah
  readers?
- Is the method production-ready for deep lexical quality, not administrative
  audit quality?

Then commit and push the relevant `latent_activation` and `prose_generation`
changes. Do not commit the frozen `quran-data` bridge unless the user explicitly
asks.
