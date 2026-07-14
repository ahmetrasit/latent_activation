# S84 Stage 1 Pass 2 - temporally conditioned reactivation

Assigned passage: S84, whole surah.

Sacred Arabic text source used: `resources/quran/surah_84.json`.

Authorized structural source used: `resources/attachments.tsv`, rows where `sura=84` and `ayah=1..25`.

Authorized lexical/QAC sources attempted:

- `resources/qac.sqlite`
- `resources/furuq_v4.sqlite`

## Root cause of the Pass 1 limitation

The limitation was not selection bias toward a few promising words. The immediate root cause was that both authorized SQLite resources are zero-byte databases in this workspace state:

- `resources/qac.sqlite`: `0` schema entries.
- `resources/furuq_v4.sqlite`: `0` schema entries.

Therefore Pass 1 could not retrieve:

- QAC word/morpheme rows for S84;
- accepted branch counts;
- `branch_id`;
- `branch_image_ar`;
- `what_is_ar`;
- `contaminated='no'` furuq branch dossiers.

I did not invent missing branch IDs or branch images. This Pass 2 restarts from the first rooted word using all recoverable S84 evidence from the sacred Arabic text and attachment rows. It records every rooted occurrence and eligible construction as a seed pass, but branch-level lexical expansion remains blocked wherever the missing furuq dossier is required.

## Exhaustive restart inventory

Opening context, not seed material: `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`. It was not used to initiate a seed. Because QAC/furuq are empty, its roots and branch dossiers were not inspected; it can only constrain divine-source framing at a very general opening-context level.

Recoverable rooted occurrence sequence from S84 attachment rows and sacred text:

1. `84:1:1 إِذَا` root `أ ذ ي`, temporal adverb construction.
2. `84:1:2 السَّمَاءُ` root `س م و`, subject of `انْشَقَّتْ`.
3. `84:1:3 انْشَقَّتْ` root `ش ق ق`, predicate/event.
4. `84:2:2 وَأَذِنَتْ` root `أ ذ ن`, coordinated event.
5. `84:2:4 لِرَبِّهَا` root `ر ب ب`, governed complement.
6. `84:2:6 وَحُقَّتْ` root `ح ق ق`, coordinated passive event.
7. `84:3:2 وَإِذَا` root `أ ذ ي`, temporal adverb construction.
8. `84:3:3 الْأَرْضُ` root `أ ر ض`, subject.
9. `84:3:4 مُدَّتْ` root `م د د`, passive event.
10. `84:4:2 وَأَلْقَتْ` root `ل ق ي`, casting event.
11. `84:4:4 فِيهَا`, prepositional containment construction, no root recovered.
12. `84:4:6 وَتَخَلَّتْ` root `خ ل و`, coordinated emptying/freeing event.
13. `84:5:2 وَأَذِنَتْ` root `أ ذ ن`, repeated coordinated event.
14. `84:5:4 لِرَبِّهَا` root `ر ب ب`, repeated governed complement.
15. `84:5:6 وَحُقَّتْ` root `ح ق ق`, repeated coordinated passive event.
16. `84:6:2 يَاأَيُّهَا` root `أ ي ي`, vocative expression.
17. `84:6:3 الْإِنْسَانُ` root `أ ن س`, addressee.
18. `84:6:5 كَادِحٌ` root `ك د ح`, predicate.
19. `84:6:7 رَبِّكَ` root `ر ب ب`, goal complement under `إِلَى`.
20. `84:6:8 كَدْحًا` root `ك د ح`, cognate accusative.
21. `84:6:10 فَمُلَاقِيهِ` root `ل ق ي`, result predicate.
22. `84:7:3 مَنْ` root `م ن ن`, relative/recipient construction.
23. `84:7:4 أُوتِيَ` root `أ ت ي`, passive receiving/giving event.
24. `84:7:5 كِتَابَهُ` root `ك ت ب`, object received.
25. `84:7:7 بِيَمِينِهِ` root `ي م ن`, governed receiving-side complement.
26. `84:8:3 يُحَاسَبُ` root `ح س ب`, passive reckoning.
27. `84:8:4 حِسَابًا` root `ح س ب`, cognate accusative.
28. `84:8:5 يَسِيرًا` root `ي س ر`, qualifier.
29. `84:9:2 وَيَنْقَلِبُ` root `ق ل ب`, return/turning event.
30. `84:9:4 أَهْلِهِ` root `أ ه ل`, goal complement.
31. `84:9:5 مَسْرُورًا` root `س ر ر`, circumstantial state.
32. `84:10:3 مَنْ` root `م ن ن`, parallel relative/recipient construction.
33. `84:10:4 أُوتِيَ` root `أ ت ي`, parallel passive event.
34. `84:10:5 كِتَابَهُ` root `ك ت ب`, parallel object.
35. `84:10:6 وَرَاءَ` root `و ر ي`, adverbial location.
36. `84:10:7 ظَهْرِهِ` root `ظ ه ر`, complement of `وَرَاءَ`.
37. `84:11:3 يَدْعُو` root `د ع و`, calling event.
38. `84:11:4 ثُبُورًا` root `ث ب ر`, object called for.
39. `84:12:2 وَيَصْلَى` root `ص ل و`, entering/suffering fiery domain.
40. `84:12:3 سَعِيرًا` root `س ع ر`, object/domain.
41. `84:13:2 كَانَ` root `ك و ن`, predication.
42. `84:13:4 أَهْلِهِ` root `أ ه ل`, setting under `فِي`.
43. `84:13:5 مَسْرُورًا` root `س ر ر`, predicate state.
44. `84:14:2 ظَنَّ` root `ظ ن ن`, belief/thought.
45. `84:15:3 رَبَّهُ` root `ر ب ب`, subject of divine seeing clause.
46. `84:15:4 كَانَ` root `ك و ن`, predication.
47. `84:15:6 بَصِيرًا` root `ب ص ر`, predicate.
48. `84:16:3 أُقْسِمُ` root `ق س م`, oath event.
49. `84:16:5 بِالشَّفَقِ` root `ش ف ق`, oath object.
50. `84:17:2 وَاللَّيْلِ` root `ل ي ل`, oath object.
51. `84:17:5 وَسَقَ` root `و س ق`, gathered object clause.
52. `84:18:2 وَالْقَمَرِ` root `ق م ر`, oath object.
53. `84:18:3 إِذَا` root `أ ذ ي`, temporal qualifier.
54. `84:19:2 لَتَرْكَبُنَّ` root `ر ك ب`, oath-answer event.
55. `84:19:3 طَبَقًا` root `ط ب ق`, traversed stage.
56. `84:19:5 طَبَقٍ` root `ط ب ق`, second stage in `عَن` construction.
57. `84:20:4 لَهُمْ`, interrogative possessor construction.
58. `84:20:6 يُؤْمِنُونَ` root `أ م ن`, negated response.
59. `84:21:3 قُرِئَ` root `ق ر ء`, passive recitation.
60. `84:21:5 الْقُرْآنُ` root `ق ر ء`, passive subject.
61. `84:21:7 يَسْجُدُونَ` root `س ج د`, negated response.
62. `84:22:2 الَّذِينَ` root `ل ل ذ`, relative subject.
63. `84:22:3 كَفَرُوا` root `ك ف ر`, relative description; root present in sacred text but not recovered in S84 attachment root columns.
64. `84:22:4 يُكَذِّبُونَ` root `ك ذ ب`, active denial.
65. `84:23:2 وَاللَّهُ` root `أ ل ه`, nominal subject.
66. `84:23:3 أَعْلَمُ` root `ع ل م`, predicate.
67. `84:23:6 يُوعُونَ` attachment root listed as `و ع د`; surface suggests a containing/concealing action but branch dossier unavailable.
68. `84:24:2 فَبَشِّرْهُمْ` root `ب ش ر`, command.
69. `84:24:4 بِعَذَابٍ` root `ع ذ ب`, announced content.
70. `84:24:5 أَلِيمٍ` root `أ ل م`, qualifier.
71. `84:25:1 إِلَّا` root `أ ل و`, exception operator.
72. `84:25:2 الَّذِينَ` root `ل ل ذ`, excepted group.
73. `84:25:3 آمَنُوا` root `أ م ن`, positive response.
74. `84:25:5 وَعَمِلُوا` root `ع م ل`, coordinated action.
75. `84:25:6 الصَّالِحَاتِ` root `ص ل ح`, object of action.
76. `84:25:9 أَجْرٌ` root `أ ج ر`, delayed subject.
77. `84:25:10 غَيْرُ` root `غ ي ر`, qualifying noun.
78. `84:25:11 مَمْنُونٍ` root `م ن ن`, genitive complement.

