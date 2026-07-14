# S82 Stage 1 Pass 2: Temporally Conditioned Reactivation

Assigned passage: S82, al-Infithar, ayat 1-19.

Sacred Arabic source: `resources/quran/surah_82.json`.

## Root Cause Of The Pass 1 Limitation

The limitation had two causes.

1. The required primary SQLite resources in this workspace, `resources/qac.sqlite` and `resources/furuq_v4.sqlite`, are zero-byte files. They have no schema or tables, so the required direct queries against `qac_words`, `qac_morphemes`, and `branch_images` cannot run here.

2. Pass 1 over-compressed the discovery pass. It identified the main convergences but grouped many singleton lexical seeds into families instead of giving every eligible rooted occurrence, branch, construction, morphosyntactic frame, and temporal/acoustic cue its own seed pass.

Recovery note: because the SQLite files are empty, this pass used the checked-in exported resource TSVs generated from the same resource names by `v1/scripts/export_v4_tsvs.py`: `resources/qac_root_ayah.tsv` for rooted occurrence metadata and `resources/v4_branches.tsv` for branch rows. `resources/attachments.tsv` was used only for S82 rows. This is a limitation of the local artifact state, not a new external source.

## Resource Slice

Sacred text includes basmala as verse_0, but S82 is a whole-surah run and seed initiation begins at 82:1. Basmala is opening context only.

S82 rooted occurrence rows from the QAC export: 49 ayah-root rows.

Distinct S82 roots: 37.

Distinct accepted branch rows for those roots: 311.

Occurrence x branch seed universe, counting repeated roots at repeated ayah positions: 401 lexical singleton seed passes.

Audit nuance: the exported branch table contains two source-row series under normalized `ش ي ء`, one with B001-B009 and another with B001-B007. Both source-row series were tested. In the compact ledger below they are collapsed by functional branch image: divine willing at 82:8, "any thing" at 82:19, and the remaining duplicate remote rows terminated.

Attachment rows used: S82 rows only, especially the four initial `إذا` adverbial frames, passive subject frames in 82:3-4, the `ما قدمت وأخرت` shared object construction, the vocative/interrogative construction at 82:6, the sequenced relative clause in 82:7-8, the guardian-writing-knowing frame at 82:10-12, the paired `لفي` containment predicates at 82:13-14, the repeated `ما أدراك ما يوم الدين` construction at 82:17-18, and the final no-ownership clause at 82:19.

## Temporal Exposure Notes

The recitation first opens four conditional upheaval frames:

1. 82:1: sky above splits.
2. 82:2: stars scatter.
3. 82:3: seas are made to burst.
4. 82:4: graves are overturned/exposed.

The first closure is not yet a punishment scene but an epistemic disclosure: a self knows what it sent forward and left behind, 82:5. The next temporal turn addresses the human who was deceived with respect to the generous Lord, 82:6, then reactivates making, evening, balancing, imaging, willing, and composing, 82:7-8. This reorders the earlier cosmic disassembly: the one who composed the human also can uncompose the world and expose the record.

The second major turn is juridical and archival: denial of `الدين`, then guardians, noble writers, and knowledge of what is done, 82:9-12. The third turn fixes the outcome as two containments, `لفي نعيم` and `لفي جحيم`, then intensifies `يوم الدين` through exposure, non-absence, repeated incomprehension, and final transfer of all command/affair to Allah, 82:13-19.

## Candidate Synthesis Units

### S82-C01: Split-Open Cosmos To Exposed Interior

- `candidate_id`: S82-C01
- `ayah_range`: 82:1-5, reactivated by 82:9-19
- `seed_type`: lexical/constructional
- `seed`: 82:1 `ٱنفَطَرَتْ`, root `ف ط ر`, B001
- `generating_set`: `(E: ف ط ر B001 opening/splitting)`, `(E: س م و B004 what is above and overshadows)`, `(E: ن ث ر B001 scattering)`, `(E: ك و ك ب B001 stars)`, `(E: ب ح ر B001 wide water)`, `(E: ف ج ر B001 wide splitting and water bursting)`, `(E: ق ب ر B001 grave/deposit)`, `(E: ب ع ث ر B001 turning soil and exposing buried things)`, `(E: sequence 82:1->82:4 repeated إذا)`
- `selected_branches`: `ف ط ر B001`, `س م و B004`, `ن ث ر B001`, `ك و ك ب B001`, `ب ح ر B001`, `ف ج ر B001`, `ق ب ر B001`, `ب ع ث ر B001`
- `constructed_model`: the ordered scene begins at the highest cover, opens it, loosens fixed lights into scatter, ruptures the broad waters, then reaches the buried lower enclosure. The model is a vertical unsealing: above, middle, fluid boundary, buried interior.
- `freeze_point`: after 82:4, before 82:5 `عَلِمَتْ نَفْسٌ`.
- `predictions_at_freeze`: an exposed hidden content; a transition from physical opening to knowing; a subject whose interior/account becomes available; later language of record, custody, or judgment.
- `unused_features_tested`: 82:5 `علمت نفس`, `ما قدمت وأخرت`; 82:10-12 guardians/writers/knowing; 82:15-19 `يوم الدين`, non-absence, no ownership, `الأمر لله`.
- `corroborators`: `(C: ع ل م B001 disclosure to knower)`, `(C: ن ف س B012 self/very entity)`, `(C: ق د م B004 forward precedence)`, `(C: ء خ ر B002 delay/laterness)`, `(C: ح ف ظ B001 guarded custody)`, `(C: ك ت ب B002 written record)`, `(C: sequence 82:1-4 physical exposure -> 82:5 epistemic exposure)`
- `constraints`: `(K: no literal human opener named in 82:1-4; verbs are intransitive/passive or event-framed)`, `(K: the primary meaning remains eschatological cosmic upheaval, not a metaphor-only psychological scene)`
- `temporal_reactivation_notes`: `بعثرت` reactivates all earlier rupture verbs by making clear that the chain is not random destruction but progressive removal of covers until hidden deposits are exposed.
- `rival_models`: a generic catastrophe list; weaker because it does not predict 82:5's disclosure of the self's forward/late contents.
- `grade`: strong
- `grade_rationale`: specific lexical branches, exact sequence, repeated morphology, and an unused epistemic/archival continuation independently confirm the model.
- `source_queries_or_rows_used`: S82 qac_root_ayah rows for `س م و`, `ف ط ر`, `ك و ك ب`, `ن ث ر`, `ب ح ر`, `ف ج ر`, `ق ب ر`, `ب ع ث ر`; S82 attachment rows 1:a1-a2 through 4:a1-a2; S82 branch rows for listed roots.

### S82-C02: What Was Sent Forward And What Was Left Behind

