# Activation Reservoir: S103, V7.5.9, Turn 1

## Field limits and status discipline

This reservoir uses only the supplied passage, morphology, syntax, and lexical
branches. The primary scaffold is absent. Nothing below is a
`PRIMARY_TRANSFORMATION`, and no formation is ranked or selected.

- `SOURCE_ACTUALITY` (`SA`) preserves a supplied passage event or one indexed
  lexical event exactly in its own occurrence, occupants, controller, polarity,
  direction, state, and result.
- `LATENT_MAPPING` (`LM`) preserves an exact contact or a maximal invariant and
  its parameter changes while every member tuple remains local.
- `LATENT_ASSEMBLY` (`LA`) projects facets from named source tuples into roles of
  a new operation. Role projection never asserts that the source occupants met
  historically.
- Passage anchors use `P[line.word]`; morphemes use the supplied `qac_ref`;
  lexical tuples use `R[root]/B[branch]`. Repeated surface performances receive
  separate occurrence IDs even when their written form and root are identical.

Two comparison lanes remain distinct. `strict-written` preserves the supplied
Quranic spelling and every mark. `mark-stripped` removes vocalization and
recitation decoration for detection while retaining such base-letter
differences as `ٱ`/`ا`, `ءا`/`آ`, and `ى`/`ي`. A morphologically supplied lemma
or stem can create a separate recovered node. Thus a detected containment does
not silently regularize spelling, and a root relation does not become an exact
substring relation.

## Exact passage and surface lattice

```text
103:1  وَٱلْعَصْرِ
103:2  إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ
103:3  إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَتَوَاصَوْا۟ بِٱلْحَقِّ وَتَوَاصَوْا۟ بِٱلصَّبْرِ
```

### Complete counts and positioned vectors

| unit | line 1 | line 2 | line 3 | total |
|---|---:|---:|---:|---:|
| supplied lines | 1 | 1 | 1 | 3 |
| orthographic words | 1 | 4 | 9 | 14 |
| morphology rows | 3 | 6 | 21 | 30 |
| syntax carrier positions recoverable from the supplied `q:` anchors | 2 | 4 | 12 | 18 |
| supplied syntax edges | 1 | 3 | 7 | 11 |
| root-bearing stem occurrences | 1 | 2 | 7 | 10 |

`LM-FORM-COUNT-01`: the complete orthographic word-count vector is
`[1,4,9] = [1^2,2^2,3^2]`; its increments are `[3,5]`. This is a positioned
formal carrier only. `LM-FORM-COUNT-02`: the morphology vector is `[3,6,21]`.
`LM-FORM-COUNT-03`: syntax-carrier counts are `[2,4,12]`, with transitions
`x2,x3`. `LM-FORM-COUNT-04`: edge counts are `[1,3,7]`, each later member
equal to twice the prior member plus one. None of these count relations imports
semantic identity.

The per-word morpheme-grouping vector, without regrouping, is:

```text
line 1: [3]
line 2: [1,2,2,1]
line 3: [1,1,2,3,2,3,3,3,3]
whole:  [3 | 1,2,2,1 | 1,1,2,3,2,3,3,3,3]
```

Line 2 encloses its two central two-morpheme words between one-morpheme words.
Line 3 moves through `1,1`, then `2,3,2,3`, then a terminal run of four
three-morpheme words. The passage's first word is itself three-morpheme, so the
opening `3` returns as the last line's four-position terminal grouping.

The surface-root occurrence order is:

```text
[ع ص ر, ء ن س, خ س ر, ء م ن, ع م ل, ص ل ح, و ص ي, ح ق ق, و ص ي, ص ب ر]
```

There are nine distinct supplied roots and ten rooted occurrences because
`و ص ي` performs twice. In first-surface-appearance order their lexical branch
counts are `[15,6,4,3,12,5,4,13,15]`; the lexical file's own root order has the
different complete vector `[3,6,13,4,15,5,15,12,4]`. Both orders remain live.

### Every orthographic carrier and its morphology

1. `P[1.1] وَٱلْعَصْرِ`: `وَ` (`103:1:1:1`, P/PREFIX, oath function in syntax)
   + `ٱلْ` (`103:1:1:2`, DET/PREFIX) + `عَصْرِ` (`103:1:1:3`, lemma
   `عَصْر`, root `ع ص ر`, masculine noun, genitive). Mark-stripped:
   `وٱلعصر`.
2. `P[2.1] إِنَّ`: `103:2:1:1`, lemma `إِنّ`, accusative particle.
   Mark-stripped: `إن`.
3. `P[2.2] ٱلْإِنسَٰنَ`: `ٱلْ` (`103:2:2:1`, DET) + `إِنسَٰنَ`
   (`103:2:2:2`, lemma `إِنسَٰن`, root `ء ن س`, masculine noun,
   accusative). Strict mark-stripped spelling is `ٱلإنسن`; the written dagger
   alif is preserved separately rather than silently replaced.
4. `P[2.3] لَفِى`: emphatic `لَ` (`103:2:3:1`) + preposition `فِى`
   (`103:2:3:2`, lemma `فِى`). Mark-stripped: `لفى`.
5. `P[2.4] خُسْرٍ`: `103:2:4:1`, lemma `خُسْر`, root `خ س ر`, masculine,
   indefinite, genitive noun. Mark-stripped: `خسر`.
6. `P[3.1] إِلَّا`: `103:3:1:1`, exception particle. Mark-stripped: `إلا`.
7. `P[3.2] ٱلَّذِينَ`: `103:3:2:1`, lemma `ٱلَّذِى`, masculine plural
   relative. It is a REL stem, not a DET plus noun, even though the written
   beginning contains the supplied article form after marks are removed.
8. `P[3.3] ءَامَنُوا۟`: `ءَامَنُ` (`103:3:3:1`, lemma `ءَامَنَ`, root
   `ء م ن`, perfect, measure IV, 3MP) + `وا۟` (`103:3:3:2`, 3MP pronoun
   suffix). Mark-stripped: `ءامنوا`; recovered stem/base: `ءامن`.
9. `P[3.4] وَعَمِلُوا۟`: conjunction `وَ` + `عَمِلُ` (lemma `عَمِلَ`, root
   `ع م ل`, perfect 3MP) + `وا۟` (3MP suffix), refs `103:3:4:1-3`.
   Mark-stripped: `وعملوا`; recovered base: `عمل`.
10. `P[3.5] ٱلصَّٰلِحَٰتِ`: `ٱل` (DET) + `صَّٰلِحَٰتِ` (lemma
    `صَّٰلِحَٰت`, root `ص ل ح`, active participle, feminine plural,
    accusative), refs `103:3:5:1-2`. Strict mark-stripped: `ٱلصلحت`; the
    supplied morphology, root, and lexical forms retain their own spellings.
11. `P[3.6] وَتَوَاصَوْا۟`: conjunction `وَ` + `تَوَاصَ` (root `و ص ي`,
    perfect, measure VI, 3MP) + `وْا۟` (3MP suffix), refs `103:3:6:1-3`.
    Mark-stripped: `وتواصوا`; recovered stem/base node: `تواص`.
12. `P[3.7] بِٱلْحَقِّ`: `بِ` + `ٱلْ` + `حَقِّ` (lemma `حَقّ`, root
    `ح ق ق`, masculine genitive), refs `103:3:7:1-3`. Mark-stripped:
    `بٱلحق`.
13. `P[3.8] وَتَوَاصَوْا۟`: a second, distinct occurrence with the same
    three-part vector as `P[3.6]`, refs `103:3:8:1-3`.
14. `P[3.9] بِٱلصَّبْرِ`: `بِ` + `ٱل` + `صَّبْرِ` (lemma `صَبْر`, root
    `ص ب ر`, masculine genitive), refs `103:3:9:1-3`. Mark-stripped:
    `بٱلصبر`.

Morphology supplies no mood value for the perfect verbs and no explicit voice
value for them. Those fields remain open rather than being filled by inference.
The four perfect predicates all carry 3MP control/suffix marking; measures are
IV for `ءَامَنُوا۟`, unmarked in the supplied measure field for `عَمِلُوا۟`,
and VI for both `تَوَاصَوْا۟` occurrences.

### Supplied syntax as participant structure

- `SA-SYN-001` (`ae:v3:s103:001:pass1:attach:a1`): oath `وَ` governs
  `ٱلْعَصْرِ`; grammatical head is the particle, complement is the genitive
  noun. A semantic speaker is not supplied.
- `SA-SYN-002a` (`...002...a1`): `إِنَّ -> ٱلْإِنسَٰنَ`, particle complement;
  the human carrier is the governed `ism`.
- `SA-SYN-002b` (`...002...a2`): `إِنَّ -> خُسْرٍ` through `فِى` inside the
  predicate; `فِى` governs the genitive complement.
- `SA-SYN-002c` (`...002...a3`): `إِنَّ -> خُسْرٍ` as predication;
  `لَفِى خُسْرٍ` supplies the predicate. The grammatical controller and the
  affected/predicated human occupant remain distinct roles.
- `SA-SYN-003a` (`...003...a1`): `إِلَّا -> ٱلَّذِينَ`; the relative plural
  group is excepted, and the supplied scope continues from `ءَامَنُوا۟`
  through `بِٱلصَّبْرِ`.
- `SA-SYN-003b` (`...003...a2`): `ءَامَنُوا۟ -> وَعَمِلُوا۟`, coordinated
  predicates. Their 3MP controller corefers with `ٱلَّذِينَ`, while the two
  performances remain separate events.
- `SA-SYN-003c` (`...003...a3`): `وَعَمِلُوا۟ -> ٱلصَّٰلِحَٰتِ`, explicit
  direct object; the group is controller/initiator and the feminine plural
  object is affected/performed content.
- `SA-SYN-003d` (`...003...a4`): `وَعَمِلُوا۟ -> وَتَوَاصَوْا۟`, another
  coordinated predicate.
- `SA-SYN-003e` (`...003...a5`): first `تَوَاصَوْا۟ -> بِٱلْحَقِّ`; `بِ`
  governs the first content complement.
- `SA-SYN-003f` (`...003...a6`): first `تَوَاصَوْا۟ ->` second
  `وَتَوَاصَوْا۟`, coordinated identical performances at distinct positions.
- `SA-SYN-003g` (`...003...a7`): second `تَوَاصَوْا۟ -> بِٱلصَّبْرِ`; `بِ`
  governs the second content complement.

The exception group is one continuous referent in `SA`, but occupies exact
rotating roles: excepted group, relative antecedent, controller of four
perfect predicates, initiator and affected co-participant in each reciprocal
measure-VI event, and possessor of four 3MP suffixes. The reciprocal events
make members both advising and advised participants; this role reciprocity is
supplied by the lexical `و ص ي/B003` tuple below, while surface coreference is
preserved separately.

The four-predicate complement vector is:

```text
ءَامَنُوا۟        -> no explicit surface content complement
عَمِلُوا۟         -> direct object, definite FP accusative ٱلصَّٰلِحَٰتِ
تَوَاصَوْا۟ #1    -> بِ + definite masculine genitive حَقّ
تَوَاصَوْا۟ #2    -> بِ + definite masculine genitive صَبْر
```

This is an exact vacancy/supply sequence, not a claim that the absent first
content is identical to a later complement.

## Exact-contact closure

### Surface-internal circuits

1. `LM-EXACT-01`: every orthographic word contains its own supplied morpheme
   sequence. These fourteen composition circuits remain prior to semantics.
2. `LM-EXACT-02`: mark-stripped `إِنَّ -> إن` occurs contiguously inside the
   distinct adjacent carrier `ٱلْإِنسَٰنَ -> ٱلإنسن`, and inside its stem
   `إِنسَٰنَ -> إنسن`. The particle and the noun remain typed nodes: no
   accusative-particle function is imported into the human stem, and no human
   sense is imported into the particle.
3. `LM-EXACT-03`: the complete supplied emphatic prefix `لَ -> ل` is contained
   in `لَفِى`, in `إِلَّا`, in each written article, in `ٱلَّذِينَ`, and in
   several later stems including `عَمِلُ` and `صَّٰلِحَٰتِ`. Each contact has
   initial payload only `[letter-order, container, position]`.
4. `LM-EXACT-04`: the complete article morpheme occurs five times as DET:
   `P[1.1]`, `P[2.2]`, `P[3.5]`, `P[3.7]`, `P[3.9]`. Strict-written forms split
   into three `ٱلْ` and two `ٱل`; mark-stripped they converge as `ٱل`. The same
   form begins `ٱلَّذِينَ`, but that whole carrier is REL, not a DET
   construction. Formal containment and grammatical identity stay separate.
5. `LM-EXACT-05`: `وَ -> و` has four prefix occurrences: oath particle at the
   first passage character and three conjunctions in line 3. Its grammatical
   vector is `[P(oath), CONJ, CONJ, CONJ]`. The same one-letter supplied form is
   also contained in every plural suffix `وا/وْا`, inside `تواص`, and in the
   larger verbal carriers. Those contacts do not make suffix, stem, conjunction,
   and oath one role.
6. `LM-EXACT-06`: the suffixes `وا۟` at `P[3.3-4]` and `وْا۟` at
   `P[3.6,3.8]` retain two strict-written pairs. After mark stripping all four
   are `وا`. That complete two-letter form is also internal to recovered
   `تواص` at both recommendation positions. Suffix plurality and stem-internal
   letters remain distinct.
7. `LM-EXACT-07`: the complete preposition `بِ -> ب` occurs as prefix at both
   recommendation complements and as the middle base letter inside `صَبْر`.
   The final carrier therefore has one prefixed `ب` and a second typed `ب`
   inside its stem. Government is attached only to the prefix node.
8. `LM-EXACT-08`: `فِى` is an exact supplied morpheme contained after `لَ` in
   `لَفِى`; its mark-stripped `فى` must not be silently merged with lexical-file
   spellings `في` using `ي`.
9. `LM-EXACT-09`: `وَتَوَاصَوْا۟` is strictly identical at `P[3.6]` and
   `P[3.8]`; their conjunction, stem, suffix, aspect, measure, person, number,
   and group controller all recur. Their complements differ exactly as
   `بِٱلْحَقِّ` versus `بِٱلصَّبْرِ`. This yields invariant frame plus content
   delta, not event identity.