Every listed occurrence was restarted as a seed. Where no branch dossier exists, the seed is recorded either as blocked or as contributing only through recoverable constructional, morphosyntactic, temporal, or repetition evidence.

## Constructional and temporal seed set

The following actual constructions were also started as seeds:

- `84:1-5`: paired `إِذَا` cosmic protasis sequence.
- `84:1-2`: sky event plus `أَذِنَتْ لِرَبِّهَا وَحُقَّتْ`.
- `84:3-5`: earth event plus `أَلْقَتْ مَا فِيهَا وَتَخَلَّتْ` and repeated `أَذِنَتْ لِرَبِّهَا وَحُقَّتْ`.
- `84:6`: vocative transfer from cosmic feminine subjects to human addressee.
- `84:6`: `كَادِحٌ ... كَدْحًا` cognate intensification.
- `84:6`: `إِلَى رَبِّكَ ... فَمُلَاقِيهِ` goal/result construction.
- `84:7-12`: `فَأَمَّا ... وَأَمَّا` bifurcation.
- `84:7-10`: `أُوتِيَ كِتَابَهُ` repeated passive receiving construction.
- `84:7` versus `84:10`: `بِيَمِينِهِ` versus `وَرَاءَ ظَهْرِهِ`.
- `84:8`: `يُحَاسَبُ حِسَابًا يَسِيرًا`.
- `84:9` versus `84:13`: repeated `أَهْلِهِ مَسْرُورًا`, one as future return, one as past misplaced comfort.
- `84:14-15`: `ظَنَّ أَن لَّن يَحُورَ` defeated by `بَلَى ... بَصِيرًا`.
- `84:16-19`: oath sequence: twilight, night and what it gathers, moon when it coheres.
- `84:19`: `طَبَقًا عَن طَبَقٍ`.
- `84:20-21`: non-response to faith and prostration.
- `84:22-24`: denial/concealment/painful announcement.
- `84:25`: exception closure with faith, righteous works, and non-diminished reward.

## Candidate synthesis units

### S84-P2-C01 - Split sky and stretched earth as obedient exposure

- `candidate_id`: `S84-P2-C01`
- `ayah_range`: `84:1-5`
- `seed_type`: constructional / temporal
- `seed`: paired `إِذَا` openings and the first rooted passage word `السَّمَاءُ` followed by `انْشَقَّتْ`.
- `generating_set`: `(E: 84:1 إذا temporal setting)`, `(E: 84:1 السماء subject attachment a2)`, `(E: 84:1 انشقت event)`, `(E: 84:2 أذنت لربها attachment a1)`, `(E: 84:2 وحقت attachment a2)`, `(E: 84:3 وإذا temporal restart)`, `(E: 84:3 الأرض subject attachment a2)`, `(E: 84:3 مدت event)`, `(E: 84:4 ألقت ما فيها attachment a1)`, `(E: 84:4 وتخلت attachment a3)`, `(E: 84:5 repeated أذنت لربها وحقت attachments a1-a2)`.
- `selected_branches`: no furuq branches available; no `branch_id` used.
- `constructed_model`: The recitation opens with an upper body split open, then repeats the same time-trigger for a lower body stretched out. Both are feminine cosmic subjects. Each submits/listens to its Lord and is made/rightfully bound to do so. Earth not only expands but throws out what is inside and becomes vacant. The image is not generic destruction; it is compliant exposure, opening, extension, unloading, and clearance.
- `freeze_point`: after `84:5`, before human address.
- `predictions_at_freeze`: a hidden/interior contents role; an authority/obligation role; a later human analogue to exposure; a movement from cosmic surfaces to contained records or concealed contents.
- `unused_features_tested`: `84:6 كادح إلى ربك`, `84:7-10 كتابه`, `84:14 لن يحور`, `84:15 بصيرا`, `84:23 بما يوعون`.
- `corroborators`: `(C: sequence 84:1-5 before human address creates cosmic-to-human transfer)`, `(C: 84:4 ما فيها supplies explicit interior contents)`, `(C: 84:7/10 كتابه later makes hidden account externally received)`, `(C: 84:15 بصيرا and 84:23 أعلم بما يوعون independently support divine access to concealed contents)`.
- `constraints`: `(K: no furuq branch dossier for ش ق ق, م د د, ل ق ي, خ ل و, أ ذ ن, ح ق ق; lexical specificity cannot be claimed)`, `(K: primary sense remains eschatological cosmic event, not metaphor-only psychology)`.
- `temporal_reactivation_notes`: `ما فيها` reactivates `انشقت` as opening-to-interior, while the repeated `أذنت لربها وحقت` after both sky and earth forces the listener to hear the two scenes as parallel submission rather than unrelated events.
- `rival_models`: simple apocalypse scene without transfer; legal summons scene; birth/extraction scene. All remain possible, but only the exposure model predicts later record, seeing, and concealment.
- `grade`: `medium-strong`
- `grade_rationale`: Strong structural repetition and later corroboration, but grade capped because no furuq branch evidence is available.
- `source_queries_or_rows_used`: `surah_84.json`; attachments `84:1:a1-a2`, `84:2:a1-a3`, `84:3:a1-a2`, `84:4:a1-a4`, `84:5:a1-a3`.