- `candidate_id`: S82-C02
- `ayah_range`: 82:5, reactivated by 82:10-12 and 82:19
- `seed_type`: lexical
- `seed`: 82:5 `قَدَّمَتْ`, root `ق د م`, B004
- `generating_set`: `(E: ق د م B004 advance/precede)`, `(E: ء خ ر B002 delay to later time)`, `(E: ع ل م B001 knowing/disclosure)`, `(E: ن ف س B012 self/entity)`
- `selected_branches`: `ق د م B004`, `ء خ ر B002`, `ع ل م B001`, `ن ف س B012`; secondary lexical color from `ق د م B002` prior standing and `ء خ ر B001 last/laterness`
- `constructed_model`: a self is made to know a two-directional ledger: what it pushed ahead into the record and what it held back, delayed, or left trailing behind.
- `freeze_point`: after 82:5, before the human address in 82:6.
- `predictions_at_freeze`: a later accounting system; evidence that acts are preserved; a judgment day vocabulary; failure of self-protection or self-transfer at closure.
- `unused_features_tested`: 82:9 `الدين`; 82:10-12 guardians/writers/knowers; 82:15/17/18 `يوم الدين`; 82:19 no self owns anything for another self.
- `corroborators`: `(C: د ي ن B002 account/recompense)`, `(C: ح ف ظ B001 custody)`, `(C: ك ت ب B003 fixing a binding decree/record)`, `(C: ف ع ل B001 deeds done)`, `(C: م ل ك B002 possession/control denied)`, `(C: ن ف س repeated at 82:19)`
- `constraints`: `(K: ما is the shared object of قدمت and أخرت by attachment rows 5:a3 and 5:a5; the model must stay about known contents, not spatial travel only)`
- `temporal_reactivation_notes`: 82:19 reactivates 82:5 by repeating `نفس` twice and denying that any self can own/transfer any `شيء` for another self. The earlier self's record is individually exposed.
- `rival_models`: a purely chronological before/after reading; valid as primary but less explanatory of the later recording apparatus if isolated from ledger imagery.
- `grade`: strong
- `grade_rationale`: forward/later pairing is explicit, and later independent record/judgment/no-transfer material confirms the frozen predictions.
- `source_queries_or_rows_used`: S82 qac rows 5 and 19; attachment rows 5:a1-a5, 10:a1-a3, 12:a1-a2, 19:a1-a7; branch rows for `ق د م`, `ء خ ر`, `ع ل م`, `ن ف س`, `د ي ن`, `ح ف ظ`, `ك ت ب`, `ف ع ل`, `م ل ك`.

### S82-C03: Deception By Generosity Against The Maker

- `candidate_id`: S82-C03
- `ayah_range`: 82:6-8, reactivated by 82:10-19
- `seed_type`: lexical
- `seed`: 82:6 `غَرَّكَ`, root `غ ر ر`, B008
- `generating_set`: `(E: غ ر ر B008 deception by what gleams and does not hold)`, `(E: ر ب ب B001 lordship/ownership/mastery)`, `(E: ر ب ب B002 nurture, repair, completion over stages)`, `(E: ك ر م B001 honor/generosity)`, `(E: خ ل ق B002 creation/bringing into being)`, `(E: س و ي B002 straightening/completion)`, `(E: ع د ل B005 setting upright/balancing)`, `(E: ص و ر B003 form/image)`, `(E: ش ي ء B002 willing)`, `(E: ر ك ب B004 assembling parts in place)`
- `selected_branches`: `غ ر ر B008`, `ر ب ب B001/B002`, `ك ر م B001`, `خ ل ق B002`, `س و ي B002`, `ع د ل B005`, `ص و ر B003`, `ش ي ء B002`, `ر ك ب B004`
- `constructed_model`: the human misreads generosity as loosened accountability, even though the generous Lord is precisely the one who owned, nurtured, measured, balanced, imaged, willed, and assembled him.
- `freeze_point`: after 82:8, before 82:9 `كلا بل تكذبون بالدين`.
- `predictions_at_freeze`: denial of accounting; a return of honorable/generous language in another role; evidence that the one composed can be audited; agency belongs to the composer, not to the composed self.
- `unused_features_tested`: 82:9 denial of `الدين`; 82:10-11 `كراما كاتبين`; 82:12 knowledge of acts; 82:19 `الأمر يومئذ لله`.
- `corroborators`: `(C: ك ذ ب B002 denial/attribution of falsehood)`, `(C: د ي ن B002 account/recompense)`, `(C: ك ر م B001 repeated in كراما, honorable agents not indulgent excuse)`, `(C: ك ت ب B002 writing)`, `(C: ع ل م B001 knowing acts)`, `(C: ء م ر B001 affair and B003 authority at closure)`, `(C: ء ل ه B001 divine object of worship)`
- `constraints`: `(K: كريم is an adjective of ربك by attachment 6:a6; it does not independently mean permissiveness)`, `(K: غرك has an interrogative subject ما, so the deception source is questioned rather than directly named)`
- `temporal_reactivation_notes`: `كرام` at 82:11 reactivates `الكريم` at 82:6. Honor/generosity is not erased; it is relocated from the human's excuse to the dignity of the recording order.
- `rival_models`: "divine kindness should prevent judgment" is a defeated model inside the passage, not the surah's thesis.
- `grade`: strong
- `grade_rationale`: the construction uses a tight local chain and predicts the immediate denial/recording correction.
- `source_queries_or_rows_used`: S82 qac rows 6-12, 19; attachment rows 6:a3-a6, 7:a1-a8, 8:a1-a4, 9:a1, 10:a1-a3, 11 row from QAC export, 12:a1-a2, 19:a5-a7.

### S82-C04: Composition And Decomposition

