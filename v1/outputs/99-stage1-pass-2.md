# S99 Stage 1 Pass 2: temporally conditioned reactivation

Assigned passage: S99.
Sacred Arabic source: `resources/quran/surah_99.json`.

## Root cause of Pass 1 limitation

The earlier limitation had two causes.

1. The prompt-authorized SQLite files in this workspace are zero-byte files: `resources/qac.sqlite` and `resources/furuq_v4.sqlite` have no schema or tables. Direct queries against `qac_words`, `qac_morphemes`, and `branch_images` therefore cannot be executed here.
2. Pass 1 kept the discovery in compressed context instead of expanding an auditable occurrence-by-branch ledger. That made it look as if only a small number of words had been visited per finding.

For this Pass 2 restart I used the local exports that preserve the needed fields:

- `resources/qac_root_ayah.tsv` for rooted occurrence, lemma, word position, and ayah sequence.
- `resources/v4_branches.tsv` for accepted `branch_image_ar` and `what_is_ar`.
- `resources/attachments.tsv` filtered to S99 for structural attachments.
- `resources/quran/surah_99.json` for sacred Arabic text and order.

No translation evidence is used. The basmala is opening recitational context only and is not seeded.

## Sacred text sequence

0. `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`
1. `إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا`
2. `وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا`
3. `وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا`
4. `يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا`
5. `بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا`
6. `يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ`
7. `فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ`
8. `وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ`

## Rooted occurrence inventory and lexical seed count

The restart begins at the first rooted word, `99:1:2 زُلْزِلَتِ / ز ل ز ل`, and treats every accepted branch of every rooted occurrence as a seed pass. Occurrences with distinct local roles are separated.

| Occurrence | Root | Accepted branches | Lexical seed passes |
| --- | ---: | ---: | ---: |
| 99:1:2 `زُلْزِلَتِ` | `ز ل ز ل` | 3 | 3 |
| 99:1:3 `ٱلْأَرْضُ` | `ء ر ض` | 12 | 12 |
| 99:1:4 `زِلْزَالَهَا` | `ز ل ز ل` | 3 | 3 |
| 99:2:1 `أَخْرَجَتِ` | `خ ر ج` | 13 | 13 |
| 99:2:2 `ٱلْأَرْضُ` | `ء ر ض` | 12 | 12 |
| 99:2:3 `أَثْقَالَهَا` | `ث ق ل` | 7 | 7 |
| 99:3:1 `قَالَ` | `ق و ل` | 16 | 16 |
| 99:3:2 `ٱلْإِنسَٰنُ` | `ء ن س` | 6 | 6 |
| 99:4:1 `يَوْمَئِذٍ` | `ي و م` | 3 | 3 |
| 99:4:2 `تُحَدِّثُ` | `ح د ث` | 7 | 7 |
| 99:4:3 `أَخْبَارَهَا` | `خ ب ر` | 5 | 5 |
| 99:5:2 `رَبَّكَ` | `ر ب ب` | 17 | 17 |
| 99:5:3 `أَوْحَىٰ` | `و ح ي` | 10 | 10 |
| 99:6:1 `يَوْمَئِذٍ` | `ي و م` | 3 | 3 |
| 99:6:2 `يَصْدُرُ` | `ص د ر` | 6 | 6 |
| 99:6:3 `ٱلنَّاسُ` | `ن و س` / `ء ن س` contextual constraint | 2 | 2 |
| 99:6:4 `أَشْتَاتًا` | `ش ت ت` | 3 | 3 |
| 99:6:5 `لِّيُرَوْا` | `ر ء ي` | 13 | 13 |
| 99:6:6 `أَعْمَٰلَهُمْ` | `ع م ل` | 12 | 12 |
| 99:7:2 `يَعْمَلْ` | `ع م ل` | 12 | 12 |
| 99:7:3 `مِثْقَالَ` | `ث ق ل` | 7 | 7 |
| 99:7:4 `ذَرَّةٍ` | `ذ ر ر` | 4 | 4 |
| 99:7:5 `خَيْرًا` | `خ ي ر` | 5 | 5 |
| 99:7:6 `يَرَهُۥ` | `ر ء ي` | 13 | 13 |
| 99:8:2 `يَعْمَلْ` | `ع م ل` | 12 | 12 |
| 99:8:3 `مِثْقَالَ` | `ث ق ل` | 7 | 7 |
| 99:8:4 `ذَرَّةٍ` | `ذ ر ر` | 4 | 4 |
| 99:8:5 `شَرًّا` | `ش ر ر` | 11 | 11 |
| 99:8:6 `يَرَهُۥ` | `ر ء ي` | 13 | 13 |

Total lexical seed passes run: 241. `مَن` in 99:7 and 99:8 is treated as a conditional construction seed, not as a lexical root branch seed, because the QAC root-sequence export does not include it as a rooted lexical item.

## Branch universe read continuously in every sweep

Each seed pass read the complete S99 root-dossier universe before selecting only passage-local expanding branches. The branch image titles below identify the accepted branches used or rejected during the sweep.

