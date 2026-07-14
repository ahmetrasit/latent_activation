# S96 Stage 1 Pass 2: Temporally Conditioned Reactivation

Assigned passage: S96, ayat 1-19  
Sacred Arabic text source: `resources/quran/surah_96.json`  
Prompt: `v1/prompts/stage1.md`  

## Root Cause Of Pass 1 Limitation

Pass 1 visited only a limited number of words per finding because the two required lexical resources were unusable in this workspace:

- `resources/qac.sqlite` exists as a zero-byte SQLite file and has no schema or tables. The required `qac_words` and `qac_morphemes` queries therefore cannot return rooted word sequence, lemmas, morphology, measures, or morphemes.
- `resources/furuq_v4.sqlite` exists as a zero-byte SQLite file and has no schema or tables. The required `branch_images` query therefore cannot return any uncontaminated `branch_id`, `branch_image_ar`, or `what_is_ar`.

I restarted from the first rooted occurrence and initiated a seed pass for every eligible rooted occurrence visible from the sacred Arabic text and the permitted S96 attachment rows. Because the lexical branch source is unavailable, no lexical branch seed can be completed without inventing branch IDs or branch prose. I therefore mark lexical branch seeds as terminated rather than silently omitting them or replacing furuq evidence with unsupported general Arabic meanings.

Permitted resources actually usable:

- Sacred Arabic text: `resources/quran/surah_96.json`
- Structural attachments: S96 rows from `resources/attachments.tsv`

Unavailable for evidence:

- QAC morphology and morpheme data from `resources/qac.sqlite`
- Furuq branch dossiers from `resources/furuq_v4.sqlite`

## Sacred Passage Order

0. Opening context, not a seed: `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`
1. `ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ`
2. `خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ`
3. `ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ`
4. `ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ`
5. `عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ`
6. `كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ`
7. `أَن رَّءَاهُ ٱسْتَغْنَىٰٓ`
8. `إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ`
9. `أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ`
10. `عَبْدًا إِذَا صَلَّىٰٓ`
11. `أَرَءَيْتَ إِن كَانَ عَلَى ٱلْهُدَىٰٓ`
12. `أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ`
13. `أَرَءَيْتَ إِن كَذَّبَ وَتَوَلَّىٰٓ`
14. `أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ`
15. `كَلَّا لَئِن لَّمْ يَنتَهِ لَنَسْفَعًۢا بِٱلنَّاصِيَةِ`
16. `نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ`
17. `فَلْيَدْعُ نَادِيَهُۥ`
18. `سَنَدْعُ ٱلزَّبَانِيَةَ`
19. `كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩`

## Lexical Seed Ledger

Each lexical occurrence below was restarted as its own seed pass in passage order. For each one, the initial image could not be formed at the required lexical standard because the accepted branch list is unavailable. All lexical branches are therefore failed seeds pending restoration of `qac.sqlite` and `furuq_v4.sqlite`.

Format: `candidate_id | occurrence | visible/attachment root | result`.

