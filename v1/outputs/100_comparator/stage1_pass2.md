# Stage 1 Pass 2 — S100 comparator main lane

Output target: `v1/outputs/100_comparator/stage1_pass2.md`  
Assigned passage: S100  
Sacred Arabic source: `resources/quran/surah_100.json`  
Prompt followed: `v1/prompts/stage1.md`

Permitted resources used only within S100:1–11:

- `resources/qac.sqlite`: schema inspected; S100 words and morphemes queried.
- `resources/attachments.tsv`: header and S100 rows queried.
- `resources/furuq_v4.sqlite`: schema inspected; only `contaminated='no'` branch images for S100 roots queried.

No other output files, translations, tafsir, hadith, web sources, or external interpretation were used.

## Root cause of Pass 1 limitation

The limitation was not a resource limitation. The root cause was reporting compression: Pass 1 foregrounded a small number of convergent findings and then placed many remaining branch-seeds into a compact ledger. That made it look as if each finding had visited only the promising words, because the per-seed sweep over all other root dossiers was not explicitly reported. I also treated constructional seeds as representative groups rather than a fully enumerated audit. For Pass 2 I restart from the first rooted word and expose the sweep ledger: every eligible occurrence × branch seed receives its own seed pass, and every eligible constructional/morphosyntactic/temporal seed is separately initiated.

## Exhaustiveness contract for this pass

First rooted word: 100:1:1 `وَٱلْعَٰدِيَٰتِ`, root `ع د و`.

Rooted word occurrences in QAC order:

1. 100:1:1 `وَٱلْعَٰدِيَٰتِ` — `ع د و` — 12 branches.
2. 100:1:2 `ضَبْحًا` — `ض ب ح` — 5 branches.
3. 100:2:1 `فَٱلْمُورِيَٰتِ` — `و ر ي` — 8 branches.
4. 100:2:2 `قَدْحًا` — `ق د ح` — 10 branches.
5. 100:3:1 `فَٱلْمُغِيرَٰتِ` — `غ ي ر` — 5 branches.
6. 100:3:2 `صُبْحًا` — `ص ب ح` — 10 branches.
7. 100:4:1 `فَأَثَرْنَ` — `ث و ر` — 7 branches.
8. 100:4:3 `نَقْعًا` — `ن ق ع` — 9 branches.
9. 100:5:1 `فَوَسَطْنَ` — `و س ط` — 7 branches.
10. 100:5:3 `جَمْعًا` — `ج م ع` — 13 branches.
11. 100:6:2 `ٱلْإِنسَٰنَ` — `ء ن س` — 6 branches.
12. 100:6:3 `لِرَبِّهِۦ` — `ر ب ب` — 17 branches.
13. 100:6:4 `لَكَنُودٌ` — `ك ن د` — 4 branches.
14. 100:7:4 `لَشَهِيدٌ` — `ش ه د` — 6 branches.
15. 100:8:2 `لِحُبِّ` — `ح ب ب` — 12 branches.
16. 100:8:3 `ٱلْخَيْرِ` — `خ ي ر` — 5 branches.
17. 100:8:4 `لَشَدِيدٌ` — `ش د د` — 6 branches.
18. 100:9:2 `يَعْلَمُ` — `ع ل م` — 6 branches.
19. 100:9:4 `بُعْثِرَ` — `ب ع ث ر` — 3 branches.
20. 100:9:7 `ٱلْقُبُورِ` — `ق ب ر` — 4 branches.
21. 100:10:1 `وَحُصِّلَ` — `ح ص ل` — 6 branches.
22. 100:10:4 `ٱلصُّدُورِ` — `ص د ر` — 6 branches.
23. 100:11:2 `رَبَّهُم` — `ر ب ب` — 17 branches.
24. 100:11:5 `لَّخَبِيرٌۢ` — `خ ب ر` — 6 branches.

Expected lexical seed passes: 190.

For every lexical seed pass below, the visited root dossiers are all other S100 root dossiers in this order:

`ع د و → ض ب ح → و ر ي → ق د ح → غ ي ر → ص ب ح → ث و ر → ن ق ع → و س ط → ج م ع → ء ن س → ر ب ب → ك ن د → ش ه د → ح ب ب → خ ي ر → ش د د → ع ل م → ب ع ث ر → ق ب ر → ح ص ل → ص د ر → خ ب ر`.

Within each seed row, `E` names only branches selected before freeze. Any root not named in `E` was nevertheless visited and rejected for construction in that seed because it did not transform, complete, or fork the image in a passage-local way. `C` and `K` name post-freeze corroborators and constraints from unused branches, morphology, attachments, sequence, and ayah boundaries.

Opening context: the sacred Arabic source includes `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ` as `verse_0`, but QAC returned no S100 ayah-0 rows. It is therefore retained only as non-seed opening context and is not used to initiate lexical seeds.

## Root dossier inventory used in the sweep

This inventory records the exact uncontaminated branch images used as the branch universe for S100.

### `ع د و`

- B001 `مجاوزة الحد والظلم` — يدخل فيه التعدي والاعتداء والعدوان وعدا على غيره والإغارة إذا كانت ظلما أو تجاوزا للحق
- B002 `العَدْو والحَضْر` — يدخل فيه الجري والحضر وعدو الفرس والعدو على الأقدام
- B003 `العَدُوّ والعداوة` — يدخل فيه العدو ضد الولي والعداوة والمعاداة وقوم أعداء أو عدا
- B004 `المجاوزة والاستثناء والصرف` — يدخل فيه عدا الشيء إذا جاوزه وما عدا في الاستثناء وعد عن الأمر إذا تجاوزه إلى غيره وتعدية الفعل
- B005 `العَدْوى في طلب الإنصاف` — يدخل فيه طلب المرء إلى وال أو قاض أن يعينه على من ظلمه وينتقم له منه
- B006 `العَدْوى في انتقال الداء` — يدخل فيه ما يقال إنه يعدي من جرب أو داء ومجاوزة العلة من صاحبها إلى غيره
- B007 `العَوادي والعادية الشاغلة` — يدخل فيه عوادي الدهر وعادية الشر وعدواء الشغل وما يشغل الإنسان أو يمنعه عن أمره
- B008 `العِداء في تعاقب الصيد` — يدخل فيه الموالاة بين صيدين أو إسقاط أحدهما إثر الآخر في طلق واحد
- B009 `العَداء والعُدوة في الجانب والطوار` — يدخل فيه طوار الشيء وما انقاد مع عرضه أو طوله وجانب الوادي وحافته وعداء النهر والجبل
- B010 `العَدْواء في صلابة المكان واضطرابه` — يدخل فيه الأرض اليابسة الصلبة والمكان غير المستوي أو غير المطمئن لمن قعد عليه
- B011 `العَدَوِيّة من نبات الصيف` — يدخل فيه نبات الصيف بعد ذهاب الربيع حين يخضر صغار الشجر فترعاه الإبل
- B012 `العَنْدَأْوَة في الالتواء والعسر` — يدخل فيه العندأوة إذا أريد بها التواء وعسر ونسبت إلى العداء

### `ض ب ح`

- B001 `صوت الضباح` — صوت الثعلب والهام والبوم والذئب والصدى وصوت أنفاس الخيل وأفواهها في العدو
- B002 `عدو ممدود الضبعين` — سير الخيل أو الإبل وعدوها مع مد الضبعين أو العدو الخفيف
- B003 `إحراق أعالي العود` — إحراق أعلى العود وحجارة القداحة وما مسته النار حتى يبدو مضبوحا
- B004 `تغير اللون إلى السواد` — انضباح اللون وتغيره إلى السواد قليلا بفعل النار أو الشمس
- B005 `الرماد` — الرماد المسمى الضبح

### `و ر ي`

- B001 `داء يأكل الجوف أو يصيب الرئة` — يدخل فيه الوري والورى داء الجوف أو الرئة، وأكل القيح للجوف، وإصابة الرئة، والجراحة التي يصيب سابرها الوري.
- B002 `نار كامنة تخرج من الزند` — يدخل فيه وري الزند وورى الزند وخروج ناره، وإيراء الزند أو النار، وإيقاد النار الخامدة ورفعها، وما يثقب به النار.
- B003 `زند يقدح نجاحا أو نصرة` — يدخل فيه قولهم فلان واري الزند إذا أنجح وأدرك طلبه، وورت بك زنادي إذا وجد منك نصحا وسماحة أو إعانة، ووريت عن فلان إذا نصرته ودفعت عنه.
- B004 `شحم وار وسمن ظاهر` — يدخل فيه اللحم الواري والشحم الواري والوري مثله، والناقة الوارية، واكتناز المخ.
- B005 `ستر الشيء وجعله وراء الظهور` — يدخل فيه وارى الشيء إذا أخفاه، وتوارى إذا استتر، ووري الخبر تورية إذا ستره وأظهر غيره، وإظهار غير المراد.
- B006 `الجانب الوراء: خلف أو أمام أو سوى` — يدخل فيه وراء بمعنى خلف، وقدام أو أمام في بعض الاستعمال، وما بعد الشيء أو سواه، والجانب الآخر من حجاب أو جدار، وصيغة وراءك للإغراء بالتأخر أو التنحي.
- B007 `ولد الولد يأتي من وراء الابن` — يدخل فيه الوراء أو وراء بمعنى ولد الولد أو ابن الابن.
- B008 `الورى: الخلق على ظهر الأرض` — يدخل فيه الورى بمعنى الخلق أو الأنام الذين على وجه الأرض في الوقت.

### `ق د ح`

- B001 `إيراء النار بالقدح` — قدح النار والزند والحجر والحديدة التي تورى بها النار
- B002 `نقر الشيء وعيبه` — قدح الشيء ونقر العظم وإحداث صدع أو وصمة في العود والعظم
- B003 `طعن في النسب` — القدح في نسب الرجل بالطعن فيه
- B004 `أكال الشجر والسن` — الأكال أو الدودة أو السواد الذي يقع في الشجر والأسنان
- B005 `غرف ما في القدر` — قدح القدر أو المرق والغرف بالمقدحة وما يبقى في أسفل القدر فيغرف بجهد والركي التي تغرف باليد
- B006 `قدح الشرب` — القدح من الآنية وأقداح الشرب وصانع الأقداح
- B007 `عود السهم والقدح في الميسر` — السهم قبل النصل والريش والقدح الواحد من قداح الميسر
- B008 `ضمر الفرس وغؤور العين` — ضمر الفرس حتى يصير مثل القدح وغؤور العين أو إخراج مائها الفاسد
- B009 `رخص أطراف النبت` — القداح من أطراف النبت والورق الغض ورخص النبات
- B010 `اقتداح الأمر بالنظر والتدبير` — اقتداح الأمر بالنظر فيه وتدبيره

### `غ ي ر`

- B001 `الصلاح والمنفعة بالميرة والسقي والإصلاح` — يدخل فيه ميرة الأهل ونفعهم، وسقي الأرض أو القوم بالغيث، وإصلاح الرحال أو شأن الراحلة.
- B002 `الغَيْر في الدية` — يدخل فيه اسم الغَيْر أو الغِيرة للدية، وأخذ الدية بدل القود.
- B003 `تغيير الصورة أو إبدال الشيء بغيره` — يدخل فيه تغيير الشيء فتغيره، وتغير الحال، وتبديل الشيء بغيره، ودفع المنكر بغيره من الحق، والمبادلة والبدل.
- B004 `الغَيْرة على الأهل` — يدخل فيه الغَيْرة المفتوحة على الأهل، ووصف الرجل أو المرأة بالغيور وغيران وغيرى، ولغة الغار في الغيرة.
- B005 `السوى والخلاف والاستثناء والنفي` — يدخل فيه كون الشيء سوى غيره وخلافه، واستعمال غير صفة أو اسما أو أداة استثناء، ومعنى لا، ونفي صورة أو ذات، وعموم الغيرين على المختلفين.

