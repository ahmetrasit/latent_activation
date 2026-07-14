# S85 Stage 1 Pass 2 - temporally conditioned reactivation

Assigned passage: S85, whole surah.

Sacred Arabic text source used: `resources/quran/surah_85.json`.

Authorized structural source used: `resources/attachments.tsv`, rows where `sura=85` and `ayah=1..22`.

Authorized lexical/QAC sources attempted:

- `resources/qac.sqlite`
- `resources/furuq_v4.sqlite`

## Root cause of the Pass 1 limitation

The limitation was not an early preference for a few promising words. The immediate root cause was that both authorized SQLite resources are zero-byte databases in this workspace state:

- `resources/qac.sqlite`: no `qac_words` or `qac_morphemes` tables available.
- `resources/furuq_v4.sqlite`: no `branch_images` table available.

Therefore Pass 1 could not retrieve:

- QAC word/morpheme rows for S85;
- accepted branch counts;
- `branch_id`;
- `branch_image_ar`;
- `what_is_ar`;
- uncontaminated furuq branch dossiers.

I did not invent missing branch IDs or branch images. This Pass 2 restarts from the first rooted word using all recoverable S85 evidence from the sacred Arabic text and attachment rows. Every recoverable rooted occurrence and every eligible construction is initiated as a seed pass. Branch-level lexical expansion remains blocked wherever the missing furuq dossier is required.

## Exhaustive restart inventory

Opening context, not seed material: `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`. It was not used to initiate a seed. Because QAC/furuq are empty, its roots and branch dossiers were not inspected; it can only constrain divine-source framing at a general opening-context level.

Recoverable rooted occurrence sequence from S85 sacred text, attachment rows, and the local QAC-derived root inventory:

1. `85:1:1 وَالسَّمَاءِ` root `س م و`, oath object.
2. `85:1:3 الْبُرُوجِ` root `ب ر ج`, idafa complement of `ذَاتِ`.
3. `85:2:1 وَالْيَوْمِ` root `ي و م`, oath object.
4. `85:2:2 الْمَوْعُودِ` root `و ع د`, adjective of `الْيَوْمِ`.
5. `85:3:1 وَشَاهِدٍ` root `ش ه د`, active participle oath object.
6. `85:3:2 وَمَشْهُودٍ` root `ش ه د`, passive participle conjoined oath object.
7. `85:4:1 قُتِلَ` root `ق ت ل`, passive event.
8. `85:4:2 أَصْحَابُ` root `ص ح ب`, passive subject of `قُتِلَ`.
9. `85:4:3 الْأُخْدُودِ` root `خ د د`, idafa complement of `أَصْحَابُ`.
10. `85:5:1 النَّارِ` root `ن و ر`, appositional/linked fire noun.
11. `85:5:3 الْوَقُودِ` root `و ق د`, idafa complement of `ذَاتِ`.
12. `85:6:4 قُعُودٌ` root `ق ع د`, predicate of `هُمْ`.
13. `85:7:4 يَفْعَلُونَ` root `ف ع ل`, relative-clause action.
14. `85:7:6 بِالْمُؤْمِنِينَ` root `ء م ن`, governed complement attached to `يَفْعَلُونَ`.
15. `85:7:8 شُهُودٌ` root `ش ه د`, predicate of `هُمْ`.
16. `85:8:3 نَقَمُوا` root `ن ق م`, negated verb.
17. `85:8:7 يُؤْمِنُوا` root `ء م ن`, excepted clausal content after `إِلَّا`.
18. `85:8:9 بِاللَّهِ` root `ء ل ه`, complement of `يُؤْمِنُوا`.
19. `85:8:10 الْعَزِيزِ` root `ع ز ز`, divine attribute.
20. `85:8:11 الْحَمِيدِ` root `ح م د`, divine attribute.
21. `85:9:3 مُلْكُ` root `م ل ك`, delayed subject of `لَهُ`.
22. `85:9:4 السَّمَاوَاتِ` root `س م و`, idafa complement of `مُلْكُ`.
23. `85:9:6 وَالْأَرْضِ` root `ء ر ض`, conjoined domain under `مُلْكُ`.
24. `85:9:8 وَاللَّهُ` root `ء ل ه`, subject of `شَهِيدٌ`.
25. `85:9:10 كُلِّ` root `ك ل ل`, governed complement under `عَلَى`.
26. `85:9:11 شَيْءٍ` root `ش ي ء`, idafa complement of `كُلِّ`.
27. `85:9:12 شَهِيدٌ` root `ش ه د`, predicate of `اللَّهُ`.
28. `85:10:3 فَتَنُوا` root `ف ت ن`, relative-clause event.
29. `85:10:4 الْمُؤْمِنِينَ` root `ء م ن`, direct object of `فَتَنُوا`.
30. `85:10:6 وَالْمُؤْمِنَاتِ` root `ء م ن`, conjoined affected group.
31. `85:10:9 يَتُوبُوا` root `ت و ب`, negated jussive after `ثُمَّ لَمْ`.
32. `85:10:13 عَذَابُ` root `ع ذ ب`, first delayed subject/punishment.
33. `85:10:17 عَذَابُ` root `ع ذ ب`, second coordinated punishment.
34. `85:10:18 الْحَرِيقِ` root `ح ر ق`, idafa complement of second `عَذَابُ`.
35. `85:11:3 آمَنُوا` root `ء م ن`, relative-clause event.
36. `85:11:5 وَعَمِلُوا` root `ع م ل`, coordinated action.
37. `85:11:6 الصَّالِحَاتِ` root `ص ل ح`, direct object of `عَمِلُوا`.
38. `85:11:9 جَنَّاتٌ` root `ج ن ن`, predicate/reward.
39. `85:11:10 تَجْرِي` root `ج ر ي`, verbal qualifier of `جَنَّاتٌ`.
40. `85:11:12 تَحْتِهَا` root `ت ح ت`, spatial complement under `مِن`.
41. `85:11:13 الْأَنْهَارُ` root `ن ه ر`, post-verbal subject of `تَجْرِي`.
42. `85:11:15 الْفَوْزُ` root `ف و ز`, predicate of `ذَلِكَ`.
43. `85:11:16 الْكَبِيرُ` root `ك ب ر`, adjective of `الْفَوْزُ`.
44. `85:12:2 بَطْشَ` root `ب ط ش`, governed name of `إِنَّ`.
45. `85:12:3 رَبِّكَ` root `ر ب ب`, idafa complement of `بَطْشَ`.
46. `85:12:5 لَشَدِيدٌ` root `ش د د`, predicate of `إِنَّ`.
47. `85:13:3 يُبْدِئُ` root `ب د ء`, predicate under `هُوَ`.
48. `85:13:5 وَيُعِيدُ` root `ع و د`, coordinated predicate.
49. `85:14:3 الْغَفُورُ` root `غ ف ر`, predicate of `هُوَ`.
50. `85:14:4 الْوَدُودُ` root `و د د`, parallel predicate.
51. `85:15:2 الْعَرْشِ` root `ع ر ش`, idafa complement of `ذُو`.
52. `85:15:3 الْمَجِيدُ` root `م ج د`, adjective/predicate quality.
53. `85:16:1 فَعَّالٌ` root `ف ع ل`, intensive predicate.
54. `85:16:3 يُرِيدُ` root `ر و د`, relative content under `لِمَا`.
55. `85:17:2 أَتَاكَ` root `ء ت ي`, interrogative arrival event.
56. `85:17:3 حَدِيثُ` root `ح د ث`, delayed subject of `أَتَى`.
57. `85:17:4 الْجُنُودِ` root `ج ن د`, idafa complement of `حَدِيثُ`.
58. `85:19:3 كَفَرُوا` root `ك ف ر`, relative-clause event.
59. `85:19:5 تَكْذِيبٍ` root `ك ذ ب`, governed complement under `فِي`.
60. `85:20:2 وَاللَّهُ` root `ء ل ه`, subject of `مُحِيطٌ`.
61. `85:20:4 وَرَائِهِمْ` root `و ر ي`, complement under `مِن`.
62. `85:20:5 مُحِيطٌ` root `ح و ط`, predicate of `اللَّهُ`.
63. `85:21:3 قُرْآنٌ` root `ق ر ء`, predicate of `هُوَ`.
64. `85:21:4 مَجِيدٌ` root `م ج د`, adjective of `قُرْآنٌ`.
65. `85:22:2 لَوْحٍ` root `ل و ح`, governed complement under `فِي`.
66. `85:22:3 مَحْفُوظٍ` root `ح ف ظ`, adjective of `لَوْحٍ`.

