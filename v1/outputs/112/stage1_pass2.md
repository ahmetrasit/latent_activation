# S112 Stage 1 Pass 2 — exhaustive temporally conditioned reactivation

## Root-cause diagnosis and Pass 2 correction

The limitation was methodological, not a shortage of available words. The earlier traversal used the correct root inventory but collapsed four distinct audit layers:

1. It treated “the full dossier was visited” as sufficient reporting, then displayed only branches selected for the already-promising center/source/product/peer model. That made each finding expose only a few words and made unselected words unverifiable.
2. It converged too early. Once a strong passage-scale geometry appeared, it became the default query and suppressed rival but weaker branch constellations such as terrain, stick/deflection, care/guarantee, cloth/enclosure, servitude, generated speech, annual production, and rhyme variation.
3. It counted rooted occurrence × branch seeds but grouped many unrooted words, morphemes, attachments, pauses, and repetitions into a small construction set instead of giving each eligible construction its own pass.
4. Its final audit checked section counts and required fields, not semantic coverage: it did not ask, seed by seed, whether every surface word had been tested and whether every branch-created fork had either been frozen or explicitly terminated.

Pass 2 restarts at `قُلْ` and corrects all four failures. Every lexical pass contains:

- an explicit continuous-dossier sweep over every other passage root;
- an explicit W01–W15 surface sweep, including unrooted words;
- every passage-local expansion fork found, including weak and defeated images;
- a separate freeze/test record for each surviving fork;
- explicit termination of unselected branches;
- construction and corroboration kept disjoint.

After the lexical sweep, 41 constructional, morphosyntactic, morphemic, temporal, acoustic, and boundary-occurrence seeds receive independent passes. A final coverage audit then searches specifically for missing images and revises the inventory before closure.

## Permitted source and evidence inventory

Sacred sequence:

```text
opening context: بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
112:1 قُلْ هُوَ ٱللَّهُ أَحَدٌ
112:2 ٱللَّهُ ٱلصَّمَدُ
112:3 لَمْ يَلِدْ وَلَمْ يُولَدْ
112:4 وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ
```

Only the sacred Arabic file, the permitted QAC rows, the permitted S112 attachment rows, and uncontaminated accepted furuq-v4 branches for passage roots were used. Basmala is recitational opening context only. Its permitted QAC analysis is `بِـ` + `ٱسْم` (root `سمو`, noun, genitive), `ٱللَّه` (root `ءله`, proper noun, genitive), and definite genitive adjectives `ٱلرَّحْمَٰن` and `ٱلرَّحِيم` (root `رحم`). It never initiates a seed. No `سمو` or `رحم` branch dossier was needed.

### Surface-word ledger used in every lexical pass

| ID | Position | Surface | Root / structure |
| --- | --- | --- | --- |
| W01 | 112:1:1 | `قُلْ` | `قول`; 2MS imperative |
| W02 | 112:1:2 | `هُوَ` | unrooted 3MS pronoun |
| W03 | 112:1:3 | `ٱللَّهُ` | `ءله`; nominative proper noun |
| W04 | 112:1:4 | `أَحَدٌ` | `ءحد`; indefinite nominative noun |
| W05 | 112:2:1 | `ٱللَّهُ` | `ءله`; nominative proper noun |
| W06 | 112:2:2 | `ٱلصَّمَدُ` | `الـ` + `صمد`; definite nominative noun |
| W07 | 112:3:1 | `لَمْ` | unrooted negator |
| W08 | 112:3:2 | `يَلِدْ` | `ولد`; active imperfect jussive, 3MS |
| W09 | 112:3:3 | `وَلَمْ` | conjunction + negator |
| W10 | 112:3:4 | `يُولَدْ` | `ولد`; passive imperfect jussive, 3MS |
| W11 | 112:4:1 | `وَلَمْ` | conjunction + negator |
| W12 | 112:4:2 | `يَكُن` | `كون`; imperfect jussive, 3MS |
| W13 | 112:4:3 | `لَّهُۥ` | preposition + 3MS pronoun |
| W14 | 112:4:4 | `كُفُوًا` | `كفء`; indefinite accusative noun |
| W15 | 112:4:5 | `أَحَدٌۢ` | `ءحد`; indefinite nominative noun |

In a `SURFACE_SWEEP`, every W01–W15 item is accounted for. `E` means used before freeze, `C` corroborates after freeze, `K` constrains/defeats after freeze, and `Ø` means explicitly tested with no passage-specific effect. Ranges such as `Ø W02–W15` are exhaustive, not shorthand for an omitted visit.

For compact secondary-fork paragraphs, the field convention is exact: `GENERATING_SET` is the complete set of items marked `E` in that fork's sentence; `UNUSED_AT_FREEZE` is every item assigned `C`, `K`, or `Ø` in that fork's `SURFACE_SWEEP`; the sentence beginning “predicts” is the frozen prediction; and the stated `C`/`K` tests and grade complete the fork record. This avoids repeating fifteen word IDs while preserving an explicit freeze boundary.

### Seed counts

- 48 accepted uncontaminated branch types across seven roots.
- 62 lexical seeds after occurrence differentiation: `قول` 16; first `ءله` 2; opening `ءحد` 6; second `ءله` 2; `صمد` 7; active `ولد` 6; passive `ولد` 6; `كون` 6; `كفء` 5; final `ءحد` 6.
- 41 independent constructional/morphosyntactic/morphemic/temporal/acoustic/boundary seeds, C01–C41.
- Total Pass 2 seed passes: **103**.

### Attachment controls

- `ae:v3:s112:001:pass1:attach:a1`: W02–W04 form the quoted complement of W01.
- `...:001:...:a2`: W04 is the nominative predicate of W03.
- `...:001:...:a3`: W03 can appose W02; confidence medium.
- `...:002:...:a1`: W06 is the nominative predicate of W05.
- `...:003:...:a1`: W08 is governed by W07.
- `...:003:...:a2`: W10 is coordinated with W08.
- `...:003:...:a3`: W10 is governed by the negator in W09.
- `...:004:...:a1`: W12 is governed by the negator in W11.
- `...:004:...:a2`: the pronoun in W13 is governed by W13's `لـ` as complement of W14.
- `...:004:...:a3`: W14 is the accusative predicate of W12.
- `...:004:...:a4`: W15 is the delayed nominative subject of W12.

Attachment rows are used only as structural evidence and never to create lexical meanings.

## Exact continuous branch dossiers

Every lexical pass reads these dossiers as continuous branch-preserving prose. In each `DOSSIER_SWEEP`, the listed branch IDs are selected; all unlisted IDs in that explicitly named range are tested and terminated.

### `قول` Q01–Q16

- B001 `إخراج القول بالنطق` — `يدخل فيه قال يقول قولا، والقول والقيل، والكلام المركب من الحروف إذا أبرز بالنطق، مفردا كان أو جملة أو قصيدة أو خطبة.`
- B002 `اللسان آلة القول` — `يدخل فيه المقول بمعنى اللسان.`
- B003 `كثرة القول في صاحبه` — `يدخل فيه قولة وقوال وقوالة وتقوالة وقؤول ومقوال ومقول إذا وصفت الإنسان بأنه لسن أو كثير القول أو منطيق.`
- B004 `القيل صاحب القول النافذ` — `يدخل فيه المقول أو القيل بلغة أهل اليمن، والواحد القيل، والجمع المقاولة والأقيال والأقوال، وملك حمير دون الملك الأعظم، والمرأة قيلة.`
- B005 `قول ما لم يكن أو نسبته` — `يدخل فيه تقول باطلا، وتقول عليه أي كذب عليه، وقولتني أو أقولتني ما لم أقل.`
- B006 `اجترار القول إلى النفس` — `يدخل فيه اقتال قولا إذا اجتر إلى نفسه قولا من خير أو شر.`
- B007 `القول الفاشي بين الناس` — `يدخل فيه القالة الحسنة أو القبيحة المنتشرة في الناس، وكثرة قالة الناس، والقيل والقال بوصفهما حديثا دائرا.`
- B008 `عود القال لضرب القلة` — `يدخل فيه القال، الخشبة التي تضرب بها القلة.`
- B009 `المقاولة في الأمر` — `يدخل فيه قاولته في أمره وتقاولنا إذا تفاوضنا.`
- B010 `اقتالة الحكم على غيره` — `يدخل فيه اقتال عليه إذا كان بمعنى تحكم.`
- B011 `قول يجري مجرى الظن` — `يدخل فيه تقول إذا أجري مجرى تظن في العمل، وخاصة في الاستفهام، وما ذكر عن بني سليم من إجراء متصرف قلت مجرى الظن في غير الاستفهام.`
- B012 `قول في النفس لم يظهر` — `يدخل فيه المتصور في النفس قبل الإبراز باللفظ، كما في قول في نفسي لم أظهره.`
- B013 `القول اعتقاد ومذهب` — `يدخل فيه القول بمعنى الاعتقاد، نحو فلان يقول بقول أبي حنيفة.`
- B014 `قول الشيء دلالته` — `يدخل فيه القول للدلالة على الشيء، مثل امتلأ الحوض وقال قطني.`
- B015 `العناية الصادقة بالشيء` — `يدخل فيه فلان يقول بكذا إذا كان معناه العناية الصادقة بالشيء.`
- B016 `قول الشيء حده` — `يدخل فيه استعمال المنطقيين القول بمعنى الحد، كقول الجوهر وقول العرض أي حدهما.`

### `ءله` L01–L02

- B001 `التعبد والمعبود` — `يدخل فيه أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.`
- B002 `اسم الله في القسم والنداء` — `يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.`

### `ءحد` A01–A06

- B001 `الأَحَدِيَّة والوَحْدَة` — `أحد بمعنى الواحد، والوصف المطلق بأحد، وتكرار أحد أحد للتأكيد.`
- B002 `استغراق النفي` — `أحد في سياق النفي لاستغراق جنس من يصلح أن يخاطب، فيشمل الواحد وما فوقه.`
- B003 `الواحد في العد والتركيب` — `أحد في العد، وتركيبه مع العشرات، وتصْيير المعدود أحد عشر.`
- B004 `الأول والإضافة` — `أحد مضافا أو مضافا إليه بمعنى الأول، واسم يوم الأحد.`
- B005 `الانفراد والتفرق آحادا` — `الانفراد بالفعل، والمجيء آحادا أفرادا.`
- B006 `جبل أُحُد` — `اسم جبل بالمدينة.`

### `صمد` S01–S07

- B001 `القصد إلى المعتمد المقصود` — `قصد الشيء واعتماده؛ السيد الذي يقصد إليه في الأمور والحوائج؛ الصمد من جهة الصمود إليه.`
- B002 `الصلابة المكتنزة بلا جوف` — `الصلابة والاكتناز وانعدام الجوف؛ المكان الصلب أو المرتفع الغليظ؛ الصخرة الراسية والأرض الشديدة.`
- B003 `سدادة القارورة المحكمة` — `الصماد بمعنى عفاص القارورة أو سدادها؛ فعل صمد القارورة أي جعل لها صمادا.`
- B004 `شد الرأس بصماد` — `تصميد الرأس بخرقة أو منديل أو ثوب دون العمامة.`
- B005 `الإشراف على الأمر مع الحفل به` — `قولهم على صمادة من أمر لمن أشرف عليه وحفل به.`
- B006 `إيقاع الضرب بالعصا` — `صمده بالعصا بمعنى ضربه بها.`
- B007 `الدوام والبقاء على الشدة` — `الدوام والبقاء؛ الناقة المصماد الباقية على القر والجدب الدائمة الرسل.`

### `ولد` Wd01–Wd06

- B001 `مولود من نسل` — `يدخل فيه الولد والمولود والابن والابنة والأولاد، ويستعمل للواحد والجمع وللصغير والكبير وللذكر والأنثى بحسب نصوص المصادر.`
- B002 `أبوان من جهة الولادة` — `يدخل فيه الوالد بمعنى الأب، والوالدة بمعنى الأم، والوالدان للأب والأم.`
- B003 `حدوث الولادة ووضع الحمل` — `يدخل فيه ولدت المرأة، والولادة بوضع الوالدة ولدها، وما قرب من وقت الولادة أو حان ولاده في أولدت، وولادة الحيوان إذا نصت المصادر عليها.`
- B004 `صغير قريب العهد بالولادة أو مملوك` — `يدخل فيه الوليد للصبي أو الغلام القريب العهد بالولادة، والوليدة للصبية أو الأمة، وما جمعه ولدان أو ولائد بحسب النص.`
- B005 `شيء حاصل عن شيء أو مستحدث منه` — `يدخل فيه تولد الشيء من الشيء إذا حصل عنه بسبب، والمولد من الكلام إذا استحدث، وما كان غير محض أو ناشئا في بيئة معينة مثل عربية مولدة ورجل مولد.`
- B006 `قرين في سن الولادة` — `يدخل فيه اللدة أو لدة الرجل بمعنى تربه ومثيله في السن.`

### `كون` K01–K06

- B001 `وقوع الشيء وحضوره في زمان` — `يدخل فيه وقوع الشيء وحضوره وحدوثه في زمان ماض أو راهن، ومصدر كان والكينونة والكائنة، واستعمال كان خبرا أو توكيدا أو في الاستثناء.`
- B002 `المكان والمكانة من الكون` — `يدخل فيه المكان والموضع والمكانة والمنزلة والتمكن إذا جعلت من كان يكون.`
- B003 `الكفالة والقيام على فلان` — `يدخل فيه الكيانة والكفالة والتكفل بفلان واكتنت به.`
- B004 `الخضوع بالاستكانة` — `يدخل فيه الاستكانة بمعنى الخضوع.`
- B005 `الشيخ المنسوب إلى كُنْتُ` — `يدخل فيه الكُنْتِيّ للرجل إذا شاخ كأنه نسب إلى قوله كُنْتُ في شبابي.`
- B006 `حالة السوء بكينة` — `يدخل فيه قولهم بات فلان بكينة سوء أي بحال سوء إذا جعلت الكينة فعلة من الكون.`

### `كفء` F01–F05

- B001 `المماثلة والمقابلة بالمثل` — `يدخل فيه الكفء والمثل والنظير؛ التساوي والتكافؤ؛ الكفاءة في المناكحة والحرب والمضادة؛ المكافأة والمجازاة بالمثل؛ المقابلة والموالاة بين شيئين.`
- B002 `الإمالة والقلب والصرف` — `يدخل فيه إمالة الشيء وقلبه وكبه؛ إمالة القوس والصحفة؛ صرف القوم عن وجهتهم؛ التمايل في المشي أو كالسفينة؛ انكسار الوجه وتغير اللون.`
- B003 `اختلاف القوافي` — `يدخل فيه الإكفاء في الشعر باختلاف القوافي في الحروف أو الحركات أو الإعراب.`
- B004 `كِفاء الخباء` — `يدخل فيه الكِفاء بمعنى شقة أو شقتين تخاطان ويجعل بهما مؤخر الخباء أو البيت.`
- B005 `كفأة السنة والنتاج` — `يدخل فيه الكفأة لحمل النخلة أو نتاج الإبل سنة؛ سؤال نتاج الإبل أو ثمر النخل سنة؛ إعطاء اللبن والوبر والأولاد سنة؛ جعل الإبل كفأتين يتناوب نتاجهما.`

## Lexical occurrence × branch sweep

For each occurrence-family below, `DOSSIER_SWEEP` names every other root's complete branch range. Selected IDs are shown with their fork; all unlisted IDs in that range terminate after testing. `SURFACE_SWEEP` accounts for every W01–W15 token.

### L01. W01 `قُلْ` × `قول B001` — overt speech, generated speech, and patterned utterance

**Initial image and implications.** `(E: قول B001)` creates an overt articulation event. It asks what is voiced, whether the voiced material is merely produced or newly generated, and whether its sound form becomes organized.

**DOSSIER_SWEEP.** `ءله B001–B002: B002→F1`; `ءحد B001–B006: B001→F1/F3`; `صمد B001–B007: B001/B002→F1 content only after freeze`; `ولد B001–B006: B005→F2`; `كون B001–B006: B001→F1 later property-occurrence`; `كفء B001–B005: B003→F3`; sibling `قول B002–B016` tested but not blended. All unlisted branches terminate.

**SURFACE_SWEEP W01–W15.** F1: `E W01–W03; C W04–W06,W08,W10,W12–W15; K W05–W15 if claimed to lie inside the forced W02–W04 quotation; Ø W07,W09,W11 as lexical content`. F2: `E W01,W08/W10 root dimension; K W02–W15 clause roles; Ø none`. F3: `E W01; C W04,W06,W10,W15 endings; K W02–W03,W05,W07–W09,W11–W14; Ø none`.

**F1 — voiced naming proposition.** `(E: قول B001) + (E: ءله B002) + (E: quoted-complement attachment)` produces a commanded vocal event whose content names a referent. `GENERATING_SET = {قول B001, ءله B002, W01 imperative, W02–W04 quote}`. `FROZEN_MODEL = command → overt named proposition`. Predictions: internally complete content, repeated reference, later properties attached to the same center. `UNUSED_AT_FREEZE = {W04 predication, W05–W15, boundaries, repetitions}`. W04 completes the proposition `(C: ءحد B001; C: predication attachment)`, W05–W06 reanchor and repredicate the name `(C: ءله B002 second occurrence; C: صمد B001/B002 rival dimensions)`, and W08/W10/W12–W15 retain the 3MS referent while adding exclusions `(C: morphology and sequence)`. The quote attachment itself ends at W04 `(K: a1 quote boundary)`. **Fork grade: medium-strong.** It is strong locally and medium-strong passage-wide.

**F2 — newly generated utterance.** `(E: قول B001) + (E: ولد B005 generated speech dimension)` creates speech as something newly produced. `GENERATING_SET = {قول B001, ولد B005}`. `FROZEN_MODEL = the utterance is a generated product`; predictions: a source/product relation should target the utterance. `UNUSED_AT_FREEZE = {actual ولد clauses and subject continuity}`. W08/W10 negate birth orientations of the maintained 3MS referent, not production of the quoted speech `(K: active/passive attachments; K: W02–W03 referent chain)`. No `مولد من الكلام` form occurs. **Fork grade: unlikely.**

**F3 — voiced patterned ending.** B001 explicitly allows an utterance as large as a poem, while `(E: كفء B003)` supplies differing rhyme endings. `GENERATING_SET = {قول B001 utterance range, كفء B003}`. `FROZEN_MODEL = a voiced composition uses varied but related endings`; prediction: repeated final material with controlled differences. `UNUSED_AT_FREEZE = {ayah-final forms}`. `أحد/الصمد/يولد/أحد` share final `د`, with exact first-last return `(C: acoustic sequence)`. W14 is contextually the noun from B001 equivalence, not `إكفاء`, and no genre construction occurs `(K: W14 morphology; K: no poetry marker)`. **Fork grade: weak.**

**Final seed grade: medium-strong.** F1 is exact and productive; F2 and F3 are retained as constrained alternatives rather than silently discarded. Very short interpretation: the first root creates a voice-and-content expectation that W02–W04 immediately completes.

### L02. W01 `قُلْ` × `قول B002` — tongue/instrument fork

**Initial image and implications.** `(E: قول B002)` supplies a tongue as the instrument of saying; it predicts instrument, operator, and vocal product.

**DOSSIER_SWEEP.** `ءله B001–B002: B002 selected as possible vocalized name`; `ءحد B001–B006: all terminate`; `صمد B001–B007: B006 tested as an unrelated stick instrument and rejected`; `ولد B001–B006: all terminate`; `كون B001–B006: all terminate`; `كفء B001–B005: all terminate`; sibling `قول B001` reserved as a post-freeze direct dimension.

**SURFACE_SWEEP W01–W15.** `E W01,W03; C W02,W04; K W01 verb morphology and absent tongue; Ø W05–W15`.

`GENERATING_SET = {قول B002, ءله B002}`. `FROZEN_MODEL = a tongue voices the divine name inside a commanded proposition`. Predictions: explicit vocal output and a locally represented instrument. `UNUSED_AT_FREEZE = {quote attachment, W02,W04–W15}`. The imperative and quotation corroborate output `(C: قول B001 distinct dimension; C: a1)`, but QAC marks W01 as a verb, not `المقول` “tongue,” and no instrument participant appears `(K: W01 morphology; K: absent tongue role)`. The tempting `صمد B006` stick is a different instrument with no speech operation and dies. **Grade: weak.** The output role is present; the branch-defining instrument is not.

### L03. W01 `قُلْ` × `قول B003` — abundant speaker / repeated formula

**Initial image and implications.** `(E: قول B003)` predicts a person characterized by much speech. A rival local image asks whether recurrence makes the command a repeated formula rather than a speaker-characterization.

