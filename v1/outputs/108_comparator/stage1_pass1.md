# S108 Stage 1 Pass 1 — comparator sweep

Assigned passage: S108, whole surah, ayat 1–3.  
Opening context in sacred file: `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`; used only as opening-context corroboration/constraint, never as seed.  
Output pass: Stage 1 Pass 1 only.

## 1. Resource compliance

Resources used:

- `resources/quran/surah_108.json` for the sacred Arabic passage and basmala opening context.
- `resources/qac.sqlite`: schema inspected; only S108:1–3 words and morphemes queried.
- `resources/attachments.tsv`: header read; only S108:1–3 rows used.
- `resources/furuq_v4.sqlite`: schema inspected; only `contaminated='no'`, `status='accepted'` branch images for S108 rooted interval roots used.

No Stage 1 Pass 2 work is included.

## 2. Sacred text and QAC sequence

Sacred Arabic text:

```text
opening-context: بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
108:1 إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ
108:2 فَصَلِّ لِرَبِّكَ وَٱنْحَرْ
108:3 إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ
```

QAC rooted word sequence:

| Ref | Surface | Root | Lemma | POS / measure |
| --- | --- | --- | --- | --- |
| 108:1:2 | أَعْطَيْنَٰكَ | ع ط و | أَعْطَىٰ | perfect verb, Form IV, 1P + 2MS object suffix |
| 108:1:3 | ٱلْكَوْثَرَ | ك ث ر | كَوْثَر | definite noun, accusative |
| 108:2:1 | فَصَلِّ | ص ل و | صَلَّىٰ | فـ + imperative verb, Form II, 2MS |
| 108:2:2 | لِرَبِّكَ | ر ب ب | رَبّ | لـ + noun, genitive, 2MS possessive suffix |
| 108:2:3 | وَٱنْحَرْ | ن ح ر | ٱنْحَرْ | و + imperative verb, 2MS |
| 108:3:2 | شَانِئَكَ | ش ن ء | شَانِئ | active participle noun, accusative, 2MS suffix |
| 108:3:4 | ٱلْأَبْتَرُ | ب ت ر | أَبْتَر | definite noun/adjective, nominative |

Important morpheme and attachment constraints:

- 108:1:1 `إِنَّا`: the suffix `نَا` is the ism of `إنّ`; the verbal clause `أَعْطَيْنَٰكَ ٱلْكَوْثَرَ` is the khabar.
- 108:1:2 `أَعْطَيْنَٰكَ`: Form IV perfect; `نَا` marks 1P subject; `كَ` is 2MS object; `ٱلْكَوْثَرَ` is the explicit accusative object.
- 108:2:1–3: `فَصَلِّ` is followed by the dedication complement `لِرَبِّكَ`; `وَٱنْحَرْ` is conjoined to the preceding imperative.
- 108:3:2: `شَانِئَكَ` is governed by `إنّ`; its `كَ` is object/construct complement of the active participle.
- 108:3:4: `ٱلْأَبْتَرُ` is the khabar of `إنّ`, with `هُوَ` separating/focusing the predicate.

## 3. Uncontaminated branch dossiers for interval roots

These are the continuous root dossiers read during the sweep. In individual seed cards below, only selected branches are carried into the image. Unselected branches are not blended into generalized root meanings.

### ع ط و

| Branch | branch_image_ar | what_is_ar |
| --- | --- | --- |
| B001 | الأخذ والتناول باليد | يدخل فيه التناول باليد ورفع اليدين إلى الورق وتناول الشيء |
| B002 | المناولة والإعطاء | يدخل فيه الإعطاء والمناولة والمعاطاة والعطاء والعطية والشيء المعطى وجمعه |
| B003 | الخدمة والمناولة للأهل | يدخل فيه خدمة الإنسان والقيام بأمره ومناولته ما يريد |
| B004 | التعاطي والخوض فيما يبلغه | يدخل فيه تعاطي ما لا حق له به أو ما لا يجوز والخوض في الأمر والتطلع إلى الرفيع بلا آلة وبلوغ الفعل بجرأة |
| B005 | استعطاء الناس | يدخل فيه سؤال العطاء وطلبه من الناس |
| B006 | اللين والانقياد والمطاوعة | يدخل فيه انقياد البعير ولين القوس ومطاوعتها وانعطاف الراحلة لصاحبها |
| B007 | الغلبة في التعاطي | يدخل فيه قولهم تعاطينا فعطوته أي غلبته |

### ك ث ر

| Branch | branch_image_ar | what_is_ar |
| --- | --- | --- |
| B001 | الكثرة ونماء العدد | يدخل فيه كثرة الشيء والعدد والمال، وضد القلة، والوصف بكثير وكثار وكاثر، وجعل الشيء كثيرا أو الاستكثار منه. |
| B002 | المكاثرة والغلبة بالعدد | يدخل فيه كاثرناهم فكثرناهم، ومكاثرة القوم إذا غلبوا غيرهم بالعدد، والتكاثر والتفاخر أو التباري بكثرة العدد والمال والعز. |
| B003 | كثرة في صاحب أو كلام أو مطالب | يدخل فيه مكثر أو كاثر بمعنى كثير المال، ومكثار في كثرة الكلام، ومكثور عليه لكثرة طالبي المعروف أو الحقوق عليه، ويتكثر بمال غيره. |
| B005 | كوثر الغبار وتكوثره | يدخل فيه الكوثر من الغبار إذا كثر وثار أو سطع، وتكوثر الشيء إذا كثر كثرة متناهية. |
| B006 | الكثر جمار النخل | يدخل فيه الكثر أو الكثر بمعنى جمار النخل، والجذب، وطلع النخل عند بعض المصادر، وما ورد في لا قطع في ثمر ولا كثر. |
| B007 | الكمثرة اجتماع الشيء | يدخل فيه الكمثرة بمعنى اجتماع الشيء، مع تصريح Maqāyīs بأن الميم زائدة وأنه من الكثرة. |

### ص ل و

| Branch | branch_image_ar | what_is_ar |
| --- | --- | --- |
| B001 | ملاقاة النار وحرها | يدخل فيه الاصطلاء بالنار والشواء والإحراق والوقود ومقاساة الحر والشدة |
| B002 | الدعاء والثناء والرحمة | يدخل فيه الدعاء للغير والتبريك والاستغفار وصلاة الله بمعنى الرحمة والثناء والتزكية |
| B003 | العبادة المخصوصة | يدخل فيه الصلاة الشرعية ذات الركوع والسجود والقيام بحدودها وإقامتها |
| B004 | الشرك المنصوبة | يدخل فيه المصالي والمصلاة التي تنصب شركا للصيد أو الإيقاع |
| B005 | الصَّلا من الظهر والجنب | يدخل فيه وسط الظهر ومكتنفا الذنب وجانبا صلا الحيوان وما يتصل بولادة الأنثى عند انفرج الصلا |
| B006 | تلو السابق في السباق | يدخل فيه المصلي من الخيل أو السابق الثاني الذي يأتي رأسه عند صلا السابق |
| B007 | مواضع الصلاة ودور العبادة | يدخل فيه الصلوات بمعنى كنائس اليهود أو مواضع صلوات الصابئين واسم موضع العبادة |
| B008 | الصَّلاية حجر الدق | يدخل فيه الصلاية والصلاءة وهي حجر عريض أو فهر يدق عليه العطر أو الهبيد |
| B009 | الصِّليان نبت ترعاه الإبل | يدخل فيه الصليان وهو نبت له سنمة أو سبطة عظيمة وتسمية العرب له خبزة الإبل |

### ر ب ب

| Branch | branch_image_ar | what_is_ar |
| --- | --- | --- |
| B001 | ربوبية وملك وسيادة | يدخل فيه الرب بمعنى الله تعالى، ومالك الشيء، وسيده المطاع، وصاحبه، ورب الدار والدابة والملك |
| B002 | إصلاح وتربية وإتمام | يدخل فيه رب الشيء إذا أصلحه وأتمه وقام عليه، ورب النعمة والصنيعة والضيعة والولد والصبي، والتربية حالا فحالا |
| B003 | علم رباني | يدخل فيه الرباني والربانيون بمعنى العلماء والحكماء وأهل العلم بالرب أو من يرب العلم ونفسه به |
| B004 | ربة وجماعات كثيرة | يدخل فيه الربة والجماعات الكثيرة، والربيون إذا فسروا بالألوف أو الجماعات، ورباب القبائل لاجتماعهم |
| B005 | ربيب وربيبة ورابة | يدخل فيه الربيب والربيبة للولد المربوب من زوج سابق، والراب والرابة لمن يقوم على أمره، والحاضنة |
| B006 | رُبّ خاثر وإصلاح به | يدخل فيه الرُّبّ الطلاء الخاثر أو ثفل السمن والزيت، والسقاء والنحي والأديم والدواء والطعام إذا جعل فيه الرُّبّ أو أصلح به |
| B007 | لزوم وإقامة ودوام | يدخل فيه رب أو أرب بالمكان إذا أقام، ومرب الإبل ومرابها، وأربت السحابة أو الجنوب إذا دامت، والإرباب بمعنى الدنو |
| B008 | رباب السحاب | يدخل فيه الرباب والربابة للسحاب، والسحاب المتعلق أو المركب بعضه على بعض، وما سمي بذلك لتربية النبات أو دوام المطر |
| B009 | شاة رُبّى وحداثة | يدخل فيه الشاة الرُّبّى والرباب لقرب العهد بالولادة أو لزوم البيت للبن، وربان الشيء بمعنى حدثانه وطراءته، وربى الشباب |
| B010 | ربابة تجمع القداح | يدخل فيه الربابة للجلدة أو الوعاء الذي تجمع فيه القداح أو سهام الميسر، وجماعة السهام نفسها |
| B011 | ربابة عهد وميثاق | يدخل فيه الربابة والرباب للعهد والميثاق والجوار، والأربة للمعاهدين، والرباب للعشور إذا جعل كالعهد |
| B012 | ربة نبات | يدخل فيه الربة والربب لضرب من الشجر أو النبت أو البقلة التي تبقى خضراء |
| B013 | ماء رَبَب كثير | يدخل فيه الربب للماء الكثير، ويقال للعذب، من جهة اجتماع الماء |
| B014 | رَبْرَب قطيع | يدخل فيه الربرب لقطيع بقر الوحش، وقيل لجماعة البقر أو الإبل |
| B015 | حرف رب وربما | يدخل فيه رب وربما وربت وربه كحرف خافض أو حرف معنى للتقليل، ودخول ما أو التاء أو الهاء عليه |
| B016 | رُبَى حاجة وعقدة ونعمة | يدخل فيه الربى بمعنى الحاجة، والرابة، والعقدة المحكمة، والنعمة والإحسان |
| B017 | رباني الملاحين | يدخل فيه الرباني لرئيس الملاحين |

