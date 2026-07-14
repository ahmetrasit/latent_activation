# Stage 2 assessment: S100 and S112

## Decisions

| Question | Recommendation | Reason |
| --- | --- | --- |
| Current Pass 1 prompt | Use `stage2_test.md` as the better base, while retaining the main prompt's evidence and Turkish-style constraints. | Its explicit order—complete the passage-scale synthesis before rendering—produces a clearer hierarchy, especially in S112 and in the opening of S100. The advantage is real but modest; neither prompt operationally prevents local, ayah-shaped paragraphs. |
| Pass 2 candidate | Candidate B is better, but it should be revised before adoption. | It distinguishes findings from mechanisms, defines load-bearing work, permits omission of redundant variants, limits growth, and makes paragraphs perform transformations. Candidate A is close to the current follow-up and preserves its central failure: “restore every genuinely distinct mechanism” plus “deepen its existing parent scene” encourages completeness-driven accretion inside an already flattened structure. |
| Where to solve it | Build the architecture in Pass 1 and audit/rebuild it in Pass 2. Do not add a routine Pass 3 yet. | Once Pass 1 has made an ayah-by-ayah essay, a follow-up that treats it as the narrative spine is structurally anchored to the wrong unit. Pass 2 must be allowed to replace that spine. A temporary Pass 3 ablation can test whether architecture-only rewriting rescues existing outputs, but its successful rules should then be folded upstream. |

Candidate B still needs three corrections. “Use the previous synthesis as the narrative spine” must become “use it as an evidence-bearing draft, not a fixed architecture.” “Follow the Quranic sequence closely” must not imply one paragraph per anchor. The complete final replay must select the relations that transform the reading, not quote or paraphrase every ayah again.

## What the outputs show

S100 exposes the same pattern in the primary and comparator runs. Most essays announce a plausible three-part wide view, then devote successive paragraphs to `100:1`, `100:2`, and so on. The final paragraph re-lists the sequence and states the connection. The connections are therefore present as commentary but do not govern how the middle of the essay is built. Pass 2 usually adds or sharpens lexical material without changing this topology. In the primary test branch it also grows from 1,771 to 2,350 words (about 33%), despite the current follow-up's compression language; the main branch contracts, showing that Candidate-A-style wording does not control this behavior reliably.

S112 is a useful control. Its short span, repeated «أَحَدٌ», two positive predicates, paired active/passive birth clauses, and final delayed subject make the macro-axis unusually explicit. All prompt branches can discover “one center, then outward/inward/parallel relations close,” and the test prompt often states it most directly. This means the S100 problem is not merely weak prose or an inability to synthesize. It is a prompt-level weakness that becomes visible when the passage requires an inferred relationship between larger sections rather than an obvious repeated-word closure.

The S100 finding record already contains stronger passage-scale material than the essays exploit architecturally. In `v1/outputs/100/stage1_pass2.md`, F01 gives outside-to-center followed by inside-to-out; F02 and F13 give latent-to-visible-to-knowable and spark-to-disclosure; F05 turns external charge into inner motive; F16 withdraws kinetic agency and reassigns the endpoint to knowledge; F18 identifies three role-complete macroblocks. These can support an earned reading in which the first five ayat enact an operating rule that the human diagnosis and final exposure then apply, reverse, or complete. The exact relation must still be selected from the supplied evidence; it should not be hard-coded as a metaphor or identity.

The existing S108 Pass 3 primary and comparator artifacts reinforce the stage recommendation: they trim their Pass 2 drafts by roughly 8% and 19%, but their bodies still advance mainly anchor by anchor. Another rewrite can improve compression; pass count alone does not create a macroblock relation.

## Cause of the cinematic flattening

