# S86 Stage 1 Pass 2

## Root Cause And Recovery

Pass 1 visited only a limited number of words per finding because the prompt-named primary SQLite resources in this workspace are zero-byte placeholders: `resources/qac.sqlite` and `resources/furuq_v4.sqlite` have no schema and no rows. I recovered by using the checked-in local TSV exports generated from the same resource layer: `resources/qac_root_ayah.tsv` for QAC root/ayah metadata and `resources/v4_branches.tsv` for v4 accepted branch rows. In Pass 1 I then compressed the fallback sweep into a small number of convergence lanes. That was the immediate limitation: branch dossiers were read, but the seed-by-seed audit was not written.

This Pass 2 restarts from the first rooted word, `86:1 السَّماءِ / س م و`, and records every rooted occurrence and every accepted branch restart. The sacred Arabic source is `resources/quran/surah_86.json`. Basmala is present only as recitational opening context and was not seeded. No translation evidence is used.

Resource counts:

- Root-ayah rows inspected from `resources/qac_root_ayah.tsv`: 38.
- Rooted occurrence contexts after splitting repeated cognate or repeated imperative forms: 41.
- Distinct S86 roots with accepted branch dossiers in `resources/v4_branches.tsv`: 33.
- Accepted lexical branch restarts initiated in occurrence context: 386.
- Structural rows inspected from `resources/attachments.tsv`: S86 rows only.

## Sacred Sequence

1. وَٱلسَّمَآءِ وَٱلطَّارِقِ
2. وَمَآ أَدْرَىٰكَ مَا ٱلطَّارِقُ
3. ٱلنَّجْمُ ٱلثَّاقِبُ
4. إِن كُلُّ نَفْسٍۢ لَّمَّا عَلَيْهَا حَافِظٌۭ
5. فَلْيَنظُرِ ٱلْإِنسَٰنُ مِمَّ خُلِقَ
6. خُلِقَ مِن مَّآءٍۢ دَافِقٍۢ
7. يَخْرُجُ مِنۢ بَيْنِ ٱلصُّلْبِ وَٱلتَّرَآئِبِ
8. إِنَّهُۥ عَلَىٰ رَجْعِهِۦ لَقَادِرٌۭ
9. يَوْمَ تُبْلَى ٱلسَّرَآئِرُ
10. فَمَا لَهُۥ مِن قُوَّةٍۢ وَلَا نَاصِرٍۢ
11. وَٱلسَّمَآءِ ذَاتِ ٱلرَّجْعِ
12. وَٱلْأَرْضِ ذَاتِ ٱلصَّدْعِ
13. إِنَّهُۥ لَقَوْلٌۭ فَصْلٌۭ
14. وَمَا هُوَ بِٱلْهَزْلِ
15. إِنَّهُمْ يَكِيدُونَ كَيْدًۭا
16. وَأَكِيدُ كَيْدًۭا
17. فَمَهِّلِ ٱلْكَٰفِرِينَ أَمْهِلْهُمْ رُوَيْدًۢا

## Candidate Synthesis Units

### S86-ST1-01: Night Intrusion Becomes Piercing Disclosure

