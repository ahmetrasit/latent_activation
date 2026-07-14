# S102 Stage 1 Pass 2 - Temporally Conditioned Reactivation

Assigned passage: S102, ayat 1-8.

Sacred Arabic text source: `resources/quran/surah_102.json`.

Permitted primary resources inspected:

- `resources/quran/surah_102.json`: available.
- `resources/attachments.tsv`: available; rows filtered to S102:1-8.
- `resources/qac.sqlite`: unavailable as a usable database; zero bytes and no schema returned.
- `resources/furuq_v4.sqlite`: unavailable as a usable database; zero bytes and no schema returned.

Root cause of Pass 1 limitation: the required QAC and furuq v4 SQLite databases are empty local files. Therefore QAC word/morpheme tables and uncontaminated furuq branch dossiers cannot be queried. I did not use substitute local TSV files because Stage 1 permits only the listed primary resources. No lexical branch IDs, branch images, or `what_is_ar` prose are fabricated below.

## Sacred Text Sequence

Opening context:

- 102:0 `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`

Assigned interval:

1. 102:1 `أَلْهَىٰكُمُ ٱلتَّكَاثُرُ`
2. 102:2 `حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ`
3. 102:3 `كَلَّا سَوْفَ تَعْلَمُونَ`
4. 102:4 `ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ`
5. 102:5 `كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ`
6. 102:6 `لَتَرَوُنَّ ٱلْجَحِيمَ`
7. 102:7 `ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ`
8. 102:8 `ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ`

## Recoverable Rooted Occurrence Registry

Because QAC is unavailable, this registry is recovered only from `attachments.tsv` S102 rows. It is sufficient to identify affected lexical roots, occurrences, and some form tags, but not sufficient to enumerate furuq branch IDs.

| occurrence | surface | root from attachment row | form tag / part | structural note |
| --- | --- | --- | --- | --- |
| 102:1:1 | أَلْهَىٰكُمُ | ل ه و | PV | governs object suffix كُم and subject ٱلتَّكَاثُرُ |
| 102:1:2 | ٱلتَّكَاثُرُ | ك ث ر | GERUND | subject naming what diverted them |
| 102:2:2 | زُرْتُمُ | ز و ر | PV | complement of حَتَّىٰ |
| 102:2:3 | ٱلْمَقَابِرَ | ق ب ر | NOUN_TIME_PLACE | direct object of زُرْتُمُ |
| 102:3:2 | سَوْفَ | س و ف | FUT_PART | future particle complement relation |
| 102:3:3 | تَعْلَمُونَ | ع ل م | IV | future verbal complement |
| 102:4:3 | سَوْفَ | س و ف | FUT_PART | repeated future particle complement relation |
| 102:4:4 | تَعْلَمُونَ | ع ل م | IV | repeated future verbal complement |
| 102:5:2 | لَوْ | ل و ي | CONDITION_PART | governs conditional verbal clause |
| 102:5:3 | تَعْلَمُونَ | ع ل م | IV | conditional knowledge verb |
| 102:5:4 | عِلْمَ | ع ل م | GERUND | cognate accusative qualifying تَعْلَمُونَ |
| 102:5:5 | ٱلْيَقِينِ | ي ق ن | GERUND | genitive mudaf ilayh of عِلْمَ |
| 102:6:2 | لَتَرَوُنَّ | ر أ ي | IV | seeing verb with explicit object |
| 102:6:3 | ٱلْجَحِيمَ | ج ح م | NOUN_CONCRETE | object seen |
| 102:7:3 | لَتَرَوُنَّهَا | ر أ ي | IV | seeing verb with object suffix هَا |
| 102:7:4 | عَيْنَ | ع ي ن | NOUN_ABSTRACT | accusative adverbial expression |
| 102:7:5 | ٱلْيَقِينِ | ي ق ن | GERUND | genitive mudaf ilayh of عَيْنَ |
| 102:8:3 | لَتُسْـَٔلُنَّ | س أ ل | IV_PASS | passive questioning verb |
| 102:8:4 | يَوْمَئِذٍ | ي و م | NOUN_ABSTRACT | temporal adverbial |
| 102:8:6 | ٱلنَّعِيمِ | ن ع م | GERUND | governed by عَنِ as question topic |

## Blocked Lexical Branch Seed Audit

Stage 1 requires each accepted uncontaminated branch of each passage root to initiate its own seed pass. The branch source `resources/furuq_v4.sqlite` is empty and has no schema, so accepted branch IDs are unrecoverable. The following lexical seed families are therefore blocked, not rejected.

For each row, the intended seed set is: every uncontaminated furuq v4 branch for that occurrence/root, if the database were available.

