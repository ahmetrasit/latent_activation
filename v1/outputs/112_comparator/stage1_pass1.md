# Stage 1 Pass 1 — S112 comparator main lane

Assigned passage: S112, ayat 1–4. Opening context in the sacred text file: `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`. QAC returned no S112 ayah-0 rows, so no basmala root branches were used and no basmala seed was initiated.

Main sacred Arabic sequence:

```text
112:1 قُلْ هُوَ ٱللَّهُ أَحَدٌ
112:2 ٱللَّهُ ٱلصَّمَدُ
112:3 لَمْ يَلِدْ وَلَمْ يُولَدْ
112:4 وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ
```

## Resource audit

Permitted resources used:

- `resources/quran/surah_112.json`
- `v1/prompts/stage1.md`
- `resources/qac.sqlite`, schemas inspected; S112 ayat 1–4 words and morphemes only
- `resources/attachments.tsv`, header and S112 ayat 1–4 rows only
- `resources/furuq_v4.sqlite`, schema inspected; uncontaminated branch images only for roots in S112 ayat 1–4

No translations, tafsir, hadith, web sources, or other outputs were read.

## QAC main-lane sequence

| Ref | Surface | Root | Lemma | Morphology |
| --- | --- | --- | --- | --- |
| 112:1:1 | قُلْ | قول | قَالَ | V, imperative, 2MS |
| 112:1:2 | هُوَ | — | — | PRON, 3MS |
| 112:1:3 | ٱللَّهُ | ءله | ٱللَّه | PN, nominative |
| 112:1:4 | أَحَدٌ | ءحد | أَحَد | N, masculine, indefinite, nominative |
| 112:2:1 | ٱللَّهُ | ءله | ٱللَّه | PN, nominative |
| 112:2:2 | ٱلصَّمَدُ | صمد | صَّمَد | DET + N, masculine singular, nominative |
| 112:3:1 | لَمْ | — | لَم | NEG |
| 112:3:2 | يَلِدْ | ولد | وَلَدَ | V, imperfect jussive, 3MS, active |
| 112:3:3 | وَلَمْ | — | لَم | CONJ + NEG |
| 112:3:4 | يُولَدْ | ولد | وَلَدَ | V, imperfect jussive, 3MS, passive |
| 112:4:1 | وَلَمْ | — | لَم | CONJ + NEG |
| 112:4:2 | يَكُن | كون | كَانَ | V, imperfect jussive, 3MS |
| 112:4:3 | لَّهُۥ | — | — | P لَـ + PRON 3MS |
| 112:4:4 | كُفُوًا | كفء | كُفُو | N, masculine, indefinite, accusative |
| 112:4:5 | أَحَدٌۢ | ءحد | أَحَد | N, masculine, indefinite, nominative |

Attachment rows used structurally only:

- 112:1 a1: `هُوَ` begins the quoted complement of `قُلْ`.
- 112:1 a2: `أَحَدٌ` is the nominative predicate of `ٱللَّهُ`.
- 112:1 a3: `ٱللَّهُ` can stand as apposition to `هُوَ`.
- 112:2 a1: `ٱلصَّمَدُ` is the nominative predicate of `ٱللَّهُ`.
- 112:3 a1/a3: `يَلِدْ` and `يُولَدْ` are governed by `لَمْ` as jussive negated imperfects.
- 112:3 a2: `يُولَدْ` is coordinated with `يَلِدْ`.
- 112:4 a1: `يَكُن` is governed by `لَمْ`.
- 112:4 a2: `لَّهُۥ` is governed by `لَـ` as complement of `كُفُوًا`.
- 112:4 a3: `كُفُوًا` is the accusative predicate of `يَكُن`.
- 112:4 a4: final `أَحَدٌۢ` is the delayed nominative subject of `يَكُن`.

## Uncontaminated root dossier inventory

Every lexical seed pass visited the full S112 dossier set below: `قول، ءله، ءحد، صمد، ولد، كون، كفء`. In each seed record, “selected” means the branches or structures that actually transformed, completed, or forked the developing image before freeze. Unselected dossier material was not blended into a generalized meaning.

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

## Lexical seed universe

Main-lane lexical seed count is occurrence × accepted branch:

- 112:1:1 `قُلْ` قول: 16 seeds
- 112:1:3 `ٱللَّهُ` ءله: 2 seeds
- 112:2:1 `ٱللَّهُ` ءله: 2 seeds
- 112:1:4 `أَحَدٌ` ءحد: 6 seeds
- 112:4:5 `أَحَدٌۢ` ءحد: 6 seeds
- 112:2:2 `ٱلصَّمَدُ` صمد: 7 seeds
- 112:3:2 `يَلِدْ` ولد: 6 seeds
- 112:3:4 `يُولَدْ` ولد: 6 seeds
- 112:4:2 `يَكُن` كون: 6 seeds
- 112:4:4 `كُفُوًا` كفء: 5 seeds

Total lexical seeds audited: 62.

## Detailed seed passes with coherent image-branches

### L01 — 112:1:1 `قُلْ`, قول B001 — uttered quote-frame

- Initial image: an utterance is brought out into articulated speech `(E: ق و ل B001)`.
- Roots visited and selected: full S112 dossier set visited. Selected: `(E: attachment 112:1 a1 quoted_complement)`, `(E: ء ل ه B002 name-bearing content)`, `(E: ء ح د B001 predicated unity)`, `(E: ص م د B001 second predication as directed-reliance center)`.
- Image: the opening command produces a controlled speech-frame. The first activated need is not a thing in the world but the content to be said. The attachment row supplies the quote boundary, and the quoted nominal material fills it: `هُوَ ٱللَّهُ أَحَدٌ`; the second ayah reactivates the named referent and adds `ٱلصَّمَدُ`.
- Generating set: قول B001; quote-complement structure; ءله B002; ءحد B001; صمد B001.
- Frozen model: a commanded utterance whose content identifies one named referent and assigns a central predicate to him.
- Predictions at freeze: later material should keep the same referent active; it should not introduce another quoted speaker, rival referent, or competing predicate-subject frame.
- Unused features tested after freeze: `لَمْ يَلِدْ`, `وَلَمْ يُولَدْ`, `وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ`, repeated `أَحَد`.
- Corroborators: `(C: repetition 112:2:1 ٱللَّهُ)` keeps the referent active; `(C: لَّهُۥ pronoun 112:4:3)` continues the same 3MS target; `(C: و ل د B003 under repeated لَم)` and `(C: ك ف ء B001 under final لَم يكن)` preserve the utterance’s single-referent field by excluding generational and equivalent counterparts.
- Constraints: `(K: قول B001 is speech-frame only, not a proof that all following lexical images are literal speech-objects)`.
- Rival forks: قول B013 can make the content doctrine-like, but the local imperative and quote attachment keep B001 primary.
- Grade: medium-strong.
- Rationale: strong structural fit to `قُلْ` and the quote attachment; passage-scale synthesis is mostly supplied by later non-قول material.

