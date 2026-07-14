# S94 Stage 1 Pass 2: Temporally Conditioned Reactivation

## Correction Note

Root cause of the limited Pass 1 coverage: the first sweep privileged early high-yield images around `نشرح / صدرك / وضعنا / وزرك` and treated later roots mainly as corroborators. That collapsed the required singleton-seed procedure into a few composite image searches. A second practical cause was that the named SQLite files were absent in this checkout, while equivalent local TSV exports were available; the first pass used the fallback data but did not explicitly turn every accepted branch into its own seed.

This pass restarts at the first rooted word and treats every eligible rooted occurrence, accepted branch, repeated occurrence, and constructional seed as having received its own seed pass. Branches that did not produce passage-local role completion are retained in the audit ledger as terminated seeds.

## Source Scope

Assigned passage: S94, `resources/quran/surah_94.json`.

Opening context: basmala in `verse_0`; used only as opening-context corroboration/constraint, never as a seed.

Passage rooted sequence from local QAC export:

`94:1` `نشرح` ش ر ح, `صدرك` ص د ر  
`94:2` `وضعنا` و ض ع, `وزرك` و ز ر  
`94:3` `أنقض` ن ق ض, `ظهرك` ظ ه ر  
`94:4` `رفعنا` ر ف ع, `ذكرك` ذ ك ر  
`94:5` `العسر` ع س ر, `يسرا` ي س ر  
`94:6` `العسر` ع س ر, `يسرا` ي س ر  
`94:7` `فرغت` ف ر غ, `فانصب` ن ص ب  
`94:8` `ربك` ر ب ب, `فارغب` ر غ ب

Structural rows used: S94 attachment rows from `resources/attachments.tsv`, especially the direct-object attachments for `صدرك`, `وزرك`, `ظهرك`, `ذكرك`; `عن` as removal complement; `لك` as beneficiary complement; `مع العسر` fronted predicate; repeated `إن مع العسر يسرا`; `إذا` temporal condition; and `إلى ربك` fronted directional complement of `فارغب`.

Branch source used: uncontaminated accepted branch rows from local `resources/v4_branches.tsv`, restricted to the roots listed above plus basmala roots for opening-context only.

## Exhaustive Seed Ledger

Lexical branch seed count by passage root:

- ش ر ح: 5 branches.
- ص د ر: 6 branches.
- و ض ع: 13 branches.
- و ز ر: 7 branches.
- ن ق ض: 7 branches.
- ظ ه ر: 24 branches.
- ر ف ع: 12 branches.
- ذ ك ر: 7 branches.
- ع س ر: 12 branches at two occurrences, so occurrence-sensitive tests were run for 94:5 and 94:6.
- ي س ر: 11 branches at two occurrences, so occurrence-sensitive tests were run for 94:5 and 94:6.
- ف ر غ: 6 branches.
- ن ص ب: 10 branches.
- ر ب ب: 17 branches.
- ر غ ب: 4 branches.

Every branch below was initiated as a seed. `kept` means it generated or joined a candidate packet. `local` means it produced a local image only. `terminated` means no specific passage-local complement survived attachment, sequence, or role tests.

Explicit coverage manifest:

- ش ر ح: ش ر ح B001, ش ر ح B002, ش ر ح B004, ش ر ح B005, ش ر ح B006.
- ص د ر: ص د ر B001, ص د ر B002, ص د ر B003, ص د ر B004, ص د ر B005, ص د ر B006.
- و ض ع: و ض ع B001, و ض ع B002, و ض ع B003, و ض ع B004, و ض ع B005, و ض ع B006, و ض ع B007, و ض ع B008, و ض ع B009, و ض ع B010, و ض ع B011, و ض ع B012, و ض ع B013.
- و ز ر: و ز ر B001, و ز ر B002, و ز ر B003, و ز ر B004, و ز ر B005, و ز ر B006, و ز ر B007.
- ن ق ض: ن ق ض B001, ن ق ض B002, ن ق ض B003, ن ق ض B004, ن ق ض B005, ن ق ض B006, ن ق ض B007.
- ظ ه ر: ظ ه ر B001, ظ ه ر B002, ظ ه ر B003, ظ ه ر B004, ظ ه ر B005, ظ ه ر B006, ظ ه ر B007, ظ ه ر B008, ظ ه ر B009, ظ ه ر B010, ظ ه ر B011, ظ ه ر B012, ظ ه ر B013, ظ ه ر B014, ظ ه ر B015, ظ ه ر B016, ظ ه ر B017, ظ ه ر B018, ظ ه ر B019, ظ ه ر B020, ظ ه ر B021, ظ ه ر B022, ظ ه ر B023, ظ ه ر B024.
- ر ف ع: ر ف ع B001, ر ف ع B002, ر ف ع B003, ر ف ع B004, ر ف ع B005, ر ف ع B006, ر ف ع B007, ر ف ع B008, ر ف ع B009, ر ف ع B010, ر ف ع B011, ر ف ع B012.
- ذ ك ر: ذ ك ر B001, ذ ك ر B002, ذ ك ر B003, ذ ك ر B004, ذ ك ر B007, ذ ك ر B008, ذ ك ر B009.
- ع س ر: ع س ر B001, ع س ر B002, ع س ر B003, ع س ر B004, ع س ر B005, ع س ر B006, ع س ر B008, ع س ر B009, ع س ر B010, ع س ر B011, ع س ر B012, ع س ر B013.
- ي س ر: ي س ر B001, ي س ر B002, ي س ر B003, ي س ر B004, ي س ر B005, ي س ر B006, ي س ر B007, ي س ر B008, ي س ر B009, ي س ر B010, ي س ر B011.
- ف ر غ: ف ر غ B001, ف ر غ B002, ف ر غ B003, ف ر غ B004, ف ر غ B005, ف ر غ B006.
- ن ص ب: ن ص ب B001, ن ص ب B002, ن ص ب B003, ن ص ب B004, ن ص ب B005, ن ص ب B006, ن ص ب B007, ن ص ب B008, ن ص ب B009, ن ص ب B010.
- ر ب ب: ر ب ب B001, ر ب ب B002, ر ب ب B003, ر ب ب B004, ر ب ب B005, ر ب ب B006, ر ب ب B007, ر ب ب B008, ر ب ب B009, ر ب ب B010, ر ب ب B011, ر ب ب B012, ر ب ب B013, ر ب ب B014, ر ب ب B015, ر ب ب B016, ر ب ب B017.
- ر غ ب: ر غ ب B001, ر غ ب B002, ر غ ب B003, ر غ ب B004.

