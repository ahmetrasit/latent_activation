# S93 Stage 1 Pass 2: Temporally Conditioned Reactivation

Assigned passage: S93  
Sacred Arabic text source: `resources/quran/surah_93.json`  
Prompt source: `v1/prompts/stage1.md`  
Output: `v1/outputs/93-stage1-pass-2.md`

## Root Cause of Pass 1 Limitation

Pass 1 visited only a limited number of words per finding because the two prompt-authorized SQLite resources required for exhaustive lexical work were not available in the local workspace:

- `resources/qac.sqlite`: unavailable.
- `resources/furuq_v4.sqlite`: unavailable.

Those two files are the only authorized sources in the Stage 1 prompt for QAC word/morpheme inventory and uncontaminated furuq branch dossiers. Without them, I cannot truthfully enumerate every accepted branch ID for each passage root, preserve `branch_image_ar` and `what_is_ar`, or run full branch-by-branch singleton seeding. I therefore restarted from the first rooted word and performed the maximum possible Pass 2 sweep using only the still-available authorized evidence:

- sacred Arabic text from `resources/quran/surah_93.json`;
- S93 structural rows from `resources/attachments.tsv`.

No translation evidence was used. No unlisted branch or morphology resource was used as evidence.

## Sacred Text

0. بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
1. وَٱلضُّحَىٰ
2. وَٱلَّيْلِ إِذَا سَجَىٰ
3. مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ
4. وَلَلْءَاخِرَةُ خَيْرٌۭ لَّكَ مِنَ ٱلْأُولَىٰ
5. وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ
6. أَلَمْ يَجِدْكَ يَتِيمًۭا فَـَٔاوَىٰ
7. وَوَجَدَكَ ضَآلًّۭا فَهَدَىٰ
8. وَوَجَدَكَ عَآئِلًۭا فَأَغْنَىٰ
9. فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ
10. وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ
11. وَأَمَّا بِنِعْمَةِ رَبِّكَ فَحَدِّثْ

## Authorized Structural Evidence From Attachments

Attachment rows available for S93:

- 93:2 `إِذَا` is an adverbial time setting for `سَجَىٰ`.
- 93:3 suffix `كَ` is object of `وَدَّعَكَ`; `رَبُّكَ` is subject; `قَلَىٰ` is coordinated with the preceding negated verb.
- 93:4 `خَيْرٌ` predicates superiority of `ٱلْءَاخِرَةُ`; `لَّكَ` is beneficiary complement; `مِنَ ٱلْأُولَىٰ` is comparison complement.
- 93:5 suffix `كَ` is object of `يُعْطِيكَ`; `رَبُّكَ` is subject; `تَرْضَىٰ` is result linked by `فَ`; `لَسَوْفَ` marks future assertion.
- 93:6 `أَلَمْ` governs `يَجِدْكَ`; suffix `كَ` is object; `يَتِيمًا` is either circumstantial or second object complement; `فَآوَىٰ` is consequent action.
- 93:7 suffix `كَ` is object of `وَجَدَكَ`; `ضَالًّا` is either circumstantial or second object complement; `فَهَدَىٰ` is consequent action.
- 93:8 suffix `كَ` is object of `وَجَدَكَ`; `عَائِلًا` is either circumstantial or second object complement; `فَأَغْنَىٰ` is consequent action.
- 93:9 `ٱلْيَتِيمَ` is fronted direct object of `تَقْهَرْ`; prohibitive `لَا` governs `تَقْهَرْ`.
- 93:10 `ٱلسَّائِلَ` is fronted direct object of `تَنْهَرْ`; prohibitive `لَا` governs `تَنْهَرْ`.
- 93:11 `نِعْمَةِ` is governed by `بـ` as complement of `حَدِّثْ`; `رَبِّكَ` is genitive possessor in `نِعْمَةِ رَبِّكَ`; suffix `كَ` is possessor of `رَبّ`.

## Exhaustive Seed Restart

The following sweep restarts at the first eligible rooted word in the passage order. Because branch dossiers are unavailable, every lexical seed is marked as `branch_dossier_unavailable`; where structural evidence still forms a candidate image, the candidate is retained with branch IDs absent by necessity. Grades are capped at weak unless supported by independent structural convergence.

### Lexical Occurrence Seeds

