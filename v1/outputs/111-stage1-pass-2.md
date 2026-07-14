# Stage 1 Pass 2 — S111

Assigned passage: S111  
Sacred Arabic text file: `resources/quran/surah_111.json`  
Prompt: `v1/prompts/stage1.md`

## Root Cause For Pass 1 Limitation

The limited word and branch coverage in Pass 1 was caused by missing required SQLite resources, not by a decision to stop early. The prompt requires:

- `resources/qac.sqlite` for rooted words, morphemes, lemmas, morphology, and sequence.
- `resources/furuq_v4.sqlite` for uncontaminated branch dossiers with `branch_image_ar` and `what_is_ar`.

At the time of this Pass 2 run, both paths exist only as zero-byte ignored files:

- `resources/qac.sqlite`: 0 bytes, no schema, no tables.
- `resources/furuq_v4.sqlite`: 0 bytes, no schema, no tables.

No alternate `.sqlite` or `.db` files are present under `resources/`. Therefore no auditable QAC morphology rows or furuq branch images can be retrieved. I have not invented branch IDs, branch images, or QAC morpheme facts. The exhaustive restart below covers every eligible rooted occurrence and construction that can be identified from the sacred Arabic text plus `resources/attachments.tsv` rows for S111. Each missing lexical-branch pass is explicitly retained as resource-blocked instead of omitted.

## Evidence Actually Available

Sacred text:

```text
111:0 بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
111:1 تَبَّتْ يَدَآ أَبِى لَهَبٍۢ وَتَبَّ
111:2 مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ
111:3 سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ
111:4 وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ
111:5 فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ
```

Attachment rows used as structural evidence only:

- `111:1 a1`: `يَدَا` is overt dual subject of `تَبَّتْ`.
- `111:1 a2`: `أَبِى` is genitive muḍāf ilayh of `يَدَا`.
- `111:1 a3`: `لَهَبٍ` completes the proper-name idafa after `أَبِى`.
- `111:1 a4`: `وَتَبَّ` is coordinated with earlier `تَبَّتْ`.
- `111:2 a1`: pronoun suffix in `عَنْهُ` is governed by `عَنْ` as complement of `أَغْنَى`.
- `111:2 a2`: `مَالُهُ` is explicit subject of `أَغْنَى`.
- `111:2 a3`: `وَمَا كَسَبَ` is coordinated with `مَالُهُ` as second subject expression under the negated verb.
- `111:2 a4`: `مَا` is fronted object inside the relative clause governed by `كَسَبَ`.
- `111:2 a5`: suffix in `مَالُهُ` is possessive dependent.
- `111:3 a1`: `نَارًا` is direct object of `سَيَصْلَى`.
- `111:3 a2`: `ذَاتَ` agrees with `نَارًا` and describes the fire.
- `111:3 a3`: `لَهَبٍ` is genitive muḍāf ilayh of `ذَاتَ`.
- `111:4 a1`: `حَمَّالَةَ` may be circumstantial describing `ٱمْرَأَتُهُ`.
- `111:4 a2`: `حَمَّالَةَ ٱلْحَطَبِ` may be predicative of `ٱمْرَأَتُهُ`.
- `111:4 a3`: `ٱلْحَطَبِ` is genitive muḍāf ilayh of `حَمَّالَةَ`.
- `111:4 a4`: suffix in `ٱمْرَأَتُهُ` is possessive dependent.
- `111:5 a1`: `جِيدِهَا` is governed by `فِى` in locative phrase predicated of `حَبْلٌ`.
- `111:5 a2`: `فِى جِيدِهَا` is fronted predicate linked to delayed subject `حَبْلٌ`.
- `111:5 a3`: `مَّسَدٍ` is governed by `مِن` as material-specifying complement of `حَبْلٌ`.
- `111:5 a4`: suffix in `جِيدِهَا` is possessive dependent.

## Exhaustive Seed Inventory Under Resource Constraint

Eligible rooted occurrence seeds identifiable from the attachment rows and sacred text:

1. `111:1:1 تَبَّتْ` root `ت ب ب`
2. `111:1:2 يَدَا` root `ي د ي`
3. `111:1:3 أَبِى` root `أ ب و`
4. `111:1:4 لَهَبٍ` root `ل ه ب`
5. `111:1:6 وَتَبَّ` root `ت ب ب`
6. `111:2:2 أَغْنَى` root `غ ن ي`
7. `111:2:4 مَالُهُ` root `م و ل`
8. `111:2:7 كَسَبَ` root `ك س ب`
9. `111:3:1 سَيَصْلَى` root `ص ل و`
10. `111:3:2 نَارًا` root `ن و ر`
11. `111:3:3 ذَاتَ` root `ذ و و`
12. `111:3:4 لَهَبٍ` root `ل ه ب`
13. `111:4:2 وَٱمْرَأَتُهُ` root `م ر أ`
14. `111:4:3 حَمَّالَةَ` root `ح م ل`
15. `111:4:4 ٱلْحَطَبِ` root `ح ط ب`
16. `111:5:2 جِيدِهَا` root `ج ي د`
17. `111:5:3 حَبْلٌ` root `ح ب ل`
18. `111:5:5 مَّسَدٍ` root `م س د`

The attachment row for `وَمَا` lists a root-like value but also identifies the token as `REL_PRON`; without QAC I do not promote it to a lexical root seed. It is handled constructionally in the negated acquisition seed.

All seed passes below use:

```text
roots visited: all 18 occurrence roots listed above, plus actual textual constructions
selected furuq branches: none available
branch status: blocked by missing furuq_v4.sqlite
QAC morphology status: blocked by missing qac.sqlite
```

## Lexical Occurrence Seed Passes

