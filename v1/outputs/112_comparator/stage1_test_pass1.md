# Stage 1 Pass 1 — S112 comparator test lane

Assigned passage: S112  
Sacred Arabic source: `resources/quran/surah_112.json`  
Prompt followed: `v1/prompts/stage1.md`  
Output: `v1/outputs/112_comparator/stage1_test_pass1.md`

## Scope and evidence boundary

Sacred Arabic text used:

```text
opening-context, not seed: بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
112:1 قُلْ هُوَ ٱللَّهُ أَحَدٌ
112:2 ٱللَّهُ ٱلصَّمَدُ
112:3 لَمْ يَلِدْ وَلَمْ يُولَدْ
112:4 وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ
```

The basmala is opening context only. It never initiates a seed. I use it only once as opening-context corroboration for the divine-name / commanded-utterance frame.

Rooted QAC sequence for the assigned ayah interval:

```text
112:1:1 قُلْ        root قول    V IMPV 2MS
112:1:3 ٱللَّهُ     root ءله    PN NOM
112:1:4 أَحَدٌ      root ءحد    N INDEF NOM
112:2:1 ٱللَّهُ     root ءله    PN NOM
112:2:2 ٱلصَّمَدُ   root صمد    DET + N MS NOM
112:3:2 يَلِدْ      root ولد    V IMPF JUS 3MS, governed by لَمْ
112:3:4 يُولَدْ     root ولد    V IMPF PASS JUS 3MS, governed by لَمْ
112:4:2 يَكُن       root كون    V IMPF JUS 3MS, governed by وَلَمْ
112:4:4 كُفُوًا     root كفء    N INDEF ACC
112:4:5 أَحَدٌۢ     root ءحد    N INDEF NOM
```

Structural attachment rows used as structure only:

```text
112:1 a1 quoted_complement: quoted content after قُلْ is هُوَ ٱللَّهُ أَحَدٌ.
112:1 a2 predication: أَحَدٌ is nominative predicate of ٱللَّهُ.
112:1 a3 apposition: ٱللَّهُ can stand as apposition to هُوَ while أَحَدٌ supplies the nominal predicate.
112:2 a1 predication: ٱلصَّمَدُ is nominative predicate of ٱللَّهُ.
112:3 a1 particle_complement: يَلِدْ governed by لَمْ as jussive negated imperfect.
112:3 a2 conjoined: يُولَدْ coordinated with يَلِدْ in the preceding negated clause.
112:3 a3 particle_complement: يُولَدْ governed by لَمْ as jussive negated passive imperfect.
112:4 a1 particle_complement: يَكُن governed by لَمْ as jussive negated imperfect.
112:4 a2 prep_complement: pronoun in لَّهُۥ is governed by لَـ as complement of كُفُوًا.
112:4 a3 kana_predicate: كُفُوًا is accusative predicate of negated copula يَكُن.
112:4 a4 subject: أَحَدٌ is delayed nominative subject of يَكُن.
```

## Uncontaminated furuq v4 branch dossiers read

Each root dossier was read as continuous branch-preserving prose. The entries below preserve the branch IDs and the exact `branch_image_ar` + `what_is_ar` content used for the sweep.

```text
ء ح د
  B001 الأَحَدِيَّة والوَحْدَة — أحد بمعنى الواحد، والوصف المطلق بأحد، وتكرار أحد أحد للتأكيد
  B002 استغراق النفي — أحد في سياق النفي لاستغراق جنس من يصلح أن يخاطب، فيشمل الواحد وما فوقه
  B003 الواحد في العد والتركيب — أحد في العد، وتركيبه مع العشرات، وتصْيير المعدود أحد عشر
  B004 الأول والإضافة — أحد مضافا أو مضافا إليه بمعنى الأول، واسم يوم الأحد
  B005 الانفراد والتفرق آحادا — الانفراد بالفعل، والمجيء آحادا أفرادا
  B006 جبل أُحُد — اسم جبل بالمدينة

ء ل ه
  B001 التعبد والمعبود — يدخل فيه أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.
  B002 اسم الله في القسم والنداء — يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.

ص م د
  B001 القصد إلى المعتمد المقصود — قصد الشيء واعتماده؛ السيد الذي يقصد إليه في الأمور والحوائج؛ الصمد من جهة الصمود إليه
  B002 الصلابة المكتنزة بلا جوف — الصلابة والاكتناز وانعدام الجوف؛ المكان الصلب أو المرتفع الغليظ؛ الصخرة الراسية والأرض الشديدة
  B003 سدادة القارورة المحكمة — الصماد بمعنى عفاص القارورة أو سدادها؛ فعل صمد القارورة أي جعل لها صمادا
  B004 شد الرأس بصماد — تصميد الرأس بخرقة أو منديل أو ثوب دون العمامة
  B005 الإشراف على الأمر مع الحفل به — قولهم على صمادة من أمر لمن أشرف عليه وحفل به
  B006 إيقاع الضرب بالعصا — صمده بالعصا بمعنى ضربه بها
  B007 الدوام والبقاء على الشدة — الدوام والبقاء؛ الناقة المصماد الباقية على القر والجدب الدائمة الرسل

ق و ل
  B001 إخراج القول بالنطق — يدخل فيه قال يقول قولا، والقول والقيل، والكلام المركب من الحروف إذا أبرز بالنطق، مفردا كان أو جملة أو قصيدة أو خطبة.
  B002 اللسان آلة القول — يدخل فيه المقول بمعنى اللسان.
  B003 كثرة القول في صاحبه — يدخل فيه قولة وقوال وقوالة وتقوالة وقؤول ومقوال ومقول إذا وصفت الإنسان بأنه لسن أو كثير القول أو منطيق.
  B004 القيل صاحب القول النافذ — يدخل فيه المقول أو القيل بلغة أهل اليمن، والواحد القيل، والجمع المقاولة والأقيال والأقوال، وملك حمير دون الملك الأعظم، والمرأة قيلة.
  B005 قول ما لم يكن أو نسبته — يدخل فيه تقول باطلا، وتقول عليه أي كذب عليه، وقولتني أو أقولتني ما لم أقل.
  B006 اجترار القول إلى النفس — يدخل فيه اقتال قولا إذا اجتر إلى نفسه قولا من خير أو شر.
  B007 القول الفاشي بين الناس — يدخل فيه القالة الحسنة أو القبيحة المنتشرة في الناس، وكثرة قالة الناس، والقيل والقال بوصفهما حديثا دائرا.
  B008 عود القال لضرب القلة — يدخل فيه القال، الخشبة التي تضرب بها القلة.
  B009 المقاولة في الأمر — يدخل فيه قاولته في أمره وتقاولنا إذا تفاوضنا.
  B010 اقتالة الحكم على غيره — يدخل فيه اقتال عليه إذا كان بمعنى تحكم.
  B011 قول يجري مجرى الظن — يدخل فيه تقول إذا أجري مجرى تظن في العمل، وخاصة في الاستفهام، وما ذكر عن بني سليم من إجراء متصرف قلت مجرى الظن في غير الاستفهام.
  B012 قول في النفس لم يظهر — يدخل فيه المتصور في النفس قبل الإبراز باللفظ، كما في قول في نفسي لم أظهره.
  B013 القول اعتقاد ومذهب — يدخل فيه القول بمعنى الاعتقاد، نحو فلان يقول بقول أبي حنيفة.
  B014 قول الشيء دلالته — يدخل فيه القول للدلالة على الشيء، مثل امتلأ الحوض وقال قطني.
  B015 العناية الصادقة بالشيء — يدخل فيه فلان يقول بكذا إذا كان معناه العناية الصادقة بالشيء.
  B016 قول الشيء حده — يدخل فيه استعمال المنطقيين القول بمعنى الحد، كقول الجوهر وقول العرض أي حدهما.

ك ف ء
  B001 المماثلة والمقابلة بالمثل — يدخل فيه الكفء والمثل والنظير؛ التساوي والتكافؤ؛ الكفاءة في المناكحة والحرب والمضادة؛ المكافأة والمجازاة بالمثل؛ المقابلة والموالاة بين شيئين
  B002 الإمالة والقلب والصرف — يدخل فيه إمالة الشيء وقلبه وكبه؛ إمالة القوس والصحفة؛ صرف القوم عن وجهتهم؛ التمايل في المشي أو كالسفينة؛ انكسار الوجه وتغير اللون
  B003 اختلاف القوافي — يدخل فيه الإكفاء في الشعر باختلاف القوافي في الحروف أو الحركات أو الإعراب
  B004 كِفاء الخباء — يدخل فيه الكِفاء بمعنى شقة أو شقتين تخاطان ويجعل بهما مؤخر الخباء أو البيت
  B005 كفأة السنة والنتاج — يدخل فيه الكفأة لحمل النخلة أو نتاج الإبل سنة؛ سؤال نتاج الإبل أو ثمر النخل سنة؛ إعطاء اللبن والوبر والأولاد سنة؛ جعل الإبل كفأتين يتناوب نتاجهما

ك و ن
  B001 وقوع الشيء وحضوره في زمان — يدخل فيه وقوع الشيء وحضوره وحدوثه في زمان ماض أو راهن، ومصدر كان والكينونة والكائنة، واستعمال كان خبرا أو توكيدا أو في الاستثناء.
  B002 المكان والمكانة من الكون — يدخل فيه المكان والموضع والمكانة والمنزلة والتمكن إذا جعلت من كان يكون.
  B003 الكفالة والقيام على فلان — يدخل فيه الكيانة والكفالة والتكفل بفلان واكتنت به.
  B004 الخضوع بالاستكانة — يدخل فيه الاستكانة بمعنى الخضوع.
  B005 الشيخ المنسوب إلى كُنْتُ — يدخل فيه الكُنْتِيّ للرجل إذا شاخ كأنه نسب إلى قوله كُنْتُ في شبابي.
  B006 حالة السوء بكينة — يدخل فيه قولهم بات فلان بكينة سوء أي بحال سوء إذا جعلت الكينة فعلة من الكون.

و ل د
  B001 مولود من نسل — يدخل فيه الولد والمولود والابن والابنة والأولاد، ويستعمل للواحد والجمع وللصغير والكبير وللذكر والأنثى بحسب نصوص المصادر.
  B002 أبوان من جهة الولادة — يدخل فيه الوالد بمعنى الأب، والوالدة بمعنى الأم، والوالدان للأب والأم.
  B003 حدوث الولادة ووضع الحمل — يدخل فيه ولدت المرأة، والولادة بوضع الوالدة ولدها، وما قرب من وقت الولادة أو حان ولاده في أولدت، وولادة الحيوان إذا نصت المصادر عليها.
  B004 صغير قريب العهد بالولادة أو مملوك — يدخل فيه الوليد للصبي أو الغلام القريب العهد بالولادة، والوليدة للصبية أو الأمة، وما جمعه ولدان أو ولائد بحسب النص.
  B005 شيء حاصل عن شيء أو مستحدث منه — يدخل فيه تولد الشيء من الشيء إذا حصل عنه بسبب، والمولد من الكلام إذا استحدث، وما كان غير محض أو ناشئا في بيئة معينة مثل عربية مولدة ورجل مولد.
  B006 قرين في سن الولادة — يدخل فيه اللدة أو لدة الرجل بمعنى تربه ومثيله في السن.
```

