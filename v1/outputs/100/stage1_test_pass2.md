# S100 — Stage 1 Test Pass 2

## Root-cause diagnosis and corrective protocol

The Pass 1 limitation had two connected causes.

1. **Model-first anchoring.** I formed a small family of promising passage models, then mapped singleton seeds back into those models. That is not equivalent to allowing every seed to change the search key independently. It favored early kinetic, disclosure, and relational images and made weak or late roots comparatively shallow.
2. **Compressed audit reporting.** I used one global convention saying that all dossiers had been visited, while each seed record displayed only selected roots. That hid the required root-by-root traversal and made an exhaustive visit look like a limited visit. It also made it harder to detect missing forks during the post-write audit.

Pass 2 restarts from 100:1:1 `ع د و B001`. Every uncontaminated branch receives an independent occurrence-level seed pass. Each pass contains an explicit 23-dossier vector in recitation order. A vector cell has one of these values:

- `S:Bxxx`: focus seed;
- `E:Bxxx`: branch selected to generate/expand before freeze;
- `F:Bxxx`: branch creates a rival fork before freeze;
- `C:Bxxx`: branch or distinct root dimension first used after freeze as corroboration;
- `K:Bxxx` or `K:local`: branch/form constrains or defeats after freeze;
- `Ø`: the entire continuous dossier was read and no branch transformed, completed, forked, corroborated, or specifically constrained that image.

The fixed vector order is:

`عدو | ضبح | وري | قدح | غير | صبح | ثور | نقع | وسط | جمع | ءنس | ربب | كند | شهد | حبب | خير | شدد | علم | بعثر | قبر | حصل | صدر | خبر`.

Thus `Ø` is an auditable refusal, not an omitted visit. Every seed separately records generating set, freeze, predictions, unused evidence tested, corroborators, constraints, rival forks, grade, and rationale. Branch density is never itself evidence.

The basmala is retained only as non-seeding opening context. QAC has no S100:0 rows, so no basmala morphology or branch dossier is inferred.

## Continuous dossier index read before singleton traversal

The Arabic titles below are the exact `branch_image_ar` values. For every seed, the corresponding full `branch_image_ar + what_is_ar` dossier was read continuously; the vectors report the selection outcome.

- `ع د و`: B001 `مجاوزة الحد والظلم`; B002 `العَدْو والحَضْر`; B003 `العَدُوّ والعداوة`; B004 `المجاوزة والاستثناء والصرف`; B005 `العَدْوى في طلب الإنصاف`; B006 `العَدْوى في انتقال الداء`; B007 `العَوادي والعادية الشاغلة`; B008 `العِداء في تعاقب الصيد`; B009 `العَداء والعُدوة في الجانب والطوار`; B010 `العَدْواء في صلابة المكان واضطرابه`; B011 `العَدَوِيّة من نبات الصيف`; B012 `العَنْدَأْوَة في الالتواء والعسر`.
- `ض ب ح`: B001 `صوت الضباح`; B002 `عدو ممدود الضبعين`; B003 `إحراق أعالي العود`; B004 `تغير اللون إلى السواد`; B005 `الرماد`.
- `و ر ي`: B001 `داء يأكل الجوف أو يصيب الرئة`; B002 `نار كامنة تخرج من الزند`; B003 `زند يقدح نجاحا أو نصرة`; B004 `شحم وار وسمن ظاهر`; B005 `ستر الشيء وجعله وراء الظهور`; B006 `الجانب الوراء: خلف أو أمام أو سوى`; B007 `ولد الولد يأتي من وراء الابن`; B008 `الورى: الخلق على ظهر الأرض`.
- `ق د ح`: B001 `إيراء النار بالقدح`; B002 `نقر الشيء وعيبه`; B003 `طعن في النسب`; B004 `أكال الشجر والسن`; B005 `غرف ما في القدر`; B006 `قدح الشرب`; B007 `عود السهم والقدح في الميسر`; B008 `ضمر الفرس وغؤور العين`; B009 `رخص أطراف النبت`; B010 `اقتداح الأمر بالنظر والتدبير`.
- `غ ي ر`: B001 `الصلاح والمنفعة بالميرة والسقي والإصلاح`; B002 `الغَيْر في الدية`; B003 `تغيير الصورة أو إبدال الشيء بغيره`; B004 `الغَيْرة على الأهل`; B005 `السوى والخلاف والاستثناء والنفي`.
- `ص ب ح`: B001 `الصبح وأول النهار`; B002 `الإتيان صباحا`; B003 `الصبوح`; B004 `يوم الصباح`; B005 `المصباح والسراج`; B006 `الصُّبْحة والصباحة`; B007 `الصُّبْحة نوما`; B008 `الناقة المصباح`; B009 `ظروف الصباح`; B010 `أصبح بمعنى صار`.
- `ث و ر`: B001 `انبعاث الشيء وانتشاره ظاهرا`; B002 `إثارة الشيء وتحريكه من موضعه`; B003 `هيجان إلى مواجهة أو غضب`; B004 `الثور: ذكر البقر`; B005 `ثورة الأقط: قطعة جامدة`; B006 `ثور اسما لمكان أو قوم أو برج`; B007 `ثور الماء: طحلب يعلو السطح`.
- `ن ق ع`: B001 `استقرار الماء وما ينقع فيه`; B002 `ماء ينقع الغلة ويروي`; B003 `نقيعة طعام أو نحر أو لبن`; B004 `نقع الغبار المثار`; B005 `نقع الصوت المرتفع`; B006 `سم ناقع ثابت أو قاتل`; B007 `نقاع الأرض القيعان السهلة`; B008 `شراب بأنقع مجرب للموارد`; B009 `نقعه بالشتم القبيح`.
- `و س ط`: B001 `العدل والخيار في موضع الوسط`; B002 `موضع الوسط بين الأطراف`; B003 `الدخول أو الجعل في الوسط`; B004 `مرتبة وسطى بين الجيد والرديء`; B005 `الوساطة بين الناس`; B006 `قطع الشيء نصفين`; B007 `الوسوط: بيت أو ناقة مخصوصة`.
- `ج م ع`: B001 `ضم المتفرق حتى يصير شيئا مجموعا`; B002 `جماعة اجتمعت أو أخلاط ضمتها الجهة`; B003 `عزم محكم جمع الرأي بعد تفرقه`; B004 `موضع أو يوم أو نداء يجمع الناس`; B005 `قبضة الكف إذا ضمت الأصابع`; B006 `اتصال الجماع والمجامعة`; B007 `حال المرأة أو الأنثى التي بقي حملها أو عذرها معها`; B008 `القيد الذي يجمع اليدين إلى العنق`; B009 `اكتمال الشيء كله بلا تفرق أو نقص`; B010 `استجماع القوة أو السير حتى تتلاحق أجزاؤه`; B011 `نخل دقل اجتمع من النوى لا يعرف اسمه`; B012 `عظم الشيء كأنه جامع ممتلئ`; B013 `ممالأة واجتماع مع غيرك على أمر`.
- `ء ن س`: B001 `ظهور الإنسان المخالف للتوحش والجن`; B002 `إيناس الشيء برؤية أو إحساس أو سماع`; B003 `الأنس الذي يزيل الوحشة`; B004 `الجانب الإنسي المقبل على الإنسان`; B005 `إنسان العين وصورة الإنسان في السواد`; B006 `ابن الإنس للنفس والصفوة`.
- `ر ب ب`: B001 `ربوبية وملك وسيادة`; B002 `إصلاح وتربية وإتمام`; B003 `علم رباني`; B004 `ربة وجماعات كثيرة`; B005 `ربيب وربيبة ورابة`; B006 `رُبّ خاثر وإصلاح به`; B007 `لزوم وإقامة ودوام`; B008 `رباب السحاب`; B009 `شاة رُبّى وحداثة`; B010 `ربابة تجمع القداح`; B011 `ربابة عهد وميثاق`; B012 `ربة نبات`; B013 `ماء رَبَب كثير`; B014 `رَبْرَب قطيع`; B015 `حرف رب وربما`; B016 `رُبَى حاجة وعقدة ونعمة`; B017 `رباني الملاحين`.
- `ك ن د`: B001 `القطع والانفصال`; B002 `كفران النعمة والمودة`; B003 `الأرض التي لا تنبت`; B004 `اسم كندة`.
- `ش ه د`: B001 `الحضور مع المشاهدة`; B002 `البيان بعلم`; B005 `اللسان الشاهد`; B006 `الخارج عند الولادة والإدراك`; B007 `الشَّهْد في الشمع`; B008 `العلامة الشاهدة`.
- `ح ب ب`: B001 `الحبة التي تنبت وتحمل الحب`; B002 `المحبة الملازمة للقلب`; B003 `صيغة المدح وغاية الرغبة`; B004 `حبة القلب سويداؤه`; B005 `البعير يلزم مكانه من عجز`; B006 `الري حتى الامتلاء`; B007 `الحب جرة عظيمة أو موضعها`; B008 `حباب الماء فقاقيعه وطرائقه`; B009 `حبب الأسنان انتظام كالدرر`; B010 `الحبحاب الصغير القصير`; B011 `نار الحباحب شرر لا ينتفع به`; B012 `الحباب الحية أو الشيطان`.
- `خ ي ر`: B001 `الميل إلى الخير النافع`; B002 `فضل الصلاح والاصطفاء`; B003 `طلب الخير بالاختيار والاستخارة`; B005 `الكرم والهبة`; B006 `استدراج الحيوان من جحره`.
- `ش د د`: B001 `شد العقد والوثاق`; B002 `شدة القوة والصلابة`; B003 `شد الحملة والعدو`; B004 `بلوغ الأشد`; B005 `شد النهار وارتفاعه`; B006 `شدة البخل`.
- `ع ل م`: B001 `انكشاف الشيء للعارف`; B002 `أثر يميز الشيء ويهدي إليه`; B004 `شق ظاهر في الشفة العليا`; B005 `ماء كثير مجتمع في عيلم`; B006 `طائر جارح يسمى العلام`; B007 `ذكر الضباع يسمى العيلام`.
- `ب ع ث ر`: B001 `قلب التراب وكشف المدفون`; B002 `تبديد المتاع وقلب بعضه على بعض`; B003 `هدم الحوض وقلب أسفله أعلاه`.
- `ق ب ر`: B001 `مواراة الميت في القبر`; B002 `غموض الشيء وتطامنه`; B003 `القُبَّرة الطائر`; B004 `طرف الأنف في الغضب`.
- `ح ص ل`: B001 `جمع الشيء حتى يظهر حاصله`; B002 `استخراج اللب أو النفيس من غلافه`; B003 `البقية والحثالة بعد الرفع أو الفصل`; B004 `موضع يجتمع فيه الطعام في جوف الطائر`; B005 `بلح حصل من النخلة قبل اشتداده`; B006 `وجع بطن الفرس من أكل التراب`.
- `ص د ر`: B001 `الصدر الجارحة وما يتصل بها`; B002 `المقدّم والأعلى والأول`; B003 `الصُّدور عن المورد`; B004 `الأصل الذي تصدر عنه الأفعال`; B005 `المصادرة على مال`; B006 `الطائفة من الشيء`.
- `خ ب ر`: B001 `العلم بالخبر وباطن الأمر`; B002 `لين الأرض ومائها`; B003 `إصلاح الأرض بالمخابرة`; B004 `الغزر في المزادة والناقة`; B005 `اللِّين في النبات والوبر والزبد`; B006 `القسمة في الشاة واللحم`.

## Lexical singleton traversal

### 100:1:1 `وَٱلْعَادِيَاتِ` — `ع د و`

#### B001 — limit-crossing wrong / assault

- **Initial image:** a force crosses a rightful limit; two forks arise—dawn assault and later adjudication.
- **V23:** `عدو=S:B001 | ضبح=E:B002 | وري=E:B002 | قدح=E:B001 | غير=F:B002 | صبح=E:B004 | ثور=E:B003,C:B002 | نقع=C:B004 | وسط=E:B003,F:B005 | جمع=E:B002 | ءنس=Ø | ربب=F:B001/B011 | كند=F:B002 | شهد=F:B002 | حبب=Ø | خير=Ø | شدد=C:B003 | علم=F:B001 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=F:B001`.
- **Lifecycle:** assault G=`ع د و B001 + ض ب ح B002 + و ر ي B002 + ق د ح B001 + ص ب ح B004 + ث و ر B003 + و س ط B003 + ج م ع B002`; freeze=a forceful dawn entry into a gathered body; P=opponent, impact trace, and later force echo; unused `ث و ر B002/ن ق ع B004/ش د د B003` corroborate effects and charge, while `(K: no enemy, weapon, wound, or combat predicate)` limits it. Judicial rival G=`غ ي ر B002 + و س ط B005 + ر ب ب B001/B011 + ك ن د B002 + ش ه د B002 + ع ل م B001`; freeze=wrong submitted for informed decision; P=claimant, judge, remedy; `خ ب ر B001` fills knowledge but `(K: no claim, verdict, or compensation transaction)` defeats passage-scale use. **Grade: medium** — specific opening completion, incomplete closure; judicial fork weak.

#### B002 — running gathers an effect chain

- **Initial image:** sustained running generates breath, impact, spark, dust, and central entry.
- **V23:** `عدو=S:B002 | ضبح=E:B001/B002 | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=E:B001/B002 | ثور=E:B002 | نقع=E:B004,F:B005 | وسط=E:B003 | جمع=E:B010 | ءنس=C:B001 | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=C:B011 | خير=Ø | شدد=C:B002/B003 | علم=C:B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ع د و B002 + ض ب ح B001/B002 + و ر ي B002 + ق د ح B001 + غ ي ر B003 + ص ب ح B001/B002 + ث و ر B002 + ن ق ع B004 + و س ط B003 + ج م ع B010`; freeze at 100:5=motion transforms latent matter into spark/dust and penetrates a center; P=the proposition should reuse force, trace, or inside/outside geometry. Unused `ش د د B002/B003` and `ح ب ب B011` reactivate force/sparks; `ش ه د B008 + ع ل م B002` corroborate trace; `ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002 + ص د ر B001 + خ ب ر B001` corroborate deeper disclosure. `(K: no species/rider; later love is not literal running/fire)`. Sound fork uses `ن ق ع B005` but remains subordinate to contextual dust. **Grade: strong** — broad ordered role completion with independent late reactivation.

#### B003 — enemy/hostile body

- **Initial image:** an enemy advances toward another body.
- **V23:** `عدو=S:B003 | ضبح=E:B002 | وري=Ø | قدح=Ø | غير=F:B002 | صبح=E:B004 | ثور=E:B003 | نقع=C:B004 | وسط=E:B003 | جمع=E:B002 | ءنس=Ø | ربب=F:B011 | كند=F:B001 | شهد=F:B002 | حبب=Ø | خير=Ø | شدد=C:B003 | علم=F:B001 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=F:B001`.
- **Lifecycle:** G=`ع د و B003 + ض ب ح B002 + ص ب ح B004 + ث و ر B003 + و س ط B003 + ج م ع B002`; freeze=hostile dawn encounter; P=opponent and collision. `ن ق ع B004` and `ش د د B003` corroborate force only; `(K: no opposing party or hostility relation)` terminates literal hostility. A weak covenant-dispute fork recruits `ر ب ب B011 + ك ن د B001 + ش ه د B002 + ع ل م B001 + خ ب ر B001`, but lacks legal roles. **Grade: weak**.

#### B004 — crossing from edge to interior

- **Initial image:** an outer limit is crossed and a center becomes the next search target.
- **V23:** `عدو=S:B004 | ضبح=Ø | وري=E:B006 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=E:B002/B003 | جمع=E:B002 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=C:B004 | خير=F:B006 | شدد=Ø | علم=Ø | بعثر=C:B001/B003 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001/B002 | خبر=C:B001`.
- **Lifecycle:** G=`ع د و B004 + و ر ي B006 + غ ي ر B003 + و س ط B002/B003 + ج م ع B002`; freeze at 100:5=edge/other-side crossing enters a gathered center; P=explicit enclosures, inside markers, and reversal out. Unused `ح ب ب B004` supplies a remote central heart-core; `ب ع ث ر B001/B003 + ق ب ر B002 + ح ص ل B002 + ص د ر B001/B002 + خ ب ر B001` satisfy enclosure, inversion, extraction, front/interior, and inward knowledge. `خ ي ر B006` creates a burrow-exit rival but `(K: no animal/lure/second opening)` defeats it. `(K: B004 is form-remote from contextual running)`. **Grade: strong** — unused paired interiors complete the predicted geometry.

#### B005 — appeal for redress

- **Initial image:** an injured party seeks an authority's aid.
- **V23:** `عدو=S:B005 | ضبح=Ø | وري=F:B003 | قدح=F:B003 | غير=E:B002 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=E:B005 | جمع=F:B013 | ءنس=Ø | ربب=E:B001/B011 | كند=E:B002 | شهد=E:B002 | حبب=Ø | خير=F:B003 | شدد=Ø | علم=E:B001 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=F:B005 | خبر=C:B001`.
- **Lifecycle:** G=`ع د و B005 + غ ي ر B002 + و س ط B005 + ر ب ب B001/B011 + ك ن د B002 + ش ه د B002 + ع ل م B001`; freeze=authority hears wrong and testimony; P=claim, compensation, verdict, enforcement. `خ ب ر B001` corroborates informed judgment, while `و ر ي B003/ق د ح B003/ج م ع B013/خ ي ر B003/ص د ر B005` fork into aid, accusation, alliance, choice, and seizure but do not supply one controlled procedure. `(K: no claimant, judge, verdict, or transaction)`. **Grade: weak** — epistemic roles fit, constitutive legal roles fail.

#### B006 — transmitted inward ailment

- **Initial image:** injury passes into another host and attacks an interior.
- **V23:** `عدو=S:B006 | ضبح=C:B001 | وري=E:B001 | قدح=E:B004 | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=F:B006 | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=Ø | كند=Ø | شهد=Ø | حبب=F:B005 | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=F:B006 | صدر=E:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ع د و B006 + و ر ي B001 + ق د ح B004 + غ ي ر B003 + ء ن س B001 + ص د ر B001`; freeze=an ailment transfers, changes, and consumes a human chest/lung interior; P=source host, recipient, transfer syntax, disease disclosure. `ض ب ح B001` corroborates breath only; `خ ب ر B001` supplies interior knowledge. Poison `ن ق ع B006`, disabled camel `ح ب ب B005`, and horse abdominal pain `ح ص ل B006` are rival pathology forks. `(K: no host-to-host relation, illness predicate, or causal transfer; مُورِيَاتِ local fire construction controls over و ر ي B001)`. **Grade: unlikely**.

#### B007 — diversion/occupation

- **Initial image:** a recurring force occupies the human and blocks another orientation.
- **V23:** `عدو=S:B007 | ضبح=Ø | وري=Ø | قدح=F:B010 | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=F:B003 | ءنس=E:B001 | ربب=E:B001/B002 | كند=E:B002 | شهد=C:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B002/B006 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`ع د و B007 + ء ن س B001 + ر ب ب B001/B002 + ك ن د B002 + ح ب ب B002 + خ ي ر B001 + ش د د B002/B006`; freeze=a human is occupied by intense attachment to benefit and correspondingly withholds the رب relation; P=competing relational targets, witness, inward record. `ش ه د B002 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate testimony, result, inner source, and knowledge. `ق د ح B010 + ج م ع B003` fork into deliberate resolve. `(K: opening عَادِيَات does not contextually mean distraction)`. **Grade: medium** — the later relational model is coherent, seed-to-form distance remains high.

#### B008 — successive hunting/capture

- **Initial image:** one capture follows another in a single release.
- **V23:** `عدو=S:B008 | ضبح=E:B002 | وري=Ø | قدح=E:B007 | غير=Ø | صبح=E:B004 | ثور=Ø | نقع=Ø | وسط=Ø | جمع=E:B010 | ءنس=Ø | ربب=F:B010 | كند=Ø | شهد=F:B008 | حبب=Ø | خير=F:B003 | شدد=E:B003 | علم=F:B002 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=F:B002 | خبر=Ø`.
- **Lifecycle:** G=`ع د و B008 + ض ب ح B002 + ق د ح B007 + ص ب ح B004 + ج م ع B010 + ش د د B003`; freeze=rapid pursuit releases successive projectiles/captures; P=prey, two outcomes, bow/wielder. `ر ب ب B010 + ص د ر B002 + ع ل م B002 + خ ي ر B003 + ش ه د B008` build an arrow/mark/choice rival, but `(K: no prey, projectile, bow, draw, target, or paired captures)`. **Grade: weak** — a detailed apparatus forms only from remote branches.

#### B009 — side, bank, and traverse

- **Initial image:** a side/edge defines movement toward a middle and another side.
- **V23:** `عدو=S:B009 | ضبح=Ø | وري=E:B006 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=E:B007 | وسط=E:B002/B003 | جمع=E:B002 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=C:B003 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001/B002 | خبر=C:B001`.
- **Lifecycle:** G=`ع د و B009 + و ر ي B006 + غ ي ر B003 + ن ق ع B007 + و س ط B002/B003 + ج م ع B002`; freeze=terrain edge is crossed into a center; P=inside/outside reversal. `ب ع ث ر B003 + ق ب ر B002 + ح ص ل B002 + ص د ر B001/B002 + خ ب ر B001` corroborate inversion, depth, extraction, front/interior, and knowledge. `(K: no bank, valley, or named terrain; B009 is remote from active participle)`. **Grade: medium-strong** — geometry is extensive, literal terrain is absent.

#### B010 — hard uneven ground under impact

- **Initial image:** rapid movement strikes resistant ground, releasing spark and dust; later the same ground is opened more deeply.
- **V23:** `عدو=S:B010 | ضبح=E:B001/B002 | وري=E:B002 | قدح=E:B001/B002 | غير=E:B003 | صبح=E:B001 | ثور=E:B002 | نقع=E:B004/B007 | وسط=E:B003 | جمع=E:B010 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=C:B011 | خير=Ø | شدد=C:B002/B003 | علم=C:B002 | بعثر=C:B001 | قبر=C:B001/B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ع د و B010 + ض ب ح B001/B002 + و ر ي B002 + ق د ح B001/B002 + غ ي ر B003 + ص ب ح B001 + ث و ر B002 + ن ق ع B004/B007 + و س ط B003 + ج م ع B010`; freeze=surface impact makes hidden fire and ground matter visible; P=a deeper ground layer, buried contents, and inward extraction. `ح ب ب B011 + ش د د B002/B003` reactivate spark/force; `ش ه د B008 + ع ل م B002` corroborate effects as traces; `ب ع ث ر B001 + ق ب ر B001/B002 + ح ص ل B002 + ص د ر B001 + خ ب ر B001` deepen surface dust → buried contents → chest contents → inner knowledge. `(K: the ground is not explicitly named in 100:1–5)`. **Grade: strong** — this missing depth-progression image explains order and closure with several unused roles.

#### B011 — late-season vegetation

- **Initial image:** growth emerges after an earlier season and invites a nurture/yield model.
- **V23:** `عدو=S:B011 | ضبح=Ø | وري=Ø | قدح=E:B009 | غير=E:B001 | صبح=E:B001 | ثور=E:B002 | نقع=E:B007 | وسط=Ø | جمع=E:B001/B011 | ءنس=Ø | ربب=E:B002/B008/B012 | كند=E:B003 | شهد=Ø | حبب=E:B001 | خير=E:B001/B005 | شدد=Ø | علم=Ø | بعثر=E:B001 | قبر=E:B002 | حصل=E:B002/B003/B005 | صدر=Ø | خبر=C:B002/B003/B005`.
- **Lifecycle:** G=`ع د و B011 + ق د ح B009 + غ ي ر B001 + ص ب ح B001 + ث و ر B002 + ن ق ع B007 + ج م ع B001/B011 + ر ب ب B002/B008/B012 + ك ن د B003 + ح ب ب B001 + خ ي ر B001/B005 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003/B005`; freeze after 100:10=seasonal ground is nurtured, seeded, turned, and separated into yield/residue; P=cultivator/knower. `خ ب ر B002/B003/B005` supplies soil, cultivation, and plant texture, but contextual `خ ب ر B001` controls final meaning. `(K: nearly every constituent is form-remote; no season/crop is primary)`. **Grade: medium** — broad role completion, weak independence and high distance.

#### B012 — twisting difficulty

- **Initial image:** an obstacle is twisted/knotted and must be cut or opened.
- **V23:** `عدو=S:B012 | ضبح=Ø | وري=Ø | قدح=F:B002 | غير=F:B003 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=E:B006 | جمع=E:B008 | ءنس=Ø | ربب=E:B016 | كند=E:B001 | شهد=Ø | حبب=Ø | خير=Ø | شدد=E:B001 | علم=Ø | بعثر=C:B002/B003 | قبر=Ø | حصل=C:B002 | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ع د و B012 + و س ط B006 + ج م ع B008 + ر ب ب B016 + ك ن د B001 + ش د د B001`; freeze=a tightened restraint is split/cut; P=bound object, release, and recovered contents. `ب ع ث ر B002/B003 + ح ص ل B002` corroborate disruption/extraction only abstractly; `ق د ح B002 + غ ي ر B003` fork into fracture/change. `(K: no knot, shackle, bound patient, or release event)`. **Grade: weak**.

### 100:1:2 `ضَبْحًا` — `ض ب ح`

#### B001 — breath/sound becomes evidence

- **Initial image:** rapid action is first accessible as breath-sound; later channels may convert sound into trace, witness, and knowledge.
- **V23:** `عدو=E:B002 | ضبح=S:B001 | وري=F:B001,E:B002 | قدح=E:B001 | غير=Ø | صبح=E:B005 | ثور=E:B002 | نقع=F:B005,E:B004 | وسط=Ø | جمع=Ø | ءنس=E:B002 | ربب=Ø | كند=Ø | شهد=E:B001/B005/B008 | حبب=F:B009 | خير=Ø | شدد=Ø | علم=C:B001/B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ض ب ح B001 + ع د و B002 + و ر ي B002 + ق د ح B001 + ص ب ح B005 + ث و ر B002 + ن ق ع B004 + ء ن س B002 + ش ه د B001/B005/B008`; freeze after 100:7=heard exertion becomes visible effect, perceived sign, and self-witness; P=explicit cognition, direct disclosure replacing signs, and inward expertise. `ع ل م B001/B002 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002 + ص د ر B001 + خ ب ر B001` satisfy those roles. Lung illness `و ر ي B001`, raised sound `ن ق ع B005`, and teeth/mouth `ح ب ب B009` are forks; `(K: نَقْعًا is locally dust, no mouth/illness)`. **Grade: strong** — every later epistemic stage arrives in order.

#### B002 — extended-limb running

- **Initial image:** limbs extend in sustained running, gathering force before impact and entry.
- **V23:** `عدو=E:B002 | ضبح=S:B002 | وري=E:B002 | قدح=E:B001,F:B008 | غير=E:B003 | صبح=E:B002/B004 | ثور=E:B002 | نقع=E:B004/B007 | وسط=E:B003 | جمع=E:B010 | ءنس=F:B004 | ربب=F:B014 | كند=Ø | شهد=C:B008 | حبب=F:B005,C:B011 | خير=Ø | شدد=C:B002/B003 | علم=C:B002 | بعثر=C:B001 | قبر=C:B002 | حصل=F:B006,C:B002 | صدر=C:B001/B002 | خبر=C:B001`.
- **Lifecycle:** G=`ض ب ح B002 + ع د و B002 + و ر ي B002 + ق د ح B001 + غ ي ر B003 + ص ب ح B002/B004 + ث و ر B002 + ن ق ع B004/B007 + و س ط B003 + ج م ع B010`; freeze=running gathers force, ignites, disturbs ground, and reaches a center; P=late charge/trace and deeper penetration. `ح ب ب B011 + ش د د B002/B003 + ش ه د B008 + ع ل م B002 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002 + ص د ر B001/B002 + خ ب ر B001` corroborate. Lean horse `ق د ح B008`, mount-facing side `ء ن س B004`, herd `ر ب ب B014`, disabled camel `ح ب ب B005`, and soil-sick horse `ح ص ل B006` form an animal-physiology fork; `(K: no species, rider, illness, or collapse)`. **Grade: strong** for kinetic/disclosure geometry; animal fork weak.

#### B003 — fire chars the struck material

- **Initial image:** fire-starting contact burns a surface and opens a processing/refining search.
- **V23:** `عدو=F:B010 | ضبح=S:B003 | وري=E:B002 | قدح=E:B001/B002 | غير=E:B003 | صبح=F:B005 | ثور=E:B001/B002 | نقع=E:B004 | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=F:B008 | حبب=C:B011 | خير=C:B001/B002 | شدد=C:B002 | علم=F:B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002/B003 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ض ب ح B003 + و ر ي B002 + ق د ح B001/B002 + غ ي ر B003 + ث و ر B001/B002 + ن ق ع B004`; freeze=impact and heat alter a matrix, releasing fire/particles; P=valuable core, residue, and inner assessment. `ح ب ب B011 + خ ي ر B001/B002 + ش د د B002 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003 + ص د ر B001 + خ ب ر B001` corroborate spark, value, extraction/residue, and inward knowledge. Hard ground `ع د و B010`, lamp `ص ب ح B005`, and sign `ش ه د B008/ع ل م B002` are terrain/light/evidence forks. `(K: no fuel, ore, furnace, or literal refining patient; ضَبْحًا is manner of runners)`. **Grade: medium-strong** — dense process completion under high form distance.

#### B004 — heat-darkened surface

- **Initial image:** heat changes an outer surface toward blackness, raising a surface/interior contrast.
- **V23:** `عدو=Ø | ضبح=S:B004 | وري=E:B002 | قدح=E:B001/B004 | غير=E:B003 | صبح=F:B006 | ثور=E:B001 | نقع=F:B004 | وسط=Ø | جمع=Ø | ءنس=F:B005 | ربب=Ø | كند=Ø | شهد=F:B008 | حبب=E:B004 | خير=Ø | شدد=Ø | علم=F:B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002/B003 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ض ب ح B004 + و ر ي B002 + ق د ح B001/B004 + غ ي ر B003 + ث و ر B001 + ح ب ب B004`; freeze=fire darkens an exterior while a dark heart-core suggests deeper hidden matter; P=opening of coverings and core extraction. `ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003 + ص د ر B001 + خ ب ر B001` satisfy disclosure, core/residue, chest, and inner knowledge. Brightness `ص ب ح B006`, pupil-darkness `ء ن س B005`, dust `ن ق ع B004`, and marks `ش ه د B008/ع ل م B002` form visual contrast forks. `(K: no colored surface or anatomical heart is primary)`. **Grade: medium** — coherent surface/interior transformation, remote generators.

#### B005 — ash as remainder

- **Initial image:** combustion leaves particulate residue; the passage may contrast residue with extracted value.
- **V23:** `عدو=F:B010 | ضبح=S:B005 | وري=E:B002 | قدح=E:B001 | غير=Ø | صبح=Ø | ثور=E:B001/B002 | نقع=E:B004 | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=F:B011 | خير=C:B001 | شدد=Ø | علم=Ø | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002/B003 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ض ب ح B005 + و ر ي B002 + ق د ح B001 + ث و ر B001/B002 + ن ق ع B004`; freeze=fire/impact leaves airborne and settled remainder; P=separation of remainder from a valuable core. `خ ي ر B001 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003 + ص د ر B001 + خ ب ر B001` corroborate value, enclosure-opening, core/residue, and inner knowledge. `ع د و B010` supplies hard ground and `ح ب ب B011` weak sparks. `(K: dust is not identified as ash; no burned matrix)`. **Grade: medium** — extraction opposition fits, substance identity does not.

### 100:2:1 `فَٱلْمُورِيَاتِ` — `و ر ي`

#### B001 — inward disease/lung injury

- **Initial image:** an interior, especially lung/chest, is consumed or injured; panting can activate it before later chest disclosure.
- **V23:** `عدو=F:B006 | ضبح=E:B001 | وري=S:B001 | قدح=F:B004 | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=F:B006 | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=Ø | كند=Ø | شهد=Ø | حبب=F:B005 | خير=Ø | شدد=Ø | علم=Ø | بعثر=C:B001 | قبر=C:B002 | حصل=F:B006,C:B002 | صدر=E:B001 | خبر=C:B001`.
- **Lifecycle:** G=`و ر ي B001 + ض ب ح B001 + غ ي ر B003 + ء ن س B001 + ص د ر B001`; freeze=strained breath signals a changing human chest interior; P=concealed pathology exposed and known. `ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002 + خ ب ر B001` corroborate disclosure/extraction/knowledge only. Contagion `ع د و B006`, decay `ق د ح B004`, poison `ن ق ع B006`, disabled camel `ح ب ب B005`, and horse pain `ح ص ل B006` fork into incompatible pathologies. `(K: مُورِيَاتِ + قَدْحًا locally selects fire production; no disease patient or transfer)`. **Grade: weak** — predicted interior appears, pathology does not.

#### B002 — latent fire forced into appearance

