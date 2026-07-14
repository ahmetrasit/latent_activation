# Stage 1 Pass 2 - S114

Assigned passage: S114  
Sacred Arabic text source: `resources/quran/surah_114.json`

## Root Cause of Pass 1 Limitation

Pass 1 was limited because the two required SQLite lexical resources are empty in this workspace:

- `resources/qac.sqlite` is 0 bytes.
- `resources/furuq_v4.sqlite` is 0 bytes.

Therefore the required QAC word/morpheme tables and uncontaminated furuq `branch_images` table could not be queried. This prevents retrieval of accepted lexical branches, `branch_id`, `branch_image_ar`, and `what_is_ar` for every S114 root. The limitation was not a decision to visit only promising words. It was a source availability failure.

This Pass 2 restarts from the first rooted word and performs the exhaustive sweep possible under the Stage 1 resource boundary. It uses only:

- sacred Arabic text from `resources/quran/surah_114.json`;
- S114 rows from `resources/attachments.tsv`;
- the observed fact that QAC and furuq SQLite branch resources are empty/unavailable.

Basmala is opening recitational context only and is not used as a seed.

## Passage Text

Opening context:

- 114:0 `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`

Assigned ayat:

- 114:1 `قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ`
- 114:2 `مَلِكِ ٱلنَّاسِ`
- 114:3 `إِلَٰهِ ٱلنَّاسِ`
- 114:4 `مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ`
- 114:5 `ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ`
- 114:6 `مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ`

## Allowed Structural Rows Used

Attachment rows used:

- 114:1 a1: `أَعُوذُ` is the quoted complement governed by `قُلْ`.
- 114:1 a2: `بِرَبِّ` is the prepositional complement of `أَعُوذُ`.
- 114:1 a3: `ٱلنَّاسِ` completes construct `رَبِّ`.
- 114:2 a1: `ٱلنَّاسِ` completes construct `مَلِكِ`.
- 114:3 a1: `ٱلنَّاسِ` completes construct `إِلَٰهِ`.
- 114:4 a1: `ٱلْوَسْوَاسِ` completes construct `شَرِّ`.
- 114:4 a2: `ٱلْخَنَّاسِ` is a definite genitive descriptive epithet of `ٱلْوَسْوَاسِ`.
- 114:5 a1: `صُدُورِ` is governed by `فِى` as locative complement of `يُوَسْوِسُ`.
- 114:5 a2: `ٱلنَّاسِ` completes construct `صُدُورِ`.
- 114:6 a1: `وَٱلنَّاسِ` is coordinated with `ٱلْجِنَّةِ` as the second genitive member after `مِنَ`.

## Rooted Occurrence Inventory

The following rooted occurrences are recoverable from the sacred text plus attachment rows. Lexical branch IDs are unavailable because `furuq_v4.sqlite` is empty.

1. 114:1:1 `قُلْ`, root recorded in attachment row as `ق ل ل`
2. 114:1:2 `أَعُوذُ`, root `ع و ذ`
3. 114:1:3 `رَبِّ`, root `ر ب ب`
4. 114:1:4 `ٱلنَّاسِ`, root `أ ن س`
5. 114:2:1 `مَلِكِ`, root `م ل ك`
6. 114:2:2 `ٱلنَّاسِ`, root `أ ن س`
7. 114:3:1 `إِلَٰهِ`, root `أ ل ه`
8. 114:3:2 `ٱلنَّاسِ`, root `أ ن س`
9. 114:4:2 `شَرِّ`, root recorded in attachment row as `ش ر ي`
10. 114:4:3 `ٱلْوَسْوَاسِ`, root `و س و س`
11. 114:4:4 `ٱلْخَنَّاسِ`, root `خ ن س`
12. 114:5:2 `يُوَسْوِسُ`, root `و س و س`
13. 114:5:4 `صُدُورِ`, root `ص د ر`
14. 114:5:5 `ٱلنَّاسِ`, root `أ ن س`
15. 114:6:2 `ٱلْجِنَّةِ`, root `ج ن ن`
16. 114:6:4 `وَٱلنَّاسِ`, root `أ ن س`

## Lexical Seed Passes

Because no uncontaminated furuq branches are available, every lexical seed below is marked as a failed lexical branch pass. The pass is still listed to preserve the exhaustive audit trail. Constructional and morphosyntactic seeds follow after the lexical inventory.

### S114-P2-L01 - `قُلْ` at 114:1:1

- seed_type: lexical
- seed: 114:1:1 `قُلْ`, root recorded as `ق ل ل`; no furuq branch ID available
- generating_set: none; branch dossier unavailable
- selected_branches: none
- constructed_model: no lexical branch image can be formed from the permitted lexical source
- freeze_point: immediately after failed branch lookup
- predictions_at_freeze: none
- unused_features_tested: attachment a1 shows quoted complement governed by `قُلْ`
- corroborators: `(C: attachment 114:1 a1 quoted_complement)` supports a speech-command frame structurally, not lexically
- constraints: `(K: furuq_v4.sqlite empty; no branch_image_ar/what_is_ar)`; root in attachment row appears as `ق ل ل`, so no independent QAC verification is possible
- temporal_reactivation_notes: the command opens an audition frame in which the following words are to be recited as protected speech
- rival_models: none
- grade: unlikely
- grade_rationale: lexical synthesis cannot be initiated without an accepted branch; the constructional command frame is handled separately
- source_queries_or_rows_used: sacred text; attachment 114:1 a1

