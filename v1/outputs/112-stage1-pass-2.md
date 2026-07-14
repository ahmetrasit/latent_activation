# S112 Stage 1 Pass 2 -- temporally conditioned reactivation

Assigned passage: S112  
Sacred Arabic text source: `resources/quran/surah_112.json`  
Final Stage 1 output path: `v1/outputs/112-stage1-pass-2.md`

## Root cause for Pass 1 limitation

The limitation was procedural: I let early high-yield axes (`أحد`, `الصمد`, paired `لم`, and `كفوا أحد`) organize too much of the sweep, then summarized many full-dossier visits instead of giving every occurrence-by-branch its own independent seed pass. That made the file look as if only the words used in successful findings had received deep lexical attention. This Pass 2 restarts at the first rooted word and records every eligible lexical occurrence-by-branch seed, plus constructional, morphosyntactic, and temporal/acoustic seeds.

## Sacred text and opening context

Opening context, not seed source:

```text
0 بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
```

Assigned passage:

```text
112:1 قُلْ هُوَ ٱللَّهُ أَحَدٌ
112:2 ٱللَّهُ ٱلصَّمَدُ
112:3 لَمْ يَلِدْ وَلَمْ يُولَدْ
112:4 وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ
```

The basmala is treated only as recitational opening context. No seed is initiated from it. It can corroborate naming/divine-source activation only as `(C: basmala opening-context)`.

## Resource note

`resources/qac.sqlite` and `resources/furuq_v4.sqlite` are zero-byte placeholders in this workspace. To preserve the Stage 1 evidence boundary, I used the local mirrors in `resources/qac_root_ayah.tsv` and `resources/v4_branches.tsv` only for the same S112 rows and accepted uncontaminated furuq-v4 branch dossiers that the prompt asks the SQLite files to provide. Structural evidence comes from `resources/attachments.tsv` filtered to S112:1-4.

Source rows used:

- `resources/quran/surah_112.json`: verses 0-4.
- `resources/qac_root_ayah.tsv`: S112:1-4 rows only.
- `resources/attachments.tsv`: S112:1-4 rows only, 11 attachment rows plus header.
- `resources/v4_branches.tsv`: accepted branch rows for passage roots `ق و ل`, `ء ل ه`, `ء ح د`, `ص م د`, `و ل د`, `ك و ن`, `ك ف ء` only.

## Passage rooted words

| occurrence | rooted word | root | form / role cue |
| --- | --- | --- | --- |
| 112:1:1 | `قُلْ` | `ق و ل` | imperative speech verb |
| 112:1:3 | `ٱللَّهُ` | `ء ل ه` | proper noun, nominative |
| 112:1:4 | `أَحَدٌ` | `ء ح د` | nominative predicate |
| 112:2:1 | `ٱللَّهُ` | `ء ل ه` | repeated proper noun |
| 112:2:2 | `ٱلصَّمَدُ` | `ص م د` | definite nominative predicate |
| 112:3:2 | `يَلِدْ` | `و ل د` | jussive active imperfect under `لَمْ` |
| 112:3:4 | `يُولَدْ` | `و ل د` | jussive passive imperfect under `لَمْ` |
| 112:4:2 | `يَكُن` | `ك و ن` | jussive negated copula |
| 112:4:4 | `كُفُوًا` | `ك ف ء` | accusative predicate of negated copula |
| 112:4:5 | `أَحَدٌۢ` | `ء ح د` | delayed nominative subject under negation |

Lexical seed count: 62 occurrence-by-branch seeds.

## Attachment evidence

- `ae:v3:s112:001:pass1:attach:a1`: `هُوَ ٱللَّهُ أَحَدٌ` is the quoted complement after `قُلْ`.
- `ae:v3:s112:001:pass1:attach:a2`: `أَحَدٌ` is the nominative predicate of `ٱللَّهُ`.
- `ae:v3:s112:001:pass1:attach:a3`: `ٱللَّهُ` can appose `هُوَ`, while `أَحَدٌ` supplies the nominal predicate.
- `ae:v3:s112:002:pass1:attach:a1`: `ٱلصَّمَدُ` is the nominative predicate of `ٱللَّهُ`.
- `ae:v3:s112:003:pass1:attach:a1`: `يَلِدْ` is governed by `لَمْ` as a jussive negated imperfect.
- `ae:v3:s112:003:pass1:attach:a2`: `يُولَدْ` is coordinated with `يَلِدْ`.
- `ae:v3:s112:003:pass1:attach:a3`: `يُولَدْ` is governed by `لَمْ` as a jussive negated passive imperfect.
- `ae:v3:s112:004:pass1:attach:a1`: `يَكُن` is governed by `لَمْ` as a jussive negated imperfect.
- `ae:v3:s112:004:pass1:attach:a2`: `لَّهُۥ` is governed by the counterpart predicate `كُفُوًا`.
- `ae:v3:s112:004:pass1:attach:a3`: `كُفُوًا` is the accusative predicate of `يَكُن`.
- `ae:v3:s112:004:pass1:attach:a4`: final `أَحَدٌۢ` is the delayed nominative subject of `يَكُن`.

## Branch dossiers

Each dossier was read as continuous branch-preserving prose during seed work.

### `ق و ل`

- `B001` `إخراج القول بالنطق` -- `يدخل فيه قال يقول قولا، والقول والقيل، والكلام المركب من الحروف إذا أبرز بالنطق، مفردا كان أو جملة أو قصيدة أو خطبة.`
- `B002` `اللسان آلة القول` -- `يدخل فيه المقول بمعنى اللسان.`
- `B003` `كثرة القول في صاحبه` -- `يدخل فيه قولة وقوال وقوالة وتقوالة وقؤول ومقوال ومقول إذا وصفت الإنسان بأنه لسن أو كثير القول أو منطيق.`
- `B004` `القيل صاحب القول النافذ` -- `يدخل فيه المقول أو القيل بلغة أهل اليمن، والواحد القيل، والجمع المقاولة والأقيال والأقوال، وملك حمير دون الملك الأعظم، والمرأة قيلة.`
- `B005` `قول ما لم يكن أو نسبته` -- `يدخل فيه تقول باطلا، وتقول عليه أي كذب عليه، وقولتني أو أقولتني ما لم أقل.`
- `B006` `اجترار القول إلى النفس` -- `يدخل فيه اقتال قولا إذا اجتر إلى نفسه قولا من خير أو شر.`
- `B007` `القول الفاشي بين الناس` -- `يدخل فيه القالة الحسنة أو القبيحة المنتشرة في الناس، وكثرة قالة الناس، والقيل والقال بوصفهما حديثا دائرا.`
- `B008` `عود القال لضرب القلة` -- `يدخل فيه القال، الخشبة التي تضرب بها القلة.`
- `B009` `المقاولة في الأمر` -- `يدخل فيه قاولته في أمره وتقاولنا إذا تفاوضنا.`
- `B010` `اقتالة الحكم على غيره` -- `يدخل فيه اقتال عليه إذا كان بمعنى تحكم.`
- `B011` `قول يجري مجرى الظن` -- `يدخل فيه تقول إذا أجري مجرى تظن في العمل، وخاصة في الاستفهام، وما ذكر عن بني سليم من إجراء متصرف قلت مجرى الظن في غير الاستفهام.`
- `B012` `قول في النفس لم يظهر` -- `يدخل فيه المتصور في النفس قبل الإبراز باللفظ، كما في قول في نفسي لم أظهره.`
- `B013` `القول اعتقاد ومذهب` -- `يدخل فيه القول بمعنى الاعتقاد، نحو فلان يقول بقول أبي حنيفة.`
- `B014` `قول الشيء دلالته` -- `يدخل فيه القول للدلالة على الشيء، مثل امتلأ الحوض وقال قطني.`
- `B015` `العناية الصادقة بالشيء` -- `يدخل فيه فلان يقول بكذا إذا كان معناه العناية الصادقة بالشيء.`
- `B016` `قول الشيء حده` -- `يدخل فيه استعمال المنطقيين القول بمعنى الحد، كقول الجوهر وقول العرض أي حدهما.`

### `ء ل ه`

- `B001` `التعبد والمعبود` -- `يدخل فيه أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.`
- `B002` `اسم الله في القسم والنداء` -- `يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.`

### `ء ح د`

- `B001` `الأَحَدِيَّة والوَحْدَة` -- `أحد بمعنى الواحد، والوصف المطلق بأحد، وتكرار أحد أحد للتأكيد.`
- `B002` `استغراق النفي` -- `أحد في سياق النفي لاستغراق جنس من يصلح أن يخاطب، فيشمل الواحد وما فوقه.`
- `B003` `الواحد في العد والتركيب` -- `أحد في العد، وتركيبه مع العشرات، وتصْيير المعدود أحد عشر.`
- `B004` `الأول والإضافة` -- `أحد مضافا أو مضافا إليه بمعنى الأول، واسم يوم الأحد.`
- `B005` `الانفراد والتفرق آحادا` -- `الانفراد بالفعل، والمجيء آحادا أفرادا.`
- `B006` `جبل أُحُد` -- `اسم جبل بالمدينة.`

### `ص م د`

- `B001` `القصد إلى المعتمد المقصود` -- `قصد الشيء واعتماده؛ السيد الذي يقصد إليه في الأمور والحوائج؛ الصمد من جهة الصمود إليه.`
- `B002` `الصلابة المكتنزة بلا جوف` -- `الصلابة والاكتناز وانعدام الجوف؛ المكان الصلب أو المرتفع الغليظ؛ الصخرة الراسية والأرض الشديدة.`
- `B003` `سدادة القارورة المحكمة` -- `الصماد بمعنى عفاص القارورة أو سدادها؛ فعل صمد القارورة أي جعل لها صمادا.`
- `B004` `شد الرأس بصماد` -- `تصميد الرأس بخرقة أو منديل أو ثوب دون العمامة.`
- `B005` `الإشراف على الأمر مع الحفل به` -- `قولهم على صمادة من أمر لمن أشرف عليه وحفل به.`
- `B006` `إيقاع الضرب بالعصا` -- `صمده بالعصا بمعنى ضربه بها.`
- `B007` `الدوام والبقاء على الشدة` -- `الدوام والبقاء؛ الناقة المصماد الباقية على القر والجدب الدائمة الرسل.`