- **Initial image:** hidden fire exits its holder under a strike; this creates a general hidden→manifest mechanism.
- **V23:** `عدو=E:B002/B010 | ضبح=E:B003 | وري=S:B002 | قدح=E:B001 | غير=E:B003 | صبح=E:B005 | ثور=E:B001/B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B010 | ءنس=C:B002 | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=C:B011 | خير=C:B001 | شدد=C:B002/B003 | علم=C:B001/B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002/B003 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`و ر ي B002 + ع د و B002/B010 + ض ب ح B003 + ق د ح B001 + غ ي ر B003 + ص ب ح B005 + ث و ر B001/B002 + ن ق ع B004 + و س ط B003 + ج م ع B010`; freeze=impact converts hidden potential into light/particles and carries force inward; P=late reactivation of sparks/intensity, deeper enclosure, extraction, and knowing. `ء ن س B002 + ش ه د B008 + ح ب ب B011 + ش د د B002/B003 + ع ل م B001/B002 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003 + ص د ر B001 + خ ب ر B001` independently fill perception, trace, spark, force, disclosure, core/residue, and knowledge. `(K: later love is not literal fire; no common material across all disclosures)`. **Grade: strong**.

#### B003 — successful spark / aid

- **Initial image:** a striking tool succeeds, then metaphorically becomes aid, counsel, or benefit.
- **V23:** `عدو=F:B005 | ضبح=Ø | وري=S:B003 | قدح=E:B001 | غير=E:B001 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=F:B005 | جمع=F:B013 | ءنس=Ø | ربب=E:B001/B002 | كند=E:B002 | شهد=C:B002 | حبب=E:B002 | خير=E:B001/B005 | شدد=Ø | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`و ر ي B003 + ق د ح B001 + غ ي ر B001 + ر ب ب B001/B002 + ك ن د B002 + ح ب ب B002 + خ ي ر B001/B005`; freeze=successful assistance/benefit is received but the beneficiary's relation is ungrateful and redirected toward the benefit; P=witness, result, inner source, informed closure. `ش ه د B002 + ع ل م B001 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Legal/social forks use `ع د و B005 + و س ط B005 + ج م ع B013`. `(K: no explicit helper, success event, or gift transaction; local مُورِيَاتِ concerns fire)`. **Grade: medium** — relational economy emerges, seed role is remote.

#### B004 — visible fat/fullness

- **Initial image:** a body or container is visibly full, suggesting abundance held inside.
- **V23:** `عدو=Ø | ضبح=Ø | وري=S:B004 | قدح=F:B006 | غير=F:B001 | صبح=F:B003 | ثور=Ø | نقع=E:B001/B002 | وسط=Ø | جمع=E:B012 | ءنس=Ø | ربب=E:B013 | كند=Ø | شهد=Ø | حبب=E:B006/B007 | خير=F:B005 | شدد=Ø | علم=E:B005 | بعثر=Ø | قبر=F:B002 | حصل=E:B004 | صدر=E:B001 | خبر=C:B004`.
- **Lifecycle:** G=`و ر ي B004 + ن ق ع B001/B002 + ج م ع B012 + ر ب ب B013 + ح ب ب B006/B007 + ع ل م B005 + ح ص ل B004 + ص د ر B001`; freeze=a full vessel/body stores abundant liquid/food in an interior; P=emptying or extraction and an abundance descriptor. `خ ب ر B004` corroborates large waterskin/camel abundance. Cup `ق د ح B006`, provision `غ ي ر B001`, morning drink `ص ب ح B003`, gift `خ ي ر B005`, and recessed container `ق ب ر B002` fork. `(K: no liquid, food, fat, vessel, or filling action; later فِى geometry alone is generic)`. **Grade: weak**.

#### B005 — concealment behind appearance

- **Initial image:** one layer hides what lies behind it while presenting another exterior.
- **V23:** `عدو=E:B004/B009 | ضبح=Ø | وري=S:B005 | قدح=Ø | غير=E:B003/B005 | صبح=E:B005 | ثور=E:B001 | نقع=Ø | وسط=E:B002/B003 | جمع=Ø | ءنس=E:B002/B005 | ربب=Ø | كند=Ø | شهد=E:B001/B008 | حبب=E:B004 | خير=Ø | شدد=Ø | علم=E:B001/B002 | بعثر=C:B001/B003 | قبر=C:B001/B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`و ر ي B005 + ع د و B004/B009 + غ ي ر B003/B005 + ص ب ح B005 + ث و ر B001 + و س ط B002/B003 + ء ن س B002/B005 + ش ه د B001/B008 + ح ب ب B004 + ع ل م B001/B002`; freeze=appearance/trace screens a deeper center; P=covering overturned, hidden contents extracted, inner source known. `ب ع ث ر B001/B003 + ق ب ر B001/B002 + ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` exactly fill the post-freeze roles. `(K: form-remote from fire-producing participle; visual metaphors remain secondary)`. **Grade: strong** — multiple unused closing words satisfy a precise concealment model.

#### B006 — front/back/other side

- **Initial image:** a barrier divides front from what lies behind; crossing and inversion can reverse orientation.
- **V23:** `عدو=E:B004/B009 | ضبح=Ø | وري=S:B006 | قدح=F:B007 | غير=E:B003/B005 | صبح=Ø | ثور=Ø | نقع=E:B007 | وسط=E:B002/B003 | جمع=Ø | ءنس=F:B004 | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=F:B006 | شدد=Ø | علم=Ø | بعثر=C:B003 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001/B002 | خبر=C:B001`.
- **Lifecycle:** G=`و ر ي B006 + ع د و B004/B009 + غ ي ر B003/B005 + ن ق ع B007 + و س ط B002/B003`; freeze=movement crosses from side/front through center to the concealed other side; P=bottom/top inversion, recessed interior, extraction, front/chest contrast. `ب ع ث ر B003 + ق ب ر B002 + ح ص ل B002 + ص د ر B001/B002 + خ ب ر B001` corroborate. Arrow/mount/burrow rivals use `ق د ح B007 + ء ن س B004 + خ ي ر B006`; `(K: no barrier, bow, rider, or burrow)`. **Grade: medium-strong** — coherent orientation reversal under remote seed morphology.

#### B007 — descendant behind descendant

- **Initial image:** a later generation emerges behind an earlier one.
- **V23:** `عدو=Ø | ضبح=Ø | وري=S:B007 | قدح=Ø | غير=Ø | صبح=Ø | ثور=F:B001 | نقع=Ø | وسط=Ø | جمع=E:B006/B007 | ءنس=E:B001 | ربب=E:B005/B009 | كند=Ø | شهد=E:B006 | حبب=E:B001 | خير=Ø | شدد=E:B004 | علم=Ø | بعثر=Ø | قبر=F:B001 | حصل=E:B005 | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`و ر ي B007 + ج م ع B006/B007 + ء ن س B001 + ر ب ب B005/B009 + ش ه د B006 + ح ب ب B001 + ش د د B004 + ح ص ل B005`; freeze=conception/birth/maturation yields a later human generation; P=parent-child chain and generational closure. `ث و ر B001` forks into emergence and `ق ب ر B001` into prior-generation burial, but `(K: no parent, child, birth, maturation, or genealogy; pronouns do not encode lineage)`. **Grade: unlikely** — a complete remote life-cycle with no local frame.

#### B008 — creatures spread on earth

- **Initial image:** a collective of creatures occupies the earth before the generic human appears.
- **V23:** `عدو=E:B002 | ضبح=E:B001/B002 | وري=S:B008 | قدح=Ø | غير=E:B005 | صبح=Ø | ثور=Ø | نقع=E:B007 | وسط=E:B003 | جمع=E:B002 | ءنس=E:B001 | ربب=F:B014 | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`و ر ي B008 + ع د و B002 + ض ب ح B001/B002 + غ ي ر B005 + ن ق ع B007 + و س ط B003 + ج م ع B002 + ء ن س B001`; freeze=earthly collective motion contrasts with the singular generic human; P=interiorization and final human plurality. `ص د ر B001 + خ ب ر B001` corroborate inward human closure; herd `ر ب ب B014` is a rival. `(K: the opening subjects are not named “all creatures,” and final human plural is not coreferential with opening feminine plural)`. **Grade: medium** — morphology supports the pivot, creature identity does not.

### 100:2:2 `قَدْحًا` — `ق د ح`

#### B001 — striking hidden fire

- **Initial image:** a strike releases latent flame; force, heat, light, residue, and later reactivation become open roles.
- **V23:** `عدو=E:B002/B010 | ضبح=E:B003/B005 | وري=E:B002 | قدح=S:B001 | غير=E:B003 | صبح=E:B005 | ثور=E:B001/B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B010 | ءنس=C:B002 | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=C:B011 | خير=C:B001 | شدد=C:B002/B003 | علم=C:B001/B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002/B003 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ق د ح B001 + ع د و B002/B010 + ض ب ح B003/B005 + و ر ي B002 + غ ي ر B003 + ص ب ح B005 + ث و ر B001/B002 + ن ق ع B004 + و س ط B003 + ج م ع B010`; freeze=impact turns hidden fire and settled surface matter into visible effects while gathering inward force; P=delayed spark/charge, deeper hidden contents, core/residue, and inner knowledge. `ء ن س B002 + ش ه د B008 + ح ب ب B011 + خ ي ر B001 + ش د د B002/B003 + ع ل م B001/B002 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003 + ص د ر B001 + خ ب ر B001` satisfy perception, trace, precise spark replay, value, force, disclosure, extraction, and closure. `(K: حُبّ remains love; no common literal fire-substance)`. **Grade: strong**.

#### B002 — strike leaves notch/defect

- **Initial image:** impact leaves a fissure or mark that can reveal its cause and begin opening a resistant covering.
- **V23:** `عدو=E:B010 | ضبح=F:B003 | وري=E:B002 | قدح=S:B002 | غير=E:B003 | صبح=Ø | ثور=E:B002 | نقع=E:B004 | وسط=Ø | جمع=Ø | ءنس=E:B002 | ربب=Ø | كند=F:B001 | شهد=E:B008 | حبب=Ø | خير=Ø | شدد=E:B002 | علم=E:B002 | بعثر=C:B001/B003 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ق د ح B002 + ع د و B010 + و ر ي B002 + غ ي ر B003 + ث و ر B002 + ن ق ع B004 + ء ن س B002 + ش ه د B008 + ش د د B002 + ع ل م B002`; freeze=force marks/cracks a resistant surface, producing a perceptible trace; P=covering overturned, recess opened, core extracted, inner cause known. `ب ع ث ر B001/B003 + ق ب ر B002 + ح ص ل B002 + ص د ر B001 + خ ب ر B001` corroborate. Burning `ض ب ح B003` and cutting `ك ن د B001` fork. `(K: no notched patient; قَدْحًا is manner of fire production)`. **Grade: medium-strong** — exact trace-to-opening trajectory, weak local patient.

#### B003 — attack on lineage by speech

- **Initial image:** speech wounds a person's lineage and invites testimony/judgment.
- **V23:** `عدو=F:B001/B005 | ضبح=Ø | وري=Ø | قدح=S:B003 | غير=F:B002 | صبح=Ø | ثور=Ø | نقع=E:B009 | وسط=F:B005 | جمع=F:B013 | ءنس=E:B001 | ربب=F:B001/B011 | كند=Ø | شهد=E:B002/B005 | حبب=Ø | خير=Ø | شدد=Ø | علم=E:B001 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=C:B001`.
- **Lifecycle:** G=`ق د ح B003 + ن ق ع B009 + ء ن س B001 + ش ه د B002/B005 + ع ل م B001`; freeze=abusive accusation is answered by testimony and knowledge; P=accused lineage, speaker, authority, judgment. `خ ب ر B001` corroborates informed assessment. Wrong/redress/compensation/mediation/covenant forks recruit `ع د و B001/B005 + غ ي ر B002 + و س ط B005 + ج م ع B013 + ر ب ب B001/B011`, but `(K: no speech, ancestry, accusation, or court roles)`. **Grade: unlikely**.

#### B004 — inward decay in tree/tooth

- **Initial image:** hidden corrosion eats a living or hard structure from within.
- **V23:** `عدو=F:B006 | ضبح=F:B004 | وري=E:B001 | قدح=S:B004 | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=F:B006 | وسط=Ø | جمع=Ø | ءنس=F:B005 | ربب=E:B012 | كند=E:B003 | شهد=Ø | حبب=E:B001/B004 | خير=Ø | شدد=Ø | علم=Ø | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002/B003 | صدر=C:B001 | خبر=C:B001/B003`.
- **Lifecycle:** G=`ق د ح B004 + و ر ي B001 + غ ي ر B003 + ر ب ب B012 + ك ن د B003 + ح ب ب B001/B004`; freeze=hidden decay or barrenness occupies a living interior; P=covering opened, diseased/barren core distinguished, knowledgeable evaluator. `ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003 + ص د ر B001 + خ ب ر B001/B003` corroborate disclosure and agricultural evaluation. Contagion/blackening/poison/pupil forks use `ع د و B006 + ض ب ح B004 + ن ق ع B006 + ء ن س B005`. `(K: no tree, tooth, disease, or decay predicate)`. **Grade: weak** — interior deterioration is coherent, local roles absent.

#### B005 — scooping a vessel's bottom

- **Initial image:** a container holds material at depth; effort retrieves what remains at the bottom.
- **V23:** `عدو=Ø | ضبح=Ø | وري=F:B005/B006 | قدح=S:B005 | غير=Ø | صبح=Ø | ثور=Ø | نقع=E:B001 | وسط=E:B002 | جمع=E:B012 | ءنس=Ø | ربب=F:B006 | كند=Ø | شهد=Ø | حبب=E:B007 | خير=Ø | شدد=Ø | علم=Ø | بعثر=C:B003 | قبر=C:B002 | حصل=C:B002/B003 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ق د ح B005 + ن ق ع B001 + و س ط B002 + ج م ع B012 + ح ب ب B007`; freeze=a filled vessel has a deep center and difficult remainder; P=inversion/opening, recessed enclosure, core/remainder extraction, informed inspection. `ب ع ث ر B003 + ق ب ر B002 + ح ص ل B002/B003 + ص د ر B001 + خ ب ر B001` corroborate geometry. Concealment/backside `و ر ي B005/B006` and thick syrup `ر ب ب B006` fork. `(K: no pot, scoop, liquid, or agentive retrieval; later operations are passive)`. **Grade: medium** — container-depth pattern predicts the close, substance/action roles fail.

#### B006 — drinking cup

- **Initial image:** a cup mediates morning drinking and quenching.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=S:B006 | غير=E:B001 | صبح=E:B003 | ثور=Ø | نقع=E:B001/B002 | وسط=Ø | جمع=E:B012 | ءنس=Ø | ربب=E:B013 | كند=Ø | شهد=Ø | حبب=E:B006/B007 | خير=F:B005 | شدد=Ø | علم=E:B005 | بعثر=Ø | قبر=Ø | حصل=F:B004 | صدر=F:B003 | خبر=C:B004`.
- **Lifecycle:** G=`ق د ح B006 + غ ي ر B001 + ص ب ح B003 + ن ق ع B001/B002 + ج م ع B012 + ر ب ب B013 + ح ب ب B006/B007 + ع ل م B005`; freeze=provision fills a cup/vessel and quenches at morning; P=drinker, liquid, return from source, abundant container. `خ ب ر B004` corroborates abundance; `خ ي ر B005 + ح ص ل B004 + ص د ر B003` fork into gift, bodily food-store, and departure from water. `(K: قَدْحًا is an accusative action noun attached to مُورِيَاتِ; no drinker or liquid)`. **Grade: unlikely**.

#### B007 — arrow shaft / lot

- **Initial image:** a marked shaft or lot sits in a holder, awaits selection, then may be driven toward a target.
- **V23:** `عدو=E:B008 | ضبح=Ø | وري=F:B003/B006 | قدح=S:B007 | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=E:B002 | جمع=E:B003 | ءنس=E:B004 | ربب=E:B010 | كند=Ø | شهد=E:B008 | حبب=Ø | خير=E:B003 | شدد=E:B001/B003 | علم=E:B002 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=E:B002 | خبر=Ø`.
- **Lifecycle:** G=`ق د ح B007 + ع د و B008 + و س ط B002 + ج م ع B003 + ء ن س B004 + ر ب ب B010 + ش ه د B008 + خ ي ر B003 + ش د د B001/B003 + ع ل م B002 + ص د ر B002`; freeze=a human-facing marked shaft/lot is held, chosen, and propelled from front through a center; P=bow/draw, wielder, target, result. Successful aid/backside forks use `و ر ي B003/B006`. `(K: no shaft, holder, bow, draw, chooser, target, or lot-event; all apparatus parts are remote)`. **Grade: weak** — exceptional part convergence, no governing textual event.

#### B008 — lean horse / sunken eye

- **Initial image:** exertion thins an animal while the eye recedes; bodily strain and perception fork.
- **V23:** `عدو=E:B002 | ضبح=E:B001/B002 | وري=F:B001 | قدح=S:B008 | غير=Ø | صبح=E:B002/B004 | ثور=Ø | نقع=E:B007 | وسط=Ø | جمع=E:B010 | ءنس=F:B004/B005 | ربب=F:B014 | كند=Ø | شهد=F:B001 | حبب=E:B005 | خير=Ø | شدد=E:B003 | علم=F:B001 | بعثر=Ø | قبر=Ø | حصل=E:B006 | صدر=E:B001/B002 | خبر=C:B001`.
- **Lifecycle:** animal G=`ق د ح B008 + ع د و B002 + ض ب ح B001/B002 + ص ب ح B002/B004 + ن ق ع B007 + ج م ع B010 + ح ب ب B005 + ش د د B003 + ح ص ل B006 + ص د ر B001/B002`; freeze=running animal becomes strained by ground/dust; P=species, injury, stopping. `خ ب ر B001` only supplies knowledge; `(K: no horse, emaciation, pain, or collapse)`. Eye fork uses `ء ن س B005 + ش ه د B001 + ع ل م B001`; mount-facing fork uses `ء ن س B004 + ر ب ب B014`; both lack explicit organs/rider. **Grade: weak**.

#### B009 — tender plant tips

- **Initial image:** vulnerable new growth requires soil, water/nurture, and eventual yield.
- **V23:** `عدو=E:B011 | ضبح=Ø | وري=Ø | قدح=S:B009 | غير=E:B001 | صبح=E:B001 | ثور=E:B002 | نقع=E:B002/B007 | وسط=Ø | جمع=E:B001/B011 | ءنس=Ø | ربب=E:B002/B008/B012 | كند=E:B003 | شهد=Ø | حبب=E:B001 | خير=E:B001/B005 | شدد=Ø | علم=Ø | بعثر=E:B001 | قبر=E:B002 | حصل=E:B002/B003/B005 | صدر=Ø | خبر=C:B002/B003/B005`.
- **Lifecycle:** G=`ق د ح B009 + ع د و B011 + غ ي ر B001 + ص ب ح B001 + ث و ر B002 + ن ق ع B002/B007 + ج م ع B001/B011 + ر ب ب B002/B008/B012 + ك ن د B003 + ح ب ب B001 + خ ي ر B001/B005 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003/B005`; freeze=growth receives nurture, emerges from soil, and is separated as yield/residue; P=cultivator/soil expert. `خ ب ر B002/B003/B005` fills that role. `(K: no contextual plant, water, crop, or harvest; little unused evidence remains)`. **Grade: medium** — exhaustive agricultural convergence, low independence.

#### B010 — deliberation sparks an undertaking

- **Initial image:** inward review sparks a plan, gathers resolve, chooses a valued object, and drives action.
- **V23:** `عدو=F:B007 | ضبح=Ø | وري=F:B003 | قدح=S:B010 | غير=E:B003 | صبح=Ø | ثور=E:B001 | نقع=Ø | وسط=Ø | جمع=E:B003 | ءنس=E:B006 | ربب=E:B001 | كند=E:B002 | شهد=C:B002 | حبب=E:B002 | خير=E:B003 | شدد=E:B002 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`ق د ح B010 + غ ي ر B003 + ث و ر B001 + ج م ع B003 + ء ن س B006 + ر ب ب B001 + ك ن د B002 + ح ب ب B002 + خ ي ر B003 + ش د د B002`; freeze after 100:8=an inwardly gathered plan/choice fixes intense value-orientation against the رب relation; P=self-testimony, explicit cognition, extracted inward source, final knowledge. `ش ه د B002 + ع ل م B001 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Distraction/success forks use `ع د و B007 + و ر ي B003`. `(K: no opening planner or explicit decision; قَدْحًا locally specifies fire production)`. **Grade: medium-strong** — a newly explicit intention model predicts the closing inward disclosure.

### 100:3:1 `فَٱلْمُغِيرَاتِ` — `غ ي ر`

#### B001 — provision, watering, and repair

- **Initial image:** a provider repairs/supplies dependents; gratitude and productive yield become expected roles.
- **V23:** `عدو=Ø | ضبح=Ø | وري=F:B003 | قدح=F:B009 | غير=S:B001 | صبح=F:B003 | ثور=E:B002 | نقع=E:B002/B007 | وسط=Ø | جمع=E:B001 | ءنس=E:B001 | ربب=E:B001/B002/B008/B012 | كند=E:B002/B003 | شهد=C:B002 | حبب=E:B001/B002 | خير=E:B001/B005 | شدد=E:B002/B006 | علم=Ø | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001/B002/B003 | صدر=C:B004 | خبر=C:B001/B003`.
- **Lifecycle:** relational G=`غ ي ر B001 + ء ن س B001 + ر ب ب B001/B002 + ك ن د B002 + ح ب ب B002 + خ ي ر B001/B005 + ش د د B002/B006`; freeze=benefit/nurture is supplied, yet gratitude is withheld and attachment fixes on the benefit; P=witness, inward source/result, informed provider. `ش ه د B002 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Agricultural fork adds `ث و ر B002 + ن ق ع B002/B007 + ج م ع B001 + ر ب ب B008/B012 + ك ن د B003 + ح ب ب B001 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003 + خ ب ر B003`; drink/growth/success branches are marked F. `(K: no explicit provision act or recipient in مُغِيرَاتِ)`. **Grade: medium-strong** — strong later relation; seed form remote.

#### B002 — compensation replacing retaliation

- **Initial image:** an injury is converted into compensation under testimony and authority.
- **V23:** `عدو=E:B001/B005 | ضبح=Ø | وري=F:B003 | قدح=F:B003 | غير=S:B002 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=E:B005 | جمع=E:B013 | ءنس=E:B001 | ربب=E:B001/B011 | كند=E:B001/B002 | شهد=E:B002 | حبب=Ø | خير=F:B003/B005 | شدد=Ø | علم=E:B001 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=E:B005 | خبر=C:B001`.
- **Lifecycle:** G=`غ ي ر B002 + ع د و B001/B005 + و س ط B005 + ج م ع B013 + ء ن س B001 + ر ب ب B001/B011 + ك ن د B001/B002 + ش ه د B002 + ع ل م B001 + ص د ر B005`; freeze=wrong/severed bond is mediated through testimony and property compensation; P=claimant, payer, verdict, transfer. `خ ب ر B001` corroborates informed authority; success/accusation/choice/gift forks use `و ر ي B003 + ق د ح B003 + خ ي ر B003/B005`. `(K: no injury, payment, legal actor, or transfer)`. **Grade: weak**.

#### B003 — state-change and substitution

- **Initial image:** each opening cue changes a prior state; later reversals may continue the same transformation grammar.
- **V23:** `عدو=E:B004/B010 | ضبح=E:B004 | وري=E:B002/B005 | قدح=E:B001/B002 | غير=S:B003 | صبح=E:B010 | ثور=E:B001/B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B001 | ءنس=C:B001 | ربب=Ø | كند=E:B001 | شهد=C:B008 | حبب=Ø | خير=Ø | شدد=C:B002 | علم=C:B002 | بعثر=C:B001/B002/B003 | قبر=C:B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`غ ي ر B003 + ع د و B004/B010 + ض ب ح B004 + و ر ي B002/B005 + ق د ح B001/B002 + ص ب ح B010 + ث و ر B001/B002 + ن ق ع B004 + و س ط B003 + ج م ع B001 + ك ن د B001`; freeze=hidden→visible, surface→airborne, outside→inside, gathered→cut are successive state changes; P=inside→outside inversion, extraction, and knowledge of resulting interior. `ء ن س B001 + ش ه د B008 + ش د د B002 + ع ل م B002 + ب ع ث ر B001/B002/B003 + ق ب ر B002 + ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` corroborate pivot, trace, force, inversion, result, and inner source. `(K: “change” is a remote root branch, not a lexical paraphrase of مُغِيرَاتِ)`. **Grade: strong** — order is almost entirely transformation-driven.

#### B004 — jealousy/guarded attachment

- **Initial image:** intense love becomes possessive guarding against a rival.
- **V23:** `عدو=F:B003 | ضبح=Ø | وري=Ø | قدح=Ø | غير=S:B004 | صبح=Ø | ثور=F:B003 | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=F:B011 | كند=E:B001/B002 | شهد=C:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B001/B002 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`غ ي ر B004 + ء ن س B001 + ك ن د B001/B002 + ح ب ب B002 + خ ي ر B001 + ش د د B001/B002`; freeze=the human's attachment to good is guarded/tight while another bond is cut; P=rival, protective act, inward motive, knowledge. `ش ه د B002 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate interior/account only. Enemy/uprising/covenant rivals use `ع د و B003 + ث و ر B003 + ر ب ب B011`. `(K: no family, rival, jealousy holder, or guarding event)`. **Grade: weak** — attachment topology fits, jealousy-specific roles fail.

#### B005 — otherness, contrast, and negation

- **Initial image:** one state is set against another; the 100:5→100:6 pivot and competing human orientations are candidate contrasts.
- **V23:** `عدو=E:B004 | ضبح=Ø | وري=E:B006 | قدح=Ø | غير=S:B005 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=E:B002 | جمع=Ø | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=C:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B002 | علم=C:B001 | بعثر=C:B003 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`غ ي ر B005 + ع د و B004 + و ر ي B006 + و س ط B002 + ء ن س B001 + ر ب ب B001 + ك ن د B002 + ح ب ب B002 + خ ي ر B001 + ش د د B002`; freeze=outer collective movement contrasts with singular human inward orientation, itself split between رب and good; P=explicit cognition, inversion of hidden/visible, inner disclosure, informed closure. `ش ه د B002 + ع ل م B001 + ب ع ث ر B003 + ق ب ر B002 + ح ص ل B002 + ص د ر B001 + خ ب ر B001` corroborate. `(K: no surface غير/exception construction; contrast is structural)`. **Grade: medium-strong**.

### 100:3:2 `صُبْحًا` — `ص ب ح`

#### B001 — dawn / first edge of day

- **Initial image:** action occurs at the day’s opening edge; the close may answer with another marked day/time.
- **V23:** `عدو=E:B002 | ضبح=E:B001/B002 | وري=E:B002 | قدح=E:B001 | غير=Ø | صبح=S:B001 | ثور=E:B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B010 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=F:B008 | حبب=Ø | خير=Ø | شدد=C:B005 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=C:B001`.
- **Lifecycle:** G=`ص ب ح B001 + ع د و B002 + ض ب ح B001/B002 + و ر ي B002 + ق د ح B001 + ث و ر B002 + ن ق ع B004 + و س ط B003 + ج م ع B010`; freeze=a dawn-bounded kinetic sequence reaches completion; P=another marked time and final resolution. `ش د د B005` reactivates day-height and `خ ب ر B001` fills knowledge at `يَوْمَئِذٍ`; `ش ه د B008` creates a time-sign fork. `(C: إِذَا + يَوْمَئِذٍ temporal structure)`, `(K: dawn is not identified with that day)`. **Grade: medium-strong**.

#### B002 — morning arrival

- **Initial image:** a moving body comes at morning and enters a destination; a water-arrival fork remains possible.
- **V23:** `عدو=E:B002 | ضبح=E:B002 | وري=E:B002 | قدح=E:B001 | غير=Ø | صبح=S:B002 | ثور=E:B002 | نقع=E:B004,F:B001/B002 | وسط=E:B003 | جمع=E:B002 | ءنس=F:B004 | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=C:B003 | علم=Ø | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002 | صدر=F:B003,C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ص ب ح B002 + ع د و B002 + ض ب ح B002 + و ر ي B002 + ق د ح B001 + ث و ر B002 + ن ق ع B004 + و س ط B003 + ج م ع B002`; freeze=morning arrival produces effects and enters a gathered destination; P=late charge and deeper inside/out reversal. `ش د د B003 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002 + ص د ر B001 + خ ب ر B001` corroborate. Water arrival/departure uses `ن ق ع B001/B002 + ص د ر B003`; rider interface uses `ء ن س B004`; both lack roles. **Grade: medium-strong**.

#### B003 — morning drink/meal

- **Initial image:** food or drink is taken at dawn.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=E:B006 | غير=E:B001 | صبح=S:B003 | ثور=Ø | نقع=E:B001/B002/B003 | وسط=Ø | جمع=E:B012 | ءنس=Ø | ربب=E:B006/B013 | كند=Ø | شهد=Ø | حبب=E:B006/B007 | خير=F:B005 | شدد=Ø | علم=E:B005 | بعثر=Ø | قبر=Ø | حصل=E:B004 | صدر=E:B003 | خبر=C:B004`.
- **Lifecycle:** G=`ص ب ح B003 + ق د ح B006 + غ ي ر B001 + ن ق ع B001/B002/B003 + ج م ع B012 + ر ب ب B006/B013 + ح ب ب B006/B007 + ع ل م B005 + ح ص ل B004 + ص د ر B003`; freeze=morning provision fills a vessel/body, quenches, and is followed by departure; P=drinker, liquid/food, source. `خ ب ر B004` corroborates abundance; gift `خ ي ر B005` forks. `(K: صُبْحًا is a time adverb for مُغِيرَاتِ; no consumption roles)`. **Grade: unlikely**.

#### B004 — dawn charge/alarm

- **Initial image:** a formed body advances at dawn toward another group.
- **V23:** `عدو=E:B001/B002/B003 | ضبح=E:B001/B002 | وري=E:B002 | قدح=E:B001 | غير=Ø | صبح=S:B004 | ثور=E:B002/B003 | نقع=E:B004 | وسط=E:B003 | جمع=E:B002/B010 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=C:B011 | خير=Ø | شدد=C:B002/B003 | علم=C:B002 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ص ب ح B004 + ع د و B001/B002/B003 + ض ب ح B001/B002 + و ر ي B002 + ق د ح B001 + ث و ر B002/B003 + ن ق ع B004 + و س ط B003 + ج م ع B002/B010`; freeze=dawn charge ignites, raises dust, and enters a group; P=opponent, trace, and late charge. `ش ه د B008 + ح ب ب B011 + ش د د B002/B003 + ع ل م B002` corroborate signs, sparks, and force. `(K: no explicit enemy, weapon, or target; no passage-scale closure)`. **Grade: medium** — strong opening-local scene.

#### B005 — lamp/light

- **Initial image:** ignition becomes illumination; what was only heard can now be seen and known.
- **V23:** `عدو=Ø | ضبح=E:B001/B003 | وري=E:B002/B005 | قدح=E:B001 | غير=E:B003 | صبح=S:B005 | ثور=E:B001 | نقع=F:B005 | وسط=Ø | جمع=Ø | ءنس=E:B002/B005 | ربب=Ø | كند=Ø | شهد=E:B001/B008 | حبب=F:B011 | خير=Ø | شدد=Ø | علم=C:B001/B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ص ب ح B005 + ض ب ح B001/B003 + و ر ي B002/B005 + ق د ح B001 + غ ي ر B003 + ث و ر B001 + ء ن س B002/B005 + ش ه د B001/B008`; freeze=fire/light changes concealed or merely audible activity into visible evidence; P=explicit knowing, direct disclosure, inner knowledge. `ع ل م B001/B002 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002 + ص د ر B001 + خ ب ر B001` corroborate. Raised sound `ن ق ع B005` and weak sparks `ح ب ب B011` fork. `(K: صُبْحًا contextually denotes time, not lamp)`. **Grade: medium-strong**.

#### B006 — brightness/beauty

- **Initial image:** a bright visible surface invites comparison with darkened exterior and pupil/heart center.
- **V23:** `عدو=Ø | ضبح=F:B004 | وري=F:B005 | قدح=Ø | غير=E:B003 | صبح=S:B006 | ثور=E:B001 | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B005 | ربب=Ø | كند=Ø | شهد=E:B001/B008 | حبب=E:B004 | خير=F:B002 | شدد=Ø | علم=E:B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ص ب ح B006 + غ ي ر B003 + ث و ر B001 + ء ن س B005 + ش ه د B001/B008 + ح ب ب B004 + ع ل م B002`; freeze=bright exterior, dark center, and visible sign create a surface/interior visual model; P=covering opened, hidden core extracted, inner state known. `ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002 + ص د ر B001 + خ ب ر B001` corroborate. Blackening/concealment/excellence forks use `ض ب ح B004 + و ر ي B005 + خ ي ر B002`. `(K: no face, beauty, eye, or color predicate)`. **Grade: medium**.

#### B007 — morning sleep

- **Initial image:** stillness/sleep at dawn competes with the surrounding acceleration.
- **V23:** `عدو=K:B002 | ضبح=K:B001/B002 | وري=Ø | قدح=Ø | غير=Ø | صبح=S:B007 | ثور=K:B002 | نقع=Ø | وسط=K:B003 | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=F:B005 | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ص ب ح B007` only; freeze=morning sleep; P=sleeper, pause, awakening. Full dossier sweep yields no completing branch; disabled immobility `ح ب ب B005` is a fork. `(K: ع د و B002 + ض ب ح B001/B002 + ث و ر B002 + و س ط B003 and repeated فـ encode uninterrupted action)`. **Grade: unlikely**.