### S111-P2-L001 — `111:1:1 تَبَّتْ` / root `ت ب ب`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: first rooted word, `تَبَّتْ`
- short title: Collapse Opens Before Agency Is Named
- initial image: the recitation begins with a completed ruin/failure event before the owner is fully resolved.
- generating_set: surface occurrence `تَبَّتْ`; structural subject attachment to `يَدَا` `(E: attachment 111:1 a1)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: a failure-state is heard first, then attached to dual hands, then repeated with `وَتَبَّ`; the opening therefore creates an activation loop of ruin → agentive instruments → named owner → ruin again.
- freeze_point: after `111:1 وَتَبَّ`.
- predictions_at_freeze: expect later material to show why hands/agency cannot avail, what possessed capacities fail, and whether the flame-name returns as a real burning environment.
- unused_features_tested: negated `أَغْنَى`; `مَالُهُ`; `مَا كَسَبَ`; `سَيَصْلَى`; `نَارًا ذَاتَ لَهَبٍ`; wife, fuel, neck, rope.
- corroborators: `(C: attachment 111:2 a2 explicit subject مَالُهُ under negated availing)`, `(C: attachment 111:2 a3 acquired expression coordinated as second failed subject)`, `(C: sequence 111:1→111:2 hands/agency followed by failed possessions and acquisitions)`, `(C: attachment 111:3 a1 direct object fire of future burning)`.
- constraints: `(K: no furuq branch can be cited for ت ب ب)`, `(K: no QAC morphology row available for tense/aspect beyond surface and attachment)`.
- temporal_reactivation_notes: the second `تَبَّ` reactivates the opening failure after the named hands have been identified; later non-availing wealth and acquisition reactivate failure in an economic/agency register.
- rival_models: simple imprecation without secondary image; agency-collapse model.
- grade: medium
- grade_rationale: structurally strong from repetition and attachments, but lexically under-audited because branch dossiers are unavailable.
- source_queries_or_rows_used: sacred text; attachment rows `111:1 a1-a4`, `111:2 a2-a4`, `111:3 a1`.

### S111-P2-L002 — `111:1:2 يَدَا` / root `ي د ي`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: `يَدَا`
- short title: Instruments Of Agency Are The First Named Subject
- initial image: dual hands as the first overt participant after failure.
- generating_set: `يَدَا`; `(E: attachment 111:1 a1 subject of تَبَّتْ)`, `(E: attachment 111:1 a2 idafa to أَبِى)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: the passage first locates ruin in two agency-instruments, then tests what those instruments ordinarily produce or control: wealth, acquisition, carrying, and a rope at the neck.
- freeze_point: after `111:1 أَبِى لَهَبٍ`.
- predictions_at_freeze: expect later action-products or possessions to fail; expect bodily imagery to continue if the hand seed is not accidental.
- unused_features_tested: `مَالُهُ`; `مَا كَسَبَ`; `حَمَّالَةَ`; `فِى جِيدِهَا حَبْلٌ`.
- corroborators: `(C: attachment 111:2 a2 مالُه explicit subject of non-availing)`, `(C: attachment 111:2 a4 ما as object of كسب)`, `(C: attachment 111:4 a1/a2 carrier role)`, `(C: attachment 111:5 a1-a2 neck locus for rope)`.
- constraints: `(K: hands are syntactic subject, not necessarily literal severing or manual action beyond the idiom-like surface)`, `(K: no branch dossier for ي د ي)`.
- temporal_reactivation_notes: agency moves from hands to possessions/acquisitions, then to a woman carrying fuel, then to a rope fixed at her neck.
- rival_models: hands as synecdoche for person; hands as literal bodily image that later body/rope imagery reactivates.
- grade: medium-strong
- grade_rationale: strong structural continuity across agency, acquisition, carrying, and bodily binding; missing lexical branch audit prevents a stronger grade.
- source_queries_or_rows_used: attachment rows `111:1 a1-a2`, `111:2 a2-a5`, `111:4 a1-a3`, `111:5 a1-a4`.

### S111-P2-L003 — `111:1:3 أَبِى` / root `أ ب و`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: `أَبِى`
- short title: Possessor In A Proper-Name Chain
- initial image: a genitive figure is introduced as the owner/source associated with the hands.
- generating_set: `(E: attachment 111:1 a2 أَبِى as genitive dependent of يَدَا)`, `(E: attachment 111:1 a3 لَهَب completes proper-name idafa after أَبِى)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: the figure is not first introduced by independent action but by possessed hands and a flame-linked name; the name then becomes available for later reactivation.
- freeze_point: after `أَبِى لَهَبٍ`.
- predictions_at_freeze: expect the `لَهَب` component to be tested later; expect possession suffixes to matter if the passage continues ownership relations.
- unused_features_tested: `ماله`, `امرأته`, `جيدها`, `نارًا ذات لهب`.
- corroborators: `(C: attachment 111:3 a3 second لَهَب as genitive dependent of ذات)`, `(C: attachment 111:2 a5 possessive suffix in ماله)`, `(C: attachment 111:4 a4 possessive suffix in امرأته)`, `(C: attachment 111:5 a4 possessive suffix in جيدها)`.
- constraints: `(K: attachment row treats أَبِى لَهَب as proper-name idafa; this constrains father/source imagery from becoming the primary contextual meaning)`, `(K: no branch dossier for أ ب و)`.
- temporal_reactivation_notes: the name is introduced in ayah 1 and its `لَهَب` element returns in ayah 3 attached to actual fire.
- rival_models: proper-name anchor only; name-as-latent-flame reactivated by later fire.
- grade: weak
- grade_rationale: useful as a name/possession anchor, but no lexical branch support is available and the attachment row constrains over-reading.
- source_queries_or_rows_used: attachment rows `111:1 a2-a3`, `111:2 a5`, `111:3 a3`, `111:4 a4`, `111:5 a4`.

### S111-P2-L004 — `111:1:4 لَهَبٍ` / root `ل ه ب`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: first `لَهَبٍ` in `أَبِى لَهَبٍ`
- short title: Flame Name Awaiting Reactivation
- initial image: flame appears first as part of a proper name, not as an explicit fire-object.
- generating_set: `(E: attachment 111:1 a3 لَهَب completes proper-name idafa)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: the name contains a flame element that is semantically dormant under the proper-name constraint until the later phrase `نارًا ذات لهب` turns it into an explicit property of fire.
- freeze_point: after `111:1`.
- predictions_at_freeze: expect either no reactivation, leaving proper-name only, or a later fire/flame expression that turns the name into a predictive cue.
- unused_features_tested: `نارًا`; `ذات لهب`; `الحطب`; `حبل من مسد`.
- corroborators: `(C: attachment 111:3 a1 نارًا object of سيصلى)`, `(C: attachment 111:3 a2 ذات describes نارًا)`, `(C: attachment 111:3 a3 second لهب as genitive of ذات)`, `(C: attachment 111:4 a3 firewood as dependent of carrier)`.
- constraints: `(K: first occurrence is constrained by proper-name idafa, not a free fire noun)`, `(K: no furuq branch for ل ه ب)`.
- temporal_reactivation_notes: ayah 3 strongly reactivates the name-internal `لَهَب` by placing the same surface root after `نارًا ذات`.
- rival_models: proper name only; proper name that becomes an anticipatory flame cue.
- grade: strong
- grade_rationale: exact recurrence and sequence provide strong reactivation; lexical branch detail remains unavailable but is not needed for the basic recurrence model.
- source_queries_or_rows_used: attachment rows `111:1 a3`, `111:3 a1-a3`, `111:4 a3`.

