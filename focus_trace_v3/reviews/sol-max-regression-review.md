# Independent review: possible HFT v3 discovery regression

- Review profile: `gpt-5.6-sol`, reasoning effort `max`
- Reviewed commit: `da7789b0`
- Focus case: `29:38`, whole-surah 69-ayah window
- Scope: v1, scope-rich v3, and current compact v3 primary artifacts; v2 was not used as an implementation baseline

## Judgment

The current evidence does **not** establish a systematic discovery-quality regression from HFT v1 to v3. It does establish a narrower claim: the single compact-v3 Sol result is not a semantic superset of the historical v1 result, and several of v1's sharpest connections are absent or weakened. At the same time, compact v3 retains most of v1's central mechanisms, adds several useful mechanisms, cites a broader set of branch targets, and is mechanically more reproducible.

My highest-ranked explanation is a one-call selection bottleneck over a very large evidence space. V3's task and packaging changes are plausible influences on which subset is selected, but the present runs do not isolate those influences from ordinary sampling variation. The evidence favors a selection/retrieval problem over lost source data, compilation damage, a conservative-reader regression, or a v2 inheritance problem. There is only one historical v1 result and one run per new condition, so same-condition stochastic variance has not been measured.

Two workflow changes may influence that selection. First, v1 was designed as a file-backed worker task with file operations and an output-compaction/validation workflow, whereas v3 delivers about 106,000 input tokens inline and disables tools. Second, v3's evidence handles reduce lexical rehearsal: the reader returns a compact occurrence ID and branch key instead of spelling out the root and exact word indices, and the prompt weakens one explicit instruction about split roots. These are plausible mechanisms, not demonstrated causes.

## Confirmed facts and exclusions

The historical response first appears with its packet in commit `7d8f07a8` on 2026-07-30. The current [v1 reader prompt](../../focus_trace/prompts/focus_trace_hermetic.md) and [v1 response schema](../../focus_trace/schemas/focus-trace-response.schema.json) are byte-identical to the versions in that commit. The prompt requests Sol/max, and the contemporaneous README prescribes a fresh worker with `fork_context: false`. There is no public launch/runtime receipt for the old `29:38` call, so this establishes the intended profile and task, not the actual historical model snapshot, service envelope, or tool behavior.

The primary semantic artifacts reviewed were the [v1 packet](../../focus_trace/runs/s29/packets/29_38.packet.json) and [v1 response](../../focus_trace/runs/s29/readers/reader_hft_a/29_38.focus_trace.json), the [scope-rich v3 Sol packet](../runs/compare-20260906-sol-max/29_38/packet.json) and [response](../runs/compare-20260906-sol-max/29_38/reader.response.json), and the current [compact-v3 Sol packet](../runs/rerun-20260906-compact-sol-max/29_38/packet.json) and [response](../runs/rerun-20260906-compact-sol-max/29_38/reader.response.json). I consulted the coordinator comparisons only after independently comparing these primary inputs and outputs.

V3 is genuinely based on v1. [V1_BASE.json](../V1_BASE.json) records the copied v1 hashes; [workflow.py](../workflow.py) imports only the local v3 copies of the v1 packet builders and validator. I found no v2 implementation or runtime import. The final v3 ledger schema is byte-identical to v1's. The `83:1` mapping repair does not alter this `29:38` evidence.

Commit `4648eb29` built v3, recorded the first scope-rich runs, restored the compact context projection, and prepared the compact jobs. The compact launch receipts record that exact clean commit before execution. Commit `da7789b0` then records the completed compact results and audits. This order rules out editing the saved compact prompt or packet in response to its generated answer.

For the current compact packet, I independently compared the serialized subtrees:

- `context_root_cues` is byte-identical to v1 at 171,474 compact bytes.
- Both packets contain 69 ayat, 10 focus-root groups, 550 context occurrence groups, 91 focus branches, and 1,902 context branches.
- Focus and context Arabic text, root occurrence content, mapped targets, and branch images used by the v1 findings remain available.
- The packet grows from 328,017 bytes in v1 to 346,065 bytes in compact v3. Most of the increase is 560 added `occurrence_id` fields (10 focus and 550 context groups); focus branches also gain repeated `branch_key` values. V3 removes the duplicate `source_phrases` field beside each focus inventory, but the focus text and each occurrence's surface and lemma remain in `focus_ayah`.

The current [compact Sol launch receipt](../runs/rerun-20260906-compact-sol-max/29_38/launch.json), aggregate [runtime audit](../runs/rerun-20260906-compact/runtime.json), and [validation](../runs/rerun-20260906-compact/validation.json) establish one fresh Sol/max turn, complete inline delivery, no tools, no fallback, no service-tier override, and successful completion. The call used 105,776 input tokens and 36,086 output tokens including 25,449 reasoning tokens. The raw answer was valid and compilation preserved its prose exactly. There is no sign of truncation or a compiler deleting findings.

