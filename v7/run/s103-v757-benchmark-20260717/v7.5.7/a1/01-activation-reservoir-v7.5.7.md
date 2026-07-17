# Activation Reservoir: S103, V7.5.7

This is a formation field, not a governing reading. All coordinates, forms,
operations, and candidate edges below remain typed; formal contact does not make
two carriers semantically identical, and repeated generic participants do not
become one discourse entity.

## Positioned surface lattice

### Exact three-line object

```text
L1 / 103:1  وَٱلْعَصْرِ
L2 / 103:2  إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ
L3 / 103:3  إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَتَوَاصَوْا۟ بِٱلْحَقِّ وَتَوَاصَوْا۟ بِٱلصَّبْرِ
```

The passage has **3 ordered lines**, **14 orthographic words**, and **30 supplied
morphology rows**. The morphology distribution is L1 = 1 word / 3 morphemes,
L2 = 4 words / 6 morphemes, and L3 = 9 words / 21 morphemes. The supplied
syntax graph has **11 edges**: 1 for L1, 3 for L2, and 7 for L3.

Two levels of complete construction are retained rather than flattened into one
clause count:

- Three top-level line constructions: the oath particle-complement in L1; the
  `إِنَّ` nominal predication in L2; and the exception-plus-relative-group scope
  in L3.
- Inside the L3 relative group, four ordered predicate carriers: P1
  `ءَامَنُوا۟`; P2 `وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ`; P3
  `وَتَوَاصَوْا۟ بِٱلْحَقِّ`; P4 `وَتَوَاصَوْا۟ بِٱلصَّبْرِ`. P1-P4 share the
  relative-group referent through surface coordination, but each retains its
  own operation, complement structure, and outgoing state.

### Orthographic-word and morpheme coordinates

| Coordinate | Exact carrier | Supplied segmentation and features | Local port kept open |
|---|---|---|---|
| L1.W1, only/1st | `وَٱلْعَصْرِ` | `وَ` P prefix + `ٱلْ` DET + `عَصْرِ`; lemma `عَصْر`, root `ع ص ر`, N, M, GEN | oath particle/controller distinct from the governed definite time/other homographic noun carrier |
| L2.W1, 1st/4 | `إِنَّ` | lemma `إِنّ`, ACC particle | grammatical head; takes an ism and a khabar predication, no semantic human occupant |
| L2.W2, 2nd/4 | `ٱلْإِنسَٰنَ` | `ٱلْ` DET + `إِنسَٰنَ`; lemma `إِنسَٰن`, root `ء ن س`, N, M, ACC | governed ism; continuous singular surface referent remains distinct from later plural controllers |
| L2.W3, 3rd/4 | `لَفِى` | `لَ` EMPH prefix + `فِى` preposition | emphasis and containment/government are separate relations; neither is an entity handoff |
| L2.W4, 4th/4 | `خُسْرٍ` | lemma `خُسْر`, root `خ س ر`, N, M, INDEF, GEN | prepositional complement and khabar content; affected participant supplied by the L2 predication |
| L3.W1, 1st/9 | `إِلَّا` | lemma `إِلَّا`, EXP | exception operator; opens a scoped contrast but is not a member of the group |
| L3.W2, 2nd/9 | `ٱلَّذِينَ` | lemma `ٱلَّذِى`, REL, MP | excepted plural relative group; referential endpoint for P1-P4 |
| L3.W3, 3rd/9 | `ءَامَنُوا۟` | `ءَامَنُ` V, PERF, form IV, root `ء م ن`, 3MP + suffix `وا۟` PRON:3MP | 3MP grammatical controller and semantic initiator; voice field is not supplied |
| L3.W4, 4th/9 | `وَعَمِلُوا۟` | `وَ` CONJ + `عَمِلُ` V, PERF, root `ع م ل`, 3MP + suffix `وا۟` PRON:3MP | same group occurrence by coordination; action has a separately bound explicit object |
| L3.W5, 5th/9 | `ٱلصَّٰلِحَٰتِ` | `ٱل` DET + `صَّٰلِحَٰتِ`; lemma `صَّٰلِحَٰت`, root `ص ل ح`, N, ACT PCPL, FP, ACC | definite feminine-plural direct object of P2; not the controller of P2 |
| L3.W6, 6th/9 | `وَتَوَاصَوْا۟` | `وَ` CONJ + `تَوَاصَ` V, PERF, form VI, root `و ص ي`, 3MP + suffix `وْا۟` PRON:3MP | reciprocal group operation; member-as-source and member-as-recipient ports remain internally rotated |
| L3.W7, 7th/9 | `بِٱلْحَقِّ` | `بِ` P + `ٱلْ` DET + `حَقِّ`; lemma `حَقّ`, root `ح ق ق`, N, M, GEN | governed content complement of P3; transported content is `الحق`, not the participants themselves |
| L3.W8, 8th/9 | `وَتَوَاصَوْا۟` | same three supplied morphemes and features as L3.W6 | a second event carrier with the same group occurrence and topology, not a duplicate token collapsed into P3 |
| L3.W9, 9th/9 | `بِٱلصَّبْرِ` | `بِ` P + `ٱل` DET + `صَّبْرِ`; lemma `صَبْر`, root `ص ب ر`, N, M, GEN | governed content complement of P4; distinct payload from L3.W7 |

The four perfect predicates are all 3MP, but that feature does not merge their
actions, objects, contents, or resulting states. The two `تَوَاصَ + وْا۟`
tokens are exact morphological recurrences and separate positioned events. The
two preceding perfect verbs have the suffix written `وا۟`; the two form-VI
verbs have the suffix written `وْا۟`. After removal of vocalization these suffix
forms meet, while their exact supplied writing remains visible.

### Supplied syntax as participant structure

The syntax file's `q:` coordinates are retained exactly and are not silently
renumbered into the nine orthographic positions of L3.

| Syntax edge | Exact span | Relation and typed consequence |
|---|---|---|
| `ae:v3:s103:001:pass1:attach:a1` | `q:103:1:1 -> q:103:1:2`, `وَالْعَصْرِ \| وَالْعَصْرِ` | `particle_complement`: oath `وَ` governs `ٱلْعَصْرِ`; grammatical governor and governed oath object stay separate |
| `...002...a1` | `q:103:2:1 -> q:103:2:2`, `إِنَّ \| الْإِنْسَانَ` | `particle_complement`: `ٱلْإِنسَٰنَ` is the governed ism of `إِنَّ` |
| `...002...a2` | `q:103:2:1 -> q:103:2:4`, `إِنَّ \| خُسْرٍ` | `prep_complement`: the supplied evidence places `خُسْرٍ` under `فِى` inside the khabar |
| `...002...a3` | same graph endpoints, `إِنَّ \| خُسْرٍ` | `predication`: `لَفِى خُسْرٍ` supplies the khabar predication; L2.W2 is its affected/referential subject, not its grammatical head |
| `...003...a1` | `q:103:3:1 -> q:103:3:2`, `إِلَّا \| الَّذِينَ` | `exception`: the excepted group is `ٱلَّذِينَ`, with P1 through P4 completing scope |
| `...003...a2` | `q:103:3:3 -> q:103:3:5`, `آمَنُوا \| وَعَمِلُوا` | `conjoined`: P2 follows P1 under the same relative-group occurrence |
| `...003...a3` | `q:103:3:5 -> q:103:3:6`, `وَعَمِلُوا \| الصَّالِحَاتِ` | `direct_object`: P2 controller/initiator acts on the explicit FP ACC object |
| `...003...a4` | `q:103:3:5 -> q:103:3:8`, `وَعَمِلُوا \| وَتَوَاصَوْا` | `conjoined`: P3 is coordinated after P2; no object or result is transported merely by coordination |
| `...003...a5` | `q:103:3:8 -> q:103:3:9`, `وَتَوَاصَوْا \| بِالْحَقِّ` | `prep_complement`: `الحق` is P3's content complement |
| `...003...a6` | `q:103:3:8 -> q:103:3:11`, `وَتَوَاصَوْا \| وَتَوَاصَوْا` | `conjoined`: P4 repeats the reciprocal operation at a later position |
| `...003...a7` | `q:103:3:11 -> q:103:3:12`, `وَتَوَاصَوْا \| بِالصَّبْرِ` | `prep_complement`: `الصبر` is P4's content complement |

Surface bindings available now: L2 ism-to-khabar predication; L3 exception
scope; identity of the one relative-group occurrence across P1-P4; P2-to-object;
P3-to-truth-content; P4-to-patience-content; and the coordination order
P1 -> P2 -> P3 -> P4. Surface binding does not equate L2's singular
`ٱلْإِنسَٰنَ` with L3's plural `ٱلَّذِينَ`, even though the exception structure
places their scopes in an explicit contrast.

### Repetition, boundaries, and differing local roles

- Passage beginnings, in order: L1 `وَـ`; L2 `إِنَّ`; L3 `إِلَّا`. L2 and L3
  both open with exact written `إِـ`, then diverge into an accusative particle
  and an exception particle. L1's initial `وَ` is tagged P and licensed as an
  oath particle; the three later exact `وَ` prefixes at L3.W4, W6, and W8 are
  tagged CONJ. Exact form recurs while grammatical operation changes.
- Passage endings, in order: `عَصْرِ` / `خُسْرٍ` / `صَّبْرِ`. All three are
  masculine genitive nouns and all end in consonant `ر`. L1 and L3 return the
  exact vocalized ending `رِ`; L2 has indefinite `رٍ`. L1 and L3 are definite
  through `ٱل`, while L2 remains indefinite. The grammatical causes also
  differ: oath government in L1, prepositional khabar containment in L2, and
  content-complement government in L3.
- The full boundary sequence is therefore not reduced to the adjacent pairs:
  `[definite M GEN / رِ] -> [indefinite M GEN / رٍ] -> [definite M GEN / رِ]`.
  Its roots remain three typed nodes: `ع ص ر -> خ س ر -> ص ب ر`.
- `ٱلْ` is supplied exactly at L1.W1, L2.W2, and L3.W7; `ٱل` without the
  written sukūn is supplied at L3.W5 and L3.W9. Definite morphology recurs five
  times without erasing the different nouns or syntactic functions.
- `بِ` recurs exactly at L3.W7 and L3.W9. Both introduce a definite masculine
  genitive content, and their heads are the two separately positioned
  `تَوَاصَوْا۟` events.
- `تَوَاصَ` recurs twice, `وْا۟` recurs twice, and the entire surface token
  `وَتَوَاصَوْا۟` recurs twice. The first occurrence is P3/6th word and receives
  `الحق`; the second is P4/8th word and receives `الصبر`.
- Four perfect 3MP predicates fill successive relative-group positions. Their
  argument patterns differ: P1 has no surface complement; P2 has a direct
  object; P3 and P4 have prepositional content complements. Shared person,
  number, aspect, and referent preserve continuity of the group but do not
  carry one predicate's complement into another.
- Consonant `ص` occurs in the L1 boundary noun and returns in L3.W5 and L3.W9;
  consonant `ر` closes every line. These are positioned form contacts only.

## Exact-contact closure

For detection, vocalization, Qur'anic small signs, and ordinary written
decoration are set aside while ordered Arabic letters are compared in both
containment directions. The recorded node always restores the exact supplied
writing, its vowels or declared pronunciation, its affixes, and its local
relation. Hamza/alif shapes, feminine endings, and other actual letter
differences are not silently repaired into identities.

### Recovered surface terms

The morphology licenses these full-form/base/affix nodes before any semantic
expansion:

