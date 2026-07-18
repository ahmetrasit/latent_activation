# Activation Reservoir: S112 / V7.5.9

This is a Turn 1 formation field. It contains no primary scaffold and makes no
`PRIMARY_TRANSFORMATION`. `SOURCE_ACTUALITY` below means only what the supplied
passage, morphology, syntax, or a named lexical utterance asserts.
`LATENT_MAPPING` preserves a complete relation while changing its carrier or
parameters. `LATENT_ASSEMBLY` places independently supplied facets in typed
roles of a provisional mechanism; it never retroactively makes their source
occupants participants in one event.

## I. Positioned surface lattice

### Exact passage object

| line | complete positioned line | complete word-token count | morphological carrier count | supplied syntax-edge count |
|---|---|---:|---:|---:|
| 112:1 | `قُلْ هُوَ ٱللَّهُ أَحَدٌ` | 4 | 4 | 3 |
| 112:2 | `ٱللَّهُ ٱلصَّمَدُ` | 2 | 3 (`ٱل` + `صَّمَدُ`) | 1 |
| 112:3 | `لَمْ يَلِدْ وَلَمْ يُولَدْ` | 4 | 5 (`وَ` + `لَمْ`) | 3 |
| 112:4 | `وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ` | 5 | 7 (`وَ` + `لَمْ`; `لَّ` + `هُۥ`) | 4 |

The complete supplied vectors are therefore: lines `4`; word tokens
`[4,2,4,5]`; morphological carriers `[4,3,5,7]`; syntax edges `[3,1,3,4]`.
Reading the supplied attachments as clause/event carriers gives the ordered
clause vector `[2,1,2,1]`: command plus quoted nominal clause; one nominal
predication; two coordinated negated verbal clauses; one negated copular
clause. Root-bearing stems by line form `[3,2,2,3]`. These vectors remain whole
positioned objects; none is a selected subset.

After removal of vocalization and ordinary recitational marks, the complete
word forms and their letter counts are:

| line | ordered normalized word forms | letter-count vector | total |
|---|---|---|---:|
| 112:1 | `قل، هو، الله، أحد` | `[2,2,4,3]` | 11 |
| 112:2 | `الله، الصمد` | `[4,5]` | 9 |
| 112:3 | `لم، يلد، ولم، يولد` | `[2,3,3,4]` | 12 |
| 112:4 | `ولم، يكن، له، كفوا، أحد` | `[3,3,2,4,3]` | 15 |

The passage-wide normalized letter total is `47`, distributed `[11,9,12,15]`.
The opening-word sequence is `قل -> الله -> لم -> ولم`; the closing-word
sequence is `أحد -> الصمد -> يولد -> أحد`. Every line closes on written `د`,
but the carrier at that boundary changes from an indefinite nominative noun,
to a definite nominative noun, to a jussive passive verb, and back to an
indefinite nominative noun. The boundary movement is thus
`د/nominal predicate -> د/nominal predicate -> د/passive event under negation
-> د/delayed subject under negation`, not four averaged rhymes.

### Every positioned carrier and its exact work

- **112:1:1 `قُلْ`.** `SOURCE_ACTUALITY`: imperative verb, lemma `قَالَ`, root
  `ق و ل`, second-person masculine singular. Its grammatical controller is an
  unexpressed `2MS`; that controller is not the quoted `هُوَ`. Supplied syntax
  makes the following `هُوَ ٱللَّهُ أَحَدٌ` its quoted complement and keeps the
  speech verb outside the quote. Initiator/addressee beyond that grammatical
  position remain unlexicalized.
- **112:1:2 `هُوَ`.** `SOURCE_ACTUALITY`: independent `3MS` pronoun. It heads
  the supplied medium-confidence apposition edge to `ٱللَّهُ`; its referent is
  continuous with the named occupant, while apposition remains its local
  grammatical work.
- **112:1:3 `ٱللَّهُ`.** `SOURCE_ACTUALITY`: nominative proper name, lemma
  `ٱللَّه`, root `ء ل ه`; appositional/name carrier after `هُوَ` and head of the
  high-confidence predication to `أَحَدٌ`.
- **112:1:4 `أَحَدٌ`.** `SOURCE_ACTUALITY`: masculine, indefinite, nominative
  noun, lemma `أَحَد`, root `ء ح د`; nominative predicate of `ٱللَّهُ`. It is
  line-final, quote-final, and the last of four word tokens.
- **112:2:1 `ٱللَّهُ`.** `SOURCE_ACTUALITY`: the same written name, lemma,
  root, nominative state, and continuing discourse referent as 112:1:3, now
  first rather than third in its line and head of a new nominal predication.
  Occupant continuity and changed clause role are recorded separately.
- **112:2:2 `ٱلصَّمَدُ`.** `SOURCE_ACTUALITY`: complete definite nominative
  predicate of `ٱللَّهُ`. Its internal supplied carriers are determiner `ٱل`
  and stem `صَّمَدُ`, lemma `صَّمَد`, root `ص م د`, masculine singular. The
  word is simultaneously line-final and second of two tokens.
- **112:3:1 `لَمْ`.** `SOURCE_ACTUALITY`: negator governing the following
  imperfect as jussive. It opens both the line and the passage's sequence of
  three supplied `لَمْ` occurrences.
- **112:3:2 `يَلِدْ`.** `SOURCE_ACTUALITY`: active imperfect, jussive, `3MS`,
  lemma `وَلَدَ`, root `و ل د`, governed by the first `لَمْ`. Its grammatical
  controller is the continuous `3MS` referent; a generated child/product slot
  is opened by the lexical operation but the whole event is negated, so no
  child occupant is minted.
- **112:3:3 `وَلَمْ`.** `SOURCE_ACTUALITY`: complete word with conjunction
  prefix `وَ` and the second negator `لَمْ`. It coordinates a second clause
  with the preceding negated clause while independently governing its verb.
- **112:3:4 `يُولَدْ`.** `SOURCE_ACTUALITY`: passive imperfect, jussive, `3MS`,
  lemma `وَلَدَ`, root `و ل د`, governed by the second `لَمْ` and coordinated
  with `يَلِدْ`. Its grammatical subject is the affected/born position; the
  initiator is suppressed by passive voice, and negation prevents assertion of
  either an event or an initiator.
- **112:4:1 `وَلَمْ`.** `SOURCE_ACTUALITY`: exact recurrence of the preceding
  complete conjunction-plus-negator word, shifted from internal word 3 of
  112:3 to the first word of 112:4. The conjunction carries the negative
  sequence across a line boundary; `لَمْ` governs `يَكُن` as jussive.
- **112:4:2 `يَكُن`.** `SOURCE_ACTUALITY`: active imperfect jussive special
  form, lemma `كَانَ`, root `ك و ن`, third-person masculine singular. Supplied
  syntax makes `كُفُوًا` its predicate and final `أَحَدٌ` its delayed subject;
  its `3MS` agreement is with that delayed subject, not with the referent of
  the suffix in `لَّهُۥ`.
- **112:4:3 `لَّهُۥ`.** `SOURCE_ACTUALITY`: complete prepositional carrier,
  decomposed into `لَّ` and suffixed `هُۥ (3MS)`. Syntax attaches its pronoun as
  the complement of `كُفُوًا`. Coreference returns to the continuing named
  referent, but the local role is referential endpoint/possessive-comparative
  complement, not subject or predicate.
- **112:4:4 `كُفُوًا`.** `SOURCE_ACTUALITY`: masculine indefinite accusative
  noun, lemma `كُفُو`, root `ك ف ء`; accusative predicate of negated `يَكُن`.
  The full form includes final accusative material not present in the lemma.
- **112:4:5 `أَحَدٌۢ`.** `SOURCE_ACTUALITY`: masculine indefinite nominative
  noun, exact lemma/root recurrence of 112:1:4, now delayed nominative subject
  of `يَكُن`, inside the scope of negation and at line and passage end. It is
  not the same occupant as the first predicate merely because its token form
  recurs.

### Distributed surface relations

1. `ٱللَّهُ` recurs at 112:1:3 and 112:2:1: same named referent, same
   nominative morphology, changed ordinal `3 -> 1`, and changed appositional /
   predication environment. This is a `SOURCE_ACTUALITY` occupant
   continuation plus a `LATENT_MAPPING` of one name across two predicate
   frames.
2. `أَحَدٌ` encloses the line sequence at 112:1:4 and 112:4:5. Form, lemma,
   root, indefiniteness, gender, and nominative case recur exactly; role and
   polarity rotate `predicate/affirmative -> delayed subject/negated`. That
   maximal delta, not a merged meaning, is `LATENT_MAPPING` `LM-S-AHAD-ROT`.
3. `وَلَمْ` recurs exactly at 112:3:3 and 112:4:1. The first joins two clauses
   inside a line; the second joins across the next line boundary. Its invariant
   is conjunction plus negating government; its positional delta is
   `internal third token -> line-opening first token`.
4. `لَمْ` has the distribution `112:3:1 -> 112:3:3[m2] -> 112:4:1[m2]`:
   bare line opening, conjunctively renewed internal negation, then the same
   conjunctive renewal as a new line opening. Its governed complements rotate
   active birth, passive birth, copular occurrence.
5. Root/lemma `و ل د / وَلَدَ` repeats in adjacent predicates with one
   controller referent but reversed grammatical exposure: controller as active
   subject in `يَلِدْ`, affected participant as passive subject in
   `يُولَدْ`. Both remain jussive, imperfect, `3MS`, and negated. This is the
   complete voice counterfield `LM-S-WLD-VOICE`, not an assertion that either
   event occurred.
6. The continuous `3MS` referent passes through independent pronoun `هُوَ`,
   named nominal `ٱللَّهُ` twice, implicit agreement in the two line-3 verbs,
   and suffixed endpoint `هُۥ`. The line-4 verb instead agrees with delayed
   `أَحَدٌ`. Coreference is one actuality path; grammatical
   controller, appositional carrier, predication head, affected passive
   subject, and complement endpoint remain distinct roles.
7. Nominal predicates appear in lines 1 and 2 (`أَحَدٌ`, `ٱلصَّمَدُ`), while
   line 4 inserts a copula, advances its accusative predicate `كُفُوًا`, and
   delays its nominative subject `أَحَدٌ`. The same nominative closing form that
   was predicate in line 1 becomes subject after an accusative predicate.
8. The full ending vector is `[أَحَدٌ, ٱلصَّمَدُ, يُولَدْ, أَحَدٌ]`: consonant
   `د` is invariant; definiteness, case/mood, voice, and syntactic role vary.
   The first and last terms additionally make an exact whole-word enclosure.
9. The opening vector changes category in order:
   `imperative verb -> nominative proper name -> negator -> conjunction+negator`.
   The line-final vector changes category `noun -> noun -> verb -> noun`.
10. The quote has three internal carriers after one command; line 2 compresses
    to two nominal carriers; line 3 expands through a balanced pair of two-word
    negative clauses; line 4 expands to five words while delaying its subject
    until the passage boundary. These are full-unit grouping operations.

## II. Exact-contact closure

### Typed formal nodes and recording rule

Detection removes vocalization and ordinary orthographic decoration, but every
record below retains the written surface. The explicitly supplied surface
nodes are:

`قُلْ/قل`, `هُوَ/هو`, `ٱللَّهُ/الله`, `أَحَدٌ/أحد`,
`ٱلصَّمَدُ/الصمد`, `لَمْ/لم`, `يَلِدْ/يلد`, `وَلَمْ/ولم`,
`يُولَدْ/يولد`, `يَكُن/يكن`, `لَّهُۥ/له`, `كُفُوًا/كفوا`;
and the independently supplied morpheme/base nodes `ٱل/ال`, `صَّمَد/صمد`,
`وَ/و`, `لَّ/ل`, `هُۥ/ه`, `قَالَ/قال`, `وَلَدَ/ولد`,
`كَانَ/كان`, `كُفُو/كفو`, plus the supplied roots.

Every contact is canonicalized as `(short complete form, containing complete
form, exact offset/direction, written forms, positioned occurrence, licensing
tuple)`. A contact preserves the two containing words as different typed
nodes. It initially carries only form and position in `LATENT_MAPPING`; the
complete source assertion is reactivated around it, but its semantics are not
copied into the other containing word.

### Closed multi-letter circuits

