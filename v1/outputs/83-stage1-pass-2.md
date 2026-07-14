# S83 Stage 1 Pass 2

Assigned passage: S83

Sacred Arabic text source: `resources/quran/surah_83.json`

Prompt: `v1/prompts/stage1.md`

## Root Cause Of Pass 1 Limitation

Pass 1 visited too few words per finding because I compressed the sweep around the most obvious convergence lanes after discovering that the specified SQLite primary-source files were not usable in this workspace. `resources/qac.sqlite` and `resources/furuq_v4.sqlite` were absent as populated databases; opening them with `sqlite3` created empty placeholders, which I removed. The local materialized equivalents available in the workspace were `resources/qac_root_ayah.tsv`, `resources/v4_branches.tsv`, and `resources/attachments.tsv`. In Pass 1 I used those rows, but I did not preserve a seed-level audit for every rooted occurrence and every accepted branch. This Pass 2 corrects that by restarting from the first rooted word, `83:1 مُطَفِّفِينَ / ط ف ف`, and treating every rooted occurrence, repeated rooted occurrence, construction, and temporal pattern as seeded.

Operational source caveat: the expected SQLite query layer was unavailable; this file cites the local TSV rows used as the only available source rows for QAC-like root/occurrence data and v4 branch dossiers. No translation was used as evidence.

## Sweep Inventory

Rooted root-ayah rows inspected from `resources/qac_root_ayah.tsv`: 99. The lexical coverage catalog has 100 table entries because the repeated `ق ل ب` row in 83:31 is split by its two word positions for temporal seeding, while the paired `ن ف س` forms in 83:26 remain one constructional occurrence.

Distinct passage roots inspected: 68.

Accepted root-branch dossiers inspected from `resources/v4_branches.tsv`: 564 distinct root branches. For repeated occurrences, the same root branch was restarted in the later occurrence context.

Attachment rows inspected from `resources/attachments.tsv`: S83:1-36 only.

Opening basmala: present in the sacred text file as recitational opening context; no basmala seed was initiated.

## Candidate Synthesis Units

### S83-S1-001: The Short Measure That Becomes A Public Deficit

- `candidate_id`: S83-S1-001
- `ayah_range`: 83:1-6
- `seed_type`: lexical
- `seed`: 83:1 `مُطَفِّفِينَ`, root `ط ف ف`, seed branch `B003 إنقاص الكيل والميزان`
- `generating_set`: `(E: ط ف ف B003)` shortage in measure; `(E: ك ي ل B001)` measuring food by a measure; `(E: و ف ي B001)` full completion without shortage; `(E: خ س ر B003)` making loss in measure/weight; `(E: و ز ن B001)` weighing by scale; `(E: و ز ن B002)` scale as justice/equity.
- `selected_branches`: `ط ف ف B003`, `ك ي ل B001`, `و ف ي B001`, `خ س ر B003`, `و ز ن B001/B002`, later `ب ع ث B001/B002`, `ق و م B002/B013`, `ي و م B003`, `ر ب ب B001/B002`.
- `constructed_model`: A person manipulates the rim of an exchange: when receiving, the vessel is brought to full completion; when giving, the measure/weight is made deficient. The image starts as tiny loss at the edge of a measure, then expands into an accountability scene where the hidden marginal deficit is raised into a public standing before the owner/master of all domains.
- `freeze_point`: After 83:3, once the receiving/giving asymmetry has been built from `ط ف ف`, `ك ي ل`, `و ف ي`, `خ س ر`, and `و ز ن`.
- `predictions_at_freeze`: The passage should expose a compensating scale larger than private trade; the private deficit should be moved into a public setting; the hidden smallness should be made great; the parties affected by measuring should reappear as a collective; authority should be introduced.
- `unused_features_tested`: 83:4 resurrection; 83:5 great day; 83:6 people standing; `لرب العالمين`; attachments for `على الناس`, object suffixes in `كالوهم/وزنوهم`, and adverbial `إذا`.
- `corroborators`: `(C: ب ع ث B001)` stirring from inertness suits bringing hidden acts out of dormancy; `(C: ب عث B002)` dispatch/being raised; `(C: ق و م B002)` bodily standing; `(C: ق و م B013)` resurrection/standing of the hour; `(C: ي و م B003)` severe event-day; `(C: ع ظ م B001/B004)` magnitude/severe calamity; `(C: ر ب ب B001)` sovereign owner/master; `(C: ر ب ب B002)` one who repairs/completes, answering the corrupted completion of measures; `(C: attachment 83:2 a1)` `على الناس` marks the social party over whom the measuring is practiced; `(C: attachment 83:3 a1/a3)` object suffixes mark the victims of giving by measure/weight.
- `constraints`: `(K: ط ف ف B001)` mere smallness alone is insufficient without the measured-exchange construction; `(K: ط ف ف B002)` rim/near-fullness is only an image support, not the primary charge; `(K: ك ي ل B002-B006)` fire-drill, rear rank, horse rivalry, comparison, and blood-equality branches terminate locally; `(K: ن و س B001/B002)` human group in the passage is QAC `ن و س`, but its branch dossier gives swaying/selling-camels and does not generate the model.
- `temporal_reactivation_notes`: The first word gives an apparently small trade fault. 83:2-3 unfolds the asymmetric pattern. 83:4-6 reactivates the small deficit as a matter of resurrection and standing; the listener retrospectively sees the measure as a preview of later measure.
- `rival_models`: A commercial-only model remains possible but weaker because it cannot explain the immediate movement to resurrection, day, standing, and Lord of worlds. A rim/edge image from `ط ف ف B002` is useful but secondary.
- `grade`: strong
- `grade_rationale`: Multiple independent channels converge: lexical measure/weight/fullness/loss, repeated conditional syntax, object marking, public resurrection, day-magnitude, and authority. The candidate explains sequence and reactivation better than a static theme of fraud.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` rows 83:1-6; `v4_branches.tsv` roots `ط ف ف`, `ك ي ل`, `و ف ي`, `خ س ر`, `و ز ن`, `ب ع ث`, `ق و م`, `ي و م`, `ع ظ م`, `ر ب ب`, `ن و س`; `attachments.tsv` S83:1-6.

### S83-S1-002: The Ledger Sent Down Into Confinement

- `candidate_id`: S83-S1-002
- `ayah_range`: 83:7-9, with forward contrast at 83:18-20
- `seed_type`: verified composite
- `seed`: `كِتَابَ ٱلْفُجَّارِ لَفِى سِجِّينٍ`
- `generating_set`: `(E: ك ت ب B003)` fixed decree/record imposing judgment; `(E: ك ت ب B002)` written object; `(E: ف ج ر B004)` deviation from truth and breach of covering; `(E: س ج ن B001)` confinement in a holding place; `(E: ر ق م B001)` marked/inscribed record.
- `selected_branches`: `ك ت ب B002/B003/B004`, `ف ج ر B001/B004/B006`, `س ج ن B001`, `ر ق م B001/B003/B006`, `د ر ي B001`.
- `constructed_model`: A moral breach becomes an inscribed record, and the record is not merely written but located inside confinement. The image is not "sin equals prison" as a flat metaphor; it is a document-bearing identity being placed in a holding register, where the written mark fixes the status.
- `freeze_point`: After 83:7 before the formulaic 83:8-9 explanation.
- `predictions_at_freeze`: Expect intensification of the unknown place; expect the record to be clarified as marked/written; expect a parallel opposite later; expect enclosure/placement to be structurally important.
- `unused_features_tested`: 83:8 `وما أدراك`; 83:9 `كتاب مرقوم`; later exact parallel 83:18-20; attachment rows for `كتاب الفجار` idafa and `لفي سجين` locative predicate.
- `corroborators`: `(C: د ر ي B001)` knowledge formula marks the location as beyond ordinary knowing; `(C: ر ق م B001)` written/marked register supplies the predicted inscription; `(C: attachment 83:7 a2)` idafa ties record to the immoral group; `(C: attachment 83:7 a3/a4)` `في سجين` is locative predicate; `(C: sequence 83:18-20)` same book-marking formula reappears in elevated counterpart.
- `constraints`: `(K: ك ت ب B001)` generic joining is too broad unless constrained by record/decree branches; `(K: ف ج ر B001/B002/B005)` water-burst, dawn, and generosity branches do not fit this local record except as weak secondary contrast to moral rupture; `(K: ر ق م B003-B006)` ornament/animal marks/ground marks/calamity marks remain secondary and do not replace the written-record role.
- `temporal_reactivation_notes`: The listener hears record plus immoral group plus confinement, then the formula asks what could make the listener know the place, then `كتاب مرقوم` reactivates `كتاب` as fixed inscription rather than a loose "book."
- `rival_models`: A spatial-prison model seeded from `س ج ن B001` is viable but must be narrowed by the repeated `كتاب مرقوم`; a mere "written fate" model lacks the downward enclosure.
- `grade`: strong
- `grade_rationale`: The candidate has exact structural support: idafa group identity, locative `في`, repeated explanatory formula, and later antithetical parallel.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` rows 83:7-9 and 83:18-20; `v4_branches.tsv` roots `ك ت ب`, `ف ج ر`, `س ج ن`, `ر ق م`, `د ر ي`, `ع ل و`, `ب ر ر`; `attachments.tsv` S83:7-9, 18-20.

### S83-S1-003: Denial As Boundary-Crossing That Coats The Heart