### `ص ب ح`

- B001 `الصبح وأول النهار` — الصبح والفجر والصباح والصبيحة وأول النهار والإصباح ووقت الإصباح
- B002 `الإتيان صباحا` — الإتيان صباحا والغدو بالخيل أو بالماء والتحية بصباح
- B003 `الصبوح` — الصبوح والشرب والأكل والسقي بالغداة وما يشرب أو يسقى أول النهار والمصابيح للأقداح
- B004 `يوم الصباح` — يوم الصباح للغارة والغدو بالخيل ونداء الاستغاثة صباحا
- B005 `المصباح والسراج` — المصباح والسراج والمسرجة ومقر السراج وما يستصبح به ومصابيح الكواكب
- B006 `الصُّبْحة والصباحة` — الحمرة أو اللون بين الحمرة والغبرة في الشعر والأسد والوجه الصبيح والصباحة والجمال والوضاءة
- B007 `الصُّبْحة نوما` — النوم بالغداة وحين يصبح المرء
- B008 `الناقة المصباح` — الناقة أو الإبل التي تبرك في مبركها ولا تنهض للرعي حتى تصبح أو يرتفع النهار
- B009 `ظروف الصباح` — أصبوحة كل يوم وذا صبوح وصبح خامسة ولصبح خامسة واللقاء أو الإتيان في صباح معين
- B010 `أصبح بمعنى صار` — أصبح إذا صار على حال والإصباح مصدرا للفعل

### `ث و ر`

- B001 `انبعاث الشيء وانتشاره ظاهرا` — يدخل فيه ثوران الغبار والسحاب والماء والجراد والحصبة والشفق وشعث الرأس إذا ظهر الشيء وانتشر بعد كمون أو سكون
- B002 `إثارة الشيء وتحريكه من موضعه` — يدخل فيه أثار الغبار أو الأرض، وإثارة التراب، واستثارة الأرنب، وإزعاج البرك وإنهاضها، وبحث علم القرآن على صورة إثارة المكنون
- B003 `هيجان إلى مواجهة أو غضب` — يدخل فيه الوثوب على الشخص، والمثاورة والمواثبة، والثورة بمعنى الهيج، وإظهار الشر أو هيجانه، وثوران الغضب
- B004 `الثور: ذكر البقر` — يدخل فيه الثور من البقر الوحشي والأهلي، والأنثى ثورة، وجموعه كالثيران والأثوار والثيرة
- B005 `ثورة الأقط: قطعة جامدة` — يدخل فيه الثور أو الثورة بمعنى قطعة، وخاصة القطعة العظيمة من الأقط وجمعها أثوار أو ثورة
- B006 `ثور اسما لمكان أو قوم أو برج` — يدخل فيه جبل ثور أو ثور أطحل، وبنو ثور أو قوم أو قبيلة ثور، وبرج الثور
- B007 `ثور الماء: طحلب يعلو السطح` — يدخل فيه الطحلب المسمى ثور الماء أو الثور الذي ظهر على متن الماء

### `ن ق ع`

- B001 `استقرار الماء وما ينقع فيه` — يدخل فيه اجتماع الماء وثباته وطول مكثه، واستنقاع الشيء في الماء، والإناء أو الموضع الذي ينقع فيه، والحوض أو البئر الكثيرة الماء وفضل ماء البئر، والنقوع والنقيع من دواء أو زبيب أو شراب أو صبغ، والأنقوعة لما سال إليه الماء أو وقبة الثريد.
- B002 `ماء ينقع الغلة ويروي` — يدخل فيه إرواء العطش والغلة، والشرب حتى يروى، والاشتفاء أو اطمئنان النفس بالخبر أو الرأي على طريق المجاز.
- B003 `نقيعة طعام أو نحر أو لبن` — يدخل فيه النقيعة طعاما للقادم أو عند الإملاك، وما ينحر من نهب أو عدة إبل، والمحْض من اللبن الذي يبرد.
- B004 `نقع الغبار المثار` — يدخل فيه النقع بمعنى الغبار، ولا سيما الغبار المرتفع أو المثار.
- B005 `نقع الصوت المرتفع` — يدخل فيه الصراخ وارتفاع الصوت وتتابعه أو دوامه، وصوت النعامة، وما قيس عليه من متكثر يصيح بما ليس عنده.
- B006 `سم ناقع ثابت أو قاتل` — يدخل فيه السم الناقع أو النقيع أو المنقوع إذا ثبت أو اجتمع في الأنياب، ويمتد في التهذيب إلى الموت الدائم والقتل.
- B007 `نقاع الأرض القيعان السهلة` — يدخل فيه النقاع جمع نقع: الأرض الحرة الطين الطيبة أو قيعان الأرض التي لا حزونة فيها ولا ارتفاع ولا انهباط.
- B008 `شراب بأنقع مجرب للموارد` — يدخل فيه المثل شراب بأنقع للرجل الذي جرب الأمور وعرف مواردها ومسالك السلامة فيها.
- B009 `نقعه بالشتم القبيح` — يدخل فيه قولهم نقعه بالشتم إذا شتمه شتما قبيحا.

### `و س ط`

- B001 `العدل والخيار في موضع الوسط` — يدخل فيه الوسط بمعنى العدل والخيار والقصد المصون عن الإفراط والتفريط، ومنه أمة وسطا، وأوسط القوم أو وسيط الحسب بمعنى خيارهم وأرفعهم محلا.
- B002 `موضع الوسط بين الأطراف` — يدخل فيه وسط الشيء أو الدار أو الرأس أو القوم، وما كان بين طرفين أو بين أجزاء مرتبة، وواسطة القلادة والأصبع الوسطى والصلاة الوسطى، واسم واسط إذا علل بالوقوع بين موضعين.
- B003 `الدخول أو الجعل في الوسط` — يدخل فيه وسط القوم أو أوسطهم أو توسطهم إذا دخل وسطهم، والتوسيط بمعنى جعل الشيء في الوسط.
- B004 `مرتبة وسطى بين الجيد والرديء` — يدخل فيه وصف الشيء أو الرجل بأنه وسط أي بين الجيد والرديء أو خارج عن حد الخير بحسب طرفي المقابلة.
- B005 `الوساطة بين الناس` — يدخل فيه التوسط بين الناس بمعنى الوساطة والسعي بين الأطراف.
- B006 `قطع الشيء نصفين` — يدخل فيه التوسيط بمعنى قطع الشيء نصفين.
- B007 `الوسوط: بيت أو ناقة مخصوصة` — يدخل فيه الوسوط كما عده Maqayis اسما لبيت من بيوت الشعر أكبر من المظلة، وقيل من النوق كالصفوف تملأ الإناء.

### `ج م ع`

- B001 `ضم المتفرق حتى يصير شيئا مجموعا` — يدخل فيه جمع الشيء أو المال أو القوم، وجعل المتفرق جميعا، وما جمع من مواضع شتى كنهب مجمع.
- B002 `جماعة اجتمعت أو أخلاط ضمتها الجهة` — يدخل فيه الجمع والجموع والجميع والجماعة والجماع إذا أريد بها جماعة الناس أو أخلاطهم أو الجيش.
- B003 `عزم محكم جمع الرأي بعد تفرقه` — يدخل فيه أجمع على الأمر، أجمع الأمر أو الكيد، الإجماع بمعنى الإعداد والعزيمة والإحكام، واجتماع الآراء على تدبير.
- B004 `موضع أو يوم أو نداء يجمع الناس` — يدخل فيه المجمع والموضع الذي يجتمع فيه الناس، وجمع للمزدلفة أو أيام منى، ويوم الجمعة ويوم الجمع، والمسجد الجامع، ونداء الصلاة جامعة، وفلاة مجمعة.
- B005 `قبضة الكف إذا ضمت الأصابع` — يدخل فيه جمع الكف، الضرب بجمع الكف، ملء الجمع، والقبضة أو جمعة التمر.
- B006 `اتصال الجماع والمجامعة` — يدخل فيه الجماع كناية عن النكاح، والمجامعة بمعنى المباضعة.
- B007 `حال المرأة أو الأنثى التي بقي حملها أو عذرها معها` — يدخل فيه ماتت المرأة بجمع أي وولدها في بطنها، أو عذراء لم تمسس، وفلانة عند زوجها بجمع إذا لم يصل إليها، وأتان جامع إذا حملت أول ما تحمل.
- B008 `القيد الذي يجمع اليدين إلى العنق` — يدخل فيه الجامعة والجوامع بمعنى الأغلال.
- B009 `اكتمال الشيء كله بلا تفرق أو نقص` — يدخل فيه جمعاء للبهيمة التي لم يذهب من بدنها شيء، وجميع وأجمعون وجمع في التوكيد والكلية، والرجل المجتمع أو الجميع في خلقه، والجارية جمعت الثياب.
- B010 `استجماع القوة أو السير حتى تتلاحق أجزاؤه` — يدخل فيه استجمع الفرس جريا، واستجمع السيل، واستجمع الأمر للمرء أي تهيأ له واجتمع.
- B011 `نخل دقل اجتمع من النوى لا يعرف اسمه` — يدخل فيه الجمع بمعنى الدقل أو كل لون من النخل خرج من النوى ولا يعرف اسمه.
- B012 `عظم الشيء كأنه جامع ممتلئ` — يدخل فيه قدر جماع أو جامعة بمعنى القدر العظيمة.
- B013 `ممالأة واجتماع مع غيرك على أمر` — يدخل فيه جامعت الرجل على الأمر إذا مالأته عليه، وجامعه على أمر إذا اجتمع معه.

### `ء ن س`

- B001 `ظهور الإنسان المخالف للتوحش والجن` — يدخل فيه الإنس والبشر والناس والأناسي والإنسان من حيث الجماعة أو الواحد، وما بالدار أنيس بمعنى أحد.
- B002 `إيناس الشيء برؤية أو إحساس أو سماع` — يدخل فيه آنس الشيء إذا أبصره أو رآه، وآنس الصوت إذا سمعه، وأحس الفزع أو وجد الشيء في نفسه، والاستئناس بمعنى النظر والتبصر.
- B003 `الأنس الذي يزيل الوحشة` — يدخل فيه أنس الإنسان بالشيء أو بفلان، المؤانسة والتأنيس، الأنيس وكل ما يؤنس به، الفرح بالقرب والحديث، والحيوان الأنوس غير العقور.
- B004 `الجانب الإنسي المقبل على الإنسان` — يدخل فيه إنسي الدابة والقوس وكل شيئين: ما يلي الإنسان أو يقبل على الراكب أو الرامي، في مقابلة الوحشي.
- B005 `إنسان العين وصورة الإنسان في السواد` — يدخل فيه إنسان العين: المثال أو الصبي الذي يرى في سواد العين، وما ألحقه تهذيب اللغة من الأنملة أو إنسان الكف.
- B006 `ابن الإنس للنفس والصفوة` — يدخل فيه كيف ابن إنسك للسؤال عن النفس، وفلان ابن أنس فلان لصفيه وخاصته، وما قاربه من الخدن والأنيس والخلص والجليس.

### `ر ب ب`

