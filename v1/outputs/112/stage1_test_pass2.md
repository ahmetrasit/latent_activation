# S112 — Stage 1 test Pass 2: exhaustive occurrence-by-occurrence reactivation

## 1. Root cause of the Pass 1 limitation

The source inventory was complete, but the traversal record was not deep enough. Four procedural choices caused the visible limitation:

1. A root-level shorthand (`V(root)`) stood in for occurrence-level visits. That collapsed the two occurrences of ٱللَّهُ, the active and passive occurrences of و ل د, and the two differently governed occurrences of أَحَدٌ even though each meets a different temporary recitation state.
2. “Dossier read” was treated as sufficient audit evidence. Only selected branches were narrated, so most visited words had no explicit selection/rejection decision inside each finding.
3. Weak seeds were allowed to terminate before every later occurrence and construction was tested. This prevented remote but complete rival images—strike/rock, cloth/enclosure, oversight/guarantee, place/rank, lifecycle, coda variation, and alternating production—from being frozen and then constrained.
4. The completion check counted seed headings, not the Cartesian coverage required here: `seed × other rooted occurrence × eligible construction`. It therefore verified 62 starts without verifying every within-seed visit.

Pass 2 corrects this by preserving every occurrence, requiring a ten-position word ledger and a twelve-construction ledger for every lexical seed, and retaining every meaningful fork until a freeze-and-test decision. A visit is control coverage, never evidence by itself.

## 2. Sacred sequence and seed universe

```text
opening-context only: بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ

O1  112:1:1  قُلْ       ق و ل
    112:1:2  هُوَ       unrooted 3MS pronoun
O2  112:1:3  ٱللَّهُ    ء ل ه
O3  112:1:4  أَحَدٌ     ء ح د
O4  112:2:1  ٱللَّهُ    ء ل ه
O5  112:2:2  ٱلصَّمَدُ  ص م د
    112:3:1  لَمْ       unrooted negator
O6  112:3:2  يَلِدْ     و ل د, active imperfect jussive
    112:3:3  وَلَمْ     conjunction + negator
O7  112:3:4  يُولَدْ    و ل د, passive imperfect jussive
    112:4:1  وَلَمْ     conjunction + negator
O8  112:4:2  يَكُن      ك و ن, imperfect jussive
    112:4:3  لَّهُۥ     preposition + 3MS pronoun
O9  112:4:4  كُفُوًا    ك ف ء, indefinite accusative noun
O10 112:4:5  أَحَدٌۢ    ء ح د, indefinite nominative noun
```

The seven roots contain 48 uncontaminated branches. Position-sensitive seeding gives 62 lexical seeds:

```text
O1:16 + O2:2 + O3:6 + O4:2 + O5:7
+ O6:6 + O7:6 + O8:6 + O9:5 + O10:6 = 62
```

Basmala never initiates a seed. Its occurrence of ٱللَّهِ may only be marked `opening-context` after a passage-generated naming model has frozen.

## 3. Eligible construction universe

Every lexical seed explicitly tests all twelve constructions. Each construction also receives its own seed pass in §6.

```text
X1  قُلْ + quoted complement هُوَ ٱللَّهُ أَحَدٌ        attachment 112:1 a1
X2  هُوَ / ٱللَّهُ / أَحَدٌ apposition-predication      attachments 112:1 a2–a3
X3  ٱللَّهُ ٱلصَّمَدُ second predication                attachment 112:2 a1
X4  exact ٱللَّهُ recurrence across 112:1→112:2
X5  three successive لَمْ clauses                       attachments 112:3 a1,a3; 112:4 a1
X6  يَلِدْ / يُولَدْ coordination + active/passive      attachment 112:3 a2
X7  لَّهُۥ governed as complement of كُفُوًا            attachment 112:4 a2
X8  يَكُن / كُفُوًا / delayed أَحَدٌ roles              attachments 112:4 a3–a4
X9  هُوَ→name→implicit 3MS verbs→لَّهُۥ referent chain
X10 exact أَحَدٌ recurrence with predicate→subject change
X11 ayah boundaries and positive→negative ordered phases
X12 ayah-final sound recurrence: أَحَد / صَمَد / يُولَد / أَحَد
```

Ledger notation: `E` means selected before freeze; `C` means unused at freeze and corroborating afterward; `K` means constraining/defeating; `R` means a distinct rival fork was generated; `0` means the full named dossier/construction was tested but did not transform, complete, fork, corroborate, or constrain the image. Ranges such as `B001–B006` mean the continuous dossier in §4 was read in full; they are not generalized root meanings.

## 4. Continuous uncontaminated root dossiers

### ق و ل

- B001 **إخراج القول بالنطق** — يدخل فيه قال يقول قولا، والقول والقيل، والكلام المركب من الحروف إذا أبرز بالنطق، مفردا كان أو جملة أو قصيدة أو خطبة.
- B002 **اللسان آلة القول** — يدخل فيه المقول بمعنى اللسان.
- B003 **كثرة القول في صاحبه** — يدخل فيه قولة وقوال وقوالة وتقوالة وقؤول ومقوال ومقول إذا وصفت الإنسان بأنه لسن أو كثير القول أو منطيق.
- B004 **القيل صاحب القول النافذ** — يدخل فيه المقول أو القيل بلغة أهل اليمن، والواحد القيل، والجمع المقاولة والأقيال والأقوال، وملك حمير دون الملك الأعظم، والمرأة قيلة.
- B005 **قول ما لم يكن أو نسبته** — يدخل فيه تقول باطلا، وتقول عليه أي كذب عليه، وقولتني أو أقولتني ما لم أقل.
- B006 **اجترار القول إلى النفس** — يدخل فيه اقتال قولا إذا اجتر إلى نفسه قولا من خير أو شر.
- B007 **القول الفاشي بين الناس** — يدخل فيه القالة الحسنة أو القبيحة المنتشرة في الناس، وكثرة قالة الناس، والقيل والقال بوصفهما حديثا دائرا.
- B008 **عود القال لضرب القلة** — يدخل فيه القال، الخشبة التي تضرب بها القلة.
- B009 **المقاولة في الأمر** — يدخل فيه قاولته في أمره وتقاولنا إذا تفاوضنا.
- B010 **اقتالة الحكم على غيره** — يدخل فيه اقتال عليه إذا كان بمعنى تحكم.
- B011 **قول يجري مجرى الظن** — يدخل فيه تقول إذا أجري مجرى تظن في العمل، وخاصة في الاستفهام، وما ذكر عن بني سليم من إجراء متصرف قلت مجرى الظن في غير الاستفهام.
- B012 **قول في النفس لم يظهر** — يدخل فيه المتصور في النفس قبل الإبراز باللفظ، كما في قول في نفسي لم أظهره.
- B013 **القول اعتقاد ومذهب** — يدخل فيه القول بمعنى الاعتقاد، نحو فلان يقول بقول أبي حنيفة.
- B014 **قول الشيء دلالته** — يدخل فيه القول للدلالة على الشيء، مثل امتلأ الحوض وقال قطني.
- B015 **العناية الصادقة بالشيء** — يدخل فيه فلان يقول بكذا إذا كان معناه العناية الصادقة بالشيء.
- B016 **قول الشيء حده** — يدخل فيه استعمال المنطقيين القول بمعنى الحد، كقول الجوهر وقول العرض أي حدهما.

### ء ل ه

- B001 **التعبد والمعبود** — يدخل فيه أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.
- B002 **اسم الله في القسم والنداء** — يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.

### ء ح د

- B001 **الأَحَدِيَّة والوَحْدَة** — أحد بمعنى الواحد، والوصف المطلق بأحد، وتكرار أحد أحد للتأكيد.
- B002 **استغراق النفي** — أحد في سياق النفي لاستغراق جنس من يصلح أن يخاطب، فيشمل الواحد وما فوقه.
- B003 **الواحد في العد والتركيب** — أحد في العد، وتركيبه مع العشرات، وتصْيير المعدود أحد عشر.
- B004 **الأول والإضافة** — أحد مضافا أو مضافا إليه بمعنى الأول، واسم يوم الأحد.
- B005 **الانفراد والتفرق آحادا** — الانفراد بالفعل، والمجيء آحادا أفرادا.
- B006 **جبل أُحُد** — اسم جبل بالمدينة.

### ص م د

- B001 **القصد إلى المعتمد المقصود** — قصد الشيء واعتماده؛ السيد الذي يقصد إليه في الأمور والحوائج؛ الصمد من جهة الصمود إليه.
- B002 **الصلابة المكتنزة بلا جوف** — الصلابة والاكتناز وانعدام الجوف؛ المكان الصلب أو المرتفع الغليظ؛ الصخرة الراسية والأرض الشديدة.
- B003 **سدادة القارورة المحكمة** — الصماد بمعنى عفاص القارورة أو سدادها؛ فعل صمد القارورة أي جعل لها صمادا.
- B004 **شد الرأس بصماد** — تصميد الرأس بخرقة أو منديل أو ثوب دون العمامة.
- B005 **الإشراف على الأمر مع الحفل به** — قولهم على صمادة من أمر لمن أشرف عليه وحفل به.
- B006 **إيقاع الضرب بالعصا** — صمده بالعصا بمعنى ضربه بها.
- B007 **الدوام والبقاء على الشدة** — الدوام والبقاء؛ الناقة المصماد الباقية على القر والجدب الدائمة الرسل.

### و ل د

- B001 **مولود من نسل** — يدخل فيه الولد والمولود والابن والابنة والأولاد، ويستعمل للواحد والجمع وللصغير والكبير وللذكر والأنثى بحسب نصوص المصادر.
- B002 **أبوان من جهة الولادة** — يدخل فيه الوالد بمعنى الأب، والوالدة بمعنى الأم، والوالدان للأب والأم.
- B003 **حدوث الولادة ووضع الحمل** — يدخل فيه ولدت المرأة، والولادة بوضع الوالدة ولدها، وما قرب من وقت الولادة أو حان ولاده في أولدت، وولادة الحيوان إذا نصت المصادر عليها.
- B004 **صغير قريب العهد بالولادة أو مملوك** — يدخل فيه الوليد للصبي أو الغلام القريب العهد بالولادة، والوليدة للصبية أو الأمة، وما جمعه ولدان أو ولائد بحسب النص.
- B005 **شيء حاصل عن شيء أو مستحدث منه** — يدخل فيه تولد الشيء من الشيء إذا حصل عنه بسبب، والمولد من الكلام إذا استحدث، وما كان غير محض أو ناشئا في بيئة معينة مثل عربية مولدة ورجل مولد.
- B006 **قرين في سن الولادة** — يدخل فيه اللدة أو لدة الرجل بمعنى تربه ومثيله في السن.

### ك و ن

- B001 **وقوع الشيء وحضوره في زمان** — يدخل فيه وقوع الشيء وحضوره وحدوثه في زمان ماض أو راهن، ومصدر كان والكينونة والكائنة، واستعمال كان خبرا أو توكيدا أو في الاستثناء.
- B002 **المكان والمكانة من الكون** — يدخل فيه المكان والموضع والمكانة والمنزلة والتمكن إذا جعلت من كان يكون.
- B003 **الكفالة والقيام على فلان** — يدخل فيه الكيانة والكفالة والتكفل بفلان واكتنت به.
- B004 **الخضوع بالاستكانة** — يدخل فيه الاستكانة بمعنى الخضوع.
- B005 **الشيخ المنسوب إلى كُنْتُ** — يدخل فيه الكُنْتِيّ للرجل إذا شاخ كأنه نسب إلى قوله كُنْتُ في شبابي.
- B006 **حالة السوء بكينة** — يدخل فيه قولهم بات فلان بكينة سوء أي بحال سوء إذا جعلت الكينة فعلة من الكون.

### ك ف ء

- B001 **المماثلة والمقابلة بالمثل** — يدخل فيه الكفء والمثل والنظير؛ التساوي والتكافؤ؛ الكفاءة في المناكحة والحرب والمضادة؛ المكافأة والمجازاة بالمثل؛ المقابلة والموالاة بين شيئين.
- B002 **الإمالة والقلب والصرف** — يدخل فيه إمالة الشيء وقلبه وكبه؛ إمالة القوس والصحفة؛ صرف القوم عن وجهتهم؛ التمايل في المشي أو كالسفينة؛ انكسار الوجه وتغير اللون.
- B003 **اختلاف القوافي** — يدخل فيه الإكفاء في الشعر باختلاف القوافي في الحروف أو الحركات أو الإعراب.
- B004 **كِفاء الخباء** — يدخل فيه الكِفاء بمعنى شقة أو شقتين تخاطان ويجعل بهما مؤخر الخباء أو البيت.
- B005 **كفأة السنة والنتاج** — يدخل فيه الكفأة لحمل النخلة أو نتاج الإبل سنة؛ سؤال نتاج الإبل أو ثمر النخل سنة؛ إعطاء اللبن والوبر والأولاد سنة؛ جعل الإبل كفأتين يتناوب نتاجهما.

## 5. Exhaustive lexical singleton passes

Every `Word ledger` below names O1–O10 exactly once. Every `Construction ledger` names X1–X12 exactly once. This makes an explicit no-effect decision part of the audit while keeping evidence limited to selected `E`, independently tested `C`, and resisting `K` material.

### 5.1 O1 — 112:1:1 قُلْ — ق و ل

#### L001 — O1 × ق و ل B001 — Spoken content reaches relational completion

- **Initial image.** `(E: ق و ل B001)` plus `(E: imperative 2MS)` creates an outward speech event with an unfilled content role; X1 immediately gives that role a quoted clause.
- **Word ledger.** `O1=focus B001`; `O2=E ء ل ه B002 name; B001 worship fork held`; `O3=E ء ح د B001 unity; B002 K in positive syntax; B003–B006 0`; `O4=C B002 repeated name; B001 0`; `O5=C ص م د B001 one-center relation; B002–B007 tested 0 for this model`; `O6=C و ل د B003 active birth denial; B001/B002/B004–B006 tested`; `O7=C B003 passive inverse; B001/B002/B004–B006 tested`; `O8=C ك و ن B001 copular occurrence; B002–B006 0`; `O9=C ك ف ء B001 equality; B002–B005 0`; `O10=C ء ح د B002 negative exhaustor + B001 recurrence; B003–B006 0`.
- **Construction ledger.** `X1=E content`; `X2=E name+predicate`; `X3=C second predicate`; `X4=C re-anchor`; `X5=C widening negation`; `X6=C inverse roles`; `X7=C comparison target`; `X8=C delayed completion`; `X9=C referent continuity`; `X10=C exact reactivation`; `X11=C phased closure`; `X12=C weak acoustic maintenance`.
- **Forks and freeze.** Main generating set `{ق و ل B001, X1, ء ل ه B002, ء ح د B001, X2}` freezes after O3 as “a commissioned utterance identifies G and predicates unity.” Predictions: maintain G, add a defining relation, remove incompatible outgoing/incoming/parallel roles, and stop when the competitor class is exhausted. A worship-center fork from ء ل ه B001 was generated but left separate because no worship act appears.
- **UNUSED_AT_FREEZE and test.** O4–O10 and X3–X12 were unused. They supply the predicted second predicate, inverse birth denials, general equality denial, delayed exhaustive subject, exact أَحَدٌ reactivation, and terminal boundary. `(K: B001 creates speech, not the truth or lexical content of the quote)`.
- **Grade: strong.** Local morphology starts the process, and nine later occurrence decisions plus independent constructions reproduce expectation, completion, reactivation, and stopping.

#### L002 — O1 × ق و ل B002 — Unmentioned tongue instrument

- **Initial image.** `(E: ق و ل B002, form-remote)` posits a tongue as instrument and predicts an oral/body part or explicit instrument role.
- **Word ledger.** `O1=focus B002`; `O2=ء ل ه B001–B002 0`; `O3=ء ح د B001–B006 0`; `O4=ء ل ه B001–B002 0`; `O5=R ص م د B004 head/cloth body-scene, B001–B003/B005–B007 0`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=ك و ن B001–B006 0`; `O9=R ك ف ء B004 cloth-panel extension, B001–B003/B005 0`; `O10=ء ح د B001–B006 0`.
- **Construction ledger.** `X1=K speech event names no tongue`; `X2=0`; `X3=0`; `X4=0`; `X5=0`; `X6=0`; `X7=0`; `X8=0`; `X9=0`; `X10=0`; `X11=0`; `X12=0`.
- **Forks and freeze.** Main set `{ق و ل B002}` freezes as “tongue used to voice content.” A remote body/textile fork `{ق و ل B002, ص م د B004, ك ف ء B004}` creates tongue + wrapped head + cloth, but no action relates the parts. Predictions: mouth, head, wrapping, or instrument attachment.
- **UNUSED_AT_FREEZE and test.** All nonfocus occurrences and constructions were tested; none fills an oral role. X1 instead selects the speech verb sense `(K: قُلْ is an imperative verb, not المقول ‘tongue’)`. The textile fork is defeated by nominal predications and absence of body/cloth syntax.
- **Grade: unlikely.** Exhaustive traversal produces one remote body fork but no passage-local role completion.

#### L003 — O1 × ق و ل B003 — Abundant-speaker trait versus repeated content

- **Initial image.** `(E: ق و ل B003, form-remote)` characterizes a frequent or eloquent speaker and predicts habitual/abundant speech attributable to the addressee.
- **Word ledger.** `O1=focus B003`; `O2=ء ل ه B001–B002 0`; `O3=R ء ح د B001 repetition dimension only, B002–B006 0`; `O4=R ء ل ه B002 name repetition, B001 0`; `O5=ص م د B001–B007 0`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=ك و ن B001–B006 0`; `O9=ك ف ء B001–B005 0`; `O10=R ء ح د B001 exact repeated word, B002 contextual but not speaker-trait; B003–B006 0`.
- **Construction ledger.** `X1=K one commanded speech event`; `X2=0`; `X3=0`; `X4=R repeated content`; `X5=R internal repetition`; `X6=0`; `X7=0`; `X8=0`; `X9=0`; `X10=R lexical recurrence`; `X11=0`; `X12=R recurrent cadence`.
- **Forks and freeze.** `{ق و ل B003, X4, X5, X10, X12}` yields a weak “abundant patterned declaration” fork: several repetitions occur inside the utterance. It predicts morphology marking the speaker as talkative or repeated speaking occasions.
- **UNUSED_AT_FREEZE and test.** The repetitions are properties of content, not a trait of the 2MS addressee `(K: one imperative occurrence; no قَوَّال-type noun/pattern)`. Every rooted occurrence was tested and none adds a habitual speaker role.
- **Grade: unlikely.** The generated repetition image is real at discourse level but cannot attach B003 to the local form.