Every listed occurrence was restarted as a seed. Because no furuq branch dossier exists in this workspace state, each lexical branch seed is recorded as blocked at branch-expansion time unless the occurrence also participates in a constructional, morphosyntactic, or temporal image below. No unlisted furuq branch is inferred.

## Exhaustive lexical seed status

All lexical root/occurrence seeds were initiated from the first rooted word onward. The shared result is:

- seed formation: surface/root/position identified where recoverable;
- QAC morpheme dossier: blocked because `resources/qac.sqlite` has no tables;
- furuq branch dossier: blocked because `resources/furuq_v4.sqlite` has no tables;
- selected branches: none;
- branch-level expansion: not performed;
- final lexical-only grade: `unlikely` as a synthesis unit, because no accepted branch can be cited.

This blocked status applies to: `س م و`, `ب ر ج`, `ي و م`, `و ع د`, `ش ه د`, `ق ت ل`, `ص ح ب`, `خ د د`, `ن و ر`, `و ق د`, `ق ع د`, `ف ع ل`, `ء م ن`, `ن ق م`, `ء ل ه`, `ع ز ز`, `ح م د`, `م ل ك`, `ء ر ض`, `ك ل ل`, `ش ي ء`, `ف ت ن`, `ت و ب`, `ع ذ ب`, `ح ر ق`, `ع م ل`, `ص ل ح`, `ج ن ن`, `ج ر ي`, `ت ح ت`, `ن ه ر`, `ف و ز`, `ك ب ر`, `ب ط ش`, `ر ب ب`, `ش د د`, `ب د ء`, `ع و د`, `غ ف ر`, `و د د`, `ع ر ش`, `م ج د`, `ر و د`, `ء ت ي`, `ح د ث`, `ج ن د`, `ك ف ر`, `ك ذ ب`, `و ر ي`, `ح و ط`, `ق ر ء`, `ل و ح`, `ح ف ظ`.

Repeated roots were not collapsed for temporal purposes. For example, the first `ش ه د` pair in the oath, the human `شُهُودٌ` at `85:7`, and the divine `شَهِيدٌ` at `85:9` each re-enter the recitation state differently; they are therefore tested separately in the constructional candidates.

## Constructional and temporal seed set

The following actual constructions were also started as seeds:

- `85:1-3`: three-part oath sequence: sky possessing `بروج`, promised day, witness and witnessed.
- `85:1`: `السَّمَاءِ ذَاتِ الْبُرُوجِ`, idafa possession construction.
- `85:2`: `الْيَوْمِ الْمَوْعُودِ`, promised-time construction.
- `85:3`: `شَاهِدٍ وَمَشْهُودٍ`, active/passive witness pair.
- `85:4-5`: `قُتِلَ أَصْحَابُ الْأُخْدُودِ النَّارِ ذَاتِ الْوَقُودِ`, passive condemnation plus trench/fire/fuel apposition.
- `85:6-7`: `إِذْ هُمْ عَلَيْهَا قُعُودٌ وَهُمْ عَلَى مَا يَفْعَلُونَ ... شُهُودٌ`, seated-over and witnessing-over construction.
- `85:8`: `وَمَا نَقَمُوا مِنْهُمْ إِلَّا أَن يُؤْمِنُوا`, negation plus exclusive exception.
- `85:8-9`: faith in Allah followed by `العزيز الحميد`, ownership of heavens and earth, and divine witness over every thing.
- `85:10`: `فَتَنُوا المؤمنين والمؤمنات ثُمَّ لَمْ يَتُوبُوا`, trial/persecution plus delayed non-return.
- `85:10`: two `لَهُمْ عَذَابُ` clauses, including `عَذَابُ الْحَرِيقِ`.
- `85:11`: `آمَنُوا وَعَمِلُوا الصالحات` followed by gardens, flowing rivers, and great triumph.
- `85:12-16`: divine agency cluster: severe grasp, begins and returns, forgiving/loving, throne/glory, active over what He wills.
- `85:17-18`: `هَلْ أَتَاكَ حَدِيثُ الْجُنُودِ فِرْعَوْنَ وَثَمُودَ`, prior-host narrative insertion.
- `85:19-20`: `بَلِ الَّذِينَ كَفَرُوا فِي تَكْذِيبٍ وَاللَّهُ مِن وَرَائِهِم مُّحِيطٌ`, denial-in-state plus surrounding-from-behind.
- `85:21-22`: `بَلْ هُوَ قُرْآنٌ مَّجِيدٌ فِي لَوْحٍ مَّحْفُوظٍ`, recitation as glorious and preserved in a tablet.

## Candidate synthesis units

### S85-P2-C01 - Oath of an upper ordered field, an appointed time, and a witness relation