10. `LM-EXACT-10`: the line-final surface bases `عصر`, `خسر`, `صبر` recur as
    explicit morphology lemmas and as complete lexical forms in their own
    records. `عمل` is recovered inside `وعملوا`; `تواص` is recovered inside
    both `وتواصوا`; `حق` is recovered inside `بالحق`; `صبر` inside `بالصبر`.
    `صالح` reaches the inflected `صالحات` through the supplied root/morphology
    and lexical base nodes, while strict mark-stripped spelling differences are
    retained. `ءامن` and lexical `آمن` remain spelling variants rather than an
    unmarked exact identity.

### The `لا` inside `إِلَّا` circuit

`LM-EXACT-LA`: mark-stripped `إِلَّا -> إلا` contains the complete supplied
negative form `لا` at its ending. This contact is formal; exception and
negation remain different typed relations. Every lexical assertion licensing
`لا`, including an attached `ولا`, is carried into the circuit intact:

- `ح ق ق/B009`: `طعنة محتقة أي لا زيغ فيها وقد نفذت`.
- `ح ق ق/B012`: the beast is carried `على ما يتعبه ولا يطيقه`.
- `ح ق ق/B014`: `الأحق من الخيل الذي لا يعرق`.
- `خ س ر/B003`: `ولا تخسروا الميزان`.
- `خ س ر/B005`: `الخناسير الهلاك لا واحد له`.
- `ص ب ر/B006`: `أم صبور أمر لا منفذ له عنه`.
- `ص ب ر/B011`: `اشتريت الشيء صبرة أي بلا وزن ولا كيل`.
- `ع ص ر/B005`: `ما بينهما عصر ولا يصر أي ما بينهما مودة ولا قرابة`.
- `ع م ل/B007`: `لا تتعمل ... لا تتعن`; `لا تعمل أي لا تتعن`.

Each complete tuple contributes its own absent deviation, absent capacity,
absent sweat, prohibited scale-loss, absent singular, absent outlet, absent
measure, absent relation, or prohibited exertion. None of these predicates is
asserted of the surface exception particle. They remain live interfaces for
later vacancy comparison.

### Ordered passage boundaries

`SA-BOUNDARY`: all three supplied lines end in a rooted noun whose final
consonant is `ر`, and all three are genitive under different local relations:

```text
line 1: وَ + ٱل + عَصْرِ   definite; oath government; ending رِ
line 2: خُسْرٍ             indefinite; فِى government; ending رٍ
line 3: بِ + ٱل + صَّبْرِ definite; بِ government; ending رِ
```

`LM-BOUNDARY-01`: the complete ending vector is
`[definite/genitive رِ, indefinite/genitive رٍ, definite/genitive رِ]`.
The first and third terms enclose the changed middle term. `LM-BOUNDARY-02`:
the affix-count vector on the terminal nouns is `[2,0,2]`; the root vector is
`[ع ص ر, خ س ر, ص ب ر]`; final `ر` stays fixed while the other consonants and
the governing relation change. `LM-BOUNDARY-03`: the first passage word and
last passage word are both three-morpheme `[functional prefix + DET +
masculine genitive stem]` carriers, with oath `و` changing to preposition `ب`
and `عصر` changing to `صبر`.

Line 1 begins and ends in its sole word. Line 2 begins with `إِنَّ` and ends in
the state complement. Line 3 begins with `إِلَّا` and ends in the second
recommendation content. The passage begins with a `و` whose supplied function
is oath and later returns to three `و` conjunctions. Lines 2 and 3 begin with
distinct hamza-initial particles; their exact shared opening is positional and
acoustic, not token identity.

### Exact source-to-source collision nodes

These nodes join complete source assertions but not their historical occupants:

- `الحق`: surface `بِٱلْحَقِّ`; `ء م ن/B002` has `إذعان النفس للحق على سبيل
  التصديق`; `ح ق ق/B001-B005,B007-B014` expose truth, obligation, right,
  dispute, establishment, protection, maturity, penetration, firmness, joint,
  exertion, completion, and step-matching tuples around the same root/form.
- `التصديق/صدق`: `ء م ن/B002` states `الإيمان التصديق`; `ح ق ق/B005` states
  `حققت قوله وظنه تحقيقا أي صدقت`. The shared confirmation schema is an `LM`;
  the believer and verifier are not thereby one occupant.
- `الإنسان`: surface human carrier; exact lexical participant in
  `ء ن س/B001,B003-B005`, `ص ب ر/B002`, `ص ل ح/B001`, and `ع ص ر/B008`.
  These respectively supply kind, familiarity, orientation, eye-image,
  coerced killing, repair, and choking/drinking tuples.
- `النفس`: `ء م ن/B001-B002` makes it tranquil or submitting to truth;
  `ء ن س/B006` names it through `ابن إنسك`; `ص ب ر/B001` holds it from panic;
  `ع ص ر/B009` supplies suffixed `نفسها` as the site of perceived maturity.
- `حبس`: exact operation in `ص ب ر/B001-B002` and `ع ص ر/B006`, with self,
  coercer, parent, property, living victim, and oath as competing controller or
  affected-role fillers.
- `العصارة`: `ع ص ر/B002` defines what flows from pressing; `ع ص ر/B007`
  makes it yield/gain; `ص ب ر/B008` makes the bitter drug an extract of a tree.
- `السحاب/السحائب`: rain-bearing or raining cloud in `ع ص ر/B003`; white,
  level, or step-stacked cloud in `ص ب ر/B010`.
- `الشتاء`: center in `ح ق ق/B011`; intensity of cold in `ص ب ر/B007`.
- `الليل`: member of the temporal pair in `ع ص ر/B001`; object connected to
  day in `و ص ي/B001`.
- `النون`: explicitly added in the `خنسرى/خيسرى` formation account of
  `خ س ر/B005` and explicitly added to `العصر` in the `عنصر` account of
  `ع ص ر/B011`. The two local derivations remain separate insertion tuples.
- `العمل` and `الصالح`: `ع م ل/B001` supplies intentional good and bad acts;
  its exact phrase `الأعمال الصالحة والسيئة` collides with the surface
  predicate-object sequence `عَمِلُوا۟ ٱلصَّٰلِحَٰتِ`; `ص ل ح/B001` supplies
  the opposed repair/corruption result field.
- `يعمل`: `و ص ي/B002` defines an instruction as advancement to another with
  what is to be acted upon, exposing a content-to-performance interface with
  `ع م ل/B001-B003`.
- `القوم`: distinct group occupants occur in dispute (`ح ق ق/B004`), completed
  livestock state (`ح ق ق/B013`), guarantor companionship and severe event
  (`ص ب ر/B003,B006`), reconciliation (`ص ل ح/B002`), rain reception
  (`ع ص ر/B003`), manual labor (`ع م ل/B006`), and reciprocal counsel
  (`و ص ي/B003`).
- `الناقة`: dependable carrier (`ء م ن/B001`), burden-ready or fattened animal
  (`ح ق ق/B008,B013`), and animal naturally formed for work (`ع م ل/B008`).
- `الشجرة`: bitter extract and sour fruit (`ص ب ر/B008-B009`) and the named
  `العصرة` tree (`ع ص ر/B013`).
- `الوسط`: the center of head/winter in `ح ق ق/B011` and the middle of the
  mountains in `ص ب ر/B017`.
- `الموت`: coerced holding until death in `ص ب ر/B002` and an instruction that
  continues after death in `و ص ي/B002`; terminal occupant versus vacated
  originator is a live vacancy mapping.
- `نقيض/خلاف/ضد`: explicit opposition operators occur across security/fear,
  familiarity/alienation, truth/falsehood, patience/panic, and
  repair/corruption. Each opposition keeps its own endpoints.

## Complete lexical actuality tuples and released ports

Every item below is a local `SOURCE_ACTUALITY` tuple. Semicolon-separated
source assertions remain locally conjoined only where the supplied branch
conjoins them. The listed ports are reusable `LM` interfaces and `LA`
affordances, not claims that another tuple fills them.

### Root `ع ص ر`, surface anchor `P[1.1]`

- `SA-LEX-ASR-B001` preserves `العصر الدهر`; `العصران الليل والنهار`;
  `العصران الغداة والعشي`; `العصر العشي`; `صلاة العصر`; `العصار الحين`;
  `جاءني فلان عصرا أي بطيئا`; and `نام وما نام لعصر`. Its complete tuple set
  exposes duration, paired phases, daily position, prayer position, delayed
  arrival, and a negated sleep-time as distinct local events. Ports: temporal
  container, ordinal phase, alternating pair, delayed participant, beginning,
  return.
- `SA-LEX-ASR-B002` preserves `ضغط شيء حتى يتحلب`; pressing grapes and oil;
  `عصرت العنب وعصرته إذا وليت عصره بنفسك`; `يعصرون الأعناب والزيت`;
  `العصارة ما سال عن العصر`; `العصارة ما تحلب من شيء تعصره`; `كل شيء عصر
  ماؤه فهو عصير`; `المعصرة ما يعصر فيه العنب`; `المعصار شيء كالمخلاة يجعل
  فيه العنب ويعصر`; and `العصر مصدر عصرت والمعصور الشيء العصير`. Atomic
  parameters: controller can undertake the pressing personally; material
  enters under pressure; press/bag can be medium; liquid flows out; pressed
  material and extracted product remain different states. Ports: force,
  vessel, material, flow path, product, residue, receiver.
- `SA-LEX-ASR-B003` keeps cloud and people events distinct: `المعصرات السحائب
  تعتصر بالمطر`; clouds come carrying rain; `السحابة المعصر التي تتحلب
  بالمطر`; `أعصر القوم إذا أتاهم المطر`; `عصر القوم أي مطروا`; and the
  supplied readings `يعصرون أي يأتيهم المطر` and `تعصرون بضم التاء أي
  تمطرون`. Controller/voice and recipient rotate among cloud, rain, and group;
  incoming carried content becomes falling/received rain.
- `SA-LEX-ASR-B004` preserves a wind that raises dust from earth toward sky as
  a column, dust shining in a round form, and `إعصار وعصار وهو أن تهيج الريح
  التراب فترفعه`. A second local event is scent rising behind a perfumed
  woman's hem: `لذيلها عصرة ... من فوح الطيب وهيجه`. Ports: wind/force,
  ground source, particulate or scent material, upward route, column/round
  form, trailing boundary.
- `SA-LEX-ASR-B005` preserves attachment and holding, `العصر الملجأ`,
  `العصر المنجاة والعصرة والمعتصر والمعصر`, taking refuge with a person or
  place, and `ما بينهما عصر ولا يصر أي ما بينهما مودة ولا قرابة`. Positive
  holding/refuge and explicitly absent bond remain opposite local states.
  Ports: endangered entrant, refuge, approach, boundary crossed, attachment,
  rescue, absent relation.
- `SA-LEX-ASR-B006` preserves `العصر الحبس`; `ما عصرك أي ما منعك`;
  extracting another's property from his hand; a parent preventing/holding a
  child's property; taking back a gift; `يعتصر يسترجع`; the one who takes from
  a thing; and `فلان عاصر إذا كان ممسكا`. Controller variants are blocker,
  parent, prior giver, and taker; affected variants are person, property, or
  gift; outgoing states are withheld, extracted, or returned.
- `SA-LEX-ASR-B007` preserves the opposed transfer direction `العصر العطية`;
  `يعصر فينا ... أي تعطي`; extract as a figure for good and giving; the one
  who takes a share; `العصارة الغلة`; and `يعصرون/تعصرون` as deriving yield
  from their land. Ports: giver, taker, productive ground, extraction,
  benefit, gift, gain. This remains separate from B006 even where the same
  formal extraction frame reverses direction.
- `SA-LEX-ASR-B008` preserves a person choking on food and then drinking water
  `قليلا قليلا ليسيغه`; the controller is the choked person, water is medium,
  throat/food supply the blockage, repeated small intake is route/measure, and
  swallowing is the result. The counterfactual line `لو بغير الماء حلقي شرق
  كنت كالغصان بالماء اعتصاري` retains its own wording and water contrast.
- `SA-LEX-ASR-B009` preserves the girl first reaching or nearing menstruation,
  reaching the increase/period of youth, seeing that increase `في نفسها`, and
  the account that she is confined in the house at that time. Ports:
  developing participant, perceived internal sign, threshold, before/after
  state, house boundary, controller of confinement left open.
- `SA-LEX-ASR-B010` preserves `عصر الزرع صار في أكمامه`; visible ears mark the
  state; the crop is secured `في غلفه` and containers. Crop is occupant,
  sheath/husk is boundary and container, entry is transition, protected state
  is result.
- `SA-LEX-ASR-B011` preserves `العنصر ... الأصل والحسب`; `كريم المعصر` at
  asking; `كريم العصير أي كريم النسب`; and the exact formal assertion
  `العنصر أصل الحسب ومما زيدت فيه النون وهو في الأصل العصر وهو الملجأ`,
  followed by return in affiliation to one's origin. Formal nodes are full
  `العنصر`, recoverable `العصر`, and inserted `ن`; genealogy/origin and refuge
  stay locally related exactly as asserted.
- `SA-LEX-ASR-B012` preserves `العصرة أيضا الدنية` and the repeated equation
  `هؤلاء موالينا عصرة أي دنية دون من سواهم`. Ports: dependent group,
  comparator group, lower relation, exclusion boundary.
- `SA-LEX-ASR-B013` is the complete named-object equation `العصرة شجرة`.
  Naming, tree occupant, and branch position remain active without importing
  pressing or refuge.
- `SA-LEX-ASR-B014` is `المعصور اللسان اليابس عطشا`: tongue is affected
  organ, thirst is condition, dryness is outgoing state. No pressing event is
  asserted in this tuple.
- `SA-LEX-ASR-B015` is `العصار الفساء`: a named bodily wind occurrence, with
  its body source and emission affordance left local.

### Root `ء ن س`, surface anchor `P[2.2]`

- `SA-LEX-INS-B001` preserves `الإنس خلاف الجن وسموا لظهورهم`; `الإنس البشر
  والواحد إنسي والجمع أناسي`; and `الإنس جماعة الناس والأناسي جماع`.
  Individual/collective number, visible appearance, human kind, and opposed
  kind are separate parameters.