### S114-P2-L02 - `أَعُوذُ` at 114:1:2

- seed_type: lexical
- seed: 114:1:2 `أَعُوذُ`, root `ع و ذ`; no furuq branch ID available
- generating_set: none; branch dossier unavailable
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediately after failed branch lookup
- predictions_at_freeze: none
- unused_features_tested: `بِرَبِّ` as prepositional complement; preceding `قُلْ`
- corroborators: `(C: attachment 114:1 a2 prep_complement)` supports a refuge-taking relation structurally
- constraints: `(K: furuq_v4.sqlite empty)`
- temporal_reactivation_notes: the word becomes the first content of the commanded utterance and governs the divine-role chain that follows
- rival_models: none
- grade: unlikely
- grade_rationale: structural role is strong, but lexical branch synthesis is unavailable
- source_queries_or_rows_used: sacred text; attachments 114:1 a1-a2

### S114-P2-L03 - `رَبِّ` at 114:1:3

- seed_type: lexical
- seed: 114:1:3 `رَبِّ`, root `ر ب ب`; no furuq branch ID available
- generating_set: none
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediate failed lexical lookup
- predictions_at_freeze: none
- unused_features_tested: `ٱلنَّاسِ` as genitive complement; later parallel `مَلِكِ ٱلنَّاسِ`, `إِلَٰهِ ٱلنَّاسِ`
- corroborators: `(C: attachment 114:1 a3 idafa)`; `(C: sequence 114:1->114:3 repeated divine-role idafa)`
- constraints: `(K: furuq_v4.sqlite empty)`
- temporal_reactivation_notes: first divine relation to `ٱلنَّاسِ`; later titles reactivate and thicken it
- rival_models: none
- grade: unlikely
- grade_rationale: no branch image; the viable material belongs to the constructional triple-title seed
- source_queries_or_rows_used: sacred text; attachment 114:1 a3

### S114-P2-L04 - `ٱلنَّاسِ` at 114:1:4

- seed_type: lexical
- seed: 114:1:4 `ٱلنَّاسِ`, root `أ ن س`; no furuq branch ID available
- generating_set: none
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediate failed lexical lookup
- predictions_at_freeze: none
- unused_features_tested: recurrence of `ٱلنَّاسِ` at 114:2, 114:3, 114:5, 114:6
- corroborators: `(C: repetition of الناس across 114:1-3, 5-6)` structurally marks the protected class and later endangered/intermixed class
- constraints: `(K: furuq_v4.sqlite empty)`
- temporal_reactivation_notes: first endpoint of refuge relation; later repeated endpoints shift from governed people to vulnerable interiors and finally to one source class
- rival_models: none
- grade: unlikely
- grade_rationale: branchless lexical seed; repetition handled in temporal seed
- source_queries_or_rows_used: sacred text; attachments 114:1 a3, 114:2 a1, 114:3 a1, 114:5 a2, 114:6 a1

### S114-P2-L05 - `مَلِكِ` at 114:2:1

- seed_type: lexical
- seed: 114:2:1 `مَلِكِ`, root `م ل ك`; no furuq branch ID available
- generating_set: none
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediate failed lexical lookup
- predictions_at_freeze: none
- unused_features_tested: idafa with `ٱلنَّاسِ`; placement between `رَبِّ` and `إِلَٰهِ`
- corroborators: `(C: attachment 114:2 a1 idafa)`; `(C: sequence middle member of triple title)`
- constraints: `(K: furuq_v4.sqlite empty)`
- temporal_reactivation_notes: the second title reactivates `ٱلنَّاسِ` and adds a governance/possession role structurally inside the address
- rival_models: none
- grade: unlikely
- grade_rationale: no lexical branch dossier; only structural role recoverable
- source_queries_or_rows_used: sacred text; attachment 114:2 a1

### S114-P2-L06 - `ٱلنَّاسِ` at 114:2:2

- seed_type: lexical
- seed: 114:2:2 `ٱلنَّاسِ`, root `أ ن س`; no furuq branch ID available
- generating_set: none
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediate failed lexical lookup
- predictions_at_freeze: none
- unused_features_tested: repeated genitive complement after `مَلِكِ`; earlier/later `ٱلنَّاسِ`
- corroborators: `(C: attachment 114:2 a1 idafa)`; `(C: repetition)`
- constraints: `(K: furuq_v4.sqlite empty)`
- temporal_reactivation_notes: repetition keeps the same referent active while the divine role changes
- rival_models: none
- grade: unlikely
- grade_rationale: branchless seed, no lexical image
- source_queries_or_rows_used: sacred text; attachment 114:2 a1

### S114-P2-L07 - `إِلَٰهِ` at 114:3:1

- seed_type: lexical
- seed: 114:3:1 `إِلَٰهِ`, root `أ ل ه`; no furuq branch ID available
- generating_set: none
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediate failed lexical lookup
- predictions_at_freeze: none
- unused_features_tested: idafa with `ٱلنَّاسِ`; closure of three-title ascent before threat appears
- corroborators: `(C: attachment 114:3 a1 idafa)`; `(C: ayah boundary after 114:3)`
- constraints: `(K: furuq_v4.sqlite empty)`
- temporal_reactivation_notes: third divine relation completes the address field before the first `مِن شَرِّ`
- rival_models: none
- grade: unlikely
- grade_rationale: no branch data; the constructional role is treated under the triple-title seed
- source_queries_or_rows_used: sacred text; attachment 114:3 a1