### S84-P2-C02 - Exhausted container: earth empties what it held

- `candidate_id`: `S84-P2-C02`
- `ayah_range`: `84:3-5`
- `seed_type`: constructional
- `seed`: `وَأَلْقَتْ مَا فِيهَا وَتَخَلَّتْ`.
- `generating_set`: `(E: 84:3 الأرض subject)`, `(E: 84:3 مدت)`, `(E: 84:4 ألقت ما فيها direct-object attachment a1)`, `(E: 84:4 فيها containment/predication attachments a2,a4)`, `(E: 84:4 تخلت conjoined event attachment a3)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: A containing body is first spread, then discharges what is inside, then becomes clear/vacant. The generated roles are container, contents, expulsion, and post-expulsion emptiness.
- `freeze_point`: after `84:4`, before the repeated `84:5` submission formula.
- `predictions_at_freeze`: later human contents should be exposed or brought out; there should be an accounting object; concealment should become unstable.
- `unused_features_tested`: `84:7/10 كتابه`, `84:15 بصيرا`, `84:23 بما يوعون`.
- `corroborators`: `(C: 84:7 and 84:10 repeated book reception converts hidden contents into an object handed over)`, `(C: 84:23 بما يوعون names a contained/concealed object under divine knowledge, with root line uncertain because attachment gives و ع د)`, `(C: 84:15 به بصيرا supports inspected interior/person)`.
- `constraints`: `(K: earth is the explicit subject; the model cannot make الإنسان the grammatical subject of 84:4)`, `(K: no branch dossier for خلو or لقي)`.
- `temporal_reactivation_notes`: When `كتاب` arrives in 84:7, the earlier earth-container scene is reactivated as an account-exposure pattern.
- `rival_models`: a burial-resurrection-only local image; a purely spatial flattening scene. Both are locally valid but explain fewer later reactivations.
- `grade`: `medium`
- `grade_rationale`: Good constructional fit, limited lexical depth.
- `source_queries_or_rows_used`: attachments `84:3:a1-a2`, `84:4:a1-a4`, `84:5:a1-a3`.

### S84-P2-C03 - Human striving as directed abrasion toward meeting

- `candidate_id`: `S84-P2-C03`
- `ayah_range`: `84:6`
- `seed_type`: morphosyntactic / constructional
- `seed`: `إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًا فَمُلَاقِيهِ`.
- `generating_set`: `(E: 84:6 vocative addressee attachments a1-a2)`, `(E: 84:6 كادح predication attachment a4)`, `(E: 84:6 إلى ربك goal complement attachment a5)`, `(E: 84:6 كدحا cognate accusative attachment a6)`, `(E: 84:6 فملاقيه result predicate/object attachments a7-a9)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: The human is addressed after the cosmic surfaces have opened. His motion is not wandering; it is a strenuous, intensified directed movement toward the Lord, and the `فـ` result closes the trajectory as meeting. The cognate accusative makes exertion thick and unavoidable.
- `freeze_point`: after `84:6`, before the two book-receiving cases.
- `predictions_at_freeze`: a destination-oriented evaluation; a later encounter mediated by an object or record; two possible outcomes after the same movement.
- `unused_features_tested`: `84:7-12` bifurcation, `84:14 لن يحور`, `84:15 بصيرا`, `84:19 طبقا عن طبق`.
- `corroborators`: `(C: 84:7-12 immediately divides outcomes of the addressed human trajectory)`, `(C: 84:14 لن يحور directly denies return, thereby reactivating the directional movement of 84:6)`, `(C: 84:19 لتركبن طبقا عن طبق supplies stage-to-stage motion after oath)`.
- `constraints`: `(K: without ك د ح furuq branches, abrasion/toil nuances cannot be branch-certified here)`, `(K: primary proposition remains direct human meeting with Lord, not merely abstract progress)`.
- `temporal_reactivation_notes`: The later `لن يحور` is heard as a false resistance to the movement already fixed in `إلى ربك ... فملاقيه`.
- `rival_models`: journey model; labor-for-account model; return model. They converge structurally but lexical ranking is blocked.
- `grade`: `medium-strong`
- `grade_rationale`: Strong local syntax and later sequence; branch-level lexical support unavailable.
- `source_queries_or_rows_used`: attachments `84:6:a1-a10`.

### S84-P2-C04 - Book-reception bifurcation: open hand versus hidden back