### `و ل د`

- `B001` `مولود من نسل` -- `يدخل فيه الولد والمولود والابن والابنة والأولاد، ويستعمل للواحد والجمع وللصغير والكبير وللذكر والأنثى بحسب نصوص المصادر.`
- `B002` `أبوان من جهة الولادة` -- `يدخل فيه الوالد بمعنى الأب، والوالدة بمعنى الأم، والوالدان للأب والأم.`
- `B003` `حدوث الولادة ووضع الحمل` -- `يدخل فيه ولدت المرأة، والولادة بوضع الوالدة ولدها، وما قرب من وقت الولادة أو حان ولاده في أولدت، وولادة الحيوان إذا نصت المصادر عليها.`
- `B004` `صغير قريب العهد بالولادة أو مملوك` -- `يدخل فيه الوليد للصبي أو الغلام القريب العهد بالولادة، والوليدة للصبية أو الأمة، وما جمعه ولدان أو ولائد بحسب النص.`
- `B005` `شيء حاصل عن شيء أو مستحدث منه` -- `يدخل فيه تولد الشيء من الشيء إذا حصل عنه بسبب، والمولد من الكلام إذا استحدث، وما كان غير محض أو ناشئا في بيئة معينة مثل عربية مولدة ورجل مولد.`
- `B006` `قرين في سن الولادة` -- `يدخل فيه اللدة أو لدة الرجل بمعنى تربه ومثيله في السن.`

### `ك و ن`

- `B001` `وقوع الشيء وحضوره في زمان` -- `يدخل فيه وقوع الشيء وحضوره وحدوثه في زمان ماض أو راهن، ومصدر كان والكينونة والكائنة، واستعمال كان خبرا أو توكيدا أو في الاستثناء.`
- `B002` `المكان والمكانة من الكون` -- `يدخل فيه المكان والموضع والمكانة والمنزلة والتمكن إذا جعلت من كان يكون.`
- `B003` `الكفالة والقيام على فلان` -- `يدخل فيه الكيانة والكفالة والتكفل بفلان واكتنت به.`
- `B004` `الخضوع بالاستكانة` -- `يدخل فيه الاستكانة بمعنى الخضوع.`
- `B005` `الشيخ المنسوب إلى كُنْتُ` -- `يدخل فيه الكُنْتِيّ للرجل إذا شاخ كأنه نسب إلى قوله كُنْتُ في شبابي.`
- `B006` `حالة السوء بكينة` -- `يدخل فيه قولهم بات فلان بكينة سوء أي بحال سوء إذا جعلت الكينة فعلة من الكون.`

### `ك ف ء`

- `B001` `المماثلة والمقابلة بالمثل` -- `يدخل فيه الكفء والمثل والنظير؛ التساوي والتكافؤ؛ الكفاءة في المناكحة والحرب والمضادة؛ المكافأة والمجازاة بالمثل؛ المقابلة والموالاة بين شيئين.`
- `B002` `الإمالة والقلب والصرف` -- `يدخل فيه إمالة الشيء وقلبه وكبه؛ إمالة القوس والصحفة؛ صرف القوم عن وجهتهم؛ التمايل في المشي أو كالسفينة؛ انكسار الوجه وتغير اللون.`
- `B003` `اختلاف القوافي` -- `يدخل فيه الإكفاء في الشعر باختلاف القوافي في الحروف أو الحركات أو الإعراب.`
- `B004` `كِفاء الخباء` -- `يدخل فيه الكِفاء بمعنى شقة أو شقتين تخاطان ويجعل بهما مؤخر الخباء أو البيت.`
- `B005` `كفأة السنة والنتاج` -- `يدخل فيه الكفأة لحمل النخلة أو نتاج الإبل سنة؛ سؤال نتاج الإبل أو ثمر النخل سنة؛ إعطاء اللبن والوبر والأولاد سنة؛ جعل الإبل كفأتين يتناوب نتاجهما.`

## Global temporal activation

The recitation begins with an imperative speech event. The quote then exposes a referent through name and unity: `قُلْ` opens public utterance, `هُوَ` points, `ٱللَّهُ` names, and `أَحَدٌ` predicates unity. The next ayah repeats the proper name rather than using only a pronoun; the repetition reanchors the referent and allows a second positive predicate, `ٱلصَّمَدُ`, to add dependence-direction, compactness, or permanence depending on branch. Ayah 3 then switches from positive predication to paired negated generative relations: no outgoing begetting and no incoming being-begotten. Ayah 4 closes with a negated copular existence frame: no counterpart exists for him, and the final `أَحَدٌ` reactivates the opening `أَحَدٌ` under a different syntactic scope, turning unity into exhaustive peer-denial.

The most stable image is not an alternative translation. It is a secondary relational simulation: a referent is named, unified, fixed as the ultimate point of orientation, then insulated from vertical genealogy and lateral equivalence. The closure occurs when the last possible peer candidate, `أَحَدٌ`, is placed under negation.

## Lexical seed passes

Every lexical seed below was run from its occurrence and branch, with all other root dossiers visited. `Visited` is compressed as `ALL_OTHER_DOSSIERS`, meaning the remaining S112 dossiers listed above were read in full and branch-preserving order. `Unused tested` includes sequence, morphology, attachments, repetition, and unused roots not selected before freeze.

### 1. `112:1:1 قُلْ` -- `ق و ل B001` -- overt utterance frame

- `initial image`: speech is brought out by articulation.
- `generating_set`: `(E: ق و ل B001)`, `(E: attachment a1 quoted complement)`, `(E: ء ل ه B002 name-form dimension)`.
- `frozen model`: a commanded vocal event releases a compact named proposition.
- `predictions_at_freeze`: overt quote span, stable named referent, predicates organizing the quote.
- `unused_features_tested`: `أحد`, second `الله`, `الصمد`, birth negations, counterpart negation, final `أحد`.
- `corroborators`: `(C: attachment a2/a3 predication/apposition)`, `(C: lexical recurrence 112:1:3->112:2:1)`, `(C: later property assignment 112:2-4)`, `(C: basmala اسم-الله opening-context)`.
- `constraints`: `(K: a1 limits explicit quote to 112:1:2-4; later ayahs continue discourse but are not inside that attachment)`.
- `temporal_reactivation_notes`: the imperative makes later predicates heard as content to be declared.
- `grade`: `medium-strong`; clear syntax and sequence, lexical image is direct but mostly frame-level.
- `source_queries_or_rows_used`: QAC S112 `ق و ل`; branch `ق و ل B001`; attachment a1-a3.

### 2. `112:1:1 قُلْ` -- `ق و ل B002` -- tongue as latent instrument

- `initial image`: the speech organ is implied by utterance.
- `generating_set`: `(E: ق و ل B002)`.
- `frozen model`: an instrument of saying is present only as bodily background.
- `predictions_at_freeze`: possible sound/acoustic continuity.
- `unused_features_tested`: all later predicates and negations.
- `corroborators`: `(C: imperative speech event requires utterance)`.
- `constraints`: `(K: no tongue/organ word, no articulation mechanics, no later role completion)`.
- `temporal_reactivation_notes`: the branch fades after `قُلْ`.
- `grade`: `weak`; real lexical branch, little passage-local expansion.
- `source_queries_or_rows_used`: `ق و ل B002`; attachment a1.

### 3. `112:1:1 قُلْ` -- `ق و ل B003` -- abundant speaker