### ش ر ح at 94:1

- B001 `فتح المعنى وبيانه`: kept in CSU-01 as opening/clarification and reactivation of later `ذكر`.
- B002 `بسط اللحم وتقطيعه`: local in CSU-01B as spreading/opening a body surface; constrained by object `صدر`, not literal butchery.
- B004 `فتح جنسي وافتضاض`: terminated; no sexual participant or construction.
- B005 `انبساط الرغبة إلى الشيء`: kept weakly as a forward echo into `فارغب`; not the contextual meaning of `نشرح`.
- B006 `حراسة الشيء وحفظه`: terminated/local; no guard role except weak protection of chest after expansion.

### ص د ر at 94:1

- B001 `الصدر الجارحة`: kept in CSU-01 and CSU-02 as interior/front torso locus.
- B002 `المقدّم والأعلى والأول`: kept in CSU-01 as first/front opening and sequence initiation.
- B003 `الصُّدور عن المورد`: kept weakly as a completion/exit echo into `فرغت`.
- B004 `الأصل الذي تصدر عنه الأفعال`: kept as a medium conceptual source-point echo for later action.
- B005 `المصادرة على مال`: terminated; no seizure/financial construction.
- B006 `الطائفة من الشيء`: terminated; no partitive use.

### و ض ع at 94:2

- B001 `وضع الشيء في موضع أخفض أو مقرر`: kept in CSU-02/03 as lowering/removal.
- B002 `إلقاء الحمل بالولادة`: kept as weak fork CSU-02B/04B; only secondary image.
- B003 `حمل الدابة على العدو`: terminated; no travel-acceleration frame.
- B004 `حط رأس المال بالخسران`: local/terminated; downward loss is lexical but no trade frame.
- B005 `انخفاض المنزلة والتذلل`: kept as contrast with `رفعنا لك ذكرك`.
- B006 `أقوام أو أثقال موضوعة`: local; supports placed burdens weakly, no people-set frame.
- B007 `إقامة الإبل على الحمض`: terminated.
- B008 `وضع القطن في خياطة الثوب`: terminated.
- B009 `وضع المرأة خمارها`: terminated.
- B010 `وضع الوديعة`: terminated.
- B011 `مواضعة الأمر`: terminated.
- B012 `نقص الاستحكام`: weak constraint only; not enough local evidence.
- B013 `تطامن عنق البعير للركوب`: terminated; no mount/rider construction.

### و ز ر at 94:2

- B001 `الملجأ والجبل`: local fork; mountain/refuge interacts with burden/back but not direct object sense.
- B002 `الحمل الثقيل`: kept in CSU-02.
- B003 `أوزار الحرب`: terminated/local; no war apparatus supplied.
- B004 `الوزير الموازر`: kept weakly as helper-bearing-relief echo.
- B005 `إحراز الشيء والذهاب به`: local; removal can imply taking away, but syntax says burden removed from you.
- B006 `غلبة الإنسان`: terminated.
- B007 `اتزار الموزر`: terminated.

### ن ق ض at 94:3

- B001 `حل المبرم وإبطال بنائه`: kept as rival fork: burden threatens structural integrity.
- B002 `بعير أنهكته الأسفار`: local; exhaustion under journey-load echoes back-bearing but lacks animal frame.
- B003 `تفتح الأرض عن الكمأة`: weak local opening-from-pressure fork; not contextually primary.
- B004 `عودة الشيء بعد التئامه إلى الانفتاح`: kept as constraint/reactivation with `شرح`: opening can be relief or rupture.
- B005 `صرير المفاصل والظهر تحت الثقل`: kept strongly in CSU-02.
- B006 `نقر وزجر وأصوات الحيوان`: terminated; no animal-sound role.
- B007 `النقاض اسم نبات`: terminated.

### ظ ه ر at 94:3

- B001 `البروز والانكشاف`: kept in CSU-03 with public `ذكر`.
- B002 `الظهر وخلاف البطن`: kept in CSU-02.
- B003 `ظهر الأرض وظاهرها`: local; surface/upper face helps vertical imagery weakly.
- B004 `وقت الظهر`: terminated.
- B005 `الركاب والعدة المحمولة`: kept weakly in CSU-02 as load-bearing apparatus.
- B006 `التقوي بالظهر والعون`: kept in CSU-02 as support/relief role.
- B007 `العلو والغلبة`: kept as vertical contrast with `رفع`.
- B008 `الاطلاع والعثور`: weak/local with `شرح`/`ذكر`, no explicit knowledge object.
- B009 `العين الظاهرة`: terminated.
- B010 `ظِهار المرأة`: terminated.
- B011 `ريش الظهار`: terminated.
- B012 `جعله بظهره`: local contrast; burden was not left behind by the addressee but removed from him.
- B013 `ظاهر عنك العار`: local; `عنك` plus removal suggests nonattachment, but no shame lexeme.
- B014 `الظهرة متاع البيت`: terminated.
- B015 `طريق الظهر وظواهر البلد`: terminated.
- B016 `الأعوان والناصرون`: local with divine help, but not textually explicit.
- B017 `بين ظهرانيهم`: terminated.
- B018 `قلب الأمر ظهرا لبطن`: local; supports reversal image only.
- B019 `ظهر الغيب والقلب`: local with hidden remembrance; no explicit memorization.
- B020 `ظاهر بين الشيئين`: terminated.
- B021 `الاحتياط والاستيثاق`: terminated.
- B022 `التدابر بالظهور`: terminated.
- B023 `عن ظهر يد وغنى`: local with grace/gift, no explicit giving syntax.
- B024 `الافتخار به`: local with raised `ذكر`, but weaker than ذ ك ر B007.

### ر ف ع at 94:4

