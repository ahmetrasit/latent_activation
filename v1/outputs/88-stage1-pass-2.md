# S88 Stage 1 Pass 2: temporally conditioned reactivation

Assigned passage: S88.
Sacred Arabic text source: `resources/quran/surah_88.json`.
Prompt: `v1/prompts/stage1.md`.

## Pass 2 restart note

Root cause of the Pass 1 limitation: Pass 1 compressed discovery into a small number of promising image-families and did not restart from every eligible rooted occurrence and construction. That caused later findings to visit only the words that looked useful for an early model. This Pass 2 restarts from the first rooted word, treats every accepted branch as visited in its root dossier, and preserves failed, local-only, and terminating seeds.

Resource note: `resources/qac.sqlite` and `resources/furuq_v4.sqlite` are empty placeholder files in this checkout, so the equivalent local TSV mirrors were used for QAC and branch rows: `resources/qac_root_ayah.tsv` and `resources/v4_branches.tsv`, plus `resources/attachments.tsv`. No translation was used.

## Ordered rooted occurrence inventory

S88 rooted occurrence order used for seed restart:

1. 88:1:2 `أَتَىٰ` root `ء ت ي`; 88:1:3 `حَدِيثُ` root `ح د ث`; 88:1:4 `غَٰشِيَةِ` root `غ ش و`.
2. 88:2:1 `وُجُوهٌ` root `و ج ه`; 88:2:3 `خَٰشِعَةٌ` root `خ ش ع`.
3. 88:3:1 `عَامِلَةٌ` root `ع م ل`; 88:3:2 `نَّاصِبَةٌ` root `ن ص ب`.
4. 88:4:1 `تَصْلَىٰ` root `ص ل ي`; 88:4:2 `نَارًا` root `ن و ر`; 88:4:3 `حَامِيَةً` root `ح م ي`.
5. 88:5:1 `تُسْقَىٰ` root `س ق ي`; 88:5:3 `عَيْنٍ` root `ع ي ن`; 88:5:4 `ءَانِيَةٍ` root `ء ن ي`.
6. 88:6:1 `لَّيْسَ` root `ل ي س`; 88:6:3 `طَعَامٌ` root `ط ع م`; 88:6:6 `ضَرِيعٍ` root `ض ر ع`.
7. 88:7:2 `يُسْمِنُ` root `س م ن`; 88:7:4 `يُغْنِى` root `غ ن ي`; 88:7:6 `جُوعٍ` root `ج و ع`.
8. 88:8:1 `وُجُوهٌ` root `و ج ه`; 88:8:3 `نَّاعِمَةٌ` root `ن ع م`.
9. 88:9:1 `سَعْيِ` root `س ع ي`; 88:9:2 `رَاضِيَةٌ` root `ر ض و`.
10. 88:10:2 `جَنَّةٍ` root `ج ن ن`; 88:10:3 `عَالِيَةٍ` root `ع ل و`.
11. 88:11:2 `تَسْمَعُ` root `س م ع`; 88:11:4 `لَٰغِيَةً` root `ل غ و`.
12. 88:12:2 `عَيْنٌ` root `ع ي ن`; 88:12:3 `جَارِيَةٌ` root `ج ر ي`.
13. 88:13:2 `سُرُرٌ` root `س ر ر`; 88:13:3 `مَّرْفُوعَةٌ` root `ر ف ع`.
14. 88:14:1 `أَكْوَابٌ` root `ك و ب`; 88:14:2 `مَّوْضُوعَةٌ` root `و ض ع`.
15. 88:15:2 `مَصْفُوفَةٌ` root `ص ف ف`.
16. 88:16:2 `مَبْثُوثَةٌ` root `ب ث ث`.
17. 88:17:2 `يَنظُرُ` root `ن ظ ر`; 88:17:4 `إِبِلِ` root `ء ب ل`; 88:17:5 `كَيْفَ` root `ك ي ف`; 88:17:6 `خُلِقَتْ` root `خ ل ق`.
18. 88:18:2 `سَّمَآءِ` root `س م و`; 88:18:3 `كَيْفَ` root `ك ي ف`; 88:18:4 `رُفِعَتْ` root `ر ف ع`.
19. 88:19:2 `جِبَالِ` root `ج ب ل`; 88:19:3 `كَيْفَ` root `ك ي ف`; 88:19:4 `نُصِبَتْ` root `ن ص ب`.
20. 88:20:2 `أَرْضِ` root `ء ر ض`; 88:20:3 `كَيْفَ` root `ك ي ف`; 88:20:4 `سُطِحَتْ` root `س ط ح`.
21. 88:21:1 `ذَكِّرْ` and 88:21:4 `مُذَكِّرٌ` root `ذ ك ر`.
22. 88:22:1 `لَّسْ` root `ل ي س`; 88:22:3 `مُصَيْطِرٍ` root `س ط ر`.
23. 88:23:3 `تَوَلَّىٰ` root `و ل ي`; 88:23:4 `كَفَرَ` root `ك ف ر`.
24. 88:24:1 and 88:24:3 `يُعَذِّبُ` / `عَذَابَ` root `ع ذ ب`; 88:24:2 `ٱللَّهُ` root `ء ل ه`; 88:24:4 `أَكْبَرَ` root `ك ب ر`.
25. 88:25:3 `إِيَابَ` root `ء و ب`.
26. 88:26:4 `حِسَابَ` root `ح س ب`.

Branch dossier coverage: all accepted branches were read for each root in the inventory. Counts: `ء ب ل` 9; `ء ت ي` 13; `ء ر ض` 12; `ء ل ه` 2; `ء ن ي` 5; `ء و ب` 5; `ب ث ث` 3; `ج ب ل` 12; `ج ر ي` 6; `ج ن ن` 15; `ج و ع` 4; `ح د ث` 7; `ح س ب` 8; `ح م ي` 12; `خ ش ع` 4; `خ ل ق` 11; `ذ ك ر` 7; `ر ض و` 7; `ر ف ع` 12; `س ر ر` 11; `س ط ح` 6; `س ط ر` 6; `س ع ي` 8; `س ق ي` 9; `س م ع` 16; `س م ن` 9; `س م و` 8; `ص ف ف` 7; `ص ل ي` 10; `ض ر ع` 13; `ط ع م` 13; `ع ذ ب` 8; `ع ل و` 11; `ع م ل` 12; `ع ي ن` 17; `غ ش و` 7; `غ ن ي` 6; `ك ب ر` 11; `ك ف ر` 15; `ك و ب` 6; `ل غ و` 6; `ل ي س` 8; `ن ص ب` 10; `ن ظ ر` 10; `ن ع م` 13; `ن و ر` 8; `و ج ه` 13; `و ض ع` 13; `و ل ي` 15. No uncontaminated branch rows were available for `ك ي ف`.

