# S92 Stage 1 Pass 2: Temporally Conditioned Reactivation

Assigned passage: S92, al-Layl. Sacred Arabic text source: `resources/quran/surah_92.json`.

## Root Cause of Pass 1 Limitation

Pass 1 compressed the branch sweep too early. I had read the passage roots and the main branch dossiers, but I grouped remote, local-only, and failed singleton seeds into broad notes instead of recording an explicit occurrence-by-branch outcome for every eligible rooted word. That caused the apparent limitation: the early high-yield words received deep visible treatment, while many weak or terminating branches were only implicit in the held context.

This Pass 2 restarts from the first rooted word, `ٱلَّيْلِ` in 92:1. For S92 there are 48 rooted word occurrences, 41 distinct passage roots, and 358 occurrence-by-branch lexical seed passes after repeated rooted occurrences are counted. The SQLite files named in the prompt, `resources/qac.sqlite` and `resources/furuq_v4.sqlite`, are present in this checkout but zero bytes; the available local v1 resource copies used here were `resources/qac_root_ayah.tsv`, `resources/v4_branches.tsv`, `resources/attachments.tsv`, and `resources/quran/surah_92.json`. No translation was used as evidence.

## Passage Exposure and First Rooted Sequence

Opening context: `بسم الله الرحمن الرحيم` is treated only as opening-context evidence. Its roots may corroborate naming, divine source, mercy, or source authority, but they do not initiate seeds.

Passage rooted sequence by activation block:

- 92:1-4: `ل ي ل`, `غ ش و`, `ن ه ر`, `ج ل و`, `خ ل ق`, `ذ ك ر`, `ء ن ث`, `س ع ي`, `ش ت ت`.
- 92:5-10: `ع ط و`, `و ق ي`, `ص د ق`, `ح س ن`, `ي س ر`, `ي س ر`, `ب خ ل`, `غ ن ي`, `ك ذ ب`, `ح س ن`, `ي س ر`, `ع س ر`.
- 92:11-13: `غ ن ي`, `م و ل`, `ر د ي`, `ه د ي`, `ء خ ر`, `ء و ل`.
- 92:14-17: `ن ذ ر`, `ن و ر`, `ل ظ ي`, `ص ل ي`, `ش ق و`, `ك ذ ب`, `و ل ي`, `ج ن ب`, `و ق ي`.
- 92:18-21: `ء ت ي`, `م و ل`, `ز ك و`, `ء ح د`, `ع ن د`, `ن ع م`, `ج ز ي`, `ب غ ي`, `و ج ه`, `ر ب ب`, `ع ل و`, `ر ض و`.

The first temporal hearing produces a cover/reveal polarity, then a created male/female polarity, then the abstract statement that human striving is scattered. The subsequent conditional pairs test that opening structure: giving/protecting/verifying leads to facilitation toward ease; withholding/self-sufficing/denying leads to facilitation toward difficulty. Later fire, avoidance, purification, non-repayment, seeking the Face, and final satisfaction reactivate the same polarity with outcome, direction, and closure.

## Exhaustive Lexical Seed Ledger

Each accepted v4 branch was initiated as a seed at each occurrence of its root. `P` means at least one occurrence-by-branch pass generated or expanded a retained image below. `L` means local-only image retained in a constructional or minor role. `K` means the branch mainly constrained or narrowed another image after freeze. `T` means the branch terminated after no passage-local role completion beyond generic association. Repeated roots were tested at each occurrence with different temporal state; the row gives the branch status across those occurrence passes.

| root | occ | branches | branch-pass outcome |
| --- | ---: | --- | --- |
| ل ي ل | 1 | B001,B002,B003,B004 | P: B001,B002; K/T: B003; T: B004 |
| غ ش و | 1 | B001,B002,B003,B004,B005,B006,B007 | P: B001,B002; L: B003,B005; K/T: B004,B006,B007 |
| ن ه ر | 1 | B001,B002,B003,B004,B006,B007,B008 | P: B002,B003; L: B001; K/T: B004; T: B006,B007,B008 |
| ج ل و | 1 | B001,B002,B003,B004,B005,B006,B007,B008,B009 | P: B001,B007; L: B002,B006,B008; K/T: B003,B004,B005,B009 |
| خ ل ق | 1 | B001,B002,B003,B004,B005,B007,B008,B009,B010,B011,B012 | P: B001,B002,B003,B004,B005; K/T: B007,B008,B009,B011,B012; T: B010 |
| ذ ك ر | 1 | B001,B002,B003,B004,B007,B008,B009 | P: B001; L: B002,B003,B004,B009; K/T: B007,B008 |
| ء ن ث | 1 | B001,B002,B003,B004,B005,B007,B008 | P: B001; L: B002,B004,B005; K/T: B003,B007,B008 |
| س ع ي | 1 | B001,B002,B003,B004,B005,B006,B007,B008 | P: B001,B002; L: B006; K/T: B003,B004,B005,B008; T: B007 |
| ش ت ت | 1 | B001,B002,B003 | P: B001,B003; K/T: B002 |
| ع ط و | 1 | B001,B002,B003,B004,B005,B006,B007 | P: B002; L: B001,B003,B006; K/T: B004,B005,B007 |
| و ق ي | 2 | B001,B002,B003,B004,B005 | P: B001,B002; L: B003; T: B004,B005 |
| ص د ق | 1 | B001,B002,B003,B004,B005,B006,B007 | P: B001,B003,B004; L: B002,B005,B006; K/T: B007 |
| ح س ن | 2 | B001,B002,B004,B005 | P: B001,B002; L: B005; T: B004 |
| ي س ر | 3 | B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011 | P: B001,B005; L: B002,B003,B006; K/T: B004,B007,B008,B009,B011; T: B010 |
| ب خ ل | 1 | B001 | P: B001 |
| غ ن ي | 2 | B001,B002,B003,B004,B005,B006 | P: B001,B002; L: B003,B004; K/T: B005,B006 |
| ك ذ ب | 2 | B001,B002,B003,B004,B005,B006,B007,B008,B009 | P: B001,B002; L: B004,B005,B006,B007,B008; K/T: B003,B009 |
| ع س ر | 1 | B001,B002,B003,B004,B005,B006,B008,B009,B010,B011,B012,B013 | P: B001,B004; L: B002,B003,B005,B011; K/T: B006,B008,B009,B010,B013; T: B012 |
| م و ل | 2 | B001 | P: B001 |
| ر د ي | 1 | B001,B002,B003,B004,B005 | P: B003; L: B001,B002,B004,B005 |
| ه د ي | 1 | B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011 | P: B001,B002,B003; L: B004,B005,B010; K/T: B006,B007,B008,B009,B011 |
| ء خ ر | 1 | B001,B002,B003 | P: B001,B002; L: B003 |
| ء و ل | 1 | B001,B002,B003,B004,B005,B007,B008,B009,B010 | P: B001,B002,B004; L: B007,B008; K/T: B003,B005,B009,B010 |
| ن ذ ر | 1 | B001,B002,B003 | P: B001; L: B002; T: B003 |
| ن و ر | 1 | B001,B002,B004,B005,B006,B007,B008,B009 | P: B002; L: B001,B005,B006,B007,B008; K/T: B004,B009 |
| ل ظ ي | 1 | B001,B002,B003,B004 | P: B001,B002; L: B003,B004 |
| ص ل ي | 1 | B001,B002,B003,B004,B005,B006,B007,B008,B009,B010 | P: B003; L: B004,B007; K/T: B001,B002,B005,B006,B008,B009,B010 |
| ش ق و | 1 | B002,B003,B004 | P: B002; L: B003,B004 |
| و ل ي | 1 | B001,B002,B003,B004,B005,B006,B007,B008,B010,B011,B012,B013,B014,B015,B016 | P: B006,B007; L: B001,B002,B003,B004,B008,B012,B013; K/T: B005,B010,B011,B014,B015,B016 |
| ج ن ب | 1 | B001,B002,B003,B005,B006,B007,B008,B009,B010,B011,B012 | P: B003; L: B001,B002,B005,B011; K/T: B006,B007,B008,B009,B010,B012 |
| ء ت ي | 1 | B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013 | P: B002; L: B001,B003,B004,B007,B010; K/T: B005,B006,B008,B009,B011,B012,B013 |
| ز ك و | 1 | B001,B002,B004,B005 | P: B001,B002; K/T: B004,B005 |
| ء ح د | 1 | B001,B002,B003,B004,B005,B006 | P: B002; L: B001,B005; K/T: B003,B004,B006 |
| ع ن د | 1 | B001,B002,B003,B004,B005,B006 | P: B004; L: B001,B002,B005,B006; K/T: B003 |
| ن ع م | 1 | B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013 | P: B001,B004; L: B002,B005,B010,B013; K/T: B003,B006,B007,B008,B009,B011,B012 |
| ج ز ي | 1 | B001,B002,B003,B004,B005 | P: B001,B002; L: B003,B004; K/T: B005 |
| ب غ ي | 1 | B001,B002,B003,B004,B005,B006,B007,B008 | P: B001; L: B002,B003; K/T: B004,B005,B006,B007,B008 |
| و ج ه | 1 | B001,B002,B003,B006,B007,B008,B009,B010,B011,B012,B013,B014,B015 | P: B001,B002,B008; L: B003,B006,B007; K/T: B009,B010,B011,B012,B013,B014,B015 |
| ر ب ب | 1 | B001,B002,B003,B004,B005,B006,B007,B008,B009,B010,B011,B012,B013,B014,B015,B016,B017 | P: B001,B002; L: B007,B011,B016; K/T: B003,B004,B005,B006,B008,B009,B010,B012,B013,B014,B015,B017 |
| ع ل و | 1 | B001,B002,B003,B004,B005,B006,B008,B009,B010,B011,B012 | P: B001,B002,B005; L: B004,B006,B012; K/T: B003,B008,B009,B010,B011 |
| ر ض و | 1 | B001,B002,B003,B004,B005,B006,B007 | P: B001,B002,B004; L: B003,B006; K/T: B005; T: B007 |

