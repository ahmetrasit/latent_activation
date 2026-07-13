# Stage 1 Pass 2 — S100 comparator test lane

Assigned passage: S100  
Sacred Arabic source: `resources/quran/surah_100.json`  
Prompt followed: `v1/prompts/stage1.md`  
Output: `v1/outputs/100_comparator/stage1_test_pass2.md`

## Source boundary

Only the sacred Arabic text, QAC rows for S100:1–11, S100 attachment rows, and uncontaminated furuq v4 branch dossiers for roots in S100:1–11 were used. No prior output file, translation, tafsir, hadith, web source, or external interpretation was read.

The sacred JSON contains the basmala as `verse_0`; QAC had no S100 ayah-0 rows, so it is visible opening context only and is not used to initiate seeds.

## Root cause of the Pass 1 limitation

The limitation was methodological, not data availability. Pass 1 did a synthesis-first reduction: it found a small set of convergent passage-scale images and then cited only the roots and branches that actively entered those findings. That hid the control sweep and made failed or weak seeds look absent. It also collapsed occurrence × branch seed passes into group summaries, so words that did not join the strongest findings were not given equal visible treatment.

Correction in Pass 2:

- restart from the first rooted word, `100:1:1 وَٱلْعَٰدِيَٰتِ`;
- initiate each occurrence × accepted branch as its own seed pass;
- initiate each eligible constructional, morphosyntactic, and temporal seed;
- in every lexical seed pass, visit the same complete S100 root dossier set before selecting, rejecting, freezing, and testing;
- record weak, unlikely, and defeated image-branches explicitly.

## Exhaustive inventory

Rooted occurrences in passage order:

| occurrence | rooted word | root | accepted branches | lexical seed count |
| --- | --- | --- | ---: | ---: |
| 100:1:1 | وَٱلْعَٰدِيَٰتِ | ع د و | 12 | 12 |
| 100:1:2 | ضَبْحًا | ض ب ح | 5 | 5 |
| 100:2:1 | فَٱلْمُورِيَٰتِ | و ر ي | 8 | 8 |
| 100:2:2 | قَدْحًا | ق د ح | 10 | 10 |
| 100:3:1 | فَٱلْمُغِيرَٰتِ | غ ي ر | 5 | 5 |
| 100:3:2 | صُبْحًا | ص ب ح | 10 | 10 |
| 100:4:1 | فَأَثَرْنَ | ث و ر | 7 | 7 |
| 100:4:3 | نَقْعًا | ن ق ع | 9 | 9 |
| 100:5:1 | فَوَسَطْنَ | و س ط | 7 | 7 |
| 100:5:3 | جَمْعًا | ج م ع | 13 | 13 |
| 100:6:2 | ٱلْإِنسَٰنَ | ء ن س | 6 | 6 |
| 100:6:3 | لِرَبِّهِۦ | ر ب ب | 17 | 17 |
| 100:6:4 | لَكَنُودٌ | ك ن د | 4 | 4 |
| 100:7:4 | لَشَهِيدٌ | ش ه د | 6 | 6 |
| 100:8:2 | لِحُبِّ | ح ب ب | 12 | 12 |
| 100:8:3 | ٱلْخَيْرِ | خ ي ر | 5 | 5 |
| 100:8:4 | لَشَدِيدٌ | ش د د | 6 | 6 |
| 100:9:2 | يَعْلَمُ | ع ل م | 6 | 6 |
| 100:9:4 | بُعْثِرَ | ب ع ث ر | 3 | 3 |
| 100:9:7 | ٱلْقُبُورِ | ق ب ر | 4 | 4 |
| 100:10:1 | وَحُصِّلَ | ح ص ل | 6 | 6 |
| 100:10:4 | ٱلصُّدُورِ | ص د ر | 6 | 6 |
| 100:11:2 | رَبَّهُم | ر ب ب | 17 | 17 |
| 100:11:5 | لَّخَبِيرٌ | خ ب ر | 6 | 6 |

Total lexical seed passes: 190.

Root dossiers visited for every lexical seed pass: `ع د و، ض ب ح، و ر ي، ق د ح، غ ي ر، ص ب ح، ث و ر، ن ق ع، و س ط، ج م ع، ء ن س، ر ب ب، ك ن د، ش ه د، ح ب ب، خ ي ر، ش د د، ع ل م، ب ع ث ر، ق ب ر، ح ص ل، ص د ر، خ ب ر`.

## Root-dossier ledger used in every lexical sweep

This ledger preserves the uncontaminated furuq fields used during the sweep: `root_norm / branch_id / branch_image_ar — what_is_ar`.

### `ء ن س`

- `B001` ظهور الإنسان المخالف للتوحش والجن — يدخل فيه الإنس والبشر والناس والأناسي والإنسان من حيث الجماعة أو الواحد، وما بالدار أنيس بمعنى أحد.
- `B002` إيناس الشيء برؤية أو إحساس أو سماع — يدخل فيه آنس الشيء إذا أبصره أو رآه، وآنس الصوت إذا سمعه، وأحس الفزع أو وجد الشيء في نفسه، والاستئناس بمعنى النظر والتبصر.
- `B003` الأنس الذي يزيل الوحشة — يدخل فيه أنس الإنسان بالشيء أو بفلان، المؤانسة والتأنيس، الأنيس وكل ما يؤنس به، الفرح بالقرب والحديث، والحيوان الأنوس غير العقور.
- `B004` الجانب الإنسي المقبل على الإنسان — يدخل فيه إنسي الدابة والقوس وكل شيئين: ما يلي الإنسان أو يقبل على الراكب أو الرامي، في مقابلة الوحشي.
- `B005` إنسان العين وصورة الإنسان في السواد — يدخل فيه إنسان العين: المثال أو الصبي الذي يرى في سواد العين، وما ألحقه تهذيب اللغة من الأنملة أو إنسان الكف.
- `B006` ابن الإنس للنفس والصفوة — يدخل فيه كيف ابن إنسك للسؤال عن النفس، وفلان ابن أنس فلان لصفيه وخاصته، وما قاربه من الخدن والأنيس والخلص والجليس.

### `ب ع ث ر`

- `B001` قلب التراب وكشف المدفون — يدخل فيه قلب التراب عن الشيء المدفون وإثارة ما في القبور وإخراجه وكشف الشيء المستور
- `B002` تبديد المتاع وقلب بعضه على بعض — يدخل فيه تفريق المتاع وتبديده وقلب بعضه على بعض
- `B003` هدم الحوض وقلب أسفله أعلاه — يدخل فيه هدم الحوض وجعل أسفله أعلاه

### `ث و ر`

- `B001` انبعاث الشيء وانتشاره ظاهرا — يدخل فيه ثوران الغبار والسحاب والماء والجراد والحصبة والشفق وشعث الرأس إذا ظهر الشيء وانتشر بعد كمون أو سكون
- `B002` إثارة الشيء وتحريكه من موضعه — يدخل فيه أثار الغبار أو الأرض، وإثارة التراب، واستثارة الأرنب، وإزعاج البرك وإنهاضها، وبحث علم القرآن على صورة إثارة المكنون
- `B003` هيجان إلى مواجهة أو غضب — يدخل فيه الوثوب على الشخص، والمثاورة والمواثبة، والثورة بمعنى الهيج، وإظهار الشر أو هيجانه، وثوران الغضب
- `B004` الثور: ذكر البقر — يدخل فيه الثور من البقر الوحشي والأهلي، والأنثى ثورة، وجموعه كالثيران والأثوار والثيرة
- `B005` ثورة الأقط: قطعة جامدة — يدخل فيه الثور أو الثورة بمعنى قطعة، وخاصة القطعة العظيمة من الأقط وجمعها أثوار أو ثورة
- `B006` ثور اسما لمكان أو قوم أو برج — يدخل فيه جبل ثور أو ثور أطحل، وبنو ثور أو قوم أو قبيلة ثور، وبرج الثور
- `B007` ثور الماء: طحلب يعلو السطح — يدخل فيه الطحلب المسمى ثور الماء أو الثور الذي ظهر على متن الماء

### `ج م ع`

- `B001` ضم المتفرق حتى يصير شيئا مجموعا — يدخل فيه جمع الشيء أو المال أو القوم، وجعل المتفرق جميعا، وما جمع من مواضع شتى كنهب مجمع.
- `B002` جماعة اجتمعت أو أخلاط ضمتها الجهة — يدخل فيه الجمع والجموع والجميع والجماعة والجماع إذا أريد بها جماعة الناس أو أخلاطهم أو الجيش.
- `B003` عزم محكم جمع الرأي بعد تفرقه — يدخل فيه أجمع على الأمر، أجمع الأمر أو الكيد، الإجماع بمعنى الإعداد والعزيمة والإحكام، واجتماع الآراء على تدبير.
- `B004` موضع أو يوم أو نداء يجمع الناس — يدخل فيه المجمع والموضع الذي يجتمع فيه الناس، وجمع للمزدلفة أو أيام منى، ويوم الجمعة ويوم الجمع، والمسجد الجامع، ونداء الصلاة جامعة، وفلاة مجمعة.
- `B005` قبضة الكف إذا ضمت الأصابع — يدخل فيه جمع الكف، الضرب بجمع الكف، ملء الجمع، والقبضة أو جمعة التمر.
- `B006` اتصال الجماع والمجامعة — يدخل فيه الجماع كناية عن النكاح، والمجامعة بمعنى المباضعة.
- `B007` حال المرأة أو الأنثى التي بقي حملها أو عذرها معها — يدخل فيه ماتت المرأة بجمع أي وولدها في بطنها، أو عذراء لم تمسس، وفلانة عند زوجها بجمع إذا لم يصل إليها، وأتان جامع إذا حملت أول ما تحمل.
- `B008` القيد الذي يجمع اليدين إلى العنق — يدخل فيه الجامعة والجوامع بمعنى الأغلال.
- `B009` اكتمال الشيء كله بلا تفرق أو نقص — يدخل فيه جمعاء للبهيمة التي لم يذهب من بدنها شيء، وجميع وأجمعون وجمع في التوكيد والكلية، والرجل المجتمع أو الجميع في خلقه، والجارية جمعت الثياب.
- `B010` استجماع القوة أو السير حتى تتلاحق أجزاؤه — يدخل فيه استجمع الفرس جريا، واستجمع السيل، واستجمع الأمر للمرء أي تهيأ له واجتمع.
- `B011` نخل دقل اجتمع من النوى لا يعرف اسمه — يدخل فيه الجمع بمعنى الدقل أو كل لون من النخل خرج من النوى ولا يعرف اسمه.
- `B012` عظم الشيء كأنه جامع ممتلئ — يدخل فيه قدر جماع أو جامعة بمعنى القدر العظيمة.
- `B013` ممالأة واجتماع مع غيرك على أمر — يدخل فيه جامعت الرجل على الأمر إذا مالأته عليه، وجامعه على أمر إذا اجتمع معه.