## Sweep conventions

Lexical sweep count: 62 occurrence × branch seeds. The sweep starts with the first rooted word, `112:1:1 قُلْ`.

`V=all` means that the seed pass visited all S112 root dossiers as continuous prose: قول، ءله، ءحد، صمد، ولد، كون، كفء. Selected branches are only the branches that transformed, completed, or forked the image before freeze.

For compact rows:

- `G` = generating set before freeze.
- `F` = frozen model.
- `P` = predictions at freeze.
- `U` = unused features tested after freeze.
- `C` = corroboration after freeze.
- `K` = constraint, narrowing, or defeat after freeze.
- `R` = rival forks.

## Lexical seed sweep

### 112:1:1 قُلْ — root قول

| Seed | Image, generation, freeze, and testing | Grade |
| --- | --- | --- |
| 112:1:1 قول B001 | Initial image: an utterance is brought out by commanded النطق. `V=all`; selected `(E: قول B001)`, `(E: attachment 112:1 a1 quoted_complement)`, `(E: ءله B002 divine-name dimension)`, `(E: ءحد B001 unity)`, `(E: صمد B001 intended/reliable support)`. `G`: قُلْ opens an exposed utterance whose quote names and predicates the referent. `F`: commanded declarative identity frame: a voice is instructed to disclose "هُوَ ٱللَّهُ أَحَدٌ / ٱللَّهُ ٱلصَّمَدُ". `P`: later material should protect the named oneness from genealogy, dependence, and comparable counterpart. `U`: ولد forms, كون, كفء, final أحد, triple لم, final attachment rows, basmala opening context. `C`: `(C: ولد B003 after-freeze, both active and passive forms negated by لم)`, `(C: كفء B001 after-freeze, equality denied)`, `(C: ءحد B002 after-freeze, final negative-scope أحد)`, `(C: sequence first أحد → final أحد reactivation)`, `(C: basmala opening-context contains اللَّه before the commanded quote)`. `K`: `(K: قُلْ remains a speech-command; no unsupplied non-speech event is introduced)`. `R`: none. | strong — the seed is locally exact, controls the quote structure, predicts the later blocks, and is independently reactivated at closure. |
| 112:1:1 قول B002 | Initial image: the tongue as speech instrument. `V=all`; selected none beyond the rooted word. `G`: tongue/instrument branch. `F`: possible bodily speech instrument. `P`: would expect an organ/instrument role. `U`: all remaining words, morphology, attachments. `C`: none specific. `K`: `(K: attachment 112:1 a1 makes the local role a quoted complement, not an organ scene)`. `R`: none. | unlikely — instrument imagery has no passage-local complement. |
| 112:1:1 قول B003 | Initial image: a person characterized by abundant speech. `V=all`; selected none. `G`: كثرة القول. `F`: loquacity/speaker-quality image. `P`: would expect repeated speaker description or much-saying. `U`: all. `C`: none. `K`: `(K: single imperative قُلْ plus compact quote; no كثرة القول role)`. `R`: none. | unlikely — the passage has a commanded utterance, not a talkative person. |
| 112:1:1 قول B004 | Initial image: authoritative قيل / صاحب قول نافذ. `V=all`; selected `(E: attachment 112:1 a1 quoted_complement)` only as speech frame. `G`: possible authority of speech. `F`: command transmits a high-authority declaration. `P`: expected authority markers. `U`: divine name, predicates, negations. `C`: `(C: ءله B002 name after freeze)` weakly supports high declaration. `K`: no local Yemenite title, ruler, or صاحب القول lexical role. `R`: none. | weak — authority can be inferred from command and content, but the branch-specific scene is absent. |
| 112:1:1 قول B005 | Initial image: saying what was not / false attribution. `V=all`; selected none. `G`: false-saying possibility. `F`: rejected misattribution image. `P`: would expect denial of false quote. `U`: remaining declaration. `C`: none. `K`: `(K: قُلْ is syntactically commanded; no تكذيب or quoted denial of the command is supplied)`. `R`: none. | unlikely — the branch is defeated by the local command frame. |
| 112:1:1 قول B006 | Initial image: drawing a saying into oneself. `V=all`; selected `(E: قول B012 internal-saying dimension)` as a rival internal fork only. `G`: inward appropriation of قول. `F`: interiorized saying. `P`: would expect private interior speech. `U`: quote complement and overt sequence. `C`: none. `K`: `(K: attachment 112:1 a1 and imperative surface make the قول outward, not hidden or merely self-directed)`. `R`: internal-speech fork with B012, both terminated. | unlikely — the passage immediately externalizes the utterance. |
| 112:1:1 قول B007 | Initial image: saying spread among people. `V=all`; selected `(E: قول B001 utterance)` only as prerequisite. `G`: potentially public circulation of the declaration. `F`: a saying capable of spreading. `P`: would expect people/social circulation. `U`: all later features. `C`: none specific. `K`: no الناس, report-circulation, or قال/قيل social scene; the quote is compact. `R`: none. | weak — public recitation may be compatible, but the branch itself is not locally built. |
| 112:1:1 قول B008 | Initial image: stick used for قلة. `V=all`; selected none. `G`: striking-stick object. `F`: object scene. `P`: would expect play/strike/object roles. `U`: all. `C`: none. `K`: no stick, striking target, or game construction. `R`: none. | unlikely — no passage-local complement. |
| 112:1:1 قول B009 | Initial image: mutual negotiation over an affair. `V=all`; selected `(E: قول B001 speech)` as speech substrate. `G`: possible dialogue/negotiation. `F`: negotiated exchange image. `P`: would expect reciprocal parties or issue negotiation. `U`: quote content and later predicates. `C`: none. `K`: `(K: 112:1 a1 quoted_complement is one-directional command+quote, not تقاولنا)`. `R`: none. | weak — speech exists, but reciprocity does not. |
| 112:1:1 قول B010 | Initial image: imposing judgment on another. `V=all`; selected none. `G`: تحكم branch. `F`: arbitrary ruling image. `P`: would expect governed human/object of judgment. `U`: all. `C`: none. `K`: quote content is nominal divine identity, not تحكم على غيره. `R`: none. | unlikely. |
| 112:1:1 قول B011 | Initial image: قول functioning like ظن. `V=all`; selected none. `G`: conjectural saying. `F`: suspicion/thought-governed image. `P`: would expect ظن-like syntax or uncertainty. `U`: all. `C`: none. `K`: no interrogative or ظن-like object structure; the quote is asserted. `R`: none. | unlikely. |
| 112:1:1 قول B012 | Initial image: saying in the self before appearing. `V=all`; selected `(E: قول B001)` only to form the outward-vs-inward contrast. `G`: hidden قول. `F`: hidden content forced outward by قُلْ. `P`: if viable, the quote should be explicit. `U`: attachment and quote. `C`: `(C: attachment 112:1 a1)` confirms explicit quote but also defeats hiddenness. `K`: `(K: the occurrence is imperative outward speech, so hidden قول is only a contrastive pre-image)`. `R`: internal fork with B006 terminated. | weak — useful as contrast with externalization, not as a stable synthesis. |
| 112:1:1 قول B013 | Initial image: قول as اعتقاد ومذهب. `V=all`; selected `(E: قول B001 uttered quote)`, `(E: ءله B002 name)`, `(E: ءحد B001 unity)`, `(E: صمد B001)` before freeze. `G`: a spoken declaration that also has belief-content geometry. `F`: compact doctrinal assertion by quoted predicates. `P`: later lines should protect the asserted content from incompatible relational alternatives. `U`: ولد, كون, كفء, final أحد, negation chain. `C`: `(C: ولد B003 negated active/passive)`, `(C: كفء B001)`, `(C: ءحد B002 final negative-scope closure)`. `K`: the local verb is still imperative speech, not an abstract madhhab noun. `R`: none. | medium — passage-wide fit is good, but the occurrence’s immediate form is plain قُلْ. |
| 112:1:1 قول B014 | Initial image: a thing “says” by indication. `V=all`; selected `(E: ءحد B001)`, `(E: صمد B001)` only as indicated predicates. `G`: indication rather than utterance. `F`: the quote as a sign-like definition. `P`: would expect predicates to delimit the referent. `U`: negations and final equal-denial. `C`: `(C: كفء B001 denied as boundary condition)` weakly supports delimitation. `K`: actual occurrence is direct imperative utterance, not nonverbal indication. `R`: merges weakly with B016 definition fork. | weak — the passage can delimit, but the branch-specific nonverbal indication is not local. |
| 112:1:1 قول B015 | Initial image: truthful/serious care for a thing. `V=all`; selected `(E: قول B001)` only. `G`: careful saying. `F`: earnest declaration. `P`: would expect maintained focus. `U`: all. `C`: compact repetition of اللَّه and closure by أحد weakly fit care. `K`: no explicit عناية construction. `R`: none. | weak — affective attention is not structurally required. |
| 112:1:1 قول B016 | Initial image: قول as حدّ/definition. `V=all`; selected `(E: attachment 112:1 a1)`, `(E: ءله B002)`, `(E: ءحد B001)`, `(E: صمد B001)`. `G`: utterance becomes delimiting definition. `F`: a definition-like model: named referent is bounded positively by أحد/الصمد and then negatively by what cannot attach to it. `P`: unused material should add boundary conditions. `U`: ولد, كون, كفء, final أحد. `C`: `(C: ولد B003 active/passive negated)`, `(C: كون B001 negated occurrence)`, `(C: كفء B001 denied)`, `(C: ءحد B002 final negative-scope closure)`. `K`: branch is specialized and not the ordinary local value of قُلْ. `R`: weak B014 indication fork. | medium-strong — the whole passage behaves like a bounded definition, though the seed branch is form-remote. |

