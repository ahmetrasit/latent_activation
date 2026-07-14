# Stage 1 Pass 2: S90 temporally conditioned reactivation

Assigned passage: S90, verses 1-20. Basmala is opening-context only.

## Root cause of Pass 1 limitation

Pass 1 was limited because the SQLite resources named in the Stage 1 prompt, `resources/qac.sqlite` and `resources/furuq_v4.sqlite`, are zero-byte files in this checkout. That prevented normal schema inspection and direct SQL retrieval of QAC morphemes and v4 branch dossiers. I therefore under-used the full branch seed universe during Pass 1. For this restart I used the sacred Arabic text, the S90 rows of `resources/attachments.tsv`, and the local TSV mirrors already present in `resources/`: `qac_root_ayah.tsv` for rooted word inventory and `v4_branches.tsv` for uncontaminated accepted branch images. This restores the intended sweep: every accepted branch of every S90 root is accounted for.

## Rooted occurrence inventory

Verse order rooted words, excluding basmala seeds:

90:1 `ق س م`, `ب ل د`; 90:2 `ح ل ل`, `ب ل د`; 90:3 `و ل د`, `و ل د`; 90:4 `خ ل ق`, `ء ن س`, `ك ب د`; 90:5 `ح س ب`, `ق د ر`, `ء ح د`; 90:6 `ق و ل`, `ه ل ك`, `م و ل`, `ل ب د`; 90:7 `ح س ب`, `ر ء ي`, `ء ح د`; 90:8 `ج ع ل`, `ع ي ن`; 90:9 `ل س ن`, `ش ف ه`; 90:10 `ه د ي`, `ن ج د`; 90:11 `ق ح م`, `ع ق ب`; 90:12 `د ر ي`, `ع ق ب`; 90:13 `ف ك ك`, `ر ق ب`; 90:14 `ط ع م`, `ي و م`, `س غ ب`; 90:15 `ي ت م`, `ق ر ب`; 90:16 `س ك ن`, `ت ر ب`; 90:17 `ك و ن`, `ء م ن`, `و ص ي`, `ص ب ر`, `و ص ي`, `ر ح م`; 90:18 `ص ح ب`, `ي م ن`; 90:19 `ك ف ر`, `ء ي ي`, `ص ح ب`, `ش ء م`; 90:20 `ن و ر`, `و ص د`.

Total distinct roots: 44. Total accepted branch seeds swept from the local v4 mirror: 389.

## All-branch seed coverage ledger

Outcome codes: `C1` city/oath/closed-domain, `C2` created-human-kabad, `C3` false calculation/accountability, `C4` speech/wealth/waste, `C5` instruments/two-paths, `C6` steep-pass/freeing, `C7` famine-care, `C8` counsel/patience/mercy, `C9` right-left companions, `C10` sealed fire closure, `L` retained local or weak local image, `T` terminated as no passage-local complement.