```text
وَٱلْعَصْرِ = وَ [oath P] + ٱلْ [DET] + عَصْرِ [GEN]
ٱلْإِنسَٰنَ = ٱلْ [DET] + إِنسَٰنَ [ACC], lemma إِنسَٰن
لَفِى = لَ [EMPH] + فِى [P]
ءَامَنُوا۟ = ءَامَنُ [form-IV PERF 3MP stem] + وا۟ [3MP]
وَعَمِلُوا۟ = وَ [CONJ] + عَمِلُ [PERF 3MP stem] + وا۟ [3MP]
ٱلصَّٰلِحَٰتِ = ٱل [DET] + صَّٰلِحَٰتِ [FP ACC active participle]
وَتَوَاصَوْا۟ = وَ [CONJ] + تَوَاصَ [form-VI PERF 3MP stem] + وْا۟ [3MP]
بِٱلْحَقِّ = بِ [P] + ٱلْ [DET] + حَقِّ [GEN], lemma حَقّ
بِٱلصَّبْرِ = بِ [P] + ٱل [DET] + صَّبْرِ [GEN], lemma صَبْر
```

The two attached content forms re-enter closure as `بِـ + ٱلحق` and
`بِـ + ٱلصبر`; the preposition is not part of either content entity. Likewise,
the plural endings of all four verbs remain explicit and the recovered stems do
not turn distinct inflected forms into one event.

### Surface trigger: `وَٱلْعَصْرِ`

`عَصْرِ`/lemma `عَصْر` meets every explicitly supplied `العصر` carrier while
keeping its branch-local relation:

- `العصر الدهر`; `العصران الليل والنهار`; `العصران الغداة والعشي`;
  `العصر العشي`; `صلاة العصر`; `العصار الحين`; delayed coming `جاءني فلان
  عصرا أي بطيئا`; and `نام وما نام لعصر` (ع ص ر B001).
- `العصر مصدر عصرت` and the pressing lineage in which a thing is pressed until
  it releases liquid, with `العصارة ما سال عن العصر` and `كل شيء عصر ماؤه فهو
  عصير` (ع ص ر B002).
- `العصر الملجأ`, `العصر المنجاة`, and the attached refuge/holding forms
  `العصرة والمعتصر والمعصر` (ع ص ر B005).
- Exact equations `العصر الحبس` (B006) and `العصر العطية` (B007). These two
  source assertions remain opposed local relations; their common surface form
  does not merge withholding and giving.