### S114-P2-L08 - `ٱلنَّاسِ` at 114:3:2

- seed_type: lexical
- seed: 114:3:2 `ٱلنَّاسِ`, root `أ ن س`; no furuq branch ID available
- generating_set: none
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediate failed lexical lookup
- predictions_at_freeze: none
- unused_features_tested: completes third idafa; later threat phrase
- corroborators: `(C: attachment 114:3 a1 idafa)`; `(C: transition 114:3->114:4 from addressed protector to danger)`
- constraints: `(K: furuq_v4.sqlite empty)`
- temporal_reactivation_notes: the third recurrence prepares for contrast when `ٱلنَّاسِ` later becomes the interior locus of whispering
- rival_models: none
- grade: unlikely
- grade_rationale: branch unavailable; temporal recurrence remains structurally useful
- source_queries_or_rows_used: sacred text; attachment 114:3 a1

### S114-P2-L09 - `شَرِّ` at 114:4:2

- seed_type: lexical
- seed: 114:4:2 `شَرِّ`, root recorded as `ش ر ي`; no furuq branch ID available
- generating_set: none
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediate failed lexical lookup
- predictions_at_freeze: none
- unused_features_tested: idafa with `ٱلْوَسْوَاسِ`; `مِن` boundary before it
- corroborators: `(C: attachment 114:4 a1 idafa)`; `(C: min phrase opens object of refuge)`
- constraints: `(K: furuq_v4.sqlite empty)`; `(K: attachment root recorded as ش ر ي, no QAC table available to verify root)`
- temporal_reactivation_notes: first explicit threat word arrives only after three protective roles
- rival_models: none
- grade: unlikely
- grade_rationale: no branch image; threat construction handled separately
- source_queries_or_rows_used: sacred text; attachment 114:4 a1

### S114-P2-L10 - `ٱلْوَسْوَاسِ` at 114:4:3

- seed_type: lexical
- seed: 114:4:3 `ٱلْوَسْوَاسِ`, root `و س و س`; no furuq branch ID available
- generating_set: none
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediate failed lexical lookup
- predictions_at_freeze: none
- unused_features_tested: genitive complement of `شَرِّ`; epithet `ٱلْخَنَّاسِ`; verbal recurrence `يُوَسْوِسُ`
- corroborators: `(C: attachment 114:4 a1 idafa)`; `(C: attachment 114:4 a2 epithet)`; `(C: repetition noun->verb 114:4->114:5)`
- constraints: `(K: furuq_v4.sqlite empty)`
- temporal_reactivation_notes: nominal label appears before operational verb, so the threat is named before its mechanism is disclosed
- rival_models: none
- grade: unlikely
- grade_rationale: branch unavailable; the noun-verb recurrence is handled as temporal/acoustic seed
- source_queries_or_rows_used: sacred text; attachments 114:4 a1-a2, 114:5 a1

### S114-P2-L11 - `ٱلْخَنَّاسِ` at 114:4:4

- seed_type: lexical
- seed: 114:4:4 `ٱلْخَنَّاسِ`, root `خ ن س`; no furuq branch ID available
- generating_set: none
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediate failed lexical lookup
- predictions_at_freeze: none
- unused_features_tested: definite genitive epithet attached to `ٱلْوَسْوَاسِ`
- corroborators: `(C: attachment 114:4 a2 adjective)` structurally binds the epithet to the whisperer
- constraints: `(K: furuq_v4.sqlite empty)`
- temporal_reactivation_notes: the epithet narrows the threat before the relative clause specifies action and location
- rival_models: none
- grade: unlikely
- grade_rationale: no accepted branch available; cannot construct the lexical image of the epithet
- source_queries_or_rows_used: sacred text; attachment 114:4 a2

### S114-P2-L12 - `يُوَسْوِسُ` at 114:5:2

- seed_type: lexical
- seed: 114:5:2 `يُوَسْوِسُ`, root `و س و س`; no furuq branch ID available
- generating_set: none
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediate failed lexical lookup
- predictions_at_freeze: none
- unused_features_tested: governed locative `فِى صُدُورِ`; antecedent `ٱلْوَسْوَاسِ ٱلْخَنَّاسِ`
- corroborators: `(C: attachment 114:5 a1 locative complement)`; `(C: repetition root/form relation with 114:4:3)`
- constraints: `(K: furuq_v4.sqlite empty)`
- temporal_reactivation_notes: the earlier noun is reactivated as an event/process inside `صُدُورِ ٱلنَّاسِ`
- rival_models: none
- grade: unlikely
- grade_rationale: no lexical branch; constructional mechanism handled separately
- source_queries_or_rows_used: sacred text; attachment 114:5 a1

### S114-P2-L13 - `صُدُورِ` at 114:5:4

- seed_type: lexical
- seed: 114:5:4 `صُدُورِ`, root `ص د ر`; no furuq branch ID available
- generating_set: none
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediate failed lexical lookup
- predictions_at_freeze: none
- unused_features_tested: governed by `فِى`; idafa with `ٱلنَّاسِ`
- corroborators: `(C: attachment 114:5 a1 prep_complement)`; `(C: attachment 114:5 a2 idafa)`
- constraints: `(K: furuq_v4.sqlite empty)`
- temporal_reactivation_notes: creates the inner vulnerable locus after the threat has been named
- rival_models: none
- grade: unlikely
- grade_rationale: no branch image; locative construction is strong and handled separately
- source_queries_or_rows_used: sacred text; attachments 114:5 a1-a2