## Candidate synthesis units

### S88-CSU-01: The covering report arrives, then turns faces into exposed evidence

- `candidate_id`: S88-CSU-01
- `ayah_range`: 88:1-2, reactivated at 88:8 and constrained by 88:24-26
- `seed_type`: lexical
- `seed`: 88:1:2 `أَتَىٰ` root `ء ت ي`, especially B001 arrival and B011 arrival of calamity
- `generating_set`: `(E: ء ت ي B001 arrival)`, `(E: ح د ث B003 renewed report)`, `(E: غ ش و B001 cover over a thing; B002 comprehensive covering)`, `(E: و ج ه B001 face/front)`, `(E: خ ش ع B001 humbled lowering)`
- `selected_branches`: `ء ت ي` B001/B011; `ح د ث` B003/B005; `غ ش و` B001/B002/B005; `و ج ه` B001/B003/B006; `خ ش ع` B001/B002/B004
- `constructed_model`: A report comes to the listener as an arriving event, but its content is the covering event itself. The first concrete surface revealed by the covering is not an inner doctrine but faces: outward fronts are lowered, marked, and made readable.
- `freeze_point`: after 88:2 `وُجُوهٌ يَوْمَئِذٍ خَاشِعَةٌ`
- `predictions_at_freeze`: a second face-state may later contrast the first; the covering should organize visible outcomes; the end should return from exposed faces to accountable return.
- `unused_features_tested`: 88:3-7 toil/fire/drink/food negation; 88:8 second `وُجُوهٌ`; 88:24-26 punishment, return, reckoning.
- `corroborators`: `(C: repeated وُجُوهٌ at 88:8)`, `(C: ع ذ ب B005 punishment follows the one who turned away)`, `(C: ء و ب B001 return at 88:25)`, `(C: ح س ب B001 calculation at 88:26)`.
- `constraints`: `(K: غاشية is idafa complement of حديث in attachment 88:1:a3, so covering is content of the report, not a literal physical blanket in the grammar)`.
- `temporal_reactivation_notes`: The opening question activates arrival and report, then `الغاشية` retroactively makes the arrival ominous. The second `وجوه` at 88:8 reactivates the first faces and splits the covered day into two visible states.
- `rival_models`: `ء ت ي` B004/B005 water-channel/sudden flood gives a possible inundation image, but it is weaker because S88 later supplies heat/fire, not flood, in the punitive side; it survives only as a local source-flow image in S88-CSU-03.
- `grade`: medium-strong
- `grade_rationale`: Several independent channels converge: arrival/report/covering, visible faces, repeated contrast, and final accountability. The lexical image is broad but passage order strongly supports it.
- `source_queries_or_rows_used`: S88 QAC rows for 88:1-2, 88:8, 88:24-26; attachment rows 88:1:a1-a3, 88:2:a1-a2.

### S88-CSU-02: Exhausted work does not nourish; it terminates in heat and non-food

- `candidate_id`: S88-CSU-02
- `ayah_range`: 88:2-7
- `seed_type`: verified composite from lexical seeds `خ ش ع`, `ع م ل`, `ن ص ب`, `ص ل ي`, `ح م ي`, `ط ع م`, `ض ر ع`, `س م ن`, `غ ن ي`, `ج و ع`
- `seed`: 88:3:1 `عَامِلَةٌ` root `ع م ل` B001 intended work and 88:3:2 `نَّاصِبَةٌ` root `ن ص ب` B004 exhausting toil
- `generating_set`: `(E: و ج ه B001/B003 visible front)`, `(E: خ ش ع B001 lowered submission)`, `(E: ع م ل B001 intentional work)`, `(E: ن ص ب B004 exhausting hardship)`, `(E: ص ل ي B003 meeting fire/heat)`, `(E: ن و ر B002 fire)`, `(E: ح م ي B001 heat)`, `(E: س ق ي B001 being given drink)`, `(E: ع ي ن B006 spring/source)`, `(E: ء ن ي B003 reaching full heat)`, `(E: ط ع م B001 food/taste)`, `(E: ض ر ع B005 plant ضريع with B003 weakness/emaciation)`.
- `selected_branches`: work/exhaustion/heat/source/food-failure branches named above.
- `constructed_model`: A labor-system is shown after its result: faces already lowered, then the work is named as strenuous but fruitless. The subsequent fire, boiling spring, and exception-food convert the labor into a closed metabolic failure: effort consumes the agent but gives no nourishment, no fattening, and no relief from hunger.
- `freeze_point`: after 88:6 `إِلَّا مِن ضَرِيعٍ`
- `predictions_at_freeze`: the passage should negate nourishment, sufficiency, or relief; the food should be grammatically present but functionally void; later successful side should answer with accepted striving.
- `unused_features_tested`: 88:7 paired negation; 88:9 `لسعيها راضية`; 88:10-16 furnished garden.
- `corroborators`: `(C: س م ن B001 fattening negated at 88:7)`, `(C: غ ن ي B002 sufficiency negated at 88:7)`, `(C: ج و ع B001 hunger remains)`, `(C: س ع ي B001/B002 striving reappears positively at 88:9)`.
- `constraints`: `(K: ع م ل remains ordinary work/doing; the heat-food model is a secondary simulation, not a claim that عاملة means punished metabolism)`, `(K: attachment 88:6:a4 marks ضريع as exceptional source/material for طعام, so the non-food image must preserve the grammatical status of ضريع as the named food exception)`.
- `temporal_reactivation_notes`: `عاملة ناصبة` initially opens activity and fatigue; `تصلى` and `تسقى` make the body the receiver of heat; `ليس لهم طعام إلا` reactivates work as failed provisioning; `لا يسمن ولا يغني` closes the prediction exactly.
- `rival_models`: `ع م ل` B009 spear-shaft and `ن ص ب` B001 erected marker can form an instrument/standing image, but S88 does not supply weapon target or erected object in 88:2-7. It is terminated locally and later reappears only in the created-landscape sequence at 88:19.
- `grade`: strong
- `grade_rationale`: The freeze prediction is directly satisfied by unused paired negation and then contrasted by positive striving in 88:9.
- `source_queries_or_rows_used`: S88 QAC rows 88:2-7 and 88:9; attachment rows 88:3:a1, 88:4:a1-a2, 88:5:a1-a2, 88:6:a1-a4, 88:7:a1-a2.