## Candidate Synthesis Units

### S92-P2-C01: Covering Night and Revealing Day Open the Polarity Engine

- `candidate_id`: S92-P2-C01
- `ayah_range`: 92:1-4
- `seed_type`: lexical
- `seed`: 92:1 `ٱلَّيْلِ`, especially `ل ي ل B001`, with `غ ش و B001` as first expansion.
- `generating_set`: `(E: ل ي ل B001 night and darkness)`, `(E: غ ش و B001 cover rising over and concealing a thing)`, `(E: ن ه ر B002 daylight against night)`, `(E: ج ل و B001 unveiling after concealment)`, `(E: ج ل و B007 white day and clear open sky)`, `(E: خ ل ق B002 bringing creation into being)`, `(E: ذ ك ر B001 male as opposite of female)`, `(E: ء ن ث B001 female as opposite of male)`, `(E: س ع ي B001 directed movement toward a sought thing)`, `(E: س ع ي B002 work/earning/conduct)`, `(E: ش ت ت B001 dispersion and divergent kinds)`.
- `selected_branches`: `ل ي ل B001,B002`; `غ ش و B001,B002`; `ن ه ر B002,B003`; `ج ل و B001,B007`; `خ ل ق B001,B002,B003`; `ذ ك ر B001`; `ء ن ث B001`; `س ع ي B001,B002`; `ش ت ت B001,B003`.
- `constructed_model`: The opening creates a perceptual engine: night covers, day uncovers, creation pairs male and female, and then human striving is declared split apart. The reciter first receives alternating states of concealment and revelation, then biological pairing, then moral/practical divergence.
- `freeze_point`: Freeze after 92:4, before the first `فَأَمَّا`.
- `predictions_at_freeze`: The passage should sort human action into opposed paths; one path should align with disclosure, opening, or ease, and another with cover, withholding, denial, or difficulty. Later closure should explain why this sorting matters.
- `unused_features_tested`: giving/withholding, truthing/denying, `حسنى`, `يسرى/عسرى`, wealth failing at downfall, guidance, fire, avoidance, purification, and final satisfaction.
- `corroborators`: `(C: ع ط و B002 giving as outward transfer)`, `(C: ب خ ل B001 withholding possessions)`, `(C: ص د ق B004 verification/actualization)`, `(C: ك ذ ب B002 attribution to falsehood)`, `(C: ي س ر B001 ease after difficulty)`, `(C: ع س ر B001 difficulty)`, `(C: attachments 92:5-10 two opposed conditional-relative profiles)`, `(C: repeated comparative endings الحسنى/اليسرى/العسرى/الأشقى/الأتقى/الأعلى)`.
- `constraints`: `(K: غ ش و B004 sexual euphemism is blocked by local subject الليل and adverbial إذا)`, `(K: ج ل و B003 bride unveiling and B009 bridal gift terminate; no nuptial construction is supplied)`, `(K: ذ ك ر B003-B009 memory/speech/honor branches remain secondary because 92:3 is direct object paired with الأنثى)`.
- `temporal_reactivation_notes`: The first four ayat make a sorting frame before any human moral action is named. The later `فأما...وأما` pair does not introduce polarity from nowhere; it fills the open slot created by cover/reveal and male/female.
- `rival_models`: A watercourse/day model from `ن ه ر B001` and `ن ه ر B003` can support flow imagery later, but the local primary contrast is day against night.
- `grade`: strong
- `grade_rationale`: Strong because the model is generated by the exact first sequence, then independently corroborated by the paired conditional architecture and repeated opposed outcomes.
- `source_queries_or_rows_used`: QAC TSV rows 92:1-4; v4 branches `ل ي ل`, `غ ش و`, `ن ه ر`, `ج ل و`, `خ ل ق`, `ذ ك ر`, `ء ن ث`, `س ع ي`, `ش ت ت`; attachments 92:1-4.

### S92-P2-C02: Scattered Striving Becomes Two Facilitated Tracks

- `candidate_id`: S92-P2-C02
- `ayah_range`: 92:4-10
- `seed_type`: constructional
- `seed`: `إِنَّ سَعْيَكُمْ لَشَتَّىٰ` followed by `فَأَمَّا...وَأَمَّا`.
- `generating_set`: `(E: س ع ي B001 directed movement)`, `(E: س ع ي B002 work and earning)`, `(E: ش ت ت B001 dispersion/different kinds)`, `(E: ش ت ت B003 distance between two things)`, `(E: ي س ر B001 ease/preparation)`, `(E: ع س ر B001 difficulty)`.
- `selected_branches`: `س ع ي B001,B002`; `ش ت ت B001,B003`; `ع ط و B002`; `و ق ي B001,B002`; `ص د ق B001,B004`; `ح س ن B001,B002`; `ب خ ل B001`; `غ ن ي B001`; `ك ذ ب B001,B002`; `ي س ر B001,B005`; `ع س ر B001,B004`.
- `constructed_model`: Human striving is not one road with different speeds; it is split into two tracks that are each made progressively easier to continue. One track opens through giving, self-protection, and verification of the fairest/finest outcome. The other tightens through withholding, imagined self-sufficiency, and denial of that same outcome.
- `freeze_point`: Freeze after 92:10.
- `predictions_at_freeze`: The passage should later show the insufficiency of stored resources, identify the guiding authority over paths, expose the end-state of the constricted track, and show the removal of the protected giver from that end-state.
- `unused_features_tested`: `وما يغني عنه ماله`, `إذا تردى`, `إن علينا للهدى`, `نارا تلظى`, `لا يصلاها إلا الأشقى`, `وسيجنبها الأتقى`, `يؤتي ماله يتزكى`.
- `corroborators`: `(C: غ ن ي B002 sufficing/availing fails at 92:11)`, `(C: م و ل B001 wealth as possession)`, `(C: ر د ي B003 falling into destruction)`, `(C: ه د ي B001 guidance to way/right)`, `(C: ن ذ ر B001 warning that awakens caution)`, `(C: ج ن ب B003 being removed/kept away from harm)`, `(C: ز ك و B002 purification)`.
- `constraints`: `(K: ي س ر B007 gambling/dividing carcass is a remote lexical branch; no lots or carcass role appears)`, `(K: ع س ر B006 obstructed birth is only a remote metaphor and does not govern the local comparative العسرى)`, `(K: ش ت ت B002 separated teeth provides only a weak image of spacing, not the main split)`.
- `temporal_reactivation_notes`: `سعيكم لشتى` becomes meaningful only after the two paths unfold. The double `فسنيسره` is a reactivation: both sides are "facilitated," but toward opposite termini.
- `rival_models`: A pure reward/punishment model explains the surface sequence but not the striking shared verb `نيسر` across both sides.
- `grade`: strong
- `grade_rationale`: Strong because the model explains sequence, repeated syntax, repeated root `يسر`, and the later tests of wealth, guidance, fire, and avoidance.
- `source_queries_or_rows_used`: QAC TSV rows 92:4-10; v4 branches listed; attachments 92:4-10.