- `candidate_id`: `S85-P2-C01`
- `ayah_range`: `85:1-3`
- `seed_type`: constructional / temporal
- `seed`: opening oath sequence from the first rooted word `السَّمَاءِ`.
- `generating_set`: `(E: 85:1 وَ oath particle attachment a1)`, `(E: 85:1 السماء oath object)`, `(E: 85:1 ذات البروج adjective/idafa attachments a2-a3)`, `(E: 85:2 واليوم oath object attachment a1)`, `(E: 85:2 الموعود adjective attachment a2)`, `(E: 85:3 وشاهد oath object attachment a1)`, `(E: 85:3 ومشهود conjoined/oath object attachments a2-a3)`.
- `selected_branches`: no furuq branches available; no `branch_id` used.
- `constructed_model`: The recitation begins by placing the listener under oath before a high ordered domain, then a time already held under promise, then a relational pair of one who bears witness and something/someone witnessed. The opening image is not yet the trench. It is a framework: an upper ordered field, a scheduled disclosure point, and a witness relation prepared before the crime narrative appears.
- `freeze_point`: after `85:3`, before `قُتِلَ أَصْحَابُ الْأُخْدُودِ`.
- `predictions_at_freeze`: a later event needing testimony; an act whose temporal reckoning is not immediate; some contrast between human witness and a higher witness; a closure involving preservation or record.
- `unused_features_tested`: `85:6-7` seated human witnesses; `85:9` Allah as witness over every thing; `85:17` arrival of a report; `85:21-22` Qur'an in protected tablet.
- `corroborators`: `(C: 85:7 شُهُودٌ repeats witness language in the crime scene)`, `(C: 85:9 شَهِيدٌ universalizes the witness role to Allah)`, `(C: 85:17 حديث الجنود supplies report-transmission after prior events)`, `(C: 85:21-22 قرآن في لوح محفوظ supplies preserved record/recitation closure)`.
- `constraints`: `(K: no furuq branch dossier for س م و, ب ر ج, ي و م, و ع د, ش ه د)`, `(K: oath objects do not themselves state the crime; they frame it)`.
- `temporal_reactivation_notes`: `شُهُودٌ` at `85:7` reactivates `شَاهِدٍ وَمَشْهُودٍ` as soon as the persecutors are described watching what they do. `وَاللَّهُ ... شَهِيدٌ` at `85:9` then displaces the human witness frame with a divine one.
- `rival_models`: purely cosmological oath; legal courtroom; eschatological calendaring. The combined witness-field model retains all three without turning any into a translation replacement.
- `grade`: `medium-strong`
- `grade_rationale`: Strong ordered repetition and later reactivation; capped because branch dossiers are unavailable.
- `source_queries_or_rows_used`: `resources/quran/surah_85.json`; attachment rows `85:1 a1-a3`, `85:2 a1-a2`, `85:3 a1-a3`, `85:7 a1`, `85:9 a5-a7`, `85:17 a1-a3`, `85:21 a1-a2`, `85:22 a1`.

### S85-P2-C02 - Human spectators inside a scene already placed under witness

- `candidate_id`: `S85-P2-C02`
- `ayah_range`: `85:3-9`
- `seed_type`: verified composite / constructional
- `seed`: `شَاهِدٍ وَمَشْهُودٍ` as a witness pair.
- `generating_set`: `(E: 85:3 witness pair attachments a1-a3)`, `(E: 85:6 إذ temporal setting)`, `(E: 85:6 هم عليها قعود predication and prep-complement attachments a1-a3)`, `(E: 85:7 هم ... شهود predication attachment a1)`, `(E: 85:7 على ما يفعلون بالمؤمنين scope/action attachments a2-a4)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: The oath's witness pair becomes populated by a grotesque human witness scene: the perpetrators sit over the fire/trench and are themselves witnesses over the action they are doing to the believers. The role of witness is first introduced as solemn and cosmic, then filled locally by agents who watch their own violence.
- `freeze_point`: after `85:7`, before the explanation of motive in `85:8`.
- `predictions_at_freeze`: motive for the action; an affected faithful group; a later witness that judges the human watchers; reversal of the watchers' apparent control.
- `unused_features_tested`: `85:8` exclusive motive; `85:9` divine witness over everything; `85:20` Allah surrounding from behind.
- `corroborators`: `(C: 85:8 إلا أن يؤمنوا supplies the motive and confirms the believers as the affected group)`, `(C: 85:9 والله على كل شيء شهيد supplies a higher witness over the human witnesses)`, `(C: 85:20 من ورائهم محيط reverses their apparent above/on-position into divine surrounding from behind)`.
- `constraints`: `(K: the human witnesses are not neutral legal witnesses; attachment row 85:7 a3 makes ما object content of يفعلون, and a4 attaches بالمؤمنين to the action)`, `(K: no lexical branch IDs for ش ه د, ق ع د, ف ع ل, ء م ن)`.
- `temporal_reactivation_notes`: The earlier indefinite `شاهد ومشهود` remains open until `شهود` at `85:7`, then gets reinterpreted again by `شهيد` at `85:9`.
- `rival_models`: witness as day-of-judgment only; witness as Prophet/community only. The local construction cannot decide the referents exhaustively, but it does show a passage-internal witness escalation.
- `grade`: `medium-strong`
- `grade_rationale`: Excellent temporal reactivation and structural fit; lexical specificity unavailable.
- `source_queries_or_rows_used`: attachment rows `85:3 a1-a3`, `85:6 a1-a3`, `85:7 a1-a4`, `85:8 a1-a7`, `85:9 a5-a7`, `85:20 a1-a3`.

### S85-P2-C03 - Pit, fire, sitting-over, and surrounding-from-behind

- `candidate_id`: `S85-P2-C03`
- `ayah_range`: `85:4-7`, with reactivation at `85:19-22`
- `seed_type`: constructional / spatial
- `seed`: `أَصْحَابُ الْأُخْدُودِ`.
- `generating_set`: `(E: 85:4 قُتِلَ passive event attachment a1)`, `(E: 85:4 أصحاب الأخدود idafa attachment a2)`, `(E: 85:5 النار ذات الوقود adjective/idafa attachments a1-a2)`, `(E: 85:6 عليها قعود prep-complement/predication attachments a1-a2)`, `(E: 85:7 على ما يفعلون ... شهود scope attachments a1-a4)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: A lower cut or trench is immediately filled by a fire specified as possessing fuel. The persecuting group is not merely near it; they are `عليها`, seated over/upon it, and also `على ما يفعلون`, over the deed they perform against the believers. The vertical geometry is pit/fire below, human sitters above, human action beneath their witnessing gaze.
- `freeze_point`: after `85:7`.
- `predictions_at_freeze`: later reversal of enclosure; the above-position will be surrounded or overruled; fire will recur as recompense; a protected higher container may close the scene.
- `unused_features_tested`: `85:10` fire punishment; `85:11` gardens under which rivers flow; `85:20` Allah surrounding from behind; `85:22` protected tablet.
- `corroborators`: `(C: 85:10 عذاب الحريق repeats burning as recompense)`, `(C: 85:11 من تحتها الأنهار reverses destructive lower fire into lower flowing rivers under gardens)`, `(C: 85:20 والله من ورائهم محيط supplies surrounding of the deniers)`, `(C: 85:22 في لوح محفوظ supplies final protected containment rather than exposed trench)`.
- `constraints`: `(K: no branch dossiers for خ د د, ن و ر, و ق د, ق ع د, ح و ط, ل و ح, ح ف ظ)`, `(K: `النار ذات الوقود` is grammatically linked to the trench scene, not an independent cosmic fire at first exposure)`.
- `temporal_reactivation_notes`: The repeated preposition `على` in `عليها` and `على ما يفعلون` makes the human above-position active. `من ورائهم محيط` later reactivates that spatial superiority as false, because the persecutors are themselves enclosed.
- `rival_models`: local historical atrocity only; eschatological fire only. The constructive model keeps the historical fire primary and treats later fire/surrounding as reactivation and reversal.
- `grade`: `medium-strong`
- `grade_rationale`: Strong constructional geometry with clear later reversals; capped for missing lexical branch evidence.
- `source_queries_or_rows_used`: attachment rows `85:4 a1-a2`, `85:5 a1-a2`, `85:6 a1-a3`, `85:7 a1-a4`, `85:10 a5-a13`, `85:11 a6-a9`, `85:20 a1-a3`, `85:22 a1`.

