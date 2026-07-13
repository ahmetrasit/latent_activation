# Stage 1 Pass 1 — S100 comparator main lane

Assigned passage: S100  
Sacred Arabic source: `resources/quran/surah_100.json`  
Primary Arabic interval used for seeds: 100:1–100:11  
Opening context: `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ` appears in the sacred text as `verse_0`; QAC has no S100 ayah-0 rows, so it is not used for lexical seeding.

Resources consulted, within the prompt limits only:

- `resources/qac.sqlite`: schema inspected; S100:1–11 words and morphemes queried.
- `resources/attachments.tsv`: header and S100:1–11 rows queried.
- `resources/furuq_v4.sqlite`: schema inspected; uncontaminated branch images for S100:1–11 roots only.

No translations, tafsir, hadith, other output files, web sources, or external interpretation were used.

## Passage-root inventory

First rooted word: `وَٱلْعَٰدِيَٰتِ` at 100:1:1, root `ع د و`.

Rooted occurrences in QAC order:

`ع د و`, `ض ب ح`, `و ر ي`, `ق د ح`, `غ ي ر`, `ص ب ح`, `ث و ر`, `ن ق ع`, `و س ط`, `ج م ع`, `ء ن س`, `ر ب ب`, `ك ن د`, `ش ه د`, `ح ب ب`, `خ ي ر`, `ش د د`, `ع ل م`, `ب ع ث ر`, `ق ب ر`, `ح ص ل`, `ص د ر`, second `ر ب ب`, `خ ب ر`.

Unique uncontaminated root-branches returned: 173. Because `ر ب ب` occurs twice, the stricter occurrence × branch ledger contains 190 lexical seed entries. All seeds below were swept against the same S100 root dossiers; the “selected” field names only branches or structures that actually transformed, completed, or forked the seed image before freeze.

## Temporary recitation-state frame

The passage first builds a rapid chain of oath-scene activations:

1. `وَٱلْعَٰدِيَٰتِ ضَبْحًا`
2. `فَٱلْمُورِيَٰتِ قَدْحًا`
3. `فَٱلْمُغِيرَٰتِ صُبْحًا`
4. `فَأَثَرْنَ بِهِۦ نَقْعًا`
5. `فَوَسَطْنَ بِهِۦ جَمْعًا`

QAC and attachments give a tightly ordered structure: oath particle + active participle, accusative manner/time complements, repeated `فـ`, feminine plural agents, then finite plural actions with repeated `بِهِۦ`, direct object `نَقْعًا`, and direct object `جَمْعًا`.

The next state is an emphatic human predication:

6. `إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌۭ`
7. `وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ`
8. `وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ`

Then the passage reopens the earlier outer scene as an inward disclosure scene:

9. `أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ`
10. `وَحُصِّلَ مَا فِى ٱلصُّدُورِ`
11. `إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ`

The dominant reactivation trajectory is:

`rapid outward force → spark/eruption/dust → entry into a gathered center → human relational interior → buried/interior contents turned out and collected → divine inner knowledge`.

This is a secondary relational image only. It is not a replacement translation.

## Convergent image-branches

### F1. Kinetic charge becomes disclosure of what was hidden

Seed: 100:1:1 `وَٱلْعَٰدِيَٰتِ`, `ع د و B002` — `العَدْو والحَضْر`.

Initial image:

Running or rapid forward motion creates an expectation of bodily exertion, sound, friction, trace, and arrival into a target field.

Selected expansion before freeze:

- `(E: ض ب ح B001)` sound of panting/breath in running.
- `(E: ض ب ح B002)` extended running with limbs/stride.
- `(E: و ر ي B002)` hidden fire emerging from striking.
- `(E: ق د ح B001)` fire produced by striking.
- `(E: ص ب ح B004)` morning/day-of-attack/galloping morning frame.
- `(E: ث و ر B001)` emergence and spreading after stillness.
- `(E: ث و ر B002)` stirring dust/earth from its place.
- `(E: ن ق ع B004)` raised dust.
- `(E: و س ط B003)` entering or making the middle.
- `(E: ج م ع B002)` a gathered group.

Frozen model:

A rapid plural force advances with audible exertion, throws off sparks, breaks into the morning, raises matter from the ground, and reaches the center of a gathered body.

Predictions at freeze:

- Later material may reopen the image through buried earth, raised hidden contents, or a containing interior.
- A human or moral target may be introduced after the oath-scene.
- A knowledge or witnessing role may close the disclosure.
- The first five ayat should function as more than static scenery because their sequential `فـ` chain creates cumulative force.

Unused features tested after freeze:

100:6–11 roots; passive morphology in 100:9–10; `فِى ٱلْقُبُورِ` / `فِى ٱلصُّدُورِ`; repeated emphatic `إِنَّ/لَـ`; attachments for direct objects and prepositional complements; ayah-boundary shift from oath-chain to predication.

Corroborators:

- `(C: attachment 100:1 a2)` `ضَبْحًا` is manner attached to `ٱلْعَٰدِيَٰتِ`, so breath/sound is not a free-floating association.
- `(C: attachment 100:2 a1)` `قَدْحًا` specifies how the `مُورِيَات` produce the fire/spark action.
- `(C: sequence 100:1→100:5)` repeated `فـ` preserves temporal acceleration.
- `(C: بعثر B001)` later “turning soil / exposing buried” reactivates the dust-earth activation from `ث و ر` and `ن ق ع`.
- `(C: قبر B001)` supplies the buried container predicted by stirred earth.
- `(C: حصل B001)` collecting until the resultant content appears reactivates `ج م ع`.
- `(C: حصل B002)` extracting the inner/noble from a covering reactivates hidden-fire and hidden-content predictions.
- `(C: صدر B001)` supplies the bodily interior site.
- `(C: خبر B001)` closes with knowledge of the inner/bāṭin matter.

Constraints:

- `(K: oath syntax 100:1)` the initial scene is governed by an oath construction; the passage does not require identifying the runners beyond the Arabic forms supplied.
- `(K: no literal transfer)` the later graves/chests do not make the first five ayat a literal burial scene; they reactivate its relational structure of force, eruption, entry, and disclosure.

Rival forks:

- F1a: battlefield-like entry into a gathered body, supported by `ص ب ح B004`, `و س ط B003`, `ج م ع B002`.
- F1b: disclosure mechanics without battle emphasis, supported by `و ر ي B002`, `ق د ح B001`, `ث و ر B002`, `ب ع ث ر B001`, `ح ص ل B002`.

Final grade: strong.

Grade rationale:

The seed begins at the first rooted word and explains the ordered sequence from motion to sound, spark, morning, dust, middle-entry, and gathering. Later passive disclosure of graves and chests independently reactivates the early earth/dust/hidden-content mechanics, while `خ ب ر B001` gives closure.

### F2. Breath/sound pressure becomes inner disclosure

Seed: 100:1:2 `ضَبْحًا`, `ض ب ح B001` — sound of panting/breath.

Initial image:

The first heard cue is exerted breath or animal sound; it predicts a moving body, forceful continuation, and a later place where breath/chest/interior may become relevant.

Selected expansion before freeze:

- `(E: ع د و B002)` running gives the sound its moving carrier.
- `(E: ض ب ح B002)` extended running thickens sound into stride.
- `(E: و ر ي B002 + ق د ح B001)` frictional ignition follows exertion.
- `(E: ث و ر B001/B002)` matter erupts and is stirred from a resting place.
- `(E: ن ق ع B004)` dust becomes the visible trace of invisible force.