### S88-CSU-03: Two water systems: punitive boiling source and garden running source

- `candidate_id`: S88-CSU-03
- `ayah_range`: 88:5 and 88:12, with contrast from 88:10-16
- `seed_type`: lexical
- `seed`: 88:5:3 `عَيْنٍ` root `ع ي ن` B006 water-source
- `generating_set`: `(E: ع ي ن B006 source of running water)`, `(E: س ق ي B001 watering/drinking)`, `(E: ء ن ي B003 full heat/reached extremity)`, later fork `(E: ج ر ي B001 flowing/streaming)`.
- `selected_branches`: `ع ي ن` B006/B010; `س ق ي` B001/B003/B007; `ء ن ي` B003; `ج ر ي` B001/B006.
- `constructed_model`: The same source schema is split by temporal placement. In 88:5 the source is a forced drink from an over-reached, heated spring. In 88:12 the source is inside the garden and flows; it supplies motion and continuity rather than compulsion and heat.
- `freeze_point`: first freeze after 88:5 `من عين آنية`; second freeze after 88:12 `فيها عين جارية`.
- `predictions_at_freeze`: the punitive source should be embedded in deprivation; the garden source should be embedded in abundance, placement, and rest.
- `unused_features_tested`: 88:6-7 food failure; 88:13-16 furnishings; repeated `فيها` locatives.
- `corroborators`: `(C: 88:6-7 no nourishing food after forced drink)`, `(C: ج ن ن B003 garden enclosure at 88:10)`, `(C: repeated فيها predicates at 88:11-13)`, `(C: س ر ر B011 resting seats and ر ف ع B001 elevation at 88:13)`.
- `constraints`: `(K: ع ي ن also has eye/watch/elite branches B001-B005/B014-B017, but attachments 88:5:a1 and 88:12:a2 force source/location readings here)`.
- `temporal_reactivation_notes`: The first `عين` becomes negative because of `تسقى` plus `آنية`; the later `عين جارية` reactivates the same lexical source but reverses its thermal and coercive profile.
- `rival_models`: Eye/watching model: `عين` B001/B003 can link to `نظر` in 88:17, but local syntax in 88:5 and 88:12 makes water-source dominant. Keep eye-model as weak reactivation only for the observation block.
- `grade`: strong
- `grade_rationale`: Same root occurs in two contrasting environments, and independent adjectives/locatives reverse the image.
- `source_queries_or_rows_used`: QAC rows 88:5, 88:12; attachment rows 88:5:a1-a2, 88:12:a1-a3.

### S88-CSU-04: The good side answers toil with satisfied striving and arranged rest

- `candidate_id`: S88-CSU-04
- `ayah_range`: 88:8-16
- `seed_type`: lexical and constructional
- `seed`: 88:9:1 `سَعْيِهَا` root `س ع ي`, B001 purposeful movement and B002 work/earning
- `generating_set`: `(E: و ج ه B001/B006 face/status)`, `(E: ن ع م B001 good condition and B002 softness/comfort)`, `(E: س ع ي B001 movement toward aim and B002 work/earning)`, `(E: ر ض و B001 satisfaction)`, `(E: ج ن ن B003 garden sheltered by growth)`, `(E: ع ل و B001/B002 highness)`, `(E: س م ع B001 hearing)`, `(E: ل غ و B001/B002 null/bad speech negated)`, `(E: ع ي ن B006 source)`, `(E: ج ر ي B001 flowing)`, `(E: س ر ر B011 resting seats)`, `(E: ر ف ع B001 raised)`, `(E: ك و ب B001 cup without handle)`, `(E: و ض ع B001 placed)`, `(E: ص ف ف B001 lined arrangement)`, `(E: ب ث ث B001 spread distribution)`.
- `selected_branches`: all named comfort, placement, and arrangement branches.
- `constructed_model`: The second face-state is not merely happy; it is set inside an ordered habitat. Striving has produced satisfaction, and the environment answers every deprivation in 88:2-7: no vain sound, flowing source, raised resting places, cups set ready, cushions aligned, carpets spread.
- `freeze_point`: after 88:10 `في جنة عالية`
- `predictions_at_freeze`: the high garden should contain internal ordered supports for hearing, drinking, sitting, receiving, and spacious placement.
- `unused_features_tested`: 88:11-16 locative inventory; repeated `فيها`; passive participles `مرفوعة/موضوعة/مصفوفة/مبثوثة`.
- `corroborators`: `(C: 88:11 no لاغية negates auditory corruption)`, `(C: 88:12 flowing source)`, `(C: 88:13-16 four passive/arranged furnishings)`, `(C: contrast with 88:3 عاملة ناصبة)`.
- `constraints`: `(K: جنة B001/B003 retains ordinary garden/enclosure; the furniture does not make it an abstract psychological state)`.
- `temporal_reactivation_notes`: The earlier `عاملة ناصبة` is reactivated by `سعيها راضية`: work is not rejected absolutely; futile toil is contrasted with accepted striving. The list of placed objects slows recitation into settled rest.
- `rival_models`: `ن ع م` B005 livestock/camel wealth could tie to 88:17 `الإبل`, but in 88:8 the predication to faces and garden setting constrain it to condition/softness.
- `grade`: strong
- `grade_rationale`: It explains sequence, repeated locatives, passive arranged objects, and direct contrast with the failed provisioning sequence.
- `source_queries_or_rows_used`: QAC rows 88:8-16; attachment rows 88:8:a1-a2, 88:9:a1-a2, 88:10:a1-a2, 88:11:a1-a2, 88:12:a1-a3, 88:13:a1-a3, 88:14:a1, 88:15:a1, 88:16:a1.

### S88-CSU-05: Look at constructed scale: camel, sky, mountains, earth

