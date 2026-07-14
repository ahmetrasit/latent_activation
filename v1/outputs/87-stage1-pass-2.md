# Stage 1 Pass 2: S87 Temporally Conditioned Reactivation

Assigned passage: S87, whole surah.

Sacred Arabic text source used: `resources/quran/surah_87.json`.

Prompt followed: `v1/prompts/stage1.md`.

## Root Cause For Pass 1 Limitation

Pass 1 visited only a limited number of words per finding for two concrete reasons.

1. The prompt-authorized SQLite files are present but zero-byte placeholders in this workspace state: `resources/qac.sqlite` and `resources/furuq_v4.sqlite` contain no tables.
2. I then used the local TSV mirrors, `resources/qac_root_ayah.tsv`, `resources/v4_branches.tsv`, and `resources/attachments.tsv`, but the first full furuq branch extraction exceeded terminal output limits and was truncated. That made Pass 1 branch-incomplete.

This Pass 2 restarts from the first rooted word and treats every S87 rooted occurrence, every accepted branch row for S87 roots, and every eligible construction as initiated. The TSV files are used only as local stand-ins for the empty SQLite databases. Branches not recruited into a passage-local image are recorded as terminated or local-only rather than silently dropped.

## Data Envelope

Opening context: `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ` appears as `verse_0` in the sacred JSON. It was not used to initiate seeds. Its only added branch dossier checked was `ر ح م`, and it is used below only as opening-context corroboration or constraint.

Recoverable S87 rooted sequence from `qac_root_ayah.tsv`:

| ayah | text | root sequence |
| --- | --- | --- |
| 87:1 | `سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى` | `س ب ح;س م و;ر ب ب;ع ل و` |
| 87:2 | `ٱلَّذِى خَلَقَ فَسَوَّىٰ` | `خ ل ق;س و ي` |
| 87:3 | `وَٱلَّذِى قَدَّرَ فَهَدَىٰ` | `ق د ر;ه د ي` |
| 87:4 | `وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ` | `خ ر ج;ر ع ي` |
| 87:5 | `فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ` | `ج ع ل;غ ث و;ح و ي` |
| 87:6 | `سَنُقْرِئُكَ فَلَا تَنسَىٰٓ` | `ق ر ء;ن س ي` |
| 87:7 | `إِلَّا مَا شَآءَ ٱللَّهُ ۚ إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ` | `ش ي ء;ء ل ه;ع ل م;ج ه ر;خ ف ي` |
| 87:8 | `وَنُيَسِّرُكَ لِلْيُسْرَىٰ` | `ي س ر;ي س ر` |
| 87:9 | `فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ` | `ذ ك ر;ن ف ع;ذ ك ر` |
| 87:10 | `سَيَذَّكَّرُ مَن يَخْشَىٰ` | `ذ ك ر;خ ش ي` |
| 87:11 | `وَيَتَجَنَّبُهَا ٱلْأَشْقَى` | `ج ن ب;ش ق و` |
| 87:12 | `ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ` | `ص ل ي;ن و ر;ك ب ر` |
| 87:13 | `ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ` | `م و ت;ح ي ي` |
| 87:14 | `قَدْ أَفْلَحَ مَن تَزَكَّىٰ` | `ف ل ح;ز ك و` |
| 87:15 | `وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ` | `ذ ك ر;س م و;ر ب ب;ص ل و` |
| 87:16 | `بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا` | `ء ث ر;ح ي ي;د ن و` |
| 87:17 | `وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ` | `ء خ ر;خ ي ر;ب ق ي` |
| 87:18 | `إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ` | `ص ح ف;ء و ل` |
| 87:19 | `صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ` | `ص ح ف` |

Counts: 47 root-ayah rows, 49 rooted occurrences, 41 distinct S87 roots, 340 accepted branch rows in `v4_branches.tsv` for those roots. Duplicate export rows for `ش ي ء` and `ق ر ء` are preserved as rows but not treated as independent semantic proof.

## Exhaustive Branch Inventory

Every branch listed here was initiated as a lexical seed. Branches named inside candidate units entered construction, corroboration, constraint, or a rival fork. All remaining branch IDs in the same row were tested and terminated for lack of passage-local role completion.

| root | accepted branch IDs |
| --- | --- |
| `ء ث ر` | `B001,B002,B003,B004,B005,B006,B007,B008,B009,B011,B012` |
| `ء خ ر` | `B001,B002,B003` |
| `ء ل ه` | `B001,B002` |
| `ء و ل` | `B001,B002,B003,B004,B005,B007,B008,B009,B010` |
| `ب ق ي` | `B001,B002,B003,B004,B005` |
| `ج ع ل` | `B001,B002,B004,B005,B006,B007,B008,B009,B010,B011,B012` |
| `ج ن ب` | `B001,B002,B003,B005,B006,B007,B008,B009,B010,B011,B012` |
| `ج ه ر` | `B001,B002,B003,B004,B005,B006,B007,B008,B009,B011` |
| `ح و ي` | `B001,B002,B003,B004,B005,B006,B007,B008` |
| `ح ي ي` | `B002,B003,B004,B006,B007,B009,B010,B011,B012,B013` |
| `خ ر ج` | `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013` |
| `خ ش ي` | `B001,B002,B004` |
| `خ ف ي` | `B001,B002,B003,B004` |
| `خ ل ق` | `B001,B002,B003,B004,B005,B007,B008,B009,B010,B011,B012` |
| `خ ي ر` | `B001,B002,B003,B005,B006` |
| `د ن و` | `B001,B002,B003,B004,B005` |
| `ذ ك ر` | `B001,B002,B003,B004,B007,B008,B009` |
| `ر ب ب` | `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014,B015,B016,B017` |
| `ر ع ي` | `B001,B002,B003,B004,B005,B006` |
| `ز ك و` | `B001,B002,B004,B005` |
| `س ب ح` | `B001,B002,B004,B005,B006,B007,B008` |
| `س م و` | `B001,B002,B003,B004,B005,B006,B007,B008` |
| `س و ي` | `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B012,B013` |
| `ش ق و` | `B002,B003,B004` |
| `ش ي ء` | `B001,B002,B003,B004,B005,B006,B007,B008,B009` plus duplicate export row set `B001-B007` |
| `ص ح ف` | `B001,B002,B003,B004,B005` |
| `ص ل و` | `B001,B002,B003,B004,B005,B006,B007,B008,B009` |
| `ص ل ي` | `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010` |
| `ع ل م` | `B001,B002,B004,B005,B006,B007` |
| `ع ل و` | `B001,B002,B003,B004,B005,B006,B008,B009,B010,B011,B012` |
| `غ ث و` | `B001,B002,B003,B004` |
| `ف ل ح` | `B001,B002,B003,B004,B005,B006,B007` |
| `ق د ر` | `B001,B003,B004,B005,B006,B007` |
| `ق ر ء` | `B001,B002,B003,B004,B005,B006,B008,B009,B010,B011,B013` plus duplicate export row set `B001,B002,B003,B005,B006` |
| `ك ب ر` | `B001,B002,B003,B004,B005,B006,B007,B010,B011,B012,B013` |
| `م و ت` | `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014` |
| `ن س ي` | `B001,B002,B003,B004,B005,B006,B007` |
| `ن ف ع` | `B001,B002,B003` |
| `ن و ر` | `B001,B002,B004,B005,B006,B007,B008,B009` |
| `ه د ي` | `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011` |
| `ي س ر` | `B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011` |

## Constructional And Temporal Seed Set

These non-lexical seeds were also initiated:

- `87:1`: imperative `سَبِّحْ` governing `ٱسْمَ`, with `رَبِّكَ` iḍāfa and `ٱلْأَعْلَى` adjective.
- `87:2-5`: repeated relative clause sequence `ٱلَّذِى ... وَٱلَّذِى ... وَٱلَّذِى`.
- `87:2`: `خَلَقَ فَسَوَّىٰ`, creation followed by leveling/proportioning.
- `87:3`: `قَدَّرَ فَهَدَىٰ`, measuring/decreeing followed by guiding.
- `87:4-5`: `أَخْرَجَ ٱلْمَرْعَىٰ فَجَعَلَهُ غُثَاءً أَحْوَىٰ`, emergence-to-withered-result.
- `87:6-7`: `سَنُقْرِئُكَ فَلَا تَنسَىٰ إِلَّا مَا شَاءَ ٱللَّهُ`, future causative recitation, negated forgetting, exception under divine will.
- `87:7`: `يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ`, public/hidden object pair.
- `87:8`: doubled `ي س ر` construction `نُيَسِّرُكَ لِلْيُسْرَىٰ`.
- `87:9-11`: reminder command plus conditional benefit plus receptive/avoidant split.
- `87:12-13`: relative description of the most wretched, fire, then `لَا يَمُوتُ ... وَلَا يَحْيَىٰ`.
- `87:14-15`: `قَدْ أَفْلَحَ مَن تَزَكَّىٰ` followed by remembering the Lord's name and prayer.
- `87:16-17`: `بَلْ` contrast between preferred near life and better/enduring afterlife.
- `87:18-19`: demonstrative closure in former scrolls, then named scroll possessors.

## Candidate Synthesis Units

### CSU-87-01: Highest Name As Vertical Ordering And Purified Address

- `candidate_id`: `CSU-87-01`
- `ayah_range`: `87:1`, reactivated by `87:15` and constrained by `87:18-19`
- `seed_type`: lexical / constructional
- `seed`: first rooted word `87:1:1 سَبِّحِ` x `س ب ح B002`, the branch image of تنزيه and تبرئة.
- `generating_set`: `(E: س ب ح B002 تنزيه وتبرئة)`, `(E: س ب ح B001 عبادة بالتسبيح والصلاة)`, `(E: س م و B005 الاسم تنويه ودلالة)`, `(E: ر ب ب B001 ربوبية وملك وسيادة)`, `(E: ر ب ب B002 إصلاح وتربية وإتمام)`, `(E: ع ل و B001 السمو والارتفاع)`, `(E: ع ل و B002 الرفعة والشرف)`, `(E: ع ل و B005 الجهة العليا)`, `(E: attachment 87:1 a1 اسم as direct object of سبح)`, `(E: attachment 87:1 a2-a4 اسم ربك الأعلى as iḍāfa plus adjective)`.
- `selected_branches`: `س ب ح B001/B002`; `س م و B005` with `B001/B008` as secondary height/repute fork; `ر ب ب B001/B002`; `ع ل و B001/B002/B005`.
- `constructed_model`: The first event is not generic praise but an ordering of speech around a Name. `سَبِّحْ` removes defect or unsuitable attribution; `ٱسْمَ` supplies the audible/designating focus; `رَبِّكَ` supplies sovereign nurture and ownership; `ٱلْأَعْلَى` pushes the whole name-frame upward. The image is vertical purification of address: speech is aligned so that the named Lord is held above all lower associations.
- `freeze_point`: after `87:1`.
- `predictions_at_freeze`: later return of name/remembrance; worship or prayer should re-enter as enacted address; created order should support the Lord's high governing role; closure may place this statement in authoritative written transmission.
- `unused_features_tested`: `87:2-5` relative clauses; `87:6-9` recitation/reminder; `87:15 ذكر اسم ربه فصلى`; `87:18-19 الصحف الأولى`.
- `corroborators`: `(C: 87:15 repeats اسم ربه and adds صلى, independently satisfying the name-plus-worship prediction through ذ ك ر B004 and ص ل و B003)`, `(C: ر ح م B001 opening-context adds divine mercy/name atmosphere without generating the seed)`, `(C: 87:18-19 صحف B002/B003 place the demonstrative content in written authority)`.
- `constraints`: `(K: attachment 87:1 a1 makes اسم the object of سبح; the model cannot shift the direct object to created things)`, `(K: س ب ح B004 swimming/running, B005 wide going, B006 beads, B007 skins, B008 place terminate as no local complement)`, `(K: ع ل و B003 tyrannical arrogance and B004 conquest are rejected because الأعلى qualifies ربك in a divine-name phrase, not a hostile actor)`.
- `temporal_reactivation_notes`: The command is heard before the acts of creation and guidance. When `وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ` appears, the initial imperative is reactivated as the successful human response.
- `rival_models`: A sound-motion model from `س ب ح B004` and `س م و B001` gives a weak image of words moving upward, but it lacks the direct-object and name evidence. It is retained only as acoustic secondary simulation.
- `grade`: strong
- `grade_rationale`: The seed is the first rooted word, the grammar is explicit, and `87:15` independently repeats the same name frame with prayer.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` rows `87:1`, `87:15`; `v4_branches.tsv` rows named; `attachments.tsv` `87:1:a1-a4`, `87:15:a1-a3`; `surah_87.json`.

### CSU-87-02: Created Form, Measured Limit, And Guided Direction

- `candidate_id`: `CSU-87-02`
- `ayah_range`: `87:2-3`, reactivated by `87:8`, `87:14-17`
- `seed_type`: lexical / temporal
- `seed`: `87:2 خَلَقَ` x `خ ل ق B001`, تقدير الشيء وقياسه before action.
- `generating_set`: `(E: خ ل ق B001 تقدير وقياس قبل الفعل)`, `(E: خ ل ق B002 إبداع الخلق وإيجاده)`, `(E: خ ل ق B003 تمام الخلقة واعتدال الصورة)`, `(E: س و ي B002 استقامة وتمام في الذات)`, `(E: س و ي B006 وسط وعدل ومكان منصف)`, `(E: ق د ر B001 مقدار يبلغ الشيء حده)`, `(E: ق د ر B005 تدبير الأمر بتقدير ونظر)`, `(E: ق د ر B006 موافقة الشيء لقدره ووقوعه في حد وسط)`, `(E: ه د ي B001 دلالة بلطف إلى الطريق والحق)`, `(E: ه د ي B002 جهة الأمر وسيرته وقصده)`, `(E: ه د ي B003 المتقدم الهادي وأوائل الشيء)`, `(E: attachments 87:2 a1 and 87:3 a1 ف sequencing)`.
- `selected_branches`: `خ ل ق B001/B002/B003`; `س و ي B002/B006`; `ق د ر B001/B005/B006`; `ه د ي B001/B002/B003`.
- `constructed_model`: A four-step ordering image forms: bringing into being is not random, because creation carries measuring; `فَسَوَّىٰ` gives straightening, completion, and just proportion; `قَدَّرَ` gives limit, capacity, and calculated allotment; `فَهَدَىٰ` gives direction, path, and leading. The developing model is a designed creature or world given form, measure, and a guided course.
- `freeze_point`: after `87:3`.
- `predictions_at_freeze`: the passage should next show a visible instance of guided natural process; later it should transfer guidance from created order to recitation and reminder; human success should look like accepting the measured/easy path rather than preferring the lower-near.
- `unused_features_tested`: `87:4-5` pasture lifecycle; `87:6-9` recitation/ease/reminder; `87:14-17` purification and preference contrast.
- `corroborators`: `(C: 87:4-5 gives an ecological example of emergence, transformation, and limit)`, `(C: ي س ر B001 in 87:8 supplies an eased course after guidance)`, `(C: ز ك و B001/B002 in 87:14 supplies the human result of rightly ordered growth/purity)`, `(C: د ن و B002 and ء خ ر B001 in 87:16-17 supply the rival ordering of near versus later)`.
- `constraints`: `(K: خ ل ق B007 invented speech, B009 worn cloth, B010 perfume, B011 water-hole, B012 sealed rock terminate)`, `(K: س و ي B003 domination/on-top and B007 otherness terminate as no local role)`, `(K: ه د ي B004 gift, B005 sacrificial offering, B006 bride, B007 protected captive, B008 swaying gait terminate or remain remote)`.
- `temporal_reactivation_notes`: The listener first hears general divine action. The `فـ` links make each act answer the preceding one, so `هَدَىٰ` reinterprets `قَدَّرَ` as measure-for-direction, not mere quantity.
- `rival_models`: A ritual-offering fork from `ه د ي B005` can connect weakly to `صلى`, but no offering object appears; it is unlikely.
- `grade`: strong
- `grade_rationale`: Multiple contiguous roots supply distinct roles in exact passage order, and later ease/reminder/purification corroborate the path model.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` `87:2-3`, `87:8`, `87:14-17`; `v4_branches.tsv` named branches; `attachments.tsv` `87:2:a1`, `87:3:a1`.

