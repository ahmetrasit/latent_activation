# S97 Stage 1 Pass 2: temporally conditioned reactivation

Assigned passage: S97, ayat 1-5.

Sacred Arabic text:

1. `إِنَّآ أَنزَلْنَٰهُ فِى لَيْلَةِ ٱلْقَدْرِ`
2. `وَمَآ أَدْرَىٰكَ مَا لَيْلَةُ ٱلْقَدْرِ`
3. `لَيْلَةُ ٱلْقَدْرِ خَيْرٌۭ مِّنْ أَلْفِ شَهْرٍۢ`
4. `تَنَزَّلُ ٱلْمَلَٰٓئِكَةُ وَٱلرُّوحُ فِيهَا بِإِذْنِ رَبِّهِم مِّن كُلِّ أَمْرٍۢ`
5. `سَلَٰمٌ هِىَ حَتَّىٰ مَطْلَعِ ٱلْفَجْرِ`

Resource note: `resources/qac.sqlite` and `resources/furuq_v4.sqlite` are zero-byte placeholders in this checkout. The usable local exports are `resources/qac_root_ayah.tsv`, `resources/v4_branches.tsv`, and `resources/attachments.tsv`. I used only S97 rows from QAC/attachments and only `status=accepted` branch rows for roots occurring in S97.

## Root cause of Pass 1 limitation

Pass 1 did the evidence collection and internal synthesis but stopped at an in-context readiness signal. It did not externalize a full seed ledger, so only a limited number of words appeared to have been visited per finding. The limitation was not lack of branch access; it was premature compression. This pass restarts from the first rooted word and records every occurrence x accepted-branch seed, plus constructional, morphosyntactic, and temporal seeds.

## Passage root order and branch inventory

Passage rooted occurrence order:

`97:1:2 ن ز ل` -> `97:1:4 ل ي ل` -> `97:1:5 ق د ر` -> `97:2:2 د ر ي` -> `97:2:4 ل ي ل` -> `97:2:5 ق د ر` -> `97:3:1 ل ي ل` -> `97:3:2 ق د ر` -> `97:3:3 خ ي ر` -> `97:3:5 ء ل ف` -> `97:3:6 ش ه ر` -> `97:4:1 ن ز ل` -> `97:4:2 م ل ك` -> `97:4:3 ر و ح` -> `97:4:5 ء ذ ن` -> `97:4:6 ر ب ب` -> `97:4:8 ك ل ل` -> `97:4:9 ء م ر` -> `97:5:1 س ل م` -> `97:5:4 ط ل ع` -> `97:5:5 ف ج ر`.

Accepted lexical seed inventory:

- `ن ز ل`: B001 hبوط/حلول, B002 إنزال/إيصال, B003 منزل/منزلة, B004 وضع في منزلته, B005 نزل الضيف, B006 نازلة شديدة, B007 نزال الحرب, B009 ماء الرجل, B010 نزلة واحدة.
- `ل ي ل`: B001 الليل/ظلمته, B002 مزاولة الأمر ليلا, B003 الليلة القريبة الداخلة, B004 اسم ليلى.
- `ق د ر`: B001 مقدار/حد/أجل, B003 قدرة/تمكن/ملك, B004 تضييق, B005 تدبير بتقدير ونظر, B006 موافقة القدر والوسط, B007 قدر الطبخ.
- `د ر ي`: B001 الدراية والعلم, B002 القصد والاعتماد, B003 الختل والاستتار للصيد, B004 المدرى والحد المحدد.
- `خ ي ر`: B001 خير نافع ضد الشر, B002 فضل وصلاح واصطفاء, B003 اختيار واستخارة, B005 كرم وهبة, B006 استدراج الحيوان من جحره.
- `ء ل ف`: B001 العدد ألف, B002 ضم وتأليف, B005 ألفة وأنس وملازمة, B006 حرف الألف.
- `ش ه ر`: B001 الشهر بالهلال والمدة, B002 الشهرة والظهور, B003 شهر السيف.
- `م ل ك`: B001 قوة وتماسك, B002 ملك وتصرف, B003 ملك وسلطان, B004 إملاك وتزويج, B005 ملاك الأمر وعماده, B006 وسط الطريق/الوادي, B007 الماء ملاك الأمر, B008 المتقدم القائد في الحيوان. The angel branch B009 is `review`, so it is not used as furuq lexical evidence.
- `ر و ح`: B001 نفس/روح الحياة, B003 ريح ونسيم, B004 رائحة, B005 رواح العشي, B006 رد الحق, B007 راحة, B008 مراوحة, B009 سعة وانبساط, B010 نشاط للمعروف, B011 قوة وغلبة, B012 ريحان النبات, B014 راحة الكف, B015 الراح الخمر, B016 موت بإراحة, B017 تفطر الشجر, B018 تحصن الفرس.
- `ء ذ ن`: B001 أذن جارحة/عروة, B002 إصغاء وقبول مسموع, B003 علم وإعلام بنداء, B004 إذن وترخيص.
- `ر ب ب`: B001 ربوبية وملك وسيادة, B002 إصلاح وتربية وإتمام, B003 علم رباني, B004 جماعات كثيرة, B005 ربيب/حضانة, B006 رب خاثر وإصلاح به, B007 لزوم وإقامة ودوام, B008 رباب السحاب, B009 حداثة/قرب عهد, B010 وعاء القداح, B011 عهد وميثاق, B012 نبات باق, B013 ماء كثير, B014 قطيع, B015 حرف رب, B016 حاجة/عقدة/نعمة, B017 رئيس الملاحين.
- `ك ل ل`: B001 كلال وخلاف الحدة, B002 عيال وثقل, B003 كل إحاطة وتمام, B004 كلالة قرابة عارضة, B005 إكليل وما يحيط, B006 كلة ستر وبيت, B007 كلكل صدر, B008 قصر وغلظ, B009 جماعات, B011 تبسم/لمع.
- `ء م ر`: B001 شأن وحال, B002 طلب وإلزام, B003 ولاية وسلطان, B004 نماء وبركة, B005 علامة وموعد, B006 أمر عظيم منكر, B007 مشاورة وتدبير رأي, B008 ضعيف الرأي التابع, B009 ولد الضأن, B011 تسليح القناة بسنان.
- `س ل م`: B001 سلامة وبراءة من الآفات, B004 صلح ومسالمة, B005 سلم بيع وسلف, B006 سلم مرقاة/سبب, B007 حجارة صلبة, B008 شجر للدباغة, B009 سليم ملدوغ, B010 عظام ومفاصل, B011 دلو بعروة, B012 تسليم وتخلية, B013 أخذ أسيرا.
- `ط ل ع`: B001 طلوع النير وموضعه, B002 ظهور المقبل, B003 إشراف وكشف, B004 طليعة تستكشف, B005 خروج الطلع والنبات, B006 مصعد ومأتى مشرف, B007 امتلاء مستوعب, B008 تطلع النفس, B009 طلعة مرئية, B010 سهم يجاوز الغرض, B011 قيء, B012 طول بارز.
- `ف ج ر`: B001 انشقاق واسع وانبعاث, B002 انبلاج الصبح, B003 اندفاع الكثير بغتة, B004 فجور وخرق ستر, B005 جود واسع, B006 وقائع الفجار.