| blocked lexical seed family | occurrence | root | status | limitation |
| --- | --- | --- | --- | --- |
| LEX-001 | 102:1:1 أَلْهَىٰكُمُ | ل ه و | blocked | no furuq branch IDs/images available |
| LEX-002 | 102:1:2 ٱلتَّكَاثُرُ | ك ث ر | blocked | no furuq branch IDs/images available |
| LEX-003 | 102:2:2 زُرْتُمُ | ز و ر | blocked | no furuq branch IDs/images available |
| LEX-004 | 102:2:3 ٱلْمَقَابِرَ | ق ب ر | blocked | no furuq branch IDs/images available |
| LEX-005 | 102:3:2 سَوْفَ | س و ف | blocked | no furuq branch IDs/images available; particle usage remains available structurally |
| LEX-006 | 102:3:3 تَعْلَمُونَ | ع ل م | blocked | no furuq branch IDs/images available |
| LEX-007 | 102:4:3 سَوْفَ | س و ف | blocked | no furuq branch IDs/images available; repeated particle usage remains available structurally |
| LEX-008 | 102:4:4 تَعْلَمُونَ | ع ل م | blocked | no furuq branch IDs/images available |
| LEX-009 | 102:5:2 لَوْ | ل و ي | blocked | no furuq branch IDs/images available; conditional function remains available structurally |
| LEX-010 | 102:5:3 تَعْلَمُونَ | ع ل م | blocked | no furuq branch IDs/images available |
| LEX-011 | 102:5:4 عِلْمَ | ع ل م | blocked | no furuq branch IDs/images available |
| LEX-012 | 102:5:5 ٱلْيَقِينِ | ي ق ن | blocked | no furuq branch IDs/images available |
| LEX-013 | 102:6:2 لَتَرَوُنَّ | ر أ ي | blocked | no furuq branch IDs/images available |
| LEX-014 | 102:6:3 ٱلْجَحِيمَ | ج ح م | blocked | no furuq branch IDs/images available |
| LEX-015 | 102:7:3 لَتَرَوُنَّهَا | ر أ ي | blocked | no furuq branch IDs/images available |
| LEX-016 | 102:7:4 عَيْنَ | ع ي ن | blocked | no furuq branch IDs/images available |
| LEX-017 | 102:7:5 ٱلْيَقِينِ | ي ق ن | blocked | no furuq branch IDs/images available |
| LEX-018 | 102:8:3 لَتُسْـَٔلُنَّ | س أ ل | blocked | no furuq branch IDs/images available |
| LEX-019 | 102:8:4 يَوْمَئِذٍ | ي و م | blocked | no furuq branch IDs/images available |
| LEX-020 | 102:8:6 ٱلنَّعِيمِ | ن ع م | blocked | no furuq branch IDs/images available |

Blocked lexical result: no lexical-branch-generated synthesis units can be honestly produced. All findings below are therefore seeded from actual constructions, morphosyntax, temporal exposure, repetition, and attachment rows. `selected_branches` is empty for every recoverable candidate.

## Candidate Synthesis Units

### S102-P2-C01 - Diversion With a Named Occupying Subject

- `candidate_id`: S102-P2-C01
- `ayah_range`: 102:1
- `seed_type`: constructional / morphosyntactic
- `seed`: `أَلْهَىٰكُمُ ٱلتَّكَاثُرُ`, with object suffix كُم governed by أَلْهَىٰ and ٱلتَّكَاثُرُ as nominative subject.
- `generating_set`: (E: attachment `ae:v3:s102:001:pass1:attach:a1`, كُم object suffix of أَلْهَىٰ); (E: attachment `ae:v3:s102:001:pass1:attach:a2`, ٱلتَّكَاثُرُ subject naming what diverted them); (E: sequence 102:1 opens with addressee as acted-upon object before naming the acting subject).
- `selected_branches`: none; branch resource unavailable.
- `constructed_model`: The recitation begins with the hearers already seized as the object of an operation. Only after the attached pronoun is heard does the source of diversion arrive: competitive increase/multiplication. The image is not a neutral theme of abundance; it is a force that occupies the addressee and displaces attention before the addressee has acted in the discourse.
- `freeze_point`: after 102:1, before using 102:2-8.
- `predictions_at_freeze`: a limit or terminus for the diversion; a later reversal in which the passive/acted-upon hearer becomes exposed to knowledge, sight, or accounting; possible reactivation of the initial object suffix near closure.
- `unused_features_tested`: 102:2 حَتَّىٰ temporal limit; 102:2 graves as endpoint; 102:3-5 repeated knowing; 102:6-7 seeing; 102:8 passive questioning and topic ٱلنَّعِيمِ.
- `corroborators`: (C: attachment `ae:v3:s102:002:pass1:attach:a1`, حَتَّىٰ subordinates the visit span as a temporal limit); (C: 102:8 passive `لَتُسْـَٔلُنَّ` returns the addressee to being acted upon); (C: attachment `ae:v3:s102:008:pass1:attach:a2`, ٱلنَّعِيمِ is the topic complement of questioning and reactivates the initial increase/benefit field structurally without using lexical branches).
- `constraints`: (K: no lexical branch for ل ه و or ك ث ر is available; this image rests on syntax, word order, and sacred text only); (K: 102:1 does not by itself specify the moral content of التكاثر beyond its role as diverter).
- `temporal_reactivation_notes`: The final questioning about ٱلنَّعِيمِ retrospectively sharpens the opening diversion: what occupied the addressee becomes the domain about which the addressee is asked.
- `rival_models`: A weaker rival treats 102:1 as only a thematic announcement, but it explains less of the object-first grammar and final passive return.
- `grade`: medium-strong
- `grade_rationale`: Strong structural evidence from attachment and sequence; lexical branch specificity is unavailable, preventing a stronger grade.
- `source_queries_or_rows_used`: sacred text 102:1-8; attachment rows `ae:v3:s102:001:pass1:attach:a1`, `a2`, `ae:v3:s102:002:pass1:attach:a1`, `ae:v3:s102:008:pass1:attach:a2`.

