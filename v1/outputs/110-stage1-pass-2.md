# S110 Stage 1 Pass 2 — temporally conditioned reactivation

## Root cause of Pass 1 limitation

Pass 1 over-selected for coherent passage-scale images and compressed weak or dead seeds into memory instead of preserving each seed as an auditable record. The local `resources/qac.sqlite` and `resources/furuq_v4.sqlite` files are empty in this checkout, so I used the TSV copies (`qac_root_ayah.tsv`, `attachments.tsv`, `v4_branches.tsv`) as the available local resource layer. That resource substitution was not the cause of the limitation; the cause was pruning during reporting. This Pass 2 restarts at the first rooted word and records every eligible rooted occurrence × accepted branch, including weak, local, rival, and terminated seeds.

## Scope

Assigned passage: S110, ayat 1-3. Sacred Arabic:

```text
110:0 بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
110:1 إِذَا جَآءَ نَصْرُ ٱللَّهِ وَٱلْفَتْحُ
110:2 وَرَأَيْتَ ٱلنَّاسَ يَدْخُلُونَ فِى دِينِ ٱللَّهِ أَفْوَاجًۭا
110:3 فَسَبِّحْ بِحَمْدِ رَبِّكَ وَٱسْتَغْفِرْهُ ۚ إِنَّهُۥ كَانَ تَوَّابًۢا
```

Opening basmala was treated as recitational context only; no seed was initiated from it. Basmala roots inspected only as opening-context constraints/corroborators: `س م و`, `ء ل ه`, `ر ح م`.

Permitted resources used:

- `resources/quran/surah_110.json`
- `v1/prompts/stage1.md`
- `resources/qac_root_ayah.tsv` for S110 root/word sequence because `resources/qac.sqlite` is empty
- `resources/attachments.tsv`, header and S110:1-3 rows only
- `resources/v4_branches.tsv` as the local branch copy because `resources/furuq_v4.sqlite` is empty; accepted rows only for S110 roots

No translation, tafsir, hadith, web source, or other surah output was used as evidence.

## Ordered recitation state

| Pos | Surface | Root | Form / role |
| --- | --- | --- | --- |
| 110:1:2 | جَآءَ | `ج ي ء` | perfect verb; temporal condition under `إِذَا` |
| 110:1:3 | نَصْرُ | `ن ص ر` | nominative subject of `جاء` |
| 110:1:4 | ٱللَّهِ | `ء ل ه` | genitive mudaf ilayh of `نصر` |
| 110:1:6 | ٱلْفَتْحُ | `ف ت ح` | coordinated with `نصر` as second subject element |
| 110:2:2 | رَأَيْتَ | `ر ء ي` | perfect verb; 2MS observer |
| 110:2:3 | ٱلنَّاسَ | `ن و س` by QAC root TSV; attachment row gives `أ ن س` | accusative object of seeing |
| 110:2:4 | يَدْخُلُونَ | `د خ ل` | imperfect plural; hal clause describing people |
| 110:2:6 | دِينِ | `د ي ن` | governed by `فِي` as entry field |
| 110:2:7 | ٱللَّهِ | `ء ل ه` | genitive mudaf ilayh of `دين` |
| 110:2:8 | أَفْوَاجًا | `ف و ج` | accusative hal/manner of entering |
| 110:3:2 | سَبِّحْ | `س ب ح` | Form II imperative, sequenced by `فـ` |
| 110:3:3 | حَمْدِ | `ح م د` | `بـ` complement of `سبح` |
| 110:3:4 | رَبِّكَ | `ر ب ب` | genitive mudaf ilayh of `حمد`; 2MS possessive |
| 110:3:6 | ٱسْتَغْفِرْهُ | `غ ف ر` | Form X imperative; object suffix `ه` |
| 110:3:8 | كَانَ | `ك و ن` | predicate carrier in `إنه كان توابا` |
| 110:3:9 | تَوَّابًا | `ت و ب` | accusative predicate of `كان` |

Attachment constraints used repeatedly:

- `إِذَا` makes the first ayah a temporal condition for `جاء`.
- `نصر` is the grammatical subject of `جاء`; `الله` is attached to `نصر`, not to `فتح`.
- `فتح` is coordinated with `نصر`.
- `الناس` is the object of `رأيت`; `يدخلون في دين الله أفواجا` is its circumstantial clause.
- `دين` is governed by `في`; `الله` is attached to `دين`.
- `أفواجا` describes the manner of entry.
- `فسبح` is the response after the condition and sight.
- `بحمد ربك` is the complement of `سبح`; `استغفره` is coordinated with it.
- `إنه كان توابا` closes as explanatory predicate; `توابا` is predicate of `كان`.

## Root dossier inventory

The exhaustive lexical seed count is occurrence × accepted branch. The `ج ي ء` root has duplicated furuq rows from two source-normalized roots; all rows were tested, with duplicate branch IDs disambiguated as `ج ي ء-src1` and `ج ي ء-src2` in the seed ledger.

| Root occurrence(s) | Accepted branch IDs tested |
| --- | --- |
| `110:1:2 ج ي ء` | src1 B001-B006; src2 B001-B003 |
| `110:1:3 ن ص ر` | B001-B007 |
| `110:1:4 ء ل ه` | B001-B002 |
| `110:1:6 ف ت ح` | B001-B009 |
| `110:2:2 ر ء ي` | B001-B013 |
| `110:2:3 ن و س` | B001-B003 |
| `110:2:4 د خ ل` | B001-B010 |
| `110:2:6 د ي ن` | B001-B007 |
| `110:2:7 ء ل ه` | B001-B002 |
| `110:2:8 ف و ج` | B001-B002 |
| `110:3:2 س ب ح` | B001, B002, B004-B008 |
| `110:3:3 ح م د` | B001-B005 |
| `110:3:4 ر ب ب` | B001-B017 |
| `110:3:6 غ ف ر` | B001-B008 |
| `110:3:8 ك و ن` | B001-B006 |
| `110:3:9 ت و ب` | B003 |

Total lexical seed passes audited: 108. Every lexical seed pass read the other passage-root dossiers continuously in recitation order before selecting expansions or terminating.

## Candidate synthesis units

### S110-CSU-01 — Arrival of divine aid opens a threshold