- `candidate_id`: S88-CSU-05
- `ayah_range`: 88:17-20
- `seed_type`: constructional and lexical
- `seed`: repeated construction `إلى X كيف passive-created/raised/erected/spread`
- `generating_set`: `(E: ن ظ ر B001 directed sight/basira)`, `(E: ء ب ل B001 camels and their management)`, `(E: خ ل ق B001 measured fashioning and B002 creating)`, `(E: س م و B004 sky/what is above)`, `(E: ر ف ع B001 raising)`, `(E: ج ب ل B001 high solid mass)`, `(E: ن ص ب B001 erecting upright)`, `(E: ء ر ض B001 lower counterpart to sky)`, `(E: س ط ح B001 broad flat surface)`.
- `selected_branches`: `نظر` B001/B010; `أبل` B001/B002/B004; `خلق` B001/B002/B003/B004; `سمو` B001/B004; `رفع` B001/B002; `جبل` B001/B005/B009; `نصب` B001/B003; `أرض` B001/B002; `سطح` B001/B005.
- `constructed_model`: The listener is moved from threatened/comforted bodies to a four-part inspection of made scale: a near survival animal, the high covering sky, fixed mountains, and the lower spread earth. The repeated `كيف` asks for manner, not merely existence.
- `freeze_point`: after 88:20
- `predictions_at_freeze`: the speaker's task should become reminding rather than coercive control; the observed arrangement should support accountability without forced domination.
- `unused_features_tested`: 88:21-22 `فذكر ... لست عليهم بمصيطر`; 88:25-26 return/reckoning.
- `corroborators`: `(C: ذ ك ر B003/B009 reminding after observation)`, `(C: س ط ر B003 domination/control is denied at 88:22)`, `(C: ء و ب B001 return and ح س ب B001 reckoning supply the closing authority)`.
- `constraints`: `(K: attachments 88:17:a1-a3, 88:18:a1-a2, 88:19:a1-a2, 88:20:a1-a2 make each object an attentional complement plus كيف-clause; do not merge them into one lexical metaphor)`.
- `temporal_reactivation_notes`: `أفلا ينظرون` reactivates earlier faces: faces that were visible evidence are now commanded to direct sight outward. The world-order sequence prepares the shift from sensory inspection to reminder.
- `rival_models`: Camel-specific subsistence seed `أبل` B002 can generate water-sufficiency contrast with 88:5/12, but the repeated cosmic construction makes it subordinate.
- `grade`: strong
- `grade_rationale`: Repetition, syntax, and branch fit are highly specific, and the next ayah confirms the rhetorical function.
- `source_queries_or_rows_used`: QAC rows 88:17-20; attachment rows 88:17:a1-a3, 88:18:a1-a2, 88:19:a1-a2, 88:20:a1-a2.

### S88-CSU-06: Reminder without domination; exception for turning away and covering

- `candidate_id`: S88-CSU-06
- `ayah_range`: 88:21-24
- `seed_type`: constructional/morphosyntactic
- `seed`: 88:21 `فذكر إنما أنت مذكر`
- `generating_set`: `(E: ذ ك ر B003 recollection after absence and B009 reminder)`, `(E: ل ي س B001 negation of present state)`, `(E: س ط ر B003 controlling overseer)`, `(E: و ل ي B007 turning away/withdrawing)`, `(E: ك ف ر B001 covering and B003 covering truth)`, `(E: ع ذ ب B005 punishment)`, `(E: ك ب ر B001 greatness)`, `(E: ء ل ه B001 worshipped deity as subject of punishment)`.
- `selected_branches`: `ذكر` B003/B004/B009; `ليس` B001; `سطر` B003; `ولي` B006/B007/B012; `كفر` B001/B003/B004; `عذب` B005; `كبر` B001/B006/B010.
- `constructed_model`: The addressee is authorized to reactivate memory, not to impose control. The exception defines the resistant subject as one who turns away and covers; punishment belongs to God and is framed as the greater punishment.
- `freeze_point`: after 88:22 `لست عليهم بمصيطر`
- `predictions_at_freeze`: if control is denied to the messenger, a later clause must identify who receives coercive judgment and by whom; the passage should keep reminding separate from punishment.
- `unused_features_tested`: 88:23 exception; 88:24 divine subject of punishment; 88:25-26 return and reckoning.
- `corroborators`: `(C: 88:23 إلا من تولى وكفر supplies the exception class)`, `(C: 88:24 الله subject of يعذبه)`, `(C: 88:25-26 إياب/حساب locate final authority elsewhere)`.
- `constraints`: `(K: سطر B001 line/writing is weak here; local form مصيطر and attachment 88:22:a1-a3 select controlling overseer B003)`, `(K: لا control over them does not erase the command to remind; it constrains means, not mission)`.
- `temporal_reactivation_notes`: After the created-world inspection, `فذكر` changes observation into admonition. `لست عليهم بمصيطر` freezes a non-coercive role; `إلا من تولى وكفر` then reactivates the earlier covering root `غ ش و` by naming the human counter-covering `كفر`.
- `rival_models`: `ذكر` B002 hard/sharp male image terminates; no local gender or cutting role supports it.
- `grade`: strong
- `grade_rationale`: The construction is syntactically explicit and predicts the divine-judgment closure.
- `source_queries_or_rows_used`: QAC rows 88:21-24; attachment rows 88:21:a1, 88:22:a1-a3, 88:23:a1-a4, 88:24:a1-a4.

### S88-CSU-07: Closure as return plus calculation

- `candidate_id`: S88-CSU-07
- `ayah_range`: 88:25-26
- `seed_type`: lexical and morphosyntactic
- `seed`: 88:25:3 `إِيَابَهُمْ` root `ء و ب` B001 return
- `generating_set`: `(E: ء و ب B001 return to مآب)`, `(E: ح س ب B001 counting/reckoning)`, `(E: ع ل و B012 على obligation/against-domain from 88:26 attachment)`.
- `selected_branches`: `ء و ب` B001/B003/B004/B006/B007; `ح س ب` B001/B003/B006/B010.
- `constructed_model`: The ending reverses apparent human movement. Whoever turned away still has return directed `إلينا`; after return, reckoning is `علينا`, a shift from destination to obligation/authority.
- `freeze_point`: after 88:25
- `predictions_at_freeze`: the next closure should name assessment, counting, or settlement; it should belong to the same divine authority, not the messenger.
- `unused_features_tested`: 88:26 `حسابهم`; earlier 88:21-22 reminder/non-control.
- `corroborators`: `(C: ح س ب B001 exactly supplies reckoning)`, `(C: attachment 88:25:a2-a3 fronted إلينا destination)`, `(C: attachment 88:26:a2-a3 fronted علينا responsibility)`.
- `constraints`: `(K: ء و ب B003 gait of limbs and B007 sunset can enrich return rhythm but do not control primary meaning)`.
- `temporal_reactivation_notes`: `تولى` in 88:23 produces outward withdrawal; `إيابهم` reactivates it as reversible movement. The final `ثم` creates a second-stage closure: return first, account after.
- `rival_models`: `ح س ب` B003 sufficiency could connect to `لا يغني` in 88:7, but local `حساب` and `علينا` select counting/reckoning.
- `grade`: strong
- `grade_rationale`: Exact lexical and syntactic closure; strongly predicts why the surah ends where it does.
- `source_queries_or_rows_used`: QAC rows 88:25-26; attachment rows 88:25:a1-a4, 88:26:a1-a4.