#### B008 — camel remaining until morning

- **Initial image:** an animal stays kneeling and delays movement.
- **V23:** `عدو=K:B002 | ضبح=K:B002 | وري=Ø | قدح=F:B008 | غير=Ø | صبح=S:B008 | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=F:B004 | ربب=F:B014 | كند=Ø | شهد=Ø | حبب=E:B005 | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=F:B006 | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ص ب ح B008 + ح ب ب B005`; freeze=exhausted camel remains down; P=animal identity, prior exertion, injury. Lean horse `ق د ح B008`, mount-facing side `ء ن س B004`, herd `ر ب ب B014`, and horse pain `ح ص ل B006` fork but do not cohere to one animal. `(K: ع د و B002 + ض ب ح B002 show continued running through 100:5; no stopping)`. **Grade: unlikely**.

#### B009 — appointed morning occasion

- **Initial image:** a specific morning appointment bounds an encounter and anticipates another marked time.
- **V23:** `عدو=E:B002 | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=S:B009 | ثور=Ø | نقع=Ø | وسط=E:B003 | جمع=E:B002/B004 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=F:B008 | حبب=Ø | خير=Ø | شدد=C:B005 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=C:B001`.
- **Lifecycle:** G=`ص ب ح B009 + ع د و B002 + و س ط B003 + ج م ع B002/B004`; freeze=a timed encounter brings a moving body into a gathering; P=later marked day and resolution. `ش د د B005 + خ ب ر B001` and `(C: إِذَا / يَوْمَئِذٍ)` corroborate temporal return; `ش ه د B008` makes time a sign fork. `(K: no calendrical interval or appointment formula)`. **Grade: medium**.

#### B010 — becoming / entry into state

- **Initial image:** each event becomes a new state, inviting a passage-wide transition chain.
- **V23:** `عدو=E:B004 | ضبح=E:B004 | وري=E:B002/B005 | قدح=E:B001 | غير=E:B003 | صبح=S:B010 | ثور=E:B001/B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B001 | ءنس=C:B001 | ربب=Ø | كند=E:B001 | شهد=C:B008 | حبب=Ø | خير=Ø | شدد=C:B002 | علم=C:B001 | بعثر=C:B001/B002/B003 | قبر=C:B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ص ب ح B010 + ع د و B004 + ض ب ح B004 + و ر ي B002/B005 + ق د ح B001 + غ ي ر B003 + ث و ر B001/B002 + ن ق ع B004 + و س ط B003 + ج م ع B001 + ك ن د B001`; freeze=successive becoming moves latency→appearance, outside→inside, gathering→severance; P=exposure, inversion, extraction, and knowing. `ء ن س B001 + ش ه د B008 + ش د د B002 + ع ل م B001 + ب ع ث ر B001/B002/B003 + ق ب ر B002 + ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` corroborate. `(K: صُبْحًا is a time noun, not أصبح)`. **Grade: medium-strong**.

### 100:4:1 `فَأَثَرْنَ` — `ث و ر`

#### B001 — latent matter emerges and spreads

- **Initial image:** something dormant becomes outwardly visible and diffuse.
- **V23:** `عدو=E:B002/B010 | ضبح=Ø | وري=E:B002/B005 | قدح=E:B001 | غير=E:B003 | صبح=E:B005 | ثور=S:B001 | نقع=E:B004 | وسط=E:B003 | جمع=Ø | ءنس=C:B002 | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=C:B011 | خير=Ø | شدد=C:B002 | علم=C:B001/B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001/B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ث و ر B001 + ع د و B002/B010 + و ر ي B002/B005 + ق د ح B001 + غ ي ر B003 + ص ب ح B005 + ن ق ع B004 + و س ط B003`; freeze=latent fire/matter emerges, becomes visible, and moves toward an interior; P=perception/signs, later concealed contents, extraction, inner knowledge. `ء ن س B002 + ش ه د B008 + ح ب ب B011 + ش د د B002 + ع ل م B001/B002 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B001/B002 + ص د ر B001 + خ ب ر B001` corroborate. `(K: local direct object narrows emergence to نَقْعًا; no one substance spans the passage)`. **Grade: strong**.

#### B002 — dislodging from place

- **Initial image:** force moves material out of its resting place; later earth and interiors may undergo deeper dislodging.
- **V23:** `عدو=E:B002/B010 | ضبح=E:B002 | وري=E:B002 | قدح=E:B001/B002 | غير=E:B003 | صبح=Ø | ثور=S:B002 | نقع=E:B004/B007 | وسط=E:B003 | جمع=E:B010 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=Ø | خير=Ø | شدد=C:B002/B003 | علم=C:B002 | بعثر=C:B001/B003 | قبر=C:B001/B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ث و ر B002 + ع د و B002/B010 + ض ب ح B002 + و ر ي B002 + ق د ح B001/B002 + غ ي ر B003 + ن ق ع B004/B007 + و س ط B003 + ج م ع B010`; freeze=kinetic force dislodges surface matter and penetrates a center; P=earth overturned, recess opened, core extracted, force/trace reactivated. `ش ه د B008 + ش د د B002/B003 + ع ل م B002 + ب ع ث ر B001/B003 + ق ب ر B001/B002 + ح ص ل B002 + ص د ر B001 + خ ب ر B001` corroborate. `(K: بِهِ antecedent remains unresolved; passive agent later unexpressed)`. **Grade: strong**.

#### B003 — uprising toward confrontation/anger

- **Initial image:** stirred force rises against another party.
- **V23:** `عدو=E:B001/B003 | ضبح=E:B002 | وري=Ø | قدح=Ø | غير=F:B004 | صبح=E:B004 | ثور=S:B003 | نقع=C:B004 | وسط=E:B003 | جمع=E:B002 | ءنس=E:B001 | ربب=F:B011 | كند=F:B001 | شهد=Ø | حبب=F:B002 | خير=Ø | شدد=C:B003 | علم=Ø | بعثر=Ø | قبر=F:B004 | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ث و ر B003 + ع د و B001/B003 + ض ب ح B002 + ص ب ح B004 + و س ط B003 + ج م ع B002`; freeze=uprising/hostile charge enters a group; P=opponent and impact. `ن ق ع B004 + ش د د B003` corroborate effect and force. Jealousy/anger-nose/relational rupture forks use `غ ي ر B004 + ق ب ر B004 + ر ب ب B011 + ك ن د B001 + ح ب ب B002`. `(K: no opponent, anger holder, or conflict relation)`. **Grade: weak**.

#### B004 — bull

- **Initial image:** a bull supplies a concrete animal candidate for the opening plurality.
- **V23:** `عدو=E:B002 | ضبح=E:B001/B002 | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=S:B004 | نقع=E:B007 | وسط=Ø | جمع=E:B002 | ءنس=F:B004 | ربب=E:B014 | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ث و ر B004 + ع د و B002 + ض ب ح B001/B002 + ن ق ع B007 + ج م ع B002 + ر ب ب B014`; freeze=a bovine herd runs over ground; P=species agreement, herd action, or human-facing control. `ء ن س B004` forks toward rider-facing side. `(K: أَثَرْنَ is a 3FP Form IV verb; no bull/bovine noun and no herd role)`. **Grade: unlikely**.

#### B005 — solid curd piece

- **Initial image:** a solid food piece belongs to a storage/meal scene.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=F:B005/B006 | غير=F:B001 | صبح=F:B003 | ثور=S:B005 | نقع=F:B003 | وسط=Ø | جمع=F:B012 | ءنس=Ø | ربب=E:B006 | كند=Ø | شهد=Ø | حبب=F:B007 | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=F:B004 | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ث و ر B005 + ر ب ب B006`; freeze=a food/thick-substance piece; P=container, meal, eater. Pot/cup/provision/morning meal/hospitality/vessel/crop forks use `ق د ح B005/B006 + غ ي ر B001 + ص ب ح B003 + ن ق ع B003 + ج م ع B012 + ح ب ب B007 + ح ص ل B004`, but no controlled composite forms. `(K: no food or substance role)`. **Grade: unlikely**.

#### B006 — proper place/tribe/constellation

- **Initial image:** a proper name could locate or identify the scene.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=S:B006 | نقع=Ø | وسط=F:B002 | جمع=F:B004 | ءنس=Ø | ربب=Ø | كند=F:B004 | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ث و ر B006` only; freeze=unnamed proper location/group; P=naming syntax or geographic attachment. Place/day and tribal forks appear in `و س ط B002 + ج م ع B004 + ك ن د B004`, but `(K: no proper noun or location identifier)`. **Grade: unlikely**.

#### B007 — algae layer on water

- **Initial image:** a layer rises to the surface of standing water.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B001 | صبح=Ø | ثور=S:B007 | نقع=E:B001/B002 | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=E:B008/B013 | كند=Ø | شهد=Ø | حبب=E:B008 | خير=Ø | شدد=Ø | علم=E:B005 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=C:B002/B005`.
- **Lifecycle:** G=`ث و ر B007 + غ ي ر B001 + ن ق ع B001/B002 + ر ب ب B008/B013 + ح ب ب B008 + ع ل م B005`; freeze=water/rain supports a visible surface layer; P=soft wet ground/plant. `خ ب ر B002/B005` corroborates watery land/soft vegetation. `(K: no water, algae, rain, or plant; نَقْعًا is raised direct object in a dust-producing chain)`. **Grade: unlikely**.

### 100:4:3 `نَقْعًا` — `ن ق ع`

#### B001 — standing water / soaking container

- **Initial image:** water settles in a containing place and holds immersed matter.
- **V23:** `عدو=Ø | ضبح=Ø | وري=F:B004 | قدح=E:B005/B006 | غير=E:B001 | صبح=F:B003 | ثور=F:B007 | نقع=S:B001 | وسط=E:B002 | جمع=E:B012 | ءنس=Ø | ربب=E:B006/B013 | كند=Ø | شهد=Ø | حبب=E:B006/B007/B008 | خير=Ø | شدد=Ø | علم=E:B005 | بعثر=C:B003 | قبر=C:B002 | حصل=C:B002/B004 | صدر=C:B001/B003 | خبر=C:B002/B004`.
- **Lifecycle:** G=`ن ق ع B001 + ق د ح B005/B006 + غ ي ر B001 + و س ط B002 + ج م ع B012 + ر ب ب B006/B013 + ح ب ب B006/B007/B008 + ع ل م B005`; freeze=a full soaking vessel has a deep center; P=inversion/emptying, recessed container, extracted contents. `ب ع ث ر B003 + ق ب ر B002 + ح ص ل B002/B004 + ص د ر B001/B003 + خ ب ر B002/B004` corroborate geometry/abundance, not water context. Full body, morning drink, algae forks use `و ر ي B004 + ص ب ح B003 + ث و ر B007`. `(K: attachment makes نَقْعًا raised object; kinetic dust branch B004 controls)`. **Grade: weak**.

#### B002 — quenching thirst / settling the self

- **Initial image:** provision fills a lack until bodily or inward unrest settles.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=E:B006 | غير=E:B001 | صبح=E:B003 | ثور=Ø | نقع=S:B002 | وسط=Ø | جمع=Ø | ءنس=E:B006 | ربب=E:B002/B013 | كند=E:B002 | شهد=Ø | حبب=E:B002/B006 | خير=E:B001/B005 | شدد=E:B002 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`ن ق ع B002 + ق د ح B006 + غ ي ر B001 + ص ب ح B003 + ء ن س B006 + ر ب ب B002/B013 + ك ن د B002 + ح ب ب B002/B006 + خ ي ر B001/B005 + ش د د B002`; freeze=benefit fills need, but the human's intense attachment settles on the benefit while gratitude fails; P=result, inward source, knowledgeable closure. `ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. `(K: no water/drinker; نَقْعًا contextual dust, and “settled self” is remote)`. **Grade: medium** — relational lack/filling model is coherent but seed use remote.

#### B003 — arrival meal/slaughter/milk

- **Initial image:** an arrival triggers hospitality or slaughtered provision.
- **V23:** `عدو=F:B002 | ضبح=Ø | وري=Ø | قدح=F:B006 | غير=E:B001 | صبح=E:B002/B003 | ثور=Ø | نقع=S:B003 | وسط=Ø | جمع=E:B002 | ءنس=E:B003 | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=E:B005 | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=F:B004 | صدر=F:B003 | خبر=F:B006`.
- **Lifecycle:** G=`ن ق ع B003 + غ ي ر B001 + ص ب ح B002/B003 + ج م ع B002 + ء ن س B003 + خ ي ر B005`; freeze=morning arrival into a group receives companionship and food/gift; P=host, guest, consumption. Running/cup/crop/departure/shared meat forks use `ع د و B002 + ق د ح B006 + ح ص ل B004 + ص د ر B003 + خ ب ر B006`. `(K: no host, guest, meal, slaughter, milk, or consumption)`. **Grade: unlikely**.

#### B004 — raised dust

- **Initial image:** motion dislodges dust, making a visible trace and beginning a ground-depth trajectory.
- **V23:** `عدو=E:B002/B010 | ضبح=E:B001/B002 | وري=E:B002 | قدح=E:B001/B002 | غير=E:B003 | صبح=E:B001 | ثور=E:B001/B002 | نقع=S:B004 | وسط=E:B003 | جمع=E:B010 | ءنس=C:B002 | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=C:B011 | خير=Ø | شدد=C:B002/B003 | علم=C:B002 | بعثر=C:B001 | قبر=C:B001/B002 | حصل=C:B002/B003 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ن ق ع B004 + ع د و B002/B010 + ض ب ح B001/B002 + و ر ي B002 + ق د ح B001/B002 + غ ي ر B003 + ص ب ح B001 + ث و ر B001/B002 + و س ط B003 + ج م ع B010`; freeze=surface force produces a visible particulate trace and enters a center; P=trace interpretation, deeper earth opening, core/residue, human interior. `ء ن س B002 + ش ه د B008 + ح ب ب B011 + ش د د B002/B003 + ع ل م B002 + ب ع ث ر B001 + ق ب ر B001/B002 + ح ص ل B002/B003 + ص د ر B001 + خ ب ر B001` corroborate. `(K: dust is an effect, not itself testimony or chest content)`. **Grade: strong**.

#### B005 — raised/repeated sound

- **Initial image:** loud continuing sound makes unseen action perceptible and may progress to testimony/report.
- **V23:** `عدو=E:B002 | ضبح=E:B001 | وري=Ø | قدح=F:B003 | غير=Ø | صبح=E:B005 | ثور=Ø | نقع=S:B005 | وسط=Ø | جمع=Ø | ءنس=E:B002/B003 | ربب=Ø | كند=Ø | شهد=E:B001/B002/B005 | حبب=F:B009 | خير=Ø | شدد=Ø | علم=C:B001 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`ن ق ع B005 + ع د و B002 + ض ب ح B001 + ص ب ح B005 + ء ن س B002/B003 + ش ه د B001/B002/B005`; freeze=sound is heard, made expressible, and reaches witness/testimony; P=knowing, direct disclosure, inner source, report of inward matter. `ع ل م B001 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Slander `ق د ح B003` and teeth/mouth `ح ب ب B009` fork. `(K: direct-object syntax and ث و ر B002 make dust B004 primary)`. **Grade: medium-strong** — complete sound→report trajectory, subordinate local branch.

#### B006 — fixed poison/death

- **Initial image:** poison accumulates, persists, and causes death/burial.
- **V23:** `عدو=F:B006 | ضبح=Ø | وري=E:B001 | قدح=E:B004 | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=S:B006 | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=Ø | كند=Ø | شهد=Ø | حبب=F:B012 | خير=Ø | شدد=Ø | علم=Ø | بعثر=F:B001 | قبر=C:B001 | حصل=Ø | صدر=E:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ن ق ع B006 + و ر ي B001 + ق د ح B004 + غ ي ر B003 + ء ن س B001 + ص د ر B001`; freeze=poison/decay attacks a human interior and yields death; P=causal death event and burial. `ق ب ر B001 + خ ب ر B001` corroborate burial/knowledge only; contagion, snake, and earth uncovering forks use `ع د و B006 + ح ب ب B012 + ب ع ث ر B001`. `(K: no poison, bite, killing, or causal route to graves)`. **Grade: unlikely**.

#### B007 — level clay ground

- **Initial image:** traversable ground receives impact, dust, and later deeper overturning.
- **V23:** `عدو=E:B002/B010 | ضبح=E:B002 | وري=E:B002 | قدح=E:B001 | غير=F:B001 | صبح=E:B002 | ثور=E:B002 | نقع=S:B007 | وسط=E:B002/B003 | جمع=E:B002 | ءنس=Ø | ربب=F:B012 | كند=F:B003 | شهد=C:B008 | حبب=F:B001 | خير=Ø | شدد=C:B003 | علم=C:B002 | بعثر=C:B001 | قبر=C:B001/B002 | حصل=C:B002/B003 | صدر=C:B001 | خبر=C:B001/B002/B003`.
- **Lifecycle:** G=`ن ق ع B007 + ع د و B002/B010 + ض ب ح B002 + و ر ي B002 + ق د ح B001 + ص ب ح B002 + ث و ر B002 + و س ط B002/B003 + ج م ع B002`; freeze=movement crosses ground, disturbs its surface, and enters a center; P=ground-depth opening and inner analogue. `ش ه د B008 + ش د د B003 + ع ل م B002 + ب ع ث ر B001 + ق ب ر B001/B002 + ح ص ل B002/B003 + ص د ر B001 + خ ب ر B001` corroborate. Agricultural fork uses `غ ي ر B001 + ر ب ب B012 + ك ن د B003 + ح ب ب B001 + خ ب ر B002/B003`. `(K: ground is implicit, not named)`. **Grade: strong** — independently regenerates the depth progression.

#### B008 — experienced knowledge of routes/resources

- **Initial image:** an experienced traveler knows resources, routes, and safe entries.
- **V23:** `عدو=E:B002/B009 | ضبح=Ø | وري=E:B006 | قدح=Ø | غير=Ø | صبح=E:B002 | ثور=Ø | نقع=S:B008 | وسط=E:B002/B003 | جمع=Ø | ءنس=E:B002 | ربب=Ø | كند=Ø | شهد=E:B008 | حبب=Ø | خير=E:B003 | شدد=Ø | علم=E:B001/B002 | بعثر=Ø | قبر=E:B002 | حصل=Ø | صدر=F:B003 | خبر=C:B001`.
- **Lifecycle:** G=`ن ق ع B008 + ع د و B002/B009 + و ر ي B006 + ص ب ح B002 + و س ط B002/B003 + ء ن س B002 + ش ه د B008 + خ ي ر B003 + ع ل م B001/B002 + ق ب ر B002`; freeze=experienced perception reads marks, chooses a route, and enters/avoids recessed spaces; P=departure/result and final expertise. `خ ب ر B001` corroborates experience; `ص د ر B003` forks into departure from a resource. `(K: no traveler, route choice, danger, or safe-path event)`. **Grade: weak**.

#### B009 — abusive speech

- **Initial image:** ugly insult strikes another person and invites testimony.
- **V23:** `عدو=F:B001/B005 | ضبح=Ø | وري=Ø | قدح=E:B003 | غير=Ø | صبح=Ø | ثور=F:B003 | نقع=S:B009 | وسط=F:B005 | جمع=Ø | ءنس=E:B001 | ربب=Ø | كند=Ø | شهد=E:B002/B005 | حبب=Ø | خير=Ø | شدد=Ø | علم=E:B001 | بعثر=Ø | قبر=F:B004 | حصل=Ø | صدر=Ø | خبر=C:B001`.
- **Lifecycle:** G=`ن ق ع B009 + ق د ح B003 + ء ن س B001 + ش ه د B002/B005 + ع ل م B001`; freeze=verbal attack is testified and known; P=speaker, target, utterance. `خ ب ر B001` corroborates report/knowledge. Wrong/redress, anger/uprising, mediation, and angry nose forks use `ع د و B001/B005 + ث و ر B003 + و س ط B005 + ق ب ر B004`. `(K: no speech event or addressee)`. **Grade: unlikely**.

### 100:5:1 `فَوَسَطْنَ` — `و س ط`

#### B001 — just/choice middle

- **Initial image:** the center is a balanced or preferred position, creating spatial, evaluative, and judicial forks.
- **V23:** `عدو=F:B005 | ضبح=Ø | وري=Ø | قدح=Ø | غير=F:B002 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=S:B001 | جمع=E:B002 | ءنس=E:B001 | ربب=F:B001 | كند=F:B002 | شهد=F:B002 | حبب=E:B003 | خير=E:B002/B003 | شدد=Ø | علم=F:B001 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=F:B001`.
- **Lifecycle:** evaluative G=`و س ط B001 + ج م ع B002 + ء ن س B001 + ح ب ب B003 + خ ي ر B002/B003`; freeze=a human/group occupies a preferred center and chooses excellence; P=comparison or selection act. Judicial fork recruits `ع د و B005 + غ ي ر B002 + ر ب ب B001 + ك ن د B002 + ش ه د B002 + ع ل م B001 + خ ب ر B001`. `(K: وَسَطْنَ is a perfect verb of entering; no criterion, chooser, mediator, or verdict)`. **Grade: weak**.

#### B002 — center between edges

- **Initial image:** an ordered space has edges and a center; earlier motion reaches it and later enclosures can invert it.
- **V23:** `عدو=E:B004/B009 | ضبح=Ø | وري=E:B006 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=E:B007 | وسط=S:B002 | جمع=E:B002 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=C:B004 | خير=F:B006 | شدد=Ø | علم=Ø | بعثر=C:B001/B003 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001/B002 | خبر=C:B001`.
- **Lifecycle:** G=`و س ط B002 + ع د و B004/B009 + و ر ي B006 + غ ي ر B003 + ن ق ع B007 + ج م ع B002`; freeze at 100:5=edge/other-side movement reaches a middle; P=explicit containment, recessed interior, inversion, core extraction. `ح ب ب B004 + ب ع ث ر B001/B003 + ق ب ر B002 + ح ص ل B002 + ص د ر B001/B002 + خ ب ر B001` corroborate center-core, inversion, chest/front, and knowledge. Burrow `خ ي ر B006` forks. `(K: later containers are not the same physical center)`. **Grade: strong**.

#### B003 — entering the middle

- **Initial image:** active entry into a gathered center establishes an outside→inside vector.
- **V23:** `عدو=E:B002/B004 | ضبح=E:B002 | وري=E:B006 | قدح=Ø | غير=E:B003 | صبح=E:B002 | ثور=E:B002 | نقع=E:B004 | وسط=S:B003 | جمع=E:B001/B002 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=C:B004 | خير=F:B006 | شدد=C:B003 | علم=Ø | بعثر=C:B001/B003 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001/B002 | خبر=C:B001`.
- **Lifecycle:** G=`و س ط B003 + ع د و B002/B004 + ض ب ح B002 + و ر ي B006 + غ ي ر B003 + ص ب ح B002 + ث و ر B002 + ن ق ع B004 + ج م ع B001/B002`; freeze=force crosses into a gathered center; P=later inside markers and inside→outside reversal. `ح ب ب B004 + ش د د B003 + ب ع ث ر B001/B003 + ق ب ر B002 + ح ص ل B002 + ص د ر B001/B002 + خ ب ر B001` corroborate. Burrow exit `خ ي ر B006` is a defeated rival. `(K: no identity among opening group, graves, chests, or final people)`. **Grade: strong**.

#### B004 — middling quality

- **Initial image:** something lies between good and bad on a quality scale.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B005 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=S:B004 | جمع=Ø | ءنس=E:B001 | ربب=Ø | كند=E:B002 | شهد=F:B002 | حبب=E:B003 | خير=E:B001/B002 | شدد=E:B002 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`و س ط B004 + غ ي ر B005 + ء ن س B001 + ك ن د B002 + ح ب ب B003 + خ ي ر B001/B002 + ش د د B002`; freeze=human valuation lies on a good/bad continuum and becomes intensely preferential; P=result, inward source, informed evaluation. `ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate; `ش ه د B002` offers testimony. `(K: no comparative scale or “bad” pole; وَسَطْنَ is verbal entry)`. **Grade: weak**.

#### B005 — mediation between people

- **Initial image:** a mediator moves between parties to settle a dispute.
- **V23:** `عدو=E:B005 | ضبح=Ø | وري=F:B003 | قدح=F:B003 | غير=E:B002 | صبح=Ø | ثور=Ø | نقع=F:B009 | وسط=S:B005 | جمع=E:B013 | ءنس=E:B001 | ربب=E:B001/B011 | كند=E:B001/B002 | شهد=E:B002 | حبب=Ø | خير=F:B003 | شدد=Ø | علم=E:B001 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=F:B005 | خبر=C:B001`.
- **Lifecycle:** G=`و س ط B005 + ع د و B005 + غ ي ر B002 + ج م ع B013 + ء ن س B001 + ر ب ب B001/B011 + ك ن د B001/B002 + ش ه د B002 + ع ل م B001`; freeze=mediator handles broken relation through testimony/compensation; P=two parties, settlement, verdict. `خ ب ر B001` corroborates informed decision; aid/accusation/insult/choice/seizure forks use `و ر ي B003 + ق د ح B003 + ن ق ع B009 + خ ي ر B003 + ص د ر B005`. `(K: no dispute, mediator, agreement, or transfer)`. **Grade: weak**.

#### B006 — cutting in half

- **Initial image:** entry through a center divides a gathered whole; later scattering and collection may replay division/recovery.
- **V23:** `عدو=E:B004 | ضبح=Ø | وري=E:B006 | قدح=E:B002 | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=S:B006 | جمع=E:B001/B009 | ءنس=Ø | ربب=F:B016 | كند=E:B001 | شهد=Ø | حبب=Ø | خير=Ø | شدد=F:B001 | علم=Ø | بعثر=C:B002/B003 | قبر=Ø | حصل=C:B001/B002 | صدر=C:B006 | خبر=Ø`.
- **Lifecycle:** G=`و س ط B006 + ع د و B004 + و ر ي B006 + ق د ح B002 + غ ي ر B003 + ج م ع B001/B009 + ك ن د B001`; freeze=a whole is crossed, cracked, and divided; P=scattering, inversion, regathering, recovered part/core. `ب ع ث ر B002/B003 + ح ص ل B001/B002 + ص د ر B006` corroborate. Knot/bond fork uses `ر ب ب B016 + ش د د B001`. `(K: attachment says جَمْعًا is entered, not cut; no divided patient)`. **Grade: medium** — ordered gather/divide/scatter/collect pattern, weak local action.

#### B007 — tent or particular camel

- **Initial image:** a shelter or animal might provide a centered enclosure.
- **V23:** `عدو=F:B002 | ضبح=F:B001/B002 | وري=Ø | قدح=Ø | غير=Ø | صبح=F:B008 | ثور=Ø | نقع=Ø | وسط=S:B007 | جمع=F:B012 | ءنس=F:B004 | ربب=F:B014 | كند=Ø | شهد=Ø | حبب=F:B005 | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`و س ط B007` only; freeze=tent/camel; P=shelter occupant or animal behavior. Running/panting/immobile camel/large enclosure/mount-facing/herd branches (`ع د و B002 + ض ب ح B001/B002 + ص ب ح B008 + ج م ع B012 + ء ن س B004 + ر ب ب B014 + ح ب ب B005`) form incompatible forks. `(K: verbal 3FP وَسَطْنَ and direct object جَمْعًا exclude a nominal tent/camel role)`. **Grade: unlikely**.

### 100:5:3 `جَمْعًا` — `ج م ع`

#### B001 — gathering dispersed parts

- **Initial image:** separated elements are collected; later severance, scattering, and recollection are predicted.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=E:B003/B006 | جمع=S:B001 | ءنس=Ø | ربب=F:B004 | كند=E:B001 | شهد=Ø | حبب=Ø | خير=Ø | شدد=F:B001 | علم=Ø | بعثر=C:B002/B003 | قبر=Ø | حصل=C:B001/B002 | صدر=C:B006 | خبر=C:B001`.
- **Lifecycle:** G=`ج م ع B001 + غ ي ر B003 + و س ط B003/B006 + ك ن د B001`; freeze=gathered whole is entered and cut/changed; P=scattering/inversion followed by collection or extracted part. `ب ع ث ر B002/B003 + ح ص ل B001/B002 + ص د ر B006 + خ ب ر B001` corroborate. Multitude/binding forks use `ر ب ب B004 + ش د د B001`. `(K: grammatical objects differ across stages)`. **Grade: medium-strong**.

#### B002 — group/army/mixture

- **Initial image:** a collected body receives the opening entry; group identity and later number shifts become testable.
- **V23:** `عدو=E:B001/B002/B003 | ضبح=E:B002 | وري=Ø | قدح=Ø | غير=Ø | صبح=E:B004 | ثور=E:B003 | نقع=C:B004 | وسط=E:B003 | جمع=S:B002 | ءنس=C:B001 | ربب=F:B004/B014 | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=C:B003 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ج م ع B002 + ع د و B001/B002/B003 + ض ب ح B002 + ص ب ح B004 + ث و ر B003 + و س ط B003`; freeze=a moving/hostile body enters a group; P=impact, human pivot, later plurality. `ن ق ع B004 + ء ن س B001 + ش د د B003 + ص د ر B001 + خ ب ر B001` corroborate effects, human scale, force, and inward plural closure; multitude/herd forks use `ر ب ب B004/B014`. `(K: no army/enemy label and final humans are not the opening group)`. **Grade: medium**.

#### B003 — gathered resolve

- **Initial image:** dispersed thought becomes firm intention and selects an object of value.
- **V23:** `عدو=F:B007 | ضبح=Ø | وري=F:B003 | قدح=E:B010 | غير=E:B003 | صبح=Ø | ثور=E:B001 | نقع=Ø | وسط=Ø | جمع=S:B003 | ءنس=E:B006 | ربب=E:B001 | كند=E:B002 | شهد=C:B002 | حبب=E:B002 | خير=E:B003 | شدد=E:B002 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`ج م ع B003 + ق د ح B010 + غ ي ر B003 + ث و ر B001 + ء ن س B006 + ر ب ب B001 + ك ن د B002 + ح ب ب B002 + خ ي ر B003 + ش د د B002`; freeze=the self gathers a deliberate, intense preference that competes with the رب relation; P=testimony, cognition, inner result/source, informed closure. `ش ه د B002 + ع ل م B001 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Distraction/success forks use `ع د و B007 + و ر ي B003`. `(K: جَمْعًا is direct object of entry, not an explicit mental noun)`. **Grade: medium-strong**.

#### B004 — gathering place/day/call

- **Initial image:** a place or day gathers people; opening group and final marked day may converge.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=E:B009 | ثور=Ø | نقع=Ø | وسط=E:B002/B003 | جمع=S:B004 | ءنس=E:B001 | ربب=C:B001/B004 | كند=Ø | شهد=F:B001 | حبب=Ø | خير=Ø | شدد=C:B005 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=C:B001`.
- **Lifecycle:** G=`ج م ع B004 + ص ب ح B009 + و س ط B002/B003 + ء ن س B001`; freeze=people meet at an appointed place/time; P=marked final day and collective human reference. `ر ب ب B001/B004 + ش د د B005 + خ ب ر B001` and `(C: يَوْمَئِذٍ + هُم)` corroborate time/plural closure; witness gathering `ش ه د B001` forks. `(K: no summons or named gathering day)`. **Grade: medium**.

#### B005 — clenched fist

- **Initial image:** a hand gathers force into a blow.
- **V23:** `عدو=E:B001 | ضبح=Ø | وري=Ø | قدح=E:B002 | غير=Ø | صبح=Ø | ثور=E:B003 | نقع=Ø | وسط=Ø | جمع=S:B005 | ءنس=E:B001 | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=E:B002/B003 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ج م ع B005 + ع د و B001 + ق د ح B002 + ث و ر B003 + ء ن س B001 + ش د د B002/B003`; freeze=a human clenches force for impact; P=hand, struck patient, wound. No unused branch supplies the body part or patient. `(K: no hand, fist, blow, or bodily impact construction)`. **Grade: weak**.

#### B006 — sexual joining

- **Initial image:** two partners join physically.
- **V23:** `عدو=Ø | ضبح=Ø | وري=F:B007 | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=S:B006 | ءنس=E:B001 | ربب=F:B005 | كند=Ø | شهد=F:B006 | حبب=E:B002 | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ج م ع B006 + ء ن س B001 + ح ب ب B002`; freeze=human partners join through love; P=two partners or reproductive result. Descendant/caretaker/birth forks use `و ر ي B007 + ر ب ب B005 + ش ه د B006`, but `(K: no sexual, partner, marriage, or reproductive construction)`. **Grade: unlikely**.

#### B007 — pregnancy/retained condition

- **Initial image:** a woman retains a child or untouched state within her.
- **V23:** `عدو=Ø | ضبح=Ø | وري=E:B007 | قدح=Ø | غير=Ø | صبح=Ø | ثور=F:B001 | نقع=Ø | وسط=Ø | جمع=S:B007 | ءنس=E:B001 | ربب=E:B005/B009 | كند=Ø | شهد=E:B006 | حبب=E:B001 | خير=Ø | شدد=E:B004 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=E:B005 | صدر=E:B001 | خبر=Ø`.
- **Lifecycle:** G=`ج م ع B007 + و ر ي B007 + ء ن س B001 + ر ب ب B005/B009 + ش ه د B006 + ح ب ب B001 + ش د د B004 + ح ص ل B005 + ص د ر B001`; freeze=contained offspring emerges and matures; P=woman, child, birth. `ث و ر B001` forks into emergence. `(K: feminine-plural opening morphology does not create pregnancy; no woman/child/birth role)`. **Grade: unlikely**.

