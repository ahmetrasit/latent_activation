WORKFLOW_ID: GSLS-3A-2.1
RUN_ID: s1-gold-a-20260715
AGENT_ID: C
STATE: C_RENDER
RUN_ROOT: /Users/ahmetrasit/projects/latent_activation/v2.1/run/s1-gold-a-20260715
ROLE_PROMPT: /Users/ahmetrasit/projects/latent_activation/v2.1/prompts/agent-c-publication.md

Read the role prompt in full.

Agent A's synthesis has been accepted by the operator and promoted unchanged to final. Render it; do not review or revise its substantive findings.

## Evidence inputs

- /Users/ahmetrasit/projects/latent_activation/v2.1/run/s1-gold-a-20260715/inputs/run-card.json
- /Users/ahmetrasit/projects/latent_activation/v2.1/run/s1-gold-a-20260715/inputs/passage-arabic.txt

## Final synthesis to render

- /Users/ahmetrasit/projects/latent_activation/v2.1/run/s1-gold-a-20260715/agent-a/final/final-synthesis.jsonl
- /Users/ahmetrasit/projects/latent_activation/v2.1/run/s1-gold-a-20260715/agent-a/final/final-synthesis.md

## Turkish rendering requirements

- Write polished, idiomatic Turkey Turkish as a continuous, high-depth essay for an educated general reader.
- Preserve all six substantive findings, their ordering logic, uncertainty, and linguistic boundaries.
- Remove English leakage and internal workflow jargon from the publication prose. In particular, do not print `non-empty`, `gold-ready`, `prepared-inputs-only`, `accepted-clean-v4-branch-records`, "run kartı", agent names, schema language, file paths, branch identifiers, or internal confidence labels.
- Recast technical calques in natural Turkish. For example, express coalition-based support as support from several converging pieces of evidence, and use "isim tamlaması" rather than untranslated notation where practical.
- Arabic passage expressions may remain in Arabic. Necessary established Turkish linguistic terms may remain technical.
- Do not flatten the argument into a summary, add outside information, or introduce any claim absent from the final synthesis.
- Before finishing, reread the entire essay specifically for stray English words, awkward mixed-language phrases, and meta-workflow language, and correct them.

## Output

Write only:

- /Users/ahmetrasit/projects/latent_activation/v2.1/run/s1-gold-a-20260715/agent-c/publication.md

Do not run another agent and do not alter the final synthesis files.
