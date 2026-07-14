# Stage 1 Pass 2 - S104

Assigned passage: S104, verses 1-9.

Sacred Arabic text source: `resources/quran/surah_104.json`.

Authorized resources inspected:

- `resources/quran/surah_104.json`
- `resources/attachments.tsv`, rows where `sura=104` and `ayah=1..9`
- `resources/qac.sqlite`
- `resources/furuq_v4.sqlite`

## Resource Limitation And Root Cause

The root cause of the limited Pass 1 coverage was not a selective lexical method. It was a hard resource failure: both `resources/qac.sqlite` and `resources/furuq_v4.sqlite` are zero-byte files in the current checkout. Therefore:

- QAC schema, word table, morpheme table, lemmas, measures, and complete rooted-word inventory could not be queried.
- Furuq `branch_images` schema and uncontaminated branch dossiers could not be queried.
- No valid `branch_id`, `branch_image_ar`, or `what_is_ar` content is available for any S104 root.

This Pass 2 restarts from the first rooted occurrence and performs the exhaustive sweep possible under the Stage 1 resource boundary. I do not import outside dictionaries or translations. Lexical seeds are therefore occurrence-level seeds based on the sacred text plus root/form/syntactic data exposed in the authorized S104 attachment rows. Every seed records `branch dossier unavailable` where furuq branch evidence would normally appear.

## Passage Order And Structural Scaffold

Sacred text:

1. `وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ`
2. `ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ`
3. `يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ`
4. `كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ`
5. `وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ`
6. `نَارُ ٱللَّهِ ٱلْمُوقَدَةُ`
7. `ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ`
8. `إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ`
9. `فِى عَمَدٍۢ مُّمَدَّدَةٍۭ`

Attachment scaffold used as structural evidence:

- 104:1 `لِكُلِّ` supplies a khabar-like PP for `وَيْلٌ`; `كُلِّ` is governed by `لـ`; `هُمَزَةٍ` is the genitive complement of `كُلِّ`; `لُمَزَةٍ` is matching descriptive apposition.
- 104:2 `ٱلَّذِى` is subject of `جَمَعَ`; `مَالًا` is direct object; `وَعَدَّدَهُ` is coordinated with `جَمَعَ`; the object suffix in `عَدَّدَهُ` is the direct object.
- 104:3 `أَنَّ مَالَهُ أَخْلَدَهُ` is the proposition reckoned by `يَحْسَبُ`; `مَالَهُ` is governed by `أَنَّ`, is subject of `أَخْلَدَهُ`, and contains a possessor suffix; the suffix in `أَخْلَدَهُ` is direct object.
- 104:4 `ٱلْحُطَمَةِ` is governed by `فِى` as destination complement of `لَيُنْبَذَنَّ`.
- 104:5 `مَا ٱلْحُطَمَةُ` is the embedded question made known by `أَدْرَىٰكَ`; `ٱلْحُطَمَةُ` is predicated of interrogative `مَا`.
- 104:6 `ٱللَّهِ` is genitive complement of `نَارُ`; `ٱلْمُوقَدَةُ` agrees with `نَارُ` as adjective.
- 104:7 `ٱلَّتِى` supplies the subject role for `تَطَّلِعُ`; `ٱلْأَفْـِٔدَةِ` is governed by `عَلَى`.
- 104:8 the suffix in `إِنَّهَا` is the governed ism; `عَلَيْهِم` modifies `مُّؤْصَدَةٌ`; `مُّؤْصَدَةٌ` is the khabar of `إِنَّ`.
- 104:9 `مُّمَدَّدَةٍ` agrees with `عَمَدٍ` as adjective.

## Exhaustive Seed Inventory

Because QAC is unavailable, the eligible rooted occurrence inventory is taken from the S104 attachment rows and then checked against the sacred text order:

1. 104:1:1 `وَيْلٌ` root `و ي ل`
2. 104:1:2 `لِّكُلِّ` root `ك ل ل`
3. 104:1:3 `هُمَزَةٍ` root `ه م ز`
4. 104:1:4 `لُّمَزَةٍ` root `ل م ز`
5. 104:2:1 `ٱلَّذِى` attachment root `ل ل ذ`, function-word seed
6. 104:2:2 `جَمَعَ` root `ج م ع`
7. 104:2:3 `مَالًا` root `م و ل`
8. 104:2:5 `وَعَدَّدَهُ` root `ع د د`
9. 104:3:1 `يَحْسَبُ` root `ح س ب`
10. 104:3:2 `أَنَّ` attachment root `أ و ن`, function-particle seed
11. 104:3:3 `مَالَهُ` root `م و ل`
12. 104:3:4 `أَخْلَدَهُ` root `خ ل د`
13. 104:4:3 `لَيُنۢبَذَنَّ` root `ن ب ذ`
14. 104:4:5 `ٱلْحُطَمَةِ` root `ح ط م`
15. 104:5:2 `وَمَا` attachment root `أ و ي`, interrogative seed
16. 104:5:3 `أَدْرَىٰكَ` root `د ر ي`
17. 104:5:4 `مَا` attachment root `أ و ي`, interrogative seed
18. 104:5:5 `ٱلْحُطَمَةُ` root `ح ط م`
19. 104:6:1 `نَارُ` attachment root `ن و ر`
20. 104:6:2 `ٱللَّهِ` root `أ ل ه`
21. 104:6:3 `ٱلْمُوقَدَةُ` root `و ق د`
22. 104:7:1 `ٱلَّتِى` attachment root `ل ل ت`, function-word seed
23. 104:7:2 `تَطَّلِعُ` root `ط ل ع`
24. 104:7:4 `ٱلْأَفْـِٔدَةِ` root `ف أ د`
25. 104:8:3 `مُّؤْصَدَةٌ` root `أ ص د`
26. 104:9:2 `عَمَدٍ` root `ع م د`
27. 104:9:3 `مُّمَدَّدَةٍ` root `م د د`

Eligible constructional, morphosyntactic, and temporal seeds:

1. 104:1 `وَيْلٌ لِّكُلِّ X`
2. 104:1 paired descriptors `هُمَزَةٍ لُّمَزَةٍ`
3. 104:2 coordinated action `جَمَعَ مَالًا وَعَدَّدَهُ`
4. 104:3 reckoning proposition `يَحْسَبُ أَنَّ مَالَهُ أَخْلَدَهُ`
5. 104:4 corrective rupture `كَلَّا`
6. 104:4 oath/emphasis/passive casting `لَيُنۢبَذَنَّ`
7. 104:4 containment/destination `فِى ٱلْحُطَمَةِ`
8. 104:4-5 repetition and disclosure `ٱلْحُطَمَةِ` -> `مَا ٱلْحُطَمَةُ`
9. 104:6 idafa/adjective definition `نَارُ ٱللَّهِ ٱلْمُوقَدَةُ`
10. 104:7 relative clause `ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ`
11. 104:8 enclosure predicate `إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌ`
12. 104:9 final containment `فِى عَمَدٍ مُّمَدَّدَةٍ`
13. Temporal arc: public hostile-descriptor -> acquisitive acts -> false mental model -> negation -> forced relocation -> disclosure -> divine ignited fire -> inner reach -> sealed enclosure -> extended columns.

## Candidate And Failed Seed Passes

### S104-P2-L001 - `وَيْلٌ`: opening doom as destination frame

- `candidate_id`: S104-P2-L001
- `ayah_range`: 104:1-9
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:1:1 `وَيْلٌ`, root `و ي ل`; furuq branch dossier unavailable
- `initial_image`: an opening condition of ruin or woe directed toward a class.
- `roots_visited`: all roots in the inventory above were structurally checked; no branch IDs available.
- `selected_pre_freeze`: `(E: attachment 104:1 a1, لِكُلِّ supplies PP for وَيْلٌ)`, `(E: attachment 104:1 a3-a4, descriptive pair fills the condemned class)`.
- `constructed_model`: doom is introduced before the actor's deeds are narrated, so the hearer receives a destination/penalty frame first; later actions fill why that frame applies.
- `freeze_point`: after 104:1, before `جَمَعَ مَالًا`.
- `predictions_at_freeze`: a class marker, conduct explaining the woe, later realization of the opened doom-frame, and a closure that makes `وَيْلٌ` concrete.
- `unused_features_tested`: collection/counting of wealth, reckoning of permanence, negation, passive casting, `الحطمة`, fire, inner reach, sealed enclosure, extended columns.
- `corroborators`: `(C: sequence 104:2-3 supplies deeds and belief after the doom-frame)`, `(C: 104:4 passive casting gives the doom an enacted transition)`, `(C: 104:6-9 defines the destination concretely)`.
- `constraints`: `(K: no furuq branch evidence for و ي ل)`, `(K: attachment rows identify syntax, not lexical branch semantics)`.
- `rival_models`: woe as merely local imprecation without passage-scale image; retained as weaker rival.
- `grade`: medium
- `grade_rationale`: structurally strong because the opening frame is completed by later destination imagery, but lexically underdetermined without furuq branches.
- `source_queries_or_rows_used`: `surah_104.json`; attachment rows 104:1 a1-a4, 104:4 a1, 104:6 a1-a2, 104:7 a1-a2, 104:8 a1-a3, 104:9 a1.