- `candidate_id`: S83-S1-003
- `ayah_range`: 83:10-17
- `seed_type`: lexical
- `seed`: 83:10/11/12/17 `ك ذ ب`, seed branch `B002 نسبة الشيء أو صاحبه إلى الكذب`
- `generating_set`: `(E: ك ذ ب B002)` active denial/imputation of falsehood; `(E: د ي ن B002)` reckoning/judgment; `(E: ع د و B001)` boundary-crossing injustice; `(E: ء ث م B001)` lagging from good; `(E: ت ل و B001)` recited following sequence; `(E: س ط ر B002)` calling it false old tales; `(E: ر ي ن B002/B003)` an overcoating condition from which there is no exit or a settled covering; `(E: ق ل ب B001)` heart/faculty of understanding; `(E: ك س ب B001)` acquired acts.
- `selected_branches`: `ك ذ ب B001/B002`, `د ي ن B002`, `ع د و B001/B004`, `ء ث م B001/B003`, `ء ي ي B003`, `ت ل و B001/B009`, `س ط ر B001/B002`, `ق و ل B001/B005`, `ر ي ن B002/B003`, `ق ل ب B001/B004/B016`, `ك س ب B001`, `ح ج ب B001/B002`, `ص ل ي B003`, `ج ح م B001`, `ق و ل B001`.
- `constructed_model`: Denial of judgment is not a bare opinion. It is a repeated act of false-ascription that belongs to a boundary-crossing, delayed-from-good subject. When signs are sequentially recited, the denier labels them old scripted tales; accumulated acquisition then becomes a covering over the heart, which later becomes a barrier from the Lord and direct exposure to the fire whose reality had been denied.
- `freeze_point`: After 83:14, once denial, transgression, recited signs, false labeling, earning, and heart-cover are assembled.
- `predictions_at_freeze`: Expect separation from the source of truth; expect the denied object to be presented back; expect a movement from inner covering to outer barrier; expect speech to reverse into speech against the deniers.
- `unused_features_tested`: 83:15 veiling from Lord; 83:16 exposure to fire; 83:17 quoted statement `هذا الذي كنتم به تكذبون`; attachment rows for recitation upon him, quoted complement, `ران على قلوبهم`, relative object `ما كانوا يكسبون`, `عن ربهم`.
- `corroborators`: `(C: ح ج ب B001/B002)` denied access/barrier externally realizes the internal coating; `(C: ص ل ي B003)` actual meeting/entering fire supplies consequence; `(C: ج ح م B001)` intense fire; `(C: ق و ل B001)` later passive saying revoices judgment against them; `(C: attachment 83:14 a1)` `على قلوبهم` makes the covering superimposed on hearts; `(C: attachment 83:17 a1/a4)` the quote points back to the denied object.
- `constraints`: `(K: ك ذ ب B003-B009)` obligation idiom, battle charge, delay, milk ceasing, animal stopping, lying soul, and deceptive cloth do not locally generate the denial model; `(K: ر ي ن B004/B005)` nausea and herd-loss branches terminate except as remote affect; `(K: س ط ر B004/B006/B007)` cutting, mistake, and goat branches terminate.
- `temporal_reactivation_notes`: The passage first announces doom for deniers, then defines the denial object as the day of reckoning, then shows the denier's recurring response to recitation, then discloses the hidden cause: acquired matter coating hearts. Later veiling and fire reactivate the internal cover as an external separation and encounter.
- `rival_models`: A pure speech-falsehood model is weaker because it does not account for `معتد أثيم`, heart covering, and veiling. A heart-disease model from `ر ي ن` alone is also weaker because it misses the denial/recitation sequence.
- `grade`: strong
- `grade_rationale`: This candidate is supported by repeated `ك ذ ب`, explicit `يوم الدين`, exception restriction, character terms, recitation and quote syntax, heart attachment, and consequence sequence.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` rows 83:10-17; `v4_branches.tsv` roots `ك ذب`, `د ي ن`, `ع د و`, `ء ث م`, `ء ي ي`, `ت ل و`, `س ط ر`, `ق و ل`, `ر ي ن`, `ق ل ب`, `ك س ب`, `ح ج ب`, `ص ل ي`, `ج ح م`; `attachments.tsv` S83:10-17.

### S83-S1-004: The Opposite Ledger Lifted Into Near Witness

- `candidate_id`: S83-S1-004
- `ayah_range`: 83:18-21
- `seed_type`: verified composite
- `seed`: `كِتَابَ ٱلْأَبْرَارِ لَفِى عِلِّيِّينَ`
- `generating_set`: `(E: ب ر ر B001)` truthfulness/nondishonesty; `(E: ب ر ر B002)` broad goodness/obedience; `(E: ك ت ب B003)` fixed decree/record; `(E: ع ل و B001/B002)` elevation and honor; `(E: ر ق م B001)` marked writing.
- `selected_branches`: `ب ر ر B001/B002/B008`, `ك ت ب B002/B003/B004`, `ع ل و B001/B002/B005`, `د ر ي B001`, `ر ق م B001`, `ش ه د B001/B002/B008`, `ق ر ب B001/B004/B005`.
- `constructed_model`: The record of the upright is fixed in an elevated register. Unlike the lower confinement of the immoral record, this record is lifted into a high domain and becomes attended or witnessed by those brought near. The image turns moral straightness and truthful completion into upward placement and visible certification.
- `freeze_point`: After 83:18, before the `وما أدراك` formula and `كتاب مرقوم`.
- `predictions_at_freeze`: Expect the same marking as the lower ledger; expect witnesses or attendants because high placement invites access/control; expect nearness; expect a later visual scene.
- `unused_features_tested`: 83:19-21 formula, marked book, witnessing by near ones; later 83:22-28 pleasure scene; contrast with 83:7-9.
- `corroborators`: `(C: ر ق م B001)` repeated marked book; `(C: ش ه د B001/B002)` presence plus testimony; `(C: ق ر ب B004)` the specially near; `(C: ع ل و B005)` upper domain; `(C: attachment 83:21 a1/a2)` object witnessed and subject `المقربون`.
- `constraints`: `(K: ب ر ر B005-B007)` land/wheat/arak-fruit branches terminate in this record setting; `(K: ع ل و B003)` arrogant elevation is a rival but constrained by `الأبرار` and `المقربون`; `(K: ش ه د B006/B007)` birth matter and honey-in-wax terminate locally.
- `temporal_reactivation_notes`: The listener recognizes the lower ledger formula and expects a counterpart. `عليين` reactivates `سجين` by contrast; `كتاب مرقوم` reactivates the fixed record; `يشهده المقربون` adds public attendance rather than hidden confinement.
- `rival_models`: A mere "paradise above" model is too broad; the better model is a mirrored register with witness access.
- `grade`: strong
- `grade_rationale`: The repeated formula with exact opposition, record marking, locative predicate, and witness subject gives strong independent corroboration.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` rows 83:18-21; `v4_branches.tsv` roots `ب ر ر`, `ك ت ب`, `ع ل و`, `د ر ي`, `ر ق م`, `ش ه د`, `ق ر ب`; `attachments.tsv` S83:18-21.

### S83-S1-005: Visible Ease On Faces From Contained Blessing

- `candidate_id`: S83-S1-005
- `ayah_range`: 83:22-24 and 83:35
- `seed_type`: constructional
- `seed`: `إِنَّ ٱلْأَبْرَارَ لَفِى نَعِيمٍ` plus `على الأرائك ينظرون`
- `generating_set`: `(E: ب ر ر B002)` goodness/obedience; `(E: ن ع م B001/B002)` good condition, blessing, soft ease; `(E: ء ر ك B004)` couches in canopies; `(E: ن ظ ر B001)` directed seeing; `(E: ع ر ف B003)` recognition from a mark; `(E: و ج ه B001)` face/front; `(E: ن ض ر B001)` radiance/freshness.
- `selected_branches`: `ن ع م B001/B002/B013`, `ء ر ك B003/B004`, `ن ظ ر B001/B004`, `ع ر ف B003/B013`, `و ج ه B001/B003/B006`, `ن ض ر B001`, plus `ب ر ر B001/B002`.
- `constructed_model`: The upright are not merely given an abstract reward; they are inside a state of ease whose effects become visible. Elevated couches give settled vantage, looking gives outward perception, and the face becomes a readable surface carrying the freshness of the very bliss in which they are contained.
- `freeze_point`: After 83:23, once containment in blessing and viewing from couches are constructed.
- `predictions_at_freeze`: Expect the state to become externally recognizable; expect faces or appearance; expect brightness/freshness; expect later repetition of couches/looking in the reversal.
- `unused_features_tested`: 83:24 `تعرف في وجوههم نضرة النعيم`; 83:35 repeated `على الأرائك ينظرون`; attachment rows for `في نعيم`, `على الأرائك`, `في وجوههم`, `نضرة النعيم`.
- `corroborators`: `(C: ع ر ف B003)` recognizing by sign; `(C: و ج ه B001)` face as visible surface; `(C: ن ض ر B001)` radiant freshness; `(C: attachment 83:24 a1-a4)` recognition occurs in faces and the object is the freshness of blessing; `(C: repetition 83:35)` same couch-looking construction closes the reversal.
- `constraints`: `(K: ء ر ك B001/B002/B006/B007)` arak tree/camels/place branches terminate; `(K: ن ع م B005-B009)` livestock/ostrich/wind branches terminate; `(K: و ج ه B010-B015)` birth, rhyme, striking, rejecting, two-faced branches terminate.
- `temporal_reactivation_notes`: After the high record is witnessed, the passage moves to embodied bliss. The later social reversal returns the believers to the same `على الأرائك ينظرون`, reactivating the earlier settled vantage as a position from which they now observe the reversed mockers.
- `rival_models`: A garden-pastoral model seeded from livestock/wind branches of `ن ع م` is weak; it does not explain couches, looking, and face-recognition as tightly.
- `grade`: medium-strong
- `grade_rationale`: Strong syntax and repeated construction, with good lexical fit. It is local rather than whole-surah governing.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` rows 83:22-24, 35; `v4_branches.tsv` roots `ب ر ر`, `ن ع م`, `ء ر ك`, `ن ظ ر`, `ع ر ف`, `و ج ه`, `ن ض ر`; `attachments.tsv` S83:22-24, 35.

### S83-S1-006: Sealed Drink From A High Source As Desirable Completion

- `candidate_id`: S83-S1-006
- `ayah_range`: 83:25-28
- `seed_type`: verified composite
- `seed`: `رحيق مختوم` / `ختامه مسك` / `مزاجه من تسنيم`
- `generating_set`: `(E: س ق ي B001)` giving drink; `(E: ر ح ق B001)` pure selected wine; `(E: خ ت م B001)` final completion/seal; `(E: خ ت م B002/B003)` sealing mark and secure closure; `(E: م س ك B001)` holding/retaining; `(E: م ز ج B001)` mixture; `(E: س ن م B001/B002)` height/raised source; `(E: ع ي ن B006)` flowing spring; `(E: ش ر ب B001/B002)` drinking/portion; `(E: ق ر ب B004)` the near elite.
- `selected_branches`: `س ق ي B001/B002`, `ر ح ق B001`, `خ ت م B001/B002/B003`, `م س ك B001/B004/B005`, `ن ف س B010`, `م ز ج B001`, `س ن م B001/B002/B004`, `ع ي ن B006/B014`, `ش ر ب B001/B002/B004`, `ق ر ب B004/B005`.
- `constructed_model`: A completed sealed drink is held intact, then its closure is identified with musk and its mixture with a high source. The reward image is a controlled opposite of fraudulent measuring: here completion is preserved, the seal is fragrant, and the desirable object invites rightful competition.
- `freeze_point`: After 83:26 `ختامه مسك وفي ذلك فليتنافس المتنافسون`.
- `predictions_at_freeze`: Expect a source for the mixture; expect height or special origin; expect drinking by an entitled group; expect competition to be over something truly valuable, not stolen.
- `unused_features_tested`: 83:27 `مزاجه من تسنيم`; 83:28 `عينا يشرب بها المقربون`; earlier measuring/fullness contrast; attachments for source prepositions and subject.
- `corroborators`: `(C: ن ف س B010)` valuable thing in which selves compete; `(C: م ز ج B001)` mixture; `(C: س ن م B001/B002)` elevation/high crest; `(C: ع ي ن B006)` spring source; `(C: ش ر ب B001)` actual drinking; `(C: ق ر ب B004)` special near recipients; `(C: attachment 83:27 a2/a3)` mixture is from `تسنيم`; `(C: attachment 83:28 a1-a3)` spring is described by drinking through/from it by the near.
- `constraints`: `(K: خ ت م B004-B007)` first irrigation, silence, hidden horse-white, polished nut branches terminate; `(K: م س ك B002)` stingy holding is a rival but constrained by generosity of being given drink; `(K: س ق ي B010)` forced unpleasant drinking is a contrast, not generator here; `(K: ش ر ب B007)` color/heart mixing is secondary only.
- `temporal_reactivation_notes`: The opening trade unit made completion a stolen asymmetry. Here completion is gifted, sealed, fragrant, and sourced from above. `فليتنافس` reactivates acquisition/desire but redirects it to a rightful object.
- `rival_models`: A purely sensory drink image is viable but misses the reactivation of completion/seal/competition against the measuring fraud. A birth/water/body model from remote branches is weak and terminates.
- `grade`: medium-strong
- `grade_rationale`: The drink sequence is tightly lexical and syntactic. The whole-surah contrast with fraudulent completion is strong but inferential, so below "strong."
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` rows 83:25-28; `v4_branches.tsv` roots `س ق ي`, `ر ح ق`, `خ ت م`, `م س ك`, `ن ف س`, `م ز ج`, `س ن م`, `ع ي ن`, `ش ر ب`, `ق ر ب`; `attachments.tsv` S83:25-28.