| seed_id | occurrence | root/source status | pass result |
| --- | --- | --- | --- |
| S93-L001 | 93:1 `ٱلضُّحَىٰ` | QAC/furuq unavailable | Failed lexical branch pass. Initial image from surface position only: bright opening / exposed daybreak cue. It predicts contrastive darkness and later reassurance, but no branch ID can be cited. Grade: weak. |
| S93-L002 | 93:2 `ٱلَّيْلِ` | QAC/furuq unavailable | Failed lexical branch pass. Surface-position image: night as opposite member of oath pair. Predicts dark interval as non-abandonment rather than rejection. Grade: weak. |
| S93-L003 | 93:2 `إِذَا` | attachment root row only | Constructional-temporal seed retained under C001, not lexical branch seed. Attachment: time setting for `سَجَىٰ`. Grade: medium as structure, weak as lexical branch. |
| S93-L004 | 93:2 `سَجَىٰ` | attachment root `س ج و`; furuq unavailable | Failed branch pass but structurally useful. Initial image: settling/covering night event governed by `إِذَا`. Predicts pause/rest not abandonment. Grade: weak-medium structurally. |
| S93-L005 | 93:3 `وَدَّعَكَ` | attachment root `و د ع`; furuq unavailable | Failed branch pass; retained structurally as negated separation. Direct object `كَ`, subject `رَبُّكَ`, and negation constrain it to denied abandonment. Grade: medium structurally. |
| S93-L006 | 93:3 `رَبُّكَ` | attachment root `ر ب ب`; furuq unavailable | Failed branch pass; retained as recurring actor/source seed. It becomes subject of denied farewell and future giving, possessor of final blessing. Grade: medium structurally. |
| S93-L007 | 93:3 `قَلَىٰ` | attachment root `ق ل ي`; furuq unavailable | Failed branch pass; structurally retained as second negated rejection verb coordinated with `وَدَّعَكَ`. Grade: weak-medium. |
| S93-L008 | 93:4 `ٱلْءَاخِرَةُ` | attachment root `أ خ ر`; furuq unavailable | Failed branch pass; retained in comparison construction C003. Later term is predicated better. Grade: medium structurally. |
| S93-L009 | 93:4 `خَيْرٌ` | attachment root `خ ي ر`; furuq unavailable | Failed branch pass; retained as comparative value predicate binding later-to-you-over-first. Grade: medium structurally. |
| S93-L010 | 93:4 `ٱلْأُولَىٰ` | attachment root `و ل ي`; furuq unavailable | Failed branch pass; retained as earlier/first pole in comparison. Grade: weak-medium. |
| S93-L011 | 93:5 `لَسَوْفَ` | attachment root `س و ف`; furuq unavailable | Temporal particle seed retained in C004. Predicts future completion rather than present closure. Grade: medium structurally. |
| S93-L012 | 93:5 `يُعْطِيكَ` | attachment root `ع ط و`; furuq unavailable | Failed branch pass; retained as future transfer/giving event with `كَ` object and `رَبُّكَ` subject. Grade: medium structurally. |
| S93-L013 | 93:5 `رَبُّكَ` | attachment root `ر ب ب`; furuq unavailable | Recurrence seed converges with L006/L031. Subject of future giving. Grade: medium structurally. |
| S93-L014 | 93:5 `تَرْضَىٰ` | attachment root `ر ض ي`; furuq unavailable | Failed branch pass; retained as result endpoint of giving. Grade: medium structurally. |
| S93-L015 | 93:6 `أَلَمْ` | attachment root `ل م م`; furuq unavailable | Interrogative-negation construction seed retained in C005. It reopens memory as evidence. Grade: medium structurally. |
| S93-L016 | 93:6 `يَجِدْكَ` | attachment root `ج د د`; furuq unavailable | Failed branch pass; retained as first find-you-state frame. Grade: medium structurally. |
| S93-L017 | 93:6 `يَتِيمًا` | attachment root `ي ت م`; furuq unavailable | Failed branch pass; retained strongly by recurrence in 93:9 as object of prohibition. Grade: medium-strong structurally. |
| S93-L018 | 93:6 `فَآوَىٰ` | attachment root `أ و ي`; furuq unavailable | Failed branch pass; retained as consequent remedy after found-state. Grade: medium structurally. |
| S93-L019 | 93:7 `وَجَدَكَ` | attachment root `و ج د`; furuq unavailable | Failed branch pass; retained as second find-you-state frame. Grade: medium structurally. |
| S93-L020 | 93:7 `ضَالًّا` | attachment root `ض ل ل`; furuq unavailable | Failed branch pass; retained as second deficient/exposed state, remedied by guidance. Grade: medium structurally. |
| S93-L021 | 93:7 `فَهَدَىٰ` | attachment root `ه د ي`; furuq unavailable | Failed branch pass; retained as consequent remedy. Grade: medium structurally. |
| S93-L022 | 93:8 `وَجَدَكَ` | attachment root `و ج د`; furuq unavailable | Failed branch pass; retained as third find-you-state frame. Grade: medium structurally. |
| S93-L023 | 93:8 `عَائِلًا` | attachment root `ع ي ل`; furuq unavailable | Failed branch pass; retained as third deficient/exposed state, remedied by enrichment. Grade: medium structurally. |
| S93-L024 | 93:8 `فَأَغْنَىٰ` | attachment root `غ ن ي`; furuq unavailable | Failed branch pass; retained as consequent remedy. Grade: medium structurally. |
| S93-L025 | 93:9 `ٱلْيَتِيمَ` | attachment root `ي ت م`; furuq unavailable | Failed branch pass; retained strongly by backward reactivation of 93:6 `يَتِيمًا`. Grade: medium-strong structurally. |
| S93-L026 | 93:9 `تَقْهَرْ` | attachment root `ق ه ر`; furuq unavailable | Failed branch pass; retained as prohibited action against reactivated orphan role. Grade: medium structurally. |
| S93-L027 | 93:10 `ٱلسَّائِلَ` | attachment root `س أ ل`; furuq unavailable | Failed branch pass; retained as fronted object in second prohibition. Predicts needy requester matching prior lack motif but no lexical branch can test. Grade: medium structurally. |
| S93-L028 | 93:10 `تَنْهَرْ` | attachment root `ن ه ر`; furuq unavailable | Failed branch pass; retained as prohibited action against requester. Grade: weak-medium structurally. |
| S93-L029 | 93:11 `نِعْمَةِ` | attachment root `ن ع م`; furuq unavailable | Failed branch pass; retained as final object/medium of commanded telling; reactivates the received remedies. Grade: medium structurally. |
| S93-L030 | 93:11 `رَبِّكَ` | attachment root `ر ب ب`; furuq unavailable | Recurrence seed: same divine-source relation closes as possessor of blessing. Grade: medium-strong structurally. |
| S93-L031 | 93:11 `حَدِّثْ` | attachment root `ح د ث`; furuq unavailable | Failed branch pass; retained as final command whose complement is `بِنِعْمَةِ رَبِّكَ`. Grade: medium structurally. |

