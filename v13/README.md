# v13 Dynamic Retrieval Latent Activation Workflow

v13 is the dynamic-retrieval version of v12.

The reader behavior stays the same: one cold agent works one fixed ayah at a
time, preserves multiple activated readings, avoids disambiguation, writes an
ayah-by-ayah analytical file, then performs a retrospective surprise pass. The
change is how evidence is delivered. Instead of giving the whole branch package
up front, the reader retrieves deterministic five-ayah focus windows on demand.

## Why v13 exists

v12 full-context packets are excellent for auditability, but they can front-load
large branch inventories. For long runs, v13 lets the reader add unseen ayat and
root branches gradually:

```text
current focus ayah
  -> retrieve focus ±2 ayat
  -> return only newly unseen ayat and branch inventories
  -> cache what has been seen
  -> move to next ayah
```

This keeps retrieval mechanical while avoiding semantic query decisions by the
reader.

## Non-Goals

- No agent-selected semantic search.
- No raw DB/QAC browsing by the reader.
- No staged reveal of hidden answers.
- No one-turn-per-ayah orchestration by the coordinator.
- No forced disambiguation.
- No keyword theme catalog.
- No gold-reading comparison during discovery.

## Retrieval Rule

For ayah-attached/app-facing runs, the default local context is five ayat:

- the fixed ayah;
- up to two ayat before it;
- up to two ayat after it;
- clipped at surah or assigned-run boundaries.

The reader must use only:

```bash
python3 v13/scripts/retrieve_window.py
```

Retrieval commands that share a state file must be run sequentially. Do not run
parallel retrievals against the same `dynamic_state.json`.

The retrieval script uses the same resource semantics as v12 packet generation:

- QAC Arabic text, normalized text, word order/morphology, and root occurrences;
- accepted, non-contaminated Furuq v4 branch inventories;
- duplicate branch-ID merging with source variants preserved;
- explicit missing-branch records;
- synthetic basmalah as ayah `0`, except S9;
- S1 basmalah moved to `1:0`, avoiding duplication of `1:1`;
- source resource hashes.

## Key Anchoring Rule

Surrounding ayat may activate, sharpen, correct, or retrospectively change a
reading, but every retained reading must remain anchored to a word, root, form,
or construction in the fixed ayah. Do not promote a surrounding-ayah theme into
the fixed ayah unless that attachment is visible.

## Preserving Later Out-of-Window Surprises

v13 must preserve an important v12 behavior: a later ayah outside an earlier
five-ayah window may still change the reading of that earlier ayah.

The solution is a final retrospective sweep. After the first ayah-by-ayah pass,
the reader runs the retriever once with `--retrospective-sweep`. This makes the
complete selected run window available through the same deterministic cache. The
reader then revisits every ayah and records later out-of-window surprises only
when they attach back to the fixed ayah.

## Minimal Run

Create a run directory and retrieve the first focus window:

```bash
python3 v13/scripts/retrieve_window.py \
  --surah 100 \
  --focus 100:1 \
  --state v13/runs/s100/dynamic_state.json \
  --output v13/runs/s100/retrieval/100_1.json
```

Then retrieve the next focus:

```bash
python3 v13/scripts/retrieve_window.py \
  --surah 100 \
  --focus 100:2 \
  --state v13/runs/s100/dynamic_state.json \
  --output v13/runs/s100/retrieval/100_2.json
```

The second packet returns the active five-ayah window, but only newly unseen
root branch inventories are included under `new_branch_inventories`. Previously
seen roots are listed under `cached_roots`; their branch details are recovered
from earlier retrieval packets in the same run.

After all ayat are processed:

```bash
python3 v13/scripts/retrieve_window.py \
  --surah 100 \
  --focus 100:1 \
  --retrospective-sweep \
  --state v13/runs/s100/dynamic_state.json \
  --output v13/runs/s100/retrieval/retrospective_sweep.json
```

The focus supplied to the retrospective sweep is only a required run anchor; the
active window becomes the complete selected run window.

## Packet Fields

Each retrieval packet uses:

```text
protocol: v13-dynamic-retrieval-packet-v1
mode: focus | retrospective_sweep
focus_ref
radius
active_window
active_ayat
new_ayah_refs
active_roots
new_roots
cached_roots
cached_available_roots
cached_missing_roots
new_branch_inventories
new_missing_branch_inventories
state_before
state_after
provenance
```

The state file uses:

```text
protocol: v13-dynamic-retrieval-state-v1
selected_window
radius
seen_ayat
seen_roots
available_roots
missing_roots
retrievals
provenance
```

The state file is part of the audit trail. Do not hand-edit it.

## Token Implication

Naive dynamic retrieval can be worse than v12 if each focus resends all branches
for its five-ayah window. v13 avoids that by sending only branch inventories for
newly unseen roots. With sequential ayah processing, total branch-token cost
approaches the union of roots encountered in the selected run, not five repeated
copies per ayah.

The reader still accumulates context over time. For long runs, the practical
token discipline is:

- keep only the current focus packet and concise run memory in immediate
  context;
- recover older branch details from earlier retrieval packets when needed;
- use the state file as the retrieval log;
- reserve full-run integration for the retrospective sweep.

## Reader Prompt

Give the reader:

```text
v13/prompts/reader.md
```

and the concrete run target, for example:

```text
surah: 100
state: v13/runs/s100/dynamic_state.json
retrieval directory: v13/runs/s100/retrieval
analytical output: v13/runs/s100/reader_a_ayah_walk.md
```

The reader should run retrieval commands itself. It must not write scripts or
query raw resources.