1. `S96-L001 | 96:1:1 ٱقْرَأْ | ق ر أ | terminated: no QAC morpheme row and no furuq branch dossier; grade unlikely`.
2. `S96-L002 | 96:1:3 ٱسْمِ | س م و | terminated: no branch dossier; attachment only gives prep complement to ٱقْرَأْ; grade unlikely`.
3. `S96-L003 | 96:1:4 رَبِّكَ | ر ب ب | terminated: no branch dossier; attachment only gives idafa with ٱسْمِ; grade unlikely`.
4. `S96-L004 | 96:1:6 خَلَقَ | خ ل ق | terminated: no branch dossier; attachment only gives relative-clause head; grade unlikely`.
5. `S96-L005 | 96:2:1 خَلَقَ | خ ل ق | terminated: no branch dossier; attachment gives direct object and source complement; grade unlikely`.
6. `S96-L006 | 96:2:2 ٱلْإِنسَٰنَ | أ ن س | terminated: no branch dossier; attachment gives object of خَلَقَ; grade unlikely`.
7. `S96-L007 | 96:2:4 عَلَقٍ | ع ل ق | terminated: no branch dossier; attachment gives مِنْ source complement; grade unlikely`.
8. `S96-L008 | 96:3:1 ٱقْرَأْ | ق ر أ | terminated: repeated command occurrence, no branch dossier; grade unlikely`.
9. `S96-L009 | 96:3:3 رَبُّكَ | ر ب ب | terminated: no branch dossier; attachment gives conjoined nominal clause; grade unlikely`.
10. `S96-L010 | 96:3:4 ٱلْأَكْرَمُ | ك ر م | terminated: no branch dossier; attachment gives predicate of رَبُّكَ; grade unlikely`.
11. `S96-L011 | 96:4:2 عَلَّمَ | ع ل م | terminated: no branch dossier; attachment gives subject and instrument; grade unlikely`.
12. `S96-L012 | 96:4:3 ٱلْقَلَمِ | ق ل م | terminated: no branch dossier; attachment gives بِ instrument complement; grade unlikely`.
13. `S96-L013 | 96:5:1 عَلَّمَ | ع ل م | terminated: no branch dossier; attachment gives two-object teaching frame; grade unlikely`.
14. `S96-L014 | 96:5:2 ٱلْإِنسَٰنَ | أ ن س | terminated: no branch dossier; attachment gives first object of عَلَّمَ; grade unlikely`.
15. `S96-L015 | 96:5:5 يَعْلَمْ | ع ل م | terminated: no branch dossier; attachment gives لَمْ complement and fronted object; grade unlikely`.
16. `S96-L016 | 96:6:3 ٱلْإِنسَٰنَ | أ ن س | terminated: no branch dossier; attachment gives governed noun of إِنَّ; grade unlikely`.
17. `S96-L017 | 96:6:5 لَيَطْغَىٰ | ط غ ي | terminated: no branch dossier; attachment gives predicate of إِنَّ; grade unlikely`.
18. `S96-L018 | 96:7:2 رَّءَاهُ | ر أ ي | terminated: no branch dossier; attachment gives verbal complement and object suffix; grade unlikely`.
19. `S96-L019 | 96:7:3 ٱسْتَغْنَىٰ | غ ن ي | terminated: no branch dossier; attachment gives circumstantial state of the seen self; grade unlikely`.
20. `S96-L020 | 96:8:3 رَبِّكَ | ر ب ب | terminated: no branch dossier; attachment gives destination complement of الرجعى; grade unlikely`.
21. `S96-L021 | 96:8:4 ٱلرُّجْعَىٰ | ر ج ع | terminated: no branch dossier; attachment gives governed noun/predication frame; grade unlikely`.
22. `S96-L022 | 96:9:1 أَرَءَيْتَ | ر أ ي | terminated: no branch dossier; attachment gives direct object scenario; grade unlikely`.
23. `S96-L023 | 96:9:3 يَنْهَىٰ | ن ه ي | terminated: no branch dossier; attachment gives relative clause predicate; grade unlikely`.
24. `S96-L024 | 96:10:1 عَبْدًا | ع ب د visible from sacred text | terminated: no QAC/branch data and no attachment row for this token; grade unlikely`.
25. `S96-L025 | 96:10:3 صَلَّىٰ | ص ل و | terminated: no branch dossier; attachment gives temporal condition under إِذَا; grade unlikely`.
26. `S96-L026 | 96:11:1 أَرَءَيْتَ | ر أ ي | terminated: no branch dossier; repeated scenario opener; grade unlikely`.
27. `S96-L027 | 96:11:3 كَانَ | ك و ن | terminated: no branch dossier; attachment gives عَلَى ٱلْهُدَى as khabar; grade unlikely`.
28. `S96-L028 | 96:11:5 ٱلْهُدَىٰ | ه د ي | terminated: no branch dossier; attachment gives عَلَى complement and kana predicate; grade unlikely`.
29. `S96-L029 | 96:12:2 أَمَرَ | أ م ر | terminated: no branch dossier; attachment gives بِٱلتَّقْوَى complement; grade unlikely`.
30. `S96-L030 | 96:12:3 ٱلتَّقْوَىٰ | و ق ي | terminated: no branch dossier; attachment gives commanded content; grade unlikely`.
31. `S96-L031 | 96:13:1 أَرَءَيْتَ | ر أ ي | terminated: no branch dossier; repeated scenario opener; grade unlikely`.
32. `S96-L032 | 96:13:3 كَذَّبَ | ك ذ ب | terminated: no branch dossier; attachment gives conjoined وَتَوَلَّى; grade unlikely`.
33. `S96-L033 | 96:13:5 تَوَلَّىٰ | و ل ي | terminated: no branch dossier; attachment gives coordination with كَذَّبَ; grade unlikely`.
34. `S96-L034 | 96:14:2 يَعْلَم | ع ل م | terminated: no branch dossier; attachment gives بِأَنَّ content clause; grade unlikely`.
35. `S96-L035 | 96:14:4 ٱللَّهَ | أ ل ه | terminated: no branch dossier; attachment gives subject of يَرَى; grade unlikely`.
36. `S96-L036 | 96:14:5 يَرَىٰ | ر أ ي | terminated: no branch dossier; attachment gives predicate of أَنَّ; grade unlikely`.
37. `S96-L037 | 96:15:5 يَنتَهِ | ن ه ي visible from sacred text | terminated: no branch dossier and no direct attachment row for this token; grade unlikely`.
38. `S96-L038 | 96:15:7 لَنَسْفَعًۢا | س ف ع | terminated: no branch dossier; attachment gives بِٱلنَّاصِيَة complement; grade unlikely`.
39. `S96-L039 | 96:15:9 ٱلنَّاصِيَةِ | ن ص ي | terminated: no branch dossier; attachment gives بِ complement of لَنَسْفَعًا; grade unlikely`.
40. `S96-L040 | 96:16:1 نَاصِيَةٍ | ن ص ي | terminated: no branch dossier; attachment gives adjective frame; grade unlikely`.
41. `S96-L041 | 96:16:2 كَٰذِبَةٍ | ك ذ ب | terminated: no branch dossier; attachment gives adjective of نَاصِيَة; grade unlikely`.
42. `S96-L042 | 96:16:3 خَاطِئَةٍ | خ ط أ | terminated: no branch dossier; attachment gives second adjective of نَاصِيَة; grade unlikely`.
43. `S96-L043 | 96:17:3 فَلْيَدْعُ | د ع ع in attachment for دعو-like surface | terminated: no branch dossier; attachment gives object نَادِيَه; grade unlikely`.
44. `S96-L044 | 96:17:4 نَادِيَهُۥ | ن د ي | terminated: no branch dossier; attachment gives called object and possessive suffix; grade unlikely`.
45. `S96-L045 | 96:18:1 سَنَدْعُ | د ع ع in attachment for دعو-like surface | terminated: no branch dossier; attachment gives object ٱلزَّبَانِيَةَ; grade unlikely`.
46. `S96-L046 | 96:18:2 ٱلزَّبَانِيَةَ | ز ب ن | terminated: no branch dossier; attachment gives accusative object of سَنَدْعُ; grade unlikely`.
47. `S96-L047 | 96:19:3 تُطِعْهُ | ط و ع | terminated: no branch dossier; attachment gives object suffix; grade unlikely`.
48. `S96-L048 | 96:19:5 ٱسْجُدْ | س ج د | terminated: no branch dossier; attachment gives command conjoined to لا تطعه; grade unlikely`.
49. `S96-L049 | 96:19:7 ٱقْتَرِب | ق ر ب | terminated: no branch dossier; attachment gives command conjoined to ٱسْجُدْ; grade unlikely`.