- `SA-LEX-INS-B002` preserves seeing and hearing the thing, seeing fire from a
  side, hearing a sound, perceiving maturity and thereby knowing it, looking,
  examination, and sensing what causes suspicion. Sensor, visual/auditory
  medium, side, fire/sound/sign, epistemic result, and felt alarm are typed
  ports; one perception mode never replaces another.
- `SA-LEX-INS-B003` preserves `الأنس ... إذا لم يستوحش منه`; `الإيناس خلاف
  الإيحاش`; `الإنس خلاف الوحشة`; companion and everything one becomes
  familiar with; joy with a person; conversation/proximity; and the tame dog
  as opposite of biting/wild. Incoming alienation/avoidance becomes
  familiarity/joy only in its local event; companion, conversation, and tame
  animal are competing media or occupants.
- `SA-LEX-INS-B004` preserves a human-facing side of each paired thing, the
  supplied left/right disagreement, the side of a beast used for mounting and
  milking, the human side facing the other leg, and the bow side facing rider
  or archer. Ports: oriented object, paired sides, person, facing relation,
  approach/use side, opposed wild-facing side.
- `SA-LEX-INS-B005` preserves `إنسان العين صبيها الذي في السواد`; `إنسان
  العين المثال الذي يرى في السواد`; its plural `أناسي`; and the additional
  equation `الإنسان الأنملة`. Eye, black field, visible miniature/example,
  observer, fingertip, singular/plural, and image containment remain distinct.
- `SA-LEX-INS-B006` preserves the equations asking `كيف ابن إنسك` about the
  self, `ابن إنسك يعني نفسه`, and calling a person's intimate `ابن إنس فلان`
  or his chosen/private companion, friend, intimate, or table companion.
  Addressed man, self, questioner, intimate other, selection, and speech event
  are open ports.

### Root `خ س ر`, surface anchor `P[2.4]`

- `SA-LEX-KHSR-B001` preserves the general decrease assertion: `أصل واحد يدل
  على النقض`; `الخسر النقصان والخسران كذلك`; and `خسر إذا نقص ميزانا أو
  غيره`. Affected thing and measure can be open; incoming amount becomes a
  lesser amount.
- `SA-LEX-KHSR-B002` preserves the trader who loses in trade, laying out or
  losing from capital, loss in sale, `انتقاص رأس المال`, and a losing deal
  `غير مربحة`. Controller/participant is trader, medium is sale/trade/deal,
  capital is affected stock, expected profit is an absent result, and outgoing
  capital is reduced.
- `SA-LEX-KHSR-B003` preserves active scale reduction: `خسرت الميزان وأخسرته
  إذا نقصته`; measuring/weighing and making it deficient; reducing the thing;
  `ولا تخسروا الميزان`; and people reducing measure and weight. Ports: agent,
  scale or measure instrument, measured object, expected amount, removed
  amount, recipient of short measure, prohibition.
- `SA-LEX-KHSR-B005` preserves the formal assertion `رجل خنسرى وقالوا خيسرى
  في موضع الخسران النون والياء زائدتان`; `الخناسر` as the plural of `خنسر`
  and as low/weak people; and `الخناسير الهلاك لا واحد له`. Full forms,
  recoverable base around inserted `ن` or `ي`, plural, low/weak class, ruin,
  and explicitly absent singular remain separate nodes.

### Root `ء م ن`, surface anchor `P[3.3]`

- `SA-LEX-AMN-B001` preserves `الأمن ضد الخوف`; `أصل الأمن طمأنينة النفس
  وزوال الخوف`; trustworthiness against betrayal and heart stillness; `الأمان
  إعطاء الأمنة`; the inflectional line `أمن فلان يأمن أمنا وأمانا وأمنة فهو
  آمن`; entering another's protection; the secure dwelling; and the dependable
  she-camel whose fatigue or stumbling is trusted not to occur. Ports: fearful
  self/heart, giver of security, entrant, protecting person or enclosure,
  entrusted object, carrier, possible fatigue/stumble, tranquility and trust.
- `SA-LEX-AMN-B002` preserves `الإيمان التصديق`; `وما أنت بمؤمن لنا أي مصدق
  لنا`; `إذعان النفس للحق على سبيل التصديق`; and the believer who confirms a
  promise. Controller is confirmer/submitting self; object is report, promise,
  or truth; addressee/beneficiary may be explicit; incoming unresolved report
  becomes assented content.
- `SA-LEX-AMN-B003` preserves `قولنا في الدعاء آمين وتفسيره اللهم افعل`;
  `التأمين من قولك آمين`; long and short pronunciation; `كذلك فليكن`;
  `معناه استجب`; and `أمن فلان إذا قال آمين`. Speaker, prayer, requested act,
  respondent, desired realization, utterance carrier, and length variant are
  all live.

### Root `ع م ل`, surface anchor `P[3.4]`

- `SA-LEX-AML-B001` preserves `أصل واحد صحيح وهو عام في كل فعل يفعل`; `عمل
  عملا فهو عامل`; `كل فعل يكون من الحيوان بقصد`; and `الأعمال الصالحة
  والسيئة`. Controller is intentional animal/person; action and intention are
  local; good/bad outcome is a parameter rather than a merged act.
- `SA-LEX-AML-B002` preserves making another work, using another, requesting
  work, applying opinion/speech/spear, using brick in construction, and
  `أعمل فلان ذهنه ... إذا دبره بفهمه`. Controller changes among employer,
  requester, thinker, builder, and wielder; instrument/affected carrier changes
  among person, mind, opinion, speech, spear, and brick.
- `SA-LEX-AML-B003` preserves alms collectors who take alms, assignment to an
  office of the ruler, and `التعميل تولية العمل`. Appointer, appointed
  official, governed work, collected property, giver/recipient, and office are
  ports.
- `SA-LEX-AML-B004` preserves `العمالة أجر ما عمل`, worker's provision,
  `العملة والعمالة أجر العمل`, and `العمالة أجرته`. Performed work precedes
  compensation; worker is beneficiary; payer and measure remain open.
- `SA-LEX-AML-B005` preserves reciprocal dealing in sale and elsewhere:
  `عاملته وأنا أعامله معاملة`; two parties alternate initiative and response,
  with transaction object and outcome open.
- `SA-LEX-AML-B006` preserves workers using their hands in digging, lining,
  clay, or other kinds of work. Group, hands, material, ground, tool, repeated
  operation, and constructed result are ports.
- `SA-LEX-AML-B007` preserves the equations `لا تتعمل ... لا تتعن`; `سوف
  أتعمل في حاجتك أي أتعنى`; and `لا تعمل أي لا تتعن`. Need, exerting person,
  effort/burden, prohibition, and intended completion remain typed.
- `SA-LEX-AML-B008` preserves a man naturally disposed to work and the noble,
  excellent working she-camel `اليعملة/الناقة العملة`, explicitly derived
  from work. Disposition precedes repeated performance; animal/person and
  excellence remain variants.
- `SA-LEX-AML-B009` preserves `عامل الرمح وعاملته` as the shaft/chest portion
  near the spearhead and below the named neighboring part. Spear, head, shaft
  segment, adjacency, orientation, and thrust path are ports; no human worker
  is asserted.
- `SA-LEX-AML-B010` preserves an animal's working limbs/legs and `عاملة الفرس`
  as its far-seeing eye in the cited line. Animal, limb or eye instrument,
  locomotion or observation, distance, and perceived target are variants.
- `SA-LEX-AML-B011` is `طريق معمل أي لحب مسلوك`: road is a traversed medium,
  prior passage produces its worn state, and traveler/path endpoints remain
  open.
- `SA-LEX-AML-B012` preserves travelers called `بني العمل` when walking on
  their feet. Travelers, feet, route, origin/destination, and locomotion are
  ports.

### Root `ص ل ح`, surface anchor `P[3.5]`

- `SA-LEX-SLH-B001` preserves the root as opposite of corruption/badness;
  goodness of thing, man, and work; `الإصلاح نقيض الإفساد`; benefit and
  seeking repair; beneficence toward an animal; and repair of the human by the
  stated divine controller. Controller, affected person/thing/animal/action,
  incoming corruption, outgoing repaired state, benefit, and good/bad polarity
  remain exact parameters.
- `SA-LEX-SLH-B002` preserves reconciliation, mutual peacemaking, and the
  explicit removal of aversion between people. Former opponents are reciprocal
  participants; aversion/dispute is incoming relation; reconciliation removes
  it and creates a changed between-state.
- `SA-LEX-SLH-B003` is the exact fit equation `هذا الشيء يصلح لك، أي هو من
  بابتك`. Thing, addressee, addressee's category/door, and fit relation are
  ports; no moral repair is asserted.
- `SA-LEX-SLH-B004` preserves `صالح` and neighboring personal names, including
  the named prophet. Proper-name referent and derivational form stay local and
  do not inherit every repair relation.
- `SA-LEX-SLH-B005` preserves `صلاح` as a name for Mecca and `الصلح` as a river
  in Maysan, including the supplied pattern comparisons. Place, river, naming
  act, and formal measure are local nodes.

### Root `و ص ي`, repeated surface anchors `P[3.6]` and `P[3.8]`

- `SA-LEX-WSY-B001` preserves `أصل يدل على وصل شيء بشيء`; `وصيت الشيء وصلته`;
  `وصيت الليلة باليوم وصلتها`; connected plants; land with connected growth;
  one desert continuous with another; and `وصى الشيء يصي إذا اتصل ووصاه غيره
  وصله`. Ports: first thing, second thing, connector, contact boundary,
  night/day succession, growing medium, land/desert extension, before/after
  continuity.
- `SA-LEX-WSY-B002` preserves the testament/instruction as speech that is
  carried/connected; `وصيته توصية وأوصيته إيصاء`; `الوصاة كالوصية`;
  `الوصاية مصدر الوصي`; instruction after death; the instructed content;
  giving something for a beneficiary; appointing another as trustee; the exact
  role equation `الوصي الموصي والموصى إليه جميعا`; and `التقدم إلى الغير بما
  يعمل به مقترنا بوعظ`. Local tuple ports: originator, utterance carrier,
  content, admonition, beneficiary, recipient/trustee, prescribed action,
  death boundary, later performance. The same term can name originator and
  recipient exactly as asserted, without erasing their directional roles.
- `SA-LEX-WSY-B003` preserves all three reciprocal equations: `تواصى القوم إذا
  تواصلوا`; `تواصى القوم أي أوصى بعضهم بعضا`; `تواصى القوم إذا أوصى بعضهم
  إلى بعض`. Group members fill both origin and endpoint roles; each performance
  remains directional member-to-member, while the complete topology is
  reciprocal/distributed.
- `SA-LEX-WSY-B004` preserves the pasture event: when pasture complies with or
  suits grazing animals and they attain abundance, `وصى لها المرتع يصي وصيا`.
  Pasture is supplying medium, herd is receiver/affected participant,
  compliance/fit is interface, feeding route is implicit/open, and abundance
  is result.

### Root `ح ق ق`, surface anchor `P[3.7]`

- `SA-LEX-HQQ-B001` preserves `الحق نقيض الباطل`; `أصل الحق المطابقة
  والموافقة`; verifying a matter until becoming certain; and `الحقيقة خلاف
  المجاز`. Belief, statement, or act can be the matching carrier; stable matter
  is referential endpoint; mismatch/falsehood and figurative status are
  explicit counterpositions; certainty is result.
- `SA-LEX-HQQ-B002` preserves `حق الشيء وجب`; being `حقيق بكذا ومحقوق به`;
  causing a thing to be required; deserving it; and the stated use across
  obligatory, necessary, and permissible. Thing, obligated person, imposer,
  entitlement, prior eligibility, and resulting requirement remain distinct.
- `SA-LEX-HQQ-B003` preserves a specific owned right: `إنك لتعرف الحقة عليك`;
  `الحق واحد الحقوق والحقة أخص منه، هذه حقتي أي حقي`; ownership/claim against
  a purchaser; and one party being more entitled to return. Claimant, obligated
  counterparty, object, recognized burden, comparative priority, and return are
  ports.
- `SA-LEX-HQQ-B004` preserves two parties each claiming right, disputing, group
  contention, and `حاققته فحققته أي خاصمته في الحق فغلبته`. Each party is
  claimant and opponent; claim content can recur; dispute is medium; victory is
  one supplied outcome, not a guarantee for every contention.
- `SA-LEX-HQQ-B005` preserves certainty about a matter; `حققت قوله وظنه
  تحقيقا أي صدقت`; a man saying `هذا الشيء هو الحق`; and `أحققت كذا أي أثبته
  حقا أو حكمت بكونه حقا، ليحق الحق`. Controller variants are investigator,
  confirmer, speaker, judge, or evidence-presenter; object variants are matter,
  saying, supposition, or truth claim; outgoing states are confirmed,
  established, judged, or made manifest.
- `SA-LEX-HQQ-B007` preserves the thing a man is obligated to protect, with
  banner, sanctity, courtyard, and what requires defense as supplied variants:
  `حامي الحقيقة إذا حمى ما يحق عليه أن يحميه`; `الحقيقة ما يحق على الرجل أن
  يحميه`; `فلان يحمي حقيقته`. Defender, protected object/place, assailing force,
  boundary, obligation, and successful/failed defense are ports.
- `SA-LEX-HQQ-B008` preserves the she-camel/young camel completing three years
  and entering the fourth, thereby deserving/capable of burden or riding; the
  female name `حقة`; and the camel reaching its mating time. Animal, age
  threshold, prior immature state, burden/rider, capacity, use, and scheduled
  time remain exact.
- `SA-LEX-HQQ-B009` preserves `طعنة محتقة إذا وصلت إلى الجوف`; `لا زيغ فيها
  وقد نفذت`; and a penetrating thrust contrasted in the branch description
  with a wound that injures without penetrating. Weapon/force, straight route,
  surface boundary, interior, wounded body, deviation vacancy, penetration,
  and nonpenetrating outcome are ports.
- `SA-LEX-HQQ-B010` preserves tightly woven cloth, firm speech, and
  `أحققت الأمر إحقاقا إذا أحكمته وصححته`. Weaver/speaker/corrector, threads or
  words or affair, joining operation, looseness/error as incoming state, and
  firm/correct result are variants.
