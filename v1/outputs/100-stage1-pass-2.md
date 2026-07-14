# S100 Stage 1 Pass 2 - temporally conditioned reactivation

## Scope

Assigned passage: S100:1-11.

Sacred Arabic text source: `resources/quran/surah_100.json`.

Opening context: `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`. The basmala is retained as recitational opening context only and generates no seed.

## Root Cause For Limited Word Coverage

The limitation was not an interpretive choice. The two Stage 1 resources that normally provide exhaustive lexical seed coverage are empty in this workspace:

- `resources/qac.sqlite`: 0 bytes. Therefore QAC schema, word table, morpheme table, rooted-word inventory, lemmas, measures, and morpheme-level morphology are unavailable.
- `resources/furuq_v4.sqlite`: 0 bytes. Therefore uncontaminated branch images, branch IDs, and `what_is_ar` dossiers are unavailable.

The recoverable resource is `resources/attachments.tsv`, whose S100 rows provide structural evidence, some surface forms, attachment roots/form tags, and syntactic reasons. Because the prompt forbids fabrication, no lexical branch ID or branch image is invented below. All lexical branch seed lanes are marked blocked. Recoverable Pass 2 work proceeds only from the sacred text, S100 attachment rows, and temporal/acoustic sequence.

## Source Rows Used

- Sacred text: `resources/quran/surah_100.json`, verses 0-11.
- Attachment rows: `awk -F '\t' 'NR==1 || ($5==100 && $6>=1 && $6<=11)' resources/attachments.tsv`.
- QAC: unavailable, zero-byte database.
- Furuq v4: unavailable, zero-byte database.

## Rooted Occurrence Inventory From Available Attachment Rows

This is not a QAC morpheme inventory. It is the maximal rooted occurrence inventory recoverable from the sacred text plus S100 attachment rows.

| Occurrence | Surface | Recoverable root/form evidence | Seed status |
| --- | --- | --- | --- |
| 100:1 | وَٱلْعَٰدِيَٰتِ | attachment root `ع د و`, active participle | lexical branches blocked |
| 100:1 | ضَبْحًا | attachment root `ض ب ح`, gerund, circumstantial | lexical branches blocked |
| 100:2 | فَٱلْمُورِيَٰتِ | attachment root `و ر ي`, active participle | lexical branches blocked |
| 100:2 | قَدْحًا | attachment root `ق د ح`, gerund, circumstantial | lexical branches blocked |
| 100:3 | فَٱلْمُغِيرَٰتِ | attachment root `غ ي ر`, active participle | lexical branches blocked |
| 100:3 | صُبْحًا | attachment root `ص ب ح`, adverbial time | lexical branches blocked |
| 100:4 | فَأَثَرْنَ | attachment root `أ ث ر`, perfect verb | lexical branches blocked |
| 100:4 | نَقْعًا | attachment root `ن ق ع`, direct object | lexical branches blocked |
| 100:5 | فَوَسَطْنَ | attachment root `و س ط`, perfect verb | lexical branches blocked |
| 100:5 | جَمْعًا | attachment root `ج م ع`, direct object | lexical branches blocked |
| 100:6 | ٱلْإِنسَٰنَ | attachment root `أ ن س`, governed ism of `إِنَّ` | lexical branches blocked |
| 100:6 | لِرَبِّهِۦ | attachment root `ر ب ب`, prepositional target of `كَنُودٌ` | lexical branches blocked |
| 100:6 | لَكَنُودٌ | attachment root `ك ن د`, emphatic predication | lexical branches blocked |
| 100:7 | لَشَهِيدٌ | attachment root `ش ه د`, emphatic predication | lexical branches blocked |
| 100:8 | لِحُبِّ | attachment root `ح ب ب`, prepositional complement of `شَدِيدٌ` | lexical branches blocked |
| 100:8 | ٱلْخَيْرِ | attachment root `خ ي ر`, genitive complement of `حُبِّ` | lexical branches blocked |
| 100:8 | لَشَدِيدٌ | attachment root `ش د د`, emphatic predication | lexical branches blocked |
| 100:9 | يَعْلَمُ | attachment root `ع ل م`, head of `إِذَا` clause | lexical branches blocked |
| 100:9 | بُعْثِرَ | attachment root `ب ع ث ر`, passive verb | lexical branches blocked |
| 100:9 | ٱلْقُبُورِ | attachment root `ق ب ر`, `فِى` complement | lexical branches blocked |
| 100:10 | حُصِّلَ | attachment root `ح ص ل`, passive verb | lexical branches blocked |
| 100:10 | ٱلصُّدُورِ | attachment root `ص د ر`, `فِى` complement | lexical branches blocked |
| 100:11 | رَبَّهُم | attachment root `ر ب ب`, governed ism of final `إِنَّ` | lexical branches blocked |
| 100:11 | لَّخَبِيرٌ | attachment root `خ ب ر`, final emphatic predication | lexical branches blocked |

## Exhaustive Lexical Seed Audit