### S111-P2-L005 — `111:1:6 وَتَبَّ` / root `ت ب ب`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: second `تَبَّ`
- short title: Repetition Closes The First Activation Loop
- initial image: after the hands and name are heard, ruin/failure is restated.
- generating_set: `(E: attachment 111:1 a4 وَتَبَّ coordinated with تَبَّتْ)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: the second verb does not introduce a new object; it locks the opening statement into a recursive frame: ruin declared, hands assigned, name supplied, ruin confirmed.
- freeze_point: end of ayah 1.
- predictions_at_freeze: expect the next ayah to justify or unpack the confirmed loss.
- unused_features_tested: the negated availing relation in ayah 2, future burning in ayah 3, wife/fuel/rope sequence.
- corroborators: `(C: sequence 111:1→111:2 confirmed ruin followed by negated availing)`, `(C: attachment 111:2 a2-a3 two subject expressions under negated availing)`.
- constraints: `(K: repetition alone does not specify the later fire/rope image)`, `(K: no branch dossier for ت ب ب)`.
- temporal_reactivation_notes: the second `تَبَّ` causes later failures in ayah 2 to be heard as explanation of the opening failure rather than a separate topic.
- rival_models: emphatic repetition; sequential transition from bodily agency to failed benefit.
- grade: medium
- grade_rationale: structurally clear but lexically branch-blocked.
- source_queries_or_rows_used: attachment rows `111:1 a4`, `111:2 a1-a5`.

### S111-P2-L006 — `111:2:2 أَغْنَى` / root `غ ن ي`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: `أَغْنَى`
- short title: Failed Sufficiency Or Non-Availing
- initial image: after ruin is confirmed, the passage asks whether something suffices or avails against it, and negates that.
- generating_set: `مَا أَغْنَى`; `(E: attachment 111:2 a1 pronoun complement عَنْهُ)`, `(E: attachment 111:2 a2 مالُه subject)`, `(E: attachment 111:2 a3 وما كسب coordinated as second subject expression)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: a protection/availing test is opened: wealth and acquired things are structurally placed as possible rescuers, but the negation defeats them.
- freeze_point: after ayah 2.
- predictions_at_freeze: expect later consequence to proceed without successful shield; expect possessed resources to be irrelevant against a coming force.
- unused_features_tested: `سيصلى نارًا ذات لهب`; wife/fuel; rope/neck.
- corroborators: `(C: attachment 111:3 a1 fire as direct object of سيصلى)`, `(C: sequence 111:2→111:3 failed availing immediately followed by future burning)`, `(C: possessive suffixes 111:4 a4 and 111:5 a4 continue ownership/body marking without rescue)`.
- constraints: `(K: no lexical branch dossier for غ ن ي)`, `(K: the construction is negated; any sufficiency image must be stated as failed)`.
- temporal_reactivation_notes: the non-availing test bridges the initial ruin and the following fire; it retrospectively explains why the hands' failure matters.
- rival_models: wealth-specific failure; general failure of protection.
- grade: medium-strong
- grade_rationale: strong syntactic support from subject/complement rows and sequence; missing lexical branches limit lexical specificity.
- source_queries_or_rows_used: attachment rows `111:2 a1-a5`, `111:3 a1`.

### S111-P2-L007 — `111:2:4 مَالُهُ` / root `م و ل`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: `مَالُهُ`
- short title: Possessed Resource That Cannot Shield
- initial image: the man's possessed resource is placed as subject of the failed availing verb.
- generating_set: `(E: attachment 111:2 a2 explicit subject of أَغْنَى)`, `(E: attachment 111:2 a5 possessive suffix)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: possession is activated as a candidate protective resource, then negated; the suffix `ه` links the resource back to the figure introduced through hands/name.
- freeze_point: after `مَالُهُ`.
- predictions_at_freeze: expect a second resource or product to be tested; expect further possessive pronouns to build a web of ownership without rescue.
- unused_features_tested: `وما كسب`, `امرأته`, `جيدها`, rope material.
- corroborators: `(C: attachment 111:2 a3 وما كسب as coordinated second subject expression)`, `(C: attachment 111:4 a4 wife possessive suffix)`, `(C: attachment 111:5 a4 her-neck possessive suffix)`.
- constraints: `(K: no furuq branch for م و ل)`, `(K: the negated verb prevents treating wealth as effective agency)`.
- temporal_reactivation_notes: wealth appears after hands; the passage shifts from bodily agency to owned resources, then later to owned/related person and body locus.
- rival_models: failed wealth only; failed ownership network.
- grade: medium
- grade_rationale: syntactically precise but branch-blocked.
- source_queries_or_rows_used: attachment rows `111:2 a2-a5`, `111:4 a4`, `111:5 a4`.

### S111-P2-L008 — `111:2:7 كَسَبَ` / root `ك س ب`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: `كَسَبَ`
- short title: Acquired Product Folded Into Failure
- initial image: what he acquired is the second failed subject expression under the negated availing frame.
- generating_set: `(E: attachment 111:2 a3 وما كسب coordinated with ماله)`, `(E: attachment 111:2 a4 ما as fronted object governed by كسب)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: the passage extends from possessed wealth to produced/acquired outcome; neither acquired product nor existing possession creates rescue.
- freeze_point: end of ayah 2.
- predictions_at_freeze: expect later material to show consequence unaffected by accumulation or action-products.
- unused_features_tested: `سيصلى نارًا`; `حمالة الحطب`; `حبل من مسد`.
- corroborators: `(C: attachment 111:3 a1 fire direct object follows immediately)`, `(C: attachment 111:4 a1/a2 carrier role as an action-bearing description)`, `(C: attachment 111:4 a3 carried material as idafa dependent)`.
- constraints: `(K: no furuq branch for ك س ب)`, `(K: acquisition does not by itself generate the fuel/rope model without later attachments)`.
- temporal_reactivation_notes: acquired product creates a transition from abstract/owned resource to later carried material.
- rival_models: economic acquisition only; action-product line that later becomes burden/fuel.
- grade: medium
- grade_rationale: clear local role under negated availing; later carrying/fuel relation is plausible but not branch-confirmed.
- source_queries_or_rows_used: attachment rows `111:2 a3-a4`, `111:3 a1`, `111:4 a1-a3`.