### `ح ب ب`

- `B001` الحبة التي تنبت وتحمل الحب — يدخل فيه الحب والحبة للحنطة والشعير والبقول والرياحين، والحبة الواحدة، وما شبه بها كالقطعة والبرد والقرط من حبة.
- `B002` المحبة الملازمة للقلب — يدخل فيه الحب والمحبة ونقيض البغض، والتحبيب، والمحبوب، والاستحباب بمعنى الإيثار، والمودة المتبادلة.
- `B003` صيغة المدح وغاية الرغبة — يدخل فيه حبذا، وحبابك أن تفعل، ونعم وحبة وكرامة، وما جاء بصيغة مدح أو بلوغ الغاية في المحبة.
- `B004` حبة القلب سويداؤه — يدخل فيه حبة القلب بمعنى سويدائه أو ثمرته أو العلقة السوداء داخله، وما صيغ كإصابة حبة القلب.
- `B005` البعير يلزم مكانه من عجز — يدخل فيه أحب البعير، والبعير المحب، والإحباب في الإبل إذا وقف أو برك أو لزم مكانه من حسر أو مرض أو كسر.
- `B006` الري حتى الامتلاء — يدخل فيه تحبب الحمار أو الإبل من الماء، وأول الري، وملء السقاء ونحوه حتى يمتلئ.
- `B007` الحب جرة عظيمة أو موضعها — يدخل فيه الحب بمعنى الجرة الضخمة أو الخابية، وجمعه حباب وحببة، وما قيل في الخشبات التي توضع عليها الجرة.
- `B008` حباب الماء فقاقيعه وطرائقه — يدخل فيه حباب الماء بمعنى الفقاقيع الطافية أو معظم الماء أو موجه وطرائقه، وما ألحق به من الطل على الشجر.
- `B009` حبب الأسنان انتظام كالدرر — يدخل فيه الحبب وحبب الأسنان، أي تنضد الأسنان وظهور بياض الريق عليها.
- `B010` الحبحاب الصغير القصير — يدخل فيه الحبحاب والحباحب بمعنى القصير أو الصغير الجسم، وما وصف به من هزال الإبل.
- `B011` نار الحباحب شرر لا ينتفع به — يدخل فيه نار الحباحب، الشرر الضعيف من الحجارة أو حوافر الخيل، والذباب أو الطائر المضيء ليلا، والنار التي لا ينتفع بها.
- `B012` الحباب الحية أو الشيطان — يدخل فيه الحباب بمعنى الحية، وما قيل في اسم الشيطان لكون الحية شيطانا.

### `ح ص ل`

- `B001` جمع الشيء حتى يظهر حاصله — يدخل فيه حصلت الشيء تحصيلا، والحاصل والمحصول بمعنى ما بقي وثبت بعد ذهاب غيره، ورد الكلام إلى محصوله، وإظهار ما في الصدور أو حاصل الحساب.
- `B002` استخراج اللب أو النفيس من غلافه — يدخل فيه التحصيل بمعنى إخراج اللب من القشور، وإخراج الذهب أو الفضة من حجر المعدن أو ترابه، وتمييز ما يحصل.
- `B003` البقية والحثالة بعد الرفع أو الفصل — يدخل فيه الحاصل والمحصول والحصائل بمعنى البقايا، والحصالة لما يبقى في الأندر من الحب بعد رفع الحب، والحصيل بمعنى الحثالة.
- `B004` موضع يجتمع فيه الطعام في جوف الطائر — يدخل فيه حوصلة الطائر وحواصل الطير، وملء الحوصلة، والطير المسمى الحوصلة، وما ألحقته العين من الحوصل للشاة واحونصال الطير.
- `B005` بلح حصل من النخلة قبل اشتداده — يدخل فيه الحصل: البلح قبل أن يشتد وتظهر ثفاريقه، وقولهم أحصل النخل.
- `B006` وجع بطن الفرس من أكل التراب — يدخل فيه حصل الفرس إذا اشتكى بطنه من أكل التراب أو تراب النبت.

### `خ ب ر`

- `B001` العلم بالخبر وباطن الأمر — يدخل فيه الخبر والنبأ والإخبار والاستخبار والخبرة بمعنى الاختبار والمعرفة ببواطن الأمر والخبير العالم والمخبر الباطن لا المنظر
- `B002` لين الأرض ومائها — يدخل فيه الخبراء والخبار والأرض الرخوة أو اللينة أو المنخفضة وما يجتمع فيها من ماء وشجر ومكان خَبِر
- `B003` إصلاح الأرض بالمخابرة — يدخل فيه الخبير بمعنى الأكار والمخابرة والمؤاكرة والمزارعة بجزء معلوم مما يخرج من الأرض
- `B004` الغزر في المزادة والناقة — يدخل فيه الخَبْر للمزادة العظيمة وتشبيه الناقة الغزيرة بها في السعة والغزر
- `B005` اللِّين في النبات والوبر والزبد — يدخل فيه الخبير للنبات اللين والوبر وزبد أفواه الإبل أو ما يلقيه البعير من فيه
- `B006` القسمة في الشاة واللحم — يدخل فيه الخُبْرة للشاة المشتركة التي يذبحها القوم ويقتسمون لحمها أو للنصيب من اللحم والسمك

### `خ ي ر`

- `B001` الميل إلى الخير النافع — يدخل فيه الخير العام المرغوب فيه، وضد الشر، وما فيه نفع أو فضل أو صلاح، والخير المطلق والمقيد، ومقابلته للشر أو الضر.
- `B002` فضل الصلاح والاصطفاء — يدخل فيه وصف الإنسان أو الشيء بأنه خير أو خيرة أو خيار أو أخيار، بمعنى الفضل والصلاح والجمال والميسم والاختيار من غير رذالة.
- `B003` طلب الخير بالاختيار والاستخارة — يدخل فيه الخيار والاختيار والتخير والاستخارة وخار الله لك وخيرته بين شيئين، أي طلب ما هو خير، أو الاصطفاء، أو تفويض الخيار.
- `B005` الكرم والهبة — يدخل فيه الخير بمعنى الكرم، والهبة والعطاء، وكثرة الخير في الشخص.
- `B006` استدراج الحيوان من جحره — يدخل فيه استخارة الضبع أو اليربوع بجعل خشبة أو نحوها في موضع من جحره حتى يخرج من موضع آخر.

### `ر ب ب`

- `B001` ربوبية وملك وسيادة — يدخل فيه الرب بمعنى الله تعالى، ومالك الشيء، وسيده المطاع، وصاحبه، ورب الدار والدابة والملك
- `B002` إصلاح وتربية وإتمام — يدخل فيه رب الشيء إذا أصلحه وأتمه وقام عليه، ورب النعمة والصنيعة والضيعة والولد والصبي، والتربية حالا فحالا
- `B003` علم رباني — يدخل فيه الرباني والربانيون بمعنى العلماء والحكماء وأهل العلم بالرب أو من يرب العلم ونفسه به
- `B004` ربة وجماعات كثيرة — يدخل فيه الربة والجماعات الكثيرة، والربيون إذا فسروا بالألوف أو الجماعات، ورباب القبائل لاجتماعهم
- `B005` ربيب وربيبة ورابة — يدخل فيه الربيب والربيبة للولد المربوب من زوج سابق، والراب والرابة لمن يقوم على أمره، والحاضنة
- `B006` رُبّ خاثر وإصلاح به — يدخل فيه الرُّبّ الطلاء الخاثر أو ثفل السمن والزيت، والسقاء والنحي والأديم والدواء والطعام إذا جعل فيه الرُّبّ أو أصلح به
- `B007` لزوم وإقامة ودوام — يدخل فيه رب أو أرب بالمكان إذا أقام، ومرب الإبل ومرابها، وأربت السحابة أو الجنوب إذا دامت، والإرباب بمعنى الدنو
- `B008` رباب السحاب — يدخل فيه الرباب والربابة للسحاب، والسحاب المتعلق أو المركب بعضه على بعض، وما سمي بذلك لتربية النبات أو دوام المطر
- `B009` شاة رُبّى وحداثة — يدخل فيه الشاة الرُّبّى والرباب لقرب العهد بالولادة أو لزوم البيت للبن، وربان الشيء بمعنى حدثانه وطراءته، وربى الشباب
- `B010` ربابة تجمع القداح — يدخل فيه الربابة للجلدة أو الوعاء الذي تجمع فيه القداح أو سهام الميسر، وجماعة السهام نفسها
- `B011` ربابة عهد وميثاق — يدخل فيه الربابة والرباب للعهد والميثاق والجوار، والأربة للمعاهدين، والرباب للعشور إذا جعل كالعهد
- `B012` ربة نبات — يدخل فيه الربة والربب لضرب من الشجر أو النبت أو البقلة التي تبقى خضراء
- `B013` ماء رَبَب كثير — يدخل فيه الربب للماء الكثير، ويقال للعذب، من جهة اجتماع الماء
- `B014` رَبْرَب قطيع — يدخل فيه الربرب لقطيع بقر الوحش، وقيل لجماعة البقر أو الإبل
- `B015` حرف رب وربما — يدخل فيه رب وربما وربت وربه كحرف خافض أو حرف معنى للتقليل، ودخول ما أو التاء أو الهاء عليه
- `B016` رُبَى حاجة وعقدة ونعمة — يدخل فيه الربى بمعنى الحاجة، والرابة، والعقدة المحكمة، والنعمة والإحسان
- `B017` رباني الملاحين — يدخل فيه الرباني لرئيس الملاحين

### `ش د د`

- `B001` شد العقد والوثاق — عقد الشيء وإيثاقه وتقوية عقده وتقوية العضد والملك
- `B002` شدة القوة والصلابة — القوة والصلابة والشجاعة وثبات القلب وشدة الحال والجوع والعذاب والتشديد وبذل الجهد والقدرة
- `B003` شد الحملة والعدو — الحمل على العدو في القتال والعدو والحضر
- `B004` بلوغ الأشد — بلوغ الأشد من القوة والرشد والحنكة والمعرفة واكتمال الشباب
- `B005` شد النهار وارتفاعه — ارتفاع النهار
- `B006` شدة البخل — الشديد والمتشدد بمعنى البخيل

