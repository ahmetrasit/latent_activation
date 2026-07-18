# v12 Spec

## Purpose

v12 tests full-context latent activation. A single cold agent receives all
material for an ayah window at once, then writes an ayah-by-ayah analysis and
retrospective surprise pass. After that analytical pass is complete, the same
agent receives a follow-up message and writes Turkish user-facing prose to a
separate file.

## Non-Goals

- No staged reveal.
- No one-turn-per-ayah orchestration by the coordinator.
- No forced disambiguation.
- No keyword theme catalog.
- No gold-reading comparison during discovery.

## Agent Profile

All spawned v12 reader and adjudicator agents must use the `gpt 5.6 sol high`
profile.

This is an orchestration requirement. The v12 scripts build, validate, and hash
files; they do not select or verify the model profile. If the agent runtime does
not expose a literal `gpt 5.6 sol high` selector, the orchestrator must record
that limitation in the run notes and use the closest available high-effort
agent profile.

## Inputs

The only required reader inputs are:

- `v12/prompts/reader.md`
- one `full_context_packet.json` built by
  `v12/scripts/build_full_context_packet.py`

The packet must include:

- ordered ayat in the selected window;
- Arabic text and normalized Arabic text;
- English translation;
- QAC root occurrences;
- accepted, non-contaminated branch inventories;
- explicit `missing_branch_inventories` records for roots without accepted,
  non-contaminated branch data;
- source resource hashes.

Missing translations are represented as empty strings. Missing branch
inventories are represented explicitly and must not be filled in by the reader.
When the branch resource reuses a `branch_id` for multiple accepted rows of the
same root, the packet must not emit duplicate branch IDs. It should merge those
rows into one branch entry, keep combined scalar image/scope fields, and preserve
the original rows under that branch entry's `variants` list.

## Reader Output

The reader first writes one analytical Markdown file. It appends as it works.

Required order:

1. ayah-by-ayah analytical findings in packet order;
2. retrospective surprises under each ayah.

The analysis must preserve multiple activated readings. A reading is retained
only when it has a visible mechanism and a change in reading, not merely a
shared keyword.

## Turkish Prose Follow-Up

After the analytical file is complete, send the same reader agent this follow-up
message. This is not part of the initial reader prompt:

```text
now can you write me a turkish user-facing prose that coherently explains what is the primary reading, and what the secondary readings change the primary reading in a suprising way? at the end of each paragraph, list relevant roots and branches inside curly brackets that created this reading. Write it to {surah}-{ayah_start}-{ayah_end}-butuncul-okuma.md in the run directory, for example 103-1-11-butuncul-okuma.md
```

The Turkish prose must be written to a separate Markdown file in the same run
directory, for example:

```text
v12/runs/s103/full_context_control/103-1-3-butuncul-okuma.md
```

Do not append Turkish prose to the analytical ayah-walk file.

## Minimal Run

```bash
python3 v12/scripts/build_full_context_packet.py \
  --surah 100 \
  --output v12/runs/s100/full_context_packet.json

python3 v12/scripts/validate_full_context_packet.py \
  v12/runs/s100/full_context_packet.json
```

Optional coverage preflight:

```bash
python3 v12/scripts/check_full_context_coverage.py --surah 100
```

Then spawn a fresh `gpt 5.6 sol high` reader agent and give it:

```text
v12/prompts/reader.md
v12/runs/s100/full_context_packet.json
```

Ask it to write:

```text
v12/runs/s100/full_context_control/reader_a_ayah_walk.md
```

After completion:

```bash
python3 v12/scripts/freeze_full_context_run.py \
  --packet v12/runs/s100/full_context_packet.json \
  --prompt v12/prompts/reader.md \
  --output-file v12/runs/s100/full_context_control/reader_a_ayah_walk.md \
  --reader-id reader_a \
  --freeze v12/runs/s100/full_context_control/frozen_run.json
```

Then send the Turkish prose follow-up to the same reader agent and ask it to
write the separate `100-1-11-butuncul-okuma.md` file in the same run directory.

## Adjudication

Adjudication is optional unless the experiment has multiple independent v12
readers for the same packet. When adjudication is run, spawn a fresh
`gpt 5.6 sol high` adjudicator agent.

Give the adjudicator only:

- `v12/prompts/adjudicator.md`;
- anonymized reader outputs;
- the matching reader `frozen_run.json` files.

The adjudicator writes a Markdown report and must not see a gold or human
reference reading. Freeze the report:

```bash
python3 v12/scripts/freeze_adjudication_report.py \
  --adjudicator-prompt v12/prompts/adjudicator.md \
  --report v12/runs/s100/adjudication/report.md \
  --reader-runs v12/runs/s100/full_context_control/frozen_run.json \
  --freeze v12/runs/s100/adjudication/frozen_report.json
```

## Audit Rules

- A changed prompt means a new treatment.
- A frozen run hashes the packet, prompt, and output file.
- Turkish prose is downstream rendering produced by the same reader agent via
  follow-up message. It must be written to a separate file and must not replace
  or rewrite the analytical findings.
- Later comparison can use older staged runs, but staged runs are legacy
  controls, not the default v12 method.