### S104-P2-L002 - `لِّكُلِّ`: totalizing distribution

- `candidate_id`: S104-P2-L002
- `ayah_range`: 104:1
- `seed_type`: lexical/function occurrence, branch unavailable
- `seed`: 104:1:2 `لِّكُلِّ`, root `ك ل ل`; furuq branch dossier unavailable
- `initial_image`: comprehensive distribution over every member of a described class.
- `selected_pre_freeze`: `(E: attachment 104:1 a1-a3, PP to وَيْلٌ plus idafa to هُمَزَةٍ)`.
- `constructed_model`: the opening does not target one episode but every instantiation of the paired descriptor.
- `freeze_point`: after `لِّكُلِّ هُمَزَةٍ`.
- `predictions_at_freeze`: plural/class behavior, descriptive apposition, a singular representative expanded by relative clause.
- `unused_features_tested`: `لُمَزَةٍ`, `ٱلَّذِى`, singular relative chain, pronoun suffixes.
- `corroborators`: `(C: 104:1 a4 apposition doubles the descriptor)`, `(C: 104:2 a1 relative pronoun supplies the representative subject)`.
- `constraints`: `(K: later pronouns are singular masculine, so the class is represented through a type, not a counted plural scene)`, `(K: no branch evidence for ك ل ل)`.
- `grade`: medium
- `grade_rationale`: good syntactic evidence for totalized class scope; limited lexical depth.
- `source_queries_or_rows_used`: attachment rows 104:1 a1-a4, 104:2 a1.

### S104-P2-L003 - `هُمَزَةٍ`: first hostile-descriptor seed

- `candidate_id`: S104-P2-L003
- `ayah_range`: 104:1-3
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:1:3 `هُمَزَةٍ`, root `ه م ز`; furuq branch dossier unavailable
- `initial_image`: an intensive descriptive role placed under totalizing condemnation.
- `selected_pre_freeze`: `(E: attachment 104:1 a3, genitive complement of كُلِّ)`, `(E: attachment 104:1 a4, paired with لُمَزَةٍ by apposition)`.
- `constructed_model`: an outward characterizing label is doubled before the text discloses the economic and mental operations behind it.
- `freeze_point`: after the paired descriptor in 104:1.
- `predictions_at_freeze`: the passage may reveal the type's operational behavior; paired descriptor should be connected to a later repeated or accumulating action.
- `unused_features_tested`: `جَمَعَ`, `عَدَّدَهُ`, `يَحْسَبُ`, `مَال`.
- `corroborators`: `(C: 104:2 coordinated action gives repeated acquisition/counting after repeated descriptor)`, `(C: 104:3 reckoning proposition supplies inner calculation behind the public type)`.
- `constraints`: `(K: without furuq branches, no precise branch image for ه م ز can be used)`, `(K: attachment rows do not prove whether the descriptor's lexical force is gesture, speech, pressure, or defect)`.
- `grade`: weak
- `grade_rationale`: the sequence from descriptor to acts is coherent, but the lexical seed cannot be deeply specified.
- `source_queries_or_rows_used`: sacred text; attachment rows 104:1 a3-a4, 104:2 a1-a5, 104:3 a1-a6.

### S104-P2-L004 - `لُّمَزَةٍ`: second hostile-descriptor seed

- `candidate_id`: S104-P2-L004
- `ayah_range`: 104:1-3
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:1:4 `لُّمَزَةٍ`, root `ل م ز`; furuq branch dossier unavailable
- `initial_image`: a second intensive descriptor matching the first in case/form.
- `selected_pre_freeze`: `(E: attachment 104:1 a4, apposition with هُمَزَةٍ)`.
- `constructed_model`: the condemnation is built from a pair rather than a single label; the second term reinforces a type marked by repeated hostile social action.
- `freeze_point`: end of 104:1.
- `predictions_at_freeze`: paired outward descriptors may be followed by a second paired operation.
- `unused_features_tested`: `جَمَعَ` and `عَدَّدَهُ`, object suffix repetition, wealth repetition.
- `corroborators`: `(C: 104:2 a3 coordination of جَمَعَ and عَدَّدَهُ mirrors the paired descriptive opening)`, `(C: 104:3 repeats مال as the object of false confidence)`.
- `constraints`: `(K: no branch evidence for ل م ز)`, `(K: parallelism is structural corroboration only, not lexical proof)`.
- `grade`: weak
- `grade_rationale`: structural pairing is real, but lexical branch content is missing.
- `source_queries_or_rows_used`: attachment rows 104:1 a4, 104:2 a2-a5, 104:3 a1-a6.

### S104-P2-L005 - `ٱلَّذِى`: relative-pronoun type carrier

- `candidate_id`: S104-P2-L005
- `ayah_range`: 104:2-3
- `seed_type`: morphosyntactic/function seed
- `seed`: 104:2:1 `ٱلَّذِى`, attachment root `ل ل ذ`; no lexical branch seed used
- `initial_image`: the condemned class is narrowed into a relative-clause profile.
- `selected_pre_freeze`: `(E: attachment 104:2 a1, subject of جَمَعَ)`, `(E: attachment 104:2 a4, shared subject of عَدَّدَهُ)`.
- `constructed_model`: `ٱلَّذِى` carries the type from description into action; the relative clause creates an explanatory dossier.
- `freeze_point`: after 104:2.
- `predictions_at_freeze`: a continued profile should expose motive or belief.
- `unused_features_tested`: 104:3 `يَحْسَبُ أَنَّ...`.
- `corroborators`: `(C: 104:3 a1 clausal complement supplies the proposition reckoned by the same type)`.
- `constraints`: `(K: function-word seed produces syntax, not a lexical image)`.
- `grade`: medium
- `grade_rationale`: strong for discourse transition from label to profile; not a lexical synthesis.
- `source_queries_or_rows_used`: attachment rows 104:2 a1-a5, 104:3 a1-a6.

### S104-P2-L006 - `جَمَعَ`: gathering wealth as accumulation seed

- `candidate_id`: S104-P2-L006
- `ayah_range`: 104:2-9
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:2:2 `جَمَعَ`, root `ج م ع`; furuq branch dossier unavailable
- `initial_image`: bringing wealth together under the type's control.
- `selected_pre_freeze`: `(E: attachment 104:2 a1, الذي as subject)`, `(E: attachment 104:2 a2, مالا as direct object)`, `(E: attachment 104:2 a3, وعدده coordinated with جمع)`.
- `constructed_model`: an accumulation system: collection is immediately joined to repeated enumeration, making wealth not just possessed but maintained as a counted store.
- `freeze_point`: end of 104:2.
- `predictions_at_freeze`: the store will become cognitively overvalued; the collected object may be treated as protective or durable; later reversal should attack the store's imagined stability.
- `unused_features_tested`: `يحسب`, `ماله`, `أخلده`, `كلا`, `لينبذن`, enclosure/fire.
- `corroborators`: `(C: 104:3 a1, the reckoned proposition supplies the mental use of collected wealth)`, `(C: 104:3 a4-a5, ماله is subject of أخلده and the suffix is the object, giving wealth causal agency in his thought)`, `(C: 104:4 كلا rejects the model)`, `(C: 104:4 passive casting into الحطمة reverses controlled accumulation into uncontrolled disposal)`.
- `constraints`: `(K: no furuq branch evidence for ج م ع)`, `(K: the passage does not state that gathering itself is the only offense; it is embedded in the condemned type and false reckoning)`.
- `rival_models`: collection as social gathering rather than wealth accumulation; defeated by `مَالًا` direct object.
- `grade`: medium-strong
- `grade_rationale`: strong structural trajectory from collection to counting to false permanence to reversal; lexical branch depth missing.
- `source_queries_or_rows_used`: attachment rows 104:2 a1-a5, 104:3 a1-a6, 104:4 a1.