- `initial image`: a person characterized by much speech.
- `generating_set`: `(E: ق و ل B003)`.
- `frozen model`: loquacity or facility of speech.
- `predictions_at_freeze`: repeated speech forms or speaker characterization.
- `unused_features_tested`: all roots and attachments.
- `corroborators`: none beyond the single imperative.
- `constraints`: `(K: only one speech imperative; no كثرة القول, no human character predicate)`.
- `temporal_reactivation_notes`: not reactivated.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ق و ل B003`.

### 4. `112:1:1 قُلْ` -- `ق و ل B004` -- effective command-holder

- `initial image`: a figure whose word has force or rank.
- `generating_set`: `(E: ق و ل B004)`.
- `frozen model`: authoritative saying.
- `predictions_at_freeze`: command authority or ruling role.
- `unused_features_tested`: divine name, predications, negations.
- `corroborators`: `(C: imperative form gives command force, but to the addressee rather than by the addressee)`.
- `constraints`: `(K: branch is Yemeni title/rank; passage does not call the speaker قيل or ملك)`.
- `temporal_reactivation_notes`: authority remains discourse-level, not lexical synthesis.
- `grade`: `weak`.
- `source_queries_or_rows_used`: `ق و ل B004`; imperative morphology.

### 5. `112:1:1 قُلْ` -- `ق و ل B005` -- false attribution pressure

- `initial image`: saying what is not so or attributing words falsely.
- `generating_set`: `(E: ق و ل B005)`.
- `frozen model`: a corrective utterance could block false attribution.
- `predictions_at_freeze`: explicit denial of misattributed relations.
- `unused_features_tested`: birth denials and counterpart denial.
- `corroborators`: `(C: 112:3-4 deny relations that could be falsely attributed)`.
- `constraints`: `(K: no explicit كذب/تقول عليه; quote is commanded truth, not accusation scene)`.
- `temporal_reactivation_notes`: later negations make this branch faintly relevant as boundary-setting.
- `grade`: `medium`; good discourse fit, branch is contextually indirect.
- `source_queries_or_rows_used`: `ق و ل B005`; attachments a1, S112:3-4 negations.

### 6. `112:1:1 قُلْ` -- `ق و ل B006` -- inwardly drawn saying

- `initial image`: speech drawn into oneself.
- `generating_set`: `(E: ق و ل B006)`.
- `frozen model`: internalized proposition.
- `predictions_at_freeze`: inward belief or hidden speech.
- `unused_features_tested`: pronoun/name/predication sequence.
- `corroborators`: `(C: هُوَ points before naming, allowing a compact mental referent)`.
- `constraints`: `(K: imperative demands outward utterance; no نفس/internal marker)`.
- `temporal_reactivation_notes`: outward `قُلْ` defeats the inward-only branch.
- `grade`: `weak`.
- `source_queries_or_rows_used`: `ق و ل B006`; attachment a1.

### 7. `112:1:1 قُلْ` -- `ق و ل B007` -- circulating saying

- `initial image`: speech spreads among people.
- `generating_set`: `(E: ق و ل B007)`.
- `frozen model`: a formula made public and repeatable.
- `predictions_at_freeze`: compact, memorable content.
- `unused_features_tested`: short ayah units, repeated `الله`, final `أحد`.
- `corroborators`: `(C: extreme compression of 112:1-4)`, `(C: repeated surface anchors support recitability)`.
- `constraints`: `(K: no explicit الناس/قالة; circulation is pragmatic rather than lexical in the passage)`.
- `temporal_reactivation_notes`: the whole surah can function as a public formula, but this is secondary.
- `grade`: `medium`.
- `source_queries_or_rows_used`: `ق و ل B007`; sequence and repetition.

### 8. `112:1:1 قُلْ` -- `ق و ل B008` -- striking stick

- `initial image`: a stick used to hit a game-piece.
- `generating_set`: `(E: ق و ل B008)`.
- `frozen model`: physical striking instrument.
- `predictions_at_freeze`: object, struck target, motion path.
- `unused_features_tested`: all roots.
- `corroborators`: none.
- `constraints`: `(K: no stick, game, strike, or target construction)`.
- `temporal_reactivation_notes`: dies at seed.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ق و ل B008`.

### 9. `112:1:1 قُلْ` -- `ق و ل B009` -- negotiation

- `initial image`: mutual exchange of words about a matter.
- `generating_set`: `(E: ق و ل B009)`.
- `frozen model`: dialogic negotiation.
- `predictions_at_freeze`: multiple speakers, reciprocal markers, disputed terms.
- `unused_features_tested`: quote and negations.
- `corroborators`: `(C: negated alternatives suggest disputed claims only by inference)`.
- `constraints`: `(K: imperative + monologic quote; no reciprocal morphology or second speaker)`.
- `temporal_reactivation_notes`: possible polemical background is not locally expressed.
- `grade`: `weak`.
- `source_queries_or_rows_used`: `ق و ل B009`; attachment a1.

### 10. `112:1:1 قُلْ` -- `ق و ل B010` -- imposed judgment

- `initial image`: controlling or ruling over another.
- `generating_set`: `(E: ق و ل B010)`.
- `frozen model`: coercive judgment by speech.
- `predictions_at_freeze`: governed party or imposed ruling.
- `unused_features_tested`: all later clauses.
- `corroborators`: `(C: imperative is command-form)`.
- `constraints`: `(K: no اقتال عليه construction; content is theological predication, not adjudication over a party)`.
- `grade`: `weak`.
- `source_queries_or_rows_used`: `ق و ل B010`; imperative morphology.

### 11. `112:1:1 قُلْ` -- `ق و ل B011` -- supposition

- `initial image`: saying as thinking/supposing.
- `generating_set`: `(E: ق و ل B011)`.
- `frozen model`: a mental proposition tested as belief.
- `predictions_at_freeze`: uncertainty, interrogative, or ظن-like complement behavior.
- `unused_features_tested`: quote and clause structures.
- `corroborators`: none.
- `constraints`: `(K: direct imperative speech, no interrogative, no ظن-like syntax)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ق و ل B011`; attachment a1.

### 12. `112:1:1 قُلْ` -- `ق و ل B012` -- unspoken inner proposition

- `initial image`: speech retained in the self before expression.
- `generating_set`: `(E: ق و ل B012)`.
- `frozen model`: hidden formulation waiting to be uttered.
- `predictions_at_freeze`: transition from inner to outer.
- `unused_features_tested`: imperative and quote.
- `corroborators`: `(C: قُلْ can convert content into outward saying)`.
- `constraints`: `(K: passage begins with outward command; no "في نفسي" marker)`.
- `grade`: `weak`.
- `source_queries_or_rows_used`: `ق و ل B012`; attachment a1.

### 13. `112:1:1 قُلْ` -- `ق و ل B013` -- articulated doctrine

- `initial image`: saying as belief, school, or position.
- `generating_set`: `(E: ق و ل B013)`, `(E: predication 112:1)`, `(E: predication 112:2)`.
- `frozen model`: a doctrinal position is articulated through positive predicates.
- `predictions_at_freeze`: same referent maintained; later material sharpens the position by exclusion.
- `unused_features_tested`: `ولد`, `كون`, `كفء`, final `أحد`.
- `corroborators`: `(C: repeated الله reanchors topic)`, `(C: 112:3-4 sharpen by negation)`.
- `constraints`: `(K: قول B013 is an abstract extension; local form is still imperative utterance)`.
- `temporal_reactivation_notes`: positive doctrine becomes bounded by subsequent denials.
- `grade`: `medium-strong`.
- `source_queries_or_rows_used`: `ق و ل B013`; attachments a1-a4.

### 14. `112:1:1 قُلْ` -- `ق و ل B014` -- content indicates its subject

- `initial image`: a thing "says" by indicating.
- `generating_set`: `(E: ق و ل B014)`, `(E: هُوَ -> الله -> أحد sequence)`.
- `frozen model`: the uttered content functions as a sign pointing to the referent.
- `predictions_at_freeze`: predicates should reveal rather than narrate events.
- `unused_features_tested`: `الصمد`, negated genealogy, negated peer.
- `corroborators`: `(C: all later clauses are predicative/relational disclosures, not narrative actions)`.
- `constraints`: `(K: branch is nonliteral indication; `قُلْ` itself is literal command to speak)`.
- `grade`: `medium`.
- `source_queries_or_rows_used`: `ق و ل B014`; sequence 112:1-4.

### 15. `112:1:1 قُلْ` -- `ق و ل B015` -- sincere care

- `initial image`: taking serious care for a matter.
- `generating_set`: `(E: ق و ل B015)`.
- `frozen model`: concentrated concern with a subject.
- `predictions_at_freeze`: explicit object of concern.
- `unused_features_tested`: named referent and predicates.
- `corroborators`: `(C: repeated naming and compact closure keep attention on one referent)`.
- `constraints`: `(K: no care/solicitude construction; branch remains remote)`.
- `grade`: `weak`.
- `source_queries_or_rows_used`: `ق و ل B015`; repetition.

### 16. `112:1:1 قُلْ` -- `ق و ل B016` -- delimiting definition

- `initial image`: a saying as a boundary/definition.
- `generating_set`: `(E: ق و ل B016)`, `(E: 112:1 positive predication)`, `(E: 112:2 positive predication)`.
- `frozen model`: the utterance first states a positive core, then should delimit false relational openings.
- `predictions_at_freeze`: no genealogy above/below, no peer beside, closure by reusing the boundary term.
- `unused_features_tested`: paired `ولد`, final `يكن له كفوا أحد`.
- `corroborators`: `(C: active/passive ولد sequence closes vertical derivation)`, `(C: كون B001 + كفء B001 close occurrence of peer)`, `(C: final ءحد B002 reactivates opening أحد)`.
- `constraints`: `(K: B016 is technical/logical usage, not the direct meaning of imperative قل)`.
- `temporal_reactivation_notes`: opening content becomes a boundary system by ayah 4.
- `grade`: `strong` as secondary simulation; lexical branch is remote but sequence fit is excellent.
- `source_queries_or_rows_used`: `ق و ل B016`; attachments all.

### 17. `112:1:3 ٱللَّهُ` -- `ء ل ه B001` -- worshipped center

- `initial image`: the one treated as deity/worshipped.
- `generating_set`: `(E: ء ل ه B001)`, `(E: ء ح د B001)`, `(E: ص م د B001)`.
- `frozen model`: the named referent is a sole center of worship/dependence.
- `predictions_at_freeze`: no divided worship-center, no source above, no product below, no equal beside.
- `unused_features_tested`: paired `ولد`, `كون`, `كفء`, final `أحد`.
- `corroborators`: `(C: ولد B003/B005 under negation blocks generative axes)`, `(C: كفء B001 under negated كون blocks peer)`, `(C: lexical recurrence الله)`.
- `constraints`: `(K: local token is proper noun; no worshipper or worship verb is explicit)`.
- `grade`: `medium-strong`.
- `source_queries_or_rows_used`: `ء ل ه B001`; `ء ح د B001`; `ص م د B001`.

### 18. `112:1:3 ٱللَّهُ` -- `ء ل ه B002` -- exact named referent

- `initial image`: the special name `الله` as name/vocative/oath-form family.
- `generating_set`: `(E: ء ل ه B002)`, `(E: attachment a3 apposition)`.
- `frozen model`: a named referent is installed inside the quote.
- `predictions_at_freeze`: same name may recur; predicates attach to the name; opening context may corroborate naming.
- `unused_features_tested`: basmala, second `الله`, `الصمد`, pronoun `له`.
- `corroborators`: `(C: basmala اسم-الله opening-context)`, `(C: الله recurrence 112:2)`, `(C: له 3MS pronoun maintains referent)`.
- `constraints`: `(K: no oath/vocative particle at this occurrence)`.
- `grade`: `strong` for naming continuity, not for oath/vocative sub-branches.
- `source_queries_or_rows_used`: `ء ل ه B002`; basmala context; attachments a1-a3.