Frozen model:

Audible exertion becomes a trajectory of invisible internal force becoming visible outside as spark and raised dust.

Predictions at freeze:

- The passage may turn from outer exertion to an inner human site.
- Chest/interior language would strongly corroborate this path.
- Knowledge/witnessing should become relevant if hidden force is made manifest.

Unused features tested after freeze:

`ٱلْإِنسَٰن`, `حُبّ`, `صُّدُور`, `شَهِيد`, `عِلْم`, `خَبِير`, attachments 100:7–11.

Corroborators:

- `(C: صدر B001)` chest as bodily front/interior reactivates breath from `ض ب ح`.
- `(C: حبب B004)` heart-kernel / black center gives an inner affective locus, if tested after freeze.
- `(C: شهد B002)` explicit declaration/witnessing gives manifestation of what had been hidden.
- `(C: خبر B001)` knowledge of the inner matter closes the sound-to-interior path.

Constraints:

- `(K: ضَبْحًا attachment)` it is an accusative manner for the opening agents, not a free independent subject.
- `(K: no direct lexical identity)` `صُّدُور` does not mean “panting”; it only corroborates the bodily-interior prediction.

Final grade: medium-strong.

Grade rationale:

The sound seed reaches much of the same model as F1, but it depends on `ع د و` to supply the carrier and on later `ص د ر/خ ب ر` for full closure.

### F3. Hidden fire made visible by striking

Seed pair, independently convergent:

- 100:2:1 `فَٱلْمُورِيَٰتِ`, `و ر ي B002` — hidden fire from the fire-stick.
- 100:2:2 `قَدْحًا`, `ق د ح B001` — producing fire by striking.

Initial image:

Latent energy is inside or behind a surface, then contact/striking releases it as visible fire.

Selected expansion before freeze:

- `(E: ق د ح B001)` when the seed is `و ر ي B002`; `(E: و ر ي B002)` when the seed is `ق د ح B001`.
- `(E: ض ب ح B003)` fire marking/burning upper wood is a nearby fire-contact branch when selected after the spark seed.
- `(E: ث و ر B002)` stirring something from its place gives a non-fire analogue of forcing latent matter outward.
- `(E: ن ق ع B004)` raised dust supplies a visible trace released by force.

Frozen model:

The passage stages a hidden potency released by impact: fire from contact, dust from movement, and eventually contents from graves and chests.

Predictions at freeze:

- Later contents may be extracted from coverings.
- The hidden/visible contrast should recur in knowledge, witness, or inner-state language.
- The spark should be constrained by immediate syntax, not made the whole meaning of the passage.

Corroborators:

- `(C: حصل B002)` extraction of the inner valuable thing from its covering directly matches the release-from-cover prediction.
- `(C: بعثر B001)` covered/buried matter exposed from soil gives a larger earth-version of the same mechanism.
- `(C: صدر B001)` contents in chests are an interior target.
- `(C: خبر B001)` inner knowledge is the final cognitive analogue of the visible spark.
- `(C: sequence 100:2→100:10)` early ignition precedes later extraction, preserving temporal reactivation.

Constraints:

- `(K: attachment 100:2 a1)` `قَدْحًا` is a manner expression for `ٱلْمُورِيَٰت`; it cannot independently generate all later disclosure without the passage sequence.
- `(K: و ر ي B005 not selected)` concealment branch is related but the local form selects the ignition branch more tightly.

Final grade: strong.

Grade rationale:

This seed has precise local support and later independent corroboration from `ح ص ل B002`, `ب ع ث ر B001`, `ص د ر B001`, and `خ ب ر B001`.

### F4. Morning change / sudden arrival

Seed: 100:3:2 `صُبْحًا`, chiefly `ص ب ح B004`, with `ص ب ح B001`.

Initial image:

The scene is located at morning, with a branch that explicitly includes a morning attack / galloping morning frame.

Selected expansion before freeze:

- `(E: ص ب ح B004)` morning-attack / galloping-morning frame.
- `(E: ع د و B002)` running.
- `(E: ض ب ح B001)` breath-sound.
- `(E: و س ط B003 + ج م ع B002)` entry into a gathered middle.
- `(E: غ ي ر B003)` change of state/image if read as the branch available for the `مُغِيرَات` root.

Frozen model:

The passage’s early motion arrives at a threshold time, changing a hidden or quiet state into a visible, entered, gathered scene.

Predictions at freeze:

- A change from surface scene to human interior may follow.
- Knowledge at a decisive time may close the scene.

Corroborators:

- `(C: يومئذ non-branch evidence 100:11)` the closing time adverb echoes the time-marking function without using another `ص ب ح` branch.
- `(C: علم B001)` the passage later asks about knowing when the disclosure event occurs.
- `(C: خبر B001)` the closing knowledge role fits a time-indexed disclosure.

Constraints:

- `(K: غ ي ر dossier)` the uncontaminated `غ ي ر` branches returned here do not supply a direct local “raid” image; `غ ي ر B003` gives change/alteration only. Therefore the morning-attack model rests mostly on `ص ب ح B004`, sequence, and morphology.

Final grade: medium.

Grade rationale:

`ص ب ح B004` is locally strong, but the companion `غ ي ر` dossier is less directly aligned with the surface participle than the kinetic and disclosure roots are.

### F5. Dust/earth stirred from stillness reactivates as graves overturned

Seed pair, independently convergent:

- 100:4:1 `فَأَثَرْنَ`, `ث و ر B001/B002`.
- 100:4:3 `نَقْعًا`, `ن ق ع B004`.

Initial image:

Something latent or settled is stirred up: dust spreads outward and becomes visible after stillness.

Selected expansion before freeze:

- `(E: ث و ر B001)` emergence/spreading after stillness.
- `(E: ث و ر B002)` stirring earth/dust from its place.
- `(E: ن ق ع B004)` raised dust.
- `(E: ع د و B002)` moving force that causes the stirring.
- `(E: و س ط B003 + ج م ع B002)` stirred movement proceeds into a gathered middle.

Frozen model:

The early scene turns settled ground into visible airborne matter, then drives into a collected body.

Predictions at freeze:

- Later earth/burial language should reactivate the model strongly.
- A later gathering/collection word should reactivate `ج م ع`.
- The transition to human interior should be explained as a move from outer soil to inner contents.

Corroborators:

- `(C: بعثر B001)` overturning soil and exposing buried matter is the strongest backward reactivation of `ث و ر/ن ق ع`.
- `(C: قبر B001)` graves provide the buried-earth field.
- `(C: حصل B001)` collection/result after separation reactivates `ج م ع`.
- `(C: فِى ٱلْقُبُورِ / فِى ٱلصُّدُورِ parallel containers)` supplies the containment pattern predicted by buried matter.

Constraints:

- `(K: attachment 100:4 a2)` `نَقْعًا` is direct object of `أَثَرْنَ`; the dust is produced/raised, not itself the agent.
- `(K: no overextension)` not every later interior is dust; dust is the early visible analogue of hidden contents being exposed.

Final grade: strong.

Grade rationale:

This is one of the cleanest temporal reactivations: early stirred dust is not merely thematically similar to `بُعْثِرَ`; the later passive scene specifically returns to earth, burial, and exposure.