### S92-P2-C03: Gift, Guard, and Verification Build the Opening Track

- `candidate_id`: S92-P2-C03
- `ayah_range`: 92:5-7, 92:17-21
- `seed_type`: lexical
- `seed`: 92:5 `أَعْطَىٰ`, `ع ط و B002`.
- `generating_set`: `(E: ع ط و B002 giving/making over)`, `(E: و ق ي B002 making oneself in protection)`, `(E: ص د ق B004 verifying promise/actualizing belief)`, `(E: ح س ن B001 the good/fair/beautiful as opposite of ugly)`, `(E: ي س ر B001 preparing ease)`.
- `selected_branches`: `ع ط و B002`; `و ق ي B001,B002`; `ص د ق B001,B003,B004`; `ح س ن B001,B002`; `ي س ر B001,B005`; later `ء ت ي B002`; `م و ل B001`; `ز ك و B001,B002`; `ب غ ي B001`; `و ج ه B001,B002,B008`; `ر ب ب B001,B002`; `ع ل و B001,B002`; `ر ض و B001,B002`.
- `constructed_model`: The positive path is a transfer system guarded by fear/protection and stabilized by verification. The initial giver returns at the end as the one who gives his wealth for self-purification, not to discharge a social debt, but seeking the Face of the highest Lord.
- `freeze_point`: Freeze after 92:7, before the negative profile and before the final description of `الأتقى`.
- `predictions_at_freeze`: If giving is the seed, later material should distinguish gift from repayment, show an object given, clarify purpose, and close with an accepted or satisfied result.
- `unused_features_tested`: `يؤتي ماله يتزكى`, `وما لأحد عنده من نعمة تجزى`, `إلا ابتغاء وجه ربه الأعلى`, `ولسوف يرضى`.
- `corroborators`: `(C: ء ت ي B002 giving/bringing at 92:18)`, `(C: م و ل B001 possessed wealth as object of giving)`, `(C: ز ك و B002 purification)`, `(C: ء ح د B002 negated universal anyone)`, `(C: ن ع م B001 favor/benefit)`, `(C: ج ز ي B001 recompense)`, `(C: ب غ ي B001 seeking)`, `(C: ر ض و B001 satisfaction after the seeker's act)`.
- `constraints`: `(K: ع ط و B004 illicit overreach is blocked by the immediately positive coordination with اتقى and صدق)`, `(K: ص د ق B006 almsgiving is related but not enough alone; the local verb is صدق بالحسنى before explicit wealth appears)`, `(K: ء ت ي B008 tribute/bribe is defeated by negated recompense in 92:19)`.
- `temporal_reactivation_notes`: The first `أعطى` is general and objectless. The later `يؤتي ماله` retroactively fills the object slot and makes the giving concrete; `يتزكى` supplies the inward transformation predicted by `اتقى`.
- `rival_models`: A simple charity model is valid at the primary level but too narrow for the full image because the passage rejects repayment logic and directs the act toward divine Face and final رضى.
- `grade`: strong
- `grade_rationale`: Strong because the seed predicts later object, motive, negated counter-motive, purification, and final closure.
- `source_queries_or_rows_used`: QAC TSV 92:5-7, 92:17-21; v4 `ع ط و`, `و ق ي`, `ص د ق`, `ح س ن`, `ي س ر`, `ء ت ي`, `م و ل`, `ز ك و`, `ء ح د`, `ن ع م`, `ج ز ي`, `ب غ ي`, `و ج ه`, `ر ب ب`, `ع ل و`, `ر ض و`; attachments 92:5-7, 92:18-20.

### S92-P2-C04: Withholding and Self-Sufficiency Make the Constriction Track

- `candidate_id`: S92-P2-C04
- `ayah_range`: 92:8-11, 92:15-16
- `seed_type`: lexical
- `seed`: 92:8 `بَخِلَ`, `ب خ ل B001`.
- `generating_set`: `(E: ب خ ل B001 withholding what should not be withheld)`, `(E: غ ن ي B001 wealth/self-sufficiency/no need)`, `(E: ك ذ ب B002 declaring or treating something as false)`, `(E: ح س ن B001 the good/fairest thing denied)`, `(E: ع س ر B001 difficulty/severity)`, `(E: غ ن ي B002 sufficing/availing tested and denied)`, `(E: م و ل B001 wealth)`, `(E: ر د ي B003 falling into destruction)`.
- `selected_branches`: `ب خ ل B001`; `غ ن ي B001,B002`; `ك ذ ب B001,B002`; `ح س ن B001`; `ي س ر B001` as facilitation mechanism; `ع س ر B001,B004`; `م و ل B001`; `ر د ي B003`; later `ش ق و B002`; `و ل ي B007`.
- `constructed_model`: The negative path begins as refusal of outward transfer, becomes self-enclosure in imagined sufficiency, rejects the fairest end, and is then made easy toward constriction. When the fall comes, the very thing that seemed to suffice cannot avail.
- `freeze_point`: Freeze after 92:10.
- `predictions_at_freeze`: The text should test sufficiency directly; the withheld possession should appear; the constricted path should end in contact with harm; denial should pair with turning away.
- `unused_features_tested`: `وما يغني عنه ماله إذا تردى`, `لا يصلاها إلا الأشقى`, `الذي كذب وتولى`.
- `corroborators`: `(C: attachment 92:11 ماله subject of لا يغني)`, `(C: ر د ي B003 falling to destruction)`, `(C: ص ل ي B003 entering/making contact with fire heat)`, `(C: ش ق و B002 hardship/misery)`, `(C: و ل ي B007 turning away/withdrawing)`, `(C: repeated كذب in 92:16 after 92:9)`.
- `constraints`: `(K: غ ن ي B003 singing/sound has no local acoustic role here)`, `(K: ع س ر B005 left-hand branch is not supported by local wording)`, `(K: ر د ي B004 garment/cloak branch is secondary and does not explain إذا تردى)`.
- `temporal_reactivation_notes`: `استغنى` is reactivated and judged by `وما يغني عنه ماله`: the passage repeats the root to distinguish felt self-sufficiency from actual non-availing.
- `rival_models`: A miser-character model explains 92:8 but misses the root repetition and downfall test in 92:11.
- `grade`: strong
- `grade_rationale`: Strong because the sequence tests the seed's own claim with a later same-root denial and concrete wealth subject.
- `source_queries_or_rows_used`: QAC TSV 92:8-11, 92:15-16; v4 branches listed; attachments 92:8-11, 92:15-16.

### S92-P2-C05: Repeated Facilitation Is a Guidance Mechanism, Not Neutral Ease