### 19. `112:1:4 أَحَدٌ` -- `ء ح د B001` -- unity reopened at closure

- `initial image`: absolute one/unified.
- `generating_set`: `(E: ء ح د B001)`, `(E: attachment a2 predication)`.
- `frozen model`: the named referent is predicated as one.
- `predictions_at_freeze`: later material should preserve unity, block division/derivation, and possibly reactivate `أحد`.
- `unused_features_tested`: `صمد`, paired `ولد`, final `كفوا أحد`.
- `corroborators`: `(C: صمد B002 compact/no-cavity dimension)`, `(C: ولد B003/B005 negated active/passive derivation)`, `(C: كفء B001 peer denial)`, `(C: final ء ح د B002 under negation)`.
- `constraints`: `(K: unity alone does not itself mean solidity or birth-denial; those are independent corroborators)`.
- `temporal_reactivation_notes`: final `أحد` returns the opening predicate inside negated peer-existence.
- `grade`: `strong`.
- `source_queries_or_rows_used`: `ء ح د B001`; attachments a2, a4.

### 20. `112:1:4 أَحَدٌ` -- `ء ح د B002` -- negative-scope branch waiting

- `initial image`: exhaustive `أحد` under negation.
- `generating_set`: `(E: ء ح د B002 as remote seed at positive occurrence)`.
- `frozen model`: dormant expectation that another `أحد` may appear under negation.
- `predictions_at_freeze`: negator, syntactic scope, class being exhausted.
- `unused_features_tested`: 112:4 final clause.
- `corroborators`: `(C: final أحد as delayed subject under لم يكن)`, `(C: attachment a4)`, `(C: كفء B001 supplies peer class)`.
- `constraints`: `(K: opening occurrence itself is positive predicate and primarily B001)`.
- `temporal_reactivation_notes`: strong delayed activation from 112:1:4 to 112:4:5.
- `grade`: `medium-strong`.
- `source_queries_or_rows_used`: `ء ح د B002`; final attachment a4.

### 21. `112:1:4 أَحَدٌ` -- `ء ح د B003` -- arithmetic composition

- `initial image`: numerical one in counting/composition.
- `generating_set`: `(E: ء ح د B003)`.
- `frozen model`: countable numeral.
- `predictions_at_freeze`: counted noun, numerical sequence, eleven/tens composition.
- `unused_features_tested`: all later roots.
- `corroborators`: none.
- `constraints`: `(K: no counted-item syntax, no numeral composition)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ء ح د B003`.

### 22. `112:1:4 أَحَدٌ` -- `ء ح د B004` -- first/day/addition

- `initial image`: firstness or Sunday/additive use.
- `generating_set`: `(E: ء ح د B004)`.
- `frozen model`: first member or calendrical/additive term.
- `predictions_at_freeze`: idafa, day name, ordered series.
- `unused_features_tested`: all later roots.
- `corroborators`: none.
- `constraints`: `(K: no idafa, no day, no ordinal series)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ء ح د B004`.

### 23. `112:1:4 أَحَدٌ` -- `ء ح د B005` -- solitary unit

- `initial image`: standing alone, individually.
- `generating_set`: `(E: ء ح د B005)`, `(E: ء ل ه B002 named referent)`.
- `frozen model`: a self-standing singular referent.
- `predictions_at_freeze`: no companion, no peer, no distributed plurality.
- `unused_features_tested`: `صمد`, `ولد`, `كفء`, final `أحد`.
- `corroborators`: `(C: كفء B001 negated peer)`, `(C: paired ولد denies relational derivation)`, `(C: final أحد exhaustive denial)`.
- `constraints`: `(K: branch normally describes individual action or arrival آحادا; passage states divine predicate, not motion/event plurality)`.
- `grade`: `medium`.
- `source_queries_or_rows_used`: `ء ح د B005`; S112:3-4.

### 24. `112:1:4 أَحَدٌ` -- `ء ح د B006` -- Mount Uḥud

- `initial image`: named mountain.
- `generating_set`: `(E: ء ح د B006)`.
- `frozen model`: geographic proper name.
- `predictions_at_freeze`: place reference.
- `unused_features_tested`: all roots.
- `corroborators`: none.
- `constraints`: `(K: no place syntax, no Medina/mountain context; `أحد` is nominative predicate)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ء ح د B006`.

### 25. `112:2:1 ٱللَّهُ` -- `ء ل ه B001` -- reanchored dependence center

- `initial image`: deity/worshipped center reintroduced.
- `generating_set`: `(E: ء ل ه B001 second occurrence)`, `(E: lexical recurrence الله)`, `(E: ص م د B001)`, `(E: attachment 112:2 a1)`.
- `frozen model`: the already unified referent is now the center toward which need/intention runs.
- `predictions_at_freeze`: asymmetry, no source above, no product below, no equal beside.
- `unused_features_tested`: 112:3-4 and final `أحد`.
- `corroborators`: `(C: ولد active/passive closes vertical axes)`, `(C: كفء B001 + كون B001 closes lateral axis)`, `(C: opening ء ح د B001 unity)`.
- `constraints`: `(K: worship/dependence participants are not directly expressed)`.
- `grade`: `strong` as relational image.
- `source_queries_or_rows_used`: `ء ل ه B001`; `ص م د B001`; attachments 112:2 a1.

### 26. `112:2:1 ٱللَّهُ` -- `ء ل ه B002` -- exact-name reactivation

- `initial image`: the name reappears across an ayah boundary.
- `generating_set`: `(E: ء ل ه B002)`, `(E: lexical recurrence 112:1:3->112:2:1)`.
- `frozen model`: the same named referent is deliberately reanchored before a new predicate.
- `predictions_at_freeze`: predicate follows; later pronoun remains attached to same referent.
- `unused_features_tested`: `الصمد`, `له`, final clauses.
- `corroborators`: `(C: attachment 112:2 a1)`, `(C: له 3MS pronoun)`, `(C: basmala اسم-الله opening-context)`.
- `constraints`: `(K: no oath/vocative at second occurrence either)`.
- `grade`: `strong`.
- `source_queries_or_rows_used`: `ء ل ه B002`; repetition; attachments 112:2 and 112:4.

### 27. `112:2:2 ٱلصَّمَدُ` -- `ص م د B001` -- intended reliable center

- `initial image`: one intended and relied upon for needs.
- `generating_set`: `(E: ص م د B001)`, `(E: attachment 112:2 a1)`, `(E: ء ل ه B001/B002 referent)`.
- `frozen model`: all orientation and need run toward the named one.
- `predictions_at_freeze`: no parent/source above, no child/product below, no counterpart beside.
- `unused_features_tested`: 112:3-4.
- `corroborators`: `(C: ولد B003 active/passive negations block source/product roles)`, `(C: كفء B001 peer negation)`, `(C: final أحد exhaustive denial)`.
- `constraints`: `(K: passage does not mention petitioners/needs; reliance participants are implicit in lexical branch)`.
- `temporal_reactivation_notes`: after unity, dependence adds direction toward the same center.
- `grade`: `strong`.
- `source_queries_or_rows_used`: `ص م د B001`; attachments.

### 28. `112:2:2 ٱلصَّمَدُ` -- `ص م د B002` -- compactness without cavity

- `initial image`: solid, compact, without internal cavity.
- `generating_set`: `(E: ص م د B002)`, `(E: ء ح د B001)`.
- `frozen model`: an indivisible/uncavitied center resists internal division.
- `predictions_at_freeze`: no generative opening, no internal passage of offspring, no equal external counterpart.
- `unused_features_tested`: `ولد`, `كفء`, final `أحد`.
- `corroborators`: `(C: active/passive ولد negation blocks birth-channel roles)`, `(C: كفء B001 blocks external matching)`, `(C: final ء ح د B002 exhausts candidates)`.
- `constraints`: `(K: physical solidity is a secondary simulation; primary predicate is not translated as "stone/solid body")`.
- `grade`: `medium-strong`.
- `source_queries_or_rows_used`: `ص م د B002`; `ء ح د B001`; S112:3-4.

### 29. `112:2:2 ٱلصَّمَدُ` -- `ص م د B003` -- sealed stopper

- `initial image`: a stopper sealing a bottle.
- `generating_set`: `(E: ص م د B003)`.
- `frozen model`: closure of an opening.
- `predictions_at_freeze`: vessel, mouth/opening, act of sealing.
- `unused_features_tested`: birth negations and peer negation.
- `corroborators`: `(C: ولد negation can weakly fit closure of generative opening)`.
- `constraints`: `(K: no vessel, stopper, or bottle; `الصمد` is predicate of الله)`.
- `grade`: `weak`.
- `source_queries_or_rows_used`: `ص م د B003`; S112:3.

### 30. `112:2:2 ٱلصَّمَدُ` -- `ص م د B004` -- head binding

- `initial image`: wrapping/binding the head with a cloth.
- `generating_set`: `(E: ص م د B004)`.
- `frozen model`: bandaged enclosure.
- `predictions_at_freeze`: head, cloth, injury or binding action.
- `unused_features_tested`: all later roots.
- `corroborators`: none.
- `constraints`: `(K: no head, cloth, wound, or wrapping construction)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ص م د B004`.

### 31. `112:2:2 ٱلصَّمَدُ` -- `ص م د B005` -- overseeing a matter