Every eligible rooted occurrence above has an attempted lexical seed pass. Each pass is blocked at seed formation because no permitted furuq branch dossier is available. No branch IDs or branch images are fabricated.

For every blocked lexical seed, the root-level limitation is the same:

- seed occurrence: the listed rooted occurrence;
- seed type: lexical;
- generating set: none;
- selected branches: none, branch dossier unavailable;
- constructed model: none;
- freeze point: blocked before branch-image formation;
- predictions at freeze: none;
- unused features tested: not applicable, because no branch image could be frozen;
- corroborators: none;
- constraints: `resources/furuq_v4.sqlite` is empty; `resources/qac.sqlite` is empty; branch IDs/images cannot be reconstructed from sacred text or attachment rows;
- grade: unlikely as a lexical branch candidate, because the seed is resource-blocked rather than evidentially constructed;
- source rows used: sacred verse and any S100 attachment row naming the occurrence.

Blocked lexical seeds:

1. `LEX-BLOCK-001` - 100:1 `وَٱلْعَٰدِيَٰتِ`, root `ع د و`.
2. `LEX-BLOCK-002` - 100:1 `ضَبْحًا`, root `ض ب ح`.
3. `LEX-BLOCK-003` - 100:2 `فَٱلْمُورِيَٰتِ`, root `و ر ي`.
4. `LEX-BLOCK-004` - 100:2 `قَدْحًا`, root `ق د ح`.
5. `LEX-BLOCK-005` - 100:3 `فَٱلْمُغِيرَٰتِ`, root `غ ي ر`.
6. `LEX-BLOCK-006` - 100:3 `صُبْحًا`, root `ص ب ح`.
7. `LEX-BLOCK-007` - 100:4 `فَأَثَرْنَ`, root `أ ث ر`.
8. `LEX-BLOCK-008` - 100:4 `نَقْعًا`, root `ن ق ع`.
9. `LEX-BLOCK-009` - 100:5 `فَوَسَطْنَ`, root `و س ط`.
10. `LEX-BLOCK-010` - 100:5 `جَمْعًا`, root `ج م ع`.
11. `LEX-BLOCK-011` - 100:6 `ٱلْإِنسَٰنَ`, root `أ ن س`.
12. `LEX-BLOCK-012` - 100:6 `لِرَبِّهِۦ`, root `ر ب ب`.
13. `LEX-BLOCK-013` - 100:6 `لَكَنُودٌ`, root `ك ن د`.
14. `LEX-BLOCK-014` - 100:7 `لَشَهِيدٌ`, root `ش ه د`.
15. `LEX-BLOCK-015` - 100:8 `لِحُبِّ`, root `ح ب ب`.
16. `LEX-BLOCK-016` - 100:8 `ٱلْخَيْرِ`, root `خ ي ر`.
17. `LEX-BLOCK-017` - 100:8 `لَشَدِيدٌ`, root `ش د د`.
18. `LEX-BLOCK-018` - 100:9 `يَعْلَمُ`, root `ع ل م`.
19. `LEX-BLOCK-019` - 100:9 `بُعْثِرَ`, root `ب ع ث ر`.
20. `LEX-BLOCK-020` - 100:9 `ٱلْقُبُورِ`, root `ق ب ر`.
21. `LEX-BLOCK-021` - 100:10 `حُصِّلَ`, root `ح ص ل`.
22. `LEX-BLOCK-022` - 100:10 `ٱلصُّدُورِ`, root `ص د ر`.
23. `LEX-BLOCK-023` - 100:11 `رَبَّهُم`, root `ر ب ب`, positional replay of 100:6 Lord relation.
24. `LEX-BLOCK-024` - 100:11 `لَّخَبِيرٌ`, root `خ ب ر`.

## Progressive Recitation State

1. 100:1 opens with an oath particle governing `ٱلْعَٰدِيَٰتِ`, then an accusative manner expression `ضَبْحًا`. Available attachment evidence makes the initial scene an oath-framed moving agent plus manner.
2. 100:2 repeats the feminine-plural active participle pattern with `فَٱلْمُورِيَٰتِ`, then attaches `قَدْحًا` as a circumstantial manner. The sequence moves from motion/manner to caused effect/manner.
3. 100:3 repeats the pattern with `فَٱلْمُغِيرَٰتِ`, then `صُبْحًا` as a time adverb. The sequence adds arrival/time.
4. 100:4 shifts into a perfect 3FP verb, `فَأَثَرْنَ`, with `بِهِۦ` as prepositional complement and `نَقْعًا` as direct object. The opening agents now produce an object/effect.
5. 100:5 continues with a perfect 3FP verb, `فَوَسَطْنَ`, repeating `بِهِۦ` and taking `جَمْعًا` as direct object. The kinetic sequence reaches an occupied collective center.
6. 100:6 pivots with `إِنَّ` from plural kinetic agents to singular `ٱلْإِنسَٰنَ`, then predicates `لَكَنُودٌ` with respect to `لِرَبِّهِۦ`.
7. 100:7 repeats `وَإِنَّهُۥ` and predicates `لَشَهِيدٌ` over `عَلَىٰ ذَٰلِكَ`.
8. 100:8 repeats `وَإِنَّهُۥ`; `لِحُبِّ` attaches intensity to love, `ٱلْخَيْرِ` is the genitive complement, and `لَشَدِيدٌ` is the emphatic predicate.
9. 100:9 asks whether he knows, then supplies a temporal `إِذَا` clause. `مَا` is the passive subject of `بُعْثِرَ`; `فِى ٱلْقُبُورِ` specifies what is inside the graves.
10. 100:10 parallels 100:9: `مَا` is the passive subject of `حُصِّلَ`; `فِى ٱلصُّدُورِ` specifies what is inside the chests.
11. 100:11 returns `إِنَّ`; `رَبَّهُم` is the governed subject, `بِهِمْ` is the reference object of `لَّخَبِيرٌ`, and `يَوْمَئِذٍ` locates the final predication in time.

