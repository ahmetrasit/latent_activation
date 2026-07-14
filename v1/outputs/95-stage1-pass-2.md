# S95 Stage 1 Pass 2

Assigned passage: S95, ayat 1-8. Basmala is present in `resources/quran/surah_95.json` as opening context only and was not used to initiate seeds.

## Restart and Resource Note

Root cause of the Pass 1 limitation: the prompt-named SQLite resources are present locally but empty. `resources/qac.sqlite` is 0 bytes and has no visible `qac_words` or `qac_morphemes` tables. `resources/furuq_v4.sqlite` is 0 bytes and has no visible `branch_images` table. Because Stage 1 authorizes only those SQLite resources for QAC morphology and furuq branch dossiers, branch-level lexical seeding cannot retrieve `branch_id`, `branch_image_ar`, or `what_is_ar` here.

This restart therefore separates:

- lexical branch passes: exhaustively initiated for every recoverable rooted occurrence, but terminated as `BRANCH_BLOCKED`;
- constructional, morphosyntactic, and temporal passes: completed from `resources/quran/surah_95.json` and S95 rows of `resources/attachments.tsv`;
- opening context: basmala noted only as opening context, with no seed initiated.

No translation was used.

## Authorized Evidence Actually Available

- Sacred Arabic text: `resources/quran/surah_95.json`.
- Attachment rows for S95: `ae:v3:s095:001:pass1:attach:a1-a3`, `ae:v3:s095:002:pass1:attach:a1-a2`, `ae:v3:s095:003:pass1:attach:a1-a3`, `ae:v3:s095:004:pass1:attach:a1-a3`, `ae:v3:s095:005:pass1:attach:a1-a3`, `ae:v3:s095:006:pass1:attach:a1-a7`, `ae:v3:s095:007:pass1:attach:a1-a4`, `ae:v3:s095:008:pass1:attach:a1-a4`.
- QAC and furuq branch dossiers: unavailable because the authorized SQLite files have no schema/content.

## Exhaustive Lexical Restart Ledger

All lexical seed passes below were initiated from the first recoverable rooted word in passage order. For each, the required next step was to read the furuq dossier for the root. That step failed uniformly because `resources/furuq_v4.sqlite` has no table content. Therefore no branch ID can be named, no branch image can be quoted, and no lexical avalanche can be validly constructed.

Common result for every lexical row:

- `seed_type`: lexical occurrence
- `generating_set`: seed occurrence only; no furuq branch available
- `selected_branches`: none
- `constructed_model`: none; `BRANCH_BLOCKED`
- `freeze_point`: before branch image formation
- `predictions_at_freeze`: none
- `unused_features_tested`: attachment rows and later sequence could not test a nonexistent branch image
- `corroborators`: none
- `constraints`: required furuq branch dossier unavailable
- `grade`: unlikely
- `grade_rationale`: not a negative lexical judgment; the seed is evidentially blocked in this workspace
- `source_queries_or_rows_used`: sacred text plus relevant attachment row(s); furuq query attempted but no schema/table exists

