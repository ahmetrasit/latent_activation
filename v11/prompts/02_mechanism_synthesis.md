# v11 Agent Prompt — 02 Mechanism Synthesis

You synthesize the activated branches into a passage mechanism.

Input:

```text
00-surah-text.json
05-activation-pass.json
01-passage.json
03-candidate-bridges.json
10-discovery-ranking.json
```

Use `00-surah-text.json` for Arabic recitation text. Treat basmala as part of analysis except for S9; for S1 it is `verse_1`, and for other surahs it is `verse_0`. Use `01-passage.json` as authoritative for QAC word order, morphology, and root resolution.

Do not summarize only the surface meaning. Use secondary activations as underlay.

Write:

1. primary surface mechanism;
2. secondary latent underlay;
3. what activates what;
4. what the secondary branches explain that a surface gloss misses;
5. graph-ready root-level edge descriptions.

Separate:

```text
all active/latent readings
```

from:

```text
surprising discovery readings
```

The final mechanism should emphasize the latter without deleting the former.

Keep branch IDs visible as evidence labels, not as final nodes.

Do not generate or overwrite discovery ranking. Use `10-discovery-ranking.json` only as the script-owned mechanical queue for likely surprise value.

Output Markdown:

```text
# Mechanism

## Primary pathway

...

## Secondary activations

...

## Root-level graph

- ع ص ر -> ء ن س via ع ص ر B009 / ء ن س B006 ...
```
