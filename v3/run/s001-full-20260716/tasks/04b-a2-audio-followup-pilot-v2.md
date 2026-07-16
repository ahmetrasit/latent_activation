# Pilot V2 Turn 4B: Audio-First JSONL Follow-up

SESSION: continue the same gold renderer agent session used for task 04a
ROLE_PROMPT: /Users/ahmetrasit/projects/latent_activation/v3/prompts/a2-publication-tr-audio-followup.md

Read the role prompt in full and follow it as a rendering-only continuation.
The written synthesis master is frozen and is the sole authority for finding boundaries, order, grades, claims, and limitations. Do not reopen discovery or synthesis from session memory.

Use only:

- /Users/ahmetrasit/projects/latent_activation/v3/run/s001-full-20260716/inputs/passage-arabic.txt
- /Users/ahmetrasit/projects/latent_activation/v3/run/s001-full-20260716/inputs/primary-scaffold.md
- /Users/ahmetrasit/projects/latent_activation/v3/run/s001-full-20260716/1-synthesis-master-pilot-v2.md

## Output

- /Users/ahmetrasit/projects/latent_activation/v3/run/s001-full-20260716/1-publication-two-pass-pilot-v2.jsonl

Write the complete artifact directly to the output path. Do not modify any other file. Do not spawn subagents.

## Deterministic Check

After writing the JSONL, run:

```bash
python3 /Users/ahmetrasit/projects/latent_activation/v3/scripts/render_publication.py /Users/ahmetrasit/projects/latent_activation/v3/run/s001-full-20260716/1-publication-two-pass-pilot-v2.jsonl --check
```

Resolve structural or content-contract errors before reporting completion. Style warnings are advisory. They never permit changing, omitting, merging, splitting, reordering, or rescoring a frozen master finding.