#### L004 — O1 × ق و ل B004 — Authoritative overseer/guarantor fork

- **Initial image.** `(E: ق و ل B004, form-remote)` creates a صاحب القول النافذ and predicts authority, command efficacy, or a ranked speaker.
- **Word ledger.** `O1=focus B004`; `O2=R ء ل ه B001 worshipped authority; B002 name`; `O3=R ء ح د B001 sole authority; B002–B006 0`; `O4=R ء ل ه B001/B002 repeated center`; `O5=R ص م د B005 oversight-with-care + B001 relied-upon center; B002–B004/B006–B007 0`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=R ك و ن B003 guarantee/standing-for; B001/B002/B004–B006 0`; `O9=R ك ف ء B001 no equal rank; B002–B005 0`; `O10=R ء ح د B002 no candidate + B001 one; B003–B006 0`.
- **Construction ledger.** `X1=E directive force but K source unnamed`; `X2=R named authority inside quote`; `X3=R predicate of reliance`; `X4=R re-anchor`; `X5=0`; `X6=0`; `X7=R no peer-to-him`; `X8=R unmatched rank`; `X9=K quoted referent not automatically commander`; `X10=R sole/no-other arc`; `X11=0`; `X12=0`.
- **Forks and freeze.** Fork A `{ق و ل B004, imperative}`: forceful declaration. Fork B `{ق و ل B004, ء ل ه B001, ء ح د B001, ص م د B005, ك و ن B003}`: a sole authoritative overseer who cares for and guarantees an affair. Predictions: identify commander, governed party, affair, or guarantee.
- **UNUSED_AT_FREEZE and test.** Final no-equal syntax can support unmatched rank `(C: ك ف ء B001 + ء ح د B002)` but no text role identifies a ruler, subject, affair, or guarantee. `(K: قُلْ is not nominal القيل; K: quoted ٱللَّهُ is inside content, while the command source is not named by X1)`.
- **Grade: weak.** A fuller authority image now exists, but its distinctive participants depend entirely on remote branches.

#### L005 — O1 × ق و ل B005 — Corrective denial of a false attribution

- **Initial image.** `(E: ق و ل B005, form-remote)` predicts fabricated speech or an assertion falsely attributed to someone.
- **Word ledger.** `O1=focus B005`; `O2=E ء ل ه B002 attribution target/name; B001 0`; `O3=R ء ح د B001 asserted property; B002–B006 0`; `O4=C B002 repeated target`; `O5=R ص م د B001/B002 asserted predicates; B003–B007 0`; `O6=R و ل د B001–B003 denied filial attribution; B004–B006 0`; `O7=R B001–B003 denied origin attribution; B004–B006 0`; `O8=ك و ن B001 C denied occurrence; B002–B006 0`; `O9=C ك ف ء B001 denied equivalence attribution; B002–B005 0`; `O10=C ء ح د B002/B001 closes denial; B003–B006 0`.
- **Construction ledger.** `X1=E commanded corrective saying`; `X2=E target+claim`; `X3=R further claim`; `X4=C target continuity`; `X5=C categorical denials`; `X6=C two attribution directions`; `X7=C relation to target`; `X8=C final denial`; `X9=C same target`; `X10=C closure`; `X11=C assertion→denial`; `X12=0`.
- **Forks and freeze.** `{ق و ل B005, X1, ء ل ه B002}` freezes as “a commanded utterance corrects false claims about G.” It predicts a prior claimant, attribution marker, or explicit correction contrast. The later birth/equality denials can fill *what* might be denied but do not establish that anyone previously said it.
- **UNUSED_AT_FREEZE and test.** O3–O10 give coherent corrective content, especially lineage and equivalence denials. Decisive constraint: no liar, prior saying, quotation of an opponent, or تَقَوُّل morphology occurs `(K: local قُلْ B001 speech event)`. The same clauses work without a correction story.
- **Grade: weak.** Exhaustive role completion yields a plausible correction protocol, but the seed's falsity/ascription frame is unattested.

#### L006 — O1 × ق و ل B006 — Inward appropriation converted to outward speech

- **Initial image.** `(E: ق و ل B006, form-remote)` draws a saying inward to oneself. It predicts an inner possessor and a later outward transition.
- **Word ledger.** `O1=focus B006`; `O2=R ء ل ه B001 inward devotion / B002 named content`; `O3=R ء ح د B001 compact inner proposition; B002–B006 0`; `O4=ء ل ه B001–B002 0 after initial selection`; `O5=ص م د B001–B007 0`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=ك و ن B001–B006 0`; `O9=ك ف ء B001–B005 0`; `O10=ء ح د B001/B002 closure only; B003–B006 0`.
- **Construction ledger.** `X1=R outward conversion and K no prior inner stage`; `X2=R proposition content`; `X3=0`; `X4=0`; `X5=0`; `X6=0`; `X7=0`; `X8=0`; `X9=0`; `X10=R compact closure`; `X11=0`; `X12=0`.
- **Forks and freeze.** Fork A `{ق و ل B006, ء ل ه B002, ء ح د B001}` is an inwardly appropriated compact proposition. Fork B adds X1 as a transition from inward possession to voiced declaration. Prediction: an explicit self, concealment, heart/mind, or before/after marker.
- **UNUSED_AT_FREEZE and test.** Every later occurrence was tested; none supplies an inner locus. X1 only supplies the outward event `(K: imperative and overt quote)` and cannot retrospectively create the absent inward stage.
- **Grade: weak.** The conversion image is coherent but half of it is inferred solely from the remote branch.

#### L007 — O1 × ق و ل B007 — A compact saying entering circulation

- **Initial image.** `(E: ق و ل B007, form-remote)` imagines a saying spreading among people; it predicts transmitters, hearers, recurrence, or circulation.
- **Word ledger.** `O1=focus B007`; `O2=E ء ل ه B002 stable repeated name; B001 0`; `O3=E ء ح د B001 memorable predicate; B002–B006 0`; `O4=R B002 name recurrence`; `O5=R ص م د B001 compact relational predicate; B002–B007 tested`; `O6=و ل د B001–B006 content only`; `O7=و ل د B001–B006 content only`; `O8=ك و ن B001–B006 content only`; `O9=ك ف ء B001–B005 content only`; `O10=R ء ح د B001/B002 terminal recurrence; B003–B006 0`.
- **Construction ledger.** `X1=E launchable utterance`; `X2=E compact clause`; `X3=R parallel clause`; `X4=R repetition`; `X5=R patterned content`; `X6=0`; `X7=0`; `X8=R closure`; `X9=0`; `X10=R refrain-like return`; `X11=R four bounded units`; `X12=R acoustic memorability`.
- **Forks and freeze.** `{ق و ل B007, X1, X2, ء ل ه B002, ء ح د B001}` yields a compact saying that could circulate; X4/X10/X12 yield a patterned-circulation fork. Predictions: plural speakers/hearers, report chain, or explicit repeated transmission.
- **UNUSED_AT_FREEZE and test.** Formal recurrence and boundaries corroborate compact repeatability, not actual diffusion. `(K: قُلْ is singular 2MS; no people, hearer, or transmission relation appears)`.
- **Grade: weak.** The passage supplies a repeatable form but not B007's social circulation event.

#### L008 — O1 × ق و ل B008 — Stick, strike, rock, and overturning avalanche

- **Initial image.** `(E: ق و ل B008, form-remote)` supplies a wooden stick used to strike a game-piece and predicts wielder, impact action, and target.
- **Word ledger.** `O1=focus B008`; `O2=ء ل ه B001–B002 0`; `O3=R ء ح د B006 mountain target; B001–B005 0`; `O4=ء ل ه B001–B002 0`; `O5=R ص م د B006 stick-strike action + B002 rock/hard target; B001/B003–B005/B007 0`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=ك و ن B001–B006 0`; `O9=R ك ف ء B002 overturning/diversion as impact result; B001/B003–B005 0`; `O10=R ء ح د B006 repeated mountain candidate; B001–B005 0`.
- **Construction ledger.** `X1=K speech syntax`; `X2=K nominal identity`; `X3=K predication not impact`; `X4=0`; `X5=0`; `X6=0`; `X7=0`; `X8=0`; `X9=0`; `X10=R repeated mountain form but wrong vocalization`; `X11=0`; `X12=0`.
- **Forks and freeze.** Fork A `{ق و ل B008, ص م د B006}` is a stick delivering a blow. Fork B adds `{ص م د B002}` as rock target; fork C adds `{ء ح د B006}` as mountain-scale target; fork D adds `{ك ف ء B002}` as overturning result. Predictions: agent, object, impact syntax, hard target, motion result.
- **UNUSED_AT_FREEZE and test.** All ten occurrences and twelve constructions were tested. None supplies a wielder or impact clause. `(K: قُلْ is speech; K: ٱلصَّمَدُ is a nominative predicate; K: أَحَدٌ ≠ أُحُد by vocalization and syntax; K: كُفُوًا is the kana equality predicate)`. The avalanche is vivid but wholly form-remote.
- **Grade: unlikely.** Pass 2 retains the complete physical fork, then rejects it through four independent local constraints.

#### L009 — O1 × ق و ل B009 — Negotiation with an absent counterpart

- **Initial image.** `(E: ق و ل B009, form-remote)` creates reciprocal negotiation over an affair and predicts two speakers, turns, and a matter under discussion.
- **Word ledger.** `O1=focus B009`; `O2=R ء ل ه B001/B002 named principal`; `O3=R ء ح د B001 one party / B002 no party; B003–B006 0`; `O4=R ء ل ه B002 repeated principal`; `O5=R ص م د B005 affair under attention + B001 relied-upon party; B002–B004/B006–B007 0`; `O6=و ل د B001–B006 possible disputed content only`; `O7=و ل د B001–B006 possible content only`; `O8=ك و ن B001–B006 0`; `O9=R ك ف ء B001 counterpart/opposition; B002–B005 0`; `O10=R ء ح د B002 no counterpart; B001/B003–B006 0`.
- **Construction ledger.** `X1=K unilateral imperative/quote`; `X2=R one identified party`; `X3=R affair/reliance predicate`; `X4=0`; `X5=0`; `X6=0`; `X7=R counterpart relation`; `X8=R no counterpart`; `X9=K one referent chain`; `X10=R one→none`; `X11=0`; `X12=0`.
- **Forks and freeze.** `{ق و ل B009, ص م د B005, ك ف ء B001}` generates negotiation about an attended affair with a counterpart. A second fork uses final ء ح د B002 to make the counterpart slot empty: a one-sided “negotiation impossible” image. Predictions: reciprocal form, second voice, response turn, or explicit affair.
- **UNUSED_AT_FREEZE and test.** X1 and X9 defeat reciprocity: one addressee is commanded to utter one continuous description. `(K: قُلْ is simple imperative, not قاول/تقاول; K: no response clause)`. Birth and equality denials can be discussion content but do not create negotiation.
- **Grade: weak.** Several remote roles align, yet the defining reciprocal speech event is absent.

#### L010 — O1 × ق و ل B010 — Controlling judgment, oversight, and opposition

- **Initial image.** `(E: ق و ل B010, form-remote)` posits one actor imposing control or judgment over another.
- **Word ledger.** `O1=focus B010`; `O2=R ء ل ه B001 authority center / B002 name`; `O3=R ء ح د B001 sole controller; B002–B006 0`; `O4=R ء ل ه B001/B002 re-anchored`; `O5=R ص م د B005 oversight + B001 reliance; B002–B004/B006–B007 0`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=R ك و ن B003 standing-for/guarantee; B001/B002/B004–B006 0`; `O9=R ك ف ء B001 opposing/equal party; B002–B005 0`; `O10=R ء ح د B002 no opposing party; B001/B003–B006 0`.
- **Construction ledger.** `X1=R directive force but K no controlled patient`; `X2=R named center`; `X3=R oversight predicate`; `X4=0`; `X5=0`; `X6=0`; `X7=R opposition relation`; `X8=R excluded opponent`; `X9=K same referent, no second agent`; `X10=0`; `X11=0`; `X12=0`.
- **Forks and freeze.** `{ق و ل B010, ء ل ه B001, ص م د B005, ك و ن B003}` yields a controlling overseer/guarantor; `{ك ف ء B001}` adds an opponent role later denied. Predictions: controller, patient, controlled act, or adjudication.
- **UNUSED_AT_FREEZE and test.** The imperative supplies directive force but not B010's control construction. No patient or governed act occurs `(K: قُلْ morphology; K: quote contains predications about G, not a judgment imposed on another)`. Final no-equal syntax removes a peer, not a controlled subject.
- **Grade: weak.** The authority cluster is more complete than a singleton, but all distinctive roles remain form-remote.

#### L011 — O1 × ق و ل B011 — Conjecture tested against categorical clauses

- **Initial image.** `(E: ق و ل B011, form-remote)` treats saying as conjecture and predicts uncertainty, interrogation, or competing hypotheses.
- **Word ledger.** `O1=focus B011`; `O2=E ء ل ه B002 conjecture's named subject; B001 0`; `O3=R ء ح د B001 hypothesis property; B002–B006 0`; `O4=R B002 repeated subject`; `O5=R ص م د B001/B002 alternative hypotheses; B003–B007 tested`; `O6=R و ل د B003 proposition tested under negation; B001/B002/B004–B006 tested`; `O7=R B003 second test; others tested`; `O8=R ك و ن B001 state test; B002–B006 0`; `O9=R ك ف ء B001 equality hypothesis; B002–B005 0`; `O10=R ء ح د B002 exhaustive rejection; B001/B003–B006 tested`.
- **Construction ledger.** `X1=K imperative declaration, no question`; `X2=K categorical predication`; `X3=K categorical predication`; `X4=0`; `X5=K negation not uncertainty`; `X6=R two tested propositions`; `X7=R relation tested`; `X8=K categorical closure`; `X9=0`; `X10=0`; `X11=R hypothesis-elimination shape`; `X12=0`.
- **Forks and freeze.** `{ق و ل B011, ء ل ه B002}` freezes as a conjecture about G. A “hypothesis elimination” fork uses O6–O10 as successive rejected alternatives. It predicts interrogative or epistemic marking that distinguishes supposition from assertion.
- **UNUSED_AT_FREEZE and test.** Every clause is declarative; لَمْ denies events rather than marking doubt. `(K: no interrogative; K: local imperative does not take the dossier's conjectural construction)`. The elimination geometry exists, but its modality is categorical.
- **Grade: unlikely.** Exhaustive testing strengthens the opposing constraint rather than the conjectural image.

#### L012 — O1 × ق و ل B012 — Latent inward proposition externalized by قُلْ

- **Initial image.** `(E: ق و ل B012, form-remote)` supplies a saying conceived inwardly but not expressed; the local imperative can become a transition cue rather than the branch's direct realization.
- **Word ledger.** `O1=focus B012`; `O2=E ء ل ه B002 named inner content; B001 R devotional locus`; `O3=E ء ح د B001 first proposition; B002–B006 0`; `O4=C B002 content re-anchor`; `O5=C ص م د B001/B002 second proposition; B003–B007 tested`; `O6=C و ل د B003 negated proposition; other branches tested`; `O7=C B003 inverse proposition; others tested`; `O8=C ك و ن B001 final proposition frame; B002–B006 0`; `O9=C ك ف ء B001 relation content; B002–B005 0`; `O10=C ء ح د B002/B001 closure; B003–B006 0`.
- **Construction ledger.** `X1=E externalization transition + K no stated prior concealment`; `X2=E first content`; `X3=C`; `X4=C`; `X5=C`; `X6=C`; `X7=C`; `X8=C`; `X9=C content continuity`; `X10=C closure`; `X11=C staged utterance`; `X12=0`.
- **Forks and freeze.** `{ق و ل B012, X1, ء ل ه B002, ء ح د B001}` freezes as “a latent proposition is brought into voiced form.” Predictions: inner locus, prior silence/concealment, or explicit before→after contrast; later material should form one coherent proposition.
- **UNUSED_AT_FREEZE and test.** O4–O10 strongly complete coherent content but do not corroborate inwardness. `(K: no word or attachment supplies mind/self/concealment; X1 directly licenses B001 outward speech)`. The outward half is exact; the inward half remains seed-only.
- **Grade: weak.** A complete externalization image forms, but its initial state lacks independent support.

#### L013 — O1 × ق و ل B013 — A doctrine with positive commitments and exclusions

- **Initial image.** `(E: ق و ل B013, form-remote)` treats القول as an adopted position or doctrine.
- **Word ledger.** `O1=focus B013`; `O2=E ء ل ه B002 doctrine's subject; B001 R worship relation`; `O3=E ء ح د B001 first commitment; B002–B006 tested`; `O4=E B002 name refresh`; `O5=E ص م د B001 second commitment; B002 R compact-core doctrine; B003–B007 tested`; `O6=C و ل د B003/B001 child exclusion; B002/B004–B006 tested`; `O7=C B003/B002 origin exclusion; others tested`; `O8=C ك و ن B001 negated state; B002–B006 tested`; `O9=C ك ف ء B001 peer exclusion; B002–B005 tested`; `O10=C ء ح د B002 exhaustive exclusion + B001 recurrence; B003–B006 tested`.
- **Construction ledger.** `X1=E stated position`; `X2=E first commitment`; `X3=E second commitment`; `X4=E continuity`; `X5=C exclusions`; `X6=C inverse lineage`; `X7=C comparison target`; `X8=C final exclusion`; `X9=C subject continuity`; `X10=C return`; `X11=C positive→negative architecture`; `X12=C weak formula cohesion`.
- **Forks and freeze.** Main `{ق و ل B013, ء ل ه B002, ء ح د B001, ص م د B001, X1–X4}` freezes as a compact position: named G is one and the relied-upon center. Rival `{ص م د B002}` makes the position about a compact core. Predictions: reject origin, offspring, and peer relations; close exhaustively.
- **UNUSED_AT_FREEZE and test.** O6–O10 and X5–X12 provide exactly those exclusions. Constraint: no believer, assent, school, or اعتقاد morphology is expressed `(K: قُلْ locally commands speech)`. B013 classifies the resulting proposition-set but does not generate its local speech act.
- **Grade: medium.** The whole sequence has doctrine-like geometry, with strong downstream fit but remote seed morphology.

#### L014 — O1 × ق و ل B014 — A thing indicated by its complete profile