Total accepted root branches: 129. Occurrence x branch lexical seeds: 158, because `ن ز ل` occurs twice, `ل ي ل` three times, and `ق د ر` three times.

## Candidate synthesis units

### S97-CAND-01: measured descent into a bounded night

- `candidate_id`: S97-CAND-01
- `ayah_range`: 97:1-5
- `seed_type`: lexical with convergent constructional support
- `seed`: first rooted word `97:1:2 أَنزَلْنَاهُ`, especially `ن ز ل B002` and `B001`
- `generating_set`: `(E: ن ز ل B002 97:1:2 إنزال وإيصال)`, `(E: ن ز ل B001 97:1:2 هبوط وحلول)`, `(E: ل ي ل B001 97:1:4 الليل وظلمته)`, `(E: ق د ر B001 97:1:5 مقدار وحد وأجل)`, `(E: ق د ر B005 97:1:5 تدبير بتقدير)`, `(E: attachment 97:1:a4 في governs ليلة as temporal complement)`, `(E: attachment 97:1:a5 ليلة القدر idafa)`.
- `selected_branches`: `ن ز ل B001/B002`, `ل ي ل B001`, `ق د ر B001/B005`, later convergent `ن ز ل B004`, `ق د ر B006`.
- `constructed_model`: A high-to-low delivery is not merely dropped; it is placed into a bounded dark temporal vessel whose identity is measurement, apportionment, and prior arrangement. The first ayah activates a motion event, a temporal interior, and an exact measure.
- `freeze_point`: after `97:1` before the interrogative reactivation in `97:2`.
- `predictions_at_freeze`: the passage should reactivate the night, clarify its status, add agents or mechanism for descent, show why measure is not only quantity but decree/ordering, and close at a temporal boundary rather than a generic topic ending.
- `unused_features_tested`: `97:2` interrogative repetition; `97:3` comparative better-than-thousand-months; `97:4` second descent, angels/spirit as subject/co-subject, `فيها`, `بإذن ربهم`, `من كل أمر`; `97:5` peace until dawn.
- `corroborators`: `(C: sequence 97:2 repeats ليلة القدر before explanation)`, `(C: attachment 97:2:a3 embedded question makes the night the object of knowing)`, `(C: 97:3 comparative predicate خير confirms extraordinary valuation)`, `(C: ء ل ف B001 + ش ه ر B001 counted months independently support measure and temporal scale)`, `(C: ن ز ل B002 97:4:1 second descent repeats delivery)`, `(C: ن ز ل B004 placing in proper station supports ordered descent)`, `(C: ء ذ ن B004 authorization supplies controlled channel)`, `(C: ر ب ب B001/B002 owner-lord and caretaker supply source authority)`, `(C: ك ل ل B003 all/totality supplies comprehensive scope)`, `(C: ء م ر B001/B002 matter/command supplies decreed content)`, `(C: س ل م B001 + حتى مطلع الفجر gives non-harmful state and endpoint)`, `(C: ط ل ع B001 + ف ج ر B002 dawn rising/appearance gives predicted temporal closure)`.
- `constraints`: `(K: pronoun ه in 97:1 is direct object but antecedent is not named inside the ayah)`, `(K: ليلة is temporal complement, not a physical container)`, `(K: ق د ر B007 cooking pot is remote and should not overwrite contextual qadr)`, `(K: تنزل in 97:4 has overt subject الملائكة and الروح, so it cannot be only a repetition of the object sent in 97:1)`.
- `temporal_reactivation_notes`: The first ayah sets an unresolved object and the phrase `ليلة القدر`. The second ayah restarts the phrase as question, the third as valuation, the fourth as activity inside it, and the fifth as closure. The phrase is progressively reactivated as time, hidden worth, active locus, and bounded state.
- `rival_models`: physical vessel/pot model from `ق د ر B007` is weak; generic "holy night" theme is too static; martial descent from `ن ز ل B007` is defeated.
- `grade`: strong
- `grade_rationale`: Multiple independent channels converge: lexical descent, temporal night, qadr as measured limit/tadbir, attachments, repeated phrase, comparative scale, authorization, total command, and dawn endpoint. The model preserves primary meaning and treats secondary geometry as simulation.
- `source_queries_or_rows_used`: QAC S97 rows for `ن ز ل/ل ي ل/ق د ر`; branch rows for `ن ز ل B001/B002/B004`, `ل ي ل B001`, `ق د ر B001/B005/B006`; attachments `97:1:a2-a5`, `97:2:a3-a5`, `97:3:a1-a4`, `97:4:a1-a8`, `97:5:a1-a3`.

### S97-CAND-02: interrogative reactivation and knowledge threshold

- `candidate_id`: S97-CAND-02
- `ayah_range`: 97:2-3, with backward link to 97:1 and forward link to 97:4-5
- `seed_type`: lexical/constructional
- `seed`: `97:2:2 أَدْرَىٰكَ`, `د ر ي B001`
- `generating_set`: `(E: د ر ي B001 الدراية والعلم)`, `(E: attachment 97:2:a1 ما as interrogative subject)`, `(E: attachment 97:2:a2 ك object suffix addressee)`, `(E: attachment 97:2:a3 embedded question ما ليلة القدر)`, `(E: repetition 97:1->97:2 ليلة القدر)`.
- `selected_branches`: `د ر ي B001`; rejected as primary: `د ر ي B002/B003/B004`.
- `constructed_model`: The hearing is stopped and made to ask how the addressee could know the night. The phrase from 97:1 is not merely repeated; it is re-opened as an epistemic gap requiring staged disclosure.
- `freeze_point`: after 97:2.
- `predictions_at_freeze`: later material should answer by describing the night's value, activity, authorization, and boundary, not by giving a dictionary definition.
- `unused_features_tested`: 97:3 comparative; 97:4 descent and authorized command; 97:5 peace until dawn.
- `corroborators`: `(C: 97:3 predication خير supplies first answer)`, `(C: ء ل ف B001 and ش ه ر B001 create calculable scale)`, `(C: 97:4 gives operational answer: descent in it by permission)`, `(C: 97:5 gives duration answer: until dawn)`.
- `constraints`: `(K: د ر ي B002 قصد/غزو, B003 hunting concealment, B004 pointed comb/horn produce vivid but passage-local weak forks)`, `(K: the interrogative construction is about making-known, not about attack, hunting, or a physical point)`.
- `temporal_reactivation_notes`: 97:2 forces backward replay of 97:1. The listener had heard "Night of Qadr"; the question makes that phrase unresolved and prepares the following ayat as answer.
- `rival_models`: Hidden-hunting model from `د ر ي B003` plus night darkness is possible as a weak secondary image: the night conceals what is being disclosed. It fails because no prey, hunter, weapon, or stalking syntax appears.
- `grade`: medium-strong
- `grade_rationale`: The construction is strongly licensed and explains sequence, but the lexical depth comes mostly from the ordinary knowledge branch; remote branches terminate.
- `source_queries_or_rows_used`: QAC `د ر ي 97:2`, attachments `97:2:a1-a5`, furuq `د ر ي B001-B004`.