#### B008 — shackle joining hands to neck

- **Initial image:** a binding apparatus gathers limbs and requires cutting/release.
- **V23:** `عدو=F:B012 | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=E:B006 | جمع=S:B008 | ءنس=E:B001 | ربب=E:B016 | كند=E:B001 | شهد=Ø | حبب=Ø | خير=Ø | شدد=E:B001 | علم=Ø | بعثر=C:B002/B003 | قبر=Ø | حصل=C:B002 | صدر=E:B001 | خبر=Ø`.
- **Lifecycle:** G=`ج م ع B008 + غ ي ر B003 + و س ط B006 + ء ن س B001 + ر ب ب B016 + ك ن د B001 + ش د د B001 + ص د ر B001`; freeze=a human body is tightly bound then cut/opened; P=prisoner, limbs, release, recovered interior. `ب ع ث ر B002/B003 + ح ص ل B002` corroborate disruption/extraction abstractly; twisted obstacle `ع د و B012` forks. `(K: no shackle, hands, neck, captive, or release)`. **Grade: weak**.

#### B009 — complete whole

- **Initial image:** a whole is complete and undispersed; later overturning tests whether it can be fully recovered.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=F:B006 | جمع=S:B009 | ءنس=Ø | ربب=F:B004 | كند=E:B001 | شهد=Ø | حبب=Ø | خير=Ø | شدد=F:B001 | علم=Ø | بعثر=C:B002 | قبر=Ø | حصل=C:B001 | صدر=C:B006 | خبر=C:B001`.
- **Lifecycle:** G=`ج م ع B009 + غ ي ر B003 + ك ن د B001`; freeze=complete whole is threatened by separation/change; P=scattering and comprehensive recollection/part accounting. `ب ع ث ر B002 + ح ص ل B001 + ص د ر B006 + خ ب ر B001` corroborate. Bisection/multitude/knot forks use `و س ط B006 + ر ب ب B004 + ش د د B001`. `(K: no explicit totalizer; objects differ)`. **Grade: medium**.

#### B010 — gathering force/running parts

- **Initial image:** running components synchronize and concentrate force.
- **V23:** `عدو=E:B002 | ضبح=E:B001/B002 | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=E:B002/B004 | ثور=E:B002 | نقع=E:B004 | وسط=E:B003 | جمع=S:B010 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=C:B011 | خير=Ø | شدد=C:B002/B003 | علم=C:B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001/B002 | خبر=C:B001`.
- **Lifecycle:** G=`ج م ع B010 + ع د و B002 + ض ب ح B001/B002 + و ر ي B002 + ق د ح B001 + غ ي ر B003 + ص ب ح B002/B004 + ث و ر B002 + ن ق ع B004 + و س ط B003`; freeze=synchronized motion concentrates force into spark, dust, and entry; P=late force/spark replay and force on hidden interiors. `ش ه د B008 + ح ب ب B011 + ش د د B002/B003 + ع ل م B002 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002 + ص د ر B001/B002 + خ ب ر B001` corroborate. `(K: later intensity is attached to love, not running)`. **Grade: strong**.

#### B011 — mixed date palms from seed

- **Initial image:** unknown seeds produce a mixed grove; nurture, barrenness, and harvest become roles.
- **V23:** `عدو=E:B011 | ضبح=Ø | وري=Ø | قدح=E:B009 | غير=E:B001 | صبح=Ø | ثور=E:B002 | نقع=E:B002/B007 | وسط=Ø | جمع=S:B011 | ءنس=Ø | ربب=E:B002/B008/B012 | كند=E:B003 | شهد=Ø | حبب=E:B001 | خير=E:B001/B005 | شدد=Ø | علم=Ø | بعثر=E:B001 | قبر=E:B002 | حصل=E:B002/B003/B005 | صدر=Ø | خبر=C:B002/B003/B005`.
- **Lifecycle:** G=`ج م ع B011 + ع د و B011 + ق د ح B009 + غ ي ر B001 + ث و ر B002 + ن ق ع B002/B007 + ر ب ب B002/B008/B012 + ك ن د B003 + ح ب ب B001 + خ ي ر B001/B005 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003/B005`; freeze=mixed seed is nurtured or barren, earth is turned, yield separated; P=soil/cultivator. `خ ب ر B002/B003/B005` corroborate. `(K: no date palm, grove, seed, or crop context)`. **Grade: medium** — complete but almost wholly remote.

#### B012 — large full vessel

- **Initial image:** a great container is filled and later may be emptied or have contents extracted.
- **V23:** `عدو=Ø | ضبح=Ø | وري=E:B004 | قدح=E:B005/B006 | غير=E:B001 | صبح=F:B003 | ثور=Ø | نقع=E:B001/B002 | وسط=E:B002 | جمع=S:B012 | ءنس=Ø | ربب=E:B006/B013 | كند=Ø | شهد=Ø | حبب=E:B006/B007 | خير=Ø | شدد=Ø | علم=E:B005 | بعثر=C:B003 | قبر=C:B002 | حصل=C:B002/B004 | صدر=C:B001/B003 | خبر=C:B004`.
- **Lifecycle:** G=`ج م ع B012 + و ر ي B004 + ق د ح B005/B006 + غ ي ر B001 + ن ق ع B001/B002 + و س ط B002 + ر ب ب B006/B013 + ح ب ب B006/B007 + ع ل م B005`; freeze=large vessel/body holds abundant liquid/material at depth; P=inversion, recess, extraction, abundance. `ب ع ث ر B003 + ق ب ر B002 + ح ص ل B002/B004 + ص د ر B001/B003 + خ ب ر B004` corroborate geometry. Morning drink `ص ب ح B003` forks. `(K: no vessel, liquid, or filling; جَمْعًا is entered object)`. **Grade: weak**.

#### B013 — alliance around an undertaking

- **Initial image:** parties join around a cause; covenant, severance, rival attachment, and testimony become possible.
- **V23:** `عدو=F:B005 | ضبح=Ø | وري=F:B003 | قدح=E:B010 | غير=F:B002 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=F:B005 | جمع=S:B013 | ءنس=E:B001 | ربب=E:B001/B011 | كند=E:B001/B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B003 | شدد=E:B001 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`ج م ع B013 + ق د ح B010 + ء ن س B001 + ر ب ب B001/B011 + ك ن د B001/B002 + ش ه د B002 + ح ب ب B002 + خ ي ر B003 + ش د د B001`; freeze=human allegiance/covenant is severed while another chosen attachment tightens; P=knowledge, inner result/source, final return of the first relation. `ع ل م B001 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Redress/aid/compensation/mediation forks use `ع د و B005 + و ر ي B003 + غ ي ر B002 + و س ط B005`. `(K: no explicit alliance/covenant or social parties)`. **Grade: medium**.

### 100:6:2 `ٱلْإِنسَانَ` — `ء ن س`

#### B001 — human appears after the kinetic collective

- **Initial image:** the generic singular human contrasts with the preceding feminine-plural action chain and later returns as a plurality.
- **V23:** `عدو=E:B002 | ضبح=E:B001/B002 | وري=F:B008 | قدح=Ø | غير=E:B005 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=E:B002 | ءنس=S:B001 | ربب=E:B001 | كند=E:B002 | شهد=C:B001/B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B002 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ء ن س B001` plus `(E: 3FP opening morphology)` + `ع د و B002 + ض ب ح B001/B002 + غ ي ر B005 + ج م ع B002 + ر ب ب B001 + ك ن د B002 + ح ب ب B002 + خ ي ر B001 + ش د د B002`; freeze after 100:8=collective exterior action has contracted to one human's competing relations; P=singular continuity, interior locus, plural human return, knowledge. `ش ه د B001/B002 + ع ل م B001 + ح ص ل B001 + ص د ر B001/B004 + خ ب ر B001` and `(C: هُ→هُم sequence)` corroborate. All-creatures fork uses `و ر ي B008`. `(K: no explicit animal/human opposition or identity between opening and final plurals)`. **Grade: strong**.

#### B002 — perception by seeing/hearing/feeling

- **Initial image:** sound and visible effects become consciously perceived, then witnessed and known.
- **V23:** `عدو=E:B002 | ضبح=E:B001 | وري=E:B005 | قدح=Ø | غير=E:B003 | صبح=E:B005 | ثور=E:B001/B002 | نقع=E:B004/B005 | وسط=Ø | جمع=Ø | ءنس=S:B002 | ربب=Ø | كند=Ø | شهد=E:B001/B002/B008 | حبب=F:B004 | خير=Ø | شدد=Ø | علم=C:B001/B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ء ن س B002 + ع د و B002 + ض ب ح B001 + و ر ي B005 + غ ي ر B003 + ص ب ح B005 + ث و ر B001/B002 + ن ق ع B004/B005 + ش ه د B001/B002/B008`; freeze after 100:7=sound/appearance/trace becomes perception and witness; P=explicit cognition, direct exposure, inner source, inward expertise. `ع ل م B001/B002 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` corroborate. Heart-core `ح ب ب B004` forks. `(K: إِنسَانَ contextually denotes human, not a perception verb)`. **Grade: strong**.

#### B003 — companionship removing estrangement

- **Initial image:** a sustaining/intimate relation should remove estrangement; cutting gratitude reverses it.
- **V23:** `عدو=F:B003 | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=F:B013 | ءنس=S:B003 | ربب=E:B001/B005/B011 | كند=E:B001/B002 | شهد=C:B002 | حبب=E:B002 | خير=E:B005 | شدد=E:B001 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`ء ن س B003 + ر ب ب B001/B005/B011 + ك ن د B001/B002 + ح ب ب B002 + خ ي ر B005 + ش د د B001`; freeze=expected care/covenant/companionship is cut while another attachment tightens; P=witness, inner result/source, knowledge. `ش ه د B002 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Enmity/alliance forks use `ع د و B003 + ج م ع B013`. `(K: no companionship, loneliness, or reciprocal social syntax)`. **Grade: medium** — relational reversal is coherent, seed social detail remote.

#### B004 — human-facing side of mount/bow

- **Initial image:** an instrument has a side oriented toward its human user, potentially linking the opening agents to a rider or archer.
- **V23:** `عدو=E:B002/B008 | ضبح=E:B001/B002 | وري=E:B006 | قدح=E:B007/B008 | غير=Ø | صبح=E:B002/B004 | ثور=Ø | نقع=E:B007 | وسط=E:B002 | جمع=E:B010 | ءنس=S:B004 | ربب=F:B010/B014 | كند=Ø | شهد=F:B008 | حبب=F:B005 | خير=F:B003 | شدد=E:B003 | علم=F:B002 | بعثر=Ø | قبر=Ø | حصل=F:B006 | صدر=E:B002 | خبر=Ø`.
- **Lifecycle:** mount G=`ء ن س B004 + ع د و B002 + ض ب ح B001/B002 + ص ب ح B002/B004 + ن ق ع B007 + ج م ع B010 + ش د د B003 + ص د ر B002`; freeze=human-facing mount carries gathered force forward; P=rider/control relation. Bow/arrow fork adds `ع د و B008 + و ر ي B006 + ق د ح B007 + ر ب ب B010 + ش ه د B008 + خ ي ر B003 + ع ل م B002`; animal debility fork adds `ق د ح B008 + ر ب ب B014 + ح ب ب B005 + ح ص ل B006`. `(K: no mount, rider, bow, archer, or control attachment)`. **Grade: weak** — several exact apparatus roles, absent governing event.

#### B005 — pupil/human image in the eye

- **Initial image:** a human image appears in a dark visual center, enabling self-seeing and surface/core contrast.
- **V23:** `عدو=Ø | ضبح=F:B004 | وري=E:B005 | قدح=F:B008 | غير=E:B003 | صبح=E:B005/B006 | ثور=E:B001 | نقع=Ø | وسط=E:B002 | جمع=Ø | ءنس=S:B005 | ربب=Ø | كند=Ø | شهد=E:B001/B008 | حبب=E:B004 | خير=Ø | شدد=Ø | علم=C:B001/B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ء ن س B005 + و ر ي B005 + غ ي ر B003 + ص ب ح B005/B006 + ث و ر B001 + و س ط B002 + ش ه د B001/B008 + ح ب ب B004`; freeze=bright appearance and dark central image make the human present to a hidden core; P=knowing, covering opened, core/chest extracted, inner expertise. `ع ل م B001/B002 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002 + ص د ر B001 + خ ب ر B001` corroborate. Blackening and sunken-eye forks use `ض ب ح B004 + ق د ح B008`. `(K: no eye, reflection, or anatomical heart)`. **Grade: medium-strong** — a distinct visual self-witness model predicts closure.

#### B006 — self/intimate/companion

- **Initial image:** the “self” or intimate relation becomes the locus of preference and hidden intention.
- **V23:** `عدو=F:B007 | ضبح=Ø | وري=Ø | قدح=E:B010 | غير=Ø | صبح=Ø | ثور=Ø | نقع=F:B002 | وسط=Ø | جمع=E:B003/B013 | ءنس=S:B006 | ربب=E:B001/B005 | كند=E:B002 | شهد=C:B002 | حبب=E:B002 | خير=E:B003 | شدد=E:B002 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`ء ن س B006 + ق د ح B010 + ج م ع B003/B013 + ر ب ب B001/B005 + ك ن د B002 + ح ب ب B002 + خ ي ر B003 + ش د د B002`; freeze=self/intimate orientation gathers a deliberate, intense preference; P=testimony, cognition, result, inward source, final knowledge. `ش ه د B002 + ع ل م B001 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Distraction and self-settling forks use `ع د و B007 + ن ق ع B002`. `(K: no address, companion, or explicit “self” expression)`. **Grade: medium**.

### `ر ب ب` — occurrence-sensitive branch sweep

#### B001 — lordship/ownership

- **100:6:3 initial:** the generic human stands in a possessive/authority relation to the رب before denial and rival attachment unfold.
- **100:6:3 V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=F:B001 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=S:B001 | كند=E:B001/B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001/B005 | شدد=E:B001/B002 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **100:6:3 lifecycle:** G=`ر ب ب B001 + ء ن س B001 + ك ن د B001/B002 + ش ه د B002 + ح ب ب B002 + خ ي ر B001/B005 + ش د د B001/B002`; freeze after 100:8=the owner/lord relation is cut/denied while attachment to good tightens; P=cognition, extracted inner result/source, return of رب, inward knowledge. `ع ل م B001 + ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` and `(C: رَبَّهُم recurrence)` corroborate; provision `غ ي ر B001` forks. `(K: does not identify الخير as property)`. **Grade: strong**.
- **100:11:2 initial:** after disclosure, the plural possessive form reactivates the singular relation from 100:6.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=S:B001,E:B001@100:6 | كند=E:B001/B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B001/B002 | علم=E:B001 | بعثر=E:B001 | قبر=E:B001/B002 | حصل=E:B001/B002 | صدر=E:B001/B004 | خبر=C:B001`.
- **100:11:2 lifecycle:** G=late seed plus the already active 100:6 relation, denial, witness, attachment, cognition, and disclosures; freeze=the first relational target returns as subject after all hidden contents are opened; P=person-reference and inner-knowledge predicate. `(C: بِهِمْ attachment + خ ب ر B001 + final إِنَّ...لَ)` complete it. `(K: plural suffix expands the generic human; it does not create a new class)`. **Grade: strong**.

#### B002 — nurture, repair, completion

- **100:6:3 initial:** a nurturer gradually completes a dependent, making gratitude/yield expected.
- **100:6:3 V23:** `عدو=Ø | ضبح=Ø | وري=F:B003 | قدح=F:B009 | غير=E:B001 | صبح=Ø | ثور=E:B002 | نقع=E:B002/B007 | وسط=Ø | جمع=E:B001 | ءنس=E:B001 | ربب=S:B002 | كند=E:B002/B003 | شهد=C:B002 | حبب=E:B001/B002 | خير=E:B001/B005 | شدد=E:B002/B006 | علم=Ø | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001/B002/B003 | صدر=C:B004 | خبر=C:B001/B003`.
- **100:6:3 lifecycle:** relational G=`ر ب ب B002 + غ ي ر B001 + ء ن س B001 + ك ن د B002 + ح ب ب B002 + خ ي ر B001/B005 + ش د د B002/B006`; freeze=beneficiary withholds gratitude and clings to benefit; P=witness, result, inner source, informed nurturer. `ش ه د B002 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Agricultural fork adds `ث و ر B002 + ن ق ع B002/B007 + ج م ع B001 + ك ن د B003 + ح ب ب B001 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003 + خ ب ر B003`; success/growth branches F. **Grade: strong relationally; medium agricultural; final medium-strong.**
- **100:11:2 initial:** the nurturer returns after results have been extracted.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B001 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=S:B002,E:B002@100:6 | كند=E:B002/B003 | شهد=E:B002 | حبب=E:B001/B002 | خير=E:B001/B005 | شدد=E:B002/B006 | علم=E:B001 | بعثر=E:B001 | قبر=E:B002 | حصل=E:B001/B002/B003 | صدر=E:B001/B004 | خبر=C:B001/B003`.
- **100:11:2 lifecycle:** G=late nurturer seed plus already active gratitude/yield/disclosure sequence; freeze=caretaker evaluates the completed inward result; P=knowledge predicate. `خ ب ر B001` directly completes; B003 cultivation is a remote corroborative fork. `(K: no explicit developmental history or crop)`. **Grade: medium-strong**.

#### B003 — رب-related knowledge

- **100:6:3 initial:** a remote knowledge dimension within the رب dossier predicts an epistemic close.
- **100:6:3 V23:** `عدو=Ø | ضبح=F:B001 | وري=Ø | قدح=Ø | غير=Ø | صبح=F:B005 | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B002 | ربب=S:B003 | كند=E:B002 | شهد=E:B001/B002 | حبب=Ø | خير=Ø | شدد=Ø | علم=E:B001 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **100:6:3 lifecycle:** G=`ر ب ب B003 + ء ن س B002 + ك ن د B002 + ش ه د B001/B002 + ع ل م B001`; freeze=the human's denial is perceptible/witnessed under a رب-linked knowledge frame; P=hidden evidence opened and inward expertise. `ب ع ث ر B001 + ق ب ر B002 + ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` corroborate; sound/light forks use `ض ب ح B001 + ص ب ح B005`. `(K: surface رَبّ is not رباني; B003 remains secondary)`. **Grade: medium-strong**.
- **100:11:2 initial:** the same remote dimension is activated immediately before `خَبِيرٌ`.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=S:B003,E:B003@100:6 | كند=E:B002 | شهد=E:B002 | حبب=Ø | خير=Ø | شدد=Ø | علم=E:B001 | بعثر=E:B001 | قبر=E:B002 | حصل=E:B001/B002 | صدر=E:B001/B004 | خبر=C:B001`.
- **100:11:2 lifecycle:** G=late seed + earlier رب, denial, witness, cognition, and disclosed interiors; freeze=رب-related knowledge needs its actual predicate. `خ ب ر B001` completes it, while `(K: adjacent خَبِيرٌ—not B003—is the contextual knowledge word)`. **Grade: medium-strong**.

#### B004 — multitudes/groups

- **100:6:3 initial:** large groups may connect opening collective, generic human, and final human plurality.
- **100:6:3 V23:** `عدو=E:B002 | ضبح=E:B002 | وري=F:B008 | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=E:B003 | جمع=E:B002/B004 | ءنس=E:B001 | ربب=S:B004 | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=C:B001 | خبر=C:B001`.
- **100:6:3 lifecycle:** G=`ر ب ب B004 + ع د و B002 + ض ب ح B002 + و س ط B003 + ج م ع B002/B004 + ء ن س B001`; freeze=collective motion becomes a human multitude model; P=interior and final plurality. `ص د ر B001 + خ ب ر B001` and `(C: رَبَّهُم/بِهِمْ)` corroborate. All-creatures `و ر ي B008` forks. `(K: local رَبِّهِ is singular relational noun, not multitude)`. **Grade: weak**.
- **100:11:2 initial:** plural suffixes make a multitude image more available at closure.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=F:B008 | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=E:B002/B004 | ءنس=E:B001 | ربب=S:B004 | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=E:B001 | خبر=C:B001`.
- **100:11:2 lifecycle:** G=`ر ب ب B004 + ج م ع B002/B004 + ء ن س B001 + ص د ر B001`; freeze=human multitude with shared interior category; P=knowledge. `خ ب ر B001` completes; creatures fork `و ر ي B008`. `(K: no multitude or gathering predicate in final clause)`. **Grade: weak**.

#### B005 — fostered child/caretaker

- **100:6:3 initial:** a caretaker-dependent relation intensifies the expectation of gratitude and affection.
- **100:6:3 V23:** `عدو=Ø | ضبح=Ø | وري=F:B007 | قدح=Ø | غير=E:B001 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=F:B007 | ءنس=E:B001/B003 | ربب=S:B005 | كند=E:B001/B002 | شهد=C:B002 | حبب=E:B002 | خير=E:B005 | شدد=E:B001 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **100:6:3 lifecycle:** G=`ر ب ب B005 + غ ي ر B001 + ء ن س B001/B003 + ك ن د B001/B002 + ح ب ب B002 + خ ي ر B005 + ش د د B001`; freeze=care/companionship relation is cut despite benefit, while another attachment tightens; P=witness, inward result/source, knowledgeable caretaker. `ش ه د B002 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Descendant/pregnancy forks use `و ر ي B007 + ج م ع B007`. `(K: no child, foster relation, spouse, or caretaker action)`. **Grade: medium**.
- **100:11:2 initial:** caretaker returns as one who knows dependents after disclosure.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=F:B007 | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=S:B005,E:B005@100:6 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B005 | شدد=Ø | علم=E:B001 | بعثر=E:B001 | قبر=E:B002 | حصل=E:B001 | صدر=E:B001/B004 | خبر=C:B001`.
- **100:11:2 lifecycle:** G=late caretaker seed plus prior relation/denial/disclosure; freeze=caretaker knows dependents' inward result; `خ ب ر B001` completes. Descendant fork persists in `و ر ي B007`. `(K: possessive suffixes do not encode fosterage/kinship)`. **Grade: medium**.

#### B006 — thick syrup / repair with substance

- **100:6:3 initial:** a thick food/repairing material invites mixture, container, and provision roles.
- **100:6:3 V23:** `عدو=Ø | ضبح=F:B005 | وري=E:B004 | قدح=E:B005/B006 | غير=E:B001 | صبح=E:B003 | ثور=F:B005 | نقع=E:B001/B003 | وسط=Ø | جمع=E:B012 | ءنس=Ø | ربب=S:B006 | كند=Ø | شهد=Ø | حبب=E:B006/B007 | خير=F:B005 | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=E:B004 | صدر=Ø | خبر=C:B004/B005`.
- **100:6:3 lifecycle:** G=`ر ب ب B006 + و ر ي B004 + ق د ح B005/B006 + غ ي ر B001 + ص ب ح B003 + ن ق ع B001/B003 + ج م ع B012 + ح ب ب B006/B007 + ح ص ل B004`; freeze=thick provision fills vessel/body; P=food/liquid, eater, abundance. `خ ب ر B004/B005` corroborates abundance/soft material; ash/curd/gift forks use `ض ب ح B005 + ث و ر B005 + خ ي ر B005`. `(K: local رب is relational noun; no substance/container/meal)`. **Grade: unlikely**.
- **100:11:2 initial:** final رب is tested as material substance.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=E:B004 | قدح=F:B005 | غير=Ø | صبح=Ø | ثور=Ø | نقع=F:B001 | وسط=Ø | جمع=F:B012 | ءنس=Ø | ربب=S:B006 | كند=Ø | شهد=Ø | حبب=F:B007 | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=F:B004 | صدر=Ø | خبر=K:B001`.
- **100:11:2 lifecycle:** G=`ر ب ب B006 + و ر ي B004` only; pot/water/vessel/crop forks fail to create final syntax. `(K: رَبَّهُم is اسم إنّ with human possessive; خَبِيرٌ B001 is knowledge, not material quality)`. **Grade: unlikely**.

#### B007 — abiding, dwelling, duration

- **100:6:3 initial:** an enduring relation remains present even when denied.
- **100:6:3 V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=F:B001 | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001/B003 | ربب=S:B007 | كند=E:B001/B002 | شهد=C:B002 | حبب=E:B002 | خير=Ø | شدد=E:B001 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **100:6:3 lifecycle:** G=`ر ب ب B007 + ء ن س B001/B003 + ك ن د B001/B002 + ح ب ب B002 + ش د د B001`; freeze=an abiding relational presence is cut/denied while another bond persists; P=return of رب, inward result, knowledge. `ش ه د B002 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` and `(C: رَبَّهُم delayed recurrence)` corroborate; dawn/duration fork uses `ص ب ح B001`. `(K: no explicit dwelling or duration predicate)`. **Grade: medium**.
- **100:11:2 initial:** lexical return itself instantiates persistence across the human section.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=F:B001 | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=S:B007,E:B007@100:6 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=Ø | شدد=Ø | علم=E:B001 | بعثر=E:B001 | قبر=E:B002 | حصل=E:B001 | صدر=E:B001/B004 | خبر=C:B001`.
- **100:11:2 lifecycle:** G=late seed + earlier رب and intervening diagnosis/disclosure; freeze=relation remains active and returns after delay; P=knowledge. `خ ب ر B001` completes. `(K: recurrence supports persistence, not literal residence)`. **Grade: medium-strong**.

#### B008 — rain-cloud layers

- **100:6:3 initial:** cloud/rain supports vegetation, nurture, and yield.
- **100:6:3 V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=E:B009 | غير=E:B001 | صبح=Ø | ثور=F:B001/B007 | نقع=E:B001/B002/B007 | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=S:B008 | كند=E:B003 | شهد=Ø | حبب=E:B001/B008 | خير=E:B001 | شدد=Ø | علم=E:B005 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002/B003/B005 | صدر=Ø | خبر=C:B002/B003/B005`.
- **100:6:3 lifecycle:** G=`ر ب ب B008 + ق د ح B009 + غ ي ر B001 + ن ق ع B001/B002/B007 + ك ن د B003 + ح ب ب B001/B008 + خ ي ر B001 + ع ل م B005`; freeze=rain-cloud waters soil/seed but barren ground may fail; P=earth turning, yield/residue, soil/cultivator. `ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003/B005 + خ ب ر B002/B003/B005` corroborate; emergence/algae forks use `ث و ر B001/B007`. `(K: no cloud, rain, water, plant, or crop)`. **Grade: medium** — rich agricultural/water convergence, wholly remote.
- **100:11:2 initial:** cloud branch is tested after all disclosure content.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=F:B009 | غير=F:B001 | صبح=Ø | ثور=F:B007 | نقع=F:B001/B002 | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=S:B008 | كند=F:B003 | شهد=Ø | حبب=F:B001/B008 | خير=Ø | شدد=Ø | علم=F:B005 | بعثر=Ø | قبر=Ø | حصل=F:B003 | صدر=Ø | خبر=K:B001,F:B002/B003/B005`.
- **100:11:2 lifecycle:** no coherent final cloud run survives local syntax; agriculture/water branches remain forks. `(K: رَبَّهُم is human possessive and خَبِيرٌ B001 controls; no weather frame)`. **Grade: unlikely**.

#### B009 — recently delivered ewe/newness

- **100:6:3 initial:** recent birth/young state suggests dependency and maturation.
- **100:6:3 V23:** `عدو=Ø | ضبح=Ø | وري=E:B007 | قدح=Ø | غير=Ø | صبح=Ø | ثور=F:B001 | نقع=Ø | وسط=Ø | جمع=E:B007 | ءنس=E:B001 | ربب=S:B009 | كند=Ø | شهد=E:B006 | حبب=E:B001 | خير=Ø | شدد=E:B004 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=E:B005 | صدر=Ø | خبر=Ø`.
- **100:6:3 lifecycle:** G=`ر ب ب B009 + و ر ي B007 + ج م ع B007 + ء ن س B001 + ش ه د B006 + ح ب ب B001 + ش د د B004 + ح ص ل B005`; freeze=birth/newness matures into later generation/yield; P=parent, child, growth. Emergence `ث و ر B001` forks. `(K: no ewe, birth, youth, milk, or maturation role)`. **Grade: unlikely**.
- **100:11:2 initial:** newness/livestock at final position.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=F:B007 | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=S:B009 | كند=Ø | شهد=F:B006 | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=K:B001`.
- **100:11:2 lifecycle:** G=`ر ب ب B009` only; descendant/birth forks do not connect. `(K: final clause supplies human relation and knowledge, not livestock/newness)`. **Grade: unlikely**.

#### B010 — holder gathering arrow-lots

- **100:6:3 initial:** a holder contains marked lots/shafts awaiting selection.
- **100:6:3 V23:** `عدو=E:B008 | ضبح=Ø | وري=F:B003/B006 | قدح=E:B007 | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=E:B002 | جمع=E:B003 | ءنس=E:B004 | ربب=S:B010 | كند=Ø | شهد=E:B008 | حبب=Ø | خير=E:B003 | شدد=E:B001/B003 | علم=E:B002 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=E:B002 | خبر=Ø`.
- **100:6:3 lifecycle:** G=`ر ب ب B010 + ع د و B008 + ق د ح B007 + و س ط B002 + ج م ع B003 + ء ن س B004 + ش ه د B008 + خ ي ر B003 + ش د د B001/B003 + ع ل م B002 + ص د ر B002`; freeze=marked lot/shaft is held, chosen, and driven; P=bow/draw, chooser, target/result. Success/backside forks `و ر ي B003/B006`. `(K: no holder, arrow, draw, lot, or target; local رب is relational)`. **Grade: weak**.
- **100:11:2 initial:** final رب is tested as arrow holder after the whole passage.
- **100:11:2 V23:** `عدو=F:B008 | ضبح=Ø | وري=F:B006 | قدح=F:B007 | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=F:B003 | ءنس=F:B004 | ربب=S:B010 | كند=Ø | شهد=F:B008 | حبب=Ø | خير=F:B003 | شدد=Ø | علم=F:B002 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=F:B002 | خبر=K:B001`.
- **100:11:2 lifecycle:** all apparatus links remain rival forks; no final construction supports them. `(K: رَبَّهُم is اسم إنّ with possessive humans; خَبِيرٌ is knowledge)`. **Grade: unlikely**.

#### B011 — covenant/pledge

- **100:6:3 initial:** a covenantal bond to the رب can be cut while a rival attachment is tightened.
- **100:6:3 V23:** `عدو=F:B005 | ضبح=Ø | وري=F:B003 | قدح=E:B010 | غير=F:B002 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=F:B005 | جمع=E:B013 | ءنس=E:B001/B003 | ربب=S:B011 | كند=E:B001/B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B003/B005 | شدد=E:B001 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **100:6:3 lifecycle:** G=`ر ب ب B011 + ق د ح B010 + ج م ع B013 + ء ن س B001/B003 + ك ن د B001/B002 + ش ه د B002 + ح ب ب B002 + خ ي ر B003/B005 + ش د د B001`; freeze=covenantal/beneficent bond is severed while chosen love tightens; P=cognition, inward result/source, return of covenant party, knowledge. `ع ل م B001 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Legal aid/compensation/mediation forks use `ع د و B005 + و ر ي B003 + غ ي ر B002 + و س ط B005`. `(K: no explicit covenant noun; opening oath is not this covenant)`. **Grade: medium-strong**.
- **100:11:2 initial:** the first covenant party returns after the inward record is exposed.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=E:B013 | ءنس=E:B001 | ربب=S:B011,E:B011@100:6 | كند=E:B001/B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B005 | شدد=E:B001 | علم=E:B001 | بعثر=E:B001 | قبر=E:B002 | حصل=E:B001 | صدر=E:B001/B004 | خبر=C:B001`.
- **100:11:2 lifecycle:** G=late covenant seed plus active bond/severance/witness/disclosure sequence; freeze=relation persists as final frame; P=inner knowledge. `خ ب ر B001 + بِهِمْ` complete. `(K: final clause states knowledge, not covenant adjudication)`. **Grade: medium-strong**.

#### B012 — persistent plant

- **100:6:3 initial:** a maintained green plant contrasts with barren soil and invites yield testing.
- **100:6:3 V23:** `عدو=E:B011 | ضبح=Ø | وري=Ø | قدح=E:B009 | غير=E:B001 | صبح=Ø | ثور=E:B002 | نقع=E:B002/B007 | وسط=Ø | جمع=E:B001/B011 | ءنس=Ø | ربب=S:B012 | كند=E:B003 | شهد=Ø | حبب=E:B001 | خير=E:B001/B005 | شدد=Ø | علم=Ø | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002/B003/B005 | صدر=Ø | خبر=C:B002/B003/B005`.
- **100:6:3 lifecycle:** G=`ر ب ب B012 + ع د و B011 + ق د ح B009 + غ ي ر B001 + ث و ر B002 + ن ق ع B002/B007 + ج م ع B001/B011 + ك ن د B003 + ح ب ب B001 + خ ي ر B001/B005`; freeze=nurtured plant/seed confronts barrenness; P=earth turned, yield/residue separated, cultivator. `ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003/B005 + خ ب ر B002/B003/B005` corroborate. `(K: no contextual plant or crop; all roles remote)`. **Grade: medium**.
- **100:11:2 initial:** plant branch at final رب position.
- **100:11:2 V23:** `عدو=F:B011 | ضبح=Ø | وري=Ø | قدح=F:B009 | غير=F:B001 | صبح=Ø | ثور=Ø | نقع=F:B007 | وسط=Ø | جمع=F:B011 | ءنس=Ø | ربب=S:B012 | كند=F:B003 | شهد=Ø | حبب=F:B001 | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=F:B003 | صدر=Ø | خبر=K:B001,F:B003/B005`.
- **100:11:2 lifecycle:** agriculture links remain forks, not a final model. `(K: final human possessive and knowledge predication defeat plant reading)`. **Grade: unlikely**.

