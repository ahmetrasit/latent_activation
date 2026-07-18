# v11 Activation Packet — S92:1-8

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_1: وَٱلَّيْلِ إِذَا يَغْشَىٰ
- verse_2: وَٱلنَّهَارِ إِذَا تَجَلَّىٰ
- verse_3: وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ
- verse_4: إِنَّ سَعْيَكُمْ لَشَتَّىٰ
- verse_5: فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ
- verse_6: وَصَدَّقَ بِٱلْحُسْنَىٰ
- verse_7: فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ
- verse_8: وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ل ي ل → غ ش و → ن ه ر → ج ل و → خ ل ق → ذ ك ر → ء ن ث → س ع ي → ش ت ت → ع ط و → و ق ي → ص د ق → ح س ن → ي س ر → ب خ ل → غ ن ي

## Branch inventory summary

- ل ي ل: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- غ ش و: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن ه ر: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ج ل و: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- خ ل ق: 12 branches (11 with Qnet bridge-theme nodes; 1 Furūq-only)
- ذ ك ر: 9 branches (7 with Qnet bridge-theme nodes; 2 Furūq-only)
- ء ن ث: 8 branches (7 with Qnet bridge-theme nodes; 1 Furūq-only)
- س ع ي: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ش ت ت: 3 branches (3 with Qnet bridge-theme nodes; 0 Furūq-only)
- ع ط و: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- و ق ي: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص د ق: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- ح س ن: 5 branches (4 with Qnet bridge-theme nodes; 1 Furūq-only)
- ي س ر: 11 branches (11 with Qnet bridge-theme nodes; 0 Furūq-only)
- ب خ ل: 1 branches (1 with Qnet bridge-theme nodes; 0 Furūq-only)
- غ ن ي: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)

## QAC-first root resolution audit

- ل ي ل | qac_keys=ليل | status=resolved | matches=root_001392
- غ ش و | qac_keys=غشو | status=resolved | matches=root_001088
- ن ه ر | qac_keys=نهر | status=resolved | matches=root_001559
- ج ل و | qac_keys=جلو | status=resolved | matches=root_000256
- خ ل ق | qac_keys=خلق | status=resolved | matches=root_000434
- ذ ك ر | qac_keys=ذكر | status=resolved | matches=root_000516
- ء ن ث | qac_keys=ءنث | status=resolved | matches=root_000058
- س ع ي | qac_keys=سعي | status=resolved | matches=root_000709
- ش ت ت | qac_keys=شتت | status=resolved | matches=root_000775
- ع ط و | qac_keys=عطو | status=resolved | matches=root_001028
- و ق ي | qac_keys=وقي | status=resolved | matches=root_001677
- ص د ق | qac_keys=صدق | status=resolved | matches=root_000852
- ح س ن | qac_keys=حسن | status=resolved | matches=root_000323
- ي س ر | qac_keys=يسر | status=resolved | matches=root_001694
- ب خ ل | qac_keys=بخل | status=resolved | matches=root_000089
- غ ن ي | qac_keys=غني | status=resolved | matches=root_001110

## Top candidate bridges