### S97-CAND-03: comparative compression of one night against counted months

- `candidate_id`: S97-CAND-03
- `ayah_range`: 97:3
- `seed_type`: verified composite
- `seed`: `97:3:3 خَيْرٌ` with construction `خير من ألف شهر`
- `generating_set`: `(E: خ ي ر B001 خير نافع مرغوب ضد الشر)`, `(E: خ ي ر B002 فضل وصلاح واصطفاء)`, `(E: attachment 97:3:a2 خير predicate of ليلة القدر)`, `(E: ء ل ف B001 العدد ألف)`, `(E: ش ه ر B001 الشهر المعلوم بالهلال والمدة)`, `(E: attachment 97:3:a3 من governs ألف after comparative)`, `(E: attachment 97:3:a4 شهر completes ألف)`.
- `selected_branches`: `خ ي ر B001/B002`, `ء ل ف B001`, `ش ه ر B001`, with weak secondary support from `ء ل ف B002`.
- `constructed_model`: A single delimited night is weighed against a large assembled duration. The phrase compresses massive repeated temporal units into a lesser side of comparison; the special night exceeds the aggregation.
- `freeze_point`: after 97:3.
- `predictions_at_freeze`: if this is not just value rhetoric, the next ayah should explain what makes the night operationally dense, and the close should give the night's temporal limit.
- `unused_features_tested`: 97:4 descent of agents and command; 97:5 peace until dawn.
- `corroborators`: `(C: 97:4 repeated descent supplies activity density inside one night)`, `(C: ك ل ل B003 comprehensive "every" aligns with total scope)`, `(C: ء م ر B001/B002 supplies content of matters/commands)`, `(C: حتى مطلع الفجر confirms the one-night bound)`, `(C: ء ل ف B002 assembly/ordering is a secondary support for many units gathered as a count)`.
- `constraints`: `(K: ألف B005 familiarity and B006 letter-name are local dead ends)`, `(K: شهر B002 fame and B003 unsheathing sword are secondary and not the comparison's surface meaning)`, `(K: خير B006 animal extraction is rejected)`.
- `temporal_reactivation_notes`: After 97:1-2, the same phrase returns in 97:3 as subject of valuation. The model shifts from hidden identity to comparative magnitude.
- `rival_models`: Fame/manifestation fork from `ش ه ر B002` can say the hidden night becomes manifest in worth; it is weak because the local phrase is `ألف شهر`, not fame.
- `grade`: medium-strong
- `grade_rationale`: The grammar and ordinary lexical branches are strong. The compression image is strengthened by the later operational density but depends on comparative structure more than remote branch convergence.
- `source_queries_or_rows_used`: QAC rows `خ ي ر/ء ل ف/ش ه ر 97:3`, branch rows listed, attachments `97:3:a1-a4`.

### S97-CAND-04: authorized descent of agents with every matter

- `candidate_id`: S97-CAND-04
- `ayah_range`: 97:4
- `seed_type`: morphosyntactic/lexical composite
- `seed`: `97:4:1 تَنَزَّلُ`
- `generating_set`: `(E: ن ز ل B002 97:4:1 تنزل الملائكة والأمر)`, `(E: ن ز ل B001 descent/hulul)`, `(E: attachment 97:4:a1 الملائكة overt subject)`, `(E: attachment 97:4:a2 الروح conjoined co-subject)`, `(E: attachment 97:4:a3 فيها setting of descent)`, `(E: ء ذ ن B004 permission/authorization)`, `(E: attachment 97:4:a4 بإذن means/authorization)`, `(E: ر ب ب B001 lord/master/source authority)`, `(E: ك ل ل B003 totality)`, `(E: ء م ر B001 matter/affair)`, `(E: ء م ر B002 command/obligation)`.
- `selected_branches`: `ن ز ل B001/B002/B004`, `ء ذ ن B004`, `ر ب ب B001/B002`, `ك ل ل B003`, `ء م ر B001/B002`, structural QAC surface `الملائكة`, `ر و ح B001`.
- `constructed_model`: The night becomes an authorized channel. Descent is populated by overt subjects and constrained by permission from their Lord, with every matter/command entering the channel.
- `freeze_point`: after 97:4.
- `predictions_at_freeze`: closure should name the resulting state of the night and its limit; the event should not culminate in violence or disorder.
- `unused_features_tested`: 97:5 peace until dawn; earlier 97:1 descent of object and 97:3 comparative value.
- `corroborators`: `(C: 97:1 initial أَنزلناه establishes descent before 97:4 repeats it)`, `(C: 97:3 خير supplies reason for value)`, `(C: س ل م B001/B004 confirms non-harm, wholeness, and peace)`, `(C: ط ل ع B001 + ف ج ر B002 gives boundary)`, `(C: ق د ر B005 tadbir links decree/measure to الأمر)`, `(C: ق د ر B001 limit/measure supports controlled authorization)`.
- `constraints`: `(K: م ل ك B009 angel branch is review, not accepted; do not count it as furuq lexical proof)`, `(K: م ل ك accepted branches can support authority/strength only secondarily, while the surface word supplies angels structurally)`, `(K: ء م ر B006 monstrous matter and B011 spear-tip are rejected as local primary)`, `(K: ن ز ل B007 battle descent defeated by سلام)`.
- `temporal_reactivation_notes`: 97:4 reactivates the descent verb from 97:1 after the phrase "Night of Qadr" has been questioned and valued. The earlier descent is no longer isolated; it becomes part of a night-long authorized descent system.
- `rival_models`: a military mobilization fork from `ن ز ل B007`, `ش ه ر B003`, `ء م ر B011`, `د ر ي B002/B004` is lexically available but strongly defeated by syntax and 97:5.
- `grade`: medium-strong
- `grade_rationale`: The morphosyntax is very strong, the authorization and total command branches are exact, but the angel participant cannot be branch-confirmed from accepted furuq rows.
- `source_queries_or_rows_used`: QAC `97:4` roots, attachments `97:4:a1-a8`, accepted furuq for `ن ز ل/ء ذ ن/ر ب ب/ك ل ل/ء م ر/ر و ح/م ل ك`.

### S97-CAND-05: peace-state held until the opening of dawn

