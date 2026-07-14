# S113 Stage 1 Pass 2 - Temporally Conditioned Reactivation

Assigned passage: S113, ayat 1-5.
Sacred Arabic text source: `resources/quran/surah_113.json`.
Prompt: `v1/prompts/stage1.md`.

## Pass 2 Restart Note

Root cause of the Pass 1 limitation: Pass 1 collected the S113 root inventory and branch dossiers, then moved too quickly into high-level convergences. It did not multiply the work by every eligible occurrence x accepted branch, and it treated several word groups as already promising instead of restarting from the first rooted word and giving the same deep lexical treatment to every seed.

Correction in this pass: the sweep restarts at the first rooted passage word, `قُلْ`, and treats every accepted branch of every passage root as a lexical seed at each eligible occurrence. It also initiates separate constructional, morphosyntactic, and temporal/acoustic seed passes. Basmala material is used only as opening-context corroboration or constraint, never as a generating seed.

Resource anomaly: the named SQLite files `resources/qac.sqlite` and `resources/furuq_v4.sqlite` are present in this workspace but zero-byte. To complete the required Stage 1 work, this pass used the local copied TSV mirrors present beside them: `resources/qac_root_ayah.tsv` for QAC-derived root/word/ayah rows and `resources/v4_branches.tsv` for accepted v4 branch images. No translation was used.

## Sacred Text And Sequence

Opening context:

- 0: `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`

Assigned interval:

- 113:1 `قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ`
- 113:2 `مِن شَرِّ مَا خَلَقَ`
- 113:3 `وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ`
- 113:4 `وَمِن شَرِّ ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ`
- 113:5 `وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ`

Passage root sequence, excluding unrooted particles:

`ق و ل -> ع و ذ -> ر ب ب -> ف ل ق -> ش ر ر -> خ ل ق -> ش ر ر -> غ س ق -> و ق ب -> ش ر ر -> ن ف ث -> ع ق د -> ش ر ر -> ح س د -> ح س د`

Basmala opening-context roots:

`س م و; ء ل ه; ر ح م; ر ح م`

## Structural Rows Used

Attachment rows used as structural evidence:

- `113:1 a1`: `أَعُوذُ بِرَبِّ ٱلْفَلَقِ` is the quoted complement of `قُلْ`.
- `113:1 a2`: `رَبِّ` is governed by prefixed `بـ` as prepositional complement of `أَعُوذُ`.
- `113:1 a3`: `ٱلْفَلَقِ` is genitive complement in `بِرَبِّ ٱلْفَلَقِ`.
- `113:2 a1`: `مَا خَلَقَ` specifies `شَرِّ` by genitive/free-relative attachment.
- `113:2 a2`: `مَا` is object of `خَلَقَ`.
- `113:3 a1`: `غَاسِقٍ` is genitive complement in `شَرِّ غَاسِقٍ`.
- `113:3 a2`: `إِذَا وَقَبَ` temporally qualifies `غَاسِقٍ`.
- `113:4 a1`: `ٱلنَّفَّٰثَٰتِ` is genitive complement in `شَرِّ ٱلنَّفَّٰثَٰتِ`.
- `113:4 a2`: `ٱلْعُقَدِ` is governed by `فِى` as complement of `ٱلنَّفَّٰثَٰتِ`.
- `113:5 a1`: `حَاسِدٍ` is genitive complement in `شَرِّ حَاسِدٍ`.
- `113:5 a2`: `إِذَا حَسَدَ` temporally qualifies `حَاسِدٍ`.

## Branch Dossiers Read

Each root dossier was read as continuous branch-preserving prose. Only accepted, uncontaminated v4 branches were used.

### Passage Roots

- `ق و ل`: B001 speech by articulation; B002 tongue as instrument; B003 frequent speaker; B004 possessor of authoritative speech; B005 false attribution or saying what was not; B006 drawing speech to oneself; B007 circulating public saying; B008 striking stick for qillah; B009 negotiation; B010 imposing judgment; B011 saying as supposition; B012 inner unexpressed saying; B013 saying as belief/doctrine; B014 a thing's indication; B015 sincere care for something; B016 definition or limit.
- `ع و ذ`: B001 refuge and protection; B002 protective charm/ruqyah/amulet; B003 newly delivered female clinging to young; B004 adhesion and staying in a shelter; B005 mark/place of collar on horse; B006 escape after threat short of completion; B007 mutual refuge or mutual default in war; B008 avoidance out of dislike.
- `ر ب ب`: B001 lordship, ownership, mastery; B002 repairing, nurturing, completing; B003 rabbinic learning; B004 large groups; B005 fostered child/caretaker; B006 thick rubb used for repair; B007 staying, abiding, duration; B008 layered cloud; B009 fresh post-birth or youth; B010 container of arrows; B011 covenant/protection pact; B012 green plant; B013 abundant water; B014 herd/group; B015 grammatical particle rubba; B016 need, firm knot, blessing; B017 chief of sailors.
- `ف ل ق`: B001 splitting/opening between two things; B002 daybreak and clarification; B003 emergence of creation from splitting; B004 low gap between elevations; B005 prisoner stocks; B006 calamity/wondrous thing; B007 army/corps.
- `ش ر ر`: B001 evil/badness; B002 spreading in sun to dry; B003 flying sparks; B004 cutting/shredding and shaken remnants from the mouth; B005 dripping fat from roast; B006 dangling tails/weights; B007 throwing one's whole self/concern onto something; B009 mosquito-like facial nuisance; B010 youthful drive/greed; B011 quarrel; B012 plant name.
- `خ ل ق`: B001 measuring/estimating before action; B002 creating/bringing into existence; B003 complete form and visible proportion; B004 inner nature/disposition; B005 fitness/readiness; B007 invented false speech; B008 smooth hard surface; B009 worn-out cloth; B010 perfume/coating; B011 hollow/pit holding water; B012 sealed hard closure.
- `غ س ق`: B001 entering darkness of night; B003 eye darkening or losing light; B004 flowing/pouring, including night pouring over mountains; B005 food impurities.
- `و ق ب`: B001 pit/hole where something disappears; B002 entering a hollow or darkness descending and hiding; B003 animal sound; B004 hunger falling on people; B005 household odds and ends; B006 continuous travel day and night; B007 shell/amulet.
- `ن ف ث`: B001 slight spittle/breath from mouth, including charm-workers blowing into knots; B002 wound emitting blood; B003 chest expelling what is inside.
- `ع ق د`: B001 tying ends and sensory knots; B002 binding covenant/contract; B003 thickening liquid/solidifying; B004 acquiring estate/property; B005 dense vegetation/pasture; B006 firmness of heart/opinion; B007 tongue-tie/obscure speech; B008 piled sand/contracted cloud; B009 cluster of grapes; B010 twisting animal limb; B011 compact body; B012 contracted anger/character; B013 magic knots/incantations; B014 counting on fingers; B015 close position; B016 encircling/enclosure; B017 turning the neck to someone for refuge.
- `ح س د`: B001 wishing removal of another's blessing; B002 emulation/admiring desire without removal.

### Opening-Context Dossiers

- `س م و`: B001 height/elevation; B002 visible elevated person or thing; B003 mounting motion; B004 sky/what is above and shades; B005 name/designation; B006 going out to hunt; B007 rivalry; B008 good repute.
- `ء ل ه`: B001 worship and one worshiped; B002 divine name in oath/call.
- `ر ح م`: B001 mercy/tenderness; B002 kinship/womb-relation; B003 womb as place of growth; B004 womb pain after birth.

## Candidate Synthesis Units

### candidate_id: S113-ST1P2-C01

ayah_range: 113:1-5

seed_type: lexical

seed: `113:1:1 قُلْ`, `ق و ل B001`

short title: Commanded protective utterance opens the whole sequence.

generating_set: `(E: ق و ل B001 articulated speech)` -> `(E: ع و ذ B001 refuge)` -> `(E: ر ب ب B001 lord/owner)` -> `(E: ف ل ق B002 daybreak/clarification)`.