### ن ح ر

| Branch | branch_image_ar | what_is_ar |
| --- | --- | --- |
| B001 | النحر صدر ظاهر | موضع النحر من الإنسان وغيره، والصدر الأعلى، وموضع القلادة، والمنحر، والنحور، وما سمي من عروقه وترقوته ودائرته |
| B002 | طعن البعير في نحره | نحر البعير والبدن والهدي، ويوم النحر، وإصابة النحر، ووصف الجواد بكثرة نحر الإبل |
| B003 | نحر يقابل نحر | استقبال الشيء ومقابلته، كدار تنحر دارا أو طريقا، والمنازل المتقابلة، وكون المرء في نحر غيره أو في أول الجيش |
| B004 | تناحر على الشيء | التشاح والتقاتل والتناحر على أمر من شدة الحرص، على صورة أن كل واحد يريد نحر صاحبه |
| B005 | نحر نفسه | انتحار الرجل، أي نحر نفسه |
| B006 | نحر الزمن حد يواجه حدا | نحر النهار وأول الشهر أو آخر يومه وليلته، والنحيرة والناحر والنواحر، حيث يواجه زمن زمنا |
| B008 | نحر العلم إتقانا | النحرير، وهو العالم المجرب أو المتقن أو الطبن الفطن الحاذق |
| B009 | انتحر السحاب بالماء | انتحار السحاب إذا اندفع بماء كثير، وتشبيه الغيث بالمنحور |

### ش ن ء

| Branch | branch_image_ar | what_is_ar |
| --- | --- | --- |
| B001 | البغضة والعداوة | يدخل فيه شنأ بمعنى أبغض، والشنآن والشنان والشنء بمعنى البغضة، والشانيء والشانئك بمعنى المبغض والعدو، والتشانؤ بمعنى التباغض. |
| B002 | التقزز والتباعد | يدخل فيه الشنوءة بمعنى التقزز والتباعد من الأدناس، وتقذر الشيء بغضا له، وما اشتق منه مثل أزد شنوءة حيث تذكره المصادر في هذا الباب. |
| B003 | إقرار الحق وإخراجه | يدخل فيه شنئت للأمر أو به بمعنى أقررت، وشنئت حقك بمعنى أقررت به وأخرجته من عندي، واستعمال شنئوا الملك بمعنى أخرجوه من عندهم. |
| B004 | وصف البغيض أو القبيح | يدخل فيه أوصاف الإنسان أو الشيء بما يورث البغض أو يدل على سوء الخلق أو قبح المنظر، مثل مشناء ومشنأ وشناءة وشنائية ومشنيئة. |

### ب ت ر

| Branch | branch_image_ar | what_is_ar |
| --- | --- | --- |
| B001 | قطع الشيء قبل تمامه | يدخل فيه بتر الشيء وقطعه قبل الإتمام، والانبتار والانقطاع، وقطع الذنب ونحوه باستئصال، والسيف الباتر أو البتار القاطع |
| B002 | انقطاع العقب والذكر والخير | يدخل فيه الأبتر لمن لا عقب له، ومن انقطع ذكره أو أثر الخير عنه، وما قيل في الأبترين لقلة خيرهما |
| B004 | قطع الرحم | يدخل فيه الرجل الأباتر الذي يقطع رحمه ويبترها |
| B006 | قصر الخلقة كأن الطول بتر | يدخل فيه بحتر بمعنى القصير المجتمع الخلق على تفسير Maqayis أنه منحوت من بتر وحتر، كأنه حرم الطول فبتر خلقه |

## 4. Progressive temporal activation trace

The hearing order creates a compact activation trajectory:

1. `إِنَّا` opens with emphasis and a plural first-person divine subject in the temporary recitation state. The basmala opening context may corroborate divine source and mercy, but does not seed the sweep.
2. `أَعْطَيْنَٰكَ` activates a completed transfer: giver → second-person recipient. The object is still unresolved until the next word.
3. `ٱلْكَوْثَرَ` completes the object as an abundant/increased thing. This creates an expectation: what does the recipient do with bestowed abundance?
4. `فَصَلِّ` answers by immediate consequence: the gift is converted into response.
5. `لِرَبِّكَ` gives the response a dedication target and reactivates the initial giver as Lord/owner/caretaker.
6. `وَٱنْحَرْ` adds a second imperative. Depending on branch, it can thicken the response as sacrifice, frontal orientation, or costly embodied dedication.
7. `إِنَّ شَانِئَكَ` introduces an opposed third party and reactivates the repeated `كَ`: the one who received abundance is also the object of hostility.
8. `هُوَ ٱلْأَبْتَرُ` closes by reversal. The opponent, not the addressee, is assigned severance. This strongly reactivates `ٱلْكَوْثَرَ` by contrast: abundance/continuity versus cut-off/removal of good or mention.

## 5. Lexical seed sweep

Conventions:

- For every lexical seed, the other S108 rooted dossiers in §3 were read as continuous branch-preserving prose. The seed cards list only branches selected into the image.
- `E` marks pre-freeze generation/expansion, `C` post-freeze corroboration, and `K` post-freeze constraint.
- Rejected/terminated branches are named when they materially tried to fork the image; otherwise “unselected dossiers” means no passage-local role survived.

### 5.1 First rooted occurrence: 108:1:2 أَعْطَيْنَٰكَ / ع ط و

For L01–L07, visited dossiers after the seed: ك ث ر, ص ل و, ر ب ب, ن ح ر, ش ن ء, ب ت ر.

#### L01 — ع ط و B001, “manual taking cannot carry the surah”

- Initial image/predictions: taking or reaching by hand predicts a handled object and recipient-side grasping `(E: ع ط و B001)`.
- Selected expansion branches: none before freeze.
- Generating set: ع ط و B001.
- Frozen model: the addressee as one who takes/receives something by hand.
- Predictions at freeze: a hand/handled medium, or later physical handling.
- Unused tested: كثر abundance, صلو worship/prayer, ربك dedication, نحر slaughter/front, شانئك hostility, الأبتر severance.
- Corroborators: the `كَ` object suffix and explicit object show a recipient and given object `(C: attachment 108:1 a3/a4)`.
- Constraints: QAC morphology is Form IV giving, not an explicit hand-taking verb `(K: morphology أَعْطَىٰ Form IV)`; no hand term or manual scene appears `(K: no hand/body-taking construction)`.
- Rival forks: none; نحر B001/B002 gives body/sacrifice but too late and not hand-specific.
- Final grade: weak. It gives a small receiving image but does not explain order or closure.

#### L02 — ع ط و B002, “bestowed abundance becomes consecrated response”

- Initial image/predictions: a completed transfer/gift asks what the recipient will do with the bestowed object `(E: ع ط و B002)`.
- Selected expansion branches: abundance fills the gift `(E: ك ث ر B001)`; Lordship/ownership gives the gift’s source and response target `(E: ر ب ب B001)`; prayer/worship and slaughter supply the commanded return `(E: ص ل و B003; E: ن ح ر B002)`.
- Generating set: ع ط و B002 + ك ث ر B001 + ر ب ب B001 + ص ل و B003 + ن ح ر B002.
- Frozen model: divine transfer of abundant good to the addressee produces an immediate, dedicated act of worship and costly offering to the Lord.
- Predictions at freeze: the recipient should remain attached to the giver; an opponent to the gift should not own the outcome; a cutting action should be consecrated, not destructive.
- Unused tested: شانئك, هو, الأبتر, the repeated `كَ`, basmala opening context, emphatic إنّ framing.
- Corroborators: the hater is introduced exactly as one directed against the gift-recipient `(C: ش ن ء B001)`; the final predicate assigns loss of posterity/mention/good to that hater `(C: ب ت ر B002)`; `هُوَ` sharpens the reversal `(C: separating pronoun/focus 108:3:3)`; basmala corroborates a divine/merciful source-frame without seeding it `(C: basmala opening-context)`.
- Constraints: the model must not identify the precise referent of `ٱلْكَوْثَرَ` beyond the passage-supported abundance/gift field `(K: no further object specification in local text)`.
- Rival forks: ن ح ر B003 can recast the second imperative as facing/orientation rather than slaughter; it yields a related but less costly response image.
- Final grade: strong. It explains sequence, roles, reactivation of `كَ`, and final closure by abundance-versus-cut-off reversal.

#### L03 — ع ط و B003, “service after being served”

- Initial image/predictions: service and provision to an intimate dependent predicts a household/caretaking relation `(E: ع ط و B003)`.
- Selected expansion branches: Lord/caretaker role `(E: ر ب ب B001/B002)`; worship as service response `(E: ص ل و B003)`; slaughter as service/offering `(E: ن ح ر B002)`.
- Generating set: ع ط و B003 + ر ب ب B001/B002 + ص ل و B003 + ن ح ر B002.
- Frozen model: the recipient, having been supplied, is placed in a service relation toward his Lord.
- Predictions at freeze: the passage should show dedication rather than private possession; hostile outsider should be excluded from the service relation.
- Unused tested: كثر, شانئك, الأبتر, فـ sequence.
- Corroborators: `فَـ` converts gift into immediate response `(C: sequence 108:1→108:2)`; `لِرَبِّكَ` supplies dedication target `(C: attachment 108:2 a1)`; هater is outside and cut off `(C: ش ن ء B001; C: ب ت ر B002)`.
- Constraints: ع ط و B003 service is not the surface sense of `أَعْطَيْنَٰكَ`; it is subordinate to the gift branch `(K: morphology/context favors giving B002)`.
- Rival forks: none.
- Final grade: medium. It coheres locally but depends on a secondary service nuance rather than the main lexical surface.