- **Initial image.** `(E: ق و ل B014, form-remote)` lets a thing “say” or indicate its state; the referent becomes legible through a profile rather than speaking literally.
- **Word ledger.** `O1=focus B014`; `O2=E ء ل ه B002 profiled referent; B001 0`; `O3=E ء ح د B001 positive feature; B002–B006 tested`; `O4=E B002 profile anchor repeated`; `O5=E ص م د B001 relational feature; B002 R physical profile; B003–B007 tested`; `O6=C و ل د B003 excluded outgoing relation; others tested`; `O7=C B003 excluded incoming relation; others tested`; `O8=C ك و ن B001 state frame; others tested`; `O9=C ك ف ء B001 comparison feature; others tested`; `O10=C ء ح د B002/B001 completes profile; B003–B006 tested`.
- **Construction ledger.** `X1=K actual speaker is addressee`; `X2=E profile starts`; `X3=E profile expands`; `X4=E anchor`; `X5=C negative features`; `X6=C relation symmetry`; `X7=C target`; `X8=C completion`; `X9=C one referent`; `X10=C profile bracket`; `X11=C layered profile`; `X12=0`.
- **Forks and freeze.** Relational fork `{ق و ل B014, ء ل ه B002, ء ح د B001, ص م د B001}` freezes as a thing indicated by unity and directional reliance. Physical fork substitutes `{ص م د B002}`. Predictions: later clauses should add diagnostic exclusions and end at full differentiation.
- **UNUSED_AT_FREEZE and test.** Birth and equality denials complete the diagnostic profile; final recurrence closes it. `(K: grammatical speaker remains the commanded 2MS addressee; G does not literally utter the clauses)`. B014 is therefore a secondary profile metaphor.
- **Grade: medium.** Ordered role completion is strong, but the local occurrence does not realize thing-as-indicator.

#### L015 — O1 × ق و ل B015 — Care, oversight, reliance, and guarantee

- **Initial image.** `(E: ق و ل B015, form-remote)` gives sincere care directed to a matter and predicts caretaker, cared-for object, and sustained attention.
- **Word ledger.** `O1=focus B015`; `O2=R ء ل ه B001 worshipped/cared-for center + B002 name`; `O3=R ء ح د B001 sole caretaker/center; B002–B006 0`; `O4=R ء ل ه B001/B002 re-anchor`; `O5=E ص م د B005 oversight-with-care + R B001 relied-upon in affairs; B002–B004/B006–B007 tested`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=E ك و ن B003 guarantee/standing for someone; B001/B002/B004–B006 0`; `O9=R ك ف ء B001 counterpart/reciprocity; B002–B005 0`; `O10=R ء ح د B002 no counterpart; B001/B003–B006 0`.
- **Construction ledger.** `X1=K lacks يقول بكذا construction`; `X2=R named caretaker`; `X3=E oversight predicate fork`; `X4=0`; `X5=0`; `X6=0`; `X7=R relational beneficiary`; `X8=0`; `X9=R one referent`; `X10=0`; `X11=0`; `X12=0`.
- **Forks and freeze.** Fork A `{ق و ل B015, ص م د B005}` is attentive oversight of an affair. Fork B adds `{ص م د B001, ك و ن B003}` to form a relied-upon overseer who guarantees another. Predictions: affair, beneficiary, care act, guarantee, or syntactic ب-object.
- **UNUSED_AT_FREEZE and test.** No occurrence supplies the cared-for affair or beneficiary. `(K: قُلْ lacks يقول بكذا; K: الصمد is predicate of ٱللَّهُ, not an affair; K: يَكُن is copular, not B003)`. Final relation concerns equality, not care.
- **Grade: weak.** Three dossiers converge on a support scene, but every distinctive local form resists it.

#### L016 — O1 × ق و ل B016 — Definition by positive profile and negative differentiae

- **Initial image.** `(E: ق و ل B016, form-remote)` supplies the technical image of stating a thing's حدّ.
- **Word ledger.** `O1=focus B016`; `O2=E ء ل ه B002 definiendum/name; B001 R worship-definition`; `O3=E ء ح د B001 first positive differentia; B002–B006 tested`; `O4=E B002 name re-anchor`; `O5=E ص م د B001 second positive differentia; B002 R compact-core definition; B003–B007 tested`; `O6=C و ل د B003/B001 downstream exclusion; B002/B004–B006 tested`; `O7=C B003/B002 upstream exclusion; others tested`; `O8=C ك و ن B001 negative predication; B002–B006 tested`; `O9=C ك ف ء B001 genus-peer exclusion; B002–B005 tested`; `O10=C ء ح د B002 exhaustive differentia + B001 recurrence; B003–B006 tested`.
- **Construction ledger.** `X1=E spoken frame but K local B001`; `X2=E identity+property`; `X3=E second property`; `X4=E definiendum refresh`; `X5=C negative differentiae`; `X6=C two orientations`; `X7=C comparison`; `X8=C exhaustive terminus`; `X9=C same subject`; `X10=C return to first property`; `X11=C positive→negative order`; `X12=C weak formal closure`.
- **Forks and freeze.** Main `{ق و ل B016, ء ل ه B002, ء ح د B001, ص م د B001, X2–X4}`: a named definiendum receives two positive specifications. Rival physical definition substitutes ص م د B002. Predictions: exclude downstream product, upstream source, and any coequal; end at an exhaustive candidate expression.
- **UNUSED_AT_FREEZE and test.** O6–O10 and X5–X12 satisfy every predicted role. `(K: local قُلْ remains an imperative speech verb; B016 supplies secondary geometry only)`. The physical fork is further constrained by absence of body/container roles.
- **Grade: medium-strong.** Remote morphology prevents “strong,” but the ordered prediction of unused clauses and exact terminal reactivation is highly specific.

### 5.2 O2 — 112:1:3 ٱللَّهُ — ء ل ه, first occurrence

#### L017 — O2 × ء ل ه B001 — Worshipped center becomes the endpoint of reliance

- **Initial image.** `(E: ء ل ه B001)` opens a worshipped/object-of-worship relation around the first named occurrence.
- **Word ledger.** `O1=E ق و ل B001 commands articulation; B002–B016 tested, B013 doctrine R`; `O2=focus B001`; `O3=E ء ح د B001 sole center; B002 K positive position; B003–B006 0`; `O4=C ء ل ه B001 repeated center + B002 name dimension`; `O5=E ص م د B001 endpoint of affairs/needs; B002 R compact center; B003–B007 tested`; `O6=C و ل د B003 active no-child edge; B001/B002/B004–B006 tested`; `O7=C B003 passive no-origin edge; others tested`; `O8=C ك و ن B001 final occurrence frame; B002–B006 tested`; `O9=C ك ف ء B001 no coequal center; B002–B005 tested`; `O10=C ء ح د B002 no candidate + B001 recurrence; B003–B006 tested`.
- **Construction ledger.** `X1=E quote about center`; `X2=E name+unity`; `X3=E reliance predicate`; `X4=C re-anchor`; `X5=C exclusions`; `X6=C lineage inversion`; `X7=C comparison to G`; `X8=C no equal`; `X9=C same G`; `X10=C sole→none`; `X11=C positive center→pruned relations`; `X12=0`.
- **Forks and freeze.** Main `{ء ل ه B001, ء ح د B001, ص م د B001, X2–X3}`: one worshipped center toward which need/affair-directed reliance converges. Rival `{ص م د B002}`: one compact center. Predictions: preserve G; no superior origin, dependent same-lineage product, or coequal center.
- **UNUSED_AT_FREEZE and test.** O4 and O6–O10 supply continuity and all three relation exclusions. `(K: no worshipper, ritual, عبد, or تنسك event appears; B001 contributes only a secondary center relation)`. The physical rival lacks body/container roles.
- **Grade: medium.** The center topology is completed independently, but worship is not instantiated by local syntax.

#### L018 — O2 × ء ل ه B002 — Pronoun resolves to a name that anchors four ayahs

- **Initial image.** `(E: ء ل ه B002)` supplies اسم الله; X2 resolves preceding هُوَ to the proper name and attaches a unity predicate.
- **Word ledger.** `O1=E ق و ل B001 quoted naming; B002–B016 tested, B016 definition R`; `O2=focus B002`; `O3=E ء ح د B001 predicate; B002 K here; B003–B006 0`; `O4=C ء ل ه B002 exact name recurrence; B001 distinct worship dimension tested`; `O5=C ص م د B001 predicate content; B002–B007 tested`; `O6=C و ل د B003 3MS active; B001/B002/B004–B006 tested`; `O7=C B003 3MS passive; others tested`; `O8=C ك و ن B001 3MS copula; B002–B006 tested`; `O9=C ك ف ء B001 relation to pronoun; B002–B005 tested`; `O10=C ء ح د B002/B001 terminal scope/recurrence; B003–B006 tested`.
- **Construction ledger.** `X1=E quoted identification`; `X2=E pronoun→name→predicate`; `X3=C new predicate`; `X4=C exact name refresh`; `X5=C same subject under negation`; `X6=C 3MS inverse verbs`; `X7=C pronoun back-reference`; `X8=C final clause`; `X9=C full referent chain`; `X10=C terminal reactivation`; `X11=C four-layer description`; `X12=0`.
- **Forks and freeze.** `{ء ل ه B002, X2, ء ح د B001}` freezes after O3 as “unresolved 3MS → named G → first property.” Predictions: exact re-anchoring, continued 3MS agreement, pronominal return, no competing named node.
- **UNUSED_AT_FREEZE and test.** O4, O6–O8, X4, X7, and X9 fulfill each referential prediction; O5/O9/O10 complete content. The same name in basmala independently pre-activates the anchor `(C: ٱللَّهِ opening-context)`. `(K: oath and vocative dimensions of B002 are absent; local role is nominative PN)`.
- **Grade: strong.** Exact morphology and multiple independent forms of recurrence sustain one temporary discourse node.

### 5.3 O3 — 112:1:4 أَحَدٌ — ء ح د, first occurrence

#### L019 — O3 × ء ح د B001 — Unity protected by three directional exclusions

- **Initial image.** `(E: ء ح د B001)` is contextually exact as the nominative predicate of ٱللَّهُ and activates absolute unity.
- **Word ledger.** `O1=E ق و ل B001 frame; B002–B016 tested, B016 R`; `O2=E ء ل ه B002 bearer/name; B001 R worship center`; `O3=focus B001`; `O4=C ء ل ه B002 re-anchor; B001 tested`; `O5=E ص م د B001 one-center direction; B002 R solid undivided core; B003–B007 tested`; `O6=C و ل د B003 active outward denial; B001/B002/B004–B006 tested`; `O7=C B003 passive inward denial; others tested`; `O8=C ك و ن B001 final state; B002–B006 tested`; `O9=C ك ف ء B001 parallel-equivalent denial; B002–B005 tested`; `O10=C ء ح د B002 current negative scope + B001 exact return; B003–B006 tested`.
- **Construction ledger.** `X1=E asserted content`; `X2=E exact predication`; `X3=E center expansion`; `X4=C same bearer`; `X5=C exclusions`; `X6=C out/in`; `X7=C to-G relation`; `X8=C parallel closure`; `X9=C one G`; `X10=C same form/new role`; `X11=C build→prune`; `X12=C sound maintenance`.
- **Forks and freeze.** Relational `{ء ح د B001, ء ل ه B002, ص م د B001}` freezes as one named endpoint. Physical rival replaces B001 with `{ص م د B002}` to form one undivided compact core. Predictions: deny outgoing product, incoming origin, and parallel equivalent; return to أَحَدٌ at closure.
- **UNUSED_AT_FREEZE and test.** O6/O7/O9 supply the three orientations; O10 and X10 supply exact reactivation; X8 closes the grammatical slot. `(K: graph directions are secondary geometry; birth remains birth)`. Physical rival is constrained by no body/cavity.
- **Grade: strong.** The seed anticipates unused role directions and the exact terminal cue through independent lexical and syntactic channels.

#### L020 — O3 × ء ح د B002 — A dormant negative-scope branch realized only at O10

- **Initial image.** `(E: ء ح د B002)` predicts exhaustive negative scope but is locally blocked because O3 is a positive predicate `(K: X2)`.
- **Word ledger.** `O1=ق و ل B001–B016 tested, B001 frame only`; `O2=ء ل ه B001–B002 tested`; `O3=focus B002 with K local syntax`; `O4=ء ل ه B001–B002 0`; `O5=ص م د B001–B007 0`; `O6=R و ل د B001–B003 first negative environment; B004–B006 0`; `O7=R B001–B003 second negative environment; B004–B006 0`; `O8=R ك و ن B001 continuing negative scope; B002–B006 0`; `O9=E ك ف ء B001 candidate relation; B002–B005 0`; `O10=C ء ح د B002 exact contextual realization + B001 recurrence; B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=K positive predication`; `X3=0`; `X4=0`; `X5=E creates negative field`; `X6=R narrower negative roles`; `X7=E candidate relation`; `X8=C delayed subject in negation`; `X9=0`; `X10=C branch switch`; `X11=C delayed realization`; `X12=0`.
- **Forks and freeze.** The O3 branch cannot freeze as local meaning. It freezes as a *latent root-family expectation*: if أَحَدٌ recurs under negation in an open candidate role, B002 can activate. Prediction: exact recurrence + negative governor + class-like subject slot.
- **UNUSED_AT_FREEZE and test.** X5 builds negative context; O9/X7 opens the comparison class; O10/X8 supplies exactly the delayed subject. `(K: B002 remains invalid for O3 itself; B001 governs the first occurrence)`.
- **Grade: medium.** It is a failed local branch but a precise temporally delayed prediction.

#### L021 — O3 × ء ح د B003 — One-versus-zero count model

- **Initial image.** `(E: ء ح د B003, form-remote)` creates the minimum unit in counting/composition.
- **Word ledger.** `O1=R ق و ل B016 definitional count; B001/B002–B015 tested`; `O2=E ء ل ه B002 counted referent; B001 0`; `O3=focus B003`; `O4=C B002 same referent`; `O5=R ص م د B001 one center + B002 indivisible unit; B003–B007 tested`; `O6=R و ل د B001 possible added member; B002–B006 tested`; `O7=R B001 possible source member; others tested`; `O8=C ك و ن B001 zero occurrence frame; B002–B006 tested`; `O9=E ك ف ء B001 class to count; B002–B005 tested`; `O10=C ء ح د B002/B003 zero candidates + B001 recurrence; B004–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=K no counted noun but E one-slot image`; `X3=R one-center`; `X4=0`; `X5=C count reduced by negation`; `X6=R no lineage additions`; `X7=E comparison class`; `X8=C zero fillers`; `X9=0`; `X10=C one→zero contrast`; `X11=C ordered reduction`; `X12=0`.
- **Forks and freeze.** `{ء ح د B003, ء ل ه B002, ص م د B001}` yields a one-item center; `{ك ف ء B001}` defines the comparison class. Prediction: final syntax lowers the number of equivalents below one.
- **UNUSED_AT_FREEZE and test.** O8/O10 and X8 yield an empty candidate class. `(K: O3 has no counted noun or numeral construction; B001 is exact there, B002 exact at O10)`. The count model is secondary logic, not local lexical replacement.
- **Grade: weak.** One→zero geometry is coherent, but both occurrences have better contextual branches.

#### L022 — O3 × ء ح د B004 — Firstness, annexation, or Sunday

- **Initial image.** `(E: ء ح د B004, form-remote)` predicts ordinal firstness, iḍāfa, or a calendrical day.
- **Word ledger.** `O1=ق و ل B001–B016 0`; `O2=ء ل ه B001–B002 0`; `O3=focus B004`; `O4=ء ل ه B001–B002 0`; `O5=R ص م د B007 duration + B002 elevated place; B001/B003–B006 0`; `O6=R و ل د B003 temporal event; B001/B002/B004–B006 0`; `O7=R B003 second event; others 0`; `O8=R ك و ن B001 time occurrence; B002–B006 0`; `O9=ك ف ء B001–B005 0`; `O10=R ء ح د B004 repeated first/day possibility; B001–B003/B005–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=K indefinite predicate, no iḍāfa`; `X3=0`; `X4=0`; `X5=R temporal negatives`; `X6=0`; `X7=0`; `X8=K final indefinite subject`; `X9=0`; `X10=R repeated form but same mismatch`; `X11=R succession, no calendar`; `X12=0`.
- **Forks and freeze.** `{ء ح د B004, ص م د B007, ك و ن B001}` generates a weak “first point persisting through time” fork; a Sunday/calendar fork also starts. Predictions: ordered series, construct relation, date/day, or explicit temporal index.
- **UNUSED_AT_FREEZE and test.** Sequence and ك و ن provide time generally but no ordinal or calendar. `(K: both أَحَدٌ tokens are indefinite nominative, neither construct-state nor day name)`. No branch supplies a series with O3 as first member.
- **Grade: unlikely.** Temporal neighbors do not complete B004's distinctive syntax.

#### L023 — O3 × ء ح د B005 — Individuated candidates tested one by one

- **Initial image.** `(E: ء ح د B005, form-remote)` evokes acting alone or individuals arriving separately.
- **Word ledger.** `O1=ق و ل B001–B016 0`; `O2=E ء ل ه B002 central referent; B001 0`; `O3=focus B005`; `O4=C B002 re-anchor`; `O5=R ص م د B001 one destination; B002–B007 tested`; `O6=R و ل د B001 potential individual offspring; B002–B006 tested`; `O7=R B001 potential individual predecessor; others tested`; `O8=C ك و ن B001 occurrence test; B002–B006 0`; `O9=E ك ف ء B001 candidate relation; B002–B005 0`; `O10=C ء ح د B002 exhaustive individuals + B005 distributive simulation; B001/B003–B004/B006 tested`.
- **Construction ledger.** `X1=0`; `X2=K no distributive action`; `X3=R one destination`; `X4=0`; `X5=C repeated candidate rejection`; `X6=R two candidate classes`; `X7=E equality test`; `X8=C delayed candidate`; `X9=0`; `X10=C return`; `X11=C progressive elimination`; `X12=0`.
- **Forks and freeze.** `{ء ح د B005, ك ف ء B001}` generates an evaluator considering possible equals individually; `{ص م د B001}` gives them one destination/standard. Prediction: distributive marker, plural candidates, arrival, or separate acts.
- **UNUSED_AT_FREEZE and test.** Final negative scope can be simulated as testing each candidate, but B002 already supplies this without motion/distribution. `(K: no arrival, plural, or آحاد morphology; O3 is a predicate)`.
- **Grade: weak.** A candidate-by-candidate simulation forms, but the branch's distinctive event is absent.

#### L024 — O3 × ء ح د B006 — Mountain, rock, strike, and fixed-height fork

- **Initial image.** `(E: ء ح د B006, form-remote)` creates Mount Uḥud and predicts proper-name/place syntax.
- **Word ledger.** `O1=R ق و ل B008 striking stick; B001–B007/B009–B016 tested`; `O2=ء ل ه B001–B002 0`; `O3=focus B006`; `O4=ء ل ه B001–B002 0`; `O5=R ص م د B002 rock/elevated hard place + B006 stick-strike + B007 endurance; B001/B003–B005 0`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=R ك و ن B002 place; B001/B003–B006 0`; `O9=R ك ف ء B002 overturning/diversion; B001/B003–B005 0`; `O10=R ء ح د B006 exact root-form recurrence but same mismatch; B001–B005 tested`.
- **Construction ledger.** `X1=K speech`; `X2=K أَحَدٌ predicate not proper name`; `X3=R hard/elevated predicate image`; `X4=0`; `X5=0`; `X6=0`; `X7=0`; `X8=K final subject not place`; `X9=0`; `X10=R repeated mountain sound only`; `X11=0`; `X12=R coda only`.
- **Forks and freeze.** Place fork `{ء ح د B006, ص م د B002, ك و ن B002}` is a hard elevated mountain/place. Impact fork adds `{ق و ل B008, ص م د B006, ك ف ء B002}`: a stick-struck rock/mountain that is overturned. Persistence fork adds ص م د B007. Predictions: locative/proper name, physical target, impact agent, or height.
- **UNUSED_AT_FREEZE and test.** `(K: أَحَدٌ is not أُحُد; O3 is indefinite predicate, O10 delayed subject; K: الصمد is nominal divine predicate; K: يَكُن is copula; K: كُفُوًا equality predicate)`. No physical participant survives local syntax.
- **Grade: unlikely.** The exhaustive avalanche is structurally complete as an image and decisively defeated as passage-local synthesis.