selected_branches: `ق و ل B001`, `ع و ذ B001`, `ر ب ب B001`, `ف ل ق B002`.

constructed_model: The first cue is not private dread but a commanded utterance. The hearer is made to produce a protective speech act. The speech act moves immediately into seeking refuge, and the refuge is anchored not in a generic object but in the master of the daybreak/splitting. The developing image is a recited protective boundary: command -> voiced appeal -> protected authority -> opening light.

freeze_point: after `بِرَبِّ ٱلْفَلَقِ`.

predictions_at_freeze:

- Later material should be threats from which refuge is sought.
- The threats should be framed as separable from the protected speaker.
- If `فلق` is active as daybreak/opening, darkness or enclosed harm should later become relevant.
- The repeated syntax should maintain the opening refuge frame rather than replace it.

unused_features_tested: repeated `مِن شَرِّ`, `مَا خَلَقَ`, `غَاسِقٍ إِذَا وَقَبَ`, `ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ`, `حَاسِدٍ إِذَا حَسَدَ`, basmala.

corroborators: `(C: attachment 113:1 a1 quoted complement)`, `(C: repeated من شر in 113:2-5 supplies objects of refuge)`, `(C: غ س ق B001 darkness after فلق)`, `(C: و ق ب B002 entering/descent of darkness)`, `(C: basmala opening-context ء ل ه B002 divine naming/call)`, `(C: basmala opening-context ر ح م B001 mercy as protective divine-source frame)`.

constraints: `(K: قُلْ is imperative quote frame, not independent magic formula)`, `(K: ع و ذ remains first-person seeking refuge, not autonomous warding object unless B002 is separately seeded)`.

temporal_reactivation_notes: `فلق` is first heard as refuge-title. When `غاسق إذا وقب` arrives, the opening/daybreak branch is reactivated backward as the counter-edge to entering darkness. The three later `ومن شر` units repeatedly reactivate `أعوذ`.

rival_models: `ق و ل B005` false speech, `ق و ل B012` inner speech, and `ع و ذ B002` charm-object models.

grade: strong

grade_rationale: It uses the actual imperative speech syntax, the first-person refuge verb, the idafa title, and the later repeated threat complements. Independent corroboration comes from syntax, repetition, and dark-entering imagery.

source_queries_or_rows_used: QAC TSV S113 root rows; attachment rows `113:1 a1-a3`, `113:2-5` threat rows; v4 branches listed above.

### candidate_id: S113-ST1P2-C02

ayah_range: 113:1-3

seed_type: lexical

seed: `113:1:4 ٱلْفَلَقِ`, `ف ل ق B002`

short title: Dawn/opening as counter-force to descending darkness.

generating_set: `(E: ف ل ق B002 daybreak/clarification)` -> `(E: غ س ق B001 entering darkness)` -> `(E: و ق ب B002 entering hollow/descent until hidden)`.

selected_branches: `ف ل ق B002`, `غ س ق B001`, `و ق ب B002`.

constructed_model: The seed creates an image of daybreak or clarifying opening. Later, the darkening one and its entering/descent do not merely add a threat; they reactivate the opening as the reverse motion. The passage sets a protected appeal to the Lord of opening against a timed ingress of darkness.

freeze_point: after constructing the dawn/darkness opposition at 113:3.

predictions_at_freeze:

- Harm should appear as something that moves inward, descends, conceals, or enters a bound space.
- Protection should remain external to the harmful medium.
- Later threats may preserve the ingress/penetration pattern in another mode.

unused_features_tested: `نفث`, `عقد`, `حاسد إذا حسد`, repeated `من شر`, basmala.

corroborators: `(C: و ق ب B001 pit/hole supplies hidden locus)`, `(C: ن ف ث B001 breath/spittle entering knots repeats inward agency)`, `(C: ع ق د B001 tied knots supply closed locus)`, `(C: sequence فلق before غاسق creates anticipatory counter-edge)`.

constraints: `(K: فلق in local syntax is genitive title under رب, not an independent event in the clause)`, `(K: ف ل ق B001 physical splitting is possible but B002 has closer fit to غ س ق B001)`.

temporal_reactivation_notes: The phrase `غاسق إذا وقب` pulls the earlier `الفلق` back into working memory as its counter-image. The order matters: protection by the Lord of opening is heard before the darkness descends.

rival_models: `ف ل ق B001` physical splitting; `ف ل ق B003` emergence of creation; `ف ل ق B004` cleft terrain.

grade: strong

grade_rationale: Strong lexical opposition and precise temporal sequence. It does not explain every later threat by itself, but it predicts later inward/closed loci well.

source_queries_or_rows_used: QAC TSV rows `ف ل ق`, `غ س ق`, `و ق ب`; attachment `113:3 a2`; v4 `ف ل ق B002`, `غ س ق B001`, `و ق ب B002`.

### candidate_id: S113-ST1P2-C03

ayah_range: 113:1-5

seed_type: lexical

seed: `113:1:2 أَعُوذُ`, `ع و ذ B001`

short title: Refuge as separation from a series of harms.

generating_set: `(E: ع و ذ B001 refuge/holding protection)` -> `(E: ر ب ب B001 authority)` -> `(E: ش ر ر B001 evil)` with constructional expansion `(E: repeated من شر)`.

selected_branches: `ع و ذ B001`, `ر ب ب B001`, `ش ر ر B001`.

constructed_model: The seed creates a movement of the vulnerable speaker toward a protective authority. The later prepositional sequence `من شر` repeatedly fills the "from what?" role. Each threat is not sought, fought, or mastered directly by the speaker; each is named as an external source of harm from which refuge is requested.

freeze_point: after first `من شر ما خلق`.

predictions_at_freeze:

- Later ayat should continue naming threat sources rather than switching into narrative.
- Threats should be introduced by separative `من`.
- The speaker should not become the direct agent against the threats.

unused_features_tested: `ومن شر` repetitions, `غاسق إذا وقب`, `نفاثات في العقد`, `حاسد إذا حسد`.

corroborators: `(C: attachment rows 113:3 a1, 113:4 a1, 113:5 a1 genitive threat complements)`, `(C: repetition of من شر at ayah openings)`, `(C: idha clauses make threat active at a time, preserving refuge need)`.

constraints: `(K: ع و ذ B002 charm-object is not the primary syntax because the local form is verb أَعُوذُ)`, `(K: no direct imperative to manipulate knots or confront envy is supplied)`.

temporal_reactivation_notes: Every `ومن شر` reactivates `أعوذ` without restating it. The omitted verb becomes progressively stronger through repeated governed complements.

rival_models: charm/amulet model from `ع و ذ B002`, clinging-in-shelter model from `B004`, escape-after-threat model from `B006`.

grade: strong

grade_rationale: Exact syntax, repetition, and role preservation support the model.

source_queries_or_rows_used: QAC TSV `ع و ذ`, `ر ب ب`, `ش ر ر`; all attachment rows.

### candidate_id: S113-ST1P2-C04

ayah_range: 113:2-5

seed_type: constructional

seed: repeated `مِن شَرِّ X`

short title: A fourfold threat catalog under one refuge verb.

generating_set: `(E: construction repeated من شر)` -> `(E: ش ر ر B001 evil/badness)` -> `(E: خ ل ق B002 creation)` -> `(E: غ س ق B001 darkness)` -> `(E: ن ف ث B001 breath/spittle)` -> `(E: ح س د B001 wishing removal of blessing)`.

selected_branches: `ش ر ر B001`, `خ ل ق B002`, `غ س ق B001`, `ن ف ث B001`, `ح س د B001`.

constructed_model: The repeated construction creates a threat ledger. The first threat is maximally general, the second time-bound and environmental, the third manipulative and concealed in tied loci, and the fourth social/interpersonal. The construction lets a single refuge appeal hold several threat species without making them synonyms.

freeze_point: after the third `ومن شر` unit at 113:4.

predictions_at_freeze:

