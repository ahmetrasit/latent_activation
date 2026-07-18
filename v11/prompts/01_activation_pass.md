# v11 Agent Prompt — 01 Activation Pass

You are doing recall-first Qnet branch activation.

Your job is not to be conservative. Your job is to preserve plausible latent activations and label them honestly.

Input files:

```text
00-surah-text.json
01-passage.json
02-branches.json
03-candidate-bridges.agent.json
04-agent-activation-packet.md
10-discovery-ranking.json
```

Read `00-surah-text.json` for Arabic recitation text. Treat basmala as part of analysis except for S9; for S1 it is `verse_1`, and for other surahs it is `verse_0`. Use `01-passage.json` as authoritative for QAC word order, morphology, and root resolution.

Use `03-candidate-bridges.agent.json` as the agent-facing bridge queue. The full reservoir remains in `03-candidate-bridges.json`; consult it only for targeted lookup when the compact queue or packet points to a specific candidate/branch that needs verification. Do not attempt to read the full reservoir exhaustively.

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

Do not generate your own discovery ranking or `discovery_value`. Consume `10-discovery-ranking.json` only as a mechanical review queue, and reference its candidate keys or `discovery_value_hint` only when useful.

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
      "mechanical_discovery_refs": ["ع ص ر B009 ↔ ء ن س B006"],
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
