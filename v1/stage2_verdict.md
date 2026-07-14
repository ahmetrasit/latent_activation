# Stage 2 prompt-design diagnosis and verdict

## Executive verdict

Stage 2 has one underlying hierarchy problem that appears in two opposite forms.

- In S100, the prose contains many valid local mechanisms but does not let a passage-scale relation govern the body. It announces a wide view, then walks ayah by ayah and saves the strongest synthesis for a final recap.
- In S108 and, to a lesser extent, S112, the passage-scale relation is found early. The failure comes afterward: later passes keep reopening lexical branches, multiplying secondary images, and expanding an already sufficient insight.

The workflow therefore should not use one undifferentiated rendering procedure for every short surah. The recommended design is a two-mode Stage 2 prompt family:

1. **Full macroblock mode** for passages with positive evidence of several role-complete movements, domain transfer, reversal, or major changes of participant, voice, agency, time, scale, or epistemic status. S100 is the reference case. Use the architecture-first v1 Pass 1 and the revised Candidate-B-style v1 Pass 2.
2. **Lightweight compact mode** for passages whose unity is carried mainly by one sequence, one hinge, and one backward-working closure. S108 and S112 are the reference cases. Use the short-surah v2 Pass 1 and compression-focused v2 Pass 2.

The current `stage2_test.md` is the better Pass 1 foundation because it explicitly completes synthesis before rendering. Candidate B is the better Pass 2 foundation because it groups findings by mechanism, permits omission, and controls growth. Neither should be adopted unchanged: the test prompt still lacks a mode gate, and Candidate B's instruction to preserve the previous narrative spine can lock in an ayah-by-ayah structure.

Do not add a routine production Pass 3. A third rewrite can compress, but the existing S108 Pass 3 outputs show that pass count does not reliably correct structural selection. Retain the v1 Pass 3 only as a temporary full-mode diagnostic. No short-mode Pass 3 is recommended.

## Scope and evidence

This verdict is based on:

- the Stage 2 boundary and current follow-up in `v1/spec.md`;
- the active main and test Pass 1 prompts;
- primary and comparator S100 Pass 1/Pass 2 main and test outputs;
- primary and comparator S112 Pass 1/Pass 2 main and test outputs;
- S108 main, test, pilot, sol-max, and available Pass 3 families in the primary and comparator directories;
- the prior proposal files and assessments under `v1/prompts/`; and
- a narrow check of the S100 Stage 1 consolidated models, especially F01, F02, F05, F13, F16, and F18 in `v1/outputs/100/stage1_pass2.md`.

No external lexical, theological, or interpretive source was used for this prompt-design verdict.

## Quantitative pattern

Word count does not measure synthesis quality by itself, but the direction of change exposes the follow-up's incentives.

| Passage and branch | Pass 1 → Pass 2 words | Approximate change | Structural result |
| --- | ---: | ---: | --- |
| S100 primary main | 2,359 → 2,071 | −12% | Better compression, but the body remains largely local and sequential. |
| S100 primary test | 1,771 → 2,350 | +33% | Coverage recovery overwhelms the stronger compact Pass 1 hierarchy. |
| S100 comparator main | 1,139 → 1,199 | +5% | Same axis, modest lexical expansion, same local traversal. |
| S100 comparator test | 1,211 → 1,280 | +6% | Same pattern. |
| S108 primary main | 1,396 → 2,122 | +52% | The compact axis is already known; Pass 2 adds image families and caveats. |
| S108 primary test | 1,397 → 1,516 | +9% | Less severe, but still no new passage-level recognition. |
| S108 primary pilot | 1,604 → 1,941 | +21% | More lexical texture, not a new organizing relation. |
| S108 comparator main | 892 → 1,207 | +35% | A clear compact draft becomes more elaborate. |
| S108 comparator test | 907 → 1,190 | +31% | Same. |
| S108 comparator pilot | 728 → 997 | +37% | The strongest compact baseline is weakened by expansion. |
| S108 comparator sol-max | 1,035 → 1,256 | +21% | Additional capacity does not remove the coverage incentive. |
| S108 comparator test sol-max | 1,221 → 1,342 | +10% | Same axis with more exposition. |
| S112 primary main | 1,191 → 1,070 | −10% | Useful compression; the axis was already explicit. |
| S112 primary test | 1,094 → 1,008 | −8% | Useful compression; no architecture rebuild was needed. |
| S112 comparator main | 762 → 829 | +9% | Small expansion around an already complete closure. |
| S112 comparator test | 715 → 734 | +3% | Essentially stable. |