#### B013 — abundant/fresh water

- **100:6:3 initial:** abundant water supplies and fills, inviting hydration and cultivation.
- **100:6:3 V23:** `عدو=Ø | ضبح=Ø | وري=E:B004 | قدح=E:B006 | غير=E:B001 | صبح=E:B003 | ثور=F:B007 | نقع=E:B001/B002 | وسط=Ø | جمع=E:B012 | ءنس=Ø | ربب=S:B013 | كند=F:B003 | شهد=Ø | حبب=E:B006/B007/B008 | خير=F:B005 | شدد=Ø | علم=E:B005 | بعثر=Ø | قبر=Ø | حصل=E:B004 | صدر=E:B003 | خبر=C:B002/B004`.
- **100:6:3 lifecycle:** G=`ر ب ب B013 + و ر ي B004 + ق د ح B006 + غ ي ر B001 + ص ب ح B003 + ن ق ع B001/B002 + ج م ع B012 + ح ب ب B006/B007/B008 + ع ل م B005 + ح ص ل B004 + ص د ر B003`; freeze=abundant provision fills vessel/body and is consumed/left; P=water source, drinker, abundance. `خ ب ر B002/B004` corroborates wet land/large waterskin; algae/barren/gift forks use `ث و ر B007 + ك ن د B003 + خ ي ر B005`. `(K: no water, vessel, or drinking)`. **Grade: weak**.
- **100:11:2 initial:** abundant water at final relational noun.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=F:B004 | قدح=F:B006 | غير=Ø | صبح=Ø | ثور=Ø | نقع=F:B001/B002 | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=S:B013 | كند=Ø | شهد=Ø | حبب=F:B006/B007 | خير=Ø | شدد=Ø | علم=F:B005 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=K:B001,F:B002/B004`.
- **100:11:2 lifecycle:** only a water/storage fork forms; `(K: رَبَّهُم + بِهِمْ + خَبِيرٌ is human relation/knowledge, not water abundance)`. **Grade: unlikely**.

#### B014 — herd

- **100:6:3 initial:** a herd could identify the opening collective and contrast with the human.
- **100:6:3 V23:** `عدو=E:B002 | ضبح=E:B001/B002 | وري=F:B008 | قدح=F:B008 | غير=Ø | صبح=E:B002/B004 | ثور=F:B004 | نقع=E:B007 | وسط=E:B003 | جمع=E:B002/B010 | ءنس=E:B001/B004 | ربب=S:B014 | كند=Ø | شهد=Ø | حبب=F:B005 | خير=Ø | شدد=E:B003 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=F:B006 | صدر=E:B002 | خبر=Ø`.
- **100:6:3 lifecycle:** G=`ر ب ب B014 + ع د و B002 + ض ب ح B001/B002 + ص ب ح B002/B004 + ن ق ع B007 + و س ط B003 + ج م ع B002/B010 + ء ن س B001/B004 + ش د د B003 + ص د ر B002`; freeze=herd/mounts run under a human-facing relation; P=species, rider, control. Creature/lean animal/bull/exhaustion/pain forks use `و ر ي B008 + ق د ح B008 + ث و ر B004 + ح ب ب B005 + ح ص ل B006`. `(K: no herd, species, or rider)`. **Grade: weak**.
- **100:11:2 initial:** plural humans might superficially resemble a herd.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=F:B008 | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=F:B002 | ءنس=E:B001 | ربب=S:B014 | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=K:B001`.
- **100:11:2 lifecycle:** G=`ر ب ب B014 + ء ن س B001` cannot progress beyond generic group; `(K: discourse referent is human and final predicate is knowledge)`. **Grade: unlikely**.

#### B015 — particle `رُبَّ/ربما`

- **100:6:3 initial:** a particle reading would introduce frequency/quantity scope.
- **100:6:3 V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=S:B015 | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **100:6:3 lifecycle:** G=`ر ب ب B015` only; freeze=particle awaiting scope; P=following indefinite clause. `(K: QAC tags رَبِّ as genitive noun with possessive suffix under لِـ)`. **Grade: unlikely**.
- **100:11:2 initial:** particle reading at اسم إنّ position.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=S:B015 | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **100:11:2 lifecycle:** G=seed only; `(K: QAC and attachment rows force accusative noun + 3MP possessive as اسم إنّ)`. **Grade: unlikely**.

#### B016 — need, blessing, firm knot

- **100:6:3 initial:** blessing/need is held in a firm bond; denial cuts it while love tightens elsewhere.
- **100:6:3 V23:** `عدو=F:B012 | ضبح=Ø | وري=Ø | قدح=E:B010 | غير=E:B001 | صبح=Ø | ثور=Ø | نقع=F:B002 | وسط=F:B006 | جمع=F:B008 | ءنس=E:B001/B006 | ربب=S:B016 | كند=E:B001/B002 | شهد=C:B002 | حبب=E:B002 | خير=E:B001/B005 | شدد=E:B001/B002 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **100:6:3 lifecycle:** G=`ر ب ب B016 + ق د ح B010 + غ ي ر B001 + ء ن س B001/B006 + ك ن د B001/B002 + ح ب ب B002 + خ ي ر B001/B005 + ش د د B001/B002`; freeze=beneficent bond/need is cut while deliberate value-attachment tightens; P=witness, cognition, inner result/source, knowledge. `ش ه د B002 + ع ل م B001 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Twisted restraint/bisection/shackle/self-settling forks use `ع د و B012 + ن ق ع B002 + و س ط B006 + ج م ع B008`. `(K: B016 combines remote senses; no literal knot/blessing noun)`. **Grade: medium-strong**.
- **100:11:2 initial:** blessing/bond returns after disclosure.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B001 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=S:B016,E:B016@100:6 | كند=E:B001/B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B005 | شدد=E:B001 | علم=E:B001 | بعثر=E:B001 | قبر=E:B002 | حصل=E:B001 | صدر=E:B001/B004 | خبر=C:B001`.
- **100:11:2 lifecycle:** G=late seed plus earlier benefit/bond, denial, witness, and disclosure; freeze=relation returns as final frame; P=inner knowledge. `خ ب ر B001` completes. `(K: no need/knot/blessing is explicitly named)`. **Grade: medium**.

#### B017 — shipmaster

- **100:6:3 initial:** a leader directs sailors/crew through movement.
- **100:6:3 V23:** `عدو=F:B002 | ضبح=Ø | وري=F:B006 | قدح=Ø | غير=Ø | صبح=F:B002 | ثور=Ø | نقع=F:B001/B008 | وسط=F:B003 | جمع=F:B002 | ءنس=E:B001 | ربب=S:B017 | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=F:B001 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=F:B003 | خبر=F:B001`.
- **100:6:3 lifecycle:** G=`ر ب ب B017 + ء ن س B001` only; movement/backside/morning/water-route/group/entry/knowledge/departure branches form a maritime possibility but no ship/sailor/water/command event. `(K: local رب denotes relational noun with human possessive)`. **Grade: unlikely**.
- **100:11:2 initial:** leader-of-crew at final position.
- **100:11:2 V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=F:B002 | ءنس=E:B001 | ربب=S:B017 | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=K:B001`.
- **100:11:2 lifecycle:** G=`ر ب ب B017 + ء ن س B001`; no navigation roles. `(K: final clause is human-reference plus knowledge, not maritime command)`. **Grade: unlikely**.

### 100:6:4 `لَكَنُودٌ` — `ك ن د`

#### B001 — cutting/separation

- **Initial image:** a relation or gathered whole is cut; a rival bond may tighten, followed by scattering and recollection.
- **V23:** `عدو=F:B012 | ضبح=Ø | وري=Ø | قدح=F:B002 | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=F:B006 | جمع=E:B001/B008/B009 | ءنس=E:B001 | ربب=E:B001/B011/B016 | كند=S:B001 | شهد=E:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B001 | علم=C:B001 | بعثر=C:B002/B003 | قبر=Ø | حصل=C:B001/B002 | صدر=C:B004/B006 | خبر=C:B001`.
- **Lifecycle:** relational G=`ك ن د B001 + ء ن س B001 + ر ب ب B001/B011/B016 + ش ه د B002 + ح ب ب B002 + خ ي ر B001 + ش د د B001`; freeze=first bond is cut while love of good tightens; P=cognition, inward source/result, return of رب, knowledge. `ع ل م B001 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Structural fork G=`غ ي ر B003 + ج م ع B001/B009 + ك ن د B001`; `ب ع ث ر B002/B003 + ح ص ل B001/B002 + ص د ر B006` corroborate gather→sever→scatter→recover. Twisted/cracked/bisected/shackled forks are marked F. `(K: no literal cutting event)`. **Grade: strong**.

#### B002 — ingratitude/withheld affection

- **Initial image:** benefit is received but gratitude/affection is withheld while desire attaches to the benefit.
- **V23:** `عدو=F:B007 | ضبح=Ø | وري=F:B003 | قدح=F:B010 | غير=E:B001 | صبح=Ø | ثور=Ø | نقع=F:B002 | وسط=Ø | جمع=F:B003 | ءنس=E:B001/B003 | ربب=E:B001/B002/B005 | كند=S:B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001/B005 | شدد=E:B002/B006 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ك ن د B002 + غ ي ر B001 + ء ن س B001/B003 + ر ب ب B001/B002/B005 + ش ه د B002 + ح ب ب B002 + خ ي ر B001/B005 + ش د د B002/B006`; freeze=the beneficiary denies the sustaining relation and intensely withholds/attaches around good; P=cognition, inner contents/result/source, return of رب, informed closure. `ع ل م B001 + ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` corroborate. Distraction, successful aid, planning, self-settling, and resolve forks use `ع د و B007 + و ر ي B003 + ق د ح B010 + ن ق ع B002 + ج م ع B003`. `(K: no external benefit inventory or transaction)`. **Grade: strong**.

#### B003 — barren soil

- **Initial image:** nurtured soil produces no growth; later earth-turning and yield separation test it.
- **V23:** `عدو=E:B011 | ضبح=Ø | وري=Ø | قدح=E:B004/B009 | غير=E:B001 | صبح=Ø | ثور=E:B002 | نقع=E:B002/B007 | وسط=Ø | جمع=E:B001/B011 | ءنس=E:B001 | ربب=E:B002/B008/B012 | كند=S:B003 | شهد=Ø | حبب=E:B001 | خير=E:B001/B005 | شدد=Ø | علم=Ø | بعثر=E:B001 | قبر=E:B001/B002 | حصل=E:B002/B003/B005 | صدر=F:B004 | خبر=C:B002/B003/B005,C:B001`.
- **Lifecycle:** G=`ك ن د B003 + ع د و B011 + ق د ح B004/B009 + غ ي ر B001 + ث و ر B002 + ن ق ع B002/B007 + ج م ع B001/B011 + ء ن س B001 + ر ب ب B002/B008/B012 + ح ب ب B001 + خ ي ر B001/B005 + ب ع ث ر B001 + ق ب ر B001/B002 + ح ص ل B002/B003/B005`; freeze=the human is secondarily modeled as ground whose nurtured/barren yield is exposed; P=soil/cultivator evaluator. `خ ب ر B002/B003/B005` corroborates agriculture; contextual `خ ب ر B001` constrains the close. `ص د ر B004` forks into inward source. `(K: كَنُودٌ predicates human, not land; no literal crop)`. **Grade: medium-strong** — deepest agriculture convergence, high lexical distance.

#### B004 — proper name Kinda

- **Initial image:** a named tribe/group.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=F:B006 | نقع=Ø | وسط=Ø | جمع=F:B002/B004 | ءنس=Ø | ربب=F:B004 | كند=S:B004 | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ك ن د B004` only; proper-place/tribe/multitude forks use `ث و ر B006 + ج م ع B002/B004 + ر ب ب B004`. `(K: indefinite predicate morphology and no naming/genealogy construction)`. **Grade: unlikely**.

### 100:7:4 `لَشَهِيدٌ` — `ش ه د`

#### B001 — presence with observation

- **Initial image:** the human is present to the diagnosed state; earlier effects can become observed evidence.
- **V23:** `عدو=Ø | ضبح=E:B001 | وري=E:B005 | قدح=E:B002 | غير=E:B003 | صبح=E:B005 | ثور=E:B001/B002 | نقع=E:B004 | وسط=Ø | جمع=Ø | ءنس=E:B002/B005 | ربب=E:B001 | كند=E:B002 | شهد=S:B001 | حبب=Ø | خير=Ø | شدد=Ø | علم=C:B001/B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ش ه د B001 + ض ب ح B001 + و ر ي B005 + ق د ح B002 + غ ي ر B003 + ص ب ح B005 + ث و ر B001/B002 + ن ق ع B004 + ء ن س B002/B005 + ر ب ب B001 + ك ن د B002`; freeze=human presence/observation organizes sound, appearance, marks, and diagnosis; P=explicit cognition, direct exposure, inner result/source, superior knowledge. `ع ل م B001/B002 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` corroborate. `(K: عَلَىٰ ذَٰلِكَ does not specify visual modality)`. **Grade: strong**.

#### B002 — testimony/statement based on knowledge

- **Initial image:** the human bears informed testimony concerning the preceding diagnosis.
- **V23:** `عدو=F:B005 | ضبح=F:B001 | وري=Ø | قدح=F:B003 | غير=F:B002 | صبح=Ø | ثور=Ø | نقع=F:B005/B009 | وسط=F:B005 | جمع=F:B013 | ءنس=E:B001/B002 | ربب=E:B001 | كند=E:B002 | شهد=S:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B002 | علم=C:B001 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ش ه د B002 + ء ن س B001/B002 + ر ب ب B001 + ك ن د B002 + ح ب ب B002 + خ ي ر B001 + ش د د B002`; freeze=testimony concerns the two human orientations; P=cognition, exposed basis, inner result/source, final knower. `ع ل م B001 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` corroborate. Legal/speech forks use `ع د و B005 + ق د ح B003 + غ ي ر B002 + ن ق ع B005/B009 + و س ط B005 + ج م ع B013`; `(K: no courtroom or spoken deposition)`. **Grade: strong**.

#### B005 — tongue/expression revealing speaker

- **Initial image:** outward expression reveals the person and points back to an inward source.
- **V23:** `عدو=Ø | ضبح=E:B001 | وري=E:B005 | قدح=F:B003 | غير=Ø | صبح=Ø | ثور=Ø | نقع=E:B005/F:B009 | وسط=Ø | جمع=Ø | ءنس=E:B002 | ربب=Ø | كند=Ø | شهد=S:B005 | حبب=F:B009 | خير=Ø | شدد=Ø | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`ش ه د B005 + ض ب ح B001 + و ر ي B005 + ن ق ع B005 + ء ن س B002`; freeze=sound/expression makes a concealed speaker perceptible; P=cognition, inward source/result, report of inner matter. `ع ل م B001 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Slander/insult/teeth-mouth forks use `ق د ح B003 + ن ق ع B009 + ح ب ب B009`. `(K: no tongue, utterance, or speech event)`. **Grade: medium**.

#### B006 — material emerging at birth/maturation

- **Initial image:** birth or maturation produces outward signs.
- **V23:** `عدو=Ø | ضبح=Ø | وري=E:B007 | قدح=Ø | غير=Ø | صبح=Ø | ثور=E:B001 | نقع=Ø | وسط=Ø | جمع=E:B006/B007 | ءنس=E:B001 | ربب=E:B005/B009 | كند=Ø | شهد=S:B006 | حبب=E:B001 | خير=Ø | شدد=E:B004 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=E:B005 | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ش ه د B006 + و ر ي B007 + ث و ر B001 + ج م ع B006/B007 + ء ن س B001 + ر ب ب B005/B009 + ح ب ب B001 + ش د د B004 + ح ص ل B005`; freeze=contained generation emerges and matures; P=parent, child, birth context. `(K: no reproductive or maturation roles; شَهِيدٌ is predicative witness)`. **Grade: unlikely**.

#### B007 — honey enclosed in wax

- **Initial image:** a valuable sweet core remains in a casing before pressing/extraction.
- **V23:** `عدو=Ø | ضبح=Ø | وري=E:B005 | قدح=F:B005 | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=E:B002 | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=S:B007 | حبب=F:B007 | خير=E:B001 | شدد=Ø | علم=Ø | بعثر=C:B003 | قبر=C:B002 | حصل=C:B002/B003 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ش ه د B007 + و ر ي B005 + و س ط B002 + خ ي ر B001`; freeze=valuable content is concealed in a casing/center; P=covering opened, core/residue extracted, inner evaluator. `ب ع ث ر B003 + ق ب ر B002 + ح ص ل B002/B003 + ص د ر B001 + خ ب ر B001` corroborate. Pot/jar forks use `ق د ح B005 + ح ب ب B007`. `(K: no honey, wax, pressing, or food; شَهِيدٌ form controls)`. **Grade: medium** — exact extraction geometry, substance absent.

#### B008 — a sign that witnesses

- **Initial image:** opening effects become marks that indicate their unseen cause; later the human becomes witness and then is challenged to know.
- **V23:** `عدو=E:B002/B010 | ضبح=E:B001 | وري=E:B005 | قدح=E:B002 | غير=E:B003 | صبح=E:B005 | ثور=E:B001/B002 | نقع=E:B004 | وسط=Ø | جمع=Ø | ءنس=E:B002 | ربب=Ø | كند=Ø | شهد=S:B008 | حبب=Ø | خير=Ø | شدد=Ø | علم=C:B001/B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ش ه د B008 + ع د و B002/B010 + ض ب ح B001 + و ر ي B005 + ق د ح B002 + غ ي ر B003 + ص ب ح B005 + ث و ر B001/B002 + ن ق ع B004 + ء ن س B002`; freeze=motion leaves audible/visible marks that testify; P=explicit knowledge, direct exposure, inward source/result, inner expertise. `ع ل م B001/B002 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` corroborate. `(K: opening effects are not grammatically called signs)`. **Grade: strong**.

### 100:8:2 `لِحُبِّ` — `ح ب ب`

#### B001 — seed bearing future yield

- **Initial image:** a seed is held in earth/casing until nurture or barrenness determines its yield.
- **V23:** `عدو=E:B011 | ضبح=Ø | وري=E:B005 | قدح=E:B004/B009 | غير=E:B001 | صبح=Ø | ثور=E:B001/B002 | نقع=E:B002/B007 | وسط=E:B002 | جمع=E:B001/B011 | ءنس=E:B001 | ربب=E:B002/B008/B012 | كند=E:B003 | شهد=Ø | حبب=S:B001 | خير=E:B001/B005 | شدد=Ø | علم=Ø | بعثر=E:B001 | قبر=E:B001/B002 | حصل=E:B002/B003/B005 | صدر=F:B004 | خبر=C:B002/B003/B005,C:B001`.
- **Lifecycle:** G=`ح ب ب B001 + ع د و B011 + و ر ي B005 + ق د ح B004/B009 + غ ي ر B001 + ث و ر B001/B002 + ن ق ع B002/B007 + و س ط B002 + ج م ع B001/B011 + ء ن س B001 + ر ب ب B002/B008/B012 + ك ن د B003 + خ ي ر B001/B005 + ب ع ث ر B001 + ق ب ر B001/B002 + ح ص ل B002/B003/B005`; freeze=human as seed/ground is nurtured or barren, then earth/casing is opened and yield separated; P=soil/cultivator and inner-human control. `خ ب ر B002/B003/B005` corroborates cultivation, while `خ ب ر B001 + ص د ر B004` constrain/reframe as inward human knowledge. `(K: حُبّ is love, not grain)`. **Grade: medium-strong** — extensive role completion, remote context.

#### B002 — love abiding in the heart

- **Initial image:** love fixes an inward orientation toward good while another relation is denied.
- **V23:** `عدو=F:B007 | ضبح=Ø | وري=Ø | قدح=F:B010 | غير=F:B004 | صبح=Ø | ثور=Ø | نقع=F:B002 | وسط=Ø | جمع=F:B003/B013 | ءنس=E:B001/B003/B006 | ربب=E:B001/B002/B005/B011 | كند=E:B001/B002 | شهد=E:B002 | حبب=S:B002 | خير=E:B001/B005 | شدد=E:B001/B002/B006 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ح ب ب B002 + ء ن س B001/B003/B006 + ر ب ب B001/B002/B005/B011 + ك ن د B001/B002 + ش ه د B002 + خ ي ر B001/B005 + ش د د B001/B002/B006`; freeze=the human's inward love of benefit is intense/tight while gratitude/covenant toward the رب is cut; P=cognition, explicit interior, extracted result/source, return of رب, inward knowledge. `ع ل م B001 + ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` corroborate. Distraction/planning/jealousy/self-settling/resolve/alliance forks are explicit in `ع د و B007 + ق د ح B010 + غ ي ر B004 + ن ق ع B002 + ج م ع B003/B013`. `(K: الخير remains unspecified good)`. **Grade: strong**.

#### B003 — praise / extreme desire

- **Initial image:** desire reaches an approving maximum around what is selected as good.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=F:B010 | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=F:B001/B004 | جمع=F:B003 | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=C:B002 | حبب=S:B003 | خير=E:B001/B002/B003 | شدد=E:B002 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`ح ب ب B003 + ء ن س B001 + ر ب ب B001 + ك ن د B002 + خ ي ر B001/B002/B003 + ش د د B002`; freeze=human assigns maximal preference to selected good despite the رب relation; P=witness, cognition, inner result/source, final knowledge. `ش ه د B002 + ع ل م B001 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Planning/resolve/quality-center forks use `ق د ح B010 + ج م ع B003 + و س ط B001/B004`. `(K: no حبذا/praise formula or comparison set)`. **Grade: medium-strong**.

#### B004 — dark heart-core

- **Initial image:** love occupies a central dark inward core; the later chest becomes a predicted enclosure.
- **V23:** `عدو=E:B004 | ضبح=F:B004 | وري=E:B005 | قدح=Ø | غير=E:B003 | صبح=F:B006 | ثور=E:B001 | نقع=Ø | وسط=E:B002/B003 | جمع=Ø | ءنس=E:B005 | ربب=E:B001 | كند=E:B002 | شهد=E:B001 | حبب=S:B004 | خير=E:B001 | شدد=E:B002 | علم=C:B001 | بعثر=C:B001/B003 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ح ب ب B004 + ع د و B004 + و ر ي B005 + غ ي ر B003 + ث و ر B001 + و س ط B002/B003 + ء ن س B005 + ر ب ب B001 + ك ن د B002 + ش ه د B001 + خ ي ر B001 + ش د د B002`; freeze=the human's value-orientation occupies a concealed central core; P=cognition, enclosure inversion, core extraction, chest/source, inner knowledge. `ع ل م B001 + ب ع ث ر B001/B003 + ق ب ر B002 + ح ص ل B002 + ص د ر B001/B004 + خ ب ر B001` corroborate. Blackening/brightness forks use `ض ب ح B004 + ص ب ح B006`. `(K: no anatomical heart or dark spot named)`. **Grade: strong as secondary geometry, medium-strong final due distance.**

#### B005 — exhausted camel remains down

- **Initial image:** exertion culminates in animal immobility or illness.
- **V23:** `عدو=E:B002 | ضبح=E:B001/B002 | وري=F:B001 | قدح=E:B008 | غير=Ø | صبح=E:B008 | ثور=Ø | نقع=E:B007 | وسط=Ø | جمع=E:B010 | ءنس=F:B004 | ربب=F:B014 | كند=Ø | شهد=Ø | حبب=S:B005 | خير=Ø | شدد=E:B003 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=E:B006 | صدر=E:B001 | خبر=Ø`.
- **Lifecycle:** G=`ح ب ب B005 + ع د و B002 + ض ب ح B001/B002 + ق د ح B008 + ص ب ح B008 + ن ق ع B007 + ج م ع B010 + ش د د B003 + ح ص ل B006 + ص د ر B001`; freeze=running animal becomes lean/sick and stops; P=species, injury, stopping point. Lung, rider, herd forks use `و ر ي B001 + ء ن س B004 + ر ب ب B014`. `(K: opening agents continue through 100:5; no camel, debility, pain, or stop)`. **Grade: weak**.

#### B006 — filling with water

- **Initial image:** body/container fills until satisfied; relation to benefit may be modeled as filling a lack.
- **V23:** `عدو=Ø | ضبح=Ø | وري=E:B004 | قدح=E:B006 | غير=E:B001 | صبح=E:B003 | ثور=Ø | نقع=E:B001/B002 | وسط=Ø | جمع=E:B012 | ءنس=F:B006 | ربب=E:B013 | كند=F:B002 | شهد=Ø | حبب=S:B006 | خير=E:B001/B005 | شدد=F:B002 | علم=E:B005 | بعثر=Ø | قبر=Ø | حصل=E:B004 | صدر=F:B003 | خبر=C:B004`.
- **Lifecycle:** G=`ح ب ب B006 + و ر ي B004 + ق د ح B006 + غ ي ر B001 + ص ب ح B003 + ن ق ع B001/B002 + ج م ع B012 + ر ب ب B013 + خ ي ر B001/B005 + ع ل م B005 + ح ص ل B004`; freeze=benefit/water fills a body/vessel; P=drinker, liquid, abundance, departure. `خ ب ر B004` corroborates abundance; self/ingratitude/intensity/departure forks use `ء ن س B006 + ك ن د B002 + ش د د B002 + ص د ر B003`. `(K: حُبّ is love, no liquid/filling syntax)`. **Grade: weak**.

#### B007 — large jar

- **Initial image:** a large container holds contents for later opening/extraction.
- **V23:** `عدو=Ø | ضبح=Ø | وري=E:B005 | قدح=E:B005/B006 | غير=Ø | صبح=Ø | ثور=Ø | نقع=E:B001 | وسط=E:B002 | جمع=E:B012 | ءنس=Ø | ربب=E:B006/B013 | كند=Ø | شهد=Ø | حبب=S:B007 | خير=Ø | شدد=Ø | علم=Ø | بعثر=C:B003 | قبر=C:B002 | حصل=C:B002/B003 | صدر=C:B001 | خبر=C:B001/B004`.
- **Lifecycle:** G=`ح ب ب B007 + و ر ي B005 + ق د ح B005/B006 + ن ق ع B001 + و س ط B002 + ج م ع B012 + ر ب ب B006/B013`; freeze=large concealed vessel has deep contents; P=inversion, recess, core/residue extraction, abundance/knowledge. `ب ع ث ر B003 + ق ب ر B002 + ح ص ل B002/B003 + ص د ر B001 + خ ب ر B001/B004` corroborate geometry. `(K: no jar, liquid, or material vessel; grave/chest are distinct contextual containers)`. **Grade: medium**.

#### B008 — water bubbles/waves

- **Initial image:** surface bubbles reveal motion in a water body.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B001 | صبح=Ø | ثور=E:B007 | نقع=E:B001/B002 | وسط=Ø | جمع=Ø | ءنس=E:B002 | ربب=E:B008/B013 | كند=Ø | شهد=F:B008 | حبب=S:B008 | خير=Ø | شدد=Ø | علم=E:B005 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=C:B002/B005`.
- **Lifecycle:** G=`ح ب ب B008 + غ ي ر B001 + ث و ر B007 + ن ق ع B001/B002 + ء ن س B002 + ر ب ب B008/B013 + ع ل م B005`; freeze=rain/water produces perceptible surface motion; P=wet soil/soft vegetation. `خ ب ر B002/B005` corroborate; sign `ش ه د B008` forks. `(K: no water, bubbles, waves, rain, or plant)`. **Grade: unlikely**.

#### B009 — ordered teeth/beads

- **Initial image:** mouth/teeth make breath or speech visible and ordered.
- **V23:** `عدو=Ø | ضبح=E:B001 | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=E:B005 | وسط=Ø | جمع=E:B009 | ءنس=E:B002 | ربب=Ø | كند=Ø | شهد=E:B005 | حبب=S:B009 | خير=Ø | شدد=Ø | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`ح ب ب B009 + ض ب ح B001 + ن ق ع B005 + ج م ع B009 + ء ن س B002 + ش ه د B005`; freeze=ordered mouth/teeth emit perceptible sound/expression; P=cognition, inward source, report. `ع ل م B001 + ص د ر B004 + خ ب ر B001` corroborate abstractly. `(K: no teeth, beads, mouth, or utterance)`. **Grade: weak**.

#### B010 — small/short body

- **Initial image:** a diminutive body or weakened animal.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=F:B008 | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=F:B014 | كند=Ø | شهد=Ø | حبب=S:B010 | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ح ب ب B010 + ء ن س B001`; freeze=small human/animal body; P=size comparison. Lean horse/herd forks use `ق د ح B008 + ر ب ب B014`. `(K: no stature or size predicate)`. **Grade: unlikely**.

#### B011 — weak sparks from stones/hooves

- **Initial image:** the late root-form reactivates opening hoof/stone sparks beside the word of intensity.
- **V23:** `عدو=E:B002/B010 | ضبح=E:B002/B003 | وري=E:B002 | قدح=E:B001 | غير=Ø | صبح=Ø | ثور=E:B001/B002 | نقع=E:B004 | وسط=Ø | جمع=E:B010 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=S:B011 | خير=E:B001 | شدد=E:B002/B003 | علم=C:B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002/B003 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G at 100:8=`ح ب ب B011` plus backward replay `ع د و B002/B010 + ض ب ح B002/B003 + و ر ي B002 + ق د ح B001 + ث و ر B001/B002 + ن ق ع B004 + ج م ع B010 + خ ي ر B001 + ش د د B002/B003`; freeze=opening spark/charge returns as a secondary force/heat simulation for intense attachment; P=force applied to hidden interiors next. `ش ه د B008 + ع ل م B002 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003 + ص د ر B001 + خ ب ر B001` corroborate trace and forced disclosure. `(K: idafa/attachment fixes contextual love of good; sparks remain remote secondary branch)`. **Grade: strong reactivation, medium-strong final due distance.**

#### B012 — snake/devil

- **Initial image:** a hidden hostile creature/deceiver.
- **V23:** `عدو=F:B003/B006 | ضبح=Ø | وري=F:B005 | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=F:B006 | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=Ø | كند=Ø | شهد=Ø | حبب=S:B012 | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=F:B002 | حصل=Ø | صدر=F:B001 | خبر=Ø`.
- **Lifecycle:** G=`ح ب ب B012 + ء ن س B001`; freeze=hostile hidden creature; P=snake/devil, attack, deception. Enemy/contagion/concealment/poison/recess/chest forks use `ع د و B003/B006 + و ر ي B005 + ن ق ع B006 + ق ب ر B002 + ص د ر B001`; `(K: no creature, bite, devil, or deception role)`. **Grade: unlikely**.

### 100:8:3 `ٱلْخَيْرِ` — `خ ي ر`

#### B001 — desired beneficial good

- **Initial image:** useful/desirable good is the object around which love and intensity orient.
- **V23:** `عدو=F:B007 | ضبح=Ø | وري=F:B003 | قدح=F:B010 | غير=E:B001 | صبح=Ø | ثور=Ø | نقع=F:B002 | وسط=Ø | جمع=F:B003 | ءنس=E:B001/B006 | ربب=E:B001/B002 | كند=E:B001/B002 | شهد=E:B002 | حبب=E:B002 | خير=S:B001 | شدد=E:B001/B002/B006 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`خ ي ر B001 + غ ي ر B001 + ء ن س B001/B006 + ر ب ب B001/B002 + ك ن د B001/B002 + ش ه د B002 + ح ب ب B002 + ش د د B001/B002/B006`; freeze=benefit is desired and tightly/intensely held while gratitude to its source is cut/withheld; P=cognition, inner result/source, return of رب, knowledge. `ع ل م B001 + ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` corroborate. Distraction/success/planning/self-settling/resolve forks explicit. `(K: الخير is not narrowed to wealth or a material good)`. **Grade: strong**.

#### B002 — excellence/selection

