# v1 orchestration spec

## Objective

Run a two-stage synthesis workflow over assigned Qurʾanic ayah intervals. The workflow is designed to discover and refine candidate synthesis units generated from temporally conditioned lexical, morphological, syntactic, and recitational activation.

The workflow must preserve auditability: every candidate must identify the seed, selected branches, unused corroborating features, constraints, grade, and evidence trail.

## Stages

### Stage 1: Temporally conditioned reactivation

- Agent: fresh `gpt 5.5 high` agent.
- Passes: two.
- Pass 1 input: `v1/prompts/stage1.md`.
- Pass 1 purpose: exhaustive discovery of candidate synthesis units by seed.
- Pass 2 input: the verbatim follow-up prose below, sent back to the same Stage 1 agent after Pass 1 is complete.
- Pass 2 output: `v1/outputs/{surah}-stage1-pass-2.md`.
- Pass 2 purpose: consolidate, prune, and clarify Stage 1 candidates while preserving seed-level audit trails.

Stage 1 must prioritize temporal exposure, constructive traversal, reactivation, prediction, freeze-points, and independent corroboration.

#### Stage 1 Pass 1 orchestration boundary

The orchestration prompt for Stage 1 Pass 1 must be minimal. It should provide only the assigned passage, the sacred Arabic text source, the prompt file path, and the output location. Do not mention Stage 1 Pass 2, Stage 2, later workflow steps, grading follow-ups, or any hidden orchestration plan in the Pass 1 prompt. The Pass 1 agent should read `v1/prompts/stage1.md` in full and strictly follow only that prompt plus the minimal routing metadata.

#### Stage 1 Pass 2 follow-up prose

The orchestration agent must send the following text verbatim as the follow-up pass after Stage 1 Pass 1 has completed:

```text
I see that you visited only a limited number of words per finding. Identify the root cause for that limitation. Then restart from the very first rooted word and perform exhaustive work. For every eligible rooted word or construction, initiate its own seed pass. Apply the same deep lexical standard to every word, not only to the words that appear promising early. After each file creation, check whether you performed exhaustive work before moving on: generate any potentially missing images and revise the file until it is exhaustive.
```

The Stage 1 Pass 2 orchestration must provide the output location `v1/outputs/{surah}-stage1-pass-2.md`. This file is the final Stage 1 artifact and the source input for both Stage 2 runs.

#### Optional Stage 1 Pass 2 recordkeeping suggestion

This is not currently required, but may be useful for future Stage 1 Pass 2 output normalization. Pass 2 may end with a standalone Image Packet Catalog, one packet per distinct image-fork:

```text
IMAGE_ID
Starting seed
Complete image
Passage-order assembly
Participants and roles
Operation / mechanism
Direction / force / medium
Temporal development
Outcome / closure
Exact branch constituents
Unfilled roles, if any
Status: COMPLETE or FRAGMENT
```

A `COMPLETE` image need not explain the whole surah. It means every role opened by that particular image has been filled. Distinct simulations must remain separate: body and childbirth, water and pastoral ecology, direction and covenant, praise and hostile labeling should each receive their own packet.

### Stage 2: Deep lexical synthesis

- Agent: fresh `gpt 5.5 high` agent for each Stage 2 run, different from the Stage 1 agent.
- Runs: two independent sibling runs.
- Run A input: `v1/prompts/stage2_questions_prompt_v1.txt`.
- Run A source input: `v1/outputs/{surah}-stage1-pass-2.md`.
- Run A output: `v1/outputs/{surah}-stage2-big-picture.md`.
- Run A purpose: identify the surah's governing axes and big-picture structure from the Stage 1 candidate set.
- Run B input: `v1/prompts/stage2_test.md`.
- Run B source input: `v1/outputs/{surah}-stage1-pass-2.md`.
- Run B output: `v1/outputs/{surah}-stage2-pass-1.md`.
- Run B purpose: perform lexical synthesis, distinguish primary meaning from secondary simulation, and preserve only synthesis units with defensible lexical support.

The two Stage 2 files are generated independently from `v1/outputs/{surah}-stage1-pass-2.md`. `v1/prompts/stage2_test.md` does not take `v1/outputs/{surah}-stage2-big-picture.md` as input.

Stage 2 must not erase Stage 1 provenance. It may revise grades, merge duplicates, split over-broad models, and mark unstable candidates for verification.

#### Stage 2 Run A orchestration boundary

The orchestration prompt for Stage 2 Run A must be minimal. It should provide only the assigned passage, the sacred Arabic text source, the Stage 1 Pass 2 output at `v1/outputs/{surah}-stage1-pass-2.md`, the authorized primary scaffold if any, the permitted finding files, the supplied annotations if any, the target language, the prompt file path, and the output location `v1/outputs/{surah}-stage2-big-picture.md`. Do not mention Stage 2 Run B, later workflow steps, revision follow-ups, or any hidden orchestration plan in the Run A prompt. The Run A agent should read `v1/prompts/stage2_questions_prompt_v1.txt` in full and strictly follow only that prompt plus the minimal routing metadata.

#### Stage 2 Run B orchestration boundary

The orchestration prompt for Stage 2 Run B must provide only the assigned passage, the sacred Arabic text source, the Stage 1 Pass 2 output at `v1/outputs/{surah}-stage1-pass-2.md`, the authorized primary scaffold if any, the permitted finding files, the supplied annotations if any, the target language, the prompt file path, and the output location `v1/outputs/{surah}-stage2-pass-1.md`. The Run B agent should read `v1/prompts/stage2_test.md` in full and strictly follow only that prompt plus the Stage 1 Pass 2 output and minimal routing metadata.

No v1 stage uses a 5.6-series model.

## Shared constraints

Agents must:

1. Use only the resources explicitly named in the prompt for the relevant pass or run.
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
- Stage 1 final output: `v1/outputs/{surah}-stage1-pass-2.md`
- Stage 2 big-picture output: `v1/outputs/{surah}-stage2-big-picture.md`
- Stage 2 Run B output: `v1/outputs/{surah}-stage2-pass-1.md`
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