### 5.4 O4 — 112:2:1 ٱللَّهُ — ء ل ه, second occurrence

#### L025 — O4 × ء ل ه B001 — Repeated worshipped center immediately receives reliance

- **Initial image.** `(E: ء ل ه B001)` starts after O3 has already activated unity; O4 repeats the named center immediately before ٱلصَّمَدُ.
- **Word ledger.** `O1=C ق و ل B001 spoken frame; B002–B016 tested`; `O2=C ء ل ه B001 earlier center + B002 name; occurrence kept distinct`; `O3=C ء ح د B001 prior unity; B002–B006 tested`; `O4=focus B001`; `O5=E ص م د B001 reliance/need direction; B002 R solid center; B003–B007 tested`; `O6=C و ل د B003/B001 no outgoing lineage; B002/B004–B006 tested`; `O7=C B003/B002 no incoming lineage; others tested`; `O8=C ك و ن B001 occurrence; B002–B006 tested`; `O9=C ك ف ء B001 no equal center; B002–B005 tested`; `O10=C ء ح د B002 no candidate + B001 return; B003–B006 tested`.
- **Construction ledger.** `X1=C quote frame`; `X2=C active prior center`; `X3=E direct predication`; `X4=E repeated center`; `X5=C relation pruning`; `X6=C two directions`; `X7=C to-G`; `X8=C parallel exclusion`; `X9=C same G`; `X10=C closure`; `X11=C boundary reset`; `X12=0`.
- **Forks and freeze.** Main `{ء ل ه B001 at O4, X4, ص م د B001, X3}` freezes as a reactivated worshipped center now specified as relied upon in affairs/needs. Physical rival uses ص م د B002. Predictions: no upper source, lower same-lineage product, or equal alternate center.
- **UNUSED_AT_FREEZE and test.** O6–O10 satisfy the three directional exclusions and exhaustive ending. `(K: no worshipper/ritual role; B001 remains secondary)`. O2 is corroborative prior activation, not merged with O4.
- **Grade: medium-strong.** Adjacency to الصمد and exact subject repetition make this occurrence more productive than O2 for the center/reliance model.

#### L026 — O4 × ء ل ه B002 — Name repetition refreshes G before ellipsis

- **Initial image.** `(E: ء ل ه B002)` is exact proper-name use at O4; X4 makes its repeated position the seed's defining event.
- **Word ledger.** `O1=C ق و ل B001 frame; B002–B016 tested, B016 R`; `O2=C ء ل ه B002 first anchor; B001 dimension tested`; `O3=C ء ح د B001 property already attached; B002–B006 tested`; `O4=focus B002`; `O5=E ص م د B001 new predicate; B002–B007 tested`; `O6=C و ل د B003 implicit 3MS active; other branches tested`; `O7=C B003 implicit 3MS passive; others tested`; `O8=C ك و ن B001 implicit 3MS; B002–B006 tested`; `O9=C ك ف ء B001 relation to suffix; B002–B005 tested`; `O10=C ء ح د B002/B001 closure; B003–B006 tested`.
- **Construction ledger.** `X1=C quote continuity`; `X2=C first anchor`; `X3=E new predication`; `X4=E exact refresh`; `X5=C same G`; `X6=C same G`; `X7=C pronominal return`; `X8=C final clause`; `X9=C predicted chain`; `X10=C`; `X11=C boundary refresh`; `X12=0`.
- **Forks and freeze.** `{ء ل ه B002 at O4, X4, X3, ص م د B001}` freezes as “the named node is refreshed at a pause and given a new predicate.” Predictions: following lexical subjects can remain unspoken while 3MS agreement and a later suffix preserve G.
- **UNUSED_AT_FREEZE and test.** O6/O7/O8 supply implicit 3MS; O9's governing phrase uses the 3MS suffix; X9 confirms uninterrupted identity. Basmala independently supplies earlier opening activation `(C: ٱللَّهِ opening-context)`. `(K: no oath/vocative use)`.
- **Grade: strong.** Position, exact repetition, predication, ellipsis, and pronominal return jointly explain O4's role.

### 5.5 O5 — 112:2:2 ٱلصَّمَدُ — ص م د

#### L027 — O5 × ص م د B001 — Convergent center predicts missing relation directions

- **Initial image.** `(E: ص م د B001)` supplies قصد/اعتماد toward a relied-upon intended center, locally predicated of repeated ٱللَّهُ.
- **Word ledger.** `O1=C ق و ل B001 frame; B002–B016 tested`; `O2=E ء ل ه B002 named G + B001 center fork`; `O3=E ء ح د B001 one center; B002–B006 tested`; `O4=E ء ل ه B002 re-anchor; B001 tested`; `O5=focus B001`; `O6=C و ل د B003 active outgoing denial; B001/B002/B004–B006 tested`; `O7=C B003 passive incoming denial; others tested`; `O8=C ك و ن B001 occurrence frame; B002–B006 tested`; `O9=C ك ف ء B001 parallel denial; B002–B005 tested`; `O10=C ء ح د B002 exhaustive candidate + B001 return; B003–B006 tested`.
- **Construction ledger.** `X1=C utterance frame`; `X2=E G+one`; `X3=E exact predication`; `X4=E re-anchor`; `X5=C widening exclusions`; `X6=C out/in`; `X7=C to-G comparison`; `X8=C empty parallel slot`; `X9=C G continuity`; `X10=C return`; `X11=C center→boundary`; `X12=C weak coda link`.
- **Forks and freeze.** `{ص م د B001, ء ل ه B002, ء ح د B001, X3–X4}` freezes as one named endpoint for directed reliance. Predictions created by the topology: no source above G, no same-kind product below G, no parallel equal beside G; preserve G; stop after the comparison class is emptied.
- **UNUSED_AT_FREEZE and test.** O6/O7/O9 realize the three orientations; O8/O10 and X8 empty the candidate slot; X10 reactivates unity. `(K: no seeker or need is an expressed syntactic argument; B001's approach arrows remain secondary imagery)`.
- **Grade: strong.** A specific direction-of-reliance branch predicts three independent unused relation tests and the stopping cue.

#### L028 — O5 × ص م د B002 — Undivided compact core with blocked generative routes

- **Initial image.** `(E: ص م د B002, form-remote)` creates solidity, compactness, and no cavity.
- **Word ledger.** `O1=R ق و ل B016 definition + B014 profile; B001–B013/B015 tested`; `O2=E ء ل ه B002 bearer; B001 0`; `O3=E ء ح د B001 undivided one; B002–B006 tested`; `O4=E ء ل ه B002 re-anchor`; `O5=focus B002`; `O6=C و ل د B003/B005 no outward generation; B001/B002/B004/B006 tested`; `O7=C B003/B005 no inward derivation; others tested`; `O8=C ك و ن B001 no occurring state; B002 R place/height; B003–B006 tested`; `O9=C ك ف ء B001 no duplicate; B002–B005 tested`; `O10=C ء ح د B001 recurrence + B002 scope; B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=E one bearer`; `X3=E predicate`; `X4=E same bearer`; `X5=C blocked relations`; `X6=C output/input geometry`; `X7=C comparison`; `X8=C no duplicate`; `X9=C`; `X10=C undivided return`; `X11=C`; `X12=0`.
- **Forks and freeze.** Core fork `{ص م د B002, ء ح د B001, ء ل ه B002}`: compact, non-hollow, undivided center. Place fork adds `{ك و ن B002}` to B002's hard/elevated location. Predictions: no opening, ingress/egress, derivation, division, or duplicate.
- **UNUSED_AT_FREEZE and test.** O6/O7 can corroborate only abstract no-output/no-input *generation*; O9 denies a duplicate; O10 returns unity. `(K: no body, cavity, container, opening, place, or transfer role; birth does not lexically mean ingress/egress)`.
- **Grade: medium.** Several later relations complete the geometry, but the physical scene is unexpressed.

#### L029 — O5 × ص م د B003 — Stoppered vessel and sealed-boundary fork

- **Initial image.** `(E: ص م د B003, form-remote)` supplies a bottle stopper or action making one and predicts vessel, mouth, content, and closure.
- **Word ledger.** `O1=R ق و ل B016 bounded definition; B001–B015 tested`; `O2=E ء ل ه B002 bearer only; B001 0`; `O3=E ء ح د B001 single closure; B002–B006 tested`; `O4=E ء ل ه B002 re-anchor`; `O5=focus B003 + E same-root B002 solid enclosure`; `O6=C و ل د B003/B005 no output; B001/B002/B004/B006 tested`; `O7=C B003/B005 no input/origin; others tested`; `O8=ك و ن B001–B006 tested, B002 R container-place`; `O9=C ك ف ء B001 no second vessel/equal; B002–B005 tested`; `O10=C ء ح د B001/B002 closure; B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=E bearer`; `X3=E predicate but K no stoppering verb`; `X4=0`; `X5=C closure repetitions`; `X6=C secondary in/out`; `X7=0`; `X8=C no duplicate`; `X9=0`; `X10=C`; `X11=C stopping metaphor`; `X12=0`.
- **Forks and freeze.** `{ص م د B003, ص م د B002, ء ح د B001}` freezes as a sealed vessel; `{ك و ن B002}` adds enclosure/place. Predictions: bottle/opening/content and an operation sealing it; later no transfer across boundary.
- **UNUSED_AT_FREEZE and test.** O6/O7 weakly match blocked generation directions and O9 no duplicate. `(K: no vessel, content, opening, or stopper; ٱلصَّمَدُ is a nominative predicate, not a stoppering event; birth remains generation)`.
- **Grade: weak.** The full sealed image is retained and tested, but its defining participants are absent.

#### L030 — O5 × ص م د B004 — Textile binding and shelter-panel fork

- **Initial image.** `(E: ص م د B004, form-remote)` supplies cloth wrapped around a head and predicts body part, fabric, binder, and wrapping action.
- **Word ledger.** `O1=R ق و ل B002 tongue/body part; B001/B003–B016 tested`; `O2=ء ل ه B001–B002 0`; `O3=R ء ح د B001 one wrapped unit; B002–B006 tested`; `O4=ء ل ه B001–B002 0`; `O5=focus B004`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=R ك و ن B002 place/shelter; B001/B003–B006 0`; `O9=E ك ف ء B004 sewn tent panels; B001–B003/B005 tested`; `O10=ء ح د B001–B006 0`.
- **Construction ledger.** `X1=0`; `X2=0`; `X3=K nominal predicate, no wrapping action`; `X4=0`; `X5=0`; `X6=0`; `X7=0`; `X8=0`; `X9=0`; `X10=0`; `X11=0`; `X12=0`.
- **Forks and freeze.** Body fork `{ص م د B004, ق و ل B002}` combines head and tongue. Textile-enclosure fork `{ص م د B004, ك ف ء B004, ك و ن B002}` combines wrapped cloth, sewn shelter panels, and place. Predictions: head/person, fabric, sewing/wrapping, or shelter.
- **UNUSED_AT_FREEZE and test.** No rooted or unrooted word supplies those roles. `(K: ٱلصَّمَدُ is a predicate noun; كُفُوًا is equality predicate; يَكُن is copula)`. The branches share textile material but not a passage-local construction.
- **Grade: unlikely.** Pass 2 generates the missing textile image, then terminates it on morphology and role absence.

#### L031 — O5 × ص م د B005 — Attentive overseer, relied-upon guarantor

- **Initial image.** `(E: ص م د B005, form-remote)` supplies someone overseeing and caring about an affair.
- **Word ledger.** `O1=E ق و ل B015 sincere care + R B004 authority/B010 control; other B001–B003/B005–B014/B016 tested`; `O2=E ء ل ه B001 worshipped center + B002 name`; `O3=E ء ح د B001 sole overseer; B002–B006 tested`; `O4=E ء ل ه B001/B002 re-anchor`; `O5=focus B005 + E same-root B001 affairs/needs reliance`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=E ك و ن B003 guarantee/standing for; B001/B002/B004–B006 tested`; `O9=R ك ف ء B001 counterpart; B002–B005 tested`; `O10=R ء ح د B002 no counterpart; B001/B003–B006 tested`.
- **Construction ledger.** `X1=K no care construction`; `X2=E named center`; `X3=E predicate but K no affair complement`; `X4=E`; `X5=0`; `X6=0`; `X7=R beneficiary/counterpart`; `X8=0`; `X9=E one G`; `X10=0`; `X11=0`; `X12=0`.
- **Forks and freeze.** Care fork `{ص م د B005, ق و ل B015}`; authority fork adds `{ق و ل B004/B010}`; support fork adds `{ص م د B001, ك و ن B003, ء ل ه B001}` to produce a sole, relied-upon overseer who cares for and guarantees an affair/person. Predictions: affair, beneficiary, oversight act, care complement, or guarantee.
- **UNUSED_AT_FREEZE and test.** O9/O10 can deny a coequal but do not supply the missing affair. `(K: no syntactic affair/beneficiary; قُلْ not يقول بكذا; يَكُن not guarantee; الصمد predicated without complement)`.
- **Grade: weak.** Four remote branches converge into a complete support image, but no distinctive role is locally realized.

#### L032 — O5 × ص م د B006 — Blow with a stick against a hard target