### S114-P2-L14 - `ٱلنَّاسِ` at 114:5:5

- seed_type: lexical
- seed: 114:5:5 `ٱلنَّاسِ`, root `أ ن س`; no furuq branch ID available
- generating_set: none
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediate failed lexical lookup
- predictions_at_freeze: none
- unused_features_tested: genitive complement of `صُدُورِ`; earlier triple-title recipients
- corroborators: `(C: attachment 114:5 a2 idafa)`; `(C: temporal reactivation of الناس from 114:1-3)`
- constraints: `(K: furuq_v4.sqlite empty)`
- temporal_reactivation_notes: `ٱلنَّاسِ` shifts from protected possessive relation to the humans whose interiors are targeted
- rival_models: none
- grade: unlikely
- grade_rationale: no lexical branch; important temporal role but branchless
- source_queries_or_rows_used: sacred text; attachment 114:5 a2

### S114-P2-L15 - `ٱلْجِنَّةِ` at 114:6:2

- seed_type: lexical
- seed: 114:6:2 `ٱلْجِنَّةِ`, root `ج ن ن`; no furuq branch ID available
- generating_set: none
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediate failed lexical lookup
- predictions_at_freeze: none
- unused_features_tested: governed by final `مِنَ`; coordinated with `وَٱلنَّاسِ`
- corroborators: `(C: attachment 114:6 a1 coordination)`; `(C: final source classification after inner operation)`
- constraints: `(K: furuq_v4.sqlite empty)`
- temporal_reactivation_notes: source disclosure is delayed until after the mechanism and locus are heard
- rival_models: none
- grade: unlikely
- grade_rationale: no branch dossier; source-pair construction handled separately
- source_queries_or_rows_used: sacred text; attachment 114:6 a1

### S114-P2-L16 - `وَٱلنَّاسِ` at 114:6:4

- seed_type: lexical
- seed: 114:6:4 `وَٱلنَّاسِ`, root `أ ن س`; no furuq branch ID available
- generating_set: none
- selected_branches: none
- constructed_model: no lexical branch image can be formed
- freeze_point: immediate failed lexical lookup
- predictions_at_freeze: none
- unused_features_tested: coordination with `ٱلْجِنَّةِ`; recurrence from protected people and vulnerable chests
- corroborators: `(C: attachment 114:6 a1 coordination)`; `(C: closure repeats الناس)`
- constraints: `(K: furuq_v4.sqlite empty)`
- temporal_reactivation_notes: final `ٱلنَّاسِ` closes the passage by making the protected class also part of the source-class pair
- rival_models: none
- grade: unlikely
- grade_rationale: no branch image; closure role is structural and temporal
- source_queries_or_rows_used: sacred text; attachment 114:6 a1

## Constructional, Morphosyntactic, and Temporal Seed Passes

### S114-P2-C01 - Commanded Refuge Utterance

- seed_type: constructional
- seed: `قُلْ` governing the quoted content `أَعُوذُ بِرَبِّ ٱلنَّاسِ`
- generating_set: `(E: attachment 114:1 a1 quoted_complement)` + `(E: attachment 114:1 a2 prep_complement)`
- selected_branches: none; branch dossiers unavailable
- constructed_model: A commanded speaker is made to voice refuge-taking. The passage begins not with direct description of danger but with an instructed utterance, so the reciter enters a protected speech act before the threat appears.
- freeze_point: after 114:1 command-plus-refuge relation is formed
- predictions_at_freeze: expected object/source of refuge; expected reason for refuge; expected specification of the protecting relation
- unused_features_tested: triple divine titles 114:1-3; `مِن شَرِّ` 114:4; threat mechanism 114:5; source classes 114:6
- corroborators: `(C: sequence 114:1-3 supplies protecting relation before threat)`; `(C: 114:4 مِن شَرِّ supplies reason for refuge)`; `(C: 114:5 supplies hidden operation and inner locus)`
- constraints: `(K: no lexical branch dossier for قُل/عوذ/رب)`; `(K: construction does not itself identify a lexical image beyond commanded refuge)`
- temporal_reactivation_notes: after the threat is named in 114:4, the initial `أَعُوذُ` becomes newly necessary; the command was not merely introductory but the response-form required by the later danger
- rival_models: a generic speech-opening model is weaker because the later `مِن شَرِّ` specifically completes the refuge expectation
- grade: medium-strong
- grade_rationale: strong structural and temporal fit, independent of unavailable lexical branches; specificity is limited by lack of branch dossiers
- source_queries_or_rows_used: sacred text; attachments 114:1 a1-a2, 114:4 a1, 114:5 a1

### S114-P2-C02 - Threefold Divine Role over `ٱلنَّاسِ`