### S83-S1-007: Mockery As Passing Social Pressure Reversed Into Judgment

- `candidate_id`: S83-S1-007
- `ayah_range`: 83:29-36
- `seed_type`: temporal/acoustic and lexical
- `seed`: repeated conditional social actions from `إِنَّ الذين أجرموا...` through final `هل ثوب...`
- `generating_set`: `(E: ج ر م B004)` crime/guilt; `(E: ء م ن B001/B002)` secure believing/heart-certainty; `(E: ض ح ك B001/B002)` laughter and laughing-at; `(E: م ر ر B001/B002)` passing and repeated occurrence; `(E: غ م ز B002/B003)` covert signaling and faulting; `(E: ق ل ب B005)` return/inversion to destination; `(E: ء ه ل B001)` close household; `(E: ف ك ه B001/B003/B006)` self-pleased merriment/joking; `(E: ر ء ي B001)` seeing; `(E: ق و ل B001)` saying; `(E: ض ل ل B001)` misguidance label; `(E: ح ف ظ B001)` guardianship; `(E: ر س ل B001/B002)` being sent; `(E: ك ف ر B003)` denial/covering truth; `(E: ث و ب B001/B002)` return/recompense of action; `(E: ف ع ل B001)` performed acts.
- `selected_branches`: `ج ر م B003/B004`, `ء م ن B001/B002`, `ض ح ك B001/B002/B003`, `م ر ر B001/B002`, `غ م ز B002/B003`, `ق ل ب B004/B005`, `ء ه ل B001/B004`, `ف ك ه B001/B003/B006/B007`, `ر ء ي B001/B012/B013`, `ق و ل B001/B005`, `ض ل ل B001/B002/B004`, `ر س ل B001/B002`, `ح ف ظ B001/B004`, `ك ف ر B001/B003`, `ي و م B003`, `ء ر ك B004`, `ن ظ ر B001`, `ث و ب B001/B002`, `ف ع ل B001`.
- `constructed_model`: The criminals repeatedly pass by believers, laughing, signaling covertly, returning to their people amused, and labeling believers astray. The passage then denies that they were sent as guardians over believers. On the decisive day the direction of laughter reverses: believers, now on couches looking, laugh from the stable vantage, and the final question frames the scene as the return of what the deniers had been doing.
- `freeze_point`: After 83:33, before `فاليوم`.
- `predictions_at_freeze`: Expect reversal of subject/object roles; expect the mocked group to receive vantage; expect the mockers' acts to return upon them; expect the final closure to name recompense or return.
- `unused_features_tested`: 83:34-36, repeated `ضحك`, repeated `على الأرائك ينظرون`, `هل ثوب`, `ما كانوا يفعلون`; attachment rows for `من الذين آمنوا`, `بهم`, `إلى أهلهم`, quoted label, guardianship, `من الكفار`, passive recompense and retained object.
- `corroborators`: `(C: ض ح ك B001/B002)` exact repeated laughter with reversed source/target; `(C: ي و م B003)` decisive day; `(C: ء ر ك B004 + ن ظ ر B001)` earlier reward-vantage returns as judgment-vantage; `(C: ث و ب B001/B002)` returning/repaying action; `(C: ف ع ل B001)` what they used to do; `(C: attachment 83:36 a1-a4)` passive subject `الكفار` and object `ما كانوا يفعلون` make recompense explicit.
- `constraints`: `(K: ض ح ك B005-B011)` road, sparkle, plant splitting, overflowing, white honey/snow, animal sound are secondary or terminate; `(K: غ م ز B001/B004)` hand-pressing and animal foot branches are too physical unless subordinated to signaling; `(K: ح ف ظ B002/B003/B006/B007)` memory, perseverance, honor, road branches do not generate guardianship here; `(K: ر س ل B003-B011)` easy gait, milk, women, trinket branches terminate.
- `temporal_reactivation_notes`: The repeated `وإذا` actions create a social loop: pass, signal, return, see, say. `فاليوم` breaks the loop and reverses the gaze. The earlier couch-looking scene from 83:23 is reactivated at 83:35 as the place from which believers observe the recompense.
- `rival_models`: A simple "mockery punished by mockery" model is weaker than the fuller reversal model because it misses repeated passing, covert signaling, claimed guardianship, and the final return/recompense root.
- `grade`: strong
- `grade_rationale`: Exact repetition, reversal of participants, final recompense root, and reactivation of earlier couch-looking make this one of the strongest temporal candidates.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` rows 83:29-36; `v4_branches.tsv` roots `ج ر م`, `ء م ن`, `ض ح ك`, `م ر ر`, `غ م ز`, `ق ل ب`, `ء ه ل`, `ف ك ه`, `ر ء ي`, `ق و ل`, `ض ل ل`, `ر س ل`, `ح ف ظ`, `ك ف ر`, `ي و م`, `ء ر ك`, `ن ظ ر`, `ث و ب`, `ف ع ل`; `attachments.tsv` S83:29-36.

### S83-S1-008: Covering Above, Covering Below

- `candidate_id`: S83-S1-008
- `ayah_range`: 83:14-17 and 83:34-36
- `seed_type`: lexical
- `seed`: root `ك ف ر`, especially 83:34/36 `الكفار`
- `generating_set`: `(E: ك ف ر B001)` covering; `(E: ك ف ر B003)` covering/denying truth; `(E: ك ذ ب B002)` active denial; `(E: ر ي ن B002/B003)` covering settled on hearts; `(E: ح ج ب B001/B002)` being barred/veiled; `(E: ث و ب B002)` recompense.
- `selected_branches`: `ك ف ر B001/B003/B004/B009`, `ك ذ ب B001/B002`, `ر ي ن B002/B003`, `ق ل ب B001`, `ح ج ب B001/B002`, `ث و ب B001/B002`.
- `constructed_model`: The denier's truth-covering is mirrored by a heart-cover, then by being covered off from the Lord. At the close, the covered/denying group is exposed to recompense under the gaze of those they covered over with ridicule.
- `freeze_point`: After 83:15 when inner coating has become separation.
- `predictions_at_freeze`: Expect exposure or recompense; expect the covered truth to return visibly; expect the deniers' label to become their own named identity.
- `unused_features_tested`: 83:17 quoted deictic `هذا`; 83:34-36 final `الكفار`, laughter reversal, recompense.
- `corroborators`: `(C: ك ف ر B003)` denial of truth labels the final group; `(C: ث و ب B002)` recompense returns action; `(C: ن ظ ر B001)` believers look, so hidden truth is now visible; `(C: ق و ل B001)` "this is what you denied" explicitly exposes the covered referent.
- `constraints`: `(K: ك ف ر B008-B015)` farmer, fruit-cover, camphor, village, mountain, submission, crown branches terminate locally; `(K: ك ف ر B009)` covering sin can only be a contrast because the passage is condemning denial, not erasing sin.
- `temporal_reactivation_notes`: `كلا بل ران` introduces coating before `كفار` is named at the end. The final naming reactivates the earlier unseen covering logic.
- `rival_models`: If seeded only from `ك ف ر B003`, the candidate is a conventional denial model; the stronger but more secondary version ties it to covering layers.
- `grade`: medium
- `grade_rationale`: Lexically coherent and temporally useful, but much of the model depends on inferential overlap between covering, denial, rān, and ḥijāb.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` rows 83:14-17, 34-36; `v4_branches.tsv` roots `ك ف ر`, `ك ذب`, `ر ي ن`, `ق ل ب`, `ح ج ب`, `ث و ب`, `ن ظ ر`, `ق و ل`.