### S102-P2-C02 - Temporal Limit: Diversion Runs Until Graves

- `candidate_id`: S102-P2-C02
- `ayah_range`: 102:1-2
- `seed_type`: constructional / temporal
- `seed`: `حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ`
- `generating_set`: (E: attachment `ae:v3:s102:002:pass1:attach:a1`, حَتَّىٰ subordinates `زُرْتُمُ ٱلْمَقَابِرَ` as a temporal limit); (E: attachment `ae:v3:s102:002:pass1:attach:a2`, ٱلْمَقَابِرَ direct object of زُرْتُمُ); (E: sequence 102:1 to 102:2, diversion followed immediately by its limit).
- `selected_branches`: none; branch resource unavailable.
- `constructed_model`: The opening occupation is not merely intense; it is temporally stretched until a boundary object appears. The graves function structurally as the reached terminus of the diversion span, not as a later unrelated scene.
- `freeze_point`: after 102:2.
- `predictions_at_freeze`: after reaching the limit, the passage should interrupt or reverse the state; the boundary should activate knowledge of what had been missed; later evidence may become judicial or perceptual because a terminal visit has exposed an endpoint.
- `unused_features_tested`: 102:3 and 102:4 `كَلَّا سَوْفَ تَعْلَمُونَ`; 102:5 conditional knowledge; 102:6-7 seeing; 102:8 questioning on that day.
- `corroborators`: (C: 102:3 begins with `كَلَّا`, an abrupt negating/rebuking interruption after the limit); (C: repeated future knowledge in 102:3-4 matches delayed recognition after the reached boundary); (C: attachment `ae:v3:s102:008:pass1:attach:a1`, يَوْمَئِذٍ provides a later temporal location for accounting after the limit).
- `constraints`: (K: the attachment row only licenses a temporal limit, not a full metaphysical model of death); (K: no ق ب ر or ز و ر branch imagery can be cited).
- `temporal_reactivation_notes`: 102:8 `يَوْمَئِذٍ` reactivates the endpoint logic of 102:2: after the limit is reached, there is a "then/that day" of questioning.
- `rival_models`: A local-only model sees 102:2 as a simple end of first sentence; it fails to explain why the later future knowledge and final day strongly echo the limit structure.
- `grade`: medium-strong
- `grade_rationale`: The attachment and sequence evidence are specific and predictive; lexical dossiers are unavailable.
- `source_queries_or_rows_used`: sacred text 102:1-8; attachment rows `ae:v3:s102:002:pass1:attach:a1`, `a2`, `ae:v3:s102:008:pass1:attach:a1`.

### S102-P2-C03 - Repeated Future Knowledge as Delayed Disclosure

- `candidate_id`: S102-P2-C03
- `ayah_range`: 102:3-4
- `seed_type`: temporal/acoustic / constructional
- `seed`: repeated `كَلَّا سَوْفَ تَعْلَمُونَ`, with 102:4 adding `ثُمَّ`.
- `generating_set`: (E: sacred text repetition 102:3 and 102:4); (E: attachment `ae:v3:s102:003:pass1:attach:a1`, سَوْفَ marks تَعْلَمُونَ as future complement); (E: attachment `ae:v3:s102:004:pass1:attach:a1`, same future relation repeated); (E: sequence, 102:4 repeats after `ثُمَّ`).
- `selected_branches`: none; branch resource unavailable.
- `constructed_model`: The first interruption does not close the matter. It creates a deferred knowledge event. The second, delayed by `ثُمَّ`, restarts the same formula, making knowledge not a single correction but an approaching disclosure with at least two waves.
- `freeze_point`: after 102:4.
- `predictions_at_freeze`: an intensification from future knowledge into a more determinate mode; a distinction between merely being told/knowing and being exposed; possible later repetition in another sensory channel.
- `unused_features_tested`: 102:5 `لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ`; 102:6-7 `لَتَرَوُنَّ`; 102:7 `ثُمَّ`; 102:8 `ثُمَّ` and questioning.
- `corroborators`: (C: attachment `ae:v3:s102:005:pass1:attach:a2`, `عِلْمَ ٱلْيَقِينِ` is an accusative masdar expression qualifying تَعْلَمُونَ, intensifying knowledge); (C: 102:6-7 shifts from knowing to seeing, satisfying prediction of determinate exposure); (C: repeated `ثُمَّ` in 102:7 and 102:8 extends staged disclosure).
- `constraints`: (K: without QAC, detailed morphology of the emphatic forms cannot be audited beyond attachment rows); (K: no ع ل م branch dossier can support a specific lexical image).
- `temporal_reactivation_notes`: 102:5 re-enters the knowledge root/form from the repeated formula and changes the future warning into a conditional standard of certainty.
- `rival_models`: The repetition may be rhetorical emphasis only; the later certainty and seeing sequence make a staged-disclosure model stronger than bare emphasis.
- `grade`: medium
- `grade_rationale`: Good temporal and repetition evidence; weaker because its lexical depth is blocked.
- `source_queries_or_rows_used`: sacred text 102:3-8; attachment rows `ae:v3:s102:003:pass1:attach:a1`, `ae:v3:s102:004:pass1:attach:a1`, `ae:v3:s102:005:pass1:attach:a2`.

### S102-P2-C04 - Conditional Knowledge of Certainty as the Missing State