#### L04 — ع ط و B004, “unauthorized reaching is defeated”

- Initial image/predictions: bold reaching into what one has no right to predicts rivalry or overreach `(E: ع ط و B004)`.
- Selected expansion branches: competitive abundance `(E: ك ث ر B002)`; hostility `(E: ش ن ء B001)`; cutting off before completion/outcome `(E: ب ت ر B001/B002)`.
- Generating set: ع ط و B004 + ك ث ر B002 + ش ن ء B001 + ب ت ر B001/B002.
- Frozen model: an antagonist reaches toward honor/abundance without right, but the attempted contest ends in his own severance.
- Predictions at freeze: the passage should identify a rival and deny him continuation.
- Unused tested: prayer/sacrifice command, Lord attachment, gift syntax.
- Corroborators: `شَانِئَكَ` introduces an opponent `(C: active participle + object suffix)`; `هُوَ ٱلْأَبْتَرُ` assigns the failed outcome to him `(C: predicate focus)`.
- Constraints: the text never says the hater tries to seize the gift `(K: no object relation from شانئ to الكوثر)`; the actual first verb says “We gave you,” not “he reached” `(K: subject/object morphology 108:1:2)`.
- Rival forks: if كثر B002 is not selected, the branch dies as generic transgression.
- Final grade: medium. It is a plausible rival-subsystem but not the main passage model.

#### L05 — ع ط و B005, “asking people for gifts is absent”

- Initial image/predictions: seeking gifts from people predicts human petition or need `(E: ع ط و B005)`.
- Selected expansion branches: none.
- Generating set: ع ط و B005.
- Frozen model: the recipient as requester of human giving.
- Predictions at freeze: request language or human donors.
- Unused tested: divine subject, Lord dedication, worship, hater, cut-off.
- Corroborators: none.
- Constraints: `إِنَّا أَعْطَيْنَٰكَ` presents unsolicited completed divine giving, not asking people `(K: perfect 1P subject + 2MS object)`; no human donor or request appears.
- Rival forks: ر ب ب B016 need/blessing was tested but cannot overcome the absent request construction.
- Final grade: unlikely. The branch is defeated by the first clause.

#### L06 — ع ط و B006, “obedient bending after gift”

- Initial image/predictions: softness, compliance, and bending to an owner predicts command-response obedience `(E: ع ط و B006)`.
- Selected expansion branches: Lordship/ownership `(E: ر ب ب B001)`; prayer and slaughter as obeyed imperatives `(E: ص ل و B003; E: ن ح ر B002)`.
- Generating set: ع ط و B006 + ر ب ب B001 + ص ل و B003 + ن ح ر B002.
- Frozen model: bestowed abundance produces a pliant, obedient turn toward the Lord.
- Predictions at freeze: commands should follow; the addressee should be grammatically bound to Lord rather than rival.
- Unused tested: كثر, شانئك, الأبتر, فـ.
- Corroborators: two 2MS imperatives follow directly `(C: morphology IMPV 108:2:1 and 108:2:3)`; `لِرَبِّكَ` supplies the master/dedication relation `(C: attachment 108:2 a1)`.
- Constraints: compliance is a remote dimension of ع ط و here; it does not explain `ٱلْكَوْثَرَ` or closure by itself `(K: no explicit softness/bending term)`.
- Rival forks: none.
- Final grade: medium. It supports the response mechanism but not the whole surah independently.

#### L07 — ع ط و B007, “contest of taking and being overcome”

- Initial image/predictions: mutual trying and one side overcoming predicts a contest `(E: ع ط و B007)`.
- Selected expansion branches: competitive abundance `(E: ك ث ر B002)`; hostile opponent `(E: ش ن ء B001)`; severance defeat `(E: ب ت ر B001/B002)`.
- Generating set: ع ط و B007 + ك ث ر B002 + ش ن ء B001 + ب ت ر B001/B002.
- Frozen model: a rival contest over status/abundance is resolved by the opponent’s loss.
- Predictions at freeze: explicit opponent and outcome.
- Unused tested: prayer/sacrifice, Lord attachment, gift syntax.
- Corroborators: `شانئك` and final `الأبتر` fit opponent/outcome `(C: ش ن ء B001; C: ب ت ر B002)`.
- Constraints: the contest is inferred; no reciprocal contest verb appears `(K: no mutual-action morphology in passage)`; the first clause is not competitive but declarative gift.
- Rival forks: none.
- Final grade: weak. It finds the enemy-resolution subsystem but overreads the gift.

### 5.2 Second rooted occurrence: 108:1:3 ٱلْكَوْثَرَ / ك ث ر

For L08–L13, visited dossiers after the seed: ع ط و, ص ل و, ر ب ب, ن ح ر, ش ن ء, ب ت ر.

#### L08 — ك ث ر B001, “abundance opposed to severance”

- Initial image/predictions: growth, multiplicity, and increase predict continuity and an opposite of diminution `(E: ك ث ر B001)`.
- Selected expansion branches: gift transfer `(E: ع ط و B002)`; Lordship as source/owner `(E: ر ب ب B001)`; worship/sacrifice response `(E: ص ل و B003; E: ن ح ر B002)`.
- Generating set: ك ث ر B001 + ع ط و B002 + ر ب ب B001 + ص ل و B003 + ن ح ر B002.
- Frozen model: an abundant gift is received from the Lord and returned through consecrated action.
- Predictions at freeze: a later negative counterpart should mark the one excluded from abundance; closure should not continue after the contrast is assigned.
- Unused tested: شانئك, هو, الأبتر, ayah boundary.
- Corroborators: hatred supplies the excluded rival `(C: ش ن ء B001)`; `بتر B002` supplies loss of posterity/mention/good as exact counter-field `(C: ب ت ر B002)`; final ayah closes after assigning the contrast `(C: closure at 108:3)`.
- Constraints: abundance remains a compact object; no local detail specifies its kind `(K: no apposition or explanatory clause after الكوثر)`.
- Rival forks: كثر B002 yields a rivalry model, treated separately in L09.
- Final grade: strong. This is the clearest temporally reactivated contrast: `ٱلْكَوْثَرَ` becomes newly meaningful at `ٱلْأَبْتَرُ`.

#### L09 — ك ث ر B002, “rivalry by number/status is reversed”

- Initial image/predictions: boasting/competition by numbers, wealth, or honor predicts an opponent and a ranking outcome `(E: ك ث ر B002)`.
- Selected expansion branches: unauthorized reaching/contest `(E: ع ط و B004/B007)`; hostility `(E: ش ن ء B001)`; cut-off as failed rank/continuity `(E: ب ت ر B002)`.
- Generating set: ك ث ر B002 + ع ط و B004/B007 + ش ن ء B001 + ب ت ر B002.
- Frozen model: someone contests the addressee’s abundance/status, but the verdict assigns real loss to the hostile comparer.
- Predictions at freeze: opponent should be named and isolated.
- Unused tested: Lord/prayer/sacrifice and gift syntax.
- Corroborators: `شَانِئَكَ` gives a local enemy `(C: active participle + 2MS suffix)`; `هُوَ` isolates him as the true bearer of the predicate `(C: focus pronoun)`.
- Constraints: the text does not explicitly state boasting or numbers; this is a secondary branch of abundance `(K: no explicit mutual كاثر morphology)`.
- Rival forks: can remain a local enemy-resolution model without the worship response.
- Final grade: medium-strong. Specific contrast with `الأبتر` is strong; competition itself is inferred.

#### L10 — ك ث ر B003, “many claims around the possessor”

- Initial image/predictions: a possessor of much wealth/speech or many claimants predicts pressure on the recipient of abundance `(E: ك ث ر B003)`.
- Selected expansion branches: gift `(E: ع ط و B002)`; Lord as proper owner `(E: ر ب ب B001)`; hater/cut-off as false claimant excluded `(E: ش ن ء B001; E: ب ت ر B002)`.
- Generating set: ك ث ر B003 + ع ط و B002 + ر ب ب B001 + ش ن ء B001 + ب ت ر B002.
- Frozen model: the recipient has a much-demanded good, but rightful orientation is to the Lord and the hostile claimant loses share/mention.
- Predictions at freeze: dedication should control the abundance.
- Unused tested: `فَصَلِّ لِرَبِّكَ وَٱنْحَرْ`.
- Corroborators: the two imperatives prevent abundance from being private self-display `(C: sequence 108:2)`.
- Constraints: “many claimants/speech” is not explicit; the passage names only one hater `(K: singular شانئك)`.
- Rival forks: none.
- Final grade: medium. It thickens social pressure but is less exact than B001/B002.

#### L11 — ك ث ر B005, “rising dust/plume”

- Initial image/predictions: an intense rising/visible plume predicts atmospheric motion or a mass stirred upward `(E: ك ث ر B005)`.
- Selected expansion branches: possible cloud-water branch `(E: ن ح ر B009)` and cloud branch `(E: ر ب ب B008)` were tested.
- Generating set: ك ث ر B005 + optional ن ح ر B009 + optional ر ب ب B008.
- Frozen model: abundance as a rising atmospheric mass.
- Predictions at freeze: further cloud/water/weather terms.
- Unused tested: prayer, Lord, hater, cut-off.
- Corroborators: none decisive.
- Constraints: the local surface `ٱلْكَوْثَرَ` is an object of giving, not an atmospheric event `(K: direct object of أعطيناك)`; the cloud branches are remote and do not explain worship or enemy closure.
- Rival forks: water/cloud fork terminates.
- Final grade: unlikely. It is lexical coincidence without passage-local role completion.

#### L12 — ك ث ر B006, “palm core/fruit cut scene”

- Initial image/predictions: palm pith/fruit predicts plant produce and possible cutting `(E: ك ث ر B006)`.
- Selected expansion branches: بتر B001 was tested for cutting, ر ب ب B012 for green plant.
- Generating set: ك ث ر B006 only; optional tested branches did not survive.
- Frozen model: a plant/fruit object.
- Predictions at freeze: plant, fruit, cutting, cultivation.
- Unused tested: gift, prayer, Lord, slaughter, hater, cut-off.
- Corroborators: none.
- Constraints: no plant noun or cultivation action appears; `الأبتر` is predicate of the hater, not cutting fruit `(K: attachment 108:3 a3)`.
- Rival forks: plant fork dies.
- Final grade: unlikely.

