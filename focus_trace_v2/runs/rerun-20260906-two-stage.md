# 29:38 two-stage Sol/Luna rerun

Workflow commit `7612cccc` was committed and pushed before these runs started.
The two-stage implementation and v1 reporting contract were unchanged during
generation. The only added reader instruction prohibited using existing outputs
from earlier runs or other agents, while permitting the same reader's own
discovery notes for its ledger pass. No comparison hints or corrective feedback
were supplied. No headroom checks were performed after the user requested that
they stop; orchestration continued without modifying the packet.

## Execution and acceptance

Both profiles were explicit: `gpt-5.6-sol / max` and `gpt-5.6-luna / max`.
Each completed exactly two turns in its own original session, with no context
compaction. No service-tier argument, fallback, semantic repair, or coordinator
retry was used. The discovery requests were identical; their base prompts
differed only in the model profile. The ledger follow-ups were identical.

Both received the full 937,494-byte packet, byte-identical to the previous
restored-v1 one-pass 29:38 packet. Source evidence was not pruned. Each follow-up
used the packet and notes already present in that reader's conversation.

| Profile | Discovery notes → final findings | Branch citations resolving | Acceptance failure |
|---|---:|---:|---|
| Sol max | 46 → 46 (8 baseline, 29 delta, 9 outlier) | 245 / 245 | Three context deltas have extra `trigger_roots` without corresponding non-focus branch citations. |
| Luna max | 58 → 58 (7 baseline, 41 delta, 10 outlier) | 262 / 279 | 36 trigger-root list mismatches; 16 incomplete occurrence-index lists; one root absent from the cited ayah. |

Both final responses are schema-valid and account for every discovery ID without
withdrawal. ID coverage does not mechanically prove semantic preservation.
Both failed final acceptance and **neither was exported**. The model outputs
remain unchanged apart from the agreed formatting-only compaction of final JSON;
the original model messages remain in the stage event files. Those event files
contain final agent messages, not the private session reasoning logs.

Sol's three list mismatches are:

- `delta_clarity_creates_liability`: extra `ب ي ن`;
- `delta_distributed_evidence_media`: extra `ع ل م`;
- `delta_crisis_clarity_and_relapse`: extra `ع ل م`.

Luna's occurrence-index failures supply only a subset of the packet's grouped
indices, rather than the complete occurrence record. For example, several
findings cite only one occurrence of `ح م ل` at 29:12. Its nonoccurring-root error
is `ر ء ي` at 29:61 in `delta_29_61_creator_acknowledged`. This is a citation
error, not evidence that the packet lost a root occurrence. The original v1
compact-response validator also requires `trigger_roots` to match non-focus
activation-trace roots (`focus_trace/scripts/validate_focus_trace.py`); this
acceptance rule was not introduced for the pilot.

Full per-stage usage counters, session/profile checks, hashes, and every
diagnostic are in [the runtime record](rerun-20260906-two-stage.runtime.json).
These counters are not a price calculation or evidence of a cheaper workflow.

## Sol interim review, performed after the ledger follow-up

The coordinator read Sol's explicit discovery notes only after sending its neutral
ledger follow-up. This review was not sent to either reader. Comparison targets
were original v1's `focus_trace/runs/s29/readers/reader_hft_a/29_38.focus_trace.json`
and the prior [restored-v1 one-pass Sol response](rerun-20260906-v1-sol-max/29_38/response.json).

Retained/recovered findings:

- Optical web: `outlier_webbed_vision` retains the `س ب ل` eye-film branch beside
  `مستبصرين` and the spider of 29:41. The counted-case reading also survives.
- Knowing denial: 29:47–49 now explicitly supports possessed clarity alongside
  active denial. The previous one-pass Sol response lacked that specific bridge.
- Security and misattributed trust: 29:67 returns as a distinct reading in which
  experienced safety is recruited as apparent proof of a self-sustaining false
  social order. This is related to, but not verbatim recovery of, v1's especially
  explicit security/believing shared-root mechanism.

Newly retained candidates relative to both earlier Sol outputs:

| Candidate | Packet anchor | Change in the focus reading |
|---|---|---|
| Cosmetic treatment of vision | `ص د د / root_000848 / B013`, mirror-prepared kohl, alongside adornment and sight | The perceiving eye is cosmetically treated; blockage and beautification become one exploratory operation. The branch itself does not assert perceptual distortion. |
| Deeds wear their own road | `ع م ل / root_001046 / B011`, the traveled/worn road | Repeated practice establishes an attractive rival route, not just an obstacle beside the way. |
| Sight intact, steering compromised | `س ك ن / root_000726 / B008`, a ship's rudder, with ships at 29:15/65 | Functioning sight can coexist with failed directional control; this is a contained, form-distant navigation analogy. |

The inventory also gains tethering, deceptive textile, public clamor, and
hydraulic-route candidates. More notes are not automatically better discoveries.
All these branches were already available in the previous one-pass v2 packet;
they were not new evidence added for this run.

Remaining omissions or less-integrated mechanisms in the notes:

- V1's 29:17 → 29:25 → 29:29 synthesis—fabricated value, affection/belonging,
  public normalization, then road-blocking—is distributed across separate notes,
  not explicitly rebuilt as that causal chain. Its ingredients are present.
- The previous one-pass response explicitly kept merely self-ascribed/ironic
  perceptiveness as an alternative. The discovery notes predominantly assume
  genuine insight that fails to govern conduct.

The final Sol response retains the three illustrated new candidates and the
optical-web reading. The selected fabrication, institutional-support, and public
obstruction entries still remain separate. Its final uncertainty summary names
worldly acumen, but not the earlier merely self-ascribed/ironic alternative.
This spot-check is not a full semantic-equivalence audit of every retained ID.

The pilot supports a broader discovery result for Sol, not an unqualified v1
superset, production acceptance, causal proof of the two-stage design's advantage,
or a settled Sol/Luna quality comparison.

## Preserved run artifacts

- [Sol notes](rerun-20260906-two-stage-sol-max/29_38/discovery.json)
- [Sol ledger — unaccepted](rerun-20260906-two-stage-sol-max/29_38/response.json)
- [Luna notes](rerun-20260906-two-stage-luna-max/29_38/discovery.json)
- [Luna ledger — unaccepted](rerun-20260906-two-stage-luna-max/29_38/response.json)