### S85-P2-C04 - The only charge is faith in the owner-witness

- `candidate_id`: `S85-P2-C04`
- `ayah_range`: `85:7-9`
- `seed_type`: constructional / morphosyntactic
- `seed`: `وَمَا نَقَمُوا مِنْهُمْ إِلَّا أَن يُؤْمِنُوا`.
- `generating_set`: `(E: 85:8 ما negation attachment a1)`, `(E: 85:8 نقموا verb)`, `(E: 85:8 منهم governed pronoun attachment a2)`, `(E: 85:8 إلا أن يؤمنوا clausal complement attachment a3)`, `(E: 85:8 أن governs يؤمنوا attachment a4)`, `(E: 85:8 بالله prep-complement attachment a5)`, `(E: 85:8 العزيز الحميد adjectives attachments a6-a7)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: The passage narrows the persecutors' grievance until only one content remains: the victims believe in Allah. The clause turns their violence into a prosecution without a legitimate charge. The divine names immediately add the offended relation: the believed-in Lord is mighty and praised, then described as the one to whom belongs the kingdom of heavens and earth and who witnesses everything.
- `freeze_point`: after `85:8`, before `85:9`.
- `predictions_at_freeze`: the believed-in party will be shown as not vulnerable to the persecutors; the charge will invert into witness and sovereignty; the victims' faith will reappear in a positive reward path.
- `unused_features_tested`: `85:9` ownership and witness; `85:10` persecutors of believing men and women; `85:11` believers who act righteous deeds.
- `corroborators`: `(C: 85:9 له ملك السماوات والأرض confirms the believed-in party as sovereign over the whole domain)`, `(C: 85:9 على كل شيء شهيد confirms the grievance is under total witness)`, `(C: 85:10 المؤمنين والمؤمنات repeats the affected faithful identity)`, `(C: 85:11 الذين آمنوا reopens faith as reward path)`.
- `constraints`: `(K: the construction says the grievance is faith, not that faith lexically means the whole conflict)`, `(K: no branch IDs for ن ق م, ء م ن, ء ل ه, ع ز ز, ح م د)`.
- `temporal_reactivation_notes`: After fire and witness, `إلا أن يؤمنوا` retrospectively explains why the believers were the object of `يفعلون`. The later `آمنوا وعملوا الصالحات` reactivates faith from persecuted cause into salvific identity.
- `rival_models`: political rebellion charge; generic moral hatred. The exclusive exception construction defeats broader charges within the local syntax.
- `grade`: `strong`
- `grade_rationale`: The syntax is precise and independently corroborated by immediate divine ownership/witness and later faith recurrence. Lexical branch support remains unavailable but is less central here.
- `source_queries_or_rows_used`: attachment rows `85:7 a3-a4`, `85:8 a1-a7`, `85:9 a1-a7`, `85:10 a2-a3`, `85:11 a1-a3`.

### S85-P2-C05 - Trial by burning reversed into burning recompense

- `candidate_id`: `S85-P2-C05`
- `ayah_range`: `85:5-10`
- `seed_type`: temporal / constructional
- `seed`: `النار ذات الوقود`.
- `generating_set`: `(E: 85:5 النار ذات الوقود attachments a1-a2)`, `(E: 85:6 هم عليها قعود attachments a1-a3)`, `(E: 85:7 ما يفعلون بالمؤمنين attachments a2-a4)`, `(E: 85:10 فتنوا المؤمنين والمؤمنات attachments a1-a3)`, `(E: 85:10 ثم لم يتوبوا attachment a4)`, `(E: 85:10 فلهم عذاب جهنم / ولهم عذاب الحريق attachments a5-a13)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: The first fire belongs to the persecutors' apparatus, with fuel and seated supervision. Later the act is named `فتنوا` against believing men and women. When no return/repentance occurs, the fire image reverses ownership: `لهم عذاب جهنم` and `لهم عذاب الحريق`. The burning scene is not abandoned; it is turned back on the agents.
- `freeze_point`: after the first punishment clause in `85:10`.
- `predictions_at_freeze`: a second punishment clause may specify the same medium; the victims should receive a contrasted domain; non-repentance should be the hinge between historical action and recompense.
- `unused_features_tested`: second `ولهم عذاب الحريق`; `85:11` gardens/rivers; `85:12` severe grasp.
- `corroborators`: `(C: 85:10 repeated لهم عذاب creates doubled assignment of recompense)`, `(C: 85:10 الحريق explicitly matches burning medium)`, `(C: 85:11 جنات تجري من تحتها الأنهار contrasts the believers' domain with the fire/trench)`, `(C: 85:12 بطش ربك لشديد supplies force behind reversal)`.
- `constraints`: `(K: this is recompense/reversal, not a claim that the historical fire and Jahannam are lexically identical)`, `(K: no furuq branches for ف ت ن, ع ذ ب, ح ر ق, ن و ر, و ق د)`.
- `temporal_reactivation_notes`: The listener hears fire first as the victims' environment, then after `ثُمَّ لَمْ يَتُوبُوا` hears fire as assigned to the perpetrators. `الحريق` reactivates `النار ذات الوقود` with agency reversed.
- `rival_models`: simple punishment after crime; general threat. The repeated fire medium makes reversal more specific than generic punishment.
- `grade`: `medium-strong`
- `grade_rationale`: Strong temporal reversal and repeated medium; lexical depth unavailable.
- `source_queries_or_rows_used`: attachment rows `85:5 a1-a2`, `85:6 a1-a3`, `85:7 a1-a4`, `85:10 a1-a13`, `85:11 a4-a11`, `85:12 a1-a4`.

### S85-P2-C06 - Persecuted belief becomes gardened triumph