#### L13 — ك ث ر B007, “gathered accumulation versus isolation”

- Initial image/predictions: accumulation/gathering predicts collected abundance and the danger of separation `(E: ك ث ر B007)`.
- Selected expansion branches: many/gathered Lord branch `(E: ر ب ب B004)`; cut-off/separation `(E: ب ت ر B002)`; hostility `(E: ش ن ء B001)`.
- Generating set: ك ث ر B007 + ر ب ب B004 + ب ت ر B002 + ش ن ء B001.
- Frozen model: a gathered plenitude stands over against the isolated cut-off opponent.
- Predictions at freeze: a severed outsider.
- Unused tested: gift syntax and worship/sacrifice.
- Corroborators: final `هو الأبتر` supplies isolated severance `(C: predicate focus)`.
- Constraints: ر ب ب B004 groups/crowds are not the local sense of `رَبِّكَ`; there is no explicit crowd scene `(K: singular ربك and شانئك)`.
- Rival forks: none.
- Final grade: weak-to-medium. It captures abundance/severance geometry but not the devotional center.

### 5.3 Third rooted occurrence: 108:2:1 فَصَلِّ / ص ل و

For L14–L22, visited dossiers after the seed: ع ط و, ك ث ر, ر ب ب, ن ح ر, ش ن ء, ب ت ر.

#### L14 — ص ل و B001, “heat/fire trial”

- Initial image/predictions: encounter with fire/heat predicts trial, burning, roasting, or sacrificial heat `(E: ص ل و B001)`.
- Selected expansion branches: ن ح ر B002 was tested as slaughter; بتر B001 as cutting.
- Generating set: ص ل و B001 + optional ن ح ر B002.
- Frozen model: heated sacrificial scene.
- Predictions at freeze: fire, cooking, burning, or explicit hardship.
- Unused tested: gift, abundance, Lord, enemy, cut-off.
- Corroborators: none local.
- Constraints: `فَصَلِّ` is Form II imperative in a dedication construction to `رَبِّكَ`, which strongly fits worship/prayer rather than heat `(K: attachment 108:2 a1; K: morphology Form II imperative)`.
- Rival forks: ritual sacrifice fork survives only through نحر, not through fire.
- Final grade: weak. It may color costly offering, but lacks local fire evidence.

#### L15 — ص ل و B002, “praise/mercy response to gift”

- Initial image/predictions: prayer, praise, blessing, mercy predicts invocation directed toward a benefactor or for another `(E: ص ل و B002)`.
- Selected expansion branches: gift `(E: ع ط و B002)`; abundance `(E: ك ث ر B001)`; Lord as addressee/source `(E: ر ب ب B001)`.
- Generating set: ص ل و B002 + ع ط و B002 + ك ث ر B001 + ر ب ب B001.
- Frozen model: bestowed abundance elicits praise/invocation toward the Lord.
- Predictions at freeze: dedication complement; second act may make praise embodied.
- Unused tested: نحر, شانئك, الأبتر, basmala.
- Corroborators: `لِرَبِّكَ` is the exact dedication complement `(C: attachment 108:2 a1)`; `وَٱنْحَرْ` adds embodied offering `(C: ن ح ر B002 if unused until after freeze)`; basmala corroborates mercy/divine source `(C: basmala opening-context)`.
- Constraints: if B002 is taken as prayer for others, the passage does not supply an intercessory object `(K: no secondary human beneficiary)`.
- Rival forks: B003 specific worship is stronger for the surface imperative.
- Final grade: medium-strong. It explains the gift-to-response transition, though B003 is more morphosyntactically exact.

#### L16 — ص ل و B003, “specified worship anchors the response”

- Initial image/predictions: formal worship/prayer predicts a dedicated addressee, ritual boundary, and obedient response `(E: ص ل و B003)`.
- Selected expansion branches: gift/abundance as cause `(E: ع ط و B002; E: ك ث ر B001)`; Lordship target `(E: ر ب ب B001)`; slaughter as paired rite `(E: ن ح ر B002)`.
- Generating set: ص ل و B003 + ع ط و B002 + ك ث ر B001 + ر ب ب B001 + ن ح ر B002.
- Frozen model: receipt of abundance is converted into commanded worship and offering to the Lord.
- Predictions at freeze: the final enemy clause should not interrupt the devotional relation but protect/reverse it.
- Unused tested: شانئك, هو, الأبتر, repeated `كَ`.
- Corroborators: the hater’s attachment to `كَ` reactivates the same recipient of the gift `(C: pronoun chain 108:1:2 → 108:2:2 → 108:3:2)`; final `بتر B002` prevents hostile severance `(C: ب ت ر B002)`.
- Constraints: worship branch does not itself generate abundance; it needs the preceding gift clause `(K: dependent on sequence 108:1→108:2)`.
- Rival forks: نحر B003 facing can be an orientation partner instead of slaughter.
- Final grade: strong. It explains why the second ayah follows the first and how the third protects the relation.

#### L17 — ص ل و B004, “trap/snare”

- Initial image/predictions: a snare or trap predicts capture/prey `(E: ص ل و B004)`.
- Selected expansion branches: شنء B001 and بتر B001 were tested as enemy caught/cut, but no local role supports a trap.
- Generating set: ص ل و B004.
- Frozen model: trap laid for an enemy.
- Predictions at freeze: prey, capture, hidden device.
- Unused tested: gift, abundance, Lord, slaughter, hater, cut-off.
- Corroborators: none.
- Constraints: the imperative is directed `لِرَبِّكَ`, not against the hater `(K: attachment 108:2 a1)`; the enemy appears only after the ritual command.
- Rival forks: enemy-trap fork dies.
- Final grade: unlikely.

#### L18 — ص ل و B005, “animal body back/side with nahr front”

- Initial image/predictions: back/side near tail predicts animal-body orientation `(E: ص ل و B005)`.
- Selected expansion branches: نحر B001/B002 for chest/slaughter; بتر B001 for tail/cutting.
- Generating set: ص ل و B005 + ن ح ر B001/B002 + ب ت ر B001.
- Frozen model: an animal-body axis from back/side to throat/cut tail.
- Predictions at freeze: body-part language should organize the passage.
- Unused tested: gift, abundance, Lord, hater.
- Corroborators: نحر supplies a real body-front branch `(C/E depending freeze: ن ح ر B001)`.
- Constraints: `فَصَلِّ` in context is not body-side vocabulary; `الأبتر` is predicate of the hater, not an animal body part `(K: attachment 108:3 a3)`.
- Rival forks: sacrifice-body image remains weakly adjacent to نحر but cannot absorb prayer.
- Final grade: weak.

#### L19 — ص ل و B006, “following after the leader”

- Initial image/predictions: the second horse following the leader predicts sequence and subordinate following `(E: ص ل و B006)`.
- Selected expansion branches: gift then response sequence `(E: ع ط و B002; E: ر ب ب B001)`; obedience branch `(E: ع ط و B006)` was tested.
- Generating set: ص ل و B006 + ع ط و B002 + ر ب ب B001.
- Frozen model: the worship act follows the prior gift and stays behind the Lord’s initiative.
- Predictions at freeze: immediate consequential ordering.
- Unused tested: `فـ`, نحر, hater/cut-off.
- Corroborators: `فَـ` strongly supports response-after-gift `(C: sequence marker 108:2:1)`.
- Constraints: no race, leader horse, or second-place frame appears `(K: no competition syntax at 108:2)`.
- Rival forks: if joined to كثر B002 competition, it becomes an enemy-race model but loses the prayer context.
- Final grade: weak. Useful as temporal metaphor only.

#### L20 — ص ل و B007, “place of prayer”

- Initial image/predictions: a worship-place predicts location or institution `(E: ص ل و B007)`.
- Selected expansion branches: رب B001 as owner/Lord.
- Generating set: ص ل و B007 + ر ب ب B001.
- Frozen model: dedication in a place of worship.
- Predictions at freeze: locative or building terms.
- Unused tested: gift, abundance, نحر, hater, cut-off.
- Corroborators: none beyond general worship.
- Constraints: no place noun, preposition of location, or building appears; `لِرَبِّكَ` is dedication, not location `(K: attachment prep_complement)`.
- Rival forks: none.
- Final grade: weak.

#### L21 — ص ل و B008, “pounding stone”

- Initial image/predictions: a broad stone for pounding predicts crushing/drying material `(E: ص ل و B008)`.
- Selected expansion branches: بتر B001 was tested as cutting; نحر B002 as slaughter.
- Generating set: ص ل و B008.
- Frozen model: preparation/crushing scene.
- Predictions at freeze: tools, substances, pounding.
- Unused tested: all remaining passage features.
- Corroborators: none.
- Constraints: no pounding tool or object appears; prayer imperative and dedication block this reading `(K: local syntax 108:2)`.
- Rival forks: none.
- Final grade: unlikely.

#### L22 — ص ل و B009, “pasture plant”

- Initial image/predictions: camel pasture plant predicts grazing/animal feed `(E: ص ل و B009)`.
- Selected expansion branches: نحر B002 animal slaughter; رب B014 herd were tested.
- Generating set: ص ل و B009.
- Frozen model: animal-pasture scene.
- Predictions at freeze: grazing, herd, plant.
- Unused tested: gift, abundance, Lord, hater, cut-off.
- Corroborators: none decisive.
- Constraints: no pasture/plant lexeme; نحر command is a ritual imperative, not a grazing scene `(K: conjoined imperative to صل)`.
- Rival forks: animal fork dies except for sacrifice in L41.
- Final grade: unlikely.

### 5.4 Fourth rooted occurrence: 108:2:2 لِرَبِّكَ / ر ب ب

For L23–L39, visited dossiers after the seed: ع ط و, ك ث ر, ص ل و, ن ح ر, ش ن ء, ب ت ر.

#### L23 — ر ب ب B001, “Lord/owner/source gathers the passage”