## Candidate Synthesis Units

### S93-C001: Light-Night Non-Abandonment Frame

- `candidate_id`: S93-C001
- `ayah_range`: 93:1-3
- `seed_type`: constructional / temporal
- `seed`: opening oath pair `وَٱلضُّحَىٰ` then `وَٱلَّيْلِ إِذَا سَجَىٰ`
- `generating_set`: passage order 93:1 then 93:2; attachment 93:2 `إِذَا` time-setting for `سَجَىٰ`; 93:3 double negation.
- `selected_branches`: none available; `branch_dossier_unavailable`.
- `constructed_model`: the recitation opens with a bright exposure cue, then moves to night when it settles, then denies two forms of relational rupture. The night cue is not allowed to mean divine absence because the next clause blocks abandonment and aversion.
- `freeze_point`: after 93:3 double negation.
- `predictions_at_freeze`: a dark interval should be reinterpreted as a temporary phase, not rejection; the addressee remains attached to `رَبُّكَ`; later sequence should supply future or remedial continuation.
- `unused_features_tested`: 93:4 later-over-first comparison; 93:5 future giving; 93:6-8 past remedies; 93:9-11 imperatives.
- `corroborators`: `(C: attachment 93:3 ربك subject of negated ودعك)`, `(C: attachment 93:3 قلى coordinated with ودعك)`, `(C: attachment 93:5 لسوف future assertion)`.
- `constraints`: `(K: no lexical branch IDs; cannot establish الضحى/ليل/سجى branch images)`.
- `temporal_reactivation_notes`: 93:2 is heard before the denial; after 93:3, settled night is replayed as non-abandoning quiet rather than evidence of rupture.
- `rival_models`: static contrast of day/night only; devotional oath only. These are possible but explain less of the immediate denial sequence.
- `grade`: medium
- `grade_rationale`: structurally coherent and order-sensitive, but lexically under-supported because furuq branches are unavailable.
- `source_queries_or_rows_used`: sacred Arabic 93:1-3; attachment row 93:2:a1; 93:3:a1-a4.

