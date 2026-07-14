# S98 Stage 1 Pass 2: temporally conditioned reactivation

Assigned passage: S98.
Sacred Arabic source: `resources/quran/surah_98.json`.

## Root cause of Pass 1 limitation

The limitation had two concrete causes.

1. The prompt-authorized SQLite files in this checkout are zero-byte placeholders: `resources/qac.sqlite` and `resources/furuq_v4.sqlite` contain no schema or queryable tables. Direct `qac_words`, `qac_morphemes`, and `branch_images` queries therefore fail here.
2. Pass 1 kept the discovery compressed in context instead of externalizing the occurrence-by-branch seed ledger. The result looked as if only a few words per finding had been visited, even though the initial sweep had identified the main dossiers.

For this restart I used the local exports that preserve the required fields:

- `resources/qac_root_ayah.tsv` for rooted occurrence, lemma, position, and ayah sequence.
- `resources/v4_branches.tsv` for accepted `branch_image_ar` and `what_is_ar`.
- `resources/attachments.tsv` filtered to S98 for structural attachments.
- `resources/quran/surah_98.json` for sacred Arabic text and order.

No translation evidence is used. The basmala is opening recitational context only and is not seeded.

## Sacred text sequence

0. `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`
1. `لَمْ يَكُنِ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ مُنفَكِّينَ حَتَّىٰ تَأْتِيَهُمُ ٱلْبَيِّنَةُ`
2. `رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ`
3. `فِيهَا كُتُبٌۭ قَيِّمَةٌۭ`
4. `وَمَا تَفَرَّقَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ إِلَّا مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَةُ`
5. `وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ حُنَفَآءَ وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ ۚ وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ`
6. `إِنَّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ فِى نَارِ جَهَنَّمَ خَٰلِدِينَ فِيهَآ ۚ أُو۟لَٰٓئِكَ هُمْ شَرُّ ٱلْبَرِيَّةِ`
7. `إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أُو۟لَٰٓئِكَ هُمْ خَيْرُ ٱلْبَرِيَّةِ`
8. `جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ لِمَنْ خَشِىَ رَبَّهُۥ`

## Rooted occurrence inventory and lexical seed count

The restart begins at the first rooted word, `98:1:2 يَكُنِ / ك و ن`, and treats every accepted branch row of every rooted occurrence as its own seed pass. Repeated roots are rerun where their local role changes. `عَدْنٍ` is included from the attachment/branch resources because it is present in the sacred text and has an accepted dossier even though the QAC root export did not list it.

| Occurrence | Root | Accepted branch rows | Lexical seed passes |
| --- | ---: | ---: | ---: |
| 98:1:2 `يَكُنِ` | `ك و ن` | 6 | 6 |
| 98:1:4 `كَفَرُوا۟` | `ك ف ر` | 15 | 15 |
| 98:1:6 `أَهْلِ` | `ء ه ل` | 6 | 6 |
| 98:1:7 `ٱلْكِتَٰبِ` | `ك ت ب` | 5 | 5 |
| 98:1:8 `ٱلْمُشْرِكِينَ` | `ش ر ك` | 8 | 8 |
| 98:1:9 `مُنفَكِّينَ` | `ف ك ك` | 9 | 9 |
| 98:1:11 `تَأْتِيَهُمُ` | `ء ت ي` | 13 | 13 |
| 98:1:12 `ٱلْبَيِّنَةُ` | `ب ي ن` | 12 | 12 |
| 98:2:1 `رَسُولٌ` | `ر س ل` | 11 | 11 |
| 98:2:3 `ٱللَّهِ` | `ء ل ه` | 2 | 2 |
| 98:2:4 `يَتْلُوا۟` | `ت ل و` | 8 | 8 |
| 98:2:5 `صُحُفًا` | `ص ح ف` | 5 | 5 |
| 98:2:6 `مُّطَهَّرَةً` | `ط ه ر` | 5 | 5 |
| 98:3:2 `كُتُبٌ` | `ك ت ب` | 5 | 5 |
| 98:3:3 `قَيِّمَةٌ` | `ق و م` | 20 | 20 |
| 98:4:2 `تَفَرَّقَ` | `ف ر ق` | 15 | 15 |
| 98:4:4 `أُوتُوا۟` | `ء ت ي` | 13 | 13 |
| 98:4:5 `ٱلْكِتَٰبَ` | `ك ت ب` | 5 | 5 |
| 98:4:8 `بَعْدِ` | `ب ع د` | 10 | 10 |
| 98:4:10 `جَآءَتْهُمُ` | `ج ي ء` | 9 | 9 |
| 98:4:11 `ٱلْبَيِّنَةُ` | `ب ي ن` | 12 | 12 |
| 98:5:2 `أُمِرُوا۟` | `ء م ر` | 10 | 10 |
| 98:5:4 `يَعْبُدُوا۟` | `ع ب د` | 11 | 11 |
| 98:5:5 `ٱللَّهَ` | `ء ل ه` | 2 | 2 |
| 98:5:6 `مُخْلِصِينَ` | `خ ل ص` | 6 | 6 |
| 98:5:8 `ٱلدِّينَ` | `د ي ن` | 7 | 7 |
| 98:5:9 `حُنَفَآءَ` | `ح ن ف` | 2 | 2 |
| 98:5:10 `يُقِيمُوا۟` | `ق و م` | 20 | 20 |
| 98:5:11 `ٱلصَّلَوٰةَ` | `ص ل و` | 9 | 9 |
| 98:5:13 `يُؤْتُوا۟` | `ء ت ي` | 13 | 13 |
| 98:5:14 `ٱلزَّكَوٰةَ` | `ز ك و` | 4 | 4 |
| 98:5:15 `دِينُ` | `د ي ن` | 7 | 7 |
| 98:5:16 `ٱلْقَيِّمَةِ` | `ق و م` | 20 | 20 |
| 98:6:3 `كَفَرُوا۟` | `ك ف ر` | 15 | 15 |
| 98:6:5 `أَهْلِ` | `ء ه ل` | 6 | 6 |
| 98:6:6 `ٱلْكِتَٰبِ` | `ك ت ب` | 5 | 5 |
| 98:6:7 `ٱلْمُشْرِكِينَ` | `ش ر ك` | 8 | 8 |
| 98:6:9 `نَارِ` | `ن و ر` | 8 | 8 |
| 98:6:11 `خَٰلِدِينَ` | `خ ل د` | 5 | 5 |
| 98:6:15 `شَرُّ` | `ش ر ر` | 11 | 11 |
| 98:6:16 `ٱلْبَرِيَّةِ` | `ب ر ء` | 13 | 13 |
| 98:7:3 `ءَامَنُوا۟` | `ء م ن` | 3 | 3 |
| 98:7:4 `عَمِلُوا۟` | `ع م ل` | 12 | 12 |
| 98:7:5 `ٱلصَّٰلِحَٰتِ` | `ص ل ح` | 5 | 5 |
| 98:7:8 `خَيْرُ` | `خ ي ر` | 5 | 5 |
| 98:7:9 `ٱلْبَرِيَّةِ` | `ب ر ء` | 13 | 13 |
| 98:8:1 `جَزَآؤُهُمْ` | `ج ز ي` | 5 | 5 |
| 98:8:2 `عِندَ` | `ع ن د` | 6 | 6 |
| 98:8:3 `رَبِّهِمْ` | `ر ب ب` | 17 | 17 |
| 98:8:4 `جَنَّٰتُ` | `ج ن ن` | 15 | 15 |
| 98:8:5 `عَدْنٍ` | `ع د ن` | 8 | 8 |
| 98:8:6 `تَجْرِى` | `ج ر ي` | 6 | 6 |
| 98:8:8 `تَحْتِهَا` | `ت ح ت` | 2 | 2 |
| 98:8:9 `ٱلْأَنْهَٰرُ` | `ن ه ر` | 7 | 7 |
| 98:8:10 `خَٰلِدِينَ` | `خ ل د` | 5 | 5 |
| 98:8:12 `أَبَدًا` | `ء ب د` | 8 | 8 |
| 98:8:13 `رَّضِىَ` | `ر ض و` | 7 | 7 |
| 98:8:14 `ٱللَّهُ` | `ء ل ه` | 2 | 2 |
| 98:8:16 `رَضُوا۟` | `ر ض و` | 7 | 7 |
| 98:8:20 `خَشِىَ` | `خ ش ي` | 3 | 3 |
| 98:8:21 `رَبَّهُۥ` | `ر ب ب` | 17 | 17 |

