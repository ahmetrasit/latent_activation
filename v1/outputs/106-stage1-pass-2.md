# S106 Stage 1 Pass 2: Temporally Conditioned Reactivation

Assigned passage: S106  
Sacred Arabic text source: `resources/quran/surah_106.json`  
Prompt: `v1/prompts/stage1.md`

## Resource Note and Root Cause of Pass 1 Limitation

The root cause of the limited Pass 1 sweep was compression, not evidence: I grouped many branches under a few promising image families instead of explicitly restarting from every eligible branch and construction. A second practical constraint also affected the sweep: the mandated files `resources/qac.sqlite` and `resources/furuq_v4.sqlite` are present in this checkout as zero-byte files, so schema inspection and SQL row queries return no usable data.

For this Pass 2 recovery, I restarted from the first rooted word and used the available TSV mirrors under `resources/` for the same resource families:

- `resources/qac_root_ayah.tsv` for rooted occurrence, surface, lemma, POS, measure, and sequence rows.
- `resources/v4_branches.tsv` for branch dossiers, restricted to S106 roots.
- `resources/attachments.tsv` for attachment rows restricted to S106.
- `resources/quran/surah_106.json` for sacred Arabic text.

This recovery-source substitution is a constraint on auditability. No translation is used as evidence. The QAC TSV did not list `قُرَيْشٍ`, but `attachments.tsv` identifies it with root `ق ر ش`, and `v4_branches.tsv` supplies an accepted `ق ر ش` dossier. Because it is a rooted sacred-text word, it is included as an eligible lexical seed and this provenance caveat is recorded.

## Sacred Text and Rooted Sequence

```text
106:0 بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
106:1 لِإِيلَٰفِ قُرَيْشٍ
106:2 إِۦلَٰفِهِمْ رِحْلَةَ ٱلشِّتَآءِ وَٱلصَّيْفِ
106:3 فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ
106:4 ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ
```

Rooted passage words from the recovery row sources:

| Occurrence | Root | Surface | Lemma/POS/measure |
| --- | --- | --- | --- |
| 106:1:1 | ء ل ف | إِيلَٰفِ | إِلَٰف, N, IV |
| 106:1:2 | ق ر ش | قُرَيْشٍ | proper noun, attachment-derived root |
| 106:2:1 | ء ل ف | إِۦلَٰفِ | إِلَٰف, N, IV |
| 106:2:2 | ر ح ل | رِحْلَةَ | رِحْلَة, N |
| 106:2:3 | ش ت و | ٱلشِّتَآءِ | شِتَاء, N |
| 106:2:5 | ص ي ف | ٱلصَّيْفِ | صَيْف, N |
| 106:3:3 | ع ب د | يَعْبُدُوا۟ | عَبَدَ, V |
| 106:3:4 | ر ب ب | رَبَّ | رَبّ, N |
| 106:3:6 | ب ي ت | ٱلْبَيْتِ | بَيْت, N |
| 106:4:2 | ط ع م | أَطْعَمَهُم | أَطْعَمَ, V, IV |
| 106:4:4 | ج و ع | جُوعٍ | جُوع, N |
| 106:4:6 | ء م ن | ءَامَنَهُم | ءَامَنَ, V, IV |
| 106:4:8 | خ و ف | خَوْفٍ | خَوْف, N |

Opening basmala is recitational opening context only. Its roots `س م و`, `ء ل ه`, and `ر ح م` are not initiated as seeds. They may corroborate naming, divinity, and mercy when a candidate independently predicts those roles.

## Attachment Evidence Used

- `(C/K: 106:1 a1)` `قُرَيْشٍ` is the genitive mudaf ilayh of `إِيلَٰفِ`.
- `(C: 106:2 a1)` suffix `هِمْ` is the possessive dependent of `إِيلَٰفِ`.
- `(C: 106:2 a2)` `رِحْلَةَ` is accusative as object of the verbal noun `إِيلَٰفِهِمْ`.
- `(C: 106:2 a3)` `ٱلشِّتَاءِ` is genitive mudaf ilayh of `رِحْلَةَ`.
- `(C: 106:2 a4)` `وَٱلصَّيْفِ` is coordinated with `ٱلشِّتَاءِ` in the same genitive construction.
- `(C: 106:3 a1)` lam al-amr governs `يَعْبُدُوا۟`.
- `(C: 106:3 a2)` `رَبَّ` is the direct object of `يَعْبُدُوا۟`.
- `(C: 106:3 a3)` `هَٰذَا` completes the construct `رَبَّ هَٰذَا`.
- `(C: 106:3 a4)` `ٱلْبَيْتِ` identifies the demonstrative by apposition.
- `(C: 106:4 a1/a5)` `ٱلَّذِى` is the subject of both relative predicates `أَطْعَمَهُم` and `ءَامَنَهُم`.
- `(C: 106:4 a2/a6)` the suffix `هُم` is the object of both verbs.
- `(C: 106:4 a3)` `جُوعٍ` is governed by `مِّن` as complement of `أَطْعَمَهُم`.
- `(C: 106:4 a4)` `ءَامَنَهُم` is coordinated with `أَطْعَمَهُم`.
- `(C: 106:4 a7)` `خَوْفٍ` is governed by `مِنْ` as complement of `ءَامَنَهُم`.

## Branch Dossier Index

Accepted branches by root:

- `ء ل ف`: B001 number one thousand/bringing to a thousand; B002 joining, composing, ordering parts; B005 familiarity, attachment, dwelling with; B006 letter alif.
- `ق ر ش`: B001 gathering and joining from directions; B002 Quraysh as tribal name and nisbah; B003 severe/famine year gathering people and livestock; B004 acquiring bit by bit; B005 dominant sea creature; B006 interlacing spears in war; B007 slander/incitement; B008 wound cracking bone without crushing; B009 intrusive hanger-on.
- `ر ح ل`: B001 departure in travel; B002 saddle/load apparatus on camel; B003 saddling; B004 dwelling/equipment of a person; B005 travel-worthy mount; B006 stage between journeys; B007 removal from place; B008 travel assistance or giving a mount; B009 riding with harm; B010 patterned cloth with saddle images; B011 white saddle-place on animal; B012 abusive kinayah.
- `ش ت و`: B001 winter time; B002 entering or dwelling in winter/winter place; B003 winter rain; B004 winter as famine/scarcity; B005 rough place or valley head.
- `ص ي ف`: B001 summer time; B002 summer rain and its growth; B003 summer dwelling/trade/raid/provisioning; B004 child born in old age; B005 swerving/diversion; B006 proverb of neglected need in summer.
- `ع ب د`: B001 slave/owned person; B003 worship and submissive obedience; B004 enslaving/subduing; B005 tamed/smoothed road or treated animal/ship; B006 honored/served person; B007 strength/solidity; B008 pride/anger/grief; B009 little delay or swift run; B010 dispersed groups/ways; B011 mount failure or difficult beast; B012 perfume grinding stone.
- `ر ب ب`: B001 lordship, ownership, mastery; B002 repairing, nurturing, completing; B003 rabbinic knowledge; B004 large groups; B005 stepchild/caretaker relation; B006 thick syrup/repairing with it; B007 abiding, staying, lasting; B008 cloud mass; B009 recent birth/freshness; B010 leather container for arrows; B011 covenant/neighboring pact; B012 green plant; B013 abundant/sweet water; B014 herd; B015 particle `rubba`; B016 need/knot/blessing; B017 chief of sailors.
- `ب ي ت`: B001 shelter, dwelling, night-place; B002 household/family; B003 verse of poetry; B004 night action/planning/raid; B005 food sufficient for a night; B006 liquid/thing kept overnight; B007 grave as house; B008 house of honor/tribal prestige; B010 marriage/house-building.
- `ط ع م`: B001 tasting/eating; B002 feeding another and asking for food; B004 livelihood, provision, good condition; B005 fruit ripening; B006 hunting instrument that feeds its owner; B007 animal fatness; B008 reason/value; B009 horse mouth/jowl and asking it to run; B010 graft accepting a joined branch; B011 ability; B012 gripping throat in choking; B013 mouth-to-mouth contact; B014 continuity of form.
- `ج و ع`: B001 empty belly/hunger; B002 famine time; B003 causing or intending hunger; B004 metaphorical emptiness/thinness.
- `ء م ن`: B001 heart stillness in security and trust; B002 confirming assent that settles the heart; B003 saying amin seeking response.
- `خ و ف`: B001 fear/terror expecting harm; B002 making another afraid; B003 overcoming in fear; B004 taking away or diminishing; B005 visible appearance of fear; B006 leather bag of honey/water carrier.

