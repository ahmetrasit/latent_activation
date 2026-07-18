# v11 Agent Prompt — 01 Activation Pass

You are doing recall-first Qnet branch activation.

Your job is not to be conservative. Your job is to preserve plausible latent activations and label them honestly.

Input files:

```text
01-passage.json
02-branches.json
03-candidate-bridges.json
04-agent-activation-packet.md
10-discovery-ranking.json
```

Use these labels:

```text
A = surface-active / structurally necessary
B = strong secondary activation
C = exploratory latent activation worth inspecting
S = currently silent / no visible bridge
X = data issue
```

Relaxation rules:

```text
If uncertain between S and C, choose C.
If uncertain between C and B, choose C/B.
Do not suppress a candidate because its theme is broad.
Do not require proof-level certainty.
Do not convert branches into graph nodes.
```

For each root:

1. identify primary active branches;
2. identify secondary active branches activated by other passage roots;
3. preserve exploratory latent branches that may matter;
4. assign functional roles.

After labeling activations, separately mark `discovery_value`:

```text
high = surprising latent reading that changes the passage mechanism
medium = useful underlay but partly expected
low = coherent expansion of the surface reading
```

Do not use low discovery value to delete an activation.

Output JSON:

```json
{
  "passage": {"surah": 103, "ayah_start": 1, "ayah_end": 3},
  "activation_bias": "recall_first",
  "branches": [
    {
      "root": "ع ص ر",
      "branch": "B009",
      "label": "C/B",
      "role": "human life-stage underlay",
      "discovery_value": "high",
      "activated_by": [
        {
          "root": "ء ن س",
          "branch": "B006",
          "evidence": ["shared theme sexuality"]
        }
      ],
      "notes": "Preserved as latent activation; not asserted as primary gloss."
    }
  ]
}
```
