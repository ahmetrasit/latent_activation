# v11 Activation Packet — S102:1-None

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_1: أَلْهَىٰكُمُ ٱلتَّكَاثُرُ
- verse_2: حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ
- verse_3: كَلَّا سَوْفَ تَعْلَمُونَ
- verse_4: ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ
- verse_5: كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ
- verse_6: لَتَرَوُنَّ ٱلْجَحِيمَ
- verse_7: ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ
- verse_8: ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ل ه و → ك ث ر → ز و ر → ق ب ر → ع ل م → ي ق ن → ر ء ي → ج ح م → ع ي ن → س ء ل → ن ع م

## Branch inventory summary

- ل ه و: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- ك ث ر: 7 branches (6 with Qnet bridge-theme nodes; 1 Furūq-only)
- ز و ر: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ق ب ر: 5 branches (4 with Qnet bridge-theme nodes; 1 Furūq-only)
- ع ل م: 7 branches (6 with Qnet bridge-theme nodes; 1 Furūq-only)
- ي ق ن: 2 branches (2 with Qnet bridge-theme nodes; 0 Furūq-only)
- ر ء ي: 13 branches (13 with Qnet bridge-theme nodes; 0 Furūq-only)
- ج ح م: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- ع ي ن: 17 branches (17 with Qnet bridge-theme nodes; 0 Furūq-only)
- س ء ل: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن ع م: 13 branches (13 with Qnet bridge-theme nodes; 0 Furūq-only)

## QAC-first root resolution audit

- ل ه و | qac_keys=لهو | status=resolved | matches=root_001382
- ك ث ر | qac_keys=كثر | status=resolved | matches=root_001286
- ز و ر | qac_keys=زور | status=resolved | matches=root_000654
- ق ب ر | qac_keys=قبر | status=resolved | matches=root_001195
- ع ل م | qac_keys=علم | status=resolved | matches=root_001040
- ي ق ن | qac_keys=يقن | status=resolved | matches=root_001696
- ر ء ي | qac_keys=رءي | status=resolved | matches=root_000531
- ج ح م | qac_keys=جحم | status=resolved | matches=root_000225
- ع ي ن | qac_keys=عين | status=resolved | matches=root_001069
- س ء ل | qac_keys=سءل | status=resolved | matches=root_000661
- ن ع م | qac_keys=نعم | status=resolved | matches=root_001525

## Top candidate bridges