- `SA-LEX-HQQ-B011` preserves `الحق ملتقى كل عظمين`; wooden/ivory cases;
  hip/ankle sockets; door socket; exact center in `حاق الرأس` or `حاق الشتاء`;
  spider web; and `مطابقة رجل الباب في حقه`. Ports: two bones, joint,
  fitted member, receiving socket/container, center, enclosure, web, exact
  placement, motion around a pivot.
- `SA-LEX-HQQ-B012` preserves `الحقحقة أرفع السير وأتعبه للظهر`; forcing a
  beast or weak participant along at what exhausts him and `لا يطيقه`; and
  severe travel. Driver/force, animal/weak affected participant, route, pace,
  back, capacity boundary, exhaustion, and inability are exact parameters.
- `SA-LEX-HQQ-B013` preserves a camel becoming fat in spring; a camel deserving
  the completed fattened state; a people's livestock becoming fat; and the
  stock reaching the end/completion of fatness. Animal or herd, spring input,
  growth process, owner group, threshold, strength, and completed state are
  ports.
- `SA-LEX-HQQ-B014` preserves the horse that does not sweat; `الأحق أن يطبق
  هذا ذاك`; the hind hoof placed in the position of the fore hoof; and the
  horse becoming lean. Horse, fore/hind limbs, prior footprint, exact target
  position, repeated gait, sweat vacancy, and bodily state are distinct.

### Root `ص ب ر`, surface anchor `P[3.9]`

- `SA-LEX-SBR-B001` preserves `الصبر نقيض الجزع`; `الصبر حبس النفس عن الجزع`;
  `صبرت نفسي أي حبستها`; and `حبس النفس على ما يقتضيه العقل والشرع`.
  Controller and affected participant can be the same self; panic is blocked
  outgoing response; reason/law supply requirement; steadfast held state is
  result. This voluntary/reflexive vector remains distinct from B002.
- `SA-LEX-SBR-B002` preserves `المصبورة المحبوسة على الموت`; installing a
  human for killing; holding a living being until it is shot; compelling an
  oath; `قتل صبر ويمين صبر`; and `الصبر الإكراه`. Coercer/ruler/killer is
  controller; living participant/oath-taker is affected without supplied
  consent; restraint is medium; death or compelled oath is result.
- `SA-LEX-SBR-B003` preserves `الصبير هو الكفيل`; `صبرت بفلان إذا كفلت به
  فأنا به صبير`; and the group's guarantor who remains with them in their
  affairs. Guarantor, guaranteed person, group, obligation, co-presence,
  duration, affair, and possible default are ports.
- `SA-LEX-SBR-B004` preserves `صبر كل شيء أعلاه`; sides of vessel and grave;
  and `الصبر جانب الشيء`. Contained thing/body, upper edge, side boundaries,
  interior/exterior, fill level, and crossing are ports.
- `SA-LEX-SBR-B005` preserves hard thick stone, stones, gravel-bearing land,
  and `أم صبار` as lava field or thick rock. Material, hardness, thickness,
  ground distribution, resistance, weight, and passage over it are ports.
- `SA-LEX-SBR-B006` preserves a group falling into a great/severe event;
  `أم صبار الحرب والداهية الشديدة`; and `أم صبور أمر لا منفذ له عنه`.
  Group is affected; event/war/calamity encloses; exit is explicitly absent;
  endurance, rescue, or termination remain open outcomes.
- `SA-LEX-SBR-B007` preserves `صبارة الشتاء شدة برده` and arrival in the
  intense cold of winter. Winter is temporal container, cold is force,
  arriving person is affected, and center/edge and relief remain open.
- `SA-LEX-SBR-B008` preserves `الصبر بكسر الباء عصارة شجرة` and the bitter
  medicine. Tree is material source, extract is product, bitterness is sensory
  state, medicine is use/medium, patient and effect remain open.
- `SA-LEX-SBR-B009` preserves `الصبار بضم الصاد` as a tree fruit more sour than
  the named comparator, with a broad red stone, and the equation to tamarind.
  Tree, fruit, seed, sour taste, eater, and bodily result are ports.
- `SA-LEX-SBR-B010` preserves a level cloud over dense cloud, a white cloud,
  cloud that piles part over part in steps, and white clouds. Layer, lower
  dense medium, upper white medium, vertical direction, step sequence, rain or
  dissipation remain open.
- `SA-LEX-SBR-B011` preserves the broad thin table sheet spread beneath food;
  a heap of food with some above some; and buying a heap `بلا وزن ولا كيل`.
  Supporting sheet, food, stacked direction, buyer/seller, unmeasured amount,
  scale vacancy, value, and later division are ports.
- `SA-LEX-SBR-B012` preserves `فليصطبر معناه فليقتص` and the exact role
  equation `أقاد السلطان فلانا وأقصه وأصبره بمعنى واحد إذا قتله بقود`.
  Ruler is controller, condemned person affected, prior offense supplies
  antecedent, equivalence/retaliation is relation, killing is result.
- `SA-LEX-SBR-B016` is the named-group assertion `الصبر أيضا بطن من غسان`.
  Group/name/genealogical membership are local; restraint is not imported.
- `SA-LEX-SBR-B017` preserves `الصبير الجبل` and `الصبير الأقدر وهو الوسط من
  الجبال`. Mountain and its middle/central member, surrounding mountains,
  height, route, and viewpoint are ports.
- `SA-LEX-SBR-B018` preserves `أصبر سد رأس الحوجلة بالصبار وهو السداد` and
  `الصبار صمام القارورة`. Container, neck/top, stopper, insertion controller,
  sealing operation, contained material, pressure, leakage vacancy, and later
  removal are ports.

## Passage actuality continuations

`SA-PATH-01`: `ٱلْإِنسَٰنَ` is the affected/predicated occupant of the loss
state. `إِلَّا ٱلَّذِينَ` creates the supplied exception relation to a plural
group; it does not erase the first predication or make the category token and
group token numerically identical.

`SA-PATH-02`: `ٱلَّذِينَ` corefers with the four 3MP verbal controllers and
pronoun suffixes. The exact occurrence chain is:

```text
relative group
-> believes/assents occurrence
-> performs occurrence with explicit object
-> reciprocal recommendation occurrence #1 with truth-content
-> reciprocal recommendation occurrence #2 with patience-content
```

Coordination supplies ordered co-predication, not causal order. Each perfect
performance retains its own controller vector. The two recommendation events
have identical frame but separate event IDs and content complements.

`LM-PATH-01`: lexical `و ص ي/B003` maps the reciprocal topology of each surface
measure-VI event: members advise some members toward other members. This maps
role schema, not the historical identity of any lexical example group.

`LM-PATH-02`: the surface progression of explicit content occupancy is
`[open, direct object, prepositional content, prepositional content]`.
`و ص ي/B002` exposes content, recipient, later action, and originator ports;
`ع م ل/B001` exposes intentional performance; `ء م ن/B002` exposes assented
report/promise/truth; `ح ق ق/B005` exposes confirmed/established content. Every
possible continuation is retained as a mapping or assembly below, never as a
new source event.

## Canonical latent mappings

Each `LM` below is canonicalized by member tuple IDs and exact payload. A tuple
can occur in several mappings because the payload differs. Parameter changes
are part of the mapping rather than evidence against it.

### Content, truth, speech, and performance

- `LM-CONTENT-01`:
  `AMN-B002[الإيمان التصديق; إذعان النفس للحق] -> confirmation schema ->
  HQQ-B001[matching/certainty] -> HQQ-B005[confirm, establish, judge]`.
  Invariant: a content carrier is related to a confirming participant and
  changes from unresolved/unconfirmed to assented, certain, established, or
  judged. Deltas: controller is submitting self, investigator, speaker, judge,
  or evidence-presenter; content is report, promise, matter, saying,
  supposition, or truth; social addressee is supplied only in some tuples.
- `LM-CONTENT-02`: the exact equation node `التصديق` links `AMN-B002` to the
  `صدقت` result in `HQQ-B005`. This mapping is narrower than general semantic
  similarity: it carries the equation/confirmation payload and exact source
  phrases.
- `LM-CONTENT-03`:
  `WSY-B002[instruction speech -> another -> what is acted on] -> carried
  content schema -> AML-B001[intentional act]`. The original utterance and the
  later action are separate occurrences. Deltas: speaker may still be present
  or vacated after death; recipient may also be trustee; action controller is
  the recipient rather than necessarily the originator; success is open.
- `LM-CONTENT-04`:
  `WSY-B002[one-way testament/instruction] <-> WSY-B003[member-to-member
  reciprocal counsel] <-> P[3.6]/P[3.8][two reciprocal performances]`.
  Invariant ports are origin, content, carrier, endpoint, and later response.
  Parameters change from one-way to reciprocal, single performance to
  distributed performances, open content to `حق` or `صبر`, and possible death
  boundary to no supplied death boundary.
- `LM-CONTENT-05`: `HQQ-B010[firm speech/tight construction]` maps speech-form
  firmness while `HQQ-B001/B005` map correspondence and confirmation. A firm
  carrier and a true/established content are independent axes; the mapping
  preserves that neither source equates them automatically.
- `LM-CONTENT-06`: `AMN-B003[آمين request -> response/realization]` and
  `WSY-B002[instruction -> later action]` share an utterance, addressed
  endpoint, desired performance, and not-yet-realized result. Deltas are
  request versus instruction, respondent versus trustee/recipient, long/short
  pronunciation versus post-death persistence, and desired divine act versus
  prescribed human act.

### Work, repair, fit, and result

- `LM-WORK-01`: the exact lexical phrase `الأعمال الصالحة والسيئة`
  (`AML-B001`) maps the base/inflection sequence in
  `P[3.4] عَمِلُوا۟ P[3.5] ٱلصَّٰلِحَٰتِ`. Invariant is intentional actor plus
  action carrying a good/bad result parameter. Surface actuality supplies the
  good-object form only; the lexical counterfield retains good and bad.
- `LM-WORK-02`: `AML-B001[intentional act] -> SLH-B001[repair versus
  corruption]`. The mapping carries action/result polarity; it does not claim
  that every intended act repairs or that every repair has the surface group
  as controller.
- `LM-WORK-03`: `AML-B002[make/use/request work]`, `AML-B003[appoint to
  office]`, and `AML-B006[manual workers]` share controller, worker/instrument,
  task, material/object, and result ports. Deltas: initiative belongs to
  employer, ruler, or worker; medium is person, mind, hand, spear, word, or
  brick; consent and compensation are unsupplied except where another tuple
  supplies them.
- `LM-WORK-04`: `AML-B003[appointed/collecting work] -> AML-B004[wage or
  provision after work]`. Office and compensation are separate tuples joined
  by performed-work interface; payer, amount, and fair measure remain vacant.
- `LM-WORK-05`: `SLH-B003[this thing fits you/is of your category]`,
  `WSY-B004[pasture suits herd and yields abundance]`, and
  `HQQ-B001[matching/accord]` instantiate a two-place fit relation. Deltas:
  abstract stable referent, human category/door, and animal-supporting pasture;
  outcome is certainty, suitability, or abundance.
- `LM-WORK-06`: `SLH-B002[remove aversion]`, `HQQ-B004[reciprocal dispute]`,
  `AML-B005[reciprocal dealing]`, and `WSY-B003[reciprocal counsel]` preserve a
  two-or-more-party between-state. Parameters change among opposition,
  transaction, counsel, and reconciliation; initiative distribution and
  result change among contention/victory, exchange, circulated content, and
  removed aversion.

### Holding, compulsion, and release

- `LM-HOLD-01`: `SBR-B001[self holds self from panic] <-> SBR-B002[coercer
  holds living participant to death/oath]`. Topology is controller -> holding
  relation -> affected participant -> blocked/reached outcome. Deltas are
  controller identity, reflexivity, consent, force, required norm, and result.
  These deltas are atomic and never averaged.
- `LM-HOLD-02`: `ASR-B006[parent/giver/taker withholds or retrieves property]
  <-> SBR-B002[ruler restrains person]`. Invariant is changed controller
  preventing an affected occupant from retaining/moving freely. Deltas:
  person versus property, death/oath versus returned gift, coercive bodily
  force versus possessive control.
- `LM-HOLD-03`: `SBR-B018[stopper seals container]`, `ASR-B010[crop secured in
  husk]`, `SBR-B004[vessel/grave sides]`, and `SBR-B006[event with no exit]`
  share inside/boundary/outside ports. Deltas: inserted closure versus grown
  enclosure versus static sides versus total situational enclosure; contained
  liquid/crop/body/group; leakage, exposure, crossing, or exit as consequence.
- `LM-HOLD-04`: `ASR-B005[person enters refuge]` reverses the value of
  enclosure relative to `SBR-B006[group trapped with no exit]`: the same
  outside-to-inside/boundary topology changes initiative, desirability, and
  result from rescue to inescapability.
- `LM-HOLD-05`: `HQQ-B012[driver exceeds capacity]`, `SBR-B002[coercer fixes
  victim]`, and `AML-B007[person exerts effort]` share force, affected body,
  effort/capacity, and result ports. Deltas: imposed versus self-undertaken
  exertion, prohibition versus performance, exhaustion/death versus intended
  completion.
- `LM-HOLD-06`: `ASR-B008[small repeated water intake releases blocked food]`
  maps a release mechanism against the holding field. The route opens by
  measured repetition; water is medium; unlike B006/B018, the desired result
  is passage rather than continued closure.

### Pressure, extraction, transfer, and amount

- `LM-EXTRACT-01`: `ASR-B002[pressure -> flowing extract]`,
  `ASR-B006[taker -> property extracted/withheld]`, and
  `ASR-B007[land/thing -> yield, gift, or share]` preserve source, operation,
  outgoing product/property, taker/receiver, and aftermath. Parameters change
  from physical pressure to possessive force or productive exploitation; from
  liquid to property/gift/yield; from self-controlled work to another's loss or
  a recipient's benefit.
- `LM-EXTRACT-02`: exact `العصارة` maps `ASR-B002[what flows from pressing]`,
  `ASR-B007[yield/gain]`, and `SBR-B008[bitter tree extract]`. Material source,
  separation, product, sensory/economic use, and receiver are preserved; tree
  extract is not asserted to be a commercial gain, and yield is not asserted
  bitter.