- B001 `ربوبية وملك وسيادة` — يدخل فيه الرب بمعنى الله تعالى، ومالك الشيء، وسيده المطاع، وصاحبه، ورب الدار والدابة والملك
- B002 `إصلاح وتربية وإتمام` — يدخل فيه رب الشيء إذا أصلحه وأتمه وقام عليه، ورب النعمة والصنيعة والضيعة والولد والصبي، والتربية حالا فحالا
- B003 `علم رباني` — يدخل فيه الرباني والربانيون بمعنى العلماء والحكماء وأهل العلم بالرب أو من يرب العلم ونفسه به
- B004 `ربة وجماعات كثيرة` — يدخل فيه الربة والجماعات الكثيرة، والربيون إذا فسروا بالألوف أو الجماعات، ورباب القبائل لاجتماعهم
- B005 `ربيب وربيبة ورابة` — يدخل فيه الربيب والربيبة للولد المربوب من زوج سابق، والراب والرابة لمن يقوم على أمره، والحاضنة
- B006 `رُبّ خاثر وإصلاح به` — يدخل فيه الرُّبّ الطلاء الخاثر أو ثفل السمن والزيت، والسقاء والنحي والأديم والدواء والطعام إذا جعل فيه الرُّبّ أو أصلح به
- B007 `لزوم وإقامة ودوام` — يدخل فيه رب أو أرب بالمكان إذا أقام، ومرب الإبل ومرابها، وأربت السحابة أو الجنوب إذا دامت، والإرباب بمعنى الدنو
- B008 `رباب السحاب` — يدخل فيه الرباب والربابة للسحاب، والسحاب المتعلق أو المركب بعضه على بعض، وما سمي بذلك لتربية النبات أو دوام المطر
- B009 `شاة رُبّى وحداثة` — يدخل فيه الشاة الرُّبّى والرباب لقرب العهد بالولادة أو لزوم البيت للبن، وربان الشيء بمعنى حدثانه وطراءته، وربى الشباب
- B010 `ربابة تجمع القداح` — يدخل فيه الربابة للجلدة أو الوعاء الذي تجمع فيه القداح أو سهام الميسر، وجماعة السهام نفسها
- B011 `ربابة عهد وميثاق` — يدخل فيه الربابة والرباب للعهد والميثاق والجوار، والأربة للمعاهدين، والرباب للعشور إذا جعل كالعهد
- B012 `ربة نبات` — يدخل فيه الربة والربب لضرب من الشجر أو النبت أو البقلة التي تبقى خضراء
- B013 `ماء رَبَب كثير` — يدخل فيه الربب للماء الكثير، ويقال للعذب، من جهة اجتماع الماء
- B014 `رَبْرَب قطيع` — يدخل فيه الربرب لقطيع بقر الوحش، وقيل لجماعة البقر أو الإبل
- B015 `حرف رب وربما` — يدخل فيه رب وربما وربت وربه كحرف خافض أو حرف معنى للتقليل، ودخول ما أو التاء أو الهاء عليه
- B016 `رُبَى حاجة وعقدة ونعمة` — يدخل فيه الربى بمعنى الحاجة، والرابة، والعقدة المحكمة، والنعمة والإحسان
- B017 `رباني الملاحين` — يدخل فيه الرباني لرئيس الملاحين

### `ك ن د`

- B001 `القطع والانفصال` — قطع الشيء وفصله ومنه قطع الحبل وقطع الشكر والمفارقة
- B002 `كفران النعمة والمودة` — الكنود وكند وامرأة كنود في كفر النعمة والمواصلة والمودة وعد المصائب ونسيان النعم والأثرة ومنع الرفد
- B003 `الأرض التي لا تنبت` — الأرض الكنود التي لا تنبت شيئا
- B004 `اسم كندة` — اسم كندة للحي اليماني وتعليله بالمفارقة

### `ش ه د`

- B001 `الحضور مع المشاهدة` — الحضور والمشاهدة والمعاينة والمحضر والمجمع ومواضع المناسك وحضور الزوج أو الشخص
- B002 `البيان بعلم` — الشهادة والخبر القاطع وأداء ما عند الشاهد والإعلام والبيان والإظهار والإقرار والحكم وما يقوم شاهدا أو شهيدا على غيره
- B005 `اللسان الشاهد` — الشاهد بمعنى اللسان والعبارة الظاهرة التي تبين عن صاحبها
- B006 `الخارج عند الولادة والإدراك` — الشهود والشاهد لما يخرج مع الولد أو على رأسه وآثار النتاج من دم أو سلى وأشهد للبلوغ بخروج المذي أو الحيض
- B007 `الشَّهْد في الشمع` — الشَّهْد والشَّهْدة للعسل ما دام في شمعه قبل العصر وجمعه شِهاد
- B008 `العلامة الشاهدة` — الشاهد لما يدل على وقت أو حال أو جودة مثل النجم وصلاة المغرب وشاهد جري الفرس

### `ح ب ب`

- B001 `الحبة التي تنبت وتحمل الحب` — يدخل فيه الحب والحبة للحنطة والشعير والبقول والرياحين، والحبة الواحدة، وما شبه بها كالقطعة والبرد والقرط من حبة.
- B002 `المحبة الملازمة للقلب` — يدخل فيه الحب والمحبة ونقيض البغض، والتحبيب، والمحبوب، والاستحباب بمعنى الإيثار، والمودة المتبادلة.
- B003 `صيغة المدح وغاية الرغبة` — يدخل فيه حبذا، وحبابك أن تفعل، ونعم وحبة وكرامة، وما جاء بصيغة مدح أو بلوغ الغاية في المحبة.
- B004 `حبة القلب سويداؤه` — يدخل فيه حبة القلب بمعنى سويدائه أو ثمرته أو العلقة السوداء داخله، وما صيغ كإصابة حبة القلب.
- B005 `البعير يلزم مكانه من عجز` — يدخل فيه أحب البعير، والبعير المحب، والإحباب في الإبل إذا وقف أو برك أو لزم مكانه من حسر أو مرض أو كسر.
- B006 `الري حتى الامتلاء` — يدخل فيه تحبب الحمار أو الإبل من الماء، وأول الري، وملء السقاء ونحوه حتى يمتلئ.
- B007 `الحب جرة عظيمة أو موضعها` — يدخل فيه الحب بمعنى الجرة الضخمة أو الخابية، وجمعه حباب وحببة، وما قيل في الخشبات التي توضع عليها الجرة.
- B008 `حباب الماء فقاقيعه وطرائقه` — يدخل فيه حباب الماء بمعنى الفقاقيع الطافية أو معظم الماء أو موجه وطرائقه، وما ألحق به من الطل على الشجر.
- B009 `حبب الأسنان انتظام كالدرر` — يدخل فيه الحبب وحبب الأسنان، أي تنضد الأسنان وظهور بياض الريق عليها.
- B010 `الحبحاب الصغير القصير` — يدخل فيه الحبحاب والحباحب بمعنى القصير أو الصغير الجسم، وما وصف به من هزال الإبل.
- B011 `نار الحباحب شرر لا ينتفع به` — يدخل فيه نار الحباحب، الشرر الضعيف من الحجارة أو حوافر الخيل، والذباب أو الطائر المضيء ليلا، والنار التي لا ينتفع بها.
- B012 `الحباب الحية أو الشيطان` — يدخل فيه الحباب بمعنى الحية، وما قيل في اسم الشيطان لكون الحية شيطانا.

### `خ ي ر`

- B001 `الميل إلى الخير النافع` — يدخل فيه الخير العام المرغوب فيه، وضد الشر، وما فيه نفع أو فضل أو صلاح، والخير المطلق والمقيد، ومقابلته للشر أو الضر.
- B002 `فضل الصلاح والاصطفاء` — يدخل فيه وصف الإنسان أو الشيء بأنه خير أو خيرة أو خيار أو أخيار، بمعنى الفضل والصلاح والجمال والميسم والاختيار من غير رذالة.
- B003 `طلب الخير بالاختيار والاستخارة` — يدخل فيه الخيار والاختيار والتخير والاستخارة وخار الله لك وخيرته بين شيئين، أي طلب ما هو خير، أو الاصطفاء، أو تفويض الخيار.
- B005 `الكرم والهبة` — يدخل فيه الخير بمعنى الكرم، والهبة والعطاء، وكثرة الخير في الشخص.
- B006 `استدراج الحيوان من جحره` — يدخل فيه استخارة الضبع أو اليربوع بجعل خشبة أو نحوها في موضع من جحره حتى يخرج من موضع آخر.

### `ش د د`

- B001 `شد العقد والوثاق` — عقد الشيء وإيثاقه وتقوية عقده وتقوية العضد والملك
- B002 `شدة القوة والصلابة` — القوة والصلابة والشجاعة وثبات القلب وشدة الحال والجوع والعذاب والتشديد وبذل الجهد والقدرة
- B003 `شد الحملة والعدو` — الحمل على العدو في القتال والعدو والحضر
- B004 `بلوغ الأشد` — بلوغ الأشد من القوة والرشد والحنكة والمعرفة واكتمال الشباب
- B005 `شد النهار وارتفاعه` — ارتفاع النهار
- B006 `شدة البخل` — الشديد والمتشدد بمعنى البخيل

### `ع ل م`

- B001 `انكشاف الشيء للعارف` — يدخل فيه العلم نقيض الجهل وإدراك الشيء ومعرفته والشعور بالخبر والتعلم والتعليم والإعلام والمغالبة بالعلم
- B002 `أثر يميز الشيء ويهدي إليه` — يدخل فيه العلامة والعلم والراية والجبل والمعلم ومعالم الطريق والحدود وعلم الثوب ورقمه وتعليم الفارس والثوب والقدح والعمامة والحناء إذا جعلت علامة
- B004 `شق ظاهر في الشفة العليا` — يدخل فيه العلم والشق في الشفة العليا ووصف الرجل أو البعير بالأعلم إذا كان الشق أو العلم في الموضع الأعلى
- B005 `ماء كثير مجتمع في عيلم` — يدخل فيه العيلم بمعنى البحر أو البئر الكثيرة الماء
- B006 `طائر جارح يسمى العلام` — يدخل فيه العلام بمعنى الصقر أو الباشق وما نسب إليه من العلامي
- B007 `ذكر الضباع يسمى العيلام` — يدخل فيه العيلام بمعنى ذكر الضباع

### `ب ع ث ر`

- B001 `قلب التراب وكشف المدفون` — يدخل فيه قلب التراب عن الشيء المدفون وإثارة ما في القبور وإخراجه وكشف الشيء المستور
- B002 `تبديد المتاع وقلب بعضه على بعض` — يدخل فيه تفريق المتاع وتبديده وقلب بعضه على بعض
- B003 `هدم الحوض وقلب أسفله أعلاه` — يدخل فيه هدم الحوض وجعل أسفله أعلاه

### `ق ب ر`

- B001 `مواراة الميت في القبر` — يدخل فيه القبر مدفن الميت ومقره، وقبر الميت أي دفنه وجعله في القبر، وأقبره أي جعل له قبرا أو أذن في قبره أو صيره ذا قبر، والمقبرة موضع القبور
- B002 `غموض الشيء وتطامنه` — يدخل فيه الغموض والتطامن في الشيء، والأرض القبور الغامضة، والنخلة القبور التي يكون حملها في سعفها، وجوف عود الطيب المتأكل، والمقبور المحصور في جلدة مصمتة
- B003 `القُبَّرة الطائر` — يدخل فيه القُبَّرة والقُبَّر اسما لطائر، وما يتصل بهما من لغة القنبرة والقنبراء
- B004 `طرف الأنف في الغضب` — يدخل فيه القبراة طرف الأنف، والقبيرة رأس القنفاء، وقولهم جاء رامعا قبراه أو فخا قبراه في الغضبان

### `ح ص ل`