### 112:1:3 ٱللَّهُ — root ءله, first occurrence

| Seed | Image, generation, freeze, and testing | Grade |
| --- | --- | --- |
| 112:1:3 ءله B001 | Initial image: المعبود / object of تأله. `V=all`; selected `(E: ءله B001)`, `(E: attachment 112:1 a3 apposition to هُوَ)`, `(E: ءحد B001)`, `(E: صمد B001)`. `G`: named divine referent occupies the quote’s identity slot. `F`: the referent of هُوَ is the one to whom قصد/اعتماد can be directed and who is marked أحد. `P`: later material should prevent sharing of divine relation by offspring, origin, or equal. `U`: second اللَّه, ولد, كون, كفء, final أحد, basmala. `C`: `(C: repetition 112:2 ٱللَّهُ reactivates the named subject)`, `(C: ولد B003 negated)`, `(C: كفء B001 denied)`, `(C: basmala opening-context divine name)`. `K`: no worship-act syntax occurs; التعبد is a lexical background, not a local event. `R`: none. | medium-strong — strong identity fit, with a constraint against reading a ritual action into the verse. |
| 112:1:3 ءله B002 | Initial image: اسم الله in voiced formulas. `V=all`; selected `(E: قول B001)`, `(E: attachment 112:1 a1)`, `(E: ءله B002)`, `(E: ءحد B001)`. `G`: commanded utterance carries the divine name. `F`: name-disclosure frame: قُلْ exposes the name, and the first predicate attaches uniqueness. `P`: name should be restated or bounded by predicates. `U`: second اللَّه, الصمد, negations, final equal-denial, opening context. `C`: `(C: 112:2 repetition of ٱللَّهُ)`, `(C: صمد B001 as second predicate)`, `(C: final كفء B001 + ءحد B002 denies counterpart)`, `(C: basmala opening-context contains اللَّه)`. `K`: branch examples include oath/appeal forms; S112 uses nominative quoted naming, not oath syntax. `R`: none. | strong — name plus speech-frame plus repetition gives a clear temporal reactivation path. |

