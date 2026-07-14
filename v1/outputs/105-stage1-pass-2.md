# Stage 1 Pass 2: S105 Temporally Conditioned Reactivation

Assigned passage: S105  
Sacred Arabic text source: `resources/quran/surah_105.json`

## Restart Note

Root cause of the Pass 1 limitation: the first pass allowed the empty SQLite files and long branch-output truncation to bias the sweep toward a small number of promising words. That was not compliant with the exhaustive singleton-seed rule. This pass restarts from the first rooted word and treats every eligible rooted occurrence and construction as its own seed. The local TSV mirrors were used for the named databases because `resources/qac.sqlite` and `resources/furuq_v4.sqlite` are zero bytes in this checkout.

Resources used:

- Sacred Arabic: `resources/quran/surah_105.json`
- QAC mirror: `resources/qac_root_ayah.tsv`, S105 rows only
- Attachment rows: `resources/attachments.tsv`, S105 rows only
- Branch mirror: `resources/v4_branches.tsv`, accepted branches only for S105 roots

No translation was used as evidence.

## Passage Rooted Occurrences

1. 105:1:2 `تَرَ` root `ر ء ي`
2. 105:1:3 `كَيْفَ` root `ك ي ف`; no accepted v4 branch row found
3. 105:1:4 `فَعَلَ` root `ف ع ل`
4. 105:1:5 `رَبُّكَ` root `ر ب ب`
5. 105:1:6 `أَصْحَابِ` root `ص ح ب`
6. 105:1:7 `فِيلِ` root `ف ي ل`
7. 105:2:2 `يَجْعَلْ` root `ج ع ل`
8. 105:2:3 `كَيْدَهُمْ` root `ك ي د`
9. 105:2:5 `تَضْلِيلٍ` root `ض ل ل`, Form II
10. 105:3:1 `أَرْسَلَ` root `ر س ل`, Form IV
11. 105:3:3 `طَيْرًا` root `ط ي ر`
12. 105:3:4 `أَبَابِيلَ` root `ء ب ل`
13. 105:4:1 `تَرْمِيهِم` root `ر م ي`
14. 105:4:2 `حِجَارَةٍ` root `ح ج ر`
15. 105:4:4 `سِجِّيلٍ` root `س ج ل`
16. 105:5:1 `جَعَلَهُمْ` root `ج ع ل`
17. 105:5:2 `عَصْفٍ` root `ع ص ف`
18. 105:5:3 `مَّأْكُولٍ` root `ء ك ل`

Accepted lexical branch count by root: `ر ء ي` 13, `ف ع ل` 6, `ر ب ب` 17, `ص ح ب` 8, `ف ي ل` 4, `ج ع ل` 11 per occurrence, `ك ي د` 7, `ض ل ل` 5, `ر س ل` 11, `ط ي ر` 5, `ء ب ل` 9, `ر م ي` 8, `ح ج ر` 7, `س ج ل` 5, `ع ص ف` 5, `ء ك ل` 12. Because `ج ع ل` occurs twice, lexical occurrence-branch seeds total 144. `ك ي ف` contributes constructional/interrogative seeds, not branch seeds.

## Candidate Synthesis Units

### S105-CSU-01: Displayed Manner of Divine Action

- ayah_range: 105:1-5
- seed_type: lexical plus constructional convergence
- seed occurrences: 105:1:2 `تَرَ` (`ر ء ي` B001, B002, B013), 105:1:3 `كَيْفَ`, 105:1:4 `فَعَلَ` (`ف ع ل` B001), interrogative construction `أَلَمْ تَرَ كَيْفَ فَعَلَ`
- generating_set: `(E: ر ء ي B001 visible seeing/basira)`, `(E: ر ء ي B002 heart-opinion/thinking)`, `(E: ر ء ي B013 araytaka as alerting/inquiring)`, `(E: ف ع ل B001 occurrence of an act)`, `(E: construction أَلَمْ تَرَ كَيْفَ فَعَلَ)`
- selected_branches: `ر ء ي` B001/B002/B013; `ف ع ل` B001; later support from `ج ع ل` B002, `ض ل ل` B001-B003, `ر م ي` B001, `ع ص ف` B001, `ء ك ل` B001/B006
- constructed_model: The opening is not merely a report but an attention-forcing display: the hearer is made to inspect the manner of an act. The passage then supplies a staged answer: hidden plotting is turned into loss of direction, hostile mass is targeted from above, and the final visible residue is recognizable as consumed plant debris.
- freeze_point: After 105:1, before using 105:2-5.
- predictions_at_freeze: A manner-sequence should follow; the action should become inspectable; later clauses should fill what the divine act did, to whom, by what means, and with what visible result.
- unused_features_tested: 105:2 result-state in `فِي تَضْلِيل`; 105:3 sending upon them; 105:4 projectile/instrument; 105:5 final comparison.
- corroborators: `(C: ج ع ل B002 at 105:2, object made into result-state)`, `(C: ج ع ل B002 at 105:5, persons made into final comparison)`, `(C: attachment a2 105:1, ترى governs كيف-clause)`, `(C: sequence 105:1 question followed by four answer clauses)`, `(C: ayah closure at visible residue)`
- constraints: `(K: ر ء ي B003 dream, B007 menstruation, B008 jinn companion, B009 lung, B010 pregnancy, B011 flag, B012 showing are lexical branches but do not passage-locally expand the inspection model except B012 weakly)`.
- rival_models: A purely optical model from `ر ء ي` B001 is valid but less complete than the alerting-plus-inspection model because the construction asks "how."
- grade: strong
- grade_rationale: The initial construction predicts a manner-disclosure sequence, and the passage supplies a complete ordered chain of act, target, means, and result. Evidence comes from syntax, sequence, and repeated result-making, not from lexical volume.
- source_queries_or_rows_used: S105 QAC root rows; attachment rows `ae:v3:s105:001:pass1:attach:a1-a7`; branches `ر ء ي` B001/B002/B013, `ف ع ل` B001, `ج ع ل` B002.