- `candidate_id`: S97-CAND-05
- `ayah_range`: 97:5, reactivating 97:1-4
- `seed_type`: lexical/constructional/temporal
- `seed`: `97:5:1 سَلَامٌ`
- `generating_set`: `(E: س ل م B001 السلامة والبراءة من الآفات)`, `(E: س ل م B004 الصلح والمسالمة)`, `(E: attachment 97:5:a1 سلام fronted predicate of هي)`, `(E: ط ل ع B001 طلوع النير وموضعه)`, `(E: attachment 97:5:a2 مطلع governed by حتى as endpoint)`, `(E: ف ج ر B002 انبلاج الصبح من الليل)`, `(E: attachment 97:5:a3 الفجر completes مطلع)`.
- `selected_branches`: `س ل م B001/B004`, `ط ل ع B001`, `ف ج ر B002`, with secondary `ف ج ر B001` and `ط ل ع B003`.
- `constructed_model`: The night, after descent and decree, is named as a safe/peaceful condition that persists until a precise emergence point: dawn's rise/opening from the night.
- `freeze_point`: after 97:5.
- `predictions_at_freeze`: because this is final closure, prior unresolved elements should be gathered: night, descent, authorization, command, value, and temporal endpoint.
- `unused_features_tested`: backward replay of 97:1-4.
- `corroborators`: `(C: ل ي ل B001 night supplies the state being ended)`, `(C: ق د ر B001 limit/أجل supports endpoint)`, `(C: ن ز ل B002 authorized descent explains why peace is produced rather than ordinary darkness)`, `(C: ء ذ ن B004 + ر ب ب B001 constrain the event as permitted)`, `(C: ك ل ل B003 + ء م ر B001/B002 explain why the state concerns all matters)`.
- `constraints`: `(K: س ل م B006 ladder/means is tempting with descent/ascent but no ascent syntax is present)`, `(K: س ل م B012 handing over may support delivery only weakly; it cannot replace سلام as peace/safety)`, `(K: ف ج ر B004 moral breach is defeated by سلام)`, `(K: ط ل ع B010 arrow overshoot is unsupported)`.
- `temporal_reactivation_notes`: The final ayah converts the dark-night frame into a bounded peace interval. `مطلع الفجر` closes the same temporal container opened by `ليلة`.
- `rival_models`: rupture/flow fork from `ف ج ر B001` can make dawn an opening that releases the night; useful as secondary geometry, not primary meaning.
- `grade`: strong
- `grade_rationale`: It explains closure, temporal boundary, and backward reactivation, with exact lexical and attachment support.
- `source_queries_or_rows_used`: QAC `س ل م/ط ل ع/ف ج ر 97:5`, attachments `97:5:a1-a3`, furuq `س ل م B001/B004`, `ط ل ع B001`, `ف ج ر B002`.

### S97-CAND-06: qadr/amr/idhn/rabb as an ordered decree channel

- `candidate_id`: S97-CAND-06
- `ayah_range`: 97:1-4
- `seed_type`: verified composite
- `seed`: repeated `ق د ر` plus `بإذن ربهم من كل أمر`
- `generating_set`: `(E: ق د ر B005 تقدير الأمر بالنظر والتهيئة والإحكام)`, `(E: ق د ر B001 مقدار وحد وأجل)`, `(E: ء ذ ن B004 permission/order)`, `(E: ر ب ب B001 Lord/master)`, `(E: ر ب ب B002 correction/care/completion)`, `(E: ك ل ل B003 all/encompassing)`, `(E: ء م ر B001 affair/matter)`, `(E: ء م ر B002 command/obligation)`.
- `selected_branches`: `ق د ر B001/B005/B006`, `ء ذ ن B004`, `ر ب ب B001/B002`, `ك ل ل B003`, `ء م ر B001/B002/B005`.
- `constructed_model`: The repeated `qadr` phrase is retrospectively specified as a system of measured, authorized matters. Permission links the descending agents to their Lord, and every affair/command enters under that measured authorization.
- `freeze_point`: after `من كل أمر` in 97:4.
- `predictions_at_freeze`: a non-chaotic outcome and temporal boundary.
- `unused_features_tested`: 97:5 peace until dawn.
- `corroborators`: `(C: س ل م B001/B004 confirms ordered non-harmful outcome)`, `(C: ط ل ع B001 + ف ج ر B002 close the measured interval)`, `(C: ء م ر B005 sign/appointed time weakly supports decreed timing)`, `(C: repeated ليلة القدر in 97:1-3 independently foregrounds qadr before amr appears)`.
- `constraints`: `(K: ء ذ ن B002 listening and B003 public call can support hearing/announcement but local syntax uses بإذن as authorization)`, `(K: ر ب ب many pastoral/material branches are remote and mostly terminate)`, `(K: ك ل ل branches about fatigue, kinship, chest, shortness, etc. do not fit `كل أمر`)`.
- `temporal_reactivation_notes`: Qadr occurs three times before `أمر` arrives. The later `كل أمر` reactivates qadr as not only worth but measured command/affair.
- `rival_models`: public-call model from `ء ذ ن B003` is possible but narrower; vessel/pot model from `ق د ر B007` is weak.
- `grade`: medium-strong
- `grade_rationale`: Strong lexical relation between measured decree, permission, lordship, totality, and affairs; less directly tied to the initial object pronoun.
- `source_queries_or_rows_used`: QAC rows for repeated `ق د ر`, `ء ذ ن/ر ب ب/ك ل ل/ء م ر`; attachments `97:1:a5`, `97:2:a5`, `97:3:a1`, `97:4:a4-a8`.

### S97-CAND-07: spirit/breath/relief as interior animation of the night

- `candidate_id`: S97-CAND-07
- `ayah_range`: 97:4-5
- `seed_type`: lexical
- `seed`: `97:4:3 ٱلرُّوحُ`, `ر و ح B001`
- `generating_set`: `(E: ر و ح B001 النفس والروح التي بها حياة البدن)`, `(E: attachment 97:4:a2 الروح conjoined co-subject with الملائكة)`, `(E: ن ز ل B001/B002 descent of co-subjects)`, `(E: فيها setting)`.
- `selected_branches`: `ر و ح B001`, with forks `B003 wind/breeze`, `B007 rest`, `B009 spaciousness`, `B010 active generosity`.
- `constructed_model`: The night is not an inert temporal container; a life/breath participant descends in it with the angels, and the result is relief/peace until dawn.
- `freeze_point`: after `والروح فيها`.
- `predictions_at_freeze`: later material should authorize the descent, specify scope, and result in rest/safety.
- `unused_features_tested`: `بإذن ربهم من كل أمر`, `سلام هي حتى مطلع الفجر`.
- `corroborators`: `(C: ء ذ ن B004 authorization)`, `(C: ر ب ب B001 source authority)`, `(C: س ل م B001 safety)`, `(C: ر و ح B007 rest as separate unused branch dimension after freeze)`, `(C: ر و ح B009 spaciousness weakly aligns with expansive peace)`.
- `constraints`: `(K: ر و ح B003 wind, B004 smell, B005 evening travel, B012 plant, B015 wine, B018 stallion are unsupported by syntax)`, `(K: الروح is co-subject, not the night itself)`.
- `temporal_reactivation_notes`: The spirit appears only after the night has been established and valued, giving a participant that animates the previously named interval.
- `rival_models`: breeze/rest model is a mild secondary scene; it should not replace `الروح` as the surface participant.
- `grade`: medium
- `grade_rationale`: Co-subject syntax is strong, but many root branches are remote and the main lexical branch is broad.
- `source_queries_or_rows_used`: QAC `ر و ح 97:4`, attachments `97:4:a2-a4`, furuq `ر و ح B001/B003/B007/B009/B010`.