## Exhaustive Constructional Seed Audit

Every S100 attachment row was initiated as a constructional or morphosyntactic seed. Rows that did not produce an independent synthesis are retained as local support, constraints, or terminated seeds.

| Seed | Attachment row | Construction | Result |
| --- | --- | --- | --- |
| CON-001 | 100:1:a1 | oath particle governing `ٱلْعَٰدِيَٰتِ` | enters C001, C008; no independent closure without later chain |
| CON-002 | 100:1:a2 | `ضَبْحًا` as accusative manner | enters C001, C007, C008; lexical image blocked |
| CON-003 | 100:2:a1 | `قَدْحًا` as accusative manner | enters C001, C007, C008; lexical image blocked |
| CON-004 | 100:3:a1 | `صُبْحًا` as time adverb | enters C001, C007, C008; lexical image blocked |
| CON-005 | 100:4:a1 | `بِهِۦ` complement of `فَأَثَرْنَ` | enters C001, C007, C009; antecedent unresolved |
| CON-006 | 100:4:a2 | `نَقْعًا` direct object of `فَأَثَرْنَ` | enters C001, C008; lexical image blocked |
| CON-007 | 100:5:a1 | `بِهِۦ` complement of `فَوَسَطْنَ` | enters C001, C007, C009; antecedent unresolved |
| CON-008 | 100:5:a2 | `جَمْعًا` direct object of `فَوَسَطْنَ` | enters C001, C008; lexical image blocked |
| CON-009 | 100:6:a1 | `ٱلْإِنسَٰنَ` as governed ism of `إِنَّ` | enters C008, C010; marks discourse pivot |
| CON-010 | 100:6:a2 | possessive suffix in `رَبِّهِۦ` | enters C003, C011; local idafa support |
| CON-011 | 100:6:a3 | `لِرَبِّهِۦ` as target/respect of `كَنُودٌ` | enters C003, C010, C011 |
| CON-012 | 100:6:a4 | `كَنُودٌ` as emphatic predicate | enters C003, C010; lexical image blocked |
| CON-013 | 100:7:a1 | suffix in `إِنَّهُۥ` as governed ism | enters C004, C010; local pronoun continuity |
| CON-014 | 100:7:a2 | `عَلَىٰ ذَٰلِكَ` complement of `شَهِيدٌ` | enters C004, C010 |
| CON-015 | 100:7:a3 | `شَهِيدٌ` as emphatic predicate | enters C004, C010; lexical image blocked |
| CON-016 | 100:8:a1 | suffix in `وَإِنَّهُۥ` as governed ism | enters C005, C010; local pronoun continuity |
| CON-017 | 100:8:a2 | `لِحُبِّ` relating intensity to love | enters C005, C010 |
| CON-018 | 100:8:a3 | `ٱلْخَيْرِ` as genitive complement of `حُبِّ` | enters C005, C010 |
| CON-019 | 100:8:a4 | `شَدِيدٌ` as emphatic predicate | enters C005, C010; lexical image blocked |
| CON-020 | 100:9:a1 | `إِذَا` clause as temporal setting for `يَعْلَمُ` | enters C004, C006, C011 |
| CON-021 | 100:9:a2 | `مَا` as passive subject of `بُعْثِرَ` | enters C002, C004, C006, C011 |
| CON-022 | 100:9:a3 | `فِى ٱلْقُبُورِ` completing `مَا` | enters C001, C004, C006, C011 |
| CON-023 | 100:10:a1 | `مَا` as passive subject of `حُصِّلَ` | enters C002, C004, C005, C006, C011 |
| CON-024 | 100:10:a2 | `فِى ٱلصُّدُورِ` completing `مَا` | enters C001, C004, C005, C006, C011 |
| CON-025 | 100:11:a1 | `رَبَّهُم` as governed ism of final `إِنَّ` | enters C002, C003, C006, C011 |
| CON-026 | 100:11:a2 | possessive suffix in `رَبَّهُم` | enters C003, C009, C011; local idafa support |
| CON-027 | 100:11:a3 | `بِهِمْ` object/reference of `خَبِيرٌ` | enters C002, C005, C007, C009, C011 |
| CON-028 | 100:11:a4 | `يَوْمَئِذٍ` time adverb for final predicate | enters C006, C011 |
| CON-029 | 100:11:a5 | `خَبِيرٌ` as final predicate | enters C002, C004, C006, C011 |

