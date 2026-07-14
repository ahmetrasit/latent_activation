# S89 Stage 1 Pass 2: Temporally Conditioned Reactivation

Assigned passage: S89, al-Fajr. Sacred Arabic text source: `resources/quran/surah_89.json`.

## Root Cause of Pass 1 Limitation

Pass 1 compressed the work too early. The local branch inventory for S89 is large: 64 rooted passage roots, 520 accepted v4 branch rows, and 825 occurrence-by-branch lexical seed passes after repeated rooted occurrences are counted. I treated that inventory as a discovery control and then wrote only high-yield images, instead of forcing every occurrence-by-branch seed to receive an explicit pass outcome. That caused a limited-word-per-finding pattern: roots that seemed promising early received deep treatment, while weak, remote, or dead branches were collapsed into general notes.

This Pass 2 restarts at the first rooted word, `فجر` in 89:1, and records the exhaustive sweep boundary explicitly. The SQLite files named in the prompt were not present in this checkout; the available local v1 resource copies used here were `resources/qac_root_ayah.tsv`, `resources/v4_branches.tsv`, `resources/attachments.tsv`, and `resources/quran/surah_89.json`. No translation was used as evidence.

## Passage Exposure and First Rooted Sequence

Opening context: `بسم الله الرحمن الرحيم` is treated only as opening-context evidence: `س م و`, `ء ل ه`, and `ر ح م` may corroborate naming, divine source, mercy, or enclosure, but never initiate seeds.

Passage rooted sequence by activation block:

- 89:1-5: `ف ج ر`, `ل ي ل`, `ع ش ر`, `ش ف ع`, `و ت ر`, `ل ي ل`, `س ر ي`, `ق س م`, `ح ج ر`.
- 89:6-14: `ر ء ي`, `ك ي ف`, `ف ع ل`, `ر ب ب`, `ع و د`, `ع م د`, `خ ل ق`, `م ث ل`, `ب ل د`, `ج و ب`, `ص خ ر`, `و د ي`, `و ت د`, `ط غ ي`, `ك ث ر`, `ف س د`, `ص ب ب`, `س و ط`, `ع ذ ب`, `ر ص د`.
- 89:15-20: `ء ن س`, `ب ل و`, `ر ب ب`, `ك ر م`, `ن ع م`, `ق و ل`, `ق د ر`, `ر ز ق`, `ه و ن`, `ي ت م`, `ح ض ض`, `ط ع م`, `س ك ن`, `ء ك ل`, `و ر ث`, `ل م م`, `ح ب ب`, `م و ل`, `ج م م`.
- 89:21-26: `د ك ك`, `ء ر ض`, `ج ي ء`, `ر ب ب`, `م ل ك`, `ص ف ف`, `ذ ك ر`, `ء ن س`, `ء ن ي`, `ق و ل`, `ق د م`, `ح ي ي`, `ع ذ ب`, `ء ح د`, `و ث ق`.
- 89:27-30: `ن ف س`, `ط م ن`, `ر ج ع`, `ر ب ب`, `ر ض و`, `د خ ل`, `ع ب د`, `د خ ل`, `ج ن ن`.

## Exhaustive Lexical Seed Ledger

Each listed accepted branch was initiated as a seed at each occurrence of its root. Branch IDs are from `resources/v4_branches.tsv`, `status=accepted`. `P` means at least one occurrence-by-branch pass generated or expanded a retained image below. `T` means the branch terminated after failing to create passage-local role completion beyond generic association. `K` means the branch mainly constrained or narrowed another image after freeze. Repeated roots were tested at each occurrence with different temporal state; the row gives the branch status across those occurrence passes.

