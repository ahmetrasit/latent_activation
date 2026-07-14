# Stage 1 Pass 2 — S112 comparator main lane

Assigned passage: S112, ayat 1–4.

Sacred Arabic sequence:

```text
opening context: بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
112:1 قُلْ هُوَ ٱللَّهُ أَحَدٌ
112:2 ٱللَّهُ ٱلصَّمَدُ
112:3 لَمْ يَلِدْ وَلَمْ يُولَدْ
112:4 وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ
```

## Root cause of the Pass 1 limitation

The limitation was not a lack of permitted resources. It was an output-structure failure: many weak or unlikely seeds were compressed into a compact audit table, while the detailed findings showed only selected branches. That made the work look selection-biased and did not give every occurrence×branch seed its own full lifecycle. Pass 2 corrects that by restarting from the first rooted word, giving each lexical seed an explicit sweep, freeze, post-freeze test, rejection/fork note, and grade.

I did not read any prior output file to make this pass. The diagnosis above is based on the instruction for Pass 2 and the known defect in the Pass 1 method.

## Permitted-resource audit

Used resources:

- `resources/quran/surah_112.json`
- `v1/prompts/stage1.md`
- `resources/qac.sqlite`: schema inspected; S112 ayat 1–4 words and morphemes only
- `resources/attachments.tsv`: header and S112 ayat 1–4 rows only
- `resources/furuq_v4.sqlite`: schema inspected; `contaminated='no'` branches only for S112 ayat 1–4 roots

Not used: other output files, translations, tafsir, hadith, web sources, or external interpretation.

QAC returned no ayah-0 basmala rows for S112. The sacred Arabic basmala is therefore retained only as opening-context sequence text and never as a lexical seed or furuq branch source.

## QAC rooted sequence

| Ref | Surface | Root | Lemma | Morphology |
| --- | --- | --- | --- | --- |
| 112:1:1 | قُلْ | قول | قَالَ | V, imperative, 2MS |
| 112:1:2 | هُوَ | — | — | PRON, 3MS |
| 112:1:3 | ٱللَّهُ | ءله | ٱللَّه | PN, nominative |
| 112:1:4 | أَحَدٌ | ءحد | أَحَد | N, masculine, indefinite, nominative |
| 112:2:1 | ٱللَّهُ | ءله | ٱللَّه | PN, nominative |
| 112:2:2 | ٱلصَّمَدُ | صمد | صَّمَد | DET + N, masculine singular, nominative |
| 112:3:1 | لَمْ | — | لَم | NEG |
| 112:3:2 | يَلِدْ | ولد | وَلَدَ | V, imperfect jussive, active, 3MS |
| 112:3:3 | وَلَمْ | — | لَم | CONJ + NEG |
| 112:3:4 | يُولَدْ | ولد | وَلَدَ | V, imperfect jussive, passive, 3MS |
| 112:4:1 | وَلَمْ | — | لَم | CONJ + NEG |
| 112:4:2 | يَكُن | كون | كَانَ | V, imperfect jussive, 3MS |
| 112:4:3 | لَّهُۥ | — | — | P لَـ + PRON 3MS |
| 112:4:4 | كُفُوًا | كفء | كُفُو | N, masculine, indefinite, accusative |
| 112:4:5 | أَحَدٌۢ | ءحد | أَحَد | N, masculine, indefinite, nominative |

## Attachment rows used structurally only

- 112:1 a1: `هُوَ` begins the quoted complement of `قُلْ`.
- 112:1 a2: `أَحَدٌ` is the nominative predicate of `ٱللَّهُ`.
- 112:1 a3: `ٱللَّهُ` can stand as apposition to `هُوَ`.
- 112:2 a1: `ٱلصَّمَدُ` is the nominative predicate of `ٱللَّهُ`.
- 112:3 a1: `يَلِدْ` is governed by `لَمْ` as a jussive negated imperfect.
- 112:3 a2: `يُولَدْ` is coordinated with `يَلِدْ`.
- 112:3 a3: `يُولَدْ` is governed by `لَمْ` as a jussive negated passive imperfect.
- 112:4 a1: `يَكُن` is governed by `لَمْ` as a jussive negated imperfect.
- 112:4 a2: `لَّهُۥ` is governed by `لَـ` as the complement of `كُفُوًا`.
- 112:4 a3: `كُفُوًا` is the accusative predicate of the negated copula `يَكُن`.
- 112:4 a4: final `أَحَدٌۢ` is the delayed nominative subject of `يَكُن`.

## Uncontaminated root dossiers

Each lexical and constructional seed below visited the same full S112 root dossier sweep:

```text
FULL-S112-SWEEP =
  قول B001–B016
  ءله B001–B002
  ءحد B001–B006
  صمد B001–B007
  ولد B001–B006
  كون B001–B006
  كفء B001–B005
```

The exact branch dossier content is:

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

## Lexical seed universe and order

Lexical seeds are occurrence × branch, in recitation order from the first rooted word:

```text
112:1:1 قُلْ / قول B001–B016 = 16
112:1:3 ٱللَّهُ / ءله B001–B002 = 2
112:1:4 أَحَدٌ / ءحد B001–B006 = 6
112:2:1 ٱللَّهُ / ءله B001–B002 = 2
112:2:2 ٱلصَّمَدُ / صمد B001–B007 = 7
112:3:2 يَلِدْ / ولد B001–B006 = 6
112:3:4 يُولَدْ / ولد B001–B006 = 6
112:4:2 يَكُن / كون B001–B006 = 6
112:4:4 كُفُوًا / كفء B001–B005 = 5
112:4:5 أَحَدٌۢ / ءحد B001–B006 = 6
Total = 62 lexical seed passes.
```

## Lexical seed passes

### 112:1:1 `قُلْ` / قول

#### L001 — قول B001 — utterance released into the quote

- Seed image: articulated speech comes out by command `(E: ق و ل B001)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: attachment 112:1 a1 quoted_complement)`, `(E: ء ل ه B002 name in the quote)`, `(E: ء ح د B001 predicate unity)`.
- Image and frozen model: `قُلْ` opens a speech event whose content is not free-floating; the quote complement immediately supplies pronoun, name, and unity predicate. Frozen model: commanded utterance → fixed named referent → positive unity.
- Predictions at freeze: the same referent should persist; later words should complete or protect the quoted content rather than introduce a rival speaker or addressee.
- Unused tested after freeze: repeated `ٱللَّهُ`, `ٱلصَّمَدُ`, both ولد verbs, final `كُفُوًا أَحَدٌ`.
- Corroborators: `(C: repetition 112:2:1 ٱللَّهُ)`, `(C: 3MS morphology on يلد / يولد / يكن and لَّهُۥ)`, `(C: ك ف ء B001 + ء ح د B002 final no-peer closure)`.
- Constraints / rejected branches: `(K: قول B001 supplies speech-frame only, not the lexical content of unity, ṣamad, birth, or peerhood)`.
- Rival forks: قول B013 and B016 create weak doctrine/definition forks, but B001 is the local constructional anchor.
- Grade: medium-strong. Rationale: exact local morphology and attachment fit; passage-scale synthesis depends on later roots.

#### L002 — قول B002 — tongue as instrument

- Seed image: speech requires a tongue/instrument `(E: ق و ل B002)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none beyond the local imperative form.
- Image and frozen model: the seed opens an instrument role, but no passage word supplies `لسان`, body, organ, or tool. Frozen model: unfilled speech-instrument frame.
- Predictions at freeze: a tongue/body/instrument cue would be needed for growth.
- Unused tested after freeze: all later named predicates and negations.
- Corroborators: none.
- Constraints / rejected branches: `(K: attachment 112:1 a1 makes quoted content, not tongue, the complement)`, `(K: no body-part or instrument role appears)`.
- Rival forks: none.
- Grade: unlikely. Rationale: locally related to speech but no passage-local role completion.

#### L003 — قول B003 — loquacious speaker

- Seed image: a person characterized by abundant speech `(E: ق و ل B003)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the branch expects a speaker-character quality, but `قُلْ` is a command to utter one content unit. Frozen model: terminated speaker-trait image.
- Predictions at freeze: a human description, repeated speaking, or كثرة القول cue would be needed.
- Unused tested after freeze: the quote, divine name, predicates, and negations.
- Corroborators: none.
- Constraints / rejected branches: `(K: imperative قُلْ does not describe the commanded addressee as قوال/مقوال)`, `(K: no كثرة or human-character predicate)`.
- Rival forks: قول B007 circulating speech also fails for lack of social diffusion.
- Grade: unlikely. Rationale: no textual complement.

#### L004 — قول B004 — holder of effective saying