- `candidate_id`: S92-P2-C05
- `ayah_range`: 92:7, 92:10, 92:12
- `seed_type`: lexical
- `seed`: repeated `فَسَنُيَسِّرُهُۥ`, `ي س ر B001`.
- `generating_set`: `(E: ي س ر B001 ease/preparation after difficulty)`, `(E: ي س ر B005 lightness and compliant movement)`, `(E: ع س ر B001 difficulty)`, `(E: ه د ي B001 gentle guidance to path/truth)`, `(E: ه د ي B002 direction/way/mode of a matter)`, `(E: ه د ي B003 the leading front of a thing)`.
- `selected_branches`: `ي س ر B001,B005`; `ع س ر B001,B004`; `ه د ي B001,B002,B003`; `و ج ه B002`; `و ل ي B006,B007`; `ج ن ب B003`.
- `constructed_model`: Facilitation is not a simple reward word; it is the process by which a person becomes fitted to a path. The same verb operates for both outcomes, and 92:12 then identifies guidance as belonging to the divine side.
- `freeze_point`: Freeze after 92:12.
- `predictions_at_freeze`: If facilitation is path-fitting, later material should specify orientation, turning, being kept to a side, and the final sought face/direction.
- `unused_features_tested`: `تولى`, `سيجنبها`, `ابتغاء وجه ربه`, `الأعلى`.
- `corroborators`: `(C: و ل ي B006 turning face/attention toward)`, `(C: و ل ي B007 turning away)`, `(C: ج ن ب B003 removal to a side/avoidance)`, `(C: و ج ه B002 direction/face/mode)`, `(C: ع ل و B005 upper direction)`, `(C: attachment 92:7 and 92:10 لِـ complements mark destination/path)`.
- `constraints`: `(K: ي س ر B003 wealth/good fortune is constrained by 92:11 where wealth does not avail)`, `(K: ي س ر B007 gambling is unsupported)`, `(K: ه د ي B006 bride-leading and B008 swaying walk terminate as local seeds)`.
- `temporal_reactivation_notes`: The listener initially expects "ease" to contrast with "difficulty," but the repeated `نيسر` forces reanalysis: both tracks are eased, because guidance/path-fitting governs movement toward the chosen end.
- `rival_models`: A reward-only model treats `نيسر` in 92:10 as anomalous or ironic; the path-fitting model explains both occurrences without flattening their outcomes.
- `grade`: strong
- `grade_rationale`: Strong because of exact repetition, destination prepositions, immediate guidance claim, and later direction/avoidance language.
- `source_queries_or_rows_used`: QAC TSV 92:7, 92:10, 92:12, 92:16-20; v4 `ي س ر`, `ع س ر`, `ه د ي`, `و ل ي`, `ج ن ب`, `و ج ه`, `ع ل و`; attachments 92:7, 92:10, 92:12.

### S92-P2-C06: Fire Replays the Opening Light as Harmful Disclosure

- `candidate_id`: S92-P2-C06
- `ayah_range`: 92:1-2, 92:14-17
- `seed_type`: lexical
- `seed`: 92:14 `نَارًا تَلَظَّىٰ`, using `ن و ر B002` and `ل ظ ي B001`.
- `generating_set`: `(E: ن ذ ر B001 warning that awakens caution)`, `(E: ن و ر B002 fire kindled and marked by light/motion)`, `(E: ل ظ ي B001 pure blazing flame)`, `(E: ل ظ ي B002 Laza as fire)`, `(E: ص ل ي B003 meeting/entering fire heat)`, `(E: ش ق و B002 misery/hardship)`, `(E: ك ذ ب B002 denial)`, `(E: و ل ي B007 turning away)`.
- `selected_branches`: `ن ذ ر B001`; `ن و ر B001,B002,B005`; `ل ظ ي B001,B002,B003,B004`; `ص ل ي B003,B004`; `ش ق و B002`; `ك ذ ب B001,B002`; `و ل ي B007`; `ج ن ب B003`; `و ق ي B001,B002`.
- `constructed_model`: The opening day revealed after night, but the later fire is a destructive illumination. Warning names it before contact; only the most wretched, defined by denial and turning away, enters it, while the most protected is set aside from it.
- `freeze_point`: Freeze after 92:15.
- `predictions_at_freeze`: The passage should define the entrant and the one excluded; exclusion should be stated with side/removal/protection language.
- `unused_features_tested`: `الذي كذب وتولى`, `وسيجنبها الأتقى`.
- `corroborators`: `(C: ك ذ ب B002 denial defines the entrant)`, `(C: و ل ي B007 turning away defines the entrant)`, `(C: ج ن ب B003 being removed/kept apart)`, `(C: و ق ي B002 self in protection in الأتقى)`, `(C: attachment 92:15 إلا restricts subject of يصلاها to الأشقى)`, `(C: attachment 92:17 passive subject الأتقى is kept from fire)`.
- `constraints`: `(K: ن و ر B001 general light is not enough; local نارا requires fire branch B002)`, `(K: ص ل ي B001 prayer and B002 blessing branches are blocked by object pronoun ها returning to fire)`, `(K: ل ظ ي B003 anger is secondary only; local adjective describes fire)`.
- `temporal_reactivation_notes`: The passage reuses the sensory field of light after opening night/day, but changes its value: disclosure is no longer daybreak clarity; it is the revealed heat of the constriction track.
- `rival_models`: A pure eschatological-fire model is primary but static; the reactivation model explains why fire arrives after guidance and track-sorting.
- `grade`: medium-strong
- `grade_rationale`: Strong local lexical and syntactic support; medium-strong rather than strong because the opening light reactivation is secondary to the primary warning/fire statement.
- `source_queries_or_rows_used`: QAC TSV 92:1-2, 92:14-17; v4 branches listed; attachments 92:14-17.

### S92-P2-C07: The Protected One Is Set to the Side of Fire

- `candidate_id`: S92-P2-C07
- `ayah_range`: 92:5, 92:14-18
- `seed_type`: lexical
- `seed`: 92:17 `وَسَيُجَنَّبُهَا`, `ج ن ب B003`.
- `generating_set`: `(E: ج ن ب B003 distancing, avoiding, removing from harm)`, `(E: ج ن ب B001 side/edge)`, `(E: و ق ي B001 barrier against harm)`, `(E: و ق ي B002 making oneself in protection)`, `(E: ن و ر B002 fire)`, `(E: ل ظ ي B001 blaze)`.
- `selected_branches`: `ج ن ب B001,B003,B005,B011`; `و ق ي B001,B002`; `ن و ر B002`; `ل ظ ي B001`; `ص ل ي B003`; `ء ت ي B002`; `ز ك و B002`.
- `constructed_model`: Avoidance is spatialized. Fire is not merely not-entered; the protected one is actively put to the side of it. The earlier `اتقى` becomes concrete as `الأتقى`, whose giving produces purification and whose position is away from the blaze.
- `freeze_point`: Freeze after 92:17, before the relative clause describing `الأتقى`.
- `predictions_at_freeze`: The protected one should be identified by an action that fits `اتقى` and by a purpose that is not ordinary exchange.
- `unused_features_tested`: `الذي يؤتي ماله يتزكى`, `وما لأحد عنده من نعمة تجزى`, `إلا ابتغاء وجه ربه الأعلى`.
- `corroborators`: `(C: ء ت ي B002 giving)`, `(C: م و ل B001 wealth)`, `(C: ز ك و B002 purification)`, `(C: ج ز ي B001 recompense negated)`, `(C: ب غ ي B001 seeking as purpose)`, `(C: و ج ه B002 directed face/goal)`.
- `constraints`: `(K: ج ن ب B006 south wind, B007 side disease, B008 low milk, B010 plant, B012 stance defects terminate)`, `(K: ج ن ب B005 leading an animal at one's side is only a weak spatial support, not the main passive sense)`.
- `temporal_reactivation_notes`: `اتقى` in 92:5 is initially an inward/protective stance; 92:17 turns that stance into a passive outcome enacted upon the person.
- `rival_models`: A moral-rank-only model explains `الأَتقى`, but the root `جنب` adds a spatial removal image that better fits the fire scene.
- `grade`: strong
- `grade_rationale`: Strong because exact passive avoidance, fire object pronoun, and final giver description all converge.
- `source_queries_or_rows_used`: QAC TSV 92:5, 92:14-18; v4 `ج ن ب`, `و ق ي`, `ن و ر`, `ل ظ ي`, `ص ل ي`, `ء ت ي`, `م و ل`, `ز ك و`; attachments 92:17-18.