- `ز ل ز ل`: B001 `اضطراب واهتزاز`; B002 `شدائد الدهر`; B003 `ماء صاف سائغ`.
- `ء ر ض`: B001 `السفل المقابل للسماء`; B002 `الأرض اللينة المنبتة`; B003 `الخليق بالخير كالأرض الأريضة`; B004 `ابن الأرض الغريب`; B005 `الإراض البساط الضخم`; B006 `لزوم الأرض والتثاقل إليها`; B007 `التعرض والتصدي`; B008 `الأَرْض الرعدة`; B009 `الأَرْض الزكام`; B010 `الأَرَضَة آكلة الخشب`; B011 `فساد القرحة بالمدة`; B012 `المأروض المخبول من أهل الأرض`.
- `خ ر ج`: B001 `النفاذ إلى خارج الشيء`; B002 `إخراج الشيء من خفائه`; B003 `مال يخرج على جهة معلومة`; B004 `قُرْح يخرج في الجسد`; B005 `ظهور السحاب وانكشاف السماء`; B006 `خروج عن الأصل أو الطاعة`; B007 `اختلاف لونين في الشيء`; B008 `خروج الخلقة عن نوعها`; B009 `خرج الوعاء ذو الأونين`; B010 `لعبة إخراج ما في اليد`; B011 `ألف الخروج بعد الصلة`; B012 `تخارج الشركاء في النصيب`; B013 `عنق خارج يغتال العنان`.
- `ث ق ل`: B001 `الثقل ضد الخفة`; B004 `المثقال والوزن`; B005 `الثقل النفيس ذو القدر`; B006 `الثقلة والبطء`; B007 `إثقال الحمل`; B008 `امرأة ثقال`; B009 `ثقل السمع`.
- `ق و ل`: B001 `إخراج القول بالنطق`; B002 `اللسان آلة القول`; B003 `كثرة القول في صاحبه`; B004 `القيل صاحب القول النافذ`; B005 `قول ما لم يكن أو نسبته`; B006 `اجترار القول إلى النفس`; B007 `القول الفاشي بين الناس`; B008 `عود القال لضرب القلة`; B009 `المقاولة في الأمر`; B010 `اقتالة الحكم على غيره`; B011 `قول يجري مجرى الظن`; B012 `قول في النفس لم يظهر`; B013 `القول اعتقاد ومذهب`; B014 `قول الشيء دلالته`; B015 `العناية الصادقة بالشيء`; B016 `قول الشيء حده`.
- `ء ن س`: B001 `ظهور الإنسان المخالف للتوحش والجن`; B002 `إيناس الشيء برؤية أو إحساس أو سماع`; B003 `الأنس الذي يزيل الوحشة`; B004 `الجانب الإنسي المقبل على الإنسان`; B005 `إنسان العين وصورة الإنسان في السواد`; B006 `ابن الإنس للنفس والصفوة`.
- `ي و م`: B001 `وقت النهار المحدود`; B002 `مدة من الزمان`; B003 `كائنة اليوم وشدته`.
- `ح د ث`: B001 `كون الشيء بعد أن لم يكن`; B002 `طراوة السن وقرب العهد`; B003 `كلام يتجدد خبرا وحديثا`; B004 `صيرورة المرء حديث الناس`; B005 `نازلة الدهر وحادثته`; B006 `إبداء الشيء وإظهاره`; B007 `جلاء السيف والقلب بالصقال`.
- `خ ب ر`: B001 `العلم بالخبر وباطن الأمر`; B002 `لين الأرض ومائها`; B003 `إصلاح الأرض بالمخابرة`; B004 `الغزر في المزادة والناقة`; B005 `اللِّين في النبات والوبر والزبد`.
- `ر ب ب`: B001 `ربوبية وملك وسيادة`; B002 `إصلاح وتربية وإتمام`; B003 `علم رباني`; B004 `ربة وجماعات كثيرة`; B005 `ربيب وربيبة ورابة`; B006 `رُبّ خاثر وإصلاح به`; B007 `لزوم وإقامة ودوام`; B008 `رباب السحاب`; B009 `شاة رُبّى وحداثة`; B010 `ربابة تجمع القداح`; B011 `ربابة عهد وميثاق`; B012 `ربة نبات`; B013 `ماء رَبَب كثير`; B014 `رَبْرَب قطيع`; B015 `حرف رب وربما`; B016 `رُبَى حاجة وعقدة ونعمة`; B017 `رباني الملاحين`.
- `و ح ي`: B001 `إلقاء علم في خفاء`; B002 `إشارة وإيماء`; B003 `كتابة ونقش`; B004 `نبأ وإلهام من الله`; B005 `صوت خفي`; B006 `سرعة وعجلة`; B007 `استيحاء طلبا`; B008 `ملك كنار`; B009 `نياحة وبكاء`; B010 `وحي في حجر`.
- `ص د ر`: B001 `الصدر الجارحة وما يتصل بها`; B002 `المقدّم والأعلى والأول`; B003 `الصُّدور عن المورد`; B004 `الأصل الذي تصدر عنه الأفعال`; B005 `المصادرة على مال`; B006 `الطائفة من الشيء`.
- `ن و س`: B001 `تذبذب الشيء المتدلّي`; B002 `سوق الإبل`.
- `ش ت ت`: B001 `التفرق والشتات`; B002 `الثغر الشتيت`; B003 `بُعد ما بين الشيئين`.
- `ر ء ي`: B001 `رؤية العين والبصيرة`; B002 `رأي القلب والتفكر`; B003 `الرؤيا في المنام`; B004 `تراء وتواجه`; B005 `رياء الناس`; B006 `مرأى ومنظر ومرآة`; B007 `ترية الحيض`; B008 `رئي من الجن`; B009 `الرئة وما يصيبها`; B010 `ظهور حمل الناقة أو الشاة`; B011 `راية منصوبة`; B012 `إراءة وإظهار`; B013 `أرأيتك للتنبيه والاستخبار`.
- `ع م ل`: B001 `الفعل المقصود والعمل`; B002 `إعمال الشيء واستعماله`; B003 `ولاية العمل والقيام عليه`; B004 `أجر العمل ورزق العامل`; B005 `المعاملة بين الناس`; B006 `العملة العاملون بالأيدي`; B007 `التعمل بمعنى التعني`; B008 `المطبوع على العمل`; B009 `عامل الرمح`; B010 `الجارحة العاملة`; B011 `الطريق المعمل`; B012 `بنو العمل من المشاة`.
- `ذ ر ر`: B001 `صغر الذر وانتشاره`; B002 `تفريق الحبوب والدقيق`; B003 `مسحوق الذريرة والذَّرور`; B004 `طلوع لطيف منتشر`.
- `خ ي ر`: B001 `الميل إلى الخير النافع`; B002 `فضل الصلاح والاصطفاء`; B003 `طلب الخير بالاختيار والاستخارة`; B005 `الكرم والهبة`; B006 `استدراج الحيوان من جحره`.
- `ش ر ر`: B001 `الشَّرّ والسوء`; B002 `نشر الشيء في الشمس ليجف`; B003 `شَرَر النار المتطاير`; B004 `الشَّرْشَرَة تقطيع ونفض`; B005 `الشواء المتقاطر دسمه`; B006 `الشراشر ذباذب وأثقال`; B007 `إلقاء الشراشر إلقاء النفس كلها`; B009 `الشَّرّان أذى كالبعوض`; B010 `شِرّة الشباب نشاط وحرص`; B011 `المشارة مخاصمة`; B012 `الشِّرْشِر نبت`.

## Temporally unfolding activation

1. `إذا زلزلت الأرض زلزالها`: the first activation is bodily and spatial instability. The repeated root creates a passive event plus its own cognate intensity. The object is not an abstract scene but `الأرض`, a lower, containing, possessed substrate.
2. `وأخرجت الأرض أثقالها`: the disturbed substrate becomes an active extractor. The surface/interior axis is now explicit: what was inside or hidden emerges as possessed burdens/weights.
3. `وقال الإنسان ما لها`: human perception enters after the earth has acted, not before. The human does not control the event; he asks about the earth's abnormal state.
4. `يومئذ تحدث أخبارها`: the earth's abnormal action reactivates as testimony. Its prior shaking and extraction become not only physical discharge but report-production.
5. `بأن ربك أوحى لها`: the cause is not autonomous earth agency. A hidden communication from `ربك` explains why the earth can report.
6. `يومئذ يصدر الناس أشتاتا ليروا أعمالهم`: the reporting field changes into human issuance and separation. People come out in divided states for a visual display of their own deeds.
7. `فمن يعمل مثقال ذرة خيرا يره`: the scale contracts from earth-burden to atom-weight. Good is not lost in smallness.
8. `ومن يعمل مثقال ذرة شرا يره`: the paired closure freezes the rule. Evil also becomes visible at the same minimal weight; the surah closes when the accounting symmetry is complete.

## Candidate synthesis units

### C99-01: possessed ground convulses, empties, then becomes evidentiary ground

