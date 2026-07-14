# Stage 1 Pass 2: S80 Temporally Conditioned Reactivation

Assigned passage: S80, ayat 1-42. Sacred text source: `resources/quran/surah_80.json`.

## Root Cause For Pass 1 Limitation

Pass 1 visited only a limited number of words per finding for two concrete reasons:

1. The prompt-authorized SQLite files `resources/qac.sqlite` and `resources/furuq_v4.sqlite` are present locally but zero bytes, so schema inspection and SQL retrieval returned no rows.
2. I then fell back to the local TSV exports in `resources/qac_root_ayah.tsv`, `resources/v4_branches.tsv`, and `resources/attachments.tsv`; the first broad branch extraction exceeded the terminal output budget and was truncated. That made the working context branch-incomplete.

Pass 2 restarts from the first rooted word, uses the TSV exports only as local stand-ins for the empty SQLite databases, and treats every S80 rooted occurrence and every accepted branch ID as initiated. Branches not recruited into an image are recorded as terminated rather than silently dropped.

## Data Envelope

Rooted occurrence inventory from `resources/qac_root_ayah.tsv`: 85 S80 root-ayah rows, 70 distinct roots, and 88 rooted occurrences when repeated roots in an ayah are counted. Accepted branch inventory from `resources/v4_branches.tsv`: 575 accepted branch rows for S80 roots, including duplicate export rows where noted. Attachment evidence: `resources/attachments.tsv`, filtered to `sura=80`.

Opening basmala appears in the sacred JSON as `verse_0`, but whole-surah S80 assignment starts at `verse_1`. I did not initiate basmala seeds.

## Exhaustive Sweep Control

For every seed below, the full S80 root dossier was treated as read before selection. Selection means the branch specifically transformed, completed, constrained, or forked a passage-local image. Branches in the seed ledger marked `terminated` were initiated but found no passage-local complement beyond generic association.

Root inventory and accepted branch IDs:

| root | occurrences | accepted branch IDs |
| --- | ---: | --- |
| ع ب س | 1 | B001,B002,B003,B004,B005,B006 |
| و ل ي | 1 | B001,B002,B003,B004,B005,B006,B007,B008,B010,B011,B012,B013,B014,B015,B016 |
| ج ي ء | 3 | B001,B002,B003,B004,B005,B006 plus duplicate export set B001,B002,B003 |
| ع م ي | 1 | B001,B002,B004,B005,B006,B007,B008,B009 |
| د ر ي | 1 | B001,B002,B003,B004 |
| ز ك و | 2 | B001,B002,B004,B005 |
| ذ ك ر | 4 | B001,B002,B003,B004,B007,B008,B009 |
| ن ف ع | 1 | B001,B002,B003 |
| غ ن ي | 2 | B001,B002,B003,B004,B005,B006 |
| ص د ي | 1 | B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011 |
| س ع ي | 1 | B001,B002,B003,B004,B005,B006,B007,B008 |
| خ ش ي | 1 | B001,B002,B004 |
| ل ه و | 1 | B001,B002,B003,B004 |
| ش ي ء | 3 | B001,B002,B003,B004,B005,B006,B007,B008,B009 plus duplicate export set B001-B007 |
| ص ح ف | 1 | B001,B002,B003,B004,B005 |
| ك ر م | 2 | B001,B002,B003,B004,B005,B006,B007,B008,B009,B010 |
| ر ف ع | 1 | B001-B012 |
| ط ه ر | 1 | B001,B002,B003,B004,B005 |
| ي د ي | 1 | B001,B002,B003,B004,B005,B006,B007,B008,B009,B013,B014,B015,B016 |
| س ف ر | 2 | B001,B002,B003,B004 |
| ب ر ر | 1 | B001-B008 |
| ء ن س | 2 | B001-B006 |
| ق ت ل | 1 | B001-B008,B011,B012 |
| ك ف ر | 2 | B001-B015 |
| خ ل ق | 2 | B001,B002,B003,B004,B005,B007,B008,B009,B010,B011,B012 |
| ن ط ف | 1 | B001-B006 |
| ق د ر | 1 | B001,B003,B004,B005,B006,B007 |
| س ب ل | 1 | B001,B002,B004,B005,B006,B007,B008,B010 |
| ي س ر | 1 | B001-B011 |
| م و ت | 1 | B001-B014 |
| ق ب ر | 1 | B001-B004 |
| ن ش ر | 1 | B001-B010 |
| ء م ر | 1 | B001-B009,B011 |
| ق ض ي | 1 | B001-B008 |
| ن ظ ر | 1 | B001-B010 |
| ط ع م | 1 | B001,B002,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014 |
| ص ب ب | 2 | B001,B002,B003,B004,B005,B006,B007,B009,B010,B011 |
| م و ه | 1 | B001-B008 |
| ش ق ق | 2 | B001-B009 |
| ء ر ض | 1 | B001-B012 |
| ن ب ت | 1 | B001-B008 |
| ح ب ب | 1 | B001-B011 |
| ع ن ب | 1 | B001-B008 |
| ق ض ب | 1 | B001-B011 |
| ز ي ت | 1 | B001-B005 |
| ن خ ل | 1 | B001-B006 |
| ح د ق | 1 | B001-B004 |
| غ ل ب | 1 | B001,B002 |
| ف ك ه | 1 | B001,B002,B003,B004,B006,B007 |
| ء ب ب | 1 | B001,B002,B003,B004,B006,B007,B008 |
| م ت ع | 1 | B001,B002,B003,B007,B008,B009 |
| ن ع م | 1 | B001-B013 |
| ص خ خ | 1 | B001-B004 |
| ي و م | 1 | B001-B003 |
| ف ر ر | 1 | B001-B011,B014,B015,B016 |
| م ر ء | 2 | B001-B006 plus duplicate export B001-B005 |
| ء خ و | 1 | B001-B003 |
| ء م م | 1 | B001-B016 |
| ء ب و | 1 | B001-B003 |
| ص ح ب | 1 | B001-B008 |
| ب ن ي | 1 | B001-B010 |
| ك ل ل | 1 | B001-B009,B011 |
| ش ء ن | 1 | B001-B006 |
| و ج ه | 2 | B001,B002,B003,B006,B007,B008,B009,B010,B011,B012,B013,B014,B015 |
| ب ش ر | 1 | B001-B008 |
| ض ح ك | 1 | B001-B009,B011 |
| غ ب ر | 1 | B001,B002,B003,B004,B005,B008 |
| ر ه ق | 1 | B001-B007 |
| ق ت ر | 1 | B001-B006,B008,B009 |
| ف ج ر | 1 | B001-B006 |

## Candidate Synthesis Units

### CSU-80-01: Face Contraction, Turned Attention, And The Unseen Possibility