- **Initial image.** `(E: ص م د B006, form-remote)` supplies striking someone/something with a stick.
- **Word ledger.** `O1=E ق و ل B008 stick implement; B001–B007/B009–B016 tested`; `O2=ء ل ه B001–B002 0`; `O3=R ء ح د B006 mountain target; B001–B005 tested`; `O4=ء ل ه B001–B002 0`; `O5=focus B006 + E same-root B002 hard rock`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=R ك و ن B002 place; B001/B003–B006 0`; `O9=E ك ف ء B002 overturning result; B001/B003–B005 tested`; `O10=R ء ح د B006 repeated target; B001–B005 tested`.
- **Construction ledger.** `X1=K speech`; `X2=K identity clause`; `X3=K predicate not strike event`; `X4=0`; `X5=0`; `X6=0`; `X7=0`; `X8=K equality syntax`; `X9=0`; `X10=R wrong-vocalized target recurrence`; `X11=0`; `X12=0`.
- **Forks and freeze.** `{ص م د B006, ق و ل B008}` supplies action+instrument; `{ص م د B002, ء ح د B006}` supplies rock/mountain target; `{ك ف ء B002}` supplies an overturned result. Predictions: striker, target, impact clause, motion.
- **UNUSED_AT_FREEZE and test.** Every required lexical role can be assembled remotely, but every local occurrence has incompatible form/syntax `(K: قُلْ speech; الصمد predicate; أَحَدٌ not أُحُد; كُفُوًا equality predicate)`. No striker exists.
- **Grade: unlikely.** A complete associative avalanche is not a passage synthesis when all role attachments fail.

#### L033 — O5 × ص م د B007 — Persistent center through successive negated states

- **Initial image.** `(E: ص م د B007, form-remote)` supplies duration/remain-through-severity.
- **Word ledger.** `O1=R ق و ل B015 sustained care + B001 utterance; other branches tested`; `O2=E ء ل ه B002 enduring G; B001 R worshipped center`; `O3=E ء ح د B001 stable unity; B002–B006 tested`; `O4=E ء ل ه B002 refreshed G`; `O5=focus B007`; `O6=C و ل د B003 no outgoing transition; B001/B002/B004–B006 tested`; `O7=C B003 no incoming transition; others tested`; `O8=C ك و ن B001 occurrence in time; B002–B006 tested`; `O9=C ك ف ء B001 no replacement/equal; B002–B005 tested`; `O10=C ء ح د B001/B002 stable-return/exhaustion; B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=E identity`; `X3=E predicate`; `X4=E persistence cue`; `X5=C successive denied states`; `X6=C transition cancellation`; `X7=C same G`; `X8=C no equal occurrence`; `X9=C stable referent`; `X10=C return`; `X11=C duration across ayahs`; `X12=0`.
- **Forks and freeze.** `{ص م د B007, ء ل ه B002, ء ح د B001, X4}` freezes as one identity persisting through sequence. Predictions: no origin/product transition or equal replacement; temporal grammar and referent continuity.
- **UNUSED_AT_FREEZE and test.** X5, O6/O7, O8 B001, and X9 fit persistence. `(K: cold, barrenness, camel, and hardship dimensions are absent; repeated لَمْ does not by itself license unlimited eternity)`.
- **Grade: medium.** A restrained persistence model is supported, but the branch's concrete severity scene is unused.

### 5.6 O6 — 112:3:2 يَلِدْ — و ل د, active occurrence

#### L034 — O6 × و ل د B001 — Outgoing offspring slot denied

- **Initial image.** `(E: و ل د B001)` supplies an offspring/product role; active يَلِدْ would direct that role outward from continuing G, while لَمْ cancels it.
- **Word ledger.** `O1=C ق و ل B001 frame; B002–B016 tested`; `O2=C ء ل ه B002 G; B001 tested`; `O3=C ء ح د B001 protected unity; B002–B006 tested`; `O4=C ء ل ه B002 re-anchor; B001 tested`; `O5=C ص م د B001 center; B002 R compact core; B003–B007 tested`; `O6=focus B001 + E active negation`; `O7=C و ل د B001 subject-not-offspring + B003 inverse event; B002/B004–B006 tested`; `O8=C ك و ن B001 final negation; B002–B006 tested`; `O9=C ك ف ء B001 no peer; B002–B005 tested`; `O10=C ء ح د B002/B001 no candidate/return; B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=C unity`; `X3=C center`; `X4=C same G`; `X5=E first of three negatives`; `X6=C inverse completion`; `X7=C comparison`; `X8=C generalization`; `X9=C same subject`; `X10=C`; `X11=C specific→general`; `X12=0`.
- **Forks and freeze.** `{و ل د B001 at O6, active voice, لَمْ}` freezes as `no OFFSPRING(G,x)`. Physical-core rival imports ص م د B002 and imagines no output from a sealed center. Predictions: inverse no-origin role, protected unity, and no parallel peer.
- **UNUSED_AT_FREEZE and test.** O7 supplies inverse participant placement, O3/O5 backward-corroborate one center, O9/O10 generalize to no equal. `(K: no overt child is elided; the event is negated; K: “output” is secondary geometry, not birth's replacement meaning)`.
- **Grade: strong.** Exact active morphology opens one role orientation and the next occurrence independently reverses it.

#### L035 — O6 × و ل د B002 — Parent role denied, then parent-source above denied

- **Initial image.** `(E: و ل د B002, branch-remote from verb)` supplies parent roles; active negated birth denies G the event that would make it a parent.
- **Word ledger.** `O1=ق و ل B001–B016 tested, B016 R`; `O2=C ء ل ه B002 G; B001 tested`; `O3=C ء ح د B001; B002–B006 tested`; `O4=C ء ل ه B002`; `O5=C ص م د B001 no superior center; B002–B007 tested`; `O6=focus B002 + E active negation`; `O7=C و ل د B002 parent-source implication + B003 passive event; B001/B004–B006 tested`; `O8=C ك و ن B001; B002–B006 tested`; `O9=C ك ف ء B001 peer; B002–B005 tested`; `O10=C ء ح د B002/B001; B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=C`; `X3=C`; `X4=C`; `X5=E/C`; `X6=C parent/child orientation`; `X7=C`; `X8=C`; `X9=C`; `X10=C`; `X11=C`; `X12=0`.
- **Forks and freeze.** `{و ل د B002, active negated event}` freezes as “G does not enter the parent role.” Prediction: passive inverse should deny a parent-source above G; no peer class beside G.
- **UNUSED_AT_FREEZE and test.** O7 passive fulfills the above-G prediction; O9 excludes the beside-G role. `(K: الوالد/الوالدة nouns, sex, and duality are absent; B003 is the exact event branch)`.
- **Grade: medium-strong.** Role implication and inverse completion are precise, though the focus branch is not the surface verbal sense.

#### L036 — O6 × و ل د B003 — Active event predicts its passive inverse

- **Initial image.** `(E: و ل د B003)` is the exact birth-event dossier; `(E: active imperfect jussive under لَمْ)` cancels an event sourced at G.
- **Word ledger.** `O1=C ق و ل B001 frame; B002–B016 tested`; `O2=C ء ل ه B002 G; B001 tested`; `O3=C ء ح د B001; B002–B006 tested`; `O4=C ء ل ه B002`; `O5=C ص م د B001; B002–B007 tested`; `O6=focus B003`; `O7=C و ل د B003 exact root passive inverse; B001/B002 role implications, B004–B006 tested`; `O8=C ك و ن B001; B002–B006 tested`; `O9=C ك ف ء B001; B002–B005 tested`; `O10=C ء ح د B002/B001; B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=C`; `X3=C`; `X4=C`; `X5=E negative field`; `X6=C exact coordination/voice reversal`; `X7=C`; `X8=C`; `X9=C 3MS`; `X10=C`; `X11=C widening`; `X12=C shared coda with O7`.
- **Forks and freeze.** `{و ل د B003 at O6, active voice, لَمْ}` freezes as a canceled outward birth event. Predictions: same root may recur in inverse voice; then a broader relation than lineage may be denied.
- **UNUSED_AT_FREEZE and test.** O7/X6 exactly supplies passive inverse; O9/X7–X8 broadens to equality; O10 exhausts candidates and reactivates O3. `(K: no pregnancy/delivery details; only event relation is recruited)`.
- **Grade: strong.** Root recurrence, conjunction, polarity, and voice deliver exact prospective completion.

#### L037 — O6 × و ل د B004 — Young child/servant participant never appears

- **Initial image.** `(E: و ل د B004, form-remote)` predicts a newborn/young boy or girl, or servant, as an explicit participant.
- **Word ledger.** `O1=ق و ل B001–B016 0`; `O2=ء ل ه B001–B002 0`; `O3=ء ح د B001–B006 0`; `O4=ء ل ه B001–B002 0`; `O5=ص م د B001–B007 0`; `O6=focus B004`; `O7=R و ل د B004 subject-as-newborn possibility + B003 event; B001/B002/B005–B006 tested`; `O8=R ك و ن B001 state in time; B002–B006 0`; `O9=ك ف ء B001–B005 0`; `O10=ء ح د B001–B006 0`.
- **Construction ledger.** `X1=0`; `X2=0`; `X3=0`; `X4=0`; `X5=K negated event instantiates no child`; `X6=R lifecycle reversal`; `X7=0`; `X8=0`; `X9=0`; `X10=0`; `X11=R lifecycle sequence`; `X12=0`.
- **Forks and freeze.** O6 seed predicts an absent young offspring; O7 generates a lifecycle fork in which G would itself enter newborn state. Predictions: child noun, youth/age, servant/ownership, or development stages.
- **UNUSED_AT_FREEZE and test.** No participant or age/ownership relation occurs. `(K: O6/O7 are negated verbs, not الوليد/الوليدة; K: no child object is realized)`.
- **Grade: unlikely.** Even the active→passive lifecycle fork lacks every distinctive B004 cue.

#### L038 — O6 × و ل د B005 — No downstream derivative, then no upstream derivation

- **Initial image.** `(E: و ل د B005, form-remote abstraction)` turns birth into one thing arising causally from another; active negation blocks a derivative from G.
- **Word ledger.** `O1=R ق و ل B016 definition and B014 profile; others tested`; `O2=C ء ل ه B002 G; B001 tested`; `O3=C ء ح د B001 one node; B002–B006 tested`; `O4=C ء ل ه B002`; `O5=C ص م د B001 dependence directed to G + R B002 sealed core; B003–B007 tested`; `O6=focus B005 + E active negation`; `O7=C و ل د B005 inverse derivation + B003 passive event; B001/B002/B004/B006 tested`; `O8=C ك و ن B001; B002–B006 tested`; `O9=C ك ف ء B001 no parallel derivative/equal; B002–B005 tested`; `O10=C ء ح د B002/B001; B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=C`; `X3=C`; `X4=C`; `X5=E/C`; `X6=C inverse causal direction`; `X7=C`; `X8=C`; `X9=C`; `X10=C`; `X11=C source/product→peer`; `X12=0`.
- **Forks and freeze.** `{و ل د B005, active negation}` freezes as `no DERIVE(G,x)`. ص م د B001 supplies a rival dependence topology; B002 supplies a sealed-source image. Predictions: no derivation of G from x and no parallel copy/equal.
- **UNUSED_AT_FREEZE and test.** O7 supplies inverse derivation, O5 B001 points dependence toward G, O9 denies parallel equivalence. `(K: B005 is abstract and cannot replace local birth; B003/voice remains primary)`.
- **Grade: medium-strong.** The abstraction predicts two unused relational completions but remains morphologically secondary.

#### L039 — O6 × و ل د B006 — Birth-cohort peer and the no-equal closure

- **Initial image.** `(E: و ل د B006, form-remote)` supplies a same-age peer and predicts birth-time/cohort plus equality.
- **Word ledger.** `O1=ق و ل B001–B016 0`; `O2=E ء ل ه B002 focal G; B001 0`; `O3=R ء ح د B001 lone member; B002–B006 tested`; `O4=C ء ل ه B002`; `O5=R ص م د B007 duration/age + B001 center; B002–B006 tested`; `O6=focus B006`; `O7=R و ل د B006 same cohort + B003 passive birth; B001–B005 tested`; `O8=R ك و ن B001 time occurrence; B002–B006 0`; `O9=E ك ف ء B001 peer/equality; B002–B005 tested`; `O10=C ء ح د B002 no peer candidate; B001/B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=R lone member`; `X3=0`; `X4=0`; `X5=C no candidate`; `X6=E cohort formation denied`; `X7=E peer-to-G`; `X8=C empty peer slot`; `X9=0`; `X10=C`; `X11=C birth→peer`; `X12=0`.
- **Forks and freeze.** `{و ل د B006, ك ف ء B001}` creates a coeval-equal class; O6/O7 jointly deny entry into a birth cohort. `{ص م د B007, ك و ن B001}` adds time/duration. Predictions: age, birth-time, cohort member, or لِدَة form.
- **UNUSED_AT_FREEZE and test.** Final equality denial and أَحَدٌ empty the peer slot, but no age criterion appears. `(K: surface forms are birth verbs, not لِدَة; كُفُوًا is general equality)`.
- **Grade: weak.** Peer/equal convergence is specific, but B006's defining same-age dimension is unsupported.

### 5.7 O7 — 112:3:4 يُولَدْ — و ل د, passive occurrence

#### L040 — O7 × و ل د B001 — G is not an offspring; backward replay finds the inverse

- **Initial image.** `(E: و ل د B001)` supplies the offspring role; passive يُولَدْ would place G in it, while repeated لَمْ cancels that placement.
- **Word ledger.** `O1=C ق و ل B001 frame; B002–B016 tested`; `O2=C ء ل ه B002 G; B001 tested`; `O3=C ء ح د B001 unity; B002–B006 tested`; `O4=C ء ل ه B002 re-anchor`; `O5=C ص م د B001 center + R B002 compact core; B003–B007 tested`; `O6=C و ل د B001 outgoing offspring + B003 active inverse; B002/B004–B006 tested`; `O7=focus B001 + E passive negation`; `O8=C ك و ن B001; B002–B006 tested`; `O9=C ك ف ء B001; B002–B005 tested`; `O10=C ء ح د B002/B001; B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=C`; `X3=C`; `X4=C`; `X5=E repeated negation`; `X6=C backward inverse`; `X7=C`; `X8=C`; `X9=C same G`; `X10=C`; `X11=C`; `X12=C O7 coda`.
- **Forks and freeze.** `{و ل د B001 at O7, passive voice, لَمْ}` freezes as `G is no offspring / no incoming lineage edge`. Predictions: backward replay should reveal the outgoing inverse; later comparison should remove a parallel peer.
- **UNUSED_AT_FREEZE and test.** O6/X6 supplies exact inverse; O9/O10 supplies no peer and exhaustive closure; O3/O5 become newly relevant as the isolated one center. `(K: no overt parent should be invented; event is negated)`.
- **Grade: strong.** The late seed reorganizes the immediately earlier clause and then predicts the broader final relation.

#### L041 — O7 × و ل د B002 — No parent-source above G

- **Initial image.** `(E: و ل د B002, branch-remote)` supplies parents as the source role implicit in a birth event; passive negation denies such an event for G.
- **Word ledger.** `O1=ق و ل B001–B016 tested`; `O2=C ء ل ه B002 G; B001 tested`; `O3=C ء ح د B001; B002–B006 tested`; `O4=C ء ل ه B002`; `O5=C ص م د B001 dependence endpoint; B002–B007 tested`; `O6=C و ل د B002 G-not-parent + B003 active event; B001/B004–B006 tested`; `O7=focus B002`; `O8=C ك و ن B001; B002–B006 tested`; `O9=C ك ف ء B001; B002–B005 tested`; `O10=C ء ح د B002/B001; B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=C`; `X3=C`; `X4=C`; `X5=E/C`; `X6=C parent/child reversal`; `X7=C`; `X8=C`; `X9=C`; `X10=C`; `X11=C`; `X12=0`.
- **Forks and freeze.** `{و ل د B002, passive negation}` freezes as “no parent-source above G.” Predictions: prior clause denies child below; final clause denies peer beside.
- **UNUSED_AT_FREEZE and test.** O6 and O9 fulfill below/beside roles; O5 B001 independently points reliance toward G rather than to a superior source. `(K: parent nouns, duality, and sex are absent; B003 is exact event branch)`.
- **Grade: medium-strong.** Three-direction role completion is strong, with a branch-to-form distance penalty.

#### L042 — O7 × و ل د B003 — Passive inverse completes bidirectional isolation

- **Initial image.** `(E: و ل د B003)` is exact birth-event content; passive voice positions G as born participant and لَمْ cancels the incoming event.
- **Word ledger.** `O1=C ق و ل B001; B002–B016 tested`; `O2=C ء ل ه B002; B001 tested`; `O3=C ء ح د B001; B002–B006 tested`; `O4=C ء ل ه B002`; `O5=C ص م د B001; B002–B007 tested`; `O6=C و ل د B003 exact active inverse + B001/B002 implications; B004–B006 tested`; `O7=focus B003`; `O8=C ك و ن B001; B002–B006 tested`; `O9=C ك ف ء B001; B002–B005 tested`; `O10=C ء ح د B002/B001; B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=C`; `X3=C`; `X4=C`; `X5=E negative field`; `X6=C exact backward inversion`; `X7=C`; `X8=C generalization`; `X9=C`; `X10=C`; `X11=C`; `X12=C coda`.
- **Forks and freeze.** `{و ل د B003 at O7, passive voice, repeated لَمْ}` freezes as canceled incoming birth. Predictions: preceding coordinated token is same-root active inverse; final clause widens from lineage to equality.
- **UNUSED_AT_FREEZE and test.** O6/X6 exactly fulfills inverse; O9/X8 supplies generalization; O10 reactivates O3. `(K: no childbirth physiology is recruited)`.
- **Grade: strong.** This seed causes precise backward reorganization and prospective completion.

#### L043 — O7 × و ل د B004 — Denied newborn/lifecycle state

- **Initial image.** `(E: و ل د B004, form-remote)` imagines G as newborn/young/servant, a state denied by the passive clause.
- **Word ledger.** `O1=ق و ل B001–B016 0`; `O2=ء ل ه B001–B002 0`; `O3=ء ح د B001–B006 0`; `O4=ء ل ه B001–B002 0`; `O5=R ص م د B007 endurance/age; B001–B006 0`; `O6=R و ل د B004 offspring youth + B003 active event; B001/B002/B005–B006 tested`; `O7=focus B004`; `O8=R ك و ن B001 state in time + B005 old-man branch; B002–B004/B006 tested`; `O9=ك ف ء B001–B005 0`; `O10=ء ح د B001–B006 0`.
- **Construction ledger.** `X1=0`; `X2=0`; `X3=0`; `X4=0`; `X5=K event negated`; `X6=R lifecycle endpoints`; `X7=0`; `X8=R temporal state`; `X9=0`; `X10=0`; `X11=R young→old lifecycle`; `X12=0`.
- **Forks and freeze.** Lifecycle fork `{و ل د B004 at O6/O7, ص م د B007, ك و ن B001/B005}` ranges from birth/young state to endurance and old-age reminiscence. Predictions: age markers, infancy, youth, old age, servant/ownership, or first-person كُنْتُ.
- **UNUSED_AT_FREEZE and test.** `(K: O6/O7 are verbs, not الوليد; K: O8 is 3MS يَكُن, not كُنْتِيّ/كُنْتُ; no age or ownership)`.
- **Grade: unlikely.** Pass 2 preserves the full lifecycle image, but every distinctive form is absent.

#### L044 — O7 × و ل د B005 — G has no upstream derivation

- **Initial image.** `(E: و ل د B005, form-remote abstraction)` treats passive birth as derivation of G from another; negation removes that source relation.
- **Word ledger.** `O1=R ق و ل B016/B014 profile; others tested`; `O2=C ء ل ه B002 G; B001 tested`; `O3=C ء ح د B001; B002–B006 tested`; `O4=C ء ل ه B002`; `O5=C ص م د B001 endpoint + R B002 sealed core; B003–B007 tested`; `O6=C و ل د B005 no downstream derivation + B003 active; B001/B002/B004/B006 tested`; `O7=focus B005`; `O8=C ك و ن B001; B002–B006 tested`; `O9=C ك ف ء B001; B002–B005 tested`; `O10=C ء ح د B002/B001; B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=C`; `X3=C`; `X4=C`; `X5=E/C`; `X6=C inverse derivation`; `X7=C`; `X8=C`; `X9=C`; `X10=C`; `X11=C`; `X12=0`.
- **Forks and freeze.** `{و ل د B005, passive negation}` freezes as `no DERIVE(x,G)`. Predictions: backward active clause supplies `no DERIVE(G,x)`; dependence converges toward G; no parallel copy.
- **UNUSED_AT_FREEZE and test.** O6, O5 B001, and O9 fulfill all three. `(K: generic derivation stays secondary to exact birth event and voice)`.
- **Grade: medium-strong.** Independent backward and forward relations complete the abstraction, despite morphological distance.

#### L045 — O7 × و ل د B006 — No coeval peer class

- **Initial image.** `(E: و ل د B006, form-remote)` supplies same-age peerhood; passive birth would locate G in a cohort, but the event is denied.
- **Word ledger.** `O1=ق و ل B001–B016 0`; `O2=E ء ل ه B002 G; B001 0`; `O3=R ء ح د B001 lone; B002–B006 tested`; `O4=C ء ل ه B002`; `O5=R ص م د B007 duration + B001 center; B002–B006 tested`; `O6=R و ل د B006 peer cohort + B003 active; B001–B005 tested`; `O7=focus B006`; `O8=R ك و ن B001 time; B002–B006 0`; `O9=E ك ف ء B001 equality; B002–B005 tested`; `O10=C ء ح د B002 empty peer class; B001/B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=R lone`; `X3=0`; `X4=0`; `X5=C`; `X6=E denied cohort`; `X7=E peer relation`; `X8=C no filler`; `X9=0`; `X10=C`; `X11=C`; `X12=0`.
- **Forks and freeze.** `{و ل د B006, ك ف ء B001, ك و ن B001, ص م د B007}` creates coeval peerhood across time, then final negation empties the peer class. Predictions: explicit age/birth-time criterion.
- **UNUSED_AT_FREEZE and test.** General equality and negative scope corroborate only peerhood, not coevality. `(K: no لِدَة form, age, or cohort; surface is passive birth event)`.
- **Grade: weak.** A complete peer-time image forms, but its defining criterion never receives independent support.

### 5.8 O8 — 112:4:2 يَكُن — ك و ن

#### L046 — O8 × ك و ن B001 — No occurrence admits an equivalent candidate

- **Initial image.** `(E: ك و ن B001)` is contextually exact for predicational كان/occurrence in time; under لَمْ it opens a denied state whose predicate and subject follow.
- **Word ledger.** `O1=C ق و ل B001 frame; B002–B016 tested, B016 R`; `O2=C ء ل ه B002 G; B001 tested`; `O3=C ء ح د B001 positive unity; B002–B006 tested`; `O4=C ء ل ه B002 re-anchor`; `O5=C ص م د B001 center; B002/B007 rivals, B003–B006 tested`; `O6=C و ل د B003 active exclusion; B001/B002/B004–B006 tested`; `O7=C B003 passive exclusion; others tested`; `O8=focus B001`; `O9=E ك ف ء B001 denied predicate; B002–B005 tested`; `O10=E ء ح د B002 delayed candidate + C B001 recurrence; B003–B006 tested`.
- **Construction ledger.** `X1=C`; `X2=C`; `X3=C`; `X4=C`; `X5=E third negative`; `X6=C narrower exclusions`; `X7=E comparison target`; `X8=E kana predicate+subject`; `X9=C same G`; `X10=C reactivation`; `X11=C closure`; `X12=C weak coda`.
- **Forks and freeze.** `{ك و ن B001, لَمْ, ك ف ء B001, ء ح د B002, X7–X8}` freezes as “no occurrence/state has any candidate equivalent to G.” Predictions: earlier clauses should define why candidates fail; final word should reconnect to opening unity and close the open subject slot.
- **UNUSED_AT_FREEZE and test.** O3/O5/O6/O7 and X10 retrospectively supply unity, one-center relation, and two lineage exclusions. The passage ends exactly when O10 fills delayed subject. `(K: no unsupported timeless metaphysics; claim stays within grammatical temporal force)`.
- **Grade: strong.** Exact branch, polarity, attachments, delayed role, and backward replay converge.

#### L047 — O8 × ك و ن B002 — Unmatched place, elevation, or rank

- **Initial image.** `(E: ك و ن B002, form-remote)` supplies place, position, station, or rank.
- **Word ledger.** `O1=R ق و ل B004 authority/B016 definition; other branches tested`; `O2=E ء ل ه B002 bearer + B001 rank-center`; `O3=E ء ح د B001 unique station; B002–B006 tested`; `O4=E ء ل ه B002 re-anchor`; `O5=E ص م د B002 hard/elevated place + R B001 relied-upon station; B003–B007 tested`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=focus B002`; `O9=E ك ف ء B001 equal rank/place; B002–B005 tested`; `O10=C ء ح د B002 no equal + B001 unique; B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=E unique bearer`; `X3=E elevated/relied predicate fork`; `X4=E`; `X5=C no equal state`; `X6=0`; `X7=E comparison`; `X8=K copular syntax but C unmatched rank geometry`; `X9=C`; `X10=C`; `X11=C`; `X12=0`.
- **Forks and freeze.** Place fork `{ك و ن B002, ص م د B002}`: a singular hard/elevated place. Rank fork `{ك و ن B002, ء ح د B001, ص م د B001, ك ف ء B001}`: one relied-upon station with no equal rank. Predictions: locative, elevation, rank scale, or مكان/مكانة form.
- **UNUSED_AT_FREEZE and test.** O9/O10 complete unequal rank, but X8 shows يَكُن is a copula whose predicate is كُفُوًا, not مكان/مكانة. `(K: لَّهُۥ is comparison complement, not location; no place phrase)`. The elevated-place fork is additionally physical and unattached.
- **Grade: weak.** “Unmatched station” is coherent secondary geometry, but B002's local morphology and locative roles are absent.

#### L048 — O8 × ك و ن B003 — Guarantor and relied-upon overseer

- **Initial image.** `(E: ك و ن B003, form-remote)` supplies guaranteeing, supporting, or standing for someone and predicts guarantor-beneficiary roles.
- **Word ledger.** `O1=E ق و ل B015 care + R B004 authority/B010 control; other branches tested`; `O2=E ء ل ه B001 worshipped center + B002 name`; `O3=E ء ح د B001 sole guarantor; B002–B006 tested`; `O4=E ء ل ه B001/B002`; `O5=E ص م د B001 reliance + B005 oversight/care; B002–B004/B006–B007 tested`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=focus B003`; `O9=R ك ف ء B001 counterpart; B002–B005 0`; `O10=R ء ح د B002 no counterpart; B001/B003–B006 0`.
- **Construction ledger.** `X1=K no guarantee statement`; `X2=E named guarantor fork`; `X3=E reliance/oversight`; `X4=E`; `X5=0`; `X6=0`; `X7=R beneficiary/comparison but wrong relation`; `X8=K copula`; `X9=E one G`; `X10=0`; `X11=0`; `X12=0`.
- **Forks and freeze.** `{ك و ن B003, ص م د B001/B005, ق و ل B015, ء ل ه B001, ء ح د B001}` yields a sole relied-upon overseer who cares for and guarantees a beneficiary. Authority branches B004/B010 make a rival controlling guarantor. Predictions: beneficiary, undertaking, care/affair, or guarantee construction.
- **UNUSED_AT_FREEZE and test.** No beneficiary or undertaking appears; O9 is equality to G, not someone guaranteed by G. `(K: يَكُن is negated copula; no B003 form; no affair/complement)`.
- **Grade: weak.** A rich support image converges across roots but fails all local role attachments.

#### L049 — O8 × ك و ن B004 — Submission toward a worshipped center

- **Initial image.** `(E: ك و ن B004, form-remote)` supplies submission/استكانة and predicts a submitting participant and authority/object.
- **Word ledger.** `O1=R ق و ل B010 control/B004 authority; others tested`; `O2=E ء ل ه B001 worshipped object + B002 name`; `O3=E ء ح د B001 sole object; B002–B006 tested`; `O4=E ء ل ه B001/B002`; `O5=E ص م د B001 direction toward relied-upon center; B002–B007 tested`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=focus B004`; `O9=R ك ف ء B001 opposition/peer; B002–B005 tested`; `O10=R ء ح د B002 no opponent; B001/B003–B006 tested`.
- **Construction ledger.** `X1=R directive but no submitter`; `X2=E center`; `X3=E direction`; `X4=E`; `X5=0`; `X6=0`; `X7=0`; `X8=K copula not استكانة`; `X9=K G is referent, no second participant`; `X10=0`; `X11=0`; `X12=0`.
- **Forks and freeze.** `{ك و ن B004, ء ل ه B001, ص م د B001}` forms a submitter oriented toward a worshipped/reliance center; authority branches add governing force. Predictions: submitter, submission act, authority complement.
- **UNUSED_AT_FREEZE and test.** No participant fills submitter; the only 3MS chain is G itself. `(K: يَكُن is copular; no استكانة morphology; imperative addressee is speaker, not grammatically a submitter)`.
- **Grade: weak.** Directional roles align remotely, but the seed's action and participant are absent.

#### L050 — O8 × ك و ن B005 — Birth-to-old-age lifecycle reminiscence

- **Initial image.** `(E: ك و ن B005, form-remote)` supplies the old man called كُنْتِيّ through retrospective كُنْتُ في شبابي.
- **Word ledger.** `O1=R ق و ل B012 inward memory/B006 appropriation; others tested`; `O2=ء ل ه B001–B002 0`; `O3=ء ح د B001–B006 0`; `O4=ء ل ه B001–B002 0`; `O5=R ص م د B007 endurance over time; B001–B006 0`; `O6=E و ل د B004 youth/newborn + B003 birth; B001/B002/B005–B006 tested`; `O7=E B004 subject-born + B003 event; others tested`; `O8=focus B005`; `O9=ك ف ء B001–B005 0`; `O10=ء ح د B001–B006 0`.
- **Construction ledger.** `X1=R recollection spoken but no first person`; `X2=0`; `X3=0`; `X4=0`; `X5=R negated life events`; `X6=E lifecycle beginning`; `X7=0`; `X8=K 3MS يَكُن not كُنْتُ`; `X9=K stable G, not aging narrator`; `X10=0`; `X11=R temporal span`; `X12=0`.
- **Forks and freeze.** `{ك و ن B005, و ل د B003/B004, ص م د B007, ق و ل B012}` creates a birth→youth→endurance→old-age recollection. Predictions: aged man, youth, first-person كُنْتُ, memory, or life stages.
- **UNUSED_AT_FREEZE and test.** `(K: O8 is third-person يَكُن under negation; no age, first person, memory, or old man; birth events are denied)`.
- **Grade: unlikely.** The lifecycle image is complete but entirely branch-remote.

#### L051 — O8 × ك و ن B006 — Bad-state branch defeated by the actual predicate

- **Initial image.** `(E: ك و ن B006, form-remote)` predicts someone in a bad condition.
- **Word ledger.** `O1=R ق و ل B005 false saying/B011 conjecture; other branches tested`; `O2=ء ل ه B001–B002 0`; `O3=ء ح د B001–B006 0`; `O4=ء ل ه B001–B002 0`; `O5=R ص م د B007 hardship; B001–B006 0`; `O6=R و ل د B003 negated event; B001/B002/B004–B006 0`; `O7=R B003 negated event; others 0`; `O8=focus B006`; `O9=K ك ف ء B001 actual equality predicate; B002–B005 0`; `O10=K ء ح د B002 actual subject scope; B001/B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=0`; `X3=0`; `X4=0`; `X5=R negative polarity but K not badness`; `X6=0`; `X7=0`; `X8=K predicate is كُفُوًا`; `X9=0`; `X10=0`; `X11=0`; `X12=0`.
- **Forks and freeze.** `{ك و ن B006, ص م د B007}` forms a bad/hard state; repeated negation could deny such a state. Prediction: سوء or a bad-state complement.
- **UNUSED_AT_FREEZE and test.** X8 explicitly identifies the complement as equality, not badness. `(K: negative polarity cannot create B006 lexical content; no سوء/state noun)`.
- **Grade: unlikely.** The full clause structure directly defeats the branch.

### 5.9 O9 — 112:4:4 كُفُوًا — ك ف ء

#### L052 — O9 × ك ف ء B001 — Empty counterpart slot reactivates the whole profile

- **Initial image.** `(E: ك ف ء B001)` is exact equality/counterpart content; X7 makes G the comparison target and X8 leaves a delayed candidate subject.
- **Word ledger.** `O1=C ق و ل B001 frame; B002–B016 tested, B016 R`; `O2=C ء ل ه B002 G; B001 tested`; `O3=C ء ح د B001 first criterion; B002–B006 tested`; `O4=C ء ل ه B002 re-anchor`; `O5=C ص م د B001 second criterion; B002/B007 rivals, B003–B006 tested`; `O6=C و ل د B003 first class exclusion; B001/B002/B004–B006 tested`; `O7=C B003 inverse class exclusion; others tested`; `O8=E ك و ن B001 negated occurrence; B002–B006 tested`; `O9=focus B001`; `O10=E ء ح د B002 candidate exhaustor + C B001 recurrence; B003–B006 tested`.
- **Construction ledger.** `X1=C`; `X2=C`; `X3=C`; `X4=C`; `X5=E negative scope`; `X6=C narrower candidate classes`; `X7=E relation-to-G`; `X8=E delayed subject`; `X9=C same G`; `X10=C profile return`; `X11=C generalizing closure`; `X12=C exact coda return`.
- **Forks and freeze.** `{ك ف ء B001, ك و ن B001, لَمْ, X7–X8, ء ح د B002}` freezes as an empty “equivalent-to-G” slot. Predictions: earlier predicates become comparison criteria; birth clauses remove narrower candidate sources; O10 repeats opening property and closes.
- **UNUSED_AT_FREEZE and test.** O3/O5 supply criteria, O6/O7 remove lineage routes, X9 fixes G, X10 returns unity. `(K: restrict B001 to counterpart/equality; do not import marriage, war, recompense, or alternating arrangement)`.
- **Grade: strong.** This late cue reorganizes every earlier layer and predicts the exact stopping word.

#### L053 — O9 × ك ف ء B002 — Role-arrow reversal visualized as tilting/overturning

- **Initial image.** `(E: ك ف ء B002, form-remote)` supplies tilting, overturning, redirecting, swaying, or changed appearance.
- **Word ledger.** `O1=R ق و ل B008 striking implement; B001–B007/B009–B016 tested`; `O2=ء ل ه B001–B002 0`; `O3=R ء ح د B006 mountain; B001–B005 tested`; `O4=ء ل ه B001–B002 0`; `O5=R ص م د B006 blow + B002 hard target; B001/B003–B005/B007 tested`; `O6=E و ل د B003 active direction; B001/B002/B004–B006 tested`; `O7=E B003 passive reversal; others tested`; `O8=R ك و ن B001 state change; B002–B006 tested`; `O9=focus B002`; `O10=ء ح د B001–B006 0`.
- **Construction ledger.** `X1=0`; `X2=0`; `X3=0`; `X4=0`; `X5=0`; `X6=E arrow reversal metaphor`; `X7=K comparison attachment`; `X8=K equality predicate morphology`; `X9=0`; `X10=0`; `X11=R directional sequence`; `X12=0`.
- **Forks and freeze.** Relational-motion fork `{ك ف ء B002, و ل د B003 active/passive}` visualizes the birth arrow being turned around. Impact fork `{ق و ل B008, ص م د B006/B002, ء ح د B006, ك ف ء B002}` ends in an overturned hard target. Predictions: actual moved object, path, direction, physical result.
- **UNUSED_AT_FREEZE and test.** X6 confirms grammatical reversal, not B002 motion. X7/X8 decisively make O9 an equality noun. `(K: no moved patient or path; role-arrow visualization is not lexical corroboration)`.
- **Grade: weak.** A useful secondary motion analogy exists, but local syntax selects B001.

#### L054 — O9 × ك ف ء B003 — Coda variation that returns to exact أَحَد

- **Initial image.** `(E: ك ف ء B003, form-remote)` supplies technical rhyme disagreement in letters, vowels, or case.
- **Word ledger.** `O1=R ق و ل B001 uttered sequence + B016 bounded form; other branches tested`; `O2=ء ل ه B001–B002 0`; `O3=E ء ح د B001 first ending; B002–B006 tested`; `O4=ء ل ه B001–B002 0`; `O5=E ص م د B001–B007 all read, sound form selected nonlexically`; `O6=و ل د B001–B006 0`; `O7=E و ل د B003 word ending, lexical branch not rhyme`; `O8=ك و ن B001–B006 0`; `O9=focus B003`; `O10=E ء ح د B001/B002 exact ending return; B003–B006 tested`.
- **Construction ledger.** `X1=R recited content`; `X2=0`; `X3=0`; `X4=0`; `X5=0`; `X6=0`; `X7=K comparison syntax`; `X8=K equality predicate`; `X9=0`; `X10=E exact return`; `X11=R bounded lines`; `X12=E coda-variation image`.
- **Forks and freeze.** `{ك ف ء B003, X12, O3/O5/O7/O10 ending forms}` yields a coda sequence أَحَد / صَمَد / يُولَد / أَحَد: variation between endpoints followed by exact return. Prediction: explicit poetry/rhyme frame or local form of الإكفاء; terminal return should align with semantic completion.
- **UNUSED_AT_FREEZE and test.** X10/X8 independently align exact sound return with predicate→subject reactivation, making the *acoustic trajectory* coherent. But `(K: كُفُوًا is an equality predicate, not rhyme terminology; no الشعر/قافية frame)`. B003 does not generate X12's validity.
- **Grade: weak.** A real acoustic image is recovered, yet the lexical seed remains locally defeated.

#### L055 — O9 × ك ف ء B004 — Sewn shelter panels and wrapped enclosure

- **Initial image.** `(E: ك ف ء B004, form-remote)` supplies one/two sewn panels forming the rear of a tent/house.
- **Word ledger.** `O1=R ق و ل B002 tongue/body; other branches tested`; `O2=ء ل ه B001–B002 0`; `O3=R ء ح د B001 one enclosure; B002–B006 tested`; `O4=ء ل ه B001–B002 0`; `O5=E ص م د B004 cloth wrap + B003 closure + B002 compact enclosure; B001/B005–B007 tested`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=E ك و ن B002 place/shelter; B001/B003–B006 tested`; `O9=focus B004`; `O10=ء ح د B001–B006 0`.
- **Construction ledger.** `X1=0`; `X2=0`; `X3=K predicate not cloth`; `X4=0`; `X5=0`; `X6=0`; `X7=K comparison complement`; `X8=K equality predicate`; `X9=0`; `X10=0`; `X11=0`; `X12=0`.
- **Forks and freeze.** `{ك ف ء B004, ص م د B004/B003/B002, ك و ن B002, ء ح د B001}` creates a one-piece textile enclosure: sewn shelter panels, wrapping, closure, and place. Body fork adds ق و ل B002. Predictions: tent/house, cloth, sewing, rear orientation, or wrapping.
- **UNUSED_AT_FREEZE and test.** None occurs. `(K: كُفُوًا is accusative kana-predicate governing لَّهُۥ; الصمد is nominative predicate; يَكُن copular)`.
- **Grade: unlikely.** The full textile-enclosure fork is explicit but unattached to every local form.

#### L056 — O9 × ك ف ء B005 — Alternating annual production and birth cycle

- **Initial image.** `(E: ك ف ء B005, form-remote)` supplies annual yield/offspring or two groups alternating production.
- **Word ledger.** `O1=ق و ل B001–B016 0`; `O2=ء ل ه B001–B002 0`; `O3=R ء ح د B003 count/group + B005 individuals; other branches tested`; `O4=ء ل ه B001–B002 0`; `O5=E ص م د B007 duration through hardship; B001–B006 tested`; `O6=E و ل د B001 offspring + B003 production event; B002/B004–B006 tested`; `O7=E B001/B003 reversed production position; B002/B004–B006 tested`; `O8=E ك و ن B001 time occurrence; B002–B006 tested`; `O9=focus B005`; `O10=R ء ح د B002 no group/candidate; B001/B003–B006 tested`.
- **Construction ledger.** `X1=0`; `X2=0`; `X3=0`; `X4=0`; `X5=R repeated cycle but negated`; `X6=E alternating active/passive positions`; `X7=K comparison relation`; `X8=K equality predicate`; `X9=0`; `X10=0`; `X11=R annual/ordered cycle`; `X12=0`.
- **Forks and freeze.** `{ك ف ء B005, و ل د B001/B003, ص م د B007, ك و ن B001, X6}` creates alternating production through time: two orientations/groups yielding offspring in turns. Predictions: year, herd/palm, milk/wool/fruit, two groups, repeated output.
- **UNUSED_AT_FREEZE and test.** Active/passive is a grammatical inversion, not two productive groups, and both events are negated. `(K: no year, agriculture, camel, yield, or alternation; O9 is equality predicate)`.
- **Grade: unlikely.** Production and alternation branches converge, but all distinctive scene roles are absent.

### 5.10 O10 — 112:4:5 أَحَدٌ — ء ح د, final occurrence

#### L057 — O10 × ء ح د B001 — Opening unity returns in a new grammatical role

- **Initial image.** `(E: ء ح د B001)` at the last token reactivates the exact O3 form and its absolute-unity image, although current syntax selects an additional negative-scope dimension.
- **Word ledger.** `O1=C ق و ل B001 completed utterance; B002–B016 tested`; `O2=E ء ل ه B002 G; B001 R center`; `O3=C ء ح د B001 exact prior predicate; B002–B006 tested`; `O4=E ء ل ه B002 re-anchor`; `O5=E ص م د B001 one-center relation; B002 R compact core; B003–B007 tested`; `O6=C و ل د B003 active exclusion; B001/B002/B004–B006 tested`; `O7=C B003 passive exclusion; others tested`; `O8=C ك و ن B001 negated state; B002–B006 tested`; `O9=C ك ف ء B001 comparison; B002–B005 tested`; `O10=focus B001 + E distinct B002 current scope`.
- **Construction ledger.** `X1=C utterance closes`; `X2=C original predicate`; `X3=E center`; `X4=E same G`; `X5=C negative field`; `X6=C lineage pair`; `X7=C comparison`; `X8=E changed delayed-subject role`; `X9=C`; `X10=E exact return`; `X11=C terminal boundary`; `X12=C exact sound return`.
- **Forks and freeze.** `{ء ح د B001 at O10 as reactivation, ء ل ه B002, ص م د B001, X10}` freezes as the opening one-center image recalled at closure. Prediction: current syntax must transform the token from property assertion into universal rival exclusion.
- **UNUSED_AT_FREEZE and test.** X8 plus distinct `(C: ء ح د B002 negative-scope dimension)` supplies that transformation; O6/O7/O9 explain the relational boundary built between occurrences. `(K: B001 alone is not O10's full contextual function; B002 and delayed-subject syntax govern current scope)`.
- **Grade: strong.** Exact form recurrence plus branch and role change is the primary temporally conditioned reactivation.

#### L058 — O10 × ء ح د B002 — Exhaustive negative subject empties the rival class

- **Initial image.** `(E: ء ح د B002)` is contextually exact under لَمْ; X8 makes O10 the delayed subject ranging over possible bearers of the equality relation.
- **Word ledger.** `O1=C ق و ل B001 closing content; B002–B016 tested`; `O2=C ء ل ه B002 G; B001 tested`; `O3=C ء ح د B001 positive counterpart; B002 K there; B003–B006 tested`; `O4=C ء ل ه B002`; `O5=C ص م د B001 center; B002/B007 rivals, others tested`; `O6=C و ل د B003 active class exclusion; B001/B002/B004–B006 tested`; `O7=C B003 passive exclusion; others tested`; `O8=E ك و ن B001 negated occurrence; B002–B006 tested`; `O9=E ك ف ء B001 candidate relation; B002–B005 tested`; `O10=focus B002`.
- **Construction ledger.** `X1=C closure`; `X2=C first positive`; `X3=C center`; `X4=C`; `X5=E scope`; `X6=C narrower classes`; `X7=E relation-to-G`; `X8=E delayed subject`; `X9=C`; `X10=C branch switch`; `X11=C stop`; `X12=C exact return`.
- **Forks and freeze.** `{ء ح د B002, ك و ن B001, ك ف ء B001, X7–X8}` freezes as `for no candidate x does equivalent(x,G) occur`. Predictions: O3 provides the positive property protected; O6/O7 remove narrower candidate routes; final position closes both grammar and model.
- **UNUSED_AT_FREEZE and test.** O3, O6, O7, X10, X11 fulfill every prediction. `(K: dossier wording about those fit to be addressed does not add an addressee inside the comparison clause; only exhaustive negative scope is recruited)`.
- **Grade: strong.** Branch, polarity, case role, comparison, backward replay, and closure are independently exact.

#### L059 — O10 × ء ح د B003 — Equivalent count falls from one cue to zero fillers

- **Initial image.** `(E: ء ح د B003, form-remote)` treats O10 as the minimum count unit in the candidate class.
- **Word ledger.** `O1=R ق و ل B016 logical definition; others tested`; `O2=E ء ل ه B002 comparison target; B001 0`; `O3=C ء ح د B001/B003 one cue; B002/B004–B006 tested`; `O4=C ء ل ه B002`; `O5=R ص م د B001 one center + B002 indivisible unit; others tested`; `O6=R و ل د B001 possible class member; B002–B006 tested`; `O7=R B001 possible source member; others tested`; `O8=E ك و ن B001 zero occurrence; B002–B006 tested`; `O9=E ك ف ء B001 class counted; B002–B005 tested`; `O10=focus B003 + E B002 contextual scope`.
- **Construction ledger.** `X1=0`; `X2=C one cue`; `X3=R center`; `X4=0`; `X5=E negation`; `X6=R member routes`; `X7=E candidate class`; `X8=E zero fillers`; `X9=0`; `X10=C one→zero`; `X11=C closure`; `X12=0`.
- **Forks and freeze.** `{ء ح د B003, ك ف ء B001, ك و ن B001}` yields a count of equivalents that does not reach one. Predictions: O3 supplies earlier one; final negative syntax supplies zero.
- **UNUSED_AT_FREEZE and test.** X10 exactly produces one-cue→zero-class geometry. `(K: no counted noun/numeral construction; B002 is exact at O10, B001 exact at O3)`.
- **Grade: medium.** The compact numerical model explains order and closure but is lexically subordinate.

#### L060 — O10 × ء ح د B004 — Final first/day/addition branch fails again

- **Initial image.** `(E: ء ح د B004, form-remote)` predicts ordinal, construct, or Sunday/day usage.
- **Word ledger.** `O1=ق و ل B001–B016 0`; `O2=ء ل ه B001–B002 0`; `O3=R ء ح د B004 earlier first/day candidate; B001–B003/B005–B006 tested`; `O4=ء ل ه B001–B002 0`; `O5=R ص م د B007 duration; B001–B006 tested`; `O6=R و ل د B003 temporal event; others tested`; `O7=R B003 temporal event; others tested`; `O8=R ك و ن B001 time; B002–B006 tested`; `O9=ك ف ء B001–B005 0`; `O10=focus B004`.
- **Construction ledger.** `X1=0`; `X2=K first token not ordinal`; `X3=0`; `X4=0`; `X5=R temporal field`; `X6=0`; `X7=0`; `X8=K final indefinite subject`; `X9=0`; `X10=R recurrence with same mismatch`; `X11=R sequence, no calendar`; `X12=0`.
- **Forks and freeze.** `{ء ح د B004, ص م د B007, ك و ن B001}` creates firstness through time; a calendar fork treats recurrent أَحَد as a day marker. Predictions: ordered series, iḍāfa, day/date.
- **UNUSED_AT_FREEZE and test.** Time and sequence are generic. `(K: O10 is indefinite nominative delayed subject; O3 indefinite predicate; neither is construct-state or day name)`.
- **Grade: unlikely.** No occurrence or construction fills B004's distinctive role.

#### L061 — O10 × ء ح د B005 — Possible equals tested as individuals

- **Initial image.** `(E: ء ح د B005, form-remote)` separates candidates into individuals or imagines them arriving one by one.
- **Word ledger.** `O1=ق و ل B001–B016 0`; `O2=E ء ل ه B002 G; B001 0`; `O3=C ء ح د B001 lone center; B002–B006 tested`; `O4=C ء ل ه B002`; `O5=R ص م د B001 common destination; B002–B007 tested`; `O6=R و ل د B001 individual offspring; B002–B006 tested`; `O7=R B001 individual source; others tested`; `O8=E ك و ن B001 candidate occurrence test; B002–B006 tested`; `O9=E ك ف ء B001 equality test; B002–B005 tested`; `O10=focus B005 + E B002 exhaustive scope`.
- **Construction ledger.** `X1=0`; `X2=C one center`; `X3=R destination`; `X4=0`; `X5=E repeated rejection`; `X6=R candidate sources`; `X7=E relation`; `X8=E delayed candidate`; `X9=0`; `X10=C`; `X11=C individual-elimination simulation`; `X12=0`.
- **Forks and freeze.** `{ء ح د B005, ك ف ء B001, ك و ن B001}` creates an evaluator testing each possible equal individually; B002 then exhausts them. Predictions: distributive marker, plural individuals, motion/arrival, or separate acts.
- **UNUSED_AT_FREEZE and test.** Final syntax supports exhaustive testing but not B005's distribution/motion. `(K: no آحاد, arrival, or separate action; B002 directly supplies scope)`.
- **Grade: weak.** The simulation is coherent but distinctive lexical support is absent.

#### L062 — O10 × ء ح د B006 — Terminal mountain/rock avalanche

- **Initial image.** `(E: ء ح د B006, form-remote)` predicts Mount Uḥud as a proper place at the last word.
- **Word ledger.** `O1=R ق و ل B008 stick; B001–B007/B009–B016 tested`; `O2=ء ل ه B001–B002 0`; `O3=R ء ح د B006 first mountain candidate; B001–B005 tested`; `O4=ء ل ه B001–B002 0`; `O5=E ص م د B002 rock/height + B006 strike + B007 endurance; B001/B003–B005 tested`; `O6=و ل د B001–B006 0`; `O7=و ل د B001–B006 0`; `O8=E ك و ن B002 place; B001/B003–B006 tested`; `O9=R ك ف ء B002 overturning; B001/B003–B005 tested`; `O10=focus B006`.
- **Construction ledger.** `X1=K speech`; `X2=R earlier mountain but K form`; `X3=R rock`; `X4=0`; `X5=0`; `X6=0`; `X7=0`; `X8=K delayed subject/equality`; `X9=0`; `X10=R repeated wrong-vocalized place`; `X11=0`; `X12=R sound only`.
- **Forks and freeze.** Place fork `{ء ح د B006 at O3/O10, ص م د B002, ك و ن B002}`; impact fork adds `{ق و ل B008, ص م د B006, ك ف ء B002}`; endurance fork adds ص م د B007. Predictions: mountain/place syntax, hard target, striker, motion.
- **UNUSED_AT_FREEZE and test.** `(K: أَحَدٌ not أُحُد; O10 delayed subject; O3 predicate; O5 predicate; O8 copula; O9 equality)`. No local physical role survives.
- **Grade: unlikely.** The complete rival is audited and multiply defeated.

## 6. Exhaustive constructional, morphosyntactic, and temporal/acoustic seed passes

### C001 — X1 seed — قُلْ and its quoted complement

- **Initial image.** `(E: X1 quoted-complement attachment 112:1 a1)` turns the imperative into an expectation for utterable content rather than an isolated command.
- **Word ledger.** `O1=E ق و ل B001`; `O2=E ء ل ه B002 name`; `O3=E ء ح د B001 first predicate`; `O4=C ء ل ه B002 re-anchor`; `O5=C ص م د B001 second predicate`; `O6=C و ل د B003 active denial`; `O7=C B003 passive denial`; `O8=C ك و ن B001 final clause`; `O9=C ك ف ء B001 comparison`; `O10=C ء ح د B002/B001 exhaustive return`.
- **Construction ledger.** `X1=focus`; `X2=E first content unit`; `X3=C`; `X4=C`; `X5=C`; `X6=C`; `X7=C`; `X8=C`; `X9=C`; `X10=C`; `X11=C`; `X12=C weak`.
- **Forks and freeze.** `{X1, ق و ل B001, X2, ء ل ه B002, ء ح د B001}` freezes as a commissioned proposition identifying G and asserting unity. Predictions: coherent continuation about G, relational completion, terminal syntax that satisfies the command's content expectation.
- **UNUSED_AT_FREEZE and test.** O4–O10/X3–X12 preserve G, add a predicate, remove three relation orientations, and close on delayed repeated أَحَدٌ. `(K: attachment a1 explicitly marks the 112:1 complement; continuation through 112:2–4 is inferred from uninterrupted referential/structural evidence, not from a1 alone)`.
- **Grade: strong.** The construction predicts content continuity and the passage's stopping condition.

### C002 — X2 seed — هُوَ → ٱللَّهُ → أَحَدٌ

- **Initial image.** `(E: X2 attachments 112:1 a2–a3)` opens a 3MS referent, permits the name as apposition, and makes أَحَدٌ its nominative predicate.
- **Word ledger.** `O1=C ق و ل B001 frame`; `O2=E ء ل ه B002 name`; `O3=E ء ح د B001 property`; `O4=C ء ل ه B002 repeated`; `O5=C ص م د B001 new property`; `O6=C و ل د B003 3MS active`; `O7=C B003 3MS passive`; `O8=C ك و ن B001 3MS`; `O9=C ك ف ء B001 to-G relation`; `O10=C ء ح د B002/B001 changed role`.
- **Construction ledger.** `X1=C`; `X2=focus`; `X3=C`; `X4=C`; `X5=C`; `X6=C`; `X7=C`; `X8=C`; `X9=C`; `X10=C`; `X11=C`; `X12=0`.
- **Forks and freeze.** `{X2, ء ل ه B002, ء ح د B001}` freezes as unresolved pronoun → named G → property. Predictions: re-anchor G, maintain 3MS, later pronominal return, no competing named subject.
- **UNUSED_AT_FREEZE and test.** O4, O6–O8, X7/X9 fulfill all predictions. `(K: a3 apposition is strongly licensed at medium confidence, not syntactically forced; the continuity model also rests on forced/stronger morphology and predications)`.
- **Grade: strong.** The seed explains the first temporary-state transition and later reference maintenance.

### C003 — X3 seed — Second positive predication

- **Initial image.** `(E: X3 attachment 112:2 a1)` makes ٱلصَّمَدُ the nominative predicate of repeated ٱللَّهُ.
- **Word ledger.** `O1=C ق و ل B001 frame`; `O2=C ء ل ه B002 first G`; `O3=C ء ح د B001 first predicate`; `O4=E ء ل ه B002 subject`; `O5=E ص م د B001 main relational branch + R B002/B007`; `O6=C و ل د B003`; `O7=C B003`; `O8=C ك و ن B001`; `O9=C ك ف ء B001`; `O10=C ء ح د B002/B001`.
- **Construction ledger.** `X1=C`; `X2=C prior predication`; `X3=focus`; `X4=E re-anchor`; `X5=C`; `X6=C`; `X7=C`; `X8=C`; `X9=C`; `X10=C`; `X11=C positive→negative`; `X12=C coda`.
- **Forks and freeze.** Main `{X3, ء ل ه B002 at O4, ص م د B001}` freezes as a named center receiving a reliance-direction predicate. Rivals B002 compactness and B007 persistence are frozen separately. Predictions: later clauses define relational boundaries of this center.
- **UNUSED_AT_FREEZE and test.** O6/O7/O9 remove outgoing/incoming/parallel relations. B002 rival lacks physical roles; B007 lacks hardship but gains restrained time support. `(K: attachment creates predication only, not unattested lexical meanings)`.
- **Grade: strong.** The construction is the pivot from positive center formation to negative relation tests.

### C004 — X4 seed — Repeated ٱللَّهُ across an ayah boundary

- **Initial image.** `(E: X4 exact recurrence O2→O4)` refreshes the named referent after the first completed predicate and before a new one.
- **Word ledger.** `O1=C ق و ل B001`; `O2=E ء ل ه B002 first anchor`; `O3=C ء ح د B001 completed property`; `O4=E ء ل ه B002 refresh`; `O5=E ص م د B001 new property`; `O6=C و ل د B003 3MS`; `O7=C B003 3MS`; `O8=C ك و ن B001 3MS`; `O9=C ك ف ء B001 with suffix`; `O10=C ء ح د B002/B001`.
- **Construction ledger.** `X1=C`; `X2=E first anchor`; `X3=E new predicate`; `X4=focus`; `X5=C`; `X6=C`; `X7=C`; `X8=C`; `X9=C`; `X10=C`; `X11=E boundary refresh`; `X12=0`.
- **Forks and freeze.** `{X4, ء ل ه B002, X3}` freezes as “G is reactivated at a pause so later clauses may omit its lexical name.” Predictions: implicit 3MS continuation and explicit suffix return.
- **UNUSED_AT_FREEZE and test.** O6/O7/O8 and O9/X7 fulfill those predictions; basmala provides still earlier name activation `(C: opening-context)`. `(K: repetition demonstrates refresh; no extra rhetorical category is asserted)`.
- **Grade: strong.** Position-sensitive recurrence explains why O4 exists and how later reference remains stable.

### C005 — X5 seed — Three successive لَمْ clauses

- **Initial image.** `(E: X5)` establishes a repeated negative operator over three propositions while lexical predicates and voice change.
- **Word ledger.** `O1=C ق و ل B001 frame`; `O2=C ء ل ه B002 G`; `O3=C ء ح د B001 protected property`; `O4=C ء ل ه B002`; `O5=C ص م د B001 center`; `O6=E و ل د B003 active first proposition`; `O7=E B003 passive second`; `O8=E ك و ن B001 third frame`; `O9=E ك ف ء B001 third predicate`; `O10=E ء ح د B002 delayed subject + C B001 return`.
- **Construction ledger.** `X1=C`; `X2=C`; `X3=C`; `X4=C`; `X5=focus`; `X6=E first two paired`; `X7=E third relation`; `X8=E widest candidate`; `X9=C`; `X10=C`; `X11=E widening sequence`; `X12=0`.
- **Forks and freeze.** `{X5, و ل د B003 at O6/O7, ك و ن B001, ك ف ء B001}` freezes as progressive pruning: outgoing birth, incoming birth, then any equivalent. Prediction: final negative clause has widest candidate scope and a delayed exhaustor.
- **UNUSED_AT_FREEZE and test.** O10 B002/X8 fulfills widest scope; O3/X10 reveals what the pruning protects. `(K: لَمْ itself does not intensify or change meaning; widening comes from changed relation roles)`.
- **Grade: strong.** Stable polarity plus systematically changing roles explains order better than generic repetition.

### C006 — X6 seed — Coordinated active/passive birth pair

- **Initial image.** `(E: X6 attachment 112:3 a2 + voice morphology)` tests the same و ل د event in opposite participant orientations under repeated negation.
- **Word ledger.** `O1=C ق و ل B001`; `O2=C ء ل ه B002 G`; `O3=C ء ح د B001 unity`; `O4=C ء ل ه B002`; `O5=C ص م د B001 center`; `O6=E و ل د B003 active`; `O7=E B003 passive`; `O8=C ك و ن B001`; `O9=C ك ف ء B001`; `O10=C ء ح د B002/B001`.
- **Construction ledger.** `X1=0`; `X2=C`; `X3=C`; `X4=C`; `X5=E shared negation`; `X6=focus`; `X7=C`; `X8=C`; `X9=C same 3MS`; `X10=C`; `X11=C orientation expansion`; `X12=C O7 ending`.
- **Forks and freeze.** `{X6, و ل د B003}` freezes as two canceled edges: `BIRTH(G,x)` and `BIRTH(x,G)`. Role forks B001/B002 give offspring/parent interpretations; B005 gives abstract derivation; B006 gives cohort-peer; B004 gives lifecycle. Predictions: broader parallel relation follows and earlier one-center cues become relevant.
- **UNUSED_AT_FREEZE and test.** O9/O10 supplies broader no-equal; O3/O5 backward-corroborate one center. B004/B006 forks are constrained by absent age/cohort; B005 remains secondary. `(K: role arrows are simulation, not translation)`.
- **Grade: strong.** Exact coordination and voice reversal create a complete two-direction subsystem and several controlled branch forks.

### C007 — X7 seed — لَّهُۥ as complement of كُفُوًا

- **Initial image.** `(E: X7 attachment 112:4 a2)` opens a directed comparison relation from an as-yet-unfilled candidate to established 3MS G.
- **Word ledger.** `O1=C ق و ل B001`; `O2=C ء ل ه B002 G`; `O3=C ء ح د B001 criterion`; `O4=C ء ل ه B002`; `O5=C ص م د B001 criterion`; `O6=C و ل د B003 narrower class`; `O7=C B003 inverse class`; `O8=E ك و ن B001 negated occurrence`; `O9=E ك ف ء B001 relation`; `O10=E ء ح د B002 candidate`.
- **Construction ledger.** `X1=C`; `X2=C`; `X3=C`; `X4=C`; `X5=E scope`; `X6=C`; `X7=focus`; `X8=E filler structure`; `X9=C back-reference`; `X10=C`; `X11=C`; `X12=0`.
- **Forks and freeze.** `{X7, ك ف ء B001}` freezes as open relation `EQUIVALENT(x,G)`. Predictions: a governor determines polarity/occurrence; a later subject fills x; earlier profile supplies comparison criteria.
- **UNUSED_AT_FREEZE and test.** O8 supplies negated occurrence, O10 fills/exhausts x, O3/O5/O6/O7 supply criteria and narrower exclusions. `(K: X7 licenses comparison complement only, not marriage/war/recompense domains)`.
- **Grade: strong.** One attachment predicts the final candidate role and triggers full backward replay.

### C008 — X8 seed — Negated kana predicate and delayed subject

- **Initial image.** `(E: X8 attachments 112:4 a3–a4)` places كُفُوًا as accusative predicate of negated يَكُن and delays nominative أَحَدٌ until the final token.
- **Word ledger.** `O1=C ق و ل B001 closing speech`; `O2=C ء ل ه B002 G`; `O3=C ء ح د B001 earlier role`; `O4=C ء ل ه B002`; `O5=C ص م د B001`; `O6=C و ل د B003`; `O7=C B003`; `O8=E ك و ن B001`; `O9=E ك ف ء B001`; `O10=E ء ح د B002 + C B001`.
- **Construction ledger.** `X1=C closure`; `X2=C role contrast`; `X3=C`; `X4=C`; `X5=E negation`; `X6=C`; `X7=E relation target`; `X8=focus`; `X9=C`; `X10=C exact role switch`; `X11=C terminal boundary`; `X12=C exact sound return`.
- **Forks and freeze.** `{X8, ك و ن B001, ك ف ء B001, ء ح د B002}` freezes as a suspended candidate slot: “who could be equivalent to G?” Prediction: last word empties the class, repeats an earlier cue, and ends the passage.
- **UNUSED_AT_FREEZE and test.** O3/X10 gives exact earlier cue; O6/O7 gives prior class pruning; X11 confirms stop at slot completion. `(K: delayed subjects do not universally close passages; claim is construction-specific)`.
- **Grade: strong.** Syntax itself produces expectation, suspension, completion, reactivation, and stopping.

### C009 — X9 seed — One referent through pronoun, name, ellipsis, and suffix

- **Initial image.** `(E: X9)` tracks هُوَ → ٱللَّهُ → repeated ٱللَّهُ → implicit 3MS verb subjects → هُۥ.
- **Word ledger.** `O1=C ق و ل B001 outside quote`; `O2=E ء ل ه B002 first name`; `O3=E ء ح د B001 property of G`; `O4=E ء ل ه B002 refresh`; `O5=E ص م د B001 property of G`; `O6=E و ل د B003 3MS`; `O7=E B003 3MS`; `O8=E ك و ن B001 3MS`; `O9=E ك ف ء B001 governs relation to suffix`; `O10=C ء ح د B002 delayed candidate, not new name`.
- **Construction ledger.** `X1=E quote boundary`; `X2=E resolution`; `X3=E`; `X4=E`; `X5=E same subject`; `X6=E same subject`; `X7=E suffix`; `X8=C final candidate`; `X9=focus`; `X10=C`; `X11=C`; `X12=0`.
- **Forks and freeze.** `{X9, ء ل ه B002}` freezes as one discourse node G maintained by four realization types. Predictions: no competing 3MS/name; all properties/negations target G; final أَحَدٌ serves candidate role rather than replacing G.
- **UNUSED_AT_FREEZE and test.** X8 identifies O10 as delayed subject of the comparison clause; O2/O4 exact repetition and all agreement support continuity. `(K: agreement alone would be insufficient, but name repetition and attachment add independent constraints)`.
- **Grade: strong.** The temporary recitation state is explicit and continuous across every ayah.

### C010 — X10 seed — Exact أَحَدٌ recurrence with branch/role change

- **Initial image.** `(E: X10)` holds O3 active until O10 repeats the exact form: predicate B001 first, delayed negative subject B002 last.
- **Word ledger.** `O1=C ق و ل B001 bracketed content`; `O2=E ء ل ه B002 bearer`; `O3=E ء ح د B001 positive predicate`; `O4=C ء ل ه B002`; `O5=C ص م د B001 center`; `O6=C و ل د B003 outward denial`; `O7=C B003 inward denial`; `O8=C ك و ن B001`; `O9=C ك ف ء B001 rival relation`; `O10=E ء ح د B002 + reactivated B001`.
- **Construction ledger.** `X1=C closure`; `X2=E first role`; `X3=C`; `X4=C`; `X5=C`; `X6=C`; `X7=C`; `X8=E second role`; `X9=C`; `X10=focus`; `X11=C terminal bracket`; `X12=C exact coda`.
- **Forks and freeze.** `{X10, ء ح د B001 at O3, ء ح د B002 at O10, X2, X8}` freezes as “assert ONE(G), later empty every EQUAL(x,G) candidate with the same form.” Predictions: intervening clauses explain the transition from property to empty rival class.
- **UNUSED_AT_FREEZE and test.** O5 builds one center, O6/O7 prunes lineage, O9 names equality; sequence is necessary. `(K: B001 and B002 remain distinct facts tied to distinct syntax)`.
- **Grade: strong.** This directly instantiates temporally conditioned reactivation.

### C011 — X11 seed — Ayah boundaries and phased role completion

- **Initial image.** `(E: X11)` segments 112:1 as identification/unity, 112:2 as second positive predicate, 112:3 as paired lineage denial, and 112:4 as general comparison denial.
- **Word ledger.** `O1=E ق و ل B001 start`; `O2=E ء ل ه B002 identification`; `O3=E ء ح د B001 first boundary`; `O4=E ء ل ه B002 reset`; `O5=E ص م د B001 second boundary`; `O6=E و ل د B003`; `O7=E B003 third boundary`; `O8=E ك و ن B001`; `O9=E ك ف ء B001`; `O10=E ء ح د B002/B001 terminal boundary`.
- **Construction ledger.** `X1=E opening expectation`; `X2=E unit 1`; `X3=E unit 2`; `X4=E reset`; `X5=E negative phase`; `X6=E unit 3`; `X7=E unit 4 relation`; `X8=E unit 4 completion`; `X9=C continuity`; `X10=C return`; `X11=focus`; `X12=C sound boundary marker`.
- **Forks and freeze.** `{X11, O1–O7}` freezes after 112:3 as three completed layers: identify/one, center relation, two-way genealogy exclusion. Prediction: final ayah generalizes the relation and reconnects to layer one.
- **UNUSED_AT_FREEZE and test.** O8–O10/X7–X10 fulfill exactly that. `(K: boundaries segment temporary state but do not create lexical meanings)`.
- **Grade: strong.** Each pause follows a role-complete subsystem, and the last completes both grammar and backward model.

### C012 — X12 seed — Coda maintenance and exact terminal return

- **Initial image.** `(E: X12 sacred-text ending sequence أَحَد / صَمَد / يُولَد / أَحَد)` keeps final د and related coda material active while only the first/last word repeats exactly.
- **Word ledger.** `O1=C ق و ل B001 recited output`; `O2=ء ل ه B001–B002 0 acoustically`; `O3=E ء ح د B001 first ending`; `O4=ء ل ه B001–B002 0`; `O5=E ص م د branches all read; lexical selection not inferred from sound`; `O6=و ل د B001–B006 0`; `O7=E و ل د B003 ending`; `O8=ك و ن B001–B006 0`; `O9=K ك ف ء B003 not selected as local rhyme sense`; `O10=E ء ح د B002/B001 exact return`.
- **Construction ledger.** `X1=C voiced sequence`; `X2=C first role`; `X3=C second boundary`; `X4=0`; `X5=0`; `X6=C O7 ending`; `X7=0`; `X8=C terminal syntax`; `X9=0`; `X10=E exact return`; `X11=E boundary alignment`; `X12=focus`.
- **Forks and freeze.** `{X12, O3/O5/O7/O10 forms}` freezes as acoustic maintenance with exact endpoint return. A lexical rival from ك ف ء B003 was generated in L054 but kept separate. Prediction: exact sound return coincides with semantic and syntactic reactivation.
- **UNUSED_AT_FREEZE and test.** X8/X10 fulfill that coincidence. `(K: sound recurrence alone is weak; no claim of technical rhyme classification; كُفُوًا locally realizes B001, not B003)`.
- **Grade: medium-strong.** Acoustic evidence becomes meaningful only because it synchronizes with exact form, role, branch, and boundary completion.

## 7. Post-sweep missing-image registry

This registry checks that every remotely plausible image found during the complete ledgers was actually generated, frozen, tested, and either retained or defeated. Repetition across independently seeded rows is convergence, not extra evidence.

| Image family | Independent generating seeds | Completed roles | Decisive test | Result |
| --- | --- | --- | --- | --- |
| Commanded one-center boundary | L001, L018, L019, L026, L027, L036, L042, L046, L052, L057, L058; C001–C011 | speech, named G, unity, reliance direction, outgoing/incoming/parallel exclusions, exhaustive terminal subject | exact morphology + attachments + unused role predictions | **strong** |
| Spoken definition | L016, with convergence from L013/L014 | named definiendum, two positive specifications, three negative differentiae | local قُلْ remains B001 speech, not technical B016 | **medium-strong secondary** |
| Worshipped/reliance center | L017, L025, with L027 | worshipped center, one endpoint, no source/product/equal | no worshipper/ritual syntax | **medium / medium-strong secondary** |
| Compact sealed core | L028, L029; physical rivals in L019/L027 | compactness, no cavity, stopper, blocked output/input, no duplicate | no body/vessel/opening; birth not transfer | **medium to weak secondary** |
| Persistence through time | L033, with L047/L050 rivals | stable G, repeated negative states, no transition/equal | no hardship/camel; temporal scope kept narrow | **medium secondary** |
| Corrective false-attribution protocol | L005 | target, positive claims, lineage/equality denials | no liar, prior saying, or correction marker | **weak** |
| Inward proposition → voiced speech | L006, L012 | inner content, externalization, complete proposition | no inner locus/concealment | **weak** |
| Circulating compact saying | L007 | launchable utterance, repeated name/word/coda, bounded units | no transmitters/hearers; singular command | **weak** |
| Negotiation without counterpart | L009 | affair, two-party/equality role, empty counterpart slot | no reciprocal form or response | **weak** |
| Authority/control/oversight/guarantee | L004, L010, L015, L031, L048 | authoritative center, care, affair, guarantor, opposition | no commander identity, patient, affair, beneficiary, or remote forms | **weak** |
| Submission toward worshipped center | L049 | submitter, worshipped/reliance endpoint, authority | no submitter or استكانة morphology | **weak** |
| Unmatched place/elevation/rank | L047, with L024/L062 place forks | unique station, hard/elevated place, no equal rank | يَكُن copula; no locative/rank form | **weak** |
| Count one → zero equivalents | L021, L059 | one cue, comparison class, zero fillers | no numeral construction; B001/B002 more exact | **weak / medium secondary** |
| Individual-by-individual candidate testing | L023, L061 | candidate class, separate tests, exhaustive denial | no distributive/motion morphology | **weak** |
| Same-age peer/cohort | L039, L045 | birth cohort, time, peer equality, empty class | no age or لِدَة form | **weak** |
| Birth-to-old-age lifecycle | L037, L043, L050 | birth, youth/newborn, endurance, old-age recollection | events negated; no age, first person, or old-man form | **unlikely** |
| Stick → strike → rock/mountain → overturn | L008, L024, L032, L053, L062 | instrument, action, hard target, place, motion result | four incompatible local forms; no agent/impact clause | **unlikely** |
| Cloth/body/shelter enclosure | L002, L030, L055 | tongue/head, wrap, sewn panels, closure, place | no body, cloth, sewing, shelter, or relevant morphology | **unlikely** |
| Coda variation / rhyme-mismatch rival | L054 and C012 | four endings, variation, exact return | acoustic trajectory real; O9 locally equality, no poetry frame | **weak lexical / medium-strong acoustic** |
| Alternating annual production | L056 | offspring/yield, active/passive alternation, duration/year expectation | no year, herd/palm, yield, or two groups | **unlikely** |
| Firstness/Sunday through time | L022, L060 | first point/day, temporal sequence, recurrence | no ordinal, iḍāfa, or calendar syntax | **unlikely** |
| Bad/hard state | L051 | hardship/state plus repeated negation | actual kana predicate is equality | **unlikely** |

No additional image family remained after replaying every `R` decision across the 74 seed ledgers. Images sharing only a generic feature without a missing role—such as “negative,” “one,” or “hard”—were not promoted into new models.

## 8. Controlled multi-seed synthesis

### S112-P2-A — One named center and the exhaustion of every competing relation

- **GENERATING_SET.** `(E: ق و ل B001 at O1)`, `(E: X1)`, `(E: ء ل ه B002 at O2)`, `(E: X2)`, `(E: ء ح د B001 at O3)`, `(E: X4)`, `(E: ص م د B001 at O5)`, `(E: X3)`.
- **Frozen model after O5.** The commanded content establishes one named node `G`; O3 predicates unity; O5 makes G the endpoint of قصد/اعتماد. This creates three open relational questions around G: can a same-lineage node proceed from G, can G proceed from another, and can a parallel node equal G?
- **Predictions at freeze.** Preserve G through agreement/anaphora; deny `BIRTH(G,x)`; deny `BIRTH(x,G)`; deny `EQUIVALENT(x,G)` for every candidate; reactivate O3 when the candidate class becomes empty; close the quote exactly there.
- **UNUSED_AT_FREEZE.** O6–O10; X5–X12; all ك و ن and ك ف ء branches; both later و ل د event orientations; final ء ح د branch/role; final attachments and boundaries.
- **Corroboration.** `(C: و ل د B003 at O6 + active morphology)` removes the outward relation. `(C: و ل د B003 at O7 + passive morphology + X6)` removes the inward relation. `(C: ك و ن B001 at O8 + ك ف ء B001 at O9 + X7/X8)` removes parallel equivalence. `(C: ء ح د B002 at O10)` exhausts candidates. `(C: X10)` reactivates O3's B001. `(C: X9)` preserves G. `(C: X11)` stops at completed grammar/model. `(C: X12)` adds subordinate acoustic maintenance.
- **Constraints.** `(K: ص م د B001 does not add an expressed seeker)`. `(K: graph arrows preserve birth/equality primary meanings)`. `(K: no physical body/container is required)`. `(K: ك ف ء B001 is general counterpart/equality only)`. `(K: no unsupported unlimited temporal claim from لَمْ/يَكُن)`.
- **Rival forks.** Spoken-definition geometry is medium-strong but qawl B016 is remote. Compact-core, persistence, worship-center, count, and acoustic models remain subordinate. Every physical, textile, authority, lifecycle, and production model is explicitly retained in §7 and constrained.
- **Final grade: strong.** Independent singleton and construction seeds converge on the same small model, and the model predicts unused orientation, scope, reactivation, reference, and closure facts.

## 9. Exhaustiveness audit results

The post-creation gate was run, the file was revised, and the gate was rerun. Final results:

- **PASS:** 62 lexical headings are sequentially L001–L062 and match the expected O1–O10 root/branch blocks.
- **PASS:** 12 construction headings are sequentially C001–C012 and match X1–X12.
- **PASS:** all 74 seed records have exactly one `Word ledger`, and every ledger contains O1–O10 exactly once: **740 explicit occurrence decisions**.
- **PASS:** all 74 seed records have exactly one `Construction ledger`, and every ledger contains X1–X12 exactly once: **888 explicit construction decisions**.
- **PASS:** all 74 records contain initial image, word visits, construction visits, freeze/forks, `UNUSED_AT_FREEZE` testing, constraints, an allowed grade, and grade rationale.
- **PASS:** all 48 uncontaminated `branch_image_ar` and all 48 matching `what_is_ar` strings are preserved in §4.
- **PASS:** every meaningful `R` fork is frozen/tested in its seed and represented or terminated in §7; replay found no unrecorded image family.
- **PASS:** no basmala seed exists; its name occurs only as explicitly labeled opening-context corroboration.
- **PASS after revision:** no placeholder, foreign-script intrusion, or trailing whitespace remains.

## 10. Very short interpretation

The recitation first fixes one named center and gives it a positive profile. It then cancels a relation outward, the same relation inward, and finally every parallel equivalent; terminal أَحَدٌ changes from the opening predicate into the exhaustive subject that empties the rival slot and closes the commanded utterance.