- `ذ ك ر B001` ↔ `ء ن ث B001` | score_hint=36 | discovery_hint=16 | themes=body, gender, kinship, physiology, reproduction_birth, sexuality | keywords=biology, body, gender, kinship, reproduction, sex | q2=—
- `ي س ر B003` ↔ `غ ن ي B001` | score_hint=28 | discovery_hint=14 | themes=abundance_scarcity, economy, hierarchy_status, provision_resource | keywords=abundance, economy, provision, resource, status | q2=—
- `ل ي ل B001` ↔ `ن ه ر B002` | score_hint=26 | discovery_hint=14 | themes=light_darkness, reasoning_decision, sequence_cycle, sky_astronomy, time | keywords=astronomy, contrast, cycle, time | q2=—
- `غ ش و B004` ↔ `ء ن ث B001` | score_hint=26 | discovery_hint=16 | themes=body, kinship, posture_embodiment, reproduction_birth, sexuality | keywords=body, embodiment, kinship, reproduction | q2=—
- `ص د ق B007` ↔ `غ ن ي B006` | score_hint=25 | discovery_hint=18 | themes=family, kinship, marriage_genealogy, obligation_contract | keywords=contract, family, kinship, marriage | q2=—
- `ج ل و B006` ↔ `ذ ك ر B004` | score_hint=24 | discovery_hint=14 | themes=communication, honor_shame, language_speech, social_relations | keywords=communication, language, reputation, society | q2=—
- `ج ل و B006` ↔ `ذ ك ر B007` | score_hint=24 | discovery_hint=14 | themes=hierarchy_status, honor_shame, memory_attention, social_relations | keywords=memory, reputation, society, status | q2=—
- `ذ ك ر B002` ↔ `ء ن ث B002` | score_hint=24 | discovery_hint=15 | themes=danger_harm, force_power, material, weaponry | keywords=force, material, strength, weapon | q2=—
- `ء ن ث B001` ↔ `ي س ر B011` | score_hint=24 | discovery_hint=15 | themes=gender, identity_personhood, kinship, physiology | keywords=gender, identity, kinship, life | q2=—
- `ن ه ر B005` ↔ `و ق ي B005` | score_hint=22 | discovery_hint=14 | themes=animal, naming_classification, wildlife | keywords=animal, taxonomy, wildlife, zoology | q2=—
- `ع ط و B006` ↔ `ي س ر B005` | score_hint=22 | discovery_hint=14 | themes=authority_governance, capacity_ability, control_restraint, motion, substance_texture | keywords=control, motion, obedience | q2=—
- `خ ل ق B010` ↔ `ء ن ث B007` | score_hint=20 | discovery_hint=14 | themes=ornament_beauty, perception | keywords=adornment, cosmetic, cosmetics, fragrance | q2=—
- `غ ش و B004` ↔ `ذ ك ر B001` | score_hint=20 | discovery_hint=15 | themes=body, kinship, reproduction_birth, sexuality | keywords=body, kinship, reproduction | q2=—
- `ج ل و B009` ↔ `ع ط و B003` | score_hint=20 | discovery_hint=13 | themes=hospitality_welfare, household_community, kinship, obligation_contract | keywords=household, kinship, obligation | q2=—
- `ج ل و B009` ↔ `غ ن ي B006` | score_hint=20 | discovery_hint=13 | themes=household_community, kinship, marriage_genealogy, obligation_contract | keywords=household, kinship, marriage | q2=—
- `ذ ك ر B004` ↔ `ص د ق B001` | score_hint=19 | discovery_hint=16 | themes=communication, language_speech, testimony_witness | keywords=communication, language, testimony | q2=—
- `ل ي ل B002` ↔ `س ع ي B001` | score_hint=18 | discovery_hint=12 | themes=motion, ritual, travel | keywords=mobility, ritual, travel | q2=—
- `ل ي ل B004` ↔ `ن ه ر B007` | score_hint=18 | discovery_hint=14 | themes=culture_tradition, identity_personhood, naming_classification | keywords=culture, identity, onomastics | q2=—
- `غ ش و B004` ↔ `ء ن ث B003` | score_hint=18 | discovery_hint=16 | themes=body, reproduction_birth, sexuality | keywords=body, reproduction, sexuality | q2=—
- `غ ش و B004` ↔ `غ ن ي B006` | score_hint=18 | discovery_hint=14 | themes=kinship, marriage_genealogy, sexuality | keywords=kinship, marriage, sexuality | q2=—
- `ن ه ر B005` ↔ `ذ ك ر B001` | score_hint=18 | discovery_hint=14 | themes=naming_classification, physiology, reproduction_birth | keywords=biology, reproduction, taxonomy | q2=—
- `ن ه ر B007` ↔ `ح س ن B004` | score_hint=18 | discovery_hint=14 | themes=geography_landscape, naming_classification, sky_astronomy | keywords=astronomy, geography, onomastics | q2=—
- `ن ه ر B007` ↔ `ي س ر B010` | score_hint=18 | discovery_hint=14 | themes=geography_landscape, identity_personhood, naming_classification | keywords=geography, identity, onomastics | q2=—
- `ذ ك ر B008` ↔ `ص د ق B007` | score_hint=18 | discovery_hint=14 | themes=law, obligation_contract, wealth_property | keywords=contract, law, property | q2=—
- `س ع ي B006` ↔ `ح س ن B002` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, hospitality_welfare, justice_judgment | keywords=charity, ethics, justice | q2=—
- `س ع ي B008` ↔ `ع ط و B007` | score_hint=18 | discovery_hint=13 | themes=agency_action, conflict, hierarchy_status | keywords=competition, conflict, victory | q2=—
- `ش ت ت B002` ↔ `ي س ر B008` | score_hint=18 | discovery_hint=14 | themes=anatomy, body, pattern_marking | keywords=anatomy, body, pattern | q2=—
- `ي س ر B011` ↔ `غ ن ي B005` | score_hint=18 | discovery_hint=14 | themes=gender, hierarchy_status, identity_personhood | keywords=gender, identity, status | q2=—
- `غ ش و B003` ↔ `س ع ي B001` | score_hint=16 | discovery_hint=12 | themes=motion, travel | keywords=mobility, movement, travel | q2=—
- `غ ش و B007` ↔ `ن ه ر B005` | score_hint=16 | discovery_hint=13 | themes=animal, naming_classification | keywords=animal, taxonomy, zoology | q2=—
- `غ ش و B007` ↔ `و ق ي B005` | score_hint=16 | discovery_hint=13 | themes=animal, naming_classification | keywords=animal, taxonomy, zoology | q2=—
- `ن ه ر B002` ↔ `ج ل و B001` | score_hint=16 | discovery_hint=12 | themes=light_darkness, perception | keywords=illumination, light, visibility | q2=—
- `ج ل و B002` ↔ `خ ل ق B003` | score_hint=16 | discovery_hint=13 | themes=ornament_beauty, perception | keywords=beauty, perception, vision | q2=—
- `ع ط و B002` ↔ `ب خ ل B001` | score_hint=16 | discovery_hint=13 | themes=hospitality_welfare, wealth_property | keywords=charity, ownership, property | q2=—
- `ع ط و B005` ↔ `غ ن ي B002` | score_hint=16 | discovery_hint=15 | themes=commerce_exchange, support_dependence | keywords=dependence, dependency, exchange | q2=—
- `ح س ن B002` ↔ `ب خ ل B001` | score_hint=16 | discovery_hint=12 | themes=ethics_morality, hospitality_welfare | keywords=charity, ethics, virtue | q2=—
- `ل ي ل B001` ↔ `ج ل و B007` | score_hint=16 | discovery_hint=12 | themes=habitat_ecology, light_darkness, sky_astronomy, time | keywords=environment, time | q2=—
- `ن ه ر B002` ↔ `ج ل و B007` | score_hint=16 | discovery_hint=13 | themes=light_darkness, perception, sky_astronomy, time | keywords=light, time | q2=—
- `ج ل و B001` ↔ `ص د ق B001` | score_hint=16 | discovery_hint=10 | themes=belief_revelation, communication, knowledge_learning, proof_uncertainty | keywords=communication, evidence | q2=—
- `ج ل و B005` ↔ `ي س ر B008` | score_hint=16 | discovery_hint=14 | themes=anatomy, body, health_medicine, identity_personhood | keywords=body, identity | q2=—
- `ج ل و B006` ↔ `ذ ك ر B009` | score_hint=16 | discovery_hint=12 | themes=cognition, communication, knowledge_learning, memory_attention | keywords=communication, memory | q2=—
- `ذ ك ر B001` ↔ `ء ن ث B003` | score_hint=16 | discovery_hint=14 | themes=body, naming_classification, reproduction_birth, sexuality | keywords=body, reproduction | q2=—
- `ذ ك ر B001` ↔ `ي س ر B011` | score_hint=16 | discovery_hint=12 | themes=gender, kinship, naming_classification, physiology | keywords=gender, kinship | q2=—
- `ء ن ث B002` ↔ `ص د ق B002` | score_hint=16 | discovery_hint=13 | themes=ethics_morality, force_power, material, weaponry | keywords=strength, weaponry | q2=—
- `ل ي ل B003` ↔ `ن ه ر B002` | score_hint=14 | discovery_hint=12 | themes=calendar_season, sequence_cycle, time | keywords=calendar, time | q2=—
- `ل ي ل B004` ↔ `ي س ر B010` | score_hint=14 | discovery_hint=13 | themes=identity_personhood, naming_classification, rhetoric_discourse | keywords=identity, onomastics | q2=—
- `ل ي ل B004` ↔ `ي س ر B011` | score_hint=14 | discovery_hint=13 | themes=gender, identity_personhood, naming_classification | keywords=gender, identity | q2=—
- `غ ش و B006` ↔ `ن ه ر B006` | score_hint=14 | discovery_hint=12 | themes=conflict, control_restraint, violence_warfare | keywords=conflict, violence | q2=—
- `غ ش و B007` ↔ `ش ت ت B002` | score_hint=14 | discovery_hint=12 | themes=anatomy, pattern_marking, visual_appearance | keywords=anatomy, appearance | q2=—
- `ن ه ر B001` ↔ `خ ل ق B011` | score_hint=14 | discovery_hint=11 | themes=earth_geology, geography_landscape, water_hydrology | keywords=hydrology, landscape | q2=—
- `ن ه ر B004` ↔ `ذ ك ر B004` | score_hint=14 | discovery_hint=12 | themes=communication, language_speech, social_relations | keywords=communication, speech | q2=—
- `ن ه ر B004` ↔ `ص د ق B001` | score_hint=14 | discovery_hint=11 | themes=communication, ethics_morality, language_speech | keywords=communication, ethics | q2=—
- `ن ه ر B006` ↔ `س ع ي B004` | score_hint=14 | discovery_hint=12 | themes=conflict, deception_corruption, violence_warfare | keywords=conflict, violence | q2=—
- `ج ل و B003` ↔ `ء ن ث B008` | score_hint=14 | discovery_hint=12 | themes=kinship, marriage_genealogy, social_relations | keywords=kinship, society | q2=—
- `ج ل و B003` ↔ `ص د ق B007` | score_hint=14 | discovery_hint=12 | themes=gender, kinship, marriage_genealogy | keywords=gender, kinship | q2=—
- `ج ل و B003` ↔ `غ ن ي B005` | score_hint=14 | discovery_hint=12 | themes=gender, marriage_genealogy, ornament_beauty | keywords=beauty, gender | q2=—
- `ج ل و B005` ↔ `ء ن ث B001` | score_hint=14 | discovery_hint=14 | themes=body, identity_personhood, physiology | keywords=body, identity | q2=—
- `ج ل و B005` ↔ `ش ت ت B002` | score_hint=14 | discovery_hint=13 | themes=anatomy, body, visual_appearance | keywords=appearance, body | q2=—
- `ج ل و B006` ↔ `خ ل ق B004` | score_hint=14 | discovery_hint=13 | themes=cognition, identity_personhood, social_relations | keywords=identity, society | q2=—
- `ج ل و B006` ↔ `ذ ك ر B003` | score_hint=14 | discovery_hint=12 | themes=cognition, knowledge_learning, memory_attention | keywords=knowledge, memory | q2=—
- `ج ل و B006` ↔ `ص د ق B001` | score_hint=14 | discovery_hint=11 | themes=communication, knowledge_learning, language_speech | keywords=communication, language | q2=—
- `ج ل و B006` ↔ `ص د ق B003` | score_hint=14 | discovery_hint=13 | themes=hierarchy_status, honor_shame, identity_personhood | keywords=identity, status | q2=—
- `ج ل و B009` ↔ `ص د ق B007` | score_hint=14 | discovery_hint=12 | themes=kinship, marriage_genealogy, obligation_contract | keywords=kinship, marriage | q2=—
- `خ ل ق B003` ↔ `ش ت ت B002` | score_hint=14 | discovery_hint=12 | themes=anatomy, ornament_beauty, visual_appearance | keywords=anatomy, beauty | q2=—
- `خ ل ق B003` ↔ `ح س ن B001` | score_hint=14 | discovery_hint=11 | themes=ornament_beauty, perception, visual_appearance | keywords=aesthetics, perception | q2=—
- `ذ ك ر B007` ↔ `س ع ي B006` | score_hint=14 | discovery_hint=12 | themes=hierarchy_status, honor_shame, social_relations | keywords=honor, reputation | q2=—
- `ذ ك ر B007` ↔ `ص د ق B003` | score_hint=14 | discovery_hint=12 | themes=hierarchy_status, honor_shame, value_quality | keywords=honor, status | q2=—
- `ء ن ث B001` ↔ `غ ن ي B005` | score_hint=14 | discovery_hint=13 | themes=gender, identity_personhood, sexuality | keywords=gender, identity | q2=—
- `ء ن ث B008` ↔ `ي س ر B011` | score_hint=14 | discovery_hint=13 | themes=identity_personhood, kinship, naming_classification | keywords=identity, kinship | q2=—
- `س ع ي B007` ↔ `غ ن ي B005` | score_hint=14 | discovery_hint=13 | themes=gender, hierarchy_status, sexuality | keywords=gender, sexuality | q2=—
- `ش ت ت B002` ↔ `ي س ر B004` | score_hint=14 | discovery_hint=13 | themes=anatomy, body, space | keywords=anatomy, body | q2=—
- `ع ط و B003` ↔ `غ ن ي B006` | score_hint=14 | discovery_hint=12 | themes=household_community, kinship, obligation_contract | keywords=household, kinship | q2=—
- `ص د ق B006` ↔ `غ ن ي B001` | score_hint=14 | discovery_hint=12 | themes=abundance_scarcity, economy, provision_resource | keywords=economy, poverty | q2=—
- `ي س ر B001` ↔ `غ ن ي B002` | score_hint=14 | discovery_hint=12 | themes=capacity_ability, change_transition, support_dependence | keywords=capacity, support | q2=—
- `ي س ر B011` ↔ `غ ن ي B006` | score_hint=14 | discovery_hint=12 | themes=hierarchy_status, household_community, kinship | keywords=kinship, status | q2=—
- `ن ه ر B003` ↔ `خ ل ق B012` | score_hint=14 | discovery_hint=12 | themes=anatomy, containment_access, control_restraint, disease_injury, substance_texture | keywords=anatomy | q2=—
- `غ ش و B007` ↔ `ي س ر B006` | score_hint=13 | discovery_hint=16 | themes=animal, livestock | keywords=animal, livestock | q2=—
- `ل ي ل B002` ↔ `غ ش و B003` | score_hint=12 | discovery_hint=12 | themes=motion, travel | keywords=mobility, travel | q2=—
- `ل ي ل B004` ↔ `ء ن ث B001` | score_hint=12 | discovery_hint=12 | themes=gender, identity_personhood | keywords=gender, identity | q2=—
- `ل ي ل B004` ↔ `غ ن ي B005` | score_hint=12 | discovery_hint=13 | themes=gender, identity_personhood | keywords=gender, identity | q2=—