## Recoverable Candidate Synthesis Units

### candidate_id: S100-P2-C001

- ayah_range: 100:1-5, tested against 100:6-11
- seed_type: constructional / temporal
- seed: opening oath chain, active feminine-plural participles followed by perfect 3FP verbs
- generating_set: 100:1 oath attachment; 100:1 `ضَبْحًا` manner; 100:2 `قَدْحًا` manner; 100:3 `صُبْحًا` time; 100:4 `نَقْعًا` object; 100:5 `جَمْعًا` object; repeated `فـ`; repeated `بِهِۦ`
- selected_branches: none; branch source unavailable
- constructed_model: a temporally advancing outside force is heard in manner, made effectual, timed at arrival, then made to raise an object and enter a collective center.
- freeze_point: after 100:5
- predictions_at_freeze: a later inside/outside axis; a pivot from active agents to an affected or judged interior; possible reactivation of center/inside by later containment language.
- unused_features_tested: 100:6-11 predications, `لِرَبِّهِۦ`, `لِحُبِّ ٱلْخَيْرِ`, paired `مَا فِى` clauses, final `رَبَّهُم بِهِمْ`.
- corroborators: (C: 100:9 `مَا فِى ٱلْقُبُورِ` gives a contained hidden object); (C: 100:10 `مَا فِى ٱلصُّدُورِ` repeats containment in an inner human location); (C: 100:11 `بِهِمْ` shifts from singular opening `بِهِۦ` to plural persons).
- constraints: (K: attachment rows keep 100:1-5 as oath-scene, not literal human interior); (K: 100:6 discourse pivot changes grammatical subject from opening plural agents to `ٱلْإِنسَٰنَ`).
- temporal_reactivation_notes: the opening movement toward `جَمْعًا` is reactivated when graves and chests become containers whose contents are later exposed.
- rival_models: a purely martial opening model cannot be verified lexically without furuq branches; it remains blocked.
- grade: medium-strong
- grade_rationale: structurally strong because order, attachment, and later containment converge; lexically limited because branch dossiers are unavailable.
- source_queries_or_rows_used: attachment rows 100:1:a1-a2, 100:2:a1, 100:3:a1, 100:4:a1-a2, 100:5:a1-a2, 100:9:a2-a3, 100:10:a1-a2, 100:11:a3.

### candidate_id: S100-P2-C002

- ayah_range: 100:1-11
- seed_type: morphosyntactic
- seed: agency transition from active oath sequence to passive exposure and final divine predication
- generating_set: active participle pattern in 100:1-3; perfect 3FP verbs in 100:4-5; passive verbs in 100:9-10; final `إِنَّ رَبَّهُم ... لَّخَبِيرٌ`
- selected_branches: none; branch source unavailable
- constructed_model: overt kinetic agency dominates the opening, then agency is withdrawn in the two exposure clauses, and final knowledge is assigned to the Lord.
- freeze_point: after recognizing the contrast between active 100:1-5 and passive 100:9-10
- predictions_at_freeze: a final agent or knower should be named; passive exposure should not itself name the exposing agent.
- unused_features_tested: 100:11 `رَبَّهُم`, `بِهِمْ`, `يَوْمَئِذٍ`, `لَّخَبِيرٌ`.
- corroborators: (C: 100:11:a1 `رَبَّهُم` is governed by final `إِنَّ`); (C: 100:11:a3 `بِهِمْ` supplies the object of reference for `خَبِيرٌ`); (C: 100:11:a5 `خَبِيرٌ` is final predicate).
- constraints: (K: passive rows 100:9:a2 and 100:10:a1 leave exposing agency unexpressed); (K: final expertise is not retrojected into every prior action as an explicit grammatical subject).
- temporal_reactivation_notes: the listener first tracks visible actors, then hears hidden contents acted upon, then receives the named final knower.
- rival_models: opening agents as ultimate judges is unsupported by grammar.
- grade: strong
- grade_rationale: the active/passive/final-predicate transition is specific, ordered, and independently fixed by attachment rows.
- source_queries_or_rows_used: attachment rows 100:1:a1-a2, 100:2:a1, 100:3:a1, 100:4:a1-a2, 100:5:a1-a2, 100:9:a2, 100:10:a1, 100:11:a1-a5.

### candidate_id: S100-P2-C003