### S104-P2-L007 - `مَالًا`: wealth-object seed, first occurrence

- `candidate_id`: S104-P2-L007
- `ayah_range`: 104:2-4
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:2:3 `مَالًا`, root `م و ل`; furuq branch dossier unavailable
- `initial_image`: concrete wealth as the object being gathered.
- `selected_pre_freeze`: `(E: attachment 104:2 a2, مالا is direct object of جمع)`, `(E: attachment 104:2 a5, suffix in عدده is object of counting)`.
- `constructed_model`: wealth becomes a handled/countable object, first gathered and then repeatedly reckoned.
- `freeze_point`: after 104:2.
- `predictions_at_freeze`: wealth will reappear as a mental anchor; its relation to the person will become explicit.
- `unused_features_tested`: 104:3 `ماله`, possessor suffix, `أخلده`.
- `corroborators`: `(C: 104:3 a2 and a6, ماله is governed by أن and carries possessor suffix)`, `(C: 104:3 a4, ماله is subject of أخلده)`.
- `constraints`: `(K: no branch evidence for م و ل)`, `(K: object handling does not by itself prove moral mechanism; the reckoning proposition supplies that)`.
- `grade`: medium-strong
- `grade_rationale`: the repeated wealth occurrence provides independent temporal reactivation; branch detail unavailable.
- `source_queries_or_rows_used`: attachment rows 104:2 a2-a5, 104:3 a1-a6.

### S104-P2-L008 - `وَعَدَّدَهُ`: counting/repetition seed

- `candidate_id`: S104-P2-L008
- `ayah_range`: 104:2-9
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:2:5 `وَعَدَّدَهُ`, root `ع د د`; furuq branch dossier unavailable
- `initial_image`: the collected object is subjected to repeated enumeration or preparation as countable store.
- `selected_pre_freeze`: `(E: attachment 104:2 a3, coordinated with جمع)`, `(E: attachment 104:2 a5, object suffix as direct object)`.
- `constructed_model`: the type converts wealth into a counted extension of self; the suffix links the counted object back to the earlier direct object.
- `freeze_point`: end of 104:2.
- `predictions_at_freeze`: mental calculation should follow; the counted object may be imagined as extending duration.
- `unused_features_tested`: `يحسب`, `أخلده`, final `ممددة`.
- `corroborators`: `(C: 104:3 a1, يحسب introduces calculation)`, `(C: 104:3 a3-a5, أخلده turns wealth into imagined duration for him)`, `(C: 104:9 a1, ممددة supplies a later extended/lengthened enclosure, a hostile reactivation of extension)`.
- `constraints`: `(K: no branch evidence for ع د د)`, `(K: final extension is punitive architecture, not a direct continuation of wealth-counting)`.
- `rival_models`: counting as mere recounting of deeds; weaker because object suffix points back to wealth in 104:2.
- `grade`: medium
- `grade_rationale`: useful temporal link from counting to calculation to extended closure, but lexical branch evidence absent and final extension is analogical/reactivating rather than direct.
- `source_queries_or_rows_used`: attachment rows 104:2 a3-a5, 104:3 a1-a6, 104:9 a1.

### S104-P2-L009 - `يَحْسَبُ`: reckoning seed

- `candidate_id`: S104-P2-L009
- `ayah_range`: 104:3-9
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:3:1 `يَحْسَبُ`, root `ح س ب`; furuq branch dossier unavailable
- `initial_image`: an inner reckoning or calculation governs the actor's relation to wealth.
- `selected_pre_freeze`: `(E: attachment 104:3 a1, أن ماله أخلده is clausal complement)`.
- `constructed_model`: the passage moves from external conduct to a proposition held in calculation: wealth has made him lasting.
- `freeze_point`: after 104:3.
- `predictions_at_freeze`: the next unit should contradict the reckoning and enact a reality that the calculation cannot control.
- `unused_features_tested`: 104:4 `كلا`, `لينبذن`, `في الحطمة`, 104:5-9 definition.
- `corroborators`: `(C: sacred sequence 104:4 كلا immediately rejects the reckoning)`, `(C: 104:4 a1, casting into الحطمة replaces calculated control with passive disposal)`, `(C: 104:8 a3, مؤصدة as predicate closes the space against escape)`.
- `constraints`: `(K: no branch evidence for ح س ب)`, `(K: calculation model depends on structural complement, not branch-specific lexical dossier)`.
- `grade`: strong structurally, medium lexically
- `grade_rationale`: the freeze prediction is directly satisfied by `كلا` and the passive punitive sequence; lexical branch evidence unavailable.
- `source_queries_or_rows_used`: attachment rows 104:3 a1-a6, 104:4 a1, 104:8 a1-a3.

### S104-P2-L010 - `أَنَّ`: proposition-boundary seed

- `candidate_id`: S104-P2-L010
- `ayah_range`: 104:3
- `seed_type`: morphosyntactic/function seed
- `seed`: 104:3:2 `أَنَّ`, attachment root `أ و ن`; no lexical branch seed used
- `initial_image`: a particle opens the content of what is reckoned.
- `selected_pre_freeze`: `(E: attachment 104:3 a1, clausal complement of يحسب)`, `(E: attachment 104:3 a2-a3, ماله as governed ism and أخلده as predicate content)`.
- `constructed_model`: the false world is held as a bounded proposition: `ماله أخلده`.
- `freeze_point`: after proposition formation.
- `predictions_at_freeze`: a negator/corrective may target the whole proposition rather than a single word.
- `unused_features_tested`: `كلا`.
- `corroborators`: `(C: sequence 104:4 كلا follows immediately and rejects the proposition as a unit)`.
- `constraints`: `(K: function particle has no available furuq branch and does not generate a concrete image by itself)`.
- `grade`: medium
- `grade_rationale`: useful for clause-scope audit, not an independent lexical synthesis.
- `source_queries_or_rows_used`: attachment rows 104:3 a1-a3.

### S104-P2-L011 - `مَالَهُ`: possessed wealth as false agent

- `candidate_id`: S104-P2-L011
- `ayah_range`: 104:3-9
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:3:3 `مَالَهُ`, root `م و ل`; furuq branch dossier unavailable
- `initial_image`: the earlier gathered wealth reappears as his wealth, possessed and mentally promoted to subject.
- `selected_pre_freeze`: `(E: attachment 104:3 a2, ماله governed by أن)`, `(E: attachment 104:3 a4, ماله explicit subject of أخلده)`, `(E: attachment 104:3 a6, suffix as possessor)`.
- `constructed_model`: possessed wealth is imagined as acting on the owner, giving him permanence.
- `freeze_point`: after 104:3.
- `predictions_at_freeze`: a reversal should expose that the possessor is not protected by the possessed object.
- `unused_features_tested`: passive `لينبذن`, `عليهم مؤصدة`, final `في عمد`.
- `corroborators`: `(C: 104:4 a1, he is passively cast into الحطمة, not preserved by wealth)`, `(C: 104:8 a2, عليهم places the enclosure over them)`, `(C: 104:9, containment persists in extended columns)`.
- `constraints`: `(K: no branch evidence for م و ل)`, `(K: ماله is only subject inside the reckoned proposition, not necessarily objective reality)`.
- `grade`: medium-strong
- `grade_rationale`: strong reactivation of wealth from object to false subject; lexical branches missing.
- `source_queries_or_rows_used`: attachment rows 104:2 a2-a5, 104:3 a1-a6, 104:4 a1, 104:8 a2-a3, 104:9 a1.

### S104-P2-L012 - `أَخْلَدَهُ`: permanence seed