### S105-CSU-02: Making the Plot Lose Its Path

- ayah_range: 105:2, with whole-surah reactivation
- seed_type: lexical/constructional
- seed occurrences: 105:2:2 `يَجْعَلْ`, 105:2:3 `كَيْدَهُمْ`, 105:2:5 `تَضْلِيلٍ`, construction `جعل X في Y`
- generating_set: `(E: ج ع ل B002 making something into a state)`, `(E: ك ي د B001 severe handling)`, `(E: ك ي د B002 plot/deception)`, `(E: ض ل ل B001 deviation from guidance/path)`, `(E: ض ل ل B002 disappearance/hiddenness)`, `(E: ض ل ل B003 loss of a thing)`
- selected_branches: `ج ع ل` B002; `ك ي د` B001/B002/B004 as local fork; `ض ل ل` B001/B002/B003/B004
- constructed_model: A directed hostile operation is not merely stopped; its own agency is inserted into a field where direction, visibility, retention, and control fail. The plot becomes a lost object, a hidden/vanished effort, and a misdirected path.
- freeze_point: End of 105:2.
- predictions_at_freeze: Later material should show external control over the plotters; target pronouns should persist; a tangible defeat should replace their intended outcome; the result should look like loss of cohesion or direction.
- unused_features_tested: `عليهم` target in 105:3, projectile action in 105:4, final conversion in 105:5.
- corroborators: `(C: ر س ل B001 Form IV sending/release upon them)`, `(C: ر م ي B001 throwing at them)`, `(C: ع ص ف B001 broken plant chaff)`, `(C: ء ك ل B006 corruption/being eaten away)`, `(C: attachment 105:2:a2 direct object كيدهم; 105:2:a4 في تضليل result-state complement)`
- constraints: `(K: ض ل ل B005 lost animal only weakly touches the route-loss image; no animal-loss role is supplied)`, `(K: ك ي د B007 vomiting and B005 crow effort terminate locally)`.
- rival_models: `ك ي د` B004 war/armed encounter creates a military-conflict fork, but the grammar foregrounds their plot as the object, not an open battle.
- grade: strong
- grade_rationale: This unit has high lexical specificity and is directly carried by the 105:2 construction. Later pronoun continuity and final disintegration independently satisfy the frozen predictions.
- source_queries_or_rows_used: S105 QAC rows for 105:2; attachment rows `ae:v3:s105:002:pass1:attach:a1-a4`; branches `ج ع ل` B002, `ك ي د` B001/B002/B004, `ض ل ل` B001-B004.

### S105-CSU-03: Released Flocks as Serial Targeting Medium

- ayah_range: 105:3-4
- seed_type: lexical/constructional
- seed occurrences: 105:3:1 `أَرْسَلَ`, 105:3:3 `طَيْرًا`, 105:3:4 `أَبَابِيلَ`, 105:4:1 `تَرْمِيهِم`
- generating_set: `(E: ر س ل B001 sending/release)`, `(E: ر س ل B005 successive groups/قطيع بعد قطيع)`, `(E: ط ي ر B001 flying creatures/light aerial movement)`, `(E: ء ب ل B003 groups, scattered or following one after another)`, `(E: ر م ي B001 throwing/projecting objects)`
- selected_branches: `ر س ل` B001/B005; `ط ي ر` B001/B002; `ء ب ل` B003; `ر م ي` B001/B003; support from attachments 105:3 and 105:4
- constructed_model: The answer to the failed plot comes as released aerial bodies in successive/scattered groupings. Their movement is not static presence but targeted projection: they are sent upon the plotters, and the next ayah reactivates them as the implied subject throwing at those same targets.
- freeze_point: After `طيرًا أبابيل`, before 105:4.
- predictions_at_freeze: The flocks should have a function; the target `عليهم` should remain active; the aerial release should become an operation rather than a scenic detail.
- unused_features_tested: `ترميهم` in 105:4, instrument `بحجارة`, source/kind `من سجيل`, final result 105:5.
- corroborators: `(C: ر م ي B001 fulfills projected action)`, `(C: ح ج ر B003 supplies hard projectile)`, `(C: attachment 105:3:a1 عليهم as target complement; 105:4:a1 هم as object suffix)`, `(C: attachment 105:3:a3/a4 أبَابِيل adjective or hal for طيرًا, both preserve flock characterization)`
- constraints: `(K: ء ب ل B001 camels and B005 bundle of firewood can create analogical grouping but do not override the local طير modifier)`, `(K: ر س ل B002 message/mission is weak because the sent object is birds, not speech)`.
- rival_models: A message-delivery model from `ر س ل` B002 is possible only as subordinate "agency by sending"; it lacks local speech content.
- grade: strong
- grade_rationale: The selected branches complete each other tightly: sending/release, aerial beings, grouped succession, and throwing all occupy distinct roles in the local syntax.
- source_queries_or_rows_used: S105 QAC 105:3-4; attachment rows `ae:v3:s105:003:pass1:attach:a1-a4`, `ae:v3:s105:004:pass1:attach:a1-a3`; branches listed above.