- `ع ي ن B010` ↔ `ن ع م B009` | score_hint=23 | discovery_hint=19 | themes=calendar_season, orientation_direction, weather_climate | keywords=climate, direction, season, weather | q2=—
- `ر ء ي B010` ↔ `ن ع م B005` | score_hint=19 | discovery_hint=18 | themes=agriculture, animal, husbandry | keywords=agriculture, animal, herding | q2=—
- `ل ه و B003` ↔ `ن ع م B005` | score_hint=15 | discovery_hint=18 | themes=agriculture, economy, provision_resource | keywords=agriculture, economy | q2=—
- `ل ه و B003` ↔ `ك ث ر B006` | score_hint=13 | discovery_hint=18 | themes=agriculture, food_nutrition | keywords=agriculture, food | q2=—
- `ز و ر B002` ↔ `ر ء ي B005` | score_hint=19 | discovery_hint=17 | themes=deception_corruption, ethics_morality, religion_worship | keywords=deception, ethics, religion | q2=—
- `ل ه و B004` ↔ `ر ء ي B009` | score_hint=22 | discovery_hint=16 | themes=anatomy, body, physiology | keywords=anatomy, body, organ, respiration | q2=—
- `ل ه و B002` ↔ `ع ي ن B015` | score_hint=13 | discovery_hint=16 | themes=family, kinship | keywords=family, kinship | q2=—
- `ع ي ن B008` ↔ `ن ع م B007` | score_hint=7 | discovery_hint=16 | themes=sky_astronomy | keywords=astronomy | q2=—
- `ع ي ن B009` ↔ `ن ع م B007` | score_hint=30 | discovery_hint=15 | themes=anatomy, reasoning_decision, surface_shape, terrain_desert, tools_equipment | keywords=analogy, anatomy, shape, tool, topography | q2=—
- `ق ب ر B004` ↔ `ج ح م B004` | score_hint=28 | discovery_hint=15 | themes=anatomy, body, emotion, grammar_expression | keywords=anger, body, emotion, expression, face | q2=—
- `ر ء ي B007` ↔ `ر ء ي B010` | score_hint=12 | discovery_hint=15 | themes=body, reproduction_birth | keywords=body, fertility | q2=—
- `ع ي ن B011` ↔ `ع ي ن B012` | score_hint=12 | discovery_hint=15 | themes=commerce_exchange, finance_debt | keywords=commerce, finance | q2=—
- `ز و ر B005` ↔ `ع ي ن B005` | score_hint=9 | discovery_hint=15 | themes=communication, politics_order | keywords=politics | q2=—
- `ع ي ن B002` ↔ `ن ع م B004` | score_hint=9 | discovery_hint=15 | themes=proof_uncertainty, testimony_witness | keywords=testimony | q2=—
- `ك ث ر B007` ↔ `ع ل م B004` | score_hint=7 | discovery_hint=15 | themes=form_structure | keywords=morphology | q2=—
- `ز و ر B007` ↔ `ع ل م B006` | score_hint=7 | discovery_hint=15 | themes=speed | keywords=speed | q2=—
- `ز و ر B007` ↔ `ن ع م B012` | score_hint=24 | discovery_hint=14 | themes=labor_work, motion, stability_endurance, travel | keywords=effort, endurance, movement, travel | q2=—
- `ق ب ر B003` ↔ `ن ع م B006` | score_hint=22 | discovery_hint=14 | themes=animal, naming_classification, wildlife | keywords=animal, bird, taxonomy, wildlife | q2=—
- `ز و ر B004` ↔ `ر ء ي B009` | score_hint=18 | discovery_hint=14 | themes=anatomy, body, health_medicine | keywords=anatomy, body, medicine | q2=—
- `ز و ر B004` ↔ `ع ي ن B016` | score_hint=18 | discovery_hint=14 | themes=anatomy, animal, body | keywords=anatomy, animal, body | q2=—
- `ق ب ر B004` ↔ `ع ل م B004` | score_hint=16 | discovery_hint=14 | themes=anatomy, body | keywords=anatomy, body, physiognomy | q2=—
- `ل ه و B003` ↔ `س ء ل B003` | score_hint=14 | discovery_hint=14 | themes=commerce_exchange, hospitality_welfare, provision_resource | keywords=generosity, provision | q2=—
- `ق ب ر B001` ↔ `ر ء ي B007` | score_hint=7 | discovery_hint=14 | themes=ritual | keywords=ritual | q2=—
- `ق ب ر B001` ↔ `ج ح م B002` | score_hint=7 | discovery_hint=14 | themes=mortality_death | keywords=death | q2=—
- `ي ق ن B001` ↔ `ع ي ن B002` | score_hint=22 | discovery_hint=13 | themes=knowledge_learning, perception, proof_uncertainty | keywords=epistemology, evidence, knowledge, perception | q2=—
- `ع ل م B006` ↔ `ن ع م B006` | score_hint=20 | discovery_hint=13 | themes=animal, habitat_ecology, naming_classification, wildlife | keywords=taxonomy, wildlife, zoology | q2=—
- `ع ل م B007` ↔ `ن ع م B006` | score_hint=20 | discovery_hint=13 | themes=animal, habitat_ecology, naming_classification, wildlife | keywords=taxonomy, wildlife, zoology | q2=—
- `ر ء ي B005` ↔ `ج ح م B005` | score_hint=20 | discovery_hint=13 | themes=ethics_morality, honor_shame, intention_character, social_relations | keywords=ethics, sociality, society | q2=—
- `ق ب ر B003` ↔ `ع ل م B006` | score_hint=18 | discovery_hint=13 | themes=animal, naming_classification, wildlife | keywords=ornithology, taxonomy, wildlife | q2=—
- `ع ل م B005` ↔ `ع ي ن B006` | score_hint=18 | discovery_hint=13 | themes=geography_landscape, habitat_ecology, water_hydrology | keywords=hydrology, nature, water | q2=—
- `ج ح م B003` ↔ `ع ي ن B016` | score_hint=18 | discovery_hint=13 | themes=anatomy, animal, perception | keywords=anatomy, animal, vision | q2=—
- `ر ء ي B009` ↔ `ج ح م B003` | score_hint=16 | discovery_hint=13 | themes=anatomy, disease_injury | keywords=anatomy, disease, illness | q2=—
- `ر ء ي B013` ↔ `ن ع م B004` | score_hint=16 | discovery_hint=13 | themes=communication, language_speech | keywords=communication, dialogue, language | q2=—
- `س ء ل B004` ↔ `ن ع م B004` | score_hint=16 | discovery_hint=13 | themes=communication, social_relations | keywords=communication, dialogue, interaction | q2=—
- `ع ل م B004` ↔ `ر ء ي B009` | score_hint=16 | discovery_hint=13 | themes=anatomy, body, disease_injury, health_medicine | keywords=anatomy, body | q2=—
- `ز و ر B004` ↔ `ع ل م B004` | score_hint=14 | discovery_hint=13 | themes=anatomy, body, health_medicine | keywords=anatomy, body | q2=—
- `ز و ر B004` ↔ `ع ي ن B009` | score_hint=14 | discovery_hint=13 | themes=anatomy, body, tools_equipment | keywords=anatomy, body | q2=—
- `ع ل م B002` ↔ `ر ء ي B011` | score_hint=14 | discovery_hint=13 | themes=communication, identity_personhood, pattern_marking | keywords=identity, symbol | q2=—
- `ع ل م B004` ↔ `ع ي ن B009` | score_hint=14 | discovery_hint=13 | themes=anatomy, body, pattern_marking | keywords=anatomy, body | q2=—
- `ر ء ي B006` ↔ `ع ي ن B016` | score_hint=14 | discovery_hint=13 | themes=body, ornament_beauty, perception | keywords=beauty, body | q2=—
- `ر ء ي B010` ↔ `ع ي ن B016` | score_hint=14 | discovery_hint=13 | themes=animal, body, perception | keywords=animal, body | q2=—
- `ل ه و B004` ↔ `ز و ر B004` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ل ه و B004` ↔ `ق ب ر B004` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ل ه و B004` ↔ `ع ل م B004` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ل ه و B004` ↔ `ع ي ن B009` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ل ه و B004` ↔ `ع ي ن B016` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ك ث ر B001` ↔ `ن ع م B010` | score_hint=12 | discovery_hint=13 | themes=measurement, quantity_number | keywords=measure, quantity | q2=—
- `ك ث ر B002` ↔ `ن ع م B002` | score_hint=12 | discovery_hint=13 | themes=hierarchy_status, wealth_property | keywords=status, wealth | q2=—
- `ز و ر B004` ↔ `ق ب ر B004` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ز و ر B004` ↔ `ر ء ي B007` | score_hint=12 | discovery_hint=13 | themes=body, health_medicine | keywords=body, medicine | q2=—
- `ز و ر B004` ↔ `ر ء ي B010` | score_hint=12 | discovery_hint=13 | themes=animal, body | keywords=animal, body | q2=—
- `ز و ر B008` ↔ `ق ب ر B002` | score_hint=12 | discovery_hint=13 | themes=material, plant_vegetation | keywords=material, plant | q2=—
- `ق ب ر B004` ↔ `ر ء ي B009` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ق ب ر B004` ↔ `ع ي ن B009` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ق ب ر B004` ↔ `ع ي ن B016` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ع ل م B004` ↔ `ع ي ن B016` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ي ق ن B002` ↔ `ع ي ن B003` | score_hint=12 | discovery_hint=13 | themes=honor_shame, protection_security | keywords=honor, protection | q2=—
- `ر ء ي B009` ↔ `ع ي ن B009` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ر ء ي B009` ↔ `ع ي ن B016` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ج ح م B004` ↔ `ع ي ن B009` | score_hint=10 | discovery_hint=13 | themes=anatomy, body, measurement | keywords=body | q2=—
- `ك ث ر B003` ↔ `ن ع م B005` | score_hint=8 | discovery_hint=13 | themes=provision_resource, wealth_property | keywords=wealth | q2=—
- `ي ق ن B001` ↔ `ر ء ي B001` | score_hint=22 | discovery_hint=12 | themes=cognition, knowledge_learning, perception | keywords=cognition, epistemology, knowledge, perception | q2=—
- `ي ق ن B001` ↔ `ر ء ي B002` | score_hint=20 | discovery_hint=12 | themes=cognition, justice_judgment, knowledge_learning, proof_uncertainty | keywords=cognition, judgment, knowledge | q2=—
- `ز و ر B002` ↔ `ي ق ن B001` | score_hint=18 | discovery_hint=12 | themes=justice_judgment, knowledge_learning, proof_uncertainty | keywords=epistemology, judgment, truth | q2=—
- `ر ء ي B001` ↔ `ع ي ن B002` | score_hint=16 | discovery_hint=12 | themes=knowledge_learning, perception | keywords=epistemology, knowledge, perception | q2=—
- `ج ح م B003` ↔ `ع ي ن B001` | score_hint=16 | discovery_hint=12 | themes=anatomy, perception | keywords=anatomy, perception, vision | q2=—
- `ك ث ر B003` ↔ `س ء ل B001` | score_hint=16 | discovery_hint=12 | themes=communication, language_speech, obligation_contract, support_dependence | keywords=communication, speech | q2=—
- `ز و ر B003` ↔ `ن ع م B011` | score_hint=14 | discovery_hint=12 | themes=hospitality_welfare, social_relations, travel | keywords=hospitality, travel | q2=—
- `ق ب ر B003` ↔ `ع ل م B007` | score_hint=14 | discovery_hint=12 | themes=animal, naming_classification, wildlife | keywords=taxonomy, wildlife | q2=—
- `ع ل م B002` ↔ `ع ي ن B010` | score_hint=14 | discovery_hint=12 | themes=geography_landscape, navigation_route, orientation_direction | keywords=geography, navigation | q2=—
- `ر ء ي B012` ↔ `ع ي ن B002` | score_hint=14 | discovery_hint=12 | themes=knowledge_learning, perception, proof_uncertainty | keywords=evidence, perception | q2=—
- `ل ه و B002` ↔ `ز و ر B003` | score_hint=12 | discovery_hint=12 | themes=desire_appetite, kinship | keywords=desire, kinship | q2=—
- `ل ه و B004` ↔ `ع ي ن B001` | score_hint=12 | discovery_hint=12 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ك ث ر B003` ↔ `ر ء ي B013` | score_hint=12 | discovery_hint=12 | themes=communication, language_speech | keywords=communication, speech | q2=—
- `ز و ر B002` ↔ `ن ع م B003` | score_hint=12 | discovery_hint=12 | themes=justice_judgment, language_speech | keywords=judgment, speech | q2=—
- `ز و ر B002` ↔ `ن ع م B004` | score_hint=12 | discovery_hint=12 | themes=language_speech, proof_uncertainty | keywords=language, truth | q2=—
- `ز و ر B003` ↔ `ع ي ن B015` | score_hint=12 | discovery_hint=12 | themes=kinship, social_relations | keywords=kinship, society | q2=—
- `ز و ر B003` ↔ `ع ي ن B017` | score_hint=12 | discovery_hint=12 | themes=household_community, social_relations | keywords=community, society | q2=—
- `ز و ر B004` ↔ `ج ح م B003` | score_hint=12 | discovery_hint=12 | themes=anatomy, animal | keywords=anatomy, animal | q2=—
- `ز و ر B004` ↔ `ع ي ن B001` | score_hint=12 | discovery_hint=12 | themes=anatomy, body | keywords=anatomy, body | q2=—

## Per-root candidate activations

### ل ه و

- `ل ه و B001` — شغل عن الشيء بغيره
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ل ه و B002` — لعب واستمتاع يكنى به
  - activated_by_or_with: ز و ر, ع ي ن
  - themes: desire_appetite, family, kinship
  - keywords: desire, family, kinship