- candidate_id: C99-01
- ayah_range: 99:1-5
- seed_type: lexical
- seed: `99:1:2 زُلْزِلَتِ × ز ل ز ل B001 اضطراب واهتزاز`
- generating_set: `(E: ز ل ز ل B001 اضطراب واهتزاز)`, `(E: ء ر ض B001 السفل المقابل للسماء)`, `(E: خ ر ج B001 النفاذ إلى خارج الشيء)`, `(E: خ ر ج B002 إخراج الشيء من خفائه)`, `(E: ث ق ل B001 الثقل ضد الخفة)`, `(E: ث ق ل B005 الثقل النفيس ذو القدر)`
- selected_branches: ZLZL B001; ARD B001; KHRJ B001/B002; THQL B001/B005; later C/K from HDTH, KHBR, WHI, RBB.
- constructed_model: a lower possessed substrate is violently disturbed, then forced to externalize what it held. The extraction becomes legible as evidence once the same substrate reports its news.
- freeze_point: after 99:2, before human speech and before `تحدث أخبارها`.
- predictions_at_freeze: expected hidden/interior contents; expected owner/possessor relation; expected reactivation of earth as more than inert location; expected explanation for earth's agency.
- unused_features_tested: 99:3 human question; 99:4 earth reporting; 99:5 divine communication; possessive suffixes in `زلزالها`, `أثقالها`, `أخبارها`; repeated `الأرض`; attachment rows for subjects and direct objects.
- corroborators: `(C: attachment 99:1 passive subject earth)`, `(C: attachment 99:1 cognate accusative zلزالها)`, `(C: attachment 99:2 earth as active subject)`, `(C: attachment 99:2 أثقالها as direct object)`, `(C: ح د ث B003 كلام يتجدد خبرا وحديثا)`, `(C: خ ب ر B001 العلم بالخبر وباطن الأمر)`, `(C: و ح ي B001 إلقاء علم في خفاء)`, `(C: ر ب ب B001 ربوبية وملك وسيادة)`.
- constraints: `(K: earth is grammatical patient in 99:1 but subject in 99:2 and 99:4, so the model must be state-transition, not stable agency)`, `(K: no branch permits replacing primary meaning with metaphor only)`.
- temporal_reactivation_notes: the first violent movement is reinterpreted at 99:4 as the first stage of testimony; extraction of burdens anticipates disclosure of reports.
- rival_models: purely physical earthquake; womb/birth model from THQL B007; bodily seizure model from ARD B008/ZLZL.
- grade: strong
- grade_rationale: several independent channels converge: root repetition, earth as repeated participant, possessed hidden contents, report-production, and divine hidden instruction.
- source_queries_or_rows_used: S99 qac-root export rows for ZLZL/ARD/KHRJ/THQL/HDTH/KHBR/RBB/WHI; S99 attachment rows 99:1 a1-a3, 99:2 a1-a3, 99:4 a1-a3, 99:5 a1-a4.

### C99-02: burdens become measured deeds

- candidate_id: C99-02
- ayah_range: 99:2, 99:6-8
- seed_type: lexical
- seed: `99:2:3 أَثْقَالَهَا × ث ق ل B001 الثقل ضد الخفة`
- generating_set: `(E: ث ق ل B001 weight/gravitas)`, `(E: خ ر ج B002 making hidden thing emerge)`, `(E: ع م ل B001 intentional action)`, `(E: ث ق ل B004 المثقال والوزن)`, `(E: ذ ر ر B001 صغر الذر وانتشاره)`
- selected_branches: THQL B001/B004/B005; KHRJ B002; AML B001; DRR B001; RAI B001/B012; KHYR B001; SHRR B001.
- constructed_model: what first appears as the earth's heavy contents reactivates as quantified moral contents. The large earth-burden is narrowed to the smallest possible weighted action.
- freeze_point: after linking 99:2 `أثقالها` to 99:6 `أعمالهم`, before 99:7-8.
- predictions_at_freeze: expected measurement; expected moral polarity; expected visibility of the hidden/actional contents; expected symmetry if the measuring principle is complete.
- unused_features_tested: `مثقال ذرة`, `خيرا`, `شرا`, repeated `يره`, paired conditionals.
- corroborators: `(C: ث ق ل B004 المثقال والوزن after freeze)`, `(C: ذ ر ر B001 smallness)`, `(C: ر ء ي B012 إراءة وإظهار)`, `(C: خ ي ر B001 الخير ضد الشر)`, `(C: ش ر ر B001 الشر والسوء)`, `(C: parallel morphology 99:7 and 99:8)`.
- constraints: `(K: أثقالها in 99:2 is possessed by earth, while أعمالهم in 99:6 is possessed by people; the synthesis must be reactivation, not identity)`.
- temporal_reactivation_notes: `أثقالها` opens heaviness; `أعمالهم` supplies human ownership; `مثقال ذرة` retrofits the burden image into precise accounting.
- rival_models: physical graves/minerals only; childbirth burden; tax/output model from KHRJ B003.
- grade: strong
- grade_rationale: the surah itself moves from weight-burdens to measured atom-weight deeds, with independent lexical support from THQL, AML, DRR, RAI, KHYR, and SHRR.
- source_queries_or_rows_used: S99 qac-root rows for THQL at 99:2/7/8, AML at 99:6/7/8, DRR, KHYR, SHRR, RAI; attachment rows 99:2 a2-a3, 99:6 a5-a6, 99:7 a2-a5, 99:8 a2-a5.

### C99-03: hidden communication authorizes the earth's testimony

- candidate_id: C99-03
- ayah_range: 99:3-5
- seed_type: lexical
- seed: `99:5:3 أَوْحَىٰ × و ح ي B001 إلقاء علم في خفاء`
- generating_set: `(E: و ح ي B001 hidden imparting of knowledge)`, `(E: و ح ي B004 divine revelation/inspiration)`, `(E: ح د ث B003 renewed speech/news)`, `(E: خ ب ر B001 inner knowledge/report)`, `(E: ر ب ب B001 lordship/ownership)`
- selected_branches: WHI B001/B004/B005; HDTH B003/B006; KHBR B001; RBB B001/B002.
- constructed_model: the earth does not spontaneously speak; a hidden divine instruction makes its buried knowledge reportable. Human bewilderment is answered by the concealed source.
- freeze_point: after 99:5, before returning to people in 99:6.
- predictions_at_freeze: expected recipient construction for earth; expected link between report and authorization; expected non-human agency under higher command.
- unused_features_tested: `لها` as recipient of revelation; `ربك` as source; 99:3 `ما لها`; 99:6 people shown their deeds.
- corroborators: `(C: attachment 99:5 أَوْحَىٰ لَهَا recipient complement)`, `(C: ق و ل B001 human utterance creates question)`, `(C: ق و ل B014 thing's condition/dalalah, constrained)`, `(C: ر ء ي B012 showing after report)`.
- constraints: `(K: ق و ل applies to human speech in 99:3, not earth's verb in 99:4; use ح د ث for earth's reporting)`, `(K: no messenger figure is supplied; revelation is to earth, not a prophet in the immediate syntax)`.
- temporal_reactivation_notes: `ما لها` makes the hearer wait for a cause; `بأن ربك أوحى لها` resolves the question.
- rival_models: earth as autonomous witness; sound-only tremor; written inscription model from WHI B003.
- grade: strong
- grade_rationale: WHI, HDTH, KHBR, RBB, attachments, and sequence independently support an authorized testimony structure.
- source_queries_or_rows_used: S99 qac-root rows for WHI/RBB/HDTH/KHBR/QWL/RAI; attachment rows 99:3 a1-a4, 99:4 a1-a3, 99:5 a1-a4.

### C99-04: human bewilderment becomes human exposure

