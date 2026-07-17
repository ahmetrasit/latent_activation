# Activation Reservoir: 112:1-4

This is a formation field, not a settled reading. `O:` marks an occupancy node or identity-preserving edge; `C:` marks a coalition node or relation-preserving link. A shared spelling, root, position, role, or topology never silently changes `C:` into `O:`. Every lexical occurrence below remains local to its source assertion unless an exact surface or syntax relation binds the same occupant.

## Positioned surface lattice

### Complete carrier set and count vectors

The supplied positioned object has four lines, fifteen space-delimited surface words, nineteen morphological carriers, eleven supplied syntax edges, and six local predicative/verbal occurrences when the command and its quoted nominal clause are counted separately. The complete vectors are:

- surface words by line: `[4, 2, 4, 5]`;
- morphological carriers by line: `[4, 3, 5, 7]`;
- supplied syntax edges by line: `[3, 1, 3, 4]`;
- local clause/predication occurrences by line: `[2, 1, 2, 1]`: the command with its quoted nominal predication; one nominal predication; two coordinated negated verbal predications; one negated copular predication.

No vector is substituted for another. In particular, the second word of line 2 is one written word but two morphological carriers (`ٱل` + `صَّمَدُ`); line 3 has four written words but five carriers because the third word is `وَ` + `لَمْ`; line 4 has five written words but seven carriers because its first word is `وَ` + `لَمْ` and its third is `لَّ` + `هُۥ`.

| line | positioned surface carriers | morphological expansion | beginning | ending |
|---|---|---|---|---|
| `112:1` | `1 قُلْ` · `2 هُوَ` · `3 ٱللَّهُ` · `4 أَحَدٌ` | `V.IMPV.2MS` · `PRON.3MS` · `PN.NOM` · `N.M.INDEF.NOM` | imperative speech carrier | indefinite nominative predicate in `د` |
| `112:2` | `1 ٱللَّهُ` · `2 ٱلصَّمَدُ` | `PN.NOM` · `DET` + `N.MS.NOM` | repeated proper-name form | definite nominative predicate in `د` |
| `112:3` | `1 لَمْ` · `2 يَلِدْ` · `3 وَلَمْ` · `4 يُولَدْ` | `NEG` · `V.IMPF.3MS.JUS` · `CONJ` + `NEG` · `V.IMPF.PASS.3MS.JUS` | bare negator | passive jussive in `د` |
| `112:4` | `1 وَلَمْ` · `2 يَكُن` · `3 لَّهُۥ` · `4 كُفُوًا` · `5 أَحَدٌۢ` | `CONJ` + `NEG` · `V.IMPF.3MS.JUS` · `P` + `PRON.3MS` · `N.M.INDEF.ACC` · `N.M.INDEF.NOM` | conjoined negator | delayed nominative subject in `د`, with the written final recitation mark retained |

The line-initial sequence is `قُلْ | ٱللَّهُ | لَمْ | وَلَمْ`: command, nominal name, bare negation, conjoined negation. The line-final sequence is `أَحَدٌ | ٱلصَّمَدُ | يُولَدْ | أَحَدٌۢ`: noun, noun, verb, noun; indefinite nominative, definite nominative, passive jussive, indefinite nominative. All four complete endings terminate in written `د`, while their case/mood and definiteness work changes. Lines 1 and 4 enclose the passage with the lemma `أَحَد`, masculine indefinite nominative in both positions, but the first is a predicate inside quoted affirmative predication and the last is the delayed subject of a negated copula. The two written forms remain distinct: `أَحَدٌ` and `أَحَدٌۢ`.

The content-root sequence, leaving particles and pronouns visible rather than deleting them, is:

```text
ق و ل -> PRON.3MS -> ء ل ه -> ء ح د
ء ل ه -> DET + ص م د
NEG -> و ل د(active) -> CONJ + NEG -> و ل د(passive)
CONJ + NEG -> ك و ن -> P + PRON.3MS -> ك ف ء -> ء ح د
```

This supplies two exact `ٱللَّهُ` positions, two surface `أَحَد` positions, two coordinated `و ل د` occurrences with changed voice, three `لَمْ` carriers, two conjunctive `وَ` carriers, one definite article, one preposition, and a distributed set of five 3MS carriers (`هُوَ`, the controllers/subjects encoded by `يَلِدْ`, `يُولَدْ`, and `يَكُن`, and suffix `هُۥ`). Shared 3MS does not merge those five occupants.

### Supplied surface bindings

The syntax graph is retained with its own endpoint indices, including indices that subdivide attached surface material differently from the space-delimited word count:

```text
SYN-1  q:112:1:1 قُلْ
       -> quoted_complement {exact span قُلْ | هُوَ}
       -> q:112:1:2, the content هُوَ ٱللَّهُ أَحَدٌ

SYN-2  q:112:1:3 ٱللَّهُ
       -> predication
       -> q:112:1:4 أَحَدٌ

SYN-3  q:112:1:2 هُوَ
       -> apposition (supplied as a possible appositional analysis)
       -> q:112:1:3 ٱللَّهُ

SYN-4  q:112:2:1 ٱللَّهُ
       -> predication
       -> q:112:2:2 ٱلصَّمَدُ

SYN-5  q:112:3:1 لَمْ
       -> particle government, jussive negated imperfect
       -> q:112:3:2 يَلِدْ

SYN-6  q:112:3:2 يَلِدْ
       -> coordination
       -> q:112:3:5 يُولَدْ

SYN-7  q:112:3:4 وَلَمْ
       -> particle government, jussive negated passive imperfect
       -> q:112:3:5 يُولَدْ

SYN-8  q:112:4:2 وَلَمْ
       -> particle government, jussive negated imperfect
       -> q:112:4:3 يَكُنْ

SYN-9  q:112:4:5 كُفُوًا
       -> prepositional-complement relation
       -> q:112:4:4, pronoun هُۥ governed by لَـ

SYN-10 q:112:4:3 يَكُنْ
       -> kana_predicate
       -> q:112:4:5 كُفُوًا

SYN-11 q:112:4:3 يَكُنْ
       -> delayed subject
       -> q:112:4:6 أَحَدٌ
```

`SYN-3` licenses a local appositional occupant binding inside line 1: the pronoun node and named node can occupy the same local referential position under that supplied analysis. `SYN-2` and `SYN-4` bind predicates to their local named subjects. Exact recurrence of the name between those lines is, by itself, only a formal coalition interface. `SYN-5` through `SYN-8` bind polarity and mood, not a positive event result. `SYN-6` binds the two verbal relations by coordination while preserving active and passive occurrences separately. `SYN-9` keeps the pronoun as the referential endpoint of the counterpart relation, not as the delayed subject. `SYN-10` keeps `كُفُوًا` accusative and `SYN-11` keeps `أَحَدٌۢ` nominative despite their delayed order.

### Local surface tuples and open occupancy ports

`O-S1-SAY`: the imperative occurrence has a grammatically encoded 2MS controller/addressee position, an unspecified utterance initiator, and the exact quoted content schema `هُوَ ٱللَّهُ أَحَدٌ`. The syntax carries that content from the command into the quote port. It does not make the addressee, speaker, pronoun, named subject, and predicate one occupant.

`O-S1-PRED`: local pronoun `هُوَ` (3MS) -> appositional binding -> local `ٱللَّهُ`; local `ٱللَّهُ` -> nominative predication -> `أَحَدٌ`. This occurrence has no supplied temporal change, material, or aftermath.

`O-S2-PRED`: a separate local `ٱللَّهُ` -> nominative predication -> definite `ٱلصَّمَدُ`. The exact name and parallel nominal form expose coalition interfaces with `O-S1-PRED`; they do not by themselves hand off the line-1 occupant.

`O-S3-ACT`: `لَمْ` scopes an active imperfect jussive occurrence. The controller is grammatically 3MS but lexically unfilled. A generated child/product endpoint opened by `وَلَدَ` is denied, not produced. No child occupant may be installed in the negated result port.

`O-S3-PASS`: conjunction aligns a second, passive imperfect jussive occurrence. Its grammatically 3MS affected/subject position is distinct from the active controller unless an identity edge is separately supplied. The external begetter/initiator is suppressed by passive voice; the occurrence and its result are negated. Coordination transports the relation between the clauses, not either local occupant.

`O-S4-KWN`: conjunction plus `لَمْ` scopes a jussive copular occurrence. `أَحَدٌۢ` is the delayed nominative subject; `كُفُوًا` is the accusative predicate; `هُۥ` is the 3MS referential endpoint selected by `لَـ` inside the counterpart relation. The existence/predication of any such subject is denied. This is an absence with typed consequence: the subject class is vacant under negation, and no positive counterpart result exists.

## Exact-contact closure

The written forms are retained beside a detection form stripped of vocalization and ordinary decoration. Detection never replaces the written node. Hamza-seat, article, affix, case, mood, voice, vowel, and final-mark differences remain attached as deltas.

### Whole-utterance and named-form circuits

`X-QUOTE` is a complete collision rather than a topical resemblance:

```text
surface 112:1  قُلْ هُوَ ٱللَّهُ أَحَدٌ
-> detection  قل هو الله احد
-> ء ح د/B001 source assertion  قل هو الله أحد
-> recovered terms  قل | هو | الله | أحد
-> positioned return 112:1:1-4
-> later returns  ٱللَّهُ at 112:2:1 | أَحَدٌۢ at 112:4:5
```

The complete quoted assertion stays intact when its four terms circulate. The lexical record does not import the lexical examples' occupants into the surface quote. The later name and final `أحد` receive form/position links, not automatic identity with the line-1 participants.

`X-AHAD` begins at both surface forms `أَحَدٌ` and `أَحَدٌۢ`, recovers the supplied base `أَحَد`, and closes through all supplied complete containing forms: `أحد`, `وأحد`, `واحد`, `واحدا`, `الواحد`, `للواحد`, `والواحد`, `أحدكما`, `فأحدهن`, `استأحد`, `استأحدت`, `الأحد`, `الأَحَدِيَّة`, `أُحُد`, `إحدى`, `إحداهما`, and `أحدثه`. Each containment keeps its delta: `أُحُد` changes vocalization while retaining the consonantal form; `الواحد` and `واحد` contain normalized `احد` after an initial `و`; `فأحدهن` adds `فـ` and `ـهن`; `أحدكما` adds `ـكما`; `استأحدت` adds `استـ` and `ـت`; `الأحدية` adds article and `ـية`; `إحداهما` has initial hamza-seat and feminine/dual material; `أحدثه` continues with `ثه` and belongs locally to a causation-of-occurrence assertion. None of those deltas is erased.

`X-ALLAH` joins the two exact surface `ٱللَّهُ` forms, the whole quote in ء ح د/B001, and the ء ل ه source nodes `الله`, `ألله`, `والله`, `اللهم`, `واللهم`, and the asserted derivation `الله <- إله` by deletion of hamza and addition of `الألف واللام`. `يا ألله`, `الله ما فعلت`, `والله ما فعلته`, `لاه أنت`, `لاه أبوك`, `لهنك`, and `لهنا` remain complete utterance-local forms. The surface composite `لَّهُۥ` yields the complete unvocalized form `له`; that form also occurs as the final two letters of `الله`, but this contact transports only letters and containment. It does not identify the line-4 pronoun with either named occupant.