### F6. Entering the gathered center becomes collection of the interior

Seed pair, independently convergent:

- 100:5:1 `فَوَسَطْنَ`, `و س ط B003`.
- 100:5:3 `جَمْعًا`, `ج م ع B002/B001`.

Initial image:

The moving plural agents reach the middle of a gathered body. The image predicts center, containment, crowd/group, and possibly later collection of dispersed contents.

Selected expansion before freeze:

- `(E: و س ط B003)` entering/making the middle.
- `(E: ج م ع B002)` gathered group or army-like collective.
- `(E: ج م ع B001)` bringing separated items together.
- `(E: ع د و B002)` running force that reaches the middle.
- `(E: ث و ر B002 + ن ق ع B004)` dust/earth raised during entry.

Frozen model:

The first half culminates in penetration into the center of a gathered field.

Predictions at freeze:

- Later `collection` or `inner contents` should matter.
- A shift from physical middle to inward human center is likely.
- The passage should close only after the hidden center is known.

Corroborators:

- `(C: حصل B001)` collecting until the resultant thing appears.
- `(C: حصل B002)` extracting inner content from covering.
- `(C: صدر B001)` chest as the inner bodily field.
- `(C: خبر B001)` inner knowledge at closure.
- `(C: attachment 100:5 a2)` `جَمْعًا` is the direct object entered by `وَسَطْنَ`, so center-entry and gathered object are structurally linked.

Constraints:

- `(K: ج م ع B006/B007/B008 etc. rejected)` many `ج م ع` branches do not receive passage-local roles and are not blended into a general “gathering” cloud.

Final grade: medium-strong.

Grade rationale:

The model explains the closure of the first five ayat and is strongly reactivated by `ح ص ل`, but it depends on the earlier kinetic chain for its agent and force.

### F7. Human relational severance under a Lord becomes exposed

Seed cluster:

- 100:6:2 `ٱلْإِنسَٰنَ`, `ء ن س B001`.
- 100:6:3 `لِرَبِّهِۦ`, `ر ب ب B001/B002`.
- 100:6:4 `لَكَنُودٌ`, `ك ن د B002`, with `ك ن د B001`.

Initial image:

The passage shifts from plural moving agents to the human being, then predicates a relation to his `رَبّ` and a cutting/ingratitude disposition.

Selected expansion before freeze:

- `(E: ء ن س B001)` human / people as opposed to wildness or jinn.
- `(E: ر ب ب B001 100:6 occurrence)` lordship, ownership, mastery.
- `(E: ر ب ب B002 100:6 occurrence)` correction, nurturing, completion.
- `(E: ك ن د B002)` ingratitude for blessing/mutuality, remembering harms and forgetting blessings.
- `(E: ك ن د B001)` cutting/separation as a structural underside of ingratitude.

Frozen model:

The passage names a human interior whose relation to a sustaining/mastering Lord is cut or inverted by ingratitude.

Predictions at freeze:

- There should be evidence/witnessing of this state.
- A motive inside the human should be specified.
- Later disclosure of chest/interior should validate why the oath-scene led into the human predicate.
- The closing Lord-reference should return to `ر ب ب`.

Corroborators:

- `(C: شهد B002)` declaration/witness by knowledge supports exposure of the human state.
- `(C: حبب B002)` love fixed in the heart supplies motive.
- `(C: خير B001/B005)` desired benefit/giving provides the object-field of the motive and sharpens the ingratitude contrast.
- `(C: شدد B002)` intensity/strength makes the motive forceful.
- `(C: شدد B006)` miserliness is a possible after-freeze narrowing of intense attachment to goods.
- `(C: حصل B001/B002 + صدر B001)` contents of the chest are collected/extracted.
- `(C: ر ب ب B001/B002 100:11 occurrence)` the closing `رَبَّهُم` reactivates the relation from 100:6 at the end.
- `(C: خبر B001)` knowledge of the inner matter completes the exposure.

Constraints:

- `(K: no identification with opening agents)` the human predicate is not lexically identical with the opening plural agents; the relation is comparator/reactivation, not simple substitution.
- `(K: attachment 100:6 a3)` `لِرَبِّهِۦ` specifies the respect/target for `كَنُودٌ`; it is not a generic object of motion.

Final grade: strong.

Grade rationale:

The shift at 100:6 is abrupt but structurally explained: the opening kinetic disclosure becomes evidence for a hidden human relational state, which later chest/disclosure language makes explicit.

### F8. Witness, knowledge, and inner expertise close the avalanche

Seed cluster:

- 100:7:4 `لَشَهِيدٌ`, `ش ه د B001/B002`.
- 100:9:2 `يَعْلَمُ`, `ع ل م B001`.
- 100:11:5 `لَّخَبِيرٌۢ`, `خ ب ر B001`.

Initial image:

The passage requires not only motion and disclosure but a knower/witness who can register what becomes manifest.

Selected expansion before freeze:

- `(E: ش ه د B001)` presence with seeing.
- `(E: ش ه د B002)` declaration/witnessing by knowledge.
- `(E: ع ل م B001)` knowing as opposed to not knowing.
- `(E: خ ب ر B001)` knowledge of the inner/bāṭin matter.
- `(E: ح ص ل B001/B002 + ص د ر B001)` exposed inner contents provide the object of knowledge.

Frozen model:

The sequence moves from visible traces to testimonial and then divine inner knowledge.

Predictions at freeze:

- The passage should end after the epistemic role has no remaining hidden object.
- The final line should bind the Lord, the people, the day, and inner knowledge.

Corroborators:

- `(C: attachment 100:7 a2)` `عَلَىٰ ذَٰلِكَ` gives the matter over which witness applies.
- `(C: attachment 100:11 a3)` `بِهِمْ` supplies the object/reference for `خَبِيرٌ`.
- `(C: attachment 100:11 a4)` `يَوْمَئِذٍ` locates the closing knowledge temporally.
- `(C: passive morphology 100:9–10)` the hidden contents undergo disclosure before the final knowledge predication.

Constraints:

- `(K: شاهد not seed for all earlier motion)` witness/knowledge branches explain closure and reactivation; they do not generate the opening kinetic details alone.

Final grade: strong.

Grade rationale:

This cluster explains why the passage closes where it does: after outer motion, human motive, buried contents, and chest contents are all placed under `خ ب ر B001`.

### F9. Love of benefit as an inner binding force

Seed cluster:

- 100:8:2 `لِحُبِّ`, `ح ب ب B002/B004`.
- 100:8:3 `ٱلْخَيْرِ`, `خ ي ر B001/B005`.
- 100:8:4 `لَشَدِيدٌ`, `ش د د B002/B006`.

Initial image:

The human interior has a binding or intensifying attachment to what is good/beneficial/given.

Selected expansion before freeze:

- `(E: ح ب ب B002)` love fixed in the heart.
- `(E: ح ب ب B004)` heart-kernel / black center as a local inner locus.
- `(E: خ ي ر B001)` desirable good/benefit.
- `(E: خ ي ر B005)` generosity/gift.
- `(E: ش د د B002)` strength/intensity.
- `(E: ش د د B006)` possible narrowing toward miserliness.
- `(E: ك ن د B002)` ingratitude for blessing/mutuality supplies the moral inversion.

Frozen model:

The hidden human state is a strong inner attachment to benefit/gift that competes with gratitude toward the Lord.

