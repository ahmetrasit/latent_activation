# v11 Activation Packet — S92:9-16

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_9: وَكَذَّبَ بِٱلْحُسْنَىٰ
- verse_10: فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
- verse_11: وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
- verse_12: إِنَّ عَلَيْنَا لَلْهُدَىٰ
- verse_13: وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- verse_14: فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- verse_15: لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- verse_16: ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ك ذ ب → ح س ن → ي س ر → ع س ر → غ ن ي → م و ل → ر د ي → ه د ي → ء خ ر → ء و ل → ن ذ ر → ن و ر → ل ظ ي → ص ل ي → ش ق و → و ل ي

## Branch inventory summary

- ك ذ ب: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- ح س ن: 5 branches (4 with Qnet bridge-theme nodes; 1 Furūq-only)
- ي س ر: 11 branches (11 with Qnet bridge-theme nodes; 0 Furūq-only)
- ع س ر: 13 branches (13 with Qnet bridge-theme nodes; 0 Furūq-only)
- غ ن ي: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- م و ل: 2 branches (2 with Qnet bridge-theme nodes; 0 Furūq-only)
- ر د ي: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- ه د ي: 11 branches (11 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء خ ر: 4 branches (3 with Qnet bridge-theme nodes; 1 Furūq-only)
- ء و ل: 11 branches (11 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن ذ ر: 3 branches (3 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن و ر: 11 branches (11 with Qnet bridge-theme nodes; 0 Furūq-only)
- ل ظ ي: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص ل ي: 10 branches (10 with Qnet bridge-theme nodes; 0 Furūq-only)
- ش ق و: 4 branches (3 with Qnet bridge-theme nodes; 1 Furūq-only)
- و ل ي: 16 branches (15 with Qnet bridge-theme nodes; 1 Furūq-only)

## QAC-first root resolution audit

- ك ذ ب | qac_keys=كذب | status=resolved | matches=root_001290
- ح س ن | qac_keys=حسن | status=resolved | matches=root_000323
- ي س ر | qac_keys=يسر | status=resolved | matches=root_001694
- ع س ر | qac_keys=عسر | status=resolved | matches=root_001012
- غ ن ي | qac_keys=غني | status=resolved | matches=root_001110
- م و ل | qac_keys=مول | status=resolved | matches=root_001457
- ر د ي | qac_keys=ردي | status=resolved | matches=root_000558
- ه د ي | qac_keys=هدي | status=resolved | matches=root_001583
- ء خ ر | qac_keys=ءخر | status=resolved | matches=root_000019
- ء و ل | qac_keys=ءول | status=resolved | matches=root_000067
- ن ذ ر | qac_keys=نذر | status=resolved | matches=root_001488
- ن و ر | qac_keys=نور | status=resolved | matches=root_001564
- ل ظ ي | qac_keys=لظي | status=resolved | matches=root_001357
- ص ل ي | qac_keys=صلي | status=resolved | matches=root_000880
- ش ق و | qac_keys=شقو | status=resolved | matches=root_000808
- و ل ي | qac_keys=ولي | status=resolved | matches=root_001684

## Top candidate bridges

- `ء و ل B011` ↔ `ص ل ي B010` | score_hint=31 | discovery_hint=21 | themes=agriculture, animal, food_nutrition, habitat_ecology, husbandry, pasture_forage, plant_vegetation | keywords=agriculture, botany, ecology, pasture | q2=—
- `ي س ر B003` ↔ `غ ن ي B001` | score_hint=28 | discovery_hint=14 | themes=abundance_scarcity, economy, hierarchy_status, provision_resource | keywords=abundance, economy, provision, resource, status | q2=—
- `ي س ر B006` ↔ `ع س ر B007` | score_hint=28 | discovery_hint=15 | themes=animal, husbandry, livestock, reproduction_birth | keywords=animal, fertility, husbandry, livestock, reproduction | q2=—
- `ع س ر B009` ↔ `ه د ي B008` | score_hint=28 | discovery_hint=15 | themes=animal, body, motion, posture_embodiment | keywords=animal, body, locomotion, motion, posture | q2=—
- `ك ذ ب B006` ↔ `ي س ر B006` | score_hint=26 | discovery_hint=16 | themes=abundance_scarcity, animal, food_nutrition, livestock, reproduction_birth | keywords=animal, fertility, livestock, nourishment | q2=—
- `ع س ر B009` ↔ `ر د ي B002` | score_hint=26 | discovery_hint=15 | themes=animal, body, motion, posture_embodiment, speed | keywords=animal, body, locomotion, speed | q2=—
- `ي س ر B004` ↔ `ء خ ر B003` | score_hint=24 | discovery_hint=15 | themes=anatomy, body, orientation_direction, space | keywords=anatomy, body, orientation, space | q2=—
- `ع س ر B009` ↔ `ص ل ي B006` | score_hint=24 | discovery_hint=15 | themes=anatomy, animal, body, motion | keywords=anatomy, animal, body, locomotion | q2=—
- `غ ن ي B006` ↔ `ه د ي B006` | score_hint=24 | discovery_hint=14 | themes=family, household_community, kinship, marriage_genealogy | keywords=family, household, kinship, marriage | q2=—
- `ي س ر B004` ↔ `ع س ر B005` | score_hint=23 | discovery_hint=20 | themes=body, orientation_direction, surface_shape | keywords=body, direction, laterality, orientation | q2=—
- `ل ظ ي B002` ↔ `ص ل ي B003` | score_hint=23 | discovery_hint=17 | themes=afterlife_eschatology, fire_heat, justice_judgment, punishment_sanction, suffering_hardship | keywords=afterlife, fire, punishment | q2=—
- `ك ذ ب B007` ↔ `ع س ر B009` | score_hint=22 | discovery_hint=14 | themes=agency_action, animal, motion | keywords=animal, behavior, motion, pursuit | q2=—
- `ي س ر B003` ↔ `م و ل B001` | score_hint=22 | discovery_hint=14 | themes=abundance_scarcity, economy, provision_resource | keywords=economy, livelihood, prosperity, resource | q2=—
- `ي س ر B005` ↔ `ع س ر B009` | score_hint=22 | discovery_hint=15 | themes=animal, body, motion | keywords=animal, body, locomotion, motion | q2=—
- `ي س ر B005` ↔ `ر د ي B002` | score_hint=22 | discovery_hint=15 | themes=animal, body, motion | keywords=animal, body, locomotion, movement | q2=—
- `ي س ر B005` ↔ `ه د ي B008` | score_hint=22 | discovery_hint=15 | themes=animal, body, motion | keywords=animal, body, locomotion, motion | q2=—
- `غ ن ي B005` ↔ `ر د ي B004` | score_hint=22 | discovery_hint=15 | themes=hierarchy_status, identity_personhood, ornament_beauty | keywords=adornment, identity, ornament, status | q2=—
- `ع س ر B001` ↔ `ش ق و B002` | score_hint=22 | discovery_hint=12 | themes=conflict, control_restraint, justice_judgment, stability_endurance, suffering_hardship | keywords=endurance, suffering, trial | q2=—
- `ع س ر B002` ↔ `م و ل B001` | score_hint=22 | discovery_hint=15 | themes=abundance_scarcity, economy, finance_debt, provision_resource, wealth_property | keywords=economy, finance, livelihood | q2=—
- `ك ذ ب B009` ↔ `ر د ي B004` | score_hint=20 | discovery_hint=14 | themes=ornament_beauty, textile_clothing | keywords=adornment, clothing, ornament, textile | q2=—
- `ر د ي B002` ↔ `ه د ي B008` | score_hint=20 | discovery_hint=14 | themes=animal, body, motion, posture_embodiment | keywords=animal, body, locomotion | q2=—
- `ك ذ ب B005` ↔ `و ل ي B002` | score_hint=18 | discovery_hint=13 | themes=sequence_cycle, stability_endurance, time | keywords=continuity, sequence, time | q2=—
- `ك ذ ب B006` ↔ `ع س ر B007` | score_hint=18 | discovery_hint=14 | themes=animal, livestock, reproduction_birth | keywords=animal, fertility, livestock | q2=—
- `ك ذ ب B007` ↔ `و ل ي B006` | score_hint=18 | discovery_hint=13 | themes=memory_attention, motion, perception | keywords=attention, motion, perception | q2=—
- `ح س ن B004` ↔ `ء و ل B006` | score_hint=18 | discovery_hint=13 | themes=form_structure, geography_landscape, terrain_desert | keywords=landscape, morphology, topography | q2=—
- `ي س ر B005` ↔ `ه د ي B010` | score_hint=18 | discovery_hint=14 | themes=body, control_restraint, motion | keywords=body, motion, movement | q2=—
- `ي س ر B005` ↔ `ص ل ي B006` | score_hint=18 | discovery_hint=14 | themes=animal, body, motion | keywords=animal, body, locomotion | q2=—
- `ي س ر B010` ↔ `ع س ر B012` | score_hint=18 | discovery_hint=14 | themes=geography_landscape, identity_personhood, naming_classification | keywords=geography, identity, naming | q2=—
- `ي س ر B011` ↔ `غ ن ي B005` | score_hint=18 | discovery_hint=14 | themes=gender, hierarchy_status, identity_personhood | keywords=gender, identity, status | q2=—
- `ع س ر B005` ↔ `ء خ ر B003` | score_hint=18 | discovery_hint=14 | themes=animal, body, orientation_direction | keywords=animal, body, orientation | q2=—
- `ع س ر B009` ↔ `ه د ي B003` | score_hint=18 | discovery_hint=13 | themes=anatomy, animal, motion | keywords=anatomy, animal, motion | q2=—
- `ع س ر B009` ↔ `ء خ ر B003` | score_hint=18 | discovery_hint=14 | themes=anatomy, animal, body | keywords=anatomy, animal, body | q2=—
- `ر د ي B002` ↔ `ص ل ي B006` | score_hint=18 | discovery_hint=14 | themes=animal, body, motion | keywords=animal, body, locomotion | q2=—
- `ه د ي B005` ↔ `ن ذ ر B002` | score_hint=18 | discovery_hint=13 | themes=pilgrimage_sacrifice, religion_worship, ritual | keywords=religion, ritual, sacrifice | q2=—
- `ه د ي B008` ↔ `ص ل ي B006` | score_hint=18 | discovery_hint=14 | themes=animal, body, motion | keywords=animal, body, locomotion | q2=—
- `ء خ ر B003` ↔ `ص ل ي B006` | score_hint=18 | discovery_hint=14 | themes=anatomy, animal, body | keywords=anatomy, animal, body | q2=—
- `ء و ل B001` ↔ `ص ل ي B007` | score_hint=18 | discovery_hint=12 | themes=hierarchy_status, motion, sequence_cycle | keywords=hierarchy, motion, sequence | q2=—
- `ن و ر B011` ↔ `و ل ي B011` | score_hint=18 | discovery_hint=13 | themes=textile_clothing, tools_equipment, transport | keywords=equipment, textile, transport | q2=—
- `ي س ر B005` ↔ `و ل ي B006` | score_hint=16 | discovery_hint=13 | themes=authority_governance, motion | keywords=motion, movement, obedience | q2=—
- `ه د ي B004` ↔ `و ل ي B014` | score_hint=16 | discovery_hint=15 | themes=commerce_exchange, wealth_property | keywords=commerce, exchange, property | q2=—
- `ه د ي B005` ↔ `ص ل ي B001` | score_hint=16 | discovery_hint=12 | themes=religion_worship, ritual | keywords=religion, ritual, worship | q2=—
- `ل ظ ي B001` ↔ `ص ل ي B004` | score_hint=16 | discovery_hint=12 | themes=change_transition, fire_heat | keywords=combustion, heat, transformation | q2=—
- `ك ذ ب B001` ↔ `ن و ر B010` | score_hint=16 | discovery_hint=11 | themes=communication, deception_corruption, proof_uncertainty, rhetoric_discourse | keywords=communication, deception | q2=—
- `ك ذ ب B002` ↔ `ن و ر B010` | score_hint=16 | discovery_hint=12 | themes=communication, knowledge_learning, proof_uncertainty, rhetoric_discourse | keywords=communication, epistemology | q2=—
- `ي س ر B002` ↔ `ر د ي B005` | score_hint=15 | discovery_hint=18 | themes=abundance_scarcity, measurement, quantity_number | keywords=quantity, scale | q2=—
- `ه د ي B005` ↔ `ص ل ي B008` | score_hint=14 | discovery_hint=13 | themes=religion_worship | keywords=religion, sanctuary, worship | q2=—
- `ء و ل B006` ↔ `ن و ر B001` | score_hint=14 | discovery_hint=12 | themes=perception | keywords=optics, perception, visibility | q2=—
- `ن و ر B002` ↔ `ص ل ي B004` | score_hint=14 | discovery_hint=13 | themes=fire_heat | keywords=combustion, fire, heat | q2=—
- `ك ذ ب B003` ↔ `ن ذ ر B002` | score_hint=14 | discovery_hint=12 | themes=agency_action, obligation_contract, religion_worship | keywords=duty, religion | q2=—
- `ك ذ ب B003` ↔ `ص ل ي B001` | score_hint=14 | discovery_hint=11 | themes=authority_governance, control_restraint, religion_worship | keywords=discipline, religion | q2=—
- `ك ذ ب B009` ↔ `ح س ن B001` | score_hint=14 | discovery_hint=11 | themes=ornament_beauty, perception, visual_appearance | keywords=appearance, perception | q2=—
- `ح س ن B001` ↔ `ه د ي B010` | score_hint=14 | discovery_hint=11 | themes=ethics_morality, ornament_beauty, visual_appearance | keywords=aesthetics, appearance | q2=—
- `ي س ر B001` ↔ `غ ن ي B002` | score_hint=14 | discovery_hint=12 | themes=capacity_ability, change_transition, support_dependence | keywords=capacity, support | q2=—
- `ي س ر B003` ↔ `ع س ر B002` | score_hint=14 | discovery_hint=13 | themes=abundance_scarcity, economy, provision_resource | keywords=economy, livelihood | q2=—
- `ي س ر B005` ↔ `ه د ي B003` | score_hint=14 | discovery_hint=12 | themes=animal, authority_governance, motion | keywords=animal, motion | q2=—
- `ي س ر B005` ↔ `و ل ي B007` | score_hint=14 | discovery_hint=12 | themes=authority_governance, control_restraint, motion | keywords=movement, obedience | q2=—
- `ي س ر B005` ↔ `و ل ي B012` | score_hint=14 | discovery_hint=13 | themes=control_restraint, force_power, motion | keywords=control, movement | q2=—
- `ي س ر B006` ↔ `ص ل ي B010` | score_hint=14 | discovery_hint=13 | themes=animal, food_nutrition, husbandry | keywords=animal, pastoralism | q2=—
- `ي س ر B008` ↔ `ن و ر B008` | score_hint=14 | discovery_hint=13 | themes=body, health_medicine, writing_text | keywords=body, inscription | q2=—
- `ي س ر B009` ↔ `ر د ي B001` | score_hint=14 | discovery_hint=12 | themes=force_power, violence_warfare, weaponry | keywords=combat, weapon | q2=—
- `ي س ر B011` ↔ `غ ن ي B006` | score_hint=14 | discovery_hint=12 | themes=hierarchy_status, household_community, kinship | keywords=kinship, status | q2=—
- `ي س ر B011` ↔ `ه د ي B006` | score_hint=14 | discovery_hint=12 | themes=gender, household_community, kinship | keywords=gender, kinship | q2=—
- `ي س ر B011` ↔ `ء و ل B003` | score_hint=14 | discovery_hint=13 | themes=household_community, identity_personhood, kinship | keywords=identity, kinship | q2=—
- `ع س ر B001` ↔ `ص ل ي B003` | score_hint=14 | discovery_hint=11 | themes=danger_harm, justice_judgment, suffering_hardship | keywords=suffering, trial | q2=—
- `ع س ر B002` ↔ `غ ن ي B001` | score_hint=14 | discovery_hint=12 | themes=abundance_scarcity, economy, provision_resource | keywords=economy, poverty | q2=—
- `ع س ر B003` ↔ `ن ذ ر B003` | score_hint=14 | discovery_hint=13 | themes=finance_debt, justice_judgment, law | keywords=justice, law | q2=—
- `ع س ر B011` ↔ `ص ل ي B007` | score_hint=14 | discovery_hint=12 | themes=motion, politics_order, sequence_cycle | keywords=order, sequence | q2=—
- `غ ن ي B001` ↔ `م و ل B001` | score_hint=14 | discovery_hint=11 | themes=abundance_scarcity, economy, provision_resource | keywords=economy, resource | q2=—
- `غ ن ي B006` ↔ `ء و ل B003` | score_hint=14 | discovery_hint=12 | themes=household_community, kinship, marriage_genealogy | keywords=household, kinship | q2=—
- `غ ن ي B006` ↔ `و ل ي B005` | score_hint=14 | discovery_hint=12 | themes=family, hierarchy_status, household_community | keywords=family, status | q2=—
- `ه د ي B003` ↔ `ص ل ي B006` | score_hint=14 | discovery_hint=12 | themes=anatomy, animal, motion | keywords=anatomy, animal | q2=—
- `ه د ي B006` ↔ `ء و ل B003` | score_hint=14 | discovery_hint=12 | themes=household_community, kinship, marriage_genealogy | keywords=household, kinship | q2=—
- `ه د ي B008` ↔ `ء خ ر B003` | score_hint=14 | discovery_hint=13 | themes=animal, body, transport | keywords=animal, body | q2=—
- `ء خ ر B001` ↔ `و ل ي B007` | score_hint=14 | discovery_hint=12 | themes=loss_absence, measurement, social_relations | keywords=absence, distance | q2=—
- `ن و ر B007` ↔ `ل ظ ي B003` | score_hint=14 | discovery_hint=12 | themes=conflict, emotion, violence_warfare | keywords=conflict, emotion | q2=—
- `ص ل ي B007` ↔ `ش ق و B003` | score_hint=14 | discovery_hint=12 | themes=conflict, hierarchy_status, reasoning_decision | keywords=competition, hierarchy | q2=—
- `ص ل ي B010` ↔ `و ل ي B015` | score_hint=14 | discovery_hint=13 | themes=agriculture, animal, husbandry | keywords=agriculture, animal | q2=—
- `ك ذ ب B001` ↔ `ه د ي B001` | score_hint=12 | discovery_hint=10 | themes=ethics_morality, proof_uncertainty | keywords=ethics, truth | q2=—
- `ك ذ ب B004` ↔ `ي س ر B009` | score_hint=12 | discovery_hint=12 | themes=motion, violence_warfare | keywords=combat, motion | q2=—
- `ك ذ ب B004` ↔ `ه د ي B010` | score_hint=12 | discovery_hint=12 | themes=intention_character, motion | keywords=motion, movement | q2=—

## Per-root candidate activations

### ك ذ ب

- `ك ذ ب B001` — خلاف الصدق
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: communication, deception_corruption, ethics_morality, proof_uncertainty, rhetoric_discourse, testimony_witness, trust_loyalty
  - keywords: communication, deception, ethics, testimony, trust, truth
- `ك ذ ب B002` — نسبة الشيء أو صاحبه إلى الكذب
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: communication, conflict, justice_judgment, knowledge_learning, proof_uncertainty, rhetoric_discourse, testimony_witness, trust_loyalty
  - keywords: communication, epistemology, judgment, testimony, trust
- `ك ذ ب B003` — كذب عليك بمعنى الزم وعليك به
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: agency_action, authority_governance, control_restraint, intention_character, motion, obligation_contract, reasoning_decision, religion_worship
  - keywords: discipline, duty, obligation, practice, pursuit, religion, resolve
- `ك ذ ب B004` — صدق الحملة أو كذبها
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: agency_action, honor_shame, intention_character, justice_judgment, motion, reasoning_decision, violence_warfare
  - keywords: combat, motion, movement, performance, resolve, trial, violence, warfare
- `ك ذ ب B005` — ما كذب أن فعل أي ما لبث
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: agency_action, change_transition, communication, sequence_cycle, speed, stability_endurance, time
  - keywords: completion, continuity, sequence, speed, time, transition
- `ك ذ ب B006` — كذب لبن الناقة إذا ذهب ولم يدم
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ل ظ ي, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: abundance_scarcity, animal, change_transition, cognition, food_nutrition, livestock, provision_resource, reproduction_birth
  - keywords: animal, fertility, livestock, nourishment, provision, resource, scarcity
- `ك ذ ب B007` — كذب الوحشي إذا جرى ثم وقف
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ل ظ ي, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: agency_action, animal, habitat_ecology, memory_attention, motion, navigation_route, perception, protection_security
  - keywords: animal, attention, behavior, motion, perception, predation, pursuit
- `ك ذ ب B008` — النفس الكذوب
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: cognition, deception_corruption, desire_appetite, ethics_morality, identity_personhood, intention_character, trust_loyalty
  - keywords: character, cognition, deception, desire, identity, morality, psychology, trust
- `ك ذ ب B009` — الكذابة ثوب يكذب بحاله
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: craft, deception_corruption, material, ornament_beauty, perception, textile_clothing, visual_appearance
  - keywords: adornment, appearance, clothing, craft, material, ornament, perception, textile

### ح س ن

- `ح س ن B001` — الحسن ضد القبح
  - activated_by_or_with: ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: desire_appetite, ethics_morality, force_power, ornament_beauty, perception, value_quality, visual_appearance
  - keywords: aesthetics, appearance, evaluation, perception, quality, virtue
- `ح س ن B002` — الإحسان فعل حسن
  - activated_by_or_with: ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: craft, ethics_morality, hospitality_welfare, justice_judgment
  - keywords: craft, ethics, generosity, justice, virtue
- `ح س ن B003` — الحسنة خير يصيب
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ح س ن B004` — أسماء الحسن للمواضع والأجسام
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, ل ظ ي, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: anatomy, form_structure, geography_landscape, naming_classification, terrain_desert
  - keywords: anatomy, geography, landscape, morphology, onomastics, taxonomy, topography
- `ح س ن B005` — حُسَيْناء الغاية والجهد
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: boundary, capacity_ability, change_transition, desire_appetite, labor_work, measurement, stability_endurance, value_quality
  - keywords: achievement, boundary, capacity, completion, endurance, exertion, limit

### ي س ر

- `ي س ر B001` — انفتاح وسهولة بعد عسر
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي
  - themes: capacity_ability, change_transition, containment_access, obligation_contract, suffering_hardship, support_dependence
  - keywords: assistance, capacity, readiness, support, transition
- `ي س ر B002` — قلة يسيرة
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ع س ر, غ ن ي, ك ذ ب, م و ل, ن و ر, و ل ي
  - themes: abundance_scarcity, boundary, measurement, quantity_number, time
  - keywords: duration, limit, quantity, scale, scarcity
- `ي س ر B003` — سعة وغنى
  - activated_by_or_with: ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, م و ل, ه د ي, و ل ي
  - themes: abundance_scarcity, economy, hierarchy_status, provision_resource
  - keywords: abundance, economy, livelihood, prosperity, provision, resource, status
- `ي س ر B004` — الجهة اليسرى واليد اليسرى
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, ك ذ ب, ن و ر, ه د ي, و ل ي
  - themes: anatomy, body, navigation_route, orientation_direction, space, surface_shape
  - keywords: anatomy, body, direction, laterality, navigation, orientation, space
- `ي س ر B005` — خفة وانقياد في الحركة
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي
  - themes: animal, authority_governance, body, capacity_ability, control_restraint, force_power, motion, substance_texture
  - keywords: animal, body, control, locomotion, motion, movement, obedience
- `ي س ر B006` — إدرار ونماء في الغنم
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, م و ل, ن و ر, ه د ي, و ل ي
  - themes: abundance_scarcity, animal, food_nutrition, husbandry, labor_work, livestock, reproduction_birth
  - keywords: abundance, animal, fertility, herd, husbandry, livestock, nourishment, pastoralism, reproduction
- `ي س ر B007` — قداح وقمار وتقسيم جزور
  - activated_by_or_with: ء و ل, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي
  - themes: food_nutrition, pilgrimage_sacrifice, proof_uncertainty, provision_resource, recreation_sport, ritual
  - keywords: allocation, ritual, sacrifice
- `ي س ر B008` — خطوط منفصلة وعلامات في البدن
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ن ذ ر, ن و ر, ه د ي
  - themes: anatomy, body, health_medicine, identity_personhood, pattern_marking, proof_uncertainty, writing_text
  - keywords: anatomy, body, identity, inscription, marking, pattern, sign
- `ي س ر B009` — فتل إلى أسفل وطعن حذاء الوجه
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي
  - themes: craft, force_power, motion, orientation_direction, violence_warfare, weaponry
  - keywords: combat, craft, direction, motion, orientation, weapon
- `ي س ر B010` — موضع أو علم باسم يسر ويسار
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن و ر, ه د ي, و ل ي
  - themes: geography_landscape, identity_personhood, naming_classification, rhetoric_discourse
  - keywords: geography, identity, naming, onomastics, poetry
- `ي س ر B011` — فتى يسمى يسارا
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, م و ل, ن و ر, ه د ي, و ل ي
  - themes: gender, hierarchy_status, household_community, identity_personhood, kinship, life_stage_aging, naming_classification, physiology
  - keywords: gender, identity, kinship, lexicography, life, status

### ع س ر

- `ع س ر B001` — الصعوبة والشدة
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: conflict, control_restraint, danger_harm, force_power, justice_judgment, stability_endurance, suffering_hardship
  - keywords: crisis, endurance, obstruction, suffering, trial
- `ع س ر B002` — ضيق ذات اليد
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, غ ن ي, ك ذ ب, م و ل, ن ذ ر, ه د ي, و ل ي, ي س ر
  - themes: abundance_scarcity, economy, finance_debt, hospitality_welfare, loss_absence, provision_resource, wealth_property
  - keywords: debt, economy, finance, livelihood, poverty, scarcity
- `ع س ر B003` — مطالبة المعسر
  - activated_by_or_with: ء خ ر, ح س ن, ر د ي, ش ق و, ص ل ي, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: commerce_exchange, control_restraint, ethics_morality, finance_debt, justice_judgment, law, obligation_contract
  - keywords: coercion, commerce, debt, justice, law, obligation
- `ع س ر B004` — الخلاف والالتواء والتعسير
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: conflict, control_restraint, force_power, form_structure, rhetoric_discourse
  - keywords: conflict, negotiation, obstruction
- `ع س ر B005` — الشمال والأعسر
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ش ق و, ص ل ي, ك ذ ب, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: animal, body, orientation_direction, proof_uncertainty, surface_shape
  - keywords: animal, body, direction, laterality, orientation, sign
- `ع س ر B006` — تعسر الولادة
  - activated_by_or_with: ر د ي, ص ل ي, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: danger_harm, gender, health_medicine, reproduction_birth
  - keywords: birth, crisis, medicine, reproduction, risk
- `ع س ر B007` — الناقة التي لا تحمل عامها
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ص ل ي, ك ذ ب, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: animal, calendar_season, husbandry, livestock, reproduction_birth
  - keywords: animal, fertility, husbandry, livestock, reproduction, season
- `ع س ر B008` — الركوب والأخذ قبل التهيئة
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ش ق و, ص ل ي, غ ن ي, ك ذ ب, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: capacity_ability, control_restraint, ethics_morality, knowledge_learning, obligation_contract, transport, wealth_property
  - keywords: coercion, consent, ownership, property, readiness, training, transport
- `ع س ر B009` — رفع الذنب في العدو
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, غ ن ي, ك ذ ب, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: agency_action, anatomy, animal, body, motion, posture_embodiment, speed
  - keywords: anatomy, animal, behavior, body, locomotion, motion, posture, pursuit, speed
- `ع س ر B010` — اليوم المشؤوم
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ش ق و, ص ل ي, ك ذ ب, ل ظ ي, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: belief_revelation, calendar_season, suffering_hardship, time
  - keywords: belief, fate, time
- `ع س ر B011` — التفرق والتتابع
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ش ق و, ص ل ي, غ ن ي, ك ذ ب, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: household_community, livestock, motion, politics_order, ritual, sequence_cycle, travel
  - keywords: herd, movement, order, sequence, travel
- `ع س ر B012` — أعلام الجن والمواضع
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, غ ن ي, ك ذ ب, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: belief_revelation, geography_landscape, identity_personhood, kinship, naming_classification, place_location
  - keywords: geography, identity, naming, place
- `ع س ر B013` — لعبة العسر
  - activated_by_or_with: ء و ل, ر د ي, ش ق و, ص ل ي, ك ذ ب, ل ظ ي, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: conflict, material, recreation_sport, tools_equipment, weaponry
  - keywords: competition, projectile, sport, tool

### غ ن ي

- `غ ن ي B001` — الغنى والاستغناء
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, ك ذ ب, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: abundance_scarcity, capacity_ability, control_restraint, economy, hierarchy_status, protection_security, provision_resource
  - keywords: abundance, capacity, economy, poverty, provision, resource, security, status
- `غ ن ي B002` — الغَناء والكفاية
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, ك ذ ب, ل ظ ي, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: capacity_ability, change_transition, commerce_exchange, health_medicine, provision_resource, support_dependence, value_quality
  - keywords: capacity, exchange, provision, support, utility
- `غ ن ي B003` — الغِناء والصوت
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: agency_action, emotion, grammar_expression, ornament_beauty, perception, religion_worship, rhetoric_discourse, ritual
  - keywords: aesthetics, emotion, performance, poetry, ritual, worship
- `غ ن ي B004` — الغنى بالمكان
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, ك ذ ب, ل ظ ي, ه د ي, و ل ي, ي س ر
  - themes: habitat_ecology, household_community, memory_attention, physiology, place_location, stability_endurance
  - keywords: community, habitat, life, place
- `غ ن ي B005` — الغانية المستغنية
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, ك ذ ب, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: desire_appetite, gender, hierarchy_status, identity_personhood, marriage_genealogy, ornament_beauty, sexuality
  - keywords: adornment, beauty, desire, gender, identity, marriage, ornament, sexuality, status
- `غ ن ي B006` — الغنى والتزويج
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, ك ذ ب, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: authority_governance, family, hierarchy_status, household_community, kinship, marriage_genealogy, obligation_contract, protection_security, sexuality
  - keywords: contract, family, household, institution, kinship, marriage, protection, sexuality, status

### م و ل

- `م و ل B001` — اتخاذ المال وكثرته
  - activated_by_or_with: ء و ل, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ن ذ ر, ه د ي, و ل ي, ي س ر
  - themes: abundance_scarcity, economy, finance_debt, husbandry, provision_resource, support_dependence, wealth_property
  - keywords: economy, finance, livelihood, ownership, pastoralism, patronage, property, prosperity, resource
- `م و ل B002` — المُولة العنكبوت
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, ك ذ ب, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: animal, form_structure, language_speech, naming_classification, wildlife
  - keywords: animal, taxonomy, zoology

### ر د ي

- `ر د ي B001` — الرمي بالحجر والصخرة
  - activated_by_or_with: ء و ل, ح س ن, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: change_transition, conflict, earth_geology, force_power, protection_security, violence_warfare, weaponry
  - keywords: combat, conflict, projectile, protection, violence, weapon
- `ر د ي B002` — الترامي في العدو والقفز
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: animal, body, labor_work, motion, posture_embodiment, speed, stability_endurance, suffering_hardship
  - keywords: animal, body, exertion, locomotion, movement, speed
- `ر د ي B003` — السقوط إلى الهلاك
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ش ق و, ص ل ي, ع س ر, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: belief_revelation, danger_harm, geography_landscape, loss_absence, mortality_death, motion, proof_uncertainty
  - keywords: danger, fate, geography, uncertainty
- `ر د ي B004` — الرداء وما يلازم المنكبين
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: hierarchy_status, identity_personhood, ornament_beauty, posture_embodiment, textile_clothing
  - keywords: adornment, clothing, identity, ornament, status, textile
- `ر د ي B005` — الزيادة على القدر
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: abundance_scarcity, commerce_exchange, economy, growth_decay, hospitality_welfare, language_speech, measurement, quantity_number, rhetoric_discourse
  - keywords: abundance, economy, exchange, growth, quantity, scale
- `ر د ي B006` — المراودة والمداراة
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: desire_appetite, force_power, hospitality_welfare, politics_order, reasoning_decision, rhetoric_discourse, social_relations
  - keywords: desire, negotiation, sociality

### ه د ي

- `ه د ي B001` — دلالة بلطف إلى الطريق والحق
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, و ل ي, ي س ر
  - themes: afterlife_eschatology, belief_revelation, ethics_morality, knowledge_learning, navigation_route, orientation_direction, proof_uncertainty, religion_worship
  - keywords: belief, ethics, navigation, orientation, religion, revelation, truth
- `ه د ي B002` — جهة الأمر وسيرته وقصده
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ن ذ ر, ن و ر, و ل ي, ي س ر
  - themes: agency_action, identity_personhood, intention_character, pattern_marking, reasoning_decision
  - keywords: behavior, identity, pattern, practice
- `ه د ي B003` — المتقدم الهادي وأوائل الشيء
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, م و ل, ن و ر, و ل ي, ي س ر
  - themes: anatomy, animal, authority_governance, livestock, motion, sequence_cycle, weaponry
  - keywords: anatomy, animal, leadership, livestock, motion, sequence, weapon
- `ه د ي B004` — بعثة لطف وهدية إلى ذي مودة
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ل ظ ي, م و ل, ن و ر, و ل ي, ي س ر
  - themes: commerce_exchange, emotion, hospitality_welfare, kinship, social_relations, wealth_property
  - keywords: commerce, emotion, exchange, generosity, kinship, property, sociality
- `ه د ي B005` — الهدي المهدى إلى الحرم
  - activated_by_or_with: ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن ذ ر, ن و ر, و ل ي, ي س ر
  - themes: economy, livestock, pilgrimage_sacrifice, religion_worship, ritual, travel
  - keywords: economy, livestock, religion, ritual, sacrifice, sanctuary, worship
- `ه د ي B006` — العروس المهدية إلى زوجها
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, و ل ي, ي س ر
  - themes: change_transition, family, gender, household_community, kinship, marriage_genealogy, motion, ritual
  - keywords: family, gender, household, kinship, marriage, transfer, transition
- `ه د ي B007` — هدي الحرمة والأسير
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, و ل ي, ي س ر
  - themes: authority_governance, control_restraint, law, obligation_contract, protection_security, religion_worship, violence_warfare
  - keywords: authority, law, protection, refuge, sanctuary, security, warfare
- `ه د ي B008` — مشي التهادي مع الاعتماد والتمايل
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, م و ل, ن ذ ر, ن و ر, و ل ي, ي س ر
  - themes: animal, body, disease_injury, gender, motion, posture_embodiment, support_dependence, transport
  - keywords: animal, assistance, body, gender, locomotion, motion, posture, transport
- `ه د ي B009` — الهداء البليد الضعيف
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, و ل ي, ي س ر
  - themes: body, capacity_ability, cognition, honor_shame, intention_character, value_quality
  - keywords: body, character, cognition, temperament
- `ه د ي B010` — هدي السكون وحسن الهيئة
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, و ل ي, ي س ر
  - themes: body, control_restraint, emotion, ethics_morality, intention_character, motion, ornament_beauty, visual_appearance
  - keywords: aesthetics, appearance, body, discipline, emotion, ethics, motion, movement
- `ه د ي B011` — إهداء الشعر ومهاداته
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن ذ ر, ن و ر, و ل ي, ي س ر
  - themes: agency_action, commerce_exchange, communication, conflict, honor_shame, support_dependence, writing_text
  - keywords: communication, conflict, exchange, patronage, performance

### ء خ ر

- `ء خ ر B001` — الآخرية بعد الأول أو غيره
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: identity_personhood, loss_absence, measurement, naming_classification, reasoning_decision, sequence_cycle, social_relations
  - keywords: absence, classification, comparison, distance, identity, relation, sequence
- `ء خ ر B002` — التأخير إلى وقت لاحق
  - activated_by_or_with: ء و ل, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: calendar_season, commerce_exchange, intention_character, obligation_contract, sequence_cycle, time
  - keywords: commerce, duration, obligation, process, time
- `ء خ ر B003` — المؤخر والخلف
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, ك ذ ب, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: anatomy, animal, body, boundary, orientation_direction, space, transport
  - keywords: anatomy, animal, body, orientation, space
- `ء خ ر B004` — الدار الآخرة
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### ء و ل

- `ء و ل B001` — ابتداء الشيء وتقدمه
  - activated_by_or_with: ء خ ر, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ه د ي, و ل ي, ي س ر
  - themes: hierarchy_status, motion, orientation_direction, sequence_cycle, time
  - keywords: hierarchy, motion, orientation, process, sequence
- `ء و ل B002` — رجوع الشيء إلى مآله وعاقبته
  - activated_by_or_with: ء خ ر, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: belief_revelation, change_transition, intention_character, language_speech, motion, reasoning_decision
  - keywords: transformation, transition
- `ء و ل B003` — آل الرجل من يرجع إليهم ويرجعون إليه
  - activated_by_or_with: ء خ ر, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: household_community, identity_personhood, kinship, marriage_genealogy, social_relations, support_dependence
  - keywords: community, household, identity, kinship, patronage, sociality
- `ء و ل B004` — إيالة الأمر بإصلاحه وسياسته
  - activated_by_or_with: ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: authority_governance, change_transition, craft, economy, politics_order, protection_security
  - keywords: authority, economy, governance, leadership, order, politics, stewardship
- `ء و ل B005` — خثور السائل وانعقاده في آخر أمره
  - activated_by_or_with: ء خ ر, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: change_transition, food_nutrition, material, physiology, sequence_cycle, substance_texture
  - keywords: chemistry, food, material, process, texture, transformation
- `ء و ل B006` — الشخص المترائي والطرف الظاهر
  - activated_by_or_with: ء خ ر, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: boundary, form_structure, geography_landscape, orientation_direction, perception, terrain_desert, visual_appearance
  - keywords: appearance, boundary, landscape, morphology, optics, orientation, perception, topography, visibility
- `ء و ل B007` — آلة الحال التي يكون عليها الشيء
  - activated_by_or_with: ء خ ر, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: abundance_scarcity, cognition, grammar_expression, hierarchy_status, naming_classification, rhetoric_discourse, value_quality
  - keywords: classification, evaluation, quality, status
- `ء و ل B008` — الآلة الحاملة أو الأداة
  - activated_by_or_with: ء خ ر, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: architecture_construction, material, mortality_death, ritual, support_dependence, tools_equipment, transport, value_quality
  - keywords: material, shelter, support, technology, tool, transport, utility
- `ء و ل B009` — الأيل الذي يأوي إلى الجبل
  - activated_by_or_with: ء خ ر, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: animal, geography_landscape, habitat_ecology, protection_security, terrain_desert, wildlife
  - keywords: habitat, mountain, refuge, security, topography, zoology
- `ء و ل B010` — الإيال وعاء الشراب حتى يجود
  - activated_by_or_with: ء خ ر, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ه د ي, و ل ي, ي س ر
  - themes: cooking_drink, craft, life_stage_aging, stability_endurance, time, value_quality
  - keywords: craft, maturation, quality, time
- `ء و ل B011` — التأويل اسم بقلة معزول
  - activated_by_or_with: ء خ ر, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: agriculture, animal, food_nutrition, habitat_ecology, husbandry, naming_classification, pasture_forage, plant_vegetation
  - keywords: agriculture, botany, ecology, lexicography, pasture, taxonomy

### ن ذ ر

- `ن ذ ر B001` — إنذار يخوف فيوقظ الحذر
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: capacity_ability, cognition, communication, danger_harm, protection_security
  - keywords: communication, danger, protection, risk, security
- `ن ذ ر B002` — إلزام النفس بما لم يكن واجبا
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: agency_action, ethics_morality, justice_judgment, obligation_contract, pilgrimage_sacrifice, religion_worship, ritual
  - keywords: agency, contract, duty, ethics, religion, ritual, sacrifice
- `ن ذ ر B003` — جرح له عقل واجب
  - activated_by_or_with: ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: disease_injury, finance_debt, health_medicine, justice_judgment, law, violence_warfare
  - keywords: finance, justice, law, medicine, violence

### ن و ر

- `ن و ر B001` — الضياء والإضاءة
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ه د ي, و ل ي, ي س ر
  - themes: belief_revelation, perception, proof_uncertainty
  - keywords: guidance, optics, perception, revelation, visibility
- `ن و ر B002` — النار المتقدة والسمة بها
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ه د ي, و ل ي, ي س ر
  - themes: animal, fire_heat, identity_personhood, livestock, naming_classification, pattern_marking
  - keywords: animal, combustion, fire, heat, identity, livestock, marking
- `ن و ر B003` — تنور النار من بعيد
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ن ذ ر, ه د ي, و ل ي, ي س ر
  - themes: communication, knowledge_learning, navigation_route, perception, protection_security, travel
  - keywords: navigation, perception, travel
- `ن و ر B004` — نور الشجر وزهره
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ه د ي, و ل ي, ي س ر
  - themes: calendar_season, change_transition, growth_decay, ornament_beauty, plant_vegetation, reproduction_birth
  - keywords: beauty, botany, fertility, growth, ornament, season
- `ن و ر B005` — المنار والمنارة الظاهرة
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ه د ي, و ل ي, ي س ر
  - themes: architecture_construction, belief_revelation, boundary, communication, geography_landscape, navigation_route, religion_worship
  - keywords: architecture, boundary, guidance, navigation, worship
- `ن و ر B006` — النِّفار وقلة الثبات
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, م و ل, ن ذ ر, ه د ي, و ل ي, ي س ر
  - themes: agency_action, animal, control_restraint, ethics_morality, intention_character, sexuality
  - keywords: animal, avoidance, behavior, ethics, sexuality, temperament
- `ن و ر B007` — النائرة بين القوم
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ه د ي, و ل ي, ي س ر
  - themes: conflict, emotion, kinship, politics_order, social_relations, violence_warfare
  - keywords: conflict, emotion, politics, violence
- `ن و ر B008` — دخان الوشم والكحل
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ه د ي, و ل ي, ي س ر
  - themes: body, fire_heat, health_medicine, ornament_beauty, ritual, substance_texture, writing_text
  - keywords: adornment, body, cosmetic, cosmetics, inscription, medicine, ritual
- `ن و ر B009` — النُّورَة المطلية
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ه د ي, و ل ي, ي س ر
  - themes: body, ornament_beauty, substance_texture
  - keywords: body, chemistry, cosmetic, cosmetics
- `ن و ر B010` — التلبيس على الغير
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ه د ي, و ل ي, ي س ر
  - themes: cognition, communication, deception_corruption, knowledge_learning, perception, proof_uncertainty, rhetoric_discourse
  - keywords: cognition, communication, deception, epistemology, perception, uncertainty
- `ن و ر B011` — وضوح النِّير وبروزه
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ه د ي, و ل ي, ي س ر
  - themes: agriculture, navigation_route, pattern_marking, perception, space, textile_clothing, tools_equipment, transport
  - keywords: agriculture, equipment, marking, textile, topology, transport, visibility

### ل ظ ي

- `ل ظ ي B001` — اللظى لهب خالص متوقد
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: change_transition, danger_harm, fire_heat, force_power
  - keywords: combustion, danger, destruction, heat, transformation
- `ل ظ ي B002` — لظى اسم للنار وجهنم
  - activated_by_or_with: ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: afterlife_eschatology, fire_heat, justice_judgment, punishment_sanction, religion_worship, suffering_hardship
  - keywords: afterlife, fire, judgment, punishment, religion
- `ل ظ ي B003` — التلظي من شدة الغضب
  - activated_by_or_with: ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: cognition, conflict, emotion, fire_heat, rhetoric_discourse, violence_warfare
  - keywords: conflict, emotion, heat, psychology
- `ل ظ ي B004` — اللظى شدة الحر
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ن و ر, و ل ي, ي س ر
  - themes: containment_access, fire_heat, habitat_ecology, suffering_hardship, terrain_desert, weather_climate
  - keywords: climate, desert, weather

### ص ل ي

- `ص ل ي B001` — الصلاة عبادة لازمة
  - activated_by_or_with: ء و ل, ش ق و, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: authority_governance, control_restraint, household_community, religion_worship, ritual
  - keywords: community, devotion, discipline, obedience, religion, ritual, worship
- `ص ل ي B002` — الدعاء والبركة والرحمة
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي
  - themes: belief_revelation, communication, ethics_morality, religion_worship, social_relations
  - keywords: communication
- `ص ل ي B003` — ملاقاة النار وحرها
  - activated_by_or_with: ح س ن, ر د ي, ش ق و, ع س ر, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: afterlife_eschatology, danger_harm, fire_heat, justice_judgment, punishment_sanction, suffering_hardship
  - keywords: afterlife, destruction, fire, heat, punishment, suffering, trial
- `ص ل ي B004` — إيقاد الصلاء وتسوية الشيء بالنار
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: change_transition, cooking_drink, craft, fire_heat, material
  - keywords: combustion, craft, fire, heat, material, transformation
- `ص ل ي B005` — المَصالي أشراك وفخوخ
  - activated_by_or_with: ء و ل, ر د ي, ش ق و, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: agriculture, control_restraint, habitat_ecology, protection_security, tools_equipment, wildlife
  - keywords: agriculture, control, predation, security, technology
- `ص ل ي B006` — الصَّلا موضع الظهر والذنب
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ع س ر, غ ن ي, ك ذ ب, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: anatomy, animal, body, kinship, motion, place_location, reproduction_birth
  - keywords: anatomy, animal, birth, body, kinship, location, locomotion, reproduction, zoology
- `ص ل ي B007` — المصلي يتلو السابق
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ش ق و, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: conflict, hierarchy_status, motion, politics_order, reasoning_decision, recreation_sport, sequence_cycle
  - keywords: comparison, competition, hierarchy, motion, order, pursuit, rank, sequence, sport
- `ص ل ي B008` — الصلوات مواضع عبادة
  - activated_by_or_with: ء و ل, ش ق و, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: architecture_construction, authority_governance, household_community, religion_worship
  - keywords: architecture, community, institution, religion, sanctuary, worship
- `ص ل ي B009` — الصلاية حجر يدق عليه
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ع س ر, غ ن ي, ك ذ ب, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: agency_action, craft, earth_geology, household_community, material, substance_texture, tools_equipment
  - keywords: craft, material, texture, tool
- `ص ل ي B010` — الصِّليان نبت ترعاه الإبل
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: agriculture, animal, food_nutrition, habitat_ecology, husbandry, pasture_forage, plant_vegetation, terrain_desert
  - keywords: agriculture, animal, botany, desert, ecology, food, pastoralism, pasture

### ش ق و

- `ش ق و B001` — الشقاء ضد السعادة
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ش ق و B002` — مشقة العسر والمعاناة
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: conflict, control_restraint, justice_judgment, labor_work, social_relations, stability_endurance, suffering_hardship
  - keywords: conflict, discipline, endurance, relation, struggle, suffering, trial
- `ش ق و B003` — الغلبة في المشاقاة
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: conflict, force_power, hierarchy_status, reasoning_decision
  - keywords: competition, conflict, hierarchy, power, struggle
- `ش ق و B004` — شاقي الجبل الطالع الطويل
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ص ل ي, ع س ر, ك ذ ب, ل ظ ي, ن و ر, ه د ي, و ل ي, ي س ر
  - themes: architecture_construction, containment_access, geography_landscape, motion, navigation_route, orientation_direction, terrain_desert, travel
  - keywords: landscape, mountain, movement, shelter, travel

### و ل ي

- `و ل ي B001` — قرب ودنو بلا فاصل
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ن و ر, ه د ي, ي س ر
  - themes: boundary, place_location, social_relations, space
  - keywords: boundary, location, relation, space, topology
- `و ل ي B002` — تتابع شيء بعد شيء
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ن و ر, ه د ي, ي س ر
  - themes: politics_order, sequence_cycle, stability_endurance, time
  - keywords: continuity, order, process, sequence, time
- `و ل ي B003` — تولي الأمر والقيام عليه
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ه د ي, ي س ر
  - themes: authority_governance, force_power, hospitality_welfare, law, obligation_contract
  - keywords: governance, institution, law, power, stewardship
- `و ل ي B004` — محبة ونصرة وموالاة
  - activated_by_or_with: ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن ذ ر, ن و ر, ه د ي, ي س ر
  - themes: belief_revelation, conflict, emotion, household_community, religion_worship, support_dependence, trust_loyalty
  - keywords: community, conflict, devotion, emotion, support
- `و ل ي B005` — ولاء قرابة وعتق وجوار
  - activated_by_or_with: ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, م و ل, ن ذ ر, ن و ر, ه د ي, ي س ر
  - themes: control_restraint, family, hierarchy_status, household_community, law, place_location, support_dependence, wealth_property
  - keywords: community, family, law, patronage, status
- `و ل ي B006` — تولية الوجه والإقبال
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ن ذ ر, ن و ر, ه د ي, ي س ر
  - themes: authority_governance, memory_attention, motion, obligation_contract, orientation_direction, perception, social_relations
  - keywords: attention, consent, motion, movement, obedience, orientation, perception, relation
- `و ل ي B007` — الإدبار والإعراض
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ن ذ ر, ن و ر, ه د ي, ي س ر
  - themes: authority_governance, communication, control_restraint, loss_absence, measurement, memory_attention, motion, social_relations
  - keywords: absence, attention, avoidance, distance, movement, obedience
- `و ل ي B008` — الأولوية والاستحقاق
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن ذ ر, ن و ر, ه د ي, ي س ر
  - themes: ethics_morality, hierarchy_status, justice_judgment, law, provision_resource, value_quality
  - keywords: allocation, hierarchy, justice, rank, value
- `و ل ي B009` — أولى لك تهديد ووعيد
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `و ل ي B010` — مطر يلي الوسمي
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, ك ذ ب, ل ظ ي, ن و ر, ي س ر
  - themes: agriculture, calendar_season, geography_landscape, reproduction_birth, weather_climate
  - keywords: agriculture, climate, fertility, season, weather
- `و ل ي B011` — ولية تحت الرحل
  - activated_by_or_with: ء خ ر, ء و ل, ر د ي, ش ق و, ص ل ي, ع س ر, ك ذ ب, م و ل, ن و ر, ه د ي, ي س ر
  - themes: animal, textile_clothing, tools_equipment, transport, travel
  - keywords: animal, equipment, textile, transport, travel
- `و ل ي B012` — استيلاء وبلوغ غاية
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, م و ل, ن و ر, ه د ي, ي س ر
  - themes: change_transition, conflict, control_restraint, force_power, motion, value_quality, wealth_property
  - keywords: achievement, competition, completion, control, movement, ownership, power
- `و ل ي B013` — إيلاء وإسناد معروف أو شر
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, ل ظ ي, ن ذ ر, ن و ر, ه د ي, ي س ر
  - themes: agency_action, commerce_exchange, danger_harm, ethics_morality, hospitality_welfare, motion
  - keywords: agency, exchange, morality, transfer
- `و ل ي B014` — تولية البيع
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ع س ر, غ ن ي, ك ذ ب, م و ل, ن ذ ر, ه د ي, ي س ر
  - themes: commerce_exchange, obligation_contract, value_quality, wealth_property
  - keywords: commerce, contract, exchange, ownership, property, value
- `و ل ي B015` — موالاة صغار النعم عن كبارها
  - activated_by_or_with: ء خ ر, ء و ل, ح س ن, ر د ي, ش ق و, ص ل ي, ع س ر, غ ن ي, ك ذ ب, م و ل, ن و ر, ه د ي, ي س ر
  - themes: agriculture, animal, boundary, control_restraint, growth_decay, husbandry, knowledge_learning, life_stage_aging
  - keywords: agriculture, animal, discipline, growth, husbandry, maturation, training
- `و ل ي B016` — ولي الرطب وتولى إذا هاج
  - activated_by_or_with: ء و ل, ح س ن, ر د ي, ص ل ي, ك ذ ب, ن و ر, ه د ي, ي س ر
  - themes: agriculture, growth_decay, life_stage_aging, plant_vegetation, substance_texture, visual_appearance
  - keywords: agriculture, botany, maturation

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