### S93-C002: Denied Severance Becomes Future Compensation

- `candidate_id`: S93-C002
- `ayah_range`: 93:3-5
- `seed_type`: morphosyntactic / temporal
- `seed`: `مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ`
- `generating_set`: negated `وَدَّعَكَ`; subject `رَبُّكَ`; coordinated negated `قَلَىٰ`; comparison `ٱلْءَاخِرَةُ خَيْرٌ لَّكَ مِنَ ٱلْأُولَىٰ`; future giving `يُعْطِيكَ رَبُّكَ فَتَرْضَىٰ`.
- `selected_branches`: none available; `branch_dossier_unavailable`.
- `constructed_model`: a relational severance hypothesis is explicitly inhibited, then replaced by a temporal-value model: the later state is better for the addressee than the earlier, and future giving from the same `رَبّ` reaches satisfaction.
- `freeze_point`: after 93:5.
- `predictions_at_freeze`: past evidence should show the same source did not abandon; later ethics should transform received care into care for parallel exposed roles.
- `unused_features_tested`: 93:6-8 found-state/remedy triad; 93:9-11 imperatives.
- `corroborators`: `(C: attachment 93:4 خير predicates superiority of الآخرة)`, `(C: attachment 93:4 لك beneficiary)`, `(C: attachment 93:5 ربك subject of يعطيك)`, `(C: attachment 93:5 فترضى result of يعطيك)`.
- `constraints`: `(K: branch dossiers absent for ودع, قلى, أخر, خير, ع ط و, رضي)`.
- `temporal_reactivation_notes`: the same `رَبُّكَ` denied as abandoner returns as giver; this reactivates 93:3 and changes the affective valence of delay.
- `rival_models`: pure consolation without structural replay; possible, but weaker than the repeated subject-object-recipient structure.
- `grade`: medium-strong
- `grade_rationale`: strong morphosyntactic convergence across 93:3-5; lexical branch audit incomplete.
- `source_queries_or_rows_used`: attachment 93:3:a1-a4; 93:4:a1-a3; 93:5:a1-a5.

### S93-C003: Later-Better-Than-First Temporal Axis

- `candidate_id`: S93-C003
- `ayah_range`: 93:4-5
- `seed_type`: constructional
- `seed`: `وَلَلْءَاخِرَةُ خَيْرٌ لَّكَ مِنَ ٱلْأُولَىٰ`
- `generating_set`: predication row for `خَيْرٌ`; beneficiary `لَّكَ`; comparison `مِنَ ٱلْأُولَىٰ`; future assertion `لَسَوْفَ`.
- `selected_branches`: none available; `branch_dossier_unavailable`.
- `constructed_model`: an early/late axis is activated; the passage then refuses closure at the earlier state and pushes toward a later gift-result endpoint.
- `freeze_point`: after 93:5.
- `predictions_at_freeze`: prior states may be revisited as incomplete beginnings rather than final judgments; final commands may convert past reception into ongoing disclosure.
- `unused_features_tested`: 93:6-8 past sequence; 93:11 final command.
- `corroborators`: `(C: attachment 93:5 لسوف future assertion)`, `(C: attachment 93:5 فترضى result)`, `(C: sequence 93:6-8 past lacks are not endpoints because each has ف-consequent remedy)`.
- `constraints`: `(K: without furuq, cannot decide whether الآخرة is passage-world later state, eschatological later state, or both as branch-supported image)`.
- `temporal_reactivation_notes`: once 93:5 arrives, `الأولى` is retrospectively populated by the three remembered earlier states in 93:6-8.
- `rival_models`: strictly eschatological contrast; purely biographical contrast. Branch data needed to separate.
- `grade`: medium
- `grade_rationale`: high structural fit; semantic scope remains underdetermined without lexical dossiers.
- `source_queries_or_rows_used`: attachment 93:4:a1-a3; 93:5:a4-a5.

