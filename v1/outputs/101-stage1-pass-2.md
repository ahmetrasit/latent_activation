# S101 Stage 1 Pass 2: temporally conditioned reactivation

Assigned passage: S101.
Sacred Arabic source: `resources/quran/surah_101.json`.
Target output: `v1/outputs/101-stage1-pass-2.md`.

## Root Cause Of Pass 1 Limitation

The limitation came from two causes.

1. The prompt-named SQLite databases are zero-byte files in this workspace: `resources/qac.sqlite` and `resources/furuq_v4.sqlite` have no visible schema or tables. A literal SQLite-only run cannot retrieve QAC words/morphemes or furuq `branch_images`.
2. Pass 1 held the discovery in compressed working context instead of expanding every occurrence x branch pass into an auditable ledger. That made the sweep look selective even though the branch dossiers had been gathered.

For this restart I used the local exports that preserve the same required fields:

- `resources/qac_root_ayah.tsv` for rooted occurrence, lemma, word position, and ayah root sequence.
- `resources/v4_branches.tsv` for accepted `branch_id`, `branch_image_ar`, and `what_is_ar`.
- `resources/attachments.tsv` filtered to S101 for structural attachments.
- `resources/quran/surah_101.json` for sacred Arabic text and recitational order.

No translation evidence is used. The basmala is opening recitational context only and is not used to initiate lexical seeds.

## Sacred Text Sequence

0. `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`
1. `ٱلْقَارِعَةُ`
2. `مَا ٱلْقَارِعَةُ`
3. `وَمَآ أَدْرَىٰكَ مَا ٱلْقَارِعَةُ`
4. `يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ`
5. `وَتَكُونُ ٱلْجِبَالُ كَٱلْعِهْنِ ٱلْمَنفُوشِ`
6. `فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ`
7. `فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ`
8. `وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ`
9. `فَأُمُّهُۥ هَاوِيَةٌۭ`
10. `وَمَآ أَدْرَىٰكَ مَا هِيَهْ`
11. `نَارٌ حَامِيَةٌۢ`

## Rooted Occurrence Inventory And Lexical Seed Count

The restart begins at the first rooted word, `101:1:1 ٱلْقَارِعَةُ / ق ر ع`, and initiates every accepted branch of every rooted occurrence as its own seed pass. Repeated occurrences are kept separate when their temporal state differs.

| Occurrence | Root | Accepted branches | Lexical seed passes |
| --- | ---: | ---: | ---: |
| 101:1:1 `ٱلْقَارِعَةُ` | `ق ر ع` | 11 | 11 |
| 101:2:2 `ٱلْقَارِعَةُ` | `ق ر ع` | 11 | 11 |
| 101:3:2 `أَدْرَىٰ` | `د ر ي` | 4 | 4 |
| 101:3:4 `ٱلْقَارِعَةُ` | `ق ر ع` | 11 | 11 |
| 101:4:1 `يَوْمَ` | `ي و م` | 3 | 3 |
| 101:4:2 `يَكُونُ` | `ك و ن` | 6 | 6 |
| 101:4:3 `ٱلنَّاسُ` | `ن و س` | 2 | 2 |
| 101:4:5 `ٱلْفَرَاشِ` | `ف ر ش` | 12 | 12 |
| 101:4:6 `ٱلْمَبْثُوثِ` | `ب ث ث` | 3 | 3 |
| 101:5:2 `تَكُونُ` | `ك و ن` | 6 | 6 |
| 101:5:3 `ٱلْجِبَالُ` | `ج ب ل` | 12 | 12 |
| 101:5:4 `ٱلْعِهْنِ` | `ع ه ن` | 9 | 9 |
| 101:5:5 `ٱلْمَنفُوشِ` | `ن ف ش` | 3 | 3 |
| 101:6:4 `ثَقُلَتْ` | `ث ق ل` | 7 | 7 |
| 101:6:5 `مَوَٰزِينُهُۥ` | `و ز ن` | 8 | 8 |
| 101:7:4 `عِيشَةٍ` | `ع ي ش` | 2 | 2 |
| 101:7:5 `رَّاضِيَةٍ` | `ر ض و` | 7 | 7 |
| 101:8:4 `خَفَّتْ` | `خ ف ف` | 8 | 8 |
| 101:8:5 `مَوَٰزِينُهُۥ` | `و ز ن` | 8 | 8 |
| 101:9:2 `أُمُّهُۥ` | `ء م م` | 16 | 16 |
| 101:9:3 `هَاوِيَةٌ` | `ه و ي` | 9 | 9 |
| 101:10:3 `أَدْرَىٰ` | `د ر ي` | 4 | 4 |
| 101:11:1 `نَارٌ` | `ن و ر` | 8 | 8 |
| 101:11:2 `حَامِيَةٌ` | `ح م ي` | 12 | 12 |

Total lexical seed passes run: 182. This total is higher than the 142 distinct root-branch count because repeated occurrences of `ق ر ع`, `ك و ن`, `و ز ن`, and `د ر ي` are separate occurrence seeds.

Function words and pronouns such as `مَا`, `مَن`, `أَمَّا`, `فِي`, `كَـ`, `هُوَ`, `هِيَهْ`, and suffixes are treated as constructional or morphosyntactic seeds, not as ordinary lexical branch seeds.

## Branch Universe Read Continuously In Every Sweep

Each seed pass read the complete S101 root-dossier universe before selecting only passage-local expanding branches. The following compact catalogue identifies the accepted branches used, locally retained, or terminated.