- `candidate_id`: S102-P2-C04
- `ayah_range`: 102:5
- `seed_type`: constructional / morphosyntactic
- `seed`: `لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ`
- `generating_set`: (E: attachment `ae:v3:s102:005:pass1:attach:a1`, لَوْ governs the verbal clause headed by تَعْلَمُونَ); (E: attachment `ae:v3:s102:005:pass1:attach:a2`, عِلْمَ ٱلْيَقِينِ is a cognate accusative/masdar expression qualifying تَعْلَمُونَ); (E: attachment `ae:v3:s102:005:pass1:attach:a3`, ٱلْيَقِينِ is genitive as mudaf ilayh of عِلْمَ).
- `selected_branches`: none; branch resource unavailable.
- `constructed_model`: After two future warnings, the passage opens a counterfactual/conditional slot: if the addressees had the knowledge characterized by certainty, the prior diversion would already be reorganized. The missing condition is not simply information but a stabilized mode of knowing.
- `freeze_point`: after 102:5, before using 102:6-8.
- `predictions_at_freeze`: a consequence should follow that manifests or verifies the certainty; the next event may turn knowledge into encounter; a later phrase may pair certainty with a different modality.
- `unused_features_tested`: 102:6 `لَتَرَوُنَّ ٱلْجَحِيمَ`; 102:7 `عَيْنَ ٱلْيَقِينِ`; 102:8 questioning.
- `corroborators`: (C: 102:6 immediately supplies a seeing event); (C: attachment `ae:v3:s102:007:pass1:attach:a2`, عَيْنَ ٱلْيَقِينِ is an adverbial expression modifying seeing); (C: attachment `ae:v3:s102:007:pass1:attach:a3`, ٱلْيَقِينِ repeats as mudaf ilayh, pairing certainty with a second construction).
- `constraints`: (K: this is a constructional certainty model, not a lexical claim about ي ق ن beyond the available idafa relation); (K: the conditional syntax does not by itself say whether the condition is impossible, absent, or admonitory).
- `temporal_reactivation_notes`: `عَيْنَ ٱلْيَقِينِ` in 102:7 reactivates `عِلْمَ ٱلْيَقِينِ` in 102:5, preserving certainty while changing the access mode from knowledge expression to eye/direct seeing expression.
- `rival_models`: A knowledge-only model fails to predict the immediate visualization in 102:6-7.
- `grade`: medium-strong
- `grade_rationale`: Strong constructional support from cognate accusative/idafa and later repeated certainty phrase; lexical branch support unavailable.
- `source_queries_or_rows_used`: sacred text 102:5-7; attachment rows `ae:v3:s102:005:pass1:attach:a1`, `a2`, `a3`, `ae:v3:s102:007:pass1:attach:a2`, `a3`.

### S102-P2-C05 - From Knowledge to Seeing: Exposure Becomes Visual

- `candidate_id`: S102-P2-C05
- `ayah_range`: 102:5-7
- `seed_type`: temporal/acoustic / constructional
- `seed`: transition from `تَعْلَمُونَ / عِلْمَ` to `لَتَرَوُنَّ / لَتَرَوُنَّهَا`
- `generating_set`: (E: 102:5 repeated knowledge root/form from sacred text and attachment rows); (E: attachment `ae:v3:s102:006:pass1:attach:a1`, ٱلْجَحِيمَ is the object seen by لَتَرَوُنَّ); (E: attachment `ae:v3:s102:007:pass1:attach:a1`, هَا suffix in لَتَرَوُنَّهَا is object pronoun governed by the repeated seeing verb).
- `selected_branches`: none; branch resource unavailable.
- `constructed_model`: The warning escalates from future knowing to direct seeing. First the object is named, then the same object is carried forward by pronoun. This creates a temporary visual field: what was only a deferred disclosure becomes an object of encounter, then a re-seen object with a more precise manner.
- `freeze_point`: after 102:7.
- `predictions_at_freeze`: after perception, an accountability or response phase should follow; the seen object may not be the final topic because the opening diversion still needs to be judged.
- `unused_features_tested`: 102:8 passive questioning; 102:8 temporal adverbial; 102:8 topic ٱلنَّعِيمِ; opening 102:1 التكاثر.
- `corroborators`: (C: 102:8 shifts from seeing to being questioned, matching a post-exposure response phase); (C: attachment `ae:v3:s102:008:pass1:attach:a1`, يَوْمَئِذٍ is temporal adverbial of questioning, anchoring accountability after exposure); (C: attachment `ae:v3:s102:008:pass1:attach:a2`, ٱلنَّعِيمِ is the topic complement, returning to the domain of enjoyed increase rather than the seen object alone).
- `constraints`: (K: no lexical branch for ر أ ي, ج ح م, or ع ي ن is available); (K: the pronoun هَا is syntactically tied to the seen object, but the attachment row alone does not identify its antecedent; the immediately prior ٱلْجَحِيمَ is the passage-local antecedent by sequence).
- `temporal_reactivation_notes`: The named object in 102:6 is reactivated as a pronoun in 102:7, allowing the phrase `عَيْنَ ٱلْيَقِينِ` to modify an already established visual object.
- `rival_models`: A pure escalation model from threat to threat ignores the pronoun continuity and the later shift away from جحيم to نعيم as question topic.
- `grade`: medium
- `grade_rationale`: Good sequence and attachment evidence; some anaphora detail cannot be fully audited without QAC.
- `source_queries_or_rows_used`: sacred text 102:5-8; attachment rows `ae:v3:s102:006:pass1:attach:a1`, `ae:v3:s102:007:pass1:attach:a1`, `ae:v3:s102:008:pass1:attach:a1`, `a2`.

