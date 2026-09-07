# Repeated 29:38 comparison: fresh v1, compact v3, revised v3

The revision recovered the non-dominant counting reading, but did not establish
an overall quality improvement. Fresh v1 also failed to reproduce several of its
historical findings. The evidence now supports a narrower diagnosis: retention
varies within workflows, and particular instructions may shift which connections
survive. It does not support treating the historical v1 output as the stable
output of the v1 workflow.

Six usable Sol/max outputs were produced, two per condition. All passed the
original contract/citation checks without coordinator repair. V3 compilation
preserved every finding and all prose. Two earlier v1 attempts failed before
reading their inputs because the execution host was disabled; those attempts
are retained separately and are not semantic samples.

## What was tested

- **Fresh v1:** original prompt, packet, and schema, with assigned files and an
  enabled execution host. These readers actually queried the packet in sections.
- **Current v3:** exact prior compact Sol prompt and packet, integration on,
  complete inline delivery, tools disabled.
- **Revised v3:** the same v3 evidence and execution, with integration off and
  “Do not collapse a split root to the dominant target only” restored.

Every condition has 69 ayat, 91 focus branches, and 1,902 context branches. The
context inventory is identical at 171,474 bytes. Both v3 conditions use the same
346,065-byte packet; v1 uses its original 328,017-byte packet. See the
[input audit](input-audit.json). The two v3 prompt changes were verified exactly
before launch; this is a bundled recovery test, not a one-variable ablation.

Preparation and the revision were committed as `589e85e4` before the first calls.
The execution-host correction and identical replacement v1 inputs were committed
as `e2c88989` before the replacements. Existing v3 runtime files were the only
untracked files allowed at replacement launch. See [host recovery](host-recovery.json).

## Findings that distinguish the conditions

These counts describe the two new samples per condition, not estimated success
rates. A component can survive without reproducing the complete historical model.

| Finding/component | Fresh v1 | Current v3 | Revised v3 |
|---|---:|---:|---:|
| Uses the non-dominant counting target for عاد | 2/2 | 0/2 | 2/2 |
| Integrates counting with individualized case/accountability | 1/2 | 0/2 | 2/2 |
| Ocular-web branch joined to sight and spider | 0/2 | 2/2 | 1/2 |
| Explicit paired security/belief and misplaced trust in 29:67 | 1/2 | 0/2 | 0/2 |
| Complete fabrication → affection → public obstruction chain | 0/2 | 0/2 | 0/2 |
| Developed crisis/rescue/relapse mechanism | 2/2 | 2/2 | 0/2 |
| Knowing-denial component from 29:49 | 1/2 | 2/2 | 2/2 |

**Counting is the clearest recovery.** Revised outputs cite `root_000989/B001`
at the focus and join it to the distributive “each” and offense in 29:40:
`o03_counted_moral_ledger` and `out_counted_dossier`. Both current-v3 readers stay
with return/recurrence instead. Both fresh v1 readers use the counting target,
although v1 sample 2 develops counted recurrence rather than the complete
offense/outcome ledger. This is consistent with the restored imperative helping,
but integration also changed, so the sentence's separate causal effect remains
unmeasured.

**The revision also loses useful coverage.** Both current-v3 samples develop
crisis clarity and post-rescue relapse. Neither revised sample does. The first
revised sample retains prayer's restraint only as a structural cue and guidance
without the effort-to-guidance converter; the second develops both fully. The
second revised sample omits the ocular-web reading while finding a different
spider/tether analogy. This is a tradeoff, not a clean recovery of v1.

**Fresh v1 changes the interpretation of “regression.”** Neither fresh v1 reader
recovers the complete fabrication/affection/public-obstruction chain or the
ocular-web reading. One misses knowing denial entirely. Conversely, v1 sample 1
does recover the security/belief connection: its citation role explicitly says
the paired occurrence binds felt safety and heart-trust and exposes their
uncoupling. Current v3 mentions sanctuary security and false belief, but does not
explicitly develop that paired-root mechanism; revised v3 omits 29:67 altogether.

**There are worthwhile discoveries in every condition.** Fresh v1 develops
armored discernment in both samples, and one reader activates a non-dominant
guidance branch as barrier-breaking. Current v3 develops worked roads and
hydraulic imagery in both samples; its second sample adds a provision tether
released by trust and a rudder model of maintained direction. Revised v3's first
sample finds the mirror/kohl branch, and its second develops a woven tether and
action-worn roads. These are additional discoveries relative to the historical
v1 output, not necessarily first discoveries anywhere in the project. The
outliers generally distinguish these images from contextual translation and
state their speculative limits.

The first revised output repeats its return and ocular-web mechanisms in both
deltas and outliers. That provides containment in the outlier section but does
not constitute two additional discoveries. Counts below are entry counts.

## Historical-mechanism continuity

**Y:** the defined connection is present. **P:** partial, including meaningful
components developed separately. **—:** absent. This deliberately stricter table
measures continuity with the historical output, not overall correctness or
quality. For example, the complete 29:64/65 salience chain is stricter than the
crisis/relapse component counted above. All finding IDs and reasons for partial
judgments are in [assessment.json](assessment.json), using the
[rubric fixed before generation](rubric.md). Assessment was by the coordinator
and was not blinded to condition.