- Seed image: `القيل` as a title/possessor of socially effective speech `(E: ق و ل B004)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the seed searches for title, rank, or sovereign speech-owner roles. The passage gives a command verb plus quoted content, not an office.
- Predictions at freeze: a title, named ruler, or rank relation would be required.
- Unused tested after freeze: all predicates and negations.
- Corroborators: none.
- Constraints / rejected branches: `(K: no قيل/ملك/صاحب قول construction)`, `(K: ٱللَّهُ is the quoted referent, not a قول-derived title)`.
- Rival forks: none.
- Grade: unlikely. Rationale: branch image is remote and unfilled.

#### L005 — قول B005 — fabricated or attributed saying

- Seed image: saying what was not, or attributing what was not said `(E: ق و ل B005)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: possible contact with later `لَمْ يَكُن` was tested but not selected.
- Image and frozen model: the seed predicts false attribution, but the syntax supplies commanded quote-content without any lie, attribution dispute, or `تقول` form. Frozen model: defeated false-speech frame.
- Predictions at freeze: a negated-being phrase might have helped only if it were the object of fabricated speech.
- Unused tested after freeze: `لَمْ يَكُن`, final no-peer clause.
- Corroborators: none.
- Constraints / rejected branches: `(K: final لَمْ يَكُن is a negated copular clause about كفوا, not "saying what was not")`, `(K: no كذب/تقول/نسبة عليه structure)`.
- Rival forks: none.
- Grade: unlikely. Rationale: surface contact with `لم يكن` is misleading and structurally blocked.

#### L006 — قول B006 — drawing a saying inward

- Seed image: a saying drawn to oneself `(E: ق و ل B006)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the seed seeks inward appropriation of speech; the local event is outward commanded utterance with a quote complement.
- Predictions at freeze: self-directed speech or inner acquisition would be needed.
- Unused tested after freeze: pronoun chain and predicates.
- Corroborators: none.
- Constraints / rejected branches: `(K: قُلْ is outward imperative)`, `(K: قول B012 inner-speech fork also loses to the explicit utterance frame)`.
- Rival forks: قول B012 inner saying.
- Grade: unlikely. Rationale: direction is wrong for the local construction.

#### L007 — قول B007 — circulating report among people

- Seed image: speech diffusing as public talk `(E: ق و ل B007)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: قول B001 utterance)`, weakly.
- Image and frozen model: the command may initiate recitable speech, but the passage itself supplies no social circulation scene. Frozen model: utterance that does not become a local public-rumor network.
- Predictions at freeze: words for الناس, spread, repeated speakers, or report circulation would be expected.
- Unused tested after freeze: all later clauses.
- Corroborators: `(C: quoted-content structure)` only supports speech, not diffusion.
- Constraints / rejected branches: `(K: no الناس/قالة/قيل وقال)`, `(K: a single commanded quote is not enough to build circulation)`.
- Rival forks: none.
- Grade: weak. Rationale: possible recitational afterlife, but not passage-local.

#### L008 — قول B008 — stick for striking the game-piece

- Seed image: `قال` as a stick used to strike a small game object `(E: ق و ل B008)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the branch needs a physical stick, game, striker, object, or impact. None appears.
- Predictions at freeze: an instrument/impact scene would be needed.
- Unused tested after freeze: ṣamad striking branch B006 and final equivalence branches were checked.
- Corroborators: none.
- Constraints / rejected branches: `(K: ص م د B006 also lacks ضرب/عصا roles)`, `(K: قُلْ is not a noun for an implement here)`.
- Rival forks: صمد B006 impact fork also terminates.
- Grade: unlikely. Rationale: no local material scene.

#### L009 — قول B009 — negotiation over an affair

- Seed image: reciprocal discussion or negotiation `(E: ق و ل B009)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the branch needs two negotiating parties or a reciprocal form. The passage has a unilateral imperative and a quoted proposition.
- Predictions at freeze: reciprocal morphology or a contested matter would be needed.
- Unused tested after freeze: predicates and negations.
- Corroborators: none.
- Constraints / rejected branches: `(K: no تقاول/قاولته morphology)`, `(K: quoted complement is not negotiated)`.
- Rival forks: none.
- Grade: unlikely. Rationale: no reciprocal structure.

#### L010 — قول B010 — imposing judgment over another

- Seed image: speech as controlling judgment `(E: ق و ل B010)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the branch searches for coercion or imposed rule. The passage instead supplies declarative quoted content.
- Predictions at freeze: object of control, adversary, or حكم relation would be required.
- Unused tested after freeze: no-peer clause.
- Corroborators: none.
- Constraints / rejected branches: `(K: no تحكم or عليه relation)`, `(K: final له is complement of كفوا, not a control target)`.
- Rival forks: none.
- Grade: unlikely. Rationale: unsupported role frame.

#### L011 — قول B011 — saying as supposing/thinking

- Seed image: `قول` behaves like ظن, opening a mental-supposition complement `(E: ق و ل B011)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the passage gives imperative utterance, not a verb governing two objects like a mental-state verb.
- Predictions at freeze: interrogative/suppositional syntax would be needed.
- Unused tested after freeze: quote complement and nominal predicates.
- Corroborators: none.
- Constraints / rejected branches: `(K: attachment 112:1 a1 is quoted content, not ظن-like government)`.
- Rival forks: قول B012 inner-speech and B013 belief remain separate.
- Grade: unlikely. Rationale: syntax blocks the branch.

#### L012 — قول B012 — unexpressed saying in the self

- Seed image: a saying held inwardly before vocal expression `(E: ق و ل B012)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the seed is immediately constrained by the imperative to say. Frozen model: inner-speech image defeated by commanded articulation.
- Predictions at freeze: an inward/hidden-saying cue would be needed.
- Unused tested after freeze: quote structure and pronoun chain.
- Corroborators: none.
- Constraints / rejected branches: `(K: قُلْ activates expression, not withholding)`, `(K: قول B001 is the stronger local branch)`.
- Rival forks: none.
- Grade: unlikely. Rationale: opposite of the local activation event.

#### L013 — قول B013 — doctrine or belief as قول

- Seed image: a `قول` as held position or doctrine `(E: ق و ل B013)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ء ل ه B002)`, `(E: ء ح د B001)`, `(E: ص م د B001)`, `(E: ولد B003 active/passive as content)`, `(E: كفء B001 final relation)`.
- Image and frozen model: the quoted proposition can be secondarily heard as a compact doctrinal saying: named referent, unity, ṣamad, no birth, no peer. Frozen model: uttered position-content.
- Predictions at freeze: content should remain proposition-like and cohesive.
- Unused tested after freeze: final delayed `أحد`, ayah closure.
- Corroborators: `(C: final ء ح د B002 closes the proposition)`, `(C: sequence positive predicates → negated relations)`.
- Constraints / rejected branches: `(K: local verb is still imperative utterance; no explicit اعتقاد or believer role)`.
- Rival forks: قول B016 definition-like boundary.
- Grade: weak. Rationale: coherent as a secondary reading, but branch is not the local verbal sense.

#### L014 — قول B014 — a thing saying by indication

- Seed image: nonverbal indication, as if a thing “says” its state `(E: ق و ل B014)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the seed looks for an object whose state indicates something. The passage uses explicit speech command and quoted language.
- Predictions at freeze: a non-speaking object or state-sign would be needed.
- Unused tested after freeze: ṣamad B002 compactness and final closure.
- Corroborators: none.
- Constraints / rejected branches: `(K: explicit قُلْ prevents replacing speech with nonverbal indication)`.
- Rival forks: none.
- Grade: unlikely. Rationale: no local nonverbal indicator.

#### L015 — قول B015 — sincere care for a matter

- Seed image: saying as devoted concern for something `(E: ق و ل B015)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the branch searches for care/concern relation; the passage has no object of عناية.
- Predictions at freeze: a concern-object or care predicate would be needed.
- Unused tested after freeze: ṣamad B001 reliance was checked but not selected because it does not supply قول بكذا.
- Corroborators: none.
- Constraints / rejected branches: `(K: no يقول بكذا construction)`, `(K: صمد B001 is reliance-centered, not قول-care syntax)`.
- Rival forks: none.
- Grade: unlikely. Rationale: unsupported construction.

#### L016 — قول B016 — definition or limit

- Seed image: a saying as a defining boundary `(E: ق و ل B016)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ء ل ه B002 named subject)`, `(E: ء ح د B001 positive boundary)`, `(E: ص م د B001/B002 predicate fork)`.
- Image and frozen model: the uttered content can weakly form a definition-like boundary: name, unity, ṣamad, then negations. Frozen model: compact limit-statement, not technical definition.
- Predictions at freeze: later material should narrow the referent by exclusion.
- Unused tested after freeze: ولد pair and final no-peer construction.
- Corroborators: `(C: و ل د B003 active/passive exclusions)`, `(C: ك ف ء B001 + ء ح د B002 final exhaustive boundary)`.
- Constraints / rejected branches: `(K: no technical حد language; قول B001 remains primary)`.
- Rival forks: B013 doctrine-like content.
- Grade: weak. Rationale: the whole passage has boundary-like force, but the branch is remote.