Total accepted lexical seed units: 103 occurrence-seeds. This counts `ء ل ف` separately at 106:1 and 106:2. Constructional, morphosyntactic, temporal, and opening-context seeds are listed after the lexical seed ledger.

## Candidate Synthesis Units

### S106-S1-001: Familiarized Gathering Stabilized Around the House

- `candidate_id`: S106-S1-001
- `ayah_range`: 106:1-4
- `seed_type`: lexical and verified composite
- `seed`: 106:1 `لِإِيلَٰفِ`, especially `ء ل ف B005` and `ء ل ف B002`, with 106:1 `قُرَيْشٍ` `ق ر ش B001/B002`
- `generating_set`: `(E: ء ل ف B005 familiarity, attachment, dwelling-with)`, `(E: ء ل ف B002 joining/composing ordered parts)`, `(E: ق ر ش B001 gathering from directions)`, `(E: ق ر ش B002 Quraysh as named gathered group)`, `(E: 106:1 a1 idafa إيلَاف قريش)`
- `selected_branches`: `ء ل ف B002/B005`; `ق ر ش B001/B002`; `ر ح ل B001`; `ش ت و B001`; `ص ي ف B001`; `ع ب د B003`; `ر ب ب B001/B002`; `ب ي ت B001/B008`; `ط ع م B002`; `ج و ع B001/B002`; `ء م ن B001`; `خ و ف B001`
- `constructed_model`: The opening names a social condition before it gives a command: Quraysh are gathered and made accustomed or attached. The repeated `إيلَافهم` then reactivates that condition as a patterned travel circuit across winter and summer. The command to worship the Lord of this House identifies the stabilizing center of the circuit, and the final relative clause supplies the reason that the attachment is not merely social habit: the Lord who centers the House has fed them from hunger and secured them from fear.
- `freeze_point`: After 106:1-2, when `إيلَاف` has occurred twice and `رحلة الشتاء والصيف` has specified a repeated seasonal travel circuit, before the worship command and the relative clause.
- `predictions_at_freeze`: an anchoring center; a beneficiary group; a reason the seasonal circuit is stable; protection from travel-related lack and danger; an obligation or response to the stabilizer.
- `unused_features_tested`: `فليعبدوا`, `رب هذا البيت`, `الذي`, `أطعمهم من جوع`, `آمنهم من خوف`, attachments in 106:3-4, basmala opening-context.
- `corroborators`: `(C: ر ح ل B001 travel/departure)`, `(C: ش ت و B001 winter)`, `(C: ص ي ف B001 summer)`, `(C: ع ب د B003 worship/submissive obedience)`, `(C: ر ب ب B001 lord/owner/master)`, `(C: ر ب ب B002 nurturing/completing)`, `(C: ب ي ت B001 shelter/dwelling)`, `(C: ب ي ت B008 house of tribal honor)`, `(C: ط ع م B002 feeding another)`, `(C: ج و ع B001 hunger)`, `(C: ج و ع B002 famine time)`, `(C: ء م ن B001 security against fear)`, `(C: خ و ف B001 fear expecting harm)`, `(C: repeated إيلَاف 106:1->106:2)`, `(C: 106:4 paired من جوع / من خوف)`.
- `constraints`: `(K: قريش is a proper-noun occurrence; branch B001 gathering supports the name but does not replace it)`, `(K: لِإيلَاف can signal reason/purpose, but the passage does not state an explicit causal particle beyond lām)`, `(K: no explicit trade goods are named; travel and provisioning are enough, commerce remains secondary)`.
- `temporal_reactivation_notes`: The first `إيلَاف` leaves an incomplete relational field. `قريش` fills the group role. The second `إيلَافهم` reactivates the first and transfers the attachment from group identity into a repeated journey. `فليعبدوا` then converts the stabilized habit into obligation. The final hunger/fear pair reactivates seasonal travel as vulnerable movement that has been made livable.
- `rival_models`: Pure tribal-name reading; pure trade-route reading; generic gratitude reading. Each is locally valid but explains less of the repeated lexical activation from gathering/familiarization to seasonal circuit to House-centered obligation.
- `grade`: strong
- `grade_rationale`: The same root recurs at the start, the named group has an independent gathering branch, the journey and seasonal terms complete the model, and the final pair of feeding/security independently predicts why familiarized travel requires a House-centered response.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` S106 rows; `attachments.tsv` S106 rows a1-a17; `v4_branches.tsv` roots `ء ل ف`, `ق ر ش`, `ر ح ل`, `ش ت و`, `ص ي ف`, `ع ب د`, `ر ب ب`, `ب ي ت`, `ط ع م`, `ج و ع`, `ء م ن`, `خ و ف`.

### S106-S1-002: Seasonal Travel Apparatus and Protected Caravan Circuit

- `candidate_id`: S106-S1-002
- `ayah_range`: 106:2-4
- `seed_type`: lexical
- `seed`: 106:2 `رِحْلَةَ`, especially `ر ح ل B001/B002/B003/B005/B006/B008`
- `generating_set`: `(E: ر ح ل B001 departure in travel)`, `(E: ر ح ل B002 camel saddle/load apparatus)`, `(E: ر ح ل B003 saddling)`, `(E: ر ح ل B005 travel-worthy mount)`, `(E: ر ح ل B006 stage between journeys)`, `(E: 106:2 a2 رحلة object of إيلَافهم)`
- `selected_branches`: `ر ح ل B001/B002/B003/B005/B006/B008`; `ش ت و B001/B002/B004`; `ص ي ف B001/B003`; `ط ع م B002/B004`; `ج و ع B001/B002`; `ء م ن B001`; `خ و ف B001`; `ر ب ب B001/B002`; `ب ي ت B001`
- `constructed_model`: The journey is not an abstract motion. The root dossier activates travel, gear, a fit mount, stages, and assistance. Winter and summer make the circuit cyclical. A circuit with mounts and stages predicts two practical vulnerabilities: provision and safety. Verse 4 then supplies both as divine acts: feeding from hunger and securing from fear.
- `freeze_point`: After `إيلَافهم رحلة الشتاء والصيف` is built as an organized seasonal travel circuit, before 106:3-4.
- `predictions_at_freeze`: provisioning across stages; protection from road danger; a stable home or House to return to; a patron or Lord who maintains the circuit.
- `unused_features_tested`: `رب هذا البيت`, `أطعمهم`, `من جوع`, `آمنهم`, `من خوف`, Quraysh attachment.
- `corroborators`: `(C: ش ت و B001/B002 winter time/place)`, `(C: ش ت و B004 winter scarcity/famine)`, `(C: ص ي ف B001 summer time)`, `(C: ص ي ف B003 summer provisioning/trade/raid/mirah)`, `(C: ط ع م B002 feeding)`, `(C: ط ع م B004 livelihood/provision)`, `(C: ج و ع B001 empty belly)`, `(C: ء م ن B001 security)`, `(C: خ و ف B001 feared harm)`, `(C: ب ي ت B001 shelter/return point)`.
- `constraints`: `(K: no explicit camel, saddle, or mount noun appears in the sacred text; ر ح ل B002/B003/B005 are secondary apparatus imagery)`, `(K: travel is grammatically object of إيلَافهم, so the primary assertion is their familiarized journey rather than the equipment itself)`.
- `temporal_reactivation_notes`: The phrase `رحلة الشتاء والصيف` creates a forward expectation for what makes such movement possible. The final `أطعمهم... وآمنهم...` retrospectively fills the two expected travel supports: food and safety.
- `rival_models`: Static seasonal calendar model; pure commercial itinerary model. The protected-caravan model has broader lexical support but must keep gear imagery secondary.
- `grade`: medium-strong
- `grade_rationale`: The journey branch is direct and the final provision/security pair strongly corroborates travel vulnerability. Apparatus details remain remote because the text does not name mounts or gear.
- `source_queries_or_rows_used`: `ر ح ل B001-B012`; `ش ت و B001-B005`; `ص ي ف B001-B006`; attachment rows 106:2 a1-a4 and 106:4 a1-a7.

### S106-S1-003: The Lord of This House as Shelter, Owner, and Nurturer

- `candidate_id`: S106-S1-003
- `ayah_range`: 106:3-4
- `seed_type`: lexical/constructional
- `seed`: 106:3 `رَبَّ هَٰذَا ٱلْبَيْتِ`
- `generating_set`: `(E: ر ب ب B001 lordship, ownership, mastery)`, `(E: ر ب ب B002 nurturing, repairing, completing)`, `(E: ب ي ت B001 shelter/dwelling/night-place)`, `(E: 106:3 a2 رب object of يعبدوا)`, `(E: 106:3 a4 البيت apposition to هذا)`
- `selected_branches`: `ر ب ب B001/B002/B007`; `ب ي ت B001/B002/B008`; `ع ب د B003`; `ط ع م B002`; `ج و ع B001`; `ء م ن B001`; `خ و ف B001`
- `constructed_model`: The command is centered not on a general divine title alone but on `the Lord of this House`. `رب` supplies ownership and care; `بيت` supplies shelter, household gathering, and honor. The following relative clause then proves the title in functional terms: this Lord has nourished and secured the group.
- `freeze_point`: After `فليعبدوا رب هذا البيت`, before the relative clause in 106:4.
- `predictions_at_freeze`: acts fitting lordship and nurture; shelter against threat; provision for dependents; a reason worship is owed.
- `unused_features_tested`: `الذي أطعمهم من جوع وآمنهم من خوف`, preceding `إيلَاف`, seasonal travel.
- `corroborators`: `(C: ط ع م B002 feeding another)`, `(C: ج و ع B001 hunger as need)`, `(C: ء م ن B001 security)`, `(C: خ و ف B001 fear as opposed state)`, `(C: ب ي ت B008 house of honor, locally plausible for Quraysh)`, `(C: ر ب ب B007 abiding/lasting as House-centered stability)`, `(C: basmala opening-context ء ل ه divinity)`, `(C: basmala opening-context ر ح م mercy/nurture, corroborative only)`.
- `constraints`: `(K: بيت B002 household is secondary; the local phrase points to this specific House, not a family household)`, `(K: رب B004 large groups and B014 herd do not define the local title)`, `(K: no architectural detail is supplied beyond house-identification)`.
- `temporal_reactivation_notes`: The House arrives after travel and seasons, so it retroactively becomes the stable center that explains how the repeated circuit is anchored. The final relative clause then reactivates `رب` as active care, not only possession.
- `rival_models`: House as mere landmark; Lord as abstract owner only. The feeding/security pair favors owner plus nurturer/protector.
- `grade`: strong
- `grade_rationale`: Direct constructional attachment and direct branch support from `رب` and `بيت`, then independently verified by the two divine acts in verse 4.
- `source_queries_or_rows_used`: `ر ب ب B001-B017`; `ب ي ت B001-B010`; attachment rows 106:3 a1-a4, 106:4 a1-a7.

### S106-S1-004: Twin Removal of Lack and Threat

- `candidate_id`: S106-S1-004
- `ayah_range`: 106:4 with backward reactivation of 106:1-3
- `seed_type`: lexical/constructional
- `seed`: 106:4 `أَطْعَمَهُم مِّن جُوعٍ وَءَامَنَهُم مِّنْ خَوْفٍ`
- `generating_set`: `(E: ط ع م B002 feeding another)`, `(E: ج و ع B001 empty belly/hunger)`, `(E: ء م ن B001 heart stillness in security)`, `(E: خ و ف B001 fear expecting harm)`, `(E: 106:4 a3/a7 min-complements marking relief from source-state)`
- `selected_branches`: `ط ع م B001/B002/B004`; `ج و ع B001/B002`; `ء م ن B001`; `خ و ف B001/B002/B005`; `ر ح ل B001`; `ش ت و B004`; `ص ي ف B003`; `ر ب ب B002`
- `constructed_model`: Verse 4 closes with a two-part relief structure. Hunger and fear are the two negative states; feeding and securing are the two answering acts. Once heard, the closure reactivates the earlier seasonal journey as exposure to need and danger, and the command to worship as response to the one who removed both.
- `freeze_point`: After the first half `أطعمهم من جوع`, before the coordinated `وآمنهم من خوف`.
- `predictions_at_freeze`: a parallel second relief act; a second negative state; a subject who supplies both material and affective/social security.
- `unused_features_tested`: `وآمنهم من خوف`, the coordinated structure, prior `رحلة الشتاء والصيف`, `رب هذا البيت`.
- `corroborators`: `(C: ء م ن B001 security against fear)`, `(C: خ و ف B001 exact opposing state)`, `(C: 106:4 a4 coordination of two relative predicates)`, `(C: ر ح ل B001 travel vulnerability)`, `(C: ش ت و B004 famine/scarcity)`, `(C: ص ي ف B003 seasonal provisioning)`, `(C: ر ب ب B002 nurture/completion)`.
- `constraints`: `(K: ط ع م B001 tasting/eating is broader than the local Form IV feeding; B002 is the exact local branch)`, `(K: ء م ن B002 inner faith is not the local sense of آمنهم here; the object suffix and من خوف favor giving security)`, `(K: خوف B002 making others afraid is constrained by passive-relief context; they are secured from fear, not made fearsome)`.
- `temporal_reactivation_notes`: The passage closes only after the second relief act. `من خوف` retroactively balances `من جوع`, and both retroactively justify `فليعبدوا`: worship responds to comprehensive care, not to one isolated benefit.
- `rival_models`: Food-only gratitude model; safety-only model. The parallel syntax requires the paired lack/threat model.
- `grade`: strong
- `grade_rationale`: Exact lexical opposition of security and fear, exact feeding/hunger pairing, and high structural symmetry.
- `source_queries_or_rows_used`: `ط ع م B001-B014`; `ج و ع B001-B004`; `ء م ن B001-B003`; `خ و ف B001-B006`; attachment rows 106:4 a1-a7.

### S106-S1-005: Seasonal Scarcity and Provisioning

- `candidate_id`: S106-S1-005
- `ayah_range`: 106:2-4
- `seed_type`: lexical
- `seed`: 106:2 `ٱلشِّتَاءِ وَٱلصَّيْفِ`
- `generating_set`: `(E: ش ت و B001 winter time)`, `(E: ش ت و B004 winter as famine/scarcity)`, `(E: ص ي ف B001 summer time)`, `(E: ص ي ف B003 summer dwelling/trade/provisioning)`, `(E: 106:2 a4 winter/summer coordination)`
- `selected_branches`: `ش ت و B001/B002/B004`; `ص ي ف B001/B002/B003/B005`; `ر ح ل B001`; `ط ع م B002/B004`; `ج و ع B001/B002`; `ء م ن B001`; `خ و ف B001`
- `constructed_model`: The paired seasons are more than a calendar span. Winter can carry scarcity and famine; summer can carry provisioning, travel, rain, and seasonal dwelling. The journey across both seasons predicts exposure to hunger and fear, and verse 4 answers those exposures.
- `freeze_point`: After the coordinated seasonal pair is attached to `رحلة`, before verse 3.
- `predictions_at_freeze`: food scarcity or supply will matter; safety across seasonal movement will matter; the circuit should be explained by a stable source of care.
- `unused_features_tested`: `أطعمهم من جوع`, `آمنهم من خوف`, `رب هذا البيت`.
- `corroborators`: `(C: ج و ع B002 famine time)`, `(C: ط ع م B004 livelihood/provision)`, `(C: ط ع م B002 feeding)`, `(C: ر ب ب B002 nurture)`, `(C: ء م ن B001 security)`, `(C: خ و ف B001 fear)`.
- `constraints`: `(K: ش ت و B003 winter rain and ص ي ف B002 summer rain/growth have no explicit rain/plant lexeme in S106)`, `(K: ص ي ف B005 swerving is not supported by the coordinated season construction)`.
- `temporal_reactivation_notes`: The final hunger phrase makes the winter-famine branch more salient after the fact; the fear phrase makes the travel-across-seasons more than simple calendar notation.
- `rival_models`: Simple merism for all-year continuity. That model is strong but less imagistic; the scarcity/provision model is a controlled secondary simulation.
- `grade`: medium-strong
- `grade_rationale`: Seasonal branches and final hunger/security strongly align, but rain/growth details remain unfilled.
- `source_queries_or_rows_used`: `ش ت و B001-B005`; `ص ي ف B001-B006`; attachment rows 106:2 a3-a4.

### S106-S1-006: Acquiring and Composing a Livelihood Bit by Bit

- `candidate_id`: S106-S1-006
- `ayah_range`: 106:1-4
- `seed_type`: lexical
- `seed`: 106:1 `قُرَيْشٍ`, especially `ق ر ش B004`, with `ء ل ف B002`
- `generating_set`: `(E: ق ر ش B004 acquiring/taking bit by bit)`, `(E: ء ل ف B002 joining/composing ordered parts)`, `(E: ر ح ل B001 travel)`, `(E: ص ي ف B003 seasonal provisioning/mirah)`
- `selected_branches`: `ق ر ش B004`; `ء ل ف B002`; `ر ح ل B001/B006`; `ص ي ف B003`; `ط ع م B004`; `ج و ع B001`; `ر ب ب B001/B002`; `ب ي ت B008`
- `constructed_model`: A secondary economic image emerges: a named group associated lexically with acquiring/gathering obtains livelihood through an ordered travel circuit. The House and its Lord function as the honored center that makes this acquisition livable rather than precarious.
- `freeze_point`: After Quraysh + repeated `إيلَاف` + seasonal journey construct a gathered/acquisitive travel scene.
- `predictions_at_freeze`: livelihood or provision; protection from scarcity; a central owner/patron; group honor.
- `unused_features_tested`: `أطعمهم من جوع`, `آمنهم من خوف`, `رب هذا البيت`.
- `corroborators`: `(C: ط ع م B004 livelihood/provision/good condition)`, `(C: ط ع م B002 feeding)`, `(C: ج و ع B001 hunger as avoided lack)`, `(C: ب ي ت B008 house of tribal honor)`, `(C: ر ب ب B001 owner/master)`.
- `constraints`: `(K: no explicit buying/selling/profit vocabulary)`, `(K: ق ر ش B004 is secondary to the proper-name branch B002 in local context)`, `(K: ص ي ف B003 includes seasonal trade/provisioning but the text itself says journey, not market)`.
- `temporal_reactivation_notes`: The feeding clause at the end reactivates acquisition branches as provision received rather than merely earned.
- `rival_models`: Direct familiarization/gathering model S106-S1-001 is stronger because it uses the repeated `إيلَاف` more directly.
- `grade`: medium
- `grade_rationale`: Several branches converge on gathering/acquisition/provision, but the passage withholds explicit commercial mechanisms.
- `source_queries_or_rows_used`: `ق ر ش B001-B009`; `ء ل ف B001-B006`; `ط ع م B004`; attachment rows 106:1 a1 and 106:2 a1-a4.

### S106-S1-007: Worship as the Correct Response to Care

- `candidate_id`: S106-S1-007
- `ayah_range`: 106:3-4
- `seed_type`: lexical/morphosyntactic
- `seed`: 106:3 `فَلْيَعْبُدُوا۟`, especially `ع ب د B003`
- `generating_set`: `(E: ع ب د B003 worship and submissive obedience)`, `(E: 106:3 a1 lam al-amr governing يعبدوا)`, `(E: 106:3 a2 رب as direct object)`, `(E: ر ب ب B001 lordship/mastery)`
- `selected_branches`: `ع ب د B003`; `ر ب ب B001/B002`; `ب ي ت B001/B008`; `ط ع م B002`; `ء م ن B001`; `ج و ع B001`; `خ و ف B001`
- `constructed_model`: The imperative does not appear at the beginning; it arrives after the listener has heard familiarization, Quraysh, journey, and seasons. The command then directs the gathered group toward submissive worship of the Lord of the House. Verse 4 supplies the reason in acts of care.
- `freeze_point`: After `فليعبدوا رب هذا البيت`, before the relative clause.
- `predictions_at_freeze`: the object of worship should be shown as lord/caretaker; preceding benefits should be morally transformed into obligation; the House should be more than geography.
- `unused_features_tested`: `الذي أطعمهم من جوع وآمنهم من خوف`, prior `إيلَاف`.
- `corroborators`: `(C: ر ب ب B001 owner/master)`, `(C: ر ب ب B002 nurturer/completer)`, `(C: ط ع م B002 feeding)`, `(C: ء م ن B001 giving security)`, `(C: basmala opening-context ء ل ه worshiped deity)`, `(C: sequence benefit -> command -> reason)`.
- `constraints`: `(K: ع ب د B001 slavery/ownership is only a background dimension; local `يعبدوا` is worship, not human enslavement)`, `(K: ع ب د B004 subduing and B005 road-taming do not supply the primary imperative sense)`.
- `temporal_reactivation_notes`: The `فـ` and lam al-amr turn previous stabilization into command. The later relative clause reactivates `رب` as the source of benefits and confirms why worship closes the first movement of the surah.
- `rival_models`: Gratitude-only model without submissive worship; servitude-only model. The local verb and object favor worshipful obedience grounded in care.
- `grade`: strong
- `grade_rationale`: Exact local branch and syntax, plus direct corroboration from `رب` and the two benefits.
- `source_queries_or_rows_used`: `ع ب د B001-B012`; attachment rows 106:3 a1-a4 and 106:4 a1-a7.

### S106-S1-008: Fear Routed Into Security

- `candidate_id`: S106-S1-008
- `ayah_range`: 106:2-4
- `seed_type`: lexical
- `seed`: 106:4 `خَوْفٍ`, with `خ و ف B001/B002/B005` and `ء م ن B001`
- `generating_set`: `(E: خ و ف B001 fear expecting harm)`, `(E: خ و ف B005 visible fear)`, `(E: ء م ن B001 security against fear)`, `(E: 106:4 a7 من خوف complement)`
- `selected_branches`: `خ و ف B001/B002/B005`; `ء م ن B001`; `ر ح ل B001`; `ر ح ل B007/B009`; `ق ر ش B006/B007`; `ع ب د B003`; `ر ب ب B001`
- `constructed_model`: The closing fear term replays the journey as dangerous exposure. Security is not merely inner calm; the object pronoun and `من خوف` mark a transition from fear-state to secured state. Remote hostile branches from Quraysh and travel can generate rival threat-images, but local syntax keeps them subordinate.
- `freeze_point`: After `آمنهم من خوف`, then tested backward against journey and group roots.
- `predictions_at_freeze`: travel danger; a protector; possible hostile social or road conditions; no need for explicit battle if fear is general.
- `unused_features_tested`: `رحلة الشتاء والصيف`, `قريش`, `رب هذا البيت`, `أطعمهم من جوع`.
- `corroborators`: `(C: ر ح ل B001 travel)`, `(C: ر ح ل B007 removal/displacement as weak travel-risk)`, `(C: ر ح ل B009 riding with harm as remote road-harm image)`, `(C: ر ب ب B001 master/protector)`, `(C: ب ي ت B001 shelter)`.
- `constraints`: `(K: ق ر ش B006 interlacing spears and B007 incitement are not selected as primary because the passage names no conflict)`, `(K: خوف B002 making others afraid is constrained by `آمنهم`; the group is recipient of security, not source of fear)`, `(K: no enemy noun appears)`.
- `temporal_reactivation_notes`: The final word `خوف` closes the surah by naming the affective danger that seasonal movement had left implicit. It also reactivates `البيت` as shelter and `رب` as protector.
- `rival_models`: Explicit battle model; social incitement model. Both are weak because no combat or slander syntax appears.
- `grade`: medium-strong
- `grade_rationale`: The fear/security pair is exact; backward travel-risk support is plausible but mostly implicit.
- `source_queries_or_rows_used`: `خ و ف B001-B006`; `ء م ن B001-B003`; `ر ح ل B001/B007/B009`; `ق ر ش B006/B007`.

### S106-S1-009: Night Shelter, Household Provision, and Stored Sustenance

- `candidate_id`: S106-S1-009
- `ayah_range`: 106:3-4
- `seed_type`: lexical
- `seed`: 106:3 `ٱلْبَيْتِ`, remote branches `ب ي ت B004/B005/B006`
- `generating_set`: `(E: ب ي ت B004 night action/planning)`, `(E: ب ي ت B005 food sufficient for a night)`, `(E: ب ي ت B006 liquid/food kept overnight)`, `(E: ط ع م B002 feeding)`, `(E: ج و ع B001 hunger)`
- `selected_branches`: `ب ي ت B004/B005/B006`; `ط ع م B002`; `ج و ع B001`; `ء م ن B001`; `خ و ف B001`; `ر ح ل B004/B006`
- `constructed_model`: A weak but locally suggestive image treats `بيت` as the place where night, shelter, and minimal provisions become salient. The final feeding-from-hunger phrase can make the House resonate as a site of sustenance, and security-from-fear makes it a shelter. Travel-stage branches add return/rest points.
- `freeze_point`: After remote `بيت` branches are connected with feeding/security in verse 4.
- `predictions_at_freeze`: night provision, shelter from fear, return from journey.
- `unused_features_tested`: `رحلة`, `رب`, `أطعم`, `آمن`.
- `corroborators`: `(C: ط ع م B002 feeding)`, `(C: ج و ع B001 hunger)`, `(C: ء م ن B001 security)`, `(C: ر ح ل B004 dwelling/equipment)`, `(C: ر ح ل B006 stage between journeys)`.
- `constraints`: `(K: local `البيت` is identified by demonstrative apposition and points to the known House, not generic night lodging)`, `(K: no night lexeme appears)`, `(K: B005/B006 are remote and cannot drive the primary reading)`.
- `temporal_reactivation_notes`: Verse 4 makes provision/shelter dimensions of `بيت` newly meaningful, but only as secondary resonance.
- `rival_models`: Primary House-as-sanctuary model S106-S1-003.
- `grade`: weak-medium
- `grade_rationale`: Some provision/shelter roles are filled, but the specific night/storage branches are not locally named.
- `source_queries_or_rows_used`: `ب ي ت B004/B005/B006`; `ط ع م B002`; `ر ح ل B004/B006`.

### S106-S1-010: Terminated Hostility, Predator, and Wound Cluster

- `candidate_id`: S106-S1-010
- `ayah_range`: 106:1-4
- `seed_type`: lexical
- `seed`: remote `ق ر ش B005/B006/B007/B008/B009` with hostile or intrusive imagery
- `generating_set`: `(E: ق ر ش B005 dominant sea creature)`, `(E: ق ر ش B006 interlacing spears)`, `(E: ق ر ش B007 incitement/slander)`, `(E: ق ر ش B008 bone-cracking wound)`, `(E: ق ر ش B009 intrusive hanger-on)`
- `selected_branches`: none retained as a primary model; weak tests used `خ و ف B001/B002`, `ء م ن B001`, `ر ح ل B009`, `ع ب د B008`
- `constructed_model`: These branches can generate danger images: predation, battle, slander, wound, or intrusion. The passage does close with fear and security, so they were tested. The image terminates because S106 never supplies sea, spear, wound, slander, enemy, or explicit combat roles.
- `freeze_point`: After hostile branch images are formed from `ق ر ش`, before testing the rest of the passage.
- `predictions_at_freeze`: enemy, weapon, wound, sea, slander, or intrusive actor.
- `unused_features_tested`: `رحلة`, `آمنهم من خوف`, `رب هذا البيت`, `أطعمهم من جوع`.
- `corroborators`: `(C: خ و ف B001 fear, only generic)`, `(C: ء م ن B001 security, only generic)`.
- `constraints`: `(K: no sea role for B005)`, `(K: no spear/war syntax for B006)`, `(K: no speech-slander role for B007)`, `(K: no wound/body role for B008)`, `(K: no hanger-on/social intrusion role for B009)`, `(K: قريش is locally the named group, not the threatening agent)`.
- `temporal_reactivation_notes`: Final `خوف` temporarily reactivates danger branches, but `آمنهم` resolves fear without specifying those mechanisms.
- `rival_models`: General protected-travel model S106-S1-002 and fear-security model S106-S1-008 absorb the valid fear dimension without hostile over-specification.
- `grade`: unlikely
- `grade_rationale`: Only generic fear/security matches; all specific branch roles are unfilled.
- `source_queries_or_rows_used`: `ق ر ش B005-B009`; `خ و ف B001/B002`; `ء م ن B001`; attachment rows 106:1 a1 and 106:4 a7.

## Exhaustive Lexical Seed Ledger

Format: `seed -> result`. `Selected model` points to the candidate above. `Terminated` means the branch was started, tested against all other passage-root dossiers and constructions, and did not form a passage-local image beyond weak association.

### 106:1 `إيلَاف` / `ء ل ف`

1. `ء ل ف B001` number one thousand/bringing to a thousand -> weak numeric-massing fork with `ق ر ش B001` gathering and `ر ب ب B004` large groups; no number or thousand role appears. Grade unlikely.
2. `ء ل ف B002` joining/composing ordered parts -> selected model S106-S1-001 and S106-S1-006. The repeated root and Quraysh gathering make ordered social composition productive. Grade strong.
3. `ء ل ف B005` familiarity/attachment/dwelling-with -> selected model S106-S1-001. Directly fits `إيلَاف` and predicts stabilized seasonal habit. Grade strong.
4. `ء ل ف B006` letter alif -> terminated. No orthographic or letter-name role.

### 106:1 `قريش` / `ق ر ش`

5. `ق ر ش B001` gathering/joining from directions -> selected model S106-S1-001. Converges with `ء ل ف B002/B005`. Grade strong.
6. `ق ر ش B002` Quraysh as tribal name -> selected model S106-S1-001. Primary proper-name fit. Grade strong.
7. `ق ر ش B003` severe/famine year gathering people/livestock -> support for S106-S1-005 through scarcity and final `جوع`; no explicit livestock. Grade medium.
8. `ق ر ش B004` acquiring bit by bit -> selected secondary economic model S106-S1-006. Grade medium.
9. `ق ر ش B005` dominant sea creature -> selected only as terminated branch in S106-S1-010. No sea/predator role. Grade unlikely.
10. `ق ر ش B006` interlacing spears in war -> terminated in S106-S1-010. Generic fear only; no war syntax. Grade unlikely.
11. `ق ر ش B007` slander/incitement -> terminated in S106-S1-010. No speech-hostility role. Grade unlikely.
12. `ق ر ش B008` bone-cracking wound -> terminated in S106-S1-010. No wound/body role. Grade unlikely.
13. `ق ر ش B009` intrusive hanger-on -> terminated in S106-S1-010. No intrusive third-party role. Grade unlikely.

### 106:2 `إيلَافهم` / `ء ل ف`

14. `ء ل ف B001` number one thousand/bringing to a thousand -> weak as above; possessive suffix gives group, not number. Grade unlikely.
15. `ء ل ف B002` joining/composing ordered parts -> selected S106-S1-001. At second occurrence it composes the seasonal journey with group habit. Grade strong.
16. `ء ل ف B005` familiarity/attachment/dwelling-with -> selected S106-S1-001/S106-S1-002. Strong because it governs `رحلة`. Grade strong.
17. `ء ل ف B006` letter alif -> terminated. No letter role.

### 106:2 `رحلة` / `ر ح ل`

18. `ر ح ل B001` departure in travel -> selected S106-S1-002 and corroborator for S106-S1-001. Grade strong.
19. `ر ح ل B002` saddle/load apparatus -> selected secondary apparatus in S106-S1-002; no explicit mount. Grade medium.
20. `ر ح ل B003` saddling -> selected secondary apparatus in S106-S1-002; no explicit saddling action. Grade weak-medium.
21. `ر ح ل B004` dwelling/equipment of a person -> support for S106-S1-009; travel-to-dwelling resonance. Grade weak-medium.
22. `ر ح ل B005` travel-worthy mount -> selected secondary support for S106-S1-002; no mount noun. Grade medium.
23. `ر ح ل B006` stage between journeys -> selected support for S106-S1-002/S106-S1-009; seasonal circuit implies stages. Grade medium.
24. `ر ح ل B007` removal/displacement from place -> weak support for travel-risk S106-S1-008; no forced expulsion. Grade weak.
25. `ر ح ل B008` travel assistance/giving a mount -> support for protected circuit S106-S1-002; no giver of mount named. Grade weak-medium.
26. `ر ح ل B009` riding with harm -> weak danger fork S106-S1-008/S106-S1-010; no harm event. Grade weak.
27. `ر ح ل B010` patterned cloth with saddle images -> terminated. No textile/pattern role.
28. `ر ح ل B011` white saddle-place on animal -> terminated. No animal-color role.
29. `ر ح ل B012` abusive kinayah -> terminated. No insult/kinship speech role.

### 106:2 `الشتاء` / `ش ت و`

30. `ش ت و B001` winter time -> selected S106-S1-005 and corroborator for S106-S1-001/S106-S1-002. Grade strong.
31. `ش ت و B002` entering/dwelling in winter or winter place -> support for seasonal circuit S106-S1-005; no winter-place named. Grade medium.
32. `ش ت و B003` winter rain -> weak ecological fork; no rain/water/plant term. Grade weak.
33. `ش ت و B004` winter as famine/scarcity -> selected S106-S1-005 and corroborates `من جوع`. Grade medium-strong.
34. `ش ت و B005` rough place/valley head -> terminated. No rough terrain or valley role.

### 106:2 `الصيف` / `ص ي ف`

35. `ص ي ف B001` summer time -> selected S106-S1-005 and corroborator for S106-S1-001/S106-S1-002. Grade strong.
36. `ص ي ف B002` summer rain/growth -> weak ecological fork with provision; no rain/plant role. Grade weak.
37. `ص ي ف B003` summer dwelling/trade/provisioning -> selected S106-S1-005/S106-S1-006; fits seasonal journey and provision. Grade medium-strong.
38. `ص ي ف B004` child of old age -> terminated. No birth/offspring role.
39. `ص ي ف B005` swerving/diversion -> weak route-diversion fork with travel and fear; no deviation marker. Grade weak.
40. `ص ي ف B006` proverb of neglected need in summer -> weak proverb resonance with need/provision; no proverb structure. Grade unlikely.

### 106:3 `يعبدوا` / `ع ب د`

41. `ع ب د B001` slave/owned person -> background support for dependency under `رب`; not primary. Grade weak-medium.
42. `ع ب د B003` worship/submissive obedience -> selected S106-S1-007. Exact local imperative. Grade strong.
43. `ع ب د B004` enslaving/subduing -> constrained. The command is to worship the Lord, not to enslave others. Grade unlikely.
44. `ع ب د B005` tamed/smoothed road or treated animal/ship -> weak with journey route; no road/ship noun. Grade weak.
45. `ع ب د B006` honored/served person -> support for worship object as honored Lord, but broad. Grade weak-medium.
46. `ع ب د B007` strength/solidity -> weak support for stable House/security; no strength noun. Grade weak.
47. `ع ب د B008` pride/anger/grief -> terminated. No anger/grief role.
48. `ع ب د B009` little delay/swift run -> weak travel motion only; no speed/delay role. Grade unlikely.
49. `ع ب د B010` dispersed groups/ways -> weak contrast with `ء ل ف/ق ر ش` gathering; no dispersal statement. Grade weak.
50. `ع ب د B011` mount failure/difficult beast -> weak travel-risk; no failed mount. Grade unlikely.
51. `ع ب د B012` perfume grinding stone -> terminated. No perfume/grinding role.

### 106:3 `رب` / `ر ب ب`

52. `ر ب ب B001` lordship/ownership/mastery -> selected S106-S1-003/S106-S1-007. Exact local title. Grade strong.
53. `ر ب ب B002` nurturing/repairing/completing -> selected S106-S1-003 and corroborates feeding/security. Grade strong.
54. `ر ب ب B003` rabbinic knowledge -> terminated. No scholars/teaching role.
55. `ر ب ب B004` large groups -> weak with Quraysh gathering; no group-number term. Grade weak.
56. `ر ب ب B005` stepchild/caretaker relation -> weak care-family fork with House; no stepchild/kinship role. Grade unlikely.
57. `ر ب ب B006` thick syrup/repairing with it -> weak food/provision resonance; no syrup or repair material. Grade unlikely.
58. `ر ب ب B007` abiding/staying/lasting -> selected support for House-centered stability S106-S1-003. Grade medium.
59. `ر ب ب B008` cloud mass -> weak ecological fork with winter/summer rain; no cloud. Grade unlikely.
60. `ر ب ب B009` recent birth/freshness -> terminated. No birth/newness role.
61. `ر ب ب B010` leather container for arrows -> terminated. No arrows/container role.
62. `ر ب ب B011` covenant/neighboring pact -> weak support for protected social order; no covenant noun. Grade weak.
63. `ر ب ب B012` green plant -> weak ecological provision fork; no plant. Grade unlikely.
64. `ر ب ب B013` abundant/sweet water -> weak provision/rain fork; no water. Grade unlikely.
65. `ر ب ب B014` herd -> weak with Quraysh B003 livestock-gathering; no herd. Grade unlikely.
66. `ر ب ب B015` particle `rubba` -> terminated. No particle usage.
67. `ر ب ب B016` need/knot/blessing -> weak blessing/need resonance with hunger/fear; branch too diffuse. Grade weak.
68. `ر ب ب B017` chief of sailors -> terminated. No sailors/sea role.

### 106:3 `البيت` / `ب ي ت`

69. `ب ي ت B001` shelter/dwelling/night-place -> selected S106-S1-003 and S106-S1-009. Grade strong.
70. `ب ي ت B002` household/family -> weak support for group/House relation; local phrase points to House, not family. Grade weak.
71. `ب ي ت B003` verse of poetry -> terminated. No poetry/metre role.
72. `ب ي ت B004` night action/planning/raid -> selected only as weak remote model S106-S1-009; no night action. Grade weak.
73. `ب ي ت B005` food sufficient for night -> support for weak provision-house model S106-S1-009; no night measure. Grade weak.
74. `ب ي ت B006` liquid/thing kept overnight -> weak with provision; no liquid/storage role. Grade unlikely.
75. `ب ي ت B007` grave as house -> terminated. No death/burial role.
76. `ب ي ت B008` house of honor/tribal prestige -> selected support S106-S1-001/S106-S1-003/S106-S1-006. Grade medium-strong.
77. `ب ي ت B010` marriage/house-building -> terminated. No marriage role.

### 106:4 `أطعمهم` / `ط ع م`

78. `ط ع م B001` tasting/eating -> support for S106-S1-004 but less exact than Form IV feeding. Grade medium.
79. `ط ع م B002` feeding another/asking food -> selected S106-S1-004 and corroborator for S106-S1-001/S106-S1-003. Grade strong.
80. `ط ع م B004` livelihood/provision/good condition -> selected S106-S1-006 and support for S106-S1-002/S106-S1-005. Grade medium-strong.
81. `ط ع م B005` fruit ripening -> weak ecological provision fork; no fruit/tree. Grade unlikely.
82. `ط ع م B006` hunting instrument that feeds owner -> weak travel-provision fork; no hunting instrument. Grade unlikely.
83. `ط ع م B007` animal fatness -> weak with mount/provision; no animal body. Grade unlikely.
84. `ط ع م B008` reason/value -> weak support for reason of command; too broad and no explicit reason noun. Grade weak.
85. `ط ع م B009` horse mouth/jowl and asking it to run -> terminated. No horse role.
86. `ط ع م B010` graft accepting joined branch -> weak metaphor with `ء ل ف B002` joining and House-centered group; no plant/graft role. Grade unlikely.
87. `ط ع م B011` ability -> weak support for making travel possible; no ability construction. Grade weak.
88. `ط ع م B012` gripping throat in choking -> weak hunger/fear body image; no choking. Grade unlikely.
89. `ط ع م B013` mouth-to-mouth contact -> terminated. No mouth contact.
90. `ط ع م B014` continuity of form -> weak support for cyclical continuity; no explicit form/creation role. Grade unlikely.

### 106:4 `جوع` / `ج و ع`

91. `ج و ع B001` empty belly/hunger -> selected S106-S1-004 and support for S106-S1-001/S106-S1-005. Grade strong.
92. `ج و ع B002` famine time -> selected support for S106-S1-005; ties to winter-scarcity. Grade medium-strong.
93. `ج و ع B003` causing or intending hunger -> constrained. The Lord feeds from hunger; no agent causing hunger is named. Grade weak.
94. `ج و ع B004` metaphorical emptiness/thinness -> weak lack-image; primary is actual hunger. Grade weak.

### 106:4 `آمنهم` / `ء م ن`

95. `ء م ن B001` security/trust, opposite fear -> selected S106-S1-004/S106-S1-008 and corroborator for S106-S1-001. Grade strong.
96. `ء م ن B002` confirming assent that settles heart -> constrained. In this form with object `هم` and `من خوف`, local sense is giving security, not faith. It may weakly support settled heart after fear. Grade weak.
97. `ء م ن B003` saying amin for response -> weak opening-context prayer echo with basmala, but no supplication formula. Grade unlikely.

### 106:4 `خوف` / `خ و ف`

98. `خ و ف B001` fear expecting harm -> selected S106-S1-004/S106-S1-008. Grade strong.
99. `خ و ف B002` making another afraid -> constrained by recipient-security syntax; weak rival threat branch. Grade weak.
100. `خ و ف B003` overcoming in fear -> weak rivalry image; no contest of fear. Grade unlikely.
101. `خ و ف B004` taking away/diminishing -> weak support for fear as a state removed; no explicit diminishment verb beyond security-from. Grade weak.
102. `خ و ف B005` visible appearance of fear -> selected weak support in S106-S1-008; no visible symptom described. Grade weak.
103. `خ و ف B006` leather bag of honey/water carrier -> terminated. No bag/honey/water carrier role.

## Constructional, Morphosyntactic, and Temporal Seeds

1. `لإيلَاف قريش` idafa and opening lām -> selected S106-S1-001. Generates a reason/purpose field around Quraysh's familiarization. Grade strong.
2. Repeated `إيلَاف` across 106:1-2 -> selected S106-S1-001. The second occurrence reactivates and specifies the first. Grade strong.
3. Possessive `إيلَافهم` -> selected S106-S1-001/S106-S1-002. The group becomes explicit beneficiary/possessor of the familiarized journey. Grade strong.
4. `إيلَافهم رحلة` verbal-noun object construction -> selected S106-S1-002. The familiarization is directed onto a journey. Grade strong.
5. `رحلة الشتاء والصيف` idafa plus coordination -> selected S106-S1-005. Builds a complete seasonal circuit. Grade strong.
6. Ayah boundary after `قريش` -> temporal seed. The first ayah leaves the kind of familiarization unresolved until verse 2. Grade medium-strong.
7. Ayah boundary after `الصيف` -> temporal seed. The travel circuit is left awaiting normative response. Grade medium-strong.
8. `فليعبدوا` with `فـ` and lam al-amr -> selected S106-S1-007. Converts prior benefits into command. Grade strong.
9. `رب هذا البيت` construct plus demonstrative apposition -> selected S106-S1-003. Identifies the worship object through the House. Grade strong.
10. Relative clause `الذي أطعمهم... وآمنهم...` -> selected S106-S1-003/S106-S1-004. Supplies the ground for the title and command. Grade strong.
11. Parallel predicates `أطعمهم / آمنهم` -> selected S106-S1-004. Two divine acts create material and security relief. Grade strong.
12. Parallel `من جوع / من خوف` -> selected S106-S1-004. Two negative states close the surah symmetrically. Grade strong.
13. Sequence `familiarization -> journey -> command -> provider/protector` -> selected S106-S1-001. Temporal exposure is essential to the candidate. Grade strong.
14. Sound recurrence in `إيلَاف / إيلَافهم` -> temporal/acoustic seed. Repetition reinforces reactivation; not independent lexical evidence. Grade medium.
15. Opening basmala as recitational context -> corroborates only divinity/mercy/naming in S106-S1-003/S106-S1-007; not a generating seed. Grade corroborative only.

## Consolidated Image Packet Catalog

### IMG-001

- `Starting seed`: `ء ل ف B005/B002` at 106:1, with `ق ر ش B001/B002`
- `Complete image`: a gathered group made familiar with a repeated seasonal circuit, anchored by the Lord of the House and resolved by provision/security.
- `Passage-order assembly`: familiarization of Quraysh -> familiarization of their winter/summer journey -> worship command to Lord of the House -> feeding from hunger and security from fear.
- `Participants and roles`: Quraysh as gathered group; seasonal journey; House as center; Lord as owner/nurturer; hunger and fear as vulnerabilities; feeding/security as closure.
- `Operation / mechanism`: social and travel instability is turned into stable habit by divine provision and protection.
- `Direction / force / medium`: movement through seasons, return to House, command toward worship.
- `Temporal development`: first `إيلَاف` opens group attachment; second `إيلَاف` specifies journey; `فليعبدوا` makes obligation; verse 4 explains the stabilizing care.
- `Outcome / closure`: the surah closes after both material and security vulnerabilities are resolved.
- `Exact branch constituents`: `ء ل ف B002/B005`, `ق ر ش B001/B002`, `ر ح ل B001`, `ش ت و B001`, `ص ي ف B001`, `ع ب د B003`, `ر ب ب B001/B002`, `ب ي ت B001/B008`, `ط ع م B002`, `ج و ع B001`, `ء م ن B001`, `خ و ف B001`.
- `Unfilled roles`: explicit trade goods, animals, and road threats are not filled.
- `Status`: COMPLETE

### IMG-002

- `Starting seed`: `ر ح ل B001/B002/B003/B005/B006`
- `Complete image`: protected caravan or travel apparatus moving through seasonal stages.
- `Passage-order assembly`: familiarized journey -> winter/summer stages -> House-centered command -> provision and security.
- `Participants and roles`: travelers; route/stages; possible mounts/gear; provider/protector; hunger/fear risks.
- `Operation / mechanism`: a vulnerable travel circuit is made possible by feeding and securing.
- `Direction / force / medium`: outward seasonal movement and return to stable center.
- `Temporal development`: final hunger/fear retroactively fills the practical risks implied by travel.
- `Outcome / closure`: travel becomes livable and therefore morally redirected to worship.
- `Exact branch constituents`: `ر ح ل B001/B002/B003/B005/B006/B008`, `ش ت و B001/B004`, `ص ي ف B001/B003`, `ط ع م B002/B004`, `ج و ع B001/B002`, `ء م ن B001`, `خ و ف B001`.
- `Unfilled roles`: explicit camel/saddle/mount terms are absent.
- `Status`: COMPLETE as secondary simulation; apparatus details are FRAGMENTARY.

### IMG-003

- `Starting seed`: `رب هذا البيت`, `ر ب ب B001/B002`, `ب ي ت B001`
- `Complete image`: House-centered lordship as sheltering ownership and care.
- `Passage-order assembly`: command to worship -> object as Lord of this House -> proof by feeding/security.
- `Participants and roles`: Lord; House; Quraysh; dependents; hunger/fear; provision/security.
- `Operation / mechanism`: lordship is demonstrated by nurture and protection.
- `Direction / force / medium`: benefits flow from Lord to group; worship is directed back to Lord.
- `Temporal development`: verse 4 reactivates `رب` as active nurture, not only title.
- `Outcome / closure`: complete reason for worship.
- `Exact branch constituents`: `ر ب ب B001/B002/B007`, `ب ي ت B001/B008`, `ع ب د B003`, `ط ع م B002`, `ج و ع B001`, `ء م ن B001`, `خ و ف B001`.
- `Unfilled roles`: detailed architecture and household family roles.
- `Status`: COMPLETE

### IMG-004

- `Starting seed`: `أطعمهم من جوع وآمنهم من خوف`
- `Complete image`: paired relief from material lack and threat.
- `Passage-order assembly`: feeding from hunger -> security from fear -> backward explanation of journey and worship.
- `Participants and roles`: hungry/fearful group; feeder/protector; negative source states; relieved beneficiaries.
- `Operation / mechanism`: two divine acts remove two vulnerabilities.
- `Direction / force / medium`: from hunger/fear into provision/security.
- `Temporal development`: second half completes the first and closes the surah.
- `Outcome / closure`: comprehensive care.
- `Exact branch constituents`: `ط ع م B002`, `ج و ع B001/B002`, `ء م ن B001`, `خ و ف B001`, with support from `ر ح ل B001`, `ش ت و B004`, `ص ي ف B003`, `ر ب ب B002`.
- `Unfilled roles`: cause of hunger/fear is not specified.
- `Status`: COMPLETE

### IMG-005

- `Starting seed`: remote hostile `ق ر ش` branches and fear branches.
- `Complete image`: danger cluster tested and rejected.
- `Passage-order assembly`: hostile branch image -> tested against journey and fear/security -> terminated by absent roles.
- `Participants and roles`: possible predator/war/slander/wound/intruder; fearful group; protector.
- `Operation / mechanism`: generic fear is resolved, but no specific hostile mechanism is supplied.
- `Direction / force / medium`: threat toward group, then security.
- `Temporal development`: final `خوف` briefly reactivates these branches, then constrains them.
- `Outcome / closure`: hostile specifics fail; only generic protected-travel risk remains.
- `Exact branch constituents`: `ق ر ش B005/B006/B007/B008/B009`, constrained by `ء م ن B001`, `خ و ف B001`.
- `Unfilled roles`: sea, spears, wound, slander, enemy, intruder.
- `Status`: FRAGMENT

## Exhaustiveness Check After File Creation

- Restarted from first rooted word `إيلَاف`.
- Included `قريش / ق ر ش` despite the QAC TSV omission because the sacred text, attachment row, and branch dossier identify it as rooted; provenance caveat is recorded.
- Initiated seed passes for all 103 accepted lexical occurrence-seeds: `ء ل ف` twice, `ق ر ش`, `ر ح ل`, `ش ت و`, `ص ي ف`, `ع ب د`, `ر ب ب`, `ب ي ت`, `ط ع م`, `ج و ع`, `ء م ن`, and `خ و ف`.
- Initiated constructional, morphosyntactic, temporal, acoustic, and opening-context seed passes.
- Preserved failed and weak seeds rather than dropping them.
- Kept generating, corroborating, and constraining evidence separate in each candidate.
- Checked that every branch ID from the S106 branch dossiers appears in either a candidate, the lexical seed ledger, the constructional seed list, or the rejected fragment catalog.
- Marked recovery-source constraints caused by empty SQLite files.