Predictions at freeze:

- Inner contents should be exposed.
- The Lord relation should return at closure.
- Earlier kinetic intensity may be retrospectively mirrored in `ش د د`.

Corroborators:

- `(C: صدر B001)` the chest is the later container for this motive.
- `(C: حصل B001/B002)` the motive is collected/extracted rather than merely asserted.
- `(C: ر ب ب B001/B002 100:11 occurrence)` the Lord relation returns after motive disclosure.
- `(C: ش د د B003 after-freeze dimension)` “charge/running/carrying against an enemy” can weakly reactivate the opening rush if kept distinct from `ش د د B002/B006`.

Constraints:

- `(K: attachment 100:8 a2/a3)` `لِحُبِّ` relates `شَدِيد` to love, and `ٱلْخَيْرِ` is the genitive complement of `حُبّ`; the branch cannot be detached into a generic intensity scene.

Final grade: medium-strong.

Grade rationale:

This model is highly local for 100:8 and is completed by 100:10–11, but it does not by itself generate the opening oath-chain.

### F10. Passive disclosure of graves and chests

Seed cluster:

- 100:9:4 `بُعْثِرَ`, `ب ع ث ر B001`.
- 100:9:7 `ٱلْقُبُورِ`, `ق ب ر B001/B002`.
- 100:10:1 `وَحُصِّلَ`, `ح ص ل B001/B002`.
- 100:10:4 `ٱلصُّدُورِ`, `ص د ر B001`.

Initial image:

Buried and interior contents are overturned, exposed, collected, and extracted.

Selected expansion before freeze:

- `(E: ب ع ث ر B001)` turning soil / exposing buried things.
- `(E: ق ب ر B001)` grave as burial-place.
- `(E: ق ب ر B002)` hidden, depressed, enclosed quality.
- `(E: ح ص ل B001)` collecting until the resultant thing appears.
- `(E: ح ص ل B002)` extracting inner valuable content from covering.
- `(E: ص د ر B001)` chest/body front as the location of inner contents.

Frozen model:

The final event reveals both outer buried bodies and inner chest contents; nothing remains merely covered.

Predictions at freeze:

- The passage should close with a knowing authority.
- Earlier dust/stirring/spark/gathering should become meaningful again.

Corroborators:

- `(C: ث و ر B002)` early stirring of earth/dust is reactivated by `ب ع ث ر B001`.
- `(C: ن ق ع B004)` early raised dust supplies a visible analogue of opened earth.
- `(C: و ر ي B002 + ق د ح B001)` early hidden fire released from contact parallels hidden contents exposed.
- `(C: ج م ع B001/B002)` early gathering is reactivated by `ح ص ل B001`.
- `(C: خبر B001)` closure with inner knowledge.

Constraints:

- `(K: passive voice 100:9–10)` the agents of disclosure are not the opening plural agents; the relation is temporal reactivation, not direct agent identity.

Final grade: strong.

Grade rationale:

This cluster explains the strongest backward replay in the passage: the early scene’s dust, spark, and center-entry become a preview of later exposure and inner collection.

## Constructional, morphosyntactic, and temporal seeds

### Cns1. Oath-chain with repeated `فـ`

Seed: constructional/temporal sequence 100:1–5.

Generating set:

`وَ` oath opening; repeated `فـ`; active participle plural forms; accusative manner/time complements; finite plural verbs in 100:4–5.

Frozen model:

A cumulative event chain, not a static list.

Predictions:

Later material should reactivate the sequence as a process: force → trace → entry → disclosure.

Corroborators:

`(C: بعثر B001)`, `(C: حصل B001/B002)`, `(C: خبر B001)`.

Constraints:

`(K: oath construction)` the chain has rhetorical oath status and is not simply narrative subject matter.

Grade: strong.

### Cns2. Accusative manner/time/object progression

Seed: morphosyntactic pattern `ضَبْحًا`, `قَدْحًا`, `صُبْحًا`, `نَقْعًا`, `جَمْعًا`.

Generating set:

Attachments 100:1 a2, 100:2 a1, 100:3 a1, 100:4 a2, 100:5 a2.

Frozen model:

The first five ayat progressively fill manner, means, time, trace, and target.

Corroborators:

Later `ما في القبور / ما في الصدور` fills hidden objects after the first half filled visible objects.

Constraints:

The accusative nouns do not all have the same syntax; the model must preserve manner/time/direct-object differences.

Grade: medium-strong.

### Cns3. Repeated `بِهِۦ` in 100:4–5

Seed: morphosyntactic repeated prepositional pronoun.

Generating set:

Attachments 100:4 a1 and 100:5 a1: repeated `بِهِۦ` governed by `أَثَرْنَ` and `وَسَطْنَ`.

Frozen model:

The same event-medium or referential carrier links raising dust and entering the gathered center.

Corroborators:

`(C: بهِمْ 100:11 attachment a3)` weakly echoes `بـ` reference at closure, now attached to the humans before `خَبِير`.

Constraints:

The exact antecedent is not established by the permitted resources alone; keep this structural, not interpretive.

Grade: medium.

### Cns4. Emphatic human predication chain

Seed: `إِنَّ ... لَـ` pattern in 100:6–8 and 100:11.

Generating set:

QAC morphology: `إِنَّ`, emphatic `لَـ`, predicates `كَنُود`, `شَهِيد`, `شَدِيد`, `خَبِير`.

Frozen model:

The passage turns from oath activation into emphatically fixed predications, then closes by applying the final predication to `رَبَّهُم`.

Corroborators:

`(C: كند B002)`, `(C: شهد B002)`, `(C: شدد B002)`, `(C: خبر B001)`.

Constraints:

The repeated pronoun in 100:7–8 remains grammatically tied to the human predication; it should not be reassigned to the opening agents.

Grade: strong.

### Cns5. Parallel containers: `فِى ٱلْقُبُورِ` and `فِى ٱلصُّدُورِ`

Seed: constructional parallelism in 100:9–10.

Generating set:

Attachments 100:9 a3 and 100:10 a2: `فِى` complements specify what the relative `مَا` is inside.

Frozen model:

Outer burial container and inner bodily container are paired.

Corroborators:

`(C: قبر B001/B002)`, `(C: صدر B001)`, `(C: حصل B002)`, `(C: خبر B001)`.

Constraints:

The parallel is structural; it does not make graves and chests the same literal container.

Grade: strong.

### Cns6. Passive perfect disclosure in 100:9–10

Seed: passive morphology `بُعْثِرَ` and `حُصِّلَ`.

Generating set:

QAC voice: both are perfect passive; attachments identify `مَا` as passive subject.

Frozen model:

Hidden contents undergo disclosure without the passage foregrounding a human discloser.

Corroborators:

`(C: خبر B001)` supplies the knowing endpoint after disclosure.

Constraints:

The opening plural agents cannot be imported as the passive agents.

Grade: strong.

## Full lexical seed ledger

Compact ledger convention:

- Roots visited for every lexical seed: all S100 root dossiers listed in the inventory.
- Selected branches before freeze are shown in `E`.
- If `E: none`, the seed was allowed to die after the full cross-root sweep.
- `C/K tested` means the unused passage sequence, morphology, attachments, ayah boundaries, and later occurrences were tested after freeze.
- Branches not named in `E` or `C` were rejected for that seed as non-transforming or non-local.
- Rival forks are `none` unless named.

