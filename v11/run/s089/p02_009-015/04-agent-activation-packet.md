# v11 Activation Packet — S89:9-15

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_9: وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ
- verse_10: وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ
- verse_11: ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ
- verse_12: فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ
- verse_13: فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ
- verse_14: إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ
- verse_15: فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ج و ب → ص خ ر → و د ي → و ت د → ط غ ي → ب ل د → ك ث ر → ف س د → ص ب ب → ر ب ب → س و ط → ع ذ ب → ر ص د → ء ن س → ب ل و → ك ر م → ن ع م → ق و ل

## Branch inventory summary

- ج و ب: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص خ ر: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- و د ي: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- و ت د: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- ط غ ي: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- ب ل د: 12 branches (12 with Qnet bridge-theme nodes; 0 Furūq-only)
- ك ث ر: 7 branches (6 with Qnet bridge-theme nodes; 1 Furūq-only)
- ف س د: 1 branches (1 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص ب ب: 11 branches (11 with Qnet bridge-theme nodes; 0 Furūq-only)
- ر ب ب: 17 branches (17 with Qnet bridge-theme nodes; 0 Furūq-only)
- س و ط: 4 branches (3 with Qnet bridge-theme nodes; 1 Furūq-only)
- ع ذ ب: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- ر ص د: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء ن س: 7 branches (6 with Qnet bridge-theme nodes; 1 Furūq-only)
- ب ل و: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- ك ر م: 10 branches (10 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن ع م: 13 branches (13 with Qnet bridge-theme nodes; 0 Furūq-only)
- ق و ل: 17 branches (16 with Qnet bridge-theme nodes; 1 Furūq-only)

## QAC-first root resolution audit

- ج و ب | qac_keys=جوب | status=resolved | matches=root_000273
- ص خ ر | qac_keys=صخر | status=resolved | matches=root_000847
- و د ي | qac_keys=ودي | status=resolved | matches=root_001637
- و ت د | qac_keys=وتد | status=resolved | matches=root_001620
- ط غ ي | qac_keys=طغي | status=resolved | matches=root_000937
- ب ل د | qac_keys=بلد | status=resolved | matches=root_000148
- ك ث ر | qac_keys=كثر | status=resolved | matches=root_001286
- ف س د | qac_keys=فسد | status=resolved | matches=root_001154
- ص ب ب | qac_keys=صبب | status=resolved | matches=root_000838
- ر ب ب | qac_keys=ربب | status=resolved | matches=root_000532
- س و ط | qac_keys=سوط | status=resolved | matches=root_000759
- ع ذ ب | qac_keys=عذب | status=resolved | matches=root_000994
- ر ص د | qac_keys=رصد | status=resolved | matches=root_000566
- ء ن س | qac_keys=ءنس | status=resolved | matches=root_000059
- ب ل و | qac_keys=بلو | status=resolved | matches=root_000153
- ك ر م | qac_keys=كرم | status=resolved | matches=root_001294
- ن ع م | qac_keys=نعم | status=resolved | matches=root_001525
- ق و ل | qac_keys=قول | status=resolved | matches=root_001272

## Top candidate bridges

- `و د ي B001` ↔ `ع ذ ب B009` | score_hint=30 | discovery_hint=16 | themes=anatomy, health_medicine, physiology, reproduction_birth, substance_texture | keywords=anatomy, fluid, medicine, physiology, reproduction | q2=—
- `ر ب ب B008` ↔ `ر ص د B004` | score_hint=30 | discovery_hint=17 | themes=agriculture, habitat_ecology, reproduction_birth, water_hydrology, weather_climate | keywords=agriculture, ecology, fertility, water, weather | q2=—
- `ر ص د B004` ↔ `ك ر م B002` | score_hint=30 | discovery_hint=18 | themes=agriculture, food_nutrition, habitat_ecology, reproduction_birth, weather_climate | keywords=agriculture, ecology, fertility, nourishment, weather | q2=—
- `و د ي B003` ↔ `ك ر م B004` | score_hint=28 | discovery_hint=17 | themes=agriculture, growth_decay, harvest_cultivation, plant_vegetation | keywords=agriculture, botany, cultivation, growth, plant | q2=—
- `ك ث ر B006` ↔ `ك ر م B004` | score_hint=28 | discovery_hint=17 | themes=agriculture, food_nutrition, harvest_cultivation, plant_vegetation | keywords=agriculture, botany, food, fruit, plant | q2=—
- `ص ب ب B010` ↔ `ن ع م B012` | score_hint=28 | discovery_hint=14 | themes=labor_work, motion, stability_endurance, travel | keywords=effort, endurance, locomotion, movement, travel | q2=—
- `ب ل و B003` ↔ `ن ع م B001` | score_hint=28 | discovery_hint=15 | themes=commerce_exchange, ethics_morality, hospitality_welfare, support_dependence | keywords=ethics, generosity, patronage, reciprocity, welfare | q2=—
- `و د ي B005` ↔ `ص ب ب B002` | score_hint=26 | discovery_hint=14 | themes=geography_landscape, navigation_route, terrain_desert, travel, water_hydrology | keywords=geography, hydrology, terrain, travel | q2=—
- `ب ل و B006` ↔ `ن ع م B004` | score_hint=26 | discovery_hint=14 | themes=communication, grammar_expression, language_speech, proof_uncertainty, reasoning_decision | keywords=communication, language, logic, truth | q2=—
- `ب ل د B012` ↔ `ن ع م B006` | score_hint=24 | discovery_hint=14 | themes=animal, habitat_ecology, terrain_desert, wildlife | keywords=animal, bird, desert, zoology | q2=—
- `ر ب ب B008` ↔ `ك ر م B002` | score_hint=24 | discovery_hint=17 | themes=agriculture, habitat_ecology, reproduction_birth, weather_climate | keywords=agriculture, ecology, fertility, weather | q2=—
- `ع ذ ب B008` ↔ `ك ر م B001` | score_hint=24 | discovery_hint=13 | themes=ethics_morality, hierarchy_status, honor_shame, hospitality_welfare | keywords=beneficence, ethics, status, virtue | q2=—
- `ر ص د B002` ↔ `ك ر م B008` | score_hint=24 | discovery_hint=16 | themes=commerce_exchange, economy, hospitality_welfare, support_dependence | keywords=economy, exchange, gift, patronage | q2=—
- `ج و ب B004` ↔ `ط غ ي B005` | score_hint=22 | discovery_hint=14 | themes=earth_geology, geography_landscape, terrain_desert | keywords=geology, landscape, terrain, topography | q2=—
- `ص خ ر B003` ↔ `ر ب ب B012` | score_hint=22 | discovery_hint=16 | themes=agriculture, habitat_ecology, plant_vegetation | keywords=agriculture, botany, ecology, flora | q2=—
- `ر ب ب B001` ↔ `ق و ل B010` | score_hint=22 | discovery_hint=14 | themes=authority_governance, force_power, hierarchy_status | keywords=authority, governance, hierarchy, power | q2=—
- `ب ل د B009` ↔ `ن ع م B011` | score_hint=20 | discovery_hint=14 | themes=place_location, social_relations | keywords=belonging, habitation, place, settlement | q2=—
- `ء ن س B001` ↔ `ب ل و B008` | score_hint=20 | discovery_hint=14 | themes=identity_personhood, social_relations | keywords=anthropology, identity, sociality, society | q2=—
- `و ت د B002` ↔ `ك ر م B007` | score_hint=20 | discovery_hint=14 | themes=anatomy, body, form_structure, motion | keywords=anatomy, body, morphology | q2=—
- `ط غ ي B001` ↔ `ق و ل B010` | score_hint=20 | discovery_hint=13 | themes=authority_governance, conflict, force_power, law | keywords=authority, law, power | q2=—
- `ب ل د B012` ↔ `ر ب ب B014` | score_hint=20 | discovery_hint=13 | themes=animal, habitat_ecology, terrain_desert, wildlife | keywords=desert, ecology, zoology | q2=—
- `س و ط B002` ↔ `ع ذ ب B005` | score_hint=20 | discovery_hint=13 | themes=control_restraint, punishment_sanction, suffering_hardship, violence_warfare | keywords=pain, punishment, violence | q2=—
- `ر ص د B003` ↔ `ب ل و B009` | score_hint=20 | discovery_hint=13 | themes=boundary, geography_landscape, motion, space | keywords=geography, movement, space | q2=—
- `ج و ب B005` ↔ `ك ر م B003` | score_hint=18 | discovery_hint=14 | themes=body, craft, textile_clothing | keywords=body, clothing, craft | q2=—
- `و د ي B001` ↔ `و ت د B004` | score_hint=18 | discovery_hint=15 | themes=physiology, reproduction_birth, sexuality | keywords=physiology, reproduction, sexuality | q2=—
- `و د ي B003` ↔ `ك ث ر B006` | score_hint=18 | discovery_hint=15 | themes=agriculture, harvest_cultivation, plant_vegetation | keywords=agriculture, botany, plant | q2=—
- `و د ي B003` ↔ `ر ص د B004` | score_hint=18 | discovery_hint=15 | themes=agriculture, change_transition, reproduction_birth | keywords=agriculture, fertility, renewal | q2=—
- `و د ي B003` ↔ `ك ر م B002` | score_hint=18 | discovery_hint=16 | themes=agriculture, growth_decay, reproduction_birth | keywords=agriculture, fertility, growth | q2=—
- `و د ي B005` ↔ `ر ص د B003` | score_hint=18 | discovery_hint=13 | themes=geography_landscape, navigation_route, travel | keywords=geography, passage, travel | q2=—
- `و د ي B006` ↔ `ر ب ب B009` | score_hint=18 | discovery_hint=14 | themes=animal, food_nutrition, livestock | keywords=animal, dairy, livestock | q2=—
- `و ت د B002` ↔ `ب ل د B008` | score_hint=18 | discovery_hint=14 | themes=anatomy, body, form_structure | keywords=anatomy, body, morphology | q2=—
- `ب ل د B001` ↔ `ن ع م B011` | score_hint=18 | discovery_hint=12 | themes=geography_landscape, habitat_ecology, place_location | keywords=geography, habitation, settlement | q2=—
- `ب ل د B002` ↔ `ك ر م B007` | score_hint=18 | discovery_hint=14 | themes=anatomy, body, motion | keywords=anatomy, body, locomotion | q2=—
- `ب ل د B002` ↔ `ن ع م B012` | score_hint=18 | discovery_hint=14 | themes=body, motion, social_relations | keywords=body, contact, locomotion | q2=—
- `ب ل د B008` ↔ `ك ر م B007` | score_hint=18 | discovery_hint=14 | themes=anatomy, body, form_structure | keywords=anatomy, body, morphology | q2=—
- `ك ث ر B006` ↔ `ر ب ب B012` | score_hint=18 | discovery_hint=16 | themes=agriculture, food_nutrition, plant_vegetation | keywords=agriculture, botany, food | q2=—
- `ر ب ب B012` ↔ `ك ر م B004` | score_hint=18 | discovery_hint=16 | themes=agriculture, food_nutrition, plant_vegetation | keywords=agriculture, botany, food | q2=—
- `ر ب ب B013` ↔ `ك ر م B002` | score_hint=18 | discovery_hint=14 | themes=abundance_scarcity, habitat_ecology, provision_resource | keywords=abundance, ecology, sustenance | q2=—
- `ر ب ب B015` ↔ `ب ل و B006` | score_hint=18 | discovery_hint=13 | themes=grammar_expression, language_speech, rhetoric_discourse | keywords=discourse, grammar, semantics | q2=—
- `ر ب ب B016` ↔ `ن ع م B001` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, hospitality_welfare, support_dependence | keywords=charity, ethics, welfare | q2=—
- `ع ذ ب B008` ↔ `ب ل و B003` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, hospitality_welfare, intention_character | keywords=ethics, generosity, virtue | q2=—
- `ب ل و B003` ↔ `ك ر م B001` | score_hint=18 | discovery_hint=12 | themes=ethics_morality, hospitality_welfare, value_quality | keywords=ethics, merit, virtue | q2=—
- `ب ل و B006` ↔ `ق و ل B001` | score_hint=18 | discovery_hint=12 | themes=communication, language_speech, rhetoric_discourse | keywords=communication, discourse, language | q2=—
- `ج و ب B002` ↔ `و د ي B005` | score_hint=16 | discovery_hint=13 | themes=geography_landscape, travel | keywords=geography, landscape, travel | q2=—
- `ج و ب B003` ↔ `ن ع م B004` | score_hint=16 | discovery_hint=13 | themes=communication, social_relations | keywords=communication, dialogue, interaction | q2=—
- `ب ل د B001` ↔ `ص ب ب B002` | score_hint=16 | discovery_hint=12 | themes=geography_landscape, terrain_desert | keywords=geography, terrain, topography | q2=—
- `ك ث ر B002` ↔ `ك ر م B006` | score_hint=16 | discovery_hint=13 | themes=conflict, hierarchy_status | keywords=competition, rivalry, status | q2=—
- `ر ب ب B001` ↔ `ق و ل B004` | score_hint=16 | discovery_hint=12 | themes=authority_governance, hierarchy_status | keywords=authority, governance, hierarchy | q2=—
- `ر ب ب B007` ↔ `ب ل و B009` | score_hint=16 | discovery_hint=13 | themes=geography_landscape, motion | keywords=geography, motion, movement | q2=—
- `ر ب ب B015` ↔ `ق و ل B001` | score_hint=16 | discovery_hint=12 | themes=language_speech, rhetoric_discourse | keywords=discourse, linguistics, rhetoric | q2=—
- `ع ذ ب B008` ↔ `ق و ل B003` | score_hint=16 | discovery_hint=13 | themes=intention_character, social_relations | keywords=character, sociability, sociality | q2=—
- `ك ر م B007` ↔ `ن ع م B012` | score_hint=16 | discovery_hint=14 | themes=body, motion | keywords=body, locomotion, movement | q2=—
- `ط غ ي B002` ↔ `ص ب ب B001` | score_hint=16 | discovery_hint=13 | themes=force_power, motion, substance_texture, water_hydrology | keywords=fluid, hydrology | q2=—
- `ط غ ي B002` ↔ `ص ب ب B008` | score_hint=16 | discovery_hint=12 | themes=danger_harm, habitat_ecology, motion, violence_warfare | keywords=motion, violence | q2=—
- `ط غ ي B004` ↔ `ع ذ ب B005` | score_hint=16 | discovery_hint=12 | themes=danger_harm, justice_judgment, punishment_sanction, violence_warfare | keywords=punishment, violence | q2=—
- `ب ل د B010` ↔ `ص ب ب B002` | score_hint=16 | discovery_hint=13 | themes=force_power, geography_landscape, terrain_desert, water_hydrology | keywords=gravity, terrain | q2=—
- `ر ب ب B014` ↔ `ن ع م B006` | score_hint=16 | discovery_hint=12 | themes=animal, habitat_ecology, terrain_desert, wildlife | keywords=desert, zoology | q2=—
- `ع ذ ب B008` ↔ `ك ر م B006` | score_hint=16 | discovery_hint=12 | themes=ethics_morality, hierarchy_status, honor_shame, social_relations | keywords=status, virtue | q2=—
- `ب ل و B003` ↔ `ك ر م B008` | score_hint=16 | discovery_hint=14 | themes=commerce_exchange, hospitality_welfare, intention_character, support_dependence | keywords=patronage, reciprocity | q2=—
- `ن ع م B004` ↔ `ق و ل B009` | score_hint=16 | discovery_hint=12 | themes=communication, obligation_contract, reasoning_decision, social_relations | keywords=agreement, communication | q2=—
- `ج و ب B002` ↔ `ر ص د B003` | score_hint=14 | discovery_hint=12 | themes=geography_landscape, motion, travel | keywords=geography, travel | q2=—
- `ج و ب B002` ↔ `ب ل و B009` | score_hint=14 | discovery_hint=12 | themes=geography_landscape, migration_displacement, motion | keywords=geography, migration | q2=—
- `ج و ب B002` ↔ `ن ع م B012` | score_hint=14 | discovery_hint=12 | themes=motion, transport, travel | keywords=transport, travel | q2=—
- `ج و ب B003` ↔ `ك ر م B009` | score_hint=14 | discovery_hint=12 | themes=rhetoric_discourse, ritual, social_relations | keywords=discourse, ritual | q2=—
- `ج و ب B004` ↔ `و د ي B005` | score_hint=14 | discovery_hint=12 | themes=earth_geology, geography_landscape, terrain_desert | keywords=landscape, terrain | q2=—
- `ج و ب B004` ↔ `ع ذ ب B004` | score_hint=14 | discovery_hint=13 | themes=containment_access, space, weather_climate | keywords=space, weather | q2=—
- `ج و ب B004` ↔ `ن ع م B007` | score_hint=14 | discovery_hint=13 | themes=geography_landscape, sky_astronomy, terrain_desert | keywords=landscape, topography | q2=—
- `ج و ب B005` ↔ `ق و ل B008` | score_hint=14 | discovery_hint=12 | themes=craft, material, tools_equipment | keywords=craft, material | q2=—
- `ج و ب B006` ↔ `ء ن س B002` | score_hint=14 | discovery_hint=12 | themes=knowledge_learning, perception, proof_uncertainty | keywords=knowledge, perception | q2=—
- `ص خ ر B001` ↔ `و ت د B001` | score_hint=14 | discovery_hint=11 | themes=architecture_construction, earth_geology, support_dependence | keywords=construction, geology | q2=—
- `ص خ ر B004` ↔ `ق و ل B008` | score_hint=14 | discovery_hint=13 | themes=craft, force_power, tools_equipment | keywords=craft, impact | q2=—
- `و د ي B004` ↔ `ص ب ب B007` | score_hint=14 | discovery_hint=13 | themes=danger_harm, growth_decay, loss_absence | keywords=decay, loss | q2=—
- `و د ي B005` ↔ `ط غ ي B005` | score_hint=14 | discovery_hint=12 | themes=earth_geology, geography_landscape, terrain_desert | keywords=landscape, terrain | q2=—
- `و ت د B002` ↔ `ب ل د B002` | score_hint=14 | discovery_hint=13 | themes=anatomy, body, motion | keywords=anatomy, body | q2=—
- `و ت د B002` ↔ `ء ن س B005` | score_hint=14 | discovery_hint=13 | themes=anatomy, body, visual_appearance | keywords=anatomy, body | q2=—
- `و ت د B002` ↔ `ن ع م B007` | score_hint=14 | discovery_hint=13 | themes=anatomy, reasoning_decision, surface_shape | keywords=anatomy, shape | q2=—
- `ط غ ي B001` ↔ `ب ل و B002` | score_hint=14 | discovery_hint=11 | themes=agency_action, ethics_morality, justice_judgment | keywords=ethics, morality | q2=—
- `ط غ ي B002` ↔ `ك ث ر B005` | score_hint=14 | discovery_hint=13 | themes=danger_harm, motion, weather_climate | keywords=motion, storm | q2=—
- `ط غ ي B003` ↔ `ر ب ب B001` | score_hint=14 | discovery_hint=11 | themes=authority_governance, belief_revelation, religion_worship | keywords=authority, theology | q2=—
- `ط غ ي B005` ↔ `ب ل د B001` | score_hint=14 | discovery_hint=11 | themes=geography_landscape, place_location, terrain_desert | keywords=terrain, topography | q2=—

## Per-root candidate activations

### ج و ب

- `ج و ب B001` — الخَرْق والقطع النافذ
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: anatomy, change_transition, containment_access, craft, disease_injury, earth_geology, navigation_route, tools_equipment
  - keywords: anatomy, craft, geology, passage, tool
- `ج و ب B002` — قطع الأرض والبلاد
  - activated_by_or_with: ب ل د, ب ل و, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: communication, geography_landscape, measurement, migration_displacement, motion, transport, travel
  - keywords: communication, geography, landscape, migration, transport, travel
- `ج و ب B003` — رَدّ الكلام والإجابة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م
  - themes: commerce_exchange, communication, prayer_supplication, rhetoric_discourse, ritual, social_relations
  - keywords: communication, dialogue, discourse, interaction, prayer, reciprocity, ritual
- `ج و ب B004` — الجَوْبة والانفتاق
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: containment_access, earth_geology, geography_landscape, loss_absence, sky_astronomy, space, terrain_desert, weather_climate
  - keywords: geology, landscape, sky, space, terrain, topography, weather
- `ج و ب B005` — الجَوْب لباسا وترسا
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: body, craft, material, protection_security, textile_clothing, tools_equipment, violence_warfare
  - keywords: body, clothing, craft, equipment, material, protection, textile, warfare
- `ج و ب B006` — النور والكشف والجلاء
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ب ب, ر ص د, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: belief_revelation, concealment_disclosure, knowledge_learning, perception, proof_uncertainty
  - keywords: clarity, knowledge, perception, truth, vision

### ص خ ر

- `ص خ ر B001` — الصخر الصلب العظيم
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: architecture_construction, earth_geology, geography_landscape, material, measurement, substance_texture, support_dependence
  - keywords: construction, geology, landscape, material
- `ص خ ر B002` — الصاخر إناء الخزف
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: cooking_drink, craft, household_community, material, storage_vessels
  - keywords: container, craft, cuisine, domestic, household, material, storage
- `ص خ ر B003` — الصخير النبات
  - activated_by_or_with: ب ل د, ب ل و, ر ب ب, ر ص د, س و ط, ص ب ب, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: agriculture, habitat_ecology, naming_classification, plant_vegetation
  - keywords: agriculture, botany, ecology, flora, nature, taxonomy
- `ص خ ر B004` — صوت الحديد المتصاخر
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: communication, craft, force_power, perception, tools_equipment
  - keywords: craft, impact

### و د ي

- `و د ي B001` — سَيَلان الودْي وإدلاء الذكر
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د
  - themes: anatomy, health_medicine, livestock, physiology, reproduction_birth, sexuality, substance_texture
  - keywords: anatomy, fluid, livestock, medicine, physiology, reproduction, sexuality
- `و د ي B002` — أداء الدية
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م
  - themes: justice_judgment, kinship, law, obligation_contract, place_location, violence_warfare
  - keywords: contract, justice, kinship, law, settlement, violence
- `و د ي B003` — صغار الفسيل
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ع ذ ب, ك ث ر, ك ر م, ن ع م, و ت د
  - themes: agriculture, change_transition, growth_decay, harvest_cultivation, plant_vegetation, reproduction_birth
  - keywords: agriculture, botany, cultivation, fertility, growth, plant, renewal
- `و د ي B004` — ذهاب الشيء وهلاكه
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د
  - themes: belief_revelation, danger_harm, growth_decay, loss_absence, mortality_death, stability_endurance
  - keywords: death, decay, disaster, loss
- `و د ي B005` — الوادي مسلك السيل
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ك ث ر, ن ع م, و ت د
  - themes: earth_geology, geography_landscape, navigation_route, terrain_desert, travel, water_hydrology
  - keywords: geography, hydrology, landscape, passage, terrain, travel
- `و د ي B006` — شد أخلاف الناقة بالتوادي
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د
  - themes: animal, control_restraint, food_nutrition, husbandry, livestock, material, tools_equipment
  - keywords: animal, control, dairy, livestock, restraint, tool

### و ت د

- `و ت د B001` — الوتد المغروز
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: architecture_construction, control_restraint, earth_geology, navigation_route, stability_endurance, support_dependence
  - keywords: anchoring, construction, fastening, geology, stability, support
- `و ت د B002` — نتوء الأذن كأنه وتد
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: anatomy, body, form_structure, motion, reasoning_decision, surface_shape, visual_appearance
  - keywords: anatomy, body, morphology, shape
- `و ت د B003` — انتصاب وثبوت كالوتد
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: orientation_direction, posture_embodiment, stability_endurance, support_dependence
  - keywords: anchoring, embodiment, orientation, posture, stability, support
- `و ت د B004` — انعاظ الرجل
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ع ذ ب, ق و ل, ك ر م, ن ع م, و د ي
  - themes: body, desire_appetite, physiology, posture_embodiment, reproduction_birth, sexuality
  - keywords: body, desire, embodiment, physiology, reproduction, sexuality

### ط غ ي

- `ط غ ي B001` — مجاوزة الحد في العصيان
  - activated_by_or_with: ب ل د, ب ل و, ر ب ب, ص ب ب, ص خ ر, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: agency_action, authority_governance, conflict, ethics_morality, force_power, justice_judgment, law
  - keywords: agency, authority, ethics, law, morality, power
- `ط غ ي B002` — علو الماء والقوة الجارفة
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: danger_harm, force_power, habitat_ecology, motion, substance_texture, violence_warfare, water_hydrology, weather_climate
  - keywords: destruction, disaster, fluid, force, hydrology, motion, nature, storm, violence
- `ط غ ي B003` — الطاغوت رأس الضلالة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ص ب ب, ع ذ ب, ف س د, ق و ل, ك ر م, ن ع م, و د ي
  - themes: authority_governance, belief_revelation, deception_corruption, ethics_morality, religion_worship
  - keywords: authority, deception, religion, theology
- `ط غ ي B004` — الطاغية عذاب غالب
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: belief_revelation, danger_harm, habitat_ecology, justice_judgment, punishment_sanction, violence_warfare
  - keywords: destruction, disaster, judgment, nature, punishment, theology, violence
- `ط غ ي B005` — الطغية الصفاة الملساء
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ع ذ ب, ك ث ر, ن ع م, و ت د, و د ي
  - themes: earth_geology, geography_landscape, orientation_direction, place_location, surface_shape, terrain_desert
  - keywords: geology, landscape, place, surface, terrain, topography

### ب ل د

- `ب ل د B001` — الموضع المحدود من الأرض
  - activated_by_or_with: ء ن س, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ر م, ن ع م, و د ي
  - themes: geography_landscape, habitat_ecology, mortality_death, place_location, terrain_desert
  - keywords: burial, geography, habitation, settlement, terrain, topography
- `ب ل د B002` — الصدر وبلدة النحر
  - activated_by_or_with: ء ن س, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: anatomy, animal, body, communication, cooking_drink, motion, posture_embodiment, social_relations
  - keywords: anatomy, animal, body, contact, gesture, locomotion, posture
- `ب ل د B003` — البلجة بين الحاجبين
  - activated_by_or_with: ء ن س, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ع ذ ب, ق و ل, ك ر م, ن ع م, و ت د, و د ي
  - themes: anatomy, body, identity_personhood, ornament_beauty, pattern_marking, proof_uncertainty, visual_appearance
  - keywords: body, clarity, identity, marking
- `ب ل د B004` — منزلة القمر والموضع السماوي الخالي
  - activated_by_or_with: ء ن س, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ع ذ ب, ن ع م, و ت د, و د ي
  - themes: calendar_season, navigation_route, sky_astronomy, space
  - keywords: astronomy, navigation, space
- `ب ل د B005` — الحيرة والتبلد
  - activated_by_or_with: ء ن س, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د
  - themes: cognition, communication, emotion, fear_grief, posture_embodiment, proof_uncertainty, religion_worship, suffering_hardship
  - keywords: cognition, emotion, gesture, posture, psychology
- `ب ل د B006` — الأثر في الجلد والبدن
  - activated_by_or_with: ء ن س, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: anatomy, body, disease_injury, health_medicine, material, pattern_marking, proof_uncertainty, surface_shape
  - keywords: body, evidence, injury, marking, material, medicine, surface
- `ب ل د B007` — البلادة وضعف النفاذ
  - activated_by_or_with: ء ن س, ب ل و, ر ب ب, ر ص د, ص ب ب, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: agency_action, animal, capacity_ability, cognition, conflict, hospitality_welfare, intention_character, labor_work
  - keywords: animal, character, cognition, competition, generosity, labor, performance
- `ب ل د B008` — غلظ الخلق وعظم الجسم
  - activated_by_or_with: ء ن س, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: anatomy, animal, body, force_power, form_structure, material, measurement
  - keywords: anatomy, animal, body, mass, morphology
- `ب ل د B009` — الإقامة ولزوم البلد
  - activated_by_or_with: ء ن س, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: household_community, migration_displacement, place_location, social_relations
  - keywords: belonging, community, habitation, migration, place, settlement
- `ب ل د B010` — اللصوق بالأرض
  - activated_by_or_with: ء ن س, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: force_power, form_structure, geography_landscape, growth_decay, posture_embodiment, social_relations, storage_vessels, terrain_desert, water_hydrology
  - keywords: contact, decay, gravity, ground, posture, terrain, vessel, water
- `ب ل د B011` — المبالدة بالسيوف والعصي
  - activated_by_or_with: ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: conflict, force_power, geography_landscape, violence_warfare, weaponry
  - keywords: conflict, contest, force, ground, violence, warfare, weapon
- `ب ل د B012` — أدحي النعام
  - activated_by_or_with: ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ر م, ن ع م, و ت د, و د ي
  - themes: animal, habitat_ecology, reproduction_birth, terrain_desert, wildlife
  - keywords: animal, bird, desert, ecology, reproduction, zoology

### ك ث ر

- `ك ث ر B001` — الكثرة ونماء العدد
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ص ب ب, ص خ ر, ق و ل, ك ر م, ن ع م, و د ي
  - themes: abundance_scarcity, growth_decay, measurement, quantity_number, wealth_property
  - keywords: abundance, excess, growth, measure, number, quantity, wealth
- `ك ث ر B002` — المكاثرة والغلبة بالعدد
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ب ب, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ر م, ن ع م
  - themes: conflict, force_power, hierarchy_status, household_community, wealth_property
  - keywords: competition, demography, hierarchy, power, rivalry, status, wealth
- `ك ث ر B003` — كثرة في صاحب أو كلام أو مطالب
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ر م, ن ع م, و ت د, و د ي
  - themes: communication, honor_shame, language_speech, law, obligation_contract, provision_resource, support_dependence, wealth_property
  - keywords: communication, liability, obligation, patronage, reputation, resource, speech, wealth
- `ك ث ر B004` — الكوثر: خير كثير وفيض مخصوص
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ك ث ر B005` — كوثر الغبار وتكوثره
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ر م, ن ع م, و ت د, و د ي
  - themes: abundance_scarcity, concealment_disclosure, danger_harm, earth_geology, material, motion, weather_climate
  - keywords: atmosphere, excess, motion, storm
- `ك ث ر B006` — الكثر جمار النخل
  - activated_by_or_with: ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ع ذ ب, ك ر م, ن ع م, و د ي
  - themes: agriculture, food_nutrition, harvest_cultivation, plant_vegetation
  - keywords: agriculture, botany, food, fruit, plant
- `ك ث ر B007` — الكمثرة اجتماع الشيء
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ك ر م, ن ع م, و ت د, و د ي
  - themes: form_structure, measurement, quantity_number, substance_texture
  - keywords: mass, morphology, plurality

### ف س د

- `ف س د B001` — خروج الشيء عن الصلاح والاعتدال
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: craft, danger_harm, ethics_morality, health_medicine, hospitality_welfare, loss_absence, politics_order, value_quality
  - keywords: damage, destruction, ethics, loss, welfare

### ص ب ب

- `ص ب ب B001` — إراقة الشيء وانصبابه
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: abundance_scarcity, containment_access, force_power, motion, storage_vessels, substance_texture, water_hydrology
  - keywords: abundance, containment, fluid, gravity, hydrology, movement, vessel
- `ص ب ب B002` — حدور ومنصب
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ن ع م, و ت د, و د ي
  - themes: force_power, geography_landscape, navigation_route, terrain_desert, travel, water_hydrology
  - keywords: geography, gravity, hydrology, terrain, topography, travel
- `ص ب ب B003` — صبابة باقية
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص خ ر, ط غ ي, ع ذ ب, ف س د, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: abundance_scarcity, food_nutrition, loss_absence, measurement, provision_resource, quantity_number, storage_vessels, substance_texture
  - keywords: consumption, container, measure, residue, scarcity, sustenance, vessel
- `ص ب ب B004` — انصباب القلب بالهوى
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ط غ ي, ع ذ ب, ق و ل, ك ر م, ن ع م, و ت د
  - themes: cognition, desire_appetite, emotion, religion_worship, rhetoric_discourse, social_relations
  - keywords: affection, attachment, desire, devotion, emotion, psychology
- `ص ب ب B005` — صبة مجتمعة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ب ب, ر ص د, س و ط, ص خ ر, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: abundance_scarcity, food_nutrition, household_community, livestock, naming_classification, provision_resource, quantity_number
  - keywords: abundance, collective, community, food, livestock, quantity
- `ص ب ب B006` — صبيب أحمر أو عصارة
  - activated_by_or_with: ء ن س, ب ل د, ج و ب, ر ب ب, ر ص د, س و ط, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: body, plant_vegetation, substance_texture, visual_appearance, weather_climate
  - keywords: body, botany, color, fluid, substance, weather
- `ص ب ب B007` — ذهاب الصبابة وتفرقها
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص خ ر, ط غ ي, ع ذ ب, ف س د, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: abundance_scarcity, boundary, change_transition, danger_harm, growth_decay, loss_absence, migration_displacement, substance_texture
  - keywords: change, decay, destruction, loss, residue, scarcity, separation
- `ص ب ب B008` — انصباب الحية على الملدوغ
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: animal, danger_harm, disease_injury, habitat_ecology, motion, violence_warfare
  - keywords: animal, danger, injury, motion, violence
- `ص ب ب B009` — صب في القيد
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: body, control_restraint, law, protection_security, punishment_sanction
  - keywords: body, coercion, control, law, punishment, restraint, security
- `ص ب ب B010` — سير صبصاب
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: labor_work, motion, sequence_cycle, stability_endurance, travel
  - keywords: effort, endurance, locomotion, movement, travel
- `ص ب ب B011` — عثو في الغنم
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ب ب, ر ص د, س و ط, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: agriculture, conflict, danger_harm, ethics_morality, husbandry, law, livestock, stability_endurance, wealth_property
  - keywords: agriculture, conflict, damage, disorder, harm, livestock, pastoralism, property

### ر ب ب

- `ر ب ب B001` — ربوبية وملك وسيادة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: authority_governance, belief_revelation, force_power, hierarchy_status, religion_worship, support_dependence, wealth_property
  - keywords: authority, devotion, governance, hierarchy, patronage, power, property, theology
- `ر ب ب B002` — إصلاح وتربية وإتمام
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: agriculture, authority_governance, belief_revelation, craft, family, growth_decay, knowledge_learning, life_stage_aging, stability_endurance
  - keywords: agriculture, craft, education, growth, maintenance, providence, stewardship
- `ر ب ب B003` — علم رباني
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ص ب ب, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ر م, ن ع م
  - themes: cognition, ethics_morality, knowledge_learning, religion_worship
  - keywords: education, ethics, philosophy, religion
- `ر ب ب B004` — ربة وجماعات كثيرة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: household_community, kinship, quantity_number, social_relations, violence_warfare
  - keywords: collectivity, demography, kinship, number, society
- `ر ب ب B005` — ربيب وربيبة ورابة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: authority_governance, family, hospitality_welfare, household_community, kinship, reproduction_birth, support_dependence
  - keywords: dependency, household, kinship
- `ر ب ب B006` — رُبّ خاثر وإصلاح به
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: agency_action, food_nutrition, health_medicine, material, stability_endurance, substance_texture
  - keywords: food, leather, material, medicine, substance
- `ر ب ب B007` — لزوم وإقامة ودوام
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: animal, geography_landscape, motion, place_location, time, weather_climate
  - keywords: animal, geography, habitation, motion, movement, temporality, time, weather
- `ر ب ب B008` — رباب السحاب
  - activated_by_or_with: ب ل د, ج و ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: agriculture, habitat_ecology, reproduction_birth, sky_astronomy, water_hydrology, weather_climate
  - keywords: agriculture, ecology, fertility, sky, water, weather
- `ر ب ب B009` — شاة رُبّى وحداثة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ص د, س و ط, ص ب ب, ص خ ر, ع ذ ب, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: animal, food_nutrition, household_community, life_stage_aging, livestock, reproduction_birth, time
  - keywords: animal, birth, dairy, household, livestock, reproduction, temporality, time
- `ر ب ب B010` — ربابة تجمع القداح
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: abundance_scarcity, belief_revelation, material, proof_uncertainty, ritual, storage_vessels, tools_equipment, weaponry
  - keywords: fortune, leather, ritual, storage, tool, weapon
- `ر ب ب B011` — ربابة عهد وميثاق
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: finance_debt, household_community, law, obligation_contract, politics_order, protection_security, trust_loyalty
  - keywords: community, contract, diplomacy, law, protection, trust
- `ر ب ب B012` — ربة نبات
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: agriculture, food_nutrition, geography_landscape, habitat_ecology, physiology, plant_vegetation, visual_appearance
  - keywords: agriculture, botany, color, ecology, flora, food, landscape
- `ر ب ب B013` — ماء رَبَب كثير
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: abundance_scarcity, cooking_drink, geography_landscape, habitat_ecology, provision_resource, purity_cleansing, water_hydrology
  - keywords: abundance, ecology, geography, hydrology, nature, purity, resource, sustenance
- `ر ب ب B014` — رَبْرَب قطيع
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: animal, habitat_ecology, household_community, husbandry, livestock, quantity_number, terrain_desert, wildlife
  - keywords: collectivity, desert, ecology, hunting, livestock, pastoralism, plurality, zoology
- `ر ب ب B015` — حرف رب وربما
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, س و ط, ص ب ب, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د
  - themes: form_structure, grammar_expression, language_speech, quantity_number, rhetoric_discourse
  - keywords: discourse, grammar, linguistics, modality, morphology, rhetoric, semantics
- `ر ب ب B016` — رُبَى حاجة وعقدة ونعمة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: control_restraint, ethics_morality, hospitality_welfare, material, obligation_contract, social_relations, support_dependence
  - keywords: charity, dependency, ethics, fastening, gift, material, obligation, relation, welfare
- `ر ب ب B017` — رباني الملاحين
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ص د, ص ب ب, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: authority_governance, hierarchy_status, labor_work, navigation_route, transport, travel, water_hydrology
  - keywords: authority, hierarchy, navigation, transport, travel, water

### س و ط

- `س و ط B001` — خلط الشيء بالشيء
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: boundary, commerce_exchange, finance_debt, form_structure, social_relations, stability_endurance, substance_texture
  - keywords: boundary, commerce, disorder, finance, relation, substance
- `س و ط B002` — السَّوط والضرب به
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ط غ ي, ع ذ ب, ق و ل, ك ر م, ن ع م, و ت د, و د ي
  - themes: body, control_restraint, disease_injury, punishment_sanction, suffering_hardship, violence_warfare, weaponry
  - keywords: body, discipline, injury, pain, punishment, violence, weapon
- `س و ط B003` — سوط من العذاب
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `س و ط B004` — السُّويطاء المختلطة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: cooking_drink, food_nutrition, household_community, plant_vegetation, substance_texture
  - keywords: cuisine, domestic, food, fruit, nourishment

### ع ذ ب

- `ع ذ ب B001` — العذوبة والطيب في الماء والمطعوم
  - activated_by_or_with: ء ن س, ب ل د, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: cooking_drink, desire_appetite, food_nutrition, perception, purity_cleansing, water_hydrology
  - keywords: consumption, nourishment, pleasure, purity, water
- `ع ذ ب B002` — العذوب امتناع الجسد عن الأكل والشرب
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ط غ ي, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: desire_appetite, food_nutrition, loss_absence, physiology, religion_worship, stability_endurance
  - keywords: consumption, endurance, physiology
- `ع ذ ب B003` — الكف والمنع والفطام عن الشيء
  - activated_by_or_with: ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ط غ ي, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: boundary, control_restraint, law, rhetoric_discourse
  - keywords: boundary, control, discipline, restraint, separation
- `ع ذ ب B004` — العذوب المكشوف للسماء
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: architecture_construction, boundary, containment_access, danger_harm, habitat_ecology, protection_security, space, weather_climate
  - keywords: boundary, environment, protection, space, weather
- `ع ذ ب B005` — العذاب إيلام وعقوبة
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ط غ ي, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: control_restraint, danger_harm, justice_judgment, punishment_sanction, suffering_hardship, violence_warfare
  - keywords: coercion, harm, justice, pain, punishment, violence
- `ع ذ ب B006` — العذبة طرف أو علاقة متدلية
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ص خ ر, ق و ل, ك ر م, ن ع م, و ت د, و د ي
  - themes: anatomy, ornament_beauty, social_relations, textile_clothing, tools_equipment
  - keywords: anatomy, attachment, textile, tool
- `ع ذ ب B007` — العذبة شوائب الماء أو سطحه
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: earth_geology, habitat_ecology, purity_cleansing, stability_endurance, substance_texture, surface_shape, water_hydrology
  - keywords: ecology, maintenance, residue, surface, water
- `ع ذ ب B008` — العذبي كريم الأخلاق
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ط غ ي, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م
  - themes: ethics_morality, hierarchy_status, honor_shame, hospitality_welfare, intention_character, social_relations
  - keywords: beneficence, character, ethics, generosity, reputation, sociability, sociality, status, virtue
- `ع ذ ب B009` — العذابة والرحم والخرج بعد الولد
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: anatomy, change_transition, health_medicine, kinship, physiology, reproduction_birth, substance_texture
  - keywords: anatomy, birth, fluid, kinship, medicine, physiology, reproduction

### ر ص د

- `ر ص د B001` — التَّرَقُّب والحراسة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: boundary, danger_harm, motion, perception, protection_security, violence_warfare
  - keywords: boundary, perception, protection, security, surveillance, warfare
- `ر ص د B002` — الإعداد والإرصاد
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: capacity_ability, commerce_exchange, economy, finance_debt, hospitality_welfare, obligation_contract, place_location, provision_resource, reasoning_decision, support_dependence
  - keywords: distribution, economy, exchange, finance, gift, obligation, patronage, settlement
- `ر ص د B003` — موضع الرصد والطريق
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: boundary, danger_harm, geography_landscape, motion, navigation_route, protection_security, space, travel, wildlife
  - keywords: danger, geography, hunting, movement, passage, space, surveillance, travel
- `ر ص د B004` — مطر الرَّصَد وكلؤه
  - activated_by_or_with: ب ل د, ج و ب, ر ب ب, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: agriculture, change_transition, food_nutrition, habitat_ecology, pasture_forage, reproduction_birth, water_hydrology, weather_climate
  - keywords: agriculture, ecology, fertility, nourishment, pasture, renewal, water, weather

### ء ن س

- `ء ن س B001` — ظهور الإنسان المخالف للتوحش والجن
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: belief_revelation, household_community, identity_personhood, place_location, social_relations
  - keywords: anthropology, community, demography, habitation, identity, sociality, society
- `ء ن س B002` — إيناس الشيء برؤية أو إحساس أو سماع
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ع ذ ب, ق و ل, ن ع م
  - themes: cognition, knowledge_learning, memory_attention, perception, proof_uncertainty
  - keywords: attention, cognition, evidence, knowledge, perception
- `ء ن س B003` — الأنس الذي يزيل الوحشة
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: emotion, health_medicine, hospitality_welfare, household_community, husbandry, social_relations
  - keywords: attachment, comfort, community, companionship, domestication, emotion, hospitality, wellbeing
- `ء ن س B004` — الجانب الإنسي المقبل على الإنسان
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ر م, ن ع م, و ت د, و د ي
  - themes: anatomy, navigation_route, orientation_direction, posture_embodiment, reasoning_decision, social_relations, space, tools_equipment
  - keywords: anatomy, embodiment, equipment, navigation, orientation, relation
- `ء ن س B005` — إنسان العين وصورة الإنسان في السواد
  - activated_by_or_with: ب ل د, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ع ذ ب, ق و ل, ك ر م, ن ع م, و ت د, و د ي
  - themes: anatomy, body, cognition, perception, posture_embodiment, visual_appearance
  - keywords: anatomy, body, embodiment, perception, vision
- `ء ن س B006` — ابن الإنس للنفس والصفوة
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ع ذ ب, ق و ل, ك ر م, ن ع م, و ت د, و د ي
  - themes: identity_personhood, kinship, sexuality, social_relations, trust_loyalty
  - keywords: affiliation, companionship, identity, kinship, loyalty
- `ء ن س B007` — الاستئناس قبل دخول البيوت
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### ب ل و

- `ب ل و B001` — البلى والاهتراء
  - activated_by_or_with: ب ل د, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: earth_geology, growth_decay, material, physiology, stability_endurance, textile_clothing, time, travel
  - keywords: material, textile, time, travel
- `ب ل و B002` — الاختبار وظهور الحال
  - activated_by_or_with: ء ن س, ب ل د, ج و ب, ر ب ب, ر ص د, ص ب ب, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ر م, ن ع م, و ت د, و د ي
  - themes: agency_action, ethics_morality, justice_judgment, knowledge_learning, proof_uncertainty, reasoning_decision, value_quality
  - keywords: ethics, judgment, knowledge, morality, performance, quality
- `ب ل و B003` — البلاء بالحسن والصنيع الجميل
  - activated_by_or_with: ء ن س, ب ل د, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: commerce_exchange, ethics_morality, hospitality_welfare, intention_character, support_dependence, value_quality, violence_warfare
  - keywords: ethics, generosity, merit, patronage, reciprocity, virtue, warfare, welfare
- `ب ل و B004` — إبلاء العذر واليمين
  - activated_by_or_with: ء ن س, ب ل د, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: ethics_morality, justice_judgment, language_speech, law, obligation_contract, social_relations, testimony_witness, trust_loyalty
  - keywords: accountability, law, liability, speech, testimony, trust
- `ب ل و B005` — بلية القبر والراحلة
  - activated_by_or_with: ب ل د, ج و ب, ر ب ب, ص ب ب, ق و ل, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: animal, culture_tradition, fear_grief, mortality_death, ritual, wealth_property
  - keywords: animal, burial, death, ownership, ritual
- `ب ل و B006` — جواب بلى ورد النفي
  - activated_by_or_with: ء ن س, ب ل د, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د
  - themes: communication, grammar_expression, language_speech, proof_uncertainty, reasoning_decision, rhetoric_discourse
  - keywords: communication, discourse, grammar, language, logic, semantics, truth
- `ب ل و B007` — عدم المبالاة وعدم الاكتراث
  - activated_by_or_with: ء ن س, ب ل د, ر ص د, س و ط, ص ب ب, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ر م, ن ع م, و د ي
  - themes: boundary, emotion, intention_character, justice_judgment, memory_attention, sequence_cycle, value_quality
  - keywords: attention, emotion, judgment, value
- `ب ل و B008` — اسم حي ونسبة
  - activated_by_or_with: ء ن س, ب ل د, ج و ب, ر ب ب, س و ط, ص ب ب, ص خ ر, ع ذ ب, ق و ل, ك ر م, ن ع م, و د ي
  - themes: identity_personhood, kinship, naming_classification, social_relations
  - keywords: anthropology, identity, kinship, sociality, society, taxonomy
- `ب ل و B009` — التفرق في الجهات
  - activated_by_or_with: ء ن س, ب ل د, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: boundary, geography_landscape, household_community, migration_displacement, motion, provision_resource, quantity_number, space
  - keywords: community, distribution, geography, migration, motion, movement, plurality, separation, space

### ك ر م

- `ك ر م B001` — الشرف والجود المحمود
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ب ب, ر ص د, ص ب ب, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ن ع م
  - themes: ethics_morality, hierarchy_status, honor_shame, hospitality_welfare, value_quality
  - keywords: beneficence, esteem, ethics, hospitality, merit, status, virtue
- `ك ر م B002` — جودة النبات والغيث
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ن ع م, و ت د, و د ي
  - themes: abundance_scarcity, agriculture, food_nutrition, growth_decay, habitat_ecology, provision_resource, reproduction_birth, weather_climate
  - keywords: abundance, agriculture, ecology, fertility, growth, nourishment, sustenance, weather
- `ك ر م B003` — الكَرْم المنظوم في العنق
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ص خ ر, ع ذ ب, ف س د, ق و ل, ك ث ر, ن ع م, و ت د
  - themes: body, craft, hierarchy_status, ornament_beauty, textile_clothing
  - keywords: body, clothing, craft, status
- `ك ر م B004` — العنب والكرمة
  - activated_by_or_with: ب ل د, ب ل و, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ع ذ ب, ك ث ر, ن ع م, و د ي
  - themes: abundance_scarcity, agriculture, food_nutrition, growth_decay, harvest_cultivation, plant_vegetation
  - keywords: abundance, agriculture, botany, cultivation, food, fruit, growth, plant
- `ك ر م B005` — طبق على رأس الوعاء
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ع ذ ب, ق و ل, ك ث ر, ن ع م, و د ي
  - themes: containment_access, household_community, protection_security, storage_vessels, tools_equipment
  - keywords: containment, household, protection, storage, vessel
- `ك ر م B006` — مفاخرة الكرم والغلبة فيه
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ن ع م
  - themes: conflict, ethics_morality, hierarchy_status, honor_shame, rhetoric_discourse, social_relations
  - keywords: competition, contest, honor, rhetoric, rivalry, status, virtue
- `ك ر م B007` — رأس الفخذ المستدير
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ن ع م, و ت د, و د ي
  - themes: anatomy, body, form_structure, health_medicine, motion
  - keywords: anatomy, body, locomotion, medicine, morphology, movement
- `ك ر م B008` — هدية تطلب المكافأة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ن ع م, و ت د, و د ي
  - themes: commerce_exchange, economy, honor_shame, hospitality_welfare, intention_character, justice_judgment, support_dependence
  - keywords: economy, exchange, gift, patronage, praise, reciprocity
- `ك ر م B009` — جواب الرضا والكرامة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ن ع م, و د ي
  - themes: authority_governance, belief_revelation, ethics_morality, hospitality_welfare, language_speech, rhetoric_discourse, ritual, social_relations
  - keywords: blessing, discourse, hospitality, ritual, speech
- `ك ر م B010` — العزيز الذي يكرم عليك
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ع ذ ب, ف س د, ق و ل, ك ث ر, ن ع م, و د ي
  - themes: emotion, hierarchy_status, honor_shame, kinship, social_relations, trust_loyalty, value_quality
  - keywords: affection, attachment, esteem, hierarchy, honor, kinship, loyalty, status, value

### ن ع م

- `ن ع م B001` — حسن الحال والنعمة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, و ت د, و د ي
  - themes: abundance_scarcity, belief_revelation, commerce_exchange, ethics_morality, hospitality_welfare, support_dependence
  - keywords: abundance, charity, ethics, fortune, generosity, patronage, providence, reciprocity, welfare
- `ن ع م B002` — اللين والنعومة ورفاه العيش
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, و ت د, و د ي
  - themes: abundance_scarcity, body, desire_appetite, health_medicine, hierarchy_status, material, perception, value_quality, wealth_property
  - keywords: body, comfort, material, pleasure, sensation, status, wealth
- `ن ع م B003` — مدح الشيء بنعم
  - activated_by_or_with: ء ن س, ب ل و, ج و ب, ر ب ب, ص ب ب, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, و ت د, و د ي
  - themes: grammar_expression, honor_shame, justice_judgment, language_speech, orientation_direction, rhetoric_discourse, value_quality
  - keywords: grammar, judgment, praise, quality, rhetoric, speech
- `ن ع م B004` — الجواب بنعم والتصديق
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ع ذ ب, ق و ل, ك ث ر, ك ر م, و ت د, و د ي
  - themes: communication, grammar_expression, language_speech, obligation_contract, proof_uncertainty, reasoning_decision, social_relations, testimony_witness
  - keywords: agreement, communication, dialogue, interaction, language, logic, modality, testimony, truth
- `ن ع م B005` — مال الأنعام والإبل
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ب ب, ر ص د, ص ب ب, ص خ ر, ق و ل, ك ث ر, ك ر م, و د ي
  - themes: agriculture, animal, economy, husbandry, pasture_forage, provision_resource, wealth_property
  - keywords: agriculture, animal, domestication, economy, pastoralism, pasture, wealth
- `ن ع م B006` — النعام والنعامة الطائر
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, و ت د, و د ي
  - themes: animal, habitat_ecology, motion, naming_classification, terrain_desert, wildlife
  - keywords: animal, bird, desert, motion, nature, taxonomy, zoology
- `ن ع م B007` — ما سمي نعامة تشبيها بالهيئة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ر م, و ت د, و د ي
  - themes: anatomy, geography_landscape, naming_classification, reasoning_decision, rhetoric_discourse, sky_astronomy, surface_shape, terrain_desert, tools_equipment
  - keywords: anatomy, astronomy, landscape, metaphor, shape, tool, topography
- `ن ع م B008` — طيران النعامة وتفرق القوم
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, و ت د, و د ي
  - themes: change_transition, household_community, loss_absence, migration_displacement, motion, rhetoric_discourse, social_relations, violence_warfare
  - keywords: collective, loss, metaphor, migration, movement, society, warfare
- `ن ع م B009` — النعامى ريح لينة
  - activated_by_or_with: ء ن س, ب ل د, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, و ت د, و د ي
  - themes: calendar_season, habitat_ecology, health_medicine, orientation_direction, perception, substance_texture, weather_climate
  - keywords: atmosphere, comfort, nature, sensation, weather
- `ن ع م B010` — زاد وأنعم في الفعل
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, و د ي
  - themes: agency_action, change_transition, measurement, quantity_number, rhetoric_discourse, sequence_cycle
  - keywords: change, measure, performance, quantity, rhetoric
- `ن ع م B011` — موافقة المكان وطيب المقام
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ر م, و ت د, و د ي
  - themes: architecture_construction, geography_landscape, habitat_ecology, health_medicine, hospitality_welfare, place_location, social_relations, travel
  - keywords: belonging, comfort, environment, geography, habitation, hospitality, place, settlement, travel
- `ن ع م B012` — المشي على القدم وابتذالها
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ط غ ي, ع ذ ب, ق و ل, ك ث ر, ك ر م, و ت د, و د ي
  - themes: body, labor_work, motion, social_relations, stability_endurance, transport, travel
  - keywords: body, contact, effort, endurance, labor, locomotion, movement, service, transport, travel
- `ن ع م B013` — نعم الله بك عينا وقرة العين
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ق و ل, ك ث ر, ك ر م, و د ي
  - themes: belief_revelation, emotion, health_medicine, honor_shame, perception, prayer_supplication
  - keywords: affection, blessing, emotion, honor, prayer, vision, wellbeing

### ق و ل

- `ق و ل B001` — إخراج القول بالنطق
  - activated_by_or_with: ب ل د, ب ل و, ج و ب, ر ب ب, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ك ث ر, ك ر م, ن ع م
  - themes: agency_action, communication, language_speech, rhetoric_discourse
  - keywords: communication, discourse, language, linguistics, performance, rhetoric
- `ق و ل B002` — اللسان آلة القول
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ص خ ر, ع ذ ب, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: anatomy, body, communication, grammar_expression, language_speech, physiology
  - keywords: anatomy, body, communication, language, physiology, speech
- `ق و ل B003` — كثرة القول في صاحبه
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ص خ ر, ع ذ ب, ك ث ر, ك ر م, ن ع م
  - themes: communication, intention_character, rhetoric_discourse, social_relations
  - keywords: character, communication, rhetoric, sociability, sociality
- `ق و ل B004` — القيل صاحب القول النافذ
  - activated_by_or_with: ر ب ب, ط غ ي, ع ذ ب, ف س د, ك ث ر, ك ر م, ن ع م
  - themes: authority_governance, hierarchy_status, politics_order
  - keywords: authority, governance, hierarchy
- `ق و ل B005` — قول ما لم يكن أو نسبته
  - activated_by_or_with: ب ل و, ج و ب, ر ب ب, ص ب ب, ط غ ي, ع ذ ب, ف س د, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: deception_corruption, ethics_morality, honor_shame, justice_judgment, rhetoric_discourse, testimony_witness
  - keywords: accountability, deception, discourse, ethics, reputation, testimony
- `ق و ل B006` — اجترار القول إلى النفس
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ك ث ر, ك ر م, ن ع م
  - themes: agency_action, communication, ethics_morality, honor_shame, identity_personhood, rhetoric_discourse, wealth_property
  - keywords: agency, communication, discourse, identity, morality, ownership, reputation
- `ق و ل B007` — القول الفاشي بين الناس
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ص خ ر, ع ذ ب, ك ث ر, ك ر م, ن ع م
  - themes: communication, concealment_disclosure, honor_shame, social_relations
  - keywords: communication, reputation, sociality, society
- `ق و ل B008` — عود القال لضرب القلة
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ف س د, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: craft, force_power, material, motion, tools_equipment
  - keywords: craft, impact, material, motion, tool
- `ق و ل B009` — المقاولة في الأمر
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ص خ ر, ع ذ ب, ف س د, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: commerce_exchange, communication, obligation_contract, politics_order, reasoning_decision, social_relations
  - keywords: agreement, commerce, communication, diplomacy
- `ق و ل B010` — اقتالة الحكم على غيره
  - activated_by_or_with: ب ل د, ب ل و, ر ب ب, س و ط, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ك ث ر, ك ر م, ن ع م, و ت د, و د ي
  - themes: authority_governance, conflict, control_restraint, force_power, hierarchy_status, law
  - keywords: authority, conflict, governance, hierarchy, law, power
- `ق و ل B011` — قول يجري مجرى الظن
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ك ث ر, ك ر م, ن ع م, و ت د
  - themes: cognition, grammar_expression, knowledge_learning, language_speech, reasoning_decision
  - keywords: cognition, grammar, language, modality
- `ق و ل B012` — قول في النفس لم يظهر
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ص ب ب, ع ذ ب, ك ث ر, ك ر م, ن ع م
  - themes: cognition, concealment_disclosure, containment_access, intention_character, language_speech
  - keywords: cognition, language, psychology
- `ق و ل B013` — القول اعتقاد ومذهب
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, س و ط, ص ب ب, ط غ ي, ع ذ ب, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: belief_revelation, cognition, culture_tradition, law, religion_worship, social_relations
  - keywords: affiliation, law, philosophy, religion, theology
- `ق و ل B014` — قول الشيء دلالته
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, ص ب ب, ص خ ر, ط غ ي, ع ذ ب, ك ث ر, ك ر م, ن ع م
  - themes: communication, habitat_ecology, language_speech, perception, proof_uncertainty, rhetoric_discourse
  - keywords: environment, evidence, metaphor, perception
- `ق و ل B015` — العناية الصادقة بالشيء
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ج و ب, ر ب ب, ر ص د, س و ط, ص ب ب, ط غ ي, ع ذ ب, ف س د, ك ث ر, ك ر م, ن ع م, و د ي
  - themes: authority_governance, ethics_morality, hospitality_welfare, labor_work, obligation_contract, religion_worship, social_relations
  - keywords: attachment, devotion, ethics, service, stewardship
- `ق و ل B016` — قول الشيء حده
  - activated_by_or_with: ء ن س, ب ل د, ب ل و, ر ب ب, ر ص د, ص ب ب, ص خ ر, ن ع م, و ت د
  - themes: cognition, naming_classification, reasoning_decision
  - keywords: logic, philosophy, taxonomy
- `ق و ل B017` — القول إلهام يلقي معنى
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