## Per-root candidate activations

### ل ي ل

- `ل ي ل B001` — الليل خلاف النهار وظلمته
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, ش ت ت, غ ش و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: concealment_disclosure, habitat_ecology, light_darkness, orientation_direction, reasoning_decision, sequence_cycle, sky_astronomy, time
  - keywords: astronomy, contrast, cycle, environment, polarity, time
- `ل ي ل B002` — مزاولة الأمر في الليل
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, س ع ي, ش ت ت, ع ط و, غ ش و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: calendar_season, commerce_exchange, labor_work, motion, ritual, time, travel
  - keywords: commerce, labor, mobility, ritual, time, travel
- `ل ي ل B003` — الليلة القريبة من اليوم
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: boundary, calendar_season, grammar_expression, language_speech, orientation_direction, place_location, sequence_cycle, time
  - keywords: boundary, calendar, orientation, proximity, speech, time
- `ل ي ل B004` — التسمية بليلى
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, غ ش و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: culture_tradition, gender, identity_personhood, naming_classification, rhetoric_discourse
  - keywords: culture, gender, identity, onomastics

### غ ش و

- `غ ش و B001` — غطاء يعلو الشيء ويستره
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, س ع ي, ش ت ت, ص د ق, ع ط و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: boundary, concealment_disclosure, perception, protection_security, storage_vessels, surface_shape, textile_clothing, tools_equipment
  - keywords: barrier, equipment, perception, protection, surface, textile