- `initial image`: being poised over an affair with care.
- `generating_set`: `(E: ص م د B005)`.
- `frozen model`: supervisory attention.
- `predictions_at_freeze`: affair, action, concern.
- `unused_features_tested`: 112:3-4.
- `corroborators`: none specific.
- `constraints`: `(K: no أمر/حفل role; later clauses are relation-denials, not management of an affair)`.
- `grade`: `weak`.
- `source_queries_or_rows_used`: `ص م د B005`.

### 32. `112:2:2 ٱلصَّمَدُ` -- `ص م د B006` -- striking with a stick

- `initial image`: impact by staff.
- `generating_set`: `(E: ص م د B006)`.
- `frozen model`: physical blow.
- `predictions_at_freeze`: striker, stick, struck object.
- `unused_features_tested`: all roots.
- `corroborators`: none.
- `constraints`: `(K: no strike event; no object roles)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ص م د B006`.

### 33. `112:2:2 ٱلصَّمَدُ` -- `ص م د B007` -- permanence under severity

- `initial image`: enduring, remaining under barrenness/severity.
- `generating_set`: `(E: ص م د B007)`, `(E: lexical recurrence الله)`.
- `frozen model`: the named referent remains after negated temporal/generative relations.
- `predictions_at_freeze`: no beginning by birth, no continuation by offspring, no peer event.
- `unused_features_tested`: `ولد`, `كون`, `كفء`, final `أحد`.
- `corroborators`: `(C: passive يولد negation blocks origin event)`, `(C: active يلد negation blocks lineage continuation)`, `(C: لم يكن كفوا أحد blocks counterpart occurrence)`.
- `constraints`: `(K: animal/famine example is source imagery only; no animal scene in passage)`.
- `grade`: `medium-strong`.
- `source_queries_or_rows_used`: `ص م د B007`; S112:3-4.

### 34. `112:3:2 يَلِدْ` -- `و ل د B001` active -- offspring denied

- `initial image`: a child/offspring from lineage.
- `generating_set`: `(E: و ل د B001 active occurrence)`, `(E: لم negation attachment 112:3 a1)`.
- `frozen model`: an outgoing offspring role is explicitly opened and denied.
- `predictions_at_freeze`: no descendant/product; passive counterpart may deny reverse relation.
- `unused_features_tested`: `يولد`, final `كفوا أحد`.
- `corroborators`: `(C: passive يولد denies incoming birth)`, `(C: كفء B001 denies peer relation)`, `(C: ء ح د B001 unity)`.
- `constraints`: `(K: the branch itself supplies offspring, but the local clause negates it)`.
- `grade`: `strong`.
- `source_queries_or_rows_used`: `و ل د B001`; attachment 112:3 a1-a3.

### 35. `112:3:2 يَلِدْ` -- `و ل د B002` active -- parent role denied

- `initial image`: father/mother from birth relation.
- `generating_set`: `(E: و ل د B002 active)`, `(E: لم يلد)`.
- `frozen model`: the named referent is denied the parent role.
- `predictions_at_freeze`: if parenthood is denied outwardly, being child of parents may also be denied.
- `unused_features_tested`: passive `يولد`, `الصمد`, final `كفء`.
- `corroborators`: `(C: passive يولد denies being born from parents)`, `(C: صمد B001 central dependence has no superior source)`.
- `constraints`: `(K: active verb does not name والد explicitly; parent role is inferred from branch)`.
- `grade`: `medium-strong`.
- `source_queries_or_rows_used`: `و ل د B002`; attachment 112:3.

### 36. `112:3:2 يَلِدْ` -- `و ل د B003` active -- birth event denied

- `initial image`: the act/event of giving birth.
- `generating_set`: `(E: و ل د B003 active)`, `(E: لم particle complement)`.
- `frozen model`: no birth event issues from the referent.
- `predictions_at_freeze`: paired passive should deny the referent entering through birth.
- `unused_features_tested`: passive `يولد`, `كون`, `كفء`, final `أحد`.
- `corroborators`: `(C: coordinated passive exactly supplies reverse denial)`, `(C: final negated copula prevents peer occurrence)`.
- `constraints`: `(K: no mother/body imagery should become primary meaning)`.
- `grade`: `strong`.
- `source_queries_or_rows_used`: `و ل د B003`; attachment a1-a3.

### 37. `112:3:2 يَلِدْ` -- `و ل د B004` active -- young/newborn denied

- `initial image`: young child, newborn, slave-girl/servant extension.
- `generating_set`: `(E: و ل د B004 active)`, `(E: negation)`.
- `frozen model`: no young/newborn dependent emerges from him.
- `predictions_at_freeze`: no dependent equal or product.
- `unused_features_tested`: passive `يولد`, `كفء`.
- `corroborators`: `(C: كفء B001 denies matching peer; offspring would create relational counterpart only by inference)`.
- `constraints`: `(K: local verb is يلد, not وليد/وليدة noun; servant extension absent)`.
- `grade`: `medium`.
- `source_queries_or_rows_used`: `و ل د B004`; S112:3-4.

### 38. `112:3:2 يَلِدْ` -- `و ل د B005` active -- derivative product denied

- `initial image`: something generated/derived from something.
- `generating_set`: `(E: و ل د B005 active)`, `(E: لم يلد)`.
- `frozen model`: no derived entity or secondary product comes from the named referent.
- `predictions_at_freeze`: no reverse derivation from a prior source; no comparable derivative peer.
- `unused_features_tested`: passive `يولد`, `كفء`, final `أحد`.
- `corroborators`: `(C: لم يولد denies being derivative)`, `(C: كفء B001 denies matching result)`, `(C: ء ح د B001 unity)`.
- `constraints`: `(K: "derivative product" is broader than literal birth; do not erase primary birth negation)`.
- `grade`: `strong`.
- `source_queries_or_rows_used`: `و ل د B005`; S112:3-4.

### 39. `112:3:2 يَلِدْ` -- `و ل د B006` active -- age-peer denied

- `initial image`: a peer in age/birth cohort.
- `generating_set`: `(E: و ل د B006 active)`.
- `frozen model`: no same-birth peer or cohort relation.
- `predictions_at_freeze`: explicit peer/counterpart denial would complete the image.
- `unused_features_tested`: `كفء`, final `أحد`.
- `corroborators`: `(C: كفء B001 directly denies counterpart/equal)`, `(C: final أحد under negation exhausts candidate peers)`.
- `constraints`: `(K: active يلد primarily concerns begetting, not same-age peer; B006 is branch-remote)`.
- `grade`: `medium`.
- `source_queries_or_rows_used`: `و ل د B006`; `ك ف ء B001`; final attachment a4.

### 40. `112:3:4 يُولَدْ` -- `و ل د B001` passive -- being offspring denied

- `initial image`: a born child/offspring.
- `generating_set`: `(E: و ل د B001 passive occurrence)`, `(E: لم passive attachment 112:3 a3)`.
- `frozen model`: the named referent is denied the status of offspring.
- `predictions_at_freeze`: no parent source, no peer class generated by lineage.
- `unused_features_tested`: prior active `يلد`, final counterpart frame.
- `corroborators`: `(C: prior active يلد denies offspring outgoing)`, `(C: صمد B001 source-center has no dependency above)`, `(C: كفء B001 denies equal)`.
- `constraints`: `(K: passive voice means subject receives birth; do not read active parenthood into this occurrence)`.
- `grade`: `strong`.
- `source_queries_or_rows_used`: `و ل د B001`; attachment a2-a3.

### 41. `112:3:4 يُولَدْ` -- `و ل د B002` passive -- parents denied

- `initial image`: parents as source of birth.
- `generating_set`: `(E: و ل د B002 passive)`, `(E: passive morphology)`.
- `frozen model`: no parent-source stands above the referent.
- `predictions_at_freeze`: referent remains unoriginated by birth; no superior counterpart.
- `unused_features_tested`: `الصمد`, final `كفء`.
- `corroborators`: `(C: صمد B001 intended center, not dependent endpoint)`, `(C: كفء B001 excludes comparable source-peer)`.
- `constraints`: `(K: والد/والدة nouns absent; parent role inferred from passive birth frame)`.
- `grade`: `medium-strong`.
- `source_queries_or_rows_used`: `و ل د B002`; passive morphology.

### 42. `112:3:4 يُولَدْ` -- `و ل د B003` passive -- birth event denied in reverse

- `initial image`: occurrence of birth undergone by the subject.
- `generating_set`: `(E: و ل د B003 passive)`, `(E: لم يولد)`.
- `frozen model`: no entry into being by birth.
- `predictions_at_freeze`: existence/counterpart clause should not install another origin relation.
- `unused_features_tested`: final `لم يكن له كفوا أحد`.
- `corroborators`: `(C: كون B001 under negation blocks occurrence of a counterpart)`, `(C: كفء B001)`.
- `constraints`: `(K: birth event denial is vertical; peer denial is lateral and must stay separate)`.
- `grade`: `strong`.
- `source_queries_or_rows_used`: `و ل د B003`; attachment 112:3 a3.

### 43. `112:3:4 يُولَدْ` -- `و ل د B004` passive -- newborn status denied

- `initial image`: newly born child/slave extension.
- `generating_set`: `(E: و ل د B004 passive)`.
- `frozen model`: the referent is not a newborn/dependent product.
- `predictions_at_freeze`: no prior source, no peer status.
- `unused_features_tested`: `صمد`, `كفء`.
- `corroborators`: `(C: صمد B007 permanence resists newness)`, `(C: كفء B001 peer denial)`.
- `constraints`: `(K: local form is verb, not وليد noun; slave extension irrelevant)`.
- `grade`: `medium`.
- `source_queries_or_rows_used`: `و ل د B004`; `ص م د B007`.

### 44. `112:3:4 يُولَدْ` -- `و ل د B005` passive -- derived-from relation denied