- `ل ه و B003` — طرح الشيء في فم الرحى والعطاء المشبه به
  - activated_by_or_with: س ء ل, ك ث ر, ن ع م
  - themes: agriculture, commerce_exchange, economy, food_nutrition, hospitality_welfare, provision_resource
  - keywords: agriculture, economy, food, generosity, provision
- `ل ه و B004` — لحمة أقصى الفم المشرفة على الحلق
  - activated_by_or_with: ر ء ي, ز و ر, ع ل م, ع ي ن, ق ب ر
  - themes: anatomy, body, physiology
  - keywords: anatomy, body, organ, respiration

### ك ث ر

- `ك ث ر B001` — الكثرة ونماء العدد
  - activated_by_or_with: ن ع م
  - themes: measurement, quantity_number
  - keywords: measure, quantity
- `ك ث ر B002` — المكاثرة والغلبة بالعدد
  - activated_by_or_with: ن ع م
  - themes: hierarchy_status, wealth_property
  - keywords: status, wealth
- `ك ث ر B003` — كثرة في صاحب أو كلام أو مطالب
  - activated_by_or_with: ر ء ي, س ء ل, ن ع م
  - themes: communication, language_speech, obligation_contract, provision_resource, support_dependence, wealth_property
  - keywords: communication, speech, wealth