- B001 `جمع الشيء حتى يظهر حاصله` — يدخل فيه حصلت الشيء تحصيلا، والحاصل والمحصول بمعنى ما بقي وثبت بعد ذهاب غيره، ورد الكلام إلى محصوله، وإظهار ما في الصدور أو حاصل الحساب.
- B002 `استخراج اللب أو النفيس من غلافه` — يدخل فيه التحصيل بمعنى إخراج اللب من القشور، وإخراج الذهب أو الفضة من حجر المعدن أو ترابه، وتمييز ما يحصل.
- B003 `البقية والحثالة بعد الرفع أو الفصل` — يدخل فيه الحاصل والمحصول والحصائل بمعنى البقايا، والحصالة لما يبقى في الأندر من الحب بعد رفع الحب، والحصيل بمعنى الحثالة.
- B004 `موضع يجتمع فيه الطعام في جوف الطائر` — يدخل فيه حوصلة الطائر وحواصل الطير، وملء الحوصلة، والطير المسمى الحوصلة، وما ألحقته العين من الحوصل للشاة واحونصال الطير.
- B005 `بلح حصل من النخلة قبل اشتداده` — يدخل فيه الحصل: البلح قبل أن يشتد وتظهر ثفاريقه، وقولهم أحصل النخل.
- B006 `وجع بطن الفرس من أكل التراب` — يدخل فيه حصل الفرس إذا اشتكى بطنه من أكل التراب أو تراب النبت.

### `ص د ر`

- B001 `الصدر الجارحة وما يتصل بها` — صدر الإنسان والحيوان وما أشرف من أعلاه، ووجع الصدر وإصابته، وما يغطى الصدر أو يسمه أو يشد عليه، وما سمي لقوة صدره
- B002 `المقدّم والأعلى والأول` — مقدّم الشيء وأعلاه وأوله، كصدر القناة والأمر والكتاب والمجلس والكلام، ومقدّم السهم، وسبق الفرس بصدره
- B003 `الصُّدور عن المورد` — الانصراف عن الماء أو البلاد أو كل أمر بعد وروده، والإصدار بمعنى الإرجاع، والطريق الصادر بأهله
- B004 `الأصل الذي تصدر عنه الأفعال` — المصدر بوصفه أصل الكلمة أو الفعل، وما يلحق به من اسم الموضع والزمان في الصدور
- B005 `المصادرة على مال` — مصادرة العامل أو غيره على مال يؤديه ويضمنه
- B006 `الطائفة من الشيء` — الصدر بمعنى طائفة من الشيء

### `خ ب ر`

- B001 `العلم بالخبر وباطن الأمر` — يدخل فيه الخبر والنبأ والإخبار والاستخبار والخبرة بمعنى الاختبار والمعرفة ببواطن الأمر والخبير العالم والمخبر الباطن لا المنظر
- B002 `لين الأرض ومائها` — يدخل فيه الخبراء والخبار والأرض الرخوة أو اللينة أو المنخفضة وما يجتمع فيها من ماء وشجر ومكان خَبِر
- B003 `إصلاح الأرض بالمخابرة` — يدخل فيه الخبير بمعنى الأكار والمخابرة والمؤاكرة والمزارعة بجزء معلوم مما يخرج من الأرض
- B004 `الغزر في المزادة والناقة` — يدخل فيه الخَبْر للمزادة العظيمة وتشبيه الناقة الغزيرة بها في السعة والغزر
- B005 `اللِّين في النبات والوبر والزبد` — يدخل فيه الخبير للنبات اللين والوبر وزبد أفواه الإبل أو ما يلقيه البعير من فيه
- B006 `القسمة في الشاة واللحم` — يدخل فيه الخُبْرة للشاة المشتركة التي يذبحها القوم ويقتسمون لحمها أو للنصيب من اللحم والسمك

## Reusable frozen models

These model labels are shorthand only; every lexical seed below still has its own pass.

- M1 kinetic-disclosure: rapid motion → breath → spark → stirred dust → center-entry → later hidden contents exposed.
- M2 breath-to-chest: audible exertion creates an expectation for body/interior/chest disclosure.
- M3 latent-fire: hidden fire released by striking becomes a model for hidden contents released from coverings.
- M4 dawn-threshold: morning/time threshold marks a sudden transition into exposure.
- M5 dust-earth reactivation: stirred dust in 100:4 reactivates as graves overturned in 100:9.
- M6 center-gathering: entering a gathered center reactivates as contents collected/extracted in 100:10.
- M7 human relational rupture: human before his Lord is marked by ingratitude/severance.
- M8 epistemic closure: witness/knowledge/inner expertise explains why closure occurs at `لَّخَبِيرٌ`.
- M9 inner motive: love of benefit/gift intensified inside the chest.
- M10 passive exposure: graves and chests are opened/collected without importing the opening agents as the passive agents.

## Exhaustive lexical seed passes

### 100:1:1 `وَٱلْعَٰدِيَٰتِ` — `ع د و`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS001 | `ع د و B001` | Overstepping/hostile excess. | `(E: ك ن د B002)`, `(E: ش د د B006)` | Human excess appears as ingratitude and miserliness. Predicts relational target. | `(C: ر ب ب B001 100:6/11)`, `(C: حبب B002)`, `(K: oath syntax does not itself assert ظلم)`. | medium |
| LS002 | `ع د و B002` | Running/rapid advance. | `(E: ض ب ح B001/B002)`, `(E: و ر ي B002)`, `(E: ق د ح B001)`, `(E: ث و ر B001/B002)`, `(E: ن ق ع B004)`, `(E: و س ط B003)`, `(E: ج م ع B002)` | M1. Predicts trace, center, and later exposure. | `(C: بعثر B001)`, `(C: حصل B001/B002)`, `(C: صدر B001)`, `(C: خبر B001)`, `(K: later passives do not reuse opening agents)`. | strong |
| LS003 | `ع د و B003` | Enemy/hostility. | `(E: ص ب ح B004)`, `(E: ش د د B003)`, `(E: ج م ع B002)` | Battle-colored fork: rapid morning confrontation entering a group. | `(C: وسط B003)`, `(K: no explicit enemy noun; remains a coloring of the kinetic model)`. | weak |
| LS004 | `ع د و B004` | Passing beyond/diversion/exception. | `(E: و س ط B003)` only as contrast. | Weak movement from boundary to middle. | `(K: no exception construction or “beyond” role; `فَوَسَطْنَ` selects middle-entry, not surpassing)`. | unlikely |
| LS005 | `ع د و B005` | Seeking legal redress. | none | Terminates: needs judge/petitioner/wrongdoer roles. | `(K: no qāḍī/authority petition structure; `رَبّ` is not introduced as court role)`. | unlikely |
| LS006 | `ع د و B006` | Disease transfer. | none | Terminates: contagion requires illness transfer. | `(K: و ر ي B001 and صدر B001 were visited but no disease event is supplied)`. | unlikely |
| LS007 | `ع د و B007` | Hindrances/distractions of time or evil. | `(E: ك ن د B002)` weakly | Human distracted from Lord by ingratitude. | `(C: حبب B002 + خير B001)`, `(K: cannot organize opening oath-chain)`. | weak |
| LS008 | `ع د و B008` | Successive hunting catch. | none | Terminates: prey/hunt sequence absent. | `(K: repeated فـ gives sequence but no hunting roles)`. | unlikely |
| LS009 | `ع د و B009` | Side/bank/edge. | none | Terminates as edge image. | `(K: وسط B002/B003 supplies middle, but no edge-to-middle contrast is grammatically marked)`. | unlikely |
| LS010 | `ع د و B010` | Hard uneven ground. | `(E: ن ق ع B004)` weakly as dust field | Ground texture model fails to predict passage. | `(K: no صلابة الأرض phrase; later graves are burial containers, not uneven terrain)`. | unlikely |
| LS011 | `ع د و B011` | Summer vegetation. | none | Terminates. | `(K: plant branches across خير/ربب/حبب were visited but no vegetation cycle is supplied)`. | unlikely |
| LS012 | `ع د و B012` | Twisting/difficulty. | none | Terminates. | `(K: no local عسر/التواء role)`. | unlikely |

### 100:1:2 `ضَبْحًا` — `ض ب ح`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS013 | `ض ب ح B001` | Panting/sound in running. | `(E: ع د و B002)`, `(E: ض ب ح B002)`, `(E: و ر ي B002)`, `(E: ق د ح B001)`, `(E: ث و ر B002)`, `(E: ن ق ع B004)` | M2. Predicts body/interior after sound and force. | `(C: صدر B001)`, `(C: حبب B004)`, `(C: خبر B001)`, `(K: ضَبْحًا remains manner, not independent subject)`. | medium-strong |
| LS014 | `ض ب ح B002` | Extended running with limbs. | `(E: ع د و B002)`, `(E: ض ب ح B001)`, `(E: و س ط B003)`, `(E: ج م ع B002)` | Stride-chain reaches a gathered center. | `(C: حصل B001)`, `(C: بعثر B001)`, `(K: stride needs opening `ع د و` carrier)`. | medium-strong |
| LS015 | `ض ب ح B003` | Burning upper wood/fire contact. | `(E: و ر ي B002)`, `(E: ق د ح B001)` | Fire-contact fork of M3. | `(C: حصل B002)`, `(K: local attachment points to sound/manner; fire dimension secondary)`. | weak |
| LS016 | `ض ب ح B004` | Slight blackening by fire/sun. | `(E: ق د ح B001)` weakly | Blackening after fire. | `(K: no blackened object, color, or sun-burning role)`. | unlikely |
| LS017 | `ض ب ح B005` | Ash. | none | Terminates. | `(K: ن قع B004 dust is not ash; no burned residue appears)`. | unlikely |

### 100:2:1 `فَٱلْمُورِيَٰتِ` — `و ر ي`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS018 | `و ر ي B001` | Inner disease/lung or belly injury. | `(E: صدر B001)` weakly | Possible interior-body injury image. | `(K: no illness, wound, or injury syntax; chest later is disclosure container, not disease)`. | weak |
| LS019 | `و ر ي B002` | Hidden fire emerging from stick. | `(E: ق دح B001)`, `(E: ضبح B003)`, `(E: ثور B002)`, `(E: نقع B004)` | M3. Predicts hidden content forced outward. | `(C: بعثر B001)`, `(C: حصل B002)`, `(C: صدر B001)`, `(C: خبر B001)`. | strong |
| LS020 | `و ر ي B003` | Fire-stick as success/help/nusra. | `(E: قدح B001)`, `(E: خير B005)` weakly | Assistance/success fork. | `(K: no explicit help, نصح, or نصرة role; spark remains stronger)`. | weak |
| LS021 | `و ر ي B004` | Visible fat/plumpness. | none | Terminates. | `(K: no fat/flesh/plump body role)`. | unlikely |
| LS022 | `و ر ي B005` | Concealing behind appearance. | `(E: بعثر B001)`, `(E: حصل B002)`, `(E: قبر B002)` | Concealment-to-exposure fork. | `(C: في القبور / في الصدور parallel)`, `(K: local `قَدْحًا` selects ignition branch more tightly)`. | medium |
| LS023 | `و ر ي B006` | Behind/beyond/other side. | none | Terminates. | `(K: no وراء or side relation marked; `وسط` gives middle not behind)`. | unlikely |
| LS024 | `و ر ي B007` | Grandchild/descendant. | none | Terminates. | `(K: no lineage or kinship roles)`. | unlikely |
| LS025 | `و ر ي B008` | Creatures on the earth. | `(E: ءنس B001)` weakly | Human/creation broadening. | `(K: too broad; does not predict sequence or closure)`. | unlikely |