- `initial image`: something obtained from something else.
- `generating_set`: `(E: و ل د B005 passive)`, `(E: passive morphology)`.
- `frozen model`: the referent is not a derivative from a prior cause/source.
- `predictions_at_freeze`: no equal derivative beside him and no origin above him.
- `unused_features_tested`: final `كفوا أحد`.
- `corroborators`: `(C: active يلد denies derivative from him)`, `(C: كفء B001 denies any comparable resultant)`, `(C: ء ح د B001 unity)`.
- `constraints`: `(K: causation/derivation is an extension; primary local sense remains birth)`.
- `grade`: `strong`.
- `source_queries_or_rows_used`: `و ل د B005`; attachments.

### 45. `112:3:4 يُولَدْ` -- `و ل د B006` passive -- birth-cohort peer denied

- `initial image`: someone of same age/birth.
- `generating_set`: `(E: و ل د B006 passive)`.
- `frozen model`: the subject has no birth-cohort relation.
- `predictions_at_freeze`: peer denial.
- `unused_features_tested`: `كفء`, final `أحد`.
- `corroborators`: `(C: كفء B001 counterpart denial)`, `(C: final ء ح د B002 exhaustive candidate denial)`.
- `constraints`: `(K: B006 is not the direct passive-verb sense)`.
- `grade`: `medium`.
- `source_queries_or_rows_used`: `و ل د B006`; final clause.

### 46. `112:4:2 يَكُن` -- `ك و ن B001` -- occurrence denied

- `initial image`: occurrence/existence of a thing in time.
- `generating_set`: `(E: ك و ن B001)`, `(E: لم يكن attachment 112:4 a1)`, `(E: ك ف ء B001)`.
- `frozen model`: the occurrence/existence of a counterpart is denied.
- `predictions_at_freeze`: counterpart predicate and subject candidate should be supplied; `له` should orient relation to named referent.
- `unused_features_tested`: `له`, `كفوا`, final `أحد`, earlier unity.
- `corroborators`: `(C: كفء B001 predicate)`, `(C: attachment a2/a3/a4)`, `(C: final ء ح د B002)`, `(C: opening ء ح د B001 reactivation)`.
- `constraints`: `(K: B001 is copular occurrence here, not an independent created-event narrative)`.
- `grade`: `strong`.
- `source_queries_or_rows_used`: `ك و ن B001`; attachment 112:4.

### 47. `112:4:2 يَكُن` -- `ك و ن B002` -- place/status

- `initial image`: place, position, station.
- `generating_set`: `(E: ك و ن B002)`.
- `frozen model`: possible station/rank for a counterpart.
- `predictions_at_freeze`: explicit place/status relation.
- `unused_features_tested`: `له كفوا أحد`.
- `corroborators`: `(C: كفء B001 can imply rank/equality)`.
- `constraints`: `(K: no مكان/مكانة lexeme; local `يكن` is copula under negation)`.
- `grade`: `weak`.
- `source_queries_or_rows_used`: `ك و ن B002`; final clause.

### 48. `112:4:2 يَكُن` -- `ك و ن B003` -- guarantor

- `initial image`: taking responsibility for someone.
- `generating_set`: `(E: ك و ن B003)`.
- `frozen model`: someone stands as guarantor/caretaker.
- `predictions_at_freeze`: dependent person and guarantor relation.
- `unused_features_tested`: `له`, `كفوا`, final `أحد`.
- `corroborators`: none.
- `constraints`: `(K: no كفالة/على فلان construction; `له` attaches to كفوا, not guarantorship)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ك و ن B003`; attachment a2.

### 49. `112:4:2 يَكُن` -- `ك و ن B004` -- submission

- `initial image`: humbling/submission.
- `generating_set`: `(E: ك و ن B004)`.
- `frozen model`: a submissive state.
- `predictions_at_freeze`: subject humbled or dependent posture.
- `unused_features_tested`: final clause and earlier predicates.
- `corroborators`: none.
- `constraints`: `(K: no استكانة form; no subject is described as submitting)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ك و ن B004`.

### 50. `112:4:2 يَكُن` -- `ك و ن B005` -- old man "I was"

- `initial image`: old person identified by past-tense reminiscence.
- `generating_set`: `(E: ك و ن B005)`.
- `frozen model`: aged-person idiom.
- `predictions_at_freeze`: human age, past boasting.
- `unused_features_tested`: all clause roles.
- `corroborators`: none.
- `constraints`: `(K: no كنتي form, no age scene)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ك و ن B005`.

### 51. `112:4:2 يَكُن` -- `ك و ن B006` -- bad condition

- `initial image`: being in a bad state.
- `generating_set`: `(E: ك و ن B006)`.
- `frozen model`: bad condition/state.
- `predictions_at_freeze`: negative condition predicate.
- `unused_features_tested`: `كفوا`.
- `corroborators`: none specific.
- `constraints`: `(K: no بكينة سوء phrase; `كفوا` is counterpart predicate, not bad-state noun)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ك و ن B006`.

### 52. `112:4:4 كُفُوًا` -- `ك ف ء B001` -- counterpart denied

- `initial image`: equal, match, counterpart, equivalence.
- `generating_set`: `(E: ك ف ء B001)`, `(E: ك و ن B001 negated copula)`, `(E: له relation)`.
- `frozen model`: no matching counterpart exists in relation to the named referent.
- `predictions_at_freeze`: candidate subject under negation; relation points to him; opening unity reactivates.
- `unused_features_tested`: final `أحد`, opening `أحد`, prior birth negations.
- `corroborators`: `(C: final ء ح د B002 as exhaustive candidate)`, `(C: opening ء ح د B001)`, `(C: ولد B006 peer branch and B005 derivation branch are already denied by 112:3)`.
- `constraints`: `(K: do not import marriage/war/mutual retaliation sub-scenes as primary; local noun means counterpart/equal)`.
- `temporal_reactivation_notes`: the final clause converts opening unity into absence of any equal.
- `grade`: `strong`.
- `source_queries_or_rows_used`: `ك ف ء B001`; attachments a2-a4.

### 53. `112:4:4 كُفُوًا` -- `ك ف ء B002` -- tilting or reversal

- `initial image`: turning, tipping, redirecting, overturning.
- `generating_set`: `(E: ك ف ء B002)`.
- `frozen model`: possible reversal away from equality.
- `predictions_at_freeze`: physical turning or redirected group.
- `unused_features_tested`: `له`, final `أحد`, earlier sequence.
- `corroborators`: `(C: the negated clause reverses expectation of a peer only abstractly)`.
- `constraints`: `(K: no vessel/bow/group movement; local form `كفوا` is counterpart predicate)`.
- `grade`: `weak`.
- `source_queries_or_rows_used`: `ك ف ء B002`.

### 54. `112:4:4 كُفُوًا` -- `ك ف ء B003` -- mismatched rhymes

- `initial image`: poetic rhyme inconsistency.
- `generating_set`: `(E: ك ف ء B003)`.
- `frozen model`: uneven endings.
- `predictions_at_freeze`: poetry/rhyme markers.
- `unused_features_tested`: ayah endings.
- `corroborators`: `(C: ayah-end sound recurrence exists only as broad acoustic material)`.
- `constraints`: `(K: no poetry/rhyme terminology; branch concerns verse craft, not local noun predicate)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ك ف ء B003`; ayah boundaries.

### 55. `112:4:4 كُفُوًا` -- `ك ف ء B004` -- tent panel

- `initial image`: cloth panels sewn to cover a tent rear.
- `generating_set`: `(E: ك ف ء B004)`.
- `frozen model`: protective covering/panel.
- `predictions_at_freeze`: tent, cloth, sewing, rear cover.
- `unused_features_tested`: all.
- `corroborators`: none.
- `constraints`: `(K: no tent/cloth/sewing roles; noun is in counterpart slot)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ك ف ء B004`.

### 56. `112:4:4 كُفُوًا` -- `ك ف ء B005` -- yearly yield/offspring allotment

- `initial image`: a year's yield, animal offspring, alternating production.
- `generating_set`: `(E: ك ف ء B005)`.
- `frozen model`: annual productive allotment.
- `predictions_at_freeze`: year, yield, animals/date-palms, alternating production.
- `unused_features_tested`: `ولد` negations.
- `corroborators`: `(C: ولد negations share production/offspring field only very remotely)`.
- `constraints`: `(K: no year/yield/animals; local clause denies equal, not productive allotment)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ك ف ء B005`; S112:3.

### 57. `112:4:5 أَحَدٌۢ` -- `ء ح د B001` final -- unity recalled

- `initial image`: one/unified.
- `generating_set`: `(E: ء ح د B001 final occurrence)`, `(E: delayed subject attachment a4)`.
- `frozen model`: the opening unity term returns at closure.
- `predictions_at_freeze`: relation to opening predicate and peer denial.
- `unused_features_tested`: `لم يكن`, `كفوا`, earlier `أحد`.
- `corroborators`: `(C: opening ء ح د B001 lexical recurrence)`, `(C: كفء B001)`, `(C: negated copula)`.
- `constraints`: `(K: because final `أحد` is under negated existence, B002 is the sharper local branch)`.
- `temporal_reactivation_notes`: final occurrence retroactively seals the opening predicate.
- `grade`: `medium-strong`.
- `source_queries_or_rows_used`: `ء ح د B001`; attachment a4.

### 58. `112:4:5 أَحَدٌۢ` -- `ء ح د B002` final -- exhaustive no-one

