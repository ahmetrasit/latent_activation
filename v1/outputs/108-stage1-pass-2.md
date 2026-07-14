# S108 Stage 1 Pass 2

Assigned passage: S108.

Sacred Arabic text source: `resources/quran/surah_108.json`.

## Pass 2 correction

Root cause of the Pass 1 limitation: the first pass gathered the relevant S108 root dossiers but did not enforce singleton seeding for every accepted branch. It let the promising gift/abundance/cut-off relation dominate too early, so many branches were read as background rather than given their own seed pass. This pass restarts from the first rooted word and records every accepted branch seed, including failed and weak seeds.

Resource caveat: in this checkout, `resources/qac.sqlite` and `resources/furuq_v4.sqlite` are zero-byte files, so the SQLite examples in the prompt cannot return rows. I used the local TSV mirrors present under `resources/`: `resources/qac_root_ayah.tsv` for QAC rooted occurrence rows and `resources/v4_branches.tsv` for accepted branch rows. Attachment evidence comes from `resources/attachments.tsv`. No translation is used as evidence.

## Sacred text and rooted sequence

Opening context: `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`. Basmala is used only as opening-context corroboration or constraint, never as a seed.

Passage:

1. `إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ`
2. `فَصَلِّ لِرَبِّكَ وَٱنْحَرْ`
3. `إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ`

Rooted passage order:

1. `108:1:2 أَعْطَيْنَٰكَ / ع ط و / Form IV verb`
2. `108:1:3 ٱلْكَوْثَرَ / ك ث ر / noun`
3. `108:2:1 صَلِّ / ص ل و / Form II imperative`
4. `108:2:2 رَبِّكَ / ر ب ب / noun in لـ complement`
5. `108:2:3 ٱنْحَرْ / ن ح ر / imperative`
6. `108:3:2 شَانِئَكَ / ش ن ء / active participle`
7. `108:3:4 ٱلْأَبْتَرُ / ب ت ر / adjective/noun`

Attachment rows used:

- `108:1 a1`: suffix `نَا` is the ism of `إِنَّا`.
- `108:1 a2`: `أَعْطَيْنَٰكَ ٱلْكَوْثَرَ` is the predicate of `إِنَّا`.
- `108:1 a3`: suffix `كَ` in `أَعْطَيْنَٰكَ` is the second-person object.
- `108:1 a4`: `ٱلْكَوْثَرَ` is the explicit accusative object given.
- `108:2 a1`: `رَبِّكَ` is governed by `لِـ` as dedication complement of `صَلِّ`.
- `108:2 a2`: suffix `كَ` is possessive mudaf ilayh of `رَبِّ`.
- `108:2 a3`: `ٱنْحَرْ` is conjoined by `و` to the imperative `صَلِّ`.
- `108:3 a1`: `شَانِئَكَ` is the ism of `إِنَّ`.
- `108:3 a2`: suffix `كَ` in `شَانِئَكَ` is object governed by active participle `شَانِئ`.
- `108:3 a3`: `ٱلْأَبْتَرُ` is the predicate of `إِنَّ`, with `هُوَ` separating it from `شَانِئَكَ`.
- `108:3 a4`: suffix `كَ` is attached to `شَانِئ` as construct pronoun complement.

## Root dossier summary

`ع ط و`: `B001` taking by hand; `B002` giving/handing over; `B003` service and handing what is wanted to one's people; `B004` overreaching into what one has no right to; `B005` asking people for gifts; `B006` yielding, pliancy, obedience; `B007` prevailing in mutual taking.

`ك ث ر`: `B001` abundance and growth of number; `B002` rivalry and prevailing by number; `B003` much wealth, much speech, many demandants; `B005` dust called kawthar when much, rising, and stirred; `B006` palm pith/jummār; `B007` gathering/accumulation.

`ص ل و`: `B001` meeting fire/heat; `B002` prayer, blessing, mercy, praise, purification; `B003` prescribed worship; `B004` snares set for catching; `B005` the back/flanks near the tail and birth opening; `B006` following the previous in a race; `B007` places of worship; `B008` grinding stone; `B009` camel-grazed plant.

`ر ب ب`: `B001` lordship, ownership, mastery; `B002` repairing, nurturing, completing; `B003` rabbānī knowledge; `B004` many groups; `B005` stepchild/caretaker; `B006` thick robb used to prepare or preserve; `B007` staying, abiding, nearness; `B008` layered cloud; `B009` recently birthed ewe/newness; `B010` container for arrows; `B011` covenant; `B012` green plant; `B013` much water; `B014` herd; `B015` particle `rubba`; `B016` need, knot, blessing; `B017` master sailor.

`ن ح ر`: `B001` upper chest/throat place; `B002` slaughtering camel at the throat; `B003` facing or standing opposite; `B004` mutual contention over something; `B005` self-slaughter; `B006` time-boundary where one day/month faces another; `B008` expert knowledge; `B009` cloud bursting with much water.

`ش ن ء`: `B001` hatred/enmity; `B002` disgust and distancing from uncleanness; `B003` acknowledgment and bringing out what is due; `B004` hateful/ugly character or appearance.

`ب ت ر`: `B001` cutting before completion; `B002` loss of offspring, mention, and trace of good; `B004` cutting kinship; `B006` shortness of stature as though length were cut.

Opening-context branches considered only after freeze: `س م و B005` name/renown; `ء ل ه B001-B002` deity/name of God; `ر ح م B001` mercy; `ر ح م B002-B003` kinship/womb. These never initiate candidates.

## Candidate synthesis units

### C01 Gift Establishes Directed Return