### L02a — 112:1:3 `ٱللَّهُ`, ءله B002 — named referent inside the quote

- Initial image: the name `ٱللَّهُ` enters as a named divine form, the first rooted content inside the quote after the pronoun `(E: ء ل ه B002)`.
- Roots visited and selected: full dossier visited. Selected: `(E: attachment 112:1 a3 apposition to هُوَ)`, `(E: attachment 112:1 a2 predication)`, `(E: ء ح د B001)`.
- Image: the pronoun points, the name fixes the referent, and `أَحَدٌ` fills the predicate slot. The quoted clause becomes a tight identification-predication unit.
- Generating set: ءله B002 at 112:1:3; apposition/predication attachments; ءحد B001.
- Frozen model: named referent + unity predicate.
- Predictions at freeze: the same named referent should be maintained; further material should complete rather than replace the identity frame.
- Unused features tested after freeze: second `ٱللَّهُ`, `ٱلصَّمَدُ`, negated birth pair, final no-peer clause.
- Corroborators: `(C: repetition 112:2:1 ٱللَّهُ)` reactivates the named referent; `(C: ص م د B001)` gives the repeated name a further predicate; `(C: ك ف ء B001 + ء ح د B002 at closure)` excludes any peer from the named referent’s field.
- Constraints: `(K: ء ل ه B002 here is a proper-name use, not specifically oath or vocative syntax)`.
- Rival forks: B001 worshipped/mabud can run as a secondary image, but B002 is closer to the QAC proper noun and repeated name.
- Grade: medium-strong.
- Rationale: excellent positional fit and strong reactivation by repetition; branch B002’s oath/vocative details are only partly local.

### L02b — 112:1:3 `ٱللَّهُ`, ءله B001 — worshipped/referent under exclusive predication

- Initial image: a worshipped/mabud frame is activated by the divine-name root `(E: ء ل ه B001)`.
- Roots visited and selected: full dossier visited. Selected: `(E: ء ح د B001)`, `(E: ص م د B001)`.
- Image: if the named referent is heard through the worshipped/mabud branch, `أَحَدٌ` immediately narrows the field to one, and `ٱلصَّمَدُ` adds directed reliance: one worshipped referent who is the intended/reliance center.
- Generating set: ءله B001; ءحد B001; صمد B001.
- Frozen model: exclusive worshipped/reliance center.
- Predictions at freeze: no other relation should create a second comparable center; no genealogy should distribute the referent into a family-like structure.
- Unused features tested after freeze: ولد branches, كفء B001, final أحد under negation.
- Corroborators: `(C: و ل د B003 active/passive negated)` blocks generation roles; `(C: ك ف ء B001)` blocks equivalent counterpart; `(C: ء ح د B002 final negative-exhaustive أحد)` extends uniqueness over all possible peer-candidates.
- Constraints: `(K: passage does not contain explicit عبد or ritual-action morphology; worshipped/reliance is a branch-derived secondary frame)`.
- Rival forks: none needed.
- Grade: medium.
- Rationale: coherent and passage-fitting, but more inferential than the proper-name and predication frames.

### L03a — 112:2:1 `ٱللَّهُ`, ءله B002 — repeated name as reactivation hinge

- Initial image: the name returns at a new ayah boundary `(E: ء ل ه B002)`.
- Roots visited and selected: full dossier visited. Selected: `(E: repetition from 112:1:3 to 112:2:1)`, `(E: ص م د B001)`, `(E: attachment 112:2 a1 predication)`.
- Image: after `هُوَ ٱللَّهُ أَحَدٌ`, the bare repeated `ٱللَّهُ` reopens the same referent and attaches a second predicate, `ٱلصَّمَدُ`. The reactivation is temporal: the name already established in 112:1 becomes the subject for a new role in 112:2.
- Generating set: ءله B002 at 112:2:1; repetition; predication attachment; صمد B001.
- Frozen model: same named referent receives a second predicate.
- Predictions at freeze: later clauses should keep this referent as the understood 3MS target.
- Unused features tested after freeze: `يَلِدْ`, `يُولَدْ`, `لَّهُۥ`, `كُفُوًا`, final `أَحَدٌۢ`.
- Corroborators: `(C: 3MS morphology on يَلِدْ / يُولَدْ / يَكُن and pronoun هُۥ)` keeps the referent active; `(C: ك ف ء B001)` supplies the final relation denied of him.
- Constraints: `(K: B002 details of oath/appeal remain nonlocal here)`.
- Rival forks: if B001 is chosen instead, the second predicate becomes reliance-centered rather than name-centered.
- Grade: strong.
- Rationale: this is one of the clearest temporal reactivations: repeated name after ayah boundary creates the hinge for the rest of the passage.

### L03b — 112:2:1 `ٱللَّهُ`, ءله B001 — worshipped/reliance center after unity

- Initial image: the worshipped/mabud branch returns after `أَحَدٌ` has already narrowed the field `(E: ء ل ه B001)`.
- Roots visited and selected: full dossier visited. Selected: `(E: ء ح د B001 already active)`, `(E: ص م د B001)`.
- Image: first unity, then the repeated divine referent, then directed reliance. This sequence makes `ٱلصَّمَدُ` not an isolated label but the second role of the same exclusive referent.
- Generating set: ءله B001 at 112:2:1; prior ءحد B001 as active context; صمد B001.
- Frozen model: one worshipped/reliance center.
- Predictions at freeze: later clauses should deny dependence, derivation, and equivalence.
- Unused features tested after freeze: birth pair and final no-peer clause.
- Corroborators: `(C: و ل د B005)` denies being a generated derivative; `(C: و ل د B003 active/passive)` denies outgoing and incoming birth; `(C: ك ف ء B001)` denies counterpart.
- Constraints: `(K: no explicit عبد action appears)`.
- Rival forks: صمد B002 gives a more compact-solid image than the reliance image.
- Grade: medium-strong.
- Rationale: the branch becomes strong through sequence and role completion, especially with صمد B001.