### S88-CSU-08: Vertical and positional axis across the whole surah

- `candidate_id`: S88-CSU-08
- `ayah_range`: 88:2-26
- `seed_type`: temporal/acoustic and verified composite
- `seed`: recurring spatial oppositions: lowering, highness, raised, erected, spread, upon/over
- `generating_set`: `(E: خ ش ع B001 lowering)`, `(E: ن ص ب B001 erected and B004 toil)`, `(E: ع ل و B001 high)`, `(E: ر ف ع B001 raised)`, `(E: س م و B001/B004 above/sky)`, `(E: ج ب ل B001 high solid mass)`, `(E: س ط ح B001 spread surface)`, `(E: ع ل و B012 على in 88:22 and 88:26)`.
- `selected_branches`: spatial branches named above.
- `constructed_model`: S88 repeatedly sets bodies and worlds on a vertical/positional axis: humbled faces, exhausting standing/toil, high garden, raised couches, raised sky, erected mountains, spread earth, no control over them, reckoning upon Us.
- `freeze_point`: after 88:20 landscape sequence
- `predictions_at_freeze`: the final address should define authority in positional terms; coercion over people should be constrained.
- `unused_features_tested`: 88:22 `عليهم بمصيطر`; 88:26 `علينا حسابهم`.
- `corroborators`: `(C: attachment 88:22:a1 domain عليهم)`, `(C: attachment 88:26:a2-a3 علينا as fronted predicate with حسابهم)`, `(C: contrast between خاشعة and عالية/مرفوعة)`.
- `constraints`: `(K: spatial axis is a synthesis of relations, not an alternative translation of any single root)`.
- `temporal_reactivation_notes`: Lowered faces come before high garden; high garden prepares raised sky; denial of domination over them prevents the vertical axis from becoming messenger-control; final `علينا` resolves it as divine accountability.
- `rival_models`: Pure social-rank model from `رفع` B002 and `وجه` B006 is plausible but incomplete because the passage supplies concrete sky/mountain/earth geometry.
- `grade`: medium-strong
- `grade_rationale`: Strong ordering support, but more composite and less lexically singular than CSU-02/05/07.
- `source_queries_or_rows_used`: QAC rows 88:2, 88:3, 88:10, 88:13, 88:18-20, 88:22, 88:26; relevant attachment rows.

## Exhaustive seed ledger

The following ledger records each eligible seed pass. `Selected path` names the image if the seed produced or joined one. `Terminated branches` means branches were read but did not receive passage-local roles.