### 100:1:1 `وَٱلْعَٰدِيَٰتِ` — root `ع د و`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ع د و B001` | Boundary-crossing/overstepping. Frozen as a possible moral excess model. | `ك ن د B002`, `ش د د B006` | C: human ingratitude/intense attachment can be a relational excess. K: opening oath scene supplies running participle, not explicit ظلم. | medium |
| `ع د و B002` | Running/rapid advance. Frozen as F1 kinetic charge. | See F1 | See F1 | strong |
| `ع د و B003` | Enemy/hostility. Frozen as rival battle-coloring only. | `ص ب ح B004`, `ش د د B003`, `ج م ع B002` | C: gathered target and morning-attack branch. K: no explicit enemy noun in passage. | weak |
| `ع د و B004` | Passing beyond/exception/diversion. | `و س ط B003` weakly | C/K tested; no passage-local exception construction after seed. | unlikely |
| `ع د و B005` | Seeking redress against wrongdoer. | none | K: no judge/petition role before or after freeze. | unlikely |
| `ع د و B006` | Contagion/transfer of disease. | none | K: no disease-transfer role. | unlikely |
| `ع د و B007` | Distracting hindrances of time/evil. | `ك ن د B002` weakly | K: can color human diversion from Lord but not sequence-generating. | weak |
| `ع د و B008` | Sequential hunting catch. | none | K: no hunting frame or prey sequence. | unlikely |
| `ع د و B009` | Side/bank/edge. | none | K: `وَسَطْنَ` moves to middle, but no edge-bank role is supplied. | unlikely |
| `ع د و B010` | Hard uneven ground. | `ن ق ع B007` weakly | K: dust/ground exists but hard uneven ground does not organize passage. | unlikely |
| `ع د و B011` | Summer vegetation after spring. | none | K: no vegetation cycle. | unlikely |
| `ع د و B012` | Twisting/difficulty. | none | K: no local support. | unlikely |

### 100:1:2 `ضَبْحًا` — root `ض ب ح`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ض ب ح B001` | Panting/sound. Frozen as F2. | See F2 | See F2 | medium-strong |
| `ض ب ح B002` | Extended running stride. | `ع د و B002`, `ض ب ح B001`, `ث و ر B002`, `ن ق ع B004` | C: F1 sequence. K: serves manner more than independent passage model. | medium-strong |
| `ض ب ح B003` | Fire touching/burning upper wood. | `و ر ي B002`, `ق د ح B001` | C: spark sequence. K: local word is attached to running sound, so fire sense is secondary. | weak |
| `ض ب ح B004` | Slight blackening by fire/sun. | `ق د ح B001` weakly | K: no blackening role after freeze. | unlikely |
| `ض ب ح B005` | Ash. | none | K: dust exists, but ash is not locally supported. | unlikely |

### 100:2:1 `فَٱلْمُورِيَٰتِ` — root `و ر ي`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `و ر ي B001` | Inner disease / lung or belly injury. | `ص د ر B001` weakly | C: chest later. K: no disease/wound construction. | weak |
| `و ر ي B002` | Hidden fire coming from the stick. Frozen as F3. | See F3 | See F3 | strong |
| `و ر ي B003` | Successful/helping fire-stick. | `ق د ح B001`, `خ ي ر B005` weakly | K: help/success not strongly sequenced. | weak |
| `و ر ي B004` | Visible fat/plumpness. | none | K: no passage-local role. | unlikely |
| `و ر ي B005` | Concealing/placing behind appearance. | `بعثر B001`, `حصل B002` | C: later hidden contents exposed. K: local `مُورِيَات` with `قَدْحًا` selects ignition more tightly. | medium |
| `و ر ي B006` | Behind/beyond/other side. | none | K: no deictic behind/beyond role. | unlikely |
| `و ر ي B007` | Grandchild after son. | none | K: no kinship lineage role. | unlikely |
| `و ر ي B008` | Created beings on earth. | `ء ن س B001` weakly | K: too broad; does not transform sequence. | unlikely |

### 100:2:2 `قَدْحًا` — root `ق د ح`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ق د ح B001` | Fire by striking. Frozen as F3. | See F3 | See F3 | strong |
| `ق د ح B002` | Nicking/defecting wood or bone. | `ك ن د B001` weakly | K: cut/defect can color moral rupture, but no local object. | weak |
| `ق د ح B003` | Attacking lineage. | none | K: no lineage/nasab role. | unlikely |
| `ق د ح B004` | Worm/decay in tree/tooth. | none | K: no decay slot. | unlikely |
| `ق د ح B005` | Ladling from pot with effort. | `ح ص ل B001` weakly | K: extraction exists later, but vessel/ladle frame unsupported. | weak |
| `ق د ح B006` | Drinking cup. | none | K: no cup/drinking frame. | unlikely |
| `ق د ح B007` | Arrow-shaft / maysir lot. | `ر ب ب B010` weakly | K: lots/shafts not present; do not blend with spark. | unlikely |
| `ق د ح B008` | Lean horse / sunken eye. | `ض ب ح B002` weakly | K: horses/running possible by opening scene, but specific emaciation not supported. | weak |
| `ق د ح B009` | Tender plant tips. | none | K: no plant role. | unlikely |
| `ق د ح B010` | Deliberating an affair. | `ع ل م B001` weakly | K: cognitive deliberation not passage-local enough. | unlikely |

### 100:3:1 `فَٱلْمُغِيرَٰتِ` — root `غ ي ر`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `غ ي ر B001` | Provision/benefit/repair. | `خ ي ر B001`, `ر ب ب B002` weakly | K: not local to opening participle; better as distant human-benefit color. | weak |
| `غ ي ر B002` | Blood-money / substitute for retaliation. | none | K: no retaliation/diyah frame. | unlikely |
| `غ ي ر B003` | Change/alteration. Frozen as F4 support. | `ص ب ح B004`, `ع د و B002` | C: shift from scene to human predication. K: does not alone supply raid. | medium |
| `غ ي ر B004` | Jealous guarding of family. | none | K: no family/jealous role. | unlikely |
| `غ ي ر B005` | Otherness/difference/exception/negation. | `أفلا/لا` non-branch weakly | K: negation appears later, but not enough to build synthesis. | weak |

### 100:3:2 `صُبْحًا` — root `ص ب ح`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ص ب ح B001` | Dawn / first day. | `ع د و B002`, `غ ي ر B003` | C: time closure `يومئذ`. K: time marker alone not whole model. | medium |
| `ص ب ح B002` | Coming in the morning. | `ع د و B002` | C/K tested; local temporal support only. | weak |
| `ص ب ح B003` | Morning drink/meal. | none | K: no drink/feeding role. | unlikely |
| `ص ب ح B004` | Morning-attack / galloping morning. Frozen as F4. | See F4 | See F4 | medium-strong |
| `ص ب ح B005` | Lamp/sirāj. | `و ر ي B002`, `ق د ح B001` | C: fire/light path. K: no lamp noun. | weak |
| `ص ب ح B006` | Redness/beauty of face/hair. | none | K: no color/beauty role. | unlikely |
| `ص ب ح B007` | Morning sleep. | none | K: no sleep role. | unlikely |
| `ص ب ح B008` | Camel staying until morning. | none | K: no staying/late-rising role. | unlikely |
| `ص ب ح B009` | Specific morning circumstances. | `يومئذ` weakly | K: too temporal/generic. | weak |
| `ص ب ح B010` | Becoming/coming to be in a state. | `غ ي ر B003` weakly | K: state-change is general, not specific. | weak |