- Closure should supply another specific harmful agent or act.
- The closing threat should still be governed by `من شر`.
- The final unit should either intensify agency or supply a terminal interpersonal focus.

unused_features_tested: `حَاسِدٍ إِذَا حَسَدَ`, occurrence doubling of `ح س د`, absence of further ayah.

corroborators: `(C: 113:5 repeats من شر exactly)`, `(C: ح س د B001 supplies interpersonal harm aimed at another's blessing)`, `(C: idha hasada gives activation threshold and closure)`.

constraints: `(K: repeated شَرّ does not let each object collapse into generic evil; each idafa complement remains distinct)`.

temporal_reactivation_notes: The first `من شر` activates an open slot. Each `ومن شر` keeps the slot while changing threat mechanism: created field -> entering darkness -> breath into knots -> envy enacted.

rival_models: spark/scattering `ش ر ر B003/B004`, total concern `B007`, quarrel `B011`.

grade: strong

grade_rationale: The construction is explicit and repeated. It explains sequence and closure better than a static theme list.

source_queries_or_rows_used: QAC TSV all `ش ر ر` occurrences; attachment rows `113:2 a1`, `113:3 a1`, `113:4 a1`, `113:5 a1`.

### candidate_id: S113-ST1P2-C05

ayah_range: 113:2

seed_type: lexical

seed: `113:2:4 خَلَقَ`, `خ ل ق B002`

short title: Created field as the widest threat horizon.

generating_set: `(E: خ ل ق B002 creating/bringing into existence)` -> `(E: ش ر ر B001 harm)` -> `(E: ر ب ب B001 Lord/owner)`.

selected_branches: `خ ل ق B002`, `ش ر ر B001`, `ر ب ب B001`.

constructed_model: Creation supplies the widest domain from which harm may arise. The appeal is not away from creation as such, but from the harmful aspect of whatever has been created. The owner/Lord frame constrains the domain: the refuge is sought from the Lord of the opening, not from a rival creator.

freeze_point: after 113:2.

predictions_at_freeze:

- Later units should specify subtypes within the created field.
- The syntax should preserve `شر` as the target, not creation as evil.
- Later agents may be environmental, manipulative, or human.

unused_features_tested: `غاسق`, `وقب`, `نفاثات`, `عقد`, `حاسد`.

corroborators: `(C: later threat agents are created or creaturely phenomena)`, `(C: 113:2 a2 ما as object of خلق)`, `(C: ر ب ب B001 controls the created domain by lordship)`.

constraints: `(K: من شر ما خلق means harm from what He created; it does not identify خلق itself as evil)`, `(K: خ ل ق B007 false invention is a rival but not local, because ما خلق is governed as creation object not speech fabrication)`.

temporal_reactivation_notes: The general `ما خلق` opens the domain, then later ayat sample it. Later specificity reactivates the broad second ayah as a heading.

rival_models: `خ ل ق B001` measuring, `B004` disposition, `B007` false invention, `B011` water-holding pit.

grade: medium-strong

grade_rationale: Strong local syntax and broad-to-specific sequence. It is less imagistic than the dawn/darkness and knot models but structurally important.

source_queries_or_rows_used: QAC TSV `خ ل ق`; attachment `113:2 a1-a2`; v4 `خ ل ق B002`.

### candidate_id: S113-ST1P2-C06

ayah_range: 113:3

seed_type: verified composite

seed: `غَاسِقٍ إِذَا وَقَبَ`

short title: Harm when darkness enters its hiding-place.

generating_set: `(E: غ س ق B001 darkness/night entering)` -> `(E: و ق ب B002 entering hollow or darkness descending)` -> `(E: ش ر ر B001 harm)`.

selected_branches: `غ س ق B001`, `و ق ب B002`, `ش ر ر B001`.

constructed_model: A darkening agent becomes harmful at a threshold: when it enters, descends, or hides. The model is temporal and spatial: a dark medium crosses into occupancy. It explains why the ayah has both the agent `غاسق` and the activation clause `إذا وقب`.

freeze_point: after 113:3.

predictions_at_freeze:

- The threat should be episodic, not continuous.
- The next threat may preserve covert entry into a bounded locus.
- Earlier `الفلق` should be reactivated as counter-threshold.

unused_features_tested: `فلق`, `نفث في العقد`, `حاسد إذا حسد`.

corroborators: `(C: ف ل ق B002 dawn/opening as reverse threshold)`, `(C: ن ف ث B001 into ع ق د B001/B013 repeats covert entry into a bounded locus)`, `(C: 113:3 a2 marks إذا وقب as temporal qualifier)`.

constraints: `(K: غ س ق B004 pouring is a possible secondary simulation but the local active participle with إذا وقب most directly supports darkening ingress)`.

temporal_reactivation_notes: `إذا` forces waiting for activation. The threat is not merely a named thing; the clause tells when its harmful phase begins.

rival_models: `غ س ق B004` pouring fluid/night; `و ق ب B001` pit/hole; `و ق ب B006` continuous travel.

grade: strong

grade_rationale: Direct lexical and syntactic alignment between darkening and entering, with strong sequence relation to `الفلق`.

source_queries_or_rows_used: QAC TSV `غ س ق`, `و ق ب`; attachment `113:3 a1-a2`; v4 branches.

### candidate_id: S113-ST1P2-C07

ayah_range: 113:4

seed_type: verified composite

seed: `ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ`

short title: Directed breath into tied constraint.

generating_set: `(E: ن ف ث B001 breath/spittle from mouth, including charm-workers blowing into knots)` -> `(E: ع ق د B013 magic knots/incantations)` -> `(E: فِي construction containment)`.

selected_branches: `ن ف ث B001`, `ع ق د B013`.

constructed_model: The ayah forms a highly specific mechanism: breath or slight spittle is directed into knots. The `في` phrase supplies the locus. This is not just hidden harm but an operation that targets a tied, bound structure.

freeze_point: after 113:4.

predictions_at_freeze:

- The harm should be mediated and indirect.
- Binding, tying, and concealed agency should remain active.
- Closure may move from manipulative external action to a human interior source.

unused_features_tested: `ح س د`, earlier `وقب`, repeated `من شر`, basmala.

corroborators: `(C: attachment 113:4 a2 في governs العقد as complement of النفاثات)`, `(C: ع ق د B001 sensory knots supports literal tied locus distinct from B013 magic-specific branch)`, `(C: و ق ب B002 earlier ingress into hidden locus)`, `(C: ح س د B001 later interior social harm shifts from manipulation to motive)`.

constraints: `(K: ن ف ث B001 is local and direct; B002 wound bleeding and B003 chest expression are not primary here)`, `(K: ع ق د B013 explicitly contains النفاثات في العقد, so it is powerful but not independent corroboration when used to generate this model)`.

temporal_reactivation_notes: After the dark ingress of 113:3, the next ayah miniaturizes ingress: breath enters tied structures. The repeated `ومن شر` carries refuge forward into this new mechanism.

rival_models: `ع ق د B001` simple tying; `B002` covenant; `B006` fixed heart; `B007` tongue-knot; `B012` anger contraction.

grade: strong

grade_rationale: This is the passage's most exact branch match. It must be constrained because one branch lexically includes the phrase itself, but syntax independently confirms the operation and locus.

source_queries_or_rows_used: QAC TSV `ن ف ث`, `ع ق د`; attachment `113:4 a1-a2`; v4 branches.

### candidate_id: S113-ST1P2-C08

ayah_range: 113:4-5

seed_type: lexical

seed: `113:4:5 ٱلْعُقَدِ`, `ع ق د B006`

short title: Fixed interior state from knot to envy.

generating_set: `(E: ع ق د B006 firmness of heart/opinion)` -> `(E: ح س د B001 wishing removal of blessing)` -> `(E: ش ر ر B001 harm)`.

selected_branches: `ع ق د B006`, `ح س د B001`, `ش ر ر B001`.

constructed_model: If `العقد` activates fixed interior resolve rather than only physical knots, the following `حاسد إذا حسد` completes the interiorized version: harm comes from a fixed state of the self directed at another's blessing. This is a secondary simulation under the primary knot syntax.

