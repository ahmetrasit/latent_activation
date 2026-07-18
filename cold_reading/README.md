# Cold Reading Workflow

This workflow tests whether independent agents reconstruct the same surprising
reading of a focus ayah without seeing a gold interpretation, earlier project
outputs, or later verses prematurely.

It is designed for **abductive reading**, not conservative lexical matching.
Agents may build causal and functional models such as “trust enables reciprocal
action.” The important requirement is that the derivation remains visible:
which literal branches were selected, which structural cue connected them, and
which causal assumption the agent supplied.

## What counts as convergence

Two readings converge when they share the same:

1. dormant branch or branch family activated in the focus ayah;
2. contextual roots that trigger the activation;
3. functional or causal topology; and
4. resulting change in how the focus ayah is read.

Shared keywords alone do not count. “Social,” “trust,” and “cooperation,” for
example, are not a match unless the agents independently derive substantially
the same relation among them.

## Separation rules

- Reader agents receive only raw Quran text, QAC roots, and canonical accepted,
  non-contaminated branch inventories from the Furuq v4 database. Both database
  origin labels (`furuq` and `quranic`) are retained; neither is a thematic
  attachment.
- They must not inspect `s1-bulgular-tr.md`, `attachments.tsv`, old version
  directories, tafsir, search results, or another reader's output.
- The window is revealed cumulatively, one ayah at a time. A reader must answer
  each stage before receiving the next packet.
- Human/reference readings stay hidden until reader outputs have been frozen and
  independently clustered.
- Different agents should receive different left/right reveal orders when the
  focus lies inside the window. This exposes anchoring and order effects.

## Build packets

```bash
python3 cold_reading/scripts/build_packets.py \
  --focus 103:2 \
  --window 103:1,103:2,103:3 \
  --reveal-order 103:1,103:3 \
  --output cold_reading/runs/s103/focus_103_2/left_first
```

For a second reader, reverse the reveal order:

```bash
python3 cold_reading/scripts/build_packets.py \
  --focus 103:2 \
  --window 103:1,103:2,103:3 \
  --reveal-order 103:3,103:1 \
  --output cold_reading/runs/s103/focus_103_2/right_first
```

The builder produces one cumulative packet per reveal stage and a manifest with
resource hashes. Each packet contains every branch for every root revealed so
far; no branch is preselected for the agent.

Check that the series has no future ayah/root leakage and still matches the raw
resource hashes:

```bash
python3 cold_reading/scripts/validate_packet_series.py path/to/manifest.json
```

## Run readers

Give each fresh agent `prompts/reader.md` and only `stage_00_*.json`. Freeze its
response. Then give that same agent `stage_01_*.json`, freeze the response, and
continue until the manifest is exhausted.

At every stage the agent records distinct syntheses that actually changed under
the reveal. An unused dormant branch is not a finding: every retained model must
show a mechanism, a reading change, and a minimal contextual trigger. This keeps
the experiment focused without imposing a fixed number of activations.

Validate each frozen response against the packet before revealing the next one:

```bash
python3 cold_reading/scripts/validate_response.py \
  path/to/stage_packet.json path/to/reader_response.json
```

The validator rejects roots or branch IDs that the agent had not actually been
shown.

After every reader has completed every stage, freeze the exact prompt, schema,
packet manifest, and responses by hash:

```bash
python3 cold_reading/scripts/freeze_run.py \
  --packet-manifest path/to/manifest.json \
  --responses path/to/responses \
  --readers reader_a,reader_b,reader_c \
  --output path/to/frozen_run.json
```

Do this before blind adjudication. Changing the reader prompt creates a new
experimental treatment and requires fresh agents.

## Compare readers

After all final responses are frozen, remove agent identities and give the
outputs to a fresh adjudicator with `prompts/adjudicator.md`. The adjudicator
clusters mechanisms before seeing a human/reference reading. Only after that
clustering is frozen should a separate comparison ask whether a cluster matches
the human reading.

Three outcomes are all informative:

- **independent convergence**: multiple agents recover the same mechanism;
- **family resemblance**: agents select the same branches but construct
  different causal directions;
- **productive divergence**: agents find different, internally coherent latent
  activations.

The workflow does not treat divergence as failure because the working premise
allows multiple simultaneous thematic activations.

## Recommended experimental unit

Use one focus ayah per experiment. For each focus, run at least three cold
readers. Preserve these four records:

1. focus-only baseline;
2. each incremental reading change;
3. final surprise reading and derivation trace;
4. a minimal ablation: which revealed root or ayah would make the interpretation
   collapse if removed.

The ablation is not a random-corpus control. It asks what actually did causal
work inside the Quranic window.
