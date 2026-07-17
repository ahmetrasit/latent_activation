# GSLS V6 Prompt Pilot

V6 is an experimental prompt-first workflow for brave lexical discovery,
passage-scale synthesis, and human Turkish publication. It is intentionally
small. It adds no validator, claim database, scoring service, or production
state machine.

The pilot tests one central hypothesis:

> The workflow will improve when one semantic author is explicitly protected
> from premature conservative closure, while separate later authors arrange
> and express the completed synthesis without re-adjudicating it.

All agents use `gpt-5.6-sol` with maximum reasoning depth and no service-tier
override.

## Agent Structure

### Agent 1: semantic author

One persistent agent completes four continuation turns:

1. `01_brave_discovery.md`
2. `02_coalition_resurrection.md`
3. `03_scaffold_integration.md`
4. `04_gold_synthesis.md`

This continuity is deliberate. A fresh synthesis agent must not inherit rich
discoveries only to weaken them because they are surprising, secondary, or not
literally named on the surface.

### Agent 2: narrative architect

A fresh agent reads the completed gold synthesis and writes:

```text
narrative-architecture.md
```

It groups the established findings into a developing oral argument. It is not
allowed to grade, reject, demote, or reopen the semantic work.

### Agent 3: Turkish publication author

A fresh Turkish author completes two continuation turns:

1. `06_publication_tr.md`
2. `07_audio_recomposition.md`

The first turn writes a continuous publication-quality Turkish work. The
second preserves that work while recomposing sentence and paragraph boundaries
for sustained listening.

## Conservative-Bias Correction

V6 treats premature rejection as the main model failure during discovery.

- A branch is not weak because it is secondary to the local gloss.
- A coalition is not weak because its literal object is absent from the
  surface.
- Surprise, remoteness, vividness, or unfamiliarity are not counterevidence.
- Several roots supplying complementary roles in passage order are positive
  evidence even when no single root can establish the scene alone.
- The direct contextual reading protects against replacement; it is not a
  ceiling on secondary activation.
- A boundary is warranted by a concrete contradiction, missing indispensable
  relation, or risk of literal identity, not by a general desire to sound
  cautious.

Discovery first develops the strongest coherent realization of a possibility
and then tests what it predicts. It does not weaken the possibility before
that development has occurred.

## Pilot Scope

The first pilot reuses the frozen V3 S1 evidence under:

```text
v3/run/s001-full-20260716/
```

The emitted manual tasks are under:

```text
v6/run/s001-prompt-pilot-20260716/tasks/
```

This isolates prompt and author-role changes before any investment in new
schemas, validators, TTS infrastructure, or preparation code.

See `00_prompt_first_orchestration.md` for the run sequence and
`08_input_and_task_template.md` for reusable task templates.