- `ق ر ع`: B001 `ضرب شيء على شيء`; B002 `مقارعة ومضاربة`; B003 `ضراب الفحل وإنزاؤه`; B004 `اقتراع ومساهمة`; B006 `ردع يقرع السامع`; B007 `مقروع مختار وخيار`; B008 `قرع وانكشاف وخلو`; B009 `قرع اليقطين`; B010 `قارعة الطريق والدار`; B011 `قراع صلب ممسوح`; B012 `وعاء وجمع في مقرع`.
- `د ر ي`: B001 `الدراية والعلم`; B002 `قصد الشيء واعتماده`; B003 `الختل والاستتار للصيد`; B004 `المدرى والحد المحدد`.
- `ي و م`: B001 `وقت النهار المحدود`; B002 `مدة من الزمان`; B003 `كائنة اليوم وشدته`.
- `ك و ن`: B001 `وقوع الشيء وحضوره في زمان`; B002 `المكان والمكانة من الكون`; B003 `الكفالة والقيام على فلان`; B004 `الخضوع بالاستكانة`; B005 `الشيخ المنسوب إلى كُنْتُ`; B006 `حالة السوء بكينة`.
- `ن و س`: B001 `تذبذب الشيء المتدلّي`; B002 `سوق الإبل`.
- `ف ر ش`: B001 `تمهيد الشيء وبسطه`; B002 `المفروش والفراش والمتاع`; B004 `فرش الأنعام وصغارها`; B005 `الفراش الطائر والخفة`; B006 `رفرفة الطائر قرب الأرض`; B007 `افتراش الجسد والذراعين والموضع`; B008 `انبساط النبات والدق من الشجر`; B009 `أثر الماء اليابس أو القليل والفقاعات`; B010 `الرقاق والصفائح في العظم والحديد`; B011 `الشجة أو الطعنة تبلغ فراش العظم`; B012 `بسط اللسان والقول على الغير`; B015 `اتساع رجل البعير أو انبساط ظهره`.
- `ب ث ث`: B001 `تفريق الشيء وبثه`; B002 `إظهار المكتوم من النفس`; B003 `بثبثة الأمر وكشفه`.
- `ج ب ل`: B001 `تجمع مرتفع صلب`; B002 `كثرة كالجبل`; B003 `غلظ الخلقة والجسم`; B004 `خلقة مطبوعة`; B005 `صلابة توقف الحفر`; B006 `دخول الجبال`; B007 `إحكام النسج`; B008 `يبس الشجر`; B009 `عسر ومنع`; B010 `حمل على أمر`; B011 `مصادفة رمل عريض`; B012 `سادات كالجِبال`.
- `ع ه ن`: B001 `حاضر ميسور قريب`; B002 `لين وانكسار بلا بينونة`; B003 `صوف مصبوغ لين`; B004 `سعف يلي قلب النخلة`; B005 `عروق في رحم الناقة`; B006 `كلام مرسل بلا روية`; B007 `قيام حسن على المال`; B009 `وردة حمراء تسمى العهنة`; B010 `العهان أصل الكباسة`.
- `ن ف ش`: B001 `انتفاش الصوف والقطن`; B002 `انتفاش الشعر والريش والشيء الرخو`; B003 `انتشار الماشية ليلا بلا راع`.
- `ث ق ل`: B001 `الثقل ضد الخفة`; B004 `المثقال والوزن`; B005 `الثقل النفيس ذو القدر`; B006 `الثقلة والبطء`; B007 `إثقال الحمل`; B008 `امرأة ثقال`; B009 `ثقل السمع`.
- `و ز ن`: B001 `تقدير الشيء بوزن أو خرْص`; B002 `ميزان العدل والقسط`; B003 `موازنة ومحاذاة بين شيئين`; B004 `قيام ميزان النهار في وسطه`; B005 `رأي وزين ثابت راجح`; B006 `قصر موزون في الجارية أو المرأة`; B007 `قدر ومنزلة لها وزن`; B008 `شيء موزون مخلوق باعتدال`.
- `ع ي ش`: B001 `الحياة والعيشة`; B002 `المعيشة والمعاش`.
- `ر ض و`: B001 `الرضا خلاف السخط`; B002 `الرضوان والمرضاة اسم للرضا الكثير أو المطلوب`; B003 `المراضاة والتراضي رضا متبادل`; B004 `الإرضاء طلب رضا الغير وإزالة سخطه`; B005 `راضاني فرضوته غلبة في ذلك`; B006 `الرضي صفة للمطيع أو المحب أو الضامن`; B007 `رضوى ورضيا أعلام من المادة`.
- `خ ف ف`: B001 `خفة الثقل والحمل`; B002 `خفة السير والارتحال`; B003 `قلة المقدار والعدد`; B004 `خفة الطيش والاضطراب`; B005 `الاستخفاف إهانة واستهانة`; B006 `الخُفّ والقدم الملبوسة`; B007 `الخفوف للطاعة والانقياد`; B008 `الإبل على خف واحد`.
- `ء م م`: B001 `الأم الوالدة والمربية`; B002 `الأم أصلا وجامعا ومرجعا`; B003 `أم الدماغ وما يصيبه`; B004 `الأمة جماعة أو نوعا`; B005 `الأمة دينا وطريقة`; B006 `القامة والهيئة`; B007 `الأمي على الجبلة غير الكاتب`; B008 `الأمة حينا وزمانا`; B009 `الإمام ومن يقتدى به`; B010 `الإمة نعمة`; B011 `الأمام قدام وقربا`; B012 `القصد والتوجه والتيمم`; B013 `الأمم اليسير الحقير`; B014 `الأمة الوليدة`; B015 `الأمة أو الآمة عيبا`; B016 `أم حرف استفهام وإضراب`.
- `ه و ي`: B001 `الهَواء والخلاء`; B002 `هُوِيّ وسقوط إلى مهواة`; B003 `إهواء اليد والشيء`; B004 `الهَوَى وميل النفس`; B006 `هُوِيّ من الزمان أو الليل`; B007 `فغر الطعنة وخلو الجوف`; B008 `مضي سريع وترامي في السير`; B009 `مهاواة وملاجّة`; B010 `هواهي القول الباطل`.
- `ن و ر`: B001 `الضياء والإضاءة`; B002 `النار المتقدة والسمة بها`; B004 `نور الشجر وزهره`; B005 `المنار والمنارة الظاهرة`; B006 `النِّفار وقلة الثبات`; B007 `النائرة بين القوم`; B008 `دخان الوشم والكحل`; B009 `النُّورَة المطلية`.
- `ح م ي`: B001 `الحرارة والإحماء`; B002 `الدفع والحماية والمنع`; B003 `الحمية والأنفة والغضب`; B004 `قرابة الزوج`; B005 `الحام من الإبل`; B006 `الحمأة والطين الأسود`; B007 `الحُمَة وحرارة السم`; B008 `سورة الشراب والحدة`; B009 `لحمة الساق`; B010 `جانبا الحافر`; B011 `حجارة طي البئر`; B012 `اسوداد الليل والسحاب`.

Opening-context basmala branches were read only when needed as constraint/corroboration: `س م و` B005 naming/deliberate designation, `ء ل ه` B001/B002 divine worship/name, and `ر ح م` B001 mercy. They do not generate any S101 seed.

## Temporally Unfolding Activation

1. `ٱلْقَارِعَةُ`: the recitation opens with a bare substantivized striking/knocking event. No object is yet supplied, so the first state is impact without disclosed target.
2. `مَا ٱلْقَارِعَةُ`: the impact becomes a question. The earlier word is reactivated as unknown magnitude, not simply repeated.
3. `وَمَا أَدْرَىٰكَ مَا ٱلْقَارِعَةُ`: knowledge itself is placed under constraint. The third occurrence freezes a heightened expectation: what kind of strike exceeds ordinary knowing?
4. `يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ`: the answer begins as a temporal event. The first disclosed patient-field is people, not mountains: suspended humans become fluttering, scattered, lightweight bodies.
5. `وَتَكُونُ ٱلْجِبَالُ كَٱلْعِهْنِ ٱلْمَنفُوشِ`: the largest stable masses are then converted into loosened, carded wool. The strike reactivates as a force that defeats both human orientation and geological solidity.
6. `فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُ`: the image shifts from cosmic disruption to sorting by weight. Weight now becomes salvation criterion rather than merely physical mass.
7. `فَهُوَ فِى عِيشَةٍ رَّاضِيَةٍ`: the heavy side closes into a contained life-state that is satisfied/acceptable.
8. `وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُ`: the second conditional reverses the weight criterion. Lightness now aligns with instability already prepared by scattered moths and loosened wool.
9. `فَأُمُّهُ هَاوِيَةٌ`: the light-weighed one is assigned not to life-enclosure but to a mother/source/refuge that is a falling abyss.
10. `وَمَا أَدْرَىٰكَ مَا هِيَهْ`: the knowing formula returns, now pointing backward to `هَاوِيَةٌ`.
11. `نَارٌ حَامِيَةٌ`: the final disclosure names the abyss as heated fire. The surah closes once the second unknown is disclosed.

## Candidate Synthesis Units

### C101-01: the striking event produces a delayed disclosure of its target and force