### S97-CAND-08: enclosure/crown/cover around every matter

- `candidate_id`: S97-CAND-08
- `ayah_range`: 97:4
- `seed_type`: lexical
- `seed`: `97:4:8 كُلِّ`, especially `ك ل ل B003`
- `generating_set`: `(E: ك ل ل B003 الكل إحاطة وتماما)`, `(E: attachment 97:4:a7 كل governed by من as further complement to تنزل)`, `(E: attachment 97:4:a8 أمر completes كل)`, `(E: ء م ر B001 شأن/حال)`.
- `selected_branches`: `ك ل ل B003`; weak secondary `B005` surrounding/crown, `B006` covering.
- `constructed_model`: The descent is not partial. It is framed by an all-encompassing scope of matters/commands, as if the night's authorized channel surrounds the full set relevant to the decree.
- `freeze_point`: after `من كل أمر`.
- `predictions_at_freeze`: closure should name a whole-state outcome rather than a local incident.
- `unused_features_tested`: 97:5 `سلام هي` as whole-night predicate.
- `corroborators`: `(C: س ل م B001 as fronted predicate names the whole state)`, `(C: ق د ر B001 limit/measure prevents "all" from becoming unbounded chaos)`, `(C: ء ذ ن B004 permission limits totality under authorization)`.
- `constraints`: `(K: ك ل ل B001 fatigue, B002 dependency, B004 kinship, B007 chest, B008 shortness, B009 groups, B011 smile/lightning are not selected)`, `(K: attachment confidence for 97:4:a7 is medium, so the further complement to تنزل is somewhat less certain than the idafa itself)`.
- `temporal_reactivation_notes`: `كل أمر` arrives late and retroactively expands `qadr` from a named night to a comprehensive decree-event.
- `rival_models`: crown/cover imagery from `ك ل ل B005/B006` is a weak spatial fork: the night as encircled/covered by descending affairs.
- `grade`: medium
- `grade_rationale`: The local `كل` meaning is exact, but most branch richness remains remote and structural confidence is medium for attachment to the verb.
- `source_queries_or_rows_used`: QAC `ك ل ل/ء م ر 97:4`, attachments `97:4:a7-a8`, furuq `ك ل ل B003/B005/B006`, `ء م ر B001/B002`.

### S97-CAND-09: dawn as rupture/opening of the night-bound state

- `candidate_id`: S97-CAND-09
- `ayah_range`: 97:5
- `seed_type`: lexical
- `seed`: `97:5:5 ٱلْفَجْرِ`, especially `ف ج ر B001/B002`
- `generating_set`: `(E: ف ج ر B002 انبلاج الصبح من الليل)`, `(E: ط ل ع B001 طلوع النير وموضعه)`, `(E: attachment 97:5:a2 حتى endpoint)`, `(E: attachment 97:5:a3 الفجر idafa complement)`.
- `selected_branches`: `ف ج ر B002`; secondary `ف ج ر B001`; `ط ل ع B001/B002/B003`.
- `constructed_model`: The endpoint is not an arbitrary stop. Dawn emerges/opens from the night and terminates the peace interval.
- `freeze_point`: after 97:5.
- `predictions_at_freeze`: earlier night imagery should be reactivated; peace should be bounded by emergence from darkness.
- `unused_features_tested`: `ليلة` repetitions, qadr limit, descent in it.
- `corroborators`: `(C: ل ي ل B001 darkness as prior state)`, `(C: ق د ر B001 limit/أجل)`, `(C: س ل م B001 state lasting until endpoint)`, `(C: ن ز ل B001/B002 activity inside the night)`.
- `constraints`: `(K: ف ج ر B004 moral breach conflicts with سلام)`, `(K: ف ج ر B003 sudden mass arrival not locally supplied)`, `(K: ط ل ع B010 arrow and B011 vomit terminate)`.
- `temporal_reactivation_notes`: The final word `الفجر` forces a full replay from night to dawn, closing the temporal activation trajectory.
- `rival_models`: water rupture from `ف ج ر B001` is useful as geometric secondary image for opening but cannot become a water scene.
- `grade`: medium-strong
- `grade_rationale`: Strong closure fit and exact lexical endpoint, with secondary rupture image constrained.
- `source_queries_or_rows_used`: QAC `ط ل ع/ف ج ر 97:5`, attachments `97:5:a2-a3`, furuq `ط ل ع B001/B003`, `ف ج ر B001/B002`.

### S97-CAND-10: remote vessel/cooking/decoction fork

- `candidate_id`: S97-CAND-10
- `ayah_range`: 97:1-5
- `seed_type`: lexical weak fork
- `seed`: `ق د ر B007`
- `generating_set`: `(E: ق د ر B007 قدر الطبخ)`, `(E: ك ل ل B005 surrounding/covering weakly)`, `(E: ف ج ر B001 rupture/opening weakly)`.
- `selected_branches`: `ق د ر B007`; weak selected support `ك ل ل B005/B006`, `ف ج ر B001`.
- `constructed_model`: A remote image treats the "qadr" night as a vessel in which matters are prepared and then the dawn opens/releases the bounded condition.
- `freeze_point`: after attempting to connect 97:1 `ليلة القدر` with 97:4 `كل أمر` and 97:5 `الفجر`.
- `predictions_at_freeze`: would expect cooking, food, heat, liquid, vessel, contents, or serving vocabulary.
- `unused_features_tested`: all other S97 words and attachments.
- `corroborators`: `(C: ن ز ل B005 hospitality/nuzl very weakly supplies prepared provision)`, `(C: ر ب ب B006 thick syrup/repair by rubb weakly touches preparation)`.
- `constraints`: `(K: no cooking, pot, food, heat, or eating syntax)`, `(K: ق د ر appears in idafa with ليلة, not as concrete قدر)`, `(K: سلام and dawn endpoint point to temporal state, not vessel contents)`.
- `temporal_reactivation_notes`: The fork arises whenever `القدر` repeats, but later material does not feed it enough.
- `rival_models`: CAND-01 and CAND-06 are stronger qadr models.
- `grade`: weak
- `grade_rationale`: Branch is accepted but remote; it creates a vivid image with little passage-local role completion.
- `source_queries_or_rows_used`: furuq `ق د ر B007`, `ك ل ل B005/B006`, `ف ج ر B001`, QAC repeated `ق د ر`.

### S97-CAND-11: hospitality/provision descent fork