- seed_type: constructional
- seed: `رَبِّ ٱلنَّاسِ / مَلِكِ ٱلنَّاسِ / إِلَٰهِ ٱلنَّاسِ`
- generating_set: `(E: attachment 114:1 a3 idafa)` + `(E: attachment 114:2 a1 idafa)` + `(E: attachment 114:3 a1 idafa)` + `(E: repetition الناس)`
- selected_branches: none
- constructed_model: The same human object is placed under three successive relations before the danger is named. The model is a layered protective address: the repeated genitive complement keeps `ٱلنَّاسِ` stable while the governing title changes at each ayah boundary.
- freeze_point: after 114:3, before `مِن شَرِّ`
- predictions_at_freeze: expected later threat to this same class; expected need for protection to operate over humans as a whole; expected reactivation of `ٱلنَّاسِ`
- unused_features_tested: 114:5 `صُدُورِ ٱلنَّاسِ`; 114:6 `وَٱلنَّاسِ`; 114:4-5 threat and whispering
- corroborators: `(C: 114:5 الناس reappears as possessors of the inner locus)`; `(C: 114:6 الناس reappears in final source pair)`; `(C: sequence threat appears only after protective address is complete)`
- constraints: `(K: branch dossiers for رب/ملك/إله/ناس unavailable)`; `(K: the construction supports layered address, not a lexical claim about each title's branch image)`
- temporal_reactivation_notes: `ٱلنَّاسِ` is first stabilized by repetition; later the same word is reactivated in a vulnerable interior relation and then in a source classification
- rival_models: a mere list of epithets underexplains the recurrence of the same genitive complement and later re-entry of `ٱلنَّاسِ`
- grade: strong
- grade_rationale: the repeated idafa structure, sequence, and later reactivations are highly specific and passage-local
- source_queries_or_rows_used: sacred text; attachments 114:1 a3, 114:2 a1, 114:3 a1, 114:5 a2, 114:6 a1

### S114-P2-C03 - Threat as Genitive Source: `مِن شَرِّ ٱلْوَسْوَاسِ`

- seed_type: constructional
- seed: `مِن شَرِّ ٱلْوَسْوَاسِ`
- generating_set: `(E: 114:4 مِن boundary/source phrase)` + `(E: attachment 114:4 a1 idafa)`
- selected_branches: none
- constructed_model: The refuge request receives its first explicit object: separation/protection from the evil belonging to or proceeding through the named whisperer. The threat is introduced as a genitive relation rather than as a visible assault.
- freeze_point: after `مِن شَرِّ ٱلْوَسْوَاسِ`, before `ٱلْخَنَّاسِ` and the relative clause are used
- predictions_at_freeze: expected specification of the whisperer; expected operation matching the name; expected locus or target
- unused_features_tested: `ٱلْخَنَّاسِ`; `ٱلَّذِى يُوَسْوِسُ`; `فِى صُدُورِ ٱلنَّاسِ`; `مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ`
- corroborators: `(C: attachment 114:4 a2 epithet narrows the whisperer)`; `(C: noun-to-verb recurrence 114:4->114:5 supplies operation)`; `(C: attachment 114:5 a1 supplies interior locus)`; `(C: 114:6 supplies source classes)`
- constraints: `(K: no lexical branches for شر or وسوس)`; `(K: idafa marks relation to the whisperer, not a free-floating generic evil)`
- temporal_reactivation_notes: the earlier `أَعُوذُ` is reactivated when `مِن شَرِّ` appears; the named whisperer is reactivated as a verb in the next ayah
- rival_models: a broad evil-only model is weaker because the passage immediately narrows the evil through a named agent, epithet, action, locus, and source pair
- grade: medium-strong
- grade_rationale: high structural specificity and successful predictions; lexical branch support absent
- source_queries_or_rows_used: sacred text; attachments 114:4 a1-a2, 114:5 a1, 114:6 a1

### S114-P2-C04 - Epithet Narrowing: `ٱلْوَسْوَاسِ ٱلْخَنَّاسِ`

- seed_type: morphosyntactic
- seed: definite genitive noun plus definite epithet
- generating_set: `(E: attachment 114:4 a2 adjective)`
- selected_branches: none
- constructed_model: The threat is not merely named; it is immediately narrowed by an agreeing epithet. The model is a hidden/receding whisper-source whose identity is compressed into a title before its process is unfolded.
- freeze_point: after 114:4, before 114:5 relative clause
- predictions_at_freeze: expected a clause explaining the epithet/title; expected hidden or hard-to-localize operation; expected internal target
- unused_features_tested: 114:5 `ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ`; 114:6 source pair
- corroborators: `(C: 114:5 relative clause explains the title by action)`; `(C: attachment 114:5 a1 locative complement supplies hidden inner locus)`; `(C: 114:6 delayed source pair leaves the source non-obvious until closure)`
- constraints: `(K: no خنس or وسوس lexical branches; cannot assert the lexical content of خناس beyond its structural epithet role)`
- temporal_reactivation_notes: the epithet creates an unresolved descriptor; the next ayah resolves by specifying what the entity does and where
- rival_models: if treated as a decorative epithet only, it underpredicts the explanatory relative clause that follows
- grade: medium
- grade_rationale: structurally real and temporally predictive, but lexical content cannot be verified from furuq
- source_queries_or_rows_used: sacred text; attachments 114:4 a2, 114:5 a1, 114:6 a1

### S114-P2-C05 - Relative Clause Mechanism: `ٱلَّذِى يُوَسْوِسُ`

