# Activation Reservoir: S103, V7.5.8

## Formation state

This is a closed-field store. Its nodes come only from the three supplied surface lines, their supplied morphology and syntax, and the supplied lexical records. The primary scaffold is absent. No node below is a governing interpretation, and no activation is ranked. Literal occupant continuity and relational coalition are kept in separate graphs throughout.

Notation:

- `Sx.wy` is a positioned surface word; `Sx.my` is a supplied morpheme when a word contains more than one.
- `U-ROOT-BRANCH.n` is a source-local utterance occurrence. Two utterances remain two occurrences even when they use the same form.
- `O:` marks an occupancy edge: an identical or explicitly coreferred occupant, state, material, or result is carried.
- `R:` marks content or role re-instantiation: only the stated schema is carried into a distinct occurrence.
- `K:` marks a coalition link: only an invariant relation, formal position, or parameter transformation is carried.
- `F:` marks exact form/position contact only. It never carries a local occupant.
- `OPEN[...]`, `ABSENT[...]`, and `NEGATED[...]` preserve supplied vacancies with their scope.

## Positioned surface lattice

### Exact ordered object

```text
S1 / 103:1 / line 1 of 3 / passage beginning
وَٱلْعَصْرِ

S2 / 103:2 / line 2 of 3 / medial line
إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ

S3 / 103:3 / line 3 of 3 / passage ending
إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَتَوَاصَوْا۟ بِٱلْحَقِّ وَتَوَاصَوْا۟ بِٱلصَّبْرِ
```

The complete supplied line-word vector is `[1, 4, 9]`; the passage has `14` positioned words. The word-level morpheme-count vectors are `S1 [3]`, `S2 [1,2,2,1]`, and `S3 [1,1,2,3,2,3,3,3,3]`. The corresponding line totals are `[3,6,21]`, and the passage total is `30` supplied morphemes. The supplied syntax-edge vector is `[1,3,7]`, total `11`. Thus the three simultaneous ordered expansions are `1 -> 4 -> 9` words, `3 -> 6 -> 21` morphemes, and `1 -> 3 -> 7` syntax edges. These complete vectors remain surface carriers; no arbitrary subvector replaces them.

Line beginnings form the exact ordered sequence `وَـ | إِنَّ | إِلَّا`: an oath-particle prefix in the first line, an accusative particle in the second, and an exception particle in the third. The sequence is not an identity chain. Line endings form `عَصْرِ | خُسْرٍ | صَبْرِ`: three masculine genitive nominal stems ending in written `ر`, with S1 definite under `ٱلْ`, S2 indefinite, and S3 definite under `ٱل`. The single terminal consonant is an exact boundary recurrence; no unattested form such as an arbitrary two-letter substring is promoted from it.

### Complete morphological positions

| Position | Complete surface carrier | Supplied internal structure | Local formal work and typed ports |
|---|---|---|---|
| `S1.w1` | `وَٱلْعَصْرِ` | `وَ` P/PREFIX + `ٱلْ` DET/PREFIX + `عَصْرِ`, lemma `عَصْر`, root `ع ص ر`, N, M, GEN | The one word is at once line beginning and ending. Supplied syntax makes `وَ` the oath particle and `ٱلْعَصْرِ` its governed complement. `OPEN[oath discourse endpoint/result]`; no semantic participant is imported from a lexical branch. |
| `S2.w1` | `إِنَّ` | lemma `إِنّ`, ACC | Head of the line's supplied government and predication. Controller in the grammatical sense is the particle; semantic initiator is not supplied. |
| `S2.w2` | `ٱلْإِنسَٰنَ` | `ٱلْ` DET + `إِنسَٰنَ`, lemma `إِنسَٰن`, root `ء ن س`, N, M, ACC | Governed `ism` of `إِنَّ`; one surface discourse occurrence, definite and masculine. This occurrence is the participant bound to the line's predication, not every lexical occurrence of `إنسان`, `إنس`, or `نفس`. |
| `S2.w3` | `لَفِى` | `لَـ` EMPH + `فِى` P | Emphasis plus a containment/state relation. The preposition governs S2.w4 inside the predicative phrase. |
| `S2.w4` | `خُسْرٍ` | lemma `خُسْر`, root `خ س ر`, N, M, INDEF, GEN | Governed complement inside the `khabar`; predicative state/condition port filled by this exact surface occurrence. No trader, balance, capital, or measure is silently added. |
| `S3.w1` | `إِلَّا` | lemma `إِلَّا`, EXP | Opens exception scope. The supplied scope begins at S3.w2 and continues through the final `بِٱلصَّبْرِ`. |
| `S3.w2` | `ٱلَّذِينَ` | lemma `ٱلَّذِى`, REL, MP | The excepted relative group. It is the surface controller shared by the coordinated perfect predicates through syntax and agreement; individual members remain unspecified. |
| `S3.w3` | `ءَامَنُوا۟` | stem `ءَامَنُ`, lemma `ءَامَنَ`, root `ء م ن`, V, PERF, measure IV, 3MP + suffix `وا۟` PRON:3MP | First predicate in exception scope. Grammatical controller is S3.w2. `OPEN[explicit surface object/complement]`; lexical records may expose schemas but do not manufacture a surface argument. |
| `S3.w4` | `وَعَمِلُوا۟` | `وَ` CONJ + stem `عَمِلُ`, lemma `عَمِلَ`, root `ع م ل`, V, PERF, 3MP + suffix `وا۟` PRON:3MP | Second predicate, coordinated after S3.w3. Same surface group occurrence controls it. Its affected/content port is filled only by S3.w5. |
| `S3.w5` | `ٱلصَّٰلِحَٰتِ` | `ٱل` DET + `صَّٰلِحَٰتِ`, lemma `صَّٰلِحَٰت`, root `ص ل ح`, N, active participle, FP, ACC | Explicit direct object of S3.w4. Feminine-plural object features do not alter the masculine-plural controller. |
| `S3.w6` | `وَتَوَاصَوْا۟` | `وَ` CONJ + stem `تَوَاصَ`, lemma `تَوَاصَ`, root `و ص ي`, V, PERF, measure VI, 3MP + suffix `وْا۟` PRON:3MP | Third predicate, coordinated after S3.w4. Reciprocal/source-lexical role topology is re-instantiated in a distinct surface occurrence. Its explicit content complement is S3.w7. |
| `S3.w7` | `بِٱلْحَقِّ` | `بِ` P + `ٱلْ` DET + `حَقِّ`, lemma `حَقّ`, root `ح ق ق`, N, M, GEN | Definite governed content complement of the first surface `تَوَاصَوْا`. It does not fill the content port of S3.w8. |
| `S3.w8` | `وَتَوَاصَوْا۟` | `وَ` CONJ + stem `تَوَاصَ`, lemma `تَوَاصَ`, root `و ص ي`, V, PERF, measure VI, 3MP + suffix `وْا۟` PRON:3MP | Fourth predicate and second occurrence of the same complete surface form. Its event identity remains distinct; its explicit content complement is S3.w9. |
| `S3.w9` | `بِٱلصَّبْرِ` | `بِ` P + `ٱل` DET + `صَّبْرِ`, lemma `صَبْر`, root `ص ب ر`, N, M, GEN | Definite governed content complement of the second surface `تَوَاصَوْا`; it is also the passage-final carrier. |

The controller vector of the four perfect predicates is `[3MP,3MP,3MP,3MP]`, but surface binding, not feature resemblance alone, carries the one S3 relative-group occurrence into each controller port. The predicate-prefix vector is `[none, وَ, وَ, وَ]`. The suffix vector is written `[وا۟, وا۟, وْا۟, وْا۟]`: two exact pairs after the supplied vocalic distinction is preserved, and one fourfold unvocalized `وا` return. The complement vector is `[OPEN, ٱلصَّٰلِحَٰتِ, بِٱلْحَقِّ, بِٱلصَّبْرِ]`; its types are `[unspecified, direct object, governed content, governed content]`. Coordination does not redistribute these complements.

### Supplied syntax as participant structure

The eleven edges remain indexed exactly as supplied, including their supplied anchor numbering:

```text
SX-01 q:103:1:1 -> particle_complement -> q:103:1:2
      وَ (oath particle) -> government -> ٱلْعَصْرِ

SX-02 q:103:2:1 -> particle_complement -> q:103:2:2
      إِنَّ -> governed ism -> ٱلْإِنسَٰنَ
SX-03 q:103:2:1 -> prep_complement -> q:103:2:4
      إِنَّ / فِى inside its khabar -> governed complement -> خُسْرٍ
SX-04 q:103:2:1 -> predication -> q:103:2:4
      إِنَّ -> khabar predication لَفِى خُسْرٍ

SX-05 q:103:3:1 -> exception -> q:103:3:2
      إِلَّا -> excepted group ٱلَّذِينَ; scope continues through بِٱلصَّبْرِ
SX-06 q:103:3:3 -> conjoined -> q:103:3:5
      ءَامَنُوا -> coordinated predicate وَعَمِلُوا
SX-07 q:103:3:5 -> direct_object -> q:103:3:6
      وَعَمِلُوا -> affected/content object ٱلصَّٰلِحَٰتِ
SX-08 q:103:3:5 -> conjoined -> q:103:3:8
      وَعَمِلُوا -> coordinated predicate وَتَوَاصَوْا
SX-09 q:103:3:8 -> prep_complement -> q:103:3:9
      first وَتَوَاصَوْا -> content بِٱلْحَقِّ
SX-10 q:103:3:8 -> conjoined -> q:103:3:11
      first وَتَوَاصَوْا -> second وَتَوَاصَوْا
SX-11 q:103:3:11 -> prep_complement -> q:103:3:12
      second وَتَوَاصَوْا -> content بِٱلصَّبْرِ
```

`SX-02 + SX-03 + SX-04` binds the same S2 human occurrence to the predicated `لَفِى خُسْرٍ` condition. `SX-05` binds the exception group and the full four-predicate scope. `SX-06 + SX-08 + SX-10`, reinforced by 3MP morphology, carries the same relative-group controller through four distinct predicate occurrences. `SX-07`, `SX-09`, and `SX-11` terminate in different typed ports. No edge binds `ٱلصَّٰلِحَٰتِ` to either `تَوَاصَوْا`, or `بِٱلْحَقِّ` to `عَمِلُوا`, or the two content nouns to each other.

### Surface recurrence and changed formal work

- Exact `وَ` occurs as the passage's first morpheme and as conjunction prefixes on S3.w4, S3.w6, and S3.w8. `F: وَ@S1 -> same written form, changed particle role -> وَ@S3`; the oath-particle occurrence and conjunction occurrences remain different grammatical events.
- The determiner is written `ٱلْ` at S1.w1, S2.w2, and S3.w7, and `ٱل` at S3.w5 and S3.w9; `ٱلَّذِينَ` contains its own supplied relative form rather than a separately analyzed determiner. Vocalization-stripped detection joins the determiner occurrences as forms while preserving `ٱلْ/ٱل` and each host.
- `بِ` is exact at S3.w7 and S3.w9, in the same word-internal ordinal `1 of 3`; it governs two different content occupants. `F` carries prefix identity and parallel position, not content identity.
- `تَوَاصَ + وْا۟` is exact at S3.w6 and S3.w8. Their local vectors match in controller, perfect aspect, measure VI, active/supplied voice status, coordination, and reciprocal topology; their content results differ as `حَقّ` and `صَبْر`. Exact recurrence opens a changed-content counterfield and does not make one literal event.
- `وا۟` closes the first two verbs, while `وْا۟` closes the last two. With decoration removed all four expose ordered `وا`; with exact writing retained they form the enclosure `[وا۟, وا۟] [وْا۟, وْا۟]` around the direct-object and two prepositional-complement patterns.
- The root vector along the four predicates and their filled complements is `ء م ن -> ع م ل / ص ل ح -> و ص ي / ح ق ق -> و ص ي / ص ب ر`. Root recurrence occurs only at the third and fourth predicate positions (`و ص ي`), while the two endpoints change.
- S1 and S3 end in definite masculine genitives, `ٱلْعَصْرِ` and `ٱلصَّبْرِ`; S2 ends in indefinite masculine genitive `خُسْرٍ`. Passage-final `صَبْرِ` also returns the `ص ... ر` consonants present, with an intervening different consonant, in `عَصْرِ`; because `صر` is not supplied as an independent complete form, only the separately supplied consonants and boundary positions are registered, not a fabricated lexical term.