- `candidate_id`: `S84-P2-C04`
- `ayah_range`: `84:7-12`
- `seed_type`: constructional / morphosyntactic
- `seed`: `فَأَمَّا مَنْ أُوتِىَ كِتَابَهُ ... وَأَمَّا مَنْ أُوتِىَ كِتَابَهُ`.
- `generating_set`: `(E: 84:7 من subject attachment a1)`, `(E: 84:7 أوتي passive receiving attachment a1)`, `(E: 84:7 كتابه object attachment a2)`, `(E: 84:7 بيمينه governed complement attachment a3)`, `(E: 84:8 يحاسب حسابا cognate reckoning attachment a1)`, `(E: 84:8 يسيرا adjective attachment a2)`, `(E: 84:9 ينقلب إلى أهله مسرورا attachments a1-a2)`, `(E: 84:10 parallel من أوتي كتابه attachments a1-a2)`, `(E: 84:10 وراء ظهره attachments a3-a4)`, `(E: 84:11 يدعو ثبورا attachment a1)`, `(E: 84:12 يصلى سعيرا attachment a1)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: One record is received into the right-side public/accessible locus and leads to easy reckoning and joyful return. The other is received behind the back, displacing the record to a reversed, concealed, non-facing locus; its outcome is calling for destruction and entering a blazing domain.
- `freeze_point`: after `84:12`, before retrospective explanation in `84:13-15`.
- `predictions_at_freeze`: the bad case should have a prior false joy or concealed assumption; the record position should map onto a stance toward return; there should be divine inspection defeating concealment.
- `unused_features_tested`: `84:13 في أهله مسرورا`, `84:14 لن يحور`, `84:15 بصيرا`, `84:23 بما يوعون`.
- `corroborators`: `(C: 84:13 repeats أهله مسرورا but relocates joy to the past bad case)`, `(C: 84:14 لن يحور supplies the false non-return assumption)`, `(C: 84:15 بصيرا defeats behind-the-back concealment)`, `(C: 84:23 بما يوعون reactivates hidden contents)`.
- `constraints`: `(K: يمين/وراء/ظهر are explicit spatial/receiving constructions; do not dissolve them into generic good/bad symbolism)`, `(K: no furuq branch dossiers for يمن, وري, ظهر, كتب, أتى)`.
- `temporal_reactivation_notes`: `أهله مسرورا` at 84:13 replays 84:9 with opposite moral valence, causing a backward reinterpretation of happiness as either returned joy or premature insulation.
- `rival_models`: legal document model; bodily orientation model; social-family return model. The candidate retains all three as roles rather than reducing to one.
- `grade`: `medium-strong`
- `grade_rationale`: Excellent constructional parallelism and reactivation; lexical branch depth missing.
- `source_queries_or_rows_used`: attachments `84:7:a1-a5`, `84:8:a1-a2`, `84:9:a1-a3`, `84:10:a1-a6`, `84:11:a1`, `84:12:a1`.

### S84-P2-C05 - Joy reactivated: returned joy versus enclosed false joy

- `candidate_id`: `S84-P2-C05`
- `ayah_range`: `84:9-15`
- `seed_type`: temporal/reactivation
- `seed`: repeated `أَهْلِهِ مَسْرُورًا`.
- `generating_set`: `(E: 84:9 ينقلب إلى أهله مسرورا attachments a1-a2)`, `(E: 84:13 كان في أهله مسرورا attachments a2-a5)`, `(E: 84:14 ظن أن لن يحور attachments a2-a3)`, `(E: 84:15 بلى إن ربه كان به بصيرا attachments a1-a5)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: The same social-emotional cluster appears twice. First, joy is the state of a successful return to family. Second, joy was already enjoyed within family as a past enclosure, and that enclosure supported the false thought that he would not return. Divine sight breaks the enclosure.
- `freeze_point`: after `84:15`.
- `predictions_at_freeze`: earlier `ينقلب` should be heard not just as motion but as true return; later disbelief should resist recited exposure; hidden contents should remain under divine knowledge.
- `unused_features_tested`: `84:20 لا يؤمنون`, `84:21 لا يسجدون`, `84:23 أعلم بما يوعون`.
- `corroborators`: `(C: 84:20-21 non-response extends the false insulation into refusal under recitation)`, `(C: 84:23 divine knowledge of what is contained/concealed repeats the sight-over-enclosure role)`.
- `constraints`: `(K: سرر branch evidence unavailable; joy/interiority role is constructional from repeated surface and attachments only)`.
- `temporal_reactivation_notes`: This is one of the clearest backward reactivation points: 84:13 forces 84:9 to be reread by contrast.
- `rival_models`: family-as-literal-return only; joy-as-moral-blindness only. The passage requires both.
- `grade`: `medium-strong`
- `grade_rationale`: Strong repetition and reversal; missing lexical branch support.
- `source_queries_or_rows_used`: attachments `84:9:a1-a3`, `84:13:a1-a5`, `84:14:a1-a3`, `84:15:a1-a5`.

### S84-P2-C06 - False non-return defeated by seeing

- `candidate_id`: `S84-P2-C06`
- `ayah_range`: `84:14-15`
- `seed_type`: constructional
- `seed`: `ظَنَّ أَن لَّن يَحُورَ` followed by `بَلَى ... بَصِيرًا`.
- `generating_set`: `(E: 84:14 ظن predication attachment a2)`, `(E: 84:14 أن لن يحور clausal complement attachment a3)`, `(E: 84:15 بلى)`, `(E: 84:15 ربه subject attachment a1)`, `(E: 84:15 كان به بصيرا attachments a3-a5)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: A human assumption blocks return: he thought the trajectory would not curve back. The correction is not an abstract assertion but a seeing relation: his Lord was seeing him. The return-denial is defeated by surveillance/knowledge of the person through time.
- `freeze_point`: after `84:15`.
- `predictions_at_freeze`: an oath or cosmic sign sequence should confirm layered transition; later denial should be framed as refusal despite exposure.
- `unused_features_tested`: `84:16-19 oath`, `84:20-23`.
- `corroborators`: `(C: 84:19 طبقا عن طبق gives stage movement after the return denial)`, `(C: 84:23 والله أعلم بما يوعون provides knowledge over concealed stores)`.
- `constraints`: `(K: root حور is not recoverable from attachment root columns, so it cannot be branch-seeded here despite being central in sacred text)`, `(K: no QAC row to confirm morphology from authorized DB)`.
- `temporal_reactivation_notes`: This seed reactivates `إلى ربك ... فملاقيه`; the false thought is a failed prediction against the earlier direction.
- `rival_models`: cognitive error only; legal accountability only; visual surveillance only. The local syntax holds thought, return, and sight together.
- `grade`: `medium`
- `grade_rationale`: Strong local contrast, but one central root is missing from available attachment root extraction and branch evidence is absent.
- `source_queries_or_rows_used`: sacred text `84:14`; attachments `84:14:a1-a3`, `84:15:a1-a5`.

### S84-P2-C07 - Oath as layered gathering before stage-riding

- `candidate_id`: `S84-P2-C07`
- `ayah_range`: `84:16-19`
- `seed_type`: temporal/acoustic / constructional
- `seed`: oath sequence `بِالشَّفَقِ`, `وَاللَّيْلِ وَمَا وَسَقَ`, `وَالْقَمَرِ إِذَا اتَّسَقَ`.
- `generating_set`: `(E: 84:16 أقسم oath event attachment a1)`, `(E: 84:16 بالشفق oath object attachment a1)`, `(E: 84:17 الليل oath object)`, `(E: 84:17 وما وسق gathered object clause attachments a1-a2)`, `(E: 84:18 القمر oath object)`, `(E: 84:18 إذا اتسق temporal qualifier attachment a1)`, `(E: 84:19 لتركبن event attachment a1)`, `(E: 84:19 طبقا عن طبق attachment a2)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: Twilight marks transition, night gathers what it contains, the moon coheres when complete, and the oath answer is traversing layer upon layer. The image is ordered aggregation and phase-transition, not isolated celestial decoration.
- `freeze_point`: after `84:19`.
- `predictions_at_freeze`: subsequent human refusal should be irrational against staged, recited, and visible order; there should be a contrast between cosmic coherence and human non-submission.
- `unused_features_tested`: `84:20 لا يؤمنون`, `84:21 لا يسجدون`, `84:22 يكذبون`.
- `corroborators`: `(C: 84:20-21 humans do not believe/prostrate after the staged oath, creating cosmic coherence versus human refusal)`, `(C: 84:1-5 earlier sky/earth transitions prefigure layered transition)`.
- `constraints`: `(K: no branch dossiers for شفق, ليل, وسق, قمر, طبق, ركب)`, `(K: oath objects remain primary oath signs; secondary image cannot replace them)`.
- `temporal_reactivation_notes`: `طبقا عن طبق` reactivates the earlier progression from sky to earth to human to record to return, making the surah itself feel stage-layered.
- `rival_models`: celestial-time model; gathered-container model; ascent/descent model. Without branch dossiers, keep all as provisional forks.
- `grade`: `medium`
- `grade_rationale`: Strong sequence, but lexical branch specificity unavailable.
- `source_queries_or_rows_used`: attachments `84:16:a1`, `84:17:a1-a2`, `84:18:a1`, `84:19:a1-a2`.