- `candidate_id`: CSU-80-01
- `ayah_range`: 80:1-4, reactivated by 80:5-10 and 80:38-42
- `seed_type`: lexical
- `seed`: 80:1:1 `عَبَسَ` x `ع ب س B001` = face contraction, frowning, harsh facial constriction.
- `generating_set`: `(E: ع ب س B001 facial constriction)`, `(E: و ل ي B007 turning away / leaving proximity)`, `(E: ج ي ء B001 coming/reaching)`, `(E: ع م ي B001 loss of eyesight)`, `(E: د ر ي B001 knowing/being made aware)`, `(E: ز ك و B001 growth)`, `(E: ز ك و B002 purification)`, `(E: ذ ك ر B009 reminder that makes something present again)`, `(E: ن ف ع B001 benefit against harm)`.
- `selected_branches`: ع ب س B001; و ل ي B007, with B006 as a rejected rival of turning the face toward; ج ي ء B001; ع م ي B001; د ر ي B001; ز ك و B001/B002; ذ ك ر B009; ن ف ع B001.
- `constructed_model`: The recitation first exposes a visible facial contraction and an outward turn. The one who comes is marked by outward blindness, but the following question blocks the addressee's assumption: the visible seer does not know whether inward growth/purification or recall will occur. The image is not "blindness means insight"; it is a directional misallocation of attention: visible facial response turns away from a person whose unseen inward future remains open.
- `freeze_point`: after 80:4 `أَوْ يَذَّكَّرُ فَتَنفَعَهُ ٱلذِّكْرَىٰ`.
- `predictions_at_freeze`: expect contrast between wrongly allocated attention and a more fitting object of care; expect repeated purification/reminder terms; expect later surface/face imagery to reactivate the opening face; expect grammar to preserve ordinary rebuke rather than allegorize every body part.
- `unused_features_tested`: 80:5-10 contrastive `أَمَّا`; `له` versus `عنه`; `استغنى`, `تصدى`, `يسعى`, `يخشى`, `تلهى`; final `وجوه` pair; attachment rows for coordinated `عبس/تولى`, subject of `جاءه`, delayed subject of `تنفعه`.
- `corroborators`: `(C: attachment 80:1 a1 coordinates تَوَلَّىٰ with عَبَسَ)`, `(C: attachment 80:2 a1-a2 makes the blind man the arriving subject and the suffix the person reached)`, `(C: غ ن ي B001 self-sufficiency in 80:5 supplies the rival attention target)`, `(C: ص د ي B007 facing/exposing oneself toward in 80:6)`, `(C: س ع ي B001 purposeful motion in 80:8)`, `(C: خ ش ي B001 reverent fear in 80:9)`, `(C: ل ه و B001 distraction/turning away in 80:10)`, `(C: و ج ه B001 final faces reactivate the opening face)`.
- `constraints`: `(K: ع م ي B002 spiritual blindness is not selected as the primary seed because 80:2 explicitly supplies ٱلْأَعْمَىٰ as the arriving subject)`, `(K: و ل ي B006 face-turning toward contradicts the sequence; B007 better fits rebuked avoidance)`, `(K: no branch licenses replacing primary rebuke with a hidden praise of blindness)`.
- `temporal_reactivation_notes`: The first audible scene is only face + turning. 80:3-4 reactivates it by asking what was not known. 80:5-10 then supplies the full contrast: the one who appears self-sufficient receives facing, while the one striving/fearing receives distraction. 80:38-42 returns to faces as final exposed states.
- `rival_models`: Rival A: "physical blindness vs spiritual blindness" from ع م ي B002; rejected as too generic and not locally generated before the explicit person arrives. Rival B: "harsh day" from ع ب س B002; retained only as a weak later echo with صاخة/day, not as the opening action.
- `grade`: strong
- `grade_rationale`: Specific lexical surface, grammar, later contrastive syntax, and final face imagery converge independently.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` rows for ع ب س, و ل ي, ج ي ء, ع م ي, د ر ي, ز ك و, ذ ك ر, ن ف ع; `v4_branches.tsv` rows named above; `attachments.tsv` 80:1 a1, 80:2 a1-a2, 80:3 a1-a4, 80:4 a1-a2.

### CSU-80-02: Misallocated Facing Toward Sufficiency Versus Striving Fear

- `candidate_id`: CSU-80-02
- `ayah_range`: 80:5-10, constrained by 80:3-4 and 80:11
- `seed_type`: constructional / lexical
- `seed`: contrastive construction `أَمَّا مَنِ ٱسْتَغْنَىٰ ... وَأَمَّا مَن جَاءَكَ يَسْعَىٰ`.
- `generating_set`: `(E: غ ن ي B001 wealth/independence/no need)`, `(E: غ ن ي B002 sufficiency/kifāyah)`, `(E: ص د ي B007 تصدّى = face/expose/stand toward)`, `(E: ج ي ء B001 coming/reaching)`, `(E: س ع ي B001 purposeful movement toward a sought object)`, `(E: س ع ي B002 effort/work)`, `(E: خ ش ي B001 fear with awe)`, `(E: ل ه و B001 being occupied away from something)`.
- `selected_branches`: غ ن ي B001/B002; ص د ي B007; ج ي ء B001; س ع ي B001/B002; خ ش ي B001; ل ه و B001.
- `constructed_model`: The passage builds a two-pan balance of attention. One figure presents as sufficient; the addressee turns toward him. The other arrives actively and inwardly fearful; the addressee is occupied away from him. The relational model is not simply rich/poor, but a misfired attentional economy: perceived sufficiency attracts response, while vulnerable purposeful seeking is neglected.
- `freeze_point`: after 80:10.
- `predictions_at_freeze`: expect a corrective boundary; expect reminder to be declared independent of elite attention; expect later individual sufficiency to return in a corrected form.
- `unused_features_tested`: 80:11 `كلا`; 80:12 voluntary remembering; 80:37 `شَأْنٌ يُغْنِيهِ`; final separation.
- `corroborators`: `(C: attachment 80:6 a2 لَهُ as directed-toward complement)`, `(C: attachment 80:10 a2 عَنْهُ as away-from complement)`, `(C: repeated ز ك و in 80:3 and 80:7 keeps purification as the disputed outcome)`, `(C: 80:37 غ ن ي B002 reactivates sufficiency as each person's own concern suffices/occupies him)`.
- `constraints`: `(K: غ ن ي B003 song and B004 residence terminate; no acoustic or dwelling role here)`, `(K: ص د ي B004 echo is a tempting sound branch but the construction gives directed facing, not reflected voice)`.
- `temporal_reactivation_notes`: The first scene is personal; the later `كلا` interrupts it and universalizes access to the reminder. In 80:37, sufficiency returns stripped of social prestige: every person has a matter that occupies/suffices him.
- `rival_models`: "Elite patronage system" is compatible but broader than lexical evidence; kept as secondary social simulation.
- `grade`: strong
- `grade_rationale`: Directional prepositions, parallel syntax, repeated purification, and later `يغنيه` make the model passage-local and temporally reactivated.
- `source_queries_or_rows_used`: QAC rows 80:5-10 and 80:37; furuq branches above; attachment rows 80:5 a1, 80:6 a1-a2, 80:7 a1-a2, 80:8 a1-a3, 80:9 a1, 80:10 a1-a2, 80:37 a6-a7.

### CSU-80-03: Reminder As Honored Written Object In Pure Raised Custody

- `candidate_id`: CSU-80-03
- `ayah_range`: 80:11-16, generated by 80:4 and reactivated by 80:38
- `seed_type`: lexical / constructional
- `seed`: 80:11:3 `تَذْكِرَةٌ` x `ذ ك ر B009`.
- `generating_set`: `(E: ذ ك ر B009 reminder / what makes present again)`, `(E: ذ ك ر B003 internal recollection)`, `(E: ذ ك ر B004 verbal mention)`, `(E: ص ح ف B002 written sheets)`, `(E: ص ح ف B003 collected written sheets)`, `(E: ك ر م B001 honor/nobility/generosity)`, `(E: ر ف ع B001 physical raising)`, `(E: ر ف ع B002 elevation of rank)`, `(E: ط ه ر B001 purity/removal of defilement)`, `(E: ط ه ر B005 moral purification)`, `(E: ي د ي B001 hands)`, `(E: ي د ي B002 power/capacity)`, `(E: س ف ر B004 book/writing/scribes)`, `(E: ب ر ر B001 truthful performance of word/deed)`, `(E: ب ر ر B002 expansive goodness/obedience)`.
- `selected_branches`: listed in generating set.
- `constructed_model`: The reminder that might benefit the overlooked seeker is re-presented as an elevated, purified, honored written deposit handled by noble truthful agents. Its value does not depend on the addressee's social attention. It has custody, height, cleanliness, and authorized transmission.
- `freeze_point`: after 80:16 `كِرَامٍۭ بَرَرَةٍۢ`.
- `predictions_at_freeze`: expect earlier neglected `ذِّكْرَى` to be revalued; expect later faces to disclose who received or rejected the reminder; expect no reduction of `سفرة` to ordinary travelers.
- `unused_features_tested`: 80:4 `الذِّكْرَى`; 80:12 `فَمَن شَاءَ ذَكَرَهُ`; 80:38 `مسفرة`; 80:42 `كفرة الفجرة`.
- `corroborators`: `(C: attachment 80:11 a2 makes تذكرة predicate of إنها)`, `(C: 80:12 conditional whoever wills remembers it supports open access)`, `(C: س ف ر B002 in 80:38 brightened faces later echoes كشف/إسفار without replacing the scribal branch)`, `(C: ك ف ر B003 final rejection of truth contrasts with honored reminder)`.
- `constraints`: `(K: ذ ك ر B001 male/masculine and B002 hard male/sharp branch terminate; no gender or weapon role)`, `(K: ص ح ف B004 bowl branch terminates; no vessel scene)`, `(K: س ف ر B003 travel branch terminates in 80:15 because بأيدي سفرة is custody/writing, not travel)`.
- `temporal_reactivation_notes`: The neglected person's possible benefit from reminder in 80:4 is frozen, then the reminder becomes the central object in 80:11-16. It is no longer dependent on the initial social encounter.
- `rival_models`: "Angelic scribes" is contextually likely, but Stage 1 preserves only the lexical custody/writing image and does not use external doctrine.
- `grade`: strong
- `grade_rationale`: Dense, contiguous lexical and syntactic support; several independent roots fill roles of object, medium, elevation, purification, custody, and agent quality.
- `source_queries_or_rows_used`: QAC rows 80:4, 80:11-16, 80:38, 80:42; furuq rows named; attachments 80:11 a1-a2, 80:12 a1-a2, 80:13 a1, 80:15 a1, 80:38 a1-a2, 80:42 a2-a3.

### CSU-80-04: Hidden Origin, Measured Path, Burial, And Reopening

- `candidate_id`: CSU-80-04
- `ayah_range`: 80:17-23, reactivated by 80:24-32 and 80:33-42
- `seed_type`: lexical
- `seed`: 80:19:2 `نُّطْفَةٍ` x `ن ط ف B002`.
- `generating_set`: `(E: ن ط ف B002 clear water/drop/seminal water)`, `(E: خ ل ق B001 measuring before cutting/acting)`, `(E: خ ل ق B002 creation/bringing into being)`, `(E: ق د ر B001 measure/limit)`, `(E: ق د ر B005 planning/arranging)`, `(E: س ب ل B001 road/path)`, `(E: ي س ر B001 ease/opening after difficulty)`, `(E: م و ت B001 death/loss of life)`, `(E: ق ب ر B001 burial/placing in grave)`, `(E: ق ب ر B002 enclosed lowering/hiddenness)`, `(E: ن ش ر B002 raising to life after death)`, `(E: ن ش ر B001 opening/spreading after being folded)`.
- `selected_branches`: listed in generating set; `ش ي ء B001` supplies general object-source in 80:18; `ش ي ء B002` supplies divine will in 80:22.
- `constructed_model`: A human who covers truth is himself unfolded from a minimal hidden water-source, measured, sent through an eased path, closed into death and burial, then reopened when willed. The image is a sequence of concealment, measuring, passage, closure, and spreading.
- `freeze_point`: after 80:22 `ثُمَّ إِذَا شَاءَ أَنشَرَهُ`.
- `predictions_at_freeze`: expect the model to challenge human self-sufficiency; expect a command left unfulfilled; expect later ecological water-to-growth sequence to mirror resurrection; expect final faces to disclose response to command.
- `unused_features_tested`: 80:17 `ما أكفره`; 80:23 `لما يقض ما أمره`; 80:25-31 water/splitting/planting; final `الكفرة الفجرة`.
- `corroborators`: `(C: ك ف ر B003/B004 human disbelief/ingratitude in 80:17 creates moral inversion against created dependence)`, `(C: ء م ر B002 command/obligation in 80:23)`, `(C: ق ض ي B004 completion/fulfillment negated by لمّا)`, `(C: ص ب ب B001 + م و ه B001 + ن ب ت B001 in 80:25-27 mirrors life from water)`, `(C: attachment 80:21 a2 coordinates burial after death)`, `(C: attachment 80:22 a1 sets شاء in temporal conditional frame)`.
- `constraints`: `(K: ن ط ف B004 impurity/accusation branch terminates; the verse gives origin, not slander)`, `(K: خ ل ق B007 invented lie terminates; not a human fabrication scene)`, `(K: ق د ر B004 constriction is possible but secondary; the local verb فَقَدَّرَهُ favors measure/arrangement)`.
- `temporal_reactivation_notes`: The first "what thing?" source question in 80:18 lowers human status. 80:19 specifies the drop, then `ثُمَّ` steps through path, death, burial, and reopening. Later food production repeats a water-to-emergence pattern at ecological scale.
- `rival_models`: Embryological detail beyond `نطفة/خلق/قدر/سبيل` is not licensed. It remains a minimal origin-path-closure-reopening simulation.
- `grade`: medium-strong
- `grade_rationale`: Strong sequential and lexical support, with independent ecological reactivation; some roles remain broad because `السبيل` could include birth path or life path.
- `source_queries_or_rows_used`: QAC rows 80:17-23, 80:25-27; furuq rows named; attachments 80:17 a1-a3, 80:18 a1-a3, 80:19 a1-a4, 80:20 a1-a2, 80:21 a1-a3, 80:22 a1-a2, 80:23 a1-a4.

### CSU-80-05: Food As Visible Proof: Poured Water, Split Earth, Emergent Multiplicity

- `candidate_id`: CSU-80-05
- `ayah_range`: 80:24-32
- `seed_type`: constructional / lexical
- `seed`: 80:24 `فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِ`.
- `generating_set`: `(E: ن ظ ر B001 directed sight/reflection)`, `(E: ط ع م B001 food/taste/what satisfies hunger)`, `(E: ط ع م B004 provision/livelihood)`, `(E: ص ب ب B001 pouring from above)`, `(E: م و ه B001 water)`, `(E: م و ه B003 supplying water by pouring/irrigation)`, `(E: ش ق ق B001 splitting/opening earth)`, `(E: ء ر ض B001 earth below)`, `(E: ء ر ض B002 fertile growing earth)`, `(E: ن ب ت B001 plant growth from earth)`, `(E: ح ب ب B001 grain/seed)`, `(E: ع ن ب B001 grape)`, `(E: ق ض ب B003 fresh cut herbage)`, `(E: ز ي ت B002 olive tree/fruit)`, `(E: ن خ ل B001 palm)`, `(E: ح د ق B003 enclosed garden)`, `(E: غ ل ب B002 thick/intertwined growth)`, `(E: ف ك ه B002 fruit)`, `(E: ء ب ب B001 pasture/fodder)`, `(E: م ت ع B001 benefit/enjoyment)`, `(E: م ت ع B003 provision for needs)`, `(E: ن ع م B005 grazing livestock)`.
- `selected_branches`: listed in generating set; `ص ب ب B002` supports downward channel as a secondary pre-freeze constituent.
- `constructed_model`: A command to look redirects the human from social mis-seeing to provision. The image unfolds vertically and materially: water is poured, earth is split, growth comes out, the list diversifies into human food and animal pasture, and the output is named as benefit for humans and livestock.
- `freeze_point`: after 80:32 `مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ`.
- `predictions_at_freeze`: expect prior creation-from-water model to be reactivated; expect final rupture/arrival to contrast ordinary provision with final need; expect no single crop to dominate the image.
- `unused_features_tested`: 80:18-22 human origin; 80:33 arrival of the ṣākhah; 80:37 each person's absorbing concern.
- `corroborators`: `(C: attachment 80:24 a1-a4 command lām, subject الإنسان, إلى طعامه complement)`, `(C: attachments 80:25 a2-a4 predicate/direct object/cognate accusative reinforce actual pouring)`, `(C: attachment 80:26 a1-a2 direct object الأرض and cognate accusative reinforce actual splitting)`, `(C: attachment 80:27 a1-a2 فِيهَا locative and حبّ object)`, `(C: attachment 80:32 a1-a4 beneficiary لكم and لأنعامكم)`, `(C: ن ط ف B002 earlier water-drop origin reactivated at ecological scale)`.
- `constraints`: `(K: ق ض ب B001 cutting is secondary to B003 fresh fodder because 80:28 is produce-list syntax)`, `(K: ح ب ب B002 love branch terminates here; حَبًّا is concrete grain)`, `(K: م و ه B005 gilding/illusion terminates; no masking image)`.
- `temporal_reactivation_notes`: The recitation commands looking only after the human has been confronted with origin, command, and incompletion. Food becomes a visible, staged replay of dependence.
- `rival_models`: A pure "agricultural catalog" explains local ayat but misses its placement after human origin and before final rupture; retained as primary local meaning, not sufficient as temporal synthesis.
- `grade`: strong
- `grade_rationale`: The passage gives an unusually explicit mechanical sequence with repeated cognate accusatives and a beneficiary closure.
- `source_queries_or_rows_used`: QAC rows 80:24-32; furuq rows listed; attachments 80:24 a1-a4 through 80:32 a1-a4.

### CSU-80-06: The Arrival That Can No Longer Be Neglected

- `candidate_id`: CSU-80-06
- `ayah_range`: 80:2, 80:8, 80:33-37
- `seed_type`: temporal/acoustic verified composite
- `seed`: repeated `جاء`: `جَاءَهُ` 80:2, `جَاءَكَ` 80:8, `جَاءَتِ ٱلصَّاخَّةُ` 80:33.
- `generating_set`: `(E: ج ي ء B001 coming/reaching)`, `(E: ص خ خ B001 overwhelming cry that strikes hearing)`, `(E: ص خ خ B004 great calamity)`, `(E: ي و م B003 severe event/day)`, `(E: ف ر ر B001 flight/escape)`, `(E: م ر ء B001 individual person)`, `(E: ء خ و B001 brotherhood/kin)`, `(E: ء م م B001 mother)`, `(E: ء ب و B001 father)`, `(E: ص ح ب B001 spouse/companion)`, `(E: ب ن ي B007 children/sons)`, `(E: ك ل ل B003 all/every)`, `(E: ش ء ن B001 matter/affair)`, `(E: غ ن ي B002 suffices/occupies)`.
- `selected_branches`: listed in generating set.
- `constructed_model`: The first arrival can be socially mishandled; the second arrival is marked by striving and fear; the final arrival is not a person but a hearing-shattering event. It dissolves every relational attachment into individual occupation. What was avoidable as human attention becomes unavoidable as final sound.
- `freeze_point`: after 80:37.
- `predictions_at_freeze`: expect final visible sorting after the sound; expect face-state disclosure; expect kinship vocabulary to remain relational rather than genealogical exposition.
- `unused_features_tested`: 80:38-42 face contrast; 80:1 face contraction; 80:5-10 attention allocation.
- `corroborators`: `(C: attachment 80:33 a1-a2 اذا frame and الصاخة subject of جاءت)`, `(C: attachment 80:34 a1-a3 day, fleeing subject, من أخيه complement)`, `(C: attachments 80:35-36 conjoined kinship pairs and possessive suffixes)`, `(C: attachment 80:37 a1-a7 fronted لكل امرئ, شأن delayed subject, يغنيه qualifying the affair)`, `(C: غ ن ي B001 from 80:5 reactivated as B002 sufficiency/occupation in 80:37)`.
- `constraints`: `(K: ص خ خ B003 piercing/stabbing branch terminates; no weapon or wound syntax)`, `(K: ف ر ر B002 tooth-exposure branch reserved for face imagery but not the flight construction)`, `(K: ء خ و B002 tether/bond is suggestive but not selected because 80:34 uses kinship noun directly)`.
- `temporal_reactivation_notes`: The repeated auditory form `جاء` creates escalating arrivals: individual seeker, active seeker, cosmic event. The final arrival reverses the opening: the one who turned away can no longer turn the event away.
- `rival_models`: "Family abandonment" alone is a local reading; the temporally conditioned model is arrival escalation plus relational dissolution.
- `grade`: medium-strong
- `grade_rationale`: Repetition of `جاء`, strong syntax, and the shift from interpersonal to final arrival are specific; lexical evidence from kin terms is straightforward rather than remote.
- `source_queries_or_rows_used`: QAC rows 80:2, 80:8, 80:33-37; furuq rows named; attachments 80:2, 80:8, 80:33-37.

### CSU-80-07: Faces At Closure: Bright Disclosure Versus Covering And Burden

- `candidate_id`: CSU-80-07
- `ayah_range`: 80:38-42, reactivating 80:1 and 80:11-16
- `seed_type`: lexical / temporal
- `seed`: 80:38:1 and 80:40:1 `وُجُوهٌ` x `و ج ه B001`.
- `generating_set`: `(E: و ج ه B001 face/front/what meets the viewer)`, `(E: س ف ر B001 removing covering)`, `(E: س ف ر B002 bright morning/face illumination)`, `(E: ض ح ك B001 expanded face with teeth showing)`, `(E: ض ح ك B003 joy/amazement showing as laughter)`, `(E: ب ش ر B005 joyful news opening the surface)`, `(E: ب ش ر B006 pleasant face/appearance)`, `(E: غ ب ر B004 dust/earth-colored darkness)`, `(E: غ ب ر B005 dark lasting calamity)`, `(E: ر ه ق B001 something covering/overwhelming by force)`, `(E: ق ت ر B004 face-darkening dust/gloom)`, `(E: ك ف ر B003 rejection/covering of truth)`, `(E: ف ج ر B004 breaking bounds from truth)`.
- `selected_branches`: listed in generating set.
- `constructed_model`: The surah closes by making the face the readable surface of response. Some faces are uncovered, bright, laughing, receptive to good news. Other faces have dust/gloom upon them and are overtaken by constricting darkness; their owners are named by covering/rejection and boundary-breaking.
- `freeze_point`: after 80:42.
- `predictions_at_freeze`: as closure, it should reactivate the opening face but not collapse the identities; it should also invert the honored/purified reminder section by showing who is brightened or covered.
- `unused_features_tested`: 80:1 `عبس`; 80:13-16 `سفرة/مكرمة/مطهرة/بررة`; 80:17 `ما أكفره`; 80:23 failed command.
- `corroborators`: `(C: ع ب س B001 opening face contraction returns as final face-state contrast)`, `(C: س ف ر B004 scribal/book branch in 80:15 and B002 bright face in 80:38 form a controlled root reactivation)`, `(C: ك ف ر B004 ingratitude in 80:17 narrows final الكفرة)`, `(C: attachment 80:40 a1-a4 عليهَا غبرة fronted predicate puts covering on faces)`, `(C: attachment 80:41 a1-a2 قترة as subject overwhelming the faces)`, `(C: attachment 80:42 a2-a3 الكفرة predicate and الفجرة matching descriptor)`.
- `constraints`: `(K: و ج ه B010 birth-hands-first branch terminates despite nearby creation theme; no birth syntax at closure)`, `(K: ض ح ك B007 palm-spathe split and B008 filled basin are remote echoes only, not selected)`, `(K: ف ج ر B001 physical water bursting is secondary to final moral descriptor B004)`.
- `temporal_reactivation_notes`: The first word activates face distortion. The final scene returns to faces after the whole sequence of reminder, origin, food, and final sound. Faces become the closure point because they disclose what attention initially concealed.
- `rival_models`: A purely emotional contrast is plausible but under-explains root reactivation of سفرة/مسفرة and كفر/كفرة.
- `grade`: strong
- `grade_rationale`: Closure is lexically dense, structurally parallel, and reactivates the opening and reminder sections.
- `source_queries_or_rows_used`: QAC rows 80:1, 80:15, 80:17, 80:38-42; furuq rows named; attachments 80:38 a1-a2, 80:39 a1, 80:40 a1-a4, 80:41 a1-a2, 80:42 a1-a3.

### CSU-80-08: Covering Versus Opening Across The Whole Passage

- `candidate_id`: CSU-80-08
- `ayah_range`: 80:17, 80:23-31, 80:40-42
- `seed_type`: verified composite
- `seed`: 80:17/42 `ك ف ر` branches B001/B003/B004, tested against split/opening roots.
- `generating_set`: `(E: ك ف ر B001 covering)`, `(E: ك ف ر B003 rejection/covering truth)`, `(E: ك ف ر B004 covering/denying blessing)`, `(E: ش ق ق B001 split/open)`, `(E: ف ج ر B001 wide splitting/bursting)`, `(E: ف ج ر B004 boundary-breaking/moral transgression)`, `(E: ن ش ر B001 spreading/opening)`, `(E: ن ش ر B002 resurrection)`, `(E: غ ب ر B004 dust covering)`, `(E: ق ت ر B004 face-covering gloom)`.
- `selected_branches`: listed in generating set.
- `constructed_model`: The human response is named as covering: covering truth, covering blessing, covering obligation. Against it the passage stages divine openings: creation from concealed drop, path eased, grave reopened, water poured, earth split, plants emerged. The final rejected group is visually covered.
- `freeze_point`: after assembling 80:17-31 and before final face contrast.
- `predictions_at_freeze`: expect final labels to join moral covering with visible covering; expect an opening/breaking root to become negative when attached to moral agency.
- `unused_features_tested`: 80:40-42 `غبرة/قترة/كفرة/فجرة`; 80:26 `شققنا`; 80:22 `أنشره`.
- `corroborators`: `(C: ف ج ر B004 supplies the negative moral boundary-breaking at closure)`, `(C: غ ب ر B004 and ق ت ر B004 supply visible covering on faces)`, `(C: attachment 80:26 cognate accusative strengthens actual splitting before moral rupture appears)`.
- `constraints`: `(K: ك ف ر B008 farmer covering seed is a remote possible echo with grain, but final الكفرة and 80:17 ما أكفره select moral rejection/ingratitude)`, `(K: ف ج ر B005 generosity terminates; no generosity role for final الفجرة)`.
- `temporal_reactivation_notes`: The root image evolves from moral covering in 80:17, to material opening in provision, to final moral label and face-covering at closure.
- `rival_models`: Crop-sowing "kāfir as farmer" is too attractive but fails because no root كفر appears in the crop section and final morphology is moral plural.
- `grade`: medium
- `grade_rationale`: Coherent cross-passage geometry, but some links are root-image contrasts rather than direct syntactic ties.
- `source_queries_or_rows_used`: QAC rows 80:17, 80:22, 80:26, 80:40-42; furuq rows named; attachments 80:17, 80:22, 80:26, 80:40-42.

### CSU-80-09: Seeing, Blindness, Looking, And Final Readable Faces

- `candidate_id`: CSU-80-09
- `ayah_range`: 80:2-4, 80:24, 80:38-42
- `seed_type`: lexical composite
- `seed`: 80:2 `ٱلْأَعْمَىٰ` x `ع م ي B001`, tested with `ن ظ ر B001` and `و ج ه B001`.
- `generating_set`: `(E: ع م ي B001 loss of eyesight)`, `(E: د ر ي B001 knowledge/detection)`, `(E: ن ظ ر B001 directed sight/reflection)`, `(E: و ج ه B001 face as visible surface/front)`, `(E: س ف ر B002 bright readable face)`, `(E: غ ب ر B004 dust-darkened surface)`.
- `selected_branches`: listed; `ع م ي B002` is tested as a rival but constrained.
- `constructed_model`: The passage begins with a person lacking sight and an addressee lacking knowledge of inward possibility. It later commands the human to look at food, then closes with faces that are visible signs. The visual field is disciplined: do not trust immediate social seeing; look at provision; final faces will disclose.
- `freeze_point`: after 80:24.
- `predictions_at_freeze`: expect closure through a visible sign; expect no wholesale conversion of physical blindness into moral blindness.
- `unused_features_tested`: 80:38-42 face contrast; 80:1 frown; 80:11-16 written/preserved reminder.
- `corroborators`: `(C: ن ظ ر B001 is explicitly commanded at 80:24)`, `(C: و ج ه B001 closure supplies visible face states)`, `(C: س ف ر B002 makes some faces bright after earlier concealed knowledge)`.
- `constraints`: `(K: ع م ي B002 heart-blindness is available but would overrun the local subject marker)`, `(K: ن ظ ر B009 watchman/guard and B010 debate terminate; no local guard/debate construction)`.
- `temporal_reactivation_notes`: Physical sight first fails as a social guide. Commanded looking later turns sight toward dependence. Final faces become the confirmed visual field.
- `rival_models`: "Blind man is spiritually seeing" remains possible as homiletic overlay but is not branch-generated enough for primary synthesis.
- `grade`: medium-strong
- `grade_rationale`: Strong temporal recurrence of sight/face, with constraints protecting against allegorical overreach.
- `source_queries_or_rows_used`: QAC rows 80:1-4, 80:24, 80:38-42; furuq rows named; relevant attachments.

### CSU-80-10: Parentage, Origin, And Flight From Kin

- `candidate_id`: CSU-80-10
- `ayah_range`: 80:18-21, 80:34-36
- `seed_type`: lexical / temporal
- `seed`: kinship list 80:34-36 tested backward against origin sequence.
- `generating_set`: `(E: ء ب و B001 fatherhood and causing/raising)`, `(E: ء م م B001 mother and nurture)`, `(E: ء خ و B001 brotherhood/kin)`, `(E: ص ح ب B001 companion/spouse)`, `(E: ب ن ي B007 children/sons)`, `(E: خ ل ق B002 creation)`, `(E: ن ط ف B002 seminal drop)`, `(E: س ب ل B001 path)`, `(E: م و ت B001 death)`, `(E: ف ر ر B001 flight)`.
- `selected_branches`: listed.
- `constructed_model`: The passage first compresses the human into origin and path; the final day dissolves the relational network that normally surrounds origin and continuity: sibling, mother, father, spouse, children. The one created through relation flees relation under final pressure.
- `freeze_point`: after 80:36.
- `predictions_at_freeze`: expect an individualizing closure; expect each person to be isolated by a matter of his own.
- `unused_features_tested`: 80:37 `لكل امرئ`; 80:5/37 `غني`.
- `corroborators`: `(C: ك ل ل B003 every/all in 80:37 individualizes)`, `(C: م ر ء B001 individual person repeated 80:34 and 80:37)`, `(C: غ ن ي B002 in 80:37 supplies self-occupation/sufficiency)`.
- `constraints`: `(K: ء م م B012 قصد/توجه and ء خ و B002 tether terminate; kinship nouns are primary)`, `(K: ب ن ي B001 building is only a remote image; 80:36 uses sons/children)`.
- `temporal_reactivation_notes`: Human lowly origin and final kin-flight are not contiguous, so this is a backward replay candidate rather than a primary local image.
- `rival_models`: "Family hierarchy" does not explain why the list comes after ṣākhah and before individual concern; the stronger model is relation dissolution.
- `grade`: medium
- `grade_rationale`: Clear lexical links but less branch-specific than the face, reminder, and provision candidates.
- `source_queries_or_rows_used`: QAC rows 80:18-21, 80:34-37; furuq rows named; attachments 80:34-37.

## Seed Pass Ledger

The following ledger records how each root's accepted branch seeds behaved after independent initiation. `Selected` means at least one occurrence x branch entered a candidate above. `Local` means a branch generated a local image only. `Terminated` means the branch was initiated but found no passage-local role after the full sweep.

### 80:1-10 Attention And Rebuke

| seed root | selected branches | local only | terminated / rejected branches |
| --- | --- | --- | --- |
| ع ب س | B001 in CSU-80-01 and CSU-80-07; B002 weak day echo with CSU-80-06 | none | B003,B004,B005,B006 |
| و ل ي | B007 in CSU-80-01; B006 rejected rival; B001/B002 weak proximity/sequence echo | B003 authority as weak role for addressee's station | B004,B005,B008,B010,B011,B012,B013,B014,B015,B016 |
| ج ي ء | B001 in CSU-80-01, CSU-80-02, CSU-80-06; B004 local "bringing/presence" | B005 weak compulsion echo at ṣākhah | B002,B003,B006 and duplicate export B002/B003 |
| ع م ي | B001 in CSU-80-01 and CSU-80-09; B002 constrained rival | B006 unknown path weak echo | B004,B005,B007,B008,B009 |
| د ر ي | B001 in CSU-80-01/09 | B004 pointed instrument remote echo terminated after no local instrument | B002,B003,B004 |
| ز ك و | B001/B002 in CSU-80-01/02 | none | B004,B005 |
| ذ ك ر | B003/B004/B009 in CSU-80-03; B007 weak honor echo | B008 document branch local echo with صحف | B001,B002 |
| ن ف ع | B001 in CSU-80-01 | B002 waterskin-side branch rejected despite water later | B002,B003 |
| غ ن ي | B001/B002 in CSU-80-02 and CSU-80-06 | B003 sound branch weak rejected; B004 residence none | B003,B004,B005,B006 |
| ص د ي | B007 in CSU-80-02 | B004 echo branch considered for sound but not selected | B001,B002,B003,B004,B005,B006,B008,B009,B010,B011 |
| س ع ي | B001/B002 in CSU-80-02 | B006 noble effort weak local | B003,B004,B005,B007,B008 |
| خ ش ي | B001 in CSU-80-02 | none | B002,B004 |
| ل ه و | B001 in CSU-80-02 | B002 local play/distraction rejected as too broad | B003,B004 |

### 80:11-16 Reminder And Custody

| seed root | selected branches | local only | terminated / rejected branches |
| --- | --- | --- | --- |
| ص ح ف | B002/B003 in CSU-80-03; B001 surface support | B005 constrained as opposite of protected reading | B004,B005 |
| ك ر م | B001 in CSU-80-03; B010 local preciousness | B002 plant quality later weak echo | B003,B004,B005,B006,B007,B008,B009 |
| ر ف ع | B001/B002 in CSU-80-03 | B005 proclamation weak; B010 voice-height rejected | B003,B004,B005,B006,B007,B008,B009,B010,B011,B012 |
| ط ه ر | B001/B005 in CSU-80-03 | B003/B004 water purification weak echo with provision | B002,B003,B004 |
| ي د ي | B001/B002/B004 in CSU-80-03 | B008 before-hands weak temporal echo; B009 deed-by-hands weak moral echo | B003,B005,B006,B007,B013,B014,B015,B016 |
| س ف ر | B004 in CSU-80-03; B001/B002 in CSU-80-07 | B003 travel rejected in 80:15 | B003 |
| ب ر ر | B001/B002 in CSU-80-03 | B003 kin-goodness weak echo with final family; B006 grain echo weak | B004,B005,B006,B007,B008 |

### 80:17-23 Human Origin And Command

| seed root | selected branches | local only | terminated / rejected branches |
| --- | --- | --- | --- |
| ء ن س | B001 in CSU-80-04/05; B002 weak seeing link; B005 eye-image local echo | B003 social comfort contrast with final flight | B004,B006 |
| ق ت ل | B001 in 80:17 local curse formula; B002 weak humbling/taming | B003 knowledge-control not selected | B004,B005,B006,B007,B008,B011,B012 |
| ك ف ر | B001/B003/B004 in CSU-80-04, CSU-80-07, CSU-80-08 | B008 seed-covering constrained; B009 atonement absent | B002,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014,B015 |
| خ ل ق | B001/B002/B003 in CSU-80-04; B005 weak fitness echo | B004 inward character local | B007,B008,B009,B010,B011,B012 |
| ش ي ء | B001 object/source in CSU-80-04; B002 will in 80:22 | B009 exclamation weak with ما أكفره | B003,B004,B005,B006,B007,B008 and duplicate nonlocal rows |
| ن ط ف | B002 in CSU-80-04 and CSU-80-05 | B003 fluid motion weak; B004 impurity constrained | B001,B004,B005,B006 |
| ق د ر | B001/B005 in CSU-80-04 | B003 ability weak; B004 constriction constrained | B006,B007 |
| س ب ل | B001 in CSU-80-04 | B004 downward release weak with water; B008 grain ear echo with food | B002,B005,B006,B007,B010 |
| ي س ر | B001 in CSU-80-04 | B005 smooth movement weak; B006 livestock increase weak with provision | B002,B003,B004,B007,B008,B009,B010,B011 |
| م و ت | B001 in CSU-80-04; B012 sleep/stillness weak echo | B003 dead land reactivated weakly by plants | B002,B004,B005,B006,B007,B008,B009,B010,B011,B013,B014 |
| ق ب ر | B001/B002 in CSU-80-04 | none | B003,B004 |
| ن ش ر | B001/B002 in CSU-80-04 and CSU-80-08 | B004 dry herbage revived by rain weak provision echo; B009 written sheets echo | B003,B005,B006,B007,B008,B010 |
| ء م ر | B002 in CSU-80-04; B001 affair echo with شأن | B005 sign/appointment weak; B006 grave matter weak | B003,B004,B005,B006,B007,B008,B009,B011 |
| ق ض ي | B004/B006 in CSU-80-04; B001 command-completion support | B005 make/execute weak | B002,B003,B007,B008 |

### 80:24-32 Provision And Ecology

| seed root | selected branches | local only | terminated / rejected branches |
| --- | --- | --- | --- |
| ن ظ ر | B001 in CSU-80-05/09 | B004 visible appearance weak; B008 eye-location echo | B002,B003,B005,B006,B007,B009,B010 |
| ط ع م | B001/B004 in CSU-80-05 | B002 feeding others local beneficiary; B005 fruit maturity echo; B010 grafting rejected | B006,B007,B008,B009,B010,B011,B012,B013,B014 |
| ص ب ب | B001/B002 in CSU-80-05 | B005 gathered mass weak; B006 liquid coloration weak | B003,B004,B007,B009,B010,B011 |
| م و ه | B001/B003 in CSU-80-05 | B002 abundance; B006 freshness/radiance weak echo | B004,B005,B007,B008 |
| ش ق ق | B001 in CSU-80-05/08 | B002 side/half weak; B003 hardship echo with final concern | B004,B005,B006,B007,B008,B009 |
| ء ر ض | B001/B002 in CSU-80-05 | B006 groundedness weak; B007 exposure echo with تصدى | B003,B004,B005,B008,B009,B010,B011,B012 |
| ن ب ت | B001/B002 in CSU-80-05 | B005 origin/site and B006 human growth weak with creation | B003,B004,B007,B008 |
| ح ب ب | B001 in CSU-80-05 | B004 heart-core weak echo; B006 saturation weak water echo | B002,B003,B005,B007,B008,B009,B010,B011 |
| ع ن ب | B001 in CSU-80-05 | none | B002,B003,B004,B005,B006,B007,B008 |
| ق ض ب | B003 in CSU-80-05; B001 cutting constrained; B004 branch/stalk support | B005 cutting tool remote | B002,B006,B007,B008,B009,B010,B011 |
| ز ي ت | B002/B001 in CSU-80-05 | B003 oiling weak | B004,B005 |
| ن خ ل | B001 in CSU-80-05 | B002 sifting weak; B003 choosing weak | B004,B005,B006 |
| ح د ق | B003 in CSU-80-05 | B001 enclosure support; B002 eye echo; B004 intense looking echo | none |
| غ ل ب | B002 in CSU-80-05; B001 weak force echo | none | none |
| ف ك ه | B002 in CSU-80-05; B001 enjoyment echo | B006 arrogance contrast weak | B003,B004,B007 |
| ء ب ب | B001 in CSU-80-05; B008 prepared season weak | B002 readiness echo | B003,B004,B006,B007 |
| م ت ع | B001/B003 in CSU-80-05 | B007 delay/enjoyment weak; B002 plant-height weak | B008,B009 |
| ن ع م | B005 in CSU-80-05; B001 blessing echo; B002 softness echo | B008 dispersal echo with flight weak | B003,B004,B006,B007,B009,B010,B011,B012,B013 |

### 80:33-42 Final Event And Face Sorting

| seed root | selected branches | local only | terminated / rejected branches |
| --- | --- | --- | --- |
| ص خ خ | B001/B004 in CSU-80-06 | B002 hard impact sound weak | B003 |
| ي و م | B003 in CSU-80-06 | B001/B002 temporal frame | none |
| ف ر ر | B001 in CSU-80-06; B002 weak face/tooth echo constrained | B005 haste weak | B003,B004,B006,B007,B008,B009,B010,B011,B014,B015,B016 |
| م ر ء | B001 in CSU-80-06/10; B002 moral personhood weak | B003 food-palatable echo | B004,B005,B006 and duplicate rows not independently selected |
| ء خ و | B001 in CSU-80-06/10 | B002 bond/tether weak metaphor; B003 intention weak | B002,B003 |
| ء م م | B001 in CSU-80-06/10 | B002 origin/gathering support; B012 direction weak | B003-B016 except B002/B012 local |
| ء ب و | B001 in CSU-80-06/10 | none | B002,B003 |
| ص ح ب | B001 in CSU-80-06/10 | B002 preservation by company weak contrast | B003-B008 |
| ب ن ي | B007 in CSU-80-06/10 | B001/B002 construction/body weak with creation | B003-B006,B008-B010 |
| ك ل ل | B003 in CSU-80-06 | B002 burden/charge weak; B001 fatigue weak | B004-B009,B011 |
| ش ء ن | B001 in CSU-80-06 | B002 concern/aim support; B006 lack of care contrast | B003,B004,B005 |
| و ج ه | B001 in CSU-80-07/09; B002/B003 support direction/facing; B008 rightness weak | B013 face-strike echo with عبس rejected | B006,B007,B009,B010,B011,B012,B014,B015 |
| ض ح ك | B001/B003/B006 in CSU-80-07 | B004 teeth local; B005 clear path echo | B002,B007,B008,B009,B011 |
| ب ش ر | B005/B006 in CSU-80-07; B001 surface support | B007 first signs echo; B008 inner/outer completeness weak | B002,B003,B004 |
| غ ب ر | B004/B005 in CSU-80-07/08 | B001 remnant weak; B002 pastness weak | B003,B008 |
| ر ه ق | B001 in CSU-80-07 | B003 burden/overload support; B004 urgency weak | B002,B005,B006,B007 |
| ق ت ر | B004 in CSU-80-07; B001 constriction support | B003 smoke smell weak; B005 glittering rejected | B002,B006,B008,B009 |
| ف ج ر | B004 in CSU-80-07/08; B001 contrastive opening in CSU-80-08 | B002 dawn echo with مسفرة weak | B003,B005,B006 |

## Constructional, Morphosyntactic, And Temporal Seeds

| construction seed | result |
| --- | --- |
| 80:1 coordinated `عَبَسَ وَتَوَلَّىٰ` | Generates CSU-80-01; attachment row forces the two actions together. |
| 80:2 `جاءه الأعمى` subject/object attachment | Supports CSU-80-01 and CSU-80-06; the blind man is not the object but the arriving subject. |
| 80:3-4 `وما يدريك لعله... أو...` | Supports unseen possibility and blocks premature judgment. |
| 80:5-10 doubled `أمّا من... فأنت...` | Generates CSU-80-02; contrastive syntax is stronger than any isolated branch. |
| 80:6 `له` versus 80:10 `عنه` | Directional corroboration for attention allocation. |
| 80:11 `كلا` | Boundary operator: terminates the misallocated attention scene and opens reminder object. |
| 80:13-16 `في صحف... بأيدي سفرة` | Generates CSU-80-03; container/custody construction. |
| 80:17 passive + exclamation `قتل الإنسان ما أكفره` | Local curse/exclamation, not literal killing event. |
| 80:18-19 two `من` source frames | Supports low origin and dependency in CSU-80-04. |
| 80:20-22 repeated `ثم` lifecycle steps | Temporal scaffold for origin-path-death-burial-reopening. |
| 80:23 `لمّا يقض ما أمره` | Completion-command constraint on the human-origin image. |
| 80:24 command `فلينظر... إلى طعامه` | Generates CSU-80-05 and CSU-80-09. |
| 80:25 and 80:26 cognate accusatives `صبا`, `شقا` | Intensify actual pouring and actual splitting. |
| 80:27 `فيها` locative | Places growth inside split earth. |
| 80:28-31 coordinated produce list | Multiplicity/abundance, not a single allegorical crop. |
| 80:32 double beneficiary `لكم ولأنعامكم` | Closes provision image by human/livestock benefit. |
| 80:33 `فإذا جاءت الصاخة` | Final arrival seed for CSU-80-06. |
| 80:34-36 kinship list with possessive suffixes | Relational dissolution seed for CSU-80-10. |
| 80:37 fronted `لكل امرئ... شأن يغنيه` | Individualizing closure of flight scene. |
| 80:38-42 paired `وجوه` descriptions | Generates CSU-80-07; final sorting by face-state. |
| 80:42 `هم الكفرة الفجرة` | Moral predicate closure; constrains covering/breaking imagery. |

## Image Packet Catalog

### IMG-80-A: Misallocated Attention

- Starting seed: `ع ب س B001`, 80:1.
- Complete image: face contraction plus turning away from an arriving blind man whose inward purification/remembrance remains possible.
- Passage-order assembly: face -> turning -> arrival -> unknown inward future -> contrastive attention.
- Participants and roles: addressee = misallocating responder; blind man = arriving possible purifier/rememberer; self-sufficient one = wrongly favored target.
- Operation / mechanism: visible surface response misreads unseen spiritual possibility.
- Direction / force / medium: toward/away prepositions and attention.
- Temporal development: 80:1-4 formed; 80:5-10 confirms; 80:38-42 reactivates faces.
- Outcome / closure: final faces disclose what the opening face failed to read.
- Exact branch constituents: ع ب س B001; و ل ي B007; ج ي ء B001; ع م ي B001; د ر ي B001; ز ك و B001/B002; ذ ك ر B009; ن ف ع B001; غ ن ي B001/B002; ص د ي B007; س ع ي B001/B002; خ ش ي B001; ل ه و B001.
- Unfilled roles: none for local image.
- Status: COMPLETE.

### IMG-80-B: Honored Reminder Custody

- Starting seed: `ذ ك ر B009`, 80:11.
- Complete image: reminder becomes an honored, elevated, purified written deposit in noble truthful hands.
- Passage-order assembly: possible remembrance -> declared reminder -> open access -> written sheets -> raised/purified -> hands/scribes -> noble truthful agents.
- Participants and roles: reminder = object; sheets = medium; hands/scribes = custodians; noble/true agents = quality constraints.
- Operation / mechanism: neglected benefit is removed from social contingency and grounded in protected transmission.
- Direction / force / medium: upward elevation, purity, written custody.
- Temporal development: 80:4 predicts; 80:11-16 completes.
- Outcome / closure: final rejection/brightness tests reception.
- Exact branch constituents: ذ ك ر B003/B004/B009; ص ح ف B002/B003; ك ر م B001; ر ف ع B001/B002; ط ه ر B001/B005; ي د ي B001/B002/B004; س ف ر B004; ب ر ر B001/B002.
- Unfilled roles: none.
- Status: COMPLETE.

### IMG-80-C: Origin-Path-Closure-Reopening

- Starting seed: `ن ط ف B002`, 80:19.
- Complete image: human emerges from drop, is measured, given path, dies, is buried, and is spread/raised when willed.
- Passage-order assembly: rebuke of human -> source question -> drop -> creation/measure -> path/ease -> death/grave -> reopening -> unfulfilled command.
- Participants and roles: human = dependent object; divine action = creator/measurer/easer/killer/burier/raiser; command = unfulfilled obligation.
- Operation / mechanism: concealed origin becomes measured passage and future reopening.
- Direction / force / medium: from hidden fluid through path to grave enclosure and reopening.
- Temporal development: 80:17-23, reactivated by water/plant sequence.
- Outcome / closure: final moral sorting.
- Exact branch constituents: ن ط ف B002; خ ل ق B001/B002; ق د ر B001/B005; س ب ل B001; ي س ر B001; م و ت B001; ق ب ر B001/B002; ن ش ر B001/B002; ء م ر B002; ق ض ي B004/B006.
- Unfilled roles: `السبيل` exact referent remains open.
- Status: COMPLETE with one unresolved local referent.

### IMG-80-D: Provision Mechanics

- Starting seed: `ن ظ ر B001` / construction 80:24.
- Complete image: look at food as staged dependence: water poured, earth split, growth produced, listed, and assigned as benefit.
- Passage-order assembly: command to look -> water -> earth split -> growth -> produce list -> benefit for humans/livestock.
- Participants and roles: human = viewer/beneficiary; water = medium; earth = receiving/splitting field; plants = produced provision; livestock = co-beneficiaries.
- Operation / mechanism: descent, incision/opening, emergence, diversification, use.
- Direction / force / medium: vertical water, opened earth, upward growth.
- Temporal development: 80:24-32.
- Outcome / closure: everyday provision stands before final event.
- Exact branch constituents: ن ظ ر B001; ط ع م B001/B004; ص ب ب B001/B002; م و ه B001/B003; ش ق ق B001; ء ر ض B001/B002; ن ب ت B001/B002; ح ب ب B001; ع ن ب B001; ق ض ب B003; ز ي ت B001/B002; ن خ ل B001; ح د ق B003; غ ل ب B002; ف ك ه B002; ء ب ب B001; م ت ع B001/B003; ن ع م B005.
- Unfilled roles: none.
- Status: COMPLETE.

### IMG-80-E: Final Sound And Relational Dissolution

- Starting seed: `ص خ خ B001`, 80:33.
- Complete image: a hearing-shattering arrival dissolves kinship proximity into individual absorbing concern.
- Passage-order assembly: final arrival -> day of flight -> brother/mother/father/spouse/children -> every individual has sufficient concern.
- Participants and roles: ṣākhah = unavoidable event; person = fleeing individual; kin = abandoned relation; شأن = absorbing matter.
- Operation / mechanism: sound/event pressure breaks social bonds.
- Direction / force / medium: arrival, flight away from kin.
- Temporal development: 80:33-37.
- Outcome / closure: faces sorted in 80:38-42.
- Exact branch constituents: ص خ خ B001/B004; ج ي ء B001; ي و م B003; ف ر ر B001; م ر ء B001; ء خ و B001; ء م م B001; ء ب و B001; ص ح ب B001; ب ن ي B007; ك ل ل B003; ش ء ن B001; غ ن ي B002.
- Unfilled roles: none.
- Status: COMPLETE.

### IMG-80-F: Face Disclosure

- Starting seed: `و ج ه B001`, 80:38.
- Complete image: faces become readable disclosures, either bright/uncovered and joyful or dust-covered and gloom-overwhelmed, ending in covering and boundary-breaking labels.
- Passage-order assembly: faces -> bright -> laughing/rejoicing -> faces -> dust upon them -> gloom overwhelms -> disbelievers/boundary-breakers.
- Participants and roles: faces = disclosure surface; brightness/laughter/rejoicing = accepted state; dust/gloom = covering state; final labels = moral interpretation.
- Operation / mechanism: final inward reality appears on outer surface.
- Direction / force / medium: surface exposure versus overlaying covering.
- Temporal development: 80:38-42, reactivating 80:1.
- Outcome / closure: surah closes where surface and moral status coincide.
- Exact branch constituents: و ج ه B001; س ف ر B001/B002; ض ح ك B001/B003/B006; ب ش ر B005/B006; غ ب ر B004/B005; ر ه ق B001; ق ت ر B004; ك ف ر B003/B004; ف ج ر B004.
- Unfilled roles: none.
- Status: COMPLETE.

## Audit Notes

- Exhaustive singleton seeding was applied at the root/branch level. Repeated roots were checked occurrence-sensitively when their contexts differ: `ج ي ء` at 80:2/8/33, `ذ ك ر` at 80:4/11/12, `ز ك و` at 80:3/7, `غ ن ي` at 80:5/37, `ك ف ر` at 80:17/42, `س ف ر` at 80:15/38, `و ج ه` at 80:38/40, and `م ر ء` at 80:34/37.
- Branches from duplicate export rows were not double-counted as independent evidence; they were treated as duplicate branch dossiers where the branch ID and image overlap.
- The strongest convergences are CSU-80-01, CSU-80-03, CSU-80-05, and CSU-80-07. The broadest whole-passage simulations are CSU-80-04, CSU-80-06, CSU-80-08, and CSU-80-09.
- Weak branches were intentionally retained in the ledger as terminated or local-only rather than elevated into primary meaning.