- `ء ح د`: B001 L, B002 C3, B003 T, B004 L, B005 C3, B006 T.
- `ء م ن`: B001 C8, B002 C8, B003 L opening-prayer resonance only, no lexical seed success in S90.
- `ء ن س`: B001 C2, B002 C3/C5, B003 C8 weak corroborator, B004 L, B005 C5 weak eye resonance, B006 L.
- `ء ي ي`: B001 L, B002 C9, B003 C9, B004 L, B005 T, B006 T, B007 T, B008 T, B009 L, B010 C1 weak oath resonance.
- `ب ل د`: B001 C1, B002 C2 weak body-center fork, B003 C5 weak face/vision fork, B004 T, B005 C3 weak bewilderment, B006 C2 weak bodily mark, B007 T, B008 T, B009 C1, B010 C1 weak ground-contact, B011 T, B012 T.
- `ت ر ب`: B001 C7, B002 C7, B003 C4 rival, B004 L, B005 C2 weak chest/body fork, B006 L, B007 T, B008 T, B009 T.
- `ج ع ل`: B001 C5, B002 C5, B004 L, B005 T, B006 T, B007 T, B008 T, B009 T, B010 T, B011 T, B012 T.
- `ح س ب`: B001 C3, B002 C3, B003 C3 rival sufficiency, B004 C4 weak boast lineage, B006 C3, B008 T, B009 T, B010 C3.
- `ح ل ل`: B001 C6/C10 weak untying contrast, B002 C1, B003 C1, B004 C10 weak liability, B005 C1 weak oath, B006 C1 weak dwelling, B007 T, B008 T, B009 T, B010 T, B011 L, B012 T, B013 T, B014 T, B015 T.
- `خ ل ق`: B001 C2, B002 C2, B003 C2/C5, B004 C2, B005 C2/C6 weak aptitude, B007 C4 weak fabricated speech, B008 L, B009 L, B010 T, B011 L, B012 C10 weak sealed/solid contrast.
- `د ر ي`: B001 C6, B002 C6 weak directed knowing, B003 T, B004 C6 weak sharp-point/edge fork.
- `ر ء ي`: B001 C3/C5, B002 C3, B003 T, B004 C3 weak confrontation, B005 C4, B006 C5, B007 T, B008 T, B009 T, B010 T, B011 C9 weak sign/flag, B012 C3, B013 C6.
- `ر ح م`: B001 C8, B002 C7/C8, B003 C2/C7 opening-context corroborator through birth/kinship, B004 C2 weak birth-pain echo.
- `ر ق ب`: B001 C3/C6, B002 C6, B003 C3 weak lookout, B004 C6, B005 L, B006 T, B007 T, B008 C7 weak child-loss, B009 L, B010 T, B011 T, B012 L, B013 T, B014 T, B015 C9 weak last/following.
- `س غ ب`: B001 C7.
- `س ك ن`: B001 C7, B002 C7 weak home-loss contrast, B003 L, B004 C8 weak solace, B006 C7, B007 T, B008 T, B009 C7, B010 C7 weak subsistence.
- `ش ء م`: B001 C9, B002 T, B003 C9.
- `ش ف ه`: B001 C5, B002 C5/C8 weak face-to-face counsel, B003 C4 rival asking/claim, B004 T.
- `ص ب ر`: B001 C8, B002 L, B003 C8, B004 C6 weak top/edge, B005 C6 weak stony terrain, B006 C6/C8, B007 L, B008 L, B009 T, B010 L, B011 C7 weak food pile contrast, B012 T, B016 T, B017 C6 weak mountain-center, B018 C10 weak stopper/closure.
- `ص ح ب`: B001 C9, B002 C9, B003 L, B004 C9, B005 C2 weak maturity, B006 T, B007 T, B008 T.
- `ط ع م`: B001 C7, B002 C7, B004 C7, B005 L, B006 T, B007 T, B008 L, B009 T, B010 C6 weak graft/connection, B011 C6 weak capacity, B012 T, B013 C5 weak mouth, B014 C2 weak succession.
- `ع ق ب`: B001 L, B002 C6, B003 C6, B004 C2/C7 weak offspring, B005 C6/C9, B006 C6/C10, B007 C10 weak consequence, B008 C6, B009 C6, B010 L, B011 C6, B012 C6, B013 T, B014 T, B015 L.
- `ع ي ن`: B001 C5, B002 C3/C5, B003 C3/C5, B004 T, B005 C3 weak surveillance, B006 C7 weak water source, B007 T, B008 C5 weak illumination, B009 L, B010 L, B011 C4 weak present cash, B012 C4 weak loan, B013 C3, B014 L, B015 L, B016 T, B017 C3.
- `ف ك ك`: B001 C6, B002 C6, B003 L, B004 C5 weak jaw/mouth, B005 C6, B006 T, B007 T, B008 T, B009 T.
- `ق ح م`: B001 C6, B002 C6, B003 C7 weak drought, B004 L, B005 L, B006 C6, B007 C3 weak eye-measure.
- `ق د ر`: B001 C3, B003 C3, B004 C3/C7, B005 C3/C5, B006 C2/C3, B007 T.
- `ق ر ب`: B001 C7, B002 L, B003 C7/C8, B004 L, B005 L, B007 C7, B008 C7 weak water-seeking, B009 C7 weak water-vessel, B010 T, B011 T, B012 C2 weak birth-nearness, B013 T, B014 T, B015 T, B016 C3 weak measured closeness.
- `ق س م`: B001 C5 weak facial distribution, B002 L, B003 C1/C9, B004 C1, B006 C3 weak divided options, B007 T, B008 L.
- `ق و ل`: B001 C4/C8, B002 C5, B003 C4, B004 C4 weak authority, B005 C4, B006 C4, B007 C8 weak circulating speech, B008 T, B009 C8, B010 T, B011 C3, B012 C4, B013 C8, B014 C9 weak sign-speech, B015 C8, B016 C9 weak definition.
- `ك ب د`: B001 C2, B002 C2, B003 C2, B004 C2 weak bent arc, B005 L, B006 C2, B007 C4/C9 weak hostility, B008 C6 weak journey.
- `ك ف ر`: B001 C9, B002 C9/C10, B003 C9, B004 C9, B005 L, B006 C9, B007 L, B008 C2/C9 weak burial/covering seed, B009 L, B010 L, B011 T, B012 C1 weak remote place, B013 C6 weak covered pass, B014 L, B015 T.
- `ك و ن`: B001 C8, B002 C8, B003 C8 weak standing-with, B004 L, B005 T, B006 L.
- `ل ب د`: B001 C4, B002 C4, B003 C4/C1 weak sticking, B004 T, B005 T, B006 T, B007 C7 rival no-possession, B008 T.
- `ل س ن`: B001 C5, B002 C4/C8, B003 C5/C8, B004 C5 weak tongue-shape, B005 C5 weak speech-cut contrast, B006 C8/C9, B007 T, B008 C8, B009 T.
- `م و ل`: B001 C4/C7.
- `ن ج د`: B001 C5/C6, B002 C5, B003 C6, B004 C6, B005 C6/C7, B006 C6, B008 T, B009 T, B010 C6, B011 T, B012 L.
- `ن و ر`: B001 C9/C10 weak light contrast, B002 C10, B004 T, B005 C9 weak visible marker, B006 C9 weak flight, B007 C10, B008 C10 weak smoke, B009 T.
- `ه د ي`: B001 C5, B002 C5, B003 C5, B004 C8 weak gift, B005 C1 weak sanctuary gift, B006 T, B007 C6 weak protected captive, B008 C6 weak dependent walking, B009 L, B010 C8, B011 T.
- `ه ل ك`: B001 C4, B002 C4/C6 rival, B003 T, B004 C7, B005 C7, B006 C6, B007 T, B008 L, B009 C4, B010 C4/C6, B011 C4, B012 C4/C7.
- `و ص د`: B001 C10, B002 C10/C1, B003 C10 weak stone enclosure, B004 T.
- `و ص ي`: B001 C8, B002 C8, B003 C8, B004 C7/C8 weak pasture-fit.
- `و ل د`: B001 C2/C7, B002 C2/C7, B003 C2, B004 C7, B005 C2, B006 L.
- `ي ت م`: B001 C7, B002 C7, B003 L, B004 C7, B005 L.
- `ي م ن`: B001 C9, B002 C9, B003 C1 weak oath echo, B004 C3/C9, B005 T, B007 C10 weak death-side.
- `ي و م`: B001 C7, B002 C7, B003 C7.

## Detailed candidate synthesis units

### C1: Oath over a bounded inhabited domain that becomes a liability-domain