- B001 `إعلاء الشيء`: kept in CSU-03.
- B002 `علو القدر`: kept strongly in CSU-03.
- B003 `رفع السير`: local with later `فانصب`, no travel frame.
- B004 `التقريب والتقديم`: local with `إلى ربك`, but no court/presentation frame.
- B005 `إذاعة الخبر`: kept with `ذكر` public mention.
- B006 `رفع الزرع`: terminated.
- B007 `رفع اللبن في الضرع`: terminated.
- B008 `الرِفاعة للمرأة`: terminated.
- B009 `رِفاع القيد`: local weak; lifting restraint after burden, but no قيد.
- B010 `رِفاعة الصوت`: kept weakly with mention/renown.
- B011 `الإصعاد في البلاد`: local with vertical ascent only.
- B012 `الرفع في الإعراب`: terminated.

### ذ ك ر at 94:4

- B001 `الذكر خلاف الأنثى`: terminated.
- B002 `صلابة الذكر وحدته وشدته`: local/terminated; strength is not the mention object.
- B003 `استحضار الشيء بعد النسيان`: kept in CSU-03 as reactivation.
- B004 `جريان الذكر على اللسان`: kept in CSU-03.
- B007 `ذكر المرء شرف وصيت`: kept strongly in CSU-03.
- B008 `ذكر الحق صك ووثيقة`: terminated; no legal document role.
- B009 `الذكرى والتذكرة ما يذكّر`: kept in CSU-03/08 as memory trigger.

### ع س ر at 94:5 and 94:6

- B001 `الصعوبة والشدة`: kept strongly in CSU-04.
- B002 `ضيق ذات اليد`: kept locally as constricted resources within hardship.
- B003 `مطالبة المعسر`: local; pressure of demand, no creditor frame.
- B004 `الخلاف والالتواء والتعسير`: kept in CSU-04 as constriction/complication.
- B005 `الشمال والأعسر`: kept only as weak lateral rival to ي س ر B004; no direction markers.
- B006 `تعسر الولادة`: kept weakly in CSU-04B; birth image constrained.
- B008 `الركوب والأخذ قبل التهيئة`: local; premature load/discipline, no mount.
- B009 `رفع الذنب في العدو`: terminated.
- B010 `اليوم المشؤوم`: local but no day/time lexeme.
- B011 `التفرق والتتابع`: kept weakly with repeated ayat as successive occurrence, not primary.
- B012 `أعلام الجن والمواضع`: terminated.
- B013 `لعبة العسر`: terminated.

### ي س ر at 94:5 and 94:6

- B001 `انفتاح وسهولة بعد عسر`: kept strongly in CSU-04.
- B002 `قلة يسيرة`: local; ease may begin as a small amount, but not specified.
- B003 `سعة وغنى`: kept in CSU-04 as spacious provision.
- B004 `الجهة اليسرى واليد اليسرى`: weak rival with ع س ر B005; constrained by lack of directional contrast.
- B005 `خفة وانقياد في الحركة`: kept in CSU-04/06 as ease of movement after release.
- B006 `إدرار ونماء في الغنم`: terminated.
- B007 `قداح وقمار وتقسيم جزور`: terminated.
- B008 `خطوط منفصلة وعلامات في البدن`: terminated.
- B009 `فتل إلى أسفل وطعن حذاء الوجه`: terminated.
- B010 `موضع أو علم`: terminated.
- B011 `فتى يسمى يسارا`: terminated.

### ف ر غ at 94:7

- B001 `الخلو بعد الشغل`: kept strongly in CSU-06.
- B002 `الصب وإخلاء الوعاء`: kept in CSU-06 as emptying/evacuation image.
- B003 `السعة في الحركة والأثر`: kept weakly with post-hardship spacious action.
- B004 `الدم المهدور`: terminated.
- B005 `ماء الرجل`: terminated.
- B006 `القصد إلى الأمر`: kept in CSU-06/07 as turning intentionally to next task.

### ن ص ب at 94:7

- B001 `إقامة الشيء منتصبا بارزا`: kept in CSU-06.
- B002 `حجر منصوب للعبادة والذبح`: local/constraint; ritual standing not idolatrous because `إلى ربك` follows.
- B003 `علامة منصوبة للحد أو الحوض`: local; boundary marker after completion, no explicit boundary object.
- B004 `تعب وعناء وبلاء`: kept in CSU-06 as exertion after relief.
- B005 `حظ معين`: terminated/local; no share allocation.
- B006 `نصاب الشيء أصله ومقداره`: local; measure/fixed threshold possible but weak.
- B007 `نصب الكلمة في الإعراب`: terminated.
- B008 `مواجهة العداوة والحرب`: terminated; no enemy.
- B009 `غناء يرفع به الصوت`: local with raised ذكر, but no song frame.
- B010 `سير اليوم سيرا لينا`: local with ongoing work, no travel frame.

### ر ب ب at 94:8

- B001 `ربوبية وملك وسيادة`: kept strongly in CSU-07.
- B002 `إصلاح وتربية وإتمام`: kept strongly in CSU-07/08.
- B003 `علم رباني`: local; no explicit learned class.
- B004 `جماعات كثيرة`: terminated.
- B005 `ربيب وربيبة`: terminated.
- B006 `رُبّ خاثر وإصلاح به`: weak local repair image only.
- B007 `لزوم وإقامة ودوام`: kept in CSU-07 as stable endpoint.
- B008 `رباب السحاب`: local; nurturing/rain image weakly supports ease but no weather lexeme.
- B009 `حداثة/قرب ولادة`: weakly supports birth fork only.
- B010 `ربابة تجمع القداح`: terminated.
- B011 `عهد وميثاق`: local with devotional orientation, but no explicit covenant term.
- B012 `نبات`: terminated.
- B013 `ماء كثير`: local with ease/spaciousness, no water.
- B014 `قطيع`: terminated.
- B015 `حرف رب`: terminated.
- B016 `حاجة وعقدة ونعمة`: local; divine favor, no direct noun.
- B017 `رئيس الملاحين`: terminated.

### ر غ ب at 94:8

- B001 `توجه الرغبة إلى الشيء أو انصرافها عنه`: kept strongly in CSU-07, especially with `إلى`.
- B002 `سعة في الشيء وجوف واسع`: kept weakly as final spacious desire after chest expansion.
- B003 `نهم وشره في الأكل`: terminated; no eating frame.
- B004 `عطاء كثير مرغوب فيه`: local; object of desire could be divine gift, but not explicit.