`X-SAMAD` retains surface `ٱلصَّمَدُ` as article `ٱل` plus stem `صَّمَدُ`; the base `صمد` returns in `صمد`, `صمدا`, `صمده`, `صمدته`, `صمدت`, `وصمدت`, `وصمده`, `وصمدته`, `يصمد`, `يصمده`, `مصمد`, `المصمد`, `صمدتها`, `وصمدتها`, and `أصمدها`. `الصمدة` and `وصمدة` contain the complete `الصمد` detection form while adding `ـة`; their rock node remains distinct from the surface predicate. Forms with an inserted long vowel, such as `الصماد`, `مصماد`, and `صمادة`, retain that insertion and do not collapse into exact `صمد` even though their root field is supplied.

`X-WLD` keeps `يَلِدْ` and `يُولَدْ` distinct. The lemma/base `وَلَدَ` is explicitly supplied for each; `ولد` is directly contained in `يولد`, `تولد`, `مولد`, `ولدة`, `ولدت`, `الولد`, `أولدت`, `مولدا`, `مولدة`, `ولدان`, `ولدون`, `المولد`, `ولدها`, and `ولدناها`, with all prefixes, long vowels, suffixes, number, gender, and voice differences retained. Surface `يَلِدْ` does not contain written `ولد` because its weak radical is absent; its route to the base is morphological, not an invented substring. Surface `يُولَدْ` occurs without vocalization as the exact source form `يولد` in the assertions `الوليد الصبي حين يولد` and `الوليد يقال لمن قرب عهده بالولادة`.

`X-KWN` starts with surface `يَكُن`, supplied lemma `كَانَ`, and root `ك و ن`. Exact `يكن` returns in `تقول باطلا أي قال ما لم يكن`. `كان` returns as `كان`, `كانت`, and inside the complete derivational/location forms `مكان`, `المكان`, `المكانة`; `كأنه` retains its attached pronoun; `الاستكانة` retains its derivational envelope. The lexical `يكون` and `فتكون` retain their medial `و`, so their relation to surface `يكن` is morphological rather than exact containment. The source form `أحدثه` also enters `X-AHAD` by its initial normalized `أحد`, but its local tuple remains causation of occurrence.

`X-KFʾ` retains surface `كُفُوًا`, supplied base `كُفُو`, and root `ك ف ء`. The source form `تكفؤا` contains the detection form `كفوا` after its `تـ` when hamza-seat/orthographic difference is registered; the exact writings `كُفُوًا` and `تكفؤا` remain separate. The root-family forms `كفء`, `الكفء`, `الكفئ`, `تكافؤ`, `مكافئ`, `مكافأة`, `كافأت`, `نكافئ`, `كافأ`, `كفأت`, `أكفأت`, `الإكفاء`, `الكفاء`, and `الكفأة` remain inflectionally and derivationally typed rather than being flattened to the surface token.

`X-QUL` preserves surface `قُلْ`, lemma `قَالَ`, root `ق و ل`, and the exact command in `قل هو الله أحد`. Its detection form `قل` also occurs as a complete embedded sequence in `أقل`, `قلت`, `القلة`, `قلب`, `وقلبه`, and `والقلب`. Thus the command enters the complete local assertions `قولتني ما لم أقل`, `بنو سليم يجرون متصرف قلت ... مجرى الظن`, `القال الخشبة التي تضرب بها القلة`, and `الإكفاء قلب الشيء كأنه إزالة المساواة`. These are formal entries into enactment: the command is not thereby false attribution, conjecture, a struck object, or inversion.

`X-HUWA` keeps surface `هُوَ` and source `هو`, including attached `وهو` and `فهو`, as base-plus-prefix forms. It touches complete equations such as `فالإله على هذا هو المعبود`, `أحد بمعنى الواحد وهو أول العدد`, `كل شيء ساوى شيئا حتى يكون مثله فهو مكافئ له`, and `الولد وهو للواحد والجميع`. Every pronoun remains local; the repeated form transports no antecedent.

`X-LAM` contains the three surface negators, preserving bare `لَمْ` versus attached `وَلَمْ`. Exact source clauses include `ما لم أقل`, `قولتني ما لم أقل`, `في نفسي قول لم أظهره`, and `قال ما لم يكن`. Because `لم` is itself a complete supplied form, closure also registers it across article-plus-`م` boundaries inside complete forms such as `المثل`, `الملك`, `المبرز`, `المركب`, `المصمت`, `المطلق`, `المقول`, `المكان`, `المولد`, `المعبود`, `المعتمد`, `المعدود`, `المقصود`, `المكانة`, `الموضع`, `المساواة`, `المقابلة`, `المقاولة`, `المكافأة`, `المماثلة`, `المناكحة`, `المنزلة`, `المولود`, and their supplied prefixed variants. This wide fan is retained as form-only contact: the negative particle does not confer negation on those nouns.

`X-LAHU` starts from morphological `لَّ` + `هُۥ` and the combined surface carrier `لَّهُۥ`. Exact `له` and its containing forms include `لله`, `الله`, `أله`, `إله`, `قوله`, `مثله`, `يأله`, `فالإله`, `والإله`, `الآلهة`, `التأله`, `قولهم`, `فأصله`, `حصوله`, `ومثيله`, and `يستعمله`. The complete source phrase `هذا كفء له أي مثله` and the longer equality phrase `كل شيء ساوى شيئا حتى يكون مثله فهو مكافئ له` enact the same typed counterpart endpoint found locally in line 4. Other `له` contacts carry only their exact local possessive, beneficiary, or pronoun relation.

### Consonantal and boundary microcontacts

The explicitly supplied one-letter morphology carriers `وَ` and `لَّ`, the root consonants, and the passage endings create a dense microcontact field. It is kept as a typed fan rather than interpreted globally:

- final `د` closes all four lines and closes the roots/forms `أحد`, `صمد`, and `ولد`. The ordered return is `[ء ح د, ص م د, و ل د, ء ح د]`, with the first root returning at the passage end. The same consonant bears nominative tanwin, nominative `ـُ`, jussive sukun, and nominative tanwin-with-final-mark in order.
- `وَ` is a complete conjunction carrier at the third word of line 3 and first word of line 4. The same letter is a root consonant in `ق و ل`, `و ل د`, and `ك و ن`, and it is an explicitly named origin or deleted consonant in `أحد فرع والأصل الواو وحد` and `اللدة نقصانه الواو لأن أصله ولدة`. These nodes share letter form only until the complete derivational assertions supply a transformation relation.
- `لَّ` at line 4 is a preposition governing `هُۥ`. `ٱل` at line 2 is a definite article. The double lam inside `ٱللَّهُ` belongs to the proper-name form. Their exact `ل` contacts do not exchange government, definiteness, or occupant.
- `ه` appears in `هُوَ`, suffix `هُۥ`, and the end of `الله`, and throughout supplied attached pronouns. Position and attachment are retained; no cross-node coreference is inferred.
- hamza participates differently in roots `ء ح د`, `ء ل ه`, and `ك ف ء`, and in the asserted deletion from `إله` to `الله`. Hamza-seat normalization opens comparison but the written difference remains part of every node.

### Recurrent complete lexical interfaces

The following complete forms expose cross-record circuits while keeping their local assertions intact:

- `واحد/الواحد`: `أحد بمعنى الواحد`, `القول والقيل واحد`, `الولد ... للواحد والجميع`, and the negative count `ولا واحد ولا اثنان فصاعدا`. The relation may be lexical equivalence, token identity, singular count, or a denied member; those parameter vectors do not merge.
- `أول`: `أحد ... أول العدد`, `يوم الأحد أي يوم الأول`, and the initial sequence inside supplied `أولاد/أولادها`. The embedded contact does not turn offspring into an ordinal.
- `إحدى`: `إحدى عشرة` and the base within `إحداهما بالأخرى`. One is a numeral term; the other selects one of a pair of panels.
- `أمر`: the object aimed at and relied on in ص م د/B001, the matter overlooked and cared about in ص م د/B005, the matter negotiated in ق و ل/B009, and the occurrence in `كان الأمر` in ك و ن/B001. Each has its own controller and outcome.
- `الشمس`: the sun locally named `الإلاهة` because a people worshipped it in ء ل ه/B001, and `عين الشمس` from which two unspecified things are used to counter/ward in ك ف ء/B001. Exact naming yields a coalition interface, not a shared event occupant.
- `العمامة`: excluded from the head-wrapping materials in ص م د/B004 and made the object whose position is named in `موضع العمامة` in ك و ن/B002. This exact object term exposes an exclusion/position vacancy comparison.
- `بيت/البيت`: `بيت مصمد أي مقصود` in ص م د/B001 and the house/tent whose rear is covered by sewn panels in ك ف ء/B004. The two house nodes remain local.
- `ضرب`: `صمده بالعصا ... ضربه بها` and `القال الخشبة التي تضرب بها القلة`. The shared operation and specified stick-like instruments expose a topology link without identifying agent, instrument, or affected object.
- `مثل/مثله`: the counterpart and equality assertions throughout ك ف ء/B001 and the same-age peer equation `لدة فلان وتربه` / `مثيله في السن` in و ل د/B006. The surface `كُفُوًا` receives the counterpart schema, but no source-example person fills its delayed subject.
- `نتاج` and `أولاد`: the annual camel/palm yield field in ك ف ء/B005 and the offspring field in و ل د. This supports a product-schema coalition while every herd, parent, child, year, and yield remains source-local.
- `يوم`: `يوم الأحد` in the first-day/name assertion and `يوم ولدت؛ يوم ولد` in the birth assertion. The temporal-position relation travels; no day identity does.
- `أصل/أصله`: origin assertions for `أحد <- وحد`, `الله <- إله`, `اللدة <- ولدة` with loss of waw, and `الكينة <- الكون`. These form a transformation coalition whose actual deletion/addition vectors remain separate.
- `الناس`: circulated saying among people in ق و ل/B007 and an event occurring between people in ك و ن/B001. The class recurrence does not identify any people.
- `فلان` and attached forms recur across speech, concern, equality, guarantee, place, and peer assertions. They remain placeholders local to each complete example; the exact form is not a universal occupant socket.

## Intact source-carrier chambers and local tuples

Every carrier quoted in this section is held as a complete source assertion before its facets are released. Semicolon-separated assertions generate distinct event occurrences even when they remain inside one branch chamber.

### The `ء ح د` chamber: unity, exhaustive vacancy, number, firstness, separation, named place

**`AHD-B001` carrier:**

> أحد فرع والأصل الواو وحد (maqayis); أحد بمعنى الواحد وهو أول العدد (sihah); قل هو الله أحد (sihah;mufradat); يستعمل مطلقا وصفا في وصف الله تعالى وأصله وحد (mufradat); أحد أحد (sihah)

`AHD-B001-T1` asserts a derivational branch/origin relation: surface term `أحد` is a branch, original consonant is named as `الواو`, and origin form is `وحد`. `T2` equates `أحد` with `الواحد` and gives that term ordinal position `أول العدد`. `T3` is the complete source/surface quote collision. `T4` supplies unrestricted descriptive use, a locally named described participant `الله تعالى`, and the origin `وحد`. `T5` repeats the complete term twice and assigns repetition the operation of emphasis. The branch image `الأَحَدِيَّة والوَحْدَة` keeps both derived state nouns and their different initial consonantal forms active.