### CSU-87-03: Pasture Brought Out, Then Dark Withered Drift

- `candidate_id`: `CSU-87-03`
- `ayah_range`: `87:4-5`
- `seed_type`: lexical / constructional
- `seed`: `87:4 أَخْرَجَ` x `خ ر ج B002`, إخراج الشيء من خفائه.
- `generating_set`: `(E: خ ر ج B001 النفاذ إلى خارج الشيء)`, `(E: خ ر ج B002 إخراج الشيء من خفائه)`, `(E: ر ع ي B001 رعي الكلإ والمرعى)`, `(E: ر ع ي B002 حفظ الراعي والرعية as weak care fork)`, `(E: ج ع ل B002 تصيير الشيء على حال)`, `(E: غ ث و B001 غثاء يطفو ويحمله السيل)`, `(E: غ ث و B002 مرعى صار هشيما غثاء)`, `(E: ح و ي B006 الحوة والأحوى: سواد أو حمرة تميل إلى السواد)`, `(E: attachment 87:4 a1 المرعى direct object of أخرج)`, `(E: attachments 87:5 a1-a3 جعلَه غثاء أحوى result complement and adjective)`.
- `selected_branches`: `خ ر ج B001/B002`; `ر ع ي B001` with `B002/B003` as pastoral-care forks; `ج ع ل B002`; `غ ث و B001/B002/B004`; `ح و ي B006`.
- `constructed_model`: The created-and-guided order becomes visible in vegetation. Something hidden or latent is brought out as pasture; then the same object pronoun is made into dry, floating, low-value debris, darkened or black-green. The image has emergence, grazing value, transformation, loss of nutritive freshness, and dark final residue.
- `freeze_point`: after `87:5`.
- `predictions_at_freeze`: a temporal lesson should follow; memory/reminder should preserve what passes; a later preference contrast should distinguish transient near life from enduring afterlife; the seed may corroborate natural cycles rather than translate the whole surah botanically.
- `unused_features_tested`: `87:6-9` recitation/reminder; `87:16-17` near life versus enduring afterlife; `87:18-19` scroll preservation.
- `corroborators`: `(C: ن س ي B001/B002 in 87:6 opposes disappearance/abandonment after the pasture image)`, `(C: ذ ك ر B003/B009 in 87:9-15 supplies preservation/re-presentation after fading)`, `(C: ب ق ي B001 in 87:17 directly answers the perishability of the pasture cycle with endurance)`, `(C: ح ي ي B002 life of earth by rain/nature in 87:16 can echo the pasture but is not the primary contextual meaning there)`.
- `constraints`: `(K: attachment 87:5 a1 makes the suffix in جعله refer back to المرعى; the transformed object is not an unspecified human group)`, `(K: غ ثو B003 nauseated soul is rejected for 87:5 because the object is pasture)`, `(K: ح و ي B001 containment and B002 circularity do not override the adjective color branch B006)`.
- `temporal_reactivation_notes`: The image lands before any explicit moral command except praise. Later `بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا` reactivates the pasture as a transient near-life model.
- `rival_models`: A flood-debris model from `غ ثو B001` and a withered-pasture model from `غ ثو B002` are both retained; the verse's `المرعى` makes B002 primary and B001 supplies motion/low-value debris.
- `grade`: strong
- `grade_rationale`: Direct object continuity, result-complement syntax, and exact branch support make this the most concrete local image.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` `87:4-5`; `v4_branches.tsv` named branches; `attachments.tsv` `87:4:a1`, `87:5:a1-a3`.

### CSU-87-04: Recitation Preserved Under Divine Exception, With Public And Hidden Known

- `candidate_id`: `CSU-87-04`
- `ayah_range`: `87:6-7`, reactivated by `87:9-10`, `87:15`, `87:18-19`
- `seed_type`: lexical / constructional
- `seed`: `87:6 سَنُقْرِئُكَ` x `ق ر ء B002`, قراءة وتلاوة وإقراء.
- `generating_set`: `(E: ق ر ء B002 قراءة وتلاوة وإقراء)`, `(E: ق ر ء B001 جمع واجتماع as collected utterance)`, `(E: ن س ي B001 غفلة الذكر وزواله)`, `(E: ن س ي B002 ترك الشيء وإهماله)`, `(E: ش ي ء B002 المشيئة المتعلقة بالشيء)`, `(E: ء ل ه B001 التعبد والمعبود)`, `(E: ء ل ه B002 اسم الله في القسم والنداء)`, `(E: ع ل م B001 انكشاف الشيء للعارف)`, `(E: ج ه ر B001 إعلان الشيء ورفع الصوت)`, `(E: ج ه ر B002 ظهور الشيء للعين عيانا)`, `(E: خ ف ي B001 الستر والخفاء)`, `(E: attachments 87:6 a1-a2 addressee object and negation of forgetting)`, `(E: attachments 87:7 a1-a9 exception, will, subject, knowledge predicate, paired objects)`.
- `selected_branches`: `ق ر ء B001/B002`; `ن س ي B001/B002`; `ش ي ء B002`; `ء ل ه B001/B002`; `ع ل م B001/B002`; `ج ه ر B001/B002`; `خ ف ي B001/B003` with B003 as reveal-from-hidden fork.
- `constructed_model`: A future act will cause the addressee to receive/recite a gathered utterance, and the promised result is non-forgetting. But the preservation is not autonomous: `إِلَّا مَا شَاءَ ٱللَّهُ` installs divine exception. The reason clause expands the memory field: God knows both what is voiced/manifest and what is hidden. The image is a protected recitational deposit whose public utterance and hidden retention are under one knowing will.
- `freeze_point`: after `87:7`.
- `predictions_at_freeze`: the passage should next move from recitation to facilitated reminder; later remembering the name should show successful retention; closure in scrolls should corroborate stable textual custody.
- `unused_features_tested`: `87:8` ease; `87:9-10` reminder/remembering; `87:15` remembered name and prayer; `87:18-19` scrolls.
- `corroborators`: `(C: ي س ر B001 in 87:8 supplies facilitated performance after recitational preservation)`, `(C: ذ ك ر B003/B009 in 87:9-10 independently satisfies memory/reminder predictions)`, `(C: 87:15 ذَكَرَ ٱسْمَ رَبِّهِ returns from non-forgetting to active mention)`, `(C: ص ح ف B002/B003 in 87:18-19 supplies written preservation outside the immediate oral event)`.
- `constraints`: `(K: ق ر ء B003 menstrual cycle, B004 womb, B009 animal mating, B013 wealth/household terminate)`, `(K: ن س ي B004 sciatic nerve, B006 staff, B007 diluted milk terminate)`, `(K: ج ه ر B005 surprise morning attack and B009 unknown terrain terminate; no hostile raid or lost travel image is supplied)`, `(K: خ ف ي B004 faint lightning is only a weak acoustic/visual image, not primary)`.
- `temporal_reactivation_notes`: `فَلَا تَنسَىٰ` makes forgetting active before `ذِّكْرَى` appears. When `فَذَكِّرْ` and `سَيَذَّكَّرُ` arrive, they do not begin a new topic; they reactivate the preserved recitation as a performed reminder.
- `rival_models`: A womb/gestation model from duplicate `ق ر ء B003` and `ر ح م B003 opening-context` is weak: it can imagine retention and release, but the local verb is causative recitation and the later closure is scrolls, not birth.
- `grade`: strong
- `grade_rationale`: Lexical branches, exception syntax, public/hidden merism, and later reminder/scroll corroborators converge.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` `87:6-7`, `87:9-10`, `87:15`, `87:18-19`; `v4_branches.tsv` named rows; `attachments.tsv` `87:6:a1-a2`, `87:7:a1-a9`.