- `candidate_id`: S90-C1
- `ayah_range`: 90:1-2, reactivated at 90:18-20
- `seed_type`: lexical/constructional
- `seed`: 90:1 `أقسم` from `ق س م B004` oath, plus 90:1-2 repeated `بهذا البلد`
- `generating_set`: `(E: ق س م B004 oath)`, `(E: ب ل د B001 bounded place)`, `(E: ب ل د B009 residence/remaining in place)`, `(E: ح ل ل B002 settling in a place)`, `(E: ح ل ل B003 lawful/unrestricted state)`
- `selected_branches`: `ق س م B004`; `ب ل د B001/B009`; `ح ل ل B002/B003`; later `و ص د B001`, `ن و ر B002`, `ك ف ر B001/B003`, `ي م ن B002`, `ش ء م B001`
- `constructed_model`: The recitation opens by binding attention to a specific bounded place. The addressed person is not abstractly present; he is `حل` in that same bounded place. The place functions as a witnessed domain where residence, permissibility, and exposure are activated before the human struggle is named.
- `freeze_point`: after 90:2
- `predictions_at_freeze`: expected internal human condition inside the domain; expected later sorting or judgment of inhabitants; expected reactivation of place/boundary at closure; possible contrast between permitted presence and barred/closed fate.
- `unused_features_tested`: creation in `كبد`, repeated calculation questions, two paths, right/left companions, `عليهم نار مؤصدة`.
- `corroborators`: `(C: ك ب د B002 struggle occurs inside created human condition)`, `(C: ن ج د B001 two elevated paths within the life-domain)`, `(C: ص ح ب B001 companions/members of final sides)`, `(C: ي م ن B002 right side)`, `(C: ش ء م B001 left side)`, `(C: و ص د B001 sealed closure)`, `(C: attachment rows 90:1-2 same demonstrative+balad repetition)`.
- `constraints`: `(K: البلد is the oath object and demonstrative domain, not itself the whole moral content)`, `(K: حل has several branches; only residence/permissibility fit the syntax "أنت حل بهذا البلد")`, `(K: no explicit lexical branch makes the city equal the fire; closure is structural reactivation, not translation)`.
- `temporal_reactivation_notes`: 90:1-2 activates place and lawful presence. 90:20 reverses openness into closedness over a group: `عليهم نار مؤصدة`. The first bounded domain is reactivated by the final sealed domain.
- `rival_models`: `ب ل د B002` chest/body-center can weakly link to created human interior, but it is secondary; `ق س م B003` division can foreshadow right/left sorting, but oath is primary in context.
- `grade`: medium-strong
- `grade_rationale`: Strong sequence and attachment support; lexical support is specific for bounded place and closure, but the city-to-fire reactivation remains structural rather than direct lexical identity.
- `source_queries_or_rows_used`: S90 sacred text; S90 attachment rows 90:1-2 and 90:20; branch rows named above.

### C2: Human emergence into central hardship

- `candidate_id`: S90-C2
- `ayah_range`: 90:3-4, reactivated at 90:13-17
- `seed_type`: lexical
- `seed`: 90:3 `والد وما ولد`, root `و ل د B003` birth/bringing forth
- `generating_set`: `(E: و ل د B002 parent)`, `(E: و ل د B003 childbirth)`, `(E: و ل د B001 offspring)`, `(E: خ ل ق B001 measured forming)`, `(E: خ ل ق B002 bringing into existence)`, `(E: ء ن س B001 visible human kind)`, `(E: ك ب د B002 hardship/mukabada)`, `(E: ك ب د B003 middle/core)`, `(E: فِي attachment 90:4 containment)`
- `selected_branches`: `و ل د B001/B002/B003/B005`; `خ ل ق B001/B002/B003/B004`; `ء ن س B001/B003`; `ك ب د B001/B002/B003/B006`; later `ر ح م B003/B004`, `ي ت م B001`, `ق ر ب B003`
- `constructed_model`: The oath over parent and born thing opens a generational channel. The answer is that the human is measured and brought forth into `كبد`: not just external difficulty, but a central, embodied, interior condition of strain.
- `freeze_point`: after 90:4
- `predictions_at_freeze`: expected later child/kin vulnerability; expected bodily instruments; expected mercy or womb/kin reactivation; expected hardship-specific relief acts.
- `unused_features_tested`: eyes/tongue/lips, freeing a neck, feeding an orphan near of kin, mercy counsel.
- `corroborators`: `(C: ع ي ن B001 eyes as made organs)`, `(C: ل س ن B001 tongue as speech organ)`, `(C: ش ف ه B001 lips)`, `(C: ي ت م B001 child cut off from protector)`, `(C: ق ر ب B003 kinship)`, `(C: ر ح م B002 kinship)`, `(C: ر ح م B003 womb opening-context and passage-local mercy root)`, `(C: basmala ر ح م opening-context for mercy, not seed)`.
- `constraints`: `(K: كبد is not reduced to childbirth; childbirth supports the embodied/generational opening, while 90:4 states the general human condition)`, `(K: والِد وما ولد is oath content, not a narrative parent-child episode)`.
- `temporal_reactivation_notes`: Birth language precedes created-human hardship, then reappears as orphan/kin/mercy repair. The social care commands do not arrive cold; they answer the generational vulnerability opened in 90:3.
- `rival_models`: `ب ل د B002` chest and `ت ر ب B005` chest can thicken body imagery, but they are weak because not locally selected by surface words. `خ ل ق B007` fabricated speech belongs better under C4.
- `grade`: strong
- `grade_rationale`: Multiple independent channels converge: birth oath, creation clause, `في` containment, `كبد` hardship/core, body instruments, orphan/kin/mercy repair.
- `source_queries_or_rows_used`: S90 attachment row 90:4 direct object and `في كبد`; branch rows named above.

### C3: False calculation under unseen capacity and sight

