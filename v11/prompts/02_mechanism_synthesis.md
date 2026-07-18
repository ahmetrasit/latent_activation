# v11 Agent Prompt — 02 Mechanism Synthesis

You synthesize the activated branches into a passage mechanism.

Input:

```text
05-activation-pass.json
01-passage.json
03-candidate-bridges.json
10-discovery-ranking.json
```

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