| seed_id | occurrence | recovered root | attachment evidence | status |
| --- | --- | --- | --- | --- |
| LEX-95-001 | 95:1 `ٱلتِّينِ` | ت ي ن | `ae:v3:s095:001:pass1:attach:a1`, `a3` | BRANCH_BLOCKED |
| LEX-95-002 | 95:1 `ٱلزَّيْتُونِ` | ز ي ت | `ae:v3:s095:001:pass1:attach:a2`, `a3` | BRANCH_BLOCKED |
| LEX-95-003 | 95:2 `طُورِ` | ط و ر | `ae:v3:s095:002:pass1:attach:a1`, `a2` | BRANCH_BLOCKED |
| LEX-95-004 | 95:2 `سِينِينَ` | س ي ن | `ae:v3:s095:002:pass1:attach:a2` | BRANCH_BLOCKED |
| LEX-95-005 | 95:3 `ٱلْبَلَدِ` | ب ل د | `ae:v3:s095:003:pass1:attach:a2`, `a3` | BRANCH_BLOCKED |
| LEX-95-006 | 95:3 `ٱلْأَمِينِ` | أ م ن | `ae:v3:s095:003:pass1:attach:a3` | BRANCH_BLOCKED |
| LEX-95-007 | 95:4 `خَلَقْنَا` | خ ل ق | `ae:v3:s095:004:pass1:attach:a1`, `a2` | BRANCH_BLOCKED |
| LEX-95-008 | 95:4 `ٱلْإِنسَٰنَ` | أ ن س | `ae:v3:s095:004:pass1:attach:a1` | BRANCH_BLOCKED |
| LEX-95-009 | 95:4 `أَحْسَنِ` | ح س ن | `ae:v3:s095:004:pass1:attach:a2`, `a3` | BRANCH_BLOCKED |
| LEX-95-010 | 95:4 `تَقْوِيمٍ` | ق و م | `ae:v3:s095:004:pass1:attach:a3` | BRANCH_BLOCKED |
| LEX-95-011 | 95:5 `رَدَدْنَٰهُ` | ر د د | `ae:v3:s095:005:pass1:attach:a1`, `a2` | BRANCH_BLOCKED |
| LEX-95-012 | 95:5 `أَسْفَلَ` | س ف ل | `ae:v3:s095:005:pass1:attach:a2`, `a3` | BRANCH_BLOCKED |
| LEX-95-013 | 95:5 `سَٰفِلِينَ` | س ف ل | `ae:v3:s095:005:pass1:attach:a3` | BRANCH_BLOCKED |
| LEX-95-014 | 95:6 `ءَامَنُوا۟` | أ م ن | `ae:v3:s095:006:pass1:attach:a2` | BRANCH_BLOCKED |
| LEX-95-015 | 95:6 `عَمِلُوا۟` | ع م ل | `ae:v3:s095:006:pass1:attach:a2`, `a3` | BRANCH_BLOCKED |
| LEX-95-016 | 95:6 `ٱلصَّٰلِحَٰتِ` | ص ل ح | `ae:v3:s095:006:pass1:attach:a3` | BRANCH_BLOCKED |
| LEX-95-017 | 95:6 `أَجْرٌ` | أ ج ر | `ae:v3:s095:006:pass1:attach:a4`, `a5`, `a6` | BRANCH_BLOCKED |
| LEX-95-018 | 95:6 `غَيْرُ` | غ ي ر | `ae:v3:s095:006:pass1:attach:a6`, `a7` | BRANCH_BLOCKED |
| LEX-95-019 | 95:6 `مَمْنُونٍ` | م ن ن | `ae:v3:s095:006:pass1:attach:a7` | BRANCH_BLOCKED |
| LEX-95-020 | 95:7 `يُكَذِّبُكَ` | ك ذ ب | `ae:v3:s095:007:pass1:attach:a1`, `a2`, `a3`, `a4` | BRANCH_BLOCKED |
| LEX-95-021 | 95:7 `بَعْدُ` | ب ع د | `ae:v3:s095:007:pass1:attach:a3` | BRANCH_BLOCKED |
| LEX-95-022 | 95:7 `ٱلدِّينِ` | د ي ن | `ae:v3:s095:007:pass1:attach:a4` | BRANCH_BLOCKED |
| LEX-95-023 | 95:8 `ٱللَّهُ` | أ ل ه | `ae:v3:s095:008:pass1:attach:a1` | BRANCH_BLOCKED |
| LEX-95-024 | 95:8 `أَحْكَمِ` | ح ك م | `ae:v3:s095:008:pass1:attach:a2`, `a3`, `a4` | BRANCH_BLOCKED |
| LEX-95-025 | 95:8 `ٱلْحَٰكِمِينَ` | ح ك م | `ae:v3:s095:008:pass1:attach:a4` | BRANCH_BLOCKED |

Function-word roots recoverable from attachment rows were also initiated, but only as function-root or constructional seeds because the rows classify them as conjunction, exception particle, preposition, or uninflected verb rather than ordinary content nouns/verbs. They are not allowed to create unattested lexical meanings.

