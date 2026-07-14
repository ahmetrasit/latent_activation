# Stage 1 test Pass 2 — S112 comparator lane

Assigned passage: S112  
Output path: `v1/outputs/112_comparator/stage1_test_pass2.md`

## Pass 2 restart note and root-cause diagnosis

Root cause of the Pass 1 limitation: I compressed the audit trail. I used a shorthand such as `V=all` and then wrote mostly the branches that succeeded or looked promising. That created the appearance, and in several findings the practical effect, of visiting only a limited number of words/roots per finding. The prompt requires a seed-by-seed cross-root sweep where even failing branches get their own turn, and where every eligible rooted occurrence and eligible construction can initiate a seed pass. Pass 2 therefore restarts from the first rooted word, `112:1:1 قُلْ`, and records all 62 occurrence × branch lexical seeds before constructional, morphosyntactic, and temporal seeds.

## Sacred Arabic text in scope

```text
opening-context only, never a seed:
بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ

112:1 قُلْ هُوَ ٱللَّهُ أَحَدٌ
112:2 ٱللَّهُ ٱلصَّمَدُ
112:3 لَمْ يَلِدْ وَلَمْ يُولَدْ
112:4 وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ
```

## Rooted QAC sequence used for seed order

```text
112:1:1 قُلْ        قول    V IMPV 2MS
112:1:3 ٱللَّهُ     ءله    PN NOM
112:1:4 أَحَدٌ      ءحد    N INDEF NOM
112:2:1 ٱللَّهُ     ءله    PN NOM
112:2:2 ٱلصَّمَدُ   صمد    DET + N MS NOM
112:3:2 يَلِدْ      ولد    V IMPF JUS 3MS under لَمْ
112:3:4 يُولَدْ     ولد    V IMPF PASS JUS 3MS under لَمْ
112:4:2 يَكُن       كون    V IMPF JUS 3MS under وَلَمْ
112:4:4 كُفُوًا     كفء    N INDEF ACC
112:4:5 أَحَدٌۢ     ءحد    N INDEF NOM
```

## Attachment rows used as structure only

```text
112:1 a1 quoted_complement: quoted content after قُلْ is هُوَ ٱللَّهُ أَحَدٌ.
112:1 a2 predication: أَحَدٌ is nominative predicate of ٱللَّهُ.
112:1 a3 apposition: ٱللَّهُ can stand as apposition to هُوَ while أَحَدٌ supplies the nominal predicate.
112:2 a1 predication: ٱلصَّمَدُ is nominative predicate of ٱللَّهُ.
112:3 a1 particle_complement: يَلِدْ governed by لَمْ as jussive negated imperfect.
112:3 a2 conjoined: يُولَدْ coordinated with يَلِدْ.
112:3 a3 particle_complement: يُولَدْ governed by لَمْ as jussive negated passive imperfect.
112:4 a1 particle_complement: يَكُن governed by لَمْ as jussive negated imperfect.
112:4 a2 prep_complement: pronoun in لَّهُۥ is governed by لَـ as complement of كُفُوًا.
112:4 a3 kana_predicate: كُفُوًا is accusative predicate of negated copula يَكُن.
112:4 a4 subject: أَحَدٌ is delayed nominative subject of يَكُن.
```

## Complete uncontaminated branch dossiers read

Every seed below uses the same full control sweep, abbreviated as `S112-ALL`:

```text
قول: B001 إخراج القول بالنطق — يدخل فيه قال يقول قولا، والقول والقيل، والكلام المركب من الحروف إذا أبرز بالنطق، مفردا كان أو جملة أو قصيدة أو خطبة.
قول: B002 اللسان آلة القول — يدخل فيه المقول بمعنى اللسان.
قول: B003 كثرة القول في صاحبه — يدخل فيه قولة وقوال وقوالة وتقوالة وقؤول ومقوال ومقول إذا وصفت الإنسان بأنه لسن أو كثير القول أو منطيق.
قول: B004 القيل صاحب القول النافذ — يدخل فيه المقول أو القيل بلغة أهل اليمن، والواحد القيل، والجمع المقاولة والأقيال والأقوال، وملك حمير دون الملك الأعظم، والمرأة قيلة.
قول: B005 قول ما لم يكن أو نسبته — يدخل فيه تقول باطلا، وتقول عليه أي كذب عليه، وقولتني أو أقولتني ما لم أقل.
قول: B006 اجترار القول إلى النفس — يدخل فيه اقتال قولا إذا اجتر إلى نفسه قولا من خير أو شر.
قول: B007 القول الفاشي بين الناس — يدخل فيه القالة الحسنة أو القبيحة المنتشرة في الناس، وكثرة قالة الناس، والقيل والقال بوصفهما حديثا دائرا.
قول: B008 عود القال لضرب القلة — يدخل فيه القال، الخشبة التي تضرب بها القلة.
قول: B009 المقاولة في الأمر — يدخل فيه قاولته في أمره وتقاولنا إذا تفاوضنا.
قول: B010 اقتالة الحكم على غيره — يدخل فيه اقتال عليه إذا كان بمعنى تحكم.
قول: B011 قول يجري مجرى الظن — يدخل فيه تقول إذا أجري مجرى تظن في العمل، وخاصة في الاستفهام، وما ذكر عن بني سليم من إجراء متصرف قلت مجرى الظن في غير الاستفهام.
قول: B012 قول في النفس لم يظهر — يدخل فيه المتصور في النفس قبل الإبراز باللفظ، كما في قول في نفسي لم أظهره.
قول: B013 القول اعتقاد ومذهب — يدخل فيه القول بمعنى الاعتقاد، نحو فلان يقول بقول أبي حنيفة.
قول: B014 قول الشيء دلالته — يدخل فيه القول للدلالة على الشيء، مثل امتلأ الحوض وقال قطني.
قول: B015 العناية الصادقة بالشيء — يدخل فيه فلان يقول بكذا إذا كان معناه العناية الصادقة بالشيء.
قول: B016 قول الشيء حده — يدخل فيه استعمال المنطقيين القول بمعنى الحد، كقول الجوهر وقول العرض أي حدهما.

ءله: B001 التعبد والمعبود — يدخل فيه أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.
ءله: B002 اسم الله في القسم والنداء — يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.

ءحد: B001 الأَحَدِيَّة والوَحْدَة — أحد بمعنى الواحد، والوصف المطلق بأحد، وتكرار أحد أحد للتأكيد
ءحد: B002 استغراق النفي — أحد في سياق النفي لاستغراق جنس من يصلح أن يخاطب، فيشمل الواحد وما فوقه
ءحد: B003 الواحد في العد والتركيب — أحد في العد، وتركيبه مع العشرات، وتصْيير المعدود أحد عشر
ءحد: B004 الأول والإضافة — أحد مضافا أو مضافا إليه بمعنى الأول، واسم يوم الأحد
ءحد: B005 الانفراد والتفرق آحادا — الانفراد بالفعل، والمجيء آحادا أفرادا
ءحد: B006 جبل أُحُد — اسم جبل بالمدينة

صمد: B001 القصد إلى المعتمد المقصود — قصد الشيء واعتماده؛ السيد الذي يقصد إليه في الأمور والحوائج؛ الصمد من جهة الصمود إليه
صمد: B002 الصلابة المكتنزة بلا جوف — الصلابة والاكتناز وانعدام الجوف؛ المكان الصلب أو المرتفع الغليظ؛ الصخرة الراسية والأرض الشديدة
صمد: B003 سدادة القارورة المحكمة — الصماد بمعنى عفاص القارورة أو سدادها؛ فعل صمد القارورة أي جعل لها صمادا
صمد: B004 شد الرأس بصماد — تصميد الرأس بخرقة أو منديل أو ثوب دون العمامة
صمد: B005 الإشراف على الأمر مع الحفل به — قولهم على صمادة من أمر لمن أشرف عليه وحفل به
صمد: B006 إيقاع الضرب بالعصا — صمده بالعصا بمعنى ضربه بها
صمد: B007 الدوام والبقاء على الشدة — الدوام والبقاء؛ الناقة المصماد الباقية على القر والجدب الدائمة الرسل

ولد: B001 مولود من نسل — يدخل فيه الولد والمولود والابن والابنة والأولاد، ويستعمل للواحد والجمع وللصغير والكبير وللذكر والأنثى بحسب نصوص المصادر.
ولد: B002 أبوان من جهة الولادة — يدخل فيه الوالد بمعنى الأب، والوالدة بمعنى الأم، والوالدان للأب والأم.
ولد: B003 حدوث الولادة ووضع الحمل — يدخل فيه ولدت المرأة، والولادة بوضع الوالدة ولدها، وما قرب من وقت الولادة أو حان ولاده في أولدت، وولادة الحيوان إذا نصت المصادر عليها.
ولد: B004 صغير قريب العهد بالولادة أو مملوك — يدخل فيه الوليد للصبي أو الغلام القريب العهد بالولادة، والوليدة للصبية أو الأمة، وما جمعه ولدان أو ولائد بحسب النص.
ولد: B005 شيء حاصل عن شيء أو مستحدث منه — يدخل فيه تولد الشيء من الشيء إذا حصل عنه بسبب، والمولد من الكلام إذا استحدث، وما كان غير محض أو ناشئا في بيئة معينة مثل عربية مولدة ورجل مولد.
ولد: B006 قرين في سن الولادة — يدخل فيه اللدة أو لدة الرجل بمعنى تربه ومثيله في السن.

كون: B001 وقوع الشيء وحضوره في زمان — يدخل فيه وقوع الشيء وحضوره وحدوثه في زمان ماض أو راهن، ومصدر كان والكينونة والكائنة، واستعمال كان خبرا أو توكيدا أو في الاستثناء.
كون: B002 المكان والمكانة من الكون — يدخل فيه المكان والموضع والمكانة والمنزلة والتمكن إذا جعلت من كان يكون.
كون: B003 الكفالة والقيام على فلان — يدخل فيه الكيانة والكفالة والتكفل بفلان واكتنت به.
كون: B004 الخضوع بالاستكانة — يدخل فيه الاستكانة بمعنى الخضوع.
كون: B005 الشيخ المنسوب إلى كُنْتُ — يدخل فيه الكُنْتِيّ للرجل إذا شاخ كأنه نسب إلى قوله كُنْتُ في شبابي.
كون: B006 حالة السوء بكينة — يدخل فيه قولهم بات فلان بكينة سوء أي بحال سوء إذا جعلت الكينة فعلة من الكون.

كفء: B001 المماثلة والمقابلة بالمثل — يدخل فيه الكفء والمثل والنظير؛ التساوي والتكافؤ؛ الكفاءة في المناكحة والحرب والمضادة؛ المكافأة والمجازاة بالمثل؛ المقابلة والموالاة بين شيئين
كفء: B002 الإمالة والقلب والصرف — يدخل فيه إمالة الشيء وقلبه وكبه؛ إمالة القوس والصحفة؛ صرف القوم عن وجهتهم؛ التمايل في المشي أو كالسفينة؛ انكسار الوجه وتغير اللون
كفء: B003 اختلاف القوافي — يدخل فيه الإكفاء في الشعر باختلاف القوافي في الحروف أو الحركات أو الإعراب
كفء: B004 كِفاء الخباء — يدخل فيه الكِفاء بمعنى شقة أو شقتين تخاطان ويجعل بهما مؤخر الخباء أو البيت
كفء: B005 كفأة السنة والنتاج — يدخل فيه الكفأة لحمل النخلة أو نتاج الإبل سنة؛ سؤال نتاج الإبل أو ثمر النخل سنة؛ إعطاء اللبن والوبر والأولاد سنة؛ جعل الإبل كفأتين يتناوب نتاجهما
```