## Exact-contact closure

### Detection discipline and rounds

Each written node is retained exactly. A second detection representation removes vocalization and Qur'anic/ordinary orthographic decoration so that ordered Arabic letters can meet; a detection match never replaces the written nodes. Alif/hamza, suffix, prefix, number, case, and spelling differences are recorded rather than erased in the resulting circuit.

Round 0 contains all fourteen complete surface words, all thirty supplied morphemes, every supplied lemma and root, and every complete lexical form, quoted term, equation term, and named expression. Round 1 registers exact recurrence and both containment directions. Round 2 re-enters only recoverable lexical bases licensed by a supplied inflection, attachment, suffix, or explicit derivational statement. Round 3 lets those bases meet other complete supplied occurrences. No arbitrary internal substring enters. A full pass after the circuits below adds no new independently supplied form; new semantic enactments remain open, but the form-contact field is closed.

### Surface-trigger circuits

1. `وَٱلْعَصْرِ@S1.w1` keeps three typed containing nodes: `وَ | ٱلْ | عَصْرِ`. The stem/lemma contact opens every supplied `ع ص ر` assertion, while each remains its own occurrence. The written surface `عَصْرِ`, lemma `عَصْر`, lexical `العصر`, and unvocalized host `والعصر` are retained as different forms. The explicit derivational assertion `العنصر أصل الحسب ومما زيدت فيه النون وهو في الأصل العصر وهو الملجأ` creates a narrower circuit: `surface العصر -> asserted base العصر -> insertion ن -> full form العنصر -> named أصل الحسب / ملجأ relation`. This is an exact form-history relation; it does not identify the surface referent with a lineage occupant.
2. `ٱلْإِنسَٰنَ@S2.w2` opens the supplied `ء ن س` forms `الإنس`, `إنسي`, `أناسي`, `الإنسان`, `إنسان العين`, and `ابن إنسك` through their explicitly supplied record, root, and recovered bases. The surface occurrence remains distinct. Exact `الذين` at S3.w2 also meets the complete phrase `العاملين عليها هم السعاة الذين يأخذون الصدقات`; only the relative form recurs, not the collector occupants.
3. `خُسْرٍ@S2.w4` meets supplied `خُسْر`, `الخسر`, `الخسران`, `خسر`, `خسرت`, `أخسرته`, `خاسر`, and `خاسرة` through the explicit root/inflection field. `خُسْرٍ` is not equated with any one trade, balance, or destruction occurrence. The exact source difference `أصل واحد يدل على النقض` versus the other supplied `النقص/النقصان` forms is retained: `النقض` and `النقص` are separate written nodes.
4. `ءَامَنُوا۟@S3.w3` exposes `ءَامَنُ + وا۟`, lemma `ءَامَنَ`, and root `ء م ن`. It meets supplied `آمن`, `أمن`, `يأمن`, `آمين`, `التأمين`, `الإيمان`, `مؤمن`, and `مصدق` only through their complete supplied relations. The surface initial `ءا`, lexical `آ`, and the `ي` of `آمين` remain visible. Root membership is not exact word identity.
5. `وَعَمِلُوا۟@S3.w4` exposes conjunction `وَ`, stem `عَمِلُ`, lemma `عَمِلَ`, 3MP suffix `وا۟`, and the recoverable base `عمل`. It collides exactly with `عمل عملا فهو عامل`, `كل فعل يكون من الحيوان بقصد`, the many `العمل` equation terms, and, across the next surface position, the complete source assertion `الأعمال الصالحة والسيئة`. The last circuit is fully positioned: `عَمِلُوا@S3.w4 -> direct_object -> ٱلصَّٰلِحَٰتِ@S3.w5`, while lexical `الأعمال الصالحة والسيئة` supplies the intact class contrast. The surface object selects its own positive-form carrier; the lexical negative alternative remains supplied but unoccupied on the surface.
6. `ٱلصَّٰلِحَٰتِ@S3.w5` exposes determiner `ٱل`, the supplied feminine-plural lemma `صَّٰلِحَٰت`, root `ص ل ح`, and, through source-attested `صالح/الصالحة`, the recoverable base `صالح` with plural `ات` retained. It meets `رجل صالح`, `الأعمال الصالحة والسيئة`, and all supplied `صلاح/صلح/إصلاح/مصلحة` forms by explicit root and derivation, not by occupant identity.
7. Each `وَتَوَاصَوْا۟` exposes `وَ + تَوَاصَ + وْا۟`, root `و ص ي`, and the source-attested full form `تواصى`. Both surface occurrences collide with the complete assertions `تواصى القوم إذا تواصلوا`, `تواصى القوم أي أوصى بعضهم بعضا`, and `تواصى القوم إذا أوصى بعضهم إلى بعض`. The surface 3MP controller supplies the local group occurrence for each re-instantiation; lexical `القوم` does not become that group by identity. The suffix difference between surface `تَوَاصَوْا۟` and source `تواصى` is retained.
8. `بِٱلْحَقِّ@S3.w7` exposes `بِ + ٱلْ + حَقِّ`, lemma `حَقّ`, and root `ح ق ق`. It meets every supplied complete `حق`, `الحق`, `حقة`, `حقيقة`, `أحق`, `استحق`, `حققت`, `أحققت`, `حاق`, and `حقحقة` carrier through its own asserted relation. Especially exact is `إذعان النفس للحق على سبيل التصديق`: lexical `الحق` is an endpoint/content inside an `إيمان` assertion, while the surface `الحق` is the governed content of a distinct `تواصوا` occurrence.
9. `بِٱلصَّبْرِ@S3.w9` exposes `بِ + ٱل + صَّبْرِ`, lemma `صَبْر`, and root `ص ب ر`. It meets exact `الصبر`, `صبرت`, `حبستها`, `صبير`, `صبرة`, `صبارة`, `صبار`, and `أصبره` carriers while keeping vowel, suffix, and derivational differences. It also meets `العصر الحبس` through exact relation-word `الحبس`, and `الصبر بكسر الباء عصارة شجرة` through exact `عصارة`, which itself meets the `ع ص ر` product definitions.

### Recovered-term circuits

- `وَٱلْعَصْرِ = وَ + ٱلْ + عَصْرِ`; recovered `عصر` is licensed by the supplied lemma. `العنصر` is not split freely: the explicit utterance alone licenses `العنصر -> ن added -> العصر`.
- `ءَامَنُوا۟ = ءَامَنُ + وا۟`; `ءَامَنَ` is supplied as lemma. `آمين` remains a different named form with supplied long/short pronunciation and prayer-act relations.
- `وَعَمِلُوا۟ = وَ + عَمِلُ + وا۟`; `عَمِلَ` is supplied as lemma and `عمل` recurs as a complete lexical term.
- `ٱلصَّٰلِحَٰتِ = ٱل + صَّٰلِحَٰتِ`; source-attested `الصالحة` and `صالح` license a base/plural circuit, preserving `ات`, FP, ACC, and the surface dagger-alif writing.
- `وَتَوَاصَوْا۟ = وَ + تَوَاصَ + وْا۟`; source-attested `تواصى` licenses the full lexical base; the two surface hosts remain separately positioned.
- `بِٱلْحَقِّ = بِ + ٱلْ + حَقِّ` and `بِٱلصَّبْرِ = بِ + ٱل + صَّبْرِ`; the preposition, determiner, and governed noun are separately typed. Their common `بِ + ٱل` envelope carries form and ordinal position only.
- `خنسرى` and `خيسرى` are kept with the explicit assertion `رجل خنسرى وقالوا خيسرى في موضع الخسران النون والياء زائدتان`: the full forms, base field `الخسران`, and added `ن/ي` are all nodes. No other substring is recovered from them.
- `اليعملة` is held with `اليعملة من الإبل اسم لها اشتق من العمل` and `اليعملة مشتقة من العمل`: full named form, base `العمل`, and asserted derivation. `العنصر`/`العصر` and `اليعملة`/`العمل` can therefore form a derivational coalition, but their inserted material and resulting named classes remain local.
- `الوصية ... كأنه كلام يوصى أي يوصل` explicitly recovers the relation `يوصى -> يوصل`; `وصيت الشيء وصلته` and `وصى الشيء يصي إذا اتصل ووصاه غيره وصله` keep full inflected terms and the connection equation intact.

### Cross-record exact returns

The following contacts re-enter closure as complete supplied terms or relations. Each arrow is `F` unless another typed edge is stated later.

```text
النفس in أصل الأمن طمأنينة النفس وزوال الخوف
  <-> النفس in إذعان النفس للحق على سبيل التصديق
  <-> النفس in صبرت نفسي / حبس النفس
  <-> النفس in ابن إنسك للنفس

الحق in إيمان/تصديق assertion
  <-> الحق in حق نقيض الباطل and all ح ق ق tuples
  <-> الحق@S3.w7

عمل / الأعمال in ع م ل tuples
  <-> يعمل in التقدم إلى الغير بما يعمل به مقترنا بوعظ
  <-> الأعمال الصالحة والسيئة
  <-> عَمِلُوا + ٱلصَّٰلِحَٰتِ on the surface

تواصى القوم in three و ص ي assertions
  <-> تَوَاصَوْا@S3.w6
  <-> تَوَاصَوْا@S3.w8

حبس / الحبس in صبرت نفسي أي حبستها and حبس النفس
  <-> المحبوسة على الموت
  <-> العصر الحبس
  <-> يمنعه إياه ويحبسه عنه
  <-> تحبس في البيت

عصارة in العصارة ما سال عن العصر / ما تحلب من شيء تعصره
  <-> الصبر بكسر الباء عصارة شجرة
  <-> العصارة الغلة

السحاب / السحائب in المعصرات and السحابة المعصر
  <-> سحاب مستو فوق السحاب الكثيف
  <-> السحائب البيض / السحاب الأبيض المتدرج

الشتاء in جئته في حاق الشتاء
  <-> صبارة الشتاء شدة برده

رأس in حاق رأسه
  <-> رأس الحوجلة in the stopper assertion

الميزان / وزن / كيل in خسر and أخسر measurement assertions
  <-> بلا وزن ولا كيل in the صبرة sale assertion

القوم in أعصر القوم / عصر القوم
  <-> وقع القوم في أم صبور
  <-> أحق القوم
  <-> تصالح القوم / تحاق القوم / تواصى القوم

الإنسان in surface and ء ن س records
  <-> الإنسان in الاعتصار أن يغص الإنسان بالطعام

عين in إنسان العين and سواد العين
  <-> بعاملة ... بعين بعيدة النظر

الرمح / السنان in عمل الرأي والكلام والرمح and عامل الرمح
  <-> عامل الرمح ما يلي السنان / صدره دون السنان

مطر / تمطرون / مطروا in ع ص ر rain assertions
  <-> السحاب carriers in ص ب ر through the specifically named cloud class

موافقة / يوافق in أصل الحق المطابقة والموافقة and يصلح لك
  <-> موافقة المرعى للسائمة in the supplied و ص ي branch image

ضد / نقيض / خلاف as explicitly recurring polarity relations
  <-> each local opposite pair, without exchanging either term of the pairs
```

The exact occurrence of `في` at S2.w3 also returns in many intact lexical assertions (`في أمانه`, `في السواد`, `في الحق`, `في حاق الشتاء`, `في تجارته`, `في أم صبور`, `في أكمامه`, `في ماله`, `في البناء`, `في حاجتك`, and others). Closure retains every host assertion, but the preposition alone transports only its written form and local relation type. Likewise, recurring `من`, `إلى`, `على`, `إذا`, `أي`, and `لا` stay attached to their complete assertions; their ubiquity never fuses occupants or events.

## Source-local tuple reservoir