## Constructional And Morphosyntactic Seed Passes

The following are constructional seeds actually runnable from the sacred text plus S96 attachment rows. These are not substitutes for lexical branch synthesis. They are provisional structural image-branches, graded conservatively because they lack furuq branch corroboration.

### S96-C001: Command Through Name To Creator

- `candidate_id`: S96-C001
- `ayah_range`: 96:1
- `seed_type`: constructional
- `seed`: `ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ`
- `generating_set`: `(E: attachment 96:1 a1, بِٱسْمِ governed by ٱقْرَأْ)`, `(E: attachment 96:1 a2, رَبِّكَ completes ٱسْمِ)`, `(E: attachment 96:1 a3-a4, relative clause ties رَبِّكَ to خَلَقَ)`
- `selected_branches`: none; furuq unavailable.
- `constructed_model`: A recitational command opens not as autonomous reading/speech but as an act routed through a named Lord, immediately specified by creative action. The command activates dependence before content.
- `freeze_point`: after the 96:1 idafa and relative-clause chain.
- `predictions_at_freeze`: later material should identify what this Lord has done, how the commanded act is enabled, and whether human independence is constrained.
- `unused_features_tested`: 96:2 creation of الإنسان from علق; 96:3-5 repeated command and teaching; 96:6-8 human overreach and return; opening basmala as name-context.
- `corroborators`: `(C: sequence 96:1→96:5, command is followed by creation and teaching frames)`, `(C: basmala opening-context, invocation/name frame precedes بِٱسْمِ)`, `(C: attachment 96:8 a2-a3, return is إلى ربك)`
- `constraints`: `(K: no QAC morphology or furuq branches; lexical content cannot be branch-verified)`, `(K: بِٱسْمِ is a governed complement, not an independent lexical image)`
- `temporal_reactivation_notes`: The later `إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰ` reactivates the initial `رَبِّكَ` as endpoint, not only opening attribution.
- `rival_models`: A generic liturgical-opening model is possible, but it fails to account for the immediate creator/teacher sequence and later return.
- `grade`: medium
- `grade_rationale`: Strong structural attachment and sequence; weak lexical depth because branch dossiers are unavailable.
- `source_queries_or_rows_used`: S96 sacred text; attachment rows 96:1 a1-a4, 96:8 a2-a3.

### S96-C002: Human Origin From Attachment/Substance

- `candidate_id`: S96-C002
- `ayah_range`: 96:2
- `seed_type`: constructional
- `seed`: `خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ`
- `generating_set`: `(E: attachment 96:2 a1, ٱلْإِنسَٰنَ direct object of خَلَقَ)`, `(E: attachment 96:2 a2, عَلَقٍ governed by مِنْ as source complement)`
- `selected_branches`: none; furuq unavailable.
- `constructed_model`: The human is introduced as an object of making with a source-from relation. The emerging image is not self-originating agency but dependence on a prior formative source.
- `freeze_point`: after object plus مِنْ source complement.
- `predictions_at_freeze`: later human status should be unstable if detached from origin; later divine action may supply formation or knowledge.
- `unused_features_tested`: 96:5 teaching the human unknown content; 96:6 human طغيان; 96:7 seeing self as self-sufficient.
- `corroborators`: `(C: sequence 96:2→96:5, same الإنسان is later taught what it did not know)`, `(C: sequence 96:6→96:7, overreach is specifically tied to seeing oneself self-sufficient)`
- `constraints`: `(K: no ع ل ق branch dossier; cannot decide which branch-image of عَلَق is active)`, `(K: no QAC morphology for case/morpheme verification beyond attachment row)`
- `temporal_reactivation_notes`: 96:7 `ٱسْتَغْنَىٰ` reactivates 96:2 as contrast: the human who had source-dependence later sees sufficiency.
- `rival_models`: Biological-origin-only model; structural-dependence model. The second better predicts later sufficiency conflict but remains unverified lexically.
- `grade`: medium
- `grade_rationale`: Clear constructional sequence and later contrast; no branch evidence.
- `source_queries_or_rows_used`: S96 sacred text; attachment rows 96:2 a1-a2.