## Candidate Synthesis Units

### CSU-01: Chest Opening As Interior Expansion And Interpretive Disclosure

- `candidate_id`: S94-CSU-01
- `ayah_range`: 94:1, reactivated by 94:4 and 94:7-8
- `seed_type`: lexical
- `seed`: 94:1 `نشرح`, ش ر ح B001
- `generating_set`: (E: ش ر ح B001 opening/clarification), (E: ص د ر B001 chest locus), (E: ص د ر B002 front/first locus)
- `selected_branches`: ش ر ح B001, B002, B005; ص د ر B001, B002, B003, B004; ذ ك ر B003/B004/B009 after freeze; ر غ ب B001/B002 after freeze
- `constructed_model`: The first cue opens the addressee's front/interior locus. The image is not a translation of `نشرح` as surgery; it is a secondary simulation of an interior space being opened, widened, and made interpretable.
- `freeze_point`: after `ألم نشرح لك صدرك`, before `وضعنا عنك وزرك`.
- `predictions_at_freeze`: an opened interior should either receive relief, disclosure, movement outward, or new directed capacity; the beneficiary pronoun predicts that the opening is for the addressee.
- `unused_features_tested`: burden removal, back under load, raised mention, hardship/ease repetition, completion followed by exertion, final directed desire.
- `corroborators`: (C: attachment row 94:1 a3, `صدرك` direct object of `نشرح`), (C: ذ ك ر B003/B009, later remembrance reactivates disclosure), (C: ذ ك ر B004/B007, opened interior becomes public mention), (C: ر غ ب B002, final spacious desire echoes widened chest), (C: basmala opening-context ر ح م B001, mercy frame fits beneficial opening).
- `constraints`: (K: ش ر ح B002 cannot become literal cutting because no flesh, knife, wound, or agent of dissection is supplied), (K: ش ر ح B004 sexual opening has no participant construction), (K: primary contextual proposition remains divine expansion/relief, not anatomical surgery).
- `temporal_reactivation_notes`: The first ayah leaves a opened-front/interior state active. Ayat 2-3 then explain why opening was needed: a load was compressing the back. Ayah 4 moves from interior/front to public mention. Ayah 8 closes with desire oriented from the opened interior toward `ربك`.
- `rival_models`: pure explanation/clarification only; anatomical cutting; expansive appetite/desire.
- `grade`: strong
- `grade_rationale`: Strong because object attachment, body locus, later load/back physiology, public mention, and final directed desire all independently fit an opened-capacity model. Remote branches are constrained.
- `source_queries_or_rows_used`: S94 qac root rows; ش ر ح and ص د ر branch dossiers; attachment rows 94:1 a2-a4.

### CSU-01B: Desire Expansion Fork From شرح To رغب

- `candidate_id`: S94-CSU-01B
- `ayah_range`: 94:1 and 94:8
- `seed_type`: lexical
- `seed`: ش ر ح B005
- `generating_set`: (E: ش ر ح B005 broad inclination/desire), (E: ر غ ب B001 directional desire)
- `constructed_model`: A weak but real fork: expansion of the chest creates an expanded field of رغبة that later receives a single approved direction, `إلى ربك`.
- `freeze_point`: after linking ش ر ح B005 to final ر غ ب B001.
- `predictions_at_freeze`: an expanded desire should be directed or constrained.
- `unused_features_tested`: `إلى ربك`, `فانصب`, repeated hardship/ease.
- `corroborators`: (C: attachment row 94:8 a1, `إلى ربك` is fronted direction), (C: ر ب ب B001/B002 supplies rightful endpoint and nurturer).
- `constraints`: (K: ش ر ح B005 is remote and not the ordinary sense of `نشرح`; no worldly object appears).
- `grade`: medium
- `grade_rationale`: Useful as temporal echo, not as governing primary model.
- `source_queries_or_rows_used`: ش ر ح, ر غ ب, ر ب ب branch dossiers; attachment row 94:8 a1.

### CSU-02: Load Removed From The Back That Was Creaking

- `candidate_id`: S94-CSU-02
- `ayah_range`: 94:2-3, reactivating 94:1
- `seed_type`: lexical
- `seed`: 94:2 `وضعنا`, و ض ع B001
- `generating_set`: (E: و ض ع B001 lowering/putting down), (E: و ز ر B002 heavy burden), (E: ن ق ض B005 creaking joints/back under load), (E: ظ ه ر B002 back/body side)
- `selected_branches`: و ض ع B001/B005; و ز ر B002/B004/B005; ن ق ض B001/B004/B005; ظ ه ر B002/B005/B006
- `constructed_model`: The passage constructs a physical relief scene: a heavy load belonging to the addressee is lowered away from him; that load had reached the back-support system and made it creak under pressure.
- `freeze_point`: after `الذي أنقض ظهرك`, before `ورفعنا لك ذكرك`.
- `predictions_at_freeze`: after downward removal from the back, a compensating upward or strengthening movement is expected; the burden should be linked to prior chest constriction and later ease.
- `unused_features_tested`: `رفعنا`, `ذكرك`, `العسر/يسر`, `فرغت/فانصب`, `إلى ربك`.
- `corroborators`: (C: attachment row 94:2 a1, `عنك` marks removal from the addressee), (C: attachment row 94:2 a2, `وزرك` is direct object removed), (C: attachment row 94:3 a2, `ظهرك` is object affected by `أنقض`), (C: ر ف ع B001/B002, vertical reversal after lowering), (C: ع س ر B001/B004, hardship as constrictive pressure), (C: ي س ر B001/B005, ease as release of motion), (C: ف ر غ B001/B002, later emptied state).
- `constraints`: (K: و ز ر B003 war equipment lacks war syntax), (K: و ز ر B001 refuge/mountain is lexically available but not the direct-object burden in this construction), (K: ن ق ض B006 animal sounds do not fit the human back object).
- `temporal_reactivation_notes`: Ayah 1 opens the chest; ayat 2-3 explain the force that made opening necessary. The hearer retrospectively recodes the chest expansion as relief from a load that had been carried on the back.
- `rival_models`: economic lowering/loss from و ض ع B004; birth-delivery from و ض ع B002; military equipment from و ز ر B003.
- `grade`: strong
- `grade_rationale`: Strong because the exact syntax supplies lowering/removal, burden, affected back, and creaking under load in sequence.
- `source_queries_or_rows_used`: branch dossiers for و ض ع, و ز ر, ن ق ض, ظ ه ر; attachment rows 94:2 a1-a3 and 94:3 a2-a3.