- `ك ث ر B004` — الكوثر: خير كثير وفيض مخصوص
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ك ث ر B005` — كوثر الغبار وتكوثره
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ك ث ر B006` — الكثر جمار النخل
  - activated_by_or_with: ل ه و
  - themes: agriculture, food_nutrition
  - keywords: agriculture, food
- `ك ث ر B007` — الكمثرة اجتماع الشيء
  - activated_by_or_with: ع ل م
  - themes: form_structure
  - keywords: morphology

### ز و ر

- `ز و ر B001` — الميل والعدول
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ز و ر B002` — الزور كذب وباطل
  - activated_by_or_with: ر ء ي, ن ع م, ي ق ن
  - themes: deception_corruption, ethics_morality, justice_judgment, knowledge_learning, language_speech, proof_uncertainty, religion_worship
  - keywords: deception, epistemology, ethics, judgment, language, religion, speech, truth
- `ز و ر B003` — زيارة وقصد الزائر
  - activated_by_or_with: ع ي ن, ل ه و, ن ع م
  - themes: desire_appetite, hospitality_welfare, household_community, kinship, social_relations, travel
  - keywords: community, desire, hospitality, kinship, society, travel
- `ز و ر B004` — زَوْر الصدر وميله
  - activated_by_or_with: ج ح م, ر ء ي, ع ل م, ع ي ن, ق ب ر, ل ه و
  - themes: anatomy, animal, body, health_medicine, tools_equipment
  - keywords: anatomy, animal, body, medicine
- `ز و ر B005` — مرجع وزعامة يمال إليها
  - activated_by_or_with: ع ي ن
  - themes: communication, politics_order
  - keywords: politics
- `ز و ر B006` — تزوير الكلام وتقويمه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ز و ر B007` — سير شديد
  - activated_by_or_with: ع ل م, ن ع م
  - themes: labor_work, motion, speed, stability_endurance, travel
  - keywords: effort, endurance, movement, speed, travel
