# v12 Cross-Run Production Package

This package integrates the standard v12 and eleven-ayah/±5 reader outputs into
an ayah-level claim ledger.

Start with [STATUS.md](STATUS.md) for the current checkpoint. The root
orchestrator then follows [ORCHESTRATION.md](ORCHESTRATION.md), spawns fresh
stage workers, and centralizes canonical writes. There is no workflow CLI and
no script invokes agents. Scripts are limited to deterministic parsing, payload
construction, packet enrichment, TSV updates, and lightweight validation.

Production compares an actually constrained regular window (focus ±2 ayat)
with an actually constrained wide window (focus ±5 ayat). A prompt declaration
does not replace packet-level visibility control. Existing whole-surah runs are
discovery/control inputs unless explicitly accepted for calibration.

## Core Flow

```text
bootstrap + linguistic bind -> extract -> normalize -> grade -> publish -> close
```

Reconciliation is used only for a real conflict or necessary split/merge.
Audits and derived handoff views are optional, not production gates.

## Non-Loss Contract

Every extracted finding remains represented:

- failed lexical gates remain `unlicensed` evidence;
- unpromoted mechanisms remain `rejected` claims;
- merged and split findings retain lineage;
- evidence-only, deferred, and conflicting material remains queryable.

`Rejected` means not promoted. `Unlicensed` means not lexically available.
Neither means discarded.

## Independent Decisions

The workflow keeps these axes separate:

1. `lexical_status`;
2. `resonance_strength`;
3. `publication_role`;
4. `translation_role`;
5. `disposition`.

A normal strong secondary resonance is:

```text
lexical_status: analogical_resonance
resonance_strength: strong
publication_role: secondary
translation_role: none
disposition: accepted
```

Multiple primary and multiple secondary claims are allowed. Analogical
resonance may organize commentary but never silently governs translation.

## Contents

- [ORCHESTRATION.md](ORCHESTRATION.md): normative agent orchestration;
- [STATUS.md](STATUS.md): current readiness decision and exact resume point;
- [schema/SCHEMA.md](schema/SCHEMA.md): canonical TSV schema;
- `schema/templates/`: exact TSV headers;
- `prompts/`: stage-worker instructions;
- `model_schemas/`: worker JSON contracts;
- `scripts/stage_operations.py`: deterministic payload and commit functions;
- `scripts/build_linguistic_bindings.py`: QAC, attachment-unit, syntax, and
  root-cooccurrence binding;
- `scripts/build_word_claim_views.py`: derived all-word and claim-specific
  branch-use TSVs for downstream commentary/translation work;
- `scripts/workflow_common.py`: parsing, packet, TSV, and state helpers;
- `scripts/validate_workspace.py`: normal structural validation; strict mode is
  optional;
- `s###/`: one canonical workspace per surah.

The S1 workspace is the integration calibration. Ayah 1:6 is the completed
slice; the remaining packet ayahs proceed through fresh stage workers under the
same orchestration spec. Because both historical S1 readers saw the same
whole-surah packet, this fixture does not by itself validate the intended
five-versus-eleven-ayah production comparison.