- **Initial image:** an object is judged superior and becomes preferred.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=E:B010 | غير=E:B005 | صبح=F:B006 | ثور=Ø | نقع=Ø | وسط=E:B001/B004 | جمع=E:B003 | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=C:B002 | حبب=E:B003 | خير=S:B002 | شدد=E:B002 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`خ ي ر B002 + ق د ح B010 + غ ي ر B005 + و س ط B001/B004 + ج م ع B003 + ء ن س B001 + ر ب ب B001 + ك ن د B002 + ح ب ب B003 + ش د د B002`; freeze=human deliberation selects and intensely prefers what is judged better; P=testimony, cognition, inner result/source, informed evaluator. `ش ه د B002 + ع ل م B001 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate; brightness/beauty `ص ب ح B006` forks. `(K: no comparison set or explicit selection act)`. **Grade: medium-strong**.

#### B003 — choice/seeking the better

- **Initial image:** alternatives are weighed, resolve gathers, and one valued orientation is selected.
- **V23:** `عدو=F:B008 | ضبح=Ø | وري=F:B003 | قدح=E:B007/B010 | غير=E:B003/B005 | صبح=Ø | ثور=E:B001 | نقع=F:B008 | وسط=E:B001 | جمع=E:B003 | ءنس=E:B006 | ربب=E:B001 | كند=E:B002 | شهد=C:B002/B008 | حبب=E:B002/B003 | خير=S:B003 | شدد=E:B002 | علم=C:B001/B002 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`خ ي ر B003 + ق د ح B010 + غ ي ر B003/B005 + ث و ر B001 + و س ط B001 + ج م ع B003 + ء ن س B006 + ر ب ب B001 + ك ن د B002 + ح ب ب B002/B003 + ش د د B002`; freeze=self gathers deliberation and chooses intense value-orientation; P=testimony/sign, cognition, inner result/source, final expertise. `ش ه د B002/B008 + ع ل م B001/B002 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Arrow/lot/success/route-choice forks use `ع د و B008 + و ر ي B003 + ق د ح B007 + ن ق ع B008`. `(K: no overt alternatives or choice verb)`. **Grade: medium-strong**.

#### B005 — generosity/gift

- **Initial image:** good is gift/benefit from a sustaining source; ingratitude and possessive withholding form a relational economy.
- **V23:** `عدو=F:B007 | ضبح=Ø | وري=F:B003 | قدح=Ø | غير=E:B001 | صبح=Ø | ثور=Ø | نقع=F:B002 | وسط=Ø | جمع=Ø | ءنس=E:B001/B003 | ربب=E:B001/B002/B005/B016 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=S:B005 | شدد=E:B002/B006 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001/B002 | صدر=F:B005,C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`خ ي ر B005 + غ ي ر B001 + ء ن س B001/B003 + ر ب ب B001/B002/B005/B016 + ك ن د B002 + ش ه د B002 + ح ب ب B002 + ش د د B002/B006`; freeze=gift/nurture is received but gratitude/return is withheld while attachment fixes on the gift; P=cognition, result, inner source, final informed giver. `ع ل م B001 + ح ص ل B001/B002 + ص د ر B004 + خ ب ر B001` corroborate. Distraction/success/self-settling/seizure forks use `ع د و B007 + و ر ي B003 + ن ق ع B002 + ص د ر B005`. `(K: no explicit giving, possession, or return transaction)`. **Grade: medium-strong**.

#### B006 — drawing an animal from a burrow

- **Initial image:** a hidden occupant is induced out through another opening.
- **V23:** `عدو=E:B004/B009 | ضبح=Ø | وري=E:B005/B006 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B001/B002 | نقع=E:B007 | وسط=E:B002/B003 | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=S:B006 | شدد=Ø | علم=Ø | بعثر=C:B001/B003 | قبر=C:B001/B002 | حصل=C:B002 | صدر=C:B001/B002 | خبر=C:B001`.
- **Lifecycle:** G=`خ ي ر B006 + ع د و B004/B009 + و ر ي B005/B006 + غ ي ر B003 + ث و ر B001/B002 + ن ق ع B007 + و س ط B002/B003`; freeze=a concealed occupant crosses from recess through an opening after disturbance; P=buried enclosure opened, core extracted, front/interior relation, knowledge. `ب ع ث ر B001/B003 + ق ب ر B001/B002 + ح ص ل B002 + ص د ر B001/B002 + خ ب ر B001` corroborate geometry. `(K: no animal, burrow, lure, or second exit; الخير is object of love)`. **Grade: medium** — exact emergence geometry, missing participants.

### 100:8:4 `لَشَدِيدٌ` — `ش د د`

#### B001 — tightening bond/knot

- **Initial image:** one relational bond is tightened while another is cut.
- **V23:** `عدو=F:B012 | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=F:B006 | جمع=F:B008 | ءنس=E:B001/B003 | ربب=E:B001/B011/B016 | كند=E:B001/B002 | شهد=C:B002 | حبب=E:B002 | خير=E:B001 | شدد=S:B001 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`ش د د B001 + ء ن س B001/B003 + ر ب ب B001/B011/B016 + ك ن د B001/B002 + ح ب ب B002 + خ ي ر B001`; freeze=love-of-good bond tightens while رب bond/covenant is cut; P=witness, cognition, inner result/source, return/knowledge. `ش ه د B002 + ع ل م B001 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. Twisted/bisected/shackled forks use `ع د و B012 + و س ط B006 + ج م ع B008`. `(K: no literal knot or rope)`. **Grade: strong**.

#### B002 — force/intensity/hardness

- **Initial image:** love reaches high intensity and reactivates opening force.
- **V23:** `عدو=E:B002/B010 | ضبح=E:B001/B002 | وري=E:B002 | قدح=E:B001 | غير=Ø | صبح=Ø | ثور=E:B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B010 | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=C:B008 | حبب=E:B002,C:B011 | خير=E:B001 | شدد=S:B002 | علم=C:B002 | بعثر=C:B001/B003 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G at 100:8=`ش د د B002 + ح ب ب B002 + خ ي ر B001 + ء ن س B001 + ر ب ب B001 + ك ن د B002`, with backward force replay `ع د و B002/B010 + ض ب ح B001/B002 + و ر ي B002 + ق د ح B001 + ث و ر B002 + ن ق ع B004 + و س ط B003 + ج م ع B010`; freeze=intense inward attachment inherits opening force geometry; P=force on hidden enclosures. `ح ب ب B011 + ش ه د B008 + ع ل م B002 + ب ع ث ر B001/B003 + ق ب ر B002 + ح ص ل B002 + ص د ر B001 + خ ب ر B001` corroborate. `(K: لِحُبِّ is actual complement; no literal charge in 100:8)`. **Grade: strong**.

#### B003 — charge/run

- **Initial image:** late `شديد` reactivates the opening charge and predicts immediate forceful disclosure.
- **V23:** `عدو=E:B001/B002/B003 | ضبح=E:B001/B002 | وري=E:B002 | قدح=E:B001 | غير=Ø | صبح=E:B004 | ثور=E:B003 | نقع=E:B004 | وسط=E:B003 | جمع=E:B002/B010 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=E:B011 | خير=E:B001 | شدد=S:B003 | علم=C:B002 | بعثر=C:B001/B003 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001/B002 | خبر=C:B001`.
- **Lifecycle:** G=`ش د د B003 + ح ب ب B011 + خ ي ر B001` plus backward `ع د و B001/B002/B003 + ض ب ح B001/B002 + و ر ي B002 + ق د ح B001 + ص ب ح B004 + ث و ر B003 + ن ق ع B004 + و س ط B003 + ج م ع B002/B010`; freeze=charge/sparks are reactivated as secondary dynamics of intense attachment; P=next events force open resistant interiors. `ش ه د B008 + ع ل م B002 + ب ع ث ر B001/B003 + ق ب ر B002 + ح ص ل B002 + ص د ر B001/B002 + خ ب ر B001` corroborate. `(K: no enemy/combat at 100:8; contextual intensity remains relational)`. **Grade: medium-strong**.

#### B004 — mature strength/discernment

- **Initial image:** a human at maturity should possess knowledge and bear witness.
- **V23:** `عدو=Ø | ضبح=Ø | وري=F:B007 | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=F:B007 | ءنس=E:B001 | ربب=F:B005/B009 | كند=E:B002 | شهد=E:B001/B002/B006 | حبب=Ø | خير=Ø | شدد=S:B004 | علم=C:B001 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002/B005 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ش د د B004 + ء ن س B001 + ك ن د B002 + ش ه د B001/B002`; freeze=mature human is witness to the diagnosed state; P=knowing and disclosed interior. `ع ل م B001 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002 + ص د ر B001 + خ ب ر B001` corroborate. Generation/maturation forks use `و ر ي B007 + ج م ع B007 + ر ب ب B005/B009 + ش ه د B006 + ح ص ل B005`. `(K: no age or maturation construction)`. **Grade: medium**.

#### B005 — height of day

- **Initial image:** dawn rises toward a later height/time and may be recalled by `يَوْمَئِذٍ`.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=E:B001/B009 | ثور=Ø | نقع=Ø | وسط=Ø | جمع=F:B004 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=F:B008 | حبب=Ø | خير=Ø | شدد=S:B005 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=C:B001`.
- **Lifecycle:** G=`ش د د B005 + ص ب ح B001/B009`; freeze=dawn/time rises toward another marked day; P=later temporal boundary and final resolution. `(C: إِذَا + يَوْمَئِذٍ + خ ب ر B001)` corroborate; gathering-day/sign forks use `ج م ع B004 + ش ه د B008`. `(K: لَشَدِيدٌ is human predicate, no noon/day-height)`. **Grade: medium**.

#### B006 — miserliness/withholding

- **Initial image:** the human loves benefit intensely yet withholds gratitude/return.
- **V23:** `عدو=F:B007 | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B001 | صبح=Ø | ثور=Ø | نقع=F:B002 | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=E:B001/B002/B016 | كند=E:B002 | شهد=C:B002 | حبب=E:B002 | خير=E:B001/B005 | شدد=S:B006 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001/B002 | صدر=F:B005,C:B004 | خبر=C:B001`.
- **Lifecycle:** G=`ش د د B006 + غ ي ر B001 + ء ن س B001 + ر ب ب B001/B002/B016 + ك ن د B002 + ح ب ب B002 + خ ي ر B001/B005`; freeze=benefit is intensely held while gratitude/return is withheld; P=witness, cognition, inner result/source, final knowledge. `ش ه د B002 + ع ل م B001 + ح ص ل B001/B002 + ص د ر B004 + خ ب ر B001` corroborate. Distraction/self-settling/seizure forks use `ع د و B007 + ن ق ع B002 + ص د ر B005`. `(K: no possession, spending, or refusal transaction)`. **Grade: medium-strong**.

### 100:9:2 `يَعْلَمُ` — `ع ل م`

#### B001 — cognition/disclosure to the knower

- **Initial image:** the question reclassifies prior witness as incomplete knowledge and opens a demand for direct disclosure.
- **V23:** `عدو=Ø | ضبح=E:B001 | وري=E:B005 | قدح=Ø | غير=E:B003 | صبح=E:B005 | ثور=E:B001/B002 | نقع=E:B004/B005 | وسط=Ø | جمع=Ø | ءنس=E:B002 | ربب=E:B003 | كند=E:B002 | شهد=E:B001/B002/B008 | حبب=E:B002 | خير=E:B001 | شدد=E:B002 | علم=S:B001 | بعثر=C:B001 | قبر=C:B001/B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ع ل م B001` plus backward `ض ب ح B001 + و ر ي B005 + غ ي ر B003 + ص ب ح B005 + ث و ر B001/B002 + ن ق ع B004/B005 + ء ن س B002 + ر ب ب B003 + ك ن د B002 + ش ه د B001/B002/B008 + ح ب ب B002 + خ ي ر B001 + ش د د B002`; freeze=prior sound/appearance/witness and relational state are gathered into a cognition challenge; P=direct opening of hidden domains, extraction, inner source, superior inward knowledge. `ب ع ث ر B001 + ق ب ر B001/B002 + ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` immediately satisfy. `(K: interrogative does not assert the human's answer)`. **Grade: strong**.

#### B002 — distinguishing mark/sign

- **Initial image:** effects mark the path/cause; the knowledge question asks whether traces are understood before direct exposure.
- **V23:** `عدو=E:B002/B010 | ضبح=E:B001 | وري=E:B005 | قدح=E:B002 | غير=E:B003 | صبح=E:B005 | ثور=E:B001/B002 | نقع=E:B004 | وسط=Ø | جمع=Ø | ءنس=E:B002 | ربب=Ø | كند=Ø | شهد=E:B008 | حبب=Ø | خير=Ø | شدد=Ø | علم=S:B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ع ل م B002` plus backward `ع د و B002/B010 + ض ب ح B001 + و ر ي B005 + ق د ح B002 + غ ي ر B003 + ص ب ح B005 + ث و ر B001/B002 + ن ق ع B004 + ء ن س B002 + ش ه د B008`; freeze=audible/visible effects become route-marks to an unseen cause; P=contents themselves exposed, inner result/source, inward expertise. `ب ع ث ر B001 + ق ب ر B002 + ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` corroborate. `(K: يَعْلَمُ contextually uses cognition B001; opening effects are not named علامات)`. **Grade: strong as backward reactivation; medium-strong final due branch distance.**

#### B004 — upper-lip cleft

- **Initial image:** a visible bodily fissure functions as a mark.
- **V23:** `عدو=Ø | ضبح=F:B001 | وري=Ø | قدح=F:B002 | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=Ø | كند=Ø | شهد=F:B008 | حبب=F:B009 | خير=Ø | شدد=Ø | علم=S:B004 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ع ل م B004 + ء ن س B001`; freeze=human lip-mark; P=face/lip/wound. Breath, notch, witness-sign, and teeth forks use `ض ب ح B001 + ق د ح B002 + ش ه د B008 + ح ب ب B009`. `(K: imperfect cognition verb, no lip/body patient)`. **Grade: unlikely**.

#### B005 — large gathered water

- **Initial image:** abundant water forms a sea/well and supports storage/hydration.
- **V23:** `عدو=Ø | ضبح=Ø | وري=F:B004 | قدح=F:B006 | غير=E:B001 | صبح=F:B003 | ثور=F:B007 | نقع=E:B001/B002 | وسط=Ø | جمع=E:B012 | ءنس=Ø | ربب=E:B008/B013 | كند=Ø | شهد=Ø | حبب=E:B006/B007/B008 | خير=Ø | شدد=Ø | علم=S:B005 | بعثر=Ø | قبر=Ø | حصل=F:B004 | صدر=F:B003 | خبر=C:B002/B004`.
- **Lifecycle:** G=`ع ل م B005 + غ ي ر B001 + ن ق ع B001/B002 + ج م ع B012 + ر ب ب B008/B013 + ح ب ب B006/B007/B008`; freeze=large water/provision fills containers and supports growth; P=liquid/consumer/wet ground. `خ ب ر B002/B004` corroborates; fullness/cup/morning drink/algae/crop/departure forks explicit. `(K: يَعْلَمُ is cognition verb, no water)`. **Grade: unlikely**.

#### B006 — falcon/hawk

- **Initial image:** a bird of prey might fit rapid pursuit.
- **V23:** `عدو=F:B008 | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=S:B006 | بعثر=Ø | قبر=F:B003 | حصل=F:B004 | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ع ل م B006` only; hunting/bird/crop forks use `ع د و B008 + ق ب ر B003 + ح ص ل B004`. `(K: no bird, prey, flight, or hunting role)`. **Grade: unlikely**.

#### B007 — male hyena

- **Initial image:** a named animal might join hunting/burrow imagery.
- **V23:** `عدو=F:B008 | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=F:B006 | شدد=Ø | علم=S:B007 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ع ل م B007` only; hunting and burrow-extraction forks use `ع د و B008 + خ ي ر B006`. `(K: no hyena, burrow, or animal role)`. **Grade: unlikely**.

### 100:9:4 `بُعْثِرَ` — `ب ع ث ر`

#### B001 — earth overturned, buried contents exposed

- **Initial image:** the earlier disturbed surface deepens into overturned grave-earth and explicit exposure.
- **V23:** `عدو=E:B010 | ضبح=Ø | وري=E:B005 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B001/B002 | نقع=E:B004/B007 | وسط=E:B002/B003 | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=F:B001 | خير=F:B006 | شدد=E:B002/B003 | علم=C:B001/B002 | بعثر=S:B001 | قبر=E:B001/B002 | حصل=C:B001/B002/B003 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ب ع ث ر B001 + ع د و B010 + و ر ي B005 + غ ي ر B003 + ث و ر B001/B002 + ن ق ع B004/B007 + و س ط B002/B003 + ش د د B002/B003 + ق ب ر B001/B002`; freeze=surface disturbance and center-entry become deep earth inversion exposing buried contents; P=parallel inner enclosure, extraction/result/residue, inward source/knowledge. `ش ه د B008 + ع ل م B001/B002 + ح ص ل B001/B002/B003 + ص د ر B001/B004 + خ ب ر B001` corroborate. Seed/burrow forks use `ح ب ب B001 + خ ي ر B006`. `(K: passive agent unexpressed; ground layers are relational simulation)`. **Grade: strong**.

#### B002 — scattering/turning goods over

- **Initial image:** a gathered set is scattered and turned over, predicting counter-collection.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=F:B006 | جمع=E:B001/B009 | ءنس=Ø | ربب=F:B004 | كند=E:B001 | شهد=Ø | حبب=Ø | خير=Ø | شدد=F:B001 | علم=Ø | بعثر=S:B002 | قبر=E:B001 | حصل=C:B001/B002/B003 | صدر=C:B006 | خبر=C:B001`.
- **Lifecycle:** G=`ب ع ث ر B002 + غ ي ر B003 + ج م ع B001/B009 + ك ن د B001 + ق ب ر B001`; freeze=gathered/buried contents are severed, scattered, and turned over; P=collection/result/core/remainder. `ح ص ل B001/B002/B003 + ص د ر B006 + خ ب ر B001` corroborate. Bisection/multitude/knot forks use `و س ط B006 + ر ب ب B004 + ش د د B001`. `(K: opening جَمْعًا and grave contents are not the same object)`. **Grade: medium-strong**.

#### B003 — basin inverted bottom-to-top

- **Initial image:** a container is turned inside-out, reversing bottom/top and exposing depth.
- **V23:** `عدو=E:B004/B009 | ضبح=Ø | وري=E:B006 | قدح=E:B005 | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=E:B001 | وسط=E:B002/B003 | جمع=E:B012 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=E:B007 | خير=Ø | شدد=Ø | علم=Ø | بعثر=S:B003 | قبر=E:B002 | حصل=C:B002/B003 | صدر=C:B001/B002 | خبر=C:B001`.
- **Lifecycle:** G=`ب ع ث ر B003 + ع د و B004/B009 + و ر ي B006 + ق د ح B005 + غ ي ر B003 + ن ق ع B001 + و س ط B002/B003 + ج م ع B012 + ح ب ب B007 + ق ب ر B002`; freeze=edge/center/depth container is inverted; P=core/residue extraction, front/chest reversal, inner knowledge. `ح ص ل B002/B003 + ص د ر B001/B002 + خ ب ر B001` corroborate. `(K: no basin or literal bottom/top; contextual object is what lies in graves)`. **Grade: medium-strong**.

### 100:9:7 `ٱلْقُبُورِ` — `ق ب ر`

#### B001 — burial enclosure

- **Initial image:** covered dead contents lie in graves until earth is overturned.
- **V23:** `عدو=F:B010 | ضبح=Ø | وري=E:B005 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B001/B002 | نقع=E:B004/B007 | وسط=E:B002 | جمع=Ø | ءنس=E:B001 | ربب=Ø | كند=Ø | شهد=Ø | حبب=F:B001 | خير=Ø | شدد=Ø | علم=Ø | بعثر=E:B001 | قبر=S:B001 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ق ب ر B001 + و ر ي B005 + غ ي ر B003 + ث و ر B001/B002 + ن ق ع B004/B007 + و س ط B002 + ء ن س B001 + ب ع ث ر B001`; freeze=ground/covering conceals human contents then is disturbed/opened; P=parallel inner container, extraction/result, inward source/knowledge. `ح ص ل B001/B002 + ص د ر B001/B004 + خ ب ر B001` corroborate. Hard ground/seed forks use `ع د و B010 + ح ب ب B001`. `(K: relative مَا is passive subject; no explicit named dead-person noun)`. **Grade: strong**.

#### B002 — recessed obscurity/enclosure

- **Initial image:** something lies deep, obscure, and enclosed; center/depth geometry becomes primary.
- **V23:** `عدو=E:B004/B009 | ضبح=Ø | وري=E:B005/B006 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B001 | نقع=E:B007 | وسط=E:B002/B003 | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=E:B004/B007 | خير=F:B006 | شدد=Ø | علم=Ø | بعثر=E:B001/B003 | قبر=S:B002 | حصل=C:B001/B002 | صدر=C:B001/B002/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ق ب ر B002 + ع د و B004/B009 + و ر ي B005/B006 + غ ي ر B003 + ث و ر B001 + ن ق ع B007 + و س ط B002/B003 + ح ب ب B004/B007 + ب ع ث ر B001/B003`; freeze=movement reaches a concealed recessed center and turns it outward; P=parallel chest, core/result extraction, front/source, inner knowledge. `ح ص ل B001/B002 + ص د ر B001/B002/B004 + خ ب ر B001` corroborate. Burrow `خ ي ر B006` forks. `(K: contextual plural denotes graves; other recesses secondary)`. **Grade: strong**.

#### B003 — bird name

- **Initial image:** a lark-like bird.
- **V23:** `عدو=F:B008 | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=F:B006 | بعثر=Ø | قبر=S:B003 | حصل=F:B004 | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ق ب ر B003` only; hunting/falcon/bird-crop forks use `ع د و B008 + ع ل م B006 + ح ص ل B004`. `(K: definite plural قُبُورِ under فِى selects graves, not bird form)`. **Grade: unlikely**.

#### B004 — nose-tip sign of anger

- **Initial image:** a bodily gesture visibly signals anger.
- **V23:** `عدو=F:B003 | ضبح=Ø | وري=Ø | قدح=Ø | غير=F:B004 | صبح=Ø | ثور=E:B003 | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=Ø | كند=Ø | شهد=E:B008 | حبب=Ø | خير=Ø | شدد=Ø | علم=E:B002 | بعثر=Ø | قبر=S:B004 | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=`ق ب ر B004 + ث و ر B003 + ء ن س B001 + ش ه د B008 + ع ل م B002`; freeze=anger produces a visible facial sign; P=angry person/face. Enemy/jealousy forks use `ع د و B003 + غ ي ر B004`. `(K: no nose, face, or anger; قُبُورِ is plural graves)`. **Grade: unlikely**.

### 100:10:1 `وَحُصِّلَ` — `ح ص ل`

#### B001 — gathering until result appears

- **Initial image:** scattered/hidden material is collected into a stable outcome; this answers earlier gathering and overturning.
- **V23:** `عدو=Ø | ضبح=Ø | وري=E:B005 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B001 | نقع=Ø | وسط=Ø | جمع=E:B001/B009 | ءنس=E:B001 | ربب=E:B001 | كند=E:B001/B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001 | شدد=Ø | علم=E:B001 | بعثر=E:B002 | قبر=E:B002 | حصل=S:B001 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ح ص ل B001` plus backward `و ر ي B005 + غ ي ر B003 + ث و ر B001 + ج م ع B001/B009 + ء ن س B001 + ر ب ب B001 + ك ن د B001/B002 + ش ه د B002 + ح ب ب B002 + خ ي ر B001 + ع ل م B001 + ب ع ث ر B002 + ق ب ر B002`; freeze=scattered/hidden human-related material is gathered as a result; P=explicit inward container/source and informed relational knower. `ص د ر B001/B004 + خ ب ر B001` and final `رَبَّهُم بِهِمْ` corroborate. `(K: objects across gather/scatter stages differ; passive agent unexpressed)`. **Grade: strong**.

#### B002 — extracting core/precious material from casing

- **Initial image:** a casing or matrix yields its inner core; grave and chest form two levels of enclosure.
- **V23:** `عدو=E:B004 | ضبح=F:B003/B005 | وري=E:B005/B006 | قدح=F:B005 | غير=E:B003 | صبح=Ø | ثور=E:B001/B002 | نقع=Ø | وسط=E:B002/B003 | جمع=Ø | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=E:B007 | حبب=E:B004/B007 | خير=E:B001 | شدد=E:B002 | علم=E:B001 | بعثر=E:B001/B003 | قبر=E:B001/B002 | حصل=S:B002 | صدر=C:B001/B002/B004 | خبر=C:B001`.
- **Lifecycle:** G=`ح ص ل B002 + ع د و B004 + و ر ي B005/B006 + غ ي ر B003 + ث و ر B001/B002 + و س ط B002/B003 + ء ن س B001 + ر ب ب B001 + ك ن د B002 + ش ه د B007 + ح ب ب B004/B007 + خ ي ر B001 + ش د د B002 + ع ل م B001 + ب ع ث ر B001/B003 + ق ب ر B001/B002`; freeze=successive coverings are crossed/inverted so valuable inward content is extracted from human-related enclosures; P=chest/source and inner knowledge. `ص د ر B001/B002/B004 + خ ب ر B001` corroborate. Fire/ash/pot refining forks use `ض ب ح B003/B005 + ق د ح B005`. `(K: contents are not called metal, honey, or treasure)`. **Grade: strong**.

#### B003 — residue after separation

- **Initial image:** separation leaves residue after a valuable or usable part is removed.
- **V23:** `عدو=E:B011 | ضبح=E:B005 | وري=Ø | قدح=E:B009 | غير=E:B001 | صبح=Ø | ثور=E:B002 | نقع=E:B007 | وسط=Ø | جمع=E:B001 | ءنس=Ø | ربب=E:B002/B012 | كند=E:B003 | شهد=Ø | حبب=E:B001 | خير=E:B001 | شدد=Ø | علم=Ø | بعثر=E:B001/B002 | قبر=E:B002 | حصل=S:B003 | صدر=Ø | خبر=C:B003,C:B001`.
- **Lifecycle:** agricultural G=`ح ص ل B003 + ع د و B011 + ق د ح B009 + غ ي ر B001 + ث و ر B002 + ن ق ع B007 + ج م ع B001 + ر ب ب B002/B012 + ك ن د B003 + ح ب ب B001 + خ ي ر B001 + ب ع ث ر B001/B002 + ق ب ر B002`; freeze=earth is turned and yield separated from chaff/residue; P=cultivator/evaluator. `خ ب ر B003` corroborates while `خ ب ر B001` controls final context. Fire-residue fork adds `ض ب ح B005`. `(K: no grain, threshing, or ash; contextual passive concerns chest contents)`. **Grade: medium-strong**.

#### B004 — bird crop / bodily food store

- **Initial image:** food collects in an animal's internal pouch.
- **V23:** `عدو=Ø | ضبح=Ø | وري=F:B004 | قدح=F:B005/B006 | غير=F:B001 | صبح=F:B003 | ثور=Ø | نقع=F:B003 | وسط=Ø | جمع=E:B001/B012 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=F:B006/B007 | خير=Ø | شدد=Ø | علم=F:B006 | بعثر=Ø | قبر=Ø | حصل=S:B004 | صدر=E:B001 | خبر=F:B005`.
- **Lifecycle:** G=`ح ص ل B004 + ج م ع B001/B012 + ص د ر B001`; freeze=food is gathered in a bodily interior; P=bird, food, ingestion. Fullness/pot/cup/provision/meal/jar/falcon/soft animal forks explicit. `(K: no bird, crop, food, or consumption; حُصِّلَ is passive Form II)`. **Grade: unlikely**.

#### B005 — unripe dates before hardening

- **Initial image:** fruit emerges before maturity/hardness.
- **V23:** `عدو=E:B011 | ضبح=Ø | وري=Ø | قدح=E:B009 | غير=E:B001 | صبح=Ø | ثور=E:B001 | نقع=E:B002/B007 | وسط=Ø | جمع=E:B011 | ءنس=Ø | ربب=E:B002/B012 | كند=E:B003 | شهد=Ø | حبب=E:B001 | خير=E:B001 | شدد=E:B004 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=S:B005 | صدر=Ø | خبر=C:B003/B005`.
- **Lifecycle:** G=`ح ص ل B005 + ع د و B011 + ق د ح B009 + غ ي ر B001 + ث و ر B001 + ن ق ع B002/B007 + ج م ع B011 + ر ب ب B002/B012 + ك ن د B003 + ح ب ب B001 + خ ي ر B001 + ش د د B004`; freeze=seed/plant matures or fails under nurture; P=cultivator/plant quality. `خ ب ر B003/B005` corroborates. `(K: no dates, palms, fruit, or maturity; contextual passive extraction dominates)`. **Grade: weak**.

#### B006 — horse abdominal pain from soil

- **Initial image:** a running animal ingests earth/dust and suffers internally.
- **V23:** `عدو=E:B002 | ضبح=E:B001/B002 | وري=E:B001 | قدح=E:B008 | غير=Ø | صبح=Ø | ثور=E:B002 | نقع=E:B004/B007 | وسط=Ø | جمع=E:B010 | ءنس=F:B004 | ربب=F:B014 | كند=Ø | شهد=Ø | حبب=E:B005 | خير=Ø | شدد=E:B003 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=S:B006 | صدر=E:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ح ص ل B006 + ع د و B002 + ض ب ح B001/B002 + و ر ي B001 + ق د ح B008 + ث و ر B002 + ن ق ع B004/B007 + ج م ع B010 + ح ب ب B005 + ش د د B003 + ص د ر B001`; freeze=running animal's dust exposure becomes internal illness/stopping; P=horse, ingestion, pain. `خ ب ر B001` only supplies knowledge; rider/herd forks use `ء ن س B004 + ر ب ب B014`. `(K: no horse, eating, abdominal pain, or stop; passive morphology controls)`. **Grade: weak**.

### 100:10:4 `ٱلصُّدُورِ` — `ص د ر`

#### B001 — bodily chest/interior

- **Initial image:** the second enclosure is a human bodily interior whose contents are extracted.
- **V23:** `عدو=E:B004 | ضبح=F:B001 | وري=E:B001/B005 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B001 | نقع=Ø | وسط=E:B002/B003 | جمع=Ø | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=E:B001/B002 | حبب=E:B002/B004 | خير=E:B001 | شدد=E:B002 | علم=E:B001 | بعثر=E:B001/B003 | قبر=E:B002 | حصل=E:B001/B002 | صدر=S:B001 | خبر=C:B001`.
- **Lifecycle:** G=`ص د ر B001 + ع د و B004 + و ر ي B001/B005 + غ ي ر B003 + ث و ر B001 + و س ط B002/B003 + ء ن س B001 + ر ب ب B001 + ك ن د B002 + ش ه د B001/B002 + ح ب ب B002/B004 + خ ي ر B001 + ش د د B002 + ع ل م B001 + ب ع ث ر B001/B003 + ق ب ر B002 + ح ص ل B001/B002`; freeze=human relational orientation lies in a concealed central chest and is extracted after outer enclosure inversion; P=inward expertise tied to persons. `خ ب ر B001 + بِهِمْ` corroborate. Breath/lung fork `ض ب ح B001 + و ر ي B001` remains secondary. `(K: contents unspecified; no named heart)`. **Grade: strong**.

#### B002 — front/foremost/upper part

- **Initial image:** front/back and edge/center orientation is reversed by opening and extraction.
- **V23:** `عدو=E:B004/B009 | ضبح=Ø | وري=E:B006 | قدح=F:B007 | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=E:B007 | وسط=E:B002/B003 | جمع=Ø | ءنس=F:B004 | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=E:B003 | قبر=E:B002 | حصل=E:B002 | صدر=S:B002 | خبر=C:B001`.
- **Lifecycle:** G=`ص د ر B002 + ع د و B004/B009 + و ر ي B006 + غ ي ر B003 + ن ق ع B007 + و س ط B002/B003 + ب ع ث ر B003 + ق ب ر B002 + ح ص ل B002`; freeze=front/edge crosses center, container turns bottom/top, and interior comes outward; P=knower of whole orientation. `خ ب ر B001` corroborates. Arrow/mount fork uses `ق د ح B007 + ء ن س B004`. `(K: صُدُورِ under فِى contextually means chests, not fronts)`. **Grade: medium-strong**.

#### B003 — departure after reaching a source

- **Initial image:** arrival at water is followed by departure/return.
- **V23:** `عدو=E:B002 | ضبح=Ø | وري=E:B006 | قدح=E:B006 | غير=E:B001 | صبح=E:B002/B003 | ثور=Ø | نقع=E:B001/B002/B008 | وسط=E:B003 | جمع=E:B002 | ءنس=Ø | ربب=E:B013 | كند=Ø | شهد=Ø | حبب=E:B006 | خير=Ø | شدد=Ø | علم=E:B005 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=S:B003 | خبر=C:B002/B004`.
- **Lifecycle:** G=`ص د ر B003 + ع د و B002 + و ر ي B006 + ق د ح B006 + غ ي ر B001 + ص ب ح B002/B003 + ن ق ع B001/B002/B008 + و س ط B003 + ج م ع B002 + ر ب ب B013 + ح ب ب B006 + ع ل م B005`; freeze=travelers arrive at water, fill, then depart by known routes; P=source, travelers, return. `خ ب ر B002/B004` corroborates watery land/abundance. `(K: no water/travel/departure; فِى ٱلصُّدُورِ is containment)`. **Grade: unlikely**.

#### B004 — inward source from which actions issue

