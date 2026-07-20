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