- `initial image`: anyone/any candidate under negation.
- `generating_set`: `(E: ء ح د B002 final occurrence)`, `(E: لم يكن)`, `(E: ك ف ء B001)`.
- `frozen model`: no one whatsoever is a counterpart to him.
- `predictions_at_freeze`: relation marker to referent and exhaustive subject role.
- `unused_features_tested`: `له`, opening `أحد`, `الصمد`, birth negations.
- `corroborators`: `(C: attachment a2/a3/a4)`, `(C: opening ء ح د B001 reactivated)`, `(C: صمد B001/B002)`, `(C: ولد B005/B006 already denied)`.
- `constraints`: `(K: exhaustive denial applies to counterpart class, not to all possible beings absolutely without the `كفوا` predicate)`.
- `temporal_reactivation_notes`: strongest closure point; the final word changes the first `أحد` from simple unity into completed peer-exclusion.
- `grade`: `strong`.
- `source_queries_or_rows_used`: `ء ح د B002`; final clause attachments.

### 59. `112:4:5 أَحَدٌۢ` -- `ء ح د B003` final -- numeral

- `initial image`: arithmetic one.
- `generating_set`: `(E: ء ح د B003 final)`.
- `frozen model`: countable numeral under negation.
- `predictions_at_freeze`: counted object.
- `unused_features_tested`: `كفوا`, clause syntax.
- `corroborators`: none.
- `constraints`: `(K: final `أحد` is delayed subject, not numerical count construction)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ء ح د B003`; attachment a4.

### 60. `112:4:5 أَحَدٌۢ` -- `ء ح د B004` final -- first/day/additive

- `initial image`: first/day/additive `أحد`.
- `generating_set`: `(E: ء ح د B004 final)`.
- `frozen model`: first member or calendrical unit.
- `predictions_at_freeze`: idafa/day/ordered series.
- `unused_features_tested`: final clause.
- `corroborators`: none.
- `constraints`: `(K: no idafa/day/series; negative-scope B002 dominates)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ء ح د B004`.

### 61. `112:4:5 أَحَدٌۢ` -- `ء ح د B005` final -- isolated individual denied

- `initial image`: an individual standing alone.
- `generating_set`: `(E: ء ح د B005 final)`, `(E: negated copula frame)`.
- `frozen model`: no individual instance can occupy the counterpart slot.
- `predictions_at_freeze`: counterpart predicate and relation marker.
- `unused_features_tested`: `كفوا`, `له`, opening unity.
- `corroborators`: `(C: كفء B001)`, `(C: له relation)`, `(C: opening ء ح د B001)`.
- `constraints`: `(K: branch's action/arrival individuality is not expressed; only singleton candidatehood fits)`.
- `grade`: `medium`.
- `source_queries_or_rows_used`: `ء ح د B005`; final clause.

### 62. `112:4:5 أَحَدٌۢ` -- `ء ح د B006` final -- Mount Uḥud

- `initial image`: Mount Uḥud.
- `generating_set`: `(E: ء ح د B006 final)`.
- `frozen model`: place name as candidate.
- `predictions_at_freeze`: geographic reference.
- `unused_features_tested`: final clause.
- `corroborators`: none.
- `constraints`: `(K: no place syntax; final `أحد` is delayed subject in universal negation)`.
- `grade`: `unlikely`.
- `source_queries_or_rows_used`: `ء ح د B006`.

## Constructional, morphosyntactic, and temporal seeds

### C1. Quoted-complement construction -- `قُلْ` -> `هُوَ ٱللَّهُ أَحَدٌ`

- `seed_type`: constructional.
- `generating_set`: `(E: attachment a1 quoted complement)`, `(E: ق و ل B001)`.
- `constructed_model`: speech command opens a bounded content span.
- `freeze_point`: after 112:1.
- `predictions_at_freeze`: later clauses may elaborate same referent but are not syntactically inside the quoted complement.
- `unused_features_tested`: 112:2-4.
- `corroborators`: `(C: الله recurrence continues same discourse referent)`, `(C: pronoun له later points back)`.
- `constraints`: `(K: explicit attachment boundary prevents treating 112:2-4 as governed by `قُلْ` in the same row)`.
- `grade`: `medium-strong`.

### C2. Opening nominal predication -- `ٱللَّهُ أَحَدٌ`

- `seed_type`: morphosyntactic.
- `generating_set`: `(E: attachment a2)`, `(E: ء ل ه B002)`, `(E: ء ح د B001)`.
- `constructed_model`: named referent receives unity predicate.
- `freeze_point`: end of 112:1.
- `predictions_at_freeze`: unity should resist division, derivation, and equivalent peerhood.
- `unused_features_tested`: `الصمد`, paired `ولد`, final counterpart clause.
- `corroborators`: `(C: صمد B002 compactness)`, `(C: ولد B005 derivation denied)`, `(C: كفء B001 peer denied)`.
- `constraints`: `(K: unity is primary; compactness/birth imagery remain secondary tests)`.
- `grade`: `strong`.

### C3. Name recurrence -- `ٱللَّهُ` at 112:1 and 112:2

- `seed_type`: temporal/acoustic.
- `generating_set`: `(E: lexical recurrence 112:1:3->112:2:1)`, `(E: ء ل ه B002)`.
- `constructed_model`: the referent is deliberately reanchored across an ayah boundary.
- `freeze_point`: start of 112:2.
- `predictions_at_freeze`: new predicate attaches to same named subject; later pronouns remain coherent.
- `unused_features_tested`: `الصمد`, `له`.
- `corroborators`: `(C: attachment 112:2 a1)`, `(C: له 3MS relation)`, `(C: basmala الله opening-context)`.
- `constraints`: `(K: recurrence is not a new deity or second participant)`.
- `grade`: `strong`.

### C4. Second nominal predication -- `ٱللَّهُ ٱلصَّمَدُ`

- `seed_type`: morphosyntactic.
- `generating_set`: `(E: attachment 112:2 a1)`, `(E: ص م د B001)`.
- `constructed_model`: same named referent is identified as the intended reliable center.
- `freeze_point`: end of 112:2.
- `predictions_at_freeze`: no superior source, no produced continuation, no equal outside center.
- `unused_features_tested`: 112:3-4.
- `corroborators`: `(C: paired birth negation)`, `(C: counterpart negation)`.
- `constraints`: `(K: no explicit petitioners; dependence is lexically supplied by صمد)`.
- `grade`: `strong`.

### C5. Paired `لَمْ` birth negation -- `لَمْ يَلِدْ وَلَمْ يُولَدْ`

- `seed_type`: constructional/morphosyntactic.
- `generating_set`: `(E: attachment 112:3 a1/a2/a3)`, `(E: و ل د B003)`, `(E: active/passive voice contrast)`.
- `constructed_model`: the vertical generative axis is closed in both directions.
- `freeze_point`: end of 112:3.
- `predictions_at_freeze`: if vertical relations are denied, final closure should deny lateral counterpart.
- `unused_features_tested`: 112:4.
- `corroborators`: `(C: كفء B001)`, `(C: كون B001)`, `(C: final ء ح د B002)`.
- `constraints`: `(K: active and passive roles must remain distinct; no single blended "birth" role)`.
- `grade`: `strong`.

### C6. Active-to-passive reversal -- `يَلِدْ` -> `يُولَدْ`

- `seed_type`: temporal/morphosyntactic.
- `generating_set`: `(E: active morphology)`, `(E: passive morphology)`, `(E: coordination a2)`.
- `constructed_model`: the recitation first blocks outgoing generation, then incoming origin.
- `freeze_point`: after `يُولَدْ`.
- `predictions_at_freeze`: remaining relation type should be neither above nor below but beside.
- `unused_features_tested`: final `كفوا أحد`.
- `corroborators`: `(C: كفء B001 lateral equality)`, `(C: final أحد under negation)`.
- `constraints`: `(K: morphology supplies direction, not a full metaphysical system by itself)`.
- `grade`: `strong`.

### C7. Final negated copula -- `وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ`

- `seed_type`: constructional.
- `generating_set`: `(E: ك و ن B001)`, `(E: ك ف ء B001)`, `(E: attachment a1/a2/a3/a4)`, `(E: ء ح د B002)`.
- `constructed_model`: no candidate exists as a counterpart in relation to him.
- `freeze_point`: final word.
- `predictions_at_freeze`: closure should reactivate opening unity and stop remaining relational openings.
- `unused_features_tested`: opening `أحد`, `الصمد`, `ولد`.
- `corroborators`: `(C: opening ء ح د B001)`, `(C: صمد B001/B002)`, `(C: ولد active/passive denials)`.
- `constraints`: `(K: `له` is complement of counterpart predicate, not independent possession claim)`.
- `grade`: `strong`.

### C8. `له` pronoun relation

- `seed_type`: morphosyntactic.
- `generating_set`: `(E: attachment 112:4 a2)`, `(E: 3MS pronoun)`.
- `constructed_model`: the final peer-denial relation is oriented to the same named referent.
- `freeze_point`: at `لَّهُۥ`.
- `predictions_at_freeze`: predicate of equivalence and candidate subject should follow.
- `unused_features_tested`: `كفوا أحد`.
- `corroborators`: `(C: كفء B001)`, `(C: final ء ح د B002)`.
- `constraints`: `(K: pronoun alone does not create ownership/possession model; attachment ties it to كفوا)`.
- `grade`: `medium-strong`.

### C9. Opening-final `أحد` reactivation

- `seed_type`: temporal/acoustic.
- `generating_set`: `(E: lexical recurrence أحد 112:1:4->112:4:5)`.
- `constructed_model`: the first `أحد` states unity; the final `أحد` tests whether any one can be a counterpart.
- `freeze_point`: final word.
- `predictions_at_freeze`: final occurrence should have a different syntactic role but preserve root activation.
- `unused_features_tested`: attachment a2 versus a4, negation scope.
- `corroborators`: `(C: opening a2 nominative predicate)`, `(C: final a4 delayed subject)`, `(C: كفء B001)`.
- `constraints`: `(K: same surface does not mean same syntax; first is positive predicate, second is negative-scope subject)`.
- `grade`: `strong`.

