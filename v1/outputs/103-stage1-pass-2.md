# S103 Stage 1 Pass 2: Temporally Conditioned Reactivation

Assigned passage: S103  
Sacred Arabic text source: `resources/quran/surah_103.json`  
Prompt: `v1/prompts/stage1.md`

## Resource Note and Root Cause of Pass 1 Limitation

The root cause of the limited Pass 1 sweep was not a judgment that only a few words mattered. The mandated databases `resources/qac.sqlite` and `resources/furuq_v4.sqlite` are present in this checkout as zero-byte files, so schema inspection and row queries returned no data. That blocked the required QAC morphology and furuq branch-dossier sweep.

For this Pass 2 recovery, I restarted from the first rooted word and used the available TSV mirrors under `resources/` for the same S103 data:

- `resources/qac_root_ayah.tsv` for rooted occurrence, surface, lemma, POS, measure, and sequence rows.
- `resources/v4_branches.tsv` for branch dossiers, restricted to the roots in S103.
- `resources/attachments.tsv` for attachment rows restricted to S103.
- `resources/quran/surah_103.json` for sacred Arabic text.

This recovery source substitution is recorded as a constraint on auditability. No translation is used as evidence.

## Sacred Text and Rooted Sequence

```text
103:0 بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
103:1 وَٱلْعَصْرِ
103:2 إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ
103:3 إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَتَوَاصَوْا۟ بِٱلْحَقِّ وَتَوَاصَوْا۟ بِٱلصَّبْرِ
```

Rooted passage words from the recovery QAC row source:

| Occurrence | Root | Surface | Lemma/POS/measure |
| --- | --- | --- | --- |
| 103:1:1 | ع ص ر | عَصْرِ | عَصْر, N |
| 103:2:2 | ء ن س | إِنسَٰنَ | إِنسَٰن, N |
| 103:2:4 | خ س ر | خُسْرٍ | خُسْر, N |
| 103:3:3 | ء م ن | ءَامَنُوا۟ | ءَامَنَ, V, IV |
| 103:3:4 | ع م ل | عَمِلُوا۟ | عَمِلَ, V |
| 103:3:5 | ص ل ح | ٱلصَّٰلِحَٰتِ | صَّٰلِحَٰت, N |
| 103:3:6 | و ص ي | تَوَاصَوْا۟ | تَوَاصَ, V, VI |
| 103:3:7 | ح ق ق | ٱلْحَقِّ | حَقّ, N |
| 103:3:8 | و ص ي | تَوَاصَوْا۟ | تَوَاصَ, V, VI |
| 103:3:9 | ص ب ر | ٱلصَّبْرِ | صَبْر, N |

Opening basmala is recitational opening context only. It is not used as a seed here.

## Attachment Evidence Used

- `(C/K: 103:1 a1)` `وَ` functions as oath particle governing `ٱلْعَصْرِ`.
- `(C/K: 103:2 a1)` `ٱلْإِنسَٰنَ` is governed as the ism of `إِنَّ`.
- `(C: 103:2 a2)` `خُسْرٍ` is governed by `فِي`.
- `(C: 103:2 a3)` `لَفِي خُسْرٍ` is the khabar predication for `إِنَّ`.
- `(C: 103:3 a1)` `إِلَّا` marks `ٱلَّذِينَ` as excepted group; the four predicates complete the scope.
- `(C: 103:3 a2)` `وَعَمِلُوا` is coordinated after `ءَامَنُوا`.
- `(C: 103:3 a3)` `ٱلصَّالِحَاتِ` is direct object of `عَمِلُوا`.
- `(C: 103:3 a4)` first `تَوَاصَوْا` is coordinated after `عَمِلُوا`.
- `(K: 103:3 a5)` `بِٱلْحَقِّ` is governed by `بـ` as content complement of `تَوَاصَوْا`, not a literal weapon event.
- `(C: 103:3 a6)` second `تَوَاصَوْا` is coordinated after the first.
- `(K/C: 103:3 a7)` `بِٱلصَّبْرِ` is governed by `بـ` as content complement of the second `تَوَاصَوْا`.

## Branch Dossier Index

Accepted branches by root:

- `ع ص ر`: B001 time/age, B002 squeezing pressure, B003 rain-bearing cloud, B004 dust-whirl, B005 refuge/attachment, B006 withholding/extraction, B007 gift/yield, B008 sipping to pass choking, B009 maturity, B010 plant in sheath, B011 lineage/origin, B012 inferior client-status, B013 tree-name, B014 dry tongue, B015 intestinal wind. B016 was `review`, not counted as an accepted lexical seed.
- `ء ن س`: B001 manifest human over against wildness/jinn, B002 perception by seeing/hearing/sensing, B003 familiarity removing estrangement, B004 inward-facing side, B005 pupil/image in eye-darkness, B006 self/intimate companion.
- `خ س ر`: B001 general decrease, B002 commercial loss/capital loss, B003 deficient measure/weight, B005 contemptible weak/harm words.
- `ء م ن`: B001 heart at security/trust, B002 confirming assent that settles the heart, B003 saying amin for response.
- `ع م ل`: B001 intentional action/work, B002 putting something to work/using instrument, B003 office/administration, B004 wage/reward of work, B005 dealings/transaction, B006 manual laborers, B007 exertion/trouble, B008 creature formed for work, B009 shaft-near-spearhead, B010 working limb/eye, B011 traveled road, B012 foot travelers.
- `ص ل ح`: B001 soundness opposed to corruption, B002 reconciliation/removing estrangement, B003 suitability, B004 proper name Salih, B005 place names.
- `و ص ي`: B001 joining/connecting, B002 transmitted injunction/testament, B003 reciprocal enjoining, B004 pasture fitting livestock.
- `ح ق ق`: B001 truth fixed against falsehood, B002 binding obligation/desert, B003 owned right, B004 contesting claims of right, B005 establishing/manifesting truth, B007 protected reality/standard, B008 camel maturity and carrying-right, B009 straight inward-reaching thrust, B010 tight weave/firm speech, B011 fitted joint/container, B012 exhausting hard travel, B013 animal completion/fattening, B014 horse step-fit/body tightening.
- `ص ب ر`: B001 restraining self from panic, B002 forced confinement for death/oath, B003 surety/standing-with, B004 top/edge/sides, B005 hard stone/gravel ground, B006 severe no-exit crisis, B007 winter cold severity, B008 bitter aloe extract, B009 sour fruit, B010 white layered cloud, B011 food heap/base cloth, B012 retaliation/qisas, B016 clan name, B017 mountain/middle, B018 stopper/seal.