- `candidate_id`: S104-P2-L012
- `ayah_range`: 104:3-9
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:3:4 `أَخْلَدَهُ`, root `خ ل د`; furuq branch dossier unavailable
- `initial_image`: making someone remain or last, asserted inside the actor's reckoning.
- `selected_pre_freeze`: `(E: attachment 104:3 a3, أخلده predicate content of أن)`, `(E: attachment 104:3 a4, ماله subject)`, `(E: attachment 104:3 a5, suffix as direct object)`.
- `constructed_model`: the false model says wealth has acted on the person to secure enduring duration.
- `freeze_point`: after 104:3.
- `predictions_at_freeze`: later passage should attack permanence with a rival duration, enclosure, or lasting punitive condition.
- `unused_features_tested`: `الحطمة`, `الموقدة`, `مؤصدة`, `ممددة`.
- `corroborators`: `(C: 104:6 a2, الموقدة describes the fire as ignited)`, `(C: 104:8 a3, مؤصدة provides closed duration)`, `(C: 104:9 a1, ممددة provides extended structure)`.
- `constraints`: `(K: the passage does not let أخلده stand as true; كلا rejects it)`, `(K: no branch evidence for خ ل د)`.
- `rival_models`: permanence as mere long life rather than immortality; unresolved without QAC/furuq, but the corrective sequence still opposes durability.
- `grade`: medium
- `grade_rationale`: strong temporal reversal pattern but lexical specificity unavailable.
- `source_queries_or_rows_used`: attachment rows 104:3 a3-a5, 104:6 a2, 104:8 a3, 104:9 a1.

### S104-P2-L013 - `لَيُنۢبَذَنَّ`: passive casting seed

- `candidate_id`: S104-P2-L013
- `ayah_range`: 104:4-9
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:4:3 `لَيُنۢبَذَنَّ`, root `ن ب ذ`; furuq branch dossier unavailable
- `initial_image`: emphatic passive throwing/casting away into a destination.
- `selected_pre_freeze`: `(E: sacred text كَلَّا as rupture before the verb)`, `(E: attachment 104:4 a1, في الحطمة as destination complement)`.
- `constructed_model`: the self-extending wealth subject is replaced by an acted-upon patient, emphatically discarded into a named crushing destination.
- `freeze_point`: after 104:4.
- `predictions_at_freeze`: the destination should be defined; enclosure or irreversible placement may follow.
- `unused_features_tested`: 104:5-9 definition of الحطمة, fire, inner reach, sealed condition, columns.
- `corroborators`: `(C: 104:5 repetition asks/defines الحطمة)`, `(C: 104:6 fire of God ignited specifies destination)`, `(C: 104:8 عليهم مؤصدة gives enclosure over them)`, `(C: 104:9 في عمد ممددة supplies final fixed containment)`.
- `constraints`: `(K: no branch evidence for ن ب ذ)`, `(K: the patient is implicit in the passive; attachment rows do not identify a named surface patient)`.
- `grade`: medium-strong
- `grade_rationale`: the passive-destination model predicts the following definition and closure well; branch detail missing.
- `source_queries_or_rows_used`: sacred text; attachment rows 104:4 a1, 104:5 a1-a4, 104:6 a1-a2, 104:8 a1-a3, 104:9 a1.

### S104-P2-L014 - `ٱلْحُطَمَةِ`: destination-name seed, first occurrence

- `candidate_id`: S104-P2-L014
- `ayah_range`: 104:4-9
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:4:5 `ٱلْحُطَمَةِ`, root `ح ط م`; furuq branch dossier unavailable
- `initial_image`: a named destination governed by `في`, heard first as the place into which the patient is cast.
- `selected_pre_freeze`: `(E: attachment 104:4 a1, governed by في as destination complement of لينبذن)`.
- `constructed_model`: the passage introduces an ominous container by name before explaining it.
- `freeze_point`: after 104:4.
- `predictions_at_freeze`: the name should be reactivated and defined; its operation should match forced containment and destruction.
- `unused_features_tested`: repetition in 104:5, `نار الله الموقدة`, `تطلع على الأفئدة`, `مؤصدة`, `عمد ممددة`.
- `corroborators`: `(C: 104:5 a3-a4, embedded question makes الحطمة the object of disclosure)`, `(C: 104:6 a1-a2, fire of God ignited defines the container's nature)`, `(C: 104:7 a2, reaches upon/over the أفئدة)`, `(C: 104:8 a3, closed over them)`, `(C: 104:9 a1, extended columns complete the enclosure image)`.
- `constraints`: `(K: no branch evidence for ح ط م, so any crushing/breaking nuance cannot be cited as branch evidence here)`.
- `grade`: medium-strong
- `grade_rationale`: very strong temporal reactivation and definition pattern; lexical branch unavailable.
- `source_queries_or_rows_used`: attachment rows 104:4 a1, 104:5 a3-a4, 104:6 a1-a2, 104:7 a1-a2, 104:8 a1-a3, 104:9 a1.

### S104-P2-L015 - `وَمَا`: first interrogative disclosure seed

- `candidate_id`: S104-P2-L015
- `ayah_range`: 104:5
- `seed_type`: function/morphosyntactic seed
- `seed`: 104:5:2 `وَمَا`, attachment root `أ و ي`; no lexical branch seed used
- `initial_image`: disclosure-gap operator: what could make you know?
- `selected_pre_freeze`: `(E: attachment 104:5 a1, ما as interrogative subject of أدراك)`, `(E: attachment 104:5 a2, ك suffix as addressed object)`.
- `constructed_model`: the listener is paused before the named destination and made to receive its definition as disclosed knowledge.
- `freeze_point`: after `وما أدراك`.
- `predictions_at_freeze`: the following clause should repeat or identify the unknown.
- `unused_features_tested`: second `ما`, `الحطمة`.
- `corroborators`: `(C: 104:5 a3-a4, ما الحطمة is embedded question and predication)`.
- `constraints`: `(K: function seed, no lexical branch image)`.
- `grade`: medium
- `grade_rationale`: structurally important for temporal suspense and reactivation; not lexical.
- `source_queries_or_rows_used`: attachment rows 104:5 a1-a4.

### S104-P2-L016 - `أَدْرَىٰكَ`: knowledge-disclosure seed

- `candidate_id`: S104-P2-L016
- `ayah_range`: 104:5-6
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:5:3 `أَدْرَىٰكَ`, root `د ر ي`; furuq branch dossier unavailable
- `initial_image`: causing the addressed listener to know what the named destination is.
- `selected_pre_freeze`: `(E: attachment 104:5 a2, ك as addressed direct object)`, `(E: attachment 104:5 a3, ما الحطمة embedded question as complement)`.
- `constructed_model`: a pedagogic interruption: the destination is not merely named but disclosed through a question-answer sequence.
- `freeze_point`: after 104:5.
- `predictions_at_freeze`: an explicit definition should immediately follow.
- `unused_features_tested`: 104:6 `نار الله الموقدة`.
- `corroborators`: `(C: 104:6 a1-a2, نار الله الموقدة supplies the answer/definition)`.
- `constraints`: `(K: no branch evidence for د ر ي)`.
- `grade`: medium
- `grade_rationale`: direct structural completion by the next ayah, though no branch dossier.
- `source_queries_or_rows_used`: attachment rows 104:5 a2-a4, 104:6 a1-a2.

### S104-P2-L017 - second `مَا`: identity-question seed

- `candidate_id`: S104-P2-L017
- `ayah_range`: 104:5-6
- `seed_type`: function/morphosyntactic seed
- `seed`: 104:5:4 `مَا`, attachment root `أ و ي`; no lexical branch seed used
- `initial_image`: the unknown is set as subject of a nominal identification.
- `selected_pre_freeze`: `(E: attachment 104:5 a3, ما الحطمة embedded question)`, `(E: attachment 104:5 a4, الحطمة predicated of ما)`.
- `constructed_model`: the passage reopens the name as a question, then defines it.
- `freeze_point`: end of 104:5.
- `predictions_at_freeze`: a nominal definition should answer the question.
- `unused_features_tested`: 104:6.
- `corroborators`: `(C: 104:6, نار الله الموقدة functions as the definitional answer)`.
- `constraints`: `(K: function seed; no branch image)`.
- `grade`: medium
- `grade_rationale`: strong local discourse role; no lexical dossier.
- `source_queries_or_rows_used`: attachment rows 104:5 a3-a4, 104:6 a1-a2.

### S104-P2-L018 - `ٱلْحُطَمَةُ`: reactivated name seed