freeze_point: after connecting `عقد` interior firmness with 113:5 envy.

predictions_at_freeze:

- The closing threat should be psychological or social, not environmental.
- It should have an activation threshold like the earlier `إذا`.
- It should still be treated as harm from which refuge is sought.

unused_features_tested: `حَاسِدٍ إِذَا حَسَدَ`, repeated `شر`, basmala mercy.

corroborators: `(C: ح س د B001 supplies interior desire to remove another's blessing)`, `(C: 113:5 a2 إذا حسد marks activation of the disposition)`, `(C: basmala ر ح م B001 opening-context mercy constrains harmful interior motive by contrast)`.

constraints: `(K: local syntax in 113:4 first points to literal/prepositional knots; B006 is secondary)`, `(K: do not translate العقد as opinions here)`.

temporal_reactivation_notes: The passage moves from bound external locus to the bound inward will of the envier. The second `إذا` makes a disposition become active.

rival_models: physical knot model C07; contract/covenant model; anger-contraction model.

grade: medium

grade_rationale: It has a plausible temporal reactivation into envy but is less primary than the literal knot/incantation branch.

source_queries_or_rows_used: QAC TSV `ع ق د`, `ح س د`; attachment `113:4 a2`, `113:5 a2`; v4.

### candidate_id: S113-ST1P2-C09

ayah_range: 113:5

seed_type: lexical

seed: `113:5:3 حَاسِدٍ` and `113:5:5 حَسَدَ`, `ح س د B001`

short title: Envy becomes harmful when it acts as envy.

generating_set: `(E: ح س د B001 wishing removal of another's blessing)` -> `(E: ش ر ر B001 harm)` with temporal construction `(E: إذا حسد)`.

selected_branches: `ح س د B001`, `ش ر ر B001`.

constructed_model: The final ayah does not merely name a type of person. It waits for the action-state: the envier when he envies. The root appears as both agent and action, closing the surah on the activation of an interior social harm.

freeze_point: after 113:5.

predictions_at_freeze:

- The surah should close because the threat has moved from general creation and environmental darkness to an interpersonal interior source.
- Repetition of root should supply closure and threshold.
- The positive alternative branch of hasad should be rejected by `شر`.

unused_features_tested: `ح س د B002`, basmala mercy, `رب` lordship/nurture, `فلق` opening.

corroborators: `(C: occurrence doubling حاسد/حسد closes with root repetition)`, `(C: 113:5 a2 temporal qualifier)`, `(C: ش ر ر B001 blocks neutral emulation)`, `(C: ر ب ب B002 nurture/protection and ر ح م B001 opening-context mercy contrast with desire to remove blessing)`.

constraints: `(K: ح س د B002 emulation without removal is defeated by من شر and by the active repetition إذا حسد)`, `(K: no explicit object of envy is named; the model must not invent one)`.

temporal_reactivation_notes: The closing `إذا` echoes 113:3. Both threats become acute at activation time. Root repetition gives a final stop: the harmful agent is harmful precisely when the named action occurs.

rival_models: `ح س د B002` benign emulation.

grade: strong

grade_rationale: Exact root repetition, explicit `شر`, and temporal activation make this highly stable.

source_queries_or_rows_used: QAC TSV `ح س د`; attachment `113:5 a1-a2`; v4 `ح س د B001-B002`.

### candidate_id: S113-ST1P2-C10

ayah_range: 113:1-5

seed_type: lexical

seed: `113:1:3 رَبِّ`, `ر ب ب B002`

short title: Nurturing-completing authority against unmaking harms.

generating_set: `(E: ر ب ب B002 repairing/nurturing/completing)` -> `(E: ف ل ق B003 emergence of creation)` -> `(E: خ ل ق B002 creation)` -> `(E: ش ر ر B001 harm)`.

selected_branches: `ر ب ب B002`, `ف ل ق B003`, `خ ل ق B002`, `ش ر ر B001`.

constructed_model: The Lord of splitting is heard as the one who brings things out and completes them stage by stage. The later harms threaten created emergence: darkness covers, knot-work binds, envy wishes the removal of blessing. The protective appeal is to the completing/nurturing authority over emergence.

freeze_point: after `من شر ما خلق`.

predictions_at_freeze:

- Later harms should obstruct emergence, opening, blessing, or integrity.
- Closing should be a threat to bestowed good, not merely physical damage.

unused_features_tested: `غاسق`, `نفاثات في العقد`, `حاسد`.

corroborators: `(C: ف ل ق B003 emergence from splitting)`, `(C: ح س د B001 wishing removal of blessing fits threat-to-bestowal)`, `(C: ع ق د B001/B013 binding constrains motion/opening)`, `(C: basmala ر ح م B001 opening-context mercy strengthens nurturing protection)`.

constraints: `(K: local noun رب primarily supports lord/master B001; nurturing B002 is a secondary but accepted branch)`, `(K: no explicit growth vocabulary beyond رب/فلق/خلق)`.

temporal_reactivation_notes: The first title is enriched as the catalog moves from creation to threats that cover, bind, and resent blessing.

rival_models: pure lordship C01; covenant B011; abiding B007; water/cloud plant branches.

grade: medium-strong

grade_rationale: Good multi-root role fit, but depends on a richer `رب` branch than the most immediate local sense.

source_queries_or_rows_used: QAC TSV `ر ب ب`, `ف ل ق`, `خ ل ق`, `ح س د`; v4 branches.

### candidate_id: S113-ST1P2-C11

ayah_range: 113:2-5

seed_type: lexical

seed: `ش ر ر B003/B004` at repeated `شَرِّ`

short title: Spark, shred, and emitted particles as a secondary harm texture.

generating_set: `(E: ش ر ر B003 flying sparks)` fork A; `(E: ش ر ر B004 shredding/remnants from mouth)` fork B -> `(E: ن ف ث B001 mouth emission)` -> `(E: غ س ق B004 pouring/flowing)`.

selected_branches: `ش ر ر B003`, `ش ر ر B004`, `ن ف ث B001`, `غ س ق B004`.

constructed_model: Some remote `شرر` branches make harm feel particulate: sparks fly, fragments scatter, mouth emissions move outward. This secondarily anticipates the breath into knots. A weaker fork also connects to darkness as a pouring spread.

freeze_point: after 113:4.

predictions_at_freeze:

- Later harm should involve emission or dispersal.
- The branch should fail where syntax requires generic evil.

unused_features_tested: `حسد`, `خلق`, `من شر`.

corroborators: `(C: ن ف ث B001 is exact mouth-emission mechanism)`, `(C: repeated شر provides multiple opportunities for harm-source texture)`.

constraints: `(K: the written local word is شَرّ not شَرَر; B001 is the primary contextual branch)`, `(K: ح س د B001 is motive, not particle emission)`, `(K: خ ل ق B002 does not require sparks or shredding)`.

temporal_reactivation_notes: The remote branch only becomes attractive after `النفاثات`, not at first hearing. That backward activation is real but subordinate.

rival_models: `ش ر ر B001` generic evil, `B007` total concern, `B011` quarrel.

grade: weak

grade_rationale: There is one striking link to `نفث`, but the branch is morphologically/contextually remote and does not explain the whole threat catalog.

source_queries_or_rows_used: all `ش ر ر` occurrences; `ن ف ث B001`; v4.

### candidate_id: S113-ST1P2-C12

ayah_range: 113:1-5

seed_type: temporal/acoustic

seed: repeated activation clauses and root repetition: `إِذَا وَقَبَ`, `إِذَا حَسَدَ`, `حَاسِدٍ/حَسَدَ`

short title: Threats become acute at activation thresholds.

generating_set: `(E: temporal construction إذا X)` -> `(E: و ق ب B002 entering/descent)` -> `(E: ح س د B001 envy enacted)`.

selected_branches: `و ق ب B002`, `ح س د B001`.