- candidate_id: C101-01
- ayah_range: 101:1-5
- seed_type: lexical
- seed: `101:1:1 ٱلْقَارِعَةُ × ق ر ع B001 ضرب شيء على شيء`
- generating_set: `(E: ق ر ع B001 striking impact)`, `(E: ق ر ع B006 impact that arrests/strikes the hearer)`, `(E: د ر ي B001 knowing made problematic by formula)`, `(E: ي و م B003 severe event/day)`, `(E: ك و ن B001 occurrence in time)`
- selected_branches: QRY B001/B006; DRY B001; YWM B003; KWN B001; later expansions from FRSH/BTH/JBL/AHN/NFSH.
- constructed_model: a bare impact is sounded before any patient is supplied. Repetition turns the impact into an unknown event whose force is disclosed only when people and mountains are shown transformed.
- freeze_point: after 101:3, before `يوم يكون`.
- predictions_at_freeze: expected event-time; expected targets or affected fields; expected transformation caused by impact; expected a second disclosure if the unknown remains unresolved.
- unused_features_tested: 101:4 people as scattered moths; 101:5 mountains as carded wool; 101:10 repeated knowing formula; 101:11 final disclosure.
- corroborators: `(C: ي و م B003 kائنة اليوم وشدته)`, `(C: attachment 101:4:a1 يوم adverbial for يكون)`, `(C: ف ر ش B005 moth/lightness)`, `(C: ب ث ث B001 scattering)`, `(C: ج ب ل B001 hard elevated mass)`, `(C: ع ه ن B003 wool)`, `(C: ن ف ش B001 carding/loosening wool)`.
- constraints: `(K: no local weapon, striker, door, or literal object is supplied; القارعة remains an event-name)`, `(K: QRY B002 combat and B003 breeding die as literal paths)`.
- temporal_reactivation_notes: the first word is semantically underfilled; 101:4-5 retroactively supplies what the striking event does.
- rival_models: combat strike; public road/track from QRY B010; chosen-lot model from QRY B004.
- grade: strong
- grade_rationale: repetition, interrogative delay, event-time, and two independent transformation scenes all support a delayed-impact model.
- source_queries_or_rows_used: S101 qac-root rows for QRY, DRY, YWM, KWN, FRSH, BTH, JBL, AHN, NFSH; attachment rows 101:2:a1, 101:3:a1-a4, 101:4:a1-a6, 101:5:a1-a4.

### C101-02: human orientation collapses into light fluttering dispersal

- candidate_id: C101-02
- ayah_range: 101:4
- seed_type: lexical
- seed: `101:4:5 ٱلْفَرَاشِ × ف ر ش B005 الفراش الطائر والخفة`
- generating_set: `(E: ف ر ش B005 moth/light fluttering)`, `(E: ب ث ث B001 scattering/spreading)`, `(E: ن و س B001 dangling/trembling movement)`, `(E: ك و ن B001 becoming/occurrence)`
- selected_branches: FRSH B005/B006; BTH B001; NWS B001; KWN B001.
- constructed_model: people become like tiny light-seeking bodies, fluttering without ordered direction and dispersed across the event-field.
- freeze_point: after 101:4 before the mountain comparison.
- predictions_at_freeze: expected lightness or instability to recur; expected larger stable objects to be destabilized if the event is total; expected contrast with later weight criteria.
- unused_features_tested: 101:5 mountains/wool; 101:6 heavy scales; 101:8 light scales; 101:11 fire.
- corroborators: `(C: خ ف ف B001 lightness against weight)`, `(C: خ ف ف B004 agitation/طيش)`, `(C: ن و ر B002 fire with flickering motion, after freeze)`, `(C: attachment 101:4:a4 kana predicate makes the simile the state of الناس)`.
- constraints: `(K: الناس is rooted in the QAC export as ن و س, not ء ن س; the human-person sense is primary from surface and syntax, while NWS contributes motion only as a secondary simulation)`.
- temporal_reactivation_notes: `الفراش المبثوث` prepares the later opposition between lightness and heavy scales; final fire also reactivates moth/fire behavior without making it the primary meaning.
- rival_models: bedding/spreading from FRSH B001/B002; livestock from FRSH B004; speech-abuse from FRSH B012.
- grade: medium-strong
- grade_rationale: FRSH B005 and BTH B001 are direct lexical hits, with later light/fire reactivation; NWS is useful but secondary.
- source_queries_or_rows_used: S101 qac-root rows for NWS/FRSH/BTH/KHF/NWR; attachment rows 101:4:a2-a5.

### C101-03: geological solidity becomes carded colored wool

- candidate_id: C101-03
- ayah_range: 101:5
- seed_type: lexical
- seed: `101:5:3 ٱلْجِبَالُ × ج ب ل B001 تجمع مرتفع صلب`
- generating_set: `(E: ج ب ل B001 high solid mass)`, `(E: ج ب ل B005 solidity stopping digging)`, `(E: ع ه ن B003 colored soft wool)`, `(E: ن ف ش B001 carding/loosening wool)`
- selected_branches: JBL B001/B005; AHN B003; NFSH B001/B002; KWN B001.
- constructed_model: the hardest raised masses are converted into loosened fibrous material. The scene requires a force that does not merely move mountains but defeats their internal cohesion.
- freeze_point: after 101:5 before the scale division.
- predictions_at_freeze: expected a later sorting by density/weight; expected opposition between solidity and looseness; expected lightness to become dangerous.
- unused_features_tested: 101:6 heavy scales; 101:8 light scales; 101:9 falling abyss; prior 101:4 scattered moths.
- corroborators: `(C: ث ق ل B001 heaviness after freeze)`, `(C: خ ف ف B001 lightness after freeze)`, `(C: ف ر ش B005 previous light fluttering)`, `(C: attachment 101:5:a3 kana predicate forces the transformation image)`.
- constraints: `(K: ع ه ن B002 broken but not separated is less exact than B003+B001 because المنفوش requires loosened wool)`, `(K: JBL B002 crowd metaphor is not needed because الناس already occupy the human field)`.
- temporal_reactivation_notes: the mountain image expands the impact from social scattering to cosmic deconstruction, then the weighing section reuses mass/lightness as judgment.
- rival_models: mountain crowd; woven cloth from JBL B007; palm-sheath AHN B004.
- grade: strong
- grade_rationale: branch specificity is high: mountains, wool, and carding are all direct local matches and explain the sequence from disruption to weight.
- source_queries_or_rows_used: S101 qac-root rows for JBL/AHN/NFSH/THQL/KHF; attachment rows 101:5:a1-a4.

### C101-04: heavy scales resist the scattering field and enter satisfied life

- candidate_id: C101-04
- ayah_range: 101:6-7
- seed_type: lexical
- seed: `101:6:4 ثَقُلَتْ × ث ق ل B001 الثقل ضد الخفة`
- generating_set: `(E: ث ق ل B001 heaviness)`, `(E: ث ق ل B004 measured weight)`, `(E: و ز ن B001 weighing/estimating)`, `(E: و ز ن B002 scales of justice)`, `(E: ع ي ش B001 life/condition)`, `(E: ر ض و B001 satisfaction/acceptance)`
- selected_branches: THQL B001/B004/B005; WZN B001/B002/B007; AYSH B001/B002; RDW B001/B002.
- constructed_model: after the world has been made light and loose, genuine weight in the scales creates a stable destination: enclosed life that is satisfied or satisfying.
- freeze_point: after 101:7 before the contrastive `وأما`.
- predictions_at_freeze: expected a symmetric opposite; expected lightness to be bad; expected the same `موازين` to appear again; expected a non-life or anti-refuge outcome.
- unused_features_tested: 101:8 `خفت موازينه`; 101:9 `أمه هاوية`; 101:11 fire.
- corroborators: `(C: خ ف ف B001 direct opposite of ثقل)`, `(C: و ز ن B002 repeated scales)`, `(C: attachment 101:6:a2 subject موازينه of ثقلت)`, `(C: attachment 101:7:a2 في عيشة predicate enclosure)`.
- constraints: `(K: no deeds are named in S101; the scale model must stay at the level of weighed balances/outcome, not import an unstated object)`.
- temporal_reactivation_notes: heaviness reverses the prior light-scattering danger. Stable weight now becomes the criterion for escape from the event's dispersive force.
- rival_models: pregnancy burden THQL B007; sleepy heaviness THQL B006; social rank WZN B007 alone.
- grade: strong
- grade_rationale: THQL/WZN are direct local roots and the passage itself supplies the exact heavy/light binary with outcomes.
- source_queries_or_rows_used: S101 qac-root rows for THQL/WZN/AYSH/RDW/KHF/HWY/NWR/HMY; attachment rows 101:6:a1-a3, 101:7:a1-a3, 101:8:a1-a3.