Every semicolon-delimited assertion below remains a separate indexed occurrence under its branch carrier. The intact carrier is given first; the released tuple notes then expose only roles and transitions stated by that carrier or its supplied `what_is_ar` and `branch_image_ar`. An unspecified controller, patient, medium, endpoint, cause, or aftermath stays open.

### `ء م ن`: security, trust, assent, and the named prayer act

**`U-AMN-B001` — `سكون القلب في أمن وثقة`.** Intact carrier: `الأمن ضد الخوف؛ أصل الأمن طمأنينة النفس وزوال الخوف؛ الأمانة ضد الخيانة ومعناها سكون القلب؛ الأمان إعطاء الأمنة؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن؛ استأمن إليه دخل في أمانه؛ مأمنه منزله الذي فيه أمنه؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها`.

- `U-AMN-B001.1`: local terms `الأمن` and `الخوف`; relation `ضد`; no controller and no transition are asserted by this equation.
- `.2`: occupant `النفس` enters with disquiet/fear as the explicitly removed state and leaves in `طمأنينة`; `زوال الخوف` is the result; cause and medium remain open.
- `.3`: `الأمانة` and `الخيانة` form another opposed pair, while `سكون القلب` is attached to `الأمانة`; the local `القلب` is not the `.2` local `النفس` by identity.
- `.4`: an open giver performs `إعطاء`; transported content/result is `الأمنة`; recipient is open.
- `.5`: `فلان` is controller/experiencer of `أمن/يأمن`; incoming state open, outgoing named by `أمنا وأمانا وأمنة`, resultant role `آمن`.
- `.6`: an unnamed seeker is controller of `استأمن`; direction `إليه`; boundary transition `دخل في أمانه`; endpoint possessor remains the pronoun's local referent.
- `.7`: `مأمنه` is asserted to be `منزله الذي فيه أمنه`: possessed place contains the possessor's local security state.
- `.8`: the local camel is called `الأمون`; its technical role is `الأمينة الوثيقة`, alternatively one whose slackening and stumbling are treated as secure. The camel, its bodily risks, and its outcome remain local.

**`U-AMN-B002` — `تصديق يطمئن إليه القلب`.** Intact carrier: `الإيمان التصديق؛ وما أنت بمؤمن لنا أي مصدق لنا؛ إذعان النفس للحق على سبيل التصديق؛ المؤمن في صفات الله يصدق ما وعد عبده`.

- `.1` is an asserted equation `الإيمان -> التصديق` with no supplied particular believer or report.
- `.2` has addressed `أنت`, negated role `NEGATED[مؤمن لنا]`, equation to `NEGATED[مصدق لنا]`, and recipient `لنا`; the content to be credited is open.
- `.3` has local `النفس` as yielding participant, endpoint/content `الحق`, manner/basis `على سبيل التصديق`, and outgoing `إذعان`. It exposes an exact `الحق` interface without identifying this local endpoint with S3.w7.
- `.4` has local role `المؤمن في صفات الله` as grammatical/semantic controller of `يصدق`; content `ما وعد عبده`; the promise's controller is the same local role, beneficiary/recipient `عبده`, and fulfillment aftermath remains open.

**`U-AMN-B003` — `قول آمين طلبا للاستجابة`.** Intact carrier: `قولنا في الدعاء آمين وتفسيره اللهم افعل؛ التأمين من قولك آمين؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين`.

- `.1`: collective speaker in attached `قولنا`; setting `في الدعاء`; uttered content `آمين`; interpretation `اللهم افعل`; requested act remains typed but unspecified.
- `.2`: controller `ك` in `قولك`; utterance `آمين`; derived act/result `التأمين`.
- `.3`: same named utterance has two pronunciation realizations, `يمد ويقصر`; meaning equation `كذلك فليكن`; desired-state content is deictically open.
- `.4`: `آمين` is `اسم للفعل`, meaning `استجب`; `فلان` enters the resultant role `أمن` only in this carrier's sense when he says `آمين`. This named act does not become the surface `ءَامَنُوا` event through root contact.

### `ء ن س`: human appearance, perception, proximity, facing side, image, and self-address

**`U-ANS-B001` — `ظهور الإنسان المخالف للتوحش والجن`.** Intact carrier: `الإنس خلاف الجن وسموا لظهورهم؛ الإنس البشر والواحد إنسي والجمع أناسي؛ الإنس جماعة الناس والأناسي جماع`.

- `.1`: opposed classes `الإنس` and `الجن`; naming has reason/result `لظهورهم`; the namers are suppressed and remain open.
- `.2`: equation `الإنس = البشر`; number mapping `الواحد إنسي -> الجمع أناسي`.
- `.3`: collective equation `الإنس = جماعة الناس`; `الأناسي = جماع`. These class/number schemas contact surface singular `ٱلْإِنسَٰنَ` only formally and derivationally.

**`U-ANS-B002` — `إيناس الشيء برؤية أو إحساس أو سماع`.** Intact carrier: `آنست الشيء إذا رأيته وآنسته إذا سمعته؛ آنسته أبصرته وآنست الصوت سمعته وآنست منه رشدا علمته؛ آنس من جانب يعني أبصر نارا والاستئناس النظر وأحس بما رابه؛ فإن آنستم منهم رشدا أي أبصرتم وآنست نارا`.

- `.1` keeps two occurrences: perceiver encoded in `ت`, affected `الشيء` in one seeing event and heard referent in another hearing event. Identical wording does not make sight and hearing one event.
- `.2` preserves equations `آنسته = أبصرته`, `آنست الصوت = سمعته`, and `آنست منه رشدا = علمته`; object, sensory medium, and epistemic result differ across the three local tuples.
- `.3` has open perceiver, boundary/source `من جانب`, perceived fire `نارا`, equation `الاستئناس = النظر`, and a separate affective detection `أحس بما رابه` with disturbing content in the relative clause.
- `.4` has plural controller in `آنستم`, source group `منهم`, result/content `رشدا`, equation to `أبصرتم`; a separate first-person fire-perception occurrence closes the carrier.

**`U-ANS-B003` — `الأنس الذي يزيل الوحشة`.** Intact carrier: `الأنس أنس الإنسان بالشيء إذا لم يستوحش منه؛ الإيناس خلاف الإيحاش والإنس خلاف الوحشة والأنيس المؤانس وكل ما يؤنس به؛ أنست بفلان أي فرحت به والأنس والاستئناس هو التأنس وكلب أنوس نقيض العقور؛ الأنس خلاف النفور ولكل ما يؤنس به`.

- `.1`: local human is experiencer, `بالشيء` is relational endpoint, and `NEGATED[استيحاش منه]` is the condition/result.
- `.2`: polarity pairs `الإيناس/الإيحاش` and `الإنس/الوحشة`; role equations `الأنيس = المؤانس` and unrestricted local class `كل ما يؤنس به`, whose quantification remains inside this assertion.
- `.3`: speaker as experiencer, `فلان` as proximity endpoint, result `فرحت به`; equation `الأنس والاستئناس = التأنس`; separate animal-class opposition `كلب أنوس / العقور`.
- `.4`: polarity `الأنس/النفور`; `لكل ما يؤنس به` opens a local relational object class, not a global port.

**`U-ANS-B004` — `الجانب الإنسي المقبل على الإنسان`.** Intact carrier: `الإنسي الأيسر من كل شيء وقيل الأيمن وما أقبل منهما على الإنسان فهو إنسي وإنسي القوس ما أقبل عليك منها؛ الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب ومن الإنسان الجانب الذي يلي الرجل الأخرى؛ إنسي الدابة للجانب الذي يلي الراكب وإنسي القوس للجانب الذي يقبل على الرامي`.

- `.1` preserves alternatives `الأيسر` and `قيل الأيمن`; the operative invariant is the one of the two sides facing `الإنسان`. The bow's human-facing side is separately re-instantiated with addressed endpoint `عليك`.
- `.2`: animal-side tuple has left side as route for mounting and milking; human-body tuple has one side adjacent to the other leg. The animals, rider, milker, human, and leg remain local.
- `.3`: animal side is oriented toward rider; bow side toward archer. The topology `object side -> faces human operator` is a coalition interface without occupant exchange.

**`U-ANS-B005` — `إنسان العين وصورة الإنسان في السواد`.** Intact carrier: `إنسان العين صبيها الذي في السواد؛ إنسان العين المثال الذي يرى في السواد أي سواد العين؛ الإنسان أيضا إنسان العين وجمعه أناسي والإنسان الأنملة`.

- `.1`: possessed eye has its `صبيها`, located `في السواد`; exact relation names it `إنسان العين`.
- `.2`: `إنسان العين = المثال الذي يرى في السواد`; second equation resolves the containing dark field as `سواد العين`; viewer/controller of `يرى` remains grammatically open.
- `.3`: equations attach `الإنسان` to `إنسان العين` and separately to `الأنملة`; number result `جمعه أناسي`. These named senses stay distinct despite one form.

**`U-ANS-B006` — `ابن الإنس للنفس والصفوة`.** Intact carrier: `كيف ابن إنسك إذا سأله عن نفسه؛ كيف ابن إنسك يعني نفسه وفلان ابن إنس فلان أي صفيه وخاصته وهذا خدني وإنسي وخلصي وجلسي؛ كيف ترى ابن إنسك إذا خاطبت الرجل عن نفسه وفلان ابن أنس فلان أي صفيه وأنيسه؛ قيل ابن إنسك للنفس`.

- `.1`: questioner asks local addressee about `نفسه` through the expression `ابن إنسك`; interrogative content remains the person's state.
- `.2`: equation `ابن إنسك = نفسه`; separate relation `فلان ابن إنس فلان = صفيه وخاصته`; first-person equations `خدني/إنسي/خلصي/جلسي` retain their common possessor but do not identify the named roles beyond the assertion.
- `.3`: addressed man is asked about his self; separate intimate-role equation `ابن أنس فلان = صفيه وأنيسه`.
- `.4`: named-expression equation `ابن إنسك = النفس` closes the exact `النفس` circuit.

### `ح ق ق`: fixed opposition, obligation, owned claim, contest, verification, defense, thresholds, penetration, fitting, severity, and completion

**`U-HQQ-B001` — `ثبات مطابق للواقع ضد الباطل`.** Intact carrier: `الحق نقيض الباطل؛ أصل الحق المطابقة والموافقة؛ حققت الأمر وأحققته إذا تحققته وصرت منه على يقين؛ الحقيقة خلاف المجاز`.

- `.1` is the local polarity equation `الحق/الباطل`.
- `.2` releases two exact relation schemas, `المطابقة` and `الموافقة`, as the stated origin of `الحق`; standards and matching occupants are open.
- `.3`: first-person controller operates on `الأمر`; `تحققته` is the condition/operation and `صرت منه على يقين` the state transition. The two inflected verbs remain explicit terms.
- `.4` is the separate polarity `الحقيقة/المجاز`.

**`U-HQQ-B002` — `لزوم واجب واستحقاق ثابت`.** Intact carrier: `حق الشيء وجب؛ حقيق بكذا ومحقوق به؛ أحققت الشيء أي أوجبته واستحققته أي استوجبته؛ يستعمل استعمال الواجب واللازم والجائز`.

- `.1`: `الشيء` transitions into `وجب`; controller/cause open.
- `.2`: role equations `حقيق بكذا` and `محقوق به`; required content remains `كذا/ه` locally open.
- `.3`: first-person controller makes `الشيء` obligatory (`أوجبته`) and separately claims/enters deserved status (`استوجبته`); the two events are not merged.
- `.4`: usage relation places the form against `الواجب`, `اللازم`, and `الجائز`; these alternatives remain a lexical parameter field.

**`U-HQQ-B003` — `حق مخصوص يملكه صاحبه`.** Intact carrier: `إنك لتعرف الحقة عليك؛ الحق واحد الحقوق والحقة أخص منه، هذه حقتي أي حقي؛ استحقها على المشتري أي ملكها عليه؛ وبعولتهن أحق بردهن`.