- **`قل هو الله أحد` whole-line circuit.** The complete 112:1 surface after
  removal of vocalization is exactly the complete source utterance
  `قل هو الله أحد` in `ء ح د/B001`. Circuit:
  `112:1 exact line -> AHd-B001 complete assertion (أحد بمعنى الواحد ...
  قل هو الله أحد ... يستعمل مطلقا وصفا ... وأصله وحد) -> exact four-word
  source subphrase -> the positioned quote and its outside command -> later
  recurrence of أحد at 112:4:5`. The lexical quotation and the passage line
  remain two source occurrences joined by exact content identity.
- **`قل`.** The surface imperative is a morphological occurrence of lemma
  `قال` and root `ق و ل`; that asserted morphology is not literal containment
  because `قال` contains medial `ا`. Exact containment does occur in QWL-B005
  `أقل` after initial `أ`, twice in `ما لم أقل`; in QWL-B011 `قلت` before final
  `ت`; and inside QWL-B008 `القلة` at the internal sequence `قل`. Each circuit
  retains respectively unsaid attribution, supposition-like government, and a
  stick-struck object; none transfers those relations to the imperative.
- **`هو`.** Besides its exact position in AHd-B001's whole quote, it is an
  exact autonomous term in Allah-B001 `فالإله على هذا هو المعبود`, Allah-B002
  `اسم الله الأكبر هو الله`, KFW-B001 `فهو مكافئ له`, KFW-B004
  `فهو مكفأ`, and WLD-B003 `الولادة فهو وضع الوالدة ولدها`. Initial `ف` in
  `فهو` is retained. The contact field thus exposes identity/predication,
  equality-result, house-result, and birth-definition tuples without claiming
  the pronoun has the same referent in them.
- **`الله`.** Exact surface recurrence joins 112:1:3 and 112:2:1. Exact lexical
  occurrences lie in AHd-B001 `قل هو الله أحد`; Allah-B001 `فالإله الله
  تعالى`; and throughout Allah-B002, including `اسم الله الأكبر هو الله`,
  `الله ما فعلت`, `والله ما فعلته`, and invocative `يا ألله`. The asserted
  base transformation `إله -> حذف الهمزة + إدخال الألف واللام -> الله`
  is preserved as a source lineage, not reduced to substring detection.
- **`أحد`.** Exact surface recurrence joins 112:1:4 and 112:4:5. Every AHd
  branch re-enters: B001 exact `أحد` and related `الواحد`. Under base-letter
  detection, `احد` occurs after initial `و` in `واحد` and after `الـو` in
  `الواحد`; the written distinction `أ` versus `ا` is retained, so this is a
  normalized formal contact plus the source's explicit semantic equation, not
  an unqualified written-form identity. B002 supplies the
  negative utterances `لا أحد`, `ما في الدار أحد`, and `من أحد`, B003
  `أحد عشر`, `أحد وعشرين`, `أحدهن`, B004 `أحدكما` and `الأحد`, B005
  `استأحدت` and `استأحد`, and B006 the exact mountain name. Each longer form's
  added initial/final material is recorded. `أحاد/آحاد` is not falsely made an
  exact `أحد` containment: its written medial alif remains.
- **`الصمد` / `صمد`.** The complete line-2 word exactly meets `الصمد` in
  SMD-B001, B002, and B007. The supplied internal base `صمد` meets B001
  `صمدته، وصمدت، صمد، يصمده، مصمد`; B002 `الصمد، الصمدة، المصمد`;
  B003 `صمدتها، أصمدها`; B004 `صمد رأسه`; and B006 `صمده، صمدا`.
  It does not erase the medial `ا` in `الصماد/صمادة/مصماد`; those are separate
  forms and do not contain `صمد` in the same order without interruption.
- **`لم`.** Three positioned surface morphemes meet QWL-B005's two exact
  `ما لم أقل` occurrences and QWL-B012 `قول لم أظهره`. A larger exact collision
  also occurs between passage `وَلَمْ يَكُن` (after its initial conjunction)
  and QWL-B005 `قال ما لم يكن`: `لم يكن` is exact. The latter source relation
  defines false saying as saying what did not occur; exact form activates that
  whole tuple but does **not** label the passage false.
- **`يلد`.** The active jussive is an explicit positioned form, but no supplied
  lexical form contains it exactly. Its link to `وَلَدَ` is morphological
  lemma/root actuality, not a fabricated substring. This negative closure
  result is retained because the paired passive behaves differently.
- **`يولد` / `ولد`.** Surface `يُولَدْ` exactly meets WLD-B001 and WLD-B004
  `الوليد الصبي حين يولد`. It contains the explicitly supplied base `ولد`
  after initial `ي`. That base also occurs in WLD-B001 `الولد` and `الولد
  المولود`; B003 `ولدت`, `أولدت`, `ولدها`, `ولدناها`, `يوم ولدت`, `يوم ولد`;
  B004 `ولدان`, `ولدة`, `يولد`; B005 `تولد`, `المولد`, `مولد`; and B006
  recovered `ولدة`, `ولدان`, `ولدون`. Forms such as `المولود` and `أولاد`
  retain their intervening letters and are not silently contracted to `ولد`.
- **`يكن`.** Surface `يَكُن` exactly meets QWL-B005 `ما لم يكن`, and the full
  passage sequence supplies exact `لم يكن`. KWN-B001 `يكون` is related by the
  supplied lemma/root and jussive inflection, but its medial `و` prevents an
  exact containment claim. Both links stay active under different statuses.
- **`له`.** The complete surface preposition-plus-pronoun exactly meets
  QWL-B004 `الذي له قول`, QWL-B007 `انتشرت له قالة`, KFW-B001 `هذا كفء له`
  and `فهو مكافئ له`, and KFW-B004 `عملت له كفاء`. It also occurs as a terminal
  ordered sequence inside written `إله` and `الله` after normalization; the
  full forms and their different added initial material remain visible. This
  is a formal contact only: deity/name relations are not imported into the
  pronominal complement.
- **`كفوا` / `كفو`.** Morphology explicitly releases lemma `كُفُو` from
  accusative surface `كُفُوًا`; the base occurs at the beginning of the full
  form and final accusative `ا/تنوين` differentiates them. The root node is
  `ك ف ء`, while lexical branches write `كفء، كفئ، كفاءة، كفاء، كفأة، تكفؤا`.
  Their hamza-bearing spellings are preserved; none is declared an exact
  `كفو` substring. Root/morphological identity and exact-letter contact remain
  separate.
- **`قال` and `كان`.** They are explicit morphology lemmas. `قال` is exact in
  QWL-B001 and QWL-B005 and contained in `القال، القالة، يقال`; `كان` is exact
  in KWN-B001 and contained in its explicitly cited uses. Neither is identical
  to its surface inflection (`قل`, `يكن`); morphology licenses their actuality
  lineage.
- **Opening/closing returns.** The exact `أحد` whole-word return, exact
  `الله` return, exact `ولم` return, and exact letter-final `د` fourfold return
  close the surface comparison pass. No arbitrary two-letter substring is
  minted merely because it could be found.

### Explicit short-form contact families

The morphology supplies complete one-letter forms `و`, `ل`, and `ه`, and a
complete two-letter determiner `ال`; therefore the no-minimum rule applies.
Their closure is represented canonically by family, not by deleting their many
members:

- `C-WAW`: both positioned conjunctions `وَ` map to every exact displayed
  lexical form or quoted form containing written `و`, with branch provenance
  retained: AHd-B001/B003/B004 (including `واحد، الواحد، يوم`), Allah-B002
  (`والله`), QWL-B001--B016 wherever `قول/يقول/قولة/...` supplies the letter,
  KFW-B001--B005 in `مكافأة/تكافؤ/سنة/...`, KWN-B001--B006 in
  `الكون/يكون/موضع/...`, and every WLD branch's `ولد/والد/مولود/...` forms.
  The family payload is exact letter and position only; conjunction is not
  assigned to internal lexical waw.
- `C-LAM`: the positioned preposition `لَّ` maps to every exact displayed form
  containing `ل`, including surface `لم، الله، الصمد، يلد، يولد، له` and all
  corresponding lexical terms. The actual prepositional relation belongs only
  to 112:4:3; other members are typed containing-word nodes.
- `C-HA`: the positioned pronominal `هُۥ` maps to exact `ه` in `هو، الله، أحدهن،
  أحدكما، إله، له، فعلته، أظهره، ولدها` and the other displayed containing
  forms in their indexed branch tuples. Only the surface suffix is the
  coreferential pronoun; an internal letter is not.
- `C-AL`: the supplied determiner `ٱل` maps to complete surface `الله` and
  `الصمد` and to every displayed definite lexical term beginning with `ال`
  (`الواحد، الأحد، الإله، الآلهة، الصمد، المصمت، الصماد، القول، القيل، القالة،
  الكفء، التكافؤ، الكفاء، الكون، الكينونة، المكان، الولد، الوالد، الولادة،
  الوليد، المولد، اللدة`, with each further inflected occurrence kept under
  its branch). Allah-B002's asserted insertion of `الألف واللام` in forming
  `الله` is separately a semantic/formational source relation.

The family notation means the full Cartesian contact set licensed by each
short supplied form; member semantics are recoverable from the tuple inventory
below. A second pass over newly released bases (`وحد، إله، صمد، ولد، كفو` and
the surface lemmas) adds the contacts just enumerated and produces no new
complete supplied form. Exact-contact closure is therefore reached without
manufacturing substrings.

## III. Source-local tuple reservoir

Each item below is an atomic `SOURCE_ACTUALITY` tuple. Quoted source relations
are retained intact; the following ports are reusable only as separately
labelled mapping interfaces or assembly affordances.

### Root `ء ح د`: six complete tuples

- **AHd-B001: unity / absolute description / emphatic recurrence.** Licensing
  utterances remain: `أحد فرع والأصل الواو وحد`; `أحد بمعنى الواحد وهو أول
  العدد`; exact `قل هو الله أحد`; `يستعمل مطلقا وصفا في وصف الله تعالى وأصله
  وحد`; `أحد أحد`. Actuality ports: derived form `أحد`, recovered origin
  `وحد`, equation with `الواحد`, first ordinal of number, unrestricted
  descriptive use in the named source context, and repetition of the complete
  form for confirmation. Inputs are a describable occupant or count; outputs
  are description, first unit, or repeated confirmation. The derivation,
  arithmetic position, descriptive predication, and reiteration are four
  distinct facets.
- **AHd-B002: exhaustive negative domain.** Intact utterances: `لا أحد في
  الدار`; `ما في الدار أحد`; `أحد في النفي لاستغراق جنس الناطقين ولا واحد ولا
  اثنان فصاعدا`; `فما منكم من أحد عنه حاجزين`. Actuality topology: a negated
  domain/location or relation; `أحد` ranges over the full class capable of
  address, from one through two and upward; result is no occupant in that
  quantified class. The house and the blockers remain their local source
  occupants. Open ports are domain, eligible class, quantity scale, negator,
  and excluded occupant.
- **AHd-B003: unit in composition.** Intact utterances: `أحد واثنان وأحد عشر
  وإحدى عشرة`; `الواحد المضموم إلى العشرات نحو أحد عشر وأحد وعشرين`;
  `فأحدهن أي صيرهن أحد عشر`. Actuality topology: unit plus tens; the joining
  operation changes a counted group to eleven or a unit-plus-tens expression.
  Feminine and masculine forms, ordinal placement, larger count, and causative
  `صيّر` remain explicit parameters.
- **AHd-B004: firstness under addition and named day.** Intact utterances:
  `أن يستعمل مضافا أو مضافا إليه بمعنى الأول`; `أما أحدكما`; `يوم الأحد أي
  يوم الأول`; `يوم الأحد يجمع على آحاد`. Actuality ports: possessed/possessor
  side of an إضافة, first member, day-name, and plural `آحاد`. The two إضافة
  directions are not averaged.
- **AHd-B005: acting or arriving singly.** Intact utterances: `ما استأحدت بهذا
  الأمر أي ما انفردت به`; `استأحد الرجل انفرد`; `جاءوا آحاد أحاد`. One tuple
  has a controller who does not monopolize an affair; another has a man become
  separate; another has a plural group arrive as distributed individuals.
  Polarity (`ما` in the first), controller, affair, separation state, and
  plural-to-single distribution are retained.
- **AHd-B006: named mountain.** `أحد جبل بالمدينة` asserts a mountain bearing
  the complete form as its name and locates it in the named city. It supplies
  a concrete elevated mass and place port, not the numerical relation of the
  other branches.

### Root `ء ل ه`: two complete tuples