### L04 — 112:1:4 `أَحَدٌ`, ءحد B001 — positive unity before exclusions

- Initial image: absolute one-ness/unity is predicated of the named referent `(E: ء ح د B001)`.
- Roots visited and selected: full dossier visited. Selected: `(E: ء ل ه B002 named subject)`, `(E: attachment 112:1 a2 predication)`, `(E: ص م د B001)`, with a rival compact-solid fork `(E: ص م د B002)`.
- Image: `أَحَدٌ` first gives a positive unity predicate. `ٱلصَّمَدُ` then either makes that unity a directed-reliance center `(صمد B001)` or a compact, non-hollow solidity image `(صمد B002)`. The later negations arrive as pruning operations.
- Generating set: ءحد B001; ءله B002; predication; صمد B001/B002 fork.
- Frozen model: one named referent, either as intended/reliance center or as compact unshared integrity.
- Predictions at freeze: no birth-out, no birth-from, no equivalent, and a possible return of `أحد` in a negative scope.
- Unused features tested after freeze: ولد B003/B005, كون B001, كفء B001, final ءحد B002.
- Corroborators: `(C: و ل د B003 active/passive)` denies generational splitting; `(C: و ل د B005)` denies derivation from or production of another thing; `(C: ك ف ء B001)` denies peer-equivalence; `(C: ء ح د B002 at 112:4:5)` reactivates `أحد` under exhaustive negation.
- Constraints: `(K: ء ح د B003 counting/compound-numeral is not locally licensed by predicative nominative أحد)`.
- Rival forks: صمد B001 reliance-center fork is stronger in direct branch fit; صمد B002 compact-solid fork is a vivid secondary simulation and receives later support from generation/equivalence denial.
- Grade: strong.
- Rationale: this seed predicts the passage’s later exclusions and is strongly reactivated by final `أَحَدٌۢ`.

### L05a — 112:4:5 `أَحَدٌۢ`, ءحد B002 — negative exhaustive closure

- Initial image: `أحد` in a negated context exhausts the class of possible candidates `(E: ء ح د B002)`.
- Roots visited and selected: full dossier visited. Selected: `(E: ك ف ء B001)`, `(E: ك و ن B001)`, `(E: attachment 112:4 a3 kana_predicate)`, `(E: attachment 112:4 a4 delayed subject)`, `(E: لَّهُۥ prep complement of كفوا)`.
- Image: the final clause has the shape “no occurrence/existence of a counterpart for him, not even one candidate.” The delayed `أَحَدٌۢ` closes the search-space after `كُفُوًا` has introduced the peer role.
- Generating set: ءحد B002 at 112:4:5; كفء B001; كون B001; negated copular construction; delayed-subject structure.
- Frozen model: exhaustive no-peer closure.
- Predictions at freeze: it should retrospectively illuminate the first `أَحَدٌ`: the first one-ness is not merely a predicate but the positive side of a later universal exclusion.
- Unused features tested after freeze: earlier `أَحَدٌ`, `ٱلصَّمَدُ`, birth negations.
- Corroborators: `(C: ء ح د B001 at 112:1:4)` is reactivated as positive unity; `(C: ص م د B001/B002)` supports lack of parallel reliance-center or lack of compositional counterpart; `(C: و ل د B003)` has already denied the most local relation by which counterpart-like family roles could arise.
- Constraints: `(K: final أحد is not simply repetition for emphasis; attachment row 112:4 a4 makes it delayed subject inside a no-peer clause)`.
- Rival forks: final ءحد B001 can also run, but B002 has the strongest local negative-scope fit.
- Grade: strong.
- Rationale: exact branch-context fit and strong backward reactivation of 112:1:4.

### L05b — 112:4:5 `أَحَدٌۢ`, ءحد B001 — final unity reactivating first unity

- Initial image: final `أحد` repeats the unity word `(E: ء ح د B001)`.
- Roots visited and selected: full dossier visited. Selected: `(E: ك ف ء B001)`, `(E: ك و ن B001)`, `(E: ء ح د B002 as local negative-scope dimension)`.
- Image: final `أَحَدٌۢ` can be heard as the same unity-word returning, but now placed inside a negated existence/equivalence construction. The first occurrence says one; the last says no one as peer.
- Generating set: ءحد B001 at 112:4:5; كفء B001; كون B001; local B002 dimension as negative-scope expansion.
- Frozen model: positive unity converted into exhaustive peer-denial.
- Predictions at freeze: the passage should close here because the possible rival role has been exhausted.
- Unused features tested after freeze: first `أَحَدٌ`; ayah boundary closure.
- Corroborators: `(C: sequence 112:1 positive أحد → 112:4 negated أحد)`; `(C: final ayah closure after delayed subject)`.
- Constraints: `(K: because final أحد is under negation, B002 is more exact than B001 for local syntax)`.
- Rival forks: B002 primary; B001 secondary reactivation.
- Grade: medium-strong.
- Rationale: strong as temporal reactivation, less exact than B002 as local branch selection.

### L06 — 112:2:2 `ٱلصَّمَدُ`, صمد B001 — intended/reliance center

- Initial image: a center intended and relied upon for matters or needs `(E: ص م د B001)`.
- Roots visited and selected: full dossier visited. Selected: `(E: ء ل ه B002 repeated subject)`, `(E: ء ح د B001 prior unity)`.
- Image: after the passage establishes `ٱللَّهُ أَحَدٌ`, `ٱللَّهُ ٱلصَّمَدُ` transforms unity into directed centrality: the one named referent is the one toward whom قصد/اعتماد is oriented.
- Generating set: صمد B001; repeated ءله B002; prior ءحد B001.
- Frozen model: exclusive reliance/direction center.
- Predictions at freeze: no genealogy should make the center one node among kin; no equal should provide a parallel center; later clauses should protect the centrality by denying roles around it.
- Unused features tested after freeze: ولد B001/B002/B003/B005; كون B001; كفء B001; final ءحد B002.
- Corroborators: `(C: و ل د B003 active/passive negation)` blocks outgoing and incoming birth roles; `(C: و ل د B005)` blocks derivation; `(C: ك ف ء B001)` blocks a peer/parallel; `(C: ء ح د B002)` exhausts all possible peer-candidates.
- Constraints: `(K: صمد B001 does not itself state the negations; the negations corroborate only after freeze)`.
- Rival forks: صمد B002 compactness; صمد B007 persistence.
- Grade: strong.
- Rationale: excellent role completion: unity → centrality → denial of genealogy and equivalence.