constructed_model: The surah distinguishes threat identity from threat activation. The darkening one is dangerous when it enters; the envier is dangerous when envy is enacted. The central knot threat is not marked with `إذا`, but its operation is already embedded as an action in `النفاثات في العقد`.

freeze_point: after 113:5.

predictions_at_freeze:

- Closure should feel complete once the final activation clause resolves.
- The two `إذا` clauses should bracket non-general threat units.

unused_features_tested: ayah boundaries, repeated `ومن`, root repetition.

corroborators: `(C: attachment 113:3 a2 and 113:5 a2)`, `(C: ح س د root repetition gives closure)`, `(C: ayah-final وقف after حسد closes on activated harm)`.

constraints: `(K: 113:4 lacks إذا, so not every threat is temporally marked the same way)`.

temporal_reactivation_notes: The second `إذا` recalls the first and teaches the hearer how to understand danger as a transition, not a static label.

rival_models: static list of four harms.

grade: medium-strong

grade_rationale: Strong discourse pattern, but not a lexical synthesis by itself.

source_queries_or_rows_used: attachment rows `113:3 a2`, `113:5 a2`; QAC root order.

## Exhaustive Lexical Seed Ledger

Notation:

- `O` = occurrence.
- `E` = branch used before freeze.
- `C` = unused corroborator after freeze.
- `K` = constraining or defeating evidence after freeze.
- "Terminates" means the seed was initiated, dossiers were checked, and no passage-local image survived beyond a small or failed model.

### 113:1:1 `قُلْ` - Root `ق و ل`

All sixteen accepted `ق و ل` branches were seeded at the first rooted word.

| seed | result |
| --- | --- |
| `ق و ل B001` | Generates C01. `(E: articulated speech)` opens a commanded refuge utterance; corroborated by quote attachment `113:1 a1` and repeated governed `من شر`. Grade strong. |
| `ق و ل B002` | Tongue-as-instrument seed forms a small local speech-body image. It can weakly touch `ن ف ث B001` mouth emission, but `قُلْ` is command to speak, not focus on tongue anatomy. `(K: no tongue term; no bodily instrument role)`. Grade weak. |
| `ق و ل B003` | Frequent speaker seed terminates. The passage has one command and repeated threat phrases, not a characterization of a talkative person. `(K: قُلْ imperative, not وصف قوال)`. Grade unlikely. |
| `ق و ل B004` | Authoritative speaker seed makes a local delegated-command image: the utterance is commanded by an authority. It is constrained because the branch's Yemenite ruler sense is remote. `(C: imperative quote frame)`, `(K: no الملك/قيل role)`. Grade weak. |
| `ق و ل B005` | False-speech seed makes a weak rival with `خ ل ق B007` invented false speech and `ن ف ث B003` chest expression. It is defeated by the sacred command syntax and refuge content. `(K: قُلْ is not false attribution)`. Grade unlikely. |
| `ق و ل B006` | Drawing speech to oneself seed terminates. First-person `أعوذ` is spoken, but no branch-specific act of appropriating a saying appears. Grade unlikely. |
| `ق و ل B007` | Circulating public saying seed weakly predicts social harm and can meet `ح س د B001`; however the surah does not depict rumor. `(K: no قال الناس/قالة structure)`. Grade weak. |
| `ق و ل B008` | Stick for striking qillah terminates. No local complement. Grade unlikely. |
| `ق و ل B009` | Negotiation seed terminates. No reciprocal speech or bargaining; `قُلْ` is unilateral command. Grade unlikely. |
| `ق و ل B010` | Imposed judgment seed weakly fits command authority but lacks local legal/judicial frame. Grade unlikely. |
| `ق و ل B011` | Saying-as-supposition seed terminates. No ظن-like syntax or interrogative. Grade unlikely. |
| `ق و ل B012` | Inner unexpressed saying seed creates a weak interior-speech fork toward `ح س د B001` hidden envy, but it is constrained by overt imperative. Grade weak. |
| `ق و ل B013` | Saying as belief/doctrine seed terminates. No doctrinal proposition is attributed. Grade unlikely. |
| `ق و ل B014` | A thing's indication seed weakly supports the whole surah as signs indicating harms, but this is too generic. Grade weak/unlikely. |
| `ق و ل B015` | Sincere care seed can weakly align with protective concern in refuge, but no idiom says "يقول بكذا" here. Grade weak. |
| `ق و ل B016` | Definition/limit seed terminates. No logical definition role. Grade unlikely. |

### 113:1:2 `أَعُوذُ` - Root `ع و ذ`

| seed | result |
| --- | --- |
| `ع و ذ B001` | Generates C03. Refuge/protection is primary and structurally repeated by `من شر`. Grade strong. |
| `ع و ذ B002` | Warding charm/ruqyah seed forms a rival protective-speech image with `ق و ل B001`, `ن ف ث B001`, and `ع ق د B013`. It is constrained because `أعوذ` is the speaker's verb, while the later charm-like action belongs to the threat, not the refuge act. Grade medium. |
| `ع و ذ B003` | Newly delivered female clinging to young seed weakly touches basmala `ر ح م B003/B004` opening-context womb/birth and `ر ب ب B009` recent birth, but none is passage-local. Grade unlikely. |
| `ع و ذ B004` | Adhesion/shelter seed creates a local image of clinging under protection: `(E: ع و ذ B004)` + `(E: ر ب ب B001)`; corroborated by repeated `من` separation. But primary lexical fit remains B001. Grade medium. |
| `ع و ذ B005` | Horse collar-mark seed terminates. No horse/mark/collar role. Grade unlikely. |
| `ع و ذ B006` | Escape after threat short of completion forms a small model: refuge asks that harms not complete. It can meet `إذا` activation clauses, but no near-killing or threatened blow is supplied. Grade weak. |
| `ع و ذ B007` | Mutual refuge/default in war seed terminates. No group mutuality or war frame. Grade unlikely. |
| `ع و ذ B008` | Avoidance out of dislike seed gives a weak aversive-separation model with `من شر`; it is less specific than B001 and lacks protection authority. Grade weak. |

### 113:1:3 `رَبِّ` - Root `ر ب ب`

| seed | result |
| --- | --- |
| `ر ب ب B001` | Enters C01/C03 as lordship/mastery. Protecting authority governs refuge. Grade strong. |
| `ر ب ب B002` | Generates C10. Nurturing/completing authority protects emergence and blessing from covering, binding, and envy. Grade medium-strong. |
| `ر ب ب B003` | Rabbinic learning seed weakly relates to commanded recitation but lacks learners/scholars. Grade unlikely. |
| `ر ب ب B004` | Large groups seed terminates; no multitudes except broad `ما خلق`, too generic. Grade unlikely. |
| `ر ب ب B005` | Foster child/caretaker seed weakly overlaps protection/care but no family/foster relation. Grade unlikely. |
| `ر ب ب B006` | Thick rubb/repair seed has remote contact with `خ ل ق B010` perfume/coating and `ع ق د B003` thickening, but none is local. Grade unlikely. |
| `ر ب ب B007` | Staying/abiding seed forms a weak endurance frame with recurrent refuge and recurring harms. `(C: repeated من شر)`, `(K: no إقامة wording)`. Grade weak. |
| `ر ب ب B008` | Layered cloud seed can weakly touch `غ س ق B004` pouring and `ف ل ق B003` rain/cloud split, but no cloud term occurs. Grade weak/unlikely. |
| `ر ب ب B009` | Fresh post-birth/youth seed only connects to opening-context `ر ح م B003/B004` and `ع و ذ B003`; no passage-local support. Grade unlikely. |
| `ر ب ب B010` | Arrow container seed terminates. No arrows/gaming container. Grade unlikely. |
| `ر ب ب B011` | Covenant/protection pact seed forms a weak refuge-under-covenant image with `ع ق د B002` binding contract. Constrained by lack of covenant language. Grade weak. |
| `ر ب ب B012` | Green plant seed weakly touches `ف ل ق B003` plant emerging from seed but no plant in passage. Grade unlikely. |
| `ر ب ب B013` | Abundant water seed weakly touches `غ س ق B004` flowing and `خ ل ق B011` water-holding pit, but passage local threat is darkness not water. Grade unlikely. |
| `ر ب ب B014` | Herd/group seed terminates. Grade unlikely. |
| `ر ب ب B015` | Particle rubba seed terminates; the occurrence is noun `رب`, not particle. Grade unlikely. |
| `ر ب ب B016` | Need/firm knot/blessing seed produces a weak bridge to `ع ق د B001/B006` and `ح س د B001` blessing-removal. It is remote but gives subordinate support to C10. Grade weak. |
| `ر ب ب B017` | Chief of sailors seed terminates. No nautical frame. Grade unlikely. |