- `candidate_id`: S82-C04
- `ayah_range`: 82:1-8
- `seed_type`: verified composite
- `seed`: 82:8 `رَكَّبَكَ`, root `ر ك ب`, B004
- `generating_set`: `(E: ر ك ب B004 placing parts in their locations)`, `(E: خ ل ق B001 measuring before making)`, `(E: خ ل ق B002 creating)`, `(E: خ ل ق B003 complete form)`, `(E: س و ي B002 straightening/completing)`, `(E: ع د ل B005 balancing/uprighting)`, `(E: ص و ر B003 form)`, `(E: ش ي ء B002 willing)`, with backward expansion to `(E: ف ط ر B001 split)`, `(E: ن ث ر B001 scatter)`, `(E: ف ج ر B001 burst)`, `(E: ب ع ث ر B001 overturn/expose)`
- `selected_branches`: creation-composition branches plus earlier disassembly branches.
- `constructed_model`: the passage juxtaposes the Maker's compositional authority over the human body with cosmic decompositional events. What was assembled by will can be opened, scattered, burst, and overturned by the same sovereignty.
- `freeze_point`: after 82:8, then backward replay to 82:1-4.
- `predictions_at_freeze`: earlier catastrophe verbs should read as controlled unmaking rather than chaos; later final authority should return to Allah.
- `unused_features_tested`: 82:19 `الأمر لله`; 82:10 guardians over the composed human; 82:12 acts done by the composed agent.
- `corroborators`: `(C: ء م ر B003 sovereignty/authority)`, `(C: ء ل ه B002 Allah named at closure)`, `(C: ح ف ظ B001 guardians over you)`, `(C: ف ع ل B001 your acts)`
- `constraints`: `(K: 82:7-8 refers directly to human formation; any cosmic-composition extension is secondary simulation generated by ordering, not primary translation)`
- `temporal_reactivation_notes`: only after `ركبك` does the first four ayat become strongly legible as uncomposition, not merely disaster.
- `rival_models`: a biological embryo/body-only model; medium as local, weaker for full-surah sequence unless it reactivates cosmic opening.
- `grade`: medium-strong
- `grade_rationale`: strong local lexical support and good backward reactivation, but the cosmic uncomposition bridge is relational rather than directly asserted.
- `source_queries_or_rows_used`: S82 qac rows 1-8 and 19; branch rows listed above.

### S82-C05: Denial Of The Accounting System Despite Active Custody

- `candidate_id`: S82-C05
- `ayah_range`: 82:9-12
- `seed_type`: constructional/lexical
- `seed`: 82:9 `تُكَذِّبُونَ بِٱلدِّينِ`, roots `ك ذ ب` B002 and `د ي ن` B002
- `generating_set`: `(E: ك ذ ب B002 treating/declaring false)`, `(E: د ي ن B002 account, judgment, recompense)`, `(E: ح ف ظ B001 guardianship)`, `(E: ك ر م B001 honorable dignity)`, `(E: ك ت ب B002 writing)`, `(E: ع ل م B001 knowing)`, `(E: ف ع ل B001 deeds)`
- `selected_branches`: `ك ذ ب B002`, `د ي ن B002`, `ح ف ظ B001`, `ك ر م B001`, `ك ت ب B002`, `ع ل م B001`, `ف ع ل B001`
- `constructed_model`: denial is answered not first by punishment imagery but by an already operating archive: over you are honorable guardians, writing, knowing what you do.
- `freeze_point`: after 82:12.
- `predictions_at_freeze`: later `يوم الدين` should become unavoidable; absence from outcome should be denied; final ownership should defeat evasion.
- `unused_features_tested`: 82:13-16 paired outcomes; 82:15,17,18 repeated `يوم الدين`; 82:16 no absence; 82:19 no ownership.
- `corroborators`: `(C: د ي ن B002 repeated three times after freeze)`, `(C: ص ل ي B003 meeting/entering fire)`, `(C: غ ي ب B001 absence/hiddenness denied)`, `(C: م ل ك B002 ownership denied)`, `(C: ء م ر B001 affair belongs to Allah)`
- `constraints`: `(K: حافظين and كاتبين are plural active participles; the model must be custodial/archival, not merely abstract memory)`, `(K: على in عليكم marks oversight over the addressees)`
- `temporal_reactivation_notes`: this section reactivates 82:5's self-knowledge as externally maintained record. The self knows because its deeds were already guarded and written.
- `rival_models`: denial as generic unbelief without account mechanics; weaker because it cannot explain the immediate guardian-writer detail.
- `grade`: strong
- `grade_rationale`: the local syntax and branch fit are exact, and later repetition of `يوم الدين` confirms the frozen account model.
- `source_queries_or_rows_used`: S82 qac rows 9-12, 15-19; attachments 9:a1, 10:a1-a3, 12:a1-a2, 15:a2-a3, 17:a3-a5, 18:a3-a5, 19:a1-a7.

### S82-C06: Two Containments: Bliss And Burning

- `candidate_id`: S82-C06
- `ayah_range`: 82:13-16
- `seed_type`: constructional
- `seed`: paired `إِنَّ ... لَفِي ...` constructions at 82:13-14
- `generating_set`: `(E: ب ر ر B002 broad righteousness/obedience)`, `(E: ن ع م B001 good state/benefaction)`, `(E: ف ج ر B004 breach/transgression)`, `(E: ج ح م B001 intense blazing fire)`, `(E: ص ل ي B003 meeting/entering fire)`, `(E: غ ي ب B001 absence/hiddenness)`
- `selected_branches`: `ب ر ر B002`, `ن ع م B001`, `ف ج ر B004`, `ج ح م B001`, `ص ل ي B003`, `غ ي ب B001`
- `constructed_model`: after the archive, persons are sorted into two enveloping states: the obedient in beneficent ease, the breachers in blazing heat, and the latter are not absent from it on the day of account.
- `freeze_point`: after 82:16.
- `predictions_at_freeze`: `يوم الدين` will be intensified; no intermediary possession/control can alter placement.
- `unused_features_tested`: repeated `ما أدراك ما يوم الدين`; final `لا تملك نفس لنفس شيئا`; `الأمر لله`.
- `corroborators`: `(C: ي و م B003 severe event/day)`, `(C: د ي ن B002 account/recompense)`, `(C: م ل ك B002 control/ownership negated)`, `(C: ء م ر B003 authority returned to Allah)`
- `constraints`: `(K: في is actual predicative containment by attachments 13:a2-a3 and 14:a2-a3; do not reduce نعيم/جحيم to mere labels)`, `(K: يصلونها applies to جحيم by feminine suffix, not to both groups)`
- `temporal_reactivation_notes`: `فجار` reactivates `فجرت`: the first bursting is cosmic water rupture; the later `فجار` is moral rupture. Same root, different branch roles, and the passage prevents collapsing them.
- `rival_models`: a water/fire elemental contrast using `بحار` and `جحيم`; possible secondary color but weak unless subordinated to the judgment containment.
- `grade`: strong
- `grade_rationale`: exact parallel syntax plus strong lexical opposition and later closure.
- `source_queries_or_rows_used`: qac rows 13-19; attachments 13:a1-a3, 14:a1-a3, 15:a1-a3, 16:a1-a3, 19:a1-a7.

### S82-C07: The Day Beyond Ordinary Knowing