### L07 — 112:2:2 `ٱلصَّمَدُ`, صمد B002 — compact non-hollow integrity

- Initial image: solid, compact, non-hollow integrity `(E: ص م د B002)`.
- Roots visited and selected: full dossier visited. Selected: `(E: ء ح د B001 unity)`, `(E: ء ل ه B002 repeated subject)`.
- Image: the word can launch a secondary simulation of dense, unpierced integrity: one named referent with no inner vacancy or divisible opening. This is not a primary paraphrase of the ayah; it is a branch-image that predicts resistance to derivation and counterparting.
- Generating set: صمد B002; ءحد B001; repeated ءله B002.
- Frozen model: compact unity without internal vacancy.
- Predictions at freeze: no being produced from another, no producing another of the same line, no counterpart structure, and no final opening into multiplicity.
- Unused features tested after freeze: ولد B003/B005; كفء B001; final ءحد B002.
- Corroborators: `(C: و ل د B005)` denies generated derivation; `(C: و ل د B003 active/passive)` denies birth relations; `(C: ك ف ء B001)` denies an equal counterpart; `(C: ء ح د B002)` closes the candidate set.
- Constraints: `(K: local syntax gives ٱلصَّمَدُ as predicate, not a literal stone/solid object; no material body is supplied)`.
- Rival forks: B001 is more directly relational; B002 is image-rich but secondary.
- Grade: medium-strong.
- Rationale: strong sequence fit and independent corroboration, but it must remain a secondary simulation.

### L08 — 112:2:2 `ٱلصَّمَدُ`, صمد B007 — persistence under severity

- Initial image: continuing/biding under severity `(E: ص م د B007)`.
- Roots visited and selected: full dossier visited. Selected: `(E: sequence 112:2 → repeated negations 112:3–4)` only weakly.
- Image: B007 can hear `ٱلصَّمَدُ` as a persistence image: the predicate remains standing while repeated `لَمْ` clauses deny possible relational changes. The model is temporal endurance more than directed reliance.
- Generating set: صمد B007; repeated negation sequence.
- Frozen model: enduring predicate held through a chain of denials.
- Predictions at freeze: later clauses should maintain rather than transform the referent.
- Unused features tested after freeze: 3MS morphology and final no-peer closure.
- Corroborators: `(C: 3MS continuity across يلد / يولد / يكن / له)` keeps the same referent through time; `(C: ك و ن B001 negated occurrence)` helps the final closure stay temporal.
- Constraints: `(K: no local word for cold, drought, hardship, or severity appears; الشدة is imported only from the branch image)`.
- Rival forks: B001 and B002 are stronger.
- Grade: weak.
- Rationale: a possible temporal-support image but lacking specific passage-local severity.

### L09 — 112:3:2 `يَلِدْ`, ولد B003 — outgoing birth denied

- Initial image: occurrence of birth/placing a child, but immediately under `لَمْ` `(E: و ل د B003 active-before-freeze)`.
- Roots visited and selected: full dossier visited. Selected: `(E: negation/mood 112:3 a1)`, `(E: coordination 112:3 a2)`, `(E: و ل د B003 passive counterpart at 112:3:4)`.
- Image: a possible outgoing generative relation is activated only to be cancelled. The coordinated passive then cancels the inverse relation. The pair builds a two-way exclusion: not source-by-birth and not born-from-source.
- Generating set: ولد B003 at 112:3:2; `لَمْ` jussive negation; coordinated passive ولد B003.
- Frozen model: bidirectional birth-relation shutdown.
- Predictions at freeze: final material should generalize from birth-relations to all peer/counterpart relations.
- Unused features tested after freeze: كون B001, كفء B001, final ءحد B002; earlier ءحد/صمد.
- Corroborators: `(C: ك ف ء B001)` supplies the broader peer role; `(C: ك و ن B001 under لَمْ)` denies occurrence/existence of that role; `(C: ء ح د B002)` exhausts the candidate set; `(C: ء ح د B001 + ص م د B001 earlier)` gives the positive unity/centrality that the negation protects.
- Constraints: `(K: ولد B003 is a negated relation, not a positive event in the passage)`.
- Rival forks: ولد B005 broadens from birth to derivation; B003 remains the best direct fit.
- Grade: strong.
- Rationale: exact local morphology, explicit active/passive pairing, and strong final expansion to no equivalent.

### L10 — 112:3:4 `يُولَدْ`, ولد B003 — incoming birth denied

- Initial image: being born, in passive form, under repeated `لَمْ` `(E: و ل د B003 passive-before-freeze)`.
- Roots visited and selected: full dossier visited. Selected: `(E: passive voice)`, `(E: negation/mood 112:3 a3)`, `(E: coordination with active 112:3 a2)`.
- Image: the passive form takes the relation that active `يَلِدْ` denied outwardly and turns it inward: not born from another. The order matters: after denying outbound generation, the passage denies inbound origin.
- Generating set: ولد B003 at 112:3:4; passive morphology; repeated `لَمْ`; coordination with active `يَلِدْ`.
- Frozen model: no genealogical vector leaves him and no genealogical vector enters him.
- Predictions at freeze: no one should be able to stand as peer, parent, child, or equivalent in relation to him.
- Unused features tested after freeze: final no-peer clause.
- Corroborators: `(C: ك ف ء B001)` denies counterpart; `(C: لَّهُۥ complement to كفوا)` attaches the no-peer relation to the same 3MS referent; `(C: ء ح د B002)` closes the possible candidate class.
- Constraints: `(K: the passive is governed by لَمْ, so the passage supplies no positive birth scene)`.
- Rival forks: ولد B002 parents can be a role-specific branch after passive birth, but B003 is the event branch directly expressed by the verb.
- Grade: strong.
- Rationale: precise voice, negation, and sequence fit.

### L11a — 112:3:2 `يَلِدْ`, ولد B001 — offspring role denied