- ayah_range: 100:6-11, with 100:1-5 as prior activation
- seed_type: constructional
- seed: `لِرَبِّهِۦ ... لَكَنُودٌ` and final `رَبَّهُم ... لَّخَبِيرٌ`
- generating_set: 100:6 prepositional target relation; 100:6 emphatic predication; 100:11 final `رَبَّهُم` subject and `خَبِيرٌ` predicate
- selected_branches: none; branch source unavailable
- constructed_model: the human is first evaluated in relation to his Lord, and the Lord relation returns at closure as the subject of exhaustive knowledge about them.
- freeze_point: after 100:6
- predictions_at_freeze: the Lord relation should return or be resolved; the human condition should be knowable, not merely asserted.
- unused_features_tested: 100:7 testimony, 100:8 intense love, 100:9-10 exposure, 100:11 final predication.
- corroborators: (C: 100:7:a2-a3 the human is witness over `ذَٰلِكَ`); (C: 100:8:a2-a4 internal motive is attached to love of good and intensity); (C: 100:9-10 paired passive exposure clauses); (C: 100:11:a1-a5 final Lord-expertise relation).
- constraints: (K: `لِرَبِّهِۦ` in 100:6 is a target/respect complement of `كَنُودٌ`, not an explicit direct object); (K: final `رَبَّهُم` is plural and closes after exposure, not simply a repeated singular phrase).
- temporal_reactivation_notes: 100:6 opens a relational deficit; 100:11 reactivates the same relation after hidden contents have been disclosed.
- rival_models: a model centered only on self-testimony at 100:7 underexplains why `رَبّ` returns in 100:11.
- grade: strong
- grade_rationale: exact lexical branch detail is blocked, but the relation, replay, and closure are structurally precise.
- source_queries_or_rows_used: attachment rows 100:6:a2-a4, 100:7:a1-a3, 100:8:a1-a4, 100:9:a1-a3, 100:10:a1-a2, 100:11:a1-a5.

### candidate_id: S100-P2-C004

- ayah_range: 100:7-10
- seed_type: constructional / epistemic
- seed: `وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌ` followed by `أَفَلَا يَعْلَمُ`
- generating_set: 100:7 testimony predication; 100:9 knowledge question
- selected_branches: none; branch source unavailable
- constructed_model: a self-attestation claim is followed by a challenge about knowledge, then tested by future exposure of what was hidden.
- freeze_point: after 100:9 `أَفَلَا يَعْلَمُ`
- predictions_at_freeze: testimony should prove insufficient unless hidden contents are brought out; the following clauses should distinguish knowing from mere witnessing.
- unused_features_tested: 100:9 passive exposure of grave contents, 100:10 passive extraction of chest contents, 100:11 final expertise.
- corroborators: (C: 100:9:a1 the `إِذَا` clause supplies the temporal setting for `يَعْلَمُ`); (C: 100:9:a2-a3 hidden grave contents become passive subject plus `فِى` complement); (C: 100:10:a1-a2 inner chest contents become passive subject plus `فِى` complement); (C: 100:11:a5 final expertise closes the epistemic sequence).
- constraints: (K: 100:7 `عَلَىٰ ذَٰلِكَ` gives the matter over which `شَهِيدٌ` applies; it does not by itself disclose the contents of graves or chests); (K: final knowledge belongs grammatically to `رَبَّهُم`, not to the human pronoun).
- temporal_reactivation_notes: self-witness is re-heard as limited once concealed contents are opened and a more inwardly informed knower is named.
- rival_models: human self-awareness as sufficient closure fails because the passage continues through exposure to `خَبِيرٌ`.
- grade: strong
- grade_rationale: sequence and grammatical role assignment strongly distinguish attestation, knowledge-question, exposure, and final expertise.
- source_queries_or_rows_used: attachment rows 100:7:a1-a3, 100:9:a1-a3, 100:10:a1-a2, 100:11:a1-a5.

### candidate_id: S100-P2-C005

- ayah_range: 100:8-10
- seed_type: constructional
- seed: `لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ`
- generating_set: 100:8 `لِحُبِّ` prepositional complement; 100:8 `ٱلْخَيْرِ` idafa complement; 100:8 `لَشَدِيدٌ` predicate
- selected_branches: none; branch source unavailable
- constructed_model: the human predication tightens around an internal attachment: intensity is attached to love, and love is grammatically completed by good.
- freeze_point: after 100:8
- predictions_at_freeze: a later inward container or motive should be exposed; the object of intensity should remain love rather than the opening agents.
- unused_features_tested: 100:9-10 passive exposure and final knowledge.
- corroborators: (C: 100:10:a2 `فِى ٱلصُّدُورِ` supplies an inner human container); (C: 100:10:a1 `مَا` is the passive subject of `حُصِّلَ`); (C: 100:11:a3-a5 final expertise refers to `بِهِمْ`).
- constraints: (K: attachment 100:8:a2 fixes `لِحُبِّ` as the complement relating intensity to love); (K: attachment 100:8:a3 fixes `ٱلْخَيْرِ` as genitive complement of love, not an independent object of `شَدِيدٌ`); (K: no lexical branch is available to equate this intensity with a particular remote image).
- temporal_reactivation_notes: the recitation moves from visible opening force to invisible motivational force, then to exposure of chest contents.
- rival_models: a model that takes `شَدِيدٌ` as merely physical strength ignores the `لِحُبِّ` attachment.
- grade: medium-strong
- grade_rationale: syntactic support is exact; lexical branch amplification is blocked.
- source_queries_or_rows_used: attachment rows 100:8:a1-a4, 100:10:a1-a2, 100:11:a3-a5.