### CSU-87-05: Ease Channel And Reminder Sorting

- `candidate_id`: `CSU-87-05`
- `ayah_range`: `87:8-11`, constrained by `87:12-13`
- `seed_type`: lexical / constructional
- `seed`: doubled `87:8 ي س ر` occurrence, especially `ي س ر B001`, انفتاح وسهولة بعد عسر.
- `generating_set`: `(E: ي س ر B001 انفتاح وسهولة بعد عسر)`, `(E: ي س ر B005 خفة وانقياد في الحركة)`, `(E: ذ ك ر B003 استحضار الشيء بعد النسيان أو مع الحفظ)`, `(E: ذ ك ر B004 جريان الذكر على اللسان)`, `(E: ذ ك ر B009 الذكرى والتذكرة ما يذكّر)`, `(E: ن ف ع B001 النفع خلاف الضر)`, `(E: خ ش ي B001 الخوف والخشية مع الهيبة)`, `(E: ج ن ب B003 المجانبة إبعاد واعتزال وغربة)`, `(E: ش ق و B002 مشقة العسر والمعاناة)`, `(E: attachments 87:8 a1-a2 object and goal complement)`, `(E: attachments 87:9 a1-a2 conditional benefit)`, `(E: attachments 87:10 a1-a2 receptive subject)`, `(E: attachments 87:11 a1-a2 avoided object and explicit subject)`.
- `selected_branches`: `ي س ر B001/B005` with `B002` as weak smallness fork; `ذ ك ر B003/B004/B009`; `ن ف ع B001`; `خ ش ي B001`; `ج ن ب B003`; `ش ق و B002`.
- `constructed_model`: After preserved recitation, the addressee is prepared toward an easy course. The command `فَذَكِّرْ` then acts only where the reminder has benefit. A receptive person marked by awe will remember; the most wretched moves sideways/away from it. The image is a channeled reminder: ease is not universal uptake, but a prepared path that sorts by inner fear and avoidant hardship.
- `freeze_point`: after `87:11`.
- `predictions_at_freeze`: the avoider should enter a hard, damaging, non-beneficial outcome; the successful counterpart should be named later with purification and prayer; near/later preference should explain why avoidance occurs.
- `unused_features_tested`: `87:12-13` fire and non-life; `87:14-15` success/purification/name/prayer; `87:16-17` preference contrast.
- `corroborators`: `(C: ص ل ي B003 and ن و ر B002 in 87:12 satisfy damaging outcome for the avoider)`, `(C: م و ت B001 and ح ي ي B003 in 87:13 create a blocked life/death result, not benefit)`, `(C: ف ل ح B005 and ز ك و B002 in 87:14 supply the successful opposite)`, `(C: ء ث ر B005/B006 with د ن و B002 in 87:16 explains the lower preference behind avoidance)`.
- `constraints`: `(K: ي س ر B007 gambling/divided camel terminates; no maysir scene)`, `(K: ذ ك ر B001 male branch and B002 hard male/sharpness terminate)`, `(K: ج ن ب B005 leading a side animal and B011 shield are remote; the direct object suffix in يتجنبها points to avoidance of the reminder)`.
- `temporal_reactivation_notes`: The recitation-protection unit ends with God knowing hidden/public. Then `نيسرك` shifts from retained text to facilitated action. `سيذكر من يخشى` makes the hidden inner state predicted by `ما يخفى` visible through response.
- `rival_models`: A bodily side/ shield model from `ج ن ب B001/B011` is possible as secondary posture: the avoider turns his side away. It remains subordinate to the explicit avoidance construction.
- `grade`: strong
- `grade_rationale`: The doubled root `ي س ر`, repeated `ذ ك ر`, conditional syntax, and immediate opposite outcomes are specific and independent.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` `87:8-11`, `87:12-17`; `v4_branches.tsv` named branches; `attachments.tsv` `87:8:a1-a2`, `87:9:a1-a2`, `87:10:a1-a2`, `87:11:a1-a2`.

### CSU-87-06: Great Fire As Suspended Non-Life

- `candidate_id`: `CSU-87-06`
- `ayah_range`: `87:11-13`
- `seed_type`: lexical / temporal
- `seed`: `87:12 يَصْلَى` x `ص ل ي B003`, ملاقاة النار وحرها.
- `generating_set`: `(E: ش ق و B002 مشقة العسر والمعاناة)`, `(E: ص ل ي B003 ملاقاة النار وحرها)`, `(E: ص ل ي B004 إيقاد الصلاء وتسوية الشيء بالنار as heat-mechanism fork)`, `(E: ن و ر B002 النار المتقدة والسمة بها)`, `(E: ن و ر B001 الضياء والإضاءة as luminosity fork)`, `(E: ك ب ر B001 العظم خلاف الصغر)`, `(E: ك ب ر B010 الكبر مشقة وثقل)`, `(E: م و ت B001 ذهاب القوة والحياة)`, `(E: م و ت B012 سكون وخمود كنوم أو بلى)`, `(E: ح ي ي B003 ذو الروح والحيوان)`, `(E: ح ي ي B013 الحياة بمعنى النفع والخير)`, `(E: attachments 87:12 a1-a2 fire object and adjective)`, `(E: attachments 87:13 a1-a2 locative and coordinated negation)`.
- `selected_branches`: `ص ل ي B003/B004`; `ن و ر B002/B001`; `ك ب ر B001/B010`; `م و ت B001/B012`; `ح ي ي B003/B013`; `ش ق و B002`.
- `constructed_model`: The avoider becomes `الأشقى`, the one in hardest misery. The fire is not merely bright but entered and suffered; it is great in scale and weight. Then `ثُمَّ` prolongs the scene into a suspended state: he neither reaches the closure of death nor the benefit/animation of life. The image is a burning containment that blocks both terminal release and living benefit.
- `freeze_point`: after `87:13`.
- `predictions_at_freeze`: a contrary path should show true success, purification, and active worship; later preference for lower life should explain why one enters non-life.
- `unused_features_tested`: `87:14-17`.
- `corroborators`: `(C: ف ل ح B005 in 87:14 supplies the opposite of failed/non-life: الفوز والبقاء في الخير)`, `(C: ز ك و B001/B002 supplies living growth/purity against burned stasis)`, `(C: ح ي ي B013 in 87:16 shows lower life as chosen object, while 87:13 denies real beneficial life in the fire)`.
- `constraints`: `(K: ن و ر B004 tree blossom is a remote contrast only; the explicit surface is النار)`, `(K: ص ل ي B001/B002 prayer/d دعاء branches are rejected for 87:12 because the object is النار; those branches belong to 87:15 under root ص ل و)`, `(K: ك ب ر B006 divine majesty not selected; الكبرى qualifies النار)`.
- `temporal_reactivation_notes`: `الأشقى` is introduced as a subject who avoids the reminder; only in the next ayah does the recitation reveal the consequence. The delayed `ثُمَّ` makes the fire image continue rather than close.
- `rival_models`: A branding/stigma fork from `ن و ر B002` is weak but can image the fire leaving a mark. No explicit mark appears, so it remains secondary.
- `grade`: medium-strong
- `grade_rationale`: The lexical fire/death/life branches are direct and the coordinated negation is strong; grade is capped because some heat-mechanism detail is inferential.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` `87:11-13`; `v4_branches.tsv` named branches; `attachments.tsv` `87:11:a1-a2`, `87:12:a1-a2`, `87:13:a1-a2`.