- Initial image: offspring/child role is activated by the birth root, then negated `(E: و ل د B001)`.
- Roots visited and selected: full dossier visited. Selected: `(E: active negated يلد)`, `(E: و ل د B003 event dimension)`, `(E: coordinated passive)`.
- Image: the active verb can be heard as denying an offspring-output role: no child or descendant is generated from the referent.
- Generating set: ولد B001 at 112:3:2; active negation; B003 event dimension.
- Frozen model: no offspring branch from him.
- Predictions at freeze: no corresponding parent/peer network should remain available.
- Unused features tested after freeze: passive `يُولَدْ`, final كفء/أحد.
- Corroborators: `(C: passive يُولَدْ)` denies the inverse parent-origin slot; `(C: ك ف ء B001)` denies peer/equal; `(C: ء ح د B002)` denies any candidate.
- Constraints: `(K: B001 is a nominal role; the local form is verbal, so B003 is more exact for the event)`.
- Rival forks: B003 primary, B001 role-specific.
- Grade: medium-strong.
- Rationale: strong role fit, but derivative from the event branch and negated morphology.

### L11b — 112:3:4 `يُولَدْ`, ولد B002 — parent-origin role denied

- Initial image: father/mother origin relation is activated through the passive birth verb `(E: و ل د B002)`.
- Roots visited and selected: full dossier visited. Selected: `(E: passive voice)`, `(E: و ل د B003 birth-event dimension)`, `(E: negation 112:3 a3)`.
- Image: passive `يُولَدْ` makes a parent-origin slot thinkable and immediately denies it. This complements the active denial of offspring.
- Generating set: ولد B002 at 112:3:4; passive morphology; ولد B003 event dimension; negation.
- Frozen model: no parent-origin relation.
- Predictions at freeze: if no parent-origin and no child-output relation exists, the final clause should deny broader equivalence rather than add another genealogy term.
- Unused features tested after freeze: كفء B001, كون B001, final ءحد B002.
- Corroborators: `(C: ك ف ء B001)` generalizes beyond parent/child roles; `(C: ك و ن B001)` denies occurrence of the relation; `(C: ء ح د B002)` exhausts all possible bearers.
- Constraints: `(K: B002 is inferred through passive birth; no explicit والد/والدة noun appears)`.
- Rival forks: B003 direct-event reading stronger locally.
- Grade: medium-strong.
- Rationale: strong role completion in the active/passive pair.

### L12a — 112:3:2 `يَلِدْ`, ولد B005 — no derivative produced from him

- Initial image: something generated from something else as a caused or derived product `(E: و ل د B005 active-outward)`.
- Roots visited and selected: full dossier visited. Selected: `(E: active negated يلد)`, `(E: coordinated passive يولد)`.
- Image: the active negation cancels a derived-output model: nothing is produced as a generated thing from the referent. The passive partner then denies that the referent himself is generated from another.
- Generating set: ولد B005 at 112:3:2; active/passive negated pair.
- Frozen model: no derivation outward or inward.
- Predictions at freeze: the passage should end by denying all counterpart/equivalent relations, not only biological birth.
- Unused features tested after freeze: كفء B001; كون B001; final ءحد B002.
- Corroborators: `(C: ك ف ء B001)` supplies the broader equivalence relation; `(C: ك و ن B001)` denies occurrence/existence; `(C: ء ح د B002)` exhausts candidates.
- Constraints: `(K: B005 is broader than the immediate verbal birth event; B003 remains the local anchor)`.
- Rival forks: B003 direct birth; B005 derivational generalization.
- Grade: medium-strong.
- Rationale: good bridge from genealogy to final equivalence denial, but broader than the local form.

### L12b — 112:3:4 `يُولَدْ`, ولد B005 — no derivative origin

- Initial image: the referent could be something resulting from another thing, but passive negation blocks it `(E: و ل د B005 passive-inward)`.
- Roots visited and selected: full dossier visited. Selected: `(E: passive voice)`, `(E: negated jussive)`, `(E: active counterpart يلد)`.
- Image: this seed starts from origin rather than output. It says no derivational source stands behind the referent; the active partner already denied derivational product from him.
- Generating set: ولد B005 at 112:3:4; passive morphology; active/passive pair.
- Frozen model: no derived-from relation.
- Predictions at freeze: final relation should deny likeness/equivalence rather than merely deny parentage.
- Unused features tested after freeze: كفء B001; final ءحد B002; prior صمد B002.
- Corroborators: `(C: ك ف ء B001)` denies comparable counterpart; `(C: ء ح د B002)` exhausts candidates; `(C: ص م د B002)` independently supports compact non-derived integrity if it was unused in this pass.
- Constraints: `(K: B005 should not erase the concrete active/passive birth morphology)`.
- Rival forks: B002 parent-origin is narrower; B005 derivational image is broader.
- Grade: medium-strong.
- Rationale: strong explanatory bridge to final closure, with local breadth constraint.

### L13 — 112:4:2 `يَكُن`, كون B001 — negated occurrence/existence of a peer

- Initial image: occurrence/happening/presence in time, under `لَمْ` `(E: ك و ن B001)`.
- Roots visited and selected: full dossier visited. Selected: `(E: negation/mood 112:4 a1)`, `(E: ك ف ء B001)`, `(E: ء ح د B002)`, `(E: attachment 112:4 a3/a4)`, `(E: لَّهُۥ complement)`.
- Image: after positive predicates and birth denials, the final verb makes closure temporal/existential: no counterpart ever comes to presence for him within the clause’s no-peer structure.
- Generating set: كون B001; final `لَمْ`; كفء B001; final ءحد B002; kana predicate/delayed-subject attachments.
- Frozen model: no occurrence/existence of any peer for him.
- Predictions at freeze: this should be the closure point because the remaining candidate set has been exhausted.
- Unused features tested after freeze: earlier `أَحَدٌ`, `ٱلصَّمَدُ`, birth pair.
- Corroborators: `(C: ء ح د B001)` gives the positive unity whose peer is denied; `(C: ص م د B001/B002)` gives centrality/compactness; `(C: و ل د B003/B005)` denies narrower origin/offspring relations before the general no-peer clause.
- Constraints: `(K: كون B002 place/status is not needed; local attachment makes كفوا the predicate and أحد the delayed subject)`.
- Rival forks: B002 status/place remains weak and constrained.
- Grade: strong.
- Rationale: exact final-clause fit and explains why the passage closes at `أَحَدٌۢ`.