- `candidate_id`: S104-P2-L018
- `ayah_range`: 104:5-9
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:5:5 `ٱلْحُطَمَةُ`, root `ح ط م`; furuq branch dossier unavailable
- `initial_image`: the destination name is reactivated as an object of inquiry.
- `selected_pre_freeze`: `(E: attachment 104:5 a4, predicated of interrogative ما)`.
- `constructed_model`: the first occurrence in 104:4 generated dread by destination; the second occurrence converts dread into a definitional frame.
- `freeze_point`: after 104:5.
- `predictions_at_freeze`: the following ayat should unpack the name's substance, action, target, and closure.
- `unused_features_tested`: 104:6-9.
- `corroborators`: `(C: 104:6 fire/idafa/adjective supplies substance/source/state)`, `(C: 104:7 relative clause supplies action and target)`, `(C: 104:8 closure over them supplies confinement)`, `(C: 104:9 final PP supplies structural fastening/extension)`.
- `constraints`: `(K: no branch evidence for ح ط م)`.
- `grade`: medium-strong
- `grade_rationale`: excellent reactivation and progressive definition; missing furuq branch detail prevents strong lexical grade.
- `source_queries_or_rows_used`: attachment rows 104:5 a4, 104:6 a1-a2, 104:7 a1-a2, 104:8 a1-a3, 104:9 a1.

### S104-P2-L019 - `نَارُ`: fire-definition seed

- `candidate_id`: S104-P2-L019
- `ayah_range`: 104:6-9
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:6:1 `نَارُ`, attachment root `ن و ر`; furuq branch dossier unavailable
- `initial_image`: the named destination is defined as fire.
- `selected_pre_freeze`: `(E: attachment 104:6 a1, الله as genitive complement of نار)`, `(E: attachment 104:6 a2, الموقدة as adjective agreeing with نار)`.
- `constructed_model`: the destination is not only a place; it is a divinely ascribed ignited fire.
- `freeze_point`: end of 104:6.
- `predictions_at_freeze`: the fire should have an operation or target and a closure condition.
- `unused_features_tested`: 104:7-9.
- `corroborators`: `(C: 104:7 a1-a2, relative clause gives fire's action and target)`, `(C: 104:8 a1-a3, the feminine pronoun returns to the fire/destination as closed over them)`, `(C: 104:9 a1, enclosure is extended in columns)`.
- `constraints`: `(K: attachment root ن و ر for نار is accepted only as exposed row data; no branch image was available)`.
- `grade`: medium-strong
- `grade_rationale`: strong definitional and pronominal continuity, but lexical branch data missing.
- `source_queries_or_rows_used`: attachment rows 104:6 a1-a2, 104:7 a1-a2, 104:8 a1-a3, 104:9 a1.

### S104-P2-L020 - `ٱللَّهِ`: divine-source idafa seed

- `candidate_id`: S104-P2-L020
- `ayah_range`: 104:6
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:6:2 `ٱللَّهِ`, root `أ ل ه`; furuq branch dossier unavailable
- `initial_image`: the fire is attached by idafa to God.
- `selected_pre_freeze`: `(E: attachment 104:6 a1, الله genitive complement of نار)`.
- `constructed_model`: the punitive fire's authority/source is not local social retaliation or wealth failure, but divine attribution.
- `freeze_point`: after 104:6.
- `predictions_at_freeze`: later closure should be absolute and not controllable by the offender.
- `unused_features_tested`: `عليهم مؤصدة`, `في عمد ممددة`.
- `corroborators`: `(C: 104:8 a3, مؤصدة as closed predicate)`, `(C: 104:9 final containment)`.
- `constraints`: `(K: basmala contains الله as opening context but may not be a seed; it can only corroborate divine-source framing)`, `(K: no branch evidence for أ ل ه)`.
- `opening_context`: `(C: basmala opening-context includes الله, but not generating evidence)`.
- `grade`: medium
- `grade_rationale`: idafa is syntactically forced and meaningful; lexical synthesis limited.
- `source_queries_or_rows_used`: sacred text basmala as opening context; attachment rows 104:6 a1, 104:8 a3, 104:9 a1.

### S104-P2-L021 - `ٱلْمُوقَدَةُ`: ignited-state seed

- `candidate_id`: S104-P2-L021
- `ayah_range`: 104:6-9
- `seed_type`: lexical/morphological occurrence, branch unavailable
- `seed`: 104:6:3 `ٱلْمُوقَدَةُ`, root `و ق د`; passive participle/adjective by attachment form tag
- `initial_image`: the fire is already set alight or kept kindled.
- `selected_pre_freeze`: `(E: attachment 104:6 a2, الموقدة agrees with نار as adjective)`.
- `constructed_model`: the destination is an activated fire, not a dormant container.
- `freeze_point`: end of 104:6.
- `predictions_at_freeze`: activated fire should act or reach; target may be internal.
- `unused_features_tested`: 104:7 `تطلع على الأفئدة`, 104:8-9 enclosure.
- `corroborators`: `(C: 104:7 a2, action toward الأفئدة supplies operational reach)`, `(C: 104:8 a3, closed over them keeps the ignited state confined upon its targets)`.
- `constraints`: `(K: no branch evidence for و ق د)`, `(K: morphology says passive participial/adjectival state, not a full independent event)`.
- `grade`: medium-strong
- `grade_rationale`: the adjective predicts an operating fire in the next ayah; lexical branch data unavailable.
- `source_queries_or_rows_used`: attachment rows 104:6 a2, 104:7 a1-a2, 104:8 a1-a3.

### S104-P2-L022 - `ٱلَّتِى`: feminine relative continuation seed

- `candidate_id`: S104-P2-L022
- `ayah_range`: 104:7
- `seed_type`: morphosyntactic/function seed
- `seed`: 104:7:1 `ٱلَّتِى`, attachment root `ل ل ت`
- `initial_image`: a relative clause reactivates the feminine antecedent, most locally `نار`.
- `selected_pre_freeze`: `(E: attachment 104:7 a1, التي supplies feminine subject role for تطلع)`.
- `constructed_model`: the definition continues by assigning the fire an action.
- `freeze_point`: after `ٱلَّتِى تَطَّلِعُ`.
- `predictions_at_freeze`: a complement should specify where the action reaches.
- `unused_features_tested`: `على الأفئدة`.
- `corroborators`: `(C: 104:7 a2, على الأفئدة supplies the governed complement)`.
- `constraints`: `(K: function-word seed produces linkage, not lexical image)`.
- `grade`: medium
- `grade_rationale`: necessary for pronominal/relative continuity; not an independent lexical candidate.
- `source_queries_or_rows_used`: attachment row 104:7 a1-a2.

### S104-P2-L023 - `تَطَّلِعُ`: reaching/upward-looking action seed

- `candidate_id`: S104-P2-L023
- `ayah_range`: 104:7-9
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:7:2 `تَطَّلِعُ`, root `ط ل ع`; furuq branch dossier unavailable
- `initial_image`: the fire performs an action directed `على` the inner targets named as `الأفئدة`.
- `selected_pre_freeze`: `(E: attachment 104:7 a1, التي as subject)`, `(E: attachment 104:7 a2, الأفئدة governed by على as complement)`.
- `constructed_model`: the fire reaches to or overtops the inner seat, converting external punishment into inner exposure.
- `freeze_point`: after 104:7.
- `predictions_at_freeze`: enclosure should prevent the target from escaping this inward reach.
- `unused_features_tested`: 104:8-9.
- `corroborators`: `(C: 104:8 a2-a3, عليهم modifies مؤصدة and closure is predicated)`, `(C: 104:9 a1, final extended columns reinforce fixed enclosure)`.
- `constraints`: `(K: no branch evidence for ط ل ع, so the exact lexical motion cannot be specified beyond the attachment)`, `(K: على marks relation to الأفئدة, but attachment rows do not decide whether it is over/upon/against in image terms)`.
- `grade`: medium
- `grade_rationale`: strong role completion from ignited fire to target to enclosure; branch evidence unavailable.
- `source_queries_or_rows_used`: attachment rows 104:7 a1-a2, 104:8 a2-a3, 104:9 a1.

### S104-P2-L024 - `ٱلْأَفْـِٔدَةِ`: inner-target seed