### S84-P2-C08 - Recitation exposure met by refusal to bow

- `candidate_id`: `S84-P2-C08`
- `ayah_range`: `84:20-23`
- `seed_type`: constructional / temporal
- `seed`: `فَمَا لَهُمْ لَا يُؤْمِنُونَ` and `وَإِذَا قُرِئَ عَلَيْهِمُ الْقُرْآنُ لَا يَسْجُدُونَ`.
- `generating_set`: `(E: 84:20 ما لهم idiom attachments a1-a2)`, `(E: 84:20 لا يؤمنون circumstantial attachment a3)`, `(E: 84:21 إذا recitation condition)`, `(E: 84:21 قريء عليهم attachment a1)`, `(E: 84:21 القرآن passive subject attachment a2)`, `(E: 84:21 لا يسجدون negated response attachment a3)`, `(E: 84:22 الذين كفروا يكذبون attachment a1)`, `(E: 84:23 الله أعلم بما يوعون attachments a1-a3)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: After cosmic and oath exposure, a recited exposure comes directly upon them. The expected bodily and inward responses, faith and prostration, do not occur. Instead, disbelief becomes denial, and what they hold within remains known to God.
- `freeze_point`: after `84:23`, before announcement and exception.
- `predictions_at_freeze`: a painful announcement should answer refusal; an exception should preserve the correct response pattern.
- `unused_features_tested`: `84:24-25`.
- `corroborators`: `(C: 84:24 فبشرهم بعذاب أليم answers refusal with announced content)`, `(C: 84:25 الذين آمنوا وعملوا الصالحات supplies the positive response set)`.
- `constraints`: `(K: ق ر ء branch evidence unavailable; no claim about recitation-root branches)`, `(K: attachment root for يوعون appears as و ع د, so its lexical root must be treated as uncertain in this artifact)`.
- `temporal_reactivation_notes`: The phrase `قُرِئَ عَلَيْهِمُ` replays the whole surah as an event being placed upon hearers, parallel to books placed into hands/behind backs.
- `rival_models`: polemical refusal model; ritual non-prostration model; concealed-content model. The construction supports a combined response/refusal image.
- `grade`: `medium`
- `grade_rationale`: Good discourse sequence and attachments; branch depth missing.
- `source_queries_or_rows_used`: attachments `84:20:a1-a3`, `84:21:a1-a3`, `84:22:a1`, `84:23:a1-a3`.

### S84-P2-C09 - Bitter glad-tiding and exception closure

- `candidate_id`: `S84-P2-C09`
- `ayah_range`: `84:24-25`
- `seed_type`: constructional
- `seed`: `فَبَشِّرْهُم بِعَذَابٍ أَلِيمٍ إِلَّا الَّذِينَ آمَنُوا...`.
- `generating_set`: `(E: 84:24 بشرهم command/object attachment a1)`, `(E: 84:24 بعذاب content attachment a2)`, `(E: 84:24 أليم adjective attachment a3)`, `(E: 84:25 إلا exception attachment a1)`, `(E: 84:25 آمنوا وعملوا coordination attachment a2)`, `(E: 84:25 الصالحات direct object attachment a3)`, `(E: 84:25 لهم أجر fronted predicate/delayed subject attachments a4-a5)`, `(E: 84:25 غير ممنون qualification attachments a6-a7)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: The command to announce good news is inverted into painful punishment for the deniers, then the final exception extracts a group whose response matches the missed expectations: faith and righteous action. Their recompense is not cut off or diminished.
- `freeze_point`: end of surah.
- `predictions_at_freeze`: closure should answer the earlier non-faith, non-prostration, denial, and concealed contents.
- `unused_features_tested`: previous sequence only, because this is closure.
- `corroborators`: `(C: 84:20 لا يؤمنون is answered by 84:25 آمنوا)`, `(C: 84:22 يكذبون is answered by faithful action)`, `(C: 84:8 حسابا يسيرا and 84:25 أجر غير ممنون converge on non-destructive/eased outcome)`.
- `constraints`: `(K: no branch dossiers for بشر, عذب, ألم, أجر, منن, صلح, عمل, أمن)`, `(K: exception closure cannot be used to erase the prior warning; it creates the final bifurcation)`.
- `temporal_reactivation_notes`: `إلا الذين آمنوا` reactivates `فما لهم لا يؤمنون` and converts a question of refusal into an exception boundary.
- `rival_models`: reward/punishment closure only; inverted-announcement rhetoric; exception-as-extraction. All are constructionally present.
- `grade`: `medium`
- `grade_rationale`: Strong closure mechanics; lexical branches unavailable.
- `source_queries_or_rows_used`: attachments `84:24:a1-a3`, `84:25:a1-a7`.

### S84-P2-C10 - Whole-surah layered exposure and response model