| seed_id | occurrence / construction | recovered root | attachment evidence | status |
| --- | --- | --- | --- | --- |
| FUNC-95-001 | oath `وَ` governing 95:1 `ٱلتِّينِ` | أ و ي | `ae:v3:s095:001:pass1:attach:a1` | STRUCTURAL_ONLY |
| FUNC-95-002 | oath `وَ` governing 95:1 `ٱلزَّيْتُونِ` | أ و ي | `ae:v3:s095:001:pass1:attach:a2` | STRUCTURAL_ONLY |
| FUNC-95-003 | oath `وَ` governing 95:2 `طُورِ` | أ و ي | `ae:v3:s095:002:pass1:attach:a1` | STRUCTURAL_ONLY |
| FUNC-95-004 | oath `وَ` governing 95:3 `هَٰذَا` | أ و ي | `ae:v3:s095:003:pass1:attach:a1` | STRUCTURAL_ONLY |
| FUNC-95-005 | exception `إِلَّا` | أ ل و | `ae:v3:s095:006:pass1:attach:a1` | STRUCTURAL_ONLY |
| FUNC-95-006 | preposed predicate `لَهُمْ` / `لـ` | و ل ي | `ae:v3:s095:006:pass1:attach:a4`, `a5` | STRUCTURAL_ONLY |
| FUNC-95-007 | negative copular question `أَلَيْسَ` | ل ي س | `ae:v3:s095:008:pass1:attach:a1`, `a2` | STRUCTURAL_ONLY |

These function-root seeds are developed below as constructional or morphosyntactic passes.

## Constructional and Temporal Seed Passes

### CSU-95-001: Oath Chain as Staged Witnessing Field

- `candidate_id`: CSU-95-001
- `ayah_range`: 95:1-4
- `seed_type`: constructional / temporal
- `seed`: the repeated oath construction in 95:1-3
- `generating_set`: `(E: oath particle_complement rows 95:1:a1, 95:1:a2, 95:2:a1, 95:3:a1)`, `(E: coordination row 95:1:a3)`, `(E: apposition row 95:3:a2)`, `(E: adjective row 95:3:a3)`
- `selected_branches`: none; branch source unavailable
- `constructed_model`: the recitation opens with a sequence of sworn terms: paired cultivated nouns, then a construct place-name, then a demonstrative-localized secure city. The image is not lexical fruit symbolism; it is a staged evidentiary field moving from paired oath objects to a named elevation and then to an immediately indicated secure locality.
- `freeze_point`: after 95:3 before 95:4
- `predictions_at_freeze`: the oath chain should release a forceful proposition; the demonstrative `هَٰذَا` should make the final oath term locally weight-bearing; the secure/local term should reactivate when later human safety, belief, judgment, or order appears.
- `unused_features_tested`: 95:4 `لَقَدْ خَلَقْنَا`; 95:4 object `ٱلْإِنسَٰنَ`; 95:6 second `أ م ن` occurrence; 95:8 final judgment predicate.
- `corroborators`: `(C: 95:4 laqad + created-object clause follows the oath chain)`, `(C: 95:3:a2 apposition makes البلد the demonstrative referent)`, `(C: 95:3:a3 الأمين qualifies the place before 95:6 ءامنوا reuses the same recovered root class)`.
- `constraints`: `(K: no furuq branch dossiers for تين, زيت, طور, سين, بلد, أمن; lexical content beyond structural oath/locality cannot be validated here)`.
- `temporal_reactivation_notes`: the oath terms create suspended force until 95:4. The secure locality in 95:3 becomes available for reactivation when the exception class in 95:6 is characterized by `ءَامَنُوا۟`.
- `rival_models`: a purely lexical ecology/topography model may exist, but cannot be formed without branch dossiers.
- `grade`: medium
- `grade_rationale`: strong syntax and sequence, but weak lexical depth due to blocked furuq dossiers.
- `source_queries_or_rows_used`: `resources/quran/surah_95.json`; attachment rows `95:1:a1-a3`, `95:2:a1-a2`, `95:3:a1-a3`, `95:4:a1-a3`, `95:6:a2`.

### CSU-95-002: Best Formation to Lowest Return