- `candidate_id`: S82-C07
- `ayah_range`: 82:15-19
- `seed_type`: temporal/acoustic/constructional
- `seed`: repeated `وَمَا أَدْرَىٰكَ مَا يَوْمُ ٱلدِّينِ`, 82:17-18
- `generating_set`: `(E: د ر ي B001 knowing/daraya)`, `(E: ي و م B003 severe event/day)`, `(E: د ي ن B002 account/recompense)`, `(E: temporal repetition 82:17 then 82:18 with ثم)`
- `selected_branches`: `د ر ي B001`, `ي و م B003`, `د ي ن B002`
- `constructed_model`: the day of account is made cognitively inaccessible by repeated questioning, then defined not by description of scenery but by agency-collapse: no self owns anything for another self, and the affair belongs to Allah.
- `freeze_point`: after 82:18, before 82:19.
- `predictions_at_freeze`: final statement should resolve the unknown by naming control/ownership rather than adding a new image.
- `unused_features_tested`: 82:19 `لا تملك نفس لنفس شيئا`; `الأمر يومئذ لله`.
- `corroborators`: `(C: م ل ك B002 ownership/control)`, `(C: ن ف س B012 self repeated twice)`, `(C: ش ي ء B001 any thing)`, `(C: ء م ر B001 affair)`, `(C: ء ل ه B002 Allah named)`
- `constraints`: `(K: أدراك is not mere information delivery; the repeated construction delays definition until 82:19)`, `(K: يوم here is not ordinary daytime B001; B003 severe event fits better after repeated interrogation)`
- `temporal_reactivation_notes`: the repeated formula holds the question open, then 82:19 closes it. It also reactivates 82:5 `علمت نفس` by showing the self knows its own record but cannot own help or transfer for another self.
- `rival_models`: ordinary calendar-day reading; primary word allows day, but B003 better fits the surah's event intensity.
- `grade`: strong
- `grade_rationale`: repetition, lexical branch, and final closure converge.
- `source_queries_or_rows_used`: qac rows 15-19; attachments 17:a1-a5, 18:a1-a5, 19:a1-a7.

### S82-C08: Final Collapse Of Delegated Control

- `candidate_id`: S82-C08
- `ayah_range`: 82:19
- `seed_type`: lexical/constructional
- `seed`: 82:19 `لَا تَمْلِكُ نَفْسٌ لِنَفْسٍ شَيْئًا`
- `generating_set`: `(E: م ل ك B002 ownership/control)`, `(E: ن ف س B012 self/entity, repeated)`, `(E: ش ي ء B001 any thing)`, `(E: ء م ر B001 affair/matter)`, `(E: ء ل ه B002 Allah named)`, with possible `(E: ء م ر B003 authority/sovereignty)`
- `selected_branches`: `م ل ك B002`, `ن ف س B012`, `ش ي ء B001`, `ء م ر B001/B003`, `ء ل ه B002`
- `constructed_model`: the final day is defined as the negation of inter-self control and the concentration of the affair/command in Allah.
- `freeze_point`: final ayah; tested by backward replay.
- `predictions_at_freeze`: earlier claims of human selfhood, deception, record, and judgment should all converge on inability to control the account.
- `unused_features_tested`: backward replay to 82:5 `علمت نفس`, 82:6 human addressee, 82:8 divine willing, 82:9 denial, 82:10 oversight.
- `corroborators`: `(C: ن ف س at 82:5)`, `(C: ء ن س B001 human as visible person)`, `(C: ش ي ء B002 divine willing at 82:8 contrasts with no thing owned at 82:19)`, `(C: د ي ن B002 repeated account)`, `(C: ح ف ظ/K ت ب archival apparatus)`
- `constraints`: `(K: لام in لنفس marks beneficiary/concern complement by attachment 19:a3; do not make one self literally possessed by another)`, `(K: الأمر is singular collective affair, not every lexical branch of ء م ر)`
- `temporal_reactivation_notes`: `نفس` at 82:19 reactivates `نفس` at 82:5. The self first knows its ledger, then loses any claim to transfer, rescue, or control.
- `rival_models`: final command-only model without no-self clause; incomplete because the negated ownership construction is the immediate definition.
- `grade`: strong
- `grade_rationale`: exact syntax and multiple backward links.
- `source_queries_or_rows_used`: qac rows 5,8,19; attachment rows 19:a1-a7.

### S82-C09: Honor Reassigned From Excuse To Witness

- `candidate_id`: S82-C09
- `ayah_range`: 82:6 and 82:11
- `seed_type`: temporal/acoustic/lexical
- `seed`: repeated root `ك ر م`: `الكريم` and `كراما`
- `generating_set`: `(E: ك ر م B001 honor/generosity)`, `(E: غ ر ر B008 deception)`, `(E: ر ب ب B001/B002 Lord/master/nurturer)`, `(E: ح ف ظ B001 guardians)`, `(E: ك ت ب B002 writers)`
- `selected_branches`: `ك ر م B001`, with rejected `ك ر م B008 gift-for-return`, `B009 polite response`, `B004 grapevine`
- `constructed_model`: the human's question concerns deception by or with respect to the generous Lord; the next use of the same root marks the recorders as noble. Honor is not a loophole but the quality of the witnessing order.
- `freeze_point`: after 82:11.
- `predictions_at_freeze`: what follows should state what those honorable witnesses do.
- `unused_features_tested`: 82:12 `يعلمون ما تفعلون`.
- `corroborators`: `(C: ع ل م B001 knowing)`, `(C: ف ع ل B001 actions)`, `(C: attachment 12:a1 clausal content known)`
- `constraints`: `(K: كراما modifies كاتبين, not ربك; the reactivation is root-level and temporal, not syntactic identity)`
- `temporal_reactivation_notes`: hearing `كراما` after `الكريم` forces a backward re-evaluation of the mistaken inference from generosity.
- `rival_models`: generic adjective repetition; medium if taken alone, stronger inside C03/C05.
- `grade`: medium-strong
- `grade_rationale`: specific repeated root and sequence, but depends on C03/C05 to become more than stylistic echo.
- `source_queries_or_rows_used`: qac rows 6,11,12; attachments 6:a6 and 12:a1-a2.

### S82-C10: Root F-J-R Split Into Cosmic Rupture And Moral Breach