| root | occ | branches | branch-pass outcome |
| --- | ---: | --- | --- |
| ف ج ر | 1 | B001,B002,B003,B004,B005,B006 | P: B001,B002,B004; T: B003,B005,B006 |
| ل ي ل | 2 | B001,B002,B003,B004 | P: B001,B002; K/T: B003; T: B004 |
| ع ش ر | 1 | B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014,B017 | P: B001,B002,B005; K: B003,B009; T: B004,B006,B007,B008,B010,B011,B012,B013,B014,B017 |
| ش ف ع | 1 | B001,B002,B003,B004,B005,B006 | P: B001,B002; K/T: B006; T: B003,B004,B005 |
| و ت ر | 1 | B001,B002,B003,B004,B005,B006,B007,B008,B009,B010 | P: B001,B003,B004,B005,B007,B009,B010; T: B002,B006,B008 |
| س ر ي | 1 | B001,B002,B003,B004,B005 | P: B001,B002,B004; K/T: B003; T: B005 |
| ق س م | 1 | B001,B002,B003,B004,B006,B007,B008 | P: B003,B004,B006; T: B001,B002,B007,B008 |
| ح ج ر | 1 | B001,B002,B003,B004,B005,B006,B007 | P: B001,B002,B003,B004,B006; T: B005,B007 |
| ر ء ي | 1 | B001-B013 | P: B001,B002,B012,B013; K/T: B004,B006,B011; T: B003,B005,B007,B008,B009,B010 |
| ك ي ف | 1 | no accepted v4 branch returned | seed pass retained only as constructional interrogative manner, not lexical branch evidence |
| ف ع ل | 1 | B001,B002,B003,B004,B005,B007 | P: B001,B002; K: B004; T: B003,B005,B007 |
| ر ب ب | 8 | B001-B017 | P: B001,B002,B007,B008,B011,B016; K/T: B003,B004,B005,B006,B009,B010,B012,B013,B014,B015,B017 |
| ع و د | 1 | B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B012 | P: B001,B002,B009,B012; K/T: B004,B006,B007,B008,B010; T: B003,B005 |
| ع م د | 1 | B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B013,B014,B015 | P: B001,B002,B003,B005,B006,B007,B013,B014; K/T: B008,B009,B010,B015; T: B004,B011 |
| خ ل ق | 1 | B001,B002,B003,B004,B005,B007,B008,B009,B010,B011,B012 | P: B001,B002,B003,B005,B008,B011,B012; K: B004,B007,B009; T: B010 |
| م ث ل | 1 | B001-B012 | P: B001,B002,B005,B008,B010,B011; K/T: B004,B006,B009,B012; T: B003,B007 |
| ب ل د | 2 | B001-B012 | P: B001,B004,B005,B007,B009,B010,B011; K/T: B002,B003,B006,B008,B012 |
| ج و ب | 1 | B001-B005 | P: B001,B002,B004; K/T: B003; T: B005 |
| ص خ ر | 1 | B001-B004 | P: B001,B004; T: B002,B003 |
| و د ي | 1 | B001-B006 | P: B004,B005; K/T: B002,B003,B006; T: B001 |
| و ت د | 1 | B001-B004 | P: B001,B003; K/T: B002; T: B004 |
| ط غ ي | 1 | B001,B002,B003,B005 | P: B001,B002,B003,B005 |
| ك ث ر | 1 | B001,B002,B003,B005,B006,B007 | P: B001,B002,B005; K/T: B003,B007; T: B006 |
| ف س د | 1 | B001 | P: B001 |
| ص ب ب | 1 | B001,B002,B003,B004,B005,B006,B007,B009,B010,B011 | P: B001,B002,B006,B009,B010,B011; K/T: B003,B004,B005,B007 |
| س و ط | 1 | B001,B002,B004 | P: B001,B002; T: B004 |
| ع ذ ب | 3 | B001,B002,B003,B004,B005,B006,B008,B009 | P: B003,B005,B006; K/T: B001,B002,B004,B008,B009 |
| ر ص د | 1 | B001-B004 | P: B001,B002,B003,B004 |
| ء ن س | 2 | B001-B006 | P: B001,B002,B003,B005,B006; K/T: B004 |
| ب ل و | 2 | B001-B009 | P: B001,B002,B003,B004,B005,B007,B009; K/T: B006,B008 |
| ك ر م | 3 | B001-B010 | P: B001,B002,B006,B008,B009,B010; K/T: B003,B004,B005,B007 |
| ن ع م | 1 | B001-B013 | P: B001,B002,B005,B007,B008,B010,B011,B013; K/T: B003,B004,B006,B009,B012 |
| ق و ل | 3 | B001-B016 | P: B001,B003,B005,B007,B009,B011,B012,B013,B014,B015; K/T: B002,B004,B006,B008,B010,B016 |
| ق د ر | 1 | B001,B003,B004,B005,B006,B007 | P: B001,B003,B004,B005,B006; T: B007 |
| ر ز ق | 1 | B001,B002,B003,B004,B006,B007 | P: B001,B002,B003,B004,B006; T: B007 |
| ه و ن | 1 | B001-B004 | P: B001,B002,B003,B004 |
| ي ت م | 1 | B001-B005 | P: B001,B002,B003,B004,B005 |
| ح ض ض | 1 | B001-B004 | P: B001,B002,B003; K/T: B004 |
| ط ع م | 1 | B001,B002,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014 | P: B001,B002,B004,B005,B008,B010,B011,B012; K/T: B006,B007,B009,B013,B014 |
| س ك ن | 1 | B001,B002,B003,B004,B006,B007,B008,B009,B010 | P: B001,B002,B003,B004,B006,B007,B008,B009,B010 |
| ء ك ل | 2 | B001,B002,B003,B004,B005,B006,B007,B009,B010,B011,B012,B013 | P: B001,B003,B004,B005,B006,B009,B010,B012,B013; K/T: B002,B007,B011 |
| و ر ث | 1 | B001,B002,B003,B005 | P: B001,B002,B003,B005 |
| ل م م | 1 | B001-B010 | P: B001,B002,B003,B004,B006,B007,B008; T: B005,B009,B010 |
| ح ب ب | 2 | B001-B011 | P: B001,B002,B004,B005,B006,B007,B008,B011; K/T: B003,B009,B010 |
| م و ل | 1 | B001 | P: B001 |
| ج م م | 1 | B001-B009 | P: B001,B002,B003,B004,B005,B006,B007,B008,B009 |
| د ك ك | 3 | B001,B002,B003,B006,B007,B008,B009 | P: B001,B002,B003,B006,B007,B008,B009 |
| ء ر ض | 1 | B001-B012 | P: B001,B002,B006,B008,B010,B011,B012; K/T: B003,B004,B005,B007,B009 |
| ج ي ء | 2 | duplicate branch rows B001-B006 and B001-B003 | P: B001,B004,B005; K/T: B002,B003,B006 |
| م ل ك | 1 | B001-B008 | P: B001,B003,B005,B006,B008; K/T: B002,B004,B007 |
| ص ف ف | 2 | B001-B007 | P: B001,B005,B007; K/T: B002,B003,B004,B006 |
| ذ ك ر | 2 | B001,B002,B003,B004,B007,B008,B009 | P: B003,B004,B007,B008,B009; K/T: B001,B002 |
| ء ن ي | 1 | B001-B005 | P: B001,B002,B003,B005; K/T: B004 |
| ق د م | 1 | B001-B010 | P: B001,B002,B003,B004,B005,B006,B007,B008,B010; T: B009 |
| ح ي ي | 1 | B002,B003,B004,B006,B007,B009,B010,B011,B012,B013 | P: B002,B003,B006,B007,B009,B010,B013; K/T: B004,B011,B012 |
| ء ح د | 2 | B001-B006 | P: B001,B002,B005; K/T: B003,B004; T: B006 |
| و ث ق | 2 | B001-B004 | P: B001,B002,B003,B004 |
| ن ف س | 1 | B001-B016 | P: B001,B002,B004,B008,B009,B010,B011,B012,B013,B014,B015; K/T: B003,B005,B006,B007,B016 |
| ط م ن | 1 | B001-B003 | P: B001,B002,B003 |
| ر ج ع | 1 | B001,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014,B015 | P: B001,B003,B005,B006,B007,B009,B010,B014,B015; K/T: B004,B008,B011,B012,B013 |
| ر ض و | 2 | B001-B007 | P: B001,B002,B003,B004,B005,B006; T: B007 |
| د خ ل | 2 | B001-B010 | P: B001,B003,B004,B005,B006,B007,B008,B009,B010; K/T: B002 |
| ع ب د | 1 | B001,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012 | P: B001,B003,B004,B005,B006,B007,B008,B009,B010,B011; T: B012 |
| ج ن ن | 1 | B001,B002,B003,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014,B016,B017 | P: B001,B002,B003,B006,B007,B008,B009,B010,B011,B013,B014,B016,B017; K/T: B005,B012 |

## Candidate Synthesis Units

### S89-P2-C01: Dawn-Rupture Oath Opens a Counting Machine