- `غ ش و B002` — غاشية تعم وتجلل
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: afterlife_eschatology, danger_harm, disease_injury, household_community, justice_judgment, punishment_sanction, social_relations, suffering_hardship
  - keywords: punishment, society
- `غ ش و B003` — إتيان يغشى المقصود
  - activated_by_or_with: ء ن ث, ج ل و, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: motion, place_location, prayer_supplication, social_relations, travel
  - keywords: mobility, movement, petition, proximity, sociality, travel
- `غ ش و B004` — غشيان المرأة كناية عن الجماع
  - activated_by_or_with: ء ن ث, ج ل و, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ن ي, ل ي ل, ن ه ر, ي س ر
  - themes: body, containment_access, kinship, marriage_genealogy, posture_embodiment, reproduction_birth, rhetoric_discourse, sexuality
  - keywords: body, embodiment, kinship, marriage, reproduction, sexuality
- `غ ش و B005` — غشية تغطي الوعي
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ع ط و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: body, capacity_ability, cognition, danger_harm, disease_injury, health_medicine
  - keywords: body, cognition, medicine
- `غ ش و B006` — إلباس الضربة بالسوط أو السيف
  - activated_by_or_with: ء ن ث, ج ل و, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: body, conflict, control_restraint, disease_injury, punishment_sanction, suffering_hardship, violence_warfare, weaponry
  - keywords: body, coercion, combat, conflict, discipline, injury, pain, punishment, violence, weapon, weaponry
- `غ ش و B007` — بياض يغشى وجه الحيوان
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, ش ت ت, ع ط و, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: anatomy, animal, livestock, naming_classification, pattern_marking, visual_appearance
  - keywords: anatomy, animal, appearance, classification, color, livestock, marking, taxonomy, zoology

### ن ه ر

- `ن ه ر B001` — نهر يشق الأرض بماء جار
  - activated_by_or_with: ء ن ث, ح س ن, خ ل ق, ص د ق, ع ط و, غ ن ي, ي س ر
  - themes: abundance_scarcity, earth_geology, geography_landscape, water_hydrology
  - keywords: abundance, erosion, geography, hydrology, landscape
- `ن ه ر B002` — انفتاح النهار بالضياء
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, ش ت ت, غ ش و, غ ن ي, ل ي ل, ي س ر
  - themes: calendar_season, light_darkness, perception, reasoning_decision, sequence_cycle, sky_astronomy, time
  - keywords: astronomy, calendar, contrast, cycle, illumination, light, time, visibility
- `ن ه ر B003` — فتح الشيء وتوسيعه حتى يسيل أو ينفسح
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, س ع ي, ش ت ت, ع ط و, غ ش و, غ ن ي, و ق ي, ي س ر
  - themes: anatomy, change_transition, containment_access, control_restraint, disease_injury, form_structure, space, substance_texture
  - keywords: anatomy, injury, morphology, space
- `ن ه ر B004` — زجر بكلام مغلظ
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, و ق ي, ي س ر
  - themes: authority_governance, communication, conflict, control_restraint, ethics_morality, language_speech, social_relations
  - keywords: authority, communication, conflict, discipline, ethics, sociality, speech
- `ن ه ر B005` — النَّهار فرخ طير
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, ش ت ت, غ ش و, غ ن ي, ل ي ل, و ق ي, ي س ر
  - themes: animal, growth_decay, life_stage_aging, naming_classification, physiology, reproduction_birth, wildlife
  - keywords: animal, biology, growth, reproduction, taxonomy, wildlife, zoology
- `ن ه ر B006` — الدغرة والخلسة
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, و ق ي, ي س ر
  - themes: concealment_disclosure, conflict, control_restraint, deception_corruption, habitat_ecology, law, reasoning_decision, violence_warfare
  - keywords: conflict, crime, deception, violence
- `ن ه ر B007` — أعلام وأسماء خاصة
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, ش ت ت, ص د ق, غ ش و, غ ن ي, ل ي ل, و ق ي, ي س ر
  - themes: culture_tradition, geography_landscape, identity_personhood, naming_classification, sky_astronomy, water_hydrology, writing_text
  - keywords: astronomy, culture, geography, hydrology, identity, onomastics
- `ن ه ر B008` — النَّاهُور سحاب
  - activated_by_or_with: ج ل و, ح س ن, خ ل ق, ذ ك ر, ل ي ل
  - themes: sky_astronomy, water_hydrology, weather_climate
  - keywords: sky, water, weather

### ج ل و

- `ج ل و B001` — الكشف والظهور
  - activated_by_or_with: ء ن ث, ح س ن, خ ل ق, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: belief_revelation, communication, emotion, health_medicine, knowledge_learning, light_darkness, perception, proof_uncertainty
  - keywords: communication, emotion, evidence, illumination, knowledge, light, visibility
- `ج ل و B002` — الصقل والتجلية
  - activated_by_or_with: ء ن ث, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, غ ش و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: craft, health_medicine, ornament_beauty, perception, proof_uncertainty, value_quality, weaponry
  - keywords: beauty, clarity, cosmetic, craft, medicine, perception, vision, weapon