### 112:1:4 أَحَدٌ — root ءحد, first occurrence

| Seed | Image, generation, freeze, and testing | Grade |
| --- | --- | --- |
| 112:1:4 ءحد B001 | Initial image: الأَحَدِيَّة والوَحْدَة. `V=all`; selected `(E: ءحد B001)`, `(E: attachment 112:1 a2 predication)`, `(E: ءله B002 name)`, `(E: صمد B001)` and optional secondary `(E: صمد B002 self-contained image)`. `G`: named subject receives unity predicate, then صمد adds self-standing/reliable density. `F`: one named referent, positively bounded by أحد and الصمد. `P`: later material should block routes by which plurality, derivation, dependence, or peerhood would enter. `U`: ولد active/passive, كون, كفء, final أحد, لم repetition. `C`: `(C: ولد B003 after-freeze, generation blocked in both directions)`, `(C: ولد B005 after-freeze, حاصل عن شيء blocked by passive negation)`, `(C: كفء B001 after-freeze, equality denied)`, `(C: ءحد B002 after-freeze, final أحد in negation reactivates first أحد)`, `(C: sequence 112:1→112:4 ring closure)`. `K`: `(K: first أَحَدٌ is positive nominative predicate, not itself negative-scope أحد)`. `R`: صمد B001 reliance fork and صمد B002 self-contained fork converge. | strong — this is the main temporal reactivation: first أحد is reinterpreted at the final أحد. |
| 112:1:4 ءحد B002 | Initial image: أحد under negation with exhaustive scope. `V=all`; selected none before freeze because 112:1:4 is positive. `G`: negative-scope branch attempted from a positive predicate. `F`: branch waits unresolved. `P`: if the root recurs under negation, it may reactivate. `U`: final أحد and final negated copula. `C`: `(C: 112:4 final أَحَدٌ appears under وَلَمْ يَكُن with كُفُوًا)`. `K`: `(K: occurrence 112:1:4 is not in a negative environment; attachment 112:1 a2 makes it positive predicate)`. `R`: none. | weak — useful only by later root recurrence; the seed’s own occurrence is constrained. |
| 112:1:4 ءحد B003 | Initial image: one in counting/composition. `V=all`; selected none. `G`: numeric/composite one. `F`: counting image. `P`: would expect numerals or compound count. `U`: all. `C`: none. `K`: no عشر or counting construction; predicate is identity/quality. `R`: none. | unlikely. |
| 112:1:4 ءحد B004 | Initial image: first/additive أحد or Sunday. `V=all`; selected none. `G`: ordinal/additive branch. `F`: first/day image. `P`: would expect إضافة or calendrical marker. `U`: all. `C`: none. `K`: no إضافة or day-name construction. `R`: none. | unlikely. |
| 112:1:4 ءحد B005 | Initial image: انفراد and coming as individuals. `V=all`; selected `(E: ءحد B001)` as close unity neighbor, `(E: صمد B001)` weakly. `G`: solitary singularity. `F`: individual non-shared standing. `P`: later text should reject pair/peer relations. `U`: ولد, كفء, final أحد. `C`: `(C: كفء B001 equality denied)`, `(C: final ءحد B002 no-any-one scope)`. `K`: no آحادا/plural-distribution construction. `R`: converges into B001 but weaker. | medium — the separation image fits the closure, but branch-specific plurality/distribution is absent. |
| 112:1:4 ءحد B006 | Initial image: جبل أُحُد. `V=all`; selected none. `G`: proper mountain name. `F`: place-name image. `P`: would expect geographic marker. `U`: all. `C`: none. `K`: no place, mountain, or المدينة cue. `R`: none. | unlikely. |

### 112:2:1 ٱللَّهُ — root ءله, second occurrence

| Seed | Image, generation, freeze, and testing | Grade |
| --- | --- | --- |
| 112:2:1 ءله B001 | Initial image: المعبود / divine object. `V=all`; selected `(E: ءله B001)`, `(E: repetition of ٱللَّهُ after 112:1)`, `(E: صمد B001)`, `(E: ءحد B001 prior-state reactivation)`. `G`: the name is repeated to carry a second predicate. `F`: the named referent is not exhausted by first أحد; it is re-presented as الصمد. `P`: later lines should remove dependence and counterpart relations. `U`: ولد, كون, كفء, final أحد. `C`: `(C: ولد B003 and B005 negated)`, `(C: كفء B001 denied)`, `(C: final ءحد B002)`. `K`: no worship-act syntax. `R`: none. | medium-strong — the second occurrence strongly reactivates the first named subject. |
| 112:2:1 ءله B002 | Initial image: divine name as formulaic Name. `V=all`; selected `(E: ءله B002)`, `(E: sequence repetition 112:1→112:2)`, `(E: صمد B001)`. `G`: Name repeated at ayah opening. `F`: re-naming before the صمد predicate, creating a second activation of the same referent. `P`: subsequent negations should apply to this reactivated referent. `U`: ولد, كون, كفء, final أحد. `C`: `(C: 112:3–4 pronoun/verbs continue 3MS reference)`, `(C: كفء B001 له complement points back to the named referent)`. `K`: not oath/نداء syntax. `R`: none. | strong — repetition plus predicate transition creates a clear temporary-state refresh. |

### 112:2:2 ٱلصَّمَدُ — root صمد