### C10. Ayah-boundary progression

- `seed_type`: temporal/acoustic.
- `generating_set`: `(E: sequence 112:1 positive unity)`, `(E: 112:2 positive صمد)`, `(E: 112:3 vertical negation)`, `(E: 112:4 lateral negation)`.
- `constructed_model`: positive core first, then vertical exclusion, then lateral closure.
- `freeze_point`: after the full sequence.
- `predictions_at_freeze`: shuffled order would weaken the image because `الصمد` predicts denial of dependency axes before the final peer-denial.
- `unused_features_tested`: repeated name and repeated `أحد`.
- `corroborators`: `(C: الله recurrence)`, `(C: أحد recurrence)`, `(C: active/passive order)`.
- `constraints`: `(K: sequence is structural evidence, not an independent lexical meaning)`.
- `grade`: `strong`.

## Candidate synthesis units

### `S112-CSU-01` -- named unity closed against all relational alternatives

- `ayah_range`: 112:1-4.
- `seed_type`: verified composite.
- `seed`: convergence from `ق و ل B016`, `ء ح د B001/B002`, `ص م د B001`, `و ل د B003/B005`, `ك و ن B001`, `ك ف ء B001`.
- `generating_set`: `(E: ق و ل B016 delimitation)`, `(E: ء ل ه B002 naming)`, `(E: ء ح د B001 opening unity)`, `(E: ص م د B001 dependence-center)`, `(E: و ل د B003/B005 active-passive negated generation)`, `(E: ك و ن B001 negated occurrence)`, `(E: ك ف ء B001 counterpart)`, `(E: ء ح د B002 final exhaustive candidate)`.
- `selected_branches`: `ق و ل B016`, `ء ل ه B002`, `ء ح د B001`, `ء ح د B002`, `ص م د B001`, `و ل د B003`, `و ل د B005`, `ك و ن B001`, `ك ف ء B001`.
- `constructed_model`: a commanded utterance names a referent, predicates unity, reanchors the name as the intended/reliable center, denies generative relations in both vertical directions, and finally denies that any candidate exists as an equal counterpart.
- `freeze_point`: after constructing the positive core through 112:2, before testing 112:3-4.
- `predictions_at_freeze`: no outgoing child/product; no incoming birth/source; no equal beside; final closure should reuse unity or candidate language.
- `unused_features_tested`: `لم يلد`, `لم يولد`, `لم يكن`, `له`, `كفوا`, final `أحد`, active/passive order, attachments.
- `corroborators`: `(C: active/passive ولد sequence)`, `(C: final negated copula)`, `(C: final ء ح د B002)`, `(C: opening-final أحد reactivation)`, `(C: الله recurrence)`, `(C: basmala اسم-الله opening-context)`.
- `constraints`: `(K: secondary relational simulation only; none of these branches licenses replacing the primary meanings of `أحد`, `الصمد`, `يلد`, or `كفوا`)`.
- `temporal_reactivation_notes`: the final `أحد` retroactively reorganizes the opening `أحد`: what first sounded like positive unity returns as exhaustive denial of any peer candidate.
- `rival_models`: physical solidity model from `ص م د B002`; public formula model from `ق و ل B007`; derivation-denial model from `و ل د B005`. These are subordinate forks, not replacements.
- `grade`: `strong`.
- `grade_rationale`: multiple independent channels converge: lexical unity, naming recurrence, predication attachments, dependence-center branch, active/passive morphology, negated copula syntax, and final root reactivation.
- `source_queries_or_rows_used`: all S112 QAC rows; all S112 attachment rows; branch dossiers for seven passage roots.

### `S112-CSU-02` -- compact uncavitied center as secondary image

- `ayah_range`: 112:1-4.
- `seed_type`: lexical/constructional.
- `seed`: `ص م د B002`.
- `generating_set`: `(E: ص م د B002)`, `(E: ء ح د B001)`.
- `selected_branches`: `ص م د B002`, `ء ح د B001`; post-freeze `و ل د B003/B005`, `ك ف ء B001`.
- `constructed_model`: a compact, non-hollow, undivided center admits no internal generative opening and no external matching counterpart.
- `freeze_point`: after 112:2.
- `predictions_at_freeze`: no birth-channel relation, no derived product, no equal beside.
- `unused_features_tested`: 112:3-4.
- `corroborators`: `(C: لم يلد ولم يولد)`, `(C: كفء B001)`, `(C: final ء ح د B002)`.
- `constraints`: `(K: this is not the primary contextual meaning of `الصمد`; no physical body is asserted)`.
- `temporal_reactivation_notes`: the birth denials make the no-cavity image newly relevant after it has been frozen.
- `rival_models`: `ص م د B001` dependence-center is primary and stronger.
- `grade`: `medium-strong`.
- `grade_rationale`: strong role completion, but image is more physical and branch-remote than the dependence-center reading.
- `source_queries_or_rows_used`: `ص م د B002`; 112:3-4 attachments.

### `S112-CSU-03` -- public formula / declared boundary

- `ayah_range`: 112:1-4.
- `seed_type`: lexical/temporal.
- `seed`: `ق و ل B001/B007/B016`.
- `generating_set`: `(E: ق و ل B001 utterance)`, `(E: ق و ل B007 public formula)`, `(E: ق و ل B016 delimitation)`, `(E: attachment a1)`.
- `selected_branches`: `ق و ل B001`, `B007`, `B016`; corroborated by `ء ح د B001/B002`.
- `constructed_model`: a short commanded utterance functions as a repeatable public boundary formula: say this content, and the content itself delimits the referent against false alternatives.
- `freeze_point`: after 112:1 quote.
- `predictions_at_freeze`: compactness, recurrence, positive core plus negative exclusions.
- `unused_features_tested`: 112:2-4.
- `corroborators`: `(C: الله recurrence)`, `(C: positive/negative sequence)`, `(C: final أحد reactivation)`.
- `constraints`: `(K: circulation/public formula is pragmatic; no explicit الناس or قالة)`.
- `temporal_reactivation_notes`: `قُلْ` remains active as the frame within which all later relational exclusions are heard.
- `rival_models`: purely doctrinal `ق و ل B013`; false-attribution correction `ق و ل B005`.
- `grade`: `medium`.
- `grade_rationale`: good discourse fit, but less lexically specific than CSU-01.
- `source_queries_or_rows_used`: `ق و ل` dossier; attachment a1; sequence.

### `S112-CSU-04` -- vertical and lateral relation closure

- `ayah_range`: 112:3-4.
- `seed_type`: constructional.
- `seed`: paired `لم` birth negation followed by final negated copula.
- `generating_set`: `(E: و ل د B003 active/passive)`, `(E: ك و ن B001)`, `(E: ك ف ء B001)`, `(E: ء ح د B002)`.
- `selected_branches`: `و ل د B003`, `و ل د B005`, `و ل د B006`, `ك و ن B001`, `ك ف ء B001`, `ء ح د B002`.
- `constructed_model`: the passage closes possible relations by axis: no offspring from him, no birth into him from another, no equal beside him.
- `freeze_point`: after 112:3 before reading 112:4.
- `predictions_at_freeze`: remaining closure should concern peer/equivalence, not another birth clause.
- `unused_features_tested`: `لم يكن له كفوا أحد`.
- `corroborators`: `(C: كفء B001)`, `(C: final أحد under negation)`, `(C: له relation)`.
- `constraints`: `(K: this candidate begins at 112:3, so opening naming/unity are corroborators, not generators)`.
- `temporal_reactivation_notes`: the final lateral denial completes the earlier vertical denials.
- `rival_models`: birth-only reading stops too early; peer-only reading misses vertical setup.
- `grade`: `strong`.
- `grade_rationale`: morphology and syntax independently complete a compact relation-axis model.
- `source_queries_or_rows_used`: S112:3-4 QAC rows and attachment rows.

### `S112-CSU-05` -- failed remote physical/action seeds catalog

- `ayah_range`: 112:1-4.
- `seed_type`: lexical failure cluster.
- `seed`: remote physical/action branches: `ق و ل B008`, `ص م د B004/B006`, `ك ف ء B004/B005`, `ك و ن B003/B005/B006`, `ء ح د B006`.
- `generating_set`: each branch was tested independently as listed in lexical seeds.
- `constructed_model`: no stable passage-local image forms.
- `freeze_point`: at seed for each branch.
- `predictions_at_freeze`: physical instruments, body parts, tent panels, yield cycles, guarantors, old-age idioms, mountain/place references.
- `unused_features_tested`: all passage roots and attachments.
- `corroborators`: none specific enough.
- `constraints`: `(K: absent participant roles and absent constructions defeat these branches)`.
- `temporal_reactivation_notes`: none; these activations decay immediately.
- `rival_models`: none retained.
- `grade`: `unlikely`.
- `grade_rationale`: preserved for audit because exhaustive singleton seeding requires failures to be recorded.
- `source_queries_or_rows_used`: corresponding branch rows in `resources/v4_branches.tsv`.

## Exhaustiveness check after file creation

- Lexical branches available for passage roots: 48.
- Occurrence-by-branch lexical seeds required: 62.
- Lexical seed passes recorded above: 62.
- Constructional/morphosyntactic/temporal seeds recorded: 10.
- All seven passage root dossiers are included with branch IDs and `branch_image_ar` / `what_is_ar` content.
- Failed seeds are explicitly retained.
- Branches used for construction are separated from corroborators and constraints.
- Basmala is used only as opening context and never as a seed.

No additional image-fork packet is required beyond the candidate units above: the distinct viable image-forks are the named unity/relation-closure model, the compact no-cavity secondary image, the public boundary formula image, and the vertical/lateral relation-closure model; failed physical/action branches do not produce complete image packets.