### `ش ه د`

- `B001` الحضور مع المشاهدة — الحضور والمشاهدة والمعاينة والمحضر والمجمع ومواضع المناسك وحضور الزوج أو الشخص
- `B002` البيان بعلم — الشهادة والخبر القاطع وأداء ما عند الشاهد والإعلام والبيان والإظهار والإقرار والحكم وما يقوم شاهدا أو شهيدا على غيره
- `B005` اللسان الشاهد — الشاهد بمعنى اللسان والعبارة الظاهرة التي تبين عن صاحبها
- `B006` الخارج عند الولادة والإدراك — الشهود والشاهد لما يخرج مع الولد أو على رأسه وآثار النتاج من دم أو سلى وأشهد للبلوغ بخروج المذي أو الحيض
- `B007` الشَّهْد في الشمع — الشَّهْد والشَّهْدة للعسل ما دام في شمعه قبل العصر وجمعه شِهاد
- `B008` العلامة الشاهدة — الشاهد لما يدل على وقت أو حال أو جودة مثل النجم وصلاة المغرب وشاهد جري الفرس

### `ص ب ح`

- `B001` الصبح وأول النهار — الصبح والفجر والصباح والصبيحة وأول النهار والإصباح ووقت الإصباح
- `B002` الإتيان صباحا — الإتيان صباحا والغدو بالخيل أو بالماء والتحية بصباح
- `B003` الصبوح — الصبوح والشرب والأكل والسقي بالغداة وما يشرب أو يسقى أول النهار والمصابيح للأقداح
- `B004` يوم الصباح — يوم الصباح للغارة والغدو بالخيل ونداء الاستغاثة صباحا
- `B005` المصباح والسراج — المصباح والسراج والمسرجة ومقر السراج وما يستصبح به ومصابيح الكواكب
- `B006` الصُّبْحة والصباحة — الحمرة أو اللون بين الحمرة والغبرة في الشعر والأسد والوجه الصبيح والصباحة والجمال والوضاءة
- `B007` الصُّبْحة نوما — النوم بالغداة وحين يصبح المرء
- `B008` الناقة المصباح — الناقة أو الإبل التي تبرك في مبركها ولا تنهض للرعي حتى تصبح أو يرتفع النهار
- `B009` ظروف الصباح — أصبوحة كل يوم وذا صبوح وصبح خامسة ولصبح خامسة واللقاء أو الإتيان في صباح معين
- `B010` أصبح بمعنى صار — أصبح إذا صار على حال والإصباح مصدرا للفعل

### `ص د ر`

- `B001` الصدر الجارحة وما يتصل بها — صدر الإنسان والحيوان وما أشرف من أعلاه، ووجع الصدر وإصابته، وما يغطى الصدر أو يسمه أو يشد عليه، وما سمي لقوة صدره
- `B002` المقدّم والأعلى والأول — مقدّم الشيء وأعلاه وأوله، كصدر القناة والأمر والكتاب والمجلس والكلام، ومقدّم السهم، وسبق الفرس بصدره
- `B003` الصُّدور عن المورد — الانصراف عن الماء أو البلاد أو كل أمر بعد وروده، والإصدار بمعنى الإرجاع، والطريق الصادر بأهله
- `B004` الأصل الذي تصدر عنه الأفعال — المصدر بوصفه أصل الكلمة أو الفعل، وما يلحق به من اسم الموضع والزمان في الصدور
- `B005` المصادرة على مال — مصادرة العامل أو غيره على مال يؤديه ويضمنه
- `B006` الطائفة من الشيء — الصدر بمعنى طائفة من الشيء

### `ض ب ح`

- `B001` صوت الضباح — صوت الثعلب والهام والبوم والذئب والصدى وصوت أنفاس الخيل وأفواهها في العدو
- `B002` عدو ممدود الضبعين — سير الخيل أو الإبل وعدوها مع مد الضبعين أو العدو الخفيف
- `B003` إحراق أعالي العود — إحراق أعلى العود وحجارة القداحة وما مسته النار حتى يبدو مضبوحا
- `B004` تغير اللون إلى السواد — انضباح اللون وتغيره إلى السواد قليلا بفعل النار أو الشمس
- `B005` الرماد — الرماد المسمى الضبح

### `ع د و`

- `B001` مجاوزة الحد والظلم — يدخل فيه التعدي والاعتداء والعدوان وعدا على غيره والإغارة إذا كانت ظلما أو تجاوزا للحق
- `B002` العَدْو والحَضْر — يدخل فيه الجري والحضر وعدو الفرس والعدو على الأقدام
- `B003` العَدُوّ والعداوة — يدخل فيه العدو ضد الولي والعداوة والمعاداة وقوم أعداء أو عدا
- `B004` المجاوزة والاستثناء والصرف — يدخل فيه عدا الشيء إذا جاوزه وما عدا في الاستثناء وعد عن الأمر إذا تجاوزه إلى غيره وتعدية الفعل
- `B005` العَدْوى في طلب الإنصاف — يدخل فيه طلب المرء إلى وال أو قاض أن يعينه على من ظلمه وينتقم له منه
- `B006` العَدْوى في انتقال الداء — يدخل فيه ما يقال إنه يعدي من جرب أو داء ومجاوزة العلة من صاحبها إلى غيره
- `B007` العَوادي والعادية الشاغلة — يدخل فيه عوادي الدهر وعادية الشر وعدواء الشغل وما يشغل الإنسان أو يمنعه عن أمره
- `B008` العِداء في تعاقب الصيد — يدخل فيه الموالاة بين صيدين أو إسقاط أحدهما إثر الآخر في طلق واحد
- `B009` العَداء والعُدوة في الجانب والطوار — يدخل فيه طوار الشيء وما انقاد مع عرضه أو طوله وجانب الوادي وحافته وعداء النهر والجبل
- `B010` العَدْواء في صلابة المكان واضطرابه — يدخل فيه الأرض اليابسة الصلبة والمكان غير المستوي أو غير المطمئن لمن قعد عليه
- `B011` العَدَوِيّة من نبات الصيف — يدخل فيه نبات الصيف بعد ذهاب الربيع حين يخضر صغار الشجر فترعاه الإبل
- `B012` العَنْدَأْوَة في الالتواء والعسر — يدخل فيه العندأوة إذا أريد بها التواء وعسر ونسبت إلى العداء

### `ع ل م`

- `B001` انكشاف الشيء للعارف — يدخل فيه العلم نقيض الجهل وإدراك الشيء ومعرفته والشعور بالخبر والتعلم والتعليم والإعلام والمغالبة بالعلم
- `B002` أثر يميز الشيء ويهدي إليه — يدخل فيه العلامة والعلم والراية والجبل والمعلم ومعالم الطريق والحدود وعلم الثوب ورقمه وتعليم الفارس والثوب والقدح والعمامة والحناء إذا جعلت علامة
- `B004` شق ظاهر في الشفة العليا — يدخل فيه العلم والشق في الشفة العليا ووصف الرجل أو البعير بالأعلم إذا كان الشق أو العلم في الموضع الأعلى
- `B005` ماء كثير مجتمع في عيلم — يدخل فيه العيلم بمعنى البحر أو البئر الكثيرة الماء
- `B006` طائر جارح يسمى العلام — يدخل فيه العلام بمعنى الصقر أو الباشق وما نسب إليه من العلامي
- `B007` ذكر الضباع يسمى العيلام — يدخل فيه العيلام بمعنى ذكر الضباع

### `غ ي ر`

- `B001` الصلاح والمنفعة بالميرة والسقي والإصلاح — يدخل فيه ميرة الأهل ونفعهم، وسقي الأرض أو القوم بالغيث، وإصلاح الرحال أو شأن الراحلة.
- `B002` الغَيْر في الدية — يدخل فيه اسم الغَيْر أو الغِيرة للدية، وأخذ الدية بدل القود.
- `B003` تغيير الصورة أو إبدال الشيء بغيره — يدخل فيه تغيير الشيء فتغيره، وتغير الحال، وتبديل الشيء بغيره، ودفع المنكر بغيره من الحق، والمبادلة والبدل.
- `B004` الغَيْرة على الأهل — يدخل فيه الغَيْرة المفتوحة على الأهل، ووصف الرجل أو المرأة بالغيور وغيران وغيرى، ولغة الغار في الغيرة.
- `B005` السوى والخلاف والاستثناء والنفي — يدخل فيه كون الشيء سوى غيره وخلافه، واستعمال غير صفة أو اسما أو أداة استثناء، ومعنى لا، ونفي صورة أو ذات، وعموم الغيرين على المختلفين.

### `ق ب ر`

- `B001` مواراة الميت في القبر — يدخل فيه القبر مدفن الميت ومقره، وقبر الميت أي دفنه وجعله في القبر، وأقبره أي جعل له قبرا أو أذن في قبره أو صيره ذا قبر، والمقبرة موضع القبور
- `B002` غموض الشيء وتطامنه — يدخل فيه الغموض والتطامن في الشيء، والأرض القبور الغامضة، والنخلة القبور التي يكون حملها في سعفها، وجوف عود الطيب المتأكل، والمقبور المحصور في جلدة مصمتة
- `B003` القُبَّرة الطائر — يدخل فيه القُبَّرة والقُبَّر اسما لطائر، وما يتصل بهما من لغة القنبرة والقنبراء
- `B004` طرف الأنف في الغضب — يدخل فيه القبراة طرف الأنف، والقبيرة رأس القنفاء، وقولهم جاء رامعا قبراه أو فخا قبراه في الغضبان

### `ق د ح`

- `B001` إيراء النار بالقدح — قدح النار والزند والحجر والحديدة التي تورى بها النار
- `B002` نقر الشيء وعيبه — قدح الشيء ونقر العظم وإحداث صدع أو وصمة في العود والعظم
- `B003` طعن في النسب — القدح في نسب الرجل بالطعن فيه
- `B004` أكال الشجر والسن — الأكال أو الدودة أو السواد الذي يقع في الشجر والأسنان
- `B005` غرف ما في القدر — قدح القدر أو المرق والغرف بالمقدحة وما يبقى في أسفل القدر فيغرف بجهد والركي التي تغرف باليد
- `B006` قدح الشرب — القدح من الآنية وأقداح الشرب وصانع الأقداح
- `B007` عود السهم والقدح في الميسر — السهم قبل النصل والريش والقدح الواحد من قداح الميسر
- `B008` ضمر الفرس وغؤور العين — ضمر الفرس حتى يصير مثل القدح وغؤور العين أو إخراج مائها الفاسد
- `B009` رخص أطراف النبت — القداح من أطراف النبت والورق الغض ورخص النبات
- `B010` اقتداح الأمر بالنظر والتدبير — اقتداح الأمر بالنظر فيه وتدبيره