## Exhaustive lexical seed inventory

```text
L01-L16: 112:1:1 قُلْ / قول B001-B016
L17-L18: 112:1:3 ٱللَّهُ / ءله B001-B002
L19-L24: 112:1:4 أَحَدٌ / ءحد B001-B006
L25-L26: 112:2:1 ٱللَّهُ / ءله B001-B002
L27-L33: 112:2:2 ٱلصَّمَدُ / صمد B001-B007
L34-L39: 112:3:2 يَلِدْ / ولد B001-B006
L40-L45: 112:3:4 يُولَدْ / ولد B001-B006
L46-L51: 112:4:2 يَكُن / كون B001-B006
L52-L56: 112:4:4 كُفُوًا / كفء B001-B005
L57-L62: 112:4:5 أَحَدٌۢ / ءحد B001-B006
```

For every lexical seed below, `Visited: S112-ALL` means every branch listed in the complete dossiers above was read and tested in that seed pass; selected branches are then named separately. This is a record of an exhaustive control sweep, not evidence by itself.

## Lexical seed passes

### L01 — 112:1:1 قُلْ / قول B001 — outward utterance opens the quote

Initial image: a command causes كلام to be brought out in speech.  
Visited: S112-ALL. Selected before freeze: `(E: قول B001 outward utterance)`, `(E: attachment 112:1 a1 quoted_complement)`, `(E: ءله B002 divine-name occurrence)`, `(E: ءحد B001 positive unity predicate)`, `(E: صمد B001 second-predicate support/reliance)`.  
Image description: the first rooted word opens a spoken container; what is brought out is not free speech but a bounded quote naming `ٱللَّهُ`, predicating `أَحَدٌ`, then reactivating the name for `ٱلصَّمَدُ`.  
Generating set: قول B001; quoted-complement attachment; ءله B002; ءحد B001; صمد B001.  
Frozen model: commanded disclosure of a single named referent with positive unity and support/self-standing predicate.  
Predictions at freeze: later material should close off relations incompatible with the disclosed unity/support: lineage, origination, equivalent counterpart.  
Unused features tested after freeze: ولد active/passive, كون, كفء, final أحد, repeated لم, له, ayah closure, basmala opening-context.  
Corroborators: `(C: ولد B003 after-freeze, active/passive birth-event denied)`, `(C: ولد B005 after-freeze, generated-from relation denied)`, `(C: كفء B001 after-freeze, equality denied)`, `(C: ءحد B002 final negative-scope occurrence)`, `(C: sequence first أحد→final أحد)`, `(C: basmala opening-context divine-name activation)`.  
Constraints: `(K: قُلْ remains a speech imperative; no unsupplied non-speech action is allowed)`, `(K: ولد relations are negated, not enacted)`.  
Rejected or terminated branches: قول B002-B015 do not become the main model; صمد B002 can support self-containedness only as a secondary simulation; literal صمد B003-B006 rejected.  
Rival forks: definition-like قول B016 fork converges later but is not the seed here.  
Final grade: strong — the seed is exact to the first rooted word and predicts the later negated relational closures.

### L02 — 112:1:1 قُلْ / قول B002 — tongue as instrument

Initial image: the organ/tool by which speech is produced.  
Visited: S112-ALL. Selected before freeze: `(E: قول B002 speech-instrument)` only; no other branch gives an organ role.  
Generating set: قول B002.  
Frozen model: a possible bodily instrument behind the command.  
Predictions at freeze: an instrument, mouth, tongue, or bodily articulation role would need to appear.  
Unused features tested after freeze: quote structure, divine name, predicates, negations, final equality clause.  
Corroborators: none specific.  
Constraints: `(K: attachment 112:1 a1 makes the active structure quote-content, not an organ scene)`, `(K: no لسان or instrument participant occurs)`.  
Rejected or terminated branches: all cross-root branches fail to complete an organ image; صمد B006 striking-instrument and قول B008 stick-object are rejected as unrelated instruments.  
Rival forks: none.  
Final grade: unlikely — the branch is lexical but unsupported passage-locally.

### L03 — 112:1:1 قُلْ / قول B003 — person of much speech

Initial image: a speaker characterized by كثرة القول.  
Visited: S112-ALL. Selected before freeze: `(E: قول B003 loquacity)` only.  
Generating set: قول B003.  
Frozen model: talkative-person image.  
Predictions at freeze: repeated sayings, social speech characterization, or a speaker quality.  
Unused features tested after freeze: all predicates and negations.  
Corroborators: none.  
Constraints: `(K: only one compact imperative and quote occurs)`, `(K: no human speaker-description noun occurs)`.  
Rejected or terminated branches: قول B007 public saying is a possible neighbor but lacks social circulation roles; no other root supplies talkativeness.  
Rival forks: none.  
Final grade: unlikely — the passage is terse commanded declaration, not كثرة قول.

### L04 — 112:1:1 قُلْ / قول B004 — authoritative saying-holder

Initial image: صاحب القول النافذ / قيل.  
Visited: S112-ALL. Selected before freeze: `(E: قول B004 authority-of-saying)`, `(E: attachment 112:1 a1 quoted_complement)`; selected only structurally, not as a lexical title.  
Generating set: قول B004 plus quote structure.  
Frozen model: an utterance with authoritative force.  
Predictions at freeze: the content should be high-stakes and identity-setting.  
Unused features tested after freeze: divine Name, unity predicate, ṣamad predicate, negations.  
Corroborators: `(C: ءله B002 after-freeze, divine name in the quote)`, `(C: ءحد B001 after-freeze, identity predicate)`.  
Constraints: `(K: no qīl/Yemenite title/ruler role is locally present)`, `(K: authority is inferred from command and content, not branch-specific title evidence)`.  
Rejected or terminated branches: كفء B001 and ولد B003 corroborate the content only after freeze; they do not construct an authority-holder scene.  
Rival forks: none.  
Final grade: weak — high declaration fits weakly, but the branch-specific image is absent.

### L05 — 112:1:1 قُلْ / قول B005 — false attribution or saying what was not

Initial image: an utterance falsely made or attributed.  
Visited: S112-ALL. Selected before freeze: `(E: قول B005 false-attribution possibility)` only.  
Generating set: قول B005.  
Frozen model: possible mis-saying/false attribution.  
Predictions at freeze: a denial of a false quote, correction, or attribution dispute.  
Unused features tested after freeze: quote content and later negations.  
Corroborators: none.  
Constraints: `(K: قُلْ is a positive imperative with a forced quoted complement)`, `(K: the later negations target ولد/كفء relations, not false speech)`.  
Rejected or terminated branches: قول B001 defeats this by providing the ordinary speech frame; no root supplies lying/attribution dispute.  
Rival forks: none.  
Final grade: unlikely — no passage-local false-saying frame appears.

### L06 — 112:1:1 قُلْ / قول B006 — drawing a saying into oneself

Initial image: اجترار القول إلى النفس.  
Visited: S112-ALL. Selected before freeze: `(E: قول B006 inward-drawn saying)`, with a weak fork `(E: قول B012 hidden inner saying)` tested and then constrained.  
Generating set: قول B006, optional قول B012.  
Frozen model: an interiorized saying before utterance.  
Predictions at freeze: private inward content should remain or be contrasted with outward quote.  
Unused features tested after freeze: attachment 112:1 a1, visible quote sequence.  
Corroborators: none stable.  
Constraints: `(K: قُلْ externalizes the saying immediately)`, `(K: attachment 112:1 a1 supplies overt quote-content)`.  
Rejected or terminated branches: all other roots address the quote’s content rather than interior appropriation.  
Rival forks: B012 hidden-saying fork terminates with the same constraint.  
Final grade: unlikely — it works only as a contrast to the actual outward command.

### L07 — 112:1:1 قُلْ / قول B007 — saying spread among people

Initial image: قول فاشٍ circulating among people.  
Visited: S112-ALL. Selected before freeze: `(E: قول B007 public-circulation)`, `(E: قول B001 utterance substrate)` weakly.  
Generating set: قول B007 with B001 as speech substrate.  
Frozen model: a declaration capable of public circulation.  
Predictions at freeze: people, circulation, report-spread, or repeated social saying.  
Unused features tested after freeze: all predicates and negations.  
Corroborators: none specific; recitational command is compatible but not branch-specific.  
Constraints: `(K: no ناس, قالة الناس, or report-circulation construction occurs)`.  
Rejected or terminated branches: ءله/ءحد/صمد become content, not evidence of social circulation.  
Rival forks: none.  
Final grade: weak — possible at the recitation level, not lexically completed by the passage.

### L08 — 112:1:1 قُلْ / قول B008 — stick for striking the qillah

Initial image: a wooden implement used in a striking game.  
Visited: S112-ALL. Selected before freeze: `(E: قول B008 stick-object)` only.  
Generating set: قول B008.  
Frozen model: physical implement/strike scene.  
Predictions at freeze: striking instrument, target, game, or object manipulation.  
Unused features tested after freeze: all.  
Corroborators: none.  
Constraints: `(K: no stick, game, strike, target, or physical action appears)`.  
Rejected or terminated branches: صمد B006 also has striking, but no local target/instrument supports combining them.  
Rival forks: none.  
Final grade: unlikely.

### L09 — 112:1:1 قُلْ / قول B009 — negotiation in an affair

Initial image: المقاولة in a matter, reciprocal verbal dealing.  
Visited: S112-ALL. Selected before freeze: `(E: قول B009 negotiation)`, `(E: قول B001 speech substrate)` weakly.  
Generating set: قول B009.  
Frozen model: possible mutual deliberation.  
Predictions at freeze: reciprocal speakers, issue negotiation, or الأمر.  
Unused features tested after freeze: quoted complement and later predicates.  
Corroborators: none.  
Constraints: `(K: attachment 112:1 a1 is one-directional command plus quoted content)`, `(K: no reciprocal parties occur)`.  
Rejected or terminated branches: صمد B005 "أمر" neighbor lacks an actual أمر word and does not rescue the image.  
Rival forks: none.  
Final grade: weak — speech exists, reciprocity does not.

### L10 — 112:1:1 قُلْ / قول B010 — imposing judgment on another