- `candidate_id`: S104-P2-L024
- `ayah_range`: 104:7-9
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:7:4 `ٱلْأَفْـِٔدَةِ`, root `ف أ د`; furuq branch dossier unavailable
- `initial_image`: the fire's action is directed upon inner human centers.
- `selected_pre_freeze`: `(E: attachment 104:7 a2, الأفئدة governed by على as complement of تطلع)`.
- `constructed_model`: the punishment reaches the inner locus, answering the earlier hidden reckoning in 104:3.
- `freeze_point`: after 104:7.
- `predictions_at_freeze`: the same persons should be enclosed, making inner exposure inescapable.
- `unused_features_tested`: 104:8 `عليهم مؤصدة`, 104:9.
- `corroborators`: `(C: sequence 104:3 concealed reckoning is retrospectively matched by 104:7 inner target)`, `(C: 104:8 a2, عليهم shifts from inner target to persons under closure)`, `(C: 104:8 a3, مؤصدة closes the structure)`.
- `constraints`: `(K: no branch evidence for ف أ د)`, `(K: relation to earlier reckoning is temporal/cognitive reactivation, not a direct syntactic link)`.
- `grade`: medium
- `grade_rationale`: strong passage-level reactivation of inner false belief, but lexical dossier unavailable.
- `source_queries_or_rows_used`: attachment rows 104:3 a1-a6, 104:7 a2, 104:8 a2-a3.

### S104-P2-L025 - `مُّؤْصَدَةٌ`: sealed-closure seed

- `candidate_id`: S104-P2-L025
- `ayah_range`: 104:8-9
- `seed_type`: lexical/morphological occurrence, branch unavailable
- `seed`: 104:8:3 `مُّؤْصَدَةٌ`, root `أ ص د`; passive participle by attachment form tag
- `initial_image`: a closed/sealed condition predicated of the feminine antecedent.
- `selected_pre_freeze`: `(E: attachment 104:8 a1, ها as ism of إن)`, `(E: attachment 104:8 a2, عليهم modifies مؤصدة)`, `(E: attachment 104:8 a3, مؤصدة as khabar of إن)`.
- `constructed_model`: the fire/destination is closed over them; the passive form emphasizes a state imposed on the enclosure.
- `freeze_point`: end of 104:8.
- `predictions_at_freeze`: final verse should specify how closure is held or extended.
- `unused_features_tested`: 104:9 `في عمد ممددة`.
- `corroborators`: `(C: 104:9 a1, ممددة agrees with عمد and supplies extended structural closure)`.
- `constraints`: `(K: no branch evidence for أ ص د)`, `(K: attachment rows do not include a row for في عمد attachment, only adjective agreement)`.
- `grade`: medium-strong
- `grade_rationale`: closure predicts final structural fastening well; lexical branch unavailable.
- `source_queries_or_rows_used`: attachment rows 104:8 a1-a3, 104:9 a1.

### S104-P2-L026 - `عَمَدٍ`: column/support seed

- `candidate_id`: S104-P2-L026
- `ayah_range`: 104:9
- `seed_type`: lexical occurrence, branch unavailable
- `seed`: 104:9:2 `عَمَدٍ`, root `ع م د`; furuq branch dossier unavailable
- `initial_image`: final structural members within/with which the sealed condition is realized.
- `selected_pre_freeze`: `(E: sacred text 104:9 في عمد)`, `(E: attachment 104:9 a1, ممددة agrees with عمد as adjective)`.
- `constructed_model`: closure ends in architecture: columns/supports are extended, giving the seal a lasting spatial mechanism.
- `freeze_point`: after 104:9.
- `predictions_at_freeze`: no later features; test against prior closure and permanence reversal.
- `unused_features_tested`: earlier `أخلده`, `مؤصدة`.
- `corroborators`: `(C: 104:8 a3, مؤصدة supplies closure that columns can structurally support)`, `(C: 104:3 a3-a5, false permanence is answered by punitive extension rather than self-preservation)`.
- `constraints`: `(K: no attachment row explicitly attaches في عمد to مؤصدة or prior clause)`, `(K: no branch evidence for ع م د)`.
- `grade`: weak-medium
- `grade_rationale`: plausible final closure role, but structural attachment is incomplete in the available rows and branch evidence missing.
- `source_queries_or_rows_used`: sacred text 104:9; attachment rows 104:8 a3, 104:9 a1.

### S104-P2-L027 - `مُّمَدَّدَةٍ`: extended-state closure seed

- `candidate_id`: S104-P2-L027
- `ayah_range`: 104:9
- `seed_type`: lexical/morphological occurrence, branch unavailable
- `seed`: 104:9:3 `مُّمَدَّدَةٍ`, root `م د د`; passive participle/adjective by attachment form tag
- `initial_image`: the final structural members are extended or lengthened.
- `selected_pre_freeze`: `(E: attachment 104:9 a1, ممددة agrees with عمد as adjective)`.
- `constructed_model`: the last heard quality is extension, transforming the false claim of wealth-made permanence into an imposed extended enclosure.
- `freeze_point`: end of passage.
- `predictions_at_freeze`: no later features; backward test against counting, permanence, and closure.
- `unused_features_tested`: `عَدَّدَهُ`, `أخلده`, `مؤصدة`.
- `corroborators`: `(C: 104:2 a3-a5, counted wealth creates a prior extension-of-store image)`, `(C: 104:3 a3-a5, أخلده creates false duration)`, `(C: 104:8 a3, مؤصدة supplies the closure extended by final adjective)`.
- `constraints`: `(K: final extension is not the same semantic field as counting or immortality without branch evidence)`, `(K: no branch evidence for م د د)`.
- `grade`: medium
- `grade_rationale`: strong temporal closure and reversal of duration, but lexically not branch-confirmed.
- `source_queries_or_rows_used`: attachment rows 104:2 a3-a5, 104:3 a3-a5, 104:8 a3, 104:9 a1.

## Constructional And Temporal Seeds

### S104-P2-C001 - `وَيْلٌ لِّكُلِّ X`: doom-to-class construction

- `candidate_id`: S104-P2-C001
- `ayah_range`: 104:1
- `seed_type`: constructional
- `seed`: `وَيْلٌ لِّكُلِّ هُمَزَةٍ لُّمَزَةٍ`
- `generating_set`: `(E: attachment 104:1 a1)`, `(E: attachment 104:1 a2)`, `(E: attachment 104:1 a3)`, `(E: attachment 104:1 a4)`.
- `constructed_model`: doom is distributed by a governed PP to every member of a doubled descriptive class.
- `freeze_point`: end of 104:1.
- `predictions_at_freeze`: the class should be explained by a following profile.
- `unused_features_tested`: relative clause and actions in 104:2-3.
- `corroborators`: `(C: 104:2 a1, relative pronoun profiles the class)`, `(C: 104:2-3 action plus reckoning explain the descriptor)`.
- `constraints`: `(K: no lexical branch evidence for the descriptors)`.
- `grade`: medium-strong
- `grade_rationale`: syntactic construction is clear and predicts a profile.
- `source_queries_or_rows_used`: attachment rows 104:1 a1-a4, 104:2 a1-a5, 104:3 a1-a6.

### S104-P2-C002 - Paired descriptors -> paired operations

- `candidate_id`: S104-P2-C002
- `ayah_range`: 104:1-2
- `seed_type`: constructional/temporal
- `seed`: paired descriptor `هُمَزَةٍ لُّمَزَةٍ`
- `generating_set`: `(E: attachment 104:1 a4, apposition/parallelism)`.
- `constructed_model`: a doubled social type is followed by doubled economic action.
- `freeze_point`: end of 104:1.
- `predictions_at_freeze`: following line may use coordination or repetition.
- `unused_features_tested`: `جَمَعَ... وَعَدَّدَهُ`.
- `corroborators`: `(C: attachment 104:2 a3, وعدده coordinated with جمع)`.
- `constraints`: `(K: parallelism alone cannot identify lexical content)`.
- `grade`: medium
- `grade_rationale`: convincing sequence pattern, but not independently lexical.
- `source_queries_or_rows_used`: attachment rows 104:1 a4, 104:2 a3.

### S104-P2-C003 - Gathered and counted wealth

- `candidate_id`: S104-P2-C003
- `ayah_range`: 104:2-3
- `seed_type`: constructional
- `seed`: `جَمَعَ مَالًا وَعَدَّدَهُ`
- `generating_set`: `(E: attachment 104:2 a1-a5)`.
- `constructed_model`: the type gathers a wealth-object and then counts that same object by suffixal return.
- `freeze_point`: end of 104:2.
- `predictions_at_freeze`: the counted object should reappear as psychologically effective.
- `unused_features_tested`: `يحسب أن ماله أخلده`.
- `corroborators`: `(C: 104:3 a1, reckoning proposition follows)`, `(C: 104:3 a4-a5, wealth is subject acting on him inside the proposition)`.
- `constraints`: `(K: no QAC morpheme table to verify exact segmentation beyond attachment row)`.
- `grade`: strong structurally
- `grade_rationale`: direct object and suffixal return create a strong constructional seed.
- `source_queries_or_rows_used`: attachment rows 104:2 a1-a5, 104:3 a1-a6.