### 100:2:2 `قَدْحًا` — `ق د ح`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS026 | `ق د ح B001` | Fire produced by striking. | `(E: و ر ي B002)`, `(E: ث و ر B002)`, `(E: ن ق ع B004)` | M3. Hidden spark becomes visible trace. | `(C: حصل B002)`, `(C: بعثر B001)`, `(C: خبر B001)`, `(K: attachment confines it to manner of `الموريات`)`. | strong |
| LS027 | `ق د ح B002` | Nicking/defect/blemish. | `(E: كند B001)` weakly | Rupture/defect model. | `(C: كند B002)`, `(K: no object is nicked; moral rupture secondary)`. | weak |
| LS028 | `ق د ح B003` | Attacking lineage. | none | Terminates. | `(K: no نسب or ancestry role)`. | unlikely |
| LS029 | `ق د ح B004` | Worm/decay in tree/tooth. | none | Terminates. | `(K: no tree/tooth/decay object)`. | unlikely |
| LS030 | `ق د ح B005` | Ladling from pot with effort. | `(E: حصل B001)` weakly | Extraction-from-container analogy. | `(K: no pot/ladle; later extraction is better supported by حصل B002)`. | weak |
| LS031 | `ق د ح B006` | Drinking cup. | none | Terminates. | `(K: no cup/drink construction)`. | unlikely |
| LS032 | `ق د ح B007` | Arrow shaft / maysir lot. | `(E: ر ب ب B010)` weakly | Lots/shafts fork. | `(K: no lot-casting or arrow syntax; not selected by `قَدْحًا`)`. | unlikely |
| LS033 | `ق د ح B008` | Lean horse / sunken eye. | `(E: عدو B002)`, `(E: ضبح B002)` weakly | Thin-runner coloring. | `(K: no emaciation or eye role)`. | weak |
| LS034 | `ق د ح B009` | Tender plant tips. | none | Terminates. | `(K: no plant field)`. | unlikely |
| LS035 | `ق د ح B010` | Deliberating an affair. | `(E: علم B001)` weakly | Cognitive consideration fork. | `(K: `يعلم` is later knowledge, not deliberative planning)`. | unlikely |

### 100:3:1 `فَٱلْمُغِيرَٰتِ` — `غ ي ر`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS036 | `غ ي ر B001` | Benefit/repair/provision. | `(E: خير B001)`, `(E: ربب B002)` weakly | Beneficial repair fork. | `(K: local participial position is in opening rush; branch does not explain dust/entry)`. | weak |
| LS037 | `غ ي ر B002` | Blood-money/substitute for retaliation. | none | Terminates. | `(K: no retaliation, compensation, or qawad role)`. | unlikely |
| LS038 | `غ ي ر B003` | Change/alteration. | `(E: صبح B004)`, `(E: عدو B002)`, `(E: ثور B001)` | M4 support: dawn change from stillness to exposure. | `(C: transition 100:5→100:6)`, `(K: does not by itself supply all raid/motion detail)`. | medium |
| LS039 | `غ ي ر B004` | Jealous guarding of family. | none | Terminates. | `(K: no family/ghayra frame)`. | unlikely |
| LS040 | `غ ي ر B005` | Otherness/exception/negation. | `(E: لا non-branch 100:9)` weakly | Negation/difference fork. | `(K: `أفلا` does not reactivate the opening participle strongly)`. | weak |

### 100:3:2 `صُبْحًا` — `ص ب ح`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS041 | `ص ب ح B001` | Dawn/first day. | `(E: عدو B002)`, `(E: غير B003)` | M4 time threshold. | `(C: يومئذ non-branch)`, `(C: علم B001)`, `(K: time marker alone not enough)`. | medium |
| LS042 | `ص ب ح B002` | Coming in the morning. | `(E: عدو B002)`, `(E: وسط B003)` | Morning arrival into center. | `(C: sequence 100:1→5)`, `(K: no separate coming-agent beyond opening chain)`. | weak |
| LS043 | `ص ب ح B003` | Morning drink/meal. | none | Terminates. | `(K: no drink/food; `نقع` water branches were rejected by local dust object)`. | unlikely |
| LS044 | `ص ب ح B004` | Morning attack/galloping morning. | `(E: عدو B002)`, `(E: ضبح B001)`, `(E: وسط B003)`, `(E: جمع B002)` | M4 plus battle-colored center-entry. | `(C: attachment 100:3 a1 time adverb)`, `(C: يومئذ closure)`, `(K: no explicit enemy noun)`. | medium-strong |
| LS045 | `ص ب ح B005` | Lamp/sirāj. | `(E: وري B002)`, `(E: قدح B001)` | Light/spark fork. | `(K: no lamp object; fire is already covered by `وري/قدح`)`. | weak |
| LS046 | `ص ب ح B006` | Redness/beauty. | none | Terminates. | `(K: no color/beauty role)`. | unlikely |
| LS047 | `ص ب ح B007` | Morning sleep. | none | Terminates. | `(K: opening chain is active, not sleep)`. | unlikely |
| LS048 | `ص ب ح B008` | Animal remaining until morning. | none | Terminates. | `(K: no staying animal; opening chain moves)`. | unlikely |
| LS049 | `ص ب ح B009` | Specific morning circumstances. | `(E: يومئذ non-branch)` weakly | Time-index fork. | `(K: too generic; lacks disclosure mechanics)`. | weak |
| LS050 | `ص ب ح B010` | Becoming a state. | `(E: غير B003)` weakly | State-change model. | `(K: no explicit becoming predicate in this local word)`. | weak |

### 100:4:1 `فَأَثَرْنَ` — `ث و ر`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS051 | `ث و ر B001` | Eruption/spreading after stillness. | `(E: عدو B002)`, `(E: نقع B004)`, `(E: وسط B003)`, `(E: جمع B002)` | M5. Predicts later earth exposure. | `(C: بعثر B001)`, `(C: قبر B001)`, `(C: حصل B001)`, `(K: dust is object/trace, not final agent)`. | strong |
| LS052 | `ث و ر B002` | Stirring dust/earth from place. | `(E: نقع B004)`, `(E: عدو B002)`, `(E: وري B002)`, `(E: قدح B001)` | M5 with earth-motion and hidden-release link. | `(C: بعثر B001)`, `(C: في القبور)`, `(C: حصل B002)`. | strong |
| LS053 | `ث و ر B003` | Rage/confrontational surge. | `(E: عدو B003)`, `(E: شدد B003)` | Violent confrontation fork. | `(K: no anger noun; remains subordinate to kinetic chain)`. | weak |
| LS054 | `ث و ر B004` | Bull. | none | Terminates. | `(K: no cattle role)`. | unlikely |
| LS055 | `ث و ر B005` | Solid lump of aqit. | none | Terminates. | `(K: no food/lump role)`. | unlikely |
| LS056 | `ث و ر B006` | Place/tribe/zodiac. | none | Terminates. | `(K: no proper name or zodiac role)`. | unlikely |
| LS057 | `ث و ر B007` | Algae on water surface. | `(E: نقع B001)` weakly | Water-surface fork. | `(K: local `نَقْعًا` is selected by dust branch, not water)`. | unlikely |

### 100:4:3 `نَقْعًا` — `ن ق ع`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS058 | `ن ق ع B001` | Settled water/soaking place. | `(E: حبب B006)` weakly | Water containment fork. | `(K: attachment makes `نَقْعًا` object raised by `أثرن`; dust branch wins)`. | unlikely |
| LS059 | `ن ق ع B002` | Quenching water. | `(E: خير B001)` weakly | Relief/quenching fork. | `(K: no thirst/relief structure)`. | unlikely |
| LS060 | `ن ق ع B003` | Food/slaughter/milk on arrival. | none | Terminates. | `(K: no food, milk, arrival-feast role)`. | unlikely |
| LS061 | `ن ق ع B004` | Raised dust. | `(E: ثور B001/B002)`, `(E: عدو B002)`, `(E: وسط B003)`, `(E: جمع B002)` | M5. Dust is visible trace of force. | `(C: بعثر B001)`, `(C: قبر B001)`, `(C: حصل B001)`, `(K: dust remains trace, not moral predicate)`. | strong |
| LS062 | `ن ق ع B005` | Raised/continued sound. | `(E: ضبح B001)`, `(E: عدو B002)` | Sound-chain fork. | `(C: صدر B001)`, `(K: local direct object is better explained as dust)`. | medium |
| LS063 | `ن ق ع B006` | Fixed/deadly poison. | none | Terminates. | `(K: no poison/venom/death-agent role)`. | unlikely |
| LS064 | `ن ق ع B007` | Easy flat ground. | `(E: عدو B010)` weakly | Terrain fork. | `(K: no flatness contrast; later graves not terrain quality)`. | unlikely |
| LS065 | `ن ق ع B008` | Experienced in safe routes/resources. | `(E: علم B001)` weakly | Knowledge-route fork. | `(K: no route/safety proverb role)`. | unlikely |
| LS066 | `ن ق ع B009` | Ugly reviling. | none | Terminates. | `(K: no insult or speech attack role)`. | unlikely |

### 100:5:1 `فَوَسَطْنَ` — `و س ط`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS067 | `و س ط B001` | Just/best middle. | `(E: خير B002)` weakly | Evaluative middle fork. | `(K: no justice/bestness predicate in 100:5)`. | weak |
| LS068 | `و س ط B002` | Middle place between edges. | `(E: جمع B002)`, `(E: حصل B001)`, `(E: صدر B001)` | Center/interior model. | `(C: في الصدور)`, `(K: less dynamic than B003)`. | medium |
| LS069 | `و س ط B003` | Entering/making the middle. | `(E: عدو B002)`, `(E: جمع B002)`, `(E: ثور B002)`, `(E: نقع B004)` | M6. Predicts later collection/extraction. | `(C: حصل B001/B002)`, `(C: صدر B001)`, `(C: خبر B001)`. | medium-strong |
| LS070 | `و س ط B004` | Average between good/bad. | `(E: خير B001)` weakly | Evaluation fork. | `(K: no “between good/bad” role)`. | unlikely |
| LS071 | `و س ط B005` | Mediation. | none | Terminates. | `(K: no mediator or negotiation structure)`. | unlikely |
| LS072 | `و س ط B006` | Cutting in half. | `(E: كند B001)` weakly | Severing fork. | `(K: no object cut in two; rupture handled by `كند`)`. | weak |
| LS073 | `و س ط B007` | Specific tent/camel. | none | Terminates. | `(K: no tent/camel object)`. | unlikely |

### 100:5:3 `جَمْعًا` — `ج م ع`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS074 | `ج م ع B001` | Joining dispersed things. | `(E: وسط B003)`, `(E: حصل B001)`, `(E: بعثر B002)` | M6 collection model. | `(C: حصل B001)`, `(C: في الصدور)`, `(K: `جمعًا` is entered object, not final collection alone)`. | medium-strong |
| LS075 | `ج م ع B002` | Gathered group/crowd. | `(E: وسط B003)`, `(E: عدو B002)`, `(E: صبح B004)` | M6 gathered-center model. | `(C: حصل B001)`, `(C: خبر B001)`. | medium-strong |
| LS076 | `ج م ع B003` | Firm resolve after divided views. | `(E: شدد B002)` weakly | Resolve/intensity fork. | `(K: no planning/opinion assembly)`. | weak |
| LS077 | `ج م ع B004` | Gathering place/day/call. | `(E: يومئذ non-branch)` weakly | Time/gathering fork. | `(K: no named place/day/call; 100:11 time adverb is closure only)`. | weak |
| LS078 | `ج م ع B005` | Closed fist/grip. | `(E: شدد B001)` weakly | Grip/binding fork. | `(K: no hand/fist object)`. | unlikely |
| LS079 | `ج م ع B006` | Sexual union. | none | Terminates. | `(K: no marital/sexual role)`. | unlikely |
| LS080 | `ج م ع B007` | Pregnancy/virginity retained. | none | Terminates. | `(K: no pregnancy/virginity role)`. | unlikely |
| LS081 | `ج م ع B008` | Shackle joining hands to neck. | `(E: شدد B001)` weakly | Restraint fork. | `(K: no shackle/restraint object)`. | unlikely |
| LS082 | `ج م ع B009` | Whole/completed without loss. | `(E: حصل B001)`, `(E: خبر B001)` | Completeness after collection. | `(C: حصل B001)`, `(K: not enough for opening action)`. | medium |
| LS083 | `ج م ع B010` | Strength/speed parts coming together. | `(E: عدو B002)`, `(E: شدد B002)` | Kinetic integration fork. | `(C: sequence 100:1→5)`, `(K: secondary to B002/B003)`. | medium |
| LS084 | `ج م ع B011` | Unnamed date-palm from seed. | none | Terminates. | `(K: no date-palm role)`. | unlikely |
| LS085 | `ج م ع B012` | Large full vessel/pot. | none | Terminates. | `(K: no vessel/pot role)`. | unlikely |
| LS086 | `ج م ع B013` | Collusion/joining with another. | `(E: كند B002)` weakly | Social alignment fork. | `(K: no collusion/mumālaʾa role)`. | weak |