### S102-P2-C06 - Two Certainty Constructions: Knowledge-Certainty to Eye-Certainty

- `candidate_id`: S102-P2-C06
- `ayah_range`: 102:5-7
- `seed_type`: constructional / morphosyntactic
- `seed`: parallel idafa phrases `عِلْمَ ٱلْيَقِينِ` and `عَيْنَ ٱلْيَقِينِ`
- `generating_set`: (E: attachment `ae:v3:s102:005:pass1:attach:a2`, عِلْمَ ٱلْيَقِينِ qualifies تَعْلَمُونَ); (E: attachment `ae:v3:s102:005:pass1:attach:a3`, ٱلْيَقِينِ genitive after عِلْمَ); (E: attachment `ae:v3:s102:007:pass1:attach:a2`, عَيْنَ ٱلْيَقِينِ adverbial modifying seeing); (E: attachment `ae:v3:s102:007:pass1:attach:a3`, ٱلْيَقِينِ genitive after عَيْنَ).
- `selected_branches`: none; branch resource unavailable.
- `constructed_model`: The passage repeats certainty as the fixed genitive pole while changing the governing noun. Certainty first qualifies knowledge, then qualifies eye/direct sight. The relational model is a transfer of the same certainty-standard across two modes of access.
- `freeze_point`: after 102:7.
- `predictions_at_freeze`: if certainty has been stabilized through knowledge and sight, closure should not introduce a third epistemic mode but should move to consequence/accountability.
- `unused_features_tested`: 102:8 `لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ`.
- `corroborators`: (C: 102:8 moves to questioning, a consequence/accountability mode, not another certainty idafa); (C: يَوْمَئِذٍ ties that consequence to the staged prior disclosure).
- `constraints`: (K: without branch dossiers, no claim is made about the lexical range of ي ق ن or ع ي ن); (K: `عَيْنَ` is used only as the attachment row licenses it: an accusative adverbial expression, not an independently elaborated lexical image).
- `temporal_reactivation_notes`: The second idafa reactivates the first by preserving `ٱلْيَقِينِ` and replacing `عِلْمَ` with `عَيْنَ`, converting earlier failed/missing certainty into direct confrontation.
- `rival_models`: The phrases may be separate idioms; the shared genitive, close placement, and knowledge-to-seeing sequence make a linked model more explanatory.
- `grade`: medium-strong
- `grade_rationale`: Very specific constructional parallelism; branch images unavailable, so grade remains below strong.
- `source_queries_or_rows_used`: sacred text 102:5-8; attachment rows `ae:v3:s102:005:pass1:attach:a2`, `a3`, `ae:v3:s102:007:pass1:attach:a2`, `a3`.

### S102-P2-C07 - Final Question Reactivates the Opening Occupation

- `candidate_id`: S102-P2-C07
- `ayah_range`: 102:1-8
- `seed_type`: temporal/acoustic / verified composite from constructions
- `seed`: 102:8 `لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ`
- `generating_set`: (E: attachment `ae:v3:s102:008:pass1:attach:a1`, يَوْمَئِذٍ temporal adverbial of تُسْـَٔلُنَّ); (E: attachment `ae:v3:s102:008:pass1:attach:a2`, ٱلنَّعِيمِ governed by عَنِ as topic complement); (E: passive verbal form tag IV_PASS from attachment row); (E: sequence, final ayah after diversion, graves, knowledge, certainty, seeing).
- `selected_branches`: none; branch resource unavailable.
- `constructed_model`: Closure does not occur at seeing the blaze. The passage closes only when the addressee is placed under questioning about نعيم. This reactivates the opening: the thing that diverted through competitive increase is judged through the enjoyed/favored domain named at the end.
- `freeze_point`: after reading 102:8 as seed, before re-testing earlier passage.
- `predictions_at_freeze`: earlier material should include a misused or distracting good; the addressee should have been grammatically positioned as acted upon before being questioned; the sequence should have deferred full recognition until after exposure.
- `unused_features_tested`: 102:1 object suffix and التكاثر; 102:2 limit; 102:3-5 knowledge; 102:6-7 seeing.
- `corroborators`: (C: attachment `ae:v3:s102:001:pass1:attach:a1`, كُم object suffix begins with addressee acted upon); (C: attachment `ae:v3:s102:001:pass1:attach:a2`, التكاثر names the diverting subject and supplies an opening domain that the final نعيم can interrogate structurally); (C: 102:6-7 seeing supplies the exposure before questioning); (C: 102:3-5 future/conditional knowledge supplies the deferred recognition).
- `constraints`: (K: no ن ع م or ك ث ر branch branches can be cited, so the نعيم/تكاثر relation is structural and thematic from sacred text, not branch-derived); (K: final question is about ٱلنَّعِيمِ, not explicitly about ٱلتَّكَاثُرُ, so the relation is reactivation rather than identity).
- `temporal_reactivation_notes`: This is the strongest backward reactivation in the recovered data: the final prepositional topic `عَنِ ٱلنَّعِيمِ` sends attention back to the first named diverter `ٱلتَّكَاثُرُ`.
- `rival_models`: A punishment-only model ends at 102:6-7 and treats 102:8 as addendum; it cannot explain why closure is postponed until نعيم.
- `grade`: medium-strong
- `grade_rationale`: Strong closure and reactivation structure; lexical branch confirmation unavailable.
- `source_queries_or_rows_used`: sacred text 102:1-8; attachment rows `ae:v3:s102:008:pass1:attach:a1`, `a2`, `ae:v3:s102:001:pass1:attach:a1`, `a2`.