1. `88:1:2 أتى / ء ت ي`: branches B001-B013 visited. Selected B001 arrival and B011 ominous arrival for CSU-01; B004/B005 water-channel/flood weakly reactivated in CSU-03 but not selected as primary; B002/B003/B006-B010/B012/B013 terminate for lack of local payment, stranger, mating, road, or execution roles. Grade medium-strong.
2. `88:1:3 حديث / ح د ث`: branches B001-B007 visited. Selected B003 renewed report and B005 event/calamity for CSU-01; B001 new occurrence gives temporal freshness; B007 polishing terminates. Grade medium.
3. `88:1:4 غاشية / غ ش و`: branches B001-B007 visited. Selected B001/B002 covering and comprehensive envelopment for CSU-01; B005 covering consciousness is a weak fork for stunned perception; B004 intercourse, B006 striking with whip/sword, B007 animal face whitening terminate. Grade medium-strong.
4. `88:2:1 وجوه / و ج ه first`: branches B001-B015 visited. Selected B001 face/front, B003 confrontation, B006 visible status for CSU-01/02; B008 right course weakly reactivates judgment; birth/plant/prosody branches terminate. Grade medium-strong.
5. `88:2:3 خاشعة / خ ش ع`: branches B001-B004 visited. Selected B001 lowering/submission for CSU-01/02 and B002 low lifeless ground as weak body-to-ground image; B003 star sinking and B004 lost-hump terminate except as faint vertical axis. Grade medium.
6. `88:3:1 عاملة / ع م ل`: branches B001-B012 visited. Selected B001 work, B002 exert/use, B007 self-imposed strain for CSU-02; B009 spear-shaft rejected by local grammar; B003 office, B004 wage, B005 transaction, B006 manual workers, B010 limb, B011 road, B012 walkers terminate. Grade strong within CSU-02.
7. `88:3:2 ناصبة / ن ص ب first`: branches B001-B010 visited. Selected B004 exhausting hardship for CSU-02; B001 erecting and B003 marker are held for later 88:19; B002 cult-stone, B005 share, B006 fixed measure, B007 case, B008 war, B009 raised song, B010 gentle travel terminate here. Grade strong.
8. `88:4:1 تصلى / ص ل ي`: branches B001-B010 visited. Selected B003 contact with fire and B004 heating/roasting for CSU-02; prayer/donation/preceding-runner/trap branches terminate by attachment to `نارا`. Grade strong.
9. `88:4:2 نارا / ن و ر`: branches B001, B002, B004-B009 visited. Selected B002 fire; B001 light is constrained by `تصلى` and `حامية`; plant blossom, minaret, fleeing, smoke/marking branches terminate. Grade strong.
10. `88:4:3 حامية / ح م ي`: branches B001-B012 visited. Selected B001 heat; B002 protection is a rival denied by punitive context; B003 anger secondary; mud/blackness/venom/night branches terminate. Grade strong.
11. `88:5:1 تسقى / س ق ي`: branches B001-B003, B005-B010 visited. Selected B001 watering/drinking and B003 water share/channel for CSU-03; B010 heart made to drink bitterness weakly corroborates punitive force; dye, dropsy, prayer-rain branches terminate. Grade strong.
12. `88:5:3 عين first / ع ي ن`: branches B001-B017 visited. Selected B006 water source for CSU-03; B001/B002 eye and B003 care are constrained by `من` source complement; elite/cash/spy branches terminate. Grade strong.
13. `88:5:4 آنية / ء ن ي`: branches B001-B005 visited. Selected B003 reaching full time/heat; B001 delay is weak temporal coloring; B004 vessel puns against drink but attachment selects adjective of source; B002 night-hours and B005 interrogative terminate. Grade strong.
14. `88:6:1 ليس first / ل ي س`: branches B001-B008 visited. Selected B001 negation and B002 exception structure for CSU-02; B003 coordinate negation anticipates 88:7; personal traits B004-B008 terminate. Grade strong.
15. `88:6:3 طعام / ط ع م`: branches B001-B014 visited. Selected B001 taste/food and B002 feeding; B004 livelihood and B007 fattening predict 88:7; choking B012 and graft B010 terminate. Grade strong.
16. `88:6:6 ضريع / ض ر ع`: branches B001-B013 visited. Selected B005 plant, B003 weakness/emaciation, B002 abasement as local negative image; milk B001 is ironic but not selected; sunset, rope, money, drink-thinness terminate. Grade strong.
17. `88:7:2 يسمن / س م ن`: branches B001-B009 visited. Selected B001 fattening as explicitly negated; B002 clarified milk-fat image supports food domain but not primary; decorative/sect/place branches terminate. Grade strong as corroborator.
18. `88:7:4 يغني / غ ن ي`: branches B001-B006 visited. Selected B002 sufficiency and B001 independence as explicitly negated; song B003 terminates here but later contrasts with `لاغية`; place/marriage branches terminate. Grade strong as corroborator.
19. `88:7:6 جوع / ج و ع`: branches B001-B004 visited. Selected B001 hunger and B004 hollowness; famine B002 generalizes but not needed; causative B003 terminates. Grade strong as closure of CSU-02.
20. `88:8:1 وجوه second / و ج ه second`: all `و ج ه` branches revisited. Selected B001 face/front and B006 status in contrast to first faces for CSU-04; B008 correct course weakly supports accepted striving; remote branches terminate. Grade strong as temporal reactivation.
21. `88:8:3 ناعمة / ن ع م`: branches B001-B013 visited. Selected B001 good condition, B002 softness/comfort, B011 pleasant dwelling for CSU-04; B005 livestock/camels weakly anticipates 88:17 but is constrained by face predication; ostrich/yes/foot branches terminate. Grade strong.
22. `88:9:1 سعي / س ع ي`: branches B001-B008 visited. Selected B001 purposeful movement, B002 work/earning, B006 noble endeavors for CSU-04; B003 official management, B004 slander, B005 slave ransom, B007 prostitution, B008 contest terminate. Grade strong.
23. `88:9:2 راضية / ر ض و`: branches B001-B007 visited. Selected B001 satisfaction and B002 abundant approval; B003 mutual satisfaction less supported because subject is singular faces; B005 contest and place names terminate. Grade strong.
24. `88:10:2 جنة / ج ن ن`: branches B001-B017 visited. Selected B003 garden sheltered by growth and B001 covering/enclosure; B008 shield weakly contrasts punishment; B010 inner heart and B011 plant growth secondary; jinn, madness, snake, bones terminate. Grade strong.
25. `88:10:3 عالية / ع ل و`: branches B001-B006, B008-B012 visited. Selected B001 height, B002 rank, B005 upper direction for CSU-04/08; B003 arrogance rejected by garden context; tool/body branches terminate. Grade strong.
26. `88:11:2 تسمع / س م ع`: branches B001-B016 visited. Selected B001 hearing and B003 understanding/obedience as negated corruption-free perception; B006 abusive hearing and B007 song are constrained by `لاغية`; equipment/animal branches terminate. Grade medium-strong.
27. `88:11:4 لاغية / ل غ و`: branches B001-B006 visited. Selected B001 worthless thing, B002 false/bad speech, B003 mixed noise; B005 deviation and B006 failure secondary; B004 dialect/tongue terminates. Grade strong.
28. `88:12:2 عين second / ع ي ن second`: all `ع ي ن` branches revisited. Selected B006 water-source; B001 eye weakly reactivated by coming observation block but constrained locally. Grade strong.
29. `88:12:3 جارية / ج ر ي`: branches B001-B004, B006-B007 visited. Selected B001 flowing/streaming and B006 continual provision; custom/agent/girl/racing-with terminate. Grade strong.
30. `88:13:2 سرر / س ر ر`: branches B001, B004-B006, B008-B011, B013-B015 visited. Selected B011 resting/leaning place; B010 hidden joy/comfort corroborates `ناعمة`; secrecy/body/lines/sand terminate. Grade medium-strong.
31. `88:13:3 مرفوعة / ر ف ع`: branches B001-B012 visited. Selected B001 raised and B002 elevated rank; B004 brought-near weakly supports readiness; news/noise/milk/agriculture/case branches terminate. Grade strong.
32. `88:14:1 أكواب / ك و ب`: branches B001-B006 visited. Selected B001 cup without handle and B005 drinking by cup; game/instrument/body-shape branches terminate. Grade medium.
33. `88:14:2 موضوعة / و ض ع`: branches B001-B013 visited. Selected B001 placed in position; B005 lowered status rejected because garden context makes readiness not humiliation; birth/trade-loss/racing/camel branches terminate. Grade medium-strong.
34. `88:15:2 مصفوفة / ص ف ف`: branches B001-B007 visited. Selected B001 aligned in rows; B004 bench/building weakly supports furnishing; meat/camel/tree/water-crowding terminate. Grade medium-strong.
35. `88:16:2 مبثوثة / ب ث ث`: branches B001-B003 visited. Selected B001 spread/dispersed; B002 disclosure of inner complaint is rejected in comfort scene; B003 revealing matter terminates. Grade medium-strong.
36. `88:17:2 ينظر / ن ظ ر`: branches B001-B010 visited. Selected B001 sight/basira and B010 deliberative consideration for CSU-05; B002 waiting weakly terminates; symmetry, beauty, destructive glance, guard branches terminate. Grade strong.
37. `88:17:4 إبل / ء ب ل`: branches B001-B009 visited. Selected B001 camels and care, B002 water-sufficiency weakly recalls thirst, B004 burden/weight local to contemplation; wood bundle/monk/date/place/tribe terminate. Grade medium-strong.
38. `88:17:5 كيف first / ك ي ف`: no accepted branch rows available. Constructional seed: repeated manner-question. Selected as structural operator with attachment 88:17:a2-a3. Grade strong as construction, ungraded lexically.
39. `88:17:6 خلقت / خ ل ق`: branches B001-B005, B007-B012 visited. Selected B001 measuring/fashioning, B002 creating, B003 complete proportion, B004 innate constitution; B007 fabrication constrained by passive created context; worn cloth/smooth surface/well/rock terminate. Grade strong.
40. `88:18:2 السماء / س م و`: branches B001-B008 visited. Selected B004 sky and B001 height; B005 name/dalalah is remote but opening-context-like only; hunting/competition terminate. Grade strong.
41. `88:18:3 كيف second / ك ي ف`: no accepted branch rows. Same manner-question construction with 88:18:a2. Grade strong as construction.
42. `88:18:4 رفعت / ر ف ع second`: all `ر ف ع` branches revisited. Selected B001 raised, B002 elevation. Earlier raised couches reactivated as local echo but not generator. Grade strong.
43. `88:19:2 الجبال / ج ب ل`: branches B001-B012 visited. Selected B001 high solid gathering, B005 hard resistance to digging, B009 difficulty/prevention; B004 innate nature weakly links with خلق; weaving/trees/sand/sadat terminate. Grade strong.
44. `88:19:3 كيف third / ك ي ف`: no accepted branch rows. Manner-question construction with 88:19:a2. Grade strong as construction.
45. `88:19:4 نصبت / ن ص ب second`: all `ن ص ب` branches revisited. Selected B001 erecting upright and B003 markers/boundaries; B004 toil reactivates 88:3 but not primary; cult-stone and case/song branches terminate. Grade strong.
46. `88:20:2 الأرض / ء ر ض`: branches B001-B012 visited. Selected B001 lower counterpart to sky and B002 productive soft earth; B006 remaining low weakly contrasts raising; insect/illness/stranger branches terminate. Grade strong.
47. `88:20:3 كيف fourth / ك ي ف`: no accepted branch rows. Manner-question construction with 88:20:a2. Grade strong as construction.
48. `88:20:4 سطحت / س ط ح`: branches B001-B006 visited. Selected B001 extended level surface and B005 useful spread/basalt; B002 body thrown flat is rejected for earth; tent-pole/vessel/plant branches terminate. Grade strong.
49. `88:21:1 ذكر / ذ ك ر imperative`: branches B001-B004, B007-B009 visited. Selected B003 recollection, B004 mention on tongue, B009 reminder for CSU-06; male/sharpness/fame/document branches terminate. Grade strong.
50. `88:21:4 مذكر / ذ ك ر participle`: same root revisited at changed occurrence. Selected B009 role noun, with B003/B004 as support. The repeated root is a self-confirming construction, not independent lexical corroboration. Grade strong.
51. `88:22:1 لست / ل ي س second`: all `ل ي س` branches revisited. Selected B001 negation; B002 exception is reserved for 88:23; personal trait branches terminate. Grade strong.
52. `88:22:3 مصيطر / س ط ر`: branches B001-B004, B006-B007 visited. Selected B003 controlling overseer; B001 line/writing and B004 cut-line are weakly imagistic but constrained by local predicate; stories/error/animal terminate. Grade strong.
53. `88:23:3 تولى / و ل ي`: branches B001-B008, B010-B016 visited. Selected B007 turning away, with B006 turning face and B012 reaching/overcoming as secondary; B001 nearness is inverted by withdrawal; friendship/legal/camel/rain branches terminate. Grade strong.
54. `88:23:4 كفر / ك ف ر`: branches B001-B015 visited. Selected B001 cover, B003 covering truth, B004 covering favor; B009 expiation rejected by hostile sequence; agriculture, perfume, place, crown branches terminate. Grade strong.
55. `88:24:1 يعذبه / ع ذ ب verb`: branches B001-B006, B008-B009 visited. Selected B005 pain/punishment; B003 restraint/fending supports punitive prevention; sweetness B001 is a lexical reversal but not selected; dangling/end-part branches terminate. Grade strong.
56. `88:24:2 الله / ء ل ه`: branches B001-B002 visited. Selected B001 worshipped deity as explicit subject and B002 divine name; not used as seed for speculative imagery. Grade strong.
57. `88:24:3 العذاب / ع ذ ب noun`: same root revisited. Selected B005 and cognate-accusative reinforcement from attachment 88:24:a3. Grade strong.
58. `88:24:4 الأكبر / ك ب ر`: branches B001-B007, B010-B013 visited. Selected B001 great magnitude, B006 greatness, B010 weight/difficulty; sin-specific B007 possible but local adjective modifies punishment; drum/day/age branches terminate. Grade strong.
59. `88:25:3 إياب / ء و ب`: branches B001, B003, B004, B006, B007 visited. Selected B001 return and B004 direction from which one comes; B003 limb-gait and B007 sunset enrich return but remain secondary; night-arrival weak. Grade strong.
60. `88:26:4 حساب / ح س ب`: branches B001-B004, B006, B008-B010 visited. Selected B001 counting/reckoning and B006 inspection of matter; B003 sufficiency reactivates `لا يغني` by contrast but is not primary; status/pillow/color/inquiry branches terminate. Grade strong.