- `candidate_id`: S97-CAND-11
- `ayah_range`: 97:1-4
- `seed_type`: lexical weak fork
- `seed`: `ن ز ل B005`
- `generating_set`: `(E: ن ز ل B005 النزل المعد للنازل/الضيف)`, `(E: ن ز ل B002 إنزال النعم)`, `(E: ر ب ب B002 care/completion)`, `(E: خ ي ر B005 generosity/gift)`.
- `selected_branches`: `ن ز ل B005`, `خ ي ر B005`, `ر ب ب B002`, weak `ر و ح B010`.
- `constructed_model`: Descent may be heard as a prepared bestowal or provision for those receiving the night, with the night functioning like a hosted interval.
- `freeze_point`: after 97:3 before 97:4.
- `predictions_at_freeze`: would expect guests, receiving community, food/provision, or explicit gift imagery.
- `unused_features_tested`: 97:4 agents descend; 97:5 peace.
- `corroborators`: `(C: خ ي ر B005 generosity)`, `(C: ن ز ل B002 divine bestowal)`, `(C: سلام as beneficial outcome)`.
- `constraints`: `(K: no guest/food/serving roles)`, `(K: الملائكة والروح are descending subjects, not guests being hosted)`, `(K: the object pronoun in 97:1 remains unnamed)`.
- `temporal_reactivation_notes`: The fork is activated by first descent and later repeated descent but never becomes the dominant model.
- `rival_models`: measured descent model CAND-01.
- `grade`: weak
- `grade_rationale`: It has lexical hooks but insufficient local participant structure.
- `source_queries_or_rows_used`: furuq `ن ز ل B005/B002`, `خ ي ر B005`, `ر ب ب B002`, QAC `97:1/97:3/97:4`.

### S97-CAND-12: rejected martial/attack/hunt avalanche

- `candidate_id`: S97-CAND-12
- `ayah_range`: 97:2-5
- `seed_type`: lexical failed composite
- `seed`: remote branches `د ر ي B002/B003/B004`, `ش ه ر B003`, `ن ز ل B007`, `ء م ر B011`, `ط ل ع B010`
- `generating_set`: `(E: د ر ي B002 قصد/غزو)`, `(E: د ر ي B003 hidden hunting)`, `(E: د ر ي B004 pointed instrument)`, `(E: ش ه ر B003 unsheathed sword)`, `(E: ن ز ل B007 battle descent)`, `(E: ء م ر B011 spear-tip)`, `(E: ط ل ع B010 arrow overshoots)`.
- `selected_branches`: the listed remote branches were allowed to form one rival image.
- `constructed_model`: A night operation in which hidden agents descend with weapons/commands and dawn ends the encounter.
- `freeze_point`: after assembling the martial fork from remote branches.
- `predictions_at_freeze`: would require weapon, opponent, strike, target, conflict, harm, or victory syntax.
- `unused_features_tested`: all local attachments and 97:5.
- `corroborators`: none specific enough after freeze.
- `constraints`: `(K: سلام B001/B004 directly defeats harm/war)`, `(K: no object of attack or wounded target)`, `(K: تنزل subjects are الملائكة والروح, not combatants in a battle construction)`, `(K: بإذن ربهم من كل أمر supplies authorized command, not weaponization)`, `(K: comparative and knowledge constructions do not support combat)`.
- `temporal_reactivation_notes`: The avalanche can be triggered by darkness and descent but is stopped by the final peace-state and missing roles.
- `rival_models`: CAND-04 authorized descent explains the same words without violence.
- `grade`: unlikely
- `grade_rationale`: Several accepted remote branches can be connected, but independent passage constraints defeat the model.
- `source_queries_or_rows_used`: furuq branches listed; attachments `97:4:a1-a8`, `97:5:a1-a3`.

## Exhaustive lexical seed ledger

Legend: `C01` = S97-CAND-01, etc.; `local` = a small local image retained but not a synthesis unit; `dead` = no specific passage-local complement; `reject` = attempted fork defeated by constraints.