### S96-C003: Repeated Command And Superlative Lord

- `candidate_id`: S96-C003
- `ayah_range`: 96:1-3
- `seed_type`: temporal/acoustic
- `seed`: repeated `ٱقْرَأْ` at 96:1 and 96:3 with intervening creation and following `وَرَبُّكَ ٱلْأَكْرَمُ`
- `generating_set`: `(E: sacred sequence repeated imperative)`, `(E: attachment 96:3 a1, ٱلْأَكْرَمُ predicate of رَبُّكَ)`, `(E: attachment 96:3 a2, nominal clause conjoined with command)`
- `selected_branches`: none.
- `constructed_model`: The first command opens under the Lord's name and creative act; the second resumes the same command after origin has been stated and adds a predicate of exceeding generosity/nobility. The repetition creates a command whose basis thickens over time.
- `freeze_point`: after 96:3.
- `predictions_at_freeze`: the next material should explain the Lord's generosity through an enabling act related to the command.
- `unused_features_tested`: 96:4-5 teaching by pen and teaching the human what he did not know.
- `corroborators`: `(C: sequence 96:4→96:5, teaching follows the repeated command and fills the enablement role)`, `(C: attachment 96:4 a2, بِٱلْقَلَمِ instrument complement)`
- `constraints`: `(K: no ق ر أ or ك ر م branch dossiers; cannot test lexical image of reading, collecting, nobility, generosity, or related branch structure)`
- `temporal_reactivation_notes`: The second `ٱقْرَأْ` reactivates the first with additional creation context; 96:4-5 retroactively make the command plausible by adding teaching.
- `rival_models`: Simple emphatic repetition; temporal thickening of command. The latter explains the immediate teaching continuation.
- `grade`: medium
- `grade_rationale`: Good sequence prediction; no lexical branch support.
- `source_queries_or_rows_used`: S96 sacred text; attachment rows 96:3 a1-a2, 96:4 a2.

### S96-C004: Teaching By Instrument

- `candidate_id`: S96-C004
- `ayah_range`: 96:4
- `seed_type`: constructional
- `seed`: `ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ`
- `generating_set`: `(E: attachment 96:4 a1, ٱلَّذِى subject of عَلَّمَ)`, `(E: attachment 96:4 a2, ٱلْقَلَمِ governed by prefixed بِ as instrument of عَلَّمَ)`
- `selected_branches`: none.
- `constructed_model`: The relative clause specifies the Lord's generosity by an act of teaching mediated through an instrument. The image is transmission by a means rather than innate possession.
- `freeze_point`: after instrument attachment.
- `predictions_at_freeze`: the next line should name the learner and the absence that teaching overcomes.
- `unused_features_tested`: 96:5 `عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ`.
- `corroborators`: `(C: attachment 96:5 a1-a4, two-object teaching and prior non-knowledge)`
- `constraints`: `(K: no ع ل م or ق ل م branch dossiers; instrument image cannot be lexically deepened)`
- `temporal_reactivation_notes`: The instrument in 96:4 prepares the explicit human learning gap in 96:5.
- `rival_models`: Instrumental writing model versus general mediated instruction model; branch data needed to choose.
- `grade`: medium
- `grade_rationale`: Attachment evidence is strong; branch evidence absent.
- `source_queries_or_rows_used`: attachment rows 96:4 a1-a2, 96:5 a1-a4.

### S96-C005: Human Non-Knowledge Filled By Teaching

- `candidate_id`: S96-C005
- `ayah_range`: 96:5
- `seed_type`: constructional
- `seed`: `عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ`
- `generating_set`: `(E: attachment 96:5 a1, ٱلْإِنسَٰنَ first object of عَلَّمَ)`, `(E: attachment 96:5 a2, مَا second object)`, `(E: attachment 96:5 a3-a4, مَا fronted object inside يَعْلَمْ and لَمْ governs يَعْلَمْ)`
- `selected_branches`: none.
- `constructed_model`: The human is positioned as recipient of unknown content. The same human previously created from a source is now completed through received knowledge.
- `freeze_point`: after 96:5.
- `predictions_at_freeze`: later disorder may arise if the recipient mistakes received completion for independent sufficiency.
- `unused_features_tested`: 96:6-7 `ٱلْإِنسَٰنَ لَيَطْغَىٰ` and `رَّءَاهُ ٱسْتَغْنَىٰ`.
- `corroborators`: `(C: repetition of ٱلْإِنسَٰنَ from 96:2 to 96:5 to 96:6)`, `(C: sequence from received knowledge to self-sufficiency claim)`
- `constraints`: `(K: no ع ل م branch dossier; cannot separate knowledge, marking, teaching, or other branch images)`
- `temporal_reactivation_notes`: 96:6 immediately reactivates the same human as a possible violator after the gift of teaching.
- `rival_models`: Pure benefaction model; benefaction-then-misrecognition model. The second predicts 96:6-7 better.
- `grade`: medium
- `grade_rationale`: Good temporal fit; no lexical branch validation.
- `source_queries_or_rows_used`: S96 sacred text; attachment rows 96:5 a1-a4, 96:6 a1-a2, 96:7 a1-a3.

### S96-C006: Overreach By Seeing Self-Sufficiency