### L14 — 112:4:4 `كُفُوًا`, كفء B001 — equivalence/counterpart denied

- Initial image: likeness, peer, equivalence, counterpart `(E: ك ف ء B001)`.
- Roots visited and selected: full dossier visited. Selected: `(E: ك و ن B001)`, `(E: final ء ح د B002)`, `(E: لَّهُۥ complement)`, `(E: attachment 112:4 a2/a3/a4)`.
- Image: `كُفُوًا` introduces the peer role, `لَّهُۥ` attaches it to the established referent, `يَكُن` under `لَمْ` denies its occurrence, and final `أَحَدٌۢ` says no candidate fills it.
- Generating set: كفء B001; كون B001; final ءحد B002; negated copular construction.
- Frozen model: no peer slot has any occupant.
- Predictions at freeze: earlier unity, ṣamad, and birth denials should now be retrospectively organized as narrower exclusions leading to this broad no-equivalence closure.
- Unused features tested after freeze: 112:1 `أَحَدٌ`, 112:2 `ٱلصَّمَدُ`, 112:3 birth pair.
- Corroborators: `(C: ء ح د B001)` positive unity; `(C: ص م د B001)` no parallel reliance-center; `(C: ص م د B002)` no counterpart to compact integrity; `(C: و ل د B003 active/passive)` no kinship route to a counterpart; `(C: و ل د B005)` no derived counterpart.
- Constraints: `(K: كفء B001 is negated; it does not assert a peer)`.
- Rival forks: none of كفء B002–B005 survives the local no-peer syntax.
- Grade: strong.
- Rationale: this seed provides the final role that gathers the earlier denials and closes the passage.

## Compact audit for additional lexical seeds

All seeds below independently visited the full S112 dossier inventory. “Selected” lists any branch/structure that survived into construction before freeze. “Terminated” means no passage-local complement transformed the seed into a coherent image.

| Seed | Initial image and selected material | Corroboration / constraint after freeze | Grade |
| --- | --- | --- | --- |
| 112:1:1 قول B002 | Tongue as instrument of speech. Selected: local `قُلْ` imperative only. | `(K: no لسان/body-instrument word; quote-complement, not organ scene)`. | unlikely |
| 112:1:1 قول B003 | Person characterized by much speech. Selected: none beyond `قُلْ`. | `(K: imperative single utterance; no وصف إنسان as loquacious)`. | unlikely |
| 112:1:1 قول B004 | Authoritative speaker/title. Selected: none. | `(K: قُلْ is command verb; no title/kingly role)`. | unlikely |
| 112:1:1 قول B005 | Fabricating or attributing what was not said. Selected: none. | `(K: quote is syntactically commanded content; no كذب/تقول frame)`. | unlikely |
| 112:1:1 قول B006 | Drawing a saying to oneself. Selected: none. | `(K: outward imperative and quoted complement oppose inward appropriation)`. | unlikely |
| 112:1:1 قول B007 | Report circulating among people. Selected: قول B001 only as speech frame. | `(K: no الناس/قالة diffusion structure; passage gives a direct command)`. | weak |
| 112:1:1 قول B008 | Stick used in game. Selected: none. | `(K: no object, game, striking, or القلة scene)`. | unlikely |
| 112:1:1 قول B009 | Mutual negotiation. Selected: quote frame only. | `(K: imperative from one side; no reciprocal المقاولة morphology)`. | unlikely |
| 112:1:1 قول B010 | Imposing judgment/control over another. Selected: none. | `(K: no تحكم relation; quoted content is not syntactically a coercive judgment act)`. | unlikely |
| 112:1:1 قول B011 | Saying used as supposing/thinking. Selected: none. | `(K: imperative قل is not ظن-like complement syntax here)`. | unlikely |
| 112:1:1 قول B012 | Saying in the self before expression. Selected: B001 as contrast. | `(K: the local event is expression by speech; B012 remains pre-verbal and is defeated by قُلْ)`. | unlikely |
| 112:1:1 قول B013 | Saying as belief/doctrine. Selected: quote proposition; ءحد B001; صمد B001; negation chain as content. | `(C: compact predications and exclusions can be held as a doctrinal proposition)`, `(K: local verb is still imperative utterance, not explicit اعتقاد)`. | weak |
| 112:1:1 قول B014 | A thing “says” by indicating. Selected: later predications only as content. | `(K: no non-speaking object whose state indicates; direct speech command dominates)`. | unlikely |
| 112:1:1 قول B015 | True care/concern for a thing. Selected: none. | `(K: no عناية construction; quote-frame only)`. | unlikely |
| 112:1:1 قول B016 | Definition/limit of a thing. Selected: ءحد B001 + صمد B001/B002 as definitional-like predicates. | `(C: two positive predicates plus exclusions create a compact boundary)`, `(K: no technical حد construction; branch is remote)`. | weak |
| 112:1:4 ءحد B002 | Negative-exhaustive أحد seeded at first occurrence. Selected: later final أحد B002 only after delay. | `(K: first أحد is not in negative scope)`, `(C: final أحد under negation reactivates the branch)`. | weak |
| 112:1:4 ءحد B003 | Counting/compound one. Selected: none. | `(K: predicate أحد, no numeral compound or counted object)`. | unlikely |
| 112:1:4 ءحد B004 | First/additive/day-name. Selected: none. | `(K: not مضاف and no day-name frame)`. | unlikely |
| 112:1:4 ءحد B005 | Singular individuals one by one. Selected: ءحد B001 as nearby. | `(K: first occurrence is predicate unity, not آحادا dispersal)`. | weak |
| 112:1:4 ءحد B006 | Mount Uḥud. Selected: none. | `(K: no place-name or mountain context)`. | unlikely |
| 112:4:5 ءحد B003 | Counting/compound one at closure. Selected: none. | `(K: delayed subject in no-peer clause, not numeral composition)`. | unlikely |
| 112:4:5 ءحد B004 | First/additive/day-name. Selected: none. | `(K: no إضافة/day-name frame)`. | unlikely |
| 112:4:5 ءحد B005 | Any individual candidate. Selected: كفء B001 + negation. | `(C: negative scope can scan candidate individuals)`, `(K: B002 gives the exact استغراق النفي branch)`. | medium |
| 112:4:5 ءحد B006 | Mount Uḥud. Selected: none. | `(K: no place-name/mountain context)`. | unlikely |
| 112:2:2 صمد B003 | Stopper/seal of bottle. Selected: possible closure image only. | `(K: no bottle/container; later negations close relations, not a literal vessel)`. | unlikely |
| 112:2:2 صمد B004 | Binding/wrapping head. Selected: none. | `(K: no head, cloth, or bandaging scene)`. | unlikely |
| 112:2:2 صمد B005 | Overseeing an affair with concern. Selected: ءله B001 only weakly. | `(K: no أمر object or حفل به structure)`. | weak |
| 112:2:2 صمد B006 | Striking with a stick. Selected: none. | `(K: no ضرب, عصا, patient, or impact scene)`. | unlikely |
| 112:3:2 ولد B002 | Parent role seeded from active `يَلِدْ`. Selected: active/passive pair. | `(K: active form more directly denies offspring-output than parent-origin; passive seed is stronger for B002)`. | weak |
| 112:3:2 ولد B004 | Newborn/young servant. Selected: none. | `(K: verbal يلد, no وليد/وليدة noun; no youth/servitude role)`. | unlikely |
| 112:3:2 ولد B006 | Peer of same birth-age. Selected: final كفء B001 weakly. | `(C: final no-peer can broadly deny peerhood)`, `(K: no age/time-of-birth comparison)`. | weak |
| 112:3:4 ولد B001 | Child/offspring role from passive `يولد`. Selected: B003 passive birth event. | `(K: passive form more directly denies parent-origin; B001 offspring-output fits active يلد better)`. | medium |
| 112:3:4 ولد B004 | Newborn/young servant. Selected: none. | `(K: no وليد/وليدة noun; no servitude/youth scene)`. | unlikely |
| 112:3:4 ولد B006 | Same-age peer. Selected: final كفء B001 weakly. | `(C: no-peer closure blocks counterpart)`, `(K: no سن/لدة comparison)`. | weak |
| 112:4:2 كون B002 | Place/status/standing. Selected: كفء B001 weakly as status-equivalence. | `(K: local construction uses كان as negated copula/existence with كفوا predicate; no مكان word)`. | weak |
| 112:4:2 كون B003 | Surety/standing for someone. Selected: none. | `(K: له is complement of كفوا, not surety/kafāla frame)`. | unlikely |
| 112:4:2 كون B004 | Submission/humbling. Selected: none. | `(K: no استكانة or submission morphology)`. | unlikely |
| 112:4:2 كون B005 | Old man named from “I was”. Selected: none. | `(K: no age/person-name frame)`. | unlikely |
| 112:4:2 كون B006 | Bad state. Selected: none. | `(K: no كينة سوء or state-of-badness phrase)`. | unlikely |
| 112:4:4 كفء B002 | Tilting/overturning/diverting. Selected: none. | `(K: كفوا is predicate noun in no-peer clause; no movement/turning scene)`. | unlikely |
| 112:4:4 كفء B003 | Rhyme discrepancy. Selected: acoustic d-pattern only as distant. | `(K: no poetry/qāfiya frame; not a lexical fit despite passage sound pattern)`. | unlikely |
| 112:4:4 كفء B004 | Rear covering of tent/house. Selected: none. | `(K: no خِباء/بيت or covering structure)`. | unlikely |
| 112:4:4 كفء B005 | Yearly produce/alternating offspring-yield. Selected: ولد B003/B005 weakly. | `(K: no palm/camel/year-production structure; final كفوا syntax demands peer/equivalence B001)`. | unlikely |

