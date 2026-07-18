# v11 — Qnet Latent Activation Workflow

`v11` is a recall-first workflow for discovering branch activations in any surah or ayah group.

The bias is intentional:

```text
false negatives are worse than labeled false positives
```

The workflow should surface latent candidates generously, then label them honestly. It should not prune early just because a bridge is broad, indirect, or not yet proven.

## Core model

Roots are graph nodes.

Branches are not graph nodes. Branches are carried as edge/port labels:

```json
{
  "source": "ع ص ر",
  "target": "ء ن س",
  "source_branch": "B009",
  "target_branch": "B006",
  "shared_themes": ["sexuality"],
  "activation_hint": "latent"
}
```

## Principle

```text
Qnet proposes.
The passage organizes.
The agent composes.
The human decides what is worth preserving.
```

This is linguistic discovery work, not a conservative proof system.

## Pipeline

```text
passage
  ↓
surah text including basmala except S9
  ↓
surface roots, words, order, morphology
  ↓
all Qnet branches for those roots
  ↓
leaf-theme / keyword / Q2 candidate bridges
  ↓
high-recall candidate graph
  ↓
agent activation pass
  ↓
mechanism synthesis
  ↓
secondary expansion pass
  ↓
final integration/report agent
  ↓
final root-level graph and report
```

## Build/run

Example:

```bash
python3 v11/scripts/qnet_activate.py \
  --surah 103 \
  --ayah-start 1 \
  --ayah-end 3 \
  --out-dir v11/run/s103-fresh
```

Every run starts from QAC:

```text
QAC surface roots/root_join_keys
  → Furūq root_id resolution with hamza/key audit
  → Qnet node/theme lookup by resolved root_id
```

Agents should not be started if root resolution is missing or ambiguous.

The script enforces this by default. It also stops if a resolved root has Furūq branches but zero Qnet branch nodes in the selected Qnet layer.

Two exceptions are intentional:

- non-branchable QAC function roots are omitted from branch/Qnet lookup only by explicit allowlist; current allowlist is `كيف` / `ك ي ف` / `كَيْفَ`;
- duplicated Furūq/Qnet IDs for one QAC root key are merged only when they pass deterministic hamza/key duplicate checks, with namespaced branch IDs such as `root_001210:B001` and explicit `source_root_id` provenance.

Override flags exist only for diagnostics:

```text
--allow-unresolved-roots
--allow-qnetless-roots
```

Diagnostic override runs are not agent-ready. If either override flag is supplied, the script publishes `DIAGNOSTIC_ONLY.json` and a diagnostic audit, and it does not publish `04-agent-activation-packet.md` or the normal mechanical output set.

Parent-theme bridges are disabled. The 17 parent themes are too broad for activation evidence and must not create, score, rank, or strengthen bridges.

The script accepts compressed SQLite inputs. Defaults are:

```text
resources/qac.sqlite.gz
resources/furuq_v4.sqlite.gz
../quran-roots/_corpus/activation/Qnet/v2/network/bridge_theme_full/bridge_theme_staging.sqlite
../quran-roots/_corpus/activation/Q2/runs
resources/quran
```

Use `bridge_theme_full` by default. `bridge_theme_current` is a smaller/current subset and can miss valid Qnet nodes for roots that are present in QAC and Furūq.

Dense whole-surah packages are also not agent-ready. By default, if the candidate reservoir exceeds 10,000 candidates, the script emits a dense gate and pericope plan instead of `04-agent-activation-packet.md`:

```text
DENSE_PASSAGE_GATE.json
11-pericope-plan.json
```

Run each listed pericope as a separate package, then integrate across pericope reports.

If a surah fails a gate during orchestration, stop the sequence, diagnose the root cause, draft a fix plan, send that plan to a read-only review agent for assessment, then fix and rerun the failed surah before continuing.

For a root with Furūq branches but no Qnet nodes:

1. first check whether Qnet already contains the same root under a key variant or another root ID;
2. if it does, create a Qnet entry for the QAC/Furūq root by deriving/splitting from that existing Qnet entry and preserving provenance in notes;
3. if it does not, create a minimal Qnet entry from accepted Furūq branch images, with conservative leaf themes/keywords and explicit documentation here;
4. rerun the failed surah before continuing orchestration.

Manual Qnet entries created during v11 orchestration:

| QAC/Furūq root | Qnet root_id | Source Qnet root | Reason | Mapping |
| --- | --- | --- | --- | --- |
| `ط م ن` | `root_003669` | `root_000948` (`ط م ء ن`) | S89 had Furūq branches but zero Qnet nodes for the QAC/Furūq root; Qnet contained the same semantic root under hamzated key `طمءن`. | `B001` calm/stability copied from `root_000948:B001`; `B002` low-ground/topography split from `root_000948:B002`; `B003` posture/bending split from `root_000948:B002`. |
| `ن و س` | `root_004965` | manual from Furūq v4 | S99/S101 had Furūq branches but zero Qnet nodes for the QAC/Furūq root; Qnet had no same-root key variant. | `B001` swaying/dangling oscillation mapped to motion/change/instability themes; `B002` camel-driving mapped to animal/livestock/husbandry/motion/control themes; `B003` disputed origin of `الناس` mapped to identity/social/community/proof-uncertainty themes. |

## Outputs

```text
00-surah-text.json
00-root-resolution-audit.json
01-passage.json
02-branches.json
03-candidate-bridges.json
03-candidate-bridges.agent.json
04-agent-activation-packet.md
08-graph.json
10-discovery-ranking.json
```

`00-surah-text.json` is copied from `resources/quran/surah_{n}.json` and is part of the agent input package. Basmala is part of analysis for every surah except S9, which does not start with basmala. For S1, the basmala is `verse_1`; for other non-S9 surahs, it is `verse_0`. QAC remains authoritative for word order, morphology, and root/root-id resolution.

`01-passage.json` includes QAC word rows, all QAC morpheme rows, root-bearing occurrences, root order, and the analysis verse keys that agents should read from `00-surah-text.json`.

The numbered gap is reserved for agent-produced files:

```text
05-activation-pass.json
06-mechanism.md
07-secondary-expansion.json
09-final-report.md
```

`03-candidate-bridges.json` is the full recall-first candidate reservoir. It can be large.

`03-candidate-bridges.agent.json` is the bounded agent-facing queue derived from `10-discovery-ranking.json`. It exists to keep agent input loadable; it does not prune or replace the full reservoir. Agents read the compact file by default and consult the full reservoir only for targeted verification.

`10-discovery-ranking.json` does not prune. It ranks candidates by likely surprise value:

```text
Does this branch add something non-obvious to the primary reading?
Does it create a material/metaphorical underlay?
Does another root activate it?
Does it change the surah-level mechanism?
```

This file is script-owned mechanical output. Agents consume it as a review queue; they do not generate or overwrite it.

## Discovery labels

Agents should use these labels:

```text
A = surface-active / structurally necessary
B = strong secondary activation
C = exploratory latent activation worth inspecting
S = currently silent / no visible bridge
X = data issue
```

Relaxation rule:

```text
When uncertain between S and C, choose C.
When uncertain between C and B, choose C/B and preserve the branch.
```

## Agent steps

Minimum:

1. activation pass
2. mechanism synthesis

Recommended:

1. activation pass
2. mechanism synthesis
3. secondary expansion pass
4. final integration/report generation

The final report must be generated by a final integration agent, not manually synthesized by the orchestrator. The orchestrator may validate, save, and format the returned report, but the interpretive integration belongs to the agent step.

See [`prompts/`](prompts/) for the exact prompt contracts.

## Discovery-value layer

The reservoir and the final discovery layer are separate.

```text
activation reservoir = preserve plausible readings
discovery ranking = highlight surprising readings
```

This avoids turning the workflow into disambiguation. The system preserves possible readings, then ranks the ones that actually add interpretive force.