### S105-CSU-04: Hard Boundaries Thrown as Instrument

- ayah_range: 105:4
- seed_type: lexical/constructional
- seed occurrences: 105:4:1 `تَرْمِيهِم`, 105:4:2 `بِحِجَارَةٍ`, 105:4:4 `سِجِّيلٍ`
- generating_set: `(E: ر م ي B001 throwing from hand/bow/stone/spear-like projection)`, `(E: ح ج ر B003 hard stone)`, `(E: ح ج ر B001 prevention/enclosure as a secondary dimension)`, `(E: س ج ل B001 full bucket/pouring out as possible medium-force fork)`, `(E: س ج ل B004 written register as possible marked/recorded-source fork)`
- selected_branches: `ر م ي` B001/B003; `ح ج ر` B003 with secondary B001/B006; `س ج ل` B001/B004
- constructed_model: The airborne operation becomes concrete through hard, bounded objects used instrumentally. The `بـ` attachment marks stones as the means of throwing; `من سجيل` then specifies source/kind. The branch data for `س ج ل` does not directly generate "baked clay"; it supports only secondary images of pouring-fullness or recorded/fixed material.
- freeze_point: After 105:4.
- predictions_at_freeze: The next clause should show impact, fragmentation, consumption, or conversion of the targets into damaged material.
- unused_features_tested: 105:5 `فجعلهم كعصف مأكول`.
- corroborators: `(C: ج ع ل B002 at 105:5, transformation of them into result)`, `(C: ع ص ف B001 broken chaff)`, `(C: ء ك ل B001 eaten and B006 corrupted/eaten-away)`, `(C: attachment 105:4:a2 بِحجارة as instrument complement)`, `(C: attachment 105:4:a3 من سجيل as kind/source of stones)`
- constraints: `(K: س ج ل branch evidence is not a direct lexical proof for the Qur'anic foreign noun's material; do not overclaim it)`, `(K: ح ج ر B002 mind/restraint and B007 protected mare terminate as seed branches for this local projectile model)`.
- rival_models: `س ج ل` B004 can produce a "registered decree" secondary simulation, but locally it is constrained by `من` modifying stones rather than a book or legal record.
- grade: medium-strong
- grade_rationale: The projectile and stone evidence is direct and strong; `س ج ل` contributes only constrained secondary support because its branch dossier does not match the surface noun transparently.
- source_queries_or_rows_used: S105 QAC 105:4; attachment rows `ae:v3:s105:004:pass1:attach:a1-a3`; branches `ر م ي`, `ح ج ر`, `س ج ل`.

### S105-CSU-05: Final Conversion into Eaten Chaff

- ayah_range: 105:5, with backward replay to 105:2
- seed_type: lexical/constructional
- seed occurrences: 105:5:1 `جَعَلَهُمْ`, 105:5:2 `عَصْفٍ`, 105:5:3 `مَّأْكُولٍ`
- generating_set: `(E: ج ع ل B002 making persons into a state/comparison)`, `(E: ع ص ف B001 husk/chaff/broken plant matter)`, `(E: ء ك ل B001 eating/consumed food)`, `(E: ء ك ل B006 erosion/corruption/being eaten away)`, `(E: ء ك ل B007 prey/prepared for eating)`
- selected_branches: `ج ع ل` B002; `ع ص ف` B001/B002/B004; `ء ك ل` B001/B002/B006/B007
- constructed_model: The closure turns the human target group into agricultural residue after consumption: not merely defeated, but converted into something already processed, emptied, and left as fragile plant waste. Backward replay reactivates 105:2: their plot entered loss, and they themselves become the visible lost remainder.
- freeze_point: End of 105:5.
- predictions_at_freeze: As a closing image, it should explain why the passage stops here: the hostile agency has no remaining active role, only a comparison-residue.
- unused_features_tested: Earlier `جعل كيدهم في تضليل`, `ترميهم`, `أصحاب الفيل`.
- corroborators: `(C: ج ع ل B002 occurs twice, first plot-to-loss then persons-to-residue)`, `(C: ر م ي B001 supplies destructive impact before residue)`, `(C: ك ي د B002 plot now retrospectively futile)`, `(C: ف ي ل B001 weakness-of-opinion branch weakly reactivates "elephant" as false strength, not primary meaning)`, `(C: attachment 105:5:a2 كعصف comparison complement; 105:5:a3 مأكول adjective of عصف)`
- constraints: `(K: ء ك ل B004 eating wealth, B009 slander, B010 accusation, B011 small group by head, B012 strong cloth/intellect, B013 vessel do not passage-locally expand the chaff result)`.
- rival_models: A windstorm model from `ع ص ف` B002/B004 explains scattering/destruction but is secondary; the surface expression chooses `عصف مأكول`, residue after eating, not simply storm.
- grade: strong
- grade_rationale: Closure is lexically and syntactically tight. The comparison and adjective are directly attached, and the two `ج ع ل` occurrences create a strong temporal transformation arc.
- source_queries_or_rows_used: S105 QAC 105:5; attachment rows `ae:v3:s105:005:pass1:attach:a1-a3`; branches `ج ع ل`, `ع ص ف`, `ء ك ل`.