### `ك ن د`

- `B001` القطع والانفصال — قطع الشيء وفصله ومنه قطع الحبل وقطع الشكر والمفارقة
- `B002` كفران النعمة والمودة — الكنود وكند وامرأة كنود في كفر النعمة والمواصلة والمودة وعد المصائب ونسيان النعم والأثرة ومنع الرفد
- `B003` الأرض التي لا تنبت — الأرض الكنود التي لا تنبت شيئا
- `B004` اسم كندة — اسم كندة للحي اليماني وتعليله بالمفارقة

### `ن ق ع`

- `B001` استقرار الماء وما ينقع فيه — يدخل فيه اجتماع الماء وثباته وطول مكثه، واستنقاع الشيء في الماء، والإناء أو الموضع الذي ينقع فيه، والحوض أو البئر الكثيرة الماء وفضل ماء البئر، والنقوع والنقيع من دواء أو زبيب أو شراب أو صبغ، والأنقوعة لما سال إليه الماء أو وقبة الثريد.
- `B002` ماء ينقع الغلة ويروي — يدخل فيه إرواء العطش والغلة، والشرب حتى يروى، والاشتفاء أو اطمئنان النفس بالخبر أو الرأي على طريق المجاز.
- `B003` نقيعة طعام أو نحر أو لبن — يدخل فيه النقيعة طعاما للقادم أو عند الإملاك، وما ينحر من نهب أو عدة إبل، والمحْض من اللبن الذي يبرد.
- `B004` نقع الغبار المثار — يدخل فيه النقع بمعنى الغبار، ولا سيما الغبار المرتفع أو المثار.
- `B005` نقع الصوت المرتفع — يدخل فيه الصراخ وارتفاع الصوت وتتابعه أو دوامه، وصوت النعامة، وما قيس عليه من متكثر يصيح بما ليس عنده.
- `B006` سم ناقع ثابت أو قاتل — يدخل فيه السم الناقع أو النقيع أو المنقوع إذا ثبت أو اجتمع في الأنياب، ويمتد في التهذيب إلى الموت الدائم والقتل.
- `B007` نقاع الأرض القيعان السهلة — يدخل فيه النقاع جمع نقع: الأرض الحرة الطين الطيبة أو قيعان الأرض التي لا حزونة فيها ولا ارتفاع ولا انهباط.
- `B008` شراب بأنقع مجرب للموارد — يدخل فيه المثل شراب بأنقع للرجل الذي جرب الأمور وعرف مواردها ومسالك السلامة فيها.
- `B009` نقعه بالشتم القبيح — يدخل فيه قولهم نقعه بالشتم إذا شتمه شتما قبيحا.

### `و ر ي`

- `B001` داء يأكل الجوف أو يصيب الرئة — يدخل فيه الوري والورى داء الجوف أو الرئة، وأكل القيح للجوف، وإصابة الرئة، والجراحة التي يصيب سابرها الوري.
- `B002` نار كامنة تخرج من الزند — يدخل فيه وري الزند وورى الزند وخروج ناره، وإيراء الزند أو النار، وإيقاد النار الخامدة ورفعها، وما يثقب به النار.
- `B003` زند يقدح نجاحا أو نصرة — يدخل فيه قولهم فلان واري الزند إذا أنجح وأدرك طلبه، وورت بك زنادي إذا وجد منك نصحا وسماحة أو إعانة، ووريت عن فلان إذا نصرته ودفعت عنه.
- `B004` شحم وار وسمن ظاهر — يدخل فيه اللحم الواري والشحم الواري والوري مثله، والناقة الوارية، واكتناز المخ.
- `B005` ستر الشيء وجعله وراء الظهور — يدخل فيه وارى الشيء إذا أخفاه، وتوارى إذا استتر، ووري الخبر تورية إذا ستره وأظهر غيره، وإظهار غير المراد.
- `B006` الجانب الوراء: خلف أو أمام أو سوى — يدخل فيه وراء بمعنى خلف، وقدام أو أمام في بعض الاستعمال، وما بعد الشيء أو سواه، والجانب الآخر من حجاب أو جدار، وصيغة وراءك للإغراء بالتأخر أو التنحي.
- `B007` ولد الولد يأتي من وراء الابن — يدخل فيه الوراء أو وراء بمعنى ولد الولد أو ابن الابن.
- `B008` الورى: الخلق على ظهر الأرض — يدخل فيه الورى بمعنى الخلق أو الأنام الذين على وجه الأرض في الوقت.

### `و س ط`

- `B001` العدل والخيار في موضع الوسط — يدخل فيه الوسط بمعنى العدل والخيار والقصد المصون عن الإفراط والتفريط، ومنه أمة وسطا، وأوسط القوم أو وسيط الحسب بمعنى خيارهم وأرفعهم محلا.
- `B002` موضع الوسط بين الأطراف — يدخل فيه وسط الشيء أو الدار أو الرأس أو القوم، وما كان بين طرفين أو بين أجزاء مرتبة، وواسطة القلادة والأصبع الوسطى والصلاة الوسطى، واسم واسط إذا علل بالوقوع بين موضعين.
- `B003` الدخول أو الجعل في الوسط — يدخل فيه وسط القوم أو أوسطهم أو توسطهم إذا دخل وسطهم، والتوسيط بمعنى جعل الشيء في الوسط.
- `B004` مرتبة وسطى بين الجيد والرديء — يدخل فيه وصف الشيء أو الرجل بأنه وسط أي بين الجيد والرديء أو خارج عن حد الخير بحسب طرفي المقابلة.
- `B005` الوساطة بين الناس — يدخل فيه التوسط بين الناس بمعنى الوساطة والسعي بين الأطراف.
- `B006` قطع الشيء نصفين — يدخل فيه التوسيط بمعنى قطع الشيء نصفين.
- `B007` الوسوط: بيت أو ناقة مخصوصة — يدخل فيه الوسوط كما عده Maqayis اسما لبيت من بيوت الشعر أكبر من المظلة، وقيل من النوق كالصفوف تملأ الإناء.

## Model ledger used by seed passes

Each model below is a frozen image-branch reached by one or more seeds. Seed rows later cite these models and preserve the failed alternatives.

### M1 — kinetic oath sequence into a gathered center

Generating set: `(E: ع د و B002)`, `(E: ض ب ح B001/B002)`, `(E: و ر ي B002)`, `(E: ق د ح B001)`, `(E: ص ب ح B001/B004)`, `(E: ث و ر B001/B002)`, `(E: ن ق ع B004)`, `(E: و س ط B002/B003)`, `(E: ج م ع B001/B002/B010)`.

Frozen model: a rapid agent-set moves, sounds, strikes fire, arrives at dawn, stirs dust, and enters the middle of a gathered body.

Predictions at freeze: sequential connectors, same-agent morphology, manner/time/object attachments, and center-entry syntax.

Corroborators: `(C: fā-chain 100:2–5)`, `(C: FP active participles 100:1–3)`, `(C: attachment ضبحا as circumstantial)`, `(C: attachment قدحا as circumstantial)`, `(C: attachment صبحا as time adverb)`, `(C: attachment نقعا direct object)`, `(C: attachment جمعا direct object entered by وسطن)`, `(C: repeated بِهِ)`.

Constraints: `(K: no explicit horse noun; animal/horse imagery remains secondary branch simulation)`, `(K: غ ي ر branches do not independently supply a clean raid lexeme in the uncontaminated dossier; the local raid-like role is supported by the active participle sequence plus صبحا attachment)`.

Grade: strong.

### M2 — hidden thing struck, stirred, exposed

Generating set: `(E: و ر ي B002 hidden fire)`, `(E: و ر ي B005 hiding)`, `(E: ق د ح B001 striking fire)`, `(E: ث و ر B001/B002 emergence/stirring)`, `(E: ن ق ع B004 raised dust)`, `(E: ب ع ث ر B001 exposing buried)`, `(E: ح ص ل B001/B002 result/extraction)`, `(E: خ ب ر B001 inner knowledge)`.

Frozen model: what is latent or covered is brought out by striking, stirring, overturning, extraction, and final interior knowledge.

Predictions at freeze: later containment, passive disclosure, hidden contents, and final knowing.

Corroborators: `(C: ما فِي القبور)`, `(C: ما فِي الصدور)`, `(C: passive بُعثر/حُصّل)`, `(C: ع ل م B001)`, `(C: خ ب ر B001)`.

Constraint: `(K: the final disclosure is not literally fire; fire is a secondary activation geometry)`.

Grade: medium-strong.

### M3 — dual container disclosure: graves then chests

Generating set: `(E: ب ع ث ر B001)`, `(E: ق ب ر B001/B002)`, `(E: ح ص ل B001/B002)`, `(E: ص د ر B001/B004)`, `(E: ع ل م B001)`, `(E: خ ب ر B001)`.

Frozen model: external burial-container is opened, then internal chest/source-container is extracted, then the scene closes under expert knowledge.

Predictions at freeze: parallel `ما في X`, passive operations, and a final knower.

Corroborators: `(C: repeated ما فِي)`, `(C: attachment فِي القبور completes ما)`, `(C: attachment فِي الصدور completes ما)`, `(C: إذا → يومئذ)`, `(C: ربهم بهم closes on the disclosed human set)`.

Constraint: `(K: grave and chest containers stay distinct; neither root absorbs the other)`.

Grade: strong.

### M4 — human breach under the Rabb

Generating set: `(E: ء ن س B001)`, `(E: ر ب ب B001/B002/B011)`, `(E: ك ن د B001/B002)`, `(E: ش ه د B001/B002)`, `(E: ح ب ب B002)`, `(E: خ ي ر B001/B005)`, `(E: ش د د B002/B006)`.

Frozen model: the human is positioned with respect to `ربه`; care, ownership, nurture, or covenant is answered by cutting/ingratitude, witnessed and intensified by inner attachment to good.