### 100:6:2 `ٱلْإِنسَٰنَ` — `ء ن س`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS087 | `ء ن س B001` | Human/person. | `(E: ر ب ب B001/B002 100:6)`, `(E: كند B002)`, `(E: حبب B002)`, `(E: شدد B002)` | M7 human relational rupture. | `(C: صدر B001)`, `(C: حصل B001/B002)`, `(C: ر ب ب B001/B002 100:11)`, `(C: خبر B001)`. | strong |
| LS088 | `ء ن س B002` | Perceiving by sight/hearing/sensing. | `(E: شهد B001)`, `(E: علم B001)`, `(E: خبر B001)` | Human perception-to-knowledge fork. | `(C: أفلا يعلم)`, `(C: شهيد)`, `(K: surface `الإنسان` selects person more directly)`. | medium |
| LS089 | `ء ن س B003` | Familiarity removing loneliness. | `(E: ر ب ب B002)`, `(E: كند B002)` | Broken familiarity/gratitude model. | `(K: no explicit comfort/familiarity term; only relational contrast)`. | weak |
| LS090 | `ء ن س B004` | Human-facing side. | `(E: وسط B002)` weakly | Orientation/side fork. | `(K: no side-facing construction)`. | unlikely |
| LS091 | `ء ن س B005` | Pupil/image in eye. | `(E: شهد B001)` weakly | Seeing-image fork. | `(K: no eye/pupil noun; witness is stronger as knowledge)`. | weak |
| LS092 | `ء ن س B006` | Self/intimate companion. | `(E: صدر B001)`, `(E: حبب B002)` weakly | Inner-self fork. | `(C: في الصدور)`, `(K: branch is remote from surface `الإنسان`)`. | weak |

### 100:6:3 `لِرَبِّهِۦ` — `ر ب ب`, first occurrence

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS093 | `ر ب ب B001` | Lordship/ownership/mastery. | `(E: ءنس B001)`, `(E: كند B002)`, `(E: شهد B002)`, `(E: حبب B002)` | M7: human before Lord, relation exposed. | `(C: ر ب ب B001 100:11)`, `(C: خبر B001)`, `(K: not a motion-agent role)`. | strong |
| LS094 | `ر ب ب B002` | Nurture/repair/completion. | `(E: كند B002)`, `(E: خير B005)`, `(E: حبب B002)` | Ingratitude toward nurturer/giver. | `(C: حصل B001/B002)`, `(C: ر ب ب B002 100:11)`, `(K: repair is relational, not physical repair in opening scene)`. | strong |
| LS095 | `ر ب ب B003` | Rabbānī knowledge. | `(E: علم B001)`, `(E: خبر B001)` | Knowledge-of-Lord fork. | `(C: خبير closure)`, `(K: branch form not local to `رَبّ`)`. | weak |
| LS096 | `ر ب ب B004` | Multitudes/groups. | `(E: جمع B002)` weakly | Group/multitude fork. | `(K: 100:6 suffix is singular; branch does not explain predication)`. | unlikely |
| LS097 | `ر ب ب B005` | Rearing stepchild/caretaker. | `(E: ر ب ب B002)` weakly | Caretaking fork. | `(K: no family/custody role)`. | unlikely |
| LS098 | `ر ب ب B006` | Thick rubb/food repair. | none | Terminates. | `(K: no food/condiment role)`. | unlikely |
| LS099 | `ر ب ب B007` | Staying/continuance. | `(E: شدد B001)` weakly | Continuity/binding fork. | `(K: no residence/staying role)`. | weak |
| LS100 | `ر ب ب B008` | Layered cloud. | none | Terminates. | `(K: no cloud/rain field)`. | unlikely |
| LS101 | `ر ب ب B009` | Recent birth/newness. | none | Terminates. | `(K: no birth/newness role)`. | unlikely |
| LS102 | `ر ب ب B010` | Container collecting lots/arrows. | `(E: قدح B007)` weakly | Lots container fork. | `(K: no maysir/arrows in passage)`. | unlikely |
| LS103 | `ر ب ب B011` | Covenant/protection. | `(E: شهد B002)`, `(E: كند B002)` weakly | Broken covenant-coloring. | `(K: no explicit عهد/ميثاق; relation remains Lord/servant by local syntax)`. | weak |
| LS104 | `ر ب ب B012` | Green plant. | none | Terminates. | `(K: no plant role)`. | unlikely |
| LS105 | `ر ب ب B013` | Much water. | `(E: نقع B001)` weakly | Water branch fork. | `(K: local dust and graves/chests defeat water model)`. | unlikely |
| LS106 | `ر ب ب B014` | Herd/flock. | `(E: جمع B002)` weakly | Group animal fork. | `(K: no herd role)`. | unlikely |
| LS107 | `ر ب ب B015` | Particle `رُبَّ`. | none | Terminates. | `(K: not the word form here)`. | unlikely |
| LS108 | `ر ب ب B016` | Need/knot/blessing. | `(E: كند B002)`, `(E: خير B005)` | Blessing-ingratitude fork. | `(C: حبب B002)`, `(K: diffuse; B001/B002 are stronger)`. | weak |
| LS109 | `ر ب ب B017` | Chief of sailors. | none | Terminates. | `(K: no sea/navigation role)`. | unlikely |

### 100:6:4 `لَكَنُودٌ` — `ك ن د`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS110 | `ك ن د B001` | Cutting/separation. | `(E: ربب B001)`, `(E: كند B002)`, `(E: حبب B002)` | Relational severance. | `(C: ر ب ب 100:11)`, `(C: صدر B001)`, `(K: no literal cutting object)`. | medium |
| LS111 | `ك ن د B002` | Ingratitude for blessing/mutuality. | `(E: ربب B001/B002)`, `(E: خير B005)`, `(E: حبب B002)`, `(E: شدد B006)` | M7. Human relation to Lord is morally exposed. | `(C: شهد B002)`, `(C: حصل B001/B002)`, `(C: خبر B001)`. | strong |
| LS112 | `ك ن د B003` | Barren land. | `(E: خير B001)`, `(E: ربب B002)` weakly | Unproductive response to benefit. | `(K: no land/growth frame; useful only as weak analogy)`. | weak |
| LS113 | `ك ن د B004` | Kindah proper name. | none | Terminates. | `(K: no proper-name role)`. | unlikely |

### 100:7:4 `لَشَهِيدٌ` — `ش ه د`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS114 | `ش ه د B001` | Presence with seeing. | `(E: ءنس B002)`, `(E: علم B001)`, `(E: خبر B001)` | M8 visual/present witness. | `(C: على ذلك attachment)`, `(C: بعثر/حصل passives disclose object)`. | medium-strong |
| LS115 | `ش ه د B002` | Declaration/witnessing by knowledge. | `(E: علم B001)`, `(E: خبر B001)`, `(E: كند B002)` | M8 testimony/knowledge closure. | `(C: attachment 100:7 a2)`, `(C: خبر B001 closure)`. | strong |
| LS116 | `ش ه د B005` | Tongue/visible expression. | `(E: كند B002)` weakly | Expression of inner state. | `(K: no tongue/speech organ; `شهيد` is better B002)`. | weak |
| LS117 | `ش ه د B006` | Birth discharge / maturity sign. | none | Terminates. | `(K: no birth/maturity bodily sign)`. | unlikely |
| LS118 | `ش ه د B007` | Honey in wax before pressing. | `(E: حصل B002)` weakly | Sweet-in-covering extraction analogy. | `(K: no honey/wax; extraction already has direct branch)`. | unlikely |
| LS119 | `ش ه د B008` | Sign indicating time/state/quality. | `(E: علم B002)`, `(E: يومئذ non-branch)` | Sign/time fork. | `(C: opening dust/spark as marks)`, `(K: secondary to explicit witness B002)`. | medium |

### 100:8:2 `لِحُبِّ` — `ح ب ب`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS120 | `ح ب ب B001` | Seed/grain. | `(E: خير B001)`, `(E: حصل B002)` weakly | Growth/kernel fork. | `(K: no agriculture; inner-kernel better under B004)`. | unlikely |
| LS121 | `ح ب ب B002` | Love attached to heart. | `(E: خير B001/B005)`, `(E: شدد B002)`, `(E: كند B002)`, `(E: صدر B001)` | M9. Strong inner attachment to benefit/gift. | `(C: حصل B001/B002)`, `(C: خبر B001)`, `(K: does not generate opening chain alone)`. | medium-strong |
| LS122 | `ح ب ب B003` | Praise/extreme desire formula. | `(E: خير B001)`, `(E: شدد B002)` | Desire-intensity fork. | `(K: formulaic praise not local)`. | weak |
| LS123 | `ح ب ب B004` | Heart-kernel/inner black center. | `(E: حبب B002)`, `(E: صدر B001)`, `(E: حصل B002)` | M9 inner-locus model. | `(C: في الصدور)`, `(C: خبر B001)`. | medium-strong |
| LS124 | `ح ب ب B005` | Camel staying from weakness. | none | Terminates. | `(K: opening motion opposes staying; no weakness/stopping role)`. | unlikely |
| LS125 | `ح ب ب B006` | Drinking until full. | `(E: نقع B002)` weakly | Thirst/fullness fork. | `(K: no drinking object; water branches fail)`. | unlikely |
| LS126 | `ح ب ب B007` | Large jar. | none | Terminates. | `(K: later `في` containers are graves/chests, not jar)`. | unlikely |
| LS127 | `ح ب ب B008` | Water bubbles/waves. | none | Terminates. | `(K: no water-surface field)`. | unlikely |
| LS128 | `ح ب ب B009` | Teeth like pearls. | none | Terminates. | `(K: no teeth/mouth role)`. | unlikely |
| LS129 | `ح ب ب B010` | Small/short body. | none | Terminates. | `(K: no body-size role)`. | unlikely |
| LS130 | `ح ب ب B011` | Useless sparks. | `(E: وري B002)`, `(E: قدح B001)` weakly | Spark echo. | `(K: “useless” not locally supplied; main spark handled at 100:2)`. | weak |
| LS131 | `ح ب ب B012` | Snake/devil. | none | Terminates. | `(K: no snake/devil role)`. | unlikely |

### 100:8:3 `ٱلْخَيْرِ` — `خ ي ر`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS132 | `خ ي ر B001` | Desired beneficial good. | `(E: حبب B002)`, `(E: شدد B002)`, `(E: كند B002)` | M9 motive object. | `(C: صدر B001)`, `(C: حصل B001)`, `(K: not enough for opening chain)`. | medium-strong |
| LS133 | `خ ي ر B002` | Excellence/choice. | `(E: وسط B001)` weakly | Best/choice fork. | `(K: no selection/comparison role)`. | weak |
| LS134 | `خ ي ر B003` | Choosing/seeking good. | `(E: حبب B002)` weakly | Choice-desire fork. | `(K: passage states love/intensity, not choosing process)`. | weak |
| LS135 | `خ ي ر B005` | Generosity/gift. | `(E: ربب B002)`, `(E: كند B002)`, `(E: حبب B002)` | Gift-ingratitude model. | `(C: ر ب ب 100:11)`, `(K: gift sense is a motive-role, not whole passage model)`. | medium |
| LS136 | `خ ي ر B006` | Driving animal from burrow. | `(E: بعثر B001)` weakly | Hidden animal extraction fork. | `(K: no animal/burrow role; graves are not this branch)`. | unlikely |

