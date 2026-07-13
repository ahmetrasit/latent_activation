# v1 orchestration spec

## Objective

Run a three-stage synthesis workflow over assigned Qurʾanic ayah intervals. The workflow is designed to discover, refine, and verify candidate synthesis units generated from temporally conditioned lexical, morphological, syntactic, and recitational activation.

The workflow must preserve auditability: every candidate must identify the seed, selected branches, unused corroborating features, constraints, grade, and evidence trail.

## Stages

### Stage 1: Temporally conditioned reactivation

- Agent: fresh `sol 5.6-max` agent.
- Passes: two.
- Pass 1 input: `v1/prompts/stage1.md`.
- Pass 1 purpose: exhaustive discovery of candidate synthesis units by seed.
- Pass 2 input: the verbatim follow-up prose below, sent back to the same Stage 1 agent after Pass 1 is complete.
- Pass 2 purpose: consolidate, prune, and clarify Stage 1 candidates while preserving seed-level audit trails.

Stage 1 must prioritize temporal exposure, constructive traversal, reactivation, prediction, freeze-points, and independent corroboration.

#### Stage 1 Pass 2 follow-up prose

The orchestration agent must send the following text verbatim as the follow-up pass after Stage 1 Pass 1 has completed:

```text
I see that you visited only a limited number of words per finding. Identify the root cause for that limitation. Then restart from the very first rooted word and perform exhaustive work. For every eligible rooted word or construction, initiate its own seed pass. Apply the same deep lexical standard to every word, not only to the words that appear promising early.
```

### Stage 2: Deep lexical synthesis

- Agent: fresh `sol 5.6-max` agent.
- Passes: two.
- Pass 1 input: `v1/prompts/stage2.md`.
- Pass 1 purpose: perform deeper lexical synthesis over the Stage 1 candidate set.
- Pass 2 input: the verbatim follow-up prose below, sent back to the same Stage 2 agent after Pass 1 is complete.
- Pass 2 purpose: refine lexical models, distinguish primary meaning from secondary simulation, and preserve only synthesis units with defensible lexical support.

Stage 2 must not erase Stage 1 provenance. It may revise grades, merge duplicates, split over-broad models, and mark unstable candidates for verification.

#### Stage 2 Pass 2 follow-up prose

The orchestration agent must send the following text verbatim as the follow-up pass after Stage 2 Pass 1 has completed:

```text
Re-read the permitted source findings and compare them carefully with your previous synthesis, looking not only for findings that were omitted but also for distinctive lexical images that were technically mentioned yet hidden beneath generic wording; restore every strong or medium finding whose specific mechanism has been underemphasized, and retain weak findings whenever they meaningfully complete a larger image, while preserving their evidential limits. Then rewrite the entire synthesis in fluent, beautiful Turkish prose—not as corrections, annotations, or a branch catalog—so that each recovered image arises naturally at its point in the Quranic sequence, performs a clear role, receives later corroboration, and remains distinct from the word’s primary contextual meaning. Use no evidence beyond the sacred Arabic text and the supplied finding files, and make the revised prose stand entirely on its own.
```

### Stage 3: Truth verification

- Agent: fresh `gpt 5.5 high` agent.
- Passes: one unless later expanded.
- Input: consolidated Stage 2 output plus source/resource references.
- Purpose: verify truth claims, source use, evidence independence, contamination status, and grading consistency.

Stage 3 must separate:

- lexical fact;
- grammatical fact;
- attachment claim;
- temporal/sequence claim;
- interpretive synthesis;
- speculative secondary simulation.

## Shared constraints

Agents must:

1. Use only the resources explicitly named in the prompt for the relevant pass.
2. Preserve branch IDs whenever branch material is used.
3. Keep generated, constituent, corroborative, and constraining evidence separate.
4. Freeze candidate models before testing unused words, morphology, attachments, sequence, or later occurrences.
5. Grade by specificity and independent corroboration, not by volume of associated material.
6. Mark failed seeds, weak candidates, and terminated avalanches instead of silently dropping them.
7. Avoid treating secondary simulations as alternative translations.

## Expected output shape

Each candidate synthesis unit should include:

- `candidate_id`
- `ayah_range`
- `seed_type`: lexical, constructional, morphosyntactic, temporal/acoustic, or verified composite
- `seed`
- `generating_set`
- `selected_branches`
- `constructed_model`
- `freeze_point`
- `predictions_at_freeze`
- `unused_features_tested`
- `corroborators`
- `constraints`
- `temporal_reactivation_notes`
- `rival_models`
- `grade`: strong, medium-strong, medium, weak, or unlikely
- `grade_rationale`
- `source_queries_or_rows_used`

## Directory conventions

- Prompts: `v1/prompts/`
- Inputs or assigned ayah ranges: `v1/inputs/`
- Outputs: `v1/outputs/`
- Scripts: `v1/scripts/`
- Shared local resources: `resources/`

## Sacred Arabic text source policy

The orchestration prompt must provide the assigned passage and a sacred Arabic text source.

For a whole-surah run, provide the surah JSON path directly. Example:

```text
Assigned passage: S108
Sacred Arabic text file: resources/quran/surah_108.json
```

For a partial-surah run or a passage that mixes ayat from multiple surahs, provide `resources/quran/complete-quran.txt` and instruct the agent to extract only the assigned ayat. The file format is:

```text
surah:ayah|arabic text
```

For partial-surah intervals, include basmala in the sacred Arabic text unless the assigned surah is S9. Treat basmala as recitational opening context: include its words, roots, morphology, and sequence position for corroboration, constraint, and reactivation, but never initiate a seed from basmala itself. If a passage-generated image later requires a naming, invocation, mercy, or divine-source role, basmala may corroborate or constrain that role, but it must be marked as opening-context evidence rather than generating evidence. Basmala roots are outside the lexical seed count for the assigned interval.

Examples:

```sh
# Canonical basmala from S1:1
grep -E '^1:1\|' resources/quran/complete-quran.txt

# Whole surah from the complete text, excluding basmala row 0
grep -E '^108:[1-9][0-9]*\|' resources/quran/complete-quran.txt

# Partial interval with basmala opening context
grep -E '^(1:1|108:(1|2|3))\|' resources/quran/complete-quran.txt

# Mixed ayat from multiple surahs with basmala opening context
grep -E '^(1:1|108:(1|2|3)|112:(1|2|3|4))\|' resources/quran/complete-quran.txt

# S9 exception: no basmala
grep -E '^9:(1|2|3)\|' resources/quran/complete-quran.txt
```

Do not use `quran-en.json` or any translation as evidence for Stage 1 or Stage 2.

## Local resources copied for v1

- `resources/qac.sqlite`
- `resources/attachments.tsv`
- `resources/furuq_v4.sqlite`
- `resources/quran/`