- `candidate_id`: S90-C3
- `ayah_range`: 90:5-7, reactivated at 90:8-10 and 90:19
- `seed_type`: morphosyntactic/lexical
- `seed`: repeated interrogative `أيحسب` at 90:5 and 90:7
- `generating_set`: `(E: ح س ب B002 supposition)`, `(E: ح س ب B001 counting/accounting)`, `(E: ق د ر B003 capacity/power)`, `(E: ق د ر B001 measure/limit)`, `(E: ء ح د B002 exhaustive "anyone" in negation)`, `(E: ر ء ي B001 seeing)`, `(E: ر ء ي B012 making seen/showing)`
- `selected_branches`: `ح س ب B001/B002/B006/B010`; `ق د ر B001/B003/B004/B005/B006`; `ء ح د B001/B002/B005`; `ر ء ي B001/B002/B012/B013`; later `ع ي ن B001/B003/B005/B013/B017`, `ء ي ي B003`
- `constructed_model`: The subject is not merely ignorant; he performs a defective internal calculation: no one can have power over him, no one saw him. The next verses answer by exposing already-given instruments of sight, speech, and guidance.
- `freeze_point`: after 90:7
- `predictions_at_freeze`: expected correction through perception, signs, or evidentiary faculties; expected exposure of hidden boast; expected limitation of self-estimated power.
- `unused_features_tested`: made eyes, tongue/lips, two paths, signs denied in 90:19.
- `corroborators`: `(C: ع ي ن B001 eye)`, `(C: ع ي ن B003 eye as care/watch)`, `(C: ع ي ن B013 the thing itself, present before one)`, `(C: ل س ن B003 articulate evidence)`, `(C: ه د ي B001 guidance to path)`, `(C: ء ي ي B003 visible sign)`, `(C: ك ف ر B003 covering truth)`, `(C: attachment rows 90:5 and 90:7 repeated clausal complement under أيحسب)`.
- `constraints`: `(K: أحد at 90:5 and 90:7 is delayed subject, not an abstract deity label by branch B001 alone)`, `(K: the passage does not say he denies eyes; eyes answer the assumption by reactivating sight)`.
- `temporal_reactivation_notes`: The first `أيحسب` predicts a power-test; the second predicts a visibility-test. 90:8 immediately backfills the visibility-test with `عينين`, then 90:19 names denial of signs.
- `rival_models`: `ح س ب B003` sufficiency creates a rival "he deems himself enough" model; it is plausible but secondary because the syntax directly supplies `أن لن يقدر` and `أن لم يره`.
- `grade`: strong
- `grade_rationale`: Repetition, syntax, branch fit, and immediate body-instrument answer make this one of the most stable units.
- `source_queries_or_rows_used`: attachment rows 90:5, 90:7, 90:8; branch rows named above.

### C4: Boastful speech consumes heaped wealth

- `candidate_id`: S90-C4
- `ayah_range`: 90:6, constrained by 90:13-16
- `seed_type`: lexical
- `seed`: 90:6 quoted utterance `أهلكت مالا لبدا`
- `generating_set`: `(E: ق و ل B001 uttered speech)`, `(E: ق و ل B012 saying held in self/inner speech)`, `(E: ه ل ك B001 ruin/finitude)`, `(E: ه ل ك B009 exhausting effort)`, `(E: م و ل B001 acquiring/possessing wealth)`, `(E: ل ب د B002 heaped accumulation)`, `(E: ل ب د B001 matter piled layer on layer)`
- `selected_branches`: `ق و ل B001/B003/B005/B006/B012/B013`; `ه ل ك B001/B002/B009/B010/B011/B012`; `م و ل B001`; `ل ب د B001/B002/B003`; later `ط ع م B002`, `ف ك ك B002`
- `constructed_model`: A voice claims expenditure as self-display: "I destroyed/spent heaped wealth." The heap image is thick and static; the later commanded acts redirect wealth from boastful depletion into freeing a constrained person and feeding a hungry person.
- `freeze_point`: after 90:6
- `predictions_at_freeze`: expected correction between waste and useful expenditure; expected recipient roles; expected anti-heap movement from accumulation into release/distribution.
- `unused_features_tested`: freeing neck, feeding, orphan, poor person stuck to dust, mutual counsel.
- `corroborators`: `(C: ف ك ك B002 release from bondage/closed pledge)`, `(C: ط ع م B002 feeding another)`, `(C: س غ ب B001 hunger with fatigue)`, `(C: ت ر ب B002 poverty stuck to dust)`, `(C: ل س ن B002 being taken by tongue, weak speech constraint)`.
- `constraints`: `(K: أهلكت can mean destructive/spent depletion here but must remain a quoted boast, not divine judgment)`, `(K: مالا لبدا is direct object plus adjective; no lexical evidence for a literal wool/felt pile beyond secondary heap simulation)`.
- `temporal_reactivation_notes`: The quoted self-account is followed by sight/accountability and then by specific costly acts. The recitation shifts from "I spent heaps" to "he did not storm the steep pass," then defines actual expenditure.
- `rival_models`: `ل ب د B003` sticking to place can support stuckness, but `ت ر ب B002` and `س ك ن B006` better supply poverty/stillness later.
- `grade`: medium-strong
- `grade_rationale`: Lexical links are specific and the passage provides a strong expenditure contrast, though the candidate explains a local subsystem more than the entire surah.
- `source_queries_or_rows_used`: attachment row 90:6 quote/direct object/adjective; branch rows named above.

### C5: Given instruments and shown two elevated ways

- `candidate_id`: S90-C5
- `ayah_range`: 90:8-10
- `seed_type`: verified composite
- `seed`: 90:8-10 list `عينين`, `لسانا`, `شفتين`, `النجدين`
- `generating_set`: `(E: ج ع ل B001 making)`, `(E: ج ع ل B002 making something into a state)`, `(E: ع ي ن B001 seeing eye)`, `(E: ع ي ن B002 direct witnessing)`, `(E: ل س ن B001 tongue as speech organ)`, `(E: ل س ن B003 eloquence/articulation)`, `(E: ش ف ه B001 lips)`, `(E: ه د ي B001 gentle guidance to path/truth)`, `(E: ن ج د B001 elevated path)`, `(E: ن ج د B002 clarity/manifestness)`
- `selected_branches`: `ج ع ل B001/B002`; `ع ي ن B001/B002/B003/B013`; `ل س ن B001/B003/B006/B008`; `ش ف ه B001/B002`; `ه د ي B001/B002/B003`; `ن ج د B001/B002/B003/B005/B006`
- `constructed_model`: The human who miscalculates is confronted with endowed faculties: sight, speech apparatus, and guidance to two raised/clear ways. The model has perception, articulation, and directed choice.
- `freeze_point`: after 90:10
- `predictions_at_freeze`: expected a choice requiring effort; expected speech to become counsel; expected polarity in outcome.
- `unused_features_tested`: steep pass, mutual counsel, right/left companions.
- `corroborators`: `(C: ق ح م B001 entering hardship without hesitation)`, `(C: ع ق ب B012 difficult rising pass)`, `(C: و ص ي B003 reciprocal counsel)`, `(C: ي م ن B002 right side)`, `(C: ش ء م B001 left side)`, `(C: attachment rows 90:8-10 object list and explicit second object/path complement)`.
- `constraints`: `(K: النجدين is tagged in the TSV as root ن ج د despite one attachment row typo; use branch dossier root ن ج د)`, `(K: the two ways are not merely anatomical; body list prepares accountable path-choice)`.
- `temporal_reactivation_notes`: After two `أيحسب` questions, `ألم نجعل` reactivates the claim of unseen/unpowered accountability by listing the very faculties that make accountability possible.
- `rival_models`: `ع ي ن B006` water source can pair with famine, but it is not generated by `عينين` in 90:8; retain only as weak later resonance.
- `grade`: strong
- `grade_rationale`: Dense local syntax, direct sequence answer, and later path/outcome polarity all converge.
- `source_queries_or_rows_used`: attachment rows 90:8-10; branch rows named above.