### S104-P2-C004 - False permanence proposition

- `candidate_id`: S104-P2-C004
- `ayah_range`: 104:3-4
- `seed_type`: constructional/morphosyntactic
- `seed`: `يَحْسَبُ أَنَّ مَالَهُ أَخْلَدَهُ`
- `generating_set`: `(E: attachment 104:3 a1-a6)`.
- `constructed_model`: an inner calculation encloses a proposition in which possessed wealth acts as subject and the person is object of permanence.
- `freeze_point`: end of 104:3.
- `predictions_at_freeze`: immediate contradiction or reversal should follow.
- `unused_features_tested`: `كلا لينبذن`.
- `corroborators`: `(C: sacred sequence 104:4 كلا)`, `(C: 104:4 a1, passive casting into destination)`.
- `constraints`: `(K: no branch evidence for حساب/خلد)`.
- `grade`: strong structurally
- `grade_rationale`: the following rupture and passive reversal specifically answer the frozen model.
- `source_queries_or_rows_used`: attachment rows 104:3 a1-a6, 104:4 a1.

### S104-P2-C005 - Corrective rupture `كَلَّا`

- `candidate_id`: S104-P2-C005
- `ayah_range`: 104:3-4
- `seed_type`: temporal/discourse
- `seed`: `كَلَّا`
- `generating_set`: `(E: sacred text sequence 104:3 -> 104:4)`.
- `constructed_model`: a discourse brake rejects the preceding reckoning before the punitive transition.
- `freeze_point`: immediately after `كلا`.
- `predictions_at_freeze`: the next words should enact an alternative reality.
- `unused_features_tested`: `لينبذن في الحطمة`.
- `corroborators`: `(C: attachment 104:4 a1, forced destination follows)`.
- `constraints`: `(K: no attachment row for كلا itself)`.
- `grade`: medium-strong
- `grade_rationale`: strong sequence function; not lexical.
- `source_queries_or_rows_used`: sacred text 104:3-4; attachment row 104:4 a1.

### S104-P2-C006 - Emphatic passive disposal

- `candidate_id`: S104-P2-C006
- `ayah_range`: 104:4-9
- `seed_type`: morphosyntactic
- `seed`: `لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ`
- `generating_set`: `(E: sacred text emphatic passive form)`, `(E: attachment 104:4 a1)`.
- `constructed_model`: the agent who gathered and counted becomes the implicit patient of emphatic passive casting into a destination.
- `freeze_point`: end of 104:4.
- `predictions_at_freeze`: the destination will be explained as a containing destructive environment.
- `unused_features_tested`: 104:5-9.
- `corroborators`: `(C: 104:5 repetition and question)`, `(C: 104:6 fire definition)`, `(C: 104:8 closure over them)`, `(C: 104:9 final contained columns)`.
- `constraints`: `(K: the passive patient is inferred from discourse, not an explicit attachment row)`.
- `grade`: medium-strong
- `grade_rationale`: excellent event reversal and destination prediction; lexical branch unavailable.
- `source_queries_or_rows_used`: sacred text 104:4; attachment rows 104:4 a1, 104:5 a3-a4, 104:6 a1-a2, 104:8 a1-a3, 104:9 a1.

### S104-P2-C007 - `فِى ٱلْحُطَمَةِ`: containment/destination

- `candidate_id`: S104-P2-C007
- `ayah_range`: 104:4-9
- `seed_type`: constructional
- `seed`: `فِى ٱلْحُطَمَةِ`
- `generating_set`: `(E: attachment 104:4 a1, الحطمة governed by في as destination complement)`.
- `constructed_model`: the punishment is a transition into a named container.
- `freeze_point`: end of 104:4.
- `predictions_at_freeze`: later material should specify container, interior operation, and closure.
- `unused_features_tested`: 104:6 fire, 104:7 inner target, 104:8 sealed over them, 104:9 in columns.
- `corroborators`: `(C: 104:8 a3, مؤصدة supplies closure)`, `(C: 104:9 final في reactivates containment)`.
- `constraints`: `(K: 104:9 attachment rows do not explicitly attach في عمد to the previous predicate)`.
- `grade`: medium-strong
- `grade_rationale`: containment recurs and closes the passage, but final syntax is only partially represented in available rows.
- `source_queries_or_rows_used`: attachment rows 104:4 a1, 104:8 a3, 104:9 a1; sacred text 104:9.

### S104-P2-C008 - `الحطمة` repetition and disclosure

- `candidate_id`: S104-P2-C008
- `ayah_range`: 104:4-6
- `seed_type`: temporal/acoustic
- `seed`: `ٱلْحُطَمَةِ` -> `مَا ٱلْحُطَمَةُ`
- `generating_set`: `(E: attachment 104:4 a1)`, `(E: attachment 104:5 a3-a4)`.
- `constructed_model`: the destination name is first heard as endpoint, then replayed as an unknown demanding disclosure.
- `freeze_point`: end of 104:5.
- `predictions_at_freeze`: immediate definition should follow.
- `unused_features_tested`: 104:6.
- `corroborators`: `(C: 104:6 a1-a2, نار الله الموقدة supplies definition)`.
- `constraints`: `(K: branch meaning of ح ط م unavailable)`.
- `grade`: strong structurally
- `grade_rationale`: direct repetition creates clear temporal reactivation and definition.
- `source_queries_or_rows_used`: attachment rows 104:4 a1, 104:5 a3-a4, 104:6 a1-a2.

### S104-P2-C009 - Fire definition: source and state

- `candidate_id`: S104-P2-C009
- `ayah_range`: 104:6-7
- `seed_type`: constructional
- `seed`: `نَارُ ٱللَّهِ ٱلْمُوقَدَةُ`
- `generating_set`: `(E: attachment 104:6 a1, idafa)`, `(E: attachment 104:6 a2, adjective agreement)`.
- `constructed_model`: the answer to `ما الحطمة` is a fire attributed to God and described as kindled.
- `freeze_point`: end of 104:6.
- `predictions_at_freeze`: relative continuation should give the fire's action.
- `unused_features_tested`: 104:7.
- `corroborators`: `(C: 104:7 a1-a2, التي تطلع على الأفئدة gives action and target)`.
- `constraints`: `(K: no lexical branch evidence for نار/وقد)`.
- `grade`: medium-strong
- `grade_rationale`: strong constructional definition with direct relative continuation.
- `source_queries_or_rows_used`: attachment rows 104:6 a1-a2, 104:7 a1-a2.

### S104-P2-C010 - Fire reaches the inner target

- `candidate_id`: S104-P2-C010
- `ayah_range`: 104:7-8
- `seed_type`: constructional
- `seed`: `ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ`
- `generating_set`: `(E: attachment 104:7 a1-a2)`.
- `constructed_model`: the defined fire is not merely surrounding; it has a directed relation to the inner human locus.
- `freeze_point`: end of 104:7.
- `predictions_at_freeze`: closure should hold the targets under that inward-reaching condition.
- `unused_features_tested`: 104:8.
- `corroborators`: `(C: 104:8 a2-a3, عليهم modifies مؤصدة and closure is predicated)`.
- `constraints`: `(K: exact lexical image of تطلع unavailable)`.
- `grade`: medium-strong
- `grade_rationale`: action-target-closing sequence is compact and predictive.
- `source_queries_or_rows_used`: attachment rows 104:7 a1-a2, 104:8 a2-a3.

### S104-P2-C011 - Closed over them

- `candidate_id`: S104-P2-C011
- `ayah_range`: 104:8-9
- `seed_type`: constructional
- `seed`: `إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌ`
- `generating_set`: `(E: attachment 104:8 a1-a3)`.
- `constructed_model`: the feminine antecedent is asserted as closed over the punished persons.
- `freeze_point`: end of 104:8.
- `predictions_at_freeze`: final verse should either specify closure structure or terminate in fixed enclosure.
- `unused_features_tested`: 104:9.
- `corroborators`: `(C: 104:9 a1, ممددة modifies عمد; sacred text includes final في عمد)`.
- `constraints`: `(K: no explicit attachment row for the PP في عمد)`.
- `grade`: medium-strong
- `grade_rationale`: final verse plausibly completes closure, though one attachment relation is absent.
- `source_queries_or_rows_used`: attachment rows 104:8 a1-a3, 104:9 a1.