- **Initial image:** an inner source generates outward orientation/action and is finally extracted.
- **V23:** `عدو=F:B007 | ضبح=F:B001 | وري=E:B005 | قدح=E:B010 | غير=E:B003 | صبح=Ø | ثور=E:B001 | نقع=F:B005 | وسط=Ø | جمع=E:B003 | ءنس=E:B006 | ربب=E:B001 | كند=E:B002 | شهد=E:B002/B005 | حبب=E:B002 | خير=E:B001/B003 | شدد=E:B002 | علم=E:B001 | بعثر=Ø | قبر=Ø | حصل=E:B001 | صدر=S:B004 | خبر=C:B001`.
- **Lifecycle:** G=`ص د ر B004 + و ر ي B005 + ق د ح B010 + غ ي ر B003 + ث و ر B001 + ج م ع B003 + ء ن س B006 + ر ب ب B001 + ك ن د B002 + ش ه د B002/B005 + ح ب ب B002 + خ ي ر B001/B003 + ش د د B002 + ع ل م B001 + ح ص ل B001`; freeze=hidden inner source gathers intention/value, issues relational behavior, testifies through expression, and is collected as result; P=final inward knower. `خ ب ر B001 + رَبَّهُم بِهِمْ` corroborate. Distraction/breath/sound forks explicit. `(K: passage does not state a causal psychology tying opening actions to chest contents)`. **Grade: strong**.

#### B005 — confiscation/seizure of property

- **Initial image:** valued property is forcibly rendered/seized; love, withholding, and extraction can form an economic-accounting image.
- **V23:** `عدو=F:B005 | ضبح=Ø | وري=Ø | قدح=Ø | غير=F:B002 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=F:B005 | جمع=Ø | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B005 | شدد=E:B006 | علم=E:B001 | بعثر=Ø | قبر=Ø | حصل=E:B001/B002 | صدر=S:B005 | خبر=C:B001`.
- **Lifecycle:** G=`ص د ر B005 + ء ن س B001 + ر ب ب B001 + ك ن د B002 + ش ه د B002 + ح ب ب B002 + خ ي ر B005 + ش د د B006 + ع ل م B001 + ح ص ل B001/B002`; freeze=human loves/withholds gift/property, which is forcibly rendered/extracted under knowledge; P=authority, transfer, account. `خ ب ر B001` corroborates informed assessment. Redress/compensation/mediation forks use `ع د و B005 + غ ي ر B002 + و س ط B005`. `(K: no property, seizure, payer, or transfer attachment)`. **Grade: medium** — a fuller economic image, but missing transaction roles.

#### B006 — portion/part

- **Initial image:** a portion is separated from a whole and recovered as part of an account.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=E:B006 | جمع=E:B001/B009 | ءنس=Ø | ربب=Ø | كند=E:B001 | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=E:B002 | قبر=Ø | حصل=E:B001/B002 | صدر=S:B006 | خبر=C:B001/F:B006`.
- **Lifecycle:** G=`ص د ر B006 + غ ي ر B003 + و س ط B006 + ج م ع B001/B009 + ك ن د B001 + ب ع ث ر B002 + ح ص ل B001/B002`; freeze=whole is divided/scattered and a part/result recovered; P=comprehensive knower or division. `خ ب ر B001` corroborates knowledge; meat-share `خ ب ر B006` forks. `(K: no partitive expression or quantified portion)`. **Grade: medium**.

### 100:11:5 `لَخَبِيرٌ` — `خ ب ر`

#### B001 — knowledge of reports and inward reality

- **Initial image:** the final predicate knows the persons' inward reality after sound, signs, testimony, cognition, and disclosure.
- **V23:** `عدو=E:B002/B004/B010 | ضبح=E:B001 | وري=E:B005 | قدح=E:B002 | غير=E:B003 | صبح=E:B005 | ثور=E:B001/B002 | نقع=E:B004/B005 | وسط=E:B002/B003 | جمع=E:B001 | ءنس=E:B001/B002 | ربب=E:B001/B003 | كند=E:B001/B002 | شهد=E:B001/B002/B005/B008 | حبب=E:B002/B004 | خير=E:B001 | شدد=E:B001/B002 | علم=E:B001/B002 | بعثر=E:B001/B002/B003 | قبر=E:B001/B002 | حصل=E:B001/B002 | صدر=E:B001/B004 | خبر=S:B001`.
- **Lifecycle:** G=`خ ب ر B001` plus full backward replay of selected disclosure, geometry, relation, and epistemic trajectories shown in V23; freeze=the رب is inwardly informed concerning the human plurality after hidden external and internal contents have become accessible; P=none—knower, object-reference, time, relation, and inner matter are complete. Post-freeze tests `(C: intensive adjective morphology)`, `(C: بِهِمْ prep attachment)`, `(C: يَوْمَئِذٍ adverbial attachment)`, `(C: final إِنَّ...لَ predication)`, and `(C: delayed ر ب ب recurrence)` all strengthen closure. `(K: no court procedure and no inference of the passive agent)`. **Grade: strong** — independently explains maximal backward reactivation and stopping.

#### B002 — soft/low wet land

- **Initial image:** low soft earth gathers water and vegetation, offering an agriculture/hydration close.
- **V23:** `عدو=E:B011 | ضبح=Ø | وري=Ø | قدح=E:B009 | غير=E:B001 | صبح=Ø | ثور=E:B002/B007 | نقع=E:B001/B002/B007 | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=E:B008/B012/B013 | كند=E:B003 | شهد=Ø | حبب=E:B001/B008 | خير=E:B001 | شدد=Ø | علم=E:B005 | بعثر=E:B001 | قبر=E:B002 | حصل=E:B002/B003/B005 | صدر=Ø | خبر=S:B002,K:B001`.
- **Lifecycle:** G=`خ ب ر B002 + ع د و B011 + ق د ح B009 + غ ي ر B001 + ث و ر B002/B007 + ن ق ع B001/B002/B007 + ر ب ب B008/B012/B013 + ك ن د B003 + ح ب ب B001/B008 + خ ي ر B001 + ع ل م B005 + ب ع ث ر B001 + ق ب ر B002 + ح ص ل B002/B003/B005`; freeze=wet/soft land is nurtured, seeded, turned, and harvested against barrenness; P=none beyond soil role. `(K: خَبِيرٌ is an intensive adjective attached to persons; B001 knowledge and final syntax defeat terrain)`. **Grade: medium as remote convergence, weak final; final weak.**

#### B003 — cultivator/sharecropping

- **Initial image:** a cultivator repairs land and assesses its share/yield.
- **V23:** `عدو=E:B011 | ضبح=Ø | وري=Ø | قدح=E:B009 | غير=E:B001 | صبح=Ø | ثور=E:B002 | نقع=E:B002/B007 | وسط=Ø | جمع=E:B001/B011 | ءنس=E:B001 | ربب=E:B002/B012 | كند=E:B003 | شهد=E:B002 | حبب=E:B001 | خير=E:B001/B005 | شدد=Ø | علم=E:B001 | بعثر=E:B001 | قبر=E:B001/B002 | حصل=E:B001/B002/B003/B005 | صدر=E:B004 | خبر=S:B003,K:B001`.
- **Lifecycle:** G=`خ ب ر B003` plus the full already-active cultivation/yield vector; freeze=the human is secondarily modeled as ground whose response to nurture is turned up, separated, and assessed by a cultivator/owner; P=none. `ش ه د B002 + ع ل م B001 + ص د ر B004` make the yield an inward human account. `(K: no land contract/share; contextual خ ب ر B001 and person attachment control)`. **Grade: medium** — strongest remote agricultural closure, explicitly subordinate.

#### B004 — abundant waterskin/camel

- **Initial image:** a large container or animal holds abundance.
- **V23:** `عدو=F:B002 | ضبح=F:B001/B002 | وري=E:B004 | قدح=E:B006 | غير=E:B001 | صبح=F:B003 | ثور=Ø | نقع=E:B001/B002 | وسط=Ø | جمع=E:B012 | ءنس=Ø | ربب=E:B013/B014 | كند=Ø | شهد=Ø | حبب=E:B006/B007 | خير=Ø | شدد=Ø | علم=E:B005 | بعثر=Ø | قبر=Ø | حصل=E:B004 | صدر=Ø | خبر=S:B004,K:B001`.
- **Lifecycle:** G=`خ ب ر B004 + و ر ي B004 + ق د ح B006 + غ ي ر B001 + ن ق ع B001/B002 + ج م ع B012 + ر ب ب B013/B014 + ح ب ب B006/B007 + ع ل م B005 + ح ص ل B004`; freeze=abundant liquid/food fills vessel or animal; P=none. Running/panting/morning drink forks explicit. `(K: final adjective concerns persons through بِهِمْ and contextual inner knowledge; no abundance container)`. **Grade: unlikely**.

#### B005 — softness in plant/hair/foam

- **Initial image:** soft growth or animal surface appears after water/nurture.
- **V23:** `عدو=E:B011 | ضبح=Ø | وري=F:B004 | قدح=E:B009 | غير=E:B001 | صبح=Ø | ثور=F:B007 | نقع=E:B001/B002/B007 | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=E:B008/B012 | كند=E:B003 | شهد=Ø | حبب=E:B001/B008 | خير=E:B001 | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=E:B005 | صدر=Ø | خبر=S:B005,K:B001`.
- **Lifecycle:** G=`خ ب ر B005 + ع د و B011 + ق د ح B009 + غ ي ر B001 + ن ق ع B001/B002/B007 + ر ب ب B008/B012 + ك ن د B003 + ح ب ب B001/B008 + خ ي ر B001 + ح ص ل B005`; freeze=soft vegetation grows under water/nurture or fails in barren soil; P=none. Fat/foam/algae forks use `و ر ي B004 + ث و ر B007`. `(K: no plant, hair, foam, or animal surface; B001 knowledge controls)`. **Grade: unlikely**.

#### B006 — shared animal/meat portion

- **Initial image:** a group divides an animal/food into shares.
- **V23:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=F:B002 | صبح=Ø | ثور=Ø | نقع=F:B003 | وسط=F:B005 | جمع=E:B002/B013 | ءنس=E:B001 | ربب=F:B014 | كند=Ø | شهد=F:B002 | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=F:B004 | صدر=E:B006 | خبر=S:B006,K:B001`.
- **Lifecycle:** G=`خ ب ر B006 + ج م ع B002/B013 + ء ن س B001 + ص د ر B006`; freeze=human group divides a portion; P=animal, slaughter, meat, shares. Compensation/meal/mediation/herd/testimony/bird-crop forks explicit. `(K: no animal, meat, division, or sharing; final predicate is inner knowledge)`. **Grade: unlikely**.

## Constructional seed traversal

Construction vectors use the same 23-root order and symbols as lexical vectors; the construction itself is the seed and selected lexical branches are `E/C/F/K`.

### C01 — oath `وَٱلْعَادِيَاتِ`

- **Initial image:** an oath-governed opening scene is held active until its proposition arrives.
- **V23-C:** `عدو=E:B002 | ضبح=E:B001 | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=E:B001 | ثور=E:B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B001 | ءنس=C:B001 | ربب=C:B001 | كند=C:B002 | شهد=C:B002 | حبب=C:B002 | خير=C:B001 | شدد=C:B002 | علم=C:B001 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=oath construction + opening kinetic roots through `ج م ع`; freeze at 100:5=a pledged action/effect/entry sequence awaits its asserted relevance; P=emphatic proposition and later closure that can replay motion, interior, or evidence. All later selected roots independently furnish human diagnosis, witness, motive, disclosure, and knowledge. `(K: oath syntax alone does not specify analogy or identity)`. **Grade: strong**.

### C02 — `ٱلْعَادِيَاتِ ضَبْحًا`

- **Initial image:** active feminine-plural running is specified by an accusative manner of breath/sound.
- **V23-C:** `عدو=E:B002 | ضبح=E:B001/B002 | وري=C:B002 | قدح=C:B001 | غير=Ø | صبح=Ø | ثور=C:B002 | نقع=C:B004/B005 | وسط=C:B003 | جمع=C:B010 | ءنس=C:B002 | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=Ø | خير=Ø | شدد=C:B003 | علم=C:B002 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=C:B001`.
- **Lifecycle:** G=construction + `ع د و B002 + ض ب ح B001/B002`; freeze=audible exertive motion; P=effects, parallel manner, later perception/force. Fire/impact, dust, center-entry, gathered force, perception/sign, and final knowledge corroborate; raised-sound B005 is a secondary fork. `(K: no species)`. **Grade: strong locally, medium-strong passage-wide**.

### C03 — `فَٱلْمُورِيَاتِ قَدْحًا`

- **Initial image:** a second feminine-plural participle is specified by fire-striking manner.
- **V23-C:** `عدو=E:B010 | ضبح=E:B003 | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=Ø | ثور=C:B001/B002 | نقع=C:B004 | وسط=Ø | جمع=C:B010 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=C:B011 | خير=C:B001 | شدد=C:B002/B003 | علم=C:B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002/B003 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=construction + `و ر ي B002 + ق د ح B001 + ع د و B010 + ض ب ح B003 + غ ي ر B003`; freeze=impact releases hidden fire and alters matter; P=visible effects, delayed spark/force replay, deeper hidden-to-open sequence. Unused selected roots fulfill all predictions. `(K: no literal fire transfer into love/chest clauses)`. **Grade: strong**.

### C04 — `فَٱلْمُغِيرَاتِ صُبْحًا`

- **Initial image:** the third active-participle unit adds a dawn time boundary before finite effects.
- **V23-C:** `عدو=E:B002 | ضبح=E:B002 | وري=Ø | قدح=Ø | غير=E:B003 | صبح=E:B001/B004 | ثور=C:B002 | نقع=C:B004 | وسط=C:B003 | جمع=C:B002 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=C:B003/B005 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=C:B001`.
- **Lifecycle:** G=construction + running/change/dawn branches; freeze=a time-marked charge/transition; P=effects, entry, later charge, later time marker. Dust/entry/group, `ش د د B003/B005`, and final knowledge at `يَوْمَئِذٍ` corroborate. `(K: no explicit combat roles; dawn not identical to final day)`. **Grade: medium-strong**.

### C05 — `فَأَثَرْنَ بِهِ نَقْعًا`

- **Initial image:** a 3FP perfect action, with pronominal means/complement, raises a direct object.
- **V23-C:** `عدو=E:B002/B010 | ضبح=Ø | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=Ø | ثور=E:B001/B002 | نقع=E:B004 | وسط=C:B003 | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=C:B011 | خير=Ø | شدد=C:B002 | علم=C:B002 | بعثر=C:B001 | قبر=C:B001/B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=attachment construction + kinetic/ignition/dislodging/dust branches; freeze=earlier force produces a visible ground effect; P=effect carried into entry, trace, and later deeper earth/interior disturbance. Repeated `بِهِ`, witness-sign, spark/intensity, grave-earth opening, chest extraction, and knowledge corroborate. `(K: singular pronoun antecedent remains lexically unresolved)`. **Grade: strong**.

### C06 — `فَوَسَطْنَ بِهِ جَمْعًا`

- **Initial image:** the same 3FP actors enter a direct object through/with the repeated pronominal complement.
- **V23-C:** `عدو=E:B004 | ضبح=Ø | وري=E:B006 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=Ø | نقع=E:B004 | وسط=E:B002/B003 | جمع=E:B001/B002 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=C:B004 | خير=Ø | شدد=C:B003 | علم=Ø | بعثر=C:B001/B003 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001/B002 | خبر=C:B001`.
- **Lifecycle:** G=construction + boundary/other-side/change/dust/center/gather branches; freeze=outside force reaches a gathered center; P=explicit deeper containment and inside→outside reversal. Heart-core, force, paired interiors, inversion, extraction, and knowledge corroborate. `(K: no coreference between objects)`. **Grade: strong**.

### C07 — repeated `بِهِ...بِهِ`

- **Initial image:** one unresolved singular reference/means links effect-production to center-entry.
- **V23-C:** `عدو=E:B002 | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=E:B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B002 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=C:B001`.
- **Lifecycle:** G=repeated attachment + motion/dislodged dust/entry/group; freeze=the means/effect of one event remains active into the next; P=a later `بـ` echo. `بِهِمْ` before `خَبِيرٌ` acoustically/structurally reactivates `بـ`, but `(K: plural human reference, different governor, no coreference)`. **Grade: medium**.

### C08 — complete 100:1–5 kinetic block

- **Initial image:** participial capacities become finite effects and culminate in center-entry.
- **V23-C:** `عدو=E:B002/B004/B010 | ضبح=E:B001/B002 | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=E:B001 | ثور=E:B001/B002 | نقع=E:B004 | وسط=E:B002/B003 | جمع=E:B001/B010 | ءنس=C:B001 | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=C:B011 | خير=Ø | شدد=C:B002/B003 | علم=C:B002 | بعثر=C:B001/B003 | قبر=C:B001/B002 | حصل=C:B002 | صدر=C:B001/B002 | خبر=C:B001`.
- **Lifecycle:** G=all opening constructions + selected opening branches; freeze=surface force releases hidden effects and crosses into a center; P=human scale pivot, late force/spark, deep enclosure inversion/extraction, knowledge. Every selected late dossier fills one predicted role. `(K: does not itself predict the specific relational content of 100:6–8)`. **Grade: strong**.

### C09 — `إِنَّ ٱلْإِنسَانَ...لَكَنُودٌ`

- **Initial image:** emphatic nominal diagnosis abruptly replaces the kinetic block.
- **V23-C:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B005 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=E:B001/B002 | كند=E:B001/B002 | شهد=C:B002 | حبب=C:B002 | خير=C:B001 | شدد=C:B001/B002 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=إنّ/اسم/خبر/emphasis construction + human/contrast/رب/denial branches; freeze=generic human is emphatically diagnosed relative to رب; P=supporting witness, motive, inward result, final knowledge. All selected later roots corroborate. `(K: no lexical identity with opening agents)`. **Grade: strong**.

### C10 — `لِرَبِّهِ لَكَنُودٌ`

- **Initial image:** `لِرَبِّهِ` is the target with respect to which the diagnosis holds.
- **V23-C:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B001 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=E:B001/B002/B011 | كند=E:B001/B002 | شهد=C:B002 | حبب=C:B002 | خير=C:B001/B005 | شدد=C:B001/B002 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=prep-complement/possessive construction + human, owner/nurturer/covenant, cut/ingratitude; freeze=first relational axis; P=competing `لِـ` axis, witness, result/source, return and knowledge. All selected later roots fulfill. `(K: no contract/debt or specific gift)`. **Grade: strong**.

### C11 — `وَإِنَّهُ عَلَىٰ ذَٰلِكَ لَشَهِيدٌ`

- **Initial image:** singular anaphora continues the human, while `عَلَىٰ ذَٰلِكَ` identifies the matter over which witness applies.
- **V23-C:** `عدو=Ø | ضبح=E:B001 | وري=E:B005 | قدح=E:B002 | غير=E:B003 | صبح=E:B005 | ثور=E:B001/B002 | نقع=E:B004 | وسط=Ø | جمع=Ø | ءنس=E:B002 | ربب=E:B001 | كند=E:B002 | شهد=E:B001/B002/B008 | حبب=Ø | خير=Ø | شدد=Ø | علم=C:B001/B002 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=anaphora/prep/predication construction + perception/trace/witness roots; freeze=the diagnosed subject is present as witness concerning that diagnosis; P=cognition, direct exposure, inward result/source, final knower. Selected closing roots fulfill. `(K: witness need not be visual/court testimony)`. **Grade: strong**.

### C12 — `وَإِنَّهُ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ`

- **Initial image:** singular anaphora continues; love is the complement of intensity and good is love's idafa complement.
- **V23-C:** `عدو=C:B007 | ضبح=Ø | وري=Ø | قدح=C:B010 | غير=C:B004 | صبح=Ø | ثور=Ø | نقع=C:B002 | وسط=Ø | جمع=C:B003 | ءنس=E:B001/B006 | ربب=E:B001 | كند=E:B001/B002 | شهد=C:B002 | حبب=E:B002,F:B001/B011 | خير=E:B001,F:B003/B005 | شدد=E:B001/B002,F:B003/B006 | علم=C:B001 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=anaphora/prep/idafa/predication construction + human/رب/cut-love-good-intensity branches; freeze=second relational axis tightly/intensely opposes the first; P=cognition and inward disclosure. Closing roots corroborate. Seed, spark, choice, gift, charge, and miserliness forks are retained but `(K: exact attachments keep love/good/intensity primary)`. **Grade: strong**.

### C13 — parallel `لِرَبِّهِ` / `لِحُبِّ ٱلْخَيْرِ`

- **Initial image:** the same preposition introduces two differently structured orientations of one human referent.
- **V23-C:** `عدو=F:B007 | ضبح=Ø | وري=Ø | قدح=F:B010 | غير=E:B001 | صبح=Ø | ثور=Ø | نقع=F:B002 | وسط=Ø | جمع=F:B003/B013 | ءنس=E:B001/B006 | ربب=E:B001/B002/B011 | كند=E:B001/B002 | شهد=C:B002 | حبب=E:B002 | خير=E:B001/B005 | شدد=E:B001/B002/B006 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=parallel attachment construction + relational roots; freeze=one axis is cut/denied, the other tightened/intensified; P=witness, cognition, inner record/source, first-axis return, knowledge. All selected closing roots fulfill. Distraction/planning/self-settling/resolve/alliance are rival mechanisms, not required. `(K: the two لِـ attachments have different local governors)`. **Grade: strong**.

### C14 — repeated `وَإِنَّهُ` at 100:7–8

- **Initial image:** exact anaphoric repetition keeps one singular human active while two supporting predicates accumulate.
- **V23-C:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B002 | علم=C:B001 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=repetition + human/diagnosis/witness/motive roots; freeze=one referent carries denial, witness, and intense attachment; P=question about his knowing and disclosure of inward content. `ع ل م B001` and closing disclosure roots fulfill. `(K: no change of referent is licensed)`. **Grade: strong**.

### C15 — `عَلَىٰ ذَٰلِكَ` demonstrative backlink