- Initial image/predictions: Lordship, ownership, and command authority predict giving, dedication, and obedience `(E: ر ب ب B001)`.
- Selected expansion branches: giving `(E: ع ط و B002)`; abundance `(E: ك ث ر B001)`; worship and offering `(E: ص ل و B003; E: ن ح ر B002)`.
- Generating set: ر ب ب B001 + ع ط و B002 + ك ث ر B001 + ص ل و B003 + ن ح ر B002.
- Frozen model: the Lord gives abundance and receives the addressee’s worship/offering as rightful owner.
- Predictions at freeze: an adversary opposed to the addressee should be excluded from the Lord-gift relation.
- Unused tested: شانئك, هو, الأبتر, basmala.
- Corroborators: basmala opening names the divine/mercy frame `(C: basmala opening-context)`; `ش ن ء B001 + ب ت ر B002` isolate and terminate the hostile outsider.
- Constraints: the first clause uses 1P pronoun, not the lexical word `رب`; identifying the giver with the later `ربك` is a sequence-based reactivation, not an explicit apposition `(K: no overt noun in 108:1)`.
- Rival forks: ر ب ب B002 completion model in L24.
- Final grade: strong. It explains source, target, command authority, and outsider closure.

#### L24 — ر ب ب B002, “nurture/completion counters premature cutting”

- Initial image/predictions: repairing, nurturing, completing over time predicts growth toward fullness and resistance to truncation `(E: ر ب ب B002)`.
- Selected expansion branches: abundance/growth `(E: ك ث ر B001)`; gift/nurtured favor `(E: ع ط و B002)`; worship/sacrifice as maintained response `(E: ص ل و B003; E: ن ح ر B002)`.
- Generating set: ر ب ب B002 + ك ث ر B001 + ع ط و B002 + ص ل و B003 + ن ح ر B002.
- Frozen model: the Lord’s gift is an ongoing completion/nurture process that the recipient answers ritually.
- Predictions at freeze: the opposing force should be one of interruption or failed completion.
- Unused tested: شانئك and الأبتر.
- Corroborators: بتر B001 exactly supplies cutting before completion `(C: ب ت ر B001)`; بتر B002 supplies loss of good/trace `(C: ب ت ر B002)`; hostile agent supplies the attempted interruption `(C: ش ن ء B001)`.
- Constraints: the text does not explicitly narrate growth over time; completion is a root-branch simulation `(K: no temporal adverb/process verb)`.
- Rival forks: none.
- Final grade: medium-strong. It has excellent final reactivation but less direct surface support than B001.

#### L25 — ر ب ب B003, “rabbinic/learned knowledge”

- Initial image/predictions: divine learning/wisdom predicts teaching, scholars, or knowledge transmission `(E: ر ب ب B003)`.
- Selected expansion branches: none before freeze.
- Generating set: ر ب ب B003.
- Frozen model: knowledge relation to the Lord.
- Predictions at freeze: instruction, wisdom, learned group.
- Unused tested: gift, abundance, prayer, slaughter, hater, cut-off.
- Corroborators: none.
- Constraints: no knowledge lexeme or teacher/student role appears; `لِرَبِّكَ` is dedication to Lord, not “rabbinic” learning `(K: attachment 108:2 a1)`.
- Rival forks: none.
- Final grade: unlikely.

#### L26 — ر ب ب B004, “crowds and multitudes”

- Initial image/predictions: groups/multitudes predict numerical mass `(E: ر ب ب B004)`.
- Selected expansion branches: كثرة/growth `(E: ك ث ر B001/B007)`; cut-off outsider `(E: ب ت ر B002)`.
- Generating set: ر ب ب B004 + ك ث ر B001/B007 + ب ت ر B002.
- Frozen model: abundant/gathered many against isolated severance.
- Predictions at freeze: crowd/multitude terms or plural social field.
- Unused tested: gift, worship, نحر, hater.
- Corroborators: plural `إِنَّا` weakly harmonizes with plurality but is not a crowd `(C: first-person plural, very limited)`.
- Constraints: `رَبِّكَ` is singular possessed Lord; no group noun appears `(K: singular noun + 2MS suffix)`.
- Rival forks: can support L13 but fails as own seed.
- Final grade: weak.

#### L27 — ر ب ب B005, “ward/caretaker household”

- Initial image/predictions: caretaker/ward relation predicts provision, household dependence, and service `(E: ر ب ب B005)`.
- Selected expansion branches: service-giving `(E: ع ط و B003)`; worship response `(E: ص ل و B003)`.
- Generating set: ر ب ب B005 + ع ط و B003 + ص ل و B003.
- Frozen model: protected dependent responds to caretaker/Lord.
- Predictions at freeze: care/provision and loyalty.
- Unused tested: abundance, نحر, hater, cut-off.
- Corroborators: gift to `كَ` supplies provision `(C: ع ط و B002 if unused as distinct giving dimension)`; repeated `كَ` gives dependence/attachment.
- Constraints: no family/ward term appears; `رَبّ` local branch B001/B002 is stronger `(K: no household role besides possessive suffix)`.
- Rival forks: none.
- Final grade: weak-to-medium. It is a secondary caretaking image.

#### L28 — ر ب ب B006, “thick sauce/medicine”

- Initial image/predictions: thickened substance or treatment predicts food/medicine process `(E: ر ب ب B006)`.
- Selected expansion branches: none survived; نحر B002 slaughter was tested as food source.
- Generating set: ر ب ب B006.
- Frozen model: prepared food/medicine.
- Predictions at freeze: substance, preparation, remedy.
- Unused tested: all passage features.
- Corroborators: none.
- Constraints: no food/medicine/preparation lexeme; `لِرَبِّكَ` blocks material-substance sense `(K: dedication complement)`.
- Rival forks: none.
- Final grade: unlikely.

#### L29 — ر ب ب B007, “duration versus being cut off”

- Initial image/predictions: staying, abiding, and duration predict continuity `(E: ر ب ب B007)`.
- Selected expansion branches: abundance/continuity `(E: ك ث ر B001)`; cut-off loss of continuation `(E: ب ت ر B002)`; gift/source `(E: ع ط و B002)`.
- Generating set: ر ب ب B007 + ك ث ر B001 + ب ت ر B002 + ع ط و B002.
- Frozen model: the gift has durable abiding force, while the opponent lacks continuation.
- Predictions at freeze: final contrast with severance.
- Unused tested: prayer/sacrifice and hater.
- Corroborators: `الأبتر` supplies the exact non-duration state `(C: ب ت ر B002)`; `شانئك` supplies the excluded bearer `(C: ش ن ء B001)`.
- Constraints: duration is not directly lexicalized in the local `رَبِّكَ` use `(K: no explicit stay/remain verb)`.
- Rival forks: none.
- Final grade: medium. It explains closure but not the ritual middle as well as B001/B002.

#### L30 — ر ب ب B008, “cloud mass”

- Initial image/predictions: layered cloud predicts rain/water abundance `(E: ر ب ب B008)`.
- Selected expansion branches: نحر B009 cloud pouring water; كثرة B005 intense mass.
- Generating set: ر ب ب B008 + ن ح ر B009 + ك ث ر B005.
- Frozen model: abundant gift as cloudburst.
- Predictions at freeze: water/rain terms.
- Unused tested: prayer, Lord, hater, cut-off.
- Corroborators: none local.
- Constraints: no explicit water/cloud noun; `رَبِّكَ` is the object of dedication, not a cloud `(K: QAC lemma رَبّ + possessive suffix)`.
- Rival forks: water-abundance fork reappears in L35/L47 but remains secondary.
- Final grade: weak.

#### L31 — ر ب ب B009, “fresh birth/newness”

- Initial image/predictions: newborn/freshness predicts recent origin, youth, or milk/house-lodging `(E: ر ب ب B009)`.
- Selected expansion branches: بتر B002 was tested because posterity/offspring can be cut off.
- Generating set: ر ب ب B009 + optional ب ت ر B002.
- Frozen model: new life/offspring threatened by severance.
- Predictions at freeze: birth, child, lineage.
- Unused tested: gift, abundance, prayer, slaughter, hater.
- Corroborators: بتر B002 includes lack of posterity `(C: ب ت ر B002)` if tested after freeze.
- Constraints: no birth/child term in the passage; posterity enters only through final `الأبتر`, not through `ربك` `(K: no lineage syntax)`.
- Rival forks: lineage fork is possible but underdetermined.
- Final grade: weak.

#### L32 — ر ب ب B010, “container of arrows”

- Initial image/predictions: a leather container collecting arrows predicts lots, gambling, or weapons `(E: ر ب ب B010)`.
- Selected expansion branches: none.
- Generating set: ر ب ب B010.
- Frozen model: arrow-container scene.
- Predictions at freeze: arrows, lots, weapons.
- Unused tested: all passage features.
- Corroborators: none.
- Constraints: no arrow/lot/weapon roles; prayer and slaughter are not archery `(K: local syntax 108:2)`.
- Rival forks: none.
- Final grade: unlikely.

#### L33 — ر ب ب B011, “covenant/protection relation”

- Initial image/predictions: covenant, pact, or protection predicts loyal obligation and exclusion of violator `(E: ر ب ب B011)`.
- Selected expansion branches: prayer/sacrifice as covenantal response `(E: ص ل و B003; E: ن ح ر B002)`; hater/cut-off as outsider `(E: ش ن ء B001; E: ب ت ر B002)`.
- Generating set: ر ب ب B011 + ص ل و B003 + ن ح ر B002 + ش ن ء B001 + ب ت ر B002.
- Frozen model: the gift establishes a protected obligation to the Lord; hostility is outside and severed.
- Predictions at freeze: possessive/dedication markers.
- Unused tested: gift/abundance and basmala.
- Corroborators: `لِرَبِّكَ` gives dedication/loyalty `(C: prep_complement)`; basmala opening context supports divine protection/mercy only weakly `(C: opening-context)`.
- Constraints: no explicit oath/covenant lexeme; pact relation is secondary `(K: no عهد/ميثاق term)`.
- Rival forks: none.
- Final grade: medium. It captures relational geometry but not lexical surface.

#### L34 — ر ب ب B012, “green plant continuity”