- `candidate_id`: S89-P2-C01
- `ayah_range`: 89:1-5
- `seed_type`: lexical
- `seed`: 89:1 `فجر`, seeded independently from `ف ج ر B001` and `ف ج ر B002`; `B004` retained as a rival moral rupture fork.
- `generating_set`: `(E: ف ج ر B001 wide splitting and water-opening)`, `(E: ف ج ر B002 dawn light at end of night)`, `(E: ل ي ل B001 night/darkness)`, `(E: ع ش ر B001 ten-count)`, `(E: ش ف ع B001 pairing)`, `(E: و ت ر B001 odd/single)`, `(E: س ر ي B001 night travel)`.
- `selected_branches`: `ف ج ر B001,B002`; `ل ي ل B001,B002`; `ع ش ر B001,B002,B005`; `ش ف ع B001`; `و ت ر B001,B004,B005`; `س ر ي B001,B004`; `ق س م B004`; `ح ج ر B001,B002`.
- `constructed_model`: The recitation begins with a crack in darkness: an opening line of dawn after night. The image is immediately counted, paired, singled, and set in motion. The oath material acts like a temporal measuring device: night gives the enclosing medium, ten nights provide duration, pair/odd provide parity sorting, and the night when it travels makes the darkness itself a moving body.
- `freeze_point`: Freeze after 89:4, before `هل في ذلك قسم لذي حجر`.
- `predictions_at_freeze`: an oath/binding operator should appear; a receiver capable of discrimination should appear; later passage material should reactivate splitting, counting, pairing/singling, and movement through night or darkness.
- `unused_features_tested`: `ق س م`, `ح ج ر`, destructive cuts in `ج و ب`, stone `ص خ ر`, stakes `و ت د`, repeated doubles `دكا دكا` and `صفا صفا`, exclusive `أحد`, and return/entry closure.
- `corroborators`: `(C: ق س م B004 oath)`, `(C: ح ج ر B002 العقل الحاجز)`, `(C: attachment 89:1-4 oath complements)`, `(C: attachment 89:5 predication in فِي ذَٰلِكَ قَسَمٌ)`, `(C: و ت ر B004 separated succession)`, `(C: د ك ك repeated cognate accusative 89:21)`, `(C: ص ف ف repeated rank 89:22)`.
- `constraints`: `(K: ف ج ر B004 moral rupture does not govern the primary oath wording at 89:1)`, `(K: B003 sudden mass arrival lacks local participant until judgment scene and remains secondary)`, `(K: B005 generosity and B006 Fijar war-name terminate as lexical seeds)`.
- `temporal_reactivation_notes`: The opening predicts measurement. The surah later provides civilizations measured by height, comparison, lands, excess, poured punishment, then a final scene ordered in ranks and exclusive negations. Pair/odd is not merely a number theme; it becomes a perception test for one who has `حجر`.
- `rival_models`: Moral rupture model from `ف ج ر B004` links to `فساد`, `طغوا`, and social greed, but it cannot explain the temporal oath ordering as strongly as the dawn-splitting model.
- `grade`: strong
- `grade_rationale`: Strong because independent channels converge: lexical dawn/splitting, oath syntax, number/parity sequence, night movement, later repetition, and final ordering.
- `source_queries_or_rows_used`: S89 qac rows for 89:1-5; v4 rows `ف ج ر`, `ل ي ل`, `ع ش ر`, `ش ف ع`, `و ت ر`, `س ر ي`, `ق س م`, `ح ج ر`; attachments 89:1-5.

### S89-P2-C02: The Oath Requires a Containing Intellect

- `candidate_id`: S89-P2-C02
- `ayah_range`: 89:1-5
- `seed_type`: constructional
- `seed`: `هَلْ فِي ذَٰلِكَ قَسَمٌ لِّذِي حِجْرٍ`
- `generating_set`: `(E: ق س م B004 oath)`, `(E: ق س م B003 apportionment/partition)`, `(E: ح ج ر B001 prevention/enclosure)`, `(E: ح ج ر B002 عقل حاجز)`, `(E: ح ج ر B006 circular boundary)`.
- `selected_branches`: `ق س م B003,B004,B006`; `ح ج ر B001,B002,B004,B006`; plus attachment 89:5 `فِي ذَٰلِكَ` as predicative containment and `لذي حجر` as audience.
- `constructed_model`: The opening materials are not just sworn objects; they are placed inside `ذلك` and offered to a possessor of `حجر`, a faculty that fences off misreading. The image is of a mind with a boundary wall: it can hold the sequence and divide it correctly.
- `freeze_point`: Freeze at 89:5 before historical exempla begin.
- `predictions_at_freeze`: later scenes should show what happens when boundary, measure, and restraint fail; an unbounded overflow should contrast with bounded cognition.
- `unused_features_tested`: `طغوا في البلاد`, `أكثروا فيها الفساد`, `قدر عليه رزقه`, social failure to honor/feed, `دكت الأرض`, and `النفس المطمئنة`.
- `corroborators`: `(C: ط غ ي B001 crossing the limit)`, `(C: ط غ ي B002 overflowing water/force)`, `(C: ف س د B001 departure from order)`, `(C: ق د ر B001 measure and limit)`, `(C: ط م ن B001 settled after disturbance)`.
- `constraints`: `(K: ح ج ر B003 stone is present only indirectly through صخر and does not replace the primary عقل reading in 89:5)`, `(K: ح ج ر B005 lap/embrace terminates; no local role)`, `(K: ق س م B001 facial beauty and B002 heat terminate)`.
- `temporal_reactivation_notes`: `لذي حجر` becomes relevant again when the human in 89:15-16 misreads trial outcomes and when `يتذكر الإنسان` comes too late in 89:23.
- `rival_models`: A stone-enclosure model can connect to Thamud carving rock, but it is secondary because the attachment row makes `حجر` the property of the oath's recipient.
- `grade`: medium-strong
- `grade_rationale`: Strong local syntax and later contrast with overflow/restriction; less passage-scale than C01 because the image depends on conceptual extension from `حجر`.
- `source_queries_or_rows_used`: QAC 89:5; v4 `ق س م`, `ح ج ر`, `ط غ ي`, `ف س د`, `ق د ر`, `ط م ن`; attachment 89:5.

### S89-P2-C03: Monumental Power Makes Vertical Supports, Then Is Watched From Ambush

- `candidate_id`: S89-P2-C03
- `ayah_range`: 89:6-14
- `seed_type`: verified composite
- `seed`: 89:6 `ألم تر كيف فعل ربك بعاد`
- `generating_set`: `(E: ر ء ي B001 seeing)`, `(E: ر ء ي B013 alerting/inform-me construction)`, `(E: ف ع ل B001 event/action)`, `(E: ر ب ب B001 lord/master)`, `(E: ع و د B012 Aad/name and ancient association)`, `(E: ع م د B003 pillars)`, `(E: ع م د B005 height/loftiness)`, `(E: خ ل ق B002 creation)`, `(E: م ث ل B001 likeness)`, `(E: ب ل د B001 bounded lands)`.
- `selected_branches`: `ر ء ي B001,B012,B013`; `ف ع ل B001,B002`; `ر ب ب B001,B002`; `ع و د B009,B012`; `ع م د B002,B003,B005,B006,B007`; `خ ل ق B001,B002,B003`; `م ث ل B001,B005,B008,B011`; `ب ل د B001,B009`.
- `constructed_model`: The listener is made to see an enacted divine response to ancient monumental power: Aad/Iram appear as a high, supported structure without peer in the lands. The scene is vertical, comparative, and public.
- `freeze_point`: Freeze after 89:8, before Thamud, Pharaoh, excess, corruption, and punishment.
- `predictions_at_freeze`: other examples should supply different material technologies or fixings; the proud built structure should be exposed as bounded and watched; action should move from human making to divine action.
- `unused_features_tested`: `جابوا الصخر بالواد`, `ذي الأوتاد`, `طغوا في البلاد`, `فأكثروا فيها الفساد`, `فصب عليهم`, `إن ربك لبالمرصاد`.
- `corroborators`: `(C: ج و ب B001 cutting/boring)`, `(C: ص خ ر B001 hard rock)`, `(C: و د ي B005 valley conduit)`, `(C: و ت د B001 stakes)`, `(C: ر ص د B001 watching/guarding)`, `(C: ر ص د B003 place of ambush/road)`, `(C: attachment 89:14 بِالْمِرْصَادِ as predicate)`.
- `constraints`: `(K: ر ب ب B002 nurturing/repair is divine role, not a human monument role)`, `(K: خ ل ق B007 fabricated speech terminates; no speech fraud here)`, `(K: ع م د B008 sickening grief and B009 damaged hump only secondary as collapse imagery)`.
- `temporal_reactivation_notes`: The oath's `شفع/وتر` sorting reappears as three exempla: Aad, Thamud, Pharaoh. Each has a material signature: pillars, cut rock, stakes. The mind first sees height, then incision, then fixing, then excess, then a poured lash.
- `rival_models`: A pure historical-list model explains the primary reference but not the ordered material progression from support to carving to stakes to overflow.
- `grade`: strong
- `grade_rationale`: Strong because the candidate is built from local syntax and multiple independent material branches, then closed by `مرصاد`.
- `source_queries_or_rows_used`: QAC 89:6-14; v4 rows listed above; attachments 89:6-14.