- `candidate_id`: `S85-P2-C06`
- `ayah_range`: `85:7-11`
- `seed_type`: temporal / constructional
- `seed`: repeated `ء م ن` occurrences: `بالمؤمنين`, `يؤمنوا`, `المؤمنين والمؤمنات`, `آمنوا`.
- `generating_set`: `(E: 85:7 بالمؤمنين governed complement attachment a4)`, `(E: 85:8 أن يؤمنوا بالله attachments a3-a5)`, `(E: 85:10 فتنوا المؤمنين والمؤمنات attachments a2-a3)`, `(E: 85:11 الذين آمنوا attachment a1)`, `(E: 85:11 وعملوا الصالحات attachments a2-a3)`, `(E: 85:11 لهم جنات تجري من تحتها الأنهار attachments a4-a9)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: Faith first marks the people as targets of an action, then as the only reason for resentment, then as a gender-inclusive persecuted community, then as the opening condition of reward. The same identity is carried through violence into gardens and flowing rivers.
- `freeze_point`: after `85:11` reward clause.
- `predictions_at_freeze`: the positive outcome should be named as success/triumph; its scale should answer the severity of the prior scene; the sequence should preserve faith without treating it as merely passive victimhood.
- `unused_features_tested`: `ذلك الفوز الكبير`; `85:12` severe grasp; `85:14` forgiving/loving.
- `corroborators`: `(C: 85:11 ذلك الفوز الكبير names the outcome as great triumph)`, `(C: 85:11 عملوا الصالحات prevents a purely passive identity; faith is paired with action)`, `(C: 85:14 الغفور الودود supplies relational divine care after threat and reward)`.
- `constraints`: `(K: without branch dossiers, ء م ن cannot be analyzed into branch-specific security/faith images)`, `(K: the reward belongs to those who believed and acted, not automatically to every earlier named victim if the construction is read narrowly)`.
- `temporal_reactivation_notes`: Each recurrence of `ء م ن` changes state: object of violence, content of charge, named persecuted community, rewarded community. This is one of the clearest reactivation chains in S85.
- `rival_models`: martyrdom-only reward; faith-only reward without deeds. The `وعملوا الصالحات` construction constrains the reward path.
- `grade`: `strong`
- `grade_rationale`: High recurrence, clear syntactic roles, and strong temporal development; no branch IDs available.
- `source_queries_or_rows_used`: attachment rows `85:7 a4`, `85:8 a3-a5`, `85:10 a2-a3`, `85:11 a1-a11`, `85:14 a1-a2`.

### S85-P2-C07 - Above/below reversal: from pit-fire to gardens with rivers beneath

- `candidate_id`: `S85-P2-C07`
- `ayah_range`: `85:4-11`
- `seed_type`: morphosyntactic / spatial
- `seed`: spatial prepositions and vertical relations: `الأخدود`, `عليها`, `على ما`, `من تحتها`.
- `generating_set`: `(E: 85:4 أصحاب الأخدود idafa attachment a2)`, `(E: 85:6 عليها governed complement attachment a1)`, `(E: 85:7 على ما scope attachment a2)`, `(E: 85:11 تجري من تحتها الأنهار verbal qualifier and spatial attachments a6-a9)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: The first spatial world is a cut/trench below, a fire in it, and persecutors positioned above it and over their action. The reward world is also vertically arranged, but life-giving rivers run beneath gardens. The lower domain changes from destructive fire under human cruelty to flowing water under divine reward.
- `freeze_point`: after `85:11`.
- `predictions_at_freeze`: the oppressors' above-position should be relativized by a larger surrounding; closure may place revelation inside a protected container.
- `unused_features_tested`: `85:20 من ورائهم محيط`; `85:22 في لوح محفوظ`.
- `corroborators`: `(C: 85:20 من ورائهم محيط encloses those who seemed spatially above/controling)`, `(C: 85:22 في لوح محفوظ supplies protected containment after exposed trench)`.
- `constraints`: `(K: spatial reversal is secondary simulation; primary meaning remains punishment/reward)`, `(K: no lexical branches for خ د د, ت ح ت, ن ه ر, ح و ط, ح ف ظ)`.
- `temporal_reactivation_notes`: The listener first sees lower space as a wound/trench with fire. At `من تحتها الأنهار`, the lower space is reactivated as ordered flow beneath gardens.
- `rival_models`: reward contrast without spatial geometry; fire/water elemental opposition. The prepositional sequence supports spatial geometry beyond mere theme.
- `grade`: `medium`
- `grade_rationale`: Coherent relational image, but dependent on constructional prepositions and unavailable lexical branches.
- `source_queries_or_rows_used`: attachment rows `85:4 a2`, `85:6 a1`, `85:7 a2`, `85:11 a6-a9`, `85:20 a1-a3`, `85:22 a1`.

### S85-P2-C08 - Non-return and divine return

- `candidate_id`: `S85-P2-C08`
- `ayah_range`: `85:10-14`
- `seed_type`: temporal / morphosyntactic
- `seed`: `ثُمَّ لَمْ يَتُوبُوا` followed by `يُبْدِئُ وَيُعِيدُ`.
- `generating_set`: `(E: 85:10 ثم sequence marker)`, `(E: 85:10 لم يتوبوا negated jussive attachment a4)`, `(E: 85:10 فلهم عذاب... punishment predicates attachments a5-a13)`, `(E: 85:13 إنه هو يبدئ ويعيد predication/conjoined attachments a1-a6)`, `(E: 85:14 وهو الغفور الودود parallel predicates attachments a1-a2)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: Human refusal to turn back after persecution becomes the hinge for punishment. Immediately after the reward/threat pair, divine agency is named as beginning and returning/repeating, followed by forgiveness and love. The model contrasts failed human return with divine capacity to originate, restore, and forgive.
- `freeze_point`: after `85:14`.
- `predictions_at_freeze`: divine action should not be limited to punishment; authority and will should follow; earlier historical cycles may be recalled.
- `unused_features_tested`: `85:15-16` throne/glory and doing what He wills; `85:17-18` prior hosts; `85:19-20` current deniers surrounded.
- `corroborators`: `(C: 85:15 ذو العرش المجيد supplies authority/elevation)`, `(C: 85:16 فعال لما يريد supplies unrestricted effective will)`, `(C: 85:17-18 حديث الجنود supplies historical recurrence)`.
- `constraints`: `(K: توبة and عود cannot be lexically related without branch dossiers; the relation here is temporal/conceptual, not asserted root evidence)`, `(K: forgiveness/love means the agency cluster is not only retaliatory)`.
- `temporal_reactivation_notes`: After `لم يتوبوا`, the later `يعيد` strongly reactivates the possibility of return/repetition at the level of divine action rather than human repentance.
- `rival_models`: punishment-only; creation/resurrection-only. The local order supports a broader begin/return agency cluster but cannot settle all theological scope.
- `grade`: `medium`
- `grade_rationale`: Good sequence logic and role contrast; lexical relation unavailable.
- `source_queries_or_rows_used`: attachment rows `85:10 a4-a13`, `85:13 a1-a6`, `85:14 a1-a2`, `85:15 a1-a2`, `85:16 a1-a2`, `85:17 a1-a3`.

### S85-P2-C09 - Severe grasp anchored by throne, will, and surrounding

- `candidate_id`: `S85-P2-C09`
- `ayah_range`: `85:12-20`
- `seed_type`: verified composite / constructional
- `seed`: `إِنَّ بَطْشَ رَبِّكَ لَشَدِيدٌ`.
- `generating_set`: `(E: 85:12 بطش ربك idafa attachments a1-a3)`, `(E: 85:12 لشديد predicate attachment a4)`, `(E: 85:15 ذو العرش المجيد attachments a1-a2)`, `(E: 85:16 فعال لما يريد attachments a1-a2)`, `(E: 85:20 والله من ورائهم محيط attachments a1-a3)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: The divine response is first condensed as severe grasp, then expanded into authority (`ذو العرش`), effective agency (`فعال لما يريد`), and enclosure (`محيط`) around those in denial. The grasp is not impulsive force; it is enthroned, will-directed, and spatially encompassing.
- `freeze_point`: after `85:16`, before the historical-host insertion and current denial statement.
- `predictions_at_freeze`: prior examples of powerful opponents; current opponents placed inside a larger enclosure; final speech/record protected by that authority.
- `unused_features_tested`: `85:17-18` Pharaoh and Thamud; `85:19` those who disbelieve in denial; `85:21-22` glorious Qur'an in protected tablet.
- `corroborators`: `(C: 85:17-18 فرعون وثمود supply paradigmatic powerful hosts)`, `(C: 85:19 في تكذيب places current deniers inside denial)`, `(C: 85:20 من ورائهم محيط fulfills surrounding/enclosure)`, `(C: 85:21-22 قرآن مجيد في لوح محفوظ carries authority into preserved revelation)`.
- `constraints`: `(K: no branch dossiers for ب ط ش, ش د د, ع ر ش, ف ع ل, ر و د, ح و ط)`, `(K: severe grasp is syntactically possessed by ربك, not an autonomous force)`.
- `temporal_reactivation_notes`: The force announced at `85:12` waits through divine attributes and historical examples before becoming spatially vivid in `محيط`.
- `rival_models`: isolated threat; general omnipotence statement. The passage order favors force plus authority plus surrounding control.
- `grade`: `medium-strong`
- `grade_rationale`: Strong constructional expansion from force to authority to enclosure; no lexical branch specificity.
- `source_queries_or_rows_used`: attachment rows `85:12 a1-a4`, `85:15 a1-a2`, `85:16 a1-a2`, `85:17 a1-a3`, `85:18 a1`, `85:19 a1-a2`, `85:20 a1-a3`, `85:21 a1-a2`, `85:22 a1`.

