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

`focus_trace/` is the standalone Hermetic Focus Trace workflow. It was added to
recover the surprising, changed-reading effect of the old staged focus runs and
the S100 `reader_m` walk at lower whole-Quran cost. See
[`focus_trace/INTEGRATION.md`](focus_trace/INTEGRATION.md).

## Hermetic Focus Trace Input Bundles (S2-S79)

All S2-S79 focus-ayah input bundles are ready under
`focus_trace/runs/s<S>/packets/` using packet protocol
`focus-trace-pericope-lean-v1`.

The current prepared scope contains 5,751 packet inputs:

- 4,466 ayat in canonical pericope windows;
- 1,285 ayat in whole-surah windows.

Pericope-based surahs:

```text
S2-S12, S14-S30, S33-S34, S36-S43, S51, S54, S56
```

Compact range form:

```text
2-12,14-30,33-34,36-43,51,54,56
```

Whole-surah-window surahs:

```text
S13, S31-S32, S35, S44-S50, S52-S53, S55, S57-S79
```

Pericope windows come from
`../quran-data/data/analysis/channels/network-v3/pericopes/surah_pericopes.jsonl`.
Generation reports are stored at
`focus_trace/runs/pericope_lean_remaining_canonical_packet_size_report.json`
and `focus_trace/runs/surah_lean_s2_s79_packet_size_report.json`.

## v12 Turkish Publication Status (2026-07-23)

The Turkish ordinary target-language baseline files are complete for all 114
surahs. S1 uses the accepted pilot artifact, and S2-S114 have generated
surah-level baseline artifacts and checkpoints under `_status/v12_cross_run/`.

The full baseline set has passed structural validation against the frozen QAC
database with `validated_count=114` and `failed_count=0`.

The Turkish v3 publication run is complete: all 114 final publication files
exist under `_status/v12_cross_run/output/tr/`.

The full 114-surah corpus close audit and downstream import reconciliation are
complete. `_status/v12_cross_run/output/tr/` remains reserved for final
`*_ayah_findings_publication.json` files only.

The durable resume record is `_status/v12_cross_run/STATUS.md`. The normative
runbook remains `_status/v12_cross_run/ORCHESTRATION.md`.

## Dictionary and Quran-SLM Integration Status (2026-07-23)

For dictionary candidate discovery, use the comprehensive `v11` QNet audit and
fix records as the integration authority. This is distinct from the semantic
neighbor matrices in `../quran-slm`.

The earlier Quran-SLM catalog gap for four accepted, clean branch cards is
closed:

- `root_000086/B011`
- `root_000086/B012`
- `root_000086/B014`
- `root_001697/B002`

The Qurʾan/QAC corpus-only pair now includes 10,932 cards, and the combined
Qurʾan/QAC + Furūq pair includes 18,785 cards. The Furūq-only catalog remains
7,853 cards; root counts do not change.

QNet fallback coverage for those four cards is no longer a blocking production
gap. The historical fallback map remains:

| Focus card | Available QNet fallback |
| --- | --- |
| `root_000086/B011` | Exact port in the frozen snapshot: 8 core keywords, 8 bridge keywords, and 5 themes |
| `root_000086/B012` | Exact port in the frozen snapshot: 7 core keywords, 9 bridge keywords, and 6 themes |
| `root_001697/B002` | Exact thematic assignment in the comprehensive `v11` post-fix record |
| `root_000086/B014` | No exact QNet port; only the represented root's QNet neighborhood and themes may be used as indirect candidates |

QNet is a nomination source, not a substitute score for a missing Quran-SLM
row. Indirect candidates must remain provenance-labeled and must be checked
against current Furūq branch boundaries before a distinction is published.

`resources/furuq_v4.sqlite` is the older 18,781-clean-card input plus QAC-only
root-registry rows needed by v12 finalization (SHA-256
`51ead7264626b4f85149b9088d7df009ad4e7a20a2f5042da5e29cbbf2e9dadf`).
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
repairs 52 bridge/theme foreign-key gaps. The audited post-fix QNet database has
been materialized/frozen for production use; do not treat an older local QNet
database as equivalent.

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