### C6: Storming the steep pass as release from constriction

- `candidate_id`: S90-C6
- `ayah_range`: 90:11-13
- `seed_type`: constructional/lexical
- `seed`: 90:11 `فلا اقتحم العقبة`
- `generating_set`: `(E: ق ح م B001 plunging into hardship)`, `(E: ق ح م B002 perilous difficult road)`, `(E: ع ق ب B012 difficult raised pass)`, `(E: ع ق ب B002 heel/track behind)`, `(E: ع ق ب B006 end/consequence)`, `(E: ف ك ك B001 opening what is closed and separating what is interlocked)`, `(E: ف ك ك B002 freeing a neck from bondage/closure)`, `(E: ر ق ب B004 neck/person in bondage)`
- `selected_branches`: `ق ح م B001/B002/B006`; `ع ق ب B002/B003/B005/B006/B008/B009/B011/B012`; `ف ك ك B001/B002/B005`; `ر ق ب B001/B002/B004`; later `ن ج د B001/B005`, `ص ب ر B006/B017`
- `constructed_model`: The two raised ways narrow into a steep pass. The pass is not crossed by talk or possession; its first named mechanism is unlocking/releasing a neck, converting difficult ascent into liberation from constriction.
- `freeze_point`: after 90:13
- `predictions_at_freeze`: expected further costly acts under hardship; expected vulnerable recipients; expected endurance/counsel to sustain crossing.
- `unused_features_tested`: feeding in famine, orphan/kin, poor in dust, patience, mercy.
- `corroborators`: `(C: ط ع م B002 feeding another)`, `(C: س غ ب B001 hunger/famine)`, `(C: ي ت م B001 orphan cut off from protector)`, `(C: ت ر ب B002 poverty stuck to dust)`, `(C: ص ب ر B001 holding oneself from panic)`, `(C: ص ب ر B006 severity with no outlet)`, `(C: و ص ي B003 reciprocal counsel)`.
- `constraints`: `(K: العقبة is object of اقتحم and then subject/predicate in 90:12; it is an image of costly passage, not a topographical report only)`, `(K: فك رقبة is idafa; the neck/person is the freed object, not a body-part metaphor detached from social release)`.
- `temporal_reactivation_notes`: `النجدين` prepares height/path; `اقتحم العقبة` intensifies one path into a difficult threshold; `فك رقبة` answers by opening a constricted human state.
- `rival_models`: `د ر ي B004` sharp instrument and `ص ب ر B005` stone terrain add texture but are too remote to generate the core.
- `grade`: strong
- `grade_rationale`: Excellent local lexical specificity and immediate explanatory expansion from path to pass to release.
- `source_queries_or_rows_used`: attachment rows 90:11-13; branch rows named above.

### C7: Famine-care targets relational and ground-level vulnerability

- `candidate_id`: S90-C7
- `ayah_range`: 90:14-16
- `seed_type`: verified composite
- `seed`: 90:14 `إطعام في يوم ذي مسغبة`
- `generating_set`: `(E: ط ع م B002 feeding another)`, `(E: ط ع م B001 tasting/taking food)`, `(E: ي و م B003 severe event/day)`, `(E: ي و م B002 duration)`, `(E: س غ ب B001 hunger with fatigue/famine)`, `(E: ي ت م B001 child cut off from protector)`, `(E: ق ر ب B003 kinship)`, `(E: س ك ن B006 humiliation/poverty)`, `(E: ت ر ب B001 earth/dust)`, `(E: ت ر ب B002 poverty stuck to dust)`
- `selected_branches`: `ط ع م B001/B002/B004`; `ي و م B001/B002/B003`; `س غ ب B001`; `ي ت م B001/B002/B004`; `ق ر ب B001/B003/B007`; `س ك ن B001/B006/B009/B010`; `ت ر ب B001/B002`
- `constructed_model`: The steep pass now becomes a concrete emergency: feeding during a day/event of hunger. The recipients are not generic: an orphan with nearness and a poor person pressed to earth. The model moves from heap-wealth to targeted relief at the point where kinship and bodily need are exposed.
- `freeze_point`: after 90:16
- `predictions_at_freeze`: expected social stabilization and mercy; expected that action alone must be joined to belief and counsel; expected right-side outcome.
- `unused_features_tested`: then being among believers, mutual counsel in patience and mercy, companions of right.
- `corroborators`: `(C: ء م ن B001 security/trust)`, `(C: ء م ن B002 settled assent)`, `(C: ر ح م B001 mercy/r tenderness)`, `(C: ر ح م B002 kinship)`, `(C: و ص ي B003 reciprocal instruction)`, `(C: ص ح ب B001 companionship)`, `(C: ي م ن B001 blessing/right fortune)`.
- `constraints`: `(K: يتيم ذا مقربة and مسكين ذا متربة are accusative recipients under feeding; not independent new oath objects)`, `(K: ترب B003 wealth-by-dust is a rival contrast, not the contextual sense of متربة)`.
- `temporal_reactivation_notes`: The birth/generation opening is reactivated by orphanhood and kinship; the wealth-boast is reoriented into feeding; the body hardship `كبد` becomes visible as hunger, dust, and social severance.
- `rival_models`: `ط ع م B010` grafting can weakly echo social joining, but feeding is primary.
- `grade`: strong
- `grade_rationale`: The local construction is explicit and fills several earlier predictions: hardship, wealth use, kin vulnerability, and mercy.
- `source_queries_or_rows_used`: attachment rows 90:14-16; branch rows named above.