### S111-P2-L009 — `111:3:1 سَيَصْلَى` / root `ص ل و`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: `سَيَصْلَى`
- short title: Consequence Enters As Future Burning
- initial image: after failed availing, the recitation introduces a future encounter with fire.
- generating_set: surface `سَيَصْلَى`; `(E: attachment 111:3 a1 نارًا direct object)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: the negated protection test yields a future fire-event; the object `نارًا` fills the expected consequence role, and `ذات لهب` further specifies the fire.
- freeze_point: after `نارًا ذات لهب`.
- predictions_at_freeze: expect fire-supporting material or flame-related roles to follow if the image is not isolated.
- unused_features_tested: wife, carrier, firewood, neck-rope.
- corroborators: `(C: attachment 111:3 a2 ذات describes fire)`, `(C: attachment 111:3 a3 لهب specifies ذات)`, `(C: attachment 111:4 a3 الحطب dependent of حمالة)`.
- constraints: `(K: no furuq branch for ص ل و)`, `(K: direct object is fire, not an abstract loss-state)`.
- temporal_reactivation_notes: `لهب` from the name is now realized as a property of fire; `الحطب` then supplies fuel-like material after the burning scene.
- rival_models: punishment event only; fire-system image linking name, flame, fuel, and rope.
- grade: medium-strong
- grade_rationale: structural sequence is strong; lexical branch specificity unavailable.
- source_queries_or_rows_used: attachment rows `111:3 a1-a3`, `111:4 a3`.

### S111-P2-L010 — `111:3:2 نَارًا` / root `ن و ر`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: `نَارًا`
- short title: Fire Receives The Name's Flame
- initial image: explicit fire enters as object of the future event.
- generating_set: `(E: attachment 111:3 a1 نارًا direct object of سيصلى)`, `(E: attachment 111:3 a2 ذات describes نارًا)`, `(E: attachment 111:3 a3 لهب genitive of ذات)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: the passage changes the first `لَهَب` from a name-component into a property of an actual fire; fire then opens the need for combustible material.
- freeze_point: end of ayah 3.
- predictions_at_freeze: expect fuel, carrying, or material support if the fire image continues.
- unused_features_tested: `حمالة الحطب`; `حبل من مسد`.
- corroborators: `(C: attachment 111:4 a3 الحطب as carried dependent)`, `(C: sequence 111:3→111:4 fire followed by firewood carrier)`.
- constraints: `(K: root ن و ر is inferred from attachment row for نارًا; QAC morphology unavailable)`, `(K: no furuq branch for ن و ر)`.
- temporal_reactivation_notes: ayah 4 answers the fuel expectation opened by ayah 3.
- rival_models: isolated fire object; continuing combustion chain.
- grade: medium-strong
- grade_rationale: very clear local construction; lexical branches missing.
- source_queries_or_rows_used: attachment rows `111:3 a1-a3`, `111:4 a1-a3`.

### S111-P2-L011 — `111:3:3 ذَاتَ` / root `ذ و و`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: `ذَاتَ`
- short title: Possessing A Quality
- initial image: the fire is characterized as having/being of flame.
- generating_set: `(E: attachment 111:3 a2 ذات agrees with نارًا and describes it)`, `(E: attachment 111:3 a3 لهب genitive dependent)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: an entity-plus-possessed-quality frame appears: fire is specified by its flame; later rope is specified by material through `من مسد`.
- freeze_point: after `ذات لهب`.
- predictions_at_freeze: expect more specification structures or material/quality complements.
- unused_features_tested: `حمالة الحطب`; `حبل من مسد`.
- corroborators: `(C: attachment 111:5 a3 من مسد material-specifying complement of حبل)`, `(C: attachment 111:4 a3 الحطب as dependent specifying what is carried)`.
- constraints: `(K: ذات modifies fire specifically; it does not license turning every later idafa into the same construction)`, `(K: no branch dossier for ذ و و)`.
- temporal_reactivation_notes: `ذات لهب` gives the fire an internal property; the final rope receives a material specification, closing with another thing-plus-constituent relation.
- rival_models: adjectival specification only; broader specification chain.
- grade: weak
- grade_rationale: constructionally suggestive but not enough independent lexical support.
- source_queries_or_rows_used: attachment rows `111:3 a2-a3`, `111:4 a3`, `111:5 a3`.

### S111-P2-L012 — `111:3:4 لَهَبٍ` / root `ل ه ب`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: second `لَهَبٍ`
- short title: Reactivated Flame
- initial image: flame now appears as the genitive complement of `ذات`, explicitly describing fire.
- generating_set: `(E: attachment 111:3 a3 لهب as genitive of ذات)`, `(E: attachment 111:3 a1-a2 fire plus description)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: the second `لَهَب` retroactively charges `أَبى لهب` with fiery relevance while remaining grammatically distinct from the proper name.
- freeze_point: after ayah 3.
- predictions_at_freeze: expect fuel or combustion-supporting material if the flame image continues.
- unused_features_tested: wife as carrier; firewood; rope material.
- corroborators: `(C: attachment 111:1 a3 earlier لهب proper-name idafa)`, `(C: attachment 111:4 a3 الحطب dependent of حمالة)`, `(C: sequence name-flame in ayah 1 → fire-flame in ayah 3 → wood in ayah 4)`.
- constraints: `(K: first occurrence remains proper-name constrained)`, `(K: no furuq branch for ل ه ب)`.
- temporal_reactivation_notes: this is one of the strongest backward reactivations in the passage: a name element becomes an explicit fire property two ayat later.
- rival_models: lexical repetition only; delayed semantic activation of a name component.
- grade: strong
- grade_rationale: exact recurrence with grammatical transformation from proper-name component to fire property.
- source_queries_or_rows_used: attachment rows `111:1 a3`, `111:3 a1-a3`, `111:4 a3`.