- `LM-EXTRACT-03`: `ASR-B003[cloud releases rain]` maps the material-transition
  topology of B002, with cloud as carrier, rain as content/product, people or
  ground as receiver, and weather rather than human pressure as controller.
  The lexical reading variants preserve whether the group is rained upon or
  the clause presents raining.
- `LM-EXTRACT-04`: `KHSR-B001[general decrease]`, `KHSR-B002[capital loss]`,
  and `KHSR-B003[agent reduces scale/measure]` share incoming quantity ->
  decrease -> lower outgoing quantity. Deltas: generic state, trader's result,
  or deliberate measuring act; capital, scale, measure, or other object;
  absent profit versus short-delivered amount.
- `LM-EXTRACT-05`: `SBR-B011[heap sold without weight or measure]` meets
  `KHSR-B003[measure actively reduced]` at a vacancy mechanism. Both expose
  quantity and transaction, but one has no measurement event while the other
  has a manipulated measurement event. Unmeasured is not equated with reduced.
- `LM-EXTRACT-06`: `AML-B004[wage after work]`, `ASR-B007[yield/gift]`,
  `KHSR-B002[profit/capital outcome]`, and `HQQ-B003[owned entitlement]` share
  a participant expecting or receiving value after a prior relation. Deltas:
  work, land, sale, or right as antecedent; wage, yield, profit, capital, or
  returned object as value; beneficiary, trader, owner, or claimant.

### Match, alignment, boundary, and route

- `LM-FIT-01`: `HQQ-B001[belief/saying/action matches stable referent]`,
  `HQQ-B011[door leg fits socket; bones meet]`, and
  `HQQ-B014[hind hoof occupies fore-hoof position]` share exact relation
  `member/carrier -> matching relation -> target/position`. Parameters change
  from propositional to fitted-object to sequential locomotor scale; target is
  reality, socket, joint, or prior footprint.
- `LM-FIT-02`: `INS-B004[side faces rider/archer]`, `AML-B009[spear segment
  lies by head]`, and `HQQ-B011[fitted member meets receiving place]` preserve
  oriented object, local side/segment, human or object endpoint, adjacency, and
  functional access. Facing, adjacency, and fitting remain separate relations.
- `LM-FIT-03`: `HQQ-B009[straight thrust crosses surface into interior]`,
  `AML-B009[spear portion below head]`, and `AML-B011[traversed road]` expose
  force/instrument/path/boundary/interior or destination. A projective assembly
  may place the spear as instrument, but no source says the lexical thrust used
  that named spear segment.
- `LM-FIT-04`: `ASR-B005[route into refuge]`, `SBR-B006[no outlet]`,
  `SBR-B017[mountain/middle]`, and `AML-B011/B012[walked road/walkers]` share
  traveler, route, terrain or enclosure, boundary, and destination. Direction
  and outcome vary among arrival, rescue, blocked exit, central position, and
  continued travel.
- `LM-FIT-05`: `INS-B005[small human image inside black eye]`,
  `SBR-B004[contents inside vessel sides]`, `ASR-B010[crop in sheath]`, and
  `HQQ-B011[member in case/socket]` preserve contained occupant, visible or
  receiving interior, boundary, scale, and possible insertion/removal. Image,
  body/crop, and fitted member are not occupants of one source event.

### Perception, body, animal, and material state

- `LM-SENSE-01`: `INS-B002[see/hear/sense -> know]`,
  `INS-B005[image visible in eye]`, and `AML-B010[far-seeing animal eye]`
  preserve sensor, organ/medium, target/sign, distance/side, and perceptual
  result. Modality changes among vision, hearing, felt alarm, and knowledge.
- `LM-SENSE-02`: `INS-B002[perceive maturity]` maps `ASR-B009[girl sees
  increased youth in herself]` through sensed sign -> recognized threshold.
  Deltas: observer may be an external plural group or the developing person;
  sign is general maturity or bodily increase; aftermath may include house
  confinement only in ASR-B009.
- `LM-SENSE-03`: `AMN-B001[heart becomes still as fear leaves]`,
  `AMN-B002[self submits/confirms]`, `INS-B003[alienation becomes familiarity]`,
  and `SBR-B001[self restrains panic]` share an inner participant and changed
  affective/cognitive state. Parameters are removal, assent, approach/joy, or
  blocked response; security, belief, familiarity, and patience remain distinct.
- `LM-ANIMAL-01`: `AMN-B001[dependable camel, failure not expected]`,
  `HQQ-B008[camel reaches load-bearing age]`, `HQQ-B013[animal/herd reaches
  full fatness]`, and `AML-B008[camel disposed to work]` share animal carrier,
  capacity, possible burden/work, state threshold, and reliability. Deltas:
  trust, age, bodily completion, and natural disposition.
- `LM-ANIMAL-02`: `INS-B004[mounting/milking side facing person]` gives the
  carrier an oriented access interface; `HQQ-B014[matched hoof placement]`
  supplies gait; `AML-B010[legs as working members]` supplies locomotor
  instruments. These map facets of animal operation without asserting one
  animal.
- `LM-MATERIAL-01`: `SBR-B005[hard stone/gravel ground]`,
  `HQQ-B010[tight cloth/firm construction]`, and
  `SBR-B018[solid stopper]` share resistance/firmness/material/boundary ports.
  Hardness, woven coherence, and sealing are different parameters and results.
- `LM-MATERIAL-02`: `SBR-B008[bitter extract]`, `SBR-B009[sour fruit]`,
  `ASR-B014[dry tongue from thirst]`, `ASR-B008[water relieves choking]`, and
  `ASR-B004[perfume plume]` preserve substance, sensory quality, body or air
  medium, reception, and aftermath. Bitter, sour, dry, water-mediated, and
  fragrant variants stay separate.

### Time, weather, succession, and layering

- `LM-TIME-01`: exact `الليل` connects `ASR-B001[night/day as temporal pair]`
  with `WSY-B001[connect night to day]`. The first supplies paired temporal
  members; the second supplies the connection operation. Neither alone asserts
  the full projected succession mechanism.
- `LM-TIME-02`: `ASR-B001[time/day/night/morning/evening/afternoon]`,
  `HQQ-B011[center of winter]`, `SBR-B007[intense winter cold]`,
  `ASR-B009[maturity threshold]`, and `HQQ-B008[age threshold]` share temporal
  container/position/before-after state. Scale changes from daily/epochal to
  seasonal to life-stage or age.
- `LM-WEATHER-01`: exact cloud nodes link `ASR-B003[rain-bearing/releasing
  cloud]` and `SBR-B010[white, level, stacked cloud]`. Parameters are content,
  vertical layer, density, color, release, and receiver.
- `LM-WEATHER-02`: `ASR-B004[wind raises dust/perfume]` and
  `SBR-B010[cloud layers rise/stack]` share upward direction and aerial medium;
  force, material, geometry, and outcome change from moving column/trail to
  persistent layers.
- `LM-WEATHER-03`: exact `الشتاء` links `HQQ-B011[center]` with
  `SBR-B007[cold intensity]`; one supplies ordinal/central position, the other
  force/condition. A center-of-intensity assembly is possible but not actual.

### Formal derivation, naming, and opposition

- `LM-FORMAL-01`: `KHSR-B005` and `ASR-B011` both explicitly name added `ن`.
  Their complete transformations differ: `خنسرى`/`خيسرى` have specified
  added `ن`/`ي` around a loss-family base, while `عنصر` has inserted `ن` into
  asserted base `العصر`. Full forms, bases, affixes, positions, and semantic
  outcomes are retained.
- `LM-FORMAL-02`: surface prefix/article/suffix succession and these lexical
  insertions share only a formal transformation interface. Attached `و`, `ل`,
  `ب`, `ٱل`, and `وا` have grammatical functions; lexical `ن`/`ي` change named
  forms. No affix meaning is transferred across them.
- `LM-NAME-01`: `ASR-B013[tree name]`, `SBR-B016[group name]`,
  `SLH-B004[personal name]`, and `SLH-B005[place/river names]` map the topology
  `form -> naming relation -> referent`. Referent class and scope differ; other
  root senses remain inactive in `SA` but available as separate assembly facets.
- `LM-OPPOSE-01`: the exact opposition schema compares
  `AMN-B001[security/fear; trust/betrayal]`, `INS-B001[human/jinn]`,
  `INS-B003[familiarity/alienation or avoidance]`, `HQQ-B001[truth/falsehood;
  literal/figurative]`, `SBR-B001[patience/panic]`, and
  `SLH-B001[repair/corruption]`. It preserves two poles and a typed relation;
  no endpoint from one pair replaces an endpoint from another.

## Changed-controller counterfields

The following tables re-enact operations under every supplied controller
change. Blank positions are typed vacancies, not permission to infer a filler.

| operation | source tuple | controller | affected participant/material | consent/initiative | result |
|---|---|---|---|---|---|
| hold | `SBR-B001` | self | same self/response | reflexive; norm-guided | panic held back |
| hold | `SBR-B002` | ruler/coercer/killer | living being or oath-taker | compelled | death or oath |
| hold/withhold | `ASR-B006` | parent, prior giver, taker | child's property, gift, another's property | controller initiative | retained or retrieved property |
| seal | `SBR-B018` | inserter | container opening/content | controller initiative | leakage/opening blocked |
| enclose | `ASR-B010` | not supplied | crop | not supplied | crop secured in husk |
| trap | `SBR-B006` | severe event/war as condition; agent open | group | involuntary | no outlet |

| content operation | source tuple | controller | content | endpoint | result |
|---|---|---|---|---|---|
| assent | `AMN-B002` | self/confirmer | report, promise, truth | addressee may be supplied | believed/confirmed |
| verify/establish | `HQQ-B005` | investigator/speaker/judge | matter, saying, claim | public/other endpoint open | certain/established/judged |
| request | `AMN-B003` | prayer speaker | desired act | respondent | response/realization requested |
| instruct | `WSY-B002` | originator | what is to be acted on | recipient/trustee | later act remains open |
| reciprocal counsel | `WSY-B003`; surface x2 | each group member | content | other members | circulation, response open |
| perform | `AML-B001`; surface | intentional actor/group | action | affected object/result | good/bad parameter; surface good-object supplied |

| force/transfer | source tuple | controller | medium | affected/output | result |
|---|---|---|---|---|---|
| press | `ASR-B002` | person, explicitly possibly self | press/bag | grapes/oil -> liquid | extract flows |
| rain/release | `ASR-B003` | cloud/weather role varies by reading | cloud/air | rain -> group/ground | rain arrives |
| raise | `ASR-B004` | wind | air | dust/perfume | column or trail |
| take/withhold | `ASR-B006` | parent/taker/giver | hand/property relation | property/gift | retrieval/retention |
| give/yield | `ASR-B007` | giver/land | extraction/land | gift/yield -> receiver | benefit/gain |
| reduce | `KHSR-B003` | measurer | scale/measure | measured amount | short amount |
| drive | `HQQ-B012` | driver | severe pace | animal/weak body | exhaustion beyond capacity |

## Vacancy-mechanism field

- `VAC-01`, surface: the first perfect predicate has no explicit content
  complement; the second has a direct object; the third and fourth have
  governed content complements. Consequence: later content forms cannot be
  backfilled into the first actuality, but they can serve as competing `LA`
  fillers.
- `VAC-02`, originator: `WSY-B002` allows instruction after death. The original
  speaker position becomes historically unavailable while content and
  recipient persist. `SBR-B002` ends the held participant in death instead;
  here death terminates the affected occupant rather than enabling his speech
  to continue. The shared terminal boundary changes the continuation.
- `VAC-03`, exit: `SBR-B006` explicitly has no outlet; `ASR-B005` supplies a
  refuge entered from outside; `ASR-B008` opens a blocked throat through small
  water increments; `HQQ-B009` crosses a body boundary without deviation.
  Absence, entrance, release, and penetration are distinct route outcomes.
- `VAC-04`, measure: `SBR-B011` lacks weight and measure; `KHSR-B003` contains
  an active but reduced measure; `KHSR-B002` lacks profit; `AML-B004` leaves
  wage amount open. Each vacancy has a different economic consequence.
- `VAC-05`, relation: `ASR-B005` explicitly has no affection or kinship between
  two parties; `SLH-B002` begins with aversion and removes it; `WSY-B003`
  supplies reciprocal content links; `HQQ-B004` supplies mutual claims. An
  absent bond, damaged bond, communication network, and contest network remain
  different between-states.
- `VAC-06`, capacity: `HQQ-B012` supplies inability to endure the imposed pace;
  `AMN-B001` supplies a dependable camel whose fatigue/stumble is trusted not
  to occur; `HQQ-B008` supplies newly reached carrying capacity. Incapacity,
  trusted nonfailure, and acquired capacity form a parameter counterfield.
- `VAC-07`, formal member: `KHSR-B005` explicitly says `الخناسير` has no
  singular. This blocks a singular-member continuation even though another
  supplied plural `الخناسر` has a singular relation. The two full forms stay
  distinct.
- `VAC-08`, deviation and sweat: `HQQ-B009` has no deviation in the penetrating
  path; `HQQ-B014` has no sweat in the horse. Both exact `لا` contacts expose
  absent properties but of different carriers and consequences.
- `VAC-09`, semantic initiators: the oath speaker in line 1, the agent/mechanism
  of line 2 loss, and any external recipient beyond the reciprocal line 3
  group are not supplied. They remain open roles.

## Projective latent assemblies

Every assembly below states its ordered functional roles and the source tuple
that supplies each role. A slash marks competing fillers, not a merger. Each
variant is allowed to finish through result and aftermath before any later
selection.

### `LA-01`: content confirmation, circulation, performance, and result

Canonical role spine:

```text
content/proposition
-> confirmer or perceiver
-> speech/instruction carrier
-> sender/receiver network
-> intentional performance
-> affected thing/relation
-> result and returned report
```

- Content fillers: report/promise/truth (`AMN-B002`), matter/saying/claim
  (`HQQ-B001,B005`), recommendation content `حق` or `صبر` (surface
  `P[3.7],P[3.9]`), prescribed action (`WSY-B002`), or requested act
  (`AMN-B003`).