- `ج ل و B003` — جلوة العروس
  - activated_by_or_with: ء ن ث, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, ي س ر
  - themes: gender, kinship, marriage_genealogy, ornament_beauty, perception, ritual, social_relations
  - keywords: beauty, gender, kinship, ritual, sociality, society, visibility, wedding
- `ج ل و B004` — الجلاء عن الوطن
  - activated_by_or_with: ب خ ل, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, ي س ر
  - themes: household_community, law, migration_displacement, place_location, politics_order, violence_warfare
  - keywords: community, law, politics, violence
- `ج ل و B005` — انكشاف مقدّم الرأس
  - activated_by_or_with: ء ن ث, ح س ن, خ ل ق, ذ ك ر, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: anatomy, body, health_medicine, hygiene_sanitation, identity_personhood, life_stage_aging, physiology, visual_appearance
  - keywords: aging, appearance, body, identity, medicine
- `ج ل و B006` — الشهرة وابن جلا
  - activated_by_or_with: ء ن ث, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: cognition, communication, hierarchy_status, honor_shame, identity_personhood, knowledge_learning, language_speech, memory_attention, social_relations
  - keywords: communication, identity, knowledge, language, memory, reputation, society, status
- `ج ل و B007` — بياض اليوم وصفاء الجو
  - activated_by_or_with: ء ن ث, ح س ن, خ ل ق, ذ ك ر, ش ت ت, ص د ق, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: habitat_ecology, light_darkness, perception, proof_uncertainty, sky_astronomy, time, weather_climate
  - keywords: clarity, environment, light, nature, perception, sky, time, weather
- `ج ل و B008` — النظر المتطلع
  - activated_by_or_with: ء ن ث, ح س ن, خ ل ق, ذ ك ر, س ع ي, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: animal, memory_attention, motion, orientation_direction, perception, wildlife
  - keywords: animal, attention, motion, orientation, perception, vision
- `ج ل و B009` — عطية الجلوة
  - activated_by_or_with: ء ن ث, ب خ ل, ح س ن, خ ل ق, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, و ق ي, ي س ر
  - themes: commerce_exchange, economy, hospitality_welfare, household_community, kinship, marriage_genealogy, obligation_contract, ritual
  - keywords: economy, exchange, household, kinship, marriage, obligation, ritual, wedding

### خ ل ق

- `خ ل ق B001` — تقدير الشيء وقياسه
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: agency_action, craft, form_structure, measurement, reasoning_decision, surface_shape, value_quality
  - keywords: craft, geometry, measure, measurement, preparation, standard
- `خ ل ق B002` — إبداع الخلق وإيجاده
  - activated_by_or_with: ج ل و, ح س ن, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, ي س ر
  - themes: agency_action, belief_revelation, cognition, labor_work, sky_astronomy
  - keywords: agency, production
- `خ ل ق B003` — تمام الخلقة واعتدال الصورة
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: anatomy, form_structure, ornament_beauty, perception, posture_embodiment, surface_shape, visual_appearance
  - keywords: aesthetics, anatomy, beauty, embodiment, geometry, morphology, perception, vision
- `خ ل ق B004` — السجية والطبيعة الباطنة
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ح س ن, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: cognition, ethics_morality, identity_personhood, intention_character, religion_worship, social_relations
  - keywords: ethics, identity, psychology, religion, sociality, society, virtue
- `خ ل ق B005` — الجدارة والتهيؤ للشيء
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, و ق ي, ي س ر
  - themes: agency_action, capacity_ability, intention_character, labor_work, value_quality
  - keywords: capacity, preparation, readiness
- `خ ل ق B006` — الخلاق نصيب الخير
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `خ ل ق B007` — اختلاق الكذب والكلام
  - activated_by_or_with: ج ل و, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, ي س ر
  - themes: communication, deception_corruption, rhetoric_discourse, writing_text
  - keywords: deception, discourse
- `خ ل ق B008` — ملاسة السطح واستواؤه
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, ذ ك ر, ش ت ت, ص د ق, ع ط و, غ ش و, ن ه ر, و ق ي, ي س ر
  - themes: body, earth_geology, geography_landscape, material, substance_texture, surface_shape, tools_equipment
  - keywords: body, geology, landscape, material, surface
- `خ ل ق B009` — بلى الثوب وذهاب وبره
  - activated_by_or_with: ء ن ث, ج ل و, ذ ك ر, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, ي س ر
  - themes: abundance_scarcity, earth_geology, food_nutrition, growth_decay, life_stage_aging, material, textile_clothing, time
  - keywords: aging, erosion, material, poverty, textile, time
- `خ ل ق B010` — الخلوق والتخليق بالطيب
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, ي س ر
  - themes: body, hygiene_sanitation, material, ornament_beauty, perception, ritual, substance_texture
  - keywords: adornment, body, cosmetic, cosmetics, fragrance, material, ritual
- `خ ل ق B011` — نقرة أو بئر تمسك الماء
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, ذ ك ر, ص د ق, غ ش و, غ ن ي, ل ي ل, ن ه ر, ي س ر
  - themes: earth_geology, geography_landscape, place_location, storage_vessels, water_hydrology, weather_climate
  - keywords: geology, hydrology, landscape, settlement, water
- `خ ل ق B012` — انسداد مصمت كالصخرة
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: anatomy, boundary, containment_access, control_restraint, disease_injury, posture_embodiment, substance_texture
  - keywords: anatomy, barrier, embodiment

### ذ ك ر

- `ذ ك ر B001` — الذكر خلاف الأنثى
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: body, gender, kinship, naming_classification, physiology, reasoning_decision, reproduction_birth, sexuality
  - keywords: biology, body, contrast, gender, kinship, reproduction, sex, taxonomy
- `ذ ك ر B002` — صلابة الذكر وحدته وشدته
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, س ع ي, ص د ق, ع ط و, غ ش و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: agriculture, danger_harm, force_power, material, terrain_desert, value_quality, weaponry, weather_climate
  - keywords: agriculture, force, material, strength, terrain, weapon, weather
- `ذ ك ر B003` — استحضار الشيء بعد النسيان أو مع الحفظ
  - activated_by_or_with: ج ل و, خ ل ق, ص د ق, غ ش و, غ ن ي
  - themes: cognition, knowledge_learning, memory_attention
  - keywords: attention, cognition, knowledge, memory, psychology