| Seed occurrence | Accepted branch pass results |
| --- | --- |
| `97:1:2 أَنزَلْ ن ز ل` | B001 -> C01; B002 -> C01/C04; B003 -> local rank/place, supports qadr-placement weakly; B004 -> C01/C06; B005 -> C11; B006 -> reject, no calamity frame; B007 -> C12 reject; B009 -> dead, no sexual/generative roles; B010 -> local single-descent occurrence, weak support for one-night boundedness. |
| `97:1:4 لَيْلَةِ ل ي ل` | B001 -> C01/C05/C09; B002 -> local night-action, supports descent happening in night; B003 -> C01 as "this entering night" temporal immediacy; B004 -> dead, name Layla/wine not passage-local. |
| `97:1:5 قَدْرِ ق د ر` | B001 -> C01/C06/C09; B003 -> C06 weak ability/authority via lordship; B004 -> local compression/tightening, weakly with one night > thousand months; B005 -> C01/C06; B006 -> C01 as fitting measure; B007 -> C10 weak. |
| `97:2:2 أَدْرَىٰ د ر ي` | B001 -> C02; B002 -> C12 reject; B003 -> C02 weak hiddenness fork, C12 reject; B004 -> C12 reject, weak "sharp disclosure" geometry only. |
| `97:2:4 لَيْلَةُ ل ي ل` | B001 -> C02 reactivated night; B002 -> local action-in-night; B003 -> C02/C01 immediacy; B004 -> dead. |
| `97:2:5 قَدْرِ ق د ر` | B001 -> C02/C06 as question about measured night; B003 -> local ability "what could make you know" weak; B004 -> weak compression; B005 -> C06; B006 -> C01; B007 -> C10 weak. |
| `97:3:1 لَيْلَةُ ل ي ل` | B001 -> C03/C05/C09; B002 -> local night-operation; B003 -> C03 one-night immediacy; B004 -> dead. |
| `97:3:2 قَدْرِ ق د ر` | B001 -> C03/C06; B003 -> C06 ability/authority weak; B004 -> C03 compression weak; B005 -> C06; B006 -> C01/C03; B007 -> C10 weak. |
| `97:3:3 خَيْرٌ خ ي ر` | B001 -> C03; B002 -> C03; B003 -> local choice/selection, supports superiority weakly; B005 -> C11 weak gift/generosity; B006 -> dead/reject, animal extraction has no complement. |
| `97:3:5 أَلْفِ ء ل ف` | B001 -> C03 exact count; B002 -> C03 secondary aggregation; B005 -> local familiarity/multiplicity, weak; B006 -> dead. |
| `97:3:6 شَهْرٍ ش ه ر` | B001 -> C03 exact month duration; B002 -> local manifestation/fame fork weak; B003 -> C12 reject. |
| `97:4:1 تَنَزَّلُ ن ز ل` | B001 -> C04; B002 -> C04; B003 -> local "station" supports placement weakly; B004 -> C04/C06 ordered placement; B005 -> C11 weak; B006 -> reject, no calamity; B007 -> C12 reject; B009 -> dead; B010 -> local repeated descent instance. |
| `97:4:2 ٱلْمَلَٰئِكَةُ م ل ك` | B001 -> C04 weak strength/cohesion of agents; B002 -> C04 weak possession/disposal; B003 -> C04/C06 weak dominion authority; B004 -> dead; B005 -> local "mainstay of matter" weak with أمر; B006 -> local path/median weak; B007 -> dead, water as mainstay not supplied; B008 -> local leading-agent image weak. B009 angel branch is review and excluded. |
| `97:4:3 ٱلرُّوحُ ر و ح` | B001 -> C07; B003 -> C07 weak breeze fork; B004 -> dead; B005 -> local evening/night timing weak; B006 -> local return-of-right weak with أمر; B007 -> C07/C05 rest; B008 -> local alternation weak; B009 -> C07 spaciousness weak; B010 -> C11 weak generosity; B011 -> local power weak; B012 -> dead; B014 -> dead; B015 -> dead; B016 -> reject, death conflicts with سلام; B017 -> local dawn/vegetal opening weak; B018 -> dead. |
| `97:4:5 إِذْنِ ء ذ ن` | B001 -> local ear/handle image weak, no complement; B002 -> local hearing/obedience support; B003 -> C02/C06 weak announcement/knowledge; B004 -> C04/C06 exact authorization. |
| `97:4:6 رَبِّ ر ب ب` | B001 -> C04/C06; B002 -> C06/C11 care/completion; B003 -> local knowledge support for C02 weak; B004 -> dead/weak groups; B005 -> dead; B006 -> C10 weak preparation; B007 -> local duration/abiding weak with night; B008 -> local cloud/rain descent weak; B009 -> dead; B010 -> dead; B011 -> C06 weak covenant; B012 -> dead; B013 -> dead; B014 -> dead; B015 -> dead; B016 -> local knot/need/benefaction weak; B017 -> dead. |
| `97:4:8 كُلِّ ك ل ل` | B001 -> dead/fatigue no fit; B002 -> dead/dependency; B003 -> C04/C06/C08 exact totality; B004 -> dead; B005 -> C08/C10 weak surrounding; B006 -> C08/C10 weak cover; B007 -> dead; B008 -> dead; B009 -> local groups weak with الملائكة; B011 -> local lightning/smile weak, not selected. |
| `97:4:9 أَمْرٍ ء م ر` | B001 -> C04/C06/C08; B002 -> C04/C06; B003 -> C06 weak authority; B004 -> C11 weak blessing/growth; B005 -> C06 weak sign/appointed time; B006 -> reject, monstrous matter unsupported; B007 -> local deliberation/tadbir weak; B008 -> dead; B009 -> dead; B011 -> C12 reject. |
| `97:5:1 سَلَامٌ س ل م` | B001 -> C05; B004 -> C05; B005 -> local prepayment/delivery weak; B006 -> local ladder/ascent weak, constrained; B007 -> dead stones; B008 -> dead tree/tanning; B009 -> reject, bitten/afflicted conflicts with سلام unless antiphrastic and unsupported; B010 -> dead joints; B011 -> dead bucket; B012 -> local delivery/handing-over weak; B013 -> reject captive. |
| `97:5:4 مَطْلَعِ ط ل ع` | B001 -> C05/C09; B002 -> C09 weak appearance; B003 -> C02/C09 weak disclosure; B004 -> C12 weak scouting reject; B005 -> local emergence/growth weak; B006 -> local ascent/lookout weak; B007 -> local fullness weak; B008 -> local longing/looking weak; B009 -> local visible form weak; B010 -> C12 reject; B011 -> dead; B012 -> dead. |
| `97:5:5 ٱلْفَجْرِ ف ج ر` | B001 -> C09 secondary rupture; B002 -> C05/C09 exact dawn; B003 -> reject/no sudden mass calamity; B004 -> reject, moral breach conflicts with سلام; B005 -> C11 weak generosity; B006 -> reject/no battle-days frame. |

## Constructional, morphosyntactic, and temporal seed ledger

| Seed | Result |
| --- | --- |
| `إِنَّا أَنزلناه` predication and object suffix | Supports C01: emphatic speaker + descent of unnamed object. Constraint: object not locally identified by QAC row. |
| `في ليلة` attachment | Supports C01/C05: temporal interior. Constraint: not a physical container. |
| `ليلة القدر` idafa in 97:1 | Supports C01/C06: night specified by qadr. |
| `وما أدراك` interrogative construction | Supports C02: knowledge threshold and reactivation. |
| Embedded `ما ليلة القدر` | Supports C02: phrase becomes content of inquiry. |
| Threefold `ليلة القدر` repetition | Supports C01/C02/C03/C06: activation -> question -> valuation. |
| `ليلة القدر خير` predication | Supports C03: night becomes valued subject. |
| Comparative `خير من ألف شهر` | Supports C03: one bounded night exceeds aggregated months. |
| Paired descents `أَنزلناه` / `تَنزل` | Supports C01/C04: initial descent is reactivated as populated descent. |
| `الملائكة` subject + `الروح` co-subject | Supports C04/C07 structurally; lexical angel branch excluded because review status. |
| `فيها` pronominal setting | Supports C01/C04: later descent happens in the already reactivated night. |
| `بإذن ربهم` | Supports C04/C06: authorized means/source. |
| `من كل أمر` | Supports C06/C08: comprehensive matter/command scope. |
| `سلام هي` fronted predicate | Supports C05: whole-night state. |
| `حتى مطلع الفجر` endpoint | Supports C05/C09: temporal closure. |
| Ayah boundary sequence 1->2->3->4->5 | Supports global trajectory: event -> epistemic reopening -> valuation -> mechanism -> closure. |

## Failed seed classes retained

- Proper-name branch `ل ي ل B004`: no local woman/wine/name role; dead for all three occurrences.
- Remote hunting/weapon branches `د ر ي B002/B003/B004`, `ش ه ر B003`, `ن ز ل B007`, `ء م ر B011`, `ط ل ع B010`: combined only in C12 and rejected.
- Concrete/material branches without local objects: `ق د ر B007`, `ك ل ل B005/B006`, `س ل م B007/B008/B010/B011`, many `ر ب ب` and `ر و ح` branches. Retained as weak or dead as ledgered.
- Negative/outcome branches contradicted by closure: `ن ز ل B006`, `ر و ح B016`, `س ل م B009/B013`, `ف ج ر B004`.
- Animal/plant/food branches mostly terminate unless weakly contributing to C10/C11; none become primary contextual meaning.

## Image Packet Catalog