### C101-05: light scales fall from measure into abyss-mother

- candidate_id: C101-05
- ayah_range: 101:8-11
- seed_type: lexical
- seed: `101:8:4 خَفَّتْ × خ ف ف B001 خفة الثقل والحمل`
- generating_set: `(E: خ ف ف B001 lightness against weight)`, `(E: و ز ن B001/B002 weighing/scales)`, `(E: ء م م B002 origin/refuge/gathering center)`, `(E: ه و ي B002 falling into a deep pit)`, `(E: ن و ر B002 fire)`, `(E: ح م ي B001 heat)`
- selected_branches: KHF B001/B003/B004; WZN B001/B002; AMM B001/B002; HWY B001/B002; NWR B002; HMY B001.
- constructed_model: deficient weight is assigned to a containing origin/refuge that is actually a plunging abyss; the delayed formula discloses that this abyss is heated fire.
- freeze_point: after 101:9 before 101:10-11.
- predictions_at_freeze: expected disclosure of what `هيه` is; expected downward/container image; expected destructive medium; expected closure after identity is supplied.
- unused_features_tested: 101:10 repeated `وما أدراك`; 101:11 `نار حامية`; earlier moth/fire hint; earlier lightness.
- corroborators: `(C: ه و ي B001 empty air/void)`, `(C: ن و ر B002 fire after freeze)`, `(C: ح م ي B001 intense heat after freeze)`, `(C: attachment 101:9:a2 هاوية predicate of أمه)`, `(C: attachment 101:10:a3 clausal complement)`, `(C: attachment 101:11:a1 حامية adjective of نار)`.
- constraints: `(K: أم here cannot be reduced to biological mother only; the predicate هاوية forces a figurative destination/refuge relation)`, `(K: AMM B003 brain-strike is a remote echo, not primary construction)`.
- temporal_reactivation_notes: the first knowing formula delayed the event; the second delays the identity of the abyss. The final line closes by naming the medium.
- rival_models: literal mother bereavement from AMM B001 plus HWY saying "his mother falls"; desire/whim from HWY B004; protected reserve from HMY B002.
- grade: strong
- grade_rationale: the exact roots for lightness, weighing, origin/refuge, falling abyss, fire, and heat converge in sequence.
- source_queries_or_rows_used: S101 qac-root rows for KHF/WZN/AMM/HWY/DRY/NWR/HMY; attachment rows 101:8:a2-a3, 101:9:a1-a2, 101:10:a1-a4, 101:11:a1.

### C101-06: the two `وما أدراك` formulas control disclosure gates

- candidate_id: C101-06
- ayah_range: 101:3, 101:10-11
- seed_type: constructional
- seed: repeated `وَمَا أَدْرَىٰكَ مَا ...`
- generating_set: `(E: د ر ي B001 knowledge)`, `(E: constructional clausal complement 101:3:a3)`, `(E: constructional clausal complement 101:10:a3)`, `(E: د ر ي B004 pointed/instrumental edge as weak secondary image of inquiry piercing toward identity)`
- selected_branches: DRY B001 primary; DRY B004 weak secondary; QRY B001; HWY B002; NWR B002; HMY B001.
- constructed_model: the surah uses two disclosure gates. The first withholds the nature of `القارعة`; the second withholds the nature of `هاوية`; both are answered by subsequent identity scenes.
- freeze_point: after the second formula at 101:10 before `نار حامية`.
- predictions_at_freeze: expected a concise identity answer; expected the second answer to complete `هيه`; expected closure after answer.
- unused_features_tested: 101:11 only; earlier answer block 101:4-5.
- corroborators: `(C: attachment 101:3:a3 embedded question is content made known)`, `(C: attachment 101:10:a3 embedded question is content made known)`, `(C: ن و ر B002 + ح م ي B001 exactly fill final identity)`.
- constraints: `(K: DRY B003 hunting/ambush and B002 raiding-intent do not fit the formula syntax)`.
- temporal_reactivation_notes: the formula at 101:10 reactivates the earlier epistemic delay and signals that the final line will disclose, not merely add detail.
- rival_models: inquiry as ambush/hunting; sharp comb/point from DRY B004.
- grade: medium-strong
- grade_rationale: constructional evidence is strong; lexical contribution from DRY beyond knowing is mostly weak.
- source_queries_or_rows_used: S101 qac-root rows for DRY/QRY/HWY/NWR/HMY; attachment rows 101:3:a1-a4, 101:10:a1-a4, 101:11:a1.

### C101-07: final fire reactivates moth-flight and lightness

- candidate_id: C101-07
- ayah_range: 101:4, 101:8-11
- seed_type: verified composite
- seed: `101:11:1 نَارٌ × ن و ر B002 النار المتقدة`
- generating_set: `(E: ن و ر B002 fire/flickering flame)`, `(E: ح م ي B001 heat)`, `(E: ف ر ش B005 moths seeking light/fire)`, `(E: خ ف ف B001 lightness)`, `(E: ه و ي B002 falling/downward movement)`
- selected_branches: NWR B002; HMY B001; FRSH B005; KHF B001; HWY B002.
- constructed_model: the final fire is not isolated. It retrospectively charges the early moth image: light, disordered bodies in the event-field anticipate a terminal fiery medium for the light-weighed side.
- freeze_point: after 101:11, then backward replay.
- predictions_at_freeze: backward prediction only: earlier passage should have primed fire-oriented light bodies or unstable movement.
- unused_features_tested: prior `الفراش`, `خفت`, `هاوية`.
- corroborators: `(C: ف ر ش B005 explicitly includes moths/light/fire behavior)`, `(C: خ ف ف B001 lightness in bad branch)`, `(C: ه و ي B002 descent into abyss)`.
- constraints: `(K: the primary meaning of الفراش in 101:4 remains the simile for people, not a literal statement that people are moths already in fire)`.
- temporal_reactivation_notes: 101:11 makes 101:4 newly meaningful by adding the fire pole that moth imagery can activate.
- rival_models: fire as simple punishment with no backward image; light/fire as unrelated closure.
- grade: medium
- grade_rationale: the backward reactivation is vivid and lexically supported, but it depends on secondary simulation rather than direct syntax.
- source_queries_or_rows_used: S101 qac-root rows for NWR/HMY/FRSH/KHF/HWY; attachment rows 101:4:a3-a5, 101:11:a1.

### C101-08: mother/refuge versus satisfied life as paired enclosures

