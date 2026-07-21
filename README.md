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