### 112:1:3 `ٱللَّهُ` / ءله

#### L017 — ءله B001 — worshipped/mabud referent inside the quote

- Seed image: a worshipped/mabud referent enters the quoted content `(E: ء ل ه B001)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: attachment 112:1 a3 apposition)`, `(E: ء ح د B001)`, `(E: ص م د B001)`.
- Image and frozen model: the named referent is heard through worship/reliance possibility; `أَحَدٌ` narrows him to one and `ٱلصَّمَدُ` later makes him a directed reliance center. Frozen model: exclusive worshipped/reliance center.
- Predictions at freeze: no family, source, product, or equal should share the field.
- Unused tested after freeze: ولد B003/B005, كفء B001, final ءحد B002.
- Corroborators: `(C: و ل د B003 active/passive negation)`, `(C: و ل د B005 no derivation)`, `(C: ك ف ء B001 no peer)`, `(C: ء ح د B002 no candidate)`.
- Constraints / rejected branches: `(K: no explicit عبد/تنسك action occurs; the branch is secondary to the proper-name use)`.
- Rival forks: ءله B002 is morphologically more local.
- Grade: medium. Rationale: coherent and passage-scale, but not explicit as worship-action.

#### L018 — ءله B002 — divine name fixed in the quote

- Seed image: `ٱللَّهُ` enters as a proper named referent `(E: ء ل ه B002)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: attachment 112:1 a3)`, `(E: attachment 112:1 a2)`, `(E: ء ح د B001)`.
- Image and frozen model: the pronoun points, the name fixes the referent, and `أَحَدٌ` predicates unity. Frozen model: named referent + unity predicate.
- Predictions at freeze: the same name/referent should be reactivated; later 3MS forms should not shift referent.
- Unused tested after freeze: repeated `ٱللَّهُ`, `ٱلصَّمَدُ`, ولد pair, final no-peer.
- Corroborators: `(C: repetition 112:2:1 ٱللَّهُ)`, `(C: 3MS continuity)`, `(C: ك ف ء B001 + ء ح د B002 closure)`.
- Constraints / rejected branches: `(K: B002’s oath/vocative examples are not local; the local feature is the name)`.
- Rival forks: ءله B001 worshipped/reliance.
- Grade: strong. Rationale: exact QAC proper-name fit and strong temporal reactivation.

### 112:1:4 `أَحَدٌ` / ءحد

#### L019 — ءحد B001 — positive unity

- Seed image: one-ness/unity predicated of the named referent `(E: ء ح د B001)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ء ل ه B002)`, `(E: attachment 112:1 a2 predication)`, `(E: ص م د B001)`, rival `(E: ص م د B002)`.
- Image and frozen model: the first `أَحَدٌ` establishes positive unity; `ٱلصَّمَدُ` later thickens it as reliance-center or compact integrity. Frozen model: one named referent with central/compact predicate.
- Predictions at freeze: later clauses should deny multiplicity routes: birth out, birth from, and peer.
- Unused tested after freeze: ولد B003/B005, كون B001, كفء B001, final ءحد B002.
- Corroborators: `(C: و ل د B003 active/passive)`, `(C: و ل د B005 no derivation)`, `(C: ك ف ء B001 no equal)`, `(C: ء ح د B002 final negative-exhaustive reactivation)`.
- Constraints / rejected branches: `(K: no counting/compound numeral structure; ءحد B003 rejected)`.
- Rival forks: صمد B001 relational fork stronger; صمد B002 image-rich secondary fork.
- Grade: strong. Rationale: predicts and is reactivated by the final closure.

#### L020 — ءحد B002 — negative-exhaustive one seeded at the first occurrence

- Seed image: `أحد` under negation exhausts a candidate class `(E: ء ح د B002)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none at first occurrence; delayed fork selected only when final `أحد` appears after freeze.
- Image and frozen model: locally this branch stalls because 112:1:4 is positive nominative predicate, not negative scope. Frozen model: premature negative-exhaustive image.
- Predictions at freeze: a later negated `أحد` could rescue the branch by reactivation.
- Unused tested after freeze: final `وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ`.
- Corroborators: `(C: final ء ح د B002 under negation)`, `(C: ك ف ء B001 peer role)`.
- Constraints / rejected branches: `(K: attachment 112:1 a2 makes first أحد a positive predicate)`.
- Rival forks: first occurrence B001 primary.
- Grade: weak. Rationale: fails locally, later becomes a reactivated echo.

#### L021 — ءحد B003 — counting and composition

- Seed image: numerical one in counting or compound numerals `(E: ء ح د B003)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the seed needs a counted object, numeral sequence, or compound like eleven. The passage gives predicate `أحد`.
- Predictions at freeze: a count frame would be required.
- Unused tested after freeze: repeated `أحد`, final no-peer clause.
- Corroborators: none.
- Constraints / rejected branches: `(K: both أحد tokens are indefinite nominals in predication/subject positions, not compound numerals)`.
- Rival forks: none.
- Grade: unlikely. Rationale: no counting syntax.

#### L022 — ءحد B004 — first/additive/day-name

- Seed image: firstness through addition or the day-name Sunday `(E: ء ح د B004)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the branch seeks إضافة, sequence-first role, or day-name. None appears.
- Predictions at freeze: an iḍāfa or calendrical construction would be needed.
- Unused tested after freeze: ayah order and repeated `أحد`.
- Corroborators: none.
- Constraints / rejected branches: `(K: first أحد is not مضاف)`, `(K: no day-name or calendrical frame)`.
- Rival forks: temporal order does not supply B004.
- Grade: unlikely. Rationale: structural conditions absent.

#### L023 — ءحد B005 — isolated individuals one by one

- Seed image: singularization or coming individually `(E: ء ح د B005)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: weak `(E: ء ح د B001 unity-neighbor)`.
- Image and frozen model: the branch can make a faint individualization image, but the local predicate is absolute unity rather than scattered individuals. Frozen model: individualization fork constrained by predication.
- Predictions at freeze: later no-peer clause might scan possible individuals.
- Unused tested after freeze: final `أحد` under negation.
- Corroborators: `(C: final ء ح د B002 can exhaust individual candidates)`.
- Constraints / rejected branches: `(K: no آحادا/multiple individuals coming separately)`, `(K: B001 is the exact first-occurrence fit)`.
- Rival forks: final occurrence B005 is stronger than first occurrence.
- Grade: weak. Rationale: related individual-candidate logic, but not local syntax.

#### L024 — ءحد B006 — Mount Uḥud