The output-footprint counters also argue against a simple collapse in what was retained. V1 has 15 entries, 89 citations, 60 distinct root/target/branch selections, and 26 cited ayah refs. Compact-v3 Sol has 17 entries, 116 citations, 72 distinct root/target/branch selections, and the same 26 cited ayah refs. V3 emits findings supported by more distinct branch evidence, but these counters cannot reveal how much evidence the model internally considered and rejected.

## What compact v3 lost, retained, and gained

The comparison below uses the actual model text, not matching titles or entry counts.

| V1 mechanism | Compact-v3 Sol result | Assessment |
|---|---|---|
| Available evidence and inward discernment fail to govern action; attractive valuation of purposive deeds redirects agency | `B01_salience_without_blindness` and `B02_ruins_as_medium` | Retained, with the two v1 baselines partly merged. |
| Insight is placed under behavioral assay | `D01_assayed_finish`, supported by `B01` | Retained but changed. V3 adds a metallic-finish analogy; v1's judgment-to-action transfer is cleaner and more direct. |
| A rival path is marketed with false transfer of its moral load | `D02_social_route_brokerage` | Retained and usefully joined to social belonging. |
| Fabrication at 29:17 becomes affection at 29:25, public normalization and road-cutting at 29:29; the diverted become blockers | `D02` supplies belonging and liability; `D04_diverted_become_blockers` supplies human/public blockage | Partial. `D04` is a clear statement of one component, but it is not stronger than v1's `delta_socialized_obstruction`: the compact result splits the chain and never selects the 29:17 fabrication step. |
| Travel and directed inspection at 29:19-20 turn surviving dwellings/signs into reproducible field evidence | `B02` and `D05_frozen_site_archive` make the site a forensic archive | Partial. The preserved-site mechanism survives, but the travel/inspection bridge is absent. Scope-rich v3 Sol did recover it in `ctx_archaeological_fieldwork`. |
| Dwellings, stasis, protectors, and the weak spider house expose false stability architecture | `B03_habitable_barrier`, `D03_migration_and_rehousing`, and `D07_webbed_security_architecture` | Retained and extended into migration, spatial release, and durable rehousing. |
| Prayer and remembrance inhibit the conduct that beautification reinforces | `D08_competing_inhibitions` | Retained, with a useful inverse-gating formulation. |
| Inward signs, knowing denial, correct acknowledgment, and failed reasoning show knowledge without orientation | `D06_knowledge_orientation_split` | Substantially retained. |
| Distraction governs ordinary salience; danger clarifies; rescue and safety restore the old attachment | `O03_settlement_as_rudder` | Partial and repackaged. Crisis clarity and post-rescue relapse are present, but only inside an exploratory nautical analogy; 29:64's distraction/aimless-action link and v1's general strong delta are absent. Scope-rich v3 Sol retained the general mechanism at medium confidence. |
| At 29:67 the single `ء م ن` occurrence spans secure sanctuary and believing, so correctly seen security collides with trust assigned to falsehood | No compact entry cites 29:67 | Absent. Scope-rich Sol cited the same occurrence as security and folded sanctuary into crisis switching, but did not articulate the shared security/belief root connection. |
| Striving is answered by guidance into plural paths, reversing blocked singular path | `D10_reciprocal_paths` | Retained and joined to the work-as-track image. |
| The peripheral eye-film branch of `س ب ل`, focus sight, and the spider make an optical web | `O02_ocular_web_over_route` | Retained. |
| The non-dominant `ع د د` target under the proper name `عاد` combines with “each” offense/outcome to make a contained case ledger | `O01_aad_return_echo` instead selects the dominant `ع و د` target | Absent. The replacement recurrence reading is coherent but is a different mechanism. |

Useful compact-v3 additions include:

- `B04_work_becomes_track`: repeated deeds wear a rival route, later reversed by effort and guidance in `D10`.
- `D09_sensory_debt`: what is attractive now becomes the conduct whose concealed quality is later enclosed and tasted.
- `D03_migration_and_rehousing`: familiar habitation can stabilize capture, departure reopens space, and reoriented work leads to a different abode.
- `B03`/`D07`: comfortable normality and an intricate shelter can themselves become the load-bearing illusion.
- `D01` and `O03`: coating/assay and rudder analogies. Both are explicitly contained and inventive, though more branch-distant than v1's missing trust and social-chain mechanisms.