### S93-C004: Find-State-Remedy Triptych

- `candidate_id`: S93-C004
- `ayah_range`: 93:6-8
- `seed_type`: constructional / morphosyntactic
- `seed`: `يجدك/وجدك + state + ف + remedy`
- `generating_set`: 93:6 `أَلَمْ` complement `يَجِدْكَ`; 93:6 `يَتِيمًا` state/object complement; 93:6 `فَآوَىٰ`; 93:7 `وَجَدَكَ ضَالًّا فَهَدَىٰ`; 93:8 `وَجَدَكَ عَائِلًا فَأَغْنَىٰ`.
- `selected_branches`: none available; `branch_dossier_unavailable`.
- `constructed_model`: the addressee is repeatedly found in a deficit or exposure state, and each state is immediately followed by a `فـ` remedy. This creates a remembered-care proof that retroactively supports the denial of abandonment.
- `freeze_point`: after 93:8.
- `predictions_at_freeze`: later commands should correspond to the remembered deficit roles; prior `رَبُّكَ` should remain the implicit source of remedy.
- `unused_features_tested`: 93:9 orphan prohibition; 93:10 requester prohibition; 93:11 blessing narration; repeated `رَبّ`.
- `corroborators`: `(C: attachment 93:6 فآوى conjoined as consequent action)`, `(C: attachment 93:7 فهدى conjoined as consequent action)`, `(C: attachment 93:8 فأغنى conjoined as consequent action)`, `(C: repeated object suffix ك)`.
- `constraints`: `(K: 93:6-8 state words are structurally ambiguous between circumstantial and second object complements; image must preserve both possibilities)`, `(K: no branch images for يتم/ضلل/عيل/أوي/هدي/غني)`.
- `temporal_reactivation_notes`: after 93:9-11, the three remembered personal remedies become ethical templates for handling corresponding vulnerable roles.
- `rival_models`: simple autobiographical proof; three-part ethical preparation. They likely converge, but lexical data is needed for stronger synthesis.
- `grade`: medium-strong
- `grade_rationale`: robust repeated syntax and order-based role completion; branch evidence absent.
- `source_queries_or_rows_used`: attachment 93:6:a1-a5; 93:7:a1-a4; 93:8:a1-a4.

### S93-C005: Orphan Reactivation and Inhibition of Force

- `candidate_id`: S93-C005
- `ayah_range`: 93:6, 93:9
- `seed_type`: verified composite / temporal reactivation
- `seed`: recurrence of `يَتِيمًا` then `ٱلْيَتِيمَ`
- `generating_set`: 93:6 found-you orphan state plus consequent sheltering; 93:9 fronted orphan object plus prohibitive `لا تقهر`.
- `selected_branches`: none available; `branch_dossier_unavailable`.
- `constructed_model`: a role first occupied by the addressee becomes an external vulnerable object; the prior experience of being sheltered predicts inhibition of overpowering or crushing treatment.
- `freeze_point`: after 93:9.
- `predictions_at_freeze`: similar reactivation should occur for the next vulnerable role; final command should name the source of prior remedy.
- `unused_features_tested`: 93:10 requester/prohibition; 93:11 blessing of Lord.
- `corroborators`: `(C: attachment 93:9 اليتيم fronted direct object of تقهر)`, `(C: attachment 93:9 لا governs prohibitive jussive)`, `(C: sequence 93:6 before 93:9 creates backward replay)`.
- `constraints`: `(K: no branch for قهر; cannot determine the exact force image lexically)`.
- `temporal_reactivation_notes`: 93:9 forces replay of 93:6: the addressee’s earlier orphan state becomes the basis for conduct toward an orphan.
- `rival_models`: legal/ethical orphan rule independent of memory. It fits, but explains reactivation less fully.
- `grade`: strong structurally, medium overall
- `grade_rationale`: strongest passage-local reactivation; lexical branch incompleteness caps grade.
- `source_queries_or_rows_used`: attachment 93:6:a3-a5; 93:9:a1-a2.

### S93-C006: Requester and Non-Repulsion as Extension of Lack-Remedy Pattern