- Seed image: the place-name/mountain Uḥud `(E: ء ح د B006)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: no place-name, mountain, or locative frame appears.
- Predictions at freeze: geographical or mountain cues would be needed.
- Unused tested after freeze: صمد B002 rock/solid branch was tested but not selected.
- Corroborators: none.
- Constraints / rejected branches: `(K: صمد B002 solid/rock image cannot convert أحد into a mountain name)`, `(K: no place syntax)`.
- Rival forks: none.
- Grade: unlikely. Rationale: homonymous branch is locally unsupported.

### 112:2:1 `ٱللَّهُ` / ءله

#### L025 — ءله B001 — worshipped/reliance center after unity

- Seed image: the named referent returns after unity as worshipped/mabud `(E: ء ل ه B001)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: prior ء ح د B001 active context)`, `(E: ص م د B001)`, `(E: attachment 112:2 a1 predication)`.
- Image and frozen model: the repeated name reopens the one referent and `ٱلصَّمَدُ` gives the worshipped/reliance-oriented center. Frozen model: one worshipped/reliance center.
- Predictions at freeze: no parent, child, derived product, or peer should remain.
- Unused tested after freeze: ولد B003/B005, كفء B001, final ءحد B002.
- Corroborators: `(C: و ل د B003 active/passive)`, `(C: و ل د B005 derivation denied)`, `(C: ك ف ء B001)`, `(C: ء ح د B002)`.
- Constraints / rejected branches: `(K: no explicit عبد action)`.
- Rival forks: ءله B002 repeated-name hinge.
- Grade: medium-strong. Rationale: sequence and ṣamad complete the worship/reliance field.

#### L026 — ءله B002 — repeated name as reactivation hinge

- Seed image: the proper name returns at a new ayah boundary `(E: ء ل ه B002)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: repetition from 112:1:3)`, `(E: ص م د B001)`, `(E: attachment 112:2 a1 predication)`.
- Image and frozen model: the repeated name reactivates the referent fixed in 112:1 and gives him a second predicate. Frozen model: same named referent → ṣamad predicate.
- Predictions at freeze: later 3MS verbs/pronoun should keep that referent active.
- Unused tested after freeze: ولد pair, `يكن`, `له`, `كفوا`, final `أحد`.
- Corroborators: `(C: 3MS morphology throughout 112:3–4)`, `(C: ك ف ء B001 + ء ح د B002 final closure)`.
- Constraints / rejected branches: `(K: oath/vocative examples in B002 are not local; repeated name is local)`.
- Rival forks: ءله B001.
- Grade: strong. Rationale: clear temporal reactivation and role handoff.

### 112:2:2 `ٱلصَّمَدُ` / صمد

#### L027 — صمد B001 — intended/reliance center

- Seed image: the one intended and relied upon `(E: ص م د B001)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ء ل ه B002 repeated subject)`, `(E: ء ح د B001 prior unity)`, `(E: attachment 112:2 a1)`.
- Image and frozen model: after unity, `ٱلصَّمَدُ` creates directed centrality: the named one is the reliance target. Frozen model: exclusive reliance-center.
- Predictions at freeze: no generational or equivalence relation should create another center.
- Unused tested after freeze: ولد B003/B005, كفء B001, final ءحد B002.
- Corroborators: `(C: و ل د B003 active/passive blocks family roles)`, `(C: و ل د B005 blocks derivation)`, `(C: ك ف ء B001 blocks a parallel)`, `(C: ء ح د B002 exhausts candidates)`.
- Constraints / rejected branches: `(K: B001 does not itself state no-birth/no-peer; those are post-freeze tests)`.
- Rival forks: B002 compact integrity; B007 endurance.
- Grade: strong. Rationale: excellent order explanation: unity → reliance center → protected from relational rivals.

#### L028 — صمد B002 — compact non-hollow solidity

- Seed image: dense compactness without inner hollow `(E: ص م د B002)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ء ح د B001 unity)`, `(E: ء ل ه B002 repeated subject)`.
- Image and frozen model: the passage can form a secondary simulation of one compact integrity, not a material object but an image of indivisible fullness. Frozen model: compact unity.
- Predictions at freeze: no internal split, derived product, origin, or counterpart should be supplied.
- Unused tested after freeze: ولد B003/B005, كفء B001, final ءحد B002.
- Corroborators: `(C: و ل د B005 no generated derivative)`, `(C: و ل د B003 active/passive no birth relation)`, `(C: ك ف ء B001 no equivalent)`, `(C: ء ح د B002 no candidate)`.
- Constraints / rejected branches: `(K: syntax predicates ٱلصَّمَدُ; no literal rock/body/material object is supplied)`.
- Rival forks: B001 more direct; B002 image-rich.
- Grade: medium-strong. Rationale: coherent secondary image with strong later constraints, but must not override primary predication.

#### L029 — صمد B003 — sealed bottle-stopper

- Seed image: a tight stopper sealing a vessel `(E: ص م د B003)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: weak final closure structure tested but not selected as literal expansion.
- Image and frozen model: the branch expects bottle/vessel, stopper, seal, or opening. The passage supplies relational closure but no container object.
- Predictions at freeze: vessel or mouth/opening terms would be needed.
- Unused tested after freeze: final no-peer closure.
- Corroborators: none.
- Constraints / rejected branches: `(K: final closure is existential/relational, not a bottle-sealing scene)`, `(K: no قارورة/عفاص/سدادة role)`.
- Rival forks: صمد B002 compactness is the viable non-hollow fork.
- Grade: unlikely. Rationale: closure analogy lacks lexical roles.

#### L030 — صمد B004 — head bound with a cloth

- Seed image: wrapping/binding the head `(E: ص م د B004)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the branch requires head, cloth, wrapping, or bandaging; none appears.
- Predictions at freeze: body/clothing cues would be needed.
- Unused tested after freeze: all negations and final relation.
- Corroborators: none.
- Constraints / rejected branches: `(K: no رأس/خرقة/منديل/ثوب role)`, `(K: ٱلصَّمَدُ is a nominative predicate, not an action of binding)`.
- Rival forks: none.
- Grade: unlikely. Rationale: no local complement.

#### L031 — صمد B005 — overseeing an affair with concern

- Seed image: standing over an affair with care `(E: ص م د B005)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: weak `(E: ء ل ه B001 worshipped/reliance context)`.
- Image and frozen model: the branch looks for an `أمر` object or supervisory relation. The passage gives a predicate of the named referent without an explicit affair.
- Predictions at freeze: a matter/affair governed by concern would be needed.
- Unused tested after freeze: ولد pair and final no-peer.
- Corroborators: none specific.
- Constraints / rejected branches: `(K: no أمر or حفل به construction)`, `(K: صمد B001 is the stronger directed-reliance branch)`.
- Rival forks: B001.
- Grade: weak. Rationale: shares central concern with B001 but lacks local syntax.

#### L032 — صمد B006 — striking with a stick

- Seed image: striking someone with a staff `(E: ص م د B006)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the branch needs striker, staff, patient, impact. None appears.
- Predictions at freeze: ضرب/عصا or object-patient cues would be needed.
- Unused tested after freeze: قول B008 stick branch.
- Corroborators: none.
- Constraints / rejected branches: `(K: no ضرب/عصا role)`, `(K: قول B008 also fails; no physical impact scene)`.
- Rival forks: none.
- Grade: unlikely. Rationale: no local support.

#### L033 — صمد B007 — endurance under severity

- Seed image: persistence/remaining under harsh conditions `(E: ص م د B007)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: temporal sequence across repeated لَمْ)` weakly.
- Image and frozen model: `ٱلصَّمَدُ` can weakly form an endurance image: the same referent remains unchanged through a chain of negated possible relations. Frozen model: enduring identity under negation.
- Predictions at freeze: later clauses should preserve the same referent through repeated testing.
- Unused tested after freeze: 3MS continuity, final no-peer.
- Corroborators: `(C: 3MS morphology on يلد / يولد / يكن / له)`, `(C: repeated negation sequence)`.
- Constraints / rejected branches: `(K: no local cold/drought/hardship term; الشدة is branch-imported)`.
- Rival forks: B001 and B002 stronger.
- Grade: weak. Rationale: temporal continuity supports it faintly, but severity is absent.

### 112:3:2 `يَلِدْ` / ولد

#### L034 — ولد B001 — offspring output denied

- Seed image: offspring/child as the product of lineage, immediately under negation `(E: و ل د B001)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: negation/mood 112:3 a1)`, `(E: و ل د B003 event dimension)`, `(E: coordinated passive 112:3 a2)`.
- Image and frozen model: active `يَلِدْ` denies a child-output role from the referent. Frozen model: no offspring branch leaves him.
- Predictions at freeze: inverse parent-origin and broader peer roles should also be denied.
- Unused tested after freeze: passive `يُولَدْ`, كفء B001, final ءحد B002.
- Corroborators: `(C: passive و ل د B003 denies inverse birth)`, `(C: ك ف ء B001 no equal)`, `(C: ء ح د B002 no candidate)`.
- Constraints / rejected branches: `(K: local form is verbal, so B003 event is the anchor; B001 is a role inferred from it)`.
- Rival forks: B003 direct event; B005 broader derivation.
- Grade: medium-strong. Rationale: strong role completion but less direct than B003.

#### L035 — ولد B002 — parent role from the active verb

- Seed image: parental relation is activated from the birth root `(E: و ل د B002)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: active يلد under لَمْ)` weakly, `(E: و ل د B003 event dimension)`.
- Image and frozen model: active `يَلِدْ` could imply becoming a parent, but the passage denies the birth event rather than naming father/mother. Frozen model: no parent-by-birth role, weakly.
- Predictions at freeze: passive birth should deny the inverse origin slot.
- Unused tested after freeze: passive `يُولَدْ`, final no-peer.
- Corroborators: `(C: passive يلد pair closes parent/child vectors)`, `(C: ك ف ء B001 generalizes beyond kinship)`.
- Constraints / rejected branches: `(K: no والد/والدة noun appears)`, `(K: B003 is more exact)`.
- Rival forks: B001 offspring output.
- Grade: weak. Rationale: plausible role implication but not branch-exact locally.

#### L036 — ولد B003 — active birth event denied

- Seed image: an outgoing birth event is activated and cancelled `(E: و ل د B003 active-before-freeze)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: attachment 112:3 a1)`, `(E: coordination 112:3 a2)`, `(E: و ل د B003 passive counterpart)`.
- Image and frozen model: the passage tests birth in the outgoing direction and cancels it, then immediately cancels the incoming passive direction. Frozen model: bidirectional birth-relation shutdown.
- Predictions at freeze: final material should broaden from birth to general equivalence.
- Unused tested after freeze: كون B001, كفء B001, final ءحد B002, earlier ءحد/صمد.
- Corroborators: `(C: ك ف ء B001 broader peer role)`, `(C: ك و ن B001 negated occurrence)`, `(C: ء ح د B002 exhaustive candidate denial)`, `(C: prior ء ح د B001 + ص م د B001 explain why the denial matters)`.
- Constraints / rejected branches: `(K: ولد is negated; no positive birth scene is asserted)`.
- Rival forks: B005 derivation generalization.
- Grade: strong. Rationale: exact morphology, order, and final expansion.

#### L037 — ولد B004 — newborn or young servant

- Seed image: newborn/child near birth or slave-girl/boy role `(E: و ل د B004)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the local form is a verb, not وليد/وليدة, and no youth/servitude role appears.
- Predictions at freeze: a nominal youth/servant cue would be needed.
- Unused tested after freeze: active/passive pair and final no-peer.
- Corroborators: none.
- Constraints / rejected branches: `(K: no وليد/وليدة noun)`, `(K: no servitude or youth scene)`.
- Rival forks: B001/B003.
- Grade: unlikely. Rationale: branch-specific roles absent.