### candidate_id: S100-P2-C006

- ayah_range: 100:9-10
- seed_type: constructional
- seed: paired containment clauses `مَا فِى ٱلْقُبُورِ` / `مَا فِى ٱلصُّدُورِ`
- generating_set: 100:9 passive subject plus `فِى` complement; 100:10 passive subject plus `فِى` complement
- selected_branches: none; branch source unavailable
- constructed_model: a parallel two-stage exposure moves from outer buried containers to inner human containers.
- freeze_point: after 100:10
- predictions_at_freeze: closure should supply the knower for these exposed contents and should locate the event temporally.
- unused_features_tested: 100:11 `رَبَّهُم`, `بِهِمْ`, `يَوْمَئِذٍ`, `خَبِيرٌ`.
- corroborators: (C: 100:11:a1 final `رَبَّهُم` is subject of the closing `إِنَّ`); (C: 100:11:a3 `بِهِمْ` supplies reference/object); (C: 100:11:a4 `يَوْمَئِذٍ` locates the predication); (C: 100:11:a5 `خَبِيرٌ` is predicate).
- constraints: (K: attachment rows assign `مَا` as passive subject in each clause, so the model must not treat graves or chests as grammatical agents); (K: the two `فِى` complements are not identical containers; the second is human-internal).
- temporal_reactivation_notes: the exact `مَا فِى` repetition invites immediate replay: first graves, then chests, from public/buried to personal/inward.
- rival_models: a single undifferentiated resurrection image loses the passage's second inward extraction.
- grade: strong
- grade_rationale: exact constructional parallel, contrastive container slots, and final knowledge closure are independently supported.
- source_queries_or_rows_used: attachment rows 100:9:a1-a3, 100:10:a1-a2, 100:11:a1-a5.

### candidate_id: S100-P2-C007

- ayah_range: 100:1-11
- seed_type: temporal/acoustic
- seed: repeated cadence and sound frame across the surah
- generating_set: `ضَبْحًا / قَدْحًا / صُبْحًا / نَقْعًا / جَمْعًا`; repeated `وَإِنَّهُۥ`; near-pair `شَهِيدٌ / شَدِيدٌ`; parallel `مَا فِى`; repeated `إِنَّ`; prepositional echo `بِهِۦ / بِهِمْ`
- selected_branches: none; branch source unavailable
- constructed_model: recurrence preserves a hearing frame while changing semantic roles: manner, manner, time, object, object; human predication, human predication, inner motive; outer container, inner container; pronoun reference shifts from an opening mechanism to persons.
- freeze_point: after recognizing the repeated sound/shape frames through 100:10
- predictions_at_freeze: the final line should both resolve the repeated frames and shift them into explicit knowledge.
- unused_features_tested: 100:11 final `إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍ لَّخَبِيرٌ`.
- corroborators: (C: 100:11 repeats `إِنَّ`); (C: 100:11:a3 `بِهِمْ` echoes earlier `بِهِۦ` at the prepositional surface while changing referent); (C: 100:11:a4 time adverb supplies final temporal closure); (C: 100:11:a5 final predicate closes epistemically).
- constraints: (K: acoustic similarity is not lexical identity); (K: `بِهِۦ` and `بِهِمْ` differ in number and reference); (K: without QAC/furuq, phonological reactivation cannot be upgraded to branch evidence).
- temporal_reactivation_notes: the reciter hears repeated templates, then each recurrence changes role, pushing from motion effects toward inward exposure and final expertise.
- rival_models: sound-only explanation is too weak without syntactic role changes.
- grade: medium
- grade_rationale: sound recurrence supports temporal replay, but it is corroborative and constrained by distinct roots and attachments.
- source_queries_or_rows_used: sacred text verses 1-11; attachment rows 100:4:a1, 100:5:a1, 100:11:a3; all predication and parallel containment rows.

### candidate_id: S100-P2-C008