- `candidate_id`: S96-C006
- `ayah_range`: 96:6-7
- `seed_type`: constructional
- `seed`: `كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ / أَن رَّءَاهُ ٱسْتَغْنَىٰٓ`
- `generating_set`: `(E: attachment 96:6 a1, ٱلْإِنسَٰنَ governed noun of إِنَّ)`, `(E: attachment 96:6 a2, لَيَطْغَى predicate)`, `(E: attachment 96:7 a1-a3, seeing self and self-sufficiency as circumstantial state)`
- `selected_branches`: none.
- `constructed_model`: A dependent recipient becomes overreaching when perception turns reflexive: he sees himself in a state of sufficiency. The error is not merely possession but a seeing-frame that reorganizes prior dependence.
- `freeze_point`: after 96:7.
- `predictions_at_freeze`: the passage should reassert endpoint, oversight, or return to the Lord named earlier.
- `unused_features_tested`: 96:8 return to `رَبِّكَ`; 96:14 divine seeing.
- `corroborators`: `(C: attachment 96:8 a2-a3, إلى ربك fronted destination of الرجعى)`, `(C: attachment 96:14 a1-a4, يعلم content that Allah sees)`, `(C: temporal contrast between رَّءَاهُ and يَرَىٰ)`
- `constraints`: `(K: no ط غ ي, ر أ ي, or غ ن ي branch dossiers; cannot build a lexical image of overflow, sight, or sufficiency)`
- `temporal_reactivation_notes`: The human origin/teaching frames are reactivated as what the self-sufficiency perception suppresses. Later divine seeing counters self-seeing.
- `rival_models`: Moral arrogance model; perceptual misframing model. The attachment of `رَآهُ` to `ٱسْتَغْنَىٰ` supports the perceptual model structurally.
- `grade`: medium-strong
- `grade_rationale`: Multiple independent structural reactivations; still lacking lexical branch dossiers.
- `source_queries_or_rows_used`: attachment rows 96:6 a1-a2, 96:7 a1-a3, 96:8 a1-a3, 96:14 a1-a4.

### S96-C007: Return To The Opening Lord

- `candidate_id`: S96-C007
- `ayah_range`: 96:8
- `seed_type`: constructional
- `seed`: `إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ`
- `generating_set`: `(E: attachment 96:8 a1, ٱلرُّجْعَى governed noun of إِنَّ)`, `(E: attachment 96:8 a2, رَبِّكَ governed by إِلَى as destination complement)`, `(E: attachment 96:8 a3, إِلَىٰ رَبِّكَ as fronted predicate)`
- `selected_branches`: none.
- `constructed_model`: The passage redirects the self-sufficiency scene toward a destination: return is to the same Lord introduced at the opening. The fronted destination constrains the human's imagined independence.
- `freeze_point`: after 96:8.
- `predictions_at_freeze`: later conflict should be judged by seeing/knowledge of the Lord, and commands should return to obedience/proximity rather than obeying the overreacher.
- `unused_features_tested`: 96:14 `ٱللَّهَ يَرَىٰ`; 96:19 `لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب`.
- `corroborators`: `(C: repetition رَبِّكَ from 96:1, 96:3, 96:8)`, `(C: sequence 96:8→96:14→96:19, return/oversight/proximity frame)`
- `constraints`: `(K: no ر ج ع or ر ب ب branch dossiers)`
- `temporal_reactivation_notes`: 96:8 backward-reactivates the named Lord of the first command and forward-prepares final nearness.
- `rival_models`: Eschatological-return only; discourse-return-to-opening-Lord. The latter is structurally more explanatory for the surah order.
- `grade`: medium
- `grade_rationale`: Strong sequence and recurrence; lexical data absent.
- `source_queries_or_rows_used`: attachment rows 96:8 a1-a3; sacred repeated `رَبِّكَ`.

### S96-C008: Prohibition Of A Praying Servant

- `candidate_id`: S96-C008
- `ayah_range`: 96:9-10
- `seed_type`: constructional
- `seed`: `أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ / عَبْدًا إِذَا صَلَّىٰٓ`
- `generating_set`: `(E: attachment 96:9 a1, ٱلَّذِى direct object of أَرَءَيْتَ)`, `(E: attachment 96:9 a2, ٱلَّذِى subject of يَنْهَى)`, `(E: attachment 96:10 a1, إِذَا sets temporal condition for صَلَّى)`
- `selected_branches`: none.
- `constructed_model`: The seeing-question shifts from self-seeing to audience-seeing: observe one who forbids a servant at the time of prayer. The model activates obstruction of worship under a scenario frame.
- `freeze_point`: after 96:10.
- `predictions_at_freeze`: the passage should test whether the servant's action is guided/protective or whether the forbidder is lying/turning away.
- `unused_features_tested`: 96:11-13 guidance, command to taqwa, denial and turning away.
- `corroborators`: `(C: repeated أَرَءَيْتَ scenario sequence at 96:9, 96:11, 96:13)`, `(C: attachment 96:11 a1-a3, guided scenario)`, `(C: attachment 96:13 a1-a2, denial/turning scenario)`
- `constraints`: `(K: no ن ه ي, ع ب د, or ص ل و branch dossiers)`, `(K: عَبْدًا lacks an attachment row in the allowed S96 extract, so its syntactic role cannot be attachment-verified here)`
- `temporal_reactivation_notes`: The earlier self-seeing problem becomes a public seeing-question about someone blocking worship.
- `rival_models`: General moral example; judicial display of an obstructer. Repeated `أَرَءَيْتَ` favors the display/testing model.
- `grade`: medium
- `grade_rationale`: Good discourse structure; missing lexical branches and one missing attachment for `عَبْدًا`.
- `source_queries_or_rows_used`: attachment rows 96:9 a1-a2, 96:10 a1, 96:11 a1-a3, 96:13 a1-a2.

