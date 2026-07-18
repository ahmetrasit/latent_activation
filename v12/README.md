# v12 Full-Context Latent Activation Workflow

v12 is the single-agent, full-context workflow.

The reader receives all ayat, roots, and branch inventories for the selected
window at once. It still works one fixed ayah at a time, appending findings as it
goes. After the ayah walk is complete, it revisits the whole file and adds
retrospective surprises plus a Turkish prose synthesis.

This is different from the older staged cold-reading protocol. v12 does not
reveal one ayah per turn and does not ask the reader to return staged JSON.

## Experimental Question

Given the complete local context, can a cold agent recover surprising latent
activation chains without seeing gold readings, older project outputs, other
agents' work, tafsir, or search results?

The output should make reading change visible:

1. which fixed ayah is being read;
2. which roots and branch IDs are doing work;
3. which surrounding ayat activate a branch or mechanism;
4. what changed in the reading;
5. what later ayat retroactively made surprising.

Multiple activated readings are allowed and expected. The reader must not
collapse them into a single interpretation.

## Separation Rules

- The reader may inspect only the v12 prompt and the assigned full-context
  packet.
- The packet contains raw Quran text, normalized Arabic text, QAC word
  order/morphology, and accepted, non-contaminated branch inventories from the
  Furuq v4 database. It does not include English translation.
- If the branch database has more than one accepted row for the same root and
  `branch_id`, the builder emits one branch entry for that ID and preserves the
  source rows under `variants`; the scalar image/scope fields are combined for
  reader convenience.
- Database origin labels (`furuq`, `quranic`) are provenance labels, not themes.
- The reader must not inspect `s1-bulgular-tr.md`, `attachments.tsv`, older
  version directories, previous v12 run outputs, staged reader outputs, tafsir,
  web search, or another agent's work.
- Discovery and rendering are separated inside the same output file: analytical
  ayah walk first, retrospective surprises second, Turkish prose synthesis last.

## Build a Full-Context Packet

Build one packet for the complete window:

```bash
python3 v12/scripts/build_full_context_packet.py \
  --surah 100 \
  --output v12/runs/s100/full_context_packet.json
```

You can also pass a custom ayah window with `--window`.

Before launching a reader, optionally inspect branch coverage:

```bash
python3 v12/scripts/check_full_context_coverage.py --surah 100
```

If a root has no accepted, non-contaminated branch inventory, the packet still
builds and records it in `missing_branch_inventories`. The reader can still
analyze the ayah, but it must not invent branch IDs for that root. Use
`--strict-branches` with the builder when you want missing branch inventories to
fail the run.

Validate that the packet is internally consistent and still matches the resource
hashes recorded at build time:

```bash
python3 v12/scripts/validate_full_context_packet.py \
  v12/runs/s100/full_context_packet.json
```

## Run One Agent

Give a fresh agent only these files:

- `v12/prompts/reader.md`
- the assigned `full_context_packet.json`

Tell the agent to write one output file, for example:

```text
v12/runs/s100/full_context_control/reader_a_ayah_walk.md
```

The reader must append sections in this order:

1. `100:1` analytical findings;
2. `100:2` analytical findings;
3. continue through the final ayah;
4. revisit every ayah and add retrospective surprises;
5. add `Turkish Prose Synthesis`, ayah by ayah.

Do not ask the agent for separate turns per ayah. The agent has all material
from the start and manages the sequential writing discipline itself.

## Freeze the Run

After the agent finishes, hash the prompt, packet, and output:

```bash
python3 v12/scripts/freeze_full_context_run.py \
  --packet v12/runs/s100/full_context_packet.json \
  --prompt v12/prompts/reader.md \
  --output-file v12/runs/s100/full_context_control/reader_a_ayah_walk.md \
  --reader-id reader_a \
  --freeze v12/runs/s100/full_context_control/frozen_run.json
```

This makes later comparison auditable. Changing `v12/prompts/reader.md` creates
a new experimental treatment and requires fresh agents.

## Output Standard

The output is prose, not JSON. It should be compact but derivationally explicit.

Each ayah section should include:

- the fixed ayah reference and Arabic text;
- multiple activated readings, if present;
- root and branch evidence;
- surrounding ayat that activate the reading;
- the concrete change in reading.

The retrospective pass should add what became visible only after later ayat were
read. The Turkish prose section should render the findings, not introduce new
analysis.

## Adjudicate Frozen Runs

Run adjudication only after reader outputs are frozen. Give the adjudicator only:

- `v12/prompts/adjudicator.md`;
- anonymized copies or labels for the reader Markdown outputs;
- the matching reader `frozen_run.json` files.

Ask it to write a report such as:

```text
v12/runs/s100/adjudication/report.md
```

Then freeze the report:

```bash
python3 v12/scripts/freeze_adjudication_report.py \
  --adjudicator-prompt v12/prompts/adjudicator.md \
  --report v12/runs/s100/adjudication/report.md \
  --reader-runs v12/runs/s100/full_context_control/frozen_run.json \
  --freeze v12/runs/s100/adjudication/frozen_report.json
```

Do not compare to a gold or human reading until after this adjudication report is
frozen.

## Legacy Scripts

The old staged packet/response scripts are retained for comparison with earlier
runs:

- `v12/scripts/build_packets.py`
- `v12/scripts/validate_packet_series.py`
- `v12/scripts/validate_response.py`
- `v12/scripts/freeze_run.py`

They are not the default v12 workflow.