IMAGE_ID: S97-IMG-01
Starting seed: `97:1:2 ن ز ل B002`
Complete image: A measured descent is placed inside a bounded dark interval; the interval is reactivated, valued, filled with authorized descending agents and matters, and closed at dawn.
Passage-order assembly: 97:1 descent/night/qadr -> 97:2 question -> 97:3 better than thousand months -> 97:4 descent in it by permission from every matter -> 97:5 peace until dawn.
Participants and roles: sender/source `إنا`/`ربهم`; delivered object `ه`; temporal locus `ليلة القدر`; descending subjects `الملائكة والروح`; authorization `إذن`; scope `كل أمر`; final state `سلام`; endpoint `مطلع الفجر`.
Operation / mechanism: authorized descent and placement.
Direction / force / medium: high-to-low descent into a temporal night.
Temporal development: opening night, reactivation, valuation, night-long activity, dawn endpoint.
Outcome / closure: peace until dawn.
Exact branch constituents: `ن ز ل B001/B002/B004`, `ل ي ل B001/B003`, `ق د ر B001/B005/B006`, `ء ذ ن B004`, `ر ب ب B001/B002`, `ك ل ل B003`, `ء م ر B001/B002`, `س ل م B001/B004`, `ط ل ع B001`, `ف ج ر B002`.
Unfilled roles, if any: antecedent of `ه` is not named inside the passage.
Status: COMPLETE.

IMAGE_ID: S97-IMG-02
Starting seed: `97:2:2 د ر ي B001`
Complete image: A heard phrase becomes an epistemic gap, then the following ayat answer by value, operation, and duration.
Passage-order assembly: phrase heard -> question asked -> comparative answer -> operational answer -> endpoint answer.
Participants and roles: addressee `ك`; unknown subject `ما`; phrase `ليلة القدر`; answer components.
Operation / mechanism: reactivation through interrogative suspense.
Direction / force / medium: cognitive movement from hearing to knowing.
Temporal development: after first exposure, the mind re-opens the phrase and waits for completion.
Outcome / closure: the night is known by its value, descent, permission, command scope, and peace until dawn.
Exact branch constituents: `د ر ي B001`, construction `ما أدراك`, repeated `ليلة القدر`, `خ ي ر B001/B002`, `ء ل ف B001`, `ش ه ر B001`, 97:4 and 97:5 structures.
Unfilled roles, if any: none for the cognitive model.
Status: COMPLETE.

IMAGE_ID: S97-IMG-03
Starting seed: `97:3:3 خ ي ر B001`
Complete image: One night outweighs a thousand counted months because its bounded interval is densely filled by authorized descent and command.
Passage-order assembly: repeated night -> comparative value -> thousand months -> operational density -> endpoint.
Participants and roles: night, counted months, descending agents, matters, peace.
Operation / mechanism: comparative compression.
Direction / force / medium: scale compression from many lunar units into one night.
Temporal development: single night exceeds long duration, then closes at dawn.
Outcome / closure: the high-value interval is finite and peaceful.
Exact branch constituents: `خ ي ر B001/B002`, `ء ل ف B001/B002`, `ش ه ر B001`, `ك ل ل B003`, `ء م ر B001/B002`, `ن ز ل B002`, `س ل م B001`, `ط ل ع B001`, `ف ج ر B002`.
Unfilled roles, if any: why exactly "thousand" rather than a generic many remains an intensifying count, not independently explained beyond `ء ل ف B001`.
Status: COMPLETE.

IMAGE_ID: S97-IMG-04
Starting seed: `97:4:1 ن ز ل B002`
Complete image: Angels and the Spirit descend inside the night by permission of their Lord with every matter.
Passage-order assembly: earlier descent -> later repeated descent -> subjects -> setting -> permission/source -> total command scope -> peace.
Participants and roles: descending subjects `الملائكة والروح`; source/authorizer `ربهم`; content/scope `كل أمر`; setting `فيها`.
Operation / mechanism: authorized procession/channel.
Direction / force / medium: descent into the night.
Temporal development: after qadr is named and valued, the night is shown active.
Outcome / closure: peace until dawn.
Exact branch constituents: `ن ز ل B001/B002/B004`, `ء ذ ن B004`, `ر ب ب B001/B002`, `ك ل ل B003`, `ء م ر B001/B002`, `ر و ح B001`.
Unfilled roles, if any: accepted furuq does not supply an accepted angel branch for `م ل ك`; use surface/attachment only.
Status: COMPLETE.

IMAGE_ID: S97-IMG-05
Starting seed: `97:5:1 س ل م B001`
Complete image: The night's result is safety/peace lasting until dawn rises.
Passage-order assembly: descent and decree -> authorized agents -> peace-state -> dawn endpoint.
Participants and roles: peace state, night pronoun `هي`, endpoint `مطلع الفجر`.
Operation / mechanism: closure by temporal limit.
Direction / force / medium: from dark night to emerging dawn.
Temporal development: the state persists through the night and ends with dawn.
Outcome / closure: complete.
Exact branch constituents: `س ل م B001/B004`, `ط ل ع B001`, `ف ج ر B002`, with secondary `ف ج ر B001`.
Unfilled roles, if any: none.
Status: COMPLETE.

IMAGE_ID: S97-IMG-06
Starting seed: `ق د ر B007`
Complete image: A weak vessel/preparation simulation in which the qadr-night contains prepared matters until dawn opens it.
Passage-order assembly: qadr repeated -> all matters -> dawn opening.
Participants and roles: vessel-like night, contents/matters, dawn opening.
Operation / mechanism: containment/preparation.
Direction / force / medium: inside a vessel-like interval.
Temporal development: preparation during night, opening at dawn.
Outcome / closure: weakly peace/release.
Exact branch constituents: `ق د ر B007`, weak `ك ل ل B005/B006`, `ف ج ر B001`, `ن ز ل B005`.
Unfilled roles, if any: no food, cooking, heat, or vessel nouns.
Status: FRAGMENT.

IMAGE_ID: S97-IMG-07
Starting seed: martial branches in C12
Complete image: A rejected night attack/hunt with descending armed agents.
Passage-order assembly: hidden knowledge -> sword/weapon/descent -> command -> endpoint.
Participants and roles: would require attacker, target, weapon, harm.
Operation / mechanism: attack/hunt.
Direction / force / medium: descent at night.
Temporal development: would culminate in conflict.
Outcome / closure: defeated by `سلام`.
Exact branch constituents: `د ر ي B002/B003/B004`, `ش ه ر B003`, `ن ز ل B007`, `ء م ر B011`, `ط ل ع B010`.
Unfilled roles, if any: no weapon event, no target, no harm.
Status: FRAGMENT.

## Exhaustiveness check

- Lexical seeds initiated: all 158 occurrence x accepted-branch seeds are represented in the seed ledger.
- Constructional seeds initiated: all attested major S97 constructions from attachment rows are represented.
- Branch separation: generating (`E`), corroborating (`C`), and constraining (`K`) evidence is separated in every candidate unit.
- Review/contaminated avoidance: only accepted branch rows are used as branch evidence; `م ل ك B009` is explicitly excluded because it is not accepted.
- Failed seeds retained: proper-name, animal, weapon, calamity, vessel, plant, body-part, and negative branches are marked as dead, weak, or rejected rather than silently dropped.
- Final output written after checking that the file contains root inventory, candidate units, lexical seed ledger, construction seed ledger, failed classes, image packets, and source rows used.