- `candidate_id`: S82-C10
- `ayah_range`: 82:3 and 82:14
- `seed_type`: lexical/temporal
- `seed`: repeated root `ف ج ر`: `فُجِّرَتْ` and `الفجار`
- `generating_set`: `(E: ف ج ر B001 wide splitting and water burst at 82:3)`, `(E: ف ج ر B004 moral breach/transgression at 82:14)`, `(E: ب ح ر B001 seas)`, `(E: ج ح م B001 fire)`
- `selected_branches`: `ف ج ر B001` for 82:3, `ف ج ر B004` for 82:14
- `constructed_model`: the root first opens a physical boundary in the seas, then names persons defined by moral boundary-breaking. The same root generates a non-identical but temporally reactivated image of breach.
- `freeze_point`: after 82:14.
- `predictions_at_freeze`: the moral breachers should be located in an outcome that answers boundary violation.
- `unused_features_tested`: 82:15-16 entering fire and not absent.
- `corroborators`: `(C: ص ل ي B003 entering/meeting fire)`, `(C: غ ي ب B001 absence denied)`, `(C: في containment)`
- `constraints`: `(K: do not make البحار morally transgressive; branch roles differ by occurrence)`, `(K: فجار are persons by morphology/noun pattern)`
- `temporal_reactivation_notes`: later `الفجار` reactivates earlier `فجرت` as a root echo without collapsing contexts.
- `rival_models`: water-fire contrast only; weaker without moral branch distinction.
- `grade`: medium-strong
- `grade_rationale`: exact repeated root and strong semantic fork, but the relation is reactivation rather than a single model.
- `source_queries_or_rows_used`: qac rows 3 and 14; branch rows for `ف ج ر`, `ب ح ر`, `ج ح م`, `ص ل ي`, `غ ي ب`.

### S82-C11: Knowing As Exposure, Record, And Human Inadequacy

- `candidate_id`: S82-C11
- `ayah_range`: 82:5, 82:12, 82:17-18
- `seed_type`: lexical/temporal
- `seed`: `ع ل م` at 82:5 and 82:12, then `د ر ي` at 82:17-18
- `generating_set`: `(E: ع ل م B001 knowing/disclosure)`, `(E: ك ت ب B002 writing)`, `(E: ح ف ظ B001 custody)`, `(E: د ر ي B001 knowing/daraya)`, `(E: repetition of ما أدراك)`
- `selected_branches`: `ع ل م B001`, `د ر ي B001`, `ك ت ب B002`, `ح ف ظ B001`
- `constructed_model`: the passage distinguishes exposed knowledge of the self's deeds and the guardians' knowledge from the addressee's inability to grasp the Day except by revelation of its final rule.
- `freeze_point`: after 82:18.
- `predictions_at_freeze`: final definition will come from divine authority, not human inference.
- `unused_features_tested`: 82:19 `الأمر لله`.
- `corroborators`: `(C: ء م ر B001/B003 affair/authority)`, `(C: ء ل ه B002 Allah)`
- `constraints`: `(K: علم and درى are not identical roots; the model must preserve difference between known deeds and incomprehensible Day)`
- `temporal_reactivation_notes`: `أدراك` twice reactivates `علمت نفس` by contrast: a self will know its deed-record, but "what makes you know" the Day requires final sovereign definition.
- `rival_models`: simple synonym chain of knowing; weaker because it misses the contrast.
- `grade`: medium-strong
- `grade_rationale`: clear temporal contrast and final resolution, though less image-rich than C01-C08.
- `source_queries_or_rows_used`: qac rows 5,12,17,18,19; attachments 5:a1-a5, 12:a1-a2, 17:a1-a5, 18:a1-a5, 19:a5-a7.

### S82-C12: The "Thing" Between Divine Will And Human Non-Possession

- `candidate_id`: S82-C12
- `ayah_range`: 82:8 and 82:19
- `seed_type`: lexical/temporal
- `seed`: root `ش ي ء`, `شاء` at 82:8 and `شيئا` at 82:19
- `generating_set`: `(E: ش ي ء B002 willing/mashi'a at 82:8)`, `(E: ر ك ب B004 assembling)`, `(E: ش ي ء B001 any thing at 82:19)`, `(E: م ل ك B002 ownership/control negated)`
- `selected_branches`: `ش ي ء B002`, `ش ي ء B001`, `ر ك ب B004`, `م ل ك B002`
- `constructed_model`: divine willing determines the human's composed form; at the end, no self owns any thing for another self. The same root-space moves from divine willing to negated creaturely control over any object.
- `freeze_point`: after 82:19 by backward replay.
- `predictions_at_freeze`: earlier composition by divine will should constrain all later self-claims.
- `unused_features_tested`: 82:6 deception, 82:9 denial, 82:10-12 record.
- `corroborators`: `(C: غ ر ر B008 deception)`, `(C: د ي ن B002 account)`, `(C: ح ف ظ B001 custody)`
- `constraints`: `(K: شاء and شيء are different forms/functions; link is root-level reactivation, not same syntactic role)`
- `temporal_reactivation_notes`: 82:19 makes 82:8 sharper: the willed and assembled creature cannot will/own any rescue-object for another self on that Day.
- `rival_models`: no meaningful link between `شاء` and `شيئا`; plausible as conservative control, but root recurrence supports at least a secondary reactivation.
- `grade`: medium
- `grade_rationale`: useful root-level temporal echo; morphology and syntax require caution.
- `source_queries_or_rows_used`: qac rows 8 and 19; branch rows for `ش ي ء`, `ر ك ب`, `م ل ك`.

### S82-C13: Weak Aquatic-Birth Interior Model

- `candidate_id`: S82-C13
- `ayah_range`: 82:3-8, weakly reactivated by 82:5 and 82:19
- `seed_type`: lexical
- `seed`: `ب ح ر B007` depth of womb/strong red blood or `ن ف س B005` childbirth
- `generating_set`: `(E: ب ح ر B007 depth of womb / intense red blood)`, `(E: ن ف س B005 birth/childbed blood)`, `(E: خ ل ق B002 creation)`, `(E: ص و ر B003 form)`, `(E: ر ك ب B004 composition)`
- `selected_branches`: weak fork using `ب ح ر B007`, `ن ف س B005`, `خ ل ق B002`, `ص و ر B003`, `ر ك ب B004`
- `constructed_model`: a remote physiological image could see seas bursting and human composition as secondary birth/interior imagery, with the self emerging to know its record.
- `freeze_point`: after constructing from 82:3 and 82:7-8.
- `predictions_at_freeze`: strong childbirth terms, mother/body roles, or explicit blood/interior support should appear.
- `unused_features_tested`: 82:5 self knows; 82:6 human; 82:19 self repeated.
- `corroborators`: `(C: ء ن س B001 human/person)`, `(C: ن ف س B012 self)`, very weakly `(C: خ ل ق B002 creation)`
- `constraints`: `(K: no mother, child, womb, blood, or birth syntax in the passage)`, `(K: البحار in 82:3 is plural seas as passive subject by attachment 3:a2)`, `(K: ن ف س contextual branch is self/entity, not childbirth)`
- `temporal_reactivation_notes`: this is an example of a remote lexical avalanche that should mostly terminate.
- `rival_models`: C01/C04 explain the same sequence with much less strain.
- `grade`: weak
- `grade_rationale`: branch material exists but passage-local roles are missing.
- `source_queries_or_rows_used`: branch rows `ب ح ر B007`, `ن ف س B005`, qac rows 3,5,6,7,8,19.