**DOSSIER_SWEEP.** `ءله B001–B002: B002 selected for repeated name`; `ءحد B001–B006: B001 repetition dimension selected`; `صمد B001–B007: all terminate`; `ولد B001–B006: all terminate`; `كون B001–B006: all terminate`; `كفء B001–B005: B003 tested for repeated endings, post-freeze only`; sibling `قول B007` kept separate.

**SURFACE_SWEEP W01–W15.** `E W01,W03/W05,W04/W15; C W07,W09,W11 repetition and ayah endings; K W01 imperative rather than speaker adjective; Ø W02,W06,W08,W10,W12–W14`.

`GENERATING_SET = {قول B003, ءله B002 name recurrence, ءحد B001 repeated-form dimension}`. `FROZEN_MODEL = a prolific speaker repeatedly voices a compact formula`; predictions: repeated speech act or morphology characterizing the addressee. `UNUSED_AT_FREEZE = {single imperative form, intervening words, negator recurrence}`. Name and `أحد` recurrence corroborate formula repetition `(C: W03→W05; C: W04→W15)`, but only one imperative occurs and no `قوال/مقول` human descriptor appears `(K: W01 verb; K: no speaker-characterization)`. Repeated `لم` is repetition of negation, not of `قول`. **Grade: weak.** Recurring content exists, while the branch's abundant-speaker role does not.

### L04. W01 `قُلْ` × `قول B004` — authoritative speaker / unrivaled master

**Initial image and implications.** `(E: قول B004)` supplies a صاحب القول النافذ or ranked ruler. It opens authority, command transmission, and hierarchy roles.

**DOSSIER_SWEEP.** `ءله B001–B002: B001→hierarchy fork`; `ءحد B001–B006: B001→single authority`; `صمد B001–B007: B001 السيد dimension→hierarchy`; `ولد B001–B006: all terminate`; `كون B001–B006: B002 rank dimension→hierarchy`; `كفء B001–B005: B001 no-peer dimension→test`; sibling `قول B001` post-freeze direct speech dimension.

**SURFACE_SWEEP W01–W15.** `E W01,W03–W06; C W14–W15; K W01 plain imperative and absent ruler title; Ø W02,W07–W13`.

`GENERATING_SET = {قول B004, ءله B001, صمد B001 السيد, كون B002 rank}`. `FROZEN_MODEL = an authoritative command transmits the assertion of a uniquely ranked master`. Predictions: command force, a hierarchy, and no equal rank. `UNUSED_AT_FREEZE = {W14–W15, W01 morphology, attachment roles}`. The final no-counterpart frame supports absence of equal rank `(C: كفء B001; C: ءحد B002)`, and imperative mood supports command force `(C: W01 morphology)`. Yet no `قيل/مقول` title, ruler noun, worshipper, or rank noun occurs `(K: branch-form distance; K: W03/W05 PN and W06 predicate syntax)`. **Grade: weak.** A coherent authority geometry forms, but its distinctive lexical roles are remote.

### L05. W01 `قُلْ` × `قول B005` — fabricated or newly generated saying

**Initial image and implications.** `(E: قول B005)` predicts false saying or attribution of words never spoken. `ولد B005` creates a specific rival: speech newly generated or innovated.

**DOSSIER_SWEEP.** `ءله B001–B002: B002 name as possible attribution target`; `ءحد B001–B006: all terminate`; `صمد B001–B007: all terminate`; `ولد B001–B006: B005→fabricated/generated-speech fork`; `كون B001–B006: B001 tested for “what did not occur,” rejected as generic`; `كفء B001–B005: all terminate`; sibling `قول B001` used only as constraint.

**SURFACE_SWEEP W01–W15.** `E W01,W03,W08/W10 branch dimension; C none; K W01 imperative, W02–W04 forced quote, W08/W10 subject roles; Ø W05–W07,W09,W11–W15`.

`GENERATING_SET = {قول B005, ولد B005 generated-speech dimension, ءله B002 name}`. `FROZEN_MODEL = a name-bearing proposition is falsely attributed or newly coined`; predictions: attribution dispute, `تقول`-type form, or generation targeting speech. `UNUSED_AT_FREEZE = {actual morphology and attachments}`. W01 is plain imperative `قُلْ`, its content is structurally licensed, and W08/W10 deny birth relations of the maintained referent rather than speech production `(K: imperative form; K: a1; K: active/passive attachments)`. No rival speaker or attribution object appears. **Grade: unlikely.** A cross-root speech-generation image exists but local syntax defeats it.

### L06. W01 `قُلْ` × `قول B006` — inwardly appropriated saying

**Initial image and implications.** `(E: قول B006)` creates motion of a saying into the self, predicting an inward locus and nonpublic retention.

**DOSSIER_SWEEP.** `ءله B001–B002: B002 tested as inwardly retained name, insufficient`; `ءحد B001–B006: all terminate`; `صمد B001–B007: all terminate`; `ولد B001–B006: all terminate`; `كون B001–B006: all terminate`; `كفء B001–B005: all terminate`; sibling `قول B012` forms a similar but separately seeded inner-speech branch.

**SURFACE_SWEEP W01–W15.** `E W01; K W01 imperative overt output and W02–W04 quote; Ø W05–W15`.

`GENERATING_SET = {قول B006}`. `FROZEN_MODEL = a proposition is drawn inward`. Predictions: internal-state marker, withheld voice, or self-directed attachment. `UNUSED_AT_FREEZE = {W02–W15 and morphology}`. Immediate overt imperative plus quoted content points outward `(K: قول B001 distinct direct dimension; K: a1)`. No inward pronoun, cognition, or retrieval role appears. **Grade: unlikely.** The seed is defeated at its occurrence.

### L07. W01 `قُلْ` × `قول B007` — circulating formula

**Initial image and implications.** `(E: قول B007)` predicts a saying spreading among people. The command could initiate transmission; repeated names/forms could stabilize a formula.

**DOSSIER_SWEEP.** `ءله B001–B002: B002→named formula`; `ءحد B001–B006: B001→repeated formula`; `صمد B001–B007: all terminate`; `ولد B001–B006: B005 generated-speech dimension tested, rejected`; `كون B001–B006: all terminate`; `كفء B001–B005: B003 sound recurrence post-freeze`; sibling `قول B003` speaker-abundance kept separate.

**SURFACE_SWEEP W01–W15.** `E W01,W03/W05,W04/W15; C W04,W06,W10,W15 acoustic endings; K singular command and no social participants; Ø W02,W07–W14 except W10`.

`GENERATING_SET = {قول B007, ءله B002 name recurrence, ءحد B001 repeated form}`. `FROZEN_MODEL = a commanded named formula is shaped for circulation`. Predictions: repetition, stable content, and evidence of multiple transmitters or social spread. `UNUSED_AT_FREEZE = {sound endings, singular/plural morphology, later clauses}`. Exact name and first-last recurrence stabilize the formula `(C: temporal recurrence)`, and final sounds recur `(C: acoustic sequence)`. No plural, reciprocal transmission, report chain, or repeated speech act appears `(K: 2MS singular imperative; K: no social roles)`. **Grade: weak.** Formula-like recurrence is real; circulation is not locally instantiated.

### L08. W01 `قُلْ` × `قول B008` — stick-game deflection image

**Initial image and implications.** `(E: قول B008)` supplies the wooden `قال` used to strike the game-piece. This seed specifically predicts a striking operation, hard playing surface, target, and changed trajectory.

**DOSSIER_SWEEP.** `ءله B001–B002: all terminate`; `ءحد B001–B006: all terminate`; `صمد B001–B007: B006 strike + B002 hard-ground dimension→stick fork`; `ولد B001–B006: all terminate`; `كون B001–B006: B002 place tested as playing location`; `كفء B001–B005: B002 turning/deflection→stick fork`; sibling `قول B001` direct speech dimension becomes decisive constraint.

**SURFACE_SWEEP W01–W15.** `E W01,W06,W12,W14 as remote branches; K W01 speech morphology,W06 predication,W12 copula,W14 noun predicate; Ø W02–W05,W07–W11,W13,W15`.

`GENERATING_SET = {قول B008 stick, صمد B006 strike, صمد B002 hard ground, كفء B002 deflection, كون B002 place}`. `FROZEN_MODEL = a stick strikes a small target on hard ground and turns it from its course`. Predictions: overt stick, striker, target, impact, motion, and locative roles. `UNUSED_AT_FREEZE = {all actual forms, attachments, and remaining words}`. None of those roles is supplied: W01 is an imperative speech verb, W06 a nominative predicate, W12 a copula, and W14 an accusative counterpart predicate `(K: QAC morphology and attachments)`. Cross-dossier vividness is not passage evidence. **Grade: unlikely.** This is a complete remote image and a useful refusal test, but every local role fails.

### L09. W01 `قُلْ` × `قول B009` — negotiation among equals

**Initial image and implications.** `(E: قول B009)` supplies reciprocal discussion over an affair. It predicts two interlocutors, parity or opposition, and turn-taking.

**DOSSIER_SWEEP.** `ءله B001–B002: all terminate`; `ءحد B001–B006: B002 possible unrestricted interlocutor→test`; `صمد B001–B007: B005 affair/attention→negotiation fork`; `ولد B001–B006: B006 peer tested`; `كون B001–B006: all terminate`; `كفء B001–B005: B001 equal counterpart→negotiation fork`; sibling `قول B001` one-way speech constraint.

**SURFACE_SWEEP W01–W15.** `E W01,W06,W14–W15 as remote branch roles; K W01 one-way imperative,W02–W04 one quote,W14–W15 denied peer; Ø W05,W07–W13`.

`GENERATING_SET = {قول B009, صمد B005 affair, كفء B001 equal interlocutor, ولد B006 peer}`. `FROZEN_MODEL = peers negotiate an attended affair`. Predictions: reciprocal morphology, at least two turns, and an available peer. `UNUSED_AT_FREEZE = {imperative/quote structure and final negation}`. The passage offers only a 2MS command and one content span `(K: W01; K: a1)`, while the final clause denies any counterpart `(K: كفء B001 locally negated; K: ءحد B002)`. No mutual form occurs. **Grade: unlikely.** Several remote roles cohere, but local order defeats reciprocity.

### L10. W01 `قُلْ` × `قول B010` — unilateral command hierarchy

**Initial image and implications.** `(E: قول B010)` supplies imposed control/judgment over another. The imperative offers a possible command relation; master, worship, rank, and no-peer branches can thicken it.

**DOSSIER_SWEEP.** `ءله B001–B002: B001→hierarchy`; `ءحد B001–B006: B001→single apex`; `صمد B001–B007: B001 السيد→hierarchy`; `ولد B001–B006: all terminate`; `كون B001–B006: B002 rank→hierarchy`; `كفء B001–B005: B001 no equal→test`; sibling `قول B004` authority branch kept separate.

**SURFACE_SWEEP W01–W15.** `E W01,W03–W06; C W14–W15; K W01 plain قال rather than اقتال and no controlled patient; Ø W02,W07–W13`.

`GENERATING_SET = {قول B010, ءله B001, صمد B001 master, كون B002 rank}`. `FROZEN_MODEL = a singular apex imposes a command down a hierarchy`. Predictions: controller, governed patient, unequal rank, no peer. `UNUSED_AT_FREEZE = {W14–W15, W01 syntax}`. Final no-counterpart syntax supports no equal `(C: كفء B001; C: ءحد B002)`, and imperative mood supplies command force `(C: morphology)`. But W01 is the addressee's plain act of saying, with quoted content rather than a controlled patient; no `اقتَال` form appears `(K: form/attachment mismatch)`. **Grade: weak.** The hierarchy is a secondary abstraction, not the branch's local construction.

### L11. W01 `قُلْ` × `قول B011` — saying as supposition

**Initial image and implications.** `(E: قول B011)` predicts `قول` operating like `ظن`, especially under interrogation, with propositional uncertainty.

**DOSSIER_SWEEP.** `ءله B001–B002: all terminate`; `ءحد B001–B006: all terminate`; `صمد B001–B007: all terminate`; `ولد B001–B006: all terminate`; `كون B001–B006: B001 predication tested but does not supply supposition`; `كفء B001–B005: all terminate`; sibling `قول B013` proposition-as-position kept separate.

**SURFACE_SWEEP W01–W15.** `E W01; K W01 imperative,W02–W06 declarative predications,W07–W15 negated assertions; Ø none`.

`GENERATING_SET = {قول B011}`. `FROZEN_MODEL = a speaker entertains a conjectural proposition`. Predictions: interrogative, uncertainty, or the branch's special government. `UNUSED_AT_FREEZE = {all syntax and later words}`. W02–W06 are attached as predications and W08/W10/W12–W15 as negated relations; no interrogative or uncertainty marker occurs `(K: attachments and morphology)`. **Grade: unlikely.** Every construction is assertional rather than conjectural.

### L12. W01 `قُلْ` × `قول B012` — unspoken inner proposition

**Initial image and implications.** `(E: قول B012)` predicts a proposition formed internally but not expressed.

**DOSSIER_SWEEP.** `ءله B001–B002: B002 tested as inward name, insufficient`; `ءحد B001–B006: all terminate`; `صمد B001–B007: all terminate`; `ولد B001–B006: all terminate`; `كون B001–B006: all terminate`; `كفء B001–B005: all terminate`; sibling `قول B001` direct contrary dimension.

**SURFACE_SWEEP W01–W15.** `E W01; K W01 imperative and W02–W04 overt quote; Ø W05–W15`.

`GENERATING_SET = {قول B012}`. `FROZEN_MODEL = withheld internal speech`. Predictions: interiority or failure to externalize. `UNUSED_AT_FREEZE = {W02–W15, morphology}`. The seed token commands externalization and supplies articulated content immediately `(K: قول B001 direct dimension; K: a1)`. No inward-state cue occurs. **Grade: unlikely.** Directly defeated.

### L13. W01 `قُلْ` × `قول B013` — articulated position with two boundary forks

**Initial image and implications.** `(E: قول B013)` turns the utterance into a held position. It predicts a stable referent, coherent positive claims, and later material that sharpens rather than changes the position.

**DOSSIER_SWEEP.** `ءله B001–B002: B001→worship-position, B002→named proposition`; `ءحد B001–B006: B001→unity`; `صمد B001–B007: B001→dependence fork, B002→compactness fork`; `ولد B001–B006: B003/B005→post-freeze boundaries`; `كون B001–B006: B001→post-freeze occurrence boundary`; `كفء B001–B005: B001→post-freeze peer boundary`; sibling `قول B016` kept separate.

**SURFACE_SWEEP W01–W15.** `E W01–W06; C W07–W15; K W01 plain imperative lacks belief-holder morphology; Ø none`.

**F1 — dependence position.** `GENERATING_SET = {قول B013, ءله B001, ءحد B001, صمد B001, two predications}`. `FROZEN_MODEL = one named worship/reliance center is asserted`. Predictions: no source above, product below, or equal beside. `UNUSED_AT_FREEZE = {W07–W15}`. Active/passive birth and final no-counterpart syntax fulfill all three `(C: ولد B003; C: كون B001; C: كفء B001; C: ءحد B002)`. No belief-holder or worshipper occurs `(K: branch-role omissions)`. **Fork grade: medium-strong.**

**F2 — compactness position.** Substitute `(E: صمد B002)` for B001. `FROZEN_MODEL = one compact/cavityless center is asserted`; predictions: no generative passage or duplicate. W08/W10 and W14/W15 corroborate those features `(C: ولد B005 secondary dimension; C: كفء B001)`, while physical literalization is blocked `(K: nominal predication and no material roles)`. **Fork grade: medium-strong.**

**Final seed grade: medium.** Both propositions are coherent, but B013's اعتقاد/مذهب sense is not marked by W01's imperative form.

### L14. W01 `قُلْ` × `قول B014` — properties as self-indication

**Initial image and implications.** `(E: قول B014)` lets a thing “say” by indicating its state. It predicts that properties, rather than an external speaker, disclose the referent.

**DOSSIER_SWEEP.** `ءله B001–B002: B002 named thing`; `ءحد B001–B006: B001 property`; `صمد B001–B007: B001/B002 rival properties`; `ولد B001–B006: B003/B005 negative properties after freeze`; `كون B001–B006: B001 property occurrence`; `كفء B001–B005: B001 negative property`; sibling `قول B001` speaker-event constraint.

**SURFACE_SWEEP W01–W15.** `E W03–W06 as indicated properties; C W08,W10,W12–W15; K W01 human-addressee imperative and quote; Ø W02,W07,W09,W11,W13`.

`GENERATING_SET = {قول B014, ءله B002 name, ءحد B001, one صمد B001/B002 fork}`. `FROZEN_MODEL = the referent's positive properties make it self-indicating`. Predictions: negative properties should refine the same object without a topic shift. `UNUSED_AT_FREEZE = {W07–W15}`. The later clauses preserve 3MS reference and add exclusions `(C: sequence)`. Yet grammatically an addressed speaker is commanded to utter W02–W04; the thing is not the subject of `قال` `(K: W01 2MS and a1)`. **Grade: weak.** Retrospective indication is coherent, but not the local speech event.

### L15. W01 `قُلْ` × `قول B015` — attentive oversight / guarantee

**Initial image and implications.** `(E: قول B015)` supplies sincere care toward something. `صمد B005` and `كون B003` can fill oversight and guarantee roles.

**DOSSIER_SWEEP.** `ءله B001–B002: B001 possible cared-for/worship hierarchy`; `ءحد B001–B006: all terminate`; `صمد B001–B007: B005 oversight + B001 relied-on master→two care forks`; `ولد B001–B006: B002 parent-care role tested`; `كون B001–B006: B003 guarantee→care fork`; `كفء B001–B005: all terminate`; sibling `قول B001` form constraint.

**SURFACE_SWEEP W01–W15.** `E W01,W06,W12/W13 as remote roles; C none; K W01 imperative,W06 predicate,W13 comparison complement; Ø W02–W05,W07–W11,W14–W15`.

`GENERATING_SET = {قول B015, صمد B005, كون B003, ولد B002 parent dimension}`. `FROZEN_MODEL = an attentive overseer guarantees and cares for dependents`. Predictions: dependent, benefit, affair, and guarantee attachments. `UNUSED_AT_FREEZE = {actual attachments and remaining words}`. W13 might superficially resemble a beneficiary, but the permitted attachment makes it complement of `كُفُوًا`, not guarantee; W06 is predicated without an overseen affair `(K: a2 at 112:4; K: 112:2 predication)`. No care verb occurs. **Grade: unlikely.** The remote branches form a scene, but local syntax supplies none of its roles.

### L16. W01 `قُلْ` × `قول B016` — delimitation by positive core and negative edges

**Initial image and implications.** `(E: قول B016)` supplies a `حد`/definition image. It predicts a positive core, then exclusions of confusable relations, and a final boundary cue.

**DOSSIER_SWEEP.** `ءله B001–B002: B002 named definiendum, B001 dependence fork`; `ءحد B001–B006: B001 positive core, B002 final scope`; `صمد B001–B007: B001 reliance fork, B002 compactness fork`; `ولد B001–B006: B003 literal birth boundary, B005 derivation boundary`; `كون B001–B006: B001 occurrence boundary`; `كفء B001–B005: B001 equivalence boundary`; sibling `قول B001` direct utterance dimension held for corroboration.

**SURFACE_SWEEP W01–W15.** `E W01–W06; C W07–W15; K W01 specialized-usage distance; Ø none`.

**F1 — relational definition.** `(E: ءله B002) + (E: ءحد B001) + (E: صمد B001)` creates a named one-way reliance center. `GENERATING_SET = {قول B016, W02–W06 predications, ءله B002, ءحد B001, صمد B001}`. `FROZEN_MODEL = positive identity plus asymmetric dependence`. Predictions: deny parent/source, offspring/product, and equal. `UNUSED_AT_FREEZE = {W07–W15}`. W08/W10 deny source/product roles and W12–W15 deny equivalence `(C: ولد B003; C: كون B001; C: كفء B001; C: ءحد B002)`. **Fork grade: medium-strong.**

**F2 — structural definition.** Use `(E: صمد B002)` instead. `FROZEN_MODEL = one compact center without cavity`; predictions: no outward/inward generation and no duplicate. W08/W10 and W14/W15 fulfill them `(C: ولد B005 secondary derivation; C: كفء B001)`, with physical literalization blocked `(K: no body/material syntax)`. **Fork grade: medium-strong.**

`قول B016` is a specialized logical usage, not the contextual sense of imperative W01 `(K: usage/form distance)`. **Final seed grade: medium-strong.** The remote seed nevertheless predicts the positive→negative architecture and last-word closure better than generic theme association.

### L17. W03 `ٱللَّهُ` × `ءله B001` — worship/reliance center, servitude hierarchy, and care

**Initial image and implications.** `(E: ءله B001)` opens worshipper–worshipped directionality. It asks whether the named referent is a unique intended center, a superior in a servitude hierarchy, or a guarantor/caretaker.

