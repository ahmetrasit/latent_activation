# GSLS 2.1

GSLS 2.1 is a lean, provider-neutral workflow for passage-specific lexical synthesis. It keeps V2's evidence model and interpretive method while removing provenance ledgers, hashes, closure files, repeated audits, and per-transition metadata.

## Workflow

```text
prepared inputs
  -> Agent A synthesis
  -> Agent B substantive review
       clean -> final synthesis
       revision-required -> Agent A targeted revision -> final synthesis
  -> optional Agent C publication rendering
```

Agent A remains the sole synthesis author. Agent B identifies substantive defects and omissions without writing a replacement analysis. Agent C only renders accepted findings.

## Prepare a run

```bash
python3 v2.1/scripts/prepare_run.py \
  --run-root runs/s1-pilot \
  --run-id s1-pilot \
  --surah 1 \
  --ayah-start 1 \
  --ayah-end 7 \
  --primary-scaffold /absolute/path/to/primary-scaffold.md \
  --allow-source-limited
```

The builder reads the configured files under `resources/`, creates the frozen prepared inputs, and excludes every V4 branch whose `branch_images.contaminated` value is not `no`.

## Orchestrate

```bash
python3 v2.1/scripts/orchestrate.py init runs/s1-pilot
python3 v2.1/scripts/orchestrate.py task runs/s1-pilot
python3 v2.1/scripts/orchestrate.py transition runs/s1-pilot complete
```

Repeat `task` and `transition` for the current state. Task emission is idempotent within a state. The scripts do not call a model provider and do not run agents themselves.

Agent events are:

- Agent A synthesis: `complete` or `evidence_blocked`
- Agent B review: `clean`, `revision_required`, `human_needed`, or `evidence_blocked`
- Agent A revision: `complete`, `human_needed`, or `evidence_blocked`
- Agent C rendering: `complete`

## Validation

```bash
python3 v2.1/scripts/validate_run.py runs/s1-pilot --stage inputs
python3 -m unittest discover -s v2.1/tests -v
```

Validation is intentionally narrow. It checks that prepared evidence is readable, lexical rows are clean, synthesis records retain their core epistemic fields, review verdicts are usable, and required work products exist.

See `00_orchestration_spec.md`, `00_input_supply_guide.md`, and `05_schema_contract.md` for the complete contract.