**`AHD-B002` carrier:**

> لا أحد في الدار؛ ما في الدار أحد (sihah); أحد في النفي لاستغراق جنس الناطقين ولا واحد ولا اثنان فصاعدا (mufradat); فما منكم من أحد عنه حاجزين (sihah;mufradat)

`AHD-B002-T1a/b` supplies two word-order realizations of a negated occupancy relation: `لا أحد` before the locative and `ما في الدار أحد` with the indefinite term delayed after the locative. `T2` assigns `أحد` under negation an exhaustive scope over the class of speaking/addressable beings and explicitly extends the denied count from one to two and upward. `T3` keeps `منكم`, `من أحد`, `عنه`, and plural `حاجزين` in their own participant arrangement. This chamber directly contacts line 4 through negation plus delayed indefinite `أحد`, but it does not fill line 4 with a house, speakers, or blockers.

**`AHD-B003` carrier:**

> أحد واثنان وأحد عشر وإحدى عشرة (sihah); الواحد المضموم إلى العشرات نحو أحد عشر وأحد وعشرين (mufradat); فأحدهن أي صيرهن أحد عشر (sihah)

`AHD-B003-T1` orders and differentiates the count forms `أحد`, `اثنان`, masculine compound `أحد عشر`, and feminine `إحدى عشرة`. `T2` is a composition operation: `الواحد` is joined to tens, with eleven and twenty-one as realized results. `T3` is causative transformation: an unspecified controller acts on feminine-plural `هن`, and the outgoing result is `أحد عشر`. The attached form is retained as `فـ + أحد + هن`. Surface `أحد` can carry the exact count form into coalition, but no surface participant becomes a counted collection.

**`AHD-B004` carrier:**

> أن يستعمل مضافا أو مضافا إليه بمعنى الأول (mufradat); أما أحدكما (mufradat); يوم الأحد أي يوم الأول (mufradat); يوم الأحد يجمع على آحاد (sihah)

`AHD-B004-T1` makes genitive/additive position alter the term's supplied sense to `الأول`; both possessor directions remain open. `T2` presents `أحدكما` as base plus second-person dual suffix, selecting one within a two-member field without naming which member. `T3` equates the named day `يوم الأحد` with `يوم الأول`. `T4` gives plural transformation `الأحد -> آحاد` while keeping the day-name carrier. The temporal day, dual pair, additive relation, and first-position schema remain independent ports.

**`AHD-B005` carrier:**

> ما استأحدت بهذا الأمر أي ما انفردت به (maqayis); استأحد الرجل انفرد (sihah); جاءوا آحاد أحاد (sihah)

`AHD-B005-T1` negates a controller's having acted alone with respect to `هذا الأمر` and explicitly equates `استأحدت به` with `انفردت به`. `T2` positively gives a local man the transition into acting/being alone. `T3` gives a plural arriving group a distributed manner/result, `آحاد أحاد`, individuals one by one. Singular agency, distributed plurality, negated exclusivity, and arrival remain distinct parameter vectors.

**`AHD-B006` carrier:**

> أحد جبل بالمدينة (sihah)

`AHD-B006-T1` is a naming/predication tuple: consonantally matching but differently vocalized `أُحُد` is a mountain, with `بالمدينة` as location. The mountain and city are local occupants. Exact contact with either surface `أحد` transports spelling and predication topology only.

### The `ء ل ه` chamber: worship relations and proper-name transformations

**`ALH-B001` carrier:**

> أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)

`ALH-B001-T1` names one root-origin relation, `التعبد`. `T2` predicates `الإله` of `الله تعالى` because the latter occupies a passive result/state, `معبود`; worshipper remains open there. `T3` gives a man control of reflexive/devotional `تأله` and equates its occurrence with `تعبد`. `T4` names the sun `الإلاهة` because a local people repeatedly worshipped it; namers, worshippers, and worshipped sun are separate roles. Further tuples equate `التأله` with worship/devotion, `أله` with performing worship, and `مألوه` with the passive role `معبود`; classify local idols as `الآلهة`; make `التأليه` a causative operation of rendering/assigning worship; and state a prerequisite topology, `لا يكون إلاها حتى يكون معبودا`. `معبوداتهم من الأصنام والأوثان آلهة` retains possessors, worshipped objects, material classes, and resulting designation. `إلاهتك وعبادتك` preserves the attached second-person possessor and equation. `إله اسما لكل معبود` opens a universally quantified naming schema, not a global occupant port.

**`ALH-B002` carrier:**

> فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

`ALH-B002-T1` repeats the deity/name predication and passive worshipped rationale. `T2` supplies exact self-equation `اسم الله الأكبر هو الله`. `T3` maps oath utterance `الله ما فعلت ذاك` to intended `والله ما فعلته`, preserving added conjunction/oath `و`, negation, first-person actor, demonstrative object, and suffix difference. `T4` maps `لاه أنت` to `لله أنت`. `T5` records `لا هم اغفر لنا` as an invocation with imperative forgiveness and first-person-plural beneficiary. Other invocation tuples keep `يا ألله اغفر لي`, and the exact equation `اللهم بمعنى يا ألله`; `لاه أبوك`, `لهنك`, and `لهنا` remain complete named usage forms. The final transformation explicitly starts from `إله`, deletes its hamza, adds `الألف واللام`, yields `الله`, and assigns the result specifically to `الباري تعالى`. This is asserted lineage, not mere letter resemblance.

### The `ص م د` chamber: directed reliance, material closure, wrapping, oversight, impact, endurance

**`SMD-B001` carrier:**

> الصمد القصد وصمدته صمدا (maqayis); وصمدت قصدت وصمدت صمد كذا أي قصدت قصده واعتمدته (ayn); صمده يصمده صمدا أي قصده والصمد السيد لأنه يصمد إليه في الحوائج وبيت مصمد أي مقصود (sihah); الصمد السيد الذي قد انتهى سؤدده والذي يصمد إليه الأمر وصمدت صمد هذا الأمر أي قصدت قصده واعتمدته (tahdhib); الصمد السيد الذي يصمد إليه في الأمر وصمده قصد معتمدا عليه قصده (mufradat)

`SMD-B001-T1` equates `الصمد` with directed intention and gives `صمدته` a controller, an affected/referential endpoint `ـه`, and the outgoing relation `قصد`. `T2` repeats first-person direction and adds reliance on that endpoint; `صمد كذا` retains a demonstrative/open target. `T3` gives an active controller repeatedly intending `ـه`, and separately names `الصمد` as a master because needs are directed toward him. `بيت مصمد أي مقصود` gives a local house the passive state of being aimed at. `T4` supplies a master whose sovereignty has reached its endpoint, and an `أمر` directed toward that master; it also maps intention toward `هذا الأمر` to reliance on it. `T5` keeps the master, the matter, the intentional agent, and the relied-on endpoint in distinct local positions. Surface `ٱلصَّمَدُ` opens all of these role schemas without selecting an occupant for their open agent, need, matter, or house ports.

**`SMD-B002` carrier:**

> الصلابة في الشيء والصمد كل مكان صلب (maqayis); المصمت الذي ليس بأجوف والصمدة صخرة راسية (ayn); الصمد المكان المرتفع الغليظ والمصمد لغة في المصمت وهو الذي لا جوف له (sihah); المصمت الذي لا جوف له والمكان المرتفع الغليظ والمصمد الصلب الذي ليس فيه خدد والشديد من الأرض (tahdhib); الصمد الذي ليس بأجوف (mufradat)

`SMD-B002-T1` predicates hardness of a thing and classifies every locally quantified hard place as `الصمد`. `T2` makes `المصمت` an object with no cavity and names `الصمدة` as a firmly anchored rock. `T3` predicates height and thickness of a place, supplies `المصمد` as a language variant of `المصمت`, and repeats the no-cavity vacancy. `T4` differentiates no cavity, no grooves, hard material, severe ground, and elevated thick place. `T5` again predicates absence of hollowness. These are material/state tuples, not agents who intend or masters to whom needs are directed.

**`SMD-B003` carrier:**

> الصماد عفاص القارورة وصمدتها صمدا (ayn); الصماد عفاص القارورة (sihah); الصماد سداد القارورة والصماد عفاص القارورة وقد صمدتها أصمدها (tahdhib)

`SMD-B003-T1` equates `الصماد` with the bottle's stopper/case and gives a controller the completed operation `صمدتها` on a feminine bottle endpoint. `T2` repeats the stopper equation. `T3` gives both `سداد القارورة` and `عفاص القارورة`, then active past/imperfect `صمدتها أصمدها`. Bottle, aperture, stopper material, controller, closed state, and any later contents remain separately typed; the contents are unspecified.

**`SMD-B004` carrier:**

> صمد رأسه تصميدا وذلك إذا لف رأسه بخرقة أو منديل أو ثوب ما خلا العمامة وهي الصماد (tahdhib)

`SMD-B004-T1` has a controller wrap a locally possessed head with one of three supplied media: cloth scrap, handkerchief, or garment. `العمامة` is explicitly excluded from the accepted media; `الصماد` names the resulting wrap/object. The head is affected, the material becomes surrounding medium, and the turban position is a typed vacancy produced by exclusion.

**`SMD-B005` carrier:**

> إني على صمادة من أمر إذا أشرف عليه وحفلت به (tahdhib)

`SMD-B005-T1` places a first-person controller `على صمادة من أمر`, then equates that condition with overlooking/supervising the matter and caring about it. The matter is the repeated endpoint of `عليه` and `به`; physical height, attention, and concern remain facets of this complete relation rather than imported locations.

**`SMD-B006` carrier:**

> صمده بالعصا صمدا إذا ضربه بها (tahdhib)

`SMD-B006-T1` has an unspecified controller act on local suffix-object `ـه` with instrument `العصا`; the assertion equates the operation with striking that same object by that same instrument. Incoming state and aftermath of the affected participant are open.

**`SMD-B007` carrier:**

> الصمد الدائم والدائم الباقي بعد فناء خلقه وناقة مصماد وهي الباقية على القر والجدب الدائمة الرسل (tahdhib)

`SMD-B007-T1` equates `الصمد` with `الدائم`; `T2` equates enduring with remaining after the annihilation of locally possessed creation, preserving the before/after boundary and absent created field. `T3` predicates `مصماد` of a she-camel that remains through cold and drought and whose milk-flow is continuous. The camel, environmental forces, milk, temporal endurance, and the possessor in `خلقه` stay local.

### The `ق و ل` chamber: utterance, instrument, speaker disposition, authority, attribution, circulation, negotiation, cognition, definition

**`QWL-B001` carrier:**

> القول من النطق (maqayis)؛ قال يقول قولا وقولة ومقالا ومقالة (sihah)؛ القول والقيل واحد (mufradat)؛ المركب من الحروف المبرز بالنطق (mufradat)؛ القيل من القول اسم (ayn)

`QWL-B001-T1` derives/defines `القول` from vocal articulation. `T2` preserves the inflectional and nominal series `قال -> يقول -> قولا/قولة/مقالا/مقالة`. `T3` asserts exact identity/equivalence between `القول` and `القيل`; this `واحد` is an equation predicate local to the two terms. `T4` makes a composition of letters incoming content and vocal articulation the operation that brings it into outward presence; the supplied scope allows a single expression, sentence, poem, or address as distinct content scales. `T5` names `القيل` as a noun from `القول`. Surface `قُلْ` re-instantiates an utterance operation whose accepted content is supplied by `SYN-1`; none of these lexical examples supplies its local speaker occupant.