- `ذ ك ر B004` — جريان الذكر على اللسان
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: communication, honor_shame, language_speech, rhetoric_discourse, social_relations, testimony_witness, value_quality
  - keywords: communication, discourse, evaluation, language, reputation, society, speech, testimony
- `ذ ك ر B005` — ذكر الله عبادة وثناء ودعاء
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ذ ك ر B006` — الذكر كتاب منزل أو كتاب دين
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ذ ك ر B007` — ذكر المرء شرف وصيت
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: culture_tradition, hierarchy_status, honor_shame, memory_attention, social_relations, value_quality
  - keywords: evaluation, hierarchy, honor, memory, reputation, society, status
- `ذ ك ر B008` — ذكر الحق صك ووثيقة حق
  - activated_by_or_with: ب خ ل, ج ل و, خ ل ق, س ع ي, ص د ق, ع ط و, غ ن ي, ن ه ر, ي س ر
  - themes: authority_governance, law, obligation_contract, proof_uncertainty, wealth_property, writing_text
  - keywords: administration, contract, evidence, law, property
- `ذ ك ر B009` — الذكرى والتذكرة ما يذكّر
  - activated_by_or_with: ج ل و, خ ل ق, س ع ي, ص د ق, ع ط و, غ ش و, غ ن ي, ن ه ر
  - themes: belief_revelation, cognition, communication, knowledge_learning, memory_attention
  - keywords: communication, memory

### ء ن ث

- `ء ن ث B001` — الأنثى خلاف الذكر
  - activated_by_or_with: ج ل و, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, ي س ر
  - themes: body, gender, identity_personhood, kinship, physiology, posture_embodiment, reproduction_birth, sexuality
  - keywords: biology, body, embodiment, gender, identity, kinship, life, reproduction, sex
- `ء ن ث B002` — اللِّين والضعف
  - activated_by_or_with: ب خ ل, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ش و, ن ه ر, و ق ي, ي س ر
  - themes: danger_harm, ethics_morality, force_power, intention_character, material, weaponry
  - keywords: conduct, force, material, strength, weapon, weaponry
- `ء ن ث B003` — الأنثيان
  - activated_by_or_with: ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: anatomy, body, naming_classification, perception, quantity_number, reproduction_birth, sexuality
  - keywords: anatomy, body, duality, nomenclature, reproduction, sexuality
- `ء ن ث B004` — الأرض السهلة الخصبة
  - activated_by_or_with: ج ل و, ح س ن, خ ل ق, ذ ك ر, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: abundance_scarcity, agriculture, earth_geology, geography_landscape, growth_decay, habitat_ecology, reproduction_birth
  - keywords: agriculture, ecology, fertility, growth, landscape, prosperity
- `ء ن ث B005` — تأنيث اللفظ
  - activated_by_or_with: ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: form_structure, gender, grammar_expression, language_speech, naming_classification
  - keywords: classification, gender, language, morphology, naming