### S96-C009: Guided Command Versus Denial And Turning

- `candidate_id`: S96-C009
- `ayah_range`: 96:11-13
- `seed_type`: morphosyntactic
- `seed`: paired `أَرَءَيْتَ` scenarios: `إِن كَانَ عَلَى ٱلْهُدَىٰ / أَوْ أَمَرَ بِٱلتَّقْوَىٰ` against `إِن كَذَّبَ وَتَوَلَّىٰ`
- `generating_set`: `(E: attachment 96:11 a1, أَرَءَيْتَ takes conditional scenario)`, `(E: attachment 96:11 a2-a3, عَلَى ٱلْهُدَى predicate of كَانَ)`, `(E: attachment 96:12 a1, بِٱلتَّقْوَى complement of أَمَرَ)`, `(E: attachment 96:13 a1-a2, conditional denial and conjoined turning)`
- `selected_branches`: none.
- `constructed_model`: The passage sets a forked evaluation: a servant may be on guidance or command protective piety, while the obstructer may deny and turn away. The image is a courtroom-like contrast of possible orientation and counter-orientation.
- `freeze_point`: after 96:13.
- `predictions_at_freeze`: knowledge/seeing by Allah should decide the hidden orientation; physical or social power should be displaced.
- `unused_features_tested`: 96:14 divine knowledge/seeing; 96:17-18 calling one's assembly versus counter-calling.
- `corroborators`: `(C: attachment 96:14 a1-a4, يعلم content that Allah sees)`, `(C: attachment 96:17 a1 and 96:18 a1, human call countered by divine call)`
- `constraints`: `(K: no ه د ي, أ م ر, و ق ي, ك ذ ب, or و ل ي branch dossiers)`
- `temporal_reactivation_notes`: The repeated `أَرَءَيْتَ` keeps reactivating the earlier perception problem while shifting from self-perception to evaluated public conduct.
- `rival_models`: Two independent examples; one evaluative fork. Parallel scenario syntax favors the fork.
- `grade`: medium-strong
- `grade_rationale`: Strong morphosyntactic parallelism and sequence; lexical depth unavailable.
- `source_queries_or_rows_used`: attachment rows 96:11 a1-a3, 96:12 a1, 96:13 a1-a2, 96:14 a1-a4, 96:17 a1, 96:18 a1.

### S96-C010: Divine Seeing Counters Human Seeing

- `candidate_id`: S96-C010
- `ayah_range`: 96:7, 96:14
- `seed_type`: temporal/acoustic
- `seed`: recurrence of seeing: `رَّءَاهُ` and `ٱللَّهَ يَرَىٰ`
- `generating_set`: `(E: attachment 96:7 a1-a3, self-seeing in sufficiency)`, `(E: attachment 96:14 a1-a4, يعلم that Allah sees)`
- `selected_branches`: none.
- `constructed_model`: The passage creates a perception contest. Human overreach begins when the human sees himself sufficient; the corrective disclosure is that Allah sees. Seeing moves from self-enclosed appraisal to divine oversight.
- `freeze_point`: after 96:14.
- `predictions_at_freeze`: coercive correction and refusal to obey the obstructer should follow.
- `unused_features_tested`: 96:15-16 seizure by forelock; 96:19 no obedience, prostration, nearness.
- `corroborators`: `(C: attachment 96:15 a1, بِٱلنَّاصِيَةِ complement of لَنَسْفَعًا)`, `(C: attachment 96:19 a1-a3, object not obeyed, then prostration and approach)`
- `constraints`: `(K: no ر أ ي branch dossier; cannot test whether the same branch-image operates in both occurrences)`, `(K: no QAC morphology for aspect/mood beyond attachment labels)`
- `temporal_reactivation_notes`: 96:14 strongly reactivates 96:7 and reframes the earlier self-seeing as an inadequate field of vision.
- `rival_models`: General omniscience assertion; direct correction of self-seeing. Repeated seeing supports the latter.
- `grade`: medium-strong
- `grade_rationale`: Strong recurrence and discourse placement; no branch evidence.
- `source_queries_or_rows_used`: attachment rows 96:7 a1-a3, 96:14 a1-a4, 96:15 a1, 96:19 a1-a3.

### S96-C011: Forelock Marked By False And Erring Description