### S105-CSU-06: False Massive Power and Weak Judgment

- ayah_range: 105:1-2, with later defeat
- seed_type: lexical
- seed occurrences: 105:1:6 `أصحاب`, 105:1:7 `الفيل`, 105:2:3 `كيدهم`
- generating_set: `(E: ص ح ب B001 companionship/possession)`, `(E: ف ي ل B004 elephant animal)`, `(E: ف ي ل B001 weak opinion/faulty judgment as secondary branch)`, `(E: ك ي د B002 plotting/stratagem)`
- selected_branches: `ص ح ب` B001/B003/B004; `ف ي ل` B004 with secondary B001/B003; `ك ي د` B002
- constructed_model: The phrase `أصحاب الفيل` first activates possession/companionship with a massive animal. Branch replay then exposes a rival interior dimension: the visible emblem of strength is paired with weak judgment or hidden guessing. The passage answers this false power by making their plan enter misdirection.
- freeze_point: After 105:1.
- predictions_at_freeze: If the elephant identity is not decorative, their strength-symbol should be undone by a more precise agency; if weak-opinion branch is active, planning should fail cognitively or directionally.
- unused_features_tested: 105:2 `كيدهم في تضليل`, 105:3-5 targeting and final residue.
- corroborators: `(C: ك ي د B002 confirms planning/stratagem)`, `(C: ض ل ل B001/B003 confirms misdirection/loss)`, `(C: final كعصف مأكول empties the mass-power image)`, `(C: attachment 105:1:a7 الفيل as idafa complement of أصحاب)`
- constraints: `(K: ف ي ل B001 is not the primary contextual meaning of الفيل; B004 animal is the surface referent)`, `(K: ف ي ل B002 hip-flesh and B003 hiding-game are weak/terminated except B003 faintly mirrors concealed strategy)`
- rival_models: A pure historical identifier model is simpler and primary. The weak-judgment branch remains secondary simulation.
- grade: medium
- grade_rationale: Possession plus elephant is direct; the weak-judgment activation is lexically available but remote and must remain subordinate.
- source_queries_or_rows_used: S105 QAC 105:1-2; attachment rows 105:1:a6-a7, 105:2:a2-a4; branches `ص ح ب`, `ف ي ل`, `ك ي د`, `ض ل ل`.

### S105-CSU-07: Repeated Making as Transformation Spine

- ayah_range: 105:2 and 105:5
- seed_type: temporal/morphosyntactic
- seed occurrences: `يَجْعَلْ` 105:2 and `جَعَلَهُمْ` 105:5
- generating_set: `(E: ج ع ل B002 making X into Y)`, `(E: repetition of root ج ع ل across ayat 2 and 5)`, `(E: attachment 105:2 object كيدهم + result في تضليل)`, `(E: attachment 105:5 object هم + comparison كعصف مأكول)`
- selected_branches: `ج ع ل` B002; B001 as weaker create/do support; B004 terminated because neither occurrence is "began to do"
- constructed_model: Two transformations frame the central intervention. First, the hostile plan is made into misdirection; then the hostile people are made into consumed residue. The first conversion is abstract/cognitive; the second is bodily/material.
- freeze_point: After recognizing the second `ج ع ل`.
- predictions_at_freeze: Both objects should share pronoun continuity with the elephant-companions; the first result should anticipate the second result.
- unused_features_tested: `هم` suffix continuity, central sending/throwing episode.
- corroborators: `(C: pronouns هم in كيدهم، عليهم، ترميهم، جعلهم bind the same target group)`, `(C: ر س ل+ر م ي episode supplies mechanism between the two transformations)`, `(C: ض ل ل then عصف مأكول create abstract-to-material degradation)`
- constraints: `(K: ج ع ل B005 wage, B006 palm, B007 pot-cloth, B008 beetle, B009 animal heat, B010 ostrich chick, B011 place-name, B012 short/fat/stubborn do not passage-locally fit either occurrence)`.
- rival_models: B001 creation/do is too broad; B002 has the better fit because both clauses require object-to-result syntax.
- grade: strong
- grade_rationale: Repetition, syntax, object continuity, and result complements converge independently.
- source_queries_or_rows_used: S105 QAC 105:2 and 105:5; attachment rows 105:2:a2/a4, 105:5:a1-a3; branches `ج ع ل` B001/B002/B004-B012.

### S105-CSU-08: Downward/Upon Targeting

- ayah_range: 105:3-4
- seed_type: constructional/morphosyntactic
- seed occurrences: `عليهم`, `ترميهم`, `بحجارة`
- generating_set: `(E: construction أرسل عليهم)`, `(E: construction ترميهم)`, `(E: ر م ي B001 projectile throwing)`, `(E: ح ج ر B003 hard stone)`
- selected_branches: `ر س ل` B001; `ر م ي` B001/B003; `ح ج ر` B003; non-branch attachments
- constructed_model: A vertical or superior targeting relation emerges from `عليهم`: something is sent upon them, then it throws them with hard objects. The repeated object pronoun keeps the target fixed while the subject shifts from divine sender to sent flock.
- freeze_point: End of 105:4.
- predictions_at_freeze: The target should be transformed into an inert result; no counter-action should remain.
- unused_features_tested: 105:5 final transformation.
- corroborators: `(C: 105:5 جعلهم object suffix continues target)`, `(C: final comparison has no agency left)`, `(C: attachments 105:3:a1, 105:4:a1, 105:4:a2)`
- constraints: `(K: no explicit lexical branch says vertical descent; this is from على plus sequence, not from root semantics alone)`.
- rival_models: A generic "against them" reading is primary; vertical descent is secondary but compatible with birds and throwing.
- grade: medium-strong
- grade_rationale: Strong morphosyntactic continuity; the directional image is constructional rather than branch-generated.
- source_queries_or_rows_used: attachment rows 105:3:a1, 105:4:a1-a2, 105:5:a1.