### 113:1:4 `ٱلْفَلَقِ` - Root `ف ل ق`

| seed | result |
| --- | --- |
| `ف ل ق B001` | Physical splitting/opening seed forms a separation model: refuge by the Lord of splitting against harms that enter/bind. `(C: و ق ب B002 ingress)`, `(C: ع ق د B001 binding as anti-opening)`. Grade medium-strong. |
| `ف ل ق B002` | Generates C02. Dawn/clarification counteracts dark ingress. Grade strong. |
| `ف ل ق B003` | Emergence-of-creation seed supports C10 with `خ ل ق B002` and blessing threatened by envy. Grade medium. |
| `ف ل ق B004` | Low gap/cleft seed creates a weak spatial hiding image with `و ق ب B001` hole and `غ س ق B001` darkness entering low spaces. Constrained by title under `رب`. Grade weak. |
| `ف ل ق B005` | Prisoner stocks seed weakly relates to `ع ق د B001/B013` binding and refuge from constriction, but no imprisonment role. Grade unlikely. |
| `ف ل ق B006` | Calamity/wondrous thing seed can read `الفلق` as awesome danger, but local `رب الفلق` and later refuge make it unlikely as generating protection title. Grade unlikely. |
| `ف ل ق B007` | Army/corps seed terminates. No military complement. Grade unlikely. |

### `شَرِّ` Occurrences - Root `ش ر ر`

The eleven accepted `ش ر ر` branches were seeded at each of four occurrences. The branch is the same, but prior activation differs by occurrence.

#### O1: 113:2:2 `شَرِّ` after refuge title

| seed | result |
| --- | --- |
| `ش ر ر B001` | Primary harm/evil heading. Generates broad created-field threat with `خ ل ق B002`; enters C04/C05. Grade strong. |
| `ش ر ر B002` | Spreading in sun to dry weakly contrasts with `ف ل ق B002` daylight but has no drying object. Grade unlikely. |
| `ش ر ر B003` | Sparks remote seed; before `نفث` it predicts flying harm but lacks fire. Grade weak/unlikely. |
| `ش ر ر B004` | Shredding/mouth remnants remote seed; before `نفث` only a vague mouth-emission expectation. Grade weak. |
| `ش ر ر B005` | Dripping roast fat terminates. Grade unlikely. |
| `ش ر ر B006` | Dangling tails/weights terminates. Grade unlikely. |
| `ش ر ر B007` | Throwing one's whole concern onto something weakly predicts envy fixation, but not yet passage-local. Grade weak. |
| `ش ر ر B009` | Mosquito-like facial nuisance seed forms tiny harm image, not supported by later threats. Grade unlikely. |
| `ش ر ر B010` | Youthful drive/greed weakly anticipates envy but lacks youth. Grade weak/unlikely. |
| `ش ر ر B011` | Quarrel weakly anticipates interpersonal final threat but no dispute language. Grade weak. |
| `ش ر ر B012` | Plant name terminates. Grade unlikely. |

#### O2: 113:3:2 `شَرِّ` after general created-field threat

| seed | result |
| --- | --- |
| `ش ر ر B001` | Harm is now specified by `غاسق إذا وقب`; enters C06. Grade strong. |
| `ش ر ر B002` | Drying-in-sun is constrained by night/darkness. Grade unlikely. |
| `ش ر ر B003` | Sparks contrast with darkness but no fire appears. Grade weak. |
| `ش ر ر B004` | Shredding/mouth remnants not yet supported until 113:4; after freeze it can be weakly corroborated by `نفث`. Grade weak. |
| `ش ر ر B005` | Terminates. Grade unlikely. |
| `ش ر ر B006` | Terminates. Grade unlikely. |
| `ش ر ر B007` | Total concern onto something has no dark-agent role. Grade unlikely. |
| `ش ر ر B009` | Nuisance swarming in darkness is possible but unsupported. Grade unlikely. |
| `ش ر ر B010` | Greedy drive no local fit. Grade unlikely. |
| `ش ر ر B011` | Quarrel no local fit. Grade unlikely. |
| `ش ر ر B012` | Terminates. Grade unlikely. |

#### O3: 113:4:2 `شَرِّ` after dark ingress

| seed | result |
| --- | --- |
| `ش ر ر B001` | Harm is specified by `النفاثات في العقد`; enters C07. Grade strong. |
| `ش ر ر B002` | Drying/spreading has no sun and is defeated by knot/breath mechanism. Grade unlikely. |
| `ش ر ر B003` | Sparks/particles seed joins C11 as secondary texture; `نفث` provides emission but no fire. Grade weak. |
| `ش ر ر B004` | Shredding/remnants-from-mouth has its best local chance with `ن ف ث B001`; still subordinate to B001. Grade weak/medium. |
| `ش ر ر B005` | Terminates. Grade unlikely. |
| `ش ر ر B006` | Dangling/weights can weakly touch knots/cords but no tails/weights. Grade weak/unlikely. |
| `ش ر ر B007` | Throwing oneself/concern onto target weakly anticipates manipulative fixation, but no self-throwing syntax. Grade weak. |
| `ش ر ر B009` | Nuisance image not supported. Grade unlikely. |
| `ش ر ر B010` | Greedy drive no fit. Grade unlikely. |
| `ش ر ر B011` | Quarrel no fit. Grade unlikely. |
| `ش ر ر B012` | Plant name no fit. Grade unlikely. |

#### O4: 113:5:2 `شَرِّ` before envy

| seed | result |
| --- | --- |
| `ش ر ر B001` | Harm is specified by `حاسد إذا حسد`; enters C09. Grade strong. |
| `ش ر ر B002` | Drying-in-sun no fit. Grade unlikely. |
| `ش ر ر B003` | Sparks metaphor for envy possible but no fire lexeme. Grade weak/unlikely. |
| `ش ر ر B004` | Shredding/remnant image could model corrosive envy, but no mouth or cutting at closure. Grade weak. |
| `ش ر ر B005` | Terminates. Grade unlikely. |
| `ش ر ر B006` | Terminates. Grade unlikely. |
| `ش ر ر B007` | Total concern/fixation gives a weak envy model: envier throws whole concern toward another's blessing. `(C: ح س د B001)`, `(K: idiom not local)`. Grade weak. |
| `ش ر ر B009` | Nuisance no specific fit. Grade unlikely. |
| `ش ر ر B010` | Youthful drive/greed weakly meets envy as acquisitive desire, but B001 of hasad specifies removal. Grade weak. |
| `ش ر ر B011` | Quarrel is a possible social-harm fork, but envy is not explicitly argument. Grade weak. |
| `ش ر ر B012` | Terminates. Grade unlikely. |

### 113:2:4 `خَلَقَ` - Root `خ ل ق`