### S104-P2-C012 - Final extended columns

- `candidate_id`: S104-P2-C012
- `ayah_range`: 104:9
- `seed_type`: constructional/closure
- `seed`: `فِى عَمَدٍ مُّمَدَّدَةٍ`
- `generating_set`: `(E: sacred text 104:9)`, `(E: attachment 104:9 a1, adjective agreement)`.
- `constructed_model`: the passage closes with containment plus extended structural members, leaving the hearer in an image of fixed, lengthened confinement.
- `freeze_point`: end of passage.
- `predictions_at_freeze`: no forward predictions; backward test against `أخلده`, `عَدَّدَهُ`, `مؤصدة`.
- `unused_features_tested`: prior false permanence and closure.
- `corroborators`: `(C: 104:3 false permanence is reversed by punitive extension)`, `(C: 104:8 closure is structurally reinforced)`.
- `constraints`: `(K: final PP attachment not represented in available attachment rows)`, `(K: no branch evidence for عمد/مدد)`.
- `grade`: medium
- `grade_rationale`: strong closure image but constrained by incomplete attachment data and missing branch dossiers.
- `source_queries_or_rows_used`: sacred text 104:9; attachment rows 104:3 a3-a5, 104:8 a3, 104:9 a1.

### S104-P2-C013 - Full temporal reactivation arc

- `candidate_id`: S104-P2-C013
- `ayah_range`: 104:1-9
- `seed_type`: temporal/acoustic verified composite
- `seed`: ordered passage exposure
- `generating_set`: `(E: 104:1 doom/class construction)`, `(E: 104:2 gather-count construction)`, `(E: 104:3 false proposition)`, `(E: 104:4 passive casting into الحطمة)`, `(E: 104:5 الحطمة replay)`, `(E: 104:6 fire definition)`, `(E: 104:7 inner target)`, `(E: 104:8 closure)`, `(E: 104:9 final extended structure)`.
- `constructed_model`: the passage starts with social-descriptive condemnation, reveals a wealth-handling system, exposes its inner false calculation, negates it, then makes the false permanence return as a reversed permanence: the person is not extended by wealth but confined in an extended, sealed, divinely ignited enclosure reaching the inner seat.
- `freeze_point`: after 104:4, where the false wealth model has been negated and casting into `الحطمة` introduced.
- `predictions_at_freeze`: definition of destination, destructive medium, target deeper than wealth, closure over the persons, and duration/extension replacing claimed permanence.
- `unused_features_tested`: 104:5-9.
- `corroborators`: `(C: 104:5 repeats الحطمة and asks for definition)`, `(C: 104:6 supplies divinely attributed kindled fire)`, `(C: 104:7 supplies inner target, reactivating the inner reckoning of 104:3)`, `(C: 104:8 closes it over them)`, `(C: 104:9 ends with extended structure, reactivating false duration/counting as punitive duration)`.
- `constraints`: `(K: no furuq branch evidence for any root)`, `(K: QAC morphology not independently queryable because qac.sqlite is empty)`, `(K: therefore this composite is structural-temporal, not a validated branch-level lexical synthesis)`.
- `grade`: medium-strong
- `grade_rationale`: the ordered reactivation is compact and predictive, especially from 104:3-9; the grade cannot be strong because the required branch-level lexical dossiers are absent.
- `source_queries_or_rows_used`: all sacred text; attachment rows listed in structural scaffold.

## Failed Or Terminated Seed Notes

The following seeds were initiated but terminated as independent lexical image generators because they are function words or because the branch database is unavailable:

- `ٱلَّذِى`, `أَنَّ`, `وَمَا`, second `مَا`, and `ٱلَّتِى` produce morphosyntactic linkage only.
- `ك ل ل`, `ه م ز`, `ل م ز`, `و ي ل`, and all other lexical roots lack valid furuq branch dossiers in this checkout, so no branch-specific lexical image can be accepted as generated evidence.
- `نار` is listed in attachment rows with root `ن و ر`; without QAC/furuq verification this is retained only as exposed attachment-row data, not normalized independently.
- `كَلَّا`, `في`, `على`, and pronoun suffixes are retained as constructional/morphosyntactic evidence, not lexical seeds.

## Image Packet Catalog

### IMG-S104-001

- `Starting seed`: `جَمَعَ مَالًا وَعَدَّدَهُ`
- `Complete image`: accumulation-counting system that becomes a false permanence proposition, then is reversed by passive casting.
- `Passage-order assembly`: 104:2 gathering/counting -> 104:3 reckoning wealth as making him last -> 104:4 negation/passive casting.
- `Participants and roles`: condemned type as gatherer/counter/reckoner; wealth as object then false subject; person as object of supposed permanence then passive patient.
- `Operation / mechanism`: collect, count, reckon, negate, cast away.
- `Direction / force / medium`: from controlled acquisition to involuntary destination.
- `Temporal development`: external action -> inner proposition -> corrective rupture.
- `Outcome / closure`: enters the next image, the named destination.
- `Exact branch constituents`: no branch IDs available; structural constituents are attachment rows 104:2 a1-a5, 104:3 a1-a6, 104:4 a1.
- `Unfilled roles, if any`: exact lexical branch semantics for gather/count/reckon/permanence.
- `Status`: COMPLETE structurally, FRAGMENT lexically.

### IMG-S104-002

- `Starting seed`: `ٱلْحُطَمَةِ` in 104:4
- `Complete image`: named destination is replayed as an unknown and defined as divinely attributed kindled fire.
- `Passage-order assembly`: 104:4 destination -> 104:5 question/repetition -> 104:6 fire definition.
- `Participants and roles`: passive patient; destination-name; addressed listener; divine fire.
- `Operation / mechanism`: naming, suspense, disclosure.
- `Direction / force / medium`: into the named container; medium becomes fire.
- `Temporal development`: ominous name -> reactivation -> definition.
- `Outcome / closure`: fire begins its relative-clause action in 104:7.
- `Exact branch constituents`: no branch IDs available; structural constituents are attachment rows 104:4 a1, 104:5 a1-a4, 104:6 a1-a2.
- `Unfilled roles, if any`: exact lexical image of `ح ط م`.
- `Status`: COMPLETE structurally, FRAGMENT lexically.

### IMG-S104-003

- `Starting seed`: `نَارُ ٱللَّهِ ٱلْمُوقَدَةُ`
- `Complete image`: an already-kindled divine fire reaches the inner locus and is closed over the punished persons in extended structure.
- `Passage-order assembly`: 104:6 fire/source/state -> 104:7 action/inner target -> 104:8 sealed over them -> 104:9 extended columns.
- `Participants and roles`: fire/destination as feminine subject; God as source/idafa; inner seats as target; punished persons as enclosed; columns as closure structure.
- `Operation / mechanism`: ignition, reaching/upon relation, sealing, structural extension.
- `Direction / force / medium`: fire directed to `الأفئدة`, closure over `عليهم`, final containment in `عمد`.
- `Temporal development`: definition -> operation -> confinement -> architectural closure.
- `Outcome / closure`: passage ends in fixed extended enclosure.
- `Exact branch constituents`: no branch IDs available; structural constituents are attachment rows 104:6 a1-a2, 104:7 a1-a2, 104:8 a1-a3, 104:9 a1.
- `Unfilled roles, if any`: exact lexical branch semantics for `ط ل ع`, `ف أ د`, `أ ص د`, `ع م د`, `م د د`.
- `Status`: COMPLETE structurally, FRAGMENT lexically.

## Exhaustiveness Check After File Creation

This file restarted from the first rooted occurrence and initiated a seed pass for every eligible rooted occurrence exposed by the S104 attachment rows, including function-word roots exposed there. It also initiated constructional, morphosyntactic, and temporal seed passes for the major actual constructions in the sacred text.

The work is exhaustive relative to the accessible authorized resources. It is not exhaustive relative to the intended furuq/QAC branch standard because the two required SQLite databases are empty in this checkout. No outside resources were substituted.