S108 outputs commonly contain roughly ten to twenty-four reader-facing text blocks despite having only three ayat. The additional blocks often explain water or cloud flow, pastoral feeding, animal anatomy, bodily front/back relations, rivalry, covenant, social memory, or related limitations. These branches can be authorized as lexical material yet still be unnecessary to the dominant synthesis. Functional coverage and reader-facing inclusion are not the same thing.

## Core diagnosis

### 1. The current prompt specifies a passage-scale goal but rewards local drafting

The instructions combine exact first-use quotation, immediate glossing, anchor–dive–return, Quranic order, paragraph-level lexical tension, and broad finding coverage. The safest way for an agent to satisfy all of these is one local explanatory unit at a time. “Passage-scale” becomes an introductory claim and a concluding recap rather than the principle that selects and sizes the body.

### 2. “One progressively unfolding image-system” is too narrow

Some passages are well described by one continuing image. S100 may not be. Its first five ayat can function as an enacted operating model: force becomes audible and visible, enters a center, and leaves effects by which an unseen source is inferred. The human diagnosis then reassigns force and direction to an inner attachment; the final movement reverses entry into exposure, withdraws human agency, and ends with the inner-knowing subject. Treating these as merely successive scenes understates their relation.

At the opposite extreme, S108 does not need a large image-system at all. It has a compact relational arc. Forcing “architecture” onto it creates scale that the primary grammar does not require.

### 3. The current Pass 2 treats omission as suspicious

Candidate-A-style language asks the agent to restore every distinct omitted mechanism inside its parent scene. This has two effects:

- it preserves the existing paragraph topology even when that topology is the problem; and
- it makes every unused strong or medium finding feel like reader-facing debt.

S100 needs permission to replace the topology. S108 and S112 need permission to leave most findings silent after the hinge and closure are clear.

### 4. Backward reactivation is often deferred and then inventoried

The prompt asks for a final replay, so agents commonly postpone the strongest relation until the end and then quote or paraphrase the entire passage again. An earned recognition should begin when the later hinge appears. The ending should complete that transformation, not announce it or enumerate every recovered anchor.

### 5. Secondary projections lack a passage-sensitive budget

The outputs usually preserve caveats, but repeated caveats do not prevent over-architecture. A remote image can remain technically qualified while still dominating reader attention. Short passages need a much stricter selection rule: normally no more than two brief secondary projections in the whole essay, with no chain of inferred objects or events.

### 6. The workflow needs structural routing, not a raw ayah threshold

S112 has four ayat yet a strong internal progression. S100 has eleven ayat and three clearly differentiated movements. Length is useful but insufficient. The deciding question is whether one closure hinge accounts for most of the reactivation, or whether several independently developed fields must be related.

## Passage-level verdicts

### S100: full macroblock mode

The S100 Stage 1 record already supports a stronger synthesis than the prose architecture displays:

- F01: outside-to-center followed by inside-to-out;
- F02/F13: latent-to-visible-to-knowable and spark-to-larger disclosure;
- F05: external charge becoming internal motive;
- F16: kinetic agency withdrawing while contents become focal and knowledge is reassigned;
- F18: three role-complete macroblocks.

The earned recognition should not be “all the ayat involve movement or disclosure.” It should make the opening perform indispensable work for what follows. A defensible account is that the first five ayat train perception on how hidden force becomes legible through breath, strike, spark, dust, and center-entry; the middle reveals an analogous but non-identical force in the human's severed and tightened relations; the close reverses the direction, brings buried and chest contents outward, and transfers the endpoint from human self-witness to the Lord's interior knowledge. The exact selected axis may differ, but it must explain the function of all three movements with several independent anchors.

This requires the v1 full procedure: macroblock identification, rival-axis testing when evidence permits, a bridge map, and a Pass 2 that can discard the previous narrative spine.

### S108: lightweight compact mode

The S108 recognition is already carried by primary grammar and a small number of hinges:

- «إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ» establishes completed giving, source, recipient, and abundant gift;
- «فَـ» in «فَصَلِّ» makes prayer and sacrifice a response rather than an unrelated command;
- «لِرَبِّكَ» gives that response its direction;
- «هُوَ» fixes «ٱلْأَبْتَرُ» on the hater rather than the addressee;
- the close makes the opening abundance newly audible as a gift within an enduring source–recipient–Lord relation, while attempted diminishment is reassigned.

That is enough for an earned insight. «وَٱنْحَرْ» must remain prayer-adjacent sacrifice, and the hater must never become a literal sacrificial victim. Water, cloud, pastoral, anatomical, contest, and covenant projections may be individually authorized but are normally unnecessary. A compact essay should choose at most one or two if they materially sharpen the relation.

### S112: lightweight compact mode

S112's closure supplies its own compact architecture:

- «قُلْ» opens a speech whose content is completed by the whole surah;
- «هُوَ ٱللَّهُ أَحَدٌ» names the referent and predicates unity;
- «ٱللَّهُ ٱلصَّمَدُ» repeats the name and establishes the depended-on center;
- «لَمْ يَلِدْ وَلَمْ يُولَدْ» closes the same birth relation in active and passive directions;
- «كُفُوًا» widens the final exclusion to equivalence;
- final «أَحَدٌۢ», under negation and as the delayed subject, returns the opening word with a changed function: positive “one” becomes the exclusion of “anyone” as an equal.

The essay does not need multiple rival architectures. The main danger is materializing «ٱلصَّمَدُ» as a literal solid or sealed body, or repeating the same outward/inward/parallel closure in too many formulations.

## Prompt verdicts

### Current main versus current test Pass 1

The test prompt is the better base. Its explicit sequence—evidence units, interlocking relations, passage-scale synthesis, then rendering—creates a clearer hierarchy. In S112 it often produces the most direct first-«أَحَدٌ»/last-«أَحَدٌ» account; in S100 its opening wide view is generally cleaner and shorter.

The main prompt still contributes useful constraints: strict evidence policy, exact Arabic quotation, natural Turkish, reader orientation, and protection of primary contextual meaning. These should remain in both proposed modes.

### Candidate A versus Candidate B Pass 2

Candidate B is superior because it:

- distinguishes findings from the mechanisms they jointly perform;
- defines load-bearing change operationally;
- states that omission is not automatically a defect;
- sets a length ceiling;
- makes paragraphs carry transformations; and
- limits weak or remote imagery.

Candidate B nevertheless needs one central change for full mode: the previous essay cannot be mandatory narrative spine. It must be an evidence-bearing draft that may be reorganized. For short mode, Candidate B is still too recovery-oriented; the correct follow-up is primarily a compactness and closure edit.

## Recommended prompt family

| Use case | Pass 1 | Pass 2 | Pass 3 |
| --- | --- | --- | --- |
| Full macroblock passages such as S100 | `v1/prompts/stage2_pass1_proposal_v1.md` | `v1/prompts/stage2_pass2_proposal_v1.md` | Diagnostic only: `v1/prompts/stage2_pass3_proposal_v1.md` |
| Compact passages such as S108/S112 | `v1/prompts/stage2_pass1_proposal_v2_short.md` | `v1/prompts/stage2_pass2_proposal_v2_short.md` | None |

The detailed short-mode rationale and gate are in `v1/prompts/stage2_short_surah_assessment_v2.md`.

## Routing rule

Route to lightweight mode when all or nearly all of these are true:

1. The passage is commonly two to six ayat.
2. One stable discourse situation or referent chain carries most of the text.
3. The primary sequence can be stated in one plain sentence.
4. One contrast, repetition, conjunction, pronoun, paired construction, or delayed word performs most of the backward reactivation.
5. There is no independently developed opening field that later wording applies, reverses, or reassigns in a different domain.

Route to full mode when there is positive evidence of several role-complete movements, substantial changes in participant or voice, a major agency or temporal shift, an early enacted model, or multiple independent cross-section bridges. When uncertain, default to lightweight mode and escalate only on positive structural evidence. Rich source notes alone are not evidence of a complex passage architecture.

Keep the variants separate during evaluation. A universal prompt that contains both full and short instructions risks allowing the heavier architecture vocabulary to leak into short outputs. A universal dispatcher can be considered only after routing is validated on more passages.