| seed | result |
| --- | --- |
| `خ ل ق B001` | Measuring/estimating before action creates a weak preparatory model; later knots and envy may imply planned harm, but `ما خلق` syntax favors creation. Grade weak. |
| `خ ل ق B002` | Generates C05. Created-field horizon under `من شر`. Grade medium-strong. |
| `خ ل ق B003` | Complete form/proportion supports created forms but does not explain threats. Grade weak. |
| `خ ل ق B004` | Inner disposition seed connects strongly to `ح س د B001` as harmful inner nature and to `ع ق د B006`. Constrained because 113:2 is broad object of creation. Grade medium. |
| `خ ل ق B005` | Fitness/readiness weakly predicts threat becoming active at `إذا`; no خليق construction. Grade weak/unlikely. |
| `خ ل ق B007` | Invented false speech seed joins rejected `ق و ل B005`; it is constrained by `ما` object of `خلق` and by lack of lie vocabulary. Grade unlikely. |
| `خ ل ق B008` | Smooth hard surface weakly touches `ف ل ق B001` splitting hard objects and `خ ل ق B012` closure, but no surface in passage. Grade unlikely. |
| `خ ل ق B009` | Worn cloth branch weakly touches `ش ر ر B004` shredding, but no garment/wear. Grade unlikely. |
| `خ ل ق B010` | Perfumed coating weakly contrasts with `ن ف ث` breath/spittle but no scent/coating. Grade unlikely. |
| `خ ل ق B011` | Water-holding pit can combine with `و ق ب B001` hole and `غ س ق B004` flow, making a weak hidden-locus model. Grade weak. |
| `خ ل ق B012` | Sealed hard closure can combine with `ع ق د B001/B016` and `و ق ب B001`; secondary enclosure model. Grade weak. |

### 113:3:3 `غَاسِقٍ` - Root `غ س ق`

| seed | result |
| --- | --- |
| `غ س ق B001` | Generates C06 with `و ق ب B002` and reactivates `ف ل ق B002`. Grade strong. |
| `غ س ق B003` | Eye darkening seed creates a weak perception-loss model. It can meet darkness and envy/evil eye by association, but no eye term appears. Grade weak. |
| `غ س ق B004` | Flowing/pouring seed makes a medium secondary model: darkness pours over the scene and harm seeps inward; corroborated by `و ق ب B002`, constrained by primary night meaning. Grade medium. |
| `غ س ق B005` | Food impurities terminates. Grade unlikely. |

### 113:3:5 `وَقَبَ` - Root `و ق ب`

| seed | result |
| --- | --- |
| `و ق ب B001` | Pit/hole seed forms a hidden-locus model with `غ س ق B001`, `ع ق د B001`, and `خ ل ق B011`. It is secondary but useful for inward disappearance. Grade medium. |
| `و ق ب B002` | Generates C06. Entering/descent of darkness into hidden space. Grade strong. |
| `و ق ب B003` | Animal sound terminates. Grade unlikely. |
| `و ق ب B004` | Hunger falling on people seed terminates; no hunger or deprivation except remote envy. Grade unlikely. |
| `و ق ب B005` | Household odds and ends terminates. Grade unlikely. |
| `و ق ب B006` | Continuous travel day/night weakly touches temporal duration and night/day opposition, but no travel. Grade unlikely. |
| `و ق ب B007` | Shell/amulet seed weakly interacts with `ع و ذ B002` charms and `ن ف ث/عقد`, but no shell appears. Grade weak/unlikely. |

### 113:4:3 `ٱلنَّفَّٰثَٰتِ` - Root `ن ف ث`

| seed | result |
| --- | --- |
| `ن ف ث B001` | Generates C07. Breath/spittle into knots is exact local mechanism. Grade strong. |
| `ن ف ث B002` | Wound emitting blood creates a weak injury-output image but no wound/blood role. Grade unlikely. |
| `ن ف ث B003` | Chest expelling what is inside creates a medium secondary bridge to hidden interior motives and `ح س د B001`, but local phrase points to mouth-breath in knots. Grade weak/medium. |

### 113:4:5 `ٱلْعُقَدِ` - Root `ع ق د`

| seed | result |
| --- | --- |
| `ع ق د B001` | Physical knots/tied ends support C07 as an independent literal locus after `ن ف ث B001`; grade strong as corroborator, medium-strong as seed. |
| `ع ق د B002` | Covenant/contract seed weakly connects to `ر ب ب B011` and refuge under protective pact, but `في العقد` points to knots. Grade weak. |
| `ع ق د B003` | Thickening/solidifying seed creates a weak image of harm congealing; can meet `غ س ق B004` flow becoming fixed. Grade weak. |
| `ع ق د B004` | Estate/property seed weakly touches envy over possessions but no property term. Grade unlikely. |
| `ع ق د B005` | Dense vegetation/pasture seed has no local plant field except remote `ف ل ق B003`; terminates. Grade unlikely. |
| `ع ق د B006` | Generates C08 as secondary interior-fixed-state model toward envy. Grade medium. |
| `ع ق د B007` | Tongue-tie/obscure speech seed links to `ق و ل B001/B002` and hidden manipulation, but no blocked speech in passage. Grade weak. |
| `ع ق د B008` | Piled sand/contracted cloud seed weakly touches `غ س ق B004` poured night/cloud imagery and `ر ب ب B008` cloud, but no sand/cloud local. Grade unlikely. |
| `ع ق د B009` | Grape cluster seed terminates. Grade unlikely. |
| `ع ق د B010` | Twisted animal limb seed has no animal body. Grade unlikely. |
| `ع ق د B011` | Compact body seed terminates. Grade unlikely. |
| `ع ق د B012` | Contracted anger/character seed makes a secondary affective model with `ح س د B001`; envy is harmful contracted disposition. Constrained by primary knots. Grade medium/weak. |
| `ع ق د B013` | Generates C07 with exact magic-knot/incantation branch. Grade strong, with constraint against double-counting as independent corroboration. |
| `ع ق د B014` | Counting on fingers seed terminates. Grade unlikely. |
| `ع ق د B015` | Close position seed terminates. Grade unlikely. |
| `ع ق د B016` | Enclosure/encircling seed forms a medium hidden-enclosure model with `و ق ب B001/B002`, `غ س ق`, and `في`. Grade medium. |
| `ع ق د B017` | Turning neck to someone for refuge creates an intriguing backward bridge to `أعوذ برب`, but local `العقد` in 113:4 is object of `في`, not refuge gesture. Grade weak. |

### 113:5:3 `حَاسِدٍ` and 113:5:5 `حَسَدَ` - Root `ح س د`

Each branch was seeded at both the agent occurrence and the verb occurrence.

| seed | result |
| --- | --- |
| `O1 حاسد - ح س د B001` | Generates C09 as harmful agent: one wishing removal of blessing. Corroborated by `من شر` and later verbal repetition. Grade strong. |
| `O1 حاسد - ح س د B002` | Benign emulation seed is defeated immediately by `من شر`. It can survive only as rejected rival. Grade unlikely. |
| `O2 حسد - ح س د B001` | Generates activation threshold model: the envier becomes dangerous when envy occurs. Corroborated by `إذا` and root repetition. Grade strong. |
| `O2 حسد - ح س د B002` | Benign emulation at the verb occurrence is defeated by `شر`, by the active clause, and by closure under refuge. Grade unlikely. |

## Constructional Seed Ledger

| seed | result |
| --- | --- |
| `قُلْ + quoted complement` | Generates C01. Commanded utterance governs the entire refuge formula. Grade strong. |
| `أعوذ برب` prepositional complement | Generates C03. Refuge takes protective authority as complement. Grade strong. |
| `رب الفلق` idafa | Splitting/daybreak is not an event narrated by the speaker but a title-domain of the Lord. Supports C01/C02/C10. Grade strong. |
| `من شر ما خلق` | Broad threat domain under creation; generates C05. Grade medium-strong. |
| repeated `ومن شر` | Generates C04 and reactivates omitted `أعوذ`. Grade strong. |
| `شر غاسق` idafa | Specific threat source after general `شر`; supports C06. Grade strong. |
| `إذا وقب` temporal clause | Threat activation threshold; supports C06/C12. Grade strong. |
| `شر النفاثات` idafa | Harm source is operator/agents of breathing; supports C07. Grade strong. |
| `في العقد` prepositional containment | Locus of operation; supports C07 and secondary enclosure models. Grade strong. |
| `شر حاسد` idafa | Harm source is an envier; supports C09. Grade strong. |
| `إذا حسد` temporal clause | Envy becomes active as harm; supports C09/C12. Grade strong. |