### S89-P2-C04: Cutting Stone in a Valley Reactivates the Opening Split

- `candidate_id`: S89-P2-C04
- `ayah_range`: 89:1-14
- `seed_type`: lexical
- `seed`: 89:9 `جابوا الصخر بالواد`, especially `ج و ب B001`
- `generating_set`: `(E: ج و ب B001 penetrating cut/boring)`, `(E: ص خ ر B001 hard rock)`, `(E: و د ي B005 valley as watercourse/open passage)`, `(E: ف ج ر B001 wide split/opening)`, `(E: ح ج ر B003 stone/rock)`.
- `selected_branches`: `ج و ب B001,B004`; `ص خ ر B001,B004`; `و د ي B005`; `ف ج ر B001`; `ح ج ر B003,B004`; `و ت د B001`.
- `constructed_model`: The initial dawn split becomes materialized in human engineering: rock is cut in the valley. What began as divine temporal opening becomes human excavation through hard matter.
- `freeze_point`: Freeze after 89:9 before Pharaoh's stakes and moral overflow.
- `predictions_at_freeze`: a fixing or fastening image should follow; cutting through boundaries should turn into overrun/corruption; punishment may arrive as flow from above.
- `unused_features_tested`: `الأوتاد`, `طغوا`, `أكثروا`, `فساد`, `صب`, `سوط`, `مرصاد`.
- `corroborators`: `(C: و ت د B001 stake driven/fixed)`, `(C: و ت د B003 upright fixedness)`, `(C: ط غ ي B002 water/force overflowing)`, `(C: ص ب ب B001 poured from above)`, `(C: س و ط B002 lash)`.
- `constraints`: `(K: ج و ب B003 response/speech does not fit the stone-cut construction)`, `(K: ج و ب B005 garment/shield terminates)`, `(K: و د ي B001 sexual/liquid branch terminates; the local noun is valley)`.
- `temporal_reactivation_notes`: This is the first strong backward reactivation of 89:1. `فجر` had opened the morning; `جابوا الصخر` opens stone. The two openings differ in agency and moral valence.
- `rival_models`: A travel-through-lands model from `ج و ب B002` is possible but weaker because the local direct object is `الصخر`, not land.
- `grade`: medium-strong
- `grade_rationale`: Specific lexical fit for `جوب`, `صخر`, `وادي`; strong reactivation of `فجر B001`, but narrower than C03.
- `source_queries_or_rows_used`: QAC 89:1, 89:9-14; v4 `ف ج ر`, `ج و ب`, `ص خ ر`, `و د ي`, `و ت د`, `ط غ ي`, `ص ب ب`, `س و ط`; attachments 89:9.

### S89-P2-C05: Overflow in the Lands Produces Poured Punishment

- `candidate_id`: S89-P2-C05
- `ayah_range`: 89:11-14
- `seed_type`: lexical
- `seed`: 89:11 `طغوا في البلاد`, seeded from `ط غ ي B001` and `ط غ ي B002`
- `generating_set`: `(E: ط غ ي B001 crossing limit in rebellion)`, `(E: ط غ ي B002 overflowing water/force)`, `(E: ب ل د B001 bounded land)`, `(E: ك ث ر B001 increasing)`, `(E: ف س د B001 corruption/departure from order)`, `(E: ص ب ب B001 pouring from above)`, `(E: س و ط B002 whip/lash)`, `(E: ع ذ ب B005 punishment/pain)`.
- `selected_branches`: `ط غ ي B001,B002,B003,B005`; `ب ل د B001,B009,B010`; `ك ث ر B001,B002,B005`; `ف س د B001`; `ص ب ب B001,B002,B006,B010`; `س و ط B001,B002`; `ع ذ ب B003,B005,B006`; `ر ص د B001,B003`.
- `constructed_model`: Bounded lands are exceeded by rebellious overflow. The excess multiplies corruption inside the domain. The response arrives as a downward pour: a lash of punishment.
- `freeze_point`: Freeze at 89:13 before `إن ربك لبالمرصاد`.
- `predictions_at_freeze`: a watcher or prepared interception point should close the block; the punishment should not be random but timed and positioned.
- `unused_features_tested`: `رصد` branches, `ربك` repetition, `علىهم` target attachment, `سوط عذاب` idafa.
- `corroborators`: `(C: ر ص د B001 ترقب وحراسة)`, `(C: ر ص د B003 موضع الرصد والطريق)`, `(C: attachment 89:13 علىهم affected target)`, `(C: attachment 89:13 سوط direct object of صب)`, `(C: attachment 89:14 بِالمرصاد predicate)`.
- `constraints`: `(K: ع ذب B001 sweet water reverses the local meaning and is only a weak contrast)`, `(K: س وط B004 soup/mixture terminates)`, `(K: ك ثر B006 palm pith terminates)`.
- `temporal_reactivation_notes`: The opening's ordered count is now answered by disordered increase: `أكثروا`. The measure implied by `حجر` fails in the lands and is replaced by surveillance from `مرصاد`.
- `rival_models`: A purely watery flood image from `طغي B002 + صب B001` is vivid but secondary; the primary syntax says rebellion and corruption.
- `grade`: strong
- `grade_rationale`: Multiple exact local words fill roles: domain, overflow, multiplication, corruption, downward force, lash, and ambush.
- `source_queries_or_rows_used`: QAC 89:11-14; v4 listed branches; attachments 89:11-14.

### S89-P2-C06: Trial Is a Test, Not a Status Label