### 100:4:1 `فَأَثَرْنَ` — root `ث و ر`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ث و ر B001` | Eruption/spreading after stillness. Frozen as F5. | See F5 | See F5 | strong |
| `ث و ر B002` | Stirring dust/earth from place. Frozen as F5. | See F5 | See F5 | strong |
| `ث و ر B003` | Rage/violent confrontation. | `ع د و B003`, `ش د د B003` | C: possible battle-coloring. K: no explicit anger. | weak |
| `ث و ر B004` | Bull. | none | K: no bull/cattle role. | unlikely |
| `ث و ر B005` | Solid lump of aqit. | none | K: no food/lump role. | unlikely |
| `ث و ر B006` | Place/tribe/zodiac Taurus. | none | K: no proper-name role. | unlikely |
| `ث و ر B007` | Algae on water surface. | `ن ق ع B001` weakly | K: water-surface model not supported by local dust object. | unlikely |

### 100:4:3 `نَقْعًا` — root `ن ق ع`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ن ق ع B001` | Settled water / soaking vessel. | `ح ب ب B006` weakly | K: passage object is dust by stronger B004; water model dies. | unlikely |
| `ن ق ع B002` | Water that quenches thirst. | `خ ي ر B001` weakly | K: no thirst/quenching frame. | unlikely |
| `ن ق ع B003` | Food/slaughter/milk for arrival. | none | K: no food-arrival frame. | unlikely |
| `ن ق ع B004` | Raised dust. Frozen as F5. | See F5 | See F5 | strong |
| `ن ق ع B005` | Raised/continued sound. | `ض ب ح B001` | C: sound chain in opening. K: local object is dust-trace more than sound. | medium |
| `ن ق ع B006` | Fixed/deadly poison. | none | K: no poison role. | unlikely |
| `ن ق ع B007` | Easy flat ground. | `ع د و B010` weakly | K: ground exists, but no flatland role. | unlikely |
| `ن ق ع B008` | Experienced in safe routes/resources. | `ع ل م B001` weakly | K: too proverbial; no route-safety role. | unlikely |
| `ن ق ع B009` | Ugly reviling. | none | K: no insult/reviling role. | unlikely |

### 100:5:1 `فَوَسَطْنَ` — root `و س ط`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `و س ط B001` | Middle as just/best. | `خ ي ر B002` weakly | K: no justice/bestness predicate. | weak |
| `و س ط B002` | Middle place between edges. | `ج م ع B002`, `ح ص ل B001` | C: later inner/collected center. K: less dynamic than B003. | medium |
| `و س ط B003` | Entering/making the middle. Frozen as F6. | See F6 | See F6 | medium-strong |
| `و س ط B004` | Average between good and bad. | `خ ي ر B001` weakly | K: no evaluative middle. | unlikely |
| `و س ط B005` | Mediation between people. | none | K: no mediator role. | unlikely |
| `و س ط B006` | Cutting in half. | `ك ن د B001` weakly | K: cut model not locally attached. | weak |
| `و س ط B007` | Specific tent/camel. | none | K: no such object. | unlikely |

### 100:5:3 `جَمْعًا` — root `ج م ع`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ج م ع B001` | Bringing dispersed things together. Frozen as F6 support. | `و س ط B003`, `ح ص ل B001` | C: collection of chest contents. | medium-strong |
| `ج م ع B002` | Gathered group / crowd / army. Frozen as F6. | See F6 | See F6 | medium-strong |
| `ج م ع B003` | Firm resolve after opinions gather. | `ش د د B002` weakly | K: no counsel/plan scene. | weak |
| `ج م ع B004` | Gathering place/day/call. | `يومئذ` weakly | K: no named gathering place or call. | weak |
| `ج م ع B005` | Closed fist/grip. | `ش د د B001` weakly | K: no hand/grip role. | unlikely |
| `ج م ع B006` | Sexual union. | none | K: no marital/sexual frame. | unlikely |
| `ج م ع B007` | Woman retaining pregnancy/virginity. | none | K: no pregnancy/virginity frame. | unlikely |
| `ج م ع B008` | Shackle gathering hands to neck. | `ش د د B001` weakly | K: no restraint/shackle role. | unlikely |
| `ج م ع B009` | Whole/completion without loss. | `ح ص ل B001` | C: final resultant completeness. K: not first-half target alone. | medium |
| `ج م ع B010` | Strength/speed parts coming together. | `ع د و B002`, `ش د د B002` | C: kinetic chain. K: secondary to B002. | medium |
| `ج م ع B011` | Unnamed date-palm from seed. | none | K: no palm role. | unlikely |
| `ج م ع B012` | Large full vessel/pot. | none | K: no vessel role. | unlikely |
| `ج م ع B013` | Collusion/joining with another. | `ك ن د B002` weakly | K: no collusion role. | weak |

### 100:6:2 `ٱلْإِنسَٰنَ` — root `ء ن س`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ء ن س B001` | Human/persons opposed to wildness/jinn. Frozen as F7. | See F7 | See F7 | strong |
| `ء ن س B002` | Perceiving by sight/hearing/sensing. | `ش ه د B001`, `ع ل م B001` | C: witness/knowledge chain. K: not the surface branch of `الإنسان`. | medium |
| `ء ن س B003` | Familiarity removing loneliness. | `ر ب ب B002`, `ك ن د B002` | C: ingratitude breaks relation. K: no explicit comfort/companionship. | weak |
| `ء ن س B004` | Human-facing side of an animal/bow. | `و س ط B002` weakly | K: side/orientation not needed. | unlikely |
| `ء ن س B005` | Pupil / human image in eye. | `ش ه د B001` weakly | K: seeing image is remote; no eye noun. | weak |
| `ء ن س B006` | Self/intimate companion. | `ص د ر B001`, `ح ب ب B002` | C: inner self possible. K: not enough to generate sequence. | weak |