- `.1`: addressed knower `ك`, object `الحقة`, obligation/claim directed `عليك`.
- `.2`: class relation `الحق واحد الحقوق`; specificity transformation `الحقة أخص منه`; deictic possessed equation `هذه حقتي = حقي`.
- `.3`: claimant/controller in `استحقها`, claimed object `ها`, counterparty `المشتري`; result `ملكها عليه`. The buyer is local only.
- `.4`: local husbands occupy comparative entitlement role `أحق`; content/action `بردهن`; the feminine objects and prior relation are local and not generalized.

**`U-HQQ-B004` — `محاقة يدعي كل طرف فيها الحق`.** Intact carrier: `حاق فلان فلانا إذا ادعى كل واحد منهما؛ حاقه أي خاصمه، والتحاق التخاصم والاحتقاق الاختصام؛ تحاق القوم واحتقوا إذا تخاصموا؛ حاققته فحققته أي خاصمته في الحق فغلبته`.

- `.1`: two local persons form reciprocal claim topology; content of each claim is suppressed after `ادعى` and remains open.
- `.2`: equations `حاقه = خاصمه`, `التحاق = التخاصم`, `الاحتقاق = الاختصام`; opponent is carried only inside each local occurrence.
- `.3`: local group is controller/participants of reciprocal dispute in two forms `تحاق/احتقوا`.
- `.4`: first-person controller disputes second-person object `ه` over `الحق`; resultant dominance `فغلبته`. Mutual contention and asymmetric outcome coexist in one tuple.

**`U-HQQ-B005` — `إثبات الحق وإظهاره`.** Intact carrier: `حققت الأمر وأحققته أي كنت على يقين منه؛ حققت قوله وظنه تحقيقا أي صدقت؛ حقق الرجل إذا قال هذا الشيء هو الحق؛ أحققت كذا أي أثبته حقا أو حكمت بكونه حقا، ليحق الحق`.

- `.1`: first-person controller, content `الأمر`, result state `يقين منه`; two verb forms are equation terms.
- `.2`: first-person verifier operates on local person's `قوله` and `ظنه`; result relation `صدقت`. Saying and supposition remain distinct contents.
- `.3`: local man produces quoted predication `هذا الشيء هو الحق`; saying event is required before his role `حقق`.
- `.4`: deictic content `كذا` becomes `حقا` under either establishing or judging operation; `ليحق الحق` preserves purpose/result. Evidence-display and completion facets from the branch summary remain open interfaces, not added occupants.

**`U-HQQ-B007` — `حقيقة يلزم حفظها`.** Intact carrier: `حامي الحقيقة إذا حمى ما يحق عليه أن يحميه ويقال الحقيقة الراية؛ الحقيقة ما يحق على الرجل أن يحميه؛ الحقيقة الراية والحرمة والفناء وما يلزمه الدفاع عنه؛ فلان يحمي حقيقته أي ما يحق عليه أن يحمى`.

- `.1`: protector role is conditional on protecting `ما يحق عليه أن يحميه`; separate naming assertion `الحقيقة = الراية`.
- `.2`: local man bears obligation; affected object is the relative `ما`; action `يحميه`.
- `.3`: named alternatives `الراية/الحرمة/الفناء` fill the local `الحقيقة` role; invariant is `ما يلزمه الدفاع عنه`.
- `.4`: `فلان` controls protection of possessed `حقيقته`; equation recovers the obligated-to-be-protected content. No surface person is this protector by identity.

**`U-HQQ-B008` — `ناقة بلغت حق الحمل والانتفاع`.** Intact carrier: `الحقة من أولاد الإبل ما استحق أن يحمل عليه؛ الحق من الإبل ابن ثلاث سنين وقد دخل في الرابعة والأنثى حقة؛ الحق من الإبل ما استحق أن يحمل عليه والأنثى حقة؛ أتت الناقة على حقها أي الوقت الذي ضربت فيه`.

- `.1`: camel offspring crosses an eligibility threshold; resultant role permits passive carrying `أن يحمل عليه`; carrier/beneficiary open.
- `.2`: local male camel is three years and has entered the fourth; gender alternative maps female to `حقة`.
- `.3`: same class/eligibility topology is restated without identifying a particular animal.
- `.4`: local she-camel reaches possessed `حقها`, equated with the time at which mating occurred; prior act and its time are required by the role.

**`U-HQQ-B009` — `طعنة استقامت حتى نفذت`.** Intact carrier: `طعنة محتقة إذا وصلت إلى الجوف؛ طعنة محتقة أي لا زيغ فيها وقد نفذت؛ المحتق من الطعن النافذ إلى الجوف`.

- `.1`: affected trajectory is the stab itself; endpoint `الجوف`; result `وصلت`.
- `.2`: same technical role has `NEGATED[زيغ]` and completed penetration `قد نفذت`.
- `.3`: class equation `المحتق من الطعن = النافذ إلى الجوف`. Weapon, striker, and struck occupant remain open.

**`U-HQQ-B010` — `إحكام رصين في نسج أو كلام`.** Intact carrier: `ثوب محقق إذا كان محكم النسج؛ كلام محقق أي رصين؛ أحققت الأمر إحقاقا إذا أحكمته وصححته`.

- `.1`: cloth occupant has woven structure; resultant state `محكم النسج`; maker open.
- `.2`: speech occupant receives role `محقق`, equation `رصين`; speaker and verifier open.
- `.3`: first-person controller operates on `الأمر`; paired results `أحكمته وصححته`.

**`U-HQQ-B011` — `حق يطابق موضعه كالمفصل والوعاء`.** Intact carrier: `الحق ملتقى كل عظمين والحق من الخشب؛ سقط على حاق رأسه وجئته في حاق الشتاء؛ الحقة من خشب وحق العاج وحق الورك وحق الوابلة وحق الكهول بيت العنكبوت؛ مطابقة رجل الباب في حقه`.

- `.1`: `الحق` names the meeting-place of every two bones and separately an item made of wood; the universal scope stays local.
- `.2`: one local fall ends on the middle/top of a head; a separate arrival is temporally located in `حاق الشتاء`.
- `.3`: material and anatomical/named alternatives remain separate: wooden box, ivory holder, hip socket, `الوابلة`, and `حق الكهول = بيت العنكبوت`.
- `.4`: door leg occupies its fitting socket; exact invariant `مطابقة`, direction `رجل الباب -> في حقه`, result fitted placement.

**`U-HQQ-B012` — `حقحقة تجهد الظهر في السير`.** Intact carrier: `الحقحقة أرفع السير وأتعبه للظهر؛ الحقحقة عند العرب أن يسار البعير ويحمل على ما يتعبه ولا يطيقه؛ الحقحقة السير الشديد`.

- `.1`: severe/high gait affects local back with fatigue; controller of travel open.
- `.2`: local camel is passively driven and loaded onto what tires it; `NEGATED[يطيقه]` fixes exceeded capacity; driver remains open.
- `.3`: equation `الحقحقة = السير الشديد`.

**`U-HQQ-B013` — `تمام حال الحيوان وقوته`.** Intact carrier: `أحقت الناقة من الربيع أي سمنت؛ استحقت الناقة سمنا وأحقت وحقت إذا سمنت؛ أحق القوم إحقاقا إذا سمن مالهم واحتق المال إذا سمن وانتهى سمنه`.

- `.1`: local she-camel, source/setting `من الربيع`, result `سمنت`.
- `.2`: three forms share the local she-camel's transition to fatness; event tokens remain distinct source examples.
- `.3`: local group enters `أحق` because its livestock/property becomes fat; separate local property reaches terminal fullness `انتهى سمنه`.

**`U-HQQ-B014` — `أحق من الخيل يطابق خطوه أو يشتد بدنه`.** Intact carrier: `الأحق من الخيل الذي لا يعرق؛ الأحق أن يطبق هذا ذاك؛ الأحق الذي يضع رجله في موضع يده؛ احتق الفرس أي ضمر`.

- `.1`: horse-class role with `NEGATED[يعرق]`.
- `.2`: deictic matching topology `هذا -> يطبق -> ذاك`; occupants intentionally unresolved.
- `.3`: horse places hind foot in the position of forefoot; same local horse and its two limbs are occupancy-bound within the event.
- `.4`: separate horse changes to `ضمر`; it is not the `.3` horse by form recurrence.

### `خ س ر`: decrease, trade loss, deficient measure, and augmented forms

**`U-XSR-B001` — `النقص العام`.** Intact carrier: `أصل واحد يدل على النقض؛ الخسر النقصان والخسران كذلك؛ خسر إذا نقص ميزانا أو غيره`.

- `.1`: exact source term `النقض` is retained beside the record's `النقص`; object and controller open.
- `.2`: equations `الخسر = النقصان` and `الخسران = كذلك` expose a state/result schema.
- `.3`: controller is suppressed; affected `ميزانا أو غيره`; result `نقص`. The alternative has local scope and is not a socket for all objects.

**`U-XSR-B002` — `خسارة التجارة`.** Intact carrier: `الخاسر الذي وضع في تجارته؛ خسر التاجر إذا وضع من رأس ماله؛ خسر في البيع خسرا وخسرانا؛ انتقاص رأس المال؛ صفقة خاسرة أي غير مربحة`.

- `.1`: local role `الخاسر`, setting/field `تجارته`, operation/result `وضع`; what is put/lost remains supplied only through the linked capital assertions.
- `.2`: local merchant is controller/affected possessor; source material `رأس ماله`; outgoing decrease `وضع منه`.
- `.3`: sale setting and resultant `خسرا وخسرانا`.
- `.4`: capital is affected participant in `انتقاص`.
- `.5`: transaction occupies `خاسرة`, equation `غير مربحة`; `NEGATED[ربح]` has transaction scope.

**`U-XSR-B003` — `إخسار الكيل والميزان`.** Intact carrier: `خسرت الميزان وأخسرته إذا نقصته؛ كلته ووزنته فأخسرته أي نقصته؛ أخسرت الميزان وخسرته؛ خسرت الشيء وأخسرته نقصته؛ ولا تخسروا الميزان؛ ينقصون في الكيل والوزن`.

- `.1`: first-person controller acts on the identical local balance across paired verb forms; result `نقصته`.
- `.2`: identical local measured object `ه` is first measured by volume and weight, then made deficient; the pronoun handoff is an explicit occupancy chain inside this utterance.
- `.3`: equation between two causative/active forms with local balance object.
- `.4`: general local object `الشيء` is reduced; its quantification remains inside the assertion.
- `.5`: plural addressees receive negation/prohibition `لا تخسروا`; affected balance explicit; denied result remains denied.
- `.6`: plural controller reduces within the two media/procedures `الكيل والوزن`; measured goods open.

**`U-XSR-B005` — `الخنسرى والخيسرى والخناسر`.** Intact carrier: `رجل خنسرى وقالوا خيسرى في موضع الخسران النون والياء زائدتان؛ الخناسر جمع خنسر وهو نحو الخنسرى وفي معناه وهم لئام الناس ورذالهم؛ الخناسر الضعاف من الناس؛ الخناسير الهلاك لا واحد له`.

- `.1`: local man receives named form `خنسرى`; variant `خيسرى` occupies the position of `الخسران`; the statement explicitly marks added `ن` and `ي`.
- `.2`: number mapping `الخناسر = جمع خنسر`; similarity `نحو الخنسرى وفي معناه`; class equations to `لئام الناس ورذالهم`.
- `.3`: class equation `الخناسر = الضعاف من الناس`.
- `.4`: `الخناسير = الهلاك`; `ABSENT[واحد له]` is a lexical-number vacancy, not an absent event participant.

### `ص ب ر`: self-restraint, coerced confinement, guarantee, sides, hard matter, blocked passage, cold, extract, fruit, cloud layers, heaps, requital, named classes, and closure

**`U-SBR-B001` — `حبس النفس عن الجزع`.** Intact carrier: `الصبر نقيض الجزع؛ الصبر حبس النفس عن الجزع؛ صبرت نفسي أي حبستها؛ حبس النفس على ما يقتضيه العقل والشرع`.