Total lexical seed passes run: 529.

## Temporally unfolding activation

1. `لم يكن الذين كفروا... منفكين حتى تأتيهم البينة`: the first rooted state is non-release. Covered/rejecting groups, affiliated groups, written-book identity, and association are held in a condition that does not loosen until a clear proof comes to them.
2. `رسول من الله يتلو صحفا مطهرة`: the expected proof arrives not as an abstract sign but as a sent bearer from Allah reciting/following purified written sheets.
3. `فيها كتب قيمة`: the sheets contain books/writings that are upright, sustaining, and norm-setting. The clarity of `البينة` is now interiorized into written upright content.
4. `وما تفرق الذين أوتوا الكتاب إلا من بعد ما جاءتهم البينة`: the arrival that should release from non-release instead triggers splitting among those given the book. The same `البينة` reactivates as a divider of response.
5. `وما أمروا إلا ليعبدوا...`: the passage narrows the command to a simple upright system: worship Allah, make religion pure for Him, incline away as hunafa, establish prayer, give zakat. The end of the ayah names this as `دين القيمة`.
6. `إن الذين كفروا... في نار جهنم... شر البرية`: the opening rejecting groups return, now located in fire and ranked as worst of creation.
7. `إن الذين آمنوا وعملوا الصالحات... خير البرية`: the rival class is named by inward security/faith and intentional repairing action, then ranked best of creation.
8. `جزاؤهم عند ربهم...`: the final state completes the positive branch: recompense near their Lord, covered gardens of stable residence, rivers running below, permanent abiding, mutual pleasure, and fear of the Lord as the eligibility condition.

## Candidate synthesis units

### C98-01: non-release until the clear separator arrives

- `candidate_id`: C98-01
- `ayah_range`: 98:1-4
- `seed_type`: lexical/constructional
- `seed`: first rooted word `98:1:2 يَكُنِ`, expanded through `98:1:9 مُنفَكِّينَ` and `98:1:12 ٱلْبَيِّنَةُ`
- `generating_set`: `(E: ك و ن B001 وقوع الشيء وحضوره في زمان)`, `(E: ك ف ر B001 ستر وتغطية)`, `(E: ك ف ر B003 حجب الحق)`, `(E: ء ه ل B001 جماعة القرب والانتماء)`, `(E: ك ت ب B002 نظم الحروف واسم المكتوب)`, `(E: ش ر ك B001 الشركة والمشاركة)`, `(E: ش ر ك B002 الشرك بالله)`, `(E: ف ك ك B003 الانفكاك عن الشيء بمعنى الزوال والمفارقة)`, `(E: ف ك ك B001 فتح المغلق وفصل المشتبك)`, `(E: ء ت ي B001 الإتيان والمجيء)`, `(E: ب ي ن B004 ظهور الشيء وانكشافه)`, `(E: ب ي ن B005 كشف المعنى بالقول أو العلامة)`
- `selected_branches`: `ك و ن B001`; `ك ف ر B001/B003`; `ء ه ل B001`; `ك ت ب B002/B003`; `ش ر ك B001/B002`; `ف ك ك B001/B003`; `ء ت ي B001`; `ب ي ن B004/B005`, with later constraint/corroboration from `ف ر ق B001/B002`, `ج ي ء B001`, `ب ع د B002`.
- `constructed_model`: The opening simulates a covered or adherent collective that is not coming loose. The clear proof is predicted as the event that can open the locked state and separate what had remained attached, covered, or confused.
- `freeze_point`: after 98:1, before `رسول من الله`.
- `predictions_at_freeze`: expected agent or medium of coming proof; expected written/communicative clarity; expected release or separation after arrival; expected test of whether clarity heals or splits the groups.
- `unused_features_tested`: 98:2 messenger and recitation; 98:3 interior written upright content; 98:4 later splitting after proof came; 98:5 restricted command; 98:6-7 final sorting.
- `corroborators`: `(C: ر س ل B002 الرسول والرسالة supplies bearer of proof)`, `(C: ت ل و B001 following/sequential recitation supplies the proof's unfolding medium)`, `(C: ص ح ف B002 written sheets)`, `(C: ط ه ر B001 purified/clean of dross)`, `(C: ق و م B008 uprightness/straightness)`, `(C: ف ر ق B001 distinguishing/separating after the proof)`, `(C: ج ي ء B001 coming in 98:4 repeats arrival)`, `(C: ب ع د B002 afterness makes the split temporally dependent on arrival)`.
- `constraints`: `(K: ف ك ك is accusative predicate of negated kāna, so the first model is not actual release but denied release)`, `(K: ب ي ن B001 separation cannot erase the surface sense of clear proof)`, `(K: the groups are not physically chained; release is a secondary simulation of cognitive/social non-disengagement)`, `(K: 98:4 shows not clean release but later rupture, so the model must fork rather than end at proof-arrival)`.
- `temporal_reactivation_notes`: `البينة` at 98:1 is first expected as the condition of release. Its recurrence in 98:4 retrospectively shows that the arrival of clarity also exposes and triggers division.
- `rival_models`: physical shackle/unfastening model from `ف ك ك B002` is vivid but unsupported by body/captivity syntax; generic "people were not leaving" is too static and misses the proof-as-separator trajectory.
- `grade`: strong
- `grade_rationale`: This unit explains the opening order, the delayed arrival, the repeated `البينة`, and the paradoxical later `تفرق` by independent lexical, syntactic, and temporal channels.
- `source_queries_or_rows_used`: S98 QAC export rows for `ك و ن/ك ف ر/ء ه ل/ك ت ب/ش ر ك/ف ك ك/ء ت ي/ب ي ن/ف ر ق/ج ي ء/ب ع د`; attachments `98:1:a1-a9`, `98:4:a1-a6`.

### C98-02: clear proof as sent recitation of purified upright writings

- `candidate_id`: C98-02
- `ayah_range`: 98:1-3
- `seed_type`: verified composite
- `seed`: `98:1:12 ٱلْبَيِّنَةُ` and its appositional unfolding in 98:2-3
- `generating_set`: `(E: ب ي ن B004 ظهور الشيء وانكشافه)`, `(E: ب ي ن B005 كشف المعنى بالقول أو العلامة)`, `(E: ر س ل B001 الإرسال والانبعاث)`, `(E: ر س ل B002 الرسول والرسالة)`, `(E: attachment 98:2:a1 من الله qualifies رسول)`, `(E: ت ل و B001 اتباع وتتابع)`, `(E: ص ح ف B002 صحيفة مكتوبة)`, `(E: ط ه ر B001 النقاء وزوال الدنس)`, `(E: attachment 98:2:a4 مطهرة modifies صحفا)`, `(E: attachment 98:3:a1-a2 فيها as fronted locative predicate for كتب)`, `(E: ك ت ب B002 written book)`, `(E: ق و م B008 استقامة واعتدال واستواء)`, `(E: ق و م B009 قوام وعماد ونظام)`
- `selected_branches`: `ب ي ن B004/B005`; `ر س ل B001/B002`; `ت ل و B001`; `ص ح ف B002/B003`; `ط ه ر B001/B005`; `ك ت ب B002/B003`; `ق و م B008/B009`.
- `constructed_model`: The clear proof is an ordered communicative body: a messenger sent from Allah recites/follows purified sheets that contain upright, sustaining writings. Clarity is not bare visibility; it is transmitted, recited, purified, written, and normatively upright.
- `freeze_point`: after 98:3.
- `predictions_at_freeze`: if this is true proof, later division should be culpable because it occurs after clarity; the command should be simple and upright rather than obscure.
- `unused_features_tested`: 98:4 `إلا من بعد ما جاءتهم البينة`; 98:5 `وما أمروا إلا`; 98:5 `دين القيمة`; 98:6-7 final ranking.
- `corroborators`: `(C: ب ع د B002 afterness in 98:4 confirms proof-before-split sequence)`, `(C: ف ر ق B001/B002 division after clarity)`, `(C: ء م ر B002 command in 98:5 makes the proof normatively directive)`, `(C: د ي ن B001 obedience/religion)`, `(C: خ ل ص B001/B004 purity and exclusive devotion mirror صحف مطهرة)`, `(C: ق و م B008 repeats at دين القيمة)`.
- `constraints`: `(K: ر س ل B003 easy gait and B005 herds in troops are not local)`, `(K: ت ل و B005 abandonment and B009 false claim are defeated by the messenger-from-Allah construction)`, `(K: ص ح ف B001 broad surface supports sheet-geometry only secondarily; the written-sheet branch is primary)`.
- `temporal_reactivation_notes`: 98:2-3 answers the suspense of 98:1. The proof arrives as a recited sequence; only after its contents are shown does 98:4 mention division.
- `rival_models`: visual-only proof; book-only proof without living messenger; purity-only proof without written/recited content.
- `grade`: strong
- `grade_rationale`: The ayah sequence itself specifies each role predicted by the seed: sender, messenger, recitation, sheets, purification, contained books, and uprightness.
- `source_queries_or_rows_used`: S98 QAC export rows for `ب ي ن/ر س ل/ء ل ه/ت ل و/ص ح ف/ط ه ر/ك ت ب/ق و م`; attachments `98:2:a1-a4`, `98:3:a1-a3`.