### CSU-87-07: Success As Growth-Purification, Name-Remembrance, And Prayer

- `candidate_id`: `CSU-87-07`
- `ayah_range`: `87:14-15`, reactivating `87:1` and contrasting `87:11-13`
- `seed_type`: lexical / constructional
- `seed`: `87:14 أَفْلَحَ` x `ف ل ح B005`, فوز وبقاء.
- `generating_set`: `(E: ف ل ح B005 فوز وبقاء)`, `(E: ف ل ح B001 شق الشيء وقطعه as weak agricultural-opening fork)`, `(E: ز ك و B001 النماء والزيادة)`, `(E: ز ك و B002 الطهارة والصلاح)`, `(E: ذ ك ر B003 استحضار الشيء بعد النسيان أو مع الحفظ)`, `(E: ذ ك ر B004 جريان الذكر على اللسان)`, `(E: ذ ك ر B009 ما يذكّر)`, `(E: س م و B005 الاسم تنويه ودلالة)`, `(E: ر ب ب B001 ربوبية وملك وسيادة)`, `(E: ر ب ب B002 إصلاح وتربية وإتمام)`, `(E: ص ل و B002 الدعاء والثناء والرحمة)`, `(E: ص ل و B003 العبادة المخصوصة)`, `(E: attachments 87:14 a1 subject construction)`, `(E: attachments 87:15 a1-a3 name object, iḍāfa, prayer sequence)`.
- `selected_branches`: `ف ل ح B005` with `B001/B003` as agrarian secondary image; `ز ك و B001/B002`; `ذ ك ر B003/B004/B009`; `س م و B005`; `ر ب ب B001/B002`; `ص ل و B002/B003`.
- `constructed_model`: The successful person is one who grows and is purified, then remembers or mentions the Lord's name and prays. This returns to the opening command but now as achieved human response: the purified growth is not merely inner, because it becomes voiced remembrance and enacted prayer.
- `freeze_point`: after `87:15`.
- `predictions_at_freeze`: the next contrast should reveal a rival object of preference; endurance should distinguish this success from the pasture's withered cycle and the fire's non-life.
- `unused_features_tested`: `87:16-17`, `87:18-19`.
- `corroborators`: `(C: 87:1 س ب ح B001/B002 and اسم ربك الأعلى are reactivated exactly)`, `(C: خ ي ر B001/B002 and ب ق ي B001 in 87:17 supply the durable good implied by ف ل ح B005)`, `(C: صحف B002 in 87:18-19 gives continuity of the same instruction beyond one moment)`.
- `constraints`: `(K: ص ل و B001 fire branch is rejected here because 87:15 has the prayer context after name-remembrance; fire branch belongs to 87:12 with ص ل ي)`, `(K: ف ل ح B007 deception in trade terminates; no marketplace/misdirection role)`, `(K: ز ك و B005 pair/even branch terminates except as a very weak two-part response: remembrance plus prayer)`.
- `temporal_reactivation_notes`: The opening imperative is not fulfilled immediately. The listener passes through creation, pasture, recitation, reminder, and punishment before the positive responder appears; that delay makes `وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ` a backward completion of `سَبِّحِ ٱسْمَ رَبِّكَ`.
- `rival_models`: An agricultural success model from `ف ل ح B001/B003` and `ز ك و B001` coheres with pasture, but the direct lexical outcome is moral/worship success, so the agrarian model is secondary.
- `grade`: strong
- `grade_rationale`: Repetition of the exact opening name frame plus independent purification, success, and prayer branches produce high specificity.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` `87:1`, `87:14-15`, `87:17-19`; `v4_branches.tsv` named branches; `attachments.tsv` `87:14:a1`, `87:15:a1-a3`.

### CSU-87-08: Preference For The Near Versus Better Enduring Afterlife

- `candidate_id`: `CSU-87-08`
- `ayah_range`: `87:16-17`
- `seed_type`: lexical / constructional
- `seed`: `87:16 تُؤْثِرُونَ` x `ء ث ر B005`, تفضيل الغير أو الشيء بالاختيار.
- `generating_set`: `(E: ء ث ر B005 تفضيل الشيء بالاختيار)`, `(E: ء ث ر B001 تقديم الشيء في البدء أو الاختيار)`, `(E: ء ث ر B006 استبداد المرء بالشيء لنفسه as selfish preference fork)`, `(E: ح ي ي B003 ذو الروح والحيوان / life)`, `(E: ح ي ي B013 الحياة بمعنى النفع والخير)`, `(E: د ن و B001 القرب والمقاربة)`, `(E: د ن و B002 الدنيا والأدنى)`, `(E: د ن و B003 الدناءة والضعة as constraining lower-quality echo)`, `(E: ء خ ر B001 الآخرية بعد الأول)`, `(E: ء خ ر B002 التأخير إلى وقت لاحق)`, `(E: خ ي ر B001 الخير النافع)`, `(E: خ ي ر B002 فضل الصلاح والاصطفاء)`, `(E: ب ق ي B001 دوام الشيء وبقاؤه)`, `(E: ب ق ي B002 البقية وما يبقى من الشيء)`, `(E: attachments 87:16 a1-a2 object and adjective)`, `(E: attachments 87:17 a1-a3 predication and parallel comparative predicates)`.
- `selected_branches`: `ء ث ر B001/B005/B006`; `ح ي ي B003/B013`; `د ن و B001/B002/B003`; `ء خ ر B001/B002`; `خ ي ر B001/B002/B003`; `ب ق ي B001/B002`.
- `constructed_model`: The contrast is an ordering failure. The addressees choose and put forward the near/lower life. The afterlife, delayed and later in sequence, is better in quality and more enduring in time. The model explains why the reminder sorts people: refusal is a mis-ranked temporal preference.
- `freeze_point`: after `87:17`.
- `predictions_at_freeze`: the final closure should make this not a newly invented local moral but an old recorded principle; earlier pasture should reactivate as a near-life image that quickly becomes debris.
- `unused_features_tested`: `87:4-5` pasture cycle; `87:18-19` scroll closure.
- `corroborators`: `(C: غ ثو B002 in 87:5 gives concrete transient near-life withering)`, `(C: ف ل ح B005 in 87:14 and ب ق ي B001 in 87:17 share success/endurance)`, `(C: ص ح ف B002/B003 and ء و ل B001 in 87:18-19 corroborate old recorded continuity)`.
- `constraints`: `(K: ء ث ر B007 sword mark and B008 camel-hoof marking terminate; no strike/tracking scene)`, `(K: ح ي ي B002 vegetation-life is only a backward echo to pasture, not the primary object in 87:16)`, `(K: د ن و B004 birth-nearness and B005 bent body terminate)`.
- `temporal_reactivation_notes`: `بَلْ` interrupts the success sequence and reveals why the warning is needed. The listener is forced to compare immediate life with the delayed but enduring reality.
- `rival_models`: A transmission model from `ء ث ر B002/B003` connects weakly to scrolls as inherited report/trace; it is better used as corroboration for `87:18-19`, not as the main meaning of `تؤثرون`.
- `grade`: strong
- `grade_rationale`: The exact contrast construction and comparative predicates independently support preference, nearness, laterness, goodness, and endurance.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` `87:16-17`, `87:4-5`, `87:18-19`; `v4_branches.tsv` named branches; `attachments.tsv` `87:16:a1-a2`, `87:17:a1-a3`.