- candidate_id: C99-04
- ayah_range: 99:3, 99:6-8
- seed_type: lexical
- seed: `99:3:2 ٱلْإِنسَٰنُ × ء ن س B002 إيناس الشيء برؤية أو إحساس أو سماع`
- generating_set: `(E: ء ن س B002 perception by seeing/hearing/sensing)`, `(E: ق و ل B001 uttered speech)`, `(E: ر ء ي B001 sight/perception)`, `(E: ر ء ي B012 showing)`, `(E: ع م ل B001 intentional action)`
- selected_branches: ANS B001/B002; QWL B001/B011/B012 constrained; RAI B001/B012/B013; AML B001.
- constructed_model: the human first senses an abnormal event and speaks a question, then becomes the one whose own intentional acts are shown back to him.
- freeze_point: after 99:3, before 99:4-8.
- predictions_at_freeze: expected answer to perception; expected human involvement beyond spectatorship; expected later visual disclosure.
- unused_features_tested: 99:6 `ليروا أعمالهم`; 99:7-8 `يره`; 99:4-5 cause of earth reporting.
- corroborators: `(C: ر ء ي B012 showing)`, `(C: ع م ل B001 intentional action)`, `(C: attachment 99:6 أعمالهم as object of showing)`, `(C: repeated يره in closure)`.
- constraints: `(K: الإنسان in 99:3 is singular generic, الناس in 99:6 plural collective; the model must allow generic-to-collective expansion)`, `(K: initial human utterance does not generate the earth's testimony; divine instruction does)`.
- temporal_reactivation_notes: the human question is not dropped; it is overtaken by a stronger answer in which the human becomes the object of display.
- rival_models: human as merely confused observer; human as accuser of earth.
- grade: medium-strong
- grade_rationale: perception/speech/showing is well supported, but the lexical route from ANS B002 to final accountability is less specific than the THQL/RAI/AML axis.
- source_queries_or_rows_used: QAC export rows for ANS/QWL/RAI/AML; attachment rows 99:3 a1-a4, 99:6 a2/a5/a6, 99:7-8 a5.

### C99-05: issuing from a source into separated groups

- candidate_id: C99-05
- ayah_range: 99:6
- seed_type: lexical
- seed: `99:6:2 يَصْدُرُ × ص د ر B003 الصُّدور عن المورد`
- generating_set: `(E: ص د ر B003 departure from a water-place/source after arrival)`, `(E: ش ت ت B001 dispersal)`, `(E: ن و س B001 dangling/trembling, weakly as post-earthquake human instability)`, `(E: ر ء ي B012 being shown)`, `(E: ع م ل B001 deeds)`
- selected_branches: SDR B003/B002/B004; SHTT B001/B003; RAI B012; AML B001.
- constructed_model: after the earth's report-source is activated, people issue out from the scene not as one body but in separated streams so that individual deeds can be displayed.
- freeze_point: after 99:6 before the two conditionals.
- predictions_at_freeze: expected distribution by difference; expected object of display; expected individualized outcomes.
- unused_features_tested: paired `فمن/ومن`, repeated `يعمل`, repeated `يره`, `خيرا/شرا`.
- corroborators: `(C: ش ت ت B001 explicit dispersal)`, `(C: ش ت ت B003 distance/divergence)`, `(C: conditional parallel 99:7-8)`, `(C: خ ي ر B001 and ش ر ر B001 polarity)`.
- constraints: `(K: ص د ر B001 chest and B005 financial confiscation do not fit the local syntax)`, `(K: no explicit water source appears; B003 functions as issuing-after-arrival geometry, not literal watering)`.
- temporal_reactivation_notes: the earlier `أخرجت` externalization is reactivated in human `يصدر`: the earth brings out contents, then people come out for display.
- rival_models: simple resurrection movement; bureaucratic procession; source/grammar model from SDR B004.
- grade: medium-strong
- grade_rationale: SDR B003 and SHTT B001 are locally exact; the water-source aspect is secondary and must remain subordinate.
- source_queries_or_rows_used: QAC export rows for SDR/SHTT/RAI/AML/KHYR/SHRR; attachment rows 99:6 a1-a6, 99:7-8.

### C99-06: the smallest dispersed particle still appears

- candidate_id: C99-06
- ayah_range: 99:7-8
- seed_type: lexical
- seed: `99:7:4 ذَرَّةٍ × ذ ر ر B001 صغر الذر وانتشاره`
- generating_set: `(E: ذ ر ر B001 tiny particles)`, `(E: ث ق ل B004 weighed measure)`, `(E: ع م ل B001 intentional action)`, `(E: ر ء ي B001 seeing)`, `(E: خ ي ر B001 good against evil)`, `(E: ش ر ر B001 evil against good)`
- selected_branches: DRR B001/B002; THQL B004; AML B001; RAI B001; KHYR B001; SHRR B001.
- constructed_model: even a particle-sized dispersed unit receives weight and visibility. Smallness no longer hides an action from display.
- freeze_point: after 99:7, before 99:8.
- predictions_at_freeze: expected exact parallel for the opposite polarity; expected repeated visual verb; expected no threshold below moral visibility.
- unused_features_tested: 99:8 full repetition with `شرا`.
- corroborators: `(C: 99:8 parallel syntax)`, `(C: ش ر ر B001 exact opposition to خير)`, `(C: repeated مثقال ذرة)`, `(C: repeated يره)`.
- constraints: `(K: ذ ر ر B002 scattering is usable as image but not primary contextual meaning; local word is singular ذرة)`.
- temporal_reactivation_notes: the surah contracts from earth-scale shaking to atom-scale disclosure; closure occurs when both polarities are covered.
- rival_models: dust/scattering only; sunrise glimmer from DRR B004.
- grade: strong
- grade_rationale: smallest-unit, weight, deed, polarity, and visual return are all explicit and independently supported.
- source_queries_or_rows_used: QAC rows for DRR/THQL/AML/RAI/KHYR/SHRR; attachment rows 99:7 a1-a5, 99:8 a1-a5.

### C99-07: writing/inscription in the earth as a secondary testimony image

- candidate_id: C99-07
- ayah_range: 99:4-5
- seed_type: lexical
- seed: `99:5:3 أَوْحَىٰ × و ح ي B003 كتابة ونقش`
- generating_set: `(E: و ح ي B003 writing/engraving)`, `(E: خ ب ر B001 inner knowledge/report)`, `(E: ح د ث B003 speech/news)`, `(E: ء ر ض B001 lower ground)`, `(E: ر ء ي B012 showing)`
- selected_branches: WHI B003/B010; KHBR B001; HDTH B003/B006; ARD B001.
- constructed_model: the earth functions like a marked or inscribed substrate: hidden instruction/report becomes readable testimony.
- freeze_point: after WHI B003 + KHBR B001, before testing `ليروا أعمالهم`.
- predictions_at_freeze: expected visibility or display; expected preserved record; expected source authority.
- unused_features_tested: `ليروا أعمالهم`, repeated `يره`, `ربك`.
- corroborators: `(C: ر ء ي B012 showing)`, `(C: ر ب ب B001 source authority)`, `(C: possessive أخبارها: reports belonging to earth)`.
- constraints: `(K: the text says أوحى لها, not كتب عليها; inscription is a secondary simulation only)`, `(K: no literal writing surface is named)`.
- temporal_reactivation_notes: the "earth as ground" reactivates as a possible record-bearing ground when it reports.
- rival_models: oral speech only; hidden voice only from WHI B005.
- grade: medium
- grade_rationale: strong branch support for a record-image, but local syntax favors hidden communication and reporting over literal inscription.
- source_queries_or_rows_used: WHI/KHBR/HDTH/ARD/RAI/RBB branch rows; attachment 99:4-5.

### C99-08: earth as laboring container / burdened body