Initial image: اقتالة الحكم على غيره.  
Visited: S112-ALL. Selected before freeze: `(E: قول B010 imposed-judgment)` only.  
Generating set: قول B010.  
Frozen model: arbitrary حكم image.  
Predictions at freeze: governed other, dispute, or imposed ruling.  
Unused features tested after freeze: identity quote and negations.  
Corroborators: none.  
Constraints: `(K: quoted content is declarative identity, not تحكم على غيره)`.  
Rejected or terminated branches: none complete the حكم scene.  
Rival forks: none.  
Final grade: unlikely.

### L11 — 112:1:1 قُلْ / قول B011 — saying as conjecture

Initial image: قول working like ظن.  
Visited: S112-ALL. Selected before freeze: `(E: قول B011 conjectural-saying)` only.  
Generating set: قول B011.  
Frozen model: uncertainty or ظن-like construal.  
Predictions at freeze: interrogative, uncertain complement, or ظن syntax.  
Unused features tested after freeze: quoted identity and negations.  
Corroborators: none.  
Constraints: `(K: قُلْ introduces asserted quote, not conjecture)`, `(K: no interrogative or ظن-governed syntax appears)`.  
Rejected or terminated branches: all later predicates are asserted/negated, not doubtful.  
Rival forks: none.  
Final grade: unlikely.

### L12 — 112:1:1 قُلْ / قول B012 — saying hidden in the self

Initial image: قول in the self before lexical emergence.  
Visited: S112-ALL. Selected before freeze: `(E: قول B012 hidden-inward saying)`, `(E: قول B001 outward saying)` as contrast.  
Generating set: قول B012 and contrastive B001.  
Frozen model: hidden content made overt by command.  
Predictions at freeze: quote-content should appear, but hiddenness itself should be constrained.  
Unused features tested after freeze: attachment 112:1 a1, visible words.  
Corroborators: `(C: attachment 112:1 a1 provides overt quote)` only as a contrastive fulfillment.  
Constraints: `(K: the actual occurrence is outward imperative قُلْ)`, `(K: no private-speech marker remains after the quote opens)`.  
Rejected or terminated branches: no content branch supplies inward secrecy.  
Rival forks: B006 inward-drawn saying.  
Final grade: weak — it explains an outwarding transition only by contrast, not as the main model.

### L13 — 112:1:1 قُلْ / قول B013 — saying as belief or doctrine

Initial image: قول as اعتقاد ومذهب.  
Visited: S112-ALL. Selected before freeze: `(E: قول B013 belief/doctrinal saying)`, `(E: قول B001 spoken form)`, `(E: ءله B002 divine name)`, `(E: ءحد B001 unity predicate)`, `(E: صمد B001 reliance predicate)`.  
Generating set: قول B013; قول B001; ءله B002; ءحد B001; صمد B001.  
Frozen model: a spoken declaration with doctrinal content geometry.  
Predictions at freeze: later units should protect the doctrinal content against incompatible relations.  
Unused features tested after freeze: ولد active/passive, كون, كفء, final أحد.  
Corroborators: `(C: ولد B003 active/passive denied)`, `(C: ولد B005 derivation denied)`, `(C: كفء B001 denied)`, `(C: ءحد B002 final universal denial)`.  
Constraints: `(K: occurrence is still imperative speech; "belief/doctrine" is secondary, not the primary local lexical value)`.  
Rejected or terminated branches: قول B011 conjecture rejected; قول B005 false attribution rejected.  
Rival forks: definition-like B016.  
Final grade: medium — coherent passage-scale content, but seed branch is less immediate than B001.

### L14 — 112:1:1 قُلْ / قول B014 — a thing saying by indication

Initial image: قول as دلالة الشيء.  
Visited: S112-ALL. Selected before freeze: `(E: قول B014 indication)`, `(E: ءحد B001)`, `(E: صمد B001)` as indicated predicates.  
Generating set: قول B014; ءحد B001; صمد B001.  
Frozen model: the utterance acts like a sign delimiting the referent.  
Predictions at freeze: later features should add boundary conditions.  
Unused features tested after freeze: ولد, كفء, final أحد.  
Corroborators: `(C: كفء B001 denied boundary)`, `(C: ولد B003/B005 denied origin boundary)`.  
Constraints: `(K: the local event is direct speech command, not nonverbal indication)`.  
Rejected or terminated branches: B016 is the stronger delimiting branch.  
Rival forks: B016 definition fork.  
Final grade: weak — compatible with delimitation, but branch-specific indication is remote.

### L15 — 112:1:1 قُلْ / قول B015 — sincere concern for a thing

Initial image: عناية صادقة بالشيء.  
Visited: S112-ALL. Selected before freeze: `(E: قول B015 concern/care)`, `(E: قول B001 speech substrate)` weakly.  
Generating set: قول B015.  
Frozen model: a careful, earnest utterance.  
Predictions at freeze: repeated attention or care-markers.  
Unused features tested after freeze: repeated name and closure.  
Corroborators: `(C: repetition 112:1-2 ٱللَّهُ)` weakly fits focus.  
Constraints: `(K: no explicit عناية construction or care-object syntax occurs)`.  
Rejected or terminated branches: صمد B005 care-over-affair is a tempting fork but lacks أمر.  
Rival forks: none.  
Final grade: weak.

### L16 — 112:1:1 قُلْ / قول B016 — saying as definition/boundary

Initial image: قول as حدّ.  
Visited: S112-ALL. Selected before freeze: `(E: قول B016 definition)`, `(E: attachment 112:1 a1 quote)`, `(E: ءله B002 name)`, `(E: ءحد B001 positive unity)`, `(E: صمد B001 support/reliance)`, secondary `(E: صمد B002 self-containedness)`.  
Generating set: قول B016; quote attachment; ءله B002; ءحد B001; صمد B001/B002.  
Frozen model: a compact definition-like utterance: named referent + positive predicate + self-standing support predicate.  
Predictions at freeze: the rest should supply boundary exclusions: no offspring, no origin, no equal.  
Unused features tested after freeze: ولد active/passive, كون, كفء, final أحد, negation wave.  
Corroborators: `(C: ولد B003 after-freeze, birth boundary denied both directions)`, `(C: ولد B005 after-freeze, derivation denied)`, `(C: كون B001 after-freeze, occurrence of equal denied)`, `(C: كفء B001 after-freeze, counterpart denied)`, `(C: ءحد B002 after-freeze, final no-any-one closure)`.  
Constraints: `(K: specialized logical "definition" is not the primary surface value of قُلْ)`.  
Rejected or terminated branches: literal صمد B003-B006 rejected; قول B005/B011 false/conjecture defeated.  
Rival forks: B014 indication, B013 doctrine; both converge as weaker variants.  
Final grade: medium-strong — the passage behaves like a boundary-definition, although the branch is semantically secondary.

### L17 — 112:1:3 ٱللَّهُ / ءله B001 — worshipped referent

Initial image: المعبود / object of تأله.  
Visited: S112-ALL. Selected before freeze: `(E: ءله B001 worshipped/divine referent)`, `(E: attachment 112:1 a3 apposition to هو)`, `(E: ءحد B001 predicate)`, `(E: صمد B001 intended/reliable support)`.  
Generating set: ءله B001; apposition/predication; ءحد B001; صمد B001.  
Frozen model: the pronoun’s referent is the divine object/referent, marked one and reliable.  
Predictions at freeze: later text should prevent divine relation from being shared by lineage or equal counterpart.  
Unused features tested after freeze: second ٱللَّهُ, ولد pair, final كفء/أحد, basmala.  
Corroborators: `(C: repeated 112:2 ٱللَّهُ)`, `(C: ولد B003/B005 denied)`, `(C: كفء B001 denied)`, `(C: basmala opening-context divine name)`.  
Constraints: `(K: no act of worship is narrated; تعبّد remains background to the Name, not a ritual event)`.  
Rejected or terminated branches: ءله B002 name-formula is a competing seed, not double-counted here.  
Rival forks: B002 name-disclosure stronger for this occurrence’s form.  
Final grade: medium-strong.

### L18 — 112:1:3 ٱللَّهُ / ءله B002 — divine Name in a spoken formula

Initial image: the Name `ٱللَّهُ` appears inside the commanded quote.  
Visited: S112-ALL. Selected before freeze: `(E: ءله B002 divine-name use)`, `(E: قول B001 command-to-say)`, `(E: attachment 112:1 a1 quote)`, `(E: ءحد B001 predicate)`.  
Generating set: ءله B002; قول B001; quoted complement; ءحد B001.  
Frozen model: speech-command discloses the divine Name with unity predicate.  
Predictions at freeze: the Name may be refreshed and then protected against incompatible relations.  
Unused features tested after freeze: 112:2 ٱللَّهُ, الصمد, ولد pair, final كفء/أحد, basmala.  
Corroborators: `(C: 112:2 repetition of ٱللَّهُ)`, `(C: صمد B001 second predicate)`, `(C: ولد B003 denied)`, `(C: كفء B001 denied)`, `(C: basmala opening-context)`.  
Constraints: `(K: no oath or vocative syntax; B002 contributes Name-use, not those formula examples)`.  
Rejected or terminated branches: ءله B001 worship relation only corroborates divine referent if unused.  
Rival forks: none.  
Final grade: strong.

### L19 — 112:1:4 أَحَدٌ / ءحد B001 — positive unity predicate

Initial image: الأَحَدِيَّة والوَحْدَة predicated of `ٱللَّهُ`.  
Visited: S112-ALL. Selected before freeze: `(E: ءحد B001 unity)`, `(E: attachment 112:1 a2 predication)`, `(E: ءله B002 named subject)`, `(E: صمد B001 support/reliance)`, optional secondary `(E: صمد B002 self-containedness)`.  
Generating set: ءحد B001; predication; ءله B002; صمد B001/B002.  
Frozen model: a named one, then a self-standing/support center.  
Predictions at freeze: subsequent material should block plurality, derivation, dependent origin, and comparable counterpart.  
Unused features tested after freeze: ولد active/passive, كون, كفء, final أحد, triple لم.  
Corroborators: `(C: ولد B003 active/passive denied)`, `(C: ولد B005 generated-from denied)`, `(C: كفء B001 equality denied)`, `(C: ءحد B002 final negative-scope reactivation)`, `(C: sequence first أحد→final أحد)`.  
Constraints: `(K: first أَحَدٌ is positive nominative predicate, not negative-scope use)`.  
Rejected or terminated branches: ءحد B003-B006 fail as counting/ordinal/mountain; صمد literal rock/stoppers not primary.  
Rival forks: صمد B001 relational support and صمد B002 self-contained density converge.  
Final grade: strong.

### L20 — 112:1:4 أَحَدٌ / ءحد B002 — negative-scope one attempted from positive occurrence