#### L038 — ولد B005 — derivative output denied

- Seed image: something produced from something else or newly derived `(E: و ل د B005 active-outward)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: active negated يلد)`, `(E: coordinated passive يولد)`.
- Image and frozen model: the branch widens birth into derivation: nothing is generated from him, and he is not generated from another. Frozen model: no derivation outward/inward.
- Predictions at freeze: final denial should move to general equivalence rather than another genealogy item.
- Unused tested after freeze: كفء B001, كون B001, final ءحد B002.
- Corroborators: `(C: ك ف ء B001 no comparable counterpart)`, `(C: ك و ن B001 no occurrence)`, `(C: ء ح د B002 no candidate)`.
- Constraints / rejected branches: `(K: B005 is broader than the concrete birth verb; B003 anchors the local event)`.
- Rival forks: B003.
- Grade: medium-strong. Rationale: good bridge from birth to no-peer closure, but broader than local morphology.

#### L039 — ولد B006 — same-age peer

- Seed image: a peer of the same birth-time/age `(E: و ل د B006)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ك ف ء B001 final peer denial)` only as a later fork, not before freeze.
- Image and frozen model: the seed expects an age-comparison peer; the passage has birth negation and later peer denial but no age equivalence.
- Predictions at freeze: a peer/equivalent cue might appear.
- Unused tested after freeze: final `كُفُوًا أَحَدٌ`.
- Corroborators: `(C: ك ف ء B001 broadly denies peerhood)`.
- Constraints / rejected branches: `(K: no لدة/سن or same-age relation)`, `(K: peerhood is handled by كفء B001, not ولد B006)`.
- Rival forks: كفء B001.
- Grade: weak. Rationale: final no-peer supports a distant peer idea, but not same-age birth.

### 112:3:4 `يُولَدْ` / ولد

#### L040 — ولد B001 — being offspring denied

- Seed image: being a born child/offspring, in passive form and under negation `(E: و ل د B001 passive-role)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: passive voice)`, `(E: negation/mood 112:3 a3)`, `(E: و ل د B003 event dimension)`.
- Image and frozen model: passive `يُولَدْ` denies that the referent occupies the born-offspring role. Frozen model: he is not a مولود من نسل.
- Predictions at freeze: no parent-origin and no equivalent slot should remain.
- Unused tested after freeze: final no-peer clause; earlier active `يَلِدْ`.
- Corroborators: `(C: active يَلِدْ denies offspring output)`, `(C: ك ف ء B001 no peer)`, `(C: ء ح د B002 no candidate)`.
- Constraints / rejected branches: `(K: B003 event is more direct than B001 nominal role)`.
- Rival forks: B002 parent-origin; B003 event.
- Grade: medium-strong. Rationale: passive form strongly activates the born-role but via negated verb.

#### L041 — ولد B002 — parent-origin relation denied

- Seed image: father/mother origin relation implied by passive birth `(E: و ل د B002)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: passive voice)`, `(E: negation 112:3 a3)`, `(E: و ل د B003 birth-event dimension)`.
- Image and frozen model: `يُولَدْ` denies that a parental origin stands behind the referent. Frozen model: no parent-origin slot.
- Predictions at freeze: final clause should deny all equivalents, not just origins.
- Unused tested after freeze: كفء B001, كون B001, final ءحد B002.
- Corroborators: `(C: ك ف ء B001 no counterpart)`, `(C: ك و ن B001 no occurrence)`, `(C: ء ح د B002 exhaustive subject)`.
- Constraints / rejected branches: `(K: no explicit والد/والدة noun; relation is inferred from passive birth)`.
- Rival forks: B003 direct event.
- Grade: medium-strong. Rationale: role completion is strong but indirect.

#### L042 — ولد B003 — passive birth event denied

- Seed image: being born is activated and cancelled `(E: و ل د B003 passive-before-freeze)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: passive morphology)`, `(E: attachment 112:3 a3)`, `(E: coordination 112:3 a2 with active يلد)`.
- Image and frozen model: the passive form reverses the active vector: not born from another. Frozen model: no genealogical vector enters him or leaves him.
- Predictions at freeze: no peer/equivalent relation should be available.
- Unused tested after freeze: كفء B001, له pronoun, final ءحد B002.
- Corroborators: `(C: ك ف ء B001 no counterpart)`, `(C: لَّهُۥ attaches relation to same referent)`, `(C: ء ح د B002 no candidate)`.
- Constraints / rejected branches: `(K: negated passive is not a positive origin scene)`.
- Rival forks: B002 parent-origin; B005 derivation.
- Grade: strong. Rationale: exact voice, negation, coordination, and final role completion.

#### L043 — ولد B004 — newborn/young servant denied

- Seed image: newborn/young servant role `(E: و ل د B004)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the branch expects وليد/وليدة or youth/servitude roles; the local passive verb does not supply them.
- Predictions at freeze: nominal young/newborn cues would be needed.
- Unused tested after freeze: final no-peer clause.
- Corroborators: none.
- Constraints / rejected branches: `(K: no وليد/وليدة noun)`, `(K: no servitude frame)`.
- Rival forks: B001 born-role and B003 event.
- Grade: unlikely. Rationale: branch-specific scene absent.

#### L044 — ولد B005 — derivative origin denied

- Seed image: being generated or derived from something else `(E: و ل د B005 passive-inward)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: passive negation)`, `(E: active/passive pair)`.
- Image and frozen model: the referent is not produced from another source, just as active `يَلِدْ` denies derivative output. Frozen model: no derived-from or derivational-product relation.
- Predictions at freeze: no equivalent/peer should be allowed.
- Unused tested after freeze: كفء B001, final ءحد B002, prior صمد B002 if unused.
- Corroborators: `(C: ك ف ء B001 no comparable counterpart)`, `(C: ء ح د B002 no candidate)`, `(C: ص م د B002 compact integrity if not already used)`.
- Constraints / rejected branches: `(K: broad derivation must remain subordinate to concrete ولد morphology)`.
- Rival forks: B003 direct-event; B002 parent-origin.
- Grade: medium-strong. Rationale: strong bridge to final closure, broader than direct birth.

#### L045 — ولد B006 — same-age peer from passive birth

- Seed image: someone of the same birth-age `(E: و ل د B006)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: passive birth could suggest birth-time, but no same-age comparison appears. Frozen model: unfilled age-peer frame.
- Predictions at freeze: a peer/equivalent cue might weakly rescue the broad peer role.
- Unused tested after freeze: final كفء B001 / ءحد B002.
- Corroborators: `(C: ك ف ء B001 no peer)` only at a broad level.
- Constraints / rejected branches: `(K: no سن/لدة comparison)`, `(K: final peerhood is not same-age peerhood)`.
- Rival forks: كفء B001.
- Grade: weak. Rationale: distant relation to peer denial, no age-specific evidence.

### 112:4:2 `يَكُن` / كون

#### L046 — كون B001 — negated occurrence/existence

- Seed image: occurrence/presence in time, immediately denied `(E: ك و ن B001)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: attachment 112:4 a1)`, `(E: ك ف ء B001)`, `(E: ء ح د B002)`, `(E: attachments 112:4 a2/a3/a4)`.
- Image and frozen model: the final clause denies that any peer comes to presence for him. Frozen model: no occurrence/existence of a counterpart.
- Predictions at freeze: this should close the passage because the candidate set is exhausted.
- Unused tested after freeze: earlier positive `أحد`, `الصمد`, birth pair.
- Corroborators: `(C: ء ح د B001 positive unity)`, `(C: ص م د B001/B002 centrality/compactness)`, `(C: و ل د B003/B005 narrower relations already denied)`.
- Constraints / rejected branches: `(K: كون B002 place/status not required; local syntax uses كان as negated copular/existential support)`.
- Rival forks: B002 status weak.
- Grade: strong. Rationale: exact final-clause architecture and closure.

#### L047 — كون B002 — place or status

