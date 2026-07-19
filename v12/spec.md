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

All spawned v12 reader and adjudicator agents must use:

```text
model: gpt-5.6-sol
reasoning_effort: high
```

This is an orchestration requirement. The v12 scripts build, validate, and hash
files; they do not select or verify the model profile. Do not silently downgrade
the model or reasoning effort. If `gpt-5.6-sol` with high reasoning is
unavailable, stop and report the blocker instead of starting substitute agents.

When spawning a reader agent, explicitly instruct it not to write scripts,
helper programs, parsers, workflow files, or patches. The reader's only write
targets are the assigned analytical Markdown file and, after follow-up, the
assigned Turkish prose Markdown file.

## Inputs

The only required reader inputs are:

- `v12/prompts/reader.md`
- one `full_context_packet.json` built by
  `v12/scripts/build_full_context_packet.py`

The packet must include:

- ordered ayat in the selected window;
- Arabic text and normalized Arabic text;
- QAC root occurrences;
- accepted, non-contaminated branch inventories;
- explicit `missing_branch_inventories` records for roots without accepted,
  non-contaminated branch data;
- source resource hashes.

The packet must not include English translation. Primary and secondary readings
must be derived from Arabic text, QAC word order/morphology, and branch
inventories. Translation can be used only outside this cold-reading packet as a
human convenience layer, not as reader evidence.

For ayah-attached/app-facing runs, the default selected window is five ayat:
the fixed ayah, up to two ayat before it, and up to two ayat after it, clipped
at surah boundaries. Whole-surah packets remain valid for discovery/control runs,
but the reader must still write one fixed ayah at a time.

Key anchoring rule: surrounding ayat may activate, sharpen, correct, or
retrospectively change a reading, but every retained reading must remain anchored
to a word, root, form, or construction in the fixed ayah. A surrounding-ayah
theme that cannot be attached back to the fixed ayah must not be promoted into a
reading for that ayah.

For `--surah N` builds, the first packet ayah must be `{N}:0`, a synthetic
basmalah entry, except for S9. S9 is the only surah-level exception and starts
at `9:1`. The synthetic basmalah uses the Arabic text, normalized Arabic text,
QAC word order, root occurrences, surfaces, lemmas, and POS tags from the
canonical basmalah resource entry, and records that source in packet provenance.
Then the packet continues with the surah's ordinary ayat. For S1, the source
basmalah is moved to `1:0` so it is not duplicated as both `1:0` and `1:1`.

Missing branch inventories are represented explicitly and must not be filled in
by the reader.
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

After the analytical file is complete, send the same reader agent the canonical
Turkish prose follow-up defined in `v11/spec.md`, substituting only the concrete
output path. This is not part of the initial reader prompt:

```text
{output_path} = v12/runs/s103/full_context_control/103-0-3-butuncul-okuma.md
```

The Turkish prose must be written to a separate Markdown file in the same run
directory, for example:

```text
v12/runs/s103/full_context_control/103-0-3-butuncul-okuma.md
```

Do not append Turkish prose to the analytical ayah-walk file.

The Turkish prose file uses a constrained Markdown schema so scripts can parse
it while it remains readable:

```text
# {surah}:{ayah_start}-{ayah_end} Bütüncül Okuma
**{surah}:{ayah}.** {arabic_ayah_text} — Birincil okuma: {primary reading}. {secondary/surprise reading change} {{root branch; root branch; ...}}
```

Rules:

- exactly one title line;
- exactly one non-empty line per ayah in packet order;
- each ayah line starts with the bold ayah marker, then the Arabic ayah text,
- then ` — `, then one Turkish paragraph;
- the Turkish paragraph must start with the exact phrase `Birincil okuma:`;
- after the primary reading, the same paragraph explains how secondary
  activations change the primary reading in a surprising way;
- each paragraph ends with curly-braced root and branch evidence;
- no bullets, tables, extra sections, postscript, or analysis notes.

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

Runs that record a closest-available or fallback model profile are legacy controls
only. They must not be presented as conforming production v12 runs under this
spec.

Then spawn a fresh `gpt-5.6-sol` reader agent with `reasoning_effort: high` and give it:

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

Then send the canonical Turkish prose follow-up from `v11/spec.md` to the same
reader agent, substituting only the concrete output path for the separate
`100-0-11-butuncul-okuma.md` file in the same run directory, and require the
constrained Turkish Markdown schema defined above.

## Adjudication

Adjudication is optional unless the experiment has multiple independent v12
readers for the same packet. When adjudication is run, spawn a fresh
`gpt-5.6-sol` adjudicator agent with `reasoning_effort: high`.

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
- Turkish prose must follow the constrained one-line-per-ayah Markdown schema
  so downstream scripts can parse ayah id, Arabic text, prose, and branch
  evidence.
- Later comparison can use older staged runs, but staged runs are legacy
  controls, not the default v12 method.