| Seed | Image, generation, freeze, and testing | Grade |
| --- | --- | --- |
| 112:2:2 صمد B001 | Initial image: القصد إلى المعتمد المقصود. `V=all`; selected `(E: صمد B001)`, `(E: attachment 112:2 a1 predication)`, `(E: ءله B002 repeated Name)`, `(E: ءحد B001 prior unity)`. `G`: the one named Allah is the intended/reliable recourse. `F`: a single named support-center, already one, now the one toward whom قصد/اعتماد is directed. `P`: such a center should not be explained by parentage, production, temporal origination, or equal counterpart. `U`: ولد active/passive, كون, كفء, final أحد, negation chain. `C`: `(C: ولد B002/B003 after-freeze: parent/birth relation denied)`, `(C: ولد B005 after-freeze: حاصل عن شيء denied by passive يولد)`, `(C: كفء B001 after-freeze: no equal support-counterpart)`, `(C: كون B001 after-freeze: negated occurrence of equal)`, `(C: final ءحد B002)`. `K`: no human request scene or حاجات nouns are locally supplied; the branch contributes relational support, not a full supplication scene. `R`: B002 self-contained fork converges but stays secondary. | strong — role completion is high: ṣمد predicts the dependence-removal sequence. |
| 112:2:2 صمد B002 | Initial image: الصلابة المكتنزة بلا جوف. `V=all`; selected `(E: صمد B002)`, `(E: ءحد B001)`, `(E: صمد B007 permanence as optional fork)`. `G`: one dense, non-hollow, self-contained image. `F`: compact self-contained referent whose interior does not open into a generative cavity. `P`: later material should block birth/opening/origin relations and peer equivalence. `U`: ولد, كون, كفء, final أحد. `C`: `(C: ولد B003 active/passive negated)`, `(C: ولد B005 generated-from relation denied)`, `(C: كفء B001 denied)`, `(C: triple لم locks out relational openings)`. `K`: `(K: الصمد is a predicate of ٱللَّهُ; no literal rock, place, or جسم role is supplied)`. `R`: B001 reliance fork is primary; B002 remains secondary simulation. | medium-strong — vivid and predictive, but must be kept subordinate to the predicate syntax. |
| 112:2:2 صمد B003 | Initial image: tight bottle stopper/seal. `V=all`; selected `(E: صمد B002 no-hollow neighbor)` as a weak fork. `G`: sealed closure. `F`: a closed vessel/blocked opening image. `P`: would expect no outgoing/incoming production. `U`: ولد active/passive and equality closure. `C`: `(C: ولد B003 negated)` weakly fits blocked opening. `K`: no bottle, stopper, container, or عفاص role in the text. `R`: collapses into B002 if retained. | weak — a possible local metaphor of closure, but branch-specific objects are absent. |
| 112:2:2 صمد B004 | Initial image: wrapping/binding the head with صماد. `V=all`; selected none. `G`: head-bandage image. `F`: bound-head object scene. `P`: would expect head, cloth, wrapping. `U`: all. `C`: none. `K`: no head or binding construction. `R`: none. | unlikely. |
| 112:2:2 صمد B005 | Initial image: overseeing an affair with care. `V=all`; selected `(E: ءله B001)` weakly as high referent. `G`: supervisory attention. `F`: one presiding over an affair. `P`: would expect أمر or managed object. `U`: all later negations. `C`: none specific. `K`: no أمر/care construction; later text negates relations rather than narrating oversight. `R`: none. | weak. |
| 112:2:2 صمد B006 | Initial image: striking with a stick. `V=all`; selected none. `G`: blow-event. `F`: impact scene. `P`: would expect striker/instrument/target. `U`: all. `C`: none. `K`: no ضرب, عصا, target, or wound role. `R`: none. | unlikely. |
| 112:2:2 صمد B007 | Initial image: الدوام والبقاء على الشدة. `V=all`; selected `(E: صمد B001)` and `(E: ءحد B001)` as support/singularity. `G`: enduring, remaining through severity. `F`: stable persistence of the named one. `P`: later text should resist temporal origination and dependent becoming. `U`: ولد passive, كون, كفء. `C`: `(C: ولد B005 generated-from denied)`, `(C: كون B001 negated occurrence of equal)`, `(C: triple لم repeated non-occurrence)`. `K`: no hardship/جدب scene is explicit. `R`: supports B001/B002 but does not replace them. | medium — strong temporal fit with negated becoming, weaker branch-specific scenery. |

### 112:3:2 يَلِدْ — root ولد, active occurrence

| Seed | Image, generation, freeze, and testing | Grade |
| --- | --- | --- |
| 112:3:2 ولد B001 | Initial image: مولود من نسل / product-child role. `V=all`; selected `(E: ولد B001 product role)`, `(E: ولد B003 birth-event)`, `(E: attachment 112:3 a1 negated jussive active)`, `(E: ءحد B001 prior unity)`. `G`: a possible outgoing child/product role is immediately blocked by لم. `F`: no offspring/product can proceed from the named one. `P`: companion passive should block reverse genealogy; final line should block peerhood. `U`: يولد passive, كون, كفء, final أحد. `C`: `(C: ولد B003 passive occurrence coordinated after-freeze)`, `(C: ولد B002 parent roles denied by active/passive pair)`, `(C: كفء B001 denied)`, `(C: final ءحد B002)`. `K`: no positive child role remains; the image is a negated relation, not a generated participant. `R`: causal-generation fork B005. | strong — the active negation builds one half of a symmetric generation block. |
| 112:3:2 ولد B002 | Initial image: والد/والدة parent roles. `V=all`; selected `(E: ولد B002)`, `(E: ولد B003)`, `(E: attachment 112:3 a1 لم يلد)`. `G`: active birth would assign parenthood; negation prevents it. `F`: no parent-role can attach to the named referent through active يلد. `P`: passive negation should deny parents over Him; final should deny equal. `U`: يولد, كفء, final أحد. `C`: `(C: passive يولد denies parent relation over the referent)`, `(C: كفء B001 no peer/equal)`. `K`: B002 is role-inferred from يلد, not an overt والد noun. `R`: B001/B003 converge. | medium-strong — role completion is good but derivative. |
| 112:3:2 ولد B003 | Initial image: حدوث الولادة ووضع الحمل. `V=all`; selected `(E: ولد B003)`, `(E: attachment 112:3 a1 negated active)`, `(E: attachment 112:3 a2 coordination to passive)`. `G`: birth-event branch is invoked only to be blocked. `F`: a two-direction birth-gate closure begins: no outgoing الولادة relation. `P`: passive member should close incoming origin; equality should then be denied. `U`: passive يولد, final كفء/أحد, كون. `C`: `(C: passive ولد B003 after-freeze completes incoming closure)`, `(C: كفء B001 denied after generation closure)`, `(C: كون B001 negated being of equal)`. `K`: morphology is negated jussive; no actual birth event is asserted. `R`: B005 broad generation fork. | strong — direct root/form match and strong sequence prediction. |
| 112:3:2 ولد B004 | Initial image: newborn/young/slave. `V=all`; selected none. `G`: الوليد branch. `F`: newborn/servant image. `P`: would expect young child or مملوك role. `U`: all. `C`: none. `K`: text has verb يلد under negation, not وليد noun or ownership scene. `R`: none. | unlikely. |
| 112:3:2 ولد B005 | Initial image: something obtained/generated from something. `V=all`; selected `(E: ولد B005)`, `(E: ولد B003 active event)`, `(E: ءحد B001 prior unity)`, `(E: صمد B001/B002 prior self-standing support)`. `G`: causal production from the referent is blocked. `F`: no derivative thing comes out from Him as generated effect. `P`: passive line should deny His derivation from something; final should deny a counterpart product. `U`: يولد passive, كفء, final أحد. `C`: `(C: passive يولد denies generated-from relation in reverse)`, `(C: كفء B001 denies equivalent counterpart)`. `K`: branch is broader than the surface verb; keep as secondary to B003. `R`: biological B003 and causal B005 forks converge. | medium-strong — useful abstraction of the birth pair without overriding the local verb. |
| 112:3:2 ولد B006 | Initial image: same-age peer / لدة. `V=all`; selected `(E: كفء B001)` only as later peer-like fork, but not before freeze. `G`: peer-by-age branch attempted. `F`: possible peerhood from birth-time. `P`: would expect equal/peer denial. `U`: final كفء/أحد. `C`: `(C: كفء B001 denies equality)`. `K`: no لدة form or age-comparison appears; يلد is active verb. `R`: merges weakly with final equality model. | weak — final equality helps, but the branch is remote from the occurrence. |