### C98-03: proof releases by dividing, not by leaving everyone intact

- `candidate_id`: C98-03
- `ayah_range`: 98:1 and 98:4
- `seed_type`: lexical/temporal
- `seed`: `98:4:2 تَفَرَّقَ`, tested backward against `مُنفَكِّينَ` and repeated `البينة`
- `generating_set`: `(E: ف ر ق B001 تمييز وتزييل بين شيئين)`, `(E: ف ر ق B002 تفريق وتشتيت إلى أجزاء)`, `(E: ب ع د B002 afterness)`, `(E: ج ي ء B001 المجيء والحصول)`, `(E: ب ي ن B004 proof/manifestness)`, `(E: ك ت ب B002/B003 the book given to them)`, `(E: ء ت ي B002 الإيتاء والإعطاء in أوتوا)`
- `selected_branches`: `ف ر ق B001/B002/B005`; `ب ع د B002`; `ج ي ء B001`; `ء ت ي B002`; `ك ت ب B002/B003`; `ب ي ن B004/B005`.
- `constructed_model`: The same clarity that should end non-release becomes a sorting event. Those given the book split only after the proof comes; their division is therefore not caused by lack of evidence but by the arrival of evidence.
- `freeze_point`: after 98:4.
- `predictions_at_freeze`: the next ayah should identify the command as simple enough to make the split culpable; later ayat should sort the two outcomes.
- `unused_features_tested`: 98:5 restricted worship command; 98:6-7 worst/best creation contrast; 98:8 reward for the responsive group.
- `corroborators`: `(C: ء م ر B002 restricted command)`, `(C: إلا construction in 98:5 narrows obligation)`, `(C: خ ل ص B004 exclusive devotion)`, `(C: ح ن ف B002 directional inclining)`, `(C: 98:6 repeats opening rejecting groups)`, `(C: 98:7 creates rival group with faith and repair)`.
- `constraints`: `(K: ف ر ق B004 sea-splitting and B011 measure-vessel are not local)`, `(K: the text says أهل الكتاب specifically split in 98:4, so do not generalize this ayah to all groups without the later sorting)`, `(K: proof is not itself a weapon; division is response to clarity)`.
- `temporal_reactivation_notes`: `حتى تأتيهم البينة` creates an expectation that arrival changes the state. `إلا من بعد ما جاءتهم البينة` confirms change but reverses a simple release expectation into culpable fragmentation.
- `rival_models`: proof as purely reconciliatory; proof as purely condemning. The passage supports a separator that clarifies and then sorts.
- `grade`: strong
- `grade_rationale`: The repeated lexical items and temporal construction make the after-arrival split a central reactivation, not an optional theme.
- `source_queries_or_rows_used`: S98 QAC export rows for `ف ر ق/ء ت ي/ك ت ب/ب ع د/ج ي ء/ب ي ن`; attachments `98:4:a1-a6`.

### C98-04: the upright religion is purification plus directed standing

- `candidate_id`: C98-04
- `ayah_range`: 98:5
- `seed_type`: verified composite
- `seed`: `98:5:2 أُمِرُوا۟` and the restricted content under `إلا`
- `generating_set`: `(E: ء م ر B002 الطلب والإلزام)`, `(E: attachment 98:5:a1 clausal complement after أمروا إلا)`, `(E: ع ب د B003 العبادة والطاعة الخاضعة)`, `(E: ء ل ه B001 التعبد والمعبود)`, `(E: خ ل ص B001 تنقية وصفاء بعد شوب)`, `(E: خ ل ص B004 اختصاص وانفراد عن الشرك)`, `(E: attachment 98:5:a3-a5 مخلصين له الدين)`, `(E: د ي ن B001 الطاعة والانقياد)`, `(E: ح ن ف B002 الميل إلى جهة)`, `(E: ق و م B003 عزم ونهوض إلى الأمر)`, `(E: ق و م B008 استقامة)`, `(E: ص ل و B003 العبادة المخصوصة)`, `(E: ء ت ي B002 الإيتاء والإعطاء)`, `(E: ز ك و B001 النماء والزيادة)`, `(E: ز ك و B002 الطهارة والصلاح)`, `(E: د ي ن B001)`, `(E: ق و م B008/B009 in دين القيمة)`
- `selected_branches`: `ء م ر B002`; `ع ب د B003`; `خ ل ص B001/B004`; `د ي ن B001`; `ح ن ف B002`; `ق و م B003/B008/B009`; `ص ل و B003`; `ء ت ي B002`; `ز ك و B001/B002`.
- `constructed_model`: After the proof-induced split, the actual command is rendered as a compact system: exclusive worship, purified religion for Allah, directional inclining away from deviation, established prayer, and given/growing purification. The closure `دين القيمة` folds the whole sequence back into uprightness.
- `freeze_point`: after 98:5.
- `predictions_at_freeze`: later sorting should contrast rejection with faith/repair; positive closure should involve stable nearness and divine acceptance.
- `unused_features_tested`: 98:6 fire/worst creation; 98:7 faith and righteous works; 98:8 recompense near Lord and mutual pleasure.
- `corroborators`: `(C: ء م ن B001/B002 faith as secure inward assent)`, `(C: ع م ل B001 intentional action)`, `(C: ص ل ح B001 repair/opposite of فساد)`, `(C: خ ي ر B001 positive pole)`, `(C: ج ز ي B001 recompense after command)`, `(C: ر ض و B001/B003 acceptance and mutual pleasure)`, `(C: خ ش ي B001 reverent fear as closing eligibility)`.
- `constraints`: `(K: ء م ر B006 monstrous affair, B011 spear-tip, and B009 lamb branch terminate)`, `(K: ع ب د B001 slavery is not the local sense, though submissive service remains subordinate geometry)`, `(K: ص ل و B001 fire-heat is constrained by the ritual object الصلاة)`, `(K: ح ن ف B001 crooked foot cannot override directional religious inclination)`.
- `temporal_reactivation_notes`: The command appears after the split, so it retrospectively reduces the excuse space: the proof did not bring an obscure demand but a purified, upright, repeated structure.
- `rival_models`: legalistic multiplicity model; ritual-only model; interior-only sincerity model. The ayah requires all roles to stay linked.
- `grade`: strong
- `grade_rationale`: The construction, attachments, and lexical branches converge tightly, and the later positive outcome independently confirms the command-response path.
- `source_queries_or_rows_used`: S98 QAC export rows for `ء م ر/ع ب د/ء ل ه/خ ل ص/د ي ن/ح ن ف/ق و م/ص ل و/ء ت ي/ز ك و`; attachments `98:5:a1-a13`.

### C98-05: covered rejection versus secure repair produces worst/best creation