**`QWL-B002` carrier:**

> المقول اللسان (maqayis;ayn;sihah)

`QWL-B002-T1` is an exact naming/equation tuple, `المقول = اللسان`. It exposes an instrument/body-part schema for speech. It remains separate from `المقول` as the title in the next chamber and from any surface speaker.

**`QWL-B003` carrier:**

> رجل قولة وقوال كثير القول (maqayis)؛ رجل تقوالة أي منطيق وقوال وقوالة أي كثير القول (ayn)؛ رجل مقول ومقوال وقولة وقوال وتقوالة أي لسن كثير القول (sihah)

`QWL-B003-T1` predicates `قولة` and `قوال` of a local man and equates that state with much speech. `T2` maps `تقوالة` to articulate/speaking and maps `قوال/قوالة` to much speech. `T3` gathers `مقول`, `مقوال`, `قولة`, `قوال`, and `تقوالة` as alternative person-descriptions and supplies both `لسن` and `كثير القول`. The man is a local bearer of a repeated-disposition state, not the controller of the surface command unless an absent identity edge is later supplied.

**`QWL-B004` carrier:**

> المقول بلغة أهل اليمن القيل وهم المقاولة والأقيال والأقوال والواحد القيل (ayn)؛ القيل ملك من ملوك حمير دون الملك الأعظم والمرأة قيلة (sihah)؛ كأنه الذي له قول أي ينفذ قوله (sihah)

`QWL-B004-T1` supplies a dialectal title equation, plural series `المقاولة/الأقيال/الأقوال`, and singular `القيل`; the local Yemenite title is not the tongue of B002 despite exact `المقول`. `T2` places the title-holder among kings of Himyar but below the greatest king and gives feminine `قيلة`. `T3` offers a role topology: the titled one possesses a `قول` whose outcome is that his word takes effect. Holder, utterance content, affected domain, rank boundary, and efficacy remain typed.

**`QWL-B005` carrier:**

> تقول باطلا أي قال ما لم يكن (ayn)؛ قولتني ما لم أقل وأقولتني ما لم أقل أي ادعيته علي (sihah)؛ تقول عليه أي كذب عليه (sihah)

`QWL-B005-T1` equates false saying with saying `ما لم يكن`: a speaker produces a content schema whose corresponding occurrence is negated. The exact subsequence `لم يكن` contacts line 4, but false-speech agency does not enter `O-S4-KWN`. `T2a/b` gives a second controller causative forms `قولتني/أقولتني`, first-person affected speaker `ـني`, content `ما لم أقل`, and the equation `ادعيته علي`: attribution to the first person of content that first person did not utter. `T3` makes `تقول عليه` an act of lying about/against a local endpoint. These tuples distinguish content production, claimed authorship, actual utterance occurrence, and truth-status.

**`QWL-B006` carrier:**

> اقتال قولا أي اجتر إلى نفسه قولا من خير أو شر (ayn)

`QWL-B006-T1` has a controller draw an utterance-content object toward the reflexive endpoint `نفسه`; the incoming content may be from good or evil under the supplied alternative. The route is toward self, and acquisition/appropriation is the outcome. Neither moral alternative is selected.

**`QWL-B007` carrier:**

> انتشرت له قالة حسنة أو قبيحة في الناس (ayn)؛ القالة القول الفاشي في الناس (ayn)؛ كثر فيه القيل والقال (ayn)؛ كثرت قالة الناس (sihah)؛ كثر القيل والقال (sihah)

`QWL-B007-T1` lets a saying/reputation spread among people with a local beneficiary/possessor `له` and an unselected favorable/unfavorable polarity. `T2` equates `القالة` with speech diffused among people. `T3` places abundant circulating `القيل والقال` in a local domain `فيه`. `T4` assigns abundant saying to people; `T5` repeats abundance of the paired terms. Utterance tokens, circulation medium, people, local possessor, evaluative polarity, and quantity remain separate facets.

**`QWL-B008` carrier:**

> القال الخشبة التي تضرب بها القلة (sihah)

`QWL-B008-T1` names `القال` as a wooden stick; an unspecified striker uses it as instrument to strike `القلة`. Detection exposes `قال` inside `القال` and surface `قل` inside `القلة`, but this is an instrument-impact tuple, not an utterance. The affected object and resulting motion/damage are open.

**`QWL-B009` carrier:**

> قاولته في أمره وتقاولنا أي تفاوضنا (sihah)

`QWL-B009-T1` has a first-person controller exchange speech with suffix-participant `ـه` concerning that participant's `أمر`; `T2` makes the controller plural/reciprocal and equates `تقاولنا` with negotiation. It exposes multiple alternating speakers, shared matter-content, and a negotiation outcome left unspecified.

**`QWL-B010` carrier:**

> اقتال عليه تحكم (sihah)

`QWL-B010-T1` equates action `اقتال عليه` with exercising control over a local endpoint. Controller, constrained participant, scope of rule, consent, and outcome are open; the direction `على` is explicit.

**`QWL-B011` carrier:**

> العرب تجري تقول وحدها في الاستفهام مجرى تظن في العمل (sihah)؛ بنو سليم يجرون متصرف قلت في غير الاستفهام أيضا مجرى الظن (sihah)

`QWL-B011-T1` gives `تقول` alone, under interrogation, the syntactic operation of `تظن`; the Arabs are the usage community, not an event controller inside the embedded syntax. `T2` gives Banu Sulaym a broader transformation: inflected `قلت` also follows the government/work of conjecture outside interrogation. Interrogative versus noninterrogative scope, speech form, conjecture schema, and governed arguments remain explicit. The exact embedded `قل` in `قلت` contacts the surface command without importing conjectural status.

**`QWL-B012` carrier:**

> المتصور في النفس قبل الإبراز باللفظ قول (mufradat)؛ في نفسي قول لم أظهره (mufradat)

`QWL-B012-T1` names content conceived in the self before outward verbalization as `قول`; incoming state is internal/conceived, the expression event is delayed. `T2` gives first-person possession/location `في نفسي`, a speech-content object, and explicitly negates the controller's bringing it outward. This vacancy comparison meets QWL-B001's articulated output and surface `قُلْ`, but no content identity is asserted.

**`QWL-B013` carrier:**

> للاعتقاد نحو فلان يقول بقول أبي حنيفة (mufradat)

`QWL-B013-T1` uses saying as belief/adherence: local `فلان` adopts/carries the content/position `قول أبي حنيفة`. The possessor of the doctrine, adopter, and doctrinal schema are distinct. This tuple explicitly accepts a repeatable content schema and therefore can receive content by re-instantiation when an exact content is supplied; none is identified with the surface quote here.

**`QWL-B014` carrier:**

> للدلالة على الشيء نحو قول الشاعر امتلأ الحوض وقال قطني (mufradat)

`QWL-B014-T1` lets a thing's state function as saying/indication. In the complete example, the pool undergoes filling, then the pool is grammatical controller of `قال`, with content `قطني`; the poet is carrier of the example but not controller of the pool's local indicative relation. Filling state -> nonhuman indication is the transformation.

**`QWL-B015` carrier:**

> للعناية الصادقة بالشيء كقولك فلان يقول بكذا (mufradat)

`QWL-B015-T1` maps `فلان يقول بكذا` to sincere concern for an unspecified thing. The demonstrative content/endpoint remains open, and the speech-form relation is a state of concern rather than necessarily an utterance event.

**`QWL-B016` carrier:**

> يستعمله المنطقيون في معنى الحد فيقولون قول الجوهر كذا وقول العرض كذا أي حدهما (mufradat)

`QWL-B016-T1` has logicians use `القول` as `الحد`. `T2a/b` gives the content forms `قول الجوهر كذا` and `قول العرض كذا` and equates each with the corresponding definition/boundary `حدهما`. Substance and accident remain two defined subject matters; `كذا` leaves each definition content open. This is a boundary/definition operation, not the numerical or divine `أحد` despite nearby consonantal contacts.

### The `ك ف ء` chamber: counterpart, inversion, formal mismatch, joined enclosure, annual yield

**`KFʾ-B001` carrier:**

> الكفء المثل (maqayis)؛ التكافؤ التساوي (maqayis)؛ هذا كفء له أي مثله في الحسب والمال والحرب (ayn)؛ المكافأة مجازاة النعم (ayn)؛ الكفئ النظير (sihah)؛ كل شيء ساوى شيئا حتى يكون مثله فهو مكافئ له (sihah;tahdhib)؛ كافأت الرجل أي فعلت به مثل ما فعل بي (tahdhib)؛ فلان كفء لفلان في المناكحة أو في المحاربة (mufradat)؛ نكافىء بهما عنا عين الشمس (tahdhib)؛ كافأ الرجل بين فارسين برمحه (tahdhib)

`KFʾ-B001-T1/T2` assert `الكفء = المثل` and `التكافؤ = التساوي`. `T3` places demonstrative `هذا` in counterpart relation to pronoun endpoint `له`, explicitly equates that relation with `مثله`, and opens three comparison measures: lineage/status, property, and war. `T4` makes `المكافأة` a return/recompense for benefits. `T5` equates `الكفئ` with a counterpart/peer.

`KFʾ-B001-T6` is kept whole: `كل شيء ساوى شيئا حتى يكون مثله فهو مكافئ له`. A first thing enters equality with a second thing, reaches a state of being like it, then bears the counterpart relation to it. Controller is not agentive; the two thing-positions remain distinct; `مثله`, `فهو`, and `له` retain their local pronouns. This topology maps directly onto the lexical predicate structure of line 4 while line 4 changes polarity to negated, mood to jussive, subject to delayed `أحد`, and predicate to accusative `كُفُوًا`.

`T7` has a first-person controller reciprocate toward a local man by doing to him the same as the man did to the controller; source act and returned act are distinct occurrences linked by content/role re-instantiation. `T8` gives two local persons counterpart status in marriage or war, preserving the unselected domain. `T9` uses dual `بهما` as a local medium/instrument to counter or ward `عين الشمس` away from first-person-plural `عنا`; the dual occupants are unspecified. `T10` has a man use his spear to align/counter between two horsemen. Agent, spear, horsemen, equality axis, and outcome remain local.

**`KFʾ-B002` carrier:**

> أكفأت الشيء إذا أملته (maqayis;tahdhib)؛ كفأت القصعة والإناء (ayn)؛ كفأت الإناء إذا كببته (sihah;tahdhib)؛ كفأت القوم إذا صرفتهم إلى غيره (sihah;tahdhib)؛ تكفأت المرأة في مشيتها (sihah)؛ تكفأ تكفؤا (tahdhib)؛ مكفأ الوجه كاسف اللون (ayn;tahdhib)؛ الإكفاء قلب الشيء كأنه إزالة المساواة (mufradat)