### S85-P2-C10 - Historical recurrence: trench owners, hosts, and current deniers

- `candidate_id`: `S85-P2-C10`
- `ayah_range`: `85:4-20`
- `seed_type`: temporal / discourse
- `seed`: `هَلْ أَتَىٰكَ حَدِيثُ الْجُنُودِ`.
- `generating_set`: `(E: 85:4 أصحاب الأخدود earlier destroyed group)`, `(E: 85:17 هل أتاك direct-object/subject attachments a1-a2)`, `(E: 85:17 حديث الجنود idafa attachment a3)`, `(E: 85:18 فرعون وثمود conjoined attachment a1)`, `(E: 85:19 بل الذين كفروا في تكذيب attachments a1-a2)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: The trench owners are not left as a one-off atrocity. The discourse later asks whether the report of hosts has come, names Pharaoh and Thamud, then turns with `بل` to current disbelievers in denial. The image is serial opposition: past perpetrators, historical hosts, current deniers, all placed under divine surrounding.
- `freeze_point`: after `85:19`.
- `predictions_at_freeze`: the current deniers will be enclosed despite apparent continuation; the closing will assert the recitation's protected authority.
- `unused_features_tested`: `85:20` surrounding from behind; `85:21-22` Qur'an in protected tablet.
- `corroborators`: `(C: 85:20 محيط gives the serial opposition a present containment)`, `(C: 85:21 بل هو قرآن مجيد shifts from historical report to present recitation)`, `(C: 85:22 في لوح محفوظ stabilizes the report/recitation as preserved)`.
- `constraints`: `(K: Pharaoh and Thamud are named examples, not branch evidence from the S85 roots)`, `(K: no branch dossiers for ح د ث, ج ن د, ك ف ر, ك ذ ب, ح و ط)`.
- `temporal_reactivation_notes`: `حديث الجنود` reactivates the earlier `أصحاب الأخدود` as part of a wider archive of hostile groups. `بل الذين كفروا` prevents the listener from leaving the pattern in the past.
- `rival_models`: detached consolation examples; generic history. The `بل` sequence ties the examples to current denial.
- `grade`: `medium`
- `grade_rationale`: Good discourse-level recurrence; lexical support unavailable and named proper examples are structurally but not lexically analyzed.
- `source_queries_or_rows_used`: attachment rows `85:4 a1-a2`, `85:17 a1-a3`, `85:18 a1`, `85:19 a1-a2`, `85:20 a1-a3`, `85:21 a1-a2`, `85:22 a1`.

### S85-P2-C11 - Denial as enclosure, then deniers enclosed from behind

- `candidate_id`: `S85-P2-C11`
- `ayah_range`: `85:19-20`
- `seed_type`: constructional / morphosyntactic
- `seed`: `فِي تَكْذِيبٍ`.
- `generating_set`: `(E: 85:19 الذين كفروا subject/relative group)`, `(E: 85:19 في تكذيب prep-complement attachment a1)`, `(E: 85:19 predication attachment a2)`, `(E: 85:20 والله subject)`, `(E: 85:20 من ورائهم complement attachment a1)`, `(E: 85:20 محيط predicate attachment a3)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: The current disbelievers are not merely performing denial; they are `في تكذيب`, inside a denial-state. The next verse surrounds them from behind with Allah's encompassing presence. Their mental/discursive enclosure is met by a greater divine enclosure.
- `freeze_point`: after `85:20`.
- `predictions_at_freeze`: closure will shift to the protected status of the recitation, not merely the state of deniers.
- `unused_features_tested`: `85:21-22` Qur'an and protected tablet.
- `corroborators`: `(C: 85:21 بل هو قرآن مجيد answers denial with the status of the recited object)`, `(C: 85:22 في لوح محفوظ repeats containment positively as preservation rather than denial-state)`.
- `constraints`: `(K: في تكذيب is a predicate PP, not necessarily a physical container)`, `(K: من ورائهم محيط is divine surrounding, not the same enclosure as denial; relation is analogical/secondary)`.
- `temporal_reactivation_notes`: The preposition `في` in `في تكذيب` is reactivated by `في لوح محفوظ`: first a negative state containing deniers, then a protected container holding the Qur'an.
- `rival_models`: denial as mere action; surrounding as threat only. The PP construction favors state/enclosure imagery.
- `grade`: `medium-strong`
- `grade_rationale`: Strong morphosyntactic enclosure pair and immediate closure; no branch dossiers.
- `source_queries_or_rows_used`: attachment rows `85:19 a1-a2`, `85:20 a1-a3`, `85:21 a1-a2`, `85:22 a1`.

### S85-P2-C12 - Preserved recitation closes the witness-record structure