- `candidate_id`: CSU-95-002
- `ayah_range`: 95:4-5
- `seed_type`: constructional / morphosyntactic
- `seed`: `فِىٓ أَحْسَنِ تَقْوِيمٍۢ` followed by `ثُمَّ رَدَدْنَٰهُ أَسْفَلَ سَٰفِلِينَ`
- `generating_set`: `(E: 95:4:a1 الإنسان direct object of خلقنا)`, `(E: 95:4:a2 في أحسن as state/setting of خلقنا)`, `(E: 95:4:a3 تقويم idafa complement of أحسن)`, `(E: 95:5:a1 ه object suffix of رددناه)`, `(E: 95:5:a2 أسفل سافلين resulting state/rank)`, `(E: 95:5:a3 سافلين idafa complement of أسفل)`
- `selected_branches`: none; branch source unavailable
- `constructed_model`: a vertical transition image: a human object is first set in the best formation/setting, then the same object is returned into the lowest rank/state. The repeated elative structures create an upper/lower axis.
- `freeze_point`: after 95:5 before the exception in 95:6
- `predictions_at_freeze`: if the lower-return state is not total, an exception or rescue boundary should appear; if the axis is evaluative, later material should identify criteria for remaining outside the downward return.
- `unused_features_tested`: 95:6 `إِلَّا`; 95:6 `ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ`; 95:6 `أَجْرٌ غَيْرُ مَمْنُونٍ`; 95:8 `أَحْكَمِ ٱلْحَٰكِمِينَ`.
- `corroborators`: `(C: 95:6:a1 exception row supplies the predicted boundary)`, `(C: 95:6:a2-a3 coordinated belief/action and object supply criteria inside the exception)`, `(C: 95:6:a4-a7 reward predicate supplies non-downward outcome)`, `(C: 95:8:a2-a4 final أَحْكَمِ repeats the elative pattern at closure)`.
- `constraints`: `(K: branch evidence for خلق, قوم, ردد, سفل is unavailable; image is structural, not a lexical branch synthesis)`.
- `temporal_reactivation_notes`: the pronoun in `رَدَدْنَٰهُ` reactivates `ٱلْإِنسَٰنَ`; the exception then reopens the immediately prior downward result.
- `rival_models`: a creation-only honor model stops at 95:4 and fails to predict the return/exception sequence; a punishment-only model misses the initial best-formation pole.
- `grade`: medium-strong
- `grade_rationale`: high structural fit and clear temporal prediction, though lexical branch support is blocked.
- `source_queries_or_rows_used`: attachment rows `95:4:a1-a3`, `95:5:a1-a3`, `95:6:a1-a7`, `95:8:a2-a4`.

### CSU-95-003: Exception Gate and Non-Depleted Outcome

- `candidate_id`: CSU-95-003
- `ayah_range`: 95:5-6
- `seed_type`: constructional
- `seed`: `إِلَّا ٱلَّذِينَ` after the downward-return clause
- `generating_set`: `(E: 95:6:a1 الذين as visible excepted term under إلا)`, `(E: 95:6:a2 عملوا coordinated with آمنوا)`, `(E: 95:6:a3 الصالحات object of عملوا)`, `(E: 95:6:a4 لهم as preposed predicate)`, `(E: 95:6:a5 أجر as delayed subject)`, `(E: 95:6:a6 غير as qualifier)`, `(E: 95:6:a7 ممنون as idafa complement)`
- `selected_branches`: none; branch source unavailable
- `constructed_model`: an exception gate opens after the lowest-return image and identifies a class by two coordinated internal/external criteria, then assigns them a preposed possession/benefit predicate and a reward qualified as not `مَمْنُونٍ`.
- `freeze_point`: after forming 95:6
- `predictions_at_freeze`: subsequent material should ask what could still deny or reject the moral/judicial order after the exception has been displayed; closure should locate authority for the distinction.
- `unused_features_tested`: 95:7 `فَمَا يُكَذِّبُكَ بَعْدُ بِٱلدِّينِ`; 95:8 final laysa question.
- `corroborators`: `(C: 95:7:a3 بعد marks later evaluation after the preceding evidence)`, `(C: 95:7:a4 بالدين provides the object/domain of denial after the exception)`, `(C: 95:8:a1-a4 final predicate supplies judging authority)`.
- `constraints`: `(K: cannot claim lexical details of أمن, عمل, صلح, أجر, غير, منن without branch dossiers)`.
- `temporal_reactivation_notes`: `إِلَّا` forces backward access to 95:5. The reward phrase then redirects the downward axis into a preserved counter-outcome.
- `rival_models`: an exception as mere grammatical appendage is possible, but it underexplains the immediate reward predicate and later `بعد`.
- `grade`: medium-strong
- `grade_rationale`: precise grammar and sequence; branch-level semantics blocked.
- `source_queries_or_rows_used`: attachment rows `95:5:a2-a3`, `95:6:a1-a7`, `95:7:a3-a4`, `95:8:a1-a4`.

### CSU-95-004: Repeated Root-Class Reactivation of Security/Faith