- Initial image/predictions: persistent green plant predicts vegetative life `(E: ر ب ب B012)`.
- Selected expansion branches: كثر B006 palm/fruit and ر ب ب B013 water were tested.
- Generating set: ر ب ب B012 only.
- Frozen model: plant growth.
- Predictions at freeze: plant/water/cultivation.
- Unused tested: all passage features.
- Corroborators: none decisive.
- Constraints: no plant terms; worship/hater/predicate do not complete plant roles `(K: no botanical syntax)`.
- Rival forks: none.
- Final grade: unlikely.

#### L35 — ر ب ب B013, “much/sweet water abundance”

- Initial image/predictions: abundant/sweet water predicts flowing plenty `(E: ر ب ب B013)`.
- Selected expansion branches: كثر B001 abundance; نحر B009 cloud water; ع ط و B002 gift.
- Generating set: ر ب ب B013 + ك ث ر B001 + ن ح ر B009 + ع ط و B002.
- Frozen model: the gift is simulated as plentiful water.
- Predictions at freeze: water-like abundance and excluded dryness/cutting.
- Unused tested: worship/sacrifice and hater/cut-off.
- Corroborators: `ٱلْكَوْثَرَ` as abundant object supports plenty generally `(C: ك ث ر B001 distinct abundance after freeze if not used)`; `بتر B002` opposes flow/continuity.
- Constraints: no explicit water term in S108; water image depends on remote branches `(K: no نهر/root water word in QAC)`.
- Rival forks: cloud-water image overlaps L30/L47.
- Final grade: medium. It is coherent but more remote than the abundance/severance model.

#### L36 — ر ب ب B014, “herd and animal sacrifice”

- Initial image/predictions: herd/group of wild cattle or camels predicts animal collectivity `(E: ر ب ب B014)`.
- Selected expansion branches: نحر B002 slaughter; كثر B001 abundance.
- Generating set: ر ب ب B014 + ن ح ر B002 + ك ث ر B001.
- Frozen model: abundant animals offered in slaughter.
- Predictions at freeze: animal/herd terms.
- Unused tested: gift, prayer, hater, cut-off.
- Corroborators: نحر B002 supplies sacrificial animal action if not used pre-freeze `(C/E: ن ح ر B002)`.
- Constraints: no herd noun; `رَبِّكَ` surface is Lord, not herd `(K: QAC lemma رَبّ)`.
- Rival forks: sacrifice branch survives only through نحر.
- Final grade: weak.

#### L37 — ر ب ب B015, “particle رب is morphologically blocked”

- Initial image/predictions: the particle رب/ربما predicts a limiting/approximate particle construction `(E: ر ب ب B015)`.
- Selected expansion branches: none.
- Generating set: ر ب ب B015.
- Frozen model: particle of quantity/probability.
- Predictions at freeze: particle syntax.
- Unused tested: all passage features.
- Corroborators: none.
- Constraints: QAC parses `رَبِّ` as noun stem with genitive and 2MS suffix, governed by `لِ` `(K: POS N; attachment prep_complement)`; not a particle.
- Rival forks: none.
- Final grade: unlikely.

#### L38 — ر ب ب B016, “need, knot, and blessing”

- Initial image/predictions: need/blessing/knot predicts a granted favor binding the recipient `(E: ر ب ب B016)`.
- Selected expansion branches: gift `(E: ع ط و B002)`; abundance `(E: ك ث ر B001)`; worship response `(E: ص ل و B003)`.
- Generating set: ر ب ب B016 + ع ط و B002 + ك ث ر B001 + ص ل و B003.
- Frozen model: abundant blessing creates a binding need-obligation to the Lord.
- Predictions at freeze: dedication and exclusion of hostile anti-blessing.
- Unused tested: نحر, شانئك, الأبتر.
- Corroborators: `لِرَبِّكَ` and imperatives supply binding dedication `(C: morphology 2MS imperative + prep complement)`; بتر B002 contrasts loss of good `(C: ب ت ر B002)`.
- Constraints: need/knot is not explicit; the branch works only as secondary blessing geometry `(K: no حاجة/عقدة noun)`.
- Rival forks: none.
- Final grade: medium.

#### L39 — ر ب ب B017, “chief pilot”

- Initial image/predictions: leader of sailors predicts navigation/crew `(E: ر ب ب B017)`.
- Selected expansion branches: none.
- Generating set: ر ب ب B017.
- Frozen model: nautical leadership.
- Predictions at freeze: ship, sea, pilot, crew.
- Unused tested: all passage features.
- Corroborators: none.
- Constraints: no nautical terms; local `ربك` is dedication to Lord `(K: attachment 108:2 a1)`.
- Rival forks: none.
- Final grade: unlikely.

### 5.5 Fifth rooted occurrence: 108:2:3 وَٱنْحَرْ / ن ح ر

For L40–L47, visited dossiers after the seed: ع ط و, ك ث ر, ص ل و, ر ب ب, ش ن ء, ب ت ر.

#### L40 — ن ح ر B001, “front/chest orientation”

- Initial image/predictions: exposed upper chest/front predicts facing, bodily presentation, or offering front `(E: ن ح ر B001)`.
- Selected expansion branches: worship `(E: ص ل و B003)`; Lordship target `(E: ر ب ب B001)`; facing branch B003 as close fork.
- Generating set: ن ح ر B001 + ص ل و B003 + ر ب ب B001.
- Frozen model: the addressee presents himself/frontally in worship to the Lord.
- Predictions at freeze: directional/dedication relation; opponent may be positioned against him.
- Unused tested: gift/abundance, hater/cut-off.
- Corroborators: `لِرَبِّكَ` supplies direction/dedication `(C: attachment 108:2 a1)`; `شَانِئَكَ` gives an adversarial orientation toward the addressee `(C: ش ن ء B001)`.
- Constraints: the branch is a body-place noun; the local verb imperative more directly supports slaughter/facing than “chest” alone `(K: imperative ٱنْحَرْ)`.
- Rival forks: B002 ritual cut and B003 facing are stronger.
- Final grade: medium.

#### L41 — ن ح ر B002, “sacrificial cut without becoming cut off”

- Initial image/predictions: slaughter at the throat/chest predicts a controlled, dedicated cutting action `(E: ن ح ر B002)`.
- Selected expansion branches: worship as paired rite `(E: ص ل و B003)`; Lord target `(E: ر ب ب B001)`; gift/abundance as cause `(E: ع ط و B002; E: ك ث ر B001)`.
- Generating set: ن ح ر B002 + ص ل و B003 + ر ب ب B001 + ع ط و B002 + ك ث ر B001.
- Frozen model: abundance is answered by a consecrated cut/offering directed to the Lord.
- Predictions at freeze: another kind of cutting may appear as contrast; the hostile party should receive destructive severance, not the addressee.
- Unused tested: شانئك, الأبتر.
- Corroborators: بتر B001 supplies destructive/incomplete cutting after freeze `(C: ب ت ر B001)`; بتر B002 assigns lost good/trace to the hater `(C: ب ت ر B002; C: ش ن ء B001)`.
- Constraints: do not turn `نحر` into violence against the hater; attachment says it is conjoined to prayer, not governed by enemy clause `(K: attachment 108:2 a3)`.
- Rival forks: if B003 is selected instead, the second imperative is orientation rather than slaughter.
- Final grade: medium-strong. It gives a precise cutting contrast with the close, but the main synthesis still depends on gift and abundance.

#### L42 — ن ح ر B003, “facing the Lord, opposed by the hater”

- Initial image/predictions: face-to-face orientation predicts alignment/opposition `(E: ن ح ر B003)`.
- Selected expansion branches: prayer/dedication `(E: ص ل و B003; E: ر ب ب B001)`; hater as counter-facing opponent `(E: ش ن ء B001)`.
- Generating set: ن ح ر B003 + ص ل و B003 + ر ب ب B001 + ش ن ء B001.
- Frozen model: the addressee is turned toward the Lord, while the hater is turned against him.
- Predictions at freeze: final verdict should decide which orientation has continuity.
- Unused tested: gift/abundance, abtar.
- Corroborators: gift/abundance provides the reason for turning to Lord `(C: ع ط و B002; C: ك ث ر B001)`; بتر B002 cuts off the hostile orientation `(C: ب ت ر B002)`.
- Constraints: نحر B003 is not the default ritual-sacrifice meaning of the imperative in this local pair; it remains a secondary orientation model `(K: conjoined with صل may license rite more strongly)`.
- Rival forks: B002 sacrificial action has stronger ritual concreteness.
- Final grade: medium-strong. It explains pronoun/direction geometry particularly well.

#### L43 — ن ح ر B004, “mutual conflict over the gift”

- Initial image/predictions: تناحر on something predicts fierce contest and reciprocal desire to kill/cut `(E: ن ح ر B004)`.
- Selected expansion branches: hostile hater `(E: ش ن ء B001)`; competitive abundance `(E: ك ث ر B002)`; cut-off outcome `(E: ب ت ر B001/B002)`.
- Generating set: ن ح ر B004 + ش ن ء B001 + ك ث ر B002 + ب ت ر B001/B002.
- Frozen model: a conflict over abundance resolves with the hostile party cut off.
- Predictions at freeze: enemy and verdict.
- Unused tested: prayer/Lord/gift.
- Corroborators: `شانئك` and `الأبتر` fit conflict/outcome `(C: active participle; C: predicate)`.
- Constraints: the imperative `وَٱنْحَرْ` is addressed to the addressee and joined to prayer, not a reciprocal fight `(K: 2MS imperative + attachment conjoined to صل)`.
- Rival forks: rivalry model overlaps L09 but is syntactically constrained.
- Final grade: weak-to-medium.

#### L44 — ن ح ر B005, “self-slaughter is defeated”

- Initial image/predictions: self-slaughter/suicide predicts self-directed destruction `(E: ن ح ر B005)`.
- Selected expansion branches: none.
- Generating set: ن ح ر B005.
- Frozen model: self-destruction.
- Predictions at freeze: reflexive/self object.
- Unused tested: prayer, Lord, hater, cut-off.
- Corroborators: none.
- Constraints: the imperative is conjoined with prayer and directed to Lord, not reflexive `(K: attachment 108:2 a1/a3)`; final destruction belongs to the hater, not the addressee `(K: إن شانئك هو الأبتر)`.
- Rival forks: none.
- Final grade: unlikely.