| Historical mechanism | V1 #1 | V1 #2 | Current #1 | Current #2 | Revised #1 | Revised #2 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Evidence/insight without action | Y | Y | Y | Y | Y | Y |
| Attractive deeds redirect agency | Y | Y | Y | Y | Y | Y |
| Dwellings become testimony | Y | Y | Y | Y | Y | Y |
| Discernment under assay | — | Y | Y | — | Y | — |
| Rival route and liability outsourcing | Y | Y | Y | Y | Y | Y |
| Fabrication–affection–public obstruction | P | P | P | P | P | P |
| Travel/inspection plus retained traces | P | Y | Y | P | P | P |
| False protective architecture | Y | Y | Y | Y | Y | Y |
| Prayer as counter-practice | Y | Y | Y | Y | P | Y |
| Inward knowing denial plus correct acknowledgment | P | P | Y | P | Y | P |
| Distraction–crisis–relapse chain | P | P | P | P | — | — |
| Secure/believe root and misplaced trust | Y | — | P | P | — | — |
| Effort opens plural paths | Y | Y | Y | Y | P | Y |
| Ocular web plus sight and spider | — | — | Y | Y | Y | — |
| Counted case with individualized accountability | Y | P | — | — | Y | Y |

## Execution and artifact quality

| Sample | Entries (baseline + delta + outlier) | Citations | Distinct cited branches / ayat | Seconds | Input tokens | Cached input | Output tokens |
|---|---:|---:|---:|---:|---:|---:|---:|
| [V1 #1](v1-host-1/29_38/response.json) | 17 (3+10+4) | 103 | 68 / 23 | 869.1 | 879,912 | 773,120 | 18,693 |
| [V1 #2](v1-host-2/29_38/response.json) | 15 (3+9+3) | 79 | 52 / 18 | 658.4 | 1,008,903 | 881,664 | 30,289 |
| [Current #1](v3-current-1/29_38/response.json) | 15 (3+9+3) | 96 | 63 / 25 | 528.3 | 105,730 | 0 | 28,978 |
| [Current #2](v3-current-2/29_38/response.json) | 17 (4+9+4) | 101 | 66 / 22 | 749.5 | 105,726 | 0 | 35,907 |
| [Revised #1](v3-revised-1/29_38/response.json) | 15 (3+8+4) | 91 | 50 / 21 | 594.0 | 105,630 | 105,472 | 27,841 |
| [Revised #2](v3-revised-2/29_38/response.json) | 17 (3+10+4) | 105 | 55 / 20 | 654.0 | 105,632 | 0 | 31,700 |

Usage is reported by Codex. V1 totals accumulate input across tool/model steps,
mostly cached; v3 delivers its packet once. Output tokens include reported
reasoning and, for v1, tool-call text. These are not final-prose token counts or
dollar costs. Cache hits differ sharply, and calls ran concurrently, so neither
raw input totals nor these wall times establish a general cost or speed ranking.
The two infrastructure failures are included in the full runtime record but
excluded from this semantic-sample table.

The runtime audit confirms Sol/max, matching base prompts and assignments,
one completed reader session per usable output, and no context compaction.
The fresh v1 readers used 15 and 16 calls to the execution wrapper; v3 used no
tools. V1's assigned input files remained unchanged. V3's compiler preserved
all prose and selected findings exactly, changing only its defined citation,
protocol, and derived-metadata fields. See [runtime.json](runtime.json) and
[validation.json](validation.json). The existing custom v1 validator ran;
an independent general JSON Schema engine did not.

## Updated root-cause assessment and next decision

1. **Within-workflow variation is now observed.** Identical current-v3 linguistic
   inputs recover different subsets, and fresh v1 does too. That does not exclude
   systematic prompt effects. It does mean a single historical v1 result cannot
   establish how reliably v1 produces each connection.
2. **The explicit split-root instruction is a promising correction.** Counting
   appears in both workflows that retain it and neither current-v3 sample. A
   test with integration still on and only that sentence restored is the next
   useful isolation. That configuration is available with `--integration` under
   the new `v1-discovery` prompt revision, but was not run here.
3. **Turning integration off is not established as an improvement.** The revised
   outputs retain fewer distinct branches and lose the developed crisis mechanism,
   while adding counting and other unusual images. Citation breadth is only the
   retained evidence footprint, not an observation of internal search.
4. **Citation salience remains a hypothesis worth testing.** The one explicit
   fresh-v1 security/belief connection notices the paired occurrence in its role.
   V3's resolved pair alone does not produce the same reading. However, citation
   format and execution differ together, and v1's other sample misses it too.
5. **File navigation is not a demonstrated general advantage.** It was actually
   used here, yet fresh v1 lost findings that inline v3 retained. This weakens any
   blanket claim that inline delivery inherently impoverishes discovery.

Keep the frozen-input and citation-compilation machinery. The current revised
default restores the split-root sentence and makes integration opt-in, as agreed;
it remains a candidate configuration with mixed results, not a quality promotion.
The former behavior is reproducible with `--prompt-revision initial --integration`.
Before calling any setting better overall or testing Luna parity, isolate the
sentence with integration on and then check a small unseen set of ayat. No further
model calls were launched beyond this experiment and its documented host recovery.
