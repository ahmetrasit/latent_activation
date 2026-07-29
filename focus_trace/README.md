# Focus Trace

Workflow name: **Hermetic Focus Trace**.

This is a standalone one-call focus workflow. It reconstructs the useful part
of the old staged focus runs without putting new prompt, schema, or script
files under `v12/`.

It is not a strict blind staged transcript. The reader receives one sealed
packet, first writes a focus-only baseline, then records context-triggered
changes. The prompt is discovery-first: it asks for surprise, latent
activation, changed reading, abductive moves, and multiple coexisting readings.
Odd but anchored activations should be carried under
`surprising_valid_outliers`, not discarded just because they are exploratory.

Build a whole-surah packet for `100:1`:

```bash
python3 focus_trace/scripts/build_focus_trace_packet.py \
  --focus 100:1 \
  --surah-window \
  --output focus_trace/runs/s100/packets/100_1.packet.json
```

For a fixed local window:

```bash
python3 focus_trace/scripts/build_focus_trace_packet.py \
  --focus 100:1 \
  --radius 5 \
  --output focus_trace/runs/s100/packets/100_1.radius5.packet.json
```

Validate a packet:

```bash
python3 focus_trace/scripts/validate_focus_trace.py \
  focus_trace/runs/s100/packets/100_1.packet.json
```

Reader inputs:

- `focus_trace/prompts/focus_trace_hermetic.md`
- `focus_trace/schemas/focus-trace-response.schema.json`
- the assigned packet JSON

Reader profile:

```text
model: gpt-5.6-sol
reasoning_effort: max
```

Validate a response:

```bash
python3 focus_trace/scripts/validate_focus_trace.py \
  focus_trace/runs/s100/packets/100_1.packet.json \
  focus_trace/runs/s100/readers/reader_a/100_1.focus_trace.json
```

The packet builder uses deterministic selection:

- focus roots: every root in the focus ayah, first-seen order, full branch
  inventories;
- context roots: every root in the selected non-focus ayat, packet order, with
  `source_phrase_ar` for each occurrence;
- context branches: every accepted, non-contaminated branch ID in compact mode,
  always including `branch_image_ar`.