### 100:8:4 `لَشَدِيدٌ` — `ش د د`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS137 | `ش د د B001` | Tightened knot/bond. | `(E: حبب B002)`, `(E: كند B001)`, `(E: ربب B001)` | Binding attachment / severed relation fork. | `(C: حب الخير attachment)`, `(K: no rope/knot object)`. | medium |
| LS138 | `ش د د B002` | Strength/intensity/firmness. | `(E: حبب B002)`, `(E: خير B001)`, `(E: كند B002)`, `(E: صدر B001)` | M9 intensity. | `(C: حصل B001/B002)`, `(C: خبر B001)`. | medium-strong |
| LS139 | `ش د د B003` | Charge/running against enemy. | `(E: عدو B002)`, `(E: صبح B004)`, `(E: جمع B002)` | Opening rush reactivation from later intensity. | `(K: in 100:8 syntax it modifies love, not attack)`. | medium |
| LS140 | `ش د د B004` | Maturity/full strength. | `(E: ءنس B001)` weakly | Human maturity fork. | `(K: no growth-to-maturity sequence)`. | unlikely |
| LS141 | `ش د د B005` | Height of day. | `(E: صبح B001)` weakly | Daytime threshold fork. | `(K: opening is morning, not high day)`. | unlikely |
| LS142 | `ش د د B006` | Miserliness. | `(E: حبب B002)`, `(E: خير B001/B005)`, `(E: كند B002)` | M9 narrowing: intense love of good as withholding. | `(C: كند B002)`, `(K: not the only dimension of شديد)`. | medium |

### 100:9:2 `يَعْلَمُ` — `ع ل م`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS143 | `ع ل م B001` | Knowing / disclosure to knower. | `(E: شهد B002)`, `(E: خبر B001)`, `(E: بعثر B001)`, `(E: حصل B001)` | M8. Knowing follows disclosure. | `(C: passive 100:9–10)`, `(C: في القبور / في الصدور)`. | strong |
| LS144 | `ع ل م B002` | Mark/sign guiding recognition. | `(E: شهد B008)`, `(E: نقع B004)`, `(E: قدح B001)` | Visible traces as signs. | `(C: dust/spark sequence)`, `(K: local verb sense is knowing, B001 stronger)`. | medium |
| LS145 | `ع ل م B004` | Visible cleft in upper lip. | none | Terminates. | `(K: no lip/cleft body mark)`. | unlikely |
| LS146 | `ع ل م B005` | Much water. | `(E: نقع B001)` weakly | Water mass fork. | `(K: water model defeated by dust/grave/chest structure)`. | unlikely |
| LS147 | `ع ل م B006` | Falcon/hawk. | none | Terminates. | `(K: no bird role)`. | unlikely |
| LS148 | `ع ل م B007` | Male hyena. | none | Terminates. | `(K: no hyena role)`. | unlikely |

### 100:9:4 `بُعْثِرَ` — `ب ع ث ر`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS149 | `ب ع ث ر B001` | Soil turned / buried exposed. | `(E: قبر B001/B002)`, `(E: ثور B002)`, `(E: نقع B004)`, `(E: حصل B002)`, `(E: خبر B001)` | M10. Later disclosure reactivates early earth/dust. | `(C: passive morphology)`, `(C: في القبور)`, `(K: opening agents not passive agents)`. | strong |
| LS150 | `ب ع ث ر B002` | Scattering goods / overturning one over another. | `(E: جمع B001)`, `(E: حصل B001)` | Dispersion-to-collection fork. | `(C: حصل B001)`, `(K: local complement `في القبور` makes B001 stronger)`. | medium |
| LS151 | `ب ع ث ر B003` | Demolishing basin, bottom over top. | `(E: قبر B002)` weakly | Inversion/overturning fork. | `(K: no basin; only inversion survives weakly)`. | weak |

### 100:9:7 `ٱلْقُبُورِ` — `ق ب ر`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS152 | `ق ب ر B001` | Grave/burial place. | `(E: بعثر B001)`, `(E: ثور B002)`, `(E: نقع B004)`, `(E: حصل B002)`, `(E: خبر B001)` | M10 outer container exposed. | `(C: في القبور attachment)`, `(C: parallel في الصدور)`. | strong |
| LS153 | `ق ب ر B002` | Hidden/depressed/enclosed. | `(E: بعثر B001)`, `(E: حصل B002)`, `(E: صدر B001)` | Hidden-container model. | `(C: في القبور / في الصدور)`, `(C: خبر B001)`. | medium-strong |
| LS154 | `ق ب ر B003` | Lark/bird. | none | Terminates. | `(K: no bird role)`. | unlikely |
| LS155 | `ق ب ر B004` | Nose-tip in anger. | none | Terminates. | `(K: no nose/anger role)`. | unlikely |

### 100:10:1 `وَحُصِّلَ` — `ح ص ل`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS156 | `ح ص ل B001` | Collecting until resultant appears. | `(E: جمع B001)`, `(E: صدر B001)`, `(E: خبر B001)`, `(E: بعثر B001)` | M10 collection/result. | `(C: ما في الصدور attachment)`, `(C: خبر closure)`. | strong |
| LS157 | `ح ص ل B002` | Extracting inner valuable from covering. | `(E: وري B002)`, `(E: قدح B001)`, `(E: قبر B002)`, `(E: صدر B001)`, `(E: خبر B001)` | M10 extraction; M3 reactivated. | `(C: في الصدور)`, `(C: passive morphology)`. | strong |
| LS158 | `ح ص ل B003` | Residue/chaff after separation. | `(E: كند B002)` weakly | Sorting residue fork. | `(K: no chaff/residue term; resultant collection stronger)`. | weak |
| LS159 | `ح ص ل B004` | Bird crop/food container. | `(E: صدر B001)` weakly | Bodily container fork. | `(K: no bird/food; chest direct)`. | unlikely |
| LS160 | `ح ص ل B005` | Unhardened dates. | none | Terminates. | `(K: no palm/date role)`. | unlikely |
| LS161 | `ح ص ل B006` | Horse belly pain from soil. | `(E: عدو B002)`, `(E: نقع B004)` weakly | Soil/body pathology fork. | `(K: no belly-pain diagnosis; remote)`. | unlikely |

### 100:10:4 `ٱلصُّدُورِ` — `ص د ر`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS162 | `ص د ر B001` | Chest/breast. | `(E: حصل B001/B002)`, `(E: حبب B002/B004)`, `(E: خبر B001)`, `(E: كند B002)` | M10 inner bodily container. | `(C: في الصدور attachment)`, `(C: خبير closure)`. | strong |
| LS163 | `ص د ر B002` | Front/top/first part. | `(E: وسط B002)`, `(E: حصل B001)` | Forepart/center fork. | `(K: `في الصدور` favors chest container over mere frontness)`. | medium |
| LS164 | `ص د ر B003` | Departure from watering-place. | `(E: نقع B002)`, `(E: صبح B003)` weakly | Water departure fork. | `(K: no water-source/departure role)`. | unlikely |
| LS165 | `ص د ر B004` | Source/origin from which acts issue. | `(E: حبب B002)`, `(E: كند B002)`, `(E: خبر B001)` | Inner-source model. | `(C: حصل ما في الصدور)`, `(K: surface plural strongly supports chest; source is secondary dimension)`. | medium |
| LS166 | `ص د ر B005` | Confiscating wealth. | `(E: خير B001)` weakly | Wealth-taking fork. | `(K: no confiscation/payment role)`. | unlikely |
| LS167 | `ص د ر B006` | Portion of a thing. | `(E: حصل B001)` weakly | Portion/result fork. | `(K: too generic)`. | unlikely |

### 100:11:2 `رَبَّهُم` — `ر ب ب`, second occurrence

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS168 | `ر ب ب B001` | Lordship/ownership/mastery at closure. | `(E: ربب B001 100:6)`, `(E: كند B002)`, `(E: خبر B001)`, `(E: علم B001)` | M7 closure: same Lord relation returns after exposure. | `(C: إن ربهم بهم يومئذ لخبير)`, `(C: 100:6→100:11 reactivation)`. | strong |
| LS169 | `ر ب ب B002` | Nurture/repair/completion at closure. | `(E: ربب B002 100:6)`, `(E: كند B002)`, `(E: خير B005)`, `(E: خبر B001)` | Nurturer/giver relation exposed. | `(C: حصل B001/B002)`, `(C: خبر B001)`. | strong |
| LS170 | `ر ب ب B003` | Rabbānī knowledge. | `(E: علم B001)`, `(E: خبر B001)` | Lord-knowledge fork. | `(C: خبير)`, `(K: branch form not surface-local)`. | medium |
| LS171 | `ر ب ب B004` | Multitudes/groups. | `(E: جمع B002)` weakly | Plural/group fork. | `(K: suffix `هم` plural exists but root branch does not explain final predicate)`. | weak |
| LS172 | `ر ب ب B005` | Rearing stepchild/caretaker. | none | Terminates. | `(K: no family/caretaker role)`. | unlikely |
| LS173 | `ر ب ب B006` | Thick rubb/food repair. | none | Terminates. | `(K: no food role)`. | unlikely |
| LS174 | `ر ب ب B007` | Staying/continuing. | `(E: يومئذ non-branch)` weakly | Temporal persistence fork. | `(K: final time adverb is event-time, not residence)`. | weak |
| LS175 | `ر ب ب B008` | Layered cloud. | none | Terminates. | `(K: no cloud role)`. | unlikely |
| LS176 | `ر ب ب B009` | Recent birth/newness. | none | Terminates. | `(K: no birth/newness role)`. | unlikely |
| LS177 | `ر ب ب B010` | Container for lots/arrows. | `(E: قدح B007)` weakly | Lots container fork. | `(K: no lots/arrows; repeated from first occurrence, still rejected)`. | unlikely |
| LS178 | `ر ب ب B011` | Covenant/protection. | `(E: كند B002)`, `(E: شهد B002)` weakly | Broken covenant-coloring at closure. | `(K: no explicit عهد; Lordship branch stronger)`. | weak |
| LS179 | `ر ب ب B012` | Green plant. | none | Terminates. | `(K: no plant role)`. | unlikely |
| LS180 | `ر ب ب B013` | Much water. | none | Terminates. | `(K: no water field)`. | unlikely |
| LS181 | `ر ب ب B014` | Herd/flock. | none | Terminates. | `(K: no herd role)`. | unlikely |
| LS182 | `ر ب ب B015` | Particle `رُبَّ`. | none | Terminates. | `(K: not the form)`. | unlikely |
| LS183 | `ر ب ب B016` | Need/knot/blessing. | `(E: كند B002)`, `(E: خير B005)` weakly | Blessing/need coloring. | `(C: حبب B002)`, `(K: diffuse; B001/B002 dominate)`. | weak |
| LS184 | `ر ب ب B017` | Chief of sailors. | none | Terminates. | `(K: no nautical role)`. | unlikely |

### 100:11:5 `لَّخَبِيرٌۢ` — `خ ب ر`