- `ء ن ث B006` — إناث الأوثان والموات
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ء ن ث B007` — طيب النساء المؤنث
  - activated_by_or_with: ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, غ ش و, غ ن ي, ل ي ل, ن ه ر, ي س ر
  - themes: gender, ornament_beauty, perception, textile_clothing, visual_appearance
  - keywords: adornment, color, cosmetic, cosmetics, fragrance, gender, textile
- `ء ن ث B008` — قبيلتا الأنثيين
  - activated_by_or_with: ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: culture_tradition, identity_personhood, kinship, marriage_genealogy, naming_classification, social_relations, time
  - keywords: identity, kinship, naming, nomenclature, society

### س ع ي

- `س ع ي B001` — حركة مقصودة إلى المطلوب
  - activated_by_or_with: ء ن ث, ج ل و, خ ل ق, ع ط و, غ ش و, غ ن ي, ل ي ل, و ق ي, ي س ر
  - themes: intention_character, motion, pilgrimage_sacrifice, ritual, travel
  - keywords: mobility, movement, ritual, travel
- `س ع ي B002` — عمل وكسب وتصرف
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ح س ن, خ ل ق, ذ ك ر, ص د ق, ع ط و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: agency_action, economy, ethics_morality, labor_work, obligation_contract, provision_resource
  - keywords: agency, economy, effort, ethics, labor, livelihood
- `س ع ي B003` — ولاية وسعاية على القوم
  - activated_by_or_with: ب خ ل, ج ل و, ح س ن, ذ ك ر, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: authority_governance, finance_debt, hospitality_welfare, household_community, politics_order
  - keywords: administration, authority, charity, community, taxation
- `س ع ي B004` — وشاية إلى السلطان
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, ش ت ت, ص د ق, ع ط و, غ ش و, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: conflict, danger_harm, deception_corruption, force_power, justice_judgment, language_speech, politics_order, trust_loyalty, violence_warfare
  - keywords: conflict, justice, politics, power, speech, violence
- `س ع ي B005` — كسب العبد لفكاك رقبته
  - activated_by_or_with: ب خ ل, ج ل و, ح س ن, خ ل ق, ذ ك ر, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: belief_revelation, control_restraint, economy, hierarchy_status, labor_work, law, obligation_contract
  - keywords: contract, economy, labor, law, slavery
- `س ع ي B006` — مسعاة المكارم
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ح س ن, خ ل ق, ذ ك ر, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: ethics_morality, hierarchy_status, honor_shame, hospitality_welfare, justice_judgment, kinship, protection_security, social_relations
  - keywords: charity, ethics, honor, justice, kinship, reputation
- `س ع ي B007` — مساعاة الإماء بالفجور
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ح س ن, خ ل ق, ذ ك ر, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: commerce_exchange, control_restraint, economy, ethics_morality, gender, hierarchy_status, law, sexuality
  - keywords: coercion, commerce, crime, economy, gender, sexuality, slavery
- `س ع ي B008` — مغالبة في السعي
  - activated_by_or_with: ج ل و, ح س ن, خ ل ق, ذ ك ر, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: agency_action, conflict, hierarchy_status, labor_work, recreation_sport, value_quality
  - keywords: achievement, competition, conflict, effort, performance, victory

### ش ت ت

- `ش ت ت B001` — التفرق والشتات
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: boundary, conflict, form_structure, migration_displacement, naming_classification, quantity_number, reasoning_decision, social_relations, stability_endurance
  - keywords: classification, conflict, separation, society
- `ش ت ت B002` — الثغر الشتيت
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: anatomy, body, ornament_beauty, pattern_marking, politics_order, space, time, visual_appearance
  - keywords: anatomy, appearance, beauty, body, pattern
- `ش ت ت B003` — بُعد ما بين الشيئين
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ش و, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: boundary, measurement, quantity_number, reasoning_decision, social_relations, space
  - keywords: contrast, duality, measurement, separation, space

### ع ط و

- `ع ط و B001` — الأخذ والتناول باليد
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: agency_action, anatomy, control_restraint, motion, posture_embodiment, social_relations, wealth_property
  - keywords: embodiment, motion
- `ع ط و B002` — المناولة والإعطاء
  - activated_by_or_with: ب خ ل, ج ل و, ح س ن, ذ ك ر, س ع ي, ص د ق, غ ش و, غ ن ي, ل ي ل, و ق ي, ي س ر
  - themes: commerce_exchange, hospitality_welfare, motion, wealth_property
  - keywords: charity, exchange, ownership, property
- `ع ط و B003` — الخدمة والمناولة للأهل
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ص د ق, غ ش و, غ ن ي, ل ي ل, ي س ر
  - themes: hospitality_welfare, household_community, kinship, labor_work, obligation_contract, support_dependence
  - keywords: assistance, household, kinship, labor, obligation, support
- `ع ط و B004` — التعاطي والخوض فيما يبلغه
  - activated_by_or_with: ء ن ث, ب خ ل, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: agency_action, boundary, danger_harm, desire_appetite, ethics_morality
  - keywords: agency, boundary, conduct, risk
- `ع ط و B005` — استعطاء الناس
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ص د ق, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: abundance_scarcity, commerce_exchange, communication, hospitality_welfare, prayer_supplication, support_dependence
  - keywords: charity, dependence, dependency, exchange, petition, poverty, welfare
- `ع ط و B006` — اللين والانقياد والمطاوعة
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ص د ق, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: authority_governance, capacity_ability, control_restraint, husbandry, material, motion, religion_worship, substance_texture
  - keywords: control, material, motion, obedience
- `ع ط و B007` — الغلبة في التعاطي
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, غ ش و, غ ن ي, ن ه ر, ي س ر
  - themes: agency_action, conflict, force_power, hierarchy_status
  - keywords: agency, competition, conflict, hierarchy, power, victory

### و ق ي

- `و ق ي B001` — دفع الضرر بوقاية
  - activated_by_or_with: ء ن ث, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ع ط و, غ ش و, غ ن ي, ل ي ل, ي س ر
  - themes: boundary, danger_harm, protection_security
  - keywords: boundary, protection, risk, security
- `و ق ي B002` — جعل النفس في وقاية
  - activated_by_or_with: ء ن ث, ب خ ل, ح س ن, خ ل ق, س ع ي, ص د ق, ع ط و, غ ش و, غ ن ي, ن ه ر, ي س ر
  - themes: afterlife_eschatology, control_restraint, ethics_morality, justice_judgment, religion_worship
  - keywords: discipline, ethics, religion
- `و ق ي B003` — توقي الدابة من وجع الحافر
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, ي س ر
  - themes: anatomy, animal, health_medicine, motion, protection_security, suffering_hardship, terrain_desert, tools_equipment
  - keywords: anatomy, animal, equipment, locomotion, pain, terrain
- `و ق ي B004` — الأوقية وزن معلوم
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ن ي, ل ي ل, ي س ر
  - themes: commerce_exchange, economy, finance_debt, measurement, quantity_number, value_quality
  - keywords: economy, measurement, quantity, standard
- `و ق ي B005` — الواقي اسم للصرد
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, ذ ك ر, س ع ي, ش ت ت, ص د ق, غ ش و, غ ن ي, ل ي ل, ن ه ر, ي س ر
  - themes: animal, habitat_ecology, language_speech, naming_classification, wildlife
  - keywords: animal, ecology, language, naming, nature, nomenclature, taxonomy, wildlife, zoology

### ص د ق

- `ص د ق B001` — صدق القول
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ع ط و, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: belief_revelation, communication, ethics_morality, knowledge_learning, language_speech, proof_uncertainty, testimony_witness
  - keywords: communication, ethics, evidence, language, testimony, verification
- `ص د ق B002` — صلابة الشيء واستواؤه
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ع ط و, غ ش و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: ethics_morality, force_power, material, posture_embodiment, stability_endurance, surface_shape, weaponry
  - keywords: embodiment, geometry, integrity, strength, weaponry
- `ص د ق B003` — تمام الصلاح والثبوت
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: ethics_morality, hierarchy_status, honor_shame, identity_personhood, place_location, stability_endurance, value_quality
  - keywords: honor, identity, integrity, place, quality, status, virtue
- `ص د ق B004` — تحقيق الوعد والفعل
  - activated_by_or_with: ب خ ل, ج ل و, خ ل ق, ذ ك ر, س ع ي, ع ط و, غ ش و, غ ن ي, ن ه ر, ي س ر
  - themes: agency_action, belief_revelation, obligation_contract, proof_uncertainty, trust_loyalty, violence_warfare
  - keywords: agency, loyalty, obligation, trust, verification
- `ص د ق B005` — صدق المودة والصحبة
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ع ط و, غ ش و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: communication, emotion, ethics_morality, household_community, social_relations, trust_loyalty
  - keywords: community, emotion, ethics, loyalty, trust
- `ص د ق B006` — صدقة المال والحق
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ح س ن, خ ل ق, س ع ي, ع ط و, غ ش و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: abundance_scarcity, economy, finance_debt, hospitality_welfare, justice_judgment, provision_resource, religion_worship
  - keywords: economy, finance, generosity, justice, poverty, religion, taxation, welfare
- `ص د ق B007` — صداق المرأة
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ذ ك ر, س ع ي, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: family, finance_debt, gender, kinship, law, marriage_genealogy, obligation_contract, wealth_property
  - keywords: contract, family, finance, gender, kinship, law, marriage, property

### ح س ن

- `ح س ن B001` — الحسن ضد القبح
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: desire_appetite, ethics_morality, force_power, ornament_beauty, perception, value_quality, visual_appearance
  - keywords: aesthetics, appearance, evaluation, perception, quality, virtue
- `ح س ن B002` — الإحسان فعل حسن
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, خ ل ق, س ع ي, ص د ق, ع ط و, غ ش و, ن ه ر, و ق ي, ي س ر
  - themes: craft, ethics_morality, hospitality_welfare, justice_judgment
  - keywords: charity, craft, ethics, generosity, justice, virtue
- `ح س ن B003` — الحسنة خير يصيب
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ح س ن B004` — أسماء الحسن للمواضع والأجسام
  - activated_by_or_with: ء ن ث, ج ل و, خ ل ق, ذ ك ر, ش ت ت, ع ط و, غ ش و, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: anatomy, form_structure, geography_landscape, naming_classification, sky_astronomy, terrain_desert
  - keywords: anatomy, astronomy, geography, landscape, morphology, onomastics, taxonomy