`.1` is polarity `الصبر/الجزع`. `.2` has `النفس` as affected occupant of `حبس`, direction away from `الجزع`, with controller open. `.3` explicitly binds first-person possessor/controller to the same local `نفسي` across `صبرت` and `حبستها`; self and affected self are one local occupant. `.4` gives the holding boundary/content `ما يقتضيه العقل والشرع`; its relative content remains constrained, not globally open. The supplied summary also preserves context-dependent contrasts with `الجبن` and `الضجر` without merging those states with `الجزع`.

**`U-SBR-B002` — `حبس القهر للقتل أو اليمين`.** Intact carrier: `المصبورة المحبوسة على الموت؛ الصبر نصب الإنسان للقتل؛ صبرت يمينه أي حلفته؛ قتل صبر ويمين صبر؛ الصبر الإكراه`.

`.1` has a feminine living patient in passive confinement toward death; confiner open. `.2` has local human passively positioned for killing. `.3` has first-person coercer and the other person's possessed oath as object; equation `حلفته`. `.4` retains two named configurations, killing and oath, under `صبر`. `.5` supplies the controller/polarity parameter `الإكراه`. These compelled tuples do not inherit self-control from B001.

**`U-SBR-B003` — `تحمل الكفالة والملازمة`.** Intact carrier: `الصبير هو الكفيل؛ صبرت بفلان إذا كفلت به فأنا به صبير؛ صبير القوم الذي يصبر لهم ويكون معهم في أمورهم`.

`.1` is role equation `الصبير = الكفيل`. `.2` keeps `فلان` as guaranteed endpoint across `صبرت به/كفلت به`; first-person controller enters resultant role `صبير`. `.3` gives a group's guarantor/supporter, beneficiary `لهم`, accompaniment `معهم`, scope `في أمورهم`; no particular surface group is identified.

**`U-SBR-B004` — `أعلى الشيء وجوانبه`.** Intact carrier: `صبر كل شيء أعلاه؛ أصبار الإناء نواحيه؛ أصبار القبر نواحيه؛ الصبر جانب الشيء`.

The four local equations name top/side boundaries: `صبر كل شيء = أعلاه`, vessel sides, grave sides, and `الصبر = جانب الشيء`. Each containing object remains local. The supplied branch also opens a fill-to-the-sides topology; material and filler remain open.

**`U-SBR-B005` — `حجر غليظ وأرض حصباء`.** Intact carrier: `الصبرة من الحجارة ما اشتد وغلظ؛ الصبارة الحجارة؛ الصبر الأرض التي فيها حصباء؛ أم صبار الحرة أو الصفاة`.

The first tuple maps a stone member to hard/thick state. The second names stones collectively. The third has land as container of pebbles. The fourth preserves alternatives `الحرة` and `الصفاة` under `أم صبار`; no stone or land occurrence transfers among them.

**`U-SBR-B006` — `الوقوع في شدة لا منفذ منها`.** Intact carrier: `وقع القوم في أم صبور إذا وقعوا في أمر عظيم؛ أم صبار الحرب والداهية الشديدة؛ وقع القوم في أم صبور أي في أمر شديد؛ أم صبور أمر لا منفذ له عنه`.

Two distinct local group occurrences undergo `وقع ... في` into an immense/severe matter. The named alternatives are war and severe calamity. Final tuple types the vacancy `NEGATED[منفذ له عنه]`: the contained participant has no exit from the local matter. This consequence is available to vacancy comparison, not as a universal impossibility.

**`U-SBR-B007` — `شدة برد الشتاء`.** Intact carrier: `صبارة الشتاء شدة برده؛ أتيته في صبارة الشتاء أي في شدة البرد`.

First equation binds winter's `صبارة` to intensity of its cold. Second has first-person arrival, local endpoint pronoun, temporal/state setting `في صبارة الشتاء`, equated with severe cold. Exact `الشتاء` meets `حاق الشتاء` while the arrival events remain distinct.

**`U-SBR-B008` — `الصبر المر وعصارته`.** Intact carrier: `الصبر بكسر الباء عصارة شجرة؛ الصبر هذا الدواء المر`.

`.1` asserts material identity `الصبر = عصارة شجرة`, preserving vowel instruction `بكسر الباء`, source class `شجرة`, and product role `عصارة`. `.2` asserts deictic identity with `الدواء المر`. The same local material may carry both asserted descriptions; the particular tree, extraction controller, patient, dose, and aftermath remain open.

**`U-SBR-B009` — `الصبار حمل الشجرة الحامض`.** Intact carrier: `الصبار حمل شجرة طعمه أشد حموضة من المصل؛ الصبار التمر الهندي`.

The fruit/product belongs to a tree; possessed taste is comparatively more sour than `المصل`. Separate name equation `الصبار = التمر الهندي`. This `الصبار` is not the B018 stopper or B005 stones.

**`U-SBR-B010` — `سحاب أبيض متراكم`.** Intact carrier: `الصبر سحاب مستو فوق السحاب الكثيف؛ الصبير السحاب الأبيض؛ السحاب الأبيض الذي يصبر بعضه فوق بعض درجا؛ الاصبار السحائب البيض`.

`.1` sets one level cloud above dense cloud, preserving vertical relation. `.2` names a white-cloud class. `.3` has parts of white cloud stack above one another in stages; each local cloud part remains within that occurrence. `.4` supplies plural white clouds. The cloud class is an exact interface to `المعصرات/السحائب`, not identity with a raining cloud.

**`U-SBR-B011` — `رقاقة الخوان وكومة الطعام`.** Intact carrier: `صبير الخوان رقاقته العريضة تبسط تحت ما يؤكل من الطعام؛ الصبرة من الطعام بعضه فوق بعض؛ اشتريت الشيء صبرة أي بلا وزن ولا كيل`.

`.1` has a broad sheet spread under edible food: support, under/over direction, and food class explicit. `.2` stacks some food above other food. `.3` has first-person buyer, object `الشيء`, sale-mode role `صبرة`, with `ABSENT[وزن] + ABSENT[كيل]`. The absence precedes no asserted deficiency; it contrasts structurally with active deficient measurement in `خ س ر`.

**`U-SBR-B012` — `الإقصاص والقود`.** Intact carrier: `فليصطبر معناه فليقتص؛ أقاد السلطان فلانا وأقصه وأصبره بمعنى واحد إذا قتله بقود`.

`.1` is an imperative-form equation `فليصطبر = فليقتص`; addressee and prior wrong remain open. `.2` has local ruler as controller and `فلان` as the same affected occupant across `أقاد/أقصه/أصبره`; the three forms are asserted `بمعنى واحد`, with killing under requital as result. This is an identity-preserving local pronoun chain.

**`U-SBR-B016` — `بطن من غسان`.** Intact carrier: `الصبر أيضا بطن من غسان`.

Named-class equation only: `الصبر = بطن من غسان`. It exposes group and source-lineage roles but no migration, action, or surface identity.

**`U-SBR-B017` — `الجبل ووسطه`.** Intact carrier: `الصبير الأقدر وهو الوسط من الجبال؛ الصبير الجبل`.

First equation names `الصبير الأقدر` as middle among mountains; second names `الصبير` as mountain. The class/member and middle-position relations remain local.

**`U-SBR-B018` — `سداد القارورة والبئر`.** Intact carrier: `أصبر سد رأس الحوجلة بالصبار وهو السداد؛ الصبار صمام القارورة`.

`.1` has open controller, affected opening `رأس الحوجلة`, instrument/material `بالصبار`, result `سد`, and equation `الصبار = السداد`. `.2` gives container-specific role `الصبار = صمام القارورة`. The supplied branch image also names well closure as an interface, but the intact assertions explicitly enact flask/bottle closure only; `OPEN[well occurrence]` remains unenacted.

### `ص ل ح`: non-corruption, reconciliation, suitability, and named persons and places

**`U-SLH-B001` — `الصلاح ضد الفساد والطلاح`.** Intact carrier: `أصل واحد يدل على خلاف الفساد؛ الصلاح نقيض الطلاح ورجل صالح ومصلح وأصلحت إلى الدابة أحسنت إليها؛ الصلاح ضد الطلاح وصلح الرجل صلاحا وصلوحا؛ الصلاح ضد الفساد والاصلاح نقيض الإفساد والمصلحة والاستصلاح؛ الصلاح ضد الفساد مختصان في أكثر الاستعمال بالأفعال وإصلاح الله تعالى الإنسان`.

`.1` supplies opposition to corruption. `.2` preserves polarity `الصلاح/الطلاح`, roles `رجل صالح/مصلح`, and a distinct first-person benefactive event directed to a local animal with result `أحسنت إليها`. `.3` has a local man transition expressed by `صلح -> صلاحا/صلوحا`. `.4` preserves two polarity pairs and named result/pursuit forms `المصلحة/الاستصلاح`. `.5` scopes the pair mainly to acts and supplies a separate repair occurrence whose controller and affected human are explicit in the utterance. No surface human is that affected human by form alone.

**`U-SLH-B002` — `الصلح إزالة النفار بين الناس`.** Intact carrier: `والصلح تصالح القوم بينهم؛ الصلاح بكسر الصاد المصالحة والاسم الصلح وقد اصطلحا وتصالحا واصالحا؛ الصلح يختص بإزالة النفار بين الناس، يقال اصطلحوا وتصالحوا`.

`.1` has local group as reciprocal participants and internal relation `بينهم`. `.2` gives pronunciation/nominal equations and three dual reciprocal forms; the two participants remain suppressed but constrained. `.3` gives process `إزالة`, affected state `النفار`, domain `بين الناس`, and two plural reciprocal forms. This topology can align with `تحاق القوم` and `تواصى القوم` only at coalition level.

**`U-SLH-B003` — `الصلاح للشيء ملاءمته`.** Intact carrier: `وهذا الشئ يصلح لك، أي هو من بابتك`.

Deictic thing is grammatical controller/theme; beneficiary/standard is addressed `لك`; result equation `هو من بابتك`. The supplied summary's `يوافقك ويلائم بابك` exposes suitability/matching interfaces. No particular surface `صالحات` object is the deictic thing by identity.

**`U-SLH-B004` — `صالح وما قاربه علما لشخص`.** Intact carrier: `وقد سمت العرب صالحا وصليحا ومصلحا؛ وصالح اسم للنبي عليه السلام`.

First tuple has local naming controller `العرب`, name alternatives as results, and unnamed named persons. Second is a named-person equation. These proper-name occupants do not enter S3.w5 through base-form contact.

**`U-SLH-B005` — `صلاح والصلح علمان لمواضع`.** Intact carrier: `إن مكة تسمى صلاحا؛ والصلح نهر بميسان؛ وصلاح في وزن حذام وقطام وهو اسم مكة؛ وصلاح مثل قطام اسم مكة`.

`.1` names local place `مكة` as `صلاحا`; namer suppressed. `.2` equates `الصلح` with a river located in `ميسان`. `.3` gives formal-weight relation to `حذام وقطام` and repeats place-name identity. `.4` gives similarity to `قطام` and repeats the same place-name role. Place and river remain distinct despite root/form contact.

### `ع ص ر`: time, pressing, rain, rising wind, refuge, withholding, gift, swallowing, maturity, enclosure, origin, affiliation, and named matter

**`U-ASR-B001` — `دهر ووقت متعاقب`.** Intact carrier: `العصر الدهر؛ العصران الليل والنهار؛ العصران الغداة والعشي؛ العصر العشي؛ صلاة العصر؛ العصار الحين؛ جاءني فلان عصرا أي بطيئا؛ نام وما نام لعصر`.

The first equation names duration. The two dual equations preserve alternative ordered pairs `الليل/النهار` and `الغداة/العشي`; neither pair is merged. Separate equations give evening, named prayer, and a time. In the arrival tuple `فلان` moves to first-person endpoint with manner/time equation `عصرا = بطيئا`. Final assertion preserves one positive sleep occurrence followed by `NEGATED[نام لعصر]`; the referent is locally suppressed. All contact S1.w1 by form, not event identity.

