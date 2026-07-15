# GSLS-3A-2.0

A production workflow for gold-standard lexical synthesis under a hard limit of three logical agents.

The constraint is feasible because semantic continuity remains with one integrated synthesis agent. The second agent audits without authoring the gold document. The third agent is optional and only renders a publication view from the adjudicated gold artifact.

## Logical agents

1. **Agent A — Integrated Synthesis Agent**  
   Sole discovery agent and sole author of the draft and final gold notebook.

2. **Agent B — Adversarial Audit Agent**  
   Independently checks evidence, omissions, overclaims, temporal leakage, and branch suppression. It cannot edit the gold notebook.

3. **Agent C — Publication Agent, optional**  
   Produces a reader-facing essay from the frozen gold manifest. It has no discovery, deletion, or confidence authority.

One logical agent may receive several sequential task messages. The orchestrator may batch files or resume a role from frozen external state, but it must not spawn semantic subagents.

Start with:

- `00_orchestration_spec.md`
- `00_input_supply_guide.md`
- `00_task_message_templates.md`
- `05_schema_contract.md`