- `candidate_id`: S93-C006
- `ayah_range`: 93:8, 93:10
- `seed_type`: constructional / temporal
- `seed`: `عَائِلًا فَأَغْنَىٰ` followed by `ٱلسَّائِلَ فَلَا تَنْهَرْ`
- `generating_set`: 93:8 found-you in need/lack state plus enrichment; 93:10 fronted requester object plus prohibition.
- `selected_branches`: none available; `branch_dossier_unavailable`.
- `constructed_model`: the remembered lack/enrichment clause prepares the addressee not to repel a requester. The requester is not identical to `عائل`, but the role of lack seeking response is structurally parallel.
- `freeze_point`: after 93:10.
- `predictions_at_freeze`: final line should move from individual vulnerable objects to naming the source/blessing behind all remedies.
- `unused_features_tested`: 93:11 `بِنِعْمَةِ رَبِّكَ فَحَدِّثْ`.
- `corroborators`: `(C: attachment 93:10 السائل fronted direct object of تنهر)`, `(C: attachment 93:10 لا governs prohibitive jussive)`, `(C: attachment 93:8 فأغنى consequent action)`.
- `constraints`: `(K: no branch for سأل, نهر, عيل, غني; exact lexical link between poverty/request/repulsion cannot be audited)`.
- `temporal_reactivation_notes`: 93:10 reactivates 93:8 less exactly than 93:9 reactivates 93:6, but it continues the same deficit-to-remedy-to-ethical-response trajectory.
- `rival_models`: requester may correspond to guidance-seeking after `ضالًا فهدى` rather than material lack. Without branch data, both forks remain.
- `grade`: medium
- `grade_rationale`: structural parallel is clear; lexical specificity is unresolved.
- `source_queries_or_rows_used`: attachment 93:8:a2-a4; 93:10:a1-a2.

### S93-C007: Blessing Narration as Closure of Received-Care Sequence

- `candidate_id`: S93-C007
- `ayah_range`: 93:3-11
- `seed_type`: constructional / verified composite
- `seed`: recurring `رَبُّكَ` / `رَبِّكَ` plus final `بِنِعْمَةِ رَبِّكَ فَحَدِّثْ`
- `generating_set`: 93:3 `رَبُّكَ` subject of denied farewell; 93:5 `رَبُّكَ` subject of future giving; 93:11 `نِعْمَةِ رَبِّكَ` complement of final command.
- `selected_branches`: none available; `branch_dossier_unavailable`.
- `constructed_model`: the passage closes by transforming divine-source care into narration. The source denied as abandoner and promised as giver becomes the possessor of the blessing to be spoken of.
- `freeze_point`: after 93:11.
- `predictions_at_freeze`: no later passage features remain; closure should account for why the final command is not another prohibition but a positive disclosure.
- `unused_features_tested`: none after closure; retrospective test against 93:6-8 and 93:9-10.
- `corroborators`: `(C: attachment 93:11 نعمة governed by بـ as complement of حدث)`, `(C: attachment 93:11 ربك genitive possessor in نعمة ربك)`, `(C: repeated ربك at 93:3, 93:5, 93:11)`.
- `constraints`: `(K: no branch for نعم or حدث; cannot test whether نعمة carries a specific tactile/prosperity/benefaction image)`.
- `temporal_reactivation_notes`: final `رَبِّكَ` reactivates both the denied abandonment and future giving; `نِعْمَة` gathers the remembered remedies into speakable evidence.
- `rival_models`: proclamation of revelation rather than personal benefaction; both may be live without branch data.
- `grade`: medium-strong
- `grade_rationale`: strong closure and recurrence; lexical branch details absent.
- `source_queries_or_rows_used`: attachment 93:3:a2-a3; 93:5:a2-a3; 93:11:a1-a3.

### S93-C008: Three Imperatives as Ethical Conversion of Three Memories