- Seed image: place, position, status, or station `(E: ك و ن B002)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: weak `(E: ك ف ء B001 status-equivalence)`.
- Image and frozen model: the branch can weakly hear `كُفُوًا` as a status-equivalent, but no place or rank location appears. Frozen model: no equal-status position, weakly.
- Predictions at freeze: a peer-status cue should appear.
- Unused tested after freeze: final `أحد`, earlier unity.
- Corroborators: `(C: ك ف ء B001 no equivalent)` supports status only broadly.
- Constraints / rejected branches: `(K: no مكان/مكانة word or locative phrase)`, `(K: attachment 112:4 a3 makes كفوا the predicate)`.
- Rival forks: B001 stronger.
- Grade: weak. Rationale: status-equivalence is possible but not the direct local sense.

#### L048 — كون B003 — surety or standing for someone

- Seed image: guaranteeing/standing as caretaker for someone `(E: ك و ن B003)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: `لَّهُۥ` might superficially invite a for-him relation, but the attachment row makes it complement of `كُفُوًا`, not surety.
- Predictions at freeze: a kafāla/caretaker relation would be needed.
- Unused tested after freeze: `لَّهُۥ`, `كُفُوًا`, final `أحد`.
- Corroborators: none.
- Constraints / rejected branches: `(K: attachment 112:4 a2 governs له by كفوا)`, `(K: no كفالة/قيام على فلان)`.
- Rival forks: none.
- Grade: unlikely. Rationale: structural row blocks the apparent role.

#### L049 — كون B004 — humbling/submission

- Seed image: submission or humbled state `(E: ك و ن B004)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: no submission actor, humility predicate, or استكانة form appears.
- Predictions at freeze: a submission/abasement role would be needed.
- Unused tested after freeze: all final-clause components.
- Corroborators: none.
- Constraints / rejected branches: `(K: يَكُن is QAC lemma كان, not استكان)`, `(K: no خضوع relation)`.
- Rival forks: none.
- Grade: unlikely. Rationale: branch image absent.

#### L050 — كون B005 — old man named from “I was”

- Seed image: a man marked by old-age reminiscence `(E: ك و ن B005)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the branch expects a human age/person-name frame; none occurs.
- Predictions at freeze: age/youth contrast or person descriptor would be needed.
- Unused tested after freeze: ولد B004 youth branch and final no-peer.
- Corroborators: none.
- Constraints / rejected branches: `(K: no الشيخ/شباب frame)`, `(K: ولد B004 also unsupported)`.
- Rival forks: none.
- Grade: unlikely. Rationale: no local roles.

#### L051 — كون B006 — bad state

- Seed image: being in a bad state `(E: ك و ن B006)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: no `كينة سوء` or bad-state predicate appears. Final clause denies peer existence, not a bad condition.
- Predictions at freeze: سوء/state wording would be needed.
- Unused tested after freeze: final no-peer clause.
- Corroborators: none.
- Constraints / rejected branches: `(K: no سوء or حال سوء phrase)`, `(K: كفوا is not a bad-state predicate)`.
- Rival forks: none.
- Grade: unlikely. Rationale: branch-specific phrase absent.

### 112:4:4 `كُفُوًا` / كفء

#### L052 — كفء B001 — counterpart/equivalent denied

- Seed image: peer, equal, counterpart, or equivalence `(E: ك ف ء B001)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ك و ن B001)`, `(E: ء ح د B002)`, `(E: لَّهُۥ complement)`, `(E: attachments 112:4 a2/a3/a4)`.
- Image and frozen model: the final clause opens the peer role, attaches it to the established referent, denies its occurrence, and leaves no candidate. Frozen model: no peer slot has an occupant.
- Predictions at freeze: earlier unity, ṣamad, and birth denials should retrospectively organize as narrower exclusions.
- Unused tested after freeze: first ءحد B001, صمد B001/B002, ولد B003/B005.
- Corroborators: `(C: ء ح د B001 positive unity)`, `(C: ص م د B001 no parallel reliance-center)`, `(C: ص م د B002 no counterpart to compact integrity)`, `(C: و ل د B003/B005 no kinship/derivation route)`.
- Constraints / rejected branches: `(K: كفء is negated; no peer is asserted)`.
- Rival forks: B002–B005 rejected by local no-peer syntax.
- Grade: strong. Rationale: strongest final role and closure seed.

#### L053 — كفء B002 — tilting, overturning, diverting

- Seed image: turning something over, inclining, diverting, or changing face `(E: ك ف ء B002)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: the branch expects movement, change of direction, inversion, or color/face change. The local `كُفُوًا` is a noun predicate in a no-peer clause.
- Predictions at freeze: motion/diversion cues would be needed.
- Unused tested after freeze: word order and final closure.
- Corroborators: none.
- Constraints / rejected branches: `(K: attachment 112:4 a3 identifies كفوا as predicate, not motion event)`, `(K: no وجه/صرف/قلب scene)`.
- Rival forks: none.
- Grade: unlikely. Rationale: incompatible local role.

#### L054 — كفء B003 — discrepancy of rhymes

- Seed image: mismatch in poetic rhyme letters/movements `(E: ك ف ء B003)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: weak acoustic recurrence tested but not selected as lexical construction.
- Image and frozen model: the passage has audible recurrence, but no poetry/qāfiya frame or rhyme-discrepancy topic. Frozen model: terminated poetic-technical image.
- Predictions at freeze: a poetry/rhyme context would be needed.
- Unused tested after freeze: acoustic dental recurrence.
- Corroborators: none.
- Constraints / rejected branches: `(K: temporal sound recurrence does not license الإكفاء في الشعر)`, `(K: no قافية/case-rhyme discussion)`.
- Rival forks: acoustic seed C017 is non-lexical and medium, but this lexical branch is not.
- Grade: unlikely. Rationale: technical branch absent.

#### L055 — كفء B004 — tent rear covering

- Seed image: sewn panel/covering at the rear of a tent or house `(E: ك ف ء B004)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: no tent, house, cloth, covering, or rear-side construction appears.
- Predictions at freeze: خِباء/بيت/covering cues would be required.
- Unused tested after freeze: صمد B004 cloth-binding branch.
- Corroborators: none.
- Constraints / rejected branches: `(K: no خِباء/بيت)`, `(K: صمد B004 also lacks cloth/body roles)`.
- Rival forks: none.
- Grade: unlikely. Rationale: no local material scene.

#### L056 — كفء B005 — year’s yield or alternating offspring

- Seed image: yearly produce/yield or alternating livestock/palm output `(E: ك ف ء B005)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: ولد B003/B005 was tested but not selected as enough.
- Image and frozen model: the branch might seek birth/produce connection, but no year, palm, camel, milk, wool, or alternating production appears.
- Predictions at freeze: year/yield cues would be needed.
- Unused tested after freeze: ولد pair.
- Corroborators: none.
- Constraints / rejected branches: `(K: ولد negations concern birth/derivation, not yearly yield)`, `(K: final كفوا syntax demands peer/equivalent B001)`.
- Rival forks: B001.
- Grade: unlikely. Rationale: branch-specific frame absent.

### 112:4:5 `أَحَدٌۢ` / ءحد

#### L057 — ءحد B001 — final unity word reactivating first unity

- Seed image: the unity word returns at closure `(E: ء ح د B001)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ك ف ء B001)`, `(E: ك و ن B001)`, `(E: ء ح د B002 local negative-scope dimension)`.
- Image and frozen model: final `أَحَدٌۢ` is the same unity-word, now placed in a no-peer clause. Frozen model: positive unity reactivated as no-one-as-peer.
- Predictions at freeze: first `أَحَدٌ` should become newly relevant.
- Unused tested after freeze: first `أَحَدٌ`, ṣamad, birth pair.
- Corroborators: `(C: sequence 112:1:4 positive أحد → 112:4:5 negated أحد)`, `(C: final ayah closure)`.
- Constraints / rejected branches: `(K: final أحد is under negation; B002 is the exact local branch)`.
- Rival forks: B002 primary, B001 reactivation.
- Grade: medium-strong. Rationale: strong temporal echo, but local syntax favors B002.

#### L058 — ءحد B002 — exhaustive no-one closure

- Seed image: `أحد` under negation exhausts all possible candidates `(E: ء ح د B002)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ك ف ء B001)`, `(E: ك و ن B001)`, `(E: attachments 112:4 a2/a3/a4)`.
- Image and frozen model: the final delayed subject closes the peer search: no counterpart exists for him, not one candidate. Frozen model: exhaustive no-peer closure.
- Predictions at freeze: the first `أَحَدٌ` should be retrospectively reactivated as the positive side of the same structure.
- Unused tested after freeze: first ءحد B001, صمد B001/B002, ولد B003/B005.
- Corroborators: `(C: ء ح د B001 first occurrence)`, `(C: ص م د B001/B002 centrality/compactness)`, `(C: و ل د B003/B005 denied routes to counterparts)`.
- Constraints / rejected branches: `(K: final أحد is delayed subject, not mere emphatic repetition)`.
- Rival forks: B001 reactivation fork.
- Grade: strong. Rationale: exact negative-scope fit and passage closure.

#### L059 — ءحد B003 — final counting one

- Seed image: one as number/compound numeral `(E: ء ح د B003)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: final `أحد` is delayed subject in a no-peer clause, not a counted numeral.
- Predictions at freeze: count sequence or compound numeral would be required.
- Unused tested after freeze: preceding كفوا and negated كان.
- Corroborators: none.
- Constraints / rejected branches: `(K: attachment 112:4 a4 delayed subject, not number phrase)`.
- Rival forks: none.
- Grade: unlikely. Rationale: syntax blocks the branch.