Initial image: أحد under negation with exhaustive scope.  
Visited: S112-ALL. Selected before freeze: `(E: ءحد B002 negative-scope seed)` only, held as an unresolved possibility because the occurrence is positive.  
Generating set: ءحد B002.  
Frozen model: negative-exhaustive branch waits for a negated environment.  
Predictions at freeze: a later `أحد` under negation would reactivate this branch.  
Unused features tested after freeze: final `أحد` in `وَلَمْ يَكُن ... أَحَدٌ`.  
Corroborators: `(C: 112:4 final ءحد B002 exact negative-scope occurrence)`, `(C: كفء B001 equality denied in that clause)`.  
Constraints: `(K: 112:1:4 occurrence itself is positive predicate by attachment 112:1 a2)`.  
Rejected or terminated branches: cannot build from 112:1 alone.  
Rival forks: final occurrence L58 is the valid seed.  
Final grade: weak — real only as anticipatory reactivation; local seed occurrence constrains it.

### L21 — 112:1:4 أَحَدٌ / ءحد B003 — counting/composition

Initial image: one as count or compound numeral.  
Visited: S112-ALL. Selected before freeze: `(E: ءحد B003 counting)` only.  
Generating set: ءحد B003.  
Frozen model: numeric counting scene.  
Predictions at freeze: numerals, composition with عشر, counted objects.  
Unused features tested after freeze: all.  
Corroborators: none.  
Constraints: `(K: no counting or numeral-compound syntax appears)`, `(K: أَحَدٌ is a predicate, not count operator)`.  
Rejected or terminated branches: final أحد recurrence is not numerical.  
Rival forks: none.  
Final grade: unlikely.

### L22 — 112:1:4 أَحَدٌ / ءحد B004 — first/addition/day-name

Initial image: firstness in إضافة or the day-name.  
Visited: S112-ALL. Selected before freeze: `(E: ءحد B004 first/addition)` only.  
Generating set: ءحد B004.  
Frozen model: ordinal/additive image.  
Predictions at freeze: إضافة construction, أول-like sequence, or day cue.  
Unused features tested after freeze: all.  
Corroborators: none.  
Constraints: `(K: no إضافة or calendrical construction occurs)`.  
Rejected or terminated branches: sequence position alone does not supply ordinal semantics.  
Rival forks: none.  
Final grade: unlikely.

### L23 — 112:1:4 أَحَدٌ / ءحد B005 — solitary individuality

Initial image: الانفراد والتفرق آحادا.  
Visited: S112-ALL. Selected before freeze: `(E: ءحد B005 solitary individuality)`, `(E: ءحد B001 unity-neighbor)`, `(E: صمد B001)` weakly.  
Generating set: ءحد B005 with B001 as adjacent unity, صمد B001 as support center.  
Frozen model: one standing without partner or distributed peer.  
Predictions at freeze: later text should reject companion/equal relations.  
Unused features tested after freeze: ولد pair, كفء, final أحد.  
Corroborators: `(C: كفء B001 equality denied)`, `(C: final ءحد B002 no-any-one)`, `(C: ولد B003 lineage denied)`.  
Constraints: `(K: no آحادا/distributive plural construction; B005 is secondary to B001)`.  
Rejected or terminated branches: ءحد B003/B004/B006.  
Rival forks: B001 stronger positive predicate.  
Final grade: medium.

### L24 — 112:1:4 أَحَدٌ / ءحد B006 — Mount Uḥud

Initial image: proper mountain name.  
Visited: S112-ALL. Selected before freeze: `(E: ءحد B006 mountain-name)` only.  
Generating set: ءحد B006.  
Frozen model: geographic proper-name image.  
Predictions at freeze: place, mountain, or Medina cue.  
Unused features tested after freeze: all.  
Corroborators: none.  
Constraints: `(K: no place, mountain, or المدينة cue appears)`.  
Rejected or terminated branches: no other root supplies geography.  
Rival forks: none.  
Final grade: unlikely.

### L25 — 112:2:1 ٱللَّهُ / ءله B001 — repeated worshipped/divine referent

Initial image: the divine referent is named again at the start of the second ayah.  
Visited: S112-ALL. Selected before freeze: `(E: ءله B001 worshipped/divine referent)`, `(E: repetition of ٱللَّهُ)`, `(E: صمد B001 predicate)`, `(E: ءحد B001 prior-state reactivation)`.  
Generating set: ءله B001; name repetition; صمد B001; prior ءحد B001.  
Frozen model: the same referent is refreshed, then marked الصمد.  
Predictions at freeze: later negations should protect this referent from lineage and equal.  
Unused features tested after freeze: ولد pair, كون, كفء, final أحد.  
Corroborators: `(C: ولد B003/B005 denied)`, `(C: كفء B001 denied)`, `(C: final ءحد B002)`.  
Constraints: `(K: no explicit act of worship is narrated)`.  
Rejected or terminated branches: not oath/vocative.  
Rival forks: B002 Name-use stronger for repetition.  
Final grade: medium-strong.

### L26 — 112:2:1 ٱللَّهُ / ءله B002 — Name reactivation before الصمد

Initial image: the divine Name is repeated as a fresh subject.  
Visited: S112-ALL. Selected before freeze: `(E: ءله B002 divine Name)`, `(E: sequence repetition 112:1→112:2)`, `(E: صمد B001 second predicate)`.  
Generating set: ءله B002; repetition; صمد B001.  
Frozen model: re-naming reactivates the same referent before a new predicate.  
Predictions at freeze: following 3MS forms and له should continue the same referent.  
Unused features tested after freeze: يلد/يولد/يكن/له, final كفء/أحد.  
Corroborators: `(C: 3MS verbs يلد، يولد، يكن continue the referent)`, `(C: له in 112:4 points back)`, `(C: كفء B001 denied for Him)`.  
Constraints: `(K: B002 contributes Name-use but not oath/vocative syntax)`.  
Rejected or terminated branches: ءله B001 worship relation not used before freeze here.  
Rival forks: none.  
Final grade: strong.

### L27 — 112:2:2 ٱلصَّمَدُ / صمد B001 — intended, relied-upon support

Initial image: القصد إلى المعتمد المقصود.  
Visited: S112-ALL. Selected before freeze: `(E: صمد B001 intended/reliable support)`, `(E: attachment 112:2 a1 predication)`, `(E: ءله B002 repeated Name)`, `(E: ءحد B001 prior unity)`.  
Generating set: صمد B001; predication; ءله B002; ءحد B001.  
Frozen model: the named one is a single support-center / relied-upon referent.  
Predictions at freeze: a true support-center should not be downstream of parents, offspring, generation, or equivalent counterpart.  
Unused features tested after freeze: ولد active/passive, كون, كفء, final أحد.  
Corroborators: `(C: ولد B002/B003 parent/birth relation denied)`, `(C: ولد B005 generated-from relation denied)`, `(C: كون B001 equal-occurrence denied)`, `(C: كفء B001 equal denied)`, `(C: final ءحد B002)`.  
Constraints: `(K: no حاجات or request scene is explicit; the branch contributes support/reliance geometry, not a supplication narrative)`.  
Rejected or terminated branches: literal branches B003-B006 rejected unless as failed forks; B002/B007 secondary.  
Rival forks: صمد B002 dense/no-hollow and B007 permanence converge secondarily.  
Final grade: strong.

### L28 — 112:2:2 ٱلصَّمَدُ / صمد B002 — compact, solid, without hollow

Initial image: الصلابة المكتنزة بلا جوف.  
Visited: S112-ALL. Selected before freeze: `(E: صمد B002 no-hollow compactness)`, `(E: ءحد B001 unity)`, `(E: ءله B002 Name)`, optional `(E: صمد B007 permanence)`.  
Generating set: صمد B002; ءحد B001; ءله B002; optional B007.  
Frozen model: self-contained, non-hollow unity as a secondary simulation under the predicate الصمد.  
Predictions at freeze: no opening into birth/production; no origin from another; no peer.  
Unused features tested after freeze: ولد active/passive, كفء, final أحد.  
Corroborators: `(C: ولد B003 active/passive birth denied)`, `(C: ولد B005 derivation denied)`, `(C: كفء B001 denied)`, `(C: triple لم closure wave)`.  
Constraints: `(K: no literal body, rock, place, or cavity is asserted; الصمد remains predicate of ٱللَّهُ)`.  
Rejected or terminated branches: B003 stopper is a more object-specific fork and remains weak.  
Rival forks: B001 support fork primary.  
Final grade: medium-strong.

### L29 — 112:2:2 ٱلصَّمَدُ / صمد B003 — sealed stopper

Initial image: سدادة القارورة المحكمة.  
Visited: S112-ALL. Selected before freeze: `(E: صمد B003 stopper/seal)`, with weak support `(E: صمد B002 closed/no-hollow neighbor)`.  
Generating set: صمد B003; weak صمد B002.  
Frozen model: closure of an opening.  
Predictions at freeze: outgoing/incoming production should be blocked.  
Unused features tested after freeze: ولد pair, final equality denial.  
Corroborators: `(C: ولد B003 denied in both active/passive directions)` weakly.  
Constraints: `(K: no bottle, stopper, container, or عفاص role occurs)`.  
Rejected or terminated branches: cannot literalize الصمد as a physical stopper.  
Rival forks: collapses into B002 if retained.  
Final grade: weak.

### L30 — 112:2:2 ٱلصَّمَدُ / صمد B004 — head binding

Initial image: تصميد الرأس بخرقة.  
Visited: S112-ALL. Selected before freeze: `(E: صمد B004 head-binding)` only.  
Generating set: صمد B004.  
Frozen model: wrapping/bandage scene.  
Predictions at freeze: head, cloth, binding, injury/covering.  
Unused features tested after freeze: all.  
Corroborators: none.  
Constraints: `(K: no head, cloth, wrapping, wound, or bandage participant occurs)`.  
Rejected or terminated branches: no other root supplies these roles.  
Rival forks: none.  
Final grade: unlikely.

### L31 — 112:2:2 ٱلصَّمَدُ / صمد B005 — overseeing an affair with concern

Initial image: الإشراف على الأمر مع الحفل به.  
Visited: S112-ALL. Selected before freeze: `(E: صمد B005 oversight/care-over-affair)`, weak `(E: قول B015 concern)` tested as fork.  
Generating set: صمد B005; weak قول B015.  
Frozen model: concerned oversight.  
Predictions at freeze: أمر, managed matter, or explicit care.  
Unused features tested after freeze: ولد/كفء negations.  
Corroborators: none specific.  
Constraints: `(K: no أمر or oversight construction occurs)`, `(K: later lines exclude relations rather than describe supervision)`.  
Rejected or terminated branches: قول B015 does not rescue the scene.  
Rival forks: none.  
Final grade: weak.

### L32 — 112:2:2 ٱلصَّمَدُ / صمد B006 — striking with a stick