- `candidate_id`: `S84-P2-C10`
- `ayah_range`: `84:1-25`
- `seed_type`: verified composite from constructional convergence
- `seed`: convergence of C01-C09.
- `generating_set`: `(E: C01 cosmic obedient exposure)`, `(E: C03 human directed striving)`, `(E: C04 record bifurcation)`, `(E: C05 joy reactivation)`, `(E: C07 layered oath/stage traversal)`, `(E: C08 recitation refusal)`, `(E: C09 exception closure)`.
- `selected_branches`: none; composite is not branch-verified.
- `constructed_model`: The surah unfolds as layers opened and traversed. Sky splits, earth stretches and empties, human striving reaches meeting, the book exposes account, family-joy is either returned or exposed as false insulation, cosmic phases gather into layer-upon-layer movement, recitation confronts hearers, denial tries to hold contents inward, and the final exception separates faithful repair from painful announcement.
- `freeze_point`: composite formed after independent constructional candidates were frozen.
- `predictions_at_freeze`: repeated interior/exposure markers should appear; movement should be directional and staged; refusal should be contrasted with cosmic submission; final closure should distinguish outcomes.
- `unused_features_tested`: all remaining constructions after each local freeze were tested in the candidate sections above.
- `corroborators`: `(C: repeated إذا temporal triggers)`, `(C: repeated أذنت لربها وحقت)`, `(C: repeated كتابه)`, `(C: repeated أهله مسرورا)`, `(C: oath-to-answer sequence)`, `(C: final إلا exception)`.
- `constraints`: `(K: not branch-verified; should enter Stage 2 as a constructional synthesis, not a deep lexical conclusion)`, `(K: no English translation used)`, `(K: basmala not used as seed)`.
- `temporal_reactivation_notes`: The strongest reactivations are `ما فيها` -> `كتابه` -> `بما يوعون`, `إلى ربك فملاقيه` -> `لن يحور` -> `طبقا عن طبق`, and `أهله مسرورا` future joy -> past false joy.
- `rival_models`: legal-accounting governing model; cosmic-collapse governing model; recitation-response governing model. The layered exposure model preserves all three but remains provisional pending branch dossiers.
- `grade`: `medium`
- `grade_rationale`: High constructional convergence, but branch-level lexical standard is unsatisfied due missing authorized DBs.
- `source_queries_or_rows_used`: all S84 attachment rows plus sacred text.

## Exhaustive seed ledger

The following ledger records the restart outcome for every rooted occurrence and eligible construction. `BRANCH_BLOCKED` means the required furuq branch dossier was unavailable because `furuq_v4.sqlite` has no schema/content in this workspace.