## Morphosyntactic Seed Ledger

| seed | result |
| --- | --- |
| Imperative `قُلْ` | The reciter is instructed to voice the refuge, so the surah begins as directed performance. Grade strong. |
| First-person imperfect `أعوذ` | The refuge remains present-tense/performative rather than narrated past. Grade strong. |
| Prefixed `بـ` on `رب` | Refuge clings to/proceeds by protective Lord; supports authority anchor. Grade strong. |
| Genitive chains under `شر` | Each threat is defined by source/complement, not by a new independent clause. Grade strong. |
| Active participles `غاسق`, `حاسد` | Threats are agent-like dispositions or entities, then `إذا` marks activation. Grade medium-strong. |
| Intensive/feminine plural `النفاثات` | Repeated/intensive breath operators; supports C07 while not requiring details beyond the text. Grade medium-strong. |
| `في` plus plural `العقد` | Internal locus and multiplicity of knots; supports hidden directed operation. Grade strong. |
| Root repetition `حاسد/حسد` | Closure and activation of same root; supports C09. Grade strong. |

## Temporal And Acoustic Seed Ledger

| seed | result |
| --- | --- |
| First rooted word `قل` before refuge | The passage is heard as instruction before personal seeking; C01. Grade strong. |
| `الفلق` before `غاسق إذا وقب` | Dawn/opening precedes and later counters dark ingress; C02. Grade strong. |
| General `ما خلق` before specific harms | Broad domain is narrowed by successive examples; C05/C04. Grade medium-strong. |
| Three `ومن شر` restarts | Each restart reactivates `أعوذ`; C04. Grade strong. |
| Two `إذا` clauses | Threats become acute at thresholds; C12. Grade medium-strong. |
| Ayah-final closure on `حسد` | Repeated root and final stop close on enacted envy. Grade strong. |
| Sound recurrence in `شر`, `غسق`, `وقب`, `عقد`, `حسد` | Hard consonantal closure supports constriction/entry as acoustic texture; evidence is only secondary. Grade weak. |

## Image Packet Catalog

### IMAGE_ID: S113-IMG-01

Starting seed: `ق و ل B001` at `قُلْ`.

Complete image: commanded protective utterance.

Passage-order assembly: command -> refuge -> Lord of opening -> from harm -> threat catalog.

Participants and roles: speaker/reciter, commanded voice, protective Lord, harmful sources.

Operation / mechanism: speech performs refuge-seeking and repeatedly governs later `من شر` complements.

Direction / force / medium: speaker turns toward authority and away from harms.

Temporal development: later threats reactivate the initial `أعوذ`.

Outcome / closure: final envy unit remains inside the same refuge frame.

Exact branch constituents: `ق و ل B001`, `ع و ذ B001`, `ر ب ب B001`, `ف ل ق B002`, `ش ر ر B001`.

Unfilled roles, if any: none for the speech/refuge frame.

Status: COMPLETE.

### IMAGE_ID: S113-IMG-02

Starting seed: `ف ل ق B002`.

Complete image: opening/daybreak against dark ingress.

Passage-order assembly: Lord of daybreak -> harm of darkening one -> when it enters.

Participants and roles: opener/daybreak Lord, darkening agent, hidden/entered locus.

Operation / mechanism: opening counters descent/concealment.

Direction / force / medium: outward clarification versus inward/dark entry.

Temporal development: `غاسق إذا وقب` reactivates `الفلق`.

Outcome / closure: later knot/enclosure images extend inward hidden threat.

Exact branch constituents: `ف ل ق B002`, `غ س ق B001`, `و ق ب B002`.

Unfilled roles, if any: no explicit physical object split; title-domain only.

Status: COMPLETE for ayah 1-3 image; PARTIAL for whole-surah coverage.

### IMAGE_ID: S113-IMG-03

Starting seed: repeated `من شر`.

Complete image: threat catalog under one refuge.

Passage-order assembly: created-field harm -> dark-ingress harm -> knot-breath harm -> envy-activation harm.

Participants and roles: created domain, environmental darkness, manipulative breathers, tied loci, envier.

Operation / mechanism: one refuge phrase receives increasingly specific threat complements.

Direction / force / medium: harms arise from different media and are separated by `من`.

Temporal development: each `ومن شر` renews the initial appeal.

Outcome / closure: the catalog closes with interpersonal envy when enacted.

Exact branch constituents: `ش ر ر B001`, `خ ل ق B002`, `غ س ق B001`, `ن ف ث B001`, `ح س د B001`.

Unfilled roles, if any: object of envy unspecified.

Status: COMPLETE.

### IMAGE_ID: S113-IMG-04

Starting seed: `ن ف ث B001` / `ع ق د B013`.

Complete image: breath directed into knots.

Passage-order assembly: after dark entry, the harm becomes deliberate breath into tied loci.

Participants and roles: breathers/operators, knots, emitted breath/spittle, protected speaker.

Operation / mechanism: slight mouth emission enters or acts within knots.

Direction / force / medium: mouth -> breath/spittle -> knots.

Temporal development: repeats the ingress pattern at a smaller scale.

Outcome / closure: next ayah moves from external manipulation to interior motive.

Exact branch constituents: `ن ف ث B001`, `ع ق د B013`, `ع ق د B001`, construction `في`.

Unfilled roles, if any: explicit victim of knot operation not named.

Status: COMPLETE for ayah 4 image.

### IMAGE_ID: S113-IMG-05

Starting seed: `ح س د B001`.

Complete image: enacted envy as closing interpersonal harm.

Passage-order assembly: envier named -> temporal clause repeats root -> surah closes.

Participants and roles: envier, unspecified possessor of blessing, blessing/good desired for removal, protected speaker.

Operation / mechanism: harmful interior desire activates when envy occurs.

Direction / force / medium: inward motive aimed outward toward another's blessing.

Temporal development: final `إذا` recalls the earlier activation threshold.

Outcome / closure: root repetition and ayah-final stop end the threat catalog.

Exact branch constituents: `ح س د B001`, `ش ر ر B001`, construction `إذا حسد`.

Unfilled roles, if any: envied object and person not named.

Status: COMPLETE.

## Exhaustiveness Check

Lexical seeds covered:

- `ق و ل`: 16 branches x 1 occurrence = 16.
- `ع و ذ`: 8 branches x 1 occurrence = 8.
- `ر ب ب`: 17 branches x 1 occurrence = 17.
- `ف ل ق`: 7 branches x 1 occurrence = 7.
- `ش ر ر`: 11 branches x 4 occurrences = 44.
- `خ ل ق`: 11 branches x 1 occurrence = 11.
- `غ س ق`: 4 branches x 1 occurrence = 4.
- `و ق ب`: 7 branches x 1 occurrence = 7.
- `ن ف ث`: 3 branches x 1 occurrence = 3.
- `ع ق د`: 17 branches x 1 occurrence = 17.
- `ح س د`: 2 branches x 2 occurrences = 4.

Total lexical seed passes recorded: 138.

Constructional seeds covered: 11.

Morphosyntactic seeds covered: 8.

Temporal/acoustic seeds covered: 7.

Potentially missing image audit:

- Main coherent images retained: commanded refuge speech, dawn/opening against dark ingress, repeated threat catalog, created-field broad horizon, knot-breath operation, enacted envy closure, nurturing/completing authority against unmaking harms.
- Remote branch images retained as weak or unlikely rather than silently dropped: false speech, public saying, charm-object refuge, clinging shelter, covenant, cloud/water/plant, physical cleft/stocks/army, sparks/shredding, smooth/worn/perfumed/closed creation branches, eye-darkening/flowing/impurity, hole/sound/hunger/household/travel/shell, wound/chest emission, all knot sub-branches, benign hasad.
- No additional complete image was found after the ledger review. The highest-risk omitted family was `ع ق د` because it has many branches; all 17 branches are explicitly logged above.