- candidate_id: C99-08
- ayah_range: 99:1-2
- seed_type: lexical
- seed: `99:2:3 أَثْقَالَهَا × ث ق ل B007 إثقال الحمل`
- generating_set: `(E: ث ق ل B007 pregnancy/burden in belly)`, `(E: خ ر ج B001 emergence from within)`, `(E: ء ر ض B001 earth/body substrate)`, `(E: ز ل ز ل B001 convulsion)`
- selected_branches: THQL B007; KHRJ B001/B002; ARD B001; ZLZL B001.
- constructed_model: the earth is imaged as a burdened body undergoing convulsive release of what it carried internally.
- freeze_point: after 99:2.
- predictions_at_freeze: expected possessed inner contents; expected later naming of what emerges; possible relation to testimony/birth.
- unused_features_tested: 99:4 `أخبارها`; 99:6 `أعمالهم`.
- corroborators: `(C: possessive suffix in أثقالها)`, `(C: خروج from hidden)`, `(C: later display of deeds as emerged contents)`.
- constraints: `(K: the text does not supply birth vocabulary, child, womb, or mother term)`, `(K: أثقالها has broader weight/burden branch support and must not be reduced to pregnancy)`.
- temporal_reactivation_notes: the convulsion/extraction sequence invites body-labor as a secondary image, then is redirected toward evidentiary/accounting contents.
- rival_models: geological discharge; evidentiary burden.
- grade: medium
- grade_rationale: the burden/extraction/convulsion fit is real but not completed by a literal childbirth lexicon.
- source_queries_or_rows_used: THQL/KHRJ/ARD/ZLZL branch rows; attachment 99:1-2.

### C99-09: the rattled human body mirrors the rattled earth

- candidate_id: C99-09
- ayah_range: 99:1, 99:3, 99:6
- seed_type: lexical
- seed: `99:1:3 ٱلْأَرْضُ × ء ر ض B008 الأَرْض الرعدة`
- generating_set: `(E: ء ر ض B008 bodily trembling)`, `(E: ز ل ز ل B001 shaking)`, `(E: ء ن س B002 perception/fear sensed)`, `(E: ن و س B001 dangling/trembling instability)`
- selected_branches: ARD B008; ZLZL B001; ANS B002; NWS B001.
- constructed_model: the earth's shaking is mirrored in the human who senses abnormality and later emerges unsteady among scattered people.
- freeze_point: after 99:3.
- predictions_at_freeze: expected human destabilization; expected dispersal or loss of composure.
- unused_features_tested: 99:6 `أشتاتا`, `الناس`.
- corroborators: `(C: ش ت ت B001 dispersal)`, `(C: ن و س B001 trembling/dangling, if الناس is permitted to activate نوس)`.
- constraints: `(K: الناس is contextually people and QAC export treats 99:3 الإنسان under ء ن س; NWS is weak and should not control the model)`, `(K: no explicit fear word appears)`.
- temporal_reactivation_notes: the first physical tremor becomes a social/perceptual tremor in human speech and separated issuing.
- rival_models: non-human earth only; strict accounting model.
- grade: weak
- grade_rationale: vivid but depends on remote ARD/NWS body-branches; local syntax favors earth testimony and moral display.
- source_queries_or_rows_used: ARD/ZLZL/ANS/NWS/SHTT branch rows; attachment 99:1, 99:3, 99:6.

### C99-10: good/evil polarity closes the display

- candidate_id: C99-10
- ayah_range: 99:7-8
- seed_type: verified composite
- seed: paired construction `فمن يعمل مثقال ذرة خيرا يره / ومن يعمل مثقال ذرة شرا يره`
- generating_set: `(E: conditional pair)`, `(E: ع م ل B001 intentional action)`, `(E: ث ق ل B004 measured weight)`, `(E: ذ ر ر B001 tiny unit)`, `(E: خ ي ر B001 good opposed to evil)`, `(E: ش ر ر B001 evil opposed to good)`, `(E: ر ء ي B001 sight)`
- selected_branches: AML B001; THQL B004; DRR B001; KHYR B001; SHRR B001; RAI B001/B012.
- constructed_model: a rule is completed only when both positive and negative actions, down to atom-weight, become visible to their doers.
- freeze_point: after 99:7, before 99:8.
- predictions_at_freeze: expected matched negative clause; expected same measure; expected same visual outcome.
- unused_features_tested: 99:8 exact parallel.
- corroborators: `(C: 99:8 repeats من يعمل مثقال ذرة ... يره)`, `(C: خ ي ر/ش ر ر lexical opposition)`, `(C: object suffix in يره attached to seen action/result)`.
- constraints: `(K: no lexical basis for collapsing good and evil into one neutral visibility; the pair preserves polarity)`.
- temporal_reactivation_notes: the surah stops when the accounting rule is symmetric and exhaustive.
- rival_models: only good reward; only exposure of evil; generic smallness.
- grade: strong
- grade_rationale: exact grammatical, lexical, and sequential symmetry.
- source_queries_or_rows_used: attachment 99:7-8; branch rows AML/THQL/DRR/KHYR/SHRR/RAI.

### C99-11: remote evil images that terminate

- candidate_id: C99-11
- ayah_range: 99:8
- seed_type: lexical
- seed: `99:8:5 شَرًّا × remote ش ر ر branches`
- generating_set: tested `ش ر ر B002/B003/B004/B005/B006/B007/B009/B010/B011/B012`
- selected_branches: weak image forks only from B002 drying/exposure, B003 sparks, B004 cutting/scattering, B007 throwing oneself entirely.
- constructed_model: evil can be secondarily imagined as exposed-to-dry matter, flying sparks, cut fragments, or total self-investment.
- freeze_point: each remote branch frozen immediately after seed.
- predictions_at_freeze: expected fire/drying/cutting/total self-casting if branch controlled the passage.
- unused_features_tested: earthquake, earth, atom-weight, seeing.
- corroborators: `(C: ر ء ي B001 visibility only weakly supports exposure)`, `(C: ذ ر ر B002 scattering weakly supports fragmenting)`.
- constraints: `(K: 99:8 context supplies moral شر against خير, not fire, drying racks, meat, youth vigor, insects, or quarrel)`.
- temporal_reactivation_notes: the remote branches die at the final closure; they do not reorganize earlier cues.
- rival_models: none retained.
- grade: unlikely
- grade_rationale: B001 is the accepted contextual branch; other branches lack passage-local role completion.
- source_queries_or_rows_used: SHRR branch rows; attachment 99:8 a4-a5.

## Exhaustive lexical seed ledger

Each entry below represents an occurrence × accepted branch seed pass. `Cxx` means the seed converged into the named candidate above. `Local` means a small local image was retained but did not reorganize the surah. `Terminated` means the seed was read against all dossiers and failed to find a passage-specific completion.

### 99:1:2 `زُلْزِلَتِ`

- `ز ل ز ل B001`: C99-01 strong; also supports C99-08 and C99-09.
- `ز ل ز ل B002`: Local medium; "شدائد الدهر" supports the day-of-event severity with `(C: ي و م B003)`, but does not by itself produce the reporting/accounting system.
- `ز ل ز ل B003`: Terminated/weak; "clear easy-flowing water" has no local water channel except a remote, constrained contact with `ص د ر B003`.

### 99:1:3 `ٱلْأَرْضُ`