### S92-P2-C08: Wealth Is Reclassified From Sufficiency to Purifying Transfer

- `candidate_id`: S92-P2-C08
- `ayah_range`: 92:8-11, 92:18-20
- `seed_type`: lexical
- `seed`: repeated `مَال`, `م و ل B001`.
- `generating_set`: `(E: م و ل B001 taking/possessing wealth and abundance)`, `(E: غ ن ي B001 wealth/self-sufficiency)`, `(E: غ ن ي B002 sufficing/availing)`, `(E: ب خ ل B001 withholding)`, `(E: ء ت ي B002 giving)`, `(E: ز ك و B001 growth/increase)`, `(E: ز ك و B002 purification/righteousness)`.
- `selected_branches`: `م و ل B001`; `غ ن ي B001,B002`; `ب خ ل B001`; `ع ط و B002`; `ء ت ي B002`; `ز ك و B001,B002`; `ن ع م B001`; `ج ز ي B001,B002`; `ب غ ي B001`; `و ج ه B001,B002`.
- `constructed_model`: Wealth appears twice with opposite functions. In the negative track, wealth is possessed and expected to avail, but cannot save at falling. In the positive track, wealth is transferred outward and becomes the medium of purification, explicitly separated from repayment for a favor.
- `freeze_point`: Freeze after 92:18.
- `predictions_at_freeze`: A later clause should prevent the gift from being read as exchange or social debt; it should provide a higher-directed purpose.
- `unused_features_tested`: `وما لأحد عنده من نعمة تجزى`, `إلا ابتغاء وجه ربه الأعلى`.
- `corroborators`: `(C: ء ح د B002 universal negation under ما/من)`, `(C: ع ن د B004 favor located with him)`, `(C: ن ع م B001 favor/benefit)`, `(C: ج ز ي B001 recompense and B002 sufficing in another's place)`, `(C: ب غ ي B001 seeking)`, `(C: و ج ه B002 direction/purpose)`, `(C: ر ب ب B001 Lord/owner)`, `(C: ع ل و B002 high rank)`.
- `constraints`: `(K: ن ع م B005 livestock wealth is not locally specified; مال is general possession)`, `(K: ج ز ي B004 tax/tribute is defeated by the negative exchange construction)`, `(K: ز ك و B005 pair/even branch terminates)`.
- `temporal_reactivation_notes`: `ماله` in 92:11 is a failed support; `ماله` in 92:18 is a released object. This reversal reactivates the opening cover/reveal contrast as holding versus exposing/transferring.
- `rival_models`: A simple "money bad/good" reading is too coarse. The passage distinguishes mode: retained wealth fails; given wealth purifies when freed from recompense logic.
- `grade`: strong
- `grade_rationale`: Strong because the same noun recurs in opposite syntactic roles and is tested by sufficiency, transfer, purification, and negated recompense.
- `source_queries_or_rows_used`: QAC TSV 92:8-11, 92:18-20; v4 branches listed; attachments 92:11, 92:18-20.

### S92-P2-C09: No Recompensed Favor Clears the Motive Channel

- `candidate_id`: S92-P2-C09
- `ayah_range`: 92:19-20
- `seed_type`: constructional
- `seed`: `وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍ تُجْزَىٰٓ إِلَّا ٱبْتِغَاءَ...`
- `generating_set`: `(E: ء ح د B002 universal negation under negation)`, `(E: ع ن د B004 possession/presence with him)`, `(E: ن ع م B001 favor/blessing/benefit)`, `(E: ج ز ي B001 recompense)`, `(E: ج ز ي B002 sufficing/standing in another's place)`, `(E: ب غ ي B001 seeking)`, `(E: و ج ه B001 face/front)`, `(E: و ج ه B002 direction/goal)`.
- `selected_branches`: `ء ح د B002`; `ع ن د B004`; `ن ع م B001,B004`; `ج ز ي B001,B002`; `ب غ ي B001`; `و ج ه B001,B002,B008`; `ر ب ب B001,B002`; `ع ل و B001,B002,B005`; `ر ض و B001`.
- `constructed_model`: The text drains away every horizontal repayment motive. No one has a favor lodged with him that is being paid back. The only exception is a verticalized seeking: the Face/direction of his highest Lord.
- `freeze_point`: Freeze after 92:20.
- `predictions_at_freeze`: A closure of acceptance or satisfaction should follow, because the motive channel has been purified and directed.
- `unused_features_tested`: `ولسوف يرضى`.
- `corroborators`: `(C: ر ض و B001 satisfaction/acceptance)`, `(C: ر ض و B002 abundant/sought رضوان)`, `(C: attachment 92:20 إلا introduces ابتغاء as excepted purpose)`, `(C: idafa chain ابتغاء وجه ربه الأعلى)`.
- `constraints`: `(K: ع ن د B001 stubborn opposition is not local; عنده is locative/possessive)`, `(K: ب غ ي B003 transgressive seeking is blocked by وجه ربه الأعلى and final رضى)`, `(K: و ج ه B013 striking face and B014 repelling from face terminate)`.
- `temporal_reactivation_notes`: The final exception reuses the earlier exception architecture of fire: one exception identifies who enters harm; this exception identifies the only valid motive for the protected giver.
- `rival_models`: Social reciprocity model is explicitly defeated by the negated `نعمة تجزى`.
- `grade`: strong
- `grade_rationale`: Strong because syntax, negation, universal `أحد`, recompense root, exception, idafa chain, and final رضى all align.
- `source_queries_or_rows_used`: QAC TSV 92:19-21; v4 `ء ح د`, `ع ن د`, `ن ع م`, `ج ز ي`, `ب غ ي`, `و ج ه`, `ر ب ب`, `ع ل و`, `ر ض و`; attachments 92:19-20.

### S92-P2-C10: Direction, Face, Turning Away, and Highest Orientation

- `candidate_id`: S92-P2-C10
- `ayah_range`: 92:12, 92:16, 92:20
- `seed_type`: verified composite
- `seed`: orientation cluster: `للهدى`, `تولى`, `وجه ربه الأعلى`.
- `generating_set`: `(E: ه د ي B001 guidance to way/right)`, `(E: ه د ي B002 direction/way/mode)`, `(E: و ل ي B006 turning face/attention toward)`, `(E: و ل ي B007 turning away)`, `(E: و ج ه B001 face/front)`, `(E: و ج ه B002 direction/goal)`, `(E: ع ل و B001 height)`, `(E: ع ل و B002 exalted rank)`.
- `selected_branches`: `ه د ي B001,B002,B003`; `و ل ي B006,B007`; `و ج ه B001,B002,B008`; `ر ب ب B001,B002`; `ع ل و B001,B002,B005`; `ب غ ي B001`; `ر ض و B001`.
- `constructed_model`: The surah has a directional axis. Guidance belongs to the divine side; the wretched one denies and turns away; the protected giver seeks a Face/direction above him. The final satisfaction closes the movement toward the correct orientation.
- `freeze_point`: Freeze after 92:20.
- `predictions_at_freeze`: A delayed satisfaction should answer the long movement; no additional earthly recipient should appear after the Face clause.
- `unused_features_tested`: `ولسوف يرضى`.
- `corroborators`: `(C: ر ض و B001 satisfaction closes the directed seeking)`, `(C: attachment 92:20 وجه is genitive complement of ابتغاء and رب is complement of وجه)`, `(C: الأعلى adjective of ربه)`.
- `constraints`: `(K: و ل ي B003 political guardianship and B014 sale transfer lack local roles)`, `(K: ع ل و B003 arrogant elevation is constrained by رب and final رضى; it is not the seeker's arrogance)`, `(K: ه د ي B004 gift branch is secondary despite giving language because 92:12 names الهدى as guidance)`.
- `temporal_reactivation_notes`: `تولى` is a backward-turning failure against guidance; `ابتغاء وجه` is forward/upward seeking. The same general orientation field divides the two tracks.
- `rival_models`: A pure legal-obligation reading of `علينا للهدى` explains 92:12 but not the later face/turning network.
- `grade`: medium-strong
- `grade_rationale`: Medium-strong because the directional branches are independently present and syntactically linked, though some are broader conceptual branches.
- `source_queries_or_rows_used`: QAC TSV 92:12, 92:16, 92:20-21; v4 branches listed; attachments 92:12, 92:16, 92:20.