### CSU-02B: Birth/Delivery Relief Fork

- `candidate_id`: S94-CSU-02B
- `ayah_range`: 94:1-6
- `seed_type`: lexical/composite fork
- `seed`: و ض ع B002
- `generating_set`: (E: و ض ع B002 laying down a pregnancy/birth load), (E: ع س ر B006 difficult birth), (E: ي س ر B001 ease after difficulty), (E: ش ر ح B002 bodily opening, remote)
- `constructed_model`: A secondary childbirth-like simulation: an enclosed pressure condition opens, the load is laid down, difficulty gives way to ease.
- `freeze_point`: after testing `العسر/يسرا`.
- `predictions_at_freeze`: if this fork were strong, passage should include mother/child/womb or explicit birth participants.
- `unused_features_tested`: `صدر`, `ظهر`, `ذكر`, `فرغ`, `ربك`.
- `corroborators`: (C: ع س ر B006 difficult birth), (C: ي س ر B001 ease), (C: opening-context ر ح م B003 only as non-generating womb-context echo).
- `constraints`: (K: no mother, fetus, womb, child, or delivery syntax), (K: `وزر` is a burden belonging to the addressee, not a pregnancy noun), (K: object is chest/back not womb).
- `grade`: weak
- `grade_rationale`: Lexical affordances exist, but the passage constrains this to a subordinate image, not a stable synthesis.
- `source_queries_or_rows_used`: و ض ع, ع س ر, ي س ر, ش ر ح branch dossiers; basmala ر ح م opening-context.

### CSU-03: Downward Removal Followed By Upward Public Elevation

- `candidate_id`: S94-CSU-03
- `ayah_range`: 94:2-4
- `seed_type`: verified composite
- `seed`: lowering/raising sequence, و ض ع B001 + ر ف ع B001
- `generating_set`: (E: و ض ع B001 lowering), (E: ر ف ع B001 raising), (E: ر ف ع B002 elevation of rank), (E: ذ ك ر B004 mention on tongue), (E: ذ ك ر B007 renown/honor)
- `constructed_model`: The passage sets a vertical exchange: the burden is lowered away from the addressee and his mention is raised for him. The load leaves the body; the name/renown rises in the social-auditory field.
- `freeze_point`: after `ورفعنا لك ذكرك`.
- `predictions_at_freeze`: a shift from bodily relief to durable public or remembered honor; later repetition should stabilize confidence before command.
- `unused_features_tested`: hardship/ease doublet, completion/exertion, final Lordward direction.
- `corroborators`: (C: attachment row 94:4 a2, `ذكرك` direct object raised), (C: attachment rows 94:1/94:4, repeated `لك` beneficiary), (C: ذ ك ر B003/B009, memory/reactivation), (C: ر ف ع B005/B010, public report/voice), (C: ظ ه ر B001/B007, emergence/overcoming after hidden pressure).
- `constraints`: (K: ذ ك ر B001 male sex and B008 legal document have no fit), (K: ر ف ع B006/B007 agricultural/milk branches do not fit the object `ذكر`), (K: رفع is not generic optimism; it is attached to a specific raised object).
- `temporal_reactivation_notes`: The addressee moves from internal chest, to relieved back, to raised mention. The reciter hears a transition from inside body to outside reputation.
- `rival_models`: public-voice model using ر ف ع B005/B010; court-presentation model using ر ف ع B004; grammatical-raising model B012 rejected.
- `grade`: strong
- `grade_rationale`: Strong due to exact lowering/raising opposition, direct-object syntax, and convergent ذكر branches.
- `source_queries_or_rows_used`: و ض ع, ر ف ع, ذ ك ر, ظ ه ر branch dossiers; attachment rows 94:2 a1-a2 and 94:4 a1-a3.

### CSU-04: Hardship Containing Ease, Repeated To Stabilize Expectation

- `candidate_id`: S94-CSU-04
- `ayah_range`: 94:5-6
- `seed_type`: constructional/lexical
- `seed`: `مع العسر يسرا`
- `generating_set`: (E: ع س ر B001 difficulty/severity), (E: ي س ر B001 ease after difficulty), (E: construction `مع العسر` fronted predicate), (E: repetition 94:5→94:6)
- `selected_branches`: ع س ر B001/B002/B004/B006/B011; ي س ر B001/B002/B003/B005; lateral ع س ر B005 + ي س ر B004 as rejected rival
- `constructed_model`: Ease is not merely after hardship; it is presented as with hardship. The repeated formula turns a single relief claim into a stable rule: the constrictive condition carries an opening/ease within its company.
- `freeze_point`: after 94:6 repetition.
- `predictions_at_freeze`: after assurance, the passage should move to action rather than passive rest; the relieved addressee should re-enter purposeful exertion.
- `unused_features_tested`: `فإذا فرغت فانصب`, `وإلى ربك فارغب`.
- `corroborators`: (C: attachment rows 94:5 a1-a3 and 94:6 a1-a3, `مع العسر` is fronted predication and `يسرا` delayed governed element), (C: ي س ر B003 spaciousness/growth opposite ع س ر B002 narrowness), (C: ي س ر B005 light movement after difficulty), (C: sequence from body burden to hard/easy rule), (C: ف ر غ B001 and ن ص ب B004, later action after relief confirms ease is enabling, not final idleness).
- `constraints`: (K: lateral left/right branch pair ع س ر B005 + ي س ر B004 lacks directional markers), (K: gambling/partition branch ي س ر B007 has no evidence), (K: birth branch ع س ر B006 remains subordinate without birth roles).
- `temporal_reactivation_notes`: The doublet retroactively generalizes the first half of the surah. Chest expansion, burden lowering, and raised mention become instances of a broader rule: constriction is accompanied by opening.
- `rival_models`: strict sequential "after hardship"; lateral right/left model; resource poverty/wealth model from ع س ر B002 + ي س ر B003.
- `grade`: strong
- `grade_rationale`: Strong because lexical antonymy, syntax with `مع`, repetition, and the following action command all converge.
- `source_queries_or_rows_used`: ع س ر and ي س ر branch dossiers; attachment rows 94:5 a1-a3 and 94:6 a1-a3.