- candidate_id: C101-08
- ayah_range: 101:7, 101:9
- seed_type: constructional
- seed: outcome predicates `فِي عِيشَةٍ راضية` and `فأمه هاوية`
- generating_set: `(E: ع ي ش B001 life/condition)`, `(E: ر ض و B001 acceptance/satisfaction)`, `(E: فِي containment construction 101:7:a1-a2)`, `(E: ء م م B002 origin/gathering/refuge)`, `(E: ه و ي B002 abyss/fall)`
- selected_branches: AYSH B001/B002; RDW B001/B002; AMM B001/B002; HWY B002.
- constructed_model: the two measured outcomes are both destinations/enclosures. Heavy scales put the person inside a satisfied life; light scales hand the person to an enclosing origin/refuge that is actually an abyss.
- freeze_point: after 101:9 before the final identity disclosure.
- predictions_at_freeze: expected the second enclosure to receive a destructive identity; expected first branch to remain stable and closed.
- unused_features_tested: 101:10-11.
- corroborators: `(C: ن و ر B002 and ح م ي B001 complete destructive enclosure)`, `(C: attachment 101:7:a2 predicate phrase for هو)`, `(C: attachment 101:9:a2 predicate of أمه)`.
- constraints: `(K: no explicit فِي governs هاوية, so enclosure there is from AMM/HWY image and predication, not the same syntax as 101:7)`.
- temporal_reactivation_notes: the stable outcome in 101:7 is inverted by the unstable abyss in 101:9, then disclosed at 101:11.
- rival_models: literal mother only; abstract "home" only; life as mere living without spatial containment.
- grade: medium-strong
- grade_rationale: the outcome-pair syntax and lexical destinations converge, though the two enclosures are not grammatically identical.
- source_queries_or_rows_used: S101 qac-root rows for AYSH/RDW/AMM/HWY/NWR/HMY; attachment rows 101:7:a1-a3, 101:9:a1-a2, 101:11:a1.

### C101-09: large and small bodies are both unmade before judgment

- candidate_id: C101-09
- ayah_range: 101:4-5
- seed_type: constructional
- seed: paired `يكون/تكون ... كـ` similes
- generating_set: `(E: ك و ن B001 occurrence/becoming)`, `(E: كـ simile complements 101:4:a3 and 101:5:a2)`, `(E: ف ر ش B005 light fluttering bodies)`, `(E: ب ث ث B001 dispersion)`, `(E: ج ب ل B001 solid elevation)`, `(E: ع ه ن B003 wool)`, `(E: ن ف ش B001 carding)`
- selected_branches: KWN B001; FRSH B005; BTH B001; JBL B001; AHN B003; NFSH B001.
- constructed_model: two transformation predicates display total destabilization: people lose order like dispersed moths; mountains lose solidity like teased wool.
- freeze_point: after 101:5 before `فأما`.
- predictions_at_freeze: expected a sorting principle after generalized destabilization; expected weight/mass to become decisive.
- unused_features_tested: 101:6-9.
- corroborators: `(C: ث ق ل B001 heavy criterion)`, `(C: خ ف ف B001 light criterion)`, `(C: و ز ن B002 scales of justice)`, `(C: sequence 101:4 before 101:5 moves small/mobile to massive/static)`.
- constraints: `(K: KWN B002 place/status can supplement but not replace the actual verbal predicate construction)`.
- temporal_reactivation_notes: the paired similes prepare the reader to interpret the scales not as ordinary measurement but as the sorting response to universal unmaking.
- rival_models: two independent ornaments; a purely naturalistic moth/wool comparison without weighing reactivation.
- grade: strong
- grade_rationale: syntax, order, and direct branch matches align tightly.
- source_queries_or_rows_used: S101 qac-root rows for KWN/FRSH/BTH/JBL/AHN/NFSH/THQL/KHF/WZN; attachment rows 101:4:a3-a5, 101:5:a2-a4.

### C101-10: Qur'anic impact as auditory knock and moral arrest

- candidate_id: C101-10
- ayah_range: 101:1-3, 101:6-11
- seed_type: lexical
- seed: `ق ر ع B006 ردع يقرع السامع`
- generating_set: `(E: ق ر ع B006 striking the hearer into arrest/reversal)`, `(E: د ر ي B001 knowing)`, `(E: ث ق ل B005 weighty value)`, `(E: و ز ن B002 justice scale)`, `(E: خ ف ف B005 contempt/light valuation as weak fork)`
- selected_branches: QRY B006; DRY B001; THQL B005; WZN B002/B007; KHF B005 weak.
- constructed_model: the opening impact is not only cosmic; it acts on the hearer as a moral arrest. The later scales specify what kind of arrest: value/weight is exposed, and lightness becomes ruin.
- freeze_point: after 101:3, with auditory/epistemic arrest frozen before outcome material.
- predictions_at_freeze: expected moral valuation or warning; expected an outcome split; expected the hearer-address formula to matter.
- unused_features_tested: 101:6-11.
- corroborators: `(C: ث ق ل B005 value/weight)`, `(C: و ز ن B002 justice)`, `(C: خ ف ف B005 contempt/light valuation as a secondary contrast)`, `(C: second-person suffix in أدرىك forces addressed hearer)`.
- constraints: `(K: the passage does not explicitly command repentance or counsel; arrest remains secondary simulation)`.
- temporal_reactivation_notes: the opening name strikes before explaining; the weighing section clarifies why the strike should arrest the hearer.
- rival_models: literal physical knock only; combat model QRY B002.
- grade: medium
- grade_rationale: QRY B006 fits the auditory force of the opening and addressed formula, but later moral valuation is inferential.
- source_queries_or_rows_used: S101 qac-root rows for QRY/DRY/THQL/WZN/KHF; attachment rows 101:3:a2-a3, 101:6:a2, 101:8:a2.

### C101-11: remote head/brain-strike echo terminates

- candidate_id: C101-11
- ayah_range: 101:1, 101:9
- seed_type: lexical
- seed: `ق ر ع B001/B011` with `ء م م B003 أم الدماغ وما يصيبه`
- generating_set: `(E: ق ر ع B001 striking)`, `(E: ء م م B003 brain/head mother as struck core)`
- selected_branches: QRY B001/B011; AMM B003; HWY B007 as remote opening/gaping wound.
- constructed_model: an impact reaches a head-core or inner mother. This is a remote anatomical echo, not a viable passage model.
- freeze_point: after testing 101:9.
- predictions_at_freeze: expected head, wound, explicit body, or instrument.
- unused_features_tested: all later words, especially `هاوية`, `نار`, `حامية`.
- corroborators: none strong.
- constraints: `(K: أمه is possessed predicate subject, not a head/brain term in local syntax)`, `(K: no body, wound, skull, or instrument role appears)`, `(K: هاوية and نار حامية pull toward abyss/fire, not head injury)`.
- temporal_reactivation_notes: the opening strike tempts this route, but the outcome syntax defeats it.
- rival_models: abyss-mother model C101-05.
- grade: unlikely
- grade_rationale: remote lexical compatibility is overwhelmed by syntax and later disclosure.
- source_queries_or_rows_used: S101 qac-root rows for QRY/AMM/HWY/NWR/HMY; attachment rows 101:9:a1-a2.

### C101-12: heat as protected boundary terminates against fire identity