- `candidate_id`: S96-C011
- `ayah_range`: 96:15-16
- `seed_type`: constructional
- `seed`: `لَنَسْفَعًۢا بِٱلنَّاصِيَةِ / نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ`
- `generating_set`: `(E: attachment 96:15 a1, ٱلنَّاصِيَة governed by بِ as complement of لَنَسْفَعًا)`, `(E: attachment 96:16 a1-a2, كَٰذِبَة and خَاطِئَة adjectives of نَاصِيَة)`
- `selected_branches`: none.
- `constructed_model`: The threatened correction targets the front/forelock and then labels it with moral-cognitive predicates: lying and erring. The body-part focus concentrates the earlier seeing/denial problem at the locus of leading orientation.
- `freeze_point`: after 96:16.
- `predictions_at_freeze`: social backing may be invoked by the threatened party and answered by a stronger summoned force.
- `unused_features_tested`: 96:17-18 calling his assembly and counter-calling الزبانية.
- `corroborators`: `(C: sequence 96:16→96:18, marked forelock followed by call/counter-call escalation)`, `(C: attachment 96:17 a1-a2 and 96:18 a1, direct objects of call verbs)`
- `constraints`: `(K: no س ف ع, ن ص ي, ك ذ ب, or خ ط أ branch dossiers; cannot lexicalize forelock, seizing, lying, or erring images)`, `(K: adjective agreement is structural evidence, not lexical branch evidence)`
- `temporal_reactivation_notes`: The lying adjective reactivates 96:13 `كَذَّبَ`; the body focus converts denial/turning from scenario into a marked target.
- `rival_models`: Literal punishment image; cognitive-orientational marking image. The adjective structure supports a moralized body target but cannot decide branch depth.
- `grade`: medium
- `grade_rationale`: Clear local syntax and recurrence of كذب; lexical branch evidence absent.
- `source_queries_or_rows_used`: attachment rows 96:15 a1, 96:16 a1-a2, 96:17 a1-a2, 96:18 a1.

### S96-C012: Human Call And Counter-Call

- `candidate_id`: S96-C012
- `ayah_range`: 96:17-18
- `seed_type`: constructional
- `seed`: `فَلْيَدْعُ نَادِيَهُۥ / سَنَدْعُ ٱلزَّبَانِيَةَ`
- `generating_set`: `(E: attachment 96:17 a1, نَادِيَه object called by يَدْعُ)`, `(E: attachment 96:17 a2, possessive suffix in نَادِيَه)`, `(E: attachment 96:18 a1, ٱلزَّبَانِيَة accusative object of سَنَدْعُ)`
- `selected_branches`: none.
- `constructed_model`: A social appeal is invited and immediately overmatched by a counter-call. The obstructer who opposed a servant's prayer is permitted to summon his assembly; the response summons another force.
- `freeze_point`: after 96:18.
- `predictions_at_freeze`: final command should detach from obeying the obstructer and return to worship/proximity.
- `unused_features_tested`: 96:19 `لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب`.
- `corroborators`: `(C: attachment 96:19 a1-a3, do not obey him, prostrate, approach)`
- `constraints`: `(K: attachment root for call surfaces appears as د ع ع; without QAC/furuq this cannot be normalized or branch-tested)`, `(K: no ن د ي or ز ب ن branch dossiers)`
- `temporal_reactivation_notes`: The call/counter-call sequence resolves the social-power fork opened by the one who forbids a servant.
- `rival_models`: Social court model; force-summoning model. Both remain possible without branch dossiers.
- `grade`: medium
- `grade_rationale`: Strong local parallelism; uncertain root normalization and no branch evidence.
- `source_queries_or_rows_used`: attachment rows 96:17 a1-a2, 96:18 a1, 96:19 a1-a3.

### S96-C013: Final Non-Obedience, Prostration, And Nearness

- `candidate_id`: S96-C013
- `ayah_range`: 96:19
- `seed_type`: constructional
- `seed`: `كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب`
- `generating_set`: `(E: attachment 96:19 a1, object suffix governed by تُطِعْ)`, `(E: attachment 96:19 a2, ٱسْجُدْ conjoined to command structure)`, `(E: attachment 96:19 a3, ٱقْتَرِب conjoined to ٱسْجُدْ)`
- `selected_branches`: none.
- `constructed_model`: The passage closes by refusing obedience to the obstructer and replacing it with worshipful lowering and approach. The final movement answers both the prohibition of prayer and the return-to-Lord frame.
- `freeze_point`: after 96:19.
- `predictions_at_freeze`: closure should reactivate 96:8 return and 96:10 prayer.
- `unused_features_tested`: backward replay to 96:8 and 96:10.
- `corroborators`: `(C: sequence 96:10→96:19, prayer obstruction answered by prostration)`, `(C: sequence 96:8→96:19, return-to-Lord answered by approach)`, `(C: object suffix in لا تطعه points back to the prohibiting figure)`
- `constraints`: `(K: no ط و ع, س ج د, or ق ر ب branch dossiers)`, `(K: final سجود/proximity cannot be expanded into a lexical image beyond attachment and sacred sequence)`
- `temporal_reactivation_notes`: The close reactivates the servant-at-prayer scene and converts the seeing/obedience conflict into an embodied command.
- `rival_models`: Mere ethical instruction; closure of the entire trajectory from command to return to approach. The latter explains closure better.
- `grade`: medium-strong
- `grade_rationale`: Strong closure and backward reactivation; lexical evidence absent.
- `source_queries_or_rows_used`: attachment rows 96:19 a1-a3; sacred text 96:8, 96:10.

## Provisional Convergence Map

Because lexical branch data is absent, this convergence map is constructional only.

