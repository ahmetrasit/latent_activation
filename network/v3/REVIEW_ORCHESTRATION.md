# v3 Review Orchestration Prototype

This prototype runs first-pass blind candidate review after v3 generation.
Generation is already complete under `network/v3/experiments/corpus_neo_adaptive/`.

## Scope

Review one surah per agent run. Start with S001 as the pilot.

Build the review bundle:

```bash
python3 network/v3/build_review_bundle.py --surah-tag s###
```

The review agent receives only:

- `network/v3/experiments/corpus_neo_adaptive/s###/review_bundle.json`
- `network/v3/prompts/blind_candidate_review.md`

No other files are review inputs.

## Agent Launch Policy

When spawning review agents, do not set a priority tier or `service_tier`.
Leave service tier unset and let the agent runtime use its default scheduling.

## Pericope-scoped launch

Before spawning a review agent, check
`network/v3/pericopes/surah_pericopes.jsonl` for rows matching the target
surah. If rows exist, include those pericope boundaries in the agent's first
message. The pericope file is an orchestration input; the review agent should
still receive only the review bundle, the blind-review prompt, and the
pericope intervals copied into its task message.

Use this launch language, with the target intervals substituted:

```text
First pass: build pericope-local channels for these intervals:

- P1: AYAH_FROM-AYAH_TO
- P2: AYAH_FROM-AYAH_TO
...

Keep every parent/subchannel and its active ayah anchors within one interval;
do not form cross-pericope channels yet. Build tight local scenes, split
different senses or operations, and do not pack motifs for coverage. Retain
channels whose latent activation supports, materializes, reframes, or usefully
pressures the primary reading, not surface summary alone.
```

## Whole-surah lexical-surprise sweep

For any surah with defined pericopes, run a separate lexical-surprise recall
sweep after the pericope-local report is written and before cross-pericope
synthesis. The pericope file excludes very short surahs, so this staged sweep
does not apply when no pericope rows exist. Send the same agent this message:

```text
Freeze the pericope-local findings. Now run a separate whole-surah
lexical-surprise sweep for compact concrete clusters not yet represented, such
as source-attested practices, objects, tools, instruments, rites, games,
body/food/craft/animal/social micro-scenes, or other concrete motifs. Add one
only when its motifs form a complete scene and its activation supports,
materializes, reframes, or usefully pressures a primary surah reading; state
that effect in the synthesis. Prefer standalone subchannels. Do not make
generic domain buckets or add motifs for visible coverage.
```

For surahs with defined pericopes, use a final cross-pericope check after the
local-scene and lexical-surprise passes. Send the same agent this message:

```text
Freeze the pericope-local and lexical-surprise findings. Now check for channels
spanning pericope boundaries or the whole surah. Add one only when its bridge
is a shared invariant, repeated scene signature, causal sequence, role
progression, contrast, or reversal, not loose topic. Name the pericopes and
bridge. Give each scene one canonical placement; do not duplicate local
findings to express a whole-surah theme.
```

## Output

Write one Markdown report:

```text
network/v3/reviews/s###/reader_a_pilot.md
```

The report must contain first-pass discovery findings in hierarchical form:

- parent channels;
- their nested subchannels; and
- standalone subchannels that do not defensibly share a parent invariant.

Working ledgers and coverage accounting stay internal. There is no channel
quota, but report length must follow scene-complete findings rather than
visible branch coverage. Do not include copied queue rows, file inventories,
command transcripts, full candidate data, grading language, or audit records.

## Pilot Command

Use the prompt file with `SURAH_TAG` replaced by the target tag.

For S001:

```text
Review S001 using only:
- network/v3/prompts/blind_candidate_review.md
- network/v3/experiments/corpus_neo_adaptive/s001/review_bundle.json

Write the report to:
- network/v3/reviews/s001/reader_a_pilot.md
```

## Review Order

1. Pilot: S001.
2. Short-surah calibration: S100, S112, S113, S114.
3. Medium review batch: S020-S030 or another bounded set chosen after the
   pilot report is checked.
4. Long surahs such as S002 should wait until the pilot output format is stable.

## Acceptance Criteria

A prototype review is complete when `reader_a_pilot.md`:

- builds one-scene subchannels before parent consolidation;
- gives exact `branches[].id` evidence without copying rows or relying only on
  non-unique `citation_ref` aliases;
- includes only active branch senses that participate in the stated scene;
- makes the surprising reach support, materialize, reframe, or usefully
  pressure the primary reading;
- keeps concrete latent scenes compact and gives each one canonical placement;
- keeps the report as discovery output, not an audit or grading record.

## Post-review recall and coverage diagnostic

After the final staged pass is complete, mechanically compute unique exact
`branches[].id` values cited in `reader_a_pilot.md` and compare them with the
bundle's `branches` table. Do not count non-unique `citation_ref` aliases
unless the exact branch ID is also present.

Coverage is diagnostic, not an acceptance threshold. The lexical-surprise
sweep controls recall; never enlarge channels or create domain catalogs merely
to raise the percentage.

If exact cited branch coverage is below 50%, send the same agent this message:

```text
Your exact branch coverage is below 50%. Do not inflate channels or create
domain buckets to raise the percentage. Re-open the uncited bundle branches and
perform an underharvest check: add only compact, scene-complete findings whose
active motifs support, materialize, reframe, or usefully pressure a primary
surah reading. If omitted branches remain unsuitable, leave them omitted rather
than stuffing them into existing channels. Report the new numerator,
denominator, and percent when finished.
```