`KFʾ-B002-T1` maps action on a thing to tilting it. `T2/T3` apply the operation to a dish/vessel and make overturning its outgoing orientation. `T4` applies it to a group and diverts them from their route toward another, locally pronominal destination. `T5` gives a woman a swaying gait; `T6` retains the event noun. `T7` gives a face an inverted/changed appearance and darkened/faded color. `T8` equates `الإكفاء` with turning a thing over and explicitly frames that as removal of equality. This final relation provides a changed-outcome counterfield to B001: equality/counterpart state versus its removal by inversion. Surface `كُفُوًا` shares the root/form interface but not any vessel, people, woman, face, or act of overturning.

**`KFʾ-B003` carrier:**

> الإكفاء في الشعر (maqayis;ayn;sihah;tahdhib;mufradat)؛ أن ترفع قافية وتخفض أخرى (maqayis)؛ الاختلاط في القوافي (ayn)؛ يخالف بين قوافيه بعضها ميم وبعضها نون (sihah)؛ اختلاف إعراب القوافي (tahdhib)

`KFʾ-B003-T1` names a poetic formal relation. `T2` opposes raising one rhyme to lowering another; `T3` names mixture among rhymes; `T4` makes a poet/controller differ his rhymes by terminal consonant, some `ميم` and some `نون`; `T5` locates difference in grammatical inflection. The complete passage-ending sequence `[د, د, د, د]` changes case/mood realization `[NOM, NOM, JUS, NOM]`. This supplies an indexed formal comparison with the lexical rhyme tuple while neither source nor surface asserts that the passage is an instance of poetic fault.

**`KFʾ-B004` carrier:**

> الكفاء شقتان تنصح إحداهما بالأخرى (maqayis)؛ الكفاء شقة أو ثنتان ينصح إحداهما بالأخرى (ayn)؛ الكفاء بالكسر والمد شقة أو شقتان (sihah)؛ أكفأت البيت فهو مكفأ إذا عملت له كفاء (tahdhib)؛ الكفاء لشقة تنصح بالأخرى فيجلل بها مؤخر البيت (mufradat)

`KFʾ-B004-T1` defines `الكفاء` as two panels sewn one to the other: `إحداهما` selects one local panel, `الأخرى` the other, and sewing joins without merging them. `T2` leaves quantity at one or two while retaining the joining relation when two are present. `T3` preserves pronunciation `بالكسر والمد` and the number alternative. `T4` has a controller furnish a local house with a `كفاء`, producing state `مكفأ`; the beneficiary relation is `له`. `T5` uses one panel as medium to cover the rear boundary of the house. Panel, counterpart panel, seam, house, rear, controller, and covering result remain typed. The embedded `أحد` in `إحداهما` transports form only.

**`KFʾ-B005` carrier:**

> الكفأة وهي حمل النخلة سنتها (maqayis)؛ يقال ذلك في نتاج الإبل أيضا (maqayis)؛ سألته نتاج إبله سنة (maqayis;ayn;tahdhib)؛ الكفأة من الإبل نتاج سنة (ayn)؛ أكفأت إبلي كفأتين (sihah;tahdhib)؛ أعطاني لبنها ووبرها وأولادها سنة (sihah)؛ سألته ثمرها سنة (tahdhib)؛ يقال لنتاج الإبل ليست تامة كفأة (mufradat)

`KFʾ-B005-T1` names a date palm's annual crop as `الكفأة`, binding plant, yield, and year. `T2` re-instantiates the named yield schema for camels. `T3` has first person request from a local possessor the annual offspring/yield of his camels. `T4` equates camel `كفأة` with a year's yield. `T5` has a controller divide/arrange possessed camels into two `كفأتين`, exposing alternation of their production cycles. `T6` transfers milk, wool, and offspring from a local feminine herd/source to first person for one year. `T7` requests its fruit for a year. `T8` applies `كفأة` to camel yield even when it is not complete, preserving the deficient-result state. The recurring year is a boundary/measure; product classes do not merge with one another.

### The `ك و ن` chamber: occurrence, position, guarantee, submission, age-name, condition

**`KWN-B001` carrier:**

> الكون الحدث يكون بين الناس ومصدر من كان يكون؛ الكينونة في مصدر كان؛ الكائنة الأمر الحادث (ayn); كان عبارة عما مضى من الزمان؛ حدوث الشيء ووقوعه؛ كان الأمر أي مذ خلق؛ تقع زائدة للتوكيد؛ لا يكون زيدا تعني الاستثناء؛ كونه فتكون أحدثه فحدث (sihah); أصل يدل على الإخبار عن حدوث شيء إما في زمان ماض أو زمان راهن؛ كان الشيء يكون كونا إذا وقع وحضر (maqayis)

`KWN-B001-T1` equates `الكون` with an event occurring among people and derives it from `كان يكون`; `T2` places `الكينونة` in the same source family; `T3` names `الكائنة` as an occurring matter. `T4` lets `كان` report past time. `T5` separates a thing's coming-to-occur from its occurrence result. `T6` maps `كان الأمر` to a boundary extending from its creation. `T7` supplies a syntactically extra occurrence used for emphasis. `T8` gives negative `لا يكون زيدا` the operation of exception, retaining its local case/argument pattern. `T9` is a causative lineage: `كونه` addressed to a thing -> `فتكون`; `أحدثه` -> `فحدث`. The controller causes, the affected thing undergoes, and the event result occurs.

The final source assertions make the root report the occurrence of a thing in past or present time and equate `كان الشيء يكون كونا` with that thing's occurring and becoming present. Surface `يَكُن` instantiates a distinct jussive negated copular occurrence; none of the lexical things or people fills its subject.

**`KWN-B002` carrier:**

> المكان اشتقاقه من كان يكون؛ تمكن (ayn;maqayis); فلان مني مكان هذا؛ موضع العمامة (ayn); المكانة المنزلة؛ مكين عند فلان بين المكانة؛ المكان والمكانة الموضع؛ تمكن (sihah)

`KWN-B002-T1` asserts derivation of `المكان` from `كان يكون` and retains resultant capability/establishment `تمكن`. `T2` places a local `فلان` relative to first person in the position of demonstrative `هذا`; the displaced/replaced occupant of that position is open. `T3` names a position for `العمامة`. `T4` equates `المكانة` with rank/station; `T5` places a locally established person `عند فلان` and gives manifest rank; `T6` equates place and station with `الموضع`, again ending in `تمكن`. Physical position, social rank, replacement, and establishment are separate realizations.

**`KWN-B003` carrier:**

> الكيانة الكفالة؛ كنت على فلان أكون كونا أي تكفلت به؛ اكتنت به اكتيانا مثله (sihah); كنت على فلان أكون عليه إذا كفلت به؛ اكتنت أيضا اكتيانا (maqayis)

`KWN-B003-T1` equates `الكيانة` with guarantee/responsibility. `T2` gives first-person controller a relation `على فلان`, continued through `أكون كونا`, and equates it with undertaking responsibility for that same local person `به`. `T3` gives `اكتنت به` the same responsibility topology. The repeated source restates `كنت ... أكون عليه` under the condition `كفلت به`. Controller, charge/beneficiary, obligation, and duration stay local; `مثله` here repeats the manner/form, not a counterpart occupant.

**`KWN-B004` carrier:**

> الاستكانة الخضوع (sihah)

`KWN-B004-T1` is an exact state equation, `الاستكانة = الخضوع`. Bearer, controller to whom submission is directed, consent, force, and aftermath are open.

**`KWN-B005` carrier:**

> يقال للرجل إذا شاخ كُنْتِيّ؛ كأنه نسب إلى قوله كُنْتُ في شبابي كذا وكذا (sihah)

`KWN-B005-T1` names a local man `كُنْتِيّ` after he has aged. `T2` supplies the naming derivation from his recurrent/attributed utterance `كُنْتُ في شبابي كذا وكذا`: past self-state, youth interval, present aged state, and unspecified remembered acts/states are retained. The naming speaker and old man may coincide only where the attached `قوله` supplies possession of the utterance.

**`KWN-B006` carrier:**

> الكينة في قولهم بات فلان بكينة سوء أي بحال سوء فأصله الكون فعلة من الكون (maqayis)

`KWN-B006-T1` locates `كينة` in the complete saying `بات فلان بكينة سوء`, places a local person in a bad condition overnight, equates that with `بحال سوء`, and explicitly derives `الكينة` as a `فعلة` form from `الكون`. Person, night interval, condition, evaluation, and derivational source remain separate.

### The `و ل د` chamber: offspring, parental roles, birth, recent-born roles, causal generation, age-peer relation

**`WLD-B001` carrier:**

> أصل صحيح وهو دليل النجل والنسل؛ الولد وهو للواحد والجميع (maqayis)؛ الولد قد يكون واحدا وجمعا؛ الوليد الصبي (sihah)؛ الولد اسم يجمع الواحد والكثير والذكر والأنثى؛ الوليد الصبي حين يولد (tahdhib)؛ الولد المولود؛ الابن والابنة؛ جمع الولد أولاد (mufradat)

`WLD-B001-T1` makes the root an origin/sign for progeny and lineage. `T2` lets `الولد` carry singular and plural number; `T3` repeats the number alternative and equates `الوليد` with a boy. `T4` gives the name scope over one/many and male/female. `T5` predicates `الوليد` of a boy at the boundary `حين يولد`. `T6` equates `الولد` with the born one, differentiates son and daughter, and supplies plural transformation `الولد -> أولاد`. Number, gender, age, lineage, and birth-state remain parameters, not occupants supplied to the negated surface verbs.

**`WLD-B002` carrier:**

> الوالد الأب والوالدة الأم وهما الوالدان (sihah)؛ يقال لأم الرجل هذه والدة (tahdhib)؛ الأب يقال له والد والأم والدة ويقال لهما والدان (mufradat)

`WLD-B002-T1` equates `الوالد` with father and `الوالدة` with mother, then groups the two local roles under dual `الوالدان` without merging them. `T2` names a local man's mother `والدة`. `T3` repeats the father/mother naming and dual grouping. These are repeatable role schemas; no particular parent is supplied on the surface.

**`WLD-B003` carrier:**

> ولدت المرأة تلد ولادا وولادة؛ أولدت حان ولادها (sihah)؛ الولادة فهو وضع الوالدة ولدها؛ شاة والد وهي الحامل؛ ولدناها أي ولينا ولادتها (tahdhib)؛ يوم ولدت؛ يوم ولد (mufradat)

`WLD-B003-T1` gives a woman controller/undergoer of active birth through past, imperfect, and event-noun forms. `T2` makes `أولدت` a threshold at which her birth time has arrived. `T3` defines birth as a mother placing/delivering her locally possessed child: mother, child, pregnancy/source state, and delivered result remain distinct. `T4` predicates `والد` of a ewe and equates the state with pregnant. `T5` gives first-person plural attendants/controller role over a feminine animal's birth, not parenthood of its child. `T6/T7` place active and passive birth forms inside a day boundary. These positive/feminine or attendant tuples map by changed controller, voice, polarity, and result to the two negated 3MS surface occurrences.

**`WLD-B004` carrier:**

> الوليدة الأنثى والجمع ولائد (maqayis)؛ الوليد الصبي والعبد والجمع ولدان وولدة؛ الوليد الصبية والأمة والجمع الولائد (sihah)؛ الوليد الصبي حين يولد؛ يقال للأمة وليدة وإن كانت مسنة (tahdhib)؛ الوليد يقال لمن قرب عهده بالولادة؛ الوليدة مختصة بالإماء في عامة كلامهم (mufradat)