### S111-P2-L013 — `111:4:2 وَٱمْرَأَتُهُ` / root `م ر أ`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: `وَٱمْرَأَتُهُ`
- short title: Paired Participant Enters The Fire System
- initial image: after the man's failed agency and fire-consequence, his wife enters as a possessed/related participant.
- generating_set: `(E: attachment 111:4 a4 possessive suffix)`, `(E: attachment 111:4 a1/a2 حمالة as either circumstantial or predicative description)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: the participant field expands from the named man to his wife; she is not introduced neutrally but immediately under a carrier/fuel description.
- freeze_point: after `حمالة الحطب`.
- predictions_at_freeze: expect her body or carried burden to be localized; expect the possessive chain to continue with feminine suffix.
- unused_features_tested: `في جيدها حبل من مسد`.
- corroborators: `(C: attachment 111:5 a4 suffix in جيدها refers to her neck)`, `(C: attachment 111:5 a1-a2 fronted neck phrase predicated of rope)`.
- constraints: `(K: attachment ambiguity between حال and predication must be preserved)`, `(K: no branch dossier for م ر أ)`.
- temporal_reactivation_notes: masculine possession suffixes in ayah 2 shift to wife relation in ayah 4, then feminine body suffix in ayah 5.
- rival_models: wife as separate participant; wife as carrier completing the flame/fuel system.
- grade: medium
- grade_rationale: strong attachment continuity but lexical branch detail unavailable.
- source_queries_or_rows_used: attachment rows `111:4 a1-a4`, `111:5 a1-a4`.

### S111-P2-L014 — `111:4:3 حَمَّالَةَ` / root `ح م ل`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: `حَمَّالَةَ`
- short title: Carrier Role Converts Fuel Into Burden
- initial image: an intensive carrier description enters after the fire/flame scene.
- generating_set: `(E: attachment 111:4 a1 circumstantial option)`, `(E: attachment 111:4 a2 predicative option)`, `(E: attachment 111:4 a3 الحطب as genitive dependent)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: the fire image obtains a human carrier of combustible material; the carrier's role then predicts a bodily load or binding relation.
- freeze_point: after `حمالة الحطب`.
- predictions_at_freeze: expect location on body or instrument of carrying/binding.
- unused_features_tested: `في جيدها حبل من مسد`.
- corroborators: `(C: attachment 111:5 a1 جيدها governed by في)`, `(C: attachment 111:5 a2 fronted predicate linked to delayed subject حبل)`, `(C: attachment 111:5 a3 rope material specified by من مسد)`.
- constraints: `(K: حال/predication ambiguity remains unresolved)`, `(K: no furuq branch for ح م ل)`.
- temporal_reactivation_notes: carrying follows fire, then neck-rope follows carrying; the sequence shifts from combustible material to burden restraint.
- rival_models: descriptor only; carrier-burden mechanism.
- grade: medium-strong
- grade_rationale: strong constructional role completion from carrier to carried object to bodily rope; branch evidence unavailable.
- source_queries_or_rows_used: attachment rows `111:4 a1-a3`, `111:5 a1-a3`.

### S111-P2-L015 — `111:4:4 ٱلْحَطَبِ` / root `ح ط ب`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: `ٱلْحَطَبِ`
- short title: Fuel After Flame
- initial image: firewood appears immediately after fire with flame, as the object of the carrier description.
- generating_set: `(E: attachment 111:4 a3 الحطب genitive dependent of حمالة)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: the fire scene receives its material supply; the woman is positioned as carrier of what feeds the flame.
- freeze_point: end of ayah 4.
- predictions_at_freeze: expect the carrying relation to resolve into a body/load/binding location.
- unused_features_tested: `في جيدها حبل من مسد`.
- corroborators: `(C: sequence 111:3 fire/flame → 111:4 firewood)`, `(C: attachment 111:5 a1-a3 neck-rope-material closure)`.
- constraints: `(K: الحطب is governed by حمالة, not directly by نارًا)`, `(K: no furuq branch for ح ط ب)`.
- temporal_reactivation_notes: `الحطب` reactivates the fire/flame from the prior ayah and prepares the final rope/burden image.
- rival_models: fuel only; fuel-as-burden that culminates in neck binding.
- grade: medium-strong
- grade_rationale: strong sequence and idafa support; no lexical branch dossier.
- source_queries_or_rows_used: attachment rows `111:3 a1-a3`, `111:4 a1-a3`, `111:5 a1-a3`.

### S111-P2-L016 — `111:5:2 جِيدِهَا` / root `ج ي د`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: `جِيدِهَا`
- short title: The Body Locus Of Closure
- initial image: a feminine possessed neck is fronted inside a locative phrase.
- generating_set: `(E: attachment 111:5 a1 جيدها governed by في)`, `(E: attachment 111:5 a2 fronted predicate linked to delayed subject حبل)`, `(E: attachment 111:5 a4 possessive suffix)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: the carrier role is localized on the woman's body; the passage closes not with abstract punishment but with a concrete locative binding image.
- freeze_point: after `في جيدها`.
- predictions_at_freeze: expect an object occupying that location; possibly an instrument/binding.
- unused_features_tested: `حبل من مسد`.
- corroborators: `(C: attachment 111:5 a2 delayed subject حبل)`, `(C: attachment 111:5 a3 material complement من مسد)`, `(C: attachment 111:4 a1/a2 carrier role prior to neck locus)`.
- constraints: `(K: locative phrase is predicated of rope; it does not directly state what she carries)`, `(K: no furuq branch for ج ي د)`.
- temporal_reactivation_notes: the feminine suffix ties the neck back to `امرأته`, completing the participant shift.
- rival_models: ornament/locus only; binding closure after carrying.
- grade: medium
- grade_rationale: strong local attachment, limited lexical branch support.
- source_queries_or_rows_used: attachment rows `111:4 a1-a4`, `111:5 a1-a4`.