### C8: Reciprocal counsel turns individual crossing into durable mercy-community

- `candidate_id`: S90-C8
- `ayah_range`: 90:17-18
- `seed_type`: constructional/morphosyntactic
- `seed`: 90:17 `ثم كان من الذين آمنوا وتواصوا بالصبر وتواصوا بالمرحمة`
- `generating_set`: `(E: ك و ن B001 being/coming to be in time)`, `(E: ك و ن B002 place/status)`, `(E: ء م ن B001 security/trust)`, `(E: ء م ن B002 assent that settles the heart)`, `(E: و ص ي B001 joining one thing to another)`, `(E: و ص ي B002 transmitted charge/counsel)`, `(E: و ص ي B003 mutual counsel)`, `(E: ص ب ر B001 restraining self from panic)`, `(E: ص ب ر B003 bearing obligation/mulaazama)`, `(E: ر ح م B001 mercy/tenderness)`, `(E: ر ح م B002 kinship/relatedness)`
- `selected_branches`: `ك و ن B001/B002/B003`; `ء م ن B001/B002`; `و ص ي B001/B002/B003/B004`; `ص ب ر B001/B003/B006/B018`; `ر ح م B001/B002/B003`; `ص ح ب B001/B002`
- `constructed_model`: After the costly acts, the person must become part of a group whose inner assent, mutual transmission, endurance, and mercy keep the pass-crossing from being a one-time gesture. Counsel is repeated, and each repetition has a content complement: patience, then mercy.
- `freeze_point`: after 90:17
- `predictions_at_freeze`: expected group designation; expected favorable side; expected opposite group defined by denial of signs.
- `unused_features_tested`: `أولئك أصحاب الميمنة`; `والذين كفروا بآياتنا`; `أصحاب المشأمة`; sealed fire.
- `corroborators`: `(C: ص ح ب B001 companionship/membership)`, `(C: ي م ن B001 blessing/success)`, `(C: ي م ن B002 right side)`, `(C: ك ف ر B003 covering/blocking truth)`, `(C: ء ي ي B003 sign)`, `(C: attachment rows 90:17 repeated تواصوا with بـ content complements)`.
- `constraints`: `(K: ثم marks sequence after pass-actions; it does not erase the prior acts)`, `(K: بالصبر and بالمرحمة are counsel contents, not instruments)`, `(K: basmala ر ح م may corroborate mercy as opening context only, not generate the lexical seed)`.
- `temporal_reactivation_notes`: Speech introduced as boast in 90:6 is reactivated as mutual counsel in 90:17. Hardship `كبد` is reactivated as patience, and parent/child/kin vulnerability is reactivated as mercy.
- `rival_models`: `و ص ي B004` pasture fitting the herd gives a weak ecology image with feeding, but the Form VI mutual counsel syntax makes B003 primary.
- `grade`: strong
- `grade_rationale`: High specificity from repeated construction, content complements, and multiple earlier reactivations.
- `source_queries_or_rows_used`: attachment rows 90:17-18; branch rows named above.

### C9: Right-side and left-side companionship as final sorting of path-choice

- `candidate_id`: S90-C9
- `ayah_range`: 90:18-19
- `seed_type`: morphosyntactic/temporal
- `seed`: paired `أصحاب الميمنة` / `أصحاب المشأمة`
- `generating_set`: `(E: ص ح ب B001 companionship/attached membership)`, `(E: ص ح ب B002 preservation by companionship)`, `(E: ي م ن B001 blessing/prosperity)`, `(E: ي م ن B002 right side)`, `(E: ي م ن B004 strength/right)`, `(E: ش ء م B001 left side)`, `(E: ش ء م B003 ill-omen/misfortune)`, `(E: ك ف ر B001 covering)`, `(E: ك ف ر B003 blocking truth)`, `(E: ء ي ي B003 visible sign)`
- `selected_branches`: `ص ح ب B001/B002/B004`; `ي م ن B001/B002/B004`; `ش ء م B001/B003`; `ك ف ر B001/B003/B004/B006`; `ء ي ي B002/B003`; later `و ص د B001`, `ن و ر B002`
- `constructed_model`: The two shown paths become two attached companies. One side is blessing/rightness; the other is left/ill-fortune, defined not by lack of faculties but by covering signs.
- `freeze_point`: after 90:19
- `predictions_at_freeze`: expected closure over the left group; expected a constricting or covering consequence.
- `unused_features_tested`: 90:20 `عليهم نار مؤصدة`
- `corroborators`: `(C: ن و ر B002 fire)`, `(C: و ص د B001 sealed closing)`, `(C: عليهم fronted predicate attachment row 90:20)`, `(C: earlier النجدين path polarity)`.
- `constraints`: `(K: أصحاب is idafa membership, not casual accompaniment only)`, `(K: ميمنة/مشأمة carry side and evaluative polarity; do not flatten them into generic good/bad)`.
- `temporal_reactivation_notes`: The path-choice of 90:10 is withheld until after pass-actions and counsel, then resolved as company membership.
- `rival_models`: `ي م ن B003` oath can echo opening oath, but final side/blessing is primary.
- `grade`: strong
- `grade_rationale`: Direct lexical polarity and mirrored syntax, with clear prior prediction from `النجدين`.
- `source_queries_or_rows_used`: attachment rows 90:18-19; branch rows named above.

### C10: Sealed fire as anti-release and final closed state