Predictions at freeze: later return to Rabb relation and exposure of inner motives.

Corroborators: `(C: attachment لربه targets كنود)`, `(C: على ذلك targets شهيد)`, `(C: لحب relates شديد to حب)`, `(C: الخير idafa complement of حب)`, `(C: ما في الصدور)`, `(C: ربهم reactivates ربه)`, `(C: خ ب ر B001)`.

Constraints: `(K: early feminine plural agents are not grammatically the later الإنسان)`, `(K: الخير remains within furuq good/benefit/gift range; no external narrowing is added)`.

Grade: strong.

### M5 — witness, sign, knowledge, expert closure

Generating set: `(E: ش ه د B001/B002/B005/B008)`, `(E: ع ل م B001/B002)`, `(E: ح ص ل B001)`, `(E: ص د ر B004)`, `(E: خ ب ر B001)`.

Frozen model: the matter is witnessed, marked, questioned as knowledge, extracted from source, and closed by expertise in the interior affair.

Predictions at freeze: specified matter of witness, explicit knowledge question, hidden evidence becoming available, final knowing subject.

Corroborators: `(C: على ذلك)`, `(C: أفلا يعلم)`, `(C: ما في الصدور)`, `(C: ربهم بهم)`, `(C: emphatic لَ in شهيد/شديد/خبير)`.

Constraint: `(K: شهيد and خبير are sequenced roles, not identical subjects)`.

Grade: medium-strong.

### M6 — inner love tightened around good

Generating set: `(E: ح ب ب B002/B004)`, `(E: ش د د B001/B002/B006)`, `(E: خ ي ر B001/B002/B003/B005)`, `(E: ص د ر B001)`, `(E: ح ص ل B002)`.

Frozen model: inner love of good is a tightened orientation whose chest-content will later be drawn out and known.

Predictions at freeze: syntax should attach intensity to love, love to good, and final disclosure to inner storage.

Corroborators: `(C: لحب relates شديد to حب)`, `(C: الخير idafa complement of حب)`, `(C: ما في الصدور)`, `(C: خ ب ر B001)`.

Constraints: `(K: حبة القلب is only secondary branch support; the surface word remains حب)`, `(K: خير is not narrowed beyond furuq)`.

Grade: medium.

### M7 — gather, cut, scatter, collect result

Generating set: `(E: ج م ع B001/B002/B009/B010)`, `(E: ك ن د B001)`, `(E: و س ط B003)`, `(E: ب ع ث ر B002/B003)`, `(E: ح ص ل B001/B003)`, `(E: ش د د B001)`.

Frozen model: the passage alternates collection and disruption: gathered center, cut relation, overturned contents, collected result.

Predictions at freeze: direct objects entered or exposed, then settled remainder/result.

Corroborators: `(C: جمعا direct object)`, `(C: ما passive subjects in 100:9–10)`, `(C: حصل result)`, `(C: خبير final knowledge)`.

Constraint: `(K: ك ن د B001 cutting cannot replace ك ن د B002 ingratitude in the middle predicate)`.

Grade: medium-strong.

### M8 — boundary, side, and middle geometry

Generating set: `(E: ع د و B004/B009/B010)`, `(E: و ر ي B006)`, `(E: و س ط B002/B003)`, `(E: ج م ع B001/B002)`, `(E: ص د ر B002)`.

Frozen model: side or boundary is crossed and the force reaches the middle/front of a gathered body.

Predictions at freeze: object or mass whose middle is entered.

Corroborators: `(C: attachment جمعا object entered by وسطن)`, `(C: repeated فَ sequence)`, `(C: later فِي container syntax as a separate inside relation)`.

Constraint: `(K: spatial geometry alone does not explain human/Rabb predicate or final knowledge)`.

Grade: medium.

### M9 — dawn and visibility threshold

Generating set: `(E: ص ب ح B001/B002/B004/B005/B010)`, `(E: ث و ر B001)`, `(E: ن ق ع B004)`, `(E: ع ل م B001/B002)`, `(E: خ ب ر B001)`.

Frozen model: a dawn/visibility threshold opens the scene; later exposure turns partial visibility into explicit knowledge.

Predictions at freeze: visibility should intensify from time-of-event to knowledge/disclosure.

Corroborators: `(C: صبحا attachment as time adverb)`, `(C: أفلا يعلم)`, `(C: بُعثر/حصل)`, `(C: يومئذ)`.

Constraint: `(K: only one explicit dawn word occurs; the model depends on later disclosure roots)`.

Grade: medium.

### M10 — sound, raised trace, witness

Generating set: `(E: ض ب ح B001)`, `(E: ن ق ع B005)`, `(E: ش ه د B005)`, `(E: ع ل م B002)`.

Frozen model: audible breath/raised sound becomes expressive trace or testimony.

Predictions at freeze: later explicit voice, tongue, or speech should appear.

Corroborator: `(C: ش ه د B005 supports expression)`.

Constraint: `(K: no explicit speech verb or tongue word occurs; ن ق ع B004 dust is stronger locally than ن ق ع B005 sound)`.

Grade: weak.

### M11 — legal vindication / compensation rival

Generating set: `(E: ع د و B005)`, `(E: غ ي ر B002)`, `(E: ش ه د B002)`, `(E: ع ل م B001)`, `(E: ص د ر B005)`, `(E: خ ب ر B006)`.

Frozen model: a claim, testimony, compensation, confiscation, or division could form a legal/accounting scene.

Predictions at freeze: explicit legal claimant, judge, compensation, property seizure, or division should appear.

Corroborators: weak `(C: شهيد testimony)`, `(C: يعلم/خبير knowledge)`.

Constraints: `(K: no claimant, judge, compensation, confiscated property, or legal division construction)`.

Grade: unlikely to weak.

### M12 — animal/mount body shadow

Generating set: `(E: ع د و B002)`, `(E: ض ب ح B001/B002)`, `(E: ق د ح B008)`, `(E: ص ب ح B008)`, `(E: ح ص ل B006)`, `(E: ر ب ب B014)`.

Frozen model: branches around running animals, breath, leanness, morning-staying animal, dirt-ingestion pain, and herd produce an animal-body shadow.

Predictions at freeze: explicit animal/mount noun, body condition, herd, pain, or reins/driver should appear.

Corroborator: `(C: early FP active-participle agent-set can host animal-like motion only as secondary simulation)`.

Constraints: `(K: no explicit animal noun in sacred Arabic)`, `(K: حصل B006 is defeated by the actual passive extraction use at 100:10)`.

Grade: weak.

### M13 — water, seed, nurture, soft-earth rival

Generating set: `(E: ن ق ع B001/B002/B007)`, `(E: ح ب ب B001/B006/B007/B008)`, `(E: ر ب ب B002/B008/B012/B013)`, `(E: خ ب ر B002/B003/B005)`, `(E: ع ل م B005)`, `(E: ص د ر B003)`.

Frozen model: soaking water, seed/grain, nurture, clouds, plant, soft land, and watering could form a growth scene.

Predictions at freeze: planting, watering, cultivation, growth, or explicit land roles.

Corroborator: weak `(C: ر ب ب B002 nurture can support M4’s benefaction contrast)`.

Constraints: `(K: نَقْعًا is locally direct object of أثَرن and is better fit by dust B004)`, `(K: حب in 100:8 is syntactically love, not seed)`, `(K: no planting/watering/cultivation construction)`.

Grade: unlikely to weak.

### M14 — vessel, food, honey, share rival

Generating set: `(E: ق د ح B005/B006)`, `(E: ح ب ب B007)`, `(E: ح ص ل B004)`, `(E: ش ه د B007)`, `(E: ص ب ح B003)`, `(E: خ ب ر B006)`, `(E: ج م ع B012)`.

Frozen model: vessels, ladling, crop/container, honey, morning drink, shares, and great vessel make a food/container scene.

Predictions at freeze: explicit vessel, food/drink, honey, share, or eating role.

Constraints: `(K: no food, drink, honey, vessel, or share syntax)`, `(K: قدحا attaches to الموريات and fits fire-striking more strongly)`.

Grade: unlikely.

### M15 — arrow/lot and decision rival

Generating set: `(E: ق د ح B007)`, `(E: ر ب ب B010)`, `(E: ج م ع B003/B013)`, `(E: ش د د B001)`, `(E: ق د ح B010)`.

Frozen model: shafts or lots are gathered in a container, tied to deliberation or firm resolve.

Predictions at freeze: explicit lots, arrows, gaming, drawing, or decision-mechanism.

Constraints: `(K: no lot/arrow/maysir construction)`, `(K: قدحا is a manner expression for إيراء/striking, not a shaft noun in context)`.

Grade: unlikely.

### M16 — disease, poison, death rival

Generating set: `(E: و ر ي B001)`, `(E: ع د و B006)`, `(E: ن ق ع B006)`, `(E: ق ب ر B001)`, `(E: ص د ر B001)`, `(E: ح ص ل B006)`.

Frozen model: disease/contagion/poison/death could connect chest, grave, and hidden injury.

Predictions at freeze: disease, poison, bodily affliction, contagion, or pain syntax.

Constraints: `(K: graves are part of passive disclosure, not disease narrative)`, `(K: no poison/disease/contagion wording)`.

Grade: unlikely.

## Lexical seed-pass audit

For each row below, `sweep = all 23 root dossiers`. If no selected model is named, the seed terminated after full sweep because no other passage root supplied a specific role, mechanism, participant, direction, medium, force, constraint, or later corroborator. All grades are provisional discovery grades, not primary contextual meanings.

### 100:1:1 `وَٱلْعَٰدِيَٰتِ` — root `ع د و`