#### L060 — ءحد B004 — first/additive/day-name at closure

- Seed image: firstness, iḍāfa, or Sunday name `(E: ء ح د B004)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: no iḍāfa, first-in-series role, or calendrical reference appears.
- Predictions at freeze: addition/day-name cues would be needed.
- Unused tested after freeze: passage closure and first `أحد`.
- Corroborators: none.
- Constraints / rejected branches: `(K: final أحد is indefinite nominative subject, not مضاف)`, `(K: no day-name frame)`.
- Rival forks: none.
- Grade: unlikely. Rationale: structural triggers absent.

#### L061 — ءحد B005 — individual candidates scanned one by one

- Seed image: individualization, one-by-one candidates `(E: ء ح د B005)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ك ف ء B001)`, `(E: negative scope)`.
- Image and frozen model: final negative context can scan possible individuals: no individual comes as a peer. Frozen model: candidate-by-candidate no-peer search.
- Predictions at freeze: it should converge with negative-exhaustive B002.
- Unused tested after freeze: first أحد and earlier unity.
- Corroborators: `(C: ء ح د B002 gives exact negative exhaustion)`, `(C: ء ح د B001 first unity reactivated)`.
- Constraints / rejected branches: `(K: no آحادا dispersal; B005 is subordinate to B002)`.
- Rival forks: B002 stronger.
- Grade: medium. Rationale: candidate scanning fits the final no-peer clause, though B002 is exact.

#### L062 — ءحد B006 — Mount Uḥud at closure

- Seed image: Mount Uḥud as place-name `(E: ء ح د B006)`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: none.
- Image and frozen model: no geographical/place-name frame appears.
- Predictions at freeze: mountain/location cues would be required.
- Unused tested after freeze: صمد B002 rock/solid branch tested but not selected.
- Corroborators: none.
- Constraints / rejected branches: `(K: final أحد is delayed subject in no-peer clause)`, `(K: صمد B002 cannot supply geography)`.
- Rival forks: none.
- Grade: unlikely. Rationale: homonymous branch unsupported.

## Constructional, morphosyntactic, and temporal seeds

Each construction seed also uses FULL-S112-SWEEP as the lexical control sweep, but starts from an actual textual construction, attachment, morphology, or temporal/acoustic event rather than from a lexical branch.

#### C001 — attachment 112:1 a1 — quoted complement under `قُلْ`

- Seed image: a command opens a quote space; `هُوَ ٱللَّهُ أَحَدٌ` fills it.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ق و ل B001)`, `(E: ء ل ه B002)`, `(E: ء ح د B001)`.
- Frozen model: commanded utterance with fixed quoted content.
- Predictions at freeze: later material should preserve the quoted referent.
- Unused tested after freeze: repeated name, 3MS morphology, final no-peer clause.
- Corroborators: `(C: repetition 112:2:1)`, `(C: 3MS continuity)`.
- Constraints: `(K: quote attachment creates no new lexical meaning by itself)`.
- Grade: medium-strong. Rationale: structurally forced and temporally foundational.

#### C002 — attachment 112:1 a2 — `أَحَدٌ` as predicate of `ٱللَّهُ`

- Seed image: the named referent receives a unity predicate.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ء ل ه B002)`, `(E: ء ح د B001)`.
- Frozen model: proper name + positive unity.
- Predictions at freeze: later material should protect unity from derivation/equivalence.
- Unused tested after freeze: ṣamad predicate, birth negations, final no-peer.
- Corroborators: `(C: ص م د B001/B002)`, `(C: و ل د B003/B005)`, `(C: ك ف ء B001 + ء ح د B002)`.
- Constraints: `(K: predicate structure rejects counting and Mount Uḥud branches)`.
- Grade: strong. Rationale: core activation that the whole closure reactivates.

#### C003 — attachment 112:1 a3 — `ٱللَّهُ` apposed to `هُوَ`

- Seed image: pronoun points, name identifies.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ء ل ه B002)`, `(E: pronoun 3MS)`, `(E: ء ح د B001)`.
- Frozen model: deictic/pronominal referent is fixed by the name.
- Predictions at freeze: later 3MS forms should continue the same referent.
- Unused tested after freeze: 112:2 repeated name; 112:3–4 verbs/pronoun.
- Corroborators: `(C: repeated ٱللَّهُ)`, `(C: يلد/يولد/يكن 3MS)`, `(C: لَّهُۥ)`.
- Constraints: `(K: apposition is medium-confidence row, so it supports but does not alone carry synthesis)`.
- Grade: medium-strong. Rationale: useful referent-tracking seed.

#### C004 — attachment 112:2 a1 — `ٱلصَّمَدُ` as predicate of repeated `ٱللَّهُ`

- Seed image: same named referent receives a second predicate.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ء ل ه B002 repetition)`, `(E: ص م د B001)`, rival `(E: ص م د B002)`.
- Frozen model: reactivated name + ṣamad role.
- Predictions at freeze: later denials should protect ṣamad centrality/compactness.
- Unused tested after freeze: birth pair and no-peer clause.
- Corroborators: `(C: و ل د B003/B005)`, `(C: ك ف ء B001)`, `(C: ء ح د B002)`.
- Constraints: `(K: ṣamad branches remain branch-images, not replacement translations)`.
- Grade: strong. Rationale: second positive predicate is a major hinge.

#### C005 — attachment 112:3 a1 — `لَمْ` governs active `يَلِدْ`

- Seed image: an outgoing birth event is grammatically opened and cancelled.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: و ل د B003 active)`, `(E: negated jussive morphology)`.
- Frozen model: no outgoing birth/generation.
- Predictions at freeze: inverse birth and broader peer should be denied.
- Unused tested after freeze: passive `يُولَدْ`, final no-peer.
- Corroborators: `(C: coordination with passive)`, `(C: ك ف ء B001 + ء ح د B002)`.
- Constraints: `(K: no positive birth event)`.
- Grade: strong. Rationale: exact morphology and role.

#### C006 — attachment 112:3 a2 — coordination of active and passive ولد

- Seed image: two vectors of the same root are paired and negated.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: و ل د B003 active)`, `(E: و ل د B003 passive)`, `(E: coordination)`.
- Frozen model: no genealogical vector outward or inward.
- Predictions at freeze: final clause should generalize to equivalence.
- Unused tested after freeze: كون B001, كفء B001, final ءحد B002.
- Corroborators: `(C: final no-peer construction)`.
- Constraints: `(K: the pair is syntactic and morphological, not a kinship narrative)`.
- Grade: strong. Rationale: compact bidirectional shutdown.

#### C007 — attachment 112:3 a3 — `لَمْ` governs passive `يُولَدْ`

- Seed image: incoming birth/origin is cancelled.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: و ل د B003 passive)`, `(E: passive voice)`, `(E: negated jussive)`.
- Frozen model: no born-from relation.
- Predictions at freeze: no parent-origin or counterpart should remain.
- Unused tested after freeze: final no-peer.
- Corroborators: `(C: ك ف ء B001)`, `(C: ء ح د B002)`.
- Constraints: `(K: no positive origin scene)`.
- Grade: strong. Rationale: exact local morphology.

#### C008 — attachment 112:4 a1 — `لَمْ` governs `يَكُن`

- Seed image: occurrence/existence is denied at the final clause.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ك و ن B001)`, `(E: negated jussive)`.
- Frozen model: no occurrence of the relation introduced in the predicate.
- Predictions at freeze: predicate and subject should identify what is denied.
- Unused tested after freeze: `له`, `كفوا`, final `أحد`.
- Corroborators: `(C: ك ف ء B001 predicate)`, `(C: ء ح د B002 delayed subject)`.
- Constraints: `(K: not a bad-state or place seed)`.
- Grade: strong. Rationale: final closure depends on this structure.

#### C009 — attachment 112:4 a2 — `لَّهُۥ` as complement of `كُفُوًا`

- Seed image: the peer relation is oriented “for/to him,” keeping the prior referent active.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ك ف ء B001)`, `(E: 3MS pronoun continuity)`.
- Frozen model: the denied peer is specifically attached to the established referent.
- Predictions at freeze: no referent switch.
- Unused tested after freeze: final `أحد`, earlier name repetition.
- Corroborators: `(C: ء ل ه B002 repeated name)`, `(C: 3MS morphology across verbs)`, `(C: ء ح د B002 no candidate)`.
- Constraints: `(K: له is not a separate lexical seed; structural evidence only)`.
- Grade: strong. Rationale: prevents a floating no-peer clause.