- `ز و ر B008` — الزِّير الوتر والكتان
  - activated_by_or_with: ق ب ر
  - themes: material, plant_vegetation
  - keywords: material, plant

### ق ب ر

- `ق ب ر B001` — مواراة الميت في القبر
  - activated_by_or_with: ج ح م, ر ء ي
  - themes: mortality_death, ritual
  - keywords: death, ritual
- `ق ب ر B002` — غموض الشيء وتطامنه
  - activated_by_or_with: ز و ر
  - themes: material, plant_vegetation
  - keywords: material, plant
- `ق ب ر B003` — القُبَّرة الطائر
  - activated_by_or_with: ع ل م, ن ع م
  - themes: animal, naming_classification, wildlife
  - keywords: animal, bird, ornithology, taxonomy, wildlife
- `ق ب ر B004` — طرف الأنف في الغضب
  - activated_by_or_with: ج ح م, ر ء ي, ز و ر, ع ل م, ع ي ن, ل ه و
  - themes: anatomy, body, emotion, grammar_expression
  - keywords: anatomy, anger, body, emotion, expression, face, physiognomy
- `ق ب ر B005` — استعارة القبر للموت والاستتار
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### ع ل م

- `ع ل م B001` — انكشاف الشيء للعارف
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ل م B002` — أثر يميز الشيء ويهدي إليه
  - activated_by_or_with: ر ء ي, ع ي ن
  - themes: communication, geography_landscape, identity_personhood, navigation_route, orientation_direction, pattern_marking
  - keywords: geography, identity, navigation, symbol
- `ع ل م B003` — الخلق عالم يدل على صانعه
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ع ل م B004` — شق ظاهر في الشفة العليا
  - activated_by_or_with: ر ء ي, ز و ر, ع ي ن, ق ب ر, ك ث ر, ل ه و
  - themes: anatomy, body, disease_injury, form_structure, health_medicine, pattern_marking
  - keywords: anatomy, body, morphology, physiognomy