## Constructional, morphosyntactic, and temporal seeds

1. `هل أتاك حديث الغاشية` (88:1): question + arrival + idafa report. Generates CSU-01. Grade medium-strong.
2. `وجوه يومئذ خاشعة` versus `وجوه يومئذ ناعمة` (88:2, 88:8): repeated face-state contrast. Generates CSU-01 and CSU-04. Grade strong.
3. `عاملة ناصبة` (88:3): paired active participles. Generates CSU-02. Grade strong.
4. Fire/drink/food deprivation sequence (88:4-7): receiver of fire, source of heated drink, exception-food, paired negation. Generates CSU-02/03. Grade strong.
5. `لا ... ولا ... من جوع` paired negation (88:7): tests and corroborates failed nourishment. Grade strong.
6. `لسعيها راضية` (88:9): lamed domain of satisfaction. Reactivates work from 88:3 and distinguishes accepted striving. Grade strong.
7. Repeated `فيها` garden inventory (88:11-13) plus coordinated furnishings (88:14-16): internal-place catalog. Generates CSU-04. Grade strong.
8. `أفلا ينظرون إلى X كيف ...` repeated inspection pattern (88:17-20): four-part manner inquiry. Generates CSU-05. Grade strong.
9. `فذكر إنما أنت مذكر` (88:21): imperative plus restrictive identity. Generates CSU-06. Grade strong.
10. `لست عليهم بمصيطر` (88:22): denied control predicate. Constrains reminder model. Grade strong.
11. `إلا من تولى وكفر` (88:23): exception + paired hostile acts. Completes CSU-06. Grade strong.
12. Cognate accusative `يعذبه ... العذاب` (88:24): intensifies punishment without making messenger agent. Grade strong.
13. Closure pair `إلينا إيابهم` / `علينا حسابهم` (88:25-26): destination then obligation/reckoning. Generates CSU-07. Grade strong.