**DOSSIER_SWEEP.** `قول B001–B016: B001→F1, B015→F3`; `ءحد B001–B006: B001→F1/F2`; `صمد B001–B007: B001→F1/F2, B005→F3`; `ولد B001–B006: B004→F2, B002→F3`; `كون B001–B006: B004→F2, B003→F3`; `كفء B001–B005: B001→F1 post-freeze`; sibling `ءله B002` kept separate.

**SURFACE_SWEEP W01–W15.** F1 `E W01,W03–W06; C W08,W10,W12–W15; K absent worshipper; Ø W02,W07,W09,W11,W13`. F2 `E W03,W06,W10,W12; K their actual forms/negation; Ø all others`. F3 `E W01,W03,W06,W08,W12/W13; K attachments; Ø remaining words`.

**F1 — sole worship/reliance center.** `GENERATING_SET = {ءله B001, قول B001, ءحد B001, صمد B001}`. `FROZEN_MODEL = voiced identification of one center toward which worship and reliance run`. Predictions: no source above, generated continuation below, or equal beside. `UNUSED_AT_FREEZE = {W07–W15}`. Active/passive birth and final counterpart negation close those axes `(C: ولد B003; C: كفء B001; C: كون B001; C: ءحد B002)`. W03 is a proper noun and no worshipper/act appears `(K: PN morphology; K: absent worship relation)`. **Fork grade: medium-strong.**

**F2 — master/servant hierarchy.** `(E: صمد B001 السيد) + (E: ولد B004 مملوك) + (E: كون B004 خضوع)` expands worship into master, dependent slave, and submission. `FROZEN_MODEL = one master with a submitted dependent`; predictions: servant noun, submission form, or governing attachment. `UNUSED_AT_FREEZE = {actual W10/W12 morphology and W14–W15}`. W10 is negated passive birth, W12 plain `يكن`, and no `وليد/استكان` form occurs `(K: morphology)`. **Fork grade: unlikely.**

**F3 — cared-for/guaranteeing center.** `(E: قول B015) + (E: صمد B005) + (E: كون B003) + (E: ولد B002 parent role)` yields attentive oversight and guarantee. W13 is not a beneficiary but complement of W14 `(K: attachment a2)`, and no care/guarantee form appears. **Fork grade: unlikely.**

**Final seed grade: medium-strong.** Only F1 has passage-scale role completion; F2/F3 expose and reject hierarchy/care overextensions.

### L18. W03 `ٱللَّهُ` × `ءله B002` — voiced name, circulating name, and attributed name

**Initial image and implications.** `(E: ءله B002)` foregrounds `اسم الله` and spoken formulas. It predicts naming context, vocalization, recurrence, and possibly oath/vocative marking.

**DOSSIER_SWEEP.** `قول B001–B016: B001→F1, B007→F2, B005→F3`; `ءحد B001–B006: B001→F2 recurrence`; `صمد B001–B007: all terminate as generators`; `ولد B001–B006: B005 generated-speech→F3`; `كون B001–B006: all terminate`; `كفء B001–B005: B003 acoustic support→F2 post-freeze`; sibling `ءله B001` separate.

**SURFACE_SWEEP W01–W15.** F1 `E W01–W03; C W04–W06,W13; K no oath/vocative; Ø W07–W12,W14–W15`. F2 `E W01,W03/W05,W04/W15; C endings; K no transmitters; Ø remaining`. F3 `E W01,W03,W08/W10 branch dimensions; K syntax; Ø remaining`.

**F1 — named referent in commanded speech.** `GENERATING_SET = {ءله B002, قول B001, quoted complement}`. `FROZEN_MODEL = a name is voiced, then predicated`. Predictions: opening-context naming, exact repetition, and stable reference. `UNUSED_AT_FREEZE = {basmala, W04–W15}`. `بِسْمِ ٱللَّهِ` corroborates the name dimension `(C: basmala opening-context)`, W05 repeats it and W04/W06 predicate it `(C: attachments)`. No oath/vocative particle occurs `(K: branch subuses absent)`. **Fork grade: medium-strong.** Naming itself is strong; the complete fork is medium-strong.

**F2 — circulating named formula.** Add `(E: قول B007)` and `(E: ءحد B001 recurrence dimension)`. `FROZEN_MODEL = repeated name and terminal form stabilize a circulated saying`; predictions: social transmission. Recurrence and endings fit `(C: W03→W05; C: W04→W15)`, but singular W01 supplies no circulation roles `(K)`. **Fork grade: weak.**

**F3 — attributed/generated name-speech.** `(E: قول B005) + (E: ولد B005 generated speech)` predicts disputed or newly coined naming. Authorized imperative/quote and subject continuity defeat it `(K: W01–W04 syntax; K: W08/W10 roles)`. **Fork grade: unlikely.**

**Final seed grade: medium-strong.** Naming is multiply corroborated; oath, circulation, and generated-attribution subimages remain constrained.

### L19. W04 `أَحَدٌ` × `ءحد B001` — unity with three geometries

**Initial image and implications.** `(E: ءحد B001)` is directly predicated of W03. It creates unity, then opens three possible geometries: one relied-upon center, one compact unit, or one term protected from genealogical/equivalent rivals.

**DOSSIER_SWEEP.** `قول B001–B016: B001 voice, B016 boundary→post-freeze`; `ءله B001–B002: B001→F1, B002 named center`; `صمد B001–B007: B001→F1, B002→F2`; `ولد B001–B006: B003/B005→F3 corroboration`; `كون B001–B006: B001→F3`; `كفء B001–B005: B001→F3`; sibling `ءحد B002` saved for final recurrence.

**SURFACE_SWEEP W01–W15.** `E W01,W03–W06; C W08,W10,W12–W15; K W07,W09,W11 only as operators not lexical unity; Ø W02,W13`.

**F1 — one reliance center.** `GENERATING_SET = {ءحد B001, ءله B001, صمد B001, W03–W06 predications}`. `FROZEN_MODEL = all worship/intention vectors converge on one center`. Predictions: no dependency source, derivative continuation, or equal. `UNUSED_AT_FREEZE = {W07–W15}`. W08/W10 and W12–W15 close all three `(C: ولد B003; C: كون B001; C: كفء B001; C: ءحد B002)`. Missing worshippers/needs constrain literal relational detail `(K)`. **Fork grade: strong.**

**F2 — compact indivisible unit.** Replace B001 with `(E: صمد B002)`. `FROZEN_MODEL = one compact cavityless unit`; predictions: no in/out generation, no duplicate. W08/W10 and W14/W15 fulfill them `(C: ولد B005; C: كفء B001)`, while no physical body occurs `(K)`. **Fork grade: strong.** This remains a secondary simulation.

**F3 — positive unity defended by relation closures.** Freeze from `(E: ءحد B001)` and its predication alone. `UNUSED_AT_FREEZE = {W05–W15}`. The same named referent is reanchored, then source/product/peer roles are denied, and W15 returns the form under B002 scope `(C: sequence and recurrence)`. Unity alone did not predict the exact birth lexeme `(K: specificity limit)`. **Fork grade: strong.**

**Final seed grade: strong.** Three independently controlled trajectories converge without blending their distinct `صمد` images.

### L20. W04 `أَحَدٌ` × `ءحد B002` — dormant exhaustive-negation branch

**Initial image and implications.** `(E: ءحد B002)` predicts `أحد` inside negative scope and exhaustive candidate coverage. W04 is instead a positive predicate, so the branch begins contextually dormant.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: all terminate`; `صمد B001–B007: all terminate`; `ولد B001–B006: B006 peer tested`; `كون B001–B006: B001→final occurrence test`; `كفء B001–B005: B001→final candidate class`; sibling `ءحد B001` direct local constraint.

**SURFACE_SWEEP W01–W15.** `E W04 as remote seed; C W12,W14,W15; K W04 positive predication; Ø W01–W03,W05–W11,W13`.

`GENERATING_SET = {ءحد B002 at W04 as dormant hypothesis}`. `FROZEN_MODEL = the form may recur later under a negator and exhaust a counterpart class`. Predictions: exact recurrence, negative governor, delayed/candidate role. `UNUSED_AT_FREEZE = {W05–W15}`. W15 exactly recurs under W11–W12 as delayed subject, with W14 defining equivalence `(C: كون B001; C: كفء B001; C: a4)`. W04 itself remains B001 in positive predication `(K: a2)`. `ولد B006` corroborates only the peer dimension `(C: ولد B006 peer)`, while its age mechanism is absent `(K: no age role)`. **Grade: medium-strong.** A precise later environment fulfills the seed, but only after its initial contextual mismatch.

### L21. W04 `أَحَدٌ` × `ءحد B003` — counted unit / production-cycle fork

**Initial image and implications.** `(E: ءحد B003)` creates arithmetic one, numeral composition, and a counted unit. It searches for partition, alternation, time cycle, or explicit count.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: all terminate`; `صمد B001–B007: B002 compact counted unit→F1`; `ولد B001–B006: B003 birth/yield→F2`; `كون B001–B006: B001 temporal occurrence→F2`; `كفء B001–B005: B005 alternating annual production→F2`; sibling `ءحد B001` direct constraint.

**SURFACE_SWEEP W01–W15.** F1 `E W04,W06; K predication/no numeral; Ø others`. F2 `E W04,W08,W10,W12,W14; K negation and absent year/count; Ø W01–W03,W05–W07,W09,W11,W13,W15`.

**F1 — one compact counted unit.** `GENERATING_SET = {ءحد B003, صمد B002}`. `FROZEN_MODEL = a single compact unit`; predictions: counting syntax or comparison to a second unit. `UNUSED_AT_FREEZE = {attachments and W14–W15}`. W14–W15 present a denied equivalent candidate `(C: كفء B001 contextual dimension)`, but W04 is a predicate with no counted noun or numeral compound `(K: a2; K: no count syntax)`. **Fork grade: weak.**

**F2 — counted annual production.** `(E: كفء B005) + (E: ولد B003) + (E: كون B001)` yields one unit in a timed birth/yield cycle with alternating groups. Predictions: year, positive production, group alternation, or count. `UNUSED_AT_FREEZE = {لم operators and actual voices}`. Both births and occurrence are negated, and no year/group/count appears `(K: W07–W12; K: W14 contextual B001)`. **Fork grade: unlikely.**

**Final seed grade: weak.** Every arithmetic-specific construction is absent.

### L22. W04 `أَحَدٌ` × `ءحد B004` — first/day timeline

**Initial image and implications.** `(E: ءحد B004)` offers ordinal “first” under annexation or Sunday. It predicts addition/iḍāfa, a day sequence, or broader calendar/age structure.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: all terminate`; `صمد B001–B007: B007 duration→timeline`; `ولد B001–B006: B006 birth-age→timeline`; `كون B001–B006: B001 time occurrence→timeline`; `كفء B001–B005: B005 annual cycle→timeline`; sibling `ءحد B001` direct local constraint.

**SURFACE_SWEEP W01–W15.** `E W04,W06,W08/W10,W12,W14 as remote timeline cues; K W04 predication, negated events, no calendar; Ø W01–W03,W05,W07,W09,W11,W13,W15`.

`GENERATING_SET = {ءحد B004, صمد B007, ولد B006, كون B001, كفء B005}`. `FROZEN_MODEL = a first day anchors an annual birth/age cycle that persists through time`. Predictions: iḍāfa/ordinal series, day/year, age peers, or recurring positive generation. `UNUSED_AT_FREEZE = {actual forms, attachments, and negation}`. W04 is indefinite nominative predicate without annexation; no day/year/age noun occurs; birth and occurrence clauses are negated `(K: QAC and attachments)`. **Grade: unlikely.** The remote timeline is internally connected but has no local foothold.

### L23. W04 `أَحَدٌ` × `ءحد B005` — separate unit and serial-candidate forks

**Initial image and implications.** `(E: ءحد B005)` supplies becoming separate or arriving one by one. It predicts a discrete unit, motion/separation, or distributive candidate sequence.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: B001 single worship target→F1`; `صمد B001–B007: B002 compactness→F1`; `ولد B001–B006: B005 non-derivation→F1 corroboration`; `كون B001–B006: B001 candidate occurrence→F2`; `كفء B001–B005: B001 matching second unit→F1/F2`; sibling `ءحد B002→F2 post-freeze`.

**SURFACE_SWEEP W01–W15.** F1 `E W03–W06; C W08,W10,W14–W15; K no separation verb; Ø operators/pronouns`. F2 `E W12,W14,W15; K no serial motion/plural; Ø W01–W11,W13`.

**F1 — separate compact unit.** `GENERATING_SET = {ءحد B005, صمد B002, ءله B001}`. `FROZEN_MODEL = one compact unit stands apart from derivation and matching units`. Predictions: no source/product and no equal. `UNUSED_AT_FREEZE = {W07–W15}`. W08/W10 and W14/W15 fit `(C: ولد B005; C: كفء B001)`, but no `انفرد`, `آحاد`, or arrival occurs `(K: form/role absence)`. **Fork grade: weak.**

**F2 — candidates excluded one by one.** `GENERATING_SET = {ءحد B005, كون B001, كفء B001}`. `FROZEN_MODEL = individual counterpart candidates appear serially and are denied`. Final B002 scope exhausts candidates `(C: ءحد B002)`, but syntax supplies one delayed indefinite subject, not serial arrivals `(K: a4)`. **Fork grade: weak.**

**Final seed grade: weak.** Compatible closure exists, but the branch's separation process is absent.

### L24. W04 `أَحَدٌ` × `ءحد B006` — terrain and camp forks

**Initial image and implications.** `(E: ءحد B006)` supplies Mount Uḥud, predicting a proper place, elevation, hard terrain, and potentially a camp/enclosure scene.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: all terminate`; `صمد B001–B007: B002 hard/elevated rock + B007 endurance→F1`; `ولد B001–B006: all terminate`; `كون B001–B006: B002 place→F1/F2`; `كفء B001–B005: B004 tent rear→F2`; sibling `ءحد B001` direct local constraint.

**SURFACE_SWEEP W01–W15.** `E W04,W06,W12,W14 as remote scene roles; K W04 indefinite predicate,W06 nominal predicate,W12 copula,W14 counterpart noun; Ø W01–W03,W05,W07–W11,W13,W15`.

**F1 — enduring elevated rock.** `GENERATING_SET = {ءحد B006, صمد B002, صمد B007, كون B002}`. `FROZEN_MODEL = a named mountain is a hard elevated place persisting under severity`. Predictions: proper-name, location, terrain, or hardship attachment. `UNUSED_AT_FREEZE = {actual morphology and sequence}`. None appears; W04 is indefinite predicate and W06/W12 have incompatible clause roles `(K: a2 and QAC)`. **Fork grade: unlikely.**

**F2 — mountain camp with rear panel.** Add `(E: كفء B004)` to place a tent at the location. It predicts cloth, house/tent, front/back, or locative relation; all are absent `(K: no scene participants; K: W14 contextual B001)`. **Fork grade: unlikely.**

**Final seed grade: unlikely.** The terrain dossier convergence is vivid but entirely nonlocal.

### L25. W05 `ٱللَّهُ` × `ءله B001` — reanchored reliance and rejected hierarchy/care forks

**Initial image and implications.** At W05 the worshipped branch is reactivated after W04 and immediately receives W06. The new local question is not merely “who?” but “what relation centers on the repeated name?”

**DOSSIER_SWEEP.** `قول B001–B016: B001 prior voice, B015→care fork`; `ءحد B001–B006: B001 prior unity`; `صمد B001–B007: B001→F1, B005→F3`; `ولد B001–B006: B003/B005→F1 corroboration, B004→F2, B002→F3`; `كون B001–B006: B004→F2, B003→F3, B001→F1`; `كفء B001–B005: B001→F1`; sibling `ءله B002` name recurrence dimension post-freeze.

**SURFACE_SWEEP W01–W15.** F1 `E W04–W06; C W01,W03,W08,W10,W12–W15; K absent worshipper; Ø W02,W07,W09,W11,W13`. F2/F3 `E W05,W06 plus remote W08/W10/W12/W13; K actual morphology/attachments; Ø remaining`.

**F1 — reanchored reliance center.** `GENERATING_SET = {ءله B001 at W05, prior ءحد B001, صمد B001, W05–W06 predication}`. `FROZEN_MODEL = the already unified referent is reset as the one-way center of intention/reliance`. Predictions: no source above, product below, peer beside. `UNUSED_AT_FREEZE = {W07–W15}`. W08/W10 and W12–W15 close all axes `(C: ولد B003; C: كون B001; C: كفء B001; C: ءحد B002)`. Exact name recurrence independently fixes the center `(C: ءله B002 distinct naming dimension)`. **Fork grade: strong.**

**F2 — master/submitted dependent.** `(E: صمد B001 السيد) + (E: ولد B004 مملوك) + (E: كون B004)` predicts servant and submission. Their actual forms are birth verb and copula, both in negated structures, not dependent/submission nouns `(K)`. **Fork grade: unlikely.**

**F3 — guarantor/parental care.** `(E: قول B015) + (E: صمد B005) + (E: كون B003) + (E: ولد B002)` predicts dependent/beneficiary attachment. W13 belongs to comparison W14 `(K: a2)`. **Fork grade: unlikely.**

**Final seed grade: strong.** The second occurrence's immediate W06 predicate makes F1 more locally controlled than at W03.

### L26. W05 `ٱللَّهُ` × `ءله B002` — exact-name reset before relational testing

**Initial image and implications.** `(E: ءله B002)` at W05 turns exact repetition into a temporal reset. It predicts a new predicate and later 3MS continuity.

**DOSSIER_SWEEP.** `قول B001–B016: B001→voiced-name context, B007→circulation fork, B005→attribution fork`; `ءحد B001–B006: B001 prior property/recurrence`; `صمد B001–B007: B001/B002 immediate rival predicates`; `ولد B001–B006: B005→generated-name/speech rejection`; `كون B001–B006: B001 later continuity`; `كفء B001–B005: B003 sound support`; sibling `ءله B001` kept separate.

**SURFACE_SWEEP W01–W15.** F1 `E W03,W05,W06; C W01,W02,W04,W08,W10,W12–W15; K no oath/vocative; Ø W07,W09,W11,W13 operators/anchor only`. F2/F3 account for all words as in L18, with W05 as seed.

**F1 — name reset.** `GENERATING_SET = {ءله B002 at W05, exact W03→W05 recurrence}`. `FROZEN_MODEL = the named referent is refreshed across an ayah boundary before a second predicate`. Predictions: immediate predication, stable 3MS continuation, and no new named competitor. `UNUSED_AT_FREEZE = {W06–W15}`. W06 is syntactically forced as predicate `(C: 112:2 a1)`; W08/W10/W12 and W13 remain 3MS-compatible `(C: QAC morphology)`. Basmala gives earlier name context `(C: opening-context)`. No oath/vocative occurs `(K)`. **Fork grade: strong.**

**F2 — formula circulation.** Add `(E: قول B007)` and use W04/W15 recurrence. Predict social transmission; exact repetition/sound fit, but no plural or report chain `(K)`. **Fork grade: weak.**

**F3 — generated/attributed name.** `(E: قول B005) + (E: ولد B005)` is defeated because W08/W10 target the referent, not the name or utterance, and W01 authorizes the content `(K)`. **Fork grade: unlikely.**

**Final seed grade: medium-strong.** Exact repetition and immediate predication are strong; branch-specific oath/vocative subuses remain absent.

### L27. W06 `ٱلصَّمَدُ` × `صمد B001` — reliance center and guardian fork

**Initial image and implications.** `(E: صمد B001)` supplies قصد/اعتماد toward a السيد who is approached in affairs and needs. It predicts directed dependents, asymmetry, and a center that is not itself dependent.

**DOSSIER_SWEEP.** `قول B001–B016: B001 voiced assertion, B015→F2`; `ءله B001–B002: B001→F1`; `ءحد B001–B006: B001→F1`; `ولد B001–B006: B003/B005→F1 corroboration, B002 parent-care→F2`; `كون B001–B006: B001→F1, B003 guarantee→F2`; `كفء B001–B005: B001→F1`; sibling `صمد B005` oversight and B002 solidity kept distinct.

**SURFACE_SWEEP W01–W15.** F1 `E W03–W06; C W01,W08,W10,W12–W15; K no approacher/need; Ø W02,W07,W09,W11,W13`. F2 `E W01,W06,W08/W10,W12/W13; K attachments; Ø remaining`.

**F1 — one-way dependence center.** `GENERATING_SET = {صمد B001, ءله B001, ءحد B001, W05–W06 predication}`. `FROZEN_MODEL = many possible needs point inward to one center; no reverse or lateral dependence is allowed`. Predictions: no parent/source, no derived child/product, no peer. `UNUSED_AT_FREEZE = {W07–W15}`. W08/W10 and W12–W15 exactly supply these exclusions `(C: ولد B003/B005; C: كون B001; C: كفء B001; C: ءحد B002)`. No approacher or need noun occurs `(K)`. **Fork grade: strong.**

**F2 — guardian/overseer.** `(E: قول B015) + (E: ولد B002) + (E: كون B003)` turns the reliable center into a guarantor caring for dependents. `FROZEN_MODEL = a superior safeguards dependents`; predictions: beneficiary/guarantee syntax. W13 is attached to equivalence, not guarantee, and no parent/care forms occur `(K: a2; K: morphology)`. **Fork grade: unlikely.**

**Final seed grade: strong.** F1 receives independent completion across every later rooted occurrence.

### L28. W06 `ٱلصَّمَدُ` × `صمد B002` — compact center, terrain, and sealed enclosure

**Initial image and implications.** `(E: صمد B002)` creates three distinguishable subimages from its own dossier: compact/cavityless body, hard/elevated terrain, and a stable rock. They must not be blended automatically.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate as expansion`; `ءله B001–B002: B001→compact center relation`; `ءحد B001–B006: B001→F1, B006→F2`; `ولد B001–B006: B003/B005→F1/F3 tests`; `كون B001–B006: B002→F2`; `كفء B001–B005: B001→F1, B004→F3`; siblings `صمد B003→F3 and B007→F2` kept role-distinct.