- `candidate_id`: CSU-95-004
- `ayah_range`: 95:3 and 95:6
- `seed_type`: morphosyntactic / temporal
- `seed`: occurrence pair `ٱلْأَمِينِ` in 95:3 and `ءَامَنُوا۟` in 95:6, both recovered by attachment rows as root class `أ م ن`
- `generating_set`: `(E: 95:3:a3 الأمين adjective agreeing with البلد)`, `(E: 95:6:a2 عملوا coordinated with آمنوا, making آمنوا the first criterion in the exception class)`
- `selected_branches`: none; no branch ID available
- `constructed_model`: the oath field contains a secure/trustworthy city before the central human-return claim. Later, the exception class begins with the same recovered root class in verbal plural form. The temporal effect is a reactivation from place-quality to human criterion.
- `freeze_point`: after identifying the pair 95:3 -> 95:6
- `predictions_at_freeze`: the reactivated root class should not stand alone; it should be paired with a second criterion and then a stabilized outcome.
- `unused_features_tested`: 95:6 coordinated `وَعَمِلُوا۟`; 95:6 object `ٱلصَّٰلِحَٰتِ`; 95:6 reward predicate.
- `corroborators`: `(C: 95:6:a2 coordination supplies paired criterion)`, `(C: 95:6:a3 object of عملوا supplies the criterion's object)`, `(C: 95:6:a4-a7 reward predicate supplies stabilized outcome)`.
- `constraints`: `(K: root-class recurrence is not enough to identify a shared branch; furuq branch dossier unavailable)`, `(K: 95:3 is adjectival place-description, 95:6 is verbal criterion; they should not be flattened into one translation)`.
- `temporal_reactivation_notes`: the earlier secure city is not used as a seed translation for faith; it is a latent cue reactivated by the later exception class.
- `rival_models`: a non-reactivating reading treats 95:3 and 95:6 as unrelated; viable, but less explanatory of repeated recovered root class.
- `grade`: medium
- `grade_rationale`: real temporal/root-class recurrence, but no branch-level lexical confirmation.
- `source_queries_or_rows_used`: attachment rows `95:3:a3`, `95:6:a2-a7`.

### CSU-95-005: Elative Scale Closure

- `candidate_id`: CSU-95-005
- `ayah_range`: 95:4-8
- `seed_type`: temporal/acoustic / morphosyntactic
- `seed`: elative/construct sequence `أَحْسَنِ تَقْوِيمٍ`, `أَسْفَلَ سَٰفِلِينَ`, `أَحْكَمِ ٱلْحَٰكِمِينَ`
- `generating_set`: `(E: 95:4:a2-a3 أحسن تقويم)`, `(E: 95:5:a2-a3 أسفل سافلين)`, `(E: 95:8:a2-a4 أحكم الحاكمين)`
- `selected_branches`: none; branch source unavailable
- `constructed_model`: the surah creates an evaluative ladder: best formation, lowest of low ones, then most decisive/wise/judging among judges as the final predicate. The closing elative is not isolated; it answers the earlier vertical spread.
- `freeze_point`: after observing 95:5, before 95:6-8
- `predictions_at_freeze`: a scale this explicit should be resolved by a discriminating criterion and a final authority.
- `unused_features_tested`: 95:6 exception criteria and reward; 95:7 denial of `الدين`; 95:8 final laysa predicate.
- `corroborators`: `(C: 95:6:a1 exception supplies discrimination)`, `(C: 95:6:a2-a7 criteria plus outcome fill the discriminated classes)`, `(C: 95:7:a4 بالدين makes judgment/order explicit structurally)`, `(C: 95:8:a1-a4 supplies final authority)`.
- `constraints`: `(K: no lexical branch support for حسن, سفل, حكم; this remains an elative-pattern candidate)`.
- `temporal_reactivation_notes`: 95:8 reactivates the morphology of 95:4 and the rank contrast of 95:5. The close resolves the scale rather than merely adding a divine title.
- `rival_models`: a simple three-superlative stylistic observation; weaker because it does not explain the exception and denial question.
- `grade`: medium-strong
- `grade_rationale`: strong formal recurrence and closure behavior; lexical branch detail unavailable.
- `source_queries_or_rows_used`: attachment rows `95:4:a2-a3`, `95:5:a2-a3`, `95:6:a1-a7`, `95:7:a4`, `95:8:a1-a4`.

### CSU-95-006: Afterward Denial as Retrospective Challenge

