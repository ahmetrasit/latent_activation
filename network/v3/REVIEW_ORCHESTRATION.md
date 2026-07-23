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

## Output

Write one Markdown report:

```text
network/v3/reviews/s###/reader_a_pilot.md
```

The report must contain first-pass discovery findings in hierarchical form:

- atomic motifs;
- parent channels;
- subchannels;
- resonance bridges;
- lexical resonances;
- surprise probes;
- residual motifs only when they do not form a coherent probe.

There is no limit on the number of parents, subchannels, bridges, or probes,
and no artificial length cap. The report should be as detailed as the supplied
evidence requires. Do not include copied queue rows, file inventories, command
transcripts, full candidate data, grading language, validation cautions, or
audit records.

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

- uses only `F###` and `PF###` row IDs as source pointers;
- inventories atomic motifs before clustering into broad domains;
- organizes findings into parent channels, subchannels, resonance bridges, and
  surprise probes instead of one flat accepted-channel list;
- gives root:branch evidence without copying rows;
- includes material branch images that belong to a cited channel, without
  carrying unrelated row tails into the report;
- explains each parent/subchannel/bridge in coherent prose rather than as a
  catalog of findings;
- assigns confidence by nucleus coherence, evidence breadth, bridge clarity,
  and distinctness;
- preserves coherent rare images as surprise probes instead of discarding them;
- surfaces coherent latent lexical imagery instead of demoting it for being
  surprising, concrete, or absent from surface translation;
- keeps the report as discovery output, not an audit or grading record.