| Seed | Outcome |
| --- | --- |
| `84:1:1 إذا / أ ذ ي` | construction seed used in C01; lexical branches `BRANCH_BLOCKED`. |
| `84:1:2 السماء / س م و` | subject seed used in C01; branches `BRANCH_BLOCKED`. |
| `84:1:3 انشقت / ش ق ق` | event seed used in C01; branches `BRANCH_BLOCKED`. |
| `84:2:2 أذنت / أ ذ ن` | repeated compliance seed used in C01; branches `BRANCH_BLOCKED`. |
| `84:2:4 ربها / ر ب ب` | authority/goal seed used in C01/C03; branches `BRANCH_BLOCKED`. |
| `84:2:6 حقت / ح ق ق` | obligation/rightful-completion construction seed used in C01; branches `BRANCH_BLOCKED`. |
| `84:3:2 إذا / أ ذ ي` | temporal restart seed used in C01/C02; branches `BRANCH_BLOCKED`. |
| `84:3:3 الأرض / أ ر ض` | lower-body/container seed used in C02; branches `BRANCH_BLOCKED`. |
| `84:3:4 مدت / م د د` | extension seed used in C02; branches `BRANCH_BLOCKED`. |
| `84:4:2 ألقت / ل ق ي` | expulsion seed used in C02; branches `BRANCH_BLOCKED`. |
| `84:4:4 فيها` | containment construction seed used in C02; no root branch. |
| `84:4:6 تخلت / خ ل و` | vacancy seed used in C02; branches `BRANCH_BLOCKED`. |
| `84:5:2 أذنت / أ ذ ن` | repeated compliance seed used in C01; branches `BRANCH_BLOCKED`. |
| `84:5:4 ربها / ر ب ب` | repeated authority seed used in C01; branches `BRANCH_BLOCKED`. |
| `84:5:6 حقت / ح ق ق` | repeated obligation seed used in C01; branches `BRANCH_BLOCKED`. |
| `84:6:2 يا أيها / أ ي ي` | vocative construction seed used in C03; branches `BRANCH_BLOCKED`. |
| `84:6:3 الإنسان / أ ن س` | addressee seed used in C03; branches `BRANCH_BLOCKED`. |
| `84:6:5 كادح / ك د ح` | striving seed used in C03; branches `BRANCH_BLOCKED`. |
| `84:6:7 ربك / ر ب ب` | goal seed used in C03; branches `BRANCH_BLOCKED`. |
| `84:6:8 كدحا / ك د ح` | cognate intensification seed used in C03; branches `BRANCH_BLOCKED`. |
| `84:6:10 فملاقيه / ل ق ي` | meeting-result seed used in C03; branches `BRANCH_BLOCKED`. |
| `84:7:3 من / م ن ن` | recipient bifurcation seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:7:4 أوتي / أ ت ي` | passive receiving seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:7:5 كتابه / ك ت ب` | record seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:7:7 بيمينه / ي م ن` | right-side receiving seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:8:3 يحاسب / ح س ب` | reckoning seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:8:4 حسابا / ح س ب` | cognate reckoning seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:8:5 يسيرا / ي س ر` | ease qualifier seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:9:2 ينقلب / ق ل ب` | return/turn seed used in C04/C05; branches `BRANCH_BLOCKED`. |
| `84:9:4 أهله / أ ه ل` | family-goal seed used in C05; branches `BRANCH_BLOCKED`. |
| `84:9:5 مسرورا / س ر ر` | joy seed used in C05; branches `BRANCH_BLOCKED`. |
| `84:10:3 من / م ن ن` | parallel recipient seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:10:4 أوتي / أ ت ي` | parallel passive receiving seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:10:5 كتابه / ك ت ب` | parallel record seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:10:6 وراء / و ر ي` | behind-position seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:10:7 ظهره / ظ ه ر` | back/body-position seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:11:3 يدعو / د ع و` | calling seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:11:4 ثبورا / ث ب ر` | destruction-call seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:12:2 يصلى / ص ل و` | fiery-entry seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:12:3 سعيرا / س ع ر` | blazing-domain seed used in C04; branches `BRANCH_BLOCKED`. |
| `84:13:2 كان / ك و ن` | past-state seed used in C05; branches `BRANCH_BLOCKED`. |
| `84:13:4 أهله / أ ه ل` | enclosed family seed used in C05; branches `BRANCH_BLOCKED`. |
| `84:13:5 مسرورا / س ر ر` | reactivated joy seed used in C05; branches `BRANCH_BLOCKED`. |
| `84:14:2 ظن / ظ ن ن` | false-thought seed used in C06; branches `BRANCH_BLOCKED`. |
| `84:14:5 يحور` | sacred-text seed central to C06; root not recovered in attachment rows; QAC unavailable. |
| `84:15:3 ربه / ر ب ب` | divine subject seed used in C06; branches `BRANCH_BLOCKED`. |
| `84:15:4 كان / ك و ن` | predication seed used in C06; branches `BRANCH_BLOCKED`. |
| `84:15:6 بصيرا / ب ص ر` | seeing seed used in C06; branches `BRANCH_BLOCKED`. |
| `84:16:3 أقسم / ق س م` | oath seed used in C07; branches `BRANCH_BLOCKED`. |
| `84:16:5 الشفق / ش ف ق` | twilight oath seed used in C07; branches `BRANCH_BLOCKED`. |
| `84:17:2 الليل / ل ي ل` | night oath seed used in C07; branches `BRANCH_BLOCKED`. |
| `84:17:5 وسق / و س ق` | gathered-object seed used in C07; branches `BRANCH_BLOCKED`. |
| `84:18:2 القمر / ق م ر` | moon oath seed used in C07; branches `BRANCH_BLOCKED`. |
| `84:18:3 إذا` | temporal qualifier seed used in C07; branches `BRANCH_BLOCKED`. |
| `84:18:4 اتسق` | sacred-text seed paired with وسق; root not recovered in attachment rows; QAC unavailable. |
| `84:19:2 لتركبن / ر ك ب` | stage-traversal seed used in C07; branches `BRANCH_BLOCKED`. |
| `84:19:3 طبقا / ط ب ق` | first stage seed used in C07; branches `BRANCH_BLOCKED`. |
| `84:19:5 طبق / ط ب ق` | second stage seed used in C07; branches `BRANCH_BLOCKED`. |
| `84:20:4 لهم` | idiom construction seed used in C08; no root branch. |
| `84:20:6 يؤمنون / أ م ن` | negated-faith seed used in C08/C09; branches `BRANCH_BLOCKED`. |
| `84:21:3 قرئ / ق ر ء` | recitation seed used in C08; branches `BRANCH_BLOCKED`. |
| `84:21:5 القرآن / ق ر ء` | recited object seed used in C08; branches `BRANCH_BLOCKED`. |
| `84:21:7 يسجدون / س ج د` | prostration-response seed used in C08; branches `BRANCH_BLOCKED`. |
| `84:22:2 الذين / ل ل ذ` | relative subject construction used in C08; branches `BRANCH_BLOCKED`. |
| `84:22:3 كفروا / ك ف ر` | sacred-text disbelief seed used in C08; not recovered in attachment root columns; QAC unavailable. |
| `84:22:4 يكذبون / ك ذ ب` | denial seed used in C08; branches `BRANCH_BLOCKED`. |
| `84:23:2 الله / أ ل ه` | divine knowledge subject used in C08; branches `BRANCH_BLOCKED`. |
| `84:23:3 أعلم / ع ل م` | knowledge seed used in C08; branches `BRANCH_BLOCKED`. |
| `84:23:6 يوعون` | concealed/contained-object seed used in C08; attachment root uncertain (`و ع د`), QAC unavailable. |
| `84:24:2 بشرهم / ب ش ر` | announcement seed used in C09; branches `BRANCH_BLOCKED`. |
| `84:24:4 عذاب / ع ذ ب` | punishment-content seed used in C09; branches `BRANCH_BLOCKED`. |
| `84:24:5 أليم / أ ل م` | pain qualifier seed used in C09; branches `BRANCH_BLOCKED`. |
| `84:25:1 إلا / أ ل و` | exception operator seed used in C09; branches `BRANCH_BLOCKED`. |
| `84:25:2 الذين / ل ل ذ` | excepted relative seed used in C09; branches `BRANCH_BLOCKED`. |
| `84:25:3 آمنوا / أ م ن` | positive-faith seed used in C09; branches `BRANCH_BLOCKED`. |
| `84:25:5 عملوا / ع م ل` | righteous-action seed used in C09; branches `BRANCH_BLOCKED`. |
| `84:25:6 الصالحات / ص ل ح` | repair/righteous-object seed used in C09; branches `BRANCH_BLOCKED`. |
| `84:25:9 أجر / أ ج ر` | recompense seed used in C09; branches `BRANCH_BLOCKED`. |
| `84:25:10 غير / غ ي ر` | negating qualifier seed used in C09; branches `BRANCH_BLOCKED`. |
| `84:25:11 ممنون / م ن ن` | non-diminished/non-cut-off qualifier seed used in C09; branches `BRANCH_BLOCKED`. |
| `84:1-5 paired إذا` | construction seed used in C01. |
| `84:1-2 sky compliance formula` | construction seed used in C01. |
| `84:3-5 earth emptying/compliance formula` | construction seed used in C01-C02. |
| `84:6 vocative transfer` | construction seed used in C03. |
| `84:6 كادح/كدحا cognate accusative` | construction seed used in C03. |
| `84:7-12 فأما/وأما bifurcation` | construction seed used in C04. |
| `84:7/10 repeated أوتي كتابه` | construction seed used in C04. |
| `84:9/13 repeated أهله مسرورا` | temporal reactivation seed used in C05. |
| `84:14-15 false return/seeing correction` | construction seed used in C06. |
| `84:16-19 oath sequence` | construction seed used in C07. |
| `84:19 طبقا عن طبق` | construction seed used in C07/C10. |
| `84:20-21 non-faith/non-prostration` | construction seed used in C08. |
| `84:22-24 denial/concealment/announcement` | construction seed used in C08-C09. |
| `84:25 exception closure` | construction seed used in C09. |

## Failed or terminated lexical branch avalanches

All root-branch avalanches requiring furuq branch IDs terminated before branch selection because `resources/furuq_v4.sqlite` has no schema/content. This includes every recovered root:

`أ ت ي`, `أ ج ر`, `أ ذ ن`, `أ ذ ي`, `أ ر ض`, `أ ل م`, `أ ل ه`, `أ ل و`, `أ م ن`, `أ ن س`, `أ ه ل`, `أ ي ي`, `ب ش ر`, `ب ص ر`, `ث ب ر`, `ح س ب`, `ح ق ق`, `خ ل و`, `د ع و`, `ر ب ب`, `ر ك ب`, `س ج د`, `س ر ر`, `س ع ر`, `س م و`, `ش ف ق`, `ش ق ق`, `ص ل ح`, `ص ل و`, `ط ب ق`, `ظ ن ن`, `ظ ه ر`, `ع ذ ب`, `ع ل م`, `ع م ل`, `غ ي ر`, `ق ر ء`, `ق س م`, `ق ل ب`, `ق م ر`, `ك ت ب`, `ك د ح`, `ك ذ ب`, `ك و ن`, `ل ق ي`, `ل ل ذ`, `ل ي ل`, `م د د`, `م ن ن`, `و ر ي`, `و س ق`, `و ع د`, `ي س ر`, `ي م ن`.

Additional sacred-text roots likely present but not reliably seedable from authorized DB output because QAC is empty and/or attachment extraction did not recover them: `ك ف ر`, `ح و ر`, and the root of `اتسق`.

## Image Packet Catalog

### IMAGE S84-IMG-01

- Starting seed: `84:1 السماء انشقت`.
- Complete image: obedient cosmic exposure.
- Passage-order assembly: sky split -> listens/is bound -> earth stretched -> empties contents -> listens/is bound.
- Participants and roles: sky/earth as opened surfaces; Lord as authority; contents as what must be exposed.
- Operation / mechanism: splitting, stretching, casting out, vacating, submission.
- Direction / force / medium: upper-to-lower progression; interior-to-exterior movement.
- Temporal development: paired `إذا` protases before human address.
- Outcome / closure: cosmic opening becomes a template for human/account exposure.
- Exact branch constituents: none available; constructional constituents from attachments.
- Unfilled roles: branch-certified lexical images for each root.
- Status: FRAGMENT, structurally strong but branch-blocked.

### IMAGE S84-IMG-02

- Starting seed: `84:6 كادح إلى ربك كدحا فملاقيه`.
- Complete image: strenuous directed movement ending in meeting.
- Passage-order assembly: human addressed -> striving intensified -> goal named -> result meeting -> outcomes split.
- Participants and roles: human traveler/worker; Lord as endpoint; meeting as closure.
- Operation / mechanism: directed exertion plus result `فـ`.
- Direction / force / medium: toward Lord.
- Temporal development: after cosmic opening and before record bifurcation.
- Outcome / closure: record and return scenes test the meeting.
- Exact branch constituents: none available; constructional constituents from attachments.
- Unfilled roles: branch-certified `ك د ح` and `ل ق ي`.
- Status: FRAGMENT, constructionally coherent.

### IMAGE S84-IMG-03

- Starting seed: repeated `أوتي كتابه`.
- Complete image: accountability object placed according to bodily orientation.
- Passage-order assembly: right-hand reception -> easy account -> joyful return; behind-back reception -> destruction call -> blazing domain.
- Participants and roles: recipient, book, receiving side/location, account, family, punishment.
- Operation / mechanism: passive giving/receiving and result sequence.
- Direction / force / medium: right side versus behind back.
- Temporal development: two parallel `أما` branches.
- Outcome / closure: future states explained by past joy and false non-return.
- Exact branch constituents: none available; constructional constituents from attachments.
- Unfilled roles: branch-certified book/side/back imagery.
- Status: FRAGMENT, structurally strong.

### IMAGE S84-IMG-04

- Starting seed: repeated `أهله مسرورا`.
- Complete image: joy either arrives after true return or had enclosed a false no-return assumption.
- Passage-order assembly: joyful return to family -> bad case explained as past joy among family -> false thought of no return -> divine seeing.
- Participants and roles: person, family, joy, assumption, Lord as seer.
- Operation / mechanism: repeated phrase revalued by sequence.
- Direction / force / medium: return into family versus enclosure within family.
- Temporal development: future joy reactivated by past joy.
- Outcome / closure: divine seeing defeats false enclosure.
- Exact branch constituents: none available.
- Unfilled roles: branch-certified `س ر ر`, `أ ه ل`, `ق ل ب`, `ب ص ر`.
- Status: FRAGMENT, strong temporal reactivation.

### IMAGE S84-IMG-05

- Starting seed: `الشفق / الليل وما وسق / القمر إذا اتسق / طبقا عن طبق`.
- Complete image: gathered phases producing layer-to-layer traversal.
- Passage-order assembly: twilight -> night gathers -> moon coheres -> you ride stage upon stage.
- Participants and roles: transition light, night container, gathered contents, coherent moon, traversing hearers.
- Operation / mechanism: phase transition, gathering, coherence, layered riding.
- Direction / force / medium: stage across stage.
- Temporal development: oath signs culminate in oath answer.
- Outcome / closure: human refusal becomes discordant with cosmic order.
- Exact branch constituents: none available.
- Unfilled roles: branch-certified `شفق`, `وسق`, `اتسق`, `طبق`, `ركب`.
- Status: FRAGMENT, constructionally coherent.

### IMAGE S84-IMG-06

- Starting seed: `قريء عليهم القرآن لا يسجدون`.
- Complete image: recited exposure meets bodily refusal and concealed denial.
- Passage-order assembly: why no faith? -> recitation upon them -> no prostration -> denial -> God knows what they contain -> announcement -> exception.
- Participants and roles: hearers, recited Qur'an, body/prostration, deniers, concealed contents, announcer, excepted faithful group.
- Operation / mechanism: recitation placed upon, expected response withheld, concealed contents known.
- Direction / force / medium: recitation upon hearers; knowledge into concealed interior.
- Temporal development: follows stage oath and closes into exception.
- Outcome / closure: punishment announcement and faithful exception.
- Exact branch constituents: none available.
- Unfilled roles: branch-certified `ق ر ء`, `س ج د`, `ك ذ ب`, `أ م ن`, `ع م ل`, `ص ل ح`.
- Status: FRAGMENT, constructionally coherent.

## Exhaustiveness check after file creation

Checked against the recoverable S84 rooted occurrence sequence from `resources/attachments.tsv` and the sacred text in `resources/quran/surah_84.json`:

- First rooted interval word restarted: `84:1:2 السماء`, with preceding `84:1:1 إذا` treated as temporal construction seed.
- Every rooted occurrence recoverable from attachment rows is present in the seed ledger.
- Every major actual construction named in `stage1.md` categories is present: lexical occurrence seed, construction seed, morphosyntactic seed, temporal/acoustic seed, repeated phrase seed, oath sequence seed, exception seed.
- No Stage 2 work was performed.
- No translation was used as evidence.
- No branch IDs were fabricated.
- The artifact is not fully branch-exhaustive because the required furuq and QAC databases are empty in this workspace. The missing branch layer is explicitly marked as the controlling constraint on all grades.