- `ع ل م B005` — ماء كثير مجتمع في عيلم
  - activated_by_or_with: ع ي ن
  - themes: geography_landscape, habitat_ecology, water_hydrology
  - keywords: hydrology, nature, water
- `ع ل م B006` — طائر جارح يسمى العلام
  - activated_by_or_with: ز و ر, ق ب ر, ن ع م
  - themes: animal, habitat_ecology, naming_classification, speed, wildlife
  - keywords: ornithology, speed, taxonomy, wildlife, zoology
- `ع ل م B007` — ذكر الضباع يسمى العيلام
  - activated_by_or_with: ق ب ر, ن ع م
  - themes: animal, habitat_ecology, naming_classification, wildlife
  - keywords: taxonomy, wildlife, zoology

### ي ق ن

- `ي ق ن B001` — ثبات العلم وزوال الشك
  - activated_by_or_with: ر ء ي, ز و ر, ع ي ن
  - themes: cognition, justice_judgment, knowledge_learning, perception, proof_uncertainty
  - keywords: cognition, epistemology, evidence, judgment, knowledge, perception, truth
- `ي ق ن B002` — صون الجارية وخدرها
  - activated_by_or_with: ع ي ن
  - themes: honor_shame, protection_security
  - keywords: honor, protection

### ر ء ي

- `ر ء ي B001` — رؤية العين والبصيرة
  - activated_by_or_with: ع ي ن, ي ق ن
  - themes: cognition, knowledge_learning, perception
  - keywords: cognition, epistemology, knowledge, perception
- `ر ء ي B002` — رأي القلب والتفكر
  - activated_by_or_with: ي ق ن
  - themes: cognition, justice_judgment, knowledge_learning, proof_uncertainty
  - keywords: cognition, judgment, knowledge
- `ر ء ي B003` — الرؤيا في المنام
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ء ي B004` — تراء وتواجه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ء ي B005` — رياء الناس
  - activated_by_or_with: ج ح م, ز و ر
  - themes: deception_corruption, ethics_morality, honor_shame, intention_character, religion_worship, social_relations
  - keywords: deception, ethics, religion, sociality, society
- `ر ء ي B006` — مرأى ومنظر ومرآة
  - activated_by_or_with: ع ي ن
  - themes: body, ornament_beauty, perception
  - keywords: beauty, body
- `ر ء ي B007` — ترية الحيض
  - activated_by_or_with: ز و ر, ق ب ر
  - themes: body, health_medicine, reproduction_birth, ritual
  - keywords: body, fertility, medicine, ritual