**`U-ASR-B002` — `ضغط حتى يتحلب`.** Intact carrier: `ضغط شيء حتى يتحلب؛ عصرت العنب واعتصرته؛ عصرت العنب وعصرته إذا وليت عصره بنفسك؛ يعصرون الأعناب والزيت؛ العصارة ما سال عن العصر؛ العصارة ما تحلب من شيء تعصره؛ كل شيء عصر ماؤه فهو عصير؛ المعصرة ما يعصر فيه العنب؛ المعصار شيء كالمخلاة يجعل فيه العنب ويعصر؛ العصر مصدر عصرت والمعصور الشيء العصير`.

`.1` has open controller, affected thing, pressure operation, and terminal expressed-fluid result. `.2` keeps first-person controller and identical local grapes across two verb forms. `.3` adds controller parameter `بنفسك`. `.4` has plural controllers and two affected material classes. `.5-.6` define `العصارة` as what flows/is expressed from pressing, with source thing open in `.6`. `.7` carries the same local thing through `عصر ماؤه` to resultant role `عصير`; its water/material lineage is explicit. `.8` defines press as container/medium for grapes. `.9` defines bag-like instrument, grapes placed inside, and passive/open-controller pressing. `.10` maps event noun to verb and `المعصور` to affected/resultant `الشيء العصير`.

**`U-ASR-B003` — `سحاب يمطر ومطر يعصر`.** Intact carrier: `المعصرات السحائب تعتصر بالمطر؛ المعصرات سحائب تجيء بمطر؛ السحابة المعصر التي تتحلب بالمطر؛ أعصر القوم إذا أتاهم المطر؛ عصر القوم أي مطروا؛ قرئت وفيه يعصرون أي يأتيهم المطر؛ تعصرون بضم التاء أي تمطرون`.

Clouds are locally equated with `المعصرات` and bear/express rain; a second cloud occurrence comes with rain; a singular cloud drips with rain. In `.4`, local group receives rain (`أتاهم`). In `.5`, local group is grammatical controller of `عصر` but equation outcome is `مطروا`. `.6` preserves reading equation `يعصرون = يأتيهم المطر`; `.7` preserves vowel instruction and `تعصرون = تمطرون`. Controllers, clouds, and rain occupants do not move between these examples absent coreference.

**`U-ASR-B004` — `إعصار وغبار مستدير`.** Intact carrier: `الإعصار ريح تهب تثير الغبار فيرتفع إلى السماء كأنه عمود؛ الإعصار الغبار الذي يسطع مستديرا والجمع الأعاصير؛ الإعصار الريح التي تهب من الأرض كالعمود الساطع نحو السماء؛ إعصار وعصار وهو أن تهيج الريح التراب فترفعه؛ مرت امرأة متطيبة لذيلها عصر؛ لذيلها عصرة تكون العصرة من فوح الطيب وهيجه`.

`.1` binds local wind through blowing and dust-raising; the same dust rises toward sky with column likeness. `.2` instead names the rising circular dust and supplies plural. `.3` names wind rising from earth toward sky like a shining column. `.4` keeps wind as initiator, soil as affected occupant carried upward. `.5` has perfumed woman moving past and a wake attached to her hem. `.6` identifies that hem-wake as perfume emission/agitation. Wind, dust, soil, perfume, and woman remain local.

**`U-ASR-B005` — `ملجأ ومنجاة واعتصام`.** Intact carrier: `تعلق بشيء وامتساك به؛ العصر الملجأ؛ العصر المنجاة والعصرة والمعتصر والمعصر؛ اعتصرت بفلان وتعصرت أي التجأت إليه؛ اعتصر بالمكان إذا التجأ إليه؛ الاعتصار الالتجاء؛ عصرة المنجود؛ ما بينهما عصر ولا يصر أي ما بينهما مودة ولا قرابة`.

The first tuple binds an open participant to a thing by attachment/holding. Equations name refuge and rescue alternatives. A first-person seeker moves toward local `فلان` under two forms, equated with taking refuge; another seeker uses a place as endpoint. `الاعتصار = الالتجاء`. `عصرة المنجود` remains a complete named expression with roles open. Final assertion has two local parties and explicitly negates `عصر/يصر`, interpreted locally as `NEGATED[مودة] + NEGATED[قرابة]` between them.

**`U-ASR-B006` — `حبس ومنع واسترجاع`.** Intact carrier: `العصر الحبس؛ تعصر أي تعسر؛ ما عصرك أي ما منعك؛ اعتصرت ماله إذا استخرجته من يده؛ يعتصر الوالد على ولده في ماله أي يمنعه إياه ويحبسه عنه؛ يعتصر يسترجع؛ أعطيت فلانا عطية فاعتصرتها أي رجعت فيها؛ المعتصر الذي يأخذ من الشيء يصيب منه؛ فلان عاصر إذا كان ممسكا`.

Equations expose confinement and difficulty. The question maps `عصرك` to a preventing force/controller. First-person extracts the same local property from its possessor's hand. Parent tuple keeps parent as controller, child as counterparty, property as identical affected occupant, with outcomes withholding and confinement away from child. `يعتصر = يسترجع`. A gift is first handed to `فلان`, then the identical gift is taken back: explicit occupancy lineage across giving and reversal. Further roles take/receive from a thing or remain withholding. These controller and consent parameters stay atomic.

**`U-ASR-B007` — `عطاء وغلة مستخرجة`.** Intact carrier: `العصر العطية؛ يعصر فينا كالذي تعصر أي تعطي؛ العرب تجعل العصارة والمعتصر مثلا للخير والعطاء؛ المعتصر الذي يصيب من الشيء ويأخذ منه؛ العصارة الغلة؛ يعصرون قال يستغلون بأرضيهم؛ وفيه تعصرون أي تستغلون`.

Equations name gift, giving, goodness/giving exemplars, recipient/taker role, and yield. Plural landholders exploit/obtain yield through their own lands; final reading equation preserves `تعصرون = تستغلون`. The property extracted in B006 is not the yield or gift here unless a local assertion says so; the shared topology travels only as coalition.

**`U-ASR-B008` — `شرب قليل لإساغة الغصة`.** Intact carrier: `الاعتصار أن يغص الإنسان بالطعام فيعتصر بالماء وهو أن يشربه قليلا قليلا ليسيغه؛ لو بغير الماء حلقي شرق كنت كالغصان بالماء اعتصاري`.

Local human undergoes choking by food, then uses water as medium in repeated small drinking, with result/purpose swallowing it. The pronoun object of `ليسيغه` stays attached to its local swallowed obstruction/content. Second utterance has first-person throat, counterfactual other-than-water condition, choking state, and comparison to one whose recourse is water. Exact `الإنسان` contacts S2 without occupant identity.

**`U-ASR-B009` — `بلوغ الجارية عصر شبابها`.** Intact carrier: `الجارية أول ما أدركت وحاضت يقال قد أعصرت؛ التي قاربت الحيض؛ بلغت عصر شبابها وإدراكها؛ إذا رأت في نفسها زيادة الشباب فقد أعصرت وهي معصر؛ إذا بلغت الجارية وقربت من حيضها فهي معصر؛ المعصر ساعة تطمث أي تحيض لأنها تحبس في البيت يجعل لها عصرا`.

Distinct girl occurrences approach or cross supplied maturity/menstruation thresholds and receive `أعصرت/معصر`. One perceives increase of youth in her own self before role assignment. Final tuple gives moment equation `تطمث = تحيض`, causal household confinement, and made enclosure. None is the camel threshold occupant in `ح ق ق`; only the threshold topology aligns.

**`U-ASR-B010` — `زرع يتحرز في أكمامه`.** Intact carrier: `عصر الزرع صار في أكمامه؛ إذا تبينت أكمام السنبل قيل قد عصر الزرع؛ مأخوذ من العصر وهو الحرز أي تحرز في غلفه`.

The same local crop transitions into its husks; visible ear-husks license the named crop state; explicit derivation maps `العصر` to `الحرز` and the crop to enclosure in its coverings. Enclosure and occupant identity are local.

**`U-ASR-B011` — `أصل وحسب ونسب`.** Intact carrier: `العنصر والعنصر الأصل والحسب؛ كريم المعصر أي كريم عند المسألة؛ فلان كريم العصير أي كريم النسب؛ العنصر أصل الحسب ومما زيدت فيه النون وهو في الأصل العصر وهو الملجأ؛ كلا يئل في الانتساب إلى أصله الذي هو منه`.

Equations name origin/lineage and generosity roles. `فلان` bears noble lineage locally. The derivational tuple explicitly keeps full `العنصر`, added `ن`, base `العصر`, and equation `العصر = الملجأ`. Final assertion has each local affiliate return for refuge in the origin from which it is; controller and origin are bound only within that generic assertion.

**`U-ASR-B012` — `دنية في الموالاة`.** Intact carrier: `العصرة أيضا الدنية؛ هؤلاء موالينا عصرة أي دنية دون من سواهم؛ هؤلاء موالينا عصرة أي دنية دون من سواهم`.

Named equation and two duplicate source occurrences remain indexed separately. Deictic group is affiliated to speaker-group, assigned lower/nearer status relative to explicitly excluded others `دون من سواهم`.

**`U-ASR-B013` — `العصرة شجرة`.** Intact carrier: `العصرة شجرة`. Exact name equation only; no extract, pressing, or medicine event is asserted here.

**`U-ASR-B014` — `لسان معصور من العطش`.** Intact carrier: `المعصور اللسان اليابس عطشا`. Equation gives local tongue, dry state, and cause `عطشا`; no drinking result is supplied.

**`U-ASR-B015` — `العصار ريح البطن`.** Intact carrier: `العصار الفساء`. Exact equation only; the branch image supplies bodily wind class. It does not inherit whirlwind scale or dust trajectory.

### `ع م ل`: intended act, making another act, appointment, wage, transaction, manual work, burden, aptitude, tool parts, organs, road, and walkers

**`U-AML-B001` — `الفعل المقصود والعمل`.** Intact carrier: `أصل واحد صحيح وهو عام في كل فعل يفعل؛ عمل عملا فهو عامل؛ كل فعل يكون من الحيوان بقصد؛ الأعمال الصالحة والسيئة`.

The first assertion gives locally universal act scope. The second has a controller perform `عملا` and enter role `عامل`. The third requires animal agent and intention parameter `بقصد`. The fourth gives the complete positive/negative object-class contrast. Surface S3.w4-w5 exactly re-instantiates `عمل + الصالحات`; it does not instantiate `السيئة`.

**`U-AML-B002` — `إعمال الشيء واستعماله`.** Intact carrier: `يستعمل غيره ويعمل رأيه أو كلامه أو رمحه؛ والبناء يستعمل اللبن؛ أعمله غيره واستعمله بمعنى؛ واستعمله أيضا أي طلب إليه العمل؛ أعمل فلان ذهنه في كذا وكذا إذا دبره بفهمه`.

Separate tuples have controller operate another, opinion, speech, or spear; builder uses bricks as material. Equation `أعمله غيره = استعمله` preserves controller rotation; another equation makes `استعمله` a request to the same local other to work. Last tuple has `فلان` direct his own mind at constrained content and produce deliberation through understanding.

**`U-AML-B003` — `ولاية العمل والقيام عليه`.** Intact carrier: `العاملين عليها هم السعاة الذين يأخذون الصدقات؛ استعمل فلان إذا ولي عملا من أعمال السلطان؛ التعميل تولية العمل؛ العاملين عليها هم المتولون على الصدقة`.

Collectors are equated with agents who take alms; the relative `الذين` stays inside this class assertion. `فلان` enters an appointed office from ruler's works; appointing controller is suppressed. `التعميل = تولية العمل`. Final equation restates administrators over alms. Role schema, not official occupants, can enter appointment coalitions.

**`U-AML-B004` — `أجر العمل ورزق العامل`.** Intact carrier: `العمالة أجر ما عمل؛ العمالة بالضم رزق العامل؛ العمالة رزق العامل؛ العملة والعمالة أجر العمل؛ العمالة أجرته`.