- `candidate_id`: S93-C008
- `ayah_range`: 93:6-11
- `seed_type`: constructional / temporal
- `seed`: 93:6-8 memory triad followed by 93:9-11 imperative triad
- `generating_set`: three found-state/remedy clauses; three `فأما/وأما` command clauses; prohibitions for orphan/requester; positive command concerning blessing.
- `selected_branches`: none available; `branch_dossier_unavailable`.
- `constructed_model`: received care is converted into conduct. The addressee was found vulnerable and remedied; then vulnerable others are placed first in the clause and protected from harm, while the received blessing is made the object/medium of speech.
- `freeze_point`: after 93:11.
- `predictions_at_freeze`: full closure should preserve both negative restraint and positive communication.
- `unused_features_tested`: none after closure.
- `corroborators`: `(C: attachment 93:9 fronted object اليتيم)`, `(C: attachment 93:10 fronted object السائل)`, `(C: attachment 93:11 بنعمة prep complement of حدث)`, `(C: sequence memory triad precedes imperative triad)`.
- `constraints`: `(K: exact one-to-one mapping for ضالًا فهدى to السائل or حدث is underdetermined without branch dossiers)`.
- `temporal_reactivation_notes`: 93:9 directly replays 93:6; 93:10 partially replays lack/remedy; 93:11 globally replays the source of all remedies.
- `rival_models`: two negative social duties plus one praise command without triadic mapping. This is viable but less order-sensitive.
- `grade`: medium-strong
- `grade_rationale`: strong formal and temporal architecture; lexical mapping remains incomplete.
- `source_queries_or_rows_used`: attachment 93:6:a1-a5; 93:7:a1-a4; 93:8:a1-a4; 93:9:a1-a2; 93:10:a1-a2; 93:11:a1-a3.

### S93-C009: Repeated Addressee Object as Stable Recipient Through Time

- `candidate_id`: S93-C009
- `ayah_range`: 93:3-8
- `seed_type`: morphosyntactic
- `seed`: repeated suffix `كَ` as direct object/possessor
- `generating_set`: 93:3 `وَدَّعَكَ`; 93:3 `رَبُّكَ`; 93:5 `يُعْطِيكَ`; 93:5 `رَبُّكَ`; 93:6 `يَجِدْكَ`; 93:7 `وَجَدَكَ`; 93:8 `وَجَدَكَ`.
- `selected_branches`: non-lexical seed.
- `constructed_model`: the same addressed person is held constant across denied rupture, promised gift, and remembered remedies. This creates continuity of recipient identity through changing temporal scenes.
- `freeze_point`: after 93:8.
- `predictions_at_freeze`: final imperatives should address the same recipient as one who has been stabilized by prior care.
- `unused_features_tested`: 93:9-11 imperative sequence; final `رَبِّكَ`.
- `corroborators`: `(C: attachment direct-object rows 93:3, 93:5, 93:6, 93:7, 93:8)`, `(C: possessive suffix rows on ربك 93:3, 93:5, 93:11)`.
- `constraints`: `(K: suffix recurrence is structural, not lexical branch evidence)`.
- `temporal_reactivation_notes`: every new event is bound to the same addressee, so later commands can be heard as consequences of personally remembered care.
- `rival_models`: generic second-person address only. The recurrence density and attachment roles support a stronger continuity model.
- `grade`: medium
- `grade_rationale`: reliable morphology/attachment evidence, but not a lexical image.
- `source_queries_or_rows_used`: attachment 93:3:a1,a3; 93:5:a1,a3; 93:6:a2; 93:7:a1; 93:8:a1; 93:11:a3.

## Failed Branch-Required Seeds

These seeds must be restarted if `resources/qac.sqlite` and `resources/furuq_v4.sqlite` become available. They cannot be completed from the authorized resources presently available:

- Every accepted branch of `ٱلضُّحَىٰ`.
- Every accepted branch of `ٱلَّيْلِ`.
- Every accepted branch of `سَجَىٰ`.
- Every accepted branch of `وَدَّعَ`.
- Every accepted branch of `ر ب ب`.
- Every accepted branch of `قَلَىٰ`.
- Every accepted branch of `أ خ ر`.
- Every accepted branch of `خ ي ر`.
- Every accepted branch of `و ل ي`.
- Every accepted branch of `ع ط و`.
- Every accepted branch of `ر ض ي`.
- Every accepted branch of `ج د د / وجد` as resolved by QAC.
- Every accepted branch of `ي ت م`.
- Every accepted branch of `أ و ي`.
- Every accepted branch of `ض ل ل`.
- Every accepted branch of `ه د ي`.
- Every accepted branch of `ع ي ل`.
- Every accepted branch of `غ ن ي`.
- Every accepted branch of `ق ه ر`.
- Every accepted branch of `س أ ل`.
- Every accepted branch of `ن ه ر`.
- Every accepted branch of `ن ع م`.
- Every accepted branch of `ح د ث`.