### 112:3:4 يُولَدْ — root ولد, passive occurrence

| Seed | Image, generation, freeze, and testing | Grade |
| --- | --- | --- |
| 112:3:4 ولد B001 | Initial image: مولود من نسل, now as passive. `V=all`; selected `(E: ولد B001)`, `(E: ولد B003)`, `(E: attachment 112:3 a3 negated passive)`, `(E: attachment 112:3 a2 coordination with يلد)`. `G`: the referent is prevented from being a produced offspring. `F`: no incoming lineage or produced-child status. `P`: final should deny equal counterpart after genealogy is closed both ways. `U`: كون, كفء, final أحد. `C`: `(C: كفء B001 denied)`, `(C: كون B001 negated occurrence)`, `(C: final ءحد B002)`. `K`: passive is negated; no offspring role is asserted. `R`: B005 causal-origination fork. | strong — direct passive counterpart to the active negation. |
| 112:3:4 ولد B002 | Initial image: parents from birth relation. `V=all`; selected `(E: ولد B002)`, `(E: ولد B003)`, `(E: passive negated morphology)`. `G`: passive birth would imply parents over the referent; negation blocks them. `F`: no parent-source over the named one. `P`: final should deny any comparable one. `U`: كفء, final أحد. `C`: `(C: كفء B001)`, `(C: final ءحد B002)`. `K`: no والد/والدة nouns occur; the role is inferred from passive يولد. `R`: B001/B003 converge. | medium-strong. |
| 112:3:4 ولد B003 | Initial image: event of birth / وضع حمل, passive. `V=all`; selected `(E: ولد B003)`, `(E: attachment 112:3 a2 coordination)`, `(E: attachment 112:3 a3 passive negation)`. `G`: the birth event is blocked in the incoming direction. `F`: after the active block, the passive block seals the other side of الولادة. `P`: final should move from genealogy to peerhood/equivalence. `U`: كون, كفء, final أحد. `C`: `(C: كفء B001 denied)`, `(C: كون B001 negated existence of equal)`, `(C: final ءحد B002 universal denial)`. `K`: no actual birth event; only the relation’s non-occurrence. `R`: B005 broader generation fork. | strong — temporal sequence and coordination make this a complete closure. |
| 112:3:4 ولد B004 | Initial image: newborn/young/slave. `V=all`; selected none. `G`: الوليد branch. `F`: newborn/servant image. `P`: would expect newborn noun or ownership scene. `U`: all. `C`: none. `K`: passive verb under negation does not supply وليد/وليدة role. `R`: none. | unlikely. |
| 112:3:4 ولد B005 | Initial image: something generated from something. `V=all`; selected `(E: ولد B005)`, `(E: passive negated morphology)`, `(E: صمد B001/B002 prior-state support/self-containedness)`. `G`: derivation of the named referent from another source is blocked. `F`: the referent is not an effect produced from something else. `P`: final should deny the remaining possibility of a counterpart. `U`: كون, كفء, final أحد. `C`: `(C: كفء B001 denied)`, `(C: final ءحد B002)`, `(C: صمد B007 prior permanence can be retrospectively reactivated)`. `K`: broad causal-generation branch must remain secondary to the passive birth form. `R`: biological B003 and causal B005 converge. | medium-strong. |
| 112:3:4 ولد B006 | Initial image: same-age peer. `V=all`; selected none before freeze. `G`: peer through birth-time. `F`: peerhood possibility. `P`: would expect peer/equal denial. `U`: final كفء/أحد. `C`: `(C: كفء B001)` weakly. `K`: no لدة or age parallel; passive يولد is not a peer noun. `R`: weak equality fork. | weak. |

### 112:4:2 يَكُن — root كون

| Seed | Image, generation, freeze, and testing | Grade |
| --- | --- | --- |
| 112:4:2 كون B001 | Initial image: وقوع الشيء وحضوره في زمان. `V=all`; selected `(E: كون B001)`, `(E: attachment 112:4 a1 negated jussive)`, `(E: كفء B001)`, `(E: attachment 112:4 a3 kana_predicate)`, `(E: attachment 112:4 a4 delayed subject أحد)`. `G`: the possible occurrence/existence of an equal is denied. `F`: not merely no birth relation, but no temporal occurrence of any كفء for Him. `P`: final أحد should universalize the denied equal. `U`: final أحد branch distinction and earlier أحد. `C`: `(C: ءحد B002 final negative-scope subject)`, `(C: first ءحد B001 reactivated as positive unity now protected by no-any-one)`, `(C: كفء B001 equality branch)`. `K`: كون is a negated copular support here; it does not create a separate event beyond the equality denial. `R`: none. | strong — final syntax gives it exact role completion. |
| 112:4:2 كون B002 | Initial image: place/status/standing. `V=all`; selected `(E: كفء B001)` weakly as status comparison. `G`: possible rank/place of an equal. `F`: no one occupies matching status for Him. `P`: would expect له complement and equal predicate. `U`: final attachments. `C`: `(C: attachment 112:4 a2 له complement of كفء)`, `(C: attachment 112:4 a3/a4 predicate+subject)`. `K`: no مكان/موضع noun; status is inferred from equality syntax. `R`: folds into B001. | medium — plausible by final syntax, but less exact than B001. |
| 112:4:2 كون B003 | Initial image: الكفالة والقيام على فلان. `V=all`; selected none. `G`: caretaking/kafala image. `F`: caretaker relation. `P`: would expect dependent person. `U`: all final structure. `C`: none. `K`: no كفالة or قيام على construction; له is complement of كفء per attachment. `R`: none. | unlikely. |
| 112:4:2 كون B004 | Initial image: خضوع بالاستكانة. `V=all`; selected none. `G`: submission image. `F`: humbled state. `P`: would expect خضوع or abasement role. `U`: all. `C`: none. `K`: final line denies equality, not submission. `R`: none. | unlikely. |
| 112:4:2 كون B005 | Initial image: old man linked to saying "كنت". `V=all`; selected none. `G`: age/old-man branch. `F`: aging reminiscence image. `P`: would expect age/person marker. `U`: all. `C`: none. `K`: no شيخ or كنت form; occurrence is يَكُن under لم. `R`: none. | unlikely. |
| 112:4:2 كون B006 | Initial image: bad-state كينة سوء. `V=all`; selected none. `G`: bad state. `F`: negative condition image. `P`: would expect سوء/state phrase. `U`: all. `C`: none. `K`: no سوء, بات, or state-quality phrase. `R`: none. | unlikely. |

### 112:4:4 كُفُوًا — root كفء