Initial image: صمده بالعصا.  
Visited: S112-ALL. Selected before freeze: `(E: صمد B006 striking)` only.  
Generating set: صمد B006.  
Frozen model: blow/impact scene.  
Predictions at freeze: striker, stick, target, hit result.  
Unused features tested after freeze: all.  
Corroborators: none.  
Constraints: `(K: no ضرب, عصا, target, or violence syntax appears)`.  
Rejected or terminated branches: قول B008 stick branch lacks shared passage roles and is also rejected.  
Rival forks: none.  
Final grade: unlikely.

### L33 — 112:2:2 ٱلصَّمَدُ / صمد B007 — permanence under severity

Initial image: الدوام والبقاء على الشدة.  
Visited: S112-ALL. Selected before freeze: `(E: صمد B007 endurance/permanence)`, `(E: صمد B001 support)`, `(E: ءحد B001 unity)`.  
Generating set: صمد B007; صمد B001; ءحد B001.  
Frozen model: one stable referent remaining, not weakened by relational dependence.  
Predictions at freeze: later clauses should deny temporal/originating dependence and counterpart.  
Unused features tested after freeze: ولد passive, كون, كفء, final أحد.  
Corroborators: `(C: ولد B005 generated-from denied)`, `(C: كون B001 no occurrence of equal)`, `(C: كفء B001 denied)`.  
Constraints: `(K: no cold/drought/severity scene occurs; permanence is abstracted from branch image)`.  
Rejected or terminated branches: literal animal/environment details rejected.  
Rival forks: supports B001/B002 but does not replace them.  
Final grade: medium.

### L34 — 112:3:2 يَلِدْ / ولد B001 — offspring/product role, active negation

Initial image: مولود من نسل as possible product of the referent.  
Visited: S112-ALL. Selected before freeze: `(E: ولد B001 offspring/product)`, `(E: ولد B003 birth-event)`, `(E: attachment 112:3 a1 negated active)`, `(E: ءحد B001 prior unity)`.  
Generating set: ولد B001/B003; negated active attachment; prior unity.  
Frozen model: no offspring/product proceeds from the named one.  
Predictions at freeze: passive counterpart should deny being offspring; final should deny equal.  
Unused features tested after freeze: يُولَدْ passive, كون, كفء, final أحد.  
Corroborators: `(C: attachment 112:3 a2/a3 passive coordination)`, `(C: ولد B002 parent-role implication denied)`, `(C: كفء B001 denied)`, `(C: ءحد B002 final no-any-one)`.  
Constraints: `(K: child/product role is only raised under negation; no child exists in the model)`.  
Rejected or terminated branches: ولد B004 newborn/slave not selected; B006 peer only later weak.  
Rival forks: ولد B005 causal generation.  
Final grade: strong.

### L35 — 112:3:2 يَلِدْ / ولد B002 — parent roles blocked

Initial image: الوالد/الوالدة role implied by birth relation.  
Visited: S112-ALL. Selected before freeze: `(E: ولد B002 parent-role)`, `(E: ولد B003 birth-event)`, `(E: attachment 112:3 a1 لم يلد)`.  
Generating set: ولد B002/B003; active negation.  
Frozen model: no parent-role attaches to the named referent through active begetting/birth.  
Predictions at freeze: passive should block parents over Him; final should block peers.  
Unused features tested after freeze: يُولَدْ, كفء, final أحد.  
Corroborators: `(C: passive ولد B003 denied)`, `(C: كفء B001 denied)`, `(C: ءحد B002 final)`.  
Constraints: `(K: no والد noun appears; role is inferred from يلد and remains negated)`.  
Rejected or terminated branches: B004/B006 not active here.  
Rival forks: B001/B003 stronger.  
Final grade: medium-strong.

### L36 — 112:3:2 يَلِدْ / ولد B003 — birth-event gate closed outward

Initial image: حدوث الولادة ووضع الحمل.  
Visited: S112-ALL. Selected before freeze: `(E: ولد B003 birth-event)`, `(E: attachment 112:3 a1 negated active)`, `(E: attachment 112:3 a2 coordination expectation)`.  
Generating set: ولد B003; active negation; coordination expectation.  
Frozen model: the outward birth-event path is closed.  
Predictions at freeze: the next coordinated passive should close the inward path; final should move to equality denial.  
Unused features tested after freeze: يُولَدْ passive, كون, كفء, final أحد.  
Corroborators: `(C: passive ولد B003 in 112:3:4)`, `(C: كون B001 in final negated copula)`, `(C: كفء B001 denied)`, `(C: ءحد B002 delayed subject)`.  
Constraints: `(K: morphology is negated jussive; no birth event is asserted)`.  
Rejected or terminated branches: B004 newborn noun not active; B005 is broader fork.  
Rival forks: B005 generated-from abstraction.  
Final grade: strong.

### L37 — 112:3:2 يَلِدْ / ولد B004 — newborn or owned young

Initial image: الوليد / close-to-birth child or slave.  
Visited: S112-ALL. Selected before freeze: `(E: ولد B004 newborn/slave)` only.  
Generating set: ولد B004.  
Frozen model: young/owned-child image.  
Predictions at freeze: الوليد/وليدة noun, young person, or ownership role.  
Unused features tested after freeze: all.  
Corroborators: none.  
Constraints: `(K: occurrence is a verb under negation, not وليد noun)`, `(K: no ownership/slavery relation occurs)`.  
Rejected or terminated branches: no other root completes this image.  
Rival forks: none.  
Final grade: unlikely.

### L38 — 112:3:2 يَلِدْ / ولد B005 — generated effect blocked outward

Initial image: شيء حاصل عن شيء أو مستحدث منه.  
Visited: S112-ALL. Selected before freeze: `(E: ولد B005 generated-from relation)`, `(E: ولد B003 active birth-event as local form)`, `(E: ءحد B001 prior unity)`, `(E: صمد B001/B002 self-standing support)`.  
Generating set: ولد B005/B003; prior unity; ṣamad self-standing/support.  
Frozen model: no generated derivative comes out from the named one.  
Predictions at freeze: passive should deny His derivation from another; equality should be denied.  
Unused features tested after freeze: يُولَدْ, كفء, final أحد.  
Corroborators: `(C: passive ولد B005 dimension in يُولَدْ)`, `(C: كفء B001 denied)`, `(C: ءحد B002 final)`.  
Constraints: `(K: B005 is broader than the verb; B003 remains the immediate local branch)`.  
Rejected or terminated branches: B004/B006 not used.  
Rival forks: biological B003 and causal B005 converge.  
Final grade: medium-strong.

### L39 — 112:3:2 يَلِدْ / ولد B006 — same-age peer

Initial image: اللدة / peer in age.  
Visited: S112-ALL. Selected before freeze: `(E: ولد B006 age-peer)` only, with `كفء B001` reserved for after-freeze because it appears later.  
Generating set: ولد B006.  
Frozen model: peerhood by birth-time.  
Predictions at freeze: later equal/peer denial may appear.  
Unused features tested after freeze: final كفء and أحد.  
Corroborators: `(C: كفء B001 denies equality/peerhood)` weakly.  
Constraints: `(K: no لدة form or age-comparison occurs)`, `(K: يلد is active verb, not peer noun)`.  
Rejected or terminated branches: no local peer construction before final.  
Rival forks: final equality model.  
Final grade: weak.

### L40 — 112:3:4 يُولَدْ / ولد B001 — offspring/product role, passive negation

Initial image: a مولود من نسل role applied to the referent, immediately negated.  
Visited: S112-ALL. Selected before freeze: `(E: ولد B001 offspring/product)`, `(E: ولد B003 passive birth-event)`, `(E: attachment 112:3 a3 negated passive)`, `(E: attachment 112:3 a2 coordination with يلد)`.  
Generating set: ولد B001/B003; passive negation; coordination.  
Frozen model: the named referent is not produced as offspring.  
Predictions at freeze: final clause should deny equivalent counterpart after lineage is closed both ways.  
Unused features tested after freeze: كون, كفء, final أحد.  
Corroborators: `(C: كفء B001 denied)`, `(C: كون B001 no occurrence of equal)`, `(C: ءحد B002 final exhaustive subject)`.  
Constraints: `(K: passive offspring role is negated, not asserted)`.  
Rejected or terminated branches: B004 not a noun occurrence.  
Rival forks: B005 derivation.  
Final grade: strong.

### L41 — 112:3:4 يُولَدْ / ولد B002 — parent-source over Him denied

Initial image: parents implied if passive birth were true.  
Visited: S112-ALL. Selected before freeze: `(E: ولد B002 parent-source role)`, `(E: ولد B003 passive birth-event)`, `(E: passive negated morphology)`.  
Generating set: ولد B002/B003; passive negation.  
Frozen model: no parent-source relation over the named referent.  
Predictions at freeze: no comparable counterpart remains.  
Unused features tested after freeze: كفء, final أحد.  
Corroborators: `(C: كفء B001 denied)`, `(C: ءحد B002 final)`.  
Constraints: `(K: والد/والدة nouns are absent; role is inferred and negated)`.  
Rejected or terminated branches: B004/B006 not selected.  
Rival forks: B001/B003 stronger.  
Final grade: medium-strong.

### L42 — 112:3:4 يُولَدْ / ولد B003 — birth-event gate closed inward

Initial image: حدوث الولادة as passive relation.  
Visited: S112-ALL. Selected before freeze: `(E: ولد B003 birth-event)`, `(E: attachment 112:3 a2 coordination)`, `(E: attachment 112:3 a3 negated passive)`.  
Generating set: ولد B003; passive negation; coordination.  
Frozen model: after no outgoing birth, no incoming birth/origin either.  
Predictions at freeze: the next layer should deny peer/equal occurrence.  
Unused features tested after freeze: كون, كفء, final أحد.  
Corroborators: `(C: كون B001 negated occurrence)`, `(C: كفء B001 equality denied)`, `(C: ءحد B002 no-any-one subject)`.  
Constraints: `(K: no actual birth event occurs; closure is relational)`.  
Rejected or terminated branches: B004 newborn noun absent.  
Rival forks: B005 generated-from abstraction.  
Final grade: strong.

### L43 — 112:3:4 يُولَدْ / ولد B004 — newborn/young/slave as passive seed

Initial image: الوليد or الوليدة.  
Visited: S112-ALL. Selected before freeze: `(E: ولد B004 newborn/slave)` only.  
Generating set: ولد B004.  
Frozen model: newborn/owned-young image.  
Predictions at freeze: a noun for newborn/young/slave or ownership relation.  
Unused features tested after freeze: all.  
Corroborators: none.  
Constraints: `(K: occurrence is passive verb يُولَدْ under negation, not وليد/وليدة)`, `(K: no ownership role)`.  
Rejected or terminated branches: no root completes.  
Rival forks: none.  
Final grade: unlikely.

### L44 — 112:3:4 يُولَدْ / ولد B005 — generated-from relation denied inward