Total accepted lexical seed units: 77 branch seeds, plus a second occurrence-sensitive `و ص ي` pass for each of B001-B004 at the second `تَوَاصَوْا`, making 81 lexical occurrence-seeds. Constructional, morphosyntactic, and temporal seeds are listed after the lexical seed ledger.

## Candidate Synthesis Units

### S103-S1-001: Enclosed Decrease Under Time-Pressure, Escaped by a Four-Part Maintenance System

- `candidate_id`: S103-S1-001
- `ayah_range`: 103:1-3
- `seed_type`: lexical and verified composite
- `seed`: 103:1 `ٱلْعَصْرِ`, especially `ع ص ر B001` and `B002`
- `generating_set`: `(E: ع ص ر B001 time/age)`, `(E: ع ص ر B002 squeezing pressure)`, `(E: خ س ر B001 general decrease)`, `(E: فِي خسر containment attachment 103:2 a2-a3)`, `(E: إِلَّا exception boundary 103:3 a1)`
- `selected_branches`: `ع ص ر B001/B002`; `خ س ر B001`; then solution-side `ء م ن B001/B002`, `ع م ل B001`, `ص ل ح B001`, `و ص ي B003`, `ح ق ق B001/B002`, `ص ب ر B001`
- `constructed_model`: A whole human subject is announced under an oath by time/pressure. The listener then receives a universal predication: the human is inside an enclosing decrease. The exception does not merely name a belief; it supplies a prevention system: settled inner assent, intentional repair-action, reciprocal truth-maintenance, and reciprocal endurance-maintenance.
- `freeze_point`: After `والعصر` + `إن الإنسان لفي خسر` + `إلا` are constructed as pressure/time + enclosed loss + exception boundary.
- `predictions_at_freeze`: an internal human locus; a counter-decrease operation; a stabilizing truth criterion; continued endurance under pressure; social maintenance rather than solitary escape.
- `unused_features_tested`: `ءَامَنُوا`, `عَمِلُوا`, `ٱلصَّالِحَات`, two `تَوَاصَوْا`, `بِٱلْحَق`, `بِٱلصَّبْر`, coordination sequence, exception scope.
- `corroborators`: `(C: ء م ن B001 security/trust)`, `(C: ء م ن B002 inner confirming assent)`, `(C: ع م ل B001 intentional work)`, `(C: ص ل ح B001 repair against corruption)`, `(C: و ص ي B003 reciprocal enjoining)`, `(C: ح ق ق B001 fixed truth)`, `(C: ح ق ق B002 binding obligation)`, `(C: ص ب ر B001 restraint from panic)`, `(C: repeated تواصوا parallelism 103:3 a4-a7)`, `(C: exception scope includes all four predicates)`.
- `constraints`: `(K: oath by عصر is not itself a lexical assertion that humans are physically squeezed)`, `(K: خسر is a predicated state, not an explicit mechanism of compression)`, `(K: solution terms remain primary religious/moral predicates, not a mechanical pressure machine)`.
- `temporal_reactivation_notes`: `خسر` retroactively makes `العصر` hearable not only as time but as a time-process in which value decays. `إلا` then reactivates the pressure/loss frame as something requiring a complete counter-system. The final `بالصبر` closes where it does because the pressure condition introduced by `العصر` requires continued endurance after truth has been mutually enjoined.
- `rival_models`: Pure “time is passing” model; pure “humans are losers unless pious” static theme. These are locally true but explain less of the order, containment, and repeated maintenance.
- `grade`: strong
- `grade_rationale`: Multiple independent channels converge: oath/time, pressure branch, containment syntax, loss branch, exception boundary, four coordinated predicates, and repeated reciprocal maintenance.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` S103 rows; `v4_branches.tsv` listed roots; attachment rows 103:1 a1, 103:2 a1-a3, 103:3 a1-a7.

### S103-S1-002: Inward Penetration Recast as Counsel-Content Rather Than Violence

- `candidate_id`: S103-S1-002
- `ayah_range`: 103:1-3
- `seed_type`: lexical
- `seed`: 103:3 `بِٱلْحَقِّ`, `ح ق ق B009`
- `generating_set`: `(E: ح ق ق B009 straight thrust reaching inward)`, `(E: ع م ل B002 putting something to work)`, `(E: ع م ل B009 shaft-near-spearhead)`, `(E: ص ب ر B001 restraint/steadiness)`, `(E: ع ص ر B002 pressure)`, `(E: خ س ر B001 decrease)`
- `selected_branches`: `ح ق ق B009`, `ع م ل B002/B009`, `ص ب ر B001`, `ع ص ر B002`, `خ س ر B001`
- `constructed_model`: A remote branch of `حق` opens an image of a straight inward-reaching line. `عمل` can supply use/operation and even spear-shaft adjacency; `صبر` restrains the motion into steadiness; `عصر` and `في خسر` give a pressured, degrading interior. The model becomes a controlled inward intervention into a degrading enclosed condition.
- `freeze_point`: After the controlled-inward-intervention image is built from `حق B009`, `عمل B002/B009`, `صبر B001`, `عصر B002`, and `خسر B001`.
- `predictions_at_freeze`: inner human target; nonrandom straightness; prevention of degradation; a need for restraint; a medium of counsel or guidance if the passage refuses literal combat.
- `unused_features_tested`: `ءَامَنُوا`, `ٱلصَّالِحَات`, `تَوَاصَوْا`, preposition `بـ`, exception syntax.
- `corroborators`: `(C: ء م ن B002 inner assent)`, `(C: ص ل ح B001 repair/counter-corruption)`, `(C: و ص ي B003 reciprocal enjoining)`, `(C: فِي containment)`, `(C: sequence pressure/loss before exception)`.
- `constraints`: `(K: 103:3 a5 بِالحق is content complement of تواصوا, not a weapon event)`, `(K: no literal wielder/target/wound construction)`, `(K: ع م ل B009 is form-remote and secondary; it cannot override primary عملوا الصالحات)`.
- `temporal_reactivation_notes`: The later `بالحق` reactivates earlier `في خسر` as an interior into which truth-content is directed. The second `وتواصوا بالصبر` prevents the image from becoming a strike and converts it into maintained counsel.
- `rival_models`: Literal spear model is rejected by syntax; pure truth-claim model survives but loses the kinetic secondary geometry.
- `grade`: medium-strong
- `grade_rationale`: The seed is remote but explicitly branch-supported and independently constrained by local syntax. It works best as secondary simulation.
- `source_queries_or_rows_used`: `ح ق ق B009`; `ع م ل B002/B009`; `ص ب ر B001`; `ع ص ر B002`; attachments 103:3 a5/a7.

### S103-S1-003: Reciprocal Connection as the Passage’s Maintenance Mechanism

- `candidate_id`: S103-S1-003
- `ayah_range`: 103:3
- `seed_type`: lexical/constructional
- `seed`: first and second `تَوَاصَوْا`, `و ص ي B001/B002/B003`
- `generating_set`: `(E: و ص ي B001 joining one thing to another)`, `(E: و ص ي B002 transmitted injunction)`, `(E: و ص ي B003 reciprocal enjoining)`, `(E: repeated تواصوا بالـ X construction)`
- `selected_branches`: `و ص ي B001/B002/B003`; complements `ح ق ق B001/B002`, `ص ب ر B001`; support from `ء م ن B002`, `ص ل ح B001`.
- `constructed_model`: The exception group is not merely internally corrected; it is kept connected by reciprocal transmission of content. The first transmission attaches to fixed/binding truth; the second attaches to restraint/endurance. The repeated Form VI predicate makes maintenance bilateral and ongoing.
- `freeze_point`: After the repeated `تواصوا بــ` construction is recognized with its two content complements.
- `predictions_at_freeze`: two content domains should be complementary; one should orient correctness, the other continuity; repetition should close the passage by making maintenance durable.
- `unused_features_tested`: `بالحق`, `بالصبر`, prior `آمنوا وعملوا الصالحات`, exception scope.
- `corroborators`: `(C: ح ق ق B001 fixed truth)`, `(C: ح ق ق B002 binding obligation)`, `(C: ص ب ر B001 restraining endurance)`, `(C: coordination 103:3 a4-a7)`, `(C: exception scope 103:3 a1)`.
- `constraints`: `(K: و ص ي B004 pasture-fits-livestock has no local pastoral complement)`, `(K: وصية after death in B002 is not activated by local death/testament roles)`.
- `temporal_reactivation_notes`: Once the second `وتواصوا` is heard, the first is reinterpreted as one half of a paired maintenance system. `بالصبر` retroactively clarifies why `بالحق` alone was not the closing point.
- `rival_models`: Single advice model; static list of virtues. The repeated construction favors a relational maintenance model.
- `grade`: strong
- `grade_rationale`: Exact repeated construction plus branch B003 directly match reciprocal maintenance; two complements fill distinct roles.
- `source_queries_or_rows_used`: `و ص ي B001-B004`; attachments 103:3 a4-a7.

### S103-S1-004: Commercial or Capital-Loss Scene

- `candidate_id`: S103-S1-004
- `ayah_range`: 103:2-3
- `seed_type`: lexical
- `seed`: 103:2 `خُسْر`, `خ س ر B002`
- `generating_set`: `(E: خ س ر B002 commercial loss/capital loss)`, `(E: ع م ل B001 intentional work)`, `(E: ع م ل B004 wage/reward)`, `(E: ص ل ح B001 corrective soundness)`
- `selected_branches`: `خ س ر B002`, `ع م ل B001/B004`, `ص ل ح B001`, `ح ق ق B003`, `و ص ي B002/B003`, `ص ب ر B001`
- `constructed_model`: Human existence is staged as a capital account inside loss. The exception group avoids loss through intentional sound action, recognized right/obligation, and mutual counsel that preserves value over time.
- `freeze_point`: After `خسر B002` plus action/reward branches create an account-loss image.
- `predictions_at_freeze`: explicit work, value-preserving repair, right/claim language, endurance over a trading interval.
- `unused_features_tested`: `عملوا`, `الصالحات`, `بالحق`, `بالصبر`, oath by time.
- `corroborators`: `(C: ع م ل B001 work)`, `(C: ع م ل B004 wage/reward as secondary)`, `(C: ص ل ح B001 repair)`, `(C: ح ق ق B003 owned right)`, `(C: ع ص ر B001 temporal interval)`.
- `constraints`: `(K: no explicit buying/selling/capital noun)`, `(K: خسر is indefinite state in فِي, not a transaction clause)`, `(K: ع م ل B004 is secondary because عملوا here governs الصالحات, not wage)`.
- `temporal_reactivation_notes`: `عملوا الصالحات` retroactively gives the loss image an activity ledger, but `تواصوا` shifts the model from individual accounting to social preservation.
- `rival_models`: Generic decrease model S103-S1-001 is stronger because it requires fewer trade-specific roles.
- `grade`: medium
- `grade_rationale`: Lexically available and partially supported by عمل/حق, but local syntax does not supply trade machinery.
- `source_queries_or_rows_used`: `خ س ر B002`; `ع م ل B001/B004`; `ح ق ق B003`; attachments 103:2 a2-a3.

### S103-S1-005: Deficient Measure and Corrective Standard

- `candidate_id`: S103-S1-005
- `ayah_range`: 103:2-3
- `seed_type`: lexical
- `seed`: 103:2 `خُسْر`, `خ س ر B003`
- `generating_set`: `(E: خ س ر B003 deficient measure/weight)`, `(E: ح ق ق B001 fixed truth)`, `(E: ح ق ق B005 establishing truth)`, `(E: ص ل ح B001 repair)`
- `selected_branches`: `خ س ر B003`, `ح ق ق B001/B005`, `ص ل ح B001`, `ع م ل B001`, `و ص ي B003`
- `constructed_model`: The human condition is imagined as a scale or measure that is being shorted. The exception restores measure through fixed truth, corrective action, and mutual enforcement of the standard.
- `freeze_point`: After the deficient-measure image is built from `خسر B003` and truth/repair branches.
- `predictions_at_freeze`: standard, correction, repeated enforcement, persistence against further shorting.
- `unused_features_tested`: `بالحق`, `الصالحات`, repeated `تواصوا`, `بالصبر`.
- `corroborators`: `(C: ح ق ق B001 fixed against false)`, `(C: ح ق ق B005 establishing truth)`, `(C: ص ل ح B001 against corruption)`, `(C: و ص ي B003 reciprocal enforcement)`.
- `constraints`: `(K: no explicit كيل/ميزان in S103)`, `(K: the passage says humans are in loss, not that they short others)`.
- `temporal_reactivation_notes`: `بالحق` later reactivates the standard implied by a measuring-loss seed, while `بالصبر` supplies continued resistance to degradation.
- `rival_models`: Commercial-loss model; generic decrease model.
- `grade`: medium
- `grade_rationale`: Good branch fit for standard/correction, but missing scale vocabulary.
- `source_queries_or_rows_used`: `خ س ر B003`; `ح ق ق B001/B005`; attachment 103:3 a5.

### S103-S1-006: Human Interior, Exposure, and Eye-Image

- `candidate_id`: S103-S1-006
- `ayah_range`: 103:2-3
- `seed_type`: lexical
- `seed`: 103:2 `ٱلْإِنسَان`, `ء ن س B001-B006`
- `generating_set`: `(E: ء ن س B001 manifest human)`, `(E: ء ن س B006 self/intimate person)`, with fork `(E: ء ن س B005 pupil-image in darkness)`
- `selected_branches`: `ء ن س B001/B005/B006`; corroborators from `ء م ن B001/B002`, `ح ق ق B009`, `فِي خسر`.
- `constructed_model`: The universal human is not an abstract category only; the root dossier opens human manifestation, selfhood/intimacy, and a possible pupil-image in darkness. The passage places this human inside loss, then requires inward assent and truth-content.
- `freeze_point`: After `الإنسان` is placed as `إن`-subject inside `في خسر`.
- `predictions_at_freeze`: interior state; dark/degrading field if the eye-pupil fork is retained; solution should address inner security/assent.
- `unused_features_tested`: `آمنوا`, `بالحق`, `الصبر`, exception group.
- `corroborators`: `(C: ء م ن B001 heart security)`, `(C: ء م ن B002 settled assent)`, `(C: فِي containment)`, `(C: ح ق ق B009 inward-reaching secondary fork)`.
- `constraints`: `(K: الإنسان in context is the human species/person, not literally the pupil)`, `(K: no eye lexeme or seeing verb is supplied)`, `(K: B002 perception and B003 familiarity do not generate passage-scale models without additional local cues)`.
- `temporal_reactivation_notes`: `آمنوا` retroactively specifies that the human-in-loss problem has an inner locus, not only an external social status.
- `rival_models`: Species-only model; eye-darkness model. Species-only is primary; eye-darkness remains weak secondary geometry.
- `grade`: medium
- `grade_rationale`: Inner-state corroboration is strong; eye-image is lexical but locally weak.
- `source_queries_or_rows_used`: `ء ن س B001-B006`; `ء م ن B001/B002`; attachments 103:2 a1-a3.

### S103-S1-007: Refuge and Escape From Pressure

- `candidate_id`: S103-S1-007
- `ayah_range`: 103:1-3
- `seed_type`: lexical
- `seed`: 103:1 `العصر`, `ع ص ر B005`
- `generating_set`: `(E: ع ص ر B005 refuge/escape/attachment)`, `(E: إِلَّا exception boundary)`, `(E: ء م ن B001 security)`, `(E: و ص ي B001 connection)`
- `selected_branches`: `ع ص ر B005`, `ء م ن B001`, `و ص ي B001/B003`, `ص ب ر B001`, `ح ق ق B001`
- `constructed_model`: A less obvious branch of `عصر` makes the opening word a possible search for refuge or attachment. The human is inside loss, then the exception group occupies a refuge-like relational system secured by faith, truth, and endurance.
- `freeze_point`: After `عصر B005` plus `إلا` create a refuge-from-loss image.
- `predictions_at_freeze`: security, attachment, connecting bonds, exit from enclosing loss.
- `unused_features_tested`: `آمنوا`, `تواصوا`, `بالحق`, `بالصبر`.
- `corroborators`: `(C: ء م ن B001 security)`, `(C: و ص ي B001 connection)`, `(C: و ص ي B003 reciprocal enjoining)`, `(C: ص ب ر B001 endurance)`.
- `constraints`: `(K: 103:1 attachment row marks oath complement, not a lexical assertion of refuge)`, `(K: no explicit shelter/place lexeme)`.
- `temporal_reactivation_notes`: `إلا` makes the opening refuge branch newly interesting after the loss statement, but this is a secondary reactivation.
- `rival_models`: Pressure-time model is stronger because `عصر` B001/B002 better match the oath and `في خسر`.
- `grade`: weak-medium
- `grade_rationale`: Branch exists and later security/connection fit, but the local oath use does not foreground refuge.
- `source_queries_or_rows_used`: `ع ص ر B005`; attachments 103:1 a1, 103:3 a1.

### S103-S1-008: Repair and Reconciliation After Estrangement

- `candidate_id`: S103-S1-008
- `ayah_range`: 103:3
- `seed_type`: lexical
- `seed`: 103:3 `ٱلصَّالِحَات`, `ص ل ح B001/B002/B003`
- `generating_set`: `(E: ص ل ح B001 soundness against corruption)`, fork `(E: ص ل ح B002 reconciliation)`, `(E: ص ل ح B003 suitability)`
- `selected_branches`: `ص ل ح B001/B002/B003`, `ع م ل B001`, `و ص ي B003`, `ح ق ق B001`, `ص ب ر B001`, `ء ن س B003`
- `constructed_model`: The exception group acts not generically but in a repair mode: works that restore soundness, possibly reconcile estrangement, and fit the human condition. Reciprocal counsel then maintains the repaired state through truth and endurance.
- `freeze_point`: After `عملوا الصالحات` is built as intentional repair action.
- `predictions_at_freeze`: corruption/decrease should precede; social maintenance should follow; truth and patience should stabilize repair.
- `unused_features_tested`: `في خسر`, `تواصوا بالحق`, `تواصوا بالصبر`.
- `corroborators`: `(C: خ س ر B001 decrease)`, `(C: و ص ي B003 reciprocal enjoining)`, `(C: ح ق ق B001 fixed truth)`, `(C: ص ب ر B001 endurance)`, `(C: attachment 103:3 a3 direct object)`.
- `constraints`: `(K: ص ل ح B004/B005 proper/place names terminate)`, `(K: B002 reconciliation needs social estrangement; passage supplies social reciprocity only after the action phrase)`.
- `temporal_reactivation_notes`: `الصالحات` reactivates `خسر` as a damaged condition capable of repair. Repeated `تواصوا` then extends repair beyond isolated acts.
- `rival_models`: Pure moral-list model; repair-system model explains order better.
- `grade`: medium-strong
- `grade_rationale`: Strong local fit for B001; B002/B003 are plausible secondary forks but less directly generated.
- `source_queries_or_rows_used`: `ص ل ح B001-B005`; attachment 103:3 a3.

### S103-S1-009: No-Exit Crisis and Stopper/Seal Forks

- `candidate_id`: S103-S1-009
- `ayah_range`: 103:2-3
- `seed_type`: lexical
- `seed`: 103:3 `الصبر`, `ص ب ر B006/B018` with support from `B001`
- `generating_set`: `(E: ص ب ر B006 severe no-exit crisis)`, `(E: ص ب ر B018 stopper/seal)`, `(E: فِي خسر containment)`, `(E: خ س ر B001 decrease)`
- `selected_branches`: `ص ب ر B006/B018/B001`, `ع ص ر B002/B006`, `ء م ن B001`, `و ص ي B003`
- `constructed_model`: The final word can reactivate the earlier `في خسر` as an enclosed crisis. One fork imagines endurance in a no-exit severity; another imagines a stopper that prevents leakage or further loss. The primary contextual meaning remains patient endurance.
- `freeze_point`: After final `بالصبر` is heard against the earlier containment.
- `predictions_at_freeze`: enclosing pressure; need for prevention of outflow/decrease; social reinforcement.
- `unused_features_tested`: repeated `تواصوا`, `عصر` pressure/withholding branches, `آمنوا`.
- `corroborators`: `(C: ع ص ر B002 pressure)`, `(C: ع ص ر B006 withholding)`, `(C: و ص ي B003 mutual maintenance)`, `(C: ء م ن B001 security)`.
- `constraints`: `(K: بالصبر is content complement, not a physical plug)`, `(K: no literal bottle/well/stopping noun)`, `(K: B006 no-exit crisis must not erase the exception's escape function)`.
- `temporal_reactivation_notes`: The closing `بالصبر` retrospectively stabilizes the entire surah: pressure/time and loss are not solved by a momentary act but by maintained restraint.
- `rival_models`: Primary endurance model; physical stopper model. Physical stopper remains weak secondary simulation.
- `grade`: medium
- `grade_rationale`: Strong closure for B001; B006/B018 offer useful but constrained imagery.
- `source_queries_or_rows_used`: `ص ب ر B001/B006/B018`; attachments 103:2 a2-a3, 103:3 a7.

### S103-S1-010: Maturity, Eligibility, and Carrying

- `candidate_id`: S103-S1-010
- `ayah_range`: 103:1-3
- `seed_type`: lexical
- `seed`: `ح ق ق B008`, `ع ص ر B009`, `ح ق ق B013`
- `generating_set`: `(E: ح ق ق B008 camel mature enough to carry)`, `(E: ع ص ر B009 reaching youth/maturity)`, `(E: ح ق ق B013 completion/fattening)`
- `selected_branches`: These branches were tested against `عملوا`, `الصالحات`, `تواصوا`, and `الصبر`.
- `constructed_model`: A weak developmental image: time brings beings to a state of eligibility/capacity; the exception group matures into carrying obligations and performing sound works.
- `freeze_point`: After maturity/carrying branches are combined.
- `predictions_at_freeze`: explicit carrying, youth, animal, capacity, or burden roles.
- `unused_features_tested`: `عملوا`, `حق`, `صبر`, `عصر`, `إنسان`.
- `corroborators`: `(C: ح ق ق B002 obligation as a distinct stronger branch)`, `(C: ع م ل B001 action)` only broadly.
- `constraints`: `(K: no camel/youth/carrying lexeme)`, `(K: الإنسان is generic human, not livestock)`, `(K: branch is remote from contextual حق as counsel-content)`.
- `temporal_reactivation_notes`: Minimal. The passage order does not reactivate animal maturity in a sustained way.
- `rival_models`: Obligation/truth model from `حق B001/B002`; pressure-time model.
- `grade`: unlikely
- `grade_rationale`: Branches are accepted but passage-local roles are missing.
- `source_queries_or_rows_used`: `ح ق ق B008/B013`; `ع ص ر B009`.

## Exhaustive Lexical Seed Ledger

Format: `seed -> result`. `Selected model` points to the candidate above; `terminated` means the branch was started, tested against all other passage-root dossiers and constructions, and did not form a passage-local image beyond weak local association.

### 103:1 `العصر` / `ع ص ر`

1. `ع ص ر B001` time/age -> selected model S103-S1-001. Generates temporal exposure; predicts later loss and endurance.
2. `ع ص ر B002` squeezing pressure -> selected model S103-S1-001 and S103-S1-002. Strong pressure transformer.
3. `ع ص ر B003` rain-bearing cloud -> weak fork: pressure releases benefit/rain; tested with `صالحات` as growth/repair and `صبر B010` cloud, but no rain/water/plant outcome in S103. Grade weak.
4. `ع ص ر B004` dust-whirl -> terminated. Circular dust/gust has no local wind/dust/rotation complement; only general pressure from B002 remains useful.
5. `ع ص ر B005` refuge/attachment -> selected weak-medium model S103-S1-007.
6. `ع ص ر B006` withholding/extraction -> weak support for S103-S1-009; predicts blocked value/loss, but no explicit extraction agent. Grade weak.
7. `ع ص ر B007` gift/yield -> weak commercial-yield fork with `خسر B002` and `عمل B004`; no explicit giving/yield. Grade weak.
8. `ع ص ر B008` sipping to pass choking -> terminated. Choking/food/water roles absent; `خسر` does not supply a throat obstruction.
9. `ع ص ر B009` maturity -> selected unlikely model S103-S1-010.
10. `ع ص ر B010` plant in sheath -> weak containment fork with `في خسر`, `صبر B004/B018`; no plant/grain lexeme. Grade unlikely.
11. `ع ص ر B011` lineage/origin -> terminated. `الإنسان` could be species/origin, but no ancestry/nasab role appears.
12. `ع ص ر B012` inferior client-status -> terminated. No mawali/status hierarchy complement.
13. `ع ص ر B013` tree-name -> terminated. No botanical support.
14. `ع ص ر B014` dry tongue -> terminated. No speech/thirst/dryness role, despite counsel verbs.
15. `ع ص ر B015` intestinal wind -> terminated. No passage-local complement.

### 103:2 `الإنسان` / `ء ن س`

16. `ء ن س B001` manifest human -> selected model S103-S1-006; primary subject of universal predication.
17. `ء ن س B002` seeing/hearing/sensing -> weak local auditory support: recitation exposure and later counsel, but no explicit perception verb. Grade weak.
18. `ء ن س B003` familiarity removing estrangement -> support for S103-S1-008 reconciliation fork; no explicit estrangement. Grade weak-medium.
19. `ء ن س B004` inward-facing side -> weak support for inward intervention S103-S1-002; no animal/bow side role. Grade unlikely to weak.
20. `ء ن س B005` pupil/image in darkness -> secondary fork in S103-S1-006; dark enclosure from `في خسر` only indirect. Grade weak.
21. `ء ن س B006` self/intimate companion -> selected in S103-S1-006 as self/interior support; corroborated by `ء م ن B001/B002`. Grade medium.

### 103:2 `خسر` / `خ س ر`

22. `خ س ر B001` general decrease -> selected model S103-S1-001; strong because it is the local predicated state.
23. `خ س ر B002` commercial loss -> selected model S103-S1-004; plausible secondary accounting scene.
24. `خ س ر B003` deficient measure/weight -> selected model S103-S1-005; plausible standard/correction scene.
25. `خ س ر B005` contemptible weak/harm words -> terminated/weak. `الخناسر` weak people could echo universal human weakness, but morphology is remote and no insult/harm-word role exists. Grade unlikely.

### 103:3 `آمنوا` / `ء م ن`

26. `ء م ن B001` security/trust -> selected corroborator in S103-S1-001 and seed candidate: inner security counters loss/pressure. Grade medium-strong as seed.
27. `ء م ن B002` confirming assent that settles heart -> selected in S103-S1-001/S103-S1-006; strong inner-locus match after `الإنسان في خسر`. Grade strong.
28. `ء م ن B003` saying amin -> terminated as lexical seed. Basmala/opening invocation might create prayer context, but S103 has no explicit supplication or response request. Grade unlikely.

### 103:3 `عملوا` / `ع م ل`

29. `ع م ل B001` intentional action/work -> selected in S103-S1-001, S103-S1-004, S103-S1-008; direct local predicate. Grade strong.
30. `ع م ل B002` putting something to work/use -> selected in S103-S1-002; transforms inward truth into operated intervention. Grade medium.
31. `ع م ل B003` office/administration -> terminated. No office, taxation, or appointed agent roles.
32. `ع م ل B004` wage/reward -> support for commercial model S103-S1-004; no explicit wage. Grade weak-medium.
33. `ع م ل B005` dealings/transaction -> support for commercial model S103-S1-004, but no transaction nouns. Grade weak.
34. `ع م ل B006` manual laborers -> terminated. Plural doers exist, but no hand-labor craft roles.
35. `ع م ل B007` exertion/trouble -> weak support for endurance under pressure; no explicit hardship noun beyond `خسر`. Grade weak.
36. `ع م ل B008` creature formed for work -> terminated. No animal/work-beast role.
37. `ع م ل B009` shaft-near-spearhead -> selected only in S103-S1-002 as remote secondary geometry; constrained by syntax. Grade weak-medium.
38. `ع م ل B010` working limb/eye -> weak eye fork with `ء ن س B005`; no explicit eye/limb. Grade unlikely.
39. `ع م ل B011` traveled road -> terminated. No path/travel sequence.
40. `ع م ل B012` foot travelers -> terminated. No walking/travel group.

### 103:3 `الصالحات` / `ص ل ح`

41. `ص ل ح B001` soundness against corruption -> selected model S103-S1-008 and corroborator for S103-S1-001. Grade strong.
42. `ص ل ح B002` reconciliation/removing estrangement -> selected secondary fork S103-S1-008; supported by reciprocal `تواصوا`, constrained by absent explicit quarrel. Grade medium.
43. `ص ل ح B003` suitability -> local suitability fork: works suited to escaping loss; broad but coherent. Grade weak-medium.
44. `ص ل ح B004` proper name Salih -> terminated. No person-name role.
45. `ص ل ح B005` place names -> terminated. No place-name role.

### 103:3 first `تواصوا بالحق` / `و ص ي`

46. `و ص ي B001` joining/connecting -> selected model S103-S1-003; first occurrence connects the group to truth-content. Grade medium-strong.
47. `و ص ي B002` transmitted injunction/testament -> selected model S103-S1-003; first occurrence as transmission of truth. Death-testament subpart constrained. Grade medium-strong.
48. `و ص ي B003` reciprocal enjoining -> selected model S103-S1-003; exact Form VI match. Grade strong.
49. `و ص ي B004` pasture fitting livestock -> terminated. No pasture/livestock role; no local complement.

### 103:3 `بالحق` / `ح ق ق`

50. `ح ق ق B001` fixed truth against falsehood -> selected model S103-S1-001/S103-S1-003; direct local content. Grade strong.
51. `ح ق ق B002` binding obligation/desert -> selected model S103-S1-001/S103-S1-003; truth as binding maintained content. Grade medium-strong.
52. `ح ق ق B003` owned right -> support for commercial/right model S103-S1-004; no claimant/property syntax. Grade medium.
53. `ح ق ق B004` contesting claims of right -> weak rival: reciprocal counsel could prevent disputes over truth, but no litigation/quarrel role. Grade weak.
54. `ح ق ق B005` establishing/manifesting truth -> selected support for S103-S1-005 and S103-S1-003; direct content fit. Grade medium-strong.
55. `ح ق ق B007` protected reality/standard -> weak support for maintaining truth as something defended; no banner/defense role. Grade weak-medium.
56. `ح ق ق B008` camel maturity/carrying-right -> selected unlikely model S103-S1-010; mostly terminates.
57. `ح ق ق B009` inward-reaching thrust -> selected model S103-S1-002; remote but productive secondary image, strongly constrained. Grade medium-strong as secondary.
58. `ح ق ق B010` tight weave/firm speech -> local counsel fork: truth as firm speech woven with patience; supported by `تواصوا`, no textile role. Grade medium.
59. `ح ق ق B011` fitted joint/container -> weak fit with `في خسر` containment and counsel fitting its object; no joint/container noun. Grade weak.
60. `ح ق ق B012` exhausting hard travel -> weak pressure/endurance fork with `عصر B001` and `صبر`; no journey/animal-load role. Grade weak.
61. `ح ق ق B013` animal completion/fattening -> selected unlikely model S103-S1-010; no animal/growth role.
62. `ح ق ق B014` horse step-fit/body tightening -> terminated. No horse/step/running role.

### 103:3 second `تواصوا بالصبر` / `و ص ي`

63. `و ص ي B001` joining/connecting -> selected model S103-S1-003; second occurrence connects the group to endurance-content and connects back to first `تواصوا`. Grade strong.
64. `و ص ي B002` transmitted injunction/testament -> selected model S103-S1-003; second occurrence transmits endurance as counsel. Grade medium.
65. `و ص ي B003` reciprocal enjoining -> selected model S103-S1-003; exact repeated Form VI closure. Grade strong.
66. `و ص ي B004` pasture fitting livestock -> terminated. No pastoral complement.

### 103:3 `بالصبر` / `ص ب ر`

67. `ص ب ر B001` restraining self from panic -> selected in S103-S1-001/S103-S1-003/S103-S1-009; direct closure. Grade strong.
68. `ص ب ر B002` forced confinement for death/oath -> weak constraint/fork: `في خسر` can be a confinement image, but no killing/oath-of-defendant role; do not confuse with oath particle at 103:1. Grade weak.
69. `ص ب ر B003` surety/standing-with -> support for reciprocal maintenance: members stand surety with one another in endurance; no explicit kafala. Grade medium.
70. `ص ب ر B004` top/edge/sides -> weak containment fork with `في خسر`; no vessel/grave side. Grade unlikely.
71. `ص ب ر B005` hard stone/gravel ground -> weak hardness/steadiness image; no stone/ground role. Grade unlikely.
72. `ص ب ر B006` severe no-exit crisis -> selected S103-S1-009; supports crisis enclosure. Grade weak-medium.
73. `ص ب ر B007` winter cold severity -> terminated. No winter/cold role.
74. `ص ب ر B008` bitter aloe extract -> weak bitterness of endurance; no plant/medicine role. Grade unlikely.
75. `ص ب ر B009` sour fruit -> terminated. No fruit/taste role.
76. `ص ب ر B010` white layered cloud -> weak only with `عصر B003`; no cloud/rain in passage. Grade unlikely.
77. `ص ب ر B011` food heap/base cloth -> weak heap/accumulation image with time/loss; no food/measure context. Grade unlikely.
78. `ص ب ر B012` retaliation/qisas -> terminated. No retaliation/legal execution role.
79. `ص ب ر B016` clan name -> terminated. No tribal-name role.
80. `ص ب ر B017` mountain/middle -> weak stability image; no mountain/middle marker. Grade unlikely.
81. `ص ب ر B018` stopper/seal -> selected weak fork S103-S1-009; useful as secondary anti-leak image, syntax constrains. Grade weak.

## Constructional, Morphosyntactic, and Temporal Seeds

1. `والعصر` oath construction -> selected S103-S1-001. Generates temporal/pressure frame; attachment a1 confirms oath governance. Grade strong.
2. `إن الإنسان لفي خسر` predication -> selected S103-S1-001/S103-S1-006. Generates universal human-in-contained-loss image. Grade strong.
3. `في خسر` prepositional containment -> selected S103-S1-001/S103-S1-002/S103-S1-009. Predicts interiority and enclosing state. Grade strong.
4. `إلا الذين...` exception scope -> selected S103-S1-001. Predicts a complete counter-condition rather than one isolated virtue. Grade strong.
5. Relative group `الذين` with four predicates -> selected S103-S1-001. The group is defined by a sequence of conditions. Grade strong.
6. `آمنوا وعملوا الصالحات` pair -> selected S103-S1-008. Inner assent moves into intentional repair-action. Grade strong.
7. `عملوا الصالحات` object attachment -> selected S103-S1-008. Prevents `عمل` from becoming generic motion or instrument only. Grade strong.
8. First `تواصوا بالحق` -> selected S103-S1-003. Reciprocal transmission of truth-content. Grade strong.
9. Second `تواصوا بالصبر` -> selected S103-S1-003/S103-S1-009. Reciprocal transmission of endurance-content and closure. Grade strong.
10. Repeated `تواصوا بــ` parallelism -> selected S103-S1-003. Reactivates the first counsel phrase when the second arrives. Grade strong.
11. Sequence `oath -> universal loss -> exception -> four conditions` -> selected S103-S1-001. Temporal order is essential: pressure/time, diagnosis, escape boundary, maintenance system. Grade strong.
12. Ayah boundary after `والعصر` -> temporal seed. The pause leaves `عصر` unresolved until the loss predication arrives. Grade medium-strong.
13. Ayah boundary after `خسر` -> temporal seed. The loss state remains unresolved until `إلا`. Grade strong.
14. Closure at `بالصبر` -> temporal/acoustic seed. The passage closes after endurance because the pressure/loss frame requires persistence, not merely truth-content. Grade strong.
15. Repeated `و` coordination in 103:3 -> morphosyntactic seed. Additive sequence prevents collapsing the four predicates into one synonym cluster. Grade medium-strong.
16. Recurrent final `-r` sounds in `العصر / خسر / صبر` -> temporal/acoustic seed. Supports auditory reactivation among time-pressure, loss, and endurance; not lexical evidence by itself. Grade weak-medium.

## Consolidated Image Packet Catalog

### IMG-001

- `Starting seed`: `ع ص ر B001/B002`, `في خسر`
- `Complete image`: human existence inside time-pressure and decrease, with a four-part exception system.
- `Passage-order assembly`: oath pressure/time -> human contained in loss -> exception -> faith -> repair-action -> reciprocal truth -> reciprocal endurance.
- `Participants and roles`: human subject; enclosing loss; exception group; inner assent; repair acts; mutual counselors; truth-content; endurance-content.
- `Operation / mechanism`: pressure produces or reveals decrease; exception system prevents/counters it.
- `Direction / force / medium`: time/pressure acts globally; solution operates inwardly and socially through counsel.
- `Temporal development`: unresolved oath, diagnosis, exception, cumulative repair, closure in endurance.
- `Outcome / closure`: the model closes at `بالصبر` because continued pressure requires maintained restraint.
- `Exact branch constituents`: `ع ص ر B001/B002`, `خ س ر B001`, `ء م ن B001/B002`, `ع م ل B001`, `ص ل ح B001`, `و ص ي B003`, `ح ق ق B001/B002`, `ص ب ر B001`.
- `Unfilled roles`: none at the secondary-image level.
- `Status`: COMPLETE

### IMG-002

- `Starting seed`: `ح ق ق B009`
- `Complete image`: controlled inward intervention into a degrading interior, recast as counsel-content.
- `Passage-order assembly`: loss containment creates interior; truth branch supplies inward direction; action/use and patience control it; counsel syntax prevents literalization.
- `Participants and roles`: interior human state; degrading enclosure; truth-content as directed penetration; reciprocal counselors; restraint.
- `Operation / mechanism`: a straight, inward-reaching truth is maintained socially rather than violently enacted.
- `Direction / force / medium`: inward direction, pressure medium, counsel as actual local medium.
- `Temporal development`: later `بالحق` reactivates earlier `في خسر`; later `بالصبر` stabilizes and inhibits literal strike.
- `Outcome / closure`: secondary simulation survives only under syntax constraints.
- `Exact branch constituents`: `ح ق ق B009`, `ع م ل B002/B009`, `ص ب ر B001`, `ع ص ر B002`, `خ س ر B001`, corroborated by `ء م ن B002`, `ص ل ح B001`, `و ص ي B003`.
- `Unfilled roles`: no literal weapon/wound roles; these are intentionally unfilled and constrained.
- `Status`: COMPLETE as secondary simulation, not primary translation.

### IMG-003

- `Starting seed`: repeated `تواصوا بــ`, `و ص ي B003`
- `Complete image`: reciprocal maintenance network.
- `Passage-order assembly`: after inner faith and repair-action, the group maintains two contents: truth and endurance.
- `Participants and roles`: members of exception group; transmitted contents; truth standard; endurance standard.
- `Operation / mechanism`: mutual injunction connects persons and preserves the repair state.
- `Direction / force / medium`: bidirectional social transmission by counsel.
- `Temporal development`: second `تواصوا` reactivates the first and makes the two complements a pair.
- `Outcome / closure`: endurance is the final maintained content.
- `Exact branch constituents`: `و ص ي B001/B002/B003`, `ح ق ق B001/B002/B005`, `ص ب ر B001/B003`.
- `Unfilled roles`: none.
- `Status`: COMPLETE

### IMG-004

- `Starting seed`: `خ س ر B002/B003`
- `Complete image`: loss as capital depletion or deficient measure corrected by truth and repair.
- `Passage-order assembly`: loss predication -> action/repair -> truth standard -> patient maintenance.
- `Participants and roles`: human account/measure; depleted value; corrective acts; truth standard.
- `Operation / mechanism`: repair and truth prevent value-shortfall.
- `Direction / force / medium`: evaluative/accounting field.
- `Temporal development`: `عملوا الصالحات` reactivates loss as damage; `بالحق` reactivates standard.
- `Outcome / closure`: coherent but under-specified.
- `Exact branch constituents`: `خ س ر B002/B003`, `ع م ل B001/B004/B005`, `ص ل ح B001`, `ح ق ق B001/B003/B005`, `ص ب ر B001`.
- `Unfilled roles`: explicit trade, capital, scale, or measure terms.
- `Status`: FRAGMENT

## Exhaustiveness Check After File Creation

- Restarted from first rooted word `العصر`.
- Initiated seed passes for every accepted branch available for each passage root.
- Split repeated `و ص ي` into occurrence-sensitive passes for `تواصوا بالحق` and `تواصوا بالصبر`.
- Initiated constructional, morphosyntactic, temporal, and acoustic seed passes.
- Preserved failed seeds rather than dropping them.
- Kept construction, corroboration, and constraint roles separate in candidate sections.
- Marked recovery-source constraint caused by empty SQLite files.