**SURFACE_SWEEP W01–W15.** F1 `E W03–W06; C W08,W10,W14–W15; K no physical body; Ø W01–W02,W07,W09,W11–W13`. F2/F3 `E W04,W06,W12,W14 plus branch dimensions; K their actual syntax; Ø remaining`.

**F1 — compact center with no passage.** `GENERATING_SET = {صمد B002 compact/no-cavity, ءحد B001, ءله B001}`. `FROZEN_MODEL = one compact center has no inner cavity or duplicate`. Predictions: no generative flow out, no derivational entry, no equal unit. `UNUSED_AT_FREEZE = {W07–W15}`. Active/passive W08/W10 and counterpart W14/W15 fulfill these `(C: ولد B003 event; C: ولد B005 derivation; C: كفء B001)`. No material/body/cavity construction occurs `(K)`. **Fork grade: strong.** This remains secondary.

**F2 — enduring elevated terrain.** `(E: ءحد B006) + (E: كون B002) + (E: صمد B007)` produces hard elevated place persisting under severity. Proper-name, location, and hardship roles are absent; W04/W06/W12 are predicate/copula forms `(K)`. **Fork grade: unlikely.**

**F3 — sealed enclosure.** `(E: صمد B003 stopper) + (E: كفء B004 rear covering)` adds closure boundaries; W08/W10 become imagined in/out traffic. `FROZEN_MODEL = a hard enclosure is sealed against passage`. No vessel, mouth, tent, cloth, or traffic attachment occurs `(K)`. **Fork grade: unlikely.**

**Final seed grade: strong.** Only the compact-center fork has independent passage-wide prediction and completion.

### L29. W06 `ٱلصَّمَدُ` × `صمد B003` — stopper, vessel, and blocked generation

**Initial image and implications.** `(E: صمد B003)` supplies a tight bottle stopper, predicting vessel, mouth, insertion, contents, and blocked traffic.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: all terminate`; `ءحد B001–B006: B001 single closure object`; `ولد B001–B006: B003/B005 in/out generation→F1`; `كون B001–B006: B002 place/container tested`; `كفء B001–B005: B004 rear-covering→F2`; siblings `صمد B002 solidity and B004 cloth closure` tested as distinct roles.

**SURFACE_SWEEP W01–W15.** F1 `E W06,W08,W10; C W14–W15 generic closure; K no vessel/opening; Ø others`. F2 `E W06,W12,W14; K no tent/cloth; Ø remaining`.

**F1 — sealed generative opening.** `GENERATING_SET = {صمد B003, ولد B003/B005 directional generation}`. `FROZEN_MODEL = a stopper blocks outward and inward generative passage`. Predictions: a vessel opening, flow, or contained substance. `UNUSED_AT_FREEZE = {actual morphology/attachments, W14–W15}`. Negated voice pair is directionally compatible `(C: active→passive)`, but no container/opening role and no `صماد` form occur `(K: W06 is الصمد predicate)`. **Fork grade: weak.**

**F2 — rear closure.** Add `(E: كفء B004)` and `(E: كون B002)`. `FROZEN_MODEL = a container/house has a sealed rear boundary`; every tent/cloth/spatial role is absent `(K)`. **Fork grade: unlikely.**

**Final seed grade: weak.** Generic closure is present, but distinctive vessel mechanics never appear.

### L30. W06 `ٱلصَّمَدُ` × `صمد B004` — wrapped head / cloth enclosure

**Initial image and implications.** `(E: صمد B004)` predicts a head wrapped with cloth rather than a turban. The only plausible cross-root extension is another sewn covering.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: all terminate`; `ءحد B001–B006: all terminate`; `ولد B001–B006: all terminate`; `كون B001–B006: B002 place→enclosure fork`; `كفء B001–B005: B004 tent cloth→enclosure fork`; siblings `صمد B003 stopper/B002 solidity` tested but not blended.

**SURFACE_SWEEP W01–W15.** `E W06,W12,W14 as remote cloth/place roles; K W06 predicate,W12 copula,W14 counterpart; Ø W01–W05,W07–W11,W13,W15`.

`GENERATING_SET = {صمد B004, كفء B004, كون B002}`. `FROZEN_MODEL = cloth binds a head or closes the rear of a shelter at a place`. Predictions: head, cloth, garment, sewing, tent/house, or spatial attachment. `UNUSED_AT_FREEZE = {all actual forms and remaining words}`. None occurs; joining two cloth branches cannot supply a local participant `(K: morphology and attachments)`. **Grade: unlikely.** A coherent material family exists, but no passage-local image forms.

### L31. W06 `ٱلصَّمَدُ` × `صمد B005` — attentive overseer

**Initial image and implications.** `(E: صمد B005)` predicts one overlooking an affair and caring about it.

**DOSSIER_SWEEP.** `قول B001–B016: B015 care→F1`; `ءله B001–B002: B001 hierarchy/dependence→F1`; `ءحد B001–B006: B001 single overseer`; `ولد B001–B006: B002 parent-care→F1`; `كون B001–B006: B003 guarantee→F1`; `كفء B001–B005: all terminate`; sibling `صمد B001 السيد` kept distinct.

**SURFACE_SWEEP W01–W15.** `E W01,W03–W06,W08/W10,W12/W13 as remote roles; K W01/W06/W08/W10/W12/W13 actual syntax; Ø W02,W07,W09,W11,W14–W15`.

`GENERATING_SET = {صمد B005, قول B015, ءله B001, ولد B002, كون B003}`. `FROZEN_MODEL = one superior attentively oversees and guarantees dependents`. Predictions: an affair, dependent/parental role, beneficiary, or guarantee construction. `UNUSED_AT_FREEZE = {actual attachments and all unselected words}`. W13 is comparison complement; birth roles are denied; no care/guarantee morphology occurs `(K)`. **Grade: unlikely.** Multi-root care imagery is lexically coherent but syntactically absent.

### L32. W06 `ٱلصَّمَدُ` × `صمد B006` — stick strike and deflection

**Initial image and implications.** `(E: صمد B006)` supplies a stick blow, requiring striker, instrument, patient, impact, and result.

**DOSSIER_SWEEP.** `قول B001–B016: B008 game stick→F1`; `ءله B001–B002: all terminate`; `ءحد B001–B006: all terminate`; `ولد B001–B006: all terminate`; `كون B001–B006: B002 place→F1`; `كفء B001–B005: B002 turning/deflection→F1`; siblings `صمد B002 hard ground` selected as separate role.

**SURFACE_SWEEP W01–W15.** `E W01,W06,W12,W14 as remote roles; K their actual speech/predicate/copula/counterpart syntax; Ø W02–W05,W07–W11,W13,W15`.

`GENERATING_SET = {صمد B006 strike, قول B008 stick, صمد B002 hard ground, كون B002 place, كفء B002 deflection}`. `FROZEN_MODEL = on hard ground, a stick hits a game-piece and diverts it`. Predictions: all five concrete roles. `UNUSED_AT_FREEZE = {actual morphology and attachments}`. None is present `(K: W01 speech, W06 nominative predicate, W12 copula, W14 accusative counterpart predicate)`. **Grade: unlikely.** This independently recreates L08's remote image and confirms that cross-seed convergence alone is insufficient without local roles.

### L33. W06 `ٱلصَّمَدُ` × `صمد B007` — persistence, harsh terrain, and production cycle

**Initial image and implications.** `(E: صمد B007)` supplies دوام/بقاء under severity. It predicts duration, repeated resistance to change, hardship, or a cycle endured over time.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: B001 stable center→F1`; `ءحد B001–B006: B001→F1, B006 mountain→F2`; `ولد B001–B006: B003 generation→F3`; `كون B001–B006: B001 time→F1/F3, B002 place→F2`; `كفء B001–B005: B005 annual cycle→F3`; siblings `صمد B002 rock/terrain→F2`.

**SURFACE_SWEEP W01–W15.** F1 `E W03–W06,W12; C W07,W09,W11,W08,W10,W14–W15; K no severity; Ø W01,W02,W13`. F2/F3 `E remote W04,W06,W08,W10,W12,W14; K actual forms; Ø remaining`.

**F1 — persistence through denied changes.** `GENERATING_SET = {صمد B007, ءله B001, ءحد B001, كون B001 time}`. `FROZEN_MODEL = one center persists while candidate changes fail to occur`. Predictions: repeated non-occurrence and several distinct denied transitions. `UNUSED_AT_FREEZE = {W07–W15}`. Three `لم` frames deny birth, being born, and counterpart-being `(C: morphology/sequence)`. No cold, drought, camel, or explicit hardship occurs `(K)`. **Fork grade: medium.**

**F2 — enduring mountain/rock.** `(E: ءحد B006) + (E: صمد B002) + (E: كون B002)` creates hard elevated terrain persisting under severity. Proper-name/place/hardship roles are absent `(K)`. **Fork grade: unlikely.**

**F3 — endurance through annual production.** `(E: ولد B003) + (E: كفء B005) + (E: كون B001)` creates recurring birth/yield across years. Actual generation and occurrence are negated, with no year/cycle `(K)`. **Fork grade: unlikely.**

**Final seed grade: medium.** Only abstract persistence receives independent temporal corroboration.

### L34. W08 `يَلِدْ` × `ولد B001` — outgoing offspring slot

**Initial image and implications.** `(E: ولد B001)` supplies offspring/lineage. Active W08 places the maintained 3MS subject on the source side, while W07 negates the relation. It predicts the inverse child position and a later peer test.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: B001 center relation`; `ءحد B001–B006: B001 unity, B002 final scope`; `صمد B001–B007: B001/B002 rival preconditions`; `كون B001–B006: B001 final occurrence`; `كفء B001–B005: B001 peer`; sibling `ولد B002/B003/B005/B006` retained as distinct role dimensions, B004 terminated.

**SURFACE_SWEEP W01–W15.** `E W03–W08; C W09–W10,W12–W15; K W08 has no overt offspring object and B001 is nominal; Ø W01–W02,W11,W13`.

`GENERATING_SET = {ولد B001, W07–W08 negated active morphology, maintained W03/W05 referent}`. `FROZEN_MODEL = the center's outgoing offspring slot is denied`. Predictions: same root in inverse orientation, then exclusion of a co-level/peer candidate. `UNUSED_AT_FREEZE = {W09–W15}`. W09–W10 provide coordinated passive inverse `(C: same root; C: voice)`, and W12–W15 deny an equal `(C: كون B001; C: كفء B001; C: ءحد B002)`. Earlier `صمد B001` gives asymmetric dependence and B002 compactness as separate corroborating geometries `(C)`. No offspring noun/object occurs `(K)`. **Grade: medium-strong.** Exact role completion outweighs the noun/verb distance.

### L35. W08 `يَلِدْ` × `ولد B002` — denied parent role and guardian fork

**Initial image and implications.** `(E: ولد B002)` supplies father/mother roles. Active W08 makes the subject a candidate parent/source and W07 denies it.

**DOSSIER_SWEEP.** `قول B001–B016: B015→guardian fork`; `ءله B001–B002: B001→guardian hierarchy`; `ءحد B001–B006: B001 unity`; `صمد B001–B007: B001 relied-on master + B005 oversight→guardian`; `كون B001–B006: B003 guarantee→guardian, B001 final`; `كفء B001–B005: B001 peer`; sibling `ولد B001/B003` direct lineage/event, others terminate.

**SURFACE_SWEEP W01–W15.** F1 `E W07–W08; C W09–W10,W14–W15; K no parent noun; Ø W01–W06,W11–W13`. F2 `E W01,W03,W06,W08,W12/W13; K attachments; Ø remaining`.

**F1 — parent position denied.** `GENERATING_SET = {ولد B002, W07–W08}`. `FROZEN_MODEL = the referent does not occupy a parental source role`. Prediction: the reciprocal child role is also denied. `UNUSED_AT_FREEZE = {W09–W15}`. Passive W10 fulfills it `(C: voice reversal)`; final peer denial closes lateral genealogy `(C: كفء B001)`. No `والد/والدة` form occurs `(K)`. **Fork grade: medium.**

**F2 — parental guardian.** `(E: قول B015) + (E: صمد B005/B001) + (E: كون B003) + (E: ءله B001)` creates a caring, relied-upon parent/guarantor. W13 is comparison complement, not beneficiary, and the parent event is negated `(K)`. **Fork grade: unlikely.**

**Final seed grade: medium.** Voice supplies role geometry; branch-specific parent nouns are absent.

### L36. W08 `يَلِدْ` × `ولد B003` — birth event, sealed passage, and annual cycle

**Initial image and implications.** `(E: ولد B003)` directly supplies occurrence of birth. Active voice creates an outward event; W07 inhibits it. The seed opens inverse birth, body/passages, and periodic production forks.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: B001 stable center`; `ءحد B001–B006: B001 unity`; `صمد B001–B007: B002 no-cavity→F2, B003 stopper→F2, B007 duration→F3`; `كون B001–B006: B001 time→F3/final`; `كفء B001–B005: B001 peer→F1, B005 annual production→F3`; sibling `ولد B005 derivation` kept separate.

**SURFACE_SWEEP W01–W15.** F1 `E W07–W08; C W09–W10,W12–W15; K absent birth participants; Ø W01–W06,W11,W13`. F2 `E W06,W08,W10; K no body/vessel; Ø others`. F3 `E W06,W08,W10,W12,W14; K negation/no year; Ø others`.

**F1 — two-direction birth closure.** `GENERATING_SET = {ولد B003, W07–W08 active negated event}`. `FROZEN_MODEL = outward birth is denied`; prediction: inverse patient orientation. `UNUSED_AT_FREEZE = {W09–W15}`. W10 repeats the root in passive voice, exactly fulfilling it `(C: a2/a3)`, and W14–W15 close peerhood `(C: كفء B001; C: ءحد B002)`. No mother/child/object scene appears `(K)`. **Fork grade: strong.**

**F2 — sealed generative passage.** `(E: صمد B002 no cavity) + (E: صمد B003 stopper)` turns birth into traffic through an opening. `FROZEN_MODEL = a sealed center permits neither outward nor inward generative passage`; W10 supplies inverse direction `(C)`, but no body, cavity, vessel, opening, or stopper form occurs `(K)`. **Fork grade: weak.**

**F3 — annual birth/yield.** `(E: كفء B005) + (E: كون B001) + (E: صمد B007)` creates recurring production through years. Both birth events are negated, no year/yield/groups appear, and W14 locally uses equivalence `(K)`. **Fork grade: unlikely.**

**Final seed grade: strong.** F1 is direct; F2/F3 are explicitly bounded remote forks.

### L37. W08 `يَلِدْ` × `ولد B004` — newborn/dependent and servitude fork

**Initial image and implications.** `(E: ولد B004)` supplies a newborn/young person or enslaved dependent. Active W08 predicts such a patient; the passage omits and negates it.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: B001→servitude`; `ءحد B001–B006: all terminate`; `صمد B001–B007: B001 master/dependence→servitude`; `كون B001–B006: B004 submission→servitude, B003 care tested`; `كفء B001–B005: all terminate`; sibling `ولد B001/B003` direct event roles.

**SURFACE_SWEEP W01–W15.** F1 `E W08; C W10 passive possibility; K no newborn noun/age; Ø remaining`. F2 `E W03,W06,W08/W10,W12; K forms and negation; Ø W01–W02,W04–W05,W07,W09,W11,W13–W15`.

**F1 — absent newborn.** `GENERATING_SET = {ولد B004 at W08}`. `FROZEN_MODEL = active birth would produce a newborn/dependent`. Predictions: overt child/young status. `UNUSED_AT_FREEZE = {W09–W15}`. Passive W10 offers only another negated event, not `وليد/وليدة`; no age/ownership appears `(K)`. **Fork grade: weak.**

**F2 — enslaved/submitted dependent.** `(E: ءله B001) + (E: صمد B001 master) + (E: كون B004 submission)` turns B004's enslaved sense into hierarchy. Predictions: slave noun, submission form, master–dependent attachment. All source forms are absent and W08/W10 are negated birth verbs `(K)`. **Fork grade: unlikely.**

**Final seed grade: weak.** Only generic patient expectation survives.

### L38. W08 `يَلِدْ` × `ولد B005` — derivation arrows, generated speech, and production cycle

**Initial image and implications.** `(E: ولد B005)` supplies one thing caused by/derived from another and, distinctly, newly generated speech. Active W08 orients the center as source.

**DOSSIER_SWEEP.** `قول B001–B016: B001/B005/B013/B016→F2`; `ءله B001–B002: B002 named proposition→F2, B001 center→F1`; `ءحد B001–B006: B001→F1`; `صمد B001–B007: B002 no-cavity→F1, B007 duration→F3`; `كون B001–B006: B001 occurrence→F1/F3`; `كفء B001–B005: B001 duplicate→F1, B005 production cycle→F3`; sibling `ولد B003` direct birth constraint.

**SURFACE_SWEEP W01–W15.** F1 `E W03–W08; C W09–W10,W12–W15; K generalized-form distance; Ø W01–W02,W11,W13`. F2 `E W01,W03,W08; K W08 subject and quote; Ø others`. F3 `E W06,W08,W10,W12,W14; K negation/no cycle; Ø others`.

**F1 — no source/product derivation.** `GENERATING_SET = {ولد B005, active W08, ءحد B001, صمد B002}`. `FROZEN_MODEL = no derivative proceeds from the compact one-center`. Predictions: deny the center as derived product and deny a duplicate. `UNUSED_AT_FREEZE = {W09–W15}`. Passive W10 and final W14–W15 fulfill both `(C: voice; C: كفء B001)`. Bare `ولد` remains literal birth locally; abstract derivation stays secondary `(K)`. **Fork grade: medium-strong.**

**F2 — generated or fabricated proposition.** `(E: قول B001/B005) + (E: ءله B002)` applies B005's generated-speech subbranch to W01–W04. Authorized quote and 3MS birth subject defeat it `(K: a1; K: W08/W10 morphology)`. **Fork grade: unlikely.**

**F3 — timed production cycle.** `(E: كفء B005) + (E: كون B001) + (E: صمد B007)` predicts annual recurring outputs; all are absent or negated `(K)`. **Fork grade: unlikely.**

**Final seed grade: medium-strong.** The derivation geometry converges; speech/cycle forks fail locally.

### L39. W08 `يَلِدْ` × `ولد B006` — birth-age peer and aging timeline

**Initial image and implications.** `(E: ولد B006)` supplies a peer of the same birth age. It predicts a co-level counterpart and, in a rival fork, age measured through years.

**DOSSIER_SWEEP.** `قول B001–B016: B009 negotiation among peers tested`; `ءله B001–B002: all terminate`; `ءحد B001–B006: B002 final candidate`; `صمد B001–B007: B007 duration→F2`; `كون B001–B006: B001 time→F2, B005 aged man→F2`; `كفء B001–B005: B001 equivalence→F1, B005 year/birth cycle→F2`; sibling `ولد B003` birth event constraint.

**SURFACE_SWEEP W01–W15.** F1 `E W08,W14; C W10,W12,W15; K no age/co-birth; Ø others`. F2 `E W06,W08,W12,W14; K no year/age/first person; Ø remaining`.

**F1 — co-birth peer denied.** `GENERATING_SET = {ولد B006, كفء B001}`. `FROZEN_MODEL = shared birth coordinate creates an equal peer`. Predictions: explicit counterpart candidate after birth material. `UNUSED_AT_FREEZE = {W09–W15}`. W14 supplies exact equivalence and W15 exhausts candidates under negation `(C: final clause)`, while both birth directions are denied `(C: W08/W10)`. No `لدة`, age, or co-birth pair occurs `(K)`. **Fork grade: medium.**