Initial image: something arising from something else, now denied of the referent.  
Visited: S112-ALL. Selected before freeze: `(E: ولد B005 generated-from relation)`, `(E: passive negated morphology)`, `(E: صمد B001/B002 prior support/self-containedness)` as reactivated background.  
Generating set: ولد B005; passive negation; prior ṣamad.  
Frozen model: the named referent is not an effect or derivative from another source.  
Predictions at freeze: equality/counterpart should be denied next.  
Unused features tested after freeze: كون, كفء, final أحد.  
Corroborators: `(C: كفء B001 denied)`, `(C: كون B001 no occurrence)`, `(C: ءحد B002 final)`, `(C: صمد B007 permanence dimension if unused)`.  
Constraints: `(K: broad causal image is subordinate to the passive birth form)`.  
Rejected or terminated branches: B004/B006 not selected.  
Rival forks: biological B003 and causal B005 converge.  
Final grade: medium-strong.

### L45 — 112:3:4 يُولَدْ / ولد B006 — age-peer from passive birth

Initial image: peer of same birth-time.  
Visited: S112-ALL. Selected before freeze: `(E: ولد B006 age-peer)` only.  
Generating set: ولد B006.  
Frozen model: peerhood possibility linked to birth-time.  
Predictions at freeze: final equality denial might match.  
Unused features tested after freeze: كفء, final أحد.  
Corroborators: `(C: كفء B001 denies equal/peer)` weakly.  
Constraints: `(K: no لدة or age-pair construction)`, `(K: passive يولد is not a peer noun)`.  
Rejected or terminated branches: none complete.  
Rival forks: equality model.  
Final grade: weak.

### L46 — 112:4:2 يَكُن / كون B001 — no occurrence/existence of an equal

Initial image: وقوع الشيء وحضوره في زمان, here under negated كان.  
Visited: S112-ALL. Selected before freeze: `(E: كون B001 occurrence/existence)`, `(E: attachment 112:4 a1 negated jussive)`, `(E: كفء B001 equal/counterpart predicate)`, `(E: attachment 112:4 a3 kana_predicate)`, `(E: ءحد B002 delayed subject under negation)`, `(E: attachment 112:4 a4 delayed subject)`.  
Generating set: كون B001; final clause attachments; كفء B001; ءحد B002.  
Frozen model: no one ever occurs/stands as a counterpart for Him.  
Predictions at freeze: the final أحد should reactivate first positive أحد.  
Unused features tested after freeze: first أحد, earlier ولد pair, ṣamad.  
Corroborators: `(C: first ءحد B001 reactivated)`, `(C: ولد B003 active/passive closure before equality denial)`, `(C: صمد B001/B002 prior self-standing support)`.  
Constraints: `(K: كون is copular support for the equality denial, not an independent event narrative)`.  
Rejected or terminated branches: كون B002-B006 not primary.  
Rival forks: B002 status/place fork.  
Final grade: strong.

### L47 — 112:4:2 يَكُن / كون B002 — no matching place/status

Initial image: مكان/مكانة/تمكن.  
Visited: S112-ALL. Selected before freeze: `(E: كون B002 status/standing)`, `(E: كفء B001 equal)`, `(E: attachment 112:4 a2 له complement)`, `(E: attachment 112:4 a3/a4 predicate-subject structure)`.  
Generating set: كون B002; كفء B001; final attachments.  
Frozen model: no one occupies an equal standing/place relative to Him.  
Predictions at freeze: final أحد should exhaust possible occupants of that standing.  
Unused features tested after freeze: first أحد and prior predicates.  
Corroborators: `(C: ءحد B002 final negative scope)`, `(C: first ءحد B001 positive unity)`.  
Constraints: `(K: no literal مكان/موضع noun occurs; status is inferred from equality syntax)`.  
Rejected or terminated branches: B001 is more exact to كان.  
Rival forks: B001 occurrence model primary.  
Final grade: medium.

### L48 — 112:4:2 يَكُن / كون B003 — caretaking/guaranteeing

Initial image: الكفالة والقيام على فلان.  
Visited: S112-ALL. Selected before freeze: `(E: كون B003 care/guarantee)` only.  
Generating set: كون B003.  
Frozen model: caretaker/guarantor relation.  
Predictions at freeze: dependent person, كفالة, قيام على.  
Unused features tested after freeze: final له/كفوا/أحد.  
Corroborators: none.  
Constraints: `(K: له is complement of كفء by attachment 112:4 a2, not a dependent of كفالة)`, `(K: no قيام/كفالة construction)`.  
Rejected or terminated branches: no cross-root support.  
Rival forks: none.  
Final grade: unlikely.

### L49 — 112:4:2 يَكُن / كون B004 — submission by الاستكانة

Initial image: خضوع بالاستكانة.  
Visited: S112-ALL. Selected before freeze: `(E: كون B004 submission)` only.  
Generating set: كون B004.  
Frozen model: humbling/submission scene.  
Predictions at freeze: خضوع, lowliness, submission relation.  
Unused features tested after freeze: final equality clause.  
Corroborators: none.  
Constraints: `(K: final line denies equality; it does not describe submission)`.  
Rejected or terminated branches: no other root supplies submission.  
Rival forks: none.  
Final grade: unlikely.

### L50 — 112:4:2 يَكُن / كون B005 — old man linked to "كنت"

Initial image: الكُنْتِيّ الشيخ.  
Visited: S112-ALL. Selected before freeze: `(E: كون B005 old-man/reminiscence branch)` only.  
Generating set: كون B005.  
Frozen model: aging-person image.  
Predictions at freeze: شيخ, age, "كنت في شبابي" texture.  
Unused features tested after freeze: all.  
Corroborators: none.  
Constraints: `(K: occurrence is يَكُن under لم, not كنت or an age/person noun)`.  
Rejected or terminated branches: no local complement.  
Rival forks: none.  
Final grade: unlikely.

### L51 — 112:4:2 يَكُن / كون B006 — bad state

Initial image: حالة السوء بكينة.  
Visited: S112-ALL. Selected before freeze: `(E: كون B006 bad-state)` only.  
Generating set: كون B006.  
Frozen model: bad-condition image.  
Predictions at freeze: سوء, بات, condition phrase.  
Unused features tested after freeze: final equality clause.  
Corroborators: none.  
Constraints: `(K: no سوء or bad-state predicate occurs; كُفُوًا is equality predicate)`.  
Rejected or terminated branches: no cross-root support.  
Rival forks: none.  
Final grade: unlikely.

### L52 — 112:4:4 كُفُوًا / كفء B001 — equal counterpart denied

Initial image: المماثلة والمقابلة بالمثل.  
Visited: S112-ALL. Selected before freeze: `(E: كفء B001 equality/counterpart)`, `(E: attachment 112:4 a2 له complement)`, `(E: attachment 112:4 a3 kana_predicate)`, `(E: كون B001 negated occurrence)`, `(E: ءحد B002 delayed subject)`.  
Generating set: كفء B001; final attachments; كون B001; ءحد B002.  
Frozen model: no counterpart equal to Him occurs.  
Predictions at freeze: first أحد should be reactivated; prior ولد negations should appear as already-closed routes to counterpart-like relation.  
Unused features tested after freeze/backward replay: first أحد, الصمد, ولد pair, repeated Name.  
Corroborators: `(C: first ءحد B001 positive unity reactivated)`, `(C: ولد B003 active/passive genealogy denial)`, `(C: صمد B001/B002 self-standing support)`, `(C: final word position of أحد)`.  
Constraints: `(K: equality is raised only to be denied)`.  
Rejected or terminated branches: كفء B002-B005 not selected except B005 as weak production fork elsewhere.  
Rival forks: none.  
Final grade: strong.

### L53 — 112:4:4 كُفُوًا / كفء B002 — tilting, flipping, turning aside

Initial image: الإمالة والقلب والصرف.  
Visited: S112-ALL. Selected before freeze: `(E: كفء B002 turning/tilting)` only.  
Generating set: كفء B002.  
Frozen model: inversion/diversion scene.  
Predictions at freeze: motion, turning, color-change, directional diversion.  
Unused features tested after freeze/backward replay: all.  
Corroborators: none.  
Constraints: `(K: كُفُوًا is an accusative predicate of يَكُن, not a turning verb or motion noun)`.  
Rejected or terminated branches: no root supplies physical inversion.  
Rival forks: none.  
Final grade: unlikely.

### L54 — 112:4:4 كُفُوًا / كفء B003 — rhyme discrepancy

Initial image: الإكفاء in poetry by differing rhymes/case.  
Visited: S112-ALL. Selected before freeze: `(E: كفء B003 rhyme-discrepancy)` only.  
Generating set: كفء B003.  
Frozen model: poetic/rhyme mismatch image.  
Predictions at freeze: poetry, قافية, or explicit sound discrepancy.  
Unused features tested after freeze/backward replay: recurrence of endings and أحد.  
Corroborators: none strong; sound recurrence does not equal قافية اختلاف.  
Constraints: `(K: no شعر or قافية construction occurs)`, `(K: final أحد recurrence is semantic/syntactic, not rhyme-discrepancy evidence)`.  
Rejected or terminated branches: no local poetic technical frame.  
Rival forks: temporal sound seed may be separate but not lexical B003.  
Final grade: unlikely.

### L55 — 112:4:4 كُفُوًا / كفء B004 — tent/back-panel

Initial image: كِفاء الخباء.  
Visited: S112-ALL. Selected before freeze: `(E: كفء B004 tent-panel)` only.  
Generating set: كفء B004.  
Frozen model: shelter-cloth/back-panel object.  
Predictions at freeze: tent, house, cloth panel, sewing.  
Unused features tested after freeze/backward replay: all.  
Corroborators: none.  
Constraints: `(K: no خباء, بيت, cloth, or shelter object occurs)`.  
Rejected or terminated branches: no cross-root support.  
Rival forks: none.  
Final grade: unlikely.

### L56 — 112:4:4 كُفُوًا / كفء B005 — yearly produce/offspring

Initial image: yearly produce/offspring of palms or camels.  
Visited: S112-ALL. Selected before freeze: `(E: كفء B005 yearly-produce/نتائج)` with weak backward fork `(E: ولد B005 generated thing)` only if constructing a production image.  
Generating set: كفء B005; weak ولد B005 fork.  
Frozen model: periodic production/offspring alternation.  
Predictions at freeze: نتاج, سنة, milk/wool/fruit, alternating production.  
Unused features tested after freeze/backward replay: ولد active/passive, final syntax.  
Corroborators: `(C: ولد B003/B005 negations)` weakly touch production.  
Constraints: `(K: final كُفُوًا is equality predicate by attachment 112:4 a3)`, `(K: no سنة, نتاج, نخل, إبل, لبن, وبر)`.  
Rejected or terminated branches: production fork terminated; B001 is exact branch.  
Rival forks: none stable.  
Final grade: weak.

### L57 — 112:4:5 أَحَدٌۢ / ءحد B001 — final unity word reactivates first unity