- **ALH-B001: worshipper / act / made object of worship.** Intact assertions:
  `أصل واحد وهو التعبد`; `فالإله الله تعالى لأنه معبود`; `تأله الرجل إذا
  تعبد`; `الإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها`; `التأله التعبد`;
  `أله ... أي عبد عبادة`; `مألوه أي معبود`; `الآلهة الأصنام`; `التأليه
  التعبيد`; `التأله التنسك والتعبد`; `لا يكون إلاها حتى يكون معبودا`;
  `معبوداتهم من الأصنام والأوثان آلهة`; `الإلاهة الشمس`; `إلاهتك وعبادتك`;
  `إله اسما لكل معبود`; `أله فلان يأله الآلهة عبد`; `فالإله على هذا هو
  المعبود`. Actuality preserves direction: a person/group performs worship;
  an object is worshipped or caused to be treated as such; source examples
  name the sun, `الأصنام`, and `الأوثان` as their own affected objects. The
  prerequisite
  `لا يكون إلاها حتى يكون معبودا` makes prior/passive reception of worship a
  typed condition. Those local occupants do not merge with the passage's named
  occupant.
- **ALH-B002: name formation, oath, address, invocation.** Intact assertions:
  `اسم الله الأكبر هو الله`; `الله ما فعلت ذاك تريد والله ما فعلته`;
  `لاه أنت أي لله أنت`; `لا هم اغفر لنا`; `منه قولنا الله وأصله إلاه`;
  `يا ألله اغفر لي`; `اللهم بمعنى يا ألله`; `لاه أبوك`; `لهنك`; `لهنا`;
  and `الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري
  تعالى`. The formal tuple is explicit: full `إله`, deletion of its hamza,
  insertion of `الألف واللام`, specialized result `الله`; written vocative,
  oath, contraction, and invocation variants remain distinct. The oath example
  includes a negated deed `ما فعلت`; invocation opens speaker, addressee,
  requested act, and beneficiary `نا`.

### Root `ص م د`: seven complete tuples

- **SMD-B001: directed intention toward a relied-upon endpoint.** Intact:
  `الصمد القصد وصمدته صمدا`; `وصمدت قصدت وصمدت صمد كذا أي قصدت قصده
  واعتمدته`; `صمده يصمده صمدا أي قصده`; `الصمد السيد لأنه يصمد إليه في
  الحوائج`; `بيت مصمد أي مقصود`; `الصمد السيد الذي قد انتهى سؤدده والذي يصمد
  إليه الأمر`; `صمدت صمد هذا الأمر أي قصدت قصده واعتمدته`; `الصمد السيد الذي
  يصمد إليه في الأمر`; `صمده قصد معتمدا عليه قصده`. Actuality topology has a
  moving/intending controller, directed act, affair or need as content, target
  who is relied upon, and arrival/intent result. `السيد`, `البيت`, and `الأمر`
  remain different local targets. Direction `seeker -> sought endpoint` is a
  reusable interface.
- **SMD-B002: solidity, compactness, no cavity, elevated/hard place.** Intact:
  `الصلابة في الشيء والصمد كل مكان صلب`; `المصمت الذي ليس بأجوف`; `الصمدة
  صخرة راسية`; `الصمد المكان المرتفع الغليظ`; `المصمد لغة في المصمت وهو الذي
  لا جوف له`; `المصمت الذي لا جوف له`; `المكان المرتفع الغليظ`; `المصمد
  الصلب الذي ليس فيه خدد`; `الشديد من الأرض`; `الصمد الذي ليس بأجوف`.
  Ports: material, resistance, compact interior, explicitly absent cavity,
  absence of grooves, elevation, thickness, anchored rock, severe ground.
  Negated interior and positive resistance are separate state fields.
- **SMD-B003: stopping/sealing a bottle.** Intact: `الصماد عفاص القارورة
  وصمدتها صمدا`; `الصماد عفاص القارورة`; `الصماد سداد القارورة`; `وقد صمدتها
  أصمدها`. Complete tuple: agent applies/makes a `صماد`; vessel is the affected
  container; mouth/opening is the typed boundary; stopper is instrument/result;
  outgoing state is closed/stoppered. The bottle's cavity is not denied as in
  B002; here a cavity-bearing container receives a boundary closure.
- **SMD-B004: wrapping the head.** `صمد رأسه تصميدا وذلك إذا لف رأسه بخرقة أو
  منديل أو ثوب ما خلا العمامة وهي الصماد`. Agent wraps; head is affected body
  part; cloth, kerchief, or garment are alternative media; turban is explicitly
  excluded; result is the named head-binding. The exclusion remains indexed
  when this facet is projected.
- **SMD-B005: overlooking an affair with full attention.** `إني على صمادة من
  أمر إذا أشرف عليه وحفلت به`. First-person controller stands over/on the verge
  of an affair, oversees it, and attends seriously to it. Spatial elevation,
  proximity, cognitive care, and the affair as content are separate ports.
- **SMD-B006: striking with a stick.** `صمده بالعصا صمدا إذا ضربه بها`.
  Controller strikes; an affected participant receives force; `العصا` is the
  instrument; direction is agent-through-stick-to-target; result is impact.
- **SMD-B007: remaining through hardship and beyond extinction.** Intact:
  `الصمد الدائم`; `الدائم الباقي بعد فناء خلقه`; `ناقة مصماد وهي الباقية على
  القر والجدب الدائمة الرسل`. One source tuple asserts persistent continuance
  after others' annihilation. A different tuple has a camel continue through
  cold and barrenness while continuously sending milk. Duration, adverse
  medium, survival, outgoing milk, and aftermath remain explicit.

### Root `ق و ل`: sixteen complete tuples

- **QWL-B001: internal letter-complex externalized in pronunciation.** Intact:
  `القول من النطق`; `قال يقول قولا وقولة ومقالا ومقالة`; `القول والقيل واحد`;
  `المركب من الحروف المبرز بالنطق`; `القيل من القول اسم`. A content may be a
  single expression, sentence, poem, or address as supplied in `what_is_ar`;
  composed letters are incoming structure, pronunciation is medium/action,
  externalized speech is result. The equation `القول والقيل واحد` and naming
  relation `القيل ... اسم` are exact semantic nodes.
- **QWL-B002: tongue as instrument.** `المقول اللسان` is an explicit equation.
  It releases tongue as bodily instrument/medium for QWL-B001 without making
  every `مقول` token a spoken content.
- **QWL-B003: profuse or fluent speaker.** Intact: `رجل قولة وقوال كثير القول`;
  `رجل تقوالة أي منطيق`; `قوال وقوالة أي كثير القول`; `رجل مقول ومقوال وقولة
  وقوال وتقوالة أي لسن كثير القول`. A person is bearer/controller; frequency
  and fluency are state parameters; the several forms are alternative named
  descriptions.
- **QWL-B004: title whose word takes effect.** Intact: `المقول بلغة أهل اليمن
  القيل وهم المقاولة والأقيال والأقوال والواحد القيل`; `القيل ملك من ملوك
  حمير دون الملك الأعظم والمرأة قيلة`; `كأنه الذي له قول أي ينفذ قوله`.
  Actuality separates one ruler, several plural classes, female form, rank
  below the greatest king, possessed word, and its effective outcome. The
  controller is the title-holder; the word is content/instrument; execution is
  result.
- **QWL-B005: nonexistent content and false attribution.** Intact: `تقول باطلا
  أي قال ما لم يكن`; `قولتني ما لم أقل`; `أقولتني ما لم أقل أي ادعيته علي`;
  `تقول عليه أي كذب عليه`. Tuple variants: speaker produces content that did
  not occur; attributor assigns an unsaid statement to another; liar speaks
  against another. Claimed speaker, actual speaker, attributed content,
  non-occurrence `لم يكن`, non-utterance `لم أقل`, and false outcome remain
  separate. Negation scopes the source content/event, not every formal contact.
- **QWL-B006: drawing a saying to oneself.** `اقتال قولا أي اجتر إلى نفسه قولا
  من خير أو شر`. Controller draws/appropriates a saying toward self; content
  polarity branches good/evil; route and endpoint are explicit.
- **QWL-B007: saying circulating among people.** Intact: `انتشرت له قالة حسنة
  أو قبيحة في الناس`; `القالة القول الفاشي في الناس`; `كثر فيه القيل والقال`;
  `كثرت قالة الناس`; `كثر القيل والقال`. A good/bad reputation or saying
  spreads through a human plurality; possessor, circulating content, social
  medium, valence, multiplicity, and recurrence are separate ports.
- **QWL-B008: striking stick.** `القال الخشبة التي تضرب بها القلة`. `القال`
  is wooden instrument; an unspecified striker uses it; `القلة` is affected
  object; strike is force/action. This source tuple is not a speech event.
- **QWL-B009: reciprocal negotiation about an affair.** `قاولته في أمره
  وتقاولنا أي تفاوضنا`. Two or more parties exchange speech; affair is shared
  content; reciprocal form changes unilateral utterance to negotiation.
- **QWL-B010: exercise of control over another.** `اقتال عليه تحكم`. Controller
  acts upon another; direction is over/against; result is control. It remains
  distinct from B006's movement of a saying toward self.
- **QWL-B011: speech verb operating as supposition.** Intact: `العرب تجري تقول
  وحدها في الاستفهام مجرى تظن في العمل`; `بنو سليم يجرون متصرف قلت في غير
  الاستفهام أيضا مجرى الظن`. A speech-form changes grammatical performance to
  that of supposition; first scope is interrogative and form `تقول` alone;
  second source community extends inflected `قلت` outside interrogation.
  Controller/community, construction, question polarity, government, and
  evidentiary/cognitive mode are parameters.
- **QWL-B012: unexternalized conception.** `المتصور في النفس قبل الإبراز
  باللفظ قول`; `في نفسي قول لم أظهره`. Content is present internally; psyche
  is container; speech has not crossed the vocal boundary; result is an open
  expression slot. This is not absence of content, but absence of performance.
- **QWL-B013: belief or doctrine.** `للاعتقاد نحو فلان يقول بقول أبي حنيفة`.
  A person adopts/holds a named proposition or doctrine; content continuity
  does not imply a fresh vocal performance.