### S92-P2-C11: Comparative Endings Form a Ranked Outcome Ladder

- `candidate_id`: S92-P2-C11
- `ayah_range`: 92:6-21
- `seed_type`: morphosyntactic
- `seed`: repeated feminine/superlative/comparative forms: `الحسنى`, `اليسرى`, `العسرى`, `الأشقى`, `الأتقى`, `الأعلى`.
- `generating_set`: `(E: ح س ن B001 good/fair/beautiful)`, `(E: ي س ر B001 ease)`, `(E: ع س ر B001 difficulty)`, `(E: ش ق و B002 hardship/misery)`, `(E: و ق ي B002 protected/pious self)`, `(E: ع ل و B002 exalted/high rank)`.
- `selected_branches`: `ح س ن B001,B002`; `ي س ر B001`; `ع س ر B001`; `ش ق و B002`; `و ق ي B002`; `ع ل و B001,B002`; morphology of repeated `أفعل/فعلى` outcomes.
- `constructed_model`: After the opening male/female pair, the passage repeatedly uses ranked polar forms to sort outcome: the fairest, easiest, hardest, most wretched, most protected, highest. The grammar makes the moral split feel like a ladder of opposed extrema.
- `freeze_point`: Freeze after 92:17, before `ربه الأعلى`.
- `predictions_at_freeze`: The final divine orientation should complete the ranked ladder with a highest term.
- `unused_features_tested`: `ربه الأعلى`, `ولسوف يرضى`.
- `corroborators`: `(C: ع ل و B002 highest rank in الأعلى)`, `(C: ر ب ب B001 Lord/owner as the high referent)`, `(C: ر ض و B001 final acceptance)`, `(C: sequence from الحسنى to الأعلى)`.
- `constraints`: `(K: these forms are not treated as alternative translations; they are morphosyntactic recurrence and ranking evidence)`, `(K: feminine endings in الحسنى/اليسرى/العسرى do not by themselves revive الأنثى as a new seed; they support patterned recurrence only)`.
- `temporal_reactivation_notes`: The ear hears `الحسنى`, then matched `اليسرى/العسرى`, then `الأشقى/الأتقى`, then `الأعلى`. The final highest term makes earlier "best/fair/easy/hard" forms part of a ranked architecture.
- `rival_models`: A mere rhyme/sound model accounts for recurrence but not the semantic polarity and rank sequence.
- `grade`: medium-strong
- `grade_rationale`: Strong formal recurrence and semantic opposition; medium-strong because it is a structural image more than a lexical branch avalanche.
- `source_queries_or_rows_used`: QAC TSV 92:6-21; v4 listed roots; attachments 92:6-20.

### S92-P2-C12: Creation Pairing Predicts Moral Pairing Without Collapsing Them

- `candidate_id`: S92-P2-C12
- `ayah_range`: 92:3-10, 92:15-17
- `seed_type`: lexical
- `seed`: 92:3 `ٱلذَّكَرَ وَٱلْأُنثَىٰ`, `ذ ك ر B001` and `ء ن ث B001`.
- `generating_set`: `(E: خ ل ق B002 creation/bringing into being)`, `(E: خ ل ق B003 complete formed shape)`, `(E: ذ ك ر B001 male opposite female)`, `(E: ء ن ث B001 female opposite male)`, `(E: ش ت ت B001 divergent kinds)`.
- `selected_branches`: `خ ل ق B001,B002,B003,B004`; `ذ ك ر B001`; `ء ن ث B001`; `ش ت ت B001,B003`; later paired conditional syntax and `الأشقى/الأتقى`.
- `constructed_model`: The created biological pair gives the passage an initial two-pole template, but the next verse moves from biological pair to divergent striving. The later pairs are moral and directional, not gender translations.
- `freeze_point`: Freeze after 92:4.
- `predictions_at_freeze`: A non-biological pair should follow and should be sorted by action rather than sex.
- `unused_features_tested`: `فأما من أعطى...وأما من بخل`, `الأشقى/الأتقى`, `الذي كذب وتولى`, `الذي يؤتي ماله`.
- `corroborators`: `(C: paired conditional syntax 92:5 and 92:8)`, `(C: relative descriptions 92:16 and 92:18 define moral agents)`, `(C: ش ق و B002 and و ق ي B002 as outcome ranks)`.
- `constraints`: `(K: ء ن ث B002 weakness and ذ ك ر B002 hardness are not used to gender the moral paths; no local evidence assigns giving or withholding by sex)`, `(K: ء ن ث B004 fertile land is a remote local-only image and terminates)`.
- `temporal_reactivation_notes`: The passage first teaches "two-ness" by creation, then immediately reuses the two-slot structure for human striving. This is reactivation of form, not transfer of gendered content.
- `rival_models`: A gender-essentializing model is defeated by the text's shift from created pair to `سعيكم` and `من`.
- `grade`: medium-strong
- `grade_rationale`: Strong sequence and syntax; medium-strong because the lexical branches mainly establish pairing rather than a detailed secondary simulation.
- `source_queries_or_rows_used`: QAC TSV 92:3-10, 92:15-18; v4 `خ ل ق`, `ذ ك ر`, `ء ن ث`, `ش ت ت`, `ش ق و`, `و ق ي`; attachments 92:3, 92:5-10, 92:15-18.

### S92-P2-C13: Seeking the Face Completes the Beauty/Goodness Seed

- `candidate_id`: S92-P2-C13
- `ayah_range`: 92:6, 92:20-21
- `seed_type`: lexical
- `seed`: 92:6 and 92:9 `ٱلْحُسْنَىٰ`, `ح س ن B001`.
- `generating_set`: `(E: ح س ن B001 good/beautiful/desirable as opposite of ugly)`, `(E: ح س ن B002 doing good/excellence/benefaction)`, `(E: ص د ق B004 actualizing verification)`, `(E: ك ذ ب B002 denying)`, `(E: ب غ ي B001 seeking)`, `(E: و ج ه B001 face/front)`, `(E: و ج ه B008 right face of an affair)`, `(E: ر ض و B001 satisfaction)`.
- `selected_branches`: `ح س ن B001,B002,B005`; `ص د ق B001,B004`; `ك ذ ب B001,B002`; `ب غ ي B001`; `و ج ه B001,B002,B008`; `ر ب ب B001`; `ع ل و B002`; `ر ض و B001,B002`.
- `constructed_model`: `الحسنى` starts as the fairest/good outcome to be verified or denied. The final scene shows what verifying it looks like in motion: seeking the Face of the highest Lord until satisfaction.
- `freeze_point`: Freeze after the second `الحسنى` in 92:9.
- `predictions_at_freeze`: The text should clarify the content or orientation of `الحسنى` without reducing it to a material reward.
- `unused_features_tested`: `ابتغاء وجه ربه الأعلى`, `ولسوف يرضى`.
- `corroborators`: `(C: ب غ ي B001 seeking)`, `(C: و ج ه B008 right/appropriate face of an affair)`, `(C: ع ل و B002 exalted rank)`, `(C: ر ض و B001 satisfaction)`.
- `constraints`: `(K: ح س ن B004 place/body names terminate)`, `(K: ح س ن B005 extreme effort is local-only and cannot define الحسنى by itself)`, `(K: the passage never states a concrete worldly object as الحسنى)`.
- `temporal_reactivation_notes`: `الحسنى` is repeated before its final motive-direction is disclosed. The repetition keeps the object active until `وجه ربه الأعلى` and `يرضى` fill its orientation and affective closure.
- `rival_models`: Identifying `الحسنى` with any single material benefit is constrained by negated recompense and the divine Face clause.
- `grade`: medium-strong
- `grade_rationale`: Good lexical and temporal support, but the exact referent remains intentionally broad and should be preserved as an oriented good rather than over-specified.
- `source_queries_or_rows_used`: QAC TSV 92:6, 92:9, 92:20-21; v4 `ح س ن`, `ص د ق`, `ك ذ ب`, `ب غ ي`, `و ج ه`, `ر ب ب`, `ع ل و`, `ر ض و`; attachments 92:6, 92:9, 92:20.