## Constructional, morphosyntactic, and temporal seeds

### C01 — quoted-complement construction under `قُلْ`

- Seed: attachment 112:1 a1, `هُوَ` as quoted complement of `قُلْ`.
- Initial image: command opens a speech chamber that must be filled by content.
- Roots visited and selected: selected `(E: قول B001)`, `(E: ءله B002)`, `(E: ءحد B001)`.
- Frozen model: an uttered content unit begins with pronoun → name → predicate.
- Predictions at freeze: the same referent should persist as later predicates/negations accumulate.
- Unused features tested: repeated `ٱللَّهُ`, 3MS verbs/pronoun, final no-peer clause.
- Corroborators: `(C: repetition 112:2:1)`, `(C: 3MS morphology across 112:3–4)`, `(C: لَّهُۥ pronoun)`.
- Constraints: `(K: quote construction does not independently create lexical meanings)`.
- Grade: medium-strong.
- Rationale: structurally forced and temporally important, but not a complete synthesis alone.

### C02 — nominal predication chain: `هُوَ ٱللَّهُ أَحَدٌ` → `ٱللَّهُ ٱلصَّمَدُ`

- Seed: two predication attachments, 112:1 a2/a3 and 112:2 a1.
- Initial image: the referent is named, predicated as `أَحَدٌ`, then re-named and predicated as `ٱلصَّمَدُ`.
- Selected evidence: `(E: ءله B002 repeated name)`, `(E: ءحد B001)`, `(E: صمد B001)` with secondary `(E: صمد B002 fork)`.
- Frozen model: two positive predicates establish uniqueness and centrality/compactness before any negations.
- Predictions at freeze: later clauses should not add rival positive entities; they should constrain possible relational misunderstandings.
- Unused features tested: `لم يلد`, `ولم يولد`, `ولم يكن له كفوا أحد`.
- Corroborators: `(C: و ل د B003/B005 negated pair)`, `(C: ك ف ء B001)`, `(C: ء ح د B002 final)`.
- Constraints: `(K: predication structure keeps images subordinate to the Arabic clauses; صمد B002 is not literal materiality)`.
- Grade: strong.
- Rationale: this construction explains sequence: positive compact identification before negative relational pruning.

### C03 — `ٱلصَّمَدُ` as hinge between unity and denials

- Seed: ayah-boundary position of `ٱللَّهُ ٱلصَّمَدُ`.
- Initial image: after unity, a second predicate creates a role that later denials protect.
- Selected evidence: `(E: صمد B001)`, `(E: ءحد B001)`, `(E: repetition of ءله B002)`.
- Frozen model: the single named referent is an exclusive reliance center.
- Predictions at freeze: no genealogy or peer relation should remain possible.
- Unused features tested: birth pair and final no-peer clause.
- Corroborators: `(C: و ل د B003 active/passive)`, `(C: ك ف ء B001)`, `(C: ء ح د B002)`.
- Constraints: `(K: hinge position supports but does not lexically prove all later denials)`.
- Grade: strong.
- Rationale: strong temporal conditioning: `الصمد` reorganizes the preceding unity and prepares the exclusions.

