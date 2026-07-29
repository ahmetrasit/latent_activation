# Focus Trace

Workflow name: **Hermetic Focus Trace**.

This is a standalone one-call focus workflow. It reconstructs the useful part
of the old staged focus runs without putting new prompt, schema, or script
files under `v12/`.

See [`INTEGRATION.md`](INTEGRATION.md) for why this exists, how it differs from
`reader_m_ayah_walk.md`, and how `prose_generation` consumes it in Layer 2.

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

Agent orchestration:

- spawn one worker per focus ayah output;
- give each worker only the prompt, schema, and its assigned packet;
- set `agent_type: worker`, `model: gpt-5.6-sol`, `reasoning_effort: max`,
  and `fork_context: false`;
- each worker owns exactly one response path under
  `focus_trace/runs/sNNN/readers/<reader_id>/`;
- after writing JSON, each worker runs `jq -c` on its own output file before
  validation so stored reader artifacts are token-efficient;
- the reader call is hermetic: no follow-up reveal messages or staged context
  messages;
- if a worker is interrupted, validate any existing output before resuming or
  replacing it.

Validate a response:

```bash
jq -c . \
  focus_trace/runs/s100/readers/reader_a/100_1.focus_trace.json \
  > /tmp/100_1.focus_trace.compact.json && \
  mv /tmp/100_1.focus_trace.compact.json \
  focus_trace/runs/s100/readers/reader_a/100_1.focus_trace.json

python3 focus_trace/scripts/validate_focus_trace.py \
  focus_trace/runs/s100/packets/100_1.packet.json \
  focus_trace/runs/s100/readers/reader_a/100_1.focus_trace.json
```

The packet builder uses deterministic selection:

- root identity: QAC roots are resolved through
  `../quran-data/data/bridges/qac-furuq-v4-root-map.sqlite.gz`; when a QAC root
  maps to multiple Furuq roots, every mapped `root_id` and its branches are
  included;
- focus roots: every root in the focus ayah, first-seen order, full branch
  inventories;
- context roots: every root in the selected non-focus ayat, packet order, with
  `source_phrase_ar` for each occurrence;
- context branches: every accepted, non-contaminated branch ID in compact mode,
  always including `branch_image_ar`;
- branch citations: `branch_id` is root-local, so reader responses must cite it
  with `mapped_root_id`.