### CSU-04B: Narrow Resources To Spacious Provision

- `candidate_id`: S94-CSU-04B
- `ayah_range`: 94:5-6
- `seed_type`: lexical fork
- `seed`: ع س ر B002 + ي س ر B003
- `generating_set`: (E: ع س ر B002 narrow means), (E: ي س ر B003 spaciousness/wealth)
- `constructed_model`: Hardship is simulated as narrowness of means and ease as spacious provision.
- `freeze_point`: after second `يسرا`.
- `predictions_at_freeze`: if financial, there should be creditor, debt, or property signals.
- `corroborators`: (C: repeated formula), (C: prior load/removal can be resource-pressure analog).
- `constraints`: (K: no explicit money, debt, creditor, or payment), (K: ع س ر B003 creditor-demand remains unfilled).
- `grade`: medium
- `grade_rationale`: Strong lexical opposition but weaker passage specificity than CSU-04.
- `source_queries_or_rows_used`: ع س ر, ي س ر branch dossiers; attachment rows 94:5-6.

### CSU-05: Structural Integrity Restored Before Renewed Exertion

- `candidate_id`: S94-CSU-05
- `ayah_range`: 94:1-7
- `seed_type`: morphosyntactic/temporal
- `seed`: body sequence `صدر` → `وزر` → `ظهر` → `فرغت` → `فانصب`
- `generating_set`: (E: ص د ر B001 chest), (E: و ز ر B002 load), (E: ظ ه ر B002 back), (E: ن ق ض B005 creaking under load), (E: ف ر غ B001 emptied after work), (E: ن ص ب B001 stand upright), (E: ن ص ب B004 exertion)
- `constructed_model`: The body is first opened and unloaded; then, once empty/complete, it is told to stand/exert again. Relief is not cessation but restored capacity for upright labor.
- `freeze_point`: after `فإذا فرغت فانصب`.
- `predictions_at_freeze`: final action should receive a direction or object beyond bare toil.
- `unused_features_tested`: `وإلى ربك فارغب`.
- `corroborators`: (C: attachment row 94:7 a1, `إذا` frames completion condition), (C: ف ر غ B002 emptying vessel reactivates burden removal), (C: ن ص ب B001 uprightness counters back-collapse), (C: ن ص ب B004 exertion shows ease enabling work), (C: ر غ ب B001 supplies final direction).
- `constraints`: (K: ن ص ب B002 idol-stone is rejected by `إلى ربك`), (K: ن ص ب B008 war confrontation lacks enemy), (K: not a promise of no work; command requires exertion).
- `temporal_reactivation_notes`: `فرغت` reactivates `وضعنا عنك وزرك`: something has been emptied/cleared. `فانصب` reactivates `ظهرك`: the back that was creaking now stands upright for renewed effort.
- `rival_models`: ritual stone/altar; travel-singing or journey; grammatical نصب.
- `grade`: medium-strong
- `grade_rationale`: Good role completion and temporal fit, though `نصب` has competing senses and the command is compact.
- `source_queries_or_rows_used`: ف ر غ and ن ص ب branch dossiers; attachment row 94:7 a1.

### CSU-06: Emptying As Completion Then Directed Reoccupation

- `candidate_id`: S94-CSU-06
- `ayah_range`: 94:7-8
- `seed_type`: lexical/constructional
- `seed`: ف ر غ B001
- `generating_set`: (E: ف ر غ B001 free/empty after occupation), (E: ف ر غ B006 turn deliberately to an affair), (E: ن ص ب B004 exertion), (E: ر غ ب B001 directional desire), (E: ر ب ب B001 Lord/master)
- `constructed_model`: Completion is an interval, not closure. When one occupation has been emptied, the addressee is to enter upright exertion and direct desire toward the Lord.
- `freeze_point`: after `وإلى ربك فارغب`.
- `predictions_at_freeze`: final closure should identify a stable endpoint/source.
- `unused_features_tested`: basmala context and ر ب ب B002/B007.
- `corroborators`: (C: attachment row 94:8 a1, `إلى ربك` fronted directional complement), (C: ر ب ب B002 nurture/completion: the endpoint is the one who repaired and brought to completion), (C: ر ب ب B007 staying/duration: desire stabilizes rather than disperses), (C: opening-context ء ل ه B001 worship and ر ح م B001 mercy).
- `constraints`: (K: desire is not open-ended appetite; `إلى ربك` constrains it), (K: ر غ ب B003 eating appetite fails), (K: ر غ ب B004 gift-desire remains implicit).
- `temporal_reactivation_notes`: The surah closes by preventing the ease/relief model from terminating in self-contained rest. Cleared capacity is reoriented.
- `rival_models`: mere leisure after completion; appetite/gift model; ritual-stone model from ن ص ب B002.
- `grade`: strong
- `grade_rationale`: Strong syntax and sequence: temporal condition, command, fronted direction, final divine endpoint.
- `source_queries_or_rows_used`: ف ر غ, ن ص ب, ر ب ب, ر غ ب branch dossiers; attachment rows 94:7 a1 and 94:8 a1-a2.

### CSU-07: Lord As Repairing Source And Final Direction