- `ء ر ض B001`: C99-01 strong; lower substrate against sky/above.
- `ء ر ض B002`: Local weak; fertile/growing earth weakly contacts `ذ ر ر B004` sprouting and `خ ب ر B002` soft lowland, but the passage emphasizes disclosure, not cultivation.
- `ء ر ض B003`: Local weak; "apt for good" weakly anticipates `خيرا`, but earth is not morally characterized.
- `ء ر ض B004`: Terminated; stranger/son of earth has no passage-local role.
- `ء ر ض B005`: Terminated; thick rug has no role.
- `ء ر ض B006`: Local medium; heaviness/remaining on earth supports the ground/weight axis but not reporting.
- `ء ر ض B007`: Terminated; exposure/opposition as "presenting oneself" lacks complement.
- `ء ر ض B008`: C99-09 weak; bodily trembling fork.
- `ء ر ض B009`: Terminated; cold/catarrh no role.
- `ء ر ض B010`: Terminated; wood-eating insect no role.
- `ء ر ض B011`: Terminated; suppurating ulcer only weakly touches KHRJ B004 but no wound lexicon.
- `ء ر ض B012`: Local weak; disturbed body/person can support C99-09 but is too remote.

### 99:1:4 `زِلْزَالَهَا`

- `ز ل ز ل B001`: C99-01 strong, with attachment cognate accusative intensifying the event.
- `ز ل ز ل B002`: Local medium; intensifies event severity.
- `ز ل ز ل B003`: Terminated; no water/clarity role.

### 99:2:1 `أَخْرَجَتِ`

- `خ ر ج B001`: C99-01 and C99-08 strong; emergence from inside.
- `خ ر ج B002`: C99-01/C99-02 strong; hidden thing made manifest.
- `خ ر ج B003`: Local weak; "output/tax" anticipates accounting but no payment/tribute role.
- `خ ر ج B004`: Local weak; bodily swelling/eruption can feed C99-08, but no wound lexicon.
- `خ ر ج B005`: Terminated; cloud emergence not locally selected.
- `خ ر ج B006`: Local weak; exiting obedience/origin weakly contacts human separation, but lacks governance syntax.
- `خ ر ج B007`: Local weak; alternating patches can contact `أشتاتا`, but not enough.
- `خ ر ج B008`: Terminated; type-deformed camel no role.
- `خ ر ج B009`: Terminated; two-sided saddlebag no role.
- `خ ر ج B010`: Terminated; game of guessing what is in hand has only generic hiddenness.
- `خ ر ج B011`: Terminated; rhyme-letter no role.
- `خ ر ج B012`: Local weak; partition among partners weakly touches separated people.
- `خ ر ج B013`: Terminated; horse neck no role.

### 99:2:2 `ٱلْأَرْضُ`

The second earth occurrence was rerun separately because its grammar changed from passive subject/patient environment to active subject of extraction.

- `ء ر ض B001`: C99-01 strong.
- `ء ر ض B002`: Local weak, as above.
- `ء ر ض B003`: Local weak, as above.
- `ء ر ض B004`: Terminated.
- `ء ر ض B005`: Terminated.
- `ء ر ض B006`: Local medium; heaviness toward earth now interacts with `أثقالها`.
- `ء ر ض B007`: Local weak; earth "presents itself" only if constrained by active subject syntax.
- `ء ر ض B008`: C99-09 weak.
- `ء ر ض B009`: Terminated.
- `ء ر ض B010`: Terminated.
- `ء ر ض B011`: Local weak; discharge/corruption branch constrained.
- `ء ر ض B012`: Local weak.

### 99:2:3 `أَثْقَالَهَا`

- `ث ق ل B001`: C99-02 strong.
- `ث ق ل B004`: C99-02 and C99-06 strong; later `مثقال`.
- `ث ق ل B005`: C99-01/C99-02 medium-strong; precious/weighty contents become important deeds.
- `ث ق ل B006`: Local weak; heaviness/slowness supports burden but not accounting.
- `ث ق ل B007`: C99-08 medium.
- `ث ق ل B008`: Terminated; woman-body description has no local completion beyond rejected childbirth extension.
- `ث ق ل B009`: Local weak; heavy hearing may explain human bewilderment, but no hearing syntax.

### 99:3:1 `قَالَ`

- `ق و ل B001`: C99-04 medium-strong.
- `ق و ل B002`: Local weak; tongue as speech instrument.
- `ق و ل B003`: Local weak; much-talking human not supported.
- `ق و ل B004`: Terminated; Yemeni chief/authoritative saying no local role.
- `ق و ل B005`: Terminated/constraint; false speech is not indicated.
- `ق و ل B006`: Local weak; drawing a saying into oneself weakly touches `ما لها`.
- `ق و ل B007`: Local medium; circulating saying anticipates earth's reports but not exact.
- `ق و ل B008`: Terminated.
- `ق و ل B009`: Local weak; negotiation not present.
- `ق و ل B010`: Terminated.
- `ق و ل B011`: Local medium; interrogative/estimate supports `ما لها`.
- `ق و ل B012`: C99-04 medium; inner saying contrasts with uttered question.
- `ق و ل B013`: Terminated; belief/madhhab no role.
- `ق و ل B014`: C99-03 constrained; thing's state "says" only as dalalah, but local verb is human `قال`.
- `ق و ل B015`: Terminated.
- `ق و ل B016`: Terminated.

### 99:3:2 `ٱلْإِنسَٰنُ`

- `ء ن س B001`: C99-04 medium; human/broader people participant.
- `ء ن س B002`: C99-04 medium-strong.
- `ء ن س B003`: Local weak; loss of familiarity/terror by contrast, but not explicit.
- `ء ن س B004`: Terminated; facing side no role.
- `ء ن س B005`: Local medium; eye-image supports later seeing but remains secondary.
- `ء ن س B006`: Local weak; self/private person touches individual accountability.

### 99:4:1 `يَوْمَئِذٍ`

- `ي و م B001`: Local weak; ordinary day-time is not the main frame.
- `ي و م B002`: Local medium; duration/temporal span supports unfolding.
- `ي و م B003`: C99-01/C99-03 medium-strong; event/day of severity and occurrence.

### 99:4:2 `تُحَدِّثُ`

- `ح د ث B001`: Local medium; new occurrence after non-existence supports event transition.
- `ح د ث B002`: Terminated; youth/freshness no local role.
- `ح د ث B003`: C99-03 strong.
- `ح د ث B004`: C99-03 medium; becoming a matter spoken of, not primary.
- `ح د ث B005`: Local medium; calamity/event of time supports day severity.
- `ح د ث B006`: C99-01/C99-03 medium-strong; making manifest.
- `ح د ث B007`: Local weak; polishing heart/sword has no local role.

### 99:4:3 `أَخْبَارَهَا`

- `خ ب ر B001`: C99-01/C99-03 strong.
- `خ ب ر B002`: Local weak; soft/low earth recontacts ARD B002 but no water/lowland scene.
- `خ ب ر B003`: Local weak; earth cultivation/accounting by output not selected.
- `خ ب ر B004`: Terminated; large waterskin/milking no role.
- `خ ب ر B005`: Terminated; soft plant/foam no role.

### 99:5:2 `رَبَّكَ`

- `ر ب ب B001`: C99-03 strong.
- `ر ب ب B002`: C99-03 medium-strong; governing/cultivating to completion supports ordered disclosure.
- `ر ب ب B003`: Local medium; divine knowledge supports hidden communication.
- `ر ب ب B004`: Local weak; multitudes weakly contact `الناس`.
- `ر ب ب B005`: Terminated; stepchild/caretaker no role.
- `ر ب ب B006`: Terminated; thick syrup/repairing skin no role.
- `ر ب ب B007`: Local medium; permanence/abiding supports fixed command.
- `ر ب ب B008`: Terminated; cloud branch no role.
- `ر ب ب B009`: Terminated; newborn sheep/youth no role.
- `ر ب ب B010`: Local weak; container of arrows weakly contacts sorting, but no lots.
- `ر ب ب B011`: Local weak; covenant/authority possible but not explicit.
- `ر ب ب B012`: Terminated; plant no role.
- `ر ب ب B013`: Terminated; water no role.
- `ر ب ب B014`: Terminated; herd no role.
- `ر ب ب B015`: Terminated; grammatical `رب` not the word here.
- `ر ب ب B016`: Terminated; need/knot/blessing not completed.
- `ر ب ب B017`: Terminated; sailors' chief no role.