## Image Packet Catalog

IMAGE_ID: S93-IMG-001  
Starting seed: oath pair, 93:1-2  
Complete image: bright exposure followed by settled night, then denial that darkness equals abandonment  
Passage-order assembly: 93:1 light; 93:2 night settling; 93:3 no farewell/no aversion; 93:5 future giving  
Participants and roles: addressee; `رَبّ`; dark interval; future gift  
Operation / mechanism: temporal reinterpretation by denial and promise  
Direction / force / medium: from apparent absence to affirmed care  
Temporal development: daybreak -> night settling -> denied abandonment -> future satisfaction  
Outcome / closure: contributes to final narration of blessing  
Exact branch constituents: none available; structural rows only  
Unfilled roles: lexical force of `ضحى`, `ليل`, `سجى`, `ودع`, `قلى`  
Status: FRAGMENT

IMAGE_ID: S93-IMG-002  
Starting seed: find-state-remedy triad, 93:6-8  
Complete image: the addressee is found in exposed states and each state receives a corresponding remedy  
Passage-order assembly: orphan -> shelter; astray/lost -> guidance; needy -> enrichment  
Participants and roles: addressee as found object; deficient state; remedy action; implied divine care source  
Operation / mechanism: discovered vulnerability followed by immediate restorative action  
Direction / force / medium: from exposure/lack to care/sufficiency/orientation  
Temporal development: remembered past supplies proof for present reassurance and later conduct  
Outcome / closure: produces the ethical conversion in 93:9-11  
Exact branch constituents: none available; attachment rows for consequent `فـ` actions  
Unfilled roles: branch-specific lexical images for every state and remedy verb  
Status: COMPLETE structurally, FRAGMENT lexically

IMAGE_ID: S93-IMG-003  
Starting seed: orphan recurrence, 93:6 and 93:9  
Complete image: a personally remembered orphan-state is reactivated as a protected external object  
Passage-order assembly: you as orphan -> sheltered; the orphan -> do not overpower  
Participants and roles: prior addressee; later orphan; prohibited aggressor role; sheltering memory  
Operation / mechanism: backward replay turns received care into restraint toward another  
Direction / force / medium: from being vulnerable to refusing force against vulnerability  
Temporal development: 93:6 memory returns at 93:9  
Outcome / closure: first ethical command is grounded in prior care  
Exact branch constituents: none available; attachment rows for fronted object and prohibition  
Unfilled roles: lexical image of `قهر`  
Status: COMPLETE structurally, FRAGMENT lexically

IMAGE_ID: S93-IMG-004  
Starting seed: final `بِنِعْمَةِ رَبِّكَ فَحَدِّثْ`  
Complete image: the whole received-care history is gathered as the Lord's blessing and made speakable  
Passage-order assembly: no abandonment -> later better -> future giving -> past remedies -> protect vulnerable -> narrate blessing  
Participants and roles: `رَبّ` as source/possessor; addressee as recipient-speaker; blessing as content/medium  
Operation / mechanism: care becomes testimony or narration  
Direction / force / medium: from received benefit to outward speech  
Temporal development: final command reactivates all previous divine-source clauses  
Outcome / closure: closes on positive declaration rather than mere prohibition  
Exact branch constituents: none available; attachment rows for `بـ` complement and idafa  
Unfilled roles: lexical images of `نعم` and `حدث`  
Status: COMPLETE structurally, FRAGMENT lexically

## Exhaustiveness Check

Exhaustive lexical branch work was not possible because the prompt-authorized QAC and furuq SQLite databases are unavailable. Within that constraint, the Pass 2 restart covered:

- every rooted occurrence visible in the sacred text and/or S93 attachment rows;
- every construction licensed by the S93 attachment rows;
- every repeated morphosyntactic pattern with passage-scale reactivation value;
- failed lexical seeds explicitly, rather than omitting them.

Potentially missing images are exactly those that require `branch_image_ar` and `what_is_ar` from `resources/furuq_v4.sqlite`. The file should be revised if the authorized SQLite resources are restored.