### S92-P2-C14: Remote Watercourse and Flow Branches Form a Weak Secondary Simulation

- `candidate_id`: S92-P2-C14
- `ayah_range`: 92:1-21
- `seed_type`: lexical
- `seed`: remote branch cluster `ن ه ر B001`, `ء ت ي B004`, `ي س ر B005`, `ه د ي B002`.
- `generating_set`: `(E: ن ه ر B001 river cutting earth with flowing water)`, `(E: ن ه ر B003 opening/widening until flow)`, `(E: ء ت ي B004 water channel and directing flow)`, `(E: ي س ر B005 light compliant movement)`, `(E: ه د ي B002 direction/way)`, `(E: ج ن ب B003 moving aside/avoidance)`.
- `selected_branches`: `ن ه ر B001,B003`; `ء ت ي B004`; `ي س ر B005`; `ه د ي B002`; `و ج ه B002`; `ج ن ب B003`; `ع س ر B004`.
- `constructed_model`: A weak but coherent secondary image treats the surah as channeling motion. Day/river opening and directed flow give a path image; facilitation makes movement compliant; difficulty is obstruction or twisting; avoidance moves a person to the side of the fire-channel.
- `freeze_point`: Freeze after assembling `هدي`, `يسر`, `عسر`, and `جنب`.
- `predictions_at_freeze`: The image should predict directionality and side-removal, not necessarily water language.
- `unused_features_tested`: `وجه`, `تولى`, `سيجنبها`, `ابتغاء`.
- `corroborators`: `(C: و ج ه B002 direction/goal)`, `(C: و ل ي B006/B007 turning toward/away)`, `(C: attachment لليسرى/للعسرى as path complements)`.
- `constraints`: `(K: no explicit water term appears in the sacred text of S92)`, `(K: ن ه ر locally means daylight in 92:2 more strongly than river)`, `(K: ء ت ي B004 is remote from يؤتي ماله, where giving is primary)`.
- `temporal_reactivation_notes`: This image is useful only as a geometry of flow and obstruction; it should not become an alternative translation.
- `rival_models`: The main path-fitting candidate C05 captures most of the same structure with less lexical remoteness.
- `grade`: weak
- `grade_rationale`: Coherent geometry, but the major water branches are remote from local primary meanings and lack explicit water corroboration.
- `source_queries_or_rows_used`: QAC TSV 92:2, 92:7, 92:10, 92:12, 92:17-20; v4 listed roots; attachments 92:7, 92:10, 92:17, 92:20.

## Constructional, Morphosyntactic, and Temporal Seeds

- `إذا` clauses in 92:1 and 92:2: retained as temporal/acoustic seed. Night and day are not static objects; each is heard under a temporal condition. `(C: attachments 92:1 and 92:2 adverbial إذا)` supports the unfolding cover/reveal image. Grade: medium-strong.
- `وما خلق الذكر والأنثى`: retained as constructional seed. Direct objects and coordination force created pairing, then `إن سعيكم لشتى` transfers the two-slot frame into action divergence. Grade: medium-strong.
- `إن سعيكم لشتى`: retained as central constructional seed. It is the hinge between cosmic/created polarity and moral path polarity. Grade: strong.
- `فأما...وأما`: retained as morphosyntactic seed. It divides the scattered striving into two profiles with parallel verb clusters. Grade: strong.
- Repeated `فسنيسره`: retained as temporal/acoustic seed. Repetition forces a path-fitting model rather than simple reward vocabulary. Grade: strong.
- Repeated `بالحسنى`: retained as temporal/acoustic seed. The same object is verified and denied, keeping it active until the final Face/satisfaction closure. Grade: medium-strong.
- `وما يغني عنه ماله إذا تردى`: retained as constraint seed. It tests and defeats the `استغنى` branch by same-root reactivation. Grade: strong.
- `إن علينا للهدى` and `وإن لنا للآخرة والأولى`: retained as ownership/guidance construction. It supplies the authority over both path and temporal end-points. Grade: medium-strong.
- `لا يصلاها إلا الأشقى` and `إلا ابتغاء وجه ربه الأعلى`: retained as repeated exception architecture. The first exception restricts fire-contact; the second purifies motive. Grade: medium-strong.
- `الذي كذب وتولى` / `الذي يؤتي ماله يتزكى`: retained as relative-clause definition seed. The two extreme agents are defined by actions, not labels alone. Grade: strong.
- Negation stack in 92:19: retained as constructional seed. `ما`, `لأحد`, `من نعمة`, and `تجزى` erase repayment before the final motive appears. Grade: strong.
- Final `ولسوف يرضى`: retained as closure seed. Deferred future satisfaction closes the directed seeking and the good-path image. Grade: medium-strong.

## Terminated Seed Families

The following branch families were initiated and rejected or limited because they did not produce passage-local role completion:

- Proper-name branches: `ل ي ل B004`, `ء ح د B006`, `ء و ل B009`, `ي س ر B010`, and similar name/place-only branches terminate.
- Animal, livestock, or specialized pastoral branches: `و ق ي B005`, `ن ع م B005-B009`, `ص ل ي B010`, `ع س ر B009`, and related branches remain remote unless used only as weak imagery; no local animal scene is supplied.
- Sexual or birth branches: `غ ش و B004`, `ء ن ث B003`, `ع س ر B006`, `و ج ه B010`, and `ء ت ي B012` terminate or remain weak constraints; the created male/female pair is not a sexual-event narrative.
- Tool/game/tax branches: `ي س ر B007`, `ج ز ي B004`, `ء ت ي B008`, `ر ب ب B010`, `ع ل و B009`, and `ع س ر B013` lack local game, tax, or instrument roles.
- Remote bodily injury or disease branches: `ج ن ب B007`, `ص ل ي B006`, `و ج ه B013`, `ب غ ي B004`, and `ن ذ ر B003` do not govern the passage's primary images.
- Sound/song branches: `غ ن ي B003` and `ه د ي B011` lack local acoustic support beyond recitational sound and were not used as lexical evidence.

## Image Packet Catalog

### IMG-S92-01

- Starting seed: `ل ي ل B001` at 92:1.
- Complete image: cover/reveal polarity becomes moral path sorting.
- Passage-order assembly: night covers -> day reveals -> pair created -> striving scattered -> two profiles unfold.
- Participants and roles: night concealer, day revealer, Creator, created pair, human strivers.
- Operation / mechanism: concealment, disclosure, pairing, divergence.
- Direction / force / medium: temporal alternation and moral sorting.
- Temporal development: 92:1-4 generates frame; 92:5-10 fills it; 92:14-21 closes outcomes.
- Outcome / closure: protected seeker receives رضى; denier/turner meets fire.
- Exact branch constituents: `ل ي ل B001`, `غ ش و B001`, `ن ه ر B002`, `ج ل و B001/B007`, `خ ل ق B002`, `ذ ك ر B001`, `ء ن ث B001`, `س ع ي B001/B002`, `ش ت ت B001`.
- Unfilled roles, if any: none for the polarity frame.
- Status: COMPLETE.

