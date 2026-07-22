# Latent Activation

This repository contains experimental workflow packages and run outputs for latent lexical activation research.

## Development Status

`v11` and `v12` are the production workflow versions.

`v13` is retired. Its dynamic retrieval/cache design reduced upfront packet
size, but the S48 comparison showed that it was less generative than `v12`: it
preserved the main latent chain while dropping several surprising secondary
activations. Use `v12` for the current ayah-attached full-context workflow.

`v3` and `v9.0` remain important candidates for stronger passage-level
synthesis work. Later synthesis experiments should consider using them to
compose a higher-level prose layer from `v11` and `v12` outputs, rather than
treating those newer outputs as the final publication form by themselves.

## v12 Turkish Baseline Status (2026-07-22)

The Turkish ordinary target-language baseline files are complete for all 114
surahs. S1 uses the accepted pilot artifact, and S2-S114 have generated
surah-level baseline artifacts and checkpoints under `_status/v12_cross_run/`.

The full baseline set has passed structural validation against the frozen QAC
database with `validated_count=114` and `failed_count=0`. The v12 cross-run
workflow is ready for the next steps documented under `_status/`, especially
the package, publication, audit, and finalization runbooks in
`_status/v12_cross_run/`.

## Dictionary and Quran-SLM Integration Status (2026-07-21)

For dictionary candidate discovery, use the comprehensive `v11` QNet audit and
fix records as the integration authority. This is distinct from the semantic
neighbor matrices in `../quran-slm`.

An audit of both Quran-SLM global baseline/Neo pairs found that their rank
artifacts are internally consistent but their shared catalogs predate four
currently accepted, clean branch cards:

- `root_000086/B011`
- `root_000086/B012`
- `root_000086/B014`
- `root_001697/B002`

These are **missing branch cards within already represented QAC-attested
roots**, not missing roots and not Furūq-only roots. Because a Neo overlay uses
its baseline catalog, it cannot recover an omitted card. The Qurʾan/QAC
corpus-only pair must grow from 10,928 to 10,932 cards, and the combined
Qurʾan/QAC + Furūq pair from 18,781 to 18,785. The Furūq-only catalog remains
7,853 cards; root counts do not change.

This gap does not block initial dictionary authoring. QNet remains a candidate
discovery fallback, with different coverage for the four cards:

| Focus card | Available QNet fallback |
| --- | --- |
| `root_000086/B011` | Exact port in the frozen snapshot: 8 core keywords, 8 bridge keywords, and 5 themes |
| `root_000086/B012` | Exact port in the frozen snapshot: 7 core keywords, 9 bridge keywords, and 6 themes |
| `root_001697/B002` | Exact thematic assignment in the comprehensive `v11` post-fix record; not yet in the frozen dictionary QNet database |
| `root_000086/B014` | No exact QNet port; only the represented root's QNet neighborhood and themes may be used as indirect candidates |

QNet is a nomination source, not a substitute score for a missing Quran-SLM
row. Indirect candidates must remain provenance-labeled and must be checked
against current Furūq branch boundaries before a distinction is published.
Once Quran-SLM is rebuilt, its candidates can be added to the four affected
master entries in a later editorial enrichment pass.

`resources/furuq_v4.sqlite` is the older 18,781-clean-card input (SHA-256
`318d7128a3b434d815eed0f0f926b7b79cd0c64a34566255c22288c5af87fca2`).
The canonical input for a rebuild is
`../dictionary/data/working/furuq_v4.sqlite` (SHA-256
`1099db0d56515d2eb3e8d72f104f2e338c2c9a8c1fa6abbb046406d3b327e722`),
with 18,785 accepted, clean cards. Do not regenerate Quran-SLM from the bundled
older copy; either synchronize it explicitly or point the exporter at the
canonical database.

The comprehensive QNet completion record is
[`v11/audits/qac-qnet-root-coverage-2026-07-19.fix-manifest.json`](v11/audits/qac-qnet-root-coverage-2026-07-19.fix-manifest.json).
It records a target state of 11,741 nodes and 74,615 branch-theme memberships,
including 448 completed branch ports across 305 roots. The follow-up
[`v11/audits/qnet-fk-repair-2026-07-19.json`](v11/audits/qnet-fk-repair-2026-07-19.json)
repairs 52 bridge/theme foreign-key gaps. The absolute QNet output path recorded
by those audits is not present in this checkout. Initial dictionary work can use
the fallback policy above, but materialize and freeze the audited post-fix
database before treating its repaired ports as an automated production QNet
source; do not treat an older local QNet database as equivalent.

## Prose Architecture

`_prose/` documents the current plan for turning workflow outputs into layered
Turkish and English prose.

The production direction is not one monolithic final essay. The target model is:

```text
Ayah first, channel later, evidence underneath.
```

Turkish is the first target language. The planned Turkish layers are:

- `Dinle`: short v12-led ayah orientation for first listening;
- `Derinleş`: expanded v12-led ayah exploration, with v11 findings promoted only
  when they clearly attach to the focused ayah;
- `Kanallar`: surah/pericope channels built from reviewed `slm_local` axes,
  v11 discovery findings, and v3-style passage synthesis;
- `İzini Sür`: expandable evidence and provenance, including roots, branches,
  source artifacts, deferred findings, and rejected alternatives.

Source roles are separated:

```text
v12       -> ayah-level analytical control
slm_local -> cheap surah/pericope channel detector and ayah-channel links
v11       -> high-recall discovery reservoir for channel validation/detail
v3        -> passage-synthesis and prose architecture support
```

The first implementation slice is S103. Before rendering prose, the plan
requires a source manifest, canonical reference map, source-finding ledger,
normalized claim/evidence/channel records, and a closed coverage audit. See
`_prose/README.md` and `_prose/tr/PLAN-s001-s100-s103.md`.