1. `100:1:1 ع د و B001 مجاوزة الحد والظلم` — Initial image: overstepping a limit. Sweep selected `(E: ك ن د B002)`, `(E: ر ب ب B001/B011)`, `(E: ش ه د B002)` → M4. Freeze predicted violated relation and witness; tested `لربه`, `على ذلك`, `ربهم`. Constraint: early agent grammar is not the later الإنسان. Grade: medium.
2. `B002 العَدْو والحَضْر` — Running. Selected M1 with breath, spark, dawn, stirring, dust, middle, gathering. Grade: strong.
3. `B003 العَدُوّ والعداوة` — Enemy/opposition. Selected weak M4 via opposition to Rabb relation. Constraint: no explicit enemy noun or battle opponent. Grade: weak.
4. `B004 المجاوزة والاستثناء والصرف` — Crossing/beyond. Selected M8 with side/middle/inside geometry. Grade: medium.
5. `B005 العَدْوى في طلب الإنصاف` — Seeking help for justice. Selected only M11 legal rival. Constraint: no claimant, judge, or compensation. Grade: unlikely to weak.
6. `B006 العَدْوى في انتقال الداء` — Disease transmission. Selected M16 rival. Constraint: no disease syntax. Grade: unlikely.
7. `B007 العَوادي والعادية الشاغلة` — Disruptive worldly happenings. Weakly tests M7, but no specific local complement. Grade: weak.
8. `B008 العِداء في تعاقب الصيد` — Successive hunting. Sequence resonates with fā-chain, but no prey/hunt role. Grade: weak.
9. `B009 العَداء والعُدوة في الجانب والطوار` — Side/bank. Selected M8. Grade: medium.
10. `B010 العَدْواء في صلابة المكان واضطرابه` — Hard/uneven place. Selected M8 weakly as difficult ground; no terrain role. Grade: weak.
11. `B011 العَدَوِيّة من نبات الصيف` — Summer plant. Selected only M13 rival. Grade: unlikely.
12. `B012 العَنْدَأْوَة في الالتواء والعسر` — Twisting/difficulty. No passage-local mechanism after sweep. Grade: unlikely.

### 100:1:2 `ضَبْحًا` — root `ض ب ح`

13. `ض ب ح B001 صوت الضباح` — Breath/sound. Selected M1 and M10. M1 grade strong local; M10 grade weak because later voice evidence is absent.
14. `B002 عدو ممدود الضبعين` — Running with stretched forelegs. Selected M1 and M12. Grade: strong for M1; weak as animal-body shadow.
15. `B003 إحراق أعالي العود` — Burning tips. Selected M2 via fire/striking. Constraint: no literal burning object beyond spark activation. Grade: medium.
16. `B004 تغير اللون إلى السواد` — Darkening by fire/sun. Tested against dawn/fire/dust; no color role. Grade: weak.
17. `B005 الرماد` — Ash. Tested against dust and exposure; no ash word or residue role. Grade: weak.

### 100:2:1 `فَٱلْمُورِيَٰتِ` — root `و ر ي`

18. `و ر ي B001 داء يأكل الجوف أو يصيب الرئة` — Hollow/lung disease. Selected M16 rival; defeated by no disease syntax. Grade: unlikely.
19. `B002 نار كامنة تخرج من الزند` — Hidden fire from flint. Selected M1/M2. Grade: strong locally, medium-strong passage-wide.
20. `B003 زند يقدح نجاحا أو نصرة` — Successful/helping flint. Tested with Rabb/good; no aid/success role. Grade: weak.
21. `B004 شحم وار وسمن ظاهر` — Visible fat/sleekness. No passage-local complement. Grade: unlikely.
22. `B005 ستر الشيء وجعله وراء الظهور` — Hiding/concealment. Selected M2/M3. Grade: medium-strong.
23. `B006 الجانب الوراء` — Behind/other side. Selected M8. Grade: medium.
24. `B007 ولد الولد يأتي من وراء الابن` — Descendant. No lineage role. Grade: unlikely.
25. `B008 الورى: الخلق على ظهر الأرض` — Created beings on earth. Weak resonance with الإنسان, but no model completion. Grade: weak.

### 100:2:2 `قَدْحًا` — root `ق د ح`

26. `ق د ح B001 إيراء النار بالقدح` — Fire-striking. Selected M1/M2. Grade: strong.
27. `B002 نقر الشيء وعيبه` — Notch/defect. Weakly tests M4 blemish, but no notch/defect syntax. Grade: weak.
28. `B003 طعن في النسب` — Attack lineage. No lineage/pedigree role. Grade: unlikely.
29. `B004 أكال الشجر والسن` — Wood/tooth decay. No local complement. Grade: unlikely.
30. `B005 غرف ما في القدر` — Ladling pot contents. Selected M14 rival; defeated by no food/vessel. Grade: unlikely.
31. `B006 قدح الشرب` — Drinking vessel. Selected M14 rival. Grade: unlikely.
32. `B007 عود السهم والقدح في الميسر` — Arrow shaft/lot. Selected M15 rival; defeated by no lot/arrow construction. Grade: unlikely.
33. `B008 ضمر الفرس وغؤور العين` — Lean horse/sunken eye. Selected M12 weakly; no explicit animal/body. Grade: weak.
34. `B009 رخص أطراف النبت` — Tender plant tips. Selected M13 rival. Grade: unlikely.
35. `B010 اقتداح الأمر بالنظر والتدبير` — Deliberating/contriving. Selected M15 weakly; no decision-mechanism. Grade: weak.

### 100:3:1 `فَٱلْمُغِيرَٰتِ` — root `غ ي ر`

36. `غ ي ر B001 الصلاح والمنفعة بالميرة والسقي والإصلاح` — Provision/repair/watering. Selected M13 rival and weak M4 benefaction contrast. Grade: weak.
37. `B002 الغَيْر في الدية` — Blood-money substitute. Selected M11 rival. Grade: unlikely.
38. `B003 تغيير الصورة أو إبدال الشيء بغيره` — Changing state/form. Selected M2/M9 as transformation support. Grade: medium.
39. `B004 الغَيْرة على الأهل` — Jealousy. Tested against love/intensity; no family-jealousy role. Grade: weak.
40. `B005 السوى والخلاف والاستثناء والنفي` — Otherness/exception/negation. Weak with opposition and contrast; no sustained model. Grade: weak.

### 100:3:2 `صُبْحًا` — root `ص ب ح`

41. `ص ب ح B001 الصبح وأول النهار` — Dawn. Selected M1/M9. Grade: strong local, medium passage-wide.
42. `B002 الإتيان صباحا` — Coming in morning. Selected M1/M9. Grade: medium.
43. `B003 الصبوح` — Morning drink/food. Selected M14 rival. Grade: unlikely.
44. `B004 يوم الصباح` — Morning raid/call. Selected M1 with constraint against importing unmarked raid detail. Grade: strong local.
45. `B005 المصباح والسراج` — Lamp. Selected M9. Grade: medium.
46. `B006 الصُّبْحة والصباحة` — Redness/beauty. No color/beauty role. Grade: weak.
47. `B007 الصُّبْحة نوما` — Morning sleep. No sleep role. Grade: unlikely.
48. `B008 الناقة المصباح` — Camel staying until morning. Selected M12 weakly; no animal noun. Grade: unlikely to weak.
49. `B009 ظروف الصباح` — Morning-time expressions. Supports time only; no independent image. Grade: weak.
50. `B010 أصبح بمعنى صار` — Becoming. Selected M9 as state-shift support. Grade: medium-weak.

### 100:4:1 `فَأَثَرْنَ` — root `ث و ر`

51. `ث و ر B001 انبعاث الشيء وانتشاره ظاهرا` — Outbreak/spread into visibility. Selected M1/M2/M9. Grade: strong.
52. `B002 إثارة الشيء وتحريكه من موضعه` — Stirring/moving from place. Selected M1/M2. Grade: strong.
53. `B003 هيجان إلى مواجهة أو غضب` — Agitation/confrontation/anger. Weak with intensity and charge, but no anger predicate. Grade: weak.
54. `B004 الثور: ذكر البقر` — Bull. Selected M12 only as rejected animal shadow. Grade: unlikely.
55. `B005 ثورة الأقط: قطعة جامدة` — Curd lump. No passage-local complement. Grade: unlikely.
56. `B006 ثور اسما لمكان أو قوم أو برج` — Place/people/constellation name. No passage-local complement. Grade: unlikely.
57. `B007 ثور الماء: طحلب يعلو السطح` — Algae on water. Selected M13 rival; defeated by dust syntax. Grade: unlikely.

### 100:4:3 `نَقْعًا` — root `ن ق ع`

58. `ن ق ع B001 استقرار الماء وما ينقع فيه` — Settled/soaking water. Selected M13 rival. Grade: unlikely to weak.
59. `B002 ماء ينقع الغلة ويروي` — Quenching water. Selected M13 rival. Grade: unlikely to weak.
60. `B003 نقيعة طعام أو نحر أو لبن` — Food/slaughter/milk. Selected M14 rival; defeated. Grade: unlikely.
61. `B004 نقع الغبار المثار` — Raised dust. Selected M1/M2/M9. Grade: strong.
62. `B005 نقع الصوت المرتفع` — Raised sound. Selected M10. Grade: weak.
63. `B006 سم ناقع ثابت أو قاتل` — Fixed/deadly poison. Selected M16 rival; defeated. Grade: unlikely.
64. `B007 نقاع الأرض القيعان السهلة` — Easy earth basins. Selected M13 weakly; no basin role. Grade: weak.
65. `B008 شراب بأنقع مجرب للموارد` — Experienced in watering places. Weakly tests خبر; no proverb/resource route. Grade: unlikely.
66. `B009 نقعه بالشتم القبيح` — Ugly insult. Weak sound/speech route; no insult role. Grade: unlikely.

### 100:5:1 `فَوَسَطْنَ` — root `و س ط`

67. `و س ط B001 العدل والخيار في موضع الوسط` — Just/excellent middle. Weak moral resonance; local verb prefers entry. Grade: medium-weak.
68. `B002 موضع الوسط بين الأطراف` — Middle place. Selected M1/M8. Grade: strong local.
69. `B003 الدخول أو الجعل في الوسط` — Entering/making middle. Selected M1/M8/M7. Grade: strong.
70. `B004 مرتبة وسطى بين الجيد والرديء` — Intermediate quality. Tested with خير/كنود; no grading syntax. Grade: weak.
71. `B005 الوساطة بين الناس` — Mediation. No mediation roles. Grade: unlikely.
72. `B006 قطع الشيء نصفين` — Cutting in halves. Selected M7 weakly via cut/disrupt. Grade: weak.
73. `B007 الوسوط: بيت أو ناقة مخصوصة` — Special tent/camel. Selected M12/M14 only as rejected rival. Grade: unlikely.

### 100:5:3 `جَمْعًا` — root `ج م ع`