This is a mixed quality shift. V1 is more compact and better at a few exact lexical and cross-episode joins. Compact v3 has a wider citation footprint and several strong new functional mechanisms, but spends more of its discovery budget on material analogies. Treating v1's own findings as the gold would overstate regression and systematically ignore v3's additions.

## Ranked diagnosis

### 1. One-call selection bottleneck; stochastic contribution unmeasured — highest-ranked

The reader retains a small set from 1,993 supplied branches and many possible cross-ayah chains. Scope-rich and compact Sol preserve the same core yet emit different secondary findings: scope-rich Sol finds travel/fieldwork, a general crisis switch, and a sanctuary reading; compact Sol loses those as standalone findings but finds coating/assay, sensory debt, and a better-integrated rudder. Compact Luna recovers an optical-web integration that scope-rich Luna missed while losing other material. This demonstrates output sensitivity across changed whole-workflow conditions. Because the inputs and compact prompt wording differ and neither condition was replicated, it does not establish either a scope effect or stochastic variance under identical conditions.

The compact Sol counters show no global reduction in the retained evidence footprint. They say nothing about unobserved internal search. Its omissions are best described at the artifact level as a different retained subset and incomplete integration. One sample per condition cannot tell whether any omission probability actually increased. This is also confounded by the lack of a historical v1 receipt and by possible backend evolution behind the same model alias between July 30 and September 6.

Confidence: high that selective retention is the immediate artifact-level description; unmeasured whether identical-condition randomness, task packaging, or their interaction is the main cause; low confidence about the size of any systematic v3 effect.

### 2. File-backed/tool-mediated work changed to a large inline, no-tool task — plausible and overlooked

V1's prompt says to write the assigned JSON and compact it with `jq` before final validation; its README describes a worker owning an output path and gives the validation command. That design permits active, selective file navigation within the same reader session, potentially across multiple tool/model steps. V3 instead puts the schema and the entire packet into one rendered stdin payload, says “Do not call tools or manage files,” and the launcher disables the shell. This is a real change in the intended reader task, even though both workflows assign the work to one hermetic reader session.

Active file navigation can support repeated searches for a root, a surface form, or a distant ayah without keeping the entire 100k-token payload equally active. An inline reader must internally navigate one long sequence. This could especially affect distant joins such as 29:17 → 29:25 → 29:29 and 29:67's two related forms. It also gives v3 a real gain: the execution is easier to freeze and audit and cannot wander into forbidden files.

There is no old runtime record proving that the historical reader actually used tools or how it paged the files, so this remains a workflow-level hypothesis rather than an established cause.

Confidence: medium plausibility, low direct causal evidence.

### 3. Citation handles reduce lexical rehearsal and weaken two useful imperatives — plausible for the sharpest omissions

V1 requires each citation to repeat `source_ref`, `root`, exact `source_word_indices`, `mapped_root_id`, and `branch_id`. V3 asks for `occurrence_id` and `branch_key`, then derives the former fields offline. This is an excellent correctness improvement, but it changes the reader's attention task. It no longer has to rehearse the root or notice that one occurrence handle expands to multiple surface positions.

The missing 29:67 mechanism is a particularly suggestive example. The packet groups `ءَامِنًا` and `يُؤْمِنُونَ` into one `ء م ن` occurrence with word indices 6 and 12. V1 explicitly cites and interprets that paired occurrence. Scope-rich v3 Sol selects the same occurrence handle but uses it only for sanctuary security. Compact v3 does not select 29:67. The data survived; the lexical relation did not become salient.

The counted-case omission has a second exact prompt change. V1 says, “Do not collapse a split root to the dominant target only.” Current v3 says that all targets are legitimate, “including non-dominant split-root targets,” but drops the prohibition. Both Sol samples remain inside the dominant `ع و د` target and develop return/habit; neither selects the supplied non-dominant `ع د د` target. Scope-rich Luna does select that target, so v3 neither removes nor makes it unusable. The weaker wording may lower its selection probability.

Three smaller changes point in the same direction but have little evidence:

- V3 derives `trigger_roots`, so the reader no longer writes the root set that defines each mechanism.
- V3 removes duplicate `source_phrases` beside focus inventories. This is adjacency loss, not surface-text loss: `focus_ayah` still contains the full ayah, surfaces, lemmas, and roots.
- V1 says not to repeat three named JSON fields. V3's broader “Do not repeat the branch text” could discourage close lexical restatement, although its required `role` still asks for literal and functional contribution and all observed readers do paraphrase branch images.

Confidence: medium for a salience tradeoff, low that it alone explains the result.

### 4. The integration instruction reallocates effort toward new peripheral/material models — plausible tradeoff