### S82-C14: Weak Weapon/Pointed-Command Model

- `candidate_id`: S82-C14
- `ayah_range`: 82:17-19
- `seed_type`: lexical
- `seed`: `ء م ر B011`, "setting a spearhead on a shaft"
- `generating_set`: `(E: ء م ر B011 spearhead/pointing a shaft)`, possible `(E: د ر ي B004 pointed comb/horn)`, possible `(E: د ر ي B005 training target)`
- `selected_branches`: `ء م ر B011`, `د ر ي B004/B005` as rival fork only
- `constructed_model`: a remote branch could imagine the final `الأمر` as a pointed, directed decisive force after the incomprehensible Day.
- `freeze_point`: after 82:19.
- `predictions_at_freeze`: weapons, shafts, strike targets, training, or direct martial roles.
- `unused_features_tested`: none support it locally.
- `corroborators`: none strong.
- `constraints`: `(K: الأمر in 82:19 is a nominal theological/juridical predicate, not a weapon event)`, `(K: no spear, shaft, wielder, target, strike, or combat construction)`, `(K: د ر ي in 82:17-18 is Form IV "made you know", not a pointed tool)`
- `temporal_reactivation_notes`: terminated avalanche.
- `rival_models`: C07/C08.
- `grade`: unlikely
- `grade_rationale`: branch is real but passage-local syntax defeats it.
- `source_queries_or_rows_used`: branch rows `ء م ر B011`, `د ر ي B004/B005`; attachment rows 17:a1-a5, 18:a1-a5, 19:a5-a7.

## Constructional And Morphosyntactic Seed Passes

1. `إذا` x4, 82:1-4: starts a temporal chain of triggered upheavals. Strongly supports C01 by repeated adverbial attachment to the event verbs.
2. Subject-event pairing in 82:1-4: sky/split, stars/scatter, seas/burst, graves/overturn. Strong for a covering-to-exposure sequence.
3. Passive morphology in 82:3-4: `فجرت`, `بعثرت` suppress agents and foreground event/subject transformation. Supports C01 and constrains literal human agency.
4. `علمت نفس ما قدمت وأخرت`, 82:5: explicit epistemic object is the paired forward/back content. Generates C02.
5. Vocative plus interrogative, 82:6: `يا أيها الإنسان ما غرك`. Generates the deception-address frame C03.
6. `بربك الكريم`, 82:6: prepositional complement and adjective. Supports C03 and C09; constrains reading `كريم` as free-floating indulgence.
7. Relative chain `الذي خلقك فسواك فعدلك`, 82:7: sequenced formative operations. Generates C04.
8. `في أي صورة ما شاء ركبك`, 82:8: form-location plus will plus assembly. Strong for C04 and C12.
9. `كلا بل تكذبون بالدين`, 82:9: discourse correction and denial object. Generates C05.
10. `وإن عليكم لحافظين`, 82:10: fronted `عليكم` and emphatic guardians. Supports oversight, not vague memory.
11. `كراما كاتبين`, 82:11: honorable-writing pair. Supports C05/C09.
12. `يعلمون ما تفعلون`, 82:12: recording becomes knowledge of acts. Supports C05/C11.
13. Paired `إن الأبرار لفي نعيم / وإن الفجار لفي جحيم`, 82:13-14: exact syntactic containment opposition. Generates C06.
14. `يصلونها يوم الدين`, 82:15: feminine object suffix returns to `جحيم`; time is `يوم الدين`. Supports C06/C07.
15. `وما هم عنها بغائبين`, 82:16: negated absence from the fire. Supports C06 and constrains escape readings.
16. Repeated `وما أدراك ما يوم الدين`, 82:17-18: delayed definition. Generates C07.
17. `ثم` before the second formula, 82:18: temporal intensification, not mere duplicate. Supports C07.
18. `يوم لا تملك نفس لنفس شيئا`, 82:19: final definition of the Day by no inter-self possession. Generates C08.
19. `والأمر يومئذ لله`, 82:19: final predication of the affair/command to Allah. Closes C07/C08 and reactivates C03/C04.

## Exhaustive Lexical Seed Ledger

Each accepted branch for each S82 root was initiated as a singleton seed. The ledger below records whether it became a generator/corroborator/constraint in a candidate or terminated. Repeated roots were rerun at each occurrence context: `ع ل م` at 82:5 and 82:12; `ك ر م` at 82:6 and 82:11; `ف ج ر` at 82:3 and 82:14; `د ي ن` at 82:9, 82:15, 82:17, 82:18; `ي و م` at 82:15, 82:17, 82:18, 82:19; `ن ف س` at 82:5 and 82:19; `ش ي ء` at 82:8 and 82:19.