### S83-S1-009: Knowledge Formulas As Thresholds For Hidden Registers

- `candidate_id`: S83-S1-009
- `ayah_range`: 83:8-9 and 83:19-20
- `seed_type`: constructional
- `seed`: repeated `وما أدراك ما...`
- `generating_set`: `(E: د ر ي B001)` knowing/informing; `(E: س ج ن B001)` hidden confinement; `(E: ع ل و B001/B002)` high domain; `(E: ك ت ب B002/B003)` written/fixed register; `(E: ر ق م B001)` marked inscription.
- `selected_branches`: `د ر ي B001`, `س ج ن B001`, `ع ل و B001/B002/B005`, `ك ت ب B002/B003`, `ر ق م B001`.
- `constructed_model`: The repeated formula marks two register-locations as beyond immediate ordinary access. Each threshold question is answered by a marked record, so knowing is not mere information; it is entry into the status of the hidden register.
- `freeze_point`: After first formula 83:8.
- `predictions_at_freeze`: Expect the second register to use the same epistemic threshold; expect answer by record/marking; expect mirror contrast.
- `unused_features_tested`: 83:19-20; attachment rows for embedded question; book-mark formula.
- `corroborators`: `(C: repetition)` exact formula repeats; `(C: ر ق م B001)` answer is written marking both times; `(C: ع ل و versus س ج ن)` vertical opposition.
- `constraints`: `(K: د ر ي B002-B004)` aiming/guided hunting and sharp comb/horn branches produce vivid but unsupported images; no local hunt or pointed instrument roles are supplied.
- `temporal_reactivation_notes`: The first knowledge threshold trains the listener to expect hidden registry explanation; the second threshold reactivates and reverses it.
- `rival_models`: Formulaic-rhetorical model only; it is true but less explanatory of why two hidden locations are paired with marked books.
- `grade`: medium-strong
- `grade_rationale`: Excellent constructional repetition, but lexical depth mostly comes from neighboring roots rather than `د ر ي` itself.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` rows 83:8-9, 19-20; `attachments.tsv` formula rows.

### S83-S1-010: Failed Pastoral/Animal And Body Forks

- `candidate_id`: S83-S1-010
- `ayah_range`: whole surah, scattered root dossiers
- `seed_type`: lexical
- `seed`: remote animal/body/plant branches across many roots
- `generating_set`: attempted seeds include `ن و س B002`, `ء ر ك B001/B002/B006`, `ب ر ر B006/B007`, `ر ب ب B008/B014`, `س ق ي B003/B007/B008`, `س ن م B002/B003/B004`, `ش ر ب B014`, `ع ي ن B010`, `ن ع م B005-B009`, `ق ر ب B008/B009/B12-B15`, `ص ل ي B006/B010`, `م س ك B010/B011`, `و ج ه B010`, `ر ء ي B010`, `ف ك ه B004`, `ح ج ب B010`.
- `selected_branches`: none retained as primary generators.
- `constructed_model`: A possible animal/pastoral/body-birth ecology can be imagined: grazing, water sources, humps/high places, near birth, body membranes, faces, and drinking. But the passage supplies no stable animals, birth event, pasture management, or body mechanism tying these branches into the moral/legal sequence.
- `freeze_point`: Each fork freezes locally after failing to attach to a passage construction.
- `predictions_at_freeze`: Would require explicit livestock, birth, body, pasture, or physical medical roles.
- `unused_features_tested`: Whole-surah sequence; measure fraud; ledgers; heart covering; drink; mockery reversal.
- `corroborators`: weak `(C: drink sequence 83:25-28)` supports water/drink only, not the animal/body ecology.
- `constraints`: `(K: no textual animal participant)`, `(K: no birth event)`, `(K: no pasture/field syntax)`, `(K: moral/legal sequence dominates)`.
- `temporal_reactivation_notes`: These branches do not reactivate at closure. They remain lexical noise under the exhaustive control sweep.
- `rival_models`: None retained.
- `grade`: unlikely
- `grade_rationale`: This records terminated avalanches so they are not silently omitted.
- `source_queries_or_rows_used`: all S83 root dossiers listed in the coverage catalog below.

## Constructional And Temporal Seeds

Each construction below was independently seeded after the lexical sweep.

1. `ويل لـ X` at 83:1 and 83:10. Result: local doom-assignment frame. Corroborates two accused groups: short-measurers and deniers. Grade medium-strong.
2. `الذين إذا... يستوفون / وإذا... يخسرون` at 83:2-3. Result: repeated conditional asymmetry; generates S83-S1-001. Grade strong.
3. `ألا يظن أولئك أنهم مبعوثون` at 83:4. Result: cognitive failure to expect being raised; corroborates measurement accountability. Grade medium-strong.
4. `ليوم عظيم / يوم يقوم الناس لرب العالمين` at 83:5-6. Result: public standing before master/repairing authority; corroborates S83-S1-001. Grade strong.
5. `كتاب X لفي Y` at 83:7 and 83:18. Result: mirrored register-locations; generates S83-S1-002 and S83-S1-004. Grade strong.
6. `وما أدراك ما Y` at 83:8 and 83:19. Result: knowledge threshold for hidden register; generates S83-S1-009. Grade medium-strong.
7. `كتاب مرقوم` at 83:9 and 83:20. Result: fixed inscription after threshold; corroborates ledger model. Grade strong.
8. `الذين يكذبون بيوم الدين` at 83:11. Result: denial object is judgment/reckoning day, not generic disbelief. Grade strong.
9. `وما يكذب به إلا كل معتد أثيم` at 83:12. Result: exception restriction maps denial to boundary-crossing character. Grade strong.
10. `إذا تتلى عليه آياتنا قال...` at 83:13. Result: recitation response pattern; expands denial model. Grade strong.
11. `بل ران على قلوبهم ما كانوا يكسبون` at 83:14. Result: acquired coating over heart; generates S83-S1-003. Grade strong.
12. `عن ربهم يومئذ لمحجوبون` at 83:15. Result: externalized barrier from source; corroborates covering model. Grade strong.
13. `ثم إنهم لصالوا الجحيم / ثم يقال...` at 83:16-17. Result: consequence and deictic exposure of denied reality. Grade strong.
14. `يشهده المقربون` at 83:21. Result: high register witnessed by near ones. Grade medium-strong.
15. `إن الأبرار لفي نعيم` at 83:22. Result: containment in ease; starts visible-blessing image. Grade medium.
16. `على الأرائك ينظرون` at 83:23 and 83:35. Result: repeated vantage construction; first bliss, then reversal. Grade strong.
17. `تعرف في وجوههم نضرة النعيم` at 83:24. Result: internal state readable on faces. Grade medium-strong.
18. `رحيق مختوم / ختامه مسك` at 83:25-26. Result: sealed complete drink; generates S83-S1-006. Grade medium-strong.
19. `وفي ذلك فليتنافس المتنافسون` at 83:26. Result: rightful competition for valuable object; reactivates acquisition/desire in corrected form. Grade medium.
20. `مزاجه من تسنيم / عينا يشرب بها المقربون` at 83:27-28. Result: high-source mixture and special drinking access. Grade medium-strong.
21. Social `إذا` chain at 83:30-32. Result: repeated worldly mockery loop. Grade strong.
22. `وما أرسلوا عليهم حافظين` at 83:33. Result: denies mockers' supervisory authority. Grade medium-strong.
23. `فاليوم الذين آمنوا من الكفار يضحكون` at 83:34. Result: reversal day. Grade strong.
24. `هل ثوب الكفار ما كانوا يفعلون` at 83:36. Result: closure as action-return/recompense. Grade strong.

## Lexical Seed Coverage Catalog

Status codes:

- `G` means at least one branch from the rooted occurrence generated or expanded a retained candidate.
- `C` means at least one branch was held unused until after freeze and then corroborated or constrained a retained candidate.
- `L` means a local image was retained but not promoted to a main candidate.
- `T` means all remaining accepted branches for that occurrence terminated after full dossier reading because they lacked passage-local roles.

For each occurrence below, every accepted branch of that root in `v4_branches.tsv` was initiated as a seed in that occurrence context. Branches not named in `G`, `C`, or `L` are `T` for that occurrence.

| Occurrence | Root | Productive branches | Terminated branch policy |
| --- | --- | --- | --- |
| 83:1 `مطففين` | `ط ف ف` | `G:B003`, `C:B001/B002` | `T:B004/B005/B006/B008/B009` |
| 83:2 `اكتالوا` | `ك ي ل` | `G:B001`, `L:B005` | `T:B002/B003/B004/B006` |
| 83:2 `الناس` | `ن و س` | `C:constructional human object only` | `T:B001/B002` |
| 83:2 `يستوفون` | `و ف ي` | `G:B001`, `C:B003/B004 weak` | `T:B002/B005` |
| 83:3 `كالوهم` | `ك ي ل` | `G:B001` | `T:B002/B003/B004/B005/B006` |
| 83:3 `وزنوهم` | `و ز ن` | `G:B001/B002`, `C:B007/B008` | `T:B003/B004/B005/B006` |
| 83:3 `يخسرون` | `خ س ر` | `G:B003`, `C:B001/B002` | `T:B005` |
| 83:4 `يظن` | `ظ ن ن` | `C:B001/B003/B006` | `T:B002/B004/B005/B007/B008/B009` |
| 83:4 `مبعوثون` | `ب ع ث` | `C:B001/B002/B004` | no terminated accepted branch beyond listed |
| 83:5 `يوم` | `ي و م` | `C:B003`, `L:B002` | `T:B001` |
| 83:5 `عظيم` | `ع ظ م` | `C:B001/B004/B007/B010` | `T:B002/B003/B005/B006/B008/B009` |
| 83:6 `يوم` | `ي و م` | `C:B003`, `L:B002` | `T:B001` |
| 83:6 `يقوم` | `ق و م` | `C:B002/B013`, `L:B004/B008/B009/B015/B017` | `T:B001/B003/B006/B007/B010/B011/B012/B014/B016/B018/B019/B020/B021` |
| 83:6 `الناس` | `ن و س` | `C:constructional public group` | `T:B001/B002` |
| 83:6 `رب` | `ر ب ب` | `C:B001/B002`, `L:B011/B016` | `T:B003/B004/B005/B006/B007/B008/B009/B010/B012/B013/B014/B015/B017` |
| 83:6 `العالمين` | `ع ل م` | `C:B001/B002` | `T:B004/B005/B006/B007` |
| 83:7 `كتاب` | `ك ت ب` | `G:B002/B003/B004`, `C:B001` | `T:B005` |
| 83:7 `الفجار` | `ف ج ر` | `G:B004`, `C:B001/B006 weak` | `T:B002/B003/B005` |
| 83:7 `سجين` | `س ج ن` | `G:B001` | no terminated accepted branch |
| 83:8 `أدراك` | `د ر ي` | `C:B001`, `L:B002/B003/B004 failed image` | `T:B002/B003/B004` for main candidates |
| 83:8 `سجين` | `س ج ن` | `C:B001` | no terminated accepted branch |
| 83:9 `كتاب` | `ك ت ب` | `C:B002/B003/B004` | `T:B001/B005` |
| 83:9 `مرقوم` | `ر ق م` | `G:B001`, `L:B003/B006` | `T:B002/B004/B005` |
| 83:10 `مكذبين` | `ك ذ ب` | `G:B001/B002` | `T:B003/B004/B005/B006/B007/B008/B009` |
| 83:11 `يكذبون` | `ك ذ ب` | `G:B001/B002` | `T:B003/B004/B005/B006/B007/B008/B009` |
| 83:11 `يوم` | `ي و م` | `G:B003`, `C:B002` | `T:B001` |
| 83:11 `الدين` | `د ي ن` | `G:B002`, `C:B001/B004/B007` | `T:B003/B005/B006` |
| 83:12 `يكذب` | `ك ذ ب` | `G:B001/B002` | `T:B003/B004/B005/B006/B007/B008/B009` |
| 83:12 `كل` | `ك ل ل` | `C:B003`, `L:B005/B006 weak enclosure` | `T:B001/B002/B004/B007/B008/B009/B011` |
| 83:12 `معتد` | `ع د و` | `G:B001`, `C:B004/B007/B009` | `T:B002/B003/B005/B006/B008/B010/B011/B012` |
| 83:12 `أثيم` | `ء ث م` | `G:B001`, `C:B003/B004` | `T:B002` |
| 83:13 `تتلى` | `ت ل و` | `G:B001`, `L:B009` | `T:B003/B004/B005/B006/B007/B008` |
| 83:13 `آياتنا` | `ء ي ي` | `G:B003`, `C:B002/B004/B006` | `T:B001/B005/B007/B008/B009/B010` |
| 83:13 `قال` | `ق و ل` | `G:B001/B005`, `C:B007/B012/B013/B014` | `T:B002/B003/B004/B006/B008/B009/B010/B011/B015/B016` |
| 83:13 `أساطير` | `س ط ر` | `G:B002`, `C:B001/B003` | `T:B004/B006/B007` |
| 83:13 `الأولين` | `ء و ل` | `C:B001/B002`, `L:B003/B004` | `T:B005/B007/B008/B009/B010` |
| 83:14 `ران` | `ر ي ن` | `G:B002/B003` | `T:B004/B005` |
| 83:14 `قلوبهم` | `ق ل ب` | `G:B001`, `C:B004/B005/B016` | `T:B002/B003/B007/B008/B009/B010/B011/B012/B013/B015` |
| 83:14 `كانوا` | `ك و ن` | `C:B001`, `L:B002/B006` | `T:B003/B004/B005` |
| 83:14 `يكسبون` | `ك س ب` | `G:B001`, `C:B002` | `T:B003/B004` |
| 83:15 `ربهم` | `ر ب ب` | `C:B001/B002` | same root-branch terminations as 83:6 |
| 83:15 `محجوبون` | `ح ج ب` | `G:B001/B002`, `C:B004/B005/B007` | `T:B003/B006/B008/B009/B010/B011/B012` |
| 83:16 `صالوا` | `ص ل ي` | `G:B003`, `C:B004/B007` | `T:B001/B002/B005/B006/B008/B009/B010` |
| 83:16 `الجحيم` | `ج ح م` | `G:B001`, `C:B003/B004` | `T:B002/B005` |
| 83:17 `يقال` | `ق و ل` | `C:B001/B005` | same root-branch terminations as 83:13 |
| 83:17 `كنتم` | `ك و ن` | `C:B001` | same root-branch terminations as 83:14 |
| 83:17 `تكذبون` | `ك ذ ب` | `C:B001/B002` | same root-branch terminations as 83:10 |
| 83:18 `كتاب` | `ك ت ب` | `G:B002/B003/B004` | `T:B001/B005` |
| 83:18 `الأبرار` | `ب ر ر` | `G:B001/B002`, `C:B003/B008` | `T:B004/B005/B006/B007` |
| 83:18 `عليين` | `ع ل و` | `G:B001/B002/B005`, `C:B004/B008/B009` | `T:B003/B006/B010/B011/B012` |
| 83:19 `أدراك` | `د ر ي` | `C:B001` | `T:B002/B003/B004` |
| 83:19 `عليون` | `ع ل و` | `C:B001/B002/B005` | same root-branch terminations as 83:18 |
| 83:20 `كتاب` | `ك ت ب` | `C:B002/B003/B004` | `T:B001/B005` |
| 83:20 `مرقوم` | `ر ق م` | `C:B001` | `T:B002/B003/B004/B005/B006` |
| 83:21 `يشهده` | `ش ه د` | `G:B001/B002/B008` | `T:B005/B006/B007` |
| 83:21 `المقربون` | `ق ر ب` | `G:B001/B004/B005`, `L:B002/B007/B016` | `T:B003/B008/B009/B010/B011/B012/B013/B014/B015` |
| 83:22 `الأبرار` | `ب ر ر` | `G:B001/B002` | same root-branch terminations as 83:18 |
| 83:22 `نعيم` | `ن ع م` | `G:B001/B002`, `C:B013` | `T:B003/B004/B005/B006/B007/B008/B009/B010/B011/B012` |
| 83:23 `الأرائك` | `ء ر ك` | `G:B004`, `C:B003/B005` | `T:B001/B002/B006/B007` |
| 83:23 `ينظرون` | `ن ظ ر` | `G:B001/B004`, `C:B002/B003/B006/B009/B010` | `T:B005/B007/B008` |
| 83:24 `تعرف` | `ع ر ف` | `G:B003/B013`, `C:B001/B002/B004/B005/B009/B010` | `T:B006/B007/B008/B011/B012/B014` |
| 83:24 `وجوههم` | `و ج ه` | `G:B001`, `C:B002/B003/B006/B008` | `T:B007/B009/B010/B011/B012/B013/B014/B015` |
| 83:24 `نضرة` | `ن ض ر` | `G:B001`, `C:B002` | `T:B003` |
| 83:24 `النعيم` | `ن ع م` | `C:B001/B002` | same root-branch terminations as 83:22 |
| 83:25 `يسقون` | `س ق ي` | `G:B001/B002`, `L:B003/B006/B007/B009/B010` | `T:B005/B008` |
| 83:25 `رحيق` | `ر ح ق` | `G:B001` | no terminated accepted branch |
| 83:25 `مختوم` | `خ ت م` | `G:B001/B002/B003` | `T:B004/B005/B006/B007` |
| 83:26 `ختامه` | `خ ت م` | `C:B001/B002/B003` | same root-branch terminations as 83:25 |
| 83:26 `مسك` | `م س ك` | `G:B001/B004/B005`, `L:B003/B009/B012` | `T:B002/B006/B008/B010/B011` |
| 83:26 `يتنافس/المتنافسون` | `ن ف س` | `G:B010`, `C:B001/B006/B008/B011/B012/B013/B014/B015` | `T:B002/B003/B004/B005/B007/B009/B016` |
| 83:27 `مزاجه` | `م ز ج` | `G:B001`, `L:B002/B003/B004/B005` | no full-candidate use for `B002-B005` |
| 83:27 `تسنيم` | `س ن م` | `G:B001/B002/B004`, `L:B003/B005/B007` | no retained primary use for `B003/B005/B007` |
| 83:28 `عيناً` | `ع ي ن` | `G:B006`, `C:B001/B002/B003/B014/B17` | `T:B004/B005/B007/B008/B009/B010/B011/B012/B013/B015/B016` |
| 83:28 `يشرب` | `ش ر ب` | `G:B001/B002/B004`, `C:B006/B007/B009/B011` | `T:B003/B005/B008/B010/B012/B013/B014` |
| 83:28 `المقربون` | `ق ر ب` | `C:B001/B004/B005` | same root-branch terminations as 83:21 |
| 83:29 `أجرموا` | `ج ر م` | `G:B003/B004`, `C:B001/B006/B007/B008` | `T:B002/B009/B010/B011` |
| 83:29 `كانوا` | `ك و ن` | `C:B001` | same root-branch terminations as 83:14 |
| 83:29 `آمنوا` | `ء م ن` | `G:B001/B002`, `L:B003` | no other accepted branch |
| 83:29 `يضحكون` | `ض ح ك` | `G:B001/B002/B003`, `C:B005/B006/B008/B009` | `T:B004/B007/B011` |
| 83:30 `مروا` | `م ر ر` | `G:B001/B002`, `C:B003/B004/B006` | `T:B005/B007/B008` |
| 83:30 `يتغامزون` | `غ م ز` | `G:B002/B003`, `L:B001` | `T:B004` |
| 83:31 `انقلبوا` | `ق ل ب` | `G:B004/B005`, `C:B001/B002` | same remaining terminations as 83:14 |
| 83:31 `أهلهم` | `ء ه ل` | `G:B001/B004`, `C:B003/B005` | `T:B002/B006` |
| 83:31 `انقلبوا` | `ق ل ب` | repeated occurrence, same productive/terminated split as first 83:31 occurrence |
| 83:31 `فكهين` | `ف ك ه` | `G:B001/B003/B006/B007`, `L:B002` | `T:B004` |
| 83:32 `رأوهم` | `ر ء ي` | `G:B001/B012/B013`, `C:B002/B004/B006/B011` | `T:B003/B005/B007/B008/B009/B010` |
| 83:32 `قالوا` | `ق و ل` | `G:B001/B005`, `C:B007/B012/B013` | same remaining terminations as 83:13 |
| 83:32 `ضالون` | `ض ل ل` | `G:B001`, `C:B002/B003/B004` | `T:B005` |
| 83:33 `أرسلوا` | `ر س ل` | `G:B001/B002`, `C:B004/B005/B007/B008/B010` | `T:B003/B006/B009/B011` |
| 83:33 `حافظين` | `ح ف ظ` | `G:B001/B004`, `C:B002/B003/B006/B007` | `T:B005` |
| 83:34 `اليوم` | `ي و م` | `C:B003`, `L:B002` | `T:B001` |
| 83:34 `آمنوا` | `ء م ن` | `G:B001/B002` | `T:B003` |
| 83:34 `الكفار` | `ك ف ر` | `G:B001/B003`, `C:B004/B005/B006/B009` | `T:B002/B007/B008/B010/B011/B012/B013/B014/B015` |
| 83:34 `يضحكون` | `ض ح ك` | `G:B001/B002/B003` | same remaining terminations as 83:29 |
| 83:35 `الأرائك` | `ء ر ك` | `C:B004` | same remaining terminations as 83:23 |
| 83:35 `ينظرون` | `ن ظ ر` | `C:B001/B004` | same remaining terminations as 83:23 |
| 83:36 `ثوب` | `ث و ب` | `G:B001/B002`, `C:B004` | `T:B003/B005` |
| 83:36 `الكفار` | `ك ف ر` | `C:B001/B003` | same remaining terminations as 83:34 |
| 83:36 `كانوا` | `ك و ن` | `C:B001` | same root-branch terminations as 83:14 |
| 83:36 `يفعلون` | `ف ع ل` | `G:B001`, `C:B002/B004/B005` | `T:B003/B007` |

## Root-Level Branch Inventory Used For The Catalog

This inventory records the accepted branch IDs seen for each S83 root. The branch image titles are the `branch_image_ar` values from `resources/v4_branches.tsv`. The fuller `what_is_ar` prose was read as the root dossier before selecting branches for candidate construction.

- `ط ف ف`: `B001 القلة والشيء الطفيف`; `B002 حافة المكيال وما يقارب الامتلاء`; `B003 إنقاص الكيل والميزان`; `B004 الحافة والشاطئ والموضع المشرف`; `B005 الدنو والتهيؤ وظهور الشيء القريب`; `B006 الرفع حتى المحاذاة والمساواة`; `B008 اللحم الرخو المضطرب`; `B009 دفع الشيء بالرجل`.
- `ك ي ل`: `B001 كيل الطعام`; `B002 كال الزند`; `B003 الكيول مؤخر الصف`; `B004 مكايلة الفرس للفرس`; `B005 المكايلة بين أمرين`; `B006 لا تكايل بالدم`.
- `ن و س`: `B001 تذبذب الشيء المتدلي`; `B002 سوق الإبل`.
- `و ف ي`: `B001 التمام الوافي بلا نقص`; `B002 قبض النفس على وجه التوفي`; `B003 البلوغ إلى علو والإشراف منه`; `B004 الموافاة إتيان الموعد والاجتماع عليه`; `B005 الميفى غطاء التنور وبيت الآجر`.
- `خ س ر`: `B001 النقص العام`; `B002 خسارة التجارة`; `B003 إخسار الكيل والميزان`; `B005 الخنسرى والخيسرى والخناسر`.
- `و ز ن`: `B001 تقدير الشيء بوزن أو خرص`; `B002 ميزان العدل والقسط`; `B003 موازنة ومحاذاة بين شيئين`; `B004 قيام ميزان النهار في وسطه`; `B005 رأي وزين ثابت راجح`; `B006 قصر موزون في الجارية أو المرأة`; `B007 قدر ومنزلة لها وزن`; `B008 شيء موزون مخلوق باعتدال`.
- `ب ع ث`: `B001 إثارة الساكن من ركوده`; `B002 إرسال المبعوث وتوجيهه`; `B004 اندفاع القوم ومضيهم`.
- `ظ ن ن`: `B001 يقين بعد أمارة`; `B002 مظنة الشيء وموضعه`; `B003 شك وتوهم`; `B004 تهمة وظنة`; `B005 سوء الظن بالناس`; `B006 أمر لا يوثق بعاقبته`; `B007 ظنين معاد`; `B008 ضعف وقلة حيلة`; `B009 امرأة يرجى ولدها`.
- `ي و م`: `B001 وقت النهار المحدود`; `B002 مدة من الزمان`; `B003 كائنة اليوم وشدته`.
- `ع ظ م`: `B001 الكبر والقوة`; `B002 معظم الشيء`; `B003 مستغلظ العضو`; `B004 العظيمة النازلة`; `B005 العظم الصلب`; `B006 التعاظم والزهو`; `B007 الاستعظام والهيبة`; `B008 عظامة الردف`; `B009 خشبة الرحل`; `B010 الحرمة والشرف`.
- `ق و م`: `B001 جماعة الناس والرجال`; `B002 انتصاب وقيام بالبدن`; `B003 عزم ونهوض إلى الأمر`; `B004 رعاية وحفظ وولاية`; `B006 مقام وإقامة في موضع`; `B007 نيابة وقيام مقام غيره`; `B008 استقامة واعتدال واستواء`; `B009 قوام وعماد ومعاش`; `B010 قيمة وتقويم وتسعير`; `B011 قامة وقوام الجسم والطول`; `B012 آلة قائمة وجزء قائم`; `B013 قيامة وبعث وقيام الساعة`; `B014 مقاومة ومنازلة`; `B015 وزن سواء ومقدار معتدل`; `B016 جمود ووقوف وكلال`; `B017 انتصاف النهار وقائم الظهيرة`; `B018 نفاق السوق`; `B019 وجع قائم بالعضو`; `B020 قوام في قوائم الشاة`; `B021 عين قائمة ذاهبة البصر`.
- `ر ب ب`: `B001 ربوبية وملك وسيادة`; `B002 إصلاح وتربية وإتمام`; `B003 علم رباني`; `B004 ربة وجماعات كثيرة`; `B005 ربيب وربيبة ورابة`; `B006 رب خاثر وإصلاح به`; `B007 لزوم وإقامة ودوام`; `B008 رباب السحاب`; `B009 شاة ربى وحداثة`; `B010 ربابة تجمع القداح`; `B011 ربابة عهد وميثاق`; `B012 ربة نبات`; `B013 ماء ربب كثير`; `B014 ربرب قطيع`; `B015 حرف رب وربما`; `B016 ربى حاجة وعقدة ونعمة`; `B017 رباني الملاحين`.
- `ع ل م`: `B001 انكشاف الشيء للعارف`; `B002 أثر يميز الشيء ويهدي إليه`; `B004 شق ظاهر في الشفة العليا`; `B005 ماء كثير مجتمع في عيلم`; `B006 طائر جارح يسمى العلام`; `B007 ذكر الضباع يسمى العيلام`.
- `ك ت ب`: `B001 ضم شيء إلى شيء`; `B002 نظم الحروف واسم المكتوب`; `B003 إثبات يوجب حكما أو قدرا`; `B004 إدخال الاسم في سجل أو زمرة`; `B005 مكاتبة العبد على عتقه`.
- `ف ج ر`: `B001 انشقاق واسع وانبعاث`; `B002 انبلاج الصبح من الليل`; `B003 اندفاع الكثير بغتة`; `B004 انحراف عن الحق وخرق الستر`; `B005 جود متفجر واسع`; `B006 وقائع الفجار لانتهاك الحرمة`.
- `س ج ن`: `B001 الحبس في موضع يحبس فيه`.
- `د ر ي`: `B001 الدراية والعلم`; `B002 قصد الشيء واعتماده`; `B003 الختل والاستتار للصيد`; `B004 المدرى والحد المحدد`.
- `ر ق م`: `B001 خط مرقوم في كتاب أو سجل`; `B002 حذق كمن يرقم في الماء`; `B003 وشي ونقش ورقشة ظاهرة`; `B004 آثار موسومة في بدن الدابة`; `B005 أثر في أرض أو موضع`; `B006 الداهية ذات الأثر`.
- `ك ذ ب`: `B001 خلاف الصدق`; `B002 نسبة الشيء أو صاحبه إلى الكذب`; `B003 كذب عليك بمعنى الزم وعليك به`; `B004 صدق الحملة أو كذبها`; `B005 ما كذب أن فعل أي ما لبث`; `B006 كذب لبن الناقة إذا ذهب ولم يدم`; `B007 كذب الوحشي إذا جرى ثم وقف`; `B008 النفس الكذوب`; `B009 الكذابة ثوب يكذب بحاله`.
- `د ي ن`: `B001 الطاعة والانقياد`; `B002 الحساب والجزاء`; `B003 الدين المالي`; `B004 الإذلال والملك`; `B005 العادة والشأن`; `B006 مدينة الطاعة`; `B007 التصديق والتفويض`.
- `ك ل ل`: `B001 الكلال وخلاف الحدة`; `B002 الكل عيالا وثقلا`; `B003 الكل إحاطة وتماما`; `B004 الكلالة قرابة عارضة`; `B005 الإكليل وما يحيط`; `B006 الكلة سترا وبيتا`; `B007 الكلكل صدرا`; `B008 الكلكل قصر وغلظ`; `B009 الكلاكل جماعات`; `B011 الانكلال تبسما ولمعا`.
- `ع د و`: `B001 مجاوزة الحد والظلم`; `B002 العدو والحضر`; `B003 العدو والعداوة`; `B004 المجاوزة والاستثناء والصرف`; `B005 العدوى في طلب الإنصاف`; `B006 العدوى في انتقال الداء`; `B007 العوادي والعادية الشاغلة`; `B008 العداء في تعاقب الصيد`; `B009 العداء والعدوة في الجانب والطوار`; `B010 العدواء في صلابة المكان واضطرابه`; `B011 العدوية من نبات الصيف`; `B012 العندأوة في الالتواء والعسر`.
- `ء ث م`: `B001 البطء والتأخر عن الخير`; `B002 التأثم كف عن الإثم`; `B003 الأثام عقوبة الإثم`; `B004 تحميل الإثم وعده عليه`.
- `ت ل و`: `B001 اتباع وتتابع`; `B003 بقية تتلو ما قبلها`; `B004 ذمة أو حق يتبع صاحبه`; `B005 ترك بعد صحبة`; `B006 ولد يتلو أمه`; `B007 صوت يتلو صوتا`; `B008 آخر رمق`; `B009 قول كذب على غيره`.
- `ء ي ي`: `B001 تمهل وانتظار`; `B002 تعمد آية الشخص`; `B003 علامة ظاهرة`; `B004 أي للسؤال والتعيين`; `B005 إيا عماد للضمير`; `B006 أيان للزمان`; `B007 كأين لعدد كثير`; `B008 أي وأيا للنداء`; `B009 أي مفسرة`; `B010 إي افتتاح للقسم`.
- `ق و ل`: `B001 إخراج القول بالنطق`; `B002 اللسان آلة القول`; `B003 كثرة القول في صاحبه`; `B004 القيل صاحب القول النافذ`; `B005 قول ما لم يكن أو نسبته`; `B006 اجترار القول إلى النفس`; `B007 القول الفاشي بين الناس`; `B008 عود القال لضرب القلة`; `B009 المقاولة في الأمر`; `B010 اقتالة الحكم على غيره`; `B011 قول يجري مجرى الظن`; `B012 قول في النفس لم يظهر`; `B013 القول اعتقاد ومذهب`; `B014 قول الشيء دلالته`; `B015 العناية الصادقة بالشيء`; `B016 قول الشيء حده`.
- `س ط ر`: `B001 السطر المصطف المكتوب`; `B002 أساطير الباطل`; `B003 سيطرة الرقيب المتسلط`; `B004 خط الضرب والقطع`; `B006 الإسْطار في الخطأ`; `B007 السطر العتود`.
- `ء و ل`: `B001 ابتداء الشيء وتقدمه`; `B002 رجوع الشيء إلى مآله وعاقبته`; `B003 آل الرجل من يرجع إليهم ويرجعون إليه`; `B004 إيالة الأمر بإصلاحه وسياسته`; `B005 خثور السائل وانعقاده في آخر أمره`; `B007 آلة الحال التي يكون عليها الشيء`; `B008 الآلة الحاملة أو الأداة`; `B009 الأيل الذي يأوي إلى الجبل`; `B010 الإيال وعاء الشراب حتى يجود`.
- `ر ي ن`: `B002 الرين وقوع لا مخرج منه`; `B003 رين النعاس والخمر`; `B004 رين النفس بالغثيان`; `B005 إرانة القوم بهلاك الماشية`.
- `ق ل ب`: `B001 القلب والفؤاد`; `B002 خالص الشيء ولبه`; `B003 قلب النخل والشجر`; `B004 رد الشيء عن وجهه`; `B005 الانصراف والمصير`; `B007 القليب البئر`; `B008 القلب من الأسورة`; `B009 الحية البيضاء المشبهة بالقلب`; `B010 قلب العقرب النجم`; `B011 داء القلب والقلبة`; `B012 انقلاب الشفة`; `B013 القليب والقلوب الذئب`; `B015 القالب البسر الأحمر`; `B016 إصابة القلب`.
- `ك و ن`: `B001 وقوع الشيء وحضوره في زمان`; `B002 المكان والمكانة من الكون`; `B003 الكفالة والقيام على فلان`; `B004 الخضوع بالاستكانة`; `B005 الشيخ المنسوب إلى كنت`; `B006 حالة السوء بكينة`.
- `ك س ب`: `B001 طلب الرزق والنفع وإصابته`; `B002 إكساب غيره خيرا أو مالا`; `B003 الكواسب الجوارح`; `B004 الكسب عصارة الدهن`.
- `ح ج ب`: `B001 منع الوصول`; `B002 ستر حاجز`; `B003 ولاية الحاجب`; `B004 حجاب الجوف`; `B005 حاجب العين`; `B006 رؤوس الوركين`; `B007 حرف الشيء`; `B008 حجب الفريضة`; `B009 عمى محجوب`; `B010 احتجاب الحامل`; `B011 الأجمة الحجيبة`; `B012 أرض حرة`.
- `ص ل ي`: `B001 الصلاة عبادة لازمة`; `B002 الدعاء والبركة والرحمة`; `B003 ملاقاة النار وحرها`; `B004 إيقاد الصلاء وتسوية الشيء بالنار`; `B005 المصالي أشراك وفخوخ`; `B006 الصلا موضع الظهر والذنب`; `B007 المصلي يتلو السابق`; `B008 الصلوات مواضع عبادة`; `B009 الصلاية حجر يدق عليه`; `B010 الصليان نبت ترعاه الإبل`.
- `ج ح م`: `B001 تأجج النار وشدة حرها`; `B002 احتدام الحرب والموت`; `B003 العين المتوقدة أو الجاحظة`; `B004 تلهب الوجه بالغضب`; `B005 قلة الحياء`.
- `ب ر ر`: `B001 صدق يمضي القول والعمل`; `B002 خير وطاعة متسعة`; `B003 صلة وإحسان ضد العقوق`; `B004 صوت وجلبة باللسان`; `B005 يابسة وصحراء`; `B006 حب وحنطة`; `B007 ثمر الأراك`; `B008 غلبة وعلو`.
- `ع ل و`: `B001 السمو والارتفاع`; `B002 الرفعة والشرف`; `B003 العظمة والتجبر`; `B004 الغلبة والاستيلاء`; `B005 الجهة العليا ومن فوق`; `B006 نداء التعالي`; `B008 الشيء المحمول على الأعلى`; `B009 أسماء الأدوات والأجزاء المرتفعة`; `B010 الطول والضخامة`; `B011 السلامة من النفاس أو العلة`; `B012 حرف على وما جرى مجراه`.
- `ش ه د`: `B001 الحضور مع المشاهدة`; `B002 البيان بعلم`; `B005 اللسان الشاهد`; `B006 الخارج عند الولادة والإدراك`; `B007 الشهد في الشمع`; `B008 العلامة الشاهدة`.
- `ق ر ب`: `B001 الدنو وخلاف البعد`; `B002 دنو الزمان وانقضاء الشيء`; `B003 قرابة الرحم والنسب`; `B004 حظوة المقربين وخاصة الملك`; `B005 القربة والقربان إلى الله`; `B007 مقاربة الشيء وملابسته`; `B008 ليلة القرب وطلب الماء`; `B009 القربة وعاء الماء`; `B010 قراب السيف ووعاؤه`; `B011 القارب السفينة الصغيرة`; `B012 دنو الولادة في الحيوان`; `B013 الخيل والإبل المقربة`; `B014 تقريب الفرس في العدو`; `B015 قرب الفرس والخاصرة`; `B016 القراب والمقاربة في المقدار`.
- `ن ع م`: `B001 حسن الحال والنعمة`; `B002 اللين والنعومة ورفاه العيش`; `B003 مدح الشيء بنعم`; `B004 الجواب بنعم والتصديق`; `B005 مال الأنعام والإبل`; `B006 النعام والنعامة الطائر`; `B007 ما سمي نعامة تشبيها بالهيئة`; `B008 طيران النعامة وتفرق القوم`; `B009 النعامى ريح لينة`; `B010 زاد وأنعم في الفعل`; `B011 موافقة المكان وطيب المقام`; `B012 المشي على القدم وابتذالها`; `B013 نعم الله بك عينا وقرة العين`.
- `ء ر ك`: `B001 الأراك شجر معروف للسواك`; `B002 إبل ترعى الأراك وتعتاده`; `B003 اللزوم والإقامة في المكان`; `B004 الأريكة سرير في حجلة`; `B005 سكون الجرح بعد صلاحه`; `B006 شكوى بطون الإبل من أكل الأراك`; `B007 أرك وأريك اسما موضع`.
- `ن ظ ر`: `B001 توجيه البصر أو البصيرة لإدراك الشيء`; `B002 ترقب الوقت وإمهال الطالب`; `B003 تواجه الأشياء حتى يرى بعضها بعضا`; `B004 ظهور الشيء للناظر أو حسن مرآه`; `B005 نظرة الدهر التي تصيب بالهلاك`; `B006 مقابلة المثل بمثله حتى يستويان`; `B007 أثر النظرة في اللون والعيب`; `B008 العين وموضع النظر فيها`; `B009 حارس ينظر ويحفظ`; `B010 تدارس الأمر بالنظر المتبادل`.
- `ع ر ف`: `B001 تتابع متصل كالشعر على عرف الفرس`; `B002 عرف مرتفع ظاهر في الشيء`; `B003 معرفة وتمييز بعد أثر أو علامة`; `B004 عرف الرائحة والتطييب`; `B005 معروف تستحسنه النفس والعقل والشرع`; `B006 عريف يعرف القوم وتعرف به أحوالهم`; `B007 عرفة وعرفات وتعريف الوقوف`; `B008 تعريف الضالة والطلب حتى تعرف`; `B009 اعتراف يقر أو ينقاد`; `B010 نفس عروف تسكن وتصبر`; `B011 عرفة قرحة في بياض الكف`; `B012 عراف يدعي معرفة خفية أو خبر صنعة`; `B013 معارف ظاهرة يعرف بها الوجه أو الأرض`; `B014 اعرورف للشر تهيأ وتشزن`.
- `و ج ه`: `B001 الوجه والمستقبل`; `B002 الجهة والوجهة`; `B003 المواجهة والتقابل`; `B006 الوجاهة والجاه`; `B007 وجه النهار وصدره`; `B008 وجه الأمر وصوابه`; `B009 توجه الشيخ`; `B010 الولادة باليدين أولا`; `B011 توجيه القافية`; `B012 توجيه النبات`; `B013 ضرب الوجه`; `B014 الرد عن الوجه`; `B015 ذو وجهين`.
- `ن ض ر`: `B001 نضرة الحسن والإشراق`; `B002 نضارة الذهب وخلوصه`; `B003 قدح النضار وخشبه`.
- `س ق ي`: `B001 إرواء الشارب`; `B002 جعل السقيا`; `B003 نصيب الري ومجراه`; `B005 ماء البطن`; `B006 دعاء السقيا`; `B007 سحابة عظيمة القطر`; `B008 بردي لا يفوته الماء`; `B009 سقي الثوب صبغا`; `B010 تسقية القلب بالمكروه`.
- `ر ح ق`: `B001 الرحيق خمر صافية مختارة`.
- `خ ت م`: `B001 بلوغ الآخر وإتمام الختم`; `B002 الطبع بالخاتم وأثره`; `B003 الختم المانع المستوثق`; `B004 ختم الزرع بأول سقية`; `B005 السكوت تغافلا عن الشيء`; `B006 بياض خفي في أشاعر الفرس`; `B007 الجوزة المملسة المسماة المختم`.
- `م س ك`: `B001 إمساك الشيء وحبسه`; `B002 إمساك المال بخلا`; `B003 مسكة تبقي الرمق`; `B004 موضع يمسك الماء أو يثبت`; `B005 جلد يمسك ما فيه`; `B006 مسكة في المعصم`; `B008 إمساك النار في التراب`; `B009 ماسكة رحم`; `B010 الماسكة على الولد`; `B011 إمساك قوائم الفرس`; `B012 حسكة مسكة`.
- `ن ف س`: `B001 خروج النسيم من الجوف`; `B002 توسيع الكربة بالتنفيس`; `B003 إصابة العين بالنفس`; `B004 الدم السائل قوام النفس`; `B005 خروج الولد ودم النفاس`; `B006 نفس الشرب وجرعته`; `B007 قدر دبغة يسيرة`; `B008 ماء تقام به النفس`; `B009 انفتاح الصبح والشيء كالنفس`; `B010 شيء نفيس تتنافس فيه النفوس`; `B011 النفس التي بها الحياة`; `B012 عين الشيء وذاته`; `B013 ما في النفس من عقل وروع`; `B014 قوة النفس وخلقها`; `B015 سعة ومسافة ومهلة`; `B016 النافس سهم الميسر الخامس`.
- `م ز ج`: `B001 خلط الشيء بغيره`; `B002 مزاج البدن وتركيبه`; `B003 الشهد أو العسل المسمى مزجا`; `B004 تلون السنبل بين الخضرة والصفرة`; `B005 إعطاء السائل شيئا`.
- `س ن م`: `B001 العلو والارتفاع`; `B002 السنام والسنمة`; `B003 رأس النبات المرتفع`; `B004 ظهور الأرض والرمل المرتفعة`; `B005 أسماء المواضع المرتفعة`; `B007 ركوب الظهر وتسنمه`.
- `ع ي ن`: `B001 العين الناظرة`; `B002 المشاهدة بالعين`; `B003 عين الحفظ والرعاية`; `B004 الإصابة بالعين`; `B005 العين الجاسوسة`; `B006 منبع الماء الجاري`; `B007 عين الجلد والسقاء`; `B008 عين الشمس`; `B009 النقرة أو الموضع العيني`; `B010 عين السحاب والمطر`; `B011 النقد الحاضر`; `B012 العينة والسلف`; `B013 عين الشيء نفسه`; `B014 العين خيار الشيء`; `B015 أعيان القوم والإخوة`; `B016 سعة العين وحسنها`; `B017 العين بمعنى الناس الحاضرون`.
- `ش ر ب`: `B001 تناول المائع`; `B002 نصيب الماء`; `B003 جماعة الشرب والمشارب`; `B004 موضع الشرب وآلته`; `B005 ماء يشرب مع كراهة`; `B006 شارب الفم ومجاري الحلق`; `B007 مخالطة اللون والقلب`; `B008 إدخال الحبل في العنق`; `B009 مد العنق للنظر`; `B010 دعوى ما لم يشرب`; `B011 الشرب فهما`; `B012 مال يؤكل ويشرب`; `B013 تطييب القربة وتشريبها`; `B014 أرض ونبت ريان`.
- `ج ر م`: `B001 القطع والصرام`; `B002 مخلفات الصرام وثمره اليابس`; `B003 الكسب والإكساب`; `B004 الذنب والجناية`; `B006 تمام الزمن وانقطاعه`; `B007 جرم البدن وقدره`; `B008 جرم الصوت وخروجه`; `B009 صفاء اللون`; `B010 الحر والبلد الحار`; `B011 جرم وجارم أسماء قبائل`.
- `ء م ن`: `B001 سكون القلب في أمن وثقة`; `B002 تصديق يطمئن إليه القلب`; `B003 قول آمين طلبا للاستجابة`.
- `ض ح ك`: `B001 انبساط الوجه وظهور الأسنان`; `B002 الشيء الذي يضحك منه`; `B003 سرور أو تعجب يظهر بالضحك`; `B004 السن الظاهرة عند الضحك`; `B005 الطريق الواضح المستبين`; `B006 بريق ظاهر كأنه يضحك`; `B007 انشقاق الطلع والبلح`; `B008 امتلاء يفيض فيظهر`; `B009 بياض حلو أو زبد أو ثلج`; `B011 تكشير الحيوان أو صوته`.
- `م ر ر`: `B001 المضي والاجتياز`; `B002 الوقعة الزمنية والتكرار`; `B003 المرارة ضد الحلاوة`; `B004 الشدة المرة والداهية`; `B005 إحكام فتل الحبل`; `B006 القوة المحكمة والعزيمة`; `B007 المرة والمرارة في الجسد`; `B008 الأمر المصارين`.
- `غ م ز`: `B001 غمز باليد أو لمس اختبارا`; `B002 إشارة خفية بالجفن أو العين أو اليد`; `B003 عيب أو موضع مطعن وضعف`; `B004 غمز الدابة من رجلها`.
- `ء ه ل`: `B001 جماعة القرب والانتماء`; `B002 اتخاذ الأهل بالزواج`; `B003 موضع الصلاح والاستحقاق`; `B004 أنس المكان والعمران`; `B005 تحية السعة والأنس`; `B006 الإهالة المذابة`.
- `ف ك ه`: `B001 طيب النفس والنعيم المستطاب`; `B002 الفاكهة والثمر المستطاب`; `B003 الفكاهة وملاحة الكلام`; `B004 لبن مفكه طيب قبل الولاد`; `B006 الأشر البطر`; `B007 التفكه بالأعراض`.
- `ر ء ي`: `B001 رؤية العين والبصيرة`; `B002 رأي القلب والتفكر`; `B003 الرؤيا في المنام`; `B004 تراء وتواجه`; `B005 رياء الناس`; `B006 مرأى ومنظر ومرآة`; `B007 ترية الحيض`; `B008 رئي من الجن`; `B009 الرئة وما يصيبها`; `B010 ظهور حمل الناقة أو الشاة`; `B011 راية منصوبة`; `B012 إراءة وإظهار`; `B013 أرأيتك للتنبيه والاستخبار`.
- `ض ل ل`: `B001 الضلال عن الهدى والقصد`; `B002 الغيبوبة والخفاء`; `B003 فقدان الشيء`; `B004 ضياع الحفظ`; `B005 الضالة في المضيعة`.
- `ح ف ظ`: `B001 مراعاة الشيء وحراسته`; `B002 ثبوت المحفوظ في النفس`; `B003 ملازمة الأمر والمواظبة عليه`; `B004 تيقظ المتحفظ وقلة غفلته`; `B005 حفيظة الغضب والحمية`; `B006 صون الحرم والعهد والعفة`; `B007 طريق حافظ بين مستقيم`.
- `ر س ل`: `B001 الإرسال والانبعاث`; `B002 الرسول والرسالة`; `B003 السير السهل واللين`; `B004 الرفق والتؤدة`; `B005 التتابع والقطع`; `B006 اللبن والدر المتتابع`; `B007 الاستئناس والانبساط`; `B008 المراسلة والمسايرة`; `B009 المرأة المراسل`; `B010 الرخاء وطيب الإعطاء`; `B011 تسميات مفردة مخصوصة`.
- `ك ف ر`: `B001 ستر وتغطية`; `B002 غمر ساتر`; `B003 حجب الحق`; `B004 ستر النعمة`; `B005 تبرؤ وتنصل`; `B006 نسبة إلى الكفر`; `B007 إلجاء إلى العصيان`; `B008 تغطية البذر`; `B009 محو الإثم بتغطيته`; `B010 كمام الثمر`; `B011 كافور طيب`; `B012 موضع منقطع`; `B013 ثنية مستورة`; `B014 خضوع متطامن`; `B015 تاج يغطي`.
- `ث و ب`: `B001 العود والرجوع إلى موضع أو حال`; `B002 جزاء العمل العائد إلى عامله`; `B003 الثوب والكسوة وما يكنى به عن النفس`; `B004 التثويب: النداء المعاود أو المتكرر`; `B005 الثيب: من زالت بكارته أو رجع عن الزوج`.
- `ف ع ل`: `B001 إحداث عمل`; `B002 فعال الخلق`; `B003 فعلة العمل`; `B004 افتعال مختلق`; `B005 فعال بين اثنين`; `B007 مفعولات النحو`.

## Exhaustiveness Check After File Creation

After drafting this file, I checked the sweep against the available local source inventory:

- First rooted occurrence restarted: `83:1 مُطَفِّفِينَ / ط ف ف`.
- Every rooted occurrence row from S83 in `qac_root_ayah.tsv` appears in the Lexical Seed Coverage Catalog.
- Every distinct S83 root has an accepted branch inventory entry.
- Every branch not explicitly used as `G`, `C`, or `L` is marked as `T` by occurrence policy.
- Constructional and temporal seeds include the repeated conditional measuring pair, both ledger formulas, both knowledge formulas, both `كتاب مرقوم` occurrences, the denial/heart-cover sequence, the reward/drink sequence, the social mockery loop, the couch-looking repetition, and the final recompense closure.
- Potentially missing images checked and retained or terminated: measurement deficit, public standing, lower ledger, denial coating, barrier/fire, upper ledger, visible bliss, sealed high-source drink, mockery reversal, covering layers, knowledge thresholds, pastoral/body remote branches.