74. `ج م ع B001 ضم المتفرق حتى يصير شيئا مجموعا` — Joining scattered things. Selected M1/M7/M3. Grade: strong.
75. `B002 جماعة اجتمعت أو أخلاط ضمتها الجهة` — Gathered group/army. Selected M1/M8. Grade: strong.
76. `B003 عزم محكم جمع الرأي بعد تفرقه` — Firm resolve after scattered opinion. Selected M15 weakly. Grade: weak.
77. `B004 موضع أو يوم أو نداء يجمع الناس` — Gathering place/day/call. Weak with `يومئذ`; no explicit call/place. Grade: medium-weak.
78. `B005 قبضة الكف إذا ضمت الأصابع` — Fist. No hand/strike role. Grade: unlikely.
79. `B006 اتصال الجماع والمجامعة` — Intercourse. No local complement. Grade: unlikely.
80. `B007 حال المرأة أو الأنثى التي بقي حملها أو عذرها معها` — Pregnancy/virgin state. No local complement. Grade: unlikely.
81. `B008 القيد الذي يجمع اليدين إلى العنق` — Shackles. Weak with شدّ binding; no shackle role. Grade: weak.
82. `B009 اكتمال الشيء كله بلا تفرق أو نقص` — Completeness. Selected M7/M3 result wholeness. Grade: medium.
83. `B010 استجماع القوة أو السير حتى تتلاحق أجزاؤه` — Gathering strength/motion. Selected M1/M7. Grade: medium-strong.
84. `B011 نخل دقل اجتمع من النوى لا يعرف اسمه` — Date palms from seeds. Selected M13 rival. Grade: unlikely.
85. `B012 عظم الشيء كأنه جامع ممتلئ` — Great full vessel. Selected M14 rival. Grade: unlikely.
86. `B013 ممالأة واجتماع مع غيرك على أمر` — Siding together on an affair. Selected M15/M11 weakly; no coalition syntax. Grade: weak.

### 100:6:2 `ٱلْإِنسَٰنَ` — root `ء ن س`

87. `ء ن س B001 ظهور الإنسان المخالف للتوحش والجن` — Human being. Selected M4. Grade: strong.
88. `B002 إيناس الشيء برؤية أو إحساس أو سماع` — Perception by seeing/sensing/hearing. Selected M5 weakly and M9. Grade: medium.
89. `B003 الأنس الذي يزيل الوحشة` — Intimacy/removal of loneliness. Tested with Rabb relation; no companionship comfort role. Grade: weak.
90. `B004 الجانب الإنسي المقبل على الإنسان` — Human-facing side. Selected M8 weakly. Grade: weak.
91. `B005 إنسان العين وصورة الإنسان في السواد` — Pupil/image in eye. Weak with witness/seeing; no eye role. Grade: weak.
92. `B006 ابن الإنس للنفس والصفوة` — Self/close companion. Supports inner-self route weakly in M4/M6. Grade: medium-weak.

### 100:6:3 `لِرَبِّهِۦ` — root `ر ب ب`

93. `ر ب ب B001 ربوبية وملك وسيادة` — Lordship/mastery. Selected M4. Grade: strong.
94. `B002 إصلاح وتربية وإتمام` — Nurture/repair/completion. Selected M4 and tested in M13 rival. Grade: medium-strong.
95. `B003 علم رباني` — Rabbinic/divine knowledge. Selected M5 weakly with خبير/علم. Grade: weak to medium.
96. `B004 ربة وجماعات كثيرة` — Many groups. Weak with جمع; no independent route. Grade: weak.
97. `B005 ربيب وربيبة ورابة` — Fostered child/caretaker. Weak relational variant of M4. Grade: weak.
98. `B006 رُبّ خاثر وإصلاح به` — Thick syrup/repair. Selected M14/M13 rival only. Grade: unlikely.
99. `B007 لزوم وإقامة ودوام` — Staying/duration. Weak continuity support; no local anchor. Grade: weak.
100. `B008 رباب السحاب` — Clouds. Selected M13 rival. Grade: unlikely.
101. `B009 شاة رُبّى وحداثة` — Ewe/recent birth. No local role. Grade: unlikely.
102. `B010 ربابة تجمع القداح` — Container gathering lots/arrows. Selected M15 rival. Grade: unlikely.
103. `B011 ربابة عهد وميثاق` — Covenant/protection. Selected M4. Grade: medium.
104. `B012 ربة نبات` — Plant. Selected M13 rival. Grade: unlikely.
105. `B013 ماء رَبَب كثير` — Much water. Selected M13 rival. Grade: unlikely.
106. `B014 رَبْرَب قطيع` — Herd. Selected M12 weakly; no herd role. Grade: unlikely.
107. `B015 حرف رب وربما` — Particle. No passage-local root role. Grade: unlikely.
108. `B016 رُبَى حاجة وعقدة ونعمة` — Need/knot/blessing. Weak M4/M6 support; no specific syntax. Grade: weak.
109. `B017 رباني الملاحين` — Sailors’ chief. No local complement. Grade: unlikely.

### 100:6:4 `لَكَنُودٌ` — root `ك ن د`

110. `ك ن د B001 القطع والانفصال` — Cutting/separation. Selected M4/M7. Grade: medium-strong.
111. `B002 كفران النعمة والمودة` — Ingratitude. Selected M4. Grade: strong.
112. `B003 الأرض التي لا تنبت` — Barren land. Selected M13 as rejected moral-barrenness rival. Grade: weak.
113. `B004 اسم كندة` — Proper name Kinda. No local role. Grade: unlikely.

### 100:7:4 `لَشَهِيدٌ` — root `ش ه د`

114. `ش ه د B001 الحضور مع المشاهدة` — Presence with witnessing. Selected M4/M5. Grade: strong.
115. `B002 البيان بعلم` — Testimony/statement with knowledge. Selected M4/M5/M11. Grade: strong.
116. `B005 اللسان الشاهد` — Witnessing tongue/expression. Selected M5/M10. Grade: medium.
117. `B006 الخارج عند الولادة والإدراك` — Birth/maturity discharge. No local role. Grade: unlikely.
118. `B007 الشَّهْد في الشمع` — Honey in wax. Selected M14 rival; defeated. Grade: unlikely.
119. `B008 العلامة الشاهدة` — Indicating sign. Selected M5. Grade: medium.

### 100:8:2 `لِحُبِّ` — root `ح ب ب`

120. `ح ب ب B001 الحبة التي تنبت وتحمل الحب` — Seed/grain. Selected M13 rival. Grade: unlikely to weak.
121. `B002 المحبة الملازمة للقلب` — Love attached to heart. Selected M4/M6. Grade: strong.
122. `B003 صيغة المدح وغاية الرغبة` — Praise/utmost desire. Selected M6 weakly. Grade: weak.
123. `B004 حبة القلب سويداؤه` — Heart core. Selected M6 as secondary support. Grade: medium-strong.
124. `B005 البعير يلزم مكانه من عجز` — Camel stuck from exhaustion. Selected M12 weakly; no local animal role. Grade: unlikely.
125. `B006 الري حتى الامتلاء` — Fullness by drinking. Selected M13 rival. Grade: weak.
126. `B007 الحب جرة عظيمة أو موضعها` — Large jar. Selected M14/M13 rival. Grade: unlikely.
127. `B008 حباب الماء فقاقيعه وطرائقه` — Water bubbles/waves. Selected M13 rival. Grade: unlikely.
128. `B009 حبب الأسنان انتظام كالدرر` — Teeth arrangement. No local role. Grade: unlikely.
129. `B010 الحبحاب الصغير القصير` — Small/short. No local role. Grade: unlikely.
130. `B011 نار الحباحب شرر لا ينتفع به` — Useless sparks. Constrains M2 by showing weak spark branch, but not generator. Grade: weak.
131. `B012 الحباب الحية أو الشيطان` — Snake/devil. No local role. Grade: unlikely.

### 100:8:3 `ٱلْخَيْرِ` — root `خ ي ر`

132. `خ ي ر B001 الميل إلى الخير النافع` — Beneficial good. Selected M4/M6. Grade: strong.
133. `B002 فضل الصلاح والاصطفاء` — Excellence/choice. Selected M6. Grade: medium.
134. `B003 طلب الخير بالاختيار والاستخارة` — Choosing/seeking good. Selected M6 weakly. Grade: weak.
135. `B005 الكرم والهبة` — Generosity/gift. Selected M4 as benefaction contrast. Grade: medium.
136. `B006 استدراج الحيوان من جحره` — Luring animal from burrow. Weak exposure analogy with M3; no animal/burrow role. Grade: weak.

### 100:8:4 `لَشَدِيدٌ` — root `ش د د`

137. `ش د د B001 شد العقد والوثاق` — Binding/knotting. Selected M6/M7/M15. Grade: medium.
138. `B002 شدة القوة والصلابة` — Strength/intensity. Selected M4/M6. Grade: strong.
139. `B003 شد الحملة والعدو` — Charge/attack. Weak bridge back to M1; no explicit attack object. Grade: medium-weak.
140. `B004 بلوغ الأشد` — Maturity. Weak with knowledge; no maturity role. Grade: weak.
141. `B005 شد النهار وارتفاعه` — High day. Weak temporal contrast with dawn; no noon/high-day marker. Grade: weak.
142. `B006 شدة البخل` — Miserliness. Selected M4/M6 as possible narrowing of intense love of good. Grade: medium.

### 100:9:2 `يَعْلَمُ` — root `ع ل م`

143. `ع ل م B001 انكشاف الشيء للعارف` — Knowledge/disclosure. Selected M2/M3/M5/M9. Grade: strong.
144. `B002 أثر يميز الشيء ويهدي إليه` — Sign/mark. Selected M5/M9. Grade: medium.
145. `B004 شق ظاهر في الشفة العليا` — Visible cleft in upper lip. No local role. Grade: unlikely.
146. `B005 ماء كثير مجتمع في عيلم` — Much gathered water. Selected M13 rival. Grade: unlikely.
147. `B006 طائر جارح يسمى العلام` — Raptor. No local role. Grade: unlikely.
148. `B007 ذكر الضباع يسمى العيلام` — Male hyena. No local role. Grade: unlikely.

### 100:9:4 `بُعْثِرَ` — root `ب ع ث ر`

149. `ب ع ث ر B001 قلب التراب وكشف المدفون` — Overturning earth/exposing buried. Selected M2/M3. Grade: strong.
150. `B002 تبديد المتاع وقلب بعضه على بعض` — Scattering/upending baggage. Selected M7. Grade: medium.
151. `B003 هدم الحوض وقلب أسفله أعلاه` — Demolishing/upturning a trough. Selected M7 weakly and M13/M14 rejected; no trough role. Grade: weak.

### 100:9:7 `ٱلْقُبُورِ` — root `ق ب ر`