- `candidate_id`: C98-05
- `ayah_range`: 98:6-7 with backward links to 98:1 and 98:5
- `seed_type`: lexical/morphosyntactic contrast
- `seed`: paired ranking constructions `شر البرية` and `خير البرية`
- `generating_set`: `(E: ك ف ر B003 حجب الحق)`, `(E: ك ف ر B001 ستر وتغطية)`, `(E: ء ه ل B001 group affiliation)`, `(E: ك ت ب B002 book identity)`, `(E: ش ر ك B002 shirk)`, `(E: ن و ر B002 النار المتقدة)`, `(E: خ ل د B001 دوام البقاء)`, `(E: ش ر ر B001 الشر والسوء)`, `(E: ب ر ء B001 الخلق والإيجاد / البرية)`, `(E: ء م ن B001 سكون القلب في أمن وثقة)`, `(E: ء م ن B002 تصديق يطمئن إليه القلب)`, `(E: ع م ل B001 الفعل المقصود والعمل)`, `(E: ص ل ح B001 الصلاح ضد الفساد)`, `(E: خ ي ر B001 الخير النافع)`, `(E: خ ي ر B002 فضل الصلاح والاصطفاء)`, `(E: attachment 98:6:a10-a11 شر البرية)`, `(E: attachment 98:7:a5-a6 خير البرية)`
- `selected_branches`: `ك ف ر B001/B003`; `ش ر ك B002`; `ن و ر B002`; `خ ل د B001`; `ش ر ر B001`; `ب ر ء B001`; `ء م ن B001/B002`; `ع م ل B001`; `ص ل ح B001`; `خ ي ر B001/B002`.
- `constructed_model`: The passage bifurcates creation itself by response to proof and command. Covered rejection and association are placed in fire with persistent duration and ranked as worst creation; secure assent and repairing intentional action are ranked best creation.
- `freeze_point`: after 98:7.
- `predictions_at_freeze`: the positive branch should receive an outcome corresponding to best creation: nearness, stable abode, flow, permanence, and satisfaction.
- `unused_features_tested`: 98:8 full reward scene and `ذلك لمن خشي ربه`.
- `corroborators`: `(C: ج ز ي B001 recompense matches prior rank)`, `(C: ع ن د B004 nearness at their Lord)`, `(C: ج ن ن B003 covered garden)`, `(C: ع د ن B001 stable residence)`, `(C: ج ر ي B001 running flow)`, `(C: ن ه ر B001 rivers)`, `(C: خ ل د B001 repeated permanence)`, `(C: ء ب د B001 duration/forever)`, `(C: ر ض و B003 mutual satisfaction)`, `(C: خ ش ي B001 reverent fear as condition)`.
- `constraints`: `(K: ن و ر B001 light branch is defeated by surface نار and branch B002 fire)`, `(K: ب ر ء B002 البراءة والتباعد can create separation imagery but البرية here is creation)`, `(K: خير/شر are predicate-rank terms, not full translations of the whole group)`.
- `temporal_reactivation_notes`: 98:6 repeats the opening `الذين كفروا من أهل الكتاب والمشركين`, proving that the opening unresolved group is now judged. 98:7 introduces the positive counterpart whose reward closes the surah.
- `rival_models`: ethnic/group identity sorting without response; generic heaven/hell contrast without proof-command sequence. Both miss the temporal buildup.
- `grade`: strong
- `grade_rationale`: The paired syntax, repeated group labels, and exact opposite lexical poles create one of the passage's clearest synthesis units.
- `source_queries_or_rows_used`: S98 QAC export rows for `ك ف ر/ء ه ل/ك ت ب/ش ر ك/ن و ر/خ ل د/ش ر ر/ب ر ء/ء م ن/ع م ل/ص ل ح/خ ي ر`; attachments `98:6:a1-a11`, `98:7:a1-a6`.

### C98-06: reward as stable covered abode with living flow

- `candidate_id`: C98-06
- `ayah_range`: 98:8
- `seed_type`: lexical/composite
- `seed`: `98:8:1 جَزَآؤُهُمْ`
- `generating_set`: `(E: ج ز ي B001 مقابلة الفعل بجزائه)`, `(E: ع ن د B004 قرب وحضور عند الشيء)`, `(E: ر ب ب B001 ربوبية وملك وسيادة)`, `(E: ر ب ب B002 إصلاح وتربية وإتمام)`, `(E: ج ن ن B003 البستان المستور بالشجر)`, `(E: ج ن ن B001 الستر والاستتار as secondary garden geometry)`, `(E: ع د ن B001 إقامة وثبات في موضع)`, `(E: ج ر ي B001 جريان الشيء وانسياحه)`, `(E: ت ح ت B001 تحت الشيء)`, `(E: ن ه ر B001 نهر يشق الأرض بماء جار)`, `(E: خ ل د B001 ثبات وبقاء)`, `(E: ء ب د B001 طول المدة والدوام)`, `(E: ر ض و B001 الرضا خلاف السخط)`, `(E: ر ض و B003 المراضاة والتراضي)`, `(E: خ ش ي B001 الخوف والخشية مع الهيبة)`
- `selected_branches`: `ج ز ي B001/B002`; `ع ن د B004`; `ر ب ب B001/B002`; `ج ن ن B001/B003`; `ع د ن B001/B002`; `ج ر ي B001/B006`; `ت ح ت B001`; `ن ه ر B001/B003`; `خ ل د B001`; `ء ب د B001/B006`; `ر ض و B001/B003`; `خ ش ي B001`.
- `constructed_model`: The final recompense is a stable nearness-field: near their Lord, enclosed gardens of residence, water running below, permanence intensified by `أبدا`, and mutual divine-human satisfaction. The closing condition is reverent fear of the Lord.
- `freeze_point`: after 98:8.
- `predictions_at_freeze`: as closure, the reward should gather earlier purity, uprightness, and permanence without reopening unresolved roles.
- `unused_features_tested`: backward replay of 98:5 command and 98:7 faith/repair.
- `corroborators`: `(C: خ ل ص B001 purity and ز ك و B002 purification prepare the clean garden-reward field)`, `(C: ق و م B008 upright religion prepares stable عَدْن)`, `(C: ء م ن B001 security is completed by رضى and جنات)`, `(C: ص ل ح B001 repair contrasts with فساد and supports best-creation reward)`, `(C: ر ب ب B001 appears both as giver-nearness and feared Lord)`.
- `constraints`: `(K: ج ن ن B006 madness, B012 snake, B013 crowd, and B016 chest bones terminate)`, `(K: ن ه ر B004 verbal rebuke and B006 stealth terminate)`, `(K: ء ب د B002 wildness and B003 empty dwelling are defeated by جنات عدن)`, `(K: خ ش ي B004 dried dates/meat terminates)`.
- `temporal_reactivation_notes`: The final ayah answers the prediction created by `خير البرية`: best creation receives an environment of permanence, flow, and acceptance, not merely a rank label.
- `rival_models`: garden as only concealment; reward as only payment; fear as terror-only. The passage combines recompense, lordly nearness, stable residence, and reverent eligibility.
- `grade`: strong
- `grade_rationale`: The closing ayah has unusually dense role completion: source, place, stability, flow, time, affect, and condition all fit independently.
- `source_queries_or_rows_used`: S98 QAC export rows plus attachment row for `ع د ن`; branch rows for `ج ز ي/ع ن د/ر ب ب/ج ن ن/ع د ن/ج ر ي/ت ح ت/ن ه ر/خ ل د/ء ب د/ر ض و/خ ش ي`; attachments `98:8:a1-a16`.

### C98-07: purity chain from proof to religion to zakat