- seed_type: constructional
- seed: `ٱلَّذِى يُوَسْوِسُ` as relative clause attached to the named threat
- generating_set: `(E: relative clause sequence 114:5)` + `(E: repetition وسواس/يوسوس)`
- selected_branches: none
- constructed_model: The named entity is converted into an operation. The noun `ٱلْوَسْوَاسِ` is reactivated as the verb `يُوَسْوِسُ`, turning label into process.
- freeze_point: after `ٱلَّذِى يُوَسْوِسُ`, before locative phrase
- predictions_at_freeze: expected a target or medium for the operation; expected internality because the operation is not externally visible in the preceding syntax
- unused_features_tested: `فِى صُدُورِ ٱلنَّاسِ`; final `مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ`
- corroborators: `(C: attachment 114:5 a1 locative complement supplies target/locus)`; `(C: attachment 114:5 a2 identifies possessors of locus as الناس)`; `(C: 114:6 gives source classes only after operation is specified)`
- constraints: `(K: no وسوس branch dossier; recurrence can be structural/acoustic only)`
- temporal_reactivation_notes: 114:5 reactivates 114:4's title and discloses its mechanism after a one-ayah delay
- rival_models: a static-threat model fails because the passage itself shifts from noun to imperfect verb
- grade: medium-strong
- grade_rationale: precise recurrence and role completion; limited by unavailable branch semantics
- source_queries_or_rows_used: sacred text; attachments 114:4 a1-a2, 114:5 a1-a2

### S114-P2-C06 - Inner Locus: `فِى صُدُورِ ٱلنَّاسِ`

- seed_type: constructional
- seed: `فِى صُدُورِ ٱلنَّاسِ`
- generating_set: `(E: attachment 114:5 a1 prep_complement)` + `(E: attachment 114:5 a2 idafa)`
- selected_branches: none
- constructed_model: The operation is placed inside the `صُدُور` belonging to `ٱلنَّاسِ`. The earlier protected people become the interior site of the threat. The model is not simply danger from outside but intrusion or operation in the human inner domain.
- freeze_point: after 114:5, before final source pair
- predictions_at_freeze: expected clarification of source; expected ambiguity between external and internal/social sources; expected closure returning to classes of beings
- unused_features_tested: 114:6 `مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ`; earlier 114:1-3 `ٱلنَّاسِ`
- corroborators: `(C: 114:6 source pair supplies both non-human and human classes)`; `(C: temporal reactivation of الناس from protected object to vulnerable inner possessors)`; `(C: final الناس makes the protected group also part of the source field)`
- constraints: `(K: no ص د ر lexical branch; only structural locative evidence available)`
- temporal_reactivation_notes: the repeated `ٱلنَّاسِ` changes role: governed by protector in 114:1-3, then possessor of the inner location in 114:5
- rival_models: external-threat-only model is constrained by `فِى صُدُورِ`
- grade: strong
- grade_rationale: highly specific attachment, sequence, and reactivation; no lexical branch needed for the core locative role, though branch support would refine it
- source_queries_or_rows_used: sacred text; attachments 114:5 a1-a2, 114:6 a1

### S114-P2-C07 - Final Source Pair: `مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ`

- seed_type: constructional
- seed: final `مِنَ` phrase with coordinated `ٱلْجِنَّةِ` and `وَٱلنَّاسِ`
- generating_set: `(E: attachment 114:6 a1 coordination)` + `(E: final من source/separation phrase)`
- selected_branches: none
- constructed_model: The passage closes by disclosing the classes from which the whispering threat may arise. The protected class `ٱلنَّاسِ` returns in the final coordinate, making the boundary complex: humans are protected, internally targeted, and also included among the sources of the operation.
- freeze_point: at passage closure
- predictions_at_freeze: none; this is a closure model
- unused_features_tested: prior `ٱلنَّاسِ` repetitions; prior `مِن شَرِّ`; inner locus at 114:5
- corroborators: `(C: repetition of من at 114:4 and 114:6 frames danger/source)`; `(C: repetition of الناس closes the same lexical chain opened in 114:1)`; `(C: coordination row forces jinn and humans into one source pair)`
- constraints: `(K: no جنن/أنس branches; cannot expand lexical content of source classes)`; `(K: final pair does not erase the earlier protective roles of الناس)`
- temporal_reactivation_notes: the final word reactivates all earlier `ٱلنَّاسِ` occurrences and closes the surah on the same class that dominated the opening
- rival_models: a model where danger comes only from an outside demonic source is constrained by coordinated `وَٱلنَّاسِ`
- grade: strong
- grade_rationale: closure and reactivation are specific and structurally forced by coordination
- source_queries_or_rows_used: sacred text; attachment 114:6 a1

### S114-P2-C08 - Double `مِن` Frame

- seed_type: morphosyntactic
- seed: `مِن شَرِّ...` at 114:4 and `مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ` at 114:6
- generating_set: `(E: 114:4 من before threat)` + `(E: 114:6 من before source classes)`
- selected_branches: none
- constructed_model: The passage first marks what refuge is from: the evil of the whisperer. It then marks the source-field from which that whisperer may come: jinn and humans. The first `مِن` opens the danger object; the second closes by classifying provenance.
- freeze_point: after identifying the two `مِن` phrases
- predictions_at_freeze: expected middle material between them to specify the threat mechanism and target
- unused_features_tested: 114:5 relative clause and locative phrase
- corroborators: `(C: 114:5 supplies operation and locus between danger and source frames)`; `(C: attachment 114:6 a1 coordination gives the second frame two members)`
- constraints: `(K: without lexical branches, the two من phrases must be kept structural, not turned into a full lexical source theory)`
- temporal_reactivation_notes: the second `مِن` reactivates the first: refuge-from evil becomes refuge-from an evil whose source classes are now named
- rival_models: treating 114:6 as an unrelated appendage fails because its `مِن` repeats the earlier refuge-frame grammar
- grade: medium-strong
- grade_rationale: strong ordered frame; specificity depends on construction rather than lexical branches
- source_queries_or_rows_used: sacred text; attachments 114:4 a1, 114:6 a1

### S114-P2-C09 - `ٱلنَّاسِ` Recurrence Chain