- `candidate_id`: S110-CSU-01
- `ayah_range`: 110:1-3
- `seed_type`: lexical/constructional convergence
- `seed`: `110:1:2 جَاءَ × ج ي ء B001 المجيء والحصول`
- `generating_set`: `(E: ج ي ء B001 coming/obtaining)`, `(E: attachment 110:1 a1 temporal condition)`, `(E: ن ص ر B001 aid/victory)`, `(E: ف ت ح B001 opened threshold)`, `(E: ف ت ح B004 victory/opening by conquest)`, `(E: د خ ل B001 entry)`.
- `selected_branches`: `ج ي ء B001`; `ن ص ر B001`; `ف ت ح B001/B004`; `د خ ل B001`; `د ي ن B001`; `ف و ج B001`.
- `constructed_model`: a decisive arrival event brings divine aid, and that aid opens a formerly closed public threshold. The next activation is not private possession but visible movement through the opened boundary: people enter the obedience/religion field in cohorts.
- `freeze_point`: after `جاء نصر الله والفتح` plus the entry branch of `دخل` are joined.
- `predictions_at_freeze`: a field into which entry occurs; visible public confirmation; collective rather than solitary movement; a response by the addressee after the condition is fulfilled.
- `unused_features_tested`: `رأيت`, `الناس`, `في دين الله`, `أفواجا`, `فسبح`, `بحمد ربك`, `استغفره`, `إنه كان توابا`, ayah boundaries, `فـ`, repeated `الله`.
- `corroborators`: `(C: ر ء ي B001)` gives direct witness; `(C: ن و س B003/attachment object الناس)` supplies people as the public mass; `(C: ف و ج B001)` supplies group-after-group entry; `(C: د ي ن B001)` names the field as obedience/religion; `(C: فـ in 110:3)` makes praise/forgiveness response conditional on the arrival and sight.
- `constraints`: `(K: جاء does not specify direction of travel by itself; the direction is supplied by دخل في دين الله)`. `(K: فتح is coordinated with نصر, not a separate object opened by the addressee)`.
- `temporal_reactivation_notes`: `فتح` first sounds like victory/opening; `يدخلون في دين الله` later reactivates it as an actual threshold; `فسبح` then reinterprets the opening as a divine completion requiring liturgical response.
- `rival_models`: water-opening model from `نصر B004` + `فتح B005`; judgment model from `فتح B003`; both are retained below but weaker.
- `grade`: strong
- `grade_rationale`: exact ordered fit: arrival -> aid/opening -> visible entry -> response. Several unused features independently fill predictions after freeze.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` S110 rows; attachment rows 110:1 a1-a4, 110:2 a1-a5, 110:3 a1-a8; `v4_branches.tsv` rows for `ج ي ء`, `ن ص ر`, `ف ت ح`, `د خ ل`, `د ي ن`, `ف و ج`, `ر ء ي`.

### S110-CSU-02 — Victory is reclassified as entry into obedience

- `candidate_id`: S110-CSU-02
- `ayah_range`: 110:1-2
- `seed_type`: lexical
- `seed`: `110:1:3 نَصْرُ × ن ص ر B001 النصرة عون وإظهار`
- `generating_set`: `(E: ن ص ر B001 aid/victory)`, `(E: ء ل ه B002 divine name attached by idafa)`, `(E: ف ت ح B004 victory/opening)`, `(E: د خ ل B001 entry)`, `(E: د ي ن B001 obedience/religion)`.
- `selected_branches`: `ن ص ر B001`; `ف ت ح B004`; `د خ ل B001`; `د ي ن B001`; `ء ل ه B002`.
- `constructed_model`: aid is not merely military relief; it manifests as a social-religious reorientation in which the aided side is shown by the influx of people into the divine obedience-field.
- `freeze_point`: after the aid/opening/entry/obedience circuit is formed.
- `predictions_at_freeze`: the aid should be explicitly God's; the later event should be observable and collective; the addressee should not claim autonomous credit.
- `unused_features_tested`: `رأيت`, `الناس`, `أفواجا`, `فسبح بحمد ربك`, `استغفره`.
- `corroborators`: idafa `نصر الله` and `دين الله` repeat the divine source; `رأيت الناس` makes victory visible; `أفواجا` makes it social and cumulative; `بحمد ربك` assigns praise to the Lord.
- `constraints`: `نصر` is the subject that arrives, not an imperative to seek aid. The text supplies no explicit named enemy.
- `temporal_reactivation_notes`: early `نصر` predicts relief over an opponent; later `دين الله` shifts the field from combat-result to allegiance-result.
- `rival_models`: `ن ص ر B002` revenge/indemnification; `B004` rain aid.
- `grade`: strong
- `grade_rationale`: strong lexical and structural fit, especially repeated `الله` and `فـ` response.
- `source_queries_or_rows_used`: same S110 QAC/attachment rows; `ن ص ر B001`, `ف ت ح B004`, `د خ ل B001`, `د ي ن B001`.

### S110-CSU-03 — Closedness opens into visible mass ingress

- `candidate_id`: S110-CSU-03
- `ayah_range`: 110:1-2
- `seed_type`: lexical
- `seed`: `110:1:6 ٱلْفَتْحُ × ف ت ح B001 انفراج المغلق واتساع المدخل`
- `generating_set`: `(E: ف ت ح B001 opening a closed thing / widened entrance)`, `(E: ج ي ء B001 arrival)`, `(E: د خ ل B001 entry)`, `(E: في دين الله attachment)`, `(E: ف و ج B001 cohorts)`.
- `selected_branches`: `فتح B001`; `ج يء B001`; `دخل B001`; `دين B001`; `فوج B001`.
- `constructed_model`: the passage first activates an opening, then reveals what the opening is for: multiple groups pass through into the field of divine religion.
- `freeze_point`: after `فتح` is read as an opened entrance and `يدخلون في دين الله` is selected.
- `predictions_at_freeze`: the opening should be followed by entry, a field or interior, and a plural body passing through.
- `unused_features_tested`: `رأيت`, `الناس`, `أفواجا`, `فسبح`, `استغفره`, `كان توابا`.
- `corroborators`: `في` + `دين` is a containment/field marker; `أفواجا` supplies repeated group movement; `رأيت` marks the opening as public and visible.
- `constraints`: `فتح` in 110:1 is coordinated with `نصر`, so it is not an independent physical door in the primary proposition.
- `temporal_reactivation_notes`: `فتح` becomes more concrete only when `يدخلون في` appears; the earlier opening is reactivated by later entry syntax.
- `rival_models`: `فتح B004` victory branch; `فتح B008` cognitive/spiritual opening; both can converge.
- `grade`: strong
- `grade_rationale`: the seed predicts later entry and containment before those unused features are tested.
- `source_queries_or_rows_used`: attachment rows 110:1 a4 and 110:2 a2-a5; `ف ت ح`, `د خ ل`, `د ي ن`, `ف و ج` dossiers.

### S110-CSU-04 — Seeing confirms the opened condition

- `candidate_id`: S110-CSU-04
- `ayah_range`: 110:2
- `seed_type`: lexical/morphosyntactic
- `seed`: `110:2:2 رَأَيْتَ × ر ء ي B001 رؤية العين والبصيرة`
- `generating_set`: `(E: ر ء ي B001 seeing)`, `(E: direct-object attachment الناس)`, `(E: hal clause يدخلون في دين الله أفواجا)`.
- `selected_branches`: `رأي B001`; `دخل B001`; `دين B001`; `فوج B001`.
- `constructed_model`: the addressee receives a visual confirmation of what the first ayah condition announced. The event is not only a report but a seen state: people are entering.
- `freeze_point`: after the object and hal clause are attached to `رأيت`.
- `predictions_at_freeze`: the seen object should be visible/social; the seen action should display the earlier opening; the following command should respond to confirmed fulfillment, not to hidden speculation.
- `unused_features_tested`: `إذا جاء`, `نصر الله والفتح`, `فسبح`, `استغفره`, `إنه كان توابا`.
- `corroborators`: earlier `فتح` supplies what the seen entry presupposes; `فـ` in `فسبح` makes sight part of the response trigger; `أفواجا` fills visibility through mass grouping.
- `constraints`: `رأيت` can include knowledge, but the local direct object plus hal clause favor public perception over private inference.
- `temporal_reactivation_notes`: `رأيت` converts earlier condition into perceptual completion; the addressee's response is delayed until the event is seen.
- `rival_models`: `رأي B002` deliberative judgment; `B012` causing to see; weaker but retained in ledger.
- `grade`: medium-strong
- `grade_rationale`: excellent structural fit; less generative than the `فتح/دخل` model but a key temporal hinge.
- `source_queries_or_rows_used`: `ر ء ي` dossier; attachment rows 110:2 a1-a5.

### S110-CSU-05 — Entry into the divine obedience-field

- `candidate_id`: S110-CSU-05
- `ayah_range`: 110:2-3
- `seed_type`: lexical/constructional
- `seed`: `110:2:4 يَدْخُلُونَ × د خ ل B001 الولوج إلى داخل`
- `generating_set`: `(E: د خ ل B001 entering)`, `(E: في دين الله prep-complement)`, `(E: د ي ن B001 obedience/religion)`, `(E: ء ل ه B002 divine name)`, `(E: ف و ج B001 groups)`.
- `selected_branches`: `دخل B001`; `دين B001`; `ءله B002`; `فوج B001`; later `سبح B001/B002`, `غفر B002`.
- `constructed_model`: collective ingress into a divine obedience field produces a required response by the addressee: purification of attribution through praise and request for covering/forgiveness.
- `freeze_point`: after entry field and cohort manner are fixed.
- `predictions_at_freeze`: movement should have an inside/outside contrast; entry should be into an owned/divine field; closure should address the Lord rather than the entrants.
- `unused_features_tested`: `فسبح بحمد ربك`, `استغفره`, `إنه كان توابا`, `نصر الله والفتح`.
- `corroborators`: `دين الله` supplies divine ownership; `ربك` supplies direct relation to addressee; `غفر`/`توب` supply return/covering after mass entry.
- `constraints`: no physical building or literal doorway is named; entry is primary into `دين`, an abstract field.
- `temporal_reactivation_notes`: the visible ingress reactivates `فتح` and transforms victory into submission/obedience.
- `rival_models`: `دخل B005` outsider mixing; `دخل B004` hidden corruption; both constrain but do not fit the explicit `دين الله`.
- `grade`: strong
- `grade_rationale`: exact `في` construction, exact plural subject, exact manner, and strong backward reactivation of `فتح`.
- `source_queries_or_rows_used`: S110 root rows; attachment 110:2 a2-a5; `د خ ل`, `د ي ن`, `ف و ج`.

### S110-CSU-06 — Cohorts complete the public-scale image

- `candidate_id`: S110-CSU-06
- `ayah_range`: 110:2
- `seed_type`: lexical
- `seed`: `110:2:8 أَفْوَاجًا × ف و ج B001 الجماعة من الناس`
- `generating_set`: `(E: ف و ج B001 group after group)`, `(E: ن و س B003 people)`, `(E: د خ ل B001 entry)`, `(E: ر ء ي B001 seeing)`.
- `selected_branches`: `فوج B001`; `ناس as attachment/QAC occurrence`; `دخل B001`; `رأي B001`.
- `constructed_model`: the passage's proof of opening is multiplicity in motion: not an isolated entrant but repeated groups entering visibly.
- `freeze_point`: after the cohort manner is linked to entry.
- `predictions_at_freeze`: a prior opening/victory should explain why the groups can enter; a response should avoid attributing the mass success to the addressee.
- `unused_features_tested`: `نصر الله`, `الفتح`, `فسبح بحمد ربك`, `استغفره`.
- `corroborators`: `فتح` supplies opened access; `نصر الله` supplies the causal power; `بحمد ربك` turns mass success into praise.
- `constraints`: `أفواجا` modifies manner; it does not itself state the content of religion or the cause.
- `temporal_reactivation_notes`: by the time `أفواجا` is heard, `فتح` is re-heard as a large-scale access event.
- `rival_models`: `فوج B002` wide space can supply an opened passage but lacks the explicit human groups.
- `grade`: medium-strong
- `grade_rationale`: highly local and structurally exact, though it covers only the public-scale subimage.
- `source_queries_or_rows_used`: `ف و ج` dossier; attachment 110:2 a5.

### S110-CSU-07 — Praise and forgiveness as the required response to completion

- `candidate_id`: S110-CSU-07
- `ayah_range`: 110:3
- `seed_type`: constructional/lexical
- `seed`: `فَسَبِّحْ بِحَمْدِ رَبِّكَ وَٱسْتَغْفِرْهُ`
- `generating_set`: `(E: فـ response sequencing)`, `(E: س ب ح B001 worship/remembering)`, `(E: س ب ح B002 declaring transcendence)`, `(E: ح م د B001 praise/thanks)`, `(E: ر ب ب B001 Lord/owner)`, `(E: غ ف ر B002 forgiveness of sin)`, `(E: ت و ب B003 inviting/allowing repentance)`.
- `selected_branches`: `سبح B001/B002`; `حمد B001`; `ربب B001`; `غفر B002`; `توب B003`.
- `constructed_model`: after public victory and mass entry, the addressee is directed to remove misattribution and deficiency: declare the Lord free of imperfection with praise, and seek covering/forgiveness from the one characterized by repeated turning/acceptance.
- `freeze_point`: after the paired imperatives and closing predicate are linked.
- `predictions_at_freeze`: the response should be Lord-directed; it should include both positive praise and removal/covering; closure should explain why seeking forgiveness is meaningful.
- `unused_features_tested`: earlier `نصر الله`, `دين الله`, repeated divine idafa, `كان`.
- `corroborators`: repeated `الله`/`ربك` creates divine referent continuity; `كان توابا` explains the forgiveness command; `فـ` ties response to fulfilled condition.
- `constraints`: `سبح` is an imperative to the addressee, not a description of the entering people. `استغفره` has divine object suffix, not forgiveness sought from the people.
- `temporal_reactivation_notes`: the closing response retroactively frames victory as God's act, not the addressee's possession.
- `rival_models`: `سبح B004/B005` movement/speed branches are weak secondary simulations; retained in ledger.
- `grade`: strong
- `grade_rationale`: exact command sequence, exact complement attachments, and exact closure.
- `source_queries_or_rows_used`: attachment 110:3 a1-a8; `س ب ح`, `ح م د`, `ر ب ب`, `غ ف ر`, `ك و ن`, `ت و ب`.

### S110-CSU-08 — Covering, return, and closure

- `candidate_id`: S110-CSU-08
- `ayah_range`: 110:3
- `seed_type`: lexical
- `seed`: `110:3:6 ٱسْتَغْفِرْهُ × غ ف ر B002 ستر الذنب وصون صاحبه من أثره`
- `generating_set`: `(E: غ ف ر B002 forgiveness/covering from effect)`, `(E: object suffix ه)`, `(E: ت و ب B003 offered repentance/return)`, `(E: ك و ن B001 settled predicate)`.
- `selected_branches`: `غفر B002`; `توب B003`; `كون B001`; `ربب B001`.
- `constructed_model`: the passage closes by turning from public influx to the addressee's need for covered deficiency and return. The closing predicate stabilizes the basis of the request: He is continually accepting/soliciting return.
- `freeze_point`: after `استغفره` and `إنه كان توابا` are linked.
- `predictions_at_freeze`: a prior reason for humility; divine object continuity; a stable attribute explaining the imperative.
- `unused_features_tested`: `نصر الله`, `الفتح`, `رأيت الناس`, `فسبح بحمد ربك`.
- `corroborators`: mass victory creates a risk of triumphal self-credit; `بحمد ربك` places credit with the Lord; `إنه` pronoun continues the divine object.
- `constraints`: the text does not specify a named sin; the model must remain response-geometry, not an external biography.
- `temporal_reactivation_notes`: after success is seen, `استغفره` reverses expected triumph into humble return.
- `rival_models`: `غفر B001` general covering and `B008` mass totality both contribute secondary imagery but do not replace B002.
- `grade`: medium-strong
- `grade_rationale`: closing fit is exact; the specific deficiency is inferred from response sequence, not named.
- `source_queries_or_rows_used`: `غ ف ر`, `ت و ب`, `ك و ن`; attachment 110:3 a4-a8.

### S110-CSU-09 — Water, rain, and opened channels

- `candidate_id`: S110-CSU-09
- `ayah_range`: 110:1-2
- `seed_type`: lexical secondary simulation
- `seed`: `ن ص ر B004 النصر مطر وإغاثة`
- `generating_set`: `(E: ن ص ر B004 rain/relief)`, `(E: ف ت ح B005 water issuing from an opening)`, `(E: ج ي ء B003 water gathered in a hollow/around a fort)`, `(E: ن ص ر B007 channels from far away)`, `(E: ر ب ب B008/B013 cloud/water abundance)`, `(E: ف و ج B002 wide opening between rises)`.
- `selected_branches`: `نصر B004/B007`; `فتح B005`; `جيء B003`; `ربب B008/B013`; `فوج B002`.
- `constructed_model`: divine relief appears as water arriving, channels opening, and gathered flow spreading through a widened passage. This simulates the social influx of people as a life-giving current.
- `freeze_point`: after rain/channel/opened-flow image is formed.
- `predictions_at_freeze`: flow, gathered mass, opened passages, replenishment, and a receiving field.
- `unused_features_tested`: `يدخلون`, `أفواجا`, `دين الله`, `فسبح بحمد ربك`, `استغفره`.
- `corroborators`: `يدخلون` supplies flow through a boundary; `أفواجا` supplies successive groups like waves; `حمد` can answer relief as gratitude.
- `constraints`: no literal water, rain, river, cloud, valley, or plant occurs in the primary text; it remains a secondary image.
- `temporal_reactivation_notes`: later entry reactivates earlier `فتح` as channel-opening; `أفواجا` makes the flow wave-like.
- `rival_models`: primary public-entry model CSU-01/03.
- `grade`: medium
- `grade_rationale`: multiple remote branches interlock specifically, but primary surface lacks water lexemes.
- `source_queries_or_rows_used`: `ن ص ر B004/B007`, `ف ت ح B005`, `ج ي ء B003`, `ر ب ب B008/B013`, `ف و ج B002`.

### S110-CSU-10 — Judgment and final settlement

- `candidate_id`: S110-CSU-10
- `ayah_range`: 110:1-3
- `seed_type`: lexical secondary simulation
- `seed`: `ف ت ح B003 فصل الإغلاق بالحكم والقضاء`
- `generating_set`: `(E: فتح B003 judgment/decision)`, `(E: دين B002 accounting/recompense)`, `(E: رأي B002 knowledge/judgment)`, `(E: كون B001 settled occurrence)`, `(E: توب B003 invitation to repentance)`.
- `selected_branches`: `فتح B003`; `دين B002`; `رأي B002`; `كون B001`; `توب B003`; weakly `غفر B002`.
- `constructed_model`: the opening is a decisive settlement of a contested matter; the visible entry becomes evidence in the case; the closure gives the correct verdict-response: praise and seek forgiveness before the one who governs return.
- `freeze_point`: after judgment/opening and account/return are linked.
- `predictions_at_freeze`: public evidence, a judge/sovereign, and a closing decree or stable predicate.
- `unused_features_tested`: `رأيت`, `إنه كان توابا`, repeated `الله`, `ربك`.
- `corroborators`: `رأيت` supplies witnessed evidence; `كان توابا` supplies settled predicate; `الله/ربك` supplies sovereign referent.
- `constraints`: no explicit litigants or courtroom language appear; the victory/opening reading is primary.
- `temporal_reactivation_notes`: `فتح` can first sound like victory; `كان توابا` later gives a judgment-like settled attribute.
- `rival_models`: CSU-01, CSU-03.
- `grade`: medium
- `grade_rationale`: coherent but depends on a less immediate branch of `فتح`.
- `source_queries_or_rows_used`: `ف ت ح B003`, `د ي ن B002`, `ر ء ي B002`, `ك و ن B001`, `ت و ب B003`.

### S110-CSU-11 — Divine ownership and repeated idafa

- `candidate_id`: S110-CSU-11
- `ayah_range`: 110:1-3
- `seed_type`: morphosyntactic
- `seed`: repeated divine attachment: `نصر الله`, `دين الله`, `حمد ربك`
- `generating_set`: `(E: ء ل ه B002 divine name in 110:1 and 110:2)`, `(E: ر ب ب B001 Lord/owner in 110:3)`, idafa attachments 110:1 a3, 110:2 a4, 110:3 a2-a3.
- `selected_branches`: `ءله B002`; `ربب B001`; `حمد B001`; `سبح B002`.
- `constructed_model`: the passage repeatedly binds the decisive event, the entry field, and the response to the same divine source. The addressee sees the event but does not own it.
- `freeze_point`: after three possessive/idafa links are aligned.
- `predictions_at_freeze`: response should be attributional; the addressee's role should be witness and worshipper, not cause.
- `unused_features_tested`: `فسبح`, `بحمد`, `استغفره`, `توابا`.
- `corroborators`: `سبح` and `حمد` enact proper attribution; `استغفره` removes improper self-attribution.
- `constraints`: `الله` in `نصر الله` and `دين الله` is genitive complement, not a separate clause subject; `ربك` introduces relation to addressee but not ownership by addressee.
- `temporal_reactivation_notes`: repeated `الله` primes divine source; `ربك` personalizes the relation at response time.
- `rival_models`: none serious.
- `grade`: strong
- `grade_rationale`: exact repetition and attachment geometry across all three ayat.
- `source_queries_or_rows_used`: attachment rows 110:1 a3, 110:2 a4, 110:3 a2-a3; `ء ل ه`, `ر ب ب`.

### S110-CSU-12 — Terminated hidden-corruption and mixed-entry rivals

- `candidate_id`: S110-CSU-12
- `ayah_range`: 110:2
- `seed_type`: lexical rival bundle
- `seed`: `د خ ل B003/B004/B005` and `ر ء ي B005`
- `generating_set`: `(E: دخل B003 hidden interior)`, `(E: دخل B004 hidden corruption)`, `(E: دخل B005 outsider mixed into a people)`, `(E: رأي B005 showing-off)`.
- `selected_branches`: tested but not retained as primary.
- `constructed_model`: possible negative simulation: outsiders mix into a community, hidden faults enter, or visible acts are performed to be seen.
- `freeze_point`: after hidden/mixed entry is hypothesized.
- `predictions_at_freeze`: signs of corruption, hypocrisy, impurity, or warning.
- `unused_features_tested`: `دين الله`, `نصر الله`, `فسبح بحمد ربك`, `استغفره`, `توابا`.
- `corroborators`: `استغفره` only broadly allows humility/defect.
- `constraints`: the hal clause explicitly describes people entering `دين الله أفواجا`; no word supplies corruption, hypocrisy, or blame. `فسبح` is a command to the addressee, not a condemnation of entrants.
- `temporal_reactivation_notes`: the negative branches are inhibited when `دين الله` and `أفواجا` arrive.
- `rival_models`: CSU-05 primary entry model.
- `grade`: unlikely
- `grade_rationale`: lexically possible but locally defeated by syntax and positive divine attribution.
- `source_queries_or_rows_used`: `د خ ل B003/B004/B005`, `ر ء ي B005`; attachment 110:2 a2-a5.

## Exhaustive lexical seed ledger

Legend: `E` branches helped construct an image before freeze; `C/K` rows mainly corroborated or constrained after freeze; `T` terminated. In every row, the same full S110 dossier set was read before selecting or terminating.

### 110:1:2 جَاءَ — `ج ي ء`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L001 `ج ي ء-src1 B001` | coming/arrival/obtaining | E: `نصر B001`, `فتح B001/B004`, `دخل B001` -> CSU-01 | C: `رأيت`, `أفواجا`, `فسبح`; K: no literal traveler named | strong |
| L002 `ج ي ء-src1 B002` | rivalry in repeated coming | E: `فوج B001`, weak `نصر B001` -> contest of arrivals | K: no reciprocal coming construction; no rival subject | weak |
| L003 `ج ي ء-src1 B003` | water gathered in hollow/around fort | E: `نصر B004/B007`, `فتح B005`, `ربب B013` -> CSU-09 | K: no water lexeme; secondary only | medium-weak |
| L004 `ج ي ء-src1 B004` | bringing/causing presence | E: `نصر B005`, `فتح B008`, `رأي B012` -> divine bringing-to-view | C: seen entry; K: جاء is intransitive here | medium |
| L005 `ج ي ء-src1 B005` | compulsion toward a place | E: `دخل B001`, `دين B004` -> compelled submission fork | K: no coercion/اضطرار marker; `دين الله` not forced slavery | weak |
| L006 `ج ي ء-src1 B006` | gathered pus in wound | E: none | K: no wound, illness, or discharge; `غفر B004` cannot rescue it | unlikely |
| L007 `ج ي ء-src2 B001` | coming plus rivalry compressed | E: primary arrival only; rivalry fork terminated | C: condition arrival; K: no mutual coming | medium |
| L008 `ج ي ء-src2 B002` | water-collection place | E: same as L003 -> CSU-09 | K: no literal water | medium-weak |
| L009 `ج ي ء-src2 B003` | wound/pus collection | E: none | K: defeated by positive `نصر الله` and no wound roles | unlikely |

### 110:1:3 نَصْرُ — `ن ص ر`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L010 `ن ص ر B001` | aid/victory/manifest support | E: `فتح B004`, `دخل B001`, `دين B001` -> CSU-02 | C: `رأيت`, `أفواجا`, `فسبح بحمد`; K: no enemy named | strong |
| L011 `ن ص ر B002` | oppressed party's redress | E: `فتح B003`, `دين B002` -> judgment/redress fork | K: no oppressor/victim named | medium-weak |
| L012 `ن ص ر B003` | coming to a land | E: `جاء B001`, `دخل B001`, `فوج B001` -> arrival-to-territory image | K: `نصر` is not locative in syntax; no البلد/أرض | weak |
| L013 `ن ص ر B004` | rain/relief | E: `فتح B005`, `ج يء B003`, `ربب B008/B013`, `فوج B002` -> CSU-09 | C: `أفواجا` wave-like; K: no water lexeme | medium |
| L014 `ن ص ر B005` | giving/good bestowed | E: `حمد B001`, `ربب B001`, `غفر B002` -> gift answered by praise | C: `فسبح`; K: `نصر` contextually aid not generic gift | medium |
| L015 `ن ص ر B006` | Christian/nasrani affiliation | E: none | K: no Christian group, `دين الله` not specified as نصرانية | unlikely |
| L016 `ن ص ر B007` | far water-channels reaching a collection | E: `فتح B005`, `ج يء B003`, `ربب B013` -> water-channel subimage | K: remote; no literal channels | weak |

### 110:1:4 ٱللَّهِ — `ء ل ه`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L017 `ء ل ه B001` | worshipped/divine object | E: `دين B001`, `سبح B001/B002`, `ربب B001` -> worship field | C: repeated `الله`, `حمد ربك`; K: proper-name use is primary | medium-strong |
| L018 `ء ل ه B002` | divine name | E: idafa `نصر الله`, repeated `دين الله`, `ربك` -> CSU-11 | C: `سبح`, `حمد`, `استغفره`; K: no oath/vocative syntax here | strong |

### 110:1:6 ٱلْفَتْحُ — `ف ت ح`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L019 `ف ت ح B001` | opening a closed threshold | E: `دخل B001`, `دين B001`, `فوج B001` -> CSU-03 | C: `في`, `أفواجا`; K: abstract entry field | strong |
| L020 `ف ت ح B002` | beginning/fatihat | E: `جاء B001`, `فسبح` -> new phase begins after victory | C: `فـ`; K: passage is not opening a recitation or prayer formally | medium-weak |
| L021 `ف ت ح B003` | judgment/decision | E: `دين B002`, `رأي B002`, `كون B001` -> CSU-10 | C: `كان توابا`; K: no litigants | medium |
| L022 `ف ت ح B004` | victory/conquest | E: `نصر B001`, `دخل B001`, `فوج B001` -> CSU-02 | C: `رأيت الناس`; K: no battle scene | strong |
| L023 `ف ت ح B005` | water issuing from opening | E: `نصر B004`, `ج يء B003`, `ربب B013` -> CSU-09 | K: no literal water | medium-weak |
| L024 `ف ت ح B006` | key/instrument for locked thing | E: `دين B001`, weak `دخل B001` -> key-to-entry image | K: no key/instrument role | weak |
| L025 `ف ت ح B007` | opened treasury/store | E: `نصر B005`, `حمد B001` -> bestowed goods | K: no treasure/wealth lexeme | weak |
| L026 `ف ت ح B008` | cognitive/spiritual opening, relief | E: `رأي B001/B002`, `دين B001`, `غفر B002` -> insight and relief | C: `رأيت`; K: `الفتح` coordinated with victory | medium |
| L027 `ف ت ح B009` | boastful display of wealth/adab | E: none; possible rival to `استغفره` | K: no boastful actor; `حمد ربك` inhibits self-display | unlikely |

### 110:2:2 رَأَيْتَ — `ر ء ي`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L028 `ر ء ي B001` | seeing by eye/insight | E: object `الناس`, hal `يدخلون`, `فتح B001` -> CSU-04 | C: `فسبح`; K: no hidden-only event | medium-strong |
| L029 `ر ء ي B002` | opinion/judgment/thought | E: `فتح B003`, `دين B002` -> judgment fork CSU-10 | K: direct object + hal favor visible seeing | medium-weak |
| L030 `ر ء ي B003` | dream vision | E: none | K: no sleep/dream marker; public `الناس` object | unlikely |
| L031 `ر ء ي B004` | mutual facing/visibility | E: `فوج B001`, `دخل B001` -> public groups in view | C: `أفواجا`; K: no reciprocal facing | medium-weak |
| L032 `ر ء ي B005` | showing-off for people | E: weak `ناس`, `سبح` | K: no blame; `دين الله` and `حمد ربك` defeat riya reading | unlikely |
| L033 `ر ء ي B006` | appearance/visible aspect/mirror | E: `فتح B008`, `حمد B002` -> favorable appearance of event | K: no mirror/appearance noun | weak |
| L034 `ر ء ي B007` | menstrual sign / purity marker | E: none | K: no menstruation/purity cloth; `غفر` does not supply it | unlikely |
| L035 `ر ء ي B008` | familiar spirit/genie | E: none | K: no jinn, divination, possession | unlikely |
| L036 `ر ء ي B009` | lung/respiration injury | E: none | K: no body organ or injury; terminated | unlikely |
| L037 `ر ء ي B010` | visible pregnancy of animal | E: none | K: no animal/pregnancy; `توب` not birth | unlikely |
| L038 `ر ء ي B011` | raised banner/sign | E: `نصر B001`, `فتح B004`, `فوج B001` -> victory standard image | K: no banner noun; secondary only | weak |
| L039 `ر ء ي B012` | causing/showing to see | E: `ج يء B004`, `فتح B008` -> divine making-visible | C: `رأيت` morphology as 2MS witness; K: verb here means saw, not showed | medium |
| L040 `ر ء ي B013` | "tell me"/attention formula | E: none | K: no interrogative or report formula; terminated | unlikely |

### 110:2:3 ٱلنَّاسَ — `ن و س` / people occurrence

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L041 `ن و س B001` | swaying/dangling motion | E: `فوج B001`, `دخل B001` -> mass motion image | K: root assignment is remote for الناس; no dangling object | weak |
| L042 `ن و س B002` | driving camels | E: weak `دخل B007`, `فوج B001` -> driven herd/crowd | K: no camels, driver, or watering except remote water fork | unlikely |
| L043 `ن و س B003` | people / debated origin | E: direct object `الناس`, `فوج B001`, `دخل B001` -> public entrants | C: `رأيت`; K: root is review-status in TSV but occurrence itself is secure | medium-strong |

### 110:2:4 يَدْخُلُونَ — `د خ ل`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L044 `د خ ل B001` | entering inside | E: `في دين الله`, `فوج B001`, `فتح B001` -> CSU-05 | C: `رأيت`, `فسبح`; K: abstract not physical entry | strong |
| L045 `د خ ل B002` | marital consummation | E: none | K: no spouse/sexual participant; terminated | unlikely |
| L046 `د خ ل B003` | hidden interior/secret | E: weak `دين B001`, `غفر B002` -> inner-religion fork | K: hal clause is public visible; no secrecy marker | weak |
| L047 `د خ ل B004` | hidden corruption/defect | E: none; rival in CSU-12 | K: positive `دين الله`, no corruption word | unlikely |
| L048 `د خ ل B005` | outsider mixed into group | E: `ناس`, `فوج B001` -> mixed crowd rival | K: no foreignness or false affiliation marker | weak |
| L049 `د خ ل B006` | income/yield entering estate | E: `حمد B001`, `نصر B005` weak gift/yield | K: no property/estate; terminated | unlikely |
| L050 `د خ ل B007` | re-entering camels to drink | E: water model `نصر B004`, `فتح B005` | K: no camels/watering; secondary remote | weak |
| L051 `د خ ل B008` | interlocking/interior parts | E: `فوج B001`, `دين B001` weak integration image | K: no parts/joints/material texture | weak |
| L052 `د خ ل B009` | small bird entering caves/trees | E: none | K: no bird/cave/tree; terminated | unlikely |
| L053 `د خ ل B010` | palm basket for dates | E: none | K: no basket/dates; terminated | unlikely |

### 110:2:6 دِينِ — `د ي ن`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L054 `د ي ن B001` | obedience/religion | E: `دخل B001`, `ءله B002`, `فوج B001` -> CSU-05 | C: `سبح`, `حمد`, `ربك`; K: not generic custom | strong |
| L055 `د ي ن B002` | accounting/judgment/recompense | E: `فتح B003`, `رأي B002`, `كون B001` -> CSU-10 | K: no day/accounting lexeme; secondary | medium |
| L056 `د ي ن B003` | financial debt | E: `غفر B001` weak debt-covering | K: no money, lender, term, repayment | unlikely |
| L057 `د ي ن B004` | subjugation/ownership | E: `نصر B001`, `ربب B001`, `دخل B001` -> submission fork | K: text uses `دين الله`, not slavery terminology | medium-weak |
| L058 `د ي ن B005` | custom/habit | E: none | K: repeated divine idafa and entry defeat generic habit | weak |
| L059 `د ي ن B006` | city where authority obeyed | E: `فتح B001`, `دخل B001`, `فوج B001` -> city-entry image | K: no city/place noun; secondary | weak |
| L060 `د ي ن B007` | entrusting/crediting someone by his religion | E: `رأي B002`, `غفر B002` weak trust/forgiveness | K: no oath/legal entrusting | weak |

### 110:2:7 ٱللَّهِ — `ء ل ه`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L061 `ء ل ه B001` | worshipped/mabud inside entry field | E: `دين B001`, `دخل B001`, `سبح B001` | C: `حمد ربك`; K: proper-name syntax primary | medium-strong |
| L062 `ء ل ه B002` | divine name in `دين الله` | E: repeated name from `نصر الله`, `ربك` -> CSU-11 | C: `استغفره`; K: no oath/vocative | strong |

### 110:2:8 أَفْوَاجًا — `ف و ج`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L063 `ف و ج B001` | human groups/cohorts | E: `ناس`, `دخل B001`, `فتح B001/B004` -> CSU-06 | C: `رأيت`, `نصر الله`; K: only manner, not cause | medium-strong |
| L064 `ف و ج B002` | wide gap/plain between rises | E: `فتح B001`, water/threshold subimage | K: no terrain/ridge; secondary only | weak |

### 110:3:2 سَبِّحْ — `س ب ح`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L065 `س ب ح B001` | worship/remembering/prayer | E: `حمد B001`, `ربب B001`, `غفر B002`, `توب B003` -> CSU-07 | C: `فـ`, prior `نصر الله`; K: not describing entrants | strong |
| L066 `س ب ح B002` | declaring transcendence/absolving | E: `حمد B001`, `غفر B001/B002` -> purification response | C: divine idafa; K: no explicit fault named | strong |
| L067 `س ب ح B004` | swimming/running swiftly | E: weak `فوج B001`, `دخل B001` -> flow/motion image | K: no water or speed verb; secondary only | weak |
| L068 `س ب ح B005` | free movement/occupation in livelihood | E: weak after opening -> room to move | K: imperative context is worship, not commerce | unlikely |
| L069 `س ب ح B006` | prayer beads | E: none | K: no beads/counting object; likely later material culture | unlikely |
| L070 `س ب ح B007` | leather garments/strong cloak | E: `غفر B001` covering weakly | K: no garment/skin; terminated | unlikely |
| L071 `س ب ح B008` | named sacred place/valley | E: weak place-entry image | K: no place-name syntax | unlikely |

### 110:3:3 حَمْدِ — `ح م د`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L072 `ح م د B001` | praise/thanks opposite blame | E: `سبح B001/B002`, `ربب B001`, `نصر B005` -> CSU-07 | C: victory as reason for praise; K: praise is by addressee | strong |
| L073 `ح م د B002` | finding something praiseworthy/satisfactory | E: `رأي B001`, `فتح B008` -> event seen as praiseworthy | K: no explicit evaluation verb beyond command | medium |
| L074 `ح م د B003` | one of many praised qualities | E: `ربب B001`, `نصر B001` -> divine qualities praised | C: repeated divine names; K: not a naming passage | medium |
| L075 `ح م د B004` | praiseworthy end/utmost | E: `كون B001`, `توب B003` -> closure reaches proper end | C: final `توابا`; K: branch formula absent | medium-weak |
| L076 `ح م د B005` | seeking credit by benefaction | E: rival self-credit model | K: `بحمد ربك` defeats self-credit; no human benefactor boasting | unlikely |

### 110:3:4 رَبِّكَ — `ر ب ب`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L077 `ر ب ب B001` | Lord/owner/master | E: `حمد B001`, `سبح B002`, `غفر B002` -> CSU-07/11 | C: repeated `الله`; K: relation is idafa to addressee, not addressee ownership | strong |
| L078 `ر ب ب B002` | nurture/repair/completion | E: `نصر B005`, `فتح B008`, `توب B003` -> completion/return image | C: closure after victory; K: no explicit تربى/إصلاح object | medium |
| L079 `ر ب ب B003` | rabbinic/divine knowledge | E: `رأي B002`, `فتح B008` weak insight | K: no scholars/teaching | weak |
| L080 `ر ب ب B004` | large groups/tribal assemblies | E: `فوج B001`, `ناس` -> mass group support | K: not attached to people; `ربك` means Lord | weak |
| L081 `ر ب ب B005` | stepchild/caretaker | E: none | K: no family/child roles | unlikely |
| L082 `ر ب ب B006` | thick syrup/repairing skins/food | E: none | K: no food/leather/medicine | unlikely |
| L083 `ر ب ب B007` | staying/lasting/dwelling | E: `كون B001`, `توب B003` -> lasting attribute | C: `كان توابا`; K: branch remote for `ربك` | medium-weak |
| L084 `ر ب ب B008` | clouds/rain nurturing plants | E: water model `نصر B004`, `فتح B005` -> CSU-09 | K: no cloud lexeme | weak |
| L085 `ر ب ب B009` | newborn ewe/newness | E: none | K: no birth/livestock | unlikely |
| L086 `ر ب ب B010` | container of lots/arrows | E: none | K: no lots/arrows/container | unlikely |
| L087 `ر ب ب B011` | covenant/neighboring pact | E: `دين B001`, `غفر B002` weak covenant return | K: no عهد/ميثاق syntax | weak |
| L088 `ر ب ب B012` | persistent green plant | E: water model weakly | K: no plant terms | unlikely |
| L089 `ر ب ب B013` | abundant water | E: water model `نصر B004`, `فتح B005`, `جاء B003` -> CSU-09 | K: no water surface words | weak |
| L090 `ر ب ب B014` | herd/cluster of wild cattle/camels | E: `فوج B001`, `نوس B002` weak herd image | K: no animal group | unlikely |
| L091 `ر ب ب B015` | particle `رب` | E: none | K: occurrence is noun `رب`, not particle | unlikely |
| L092 `ر ب ب B016` | need/knot/blessing | E: `نصر B005`, `غفر B002` weak need/blessing | K: no need/knot word | weak |
| L093 `ر ب ب B017` | chief of sailors | E: none | K: no sea/sailors | unlikely |

### 110:3:6 ٱسْتَغْفِرْهُ — `غ ف ر`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L094 `غ ف ر B001` | covering/protective cover | E: `سبح B002`, `حمد B001`, `توب B003` -> covering after victory | C: `استغفره` form; K: general cover, not full sin-forgiveness by itself | medium-strong |
| L095 `غ ف ر B002` | forgiveness of sin/protection from effect | E: `توب B003`, `ربب B001`, `كون B001` -> CSU-08 | C: `إنه كان توابا`; K: sin not specified | medium-strong |
| L096 `غ ف ر B003` | fuzz/hair covering surface | E: none | K: no cloth/hair/surface | unlikely |
| L097 `غ ف ر B004` | relapse of wound/illness | E: none; checked against `ج يء B006` | K: no illness; imperatival request to God | unlikely |
| L098 `غ ف ر B005` | wild-goat kid and mother | E: none | K: no animal/mother | unlikely |
| L099 `غ ف ر B006` | lunar mansion of three stars | E: none | K: no stars/time mansion | unlikely |
| L100 `غ ف ر B007` | sweet tree exudate | E: water/plant model weakly | K: no tree/sweet gum | unlikely |
| L101 `غ ف ر B008` | the whole crowd, none missing | E: `ناس`, `فوج B001`, `جاء B001` -> total-mass image | C: `أفواجا`; K: phrase not present; branch idiomatic | medium-weak |

### 110:3:8 كَانَ — `ك و ن`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L102 `ك و ن B001` | occurrence/being in time | E: predicate `توابا`, `غفر B002` -> stable closure | C: final explanatory clause; K: not generating whole surah alone | medium-strong |
| L103 `ك و ن B002` | place/status | E: `دين B001`, `فتح B001` weak status/place | K: `كان` is predicate carrier, not place noun | weak |
| L104 `ك و ن B003` | guarantee/care for someone | E: `ربب B001/B002`, `غفر B002` weak divine care | K: no kafala construction | weak |
| L105 `ك و ن B004` | subjection/humility | E: `دين B004`, `استغفره` humility fork | K: branch appears in استكانة, not local `كان` | weak |
| L106 `ك و ن B005` | old man saying "I used to" | E: none | K: no age/reminiscence | unlikely |
| L107 `ك و ن B006` | bad state | E: none; rival to forgiveness | K: no bad-state predicate except the need for forgiveness | unlikely |

### 110:3:9 تَوَّابًا — `ت و ب`

| Seed | Initial image | Selected expansion / freeze | C/K after freeze | Grade |
| --- | --- | --- | --- | --- |
| L108 `ت و ب B003` | inviting/offering return from wrongdoing | E: `غفر B002`, `سبح B002`, `ربب B001`, `كون B001` -> CSU-08 | C: closing predicate of `كان`; K: furuq TSV contains only this accepted branch for root | medium-strong |

## Constructional and temporal seed passes

| Construction seed | Model | Corroborators / constraints | Grade |
| --- | --- | --- | --- |
| C001 `إِذَا جَاءَ ... فَسَبِّحْ` | condition fulfilled -> commanded response | C: `فـ`; K: response starts only after both arrival and sight sequence | strong |
| C002 `جاء نصر الله والفتح` | arriving subject is divine aid plus opening | C: `نصر` nominative subject, `فتح` coordinated; K: addressee does not bring victory | strong |
| C003 `نصر الله` / `دين الله` repeated idafa | source and field both divine | C: `ربك`, `استغفره`; K: divine name not merely decorative | strong |
| C004 `ورأيت الناس` | addressee as witness of public fulfillment | C: direct object + hal clause; K: not a private dream | medium-strong |
| C005 `يدخلون في دين الله أفواجا` | opened threshold receives groups into obedience field | C: `في`, `أفواجا`; K: abstract field, not building | strong |
| C006 `فسبح بحمد ربك` | response is praise with divine attribution | C: `بحمد` complement; `ربك`; K: not self-congratulation | strong |
| C007 `واستغفره` | response includes covering/forgiveness | C: object suffix continues divine referent; K: sin unspecified | medium-strong |
| C008 `إنه كان توابا` | closure explains request by stable divine return/acceptance | C: `كان` + accusative predicate; K: not new event sequence | medium-strong |
| C009 ayah boundary 1 -> 2 | event announced, then seen | C: 110:2 visually confirms 110:1 | medium-strong |
| C010 ayah boundary 2 -> 3 | public sign triggers private liturgical humility | C: `فـ`, imperatives | strong |
| C011 sound/repetition `الله ... الله ... ربك ... ـه` | referent continuity | C: divine object of praise and forgiveness; K: `ربك` personalizes without changing referent | strong |
| C012 entrance/return loop `دخل` -> `توب` | groups enter; addressee returns/turns through praise and forgiveness | C: `استغفره`, `توابا`; K: return is secondary, not lexical translation of entry | medium |

## Multi-seed convergence

| Convergent image | Lexical seeds supporting it | Constructional supports | Status |
| --- | --- | --- | --- |
| Arrival-opening-entry-response | `ج يء B001`, `نصر B001`, `فتح B001/B004`, `دخل B001`, `دين B001`, `فوج B001`, `سبح B001/B002`, `حمد B001`, `غفر B002`, `توب B003` | C001-C008 | primary, strong |
| Divine attribution circuit | `ءله B002`, `ربب B001`, `حمد B001`, `سبح B002`, `غفر B002` | repeated idafa + object suffix | primary, strong |
| Water/channel relief simulation | `نصر B004/B007`, `فتح B005`, `ج يء B003`, `ربب B008/B013`, `فوج B002`, weak `دخل B007` | opening + entering + cohorts | secondary, medium |
| Judgment/settlement simulation | `فتح B003`, `دين B002`, `رأي B002`, `كون B001`, `توب B003` | final `كان توابا` predicate | secondary, medium |
| Negative hidden-entry rival | `دخل B003/B004/B005`, `رأي B005`, weak `دين B004` | none decisive | terminated/unlikely |

## Exhaustiveness check after file creation

- Lexical seed count expected from S110 occurrence × accepted branch inventory: 108.
- Lexical seed rows recorded above: L001-L108.
- Constructional/temporal seed rows recorded above: C001-C012.
- Every S110 rooted occurrence appears at least once in the ledger.
- Every accepted branch listed in the inventory appears in the ledger.
- Basmala used only as opening context; no basmala seed initiated.
- Generated/constituent evidence (`E`) is separated from corroboration/constraint (`C/K`) in candidate packets and summarized in the ledger.
- Potential image packets retained: primary threshold-entry-response, divine attribution circuit, water/channel relief, judgment/settlement, and terminated negative hidden-entry rival.