- `candidate_id`: C98-07
- `ayah_range`: 98:2-5
- `seed_type`: lexical convergence
- `seed`: `98:2:6 مُّطَهَّرَةً` and `98:5:6 مُخْلِصِينَ`, tested with `ٱلزَّكَوٰةَ`
- `generating_set`: `(E: ط ه ر B001 النقاء وزوال الدنس)`, `(E: ط ه ر B005 تنزيه النفس والعمل عن القبيح)`, `(E: خ ل ص B001 صفاء بعد شوب)`, `(E: خ ل ص B004 اختصاص وانفراد عن الشرك)`, `(E: ز ك و B002 الطهارة والصلاح)`, `(E: ز ك و B001 النماء والزيادة)`, `(E: attachment 98:2:a4 purified modifies sheets)`, `(E: attachment 98:5:a3-a5 مخلصين له الدين)`, `(E: attachment 98:5:a10 الزكاة direct object of يؤتوا)`
- `selected_branches`: `ط ه ر B001/B005`; `خ ل ص B001/B004`; `ز ك و B001/B002`; secondary `ص ل ح B001`.
- `constructed_model`: Purity begins with the proof's written medium, then moves into the worshipper's directed religion, then becomes an enacted giving/purification. The passage builds a chain from clean source to clean devotion to clean social output.
- `freeze_point`: after 98:5:14.
- `predictions_at_freeze`: positive group should be defined by faith plus repairing action, and reward should be clean/stable rather than mixed.
- `unused_features_tested`: 98:7 `آمنوا وعملوا الصالحات`; 98:8 gardens and divine pleasure.
- `corroborators`: `(C: ص ل ح B001 repair/suitability confirms purity in action)`, `(C: ع م ل B001 intentional work)`, `(C: ر ض و B001 acceptance confirms purified relation)`, `(C: ج ن ن B003 garden outcome, not fire)`.
- `constraints`: `(K: ط ه ر B002 menstrual purity and B003 water-washing remain local but not generated by the passage)`, `(K: خ ل ص B008 food/smen extraction is secondary only)`, `(K: ز ك و B005 odd/even game branch terminates)`.
- `temporal_reactivation_notes`: The proof is `مطهرة` before the command is stated; only later does the same purity logic appear in `مخلصين` and `الزكوة`.
- `rival_models`: ritual purity only; sincerity only; almsgiving only. The passage supports one chain with distinct roles.
- `grade`: medium-strong
- `grade_rationale`: Strong lexical convergence, but less passage-wide than the release/proof/sorting candidates.
- `source_queries_or_rows_used`: S98 QAC export rows for `ط ه ر/خ ل ص/ز ك و/ص ل ح/ع م ل/ر ض و`; attachments `98:2:a4`, `98:5:a3-a5/a9-a10`, `98:7:a3-a4`.

### C98-08: uprightness as contained writing, established practice, and final religion

- `candidate_id`: C98-08
- `ayah_range`: 98:3 and 98:5
- `seed_type`: lexical/constructional
- `seed`: repeated `ق و م` in `قيمة`, `يقيموا`, and `دين القيمة`
- `generating_set`: `(E: ق و م B008 استقامة واعتدال واستواء)`, `(E: ق و م B009 قوام وعماد ونظام)`, `(E: ق و م B003 عزم ونهوض إلى الأمر)`, `(E: attachment 98:3:a3 قيمة modifies كتب)`, `(E: attachment 98:5:a7 يقيموا coordinated with يعبدوا)`, `(E: attachment 98:5:a11-a12 دين القيمة)`
- `selected_branches`: `ق و م B003/B004/B008/B009`; rejected primary branches include body height, midday, market, eye, disease, and furniture parts.
- `constructed_model`: Uprightness is seeded inside the proof's writings, then enacted as establishing prayer, then named as the religion's character. The root recurs at text, practice, and system levels.
- `freeze_point`: after `دين القيمة`.
- `predictions_at_freeze`: final positive outcome should be stable and properly placed.
- `unused_features_tested`: 98:8 `جنات عدن`, `عند ربهم`, and abiding permanence.
- `corroborators`: `(C: ع د ن B001 stable residence)`, `(C: خ ل د B001 permanence)`, `(C: ع ن د B004 nearness/place)`, `(C: ر ب ب B002 caretaking/completion)`.
- `constraints`: `(K: ق و م B010 price/value can echo قيمة but cannot replace uprightness in the coordinated command)`, `(K: قام bodily standing is only one component; the passage requires normative establishment)`.
- `temporal_reactivation_notes`: The listener first hears upright books inside purified sheets, then an upright command, then a final upright reward-location.
- `rival_models`: value/price model; posture-only prayer model.
- `grade`: medium-strong
- `grade_rationale`: Repetition gives strong temporal reactivation; branch polysemy requires careful constraint.
- `source_queries_or_rows_used`: S98 QAC export rows for three `ق و م` occurrences; attachments `98:3:a3`, `98:5:a7-a12`, reward rows in 98:8.

### C98-09: fire versus covered garden as opposed enclosures

- `candidate_id`: C98-09
- `ayah_range`: 98:6-8
- `seed_type`: lexical contrast
- `seed`: `98:6:9 نَارِ` contrasted with `98:8:4 جَنَّٰتُ`
- `generating_set`: `(E: ن و ر B002 النار المتقدة والسمة بها)`, `(E: attachment 98:6:a5-a7 في نار جهنم predicate)`, `(E: خ ل د B001 abiding in it)`, `(E: ج ن ن B003 covered garden)`, `(E: ج ن ن B001 covering/shelter secondary)`, `(E: ع د ن B001 stable residence)`, `(E: ج ر ي B001 running flow)`, `(E: ن ه ر B001 watercourse)`, `(E: خ ل د B001 repeated positive permanence)`
- `selected_branches`: `ن و ر B002`; `خ ل د B001`; `ج ن ن B003`; `ع د ن B001`; `ج ر ي B001`; `ن ه ر B001`; `ت ح ت B001`.
- `constructed_model`: The two ranked classes receive opposed enclosures: fire for the covered rejecters, garden-cover with flowing water for the secure repairing group. Both are permanent, but their media differ.
- `freeze_point`: after 98:8:12.
- `predictions_at_freeze`: affective closure should correspond to the positive enclosure; eligibility should be named.
- `unused_features_tested`: `رضي الله عنهم ورضوا عنه` and `لمن خشي ربه`.
- `corroborators`: `(C: ر ض و B003 mutual pleasure fits positive enclosure)`, `(C: خ ش ي B001 reverent fear prevents complacency)`, `(C: ك ف ر B001 covering negatively contrasts ج ن ن B003 covering positively)`.
- `constraints`: `(K: ن و ر B001 light/illumination is not primary for نار here)`, `(K: ج ن ن B006 madness and B005 hidden jinn terminate)`, `(K: both branches use containment, but the passage's moral polarity controls the difference)`.
- `temporal_reactivation_notes`: The coveredness of `كفر` at the opening is answered by two enclosures: fire as punitive containment and garden as protected reward.
- `rival_models`: generic afterlife contrast; element-only fire/water model without ranked creation.
- `grade`: medium-strong
- `grade_rationale`: Strong lexical contrast and repeated `خالدين فيها`; less explanatory for the proof-command sequence than C98-01 to C98-05.
- `source_queries_or_rows_used`: S98 QAC export rows for `ن و ر/خ ل د/ج ن ن/ع د ن/ج ر ي/ت ح ت/ن ه ر/ر ض و/خ ش ي`; attachments `98:6:a5-a9`, `98:8:a1-a16`.

### C98-10: coming/giving/guided transfer axis

- `candidate_id`: C98-10
- `ayah_range`: 98:1, 98:4-5
- `seed_type`: lexical
- `seed`: repeated `ء ت ي` plus `ج ي ء`
- `generating_set`: `(E: ء ت ي B001 الإتيان والمجيء at 98:1 تأتيهم)`, `(E: ج ي ء B001 المجيء والحصول at 98:4 جاءتْهم)`, `(E: ء ت ي B002 الإيتاء والإعطاء at 98:4 أوتوا and 98:5 يؤتوا)`, `(E: ك ت ب B002/B003 object of being given)`, `(E: ز ك و B001/B002 object of giving)`, `(E: ب ي ن B004 proof that comes)`
- `selected_branches`: `ء ت ي B001/B002/B003`; `ج ي ء B001/B004`; `ك ت ب B002/B003`; `ز ك و B001/B002`.
- `constructed_model`: The surah repeatedly stages transfer: proof comes to them, book had been given to them, proof came to them, and zakat is to be given. Arrival of guidance and obligation to give are part of one directional economy.
- `freeze_point`: after 98:5:14.
- `predictions_at_freeze`: those who respond should receive a corresponding recompense; those who reject the transfer of proof should be sorted negatively.
- `unused_features_tested`: 98:8 `جزاؤهم عند ربهم`.
- `corroborators`: `(C: ج ز ي B001 recompense closes the transfer logic)`, `(C: ر ض و B001 acceptance confirms reciprocal relation)`, `(C: ر س ل B001 sending precedes coming)`.
- `constraints`: `(K: ء ت ي B005 flood, B006 stranger, B010 road, and B011 calamity are only remote unless tied to specific local roles)`, `(K: ج ي ء water-pool and wound-pus branches terminate)`.
- `temporal_reactivation_notes`: The first arrival predicts proof; the later arrivals and givings show that receiving clarity entails giving purified due and receiving final recompense.
- `rival_models`: commercial/tax model from `ء ت ي B008`; water-channel model from `ء ت ي B004`. Both are weak secondary images.
- `grade`: medium
- `grade_rationale`: Repetition is strong, but the lexical family is broad and supports a directional axis rather than a fully independent image.
- `source_queries_or_rows_used`: S98 QAC export rows for three `ء ت ي` occurrences plus `ج ي ء`; attachments `98:1:a6-a9`, `98:4:a3-a6`, `98:5:a9-a10`.