## Image Packet Catalog

### IMAGE-S88-01

- Starting seed: `ء ت ي B001` at 88:1.
- Complete image: arriving report of an enveloping event that makes faces readable.
- Passage-order assembly: arrival -> report -> covering -> humbled faces -> contrasting faces -> return/reckoning.
- Participants and roles: report, covering event, faces, final authority.
- Operation / mechanism: disclosure by recited report and visible outcome.
- Direction / force / medium: arrival to addressee; covering over the day; return to God.
- Temporal development: question opens expectation; faces split; closure accounts.
- Outcome / closure: return and reckoning.
- Exact branch constituents: `ء ت ي B001/B011`, `ح د ث B003/B005`, `غ ش و B001/B002`, `و ج ه B001`, `خ ش ع B001`, `ن ع م B001`.
- Unfilled roles, if any: none.
- Status: COMPLETE.

### IMAGE-S88-02

- Starting seed: `ع م ل B001` at 88:3.
- Complete image: futile labor-metabolism ending in heat, forced drink, non-nourishing food, and hunger.
- Passage-order assembly: humbled faces -> work/exhaustion -> fire -> boiling source -> exception-food -> no fattening/no relief.
- Participants and roles: laboring faces, fire, heated spring, ضريع, hunger.
- Operation / mechanism: work consumes but does not provision.
- Direction / force / medium: body receives heat and drink; food fails its function.
- Temporal development: activity named before its failed outputs.
- Outcome / closure: hunger remains.
- Exact branch constituents: `ع م ل B001`, `ن ص ب B004`, `ص ل ي B003`, `ن و ر B002`, `ح م ي B001`, `س ق ي B001`, `ع ي ن B006`, `ء ن ي B003`, `ط ع م B001`, `ض ر ع B005/B003`, `س م ن B001`, `غ ن ي B002`, `ج و ع B001`.
- Unfilled roles, if any: none.
- Status: COMPLETE.

### IMAGE-S88-03

- Starting seed: `ع ي ن B006` at 88:5.
- Complete image: split source system, punitive heated source versus garden flowing source.
- Passage-order assembly: forced drink from hot source -> deprivation -> garden -> running source -> furnishings.
- Participants and roles: drinker, source, heat, garden, flow.
- Operation / mechanism: same source schema changes by location and qualifier.
- Direction / force / medium: source-to-body in punishment; source-within-garden in comfort.
- Temporal development: first source is constrained by heat; second source reactivates and reverses it.
- Outcome / closure: water becomes part of settled abundance.
- Exact branch constituents: `ع ي ن B006`, `س ق ي B001`, `ء ن ي B003`, `ج ر ي B001`, `ج ن ن B003`.
- Unfilled roles, if any: none.
- Status: COMPLETE.

### IMAGE-S88-04

- Starting seed: repeated construction `إلى X كيف` at 88:17.
- Complete image: made world-scale as reminder scaffold.
- Passage-order assembly: camel -> sky -> mountains -> earth -> remind -> no coercive control.
- Participants and roles: observers, camel, sky, mountains, earth, reminder-agent.
- Operation / mechanism: directed looking turns created order into recollection.
- Direction / force / medium: gaze toward objects; passive created/raised/erected/spread operations.
- Temporal development: local animal to cosmic structure to mission boundary.
- Outcome / closure: reminder, not domination; final divine account.
- Exact branch constituents: `ن ظ ر B001`, `ء ب ل B001`, `خ ل ق B001/B002`, `س م و B004`, `ر ف ع B001`, `ج ب ل B001`, `ن ص ب B001`, `ء ر ض B001`, `س ط ح B001`, `ذ ك ر B009`, `س ط ر B003`.
- Unfilled roles, if any: no explicit human response inside 88:17-20; response handled by 88:21-26.
- Status: COMPLETE.

### IMAGE-S88-05

- Starting seed: `ذ ك ر B009` at 88:21.
- Complete image: reminder without control, followed by divine exception-judgment.
- Passage-order assembly: remind -> role restriction -> denied control -> exception person -> divine punishment -> return/account.
- Participants and roles: reminder, addressees, turning-covering resister, God, returnees.
- Operation / mechanism: cognitive reactivation by reminder; coercion reserved to divine judgment.
- Direction / force / medium: speech/memory, not domination; return to divine accounting.
- Temporal development: mission boundary before exception and punishment.
- Outcome / closure: return and reckoning.
- Exact branch constituents: `ذ ك ر B003/B009`, `ل ي س B001`, `س ط ر B003`, `و ل ي B007`, `ك ف ر B001/B003`, `ع ذ ب B005`, `ء و ب B001`, `ح س ب B001`.
- Unfilled roles, if any: none.
- Status: COMPLETE.

## Exhaustiveness check after file creation

- Rooted occurrence restart: complete for the 60 occurrence-level seed passes listed above.
- Accepted branch coverage: complete by root dossier counts listed above; terminated branches are summarized in each seed row rather than silently omitted.
- Constructional seeds: complete for repeated face contrast, deprivation sequence, garden inventory, four `كيف` inspection clauses, reminder/non-control, exception, punishment, and return/account closure.
- Generated images: five image packets cover the coherent image-forks. No additional image-fork remained unrepresented after checking terminated seeds; weak local forks are named in the relevant seed rows and candidate rival models.
- Stage boundary: this file is Stage 1 Pass 2 only. No Stage 2 synthesis was run.