- Confirmation fillers: submitting self (`AMN-B002`), investigator/judge
  (`HQQ-B005`), seeing/hearing knower (`INS-B002`), or no preconfirmation
  supplied.
- Carrier fillers: firm speech (`HQQ-B010`), testament/admonition
  (`WSY-B002`), reciprocal advice (`WSY-B003` plus the two surface
  performances), or prayer response formula (`AMN-B003`).
- Performance/result fillers: intentional act (`AML-B001`), assigned work
  (`AML-B003`), repair/corruption delta (`SLH-B001`), reconciliation
  (`SLH-B002`), confirmation of the prior saying (`HQQ-B005`), or open result.

`LA-01a`, truth-content route:
`unconfirmed content -> AMN-B002 assent -> WSY-B003 reciprocal carrying ->
AML-B001 intended act -> SLH-B001 repair/corruption result -> HQQ-B005 later
verification`. If later verification confirms the result, the content becomes
available for another reciprocal performance; when it returns to an already
visited content/network state, record one circulation cycle and stop. A failed
or corrupt result stays a distinct terminal variant.

`LA-01b`, patience-content route: `SBR-B001 self-holding operation` is projected
as content into `WSY-B003`; each member can receive the content, become the
controller of a fresh self-holding event, and continue or fail an
`AML-B001` act. The advised content and the new act of patience are different
occurrences. Competing outcomes are held response, panic released, intended
action completed, or capacity exceeded (`HQQ-B012`).

`LA-01c`, post-death route: originator forms an instruction (`WSY-B002`), death
vacates the originator, recipient/trustee retains the carrier, recipient
performs (`AML-B001`), and another participant verifies the result
(`HQQ-B005`). Mismatch is explicit if no recipient, content, or action filler
is supplied; the instruction persists as an unperformed carrier.

`LA-01d`, request route: speaker says `آمين` (`AMN-B003`), desired act occupies
the content slot, respondent/action controller remains differentiated, and a
later outcome can be perceived (`INS-B002`) and confirmed (`HQQ-B005`). The
source never equates request with instruction or response with performance, so
nonresponse remains a complete aftermath.

### `LA-02`: pressure, enclosure, flow, and reception

Canonical role spine:

```text
source material -> applied/natural force -> containing instrument or boundary
-> narrowed route -> separated output -> receiver/use -> residue/aftermath
```

`LA-02a`, pressed liquid: grapes/oil (`ASR-B002`) enter press/bag
(`ASR-B002`), self-controlled pressure acts, liquid flows, and receiver/use is
open. A stopper (`SBR-B018`) can project into the outlet: closed stopper retains
the liquid; removal releases it; leakage is the failed-boundary variant.

`LA-02b`, bitter extract: tree is source and bitter drug is actual product in
`SBR-B008`; `ASR-B002` supplies projected pressure/instrument; patient and
bodily result are open. The complete route ends in administered medicine,
unadministered stored extract, or leaked/lost extract. Bitterness remains a
sensory parameter, not a moral or truth parameter.

`LA-02c`, rain release: cloud (`ASR-B003`) occupies source/container, rain its
content, cloud/weather its controller, and group/ground the receiver. Layered
white cloud (`SBR-B010`) supplies competing upper/lower boundary structure.
Outcomes are retained rain, released rain reaching group, dispersed cloud, or
stacked cloud without a supplied release.

`LA-02d`, yield/gift: productive land (`ASR-B007`) fills source; work or
extraction fills force; yield/gift fills output; worker/recipient fills
receiver; wage (`AML-B004`) or profit/loss (`KHSR-B002`) fills aftermath.
Variants end in benefit, no profit, reduced capital, unpaid work, or unharvested
yield.

`LA-02e`, coerced property extraction: another's property (`ASR-B006`) is
material, taker/parent controller, hand/possession boundary, removal the route,
and taker the receiver. Mapping the physical press reveals a fit at
source-force-output but a mismatch at consent and product identity. The
aftermath branches into retained property, restored property, retrieved gift,
or loss to the prior holder.

`LA-02f`, choking release: blocked food/throat (`ASR-B008`) fills narrowed
route, repeated small water doses fill medium/measure, the person controls
application, and successful swallowing fills release. Projecting a stopper
here produces a mismatch because continued sealing defeats the supplied
result; projecting vessel sides only supplies measured containment of water.

### `LA-03`: enclosure, protection, entrapment, and fitted occupancy

Canonical role spine:

```text
occupant -> approach/insertion/growth -> boundary with inside/outside
-> retained state -> force at boundary -> release, protection, or damage
```

`LA-03a`, protective growth: crop (`ASR-B010`) grows into husk/container;
hardness (`SBR-B005`) or firm weave (`HQQ-B010`) can project as boundary
resistance; exposure force remains open. Result is protected crop; later
opening/harvest remains an unfilled release role.

`LA-03b`, chosen refuge: endangered entrant (`ASR-B005`) follows a route into
refuge; defender (`HQQ-B007`) guards banner/sanctity/courtyard boundary; hard
ground or mountain (`SBR-B005,B017`) supplies terrain. Outcomes are rescue,
successful defense, failed defense, or entrant unable to reach the boundary.

`LA-03c`, inescapable event: group (`SBR-B006`) is occupant, war/calamity the
enclosing condition, outlet explicitly absent. Projecting refuge changes the
desired direction but does not create an actual exit. Projecting the
penetrating path (`HQQ-B009`) creates a possible boundary-crossing role whose
fit or failure remains assembly data: penetration can open an exit, enter the
group's interior instead, or be blocked by resistance.

`LA-03d`, fitted socket: door leg/bone (`HQQ-B011`) is occupant/member, socket
or joint the receiving boundary, exact match the insertion condition, and
movement around joint or closed door the result. Stopper (`SBR-B018`) is a
competing fitted member: its result is sealing rather than articulation.

`LA-03e`, image enclosure: human image (`INS-B005`) occupies the black eye;
working/far-seeing eye (`AML-B010`) supplies perceptual performance; external
observer/target remains differentiated. The visible image can be perceived,
but it is not physically imprisoned, fitted like a door, or secured like crop;
those mismatches stay recorded.

`LA-03f`, grave/vessel sides: sides (`SBR-B004`) project a neutral boundary;
body, food, liquid, or stone can compete as occupant. Result changes with
occupant and closure: containment, burial, storage, spilling, or filled-to-edge
state. No occupant is selected.

### `LA-04`: route, orientation, penetration, and return

Canonical role spine:

```text
traveler/force -> bodily or material instrument -> oriented path/terrain
-> boundary or central position -> destination/interior -> aftermath/return
```

`LA-04a`, pedestrian route: travelers/feet (`AML-B012`) enter the worn road
(`AML-B011`), face a mountain/central mountain (`SBR-B017`) or hard gravel
ground (`SBR-B005`), and seek refuge (`ASR-B005`). Outcomes: arrival/rescue,
continued travel, exhaustion (`HQQ-B012` projected), or no outlet
(`SBR-B006`).

`LA-04b`, oriented animal route: rider-facing side (`INS-B004`) supplies access,
working legs (`AML-B010`) supply instruments, exact hoof replacement
(`HQQ-B014`) supplies positional sequence, and road (`AML-B011`) supplies
medium. Each new step moves hind hoof to prior fore-hoof position; a return to
an already represented generic step state records one gait cycle rather than
minting an infinite route.

`LA-04c`, thrust route: spear (`AML-B009`) supplies instrument and oriented
segment; straight penetrating stab (`HQQ-B009`) supplies force/path/boundary;
interior is destination; wound is aftermath. Variants: no deviation and full
penetration, surface injury without penetration, resisted path, or instrument
misalignment. No source assertion identifies the spear event with the stab
event, so the composite is `LA` only.

`LA-04d`, dust route: wind (`ASR-B004`) is force, dust material, ground origin,
skyward column path, air medium, and settling an open return. Perfume replaces
dust and a hem replaces ground; the output becomes a trailing plume rather
than column. Cloud layer (`SBR-B010`) can receive raised material only as a
projected endpoint, with fit/mismatch retained.

### `LA-05`: matching, suitability, and consequence

Canonical role spine:

```text
candidate member/content -> comparison or receiving position -> fit test
-> controller's decision/use -> stable fit or mismatch -> consequence
```

`LA-05a`, proposition fit: belief/saying/action (`HQQ-B001`) is candidate,
stable matter target, investigator (`HQQ-B005`) tester, and certainty or
rejection result. Firm speech (`HQQ-B010`) can carry the candidate but cannot
guarantee match.

`LA-05b`, object fit: door member/socket (`HQQ-B011`) supplies candidate and
target; hoof/prior footprint (`HQQ-B014`) supplies sequential match; human-
facing side (`INS-B004`) supplies orientation. Full fit yields closed door,
articulating joint, aligned step, or accessible side; mismatch yields jam,
misstep, or wrong-facing side.

`LA-05c`, ecological fit: pasture (`WSY-B004`) is candidate medium, herd
receiver, abundance result; `SLH-B003` supplies suitability-to-recipient
relation. Deltas end in nourishment/abundance, mere category fit without
feeding, or failed pasture fit.

`LA-05d`, social fit: thing/person and addressee's category (`SLH-B003`) receive
a selected intimate (`INS-B006`) or assigned worker (`AML-B003`) as competing
candidate. Results are companionship, appointment, rejected mismatch, or an
open test; no source states selection criteria.

### `LA-06`: measure, work, entitlement, and loss

Canonical role spine:

```text
prior stock/work/right -> measuring or adjudicating medium -> allocating agent
-> recipient/counterparty -> delivered amount -> gain/loss/claim aftermath
```

`LA-06a`, trade: capital and trader (`KHSR-B002`) enter sale/deal; reciprocal
dealing (`AML-B005`) supplies counterparty relation; scale (`KHSR-B003`) or no
measure (`SBR-B011`) competes as medium. Outcomes: profit, no profit, reduced
capital, short measure, or indeterminate heap amount.

`LA-06b`, wage: performed work/worker (`AML-B001,B004`) supplies antecedent and
beneficiary; owned entitlement (`HQQ-B003`) supplies claim; payer and measure
are open. Outcomes: paid provision, recognized unpaid claim, disputed claim
(`HQQ-B004` projected), or diminished wage (`KHSR-B003`).

`LA-06c`, yield: land/yield (`ASR-B007`) supplies productive stock; worker
(`AML-B006`) supplies labor; extracted amount becomes gain; capital-loss field
(`KHSR-B002`) supplies adverse comparison. Aftermath branches into abundance,
mere subsistence, no profit, or resource depletion.

`LA-06d`, rights contest: two claimants (`HQQ-B004`) dispute a specific right
(`HQQ-B003`); verification/evidence (`HQQ-B005`) supplies adjudicating medium;
one may prevail. Reconciliation (`SLH-B002`) can project as changed aftermath,
but victory and reconciliation remain different terminal states.

### `LA-07`: reciprocal group network and changed between-state

Canonical role spine:

```text
member A -> directional act/content -> member B
member B -> response/return act/content -> member A
-> distributed group state -> continuation or one recorded cycle
```

`LA-07a`, advice: `WSY-B003` supplies both directions; surface performance #1
supplies truth-content and #2 patience-content. Variant orderings are
truth-then-patience (surface order), truth circulating alone, patience
circulating alone, or distinct members carrying the two contents. A return to
the same member-content state records one cycle; no infinite chain is emitted.

`LA-07b`, dispute: `HQQ-B004` fills directional acts with claims and opposition;
each says the right is with him; victory is possible. Projecting truth-content
does not settle the contest until the verification/adjudication role
(`HQQ-B005`) is filled.

`LA-07c`, reconciliation: `SLH-B002` begins from aversion/dispute and changes
the between-state; reciprocal dealing (`AML-B005`) or counsel (`WSY-B003`) can
provide a medium. Results: removed aversion, transaction without reconciliation,
continued dispute, or renewed relation.

`LA-07d`, guarantor: guarantor (`SBR-B003`) remains with group in affairs;
reciprocal group network supplies multiple beneficiaries/obligees; instruction
(`WSY-B002`) can supply duty. Outcomes: obligation borne, default prevented,
default occurring, or guarantor position unfilled.

### `LA-08`: inner perception, assent, restraint, and response

Canonical role spine:

```text
external or internal sign/content -> sensory/cognitive medium -> self/heart
-> affective or epistemic change -> self-controlled response -> aftermath
```

`LA-08a`, fear-to-security: feared condition enters awareness (`INS-B002`),
security giver/refuge (`AMN-B001`) removes fear and stills heart, self then
holds panic (`SBR-B001`). Variants distinguish external safety actually given,
mere perception, trust in a carrier, and restraint despite fear not yet
removed.

`LA-08b`, truth-to-assent: truth content (`HQQ-B001`) is perceived/considered,
self submits/confirms (`AMN-B002`), then can carry content reciprocally
(`WSY-B003`). Failure variants are mismatch, unconfirmed report, or assent with
no later speech.

`LA-08c`, familiarity: perceived person/conversation (`INS-B002,B003`) reaches
self, alienation changes to familiarity/joy, selected intimate (`INS-B006`)
fills stable social endpoint. A tame animal or human-facing side can fill the
approachable-object role in distinct variants; neither is the same occupant.

`LA-08d`, maturity perception: developing girl (`ASR-B009`) perceives internal
increase; knowledge threshold (`INS-B002`) is crossed; house confinement may
follow. Self-restraint (`SBR-B001`) and imposed restraint (`SBR-B002`) are
competing projected aftermaths whose consent delta remains explicit.

### `LA-09`: temporal pairing, connection, threshold, and persistence

Canonical role spine:

```text
phase/state A -> connection or elapsed interval -> phase/state B
-> threshold/result -> carrier continuing across boundary -> return/open end
```

`LA-09a`, night/day: temporal pair (`ASR-B001`) supplies members; explicit
night-to-day connection (`WSY-B001`) supplies edge. Morning/evening and
afternoon supply competing indexed subpositions. Only the supplied direction
is actual; any day-to-night return remains projected/open.

`LA-09b`, life threshold: immature camel/girl (`HQQ-B008`, `ASR-B009`) passes
elapsed interval/sign into load-bearing or maturation state. Work disposition
(`AML-B008`) or house confinement (`ASR-B009`) fills competing aftermath. Age,
bodily sign, capacity, and social boundary are not collapsed.