### S105-CSU-09: Scatter, Fragment, Consume

- ayah_range: 105:3-5
- seed_type: lexical convergence
- seed occurrences: `طيرًا`, `أبابيل`, `ترميهم`, `عصف`, `مأكول`
- generating_set: `(E: ط ي ر B002 spread after lightness)`, `(E: ء ب ل B003 scattered/successive groups)`, `(E: ر م ي B001 projection)`, `(E: ع ص ف B002 wind that scatters/breaks)`, `(E: ع ص ف B004 force that sweeps people away)`, `(E: ء ك ل B006 erosion/corruption)`
- selected_branches: `ط ي ر` B002; `ء ب ل` B003; `ر م ي` B001; `ع ص ف` B001/B002/B004; `ء ك ل` B006
- constructed_model: A dispersion avalanche forms: grouped aerial movement, projection of stones, then a closing comparison to scattered plant matter already eaten away. This does not replace the primary event but supplies motion geometry: released bodies, distributed impacts, fragmented remains.
- freeze_point: After linking 105:3-4 before 105:5.
- predictions_at_freeze: The endpoint should show loss of cohesion, brittleness, or dispersed residue.
- unused_features_tested: `كعصف مأكول`.
- corroborators: `(C: ع ص ف B001 exact chaff/residue)`, `(C: ء ك ل B001/B006 exact consumed/eaten-away adjective)`, `(C: أبَابِيل attachment as adjective or hal keeps distributed grouping active)`
- constraints: `(K: ع ص ف B002 wind is not explicitly in the ayah; it is a secondary simulation of the chaff result)`.
- rival_models: The concrete eaten-chaff model in CSU-05 is stronger than a wind-only destruction model.
- grade: medium-strong
- grade_rationale: Strong final lexical convergence; the wind/scatter mechanism is plausible but partly secondary.
- source_queries_or_rows_used: branches `ط ي ر`, `ء ب ل`, `ر م ي`, `ع ص ف`, `ء ك ل`; attachment rows 105:3:a3/a4 and 105:5:a2/a3.

## Exhaustive Seed Audit Catalog

Legend: `G` = generated or expanded a candidate above; `C` = corroborated after freeze; `K` = constrained/narrowed/terminated; `T` = terminated with no passage-local synthesis. Every accepted branch is listed for every rooted occurrence. `ج ع ل` is listed twice because 105:2 and 105:5 have different occurrence contexts.

### 105:1:2 `تَرَ` root `ر ء ي`

- B001 seeing by eye/basira: G in CSU-01; predicts inspectable sequence.
- B002 heart-opinion/thinking: G in CSU-01; supports reflective seeing of manner.
- B003 dream vision: T; no sleep/dream frame.
- B004 mutual facing/visibility: C weak; the hearer faces a displayed event, but no mutual encounter construction.
- B005 showing-off/riya: T; no human performative piety frame.
- B006 appearance/mirror: C weak; final residue is visible, but no mirror/beauty role.
- B007 menstruation sign: T; no purity/menstrual diagnostic frame.
- B008 jinn familiar: T; no soothsaying or companion-spirit role.
- B009 lung/breath organ: T; no respiratory role.
- B010 visible pregnancy: T; no pregnancy/birth role.
- B011 raised flag: T; no banner/signpost construction.
- B012 showing/making see: C weak to CSU-01; opening causes the hearer to see/consider.
- B013 araytaka alerting/inquiring: G in CSU-01; matches `ألم تر` as attention-opening.

### 105:1:3 `كَيْفَ` root `ك ي ف`

- No accepted branch row found in `resources/v4_branches.tsv`; treated as constructional seed. G in CSU-01 as manner-question. Attachment 105:1:a2/a3 makes it the indirect question and adverbial of `فعل`.

### 105:1:4 `فَعَلَ` root `ف ع ل`

- B001 causing/doing an act: G in CSU-01.
- B002 noble/good or evaluable deed: C weak; `فعل ربك` can receive evaluative force but the passage does not lexicalize generosity.
- B003 workers/craftsmen: T; no laborer class.
- B004 fabricated invention: T as local branch; could rival the plot theme but `فعل ربك` is not fabricated.
- B005 action between two: T; no reciprocal action at this word.
- B007 grammatical objects: K/C structural only; useful for attachment awareness, not lexical image.

### 105:1:5 `رَبُّكَ` root `ر ب ب`