#### L45 — ن ح ر B006, “facing time boundary”

- Initial image/predictions: a temporal edge facing another edge predicts boundary/transition `(E: ن ح ر B006)`.
- Selected expansion branches: sequence gift→response→verdict; بتر B001 termination.
- Generating set: ن ح ر B006 + ب ت ر B001.
- Frozen model: a threshold at which one state faces another and closes.
- Predictions at freeze: ayah-boundary role.
- Unused tested: all lexical content.
- Corroborators: the surah does pivot at ayah 2 between gift and verdict `(C: sequence 108:1→108:2→108:3)`; final closure after `الأبتر` is sharp `(C: closure)`.
- Constraints: no explicit temporal noun; branch is remote from imperative surface `(K: no time expression)`.
- Rival forks: none.
- Final grade: weak. It can describe formal sequence, not lexical synthesis.

#### L46 — ن ح ر B008, “expert mastery”

- Initial image/predictions: expert/experienced mastery predicts skill or knowledge `(E: ن ح ر B008)`.
- Selected expansion branches: none.
- Generating set: ن ح ر B008.
- Frozen model: skilled expert action.
- Predictions at freeze: knowledge/mastery vocabulary.
- Unused tested: all passage features.
- Corroborators: none.
- Constraints: no expert/knowledge term; imperative asks an act, not expertise `(K: morphology IMPV 2MS)`.
- Rival forks: none.
- Final grade: unlikely.

#### L47 — ن ح ر B009, “cloudburst abundance”

- Initial image/predictions: cloud pouring abundant water predicts descending plenty `(E: ن ح ر B009)`.
- Selected expansion branches: كثرة B001/B005; ر ب ب B008/B013; ع ط و B002.
- Generating set: ن ح ر B009 + ك ث ر B001/B005 + ر ب ب B008/B013 + ع ط و B002.
- Frozen model: the gift as a descending/pouring abundance.
- Predictions at freeze: water/cloud/flow imagery and blocked severance.
- Unused tested: prayer, hater, abtar.
- Corroborators: general abundance supports overflowing plenty `(C: ك ث ر B001 if not used)`; abtar opposes continuity `(C: ب ت ر B002)`.
- Constraints: no local water/cloud word; `انحر` is conjoined to prayer and likely an act, not a cloud event `(K: attachment 108:2 a3)`.
- Rival forks: overlaps L35; remains secondary.
- Final grade: weak-to-medium.

### 5.6 Sixth rooted occurrence: 108:3:2 شَانِئَكَ / ش ن ء

For L48–L51, visited dossiers after the seed: ع ط و, ك ث ر, ص ل و, ر ب ب, ن ح ر, ب ت ر.

#### L48 — ش ن ء B001, “the hater is the excluded cut-off”

- Initial image/predictions: hatred/enmity predicts an opposed agent directed at the addressee `(E: ش ن ء B001)`.
- Selected expansion branches: cut-off loss of trace/good `(E: ب ت ر B002)`; abundance as what opposition cannot cancel `(E: ك ث ر B001)`; gift to addressee `(E: ع ط و B002)`.
- Generating set: ش ن ء B001 + ب ت ر B002 + ك ث ر B001 + ع ط و B002.
- Frozen model: the one hostile to the recipient of abundance is himself severed from good/trace.
- Predictions at freeze: emphatic identification of the enemy as bearer of severance; reactivation of earlier gift.
- Unused tested: prayer/sacrifice and Lord attachment.
- Corroborators: `هُوَ` isolates the hater as the predicate bearer `(C: focus pronoun)`; worship/sacrifice show the addressee’s relation is to Lord, not enemy `(C: ص ل و B003; C: ن ح ر B002; C: ر ب ب B001 if unused)`.
- Constraints: this seed starts late; it cannot by itself explain why gift and worship occur before it, except by retrospective reactivation `(K: temporal lateness)`.
- Rival forks: ش ن ء B004 ugly descriptor gives a weaker character-judgment model.
- Final grade: strong. It powerfully explains the close and backward reactivation, though less the initial gift sequence.

#### L49 — ش ن ء B002, “revulsion/distance”

- Initial image/predictions: disgusted distancing from impurity predicts separation from something considered defiled `(E: ش ن ء B002)`.
- Selected expansion branches: cut-off/separation `(E: ب ت ر B002)`; Lord/worship as pure opposing field `(E: ر ب ب B001; E: ص ل و B003)`.
- Generating set: ش ن ء B002 + ب ت ر B002 + ر ب ب B001 + ص ل و B003.
- Frozen model: the opponent distances himself and thereby becomes separated from abundance/good.
- Predictions at freeze: purity/impurity or distance markers.
- Unused tested: gift/abundance, nahr.
- Corroborators: final severance fits distancing `(C: ب ت ر B002)`.
- Constraints: no impurity/disgust vocabulary; active participle context favors plain hatred `(K: شَانِئَكَ object relation)`; the passage assigns severance rather than describing disgust.
- Rival forks: none.
- Final grade: weak.

#### L50 — ش ن ء B003, “acknowledging/extracting a right”

- Initial image/predictions: acknowledging a right and bringing it out predicts confession, payment, or removal from possession `(E: ش ن ء B003)`.
- Selected expansion branches: gift `(E: ع ط و B002)` and cut-off `(E: ب ت ر B001/B002)` were tested.
- Generating set: ش ن ء B003.
- Frozen model: someone forced to acknowledge or disgorge a right.
- Predictions at freeze: confession/right/object extraction.
- Unused tested: all other passage features.
- Corroborators: none decisive.
- Constraints: QAC marks `شَانِئَكَ` as active participle with object suffix in the enemy slot; the following predicate is not confession but `الأبتر` `(K: attachment 108:3 a1/a2/a3)`.
- Rival forks: could be a moral-verdict fork, but no explicit حق.
- Final grade: unlikely.

#### L51 — ش ن ء B004, “the repulsive/ugly opponent”

- Initial image/predictions: descriptor of the hated/ugly/bad predicts a negative character judgment `(E: ش ن ء B004)`.
- Selected expansion branches: cut-off as final shame/loss `(E: ب ت ر B002)`; hostile relation `(E: ش ن ء B001 distinct hatred dimension if tested after freeze)`.
- Generating set: ش ن ء B004 + ب ت ر B002.
- Frozen model: the one associated with repulsiveness is marked by loss of good/mention.
- Predictions at freeze: predicative condemnation.
- Unused tested: abundance/gift and worship.
- Corroborators: `هو الأبتر` is exactly a predicative condemnation `(C: attachment 108:3 a3)`.
- Constraints: B004 is descriptive and secondary; B001 is the local active-participle sense `(K: lemma شَانِئ)`.
- Rival forks: none.
- Final grade: medium.

### 5.7 Seventh rooted occurrence: 108:3:4 ٱلْأَبْتَرُ / ب ت ر

For L52–L55, visited dossiers after the seed: ع ط و, ك ث ر, ص ل و, ر ب ب, ن ح ر, ش ن ء.

#### L52 — ب ت ر B001, “destructive cutting versus consecrated cutting/completion”

- Initial image/predictions: cutting before completion predicts interruption, truncation, or destructive severance `(E: ب ت ر B001)`.
- Selected expansion branches: nurture/completion `(E: ر ب ب B002)`; abundance/growth `(E: ك ث ر B001)`; ritual slaughter as controlled cutting `(E: ن ح ر B002)`; hater as bearer `(E: ش ن ء B001)`.
- Generating set: ب ت ر B001 + ر ب ب B002 + ك ث ر B001 + ن ح ر B002 + ش ن ء B001.
- Frozen model: the hostile one is assigned the destructive cut, while the addressee’s cutting act, if any, is consecrated and paired with worship.
- Predictions at freeze: a distinction between cut-as-offering and cut-as-loss.
- Unused tested: gift syntax, prayer, Lord dedication.
- Corroborators: `وَٱنْحَرْ` is conjoined to `فَصَلِّ` and directed to Lord, not toward the enemy `(C: attachment 108:2 a3; C: attachment 108:2 a1)`; gift/abundance gives the completion field that cutting threatens `(C: ع ط و B002; C: ك ث ر B001 if unused)`.
- Constraints: do not make `الأبتر` a command to cut; it is the predicate of `شانئك` `(K: attachment 108:3 a3)`.
- Rival forks: B002 loss-of-good is even closer to the surface adjective.
- Final grade: medium-strong. It explains the nahr/batr contrast and closure well.

#### L53 — ب ت ر B002, “loss of posterity/mention/good closes the surah”

- Initial image/predictions: being cut off from posterity, mention, or good predicts a final verdict and contrast with abundance `(E: ب ت ر B002)`.
- Selected expansion branches: abundance/good `(E: ك ث ر B001)`; gift `(E: ع ط و B002)`; hostile bearer `(E: ش ن ء B001)`.
- Generating set: ب ت ر B002 + ك ث ر B001 + ع ط و B002 + ش ن ء B001.
- Frozen model: the addressee has abundant bestowed good; the enemy is the one deprived of continuing good/trace.
- Predictions at freeze: emphatic assignment to enemy and no further clause after verdict.
- Unused tested: worship/sacrifice and Lord.
- Corroborators: `هُوَ` focuses the predicate on the hater `(C: 108:3:3)`; prayer/sacrifice to Lord shows the recipient’s continuity relation is maintained `(C: ص ل و B003; C: ن ح ر B002; C: ر ب ب B001 if unused)`.
- Constraints: posterity/mention is in branch content, not locally specified by a child/lineage word `(K: no explicit عقب/ذكر noun)`.
- Rival forks: B001 cutting-before-completion provides the mechanical cut image.
- Final grade: strong. It is the strongest closing seed and best backward reactivator of `ٱلْكَوْثَرَ`.

#### L54 — ب ت ر B004, “kinship severance”