| Seed | Image, generation, freeze, and testing | Grade |
| --- | --- | --- |
| 112:4:4 كفء B001 | Initial image: المماثلة والمقابلة بالمثل. `V=all`; selected `(E: كفء B001)`, `(E: attachment 112:4 a2 له complement)`, `(E: attachment 112:4 a3 kana_predicate)`, `(E: كون B001 negated occurrence)`, `(E: ءحد B002 delayed subject under negation)`. `G`: equality/counterpart relation is raised and denied. `F`: no matching counterpart exists for the named referent. `P`: should reactivate the first أحد and close the passage at the root of individuality/oneness. `U`: first أحد, prior ولد pair, صمد. `C`: `(C: first ءحد B001 reactivated)`, `(C: ولد B003 active/passive pair already removed genealogy)`, `(C: صمد B001/B002 prior self-standing support)`, `(C: final word position of أحد closes the equality test)`. `K`: none beyond negated syntax; equality is not asserted. `R`: none. | strong — exact local branch, exact final syntax, strong backward replay. |
| 112:4:4 كفء B002 | Initial image: tilting, flipping, turning aside. `V=all`; selected none. `G`: inversion/turning branch. `F`: turned-over image. `P`: would expect motion/inversion or diverted direction. `U`: final syntax. `C`: none. `K`: كُفُوًا is predicate of يَكُن, not a verb of turning. `R`: none. | unlikely. |
| 112:4:4 كفء B003 | Initial image: rhyme discrepancy. `V=all`; selected none. `G`: poetic قافية variation. `F`: sound-pattern mismatch image. `P`: would expect poetry/rhyme evidence. `U`: final sound recurrence. `C`: none specific; final أحد recurrence is root-semantic, not قافية اختلاف. `K`: no شعر or قافية construction. `R`: none. | unlikely. |
| 112:4:4 كفء B004 | Initial image: tent/back-panel كفاء الخباء. `V=all`; selected none. `G`: tent-panel object. `F`: shelter-piece image. `P`: would expect خباء/بيت. `U`: all. `C`: none. `K`: no tent or house. `R`: none. | unlikely. |
| 112:4:4 كفء B005 | Initial image: yearly produce/offspring of palms/camels. `V=all`; selected `(E: ولد B005)` only as a remote production fork. `G`: periodic production. `F`: production/equivalence fork. `P`: would expect نتاج or yearly alternation. `U`: prior ولد pair. `C`: `(C: prior ولد B003/B005 negations)` very weak. `K`: final noun كُفُوًا is equality predicate, not كفأة نتاج. `R`: production fork terminated. | weak — only remote contact with ولد; local form defeats it. |

### 112:4:5 أَحَدٌۢ — root ءحد, final occurrence

| Seed | Image, generation, freeze, and testing | Grade |
| --- | --- | --- |
| 112:4:5 ءحد B001 | Initial image: الأَحَدِيَّة والوَحْدَة at the closing word. `V=all`; selected `(E: ءحد B001)`, `(E: كفء B001)`, `(E: كون B001 negated occurrence)`, `(E: attachment 112:4 a4 delayed subject)`. `G`: an individual/one is placed as delayed subject in a negated equality clause. `F`: the passage closes by letting أحد return, now inside a no-equal structure. `P`: backward replay should connect to 112:1 أَحَدٌ. `U`: first أحد, first predicates, ولد pair. `C`: `(C: first ءحد B001 positive predicate reactivated)`, `(C: ولد B003 pair already prevents lineage plurality)`, `(C: sequence first rooted predicate → final root recurrence)`. `K`: because final occurrence is under negation, B002 is the more exact local branch. `R`: B002 stronger fork. | medium-strong — strong closure, but final syntax favors B002. |
| 112:4:5 ءحد B002 | Initial image: استغراق النفي. `V=all`; selected `(E: ءحد B002)`, `(E: كفء B001)`, `(E: كون B001)`, `(E: attachment 112:4 a4 delayed subject)`, `(E: attachment 112:4 a3 predicate)`. `G`: the delayed subject under negated كان exhausts the class of any possible counterpart. `F`: no one whatsoever is a كفء له. `P`: this should retroactively complete first أحد: the initial unity becomes protected against every comparable individual. `U`: first أحد, صمد, ولد pair, repeated اللَّه. `C`: `(C: first ءحد B001 positive unity reactivated)`, `(C: صمد B001/B002 self-standing center)`, `(C: ولد B003 active/passive genealogy denied before final universalization)`, `(C: repetition/closure final word = أحد)`. `K`: none; this is the exact local environment. `R`: B001 closure fork is included but subordinate. | strong — best final reactivation seed. |
| 112:4:5 ءحد B003 | Initial image: one in counting/composition. `V=all`; selected none. `G`: numeric/compound-count branch. `F`: counting image. `P`: would expect numeric composition. `U`: all. `C`: none. `K`: final أحد is delayed subject under negation, not counting. `R`: none. | unlikely. |
| 112:4:5 ءحد B004 | Initial image: first/addition or Sunday. `V=all`; selected none. `G`: ordinal/day branch. `F`: first/day image. `P`: would expect إضافة/day. `U`: all. `C`: none. `K`: no إضافة or calendrical cue. `R`: none. | unlikely. |
| 112:4:5 ءحد B005 | Initial image: individual separation. `V=all`; selected `(E: ءحد B005)`, `(E: كفء B001)`, `(E: كون B001)`. `G`: no separated individual can stand as equal. `F`: individual-by-individual exclusion of counterpart. `P`: backward replay should support first unity. `U`: first أحد and ولد pair. `C`: `(C: first ءحد B001)`, `(C: ولد active/passive blocks lineage-based individuals)`. `K`: no آحادا or distributive plural form; B002 is more exact. `R`: B002 stronger. | medium — coherent but less syntactically exact than negative-scope B002. |
| 112:4:5 ءحد B006 | Initial image: جبل أُحُد. `V=all`; selected none. `G`: mountain name. `F`: place-name image. `P`: would expect geography. `U`: all. `C`: none. `K`: no mountain/place cue. `R`: none. | unlikely. |

## Constructional, morphosyntactic, and temporal seeds

These seeds are not additional lexical branches. They use only the actual constructions, morphology, attachments, order, repetition, and ayah boundaries in the assigned passage.