- `candidate_id`: S94-CSU-07
- `ayah_range`: 94:1-8
- `seed_type`: lexical
- `seed`: ر ب ب B002
- `generating_set`: (E: ر ب ب B002 repair, nurture, completion), (E: ر ب ب B001 Lord/master), (E: ر غ ب B001 direction of desire), (E: ش ر ح B001 beneficial opening), (E: و ض ع B001 relief), (E: ر ف ع B002 elevation)
- `constructed_model`: The final `ربك` retrospectively names the source who has been repairing the addressee through staged operations: opening the chest, lowering the load, raising mention, placing ease with hardship, and directing post-completion desire.
- `freeze_point`: after full passage closure.
- `predictions_at_freeze`: earlier benefits should show coherent care and ownership rather than random relief.
- `unused_features_tested`: basmala, repeated `نا` divine actor, repeated `لك/ك`.
- `corroborators`: (C: repeated first-person plural verbs `نشرح/وضعنا/رفعنا`), (C: repeated second-person suffixes `لك/صدرك/عنك/وزرك/ظهرك/ذكرك/ربك`), (C: opening-context ر ح م B001 mercy), (C: opening-context ء ل ه B001/B002 divine name and worship), (C: ر ب ب B007 endurance/stability at closure).
- `constraints`: (K: ر ب ب B004/B014 group/animal branches fail), (K: ر ب ب B015 particle `رب` is not the noun `ربك` in context), (K: source model must not erase distinct local mechanisms).
- `temporal_reactivation_notes`: Only at the final ayah does the passage name the relational endpoint explicitly. Earlier divine actions are then gathered under `ربك`, making the whole sequence a nurtured transition from constriction to directed service.
- `rival_models`: covenant from ر ب ب B011; rain/nurture from ر ب ب B008; thick syrup repair from ر ب ب B006.
- `grade`: medium-strong
- `grade_rationale`: Strong discourse closure and repeated pronoun pattern, but several `ربب` branches remain only analogical.
- `source_queries_or_rows_used`: ر ب ب and ر غ ب branch dossiers; basmala branch dossiers for opening-context only; S94 sacred text sequence.

### CSU-08: Memory, Mention, And Reactivation

- `candidate_id`: S94-CSU-08
- `ayah_range`: 94:1-8
- `seed_type`: lexical/temporal
- `seed`: ذ ك ر B009
- `generating_set`: (E: ذ ك ر B009 reminder/reactivation), (E: ذ ك ر B003 recollection), (E: ذ ك ر B004 uttered mention), (E: ر ف ع B005 publicizing), (E: ش ر ح B001 making hidden content clear)
- `constructed_model`: `ذكرك` is not only honor; it functions as a memory/reactivation hinge. The raised mention keeps the addressee present to others and makes the prior acts recitable as remembered favors.
- `freeze_point`: after `ورفعنا لك ذكرك`.
- `predictions_at_freeze`: later commands should rely on remembered prior favors for motivation and orientation.
- `unused_features_tested`: repeated assurance and final `ربك`.
- `corroborators`: (C: repetition 94:5-6 reinforces memory), (C: final `ربك` ties remembered favors to their source), (C: opening-context س م و B005, name as elevation/dalalah, only opening-context), (C: opening-context س م و B001 highness echoes raised mention).
- `constraints`: (K: legal-document branch ذ ك ر B008 unsupported), (K: masculine branch B001 unsupported), (K: public mention is a component, not a replacement for the body-relief sequence).
- `temporal_reactivation_notes`: The raised mention makes earlier private relief socially/audibly durable, then the repeated hard/easy formula gives the listener a remembered rule.
- `rival_models`: pure fame only; legal record; sharp/strong masculine branch.
- `grade`: medium-strong
- `grade_rationale`: Multiple ذكر and رفع branches converge, but it is a subsystem rather than the whole surah.
- `source_queries_or_rows_used`: ذ ك ر, ر ف ع, ش ر ح branch dossiers; opening-context س م و.

## Constructional Seeds

### C-01: Interrogative-Negative Opening `ألم نشرح`

- `seed_type`: morphosyntactic/temporal
- `generating_set`: (E: jussive/negative question structure), (E: ش ر ح B001), (E: attachment row 94:1 a1)
- `model`: The passage begins by reactivating an accomplished favor as if asking the listener to recognize it. This prepares later commands to rest on remembered prior relief.
- `freeze_point`: after 94:1.
- `tested`: past perfective-like divine acts in 94:2 and 94:4, final imperative sequence.
- `grade`: medium-strong

### C-02: Repeated Beneficiary `لك`

- `seed_type`: morphosyntactic
- `generating_set`: attachment rows 94:1 a2 and 94:4 a1
- `model`: Opening the chest and raising the mention are both marked as for the addressee; one is interior, one public.
- `corroborators`: second-person suffixes throughout, final `ربك`.
- `grade`: strong

### C-03: Removal Complement `عنك`

- `seed_type`: constructional
- `generating_set`: attachment row 94:2 a1
- `model`: `عن` fixes the burden as something displaced away from the addressee, constraining remote branches of و ز ر and و ض ع.
- `grade`: strong

### C-04: Relative Clause `الذي أنقض ظهرك`

- `seed_type`: constructional
- `generating_set`: attachment rows 94:3 a1-a2; ن ق ض B005; ظ ه ر B002
- `model`: The burden is not generic; it is identified by its effect on the back.
- `grade`: strong

### C-05: `إن مع العسر يسرا` Repetition

- `seed_type`: temporal/acoustic/constructional
- `generating_set`: repetition 94:5-6; ع س ر B001; ي س ر B001
- `model`: Repetition freezes the hard/easy rule and prevents the first half from being interpreted as a one-off event.
- `grade`: strong

### C-06: `إذا فرغت فانصب`

- `seed_type`: temporal construction
- `generating_set`: attachment row 94:7 a1; ف ر غ B001/B006; ن ص ب B001/B004
- `model`: Completion immediately predicts renewed upright exertion.
- `grade`: medium-strong

### C-07: Fronted `إلى ربك`

- `seed_type`: morphosyntactic/directional
- `generating_set`: attachment row 94:8 a1; ر غ ب B001; ر ب ب B001/B002
- `model`: Desire is constrained before the command is completed; the final endpoint controls the final motion.
- `grade`: strong

## Failed Or Terminated Seed Families

These branches were visited and initiated but did not form passage-local models:

- Sexual/body-opening branches: ش ر ح B004 and ظ ه ر B010 fail for lack of sexual/marital syntax.
- Trade/legal-document branches: ص د ر B005, و ض ع B004, ذ ك ر B008 fail or remain weak because no money, contract, or document appears.
- War branches: و ز ر B003, ن ص ب B008 fail for lack of enemy, weapon, battle, or hostile actor.
- Animal/travel branches: و ض ع B003, ظ ه ر B005 as literal mount, ر ف ع B003, ع س ر B008/B009, ن ص ب B010 mostly fail; some contribute weak movement pressure but not a full scene.
- Agriculture/weather/animal-product branches: ر ف ع B006/B007, ي س ر B006, ر ب ب B008/B012/B013 do not receive enough local roles.
- Grammar-only branches: ر ف ع B012, ن ص ب B007 fail as lexical synthesis; their forms are not the passage topic.
- Idolatry/stone branch: ن ص ب B002 is actively constrained by the following `إلى ربك`.
- Remote name/place/person branches: ع س ر B012, ي س ر B010/B011, ن ق ض B007, ر ب ب B014/B017 terminate.