- candidate_id: C101-12
- ayah_range: 101:11
- seed_type: lexical
- seed: `101:11:2 حَامِيَةٌ × ح م ي B002 الدفع والحماية والمنع`
- generating_set: `(E: ح م ي B002 protected/prohibited zone)`, `(E: ن و ر B002 fire)`
- selected_branches: HMY B002; NWR B002.
- constructed_model: the final fire might be imagined as a protected or prohibited boundary that cannot be approached.
- freeze_point: after 101:11.
- predictions_at_freeze: expected explicit prohibition, guarded reserve, or avoidance language.
- unused_features_tested: the whole passage backward.
- corroborators: `(C: HMY B002 contains "لا يقرب" only as lexical possibility)`.
- constraints: `(K: surface حامية is adjectival heat in local syntax, and HMY B001 directly fits)`, `(K: no guarding/prohibition construction appears)`.
- temporal_reactivation_notes: final heat closes the abyss identity, not a legal boundary.
- rival_models: C101-05 final heated abyss.
- grade: weak
- grade_rationale: the branch is real but locally displaced by the direct heat branch.
- source_queries_or_rows_used: S101 qac-root rows for HMY/NWR; attachment row 101:11:a1.

## Exhaustive Lexical Seed Ledger

Each entry below represents an occurrence x accepted branch seed pass. `C101-xx` means the seed converged into the candidate above. `Local` means a small local image was retained but did not reorganize the passage. `Terminated` means the seed was read against all dossiers and failed to find a passage-specific completion.

### 101:1:1 `ٱلْقَارِعَةُ`

- QRY B001 `ضرب شيء على شيء`: C101-01; impact event expands through people/mountains transformation.
- QRY B002 `مقارعة ومضاربة`: Terminated; no combat participants or weapons.
- QRY B003 `ضراب الفحل`: Terminated; no mating/breeding roles.
- QRY B004 `اقتراع ومساهمة`: Local weak; scales/portioning are later, but no lot-casting.
- QRY B006 `ردع يقرع السامع`: C101-10; auditory/moral arrest.
- QRY B007 `مقروع مختار وخيار`: Terminated; no chosen-best object.
- QRY B008 `انكشاف وخلو`: Local weak; later void in HWY, but no bald/exposed surface.
- QRY B009 `قرع اليقطين`: Terminated.
- QRY B010 `قارعة الطريق والدار`: Local weak; "event-road" possible only as remote scene.
- QRY B011 `قراع صلب ممسوح`: Local weak; supports hard impact against mountains only indirectly.
- QRY B012 `وعاء وجمع في مقرع`: Terminated; no container of dates/food.

### 101:2:2 `ٱلْقَارِعَةُ`

- QRY B001: C101-01; repetition reactivates the initial strike as questioned.
- QRY B002: Terminated.
- QRY B003: Terminated.
- QRY B004: Local weak; question does not become lottery.
- QRY B006: C101-10; interrogative increases hearer-arrest.
- QRY B007: Terminated.
- QRY B008: Local weak; unknownness creates disclosure gap, not lexical baldness.
- QRY B009: Terminated.
- QRY B010: Local weak; no road/yard syntax.
- QRY B011: Local weak; no direct hard object yet.
- QRY B012: Terminated.

### 101:3:2 `أَدْرَىٰ`

- DRY B001 `الدراية والعلم`: C101-06; formulaic knowledge gate.
- DRY B002 `قصد الشيء واعتماده`: Terminated; no raid/intent complement.
- DRY B003 `الختل والاستتار للصيد`: Terminated; no hunting concealment.
- DRY B004 `المدرى والحد المحدد`: Local weak; pointed inquiry image only.

### 101:3:4 `ٱلْقَارِعَةُ`

- QRY B001: C101-01; third mention freezes delayed-disclosure model.
- QRY B002: Terminated.
- QRY B003: Terminated.
- QRY B004: Local weak; no lots.
- QRY B006: C101-10.
- QRY B007: Terminated.
- QRY B008: Local weak; disclosure gap.
- QRY B009: Terminated.
- QRY B010: Local weak.
- QRY B011: Local weak.
- QRY B012: Terminated.

### 101:4:1 `يَوْمَ`

- YWM B001 `وقت النهار المحدود`: Local; supplies temporal frame but not full image.
- YWM B002 `مدة من الزمان`: Local; duration not emphasized.
- YWM B003 `كائنة اليوم وشدته`: C101-01; event-day matches delayed strike.

### 101:4:2 `يَكُونُ`

- KWN B001 `وقوع الشيء وحضوره في زمان`: C101-09; becoming/occurrence predicate.
- KWN B002 `المكان والمكانة`: Local; state/place nuance in predicates.
- KWN B003 `الكفالة`: Terminated.
- KWN B004 `الخضوع بالاستكانة`: Terminated; no submission syntax.
- KWN B005 `الشيخ المنسوب إلى كنت`: Terminated.
- KWN B006 `حالة السوء`: Local weak; bad state but no lexical need.

### 101:4:3 `ٱلنَّاسُ`

- NWS B001 `تذبذب الشيء المتدلي`: C101-02; secondary motion image for people in simile.
- NWS B002 `سوق الإبل`: Terminated; no herding.

### 101:4:5 `ٱلْفَرَاشِ`

- FRSH B001 `تمهيد وبسط`: Local weak; spread-out field but not exact.
- FRSH B002 `الفراش والمتاع`: Terminated; no bedding.
- FRSH B004 `فرش الأنعام وصغارها`: Terminated.
- FRSH B005 `الفراش الطائر والخفة`: C101-02 and C101-07.
- FRSH B006 `رفرفة الطائر قرب الأرض`: C101-02 local reinforcement.
- FRSH B007 `افتراش الجسد والذراعين`: Terminated.
- FRSH B008 `انبساط النبات والدق`: Local weak; dispersed smallness only.
- FRSH B009 `أثر الماء اليابس/فقاعات`: Terminated.
- FRSH B010 `رقاق العظم والحديد`: Terminated.
- FRSH B011 `الشجة تبلغ فراش العظم`: Terminated.
- FRSH B012 `بسط اللسان والقول`: Terminated.
- FRSH B015 `اتساع رجل البعير`: Terminated.

### 101:4:6 `ٱلْمَبْثُوثِ`

- BTH B001 `تفريق الشيء وبثه`: C101-02; direct modifier.
- BTH B002 `إظهار المكتوم من النفس`: Terminated; no grief/secret context.
- BTH B003 `بثبثة الأمر وكشفه`: Local weak; disclosure is elsewhere through DRY.

### 101:5:2 `تَكُونُ`

- KWN B001: C101-09; second becoming predicate.
- KWN B002: Local; state/place nuance.
- KWN B003: Terminated.
- KWN B004: Terminated.
- KWN B005: Terminated.
- KWN B006: Local weak.

### 101:5:3 `ٱلْجِبَالُ`

- JBL B001 `تجمع مرتفع صلب`: C101-03.
- JBL B002 `كثرة كالجبل`: Local weak; people already supplied.
- JBL B003 `غلظ الخلقة والجسم`: C101-03 support for mass.
- JBL B004 `خلقة مطبوعة`: Local weak; natural constitution undone.
- JBL B005 `صلابة توقف الحفر`: C101-03 support for defeated solidity.
- JBL B006 `دخول الجبال`: Terminated.
- JBL B007 `إحكام النسج`: Local weak; contrasts with wool loosened.
- JBL B008 `يبس الشجر`: Terminated.
- JBL B009 `عسر ومنع`: Local weak; hardness/resistance.
- JBL B010 `حمل على أمر`: Terminated.
- JBL B011 `مصادفة رمل عريض`: Terminated.
- JBL B012 `سادات كالجِبال`: Terminated.

### 101:5:4 `ٱلْعِهْنِ`