### CSU-87-09: Former Scrolls As Written Continuity And Return To First Principles

- `candidate_id`: `CSU-87-09`
- `ayah_range`: `87:18-19`
- `seed_type`: lexical / constructional
- `seed`: `87:18 ٱلصُّحُفِ` x `ص ح ف B002`, صحيفة مكتوبة.
- `generating_set`: `(E: ص ح ف B002 صحيفة مكتوبة)`, `(E: ص ح ف B003 جمع الصحف في مصحف)`, `(E: ص ح ف B001 انبساط وسعة as surface/page fork)`, `(E: ء و ل B001 ابتداء الشيء وتقدمه)`, `(E: ء و ل B002 رجوع الشيء إلى مآله وعاقبته)`, `(E: ء و ل B004 إيالة الأمر بإصلاحه وسياسته as weak governance-continuity fork)`, `(E: attachments 87:18 a1-a4 demonstrative, prepositional predicate, الصحف complement, الأولى adjective)`, `(E: attachments 87:19 a1-a3 idāfa to Ibrahim and Moses)`.
- `selected_branches`: `ص ح ف B001/B002/B003`; `ء و ل B001/B002`; `ء و ل B004` weakly; plus proper-name possessor construction.
- `constructed_model`: The final claim is placed in written sheets that are former/first. The closure does not add a new image but stabilizes the whole recitation as continuity: the principle of purified naming, measured guidance, reminder, sorting, and preference for the enduring afterlife is already on earlier written surfaces associated with Ibrahim and Musa.
- `freeze_point`: after `87:19`, final closure.
- `predictions_at_freeze`: no later passage material remains. The test is backward: does scroll closure explain why recitation, remembering, name, and old/later contrast were activated?
- `unused_features_tested`: whole passage backward replay.
- `corroborators`: `(C: ق ر ء B002 in 87:6 supplies oral recitation; صحف B002 supplies written preservation)`, `(C: ذ ك ر B008 ذكر الحق صك ووثيقة حق is a weak corroborator for remembered/documented right)`, `(C: ء ث ر B002 نقل الخبر حتى يصير مأثورا and B003 علامة باقية تدل على ما كان weakly corroborate transmitted trace after the preference contrast)`, `(C: 87:1 name command and 87:15 name/prayer bracket the written closure with worship continuity)`.
- `constraints`: `(K: ص ح ف B004 bowl branch terminates; no vessel image)`, `(K: ص ح ف B005 misreading/corruption is a constraint only: the passage claims stable former scrolls, not mistaken reading)`, `(K: ء و ل B005 coagulated liquid, B008 tool, B009 mountain animal, B010 drink vessel terminate)`.
- `temporal_reactivation_notes`: The closure replays the whole surah as not a one-time exhortation but a preserved pattern already in former sheets. The oral `سنقرئك` and written `الصحف` now form a two-channel memory system.
- `rival_models`: A political-governance model from `ء و ل B004` can read the old scrolls as managed order, but the direct construction is locative textual custody, so governance remains secondary.
- `grade`: medium-strong
- `grade_rationale`: The textual branches and attachment rows are direct; the broader backward integration is interpretive but well supported by recitation/remembrance links.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` `87:6`, `87:9-10`, `87:15`, `87:18-19`; `v4_branches.tsv` named branches; `attachments.tsv` `87:18:a1-a4`, `87:19:a1-a3`.

### CSU-87-10: Passage-Scale Reactivation Trajectory

- `candidate_id`: `CSU-87-10`
- `ayah_range`: `87:1-19`
- `seed_type`: verified composite
- `seed`: convergence of independently run seeds `س ب ح B002`, `خ ل ق B001/B002`, `خ ر ج B002`, `ق ر ء B002`, `ي س ر B001`, `ذ ك ر B009`, `ف ل ح B005`, `ء ث ر B005`, `ص ح ف B002`.
- `generating_set`: `(E: CSU-87-01 highest-name purification)`, `(E: CSU-87-02 created-measured-guided order)`, `(E: CSU-87-03 pasture emergence and withering)`, `(E: CSU-87-04 preserved recitation)`, `(E: CSU-87-05 reminder sorting)`, `(E: CSU-87-07 successful purification/name/prayer)`, `(E: CSU-87-08 near/later preference)`, `(E: CSU-87-09 scroll continuity)`.
- `selected_branches`: composite only from previously frozen candidate units; no new branch introduced after freeze.
- `constructed_model`: The passage begins by purifying the highest name. It then displays a Lord whose created order is formed, measured, and guided, with pasture as the most concrete demonstration of emergence and transience. The addressee receives protected recitation so that forgetting does not erase the guidance. That recitation becomes an eased reminder, which benefits the fearful but is avoided by the most wretched, whose end is burning non-life. The successful response completes the opening command by purifying, remembering the Lord's name, and praying. The final contrast names the central human failure as preferring the near life over the better enduring afterlife, and the scroll closure stabilizes the whole pattern as former written continuity.
- `freeze_point`: after integrating `87:18-19`; no new evidence remains.
- `predictions_at_freeze`: passage order should matter: name before creation; creation before pasture; pasture before memory; memory before reminder; reminder before sorting; sorting before preference diagnosis; preference before old-scroll closure.
- `unused_features_tested`: all rooted occurrences and constructional seeds in the sweep.
- `corroborators`: `(C: repeated اسم رب in 87:1 and 87:15)`, `(C: repeated ذ ك ر forms in 87:9, 87:10, 87:15)`, `(C: oral/written pair ق ر ء B002 and ص ح ف B002)`, `(C: transient pasture versus أبقى)`, `(C: hidden/public knowledge before hidden inner response of خشية and avoidance)`.
- `constraints`: `(K: composite does not replace the primary statements with a single botanical or textual metaphor)`, `(K: several remote branches produced local images only and are not allowed to upgrade the candidate)`, `(K: duplicate branch export rows for ق ر ء and ش ي ء were not double-counted)`.
- `temporal_reactivation_notes`: The strongest temporal reactivation is `87:15` completing `87:1`. Secondary reactivations are `87:16-17` replaying the pasture's transience, `87:9-10` replaying `فلا تنسى`, and `87:18-19` replaying oral recitation as written custody.
- `rival_models`: A pure nature-cycle reading explains 87:2-5 and 87:16-17 but under-explains recitation/reminder/scrolls. A pure scripture-memory reading explains 87:6-19 but under-explains the creation/pasture setup. The composite keeps both as ordered subsystems.
- `grade`: medium-strong
- `grade_rationale`: Many independent candidates converge, but passage-scale synthesis is broader than any single lexical seed and must remain secondary to the specific units above.
- `source_queries_or_rows_used`: all S87 rows from `qac_root_ayah.tsv`, filtered `attachments.tsv`, and S87-root rows from `v4_branches.tsv`.

## Exhaustive Seed Ledger

This ledger records every rooted word/root branch family and eligible construction seed. `Selected` means at least one branch entered a candidate above. `Terminated` means the branch was initiated but found no passage-local role beyond generic association.

| seed root or construction | selected/local branches | terminated or constrained branches |
| --- | --- | --- |
| `87:1 س ب ح` | `B001`, `B002`; `B004` weak acoustic fork | `B005,B006,B007,B008` |
| `87:1/15 س م و` | `B005`; `B001,B008` corroborative height/repute | `B002,B003,B004,B006,B007` |
| `87:1/15 ر ب ب` | `B001,B002`; `B007,B011` weak durability/covenant echoes | `B003,B004,B005,B006,B008,B009,B010,B012,B013,B014,B015,B016,B017` |
| `87:1 ع ل و` | `B001,B002,B005` | `B003,B004,B006,B008,B009,B010,B011,B012` |
| `87:2 خ ل ق` | `B001,B002,B003` | `B004,B005,B007,B008,B009,B010,B011,B012` |
| `87:2 س و ي` | `B002,B006`; `B001,B004` local | `B003,B005,B007,B008,B009,B010,B012,B013` |
| `87:3 ق د ر` | `B001,B005,B006`; `B003` capacity echo | `B004,B007` |
| `87:3 ه د ي` | `B001,B002,B003,B010` | `B004,B005,B006,B007,B008,B009,B011` |
| `87:4 خ ر ج` | `B001,B002` | `B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013` |
| `87:4 ر ع ي` | `B001`; `B002,B003,B004,B005,B006` local pastoral/hearing/withdrawing echoes | none excluded from local audit, but only `B001` constructs CSU-87-03 |
| `87:5 ج ع ل` | `B002`; `B001,B004` local | `B005,B006,B007,B008,B009,B010,B011,B012` |
| `87:5 غ ث و` | `B001,B002,B004` | `B003` |
| `87:5 ح و ي` | `B006`; `B001,B002,B008` weak containment/water forks | `B003,B004,B005,B007` |
| `87:6 ق ر ء` | `B001,B002`; duplicate `B001` oral collection row | `B003,B004,B005,B006,B008,B009,B010,B011,B013` and duplicate `B002,B003,B005,B006` as non-counted extras |
| `87:6 ن س ي` | `B001,B002`; `B003` weak cast-off echo with غثاء | `B004,B005,B006,B007` |
| `87:7 ش ي ء` | `B001,B002`; duplicate `B001` المشيئة row selected as same semantic field | `B003,B004,B005,B006,B007,B008,B009` plus duplicate non-counted rows |
| `87:7 ء ل ه` | `B001,B002` | none |
| `87:7 ع ل م` | `B001,B002` | `B004,B005,B006,B007` |
| `87:7 ج ه ر` | `B001,B002`; `B011` acoustic constraint | `B003,B004,B005,B006,B007,B008,B009` |
| `87:7 خ ف ي` | `B001`; `B003` reveal-from-hidden fork | `B002,B004` |
| `87:8 ي س ر` | `B001,B005`; `B002` weak smallness/ease echo | `B003,B004,B006,B007,B008,B009,B010,B011` |
| `87:9/10/15 ذ ك ر` | `B003,B004,B009`; `B007,B008` repute/document echoes | `B001,B002` |
| `87:9 ن ف ع` | `B001` | `B002,B003` |
| `87:10 خ ش ي` | `B001`; `B002` knowledge echo | `B004` |
| `87:11 ج ن ب` | `B003`; `B001,B002,B011` posture/side echoes | `B005,B006,B007,B008,B009,B010,B012` |
| `87:11 ش ق و` | `B002`; `B004` climbing-hardship weak image | `B003` |
| `87:12 ص ل ي` | `B003,B004` | `B001,B002,B005,B006,B007,B008,B009,B010` |
| `87:12 ن و ر` | `B002`; `B001,B004` luminosity/vegetation contrast | `B005,B006,B007,B008,B009` |
| `87:12 ك ب ر` | `B001,B010`; `B006,B007` gravity/sin echo | `B002,B003,B004,B005,B011,B012,B013` |
| `87:13 م و ت` | `B001,B012`; `B013` submission echo | `B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B014` |
| `87:13/16 ح ي ي` | `B003,B013`; `B002` pasture-life echo | `B004,B006,B007,B009,B010,B011,B012` |
| `87:14 ف ل ح` | `B005`; `B001,B003` agrarian split/cultivation echo | `B002,B004,B006,B007` |
| `87:14 ز ك و` | `B001,B002`; `B004` fitness echo | `B005` |
| `87:15 ص ل و` | `B002,B003`; `B006` following-after echo | `B001,B004,B005,B007,B008,B009` |
| `87:16 ء ث ر` | `B001,B005,B006`; `B002,B003` transmission/trace corroboration for scroll closure | `B004,B007,B008,B009,B011,B012` |
| `87:16 د ن و` | `B001,B002,B003` | `B004,B005` |
| `87:17 ء خ ر` | `B001,B002` | `B003` |
| `87:17 خ ي ر` | `B001,B002,B003`; `B005` generosity echo | `B006` |
| `87:17 ب ق ي` | `B001,B002`; `B003` mercy/non-erasure echo | `B004,B005` |
| `87:18/19 ص ح ف` | `B001,B002,B003`; `B005` constraint | `B004` |
| `87:18 ء و ل` | `B001,B002`; `B004` weak order/governance echo | `B003,B005,B007,B008,B009,B010` |
| `imperative سبح اسم ربك الأعلى` | selected in CSU-87-01 | constrained by direct-object attachment |
| `relative action chain 87:2-5` | selected in CSU-87-02 and CSU-87-03 | no separate rival after branch testing |
| `exception إلا ما شاء الله` | selected in CSU-87-04 | constrained: exception remains divine will, not textual instability |
| `الجهر وما يخفى pair` | selected in CSU-87-04 and corroborates CSU-87-05 | no further rival |
| `نيسرك لليسرى doubled root` | selected in CSU-87-05 | no further rival |
| `إن نفعت الذكرى conditional` | selected in CSU-87-05 | constrains reminder benefit as conditional |
| `لا يموت فيها ولا يحيا` | selected in CSU-87-06 | constrains fire outcome as suspended state |
| `بل تؤثرون... والآخرة...` | selected in CSU-87-08 | constrains diagnosis to preference/ranking |
| `لفي الصحف الأولى / صحف إبراهيم وموسى` | selected in CSU-87-09 | constrains closure as textual continuity |

## Image Packet Catalog

`IMG-87-01`

Starting seed: `س ب ح B002` at `87:1`.

Complete image: purified vertical address of the highest Lord's name.

Passage-order assembly: `سبح` -> `اسم` -> `ربك` -> `الأعلى`, reactivated by `ذكر اسم ربه فصلى`.

Participants and roles: addressee as commanded speaker/worshipper; name as direct object; Lord as sovereign nurturer; highest as vertical rank.

Operation / mechanism: remove unsuitable attribution and align speech/worship to the name.

Direction / force / medium: upward rank and oral/prayer medium.

Temporal development: command first, successful human response late.

Outcome / closure: confirmed in old scroll continuity.

Exact branch constituents: `س ب ح B001/B002`, `س م و B005`, `ر ب ب B001/B002`, `ع ل و B001/B002/B005`, `ص ل و B002/B003`.

Unfilled roles: none.

Status: COMPLETE.

`IMG-87-02`

Starting seed: `خ ل ق B001/B002` at `87:2`.

Complete image: created form is measured, proportioned, and guided.

Passage-order assembly: `خلق` -> `سوى` -> `قدر` -> `هدى` -> ecological example.

Participants and roles: Lord as creator/measurer/guide; created thing as formed object; path/course as outcome.

Operation / mechanism: bringing into being, leveling, limiting, directing.

Direction / force / medium: ordered causation through `فـ`.

Temporal development: creation precedes proportion; measure precedes guidance.

Outcome / closure: human ease/reminder tests whether guidance is accepted.

Exact branch constituents: `خ ل ق B001/B002/B003`, `س و ي B002/B006`, `ق د ر B001/B005/B006`, `ه د ي B001/B002/B003`.

Unfilled roles: specific created object remains general until pasture.

Status: COMPLETE.

`IMG-87-03`

Starting seed: `خ ر ج B002` at `87:4`.

Complete image: pasture emerges and is turned into dark withered drift.

Passage-order assembly: `أخرج المرعى` -> `جعله غثاء أحوى` -> later `الدنيا` versus `أبقى`.

Participants and roles: Lord as bringer-out/transformer; pasture as object; residue as final state.

Operation / mechanism: emergence, grazing value, result transformation, darkening/withered scattering.

Direction / force / medium: outward from hiddenness; downward into low-value debris.

Temporal development: fresh emergence becomes spent residue.

Outcome / closure: reactivated as transience against enduring afterlife.

Exact branch constituents: `خ ر ج B001/B002`, `ر ع ي B001`, `ج ع ل B002`, `غ ث و B001/B002/B004`, `ح و ي B006`.

Unfilled roles: water/rain is implicit but not stated in S87.

Status: COMPLETE.

`IMG-87-04`

Starting seed: `ق ر ء B002` at `87:6`.

Complete image: oral recitation preserved against forgetting under divine will, with public and hidden known.

Passage-order assembly: `سنقرئك` -> `فلا تنسى` -> exception -> public/hidden knowledge -> reminder -> scrolls.

Participants and roles: God as reciter/knower; addressee as recipient; recitation as deposit; public and hidden as knowledge domains.

Operation / mechanism: causing recitation, preventing forgetting, bounding by will, knowing manifest/concealed.

Direction / force / medium: oral transmission and memory.

Temporal development: future promise becomes reminder action.

Outcome / closure: written scrolls stabilize the oral deposit.

Exact branch constituents: `ق ر ء B001/B002`, `ن س ي B001/B002`, `ش ي ء B002`, `ع ل م B001`, `ج ه ر B001/B002`, `خ ف ي B001`, `ص ح ف B002/B003`.

Unfilled roles: exact identity of `ما شاء الله` remains unspecified by the passage.

Status: COMPLETE.

`IMG-87-05`

Starting seed: `ي س ر B001` at `87:8`.

Complete image: an eased reminder channel sorts receptive fear from avoidant wretchedness.

Passage-order assembly: `نيسرك لليسرى` -> `فذكر` -> conditional benefit -> fearful remembers -> most wretched avoids.

Participants and roles: addressee as reminder-giver; reminder as object; fearful person as receptive; most wretched as avoider.

Operation / mechanism: facilitation, reminding, benefit, inner awe, lateral avoidance.

Direction / force / medium: toward easy course versus away-to-the-side.

Temporal development: facilitation enables reminder; reminder reveals inner state.

Outcome / closure: avoider enters fire; purified person succeeds.

Exact branch constituents: `ي س ر B001/B005`, `ذ ك ر B003/B004/B009`, `ن ف ع B001`, `خ ش ي B001`, `ج ن ب B003`, `ش ق و B002`.

Unfilled roles: why one fears is not explained inside this unit.

Status: COMPLETE.

`IMG-87-06`

Starting seed: `ء ث ر B005` at `87:16`.

Complete image: temporal misranking chooses the near/lower life over the better enduring afterlife.

Passage-order assembly: `بل تؤثرون` -> `الحياة الدنيا` -> `والآخرة خير وأبقى` -> scroll closure.

Participants and roles: plural humans as choosers; lower life as preferred object; afterlife as delayed enduring good.

Operation / mechanism: preference, ranking, comparison, endurance.

Direction / force / medium: near/lower versus later/enduring.

Temporal development: diagnosis follows example, warning, and success.

Outcome / closure: the principle is affirmed in former scrolls.

Exact branch constituents: `ء ث ر B001/B005/B006`, `ح ي ي B003/B013`, `د ن و B001/B002/B003`, `ء خ ر B001/B002`, `خ ي ر B001/B002`, `ب ق ي B001/B002`, `ص ح ف B002`.

Unfilled roles: none.

Status: COMPLETE.

`IMG-87-07`

Starting seed: `ص ل ي B003` at `87:12`.

Complete image: the most wretched enters a great fire and is held in suspended non-life.

Passage-order assembly: avoider of reminder -> most wretched -> fire -> no death and no life.

Participants and roles: avoider as sufferer; fire as burning containing medium; death and life as denied closures.

Operation / mechanism: heat-contact, enlargement/weight, locative containment, coordinated negation.

Direction / force / medium: into fire, then held there.

Temporal development: avoidance becomes consequence; consequence does not terminate.

Outcome / closure: not release by death and not benefit by life.

Exact branch constituents: `ج ن ب B003`, `ش ق و B002`, `ص ل ي B003/B004`, `ن و ر B002`, `ك ب ر B001/B010`, `م و ت B001/B012`, `ح ي ي B003/B013`.

Unfilled roles: duration beyond the suspended state is not specified in this unit.

Status: COMPLETE.

`IMG-87-08`

Starting seed: `ف ل ح B005` at `87:14`.

Complete image: success appears as purified growth that remembers the Lord's name and prays.

Passage-order assembly: success -> purification/growth -> name remembrance -> prayer -> preference contrast.

Participants and roles: purified person as successful responder; Lord's name as remembered object; prayer as enacted response.

Operation / mechanism: purification, remembrance, voiced naming, worship.

Direction / force / medium: inward purification becomes outward mention and prayer.

Temporal development: the opening command returns as fulfilled response after warning.

Outcome / closure: opposed to near-life preference and aligned with enduring good.

Exact branch constituents: `ف ل ح B005`, `ز ك و B001/B002`, `ذ ك ر B003/B004/B009`, `س م و B005`, `ر ب ب B001/B002`, `ص ل و B002/B003`.

Unfilled roles: none.

Status: COMPLETE.

`IMG-87-09`

Starting seed: `ص ح ف B002` at `87:18`.

Complete image: the recited principle is stabilized on former written sheets.

Passage-order assembly: demonstrative `هذا` -> in former scrolls -> scrolls of Ibrahim and Musa.

Participants and roles: this recited teaching as content; scrolls as written surface/custody; earlier named figures as possessors or associated transmitters.

Operation / mechanism: inscription/custody, earlierness, continuity.

Direction / force / medium: oral recitation is grounded in written former record.

Temporal development: final backward replay of the whole surah as old continuity.

Outcome / closure: the passage closes by anchoring itself in earlier scripture.

Exact branch constituents: `ص ح ف B001/B002/B003`, `ء و ل B001/B002`, `ق ر ء B002`, `ذ ك ر B008` weak document corroborator, `ء ث ر B002/B003` weak transmitted-trace corroborator.

Unfilled roles: exact content boundaries of `هذا` remain broad.

Status: COMPLETE.