### 99:5:3 `أَوْحَىٰ`

- `و ح ي B001`: C99-03 strong.
- `و ح ي B002`: C99-03 medium; signaling to earth.
- `و ح ي B003`: C99-07 medium.
- `و ح ي B004`: C99-03 strong.
- `و ح ي B005`: Local medium; hidden sound supports recitational/report image but not visible accounting.
- `و ح ي B006`: Local weak; rapid command may explain sudden transition, but not central.
- `و ح ي B007`: Terminated; seeking help/inquiry not local.
- `و ح ي B008`: Terminated; kingship/fire branch lacks local support.
- `و ح ي B009`: Terminated; mourning/crying no role.
- `و ح ي B010`: C99-07 weak-medium; hidden/engraved in stone proverb supports inscription only secondarily.

### 99:6:1 `يَوْمَئِذٍ`

- `ي و م B001`: Local weak.
- `ي و م B002`: Local medium; second temporal marker links reporting and issuing.
- `ي و م B003`: C99-05 medium-strong; severe event day.

### 99:6:2 `يَصْدُرُ`

- `ص د ر B001`: Local weak; chest/front body no direct role.
- `ص د ر B002`: Local medium; coming at the front/beginning supports procession.
- `ص د ر B003`: C99-05 medium-strong.
- `ص د ر B004`: C99-05 medium; source/origin of actions as a grammatical image.
- `ص د ر B005`: Terminated; confiscation no role.
- `ص د ر B006`: Local weak; party/group supports `أشتاتا`.

### 99:6:3 `ٱلنَّاسُ`

- `ن و س B001`: C99-09 weak; trembling/dangling only secondary.
- `ن و س B002`: Terminated; driving camels no role.

### 99:6:4 `أَشْتَاتًا`

- `ش ت ت B001`: C99-05 strong.
- `ش ت ت B002`: Terminated; spaced teeth no role.
- `ش ت ت B003`: C99-05 medium-strong; distance/divergence reinforces separation.

### 99:6:5 `لِّيُرَوْا`

- `ر ء ي B001`: C99-04/C99-05/C99-10 strong.
- `ر ء ي B002`: Local medium; insight/judgment supports moral recognition.
- `ر ء ي B003`: Terminated; dream no role.
- `ر ء ي B004`: Local medium; mutual facing supports display, not central.
- `ر ء ي B005`: Local weak; showing to people/ostentation is constrained because the showing is divine/accounting, not human show.
- `ر ء ي B006`: C99-14 local medium; mirror/appearance image retained as secondary.
- `ر ء ي B007`: Terminated; menstrual sign no role.
- `ر ء ي B008`: Terminated; jinn familiar no role.
- `ر ء ي B009`: Terminated; lung no role.
- `ر ء ي B010`: Terminated; animal pregnancy no role.
- `ر ء ي B011`: Local weak; raised sign supports display only generically.
- `ر ء ي B012`: C99-04/C99-05/C99-10 strong.
- `ر ء ي B013`: Local medium; attention/get-me-informed supports the human question and final disclosure.

### 99:6:6 `أَعْمَٰلَهُمْ`

- `ع م ل B001`: C99-02/C99-04/C99-10 strong.
- `ع م ل B002`: Local medium; employing/setting to work supports caused display.
- `ع م ل B003`: Local weak; office/administration supports accounting only remotely.
- `ع م ل B004`: Local medium; wage/recompense implied by showing deeds but not explicit.
- `ع م ل B005`: Local weak; transactions among people not local.
- `ع م ل B006`: Terminated; manual laborers no role.
- `ع م ل B007`: Local weak; hardship of acting not central.
- `ع م ل B008`: Terminated; work-bred camel/person no role.
- `ع م ل B009`: Terminated; spear shaft has no local weapon roles.
- `ع م ل B010`: Local weak; active limb/eye connects weakly to seeing/doing.
- `ع م ل B011`: Local weak; traveled path supports life-course only secondarily.
- `ع م ل B012`: Local weak; walkers/travelers weakly contact issuing people.

### 99:7:2 `يَعْمَلْ`

All `ع م ل` branches were rerun for the conditional verb. B001 is C99-10 strong. B002, B004, B010, and B011 remain local weak-to-medium secondary images. B003, B005, B006, B007, B008, B009, and B012 terminate or remain too remote because the conditional requires intentional deed, not office, transaction, manual crew, spear, or traveler identity.

### 99:7:3 `مِثْقَالَ`

All `ث ق ل` branches were rerun for the measured object. B004 is C99-06/C99-10 strong. B001 supports C99-02. B005 is medium as moral weight/importance. B006/B007/B008/B009 terminate or remain weak because the local form is a measure, not bodily heaviness, pregnancy, body description, or hearing defect.

### 99:7:4 `ذَرَّةٍ`

- `ذ ر ر B001`: C99-06 strong.
- `ذ ر ر B002`: Local medium; scattering supports dispersed small units but not primary.
- `ذ ر ر B003`: Terminated; powdered perfume no role.
- `ذ ر ر B004`: Local weak; subtle dawn/sprouting image not completed.

### 99:7:5 `خَيْرًا`

- `خ ي ر B001`: C99-10 strong.
- `خ ي ر B002`: Local medium; excellence/selection supports positive pole.
- `خ ي ر B003`: Local weak; choosing better not syntactically present.
- `خ ي ر B005`: Local weak; gift/beneficence can instantiate good but not general.
- `خ ي ر B006`: Terminated; driving animal from burrow no role.

### 99:7:6 `يَرَهُۥ`

All `ر ء ي` branches were rerun for the singular closure. B001 and B012 are C99-06/C99-10 strong. B002 is medium as recognition. B004/B006/B011/B013 are local secondary display/sign/attention images. B003/B005/B007/B008/B009/B010 terminate or are constrained by the direct object suffix and moral-display syntax.

### 99:8:2 `يَعْمَلْ`

The second conditional `ع م ل` pass repeats the 99:7 outcomes but now tests the negative pole. B001 remains C99-10 strong; B004 recompense becomes slightly more active; all remote branches remain terminated or local as above.

### 99:8:3 `مِثْقَالَ`

The second `ث ق ل` measured pass repeats the 99:7 outcomes and corroborates symmetry. B004 remains C99-10 strong; B001 and B005 support moral weight; remote body/hearing branches terminate.

### 99:8:4 `ذَرَّةٍ`

The second `ذ ر ر` pass repeats the 99:7 outcomes and corroborates that tiny-unit visibility covers both poles. B001 strong; B002 local; B003/B004 terminate or remain weak.

### 99:8:5 `شَرًّا`