- AHN B001 `حاضر ميسور قريب`: Terminated.
- AHN B002 `لين وانكسار بلا بينونة`: Local; softness/breakage but less exact than wool.
- AHN B003 `صوف مصبوغ لين`: C101-03.
- AHN B004 `سعف يلي قلب النخلة`: Terminated.
- AHN B005 `عروق في رحم الناقة`: Terminated.
- AHN B006 `كلام مرسل بلا روية`: Terminated.
- AHN B007 `قيام حسن على المال`: Terminated.
- AHN B009 `وردة حمراء`: Terminated.
- AHN B010 `أصل الكباسة`: Terminated.

### 101:5:5 `ٱلْمَنفُوشِ`

- NFSH B001 `انتفاش الصوف والقطن`: C101-03.
- NFSH B002 `انتفاش الشعر والريش والرخو`: Local; supports looseness.
- NFSH B003 `انتشار الماشية ليلا بلا راع`: Local weak; wandering without keeper but no livestock.

### 101:6:4 `ثَقُلَتْ`

- THQL B001 `الثقل ضد الخفة`: C101-04.
- THQL B004 `المثقال والوزن`: C101-04.
- THQL B005 `الثقل النفيس ذو القدر`: C101-04/C101-10.
- THQL B006 `الثقلة والبطء`: Terminated; no sluggishness.
- THQL B007 `إثقال الحمل`: Local weak; no pregnancy roles.
- THQL B008 `امرأة ثقال`: Terminated.
- THQL B009 `ثقل السمع`: Local weak; hearing-arrest possible but not local.

### 101:6:5 `مَوَٰزِينُهُۥ`

- WZN B001 `تقدير الشيء بوزن`: C101-04.
- WZN B002 `ميزان العدل والقسط`: C101-04.
- WZN B003 `موازنة ومحاذاة`: Local; paired outcomes.
- WZN B004 `قيام ميزان النهار`: Terminated.
- WZN B005 `رأي وزين ثابت راجح`: Local weak; stable judgment.
- WZN B006 `قصر موزون`: Terminated.
- WZN B007 `قدر ومنزلة لها وزن`: C101-04/C101-10.
- WZN B008 `مخلوق باعتدال`: Local weak; balance/order.

### 101:7:4 `عِيشَةٍ`

- AYSH B001 `الحياة والعيشة`: C101-04/C101-08.
- AYSH B002 `المعيشة والمعاش`: C101-08 local support.

### 101:7:5 `رَّاضِيَةٍ`

- RDW B001 `الرضا خلاف السخط`: C101-04/C101-08.
- RDW B002 `الرضوان والمرضاة`: C101-04 support.
- RDW B003 `المراضاة والتراضي`: Local weak; no mutuality.
- RDW B004 `الإرضاء`: Local; satisfaction caused by outcome.
- RDW B005 `غلبة في المراضاة`: Terminated.
- RDW B006 `المطيع/المحب/الضامن`: Local weak.
- RDW B007 `رضوى جبل`: Terminated.

### 101:8:4 `خَفَّتْ`

- KHF B001 `خفة الثقل والحمل`: C101-05.
- KHF B002 `خفة السير والارتحال`: Local; downward/rapid motion later.
- KHF B003 `قلة المقدار والعدد`: C101-05 support.
- KHF B004 `خفة الطيش والاضطراب`: C101-02/C101-05 support.
- KHF B005 `الاستخفاف إهانة`: C101-10 weak valuation.
- KHF B006 `الخف والقدم`: Terminated.
- KHF B007 `الخفوف للطاعة`: Terminated.
- KHF B008 `الإبل على خف واحد`: Terminated.

### 101:8:5 `مَوَٰزِينُهُۥ`

- WZN B001: C101-05.
- WZN B002: C101-05.
- WZN B003: Local; balances paired against 101:6.
- WZN B004: Terminated.
- WZN B005: Local weak.
- WZN B006: Terminated.
- WZN B007: C101-05 support by loss of weight/value.
- WZN B008: Local weak.

### 101:9:2 `أُمُّهُۥ`

- AMM B001 `الأم الوالدة والمربية`: C101-05 rival literal mother; constrained.
- AMM B002 `الأم أصلا وجامعا ومرجعا`: C101-05/C101-08.
- AMM B003 `أم الدماغ`: C101-11 terminated echo.
- AMM B004 `الأمة جماعة`: Terminated.
- AMM B005 `الأمة دينا وطريقة`: Terminated.
- AMM B006 `القامة والهيئة`: Terminated.
- AMM B007 `الأمي غير الكاتب`: Terminated.
- AMM B008 `الأمة حينا`: Terminated.
- AMM B009 `الإمام ومن يقتدى به`: Terminated.
- AMM B010 `الإمة نعمة`: Terminated.
- AMM B011 `الأمام قدام`: Local weak; destination/front.
- AMM B012 `القصد والتوجه`: Local; directed destiny to abyss.
- AMM B013 `الأمم اليسير الحقير`: Local weak with lightness.
- AMM B014 `الأمة الوليدة`: Terminated.
- AMM B015 `العيب`: Terminated.
- AMM B016 `أم حرف استفهام`: Terminated; surface is noun with suffix.

### 101:9:3 `هَاوِيَةٌ`

- HWY B001 `الهواء والخلاء`: C101-05; abyss void support.
- HWY B002 `سقوط إلى مهواة`: C101-05.
- HWY B003 `إهواء اليد والشيء`: Local weak; casting down only by extension.
- HWY B004 `ميل النفس`: Terminated; no desire.
- HWY B006 `حين طويل`: Terminated.
- HWY B007 `فغر الطعنة وخلو الجوف`: C101-11 weak rival only.
- HWY B008 `مضي سريع وترامي`: Local; fall velocity.
- HWY B009 `مهاواة وملاجّة`: Terminated.
- HWY B010 `باطل القول`: Terminated.

### 101:10:3 `أَدْرَىٰ`

- DRY B001 `الدراية والعلم`: C101-06.
- DRY B002 `قصد واعتماد`: Terminated.
- DRY B003 `ختل الصيد`: Terminated.
- DRY B004 `المدرى والحد المحدد`: Local weak.

### 101:11:1 `نَارٌ`

- NWR B001 `الضياء والإضاءة`: C101-07 support.
- NWR B002 `النار المتقدة`: C101-05/C101-07.
- NWR B004 `نور الشجر وزهره`: Terminated.
- NWR B005 `المنار والمنارة`: Local weak; disclosure/visibility only.
- NWR B006 `النفار وقلة الثبات`: Local weak; prior moth instability.
- NWR B007 `النائرة بين القوم`: Terminated.
- NWR B008 `دخان الوشم والكحل`: Local weak; smoke/dark trace not local.
- NWR B009 `النورة المطلية`: Terminated.

### 101:11:2 `حَامِيَةٌ`

- HMY B001 `الحرارة والإحماء`: C101-05/C101-07.
- HMY B002 `الدفع والحماية والمنع`: C101-12 weak terminated fork.
- HMY B003 `الحمية والأنفة والغضب`: Local weak; wrath simulation only.
- HMY B004 `قرابة الزوج`: Terminated.
- HMY B005 `الحام من الإبل`: Terminated.
- HMY B006 `الحمأة والطين الأسود`: Local weak; dark pit but no mud.
- HMY B007 `حرارة السم`: Local weak; painful heat.
- HMY B008 `سورة الشراب والحدة`: Local weak; intensity.
- HMY B009 `لحمة الساق`: Terminated.
- HMY B010 `جانبا الحافر`: Terminated.
- HMY B011 `حجارة طي البئر`: Local weak; pit lining only, not local.
- HMY B012 `اسوداد الليل والسحاب`: Local weak; darkness of abyss, not primary.

## Constructional, Morphosyntactic, And Temporal Seeds