`LA-09c`, after death: instruction (`WSY-B002`) crosses originator's death
boundary and persists in recipient; coerced victim (`SBR-B002`) instead reaches
terminal death with no supplied continued agency. The assembly exposes content
as a carrier that can continue where an occupant cannot.

`LA-09d`, winter position: time (`ASR-B001`) supplies container, exact center
(`HQQ-B011`) ordinal position, intense cold (`SBR-B007`) force, traveler
arrival the affected event. Outcomes: exposure, endurance, shelter/refuge, or
departure; center does not automatically mean greatest intensity.

### `LA-10`: atmospheric layer, precipitation, and ground response

Canonical role spine:

```text
ground/water source -> atmospheric carrier/layer -> force and vertical motion
-> released rain/dust/scent -> land/group receiver -> growth, abundance, or
settling aftermath
```

`LA-10a`: stacked white cloud (`SBR-B010`) carries rain (`ASR-B003`), releases
it to connected vegetation/land (`WSY-B001`) or suitable pasture/herd
(`WSY-B004`), and yields abundance. Nonrelease, rain missing the receiver, and
pasture failing to suit herd remain variants.

`LA-10b`: wind raises dust (`ASR-B004`) through cloud levels (`SBR-B010`);
hard/gravel land (`SBR-B005`) supplies source ground. Result is column,
dispersal, deposition, or obscured perception (`INS-B002`). Dust is not rain.

`LA-10c`: perfume replaces dust, hem replaces ground source, and perceiver
(`INS-B002`) replaces land receiver. The path trails rather than nourishing;
aftermath is sensed scent, dissipation, or no detection.

### `LA-11`: animal carrier, access, capacity, and labor

Canonical role spine:

```text
animal state -> human-facing access -> burden/work demand -> locomotor members
-> route/gait -> delivery or failure -> care/compensation aftermath
```

`LA-11a`, capable camel: age threshold (`HQQ-B008`) supplies readiness;
dependability against fatigue/stumble (`AMN-B001`) supplies reliability;
natural work disposition (`AML-B008`) supplies repeated action; rider-facing
side (`INS-B004`) supplies access. Result is carried burden/ride, fatigue,
stumble, or unused capacity.

`LA-11b`, overdriven carrier: severe pace (`HQQ-B012`) exceeds capacity;
working legs (`AML-B010`) and matched hoof placement (`HQQ-B014`) supply
motion; hard road (`SBR-B005`) supplies resistance. Reliability becomes a
counterfield rather than guaranteed outcome; aftermath is exhaustion,
inability, continued gait, or rest.

`LA-11c`, supported animal: human performs beneficent repair/care toward animal
(`SLH-B001`), pasture fits it (`WSY-B004`), and fatness reaches completion
(`HQQ-B013`). Work can follow, but care, feeding, growth, and labor remain
separate events and controllers.

### `LA-12`: force, body boundary, support, and injury

Canonical role spine:

```text
controller/force -> instrument or pace -> body/structural support -> capacity
boundary -> penetration/exhaustion/holding -> recovery or terminal result
```

`LA-12a`: spear (`AML-B009`) plus straight stab (`HQQ-B009`) meets body
interior; hard/thick resistance (`SBR-B005`) or firm weave (`HQQ-B010`) can
project as armor/boundary only as a role, not a supplied object. Outcomes are
penetration, nonpenetrating wound, deflection, or stopped force.

`LA-12b`: driver and severe pace (`HQQ-B012`) act on animal back; working legs
(`AML-B010`) carry force; no capacity remains. Self-restraint (`SBR-B001`) is a
controller-mismatched alternative, while coercive holding (`SBR-B002`) aligns
at external control. Outcomes are exhaustion, forced continuation, halt, or
death.

`LA-12c`: guarantor (`SBR-B003`) fills support role for a group rather than a
body; firm structure (`HQQ-B010`) supplies functional stability; severe event
(`SBR-B006`) supplies load. This social-scale projection ends in borne duty,
group survival, support failure, or inescapable collapse.

### `LA-13`: derivational insertion and surface attachment

Canonical role spine:

```text
base form -> exact added/attached material at indexed position -> full form
-> changed grammatical or named relation -> positioned recurrence
```

`LA-13a`: `العصر + inserted ن -> العنصر` (`ASR-B011`) yields origin/genealogy
form while retaining asserted refuge-base relation. Surface `عصر` at `P[1.1]`
is a separate positioned base occurrence, so the circuit is
`surface base -> source assertion -> inserted ن -> full lexical form`, not a
claim that the surface token denotes genealogy.

`LA-13b`: loss-family base plus `ن`/`ي` yields `خنسرى`/`خيسرى`
(`KHSR-B005`), then plural/ruin/weak-class forms branch. The explicit absent
singular for `الخناسير` terminates that route. Surface `خسر` at `P[2.4]`
touches the recovered base but does not inherit the added-form referents.

`LA-13c`: surface base plus prefix/article/suffix forms all fourteen words.
Variant grammatical results are oath government, emphasis, definiteness,
conjunction, prepositional government, and 3MP reference. The lexical inserted
letters can occupy the material role, but their result is named-form change,
not grammar. This mismatch keeps both formal operations differentiated.

### `LA-14`: three-line boundary machine

Canonical roles are fixed by complete surface positions:

```text
opening framed noun [و+ال+عصرِ]
-> middle predicated state ending [خسرٍ]
-> closing framed content noun [ب+ال+صبرِ]
```

`LA-14a`, enclosure variant: first and third terminal carriers supply the same
three-morpheme, definite, genitive shape around the bare indefinite middle
terminal. Oath government changes to prepositional government; time/refuge/
pressure facets from `ASR` and holding/boundary facets from `SBR` may project as
outer roles; decrease facets from `KHSR` occupy the middle state. The structural
operation is enclosure with changed controller and content, not a completed
interpretation.

`LA-14b`, final-consonant route: `ر` persists through all three endings while
the preceding root material, definiteness, and governing head change. A stable
terminal aperture receives three different lexical tuple families. Any
semantic filler attached to the recurrent sound remains projected; the exact
payload is position, consonant, case, and boundary return.

`LA-14c`, expansion variant: word units expand `1 -> 4 -> 9`, morphology rows
expand `3 -> 6 -> 21`, syntax carriers `2 -> 4 -> 12`, and syntax edges
`1 -> 3 -> 7`. The single opening carrier expands into predication and then a
four-performance exception scope. These complete vectors can supply scale and
differentiation roles to later formations but currently carry no hierarchy.

### `LA-15`: sensory substance, body response, and transmission

Canonical role spine:

```text
substance source -> sensory medium/path -> perceiver/body -> immediate quality
-> controlled response -> later state/use
```

`LA-15a`, bitter medicine: tree extract (`SBR-B008`) enters mouth/body;
bitterness is perceived (`INS-B002` projected); intentional administration
(`AML-B001`) responds; repair (`SLH-B001`) is a possible but unsupplied outcome.
Variants end in therapeutic use, rejection due to bitterness, or no effect.

`LA-15b`, sour fruit: fruit/tree (`SBR-B009`) supplies substance and acidity;
eater/perceiver remains open; dry tongue (`ASR-B014`) or choking throat
(`ASR-B008`) competes as bodily state; water can mediate passage. Outcomes are
continued dryness, swallowing, stronger discomfort, or sensory recognition.

`LA-15c`, scent: perfume plume (`ASR-B004`) follows hem through air; hear/see/
sense tuple (`INS-B002`) supplies detection role; familiarity/joy
(`INS-B003`) can fill one affective aftermath while alarm/suspicion fills
another. Same detected substance does not predetermine response.

### `LA-16`: naming, reflection, and social position

`LA-16a`: form (`ASR-B013`, `SBR-B016`, `SLH-B004,B005`) enters naming
relation and points to tree, group, person, city, or river. A perceiver
(`INS-B002`) can recognize the name; an instruction (`WSY-B002`) can transmit
it; a later action can use it. Other root senses are not imported into the
referent.

`LA-16b`: small human image in eye (`INS-B005`) projects a representation role;
firm/true speech (`HQQ-B001,B010`) projects a second representation carrier;
surface `ٱلْإِنسَٰنَ` supplies a human category anchor. Variants compare visual
image, named human, and proposition about a human; occupant identity is never
asserted across the three.

`LA-16c`: lower client position (`ASR-B012`), intimate selected position
(`INS-B006`), appointed official (`AML-B003`), entitled claimant
(`HQQ-B003`), and guarantor (`SBR-B003`) compete as social-role fillers in a
group. Each yields different duties, access, rank, and aftermath; generic
membership is only the assembly cue.

### `LA-17`: branch-light remainder assemblies

These variants prevent slight or awkward branches from disappearing:

- `LA-17a`: flatulence/wind (`ASR-B015`) can fill bodily source and expelled
  air in the same directional skeleton as dust/perfume wind (`ASR-B004`), but
  medium, scale, controller, and social/sensory aftermath all mismatch. The
  variant ends at emission/dissipation.
- `LA-17b`: named tree `العصرة` (`ASR-B013`) can fill source-tree in bitter
  extract (`SBR-B008`) or sour fruit (`SBR-B009`); no source states that it
  yields either product, so productive outcome stays open or mismatched.
- `LA-17c`: dry tongue (`ASR-B014`) can occupy affected organ in gradual-water
  release (`ASR-B008`); thirst, not choking food, supplies incoming condition.
  Outcome branches into moisture, continued dryness, or impaired passage.
- `LA-17d`: proper name (`SLH-B004`), place name (`SLH-B005`), and group name
  (`SBR-B016`) can fill referential endpoints in speech/advice, while repair,
  reconciliation, restraint, and geography remain independent facets.
- `LA-17e`: table sheet/food heap (`SBR-B011`) can fill support/material in
  manual work or transaction (`AML-B005,B006`); unmeasured sale creates an
  amount vacancy, while stacked food creates a vertical form. These two
  consequences remain separate.
- `LA-17f`: spider web/case (`HQQ-B011`) can fill enclosure or woven-firmness
  roles (`HQQ-B010`), but the web's supplied existence does not state tightness
  or successful protection. Variant outcomes are enclosure, fragile boundary,
  or exact fit.

## Surface-root exact-form registers

These registers close the base/contact pass while preserving negative results.
Only explicitly supplied complete forms seed substrings; ordinary derived
similarity does not.

- `CF-ASR`: exact `عصر` occurs in surface/morphology and in supplied forms such
  as `العصر`, `العصران`, `عصرا`, `لعصر`, `عصرت`, `عصرته`, `يعصرون`,
  `المعصرة`, `المعصرات`, `أعصر`, `تعصرون`, `عصرة`, `تعصرت`, `عصرك`, and
  `عصر الزرع`. It is not a contiguous exact base in `إعصار`, `عصارة`, `عصير`,
  `معصار`, `معصور`, `عاصر`, `اعتصار`, `المعتصر`, or `عنصر`; those retain root,
  derivational, or explicit equation relations instead. `عنصر` re-enters by the
  exact added-`ن` assertion.
- `CF-INS`: strict surface/morphology `إنسن` preserves the dagger-alif spelling;
  supplied lexical `إنسان` has an ordinary written alif. The complete shorter
  lexical form `إنس` occurs at the beginning of the stem and in `الإنس`,
  `إنسي`, and `إنسك`; the complete surface particle `إن` is shorter again and
  occurs inside the stem. These nested nodes are `[إن < إنس < إنسن/إنسان]`
  with every spelling and type retained.
- `CF-KHSR`: exact `خسر` recurs in `الخسر`, `الخسران`, `خسر`, `خسرت`,
  `أخسرته`, and related suffixed carriers. It is interrupted by the asserted
  additions in `خنسرى`, `خيسرى`, `الخناسر`, and `الخناسير`; recovered formal
  bases, not false substrings, carry those circuits.
- `CF-AMN`: recovered surface lemma/stem is strictly `ءامن`; lexical records use
  such distinct written forms as `آمن`, `آمين`, `أمن`, `الإيمان`, and `مؤمن`.
  Root and explicit definitional relations connect them. Madda, standalone
  hamza plus alif, and hamza-on-alif are not erased to manufacture an exact
  token identity.
- `CF-AML`: exact `عمل` occurs in surface `وعملوا` and in `عمل`, `العمل`,
  `يعمل`, `أعمل`, `استعمل`, `العملة`, and `تعمل`. Forms with inserted alif such
  as `عامل` and `معاملة` remain derivationally related but not exact `عمل`
  substrings.
- `CF-SLH`: the supplied surface uses dagger-alif writing in `صَّٰلِحَٰتِ` and
  strict mark-stripped `صلحت`; lexical records provide `صالح`, `الصالحة`, and
  proper-name forms with ordinary alif. Morphology supplies root `ص ل ح`,
  active-participle status, feminine plural, and accusative case. These are the
  licensed relations; conventional spelling is not silently substituted in
  the strict lane.
- `CF-WSY`: recovered surface `تواص` occurs twice and is an exact initial
  sequence in supplied `تواصى` and `تواصلوا`. Lexical full forms retain final
  `ى`, later `ل`, or other material; surface full forms retain conjunction and
  3MP suffix. Root `و ص ي` supplies the lineage to `وصية`, `وصي`, and `وصل`
  assertions where no exact `تواص` containment exists.
- `CF-HQQ`: exact `حق` occurs in surface `بالحق` and in `الحق`, `حقيق`,
  `محقوق`, `استحق`, `حققت`, `أحققت`, `ليحق`, `الأحق`, and repeated positions
  of `الحقحقة`. Forms such as `حاق`, `حقيقة`, and `محتقة` retain their supplied
  branch relations without being forced into a contiguous `حق` occurrence.
- `CF-SBR`: exact `صبر` occurs in surface `بالصبر` and supplied `الصبر`,
  `صبرت`, `صبرا`, `صبرة`, and `أصبره`. `صبير`, `صبار`, `صبارة`, and `اصطبر`
  insert or change letter order and remain complete distinct forms. Vocalic
  branch distinctions such as `الصبر بكسر الباء` and `الصبار بضم الصاد` remain
  source actuality even when mark-stripped detection increases formal contact.