All five equations remain separate: compensation is tied to prior performed content, worker's provision, work's wage, or possessed wage. The worker and labor occurrence remain locally open unless the assertion names them.

**`U-AML-B005` — `المعاملة بين الناس`.** Intact carrier: `المعاملة مصدر من قولك عاملته وأنا أعامله معاملة؛ عاملت الرجل أعامله معاملة في المبايعة وغيرها`.

First-person controller and the same pronominal counterpart persist across perfect/imperfect verbal occurrences and event noun. Second binds counterpart as `الرجل`, setting `المبايعة وغيرها`; `غيرها` is a local alternative, not global.

**`U-AML-B006` — `العملة العاملون بالأيدي`.** Intact carrier: `العملة القوم يعملون بأيديهم ضروبا من العمل حفرا أو طيا أو نحوه؛ العملة القوم الذين يعملون بأيديهم ضروبا من العمل في طين أو حفر أو غيره`.

Two group occurrences are manual controllers, hands are instruments, and work classes are digging, lining/folding, clay, or locally scoped alternatives. The groups remain distinct from surface `ٱلَّذِينَ`.

**`U-AML-B007` — `التعمل بمعنى التعني`.** Intact carrier: `لا تتعمل في أمرك ذا كقولك لا تتعن؛ سوف أتعمل في حاجتك أي أتعنى؛ لا تعمل أي لا تتعن`.

First and third are addressed negations equated with not burdening oneself. Second has future first-person effort directed into addressee's need, equation `أتعمل = أتعنى`. Denied acts remain denied.

**`U-AML-B008` — `المطبوع على العمل`.** Intact carrier: `اليعملة من الإبل اسم لها اشتق من العمل؛ رجل عمل بكسر الميم أي مطبوع على العمل؛ ورجل عمول؛ اليعملة الناقة النجيبة المطبوعة على العمل؛ ناقة عملة بينة العمالة مثل اليعملة إذا كانت فارهة؛ اليعملة مشتقة من العمل`.

Explicit derivation binds named camel form to `العمل`. Separate man roles preserve vowel instruction and aptitude. A noble she-camel is disposed toward work; another local she-camel is visibly work-capable and likened to `اليعملة` under excellence. No animal transfers to severe-gait or security-camel tuples.

**`U-AML-B009` — `عامل الرمح`.** Intact carrier: `عامل الرمح وعاملته وهو ما دون الثعلب قليلا مما يلي السنان وهو صدره؛ عامل الرمح ما يلي السنان وهو دون الثعلب؛ عامل الرمح صدره دون السنان ويجمع عوامل؛ عامل الرمح ما يلي السنان`.

Each tuple locates the named spear part relative to point and `الثعلب`, alternatively names it the shaft/front, and supplies plural `عوامل`. These are part-position relations; no stabbing event is asserted.

**`U-AML-B010` — `الجارحة العاملة`.** Intact carrier: `عوامل الدابة قوائمه واحدها عاملة؛ وترقبه بعاملة قذوف أي ترقبه بعين بعيدة النظر`.

First maps animal legs to plural/singular working-part names. Second has watcher, watched pronominal object, eye instrument, and long-distance sight capacity. The eye contacts perception and `إنسان العين` tuples without sharing an eye occupant.

**`U-AML-B011` — `الطريق المعمل`.** Intact carrier: `طريق معمل أي لحب مسلوك`. Equation gives road, open/worn state, and prior traversal implied by `مسلوك`; travelers remain open.

**`U-AML-B012` — `بنو العمل من المشاة`.** Intact carrier: `المسافرون إذا مشوا على أرجلهم يسمون بني العمل`. Travelers control walking, legs are medium, and resultant name follows the walking condition. No particular road is filled.

### `و ص ي`: connection, carried instruction, reciprocal recommendation, and pasture fit

**`U-WSY-B001` — `وصل الشيء بالشيء`.** Intact carrier: `أصل يدل على وصل شيء بشيء؛ ووصيت الشيء وصلته؛ وصيت الليلة باليوم وصلتها؛ تواصى النبت إذا اتصل؛ أرض واصية متصلة النبات؛ فلاة واصية يتصل بفلاة أخرى؛ وصى الشيء يصي إذا اتصل ووصاه غيره وصله`.

The first tuple opens two distinct things and a connecting operation. The second binds identical local thing across `وصيت/وصلته`. The third connects night to day with direction retained. Plant becomes continuous; land has continuous vegetation; one desert connects to another. Final assertion distinguishes self-connection from another controller connecting it. None of these occupants enters a surface reciprocal recommendation event.

**`U-WSY-B002` — `عهد موصول إلى غيره`.** Intact carrier: `الوصية من هذا القياس كأنه كلام يوصى أي يوصل؛ وصيته توصية وأوصيته إيصاء؛ الوصاة كالوصية؛ الوصاية مصدر الوصي؛ الوصية بعد الموت؛ الوصية ما أوصيت به؛ أوصيت له بشئ وأوصيت إليه إذا جعلته وصيك؛ الوصي الموصي والموصى إليه جميعا؛ التقدم إلى الغير بما يعمل به مقترنا بوعظ`.

Instruction is likened to speech connected onward; paired verb/event-noun forms preserve a local content object. `الوصاة` is likened to `الوصية`; guardianship is the role's event noun. One instruction is temporally after death; another is exactly the content previously instructed. Giving something for a beneficiary differs from directing to an appointee who becomes `وصيك`. The same form `الوصي` can name recommender and recipient roles without identifying their occupants. Final tuple has initiator, direction to another, content schema `ما يعمل به`, and accompaniment `وعظ`.

**`U-WSY-B003` — `تبادل الوصية بين القوم`.** Intact carrier: `تواصى القوم إذا تواصلوا؛ تواصى القوم أي أوصى بعضهم بعضا؛ تواصى القوم إذا أوصى بعضهم إلى بعض`.

Three local group occurrences instantiate reciprocal topology. First equates it with mutual connection. Second and third distribute initiator and endpoint roles among group members (`بعضهم -> بعض`). Surface S3.w6 and S3.w8 each re-instantiate this role schema with the surface relative group as controller and with its own content complement.

**`U-WSY-B004` — `موافقة المرعى للسائمة`.** Intact carrier: `إذا أطاع المرعى للسائمة فأصابته رغدا قيل وصى لها المرتع يصي وصيا`.

Pasture is grammatical controller/theme, grazing animals beneficiary, result abundance/ease reaches them, and the configuration receives the named verb. The branch's exact suitability relation `موافقة المرعى للسائمة` remains a coalition interface to `المطابقة والموافقة` and `يصلح لك`; no pasture or animal crosses records.

## Occupancy graph: licensed literal continuities

Only the following continuities carry occupants, states, materials, or results. Every other cross-attraction below is coalition-only.

```text
O-S2.1  ٱلْإِنسَٰنَ@S2.w2
  -> SX-02 governed-ism identity
  -> participant of إِنَّ@S2.w1
  -> SX-03/SX-04 surface-predication binding
  -> same surface human occurrence located/predicated لَفِى خُسْرٍ@S2.w3-w4

O-S3.1  ٱلَّذِينَ@S3.w2
  -> SX-05 exception-scope identity + 3MP surface agreement
  -> controller of ءَامَنُوا@S3.w3
  -> SX-06 coordination identity
  -> controller of عَمِلُوا@S3.w4
  -> SX-08 coordination identity
  -> controller of first تَوَاصَوْا@S3.w6
  -> SX-10 coordination identity
  -> controller of second تَوَاصَوْا@S3.w8

O-S3.2  ٱلصَّٰلِحَٰتِ@S3.w5
  -> SX-07 direct-object occupancy
  -> affected/content object of عَمِلُوا@S3.w4 only

O-S3.3  حَقّ@S3.w7
  -> SX-09 governed-complement occupancy
  -> content of first تَوَاصَوْا@S3.w6 only

O-S3.4  صَبْر@S3.w9
  -> SX-11 governed-complement occupancy
  -> content of second تَوَاصَوْا@S3.w8 only
```

The four S3 predicates are distinct occurrences even though their controller is the same discourse group. The two `تَوَاصَوْا` occurrences instantiate the same reciprocal schema but do not share an event. The explicit surface contents are different occupants. The lexical assertion `تواصى القوم أي أوصى بعضهم بعضا` re-instantiates two internal reciprocal roles in each surface event; it transports the role specification, not its lexical `القوم` occupant:

```text
R-WSY-S3a  U-WSY-B003 reciprocal schema بعضهم -> أوصى -> بعضا
  -> exact-lemma re-instantiation; new controller supplied by S3.w2
  -> event S3.w6; content supplied by S3.w7; individual member allocation OPEN

R-WSY-S3b  U-WSY-B003 reciprocal schema بعضهم -> أوصى -> بعضا
  -> exact-lemma re-instantiation; new controller supplied by S3.w2
  -> distinct event S3.w8; content supplied by S3.w9; individual member allocation OPEN
```

Further source-internal occupancy paths remain local:

- `O-AMN.2`: `النفس -> fear removed -> طمأنينة` inside `أصل الأمن طمأنينة النفس وزوال الخوف`.
- `O-ANS.2`: each attached object pronoun remains identical across its asserted perception equation (`آنسته -> أبصرته`, `آنست الصوت -> سمعته`, `آنست منه رشدا -> علمته`).
- `O-XSR.3`: the measured object `ه` continues through `كلته -> وزنته -> أخسرته/نقصته`; this explicit chain does not become S2's loss-state occupant.
- `O-SBR.1`: first-person possessor/controller restrains identical `نفسي/ها` in `صبرت نفسي أي حبستها`.
- `O-SBR.12`: `فلانا/ه` is the identical patient across `أقاد السلطان فلانا وأقصه وأصبره ... قتله بقود`.
- `O-ASR.2`: grape/material identity continues through local pressing assertions to expressed liquid only where `كل شيء عصر ماؤه فهو عصير` or `العصارة ما تحلب من شيء تعصره` asserts the lineage. Controller, particular source thing, and instrument remain assertion-local.
- `O-ASR.4`: dust/soil raised by local wind is the same affected material that rises in that utterance; no cloud or bodily wind enters.
- `O-ASR.6`: the same gift in `أعطيت فلانا عطية فاعتصرتها` passes to `فلان` and returns under first-person repossession. This is a true reversal lineage.
- `O-AML.5`: counterpart `ه/الرجل` persists across `عاملته/أعامله` inside each transaction utterance.
- `O-WSY.1`: the same `الشيء` is connected across `وصيت الشيء وصلته`; night remains the same local night connected to local day in the next assertion.
- `O-WSY.2`: `الوصية ما أوصيت به` identifies instruction-content with what was instructed; `أوصيت إليه` makes its local endpoint enter the role `وصيك`.

`U-SBR-B008.1` gives `الصبر = عصارة شجرة`, while `U-ASR-B002.5-.7` define the role and lineage of `عصارة/عصير`. The exact term licenses full enactment but does not, by itself, identify a particular B008 tree with a particular B002 pressed thing. The recoverable path is therefore split:

```text
O-SBR.8  local medicinal material -> asserted identity -> عصارة شجرة
K-ASR/SBR exact technical-role interface: عصارة -> product-of-expression relation
OPEN[identity of a particular tree with a particular pressing-source occurrence]
OPEN[controller, instrument, and actual pressing event for the B008 material]
```

## Coalition field: payload-preserving links

### Positioned surface architecture

`K-SURF-1` carries the whole line vectors `[1,4,9] / [3,6,21] / [1,3,7]`: single governed oath carrier -> predicated participant/state carrier -> exception scope with four coordinated predicates. Only ordinal work, attachment density, and boundary transformation travel. No line occupant crosses this link.

`K-SURF-2` maps passage starts `وَ -> إِنَّ -> إِلَّا` as three changed particle operations: government of an oath complement -> government plus predication -> exception and scoped coordination. `K-SURF-3` maps endings `definite GEN عصر -> indefinite GEN خسر -> definite GEN صبر`; it carries boundary position, case, definiteness delta, and terminal `ر`, not lexical meaning or entity.