- `candidate_id`: `S85-P2-C12`
- `ayah_range`: `85:1-3`, `85:9`, `85:17`, `85:21-22`
- `seed_type`: verified composite / temporal
- `seed`: `بَلْ هُوَ قُرْآنٌ مَجِيدٌ فِي لَوْحٍ مَحْفُوظٍ`.
- `generating_set`: `(E: 85:21 هو قرآن predication attachment a1)`, `(E: 85:21 مجيد adjective attachment a2)`, `(E: 85:22 في لوح محفوظ adjective attachment a1)`, `(E: 85:3 شاهد ومشهود witness pair)`, `(E: 85:9 والله على كل شيء شهيد scope attachments a5-a7)`, `(E: 85:17 حديث الجنود report construction attachment a3)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: The passage closes by identifying the present recitation as glorious Qur'an in a protected tablet. This retrospectively stabilizes the earlier witness and report motifs: the crime was watched, the Lord is witness over every thing, reports of hosts arrive, and the recitation itself is preserved.
- `freeze_point`: after `85:22`, final closure.
- `predictions_at_freeze`: no further passage features remain; closure should explain why witness/report language does not need another narrative ending.
- `unused_features_tested`: none after final closure; backward test against oath, witness, report, denial, and surrounding.
- `corroborators`: `(C: 85:3 witness pair sets record/testimony expectation)`, `(C: 85:9 على كل شيء شهيد universalizes recordability)`, `(C: 85:17 حديث supplies transmitted report)`, `(C: 85:19 في تكذيب gives the rival denial-state answered by Qur'an)`, `(C: 85:20 محيط supplies divine control around deniers before preserved closure)`.
- `constraints`: `(K: closing does not make the Qur'an merely a document in the human crime scene; it is the protected recitation that answers denial)`, `(K: no lexical branches for ق ر ء, م ج د, ل و ح, ح ف ظ)`.
- `temporal_reactivation_notes`: The final `في لوح محفوظ` reactivates the opening witness field as durable record. It also contrasts `في تكذيب`: denial is an unstable containment; the Qur'an is in protected containment.
- `rival_models`: simple praise of Qur'an only; legal archive only. The passage's prior witness/report chain makes preserved-recitation closure more explanatory.
- `grade`: `medium-strong`
- `grade_rationale`: Strong final reactivation of witness/report/denial; no branch-level lexical support.
- `source_queries_or_rows_used`: attachment rows `85:3 a1-a3`, `85:9 a5-a7`, `85:17 a1-a3`, `85:19 a1-a2`, `85:20 a1-a3`, `85:21 a1-a2`, `85:22 a1`.

### S85-P2-C13 - Divine names bridge violated believers and cosmic ownership

- `candidate_id`: `S85-P2-C13`
- `ayah_range`: `85:8-16`
- `seed_type`: morphosyntactic / temporal
- `seed`: divine attribute chain beginning with `اللَّهِ الْعَزِيزِ الْحَمِيدِ`.
- `generating_set`: `(E: 85:8 بالله prep-complement attachment a5)`, `(E: 85:8 العزيز والحميد adjectives attachments a6-a7)`, `(E: 85:9 الذي له ملك السماوات والأرض predication/idafa attachments a1-a4)`, `(E: 85:9 والله على كل شيء شهيد attachments a5-a7)`, `(E: 85:12 بطش ربك لشديد attachments a1-a4)`, `(E: 85:13 يبدئ ويعيد attachments a1-a6)`, `(E: 85:14 الغفور الودود attachments a1-a2)`, `(E: 85:15 ذو العرش المجيد attachments a1-a2)`, `(E: 85:16 فعال لما يريد attachments a1-a2)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: The God in whom belief provokes persecution is immediately unfolded through attributes and actions: mighty/praised, owner of heavens and earth, witness over every thing, severe in grasp, originator and returner, forgiving and loving, possessor of the throne, glorious, active over what He wills. The attributes bridge the victims' vulnerable social position and the true scale of the one they trust.
- `freeze_point`: after `85:16`.
- `predictions_at_freeze`: hostile groups will be relativized by this scale; current denial will be enclosed; the recitation will be marked with matching glory/preservation.
- `unused_features_tested`: `85:17-18` hosts; `85:19-20` deniers surrounded; `85:21` Qur'an `مجيد`.
- `corroborators`: `(C: 85:17-18 historical hosts test the divine scale against worldly power)`, `(C: 85:20 محيط applies divine encompassing to current opponents)`, `(C: 85:21 مجيد reactivates 85:15 المجيد as glory transferred to the Qur'an's description)`.
- `constraints`: `(K: attribute chain must remain divine predication, not a secondary translation of faith)`, `(K: no lexical branches for ع ز ز, ح م د, م ل ك, ش ه د, ب ط ش, غ ف ر, و د د, م ج د)`.
- `temporal_reactivation_notes`: `المجيد` at `85:15` is reactivated by `قرآن مجيد` at `85:21`, linking divine majesty to the preserved recitation.
- `rival_models`: independent list of attributes; consolation block only. The repeated ties to persecution, hosts, denial, and Qur'an make it a bridge structure.
- `grade`: `medium`
- `grade_rationale`: Broad but coherent; grade capped by width and lack of branch-specific evidence.
- `source_queries_or_rows_used`: attachment rows `85:8 a5-a7`, `85:9 a1-a7`, `85:12 a1-a4`, `85:13 a1-a6`, `85:14 a1-a2`, `85:15 a1-a2`, `85:16 a1-a2`, `85:17 a1-a3`, `85:20 a1-a3`, `85:21 a2`.

### S85-P2-C14 - Repeated possession: false owners, true owner, possessed fire, possessed throne

- `candidate_id`: `S85-P2-C14`
- `ayah_range`: `85:1-16`
- `seed_type`: morphosyntactic / constructional
- `seed`: repeated possession/idafa constructions: `ذات البروج`, `أصحاب الأخدود`, `ذات الوقود`, `له ملك`, `ذو العرش`.
- `generating_set`: `(E: 85:1 ذات البروج attachments a2-a3)`, `(E: 85:4 أصحاب الأخدود attachment a2)`, `(E: 85:5 ذات الوقود attachments a1-a2)`, `(E: 85:9 له ملك السماوات والأرض attachments a1-a4)`, `(E: 85:15 ذو العرش attachment a1)`.
- `selected_branches`: no furuq branches available.
- `constructed_model`: The passage repeatedly marks possession or belonging. The sky possesses towers/constellations; the condemned people are "owners/companions" of the trench; the fire possesses fuel; Allah possesses the kingdom of heavens and earth; He is possessor of the throne. The early human and material possessive frames are swallowed by divine possession.
- `freeze_point`: after `85:15`.
- `predictions_at_freeze`: the one with true possession will act according to will; current deniers will not own the interpretive field; the recitation will be held in protection.
- `unused_features_tested`: `85:16 فعال لما يريد`; `85:19 في تكذيب`; `85:22 في لوح محفوظ`.
- `corroborators`: `(C: 85:16 فعال لما يريد confirms effective possession/agency)`, `(C: 85:20 محيط confirms deniers are within divine surround, not owners of the scene)`, `(C: 85:22 محفوظ confirms protected holding)`.
- `constraints`: `(K: possession constructions are heterogeneous; `ذات`, `أصحاب`, `له ملك`, and `ذو` are not identical)`, `(K: no branch dossiers for ذ و و because QAC/furuq unavailable; constructional only)`.
- `temporal_reactivation_notes`: `أصحاب الأخدود` initially gives the persecutors an identity by association with the trench. `له ملك السماوات والأرض` later reorders all ownership under Allah.
- `rival_models`: simple genitive catalogue; ownership theme. The temporal order adds false/local possession yielding to true/comprehensive possession.
- `grade`: `medium`
- `grade_rationale`: Interesting repeated construction, but heterogeneous and branch-light.
- `source_queries_or_rows_used`: attachment rows `85:1 a2-a3`, `85:4 a2`, `85:5 a1-a2`, `85:9 a1-a4`, `85:15 a1`, `85:16 a1-a2`, `85:20 a1-a3`, `85:22 a1`.

## Failed or blocked singleton seed passes

The following singleton lexical seeds were initiated but produced no branch-level synthesis because the required furuq branch dossier is unavailable. They may still participate as surface/root occurrences in the constructional candidates above, but no branch image is claimed:

- `85:1 س م و`, `85:1 ب ر ج`
- `85:2 ي و م`, `85:2 و ع د`
- `85:3 ش ه د` active and passive occurrences
- `85:4 ق ت ل`, `ص ح ب`, `خ د د`
- `85:5 ن و ر`, `و ق د`
- `85:6 ق ع د`
- `85:7 ف ع ل`, `ء م ن`, `ش ه د`
- `85:8 ن ق م`, `ء م ن`, `ء ل ه`, `ع ز ز`, `ح م د`
- `85:9 م ل ك`, `س م و`, `ء ر ض`, `ء ل ه`, `ك ل ل`, `ش ي ء`, `ش ه د`
- `85:10 ف ت ن`, `ء م ن`, `ت و ب`, `ع ذ ب`, `ح ر ق`
- `85:11 ء م ن`, `ع م ل`, `ص ل ح`, `ج ن ن`, `ج ر ي`, `ت ح ت`, `ن ه ر`, `ف و ز`, `ك ب ر`
- `85:12 ب ط ش`, `ر ب ب`, `ش د د`
- `85:13 ب د ء`, `ع و د`
- `85:14 غ ف ر`, `و د د`
- `85:15 ع ر ش`, `م ج د`
- `85:16 ف ع ل`, `ر و د`
- `85:17 ء ت ي`, `ح د ث`, `ج ن د`
- `85:19 ك ف ر`, `ك ذ ب`
- `85:20 ء ل ه`, `و ر ي`, `ح و ط`
- `85:21 ق ر ء`, `م ج د`
- `85:22 ل و ح`, `ح ف ظ`

## Image packet catalog

### IMAGE-S85-01

Starting seed: `85:1-3` oath sequence.

Complete image: Upper ordered field, appointed time, and witness relation prepare a record/witness architecture.

Passage-order assembly: sky with `بروج` -> promised day -> witness/witnessed -> human witnesses over crime -> Allah witness over every thing -> report of hosts -> glorious Qur'an in protected tablet.

Participants and roles: sky/order frame; promised day as scheduled disclosure; human perpetrators as corrupted witnesses; Allah as total witness; Qur'an/tablet as preserved record.

Operation / mechanism: oath opens roles; later witness terms fill and revise them.

Direction / force / medium: vertical/cosmic-to-human-to-divine.

Temporal development: open witness slot, local crime witness, divine witness, preserved recitation.

Outcome / closure: protected Qur'an closes the witness-record chain.

Exact branch constituents: none available; constructional evidence only.

Unfilled roles, if any: exact lexical branch images for all roots.

Status: FRAGMENT, because branch dossiers are missing.

### IMAGE-S85-02

Starting seed: `أصحاب الأخدود`.

Complete image: Trench/fire below, perpetrators seated above and watching their deed, later surrounded from behind and assigned burning punishment.

Passage-order assembly: trench -> fire with fuel -> sitting over it -> witnessing over their action -> trial of believers -> punishment of burning -> Allah surrounding from behind.

Participants and roles: persecutors as apparent above-controllers; believers as acted-upon faithful group; fire as first instrument and later recompense; Allah as surrounding authority.

Operation / mechanism: spatial superiority is reversed by divine enclosing and fiery recompense.

Direction / force / medium: above/below; fire; surrounding from behind.

Temporal development: instrument of persecution becomes image of punishment.

Outcome / closure: deniers are enclosed; Qur'an is protected.

Exact branch constituents: none available; constructional evidence only.

Unfilled roles, if any: branch-specific senses of trench, fire, sitting, surrounding.

Status: FRAGMENT.

### IMAGE-S85-03

Starting seed: repeated `ء م ن` occurrences.

Complete image: Faith marks the group as target, charge, persecuted community, then rewarded community.

Passage-order assembly: believers acted against -> only charge is belief in Allah -> believing men and women are tried -> those who believe and act righteous deeds receive gardens -> great triumph.

Participants and roles: believers as object/charge/community/reward recipients; persecutors as resenters/testers; Allah as believed-in sovereign; righteous deeds as active completion.

Operation / mechanism: recurrence changes the state of the same identity across the recitation.

Direction / force / medium: social violence to divine reward.

Temporal development: victim identity becomes triumph identity.

Outcome / closure: `الفوز الكبير`.

Exact branch constituents: none available; constructional/repetition evidence only.

Unfilled roles, if any: branch-specific ء م ن dimensions.

Status: FRAGMENT.

### IMAGE-S85-04

Starting seed: `في تكذيب`.

Complete image: Deniers are inside denial while Allah surrounds them from behind; the Qur'an is in a protected tablet.

Passage-order assembly: current disbelievers -> in denial -> Allah surrounding -> Qur'an glorious -> in protected tablet.

Participants and roles: deniers as enclosed in denial; Allah as encompassing; Qur'an as preserved object; tablet as secure container.

Operation / mechanism: negative containment is answered by stronger divine containment and positive preservation.

Direction / force / medium: interior state and surrounding boundary.

Temporal development: `في تكذيب` reactivated by `في لوح محفوظ`.

Outcome / closure: preserved recitation defeats denial-state.

Exact branch constituents: none available; constructional evidence only.

Unfilled roles, if any: branch-specific meanings for ك ذ ب, ح و ط, ل و ح, ح ف ظ.

Status: FRAGMENT.

## Exhaustiveness check after file creation

Checks performed in this Pass 2 artifact:

- Restarted from the first rooted occurrence `85:1 وَالسَّمَاءِ`.
- Listed every recoverable rooted occurrence through `85:22 مَحْفُوظٍ`.
- Initiated singleton lexical seed status for every listed occurrence/root.
- Marked every lexical seed as blocked where furuq/QAC branch data was required.
- Initiated actual constructional, morphosyntactic, temporal, and repetition seeds from the passage.
- Preserved construction/corroboration/constraint separation in each candidate.
- Did not invent branch IDs, branch images, or QAC morphology from unavailable databases.

Remaining non-exhaustive component: true branch-level lexical Pass 2 remains impossible until `resources/qac.sqlite` and `resources/furuq_v4.sqlite` contain their expected tables and rows.