- CON-101-01 bare opening noun `ٱلْقَارِعَةُ`: C101-01; generates suspended event-name with no supplied predicate.
- CON-101-02 `مَا ٱلْقَارِعَةُ`: C101-01/C101-06; nominal predication marks unknown identity.
- CON-101-03 `وما أدراك ما القارعة`: C101-06; first disclosure gate.
- CON-101-04 `يوم يكون ...`: C101-01/C101-09; temporal answer construction.
- CON-101-05 `الناس كالفراش المبثوث`: C101-02; simile + adjective as transformation predicate.
- CON-101-06 `الجبال كالعهن المنفوش`: C101-03; second simile + adjective as transformation predicate.
- CON-101-07 paired `يكون/تكون`: C101-09; totalizing parallel transformation across humans and mountains.
- CON-101-08 `فأما من ثقلت موازينه`: C101-04; conditional-relative sorting seed.
- CON-101-09 `فهو في عيشة راضية`: C101-04/C101-08; contained satisfied outcome.
- CON-101-10 `وأما من خفت موازينه`: C101-05; contrastive conditional sorting seed.
- CON-101-11 `فأمه هاوية`: C101-05/C101-08; inverted refuge/destination predicate.
- CON-101-12 `وما أدراك ما هيه`: C101-06; second disclosure gate.
- CON-101-13 `نار حامية`: C101-05/C101-07; terminal identity closure.
- MORPH-101-01 repeated definite `ٱلْقَارِعَةُ`: C101-01; the named event is reactivated three times before explanation.
- MORPH-101-02 two possessive suffixes on `موازينه`: C101-04/C101-05; each outcome belongs to a person.
- TEMP-101-01 opening delay then event-time: C101-01; question precedes answer.
- TEMP-101-02 small mobile bodies before massive bodies: C101-09; field of disruption expands in scale.
- TEMP-101-03 heavy branch before light branch: C101-04/C101-05; stable rescue precedes unstable fall.
- TEMP-101-04 final identity after second formula: C101-06; closure occurs when `هيه` is named.

## Image Packet Catalog

### IMG-101-A

- Starting seed: `ق ر ع B001`.
- Complete image: a striking event whose target is disclosed only after interrogation.
- Passage-order assembly: 101:1 impact; 101:2-3 unknown; 101:4-5 transformed people/mountains.
- Participants and roles: striking event, hearer, event-day, people, mountains.
- Operation / mechanism: impact destabilizes and transforms.
- Direction / force / medium: external force expressed through scattering and loosening.
- Temporal development: delayed disclosure.
- Outcome / closure: becomes the premise for judgment by weight.
- Exact branch constituents: QRY B001/B006; DRY B001; YWM B003; KWN B001; FRSH B005; BTH B001; JBL B001; AHN B003; NFSH B001.
- Unfilled roles, if any: literal striker remains unfilled by design.
- Status: COMPLETE.

### IMG-101-B

- Starting seed: `ف ر ش B005`.
- Complete image: humans as light, fluttering, scattered bodies.
- Passage-order assembly: 101:4 then reactivated by 101:8 and 101:11.
- Participants and roles: people, moth-like simile, dispersion, fire.
- Operation / mechanism: loss of ordered movement and stable weight.
- Direction / force / medium: scattered motion toward fiery closure as secondary replay.
- Temporal development: first disclosed transformation, later backward fire reactivation.
- Outcome / closure: supports light-scale danger.
- Exact branch constituents: FRSH B005/B006; BTH B001; NWS B001; KHF B001/B004; NWR B002.
- Unfilled roles, if any: no literal flame at 101:4.
- Status: COMPLETE as secondary image.

### IMG-101-C

- Starting seed: `ج ب ل B001`.
- Complete image: hard mountains made into teased wool.
- Passage-order assembly: 101:5 then reactivated by 101:6-8 weight language.
- Participants and roles: mountains, wool, carding/loosening force.
- Operation / mechanism: solid mass loses cohesion.
- Direction / force / medium: hard-to-soft transformation.
- Temporal development: follows human dispersal and prepares scale criterion.
- Outcome / closure: weight/lightness become judgment axes.
- Exact branch constituents: JBL B001/B005; AHN B003; NFSH B001; THQL B001; KHF B001; WZN B002.
- Unfilled roles, if any: no visible carder named.
- Status: COMPLETE.

### IMG-101-D

- Starting seed: `ث ق ل B001` / `خ ف ف B001`.
- Complete image: scales sort stable weight from deficient lightness.
- Passage-order assembly: 101:6 heavy scales; 101:7 satisfied life; 101:8 light scales; 101:9 abyss.
- Participants and roles: weighed person, scales, heavy/light criteria, two destinations.
- Operation / mechanism: moral/existential sorting through weight.
- Direction / force / medium: heavy stabilizes; light falls.
- Temporal development: binary branch after cosmic unmaking.
- Outcome / closure: life versus abyss-fire.
- Exact branch constituents: THQL B001/B004/B005; WZN B001/B002/B007; KHF B001/B003; AYSH B001; RDW B001; AMM B002; HWY B002.
- Unfilled roles, if any: specific weighed deeds are not named in S101.
- Status: COMPLETE with noted constraint.

### IMG-101-E

- Starting seed: `ه و ي B002`.
- Complete image: an apparent mother/refuge is a falling abyss disclosed as heated fire.
- Passage-order assembly: 101:9 abyss-mother; 101:10 question; 101:11 fire/heat.
- Participants and roles: light-weighed person, mother/refuge, abyss, fire, heat.
- Operation / mechanism: false refuge becomes destructive descent.
- Direction / force / medium: downward into fiery heat.
- Temporal development: delayed identity disclosure.
- Outcome / closure: `نار حامية`.
- Exact branch constituents: AMM B002; HWY B001/B002; DRY B001; NWR B002; HMY B001.
- Unfilled roles, if any: no biological mother role survives as primary.
- Status: COMPLETE.

### IMG-101-F

- Starting seed: repeated `وما أدراك`.
- Complete image: two epistemic gates controlling disclosure.
- Passage-order assembly: 101:3 asks about event; 101:4-5 answers by scenes; 101:10 asks about abyss; 101:11 answers by identity.
- Participants and roles: addressee, unknown event, unknown abyss, final identity.
- Operation / mechanism: withholding then disclosure.
- Direction / force / medium: cognitive delay.
- Temporal development: formula repeats with narrower referent.
- Outcome / closure: second answer ends the surah.
- Exact branch constituents: DRY B001; QRY B001; HWY B002; NWR B002; HMY B001; attachment rows for clausal complements.
- Unfilled roles, if any: none.
- Status: COMPLETE.

## Final Self-Check For Exhaustion

- Sacred Arabic source used and no translation used: yes.
- Basmala treated as opening context only, with no seeds initiated: yes.
- First rooted word restarted: yes, `101:1:1 ٱلْقَارِعَةُ`.
- Every rooted occurrence received an occurrence-level seed pass: yes, 24 occurrence rows.
- Every accepted branch for those occurrences was initiated: yes, 182 occurrence x branch passes.
- Constructional, morphosyntactic, and temporal seeds were initiated separately: yes.
- Construction and corroboration are kept separate in candidate packets: yes.
- Failed, weak, and terminated branches are explicit in the ledger: yes.
- Potentially missing images checked after file creation: yes; the distinct image families are impact-disclosure, human scattering, mountain unweaving, weight sorting, abyss-fire, and epistemic gating. Remote head-strike and protected-boundary paths are marked weak/terminated rather than omitted.