### IMG-S92-02

- Starting seed: `س ع ي B001/B002` at 92:4.
- Complete image: scattered striving becomes two facilitated tracks.
- Passage-order assembly: striving split -> giving/protection/verification -> ease; withholding/self-sufficiency/denial -> difficulty.
- Participants and roles: two `من` agents, divine facilitator, path termini.
- Operation / mechanism: repeated facilitation fits each person to a path.
- Direction / force / medium: motion toward `اليسرى` or `العسرى`.
- Temporal development: 92:4 states divergence; 92:5-10 models it; 92:12 grounds guidance.
- Outcome / closure: one path is side-removed from fire; one enters it.
- Exact branch constituents: `س ع ي B001/B002`, `ش ت ت B001/B003`, `ي س ر B001`, `ع س ر B001`, `ه د ي B001/B002`.
- Unfilled roles, if any: none.
- Status: COMPLETE.

### IMG-S92-03

- Starting seed: `ع ط و B002` at 92:5.
- Complete image: giving becomes purified non-reciprocal transfer.
- Passage-order assembly: gave -> protected self -> verified best -> later gives wealth -> purifies -> no favor repaid -> seeks Face -> satisfaction.
- Participants and roles: giver, wealth, no human creditor, highest Lord, final satisfied recipient.
- Operation / mechanism: transfer, purification, motive-clearing.
- Direction / force / medium: wealth moves outward; intention moves upward.
- Temporal development: 92:5 objectless giving is concretized in 92:18-20.
- Outcome / closure: `ولسوف يرضى`.
- Exact branch constituents: `ع ط و B002`, `و ق ي B002`, `ص د ق B004`, `ح س ن B001`, `ء ت ي B002`, `م و ل B001`, `ز ك و B002`, `ب غ ي B001`, `و ج ه B002`, `ر ب ب B001`, `ع ل و B002`, `ر ض و B001`.
- Unfilled roles, if any: the exact referent of `الحسنى` remains deliberately broad.
- Status: COMPLETE.

### IMG-S92-04

- Starting seed: `ب خ ل B001` at 92:8.
- Complete image: withholding becomes constriction and failed sufficiency.
- Passage-order assembly: withheld -> self-sufficed -> denied best -> eased to difficulty -> wealth fails -> falls -> enters fire.
- Participants and roles: withholder, wealth, denied good, constricted path, fire.
- Operation / mechanism: retention, self-enclosure, denial, downfall.
- Direction / force / medium: inward hoarding followed by downward falling and fire-contact.
- Temporal development: 92:8-10 constructs; 92:11 tests; 92:15-16 closes.
- Outcome / closure: exclusive fire-contact for `الأشقى`.
- Exact branch constituents: `ب خ ل B001`, `غ ن ي B001/B002`, `ك ذ ب B002`, `ع س ر B001`, `م و ل B001`, `ر د ي B003`, `ص ل ي B003`, `ش ق و B002`, `و ل ي B007`.
- Unfilled roles, if any: none.
- Status: COMPLETE.

### IMG-S92-05

- Starting seed: `ن و ر B002` / `ل ظ ي B001` at 92:14.
- Complete image: harmful light/fire reactivates opening disclosure.
- Passage-order assembly: warning -> blazing fire -> only wretched enters -> denier turns away -> protected one is set aside.
- Participants and roles: warner, fire, wretched entrant, protected avoider.
- Operation / mechanism: warning, fire-contact, exclusion, side-removal.
- Direction / force / medium: blaze and spatial avoidance.
- Temporal development: opening day-light becomes later fire-light by contrast.
- Outcome / closure: the protected one is kept away and defined by purified giving.
- Exact branch constituents: `ن ذ ر B001`, `ن و ر B002`, `ل ظ ي B001/B002`, `ص ل ي B003`, `ش ق و B002`, `ك ذ ب B002`, `و ل ي B007`, `ج ن ب B003`, `و ق ي B002`.
- Unfilled roles, if any: none.
- Status: COMPLETE.

### IMG-S92-06

- Starting seed: `ن ه ر B001` / `ء ت ي B004` remote flow cluster.
- Complete image: weak channel/flow geometry.
- Passage-order assembly: day/river opening -> path facilitation -> guidance direction -> side-removal.
- Participants and roles: moving person, channel/path, guide, obstruction/side removal.
- Operation / mechanism: channeling, easing, obstructing, avoiding.
- Direction / force / medium: path-flow rather than explicit water.
- Temporal development: distributed across 92:2, 92:7, 92:10, 92:12, 92:17, 92:20.
- Outcome / closure: useful as geometry only.
- Exact branch constituents: `ن ه ر B001/B003`, `ء ت ي B004`, `ي س ر B005`, `ه د ي B002`, `و ج ه B002`, `ج ن ب B003`.
- Unfilled roles, if any: no explicit water term in passage.
- Status: FRAGMENT.

### IMG-S92-07

- Starting seed: `ء ح د B002` and the negation stack at 92:19.
- Complete image: motive-clearing channel toward the Face of the highest Lord.
- Passage-order assembly: wealth is given -> no favor with anyone is being repaid -> only seeking the Face remains -> satisfaction closes.
- Participants and roles: giver, excluded human creditor, favor/recompense relation, highest Lord, final رضى.
- Operation / mechanism: negation, removal of exchange motive, exception, directed seeking.
- Direction / force / medium: horizontal repayment is cleared; intention is directed upward.
- Temporal development: 92:18 gives the act; 92:19 purges reciprocity; 92:20 supplies purpose; 92:21 supplies closure.
- Outcome / closure: `ولسوف يرضى`.
- Exact branch constituents: `ء ح د B002`, `ع ن د B004`, `ن ع م B001`, `ج ز ي B001/B002`, `ب غ ي B001`, `و ج ه B001/B002`, `ر ب ب B001`, `ع ل و B002`, `ر ض و B001`.
- Unfilled roles, if any: none.
- Status: COMPLETE.

### IMG-S92-08

- Starting seed: repeated ranked forms `الحسنى/اليسرى/العسرى/الأشقى/الأتقى/الأعلى`.
- Complete image: comparative ladder of opposed extrema.
- Passage-order assembly: fairest good -> easiest path / hardest path -> most wretched / most protected -> highest Lord.
- Participants and roles: two path agents, ranked outcomes, highest divine orientation.
- Operation / mechanism: morphological recurrence, semantic opposition, rank escalation.
- Direction / force / medium: upward/downward ranking and path polarity.
- Temporal development: begins at 92:6, forks at 92:7-10, names extremes at 92:15-17, completes at 92:20.
- Outcome / closure: final رضى follows the highest-oriented side.
- Exact branch constituents: `ح س ن B001`, `ي س ر B001`, `ع س ر B001`, `ش ق و B002`, `و ق ي B002`, `ع ل و B001/B002`.
- Unfilled roles, if any: the precise semantic breadth of `الحسنى` remains open by design.
- Status: COMPLETE.

## Exhaustiveness Check After File Creation

The file now accounts for all 41 distinct S92 roots, all 48 rooted word occurrences, and all 358 occurrence-by-branch lexical seed passes from the available accepted v4 branch rows. It also records the required non-lexical seed families: temporal `إذا` clauses, created-pair coordination, `إن سعيكم لشتى`, the two `فأما` profiles, repeated `فسنيسره`, repeated `بالحسنى`, the wealth/downfall constraint, divine guidance/ownership, exception architecture, relative-clause definitions, the negation stack, and final رضى closure. The image packet catalog covers the complete retained images and marks the one remote watercourse model as a fragment.