- `candidate_id`: S90-C10
- `ayah_range`: 90:20, reactivating 90:1-2 and 90:13
- `seed_type`: lexical/temporal closure
- `seed`: 90:20 `نار مؤصدة`
- `generating_set`: `(E: ن و ر B002 fire kindled)`, `(E: ن و ر B007 hostile flare/na'ira between groups)`, `(E: و ص د B001 shutting/bolting a door)`, `(E: و ص د B002 door/threshold/fenced forecourt)`, `(E: attachment 90:20 عليهم fronted predicate over delayed نار)`
- `selected_branches`: `ن و ر B001/B002/B005/B007/B008`; `و ص د B001/B002/B003`; constraints from `ف ك ك B001/B002` and `ح ل ل B001/B003`
- `constructed_model`: The closing image inverts the pass solution. Earlier, `فك رقبة` opened a locked human state; here the left-side company has fire closed over them. The preposition `على` places the fire over/upon them, not merely near them.
- `freeze_point`: after 90:20
- `predictions_at_freeze`: no later passage material remains; test is backward only.
- `unused_features_tested`: `فك رقبة`, `حل بهذا البلد`, `كفروا بآياتنا`, `أصحاب المشأمة`.
- `corroborators`: `(C: ف ك ك B001/B002 anti-image: opening vs sealing)`, `(C: ك ف ر B001 covering truth anticipates covered enclosure)`, `(C: ش ء م B003 misfortune)`, `(C: ح ل ل B003 lawful/open state contrast)`, `(C: ب ل د B001 bounded domain reactivated as final closed domain)`.
- `constraints`: `(K: نار is rooted in ن و ر in the TSV branch data; contextual sense here is fire, not abstract light)`, `(K: مؤصدة qualifies نار, so closure belongs to the fire-state, not to a city gate in the primary reading)`.
- `temporal_reactivation_notes`: The surah closes exactly where its oppositions have been exhausted: opened neck versus sealed fire, right company versus left company, signs/guidance versus covered denial.
- `rival_models`: `و ص د B003` stone livestock enclosure gives a remote mountain/stone enclosure echo with `العقبة`; retain as weak texture only.
- `grade`: strong
- `grade_rationale`: Direct lexical closure, strong contrast with `فك`, and final-position explanatory force.
- `source_queries_or_rows_used`: attachment row 90:20; branch rows named above.

## Constructional and temporal seed passes

- `CS1 بهذا البلد repetition`: Generates a demonstrative place-frame in 90:1-2. It freezes before creation/hardship and is corroborated by final bounded closure. Grade: medium-strong.
- `CS2 لا أقسم + oath cluster`: Generates solemn witness-frame. Corroborated by `والد وما ولد`; weakly by `ي م ن B003` oath. Constraint: `لا` scope belongs to oath-opening formula per attachment row. Grade: medium.
- `CS3 والد وما ولد`: Generates generational/birth frame. Corroborated by created human, orphan, kinship, mercy. Grade: strong.
- `CS4 أيحسب / أيحسب repetition`: Generates defective internal assessment and two denials: power and sight. Corroborated by eyes/guidance/signs. Grade: strong.
- `CS5 قول quote`: Generates displayed self-account. Corroborated by later counsel-speech contrast. Grade: medium-strong.
- `CS6 body-part list`: Generates accountable faculties. Corroborated by seeing/signs, speech/counsel, path-choice. Grade: strong.
- `CS7 النجدين to العقبة`: Generates path-to-pass narrowing. Corroborated by steep pass and difficult acts. Grade: strong.
- `CS8 وما أدراك ما العقبة`: Suspends and magnifies the pass before defining it. Corroborated by the appositional list that follows. Grade: strong as discourse construction, lexical grade medium.
- `CS9 أو...أو feeding alternatives`: Generates alternate pass-actions after freeing. Corroborated by recipient constructions. Grade: strong.
- `CS10 ذا مقربة / ذا متربة parallel`: Generates two recipient specifications: relational nearness and earth-level deprivation. Grade: strong.
- `CS11 ثم كان من الذين`: Generates belonging after action, not action alone. Corroborated by أصحاب. Grade: strong.
- `CS12 repeated وتواصوا بـ`: Generates social maintenance with two content complements. Grade: strong.
- `CS13 أصحاب الميمنة / أصحاب المشأمة`: Generates final polarity and group membership. Grade: strong.
- `CS14 عليهم نار مؤصدة`: Generates final anti-release closure over the left group. Grade: strong.

## Failed and terminated seed summary

The following branch classes were visited and terminated when they did not create a passage-local transformation: named places or proper nouns (`ء ح د B006`, `ق ر ب B011`, `ه ل ك B007`, `ل ب د B008`), animal-specific branches without local support (`ج ع ل B008-B010`, `ط ع م B009`, `ح ل ل B014`, `ل س ن B007`), textile/garment/oil branches without local support (`ح ل ل B007/B015`, `ق س م B007`, `ل ب د B004`), astronomical branches without local support (`ب ل د B004`, `ر ق ب B007`, `ف ك ك B008`), remote plant branches without local support (`ت ر ب B007`, `ن و ر B004`, `و ص د B004`), and grammatical particles under `ء ي ي` that do not match the surface `آياتنا` except the sign branch B003.

Several remote branches were retained only as weak texture, not candidate generators: `ب ل د B002` chest, `ك ب د B004` bow curve, `د ر ي B004` sharp edge, `ص ب ر B005/B017` stone/mountain, `ع ي ن B006` water-source, `و ص د B003` stone enclosure. None should be promoted to primary meaning in Stage 2 without independent corroboration.

## Image Packet Catalog

### IMAGE S90-IMG1: Bounded Domain / Closed Domain

- Starting seed: `ق س م B004` + `ب ل د B001`
- Complete image: A specific bounded place is invoked; human life inside it is tested; the failed side ends in another bounded state, sealed over them.
- Passage-order assembly: 90:1-2 domain; 90:4 human condition inside struggle; 90:18-20 sorted companies and sealed fire.
- Participants and roles: oath speaker, addressed person, inhabitants/human subject, right company, left company.
- Operation / mechanism: oath binds attention; judgment sorts; closure seals.
- Direction / force / medium: from open demonstrative place to closed fire-over-them.
- Temporal development: opening place-frame reactivates only at final closure.
- Outcome / closure: `نار مؤصدة`.
- Exact branch constituents: `ق س م B004`; `ب ل د B001/B009`; `ح ل ل B002/B003`; `و ص د B001`; `ن و ر B002`.
- Unfilled roles, if any: city identity remains primary historical/contextual outside Stage 1 lexical proof.
- Status: COMPLETE.