The explicit one-letter surface forms `و`, `ل`, and `ب` recur inside many
lexical tokens. Their closure is represented canonically as
`[typed one-letter node, exact containing full form, source/position]`; every
new container preserves its complete branch tuple. This prevents an unbounded
list of identical letter-only edges while retaining every distinct container
and never transferring grammatical function to an internal root letter.

## Root-pair interface closure

This matrix records a maximal interface or, where no exact invariant is
licensed, the live `LA` search cue for every pair of the nine surface roots.
It prevents a remote root family from dropping out merely because a stronger
contact exists elsewhere.

| root pair | closed interface or assembly cue |
|---|---|
| `ع ص ر` / `ء ن س` | maturity perceived; person choking/drinking; refuge or proximity; wind/substance perceived |
| `ع ص ر` / `خ س ر` | extracted yield/gift versus decreased capital/no profit; amount and transfer direction |
| `ع ص ر` / `ء م ن` | refuge/security; inner stillness versus held refuge; dependable camel versus time/capacity |
| `ع ص ر` / `ع م ل` | pressing or land exploitation as intentional work; instrument, road, traveler, yield |
| `ع ص ر` / `ص ل ح` | productive/relieving result versus repair; fit of refuge/pasture/result remains projective |
| `ع ص ر` / `و ص ي` | exact night/day connection; connected land; extracted or temporal content carried onward |
| `ع ص ر` / `ح ق ق` | time/center, maturity thresholds, camel states, extraction/entitlement, refuge/defense |
| `ع ص ر` / `ص ب ر` | exact extract, cloud, winter, holding, enclosure, water/body, tree/substance contacts |
| `ء ن س` / `خ س ر` | human participant under loss; weak/low people class; perception of decrease remains `LA` |
| `ء ن س` / `ء م ن` | perceived content -> assent; familiarity/security; self/heart participant |
| `ء ن س` / `ع م ل` | eye as perceiving/working member; intentional human; facing side as access to instrument |
| `ء ن س` / `ص ل ح` | human as repair target; person/thing suitability; familiarity/reconciliation between people |
| `ء ن س` / `و ص ي` | visible/known content entering communication; group/member orientation and endpoint |
| `ء ن س` / `ح ق ق` | perception/knowledge -> verification/certainty; facing side -> exact fit/position |
| `ء ن س` / `ص ب ر` | human/self as held participant; inner state; eye-image inside boundary; person in severe event |
| `خ س ر` / `ء م ن` | threatened/reduced state versus security/trust; trader/report confidence is `LA`, not invariant |
| `خ س ر` / `ع م ل` | trade, wage, work, amount, compensation, and capital result |
| `خ س ر` / `ص ل ح` | damaged/decreased state versus repair; action can worsen or restore, controller open |
| `خ س ر` / `و ص ي` | short-delivered recipient versus content recipient; only receiver/transfer roles align, so `LA` |
| `خ س ر` / `ح ق ق` | deficient amount versus entitlement/obligation; adjudicated right and transaction loss |
| `خ س ر` / `ص ب ر` | unmeasured heap versus reduced measure; no singular/no outlet vacancies; endurance under loss is `LA` |
| `ء م ن` / `ع م ل` | confirmed content -> intended action; dependable working animal; trust in appointed worker is `LA` |
| `ء م ن` / `ص ل ح` | human inner security and repaired state; good action; opposed bad/fear states remain distinct |
| `ء م ن` / `و ص ي` | confirmed report/promise carried as instruction or reciprocal counsel |
| `ء م ن` / `ح ق ق` | exact truth and confirmation circuit; certainty, assent, evidence, promise |
| `ء م ن` / `ص ب ر` | fear removal versus panic restraint; trusted nonfailure versus capacity/exhaustion; self node |
| `ع م ل` / `ص ل ح` | exact good/bad works and repair/corruption result; surface predicate-object binding |
| `ع م ل` / `و ص ي` | exact prescribed content `بما يعمل به`; recipient becomes fresh action controller |
| `ع م ل` / `ح ق ق` | wage/entitlement, firm speech/worked material, spear segment/penetrating path, fitted action |
| `ع م ل` / `ص ب ر` | exertion/restraint, worker support/guarantor, unmeasured transaction, feet/terrain |
| `ص ل ح` / `و ص ي` | reconciliation through reciprocal relation; suitability and pasture compliance; advice toward action |
| `ص ل ح` / `ح ق ق` | fit/matching, repair/verification, dispute/reconciliation, obligation to protect repaired relation |
| `ص ل ح` / `ص ب ر` | repaired state under self-restraint; coercion can damage rather than repair; group/place names only formally map |
| `و ص ي` / `ح ق ق` | truth as counsel content; one-way/reciprocal claims; fit of pasture; instruction and obligation |
| `و ص ي` / `ص ب ر` | patience as counsel content; after-death/terminal boundary; guarantor duty; connected stacked layers only as `LA` |
| `ح ق ق` / `ص ب ر` | firm boundary, joint/side/stopper, forced pace/forced holding, winter center/cold, rights/retaliation |

## Forward reading movement

1. `FWD-1`, line 1: the first and only word supplies an oath-governed,
   definite, genitive time/root carrier. Its lexical field immediately branches
   into time, pressure/extract, rain, whirlwind, refuge, withholding, gift,
   gradual water release, maturity, husk, origin, low social position, tree,
   dry tongue, and bodily wind. None is selected. The single-word line is
   already a multiport reservoir.
2. `FWD-2a`, line 2 opening: `إِنَّ` contacts the beginning of the adjacent
   human stem before syntax separates particle from governed noun. Human then
   opens kind/collective, perception, familiarity, facing side, eye-image, and
   self/intimate tuples.
3. `FWD-2b`, line 2 predicate: emphatic/prepositional enclosure places the human
   carrier in `خسر`; lexical loss branches into general decrease, trade/capital
   result, active measure reduction, and inserted-letter/weak-class/ruin forms.
   Agent, mechanism, measure, and aftermath remain open on the surface.
4. `FWD-3a`, line 3 opening: `إِلَّا` sets an exception scope and simultaneously
   creates the formal `لا` microcontact field. The relative plural group then
   becomes the repeated 3MP controller.
5. `FWD-3b`, belief and action: the group performs a confirmation/security-root
   event and then an intentional work event with explicit good-action object.
   Lexical circuits release assent, report/promise, inner tranquility, request,
   intention, appointed work, instrument, wage, path, and repair/fit ports.
6. `FWD-3c`, reciprocal pair: the exact recommendation frame performs twice.
   First content activates truth, match, right, obligation, dispute, evidence,
   defense, maturity, penetration, firmness, joint, exertion, completion, and
   aligned gait. Second content activates self-restraint, coercion, guarantee,
   side, stone, no-exit severity, cold, bitter extract, sour fruit, cloud,
   food support/heap, retaliation, group name, mountain, and stopper. The
   paired frame keeps these two content fields adjacent but differentiated.
7. `FWD-BOUNDARY`: each forward line terminates in the genitive `ر` boundary;
   the lexical field expands while the final consonant returns.

## Backward rereading movement

1. `BACK-1`, from `بِٱلصَّبْرِ`: the last content is not only self-restraint.
   Its supplied branches reopen the preceding reciprocal event as possible
   transmission of a self-controlled operation, warning about coercion,
   guarantor duty, boundary knowledge, hard resistance, no-exit condition,
   winter force, bitter substance, layered cloud, unmeasured heap, retaliation,
   named group/mountain, or sealing mechanism. Each variant returns to the
   second `تَوَاصَوْا۟` with a different content vector and aftermath.
2. `BACK-2`, from the repeated verb: the second identical performance makes the
   first performance newly visible as one member of a two-slot carrier system.
   Same controller, grammar, measure, and route can carry changed content. The
   first does not absorb the second; together they expose carrier invariance.
3. `BACK-3`, from `بِٱلْحَقِّ`: truth's physical fit, right, dispute, defense,
   maturity, penetration, firm weave, socket, strenuous pace, completed animal
   state, and hoof alignment reopen what a content can do: correspond, bind,
   be claimed, be shown, require defense, penetrate, fit, exhaust, or mark a
   threshold. Returning to `ءَامَنُوا۟`, the exact `التصديق/صدق` circuit gives
   earlier assent an object/verification interface without making the surface
   belief content explicit.
4. `BACK-4`, from `ٱلصَّٰلِحَٰتِ`: suitability, repair, reconciliation, and
   personal/place-name branches reopen `عَمِلُوا۟`. The lexical phrase
   `الأعمال الصالحة والسيئة` makes action polarity explicit; `SLH-B001` gives
   work a repair/corruption aftermath; `SLH-B003` gives it a fit test. Proper
   names remain formal remainders rather than results.
5. `BACK-5`, from `عَمِلُوا۟` to `ءَامَنُوا۟`: work's intention, assignment,
   wage, reciprocity, hand/instrument, effort, animal disposition, spear/eye,
   road, and walking ports make prior assent able to precede many fresh
   performances. This is content/performance continuation, not asserted
   causation.
6. `BACK-6`, from the exception group to `ٱلْإِنسَٰنَ`: the plural controllers
   reopen the earlier human carrier as collective/individual, perceiver,
   companion, oriented body, eye-image, or self. The exception relation binds
   category and group positionally while exact occupant identity remains only
   where syntax/coreference supplies it.
7. `BACK-7`, from `خسر` through later amount and state mechanisms: later work,
   wage, right, measure, self-restraint, no-outlet, and repair ports give the
   earlier loss state possible mechanisms, counters, or aftermaths. None is
   inserted into `SA` because line 2 does not supply its agent or measure.
8. `BACK-8`, from final `صبر` to opening `عصر`: exact `العصارة` joins bitter
   tree extract to pressure/yield; exact cloud joins layers to rain release;
   exact winter joins cold to central time; holding joins self-restraint to
   confinement/withholding; boundary joins stopper/sides to husk/refuge. The
   first word's time, pressure, refuge, and enclosure roles are therefore
   changed by the last word without either becoming the other.
9. `BACK-9`, passage boundary return: closing `[ب+ال+صبرِ]` reactivates opening
   `[و+ال+عصرِ]` as the same three-part formal frame under changed head, root,
   lexical field, and passage position. The middle `خسرٍ` remains the unframed,
   indefinite changed term.

## Live trajectories and unresolved attractions

- `TR-01`: perceived content -> confirmation -> reciprocal carrying -> action
  -> repair/corruption -> later verification. Open: exact initial content,
  verifier of aftermath, and whether circulation returns.
- `TR-02`: pressure/force -> bounded material -> extract/yield -> receiver ->
  benefit/loss. Open: instrument for rain/property variants, legitimate
  entitlement, residue, and measure.
- `TR-03`: outside threat -> refuge/boundary -> defense or sealing -> protected
  occupant. Open: threat, entrant identity, defender, release time.
- `TR-04`: enclosure -> absent outlet -> penetrating/releasing route -> escape
  or injury. Open: whether penetration benefits occupant or harms it.
- `TR-05`: work -> wage/right -> measuring/adjudicating medium -> paid,
  diminished, disputed, or unrewarded aftermath. Open: payer and standard.
- `TR-06`: group aversion/claim -> reciprocal speech/dealing -> victory,
  reconciliation, continued dispute, or guaranteed relation. Open: content and
  adjudicator.
- `TR-07`: time phase -> connection -> maturity/capacity threshold -> work or
  confinement -> later state. Open: elapsed measure and return.
- `TR-08`: cloud/ground -> vertical carrier -> rain/dust/scent -> receiver ->
  abundance, obscurity, detection, or dissipation. Open: force and return path.
- `TR-09`: animal state -> access -> burden/route -> aligned gait or exceeded
  capacity -> care, rest, failure, or completion. Open: controller consent and
  burden.
- `TR-10`: base form -> added/attached material -> changed full form -> named or
  grammatical relation -> positioned recurrence. Open: no semantic transfer
  unless the exact source assertion supplies it.

## Typed open-role register

| anchor/formation | supplied positions | explicitly open, absent, or competing positions |
|---|---|---|
| line 1 oath | particle, governed time/root noun | speaker, addressed endpoint, purpose/aftermath |
| line 2 predication | human occupant, emphatic prepositional state, loss | loss agent, mechanism, measure, onset, response, exit |
| exception frame | exception particle, plural relative group, full scope | no extra exception members; relation to individual category remains categorical, not token identity |
| belief event | 3MP controller, perfect IV performance | explicit surface content, medium, addressee, result evidence |
| work event | same group, intentional-work root, good FP object | individual acts, tools, beneficiaries, aftermath/compensation |
| reciprocal event #1 | same group as bilateral participants, truth content | member-level direction sequence, response, verifier, result |
| reciprocal event #2 | same group as bilateral participants, patience content | whether content is operation, instruction, warning, boundary, substance, or another supplied branch facet |
| pressure assemblies | material, force, output in local tuples | residue, receiver/use, legitimacy, replenishment |
| enclosure assemblies | occupant, boundary, inside/outside in local tuples | controller in natural enclosures, release time, protective versus harmful value |
| economic assemblies | stock/work/right, possible transaction and amount | fair standard, payer, entitlement judgment, actual delivery |
| social assemblies | group/member roles, counsel/dispute/reconciliation/guarantee | which members fill which roles, duration, breach, renewed cycle |
| temporal assemblies | paired phases and thresholds | full directionality, duration, cycle return, relation to passage scope |
| naming tuples | form and named referent | any functional consequence beyond reference |

## Reservoir handoff state

All three statuses available in Turn 1 remain separately recoverable:

- `SOURCE_ACTUALITY`: exact passage, morphology, syntax edges, coreference,
  boundary order, and all 77 indexed lexical branch tuples.
- `LATENT_MAPPING`: strict and mark-stripped contact circuits, base/affix nodes,
  count vectors, repeated surface frame, boundary sequence, content and role
  continuations, full topology/delta mappings, controller counterfields, and
  vacancy comparisons.
- `LATENT_ASSEMBLY`: seventeen canonical role systems with explicit source IDs,
  competing fillers, mismatch variants, completed results, aftermaths, and
  bounded cycles.

No governing interpretation has been chosen. No primary scaffold has been
read, and no primary relation has been projected.