- B001 lordship/ownership/mastery: C to CSU-01 and CSU-07; supplies authoritative agent.
- B002 repair, nurture, completion: C weak; the action completes a corrective process but nurture is not foregrounded.
- B003 learned/rabbani: T; no scholar role.
- B004 large groups: T; group roles are elsewhere (`أصحاب`, `أبابيل`).
- B005 stepchild/caretaker: T.
- B006 thick syrup/repairing container with rubb: T.
- B007 abiding/staying: T; no staying role.
- B008 clouds/rain: T; birds/stones not rain-clouds in local syntax.
- B009 recently delivered sheep/youth: T.
- B010 quiver/skin for lots: T, though projectile container is tempting; no quiver word.
- B011 covenant/protection: C weak; divine relation to addressee via suffix `ك`, but no covenant construction.
- B012 plant: T.
- B013 abundant water: T.
- B014 herd/cluster: T; grouping comes from `أبابيل`.
- B015 particle `rubba`: T.
- B016 need/knot/blessing: T.
- B017 chief sailor: T.

### 105:1:6 `أَصْحَابِ` root `ص ح ب`

- B001 companionship/possession: G in CSU-06.
- B002 preservation by companionship: K; no preservation succeeds for them.
- B003 submission/following after difficulty: C weak; their association with elephant may imply led/attached force, but not explicit.
- B004 making something accompany/keeping with: C weak; elephant accompanies identity label.
- B005 son becoming companion: T.
- B006 hide left with hair: T; no skin-processing role.
- B007 algae on water: T.
- B008 reddish color: T.

### 105:1:7 `الفِيل` root `ف ي ل`

- B001 weakness of opinion/faulty judgment: G secondary in CSU-06; subordinate to surface elephant.
- B002 hip flesh/vein: T.
- B003 hidden-object game: C very weak; analogical concealment for plot only, not local meaning.
- B004 elephant animal: G primary in CSU-06.

### 105:2:2 `يَجْعَلْ` root `ج ع ل`

- B001 making/creating/doing: C in CSU-02 and CSU-07, weaker than B002.
- B002 making X into a state: G in CSU-02 and CSU-07.
- B004 beginning to do: T; syntax is transitive with object/result, not inchoative.
- B005 wage/reward: T.
- B006 small palms: T.
- B007 cloth for lowering pot: T.
- B008 beetle: T.
- B009 female animal in heat: T.
- B010 ostrich chick: T.
- B011 place noun: T.
- B012 short, fat, stubborn: T.

### 105:2:3 `كَيْدَهُمْ` root `ك ي د`

- B001 severe handling/working at something: G in CSU-02; plot as strenuous operation.
- B002 plotting/deception/stratagem: G in CSU-02 and CSU-06.
- B003 struggling as the soul exits: C weak to final destruction, but not the plot's primary image.
- B004 war/fighting: Rival fork in CSU-02; military context but not the immediate object of `جعل`.
- B005 crow cry with effort: T.
- B006 slow fire from firestick: T; no ignition role.
- B007 vomiting: T.

### 105:2:5 `تَضْلِيل` root `ض ل ل`

- B001 deviation from guidance/path: G in CSU-02.
- B002 hiding/disappearance: G in CSU-02; plot vanishes into failure.
- B003 losing a thing: G in CSU-02; their plan becomes lost.
- B004 loss of memory/preservation: C weak; counters `صحب` B002 preservation.
- B005 lost animal in wasteland: K/T; animal-loss branch is too specific.

### 105:3:1 `أَرْسَلَ` root `ر س ل`

- B001 sending/release/opposite of holding: G in CSU-03 and CSU-08.
- B002 messenger/message: K weak; sent object is birds, not speech.
- B003 easy/soft movement: C weak; movement of sent flocks, but not central.
- B004 deliberateness/slow recitation: T; no slow speech/action cue.
- B005 successive groups/flocks: G in CSU-03.
- B006 milk/flowing yield: T.
- B007 familiarity/ease toward someone: T.
- B008 correspondence/paired worker: T.
- B009 widow receiving suitors: T.
- B010 ease/generous giving: T.
- B011 special names: short arrow/necklace/veins: K weak for projectile image but no local word selects it.

### 105:3:3 `طَيْرًا` root `ط ي ر`

- B001 birds/flying/lightness: G in CSU-03.
- B002 spreading after lightness: G in CSU-09.
- B004 wide-mouthed well: T.
- B005 agitation/flightiness/rage: C weak; hostile force is agitated, but birds are literal subject.
- B006 still birds as proverb: T; no stillness/proverb frame.

### 105:3:4 `أَبَابِيل` root `ء ب ل`

- B001 camels and herding: K weak; may echo animal mass against elephant, but local adjective is for birds.
- B002 sufficing without water: T.
- B003 groups/flocks in succession or scattering: G in CSU-03 and CSU-09.
- B004 heaviness/liability: C weak; their arrival brings burden on targets, but not local.
- B005 bundle of firewood: C weak analogical grouping; no firewood role.
- B006 monk/priest: T.
- B007 lump of dates: T.
- B008 place name: T.
- B009 tribe: T.

### 105:4:1 `تَرْمِيهِم` root `ر م ي`

- B001 throwing/casting/projecting: G in CSU-03, CSU-04, CSU-08.
- B002 exceeding/increase: T.
- B003 thing connected with throwing: C in CSU-04; stones fill thrown-object role.
- B004 cloud/pieces thrown as rain: Rival weak fork; aerial shower imagery, but stones not rain.
- B006 reaching an endpoint/decay: C weak; action ends in final residue.
- B007 travel toward a direction: C weak; directional targeting but not travel.
- B008 verbal accusation: T; no speech accusation.
- B009 inaccurate conjecture: T.

### 105:4:2 `حِجَارَة` root `ح ج ر`