### IMAGE S90-IMG2: Birth / Embodied Hardship / Mercy Repair

- Starting seed: `و ل د B003`
- Complete image: Human birth and creation place the person in central hardship; later vulnerable offspring/kin and mercy repair that exposed condition.
- Passage-order assembly: 90:3 parent-born; 90:4 created human in `كبد`; 90:15 orphan-near; 90:17 mercy.
- Participants and roles: parent, born human, orphan, near kin, merciful counsel-community.
- Operation / mechanism: generation exposes vulnerability; care and mercy answer it.
- Direction / force / medium: from womb/lineage to social mercy.
- Temporal development: early birth image returns after steep-pass acts.
- Outcome / closure: right-side companionship if joined to belief/counsel.
- Exact branch constituents: `و ل د B001/B002/B003`; `خ ل ق B001/B002`; `ك ب د B002/B003`; `ي ت م B001`; `ق ر ب B003`; `ر ح م B001/B002/B003`.
- Unfilled roles, if any: exact parent in oath not specified.
- Status: COMPLETE.

### IMAGE S90-IMG3: Defective Calculation / Given Faculties / Signs

- Starting seed: `ح س ب B002`
- Complete image: The subject calculates immunity from power and sight; the passage answers with made eyes, tongue/lips, guidance, and signs.
- Passage-order assembly: 90:5-7 assumptions; 90:8-10 faculties and paths; 90:19 signs denied.
- Participants and roles: calculating human, unseen one who sees/has power, given faculties, signs.
- Operation / mechanism: false inner estimate is exposed by prior endowment and later signs.
- Direction / force / medium: from interior supposition to visible faculties and signs.
- Temporal development: questions trigger backward/forward audit of perception.
- Outcome / closure: denial of signs places one among left-side companions.
- Exact branch constituents: `ح س ب B001/B002`; `ق د ر B001/B003`; `ر ء ي B001/B012`; `ع ي ن B001/B003`; `ء ي ي B003`.
- Unfilled roles, if any: the powerful/seer is grammatically `أحد`; theological identification is not Stage 1 lexical proof.
- Status: COMPLETE.

### IMAGE S90-IMG4: Heap-Waste / Targeted Relief

- Starting seed: `ل ب د B002`
- Complete image: A boastful voice claims heaps of wealth were consumed; the passage redirects expenditure into freeing and feeding under famine.
- Passage-order assembly: 90:6 wealth heap; 90:13 freeing; 90:14-16 feeding recipients.
- Participants and roles: boasting speaker, wealth heap, captive/neck, hungry orphan/poor.
- Operation / mechanism: accumulated mass is depleted or reallocated; valid expenditure opens and feeds.
- Direction / force / medium: from self-display to recipient-directed relief.
- Temporal development: quote is tested by later costly pass definitions.
- Outcome / closure: only joined to belief/counsel does action become right-side membership.
- Exact branch constituents: `ق و ل B001/B012`; `ه ل ك B001/B009`; `م و ل B001`; `ل ب د B001/B002`; `ف ك ك B002`; `ط ع م B002`; `س غ ب B001`.
- Unfilled roles, if any: whether the boast refers to actual generosity or waste remains rival.
- Status: COMPLETE.

### IMAGE S90-IMG5: Two Raised Ways / Steep Pass

- Starting seed: `ن ج د B001`
- Complete image: Guidance to two elevated clear ways is narrowed into the hard pass that must be stormed through freeing, feeding, patience, and mercy.
- Passage-order assembly: 90:10 two ways; 90:11-12 pass; 90:13-17 pass operations and maintenance.
- Participants and roles: guided human, two paths, steep pass, freed person, fed recipients, counsel group.
- Operation / mechanism: path-choice becomes costly ascent and social repair.
- Direction / force / medium: upward/raised route into difficult threshold.
- Temporal development: the path appears before the pass is named, allowing prediction.
- Outcome / closure: right/left sorting.
- Exact branch constituents: `ه د ي B001`; `ن ج د B001/B002/B005`; `ق ح م B001/B002`; `ع ق ب B012`; `ف ك ك B002`; `ط ع م B002`; `ص ب ر B001`; `ر ح م B001`.
- Unfilled roles, if any: exact two alternatives are defined by sequence rather than a single lexical branch.
- Status: COMPLETE.

### IMAGE S90-IMG6: Counsel Network / Right-Side Company

- Starting seed: `و ص ي B003`
- Complete image: Individual costly action becomes durable only inside reciprocal counsel: belief, patience, and mercy bind a company of the right.
- Passage-order assembly: 90:17 belief and two counsels; 90:18 right companions; 90:19 opposite denied signs.
- Participants and roles: believers, mutual counselors, right companions, left deniers.
- Operation / mechanism: reciprocal transmission maintains patience and mercy.
- Direction / force / medium: social connection through speech.
- Temporal development: boastful speech becomes counsel speech.
- Outcome / closure: right-side companionship.
- Exact branch constituents: `ء م ن B001/B002`; `و ص ي B001/B002/B003`; `ص ب ر B001/B003`; `ر ح م B001/B002`; `ص ح ب B001`; `ي م ن B001/B002`.
- Unfilled roles, if any: none.
- Status: COMPLETE.

## Exhaustiveness check after file creation

- Rooted words: all 44 distinct S90 roots from the local QAC-root TSV are included.
- Lexical branch seeds: all 389 accepted branch IDs for those roots from the local v4 branch TSV are accounted for in the coverage ledger.
- Constructional seeds: repeated oath/place, birth oath, two `أيحسب` clauses, quote, body list, two paths, steep-pass question, freeing/feeding definitions, recipient parallels, `ثم كان`, repeated `تواصوا بـ`, right/left companions, and sealed fire are included.
- Evidence timing: detailed candidates separate generating sets from post-freeze corroborators and constraints.
- Basmala: used only as opening-context corroboration for mercy, never as seed.
- Remaining limitation: because the prompt-named SQLite databases are empty in this checkout, this file relies on local TSV mirrors for QAC/root and branch data. Stage 2 should treat that as a source-condition note, not as a lexical conclusion.
