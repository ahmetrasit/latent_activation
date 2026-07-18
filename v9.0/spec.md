# V9.0 Orchestration Specification

V9.0 begins after an authorized formation reservoir already exists. It does
not run lexical discovery, recursive harvesting, validation, or adversarial
review.

## Agent

Use one persistent cold author for both turns. When the interface exposes the
settings, use:

```json
{
  "agent_type": "worker",
  "fork_context": false,
  "model": "gpt-5.6-sol",
  "reasoning_effort": "max"
}
```

Prefer `multi_agent_v1.spawn_agent`. If only `collaboration.spawn_agent` is
available, use `fork_turns: "none"` and report that role, model, and reasoning
effort could not be selected explicitly.

## Turns

Turn 1 uses `prompts/01_theme_recomposition-v9.0.md`. Supply the raw passage,
primary scaffold, morphology, syntax, lexical branches, and frozen reservoir.
It writes a compact findings map.

Turn 2 continues with the same author and uses
`prompts/02_target_language_rendering-v9.0.md`. Supply the same authorized
field plus that author's findings map. It writes the sole target-language
publication.

Turn 3 is a mandatory same-author follow-up pass. Send the paragraph below
verbatim after Turn 2 completes. It is not passage-specific and must not name
benchmark findings, predecessor outputs, gold/reference prose, or the expected
answer. Its purpose is to correct the general failure mechanism observed in
pilot runs: agents often keep strong latent operations beside the surface
reading as decorative imagery, negative-only boundary cases, or compressed
branch lists instead of letting them transform the passage.

```text
What is the root cause that the draft still feels conservative, flattened, additive, and underformed? Redo it from the upstream theme map rather than from the previous prose. The main failure mode to avoid is treating latent formations as decorative, optional, or only negative boundary cases. When the supplied map supports a full operative transformation, state it directly and let it change the surface reading. Each major paragraph should create one memorable lexical surprise: ordinary surface hearing -> exact latent operation -> changed surface hearing. Do not expand by cataloguing branches; combine branches that perform the same operation, give the formation enough concrete image-force to be felt, and let exact grammar, participant roles, source-to-surface locks, and passage movement determine rank. Repair every axis that is merely mentioned rather than actually formed. If a formation is defensible, do not bury it in caution; if it is only decorative, omit it. Preserve successful architecture, but replace weak prose when a stronger exact formation does the passage work better. Write synthesis, not audit language. This time do it right.
```

Turn 3 overwrites the Turn 2 publication path. It must use the upstream theme
map as its source rather than revising the previous publication line by line.
Do not ask the author to create an assessment file during orchestration.

Do not show the author gold/reference prose, predecessor publications,
comparisons, reviews, benchmark diagnoses, or named expected findings. Do not
manually suggest a passage-specific positive or negative interpretation.

## S1 test paths

Authorized inputs:

```text
v3/run/s001-full-20260716/inputs/passage-arabic.txt
v3/run/s001-full-20260716/inputs/primary-scaffold.md
v3/run/s001-full-20260716/inputs/morphology.tsv
v3/run/s001-full-20260716/inputs/syntax.tsv
v3/run/s001-full-20260716/inputs/lexical-branches.jsonl
scratch/s001-hybrid-proof-20260717/03-integrated-mechanism-map-hybrid-proof.md
```

Versioned outputs:

```text
v9.0/run/s001-existing-reservoir-20260718/01-theme-map-v9.0.md
v9.0/run/s001-existing-reservoir-20260718/02-publication-tr-v9.0.md
```

Assessment occurs only after Turn 3. Compare equal material only. The test is
whether shared formations are more coherent, memorable, interpretively
productive, and immediately visible than in the expansive reservoir.

## General run pattern

For a new surah, create a versioned run directory under:

```text
v9.0/run/sNNN-existing-reservoir-YYYYMMDD/
```

Use these output filenames:

```text
01-theme-map-v9.0.md
02-publication-tr-v9.0.md
```

If no custom frozen reservoir exists for that surah, use the best available
authorized predecessor reservoir or mechanism map as the frozen reservoir. In
the current workspace, V3 mechanism maps are acceptable upstream reservoirs
for pilot runs because they already contain discovered formations and are not
gold/reference prose.

The cold author needs only:

- this spec;
- the two V9 prompts;
- the raw passage, primary scaffold, morphology, syntax, and lexical branches;
- the selected frozen reservoir or mechanism map;
- the versioned output paths.

The cold author should not inspect repository history or search for comparison
materials unless explicitly assigned to assess after orchestration.