## Occurrence-by-branch seed ledger

### 98:1:2 `يَكُنِ`

All six `ك و ن` branch rows were seeded. `B001` supports C98-01 as temporal occurrence/state. `B002` place/status and `B006` bad-state are local weak supports for the negated condition. `B003` surety/undertaking is weak near the proof-command system. `B004` submissive weakness and `B005` old-man attribution terminate.

### 98:1:4 `كَفَرُوا۟`

All fifteen `ك ف ر` rows were seeded. `B001` covering, `B003` truth-covering/rejection, and `B004` covering ingratitude support C98-01/C98-05. `B005` disavowal is local medium because 98:6 later separates outcomes. `B008` seed-covering and `B009` covering sin are weak secondary images. `B002`, `B006`, `B007`, `B010`, `B011`, `B012`, `B013`, `B014`, and `B015` terminate or remain remote.

### 98:1:6 `أَهْلِ`

All six `ء ه ل` rows were seeded. `B001` group affiliation supports C98-01/C98-05. `B003` eligibility weakly anticipates final `لمن خشي ربه`. `B004/B005` habitation/being among familiar people are local weak. `B002` marriage and `B006` rendered fat terminate.

### 98:1:7 `ٱلْكِتَٰبِ`

All five `ك ت ب` rows were seeded. `B002` written book and `B003` decreed/obligating writing support C98-01/C98-02/C98-03. `B001` joining/collecting supports the assembled book-people identity only secondarily. `B004` register and `B005` manumission contract are local weak to terminated.

### 98:1:8 `ٱلْمُشْرِكِينَ`

All eight `ش ر ك` rows were seeded. `B002` shirk is primary in C98-01/C98-05. `B001` partnership/mixing supports the non-release/adherence image. `B006` snare is a weak image for entanglement but lacks hunting syntax. `B003`, `B004`, `B005`, `B007`, and `B008` terminate or remain remote.

### 98:1:9 `مُنفَكِّينَ`

All nine `ف ك ك` rows were seeded. `B003` non-separation/zawal and `B001` opening/factual unfastening support C98-01. `B002` freeing captive/ransom is a vivid but constrained secondary image. `B005` loosened joint weakly supports loss of cohesion. `B004`, `B006`, `B007`, `B008`, and `B009` terminate.

### 98:1:11 `تَأْتِيَهُمُ`

All thirteen `ء ت ي` rows were seeded. `B001` coming supports C98-01/C98-10. `B003` proper way/prepared access is local medium. `B002` giving is reserved for `أوتوا/يؤتوا` but tested here as weak. `B004/B005` water-channel/flood are weak secondary direction images. `B006`, `B007`, `B008`, `B009`, `B010`, `B011`, `B012`, and `B013` terminate or remain remote.

### 98:1:12 `ٱلْبَيِّنَةُ`

All twelve `ب ي ن` rows were seeded. `B004` manifest proof and `B005` explanatory disclosure support C98-01/C98-02. `B001` separation and `B003` relation-between-parties support C98-03 secondarily. `B002` between/interval supports temporal mediation weakly. `B006`, `B007`, `B008`, `B009`, `B010`, `B011`, and `B012` terminate or remain remote.

### 98:2:1 `رَسُولٌ`

All eleven `ر س ل` rows were seeded. `B001` sending and `B002` messenger/message support C98-02. `B004` measured recitation/slow care is local medium with `يتلو`. `B005` troops/series weakly supports sequential recitation. `B003`, `B006`, `B007`, `B008`, `B009`, `B010`, and `B011` terminate or remain remote.

### 98:2:3 and 98:5:5 and 98:8:14 `ٱللَّه`

Both `ء ل ه` rows were rerun at each occurrence. `B001` worshipped deity supports C98-04; `B002` divine name supports source/subject roles in C98-02, C98-04, and C98-06. The basmala `ء ل ه` is opening-context corroboration only.

### 98:2:4 `يَتْلُوا۟`

All eight `ت ل و` rows were seeded. `B001` following/reciting in sequence supports C98-02. `B003` remaining obligation/claim weakly supports written content. `B004` liability/surety is remote to command. `B005` abandonment, `B006` offspring, `B007` echoing singer, `B008` last breath, and `B009` false claim terminate.

### 98:2:5 `صُحُفًا`

All five `ص ح ف` rows were seeded. `B002` written sheet and `B003` gathered sheets support C98-02. `B001` flat/wide surface is local image support. `B004` broad bowl and `B005` misreading terminate or remain constraints.

### 98:2:6 `مُّطَهَّرَةً`

All five `ط ه ر` rows were seeded. `B001` purity and `B005` moral/work purification support C98-02/C98-07. `B003/B004` washing/purifying medium are local weak; `B002` menstruation-specific purity terminates.

### 98:3:2, 98:4:5, 98:6:6 `كِتَاب/كُتُب`

All five `ك ت ب` rows were rerun at each occurrence. In 98:3 `B002/B003` support C98-02 as contained upright writings. In 98:4 `B002/B003` support C98-03 as the received book. In 98:6 they support C98-05 as group identity under judgment. `B001` remains secondary collection; `B004/B005` remain local weak or terminated in all three.

### 98:3:3, 98:5:10, 98:5:16 `قَيِّمَة / يُقِيمُوا / ٱلْقَيِّمَة`

All twenty `ق و م` rows were rerun at each occurrence. `B008` uprightness, `B009` sustaining order, `B003` rising to perform, and `B004` care/maintenance support C98-04/C98-08. `B002` bodily standing is local for prayer establishment only. `B010` value/price is constrained to the adjective echo. `B001`, `B006`, `B007`, `B011`, `B012`, `B013`, `B014`, `B015`, `B016`, `B017`, `B018`, `B019`, `B020`, and `B021` terminate or remain remote.

### 98:4:2 `تَفَرَّقَ`

All fifteen `ف ر ق` rows were seeded. `B001` distinguishing/separation and `B002` fragmentation support C98-03. `B005` faction/group supports the result weakly. `B009` fear-fracture can be local with later `خشي` but is not primary. `B004`, `B006`, `B007`, `B008`, `B010`, `B011`, `B012`, `B013`, `B014`, `B015`, and `B016` terminate or remain remote.

### 98:4:4 `أُوتُوا۟` and 98:5:13 `يُؤْتُوا۟`

All thirteen `ء ت ي` rows were rerun. At 98:4 `B002` giving is primary for being given the book; at 98:5 `B002` giving is primary for zakat. `B001` coming supports the proof-arrival axis, while `B003` proper access is local. All other branches are weak directional images or terminated as above.

### 98:4:8 `بَعْدِ`

All ten `ب ع د` rows were seeded. `B002` afterness supports C98-03. `B001` distance and `B003` making distant support separation only secondarily. `B004` curse/destruction weakly anticipates negative outcome. `B005`, `B006`, `B007`, `B008`, `B009`, and `B010` terminate or remain remote.

### 98:4:10 `جَآءَتْهُمُ`

All nine `ج ي ء` branch rows were seeded. `B001` coming supports C98-03/C98-10. `B004` bringing/presenting is local medium. `B005` compulsion is weak because proof constrains response. Water-pool, wound-pus, and duplicate/remote coming branches terminate or remain non-primary.

### 98:5:2 `أُمِرُوا۟`

All ten `ء م ر` rows were seeded. `B002` command supports C98-04. `B001` affair supports the content generally. `B003` authority is local under divine command. `B004` growth/blessing weakly meets zakat. `B005` sign/appointed mark weakly meets proof/order. `B006`, `B007`, `B008`, `B009`, and `B011` terminate or remain remote.

### 98:5:4 `يَعْبُدُوا۟`

All eleven `ع ب د` rows were seeded. `B003` worship/submissive obedience supports C98-04. `B001` slavery is constrained as secondary submission, not social slavery. `B005` leveled road is weak directional support with `حنفاء/قيمة`. `B006` honoring is local weak. `B004`, `B007`, `B008`, `B009`, `B010`, `B011`, and `B012` terminate or remain remote.

