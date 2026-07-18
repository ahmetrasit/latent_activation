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

Assessment occurs only after Turn 2. Compare equal material only. The test is
whether shared formations are more coherent, memorable, interpretively
productive, and immediately visible than in the expansive reservoir.