## Image Packet Catalog

### IMAGE_ID: S94-IMG-01 Interior Opening

- Starting seed: ش ر ح B001 at `نشرح`.
- Complete image: an interior/front space is opened and made capacious.
- Passage-order assembly: `نشرح` → `صدرك` → burden removal explains pressure → final desire receives direction.
- Participants and roles: divine actor opens; addressee receives; chest/interior is locus.
- Operation / mechanism: opening, widening, clarifying.
- Direction / force / medium: inward/front bodily locus.
- Temporal development: opening first, pressure explanation second, direction last.
- Outcome / closure: capacity becomes desire toward `ربك`.
- Exact branch constituents: ش ر ح B001/B002/B005; ص د ر B001/B002; ر غ ب B001/B002.
- Unfilled roles: none for the secondary image; literal surgical roles absent by constraint.
- Status: COMPLETE.

### IMAGE_ID: S94-IMG-02 Burden Off The Back

- Starting seed: و ض ع B001 at `وضعنا`.
- Complete image: a heavy load is set down away from a back that was creaking.
- Passage-order assembly: opening chest → lowering burden → creaking back → raised mention.
- Participants and roles: divine remover; addressee; burden; back support.
- Operation / mechanism: lowering/removing from; relieving structural stress.
- Direction / force / medium: downward/outward from addressee.
- Temporal development: pressure is first relieved, then status is elevated.
- Outcome / closure: body no longer bears the crushing load.
- Exact branch constituents: و ض ع B001; و ز ر B002; ن ق ض B005; ظ ه ر B002/B006.
- Unfilled roles: exact nature of burden not lexically specified beyond load/sin-weight.
- Status: COMPLETE.

### IMAGE_ID: S94-IMG-03 Vertical Exchange

- Starting seed: ر ف ع B001 at `رفعنا`.
- Complete image: what weighed downward is removed; what belongs to the addressee is raised.
- Passage-order assembly: `وضعنا عنك وزرك` → `رفعنا لك ذكرك`.
- Participants and roles: divine actor; addressee; burden lowered; mention elevated.
- Operation / mechanism: lowering and lifting.
- Direction / force / medium: vertical contrast, body-to-public-auditory field.
- Temporal development: relief precedes elevation.
- Outcome / closure: public/honor field replaces crushing private load.
- Exact branch constituents: و ض ع B001/B005; ر ف ع B001/B002/B005/B010; ذ ك ر B004/B007/B009.
- Unfilled roles: audience of mention not named.
- Status: COMPLETE.

### IMAGE_ID: S94-IMG-04 Hardship With Ease

- Starting seed: construction `مع العسر يسرا`.
- Complete image: constriction contains or accompanies an opening.
- Passage-order assembly: after concrete relief/elevation, a repeated rule is stated.
- Participants and roles: hardship as constricting medium; ease as accompanying opening.
- Operation / mechanism: co-presence rather than simple replacement.
- Direction / force / medium: constriction versus spaciousness/lightness.
- Temporal development: repeated twice to stabilize expectation.
- Outcome / closure: enables command to exert.
- Exact branch constituents: ع س ر B001/B002/B004; ي س ر B001/B003/B005; repetition 94:5-6.
- Unfilled roles: exact external hardship not identified; generalized.
- Status: COMPLETE.

### IMAGE_ID: S94-IMG-05 Completion To Upright Exertion

- Starting seed: ف ر غ B001 at `فرغت`.
- Complete image: cleared capacity is immediately reoccupied by upright exertion.
- Passage-order assembly: `فإذا فرغت` → `فانصب` → `فارغب`.
- Participants and roles: addressee; completed task/emptied state; new exertion; final direction.
- Operation / mechanism: emptying, standing/straining, directing desire.
- Direction / force / medium: from emptied interval into vertical exertion and Lordward orientation.
- Temporal development: after completion, no idle closure; new directed action.
- Outcome / closure: desire fixed on `ربك`.
- Exact branch constituents: ف ر غ B001/B002/B006; ن ص ب B001/B004; ر غ ب B001; ر ب ب B001/B002.
- Unfilled roles: the specific completed task is not named.
- Status: COMPLETE.

### IMAGE_ID: S94-IMG-06 Birth/Delivery Fork

- Starting seed: و ض ع B002.
- Complete image: difficult pressure is released like delivery.
- Passage-order assembly: opening → setting down load → difficult/easy doublet.
- Participants and roles: pressure/load; opening; relief.
- Operation / mechanism: delivery, difficult birth, ease.
- Direction / force / medium: interior pressure outward.
- Temporal development: possible but not textually secured.
- Outcome / closure: constrained as secondary simulation only.
- Exact branch constituents: و ض ع B002; ع س ر B006; ي س ر B001; opening-context ر ح م B003.
- Unfilled roles: mother, child, womb, birth agent absent.
- Status: FRAGMENT.

## Consolidated Temporal Trajectory

The strongest passage-scale model is not one metaphor replacing the primary meaning. It is a sequence of reactivations:

1. `ألم نشرح لك صدرك`: an interior/front locus is opened for the addressee.
2. `ووضعنا عنك وزرك`: the reason for opening is clarified; a heavy load is removed away from him.
3. `الذي أنقض ظهرك`: the load is specified by bodily stress; the back had creaked under it.
4. `ورفعنا لك ذكرك`: downward relief is paired with upward elevation of mention.
5. `فإن مع العسر يسرا / إن مع العسر يسرا`: the concrete relief becomes a repeated rule of constriction accompanied by ease.
6. `فإذا فرغت فانصب`: ease is not idleness; completion becomes renewed upright exertion.
7. `وإلى ربك فارغب`: exertion and desire close on the repairing Lord, retrospectively naming the source of the whole transition.

Final consolidated grade: strong for the core load-relief/elevation/ease-action trajectory; medium-strong for the Lord-as-repairing-source closure; weak for childbirth and other remote branch forks.