- `candidate_id`: S89-P2-C06
- `ayah_range`: 89:15-17
- `seed_type`: constructional
- `seed`: paired conditional frame `فأما الإنسان إذا ما ابتلاه ربه... وأما إذا ما ابتلاه...`
- `generating_set`: `(E: ء ن س B001 human appearing)`, `(E: ب ل و B002 test/revealing real state)`, `(E: ر ب ب B001 lord/master)`, `(E: ر ب ب B002 training/bringing to completion)`, `(E: ك ر م B001 honor/generosity)`, `(E: ن ع م B001 blessing/good condition)`, `(E: ق د ر B004 constricting provision)`, `(E: ر ز ق B001 apportioned gift)`, `(E: ه و ن B003 humiliation)`, `(E: ق و ل B001 utterance)`.
- `selected_branches`: `ء ن س B001,B002,B003,B006`; `ب ل و B001,B002,B003,B004,B007,B009`; `ر ب ب B001,B002`; `ك ر م B001,B006,B009,B010`; `ن ع م B001,B002,B010,B013`; `ق د ر B001,B004,B005,B006`; `ر ز ق B001,B002,B003,B004,B006`; `ه و ن B001,B002,B003`; `ق و ل B001,B011,B012,B013`.
- `constructed_model`: The human is put through two forms of disclosure: expansion through honor/blessing and contraction through measured provision. In both, the human converts a test into a status label by saying "my Lord honored me" or "humiliated me."
- `freeze_point`: Freeze after the two quoted sayings in 89:15-16, before `كلا بل`.
- `predictions_at_freeze`: correction should come; the real criterion should involve response to vulnerable others and distribution of goods, not the felt state of expansion or constriction.
- `unused_features_tested`: `كلا بل`, `لا تكرمون اليتيم`, `ولا تحاضون على طعام المسكين`, `تأكلون التراث`, `تحبون المال`.
- `corroborators`: `(C: ك ر م reactivated at 89:17 as failed honoring of orphan)`, `(C: ي ت م B001 orphan cut off from support)`, `(C: ح ض ض B001 urging)`, `(C: ط ع م B002 feeding another)`, `(C: س ك ن B006 poverty/weakness)`, `(C: ء ك ل B004 consuming wealth)`, `(C: و ر ث B001 inherited transfer)`, `(C: ح ب ب B002 heart-attachment)`, `(C: م و ل B001 wealth)`, `(C: ج م م B001 heap/fullness)`.
- `constraints`: `(K: ن ع م B005 livestock and B006 ostrich branches do not govern the trial image)`, `(K: ه و ن B001 gentleness is a rival branch but local form أهانني selects humiliation)`, `(K: ب ل و B006 response-particle branch terminates)`.
- `temporal_reactivation_notes`: `كرم` first appears as divine action and quoted interpretation, then reappears negated in social action. This is a precise reactivation: the human's honor-claim is tested by whether the human honors the orphan.
- `rival_models`: A prosperity/poverty binary model is weaker because `ابتلاه` frames both states as test, and `كلا` rejects the status inference.
- `grade`: strong
- `grade_rationale`: Strong constructional symmetry and exact lexical reactivation of `كرم`; later social verses supply independent test criteria.
- `source_queries_or_rows_used`: QAC 89:15-20; v4 listed branches; attachments 89:15-20.

### S89-P2-C07: Social Failure as Failed Joining, Feeding, and Proper Transfer

- `candidate_id`: S89-P2-C07
- `ayah_range`: 89:17-20
- `seed_type`: lexical/constructional
- `seed`: 89:17 `لا تكرمون اليتيم`
- `generating_set`: `(E: ك ر م B001 honor/generosity)`, `(E: ي ت م B001 child cut off from father/support)`, `(E: ي ت م B002 solitary/unmatched thing)`, `(E: ح ض ض B001 urging)`, `(E: ط ع م B002 feeding another)`, `(E: س ك ن B006 miskin/f poverty and weakness)`, `(E: ء ك ل B004 taking/consuming wealth)`, `(E: و ر ث B001 inheritance transfer)`, `(E: ل م م B001 gathering the scattered)`, `(E: ح ب ب B002 love fixed in heart)`, `(E: م و ل B001 wealth)`, `(E: ج م م B001 accumulated heap)`.
- `selected_branches`: `ك ر م B001,B008,B009,B010`; `ي ت م B001-B005`; `ح ض ض B001,B002`; `ط ع م B001,B002,B004,B008,B010,B011,B012`; `س ك ن B001,B002,B003,B004,B006,B007,B008,B009,B010`; `ء ك ل B001,B003,B004,B005,B006,B009,B010,B012,B013`; `و ر ث B001,B002,B003,B005`; `ل م م B001,B002,B003,B004,B006,B007,B008`; `ح ب ب B001,B002,B004,B006,B007,B008,B011`; `م و ل B001`; `ج م م B001-B009`.
- `constructed_model`: The social section shows misdirected aggregation. What should be joined is the cut-off orphan and the needy person's food network. Instead, inheritance is gathered and consumed, while love attaches to piled wealth.
- `freeze_point`: Freeze after 89:20, before the earth is crushed.
- `predictions_at_freeze`: the false heap should be undone; accumulation should be answered by compression, breaking, or leveling; remembered value should arrive too late.
- `unused_features_tested`: `دكت الأرض دكا دكا`, `صفا صفا`, `يتذكر الإنسان`, `قدمت لحياتي`, `لا يعذب...ولا يوثق`, `ارجعي`.
- `corroborators`: `(C: د ك ك B001 pounding/leveling)`, `(C: د ك ك B008 crowding/pressing on a thing)`, `(C: ص ف ف B001 ranks/order)`, `(C: ذ ك ر B003 recollection after neglect)`, `(C: ق د م B004 forward preparation)`.
- `constraints`: `(K: ط ع م B013 mouth-to-mouth contact terminates)`, `(K: ح بب B009 teeth arrangement terminates)`, `(K: ج مم B004 skull/hair is only remote secondary; not used)`, `(K: ل مم B010 place-name terminates)`.
- `temporal_reactivation_notes`: The repeated second-person plurals turn the trial from private feeling into collective practice. `كَرَم` is reactivated as the decisive missing social act.
- `rival_models`: A general greed model is valid but too broad; the stronger model is failed distribution/attachment: orphan unsupported, poor unfed, inheritance gathered, wealth loved as a heap.
- `grade`: strong
- `grade_rationale`: Dense local syntax, repeated negated actions, and exact branches for cutting-off, urging, feeding, consuming, inheritance, gathering, love, wealth, and heap.
- `source_queries_or_rows_used`: QAC 89:17-20; v4 listed roots; attachments 89:17-20.

### S89-P2-C08: The Heap Is Answered by Crushing and Rank Ordering

