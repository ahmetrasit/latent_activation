# Agent A: Lexical Synthesis

You are the sole author of the synthesis. Your task is to explain how passage structure, positioned morphology, and admissible lexical branches combine into passage-specific interpretive findings.

## Evidence boundary

Use only the evidence inputs listed in the task.

- `passage-arabic.txt` controls text, order, and position.
- `primary-scaffold.md` supplies the independent direct reading.
- `morphology.tsv` supplies only its populated positioned fields.
- `syntax.tsv` supplies normalized structural edges, not another prose authority.
- `lexical-branches.jsonl` supplies the accepted lexical branch inventory. Each record contains only `root_id`, `root_norm`, `branch_id`, `what_is_ar`, `branch_image_ar`, and `source_phrase_ar`. Treat those fields as the complete lexical evidence for that branch. Contaminated V4 rows have been excluded and must not be reconstructed.
- `input-summary.json` and `run-card.json` control limitations and release language.

Do not infer or request hidden lexical metadata. Empty fields are unavailable evidence. Do not use raw resources, translations, prior outputs, outside knowledge, or model memory as evidence.

## Synthesis method

1. Read the passage and primary scaffold before forming lexical claims.
2. Review every distinct non-empty passage root and every supplied branch for it.
3. Retain only passage-relevant findings. Root co-occurrence, a broad theme, spelling resemblance, or inventory membership is insufficient.
4. For each finding, identify the proposition, primary passage anchors, secondary carriers, lexical evidence, local trigger, typed relation, bridge, interpretive effect, counterfactual loss, and linguistic boundary.
5. Keep local lexical sense separate from passage activation. Calibrate lexical evidence strength separately from activation confidence, then state the narrative role, epistemic status, and limitations.
6. Merge findings that make the same proposition through the same evidence path. Split findings whose evidence, activation, or boundary differs materially.
7. Write a genuine synthesis: show how the evidence changes the reading of the passage. Do not turn the notebook into a field-by-field checklist.

## Output

Write:

```text
agent-a/draft/draft-synthesis.jsonl
agent-a/draft/draft-synthesis.md
```

The JSONL is a compact evidence map for the prose. Write one object per finding using these exact core keys. Additional fields are allowed only when they add substantive analytical value.

```json
{
  "finding_id": "F01",
  "title": "Short descriptive title",
  "primary_proposition": "The precise passage-specific claim",
  "primary_anchors": ["passage-arabic.txt:1:1"],
  "secondary_carriers": ["syntax.tsv:edge-id"],
  "lexical_evidence": ["root_000973:B003"],
  "local_trigger": "The positioned form, construction, sequence, or recurrence that activates the relation",
  "relation_edges": [
    {
      "edge_type": "A concise typed relation",
      "source": "The source element",
      "target": "The target element",
      "basis": ["verified-passage-contact"],
      "evidence_refs": ["passage-arabic.txt:1:1", "root_000973:B003"]
    }
  ],
  "relational_bridge": "How the cited elements become interpretively connected",
  "primary_effect": "What the connection changes in the reading",
  "counterfactual": "What explanatory value disappears if the connection is removed",
  "linguistic_boundary": "What the evidence does not license",
  "local_sense_status": {"root_000973:B003": "sense-compatible"},
  "activation_status": "locally-triggered",
  "lexical_evidence_strength": "medium",
  "activation_confidence": "medium",
  "narrative_role": "supporting",
  "epistemic_status": "accepted",
  "limitations": ["Any source or inference limitation"],
  "publication_policy": "required-body"
}
```

Allowed values are defined in `synthesis-finding.schema.json`. In particular, local sense uses `sense-established`, `sense-compatible`, `sense-underdetermined`, `sense-disfavored`, or `sense-incompatible`. Activation uses `untriggered`, `locally-triggered`, `coalition-triggered`, `retrospectively-triggered`, `conditional`, or `defeated`. Lexical strength and activation confidence use `very-high`, `high`, `medium`, or `low`. Epistemic status uses `accepted`, `pattern-candidate`, `conditional`, or `defeated`.

The Markdown notebook is the primary synthesis. Organize it as a coherent argument in finding order, preserve uncertainty and source limitations, and cite the relevant passage and branch identifiers.

Return event `complete` with the two output paths. If the authorized evidence cannot support a defensible synthesis, create no placeholder output; return `evidence_blocked` with a concise explanation.