### S102-P2-C08 - Object Pronoun Arc: You Are Seized, Then You Are Questioned

- `candidate_id`: S102-P2-C08
- `ayah_range`: 102:1-8
- `seed_type`: morphosyntactic / temporal
- `seed`: initial object suffix كُم in `أَلْهَىٰكُمُ` and final passive `لَتُسْـَٔلُنَّ`
- `generating_set`: (E: attachment `ae:v3:s102:001:pass1:attach:a1`, كُم suffix is object pronoun governed by أَلْهَىٰ); (E: attachment `ae:v3:s102:008:pass1:attach:a1`, يَوْمَئِذٍ adverbial of passive questioning verb); (E: attachment row form tag IV_PASS for `لَتُسْـَٔلُنَّ`).
- `selected_branches`: none; branch resource unavailable.
- `constructed_model`: The addressee is introduced as an object affected by diversion. At closure, the addressee again undergoes an event, now questioning. Between those endpoints, knowledge and sight are imposed in stages. The hearer is not primarily an autonomous narrator of events but the one being moved through exposure into accountability.
- `freeze_point`: after pairing 102:1 and 102:8 endpoints.
- `predictions_at_freeze`: intervening discourse should show externally imposed transitions rather than voluntary reform; it should include future certainty markers and perception events.
- `unused_features_tested`: 102:3-7 future knowledge and seeing; 102:2 limit.
- `corroborators`: (C: repeated `سَوْفَ تَعْلَمُونَ` places knowledge in the future rather than present control); (C: 102:6-7 emphatic seeing forms impose perception after knowledge); (C: 102:2 حَتَّىٰ sets an externally recognized limit).
- `constraints`: (K: QAC morphology is unavailable, so only attachment row morphology is used); (K: this model does not decide whether the addressee is morally passive; it only tracks grammatical patienthood and imposed exposure).
- `temporal_reactivation_notes`: The final passive questioning reactivates the initial object suffix as an arc of being acted upon: diverted, brought to a limit, made to know, made to see, questioned.
- `rival_models`: A simple second-person address model accounts for addressee continuity but not the object/passive endpoint symmetry.
- `grade`: medium
- `grade_rationale`: Good morphosyntactic arc, but some morphology is unavailable and lexical branches are absent.
- `source_queries_or_rows_used`: sacred text 102:1-8; attachment rows `ae:v3:s102:001:pass1:attach:a1`, `ae:v3:s102:008:pass1:attach:a1`.

### S102-P2-C09 - Named Object to Pronoun: The Visual Field Is Held Across Ayat

- `candidate_id`: S102-P2-C09
- `ayah_range`: 102:6-7
- `seed_type`: morphosyntactic / temporal
- `seed`: `لَتَرَوُنَّ ٱلْجَحِيمَ` followed by `ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ`
- `generating_set`: (E: attachment `ae:v3:s102:006:pass1:attach:a1`, ٱلْجَحِيمَ is direct object of seeing); (E: attachment `ae:v3:s102:007:pass1:attach:a1`, هَا suffix is object pronoun of the repeated seeing verb); (E: sequence, object named before object pronominalized).
- `selected_branches`: none; branch resource unavailable.
- `constructed_model`: The first seeing names the object. The second seeing keeps that object active by suffix, then adds the `عَيْنَ ٱلْيَقِينِ` manner. This creates an activation packet that is not merely "see X twice"; it is "establish X, then hold X in view under intensified certainty."
- `freeze_point`: after 102:7.
- `predictions_at_freeze`: closure should not need to rename the same object; it should move to a consequence after the object has been visually stabilized.
- `unused_features_tested`: 102:8 questioning and نعيم topic.
- `corroborators`: (C: 102:8 does not rename ٱلْجَحِيمَ, supporting the closure shift after visual stabilization); (C: final questioning introduces a new topic domain rather than extending the object chain).
- `constraints`: (K: antecedent assignment is sequence-based; the attachment row confirms object suffix but not antecedent resolution); (K: no ج ح م or ر أ ي branches can be used).
- `temporal_reactivation_notes`: The second seeing reactivates the named object from the prior ayah without repeating its noun.
- `rival_models`: The pronoun could be treated as generic anaphora only; the repeated seeing verb and immediate sequence make it a retained visual field.
- `grade`: medium
- `grade_rationale`: Specific syntactic evidence for object/pronoun continuity, with limited lexical depth.
- `source_queries_or_rows_used`: sacred text 102:6-8; attachment rows `ae:v3:s102:006:pass1:attach:a1`, `ae:v3:s102:007:pass1:attach:a1`.

### S102-P2-C10 - Three-Stage Exposure: Limit, Knowledge, Sight, Question