- `ر ء ي B008` — رئي من الجن
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ء ي B009` — الرئة وما يصيبها
  - activated_by_or_with: ج ح م, ز و ر, ع ل م, ع ي ن, ق ب ر, ل ه و
  - themes: anatomy, body, disease_injury, health_medicine, physiology
  - keywords: anatomy, body, disease, illness, medicine, organ, respiration
- `ر ء ي B010` — ظهور حمل الناقة أو الشاة
  - activated_by_or_with: ز و ر, ع ي ن, ن ع م
  - themes: agriculture, animal, body, husbandry, perception, reproduction_birth
  - keywords: agriculture, animal, body, fertility, herding
- `ر ء ي B011` — راية منصوبة
  - activated_by_or_with: ع ل م
  - themes: communication, identity_personhood, pattern_marking
  - keywords: identity, symbol
- `ر ء ي B012` — إراءة وإظهار
  - activated_by_or_with: ع ي ن
  - themes: knowledge_learning, perception, proof_uncertainty
  - keywords: evidence, perception
- `ر ء ي B013` — أرأيتك للتنبيه والاستخبار
  - activated_by_or_with: ك ث ر, ن ع م
  - themes: communication, language_speech
  - keywords: communication, dialogue, language, speech

### ج ح م

- `ج ح م B001` — تأجج النار وشدة حرها
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج ح م B002` — احتدام الحرب والموت
  - activated_by_or_with: ق ب ر
  - themes: mortality_death
  - keywords: death
- `ج ح م B003` — العين المتوقدة أو الجاحظة
  - activated_by_or_with: ر ء ي, ز و ر, ع ي ن
  - themes: anatomy, animal, disease_injury, perception
  - keywords: anatomy, animal, disease, illness, perception, vision
- `ج ح م B004` — تلهب الوجه بالغضب
  - activated_by_or_with: ع ي ن, ق ب ر
  - themes: anatomy, body, emotion, grammar_expression, measurement
  - keywords: anger, body, emotion, expression, face
- `ج ح م B005` — قلة الحياء
  - activated_by_or_with: ر ء ي
  - themes: ethics_morality, honor_shame, intention_character, social_relations
  - keywords: ethics, sociality, society

### ع ي ن

- `ع ي ن B001` — العين الناظرة
  - activated_by_or_with: ج ح م, ز و ر, ل ه و
  - themes: anatomy, body, perception
  - keywords: anatomy, body, perception, vision
- `ع ي ن B002` — المشاهدة بالعين
  - activated_by_or_with: ر ء ي, ن ع م, ي ق ن
  - themes: knowledge_learning, perception, proof_uncertainty, testimony_witness
  - keywords: epistemology, evidence, knowledge, perception, testimony
- `ع ي ن B003` — عين الحفظ والرعاية
  - activated_by_or_with: ي ق ن
  - themes: honor_shame, protection_security
  - keywords: honor, protection
- `ع ي ن B004` — الإصابة بالعين
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ي ن B005` — العين الجاسوسة
  - activated_by_or_with: ز و ر
  - themes: communication, politics_order
  - keywords: politics
- `ع ي ن B006` — منبع الماء الجاري
  - activated_by_or_with: ع ل م
  - themes: geography_landscape, habitat_ecology, water_hydrology
  - keywords: hydrology, nature, water
- `ع ي ن B007` — عين الجلد والسقاء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ي ن B008` — عين الشمس
  - activated_by_or_with: ن ع م
  - themes: sky_astronomy
  - keywords: astronomy
- `ع ي ن B009` — النقرة أو الموضع العيني
  - activated_by_or_with: ج ح م, ر ء ي, ز و ر, ع ل م, ق ب ر, ل ه و, ن ع م
  - themes: anatomy, body, measurement, pattern_marking, reasoning_decision, surface_shape, terrain_desert, tools_equipment
  - keywords: analogy, anatomy, body, shape, tool, topography
- `ع ي ن B010` — عين السحاب والمطر
  - activated_by_or_with: ع ل م, ن ع م
  - themes: calendar_season, geography_landscape, navigation_route, orientation_direction, weather_climate
  - keywords: climate, direction, geography, navigation, season, weather
- `ع ي ن B011` — النقد الحاضر
  - activated_by_or_with: same-root only
  - themes: commerce_exchange, finance_debt
  - keywords: commerce, finance