**F2 — age/year timeline.** `(E: كون B001/B005) + (E: كفء B005) + (E: صمد B007)` creates peers aging through annual cycles. No first-person reminiscence, age, year, or positive cycle appears `(K)`. **Fork grade: unlikely.**

**Final seed grade: medium.** The peer prediction is specific and fulfilled; its age mechanism is absent.

### L40. W10 `يُولَدْ` × `ولد B001` — denied position as offspring

**Initial image and implications.** `(E: ولد B001)` at passive W10 places the maintained subject in the offspring position and negates it. Backward replay asks whether W08 already denied the reciprocal source role.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: B001 center`; `ءحد B001–B006: B001 prior unity, B002 final scope`; `صمد B001–B007: B001/B002 rival center geometries`; `كون B001–B006: B001 final occurrence`; `كفء B001–B005: B001 peer`; sibling `ولد B002/B003/B005/B006` retained as separate role dimensions.

**SURFACE_SWEEP W01–W15.** `E W09–W10; C W03–W08 backward,W11–W15 forward; K no offspring noun/agent; Ø W01–W02,W13`.

`GENERATING_SET = {ولد B001, W09–W10 negated passive morphology}`. `FROZEN_MODEL = the center's incoming offspring slot is denied`. Predictions: backward source-side denial and forward peer closure. `UNUSED_AT_FREEZE = {W08 for explicit backward test, W11–W15}`. W08 supplies active reciprocal `(C: same-root voice sequence)`, and W14–W15 deny an equal `(C: كفء B001; C: ءحد B002)`. Earlier W04/W06 keep unity and center active `(C)`. No offspring noun or passive agent appears `(K)`. **Grade: medium-strong.** The occurrence's temporal position makes backward completion explicit.

### L41. W10 `يُولَدْ` × `ولد B002` — no parental source / rejected guardianship

**Initial image and implications.** `(E: ولد B002)` supplies parents. Passive W10 implies a source side while making the subject born; W09 negates the event.

**DOSSIER_SWEEP.** `قول B001–B016: B015→guardian fork`; `ءله B001–B002: B001→guardian`; `ءحد B001–B006: B001 unity`; `صمد B001–B007: B001/B005→guardian`; `كون B001–B006: B003→guardian, B001 final`; `كفء B001–B005: B001 peer`; sibling `ولد B001/B003` direct roles.

**SURFACE_SWEEP W01–W15.** F1 `E W09–W10; C W07–W08 backward,W14–W15; K absent parents/agent; Ø others`. F2 `E remote W01,W03,W06,W10,W12/W13; K attachments; Ø remaining`.

**F1 — absent parental source.** `GENERATING_SET = {ولد B002, passive W10, W09 negation}`. `FROZEN_MODEL = no parent/source stands above the referent`. Prediction: W08 denies the reciprocal parental role. `UNUSED_AT_FREEZE = {W08 backward, W11–W15}`. W08 does so `(C: active voice)`, and W14 denies a peer `(C)`. No parent noun or agent is expressed `(K)`. **Fork grade: medium.**

**F2 — parent-guarantor.** `(E: قول B015) + (E: صمد B001/B005) + (E: كون B003) + (E: ءله B001)` predicts care/beneficiary roles. W13 is comparison complement and birth is negated `(K)`. **Fork grade: unlikely.**

**Final seed grade: medium.** Symmetric role closure is present; parental lexemes are not.

### L42. W10 `يُولَدْ` × `ولد B003` — mirror completed, passage and cycle forks tested

**Initial image and implications.** `(E: ولد B003)` directly supplies a passive birth event. At this temporal point, W08's active event remains in memory; same-root voice reversal can now form a complete two-direction model.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: B001 center`; `ءحد B001–B006: B001 prior/B002 final`; `صمد B001–B007: B002/B003→sealed-passage fork, B007→cycle`; `كون B001–B006: B001→final/cycle`; `كفء B001–B005: B001→peer, B005→cycle`; sibling `ولد B005` derivation fork separate.

**SURFACE_SWEEP W01–W15.** F1 `E W07–W10; C W03–W06,W11–W15; K no birth participants; Ø W01–W02,W13`. F2 `E W06,W08,W10; K no opening/body; Ø rest`. F3 `E W06,W08,W10,W12,W14; K negation/no year; Ø rest`.

**F1 — completed source/patient closure.** `GENERATING_SET = {ولد B003 at W10, prior ولد B003 at W08, two لم frames, coordination, active→passive}`. `FROZEN_MODEL = both source and patient positions of birth are closed`. Predictions: next, a non-genealogical peer axis; at closure, return to opening unity. `UNUSED_AT_FREEZE = {W11–W15}`. Final W12–W15 supplies no-equivalent syntax and exact W04→W15 return `(C: كون B001; C: كفء B001; C: ءحد B002/B001 recurrence)`. **Fork grade: strong.**

**F2 — blocked passage.** `(E: صمد B002/B003)` gives cavity and stopper roles. Voice inversion fits out/in movement `(C)`, but no vessel/body/opening appears `(K)`. **Fork grade: weak.**

**F3 — annual production cycle.** `(E: صمد B007) + (E: كون B001) + (E: كفء B005)` predicts recurrent positive yield; negation and absent year/groups defeat it `(K)`. **Fork grade: unlikely.**

**Final seed grade: strong.** This seed independently reaches the full role-axis model from the passive endpoint.

### L43. W10 `يُولَدْ` × `ولد B004` — newborn state and servitude

**Initial image and implications.** `(E: ولد B004)` at passive W10 most naturally evokes a newborn/young dependent, with a secondary enslaved-person branch.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: B001→servitude`; `ءحد B001–B006: all terminate`; `صمد B001–B007: B001 master/reliance→servitude`; `كون B001–B006: B004 submission→servitude, B003 care tested`; `كفء B001–B005: all terminate`; sibling `ولد B001/B003` direct event roles.

**SURFACE_SWEEP W01–W15.** F1 `E W10; K negation/no newborn noun/age; Ø W01–W09,W11–W15`. F2 `E W03,W06,W10,W12; K forms; Ø remaining`.

**F1 — denied newborn state.** `GENERATING_SET = {ولد B004, passive W10}`. `FROZEN_MODEL = the subject would enter newborn/dependent status`. Predictions: `وليد/وليدة`, age, or ownership. `UNUSED_AT_FREEZE = {all other words/forms}`. None occurs; the event is negated `(K)`. **Fork grade: weak.**

**F2 — enslaved/submitted dependent.** `(E: ءله B001) + (E: صمد B001 master) + (E: كون B004)` predicts master, servant, and submission. W10/W12 have incompatible forms and no ownership attachment exists `(K)`. **Fork grade: unlikely.**

**Final seed grade: weak.** Passive morphology supports a patient state only generically.

### L44. W10 `يُولَدْ` × `ولد B005` — no derivational source, generated-speech and cycle forks

**Initial image and implications.** `(E: ولد B005)` makes the passive subject a candidate outcome derived from another source. It also retains the branch's separate newly generated speech dimension.

**DOSSIER_SWEEP.** `قول B001–B016: B001/B005/B013/B016→generated-speech fork`; `ءله B001–B002: B002→named speech, B001 center`; `ءحد B001–B006: B001`; `صمد B001–B007: B002→non-derivation, B007→cycle`; `كون B001–B006: B001→derivation/cycle`; `كفء B001–B005: B001→duplicate, B005→cycle`; sibling `ولد B003` direct local event.

**SURFACE_SWEEP W01–W15.** F1 `E W09–W10,W04,W06; C W07–W08 backward,W12–W15; K abstract-form distance; Ø W01–W03,W05,W11,W13`. F2/F3 account for all words through explicit K/Ø as below.

**F1 — no derived origin.** `GENERATING_SET = {ولد B005, passive W10, ءحد B001, صمد B002}`. `FROZEN_MODEL = the one compact center is not an outcome from another source`. Predictions: backward denial of producing role and forward no duplicate. `UNUSED_AT_FREEZE = {W08 backward, W11–W15}`. W08 and W14–W15 satisfy both `(C: active source denial; C: كفء B001)`. Bare W10 is literal birth; derivation remains secondary `(K)`. **Fork grade: medium-strong.**

**F2 — generated proposition.** `(E: قول B001/B005) + (E: ءله B002)` applies production to W01–W04. Quote authorization and 3MS subject continuity defeat it `(K)`. **Fork grade: unlikely.**

**F3 — annual output.** `(E: صمد B007) + (E: كون B001) + (E: كفء B005)` predicts year/cycle/yield; all absent or negated `(K)`. **Fork grade: unlikely.**

**Final seed grade: medium-strong.** The passive occurrence gives the generalized derivation fork its clearest orientation.

### L45. W10 `يُولَدْ` × `ولد B006` — peer anticipated immediately before `كُفُوًا`

**Initial image and implications.** `(E: ولد B006)` supplies same-birth-age peer. Because W10 is followed by the final clause, it makes a precise forward prediction: an explicit counterpart term.

**DOSSIER_SWEEP.** `قول B001–B016: B009 peer negotiation tested`; `ءله B001–B002: all terminate`; `ءحد B001–B006: B002→candidate scope`; `صمد B001–B007: B007→age-duration fork`; `كون B001–B006: B001→peer occurrence, B005→age fork`; `كفء B001–B005: B001→peer, B005→age/year`; sibling `ولد B003` local birth constraint.

**SURFACE_SWEEP W01–W15.** F1 `E W10; C W12,W14,W15,W08 backward; K no age/co-birth; Ø remaining`. F2 `E remote W06,W10,W12,W14; K no year/age/first person; Ø remaining`.

**F1 — co-birth peer denied.** `GENERATING_SET = {ولد B006 at W10}`. `FROZEN_MODEL = a birth coordinate would allow a same-level peer`. Prediction: immediate equivalence/candidate construction. `UNUSED_AT_FREEZE = {W11–W15}`. W14 is direct equivalence B001 and W15 exhausts candidates under negation `(C: كفء B001; C: ءحد B002)`. No age or `لدة` form occurs `(K)`. **Fork grade: medium.**

**F2 — aging timeline.** `(E: صمد B007) + (E: كون B005/B001) + (E: كفء B005)` creates coevals across years; no age/year/remembrance appears and births are negated `(K)`. **Fork grade: unlikely.**

**Final seed grade: medium.** The peer role is predicted with high positional specificity, though its birth-age mechanism is remote.

### L46. W12 `يَكُن` × `كون B001` — counterpart occurrence, persistence, and derivation

**Initial image and implications.** `(E: كون B001)` directly supplies occurrence/presence in time and copular predication. W11 negates it; W14/W15 determine what is prevented from occurring.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: B001 stable center`; `ءحد B001–B006: B001 backward/B002 final`; `صمد B001–B007: B007→F2, B001/B002 center`; `ولد B001–B006: B005→F3, B003 prior relation closure`; `كفء B001–B005: B001→F1, B005 cycle tested`; sibling `كون B002–B006` separately seeded.

**SURFACE_SWEEP W01–W15.** F1 `E W11–W15; C W03–W10; K no generic nonbeing; Ø W01–W02`. F2 `E W06,W11–W12; C repeated negation; K no hardship; Ø others`. F3 `E W08,W10,W12; K abstraction/negation scope; Ø others`.

**F1 — no counterpart enters occurrence.** `GENERATING_SET = {كون B001, W11–W12, كفء B001, W13 relation, delayed W15}`. `FROZEN_MODEL = no candidate equivalent occurs in relation to the maintained referent`. Predictions: exhaustive candidate, backward support from genealogy closure, terminal completion. `UNUSED_AT_FREEZE = {W04 recurrence, W07–W10}`. W15 activates B002 and W04 B001 in backward replay; W08/W10 already close genealogy `(C)`. Negation is restricted to W14 predicate, not generic being `(K: a3)`. **Fork grade: strong.**

**F2 — persistence through non-occurrence.** `(E: صمد B007)` turns negated occurrence into persistence. `FROZEN_MODEL = the center remains while candidate changes never occur`; repeated `لم` and three jussives corroborate `(C)`, but no severity scene occurs `(K)`. **Fork grade: medium.**

**F3 — derivational occurrence.** `(E: ولد B005)` asks whether generated products come into being. W08/W10 corroborate source/product closure `(C: ولد B005 dimension)`, while W12 negates only counterpart occurrence `(K: W14 predicate limits W12 scope)`. No generic creation event is asserted. **Fork grade: weak.**

**Final seed grade: strong.** F1 is exact; F2/F3 remain bounded dimensions.

### L47. W12 `يَكُن` × `كون B002` — equal standing and physical place

**Initial image and implications.** `(E: كون B002)` supplies place, position, rank, or standing. It forks naturally into social rank and terrain location.

**DOSSIER_SWEEP.** `قول B001–B016: B004/B010 authority tested→F1`; `ءله B001–B002: B001→F1`; `ءحد B001–B006: B001→F1, B006→F2`; `صمد B001–B007: B001 master→F1, B002 hard/elevated place→F2`; `ولد B001–B006: all terminate`; `كفء B001–B005: B001 equal standing→F1, B004 camp→F2`; sibling `كون B001` direct local constraint.

**SURFACE_SWEEP W01–W15.** F1 `E W03–W06,W12–W15; C authority/no-peer; K W12 copula not rank noun; Ø W01–W02,W07–W11`. F2 `E W04,W06,W12,W14; K no locative/terrain; Ø others`.

**F1 — no equal standing.** `GENERATING_SET = {كون B002 rank, كفء B001, صمد B001 master, ءحد B001}`. `FROZEN_MODEL = no candidate occupies equal rank beside the one center`. Predictions: comparison anchor and exhaustive subject. `UNUSED_AT_FREEZE = {W13,W15 attachments}`. Both arrive `(C: a2/a4)`. W12 is plain copula, not `مكانة/منزلة`, so rank is only a narrowing of W14 equivalence `(K)`. **Fork grade: medium.**

**F2 — hard elevated place/camp.** `(E: ءحد B006) + (E: صمد B002) + (E: كفء B004)` produces a mountain place with shelter. No proper-name, location, rock, tent, or cloth role occurs `(K)`. **Fork grade: unlikely.**

**Final seed grade: medium.** Rank has local comparison support; physical place does not.

### L48. W12 `يَكُن` × `كون B003` — guarantor/caretaker network

**Initial image and implications.** `(E: كون B003)` supplies guarantee and standing for another. It predicts guarantor, dependent/beneficiary, care, and responsibility attachments.

**DOSSIER_SWEEP.** `قول B001–B016: B015 care→F1`; `ءله B001–B002: B001 hierarchy/dependence→F1`; `ءحد B001–B006: B001 single guarantor`; `صمد B001–B007: B001 relied-on + B005 oversight→F1`; `ولد B001–B006: B002 parent role→F1`; `كفء B001–B005: all terminate`; sibling `كون B001` local copula constraint.

**SURFACE_SWEEP W01–W15.** `E remote W01,W03–W06,W08/W10,W12/W13; K W12 plain copula,W13 comparison complement,birth negation; Ø W02,W07,W09,W11,W14–W15`.

`GENERATING_SET = {كون B003, قول B015, ءله B001, صمد B001/B005, ولد B002}`. `FROZEN_MODEL = one relied-upon overseer guarantees dependents like a parent`. Predictions: beneficiary governed by the guarantor, affair/care construction, or responsibility verb. `UNUSED_AT_FREEZE = {actual W12–W15 attachments and all unselected words}`. W13 is governed by W14's comparison relation, not guarantee `(K: a2)`; W12 is `يكن`, not a guarantee form; parent roles are negated `(K)`. **Grade: unlikely.** A dense remote network has no local syntactic anchor.

### L49. W12 `يَكُن` × `كون B004` — submission/servitude hierarchy

**Initial image and implications.** `(E: كون B004)` supplies submission. It predicts a superior, submitted dependent, and hierarchy.

**DOSSIER_SWEEP.** `قول B001–B016: B010 authority→F1`; `ءله B001–B002: B001 worship→F1`; `ءحد B001–B006: B001 single apex`; `صمد B001–B007: B001 master→F1`; `ولد B001–B006: B004 enslaved dependent→F1`; `كفء B001–B005: B001 unequal/no-peer test`; sibling `كون B001` local constraint.

**SURFACE_SWEEP W01–W15.** `E remote W01,W03–W06,W10,W12,W14; C final no-peer only abstractly; K actual forms/no servant; Ø W02,W07–W09,W11,W13,W15`.

`GENERATING_SET = {كون B004, قول B010, ءله B001, صمد B001, ولد B004}`. `FROZEN_MODEL = a singular master stands above a submitted enslaved dependent`. Predictions: `استكان`, servant/ownership, governed patient. `UNUSED_AT_FREEZE = {actual morphology and attachments}`. None occurs; W10 is negated passive birth and W12 plain copula with counterpart predicate `(K)`. W14's no-equal relation cannot create submission. **Grade: unlikely.** Coherent hierarchy, zero local role realization.

### L50. W12 `يَكُن` × `كون B005` — aging/coeval timeline

**Initial image and implications.** `(E: كون B005)` supplies the old man labeled from `كُنْتُ`, predicting age, first-person reminiscence, and a temporal peer.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: all terminate`; `ءحد B001–B006: B004 day/calendar→F1`; `صمد B001–B007: B007 duration→F1`; `ولد B001–B006: B006 same-age peer→F1`; `كفء B001–B005: B001 peer + B005 annual cycle→F1`; sibling `كون B001` time dimension.

**SURFACE_SWEEP W01–W15.** `E remote W04,W06,W08/W10,W12,W14; K W12 3MS imperfect/no first person, no age/year; Ø W01–W03,W05,W07,W09,W11,W13,W15`.

`GENERATING_SET = {كون B005, كون B001 time, ءحد B004 day, صمد B007 duration, ولد B006 age-peer, كفء B005 year}`. `FROZEN_MODEL = an old speaker recalls youth while coevals are measured through annual cycles`. Predictions: first-person past form, age, day/year, peer pair. `UNUSED_AT_FREEZE = {actual QAC morphology and attachments}`. W12 is 3MS imperfect jussive under negation; no age/calendar/remembrance occurs `(K)`. **Grade: unlikely.** All distinctive features fail despite temporal branch connectivity.

### L51. W12 `يَكُن` × `كون B006` — persisting bad condition

**Initial image and implications.** `(E: كون B006)` supplies a bad state. `صمد B007` can add persistence under hardship.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: all terminate`; `ءحد B001–B006: all terminate`; `صمد B001–B007: B007→F1`; `ولد B001–B006: all terminate`; `كفء B001–B005: all terminate`; sibling `كون B001` local occurrence dimension.

**SURFACE_SWEEP W01–W15.** `E remote W06,W12; K W12 predicate is W14, no سوء/كينة/hardship; Ø W01–W05,W07–W11,W13–W15`.

`GENERATING_SET = {كون B006, صمد B007}`. `FROZEN_MODEL = a subject remains in a harsh bad state`. Predictions: bad-state noun/evaluation and severity. `UNUSED_AT_FREEZE = {W14 predicate attachment and remaining words}`. W14 is the actual predicate and means equivalence through B001; negation is not bad evaluation `(K: a3)`. No hardship occurs. **Grade: unlikely.** The seed is directly defeated by its predicate.

### L52. W14 `كُفُوًا` × `كفء B001` — equivalent, co-birth peer, and negotiating peer

**Initial image and implications.** `(E: كفء B001)` directly supplies equivalence/counterpart between two terms. W13 anchors one term; W15 is delayed as candidate for the other.

**DOSSIER_SWEEP.** `قول B001–B016: B009→F3`; `ءله B001–B002: B001 center→F1`; `ءحد B001–B006: B001 backward/B002 final→F1`; `صمد B001–B007: B001/B002 rival center geometries`; `ولد B001–B006: B006→F2, B003/B005 genealogy boundaries`; `كون B001–B006: B001→F1`; sibling `كفء B002–B005` separately seeded.

**SURFACE_SWEEP W01–W15.** F1 `E W11–W15; C W03–W10; K specialized marriage/war/reward subuses absent; Ø W01–W02`. F2 `E W08/W10,W14–W15; K no age; Ø rest`. F3 `E W01,W06,W14–W15 remote roles; K one-way speech/no peer; Ø rest`.

**F1 — no counterpart.** `GENERATING_SET = {كفء B001, كون B001, W13 complement, W15 delayed subject}`. `FROZEN_MODEL = no candidate occupies equivalence to the center`. Predictions: exhaustive candidate, backward unity, prior source/product closure. `UNUSED_AT_FREEZE = {W04, W08/W10}`. All arrive `(C: ءحد B001/B002 recurrence; C: ولد B003/B005)`. Specialized B001 subscenes are absent `(K)`. **Fork grade: strong.**

**F2 — co-birth peer.** `(E: ولد B006)` specifies equality by same birth age. W08/W10 deny birth and W15 exhausts candidates `(C)`, but age/co-birth is absent `(K)`. **Fork grade: medium.**