### 100:6:3 `لِرَبِّهِۦ` — root `ر ب ب`, first occurrence

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ر ب ب B001` | Lordship/ownership/mastery. Frozen as F7. | See F7 | See F7 | strong |
| `ر ب ب B002` | Nurture/repair/completion. Frozen as F7. | See F7 | See F7 | strong |
| `ر ب ب B003` | Rabbānī knowledge. | `ع ل م B001`, `خ ب ر B001` | C: knowledge closure. K: branch form not local to `رَبّ`. | weak |
| `ر ب ب B004` | Large groups/multitudes. | `ج م ع B002` weakly | K: group exists earlier, but Lord relation is singular possessive here. | unlikely |
| `ر ب ب B005` | Stepson/caretaker. | `ر ب ب B002` weakly | K: no family/custody role. | unlikely |
| `ر ب ب B006` | Thick rubb / food repaired with it. | none | K: no food-condiment role. | unlikely |
| `ر ب ب B007` | Staying/settling/continuing. | `ش د د B001` weakly | K: no residence/staying role. | weak |
| `ر ب ب B008` | Layered cloud. | none | K: no cloud/weather role. | unlikely |
| `ر ب ب B009` | Recently delivered ewe / newness. | none | K: no animal birth/newness role. | unlikely |
| `ر ب ب B010` | Container for arrow lots. | `ق د ح B007` weakly | K: no maysir/lot frame. | unlikely |
| `ر ب ب B011` | Covenant/protection. | `شهد B002` weakly | K: no explicit covenant term. | weak |
| `ر ب ب B012` | Specific plant remaining green. | none | K: no plant role. | unlikely |
| `ر ب ب B013` | Much water. | `ن ق ع B001` weakly | K: no water model. | unlikely |
| `ر ب ب B014` | Herd/flock. | `ج م ع B002` weakly | K: no herd. | unlikely |
| `ر ب ب B015` | Particle `رُبَّ`. | none | K: not the form here. | unlikely |
| `ر ب ب B016` | Need/knot/blessing. | `ك ن د B002` weakly | K: blessing fits ingratitude but branch is diffuse. | weak |
| `ر ب ب B017` | Chief of sailors. | none | K: no sea/navigation role. | unlikely |

### 100:6:4 `لَكَنُودٌ` — root `ك ن د`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ك ن د B001` | Cutting/separation. | `ر ب ب B001`, `ك ن د B002`, `ح ب ب B002` | C: relational rupture. K: literal cutting not supplied. | medium |
| `ك ن د B002` | Ingratitude for blessing/mutuality. Frozen as F7. | See F7 | See F7 | strong |
| `ك ن د B003` | Barren land that does not grow. | `خ ي ر B001`, `ر ب ب B002` weakly | K: no land/fruit frame, but refusal of benefit gives weak image. | weak |
| `ك ن د B004` | Name of Kindah tribe. | none | K: proper-name branch has no local role. | unlikely |

### 100:7:4 `لَشَهِيدٌ` — root `ش ه د`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ش ه د B001` | Presence with seeing. Frozen as F8 support. | `ء ن س B002`, `ع ل م B001` | C: witness/knowledge chain. | medium-strong |
| `ش ه د B002` | Declaration/witnessing by knowledge. Frozen as F8. | See F8 | See F8 | strong |
| `ش ه د B005` | Tongue/visible expression. | `ك ن د B002` weakly | K: no tongue/speech organ in passage. | weak |
| `ش ه د B006` | Birth discharge / signs of maturity. | none | K: no birth/maturity role. | unlikely |
| `ش ه د B007` | Honey in wax before pressing. | `ح ص ل B002` weakly | K: extraction analogy too remote; no honey/wax. | unlikely |
| `ش ه د B008` | Sign indicating time/state/quality. | `ع ل م B002`, `يومئذ` | C: sign/time role. K: secondary to B002. | medium |

### 100:8:2 `لِحُبِّ` — root `ح ب ب`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ح ب ب B001` | Seed/grain that grows. | `خ ي ر B001`, `ح ص ل B002` weakly | K: no agriculture. | unlikely |
| `ح ب ب B002` | Love fixed in heart. Frozen as F9. | See F9 | See F9 | medium-strong |
| `ح ب ب B003` | Praise / extreme desire formula. | `خ ي ر B001`, `ش د د B002` | C: desire intensity. K: formulaic praise not local. | weak |
| `ح ب ب B004` | Heart-kernel / black center. Frozen as F9 support. | `ح ب ب B002`, `ص د ر B001`, `ح ص ل B002` | C: inner chest collection. | medium-strong |
| `ح ب ب B005` | Camel staying from weakness. | none | K: opening motion opposes this stillness; no lameness role. | unlikely |
| `ح ب ب B006` | Drinking until full. | `ن ق ع B002` weakly | K: no drinking/thirst frame. | unlikely |
| `ح ب ب B007` | Large jar. | none | K: no jar/container beyond later `في`; too remote. | unlikely |
| `ح ب ب B008` | Water bubbles/waves. | none | K: no water surface. | unlikely |
| `ح ب ب B009` | Teeth like ordered pearls. | none | K: no teeth/mouth role. | unlikely |
| `ح ب ب B010` | Small/short body. | none | K: no size role. | unlikely |
| `ح ب ب B011` | Useless sparks. | `و ر ي B002`, `ق د ح B001` | C: spark echo. K: “useless” not local, and 100:2 already supplies stronger spark branch. | weak |
| `ح ب ب B012` | Snake/devil. | none | K: no snake/devil role. | unlikely |

### 100:8:3 `ٱلْخَيْرِ` — root `خ ي ر`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `خ ي ر B001` | Desired good/benefit. Frozen as F9 support. | `ح ب ب B002`, `ش دد B002`, `ك ن د B002` | C: motive and ingratitude relation. | medium-strong |
| `خ ي ر B002` | Excellence/choice/virtue. | `و س ط B001` weakly | K: no explicit choosing or superiority role. | weak |
| `خ ي ر B003` | Choosing/seeking good. | `ح ب ب B002` weakly | K: passage says love, not choice-process. | weak |
| `خ ي ر B005` | Generosity/gift. Frozen as F9 support. | `ر ب ب B002`, `ك ن د B002`, `ح ب ب B002` | C: ingratitude toward given benefit. | medium |
| `خ ي ر B006` | Driving animal from burrow. | `ب ع ث ر B001` weakly | K: hidden/extracted is too remote; no animal burrow role. | unlikely |

### 100:8:4 `لَشَدِيدٌ` — root `ش د د`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ش د د B001` | Tightening knots/bonds. | `ح ب ب B002`, `ك ن د B001` | C: strong attachment. K: no actual rope/bond. | medium |
| `ش د د B002` | Strength/intensity/firmness. Frozen as F9. | See F9 | See F9 | medium-strong |
| `ش د د B003` | Charging/running against enemy. | `ع د و B002`, `ص ب ح B004` | C: reactivates opening rush if after-freeze. K: in 100:8 it modifies love, not attack. | medium |
| `ش د د B004` | Reaching maturity/strength. | `ء ن س B001` weakly | K: no maturity process. | unlikely |
| `ش د د B005` | Height of day. | `ص ب ح B001` weakly | K: opening uses morning, not high noon. | unlikely |
| `ش د د B006` | Miserliness. Frozen as F9 narrowing. | `ح ب ب B002`, `خ ي ر B001`, `ك ن د B002` | C: motive/ingratitude. K: not the only meaning of `شديد`. | medium |

### 100:9:2 `يَعْلَمُ` — root `ع ل م`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ع ل م B001` | Knowing / perceiving. Frozen as F8. | `ش ه د B002`, `خ ب ر B001`, `ح ص ل B001` | C: disclosure chain. | strong |
| `ع ل م B002` | Mark/sign/guide. | `ش ه د B008`, `ن ق ع B004` weakly | C: visible traces can mark hidden force. K: not the local verb sense. | medium |
| `ع ل م B004` | Cleft in upper lip. | none | K: no body-defect role. | unlikely |
| `ع ل م B005` | Large water. | `ن ق ع B001` weakly | K: no water model. | unlikely |
| `ع ل م B006` | Hawk/falcon. | none | K: no bird role. | unlikely |
| `ع ل م B007` | Male hyena. | none | K: no hyena role. | unlikely |