`K-SURF-4` maps the two exact `تواصوا` tuples maximally:

```text
relative-group controller -> perfect reciprocal act -> بِ-governed definite content
same controller           -> perfect reciprocal act -> بِ-governed definite content
delta: ordinal 3rd predicate / حق content -> ordinal 4th predicate / صبر content
invariant: form, root, measure VI, aspect, 3MP, conjunction, reciprocal topology,
           preposition, definiteness, masculine genitive complement
```

### Exact-relation and changed-controller constellations

`K-OPPOSITION` connects only the recurring explicit relation types: `الأمن/الخوف`, `الأمانة/الخيانة`, `الحق/الباطل`, `الحقيقة/المجاز`, `الصبر/الجزع`, `الصلاح/الطلاح`, `الصلاح/الفساد`, `الإصلاح/الإفساد`, `الإنس/الجن`, `الإيناس/الإيحاش`, `الإنس/الوحشة`, `الأنس/النفور`, and `كلب أنوس/العقور`. Payload is `[binary polarity; named relation ضد/نقيض/خلاف; local positive and opposed positions]`. No term occupies another pair's position.

`K-NAFS` uses exact `النفس`: security tuple removes fear and yields quiet; faith tuple has self yield toward truth by assent; patience tuple has a self held by its own controller; human-expression tuple makes self the referent of inquiry. Payload is `[same named participant class + changed operation/controller/direction/outcome]`, not one soul occurrence.

`K-TRUTH-CONTENT` begins at exact `الحق` in `إذعان النفس للحق على سبيل التصديق`, expands through `الإيمان = التصديق`, `حققت قوله وظنه ... صدقت`, `قال هذا الشيء هو الحق`, and the surface content `بالحق`. It carries a content/verification topology: content can be assented to, verified/judged, asserted in speech, or reciprocally recommended. Controllers change from local self, verifier, speaker, and S3 group; contents remain local. `التقدم إلى الغير بما يعمل به مقترنا بوعظ` exposes a recommendation-content schema actable by another, and `الأعمال الصالحة والسيئة` plus S3 direct object exposes intentional action; only the schema `recommended content -> something acted upon` travels. No surface claim that S3's truth content was the direct object of S3's `عملوا` is created.

`K-RECIPROCAL-GROUP` aligns the complete local topologies `تواصى القوم/بعضهم بعضا`, `تصالح القوم بينهم`, `تحاق القوم/احتقوا`, and `المعاملة بين الناس`. Invariant: plural or paired participants distribute action internally. Deltas: connection/recommendation; removal of estrangement; mutual contest with possible asymmetric victory; buying or other dealing. Each group and counterparty remains local. Surface S3 supplies two more recommendation realizations with different contents.

`K-MATCHING` carries exact `المطابقة/الموافقة` from `أصل الحق`, the fitted door leg in its socket, the horse foot placed at the forefoot position, the suitable thing `يصلح لك`, and pasture fit for grazing animals. Parameter vectors differ: abstract standard open; physical part/socket; moving animal limbs; beneficiary-addressed suitability; pasture/animal abundance. No hybrid realization is manufactured.

`K-HOLDING-COUNTERFIELD` aligns `حبس النفس`, coerced confinement toward death/oath, `العصر الحبس`, parent withholding a child's property, girl confined in house, crop enclosed in husks, stopper closing a flask, and attachment/holding in refuge. The invariant is a supplied hold/boundary relation. Controllers and consent change: self-control; open coercer; parent; household/passive cause; growth transition; closer/instrument; seeker attaching itself. Outcomes change among restraint, death-facing captivity, denied access, maturity enclosure, protection, sealed opening, and refuge. No occupant or denied result crosses.

`K-EXTRACTION-REVERSAL` connects pressing-source -> expressed product, property extracted from another's hand, gift given then reclaimed, yield obtained from land, and recipient who takes from a thing. It carries direction and controller changes only: material outward under pressure; property away from possessor; gift outward then back; yield from land; share from thing. `العصر العطية` and `العصر الحبس` remain opposed local realizations in the same form field without being averaged.

`K-MEASURE-VACANCY` maps `كلته ووزنته فأخسرته` against `اشتريت الشيء صبرة أي بلا وزن ولا كيل`. Both explicitly name `كيل/وزن` and a transaction/material context. First: procedures occur and their result is deficient. Second: procedures are absent at sale. Payload is `[measurement status + consequence type]`; no goods, buyer, measurer, or deficiency transfers.

`K-CLOUD-WATER` maps raining `المعصرات/السحائب`, dripping singular cloud, white cloud, level cloud above dense cloud, and white cloud stacked in stages. Specifically named class `السحاب/السحائب` licenses emission. Deltas are rain-bearing/dripping versus color, density, vertical layer, and staged stacking. The coalition does not assert that a white layered cloud rained.

`K-ENCLOSURE-EXIT` connects vessel/grave sides, stacked food, no-exit severe matter, refuge/place, crop in husks, boxes/sockets, and bottle stopper. Payloads remain typed: lateral boundary; above/below pile; `NEGATED[exit]`; available refuge endpoint; protective covering; fitting receptacle; sealed aperture. The exact contrast `ملجأ/منجاة` versus `لا منفذ` is a vacancy-mechanism counterfield, not a claim about one trapped occupant.

`K-THRESHOLD` maps camel entering fourth year and entitlement to carry, girl approaching/entering maturity, livestock reaching terminal fatness, and crop becoming enclosed when husks appear. Payload is `[prior state -> stated boundary -> named resultant role]`; species, body, time, controller, and consequences remain local.

`K-PERCEPTION` connects seeing/hearing/knowing tuples, human-facing object sides, image seen in eye-darkness, long-sighted working eye, and the girl who sees increased youth in herself. Interfaces are specifically supplied `رأى/أبصر/سمع/علم/عين/نظر` and facing-to-observer topology. Objects and perceivers never transfer through the coalition.

`K-MOVEMENT-PARTS` holds open a connected but nonliteral architecture: severe gait exhausts camel/back; travelers walk on legs; animal legs are `عوامل`; traversed road is `معمل`; spear's `عامل` is positioned by its point; a penetrating stab reaches interior without deviation. Exact `عمل/عامل`, named legs, road traversal, and tool-part position expose adjacent interfaces. No source edge identifies a particular traveler, road, camel, spear, or stab, so every occupant stays local and the links remain coalition-only.

`K-DERIVATION` connects only explicit formal histories: `العنصر -> ن added -> العصر`; `خنسرى/خيسرى -> ن/ي added in the position of الخسران`; `اليعملة -> مشتقة من العمل`; `الوصية -> كلام يوصى أي يوصل`. Payload is base/form transformation and asserted relational equation. Resulting origin, person class, camel class, and instruction content remain separate.

## Open ports and unresolved attractions

- S1 supplies government of `العصر` but no surface assertion of which `ع ص ر` lexical occurrence, no oath-result port, and no link to the S2 participant. All fifteen lexical branch realizations remain active against the exact form.
- S2 supplies one human occurrence and a loss-state predication. It does not supply a cause, initiator, instrument, scale, trade, balance, quantity, prior capital, or aftermath. The exception edge relates S3 scope to the preceding structure syntactically but does not identify the S2 singular occurrence with the S3 plural group.
- S3 faith has no explicit surface complement. Lexical `إذعان النفس للحق` opens a truth-endpoint schema, but it does not move S3.w7 backward as an occupant or make the faith event identical to the recommendation event.
- The individual senders and recipients inside each reciprocal `تواصوا` are constrained to the re-instantiated `بعضهم/بعضا` roles but not individually allocated.
- `الصالحات` is the action object; which acts, materials, recipients, and results it contains remain unspecified. Proper-name `صالح`, place-name `صلاح`, river `الصلح`, and reconciliation participants remain excluded from this occupancy port.
- `الحق` content carries no explicit surface proposition; every lexical right, camel, joint, box, stab, cloth, claim, and horse remains a distinct tuple, available through form contact but not inserted into the content.
- `الصبر` content carries no explicit surface patient, coercer, duration, boundary, stone, medicine, cloud, heap, mountain, group, or stopper. These remain separately enacted source tuples.
- The exact source phrase `عصرة المنجود`, the technical terms `الوابلة`, `الثعلب`, and the branch-image well closure retain their constrained openings. No generic completion is supplied.

## Forward and backward formation passes

### Forward pass: S1 -> S2 -> S3

The passage begins with one word whose internal sequence is particle -> determiner -> time/press/refuge/hold/gift/etc. form-field. None is selected. The first boundary is both minimal in word count and internally tripartite. S2 expands to four words and distributes particle, definite participant, emphasis/preposition, and indefinite state. Its exact occupancy path is human -> predicated containment -> loss; the lexical loss field simultaneously keeps decrease, trade, measurement, and named augmented forms active without filling the surface event.

S3 begins by changing the line-opening particle into exception, then gives a relative plural controller and four perfect occurrences. The first predicate exposes security/assent/prayer-act records but has an open surface endpoint. The second is immediately surface-bound to the feminine-plural positive-act object, closing the exact `الأعمال الصالحة والسيئة` collision in one polarity while leaving the negative alternative unoccupied. The third and fourth repeat a reciprocal connective operation: first with truth content, then with restraint content. Their complete parallel vectors enact difference without sharing event identity.

Forward lexical enactment keeps several trajectories simultaneously live: quieting/removing fear -> assent toward truth; perception -> image/facing/knowledge; fixing/obligation/verification -> claim/defense/fitting; decrease -> deficient or absent measure; restraint -> coercion/guarantee/boundary/material/cloud; repair -> reconciliation/suitability/naming; time -> pressure/product/rain/refuge/withholding/gift/enclosure; intended act -> appointment/wage/tool/road; connection -> instruction -> reciprocal internal transmission. These are active paths through supplied interfaces, not selected channels.

### Backward pass: S3 -> S2 -> S1

Beginning at the final `بِٱلصَّبْرِ` reopens not only self-restraint but its changed-controller field: compelled confinement, guarantee, sides, hard matter, no exit, cold, bitter extract, fruit, cloud layers, food heap, requital, named group/mountain, and sealed container. Exact `عصارة` then returns backward into pressing/product tuples under `ع ص ر`; exact `حبس` returns into withholding and enclosure; exact `السحاب` returns into rain. These contacts do not convert the final content occupant into any lexical material.

The second `تَوَاصَوْا` returns to the first through exact form and reciprocal topology; moving backward changes content from restraint to truth while holding controller and grammar fixed. `بِٱلْحَقِّ` then opens opposition, matching, obligation, owned claim, dispute, verification, defense, thresholds, penetration, fabric/speech solidity, receptacles, severe movement, completed fatness, and hoof alignment. Its exact occurrence inside the faith assertion reopens the earlier `ءَامَنُوا`, but only as a content-schema relation.

`ٱلصَّٰلِحَٰتِ` backward-binds to `عَمِلُوا` by direct object and to `الأعمال الصالحة والسيئة` by exact source relation. Repair, reconciliation, suitability, and names remain adjacent form constellations, not occupants. `ءَامَنُوا` then returns through `النفس` to self-restraint and self-reference, through `التصديق` to verification, and through security to removal of fear. The exception controller remains the same surface group throughout these backward reopenings.

Crossing into S2, the surface group is not collapsed into `ٱلْإِنسَٰنَ`. The singular participant remains in its exact predicated loss state. Backward contact from human form opens appearance, sensory detection, proximity, facing side, eye-image, and self-address; from loss it opens decrease, commerce, deficient measure, and the measurement-vacancy comparison. Neither field supplies an occupancy bridge into S3.

Returning finally to `وَٱلْعَصْرِ`, the passage-ending `صبر` has already reactivated `عصارة` and `حبس`, while `حق` has reactivated completion and matching, and `تواصى` has reactivated connection across night/day and thing/thing. Those later exact relations now meet the first form's pressing, confinement, refuge, temporal pairs, rain, origin, gift, and enclosure tuples. The return remains a many-node activation: the one-word beginning receives form and coalition links from later positions, but no later participant, state, content, or event occupant is transported into it.