Initial image: الأَحَدِيَّة والوَحْدَة at the closing word.  
Visited: S112-ALL. Selected before freeze: `(E: ءحد B001 unity)`, `(E: كفء B001 equality predicate)`, `(E: كون B001 negated occurrence)`, `(E: attachment 112:4 a4 delayed subject)`.  
Generating set: ءحد B001; كفء B001; كون B001; final delayed-subject attachment.  
Frozen model: the passage closes on the same unity-root after denying an equal.  
Predictions at freeze: first positive أحد should be reactivated.  
Unused features tested after freeze/backward replay: first أحد, ولد pair, صمد.  
Corroborators: `(C: first ءحد B001 positive predicate)`, `(C: ولد B003 active/passive closure)`, `(C: صمد B001/B002 support/self-standing predicate)`, `(C: final word position)`.  
Constraints: `(K: local final syntax is negative-scope; B002 is more exact for the final occurrence)`.  
Rejected or terminated branches: B003-B006 fail.  
Rival forks: B002 stronger.  
Final grade: medium-strong.

### L58 — 112:4:5 أَحَدٌۢ / ءحد B002 — exhaustive negative-scope closure

Initial image: أحد in negation exhausts the class of anyone fit to be addressed/considered.  
Visited: S112-ALL. Selected before freeze: `(E: ءحد B002 negative-scope one)`, `(E: كفء B001 counterpart/equal)`, `(E: كون B001 negated occurrence)`, `(E: attachment 112:4 a3/a4 predicate and delayed subject)`, `(E: attachment 112:4 a2 له complement)`.  
Generating set: ءحد B002; كفء B001; كون B001; final attachments.  
Frozen model: no one whatsoever is كفء له.  
Predictions at freeze: this final no-any-one should retrospectively complete the first positive أحد.  
Unused features tested after freeze/backward replay: first أحد, الصمد, ولد pair, repeated name.  
Corroborators: `(C: first ءحد B001 positive unity reactivated)`, `(C: صمد B001/B002 self-standing support)`, `(C: ولد B003 active/passive genealogy denied before final universalization)`, `(C: ءله B002 repeated name keeps same referent)`.  
Constraints: `(K: no rival is introduced; equality is denied)`.  
Rejected or terminated branches: B003-B006 rejected; B001 contributes only as reactivated prior occurrence, not the local final branch.  
Rival forks: B001 closure fork subordinate.  
Final grade: strong.

### L59 — 112:4:5 أَحَدٌۢ / ءحد B003 — final counting one

Initial image: numeric one or compound count.  
Visited: S112-ALL. Selected before freeze: `(E: ءحد B003 counting)` only.  
Generating set: ءحد B003.  
Frozen model: counting scene.  
Predictions at freeze: counted objects or numeral composition.  
Unused features tested after freeze/backward replay: all.  
Corroborators: none.  
Constraints: `(K: final أحد is delayed subject of negated كان, not count syntax)`.  
Rejected or terminated branches: first أحد recurrence does not create a counting series.  
Rival forks: none.  
Final grade: unlikely.

### L60 — 112:4:5 أَحَدٌۢ / ءحد B004 — final first/addition/day-name

Initial image: first/additive أحد or Sunday.  
Visited: S112-ALL. Selected before freeze: `(E: ءحد B004 first/addition)` only.  
Generating set: ءحد B004.  
Frozen model: ordinal/day image.  
Predictions at freeze: إضافة, firstness marker, day cue.  
Unused features tested after freeze/backward replay: all.  
Corroborators: none.  
Constraints: `(K: no إضافة or day-name cue; final word is negative-scope subject)`.  
Rejected or terminated branches: none complete.  
Rival forks: none.  
Final grade: unlikely.

### L61 — 112:4:5 أَحَدٌۢ / ءحد B005 — no individual equal

Initial image: individual separation / آحادا.  
Visited: S112-ALL. Selected before freeze: `(E: ءحد B005 individual separateness)`, `(E: كفء B001 equal)`, `(E: كون B001 negated occurrence)`.  
Generating set: ءحد B005; كفء B001; كون B001.  
Frozen model: no separated individual can stand as equal for Him.  
Predictions at freeze: first unity and genealogy-denial should support the closure.  
Unused features tested after freeze/backward replay: first أحد, ولد pair, صمد.  
Corroborators: `(C: first ءحد B001)`, `(C: ولد B003 active/passive blocks lineage individuals)`, `(C: صمد B001 self-standing support)`.  
Constraints: `(K: no آحادا/distributive plural form; B002 is syntactically exact)`.  
Rejected or terminated branches: B003/B004/B006.  
Rival forks: B002 stronger.  
Final grade: medium.

### L62 — 112:4:5 أَحَدٌۢ / ءحد B006 — Mount Uḥud at closure

Initial image: proper mountain name.  
Visited: S112-ALL. Selected before freeze: `(E: ءحد B006 mountain-name)` only.  
Generating set: ءحد B006.  
Frozen model: geographic closure.  
Predictions at freeze: place or mountain cue.  
Unused features tested after freeze/backward replay: all.  
Corroborators: none.  
Constraints: `(K: no geography, mountain, or المدينة cue; final word is subject in a negated equality clause)`.  
Rejected or terminated branches: no cross-root support.  
Rival forks: none.  
Final grade: unlikely.

## Constructional, morphosyntactic, temporal, and acoustic seed passes

These are actual passage structures, not lexical branch-pair generation. They are included because the prompt requires construction, morphosyntax, temporal order, repetition, ayah boundary, and sound/recitation-state seeds when eligible.

### C01 — quoted-complement frame: `قُلْ` → `هُوَ ٱللَّهُ أَحَدٌ`

Initial image: a command opens quoted content.  
Visited: S112-ALL as lexical support only. Selected before freeze: `(E: attachment 112:1 a1 quoted_complement)`, `(E: قول B001)`, `(E: ءله B002)`, `(E: ءحد B001)`.  
Generating set: quote attachment; قول B001; ءله B002; ءحد B001.  
Frozen model: spoken disclosure of a named unity predicate.  
Predictions at freeze: subsequent ayahs should remain referentially tied to the quote.  
Unused tested: 112:2-4, pronouns, negations.  
Corroborators: `(C: repeated ٱللَّهُ in 112:2)`, `(C: 3MS verbs يلد/يولد/يكن)`, `(C: له complement in 112:4)`.  
Constraints: `(K: قُلْ is outside the predicate chain)`.  
Grade: strong.

### C02 — deictic-filling sequence: `هُوَ` → `ٱللَّهُ` → `أَحَدٌ`

Initial image: a pronoun is resolved by a Name and predicate.  
Visited: S112-ALL. Selected before freeze: `(E: attachment 112:1 a3 apposition)`, `(E: attachment 112:1 a2 predication)`, `(E: ءله B002)`, `(E: ءحد B001)`.  
Generating set: pronoun/name/predicate attachments.  
Frozen model: referent focus: هو is filled, named, and predicated as one.  
Predictions: later words should keep the same referent.  
Unused tested: repeated Name, 3MS verbs, له.  
Corroborators: `(C: 112:2 ٱللَّهُ)`, `(C: يلد/يولد/يكن 3MS continuity)`, `(C: له)`.  
Constraints: `(K: apposition row has medium confidence; predication is stronger)`.  
Grade: strong.

### C03 — two nominal predications across ayah boundary

Initial image: `ٱللَّهُ أَحَدٌ` followed by `ٱللَّهُ ٱلصَّمَدُ`.  
Visited: S112-ALL. Selected before freeze: `(E: ءله B002 repeated Name)`, `(E: ءحد B001)`, `(E: صمد B001)`, `(E: attachment 112:2 a1 predication)`.  
Frozen model: first predicate establishes unity; second thickens it as ṣamad.  
Predictions: following clauses should block dependence and counterpart.  
Unused tested: ولد pair, final equality clause.  
Corroborators: `(C: ولد B003/B005 denied)`, `(C: كفء B001 denied)`, `(C: ءحد B002 closure)`.  
Constraints: `(K: only supplied predicates are used; no added predicate)`.  
Grade: strong.

### C04 — repeated divine Name at ayah boundary

Initial image: `ٱللَّهُ` is not merely carried by pronoun; it is restated.  
Visited: S112-ALL. Selected: `(E: ءله B002)`, `(E: repetition 112:1→112:2)`, `(E: صمد B001)`.  
Frozen model: recitational refresh of the same referent before the second predicate.  
Predictions: later 3MS references remain linked.  
Unused tested: يلد/يولد/يكن/له.  
Corroborators: `(C: 3MS morphology)`, `(C: له final complement)`.  
Constraints: `(K: no oath/vocative reading)`.  
Grade: medium-strong.

### C05 — definiteness alternation

Initial image: definite Name and definite `ٱلصَّمَدُ` interact with indefinite `أَحَدٌ`, `كُفُوًا`, and final `أَحَدٌ`.  
Visited: S112-ALL. Selected: `(E: morphology definiteness)`, `(E: ءله B002)`, `(E: ءحد B001)`, `(E: صمد B001)`, `(E: كفء B001)`, `(E: ءحد B002 final)`.  
Frozen model: a definite named center is bounded by positive uniqueness, then by indefinite exhaustive denial.  
Predictions: the final indefinite should widen negation rather than name a specific rival.  
Unused tested: final negated copula.  
Corroborators: `(C: كون B001 under لم)`, `(C: attachment 112:4 a4 delayed subject)`.  
Constraints: `(K: definiteness supports but does not create lexical meanings)`.  
Grade: medium-strong.

### C06 — `الصمد` as hinge between positive identity and negative closures

Initial image: after `أحد`, `الصمد` creates a support/self-standing hinge.  
Visited: S112-ALL. Selected: `(E: صمد B001)`, `(E: صمد B002 secondary)`, `(E: ءحد B001)`.  
Frozen model: unity becomes a self-standing/support center before relational exclusions.  
Predictions: no birth, no origin, no equal.  
Unused tested: ولد pair, كفء.  
Corroborators: `(C: ولد B003/B005 denied)`, `(C: كفء B001 denied)`.  
Constraints: `(K: no literal body/rock/stopper asserted)`.  
Grade: strong.

### C07 — active negated birth clause `لَمْ يَلِدْ`

Initial image: outgoing generation is raised and denied.  
Visited: S112-ALL. Selected: `(E: attachment 112:3 a1)`, `(E: ولد B003)`, `(E: ولد B001/B002 role implications)`.  
Frozen model: no offspring/parent-role outward from the named referent.  
Predictions: passive counterpart should follow or be implied.  
Unused tested: `وَلَمْ يُولَدْ`, final equality.  
Corroborators: `(C: attachment 112:3 a2/a3 passive pair)`, `(C: كفء B001 denied later)`.  
Constraints: `(K: no actual birth event asserted)`.  
Grade: strong.

### C08 — passive negated birth clause `وَلَمْ يُولَدْ`