- **QWL-B014: an object's indication.** `للدلالة على الشيء نحو قول الشاعر
  امتلأ الحوض وقال قطني`. A filled basin is nonhuman signifying carrier; its
  state indicates `enough`. Controller changes from speaker to object/state;
  no tongue is required.
- **QWL-B015: sincere care directed to a thing.** `للعناية الصادقة بالشيء
  كقولك فلان يقول بكذا`. A person directs genuine care toward an object or
  affair. Attention, truthfulness, target, and continuing stance are ports.
- **QWL-B016: definition as boundary.** `يستعمله المنطقيون في معنى الحد
  فيقولون قول الجوهر كذا وقول العرض كذا أي حدهما`. Logicians are controllers;
  substance/accident are defined objects; `قول` is their limit/definition;
  result is a conceptual boundary rather than merely an uttered token.

### Root `ك ف ء`: five complete tuples

- **KFW-B001: equality, peer relation, reciprocal like-for-like action.** The
  complete assertion field is retained: `الكفء المثل`; `التكافؤ التساوي`;
  `هذا كفء له أي مثله في الحسب والمال والحرب`; `المكافأة مجازاة النعم`;
  `الكفئ النظير`; `كل شيء ساوى شيئا حتى يكون مثله فهو مكافئ له`; `كافأت
  الرجل أي فعلت به مثل ما فعل بي`; `فلان كفء لفلان في المناكحة أو في
  المحاربة`; `نكافىء بهما عنا عين الشمس`; `كافأ الرجل بين فارسين برمحه`.
  Actuality variants expose: two comparands; a measure/domain (lineage, wealth,
  war, marriage); equality state; benefit received and answer in kind; first
  act and returned like act; two objects placed opposite/successive; two
  horsemen related by a spear; an unspecified dual medium in `بهما` warding
  the sun's eye away. Equality, reciprocity, opposition, pairing, and warding are
  distinct facets, though all retain two-sided topology.
- **KFW-B002: inclination, inversion, diversion, swaying, changed face.** Intact
  assertions: `أكفأت الشيء إذا أملته`; `كفأت القصعة والإناء`; `كفأت الإناء
  إذا كببته`; `كفأت القوم إذا صرفتهم إلى غيره`; `تكفأت المرأة في مشيتها`;
  `تكفأ تكفؤا`; `مكفأ الوجه كاسف اللون`; `الإكفاء قلب الشيء كأنه إزالة
  المساواة`. Agent tilts or overturns a thing/vessel; diverts a group away from
  its direction; a woman/body or ship-like carrier sways; a face's color/state
  breaks; explicit aftermath is removal of equality. Incoming orientation,
  force, pivot, outgoing direction, spilled/open content position, and changed
  equality are ports.
- **KFW-B003: discord among poetic endings.** Intact: `الإكفاء في الشعر`;
  `أن ترفع قافية وتخفض أخرى`; `الاختلاط في القوافي`; `يخالف بين قوافيه بعضها
  ميم وبعضها نون`; `اختلاف إعراب القوافي`. The complete ordered poem is the
  scale; each rhyme is a positioned carrier; letter, movement, and inflection
  are independent comparison parameters; raised/lowered, `م/ن`, or mixed
  endings create discord. The relation requires distribution, not one isolated
  ending.
- **KFW-B004: one or two sewn tent pieces.** Intact: `الكفاء شقتان تنصح
  إحداهما بالأخرى`; `الكفاء شقة أو ثنتان ينصح إحداهما بالأخرى`; `الكفاء
  بالكسر والمد شقة أو شقتان`; `أكفأت البيت فهو مكفأ إذا عملت له كفاء`;
  `الكفاء لشقة تنصح بالأخرى فيجلل بها مؤخر البيت`. Material is one or two
  pieces; joining/sewing relates one to the other; resulting covering is made
  for the rear boundary of tent/house. Alternatives one/two, seam partner,
  maker, house, rear, covering path, and covered result remain typed.
- **KFW-B005: annual yield and alternating cohorts.** Intact: `الكفأة وهي حمل
  النخلة سنتها`; `يقال ذلك في نتاج الإبل أيضا`; `سألته نتاج إبله سنة`;
  `الكفأة من الإبل نتاج سنة`; `أكفأت إبلي كفأتين`; `أعطاني لبنها ووبرها
  وأولادها سنة`; `سألته ثمرها سنة`; `يقال لنتاج الإبل ليست تامة كفأة`.
  Scale is one year; source can be palm or camels; outputs branch fruit,
  offspring, milk, wool; an asker requests and an owner gives; herd can be
  divided into two cohorts whose production alternates; one yield is explicitly
  incomplete. Period, source, beneficiary, product bundle, completion, and
  alternation phase are separate fields.

### Root `ك و ن`: six complete tuples

- **KWN-B001: occurrence/presence in time and grammatical performance.** Intact
  assertion field: `الكون الحدث يكون بين الناس ومصدر من كان يكون`; `الكينونة
  في مصدر كان`; `الكائنة الأمر الحادث`; `كان عبارة عما مضى من الزمان`;
  `حدوث الشيء ووقوعه`; `كان الأمر أي مذ خلق`; `تقع زائدة للتوكيد`; `لا يكون
  زيدا تعني الاستثناء`; `كونه فتكون أحدثه فحدث`; `أصل يدل على الإخبار عن
  حدوث شيء إما في زمان ماض أو زمان راهن`; `كان الشيء يكون كونا إذا وقع
  وحضر`. Ports: event, people among whom it occurs, past/present time,
  occurrence and presence, report, added emphasis, exception construction,
  causing controller, caused object, and resulting event. `كونه فتكون أحدثه
  فحدث` is a complete source-to-caused-occurrence lineage.
- **KWN-B002: place, station, and establishment.** Intact: `المكان اشتقاقه من
  كان يكون`; `تمكن`; `فلان مني مكان هذا`; `موضع العمامة`; `المكانة المنزلة`;
  `مكين عند فلان بين المكانة`; `المكان والمكانة الموضع`; `تمكن`. An occupant
  has a position relative to another; a turban has a head location; status is
  a social station; establishment changes mobility to located capacity.
  Physical place, relative place, rank, and enabling state remain distinct.
- **KWN-B003: guaranteeing/standing for a person.** Intact: `الكيانة الكفالة`;
  `كنت على فلان أكون كونا أي تكفلت به`; `اكتنت به اكتيانا مثله`; `كنت على
  فلان أكون عليه إذا كفلت به`; `اكتنت أيضا اكتيانا`. Guarantor/controller
  takes responsibility over/for a beneficiary; obligation is medium/state;
  outcome is continuing care or liability.
- **KWN-B004: submission.** `الاستكانة الخضوع` is an exact equation. A
  participant changes or remains in a lowered/submissive relation to an open
  authority endpoint.
- **KWN-B005: aged speaker indexed by former self-report.** `يقال للرجل إذا شاخ
  كُنْتِيّ`; `كأنه نسب إلى قوله كُنْتُ في شبابي كذا وكذا`. Current occupant is
  an old man; quoted `كُنْتُ` locates a prior youthful state; repeated
  self-report supplies the label. Same referent, changed time/state, memory
  content, and fresh speech performance remain separate.
- **KWN-B006: a bad condition through the night.** `الكينة في قولهم بات فلان
  بكينة سوء أي بحال سوء فأصله الكون فعلة من الكون`. Person is occupant; night
  is duration; bad condition is state; `كينة` has explicitly stated formal
  derivation from `الكون` on the named pattern.

### Root `و ل د`: six complete tuples

- **WLD-B001: offspring/progeny and variable number/class.** Intact assertions:
  `أصل صحيح وهو دليل النجل والنسل`; `الولد وهو للواحد والجميع`; `الولد قد
  يكون واحدا وجمعا`; `الوليد الصبي`; `الولد اسم يجمع الواحد والكثير والذكر
  والأنثى`; `الوليد الصبي حين يولد`; `الولد المولود`; `الابن والابنة`;
  `جمع الولد أولاد`. Product/occupant may be one or plural, young or older,
  male or female according to the exact named form; parent/source remains an
  open role in this branch. Number and gender ambiguity are actuality fields,
  not license to merge occupants.
- **WLD-B002: parent roles.** Intact: `الوالد الأب والوالدة الأم وهما
  الوالدان`; `يقال لأم الرجل هذه والدة`; `الأب يقال له والد والأم والدة ويقال
  لهما والدان`. Father and mother are distinct source roles relative to a child;
  dual `والدان` joins them as a pair. Direction is parent/source to child, with
  kin relation as interface.
- **WLD-B003: birth event and attendance.** Intact: `ولدت المرأة تلد ولادا
  وولادة`; `أولدت حان ولادها`; `الولادة فهو وضع الوالدة ولدها`; `شاة والد وهي
  الحامل`; `ولدناها أي ولينا ولادتها`; `يوم ولدت`; `يوم ولد`. Mother is
  grammatical/semantic initiator in active birth; child moves from carried to
  placed/born state; a sheep can occupy pregnant-source state; impending time
  differs from completed event; attendants in `ولدناها` oversee rather than
  become the mother; day is temporal boundary.
- **WLD-B004: newborn or enslaved-status terms.** Intact: `الوليدة الأنثى
  والجمع ولائد`; `الوليد الصبي والعبد والجمع ولدان وولدة`; `الوليد الصبية
  والأمة والجمع الولائد`; `الوليد الصبي حين يولد`; `يقال للأمة وليدة وإن كانت
  مسنة`; `الوليد يقال لمن قرب عهده بالولادة`; `الوليدة مختصة بالإماء في عامة
  كلامهم`. Age-near-birth and social-status uses are different parameters;
  masculine/feminine and plural variants remain exact. An old female servant
  proves that named status need not carry young age.
- **WLD-B005: causal production and newly made/non-pure artifact.** Intact:
  `تولد الشيء عن الشيء حصل عنه`; `عربية مولدة ورجل مولد إذا كان عربيا غير
  محض`; `المولد من الكلام مولدا إذا استحدثوه`; `كتاب مولد أي مفتعل`; `بينة
  مولدة وليست بمحققة`; `تولد الشيء من الشيء حصوله عنه بسبب من الأسباب`.
  Complete topology: source thing plus cause produces result thing. Product
  branches newly coined speech, mixed lineage/language, fabricated book, or
  generated but unverified evidence. `ليست بمحققة` negates verification, not
  production. Source, causal medium, novelty, purity, authenticity, and result
  are distinct fields.
- **WLD-B006: same-age peer and recovered initial letter.** Intact: `اللدة
  نقصانه الواو لأن أصله ولدة`; `لدة الرجل تربه`; `وهما لدان والجمع لدات
  ولدون`; `اللدة مختصة بالترب يقال فلان لدة فلان وتربه`. Formal tuple recovers
  base `ولدة` by restoring deleted initial `و`; relational tuple places two
  persons as peers in birth-age. Singular, dual, plural, peer relation, age
  measure, full form, reduced form, and missing initial remain indexed.

### Exact branch-image carrier register

These supplied images remain independently retrievable even where a tuple
above released more detailed microfacets:

- `AHd-B001` `الأَحَدِيَّة والوَحْدَة`; `B002` `استغراق النفي`; `B003`
  `الواحد في العد والتركيب`; `B004` `الأول والإضافة`; `B005` `الانفراد
  والتفرق آحادا`; `B006` `جبل أُحُد`.
- `ALH-B001` `التعبد والمعبود`; `B002` `اسم الله في القسم والنداء`.
- `SMD-B001` `القصد إلى المعتمد المقصود`; `B002` `الصلابة المكتنزة بلا جوف`;
  `B003` `سدادة القارورة المحكمة`; `B004` `شد الرأس بصماد`; `B005`
  `الإشراف على الأمر مع الحفل به`; `B006` `إيقاع الضرب بالعصا`; `B007`
  `الدوام والبقاء على الشدة`.
- `QWL-B001` `إخراج القول بالنطق`; `B002` `اللسان آلة القول`; `B003` `كثرة
  القول في صاحبه`; `B004` `القيل صاحب القول النافذ`; `B005` `قول ما لم يكن
  أو نسبته`; `B006` `اجترار القول إلى النفس`; `B007` `القول الفاشي بين الناس`;
  `B008` `عود القال لضرب القلة`; `B009` `المقاولة في الأمر`; `B010` `اقتالة
  الحكم على غيره`; `B011` `قول يجري مجرى الظن`; `B012` `قول في النفس لم
  يظهر`; `B013` `القول اعتقاد ومذهب`; `B014` `قول الشيء دلالته`; `B015`
  `العناية الصادقة بالشيء`; `B016` `قول الشيء حده`.
- `KFW-B001` `المماثلة والمقابلة بالمثل`; `B002` `الإمالة والقلب والصرف`;
  `B003` `اختلاف القوافي`; `B004` `كِفاء الخباء`; `B005` `كفأة السنة والنتاج`.
- `KWN-B001` `وقوع الشيء وحضوره في زمان`; `B002` `المكان والمكانة من الكون`;
  `B003` `الكفالة والقيام على فلان`; `B004` `الخضوع بالاستكانة`; `B005`
  `الشيخ المنسوب إلى كُنْتُ`; `B006` `حالة السوء بكينة`.
- `WLD-B001` `مولود من نسل`; `B002` `أبوان من جهة الولادة`; `B003` `حدوث
  الولادة ووضع الحمل`; `B004` `صغير قريب العهد بالولادة أو مملوك`; `B005`
  `شيء حاصل عن شيء أو مستحدث منه`; `B006` `قرين في سن الولادة`.

The `what_is_ar` carrier also keeps several details not allowed to disappear
into those short images: QWL-B001 content may be `مفردا` or `جملة` or `قصيدة`
or `خطبة`; KFW-B001 includes `المضادة` and `الموالاة بين شيئين`; KFW-B002
includes inclination of `القوس والصحفة` and swaying like `السفينة`; WLD-B001
allows the named offspring term across small/large as well as single/plural and
male/female parameters; WLD-B005 includes a result arising in a particular
environment as well as a non-pure or newly made result. These facets retain the
same branch IDs in every projection.

## IV. Passage event tuples and actuality paths

### `P-Q1`: command and quoted content

`SOURCE_ACTUALITY` tuple:

`implicit 2MS grammatical controller -> imperative قُلْ [QWL lemma/root;
active command] -> quoted content boundary -> هُوَ ٱللَّهُ أَحَدٌ -> nominal
predication result`

The command occurrence, the propositional content, and any eventual fresh
performance are separate. The supplied surface asserts the command and embeds
the content; it does not assert which lexical QWL-B001 medium, QWL-B002 tongue,
or QWL-B007 social route realizes a later performance. The quote's internal
roles are pronoun/appositional name/predicate. The command's object is the
whole three-token content, not only `هُوَ`.

Actuality continuation: 112:1:2 `هُوَ` -> appositional 112:1:3 `ٱللَّهُ` ->
predicated 112:1:4 `أَحَدٌ`; then the same named occupant continues to 112:2:1.
Content continuation is separately available: the exact four-word line is
quoted in AHd-B001, but its lexical-source occurrence is not the same
historical speech performance.

### `P-N2`: second nominal predication

`SOURCE_ACTUALITY` tuple:

`continuing named occupant ٱللَّهُ [nominative; line-initial] -> predication ->
definite nominative ٱلصَّمَدُ [line-final; determiner+stem]`

No seeker, bottle, rock, cloth, affair, stick, camel, cold, or milk from the
seven `ص م د` branches becomes a passage occupant. Each branch instead exposes
an interface around the exact predicate form.

### `P-W3A` and `P-W3B`: changed-voice counterfield

`SOURCE_ACTUALITY P-W3A`:

`لَمْ -> governs active IMPF.JUS.3MS يَلِدْ -> continuous referent as
grammatical controller/semantic source -> child/product role explicitly empty
because event is negated`

`SOURCE_ACTUALITY P-W3B`:

`وَ + لَمْ -> coordinates and governs passive IMPF.JUS.3MS يُولَدْ ->
continuous referent in affected/passive-subject role -> initiating parent role
suppressed by voice and event absent under negation`

The invariant is the WLD event schema and negated jussive imperfect; the
parameter vector changes active/passive, controller exposure, and vacancy
side. The first denies output from the referent; the second denies the referent
as output. No parent or child is introduced to fill either vacancy.

### `P-K4`: negated occurrence of a counterpart relation

`SOURCE_ACTUALITY` tuple:

`وَ + لَمْ -> governs يَكُن [IMPF.JUS.3MS, KWN] -> delayed nominative subject
أَحَدٌ -> accusative predicate كُفُوًا -> complement endpoint لَّهُۥ ->
counterpart-occurrence absent`

The syntax exposes an important role order distinct from word order: copula
then endpoint `له`, predicate `كفوا`, delayed subject `أحد`. Semantic topology
can be rendered without moving the surface nodes:
`candidate أحد -> counterpart predicate كفوا -> relative endpoint ه ->
negated occurrence`. Final `أحد` is both the delayed grammatical subject and,
through AHd-B002's exact negative-use tuple, an exhaustive candidate-class
interface. `كفوا` remains accusative because it is predicate; `أحد` remains
nominative because it is subject.

### Coreferential actuality path without role averaging

`هُوَ[pronoun/apposition head] -> ٱللَّهُ[quoted nominal] ->
ٱللَّهُ[new line's predication head] -> Ø[active 3MS controller of يلد] ->
Ø[affected passive subject of يولد] -> هُ[complement endpoint of كفوا]`.

`يَكُن` and its delayed subject `أَحَدٌ` form a different `3MS` agreement path;
the shared person/number/gender features do not create coreference.

The path records continuous reference. It does not make the same occupant a
second-person controller of `قل`, the delayed subject `أحد`, or any lexical
source example's camel, ruler, speaker, parent, vessel, or peer.

## V. Latent mapping interfaces

These are complete-tuple invariants. Every member keeps its actuality vector
and every delta is explicit.

### `LM-EXACT-P1`: exact content, changed occurrence

Member A is the positioned passage event `P-Q1`; member B is AHd-B001's source
utterance `قل هو الله أحد`. Payload: exact ordered four-word content. Delta:
passage occurrence versus a lexical-source quotation; positioned morphology
and syntax are supplied only for A. The same proposition/content schema can
therefore continue without declaring the performances or historical speakers
identical. QWL-B001 supplies an externalization interface, QWL-B012 an
unexternalized-content interface, QWL-B013 an adopted-belief interface, and
QWL-B014 a nonvocal indication interface. Each would be a new carrier and
fresh performance.

### `LM-AHAD-POLARITY`: one form through two source relations

Maximal mapping:

| parameter | 112:1:4 | 112:4:5 |
|---|---|---|
| exact form/lemma/root | `أَحَدٌ / أَحَد / ء ح د` | same |
| case/definiteness | nominative, indefinite | nominative, indefinite |
| local role | predicate of `ٱللَّهُ` | delayed subject of `يَكُن` |
| polarity | affirmative nominal predication | inside `لَمْ` negation |
| lexical relation directly activated | AHd-B001 absolute `أحد` / exact quote | AHd-B002 exhaustive `أحد` in negation |
| position | line 1 close, quote close | line 4 and passage close |

AHd-B003's composed unit, B004's firstness, B005's separated individuals, and
B006's mountain remain additional assembly ports; they do not overwrite the
two directly mapped contexts.

### `LM-KFW-P4`: counterpart schema with polarity and order change

KFW-B001 supplies exact `هذا كفء له أي مثله ...`, `كل شيء ساوى شيئا حتى يكون
مثله فهو مكافئ له`, and two-party peer/reciprocity tuples. `P-K4` supplies
`لم يكن له كفوا أحد`. The maximal invariant is:

`candidate comparand -> كفء/كفو predicate -> ل + comparison endpoint`.

Deltas: demonstrative or named first comparand becomes exhaustive delayed
`أحد`; source assertion is positive equality while passage relation is
negated; source predicate is nominative nominal `كفء` while passage uses
accusative copular `كفوا`; source order can place candidate before relation,
while passage advances endpoint and predicate and delays candidate. This is a
strong `LATENT_MAPPING` because the complete named relation and complement
topology recur. It does not assert any of KFW-B001's local domains (wealth,
lineage, marriage, war) in the passage.

### `LM-WLD-VOICE`: source/product relation rotated

The complete surface pair maps to WLD-B002/B003/B005:

| tuple | exposed source/controller | exposed affected/product | voice | event status |
|---|---|---|---|---|
| WLD-B003 `ولدت المرأة` | mother | child | active | asserted in source example |
| WLD-B003 `يوم ولد` / B004 `حين يولد` | initiator suppressed | born participant | passive/open | asserted as source expression |
| WLD-B005 `تولد الشيء من الشيء` | causal source thing | resulting thing | derivational/process | asserted in source definition |
| `P-W3A يلد` | continuing 3MS referent | child slot | active | negated |
| `P-W3B يولد` | suppressed parent/source slot | continuing 3MS referent | passive | negated |

The invariant is source-to-product transition; deltas are occupant, biological
versus general causal scale, grammatical voice, and polarity. WLD-B001's
number/gender range describes possible product classes only in its source.

### `LM-OCCURRENCE-VACANCY`: different kinds of not-filled position

The vacancy field is deliberately differentiated:

- `P-W3A`: event and child-output position absent under `لم`; controller is
  grammatically present.
- `P-W3B`: birth-of-affected event absent; initiating position is also
  suppressed by passive voice, a grammatical openness independent of negation.
- `P-K4`: occurrence of any counterpart relative to `ه` is absent; candidate
  class is exhaustive through AHd-B002.
- AHd-B002: eligible occupant of a domain is absent, covering one and upward.
- QWL-B005 `ما لم يكن`: represented event/content did not occur; `ما لم أقل`:
  utterance by attributed speaker did not occur even though an attribution did.
- QWL-B012 `لم أظهره`: content exists internally while external performance is
  absent.
- SMD-B002 `لا جوف له / ليس بأجوف` and `ليس فيه خدد`: a cavity or grooves are
  structurally absent from a solid object; no event is negated.
- KFW-B005 `ليست تامة كفأة`: yield exists but completion is absent.
- WLD-B005 `بينة مولدة وليست بمحققة`: generated evidence exists while
  verification is absent.
- ALH-B001 `لا يكون إلاها حتى يكون معبودا`: role is unavailable before a
  required prior relation; the vacancy has a prerequisite mechanism.

All share a typed open/absent position, but their consequences differ:
non-occurrence, no occupant, unexpressed content, no interior, incomplete
cycle, unverified result, or role not yet licensed. This mapping prevents the
negations from collapsing into one generic absence.

### `LM-SOURCE-TO-RESULT`: caused, expressed, born, and yielded products

Complete tuple topology:

`source/controller + material/content + operation/medium + temporal or spatial
boundary -> resulting product/state + aftermath`.

Members and exact parameter vectors:

| source tuple | source/controller | operation/medium | result | aftermath/status |
|---|---|---|---|---|
| QWL-B001 | composed letters / speaker | pronunciation | externalized saying | available as word, sentence, poem, address |
| QWL-B012 | psyche + conceived content | expression boundary still closed | no external token | content remains internal |
| WLD-B003 | mother | birth / placement | child born | day and attendants may frame event |
| WLD-B005 | source thing + cause | causal generation | resulting thing / new speech / artifact | may be mixed, fabricated, or unverified |
| KWN-B001 `كونه فتكون` | causer | causing occurrence | event occurs/presents | `أحدثه فحدث` |
| KFW-B005 | palm/camel herd + year | seasonal production / giving | fruit, offspring, milk, wool | complete, incomplete, or alternating next cohort |
| SMD-B007 | enduring camel under cold/barrenness | continuing through hardship | continuing milk flow | persistence |

Mappings preserve material and scale changes. No biological parent becomes a
speaker, and no utterance becomes milk; those are only alternative fillers of
typed source/process/product roles.

### `LM-CONTENT-CARRIERS`: one schema, many performances

QWL records themselves license a content-continuation network:

`internal conception (B012) -> vocal externalization (B001 through B002) ->
profuse repetition by a speaker (B003) -> effective ruler's word (B004) /
false invention or attribution (B005) / drawing to self (B006) / social spread
(B007) / reciprocal negotiation (B009) / control (B010) / supposition-like
grammatical operation (B011) / belief adoption (B013) / object-signification
(B014) / sincere care (B015) / definition (B016)`.

This is not one actuality chain: each arrow is a `LATENT_MAPPING` interface by
content or role schema and creates a fresh controller, medium, state, and
outcome. QWL-B008 exits the content network and enters the instrument-strike
network because its `القال` is a wooden implement.

### `LM-STRIKE-INSTRUMENT`: two exact force tuples

SMD-B006 `صمده بالعصا ... ضربه بها` maps maximally to QWL-B008 `القال الخشبة
التي تضرب بها القلة`:

`controller (open) -> wooden/stick instrument -> strike force -> affected
target -> impact`.

Deltas: `العصا` versus named `القال/الخشبة`; affected animate/unspecified
pronoun versus `القلة`; named verb/root context. KFW-B001's spear between two
horsemen supplies an assembly affordance (instrument mediating a pair), not an
exact strike mapping because its source assertion does not say the spear
strikes.

### `LM-PAIR-MEASURE`: peers, equality, and same-age relation

KFW-B001 explicitly names `المثل`, `النظير`, equality, and peer domains. WLD-B006
explicitly names `لدة الرجل تربه` and a person as another's same-age peer.
Invariant: two independently occupied positions compared under a specified
measure. Delta: general/domain-specific equality versus age-of-birth measure.
AHd-B003's unit-plus-tens and KFW-B004's two pieces are not automatically peers;
they enter assembly as count and pairing material only.

### `LM-BOUNDARY-COVER`: closing different exposed regions

- SMD-B003: stopper closes a bottle mouth; the vessel can have an interior.
- SMD-B004: cloth/kerchief/garment wraps a head; turban is excluded.
- KFW-B004: one/two sewn pieces cover the rear of tent/house.
- QWL-B016: definition supplies a conceptual `حد` around substance/accident.

Invariant: material or formal boundary is applied to an open/defined region.
Deltas: container mouth/body part/building rear/concept; stopper/wrap/sewn
piece/definition; physical closure versus conceptual delimitation. SMD-B002's
no-cavity solid is a counter-parameter: there is no interior opening to stop.

### `LM-DIRECTION-CONTROLLER`: seek, draw, divert, attend

SMD-B001 directs an intending seeker toward a relied-upon target; QWL-B006
draws a saying toward self; KFW-B002 diverts a group away from its current
direction; SMD-B005 places an overseeing attendant over an affair; QWL-B015
directs sincere care toward a thing. The maximal interface is controller,
route/orientation, content or affected participant, endpoint, and outgoing
relation. Parameter deltas are approach/appropriation/diversion/oversight/care,
physical versus attentional route, and whether endpoint is other, self, or an
affair.

### `LM-FORMAL-TRANSFORMATION`: supplied bases and changed forms

1. AHd-B001: `أحد` is a branch and original is `وحد`; additionally normalized
   base letters `احد` occur inside `واحد` after initial `و`, with the written
   `أ/ا` difference retained, while the source independently asserts
   `أحد بمعنى الواحد`.
2. ALH-B002: `إله -> حذف الهمزة + إدخال الألف واللام -> الله`; the full form,
   removed hamza, added determiner material, and specialization are retained.
3. WLD-B006: `ولدة -> حذف الواو -> لدة`; missing initial and recovered base
   are explicit.
4. Morphology: `قال -> قُلْ`, `ولد -> يَلِدْ / يُولَدْ`, `كان -> يَكُن`, and
   `كفو -> كفوا` are asserted lemma-to-inflection lineages. Exact containment
   is present only where recorded in Section II.
5. SMD-B002/B003 preserve `مصمت/مصمد`, `صمد/صماد`, and their exact differences;
   KFW branches preserve `كفء/كفاء/كفأة/تكفؤ` rather than flattening hamza and
   vowel-bearing forms.

The shared topology is base plus deletion/addition/inflection, but the actual
letters, controller (lexical history versus grammar), and semantic outcome
remain tuple-specific.

### `LM-END-DISTRIBUTION`: full surface ending vector through KFW-B003

KFW-B003 licenses comparison of a complete poem's rhyme letters, movements,
and inflection. The passage supplies the complete ordered boundary vector
`[أَحَدٌ, ٱلصَّمَدُ, يُولَدْ, أَحَدٌ]`. Surface parameters are:

| boundary | final consonant | final grammatical marking | carrier role |
|---|---|---|---|
| 1 | `د` | nominative tanwin | indefinite nominal predicate |
| 2 | `د` | nominative damma | definite nominal predicate |
| 3 | `د` | jussive sukun | passive verb |
| 4 | `د` | nominative tanwin | indefinite delayed subject |

The source's example `بعضها ميم وبعضها نون` is not the surface (the surface
letter stays `د`); its parameter interface makes the absence of consonantal
discord and the presence of movement/inflectional variation recordable. The
first/fourth exact return encloses the intervening two different boundary
types.

### `LM-TIME-SCALES`: instant, day, year, life phase, endurance

KWN-B001 supplies past/present occurrence; WLD-B003 a birth day and impending
time; KFW-B005 a one-year yield and alternating years/cohorts; KWN-B005 an old
man's present recollection of youth; KWN-B006 one night in a bad condition;
SMD-B007 persistence through cold/barrenness and beyond another population's
extinction; WLD-B006 equal age from birth. The invariant is a state or event
indexed to a complete temporal measure. Deltas include point/boundary,
seasonal cycle, night duration, lifetime contrast, coeval comparison, and
open-ended continuance.

### `LM-COUNT-GROUPING`: supplied complete count operations

AHd-B001 provides first unit; B002 scales one/two/upward under negation; B003
joins one to tens; B004 first/day; B005 distributes a group into individuals.
KFW-B004 alternates one or two cloth pieces; KFW-B005 divides a herd into two
production cohorts; WLD-B001 lets `ولد` denote one or many; WLD-B002 joins two
parents in a dual; WLD-B006 marks singular, dual, and plural peers. These map
to the surface's complete `[4,2,4,5]`, `[2,1,2,1]`, `[4,3,5,7]`, and recurrence
vectors only at the structural interface of unit/group/order. No numerical
source assertion is claimed to interpret the passage count.

## VI. Projective latent assemblies

Every assembly below is `LATENT_ASSEMBLY`. The ordered role list is the
canonical identity; bracketed IDs name the source actuality that supplied each
role. Variants preserve different fillers or consequences rather than selecting
among them.

### `LA-01`: command, content, carrier, crossing, receiver, aftermath

Functional spine:

`command/controller [P-Q1] -> content [P-Q1 exact quote / AHd-B001] -> possible
internal holding [QWL-B012] -> bodily medium [QWL-B002] -> vocal crossing
[QWL-B001] -> receiver/open social medium [QWL-B007 or open] -> aftermath`

- **Variant 01A, externalized exact content.** The exact quote fills content;
  tongue fills instrument; pronunciation releases the composed letters. A
  receiver remains open because the passage does not name one. If QWL-B007
  fills aftermath, a fresh carrier circulates the saying among people, with
  good/bad valuation still a branched parameter rather than assigned in
  advance.
- **Variant 01B, content held behind the boundary.** QWL-B012 supplies psyche
  as container and `لم أظهره` as unfilled vocal crossing. The command opens a
  performance role, but the projected mechanism stops before QWL-B001 output;
  exact content remains present internally. Its mismatch with an enacted
  command is itself the result: instruction and content exist, performance
  does not.
- **Variant 01C, fluent repetition.** QWL-B003 supplies a frequent/fluent
  controller; QWL-B001 supplies repeated vocal output; AHd-B001 `أحد أحد`
  supplies exact complete-form reiteration. Aftermath is increased token count,
  not new propositional content.
- **Variant 01D, effective word.** QWL-B004 supplies a title-holder, word as
  instrument, and execution as result. The quote can fill content schema, but
  the ruler remains only a projected controller and the passage does not assert
  worldly rank or enforcement.
- **Variant 01E, false or misattributed carrier.** QWL-B005 supplies either a
  fresh speaker saying what did not occur or an attributor assigning what a
  different person did not say. The exact contact `لم يكن` closes formally
  with line 4; the completed assembly produces false attribution as its own
  aftermath. It simultaneously records a severe mismatch with the passage
  tuple, whose content is source actual and never labelled false.
- **Variant 01F, appropriated content.** QWL-B006 draws a good/evil saying
  toward self. Route reverses from QWL-B001's inside-to-outside emission to
  outside-to-self acquisition. Result is held/claimed content; good and evil
  remain two variants.
- **Variant 01G, reciprocal speech.** QWL-B009 supplies at least two
  negotiators and an affair; each output becomes the other's input until the
  already-visited exchange state returns, recording one cycle. No infinite
  rewrapping occurs. The passage quote can be one content proposal, but no
  negotiating respondent is actualized.
- **Variant 01H, controlling speech.** QWL-B010 supplies a controller over an
  affected other. It fills force/outcome rather than receiver consent. QWL-B004
  effective word is an alternative filler, not a duplicate: title/rank and
  unilateral control have different source vectors.
- **Variant 01I, supposition-like performance.** QWL-B011 changes grammatical
  operation: question-scoped `تقول` or the named community's wider use of
  inflected `قلت` supplies a cognitive/evidentiary carrier. Content output is a
  supposition structure, not simply a pronounced report.
- **Variant 01J, belief continuation.** QWL-B013 supplies a new holder who
  adopts content as doctrine. The proposition recurs, but performance and
  controller are new; no vocalization is required.
- **Variant 01K, nonhuman indication.** QWL-B014 supplies a filled basin whose
  state indicates `قطني`. The quote role is replaced by a state-sign; tongue
  is vacant but performance succeeds as indication. This tests medium change.
- **Variant 01L, care or definition.** QWL-B015 can fill orientation/attention
  toward content; QWL-B016 can fill final boundary, delimiting the thing under
  discussion. These consequences differ: sustained concern versus a completed
  conceptual limit.
- **Variant 01M, instrument branch.** QWL-B008 cannot fill speech medium merely
  because it shares the root. When provisionally inserted, `القال` becomes a
  wooden striker and the utterance spine changes to the force assembly
  `LA-07`; failure to carry content is a typed rerouting, not discarded data.

### `LA-02`: directed approach to a relied-upon endpoint

Functional spine:

`initiator/seeker [SMD-B001] -> affair/need [SMD-B001] -> intention and route
[SMD-B001] -> relied-upon endpoint [SMD-B001] -> reception/result [open]`.

The exact surface predicate `ٱلصَّمَدُ [P-N2]` anchors every variant as formal
trigger while all local seekers and sought lords/houses remain lexical-source
occupants.

- **02A, saying as carried need.** QWL-B001 supplies externalized content as
  material; SMD-B001 supplies directed route and target. The unfilled receiver
  becomes the relied-upon endpoint, and aftermath can be reception, answer, or
  remain open; no answer is source-asserted.
- **02B, inward appropriation.** QWL-B006 reverses the route: saying is drawn
  to the controller's self rather than directed to another target. The shared
  directional spine survives with endpoint delta `other -> self`.
- **02C, diverted approach.** KFW-B002 fills force and turns a group away from
  its intended endpoint. Result is nonarrival at the SMD-B001 target. Incoming
  intention remains; outgoing direction changes.
- **02D, attending from above.** SMD-B005 fills positional controller and
  cognitive force: the controller overlooks and attends the affair rather than
  travels to it. KWN-B002 can fill relative place. Result is supervised
  proximity.
- **02E, sincere orientation.** QWL-B015 fills sustained care for the affair;
  SMD-B001 supplies target relation. Travel is unfilled but directed attention
  completes the functional route.
- **02F, hard/elevated endpoint.** SMD-B002 fills material and boundary with
  elevated, thick, hard, cavityless place; AHd-B006 can fill a separately
  sourced mountain occupant. The assembly makes an approach toward an elevated
  resistant mass. It does not identify the named mountain with any SMD source
  place or with the surface referent.
- **02G, house endpoint.** SMD-B001's `بيت مصمد` is already an actuality target.
  KFW-B004 projects a rear covering onto that house role. The result is a
  sought house with a covered rear; the covering event is latent, while the
  house's being sought remains source actual in its own tuple.

### `LA-03`: inside, opening, boundary, and crossing

Canonical roles:

`container/region -> possible interior -> opening/boundary -> applying agent
or force -> medium/closure -> inside/outside result`.

- **03A, stoppered vessel.** Container `القارورة` and stopper operation come
  together in SMD-B003 actuality. KFW-B002 adds an alternative force that tips
  or overturns the vessel. With stopper present, route outward is resisted;
  with stopper absent/open, content position becomes an unresolved spill port.
- **03B, cavityless solid.** SMD-B002 supplies region and explicit absence of
  interior. Attempting to install SMD-B003's stopper finds no cavity opening;
  completed result is typed mismatch `closure instrument -> no applicable
  opening`. This differs from an empty vessel.
- **03C, internal saying.** QWL-B012 supplies psyche/container and conceived
  content; QWL-B001 supplies a vocal boundary crossing; QWL-B002 supplies
  tongue medium. Before crossing, content exists but output is vacant; after
  crossing, a fresh external token exists.
- **03D, wrapped head.** SMD-B004 supplies body region, cloth/kerchief/garment,
  wrapping action, and covered result. KWN-B002's `موضع العمامة` can fill
  location, but SMD-B004 explicitly excludes the turban as its medium. Thus the
  projected site can be a turban site while the actual wrapper must remain one
  of the allowed alternatives.
- **03E, covered house rear.** KFW-B004 supplies one/two sewn pieces and house
  rear. One piece leaves its partner role optional; two pieces fill reciprocal
  seam positions. Result is a covered boundary rather than a closed container
  mouth.
- **03F, conceptual limit.** QWL-B016 fills region with substance/accident and
  closure with definition. There is no physical medium; result is a bounded
  account. It can receive the exact quote as proposed content in a variant, but
  the passage does not assert that the quote is a logician's definition.
- **03G, quote boundary.** `P-Q1` supplies outside command and inside quoted
  content. The speech verb does not enter the quote; QWL-B001 can project a
  crossing performance that carries the quote outward while preserving this
  syntactic boundary.

### `LA-04`: equality, candidate, measure, counterpart, return

Canonical roles:

`candidate A -> measure/domain -> candidate B/endpoint -> equality or
counterpart decision -> optional like-for-like return -> aftermath`.

- **04A, positive equality counterfield.** KFW-B001 fills both candidates and
  a domain among lineage, wealth, war, or marriage. Result is `مثل/نظير`.
  `P-K4` remains alongside as source-actual negative counterpart occurrence;
  projecting the positive tuple therefore creates an explicit polarity
  counterfield, never a correction of the passage.
- **04B, exhaustive no-candidate.** AHd-B002 fills candidate A as a complete
  eligible class under negation; `P-K4` fills measure and endpoint. The search
  ranges from one through more-than-one and returns no counterpart occupant.
  This is the completed vacancy mechanism of the surface tuple.
- **04C, same-age peer.** WLD-B006 supplies two people and birth-age as measure;
  KFW-B001 supplies peer decision. A peer result is possible in the lexical
  source assembly, while the surface counterpart position remains negated.
- **04D, reciprocal action.** KFW-B001 `فعلت به مثل ما فعل بي` fills first act,
  reverse route, and like return. One completed cycle returns to the same
  relational state and stops. QWL-B009's negotiation can replace action with
  alternating speech; source IDs keep those variants distinct.
- **04E, pair mediated by spear.** KFW-B001 supplies two horsemen and spear as
  mediator. SMD-B006/QWL-B008 can project strike force, producing two branch
  variants according to which instrument tuple supplies force. Without those
  projections, the spear only relates the horsemen as actually asserted.
- **04F, equality removed by inversion.** Begin with KFW-B001 equality state;
  KFW-B002 supplies tilt/overturn and explicit aftermath `إزالة المساواة`.
  Path is `equal pair -> applied inversion -> unequal orientation`. A return
  to equality would require a newly supplied reversing act and remains open.
- **04G, discordant endings.** KFW-B003 replaces social/material measure with
  rhyme letter/movement/inflection; candidates are positioned endings. The
  surface's four `د` endings fill the series, yielding consonantal recurrence
  with grammatical-movement variation rather than its source example's
  `م/ن` letter change.
- **04H, sewn pair.** KFW-B004 supplies one/two pieces. With two, each fills a
  counterpart material role and joining makes a covering. Equality is not
  source-asserted; complementary joining, not sameness, is the result.
- **04I, alternating cohorts.** KFW-B005 supplies two herd groups and year as
  phase measure. They correspond by alternating production, not simultaneous
  equivalence. Result is renewed output at successive phases.
- **04J, one and tens.** AHd-B003 supplies one plus tens and changes a count to
  eleven; it can fill candidate/count positions but not counterpart equality.
  Completed result is composition, revealing a role mismatch with peerhood.

### `LA-05`: production under active, passive, causal, and negated control

Canonical roles:

`source/controller -> material or carried state -> producing operation ->
boundary/time -> product/affected participant -> verification/continuation`.

- **05A, biological birth.** WLD-B002 supplies father/mother source roles;
  WLD-B003 supplies mother as active controller, birth, child, and day. An
  attendant from `ولدناها` can fill support/oversight without replacing the
  mother. Product number/gender branches through WLD-B001.
- **05B, impending birth.** WLD-B003 `أولدت حان ولادها` fills incoming
  pregnant/near-time state; product remains delayed until the birth boundary.
  The open product position is temporal, not negated.
- **05C, surface active denial.** `P-W3A` fills source/controller with the
  continuous passage referent and operation with active `يلد`; `لم` blocks
  transition. No product node is created. WLD-B003 source events remain actual
  only in their lexical tuples.
- **05D, surface passive denial.** `P-W3B` fills affected/result position with
  the same referent, suppresses initiator by passive voice, and `لم` blocks the
  event. This is not simply the reverse of 05C: the vacancy lies on the source
  side and the grammatical controller role has rotated.
- **05E, general causal generation.** WLD-B005 fills source thing, cause, and
  resulting thing; KWN-B001 fills causation-to-occurrence. Product can be new
  speech, mixed language/person, fabricated book, or unverified evidence.
  Each aftermath is its own branch.
- **05F, newly generated saying.** QWL-B012 supplies internal content;
  QWL-B001 supplies externalization; WLD-B005 supplies `المولد من الكلام إذا
  استحدثوه`. Result is newly coined speech. QWL-B005 can alternatively fill
  fabrication/false attribution; novelty and falsity are kept separate because
  one does not entail the other.
- **05G, annual yield.** KFW-B005 fills year, palm/camel source, and fruit or
  milk/wool/offspring product. Completion branches full/incomplete; two cohorts
  branch alternating phases. This is production rather than birth alone.
- **05H, occurrence without material product.** KWN-B001 fills controller and
  caused event `أحدثه فحدث`; result is presence/occurrence. It completes the
  source-to-result spine while leaving material product unfilled.

### `LA-06`: enduring herd-production cycle under adversity

This assembly gathers a concrete distributed mechanism without merging source
events:

`camel/herd source [SMD-B007; KFW-B005] -> cold and barrenness resistance
[SMD-B007] -> one-year production phase [KFW-B005] -> milk/wool/offspring
[SMD-B007; KFW-B005; WLD-B001] -> requester/beneficiary [KFW-B005] -> next
cohort or continuation [KFW-B005; SMD-B007]`.

- **06A:** one camel persists and continues milk through adversity; yearly
  measure and requester are projected from KFW-B005. Result is delivered milk.
- **06B:** two herd cohorts alternate birth/yield; SMD-B007 supplies adversity
  resistance. Result is phase-shifted renewal rather than simultaneous output.
- **06C:** KFW-B005's incomplete yield fills aftermath; persistence remains but
  product bundle lacks completion. This distinguishes survival from full
  productivity.
- **06D:** WLD-B003 supplies an attended camel/sheep birth event; KFW-B005
  supplies annual scale; WLD-B001 supplies product class. The birth event is
  latent because the source animals and occasions differ.

### `LA-07`: force transmission and changed direction

Canonical roles:

`controller -> instrument/force -> path -> affected participant(s) -> changed
orientation/state -> aftermath`.

- **07A:** SMD-B006 supplies stick, strike, and pronominal target.
- **07B:** QWL-B008 supplies wooden `القال`, strike, and `القلة` target.
- **07C:** KFW-B001 supplies spear between two horsemen; SMD-B006 supplies
  projected impact. Path branches toward either horseman; no strike is source
  actual in the KFW tuple itself.
- **07D:** KFW-B002 supplies force that tilts a thing, overturns a vessel, or
  diverts a group. Affected state becomes inclined/inverted/redirected rather
  than struck.
- **07E:** KFW-B002 supplies swaying woman/ship-like motion without an external
  controller; force role remains ambient/open, and result is repeated
  oscillation. The first return to the same orientation records one cycle.
- **07F:** QWL-B010 supplies control as nonmaterial force over another;
  QWL-B004 supplies an effective word as alternative instrument. Outcome is
  changed agency/obedience, not bodily impact.
- **07G:** KFW-B001's unspecified dual `بهما` wards off the sun's eye. Force
  direction is incoming from `عين الشمس` toward those two media; result is
  deflection away from the protected endpoint. This is not a strike but
  completes the resistance path.

### `LA-08`: place, elevation, station, oversight, and shelter

Canonical roles:

`occupant -> location/relative station -> vertical or social measure ->
boundary/shelter -> oversight or establishment -> resulting state`.

- **08A:** AHd-B006 supplies named mountain; SMD-B002 supplies elevated, thick,
  hard place and anchored rock; KWN-B002 supplies location. Result is a
  positioned elevated resistant mass, with mountain and rock kept as different
  projected fillers.
- **08B:** SMD-B005 supplies observer above an affair; KWN-B002 supplies
  relative place; QWL-B015 supplies sincere attention. Result is sustained
  oversight.
- **08C:** KFW-B004 supplies house/tent and covered rear; SMD-B001 supplies a
  sought house; KWN-B002 supplies established place. Result is a located,
  approached shelter with an enclosed rear.
- **08D:** KWN-B002 replaces physical height with social `مكانة/منزلة`;
  QWL-B004 supplies ruler below the greatest king. Result is a ranked station,
  not terrain.
- **08E:** KWN-B003 fills responsible person over another; SMD-B005 supplies
  oversight. The spatial `على` becomes duty/care topology; beneficiary and
  obligation fill the downstream roles.
- **08F:** KWN-B004 fills submissive occupant; vertical endpoint/authority
  remains open. This is a lowered relation that contrasts with SMD-B005's
  overlooking position but does not assert a shared scale.

### `LA-09`: formal passage sequence as a differentiated mechanism

Canonical surface roles are fixed, not regrouped:

`line 1 command+quoted predication -> line 2 compressed predication -> line 3
paired active/passive negations -> line 4 extended negated counterpart clause
with delayed subject`.

- **09A, enclosure.** Exact `أحد` occupies line-1 close and passage close;
  AHd-B001 supplies affirmative absolute-description relation at the first;
  AHd-B002 supplies exhaustive-negative relation at the second. The enclosed
  middle carries `الصمد`, then the active/passive WLD pair.
- **09B, bridge.** `وَلَمْ` at 112:3:3 joins within line; its exact return at
  112:4:1 joins across line. The first transition changes active to passive
  WLD; the second changes WLD event to KWN/KFW relation.
- **09C, expanding morphology.** Carrier counts `[4,3,5,7]` rise after line 1,
  while word counts `[4,2,4,5]` do not follow the same curve. The divergence is
  caused by determiner, conjunction, negator, preposition, and pronoun
  decomposition, not arbitrary counting.
- **09D, role-rotating `د` boundary.** KFW-B003 supplies letter/movement/
  inflection comparison. Consonant repeats; grammar changes; exact first/last
  word repeats. Result is recurrence with differentiated work.
- **09E, two-one alternation.** Clause counts `[2,1,2,1]` alternate while
  syntax-edge counts `[3,1,3,4]` break the final repetition. The delayed subject
  and complement/predicate attachments make line 4 structurally denser.
- **09F, singular/pair progression.** Line 1 closes with one predicate; line 2
  has one predicate; line 3 pairs two WLD events; line 4 opens a candidate class
  and negates counterpart relation. AHd-B003/KFW-B004/KFW-B005/WLD-B001 count
  facets remain live alternative models of unit, pair, group, and alternation,
  but none is selected as governing.

### `LA-10`: temporal carrier and state succession

Canonical roles:

`occupant -> incoming state -> time measure/boundary -> operation or endurance
-> outgoing state -> remembered/renewed aftermath`.

- **10A:** KWN-B001 supplies past or present occurrence; its causer can create
  a new event. Result is presence at a time.
- **10B:** KWN-B005 supplies one continuing man, youthful prior state, aged
  current state, and repeated `كنت` report. QWL-B012/B001 branch the report as
  internal memory or fresh vocal performance.
- **10C:** WLD-B003 supplies birth day as beginning boundary; WLD-B006 supplies
  coeval comparison; KWN-B005 supplies later age. Result is a life-phase route
  without asserting any named surface occupant traverses it.
- **10D:** KFW-B005 supplies annual recurrence; cohort alternation makes one
  cycle. A second return to the same phase stops path extension.
- **10E:** KWN-B006 supplies one night and bad condition; SMD-B007 supplies
  endurance through cold/barrenness. Result branches condition ended at dawn
  (open, not asserted) versus continuing beyond the measured night.
- **10F:** SMD-B007 supplies survival after others' annihilation. WLD-B001 can
  fill the perishing population role only projectively; persistence and lineage
  remain independently sourced.
- **10G:** AHd-B004 supplies first/day `الأحد`; WLD-B003 supplies birth day;
  KFW-B005 supplies year. These occupy day-name, event-day, and annual-measure
  roles without equating them.

### `LA-11`: form loss, addition, recovery, and positioned return

Functional spine:

`base form -> typed deletion/addition/inflection -> surface result -> later
exact contact -> recovered base`.

- **11A:** ALH-B002 `إله` loses hamza and receives `الألف واللام`, yielding
  specialized `الله`; passage positions 112:1:3 and 112:2:1 return the result.
- **11B:** WLD-B006 `ولدة` loses initial `و` to `لدة`; recovery of `ولدة`
  re-enters the field and meets WLD surface lemma `ولد` and passive `يولد` by
  the exact contacts already recorded.
- **11C:** AHd-B001 supplies `أحد` and origin `وحد`; normalized `احد` also lies
  within asserted `واحد` after initial `و`, with written `أ/ا` kept as a delta,
  and exact written `أحد` returns at both passage ends.
- **11D:** morphology transforms lemma `ولد` through active `يلد` and passive
  `يولد`; only passive retains `ولد` as an exact interior sequence. Voice and
  formal containment diverge in the paired surface positions.
- **11E:** morphology transforms `كفو` to accusative `كفوا`; syntax places it
  before delayed nominative `أحد`. Lexical hamza-bearing KFW terms remain root
  relations rather than forced exact spellings.
- **11F:** morphology relates `قال` to imperative `قل` and `كان` to jussive
  `يكن`; source `قلت` and `لم يكن` then provide independent exact contacts to
  the shorter surfaces. The loop closes at the recovered lemma/base and does
  not generate longer rewrapped variants.

### `LA-12`: persistence, sealing, and transmission countervariants

Canonical roles:

`material/content -> exposure to loss or hardship -> resistance/boundary ->
continued identity or transmission -> aftermath`.

- **12A:** SMD-B007 fills living carrier, cold/barrenness, survival, and
  continuing milk transmission.
- **12B:** SMD-B002 fills compact solid and absent cavity. Material persists by
  resistance; there is no transmitted interior content.
- **12C:** SMD-B003 fills vessel and stopper. Content may persist by being
  retained; transmission is blocked until boundary changes.
- **12D:** SMD-B004 fills head and wrap. Boundary protects/covers a body region;
  turban remains excluded.
- **12E:** QWL-B012 fills internal content and closed expressive boundary;
  QWL-B001 opens transmission. Identity of proposition may continue while
  token/performance changes.
- **12F:** QWL-B007 fills social medium and repeated circulation. Persistence
  now comes from renewed carriers rather than one durable material occupant.
- **12G:** KFW-B004 fills sewn covering and house rear; persistence is shelter
  integrity. KFW-B002 can overturn the house/vessel orientation as a competing
  disruption path.

The seven paths distinguish material survival, absence of interior, retention,
covering, unexpressed content, social recurrence, and structural shelter. They
are complementary affordances, not one asserted explanation.

## VII. Forward and backward rereading

### Forward activation

1. **112:1:1 opens a performance without naming its receiver.** The imperative
   activates every QWL controller/medium branch, but the exact syntactic quote
   constrains content to the whole `هُوَ ٱللَّهُ أَحَدٌ`. QWL-B012 makes prior
   internal content possible only as assembly; QWL-B001 makes vocal release;
   B002 provides tongue; B003--B016 branch changed carriers and outcomes.
2. **112:1:2--4 establish a referent and affirmative predicate.** The exact
   AHd-B001 quotation closes the first source circuit. AHd-B001 also releases
   `واحد`, `وحد`, firstness, and repeated `أحد أحد`, while the grammatical
   occurrence remains a single nominative predicate.
3. **112:2 shifts the named occupant to line opening.** Exact name recurrence
   provides actuality continuation. `ٱلصَّمَدُ` then activates seven distinct
   source tuples: approach endpoint; hard/no-cavity material; bottle stopper;
   head wrap; overseeing attention; stick strike; durability through hardship.
   None is chosen as the predicate's governing channel in this turn.
4. **112:3 changes from nominal state to negated event topology.** First the
   continuous referent occupies active source/controller position; then the
   same referent occupies passive affected position. WLD's parent, birth,
   offspring, causal-generation, and age-peer roles enter, but negation keeps
   the passage event slots vacant.
5. **112:4 carries exact `ولم` over the boundary.** KWN occurrence enters under
   negation. Endpoint `له`, counterpart predicate `كفوا`, and delayed candidate
   `أحد` build a complete negative relation. KFW-B001 supplies its positive
   topology counterfield; AHd-B002 supplies exhaustive candidate range. The
   passage closes by returning exactly to line 1's form with changed role and
   polarity.

### Backward reopening

1. **Final `أَحَدٌ` reopens initial `أَحَدٌ`.** Read backward, AHd-B002's
   exhaustive negative candidate first encounters KFW-B001's counterpart
   measure, then reaches AHd-B001's affirmative predicate and exact line-1
   quotation. The return changes what the first form can expose: it now carries
   a live positive/negative, predicate/subject, opening-close/enclosing
   counterfield without merging the occurrences.
2. **`كُفُوًا` reopens every earlier pair and correspondence.** KFW-B001's
   equality asks whether the active/passive WLD pair, the two nominal
   predications, the two Allah positions, and the two Ahad positions are equal.
   Full tuple comparison answers with parameter deltas: voice differs in WLD;
   predicates differ in definiteness/root; name positions differ in ordinal;
   Ahad role and polarity differ. KFW-B002 then exposes inversion/removal of
   equality; B003 exposes endings; B004 sewn complementarity; B005 alternation.
3. **`لَّهُۥ` returns to the named occupant.** Backward coreference moves from
   complement endpoint through implicit verbal agreement to line-2 and line-1
   `ٱللَّهُ` and pronoun `هُوَ`. Exact-letter contact `له` inside `إله/الله`
   also reopens ALH-B002's name-formation utterance, but only as form.
4. **`يَكُن` returns to occurrence and to `ما لم يكن`.** KWN-B001 supplies
   event/presence, past/current, causation, emphasis, and exception. QWL-B005's
   exact `لم يكن` contact supplies nonexistent content in a false-speaking
   source tuple. Backward formation therefore opens two distinct paths:
   negated counterpart occurrence, and fabricated report of non-occurrence.
   Their formal overlap is exact; their actuality is not.
5. **Repeated `وَلَمْ` returns into line 3.** The cross-line coordinator becomes
   the internal coordinator; copular negation becomes passive birth negation,
   then active birth negation. Each backward step retains the governed verb and
   does not let `لم` float as a generic negative theme.
6. **`يُولَدْ` recovers `ولد`; `يَلِدْ` does not contain it exactly.** Backward
   voice rotation opens parent/source, child/product, attendant, day,
   singular/plural/gender, new causal product, and same-age peer. WLD-B006's
   deleted initial waw then sharpens attention to the different formal loss in
   active `يلد` and retention in passive `يولد`.
7. **`ٱلصَّمَدُ` receives later vacancy and persistence fields.** The later
   absence of birth/counterpart can meet SMD-B002's no-cavity vacancy only as a
   typed comparison; SMD-B003 shows closure rather than no interior; SMD-B007
   shows continuance and outgoing milk, which reopens WLD/KFW production
   assemblies. Later `كفوا` also sends KFW-B004's house covering backward to
   SMD-B001's sought house and SMD-B004's wrap.
8. **Second `ٱللَّهُ` returns to first `ٱللَّهُ`, then `هُوَ`.** Line-initial
   predication head becomes quoted name/apposition, and the name-formation
   source tuple releases `إله -> الله`. The short `ال`, `ل`, and `ه` contact
   families become visible only after the later determiner/preposition/pronoun
   decomposition, so backward reading expands the first line's formal field.
9. **The final boundary vector returns to `قُلْ`.** Four `د` endings, exact
   first/final `أحد`, and KFW-B003's rhyme interface make the command's content
   a positioned acoustic/formal object. QWL-B001 can now carry not just a
   proposition but composed letters and their ordered boundary distribution
   into a fresh performance.

## VIII. Live open roles and unresolved attractions

These positions remain intentionally unfilled or multiply filled. They are
formation material, not deficiencies.

- `P-Q1` leaves the identity of the imperative's `2MS` controller beyond its
  grammatical features unstated; it also leaves an audience/receiver and the
  concrete performance medium open.
- The quote has exact content identity with AHd-B001 but no asserted identity
  with QWL-B003's frequent speaker, B004's ruler, B005's liar/attributor,
  B006's appropriator, B009's negotiators, B010's controller, or B011's
  supposer. Each remains a competing controller variant.
- QWL-B012's internal content seeks either QWL-B001 vocal crossing, QWL-B013
  belief continuation, QWL-B014 signification, QWL-B015 care, or QWL-B016
  delimitation. None is an entrance requirement for another.
- SMD-B001 exposes seeker, need, route, relied-upon endpoint, and response. The
  source fills the first four locally but leaves response/aftermath open.
  Projected speech, social group, or affair fillers remain alternatives.
- SMD-B002's absent cavity is attracted to SMD-B003's stopper because the
  latter requires an opening; the enacted mismatch `no opening` remains a
  distinct variant from a successfully stoppered bottle.
- SMD-B004 retains three allowed wrapping media and one excluded turban.
  KWN-B002's turban location may fill site, never the excluded medium.
- SMD-B005's affair can attract QWL-B009 negotiation, QWL-B015 care, QWL-B016
  definition, or SMD-B001 directed reliance. Each changes controller and
  outcome.
- SMD-B006 and QWL-B008 open unspecified striker/affected positions around two
  stick instruments; KFW-B001 opens two horsemen around a spear. Direction and
  target remain branched.
- SMD-B007 opens the identity of what persists, the hardship duration, and the
  recipient of continuous milk. KFW-B005 and WLD-B001 fill herd/product roles
  only projectively.
- `P-W3A` has an uninstantiated child/output because of negation. `P-W3B` has a
  suppressed initiating source because of passive voice and no birth event
  because of negation. These two vacancies must not fill each other into an
  actual lineage.
- WLD-B001 keeps number, sex, and age alternatives; B002 keeps father and mother
  distinct; B003 keeps mother, child, attendant, pregnant state, impending
  time, and completed day distinct; B004 keeps newborn-age and enslaved-status
  uses distinct.
- WLD-B005's causal source and reason are open for each product. New speech,
  mixed language/person, fabricated book, and unverified evidence have
  different aftermaths. Verification can remain absent even when generation
  is complete.
- WLD-B006's age measure can compare two persons, but neither is thereby
  `كفوا` under every KFW-B001 domain.
- `P-K4` exposes no actual counterpart occupant. KFW-B001 supplies possible
  comparison measures as a counterfield; AHd-B002 exhausts the candidate
  class; neither fills the negated subject position with an entity.
- KFW-B001 keeps equality, reciprocity, pairing, warfare/marriage domains,
  shielding, and spear mediation distinct. KFW-B002 opens removed equality and
  redirected path; B003 opens ordered ending comparison; B004 opens one/two
  material pieces; B005 opens two temporal cohorts. Their shared root is not a
  shared actuality event.
- KWN-B001's occurrence can receive an event content; KWN-B002's place can
  receive an occupant; B003's guarantee can receive a beneficiary; B004's
  submission can receive an authority; B005's `كنت` can receive a remembered
  youthful predicate; B006's bad state can receive an aftermath after night.
- AHd-B003's unit can join tens, B004's first can enter an إضافة/day sequence,
  B005's individuals can distribute from a group, and B006's mountain can fill
  a place/elevation role. None displaces AHd-B001/B002's direct surface
  activations.
- The full surface vectors attract KFW-B003 ending comparison, AHd count and
  distribution, KFW paired pieces/cohorts, and WLD singular/plural relations.
  These remain alternative formal enactments until later turns supply more
  structure.

## IX. Canonical live-field register

The following non-hierarchical channels remain available to the continuing
author:

| register | status | canonical source vector | current output/open return |
|---|---|---|---|
| exact quoted line | `LATENT_MAPPING` | `P-Q1 + AHd-B001` | same content, distinct occurrence; fresh carrier open |
| named referent path | `SOURCE_ACTUALITY` | passage pronoun/name/agreement/suffix | role-rotating continuous referent |
| Ahad enclosure | `LATENT_MAPPING` | `112:1:4 + 112:4:5 + AHd-B001/B002` | affirmative predicate / exhaustive negative subject |
| Samad predicate field | source trigger plus assemblies | `P-N2 + SMD-B001..B007` | direction, material, closure, cover, care, force, endurance variants |
| WLD voice pair | `LATENT_MAPPING` | `P-W3A + P-W3B + WLD tuples` | source/output vacancies kept apart |
| counterpart relation | `LATENT_MAPPING` | `P-K4 + KFW-B001 + AHd-B002` | no candidate occupant; positive counterfield retained |
| occurrence vacancies | `LATENT_MAPPING` | passage negations + named absence tuples | differentiated absence consequences |
| speech carrier system | `LATENT_ASSEMBLY` | `P-Q1 + QWL-B001..B016` | controller, medium, truth, receiver, aftermath variants |
| boundary/container system | `LATENT_ASSEMBLY` | `SMD-B002..B004 + KFW-B004 + QWL-B012/B016` | cavity, stopper, wrap, cover, expression, definition variants |
| generation system | `LATENT_ASSEMBLY` | `WLD + KWN-B001 + KFW-B005 + QWL` | biological, causal, verbal, seasonal, negated variants |
| equality/pair system | mapping plus assembly | `KFW + WLD-B006 + AHd + P-K4` | peer, reciprocal, inverted, discordant, complementary, alternating variants |
| force system | mapping plus assembly | `SMD-B006 + QWL-B008/B010 + KFW-B001/B002` | impact, mediation, diversion, control, resistance |
| time system | `LATENT_ASSEMBLY` | `KWN + WLD-B003/B006 + KFW-B005 + SMD-B007` | point, day, night, year, age, endurance |
| formal transformations | `LATENT_MAPPING` | explicit base/deletion/addition/inflection tuples | recovered bases and exact contacts closed |
| complete surface lattice | `LATENT_MAPPING` / assembly carrier | line/word/clause/morph/edge/boundary vectors | recurrence with changed grammatical work |

All paths are simple paths through typed states. The QWL reciprocal exchange,
KFW like-for-like return, KFW cohort alternation, and swaying orientation each
record one return cycle and stop. Identical exact-contact members are factored
by form, offset, position, and tuple ID; different source assertions,
controllers, role assignments, polarity vectors, consequences, and routes
remain separate. No source facet has been deleted for slightness or mismatch,
and no channel has yet been promoted to a governing interpretation.
