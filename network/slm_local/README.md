# SLM-local + Qnet production workflow

This is the current stable workflow for building semantic-channel candidate
packages in this repo.

It reads `quran-slm` `surah-local-ar-conditional-v1` bundles and combines them
with existing Qnet branch keywords/themes from `quran-roots`.

It does not generate new lexical facts and must not modify either sibling repo.

## Inputs

For a surah number `N`, the script expects:

```text
../quran-slm/resources/surahs/s###/branches_ar.tsv
../quran-slm/resources/surahs/s###/root_occurrences.tsv
../quran-slm/artifacts/surah_networks_global/s###/catalog.json
../quran-slm/artifacts/surah_networks_global/s###/affinity.npy
../quran-roots/_corpus/activation/Qnet/v2/network/incidence_full/branch_keywords.tsv
../quran-roots/_corpus/activation/Qnet/v2/network/bridge_theme_full/branch_theme_inventory.tsv
```

The `s###` tag is zero-padded, for example S1 is `s001` and S48 is `s048`.

`artifacts/surah_networks_global/` is authoritative and contains all 114
surah-scoped dense networks.

## Run

Run one surah:

```bash
python3 network/slm_local/build_surah_channel_package.py --surah 100
```

Run the current validation set:

```bash
python3 network/slm_local/build_surah_channel_package.py --surah 1
python3 network/slm_local/build_surah_channel_package.py --surah 100
python3 network/slm_local/build_surah_channel_package.py --surah 103
python3 network/slm_local/build_surah_channel_package.py --surah 48
```

Optional arguments:

```bash
python3 network/slm_local/build_surah_channel_package.py \
  --surah 100 \
  --quran-slm ../quran-slm \
  --quran-roots ../quran-roots \
  --output-dir network/slm_local/output \
  --top-k 10 \
  --skip-n 1
```

## Outputs

For S100, output goes to:

```text
network/slm_local/output/s100/
```

Each run writes:

- `summary.json`: counts, status totals, roots, branch counts, and ayah span per
  channel.
- `domain_channel_candidates.jsonl`: full review records including per-ayah
  construction and support examples.
- `domain_channel_candidates.tsv`: compact table for quick inspection.
- `slm_edges.jsonl`: raw SLM branch-neighbor evidence.

Normal agent review should use only `summary.json` and
`domain_channel_candidates.*`.

Use `slm_edges.jsonl` only for debugging because it can be large.

## What the script does

The script:

1. loads surah-local SLM affinity scores;
2. loads Qnet branch keywords/themes;
3. selects direct in-domain anchor branches from existing Qnet facets;
4. uses SLM nearest-neighbor edges as support/bridge evidence;
5. writes channel candidates with root counts, branch counts, ayah coverage,
   anchor edge counts, bridge edge counts, top facets, and per-ayah build.

The script does not decide final findings.

It produces candidate packages for human or blind-agent adjudication.

## Current channel gates

The current transparent domain gates are:

- D01: motion / force / incursion / center
- D02: fire / ignition / light / daybreak
- D03: conflict / redress / judgment / restraint
- D04: favor / wealth / attachment / ingratitude
- D05: concealment / extraction / knowledge / testimony
- D06: water / growth / fertility / barrenness
- D07: guidance / road / direction
- D08: authority / obedience / hierarchy

These are not final theological findings.

They are repeatable review candidates built from existing branch labels and
network support.

## Review policy

A reviewer should judge each channel as:

- `strong`: coherent, sufficiently supported, and prose-explainable from branch
  images.
- `conditional`: partly coherent but composite, generic, root-critical, or
  requiring manual split.
- `reject`: too thin, over-broad, mislabeled, or not supported by branch images.

Required review outputs:

- verdict per channel;
- 2-5 sentence prose explanation per channel;
- root count and branch count per accepted/conditional channel;
- notes on over-broad roots, generic facets, and likely split points;
- methodology flaws that could affect the package.

## Known caveats

- S48 `ن و س` is resolved upstream through canonical `ء ن س` alignment.
- S48 currently produces over-broad channels that span most ayahs, so treat S48
  output as recall-heavy.
- Contextual sense selection is unresolved: one root occurrence can enter
  multiple channels through different dictionary branches.
- Reciprocal branch edges and duplicated facets can inflate support counts, so
  prose review must prioritize branch-image coherence over raw edge count.