- `ش ر ر B001`: C99-10 strong.
- `ش ر ر B002`: C99-11 unlikely; exposure/drying weakly fits visibility but lacks local material.
- `ش ر ر B003`: C99-11 unlikely; sparks are attractive after shaking but unsupported.
- `ش ر ر B004`: C99-11 unlikely; cutting/shredding lacks object.
- `ش ر ر B005`: Terminated; dripping roast no role.
- `ش ر ر B006`: Local weak; dangling weights can contact THQL/NWS, but no tail/appendage.
- `ش ر ر B007`: Local weak; self wholly cast into an act can moralize evil, but branch is idiomatic and not local.
- `ش ر ر B009`: Terminated; gnat-like pest no role.
- `ش ر ر B010`: Terminated; youthful vigor no role.
- `ش ر ر B011`: Local weak; quarrel not present.
- `ش ر ر B012`: Terminated; plant no role.

### 99:8:6 `يَرَهُۥ`

The final `ر ء ي` pass repeats the 99:7 result and closes the surah. B001/B012 are strong; B002 medium; B004/B006/B011/B013 secondary; all remaining branches terminate.

## Constructional, morphosyntactic, and temporal seeds

- `إذا + passive shaking + cognate accusative`: C99-01 strong. The construction creates an event-trigger with intensified internal repetition.
- repeated `الأرض` as subject/patient/agent: C99-01 strong. Earth shifts from passive subject of shaking to active subject of extraction and reporting.
- possessive suffix chain `زلزالها / أثقالها / أخبارها`: C99-01/C99-02 strong. The repeated `ها` keeps the earth as owner/container/witness.
- human question `ما لها`: C99-03/C99-04 medium-strong. It freezes an unresolved cause that 99:5 answers.
- `يومئذ` repetition at 99:4 and 99:6: medium-strong temporal seed. It binds report-time and issuing-time as the same realized event-state.
- `بأن ربك أوحى لها`: C99-03 strong. The `بأن` explanation and `لها` recipient prevent autonomous-earth models.
- `يصدر الناس أشتاتا`: C99-05 medium-strong. Issuing plus separation predicts individualized display.
- purpose construction `ليروا أعمالهم`: C99-04/C99-05 strong. The movement of people is not purposeless; it is directed toward seeing deeds.
- paired conditionals `فمن ... ومن ...`: C99-10 strong. The final construction completes exhaustive polarity.
- repeated `يعمل / مثقال ذرة / يره`: C99-06/C99-10 strong. The repeated frame says that the governing rule is invariant under good/evil polarity.

## Image Packet Catalog

### IMG-99-A

- Starting seed: `ز ل ز ل B001` at 99:1:2.
- Complete image: a possessed lower substrate convulses, discharges hidden burdens, and becomes a reporting witness under hidden divine command.
- Passage-order assembly: 99:1 shaking -> 99:2 extraction -> 99:3 question -> 99:4 report -> 99:5 authorization.
- Participants and roles: earth = substrate/container/witness; burdens = hidden contents; human = bewildered observer; Lord = authorizing source.
- Operation / mechanism: disturbance externalizes hidden contents, then communication makes disclosure verbal/evidentiary.
- Direction / force / medium: from inside earth outward; from hidden command to earth; from report to human exposure.
- Temporal development: physical event becomes evidentiary event.
- Outcome / closure: prepares `أعمالهم` and atom-weight display.
- Exact branch constituents: ZLZL B001; ARD B001; KHRJ B001/B002; THQL B001/B005; HDTH B003; KHBR B001; WHI B001/B004; RBB B001.
- Unfilled roles: exact identity of `أثقالها` remains open until linked with deeds.
- Status: COMPLETE.

### IMG-99-B

- Starting seed: `ث ق ل B001/B004` at 99:2:3 and 99:7-8.
- Complete image: hidden heaviness becomes moral measure down to atom-weight.
- Passage-order assembly: 99:2 burdens -> 99:6 deeds -> 99:7-8 measured good/evil.
- Participants and roles: earth = initial holder; people = owners of deeds; atom = lower bound; sight = disclosure.
- Operation / mechanism: heaviness is transformed into measurement.
- Direction / force / medium: from large buried burden to minimal quantified act.
- Temporal development: early weight is reactivated by later `مثقال`.
- Outcome / closure: no good or evil action below visibility threshold.
- Exact branch constituents: THQL B001/B004/B005; AML B001; DRR B001; RAI B001/B012; KHYR B001; SHRR B001.
- Unfilled roles: none.
- Status: COMPLETE.

### IMG-99-C

- Starting seed: `و ح ي B001` at 99:5:3.
- Complete image: hidden instruction authorizes non-human testimony.
- Passage-order assembly: question -> earth reports -> because Lord communicates to it.
- Participants and roles: Lord = source/owner; earth = recipient/witness; reports = content.
- Operation / mechanism: concealed knowledge-command causes public report.
- Direction / force / medium: from divine source to earth, then from earth to hearing/display.
- Temporal development: the cause appears after the effect, reinterpreting earth's behavior.
- Outcome / closure: people are shown their deeds in the authorized disclosure field.
- Exact branch constituents: WHI B001/B004; HDTH B003; KHBR B001; RBB B001/B002.
- Unfilled roles: medium of the communication remains unspecified.
- Status: COMPLETE.

### IMG-99-D

- Starting seed: paired conditional construction at 99:7-8.
- Complete image: a symmetric accountability rule.
- Passage-order assembly: people shown deeds -> whoever does atom-weight good sees it -> whoever does atom-weight evil sees it.
- Participants and roles: doer = conditional subject; deed = measured object; good/evil = polarity; seeing = outcome.
- Operation / mechanism: action is weighed and displayed.
- Direction / force / medium: from performed act to visible return.
- Temporal development: final pair closes the scope of display.
- Outcome / closure: exhaustive polarity at smallest scale.
- Exact branch constituents: AML B001; THQL B004; DRR B001; KHYR B001; SHRR B001; RAI B001/B012.
- Unfilled roles: none.
- Status: COMPLETE.

### IMG-99-E

- Starting seed: `ث ق ل B007` and `ء ر ض B008`.
- Complete image: body-like convulsion and burden release.
- Passage-order assembly: shaking -> earth extracts burdens -> human asks.
- Participants and roles: earth = burdened body; burdens = carried contents; human = startled witness.
- Operation / mechanism: convulsion releases interior load.
- Direction / force / medium: from belly/interior to outside.
- Temporal development: physical image is later constrained by report/accounting.
- Outcome / closure: retained as secondary simulation only.
- Exact branch constituents: THQL B007; ARD B008; ZLZL B001; KHRJ B001.
- Unfilled roles: no child/womb term; no explicit body lexicon for earth.
- Status: FRAGMENT.

## Final self-check for exhaustion

- Rooted occurrence sweep restarted from first rooted word: yes, beginning with `99:1:2 زُلْزِلَتِ`.
- Every accepted branch in the S99 branch universe was given a seed pass: yes, represented in the ledger above.
- Every repeated rooted occurrence with a different local role was rerun: yes, especially `ز ل ز ل`, `ء ر ض`, `ث ق ل`, `ر ء ي`, `ع م ل`, `ذ ر ر`, and `ي و م`.
- Constructional/morphosyntactic seeds were run separately: yes.
- Construction and corroboration are kept separate in candidate packets: yes.
- Failed and weak seeds are not silently dropped: yes; they are marked `Terminated`, `Local weak`, or `unlikely`.
- Potentially missing images checked: yes. Additional remote images from water, cloud, childbirth, wound, inscription, mirror, sparks, drying, quarrel, and body-tremor branches were generated or tested; only the coherent or instructive fragments were retained.
- Pass 2 output path written: `v1/outputs/99-stage1-pass-2.md`.