- `candidate_id`: CSU-95-006
- `ayah_range`: 95:7-8 with backward scope to 95:1-6
- `seed_type`: constructional / temporal
- `seed`: `فَمَا يُكَذِّبُكَ بَعْدُ بِٱلدِّينِ`
- `generating_set`: `(E: 95:7:a1 ما as interrogative subject)`, `(E: 95:7:a2 ك suffix object of يكذب)`, `(E: 95:7:a3 بعد as temporal adverb)`, `(E: 95:7:a4 بالدين as bāʾ-governed complement)`
- `selected_branches`: none; branch source unavailable
- `constructed_model`: the question is temporally conditioned: `بَعْدُ` asks what could deny after the oath, creation, return, exception, and reward sequence has already been recited. It creates a backward replay demand.
- `freeze_point`: after 95:7 before 95:8
- `predictions_at_freeze`: closure should answer with authority rather than more evidence; the authority should match the domain of `الدين`.
- `unused_features_tested`: 95:8 `أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ`.
- `corroborators`: `(C: 95:8:a1 الله as laysa subject)`, `(C: 95:8:a2-a4 bāʾ-marked predicate أحكم الحاكمين answers the judgment/order domain)`.
- `constraints`: `(K: lexical branches for كذب, بعد, دين, حكم unavailable; cannot specify their branch imagery)`.
- `temporal_reactivation_notes`: `بَعْدُ` is the explicit reactivation trigger. It compels the listener to treat 95:1-6 as already available evidence.
- `rival_models`: a local rhetorical question only; viable but fails to use `بعد` as a sequencing operator.
- `grade`: strong structurally, medium overall
- `grade_rationale`: excellent temporal role, but lexical depth blocked.
- `source_queries_or_rows_used`: attachment rows `95:7:a1-a4`, `95:8:a1-a4`.

### CSU-95-007: Final Judgment Predicate as Closure

- `candidate_id`: CSU-95-007
- `ayah_range`: 95:8
- `seed_type`: morphosyntactic / closure
- `seed`: `أَلَيْسَ ٱللَّهُ بِأَحْكَمِ ٱلْحَٰكِمِينَ`
- `generating_set`: `(E: 95:8:a1 الله as nominative ism of أليس)`, `(E: 95:8:a2 bāʾ-marked predicate)`, `(E: 95:8:a3 أحكم governed by bāʾ)`, `(E: 95:8:a4 الحاكمين idafa complement of أحكم)`
- `selected_branches`: none; branch source unavailable
- `constructed_model`: the close is a negative interrogative whose predicate is a superlative construct. It supplies the final adjudicating authority for the preceding scale, exception, reward, and denial question.
- `freeze_point`: at closure
- `predictions_at_freeze`: none beyond closure; this is a terminating candidate.
- `unused_features_tested`: backward: 95:4-5 elative axis, 95:6 exception/outcome, 95:7 `الدين`.
- `corroborators`: `(C: 95:4:a2-a3 earlier أحسن construct)`, `(C: 95:5:a2-a3 earlier أسفل construct)`, `(C: 95:6:a1 exception requires discrimination)`, `(C: 95:7:a4 بالدين gives the domain answered by حكم construction)`.
- `constraints`: `(K: cannot claim a specific حكم branch or divine-name branch from furuq)`.
- `temporal_reactivation_notes`: as the final ayah, it retrospectively stabilizes the prior sequence: what began as oath, formation, fall, exception, and denial closes as judgment.
- `rival_models`: final praise alone; weaker because the predicate form is syntactically tied to the immediately prior question.
- `grade`: medium-strong
- `grade_rationale`: strong closure and attachment support; lexical branch support absent.
- `source_queries_or_rows_used`: attachment rows `95:4:a2-a3`, `95:5:a2-a3`, `95:6:a1`, `95:7:a4`, `95:8:a1-a4`.

## Failed or Terminated Construction Seeds

### TERM-95-001: Fruit-Pair Lexical Ecology

- `seed`: `ٱلتِّينِ` + `ٱلزَّيْتُونِ`
- `initial image`: paired oath nouns in 95:1.
- `termination`: branch dossiers for ت ي ن and ز ي ت are unavailable; no authorized lexical branch image can be formed.
- `retained structural note`: coordination and shared oath role are valid `(C/K: 95:1:a1-a3)`, but lexical ecology remains unbuilt.
- `grade`: unlikely / blocked.

### TERM-95-002: Mountain/Sinin Lexical Topography

- `seed`: `طُورِ سِينِينَ`
- `initial image`: construct phrase under oath in 95:2.
- `termination`: branch dossiers for ط و ر and س ي ن are unavailable; no lexical topography image can be formed.
- `retained structural note`: idafa is forced `(C/K: 95:2:a2)`.
- `grade`: unlikely / blocked.