## Pass responsibilities

### Full Pass 1

- establish primary movement and role-complete macroblocks;
- compare plausible cross-block axes;
- choose the axis with the strongest independent support;
- group findings by function within that axis;
- render transformations rather than finding-shaped paragraphs.

### Full Pass 2

- treat the old essay as revisable evidence-bearing draft;
- audit and, if necessary, replace the macro-axis;
- recover only omitted mechanisms that change the architecture;
- pay for added depth by compression;
- keep normal length between roughly 90% and 105% of Pass 1 and below 110%.

### Compact Pass 1

- state the primary sequence internally in one sentence;
- select one compact relation, one hinge, and one backward-working closure;
- use no rival-axis or macroblock exercise when that suffices;
- normally use zero to two brief secondary projections;
- aim for four to six substantive paragraphs and about 450–850 Turkish words.

### Compact Pass 2

- preserve the successful compact axis by default;
- repair primary gloss, hinge, participant, direction, or closure only when necessary;
- omit rather than recover redundant findings;
- compress to roughly 75–95% of Pass 1 and never grow;
- let one final paragraph perform both closure and replay.

## Acceptance protocol

### Experimental matrix

1. **S100 full-mode stress test:** two matched primary and comparator replications of current test versus v1 full Pass 1/Pass 2. Branch the same Pass 1 state across current Candidate A, Candidate B, and proposed full Pass 2 when possible.
2. **S108 compact-mode test:** two matched primary and comparator replications of current test versus v2 short Pass 1/Pass 2. Compare against the strongest compact existing control, `v1/outputs/108_comparator/stage2_pilot_pass1.md`.
3. **S112 compact non-regression:** two matched primary and comparator replications against `v1/outputs/112_comparator/stage2_test_pass1.md` and the current test pair.
4. **Routing test:** the gate must select compact mode for S108 and S112 and full mode for S100 without being told those expected labels.
5. **Fresh validation:** after these pass, add at least one compact surah and one medium-length multi-movement surah not used to design the prompts.

### Blind scoring

Score each output from 0–4 on:

- primary lexical and grammatical fidelity;
- compact or macro-scale axis specificity, as appropriate;
- later-to-earlier reactivation;
- reader orientation and natural Turkish;
- selection and compression discipline.

Faithfulness is a veto, not a score that can be averaged away. Apply explicit penalties for unsupported participant identity, false causal sequence, literalized secondary imagery, finding catalogs, repeated caveats, one-root-per-paragraph rendering, and meta-announcement of the insight.

### Passage-specific success tests

- **S100:** a blind reader can state one non-generic three-movement transformation and cite at least three independent cross-block anchors. At least one relation must become perceptible before the final paragraph.
- **S108:** a blind reader can state how giving becomes directed response and how «هُوَ» reassigns cut-off status; the hater is not made a victim of «وَٱنْحَرْ», and no secondary scene is needed to understand the result.
- **S112:** a blind reader can explain the changed role of final «أَحَدٌۢ», the two directions of the birth pair, and the broader equivalence closure without treating «ٱلصَّمَدُ» materially.

### Shape thresholds

- S108: normally 450–750 words and four to six substantive paragraphs.
- S112: normally 550–850 words and four to six substantive paragraphs.
- Compact Pass 2: no growth over Pass 1.
- Full Pass 2: normally no more than 10% growth and only for a missing passage-scale mechanism.
- No output should add a final inventory after the closure has already performed the replay.

## Final decision

Approve the v1 full-mode and v2 compact-mode proposals for controlled evaluation, not immediate activation. The central production change should be routing by structural complexity and changing the unit of coverage from findings to reader-perceptible mechanisms.

Promotion to active status should require:

1. two successful matched replications on S100, S108, and S112;
2. zero faithfulness regressions;
3. successful blind routing on all three;
4. no Pass 2 growth in compact mode;
5. a clear pairwise preference for the proposed output on reactivation and prose unity; and
6. non-regression on one fresh compact and one fresh multi-movement passage.

The principal unresolved question is empirical rather than conceptual: whether the lightweight word/image budget retains enough lexical richness across a broader compact-surah sample. That is a test requirement, not a blocker to creating or evaluating the proposals. Active prompt and specification files should remain unchanged until those tests pass.