**F3 — equal negotiators.** `(E: قول B009) + (E: صمد B005 affair)` predicts reciprocal turns. W01 is one-way command and the peer is denied `(K)`. **Fork grade: unlikely.**

**Final seed grade: strong.** Direct syntax completes F1; F2/F3 expose narrower peer mechanisms.

### L53. W14 `كُفُوًا` × `كفء B002` — relation reversal, stick deflection, and polarity turn

**Initial image and implications.** `(E: كفء B002)` supplies tilting, turning, overturning, or diversion. It predicts a nearby reversal or changed trajectory.

**DOSSIER_SWEEP.** `قول B001–B016: B008→stick fork`; `ءله B001–B002: all terminate`; `ءحد B001–B006: B001/B002→polarity fork`; `صمد B001–B007: B006 strike + B002 ground→stick fork`; `ولد B001–B006: B003→voice-reversal fork`; `كون B001–B006: B001→polarity/occurrence`; sibling `كفء B001` decisive local constraint.

**SURFACE_SWEEP W01–W15.** F1 `E W08,W10,W14; C voice; K W14 noun predicate; Ø others`. F2 `E remote W01,W06,W12,W14; K forms; Ø rest`. F3 `E W04,W06,W07–W15; K semantic overreach; Ø W01–W03,W05`.

**F1 — active/passive turn.** `GENERATING_SET = {كفء B002, ولد B003 active→passive sequence}`. `FROZEN_MODEL = one relation is turned into its inverse orientation`. Predictions: same root, mirrored roles, adjacency. `UNUSED_AT_FREEZE = {voice/coordination details}`. All are exact `(C: W08→W10; C: a2)`. W14 itself is an accusative noun predicate contextually B001, not a turning verb `(K)`. **Fork grade: medium.**

**F2 — struck object diverted.** `(E: قول B008) + (E: صمد B006/B002)` creates stick, blow, ground, deflection. All local forms/roles fail `(K)`. **Fork grade: unlikely.**

**F3 — discourse polarity turn.** B002's turning image maps W01–W06 positive predication to W07–W15 repeated negation. Sequence corroborates a turn `(C)`, but no lexical turning event occurs and polarity change is generic `(K)`. **Fork grade: weak.**

**Final seed grade: medium.** Voice reversal is specific; local branch fit remains remote.

### L54. W14 `كُفُوًا` × `كفء B003` — varied endings / utterance form

**Initial image and implications.** `(E: كفء B003)` supplies differing rhyme endings. It predicts a voiced composition whose endings partly recur and partly differ.

**DOSSIER_SWEEP.** `قول B001–B016: B001 utterance/قصيدة range→F1`; `ءله B001–B002: B002 name recurrence`; `ءحد B001–B006: B001 first-last recurrence`; `صمد B001–B007: all terminate lexically`; `ولد B001–B006: B003 W10 ending only as sound`; `كون B001–B006: all terminate`; sibling `كفء B001` local constraint.

**SURFACE_SWEEP W01–W15.** `E W01,W14; C W04,W06,W10,W15; K W14 noun predicate/no poetry marker; Ø W02–W03,W05,W07–W09,W11–W13`.

`GENERATING_SET = {كفء B003, قول B001 voiced-composition range}`. `FROZEN_MODEL = a voiced sequence organizes nonidentical endings`. Predictions: recurrent final material plus variation. `UNUSED_AT_FREEZE = {ayah-final forms}`. `أحد/الصمد/يولد/أحد` all end in `د`, with exact first-last return `(C: acoustic sequence)`. W14 is not `إكفاء`, and no genre marker occurs `(K)`. **Grade: weak.** The sound pattern is real but corroborative and lexically remote.

### L55. W14 `كُفُوًا` × `كفء B004` — cloth enclosure / camp

**Initial image and implications.** `(E: كفء B004)` supplies sewn panels forming the rear of a tent/house. It predicts cloth, shelter, back/front, sewing, and location.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: all terminate`; `ءحد B001–B006: B006 mountain/camp location→F1`; `صمد B001–B007: B004 head cloth + B003 stopper + B002 hard place→F1`; `ولد B001–B006: all terminate`; `كون B001–B006: B002 place→F1`; sibling `كفء B001` local constraint.

**SURFACE_SWEEP W01–W15.** `E remote W04,W06,W12,W14; K their predicate/copula roles and no cloth; Ø W01–W03,W05,W07–W11,W13,W15`.

`GENERATING_SET = {كفء B004, ءحد B006, صمد B002/B003/B004 role-distinct closure cues, كون B002}`. `FROZEN_MODEL = at a hard mountain place, cloth closes the rear of a shelter`. Predictions: proper location, tent/house, cloth, sewing, spatial relation. `UNUSED_AT_FREEZE = {actual forms and attachments}`. None is present; W13 is comparison complement, not location `(K)`. **Grade: unlikely.** The enclosure network is exhaustive but nonlocal.

### L56. W14 `كُفُوًا` × `كفء B005` — annual alternating production

**Initial image and implications.** `(E: كفء B005)` supplies annual yield/birth and two groups alternating production. It predicts year, positive generation, alternation, and products.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: all terminate`; `ءحد B001–B006: B003 count + B004 day→cycle`; `صمد B001–B007: B007 duration→cycle`; `ولد B001–B006: B003 birth + B006 same-age→cycle`; `كون B001–B006: B001 time→cycle`; sibling `كفء B001` local constraint.

**SURFACE_SWEEP W01–W15.** `E remote W04,W06,W08,W10,W12,W14; K repeated negation,no year/groups,yield, W14 contextual B001; Ø W01–W03,W05,W07,W09,W11,W13,W15`.

`GENERATING_SET = {كفء B005, ءحد B003/B004, صمد B007, ولد B003/B006, كون B001}`. `FROZEN_MODEL = counted groups alternate births/yields across annual cycles`. Predictions: year/day/count, two productive groups, positive recurring output. `UNUSED_AT_FREEZE = {actual operators, voices, attachments}`. W08/W10 are both negated rather than alternating productive groups; W12 is negated; no calendar/count/product exists; W14 is counterpart predicate `(K)`. **Grade: unlikely.** This is the complete temporal-production fork and is decisively defeated.

### L57. W15 `أَحَدٌۢ` × `ءحد B001` — opening unity reactivated inside final denial

**Initial image and implications.** `(E: ءحد B001)` at the last token retrieves W04's positive unity cue. Local negative scope simultaneously predicts that a different `ءحد` branch may control W15's immediate syntax.

**DOSSIER_SWEEP.** `قول B001–B016: B016 boundary post-freeze`; `ءله B001–B002: B001/B002 maintained center`; `صمد B001–B007: B001 reliance and B002 compactness→two backward geometries`; `ولد B001–B006: B003/B005 prior axes`; `كون B001–B006: B001 final frame`; `كفء B001–B005: B001 counterpart`; sibling `ءحد B002` direct local dimension; B003–B006 terminate.

**SURFACE_SWEEP W01–W15.** `E W15 and backward W04; C W03–W14; K W15 local B002 scope against a second positive predication; Ø W01–W02 only as framing`.

**F1 — same form, changed role.** `GENERATING_SET = {ءحد B001 at W15, exact W04→W15 recurrence}`. `FROZEN_MODEL = opening unity is carried into a final test for a second/equal term`. Predictions: local no-counterpart syntax and a distinct negative-scope branch. `UNUSED_AT_FREEZE = {W11–W14 attachments and ءحد B002 dimension}`. W12–W14 supply negated equivalence and W15 is delayed subject under B002 scope `(C: كون B001; C: كفء B001; C: ءحد B002)`. It is not a second positive predicate `(K: a4)`. **Fork grade: strong.**

**F2 — reliance-center replay.** Backward replay links W04 B001 to W06 `(C: صمد B001)` and W08/W10/W14 closures. `FROZEN_MODEL = one reliance center has no source/product/peer`; all roles are complete, but W15 itself only reactivates rather than constructs that whole model. **Fork grade: strong.** Its function here is corroborative replay.

**F3 — compact-center replay.** Replace with `(C: صمد B002)` and `(C: ولد B005)`: one compact unit has no generative origin/output or duplicate. Physical literalization remains constrained `(K)`. **Fork grade: strong.** It remains a secondary simulation.

**Final seed grade: strong.** W15 reorganizes several earlier cues while preserving its own negative-scope syntax.

### L58. W15 `أَحَدٌۢ` × `ءحد B002` — exhaustive candidate closure

**Initial image and implications.** `(E: ءحد B002)` is directly licensed by W11–W12 negative scope and W15's delayed-subject role. It predicts an exhaustively denied candidate class.

**DOSSIER_SWEEP.** `قول B001–B016: B016 boundary corroboration`; `ءله B001–B002: B001/B002 maintained referent`; `صمد B001–B007: B001/B002 rival center geometries`; `ولد B001–B006: B003/B005 genealogy boundaries, B006 peer dimension`; `كون B001–B006: B001→occurrence frame`; `كفء B001–B005: B001→candidate class`; sibling `ءحد B001` backward reactivation; B003–B006 terminate.

**SURFACE_SWEEP W01–W15.** `E W11–W15; C W03–W10; K no arithmetic/ordinal/separation/place reading; Ø W01–W02`.

`GENERATING_SET = {ءحد B002, كون B001, كفء B001, W13 complement, a3/a4}`. `FROZEN_MODEL = every possible candidate for equivalence is denied`. Predictions: earlier genealogical candidates removed, exact opening-form return, no unresolved role after W15. `UNUSED_AT_FREEZE = {W04, W08/W10, ayah/sound sequence}`. All corroborate `(C: ءحد B001 recurrence; C: ولد B003 active/passive; C: final acoustic return)`. B006 supplies only a remote peer mechanism `(C: ولد B006 peer dimension)`, while age is absent `(K: no age role)`. **Grade: strong.** Branch, scope, case, attachment, sequence, and closure coincide.

### L59. W15 `أَحَدٌۢ` × `ءحد B003` — final arithmetic candidate / defeated cycle

**Initial image and implications.** `(E: ءحد B003)` predicts arithmetic one or numeral composition at the last word.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: all terminate`; `صمد B001–B007: B002 compact counted unit`; `ولد B001–B006: B003→production cycle`; `كون B001–B006: B001 time`; `كفء B001–B005: B005 alternating cycle, B001 local constraint`; sibling `ءحد B002` decisive negative-scope constraint.

**SURFACE_SWEEP W01–W15.** F1 `E W06,W15; K no numeral/count syntax; Ø others`. F2 `E remote W08,W10,W12,W14,W15; K negation/no cycle; Ø rest`.

**F1 — one counted counterpart.** `GENERATING_SET = {ءحد B003, صمد B002}`. `FROZEN_MODEL = one compact unit is tested against another`. Predictions: a counted second unit or numeral construction. `UNUSED_AT_FREEZE = {W01–W14 except W06}`. W14 does create an equivalence relation `(C: كفء B001)`, but W15 is delayed subject under negation, not numeral, and no counted noun occurs `(K: a4)`. **Fork grade: weak.**

**F2 — final count in a production cycle.** `(E: ولد B003) + (E: كون B001) + (E: كفء B005)` predicts counted annual output/alternation. Birth/occurrence are negated and no year/count exists `(K)`. **Fork grade: unlikely.**

**Final seed grade: weak.** B002 exhaustiveness, not arithmetic, controls the token.

### L60. W15 `أَحَدٌۢ` × `ءحد B004` — ordinal/day timeline at closure

**Initial image and implications.** `(E: ءحد B004)` predicts first/annexation or Sunday, with possible calendar-age extensions.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: all terminate`; `صمد B001–B007: B007 duration`; `ولد B001–B006: B006 birth-age`; `كون B001–B006: B001 time, B005 aging`; `كفء B001–B005: B005 year cycle, B001 local constraint`; sibling `ءحد B002` local scope constraint.

**SURFACE_SWEEP W01–W15.** `E remote W06,W08/W10,W12,W14,W15; K W15 delayed subject,no iḍāfa/day/year/age; Ø W01–W05,W07,W09,W11,W13`.

`GENERATING_SET = {ءحد B004, صمد B007, ولد B006, كون B001/B005, كفء B005}`. `FROZEN_MODEL = a first/day cue anchors age and annual cycles`. Predictions: ordinal annexation, calendar, age peer, positive recurrence. `UNUSED_AT_FREEZE = {actual final syntax and morphology}`. None appears; W15's indefinite nominative role is exhaustive candidate under negation `(K)`. **Grade: unlikely.** Full temporal branch traversal yields no local foothold.

### L61. W15 `أَحَدٌۢ` × `ءحد B005` — serial individuals and separate-unit replay