- **Initial image:** `ذَٰلِكَ` points backward, reactivating the immediately preceding human diagnosis as witness-content.
- **V23-C:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=E:B001/B002 | حبب=Ø | خير=Ø | شدد=Ø | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001 | صدر=C:B004 | خبر=C:B001`.
- **Lifecycle:** G=demonstrative/prep attachment + human/رب/ingratitude/witness; freeze=earlier diagnosis is reactivated as the matter witnessed; P=cognition and inward evidentiary result. `ع ل م B001 + ح ص ل B001 + ص د ر B004 + خ ب ر B001` corroborate. `(K: demonstrative scope does not add lexical content)`. **Grade: strong**.

### C16 — idafa `حُبِّ ٱلْخَيْرِ`

- **Initial image:** love contains/directs itself toward good; remote seed/value/gift branches remain subordinate alternatives.
- **V23-C:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B001 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001/B006 | ربب=E:B001/B002 | كند=E:B002 | شهد=C:B002 | حبب=E:B002,F:B001/B004/B011 | خير=E:B001,F:B003/B005 | شدد=E:B002 | علم=C:B001 | بعثر=Ø | قبر=Ø | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=idafa + contextual love/good and relational comparison; freeze=benefit-directed inward attachment; P=witness, knowledge, chest/source/result, final knower. Closing roots fulfill. Seed/heart-core/spark/choice/gift forks add geometry or reactivation but `(K: cannot replace the idafa's contextual relation)`. **Grade: strong**.

### C17 — `أَفَلَا يَعْلَمُ`

- **Initial image:** interrogative, consequential particle, and negation challenge the singular subject's cognition after witness/intensity.
- **V23-C:** `عدو=Ø | ضبح=E:B001 | وري=E:B005 | قدح=Ø | غير=E:B003 | صبح=E:B005 | ثور=E:B001 | نقع=E:B004/B005 | وسط=Ø | جمع=Ø | ءنس=E:B002 | ربب=E:B003 | كند=E:B002 | شهد=E:B001/B002/B008 | حبب=E:B002 | خير=E:B001 | شدد=E:B002 | علم=E:B001 | بعثر=C:B001 | قبر=C:B001/B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=question construction + prior sensory/witness/relational state; freeze=the subject's self-witness is challenged as incomplete knowledge; P=direct exposure of hidden external/internal domains and superior inward knowledge. The next two ayahs and final predicate exactly fulfill. `(K: question does not assert his answer)`. **Grade: strong**.

### C18 — temporal setting `إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ`

- **Initial image:** the cognition question is temporally conditioned by passive grave disclosure.
- **V23-C:** `عدو=E:B010 | ضبح=Ø | وري=E:B005 | قدح=Ø | غير=E:B003 | صبح=E:B001 | ثور=E:B001/B002 | نقع=E:B004/B007 | وسط=E:B002 | جمع=Ø | ءنس=E:B001 | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=E:B001 | بعثر=E:B001 | قبر=E:B001/B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=temporal-clause attachment + ground/concealment/emergence/grave branches; freeze=knowing is tested when covered earth yields hidden contents; P=parallel inner enclosure and extraction, final knowledge at marked time. `ح ص ل B002 + ص د ر B001 + خ ب ر B001` fulfill. `(K: passive agent unexpressed; dawn not equated with this time)`. **Grade: strong**.

### C19 — passive unit `بُعْثِرَ مَا فِى ٱلْقُبُورِ`

- **Initial image:** passive overturning has relative `مَا` as overt subject and a `فِى` grave-domain.
- **V23-C:** `عدو=E:B004/B010 | ضبح=Ø | وري=E:B005 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B001/B002 | نقع=E:B004/B007 | وسط=E:B002/B003 | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=F:B001 | خير=F:B006 | شدد=Ø | علم=Ø | بعثر=E:B001/B003 | قبر=E:B001/B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=passive/subject/prep construction + ground-depth/inversion branches; freeze=first hidden container is opened without expressed agent; P=parallel second container, extraction/result, inner source, knowledge. Next ayah and final predicate fulfill. Seed/burrow forks remain remote. **Grade: strong**.

### C20 — passive unit `وَحُصِّلَ مَا فِى ٱلصُّدُورِ`

- **Initial image:** the second passive repeats relative-subject and containment syntax but moves from grave-domain to human chest-domain.
- **V23-C:** `عدو=E:B004 | ضبح=Ø | وري=E:B005 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B001 | نقع=Ø | وسط=E:B002/B003 | جمع=E:B001 | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=E:B002 | حبب=E:B002/B004 | خير=E:B001 | شدد=E:B002 | علم=E:B001 | بعثر=E:B001/B003 | قبر=E:B002 | حصل=E:B001/B002 | صدر=E:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=second passive construction + relational/interior/extraction branches; freeze=outer disclosure deepens into extraction of the human inner source/result; P=knower with human object-reference. `خ ب ر B001 + رَبَّهُم بِهِمْ` fulfill. `(K: contents remain unspecified; passive agent unexpressed)`. **Grade: strong**.

### C21 — paired `[PASSIVE] مَا فِى [CONTAINER]`

- **Initial image:** exact adjacent templates align two enclosures and two disclosure operations.
- **V23-C:** `عدو=E:B004 | ضبح=Ø | وري=E:B005/B006 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B001/B002 | نقع=Ø | وسط=E:B002/B003 | جمع=E:B001 | ءنس=E:B001 | ربب=E:B001 | كند=E:B001/B002 | شهد=E:B002 | حبب=E:B004 | خير=E:B001 | شدد=E:B002 | علم=E:B001 | بعثر=E:B001/B002/B003 | قبر=E:B001/B002 | حصل=E:B001/B002 | صدر=E:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=parallel construction + full boundary/gather/scatter/relational/disclosure roots; freeze=outer buried and inner human contents undergo ordered exposure/extraction; P=unified inward knower concerning persons. `خ ب ر B001` and final attachments fulfill. `(K: two مَا sets and verbs are not lexically identical)`. **Grade: strong**.

### C22 — `رَبَّهُم بِهِمْ`

- **Initial image:** final رب has plural possessive humans, while `بِهِمْ` supplies the object of reference for the pending predicate.
- **V23-C:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=E:B001/B003 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B002 | علم=E:B001 | بعثر=E:B001 | قبر=E:B002 | حصل=E:B001/B002 | صدر=E:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=possessive/reference construction + prior human relation and disclosure state; freeze=the first relational target returns with collective person-reference; P=predicate of inward knowledge. `خ ب ر B001` immediately fulfills. `(K: does not assign رب as passive agent)`. **Grade: strong**.

### C23 — full final clause `إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍ لَخَبِيرٌ`

- **Initial image:** emphatic predication integrates relation, human plurality, object-reference, marked time, and inward expertise.
- **V23-C:** `عدو=C:B002/B004 | ضبح=C:B001 | وري=C:B005 | قدح=C:B002 | غير=C:B003 | صبح=C:B001 | ثور=C:B001/B002 | نقع=C:B004/B005 | وسط=C:B002/B003 | جمع=C:B001 | ءنس=E:B001 | ربب=E:B001/B003 | كند=E:B001/B002 | شهد=E:B001/B002/B008 | حبب=E:B002/B004 | خير=E:B001 | شدد=E:B001/B002 | علم=E:B001/B002 | بعثر=E:B001/B002/B003 | قبر=E:B001/B002 | حصل=E:B001/B002 | صدر=E:B001/B004 | خبر=E:B001`.
- **Lifecycle:** G=all final attachments/predication + human/relational/epistemic/disclosure roots; freeze=all outstanding roles complete. Earlier kinetic/trace/geometry roots become C in backward replay, not construction. P=none; `(K: no unresolved participant or operation remains)`. **Grade: strong** — explains stopping.

### C24 — lexical bracket `رَبِّهِ` → `رَبَّهُم`

- **Initial image:** the same relational root moves from generic singular possession to collective human possession after disclosure.
- **V23-C:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=E:B001/B007/B011 | كند=E:B001/B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B001/B002 | علم=E:B001 | بعثر=E:B001 | قبر=E:B002 | حصل=E:B001/B002 | صدر=E:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=root recurrence/possessive-number transition + relational trajectory; freeze=denied first relation persists through witness/motive/disclosure and returns collectively; P=knowledge. `خ ب ر B001` fulfills. `(K: number expansion does not introduce a different human class)`. **Grade: strong**.

## Morphosyntactic seed traversal

### MS01 — feminine-plural active-participle triad

- **Initial image:** `عَادِيَات / مُورِيَات / مُغِيرَات` preserve feminine-plural active agency while accumulating running, production, and change.
- **V23-M:** `عدو=E:B002 | ضبح=C:B001 | وري=E:B002 | قدح=C:B001 | غير=E:B003 | صبح=C:B001 | ثور=C:B002 | نقع=C:B004 | وسط=C:B003 | جمع=C:B010 | ءنس=C:B001 | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=C:B003 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=three ACT/FP participles + their rooted branches; freeze=unresolved collective capacities build before finite action; P=3FP finite continuation, effects, and boundary. Manner/time complements and 100:4–5 fulfill; human pivot/late charge corroborate. `(K: morphology does not identify species)`. **Grade: strong locally, medium passage-wide**.

### MS02 — manner, manner, time complements at 100:1–3

- **Initial image:** `ضَبْحًا / قَدْحًا / صُبْحًا` progressively specify how, how, then when.
- **V23-M:** `عدو=E:B002 | ضبح=E:B001 | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=E:B001 | ثور=C:B002 | نقع=C:B004 | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=C:B011 | خير=Ø | شدد=C:B003/B005 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=attachment roles + first six roots; freeze=audible exertion becomes ignition under a dawn boundary; P=finite effects and later spark/time/charge replay. `ث و ر/ن ق ع`, `ح ب ب B011`, and `ش د د B003/B005` fulfill. `(K: shared accusative ending does not imply same semantic role)`. **Grade: strong**.

### MS03 — Form IV corridor at 100:2–4

- **Initial image:** Form IV marks `مُورِيَات`, `مُغِيرَات`, and `أَثَرْنَ` in adjacent steps.
- **V23-M:** `عدو=Ø | ضبح=Ø | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=Ø | ثور=E:B001/B002 | نقع=C:B004 | وسط=C:B003 | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=measure pattern + fire/change/dislodging branches; freeze=production/change/causation corridor; P=visible effect and later state-changing disclosure. Dust, entry, grave/chest opening, extraction, and knowledge corroborate. `(K: one measure does not guarantee one shared lexical causative meaning)`. **Grade: medium-strong**.

### MS04 — participles → perfect finite actions

- **Initial image:** descriptive/ongoing active capacities turn into completed 3FP effects and entry.
- **V23-M:** `عدو=E:B002 | ضبح=E:B001 | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=E:B001 | ثور=E:B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B001 | ءنس=C:B001 | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=aspect/category transition + opening roots; freeze=capacities culminate in consequences and target-entry; P=scene completion followed by proposition. 100:5→6 boundary and human pivot corroborate. `(K: transition alone does not state the relation between scene and proposition)`. **Grade: medium-strong**.

### MS05 — 3FP subject continuity 100:1–5

- **Initial image:** the same feminine-plural activation persists across participles and suffixed perfect verbs.
- **V23-M:** `عدو=E:B002 | ضبح=E:B002 | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=E:B004 | ثور=E:B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B002 | ءنس=C:B001 | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=C:B003 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=gender/number continuity + opening event roots; freeze=one unresolved collective moves through the whole scene; P=boundary and referent/number change. `ء ن س B001` and `ش د د B003` corroborate pivot/reactivation. `(K: no lexical subject identity)`. **Grade: strong structurally**.

### MS06 — accusative role progression 100:1–5

- **Initial image:** two manners → time → produced object → entered object.
- **V23-M:** `عدو=E:B002 | ضبح=E:B001 | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=E:B001 | ثور=E:B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B001/B002 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=attachment/case progression + opening branches; freeze=scene thickens from action quality and time into effect and target; P=completion at 100:5. Verse boundary fulfills. `(K: accusative forms are structurally distinct)`. **Grade: strong**.

### MS07 — active opening → passive disclosures

- **Initial image:** explicit 3FP agency yields to agent-suppressing passives focused on hidden contents.
- **V23-M:** `عدو=E:B002 | ضبح=Ø | وري=E:B005 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B001/B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B001 | ءنس=E:B001 | ربب=C:B001 | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=E:B002 | علم=Ø | بعثر=E:B001/B002/B003 | قبر=E:B001/B002 | حصل=E:B001/B002 | صدر=E:B001 | خبر=C:B001`.
- **Lifecycle:** G=voice transition + action/disclosure roots; freeze=attention moves from agents generating effects to contents undergoing exposure; P=relation/knower rather than necessarily passive actor. Final `ر ب ب + خ ب ر` fulfills knowledge. `(K: do not infer رب as passive agent)`. **Grade: strong**.

### MS08 — person/number trajectory: 3FP → generic 3MS → 3MP

- **Initial image:** collective outward agency contracts to one generic human and expands to final human plurality.
- **V23-M:** `عدو=E:B002 | ضبح=E:B002 | وري=Ø | قدح=Ø | غير=E:B005 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=E:B002 | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B002 | علم=E:B001 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=E:B001 | خبر=C:B001`.
- **Lifecycle:** G=person/number morphology + human relational trajectory; freeze=exterior collective → singular inward diagnosis → collective human closure; P=knowledge. `خ ب ر B001` fulfills. `(K: opening FP and closing MP are not coreferentially equated)`. **Grade: medium-strong**.

### MS09 — changing prepositional geometry

- **Initial image:** `بـ` means/reference, `لـ` relation, `على` witness scope, `فِى` containment, and final `بـ` human reference successively reshape the model.
- **V23-M:** `عدو=E:B004 | ضبح=Ø | وري=E:B006 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B002 | نقع=E:B004 | وسط=E:B002/B003 | جمع=E:B001 | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B002 | علم=E:B001 | بعثر=E:B001 | قبر=E:B002 | حصل=E:B002 | صدر=E:B001 | خبر=E:B001`.
- **Lifecycle:** G=all prepositional attachments + selected geometry/relational roots; freeze=means-driven motion becomes relational orientation, witness-content, enclosure, then person-reference in knowledge. P=none at final; roles complete. `(K: repeated prepositions do not imply same relation)`. **Grade: strong**.

### MS10 — emphatic `إِنَّ...لَ` frame

- **Initial image:** emphatic diagnosis at 100:6–8 is interrupted by question/disclosure and answered by emphatic final knowledge.
- **V23-M:** `عدو=C:B002 | ضبح=C:B001 | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B002 | علم=C:B001 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=ACC/EMPH morphology and predications + human propositions; freeze after 100:8=emphatic diagnosis awaits challenge/resolution; P=question, disclosed basis, emphatic close. 100:9–11 fulfill. Opening sound/motion only corroborate discourse framing. **Grade: strong**.

### MS11 — doubled passive relative-subject template

- **Initial image:** both passives take overt relative `مَا`, each completed by `فِى` + container.
- **V23-M:** `عدو=E:B004 | ضبح=Ø | وري=E:B005 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B001 | نقع=Ø | وسط=E:B002 | جمع=Ø | ءنس=E:B001 | ربب=Ø | كند=Ø | شهد=Ø | حبب=E:B004 | خير=Ø | شدد=Ø | علم=Ø | بعثر=E:B001/B003 | قبر=E:B001/B002 | حصل=E:B001/B002 | صدر=E:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=subject/prep template + concealment/inversion/extraction roots; freeze=two hidden-content levels undergo parallel but nonidentical disclosure; P=unified inner knower. `خ ب ر B001` fulfills. `(K: verbs/contents differ; agent omitted)`. **Grade: strong**.

### MS12 — possessive/idafa chain

- **Initial image:** `رَبِّهِ`, `حُبِّ ٱلْخَيْرِ`, and `رَبَّهُم` bind relation, valued object, and final collective relation.
- **V23-M:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B001 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=E:B001/B002 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001/B005 | شدد=E:B002 | علم=E:B001 | بعثر=Ø | قبر=Ø | حصل=E:B001 | صدر=E:B004 | خبر=C:B001`.
- **Lifecycle:** G=idafa/possessive morphology + relational roots; freeze=human relation, object of love, and plural return are grammatically linked without equating them; P=final knowledge. `خ ب ر B001` fulfills. `(K: possession morphology does not make الخير property)`. **Grade: strong**.

### MS13 — unresolved singular pronouns → resolved plural pronouns

- **Initial image:** repeated singular `بِهِ` accompanies opening effects without lexical resolution; final `هُم/بِهِمْ` explicitly tracks humans.
- **V23-M:** `عدو=E:B002 | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=E:B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B002 | ءنس=C:B001 | ربب=C:B001 | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=pronoun recurrence/shift + opening causal sequence; freeze=unresolved means-reference contrasts with resolved human reference; P=human relational closure. Final `هُم/بِهِمْ`, chest, and knowledge corroborate. `(K: no coreference between singular and plural forms)`. **Grade: medium**.

### MS14 — anaphora and demonstrative continuity

- **Initial image:** `ٱلْإِنسَانَ` remains active through `هُ`, `ذَٰلِكَ`, repeated `هُ`, implicit 3MS in `يَعْلَمُ`, then expands to `هُم`.
- **V23-M:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B002 | علم=E:B001 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=E:B001 | خبر=C:B001`.
- **Lifecycle:** G=referential chain + human proposition roots; freeze=one human referent carries diagnosis, witness, motive, and cognition before pluralized closure; P=inner knowledge. `ص د ر B001 + خ ب ر B001` fulfill. `(K: demonstrative points to matter, not a new person)`. **Grade: strong**.

## Temporal and acoustic seed traversal

### T01 — boundary 100:1→100:2: breath to ignition

- **Initial image:** audible running remains active when the next ayah supplies hidden fire and striking.
- **V23-T:** `عدو=E:B002 | ضبح=E:B001/B002 | وري=E:B002 | قدح=E:B001 | غير=Ø | صبح=Ø | ثور=C:B001/B002 | نقع=C:B004 | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=C:B011 | خير=Ø | شدد=C:B003 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=boundary order + running/breath/fire/strike; freeze=exertion immediately becomes ignition; P=generated effect and later spark/charge replay. Dust and late `ح ب ب/ش د د` fulfill. `(K: temporal adjacency does not identify the physical instrument)`. **Grade: strong locally, medium-strong overall**.

### T02 — boundary 100:2→100:3: ignition to dawn action

- **Initial image:** fire-striking is followed by changed/action-bearing agents at a marked time.
- **V23-T:** `عدو=E:B002 | ضبح=Ø | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=E:B001/B004 | ثور=C:B002 | نقع=C:B004 | وسط=Ø | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=C:B003 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=ordered boundary + fire/change/dawn; freeze=ignition is placed inside a dawn charge/transition; P=finite consequence and force echo. Dust/dislodging and late charge corroborate. `(K: no combat identity)`. **Grade: medium-strong**.

### T03 — boundary 100:3→100:4: participle/time to finite effect

- **Initial image:** time-bounded agent description changes into completed causation with a direct object.
- **V23-T:** `عدو=E:B002 | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B003 | صبح=E:B001 | ثور=E:B001/B002 | نقع=E:B004 | وسط=C:B003 | جمع=Ø | ءنس=Ø | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=Ø | خير=Ø | شدد=Ø | علم=C:B002 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=boundary/aspect shift + change/dawn/dislodging/dust; freeze=described capacity becomes visible effect; P=effect used for entry and trace. Center-entry and sign/mark corroborate. **Grade: strong**.

### T04 — boundary 100:4→100:5: produced effect to center-entry

- **Initial image:** dust/effect and repeated `بِهِ` remain active as the same actors enter a gathered center.
- **V23-T:** `عدو=E:B004 | ضبح=Ø | وري=E:B006 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B002 | نقع=E:B004 | وسط=E:B002/B003 | جمع=E:B001/B002 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=Ø | حبب=C:B004 | خير=Ø | شدد=Ø | علم=Ø | بعثر=C:B003 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001/B002 | خبر=C:B001`.
- **Lifecycle:** G=boundary/repeated pronoun + effect/edge/center/group; freeze=generated trace becomes means/accompaniment of inward entry; P=deeper enclosures and reversal. Closing geometry fulfills. `(K: pronoun antecedent unresolved; no object identity)`. **Grade: strong**.

### T05 — boundary 100:5→100:6: action scene to human diagnosis

- **Initial image:** center-entry stops; emphatic singular human diagnosis begins.
- **V23-T:** `عدو=E:B002/B004 | ضبح=E:B001 | وري=E:B002 | قدح=E:B001 | غير=E:B005 | صبح=E:B001 | ثور=E:B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B001 | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=C:B002 | حبب=C:B002 | خير=C:B001 | شدد=C:B002 | علم=C:B001 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=ayah boundary + opening model + human/contrast/diagnosis; freeze=outer collective force is held while discourse contracts to inward singular relation; P=witness/motive and deep disclosure. Every selected later root fulfills. `(K: boundary does not assert analogy or agent identity)`. **Grade: strong**.

### T06 — boundary 100:6→100:7: diagnosis to self-witness

- **Initial image:** the diagnosed human immediately becomes witness concerning `ذَٰلِكَ`.
- **V23-T:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=E:B001/B002 | حبب=C:B002 | خير=C:B001 | شدد=C:B002 | علم=C:B001 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=boundary + referential continuity + diagnosis/witness; freeze=self-witness anchors the claim; P=motive, cognition, disclosed basis, final knower. 100:8–11 fulfill. **Grade: strong**.

### T07 — boundary 100:7→100:8: witness to motive/intensity

- **Initial image:** after witnessing the diagnosis, recitation specifies the human's intense value-attachment.
- **V23-T:** `عدو=F:B007 | ضبح=Ø | وري=Ø | قدح=F:B010 | غير=F:B004 | صبح=Ø | ثور=Ø | نقع=F:B002 | وسط=Ø | جمع=F:B003 | ءنس=E:B001/B006 | ربب=E:B001 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B001/B002 | علم=C:B001 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B001/B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=boundary + repeated anaphora + witness/motive roots; freeze=witness is followed by a possible inward mechanism for the diagnosis; P=cognition and exposure of that mechanism. Closing roots fulfill; distraction/planning/jealousy/self-settling/resolve remain rivals. `(K: sequence does not state causal equivalence)`. **Grade: strong**.

### T08 — boundary 100:8→100:9: maximum intensity to cognition challenge

- **Initial image:** intense attachment is immediately followed by `أَفَلَا يَعْلَمُ` and conditioned disclosure.
- **V23-T:** `عدو=C:B002 | ضبح=C:B001 | وري=C:B002/B005 | قدح=C:B001/B010 | غير=C:B003 | صبح=Ø | ثور=C:B001/B002 | نقع=C:B004 | وسط=C:B003 | جمع=C:B003/B010 | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=E:B002 | حبب=E:B002/B011 | خير=E:B001 | شدد=E:B002/B003 | علم=E:B001 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=boundary + relational/intensity/cognition roots; freeze=intense inward attachment is put under a knowledge test; P=forced opening of hidden basis. Opening force/fire are backward C, and closing disclosure roots fulfill. `(K: attachment does not cause the later event)`. **Grade: strong**.

### T09 — boundary 100:9→100:10: grave interior to chest interior

- **Initial image:** one passive enclosure-disclosure is immediately repeated at a deeper human level.
- **V23-T:** `عدو=E:B004 | ضبح=Ø | وري=E:B005/B006 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B001 | نقع=Ø | وسط=E:B002 | جمع=Ø | ءنس=E:B001 | ربب=Ø | كند=Ø | شهد=Ø | حبب=E:B004 | خير=Ø | شدد=Ø | علم=Ø | بعثر=E:B001/B003 | قبر=E:B001/B002 | حصل=E:B001/B002 | صدر=E:B001/B004 | خبر=C:B001`.
- **Lifecycle:** G=boundary/parallel syntax + enclosure/disclosure roots; freeze=outer buried contents become inner human contents; P=unified inward knowledge. Final `خ ب ر B001` fulfills. `(K: operations and contents differ)`. **Grade: strong**.

### T10 — boundary 100:10→100:11: extracted interior to informed رب

- **Initial image:** chest contents are extracted, then the first relational noun returns as emphatic inward knower of the people.
- **V23-T:** `عدو=Ø | ضبح=Ø | وري=E:B005 | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=E:B001/B003 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B002 | علم=E:B001 | بعثر=E:B001 | قبر=E:B002 | حصل=E:B001/B002 | صدر=E:B001/B004 | خبر=E:B001`.
- **Lifecycle:** G=boundary + full relational/disclosure state; freeze=the disclosed inner record awaits a knower and relational closure; final clause fills all roles. `(K: final رب not inferred as passive agent)`. **Grade: strong**.

### T11 — repeated `فَـ` acceleration at 100:2–5

- **Initial image:** four successive `فَـ` prefixes preserve rapid event-to-event activation.
- **V23-T:** `عدو=E:B002 | ضبح=E:B001/B002 | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=E:B001 | ثور=E:B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B010 | ءنس=C:B001 | ربب=Ø | كند=Ø | شهد=Ø | حبب=C:B011 | خير=Ø | شدد=C:B003 | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=repetition/order + opening roots; freeze=each event's result becomes the next search key; P=hard stop/pivot and delayed force/spark reactivation. 100:6 boundary, `ح ب ب B011`, and `ش د د B003` fulfill. `(K: فـ alone does not prove strict physical causation)`. **Grade: strong**.

### T12 — `صُبْحًا` → `يَوْمَئِذٍ`

- **Initial image:** early dawn remains active when a final marked day/time closes the sequence.
- **V23-T:** `عدو=E:B002 | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=E:B001/B009 | ثور=Ø | نقع=Ø | وسط=Ø | جمع=F:B004 | ءنس=Ø | ربب=E:B001 | كند=Ø | شهد=F:B008 | حبب=Ø | خير=Ø | شدد=E:B005 | علم=E:B001 | بعثر=E:B001 | قبر=E:B001 | حصل=E:B001 | صدر=E:B001 | خبر=E:B001`.
- **Lifecycle:** G=temporal positions + dawn/day-height roots; freeze=immediate action-time contrasts with later disclosure/knowledge-time; P=conditioned transition and resolution. `إِذَا`, passives, final time attachment, and knowledge fulfill. Gathering-day/sign forks remain. `(K: two times are not equated)`. **Grade: medium-strong**.

### T13 — `قَدْحًا` → `حُبِّ...شَدِيدٌ` backward replay

- **Initial image:** early fire-strike fades; late `ح ب ب B011` and `ش د د B003` reactivate sparks/hooves and charge beside contextual love/intensity.
- **V23-T:** `عدو=E:B002/B010 | ضبح=E:B002/B003 | وري=E:B002 | قدح=E:B001 | غير=Ø | صبح=Ø | ثور=E:B001/B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B010 | ءنس=Ø | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=E:B011,K:B002-local | خير=E:B001 | شدد=E:B003,K:B002-local | علم=C:B002 | بعثر=C:B001/B003 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=ordered delay + spark/charge branches; freeze at 100:8=opening heat/force becomes secondary geometry for inward intensity; P=force on hidden interiors. Next passives and final knowledge fulfill. `(K: exact idafa/attachment preserve love of good and noncombat intensity)`. **Grade: medium-strong**.

### T14 — delayed `رَبِّهِ` → `رَبَّهُم`

- **Initial image:** the first relational target disappears for four ayahs, then returns in the final clause with number expansion.
- **V23-T:** `عدو=Ø | ضبح=Ø | وري=Ø | قدح=Ø | غير=E:B001 | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=E:B001/B007/B011 | كند=E:B001/B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001/B005 | شدد=E:B001/B002 | علم=E:B001 | بعثر=E:B001 | قبر=E:B002 | حصل=E:B001/B002 | صدر=E:B001/B004 | خبر=E:B001`.
- **Lifecycle:** G=lexical delay/recurrence + intervening relational/disclosure roots; freeze=denied relation remains latent and returns after its inward result is exposed; P=knowledge. `خ ب ر B001` in the return clause completes. `(K: recurrence does not prove covenant/duration branches literally)`. **Grade: strong**.

### T15 — acoustic/prepositional `بِهِ، بِهِ، بِهِمْ`

- **Initial image:** two singular forms accompany opening action, then a plural form accompanies final knowledge.
- **V23-T:** `عدو=E:B002 | ضبح=Ø | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=E:B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B002 | ءنس=C:B001 | ربب=C:B001 | كند=Ø | شهد=Ø | حبب=Ø | خير=Ø | شدد=Ø | علم=Ø | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=sound/preposition recurrence + opening means/effect; freeze=action-linked `بـ` is reactivated as person-linked reference; P=human closure. Final human/chest/knowledge roots corroborate. `(K: different number, governor, and referents)`. **Grade: medium**.

### T16 — acoustic triad `ضَبْحًا / قَدْحًا / صُبْحًا`

- **Initial image:** three ayah endings share accusative `-an` and final root consonant `ح`, while lexical roles move breath → strike → dawn.
- **V23-T:** `عدو=E:B002 | ضبح=E:B001 | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=E:B001 | ثور=C:B002 | نقع=C:B004/B005 | وسط=Ø | جمع=Ø | ءنس=C:B002 | ربب=Ø | كند=Ø | شهد=C:B008 | حبب=C:B011 | خير=Ø | شدد=C:B003 | علم=C:B002 | بعثر=Ø | قبر=Ø | حصل=Ø | صدر=Ø | خبر=Ø`.
- **Lifecycle:** G=acoustic sequence + breath/strike/time roots; freeze=sound recurrence binds changing roles into one accelerating opening; P=effect and delayed acoustic/conceptual reactivation. Dust/sound/perception/sign/spark/charge fulfill. `(K: phonological similarity does not merge lexical meanings)`. **Grade: medium-strong**.

### T17 — three cadence blocks

- **Initial image:** 100:1–5 close in accusative `-ā`, 100:6–8 in emphatic `-ūd/-īd`, and 100:9–11 in `قُبُور/صُدُور/خَبِير`-like closings.
- **V23-T:** `عدو=E:B002 | ضبح=E:B001 | وري=E:B002 | قدح=E:B001 | غير=E:B003 | صبح=E:B001 | ثور=E:B002 | نقع=E:B004 | وسط=E:B003 | جمع=E:B001 | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B002 | علم=E:B001 | بعثر=E:B001 | قبر=E:B001/B002 | حصل=E:B002 | صدر=E:B001 | خبر=E:B001`.
- **Lifecycle:** G=ayah-end sound grouping + representative roots; freeze=kinetic, diagnostic, and disclosure/knowledge phases are acoustically segmented; P=boundary-aligned syntax. QAC/attachments and discourse shifts corroborate. `(K: cadence is structural evidence only)`. **Grade: medium-strong**.

### T18 — `قُبُور / صُدُور / خَبِير` closing resonance

- **Initial image:** adjacent plural enclosures share `-ُور`, then final `خَبِير` preserves a related long-vowel/rhotic close while changing from containers to knower.
- **V23-T:** `عدو=Ø | ضبح=Ø | وري=E:B005 | قدح=Ø | غير=E:B003 | صبح=Ø | ثور=E:B001 | نقع=Ø | وسط=E:B002 | جمع=Ø | ءنس=E:B001 | ربب=E:B001 | كند=Ø | شهد=Ø | حبب=E:B004 | خير=Ø | شدد=Ø | علم=E:B001 | بعثر=E:B001 | قبر=E:B001/B002 | حصل=E:B002 | صدر=E:B001/B004 | خبر=E:B001`.
- **Lifecycle:** G=acoustic adjacency + enclosure/disclosure/knowledge roots; freeze=sound carries activation from grave-container to chest-container to inward knower; P=none. `(K: resonance does not establish etymological or referential identity)`. **Grade: medium-strong**.

### T19 — `إِنَّ / وَإِنَّهُ / وَإِنَّهُ / إِنَّ` refrain

- **Initial image:** emphatic framing marks diagnosis, two elaborations, and final resolution.
- **V23-T:** `عدو=C:B002 | ضبح=C:B001 | وري=Ø | قدح=Ø | غير=Ø | صبح=Ø | ثور=Ø | نقع=Ø | وسط=Ø | جمع=Ø | ءنس=E:B001 | ربب=E:B001 | كند=E:B002 | شهد=E:B002 | حبب=E:B002 | خير=E:B001 | شدد=E:B002 | علم=C:B001 | بعثر=C:B001 | قبر=C:B002 | حصل=C:B002 | صدر=C:B001 | خبر=C:B001`.
- **Lifecycle:** G=refrain positions + human propositions; freeze after 100:8=emphatic diagnosis/elaboration awaits answer; P=question/disclosure and emphatic close. 100:9–11 fulfill. Opening roots only establish oath-to-assertion transition. **Grade: strong**.

### T20 — terminal `خَبِيرٌ`

- **Initial image:** after trace, witness, cognition, and exposed interiors, inward expertise occupies the last predicate.
- **V23-T:** `عدو=C:B002/B004/B010 | ضبح=C:B001 | وري=C:B005 | قدح=C:B002 | غير=C:B003 | صبح=C:B005 | ثور=C:B001/B002 | نقع=C:B004/B005 | وسط=C:B002/B003 | جمع=C:B001 | ءنس=E:B001/B002 | ربب=E:B001/B003 | كند=E:B001/B002 | شهد=E:B001/B002/B008 | حبب=E:B002/B004 | خير=E:B001 | شدد=E:B001/B002 | علم=E:B001/B002 | بعثر=E:B001/B002/B003 | قبر=E:B001/B002 | حصل=E:B001/B002 | صدر=E:B001/B004 | خبر=E:B001`.
- **Lifecycle:** G=final word plus active human/relational/epistemic/disclosure state; freeze=all unresolved roles—knower, persons, time, relation, inward matter—are filled. Earlier kinetic/geometry roots become backward corroborators. P=none; `(K: no continuation needed inside assigned passage and no claim of exhaustive interpretation)`. **Grade: strong**.

## Post-creation exhaustiveness audit and revisions

### Mechanical coverage audit

| Audited unit | Required or derived total | Observed total | Result |
|---|---:|---:|---|
| Uncontaminated lexical branches | 173 | 173 `Bxxx` headings | complete |
| Ordinary branch-occurrence seed passes | 156 | 156 | complete |
| `ر ب ب` branches at 100:6:3 | 17 | 17 | complete |
| `ر ب ب` branches at 100:11:2 | 17 | 17 | complete |
| Total occurrence-level lexical vectors | 190 | 190 `V23` vectors | complete |
| Ordinary lexical records with initial image, vector, lifecycle, constraints, and grade | 156 | 156 | complete |
| `ر ب ب` occurrence-specific records with the same fields | 34 | 34 | complete |
| Cells in every lexical vector | 23 | 23; zero malformed vectors | complete |
| Constructional seeds | 24 | 24 `V23-C` vectors | complete |
| Morphosyntactic seeds | 14 | 14 `V23-M` vectors | complete |
| Temporal/acoustic seeds | 20 | 20 `V23-T` vectors | complete |
| Structural records with initial image, vector, lifecycle, constraints, and grade | 58 | 58 | complete |
| Cells in every structural vector | 23 | 23; zero malformed vectors | complete |

The lexical branch totals in first-occurrence order are `12, 5, 8, 10, 5, 10, 7, 9, 7, 13, 6, 17, 4, 6, 12, 5, 6, 6, 3, 4, 6, 6, 6`. Their sum is 173. Because `ر ب ب` occurs twice, its seventeen branches were each restarted at both occurrences; therefore the occurrence-level total is `173 - 17 + (17 × 2) = 190`. No `Ø` cell was inferred from another seed: it records a separate no-selection decision after the full dossier visit.

The ordering audit confirms that the first singleton is `ع د و B001` and that no later apparently promising family displaced an earlier or weaker branch. The final singleton is `خ ب ر B006`. The opening context was checked separately: the visible basmala has no permitted QAC row and remains non-seeding.

### Missing-image audit

After the first complete draft, every branch image was swept again by semantic role rather than by early model promise. The role families checked were:

- motion, direction, edge, center, terrain, force, impact, and restraint;
- breath, sound, fire, light, color, surface, particle, and remainder;
- liquid, vessel, food, plant, soil, animal, body, disease, birth, and generation;
- human identity, relation, covenant, law, exchange, gift, benefit, value, withholding, and choice;
- perception, visible mark, witness, speech, knowledge, concealment, enclosure, inversion, extraction, chest, source, and inward content.

This second route recovered four families that could be underrepresented by a model-first reading. They are now retained below as explicit convergence candidates: (1) surface disturbance progressing to grave-earth and then chest-content depth; (2) deliberation/choice behind attachment; (3) visible surface or screen versus a concealed core and self-witness; and (4) benefit/gift versus withholding inside the relational economy. Water/storage, animal/reproduction, legal, projectile/lot, disease, food, and speech images were also regenerated, but their required roles failed and are recorded as controls rather than silently dropped.

The construction audit then restarted at every eligible multiword and repeated-form unit found in the permitted morphology/attachment data. It found no unseeded coordination, idafa, prepositional, passive, emphatic, anaphoric, temporal, cadence, or ayah-boundary unit beyond C01–C24, MS01–MS14, and T01–T20. A final image-family sweep after the revisions found no remaining branch title without a singleton pass, no eligible rooted occurrence without an occurrence-sensitive pass, and no potentially passage-scale family without either a convergence record or a stated defeat.

## Convergence synthesis

The table below does not create candidates from branch density. Each retained row requires multiple independently initiated singleton or construction seeds, a freeze before the closing evidence is consumed, and later role fulfillment that is more specific than generic thematic similarity.

| Candidate image | Independent seed convergence | Frozen prediction and later test | Decision |
|---|---|---|---|
| Surface disturbance → deep disclosure | `ع د و B002/B010`, `ث و ر B001/B002`, `ن ق ع B004`, `ب ع ث ر B001`, `ق ب ر B001/B002`, `ح ص ل B002`, `ص د ر B001/B004`, `خ ب ر B001`; C05, C19–C21; MS07/MS11; T09–T10 | Opening motion should leave a surface effect, then the closing should move below the surface, open an enclosure, extract a core, expose an inward source, and end in inward knowledge. Dust, overturned grave-earth, extracted chest contents, and `خَبِيرٌ` fulfill the ordered roles. | **strong** |
| Edge → center → interior, followed by reversal outward | `ع د و B004/B009`, `و ر ي B005/B006`, `و س ط B002/B003`, `ب ع ث ر B003`, `ق ب ر B002`, `ح ص ل B002`, `ص د ر B001/B002`; C06/C21; MS06/MS09; T04/T09 | After crossing and center-entry freeze, explicit enclosures and an inside marker should appear; the closure should invert or expose them and separate what was within. Both `مَا فِى` passives fulfill this without requiring a literal common container. | **strong** |
| Misoriented relation and tightened attachment | both `ر ب ب B001/B002` occurrence sweeps, `ك ن د B001/B002`, `ح ب ب B002`, `خ ي ر B001/B005`, `ش د د B001/B002/B006`, `ص د ر B004`, `خ ب ر B001`; C09–C16/C22–C24; MS10/MS12–MS14; T14/T19 | Once denial/cutting toward `رَبِّهِ` and attachment to benefit freeze, the passage should expose an inward motive and return to the relational target as knower. The chest disclosure and `رَبَّهُم...خَبِيرٌ` return fulfill; covenant, gift, and miserliness remain bounded submodels. | **strong** |
| Sound/trace → witness → knowledge | `ض ب ح B001`, `ن ق ع B004/B005`, `ء ن س B002`, `ش ه د B001/B002/B008`, `ع ل م B001/B002`, `خ ب ر B001`; C11/C15/C17/C23; T06/T16/T20 | Perceptible effects should become marks, marks should support witness, and direct disclosure should supersede indirect signs in final knowledge. That sequence is present; it does not require every sound branch to be literal. | **strong** |
| Latent spark and charge replay | `و ر ي B002`, `ق د ح B001`, `ح ب ب B011`, `ش د د B002/B003`, with `ث و ر B002` and `ن ق ع B004`; C03/C08/C12; T01/T11/T13 | Fire released by impact should leave a delayed force/spark echo after the opening. The late roots independently offer spark and charge branches, while local syntax constrains `حُبِّ` to attachment and `شَدِيدٌ` to intensity rather than literal combat. | **medium-strong** |
| Deliberation → selected value → inward source | `ق د ح B010`, `ج م ع B003`, `ء ن س B006`, `ح ب ب B002/B003`, `خ ي ر B003`, `ش د د B002`, `ع ل م B001`, `ص د ر B004`, `خ ب ر B001`; C12/C16/C17/C20 | A choice/resolve image should culminate not merely in an external object but in an inward source available to knowledge. `حُبِّ ٱلْخَيْرِ`, the cognition challenge, and chest-content disclosure fulfill. No explicit consultation or divination permits a stronger grade. | **medium-strong** |
| Visible screen/mark → concealed core → self-witness | `و ر ي B005`, `ص ب ح B005/B006`, `ء ن س B002/B005`, `ش ه د B001/B008`, `ح ب ب B004`, `ع ل م B001/B002`, `ح ص ل B002`, `ص د ر B001`, `خ ب ر B001`; C11/C15/C20; T06/T18/T20 | Surface light, image, or sign should contrast with a hidden center that is later made manifest and known. Witness, extracted chest content, and inward expertise fulfill; lamp, beauty, pupil, and anatomical heart stay analogical, not referential. | **medium-strong** |
| Cultivation/harvest and residue | `ع د و B011`, `ق د ح B009`, `غ ي ر B001`, `ن ق ع B001/B002`, `ج م ع B011`, `ر ب ب B012/B013`, `ك ن د B003`, `ح ب ب B001`, `ح ص ل B003/B005`, `خ ب ر B002/B003/B005` | Seed, water, soil, growth, barrenness, gathering, and core/residue roles can be assembled, and benefit plus extraction support a harvest-like closure. The passage supplies no literal sowing, crop, cultivator, or harvest action, so this remains a secondary medium. | **medium** |
| Benefit/gift versus withholding/accounting | `غ ي ر B001/B002`, `ر ب ب B001/B016`, `ك ن د B002`, `ح ب ب B002`, `خ ي ر B001/B005`, `ش د د B006`, `ح ص ل B001`, `ص د ر B005`, `خ ب ر B006`; C10/C12/C13/C23 | A received benefit followed by withholding should predict a final reckoning or informed division. Relational ingratitude, love of benefit, result, and informed closure fit, but no explicit donor-transfer-payment sequence appears. | **medium** |
| Dawn-local activation | `ص ب ح B001/B002/B004/B009` with `ع د و B002`, `ض ب ح B002`, `غ ي ر B003`, `ث و ر B002`, and `ج م ع B010`; C04/C08; T02/T12 | The opening should become a coordinated action at dawn and may contrast with the final marked day. Local time and sequence are exact; identification with a named historical or eschatological event is not licensed. | **medium, local only** |

### Exhaustive controls and defeated passage-scale models

- **Combat/raid:** force, dawn, dust, center-entry, and gathered bodies generate it repeatedly, but opponent, weapon, rider, wound, and explicit hostile relation never arrive. It remains a possible local scene-shape, not a licensed named event.
- **Animal physiology or herd:** running limbs, camel/horse pain, cattle, herd, and mount-side branches generate complete forks. Species, rider, tack, feeding, illness, and collapse roles fail.
- **Water, drink, vessel, and food storage:** water, soaking, cup, jar, abundance, crop, food, and bodily storage branches connect densely. No liquid or food patient and no filling, drinking, pouring, or emptying action appears.
- **Birth, reproduction, and genealogy:** intercourse, pregnancy, birth discharge, offspring, maturation, seed, and prior burial can form a life-cycle. Parent-child reference and birth/genealogy predicates are absent.
- **Legal claim, compensation, and adjudication:** limit-crossing, appeal, blood compensation, mediation, covenant, testimony, seizure, and informed judgment form a procedural fork. Claimant, respondent, verdict, remedy, and transaction syntax are absent.
- **Arrow, projectile, lot, or divination:** shaft/cup, drawing lots, striking, resolve, direction, center, and gathering form a tool-procedure fork. Bow, casting/drawing operation, target, allocation, and outcome formula are absent.
- **Disease, poison, and inward decay:** breath, lung injury, contagion, poison, tooth/tree decay, chest, and inward knowledge converge. No patient, transfer, symptom sequence, or disease disclosure appears.
- **Speech abuse and accusation:** raised sound, insult, lineage attack, witness, tongue, and knowledge converge. No speaker, utterance, accused party, or reported content appears.
- **Named place, tribe, constellation, or lexical particle:** the proper-name and particle branches never acquire a syntactic host in the sacred text; they are defeated locally before passage-scale testing.

## Minimal passage-level result

Within the permitted evidence, the strongest convergent image is an ordered movement from forceful surface action and center-entry to human relational diagnosis, then to the reversal of hidden enclosures, extraction of inward content, and comprehensive inward knowledge. The evidence/trace chain and the contrast between relation to the `رب` and intensified attachment to `الخير` reinforce that movement. This is a constrained Stage 1 model, not a translation or a claim that the defeated lexical images are meanings of the passage.