- B001 prevention/enclosure: C secondary in CSU-04; hard objects impose stopping.
- B002 restraining mind: T.
- B003 hard stone: G in CSU-04 and CSU-08.
- B004 enclosed place: C weak; stones as bounded matter, not place.
- B005 lap/protection: T.
- B006 circle around something: C weak; possible surrounding volley image, not explicit.
- B007 protected mare: T.

### 105:4:4 `سِجِّيل` root `س ج ل`

- B001 full bucket/pouring out: C weak in CSU-04; supports poured volley as secondary image.
- B002 contest by alternating buckets/war fortunes: C weak; may echo reversal of war fortune, but not local.
- B003 abundant unrestricted pouring/giving: C weak; released shower only.
- B004 written register/document: C weak to a fixed/decreed-source simulation; constrained by `من` as material/source modifier.
- B006 full/long/relaxed organ: T.

### 105:5:1 `جَعَلَهُمْ` root `ج ع ل`

- B001 making/creating/doing: C in CSU-05/07, weaker than B002.
- B002 making X into a state/comparison: G in CSU-05 and CSU-07.
- B004 beginning to do: T.
- B005 wage/reward: T.
- B006 small palms: T.
- B007 pot-cloth: T.
- B008 beetle: T.
- B009 female animal in heat: T.
- B010 ostrich chick: T.
- B011 place noun: T.
- B012 short, fat, stubborn: T.

### 105:5:2 `عَصْف` root `ع ص ف`

- B001 chaff/husks/broken plant matter: G in CSU-05 and C in CSU-09.
- B002 strong wind scattering/breaking things: G secondary in CSU-09.
- B003 lightness/speed: C weak; fast destructive process.
- B004 force sweeping people away/destroying: G secondary in CSU-09.
- B005 earning livelihood by effort/cunning: K/T; "cunning" echoes `كيد` only remotely and does not fit final comparison.

### 105:5:3 `مَّأْكُول` root `ء ك ل`

- B001 eating/consuming food: G in CSU-05.
- B002 fruit/yield of tree or crop: C in CSU-05; plant residue frame.
- B003 share/provision: T.
- B004 consuming/taking wealth: T.
- B005 fire eating fuel/flame: C weak rival; destructive consumption, but no fire.
- B006 corrosion/being eaten away/corruption: G in CSU-05 and CSU-09.
- B007 prey/prepared for eating: G secondary in CSU-05.
- B009 corruption/slander among people: T.
- B010 accusation/handing someone over: T.
- B011 small group enough for one head: T.
- B012 strength/fullness of material/intellect: T.
- B013 vessel/place for eating: T.

## Constructional and Temporal Seeds

### CON-01: `أَلَمْ تَرَ كَيْفَ فَعَلَ`

- seed_type: constructional
- generating_set: `(E: interrogative negated perfective frame)`, `(E: ترى governs كيف-clause by attachment 105:1:a2)`, `(E: كيف adverbial of فعل by attachment 105:1:a3)`
- frozen_model: An opening demand to inspect the manner of an already-established divine act.
- predictions_at_freeze: A sequence explaining the manner should follow.
- corroborators: all following ayat answer by staged actions and outcomes.
- constraints: Does not by itself select the lexical mechanism.
- grade: strong.

### CON-02: `فَعَلَ رَبُّكَ بِأَصْحَابِ ٱلْفِيل`

- seed_type: constructional/morphosyntactic
- generating_set: `(E: ربك subject by attachment 105:1:a4)`, `(E: بأصحاب governed complement by 105:1:a6)`, `(E: الفيل idafa by 105:1:a7)`
- frozen_model: Divine agent acts upon/with respect to the elephant-companions.
- predictions_at_freeze: Later pronouns should preserve this group as target.
- corroborators: `كيدهم`, `عليهم`, `ترميهم`, `جعلهم`.
- grade: strong.

### CON-03: `جعل كيدهم في تضليل`

- seed_type: constructional
- generating_set: `(E: جعل transitive object كيدهم)`, `(E: في تضليل result-state complement)`
- frozen_model: Their plan is put into a state/field of misdirection/loss.
- predictions_at_freeze: Later clauses should show the same group acted upon, not merely their plan.
- corroborators: 105:3-5 pronoun chain.
- grade: strong.

### CON-04: `أرسل عليهم طيرا أبابيل`

- seed_type: constructional
- generating_set: `(E: أرسل + على target)`, `(E: طيرا direct object)`, `(E: أبابيل adjective/hal ambiguity for grouped manner)`
- frozen_model: A sent aerial medium is directed upon the target group in grouped/successive form.
- predictions_at_freeze: The birds should perform or carry an action.
- corroborators: 105:4 `ترميهم`.
- grade: strong.

### CON-05: `ترميهم بحجارة من سجيل`

- seed_type: constructional
- generating_set: `(E: ترميهم object suffix)`, `(E: بحجارة instrument complement)`, `(E: من سجيل kind/source modifier)`
- frozen_model: Targeting becomes projectile impact through hard instruments from a specified source/kind.
- predictions_at_freeze: Impact should yield material disintegration.
- corroborators: 105:5 comparison.
- constraints: `س ج ل` branch data does not license over-specific material claims.
- grade: medium-strong.

### CON-06: `فجعلهم كعصف مأكول`

- seed_type: constructional
- generating_set: `(E: جعلهم object)`, `(E: كعصف comparison complement)`, `(E: مأكول adjective modifying عصف)`
- frozen_model: Persons become a comparison-residue: eaten chaff.
- predictions_at_freeze: This should close the passage because the hostile agency is exhausted.
- corroborators: The surah ends here; no further action remains.
- grade: strong.

