# Fresh Gold Renderer: Audio-First Turkish Publication

SESSION: fresh context-free gold renderer agent session; do not continue the A2 session
ROLE_PROMPT: /Users/ahmetrasit/projects/latent_activation/v3/prompts/a2-publication-tr-audio-first.md

Read the role prompt in full and follow it as the intellectual method for this turn.
Use only the evidence and work products listed below. Do not read the gold reference, prior target outputs, translations, the v1 tree, or unlisted repository files.

## Inputs

- /Users/ahmetrasit/projects/latent_activation/v3/run/s001-full-20260716/inputs/passage-arabic.txt
- /Users/ahmetrasit/projects/latent_activation/v3/run/s001-full-20260716/inputs/primary-scaffold.md
- /Users/ahmetrasit/projects/latent_activation/v3/run/s001-full-20260716/a1/discovery-integrated.md
- /Users/ahmetrasit/projects/latent_activation/v3/run/s001-full-20260716/a2/mechanism-map.md

## Output

- /Users/ahmetrasit/projects/latent_activation/v3/run/s001-full-20260716/1-publication.jsonl

Write the complete artifact directly to the output path.

## Deterministic Check

After writing the JSONL, run:

```bash
python3 /Users/ahmetrasit/projects/latent_activation/v3/scripts/render_publication.py /Users/ahmetrasit/projects/latent_activation/v3/run/s001-full-20260716/1-publication.jsonl --check
```

Resolve every structural or content-contract error before reporting completion. Style warnings are advisory and may guide presentation-only rewriting. A third paragraph explicitly permitted by the role prompt is not an error and must not be compressed merely to reach zero warnings. Preserve the established synthesis hierarchy, complete graded finding coverage, and exact grades; never split a synthesized finding into evidence-sized records merely to satisfy formatting or style checks.