### C04 — paired negation: `لَمْ يَلِدْ وَلَمْ يُولَدْ`

- Seed: repeated `لَمْ`, active/passive ولد, coordination 112:3 a2.
- Initial image: a relation is tested in both directions and cancelled in both directions.
- Selected evidence: `(E: و ل د B003 active)`, `(E: و ل د B003 passive)`, `(E: morphology active/passive)`, `(E: repeated negated jussive)`.
- Frozen model: no birth-output and no birth-origin.
- Predictions at freeze: a broader relational exclusion should follow, because only genealogy has been denied so far.
- Unused features tested: final `كُفُوًا أَحَدٌ`.
- Corroborators: `(C: ك ف ء B001)` broadens from genealogy to equivalence; `(C: ء ح د B002)` exhausts candidates; `(C: ك و ن B001)` supplies existential closure.
- Constraints: `(K: no positive birth event is asserted)`.
- Grade: strong.
- Rationale: exact morphology and sequence create a compact bidirectional shutdown that predicts the final clause.

### C05 — final no-peer construction: `وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ`

- Seed: negated `كان` + `له` complement + `كفوا` predicate + delayed `أحد`.
- Initial image: the peer slot is opened and emptied.
- Selected evidence: `(E: كون B001)`, `(E: كفء B001)`, `(E: ءحد B002)`, `(E: attachments 112:4 a1–a4)`.
- Frozen model: no occurrence/existence of a peer for him, with no possible candidate left.
- Predictions at freeze: this should retrospectively gather first `أحد`, `الصمد`, and the birth negations.
- Unused features tested: earlier positive predicates.
- Corroborators: `(C: ء ح د B001 positive unity)`, `(C: ص م د B001/B002)`, `(C: و ل د B003/B005)`.
- Constraints: `(K: كفء B001 is negated; the clause is not asserting resemblance)`.
- Grade: strong.
- Rationale: strongest closure seed; it explains why the passage stops after final `أحد`.

### C06 — repeated `أحد`: positive one-ness becomes exhaustive no-one

- Seed: temporal recurrence 112:1:4 `أَحَدٌ` → 112:4:5 `أَحَدٌۢ`.
- Initial image: the same lexical form first states one-ness, then returns under negation to exclude every candidate.
- Selected evidence: `(E: ءحد B001 first occurrence)`, `(E: ءحد B002 final occurrence)`, `(E: كفء B001)`.
- Frozen model: positive unity is reactivated as universal no-peer exclusion.
- Predictions at freeze: intervening material should make the shift necessary rather than ornamental.
- Unused features tested: `الصمد`; birth pair.
- Corroborators: `(C: صمد B001/B002)` supplies the central/compact predicate that needs protection; `(C: ولد B003 active/passive)` removes genealogy before the final broader denial.
- Constraints: `(K: the two أحد tokens do not perform identical syntax; first is predicate, final is delayed subject under negation)`.
- Grade: strong.
- Rationale: clearest temporally conditioned reactivation in the surah.

### C07 — positive predicates followed by negative pruning

- Seed: passage-level sequence: 112:1–2 positive nominal predicates, 112:3–4 repeated `لَمْ` denials.
- Initial image: establish a referent and predicates, then remove possible relational competitors.
- Selected evidence: `(E: ءله B002)`, `(E: ءحد B001)`, `(E: صمد B001)`, `(E: ولد B003 active/passive)`, `(E: كفء B001)`.
- Frozen model: identity → centrality → genealogy denied → equivalence denied.
- Predictions at freeze: the final denial should be broader than the birth denial.
- Unused features tested: final ءحد B002 and kana structure.
- Corroborators: `(C: كون B001 + ءحد B002)` closes the candidate set; `(C: ayah boundary 112:4 close)` stops after peer-exhaustion.
- Constraints: `(K: sequence model is structural; it depends on lexical branches for content)`.
- Grade: strong.
- Rationale: explains order better than a shuffled list of roots.

### C08 — acoustic/temporal recurrence of final د sounds

- Seed: recitational sound recurrence across `أَحَدٌ`, `ٱلصَّمَدُ`, `يَلِدْ`, `يُولَدْ`, final `أَحَدٌ`.
- Initial image: repeated dental closure binds the sequence acoustically while semantic roles tighten.
- Selected evidence: `(E: temporal/acoustic recurrence)`; lexical support from `(E: ءحد B001/B002)`, `(E: صمد B001/B002)`, `(E: ولد B003)`.
- Frozen model: sound recurrence keeps earlier items available for reactivation as the passage moves from positive predicates to negations.
- Predictions at freeze: final `أحد` should feel like acoustic and lexical closure.
- Unused features tested: final no-peer construction.
- Corroborators: `(C: final أحد repeats both sound and lexeme)`, `(C: ayah closure after delayed subject)`.
- Constraints: `(K: sound recurrence alone does not license lexical synthesis; it only supports temporal availability)`.
- Grade: medium.
- Rationale: useful for hearing-based reactivation, but weaker than morphosyntax and branch content.

## Multi-seed convergence

Several independent seeds converge on the same compact relational model:

```text
قول B001 + quote attachment
  → content must be spoken
ءله B002 repetition
  → one named referent remains active
ءحد B001
  → positive unity
صمد B001 / B002
  → reliance-center or compact integrity
ولد B003 active/passive + ولد B005
  → no outgoing/incoming birth or derivation
كفء B001 + كون B001 + ءحد B002
  → no peer exists for him, not any candidate
```

Frozen synthesis:

The passage first fixes a named referent in commanded speech, predicates unity, then predicates `ٱلصَّمَدُ` as a central/reliance role with a secondary compact-integrity image. The following negated pair removes birth in both directions; the final negated copular clause removes the broader peer/equivalence role and reactivates the first `أَحَدٌ` as exhaustive closure.

Short interpretation generated by the image process:

The strongest temporal reactivation is the path from first `أَحَدٌ` to final `أَحَدٌۢ`: the first establishes one-ness; `ٱلصَّمَدُ` thickens that one-ness into centrality/compactness; `لَمْ يَلِدْ وَلَمْ يُولَدْ` blocks genealogical relations; `وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ` closes the passage by denying any equivalent candidate at all.