- `س م و` 82:1: B001 C01 local elevation; B002 weak visible-high cue; B003 terminated; B004 E in C01; B005 terminated name branch; B006 terminated hunting; B007 terminated rivalry; B008 weak acoustic/status echo, terminated.
- `ف ط ر` 82:1: B001 E in C01/C04; B002 C in C04 as making counterpart; B004 terminated fasting; B005 terminated milking; B006 weak premature-making fork, constrained; B007 terminated tooth emergence; B008 terminated mushroom.
- `ك و ك ب` 82:2: B001 E in C01; B002 terminated bull simile; B003 weak white-sky color, local only; B004 terminated night droplets; B005 weak "mass of thing" local; B006 terminated garden light; B007 weak shine-metal, constrained; B008 C for scattering image but not primary.
- `ن ث ر` 82:2: B001 E in C01; B002 terminated nasal branch; B003 weak violent-fall image, constrained; B004 weak star-name echo; B005 terminated armor; B006 terminated childbirth.
- `ب ح ر` 82:3: B001 E in C01; B002 C for expansiveness; B003 weak broad split, C if unused for C01; B004 terminated salinity; B005 weak exposed-open-space corroborator; B006 terminated low waterland; B007 weak C13; B008 weak bewilderment, constrained; B009 terminated sea travel; B010 terminated accidental meeting; B011 terminated disease/thirst; B012 terminated medical crisis; B013 terminated large belly.
- `ف ج ر` 82:3 and 82:14: at 82:3 B001 E in C01/C10; B002 weak dawn image; B003 weak sudden-rush; B004 C/K as later moral branch in C10, not same occurrence; B005 terminated broad generosity; B006 terminated battle days. At 82:14 B004 E in C06/C10; B001 is backward root echo only; other branches terminated.
- `ق ب ر` 82:4: B001 E in C01; B002 C for hidden/depressed interior; B003 terminated bird; B004 terminated nose/ganger branch.
- `ب ع ث ر` 82:4: B001 E in C01; B002 C for scattered contents but less exact than grave exposure; B003 weak overturning-bottom-up, local corroborator.
- `ع ل م` 82:5 and 82:12: B001 E/C in C02/C05/C11; B002 C for sign/mark only if tied to record; B004 terminated lip cleft; B005 weak water gathering, terminated; B006 terminated hawk; B007 terminated hyena.
- `ن ف س` 82:5 and 82:19: B001 weak breath, terminated; B002 weak relief, constrained by judgment; B003 terminated evil eye; B004 weak life-blood, constrained; B005 weak C13 only; B006 terminated drink-breath; B007 terminated tanning; B008 terminated water; B009 weak opening/reactivation but not contextual; B010 weak value/competition; B011 C for living soul; B012 E/C in C02/C08; B013 C for inward contents; B014 weak moral force; B015 weak delay/space; B016 terminated gambling arrow.
- `ق د م` 82:5: B001 terminated foot; B002 C for prior standing/precedent; B003 weak pastness; B004 E in C02; B005 terminated travel arrival; B006 weak initiative, constrained; B007 C for front/forepart; B008 terminated adze; B009 terminated place; B010 weak "set toward" but not main.
- `ء خ ر` 82:5: B001 C later/other; B002 E in C02; B003 C rear/back, secondary image only.
- `ء ن س` 82:6: B001 E/C human visible person in C03/C08; B002 C perception/awareness, weak; B003 weak comfort/companionship, constrained by deception; B004 weak facing-side image; B005 terminated pupil image; B006 weak self/close-person echo.
- `غ ر ر` 82:6: B001 terminated crease; B002 weak pattern; B003 weak gleaming white; B004 weak nobility, rival with `كرم`; B005 weak beginning; B007 C gullibility; B008 E in C03; B009 C danger/unknown outcome; B010 weak deficiency; B011 terminated feeding/filling; B012 terminated blade edge; B013 terminated sack; B014 weak death-rattle, constrained.
- `ر ب ب` 82:6: B001 E in C03; B002 E in C03; B003 weak teacher/wisdom corroborator; B004 terminated crowds; B005 weak nurtured child local; B006 terminated thick syrup; B007 C abiding oversight; B008 weak cloud/rain; B009 weak newness; B010 terminated arrow-bag; B011 weak covenant; B012 terminated plant; B013 terminated abundant water; B014 terminated herd; B015 terminated particle; B016 weak blessing/need; B017 terminated sailors' chief.
- `ك ر م` 82:6 and 82:11: B001 E/C in C03/C09; B002 weak rain/plant quality; B003 terminated necklace; B004 terminated vine; B005 terminated lid; B006 weak boasting rivalry; B007 terminated thigh joint; B008 weak reward-seeking gift; B009 weak polite response; B010 C precious/honored.
- `خ ل ق` 82:7: B001 E in C04; B002 E in C03/C04; B003 E in C04; B004 weak inner disposition; B005 C fitted/prepared; B007 K against fabricated-denial link unless tied to `كذب`; B008 C smooth/even surface with `سوى`; B009 terminated worn cloth; B010 terminated perfume; B011 weak water-holding hollow; B012 weak closed solid, constrained.
- `س و ي` 82:7: B001 C equality/balance; B002 E in C03/C04; B003 weak rising/settling; B004 weak directed intention; B005 C completion/maturity; B006 C middle/just path; B007 terminated otherness; B008 weak directed speech; B009 weak broad smooth land; B010 terminated saddlecloth; B011 terminated omission; B012 terminated moon-night; B013 terminated head-equivalent.
- `ع د ل` 82:7: B001 C justice, reactivated by `دين`; B002 C equivalence; B003 weak ransom/value, reactivated by 82:19 no transfer; B004 weak balancing loads; B005 E in C03/C04; B006 K possible deviation branch but contextual verb is formative; B008 weak weighing alternatives.
- `ص و ر` 82:8: B001 weak turning/mal-disposition, constrained; B003 E in C03/C04; B004 terminated horn; B005 terminated palms; B006 terminated cattle herd; B007 terminated musk container; B008 terminated head itch; B009 terminated responsive sparrow; B010 terminated mouth corners.
- `ش ي ء` 82:8 and 82:19: at 82:8 B002/B001 E in C03/C12 as willing; B003 weak compelled-to; B004 K deformation branch; B005 weak attraction; B006 terminated listening; B007 terminated far-looking horse; B008 terminated small palms; B009 weak astonishment. At 82:19 B001 E in C08/C12; B002 backward divine-will contrast; rest terminated.
- `ر ك ب` 82:8: B001 weak riding; B002 C layering/stacking; B003 weak taking on an affair; B004 E in C03/C04/C12; B005 terminated knee; B006 terminated pubic place; B007 terminated plant shoot; B008 weak origin/stock; B009 terminated field strip; B010 terminated sheep back disease.
- `ك ذ ب` 82:9: B001 C falsehood; B002 E in C05; B003 terminated "stick to it"; B004 weak failed charge; B005 weak no-delay echo; B006 terminated milk failed; B007 terminated animal run-stop; B008 weak deceitful self; B009 terminated deceptive cloth.
- `د ي ن` 82:9,15,17,18: B001 C obedience; B002 E/C in C02/C05/C06/C07; B003 weak debt; B004 C subjection/ownership; B005 weak custom; B006 terminated city; B007 weak entrusting.
- `ح ف ظ` 82:10: B001 E in C05; B002 C memory/stability; B003 C continual observance; B004 C vigilance; B005 weak zeal/anger; B006 C keeping sanctities/covenant; B007 weak clear path.
- `ك ت ب` 82:11: B001 C joining/assembling record; B002 E in C05; B003 C binding decree; B004 C inscription in register; B005 terminated manumission contract.
- `ف ع ل` 82:12: B001 E in C05; B002 C quality of deed; B003 terminated laborers; B004 K fabricated act only if rival; B005 weak mutual doing; B006 terminated axe handle; B007 grammar-only.
- `ب ر ر` 82:13: B001 C truthful deed; B002 E in C06; B003 weak filial goodness; B004 terminated noise; B005 weak dry-land contrast to seas; B006 terminated wheat; B007 terminated arak fruit; B008 weak superiority.
- `ن ع م` 82:13: B001 E in C06; B002 C softness/ease; B003 weak praise; B004 terminated yes-answer; B005 terminated cattle; B006 terminated ostrich; B007 terminated ostrich-like objects; B008 weak scattering/flight but constrained; B009 weak soft wind; B010 weak increase; B011 C fitting place; B012 terminated walking; B013 C eye-delight.
- `ج ح م` 82:14: B001 E in C06; B002 C battle/death heat; B003 weak burning eyes; B004 weak face anger; B005 terminated shamelessness.
- `ص ل ي` 82:15: B001 terminated prayer; B002 weak prayer/blessing, constrained by object `ها`; B003 E in C06; B004 C fire-setting/roasting; B005 terminated traps; B006 weak back/tail childbirth branch, constrained; B007 weak following in race; B008 terminated worship places; B009 terminated pounding stone; B010 terminated plant.
- `غ ي ب` 82:16: B001 E in C06; B002 C low hidden place; B003 terminated thicket; B004 weak backbiting; B006 weak doubt; B007 terminated fat; B008 weak hidden roots; B009 C burial echo.
- `د ر ي` 82:17 and 82:18: B001 E in C07/C11; B002 weak seeking/aiming; B003 weak stalking; B004 K in C14; B005 K in C14; B006 weak gentleness.
- `ي و م` 82:15,17,18,19: B001 primary day but weak for event intensity; B002 C extended time; B003 E in C07 as severe event.
- `م ل ك` 82:19: B001 C firmness/control; B002 E in C08; B003 C sovereignty; B004 terminated marriage; B005 C support/hinge of affair; B006 weak road middle; B007 weak sustaining water; B008 weak leader; B009 possible angel homograph branch but not contextual here.
- `ء م ر` 82:19: B001 E in C08; B002 C command; B003 C authority/sovereignty; B004 weak abundance/blessing; B005 weak appointed time/sign; B006 weak terrible affair; B007 weak deliberation; B008 weak dependent opinion; B009 terminated lamb; B011 unlikely C14 weapon branch.
- `ء ل ه` 82:19: B001 C worshipped deity; B002 E/C proper divine naming at closure and opening-context echo.