| ID | Seed | Initial image | E before freeze | Frozen model / predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| LS185 | `خ ب ر B001` | Knowledge of report and inner matter. | `(E: علم B001)`, `(E: شهد B002)`, `(E: حصل B001/B002)`, `(E: صدر B001)`, `(E: ربب B001 100:11)` | M8/M10 closure: hidden contents known. | `(C: بهم attachment)`, `(C: يومئذ time)`, `(C: 100:9–10 passives)`. | strong |
| LS186 | `خ ب ر B002` | Soft/moist low land. | `(E: نقع B001)` weakly | Moist-land fork. | `(K: no moist ground; dust and graves/chests dominate)`. | unlikely |
| LS187 | `خ ب ر B003` | Sharecropping/cultivating land. | `(E: خير B001)` weakly | Cultivation fork. | `(K: no agriculture/land contract role)`. | unlikely |
| LS188 | `خ ب ر B004` | Full wineskin / abundant she-camel. | none | Terminates. | `(K: no wineskin/abundance animal role)`. | unlikely |
| LS189 | `خ ب ر B005` | Soft plant/hair/foam. | none | Terminates. | `(K: no soft plant/foam role)`. | unlikely |
| LS190 | `خ ب ر B006` | Shared slaughtered meat/portion. | `(E: جمع B001)` weakly | Division/portion fork. | `(K: no meat/division role; `خبر B001` is decisive closure)`. | unlikely |

## Exhaustive constructional, morphosyntactic, and temporal seed passes

The constructional sweep uses only actual S100 constructions from QAC and `attachments.tsv`. Construction rows do not create new lexical meanings; they test structural roles.

| ID | Seed construction | Initial image | Generating set before freeze | Predictions | C/K after freeze | Grade |
| --- | --- | --- | --- | --- | --- | --- |
| CS001 | Basmala opening context | Invocation/opening frame only; not a seed source. | none | May constrain divine-source closure only if needed. | `(K: QAC has no S100 ayah-0 rows; no lexical seed initiated)`. | not graded |
| CS002 | Oath particle governing `وَٱلْعَٰدِيَٰتِ` | Opening oath activates focused, solemn exposure. | attachment 100:1 a1 | Later predications should be read as oath-supported assertions. | `(C: إن/لـ emphatic predications)`, `(K: oath does not identify the agents beyond text)`. | medium-strong |
| CS003 | `ٱلْعَٰدِيَٰتِ ضَبْحًا` | Agent plus manner sound. | attachment 100:1 a2 | Motion should carry audible exertion. | `(C: ض ب ح B001/B002)`, `(K: manner is not separate agent)`. | strong |
| CS004 | `فَٱلْمُورِيَٰتِ` after 100:1 | Sequential escalation. | `فـ` + active participle | The second image should continue rather than restart. | `(C: و ر ي B002 + ق د ح B001)`. | strong |
| CS005 | `ٱلْمُورِيَٰتِ قَدْحًا` | Fire-producing manner. | attachment 100:2 a1 | Hidden energy becomes visible by contact. | `(C: ح ص ل B002 later extraction)`. | strong |
| CS006 | `فَٱلْمُغِيرَٰتِ` after spark line | Another sequential escalation. | `فـ` + active participle | A threshold arrival/change follows. | `(C: صبح B004)`, `(K: غ ي ر dossier gives change more directly than raid)`. | medium |
| CS007 | `صُبْحًا` time adverb | Dawn/time threshold. | attachment 100:3 a1 | Later time marker may close disclosure. | `(C: يومئذ)`. | medium-strong |
| CS008 | Feminine plural active participle chain | Repeated plural agents. | 100:1–3 morphology | Continuity across first three images. | `(C: 100:4–5 feminine plural finite verbs)`. | strong |
| CS009 | `فَأَثَرْنَ` finite perfect | Event changes from labels to action. | QAC Form IV, 3FP | The chain should now produce an object. | `(C: نقعًا direct object)`. | strong |
| CS010 | `بِهِۦ` after `أَثَرْنَ` | Instrument/medium/reference carrier. | attachment 100:4 a1 | May link dust-raising to next entry. | `(C: repeated بِهِۦ in 100:5)`, `(K: antecedent not resolved by permitted resources)`. | medium |
| CS011 | `نَقْعًا` direct object | Visible trace/object of stirring. | attachment 100:4 a2 | Dust/trace can be reactivated by later earth. | `(C: بعثر B001 + قبر B001)`. | strong |
| CS012 | `فَوَسَطْنَ` finite perfect | Chain enters a center. | QAC 3FP + `فـ` | A target/interior should be supplied. | `(C: جمعًا direct object)`. | strong |
| CS013 | repeated `بِهِۦ` after `وَسَطْنَ` | Same carrier/reference persists. | attachment 100:5 a1 | Dust-raising and center-entry are linked. | `(K: structural only; no new lexical meaning)`. | medium |
| CS014 | `جَمْعًا` direct object | Gathered target entered. | attachment 100:5 a2 | Later collection/extraction may reactivate it. | `(C: حصل B001)`. | strong |
| CS015 | Whole 100:1–5 `فـ` chain | Ordered avalanche: motion → sound → spark → time → dust → center. | CS003–CS014 | Later should reorganize this as disclosure mechanics. | `(C: بعثر/حصل/خبر sequence)`. | strong |
| CS016 | Ayah boundary 100:5→100:6 | Abrupt turn from scene to human predication. | boundary + `إِنَّ` | The first scene should serve comparator/reactivator for human condition. | `(C: كند B002)`, `(C: حبب B002)`, `(K: not simple agent identity)`. | strong |
| CS017 | `إِنَّ ٱلْإِنسَٰنَ` | Human introduced as governed subject. | attachment 100:6 a1 | Human interior/relation will be predicated. | `(C: ء ن س B001)`. | strong |
| CS018 | `لِرَبِّهِۦ` target relation | Predication is with respect to his Lord. | attachment 100:6 a3 + idafa a2 | Later `رَبَّهُم` should reactivate relation. | `(C: ر ب ب B001/B002 100:11)`. | strong |
| CS019 | `لَكَنُودٌ` emphatic predicate | Fixed human relational defect. | attachment 100:6 a4 + emphatic lām | Witness and motive should follow. | `(C: شهد B002)`, `(C: حبب/خير/شدد)`. | strong |
| CS020 | `وَإِنَّهُ` pronoun continuity | Same human referent continues. | QAC pronoun + attachment 100:7 a1 | Witness applies to the human predicate. | `(K: pronoun not reassigned to opening plural agents)`. | strong |
| CS021 | `عَلَىٰ ذَٰلِكَ` complement | Matter over which witness applies. | attachment 100:7 a2 | Prior defect becomes explicit object of witness. | `(C: شهد B002)`. | strong |
| CS022 | `لَشَهِيدٌ` predicate | Witness/manifestation role. | attachment 100:7 a3 | Knowledge chain will intensify. | `(C: علم B001, خبر B001)`. | strong |
| CS023 | `وَإِنَّهُ لِحُبِّ` | Same referent plus motive prepositional relation. | attachment 100:8 a1/a2 | Love supplies inner reason for defect. | `(C: حبب B002/B004)`. | strong |
| CS024 | `حُبِّ ٱلْخَيْرِ` idafa | Object of love constrained to `خير`. | attachment 100:8 a3 | Good/benefit/gift should sharpen motive. | `(C: خير B001/B005)`. | strong |
| CS025 | `لَشَدِيدٌ` predicate | Intensity predicated with respect to love. | attachment 100:8 a4 | Inner motive is not mild; it is forceful. | `(C: شدد B002/B006)`, `(K: not attack by syntax)`. | strong |
| CS026 | `أَفَلَا يَعْلَمُ` | Interrogative/negation opens knowledge test. | QAC particles + `علم` | Hidden things should become knowable. | `(C: بعثر/حصل passives)`. | strong |
| CS027 | `إِذَا بُعْثِرَ...` temporal clause | Knowledge located at disclosure time. | attachment 100:9 a1 | Final time marker may close the event. | `(C: يومئذ 100:11)`. | strong |
| CS028 | `بُعْثِرَ` passive + `مَا` subject | Hidden contents are exposed without named agent. | attachment 100:9 a2 + passive voice | Do not import opening plural agents as passive agents. | `(K: passive voice constraint)`. | strong |
| CS029 | `فِى ٱلْقُبُورِ` complement | Outer buried container. | attachment 100:9 a3 | Early dust/earth reactivates. | `(C: ثور B002, نقع B004, قبر B001)`. | strong |
| CS030 | `وَحُصِّلَ` coordination after `بُعْثِرَ` | Second disclosure, now collecting/extracting. | `و` + passive Form II | Outer disclosure should pair with inner disclosure. | `(C: حصل B001/B002)`. | strong |
| CS031 | `حُصِّلَ` passive + `مَا` subject | Contents collected/extracted without named agent. | attachment 100:10 a1 + passive voice | Final knower receives exposed contents. | `(C: خبر B001)`. | strong |
| CS032 | `فِى ٱلصُّدُورِ` complement | Inner bodily container. | attachment 100:10 a2 | Human motive and relation are now exposed. | `(C: صدر B001, حبب B002, كند B002)`. | strong |
| CS033 | Parallel `مَا فِى القبور / مَا فِى الصدور` | Outer container paired with inner container. | attachments 100:9 a3 and 100:10 a2 | Early earth scene and human interior converge. | `(C: قبر B001/B002 + صدر B001)`, `(K: containers remain distinct)`. | strong |
| CS034 | Final `إِنَّ رَبَّهُم` | Lord relation returns as subject. | attachment 100:11 a1/a2 | 100:6 `لربه` reactivated. | `(C: ربب B001/B002 two occurrences)`. | strong |
| CS035 | `بِهِمْ ... خَبِيرٌ` | Humans become object/reference of inner knowledge. | attachment 100:11 a3 | Closure occurs when hidden contents are known. | `(C: خبر B001)`. | strong |
| CS036 | `يَوْمَئِذٍ` with `خَبِيرٌ` | Knowledge is indexed to that disclosure day/time. | attachment 100:11 a4 | Time chain from `صبحًا` to final event closes. | `(C: صبح B001/B004 as weak time reactivation)`. | medium-strong |
| CS037 | `لَّخَبِيرٌ` final predicate | Final epistemic closure. | attachment 100:11 a5 + emphatic lām | Passage closes because no hidden object remains. | `(C: خ ب ر B001)`, `(C: passive disclosure 100:9–10)`. | strong |

## Post-creation exhaustiveness self-audit

Expected lexical seed rows: 190. Present lexical seed rows: 190 (`LS001` through `LS190`).

Expected constructional/morphosyntactic/temporal seed rows: 37. Present construction rows: 37 (`CS001` through `CS037`).

Checks performed conceptually before finalizing this file:

- Every rooted occurrence from QAC order is represented.
- The repeated `ر ب ب` occurrence is represented twice, not collapsed.
- Every uncontaminated branch returned for each S100 root is assigned exactly one seed row per occurrence.
- Every row records an initial image, selected or rejected expansion, freeze model/prediction, post-freeze corroboration/constraint, and grade.
- Constructional seeds include the actual attachment rows and the major temporal/acoustic/ayah-boundary patterns.

## Final synthesis retained after exhaustive sweep

The exhaustive sweep still converges on a compact secondary model:

`rapid force → breath/sound → latent fire released → dawn threshold → earth/dust stirred → gathered center entered → human relation to Lord exposed as ingratitude/intense attachment → graves and chests opened/collected → Lord knows the inner matter`.

The strongest seeds are not isolated theme matches. They succeed because they preserve the order of activation and then explain backward reactivation: `ث و ر / ن ق ع` become newly relevant at `بُعْثِرَ مَا فِى ٱلْقُبُورِ`; `ج م ع / و س ط` become newly relevant at `حُصِّلَ مَا فِى ٱلصُّدُورِ`; `ر ب ب / ك ن د / ح ب ب / خ ي ر / ش د د` become newly relevant when the final `رَبَّهُم ... لَّخَبِيرٌ` closes the human interior under divine knowledge.

The many unlikely seeds are also necessary to the result: they prevent the synthesis from becoming a generalized root-cloud and show where the passage itself stops the avalanche.