`WLD-B004-T1` equates `الوليدة` with a female and supplies plural `ولائد`. `T2` gives `الوليد` boy and male-servant roles with plural `ولدان/ولدة`, then gives the feminine form girl/female-servant roles and plural `الولائد`. `T3` binds boy-status to the time `حين يولد`. `T4` permits a female servant to retain `وليدة` even when aged, explicitly separating social role from recent-birth age. `T5` otherwise ties `الوليد` to nearness of birth; `T6` specializes `الوليدة` to female servants in general usage. Age, sex, servitude, number, and naming community remain distinct dimensions.

**`WLD-B005` carrier:**

> تولد الشيء عن الشيء حصل عنه (maqayis)؛ عربية مولدة ورجل مولد إذا كان عربيا غير محض (sihah)؛ المولد من الكلام مولدا إذا استحدثوه؛ كتاب مولد أي مفتعل؛ بينة مولدة وليست بمحققة (tahdhib)؛ تولد الشيء من الشيء حصوله عنه بسبب من الأسباب (mufradat)

`WLD-B005-T1` gives one local thing an origin in another and equates generation with obtaining/occurring from it. `T2` predicates generated/non-pure status of an Arabic variety and a man under a conditional ethnic/language classification. `T3` makes people innovate a generated item of speech; controller is encoded plural in `استحدثوه`, content/product is `المولد من الكلام`. `T4` equates a generated book with fabricated. `T5` gives generated evidence a state explicitly not verified. `T6` restates cause-mediated generation: source thing -> one cause among causes -> resulting thing. These tuples can transport a content-generation or causal lineage schema, but surface negation supplies neither positive source nor product.

**`WLD-B006` carrier:**

> اللدة نقصانه الواو لأن أصله ولدة (maqayis)؛ لدة الرجل تربه؛ وهما لدان والجمع لدات ولدون (sihah)؛ اللدة مختصة بالترب يقال فلان لدة فلان وتربه (mufradat)

`WLD-B006-T1` supplies exact transformation lineage `ولدة -> اللدة` by loss of waw. `T2` equates a local man's `لدة` with his same-age peer. `T3` groups two peers as dual `لدان` and supplies plural `لدات/ولدون`. `T4` restricts the term to age-peer relation and gives reciprocal local placeholders `فلان لدة فلان وتربه`. The peer schema interfaces with `مثل/نظير/كفء`, while no source person fills line 4.

## Typed occupancy graph

### Admitted local continuations

These mappings carry an occupant, state, or content only where the supplied relation binds that same local node. The arrow label states the entire transported payload.

```text
O-S1-SAY.command occurrence
-> quoted_complement {exact content schema: هُوَ ٱللَّهُ أَحَدٌ}
-> O-S1-PRED.quoted occurrence

O-S1-PRED.هُوَ
-> apposition {same local referential position under SYN-3}
-> O-S1-PRED.ٱللَّهُ

O-S1-PRED.ٱللَّهُ
-> predication {local nominative property أَحَدٌ}
-> O-S1-PRED.property port

O-S2-PRED.ٱللَّهُ
-> predication {local nominative property ٱلصَّمَدُ}
-> O-S2-PRED.property port

O-S3-ACT.لَمْ
-> government/scope {NEG + IMPF + JUS}
-> O-S3-ACT.يَلِدْ occurrence denied

O-S3-ACT.complete relation
-> coordination {relation alignment only; no occupant}
-> O-S3-PASS.complete relation

O-S3-PASS.وَلَمْ
-> government/scope {CONJ + NEG + IMPF + PASS + JUS}
-> O-S3-PASS.يُولَدْ occurrence denied

O-S4-KWN.وَلَمْ
-> government/scope {CONJ + NEG + IMPF + JUS}
-> O-S4-KWN.يَكُن occurrence denied

O-S4-KWN.يَكُن
-> kana_predicate {كُفُوًا, M.INDEF.ACC}
-> O-S4-KWN.counterpart-state port denied

O-S4-KWN.يَكُن
-> delayed_subject {أَحَدٌۢ, M.INDEF.NOM}
-> O-S4-KWN.subject class vacant under negation

O-S4-KWN.كُفُوًا
-> prep_complement {لَـ government}
-> O-S4-KWN.هُۥ local 3MS referential endpoint
```

Source-local lineages continue only their declared nodes:

```text
ALH-B002.إله
-> asserted form lineage {delete همزة; add الألف واللام}
-> ALH-B002.الله

WLD-B006.ولدة
-> asserted form lineage {loss of واو}
-> WLD-B006.اللدة

AHD-B001.وحد
-> asserted origin/branch relation {original واو; branch form}
-> AHD-B001.أحد

KWN-B001.causative controller + local thing
-> causation {كونه/أحدثه}
-> same local thing in occurrence state {فتكون/فحدث}

WLD-B005.source thing
-> asserted causal lineage {one supplied cause}
-> WLD-B005.distinct generated thing

WLD-B003.local mother + possessed fetus/child
-> birth {وضع الوالدة ولدها}
-> same local child in delivered/born state

KFʾ-B001.prior act by local man
-> content/role re-instantiation {same act schema, roles reversed}
-> KFʾ-B001.return act by first-person controller

QWL-B005.local attributed content
-> claimed-authorship relation {ادعيته علي}
-> first-person target, while actual first-person utterance remains negated
```

There is no admitted cross-record occupant handoff. In particular:

- the two surface occurrences of `ٱللَّهُ` have an exact-name/form link and parallel syntax, but recurrence alone does not transport the line-1 occupant to line 2;
- the five 3MS carriers do not corefer merely through person/gender;
- active `يَلِدْ` controller, passive `يُولَدْ` affected subject, `يَكُن` subject, and `هُۥ` endpoint remain distinct;
- source-example `فلان`, `الرجل`, `المرأة`, `القوم`, `الناس`, parents, children, masters, kings, worshippers, and things never enter a surface port without a supplied identity edge;
- negated offspring, birth, occurrence, or counterpart results are vacancies, not occupants available for later transport.

## Coalition field

Each node is canonicalized by member tuple identities plus the exact mapped payload. A node's membership exposes only the mapped interface stated here.

### Surface-indexed constellations

**`C-PRED-12 = {O-S1-PRED, O-S2-PRED}`**

```text
O-S1-PRED [local هُوَ/ٱللَّهُ -> NOM predication -> أَحَدٌ]
-> payload {exact subject form ٱللَّهُ; nominal predication; adjacent line ordinal 1->2}
-> O-S2-PRED [local ٱللَّهُ -> NOM predication -> ٱلصَّمَدُ]
```

Invariant: a locally named nominative carrier precedes a nominative predicate. Deltas: line 1 has an appositional pronoun and indefinite `أحد`; line 2 has no supplied pronoun and a definite article on `الصمد`; line 1 is quoted content after an imperative; line 2 has no supplied quote-attachment edge. The local named occupants and predicate states do not cross.

**`C-AHAD-OUTER = {O-S1-PRED, O-S4-KWN, AHD-B001, AHD-B002}`**

```text
112:1:4 أَحَدٌ, affirmative NOM predicate
-> payload {exact lemma/form; outer position 1; line-final د}
-> 112:4:5 أَحَدٌۢ, negated delayed NOM subject, outer position 4

AHD-B001.absolute/predicate and repeated-form tuples
-> payload {complete form أحد; predicative role schema}
-> O-S1-PRED

AHD-B002.negated exhaustive-class + delayed-order tuples
-> payload {أحد under negation; exhaustive class; delayed indefinite position}
-> O-S4-KWN
```

The complete outer mapping carries exact form, positional enclosure, grammatical-role change, and polarity change. It does not make the two `أحد` tokens one entity. `AHD-B002` supplies the vacancy consequence for the last occurrence; `AHD-B001` supplies lexical predication and the exact full quote for the first.

**`C-NEGATIVE-SEQUENCE = {O-S3-ACT, O-S3-PASS, O-S4-KWN}`**

```text
NEG + active IMPF.3MS.JUS + denied production
-> payload {لَم government; jussive; 3MS; negated occurrence; voice delta}
-> CONJ + NEG + passive IMPF.3MS.JUS + denied undergoing-birth
-> payload {CONJ return; لَم government; jussive; 3MS; operation-class delta}
-> CONJ + NEG + copular IMPF.3MS.JUS + denied counterpart predication
```

The line-3 active/passive rotation and line-4 copular vacancy are a distributed architecture of three denied occurrences. The architecture carries polarity, mood, ordering, conjunction, and parameter changes only. It neither joins the three 3MS positions nor turns offspring into a counterpart.

**`C-ENDINGS = {112:1.end, 112:2.end, 112:3.end, 112:4.end, KFʾ-B003}`**

```text
[أَحَدٌ, ٱلصَّمَدُ, يُولَدْ, أَحَدٌۢ]
-> payload {four indexed line ends; terminal د recurrence; full case/mood vector}
-> [N.INDEF.NOM, N.DEF.NOM, V.PASS.JUS, N.INDEF.NOM]
-> comparison interface {raise/lower, letter difference, movement/i'rab difference}
-> KFʾ-B003 rhyme-form tuples
```

Here the lexical comparison mechanism is enacted against the complete four-member boundary sequence. The surface has consonant recurrence rather than the source example's `ميم/نون` alternation, while it does have grammatical ending changes. No unseen rhyme realization is manufactured.

**`C-COUNT-POSITION = {surface complete vectors, AHD-B001, AHD-B003, AHD-B004, KFʾ-B004}`**

The surface vectors stay whole: `[4,2,4,5]`, `[4,3,5,7]`, `[3,1,3,4]`, `[2,1,2,1]`. They expose actual first, second, third, and fourth line positions and every carrier ordinal. `AHD-B001` supplies first-of-number; `AHD-B003` supplies one/two and compound-number operations; `AHD-B004` supplies first/addition and one-of-two; `KFʾ-B004` supplies one-or-two panels and `إحداهما/الأخرى`. Coalition links carry ordinal, pair selection, composition, and count-alternative relations onto the complete indexed vectors. They do not select arbitrary subsets of the passage or assert that a line is a panel, a day, or the number eleven.

### Exact source/surface enactments

**`C-Q4-COUNTERPART = {O-S4-KWN, KFʾ-B001-T3, KFʾ-B001-T6, KWN-B001}`**

```text
KFʾ-B001-T3  هذا -> كفء/مثل -> له
-> payload {counterpart topology; endpoint introduced by ل; comparison domains remain local}
-> O-S4-KWN  أحدٌ -> [NEG يكن] -> كفوا -> له

KFʾ-B001-T6  شيء₁ -> ساوى -> شيء₂ -> يكون مثله -> فهو مكافئ له
-> payload {two-place equality-to-counterpart spine; KWN occurrence; local له endpoint}
-> O-S4-KWN  delayed subject -> denied copular counterpart -> 3MS endpoint
```

Invariant: subject-like position, counterpart/equality predicate, and `لـ + pronoun` endpoint. Deltas: positive versus negated; generic thing/demonstrative versus exhaustive delayed `أحد`; indicative/source `يكون` versus surface jussive `يكن`; nominative/root-family forms versus accusative `كُفُوًا`; source order places subject first while surface delays it; comparison measures in `T3` are absent from the surface and therefore stay unspecified.