| Seed | Image, generation, freeze, and testing | Grade |
| --- | --- | --- |
| C01 quoted-complement frame: `قُلْ` → `هُوَ ٱللَّهُ أَحَدٌ` | Initial image: a command opens a quote. `V=all`; selected `(E: attachment 112:1 a1 quoted_complement)`, `(E: قول B001)`, `(E: ءله B002)`, `(E: ءحد B001)`. `G`: speech act plus quoted identity. `F`: the whole passage is heard as recited content following the initial command. `P`: subsequent ayahs should remain inside the same declared referent. `U`: 112:2–4. `C`: `(C: 112:2 repeats ٱللَّهُ)`, `(C: 3MS verbal/pronominal continuity in يلد/يولد/يكن/له)`, `(C: final أحد closes the quote-content around the first predicate)`. `K`: command itself is not part of the divine predicate chain. `R`: none. | strong — exact attachment and sequence. |
| C02 pronoun-name-predicate cluster: `هُوَ ٱللَّهُ أَحَدٌ` | Initial image: deictic pronoun is filled by the divine name and a nominative predicate. `V=all`; selected `(E: attachment 112:1 a3 apposition)`, `(E: attachment 112:1 a2 predication)`, `(E: ءله B002)`, `(E: ءحد B001)`. `F`: referent focusing: هو → الله → أحد. `P`: later text should keep filling and protecting this same referent. `U`: 112:2–4. `C`: `(C: repeated الله in 112:2)`, `(C: final له pronoun complement points back)`, `(C: final أحد reactivation)`. `K`: apposition row is medium-confidence; predicate relation is stronger. `R`: apposition vs direct nominal reading does not change the synthesis. | strong. |
| C03 two nominal predicates across ayah boundary: `ٱللَّهُ أَحَدٌ` then `ٱللَّهُ ٱلصَّمَدُ` | Initial image: the Name is repeated to accept a second predicate. `V=all`; selected `(E: ءله B002 repeated name)`, `(E: ءحد B001)`, `(E: صمد B001)`, `(E: attachment 112:2 a1 predication)`. `F`: unity is not left abstract; it is thickened into a support/self-standing predicate. `P`: next material should explain what relations cannot attach to this one/support. `U`: ولد pair, final equal-denial. `C`: `(C: active/passive ولد negated)`, `(C: كفء B001 denied)`. `K`: no extra predicate beyond the supplied nouns may be invented. `R`: صمد B002 secondary self-contained fork. | strong. |
| C04 definite/indefinite alternation: `ٱللَّهُ` / `أَحَدٌ` / `ٱلصَّمَدُ` / `كُفُوًا أَحَدٌ` | Initial image: definite Name and definite الصمد are paired with indefinite أحد and كفوا/أحد. `V=all`; selected `(E: morphology definiteness)`, `(E: ءحد B001)`, `(E: صمد B001)`, `(E: كفء B001)`, `(E: ءحد B002 final)`. `F`: a named definite center is bounded by positive uniqueness and final indefinite-exhaustive denial. `P`: final indefinite should widen the denial rather than introduce a named rival. `U`: negation syntax. `C`: `(C: final لم يكن makes the indefinite subject exhaustive through ءحد B002)`. `K`: morphology alone does not define the doctrine; it supports the lexical/syntactic model. `R`: none. | medium-strong. |
| C05 active/passive ولد pair under repeated لم | Initial image: outgoing and incoming الولادة relations are both presented only under negation. `V=all`; selected `(E: ولد B003)`, `(E: ولد B001/B002 role implications)`, `(E: attachment 112:3 a1/a2/a3)`. `F`: generation is closed in both directions around the same 3MS referent. `P`: once lineage is closed, the remaining possible relation to close is peer/equal. `U`: 112:4. `C`: `(C: كفء B001)`, `(C: كون B001)`, `(C: ءحد B002 final universal subject)`. `K`: no positive birth event exists. `R`: B005 causal-generation fork. | strong. |
| C06 triple negation chain: `لَمْ` / `وَلَمْ` / `وَلَمْ` | Initial image: repeated jussive negation moves from active ولد, to passive ولد, to كون of equal. `V=all`; selected `(E: morphology JUS/NEG)`, `(E: ولد B003)`, `(E: كون B001)`, `(E: كفء B001)`. `F`: a three-step exclusion wave: not outgoing-generation, not incoming-generation, not equal-existence. `P`: closure should land on the most general possible subject. `U`: final أحد. `C`: `(C: ءحد B002 final negative scope)`, `(C: word order puts أحد last)`. `K`: the chain is negative structure, not an independent lexical meaning. `R`: none. | strong. |
| C07 final `لم يكن له كفوا أحد` attachment package | Initial image: negated copula, له complement of كفوا, كفوا predicate, delayed أحد subject. `V=all`; selected `(E: attachment 112:4 a1/a2/a3/a4)`, `(E: كون B001)`, `(E: كفء B001)`, `(E: ءحد B002)`. `F`: the final clause denies the occurrence of any equal-for-Him. `P`: it should retrospectively organize first أحد and the ولد negations. `U`: earlier first أحد and birth pair. `C`: `(C: first ءحد B001)`, `(C: ولد B003 active/passive closure)`, `(C: صمد B001 self-standing predicate)`. `K`: equality is denied, not asserted. `R`: none. | strong. |
| C08 root recurrence ring: first `أَحَدٌ` → final `أَحَدٌ` | Initial image: the same root appears first as positive predicate and last as negative-scope delayed subject. `V=all`; selected `(E: ءحد B001 first)`, `(E: ءحد B002 final)`, `(E: sequence boundary first predicate/final word)`. `F`: temporal ring: first unity is reactivated and universalized by final no-any-one. `P`: middle material should explain why the final reactivation is needed. `U`: الصمد and ولد/كفء. `C`: `(C: صمد B001/B002 gives self-standing center)`, `(C: ولد pair blocks genealogy)`, `(C: كفء B001 makes final أحد a counterpart-denial)`. `K`: first and final occurrences are not identical syntactically; the contrast is the point. `R`: none. | strong. |
| C09 repeated divine Name at ayah boundary: `ٱللَّهُ` / `ٱللَّهُ` | Initial image: the name is stated, then restated before the second predicate. `V=all`; selected `(E: ءله B002)`, `(E: sequence repetition)`, `(E: ءحد B001)`, `(E: صمد B001)`. `F`: a referent-refresh before the صمد predicate. `P`: subsequent third-person forms should continue that referent. `U`: 112:3–4. `C`: `(C: 3MS verbs يلد/يولد/يكن)`, `(C: له complement in final clause)`. `K`: not oath/نداء syntax. `R`: none. | medium-strong. |
| C10 ayah-boundary progression | Initial image: each ayah adds one layer: command/identity, support/self-standing predicate, genealogy negation, equal-existence negation. `V=all`; selected `(E: sequence 112:1→112:4)`, `(E: قول B001)`, `(E: ءحد B001)`, `(E: صمد B001)`, `(E: ولد B003)`, `(E: كفء B001)`. `F`: ordered exclusion model. `P`: closure should be last because equality denial is broader than lineage denial. `U`: final أحد. `C`: `(C: final ءحد B002)`, `(C: word order delayed subject)`. `K`: sequence alone cannot supply lexical content; it organizes the branch-supported content. `R`: none. | strong. |
| C11 opening-context check, not a seed | The basmala contains اللَّه before the assigned passage. It is not used to generate a model. It is tested after freeze in the قول/ءله name-frame seeds only. `C`: `(C: basmala opening-context, divine-name activation before قُلْ)`. `K`: no basmala root initiates a lexical seed; no رحمن/رحيم branch is imported. | not graded as seed — opening-context corroboration only. |

## Convergence summary

Strong or medium-strong seeds converge on one compact relational model:

```text
commanded utterance
  → named referent
  → positive unity
  → صمد support / self-standing density
  → no outgoing الولادة
  → no incoming الولادة
  → no occurrence of any equal-for-Him
  → final أحد reactivates first أحد under exhaustive negation
```

The strongest generators are `(E: قول B001)`, `(E: ءله B002)`, `(E: ءحد B001 first occurrence)`, `(E: صمد B001)`, `(E: ولد B003 active/passive)`, `(E: كون B001)`, `(E: كفء B001)`, and `(E: ءحد B002 final occurrence)`.

The strongest independent corroborators after freeze are the active/passive ولد pair, the final كفء equality branch, the negated كون construction, and the recurrence of أحد in a different syntactic environment. The principal constraints are equally important: `قُلْ` remains a quoted speech command; `الصمد` remains a predicate of ٱللَّهُ and not a literal rock, stopper, or body; `ولد` relations are negated rather than asserted; and final equality is denied rather than introduced.

Very short interpretation: the passage produces a temporal reactivation in which the first positive `أَحَدٌ` is held in memory, thickened by `ٱلصَّمَدُ`, protected by the two-direction ولد negation, and finally reactivated at the closing `أَحَدٌۢ` as an exhaustive denial of any equal counterpart.