### 98:5:6 `مُخْلِصِينَ`

All six `خ ل ص` rows were seeded. `B001` purification from mixture and `B004` exclusive belonging support C98-04/C98-07. `B002` escaping from entanglement weakly reactivates `منفكين`. `B003` reaching is local weak. `B007` pure friendship and `B008` food/smen extraction remain secondary or terminated.

### 98:5:8 and 98:5:15 `ٱلدِّينَ / دِينُ`

All seven `د ي ن` rows were rerun. `B001` obedience/religion supports C98-04. `B002` judgment/recompense weakly anticipates 98:8. `B003` debt is local weak under obligation/giving. `B004` subjugation is constrained. `B005`, `B006`, and `B007` terminate or remain remote.

### 98:5:9 `حُنَفَآءَ`

Both `ح ن ف` rows were seeded. `B002` directional inclining supports C98-04. `B001` crooked foot is retained only as constrained body-geometry and cannot become the primary sense.

### 98:5:11 `ٱلصَّلَوٰةَ`

All nine `ص ل و` rows were seeded. `B003` ritual prayer supports C98-04. `B002` invocation/mercy is local support. `B006` following in a race weakly echoes `تلو`/sequence but is not primary. `B001` fire-heat is constrained by ritual object and by negative fire later. `B004`, `B005`, `B007`, `B008`, and `B009` terminate or remain remote.

### 98:5:14 `ٱلزَّكَوٰةَ`

All four `ز ك و` rows were seeded. `B002` purification/righteousness and `B001` growth support C98-04/C98-07. `B004` suitability is local weak. `B005` odd/even game terminates.

### 98:6:9 `نَارِ`

All eight `ن و ر` rows were seeded. `B002` fire supports C98-05/C98-09. `B001` light is constrained and cannot override fire. `B007` enmity weakly supports negative social outcome. `B004`, `B005`, `B006`, `B008`, and `B009` terminate or remain remote.

### 98:6:11 and 98:8:10 `خَٰلِدِينَ`

All five `خ ل د` rows were rerun at both occurrences. `B001` permanence supports C98-05/C98-06/C98-09 on both negative and positive sides. `B002` clinging/settling is local support. `B004` heart/inner thought weakly contacts `آمنوا`. `B003` ornament and `B005` blind animal terminate.

### 98:6:15 `شَرُّ`

All eleven `ش ر ر` rows were seeded. `B001` evil/worst supports C98-05. `B003` sparks weakly contacts fire but is not syntactically used. `B011` quarrel weakly fits division. `B002`, `B004`, `B005`, `B006`, `B007`, `B009`, `B010`, and `B012` terminate or remain remote.

### 98:6:16 and 98:7:9 `ٱلْبَرِيَّةِ`

All thirteen `ب ر ء` rows were rerun at both occurrences. `B001` creation supports C98-05. `B002` separation can weakly echo sorting, but surface `البرية` constrains it. `B003` healing weakly supports positive repair; `B004/B005` legal/biological clearance are remote. Hunting-hide, month-end, duplicate clearance rows terminate.

### 98:7:3 `ءَامَنُوا۟`

All three `ء م ن` rows were seeded. `B002` settled truth-assent and `B001` security/trust support C98-05 and C98-06. `B003` saying amen is local weak/opening-context only and does not generate the group.

### 98:7:4 `عَمِلُوا۟`

All twelve `ع م ل` rows were seeded. `B001` intentional work supports C98-05. `B002` employing/operating is local medium. `B004` wage/recompense anticipates reward weakly. `B010` working limb is weak. Office, transaction, manual laborer, hardship, work-bred animal, spear shaft, road, and walkers terminate or remain remote.

### 98:7:5 `ٱلصَّٰلِحَٰتِ`

All five `ص ل ح` rows were seeded. `B001` repair/opposite corruption supports C98-05/C98-07. `B003` suitability is local. `B002` reconciliation weakly echoes split repair but is not explicit. Named-person and place branches terminate.

### 98:7:8 `خَيْرُ`

All five `خ ي ر` rows were seeded. `B001` good/benefit and `B002` excellence/selection support C98-05. `B003` choosing is local weak; `B005` generosity weakly anticipates reward. `B006` animal extraction terminates.

### 98:8:1 `جَزَآؤُهُمْ`

All five `ج ز ي` rows were seeded. `B001` recompense supports C98-06. `B002` sufficiency/substitution is local medium. `B003` debt-collection weakly reactivates `دين`. `B004` jizya and `B005` rivalry in recompense terminate.

### 98:8:2 `عِندَ`

All six `ع ن د` rows were seeded. `B004` nearness/presence supports C98-06. `B001` stubborn resistance is a rejected contrast with the negative group. `B002/B003` side-flow are weak only near rivers. `B005/B006` terminate.

### 98:8:3 and 98:8:21 `رَبِّهِمْ / رَبَّهُ`

All seventeen `ر ب ب` rows were rerun at both occurrences. `B001` lordship/ownership and `B002` care/completion support C98-06. `B007` abiding and `B011` covenant are local weak. `B008/B013` cloud/water weakly contact garden/rivers. Remaining pastoral, vessel, plant, herd, grammar-particle, need, and seafaring branches terminate or remain remote.

### 98:8:4 `جَنَّٰتُ`

All fifteen `ج ن ن` rows were seeded. `B003` garden supports C98-06/C98-09. `B001` covering/shelter is secondary. `B011` dense vegetation is local support. `B007` hidden fetus and `B009` burial are defeated by reward context. Madness, jinn, shield, snake, crowds, beginning, chest bones, and hiding-place branches terminate or remain remote.

### 98:8:5 `عَدْنٍ`

All eight `ع د ن` rows were seeded. `B001` stable residence supports C98-06. `B002` original/stable source is local medium. `B003` shore, `B004` patched vessel, `B005` group, `B006` striking earth, `B007` fullness of drinker, and `B008` names/nasabs terminate or remain remote.

### 98:8:6 `تَجْرِى`

All six `ج ر ي` rows were seeded. `B001` running/flow supports C98-06/C98-09. `B006` continuing provision is local medium. `B002` regular course weakly supports stable reward order. `B003`, `B004`, and `B007` terminate or remain remote.

### 98:8:8 `تَحْتِهَا`

Both `ت ح ت` rows were seeded. `B001` below supports C98-06. `B002` low/common people terminates.

### 98:8:9 `ٱلْأَنْهَٰرُ`

All seven `ن ه ر` rows were seeded. `B001` watercourse supports C98-06/C98-09. `B003` opening/widening supports flow geometry secondarily. `B002` daylight weakly contrasts final brightness but is not local. Rebuke, stealth, names, and cloud branches terminate.

### 98:8:12 `أَبَدًا`

All eight `ء ب د` rows were seeded. `B001` long duration/forever and `B006` staying without leaving support C98-06. `B007` lasting memory is local weak. Wildness, empty dwelling, prolific animal, strange word, and anger branches terminate.

### 98:8:13 and 98:8:16 `رَّضِىَ / رَضُوا۟`

All seven `ر ض و` rows were rerun at both occurrences. `B001` satisfaction and `B003` mutual satisfaction support C98-06. `B004` seeking/removing displeasure is local. `B002` abundant رضوان is a secondary support. `B005`, `B006`, and `B007` terminate or remain remote.

### 98:8:20 `خَشِىَ`

All three `خ ش ي` rows were seeded. `B001` reverent fear supports C98-06 as closing eligibility. `B002` knowledge-by-extension is local weak because fear follows clarity. `B004` dried dates/meat terminates.

## Constructional, morphosyntactic, and temporal seeds