### TEMP-01: Abstract-to-Material Degradation Sequence

- seed_type: temporal
- generating_set: `(E: 105:1 attention to manner)`, `(E: 105:2 plot made lost)`, `(E: 105:3 sent grouped medium)`, `(E: 105:4 projectile mechanism)`, `(E: 105:5 residue closure)`
- frozen_model: The passage moves from cognitive inspection to hostile intention, then to external intervention, then to impact, then to inert remains.
- predictions_at_freeze: Shuffling would weaken the model; the order is explanatory.
- corroborators: The two `ج ع ل` occurrences frame the inner mechanism.
- grade: strong.

### TEMP-02: Pronoun Target Chain

- seed_type: morphosyntactic/temporal
- generating_set: `ربك` acts on `أصحاب الفيل`; `كيدهم`; `عليهم`; `ترميهم`; `جعلهم`
- frozen_model: The target group remains active across each stage while their agency decreases.
- predictions_at_freeze: Final target should be object, not subject.
- corroborators: 105:5 `جعلهم` makes them object of transformation.
- grade: strong.

## Branches Rejected as Non-Productive Families

The following branch families were visited and terminated repeatedly because they lacked passage-local roles: menstruation, pregnancy, lung, jinn familiar, monk/priest, pot-cloth, beetle, animal mating heat, ostrich chick, small palms, algae, reddish donkey color, hip-flesh, lost animal as a specific livestock category, milk flow, widow suitors, eating-vessel, accusation, slander, small-group idiom, protected mare, lap/custody, restraining intellect, and sailor-chief. These were not omitted; they are represented in the seed catalog above at their exact roots.

## Image Packet Catalog

### IMAGE-105-01

- Starting seed: `أَلَمْ تَرَ كَيْفَ فَعَلَ`
- Complete image: A hearer is made to inspect the manner of a divine act through a staged transformation sequence.
- Passage-order assembly: question -> plot lost -> flocks sent -> stones thrown -> eaten chaff.
- Participants and roles: divine agent; elephant-companions as target; their plot as first object; birds as sent medium; stones as instrument; chaff as residue.
- Operation / mechanism: making into loss, sending, throwing, making into residue.
- Direction / force / medium: upon them; aerial flocks; hard stones.
- Temporal development: abstract plan fails before bodily/material destruction closes.
- Outcome / closure: consumed plant debris; no active hostile role remains.
- Exact branch constituents: `ر ء ي` B001/B002/B013; `ف ع ل` B001; `ج ع ل` B002; `ك ي د` B002; `ض ل ل` B001-B003; `ر س ل` B001/B005; `ط ي ر` B001; `ء ب ل` B003; `ر م ي` B001; `ح ج ر` B003; `ع ص ف` B001; `ء ك ل` B001/B006.
- Unfilled roles, if any: material semantics of `سجيل` remain constrained by weak branch fit.
- Status: COMPLETE.

### IMAGE-105-02

- Starting seed: `كيدهم في تضليل`
- Complete image: A hostile plan is inserted into a field where path, visibility, retention, and control fail.
- Passage-order assembly: plot -> loss field -> same group targeted -> final residue.
- Participants and roles: plotters; plot; divine transformer; later aerial/projectile mechanism.
- Operation / mechanism: object-to-result transformation.
- Direction / force / medium: inward to a loss-state, then outward impact upon the plotters.
- Temporal development: their intention fails before their bodies are reduced.
- Outcome / closure: plan and people both lose coherence.
- Exact branch constituents: `ج ع ل` B002; `ك ي د` B001/B002; `ض ل ل` B001/B002/B003; later `ر م ي` B001; `ع ص ف` B001.
- Unfilled roles, if any: none.
- Status: COMPLETE.

### IMAGE-105-03

- Starting seed: `أرسل عليهم طيرا أبابيل`
- Complete image: Released aerial groups arrive successively/scattered upon a target and perform throwing.
- Passage-order assembly: sent upon them -> grouped birds -> throwing with stones -> result.
- Participants and roles: sender; birds/flocks; target group; stones.
- Operation / mechanism: release, grouping, projection.
- Direction / force / medium: from sender upon target by aerial medium.
- Temporal development: dispatch becomes action in next ayah.
- Outcome / closure: target transformed into residue.
- Exact branch constituents: `ر س ل` B001/B005; `ط ي ر` B001/B002; `ء ب ل` B003; `ر م ي` B001; `ح ج ر` B003.
- Unfilled roles, if any: none.
- Status: COMPLETE.

### IMAGE-105-04

- Starting seed: `كعصف مأكول`
- Complete image: Human power is reduced to plant residue already consumed or eaten away.
- Passage-order assembly: earlier target pronouns converge into final object `هم`; comparison supplies residue-state.
- Participants and roles: target group as object; chaff as comparison; eating/corrosion as completed process.
- Operation / mechanism: transformation into residue.
- Direction / force / medium: destructive reduction after projectile impact.
- Temporal development: closes the passage after agency is exhausted.
- Outcome / closure: complete inert residue.
- Exact branch constituents: `ج ع ل` B002; `ع ص ف` B001; `ء ك ل` B001/B006/B007; secondary `ع ص ف` B002/B004.
- Unfilled roles, if any: none.
- Status: COMPLETE.