### TERM-95-003: Reward-Without-Depletion Lexical Image

- `seed`: `أَجْرٌ غَيْرُ مَمْنُونٍ`
- `initial image`: reward predicate with negative qualifier.
- `termination`: branch dossiers for أ ج ر, غ ي ر, and م ن ن are unavailable.
- `retained structural note`: preposed `لهم`, delayed `أجر`, qualifier `غير`, and idafa complement `ممنون` are structurally secure `(C/K: 95:6:a4-a7)`.
- `grade`: unlikely / blocked as lexical image; medium as a structural component inside CSU-95-003.

## Image Packet Catalog

### IMAGE-S95-A: Witness Field to Human Formation

- Starting seed: repeated oath construction in 95:1-3.
- Complete image: oath terms create suspended evidentiary force, discharged by the human-creation proposition in 95:4.
- Passage-order assembly: paired nouns -> construct place -> demonstrative secure city -> `لَقَدْ خَلَقْنَا`.
- Participants and roles: sworn terms as witnesses; human as object of creation.
- Operation / mechanism: oath accumulation followed by emphatic proposition.
- Direction / force / medium: temporal buildup.
- Temporal development: 95:1-3 suspension; 95:4 release.
- Outcome / closure: supports later retrospective challenge.
- Exact branch constituents: none; branch source unavailable.
- Unfilled roles: lexical meanings of oath terms.
- Status: FRAGMENT.

### IMAGE-S95-B: Vertical Formation and Return

- Starting seed: `فِىٓ أَحْسَنِ تَقْوِيمٍ` -> `أَسْفَلَ سَٰفِلِينَ`.
- Complete image: human object set at best formation, then returned to lowest rank/state, with exception boundary.
- Passage-order assembly: creation object -> best formation -> return pronoun -> lowest state -> exception.
- Participants and roles: Creator subject, human object, return object pronoun, excepted class.
- Operation / mechanism: formation, return, exception.
- Direction / force / medium: vertical/evaluative descent and preservation.
- Temporal development: 95:4 high pole; 95:5 low pole; 95:6 exception.
- Outcome / closure: final judgment predicate resolves the scale.
- Exact branch constituents: none; branch source unavailable.
- Unfilled roles: lexical branches for خلق, قوم, ردد, سفل, حكم.
- Status: FRAGMENT, structurally strong.

### IMAGE-S95-C: Retrospective Judgment Challenge

- Starting seed: `فَمَا يُكَذِّبُكَ بَعْدُ بِٱلدِّينِ`.
- Complete image: after the full sequence, denial is challenged and answered by final judging authority.
- Passage-order assembly: after-marker -> denial question -> `الدين` complement -> laysa question -> `أحكم الحاكمين`.
- Participants and roles: denier/question subject, addressed object suffix, domain of judgment, God as final subject.
- Operation / mechanism: backward replay and closure.
- Direction / force / medium: retrospective evaluation.
- Temporal development: 95:7 reopens 95:1-6; 95:8 closes.
- Outcome / closure: final authority stated as superlative predicate.
- Exact branch constituents: none; branch source unavailable.
- Unfilled roles: lexical branches for كذب, دين, حكم.
- Status: FRAGMENT, structurally strong.

## Exhaustiveness Check

After file creation, I checked whether the restart covered:

- every rooted content occurrence recoverable from S95 attachment rows: yes, LEX-95-001 through LEX-95-025;
- every rooted function-word construction recoverable from S95 attachment rows: yes, FUNC-95-001 through FUNC-95-007;
- repeated rooted occurrences as separate seeds: yes, أ م ن, س ف ل, and ح ك م repeats are separated;
- eligible constructions: oath chain, idafa/apposition/adjective, creation-object/state, return-object/result-state, exception, coordinated criteria, reward predicate, denial question, and final laysa predicate are covered;
- temporal/acoustic reactivation points: oath suspension, pronoun reactivation, exception reopening, `بعد` retrospective replay, and final elative closure are covered;
- branch images: no, because the authorized furuq SQLite source is empty. Potentially missing images are exactly the branch-dependent lexical images for the roots listed in the lexical restart ledger. They must be regenerated if `resources/qac.sqlite` and `resources/furuq_v4.sqlite` are restored with their expected tables.