**`C-Q4-EXHAUSTIVE-VACANCY = {O-S4-KWN, AHD-B002-T1a, AHD-B002-T1b, AHD-B002-T2, AHD-B002-T3}`**

```text
لا أحد + في الدار
ما + في الدار + أحد
أحد في النفي -> استغراق جنس الناطقين -> لا واحد ولا اثنان فصاعدا
فما + منكم + من أحد + عنه + حاجزين
-> payload {negation scope; indefinite أحد; delayed-position alternative; exhaustive vacancy consequence}
-> وَلَمْ + يَكُن + لَهُ + كُفُوًا + أَحَدٌ
```

The topology maps negator, relational/predicative material, and indefinite `أحد`, including the delayed realization. House, speaking class, addressees, and blockers remain source-local. The surface supplies its own endpoint `هُۥ`, counterpart predicate, copula, case, and order.

**`C-LAM-YAKUN = {O-S4-KWN, QWL-B005-T1, KWN-B001}`**

```text
QWL-B005  قال ما لم يكن
-> payload {exact clause form لم يكن; negated occurrence content}
-> surface 112:4  وَلَمْ يَكُن ...
```

The full source assertion is enacted: in QWL-B005 a speaker says a content whose occurrence is denied, yielding the local false-speech relation. On the surface, `لم يكن` is itself the clause relation, not content asserted by that lexical speaker. The coalition carries the exact negative-occurrence schema; it does not carry falsehood, speaker, attributed content, or evaluative result into the surface command.

**`C-WLD-VOICE = {O-S3-ACT, O-S3-PASS, WLD-B001, WLD-B003, WLD-B004, WLD-B005}`**

```text
WLD-B003 woman -> active تلد/ولدت -> child delivered
-> payload {birth operation; controller/affected/result schema; parameter deltas}
-> O-S3-ACT implicit 3MS -> NEG active يلد -> no result

WLD-B003/WLD-B004 born participant -> passive/threshold ولد/يولد -> recent-born state
-> payload {passive affected-role schema; birth boundary; parameter deltas}
-> O-S3-PASS implicit 3MS affected -> NEG PASS يولد -> no occurrence/result

WLD-B005 source thing -> cause -> generated thing
-> payload {causal generation spine only}
-> coordinated O-S3-ACT/O-S3-PASS source/result role rotation
```

The lexical positive events make controller, mother, child, source thing, cause, and result available only inside their own tuples. The surface accepts the operation/role schema but supplies 3MS, negative polarity, jussive mood, active/passive voice, and no positive occupant or outcome.

**`C-FULL-QUOTE = {O-S1-SAY, O-S1-PRED, AHD-B001-T3, QWL-B001}`**

The exact content `قل هو الله أحد` in AHD-B001 collides with all four line-1 positions. QWL-B001 supplies articulated composed-letter speech; surface `قُلْ` supplies imperative controller morphology and `SYN-1` supplies the quote-accepting port. The lexical quote and surface quote are distinct occurrences of identical content. The transported payload is the exact content schema and term order, not a shared speaker or addressee.

### Microcontact coalitions carried through their complete relations

**`C-QUL-EMBED = {surface قُلْ, QWL-B005, QWL-B008, QWL-B011, KFʾ-B002}`**

```text
قُلْ -> normalized complete form قل
-> أقل/قلت {added همزة or ت; speech/attribution/conjecture tuples}
-> القلة {article + containing noun; stick-strike tuple}
-> قلب/وقلبه {added ب and attachments; inversion/removal-of-equality tuple}
```

The source relations now surround the initial command without replacing it. `أقل`/`قلت` expose person, negated authorship, and syntactic-conjecture changes; `القلة` exposes an affected object struck by `القال`; `قلب` exposes overturning and removal of equality. The initial command remains a 2MS speech act with quoted content. Addition of a letter or affix creates a formal trajectory, not an assertion that the command underwent the containing event.

**`C-AHAD-EMBED = {surface أَحَد x2, AHD chambers, KFʾ-B004, KWN-B001, QWL-B001, WLD-B001}`**

```text
أحد -> واحد/الواحد {initial و; equivalence/count tuples}
أحد -> استأحد/استأحدت {استـ, ـت; separation tuples}
أحد -> أحدكما/فأحدهن {dual or feminine-plural suffix; selection/causation tuples}
أحد -> الأحد/الأحدية {article, ـية; day/state tuples}
أحد -> أُحُد {vocalic delta; named mountain tuple}
أحد -> إحداهما {hamza-seat + feminine/dual material; two-panel tuple}
أحد -> أحدثه {ثه extension; causation-of-occurrence tuple}
```

Each containing form's complete tuple is active around both surface endpoints. The two surface roles remain predicate and delayed subject; no mountain, panel, event, pair member, or generated thing becomes either occupant.

**`C-LAHU-NAME = {surface لَّهُۥ, surface ٱللَّهُ x2, ALH-B001/B002, KFʾ-B001}`**

The exact `له` sequence occurs independently as preposition-plus-pronoun, within the written name `الله`, and inside local forms such as `إله`, `فالإله`, `مثله`, and `مكافئ له`. Its complete enactment juxtaposes a governed counterpart endpoint, proper-name derivation, deity/worshipped equations, and similarity/counterpart pronouns. Edge payload is the exact sequence plus its position/containment delta. Government from surface `لَـ` does not enter the name; namehood and worship relations do not enter the surface suffix.

**`C-LAM-FAN`** retains every complete noun in which particle-form `لم` appears across an `الـ + م...` boundary. Each such contact re-enters the already enacted tuple for its containing noun: counterpart (`المثل`), ruler (`الملك`), outward speech (`المبرز`, `المركب`, `المقول`), solidity (`المصمت`), absolute description (`المطلق`), place/status (`المكان`, `المكانة`, `الموضع`, `المنزلة`), generated product (`المولد`, `المولود`), worship (`المعبود`), reliance (`المعتمد`, `المقصود`), number (`المعدود`, `المضموم`), equality/counteraction (`المساواة`, `المقابلة`, `المقاولة`, `المكافأة`, `المماثلة`, `المناكحة`), and logic users (`المنطقيون/المنطقيين`). The local negative particle never expands its scope into a containing noun merely because the two-letter sequence crosses its article boundary.

### Cross-record relational coalitions

**`C-ORIGIN-FORMS = {AHD-B001, ALH-B002, WLD-B006, KWN-B006}`**

```text
وحد -> branch/origin with named واو -> أحد
إله -> delete همزة + add الألف واللام -> الله
ولدة -> lose واو -> اللدة
الكون -> فعلة derivation -> الكينة
```

Invariant: an explicitly named source term and a derived/result term. Deltas: consonant replacement/branching, deletion plus article addition, initial weak-letter loss, and morphological-pattern derivation. The node carries transformation topology and actual deltas; it never composes an unseen form from one tuple's deletion and another's article.

**`C-EQUATION-COUNTFIELD = {AHD-B001/B002/B003, QWL-B001, KFʾ-B001, WLD-B001, WLD-B006}`**

The exact `واحد/الواحد` circuit carries four different local operations: `أحد = الواحد` and first-of-number; `القول والقيل واحد` as identity/equation; `الولد` usable for one and many; and negative exclusion of one, two, and upward. `الكفء = المثل`, `التكافؤ = التساوي`, and `اللدة = الترب/مثيل السن` add explicit peer/equality relations. The coalition spine is term A -> supplied equivalence/count relation -> term B, with number, domain, polarity, and participant type deltas. It does not make utterance, child, counterpart, and `أحد` one occupant.

**`C-AMR-DIRECTIONS = {SMD-B001, SMD-B005, QWL-B009, KWN-B001}`**

```text
local أمر -> intended/reliance endpoint
local أمر -> object of overlooking/care
local أمره -> negotiated content
local الأمر -> occurring/created temporal event
```

The exact base `أمر` plus attachments supplies the interface. Controllers change from intending/relying agent, to supervising first person, to reciprocal speakers, to temporal occurrence. Direction changes toward, above/about, reciprocal exchange concerning, and presence from creation. No matter occupant crosses these tuples.

**`C-IMPACT = {SMD-B006, QWL-B008}`**

```text
agent -> ضرب via العصا -> local suffix-object
agent -> ضرب via الخشبة/القال -> القلة
```

Invariant: active strike, handheld specified instrument, affected endpoint. Deltas: instrument name, affected form, naming of the operation, and unspecified aftermath. The exact `ضرب` relation emits the link; local sticks and objects remain local.

**`C-HOUSE-BOUNDARY = {SMD-B001, SMD-B002, SMD-B003, SMD-B004, KFʾ-B004}`**

`بيت مصمد` and `البيت` supply an exact house-form interface. Around it remain distinct topologies: a house aimed at; a hard/no-cavity place; a bottle receiving a stopper; a head receiving a wrap with turban excluded; and a house rear receiving sewn covering panels. Same-root `ص م د`, exact `بيت`, and explicit closure/vacancy consequences license a distributed boundary comparison. No bottle becomes a house, no head becomes a vessel, and no no-cavity state is transferred to the covered house. The coalition carries target/boundary/covering/opening relations and their deltas only.

**`C-TURBAN-VACANCY = {SMD-B004, KWN-B002}`**

```text
SMD-B004 accepted wrapping media -> explicit exclusion {العمامة} -> turban slot vacant
KWN-B002 موضع -> exact object {العمامة} -> position named
```

The exact object term aligns exclusion with position. It does not assert that the excluded turban occupies the named position in either local event.

**`C-SUN = {ALH-B001, KFʾ-B001-T9}`**

```text
local الشمس -> named الإلاهة because local people worship it
local عين الشمس -> endpoint countered/warded by dual medium away from عنا
```

Exact `الشمس` carries named-entity class and local role correspondence. Worshippers, dual medium, first-person group, naming event, and countering event remain distinct.

**`C-PRODUCT-CYCLES = {KFʾ-B005, WLD-B001/B003/B005, QWL-B001/B005}`**

`نتاج`, `أولاد`, and `المولد من الكلام` expose produced-result schemas. KFʾ-B005 supplies annual measure, alternating herds, and milk/wool/offspring outputs. WLD supplies birth, child, plural offspring, and cause-mediated generation. QWL supplies composed speech brought outward and content said despite nonoccurrence. Mappings transport product role, source-to-result direction, time/cause boundary, and evidentiary-status changes. They do not turn speech into an animal child, assign parents to a book, or import a positive product into surface `لَمْ يَلِدْ وَلَمْ يُولَدْ`.

**`C-SPEECH-MODES = {O-S1-SAY, QWL-B001, B004, B005, B006, B007, B009, B010, B011, B012, B013, B014, B015, B016}`**

All members share the exact `ق و ل` record interface, but each actual vector remains whole:

- outward articulated letters/content (`B001`);
- efficacious word of a titled ruler (`B004`);
- false content, denied occurrence, or imposed authorship (`B005`);
- content pulled toward self (`B006`);
- favorable/unfavorable saying circulating among people (`B007`);
- reciprocal negotiation about a matter (`B009`);
- control directed over another (`B010`);
- speech-form functioning syntactically as conjecture (`B011`);
- internal content not expressed (`B012`);
- adopted belief/content (`B013`);
- a filled thing indicating its state (`B014`);
- sincere concern represented by `يقول بكذا` (`B015`);
- logical definition/boundary (`B016`);
- surface imperative production of the exact quoted content (`O-S1-SAY`).