1. **Continuous-image bias.** “One progressively unfolding image-system,” inherited participants, and scenes that “never restart” favor one continuous movie. S100 may instead require an enacted model followed by a change of domain, a reversal, and an epistemic completion. Those are relations between scenes, not merely extensions of one scene.
2. **Local-anchor incentives.** Exact first-use quotation and gloss, anchor–dive–return, Quranic order, and “every paragraph” turning on a lexical tension collectively reward one paragraph per word or ayah. The prompt asks for a passage-scale result but evaluates the drafting process locally.
3. **No architecture-selection gate.** The agent never has to compare rival accounts of what each macroblock does for the others, identify cross-block bridges, or reject a merely thematic axis.
4. **Synthesis is deferred to the ending.** Reserving the backward replay without requiring earlier reclassification lets the body remain a gloss sequence. The conclusion then summarizes connections instead of letting later wording change earlier wording at the moment of encounter.
5. **Coverage pressure outranks hierarchy.** Candidate A's recovery obligation and parent-scene rule make omitted findings salient while leaving paragraph structure intact. Distinct literal variants become extra prose even when their shared mechanism is already audible.
6. **The model example is linear.** The S103 example demonstrates accumulation and counter-system formation well, but not analogy, enacted demonstration, domain transfer, or reversal between macroblocks. It cannot by itself teach the relation S100 appears to need.

## Prompting a relational axis without producing a summary

A relational axis should be defined as a transformation, not a topic: an early macroblock establishes an operation with roles and direction; a later block reassigns, applies, reverses, or exposes that operation; the close completes it and changes how the opening is heard. Before drafting, the agent should silently:

1. divide the passage into role-complete macroblocks from grammar, sequence, and findings;
2. form at least two rival axis hypotheses when the evidence permits;
3. require the selected axis to have several independent bridges across macroblocks, with primary meanings, participants, and directions preserved;
4. state what indispensable work each macroblock does for the whole;
5. group findings under those bridges and discard concrete variants that do not alter the selected architecture.

The essay should then stage that axis rather than report the memo. For short surahs, a few transformation-based paragraphs should normally carry several Arabic anchors. A paragraph should advance when the principal operation, domain, participant, direction, or epistemic status changes—not because the next ayah has arrived. Cross-block callbacks should begin in the body as soon as later wording earns them; only the complete replay is reserved for the ending. The ending should enact the changed perception and should not use labels such as “aha,” “mechanism,” “architecture,” or “finding.”

## Test plan

Use identical sacred text, scaffold, annotations, and Stage 1 finding packages within each comparison.

1. **S100, two independent replications:** compare the current test Pass 1, proposed Pass 1, and proposed Pass 1 followed by each of Candidate A, Candidate B, and the proposed Pass 2. To isolate the follow-up, branch the same completed proposed-Pass-1 state if the runner supports checkpoints; otherwise use matched fresh runs and record the limitation. Compare both Pass 1 and Pass 2, not only final polish.
2. **S112, two independent replications:** run the current test and proposed pair as a non-regression control. The new architecture gate should preserve its concise first-«أَحَدٌ»/last-«أَحَدٌ» closure rather than manufacture extra layers.
3. **S108, one primary and one comparator replication:** use the existing finding packages as a compact control for over-architecting a three-ayah passage.
4. **S101, after a matched Stage 1 package exists:** use it as a fresh medium-length stress test with several movements and no S100-specific prompt cues.
5. **Diagnostic only:** apply `stage2_pass3_proposal_v1.md` to the existing S100 Pass 2 drafts. If it repairs the axis without adding evidence, the defect is primarily organization/rendering; incorporate those rules into Pass 1/2 rather than institutionalizing Pass 3.

Blind-score the outputs on five 0–4 scales: axis specificity, cross-block transformation, retrospective reactivation, lexical/grammatical faithfulness, and natural Turkish reader orientation. Apply separate penalties for one-ayah-per-paragraph traversal, finding-shaped catalogs, repeated caveats, unsupported literalization, and meta-announcement of the insight.

Accept the proposal only if:

- in both S100 replications, a reader can state one non-generic whole-passage transformation and cite at least three source-supported cross-block bridges;
- later wording changes the perceived function of an earlier scene before the final paragraph, including a defensible strike/spark-to-disclosure/knowledge path or a better-supported rival;
- Pass 2 normally stays within 10% of Pass 1 length and removes local repetition when adding depth;
- the proposed pair wins the blind architecture/reactivation comparison in both S100 replications without a faithfulness loss; and
- S112 and S108 do not become longer, more abstract, or more speculative merely to satisfy the architecture instruction.