Derived carriers containing the supplied ordered letters return to the same
field: `عصرت`, `اعتصرته`, `يعصرون`, `العصارة`, `العصير`, `المعصرة`,
`المعصار`, `المعصرات`, `الإعصار`, `اعتصرت`, `تعصرت`, `المعتصر`,
`المعصور`. `العنصر` is not treated as a manufactured substring derivation;
its contact is instead explicitly licensed by B011's assertion `مما زيدت فيه
النون وهو في الأصل العصر وهو الملجأ`, which preserves `العنصر`, added `ن`,
base `العصر`, and the asserted refuge relation.

### Surface trigger: `ٱلْإِنسَٰنَ`

- The shorter explicitly supplied form `الإنس` occurs in the longer surface
  carrier `الإنسان` after decorative stripping. It brings its complete local
  assertions: `الإنس خلاف الجن وسموا لظهورهم`; `الإنس البشر والواحد إنسي
  والجمع أناسي`; `الإنس جماعة الناس والأناسي جماع` (ء ن س B001). The embedded
  contact does not by itself make every `إنس`, `إنسي`, or `أناسي` occurrence the
  same participant as L2.W2.
- The exact full expression `إنسان العين` returns in B005: `إنسان العين صبيها
  الذي في السواد`; `إنسان العين المثال الذي يرى في السواد أي سواد العين`;
  `الإنسان أيضا إنسان العين وجمعه أناسي والإنسان الأنملة`. The L2 surface
  person, the seen image, and the fingertip remain different entity types even
  while the same supplied word carries them.
- Explicit `إنسي` carriers orient sides toward a human, rider, or archer (B004),
  and `ابن إنسك` is explicitly used for the self/intimate (B006). These reopen
  orientation and self-reference ports around the containing surface form.
- `أنس`/`الأنس` and `آنس` carriers are retained with their supplied hamza and
  vocalic differences: sensory seeing/hearing/knowing (B002) and removal of
  estrangement through nearness or companionship (B003). Ordered consonantal
  contact with `إِنسَٰن` is formal; it does not erase these declared operations.

### Surface trigger: `خُسْرٍ`

The inflected surface form recovers lemma `خُسْر` and meets the exact source
forms `الخسر`, `خسر`, `خسرا`, and `خسرانا`:

- `أصل واحد يدل على النقض`; `الخسر النقصان والخسران كذلك`; `خسر إذا نقص
  ميزانا أو غيره` (خ س ر B001).
- Trade lineage: `الخاسر الذي وضع في تجارته`; `خسر التاجر إذا وضع من رأس
  ماله`; `خسر في البيع خسرا وخسرانا`; `انتقاص رأس المال`; `صفقة خاسرة أي غير
  مربحة` (B002).
- Measure lineage: `خسرت الميزان وأخسرته إذا نقصته`; `كلته ووزنته فأخسرته`;
  `خسرت الشيء وأخسرته نقصته`; `ولا تخسروا الميزان`; `ينقصون في الكيل والوزن`
  (B003).
- The longer explicitly supplied forms `خنسرى`, `خيسرى`, `الخناسر`, and
  `الخناسير` retain the declared added `ن` or `ي`, their positions in loss,
  destruction, meanness, or weakness, and the assertion `الخناسير الهلاك لا
  واحد له` (B005). No arbitrary shorter substring is coined from them.

### Surface trigger: `ءَامَنُوا۟`

The morphology supplies the exact recoverable form-IV stem `ءَامَنُ`, lemma
`ءَامَنَ`, root `ء م ن`, and suffix `وا۟`. It meets, without collapsing,
security `أمن/آمن`, assent `الإيمان/مؤمن`, and prayer-response `آمين` carriers:

- B001 keeps `الأمن ضد الخوف`, `أصل الأمن طمأنينة النفس وزوال الخوف`,
  `الأمانة ضد الخيانة ومعناها سكون القلب`, `الأمان إعطاء الأمنة`, the state
  transition `أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن`, entry `استأمن إليه دخل
  في أمانه`, place `مأمنه منزله الذي فيه أمنه`, and the trustworthy/she-camel
  carrier `الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها`.
- B002 keeps the exact identities and participant arrangements `الإيمان
  التصديق`; `وما أنت بمؤمن لنا أي مصدق لنا`; `إذعان النفس للحق على سبيل
  التصديق`; and `المؤمن في صفات الله يصدق ما وعد عبده`.
- B003 keeps `قولنا في الدعاء آمين وتفسيره اللهم افعل`; `التأمين من قولك
  آمين`; the declared length alternatives `آمين في الدعاء يمد ويقصر` and
  `آمين يقال بالمد والقصر`; and the asserted outcomes `كذلك فليكن`, `استجب`,
  and `أمن فلان إذا قال آمين`.

The phrase `إذعان النفس للحق على سبيل التصديق` releases the attached term
`للحق = لـ + الحق`. The full attached source form and its `لـ` direction differ
from surface `بِٱلْحَقِّ = بِـ + الحق`; recovered `الحق` is an exact shared term
and re-enters every truth carrier below.

### Surface triggers: `عَمِلُوا۟` and `ٱلصَّٰلِحَٰتِ`

- Surface `عَمِلُ + وا۟` meets `عمل عملا فهو عامل`, `كل فعل يكون من الحيوان
  بقصد`, and the exact cross-word phrase `الأعمال الصالحة والسيئة` (ع م ل
  B001). The action's agent, intent, act, and good/bad qualification remain
  separate ports.
- Surface `الصالحات` meets the explicitly supplied base form `صالح` and the
  action-quality assertions `الصلاح ضد الفساد`, `الإصلاح نقيض الإفساد`, and
  the statement that `الصلاح` and `الفساد` are mostly used of acts (ص ل ح
  B001). The feminine plural accusative passage object is retained against the
  singular masculine adjective/name forms; containment does not import the
  named person of B004.
- The complete lexical phrase `الأعمال الصالحة والسيئة` collides with the
  adjacent surface construction `عَمِلُوا۟ ٱلصَّٰلِحَٰتِ`: `عمل` returns in
  the verb, and `الصالحة`/`صالح` returns inside the plural object's supplied
  root/form family. Surface syntax independently binds the verb to that object.
- The recommendation assertion `التقدم إلى الغير بما يعمل به مقترنا بوعظ`
  (و ص ي B002) contains inflected `يعمل`; recoverable lexical base `عمل`, prefix
  `يـ`, and attached `به = بـ + هـ` are held together. This opens a formal and
  operational contact from recommendation content to the later surface work
  carrier without declaring that every recommendation is the performed act.

### Surface triggers: the two `وَتَوَاصَوْا۟`

The full tokens, form-VI stems, 3MP endings, and positions recur exactly. Their
lexical source assertions provide the reciprocal topology:

```text
تواصى القوم إذا تواصلوا
تواصى القوم أي أوصى بعضهم بعضا
تواصى القوم إذا أوصى بعضهم إلى بعض
```

The supplied surface group can therefore occupy the local lexical ports
member-A as recommender -> content -> member-B and member-B as recommender ->
content -> member-A. The 3MP group is both distributed initiator and distributed
recipient, not a single fused participant. P3 and P4 instantiate this topology
separately with `الحق` and `الصبر`.

The smaller relation remains attached to its larger source family:

- `أصل يدل على وصل شيء بشيء`; `ووصيت الشيء وصلته`; `وصيت الليلة باليوم
  وصلتها`; plant, ground, and open-land continuity; and `وصى الشيء يصي إذا اتصل
  ووصاه غيره وصله` (و ص ي B001).
- `الوصية ... كأنه كلام يوصى أي يوصل`; `وصيته توصية وأوصيته إيصاء`;
  `الوصية بعد الموت`; `الوصية ما أوصيت به`; assigning another as executor in
  `أوصيت له بشئ وأوصيت إليه إذا جعلته وصيك`; reversible lexical role naming in
  `الوصي الموصي والموصى إليه جميعا`; and advance-to-another plus admonition in
  `التقدم إلى الغير بما يعمل به مقترنا بوعظ` (B002).
- `وصى لها المرتع` keeps a separate fit topology: pasture as grammatical
  initiator/condition, grazing animals as beneficiary/affected participant, and
  ease as outcome in `إذا أطاع المرعى للسائمة فأصابته رغدا قيل وصى لها المرتع
  يصي وصيا` (B004).

`وصى`, `أوصى`, `الوصي`, `تواصى`, `تواصلوا`, and `وصل` stay typed as distinct
forms. The lexical identity of `الوصي` as both `الموصي` and `الموصى إليه` is an
explicit named role relation; it does not make every source and recipient in
the passage numerically one.

### Surface trigger: `بِٱلْحَقِّ`

Attached surface `بِـ + ٱلْ + حَقِّ` recovers exact term `الحق`. Its source
utterances remain separate complete carriers:

- opposition/matching: `الحق نقيض الباطل`; `أصل الحق المطابقة والموافقة`;
  verification into certainty; `الحقيقة خلاف المجاز` (ح ق ق B001).
- obligation: `حق الشيء وجب`; `حقيق بكذا ومحقوق به`; causing obligation and
  deserving it; use as required/necessary/permissible (B002).
- possessed claim: `إنك لتعرف الحقة عليك`; `الحق واحد الحقوق والحقة أخص منه،
  هذه حقتي أي حقي`; buyer-directed ownership `استحقها على المشتري أي ملكها
  عليه`; `وبعولتهن أحق بردهن` (B003).
- reciprocal dispute: each side claims truth with itself; contest, mutual
  contest, and overcoming in `حاققته فحققته أي خاصمته في الحق فغلبته` (B004).
- establishing/showing: certainty, confirming an utterance or supposition,
  saying a thing is truth, establishing/judging it truth, and `ليحق الحق` (B005).
- protected obligation: the standard, inviolability, precinct, or other thing
  a person must protect and defend in `الحقيقة ما يحق على الرجل أن يحميه`
  (B007).
- attained capacity: the camel reaching the year/state that makes carrying or
  riding due; time of mating (B008), and the camel/property reaching full
  fatness (B013).
- penetration: a thrust that reaches the interior, has no deviation, and has
  penetrated, contrasted locally with a wound that does not penetrate (B009).
- tight construction: tightly woven cloth, weighty speech, and making a matter
  firm/correct (B010).
- fitted joint/container/center: meeting of bones, wooden or ivory receptacle,
  hip joint, door fitting in its socket, crown of the head, middle of winter,
  and spider web (B011).
- exhausting intensity in travel, including making a weak bearer carry what it
  cannot endure (B012).
- hoof-placement/condition: a horse that does not sweat, places hind hoof where
  fore hoof was, or becomes lean (B014).

The repeated letters `حق` and longer `حقة`, `حقيق`, `محقوق`, `استحق`,
`احتق`, `حقق`, `أحق`, `حاق` return to closure while each affix, participant
structure, direction, state, and scale remains present.

### Surface trigger: `بِٱلصَّبْرِ`

Attached surface `بِـ + ٱل + صَّبْرِ` recovers `الصبر`. All explicit homographic
and derived carriers remain active:

- `الصبر نقيض الجزع`; `الصبر حبس النفس عن الجزع`; `صبرت نفسي أي حبستها`;
  `حبس النفس على ما يقتضيه العقل والشرع` (ص ب ر B001).
- coercive holding: a living being held for death or shooting, a person set up
  for killing, a compelled oath, and `الصبر الإكراه` (B002).
- guarantee/attendance: `الصبير هو الكفيل`; `صبرت بفلان إذا كفلت به فأنا به
  صبير`; a group's `صبير` remaining with them in their affairs (B003).
- upper edge/sides: top of anything, sides of vessel and grave, and side of a
  thing (B004).
- hard matter/terrain: thick hard stones, gravelly ground, and `أم صبار` as lava
  field or thick rock (B005).
- inescapable severity: war, calamity, a great/severe matter, and `أم صبور أمر
  لا منفذ له عنه` (B006).
- severe winter cold in `صبارة الشتاء` (B007).
- declared pronunciation branch: `الصبر بكسر الباء عصارة شجرة` and `الصبر هذا
  الدواء المر` (B008). The source explicitly gives kasra on `ب`; the passage
  writes sukūn in `صَّبْرِ`. Consonantal closure activates the collision while
  preserving that vocalic difference.
- sour tree fruit / tamarind `الصبار` (B009); level white or layered cloud
  `الصبر/الصبير` (B010); broad table sheet and piled/unmeasured food `صبير
  الخوان` / `الصبرة` (B011); retaliation and execution under requital
  `فليصطبر` / `أصبره` (B012); a named clan `الصبر ... بطن من غسان` (B016);
  mountain and its middle `الصبير` (B017); and bottle stopper/seal `الصبار`
  (B018).

These carriers do not turn P4's content into a stone, cloud, medicine, clan,
mountain, or stopper. Each exact formal collision opens the complete local
relation for enactment against the positioned passage carrier while preserving
pronunciation, scale, and entity type.

## Source-to-source exact circuits

Every circuit below begins at an explicitly supplied form or proposition. A
recurrent word transports its written form and source position; only an
identity, definition, equation, participant continuity, or complete topology
explicitly supplied can transport more.

### `النفس` and its attached forms

```text
ء م ن B001  أصل الأمن طمأنينة النفس وزوال الخوف
ء م ن B002  إذعان النفس للحق على سبيل التصديق
ص ب ر B001  الصبر حبس النفس عن الجزع
ص ب ر B001  صبرت نفسي أي حبستها
ء ن س B006  قيل ابن إنسك للنفس
ء ن س B006  كيف ابن إنسك ... نفسه
ع ص ر B009  إذا رأت في نفسها زيادة الشباب ...
```

Closure retains `النفس`, `نفسي = نفس + ي`, `نفسه = نفس + ه`, and
`نفسها = نفس + ها`. The first three complete relations expose differing state
transitions around the نفس: fear -> calm, truth-addressed assent -> assent, and
impulse toward distress -> held from distress. B006 supplies a named
self-reference equation; B009 supplies self-perception during a biological
transition. Shared `نفس` is not a global occupant. When P1 and P4 are enacted
for the same relative-group occurrence, the group-member self is a constrained
possible binder for the assent and restraint ports; its identity comes from the
surface controller, not from the generic word alone.

### `الحق` across assent, content, matching, and claim

```text
surface P3   بِٱلْحَقِّ: content complement of first تواصوا
ء م ن B002   إذعان النفس للحق على سبيل التصديق
ح ق ق B001   الحق نقيض الباطل
ح ق ق B001   أصل الحق المطابقة والموافقة
ح ق ق B004   ... ادعى كل واحد أن الحق معه
ح ق ق B005   حقق الرجل إذا قال هذا الشيء هو الحق
ح ق ق B005   أحققت كذا أي أثبته حقا أو حكمت بكونه حقا، ليحق الحق
```

The affixed nodes are separately recoverable: `للحق = لـ + الحق`, surface
`بالحق = بـ + الحق`, and `في الحق = في + الحق`. Exact term recurrence lets the
complete assent assertion and every `حق` definition meet the surface content
node. It does not turn the reciprocal recommenders into disputants, judges, or
claim-owners. Those remain alternate local enactments around the same supplied
term.

### `عمل` / `صالح` / what is to be acted upon

```text
surface P2                عَمِلُوا۟ ٱلصَّٰلِحَٰتِ
ع م ل B001                الأعمال الصالحة والسيئة
ص ل ح B001 what_is_ar     صلاح الشيء والرجل والعمل
ص ل ح B001                الصلاح ضد الفساد ... مختصان ... بالأفعال
و ص ي B002                التقدم إلى الغير بما يعمل به مقترنا بوعظ
```

`عمل` is explicit as a passage lemma, an uninflected source form, and the base
within `يعمل = يـ + عمل`. `صالح` is explicit inside the supplied plural/derived
family and in `الأعمال الصالحة`. The surface direct-object edge gives a binding
independent of the lexical collision. The وصي assertion supplies an addressee,
content that is to be acted on, and accompanying admonition; it opens a content
handoff toward an act only when the content occurrence itself is maintained.

### `الليل`, `الليلة`, and `اليوم`

```text
ع ص ر B001  العصران الليل والنهار
ع ص ر B001  what_is_ar: الدهر والحين واليوم والليلة
و ص ي B001  وصيت الليلة باليوم وصلتها
```

`الليل` is an explicitly supplied shorter form inside `الليلة`; the latter
retains feminine `ة`. `باليوم` releases `بـ + اليوم`. The complete وصي source
assertion directs one temporal carrier, `الليلة`, into connection with another,
`اليوم`, and explicitly predicates `وصلتها`. The `عصر` source independently
names paired temporal extents. Thus the surface first word can open a time-pair
tuple while the later surface `تواصوا` opens a connecting operation. This is a
closed formal-and-source circuit; it does not assert that the oath carrier is
only one member of either pair.

### `الحبس` / `حبس` / `تحبس`

```text
ع ص ر B006  العصر الحبس
ع ص ر B006  يمنعه إياه ويحبسه عنه
ع ص ر B009  تحبس في البيت يجعل لها عصرا
ص ب ر B001  الصبر حبس النفس عن الجزع
ص ب ر B002  المصبورة المحبوسة على الموت
```

The exact equation `العصر الحبس` and exact definition `الصبر حبس النفس عن
الجزع` place both boundary words against a supplied holding relation. The local
topologies remain unlike: generic noun identity; a parent withholding property
from a child; a girl confined in a house; self-restraint with self as affected
participant; and coercive restraint of a living being toward death. Complete
topology replay may align holder/held/boundary/outgoing state while retaining
agency, consent, scale, and outcome.

### `العصارة`

```text
ع ص ر B002  العصارة ما سال عن العصر
ع ص ر B002  العصارة ما تحلب من شيء تعصره
ع ص ر B007  العصارة الغلة
ص ب ر B008  الصبر بكسر الباء عصارة شجرة
```

This is an exact cross-root source circuit. B008 states an identity using
`الصبر` with declared kasrat al-bāʾ as a term and `عصارة شجرة` as the other.
B002 supplies the source-to-product lineage: pressed thing -> pressing -> that
which flows/is drawn out -> `العصارة`; B007 supplies `العصارة = الغلة`. The
passage writes `صَّبْرِ` with sukūn, so the contact is consonantal/orthographic
after vocalization is set aside, not a collapse of readings. Full form, declared
vowel, tree source, pressing source, and product remain typed.

### `السحاب` / `السحائب`

```text
ع ص ر B003  المعصرات السحائب تعتصر بالمطر
ع ص ر B003  المعصرات سحائب تجيء بمطر
ع ص ر B003  السحابة المعصر التي تتحلب بالمطر
ص ب ر B010  الصبر سحاب مستو فوق السحاب الكثيف
ص ب ر B010  الصبير السحاب الأبيض
ص ب ر B010  السحاب الأبيض الذي يصبر بعضه فوق بعض درجا
ص ب ر B010  الاصبار السحائب البيض
```

Exact cloud terms recur; there is no evidence that any two generic cloud
mentions denote one cloud instance. Topology replay can preserve, on one side,
cloud as a rain-bearing/releasing medium and, on the other, cloud layers held
one above another. The shared medium class and explicit `تحلب` also recontacts
the liquid-extraction assertion under `عصر`, but carries no rain into a pressed
grape or tree extract.

### `الوزن` and `الكيل`

```text
خ س ر B003  ينقصون في الكيل والوزن
خ س ر B003  كلته ووزنته فأخسرته أي نقصته
ص ب ر B011  اشتريت الشيء صبرة أي بلا وزن ولا كيل
ص ل ح B005  وصلاح في وزن حذام وقطام وهو اسم مكة
```

The first two carriers provide measured quantity -> diminution. The food-pile
carrier provides purchase of a pile specifically without weight or measure.
The place-name assertion uses `وزن` as morphological pattern, a distinct scale
and payload. Exact form recurrence does not send a commercial quantity into a
name pattern. The first two topologies can be aligned as
commodity / measuring regime / transaction / quantity-state, with polarity
`diminished under measure` versus `transacted without measure` retained.

### `العين` and seeing instruments

```text
ء ن س B005  إنسان العين المثال الذي يرى في السواد أي سواد العين
ء ن س B002  آنست الشيء إذا رأيته ... آنسته أبصرته
ع م ل B010  وترقبه بعاملة قذوف أي ترقبه بعين بعيدة النظر
```

`بعين` recovers `بـ + عين`; `عينه` in the branch description recovers
`عين + ه`. The first assertion places a visible human-image carrier in the dark
part of the eye; the second supplies perceiver -> seeing -> perceived object;
the third names the far-seeing eye `عاملة` within its cited arrangement. This
creates a formal circuit from surface `الإنسان` to `إنسان العين` and from
surface `عملوا` to `عاملة`, while keeping the visible image, perceiver, eye,
watcher, and work-agent as distinct ports.

### `الناقة`, `الدابة`, and `الفرس`

Exact animal terms produce complete topology replays, not entity handoffs:

- `الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها` (ء م ن B001):
  a she-camel characterized by trust/security concerning slackening or stumbling.
- `الحقة ... ما استحق أن يحمل عليه`, entry into the fourth year, time of
  mating, and a she-camel reaching fatness (ح ق ق B008/B013): attained state ->
  licensed capacity or condition.
- `اليعملة الناقة النجيبة المطبوعة على العمل` and `ناقة عملة ... فارهة`
  (ع م ل B008): animal disposition -> work-readiness.
- `إنسي الدابة` is the side facing the rider (ء ن س B004); `عوامل الدابة
  قوائمه` (ع م ل B010); and `أصلحت إلى الدابة أحسنت إليها` (ص ل ح B001).
  Facing side, working limbs, and beneficiary-of-kindness are different ports.
- `الأحق من الخيل` places hoof in the earlier hoof-position or does not sweat,
  while `احتق الفرس أي ضمر` (ح ق ق B014); `عاملة الفرس ... عينه` (ع م ل B010).
  Position, bodily condition, and visual organ remain separate.

### `المطابقة`, `الموافقة`, and fit

```text
ح ق ق B001  أصل الحق المطابقة والموافقة
ح ق ق B011  مطابقة رجل الباب في حقه
ح ق ق B014  الأحق أن يطبق هذا ذاك / يضع رجله في موضع يده
ص ل ح B003  وهذا الشئ يصلح لك، أي هو من بابتك
و ص ي B004 what_is_ar  وافق المرعى السائمة فأصابتها رغدا
```

Complete fit tuples expose item-A, item-B/slot, correspondence, direction, and
outcome. Door-part to socket, hind hoof to fore-hoof position, thing to person's
domain, and pasture to grazing animal have different occupants and scales.
Topology replay aligns the correspondence only; it neither makes the truth
content a door fitting nor hands one local object to another scene.

### `وصلت` and route completion

```text
و ص ي B001  ووصيت الشيء وصلته
و ص ي B001  وصيت الليلة باليوم وصلتها
ح ق ق B009  طعنة محتقة إذا وصلت إلى الجوف
```

The exact inflected form `وصلت` occurs in connection and penetration
assertions. One endpoint is another thing/time period; the other endpoint is
the interior of a body. Route, force, affected material, and outcome differ.
Only the abstract supplied topology origin -> traversal/contact -> endpoint can
replay; no wound participant enters the temporal or recommendation relation.

### `بعض ... بعض`

```text
و ص ي B003  أوصى بعضهم بعضا / أوصى بعضهم إلى بعض
ص ب ر B010  السحاب الأبيض الذي يصبر بعضه فوق بعض درجا
ص ب ر B011  الصبرة من الطعام بعضه فوق بعض
```

The exact distributed pair `بعض ... بعض` recurs. In recommendation it rotates
source and recipient among group members; in the cloud and food carriers it
orders material parts vertically, one above another. Reciprocal horizontal role
rotation and vertical stacking are not merged. The ordered-pair form itself
remains a seed, especially beside the two surface occurrences of `تواصوا`.

### `الشتاء`, `رأس`, and `الوسط`

- `جئته في حاق الشتاء` (ح ق ق B011) and `صبارة الشتاء شدة برده` / `أتيته في
  صبارة الشتاء` (ص ب ر B007) share exact `الشتاء`. Middle/heart of a season and
  severity of its cold are separate local conditions.
- `رأس المال` under trade loss (خ س ر B002), `حاق رأسه` (ح ق ق B011), and
  `سد رأس الحوجلة بالصبار` (ص ب ر B018) share recoverable `رأس` while changing
  scale and possessor: capital principal, bodily head/crown, vessel mouth/top.
- `حاق ... الوسط` in the حق branch description and `الصبير الأقدر وهو الوسط
  من الجبال` (ص ب ر B017) return the explicit center term with seasonal versus
  mountain scale.

### Explicit opposition vocabulary

The exact relation words themselves recur and therefore permit complete
topology replay:

```text
الأمن ضد الخوف                    الأمانة ضد الخيانة
الحق نقيض الباطل                  الحقيقة خلاف المجاز
الإنس خلاف الجن                   الإيناس خلاف الإيحاش
الإنس خلاف الوحشة                 الأنس خلاف النفور
الصبر نقيض الجزع                  الصلاح ضد الطلاح
الصلاح ضد الفساد                  الإصلاح نقيض الإفساد
```

Each tuple keeps positive term, negative/opposed term, local dimension, and
whether the source says `ضد`, `نقيض`, or `خلاف`. Replaying the polarity relation
does not make fear, betrayal, falsehood, jinn, estrangement, flight, distress,
badness, and corruption interchangeable.

### Generic recurrences kept nonbinding

`شيء`, `فلان`, `الرجل`, `القوم`, `الناس`, `غيره`, `كل`, suppressed pronouns,
and universal or indefinite objects recur widely. Their recurrence is
registered as form and source position only. None is a global socket. In
particular, the generic `القوم` of rain arrival, reciprocal recommendation,
fattened property, reconciliation, or falling into calamity denotes no shared
group instance without an additional binding; the camel, horse, person, thing,
and property examples likewise remain distinct occurrences.

## Local operation reservoir

The following source operations remain available even where no cross-record
edge has yet appeared. They are arranged by what can be enacted rather than as
a root-by-root verdict.

### Changing, confirming, reconciling, and fitting

- `صلاح` holds act/person/thing moving or standing against فساد/طلاح; `الإصلاح
  نقيض الإفساد`; `المصلحة` and `الاستصلاح` keep the sought beneficial state;
  `أصلحت إلى الدابة أحسنت إليها` gives an initiator, animal beneficiary, act of
  kindness, and improved outgoing relation (ص ل ح B001).
- `والصلح تصالح القوم بينهم`; `اصطلحا وتصالحا واصالحا`; and `الصلح يختص
  بإزالة النفار بين الناس` supply two or more initially estranged participants,
  reciprocal reconciliation, removal of aversion, and a changed inter-personal
  state (ص ل ح B002). This can replay against ح ق ق B004's reciprocal dispute
  while preserving opposite trajectories: disagreement/claims -> contest and
  estrangement -> removed estrangement.
- `هذا الشئ يصلح لك، أي هو من بابتك` retains thing, beneficiary/evaluator,
  person's domain, fit relation, and compatibility outcome (ص ل ح B003).
- `صالح`, `صليح`, and `مصلح` as personal names, including `صالح اسم للنبي`,
  stay proper-name carriers and do not flow into surface `الصالحات` (B004).
- `صلاح` as a name for Mecca and `الصلح` as a river at Maysan remain place-name
  carriers; declared pattern `وزن حذام وقطام` stays attached (B005).

### Pressing, releasing, raining, rising, and ingesting

- A thing, grapes, or oil can be pressed by an agent; pressing produces released
  liquid, `عصارة` or `عصير`; the press and sack-like `معصار` are media/places;
  `عصرت ... إذا وليت عصره بنفسك` keeps self-performed agency distinct from the
  affected fruit and product (ع ص ر B002).
- Clouds arrive bearing rain, are pressed/release rain, or the people receive
  rain: `المعصرات السحائب تعتصر بالمطر`; `أعصر القوم إذا أتاهم المطر`;
  `عصر القوم أي مطروا`; and the readings `يعصرون/تعصرون` with rain outcome
  (B003). Grammatical controller varies among cloud, people, and impersonal rain
  arrival; it is not merged with the beneficiary group.
- Wind raises dust from earth into a column; dust rises circularly; perfume
  effluence rises behind a scented woman's hem: `الإعصار ريح تهب تثير الغبار
  فيرتفع إلى السماء كأنه عمود`, `تهيج الريح التراب فترفعه`, `لذيلها عصرة ...
  من فوح الطيب وهيجه` (B004). Force, material, route, shape, and sensory medium
  remain explicit.
- A choking person drinks water little by little to make food pass:
  `الاعتصار أن يغص الإنسان بالطعام فيعتصر بالماء ... يشربه قليلا قليلا
  ليسيغه`; the cited dry-throat utterance remains attached (B008). Person,
  obstructing food, throat, water, incremental measure, and successful passage
  are separate ports.
- `المعصور اللسان اليابس عطشا` keeps tongue, dryness, thirst, and resulting
  bodily state (B014); `العصار الفساء` keeps the exact named bodily wind without
  importing the dust-storm relation (B015).

### Refuge, withholding, reversal, gift, and protected enclosure

- `تعلق بشيء وامتساك به`; `العصر الملجأ`; `العصر المنجاة`; `اعتصرت بفلان
  وتعصرت أي التجأت إليه`; place-directed refuge; and `ما بينهما عصر ولا يصر أي
  ما بينهما مودة ولا قرابة` provide seeker, support/person/place, attachment,
  danger/open condition, and refuge or absent bond (ع ص ر B005).
- `العصر الحبس`; `ما عصرك أي ما منعك`; extracting another's property from his
  hand; a parent withholding a child's property; `يعتصر يسترجع`; and the full
  reversal `أعطيت فلانا عطية فاعتصرتها أي رجعت فيها` provide holder, owner,
  property, transfer, prevention, and reversed transfer (B006).
- `العصر العطية`; `يعصر ... تعطي`; `العصارة والمعتصر` as good/giving;
  `المعتصر` taking/receiving from a thing; yield and land exploitation provide
  giver, recipient, resource, extraction, gift/yield, and possession states
  (B007). The giving trajectory and B006's taking-back trajectory remain
  simultaneously open.
- Crop enters ears/covers and becomes guarded in husks: `عصر الزرع صار في
  أكمامه`; `تحرز في غلفه` (B010). Crop, enclosing husk, transition into cover,
  and protected outgoing state remain local.

### Time, maturation, lineage, degree, and named remainder

- `العصر` as age/time, day/night or morning/evening pair, afternoon, prayer
  time, occasion, slowness, or coming outside an expected time keeps each
  temporal scale and boundary distinct (ع ص ر B001).
- A girl reaches or approaches menstruation/youth; `إذا رأت في نفسها زيادة
  الشباب فقد أعصرت وهي معصر`; confinement in the house is separately supplied
  as a reason for `عصرا` (B009). Perceiver, bodily subject, detected increase,
  threshold, named attained state, and social enclosure remain typed.
- `العنصر` is origin/lineage with declared added nūn; noble extraction and
  return of an affiliate to origin remain lineage operations (B011).
- `العصرة` as lower/lesser status among clients (`دنية دون من سواهم`) provides
  group, comparison class, ranking direction, and excluded others (B012).
  `العصرة شجرة` remains a named tree (B013).

### Intended action, causing action, office, and exchange

- Action is any intentionally performed animal act, and can be good or bad;
  actor -> intended act -> resulting work remains the B001 `عمل` tuple.
- Causing another to act, requesting work, using a thing, deploying opinion,
  speech, spear, or brick, and directing one's mind in deliberation supply
  causer/user, worker/instrument, task, medium, and result: `يستعمل غيره`,
  `طلب إليه العمل`, `أعمل فلان ذهنه ... دبره بفهمه` (ع م ل B002).
- Charity officials take alms; a person is appointed to an office of authority;
  `التعميل تولية العمل`. Appointer, office-holder, source community/property,
  collected alms, and governing office remain distinct (B003).
- `العمالة أجر ما عمل`, `رزق العامل`, `العملة والعمالة أجر العمل`: performed
  work -> due wage/provision -> worker recipient (B004).
- `عاملت الرجل أعامله معاملة في المبايعة وغيرها`: two participants enter a
  reciprocal transaction, with exchange object and terms left locally open
  (B005).
- `العملة` are people working by hand in digging, lining, clay, or another
  craft: group, hands, material, operation, and made/altered site (B006).
- `لا تتعمل ... لا تتعن`; `سوف أتعمل في حاجتك أي أتعنى`: laboring toward a
  need is explicitly equated with taking trouble (B007).
- A man or she-camel is disposed/formed for work; the noble working camel has an
  ingrained capacity rather than one performed event (B008).

### Working parts, paths, and movement

- `عامل الرمح`/`عاملته` is the shaft/chest portion next to the spearhead and
  below another named part. Whole spear, ordered part, adjacency to point, and
  direction along the implement are preserved (ع م ل B009).
- `عوامل الدابة قوائمه واحدها عاملة` and the far-seeing eye called `عاملة`
  keep limb and eye as named working parts without merging their functions
  (B010).
- `طريق معمل أي لحب مسلوك` provides travelers/users, a path made/passable by
  being trodden, direction, and traversed condition (B011).
- `المسافرون إذا مشوا على أرجلهم يسمون بني العمل`: travelers, feet,
  self-propelled walking, route, and collective name remain active (B012).

### Surfaces, sides, containers, and hard boundaries

- Seeing/hearing/knowing operations under `آنس` keep sensory medium and
  perceiver distinct; `الاستئناس النظر` adds directed inspection, and `أحس بما
  رابه` retains disturbing stimulus and felt outcome (ء ن س B002).
- `الأنس`/`الإيناس` removes estrangement; nearness and conversation give joy;
  an `أنوس` animal is opposed to one that attacks (B003).
- `إنسي` is whichever side faces the human, rider, or archer; supplied sources
  preserve disagreement over left/right while fixing the relational criterion
  “what faces/is next to” (B004).
- The image/child seen in the dark of the eye and the fingertip use of
  `الإنسان` remain small-scale image/body carriers (B005). `ابن إنسك` for self,
  intimate, chosen companion, confidant, or table companion retains each
  relation to the addressed person (B006).
- Top/sides of vessel or grave (ص ب ر B004), hard stone/gravel terrain (B005),
  inescapable war/calamity (B006), mountain/middle (B017), and stopper at the
  bottle head (B018) make distinct boundaries: edge, terrain, situation with no
  exit, geographic mass, and closure device.

### Claims, obligation, maturity, penetration, and construction

- Truth can oppose falsehood, match what is fixed, become known with certainty,
  or contrast reality with figurative expression (ح ق ق B001).
- A thing becomes due/required; a person is worthy/obligated; an actor makes a
  thing obligatory or earns/deserves it (B002). Initiator of obligation,
  obligated/entitled participant, required thing, and modal state stay apart.
- A right can be a specifically owned claim directed against another; buyer,
  owner, claim, and object possessed remain distinct (B003).
- Two sides claim truth, contest, and one overcomes the other (B004); a verifier
  establishes, confirms, judges, shows evidence, or completes a matter (B005).
- A person protects what is incumbent on him to defend: standard, inviolability,
  precinct, or other protected `حقيقة` (B007).
- Camel maturity/capacity (B008), penetrating thrust (B009), tight cloth or
  sound speech (B010), fitted joints/receptacles (B011), exhausting travel
  intensity (B012), completed fatness (B013), and hoof correspondence/leaning
  (B014) stay fully enacted at their animal, bodily, material, spatial, or
  kinetic scales.

### Measure loss, trade loss, and marked forms

- General `خسر` is diminution/loss of amount (خ س ر B001); trade loss moves
  capital from initial principal toward reduced/no-profit outcome (B002);
  measure loss has an agent reduce scale or measure, an affected commodity and
  measuring medium, and an outgoing lesser quantity (B003).
- `خنسرى`, `خيسرى`, `الخناسر`, and `الخناسير` keep their declared added letters,
  plural status, human weakness/meanness, and destruction uses (B005). Their
  formal excess contrasts with the branch's semantic diminution without
  canceling either.

### Patience homographs at their own scales

- Voluntary self-restraint (ص ب ر B001), coercive restraint/killing/oath (B002),
  guarantee/attendance (B003), top/sides (B004), hard stone/terrain (B005),
  inescapable severity (B006), winter cold (B007), bitter tree extract/medicine
  with declared kasra (B008), sour fruit (B009), layered cloud (B010), table
  sheet/piled unmeasured food (B011), retaliation (B012), clan name (B016),
  mountain/center (B017), and stopper (B018) all remain live. No local branch is
  consumed by P4's first available reciprocal-content enactment.

### Further exact returns without participant merger

- `الإنسان` occurs as the L2 referent, the choking eater in ع ص ر B008, the
  person set up for killing in ص ب ر B002, and the human whom God reforms in
  ص ل ح B001. Exact generic form is carried; no occurrence identity is.
- `الطعام` is an obstruction swallowed with water in ع ص ر B008 and the
  material laid on a broad sheet or heaped in ص ب ر B011. The food occurrences
  differ, while route-through-throat and pile-on-surface preserve their own
  spatial relations.
- `شجرة` occurs as the source of bitter extract in ص ب ر B008, source of sour
  fruit in B009, and the complete identity `العصرة شجرة` in ع ص ر B013. Tree,
  extract, fruit, and named tree remain distinct nodes.
- `الموت` appears in `الوصية بعد الموت` (و ص ي B002) and `المصبورة المحبوسة
  على الموت` (ص ب ر B002). One is a temporal condition for a transmitted
  testament; the other is an imposed endpoint for the held living being.
- `اليد` returns as property being extracted `من يده` (ع ص ر B006), workers
  acting `بأيديهم` (ع م ل B006), and the forelimb position in `يضع رجله في
  موضع يده` (ح ق ق B014). `يده = يد + ه` and `بأيديهم = بـ + أيدي + هم`
  preserve possessor, number, and bodily/figurative scale.
- `الكلام` is connected testamentary speech in `كأنه كلام يوصى أي يوصل`
  (و ص ي B002), something an agent can operate/use in `يعمل ... كلامه`
  (ع م ل B002), and firmly realized speech in `كلام محقق أي رصين` (ح ق ق
  B010). These supply speech-source, deployment, transmission, construction,
  and received form as distinct ports.
- `الرمح` is an implement one can set to work (ع م ل B002) and a whole with a
  named ordered part `عامل الرمح` beside the spearhead (B009). The instrument
  occurrence need not be the part-description occurrence.
- Added `ن` is itself an explicitly named microcontact: خ س ر B005 says of
  `خنسرى/خيسرى` that `النون والياء زائدتان`, while ع ص ر B011 says of
  `العنصر` that it is `مما زيدت فيه النون` and preserves base `العصر`.
  The same named addition operation acts on different full forms and produces
  different results; the added letter, base, and result stay separate.
- The named letter `الصاد` returns with declared vocalic differences: `الصبار
  بضم الصاد` (ص ب ر B009) and `الصلاح بكسر الصاد المصالحة` (ص ل ح B002).
  Surface `صَّبْرِ` and `صَّٰلِحَٰتِ` retain their own exact vocalization. This
  is a pronunciation circuit, not identity of fruit, reconciliation, patience,
  or good works.
- Threshold entry recurs in `الحق من الإبل ... دخل في الرابعة` (ح ق ق B008),
  `استأمن إليه دخل في أمانه` (ء م ن B001), and the girl's `بلغت عصر شبابها`
  (ع ص ر B009). Entrant, boundary, attained state, and consequence align while
  camel, seeker, and girl remain distinct.
- `السلطان` is the appointing institutional context in ع م ل B003 and the actor
  who exacts retaliation/causes execution in ص ب ر B012. Office-conferral and
  coercive requital have different affected participants and outcomes.
- `الفعل` under ع م ل B001 is the intentional act; ح ق ق B001's branch field
  includes matching an act, saying, or belief to what is fixed, and ص ل ح B001
  locates goodness/corruption especially in acts. This exact act/work cluster
  re-enters surface P2 while retaining intent, matching, and quality as three
  relations.
- `المال` and attached forms bring capital reduced in trade (خ س ر B002), a
  claim owned against another/buyer and property reaching fatness (ح ق ق
  B003/B013), and another's or a child's property extracted/withheld (ع ص ر
  B006). Owner, claimant, buyer, parent, child, and property instance do not
  merge.
- `الشيء` in `وصيت الشيء وصلته`, `حق الشيء وجب`, `خسرت الشيء ... نقصته`,
  `كل شيء عصر ماؤه`, and `هذا الشئ يصلح لك` retains five incompatible local
  type constraints: connectable term, obligated matter, diminished quantity,
  pressable material, and fit item. Its generic spelling creates no handoff.

### Uncompressed microfacets retained with their carriers

- The `آمين` field also retains the what-is assertion that one view made it
  `اسما من أسماء الله`, separately from the source assertion that it is
  `اسم للفعل` meaning `استجب`. The attributed naming claim, verb-name analysis,
  request, and response outcome are not collapsed (ء م ن B003).
- Human/group `إنس` retains `ما بالدار أنيس بمعنى أحد`; sensory `آنس` retains
  fright sensed or a thing found in oneself; the facing animal side retains its
  riding and milking relation; and the eye/fingertip carrier retains
  `إنسان الكف` beside `الأنملة` (ء ن س B001/B002/B004/B005).
- The claim field retains comparative entitlement among claimants; the dispute
  field retains the named expression `نزق الحقاق`; and fitted receptacles retain
  `حق الورك`, `حق الوابلة`, `حق العاج`, `الحق من الخشب`, and `حق الكهول بيت
  العنكبوت` as separate named carriers (ح ق ق B003/B004/B011).
- Coercive patience retains a living being held until it is shot, not only a
  person installed for killing; side/edge patience retains filling up to the
  vessel's `أصبار`; severe cold retains `صنابر الشتاء`; the sour `الصبار`
  retains its broad red stone/seed `عجم أحمر عريض`; and the B018 branch image
  retains bottle-and-well closure alongside the exact bottle-stopper source
  assertions (ص ب ر B002/B004/B007/B009/B018).
- Refuge keeps the exact named carrier `عصرة المنجود`. Withholding keeps
  `تعصر أي تعسر`, the taker `المعتصر الذي يأخذ من الشيء يصيب منه`, and
  `فلان عاصر` as withholding/little-good disposition. Incremental drinking
  keeps the complete cited utterance `لو بغير الماء حلقي شرق كنت كالغصان
  بالماء اعتصاري` (ع ص ر B005/B006/B008).
- Lineage keeps `كريم المعصر أي كريم عند المسألة`, `فلان كريم العصير أي كريم
  النسب`, and `كلا يئل في الانتساب إلى أصله الذي هو منه`; yield keeps both
  `يعصرون قال يستغلون بأرضيهم` and `وفيه تعصرون أي تستغلون` (ع ص ر
  B007/B011).
- Intended action retains `اعتمل إذا عمل لنفسه`. Caused/used action retains
  opinion, speech, spear, and `البناء يستعمل اللبن`; work-disposition retains
  both `رجل عمل` and `رجل عمول`; hand work retains digging, lining/well-work,
  and clay as distinct materials/operations (ع م ل B001/B002/B006/B008).
- Connection retains plant-to-plant continuity, `أرض واصية متصلة النبات`, and
  one open land joined to another. Testament retains `الوصاة كالوصية`,
  `الوصاية مصدر الوصي`, and the directional contrast `أوصيت له بشئ` versus
  `أوصيت إليه إذا جعلته وصيك` (و ص ي B001/B002).

These details stay attached to their exact complete assertions; they do not
create new cross-record edges merely by being more specific.

## Typed ports

An arrow below is available only where a supplied relation licenses it. Blank
incoming states remain blank; no generic event template fills them.

### Positioned surface ports

| Port | Exact carrier and source | Participants and roles | Operation, direction, state, scope |
|---|---|---|---|
| `S-L1-OATH` | `وَٱلْعَصْرِ`, syntax `...001...a1` | grammatical governor `وَ`; governed noun `ٱلْعَصْرِ`; enunciating semantic initiator not supplied | oath particle -> governed complement; no lexical sense selected; line 1/3, word 1/1 |
| `S-L2-ISM` | `ٱلْإِنسَٰنَ`, morphology + syntax `...002...a1` | grammatical dependent/ism; singular human referent; semantic initiator of the state not supplied | governed by `إِنَّ`; M ACC definite; line 2, word 2/4 |
| `S-L2-KHABAR` | `لَفِى خُسْرٍ`, syntax `...002...a2-a3` | affected/referential participant = `S-L2-ISM`; content/location = indefinite `خسر`; cause, agent, instrument open | emphatic predication, human -> in loss condition; L2 ending |
| `S-L3-EXCEPT` | `إِلَّا ٱلَّذِينَ ...`, syntax `...003...a1` | operator; excepted MP relative group; enclosing contrast set supplied only by L2/L3 relation | exception -> selected group, P1-P4 in scope; line 3 opening |
| `S-P1` | `ءَامَنُوا۟`, morphology and L3 scope | 3MP group = grammatical controller/semantic initiator; lexical endpoint/open content not expressed on surface | perfect form-IV operation; incoming state unspecified -> belief/assent operation supplied by ء م ن B002 |
| `S-P2` | `وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ`, syntax `...a2-a4` | same group occurrence as controller/agent; `الصالحات` explicit affected/direct object | perfect intended action -> acted good-work object; result/beneficiary open |
| `S-P3` | `وَتَوَاصَوْا۟ بِٱلْحَقِّ`, syntax `...a4-a6` | same distributed group; members rotate source/recipient by و ص ي B003; truth is content, not participant | reciprocal recommendation, member -> truth-content -> other member; perfect; first occurrence |
| `S-P4` | `وَتَوَاصَوْا۟ بِٱلصَّبْرِ`, syntax `...a6-a7` | same distributed group; members rotate source/recipient; patience is content | reciprocal recommendation, member -> patience-content -> other member; perfect; second occurrence |

### Lexical operation ports with surface access

| Port | Exact licensing assertion | Typed local realization |
|---|---|---|
| `L-AMN-SECURE` | `أصل الأمن طمأنينة النفس وزوال الخوف` | نفس as affected experiencer; fear present/open -> fear removed and self calm; security is outgoing state |
| `L-AMN-ASSENT` | `إذعان النفس للحق على سبيل التصديق` | نفس as assenting participant -> إذعان/تصديق -> الحق as referential endpoint; modality “على سبيل التصديق” retained |
| `L-AMN-PROMISE` | `المؤمن ... يصدق ما وعد عبده` | confirmer -> promised content -> servant/recipient; promise and confirmation state distinct |
| `L-INS-PERCEIVE` | `آنست الشيء إذا رأيته وآنسته إذا سمعته` | perceiver -> seeing/hearing medium -> perceived thing/sound; knowledge outcome supplied in adjacent examples |
| `L-INS-EYE` | `إنسان العين المثال الذي يرى في السواد` | image/example as seen entity; dark of eye as containing medium; viewer remains open |
| `L-HQQ-MATCH` | `أصل الحق المطابقة والموافقة` | item/assertion/belief/action -> match/conform -> fixed counterpart; polarity opposed to باطل |
| `L-HQQ-DUE` | `حق الشيء وجب` | thing -> becomes due/necessary; obligating initiator and obligated recipient may remain open in this minimal assertion |
| `L-HQQ-ESTABLISH` | `أحققت كذا أي أثبته حقا أو حكمت بكونه حقا` | verifier/judge -> evidence/judgment -> matter -> established-as-truth state |
| `L-KSR-GENERAL` | `الخسر النقصان` | affected amount/status -> diminution -> lesser outgoing state; cause open |
| `L-KSR-MEASURE` | `خسرت الميزان وأخسرته إذا نقصته` | agent -> reducing operation through scale/measure -> measured quantity/scale -> diminished state |
| `L-KSR-TRADE` | `خسر التاجر إذا وضع من رأس ماله` | trader/owner -> transaction -> capital -> reduced principal/no-profit outcome |
| `L-SBR-SELF` | `الصبر حبس النفس عن الجزع` | self as controller/holder and affected participant -> holding away from distress -> held/stable state; voluntary agency retained |
| `L-SBR-COERCE` | `المصبورة المحبوسة على الموت` | external holder/force open -> living being -> confinement -> death endpoint; coercive polarity |
| `L-SBR-PILE` | `الصبرة من الطعام بعضه فوق بعض` | food parts -> stacking -> other food parts; vertical direction; pile outgoing form |
| `L-SBR-EXTRACT` | `الصبر بكسر الباء عصارة شجرة` | explicit term identity: kasra-pronounced `الصبر` = tree extract; tree source and product type retained |
| `L-SLH-REPAIR` | `الإصلاح نقيض الإفساد` / `أصل واحد يدل على خلاف الفساد` | initiator open -> action/person/thing -> repair/good state opposed to corruption |
| `L-SLH-RECONCILE` | `الصلح يختص بإزالة النفار بين الناس` | people/parties -> reciprocal reconciliation -> aversion removed -> changed between-party state |
| `L-ASR-TIME` | `العصر الدهر`; `العصران الليل والنهار` | time carrier or paired spans; direction/order supplied by pair wording, no causal agent |
| `L-ASR-PRESS` | `ضغط شيء حتى يتحلب`; `العصارة ما سال عن العصر` | pressing agent/force -> pressable material -> pressure -> released liquid/product; container/tool may bind from same branch |
| `L-ASR-HOLD` | `العصر الحبس`; `ما عصرك أي ما منعك` | exact identity and question: holder/cause -> affected participant/property -> prevention/holding; outgoing nontransfer |
| `L-ASR-GIVE` | `العصر العطية`; `يعصر ... تعطي` | giver -> gift/good/yield -> recipient; transfer state |
| `L-ASR-REVERSE` | `أعطيت فلانا عطية فاعتصرتها أي رجعت فيها` | giver -> recipient -> gift transferred -> same giver takes it back; explicit state reversal |
| `L-AML-ACT` | `كل فعل يكون من الحيوان بقصد` | intentional animal agent -> intended act -> performed work; quality separately supplied |
| `L-AML-CAUSE` | `استعمله ... طلب إليه العمل` | requester/causer -> requested task -> other worker; other becomes grammatical/semantic actor in later work |
| `L-AML-WAGE` | `العمالة أجر ما عمل` | completed work -> wage due -> worker recipient; prior act required |
| `L-WSY-CONNECT` | `أصل يدل على وصل شيء بشيء`; `وصيت الشيء وصلته` | connector -> first thing -> connection -> second thing; connected outgoing relation |
| `L-WSY-TIME` | `وصيت الليلة باليوم وصلتها` | connector/operation -> night -> day -> explicit joined temporal state |
| `L-WSY-TESTAMENT` | `الوصية ... كأنه كلام يوصى أي يوصل` | speaker/testator -> connected speech/content -> another/legatee/executor; after-death modality separately retained |
| `L-WSY-RECIP` | `تواصى القوم ... أوصى بعضهم بعضا` | distributed group: each member as source and recipient -> recommendation content -> other member; reciprocal direction |
| `L-WSY-FIT` | `وصى لها المرتع ... فأصابته رغدا` | pasture/condition -> grazing animal beneficiary -> fit/ease -> abundance/ease outcome |

### Open ports that stay precisely constrained

- `S-L1-OATH`: the semantic speaker/initiator and the particular lexical sense
  of `العصر` are not supplied by surface syntax. The port is “governed exact
  carrier at first line boundary,” not a generic source slot.
- `S-L2-KHABAR`: the human referent and loss state are bound; cause, agent,
  instrument, scale, and whether the state is quantity, trade, measure, or
  another B001 local realization remain unfilled.
- `S-P1`: the controller is bound; no surface object is. `L-AMN-ASSENT` exposes
  an endpoint `الحق`, and the exact later surface term offers a candidate edge,
  but P1 does not acquire P3's prepositional complement by adjacency.
- `S-P2`: agent and direct object are bound. Product, beneficiary, duration,
  instrument, and wage are open unless a supplied action branch or later edge
  binds one.
- `S-P3` and `S-P4`: group, reciprocal direction, and their respective contents
  are bound. The exact uttered wording, individual speaker sequence, temporal
  frequency, and post-recommendation result remain open.
- `L-ASR-PRESS`: pressable material, force, product, and tool ports are typed;
  none can be filled by generic `شيء` alone. Grapes/oil, cloud/rain, and tree
  extract are separately licensed local realizations.
- `L-SBR-SELF`: self, distress, holding, and voluntary direction are supplied;
  no external coercer can enter from B002 without an explicit parameter map
  preserving changed agency and polarity.
- Proper names, place names, clan names, and named trees keep their own entity
  type even when their spelling contacts a passage form.

## Licensed candidate edges

The mappings below are generated without ranking. Each declares exactly what
can cross the edge.

### Exact circuits

1. `S-P1 (ءَامَنُوا)` -> **morphology/root access carrying exact lemma/root and
   inflection** -> `L-AMN-ASSENT`. Payload: form-IV `ءَامَنَ`, root `ء م ن`,
   3MP controller position. It does not carry later truth content yet.
2. `L-AMN-ASSENT.term (للحق = لـ + الحق)` -> **exact recovered-term recurrence
   carrying `الحق` plus the full assent assertion** -> `S-P3.content
   (بالحق = بـ + الحق)`. Prefix direction changes from `لـ` to `بـ`; the base
   term stays exact.
3. `S-P3.content` -> **exact surface/lexical term recurrence carrying form and
   positioned content role** -> every typed `ح ق ق` truth assertion. It does
   not carry the P3 group into the verifier, disputant, buyer, camel, cloth, or
   wound ports.
4. `S-P2` -> **surface direct-object binding plus exact phrase collision** ->
   `L-AML-ACT + ص ل ح B001`. Payload: controller, act `عمل`, object
   `الصالحات`, and the supplied good/bad action qualification. Neither the
   proper name صالح nor place صلاح crosses.
5. `L-WSY-TESTAMENT.term (يعمل = يـ + عمل)` -> **base-form recurrence carrying
   `عمل` and the assertion “what is to be acted on”** -> `S-P2`. The recommendation
   participant is not automatically the surface action object.
6. `S-L1-OATH.term (العصر)` -> **exact lexical identity access** ->
   `L-ASR-TIME`, `L-ASR-PRESS`, `L-ASR-HOLD`, `L-ASR-GIVE`, and the other
   explicitly supplied homographs. Each returns a separate enactment.
7. `L-ASR-TIME.terms (الليل/اليوم/الليلة)` -> **exact term recurrence carrying
   the time-pair occupants** -> `L-WSY-TIME`; then `وصيت/وصلتها` -> **explicit
   connection relation carrying the complete time-joining tuple** -> the
   `و ص ي` family contacted by `S-P3/S-P4`.
8. `L-ASR-HOLD.term (الحبس)` -> **exact identity/equation carrying
   `العصر = الحبس`** -> `L-SBR-SELF.operation (حبس النفس)`; and the latter ->
   **definition carrying self-restraint tuple** -> `S-P4.content` through exact
   `الصبر`. Distinct agency and affected participants remain visible.
9. `L-ASR-PRESS.product (العصارة)` -> **exact definition carrying
   pressure-to-product lineage** -> `L-SBR-EXTRACT.product (عصارة شجرة)`;
   `L-SBR-EXTRACT.term` -> **declared consonantal/form contact with vocalic
   difference** -> `S-P4.content`. No liquid material crosses into P4 absent an
   accepting material port.
10. `S-L2-KHABAR.term (خسر)` -> **exact lexical access** ->
    `L-KSR-GENERAL`, `L-KSR-TRADE`, `L-KSR-MEASURE`, and B005 marked forms.
    The L2 human remains the affected participant only where that local
    operation accepts a human/status port; generic recurrence does not force it.
11. `L-KSR-MEASURE.terms (الكيل/الوزن)` -> **exact term recurrence carrying
    measuring regime only** -> `L-SBR-PILE`'s `بلا وزن ولا كيل`. Presence of
    diminution and absence of measure remain opposite parameters.
12. `S-L2-ISM (الإنسان)` -> **explicit containment of supplied `الإنس` and
    exact full-form recurrence** -> ء ن س B001/B005. Payload: written form,
    singular surface position, and each complete local assertion; not every
    generic human example.
13. `ء ن س B005 (إنسان العين)` -> **exact `عين` recurrence carrying image-in-eye
    topology** -> ع م ل B010's `بعين بعيدة النظر`; surface roots then reopen
    `S-P2`. Watcher, visible image, and action agent do not merge.
14. `L-WSY-RECIP (بعضهم بعضا)` -> **complete source assertion and exact ordered
    expression** -> the two `S-P3/S-P4` reciprocal events. The same expression
    also contacts SBR cloud/food stacking by form only.
15. `و ص ي B002 (كلام ... يوصل)` -> **exact `كلام` recurrence** -> ع م ل B002
    `يعمل ... كلامه` and ح ق ق B010 `كلام محقق`. Payload is speech as a typed
    medium; testament, deployment, and firm construction stay separate operations.

### Participant or state handoffs

1. `S-L3-EXCEPT.group` -> **same discourse occurrence across coordination** ->
   controller ports of `S-P1`, `S-P2`, `S-P3`, and `S-P4`. Payload: only the
   plural-group identity and its 3MP features.
2. Each member-source in `S-P3` -> **explicit reciprocal rotation from
   L-WSY-RECIP** -> member-recipient in the same P3 event; likewise within P4.
   Payload: member identity and the event's own bound content.
3. `L-ASR-REVERSE`: original giver -> **explicit state lineage** -> later taker
   back; gift transferred -> **explicit reversal** -> gift reclaimed. This is
   complete inside the source assertion and remains available to later
   formations.
4. `L-ASR-PRESS`: pressable material -> **explicit transformation lineage** ->
   released liquid/`عصارة`; product can enter `L-SBR-EXTRACT` only because the
   latter explicitly accepts `عصارة` as its product term.
5. `L-AML-ACT.completed work` -> **explicit prior-act requirement** ->
   `L-AML-WAGE.work basis`; wage -> worker recipient. The surface P2 act may
   enter only if its performed-work occurrence is preserved, not by shared root
   alone.
6. `L-AMN-ASSENT.نفس` and `L-SBR-SELF.نفس` remain a constrained candidate
   handoff through the same P1/P4 group member. The binder is not yet explicit
   as a surface `نفس`; keep member-self identity open rather than completed.

### Complete topology replays

1. `S-P3` <-> `S-P4`: identical surface topology and grammatical parameters,
   with explicit map `position 6th -> 8th`, `content الحق -> الصبر`; controller,
   aspect, number, reciprocal direction, preposition, definiteness, case, and
   event shape retained. No content handoff occurs.
2. `L-AMN-SECURE`, `L-HQQ-MATCH`, `L-SBR-SELF`, and `L-SLH-REPAIR`: each has an
   explicitly supplied opposition relation. Replay maps positive term,
   opposed term, state dimension, and polarity while preserving fear/betrayal,
   falsehood, distress, and corruption as different occupants.
3. ح ق ق B004 dispute <-> ص ل ح B002 reconciliation: plural parties and
   reciprocal relation align; parameter map retains claim/contest/overcoming
   versus removal of aversion/reconciled outcome. No disputant instance is
   handed off.
4. HQQ door fit / hoof placement <-> SLH personal fit <-> WSY pasture fit:
   item-A, target/slot-B, correspondence, and outcome align, with material,
   bodily, personal, and ecological scales preserved.
5. ASR rain-cloud release <-> ASR pressed-liquid release <-> SBR stacked cloud:
   medium, contained material/layer, force or holding relation, direction, and
   output align only under the explicit cloud/liquid/top-above relations. Rain,
   juice, and cloud parts do not transfer.
6. KSR measured diminution <-> SBR unmeasured pile purchase: commodity,
   transaction, quantity regime, and outcome align; measure present/reduced
   versus measure absent remains the explicit polarity map.
7. ASR withholding <-> SBR self-restraint <-> SBR coercive restraint <-> ASR
   crop enclosure: holder/boundary, held entity, direction, agency, consent,
   and outgoing state align while all changed parameters remain exposed.
8. WSY reciprocal `بعضهم بعضا` <-> SBR layered `بعضه فوق بعض`: distributed
   units and relation repeat; horizontal role rotation versus vertical
   ordering is retained.
9. INS facing side <-> SBR vessel/grave sides <-> HQQ joint/socket <-> AML spear
   part: whole, positioned part/boundary, orientation, and user/body relation
   align; no part moves between wholes.
10. AMN trustworthy camel <-> HQQ mature/capable camel <-> AML work-disposed
    camel: animal, acquired/inherent condition, risk/capacity, and work/load
    outcome align with distinct generic animal occurrences.

### Surface bindings

1. `إِنَّ` -> governed ism `ٱلْإِنسَٰنَ`; `فِى` -> governed `خُسْرٍ`; full
   `لَفِى خُسْرٍ` -> khabar predicated of that ism.
2. `إِلَّا` -> `ٱلَّذِينَ` -> scope P1-P4. This binds selection/contrast, not
   numerical identity between the L2 singular and L3 plural.
3. P1 -> P2 -> P3 -> P4 by coordination; group identity crosses, neighboring
   complements and outcomes do not.
4. P2 -> `ٱلصَّٰلِحَٰتِ` as direct object.
5. P3 -> `بِٱلْحَقِّ` and P4 -> `بِٱلصَّبْرِ` as separately governed content
   complements.
6. L1 oath `وَ` -> `ٱلْعَصْرِ`; later conjunction `وَ` tokens do not inherit
   oath government.

No scaffold binding is available in this turn.

## Provisional enactments of connected paths

These are operational configurations, not governing interpretations. Each path
can coexist with the others, and every step restates the payload it is allowed
to carry.

### Same group, assent endpoint, then reciprocal truth-content

```text
S-L3-EXCEPT.group
-> surface identity of controller only
-> S-P1 / ءَامَنُوا
-> lexical access to L-AMN-ASSENT
-> نفس --إذعان/تصديق--> الحق
-> exact recovered term الحق only
-> S-P3.content / بِٱلْحَقِّ
-> L-WSY-RECIP topology
-> each group member --truth content--> another group member
```

The first and last group occupants can be coreferred because surface
coordination supplies one relative-group occurrence. The نفس is a member-self
opened by the lexical assertion; whether it binds across every member remains
an explicit open role. The assent state does not travel into the recipient of
P3 merely because `الحق` travels as a term. P3's recommendation outcome also
remains open.

### Intended act, good-work object, and recommendation about what is acted on

```text
S-P2.controller
-> surface direct action
-> S-P2.object / الصالحات
-> exact collision with الأعمال الصالحة والسيئة
-> intentional-act tuple L-AML-ACT + action-quality tuple L-SLH-REPAIR