- ayah_range: 100:1-8
- seed_type: constructional / discourse
- seed: oath sequence followed by `إِنَّ ٱلْإِنسَٰنَ`
- generating_set: 100:1 oath attachment; 100:1-5 consecutive `فـ` sequence; 100:6 `إِنَّ` human predication
- selected_branches: none; branch source unavailable
- constructed_model: an oath-framed kinetic display creates pressure before the discourse pivot diagnoses the human. The opening does not merely decorate the claim; it supplies a temporal force-pattern that 100:6-8 reinterprets as relational and motivational intensity.
- freeze_point: at 100:6
- predictions_at_freeze: the human diagnosis should be expanded by a relation, evidence, and motive.
- unused_features_tested: 100:6 `لِرَبِّهِۦ`, 100:7 witness, 100:8 love-good-intensity.
- corroborators: (C: 100:6:a3 target relation to Lord); (C: 100:7:a2-a3 witness over the matter); (C: 100:8:a2-a4 intense love of good).
- constraints: (K: opening feminine plural agents are not grammatically identical to singular `ٱلْإِنسَٰنَ`); (K: no lexical branch support is available for mapping specific opening words onto the human state).
- temporal_reactivation_notes: the transition makes the listener ask how the charged exterior sequence bears on the inner human claim.
- rival_models: treating 100:1-5 as isolated oath content leaves 100:6-8 structurally underconnected.
- grade: medium
- grade_rationale: discourse order supports reactivation, but lexical specificity is unavailable.
- source_queries_or_rows_used: attachment rows 100:1:a1-a2, 100:2:a1, 100:3:a1, 100:4:a1-a2, 100:5:a1-a2, 100:6:a1-a4, 100:7:a1-a3, 100:8:a1-a4.

### candidate_id: S100-P2-C009

- ayah_range: 100:4-5 and 100:11
- seed_type: constructional / pronoun replay
- seed: repeated `بِهِۦ` followed by final `بِهِمْ`
- generating_set: 100:4 `بِهِۦ` prepositional complement of `فَأَثَرْنَ`; 100:5 `بِهِۦ` prepositional complement of `فَوَسَطْنَ`
- selected_branches: none; branch source unavailable
- constructed_model: a repeated instrumental/reference slot in the opening prepares a final prepositional reference slot, but the referent changes from singular `it/him` in the kinetic chain to plural `them` under final expertise.
- freeze_point: after 100:5
- predictions_at_freeze: if replay occurs, it should mark a changed reference rather than simple repetition.
- unused_features_tested: 100:11 `بِهِمْ` and final predication.
- corroborators: (C: 100:11:a3 `بِهِمْ` supplies object of reference for `خَبِيرٌ`); (C: plural suffix matches `رَبَّهُم`); (C: final predicate makes the reference epistemic rather than kinetic).
- constraints: (K: singular `بِهِۦ` in 100:4-5 cannot be conflated with plural `بِهِمْ`); (K: attachment rows do not identify the antecedent of `بِهِۦ`, so this candidate remains a replay of surface construction, not a resolved lexical image).
- temporal_reactivation_notes: the listener hears the prepositional slot recur at closure with a transformed referent and function.
- rival_models: resolving `بِهِۦ` lexically is blocked without QAC/furuq and exceeds the available attachment evidence.
- grade: medium
- grade_rationale: exact surface recurrence and role transformation are useful, but antecedent ambiguity limits strength.
- source_queries_or_rows_used: attachment rows 100:4:a1, 100:5:a1, 100:11:a2-a3.

### candidate_id: S100-P2-C010

- ayah_range: 100:6-8
- seed_type: morphosyntactic
- seed: triple emphatic human predication
- generating_set: `إِنَّ ٱلْإِنسَٰنَ ... لَكَنُودٌ`; `وَإِنَّهُ ... لَشَهِيدٌ`; `وَإِنَّهُ ... لَشَدِيدٌ`
- selected_branches: none; branch source unavailable
- constructed_model: the passage builds a threefold human profile: relational deficit, witness over that matter, and intense attachment to love of good.
- freeze_point: after 100:8
- predictions_at_freeze: the following material should not merely continue description; it should test and expose what the profile contains.
- unused_features_tested: 100:9-11 exposure and final expertise.
- corroborators: (C: 100:9:a1 knowledge question sets a test); (C: 100:9:a2-a3 and 100:10:a1-a2 expose hidden contents); (C: 100:11:a5 final expertise evaluates them).
- constraints: (K: each predication has a distinct attachment: Lord relation, matter of witness, love-good-intensity); (K: the three predicates should not be flattened into one generic vice).
- temporal_reactivation_notes: the repeated pronoun creates continuity while each predicate adds a new unresolved layer, which is only closed by exposure and final knowledge.
- rival_models: a single-theme moral summary omits the staged predication sequence.
- grade: strong
- grade_rationale: constructional repetition with distinct complements and a later test sequence gives strong structural synthesis.
- source_queries_or_rows_used: attachment rows 100:6:a1-a4, 100:7:a1-a3, 100:8:a1-a4, 100:9:a1-a3, 100:10:a1-a2, 100:11:a1-a5.

### candidate_id: S100-P2-C011

