# Focus Trace Ledger Annotation Protocol

You are reviewing a mechanically generated raw ledger of focus-trace findings.

Input:

- `ledger.raw.jsonl`

Read only the raw ledger. Do not inspect source focus-trace JSON files, packets,
prior reviews, or other outputs unless the coordinator explicitly supplies them
as input for this annotation task.

## Task

- Read the raw ledger.
- Identify overlap, redundancy, near-duplicates, and low-value findings.
- Preserve valuable ayah/item-specific mechanisms even when roots, triggers, or
  sequence motifs repeat.
- Output JSONL annotation rows only.
- Do not rewrite, summarize, or duplicate the raw ledger.
- Do not edit source files.

Repeated roots or repeated trigger patterns are not by themselves redundant. A
finding is redundant only if its mechanism and changed reading add no
item-specific value beyond another finding.

## Output

Output one valid JSON object per line. Do not output a top-level array. Do not
output Markdown, code fences, comments, or prose report text. Use JSON `null`,
not the string `"null"`.

Each annotation row must be keyed by `finding_key` exactly as provided in the
raw ledger.

Schema:

```json
{
  "finding_key": "source_file::category::finding_id",
  "mechanism_family": "short_snake_case_label_or_null",
  "overlap_group": "short_snake_case_label_or_null",
  "overlap_status": "distinct | valuable_overlap | compressible | near_duplicate | low_value",
  "future_action": "keep | compress | merge | downgrade | omit",
  "merge_target": "finding_key_or_null",
  "commentary_value": "high | medium | low",
  "rationale": "One concise sentence explaining the judgment."
}
```

## Sparse annotation mode

Unless the coordinator asks for a full annotation ledger, output only rows where
at least one annotation field differs from this default:

```json
{
  "mechanism_family": null,
  "overlap_group": null,
  "overlap_status": "distinct",
  "future_action": "keep",
  "merge_target": null,
  "commentary_value": "medium",
  "rationale": null
}
```

The join script will fill missing annotations with those defaults.

## Rules

1. In full annotation mode, output one annotation row for every non-discarded
   finding in `ledger.raw.jsonl`.
2. In sparse annotation mode, output only non-default rows.
3. Use `finding_key` exactly as provided.
4. `merge_target` must be another `finding_key` present in `ledger.raw.jsonl`.
5. `merge_target` must not equal `finding_key`.
6. If `future_action` is `merge`, `merge_target` is required.
7. If `future_action` is not `merge`, `merge_target` must be `null`.
8. Only use `future_action: "merge"` when `overlap_status` is `near_duplicate`
   or `compressible`.
9. Prefer `keep` for findings with a strong local role, even if they overlap
   with a common mechanism family.
10. Use `valuable_overlap` when a finding repeats a shared mechanism but
    develops a distinct local function.
11. Use `compressible` when the finding is valid but can be represented as a
    short note under a stronger nearby finding.
12. Use `near_duplicate` when mechanism and changed reading substantially
    repeat another finding.
13. Use `low_value` when the finding is valid but unlikely to improve
    downstream commentary or analysis.
14. If `overlap_status` is `distinct`, `future_action` should usually be
    `keep`.
15. If `overlap_status` is `low_value`, `future_action` should usually be
    `downgrade` or `omit`.
16. If `future_action` is `omit`, `commentary_value` should be `low`.
17. Keep rationales short. Do not include long excerpts from the raw ledger.

## Mechanism family labels

Prefer these labels when they fit:

- `motion_exertion`
- `motion_to_ignition`
- `visibility_threshold`
- `trace_forensics`
- `witness_testimony`
- `center_penetration`
- `gathering_reconfiguration`
- `nurture_severance`
- `desire_attachment`
- `disclosure_excavation`
- `inner_assay`
- `expert_knowledge`
- `growth_yield`
- `hydraulic_ecology`
- `count_return_accounting`
- `containment_selection`
- `corrosion_diagnostic`
- `other`

For non-S100 runs, if none fit, use `other` or a concise new
`short_snake_case` label.

## Suggested working strategy

First cluster rows by trigger roots, changed-reading shape, and mechanism. Then
judge whether each repeated pattern has a distinct local role. Finally emit
JSONL annotations only.