- `candidate_id`: S102-P2-C10
- `ayah_range`: 102:1-8
- `seed_type`: temporal/acoustic / verified composite from constructions
- `seed`: whole passage order as progressive exposure
- `generating_set`: (E: 102:1 diversion construction); (E: 102:2 حَتَّىٰ temporal limit construction); (E: 102:3-5 repeated knowledge and certainty constructions); (E: 102:6-7 seeing constructions); (E: 102:8 questioning construction).
- `selected_branches`: none; branch resource unavailable.
- `constructed_model`: The passage unfolds as an enforced exposure sequence. First the addressee is occupied by increase. Then the occupation reaches the graves. Then future knowledge is announced twice and sharpened into knowledge of certainty. Then the object of dread is seen and re-seen with eye-certainty. Finally the addressee is questioned about نعيم, returning the whole sequence to the opening occupation.
- `freeze_point`: after assembling constructions C01-C07, before using repetition and closure as corroboration.
- `predictions_at_freeze`: repetition should mark stages rather than random emphasis; closure should explain why seeing is not the final ayah; initial and final domains should connect.
- `unused_features_tested`: repeated `كَلَّا`; repeated `ثُمَّ`; repeated future particles; repeated certainty genitive; final `عَنِ ٱلنَّعِيمِ`.
- `corroborators`: (C: repeated `ثُمَّ` at 102:4, 102:7, 102:8 marks staged progression); (C: repeated certainty genitive binds knowledge and sight stages); (C: final topic `ٱلنَّعِيمِ` explains closure beyond seeing); (C: opening `ٱلتَّكَاثُرُ` is reactivated by final نعيم topic structurally).
- `constraints`: (K: no branch-generated image can be claimed; this is a structural synthesis); (K: because branch evidence is absent, this composite must not be upgraded to a lexical synthesis).
- `temporal_reactivation_notes`: The main reactivation path is 102:8 back to 102:1, with sub-reactivations 102:7 back to 102:6 and 102:7 back to 102:5.
- `rival_models`: A linear warning model explains sequence but less strongly explains why final questioning is about نعيم rather than جحيم.
- `grade`: medium-strong
- `grade_rationale`: The full passage order, repeated operators, attachment rows, and closure reactivation converge; lexical branch evidence unavailable.
- `source_queries_or_rows_used`: sacred text 102:1-8; all S102 attachment rows listed above.

### S102-P2-C11 - `ثُمَّ` as Staged Re-Opening, Not Mere Continuation

- `candidate_id`: S102-P2-C11
- `ayah_range`: 102:4, 102:7, 102:8
- `seed_type`: temporal/acoustic
- `seed`: repeated `ثُمَّ` before renewed warning, renewed seeing, and final questioning.
- `generating_set`: (E: sacred text `ثُمَّ` at 102:4 before repeated future knowledge); (E: sacred text `ثُمَّ` at 102:7 before second seeing); (E: sacred text `ثُمَّ` at 102:8 before final questioning).
- `selected_branches`: none; branch resource unavailable.
- `constructed_model`: `ثُمَّ` repeatedly reopens the scene after an apparently sufficient disclosure. First knowledge is repeated; then seeing is repeated; then questioning comes after sight. The temporal operator prevents premature closure.
- `freeze_point`: after identifying the three `ثُمَّ` positions.
- `predictions_at_freeze`: each `ثُمَّ` should precede an escalation or new stage, not a redundant restatement.
- `unused_features_tested`: 102:4 repeated `كَلَّا سَوْفَ تَعْلَمُونَ`; 102:7 pronoun plus `عَيْنَ ٱلْيَقِينِ`; 102:8 passive questioning about نعيم.
- `corroborators`: (C: 102:4 repeats warning after `ثُمَّ`, making knowledge staged); (C: 102:7 repeats seeing with pronoun and eye-certainty, making perception staged); (C: 102:8 introduces questioning, a new accountability stage).
- `constraints`: (K: no attachment rows for `ثُمَّ`; evidence is from sacred text sequence only); (K: it cannot specify the duration of delay).
- `temporal_reactivation_notes`: Each `ثُمَّ` pulls a prior event forward and re-presents it under added force: know again, see again, then answer.
- `rival_models`: Treating `ثُمَّ` as simple conjunction misses the repeated placement before escalations.
- `grade`: medium
- `grade_rationale`: Clear recurrence and placement, but no attachment or lexical branch support for the particle.
- `source_queries_or_rows_used`: sacred text 102:4, 102:7, 102:8.

### S102-P2-C12 - `كَلَّا` as Repeated Inhibitor of the Diversion State

- `candidate_id`: S102-P2-C12
- `ayah_range`: 102:3-5
- `seed_type`: temporal/acoustic
- `seed`: repeated `كَلَّا` at 102:3, 102:4, 102:5.
- `generating_set`: (E: sacred text `كَلَّا` immediately after the diversion-to-graves unit); (E: sacred text repeated `كَلَّا` before future knowledge and conditional certainty).
- `selected_branches`: none; branch resource unavailable.
- `constructed_model`: After the diversion reaches its limit, `كَلَّا` repeatedly inhibits the activated state. It blocks the opening trajectory from being accepted as stable, then couples each inhibition with knowledge language.
- `freeze_point`: after 102:5.
- `predictions_at_freeze`: the inhibited state should be replaced by forced disclosure; later lines should show exposure rather than additional worldly increase.
- `unused_features_tested`: 102:6-7 seeing of جحيم; 102:8 questioning about نعيم.
- `corroborators`: (C: 102:6-7 replace diversion with visual exposure); (C: 102:8 final question about نعيم evaluates the domain rather than extending the initial increase).
- `constraints`: (K: no lexical/morphological dossier for `كَلَّا`; its role is taken only from repeated placement as sacred-text particle); (K: this seed cannot independently produce the whole model without the surrounding constructions).
- `temporal_reactivation_notes`: Each `كَلَّا` restarts the negation of the opening state and keeps the hearer from settling into the prior diversion.
- `rival_models`: Pure rhetorical rebuke is possible; the repeated pairing with knowledge makes inhibitory disclosure more specific.
- `grade`: medium
- `grade_rationale`: Strong positional recurrence but no branch or attachment data.
- `source_queries_or_rows_used`: sacred text 102:3-5.