- ayah_range: 100:11, replaying 100:6-10
- seed_type: constructional / closure
- seed: final `إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍ لَّخَبِيرٌ`
- generating_set: 100:11 final subject, possessive suffix, object of reference, time adverb, predicate
- selected_branches: none; branch source unavailable
- constructed_model: closure gathers relation, persons, time, and expertise into one final predication. It retrospectively resolves the Lord relation of 100:6 and the epistemic problem of 100:9.
- freeze_point: after 100:11
- predictions_at_freeze: no later passage features remain; closure should explain why the sequence stops here.
- unused_features_tested: earlier relation `لِرَبِّهِۦ`, witness/knowledge question, paired exposure clauses.
- corroborators: (C: 100:6:a3 earlier Lord relation); (C: 100:9:a1 question of knowledge); (C: 100:9:a2-a3 and 100:10:a1-a2 exposed contents); (C: 100:11:a4 final time); (C: 100:11:a5 final expertise).
- constraints: (K: the final predicate is not assigned to the human witness but to `رَبَّهُم`); (K: `يَوْمَئِذٍ` prevents a timeless generic-only closure; the final knowing is located at the exposure event).
- temporal_reactivation_notes: every major post-oath thread is reactivated: Lord relation, human object, day of exposure, and knowledge.
- rival_models: ending at 100:10 with exposure alone is incomplete because the final knower has not yet been named.
- grade: strong
- grade_rationale: exact closure mechanics are fixed by attachment rows and passage order.
- source_queries_or_rows_used: attachment rows 100:6:a2-a4, 100:9:a1-a3, 100:10:a1-a2, 100:11:a1-a5.

## Terminated Or Blocked Image Families

- Lexical branch images from all rooted words are blocked because `resources/furuq_v4.sqlite` is empty. This affects every lexical seed, including the first rooted word `وَٱلْعَٰدِيَٰتِ`.
- Morpheme-level morphology and measures are blocked because `resources/qac.sqlite` is empty.
- Basmala root corroboration is blocked because QAC/furuq roots and branches for opening context are unavailable. The basmala remains sacred opening context only.
- Any image requiring exact branch IDs, accepted branch counts, or `branch_image_ar` / `what_is_ar` is blocked, not weakly inferred.

## Image Packet Catalog

### IMAGE-S100-001

Starting seed: opening oath chain, 100:1-5.

Complete image: an outside kinetic sequence advances by repeated `فـ`, shifts from manner to effect to arrival to raised object to center-entry.

Passage-order assembly: 100:1 oath/manner -> 100:2 manner/effect -> 100:3 time/arrival -> 100:4 raised object -> 100:5 center-entry -> 100:9-10 hidden containers opened -> 100:11 final knowledge.

Participants and roles: opening plural agents; raised object `نَقْعًا`; entered object `جَمْعًا`; later concealed contents; final Lord as knower.

Operation / mechanism: temporal advance, effect production, entry, then passive exposure.

Direction / force / medium: from active outward motion toward collective center, then from concealed interiors outward into knowledge.

Temporal development: opening active sequence, human predication pivot, future exposure, final closure.

Outcome / closure: `رَبَّهُم ... لَّخَبِيرٌ`.

Exact branch constituents: none available; branch source blocked.

Unfilled roles: exact lexical images for every root.

Status: FRAGMENT, structurally strong but lexically blocked.

### IMAGE-S100-002

Starting seed: `لِرَبِّهِۦ ... لَكَنُودٌ`.

Complete image: a relational deficit is stated with respect to the Lord, then returned at closure as the Lord's informed knowledge of them.

Passage-order assembly: 100:6 Lord relation -> 100:7 witness -> 100:8 intense attachment -> 100:9-10 exposure -> 100:11 Lord expertise.

Participants and roles: human; his Lord; hidden contents; final Lord/knower.

Operation / mechanism: relation opened, human profile expanded, concealed contents exposed, relation closed epistemically.

Direction / force / medium: inward moral relation and hidden motive.

Temporal development: assertion, self-witness, motive, exposure, final knowledge.

Outcome / closure: Lord knows them on that day.

Exact branch constituents: none available; branch source blocked.

Unfilled roles: lexical specificity of `كَنُود`, `حُب`, `خَيْر`, `خَبِير`.

Status: FRAGMENT, structurally strong but lexically blocked.

### IMAGE-S100-003

Starting seed: paired `مَا فِى` clauses.

Complete image: two containers are opened in sequence: graves, then chests.

Passage-order assembly: 100:9 passive exposure of what is in graves -> 100:10 passive extraction of what is in chests -> 100:11 final informed predication.

Participants and roles: concealed contents; graves as outer container; chests as inner container; Lord as final knower.

Operation / mechanism: passive exposure and collection/extraction.

Direction / force / medium: hidden-inside to exposed-known.

Temporal development: knowledge question, future exposure, final expertise.

Outcome / closure: knowledge no longer rests on visible sign or self-attestation but on `خَبِيرٌ`.

Exact branch constituents: none available; branch source blocked.

Unfilled roles: exact lexical branch difference between `بُعْثِرَ` and `حُصِّلَ`.

Status: FRAGMENT, structurally strong but lexically blocked.

## Exhaustiveness Check After File Creation

The file covers:

- every rooted occurrence recoverable from S100 attachment rows;
- every lexical seed lane, marked blocked rather than fabricated;
- every recoverable attachment construction from S100 rows;
- temporal/acoustic recurrence from the sacred text;
- failed/blocked branch image families;
- image packets only where constructional evidence supports them.

Missing work is limited to unavailable permitted resources: QAC morphology and furuq branch dossiers.