- `candidate_id`: S86-ST1-01
- `ayah_range`: 86:1-4
- `seed_type`: lexical and temporal/acoustic
- `seed`: 86:1 `الطارق`, especially `ط ر ق B001` الآتي ليلا and `ط ر ق B003` الضرب الموقّع
- `generating_set`: `(E: ط ر ق B001 night-arrival)`, `(E: ث ق ب B001 penetrating through a hole)`, `(E: ث ق ب B002 light piercing by brightness)`, `(E: ن ج م B001 star)`, `(E: س م و B004 sky/what is above and shades)`
- `selected_branches`: `ط ر ق B001,B003,B009`; `ث ق ب B001,B002`; `ن ج م B001,B002`; `س م و B004`
- `constructed_model`: A visitor appears from the elevated covering field. The first cue is not only an object in the sky but a nocturnal arrival with impact-like onset. The question in 86:2 suspends identification; 86:3 resolves it as a star whose light penetrates. The image is a dark covering field interrupted by a punctual, striking, luminous entry.
- `freeze_point`: after 86:3, before using 86:4.
- `predictions_at_freeze`: expected an unseen/hard-to-reach locus; expected watching or disclosure from above; expected penetration to become epistemic rather than merely spatial; expected a role that maintains awareness after the flash.
- `unused_features_tested`: `حافظ`, `كل نفس`, `عليها`, interrogative repetition, oath coordination, later sky-return oath.
- `corroborators`: `(C: ح ف ظ B001 guarding/keeping watch)`, `(C: ح ف ظ B004 vigilance and little heedlessness)`, `(C: attachment 86:4 حافظ predicated over every نفس)`, `(C: sequence 86:1-3 mystery then identification then universal watcher)`, `(C: ر ج ع B007 repeated sound/echo as a secondary acoustic return in later oath)`
- `constraints`: `(K: attachment 86:3 الثاقب is adjective of النجم, so penetration is a property of the star, not an independent weapon event)`, `(K: oath grammar makes السماء والطارق oath objects, not agents acting on the human self)`
- `temporal_reactivation_notes`: The first oath activates height and night arrival; the explanatory answer activates piercing light; 86:4 retroactively makes the piercing not only visual but surveillance-like: every self has a keeper over it.
- `rival_models`: `ط ر ق B002` path and `ط ر ق B009` trace-following create a weaker path/track model: a repeated trace in the sky leads attention to later return. It remains local unless joined to `ر ج ع`.
- `grade`: medium-strong
- `grade_rationale`: Specific branches match the actual lexical surface (`الطارق`, `النجم`, `الثاقب`) and the order creates real suspense and resolution. The universal guardian in 86:4 is a strong reactivation, but literal night-visitation remains subordinate to the primary star oath.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` rows for S86:1-4; `v4_branches.tsv` roots `س م و`, `ط ر ق`, `د ر ي`, `ن ج م`, `ث ق ب`, `ك ل ل`, `ن ف س`, `ح ف ظ`; `attachments.tsv` 86:1 a1, 86:2 a1-a4, 86:3 a1, 86:4 a1-a4.

### S86-ST1-02: Guarded Self Becomes Exposed Secret

- `candidate_id`: S86-ST1-02
- `ayah_range`: 86:4, 86:8-10
- `seed_type`: lexical
- `seed`: 86:4 `نفس`, especially `ن ف س B011` living soul and `ن ف س B013` what is in the self
- `generating_set`: `(E: ن ف س B011 living soul)`, `(E: ن ف س B012 self/very thing)`, `(E: ح ف ظ B001 guarding and keeping)`, `(E: ح ف ظ B002 fixed preservation in the self)`
- `selected_branches`: `ن ف س B011,B012,B013`; `ح ف ظ B001,B002,B004,B006`; `ب ل و B002`; `س ر ر B001,B014`; `ق و ي B001`; `ن ص ر B001`
- `constructed_model`: The self is not an unobserved private interior. It is a living unit placed under preservation, then later returned to a day when concealed interiors are tested and exposed. The passage builds a hidden ledger: guarded self, return-capacity, trial of secrets, no internal force and no outside helper.
- `freeze_point`: after constructing from 86:4 and 86:8-9, before using 86:10.
- `predictions_at_freeze`: expected interiority; expected exposure or testing; expected personal inability once the hidden content is made public; expected no escape from the preserving record.
- `unused_features_tested`: 86:10 negated force/helper, 86:5 imperative inspection, 86:15-17 scheming/delay.
- `corroborators`: `(C: س ر ر B001 hidden interior/secret)`, `(C: س ر ر B014 penetration into hidden matters)`, `(C: ب ل و B002 testing and appearance of reality)`, `(C: attachment 86:9 السرائر passive subject of تبلى)`, `(C: ق و ي B001 denied gathered strength)`, `(C: ن ص ر B001 denied helper)`, `(C: attachment 86:10 force and helper coordinated under negation)`
- `constraints`: `(K: حافظ is indefinite predicate over كل نفس, so the image is universal custody, not a named individual guard)`, `(K: no branch makes نفس mean merely breath here; breath/water branches can only corroborate life-source imagery elsewhere)`
- `temporal_reactivation_notes`: The watcher over every self in 86:4 is reactivated only after 86:9 reveals that what is guarded is not just bodily life but inner deposits. 86:10 then closes the hidden-ledger image by removing both self-power and external support.
- `rival_models`: `ن ف س B001` breath can seed a physiology image with `ماء دافق`, but it does not explain `السرائر` as well as B011/B013.
- `grade`: strong
- `grade_rationale`: The model is generated by local roots and tested by independently unused syntax: universal quantification, over/upon attachment, passive testing of secrets, and double negation of force/helper.
- `source_queries_or_rows_used`: S86 rows for `ن ف س`, `ح ف ظ`, `ر ج ع`, `ق د ر`, `ب ل و`, `س ر ر`, `ق و ي`, `ن ص ر`; attachments 86:4, 86:8-10.

### S86-ST1-03: Origin, Return, Rain, And Split Earth

- `candidate_id`: S86-ST1-03
- `ayah_range`: 86:5-12
- `seed_type`: verified composite
- `seed`: 86:5-7 source inquiry: `فلينظر الإنسان مم خلق / خلق من ماء دافق / يخرج من بين الصلب والترائب`
- `generating_set`: `(E: ن ظ ر B001 directing sight/intellect for examination)`, `(E: ء ن س B001 human as visible human being)`, `(E: خ ل ق B001 measuring/forming before act)`, `(E: خ ل ق B002 creating/bringing into being)`, `(E: م و ه B001 water)`, `(E: م و ه B004 male fluid in womb)`, `(E: د ف ق B001 sudden outpouring liquid)`, `(E: خ ر ج B001 emergence outward)`, `(E: ب ي ن B002 between two endpoints)`, `(E: ص ل ب B002 back/loins)`, `(E: ت ر ب B005 chest-bones/place of necklace)`
- `selected_branches`: `ن ظ ر B001`; `ء ن س B001,B002`; `خ ل ق B001,B002,B003,B011`; `م و ه B001,B004`; `د ف ق B001`; `خ ر ج B001,B002`; `ب ي ن B002`; `ص ل ب B001,B002`; `ت ر ب B005`; `ر ج ع B001,B006`; `ق د ر B003`; `س م و B004`; `ء ر ض B001`; `ص د ع B001,B003`
- `constructed_model`: The human is commanded to inspect origin. Creation is not abstract; it is measured formation from outpoured water that emerges from a between-space bounded by hard bodily structures. This local physiology then expands into a larger return ecology: sky possesses returning water and earth possesses splitting, so emergence from hidden water and between-hardness becomes a repeated cosmological mechanism.
- `freeze_point`: after 86:5-8, before the second oath in 86:11-12.
- `predictions_at_freeze`: expected another return process; expected water or repeated coming-back; expected splitting/opening after pressure or concealment; expected power over reconstitution, not only first creation.
- `unused_features_tested`: 86:11 sky with return, 86:12 earth with splitting, 86:9 testing of hidden interiors, 86:13 decisive statement.
- `corroborators`: `(C: ر ج ع B001 return/restitution)`, `(C: ق د ر B003 power/ability over act)`, `(C: ر ج ع B006 returning water/rain)`, `(C: س م و B004 sky including cloud/rain)`, `(C: ص د ع B001 splitting in solid thing)`, `(C: ص د ع B003 plant splitting earth)`, `(C: attachment 86:11-12 ذات idafa assigns return to sky and split to earth)`, `(C: sequence human-fluid emergence before sky-earth return/split)`
- `constraints`: `(K: 86:7 attachment makes بين govern الصلب والترائب as source endpoints; it does not identify the endpoints as agents)`, `(K: رجعه in 86:8 is governed by على with قادر, so return is under power, not spontaneous natural cycle only)`, `(K: the rain/plant cycle corroborates return and splitting but does not replace the primary resurrection argument)`
- `temporal_reactivation_notes`: The command to look backward to origin freezes a first-creation model. The later sky/earth oath reactivates water and emergence at a higher scale: what began as human source-fluid becomes cosmic return-water and splitting ground.
- `rival_models`: A purely biological reading using only `م و ه B004`, `د ف ق B001`, `ص ل ب B002`, `ت ر ب B005` is strong locally but less able to explain the immediate sky/earth re-oath. A purely rain/vegetation reading beginning at 86:11 explains vv11-12 but must be constrained by vv5-8.
- `grade`: strong
- `grade_rationale`: Multiple independent channels converge: source syntax, water branch, outpouring branch, between construction, return/power predicate, and later sky-earth return/splitting oath.
- `source_queries_or_rows_used`: S86 rows for `ن ظ ر`, `ء ن س`, `خ ل ق`, `م و ه`, `د ف ق`, `خ ر ج`, `ب ي ن`, `ص ل ب`, `ت ر ب`, `ر ج ع`, `ق د ر`, `س م و`, `ء ر ض`, `ص د ع`; attachments 86:5-8, 86:11-12.

### S86-ST1-04: Between Hardness And Chest: Local Emergence Channel

- `candidate_id`: S86-ST1-04
- `ayah_range`: 86:6-7
- `seed_type`: constructional
- `seed`: `من بين الصلب والترائب`
- `generating_set`: `(E: ب ي ن B002 middle/interspace between two or more)`, `(E: ص ل ب B001 hardness/solidity)`, `(E: ص ل ب B002 back/vertebrae)`, `(E: ت ر ب B005 ترائب chest bones/place of necklace)`, `(E: خ ر ج B001 outward emergence)`, `(E: د ف ق B001 outpouring liquid)`
- `selected_branches`: `ب ي ن B002,B001,B008`; `ص ل ب B001,B002`; `ت ر ب B005`; `خ ر ج B001`; `د ف ق B001`
- `constructed_model`: A liquid emergence is situated in an interval between firm bodily structures. The interspace matters more than either endpoint alone: the passage activates boundedness, pressure/flow, and a hidden source channel.
- `freeze_point`: after 86:7.
- `predictions_at_freeze`: expected later reactivation of splitting or opening; expected a return from hiddenness; expected an outer/inward contrast.
- `unused_features_tested`: 86:8 return, 86:9 secrets tested, 86:12 earth with split.
- `corroborators`: `(C: ر ج ع B001 return)`, `(C: س ر ر B001 hidden interior)`, `(C: ص د ع B001 split in solid)`, `(C: attachment 86:7 بين construct completed by two coordinated genitives)`
- `constraints`: `(K: ت ر ب B001 dust/earth and B002 poverty-by-dust are not passage-local for ترائب here)`, `(K: ص ل ب B005 crucifixion is branch-remote and has no local role)`
- `temporal_reactivation_notes`: The between-hardness image is first bodily; 86:12 later replays it on earth as solid matter opened by split.
- `rival_models`: `ب ي ن B001` separation can seed a parting model, but `بين` in the attachment row is syntactically an interspace, so B002 dominates.
- `grade`: medium-strong
- `grade_rationale`: Strong local syntax and branch support, narrower than the larger origin-return model.
- `source_queries_or_rows_used`: S86 rows for 86:6-7 plus later tests 86:8-12; attachments 86:6 a1-a2, 86:7 a1-a4.

### S86-ST1-05: Decisive Speech As Separating Cut

- `candidate_id`: S86-ST1-05
- `ayah_range`: 86:11-14
- `seed_type`: lexical and constructional
- `seed`: 86:13 `قول فصل`
- `generating_set`: `(E: ق و ل B001 speech brought out in utterance)`, `(E: ف ص ل B001 separating one thing from another until a boundary appears)`, `(E: ف ص ل B002 judgment separating truth from falsehood)`, `(E: ف ص ل B013 detailing and distinguishing parts/meanings)`
- `selected_branches`: `ق و ل B001,B014,B016`; `ف ص ل B001,B002,B004,B011,B013`; `ه ز ل B001`; `ص د ع B004`; `ب ي ن B005`
- `constructed_model`: The passage's statement is not loose play; it is a word whose force is to separate, define, judge, and make boundaries visible. The preceding earth-splitting image supplies a physical analogue: what is closed is opened; what is mixed is distinguished.
- `freeze_point`: after 86:13, before 86:14.
- `predictions_at_freeze`: expected denial of unserious speech; expected opposition to deceptive plotting; expected a closure where speech prevails without hurry.
- `unused_features_tested`: 86:14 negated هزل, 86:15-17 scheme/counter-scheme/delay, 86:12 الصدع.
- `corroborators`: `(C: ه ز ل B001 speech with no seriousness/play)`, `(C: attachment 86:14 بالهزل is denied predicate complement)`, `(C: ص د ع B004 open proclamation/final separation of truth)`, `(C: ف ص ل B011 verse endings/fواصل as secondary formal support)`, `(C: ق و ل B014 thing's indication and B016 definition/limit as secondary)`
- `constraints`: `(K: قول فصل is nominal predication, not a described physical blade)`, `(K: ف ص ل B003 weaning and B006 water-channel are local dead branches here)`
- `temporal_reactivation_notes`: After origin/return and hidden-testing, the passage reinterprets itself as a separating utterance. The denial of play blocks treating the imagery as amusement or empty verbal display.
- `rival_models`: A purely formal fواصل model from `ف ص ل B011` can explain sound closure but not judgment; it remains corroborative.
- `grade`: strong
- `grade_rationale`: The `قول` plus `فصل` construction is explicit, and `وما هو بالهزل` gives direct independent constraint/corroboration.
- `source_queries_or_rows_used`: S86 rows for `س م و`, `ر ج ع`, `ء ر ض`, `ص د ع`, `ق و ل`, `ف ص ل`, `ه ز ل`; attachments 86:11-14.

### S86-ST1-06: Scheme Answered By Greater Scheme Under Delay

- `candidate_id`: S86-ST1-06
- `ayah_range`: 86:15-17
- `seed_type`: lexical, morphosyntactic, temporal/acoustic
- `seed`: repeated `ك ي د` in 86:15-16
- `generating_set`: `(E: ك ي د B001 severe handling/working at a thing)`, `(E: ك ي د B002 plot, stratagem, and hidden attempt at harm)`, `(E: attachment 86:15 and 86:16 cognate accusatives intensify each كيد)`
- `selected_branches`: `ك ي د B001,B002,B003,B004,B006`; `م ه ل B001`; `ر و د B005`; `ك ف ر B001,B003`; `ه ز ل B001`
- `constructed_model`: Human plotting is mirrored by divine counter-plotting. The repeated cognate accusative thickens the action, while the closure does not rush into visible impact; it commands deliberate delay. The counter-scheme is not absence of response but controlled timing.
- `freeze_point`: after 86:16, before 86:17.
- `predictions_at_freeze`: expected command not to panic; expected withheld or delayed resolution; expected the addressees to be marked by covering/denial; expected closure by small interval.
- `unused_features_tested`: 86:17 `فمهل`, `أمهلهم`, `رويداً`, `الكافرين`.
- `corroborators`: `(C: م ه ل B001 deliberateness, delay, leaving haste)`, `(C: ر و د B005 gentle/slight delay in رويد)`, `(C: attachment 86:17 رويدا adverbially limits أمهلهم)`, `(C: ك ف ر B001 covering and B003 denial of truth for الكافرين)`, `(C: repeated imperative مهل/أمهل)`
- `constraints`: `(K: كيد B004 war remains possible as branch background but the local grammar is plotting/scheming, not an open battle scene)`, `(K: م ه ل B003 molten residue has no role in the final imperative except as a terminated lexical branch)`
- `temporal_reactivation_notes`: The decisive speech in 86:13-14 prevents the scheme from being read as effective; 86:17 delays the visible answer, preserving control and expectation.
- `rival_models`: `ك ي د B003` struggling at death can locally echo no-force/no-helper, but it does not generate the closure as well as B002.
- `grade`: medium-strong
- `grade_rationale`: Strong local repetition and syntax, good corroboration by delay imperatives. Less passage-wide than the origin-return and guarded-secret units.
- `source_queries_or_rows_used`: S86 rows for `ك ي د`, `م ه ل`, `ر و د`, `ك ف ر`; attachments 86:15 a1-a3, 86:16 a1, 86:17 a1-a3.

### S86-ST1-07: Recurrent Sky-Earth Witness Reorganizes The Whole Passage

- `candidate_id`: S86-ST1-07
- `ayah_range`: 86:1-3, 86:11-12
- `seed_type`: temporal/acoustic and constructional
- `seed`: repeated oath with `السماء`: 86:1 `والسماء والطارق`, 86:11 `والسماء ذات الرجع`
- `generating_set`: `(E: س م و B004 sky/what is above)`, `(E: ط ر ق B001 night arrival)`, `(E: ر ج ع B006 returning water/rain)`, `(E: ء ر ض B001 lower opposite of sky)`, `(E: ص د ع B001 split in solid thing)`, `(E: ص د ع B003 plant splitting earth)`
- `selected_branches`: `س م و B004,B001`; `ط ر ق B001,B009`; `ر ج ع B006,B001`; `ء ر ض B001,B002`; `ص د ع B001,B003,B006`
- `constructed_model`: The first sky oath presents a vertical field pierced by a returning/arriving light. The second sky oath returns to the same vertical field but now gives it a recurring action, then pairs it with earth that opens. The passage thereby converts sky from spectacle into mechanism: above returns; below splits.
- `freeze_point`: after 86:12.
- `predictions_at_freeze`: expected the intervening human-origin argument to be reinterpreted as one instance of return plus emergence; expected the final speech to present this as decisive, not decorative.
- `unused_features_tested`: `قول فصل`, `ما هو بالهزل`, origin water in 86:6, return in 86:8.
- `corroborators`: `(C: م و ه B001 water)`, `(C: د ف ق B001 outpoured liquid)`, `(C: ر ج ع B001 return in 86:8)`, `(C: ق و ل B001 + ف ص ل B002 decisive word after oaths)`, `(C: attachment 86:1 and 86:11 oath governance)`
- `constraints`: `(K: س م و B005 name/signification is branch-relevant only as remote support for oath naming, not generating evidence)`, `(K: ء ر ض B010 termite and related earth-remote branches terminate)`
- `temporal_reactivation_notes`: Hearing 86:11 makes 86:1 newly active: the same sky now carries a second property. The first piercing star and later returning rain become paired vertical descents, while earth split answers hidden emergence.
- `rival_models`: A pure agricultural rain/earth model from 86:11-12 is viable but must remain corroborative of the human return argument.
- `grade`: medium-strong
- `grade_rationale`: The repetition of sky and the paired idafa structures create a real temporal reactivation. The mechanism is strong as a passage-level image but secondary to the explicit human return statement.
- `source_queries_or_rows_used`: S86 rows for `س م و`, `ط ر ق`, `ن ج م`, `ث ق ب`, `ر ج ع`, `ء ر ض`, `ص د ع`, plus 86:5-8 roots for testing.

### S86-ST1-08: Directed Looking Into Origin And Hidden Knowledge

- `candidate_id`: S86-ST1-08
- `ayah_range`: 86:2, 86:5, 86:9
- `seed_type`: lexical and morphosyntactic
- `seed`: 86:5 `فلينظر الإنسان`
- `generating_set`: `(E: ن ظ ر B001 directing eye or insight to perceive/examine)`, `(E: ء ن س B001 visible human being)`, `(E: د ر ي B001 knowing/being made to know)`, `(E: س ر ر B001 hidden interior)`
- `selected_branches`: `ن ظ ر B001,B008,B009,B010`; `ء ن س B001,B002,B005`; `د ر ي B001`; `س ر ر B001,B014`; `ب ل و B002`
- `constructed_model`: The passage alternates between what the addressee does not know, what the human is ordered to inspect, and what will be made manifest from within. Looking begins as commanded reflection on origin and ends as exposure of what was secret.
- `freeze_point`: after 86:5, before 86:9.
- `predictions_at_freeze`: expected a hidden object; expected later disclosure/test; expected inner material rather than surface observation alone.
- `unused_features_tested`: `السرائر`, `تبلى`, `حافظ`, `الثاقب`.
- `corroborators`: `(C: ب ل و B002 testing and appearance of reality)`, `(C: ث ق ب B001/B002 piercing as earlier visual penetration)`, `(C: ح ف ظ B002 preservation in memory/self)`, `(C: attachment 86:5 لينظر governs embedded question مم خلق)`
- `constraints`: `(K: ن ظ ر B002 delay belongs more strongly to 86:17 via مهل/رويد, not to the imperative looking in 86:5)`, `(K: د ر ي B003 hunting concealment and B005 target-practice are remote and terminate here)`
- `temporal_reactivation_notes`: The formula `ما أدراك` creates a knowledge gap. `فلينظر` converts the hearer from passive recipient of the question into examiner of origin. `تبلى السرائر` later makes the object of knowing interior and involuntary.
- `rival_models`: `ء ن س B005` eye-image can generate a visual micro-model, but it is too narrow without `ن ظ ر B001`.
- `grade`: medium
- `grade_rationale`: Coherent temporal cognition lane, but much of the model is constructional rather than a single tight lexical avalanche.
- `source_queries_or_rows_used`: S86 rows for `د ر ي`, `ن ظ ر`, `ء ن س`, `خ ل ق`, `ب ل و`, `س ر ر`; attachments 86:2, 86:5, 86:9.

### S86-ST1-09: Impact, Echo, And Measured Recitation Pressure

- `candidate_id`: S86-ST1-09
- `ayah_range`: 86:1-3, 86:8, 86:11, 86:15-17
- `seed_type`: temporal/acoustic
- `seed`: recurrent impact and repetition patterns: `طارق`, `ثاقب`, `رجع`, `يكيدون كيدا / أكيد كيدا`, `مهل / أمهلهم`
- `generating_set`: `(E: ط ر ق B003 rhythmic striking)`, `(E: ث ق ب B001 penetration)`, `(E: ر ج ع B007 repeated sound/echo)`, `(E: ك ي د cognate accusative construction)`, `(E: م ه ل B001 delay/withholding haste)`
- `selected_branches`: `ط ر ق B003,B014`; `ث ق ب B001`; `ر ج ع B007`; `ك ي د B001,B002`; `م ه ل B001`; `ر و د B005`
- `constructed_model`: The recitation produces repeated pressure: night-strike, piercing point, return/echo, doubled scheme, counter-doubled scheme, and softened delay. The acoustic motion supports the semantic structure of impact answered by controlled return.
- `freeze_point`: after 86:16, before final `رويدا`.
- `predictions_at_freeze`: expected deceleration or controlled closure; expected no immediate explosive ending.
- `unused_features_tested`: final `رويدا`, negated `هزل`, decisive `فصل`.
- `corroborators`: `(C: ر و د B005 gentle/slight delay)`, `(C: ف ص ل B011 formal verse divisions as secondary)`, `(C: ه ز ل B001 denial of empty play constrains acoustic pleasure)`
- `constraints`: `(K: acoustic recurrence is corroborative, not a substitute for lexical meaning)`, `(K: ط ر ق B014 single note is remote; it can support sound only weakly)`
- `temporal_reactivation_notes`: The final softening replays the earlier strike under restraint: the passage that opened with a night-strike closes by telling the addressee to delay them gently.
- `rival_models`: A pure sound-symbolic model is insufficient; it works only as a secondary simulation attached to lexical candidates.
- `grade`: medium
- `grade_rationale`: Repetition and cognate accusatives are concrete, but the sound-pressure image depends on multiple secondary branches.
- `source_queries_or_rows_used`: S86 branch rows for `ط ر ق`, `ث ق ب`, `ر ج ع`, `ك ي د`, `م ه ل`, `ر و د`, `ف ص ل`, `ه ز ل`; attachments 86:15-17.

### S86-ST1-10: Covering Denial Versus Uncovering Trial

- `candidate_id`: S86-ST1-10
- `ayah_range`: 86:9, 86:14-17
- `seed_type`: lexical
- `seed`: 86:17 `الكافرين`, especially `ك ف ر B001` covering and `ك ف ر B003` denial of truth
- `generating_set`: `(E: ك ف ر B001 covering/concealing)`, `(E: ك ف ر B003 denial and obstruction of truth)`, `(E: س ر ر B001 hidden secret)`, `(E: ب ل و B002 test and disclosure)`
- `selected_branches`: `ك ف ر B001,B003,B008`; `س ر ر B001`; `ب ل و B002`; `ه ز ل B001`; `ك ي د B002`
- `constructed_model`: Those named at the close are coverers of truth, but the passage has already announced that hidden interiors will be tested. Their scheming attempts to keep control of covered reality; the decisive non-playful word and delayed counter-scheme hold them inside exposure-time.
- `freeze_point`: after `الكافرين` in 86:17, backward-tested against 86:9 and 86:14-16.
- `predictions_at_freeze`: expected concealment vocabulary earlier; expected exposure or testing; expected false seriousness/play contrast.
- `unused_features_tested`: `السرائر`, `تبلى`, `وما هو بالهزل`, `يكيدون`.
- `corroborators`: `(C: س ر ر B001 hidden interior)`, `(C: ب ل و B002 appearance of reality under test)`, `(C: ه ز ل B001 denied unserious speech)`, `(C: ك ي د B002 covert stratagem)`, `(C: attachment 86:17 الكافرين direct object of مهل)`
- `constraints`: `(K: ك ف ر B008 covering seed/burying grain has agricultural overlap with earth split but is not the contextual sense of الكافرين)`, `(K: the final command delays them; it does not describe their immediate exposure inside 86:17)`
- `temporal_reactivation_notes`: The final naming of the disbelievers reactivates the entire hidden/exposed axis: covered truth meets tested secrets and decisive speech.
- `rival_models`: Agricultural covering `B008` could join rain/earth split, but it is a remote pun-like branch and remains terminated for the main model.
- `grade`: medium
- `grade_rationale`: Strong backward reactivation to hiddenness and testing, but the lexical role of `كفر` is final and does not independently organize the earlier origin section.
- `source_queries_or_rows_used`: S86 rows for `ك ف ر`, `س ر ر`, `ب ل و`, `ه ز ل`, `ك ي د`, `م ه ل`; attachments 86:9, 86:14-17.

## Exhaustive Lexical Seed Coverage Catalog

Legend: `G` generated a candidate before freeze; `C` corroborated or constrained after freeze; `L` produced a local image only; `T` terminated with no passage-local synthesis. Every accepted branch listed below was restarted in the occurrence context shown.

Exact accepted branch inventory by root:

- `ء ر ض`: `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012`
- `ء ن س`: `B001,B002,B003,B004,B005,B006`
- `ب ل و`: `B001,B002,B003,B004,B005,B006,B007,B008,B009`
- `ب ي ن`: `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012`
- `ت ر ب`: `B001,B002,B003,B004,B005,B006,B007,B008,B009`
- `ث ق ب`: `B001,B002,B003,B004,B005,B006`
- `ح ف ظ`: `B001,B002,B003,B004,B005,B006,B007`
- `خ ر ج`: `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013`
- `خ ل ق`: `B001,B002,B003,B004,B005,B007,B008,B009,B010,B011,B012`
- `د ر ي`: `B001,B002,B003,B004,B005,B006`
- `د ف ق`: `B001,B002,B003,B004,B005,B006,B007`
- `ر ج ع`: `B001,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014,B015`
- `ر و د`: `B001,B002,B003,B004,B005,B006,B007,B008`
- `س ر ر`: `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014,B015`
- `س م و`: `B001,B002,B003,B004,B005,B006,B007,B008`
- `ص د ع`: `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011`
- `ص ل ب`: `B001,B002,B003,B004,B005,B006,B007`
- `ط ر ق`: `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014`
- `ف ص ل`: `B001,B002,B003,B004,B005,B006,B007,B009,B010,B011,B012,B013,B014,B015,B016`
- `ق د ر`: `B001,B003,B004,B005,B006,B007`
- `ق و ل`: `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014,B015,B016`
- `ق و ي`: `B001,B002,B003,B004,B005,B006`
- `ك ف ر`: `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014,B015`
- `ك ل ل`: `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011`
- `ك ي د`: `B001,B002,B003,B004,B005,B006,B007,B008`
- `م ه ل`: `B001,B002,B003,B004`
- `م و ه`: `B001,B002,B003,B004,B005,B006,B007,B008`
- `ن ج م`: `B001,B002,B003,B005,B006,B007,B008`
- `ن ص ر`: `B001,B002,B003,B004,B005,B006,B007`
- `ن ظ ر`: `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010`
- `ن ف س`: `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014,B015,B016`
- `ه ز ل`: `B001,B002,B003,B004`
- `ي و م`: `B001,B002,B003`

- `86:1 س م و / السَّماءِ`: branches initiated `B001-B008`. `G/C`: `B001(C S86-ST1-01,S86-ST1-07)`, `B004(G S86-ST1-01,S86-ST1-07)`, `B005(L naming/signifying only)`. `T`: `B002,B003,B006,B007,B008`.
- `86:1 ط ر ق / الطارق`: branches initiated `B001-B014`. `G/C`: `B001(G S86-ST1-01,S86-ST1-07)`, `B003(G S86-ST1-09)`, `B007(C layer/cover support)`, `B009(C trace-following/path recurrence)`, `B014(L weak acoustic)`. `T`: `B002,B004,B005,B006,B008,B010,B011,B012,B013`.
- `86:2 د ر ي / أدراك`: branches initiated `B001-B006`. `G/C`: `B001(G S86-ST1-08)`. `L`: `B003` hidden pursuit, `B004` pointed instrument, `B005` target for practice. `T`: `B002,B006`.
- `86:2 ط ر ق / الطارق`: branches restarted `B001-B014` in interrogative context. `G/C`: `B001(C mystery-object reactivation)`, `B003(C impact sound)`, `B009(L trace question)`. `T`: `B002,B004,B005,B006,B007,B008,B010,B011,B012,B013,B014`.
- `86:3 ن ج م / النجم`: branches initiated `B001,B002,B003,B005,B006,B007,B008`. `G/C`: `B001(G S86-ST1-01)`, `B002(C emergence/appearance)`, `B007(C clearing sky, weak)`. `T`: `B003,B005,B006,B008`.
- `86:3 ث ق ب / الثاقب`: branches initiated `B001-B006`. `G/C`: `B001(G S86-ST1-01,S86-ST1-09)`, `B002(G S86-ST1-01)`, `B006(L passage through thickness, later split echo)`. `T`: `B003,B004,B005`.
- `86:4 ك ل ل / كل`: branches initiated `B001-B011`. `G/C`: `B003(C totality/allness for every self)`, `B005(L enclosing crown/ring, weak)`, `B006(L covering tent, weak)`. `T`: `B001,B002,B004,B007,B008,B009,B010,B011`.
- `86:4 ن ف س / نفس`: branches initiated `B001-B016`. `G/C`: `B011(G S86-ST1-02)`, `B012(G S86-ST1-02)`, `B013(C interior intention/secret)`, `B001(L breath physiology)`, `B005(C birth/source lane)`, `B008(C water-life lane)`, `B009(C opening/splitting lane)`, `B015(C delay/space lane)`. `T`: `B002,B003,B004,B006,B007,B010,B014,B016`.
- `86:4 ح ف ظ / حافظ`: branches initiated `B001-B007`. `G/C`: `B001(G S86-ST1-02)`, `B002(G/C preservation in self)`, `B004(C vigilance)`, `B006(C guarded inviolability, weak)`, `B007(L straight path, weak).` `T`: `B003,B005`.
- `86:5 ن ظ ر / ينظر`: branches initiated `B001-B010`. `G/C`: `B001(G S86-ST1-03,S86-ST1-08)`, `B002(C delay only in final section, not local)`, `B008(L eye image)`, `B009(C watcher echo)`, `B010(L mutual examination).` `T`: `B003,B004,B005,B006,B007`.
- `86:5 ء ن س / الإنسان`: branches initiated `B001-B006`. `G/C`: `B001(G human subject)`, `B002(C seeing/sensing in inspection lane)`, `B005(L eye image)`, `B006(C self/inner person, weak)`. `T`: `B003,B004`.
- `86:5 خ ل ق / خلق`: branches initiated `B001,B002,B003,B004,B005,B007,B008,B009,B010,B011,B012`. `G/C`: `B001(G measured formation)`, `B002(G creation/bringing into being)`, `B003(C completed form)`, `B004(C inner nature, weak to secrets)`, `B011(C water-holding hollow, weak).` `T`: `B005,B007,B008,B009,B010,B012`.
- `86:6 خ ل ق / خلق`: same branches restarted in source-material context. `G/C`: `B001(G)`, `B002(G)`, `B003(C)`, `B011(C water-holding hollow, weak).` `T`: `B004,B005,B007,B008,B009,B010,B012`.
- `86:6 م و ه / ماء`: branches initiated `B001-B008`. `G/C`: `B001(G water)`, `B004(G reproductive water)`, `B002(C abundance/entry of water)`, `B003(C pouring/supplying water, weak)`, `B006(L waterlike radiance, weak).` `T`: `B005,B007,B008`.
- `86:6 د ف ق / دافق`: branches initiated `B001-B007`. `G/C`: `B001(G outpoured liquid)`, `B002(C suddenness)`, `B003(C fast motion, weak)`, `B004(C member protrusion, local body-channel support).` `T`: `B005,B006,B007`.
- `86:7 خ ر ج / يخرج`: branches initiated `B001-B013`. `G/C`: `B001(G emergence outward)`, `B002(C extraction from hiddenness)`, `B005(C sky clearing, weak link to sky oath).` `T`: `B003,B004,B006,B007,B008,B009,B010,B011,B012,B013`.
- `86:7 ب ي ن / بين`: branches initiated `B001-B012`. `G/C`: `B002(G interspace)`, `B001(C separation)`, `B004(C disclosure/clarity)`, `B005(C speech disclosure to S86-ST1-05)`, `B008(C opening away from adjoining part).` `T`: `B003,B006,B007,B009,B010,B011,B012`.
- `86:7 ص ل ب / الصلب`: branches initiated `B001-B007`. `G/C`: `B001(G hardness)`, `B002(G back/loins/vertebral line)`, `B007(C lineage/origin, weak).` `T`: `B003,B004,B005,B006`.
- `86:7 ت ر ب / الترائب`: branches initiated `B001-B009`. `G/C`: `B005(G chest bones/place of necklace)`, `B001(C dust/earth only remote to earth oath)`. `T`: `B002,B003,B004,B006,B007,B008,B009`.
- `86:8 ر ج ع / رجعه`: branches initiated `B001,B003-B015`. `G/C`: `B001(G return/restitution)`, `B005(C answer/word return)`, `B006(C rain/water return to later oath)`, `B007(C sound echo),` `B010(L hand returning to weapon, terminated as literal).` `T`: `B003,B004,B008,B009,B011,B012,B013,B014,B015`.
- `86:8 ق د ر / قادر`: branches initiated `B001,B003,B004,B005,B006,B007`. `G/C`: `B003(G power/ability)`, `B001(C measured limit/appointed extent)`, `B005(C planning by measure)`, `B006(C fitting to measure).` `T`: `B004,B007`.
- `86:9 ي و م / يوم`: branches initiated `B001-B003`. `G/C`: `B002(G time-span)`, `B003(C severe event/day).` `T`: `B001` as mere daylight.
- `86:9 ب ل و / تبلى`: branches initiated `B001-B009`. `G/C`: `B002(G testing and manifestation)`, `B001(C wear/laying bare, weak)`, `B003(L trial by good/bad)`, `B004(L excuse/oath exposure).` `T`: `B005,B006,B007,B008,B009`.
- `86:9 س ر ر / السرائر`: branches initiated `B001-B015`. `G/C`: `B001(G hidden secret)`, `B005(C innermost choice place)`, `B006(C navel/source echo, weak)`, `B008(C hollow interior, weak)`, `B014(C entering hidden matters).` `T`: `B002,B003,B004,B007,B009,B010,B011,B012,B013,B015`.
- `86:10 ق و ي / قوة`: branches initiated `B001-B006`. `G/C`: `B001(C denied gathered strength)`. `T`: `B002,B003,B004,B005,B006`.
- `86:10 ن ص ر / ناصر`: branches initiated `B001-B007`. `G/C`: `B001(C denied helper)`, `B004(C rain/help in sky-earth lane, weak)`, `B007(C water-channel, weak).` `T`: `B002,B003,B005,B006`.
- `86:11 س م و / السماء`: branches restarted `B001-B008`. `G/C`: `B004(G sky in return oath)`, `B001(C height)`, `B005(L sign/name, weak).` `T`: `B002,B003,B006,B007,B008`.
- `86:11 ر ج ع / الرجع`: branches restarted `B001,B003-B015`. `G/C`: `B006(G rain/returning water)`, `B001(C return to first creation and 86:8)`, `B007(C sound/echo lane),` `B005(C returned word/answer, weak).` `T`: `B003,B004,B008,B009,B010,B011,B012,B013,B014,B015`.
- `86:12 ء ر ض / الأرض`: branches initiated `B001-B012`. `G/C`: `B001(G lower opposite of sky)`, `B002(C fertile earth/plant lane)`, `B006(C staying to earth, weak).` `T`: `B003,B004,B005,B007,B008,B009,B010,B011,B012`.
- `86:12 ص د ع / الصدع`: branches initiated `B001-B011`. `G/C`: `B001(G split in solid)`, `B003(G plant splitting earth)`, `B004(C decisive proclamation/final separation)`, `B006(C split dawn/opening, weak).` `T`: `B002,B005,B007,B008,B009,B010,B011`.
- `86:13 ق و ل / قول`: branches initiated `B001-B016`. `G/C`: `B001(G uttered speech)`, `B014(C thing's indication)`, `B016(C definition/limit),` `B009(L mutual negotiation, weak).` `T`: `B002,B003,B004,B005,B006,B007,B008,B010,B011,B012,B013,B015`.
- `86:13 ف ص ل / فصل`: branches initiated `B001,B002,B003,B004,B005,B006,B007,B009,B010,B011,B012,B013,B014,B015,B016`. `G/C`: `B001(G separation/ boundary)`, `B002(G judgment)`, `B004(C articulate tongue)`, `B011(C formal verse divisions)`, `B013(C detailed distinction).` `T`: `B003,B005,B006,B007,B009,B010,B012,B014,B015,B016`.
- `86:14 ه ز ل / الهزل`: branches initiated `B001-B004`. `G/C`: `B001(C denied play/unserious speech)`, `B002(C weakness by loss, remote contrast to decisive speech).` `T`: `B003,B004`.
- `86:15 ك ي د / يكيدون كيدا`: branches initiated `B001-B008` for the verb and restarted for the cognate accusative. `G/C`: `B001(G severe handling)`, `B002(G scheming)`, `B003(C death-struggle echo to no-force lane, weak)`, `B004(C conflict/war background)`, `B006(C delayed fire, weak).` `T`: `B005,B007,B008`.
- `86:16 ك ي د / أكيد كيدا`: branches restarted `B001-B008` for divine counter-action and cognate accusative. `G/C`: `B001(G counter-handling)`, `B002(G counter-scheme)`, `B006(C delayed ignition, weak).` `T`: `B003,B004,B005,B007,B008`.
- `86:17 م ه ل / مهل وأمهل`: branches initiated `B001-B004` for both imperative forms. `G/C`: `B001(G delay/forbearance)`, `B002(L precedence/advance, weak)`, `B004(L upright moderation, weak).` `T`: `B003`.
- `86:17 ك ف ر / الكافرين`: branches initiated `B001-B015`. `G/C`: `B001(G covering)`, `B003(G denial of truth)`, `B008(C seed-covering remote to earth lane)`, `B009(C covering/removal of sin, contrast only)`, `B013(L hidden pass, weak).` `T`: `B002,B004,B005,B006,B007,B010,B011,B012,B014,B015`.
- `86:17 ر و د / رويدا`: branches initiated `B001-B008`. `G/C`: `B005(G gentle delay)`, `B003(C seeking/going out, weak),` `B004(C coming-and-going delay, weak).` `T`: `B001,B002,B006,B007,B008`.

## Constructional And Temporal Seed Coverage

- `Oath coordination 86:1`: generated S86-ST1-01; attachment a1 constrains both `السماء` and `الطارق` as genitive oath objects.
- `ما أدراك ما الطارق 86:2`: generated S86-ST1-08 as knowledge-gap construction; attachments a1-a4 constrain `الطارق` as predicate answer to the embedded `ما`.
- `النجم الثاقب 86:3`: generated S86-ST1-01; attachment a1 makes `الثاقب` an adjective of `النجم`, constraining penetration to the star's quality.
- `إن كل نفس لما عليها حافظ 86:4`: generated S86-ST1-02; attachments a1-a4 support universal self under over/upon guarding.
- `فلينظر الإنسان مم خلق 86:5`: generated S86-ST1-03 and S86-ST1-08; attachments a1-a3 make the human subject and the source-question complement.
- `خلق من ماء دافق 86:6`: generated S86-ST1-03; attachments a1-a2 bind source material and adjective.
- `يخرج من بين الصلب والترائب 86:7`: generated S86-ST1-04; attachments a1-a4 bind source interspace and two coordinated endpoints.
- `إنه على رجعه لقادر 86:8`: generated return-capacity in S86-ST1-03 and tested S86-ST1-02; attachments a1-a4 make return governed under power.
- `يوم تبلى السرائر 86:9`: generated exposed-secret lane in S86-ST1-02 and S86-ST1-10; attachments a1-a2 make the day an adverbial frame and secrets passive subject.
- `فما له من قوة ولا ناصر 86:10`: corroborated S86-ST1-02; attachments a1-a5 show coordinated denied resources under negation.
- `والسماء ذات الرجع / والأرض ذات الصدع 86:11-12`: generated S86-ST1-07 and corroborated S86-ST1-03; attachments make `الرجع` and `الصدع` idafa complements of `ذات`.
- `إنه لقول فصل / وما هو بالهزل 86:13-14`: generated S86-ST1-05; attachments establish nominal predication and denial of `هزل`.
- `إنهم يكيدون كيدا / وأكيد كيدا 86:15-16`: generated S86-ST1-06; cognate accusatives intensify both sides.
- `فمهل الكافرين أمهلهم رويدا 86:17`: generated closure-delay in S86-ST1-06 and S86-ST1-10; attachments make `الكافرين` object, suffix object, and `رويدا` adverbial limiter.

## Terminated Branch Families

The following recurrent branch families were explicitly restarted but did not produce passage-local synthesis beyond weak local echoes:

- animal, tribe, place-name, and proper-name branches: `ب ل و B008`, `ت ر ب B008`, `ن ص ر B006`, and comparable rows.
- bodily disease branches without local support: `ء ر ض B008-B012`, `ص ل ب B003`, `س ر ر B007`, `ن ظ ر B007`, `ه ز ل B002-B004`.
- commerce/game/tool branches with no passage roles: `ن ف س B016`, `خ ر ج B003,B010,B012`, `ر ج ع B011`, `ق و ي B004,B005`, `ف ص ل B012`.
- literal combat/weapon branches were constrained unless the local syntax supplied agents and targets: `ص ل ب B005`, `د ر ي B004-B005`, `ر ج ع B010`, `ك ي د B004`.
- agricultural branches were kept only as corroboration after the sky-return/earth-split oath; they were not allowed to replace the primary human-origin and return argument.

## Image Packet Catalog

### IMAGE_ID: S86-IMG-01 Night Piercing Watch

- Starting seed: `ط ر ق B001` at 86:1.
- Complete image: elevated dark field, night visitor, piercing star, universal watcher.
- Passage-order assembly: sky oath -> mysterious visitor -> star that pierces -> every self under keeper.
- Participants and roles: sky field, arriving/piercing star, self, keeper.
- Operation / mechanism: appearance by night, luminous penetration, watch/preservation.
- Direction / force / medium: from above into darkness; medium is sky/night.
- Temporal development: mystery, answer, reactivation as surveillance.
- Outcome / closure: self is not unobserved.
- Exact branch constituents: `س م و B004`, `ط ر ق B001`, `ث ق ب B001,B002`, `ن ج م B001`, `ح ف ظ B001`.
- Unfilled roles: none for local image.
- Status: COMPLETE.

### IMAGE_ID: S86-IMG-02 Origin Return Cycle

- Starting seed: 86:5 source inquiry.
- Complete image: human formed from outpoured water, emerging from bounded bodily interval, then return demonstrated by sky water and earth split.
- Passage-order assembly: look at creation -> water source -> emergence from between -> power over return -> sky return -> earth split.
- Participants and roles: human, source-water, bounded body structures, powerful returner, sky, earth.
- Operation / mechanism: formation, outpouring, emergence, return, splitting.
- Direction / force / medium: fluid outward from hidden source; rain downward/returning; earth opening upward.
- Temporal development: first creation becomes prediction of re-creation.
- Outcome / closure: return is lexically and structurally plausible.
- Exact branch constituents: `ن ظ ر B001`, `خ ل ق B001,B002`, `م و ه B001,B004`, `د ف ق B001`, `خ ر ج B001`, `ب ي ن B002`, `ص ل ب B002`, `ت ر ب B005`, `ر ج ع B001,B006`, `ص د ع B001,B003`.
- Unfilled roles: none for passage-scale image.
- Status: COMPLETE.

### IMAGE_ID: S86-IMG-03 Guarded Hidden Ledger

- Starting seed: `ن ف س B011/B013` at 86:4.
- Complete image: every living self has preserved interior contents that will be tested and exposed when no force or helper remains.
- Passage-order assembly: every self guarded -> return under power -> day secrets are tested -> no force/helper.
- Participants and roles: self, keeper, secret interiors, testing day, absent supports.
- Operation / mechanism: preservation, inward concealment, trial/exposure, stripping of supports.
- Direction / force / medium: inward/private to outward/disclosed.
- Temporal development: watcher becomes record; secret becomes tested object.
- Outcome / closure: no escape through strength or aid.
- Exact branch constituents: `ن ف س B011,B012,B013`, `ح ف ظ B001,B002`, `ب ل و B002`, `س ر ر B001,B014`, `ق و ي B001`, `ن ص ر B001`.
- Unfilled roles: none.
- Status: COMPLETE.

### IMAGE_ID: S86-IMG-04 Separating Speech

- Starting seed: `قول فصل`.
- Complete image: utterance that distinguishes, judges, defines, and is denied play.
- Passage-order assembly: sky/earth signs -> statement is separating word -> not play -> schemes answered under delay.
- Participants and roles: speech, separation boundary, unserious rival, schemers.
- Operation / mechanism: verbal disclosure and judgment.
- Direction / force / medium: from uttered word into mixed/hidden reality.
- Temporal development: physical splitting becomes verbal/legal separation.
- Outcome / closure: speech has serious force over plots.
- Exact branch constituents: `ق و ل B001`, `ف ص ل B001,B002,B013`, `ه ز ل B001`, `ص د ع B004`.
- Unfilled roles: none.
- Status: COMPLETE.

### IMAGE_ID: S86-IMG-05 Counter-Scheme Delayed

- Starting seed: `ك ي د B002` at 86:15.
- Complete image: human plotting is mirrored and contained by counter-scheme; visible judgment is delayed gently, not absent.
- Passage-order assembly: they scheme intensely -> I scheme intensely -> delay the disbelievers a little.
- Participants and roles: human schemers, divine counter-agent, disbelievers, delay interval.
- Operation / mechanism: covert planning, counter-planning, controlled postponement.
- Direction / force / medium: hidden intention through time.
- Temporal development: escalation by repetition, then deceleration by command.
- Outcome / closure: controlled delay.
- Exact branch constituents: `ك ي د B001,B002`, `م ه ل B001`, `ر و د B005`, `ك ف ر B001,B003`.
- Unfilled roles: final visible outcome is deferred by the passage itself.
- Status: FRAGMENT.

## Exhaustiveness Check

- Every S86 rooted occurrence row in `qac_root_ayah.tsv` appears in the lexical seed catalog.
- Every accepted branch ID for each S86 root in `v4_branches.tsv` is listed under an occurrence context, either as `G`, `C`, `L`, or `T`.
- Repeated occurrence contexts were restarted separately: `ط ر ق` at 86:1 and 86:2; `خ ل ق` at 86:5 and 86:6; `ر ج ع` at 86:8 and 86:11; `س م و` at 86:1 and 86:11; `ك ي د` at 86:15 and 86:16 plus cognate accusative restarts; `م ه ل` at both imperatives in 86:17.
- Every S86 attachment row was used as structural evidence, corroboration, or constraint.
- No Stage 2 synthesis or translation evidence was used.