- `لم يكن ... منفكين حتى تأتيهم البينة`: C98-01 strong. Negated state plus until-clause creates unresolved non-release until proof-arrival.
- `من أهل الكتاب والمشركين`: C98-01/C98-05 strong. Attachment rows make the two group labels partitive/coordinated under `من`.
- appositional unfolding `البينة -> رسول من الله يتلو صحفا مطهرة -> فيها كتب قيمة`: C98-02 strong. The proof is expanded over three ayat.
- repeated `البينة` in 98:1 and 98:4: C98-01/C98-03 strong. First it is anticipated as release condition; then it becomes the after-which of division.
- `إلا من بعد ما جاءتهم`: C98-03 strong. Exception plus afterness prevents treating division as pre-proof ignorance.
- `وما أمروا إلا`: C98-04 strong. Restricted-command construction narrows the demand after the split.
- coordinated command sequence `ليعبدوا / يقيموا / يؤتوا`: C98-04 strong. The command is not one isolated act but a structured worship-practice-giving system.
- repeated `قيمة / يقيموا / القيمة`: C98-08 medium-strong. Uprightness moves from text to practice to religion.
- paired `شر البرية` / `خير البرية`: C98-05 strong. Creation-rank polarity is syntactically explicit.
- repeated `خالدين فيها`: C98-09 medium-strong. Permanence applies to both negative and positive enclosures.
- final mutuality `رضي الله عنهم ورضوا عنه`: C98-06 strong. It resolves the positive branch affectively and reciprocally.
- closing `ذلك لمن خشي ربه`: C98-06 medium-strong. The final deictic gathers the reward and names reverent fear of the Lord as eligibility.

## Image Packet Catalog

### IMG-98-A

- Starting seed: `ف ك ك B003` at 98:1:9.
- Complete image: a covered/adhered social-religious field is not released until clear proof arrives; the proof then separates response rather than leaving the field fused.
- Passage-order assembly: non-release -> proof comes -> messenger recites purified sheets -> proof comes again -> division after proof.
- Participants and roles: rejecting groups = covered/adhered field; proof = clarifying separator; messenger = carrier; book-people = already text-affiliated subgroup.
- Operation / mechanism: clarity opens and distinguishes.
- Direction / force / medium: arrival from outside to them; recited/written disclosure; separation after arrival.
- Temporal development: expected release becomes revealed division.
- Outcome / closure: sorted into worst/best creation.
- Exact branch constituents: KWN B001; KFR B001/B003; AHL B001; KTB B002/B003; SHRK B001/B002; FKK B001/B003; ATY B001; BYN B004/B005; FRQ B001/B002; JYء B001.
- Unfilled roles: exact inward reason for refusal remains supplied only by later `كفر/شرك`.
- Status: COMPLETE.

### IMG-98-B

- Starting seed: `ب ي ن B004/B005` at 98:1:12.
- Complete image: clear proof as a sent, recited, purified, written, upright communicative body.
- Passage-order assembly: proof named -> messenger from Allah -> recites sheets -> sheets purified -> inside them upright writings.
- Participants and roles: Allah = source; messenger = sent bearer; sheets = medium; books/writings = contained content; uprightness = normative shape.
- Operation / mechanism: clarity is transmitted through purified recitation and writing.
- Direction / force / medium: from Allah through messenger into recited sheets.
- Temporal development: the initially unresolved proof is specified across 98:2-3.
- Outcome / closure: makes later division culpable and command intelligible.
- Exact branch constituents: BYN B004/B005; RSL B001/B002; TLW B001; SHF B002/B003; THR B001/B005; KTB B002/B003; QWM B008/B009.
- Unfilled roles: none.
- Status: COMPLETE.

### IMG-98-C

- Starting seed: `ء م ر B002` at 98:5:2.
- Complete image: an upright purified religion composed of exclusive worship, purified allegiance, directional inclining, established prayer, and purifying/growing giving.
- Passage-order assembly: command restricted -> worship Allah -> purify religion for Him -> incline as hunafa -> establish prayer -> give zakat -> that is upright religion.
- Participants and roles: Allah = object/source; worshippers = commanded agents; religion = purified directed allegiance; prayer/zakat = stabilizing practices.
- Operation / mechanism: command reduces complexity into upright practice.
- Direction / force / medium: inward purity and outward establishment/giving.
- Temporal development: proof's purity becomes religious purity and action.
- Outcome / closure: faith plus righteous works receive best-creation rank.
- Exact branch constituents: AMR B002; ABD B003; ءLH B001; KHLS B001/B004; DYN B001; HNF B002; QWM B003/B008/B009; SLW B003; ATY B002; ZKW B001/B002.
- Unfilled roles: exact historical addressees are constrained by previous ayat, not expanded.
- Status: COMPLETE.

### IMG-98-D

- Starting seed: paired creation-rank predicates `شر البرية` / `خير البرية`.
- Complete image: creation is sorted into covered rejection and secure repairing response.
- Passage-order assembly: rejecting groups in fire/worst creation -> believing and repairing group best creation -> reward near Lord.
- Participants and roles: rejecters/associators = negative class; believers/doers of repair = positive class; creation = ranking field; fire/garden = outcome fields.
- Operation / mechanism: response to proof and command determines rank and destination.
- Direction / force / medium: from proof-command response to final classification.
- Temporal development: opening group returns under judgment; rival group appears after command.
- Outcome / closure: reward scene completes positive ranking.
- Exact branch constituents: KFR B001/B003; SHRK B002; NWR B002; KHLD B001; SHRR B001; BRء B001; AMN B001/B002; AML B001; SLH B001; KHYR B001/B002.
- Unfilled roles: none.
- Status: COMPLETE.

### IMG-98-E

- Starting seed: `ج ز ي B001` at 98:8:1.
- Complete image: stable reward near the Lord, with covered gardens, residence, rivers below, permanence, mutual pleasure, and reverent fear.
- Passage-order assembly: recompense -> near Lord -> gardens of Eden -> rivers flow underneath -> abiding forever -> mutual pleasure -> for one who fears his Lord.
- Participants and roles: Lord = source and feared one; rewarded group = recipients; gardens = stable enclosure; rivers = living flow; pleasure = reciprocal closure.
- Operation / mechanism: intentional faith/repair receives fitting recompense.
- Direction / force / medium: from action/faith to nearness and stable abode.
- Temporal development: positive rank becomes complete environment.
- Outcome / closure: no unresolved role remains; final condition is fear of the Lord.
- Exact branch constituents: JZY B001; AND B004; RBB B001/B002; JNN B003; ADN B001; JRY B001; THT B001; NHR B001; KHLD B001; ءBD B001; RDW B001/B003; KHSH B001.
- Unfilled roles: none.
- Status: COMPLETE.

### IMG-98-F

- Starting seed: `ن و ر B002` at 98:6:9 and `ج ن ن B003` at 98:8:4.
- Complete image: opposed enclosures, one fire and one covered garden with water.
- Passage-order assembly: negative class in fire, abiding there -> positive class in gardens, rivers, abiding forever.
- Participants and roles: fire = punitive enclosure; garden = protective enclosure; rivers = life-flow; permanence = duration shared by opposite outcomes.
- Operation / mechanism: moral polarity selects medium of containment.
- Direction / force / medium: enclosed in fire versus sheltered in garden with water below.
- Temporal development: covered rejection becomes punitive enclosure; secure faith becomes protected enclosure.
- Outcome / closure: mutual pleasure marks the positive enclosure.
- Exact branch constituents: NWR B002; KHLD B001; JNN B003/B001; ADN B001; JRY B001; NHR B001; RDW B003.
- Unfilled roles: none.
- Status: COMPLETE.

## Final self-check for exhaustion

- Rooted occurrence sweep restarted from the first rooted word: yes, beginning with `98:1:2 يَكُنِ`.
- Every accepted branch row for every S98 rooted occurrence was given a seed pass: yes, 529 lexical seed passes including repeated occurrences and the text-attested `ع د ن`.
- Every repeated rooted occurrence with a different local role was rerun: yes, especially `ك ف ر`, `ء ه ل`, `ك ت ب`, `ش ر ك`, `ء ت ي`, `ب ي ن`, `ق و م`, `د ي ن`, `خ ل د`, `ب ر ء`, `ر ب ب`, and `ر ض و`.
- Constructional/morphosyntactic seeds were run separately: yes.
- Construction and corroboration are kept separate in candidate packets: yes.
- Failed and weak seeds are not silently dropped: yes; they are marked as terminated, local weak, constrained, or remote in the ledger.
- Potentially missing images checked: yes. Remote images from water channels, physical captivity, wounds, body joints, sea-splitting, price/value, fire/light, concealment, garden-cover, and stable residence were generated or tested; only coherent or instructive fragments were retained.
- Pass 2 output path written: `v1/outputs/98-stage1-pass-2.md`.