## Terminated and Weak Seeds

These constructional or temporal seeds were initiated but did not produce independent synthesis beyond the candidates above:

- `حَتَّىٰ` alone: retained only as part of C02. Alone it gives temporal limit but no separate image without its complement. Grade: unlikely as independent synthesis.
- `سَوْفَ` alone at 102:3 and 102:4: retained only as part of C03. Alone it marks futurity but does not generate a complete model. Grade: weak as independent synthesis.
- `لَوْ` alone at 102:5: retained only as part of C04. Alone it opens a conditional construction but requires the knowledge/certainty complement. Grade: weak as independent synthesis.
- `عَنِ` alone at 102:8: retained only as part of C07. Alone it marks topic complement but does not generate a passage model. Grade: weak as independent synthesis.
- Basmala opening context: available as recitational opening context but not used as generating evidence. No recovered candidate required naming, invocation, mercy, or divine-source corroboration. Grade: no independent seed permitted.

## Convergence Notes

The recoverable evidence converges on a compact structural trajectory:

```text

diverted addressee
  -> temporal limit at graves
  -> repeated inhibited warning
  -> missing knowledge-certainty
  -> forced seeing and eye-certainty
  -> final questioning about نعيم
  -> reactivation of the opening diversion by التكاثر

```

This is not a lexical-branch synthesis, because branch dossiers are unavailable. It is a constructional and temporal synthesis from sacred text and S102 attachment rows.

## Image Packet Catalog

IMAGE_ID: S102-IMG-01

- Starting seed: 102:1 `أَلْهَىٰكُمُ ٱلتَّكَاثُرُ`
- Complete image: an addressee occupied by competitive increase until a boundary is reached, then forced through knowledge, sight, and questioning.
- Passage-order assembly: 102:1 diversion; 102:2 limit; 102:3-5 knowledge; 102:6-7 sight; 102:8 questioning.
- Participants and roles: addressee as object/patient; التكاثر as diverting subject; المقابر as limit object; الجحيم as seen object; النعيم as final question topic.
- Operation / mechanism: displacement of attention followed by staged exposure and accountability.
- Direction / force / medium: forward temporal pressure from diversion to limit, then backward reactivation from final نعيم to initial تكاثر.
- Temporal development: until graves; then repeated future knowing; then conditional certainty; then emphatic seeing; then final questioning on that day.
- Outcome / closure: closure occurs only when نعيم is questioned, not when جحيم is seen.
- Exact branch constituents: none available; furuq branch database empty.
- Unfilled roles: lexical branch images for every rooted occurrence remain blocked.
- Status: FRAGMENT structurally coherent, lexically incomplete.

IMAGE_ID: S102-IMG-02

- Starting seed: 102:5-7 certainty constructions.
- Complete image: certainty is transferred from knowledge to eye/direct seeing.
- Passage-order assembly: `عِلْمَ ٱلْيَقِينِ`; `لَتَرَوُنَّ ٱلْجَحِيمَ`; `عَيْنَ ٱلْيَقِينِ`.
- Participants and roles: addressee as knower/seer; certainty as shared genitive pole; جحيم as visual object.
- Operation / mechanism: epistemic escalation from knowledge phrase to sight phrase.
- Direction / force / medium: from cognitive mode to visual mode.
- Temporal development: repeated warnings, conditional knowledge, named seeing, pronominal re-seeing.
- Outcome / closure: after seeing, discourse moves to questioning.
- Exact branch constituents: none available; furuq branch database empty.
- Unfilled roles: lexical branches for ع ل م, ي ق ن, ر أ ي, ج ح م, ع ي ن.
- Status: FRAGMENT structurally coherent, lexically incomplete.

## Exhaustiveness Check

- Every rooted occurrence recoverable from permitted S102 attachment rows has been listed.
- Every affected lexical branch seed family has been marked blocked rather than omitted.
- No branch ID or branch image has been fabricated.
- All S102 attachment rows were considered as potential structural evidence.
- Constructional seeds were initiated for the major recoverable attachments: object suffix, subject relation, حَتَّىٰ complement, direct objects, future particle complements, لو conditional complement, cognate accusative, idafa pairs, seeing object/pronoun, adverbial certainty phrase, temporal adverbial, and عن complement.
- Temporal/acoustic seeds were initiated for the major recoverable sequence features: repeated `كَلَّا`, repeated `سَوْفَ تَعْلَمُونَ`, repeated `ثُمَّ`, knowledge-to-seeing escalation, named-object-to-pronoun reactivation, and final closure reactivation.
- The output remains limited because the permitted lexical databases are empty; this is recorded as a resource limitation, not treated as evidence against the passage roots.