L-WSY-TESTAMENT / التقدم إلى الغير بما يعمل به مقترنا بوعظ
-> exact base عمل, with addressee and actable-content ports retained
-> attraction toward S-P2 and toward S-P3/S-P4 reciprocal addressees
```

The supplied field can place work, good qualification, addressee, and something
to be acted on in one open configuration. It does not yet identify `الحق` or
`الصبر` as a particular direct object of P2, nor does it identify P2's completed
act as the result of either recommendation. Those handoffs remain unbound.

### Time pair joined by the later root-family operation

```text
S-L1-OATH / العصر
-> L-ASR-TIME: الدهر; العصران الليل والنهار; اليوم والليلة
-> exact terms الليلة + اليوم
-> L-WSY-TIME: وصيت الليلة باليوم وصلتها
-> full connection topology, time-1 -> joined-to -> time-2
-> lexical وصى/تواصى family
-> formal return at S-P3 and S-P4
```

The complete temporal joining occurs inside the source utterance before the
surface repeated form is revisited. The later plural reciprocal events accept
group members and contents, not time periods; therefore the path carries the
connection topology and form-family contact, not night/day occupants into P3 or
P4.

### Holding relations between first and last boundary carriers

```text
S-L1-OATH.term العصر
-> exact equation العصر الحبس
-> operation holder --holds/prevents--> affected
-> exact term حبس
-> الصبر حبس النفس عن الجزع
-> self --holds self away from--> distress
-> exact term الصبر, with passage-vowel record retained
-> S-P4.content
```

The configuration exposes a generic holding operation at the first boundary
and a fully typed self-restraint operation at the last. It also branches into
parent/property withholding, coercive deathward confinement, crop enclosure,
girl/house confinement, vessel stopper, and inescapable calamity. Each branch
preserves agency, boundary, consent, and outcome; none is selected as the one
meaning of either surface noun.

### Extracted product between first and last boundary carriers

```text
S-L1-OATH.term العصر
-> L-ASR-PRESS
-> pressable source --pressure--> released عصارة
-> exact product term عصارة
-> الصبر بكسر الباء عصارة شجرة
-> tree --source/product identity--> bitter extract
-> consonantal contact, declared vowel difference retained
-> S-P4.content الصَّبْرِ
```

This path is complete as formal/source enactment but has no surface material
port at P4 that accepts liquid. It therefore keeps product lineage and vocalic
difference active without turning reciprocal patience-content into a fluid.

### Loss, measure, and an unmeasured pile

```text
S-L2-KHABAR / خسر
-> L-KSR-MEASURE: measured thing --diminution through measure--> lesser amount
-> exact terms الوزن / الكيل
-> L-SBR-PILE: food parts --stacked without weight or measure--> صبرة
-> consonantal/source contact with S-P4 term الصبر
```

Measure is present and manipulated in the first local scene, explicitly absent
in the second. The food pile is not handed to the L2 human, and no diminished
quantity is imported into P4. The opposed measuring regimes, commerce ports,
and exact word family remain a connected configuration.

### Seen human-image, seeing, and a named working eye

```text
S-L2-ISM / الإنسان
-> exact containing form إنسان العين
-> image in dark of eye --is seen by--> viewer
-> ء ن س B002 seeing/hearing operation
-> exact عين / بعين / عينه returns
-> ع م ل B010 عاملة = far-seeing eye in the cited arrangement
-> form-family return to S-P2 / عملوا
```

This configuration retains surface person, image, eye, viewer, watcher, and
work-agent as six possible ports. The exact terms and named relations connect;
no participant identity has been supplied among them.

### Reciprocal relations with changed polarity and outcome

```text
و ص ي B003: members recommend to one another / communicate
ح ق ق B004: parties each claim الحق / dispute / one overcomes
ص ل ح B002: parties reconcile / estrangement is removed
```

All three provide plural parties and a between-party operation. The explicit
parameter map retains transported content versus competing claim, cooperative
reciprocity versus contention, and removed estrangement versus victory. Surface
P3/P4 instantiate only the recommendation topology. Dispute and reconciliation
remain topology replays, not hidden surface events.

### Speech made operative, connected, and firm

```text
و ص ي B002  كلام يوصى أي يوصل
ع م ل B002  يعمل ... كلامه
ح ق ق B010  كلام محقق أي رصين
```

Speech can be content connected to another, a medium an agent puts into
operation, and an artifact/state characterized as firm. A candidate composite
has speaker/agent, speech content, operation/deployment, route to another, and
firm outgoing form. It remains open whether any one speech occurrence occupies
all roles; exact `كلام` recurrence alone does not assert that handoff.

### Transfer, return, due result, and succession

The field supplies several complete trajectories without merging their
materials:

- giver -> gift -> recipient, then the original giver takes the same gift back
  (`أعطيت فلانا عطية فاعتصرتها`) versus `العصر العطية` as outward transfer;
- testator/speaker -> connected testament -> another/executor, with after-death
  condition;
- worker -> completed work -> wage/provision due to that worker;
- recommender -> content -> other member, reciprocally reversed;
- owner/claimant -> right against buyer/other -> ownership state;
- trader -> transaction -> diminished capital.

Each has an explicit source, payload, endpoint, and state change. Their open
attraction lies in the different ways something crosses, is due, is withheld,
or returns; no generic “transfer” label itself creates an edge.

### Attained capacity at a threshold

Camel entering its fourth year and becoming fit to carry, property/she-camel
reaching full fatness, girl reaching youth/menstrual threshold, seeker entering
security, crop entering its husk, and a worker/animal disposed to work all expose
incoming state -> boundary crossing -> named attained state -> newly licensed
capacity or condition. Exact `دخل`/`بلغت` contacts and explicit source
transformations license topology replay. The occupants, thresholds, and outcomes
stay distinct.

### Ordered ends and repeated content frames

The three ending nouns can be held simultaneously as:

```text
L1 final: definite M GEN, oath-governed, رِ, root ع ص ر
L2 final: indefinite M GEN, in khabar, رٍ, root خ س ر
L3 final: definite M GEN, recommendation content, رِ, root ص ب ر
```

L1 and L3 provide formal return in definiteness and exact `رِ`; L2 interrupts
with indefiniteness and tanwīn while retaining genitive case and final `ر`.
Lexical source circuits add holding (`العصر الحبس` / `الصبر حبس النفس`),
extract (`العصارة` / `الصبر ... عصارة`), and measure (خسر in measure / صبرة
without measure) around the three typed boundary carriers. These coexist; the
surface sequence itself carries only form, order, morphology, and local syntax.

## Forward traversal with recursive returns

### From L1 into L2

1. `وَ` first opens oath government, not coordination. `ٱلْعَصْرِ` is the only
   orthographic word and the first/last carrier of L1. Its lexical field fans
   into time and paired periods; pressing and extracted liquid; rain-bearing
   cloud; rising dust/perfume; refuge and attachment; holding/prevention and
   gift reversal; giving/yield; incremental drinking; maturation; crop cover;
   lineage with added nūn; lower status; tree; dry tongue; bodily wind.
2. The time branch immediately re-enters the وصي source through night joined to
   day; the holding branch opens exact `حبس`; the pressing branch opens exact
   `عصارة`; added nūn meets the explicitly added nūn in خسر forms. None selects
   a lexical sense for the oath carrier.
3. L2 begins with `إِنَّ`, changing the opening particle from oath government
   to accusative nominal government. `ٱلْإِنسَٰنَ` activates human/group,
   visible/manifest humanity, sensing, companionship, facing side, eye-image,
   and self/intimate expressions. The exact embedded `الإنس` is registered
   before those broader operations.
4. `لَفِى` brings emphasis plus prepositional containment. The human is the
   referential affected participant; `خُسْرٍ` supplies the state. General
   diminution, lost capital/no profit, diminished measure, and marked added-letter
   forms enact separately. Cause, instrument, scale, and loss subtype remain
   open.

### From L2 into L3

1. The L2 ending leaves `إنسان -> in خسر` active. L3 opens `إِلَّا` and binds
   an MP relative group in exception scope. The surface relation contrasts
   scopes but does not turn the plural group into the same participant instance
   as the L2 singular.
2. P1 gives the group a form-IV perfect operation. Security, assent, and `آمين`
   response branches remain distinct. The complete assent-to-truth assertion
   exposes `النفس`, `الحق`, and `التصديق`; exact `الحق` waits ahead at P3.
3. Conjunction at P2 retains the same group and adds an intentional action with
   explicit `الصالحات` object. The source phrase `الأعمال الصالحة والسيئة`
   closes across the two surface words; repair/corruption, reconciliation, fit,
   names, and place names remain separately available from ص ل ح.
4. P3 changes the argument frame from direct object to reciprocal content. The
   lexical source rotates each group member through recommender and recipient;
   exact `الحق` receives the full matching, obligation, claim, dispute,
   establishment, protection, maturity, penetration, construction, fitting,
   intensity, completion, and hoof-position fields without merging them.
5. P4 exactly repeats conjunction + form-VI perfect 3MP + reciprocal group +
   `بـ` content frame, changing only position and content term. `الصبر` opens
   self-restraint, coercive restraint, guarantee, edges, stone, severity,
   winter, extract, fruit, cloud, pile, retaliation, clan, mountain, and stopper.
   It then returns by exact `حبس`, `عصارة`, `الوزن/الكيل`, `السحاب`, `الشتاء`,
   `بعض...بعض`, and boundary `رِ` to earlier carriers.

## Backward traversal as functional reopening

### From `بِٱلصَّبْرِ` backward

- P4 first remains recommendation-content, not an enacted physical homograph.
  Its source definition `حبس النفس` reopens P1's `النفس` through the exact
  assent assertion and reopens L1's `العصر الحبس`. The group-member self becomes
  a constrained open binder across assent and restraint.
- The declared kasra branch `عصارة شجرة` reopens L1 pressing and its product
  lineage. The passage sukūn makes the return visibly nonidentical in
  pronunciation.
- `الصبرة ... بلا وزن ولا كيل` reopens L2 measure-loss with a changed parameter:
  absence of measuring versus diminution through measure.
- Layered cloud reopens L1 rain-cloud and pressure/release; `صبارة الشتاء`
  reopens `حاق الشتاء`; `بعضه فوق بعض` reopens P3/P4 reciprocal
  `بعضهم بعضا` while changing vertical order to role rotation.
- Boundary side, stone, mountain, and stopper reopen earlier side/fitting/refuge
  carriers without entering the reciprocal event's content port.

### From `بِٱلْحَقِّ` backward

- Exact `الحق` returns first to P1's source phrase `إذعان النفس للحق`, so the
  earlier complementless surface belief operation acquires an attraction toward
  the later exact endpoint without stealing P3's syntactic complement.
- `أصل الحق المطابقة والموافقة` reopens P2 as an intentional act and its
  `الصالحات` quality: act, matching-to-fixed, and good/corrupt qualification can
  occupy separate facets of one act only if a later binder supplies the fixed
  counterpart and state.
- `كلام محقق` and establishing/verifying speech reopen the وصي testament-as-
  connected-speech and عمل speech-as-operated-medium circuit.
- Dispute in which each claims truth reopens the reciprocal form of P3 and the
  reconciliation source under صالح; changed polarity and outcome remain
  explicit.
- Obligation, right, due capacity, protection, penetration, woven firmness,
  joint fit, exhausting travel, and hoof placement remain alternative local
  operations rather than being read away after the truth-content contact.

### From the two `تَوَاصَوْا` tokens backward

- The second token reopens the first as a complete topology replay with changed
  content. It does not make truth and patience one payload.
- `تواصى القوم إذا تواصلوا` and `وصيت الشيء وصلته` reopen L1 paired time spans
  through `وصيت الليلة باليوم وصلتها`.
- `التقدم إلى الغير بما يعمل به مقترنا بوعظ` reopens P2's عمل and its acted
  object; recipient and actable content remain open rather than being inferred.
- `الوصي الموصي والموصى إليه جميعا` reopens the reciprocal source/recipient
  rotation while preserving the explicit lexical role equation and distinct
  group-member instances.

### From `ٱلصَّٰلِحَٰتِ` and `عَمِلُوا` backward

- The exact source phrase `الأعمال الصالحة والسيئة` gathers the two positioned
  words into an already supplied lexical phrase, while syntax independently
  binds verb to direct object.
- Intended action reopens the human agent in L2 only as a generic form contact;
  the actual P2 agent is the L3 plural group.
- Wage requiring prior work, appointed office, hand work, transaction,
  exertion, ingrained capacity, spear part, limbs/eye, traveled path, and walking
  travelers all remain possible local action constellations. None is imported
  into `الصالحات` by the shared root.
- Repair versus corruption and reconciliation versus estrangement reopen the
  opposition and reciprocal topologies later encountered under truth and mutual
  recommendation.

### From `ءَامَنُوا` and `ٱلَّذِينَ` backward

- Assent returns to the exact later truth term; security returns to self calm,
  removal of fear, trust, secure dwelling, and the trustworthy camel; `آمين`
  returns to request and response with declared long/short pronunciation.
- `النفس` reopens `ابن إنسك` for self and P4's self-restraint. `المأمن` and
  entry into security reopen L1 refuge/attachment and threshold-entry
  topologies.
- The plural relative group returns to the singular `ٱلْإِنسَٰنَ` only through
  exception scope. Number, definiteness, case, and discourse occurrence remain
  different.

### From `خُسْرٍ` and `ٱلْإِنسَٰنَ` back to L1

- Diminished measure returns forward from the final pile-without-measure; lost
  capital returns to right/property/withholding/gift-reversal fields. These
  backward contacts add transaction, ownership, and quantity ports but no
  causal agent to L2.
- Human reopens visible image in the eye, sensing, facing sides, companionship,
  self/intimate, the choking eater, the coerced victim, and the person reformed.
  They remain separate generic occurrences.
- L2's exact final `رٍ` returns to the `رِ` endings on both sides. Genitive case
  remains constant while definiteness and boundary role change.
- L1's `وَ` is revisited after the three conjunctive `وَ` tokens: identical
  prefix form, changed grammatical relation. The backward pass therefore ends
  at oath government rather than retroactively coordinating L1 with P1-P4.

## Open attractions carried forward

| Concrete fragments held together | Available relation | Binder or parameter still open |
|---|---|---|
| P1 `ءَامَنُوا` + source `إذعان النفس للحق` + P3 `بالحق` | exact term circuit plus same group occurrence | whether P1's unexpressed endpoint is surface-bound to the later P3 content rather than merely contacted |
| P1 `النفس` + P4 definition `حبس النفس` | exact participant term and same member-group field | explicit surface realization of member-self and any state handoff |
| P2 `عملوا الصالحات` + `بما يعمل به` | exact base `عمل`, actable-content relation | identity of recommendation content and performed direct object |
| P3/P4 reciprocal events | complete surface topology replay | exact individual sequencing and outgoing effect on recipients |
| L1 time pair + `وصيت الليلة باليوم وصلتها` + surface تواصوا | exact time terms and supplied connection relation | an accepting temporal port in the surface reciprocal events |
| `العصر الحبس` + `الصبر حبس النفس` | exact equation/definition and holding topology | holder/held parameter map for L1; no surface physical holding port |
| `العصارة ما سال عن العصر` + `الصبر ... عصارة شجرة` | exact product and transformation lineage | passage vowel differs; P4 has no material-product port |
| L2 measure loss + `صبرة ... بلا وزن ولا كيل` | exact measure terms and changed regime | identity of commodity/transaction occurrence |
| human + eye-image + seeing + `عاملة` eye + عملوا | exact forms and perception/instrument relations | participant identity among surface human, viewer, watcher, and group agent |
| truth dispute + reconciliation + mutual recommendation | complete plural relational topologies | changed polarity/outcome map only; no participant handoff |
| testamentary كلام + operated كلام + firm كلام | exact speech medium | one coreferred speech occurrence |
| secure camel + mature camel + work-disposed camel | exact animal class and state/capacity topology | same animal occurrence is not supplied |
| facing animal side + working limbs + kindness to animal | exact `الدابة` class and part/beneficiary relations | same animal occurrence is not supplied |
| camel/girl/security threshold entry | exact entry/attainment forms and state transition | invariant threshold parameter, with occupants and outcomes distinct |
| measured capital/property/right/gift | exact `مال` family and transaction/ownership operations | identity of property and owner across scenes |
| giver takes gift back + reciprocal source/recipient rotation | explicit reversals | payload types differ; no shared gift/content occurrence |
| winter middle + severe winter cold | exact `الشتاء` | temporal state relation between middle and severity |
| `بعضهم بعضا` recommendation + `بعضه فوق بعض` cloud/food | exact distributed pair | horizontal reciprocal versus vertical positional parameter |
| added nūn in `خنسرى` and `العنصر` | exact named letter-addition operation | different bases/results; no lexical identity |
| line-ending `عصر/خسر/صبر` | ordered boundary, GEN morphology, final ر | no semantic payload licensed by position alone |

Every unbound attraction remains a typed opening rather than an incomplete
claim. Proper-name, place-name, bodily, botanical, animal, meteorological,
commercial, material, and acoustic carriers remain available alongside the
currently connected paths.

## Closure coordinates for continuation

- Supplied root/record field: `ء م ن` B001-B003 (3); `ء ن س` B001-B006 (6);
  `ح ق ق` B001-B005 and B007-B014 (13); `خ س ر` B001-B003 and B005 (4);
  `ص ب ر` B001-B012 and B016-B018 (15); `ص ل ح` B001-B005 (5); `ع ص ر`
  B001-B015 (15); `ع م ل` B001-B012 (12); `و ص ي` B001-B004 (4). Total: 77.
- Every record remains either in a surface-access path, an exact source circuit,
  a topology replay, or a fully enacted local operation above. A local carrier
  has not been discarded for lacking a cross-record edge.
- The final exact-contact pass returns the already typed clusters: surface
  bases/affixes; `النفس`; `الحق`; `عمل/صالح`; time-pair forms; `حبس`;
  `عصارة`; cloud terms; measure terms; eye terms; animal terms; matching/fit;
  `وصلت`; `بعض...بعض`; winter/head/center; opposition words; food/tree/death/
  hand/speech/spear/property; named letter additions and declared pronunciations;
  plus generic words registered as nonbinding. No new typed contact is produced
  by another pass through those supplied forms.
- Surface coordinates, source coordinates, affixes, declared vowels, local
  participants, direction, polarity, voice availability, state changes, scale,
  and outcome remain recoverable for recursive maturation. No scaffold relation
  and no governing interpretation has entered this reservoir.