- Initial image/predictions: cutting kinship predicts relational rupture `(E: ب ت ر B004)`.
- Selected expansion branches: pronoun relationships with Lord/addressee/hater; hostility `(E: ش ن ء B001)`; Lord relation `(E: ر ب ب B001)`.
- Generating set: ب ت ر B004 + ش ن ء B001 + ر ب ب B001.
- Frozen model: the hater cuts himself from the relational network around the addressee and Lord.
- Predictions at freeze: relational suffixes should matter.
- Unused tested: repeated `كَ`, gift, worship, abundance.
- Corroborators: the `كَ` chain does organize relations: given-to-you, your Lord, your hater `(C: pronoun chain)`; hater is the one severed by predicate.
- Constraints: no kinship/رحم term appears; `ربك` is not kinship `(K: no family lexeme)`.
- Rival forks: none.
- Final grade: medium. The relation geometry is useful, but kinship is under-specified.

#### L55 — ب ت ر B006, “shortened/truncated body”

- Initial image/predictions: shortened body/form predicts physical truncation `(E: ب ت ر B006)`.
- Selected expansion branches: نحر B001 body-front; صلو B005 body-side were tested.
- Generating set: ب ت ر B006 + optional ن ح ر B001 + optional ص ل و B005.
- Frozen model: a bodily truncation image.
- Predictions at freeze: body shape, stature, tail/limb.
- Unused tested: gift, abundance, Lord, hater.
- Corroborators: نحر B001 offers body location, but not enough `(C: ن ح ر B001 weak)`.
- Constraints: `الأبتر` is predicated of a hostile person in a moral/social verdict; no bodily shortness is described `(K: attachment 108:3 a3; K: no physical descriptor besides adjective branch)`.
- Rival forks: animal-body fork overlaps L18 but remains weak.
- Final grade: weak.

## 6. Constructional, morphosyntactic, and temporal seeds

These seeds are not counted in the lexical branch count. Basmala is not used as a seed.

### C01 — construction seed: `إِنَّا أَعْطَيْنَٰكَ ٱلْكَوْثَرَ`

- Initial image/predictions: emphatic completed gift: divine/plural subject → addressee → abundant object.
- Selected branches: `(E: ع ط و B002)`, `(E: ك ث ر B001)`.
- Generating set: gift predication + ع ط و B002 + ك ث ر B001.
- Frozen model: the addressee is already secured by an emphatically completed abundance transfer.
- Predictions at freeze: next material should answer the gift or protect it from negation.
- Unused tested: ayah 2 response and ayah 3 enemy verdict.
- Corroborators: `فَصَلِّ` immediately turns possession into response `(C: sequence 108:1→108:2)`; final `الأبتر` protects by contrast `(C: ب ت ر B002)`.
- Constraints: no detail identifies the exact referent of `الكوثر` beyond local abundance.
- Final grade: strong.

### C02 — construction seed: `فَصَلِّ لِرَبِّكَ وَٱنْحَرْ`

- Initial image/predictions: consequential paired imperatives after gift.
- Selected branches: `(E: ص ل و B003)`, `(E: ر ب ب B001)`, `(E: ن ح ر B002)` with B003 as facing fork.
- Generating set: فـ response + two imperatives + Lord dedication.
- Frozen model: a gift-response system: pray/worship and offer/facing act to the Lord.
- Predictions at freeze: the final clause should not add another command but should resolve opposition to the relation.
- Unused tested: `إن شانئك هو الأبتر`.
- Corroborators: the hater is grammatically outside the imperative relation and receives the cut-off predicate `(C: ش ن ء B001; C: ب ت ر B002)`.
- Constraints: نحر must not be redirected against the hater; it is conjoined to prayer before the hater appears `(K: attachment 108:2 a3)`.
- Final grade: strong.

### C03 — construction seed: `إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ`

- Initial image/predictions: emphatic verdict: enemy of you = he himself the cut-off.
- Selected branches: `(E: ش ن ء B001)`, `(E: ب ت ر B002)`.
- Generating set: enemy noun phrase + focus pronoun + cut-off predicate.
- Frozen model: the late enemy clause reverses any perceived threat to the addressee.
- Predictions at freeze: it should reactivate earlier addressee-gift structure.
- Unused tested: `أعطيناك الكوثر`, `لربك`, paired imperatives.
- Corroborators: `كَ` in `شانئك` reactivates `كَ` in `أعطيناك` and `ربك` `(C: pronoun chain)`; abundance is the natural opposite field of cut-off `(C: ك ث ر B001)`.
- Constraints: by itself it does not explain the ritual command except as protected response.
- Final grade: strong.

### C04 — construction seed: abundance/cut-off lexical polarity `ٱلْكَوْثَرَ` ↔ `ٱلْأَبْتَرُ`

- Initial image/predictions: a polarity of surplus/increase versus severance/loss.
- Selected branches: `(E: ك ث ر B001)`, `(E: ب ت ر B002)`.
- Generating set: object of gift + final predicate contrast.
- Frozen model: the passage moves from abundance assigned to the addressee to severance assigned to the hater.
- Predictions at freeze: middle commands should show the addressee inhabiting abundance properly rather than boasting.
- Unused tested: prayer, Lord, slaughter, hater.
- Corroborators: `فَصَلِّ لِرَبِّكَ وَٱنْحَرْ` channels abundance to the Lord `(C: ص ل و B003; C: ر ب ب B001; C: ن ح ر B002)`; `شانئك` supplies the excluded bearer.
- Constraints: polarity alone can become static; the middle ayah adds the necessary response mechanism.
- Final grade: strong.

### C05 — morphosyntactic seed: repeated `كَ` chain

- Initial image/predictions: the addressee is the recurring relational hub: gift-to-you, your Lord, your hater.
- Selected branches: `(E: ع ط و B002)`, `(E: ر ب ب B001)`, `(E: ش ن ء B001)`, `(E: ب ت ر B002)`.
- Generating set: three 2MS suffixes plus final predicate.
- Frozen model: the addressee is not merely a recipient but a relational center: secured by gift, obligated to Lord, opposed by hater.
- Predictions at freeze: final predicate should not attach to the addressee but to the hostile relation.
- Unused tested: `هُوَ`, `الأبتر`, attachment rows.
- Corroborators: `هُوَ` and predicate attachment force the cut-off status onto `شانئك`, not onto `كَ` `(C: attachment 108:3 a3)`.
- Constraints: suffix chain alone cannot specify abundance/prayer content.
- Final grade: medium-strong.

### C06 — temporal seed: ayah sequence gift → response → verdict

- Initial image/predictions: the three ayahs form state transition: secured gift, required response, hostile closure.
- Selected branches: `(E: ع ط و B002)`, `(E: ك ث ر B001)`, `(E: ص ل و B003)`, `(E: ر ب ب B001)`, `(E: ن ح ر B002)`, `(E: ش ن ء B001)`, `(E: ب ت ر B002)`.
- Generating set: ordered clauses and ayah boundaries.
- Frozen model: abundance is not left static; it is activated into worship, then defended by a verdict.
- Predictions at freeze: if order were shuffled, the hater verdict would lose its backward reactivation of the gift.
- Unused tested: basmala opening context and focus pronoun.
- Corroborators: basmala supports divine-source opening `(C: opening-context)`; `هُوَ` gives the final verdict a sharp stop `(C: focus/closure)`.
- Constraints: temporal seed is structural, not a separate lexical meaning.
- Final grade: strong.

### C07 — morphosyntactic seed: paired imperatives under one dedication field

- Initial image/predictions: `فَصَلِّ` and `وَٱنْحَرْ` are both 2MS imperatives; `لِرَبِّكَ` governs/dedicates the prayer clause and semantically colors the pair.
- Selected branches: `(E: ص ل و B003)`, `(E: ن ح ر B002/B003)`, `(E: ر ب ب B001)`.
- Generating set: imperative morphology + conjunction + Lord complement.
- Frozen model: the addressee’s response has two coordinated modes: worship and offering/facing.
- Predictions at freeze: the enemy clause should be outside the command pair.
- Unused tested: attachment row 108:2 a3 and 108:3 rows.
- Corroborators: attachment says `وانحر` is conjoined to `صل`, while `الأبتر` is predicate of `شانئك` `(C: attachment 108:2 a3; C: attachment 108:3 a3)`.
- Constraints: cannot use `نحر` as enemy-directed violence.
- Final grade: medium-strong.

### C08 — morphosyntactic seed: final nominal verdict with `هو`

- Initial image/predictions: the final clause is not narrative action but identity/verdict.
- Selected branches: `(E: ش ن ء B001)`, `(E: ب ت ر B002)`.
- Generating set: `إنّ` + active participle subject + focus pronoun + definite predicate.
- Frozen model: closure occurs when the correct bearer of severance is identified.
- Predictions at freeze: no further action is needed after the verdict.
- Unused tested: abundance/gift and worship relation.
- Corroborators: lexical polarity with `الكوثر` supplies retrospective force `(C: ك ث ر B001)`; attachment places the hater, not the addressee, under the predicate.
- Constraints: does not by itself generate the middle imperative pair.
- Final grade: medium-strong.

## 7. Convergence summary

Strongest convergent synthesis:

```text
completed divine giving
  → abundant object assigned to the addressee
  → immediate consecrated response to the Lord
  → hostile relation appears
  → final predicate assigns severance to the hater
  → earlier abundance is reactivated as the opposite of being cut off
```

Primary generating/corroborating roots across independent successful seeds:

- ع ط و B002: transfer/gift.
- ك ث ر B001: abundance/growth.
- ص ل و B003/B002: worship/prayer/praise response.
- ر ب ب B001/B002: Lord/source/owner and completion/caretaking.
- ن ح ر B002/B003: offering or facing act paired with prayer.
- ش ن ء B001: hostile opposed agent.
- ب ت ر B002/B001: loss of good/trace or destructive cutting.

Best grades:

- Strong: L02, L08, L16, L23, L48, L53, C01–C04, C06.
- Medium-strong: L09, L15, L24, L41, L42, L52, C05, C07, C08.
- Medium or weaker branches mostly produce local corroboration, rival subsystems, or terminated remote images.

Short interpretation produced by the image-generation process: S108 is modeled as a gift-response-reversal system. The first ayah installs abundant divine giving; the second converts that abundance into worshipful dedication; the third reactivates the first by assigning the opposite of abundance—severed good/trace—not to the recipient but to the hostile outsider. The passage closes exactly at that predicate because the threatened relation has been reversed and no further role remains unresolved.