- `ح س ن B005` — حُسَيْناء الغاية والجهد
  - activated_by_or_with: ج ل و, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: boundary, capacity_ability, change_transition, desire_appetite, labor_work, measurement, stability_endurance, value_quality
  - keywords: achievement, boundary, capacity, limit

### ي س ر

- `ي س ر B001` — انفتاح وسهولة بعد عسر
  - activated_by_or_with: ب خ ل, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ش و, غ ن ي, ن ه ر, و ق ي
  - themes: capacity_ability, change_transition, containment_access, obligation_contract, suffering_hardship, support_dependence
  - keywords: assistance, capacity, readiness, support
- `ي س ر B002` — قلة يسيرة
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي
  - themes: abundance_scarcity, boundary, measurement, quantity_number, time
  - keywords: limit, measure, quantity
- `ي س ر B003` — سعة وغنى
  - activated_by_or_with: ء ن ث, ج ل و, خ ل ق, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ن ي, ن ه ر, و ق ي
  - themes: abundance_scarcity, economy, hierarchy_status, provision_resource
  - keywords: abundance, economy, livelihood, prosperity, provision, resource, status
- `ي س ر B004` — الجهة اليسرى واليد اليسرى
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, ش ت ت, ص د ق, ع ط و, غ ش و, ل ي ل, ن ه ر, و ق ي
  - themes: anatomy, body, orientation_direction, space, surface_shape
  - keywords: anatomy, body, direction, orientation, polarity, space
- `ي س ر B005` — خفة وانقياد في الحركة
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي
  - themes: animal, authority_governance, body, capacity_ability, control_restraint, force_power, motion, substance_texture
  - keywords: animal, body, control, locomotion, motion, movement, obedience
- `ي س ر B006` — إدرار ونماء في الغنم
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي
  - themes: abundance_scarcity, animal, food_nutrition, husbandry, labor_work, livestock, reproduction_birth
  - keywords: abundance, animal, fertility, livestock, production, reproduction
- `ي س ر B007` — قداح وقمار وتقسيم جزور
  - activated_by_or_with: ج ل و, خ ل ق, ذ ك ر, س ع ي, ص د ق, غ ن ي, ل ي ل
  - themes: food_nutrition, pilgrimage_sacrifice, proof_uncertainty, provision_resource, recreation_sport, ritual
  - keywords: ritual
- `ي س ر B008` — خطوط منفصلة وعلامات في البدن
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي
  - themes: anatomy, body, health_medicine, identity_personhood, pattern_marking, proof_uncertainty, writing_text
  - keywords: anatomy, body, identity, marking, pattern
- `ي س ر B009` — فتل إلى أسفل وطعن حذاء الوجه
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ش و, ل ي ل, ن ه ر, و ق ي
  - themes: craft, force_power, motion, orientation_direction, violence_warfare, weaponry
  - keywords: combat, craft, direction, force, motion, orientation, weapon
- `ي س ر B010` — موضع أو علم باسم يسر ويسار
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, ش ت ت, ص د ق, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي
  - themes: geography_landscape, identity_personhood, naming_classification, rhetoric_discourse
  - keywords: geography, identity, naming, onomastics, poetry
- `ي س ر B011` — فتى يسمى يسارا
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, غ ن ي, ل ي ل, ن ه ر, و ق ي
  - themes: gender, hierarchy_status, household_community, identity_personhood, kinship, life_stage_aging, naming_classification, physiology
  - keywords: gender, identity, kinship, life, status

### ب خ ل

- `ب خ ل B001` — البخل
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ن ي, ن ه ر, و ق ي, ي س ر
  - themes: ethics_morality, hospitality_welfare, law, obligation_contract, wealth_property
  - keywords: charity, ethics, obligation, ownership, property, virtue

### غ ن ي

- `غ ن ي B001` — الغنى والاستغناء
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ش و, ن ه ر, و ق ي, ي س ر
  - themes: abundance_scarcity, capacity_ability, control_restraint, economy, hierarchy_status, protection_security, provision_resource
  - keywords: abundance, capacity, economy, poverty, provision, resource, security, status
- `غ ن ي B002` — الغَناء والكفاية
  - activated_by_or_with: ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ش و, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: capacity_ability, change_transition, commerce_exchange, health_medicine, provision_resource, support_dependence, value_quality
  - keywords: capacity, dependence, dependency, exchange, provision, support
- `غ ن ي B003` — الغِناء والصوت
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: agency_action, emotion, grammar_expression, ornament_beauty, perception, religion_worship, rhetoric_discourse, ritual
  - keywords: aesthetics, emotion, performance, poetry, ritual
- `غ ن ي B004` — الغنى بالمكان
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, ل ي ل, ن ه ر, و ق ي, ي س ر
  - themes: habitat_ecology, household_community, memory_attention, physiology, place_location, stability_endurance
  - keywords: community, life, memory, place, settlement
- `غ ن ي B005` — الغانية المستغنية
  - activated_by_or_with: ء ن ث, ج ل و, ح س ن, خ ل ق, ذ ك ر, س ع ي, ش ت ت, ص د ق, ع ط و, غ ش و, ل ي ل, ن ه ر, ي س ر
  - themes: desire_appetite, gender, hierarchy_status, identity_personhood, marriage_genealogy, ornament_beauty, sexuality
  - keywords: adornment, beauty, gender, identity, marriage, sexuality, status
- `غ ن ي B006` — الغنى والتزويج
  - activated_by_or_with: ء ن ث, ب خ ل, ج ل و, ذ ك ر, س ع ي, ص د ق, ع ط و, غ ش و, ن ه ر, و ق ي, ي س ر
  - themes: authority_governance, family, hierarchy_status, household_community, kinship, marriage_genealogy, obligation_contract, protection_security, sexuality
  - keywords: contract, family, household, kinship, marriage, protection, sexuality, status

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