**Initial image and implications.** `(E: ءحد B005)` evokes individuals arriving one by one or a unit becoming separate. Final position offers serial-candidate and compact-unit forks.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: B001 one center→F2`; `صمد B001–B007: B002 compactness→F2`; `ولد B001–B006: B005 non-derivation→F2`; `كون B001–B006: B001 candidate occurrence→F1`; `كفء B001–B005: B001 equivalence→F1/F2`; sibling `ءحد B002 exhaustive scope` post-freeze.

**SURFACE_SWEEP W01–W15.** F1 `E W12,W14,W15; C negative scope; K no serial movement/plural; Ø W01–W11,W13`. F2 `E backward W03–W06,W15; C W08,W10,W14; K no separation form; Ø operators`.

**F1 — candidates one by one.** `GENERATING_SET = {ءحد B005, كون B001, كفء B001}`. `FROZEN_MODEL = individual peers enter the comparison slot serially and are denied`. Predictions: distributive motion, plurality, or serial candidate entry. `UNUSED_AT_FREEZE = {all surface words except W12,W14,W15}`. B002 exhaustiveness supports all candidates `(C: ءحد B002)`, but syntax supplies one delayed indefinite subject, no plural `آحاد` or arrival `(K)`. **Fork grade: weak.**

**F2 — separate compact center.** `(E: صمد B002) + (E: ءله B001)` yields an isolated compact unit; W08/W10/W14 deny derivation/duplicate `(C: ولد B005; C: كفء B001)`. No separation event occurs `(K)`. **Fork grade: weak.**

**Final seed grade: weak.** Compatible geometry does not instantiate B005's process.

### L62. W15 `أَحَدٌۢ` × `ءحد B006` — mountain/place fork defeated at closure

**Initial image and implications.** `(E: ءحد B006)` predicts Mount Uḥud as proper place, hard elevation, and possibly camp.

**DOSSIER_SWEEP.** `قول B001–B016: all terminate`; `ءله B001–B002: all terminate`; `صمد B001–B007: B002 hard/elevated + B007 endurance→F1`; `ولد B001–B006: all terminate`; `كون B001–B006: B002 place→F1`; `كفء B001–B005: B004 tent→F2, B001 local constraint`; sibling `ءحد B002` local scope constraint.

**SURFACE_SWEEP W01–W15.** `E remote W04,W06,W12,W14,W15; K W15 delayed indefinite subject/no place; Ø W01–W03,W05,W07–W11,W13`.

**F1 — enduring hard mountain.** `GENERATING_SET = {ءحد B006, صمد B002/B007, كون B002}`. `FROZEN_MODEL = a named hard elevated place persists under severity`. Predictions: proper-name, locative, terrain, hardship. `UNUSED_AT_FREEZE = {all actual word forms, attachments, and sequence evidence}`. None occurs; W15 is candidate subject in comparison `(K: a4)`. **Fork grade: unlikely.**

**F2 — mountain camp.** Add `(E: كفء B004)`; predict tent/cloth/place attachments. None occurs and W14 is equivalence B001 `(K)`. **Fork grade: unlikely.**

**Final seed grade: unlikely.** Exact local syntax defeats both terrain forks.

## Constructional, morphosyntactic, morphemic, temporal, and acoustic sweep

### C01. W02 `هُوَ` — standalone pronoun seed

**Initial image.** `(E: W02 3MS pronoun)` creates an unresolved referent pointer. It predicts local identification, predication, and later compatible reference.

**ROOT_SWEEP.** All seven full dossiers visited; selected `(E: ءله B002)` for naming and `(E: ءحد B001)` for the first predicate; `قول B001` supplies the containing quote; all other branches terminate before freeze. **SURFACE_SWEEP:** `E W01–W04; C W05–W06,W08,W10,W12–W15; Ø W07,W09,W11 as operators; K none beyond apposition confidence`.

`GENERATING_SET = {W02 pronoun, W03 possible apposition, W04 predicate}`. `FROZEN_MODEL = point → name → predicate`. Predictions: name recurrence, 3MS verbal continuity, later 3MS pronoun. `UNUSED_AT_FREEZE = {W05–W15}`. W05 repeats the name; W08/W10/W12 are 3MS; W13 contains 3MS pronoun `(C: QAC morphology and sequence)`. W03 apposition is strongly licensed but medium confidence `(K: a3 confidence)`. Rival: treating W02 as a permanently unresolved pronoun dies at W03–W04. **Grade: strong.** The very next words resolve the pointer and later forms preserve it.

### C02. W06 `الـ` — definiteness on `ٱلصَّمَدُ`

**Initial image.** `(E: W06 determiner prefix)` marks W06 as definite, unlike indefinite W04/W14/W15. It predicts a stable predication tied to repeated W05 rather than an unrestricted candidate class.

**ROOT_SWEEP.** All seven dossiers visited; selected `صمد B001` and B002 as rival predicate images, `ءله B002` name recurrence, `ءحد B001/B002` for definiteness contrast, and `كفء B001` for final indefinite comparison. **SURFACE_SWEEP:** `E W04–W06; C W14–W15; K morphology alone cannot choose صمد branch; Ø W01–W03,W07–W13`.

`GENERATING_SET = {W05–W06 predication, W06 definiteness}`. `FROZEN_MODEL = a repeated proper name receives a definite predicate before later indefinite candidates are negated`. Predictions: same referent, positive assertion before unrestricted negation. `UNUSED_AT_FREEZE = {W07–W15}`. Final W14/W15 are indefinite and occur under negation `(C: QAC)`. The determiner does not lexically decide reliance versus solidity `(K: branch neutrality)`. **Grade: medium.** It helps organize positive center versus later candidate class but does not generate a vivid image alone.

### C03. W07 first `لَمْ` — first inhibition operator

**Initial image.** `(E: W07 NEG)` opens an unresolved negative complement and predicts a governed jussive event.

**ROOT_SWEEP.** All dossiers visited; selected `ولد B003` for the immediate event and B005 as secondary derivation; all others terminate before freeze. **SURFACE_SWEEP:** `E W07–W08; C W09–W10,W11–W15; K W01–W06 are not retroactively negated; Ø W01–W06 otherwise`.

`GENERATING_SET = {W07, W08 jussive attachment}`. `FROZEN_MODEL = inhibit an outward birth event`. Predictions: complement immediately follows, repeated operator may test inverse/other relations. `UNUSED_AT_FREEZE = {W09–W15}`. W09 repeats `لم`, W10 reverses voice, W11 repeats again with a new predicate frame `(C: morphology/attachments)`. Scope begins at W07 and does not negate prior positive predications `(K: sequence)`. **Grade: strong.** Operator expectation and complement are exact.

### C04. W09 `وَ` — first conjunction morpheme

**Initial image.** `(E: W09 conjunction)` predicts continuation coordinated with the preceding birth clause.

**ROOT_SWEEP.** All dossiers visited; selected `ولد B003` same-root event, `كفء B002` only as post-freeze reversal image, and rejected `كفء B005` alternation cycle. **SURFACE_SWEEP:** `E W07–W10; C W11–W15; K no productive alternation cycle; Ø W01–W06`.

`GENERATING_SET = {W09 conjunction, W08/W10 coordination attachment}`. `FROZEN_MODEL = add a parallel second test to the first denied relation`. Predictions: structural parallelism with a meaningful changed feature. `UNUSED_AT_FREEZE = {W09 negator, W10 voice}`. The negator repeats and voice changes active→passive `(C)`. `كفء B005`'s alternating production is defeated because both events are negated and no groups/year occur `(K)`. **Grade: strong.** The conjunction preserves the root while enabling role reversal.

### C05. W09 second `لَمْ` — inverse-event inhibition

**Initial image.** `(E: W09 NEG)` predicts another governed jussive; preceding W08 makes an inverse same-root event especially informative.

**ROOT_SWEEP.** All dossiers visited; selected `ولد B003/B005`; `صمد B002/B003` tested for blocked passage after freeze; all other branches terminate. **SURFACE_SWEEP:** `E W09–W10; C W07–W08 backward,W11–W15 forward; K no physical passage; Ø W01–W06`.

`GENERATING_SET = {second لم, passive W10 attachment}`. `FROZEN_MODEL = inhibit the same relation with subject now in patient/product position`. Predictions: backward active counterpart and forward new relation type. `UNUSED_AT_FREEZE = {W08 backward test, W11–W15}`. Both are supplied `(C: voice mirror; C: final counterpart frame)`. No body/vessel licenses a literal blocked passage `(K)`. **Grade: strong.** This morpheme turns repetition into inverse role closure.

### C06. W11 `وَ` — cross-ayah continuation morpheme

**Initial image.** `(E: W11 conjunction)` carries the negative series across the 112:3→112:4 boundary. It predicts another coordinated exclusion but allows a new root/role.

**ROOT_SWEEP.** All dossiers visited; selected `كون B001`, `كفء B001`, `ءحد B002`; `كفء B005` alternating-cycle image tested and rejected. **SURFACE_SWEEP:** `E W07–W12; C W13–W15; K no new topic/production cycle; Ø W01–W06`.

`GENERATING_SET = {W11 conjunction, prior two negated clauses}`. `FROZEN_MODEL = continue the same inhibitory program with a third relational test`. Predictions: repeated negator, jussive complement, role not redundant with birth. `UNUSED_AT_FREEZE = {W11 negator,W12–W15}`. W12 is jussive under `لم` and W14/W15 test equivalence, not genealogy `(C)`. **Grade: strong.** The conjunction preserves operation while changing relational axis.

### C07. W11 third `لَمْ` — counterpart-occurrence inhibition

**Initial image.** `(E: W11 NEG)` predicts a third jussive complement; after two birth relations, a different relation is expected to avoid redundancy.

**ROOT_SWEEP.** All dossiers visited; selected `كون B001`, `كفء B001`, `ءحد B002`; `صمد B007` persistence only post-freeze. **SURFACE_SWEEP:** `E W11–W15; C W07–W10 repetition; K no generic eternal claim from لم alone; Ø W01–W06`.

`GENERATING_SET = {third لم, W12 particle-complement}`. `FROZEN_MODEL = inhibit occurrence of a relation still awaiting its predicate/subject`. Predictions: jussive W12, completed predicate, candidate subject. `UNUSED_AT_FREEZE = {W13–W15}`. Attachments fill all roles `(C: a2–a4)`. Repetition can corroborate `صمد B007` persistence but cannot lexicalize duration by itself `(K)`. **Grade: strong.** The operator remains unresolved until the last word.

### C08. W13 `لَـ` — relation-anchor preposition

**Initial image.** `(E: W13 preposition)` opens a relational complement around the 3MS pronoun. It predicts a governing predicate rather than an independent possession/care scene.

**ROOT_SWEEP.** All dossiers visited; selected `كفء B001` as governor and `كون B001` frame; tested `كون B003`, `قول B015`, and `صمد B005` care/guarantee rival, then rejected it. **SURFACE_SWEEP:** `E W12–W15; C W03/W05 referent; K care/benefit/possession overread; Ø W01–W02,W04,W06–W11`.

`GENERATING_SET = {W13 لـ, W14 prep-complement attachment}`. `FROZEN_MODEL = equivalence is evaluated relative to him`. Predictions: comparison predicate and candidate subject. `UNUSED_AT_FREEZE = {W14–W15}`. Both follow and are structurally fixed `(C)`. W13 cannot be reassigned as beneficiary of guarantee/care because a2 governs it from W14 `(K)`. **Grade: strong.** The preposition fixes one term of the final comparison.

### C09. W13 `هُۥ` — 3MS referent reactivation

**Initial image.** `(E: W13 3MS pronoun)` calls the maintained referent back without renaming it.

**ROOT_SWEEP.** All dossiers visited; selected `ءله B002` name recurrence, `ءحد B001` and `صمد B001/B002` as prior properties, `كفء B001` as current relation; all care/guarantee branches rejected by attachment. **SURFACE_SWEEP:** `E W03/W05,W13–W15; C W02,W08,W10,W12; K no explicitly annotated full-surah coreference edge; Ø W01,W04,W06–W07,W09,W11`.

`GENERATING_SET = {W13 pronoun, prior repeated W03/W05 name}`. `FROZEN_MODEL = the named center is reactivated as one term in the final comparison`. Predictions: 3MS compatibility and no intervening named competitor. `UNUSED_AT_FREEZE = {W02/W08/W10/W12 person features,W14–W15}`. All are compatible `(C: QAC)`. Full coreference is a sequence inference, not an attachment label `(K)`. **Grade: medium-strong.** Morphological continuity is strong, with one inferential boundary.

### C10. W01→W02–W04 — quoted-complement attachment

**Initial image.** `(E: attachment a1)` makes W01 a speech command outside a W02–W04 content span.

**ROOT_SWEEP.** All dossiers visited; selected `قول B001`, `ءله B002`, `ءحد B001`; `قول B013/B016` retained as rival content-types, not attachment meanings. **SURFACE_SWEEP:** `E W01–W04; C W05–W15 as continued same-referent discourse; K W05–W15 excluded from this forced quote span; Ø none`.

`GENERATING_SET = {W01 imperative, a1, W02–W04}`. `FROZEN_MODEL = command → internally complete quoted proposition`. Predictions: W02–W04 have referent and predicate; later material may continue the referent without belonging to a1. `UNUSED_AT_FREEZE = {a2/a3,W05–W15}`. A2/a3 complete the proposition; W05 name recurrence continues reference `(C)`. Extending a1 beyond W04 is prohibited `(K)`. **Grade: strong.** Exact attachment explains opening order and boundary.

### C11. W03–W04 — first predication attachment

**Initial image.** `(E: attachment 112:1 a2)` fixes W04 as nominative predicate of W03.

**ROOT_SWEEP.** All dossiers visited; selected `ءله B002` name and `ءحد B001` unity; `ءحد B002–B006` constrained by positive predicate syntax. **SURFACE_SWEEP:** `E W03–W04; C W05–W06,W15; K W15 has different role; Ø W01–W02,W07–W14`.

`GENERATING_SET = {W03 name, W04 predicate, a2}`. `FROZEN_MODEL = positive unity is assigned to the named referent`. Predictions: repeated name can receive a second predicate; repeated W04 form may later change role. `UNUSED_AT_FREEZE = {W05–W15}`. Both occur `(C: W05–W06 predication; C: W15 delayed subject)`. Arithmetic/day/mountain branches are defeated locally `(K)`. **Grade: strong.**

### C12. W02–W03 — apposition attachment

**Initial image.** `(E: attachment 112:1 a3)` allows W03 to appose W02, turning unresolved pronoun into named referent.

**ROOT_SWEEP.** All dossiers visited; selected `ءله B002`; all lexical scene branches terminate. **SURFACE_SWEEP:** `E W02–W04; C W05,W08,W10,W12–W13; K a3 medium confidence; Ø W01,W06–W07,W09,W11,W14–W15`.

`GENERATING_SET = {W02 pronoun,W03 name,a3}`. `FROZEN_MODEL = pointing expression is resolved by a name before predication`. Predictions: W04 predicate and later reference continuity. `UNUSED_AT_FREEZE = {W04–W15}`. W04 and later 3MS forms fulfill this `(C)`. Apposition is strongly licensed but medium confidence, so the model must tolerate another compatible nominal analysis `(K)`. **Grade: medium-strong.**

### C13. W05–W06 — second predication attachment

**Initial image.** `(E: attachment 112:2 a1)` fixes W06 as nominative predicate of repeated W05.

**ROOT_SWEEP.** All dossiers visited; selected `ءله B001/B002`, `صمد B001` and B002 as rival images, `ءحد B001` prior property; all other `صمد` branches become tested forks, not merged meaning. **SURFACE_SWEEP:** `E W03–W06; C W08,W10,W12–W15; K physical/dependence role omissions; Ø W01–W02,W07,W09,W11,W13`.

F1 `GENERATING_SET = {a1, ءله B001, صمد B001}`; `FROZEN_MODEL = named one is the relied-upon center`; predictions: no reverse/lateral dependence. F2 uses `(E: صمد B002)`; `FROZEN_MODEL = named one is compact/cavityless`; predictions: no in/out generation or duplicate. `UNUSED_AT_FREEZE = {W07–W15}` for both. W08/W10/W14–W15 fulfill both relationally `(C)`; missing dependents or physical body constrain literalization `(K)`. **Grade: strong.** The attachment hosts two separate, independently testable branch geometries.

### C14. W07–W08 — first particle-complement attachment

**Initial image.** `(E: attachment 112:3 a1)` fixes active W08 as jussive complement of W07.

**ROOT_SWEEP.** All dossiers visited; selected `ولد B003` direct event and B005 secondary derivation; all physical/production forks tested later. **SURFACE_SWEEP:** `E W07–W08; C W09–W10,W11–W15; K no overt birth object; Ø W01–W06`.

`GENERATING_SET = {W07,W08,a1,ولد B003}`. `FROZEN_MODEL = outward birth event is denied`. Prediction: inverse same-root relation. `UNUSED_AT_FREEZE = {W09–W15}`. W10 fulfills it in passive voice `(C)`. B005 derivation is secondary because bare W08 is literal event form `(K)`. **Grade: strong.**

### C15. W08↔W10 — coordination attachment

**Initial image.** `(E: attachment 112:3 a2)` makes W10 parallel to W08 across W09.

**ROOT_SWEEP.** All dossiers visited; selected `ولد B003/B005`, `كفء B002` reversal after freeze; rejected `كفء B005` alternating production. **SURFACE_SWEEP:** `E W07–W10; C W11–W15; K no positive alternation; Ø W01–W06`.

`GENERATING_SET = {a2,same root,active W08,passive W10,repeated لم}`. `FROZEN_MODEL = one relation is tested in both source and patient orientations`. Predictions: non-genealogical peer test next. `UNUSED_AT_FREEZE = {W11–W15}`. Final counterpart frame fulfills it `(C)`. B002 turning is a secondary image; B005 cycle is defeated `(K)`. **Grade: strong.**

### C16. W09–W10 — second particle-complement attachment

**Initial image.** `(E: attachment 112:3 a3)` fixes passive W10 as jussive complement of W09's negator.

**ROOT_SWEEP.** All dossiers visited; selected `ولد B003/B005`; `صمد B002/B003` tested as passage imagery; others terminate. **SURFACE_SWEEP:** `E W09–W10; C W07–W08 backward,W11–W15; K no vessel/body; Ø W01–W06`.

`GENERATING_SET = {W09 negator,W10 passive,a3}`. `FROZEN_MODEL = the referent's born/product role is denied`. Predictions: backward source denial and forward peer denial. `UNUSED_AT_FREEZE = {W08,W11–W15}`. Both occur `(C)`. Sealed-passage imagery lacks participants `(K)`. **Grade: strong.**

### C17. W11–W12 — third particle-complement attachment

**Initial image.** `(E: attachment 112:4 a1)` fixes W12 as jussive complement of the third negator.

**ROOT_SWEEP.** All dossiers visited; selected `كون B001`; `صمد B007` persistence tested post-freeze; others terminate until W14 predicate resolves the frame. **SURFACE_SWEEP:** `E W11–W12; C W13–W15,W07–W10; K no generic nonbeing/eternity; Ø W01–W06`.

`GENERATING_SET = {W11,W12,a1,كون B001}`. `FROZEN_MODEL = a third relation is prevented from occurring but remains unspecified`. Predictions: complement roles after W12. `UNUSED_AT_FREEZE = {W13–W15}`. Comparison anchor, predicate, and delayed subject complete it `(C)`. **Grade: strong.**

### C18. W13 governed by W14 — prepositional-complement attachment

**Initial image.** `(E: attachment 112:4 a2)` fixes W13's pronoun as complement of W14, establishing one side of comparison.

**ROOT_SWEEP.** All dossiers visited; selected `كفء B001`, `ءله B002` referent; care/guarantee branches `قول B015/صمد B005/كون B003` explicitly rejected. **SURFACE_SWEEP:** `E W13–W15; C W03/W05; K beneficiary/possession/guarantee readings; Ø W01–W02,W04,W06–W12`.

`GENERATING_SET = {a2,W13,W14,كفء B001}`. `FROZEN_MODEL = equivalence is oriented relative to the named 3MS center`. Prediction: candidate second term. `UNUSED_AT_FREEZE = {W15}`. W15 supplies it `(C: a4)`. Rival care/guarantee image dies because attachment government is explicit `(K)`. **Grade: strong.**

### C19. W12–W14 — `كان` predicate attachment

**Initial image.** `(E: attachment 112:4 a3)` fixes accusative W14 as predicate of negated W12.

**ROOT_SWEEP.** All dossiers visited; selected `كون B001`, `كفء B001`; rejected `كون B002–B006` and `كفء B002–B005` as local senses while preserving their secondary forks. **SURFACE_SWEEP:** `E W11–W14; C W15 and W08/W10; K generic nonbeing or turning/cycle readings; Ø W01–W07`.

`GENERATING_SET = {a3,كون B001,كفء B001,W11–W14}`. `FROZEN_MODEL = no equivalence predicate is instantiated for the maintained referent`. Prediction: a subject candidate under negation. `UNUSED_AT_FREEZE = {W15}`. W15 supplies it `(C)`. The predicate prevents reading W12 as generic nonexistence `(K)`. **Grade: strong.**

### C20. W12–W15 — delayed-subject attachment

**Initial image.** `(E: attachment 112:4 a4)` places the subject at the last word, leaving the final clause unresolved until W15.

**ROOT_SWEEP.** All dossiers visited; selected `ءحد B002`, `كون B001`, `كفء B001`; `ءحد B001` reserved for backward reactivation. **SURFACE_SWEEP:** `E W11–W15; C W04,W08,W10; K arithmetic/day/separation/mountain branches; Ø W01–W03,W05–W07,W09`.

`GENERATING_SET = {a4,negated copula,predicate W14,pending subject}`. `FROZEN_MODEL = counterpart frame waits for an exhaustive candidate until the last token`. Predictions: nominative candidate, negative-scope B002, opening-form reactivation. `UNUSED_AT_FREEZE = {W15 surface identity and branch}`. All coincide `(C: ءحد B002 locally; C: ءحد B001 backward)`. **Grade: strong.** This attachment alone predicts where grammatical closure must occur.

### C21. W02–W04 `هُوَ ٱللَّهُ أَحَدٌ` — pronoun/name/predicate construction

**Initial image.** `(E: W02–W04 attachments)` creates a three-stage referent: point, name, predicate.

**ROOT_SWEEP.** All dossiers visited; selected `ءله B002`, `ءحد B001`, `قول B001`; all remote lexical scenes terminate. **SURFACE_SWEEP:** `E W01–W04; C W05–W06,W08,W10,W12–W15; Ø operators W07,W09,W11; K a3 confidence only`.

`GENERATING_SET = {W02 pronoun,W03 apposition/name,W04 predicate}`. `FROZEN_MODEL = unresolved reference becomes named unity`. Predictions: name reset, second predicate, compatible 3MS chain, terminal recurrence. `UNUSED_AT_FREEZE = {W05–W15}`. Every feature appears `(C: recurrence, a1 at 112:2, QAC person, W15)`. **Grade: strong.** It is the minimal opening referent-construction.

### C22. W03–W06 — parallel positive predications

**Initial image.** Repeated `ٱللَّهُ` receives W04 then W06 as nominative predicates `(E: two predication attachments; E: name recurrence)`.

**ROOT_SWEEP.** All dossiers visited; selected `ءله B001/B002`, `ءحد B001`, and separate `صمد B001`/B002 forks; all other branches tested and terminated or retained in their lexical passes. **SURFACE_SWEEP:** `E W03–W06; C W08,W10,W12–W15; K no dependent/body roles; Ø W01–W02,W07,W09,W11,W13`.

F1 `FROZEN_MODEL = one reliance center`; F2 `FROZEN_MODEL = one compact cavityless center`. `GENERATING_SET = {parallel predications plus the selected صمد fork}`. Shared predictions: no incoming source, outgoing product, or equal. `UNUSED_AT_FREEZE = {W07–W15}`. W08/W10/W14/W15 fulfill them `(C)`. F1 lacks explicit dependents; F2 lacks physical body `(K)`. **Grade: strong.** The fork is preserved rather than averaged.

### C23. W08→W10 — active/passive mirror composite

**Initial image.** Same-root clauses under repeated `لم`, coordinated by W09, invert voice `(E: ولد B003; E: morphology/a2)`.

**ROOT_SWEEP.** All dossiers visited; selected `ولد B003/B005`, `كفء B002` reversal only after freeze, `كفء B001` future peer; sealed-passage/cycle forks tested and constrained. **SURFACE_SWEEP:** `E W07–W10; C W11–W15,W03–W06; K no body/cycle; Ø W01–W02,W13`.

`GENERATING_SET = {W07–W10,active→passive,same root,coordination}`. `FROZEN_MODEL = source and product positions of one relation are both closed`. Prediction: lateral peer remains. `UNUSED_AT_FREEZE = {W11–W15}`. Final comparison closes it `(C)`. B002 turning is a valid secondary shape; bottle/cycle imagery fails `(K)`. **Grade: strong.** Ordered voice is indispensable.

### C24. W11–W15 — complete final comparison clause

**Initial image.** Negator, copula, comparison anchor, accusative predicate, and delayed subject form one relation `(E: a1–a4)`.

**ROOT_SWEEP.** All dossiers visited; selected `كون B001`, `كفء B001`, `ءحد B002`; `ءحد B001` retained for replay; all care/rank/turn/rhyme/tent/cycle forks explicitly constrained. **SURFACE_SWEEP:** `E W11–W15; C W03–W10; K generic nonbeing and non-comparison readings; Ø W01–W02`.

`GENERATING_SET = {full final clause, selected direct branches}`. `FROZEN_MODEL = no candidate is equivalent to the maintained center`. Predictions: prior genealogy closure and opening-unity return. `UNUSED_AT_FREEZE = {W04,W08,W10}`. All occur `(C)`. **Grade: strong.** Every word has a required role; removing W13, W14, or W15 destroys the relation.

### C25. W03→W05 — repeated `ٱللَّهُ`

**Initial image.** Exact proper-name recurrence across the W04/ayah boundary reanchors the referent `(E: ءله B002; E: temporal recurrence)`.

**ROOT_SWEEP.** All dossiers visited; selected `قول B001` voiced name, `ءحد B001` first property, `صمد B001/B002` new property; worship/circulation/attribution forks tested. **SURFACE_SWEEP:** `E W01,W03–W06; C W08,W10,W12–W15; K no oath/vocative/circulation roles; Ø W02,W07,W09,W11,W13`.

`GENERATING_SET = {W03,W05 exact name}`. `FROZEN_MODEL = same center is reset before a new predicate and relational tests`. Predictions: W06 attaches to W05; later 3MS forms remain continuous. `UNUSED_AT_FREEZE = {W06–W15}`. Both are true `(C)`. **Grade: strong.** Repetition is functionally positioned, not redundant.

### C26. W04→W15 — repeated `أَحَدٌ`

**Initial image.** Exact surface recurrence links positive predicate W04 to delayed subject W15 `(E: ءحد B001 at opening; temporal retention)`.

**ROOT_SWEEP.** All dossiers visited; selected `ءحد B002`, `كون B001`, `كفء B001`, with `صمد B001/B002` and `ولد B003/B005` as backward model constituents. **SURFACE_SWEEP:** `E W04,W15; C W03,W05–W14; K simple adjacent emphasis/arithmetic/day/place; Ø W01–W02`.

`GENERATING_SET = {W04 positive predicate, exact W15 recurrence}`. `FROZEN_MODEL = the unity cue returns in a new syntactic role`. Predictions: local negative scope changes branch function and final relation protects opening unity. `UNUSED_AT_FREEZE = {a4,B002,W14}`. All fulfill it `(C)`. Nonadjacency prevents treating it as simple `أحد أحد` emphasis `(K)`. **Grade: strong.** This is the central reactivation event.

### C27. W08→W10 — repeated `ولد` root

**Initial image.** Same lexical root recurs after only W09; root memory predicts reinforcement or role change.

**ROOT_SWEEP.** All dossiers visited; selected `ولد B003` primary, B005 derivation, B001/B002 role labels, B006 peer prediction; B004 dependent fork constrained. **SURFACE_SWEEP:** `E W08,W10; C W07,W09,W11–W15; K no overt birth participants; Ø W01–W06`.

`GENERATING_SET = {same-root recurrence}`. `FROZEN_MODEL = the second occurrence should reorganize, not merely repeat, the first`. Predictions: changed voice/role. `UNUSED_AT_FREEZE = {W10 morphology}`. Passive voice exactly reverses source/patient orientation `(C)`. **Grade: strong.** Root recurrence plus voice change produces constructive reactivation.

### C28. W07→W09→W11 — repeated `لَمْ`

**Initial image.** Three identical negative operators create a stable inhibitory operation applied successively.

**ROOT_SWEEP.** All dossiers visited; selected `ولد B003`, `كون B001`, `كفء B001`; `صمد B007` persistence only corroborative. **SURFACE_SWEEP:** `E W07–W12; C W13–W15; K no lexical eternity; Ø W01–W06`.

