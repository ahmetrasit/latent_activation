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
mechanical source validation + compact whole-surah package
  -> Agent A publishes the whole surah
  -> Agent A performs a separate whole-surah self-audit
  -> one global surgical anchor-repair pass
  -> deterministic materialization, close, and atomic commit
```

Agents are never assigned individual ayat. They receive paths to complete
source files plus a packet-derived ayah roster and database-derived cited-anchor
map, then read the material they need on demand. The full packet and linguistic
cache remain coordinator-side.

The anchor map is one column header plus atomic row arrays. Agent A cites short
`anchor_key` strings in its semantic draft; the coordinator later materializes
the used fixed-ayah keys into final `[qac_word_ref, root_id, branch_ids]` rows.
Malformed or
ambiguous keys do not pause Agent A and are collected for the global repair
pass.

Agent A does not rely on memory for the self-audit. After saving the complete
draft, it traverses both source outputs and the draft again in ayah order,
corrects omissions, over-merging, duplication, invalid anchors, and grade-shape
errors in place, and only then marks the draft ready for mechanical close.

## Output

Each ayah contains:

- exactly one row for every packet ayah, in packet order;
- one flat `findings` array with zero or more contextual readings;
- one finding-level grade on every finding: `strong`, `weak`, or `reject`;
- only used fixed-ayah anchors, shaped as
  `[qac_word_ref, root_id, branch_ids]`.

An exploratory source finding remains in the same array and is distinguished by
its grade. A `reject` finding is retained in full; there is no separate rejected
category.

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
The coordinator consumes this cache for mechanical/downstream checks. It is
not sent to the publication agent.

The binder emits `source_tokens.tsv`, QAC word/morpheme rows, and
`word_roots.tsv`. It retains many-to-one cases such as 37:130 rather than
assuming displayed-token and QAC-word counts are equal. The finalizer derives
`finding_word_branches.tsv` by expanding finalized QAC/root anchors to their
used branch IDs. It does not publish unrooted words, unused roots, a complete
word spine, or context-only anchors.

## Legacy Material

The numbered prompts, old schemas, TSV templates, and S1 ayah-scoped task
artifacts document the previous calibration workflow. They remain available as
history but are not the target production contract. Production uses
`publish_whole_surah.md`, `publication_draft.json`, the global repair contract,
and the deterministic package/finalization scripts named in ORCHESTRATION.