### 100:9:4 `بُعْثِرَ` — root `ب ع ث ر`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ب ع ث ر B001` | Turning soil / exposing buried. Frozen as F10. | See F10 | See F10 | strong |
| `ب ع ث ر B002` | Scattering goods / mixing one over another. | `ج م ع B001`, `ح ص ل B001` | C: collection after dispersion. K: local complement is graves, so B001 dominates. | medium |
| `ب ع ث ر B003` | Demolishing basin, bottom over top. | `ق ب ر B002` weakly | K: inversion image present but no basin. | weak |

### 100:9:7 `ٱلْقُبُورِ` — root `ق ب ر`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ق ب ر B001` | Grave / burial. Frozen as F10. | See F10 | See F10 | strong |
| `ق ب ر B002` | Hidden/depressed/enclosed. Frozen as F10 support. | `ب ع ث ر B001`, `ح ص ل B002`, `ص د ر B001` | C: hidden interior paired with chests. | medium-strong |
| `ق ب ر B003` | Lark/qubbar bird. | none | K: no bird role. | unlikely |
| `ق ب ر B004` | Nose-tip in anger. | none | K: no anger/nose role. | unlikely |

### 100:10:1 `وَحُصِّلَ` — root `ح ص ل`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ح ص ل B001` | Collecting until resultant appears. Frozen as F10. | See F10 | See F10 | strong |
| `ح ص ل B002` | Extracting inner valuable from covering. Frozen as F10. | See F10 | See F10 | strong |
| `ح ص ل B003` | Residue/chaff after separation. | `ك ن د B002` weakly | K: outcome of sorting possible, but not local enough. | weak |
| `ح ص ل B004` | Bird crop where food gathers. | `ص د ر B001` weakly | K: bodily container, but no bird/food. | unlikely |
| `ح ص ل B005` | Unhardened dates on palm. | none | K: no dates/palm. | unlikely |
| `ح ص ل B006` | Horse belly pain from eating soil. | `ع د و B002`, `ن ق ع B004` weakly | K: horse/soil echo is too remote and pathological. | unlikely |

### 100:10:4 `ٱلصُّدُورِ` — root `ص د ر`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ص د ر B001` | Chest/breast and what connects to it. Frozen as F10. | See F10 | See F10 | strong |
| `ص د ر B002` | Front/top/first part. | `و س ط B002`, `ح ص ل B001` | C: inner/front body. K: `في الصدور` favors chest. | medium |
| `ص د ر B003` | Departing from watering-place after arrival. | `ص ب ح B003`, `ن ق ع B002` weakly | K: water/departure model unsupported. | unlikely |
| `ص د ر B004` | Source/origin from which acts issue. | `خ ب ر B001`, `ح ب ب B002` | C: inner source of human acts. K: grammatical root branch not local surface. | medium |
| `ص د ر B005` | Confiscating wealth. | `خ ي ر B001` weakly | K: no confiscation role. | unlikely |
| `ص د ر B006` | Portion of a thing. | `ح ص ل B001` weakly | K: too generic. | unlikely |

### 100:11:2 `رَبَّهُم` — root `ر ب ب`, second occurrence

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `ر ب ب B001` | Lordship/ownership/mastery at closure. | `خ ب ر B001`, `ر ب ب B001 100:6`, `ك ن د B002` | C: reactivates 100:6 `لربه`; closes relational arc. | strong |
| `ر ب ب B002` | Nurture/repair/completion at closure. | `خ ب ر B001`, `ر ب ب B002 100:6`, `ك ن د B002` | C: ingratitude toward the one who nurtures is exposed. | strong |
| `ر ب ب B003` | Rabbānī knowledge. | `ع ل م B001`, `خ ب ر B001` | C: knowledge closure. K: branch form remote. | medium |
| `ر ب ب B004` | Multitudes/groups. | `ج م ع B002` weakly | K: plural pronoun `هم` exists, but branch does not organize closure. | weak |
| `ر ب ب B005` | Stepson/caretaker. | none | K: no family/custody role. | unlikely |
| `ر ب ب B006` | Thick rubb / repaired food. | none | K: no food role. | unlikely |
| `ر ب ب B007` | Staying/settling/continuing. | `يومئذ` weakly | K: temporal closure, not staying. | weak |
| `ر ب ب B008` | Layered cloud. | none | K: no cloud role. | unlikely |
| `ر ب ب B009` | Recent-birth ewe/newness. | none | K: no animal birth role. | unlikely |
| `ر ب ب B010` | Container of arrow lots. | `ق دح B007` weakly | K: lots absent. | unlikely |
| `ر ب ب B011` | Covenant/protection. | `شهد B002`, `كند B002` weakly | K: possible relational coloring, no explicit covenant. | weak |
| `ر ب ب B012` | Green plant. | none | K: no plant role. | unlikely |
| `ر ب ب B013` | Much water. | none | K: no water model. | unlikely |
| `ر ب ب B014` | Herd/flock. | none | K: no herd role. | unlikely |
| `ر ب ب B015` | Particle `رُبَّ`. | none | K: not the form. | unlikely |
| `ر ب ب B016` | Need/knot/blessing. | `كند B002`, `خ ي ر B005` weakly | K: blessing/gift relation possible but diffuse. | weak |
| `ر ب ب B017` | Chief of sailors. | none | K: no nautical role. | unlikely |

### 100:11:5 `لَّخَبِيرٌۢ` — root `خ ب ر`

| Seed | Initial image and frozen model | E | C/K tested after freeze | Grade |
| --- | --- | --- | --- | --- |
| `خ ب ر B001` | Knowledge of report and inner matter. Frozen as F8/F10 closure. | See F8 and F10 | See F8 and F10 | strong |
| `خ ب ر B002` | Soft/low moist land. | `ن قع B001` weakly | K: no moist-land model. | unlikely |
| `خ ب ر B003` | Cultivating land by sharecropping. | `خ ي ر B001` weakly | K: no cultivation role. | unlikely |
| `خ ب ر B004` | Full wineskin / abundant she-camel. | none | K: no wineskin/camel abundance role. | unlikely |
| `خ ب ر B005` | Soft plant/hair/foam. | none | K: no soft plant or foam. | unlikely |
| `خ ب ر B006` | Dividing meat/share. | `ج م ع B001` weakly | K: no meat/share division. | unlikely |

## Branches most consistently rejected

The following branch families repeatedly failed because they lacked a passage-local role after full sweep:

- Proper names, tribes, zodiac, or place-name branches: `ث و ر B006`, `ك ن د B004`, etc.
- Animal/object branches without local support: bull, lark, hyena, snake, bird-crop, cup, pot, jar, tent, sailor-chief.
- Water/food/plant submodels, except as weak analogies, because the local opening object is `نَقْعًا` by the dust branch and the later containers are graves/chests.
- Kinship, pregnancy, sexuality, lineage, blood-money, and maysir branches, because no local roles or attachments support them.

These refusals are part of the audit: they were not blended into generalized meanings.

## Final synthesis

The strongest compact structure is a temporally conditioned disclosure model:

`running force → breath → spark → dawn arrival → stirred dust → penetration of a gathering → human ingratitude before his Lord → witness/motive/intensity → graves overturned → chest contents collected → Lord’s inner knowledge`.

The early oath-scene supplies motion, force, friction, eruption, trace, and center-entry. The middle predication supplies the human relational interior. The last three ayat reactivate the first five by turning the same relational geometry inward and eschatologically: what was hidden in earth and in chests is exposed, collected, and known. The passage closes exactly when the hidden object has no remaining concealment under `خ ب ر B001`.