- `ع ي ن B012` — العينة والسلف
  - activated_by_or_with: same-root only
  - themes: commerce_exchange, finance_debt
  - keywords: commerce, finance
- `ع ي ن B013` — عين الشيء نفسه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ي ن B014` — العين خيار الشيء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ي ن B015` — أعيان القوم والإخوة
  - activated_by_or_with: ز و ر, ل ه و
  - themes: family, kinship, social_relations
  - keywords: family, kinship, society
- `ع ي ن B016` — سعة العين وحسنها
  - activated_by_or_with: ج ح م, ر ء ي, ز و ر, ع ل م, ق ب ر, ل ه و
  - themes: anatomy, animal, body, ornament_beauty, perception
  - keywords: anatomy, animal, beauty, body, vision
- `ع ي ن B017` — العين بمعنى الناس الحاضرون
  - activated_by_or_with: ز و ر
  - themes: household_community, social_relations
  - keywords: community, society

### س ء ل

- `س ء ل B001` — السؤال والطلب
  - activated_by_or_with: ك ث ر
  - themes: communication, language_speech, obligation_contract, support_dependence
  - keywords: communication, speech
- `س ء ل B002` — السُّؤل المطلوب
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `س ء ل B003` — قضاء المسألة
  - activated_by_or_with: ل ه و
  - themes: commerce_exchange, hospitality_welfare, provision_resource
  - keywords: generosity, provision
- `س ء ل B004` — السؤال المتبادل
  - activated_by_or_with: ن ع م
  - themes: communication, social_relations
  - keywords: communication, dialogue, interaction

### ن ع م

- `ن ع م B001` — حسن الحال والنعمة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن ع م B002` — اللين والنعومة ورفاه العيش
  - activated_by_or_with: ك ث ر
  - themes: hierarchy_status, wealth_property
  - keywords: status, wealth
- `ن ع م B003` — مدح الشيء بنعم
  - activated_by_or_with: ز و ر
  - themes: justice_judgment, language_speech
  - keywords: judgment, speech
- `ن ع م B004` — الجواب بنعم والتصديق
  - activated_by_or_with: ر ء ي, ز و ر, س ء ل, ع ي ن
  - themes: communication, language_speech, proof_uncertainty, social_relations, testimony_witness
  - keywords: communication, dialogue, interaction, language, testimony, truth
- `ن ع م B005` — مال الأنعام والإبل
  - activated_by_or_with: ر ء ي, ك ث ر, ل ه و
  - themes: agriculture, animal, economy, husbandry, provision_resource, wealth_property
  - keywords: agriculture, animal, economy, herding, wealth
- `ن ع م B006` — النعام والنعامة الطائر
  - activated_by_or_with: ع ل م, ق ب ر
  - themes: animal, habitat_ecology, naming_classification, wildlife
  - keywords: animal, bird, taxonomy, wildlife, zoology
- `ن ع م B007` — ما سمي نعامة تشبيها بالهيئة
  - activated_by_or_with: ع ي ن
  - themes: anatomy, reasoning_decision, sky_astronomy, surface_shape, terrain_desert, tools_equipment
  - keywords: analogy, anatomy, astronomy, shape, tool, topography
- `ن ع م B008` — طيران النعامة وتفرق القوم
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن ع م B009` — النعامى ريح لينة
  - activated_by_or_with: ع ي ن
  - themes: calendar_season, orientation_direction, weather_climate
  - keywords: climate, direction, season, weather
- `ن ع م B010` — زاد وأنعم في الفعل
  - activated_by_or_with: ك ث ر
  - themes: measurement, quantity_number
  - keywords: measure, quantity
- `ن ع م B011` — موافقة المكان وطيب المقام
  - activated_by_or_with: ز و ر
  - themes: hospitality_welfare, social_relations, travel
  - keywords: hospitality, travel
- `ن ع م B012` — المشي على القدم وابتذالها
  - activated_by_or_with: ز و ر
  - themes: labor_work, motion, stability_endurance, travel
  - keywords: effort, endurance, movement, travel
- `ن ع م B013` — نعم الله بك عينا وقرة العين
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