- seed_type: temporal/acoustic
- seed: repeated `ٱلنَّاسِ` at 114:1, 114:2, 114:3, 114:5, and 114:6
- generating_set: `(E: repetition الناس)` + `(E: idafa rows 114:1 a3, 114:2 a1, 114:3 a1, 114:5 a2)` + `(E: coordination row 114:6 a1)`
- selected_branches: none
- constructed_model: `ٱلنَّاسِ` is the main recurrent token. It begins as the complement to three divine relations, reappears as possessors of the inner locus, and closes as a source class coordinated with `ٱلْجِنَّةِ`. The same sound/form carries the passage from protected object to vulnerable interior to implicated source class.
- freeze_point: after mapping all five occurrences
- predictions_at_freeze: none; full recurrence model is assembled from the whole passage
- unused_features_tested: command/refuge frame; whispering noun-verb recurrence; double `مِن`
- corroborators: `(C: command/refuge frame explains why the repeated class is addressed protectively)`; `(C: whispering mechanism explains why their interiors matter)`; `(C: final source pair creates closure by returning to the repeated word)`
- constraints: `(K: no أنس branch dossier; recurrence is formal and syntactic, not lexical-branch evidence)`; `(K: not every الناس occurrence has the same grammatical role)`
- temporal_reactivation_notes: every later `ٱلنَّاسِ` reactivates the opening triple; the final one forces retrospective distinction between humans as protected and humans as possible sources of whispering
- rival_models: a simple refrain model underexplains the role changes across genitive complement, inner possessor, and coordinate source
- grade: strong
- grade_rationale: exact repetition, ordered role-shifts, and closure are highly passage-specific
- source_queries_or_rows_used: sacred text; attachments 114:1 a3, 114:2 a1, 114:3 a1, 114:5 a2, 114:6 a1

### S114-P2-C10 - `وسواس / يوسوس` Nominal-Verbal Reactivation

- seed_type: temporal/acoustic
- seed: `ٱلْوَسْوَاسِ` at 114:4 and `يُوَسْوِسُ` at 114:5
- generating_set: `(E: repetition of وسوس forms across noun and imperfect verb)` + `(E: attachment 114:4 a1)` + `(E: attachment 114:5 a1)`
- selected_branches: none
- constructed_model: The passage names the threat nominally, then reactivates the same form as an action. This creates an exposure sequence: label first, mechanism second, locus third.
- freeze_point: after 114:5 verb and locative complement
- predictions_at_freeze: expected source classification or closure, since agent/action/locus have been supplied
- unused_features_tested: 114:6 source pair
- corroborators: `(C: 114:6 supplies source pair after action and locus)`; `(C: epithet at 114:4 narrows the nominal label before action unfolds)`
- constraints: `(K: no وسوس lexical branch; relation is surface/root-form recurrence only from allowed evidence)`
- temporal_reactivation_notes: hearing `يُوَسْوِسُ` retrospectively activates `ٱلْوَسْوَاسِ`; the title becomes process
- rival_models: if 114:4 were only a label, 114:5 would be redundant; the noun-to-verb shift makes it progressive
- grade: medium-strong
- grade_rationale: strong formal recurrence and temporal transformation; lexical branch data absent
- source_queries_or_rows_used: sacred text; attachments 114:4 a1-a2, 114:5 a1

### S114-P2-C11 - Interior Threat after Exterior Titles

- seed_type: verified composite
- seed: composite verified from C02 + C06 + C07
- generating_set: `(E: triple idafa divine roles over الناس)` + `(E: في صدور الناس locative)` + `(E: final من الجنة والناس source pair)`
- selected_branches: none
- constructed_model: The passage first surrounds `ٱلنَّاسِ` with protective divine relations, then reveals that the danger operates in their inner domain, then discloses that the source-field includes both hidden and human classes. The compact latent structure is a protection-address that anticipates a hidden interior operation and closes by widening the source boundary.
- freeze_point: after constructing from 114:1-6 structural trajectory
- predictions_at_freeze: none; composite is whole-passage
- unused_features_tested: command frame; double `مِن`; وسواس/yوسوس recurrence; epithet
- corroborators: `(C: command frame makes the protection-address recitable)`; `(C: double من separates danger-object and source-field)`; `(C: وسواس/yوسوس recurrence names then operationalizes the threat)`; `(C: epithet narrowing prepares the delayed explanation)`
- constraints: `(K: all lexical branch dossiers unavailable; model must remain a structural-temporal synthesis, not a branch-rich lexical synthesis)`; `(K: no translation evidence used)`
- temporal_reactivation_notes: `ٱلنَّاسِ` is repeatedly stabilized before being relocated inward; `ٱلْوَسْوَاسِ` is named before becoming a process; the final `ٱلنَّاسِ` reopens the protected class as a possible source-class member
- rival_models: purely external-protection model fails at `فِى صُدُورِ`; purely internal-psychological model fails at `مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ`; generic refuge model fails to explain the ordered recurrence of `ٱلنَّاسِ`
- grade: medium-strong
- grade_rationale: coherent whole-passage trajectory with multiple independent structural corroborators; cannot be upgraded to strong lexical synthesis because furuq branches are unavailable
- source_queries_or_rows_used: sacred text; attachments 114:1 a1-a3, 114:2 a1, 114:3 a1, 114:4 a1-a2, 114:5 a1-a2, 114:6 a1

### S114-P2-C12 - Ayah-Boundary Disclosure Sequence