#### C010 — attachment 112:4 a3 — `كُفُوًا` as predicate of negated `يَكُن`

- Seed image: the denied predicate is peer/equivalence.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ك ف ء B001)`, `(E: ك و ن B001)`.
- Frozen model: no peer-predicate occurs.
- Predictions at freeze: final subject should exhaust possible fillers.
- Unused tested after freeze: final ءحد B002.
- Corroborators: `(C: ء ح د B002 delayed subject)`.
- Constraints: `(K: كفء B002–B005 rejected by predicate role and context)`.
- Grade: strong. Rationale: locks the final semantic role.

#### C011 — attachment 112:4 a4 — final `أَحَدٌۢ` as delayed subject

- Seed image: the final word supplies the subject after the peer role has already been denied.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ء ح د B002)`, `(E: ك ف ء B001)`, `(E: ك و ن B001)`.
- Frozen model: no one fills the peer role.
- Predictions at freeze: closure is licensed because the candidate set is exhausted.
- Unused tested after freeze: first ءحد B001.
- Corroborators: `(C: first أحد positive unity reactivated)`.
- Constraints: `(K: final أحد is not merely repeated emphasis; delayed subject role matters)`.
- Grade: strong. Rationale: exact closure mechanism.

#### C012 — temporal seed: repeated `ٱللَّهُ`

- Seed image: the named referent established in 112:1 returns at 112:2.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ء ل ه B002 at both occurrences)`, `(E: ص م د B001)`.
- Frozen model: referent reactivation enables a second predicate.
- Predictions at freeze: later clauses should keep the same 3MS referent.
- Unused tested after freeze: 112:3–4 morphology.
- Corroborators: `(C: 3MS verbs and لَّهُۥ)`.
- Constraints: `(K: repetition itself is structural; it does not choose between ṣamad branches alone)`.
- Grade: strong. Rationale: clear temporal conditioning.

#### C013 — temporal seed: repeated `أَحَد`

- Seed image: positive one-ness returns as negative-exhaustive no-one.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ء ح د B001 first)`, `(E: ء ح د B002 final)`, `(E: ك ف ء B001)`.
- Frozen model: first `أحد` is retrospectively reorganized by final `أحد`.
- Predictions at freeze: intervening material should motivate the shift.
- Unused tested after freeze: ṣamad, birth pair.
- Corroborators: `(C: ص م د B001/B002)`, `(C: و ل د B003/B005)`.
- Constraints: `(K: different syntax: first predicate, final delayed subject under negation)`.
- Grade: strong. Rationale: strongest reactivation path.

#### C014 — temporal seed: repeated `لَمْ`

- Seed image: a chain of cancellations begins at birth and ends at peer existence.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: و ل د B003 active/passive)`, `(E: ك و ن B001)`, `(E: ك ف ء B001)`.
- Frozen model: repeated negation strips possible relations in order.
- Predictions at freeze: the final denial should be broader than the birth denials.
- Unused tested after freeze: final ءحد B002.
- Corroborators: `(C: final no-candidate subject)`.
- Constraints: `(K: لَمْ is structural, not lexical furuq evidence)`.
- Grade: strong. Rationale: explains sequence of exclusions.

#### C015 — morphosyntactic seed: 3MS referent continuity

- Seed image: `هُوَ`, `ٱللَّهُ`, 3MS verbs, and `لَّهُۥ` maintain one referent.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ء ل ه B002)`, `(E: pronoun/morphology 3MS)`, `(E: ولد B003)`, `(E: كون B001)`, `(E: كفء B001)`.
- Frozen model: a single referent is carried through positive predicates and negative relation tests.
- Predictions at freeze: no referent split.
- Unused tested after freeze: final أحد.
- Corroborators: `(C: ء ح د B002 no alternate candidate)`.
- Constraints: `(K: morphology tracks referent; it does not independently supply unity)`.
- Grade: strong. Rationale: prevents shuffled or multi-referent readings of the image.

#### C016 — temporal seed: positive predicates before negative pruning

- Seed image: first establish, then protect by exclusion.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: ء ل ه B002)`, `(E: ء ح د B001)`, `(E: ص م د B001/B002)`, `(E: ولد B003)`, `(E: كفء B001)`.
- Frozen model: identity → unity/ṣamad → no birth → no peer.
- Predictions at freeze: final clause should close by exhausting all remaining counterpart candidates.
- Unused tested after freeze: كون B001 + final ءحد B002.
- Corroborators: `(C: ك و ن B001)`, `(C: ء ح د B002)`, `(C: ayah closure)`.
- Constraints: `(K: sequence model must stay tied to branch-specific evidence)`.
- Grade: strong. Rationale: explains the order better than static root presence.

#### C017 — temporal/acoustic seed: د closure recurrence

- Seed image: repeated final dental sounds keep earlier tokens available: `أَحَدٌ`, `ٱلصَّمَدُ`, `يَلِدْ`, `يُولَدْ`, final `أَحَدٌ`.
- Roots visited: FULL-S112-SWEEP. Selected before freeze: `(E: temporal/acoustic recurrence)`, `(E: ءحد B001/B002)`, `(E: صمد B001/B002)`, `(E: ولد B003)`.
- Frozen model: acoustic recurrence supports memory/reactivation while semantic relations tighten.
- Predictions at freeze: final `أحد` should sound and function like closure.
- Unused tested after freeze: no-peer construction.
- Corroborators: `(C: final delayed subject closes the clause)`.
- Constraints: `(K: sound recurrence alone cannot license lexical meanings)`.
- Grade: medium. Rationale: useful hearing-state support, weaker than syntax/branch evidence.

## Opening-context check: basmala

The sacred Arabic file includes `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ` before the assigned ayat. It was not used as a seed. Since QAC returned no S112 ayah-0 rows, no basmala roots or furuq branches were queried. It can only weakly support the already active opening context of divine naming: `(C: basmala opening-context, sacred Arabic sequence only)`. No synthesis above depends on basmala branch evidence.

## Multi-seed convergence

The strongest convergence is:

```text
قول B001 + quote attachment
  → commanded utterance with bounded content
ءله B002 at 112:1 and 112:2
  → same named referent reactivated
ءحد B001 at 112:1:4
  → positive unity
صمد B001 / B002 at 112:2:2
  → reliance-center / compact integrity
ولد B003 active + ولد B003 passive, with ولد B005 as broader derivation fork
  → no outward or inward generation
كون B001 + كفء B001 + ءحد B002 at 112:4
  → no occurrence of any peer candidate
```

Compact frozen synthesis:

The passage opens as commanded speech, fixes a named referent, predicates unity, reactivates the referent to predicate `ٱلصَّمَدُ`, then tests and cancels relations that would create multiplicity: birth outward, birth inward, and finally any peer/equivalent candidate at all. The final `أَحَدٌۢ` reactivates the first `أَحَدٌ`: what began as positive one-ness closes as exhaustive no-one-as-peer.

## Exhaustiveness self-audit before completion

- Lexical seed count required: 62.
- Lexical seed count written: L001–L062 = 62.
- Rooted occurrences covered in order:
  - 112:1:1 قول B001–B016: L001–L016
  - 112:1:3 ءله B001–B002: L017–L018
  - 112:1:4 ءحد B001–B006: L019–L024
  - 112:2:1 ءله B001–B002: L025–L026
  - 112:2:2 صمد B001–B007: L027–L033
  - 112:3:2 ولد B001–B006: L034–L039
  - 112:3:4 ولد B001–B006: L040–L045
  - 112:4:2 كون B001–B006: L046–L051
  - 112:4:4 كفء B001–B005: L052–L056
  - 112:4:5 ءحد B001–B006: L057–L062
- Construction and temporal seeds written: C001–C017.
- Attachment coverage: all 11 S112 attachment rows are represented by C001–C011.
- Additional temporal/morphosyntactic/acoustic coverage: repeated `ٱللَّهُ`, repeated `أحد`, repeated `لَمْ`, 3MS continuity, positive-to-negative sequence, and dental sound recurrence are represented by C012–C017.
- Basmala: checked as opening context only, not seeded.
- Potentially missing images generated before finalization: weak/remote branches that were compacted before are now individual seed passes, including قول B002–B016, ءحد B003–B006 at both occurrences, صمد B003–B007, ولد B004/B006 at both occurrences, كون B002–B006, and كفء B002–B005.