## Image Packet Catalog

IMAGE_ID: S82-IP01
Starting seed: `ف ط ر B001` at 82:1
Complete image: vertical unsealing from sky to grave, ending in exposed self-knowledge.
Passage-order assembly: sky split -> stars scattered -> seas burst -> graves overturned -> self knows.
Participants and roles: upper cover, celestial fixed points, broad waters, buried deposits, self/account.
Operation / mechanism: opening, scattering, bursting, overturning, knowing.
Direction / force / medium: above to below, exterior covers to hidden interiors.
Temporal development: four `إذا` triggers followed by disclosure.
Outcome / closure: reactivated by record and final day.
Exact branch constituents: `س م و B004`, `ف ط ر B001`, `ك و ك ب B001`, `ن ث ر B001`, `ب ح ر B001`, `ف ج ر B001`, `ق ب ر B001`, `ب ع ث ر B001`, `ع ل م B001`.
Unfilled roles: physical agent intentionally omitted by passage.
Status: COMPLETE.

IMAGE_ID: S82-IP02
Starting seed: `ق د م B004` at 82:5
Complete image: ledger of forward and delayed contents disclosed to the self.
Passage-order assembly: self knows -> denial of account -> guardians write -> day of account -> no self-transfer.
Participants and roles: self, deeds/contents, recorders, day, Allah's affair.
Operation / mechanism: advance, delay, custody, writing, recompense, no possession.
Direction / force / medium: temporal forward/back plus juridical accounting.
Temporal development: 82:5 becomes fully legible at 82:10-19.
Outcome / closure: no self owns anything for another self.
Exact branch constituents: `ق د م B004`, `ء خ ر B002`, `ع ل م B001`, `ن ف س B012`, `د ي ن B002`, `ح ف ظ B001`, `ك ت ب B002`, `م ل ك B002`.
Unfilled roles: none.
Status: COMPLETE.

IMAGE_ID: S82-IP03
Starting seed: `غ ر ر B008` at 82:6
Complete image: deception by misread generosity corrected by maker/recorder sovereignty.
Passage-order assembly: human deceived -> Lord generous -> Lord made/evened/balanced/composed -> denial -> noble writers -> final command belongs to Allah.
Participants and roles: human, Lord, generosity, formative acts, recorders, final authority.
Operation / mechanism: deceptive inference, formation, archival correction, sovereignty.
Direction / force / medium: from mistaken human inference to divine command.
Temporal development: `الكريم` reactivated by `كراما`.
Outcome / closure: generosity does not cancel account.
Exact branch constituents: `غ ر ر B008`, `ر ب ب B001/B002`, `ك ر م B001`, `خ ل ق B002`, `س و ي B002`, `ع د ل B005`, `ص و ر B003`, `ر ك ب B004`.
Unfilled roles: source of deception remains interrogative, not named.
Status: COMPLETE.

IMAGE_ID: S82-IP04
Starting seed: paired `لفي`
Complete image: two final containments.
Passage-order assembly: record -> righteous in bliss -> transgressors in fire -> they enter it on day of account -> not absent.
Participants and roles: righteous, breachers, bliss, blaze, day, absence denied.
Operation / mechanism: sorting into containing states.
Direction / force / medium: inward containment.
Temporal development: outcome follows archive.
Outcome / closure: intensified by repeated `يوم الدين`.
Exact branch constituents: `ب ر ر B002`, `ن ع م B001`, `ف ج ر B004`, `ج ح م B001`, `ص ل ي B003`, `غ ي ب B001`.
Unfilled roles: none.
Status: COMPLETE.

IMAGE_ID: S82-IP05
Starting seed: repeated `ما أدراك ما يوم الدين`
Complete image: incomprehensible day defined by agency collapse and Allah's sole affair.
Passage-order assembly: enter fire on day -> no absence -> what makes you know? -> repeated -> no self owns for another -> affair belongs to Allah.
Participants and roles: addressee, day, selves, any thing, affair, Allah.
Operation / mechanism: delayed definition, negated intercession/control, final predication.
Direction / force / medium: from question to closure.
Temporal development: repetition with `ثم` intensifies and postpones.
Outcome / closure: `والأمر يومئذ لله`.
Exact branch constituents: `د ر ي B001`, `ي و م B003`, `د ي ن B002`, `م ل ك B002`, `ن ف س B012`, `ش ي ء B001`, `ء م ر B001/B003`, `ء ل ه B002`.
Unfilled roles: none.
Status: COMPLETE.

## Short Interpretation

S82's strongest latent structure is not merely "cosmic destruction followed by judgment." It is an ordered exposure-and-accounting system. Covers split, fixed lights scatter, waters burst, graves are overturned, and then the self knows its advanced and delayed contents. The human's deception is corrected by remembering that the generous Lord is also the one who formed and composed him. Denial of account is answered by guardians who write and know deeds. The outcome becomes two containments, and the repeated question about the Day closes with the negation of all inter-self control and the return of the affair to Allah.