`GENERATING_SET = {three لم occurrences and their jussive complements}`. `FROZEN_MODEL = hold inhibition constant while changing source, product, and peer relations`. Predictions: every complement jussive; each adds a role; last remains unresolved longest. `UNUSED_AT_FREEZE = {voice,final attachments}`. All confirm `(C)`. **Grade: strong.** Operator recurrence structures the entire negative half.

### C29. W09→W11 — repeated `وَ`

**Initial image.** Two conjunctions extend one list first within 112:3 and then across the ayah boundary.

**ROOT_SWEEP.** All dossiers visited; selected `ولد B003`, `كون B001`, `كفء B001`; `كفء B005` alternation rejected. **SURFACE_SWEEP:** `E W07–W12; C W13–W15; K no annual alternating groups; Ø W01–W06`.

`GENERATING_SET = {two conjunctions, three negated clauses}`. `FROZEN_MODEL = an ordered list of exclusions remains open after each conjunction`. Predictions: parallel operators with nonredundant complements. `UNUSED_AT_FREEZE = {W10 voice,W12–W15 relation}`. Voice and relation change satisfy it `(C)`. **Grade: strong.** Conjunction preserves list identity while allowing role progression.

### C30. W02/W03/W05/W08/W10/W12/W13 — 3MS referential chain

**Initial image.** Pronoun, appositional name, exact name recurrence, three 3MS verbs, and 3MS pronoun maintain one temporary referent.

**ROOT_SWEEP.** All dossiers visited; selected `ءله B002`, `ءحد B001`, `صمد B001/B002`, `ولد B003`, `كون B001`, `كفء B001`; all participant-rich remote scenes constrained. **SURFACE_SWEEP:** `E W02–W15 except operators as structural E; C W01 frame; K no explicit full-surah coreference attachment; Ø none`.

`GENERATING_SET = {person/number continuity and name recurrence}`. `FROZEN_MODEL = every later relation targets the opening referent`. Predictions: no named competitor and W13 compatible with prior subject. `UNUSED_AT_FREEZE = {full sequence}`. Satisfied `(C)`. Coreference remains a strong sequence inference rather than a labeled edge `(K)`. **Grade: medium-strong.** It explains role continuity but not lexical choice alone.

### C31. Case and definiteness progression

**Initial image.** W03/W05 are nominative proper nouns; W04 and W15 are indefinite nominatives in different roles; W06 is definite nominative; W14 is indefinite accusative predicate.

**ROOT_SWEEP.** All dossiers visited; selected `ءحد B001/B002`, `صمد B001/B002`, `كون B001`, `كفء B001`; no remote branch generated by case alone. **SURFACE_SWEEP:** `E W03–W06,W12–W15; C W04→W15 recurrence; K morphology cannot determine all semantics; Ø W01–W02,W07–W11`.

`GENERATING_SET = {QAC case/definiteness and attachments}`. `FROZEN_MODEL = positive named predicates precede an indefinite counterpart predicate and exhaustive candidate`. Predictions: opening/final role contrast and correct final attachment. `UNUSED_AT_FREEZE = {negative scope and recurrence}`. Both confirm `(C)`. **Grade: medium-strong.** Formal geometry independently supports the semantic trajectory.

### C32. Nominal-positive → verbal-negative transition

**Initial image.** W02–W06 are organized by nominal apposition/predication; W07–W15 use negated jussive verbs and a negated copular frame.

**ROOT_SWEEP.** All dossiers visited; selected `ءحد B001`, `صمد B001/B002`, `ولد B003`, `كون B001`, `كفء B001`; all generic theme branches rejected. **SURFACE_SWEEP:** `E W02–W15; C W01 command; K positivity alone does not uniquely predict birth; Ø none`.

`GENERATING_SET = {ordered clause-type/polarity shift}`. `FROZEN_MODEL = establish a center positively, then test relations negatively`. Predictions: stable referent, distinct negative roles, final closure. `UNUSED_AT_FREEZE = {voice/order/final subject}`. These supply source→product→peer `(C)`. Birth is not uniquely predicted by nominal clauses alone `(K)`. **Grade: medium-strong.** Order is explanatory but not fully lexical-predictive.

### C33. Ayah-boundary sequence

**Initial image.** Boundary after W04 freezes first predicate; W05 immediately reanchors the name. Boundary after W06 freezes the positive center; W07 changes polarity. Boundary after W10 freezes two-direction genealogy; W11 continues to peerhood.

**ROOT_SWEEP.** All dossiers visited; selected `ءله B002`, `ءحد B001`, `صمد B001/B002`, `ولد B003`, `كون B001`, `كفء B001`. **SURFACE_SWEEP:** `E all W01–W15 by ordered boundary state; K shuffled boundary/order control; Ø none`.

`GENERATING_SET = {three internal ayah boundaries and four ordered ayahs}`. `FROZEN_MODEL = each pause closes one subsystem while preserving one unresolved next role`. Predictions: name reset after first; polarity shift after second; new relation class after third. `UNUSED_AT_FREEZE = {tokens after each boundary}`. All occur `(C)`. Shuffling boundaries weakens these transitions `(K)`. **Grade: strong.** Pauses align with referent, polarity, and relation-axis changes.

### C34. Ayah-final `د` recurrence

**Initial image.** Progressive endings are W04 `أحد`, W06 `الصمد`, W10 `يولد`, W15 `أحد`; each ends in `د`, while first and last exactly match.

**ROOT_SWEEP.** All dossiers visited; selected none as generator; `كفء B003` and `قول B001` tested only as remote lexical analogues. **SURFACE_SWEEP:** `E W04,W06,W10,W15; C their grammatical closure roles; K sound cannot generate semantics or make W14 B003; Ø other words`.

`GENERATING_SET = {ordered ayah-final forms}`. `FROZEN_MODEL = a stable terminal sound holds changing lexical roles together and may close by exact return`. Prediction: fourth ending strengthens recurrence. `UNUSED_AT_FREEZE = {W15}`. Exact return fulfills it `(C)`. B003 rhyme sense is form-remote `(K)`. **Grade: medium-strong.** Acoustic and grammatical closure coincide, but sound is corroborative.

### C35. W15 last-word multi-channel closure

**Initial image.** Before W15, final syntax lacks its subject; comparison lacks a candidate; temporary memory retains W04; acoustic sequence awaits its fourth ending.

**ROOT_SWEEP.** All dossiers visited; selected `ءحد B002` locally and B001 retrospectively, `كون B001`, `كفء B001`; `صمد B001/B002` and `ولد B003/B005` replay as completed models. **SURFACE_SWEEP:** `E W11–W15; C W03–W10; K moving W15 earlier; Ø W01–W02 only framing`.

`GENERATING_SET = {unresolved final syntax through W14}`. `FROZEN_MODEL = last slot must supply nominative exhaustive candidate and memory closure`. Predictions: B002 scope, exact W04 return, final `د`, no unresolved role afterward. `UNUSED_AT_FREEZE = {W15}`. One word fulfills all four `(C)`. Earlier placement would destroy delayed completion and terminal return `(K)`. **Grade: strong.** It directly explains why the passage closes where it does.

### C36. Basmala opening-context → W01–W03 naming transition

**Initial image.** The eligible seed remains W01, not basmala: overt utterance followed by W03 name. Opening context is withheld until post-freeze.

**ROOT_SWEEP.** All seven passage-root dossiers visited; selected `قول B001`, `ءله B002`; no `سمو/رحم` dossier inspected or seeded. **SURFACE_SWEEP:** `E W01–W03; C basmala name morphology,W04–W06; K opening-context seed prohibition; Ø W07–W15`.

`GENERATING_SET = {W01 speech,W03 name}`. `FROZEN_MODEL = a name is voiced and predicated`. Prediction: opening context independently supports naming/invocation. `UNUSED_AT_FREEZE = {basmala}`. `بِسْمِ ٱللَّهِ` does so `(C: opening-context)`. It does not predict birth/counterpart sequence `(K)`. **Grade: medium.** Independent naming support, limited passage-scale reach.

### C37. Ordered center → source → product → peer model, with shuffled-order control

**Initial image.** Only verified constructions are composed: W03–W06 establish one center; W08 denies source role; W10 reverses and denies product role; W12–W15 deny peer occurrence.

**ROOT_SWEEP.** All seven full dossiers visited. Selected direct set `ءله B002`, `ءحد B001/B002`, separate `صمد B001` and B002 center forks, `ولد B003` primary/B005 secondary, `كون B001`, `كفء B001`. Every other branch has an explicit lexical termination above. **SURFACE_SWEEP:** `E W01–W14; C W15; K shuffled order and any physical literalization; Ø none`.

`GENERATING_SET = {speech frame, positive center, active source denial, passive product denial, pending peer frame}`. Freeze immediately before W15: `FROZEN_MODEL = one established center with outward, inward, and lateral competitor axes successively closed`. Predictions: final exhaustive candidate, opening-unity reactivation, grammatical/acoustic stopping. `UNUSED_AT_FREEZE = {W15}`. W15 fulfills all `(C: ءحد B002 local; C: ءحد B001 replay; C: a4; C: final sound)`. Shuffling destroys active→passive completion, name reset before testing, and terminal reactivation `(K: ordered-role control)`. **Grade: strong.** This is the smallest model reproducing activation, expectation, completion, reactivation, and closure.

### C38. Boundary after W04 / 112:1 pause

**Initial image.** `(E: first ayah boundary)` pauses after the complete W02–W04 quoted proposition and freezes opening unity.

**ROOT_SWEEP.** All seven dossiers visited; selected `قول B001`, `ءله B002`, `ءحد B001`; all later branches withheld until post-freeze. **SURFACE_SWEEP:** `E W01–W04; C W05–W06,W15; K boundary does not end the larger recitation; Ø W07–W14 except W15`.

`GENERATING_SET = {W01–W04 quote/predication, first boundary}`. `FROZEN_MODEL = commanded named-unity proposition is locally complete but its referent remains active`. Predictions: if recitation continues, a referent reset or new predicate should follow; W04 may remain available for later recurrence. `UNUSED_AT_FREEZE = {W05–W15}`. W05 immediately repeats the name, W06 adds a predicate, and W15 returns W04 `(C)`. Treating the pause as total discourse closure fails `(K: continued sacred sequence)`. **Grade: strong.** This boundary closes one proposition while preserving referent memory.

### C39. Boundary after W06 / 112:2 pause

**Initial image.** `(E: second ayah boundary)` freezes two positive predications and the two separate `صمد` image forks.

**ROOT_SWEEP.** All dossiers visited; selected `ءله B001/B002`, `ءحد B001`, separate `صمد B001/B002`; `ولد/كون/كفء` remain unused for testing. **SURFACE_SWEEP:** `E W03–W06; C W07–W15; K positive predicates alone do not name the exact next lexeme; Ø W01–W02`.

`GENERATING_SET = {parallel positive predications, second boundary}`. `FROZEN_MODEL = one center is positively established before any relation-denial begins`. Predictions: continuation should preserve the referent and may constrain source/product/peer relations implied by the two center geometries. `UNUSED_AT_FREEZE = {W07–W15}`. W07 changes polarity; W08/W10/W14–W15 close those relations `(C)`. The pause does not uniquely predict birth as the first lexical choice `(K)`. **Grade: medium-strong.** It marks the build→test transition exactly.

### C40. Boundary after W10 / 112:3 pause

**Initial image.** `(E: third ayah boundary)` freezes same-root active/passive birth denial as a completed two-direction subsystem.

**ROOT_SWEEP.** All dossiers visited; selected `ولد B003/B005`; `كون B001`, `كفء B001`, and `ءحد B002` withheld for testing; sealed-passage/cycle branches constrained. **SURFACE_SWEEP:** `E W07–W10; C W11–W15; K pause does not complete peer axis; Ø W01–W06`.

`GENERATING_SET = {two coordinated negated ولد clauses, third boundary}`. `FROZEN_MODEL = source and product roles are closed, leaving a possible lateral counterpart role unresolved`. Prediction: continuation should either close that remaining role or change topic. `UNUSED_AT_FREEZE = {W11–W15}`. The next ayah preserves `لم` and supplies exact counterpart syntax `(C: كون B001; C: كفء B001; C: ءحد B002)`. **Grade: strong.** The pause separates genealogical closure from peer closure.

### C41. Boundary after W15 / terminal pause

**Initial image.** `(E: terminal boundary)` tests whether any syntactic, referential, relational, or acoustic expectation remains unresolved after W15.

**ROOT_SWEEP.** All dossiers visited; selected `ءحد B002` locally, B001 retrospectively, `كون B001`, `كفء B001`, and prior `ولد B003`; all remote scene branches terminate. **SURFACE_SWEEP:** `E W11–W15; C W03–W10; K any demand for an additional peer/source/product token; Ø W01–W02 framing only`.

`GENERATING_SET = {completed delayed-subject clause, terminal pause}`. `FROZEN_MODEL = grammar, exhaustive scope, relation-axis closure, lexical return, and final sound are all complete`. Predictions: no open complement, participant, or candidate remains. `UNUSED_AT_FREEZE = {backward replay of W03–W10}`. Replay confirms name, positive predicates, and both genealogy directions already resolved `(C)`. Adding another relation would reopen a model whose three axes are closed `(K)`. **Grade: strong.** The terminal pause is licensed by simultaneous completion across all channels.

## Post-creation exhaustiveness audit and revision record

### Audit 1 — seed and required-field coverage

The completed draft was checked mechanically and then revised before this section was closed.

- Lexical headings are consecutive L01–L62: **62/62** occurrence × branch seeds.
- Construction headings are consecutive C01–C41: **41/41** seeds.
- Exact Arabic dossier records: **48/48** accepted uncontaminated branches.
- Every one of the 103 seed sections contains a full `DOSSIER_SWEEP` or `ROOT_SWEEP`, a W01–W15 `SURFACE_SWEEP`, `GENERATING_SET`, `FROZEN_MODEL`, predictions, `UNUSED_AT_FREEZE`, post-freeze `C`/`K` testing, and an allowed grade.
- The first check found three weak final-`أحد` forks without an explicit unused set and several hybrid grade labels. Those omissions were revised; all grades now belong to the required five-value scale. The second check found that boundary occurrences had been grouped; C38–C41 were added so each pause has its own seed pass.

### Audit 2 — lexical-family coverage

| Root occurrence(s) | Required branches | Seed passes present | Distinct images explicitly tested |
| --- | ---: | ---: | --- |
| W01 `قول` | B001–B016 | 16/16 | overt speech; tongue; abundance; authority; false/generated attribution; inward speech; circulation; stick; negotiation; control; supposition; doctrine; indication; care; definition |
| W03/W05 `ءله` | B001–B002 × 2 | 4/4 | worship/reliance; naming; circulation; hierarchy; care; generated attribution |
| W04/W15 `ءحد` | B001–B006 × 2 | 12/12 | unity; exhaustive negation; arithmetic; calendar/ordinal; separation/serial individuals; mountain/terrain/camp |
| W06 `صمد` | B001–B007 | 7/7 | reliance center; compactness; stopper; head cloth; oversight; stick blow; persistence |
| W08/W10 `ولد` | B001–B006 × 2 | 12/12 | offspring; parent; birth event; newborn/enslaved dependent; derivation/generated speech; birth-age peer |
| W12 `كون` | B001–B006 | 6/6 | occurrence; place/rank; guarantee; submission; aging; bad state |
| W14 `كفء` | B001–B005 | 5/5 | equivalence; turning; rhyme variation; tent cloth; annual alternating production |

No branch was accepted merely because another remote branch matched it. The stick-game, care/guarantee, mountain/camp, cloth/enclosure, servitude, generated-speech, calendar/production, aging, and rhyme families all form multi-root images, but each is retained as weak or unlikely where local morphology and attachments fail.

### Audit 3 — construction universe

- C01–C09: every unrooted in-passage word/morpheme type at its material occurrence—W02 pronoun, W06 determiner, three `لم`, two `و`, W13 preposition, W13 pronoun.
- C10–C20: all eleven permitted attachment rows independently seeded.
- C21–C24: complete local clause constructions.
- C25–C29: every exact lexical/operator recurrence (`الله`, `أحد`, `ولد`, `لم`, `و`).
- C30–C32: referential, case/definiteness, and clause-type/polarity morphology.
- C33: the combined boundary sequence; C34–C35: final sounds and last-word closure.
- C36: opening context used only after a passage-generated naming prediction.
- C37: verified relations composed into the passage-scale model and tested against shuffled order.
- C38–C41: each of the four ayah/terminal boundary occurrences independently seeded.

### Audit 4 — missing-image challenge

The full dossiers were searched again by open scene role rather than by the leading synthesis. The following possible constellations were specifically challenged:

| Open role query | Branch constellation found | Result |
| --- | --- | --- |
| speech + generated product | `قول B001/B005 + ولد B005` | Generated/attributed speech fork retained, then defeated by quote and subject syntax. |
| instrument + impact + motion | `قول B008 + صمد B006/B002 + كفء B002` | Complete stick-game image retained, then defeated by every local form. |
| authority + master + rank | `قول B004/B010 + صمد B001 + كون B002` | Hierarchy image retained as weak; no title/rank/patient form. |
| care + oversight + guarantee + parent | `قول B015 + صمد B005 + كون B003 + ولد B002` | Complete caretaker image retained, then defeated by W13 attachment. |
| worship + master + enslaved/submitted dependent | `ءله B001 + صمد B001 + ولد B004 + كون B004` | Servitude image retained, then defeated by morphology and negation. |
| mountain + hard elevation + place + endurance | `ءحد B006 + صمد B002/B007 + كون B002` | Terrain image retained, then defeated by predication/case. |
| stopper/wrap + tent rear | `صمد B003/B004 + كفء B004` | Closure/cloth image retained, then defeated by absent vessel/body/tent roles. |
| number/day + birth-age + annual cycle + time | `ءحد B003/B004 + ولد B006/B003 + كفء B005 + كون B001` | Calendar/production image retained, then defeated by negation and absent count/year. |
| birth coordinate + equality | `ولد B006 + كفء B001` | Peer feature corroborated; age mechanism constrained. |
| persistence + temporal occurrence | `صمد B007 + كون B001 + repeated لم` | Medium abstract persistence model retained; hardship scene constrained. |
| voiced composition + differing endings | `قول B001 + كفء B003 + ayah endings` | Weak sound-form fork retained; W14's local equivalence and absent genre constrain it. |
| positive-to-negative turn | `كفء B002 + clause-order change` | Weak discourse-turn fork retained; active/passive reversal gives the more specific medium image. |

No additional passage-local expansion or rival image remained unrecorded after this role-based search. The file was therefore revised to the exhaustive state represented above.

## Multi-seed convergence

| Synthesis | Independent seed routes | Grade | Specific explanatory work |
| --- | --- | --- | --- |
| Ordered center → source → product → peer closure | L19/L25/L27/L28, L36/L38, L42/L44, L46/L52/L58, C22/C23/C24/C37 | **strong** | Explains positive setup, active→passive order, final relation, and why W15 is required. |
| Opening/final `أحد` reactivation | L19/L20, L57/L58, C11/C20/C26/C35 | **strong** | Same surface changes from positive predicate B001 to exhaustive delayed subject B002. |
| Reliance-center geometry | `ءله B001 + صمد B001 + ءحد B001`, later `ولد/كفء` closures | **strong** | Models directed dependence and why reverse/lateral relations are denied. |
| Compact-center geometry | `صمد B002 + ءحد B001`, later `ولد B005 + كفء B001` | **strong** | Predicts no generative passage and no duplicate; remains explicitly secondary/nonphysical. |
| Spoken naming/reset frame | `قول B001 + ءله B002`, quote, basmala corroboration, repeated name | **medium-strong** | Explains W01, W03, W05, and transition into predication. |
| Definition/boundary frame | remote `قول B016`, positive predications, later exclusions | **medium-strong** | Predicts positive core followed by source/product/peer boundary-setting. |
| Persistence through denied transitions | `صمد B007 + كون B001 + repeated لم` | **medium** | Explains sustained inhibition, but lacks the branch's explicit hardship scene. |
| Active/passive turning image | `كفء B002 + ولد B003 voice reversal` | **medium** | Captures exact relation inversion; W14 itself remains local B001 equivalence. |
| Acoustic first-last return | ayah-final `د`, W04→W15 exact recurrence, delayed subject | **medium-strong** | Marks the same stopping point as grammar and lexical memory. |

## Very short interpretation

The recitation first creates a voice, resolves a pronoun into a repeated name, and assigns two positive predicates. It then holds negation constant while closing an outward source role, the inverted inward product role, and finally the lateral peer role. W15 closes the grammar as exhaustive `أحد` while reactivating W04's positive `أحد`; syntax, memory, relation geometry, and sound therefore stop together. The reliance-center and compact-center images remain separate secondary simulations, not replacement translations.