- `candidate_id`: `S108-C01`
- `ayah_range`: `108:1-2`
- `seed_type`: lexical
- `seed`: `108:1 أَعْطَيْنَٰكَ / ع ط و B002`
- `generating_set`: `(E: ع ط و B002 giving/handing over)`, `(E: ك ث ر B001 abundant object)`, `(E: ص ل و B002 prayer/praise/mercy-response)`, `(E: ر ب ب B001 lord/owner in لربك)`, `(E: ن ح ر B002 sacrificial nahr as concrete second response)`
- `selected_branches`: `ع ط و B002`, `ك ث ر B001`, `ص ل و B002`, `ص ل و B003`, `ر ب ب B001`, `ن ح ر B002`
- `constructed_model`: A gift is placed from the emphatic divine giver to the addressed recipient; the next ayah turns the recipient's action back toward the giver-owner through dedicated worship and sacrifice. The latent structure is not simple possession but reception followed by directed return.
- `freeze_point`: After `فَصَلِّ لِرَبِّكَ وَٱنْحَرْ`.
- `predictions_at_freeze`: The object should be abundant enough to call for more than private enjoyment; the response should be dedicated to the giver, not to the hostile observer; a rival human claim may be displaced by divine ownership.
- `unused_features_tested`: `إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ`, repeated `كَ`, `هُوَ`, basmala opening, `ك ث ر B002/B003`, `ب ت ر B001/B002`.
- `corroborators`: `(C: attachment 108:1 a3/a4 double object: you plus given object)`, `(C: attachment 108:2 a1 dedication complement لربك)`, `(C: sequence 108:1→108:2 فـ response after gift)`, `(C: ر ب ب B002 completion/nurture as a distinct unused dimension)`, `(C: basmala opening-context ر ح م B001 mercy frames gift as benefaction rather than seizure)`
- `constraints`: `(K: صل does not contextually mean only generic thanks; attachment makes it a commanded act to ربك)`, `(K: نحر is a coordinated imperative, not a metaphorical adjective of prayer)`, `(K: الكوثر is object of أعطيناك, not a human demand extracted by the addressee)`
- `temporal_reactivation_notes`: `لربك` reactivates the divine `نا` of `إنا`, and the suffix `ك` moves from recipient of gift to servant of Lord. The listener first hears bestowed abundance, then a required directional return.
- `rival_models`: Pure "receive and enjoy" model fails because ayah 2 immediately commands directed worship and sacrifice. Pure sacrificial model fails because the first exposed state is giving abundance, not ritual slaughter.
- `grade`: strong
- `grade_rationale`: The model is generated by the contextual branches and independently supported by syntax, sequence, and pronoun movement.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv S108 rows for ع ط و, ك ث ر, ص ل و, ر ب ب, ن ح ر`; `v4_branches.tsv accepted rows listed above`; attachment rows `108:1 a2-a4`, `108:2 a1-a3`; `surah_108.json`.

### C02 Abundance Versus Cut-Off Closure

- `candidate_id`: `S108-C02`
- `ayah_range`: `108:1-3`
- `seed_type`: lexical
- `seed`: `108:1 ٱلْكَوْثَرَ / ك ث ر B001`
- `generating_set`: `(E: ك ث ر B001 abundance/growth)`, `(E: ع ط و B002 divine giving)`, `(E: ب ت ر B002 loss of offspring, mention, and trace of good)`, `(E: ش ن ء B001 enemy/hatred)`, `(E: ر ب ب B001 giver-owner as dedication target)`
- `selected_branches`: `ك ث ر B001`, `ك ث ر B002`, `ك ث ر B003`, `ع ط و B002`, `ش ن ء B001`, `ب ت ر B001`, `ب ت ر B002`
- `constructed_model`: The passage sets a maximal-gift field against a hostile verdict of truncation. The recipient receives `الكوثر`; the enemy who would define the recipient as cut off is himself assigned `الأبتر`.
- `freeze_point`: After constructing the abundant-gift versus enemy-cut model at `108:3`.
- `predictions_at_freeze`: There should be explicit predication assigning cut-off to the enemy; the enemy must be syntactically tied to the addressee; the abundant side should precede the hostile verdict so that closure reinterprets the initial gift.
- `unused_features_tested`: `هُوَ`, active participle `شَانِئ`, attachment of `كَ`, `ب ت ر B001`, basmala `س م و B005` name/renown.
- `corroborators`: `(C: attachment 108:3 a1/a3 إن makes شانئك subject and الأبتر predicate)`, `(C: هو separates and focuses predicate assignment)`, `(C: ش ن ء B004 hateful/ugly character after freeze narrows hostile evaluator)`, `(C: ب ت ر B001 literal cutting before completion supports the cut-off image under B002)`, `(C: opening-context س م و B005 name/renown can corroborate the mention/renown dimension only as opening context)`
- `constraints`: `(K: ك ث ر B005 dust is not selected; no local dust, rising cloud, or battle-powder cue)`, `(K: ب ت ر B004 cutting kinship is related but too narrow as the only local predicate)`, `(K: no external biographical claim is needed for this Stage 1 model)`
- `temporal_reactivation_notes`: At first `الكوثر` activates abundance without a stated opponent. The final `الأبتر` retroactively sharpens the abundance as the opposite of truncation and loss of trace.
- `rival_models`: A mere quantity model explains `كوثر` but not `شانئك` and `هو الأبتر`. A pure insult-reversal model explains closure but not the gift-to-response middle.
- `grade`: strong
- `grade_rationale`: Specific lexical opposition, exact predicate syntax, and passage closure converge.
- `source_queries_or_rows_used`: S108 QAC rows, `ك ث ر`, `ب ت ر`, `ش ن ء`, `ع ط و`, `ر ب ب` branch rows; attachment `108:3 a1-a4`.

### C03 Public Devotion Against Hostile Evaluation

- `candidate_id`: `S108-C03`
- `ayah_range`: `108:2-3`
- `seed_type`: lexical
- `seed`: `108:2 صَلِّ / ص ل و B002-B003`
- `generating_set`: `(E: ص ل و B002 prayer/praise/mercy)`, `(E: ص ل و B003 prescribed worship)`, `(E: ر ب ب B001 lord/master)`, `(E: ن ح ر B002 sacrificial act)`, `(E: ش ن ء B001 enemy/hatred)`
- `selected_branches`: `ص ل و B002`, `ص ل و B003`, `ر ب ب B001`, `ن ح ر B002`, `ش ن ء B001`, `ب ت ر B002`
- `constructed_model`: The second ayah creates an outward devotional response: worship and sacrifice are directed to the Lord, while the hostile observer is denied authority over the recipient's standing.
- `freeze_point`: After `وانحر`, before reading `إن شانئك هو الأبتر`.
- `predictions_at_freeze`: A rival audience or rival evaluator may appear; the recipient's action should remain directed upward/ownerward rather than toward the human enemy; the closure should separate enemy speech from real status.
- `unused_features_tested`: `شانئك`, `هو`, `الأبتر`, `إنا أعطيناك الكوثر`.
- `corroborators`: `(C: ش ن ء B001 supplies rival hostile evaluator after freeze)`, `(C: ب ت ر B002 supplies the hostile evaluator's true status)`, `(C: attachment 108:2 a1 لربك fixes direction of worship)`, `(C: attachment 108:2 a3 makes نحر coordinated with صل)`, `(C: 108:1 prior gift motivates response)`
- `constraints`: `(K: ص ل و B001 heat/fire does not fit the imperative with لربك)`, `(K: ص ل و B004 snare lacks passage-local prey/capture roles)`, `(K: نحر is an imperative action, not merely a body-part label in context)`
- `temporal_reactivation_notes`: `لربك` draws the response away from the later enemy, so when the enemy appears, the listener has already heard the proper direction of action.
- `rival_models`: A social-display model is constrained because the attachment targets `ربك`, not public viewers. A purely interior prayer model is constrained by the concrete conjoined `وانحر`.
- `grade`: medium-strong
- `grade_rationale`: Strong syntax and sequence; lexical synthesis is slightly broader because `ص ل و B002` and `B003` overlap in normal contextual meaning.
- `source_queries_or_rows_used`: S108 QAC rows; `ص ل و`, `ر ب ب`, `ن ح ر`, `ش ن ء`, `ب ت ر` branch rows; attachments `108:2 a1-a3`, `108:3 a1-a3`.

### C04 Nahr as Directed Offering and Boundary Marker

- `candidate_id`: `S108-C04`
- `ayah_range`: `108:2`
- `seed_type`: lexical
- `seed`: `108:2 ٱنْحَرْ / ن ح ر B002`
- `generating_set`: `(E: ن ح ر B002 slaughter at the upper chest)`, `(E: ص ل و B003 prescribed worship)`, `(E: ر ب ب B001 lord/master)`, `(E: ع ط و B002 previous gift)`
- `selected_branches`: `ن ح ر B001`, `ن ح ر B002`, `ن ح ر B003`, `ن ح ر B006`, `ص ل و B003`, `ر ب ب B001`, `ع ط و B002`
- `constructed_model`: The conjoined imperative moves from worship to a concrete offering act. The latent image is a front-facing dedication: the recipient turns toward the Lord and performs a costly, visible act at the throat/chest locus of sacrifice.
- `freeze_point`: After `وانحر`.
- `predictions_at_freeze`: The action should be a response to prior benefaction; it should not become mutual contention; it may establish a boundary between divine-directed offering and hostile social judgment.
- `unused_features_tested`: `الكوثر`, `شانئك`, `الأبتر`, `ن ح ر B003/B006`.
- `corroborators`: `(C: sequence 108:1 gift precedes command)`, `(C: attachment 108:2 a3 conjoins nahr to prayer)`, `(C: ن ح ر B003 facing/opposite as an unused dimension supports directed stance)`, `(C: ن ح ر B006 boundary-facing-time weakly supports ayah 2 as turning point between gift and verdict)`
- `constraints`: `(K: ن ح ر B004 contention is rejected; no mutual contest construction in ayah 2)`, `(K: ن ح ر B005 self-slaughter is defeated by imperative context and devotional coordination)`, `(K: ن ح ر B009 cloud-water is not locally cued except by remote abundance imagery and remains unselected)`
- `temporal_reactivation_notes`: `وانحر` thickens `فصل لربك` from verbal devotion to embodied offering. Later `شانئك` cannot become the addressee of the offering because `لربك` has already fixed direction.
- `rival_models`: "Face the enemy" from `ن ح ر B003` is weaker because the explicit complement belongs to `ربك`, not to `شانئك`.
- `grade`: medium
- `grade_rationale`: The sacrificial contextual sense is strong, but boundary/facing dimensions are secondary and must not replace primary nahr.
- `source_queries_or_rows_used`: `ن ح ر`, `ص ل و`, `ر ب ب`, `ع ط و`, `ش ن ء`, `ب ت ر` branch rows; attachments `108:2 a1-a3`.

### C05 Reciprocal Human Taking Is Inhibited by Divine Giving

- `candidate_id`: `S108-C05`
- `ayah_range`: `108:1-2`
- `seed_type`: lexical
- `seed`: `108:1 أَعْطَيْنَٰكَ / ع ط و B001`
- `generating_set`: `(E: ع ط و B001 hand-taking/reaching)`, `(E: ع ط و B002 giving/handing over)`, `(E: ك ث ر B001 abundant object)`, `(E: ر ب ب B001 owner/master)`, `(E: ص ل و B002 prayer/praise response)`
- `selected_branches`: `ع ط و B001`, `ع ط و B002`, `ع ط و B006`, `ك ث ر B001`, `ر ب ب B001`, `ص ل و B002`
- `constructed_model`: The first verb contains an older manual image of taking/handing, but Form IV and syntax resolve it as divine giving to the addressee. The response is not grasping more but pliant dedication to the Lord.
- `freeze_point`: After ayah 2 direction `لربك`.
- `predictions_at_freeze`: Demand, overreach, or human extraction branches should be constrained; obedience/yielding may corroborate.
- `unused_features_tested`: `ع ط و B004/B005/B006/B007`, `شانئك`, `الأبتر`.
- `corroborators`: `(C: ع ط و B006 yielding/pliancy as distinct unused dimension fits commanded response)`, `(C: attachment 108:1 a3/a4 controls giver-recipient-object roles)`, `(C: 108:2 imperatives show received gift becomes obedience)`
- `constraints`: `(K: ع ط و B004 overreaching is rejected for the addressee; no illicit taking construction)`, `(K: ع ط و B005 asking people is rejected; giver is divine plural subject, not human crowd)`, `(K: ع ط و B007 mutual prevailing is rejected; no reciprocal contest in ayah 1)`
- `temporal_reactivation_notes`: The listener hears `أعطيناك` before any command; ayah 2 prevents the hand-receiving image from becoming possessive autonomy.
- `rival_models`: A beneficiary-centered acquisition model is weaker than divine-gift-to-dedication because the next word group supplies `لربك`.
- `grade`: medium
- `grade_rationale`: Useful inhibition of rival `ع ط و` branches, but the main model is carried by ordinary giving syntax.
- `source_queries_or_rows_used`: `ع ط و` all branches, `ك ث ر B001`, `ر ب ب B001`, `ص ل و B002`; attachments `108:1 a2-a4`, `108:2 a1`.

### C06 Rival Multiplication and Boast Collapses Into Truncation

- `candidate_id`: `S108-C06`
- `ayah_range`: `108:1-3`
- `seed_type`: lexical
- `seed`: `108:1 ٱلْكَوْثَرَ / ك ث ر B002`
- `generating_set`: `(E: ك ث ر B002 rivalry/prevailing by number)`, `(E: ك ث ر B003 wealth/speech/demandants)`, `(E: ش ن ء B001 hostile evaluator)`, `(E: ب ت ر B002 loss of trace/good)`, `(E: ع ط و B002 divine gift)`
- `selected_branches`: `ك ث ر B002`, `ك ث ر B003`, `ش ن ء B001`, `ش ن ء B004`, `ب ت ر B002`, `ع ط و B002`
- `constructed_model`: A rival field of counting, boasting, many words, or many demandants is activated by `كوثر` branches, but the surah places abundance as given by God and closes by assigning real loss of trace to the hater.
- `freeze_point`: After `إن شانئك هو الأبتر`.
- `predictions_at_freeze`: If rivalry is relevant, the enemy should be linked to evaluation rather than possession of abundance; cut-off should answer boastful counting with loss of consequence.
- `unused_features_tested`: `صل لربك وانحر`, `هو`, attachments.
- `corroborators`: `(C: ش ن ء B004 ugly/hateful character narrows rival speaker)`, `(C: ب ت ر B002 loss of mention counters boasting/much speech)`, `(C: هو focus makes the hater, not the addressee, the one finally defined)`
- `constraints`: `(K: ك ث ر B002 is not the primary contextual sense of الكوثر; it is a secondary rivalry simulation)`, `(K: no explicit plural crowd or counting construction appears)`, `(K: devotional middle prevents the passage from becoming mere status competition)`
- `temporal_reactivation_notes`: The final `الأبتر` makes any earlier activated abundance-rivalry branch recoil against the hater.
- `rival_models`: Pure "many people versus no descendants" model is possible but needs external data; local evidence supports only abundance/rivalry/truncation as a secondary structure.
- `grade`: medium
- `grade_rationale`: Coherent with branch opposition and closure but less directly encoded than C02.
- `source_queries_or_rows_used`: `ك ث ر B002/B003`, `ش ن ء B001/B004`, `ب ت ر B002`, attachments `108:3 a1-a3`.

### C07 The Hater's Attempted Cut Returns to Himself

- `candidate_id`: `S108-C07`
- `ayah_range`: `108:3`
- `seed_type`: lexical
- `seed`: `108:3 ٱلْأَبْتَرُ / ب ت ر B001`
- `generating_set`: `(E: ب ت ر B001 cutting before completion)`, `(E: ب ت ر B002 cut off from offspring/mention/good)`, `(E: ش ن ء B001 enemy/hatred)`, `(E: ش ن ء B002 distancing/disgust)`
- `selected_branches`: `ب ت ر B001`, `ب ت ر B002`, `ب ت ر B004`, `ش ن ء B001`, `ش ن ء B002`, `ش ن ء B004`
- `constructed_model`: The closure identifies the hostile relation itself as the locus of truncation. Hatred tries to distance and diminish the addressee, but syntax assigns cut-off to the hater.
- `freeze_point`: At `هُوَ ٱلْأَبْتَرُ`.
- `predictions_at_freeze`: The hater must be explicitly attached to the addressee, and the predicate must not grammatically attach to the addressee.
- `unused_features_tested`: `كَ` in `شانئك`, `هو`, `إن`, `ب ت ر B004`, basmala `ر ح م B002`.
- `corroborators`: `(C: attachment 108:3 a2/a4 ties hater to the addressed person as object/construct complement)`, `(C: attachment 108:3 a3 assigns الأبتر as predicate)`, `(C: ش ن ء B002 distancing gives the hater a separating motion)`, `(C: ب ت ر B004 cutting kinship is a local-adjacent but secondary cut relation)`, `(C: opening-context ر ح م B002 kinship only weakly corroborates cut-kinship contrast and is not generating evidence)`
- `constraints`: `(K: ب ت ر B006 short stature is rejected; no body-size cue)`, `(K: ش ن ء B003 acknowledgment is not the contextual active participle sense here)`, `(K: الأبتر is not syntactically a predicate of ك in أعطيناك or ربك)`
- `temporal_reactivation_notes`: The last word reactivates the abundance of the first ayah by contrast: the one opposed to the recipient is the one without continuation.
- `rival_models`: A generic curse model misses the precise relational syntax: `شانئك` is the hater of you, and `هو` makes him the predicate target.
- `grade`: strong
- `grade_rationale`: Exact closure syntax and branch specificity are high.
- `source_queries_or_rows_used`: `ب ت ر`, `ش ن ء` branch rows; attachments `108:3 a1-a4`.

### C08 Completion/Nurture of the Gift Under Lordship

- `candidate_id`: `S108-C08`
- `ayah_range`: `108:1-2`
- `seed_type`: lexical
- `seed`: `108:2 رَبِّكَ / ر ب ب B002`
- `generating_set`: `(E: ر ب ب B002 nurturing/completing/repairing)`, `(E: ع ط و B002 gift)`, `(E: ك ث ر B001 abundance)`, `(E: ص ل و B002-B003 worship/prayer response)`
- `selected_branches`: `ر ب ب B001`, `ر ب ب B002`, `ر ب ب B007`, `ر ب ب B011`, `ع ط و B002`, `ك ث ر B001`, `ص ل و B002`
- `constructed_model`: The gift is not inert quantity; under `ربك`, it belongs to a Lord who owns, completes, and nurtures. The response is therefore oriented to the giver's lordship rather than to the abundance as an independent possession.
- `freeze_point`: After reading `لربك`.
- `predictions_at_freeze`: There may be a completion-versus-cutting contrast at closure; abiding/covenant branches may weakly support loyalty.
- `unused_features_tested`: `ب ت ر B001/B002`, `ر ب ب B007/B011`, `شانئك`.
- `corroborators`: `(C: ب ت ر B001 cutting before completion directly opposes ر ب ب B002 completion)`, `(C: ب ت ر B002 loss of trace/good opposes nurturing gift)`, `(C: ر ب ب B007 abiding/nearness supports continuing directed relation)`, `(C: ر ب ب B011 covenant weakly supports loyal dedication)`
- `constraints`: `(K: ر ب ب B003 knowledge, B005 stepchild, B006 robb, B010 arrow-container, B015 particle, B017 sailor have no passage-local roles)`, `(K: ربك is syntactically complement of صل, not an independent subject of ayah 2)`
- `temporal_reactivation_notes`: `ربك` reactivates the divine giver and anticipates the final opposition: completed/nurtured relation versus cut-off hater.
- `rival_models`: A mere title model works contextually but misses the completion/cut-off branch opposition. The branch opposition is secondary, not a translation.
- `grade`: medium-strong
- `grade_rationale`: Good independent opposition between `ر ب ب B002` and `ب ت ر B001/B002`; several other `ر ب ب` branches are terminated.
- `source_queries_or_rows_used`: `ر ب ب B001-B017`, `ب ت ر B001/B002`, attachments `108:2 a1-a2`.

### C09 Remote Dust/Cloud/Water Abundance Fork

- `candidate_id`: `S108-C09`
- `ayah_range`: `108:1-2`
- `seed_type`: lexical
- `seed`: `108:1 ٱلْكَوْثَرَ / ك ث ر B005`
- `generating_set`: `(E: ك ث ر B005 abundant stirred dust called kawthar)`, `(E: ر ب ب B008 layered cloud)`, `(E: ر ب ب B013 much water)`, `(E: ن ح ر B009 cloud bursting with much water)`
- `selected_branches`: `ك ث ر B005`, `ر ب ب B008`, `ر ب ب B013`, `ن ح ر B009`, `ك ث ر B001`
- `constructed_model`: A remote natural image can be assembled: abundance rises or gathers like dust/cloud, and cloud-water bursts forth. This gives the gift a secondary force of overflow, but the passage does not supply enough local weather roles.
- `freeze_point`: After assembling cloud/dust/water branches.
- `predictions_at_freeze`: Expect sky, cloud, rain, watercourse, or outflow lexemes; expect some relation between abundance and bursting.
- `unused_features_tested`: `أعطيناك`, `فصل لربك وانحر`, `شانئك هو الأبتر`.
- `corroborators`: `(C: ك ث ر B001 general abundance supports overflow at a broad level)`
- `constraints`: `(K: no explicit sky/cloud/water lexeme in S108)`, `(K: ن ح ر B009 is remote and not contextual imperative nahr)`, `(K: ر ب ب B008/B013 are not activated by surface ربك except remotely)`, `(K: devotional and hostile-predicate sequence is unexplained)`
- `temporal_reactivation_notes`: The branch creates a visual overflow but does not explain the ordered movement from gift to worship to enemy verdict.
- `rival_models`: Pastoral-water abundance remains a fragment.
- `grade`: weak
- `grade_rationale`: Branches can make an image, but local syntax and lexical sequence do not corroborate it.
- `source_queries_or_rows_used`: `ك ث ر B005`, `ر ب ب B008/B013`, `ن ح ر B009`.

### C10 Body, Birth, and Continuity Fork

- `candidate_id`: `S108-C10`
- `ayah_range`: `108:2-3`
- `seed_type`: lexical
- `seed`: `108:2 صَلِّ / ص ل و B005`
- `generating_set`: `(E: ص ل و B005 back/flanks and birth opening)`, `(E: ر ح م B003 opening-context womb only after freeze if needed)`, `(E: ب ت ر B002 loss of offspring/continuation)`, `(E: ب ت ر B004 cutting kinship)`
- `selected_branches`: `ص ل و B005`, `ب ت ر B002`, `ب ت ر B004`, opening-context `ر ح م B003`, `ر ح م B002`
- `constructed_model`: A remote body-continuity image can be formed: birth/offspring/kinship are activated by `ص ل و B005` and `ب ت ر B002/B004`. It could make the final `الأبتر` feel like loss of bodily continuation, but it is not strongly generated by contextual `صل`.
- `freeze_point`: After `ب ت ر B002/B004` connection.
- `predictions_at_freeze`: Expect womb, offspring, kinship, lineage, body-part, or birth context.
- `unused_features_tested`: Basmala `رحم`, `نحر B001`, `أعطيناك الكوثر`.
- `corroborators`: `(C: opening-context ر ح م B003 womb is only opening-context and weak)`, `(C: opening-context ر ح م B002 kinship weakly supports بتر B004)`, `(C: ن ح ر B001 upper chest supplies a body locus but not birth)`
- `constraints`: `(K: صل is Form II imperative in devotional frame, not body-part noun)`, `(K: no explicit child, womb, or lineage lexeme in S108)`, `(K: basmala cannot generate the model)`
- `temporal_reactivation_notes`: Only the final `الأبتر` makes this body-continuity fork intelligible; before closure it has little passage-local traction.
- `rival_models`: The lexical-final cut-off model C07 is stronger and should absorb only the continuation feature, not the full body-birth image.
- `grade`: weak
- `grade_rationale`: It records a possible image but remains remote and constrained.
- `source_queries_or_rows_used`: `ص ل و B005`, `ب ت ر B002/B004`, opening-context `ر ح م B002/B003`.

### C11 Trap, Contention, and Enemy Defeat Fork

- `candidate_id`: `S108-C11`
- `ayah_range`: `108:2-3`
- `seed_type`: lexical
- `seed`: `108:2 صَلِّ / ص ل و B004`
- `generating_set`: `(E: ص ل و B004 snare/trap)`, `(E: ن ح ر B004 mutual contention)`, `(E: ش ن ء B001 enmity)`, `(E: ب ت ر B001 cutting)`
- `selected_branches`: `ص ل و B004`, `ن ح ر B004`, `ش ن ء B001`, `ب ت ر B001`
- `constructed_model`: A conflict image can be forced: an enemy sets or enters a trap/contest and ends cut off. The passage does contain enmity and cutting, but it lacks prey, snare, mutual combat, or trap syntax.
- `freeze_point`: After assembling conflict branches.
- `predictions_at_freeze`: Expect capture, prey, hunting, mutual attack, or explicit contest.
- `unused_features_tested`: `لربك`, `وانحر`, `هو الأبتر`.
- `corroborators`: `(C: ش ن ء B001 gives enmity)`, `(C: ب ت ر B001 gives cutting)`
- `constraints`: `(K: ص ل و B004 is defeated by devotional imperative and لربك)`, `(K: ن ح ر B004 contention is defeated by coordinated worship/sacrifice, not mutual combat)`, `(K: no hunting or trap object appears)`, `(K: enemy is predicate subject, not captured prey)`
- `temporal_reactivation_notes`: The closure can support enemy reversal, but the trap mechanics are not reactivated by any local construction.
- `rival_models`: C07 supplies enemy defeat without importing trap roles.
- `grade`: unlikely
- `grade_rationale`: Too many required roles are absent.
- `source_queries_or_rows_used`: `ص ل و B004`, `ن ح ر B004`, `ش ن ء B001`, `ب ت ر B001`; attachments `108:2 a1-a3`.

## Exhaustive lexical seed audit

Every accepted branch of every passage root is listed. "Converges" means it independently recreates or strengthens a candidate above. "Local" means it creates a partial image but not a passage-scale synthesis. "Terminated" means no passage-local complement survived constraints.

| Seed | Pass result | Status |
| --- | --- | --- |
| `108:1 ع ط و B001` taking by hand | Becomes C05 as a manual receiving image, then is constrained by Form IV gift syntax and `لربك`. | local / medium |
| `108:1 ع ط و B002` giving/handing over | Generates C01 and supports C02/C05/C08. | converges / strong |
| `108:1 ع ط و B003` serving one's people | Weakly parallels ayah 2 response as service, but `ربك` not "people"; no separate candidate beyond C05. | local / weak |
| `108:1 ع ط و B004` illicit overreach | Tested as rival acquisition; defeated by divine giver subject and object syntax. | terminated |
| `108:1 ع ط و B005` asking people for gifts | Defeated: the addressee is recipient, not petitioner; no human donor crowd. | terminated |
| `108:1 ع ط و B006` yielding/pliancy | Corroborates C05 as response-obedience after gift; does not generate full model alone. | local / weak-medium |
| `108:1 ع ط و B007` prevailing in mutual taking | Could pair with rivalry, but no reciprocal struggle in ayah 1; C06 absorbs only broad rivalry possibility. | terminated / weak |
| `108:1 ك ث ر B001` abundance/growth | Generates C02 and supports C01. | converges / strong |
| `108:1 ك ث ر B002` rivalry by number | Generates C06 as secondary rivalry fork. | local / medium |
| `108:1 ك ث ر B003` much wealth/speech/demandants | Supports C06; no independent local demandant structure. | local / weak-medium |
| `108:1 ك ث ر B005` stirred abundant dust | Generates C09 remote dust/cloud overflow fork; weakly supported by abundance only. | local / weak |
| `108:1 ك ث ر B006` palm pith | No palm, pith, fruit, or cutting exemption cue in S108. | terminated |
| `108:1 ك ث ر B007` gathering/accumulation | Reduces to broad abundance; no separate mechanism beyond C02. | local / weak |
| `108:2 ص ل و B001` heat/fire | Tested with nahr and enemy; defeated by `لربك` prayer frame and no fire lexeme. | terminated |
| `108:2 ص ل و B002` prayer/blessing/mercy/praise | Generates C03 and supports C01. | converges / medium-strong |
| `108:2 ص ل و B003` prescribed worship | Generates C03/C04 as contextual prayer. | converges / medium-strong |
| `108:2 ص ل و B004` snare | Generates C11 trap fork, then defeated by missing trap roles. | terminated / unlikely |
| `108:2 ص ل و B005` back/flanks/birth | Generates C10 body-continuity fork, then constrained. | local / weak |
| `108:2 ص ل و B006` second horse/follower | Could model response following gift, but no race or prior runner; only sequence echo. | terminated / weak |
| `108:2 ص ل و B007` worship places | No place/house/church/masjid lexeme; devotional act present but not place. | terminated |
| `108:2 ص ل و B008` grinding stone | No grinding, pounding, scent, or grain role. | terminated |
| `108:2 ص ل و B009` camel-grazed plant | No pasture, camel, or plant cue; possible only through remote pastoral branches rejected in C09. | terminated |
| `108:2 ر ب ب B001` lordship/ownership/mastery | Supports C01/C03/C04 and anchors dedication. | converges / strong |
| `108:2 ر ب ب B002` nurturing/completing | Generates C08 and corroborates completion versus cut-off. | converges / medium-strong |
| `108:2 ر ب ب B003` rabbani knowledge | No teaching/knowledge role except remote `نحرير`; no synthesis. | terminated |
| `108:2 ر ب ب B004` many groups | Can echo abundance/rivalry, but no local group noun. | terminated / weak |
| `108:2 ر ب ب B005` stepchild/caretaker | No stepchild or foster relation; terminated. | terminated |
| `108:2 ر ب ب B006` thick robb/preservation | No food, leather, medicine, or condiment roles; terminated. | terminated |
| `108:2 ر ب ب B007` abiding/nearness | Corroborates C08 as continuing relation but not an independent model. | local / weak-medium |
| `108:2 ر ب ب B008` cloud | Supports C09 remote natural fork only. | local / weak |
| `108:2 ر ب ب B009` newly birthed ewe | Could touch C10 continuity, but no animal-birth cue except remote nahr/sacrifice; terminated. | terminated / weak |
| `108:2 ر ب ب B010` arrow-container | No arrows, lottery, or container cue. | terminated |
| `108:2 ر ب ب B011` covenant | Weakly supports dedication/loyalty in C08; no explicit oath/covenant. | local / weak |
| `108:2 ر ب ب B012` green plant | No plant cue; terminated. | terminated |
| `108:2 ر ب ب B013` much water | Supports C09 remote overflow fork only. | local / weak |
| `108:2 ر ب ب B014` herd | No herd cue except sacrificial animal by inference; too remote. | terminated |
| `108:2 ر ب ب B015` particle `rubba` | Not the form in `ربك`; no syntactic role. | terminated |
| `108:2 ر ب ب B016` need/knot/blessing | Blessing dimension weakly touches gift but no distinct role; knot/need absent. | terminated / weak |
| `108:2 ر ب ب B017` master sailor | No sea/ship role. | terminated |
| `108:2 ن ح ر B001` upper chest/throat | Supports C04 body locus of sacrifice; weakly supports C10. | local / medium |
| `108:2 ن ح ر B002` slaughter at throat | Generates C04 and supports C01/C03. | converges / medium-strong |
| `108:2 ن ح ر B003` facing/opposite | Supports C04 as directional stance; rival "face enemy" constrained by `لربك`. | local / medium |
| `108:2 ن ح ر B004` contention | Generates C11 conflict fork, then defeated. | terminated / unlikely |
| `108:2 ن ح ر B005` self-slaughter | Defeated by devotional imperative and no reflexive object. | terminated |
| `108:2 ن ح ر B006` time boundary | Weakly supports ayah 2 as transition between gift and verdict; no independent model. | local / weak |
| `108:2 ن ح ر B008` expert knowledge | No knowledge/mastery predicate; remote with `ر ب ب B003` but no synthesis. | terminated |
| `108:2 ن ح ر B009` cloud bursting water | Supports C09 remote natural fork only. | local / weak |
| `108:3 ش ن ء B001` hatred/enmity | Generates C07 and supports C02/C03/C06. | converges / strong |
| `108:3 ش ن ء B002` disgust/distancing | Supports C07 as separating motion; not primary contextual meaning. | local / medium |
| `108:3 ش ن ء B003` acknowledgment/bringing out due | Possible ironic "enemy acknowledges right" fork, but active participle `شانئ` and predicate `الأبتر` favor hatred; no model survives. | terminated / weak |
| `108:3 ش ن ء B004` hateful/ugly character | Supports C06/C07 by qualifying hostile evaluator. | local / medium |
| `108:3 ب ت ر B001` cutting before completion | Generates C07 and corroborates C08 completion contrast. | converges / strong |
| `108:3 ب ت ر B002` loss of offspring/mention/good | Generates C02/C07. | converges / strong |
| `108:3 ب ت ر B004` cutting kinship | Supports C07/C10 as secondary cut relation; not primary alone. | local / weak-medium |
| `108:3 ب ت ر B006` short stature | No body-size cue; terminated. | terminated |

## Constructional, morphosyntactic, and temporal seed audit

| Seed | Constructed image | Corroboration / constraint | Grade |
| --- | --- | --- | --- |
| `إِنَّا + verbal predicate` | Emphatic divine-origin proposition opens the passage. | `(C: attachment 108:1 a1-a2)`, `(C: basmala opening-context ء ل ه B002 divine name)`, `(K: not a generic narrator; suffix نا is grammatical subject/ism frame)`. | strong |
| Double object in `أعطيناك الكوثر` | Recipient and gift are both explicit, creating transfer geometry. | `(C: attachment 108:1 a3-a4)`, supports C01/C02/C05. | strong |
| `فـ` before `صل` | Gift immediately conditions response. | `(C: sequence 108:1→108:2)`, `(K: response is not delayed narrative or unrelated command)`. | strong |
| `لربك` dedication complement | Worship is directed to the recipient's Lord. | `(C: attachment 108:2 a1-a2)`, constrains enemy-directed or audience-directed models. | strong |
| Coordinated imperatives `صل ... وانحر` | Two-part response: devotional act plus concrete offering. | `(C: attachment 108:2 a3)`, supports C03/C04. | medium-strong |
| Repeated `كَ` pronoun | Same addressee receives gift, dedicates to Lord, and is hated by enemy. | `(C: 108:1 recipient; 108:2 possessive relation; 108:3 object of hatred)`. | strong |
| `إن شانئك` | Closure introduces a hostile relation, not a neutral observer. | `(C: attachment 108:3 a1-a2/a4)`, supports C07. | strong |
| `هو الأبتر` | Predicate focus assigns cut-off status to the hater. | `(C: attachment 108:3 a3)`, supports C02/C07. | strong |
| Three-ayah temporal arc | Gift -> directed response -> enemy verdict. | Reactivates `كوثر` by final `أبتر`; reactivates divine giver by `ربك`. | strong |
| Sound/shape recurrence: emphatic openings `إنا` / `إن` | First and last ayah make parallel assertions: divine gift and enemy cut-off. | Corroborates enclosure of middle command; does not create lexical meaning. | medium |
| Basmala opening context | Name/divinity/mercy may constrain gift as divine mercy. | `(C: ر ح م B001 opening-context)`, `(C: ء ل ه B001-B002 opening-context)`, never seed-generating. | weak-medium |

## Branches rejected after exhaustive traversal

The following branches were visited and rejected as independent synthesis generators because they lacked passage-local role completion: `ع ط و B004-B005-B007`; `ك ث ر B006`; `ص ل و B001/B004/B006/B007/B008/B009`; `ر ب ب B003/B004/B005/B006/B009/B010/B012/B014/B015/B016/B017`; `ن ح ر B004/B005/B008`; `ش ن ء B003`; `ب ت ر B006`. Some of these appear as weak local corroborators or rival forks above, but none should be used as primary contextual meaning.

## Multi-seed convergence

The strongest recurrent structure is:

`divine giving (ع ط و B002)` -> `abundant gift (ك ثر B001)` -> `dedicated response to Lord (ص ل و B002/B003 + ر ب ب B001 + ن ح ر B002)` -> `hostile evaluator reassigned cut-off status (ش ن ء B001 + ب ت ر B002)`.

Independent starts that recreate this structure: `ع ط و B002`, `ك ثر B001`, `ص ل و B002/B003`, `ر ب ب B001/B002`, `ن ح ر B002`, `ش ن ء B001`, `ب ت ر B001/B002`.

Secondary but controlled simulations:

- abundance versus truncation: strong;
- gift-to-directed-return: strong;
- completion/nurture versus premature cutting: medium-strong;
- public devotion against hostile evaluation: medium-strong;
- rivalry/boasting versus true cut-off: medium;
- body/birth/kinship continuity: weak;
- dust/cloud/water overflow: weak;
- trap/contention defeat: unlikely.

## Image Packet Catalog

IMAGE_ID: `IP-S108-01`

Starting seed: `ع ط و B002`

Complete image: A divine giver hands abundant good to the addressee; the addressee turns the received gift back toward the giver's lordship through prayer and sacrifice.

Passage-order assembly: `إنا` -> `أعطيناك` -> `الكوثر` -> `فصل` -> `لربك` -> `وانحر`.

Participants and roles: divine giver; addressed recipient; abundant gift; Lord/owner; devotional response; sacrificial response.

Operation / mechanism: transfer followed by dedicated return.

Direction / force / medium: from divine giver to addressee, then from addressee toward Lord.

Temporal development: gift first, response second.

Outcome / closure: enemy verdict cannot own the frame; closure moves to hater's cut-off status.

Exact branch constituents: `ع ط و B002`, `ك ثر B001`, `ص ل و B002/B003`, `ر ب ب B001`, `ن ح ر B002`.

Unfilled roles, if any: none within ayat 1-2; enemy closure supplied by IP-S108-02.

Status: COMPLETE.

IMAGE_ID: `IP-S108-02`

Starting seed: `ك ثر B001` or `ب ت ر B002`.

Complete image: Abundance and continuation stand opposite truncation. The recipient is placed on the abundant side by gift; the hater is assigned the cut-off side by predicate.

Passage-order assembly: `الكوثر` first activates abundance; `الأبتر` closes with opposite status.

Participants and roles: addressee as recipient of abundance; hater as hostile evaluator; cut-off predicate.

Operation / mechanism: final predication reverses hostile diminution.

Direction / force / medium: evaluative force rebounds from addressee to hater through `هو الأبتر`.

Temporal development: abundance is heard before enemy; enemy closure reactivates abundance as non-truncation.

Outcome / closure: `الأبتر` is the hater, not the addressee.

Exact branch constituents: `ك ثر B001`, `ش ن ء B001`, `ب ت ر B001/B002`.

Unfilled roles, if any: no external lineage details supplied locally.

Status: COMPLETE.

IMAGE_ID: `IP-S108-03`

Starting seed: `ر ب ب B002`.

Complete image: The Lord relation completes and nurtures what the cut-off relation tries to deny.

Passage-order assembly: `أعطيناك الكوثر` -> `لربك` -> `الأبتر`.

Participants and roles: Lord as owner/completer; addressee as servant/recipient; hater as cut-off contrast.

Operation / mechanism: completion under lordship opposed to premature cutting.

Direction / force / medium: completion flows from Lord relation; cutting is assigned to enemy.

Temporal development: gift and Lordship precede cut-off verdict.

Outcome / closure: completion/care is not defeated by hostile truncation.

Exact branch constituents: `ر ب ب B002`, `ع ط و B002`, `ك ثر B001`, `ب ت ر B001/B002`.

Unfilled roles, if any: covenant/abiding branches remain secondary.

Status: COMPLETE.

IMAGE_ID: `IP-S108-04`

Starting seed: `ك ثر B005`, `ر ب ب B008/B013`, `ن ح ر B009`.

Complete image: A remote overflow scene of stirred abundance, layered cloud, and bursting water.

Passage-order assembly: branch-level only; not strongly tied to the ayah sequence.

Participants and roles: gathered abundance; cloud/water; burst.

Operation / mechanism: accumulation and release.

Direction / force / medium: upward/stirred or cloud-burst motion.

Temporal development: insufficiently anchored.

Outcome / closure: does not explain hater/cut-off closure.

Exact branch constituents: `ك ثر B005`, `ر ب ب B008/B013`, `ن ح ر B009`.

Unfilled roles, if any: no explicit cloud, water, sky, or flow lexeme.

Status: FRAGMENT.

IMAGE_ID: `IP-S108-05`

Starting seed: `ص ل و B005`, `ب ت ر B004`.

Complete image: Body/birth/kinship continuity is threatened by cutting.

Passage-order assembly: mostly closure-driven from `الأبتر`; `صل` contextual form does not sustain the body branch.

Participants and roles: body locus, womb/kinship opening-context, hater/cutter.

Operation / mechanism: continuity versus severance.

Direction / force / medium: bodily/lineal continuity.

Temporal development: weak until the final cut-off word.

Outcome / closure: only the loss-of-continuation feature survives into C07/C10.

Exact branch constituents: `ص ل و B005`, `ب ت ر B002/B004`, opening-context `ر ح م B002/B003`.

Unfilled roles, if any: no explicit offspring, womb, or lineage lexeme in S108.

Status: FRAGMENT.

## Final short interpretation

The most defensible Stage 1 synthesis is a compact three-step activation trajectory: a divine giver grants abundance to the addressee; the addressee is directed to answer the gift through worship and sacrifice to his Lord; the hostile evaluator who would frame the addressee as diminished is himself declared cut off. The strongest secondary geometry is abundance/completion versus premature severance. Remote body, cloud, trap, and pastoral branches are preserved only as weak or unlikely simulations and should not be promoted to primary meaning.

## Exhaustiveness check

Lexical branch seeds counted: `55`.

Lexical branch seeds audited: `55`.

Passage rooted occurrences audited: `7`.

Constructional/morphosyntactic/temporal seeds audited: `11`.

Opening-context roots used only after freeze: `س م و`, `ء ل ه`, `ر ح م`.

No additional image packets are missing from the branch traversal: all successful and fragmentary image families are represented as IP-S108-01 through IP-S108-05.