- Opening dependence: S96-C001, S96-C002, S96-C003, S96-C004, S96-C005.
- Human misrecognition: S96-C005, S96-C006, S96-C007, S96-C010.
- Seeing/evaluation axis: S96-C006, S96-C008, S96-C009, S96-C010.
- Obstruction and correction: S96-C008, S96-C009, S96-C011, S96-C012, S96-C013.
- Closure by worshipful nearness: S96-C007, S96-C008, S96-C013.

Compact constructional model:

The passage opens with a command routed through the Lord's name, then supplies creation and teaching as the ground of that command. The same human recipient then overreaches through self-sufficient self-seeing. The passage answers by reasserting return to the Lord, displaying an obstructer of worship under repeated seeing-questions, opposing false/turning orientation with divine seeing, threatening a marked forelock, defeating social appeal by counter-call, and closing with non-obedience to the obstructer plus prostration and approach.

This model is not a lexical synthesis in the full Stage 1 sense because no branch IDs or branch images could be used.

## Image Packet Catalog

### IMG-S96-01

- Starting seed: S96-C001 command through name to creator.
- Complete image: command grounded in named Lord, creation, teaching, and return.
- Passage-order assembly: 96:1 command/name/Lord/creator; 96:2 human created from source; 96:3 repeated command/Lord as most generous; 96:4-5 teaching by pen and unknown content; 96:8 return to Lord.
- Participants and roles: commanded reciter/servant; Lord as creator, teacher, endpoint; human as created/taught recipient.
- Operation / mechanism: command is made possible by divine creation and teaching.
- Direction / force / medium: from Lord/name to recitation; from creation/source to human; through pen/instrument; back to Lord.
- Temporal development: command -> origin -> repeated command -> teaching -> return.
- Outcome / closure: reactivated by final approach in 96:19.
- Exact branch constituents: none available; constructional attachments only.
- Unfilled roles: lexical image of reading/name/Lord/creation/teaching/pen.
- Status: FRAGMENT.

### IMG-S96-02

- Starting seed: S96-C006 overreach by self-seeing.
- Complete image: recipient misreads dependence as sufficiency; divine seeing and return correct the field.
- Passage-order assembly: 96:2 creation; 96:5 teaching; 96:6 overreach; 96:7 self-seeing as sufficient; 96:8 return; 96:14 Allah sees.
- Participants and roles: human as dependent recipient; self-perception as distortion; Lord/Allah as endpoint and seer.
- Operation / mechanism: reflexive seeing reorganizes dependence into imagined autonomy; later seeing reverses it.
- Direction / force / medium: inward self-appraisal countered by divine oversight and return.
- Temporal development: received origin/knowledge -> overreach -> self-sufficiency perception -> return/oversight.
- Outcome / closure: final لا تطعه prevents the overreacher from becoming obeyed.
- Exact branch constituents: none available; constructional attachments only.
- Unfilled roles: lexical images for طغى, رأى, غني, رجع.
- Status: FRAGMENT.

### IMG-S96-03

- Starting seed: S96-C008 prohibition of praying servant.
- Complete image: an obstructer forbids worship; the passage stages scenarios, exposes denial/turning, marks the forelock, and overmatches the human assembly.
- Passage-order assembly: 96:9-10 forbidder and praying servant; 96:11-13 guided/taqwa scenario versus denial/turning; 96:14 divine seeing; 96:15-16 forelock; 96:17-18 call/counter-call; 96:19 do not obey, prostrate, approach.
- Participants and roles: obstructer; servant at prayer; Allah as seer and caller; human assembly; الزبانية.
- Operation / mechanism: public obstruction is evaluated, exposed, threatened, and displaced by final worship-command.
- Direction / force / medium: prohibition blocks prayer; counter-command restores prostration and approach.
- Temporal development: obstruction -> evaluative scenarios -> divine seeing -> seizure threat -> social call defeated -> worshipful closure.
- Outcome / closure: لا تطعه واسجد واقترب.
- Exact branch constituents: none available; constructional attachments only.
- Unfilled roles: lexical images for نهى, عبد, صلى, هدى, وقى, كذب, ولى, سفع, ناصية, زبن, سجد, قرب.
- Status: FRAGMENT.

## Exhaustiveness Check After File Creation

- Restarted from first rooted occurrence: yes, beginning with 96:1:1 `ٱقْرَأْ`.
- Every eligible rooted occurrence visible from the sacred text and S96 attachment rows received a seed entry: yes, 49 lexical occurrence attempts are listed.
- Every lexical branch received a seed pass: no branch list exists because `furuq_v4.sqlite` has no usable table. This is recorded as a resource failure for each lexical occurrence.
- Every eligible constructional/morphosyntactic/temporal seed recoverable from the sacred text and attachment rows received a seed pass: yes, 13 constructional or temporal candidates are listed.
- Generated, constituent, corroborative, and constraining evidence kept separate: yes, with `E`, `C`, and `K` labels.
- Branch IDs preserved where used: no branch IDs were available or used.
- Unused features tested after freeze: yes for constructional seeds; not possible for branch-failed lexical seeds.
- Images generated where possible: yes, three provisional fragment image packets are cataloged.
- Final limitation: the artifact is exhaustive under the usable permitted resources, but it is not a full lexical Stage 1 synthesis until the two required SQLite resources are restored with QAC tables and uncontaminated furuq branch dossiers.