### S111-P2-L017 — `111:5:3 حَبْلٌ` / root `ح ب ل`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: `حَبْلٌ`
- short title: Rope As Delayed Subject And Binding Closure
- initial image: the delayed subject fills the fronted neck-location with a rope.
- generating_set: `(E: attachment 111:5 a2 في جيدها as fronted predicate linked to delayed subject حبل)`, `(E: attachment 111:5 a3 من مسد material complement)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: the image closes with an object in the neck, specified by material; prior carrying/fuel now resolves into binding and burden.
- freeze_point: after `حبل من مسد`.
- predictions_at_freeze: none; this is the closure position.
- unused_features_tested: prior carrier/fuel; prior hands/agency; possession suffix chain.
- corroborators: `(C: attachment 111:4 a1/a2 carrier role)`, `(C: attachment 111:4 a3 carried firewood)`, `(C: sequence hands at opening → neck at closure creates body-part frame)`.
- constraints: `(K: no furuq branch for ح ب ل)`, `(K: rope is subject of predication, not grammatically direct object of carrying)`.
- temporal_reactivation_notes: the final rope reactivates earlier hands/body agency by moving the bodily focus from hands to neck.
- rival_models: literal rope closure; symbolically intensified burden/binding image.
- grade: medium-strong
- grade_rationale: excellent structural closure; branch evidence missing.
- source_queries_or_rows_used: attachment rows `111:4 a1-a3`, `111:5 a1-a3`.

### S111-P2-L018 — `111:5:5 مَّسَدٍ` / root `م س د`

- seed_type: lexical occurrence
- ayah_range: 111:1-5
- seed: `مَّسَدٍ`
- short title: Material Specification At The End
- initial image: the final word specifies the material/source of the rope.
- generating_set: `(E: attachment 111:5 a3 مسد governed by من as material-specifying complement of حبل)`.
- selected_branches: none; furuq dossier unavailable.
- constructed_model: the passage closes by specifying what the binding object is made from; the last word hardens the image from location/object into material.
- freeze_point: passage end.
- predictions_at_freeze: none; closure.
- unused_features_tested: prior `ذات لهب`, `حمالة الحطب`, `في جيدها`.
- corroborators: `(C: attachment 111:3 a2-a3 fire specified by ذات لهب)`, `(C: attachment 111:4 a3 carried item specified by idafa)`, `(C: final-position closure)`.
- constraints: `(K: no furuq branch for م س د)`, `(K: material complement does not by itself explain the whole surah without prior sequence)`.
- temporal_reactivation_notes: the final material complement mirrors earlier specification structures and stops the recitation on the binding medium.
- rival_models: material detail only; final concretization of burden/binding system.
- grade: medium
- grade_rationale: strong closure role but lexical branch unavailable.
- source_queries_or_rows_used: attachment rows `111:3 a2-a3`, `111:4 a3`, `111:5 a1-a3`.

## Constructional, Morphosyntactic, And Temporal Seed Passes

### S111-P2-C001 — `تَبَّتْ يَدَا أَبِى لَهَبٍ وَتَبَّ`

- seed_type: constructional
- ayah_range: 111:1
- seed: opening clause plus coordinated repetition
- short title: Ruin → Hands → Name → Ruin
- generating_set: `(E: attachment 111:1 a1 subject)`, `(E: attachment 111:1 a2 idafa)`, `(E: attachment 111:1 a3 proper-name idafa)`, `(E: attachment 111:1 a4 coordinated repetition)`.
- selected_branches: none.
- constructed_model: the first ayah is a compact activation loop: failure is announced, attached to dual hands, tied to a flame-bearing proper name, then repeated.
- freeze_point: end of ayah 1.
- predictions_at_freeze: later passage should unpack agency failure, name/flame reactivation, or both.
- unused_features_tested: ayah 2 non-availing wealth/acquisition; ayah 3 fire/flame; ayah 4 fuel carrier; ayah 5 neck rope.
- corroborators: `(C: attachment 111:2 a2-a4 failed resources and acquisition)`, `(C: attachment 111:3 a1-a3 fire with flame)`, `(C: attachment 111:4 a1-a3 carrier of firewood)`, `(C: attachment 111:5 a1-a3 rope at neck)`.
- constraints: `(K: the opening does not itself supply wife/fuel/rope roles)`.
- temporal_reactivation_notes: ayah 2 reactivates agency; ayah 3 reactivates flame; ayahs 4-5 complete fuel/burden/binding.
- rival_models: emphatic curse formula; structured seed of agency/flame system.
- grade: strong
- grade_rationale: the construction predicts two major later tracks: failed agency and reactivated flame.
- source_queries_or_rows_used: attachment rows `111:1 a1-a4`, `111:2 a2-a4`, `111:3 a1-a3`, `111:4 a1-a3`, `111:5 a1-a3`.

### S111-P2-C002 — Name-Flame Reactivation

- seed_type: temporal/acoustic
- ayah_range: 111:1-3
- seed: `أَبِى لَهَبٍ` followed by `نَارًا ذَاتَ لَهَبٍ`
- short title: Proper Name Becomes Fire Property
- generating_set: `(E: attachment 111:1 a3 first لهب constrained as proper-name idafa)`, `(E: attachment 111:3 a1 نارًا direct object)`, `(E: attachment 111:3 a2 ذات describes fire)`, `(E: attachment 111:3 a3 second لهب genitive of ذات)`.
- selected_branches: none.
- constructed_model: the first `لَهَب` is heard under proper-name grammar; the later `لَهَب` is heard as a property of fire, creating a backward reactivation from explicit fire to name.
- freeze_point: after ayah 3.
- predictions_at_freeze: after fire/flame, expect combustible material or a participant tied to fuel if the image continues.
- unused_features_tested: `حمالة الحطب`; final rope material.
- corroborators: `(C: attachment 111:4 a3 الحطب dependent of carrier)`, `(C: sequence 111:3→111:4)`.
- constraints: `(K: first لهب is not grammatically free flame; it is proper-name material)`.
- temporal_reactivation_notes: this is a clean delayed reactivation: later explicit flame reorganizes the earlier name.
- rival_models: repetition as sound only; repetition as semantic reactivation.
- grade: strong
- grade_rationale: exact repeated surface root in different grammatical environments with intervening sequence support.
- source_queries_or_rows_used: attachment rows `111:1 a3`, `111:3 a1-a3`, `111:4 a3`.

### S111-P2-C003 — Negated Availing Construction

- seed_type: constructional
- ayah_range: 111:2
- seed: `مَا أَغْنَى عَنْهُ مَالُهُ وَمَا كَسَبَ`
- short title: Failed Shield Of Possession And Acquisition
- generating_set: `(E: attachment 111:2 a1 pronoun complement)`, `(E: attachment 111:2 a2 مال subject)`, `(E: attachment 111:2 a3 coordinated second subject expression)`, `(E: attachment 111:2 a4 ما fronted object of كسب)`, `(E: attachment 111:2 a5 possessive suffix)`.
- selected_branches: none.
- constructed_model: two possible availing sources are syntactically tested and negated: what he has and what he acquired.
- freeze_point: end of ayah 2.
- predictions_at_freeze: expect consequence to proceed immediately; no protective role remains open.
- unused_features_tested: ayah 3 fire event; ayahs 4-5 related participant and rope.
- corroborators: `(C: attachment 111:3 a1 fire object of future event)`, `(C: sequence ayah 2→3)`, `(C: suffix chain ماله → امرأته → جيدها)`.
- constraints: `(K: because the construction is negated, wealth/acquisition cannot be a successful counterforce)`.
- temporal_reactivation_notes: ayah 2 explains the opening failure and prepares the consequence.
- rival_models: legal/economic inventory only; failed-protection transition.
- grade: strong
- grade_rationale: syntactically forced structure with direct temporal consequence.
- source_queries_or_rows_used: attachment rows `111:2 a1-a5`, `111:3 a1`, `111:4 a4`, `111:5 a4`.

### S111-P2-C004 — Fire-With-Flame Construction

- seed_type: constructional
- ayah_range: 111:3
- seed: `سَيَصْلَى نَارًا ذَاتَ لَهَبٍ`
- short title: Consequence Object With Internal Flame
- generating_set: `(E: attachment 111:3 a1 direct object)`, `(E: attachment 111:3 a2 adjective/description agreement)`, `(E: attachment 111:3 a3 idafa)`.
- selected_branches: none.
- constructed_model: the consequence is not simply stated as a future event; it is specified as fire, and the fire is internally characterized by flame.
- freeze_point: end of ayah 3.
- predictions_at_freeze: expect combustible support or a participant who handles fuel.
- unused_features_tested: `وامرأته حمالة الحطب`; `في جيدها حبل من مسد`.
- corroborators: `(C: attachment 111:4 a1/a2 wife described by carrier role)`, `(C: attachment 111:4 a3 firewood dependent)`, `(C: attachment 111:5 a3 material rope complement as final material specification)`.
- constraints: `(K: ayah 3 does not identify the wife; the participant expansion occurs only in ayah 4)`.
- temporal_reactivation_notes: ayah 3 reactivates `لَهَب` from ayah 1 and predicts the fuel image in ayah 4.
- rival_models: isolated punishment line; fire/fuel/rope system.
- grade: strong
- grade_rationale: direct object, internal specification, exact `لَهَب` recurrence, and immediate fuel continuation.
- source_queries_or_rows_used: attachment rows `111:1 a3`, `111:3 a1-a3`, `111:4 a1-a3`, `111:5 a3`.

### S111-P2-C005 — Wife As Carrier Of Firewood

- seed_type: constructional
- ayah_range: 111:4
- seed: `وَٱمْرَأَتُهُ حَمَّالَةَ ٱلْحَطَبِ`
- short title: Related Participant Becomes Fuel Carrier
- generating_set: `(E: attachment 111:4 a1 circumstantial option)`, `(E: attachment 111:4 a2 predicative option)`, `(E: attachment 111:4 a3 firewood idafa)`, `(E: attachment 111:4 a4 possessive suffix)`.
- selected_branches: none.
- constructed_model: the wife's role is defined by carrying combustible material; the syntax allows either circumstantial or predicative reading, both preserving carrier identity.
- freeze_point: end of ayah 4.
- predictions_at_freeze: expect the carried/burdened body to be localized or constrained.
- unused_features_tested: ayah 5 neck-rope phrase.
- corroborators: `(C: attachment 111:5 a1-a2 locative neck phrase predicated of rope)`, `(C: attachment 111:5 a4 feminine possessive suffix)`.
- constraints: `(K: attachment ambiguity remains; do not collapse حال and predication into one syntactic claim)`.
- temporal_reactivation_notes: after fire/flame, the passage introduces the person associated with fuel, then resolves her with a body-bound rope.
- rival_models: descriptive epithet only; fuel-carrier-to-binding sequence.
- grade: medium-strong
- grade_rationale: high local structural fit; syntactic ambiguity and missing lexical branches prevent strong.
- source_queries_or_rows_used: attachment rows `111:4 a1-a4`, `111:5 a1-a4`.

### S111-P2-C006 — Fronted Neck Predicate And Delayed Rope

- seed_type: constructional
- ayah_range: 111:5
- seed: `فِى جِيدِهَا حَبْلٌ مِّن مَّسَدٍ`
- short title: Binding Object Appears At The Passage Closure
- generating_set: `(E: attachment 111:5 a1 prepositional complement)`, `(E: attachment 111:5 a2 fronted predicate linked to delayed subject)`, `(E: attachment 111:5 a3 material complement)`, `(E: attachment 111:5 a4 possessive suffix)`.
- selected_branches: none.
- constructed_model: the final ayah delays the subject until after the neck-location, making the location salient first and then filling it with rope and material.
- freeze_point: passage end.
- predictions_at_freeze: none; terminal closure.
- unused_features_tested: prior hands, carrier, firewood, possession chain.
- corroborators: `(C: attachment 111:1 a1 hands as opening body-part subject)`, `(C: attachment 111:4 a1/a2 carrier role)`, `(C: attachment 111:4 a3 carried firewood)`, `(C: final-position closure)`.
- constraints: `(K: rope is not grammatically attached as the direct object of حمالة)`.
- temporal_reactivation_notes: the body frame opened by hands closes at neck; agency failure becomes bodily binding.
- rival_models: static final image; completion of burden/binding trajectory.
- grade: strong
- grade_rationale: syntactically forced local construction and powerful positional closure.
- source_queries_or_rows_used: attachment rows `111:1 a1`, `111:4 a1-a3`, `111:5 a1-a4`.

### S111-P2-C007 — Possessive Suffix Chain

- seed_type: morphosyntactic
- ayah_range: 111:2-5
- seed: `عنه / ماله / امرأته / جيدها`
- short title: Possession And Relation Without Rescue
- generating_set: `(E: attachment 111:2 a1 عنه complement)`, `(E: attachment 111:2 a5 ماله possessive)`, `(E: attachment 111:4 a4 امرأته possessive)`, `(E: attachment 111:5 a4 جيدها possessive)`.
- selected_branches: none.
- constructed_model: suffixes keep personal reference active while the roles shift from him, to his wealth, to his wife, to her neck.
- freeze_point: after `جيدها`.
- predictions_at_freeze: the chain should support participant continuity, not independent lexical meaning.
- unused_features_tested: rope/material closure.
- corroborators: `(C: attachment 111:5 a2 rope subject fills her-neck predicate)`.
- constraints: `(K: pronoun chain cannot establish lexical branches by itself)`.
- temporal_reactivation_notes: masculine suffixes dominate the failed-resource frame; feminine suffix closes the wife's body frame.
- rival_models: ordinary pronominal cohesion; possession-chain image of failed ownership and transferred bodily consequence.
- grade: medium
- grade_rationale: useful morphosyntactic cohesion, but it is corroborative rather than a full lexical image.
- source_queries_or_rows_used: attachment rows `111:2 a1,a5`, `111:4 a4`, `111:5 a1-a4`.

### S111-P2-C008 — Whole-Passage Temporal Assembly

- seed_type: temporal/acoustic
- ayah_range: 111:1-5
- seed: ordered recitation sequence
- short title: Agency Collapse, Failed Protection, Fire, Fuel, Binding
- generating_set: `(E: sequence 111:1 ruin/hands/name/repetition)`, `(E: sequence 111:2 failed availing)`, `(E: sequence 111:3 fire with flame)`, `(E: sequence 111:4 wife carrying firewood)`, `(E: sequence 111:5 rope in neck from material)`.
- selected_branches: none.
- constructed_model: the passage unfolds as a controlled cascade: bodily agency fails; possessed resources cannot avert; the name's flame becomes a fire; fuel and carrier appear; the carrier is closed in a neck-rope image.
- freeze_point: after ayah 5.
- predictions_at_freeze: none; this is a retrospective assembly.
- unused_features_tested: all attachment relations and repeated roots.
- corroborators: `(C: exact لهب recurrence)`, `(C: opening hands / closing neck body-part frame)`, `(C: wealth/acquisition followed by no rescue and fire)`, `(C: fire followed by firewood)`, `(C: carrier followed by rope at neck)`.
- constraints: `(K: no furuq branches available; this is constructional-temporal, not branch-lexical)`, `(K: do not replace primary reading with secondary image)`.
- temporal_reactivation_notes: strongest reactivations are `لَهَب` ayah 1→3, hands ayah 1→agency/acquisition ayah 2, fire ayah 3→firewood ayah 4, carrier ayah 4→neck rope ayah 5.
- rival_models: five independent statements; single temporal cascade.
- grade: medium-strong
- grade_rationale: highly coherent sequence from attachments and repetition; branch-level evidence missing.
- source_queries_or_rows_used: all S111 attachment rows listed above.

## Image Packet Catalog

### IMAGE-S111-001

- Starting seed: `تَبَّتْ` / opening construction
- Complete image: agency collapse unfolds into failed protection and consequence.
- Passage-order assembly: ruin → hands → name → ruin → non-availing wealth/acquisition → fire.
- Participants and roles: named man; hands as agency locus; wealth/acquisition as failed protective resources.
- Operation / mechanism: negated availing after confirmed ruin.
- Direction / force / medium: from possessed agency/resources toward failed protection.
- Temporal development: ayah 1 creates failure loop; ayah 2 explains non-availing; ayah 3 consequence follows.
- Outcome / closure: consequence proceeds to fire.
- Exact branch constituents: none available; furuq blocked.
- Unfilled roles: lexical branch images for `ت ب ب`, `ي د ي`, `غ ن ي`, `م و ل`, `ك س ب`.
- Status: FRAGMENT

### IMAGE-S111-002

- Starting seed: first `لَهَب`
- Complete image: proper-name flame becomes explicit fire-flame and draws fuel into the sequence.
- Passage-order assembly: `أَبى لهب` → `نارًا ذات لهب` → `حمالة الحطب`.
- Participants and roles: named man; fire; wife as carrier; firewood as combustible material.
- Operation / mechanism: delayed reactivation of a name component by later explicit fire.
- Direction / force / medium: semantic activation moves backward from fire to name and forward from flame to fuel.
- Temporal development: dormant name element in ayah 1, explicit fire/flame in ayah 3, fuel carrier in ayah 4.
- Outcome / closure: prepares burden/binding closure.
- Exact branch constituents: none available; furuq blocked.
- Unfilled roles: furuq branch images for `ل ه ب`, `ن و ر`, `ح م ل`, `ح ط ب`.
- Status: COMPLETE constructionally, FRAGMENT lexically

### IMAGE-S111-003

- Starting seed: `حَمَّالَةَ ٱلْحَطَبِ`
- Complete image: carrier of fuel is localized and bound at the neck by a material rope.
- Passage-order assembly: wife → carrier of firewood → in her neck → rope → from masad.
- Participants and roles: wife as carrier; firewood as carried material; neck as locus; rope as binding object; masad as material.
- Operation / mechanism: carrying/burden image resolves into locative binding.
- Direction / force / medium: burden carried by participant; binding placed at neck; rope specified by material.
- Temporal development: ayah 4 opens carrier role; ayah 5 fills bodily location and object.
- Outcome / closure: final materialized rope image.
- Exact branch constituents: none available; furuq blocked.
- Unfilled roles: furuq branch images for `م ر أ`, `ح م ل`, `ح ط ب`, `ج ي د`, `ح ب ل`, `م س د`.
- Status: COMPLETE constructionally, FRAGMENT lexically

## Final Exhaustiveness Check

After file creation, I checked the seed inventory against every rooted occurrence identifiable from S111 attachment rows and the sacred text. All 18 rooted occurrence seeds have an explicit pass above. The main textual constructions and temporal/acoustic reactivations have also been seeded separately.

The work is not exhaustive in the full Stage 1 lexical sense because the required QAC and furuq databases are unavailable at the specified paths. Exhaustive furuq branch seeding remains blocked until `resources/qac.sqlite` and `resources/furuq_v4.sqlite` are restored with schemas and data.
