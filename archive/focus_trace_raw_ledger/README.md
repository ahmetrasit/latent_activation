# Archived Focus Trace Raw Ledger Prototype

Status: retired on 2026-07-29.

This folder preserves the prototype mechanical normalized raw ledger workflow:

- `build_focus_trace_raw_ledger.py`
- `focus_trace_ledger_annotation.md`

The workflow was intentionally removed from active Focus Trace orchestration.

## Why it was retired

The goal was to create a surah/pericope-level addition that finds consolidated
surah-wide channels and patterns after ayah-level work completes. The raw
ledger approach was a poor primary substrate for that goal:

- the rich ledger retained too much repeated per-finding evidence and only
  reduced S100 payload from about 611 KB to about 448 KB;
- dropping activation summaries reduced payload further, but then weakened the
  annotation agent's ability to distinguish true duplication from shared
  mechanisms with different evidence;
- using a ledger as the primary surah-wide input keeps the workflow close to
  audit/review of individual findings rather than synthesis of the final
  ayah-level prose.

## Preferred replacement

For surah-wide consolidation, use the generated ayah prose outputs as the
primary input. The prose already performs the first synthesis step and is a
better substrate for discovering macro-channels, repeated mechanisms,
ayah-specific developments, and missing connective tissue.

Keep the raw ledger prototype only as archived reference material. If exact
finding-level audit is needed later, revive this design deliberately as a
secondary audit tool, not as the default surah-level consolidation workflow.