- `candidate_id`: S89-P2-C08
- `ayah_range`: 89:20-23
- `seed_type`: temporal/acoustic
- `seed`: repetitions `دكا دكا`, `صفا صفا`, `يومئذ...يومئذ`
- `generating_set`: `(E: ج م م B001 accumulation until fullness)`, `(E: د ك ك B001 pounding/humbling to level)`, `(E: د ك ك B002 flattening/low surface)`, `(E: ء ر ض B001 lower earth)`, `(E: ج ي ء B001 coming)`, `(E: ج ي ء B004 bringing a thing)`, `(E: ص ف ف B001 rows/ranks)`, `(E: ذ ك ر B003 remembering after forgetting)`, `(E: ذ ك ر B009 reminder)`.
- `selected_branches`: `ج م م B001`; `د ك ك B001,B002,B003,B006,B007,B008,B009`; `ء ر ض B001,B002,B006,B008,B010,B011,B012`; `ج ي ء B001,B004,B005`; `م ل ك B001,B003,B005,B006,B008`; `ص ف ف B001,B005,B007`; `ذ ك ر B003,B004,B007,B008,B009`; `ء ن س B001,B002,B005`; `ء ن ي B001,B002,B003,B005`.
- `constructed_model`: Human accumulation is met by a scene that pulverizes the lower ground and reorders presence into ranks. What was loved as a heap becomes a flattened field, then a ranked arrival, then forced memory.
- `freeze_point`: Freeze after 89:23 `يتذكر الإنسان`.
- `predictions_at_freeze`: memory should be acknowledged as late or inaccessible; speech should express regret; preparation/forwarding should become the missing action.
- `unused_features_tested`: `وأنى له الذكرى`, `يا ليتني قدمت لحياتي`.
- `corroborators`: `(C: ء ن ي B005 أنى as how/from where question)`, `(C: ء ن ي B001 delay/slowness)`, `(C: ء ن ي B003 arrival of time/maturity)`, `(C: ق و ل B001 utterance)`, `(C: ق د م B004 forward placing)`, `(C: ح ي ي B003 life)`, `(C: ح ي ي B013 life as benefit/good)`.
- `constraints`: `(K: م ل ك v4 lacks a distinct angel branch in this export, so الملك is used only as local surface/attachment evidence, not as a branch-generated angel image)`, `(K: ج يء duplicate branch rows were not double-counted as independent corroboration)`, `(K: ءرض B010 termite branch is remote; only secondary as destructive eating, not generating)`.
- `temporal_reactivation_notes`: Repetition converts accumulation into ordered destruction. `يومئذ` doubles the temporal pressure: the moment arrives, then the same moment is heard again when memory opens.
- `rival_models`: A pure eschatological arrival model is primary at translation level, but the secondary simulation adds the passage's pressure geometry: heap -> crush -> ranks -> memory.
- `grade`: medium-strong
- `grade_rationale`: Strong repetitive/morphosyntactic evidence; some lexical branches are broad and the angel word cannot be branch-supported from the local v4 export.
- `source_queries_or_rows_used`: QAC 89:20-24; v4 listed roots; attachments 89:21-24.

### S89-P2-C09: Late Memory Produces a Wish to Have Sent Forward for Life

- `candidate_id`: S89-P2-C09
- `ayah_range`: 89:23-24
- `seed_type`: lexical
- `seed`: 89:23 `يتذكر الإنسان`
- `generating_set`: `(E: ذ ك ر B003 recollection after forgetting)`, `(E: ذ ك ر B009 reminder)`, `(E: ء ن س B001 human)`, `(E: ء ن ي B005 how/from where)`, `(E: ء ن ي B001 delay)`, `(E: ق و ل B001 utterance)`, `(E: ق د م B004 sending/placing forward)`, `(E: ق د م B002 prior credit/standing)`, `(E: ح ي ي B003 life)`, `(E: ح ي ي B013 life as benefit/preservation)`.
- `selected_branches`: `ذ ك ر B003,B004,B007,B008,B009`; `ء ن س B001,B002,B005,B006`; `ء ن ي B001,B002,B003,B005`; `ق و ل B001,B005,B011,B012,B013`; `ق د م B001-B008,B010`; `ح ي ي B002,B003,B006,B007,B009,B010,B013`.
- `constructed_model`: The human who failed to read trial in time now remembers when memory no longer functions as preparation. Speech becomes a wish: if only something had been put ahead for life.
- `freeze_point`: Freeze at 89:24 before exclusive punishment/binding.
- `predictions_at_freeze`: the next lines should close human agency and deny substitution or shared agency; no one else will perform the decisive act.
- `unused_features_tested`: `لا يعذب عذابه أحد`, `ولا يوثق وثاقه أحد`.
- `corroborators`: `(C: ء ح د B002 exhaustive negation)`, `(C: ع ذ ب B005 punishment)`, `(C: و ث ق B003 binding)`, `(C: attachment 89:25-26 delayed أحد under negation)`.
- `constraints`: `(K: ق د م B008 adze/nutting tool and B009 place-name terminate)`, `(K: ح يي B004 snake and B011 sexual organ terminate)`, `(K: ذ كر B001 male branch not used)`.
- `temporal_reactivation_notes`: The opening addressed `ذي حجر`; by 89:23 the human has memory but not effective `ذكرى`. The cognitive faculty arrives after the trial sequence has closed.
- `rival_models`: A pure regret model is valid; this candidate specifically preserves the temporal failure: remembrance after the moment when forwarding was possible.
- `grade`: medium-strong
- `grade_rationale`: Exact local lexical sequence from remembering to saying to forwarding to life; strong temporal fit.
- `source_queries_or_rows_used`: QAC 89:23-26; v4 listed roots; attachments 89:23-26.

### S89-P2-C10: Exclusive Punishment and Binding Close the Human's Transfer Fantasy

- `candidate_id`: S89-P2-C10
- `ayah_range`: 89:25-26
- `seed_type`: morphosyntactic
- `seed`: parallel negations `لا يعذب عذابه أحد / ولا يوثق وثاقه أحد`
- `generating_set`: `(E: ء ح د B002 exhaustive negation)`, `(E: ع ذ ب B005 punishment/pain)`, `(E: ع ذ ب B006 dangling lash/end)`, `(E: و ث ق B003 binding/rope)`, `(E: و ث ق B002 securing)`, `(E: و ث ق B004 covenant/confirmed bond)`.
- `selected_branches`: `ء ح د B001,B002,B005`; `ع ذ ب B003,B005,B006`; `و ث ق B001-B004`.
- `constructed_model`: After the wish to have sent forward, agency is closed by exhaustive negation. No one performs that punishment and no one binds that binding. The cognate accusatives turn action into uniquely specified act.
- `freeze_point`: Freeze after 89:26 before the vocative to the tranquil self.
- `predictions_at_freeze`: a contrasting addressee should appear: one not caught in late regret and binding, but settled and able to return.
- `unused_features_tested`: `يا أيتها النفس المطمئنة`, `ارجعي`, `راضية مرضية`, `ادخلي`.
- `corroborators`: `(C: ن ف س B011 life/soul)`, `(C: ط م ن B001 settled after disturbance)`, `(C: ر ج ع B001 return)`, `(C: ر ض و B003 mutual satisfaction)`, `(C: د خ ل B001 entry)`.
- `constraints`: `(K: ء ح د B006 Mount Uhud terminates)`, `(K: ع ذب B001 sweetness is a contrast only)`, `(K: وثق B001 trust is secondary; local Form IV/cognate accusative selects binding)`.
- `temporal_reactivation_notes`: The two `أحد` occurrences are not numerical decoration; they close transfer. The earlier social failures involved others who should have been honored/fed; now no other can absorb or perform the final act.
- `rival_models`: Legal-covenant model from `وثق B004` is secondary but helps explain why binding is not just physical; it is a final fastening of consequence.
- `grade`: medium-strong
- `grade_rationale`: Strong parallel morphology and repeated exhaustive negation, narrower lexical field.
- `source_queries_or_rows_used`: QAC 89:25-30; v4 `ء ح د`, `ع ذب`, `و ثق`, `ن فس`, `طمن`, `رجع`, `رضو`, `دخل`; attachments 89:25-30.