The coalition maps controller changes (2MS command controller, speaker, king, attributor, self-directed agent, people, negotiating group, nonhuman pool, logicians), expression status, content status, direction, scale, and outcome. It does not manufacture one speech occurrence having all modes at once.

**`C-MASTER-TITLE-RESPONSIBILITY` remains an open attraction rather than a fused node.** `SMD-B001` has a master toward whom needs/matters are directed; `QWL-B004` has a titled king whose word takes effect; `KWN-B003` has a guarantor responsible for another; `QWL-B010` has control over another. Exact local terms such as `أمر`, `قول`, or directional pronouns can support narrower links already recorded, but broad authority or dependency alone does not emit a coalition or transport a controller.

**`C-ENDURANCE-OCCURRENCE` remains locally articulated.** `SMD-B007` supplies remaining after annihilation and endurance through cold/drought; `KWN-B001` supplies occurrence/presence in past or present and creation boundary. The exact `خلق` contact in `فناء خلقه` and `مذ خلق` opens a temporal boundary comparison. No enduring occupant is identified with any occurring thing, and no camel is installed in an occurrence port.

## Changed-controller and vacancy counterfields

The following actual parameter vectors remain side by side; none is synthesized into an unattested realization.

| local tuple | controller / grammatical subject | operation | polarity / voice | result or vacancy |
|---|---|---|---|---|
| `O-S1-SAY` | encoded 2MS command controller; utterance initiator unspecified | say exact quote | imperative, active | quote content present |
| `QWL-B001` | generic articulator | bring composed letters outward | positive active | articulated speech |
| `QWL-B012` | first person | retain speech in self | expression negated | outward-expression port vacant |
| `QWL-B005-T1` | local speaker | say content whose event did not occur | positive saying + embedded negative occurrence | false-speech status local |
| `O-S3-ACT` | implicit 3MS | beget/generate | negative active jussive | child/product port vacant |
| `WLD-B003` | woman/mother | give birth/place child | positive active | child delivered |
| `O-S3-PASS` | implicit affected 3MS; external agent suppressed | be born | negative passive jussive | birth occurrence/result vacant |
| `WLD-B003/4` | child/born participant or locally encoded passive form | undergo birth / be recently born | positive/passive or state | recent-born state present |
| `O-S4-KWN` | delayed `أحد`; nonagentive copula | be counterpart for `هُۥ` | negative jussive | counterpart subject and state absent |
| `KFʾ-B001-T6` | first thing, nonagentive equality subject | equal/be like/be counterpart to second | positive | counterpart state present |
| `KFʾ-B002-T8` | unspecified agent | overturn thing | positive active | equality explicitly removed |
| `SMD-B004` | wrapping agent | wrap head | positive active | wrap present; turban medium absent |
| `KWN-B002` | naming/location relation | give position for turban | positive stative | occupant of position unspecified |
| `SMD-B002` | nonagentive material bearer | lack cavity/grooves | negative property | internal cavity position absent |
| `SMD-B003` | stopper-applying agent | stop/close bottle | positive active | stopper present; contents open |

Vacancies do not globalize. The no-cavity vacancy cannot receive a child, a quote, or a counterpart. The absent turban is not the absent delayed `أحد`. Suppressed passive agent is not the unspecified imperative speaker. The unexpressed internal saying is a content-expression vacancy, not a denied event result. The incomplete annual yield is a deficient product, not a negated birth.

## Forward formations left open

Moving from line 1 to line 4 leaves these concrete attractions active without assigning them a governing interpretation:

1. `قُلْ` opens an utterance occurrence and binds only the immediately supplied quote `هُوَ ٱللَّهُ أَحَدٌ`. Its exact smaller form continues into `قلت`, `أقل`, `القلة`, and `قلب`; each containing source relation remains available around the initial carrier.
2. `هُوَ -> ٱللَّهُ -> أَحَدٌ` supplies a local apposition/predication spine. `هو` later reappears inside source equations for deity/worshipped status, equality/counterpart status, and singular/plural child status, without a shared antecedent.
3. The exact name begins line 2 after occurring third in line 1. Parallel named-subject predication aligns `أحد` with `الصمد` only as local predicate positions; lexical unity, aim/reliance, material hardness, closure, impact, and endurance all remain available around their separate tuple nodes.
4. The complete line-2 contraction from four surface words to two, while morphology splits its final word, precedes the return to four surface words and active/passive coordination in line 3. The full `[4,2,4,5]` vector remains a structural carrier.
5. Three successive `لَمْ` scopes form bare, conjoined, conjoined positions. Their complete negative relations move from active production, through passive undergoing, to copular counterpart vacancy; their local subjects remain unbound to one another.
6. Active `يَلِدْ` and passive `يُولَدْ` expose opposite grammatical orientations around the same supplied lemma. Lexical birth, offspring, parent, causal generation, and product tuples remain possible coalition interfaces but contribute no positive occupant to either denied event.
7. `لَّهُۥ كُفُوًا أَحَدٌۢ` delays the indefinite subject beyond its predicate and pronoun endpoint. The complete source assertions `هذا كفء له أي مثله` and `كل شيء ساوى شيئا حتى يكون مثله فهو مكافئ له` surround that order with a positive counterfield, while AHD-B002 supplies the exhaustive consequence of `أحد` under negation.
8. Final `أَحَدٌۢ` returns to the first line's lexical form and final consonant but changes syntactic role and polarity. It also reopens all contained-form circuits (`إحداهما`, `أحدثه`, `أُحُد`, `استأحد`, `الواحد`) without choosing among their local event types.

## Backward reopening

Backward movement begins with the last positioned carrier, not with a summary.

**From `112:4:5 أَحَدٌۢ` backward:** its delayed subject role reopens `AHD-B002` rather than copying the line-1 predicate role. Exhaustive negation returns through `ما في الدار أحد` and `فما منكم من أحد عنه حاجزين`; their locatives, speaking class, and blockers stay local. The exact form then reaches line 1 and exposes the outer role reversal: delayed negated subject -> affirmative quoted predicate.

**From `كُفُوًا` and `لَّهُۥ` backward:** the positive source spines `كفء له -> مثله` and `ساوى -> يكون مثله -> مكافئ له` re-enter. Their positive results make the surface absence type precise without filling it. The `له` contact then reaches the final letters of `الله`, ء ل ه worship/name equations, and attached pronoun forms; this return sharpens the separation between a proper-name form and a governed pronoun endpoint.

**From `يَكُن` backward:** exact `لم يكن` reaches QWL-B005's false-content assertion, while root/lemma reaches KWN occurrence, exception, emphasis, location, guarantee, submission, age-memory, and condition tuples. Because the surface occurrence is copular, negated, and jussive, none of those lexical controllers or outcomes can be imported. The `أحدثه` form sends a formal `أحد` contact farther back to both outer endpoints.

**From `يُولَدْ` backward:** passive voice first opens the affected-participant vacancy and the suppressed initiator. It then reaches lexical `حين يولد`, `يوم ولد`, recent-born role, child/male-servant/female-servant alternatives, and cause-mediated generated products. Moving one clause farther back reaches active `يَلِدْ`, but coordination does not identify passive affected participant with active controller.

**From the repeated `لَمْ` backward:** exact source `قول لم أظهره` exposes expression vacancy, and `ما لم أقل` exposes denied authorship. The article-boundary `لم` fan returns to all containing nouns while remaining form-only. The first bare negator and two conjoined negators preserve the ordered sequence `[bare, وَ+NEG, وَ+NEG]`.

**From `ٱلصَّمَدُ` backward:** the final `د` aligns with all passage endings. Its article and stem separate, then the stem reaches every `صمد` operation: intention/reliance, master aimed at in needs, hard/no-cavity state, stopper application, head wrapping excluding turban, oversight/care, stick impact, and endurance. These do not collapse into one event. Exact `بيت` and `العمامة` send narrower links to the panel-house and position chambers.

**From line-2 `ٱللَّهُ` backward:** exact form returns to the line-1 name, then to the full quoted source assertion and the asserted `إله -> الله` transformation. The return carries spelling, proper-name derivation, and parallel predication interface. It does not retroactively identify all local deity, sun, idol, oath, or invocation participants with a surface occupant.

**At `قُلْ` again:** later negation does not negate the command, later passive voice does not change its active imperative morphology, and later counterpart vacancy does not alter its exact quoted content. What has changed is the surrounding contact field: `قل` is now simultaneously positioned at passage opening and embedded, with preserved deltas, in attribution, conjectural syntax, a struck-object name, and an inversion term. The command remains available for the next turn as its own local occurrence.

## Unfilled ports and unresolved attractions

These openings remain concretely typed:

- `O-S1-SAY`: utterance initiator is unspecified; 2MS command controller/addressee is grammatically present; no identity between them is supplied.
- `O-S3-ACT`: implicit 3MS controller has no explicit binder; generated-child/product port and aftermath are denied.
- `O-S3-PASS`: implicit 3MS affected subject has no explicit binder; external begetter/agent is suppressed; birth result is denied.
- `O-S4-KWN`: pronoun endpoint is 3MS but antecedent is not bound by the supplied local syntax; delayed subject class and counterpart state are absent under negation.
- `AHD-B004`: one-of-two selector is open in `أحدكما`; possessor direction in additive use remains local; the named day has no supplied event occupant.
- `AHD-B005`: `هذا الأمر` is locally present but its content is unspecified; the arriving individuals in `آحاد أحاد` have no identities.
- `SMD-B001`: intending agent, needs, matter, and relied-on endpoint differ by tuple and remain open where not lexically filled.
- `SMD-B002/B003/B004`: bearer of hardness, bottle contents, wrapping controller, and head possessor remain local/open; cavity, groove, and turban vacancies keep distinct consequences.
- `QWL` field: surface quote has exact content; lexical belief, definition, negotiation, circulation, false attribution, internal content, and concern ports have no license to accept that content merely from shared root.
- `KFʾ-B001`: source comparison measures `الحسب والمال والحرب`, marriage/war alternatives, dual solar medium, and two horsemen are all local; none appears on the surface.
- `KFʾ-B005`: annual source, herd ownership, alternation phase, and incomplete yield remain source-local; no annual measure is supplied for the passage events.
- `KWN` field: occurrence thing, time, place occupant, guaranteed person, submission endpoint, remembered youth content, and bad-state bearer remain distinct.
- `WLD` field: parent, mother, child, animal, attendant, generated source/product, cause, language/book/evidence product, servant, and age-peer remain separate occupants and role schemas.

Broad resemblances remain attractions without emitted links: deity, master, king, guarantor, and controller are not one role; mountain, hard place, house, bottle, head, and positional `مكان` are not one location; solidity, uniqueness, and absence of a counterpart are not one state; endurance after annihilation and negated occurrence are not one temporal event; stopper, wrap, and sewn panels are not one material; offspring, annual yield, generated speech, book, and evidence are not one product. Their exact narrower contacts and complete local tuples remain active for later maturation.

No local tuple is consumed by these formations. Every tuple, exact form, boundary position, occupancy vacancy, and coalition interface above remains available in parallel.
