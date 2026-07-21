# v12 Cross-Run Whole-Surah Publication

This package consolidates canonical regular v12 and ±5 v12 findings into a
direct publication structure. Both source families are complete for S001-S114;
no new reader runs are pending.

Start with:

- [STATUS.md](STATUS.md): current implementation checkpoint;
- [ORCHESTRATION.md](ORCHESTRATION.md): normative whole-surah agent workflow;
- [schema/SCHEMA.md](schema/SCHEMA.md): simplified publication model.

## Production Flow

```text
mechanical whole-surah package + QAC/attachment binding
  -> Agent A publishes the whole surah
  -> Agent B reviews the whole surah
  -> optional Agent A repair
  -> deterministic close and atomic commit
```

Agents are never assigned individual ayat. They receive paths to complete
surah files and read the material they need on demand, following the original
v12 pattern.

## Output

Each ayah contains:

- one or more primary contextual findings with `root_id` + `branch_id`
  anchors;
- one or more secondary contextual findings with anchors and a finding-level
  grade: `strong`, `weak`, or `reject`.

Every non-primary or exploratory source finding becomes secondary. A `reject`
secondary is retained in full. There is no third rejected category.

The publication output omits source-finding IDs, translation eligibility,
lexical-status labels, branch-level roles, and branch-level grades. Original
v12 files remain the provenance source.

Deduplication follows contextual-reading equivalence. Anchor overlap does not
justify merging; different contextual readings with the same branches remain
separate.

## Mechanical Linguistic Boundary

`scripts/build_linguistic_bindings.py` already assigns QAC word/morpheme IDs
and cross-walks attachment identifiers to QAC identifiers. It preserves the
original attachment IDs, resolved QAC endpoints, binding methods, and warnings.
The publication agent consumes this cache and never performs the alignment.

## Legacy Material

The existing prompts, model schemas, TSV templates, and S1 ayah-scoped task
artifacts document the previous calibration workflow. They remain available as
history but are not the target production contract. Only Markdown
documentation was updated in the current change; implementation alignment is
still pending.