152. `ق ب ر B001 مواراة الميت في القبر` — Burial/grave. Selected M3/M16. Grade: strong in M3; unlikely as disease/death rival.
153. `B002 غموض الشيء وتطامنه` — Hiddenness/sunkenness. Selected M3/M2. Grade: medium-strong.
154. `B003 القُبَّرة الطائر` — Bird. No local role. Grade: unlikely.
155. `B004 طرف الأنف في الغضب` — Nose-tip in anger. No local role. Grade: unlikely.

### 100:10:1 `وَحُصِّلَ` — root `ح ص ل`

156. `ح ص ل B001 جمع الشيء حتى يظهر حاصله` — Collecting until result appears. Selected M3/M5/M7. Grade: strong.
157. `B002 استخراج اللب أو النفيس من غلافه` — Extracting kernel/precious thing from cover. Selected M2/M3/M6. Grade: strong.
158. `B003 البقية والحثالة بعد الرفع أو الفصل` — Residue after separation. Selected M7. Grade: medium.
159. `B004 موضع يجتمع فيه الطعام في جوف الطائر` — Bird crop. Selected M14 rival; no bird/food role. Grade: weak.
160. `B005 بلح حصل من النخلة قبل اشتداده` — Unripe dates. Selected M13 rival. Grade: unlikely.
161. `B006 وجع بطن الفرس من أكل التراب` — Horse belly pain from eating soil. Selected M12/M16 rival; defeated. Grade: unlikely.

### 100:10:4 `ٱلصُّدُورِ` — root `ص د ر`

162. `ص د ر B001 الصدر الجارحة وما يتصل بها` — Chest. Selected M3/M4/M6/M16. Grade: strong in M3/M4/M6.
163. `B002 المقدّم والأعلى والأول` — Front/top/first. Selected M8. Grade: medium.
164. `B003 الصُّدور عن المورد` — Departure from watering/source. Selected M13 rival. Grade: weak.
165. `B004 الأصل الذي تصدر عنه الأفعال` — Source/origin of acts. Selected M3/M5. Grade: medium.
166. `B005 المصادرة على مال` — Confiscation of property. Selected M11 rival. Grade: unlikely.
167. `B006 الطائفة من الشيء` — Portion. Weak with collection/result; no specific local role. Grade: weak.

### 100:11:2 `رَبَّهُم` — root `ر ب ب`, second occurrence

168. `ر ب ب B001 ربوبية وملك وسيادة` — Final lordship/mastery. Selected M4/M3 closure. Grade: strong.
169. `B002 إصلاح وتربية وإتمام` — Final care/completion. Selected M4 closure and tested M13. Grade: strong.
170. `B003 علم رباني` — Knowledge branch. Selected M5 with خبير. Grade: medium.
171. `B004 ربة وجماعات كثيرة` — Many groups. Weak plural resonance; no model. Grade: weak.
172. `B005 ربيب وربيبة ورابة` — Foster relation. Weak relational closure. Grade: weak.
173. `B006 رُبّ خاثر وإصلاح به` — Thick syrup/repair. Selected M14 rival only. Grade: unlikely.
174. `B007 لزوم وإقامة ودوام` — Staying/duration. Weak final permanence. Grade: weak.
175. `B008 رباب السحاب` — Clouds. Selected M13 rival. Grade: unlikely.
176. `B009 شاة رُبّى وحداثة` — Ewe/recent birth. No local role. Grade: unlikely.
177. `B010 ربابة تجمع القداح` — Container for lots/arrows. Selected M15 rival. Grade: unlikely.
178. `B011 ربابة عهد وميثاق` — Covenant/protection. Selected M4 as final relational return. Grade: medium.
179. `B012 ربة نبات` — Plant. Selected M13 rival. Grade: unlikely.
180. `B013 ماء رَبَب كثير` — Much water. Selected M13 rival. Grade: unlikely.
181. `B014 رَبْرَب قطيع` — Herd. Selected M12 weakly; no herd role. Grade: unlikely.
182. `B015 حرف رب وربما` — Particle. No root role. Grade: unlikely.
183. `B016 رُبَى حاجة وعقدة ونعمة` — Need/knot/blessing. Weak M4/M6 closure. Grade: weak.
184. `B017 رباني الملاحين` — Sailors’ chief. No local role. Grade: unlikely.

### 100:11:5 `لَّخَبِيرٌ` — root `خ ب ر`

185. `خ ب ر B001 العلم بالخبر وباطن الأمر` — Knowledge of report/interior affair. Selected M2/M3/M4/M5/M6. Grade: strong.
186. `B002 لين الأرض ومائها` — Soft/moist land. Selected M13 rival. Grade: weak.
187. `B003 إصلاح الأرض بالمخابرة` — Cultivating land. Selected M13 rival. Grade: weak.
188. `B004 الغزر في المزادة والناقة` — Wide/gushing waterskin/camel. Selected M12/M14 rival; no local role. Grade: unlikely.
189. `B005 اللِّين في النبات والوبر والزبد` — Soft plant/wool/froth. Selected M13 rival. Grade: unlikely.
190. `B006 القسمة في الشاة واللحم` — Shared meat/portion. Selected M11/M14 rival. Grade: weak.

## Constructional, morphosyntactic, and temporal seed-pass audit

These are independent non-lexical seeds. Each was initiated after the lexical sweep and tested against the same S100 word order, QAC morphology, attachment rows, and branch-selected models.

1. `opening-context basmala in sacred JSON` — Not initiated as a seed, per prompt. No QAC ayah-0 rows available, and no model required opening-context corroboration. Grade: not seeded.
2. `oath particle وَ governing العاديات` — Initial image: solemn opening frame. Selected M1. Corroborator: attachment 100:1 a1. Grade: strong.
3. `100:1–3 feminine plural active participles` — Initial image: same agent-set through three descriptors. Selected M1. Constraint: no explicit animal noun. Grade: strong.
4. `100:1–5 fā-chain after opening وَ` — Initial image: staged event sequence. Selected M1/M2. Grade: strong.
5. `accusative ضبحا/قدحا/صبحا` — Initial image: manner → manner → time. Selected M1/M9. Grade: medium-strong.
6. `attachment ضبحا to العاديات` — Manner seed. Selected M1/M10. Grade: strong local.
7. `attachment قدحا to الموريات` — Manner seed. Selected M1/M2. Constraint: defeats M15 shaft/lot reading. Grade: strong.
8. `attachment صبحا to المغيرات` — Time seed. Selected M1/M9. Grade: strong local.
9. `فأثرن به نقعا` — Stirring + pronoun + object seed. Selected M1/M2. Grade: strong.
10. `فوسطن به جمعا` — Middle-entry + pronoun + object seed. Selected M1/M8. Grade: strong.
11. `repeated بِهِ in 100:4–5` — Same prior force/instrument/path seed. Selected M1/M2. Constraint: antecedent remains pronominal. Grade: medium-strong.
12. `abrupt إِنَّ الإنسان after kinetic chain` — Discourse-turn seed. Selected M4. Constraint: not same grammatical subject as early FP agents. Grade: strong.
13. `لربه as target of كنود` — Relational-target seed. Selected M4. Grade: strong.
14. `إن الإنسان لربه لكنود` — Full middle predication seed. Selected M4/M7. Grade: strong.
15. `وإنه على ذلك لشهيد` — Witness-over-that seed. Selected M4/M5. Grade: strong.
16. `وإنه لحب الخير لشديد` — Love-good-intensity seed. Selected M4/M6. Grade: strong.
17. `three emphatic predicates لكنود/لشهيد/لشديد` — Layered human-state seed. Selected M4/M5/M6. Grade: strong.
18. `أفلا يعلم` — Interrogative knowledge seed. Selected M3/M5/M9. Grade: strong.
19. `إذا بعثر` — Temporal passive-disclosure seed. Selected M2/M3. Grade: strong.
20. `ما في القبور` — Hidden external container seed. Selected M3. Grade: strong.
21. `وحصل ما في الصدور` — Extracted internal container seed. Selected M3/M6. Grade: strong.
22. `parallel ما في القبور / ما في الصدور` — Dual-container seed. Selected M3. Grade: strong.
23. `passive بُعثر / حُصل` — Non-human disclosure-operation seed. Selected M2/M3/M5. Grade: strong.
24. `إذا → يومئذ` — Temporal bracket seed. Selected M3/M5/M9. Grade: medium-strong.
25. `ربه → ربهم` — Rabb-relation reactivation seed. Selected M4. Grade: strong.
26. `بهم with خبير` — Object-of-expertise seed. Selected M3/M4/M5. Grade: strong.
27. `final إن ربهم بهم يومئذ لخبير` — Closure seed. Selected M3/M4/M5. Grade: strong.
28. `singular الإنسان/إنه to plural ربهم/بهم` — Human-class-to-plural-disclosure seed. Selected M4/M3. Constraint: pronouns do not override explicit morphology. Grade: medium-strong.
29. `early outer motion → later inner contents` — Temporal reactivation seed. Selected M2/M3. Grade: medium-strong.
30. `sound/dust ambiguity at نقع` — Fork seed. M1 dust wins; M10 sound retained weakly. Grade: medium for fork, strong for dust branch, weak for sound branch.

## Exhaustiveness self-check and revisions performed in Pass 2

Coverage check before finalizing:

- Expected lexical seed passes: 190.
- Lexical seed rows present above: 190.
- Expected rooted occurrences: 24.
- Rooted occurrence sections present above: 24.
- Unique uncontaminated branch entries in the root-dossier ledger: 173.
- The additional 17 lexical seed passes come from the second `ر ب ب` occurrence at 100:11:2, producing 190 occurrence × branch passes.
- Expected constructional/morphosyntactic/temporal seeds: all prompted seed families that occur in S100 were initiated; rows present: 30.
- Potentially missing image families generated and tested in this pass: legal/compensation M11, animal/mount body M12, water/seed/nurture M13, food/vessel/share M14, arrow/lot decision M15, disease/poison/death M16.
- No branch was upgraded merely because it was vivid; each rejected rival records its defeating constraint.

Final compact interpretation: S100’s strongest reactivation trajectory is not a single static theme. The opening builds a temporally ordered kinetic incursion into a gathered center. The middle reinterprets force as a human relational breach under `ربه`, witnessed and intensified around `حب الخير`. The close reactivates the early disturbance/exposure geometry at a deeper level: hidden contents in graves and chests are overturned, extracted, and known by `ربهم ... خبير`.
