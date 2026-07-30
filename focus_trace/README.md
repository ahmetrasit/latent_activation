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

## Prepared S2-S79 Inputs

All S2-S79 focus-ayah input bundles are ready under
`focus_trace/runs/s<S>/packets/` using packet protocol
`focus-trace-pericope-lean-v1`.

The prepared set contains 5,751 packet inputs:

- 4,466 ayat in canonical pericope windows;
- 1,285 ayat in whole-surah windows.

Pericope-based surahs:

```text
S2-S12, S14-S30, S33-S34, S36-S43, S51, S54, S56
```

Compact range form:

```text
2-12,14-30,33-34,36-43,51,54,56
```

Whole-surah-window surahs:

```text
S13, S31-S32, S35, S44-S50, S52-S53, S55, S57-S79
```

Pericope windows come from
`../quran-data/data/analysis/channels/network-v3/pericopes/surah_pericopes.jsonl`.
Do not infer packet scope from surah number alone; use the lists above and the
generation reports:

- `focus_trace/runs/pericope_lean_remaining_canonical_packet_size_report.json`
- `focus_trace/runs/surah_lean_s2_s79_packet_size_report.json`

## Building Packets

Build a lean packet for a fixed pericope/window:

```bash
python3 focus_trace/scripts/build_pericope_focus_trace_packet.py \
  --focus 2:1 \
  --window 2:1,2:2,2:3,2:4,2:5,2:6,2:7,2:8,2:9,2:10,2:11,2:12,2:13,2:14,2:15,2:16,2:17,2:18,2:19,2:20 \
  --output focus_trace/runs/s2/packets/2_1.packet.json
```

Build lean whole-surah-window packets only for surahs listed as whole-surah
scope above:

```bash
python3 focus_trace/scripts/generate_pericope_packets.py \
  --window-mode surah \
  --surah-list 13 \
  --overwrite \
  --validate \
  --report focus_trace/runs/surah_lean_s13_packet_size_report.json
```

Validate a packet:

```bash
python3 focus_trace/scripts/validate_focus_trace.py \
  focus_trace/runs/s2/packets/2_1.packet.json
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
  focus_trace/runs/s2/readers/reader_hft_a/2_1.focus_trace.json \
  > /tmp/2_1.focus_trace.compact.json && \
  mv /tmp/2_1.focus_trace.compact.json \
  focus_trace/runs/s2/readers/reader_hft_a/2_1.focus_trace.json

python3 focus_trace/scripts/validate_focus_trace.py \
  focus_trace/runs/s2/packets/2_1.packet.json \
  focus_trace/runs/s2/readers/reader_hft_a/2_1.focus_trace.json
```

The packet builder uses deterministic selection:

- root identity: QAC roots are resolved through
  `../quran-data/data/bridges/qac-furuq-v4-root-map.sqlite.gz`; when a QAC root
  maps to multiple Furuq roots, every mapped `root_id` and its branches are
  included;
- focus roots: every root in the focus ayah, first-seen order, full branch
  inventories, with `source_phrase_ar` retained only for the focus ayah;
- context ayat: original Arabic text plus root occurrences; no duplicate
  normalized Arabic text;
- context root cues: non-focus roots that are not already present in focus
  inventories, with compact Arabic branch inventories only;
- remote orientation: same-surah orientation-only refs and selected root cues,
  marked `citable: false`;
- branch citations: `branch_id` is root-local, so reader responses must cite it
  with `mapped_root_id`.

Lean reader packets exclude English fields, source paths, ranking/provenance
details, audit metadata, normalized-Arabic duplicates, and branch diagnostics.
Those belong in coordinator reports when needed.