The v1 discovery posture and core task remain verbatim. V3 adds [integration.md](../prompts/integration.md), which asks for a revisit of peripheral branches and additional causal, reversal, or material relationships. The compact Sol gains precisely this kind of output: worn tracks, metallic finish, a rudder, shelter architecture, and sensory reversal. Yet it does not integrate the full v1 fabrication/affection/public-blockage chain, and it omits the counted split target and trust collision.

The instruction may be useful while competing for finite reasoning and visible-output budget under the unchanged “not a catalog” constraint. It may also merely reveal ordinary sampling variance. No integration-off v3 result exists, so attribution is premature.

Confidence: medium plausibility, no direct controlled evidence.

### 5. Scope-rich context dilution may have affected the first v3 run, but cannot explain the current gap alone

The scope-rich context inventory is 540,569 bytes versus 171,474 in v1/current compact, and scope-rich Sol used 185,362 input tokens versus 105,776 compact. This can plausibly dilute focus among many longer context branches. It is not the root cause of the remaining compact-v3 omissions: the compact evidence view restores v1's context cues exactly and still loses some v1 mechanisms, while also losing some mechanisms that scope-rich Sol had found.

Confidence: medium for affecting the scope-rich condition, high that it is not a sufficient explanation of compact-v3 behavior.

### 6. Remaining packet overhead, ordering, and platform envelope — low-priority confounds

Compact v3 adds roughly 18 KB to the v1 packet, mainly identifiers on 550 context occurrence groups. It places a 6,768-byte schema before the inline packet and includes ordinary platform developer scaffolding; the audited Sol and Luna platform envelopes are not literally identical. These changes might create small serial-position or compliance effects. They contain no missing linguistic evidence, target interpretation, or prior result, and compact v3's focus-inventory share is not reduced. I would not prioritize them before replication, tool-interface, handle, and integration tests.

## Smallest useful controlled tests

Run these sequentially and stop when the earlier result resolves the question. Score outputs after generation against a preregistered rubric; never show the comparison targets or prior readings to the reader. Include novel grounded findings and unsupported arrows in the rubric so v1 is not treated as unquestioned gold.

1. **Exact replication first.** Run two more fresh compact-v3 Sol/max calls with the exact current prompt, packet, schema, launcher, and platform settings. Together with the existing call this gives three samples. If fieldwork, crisis switching, 29:67, counting, and the social chain appear inconsistently while retained evidence breadth remains similar, that establishes same-condition variability. It would not by itself exclude a systematic v3 effect or establish variability as the primary cause. Two additional calls provide a small initial check, not a reliable estimate of omission rates.

2. **Integration on/off pair.** If the same omissions recur, run at least two fresh compact Sol/max calls with integration on and two with `--no-integration`, keeping everything else byte-identical. Compare retention of ordinary lexical/cross-episode mechanisms, number and quality of peripheral material analogies, and integrated-versus-fragmented chains. This directly tests whether the added revisit trades breadth for a particular style of novelty.

3. **Two lexical-salience micro-tests.** First, hold everything fixed and change only one sentence: restore v1's exact “Do not collapse a split root to the dominant target only.” Use at least two fresh calls per condition and score non-dominant-target use without telling the readers which target matters. If that changes selection, test handles separately: fix the split-root wording in both conditions and compare current handles against citations that also expose `root` and exact `source_word_indices` (or human-readable handles containing them). Pre-register repeated-root and split-target opportunities across `29:38` and a small unseen set. Keeping these as two A/Bs avoids attributing an effect to the wrong part of a bundled prompt change.

4. **Inline versus file-navigation pair.** Only if the first three leave a stable deficit, give fresh Sol/max readers identical prompt, schema, packet, and evidence, varying only delivery: one complete inline/no-tool payload versus read-only file access with search/read tools and a separate output path. Do not expose repository history or prior outputs. Record tool calls. This tests whether active evidence navigation, rather than prompt semantics, accounts for v1-like cross-linking.

Repeating scope-rich versus compact is lower priority. The existing pair already rules out scope bloat as the sole cause, and it costs about 80,000 extra input tokens per Sol call. Likewise, testing only the `source_phrases` duplicate or only the “branch text” wording is premature; both are smaller salience changes nested inside the more informative handle test.

## Practical conclusion

Keep the compact v3 provenance, compilation, and validation architecture. Those are real gains, and neither the compiler nor the evidence projection caused the observed omissions. Do not claim v3 semantic parity or regression from this case yet. Replicate the exact current condition, then test the two task changes most capable of altering discovery: active file navigation and lexical rehearsal around occurrence/split-root handles. If a prompt adjustment is made before broader testing, restoring v1's explicit split-root prohibition is the smallest neutral correction; it asks the reader to examine supplied alternatives without naming any desired `29:38` reading.
