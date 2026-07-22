# Cold-agent orchestration spec

Use this spec when a fresh agent needs to run or review the production
semantic-channel workflow without prior conversation context.

## Objective

Build and review semantic-channel candidate packages for one or more surahs
using the production `network/slm_local` workflow.

The workflow is candidate generation, not final adjudication.

## Authority and scope

Allowed:

- read this repo;
- write outputs under `network/slm_local/output/`;
- read `../quran-slm`;
- read `../quran-roots`.

Not allowed unless explicitly requested:

- modify `../quran-slm`;
- modify `../quran-roots`;
- invent new lexical roots, branch labels, or themes;
- treat raw script output as final findings without review.

## Preflight checks

Run these checks first:

```bash
test -f network/slm_local/build_surah_channel_package.py
test -d ../quran-slm
test -d ../quran-roots
python3 -m py_compile network/slm_local/build_surah_channel_package.py
```

For each target surah, verify the source bundle exists:

```bash
test -f ../quran-slm/artifacts/surah_networks_global/s###/catalog.json
test -f ../quran-slm/artifacts/surah_networks_global/s###/affinity.npy
test -f ../quran-slm/resources/surahs/s###/branches_ar.tsv
test -f ../quran-slm/resources/surahs/s###/root_occurrences.tsv
```

Replace `s###` with the zero-padded surah tag, for example `s001`, `s100`,
`s103`, or `s048`.

## Generation commands

Run one surah:

```bash
python3 network/slm_local/build_surah_channel_package.py --surah 100
```

Run the current test set:

```bash
python3 network/slm_local/build_surah_channel_package.py --surah 1
python3 network/slm_local/build_surah_channel_package.py --surah 100
python3 network/slm_local/build_surah_channel_package.py --surah 103
python3 network/slm_local/build_surah_channel_package.py --surah 48
```

Output path pattern:

```text
network/slm_local/output/s###/
```

## Normal review inputs

Use these files:

```text
network/slm_local/output/s###/summary.json
network/slm_local/output/s###/domain_channel_candidates.jsonl
network/slm_local/output/s###/domain_channel_candidates.tsv
```

Do not load this file unless debugging edge details:

```text
network/slm_local/output/s###/slm_edges.jsonl
```

For example, S48 `slm_edges.jsonl` is large and not suitable as normal agent
review input.

## Required report

For each surah, report:

- output folder;
- channel count by status;
- channel verdicts: `strong`, `conditional`, or `reject`;
- root count and branch count per channel;
- one sentence describing how each channel is built;
- any known caveat, especially uncovered roots or over-broad channels.

## Blind-review prompt template

Use this prompt when spawning a blind review agent:

```text
Blind semantic-channel review task.

Use only these local files as evidence:

- network/slm_local/output/s###/summary.json
- network/slm_local/output/s###/domain_channel_candidates.jsonl
- network/slm_local/output/s###/domain_channel_candidates.tsv
- network/slm_local/README.md

Do not use prior agent reports, gold lists, external knowledge, or raw
slm_edges.jsonl unless specifically asked.

For each channel, provide:

1. a short title;
2. verdict: strong / conditional / reject;
3. root count and branch count;
4. 2-5 sentence prose explaining how the channel is built from ayahs, roots,
   and branch images;
5. one methodology caveat if visible.

Prioritize branch-image coherence over raw edge count.
Flag channels that are over-broad, generic, root-critical, or likely composites.
```

## Turkish prose-review prompt template

Use this prompt when the user wants Turkish prose:

```text
Blind Turkish prose task.

Use only these local files as evidence:

- network/slm_local/output/s###/summary.json
- network/slm_local/output/s###/domain_channel_candidates.jsonl
- network/slm_local/output/s###/domain_channel_candidates.tsv
- network/slm_local/README.md

Do not use prior agent reports, gold lists, external knowledge, or raw
slm_edges.jsonl unless specifically asked.

Her kanal için kısa Türkçe başlık ver.
Sonra 3-5 cümlede kanalın hangi ayetler, kökler ve dal imgeleriyle kurulduğunu
açıkla.
Kök sayısını ve dal sayısını belirt.
Sonunda verdict yaz: güçlü / şartlı / reddedilmeli.
Ham edge sayısından çok dal-imgesi tutarlılığına öncelik ver.
```

## Known package states

Current committed/generated packages:

- S1: `network/slm_local/output/s001/`; 8 channels, 6 stable and 2 mixed.
- S100: `network/slm_local/output/s100/`; blind review found 5 strong channels,
  1 conditional channel, and 1 reject.
- S103: `network/slm_local/output/s103/`; 2 stable channels.
- S48: `network/slm_local/output/s048/`; 8 script-stable channels, but likely
  over-broad.

Known issue:

- S48 `ن و س` is resolved upstream through canonical `ء ن س` alignment, but S48
  remains recall-heavy because its candidate channels are broad.

## Success criteria

A run is successful when:

- the script exits successfully;
- `summary.json` exists;
- `domain_channel_candidates.jsonl` exists;
- `domain_channel_candidates.tsv` exists;
- the report distinguishes script status from review verdict.

A review is successful when:

- it can explain each accepted/conditional channel in prose;
- it reports root and branch counts;
- it rejects or flags over-broad/generic channels;
- it names unresolved methodological risks.