- seed_type: temporal/acoustic
- seed: ayah sequence 1->6
- generating_set: `(E: ayah 1 command/refuge)` + `(E: ayah 2-3 title continuation)` + `(E: ayah 4 threat name)` + `(E: ayah 5 operation/locus)` + `(E: ayah 6 source pair)`
- selected_branches: none
- constructed_model: The passage discloses roles in a staged order: instructed refuge, protective titles, threat, operation and inner locus, source classes. Each later stage answers an expectation opened earlier.
- freeze_point: after full ayah-sequence assembly
- predictions_at_freeze: none; temporal model is complete
- unused_features_tested: repeated `ٱلنَّاسِ`, repeated `وسوس`, preposition pattern
- corroborators: `(C: الناس recurrence links stages 1-3, 5, 6)`; `(C: وسوس recurrence links threat-name to operation)`; `(C: من...من frames danger and source)`
- constraints: `(K: no lexical branch support; stage labels come from syntax and surface sequence only)`
- temporal_reactivation_notes: 114:4 reactivates 114:1's refuge; 114:5 reactivates 114:4's whisperer; 114:6 reactivates both 114:4's `مِن` and the repeated `ٱلنَّاسِ`
- rival_models: shuffled order would lose prediction: source classes before inner operation would not close the same expectation; threat before divine titles would not create the same protected-field setup
- grade: strong
- grade_rationale: order-sensitive model explains why the passage closes where it does and why earlier expressions reactivate
- source_queries_or_rows_used: sacred text; all S114 attachment rows

## Exhaustiveness Check

- Every rooted occurrence recoverable from the allowed S114 attachment rows was given an individual lexical seed pass: L01-L16.
- Every lexical seed was restarted from its own occurrence, including repeated `ٱلنَّاسِ` and repeated `وسوس` forms.
- No lexical branch was silently omitted: all lexical branches are unavailable because `furuq_v4.sqlite` is empty.
- Eligible constructional, morphosyntactic, temporal, and verified composite seeds were separately initiated: C01-C12.
- Construction and corroboration/constraint were kept separate in each retained constructional finding.
- Basmala was not used as a seed.
- No translation evidence was used.

## Image Packet Catalog

### IMG-S114-01 - Commanded Refuge Speech

- Starting seed: `قُلْ` + quoted `أَعُوذُ`
- Complete image: reciter is commanded into a refuge utterance before the danger is named
- Passage-order assembly: 114:1 opens; 114:4 supplies danger; 114:5-6 explain mechanism/source
- Participants and roles: commanded speaker; protecting addressee; threat later disclosed
- Operation / mechanism: speech act establishes refuge
- Direction / force / medium: utterance directed toward protective divine relation
- Temporal development: command -> refuge -> protector titles -> threat
- Outcome / closure: source field named at 114:6
- Exact branch constituents: none; branch dossiers unavailable
- Unfilled roles: lexical branch detail for `قُلْ`, `أَعُوذُ`, `رَبِّ`
- Status: FRAGMENT

### IMG-S114-02 - Layered Protection over Humans

- Starting seed: repeated idafa `رَبِّ/مَلِكِ/إِلَٰهِ ٱلنَّاسِ`
- Complete image: the same people are placed under successive protective/governing/divine relations before threat disclosure
- Passage-order assembly: 114:1, 114:2, 114:3
- Participants and roles: divine title-bearer; `ٱلنَّاسِ` as repeated genitive complement
- Operation / mechanism: repeated genitive binding thickens the protected field
- Direction / force / medium: title relation over the repeated human class
- Temporal development: role 1 -> role 2 -> role 3 -> threat
- Outcome / closure: humans later become inner target and final source-class member
- Exact branch constituents: none; branch dossiers unavailable
- Unfilled roles: lexical differences among `رَبّ`, `مَلِك`, `إِلَه`
- Status: COMPLETE structurally, FRAGMENT lexically

### IMG-S114-03 - Hidden Inner Whisper Operation

- Starting seed: `ٱلْوَسْوَاسِ` -> `يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ`
- Complete image: named whisperer becomes ongoing operation inside human chests
- Passage-order assembly: 114:4 name/epithet; 114:5 action/locus
- Participants and roles: whisperer; operation; human inner locus
- Operation / mechanism: noun title reactivated as verb process
- Direction / force / medium: operation occurs `فِى صُدُورِ`
- Temporal development: threat named -> narrowed by epithet -> action disclosed -> locus disclosed
- Outcome / closure: source classes named in 114:6
- Exact branch constituents: none; branch dossiers unavailable
- Unfilled roles: lexical branches for `وسوس`, `خنس`, `صدر`
- Status: COMPLETE structurally, FRAGMENT lexically

### IMG-S114-04 - Boundary-Complex Source Field

- Starting seed: final `مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ`
- Complete image: danger source is disclosed as a coordinated pair, including the same humans who were earlier protected and targeted
- Passage-order assembly: 114:6 after 114:1-5
- Participants and roles: jinn; humans; whispering source field
- Operation / mechanism: final `مِن` classifies provenance/source after mechanism is known
- Direction / force / medium: from source classes toward inner human locus
- Temporal development: refuge from evil -> named whisperer -> inner operation -> source classes
- Outcome / closure: final `ٱلنَّاسِ` reactivates and closes the repeated human chain
- Exact branch constituents: none; branch dossiers unavailable
- Unfilled roles: lexical branches for `ج ن ن`, `أ ن س`
- Status: COMPLETE structurally, FRAGMENT lexically