### S89-P2-C11: The Tranquil Self Returns Into Belonging and Gardened Cover

- `candidate_id`: S89-P2-C11
- `ayah_range`: 89:27-30
- `seed_type`: lexical/constructional
- `seed`: 89:27 `النفس المطمئنة`
- `generating_set`: `(E: ن ف س B011 living soul)`, `(E: ن ف س B013 inward mind/intent)`, `(E: ن ف س B001 breath)`, `(E: ط م ن B001 stillness after disturbance)`, `(E: ر ج ع B001 return to what was)`, `(E: ر ب ب B001 Lord/master)`, `(E: ر ب ب B002 nurturer/completer)`, `(E: ر ض و B001 satisfaction)`, `(E: ر ض و B003 mutual satisfaction)`, `(E: د خ ل B001 entering inside)`, `(E: ع ب د B003 worshipful servitude)`, `(E: ج ن ن B003 garden enclosed by trees)`.
- `selected_branches`: `ن ف س B001,B002,B004,B008,B009,B010,B011,B012,B013,B014,B015`; `ط م ن B001-B003`; `ر ج ع B001,B003,B005,B006,B007,B009,B010,B014,B015`; `ر ب ب B001,B002,B007,B008,B011,B016`; `ر ض و B001-B006`; `د خ ل B001,B003-B010`; `ع ب د B001,B003-B011`; `ج ن ن B001,B002,B003,B006-B011,B013,B014,B016,B017`.
- `constructed_model`: The close reverses the prior constriction. The addressed self is settled after disturbance, called to return to its Lord, mutually satisfied, then moved by two entries: into servants and into garden. The image has breath/self, return, acceptance, interiority, collective belonging, and sheltered growth.
- `freeze_point`: Freeze at 89:30, the passage closure.
- `predictions_at_freeze`: passage should close because all earlier open roles are resolved: trial misreading answered by satisfaction, false accumulation answered by entry into rightful belonging, night/dawn movement answered by gardened covering after return.
- `unused_features_tested`: backward replay across `حجر`, `قدر`, `رزق`, `أكل التراث`, `دك`, `صف`, `وثاق`.
- `corroborators`: `(C: د خ ل B003 inward/secret resolves inner self)`, `(C: ج ن ن B001 covering and shelter)`, `(C: ج ن ن B010 hidden heart)`, `(C: ع ب د B001 slave/servant belonging)`, `(C: ع ب د B006 honored/served branch reverses failed تكريم)`, `(C: opening-context ر ح م B001 mercy as divine-source corroboration only)`, `(C: opening-context ء ل ه B001 worshipped/divine source)`.
- `constraints`: `(K: ج نن B012 snake terminates)`, `(K: ع بد B012 perfume pestle terminates)`, `(K: د خل B002 marital euphemism terminates)`, `(K: نفس B016 maysir arrow terminates)`.
- `temporal_reactivation_notes`: The final imperatives complete the surah's motion. Night travels; civilizations exceed; provision constricts; earth is crushed; memory comes too late; the tranquil self is the first figure allowed an ordered return and entry.
- `rival_models`: A purely garden-reward model is primary contextually. The secondary simulation is a return from disturbed breath and mismeasured possession into settled, enclosed belonging.
- `grade`: strong
- `grade_rationale`: Exact closure of multiple earlier activations: trial, constriction, inner self, return, satisfaction, entering, servants, garden/cover.
- `source_queries_or_rows_used`: QAC 89:27-30; v4 listed roots; attachments 89:27-30; basmala opening context only for mercy/divine source.

## Constructional and Temporal Seeds

These seed passes were initiated separately from lexical branches. They either converge with the candidates above or terminate.

1. Oath-chain `وَالفجر / وليال / والشفع / والوتر / والليل`: productive. Generates C01 through parallel oath complements and ordered temporal exposure.
2. Adjective `ليال عشر`: productive. Counted duration joins night as a measured interval; constrains remote `عشر` branches.
3. Pair `الشفع والوتر`: productive. Generates parity sorting and later reactivates as paired/unique negation.
4. Conditional `إذا يسر`: productive. Night is not static; it moves. Joins C01.
5. Predication `في ذلك قسم`: productive. The oath objects are contained in a demonstrative packet. Joins C02.
6. `لذي حجر`: productive. Constructs audience with bounded/discriminating mind. Joins C02.
7. `ألم تر كيف فعل ربك`: productive. Auditory recitation demands vision of manner. Joins C03.
8. Relative exempla sequence `عاد / ثمود / فرعون`: productive. Gives three public cases with material signatures. Joins C03.
9. Idafa `ذات العماد`: productive. Possessed pillars/support. Joins C03.
10. Passive comparison `لم يخلق مثلها`: productive. Unmatched creation/comparison. Joins C03.
11. Direct object `جابوا الصخر`: productive. Forces cutting into hard object rather than generic travel. Joins C04.
12. `بِالواد`: productive as locative conduit; joins C04.
13. `ذي الأوتاد`: productive. Possessed fixing/stakes; joins C03/C04.
14. `طغوا في البلاد`: productive. Overflow inside bounded domain; joins C05.
15. `فأكثروا فيها الفساد`: productive. Excess multiplied inside the same domain; joins C05.
16. `فصب عليهم ربك سوط عذاب`: productive. Downward poured punishment with affected target; joins C05.
17. Predicate `لبالمرصاد`: productive. Watch/ambush closes the historical block; joins C05.
18. Paired trial frame `فأما...وأما`: productive. Generates C06.
19. Quoted claims `ربي أكرمن / ربي أهانن`: productive. Human converts test into status label; joins C06.
20. Correction `كلا بل`: productive non-branch discourse constraint; rejects the human inference.
21. Negations `لا تكرمون / لا تحاضون`: productive. Moves criterion to social action; joins C07.
22. Cognate accusative `أكلا لما`: productive. Intensifies gathering/consuming; joins C07.
23. Cognate accusative `حبا جما`: productive. Intensifies attachment to heap; joins C07.
24. Repetition `دكا دكا`: productive. Acoustic crushing/leveling; joins C08.
25. Repetition `صفا صفا`: productive. Ordered rows answer heap/crushing; joins C08.
26. Double `يومئذ`: productive. Time pressure and delayed memory; joins C08/C09.
27. `وأنى له الذكرى`: productive. Interrogative impossibility/delay; joins C09.
28. Wish formula `يا ليتني`: productive. Speech of too-late desire; joins C09.
29. Parallel exclusive negations with cognate accusatives: productive. Generates C10.
30. Vocative `يا أيتها النفس`: productive. New addressee after closed punishment; joins C11.
31. Circumstantial pair `راضية مرضية`: productive. Mutual satisfaction; joins C11.
32. Imperative pair `ادخلي...وادخلي`: productive. Double entry closes the passage; joins C11.