Initial image: incoming origin/birth is raised and denied.  
Visited: S112-ALL. Selected: `(E: attachment 112:3 a3)`, `(E: ولد B003)`, `(E: ولد B005)`.  
Frozen model: the named referent is not born/generated from another.  
Predictions: after both genealogy directions close, equality closes.  
Unused tested: 112:4 final clause.  
Corroborators: `(C: كفء B001)`, `(C: كون B001)`, `(C: ءحد B002)`.  
Constraints: `(K: passive relation is negated)`.  
Grade: strong.

### C09 — active/passive ولد pair as bidirectional gate

Initial image: two coordinated clauses close outgoing and incoming birth.  
Visited: S112-ALL. Selected: `(E: attachment 112:3 a1/a2/a3)`, `(E: ولد B003)`, `(E: ولد B005)`.  
Frozen model: birth/generation cannot move out from Him or into Him.  
Predictions: remaining relational threat is peer/equal.  
Unused tested: final `لم يكن له كفوا أحد`.  
Corroborators: `(C: كفء B001 equal denied)`, `(C: ءحد B002 universal subject)`.  
Constraints: `(K: pair is purely negative)`.  
Grade: strong.

### C10 — triple `لم` negation wave

Initial image: three negative gates: `لم يلد`, `ولم يولد`, `ولم يكن`.  
Visited: S112-ALL. Selected: `(E: morphology NEG/JUS repetition)`, `(E: ولد B003)`, `(E: كون B001)`, `(E: كفء B001)`.  
Frozen model: an exclusion wave moves from birth-out, to birth-in, to equal-existence.  
Predictions: final word should name the widest possible excluded subject.  
Unused tested: final أحد.  
Corroborators: `(C: ءحد B002 negative-scope final subject)`, `(C: word order delayed subject)`.  
Constraints: `(K: negation structure supplies sequencing, not new lexical senses)`.  
Grade: strong.

### C11 — final negated copula package

Initial image: `وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ`.  
Visited: S112-ALL. Selected: `(E: attachment 112:4 a1/a2/a3/a4)`, `(E: كون B001)`, `(E: كفء B001)`, `(E: ءحد B002)`.  
Frozen model: no one exists/occurs as equal for Him.  
Predictions: first `أحد` should return in memory.  
Unused tested: first أحد, الصمد, ولد pair.  
Corroborators: `(C: first ءحد B001)`, `(C: صمد B001/B002)`, `(C: ولد B003 pair)`.  
Constraints: `(K: equality is denied, not asserted)`.  
Grade: strong.

### C12 — `لَّهُۥ` as complement of `كُفُوًا`

Initial image: the final equality relation is explicitly "for Him / to Him."  
Visited: S112-ALL. Selected: `(E: attachment 112:4 a2 prep_complement)`, `(E: كفء B001)`, `(E: ءله B002 repeated referent continuity)`.  
Frozen model: equality is measured relative to the same named referent.  
Predictions: previous references should all point to the same subject.  
Unused tested: earlier `ٱللَّهُ`, 3MS verbs.  
Corroborators: `(C: repeated ٱللَّهُ)`, `(C: 3MS verbal morphology)`.  
Constraints: `(K: له is not a separate possession scene; it binds the equality predicate)`.  
Grade: medium-strong.

### C13 — delayed final subject `أَحَدٌ`

Initial image: subject is delayed until the closing word.  
Visited: S112-ALL. Selected: `(E: attachment 112:4 a4 delayed subject)`, `(E: ءحد B002)`, `(E: كفء B001)`.  
Frozen model: the final word arrives as the widest excluded subject.  
Predictions: the first `أحد` should be reactivated at closure.  
Unused tested: 112:1:4.  
Corroborators: `(C: first ءحد B001)`, `(C: sequence closure)`.  
Constraints: `(K: delayed subject is syntactic closure, not an added lexical branch)`.  
Grade: strong.

### C14 — root recurrence ring: first `أَحَدٌ` to final `أَحَدٌ`

Initial image: the same root appears first as positive predicate, last as negative-scope subject.  
Visited: S112-ALL. Selected: `(E: ءحد B001 first)`, `(E: ءحد B002 final)`, `(E: temporal recurrence)`.  
Frozen model: first unity is reactivated as final exhaustive no-any-one.  
Predictions: middle units should explain why reactivation is needed.  
Unused tested: الصمد, ولد pair, كفء.  
Corroborators: `(C: صمد B001/B002 self-standing support)`, `(C: ولد B003/B005 genealogy denied)`, `(C: كفء B001 equality denied)`.  
Constraints: `(K: first and final occurrences differ syntactically; this contrast drives the reactivation)`.  
Grade: strong.

### C15 — ayah-boundary progression

Initial image: each ayah contributes a layer: command/identity, ṣamad predicate, birth-negation pair, equal-denial closure.  
Visited: S112-ALL. Selected: `(E: temporal order 112:1→112:4)`, `(E: قول B001)`, `(E: ءحد B001)`, `(E: صمد B001)`, `(E: ولد B003)`, `(E: كفء B001)`, `(E: ءحد B002)`.  
Frozen model: ordered exclusion: say/name/unify; thicken as ṣamad; deny genealogy; deny counterpart.  
Predictions: shuffling would weaken the final reactivation.  
Unused tested: word order and final delayed subject.  
Corroborators: `(C: attachment 112:4 a4 final subject)`, `(C: triple لم sequence)`.  
Constraints: `(K: temporal order organizes but does not invent lexical content)`.  
Grade: strong.

### C16 — pronoun and 3MS referent continuity

Initial image: `هُوَ`, then 3MS verbs, then `لَّهُۥ` preserve a single referent.  
Visited: S112-ALL. Selected: `(E: morphology 3MS continuity)`, `(E: ءله B002 named referent)`, `(E: attachment 112:4 a2 له complement)`.  
Frozen model: the passage keeps one referent active through predicate and negation sequence.  
Predictions: no new subject should replace Him in the negative clauses except the final denied `أحد`.  
Unused tested: final delayed subject.  
Corroborators: `(C: ءحد B002 final is denied subject, not replacement referent)`.  
Constraints: `(K: pronoun continuity is structural, not a lexical branch)`.  
Grade: medium-strong.

### C17 — surface repetition and sound closure

Initial image: recurring surfaces/endings create recitational memory: `أَحَدٌ`, `ٱلصَّمَدُ`, `يُولَدْ`, `أَحَدٌ`.  
Visited: S112-ALL. Selected: `(E: temporal/acoustic recurrence)`, `(E: ءحد B001/B002 recurrence)`, `(E: صمد B001)`, `(E: ولد B003)`.  
Frozen model: closing sound recurrence supports memory of earlier `أحد` while the lexical sequence supplies the real model.  
Predictions: final `أحد` should be semantically and syntactically meaningful, not sound alone.  
Unused tested: final attachment package.  
Corroborators: `(C: attachment 112:4 a4 delayed subject)`, `(C: كفء B001 equality denial)`.  
Constraints: `(K: sound recurrence alone is not treated as tafsir or as lexical proof)`, `(K: كفء B003 rhyme-discrepancy remains rejected)`.  
Grade: medium — useful for recitation-state reactivation, subordinate to syntax and roots.

### C18 — opening-context basmala check, not a seed

The basmala is not an eligible seed here. It is tested only after freeze in models that already predict a divine-name or commanded-recitation frame.  
Use: `(C: basmala opening-context, اللَّه present before the assigned passage)`.  
Constraint: `(K: no basmala root initiates a seed; no رحمن/رحيم branch or interpretation is imported)`.  
Grade: not graded as a seed.

## Pass 2 convergence and compact model

The exhaustive sweep produced many immediate terminations, especially for object-specific branches such as قول B008, صمد B004/B006, كفء B004, and ءحد B006. Those failures are part of the audit. The successful or converging seeds independently produce the same ordered model:

```text
قُلْ
  → commanded outward utterance
هُوَ ٱللَّهُ أَحَدٌ
  → referent filled, named, unified
ٱللَّهُ ٱلصَّمَدُ
  → name refreshed; unity thickened as support/self-standing center
لَمْ يَلِدْ
  → no outgoing birth/generation
وَلَمْ يُولَدْ
  → no incoming birth/origin
وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ
  → no occurrence of any equal-for-Him
  → final أحد reactivates first أحد
```

Strongest seed convergence:

```text
قول B001
ءله B002 at both name occurrences
ءحد B001 at 112:1:4
صمد B001, with B002/B007 secondary
ولد B003 at both active and passive occurrences, with B005 secondary
كون B001
كفء B001
ءحد B002 at 112:4:5
constructional C01-C15
```

Key constraints preventing over-reading:

```text
قُلْ remains a speech command, not a non-speech action.
الصمد remains a predicate of ٱللَّهُ, not a literal rock, stopper, head-bandage, or strike.
ولد relations are negated; no offspring, parent, or birth event is asserted.
كفء equality is denied; no equal counterpart is introduced.
First أحد and final أحد differ syntactically; the synthesis depends on that temporal contrast.
The basmala is opening-context corroboration only, never a seed.
```

## Exhaustiveness self-check before finalization

Lexical branch arithmetic:

```text
قول: 1 occurrence × 16 branches = 16 seeds
ءله: 2 occurrences × 2 branches = 4 seeds
ءحد: 2 occurrences × 6 branches = 12 seeds
صمد: 1 occurrence × 7 branches = 7 seeds
ولد: 2 occurrences × 6 branches = 12 seeds
كون: 1 occurrence × 6 branches = 6 seeds
كفء: 1 occurrence × 5 branches = 5 seeds
Total lexical seeds = 62
```

Constructional/morphosyntactic/temporal seeds included:

```text
C01 quoted complement
C02 pronoun-name-predicate focus
C03 two nominal predications
C04 repeated divine Name
C05 definiteness alternation
C06 الصمد hinge
C07 active ولد negation
C08 passive ولد negation
C09 active/passive ولد gate
C10 triple لم wave
C11 final negated copula package
C12 له complement of كفوا
C13 delayed final subject
C14 أحد root recurrence ring
C15 ayah-boundary progression
C16 pronoun/3MS continuity
C17 surface repetition and sound closure
C18 basmala opening-context check, not a seed
```

Potentially missing image audit:

```text
Failed object branches were not omitted: قول B008, صمد B003-B006, كفء B004-B005, ءحد B006 each have explicit seed passes.
Failed morphosyntactic branches were not omitted: كون B003-B006 each have explicit seed passes.
Both occurrences of repeated roots were seeded separately: ءله at 112:1:3 and 112:2:1; ولد active and passive; ءحد first and final.
Both major ءحد functions were kept distinct: positive unity B001 at 112:1:4; negative-scope exhaustive B002 at 112:4:5.
No basmala branch was used as a seed.
```

Very short interpretation: the passage’s strongest temporally conditioned reactivation is the transformation of `أَحَدٌ` from a first positive unity predicate into a final exhaustive denial of any equal. The middle sequence (`ٱلصَّمَدُ`, then the active/passive ولد negations) supplies the relational pressure that makes the final `أَحَدٌۢ` close exactly where it does.