## Terminated Avalanche Notes

The following branches were initiated as seeds but did not produce a retained model beyond minor local constraint:

- Proper-name or place-name branches: `ء ح د B006`, `ق د م B009`, `ل م م B010`, most `ر ض و B007`.
- Animal/body-specific branches without local role: `و ت د B004`, `ن ع م B006`, `ح ي ي B004`, `ح ي ي B011`, `ج ن ن B012`, `ن ف س B016`.
- Tool/object branches without local syntax: `ق و ل B008`, `ق د م B008`, `ه و ن B004`, `ع ب د B012`, `ج و ب B005`, `ص خ ر B002`, `ص خ ر B003`.
- Remote material branches used only as constraints: `ح ب ب B009`, `ج م م B004`, `ط ع م B013`, `ع ش ر B017`, `ر ء ي B007-B010`.
- Basmala roots were never used as seeds. `ر ح م B001`, `ء ل ه B001/B002`, and `س م و B005` only corroborate the divine-source/opening-context closure in C11 when needed.

## Image Packet Catalog

### IMG-S89-01: Measured Dawn Oath

- Starting seed: `ف ج ر B001/B002`
- Complete image: darkness splits into dawn, then gets counted, paired, singled, and set moving.
- Passage-order assembly: 89:1 dawn -> 89:2 ten nights -> 89:3 pair/odd -> 89:4 night travels -> 89:5 oath to bounded mind.
- Participants and roles: dawn opening, night medium, count, parity, moving darkness, oath receiver.
- Operation / mechanism: temporal sorting and discrimination.
- Direction / force / medium: from night enclosure toward dawn opening.
- Temporal development: opening oath later reactivated by cutting, crushing, ranks, and return.
- Outcome / closure: discriminating mind is required before exempla.
- Exact branch constituents: `ف ج ر B001,B002`; `ل ي ل B001`; `ع ش ر B001`; `ش ف ع B001`; `و ت ر B001`; `س ر ي B001`; `ق س م B004`; `ح ج ر B002`.
- Unfilled roles: none.
- Status: COMPLETE

### IMG-S89-02: Bounded Lands Overrun and Watched

- Starting seed: `ط غ ي B001/B002`
- Complete image: bounded lands overflow with multiplied corruption until a watched ambush-position releases punishment.
- Passage-order assembly: monuments -> cut rock -> stakes -> overflow -> corruption -> poured lash -> ambush.
- Participants and roles: civilizations, lands, excess, corruption, Lord, lash, ambush point.
- Operation / mechanism: limit violation answered by positioned surveillance and downward force.
- Direction / force / medium: overflow outward, punishment downward.
- Temporal development: human power expands before divine response descends.
- Outcome / closure: `إن ربك لبالمرصاد`.
- Exact branch constituents: `ب ل د B001`; `ط غ ي B001,B002`; `ك ثر B001`; `ف سد B001`; `صبب B001`; `سوط B002`; `عذب B005`; `رصد B001,B003`.
- Unfilled roles: none.
- Status: COMPLETE

### IMG-S89-03: Trial Misread as Honor/Humiliation

- Starting seed: `ب ل و B002`
- Complete image: test conditions reveal human misclassification; expansion and constriction are mistaken for honor and humiliation.
- Passage-order assembly: test by honor/blessing -> speech claim -> test by constrained provision -> speech claim -> rejection -> social criterion.
- Participants and roles: human, Lord, test, honor, blessing, provision, speech, correction, orphan, poor.
- Operation / mechanism: disclosure through alternating states.
- Direction / force / medium: expansion/constriction of provision.
- Temporal development: private interpretation is corrected by public social action.
- Outcome / closure: false inference defeated by `كلا بل`.
- Exact branch constituents: `ء ن س B001`; `ب لو B002`; `ربب B001,B002`; `كرم B001`; `نعم B001`; `قدر B004`; `رزق B001`; `هون B003`; `قول B001`; `يتم B001`; `حضض B001`; `طعم B002`; `سكن B006`.
- Unfilled roles: none.
- Status: COMPLETE

### IMG-S89-04: Heap, Crushing, Ranks, Memory

- Starting seed: `ج م م B001`
- Complete image: loved heap meets crushing repetition and rank repetition, then memory opens too late.
- Passage-order assembly: love of wealth as heap -> earth crushed -> Lord/angelic rows -> Hell brought -> human remembers -> wish to have sent forward.
- Participants and roles: heap, earth, ranks, brought object, human, memory, prior preparation.
- Operation / mechanism: accumulated value is flattened and reordered.
- Direction / force / medium: compression downward, ordering in lines.
- Temporal development: accumulated present is overturned by the day of recollection.
- Outcome / closure: regret speech.
- Exact branch constituents: `جمم B001`; `دكك B001,B002`; `أرض B001`; `جيء B001,B004`; `صفف B001`; `ذكر B003,B009`; `قدم B004`; `حيي B003,B013`.
- Unfilled roles: none.
- Status: COMPLETE

### IMG-S89-05: Tranquil Return and Double Entry

- Starting seed: `ط م ن B001`
- Complete image: a self settled after disturbance returns to its Lord, mutually satisfied, then enters servants and gardened shelter.
- Passage-order assembly: tranquil self -> return -> satisfaction pair -> enter servants -> enter garden.
- Participants and roles: self, Lord, satisfaction, servants, garden.
- Operation / mechanism: return and inclusion.
- Direction / force / medium: inward entry after return.
- Temporal development: closes all prior movement: night travels, humans overrun, earth crushed, self returns.
- Outcome / closure: `وادخلي جنتي`.
- Exact branch constituents: `نفس B011,B013`; `طمن B001`; `رجع B001`; `ربب B001,B002`; `رضو B001,B003`; `دخل B001`; `عبد B003`; `جنن B001,B003`.
- Unfilled roles: none.
- Status: COMPLETE

## Exhaustiveness Check After File Creation

This file covers:

- All 64 rooted passage roots from S89.
- All accepted branch IDs returned for those roots in the local v4 export, with productive, constraining, or terminated outcome.
- Repeated roots as occurrence-by-branch seeds in the audit count: 825 lexical occurrence-by-branch seed passes, excluding `ك ي ف`, which had no accepted v4 branch row and was retained only as a constructional interrogative seed.
- All major constructional seeds visible in the attachment rows for 89:1-30.
- Opening basmala context only as non-generating corroboration.

No Stage 2 work is performed here.
