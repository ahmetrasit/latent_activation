# v11 Activation Packet — S87:15-19

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_15: وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ
- verse_16: بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- verse_17: وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ
- verse_18: إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ
- verse_19: صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ذ ك ر → س م و → ر ب ب → ص ل و → ء ث ر → ح ي ي → د ن و → ء خ ر → خ ي ر → ب ق ي → ص ح ف → ء و ل

## Branch inventory summary

- ذ ك ر: 9 branches (7 with Qnet bridge-theme nodes; 2 Furūq-only)
- س م و: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ر ب ب: 17 branches (17 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص ل و: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء ث ر: 12 branches (11 with Qnet bridge-theme nodes; 1 Furūq-only)
- ح ي ي: 14 branches (10 with Qnet bridge-theme nodes; 4 Furūq-only)
- د ن و: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء خ ر: 4 branches (3 with Qnet bridge-theme nodes; 1 Furūq-only)
- خ ي ر: 6 branches (5 with Qnet bridge-theme nodes; 1 Furūq-only)
- ب ق ي: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص ح ف: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء و ل: 11 branches (11 with Qnet bridge-theme nodes; 0 Furūq-only)

## QAC-first root resolution audit

- ذ ك ر | qac_keys=ذكر | status=resolved | matches=root_000516
- س م و | qac_keys=سمو | status=resolved | matches=root_000745
- ر ب ب | qac_keys=ربب | status=resolved | matches=root_000532
- ص ل و | qac_keys=صلو | status=resolved | matches=root_000879
- ء ث ر | qac_keys=ءثر | status=resolved | matches=root_000011
- ح ي ي | qac_keys=حيي | status=resolved | matches=root_000383
- د ن و | qac_keys=دنو | status=resolved | matches=root_000493
- ء خ ر | qac_keys=ءخر | status=resolved | matches=root_000019
- خ ي ر | qac_keys=خير | status=resolved | matches=root_000452
- ب ق ي | qac_keys=بقي | status=resolved | matches=root_000142
- ص ح ف | qac_keys=صحف | status=resolved | matches=root_000845
- ء و ل | qac_keys=ءول | status=resolved | matches=root_000067

## Top candidate bridges

- `ص ل و B009` ↔ `ء و ل B011` | score_hint=27 | discovery_hint=20 | themes=animal, food_nutrition, habitat_ecology, pasture_forage, plant_vegetation | keywords=botany, ecology, forage, pasture | q2=—
- `ح ي ي B010` ↔ `ء و ل B003` | score_hint=27 | discovery_hint=19 | themes=household_community, identity_personhood, kinship, marriage_genealogy, social_relations | keywords=community, genealogy, identity, kinship | q2=—
- `ص ل و B004` ↔ `خ ي ر B006` | score_hint=26 | discovery_hint=14 | themes=animal, control_restraint, habitat_ecology, tools_equipment, wildlife | keywords=animal, capture, hunting, tool | q2=—
- `س م و B006` ↔ `ص ل و B004` | score_hint=24 | discovery_hint=14 | themes=animal, habitat_ecology, tools_equipment, wildlife | keywords=animal, hunting, predation, tool | q2=—
- `ر ب ب B008` ↔ `ح ي ي B002` | score_hint=24 | discovery_hint=17 | themes=agriculture, habitat_ecology, reproduction_birth, weather_climate | keywords=agriculture, ecology, fertility, weather | q2=—
- `ص ل و B005` ↔ `ء خ ر B003` | score_hint=24 | discovery_hint=15 | themes=anatomy, animal, body, orientation_direction | keywords=anatomy, animal, body, orientation | q2=—
- `د ن و B002` ↔ `ء و ل B001` | score_hint=24 | discovery_hint=13 | themes=hierarchy_status, orientation_direction, sequence_cycle, time | keywords=hierarchy, orientation, sequence, temporality | q2=—
- `س م و B006` ↔ `خ ي ر B006` | score_hint=24 | discovery_hint=14 | themes=animal, habitat_ecology, motion, provision_resource, tools_equipment, wildlife | keywords=animal, hunting, tool | q2=—
- `ص ل و B002` ↔ `ح ي ي B007` | score_hint=24 | discovery_hint=13 | themes=belief_revelation, communication, ethics_morality, religion_worship, ritual, social_relations | keywords=blessing, communication, ritual | q2=—
- `ذ ك ر B007` ↔ `س م و B001` | score_hint=20 | discovery_hint=13 | themes=hierarchy_status, honor_shame | keywords=hierarchy, honor, reputation, status | q2=—
- `ذ ك ر B009` ↔ `ء ث ر B002` | score_hint=20 | discovery_hint=13 | themes=belief_revelation, communication, knowledge_learning, memory_attention | keywords=communication, education, memory | q2=—
- `ر ب ب B009` ↔ `د ن و B004` | score_hint=20 | discovery_hint=15 | themes=animal, life_stage_aging, reproduction_birth, time | keywords=animal, reproduction, time | q2=—
- `ر ب ب B012` ↔ `ء و ل B011` | score_hint=20 | discovery_hint=16 | themes=agriculture, food_nutrition, habitat_ecology, plant_vegetation | keywords=agriculture, botany, ecology | q2=—
- `ر ب ب B014` ↔ `ص ل و B009` | score_hint=20 | discovery_hint=13 | themes=animal, habitat_ecology, livestock, terrain_desert | keywords=desert, ecology, livestock | q2=—
- `ص ل و B005` ↔ `د ن و B004` | score_hint=20 | discovery_hint=16 | themes=animal, body, physiology, reproduction_birth | keywords=animal, body, reproduction | q2=—
- `ء ث ر B002` ↔ `ص ح ف B002` | score_hint=20 | discovery_hint=13 | themes=belief_revelation, communication, knowledge_learning, writing_text | keywords=communication, scripture, text | q2=—
- `ذ ك ر B001` ↔ `د ن و B004` | score_hint=18 | discovery_hint=15 | themes=body, physiology, reproduction_birth | keywords=biology, body, reproduction | q2=—
- `ذ ك ر B007` ↔ `س م و B008` | score_hint=18 | discovery_hint=13 | themes=honor_shame, memory_attention, social_relations | keywords=memory, praise, reputation | q2=—
- `ذ ك ر B007` ↔ `د ن و B003` | score_hint=18 | discovery_hint=13 | themes=hierarchy_status, honor_shame, value_quality | keywords=hierarchy, honor, status | q2=—
- `س م و B004` ↔ `ر ب ب B008` | score_hint=18 | discovery_hint=16 | themes=agriculture, sky_astronomy, weather_climate | keywords=agriculture, meteorology, weather | q2=—
- `س م و B006` ↔ `ء ث ر B008` | score_hint=18 | discovery_hint=13 | themes=animal, navigation_route, tools_equipment | keywords=animal, tool, tracking | q2=—
- `ر ب ب B004` ↔ `ح ي ي B010` | score_hint=18 | discovery_hint=13 | themes=household_community, kinship, social_relations | keywords=kinship, society, tribe | q2=—
- `ر ب ب B007` ↔ `ب ق ي B005` | score_hint=18 | discovery_hint=14 | themes=motion, time, weather_climate | keywords=movement, time, weather | q2=—
- `ر ب ب B012` ↔ `ص ل و B009` | score_hint=18 | discovery_hint=15 | themes=food_nutrition, habitat_ecology, plant_vegetation | keywords=botany, ecology, food | q2=—
- `ص ل و B005` ↔ `د ن و B005` | score_hint=18 | discovery_hint=14 | themes=anatomy, body, orientation_direction | keywords=anatomy, body, orientation | q2=—
- `ح ي ي B006` ↔ `ب ق ي B003` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, stability_endurance, violence_warfare | keywords=mercy, survival, violence | q2=—
- `ح ي ي B013` ↔ `خ ي ر B001` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, hospitality_welfare, protection_security | keywords=ethics, protection, welfare | q2=—
- `د ن و B005` ↔ `ء خ ر B003` | score_hint=18 | discovery_hint=14 | themes=anatomy, body, orientation_direction | keywords=anatomy, body, orientation | q2=—
- `س م و B001` ↔ `د ن و B003` | score_hint=16 | discovery_hint=12 | themes=hierarchy_status, honor_shame | keywords=hierarchy, honor, status | q2=—
- `س م و B002` ↔ `ء و ل B006` | score_hint=16 | discovery_hint=13 | themes=orientation_direction, perception | keywords=orientation, perception, visibility | q2=—
- `ر ب ب B003` ↔ `ء ث ر B011` | score_hint=16 | discovery_hint=13 | themes=cognition, knowledge_learning | keywords=education, expertise, learning | q2=—
- `ر ب ب B009` ↔ `ص ل و B005` | score_hint=16 | discovery_hint=14 | themes=animal, reproduction_birth | keywords=animal, birth, reproduction | q2=—
- `ء ث ر B001` ↔ `خ ي ر B003` | score_hint=16 | discovery_hint=12 | themes=agency_action, reasoning_decision | keywords=agency, decision, selection | q2=—
- `ء ث ر B001` ↔ `ء و ل B001` | score_hint=16 | discovery_hint=11 | themes=sequence_cycle, time | keywords=priority, sequence, temporality | q2=—
- `د ن و B003` ↔ `خ ي ر B001` | score_hint=16 | discovery_hint=12 | themes=ethics_morality, value_quality | keywords=ethics, morality, value | q2=—
- `ص ل و B004` ↔ `ح ي ي B004` | score_hint=16 | discovery_hint=12 | themes=animal, danger_harm, habitat_ecology, wildlife | keywords=animal, danger | q2=—
- `ذ ك ر B001` ↔ `ح ي ي B011` | score_hint=15 | discovery_hint=17 | themes=gender, reproduction_birth, sexuality | keywords=gender, reproduction | q2=—
- `ذ ك ر B001` ↔ `ص ل و B005` | score_hint=14 | discovery_hint=14 | themes=body, physiology, reproduction_birth | keywords=body, reproduction | q2=—
- `ذ ك ر B002` ↔ `س م و B004` | score_hint=14 | discovery_hint=14 | themes=agriculture, terrain_desert, weather_climate | keywords=agriculture, weather | q2=—
- `ذ ك ر B004` ↔ `س م و B008` | score_hint=14 | discovery_hint=12 | themes=communication, honor_shame, social_relations | keywords=communication, reputation | q2=—
- `ذ ك ر B004` ↔ `ص ل و B002` | score_hint=14 | discovery_hint=12 | themes=communication, language_speech, social_relations | keywords=communication, speech | q2=—
- `ذ ك ر B007` ↔ `س م و B007` | score_hint=14 | discovery_hint=12 | themes=hierarchy_status, honor_shame, value_quality | keywords=honor, status | q2=—
- `س م و B002` ↔ `د ن و B001` | score_hint=14 | discovery_hint=12 | themes=measurement, orientation_direction, space | keywords=distance, orientation | q2=—
- `س م و B003` ↔ `ر ب ب B009` | score_hint=14 | discovery_hint=13 | themes=animal, livestock, reproduction_birth | keywords=livestock, reproduction | q2=—
- `س م و B003` ↔ `ر ب ب B014` | score_hint=14 | discovery_hint=12 | themes=animal, husbandry, livestock | keywords=livestock, zoology | q2=—
- `س م و B005` ↔ `ء خ ر B001` | score_hint=14 | discovery_hint=12 | themes=identity_personhood, naming_classification, reasoning_decision | keywords=classification, identity | q2=—
- `س م و B006` ↔ `ص ل و B009` | score_hint=14 | discovery_hint=13 | themes=animal, habitat_ecology, provision_resource | keywords=animal, subsistence | q2=—
- `س م و B007` ↔ `د ن و B003` | score_hint=14 | discovery_hint=12 | themes=hierarchy_status, honor_shame, value_quality | keywords=honor, status | q2=—
- `س م و B007` ↔ `خ ي ر B002` | score_hint=14 | discovery_hint=12 | themes=hierarchy_status, reasoning_decision, value_quality | keywords=excellence, status | q2=—
- `ر ب ب B002` ↔ `ء و ل B010` | score_hint=14 | discovery_hint=13 | themes=craft, life_stage_aging, stability_endurance | keywords=craft, maturation | q2=—
- `ر ب ب B005` ↔ `ء و ل B003` | score_hint=14 | discovery_hint=13 | themes=household_community, kinship, support_dependence | keywords=household, kinship | q2=—
- `ر ب ب B006` ↔ `ء ث ر B009` | score_hint=14 | discovery_hint=14 | themes=agency_action, food_nutrition, substance_texture | keywords=food, substance | q2=—
- `ر ب ب B006` ↔ `ء و ل B005` | score_hint=14 | discovery_hint=14 | themes=food_nutrition, material, substance_texture | keywords=food, material | q2=—
- `ر ب ب B009` ↔ `ص ل و B009` | score_hint=14 | discovery_hint=13 | themes=animal, food_nutrition, livestock | keywords=animal, livestock | q2=—
- `ر ب ب B014` ↔ `خ ي ر B006` | score_hint=14 | discovery_hint=12 | themes=animal, habitat_ecology, wildlife | keywords=ecology, hunting | q2=—
- `ر ب ب B016` ↔ `خ ي ر B005` | score_hint=14 | discovery_hint=13 | themes=ethics_morality, hospitality_welfare, support_dependence | keywords=charity, gift | q2=—
- `ص ل و B002` ↔ `ح ي ي B009` | score_hint=14 | discovery_hint=12 | themes=communication, religion_worship, ritual | keywords=communication, ritual | q2=—
- `ص ل و B003` ↔ `ح ي ي B009` | score_hint=14 | discovery_hint=12 | themes=authority_governance, religion_worship, ritual | keywords=ritual, worship | q2=—
- `ص ل و B006` ↔ `ء و ل B001` | score_hint=14 | discovery_hint=11 | themes=hierarchy_status, motion, sequence_cycle | keywords=motion, sequence | q2=—
- `ص ل و B007` ↔ `ح ي ي B009` | score_hint=14 | discovery_hint=12 | themes=authority_governance, religion_worship, ritual | keywords=ritual, worship | q2=—
- `ص ل و B008` ↔ `ص ح ف B004` | score_hint=14 | discovery_hint=13 | themes=food_nutrition, household_community, tools_equipment | keywords=domesticity, food | q2=—
- `ص ل و B009` ↔ `خ ي ر B006` | score_hint=14 | discovery_hint=13 | themes=animal, habitat_ecology, provision_resource | keywords=animal, ecology | q2=—
- `ء ث ر B001` ↔ `د ن و B002` | score_hint=14 | discovery_hint=11 | themes=reasoning_decision, sequence_cycle, time | keywords=sequence, temporality | q2=—
- `ء ث ر B002` ↔ `ص ح ف B003` | score_hint=14 | discovery_hint=12 | themes=belief_revelation, communication, writing_text | keywords=scripture, text | q2=—
- `ء ث ر B005` ↔ `د ن و B003` | score_hint=14 | discovery_hint=12 | themes=ethics_morality, hierarchy_status, value_quality | keywords=ethics, hierarchy | q2=—
- `ح ي ي B012` ↔ `د ن و B005` | score_hint=14 | discovery_hint=13 | themes=anatomy, body, posture_embodiment | keywords=anatomy, body | q2=—
- `د ن و B002` ↔ `ء خ ر B001` | score_hint=14 | discovery_hint=12 | themes=measurement, reasoning_decision, sequence_cycle | keywords=comparison, sequence | q2=—
- `د ن و B003` ↔ `خ ي ر B002` | score_hint=14 | discovery_hint=12 | themes=ethics_morality, hierarchy_status, value_quality | keywords=ethics, status | q2=—
- `د ن و B004` ↔ `ء خ ر B003` | score_hint=14 | discovery_hint=13 | themes=animal, body, boundary | keywords=animal, body | q2=—
- `ص ح ف B001` ↔ `ء و ل B006` | score_hint=14 | discovery_hint=11 | themes=geography_landscape, terrain_desert, visual_appearance | keywords=appearance, topography | q2=—
- `ذ ك ر B002` ↔ `ر ب ب B008` | score_hint=12 | discovery_hint=14 | themes=agriculture, weather_climate | keywords=agriculture, weather | q2=—
- `ذ ك ر B002` ↔ `ح ي ي B002` | score_hint=12 | discovery_hint=14 | themes=agriculture, weather_climate | keywords=agriculture, weather | q2=—
- `ذ ك ر B003` ↔ `ء ث ر B011` | score_hint=12 | discovery_hint=12 | themes=cognition, knowledge_learning | keywords=cognition, learning | q2=—
- `ذ ك ر B004` ↔ `ح ي ي B007` | score_hint=12 | discovery_hint=12 | themes=communication, social_relations | keywords=communication, society | q2=—
- `ذ ك ر B007` ↔ `ء و ل B007` | score_hint=12 | discovery_hint=12 | themes=hierarchy_status, value_quality | keywords=evaluation, status | q2=—
- `ذ ك ر B008` ↔ `ر ب ب B011` | score_hint=12 | discovery_hint=12 | themes=law, obligation_contract | keywords=contract, law | q2=—
- `ذ ك ر B009` ↔ `س م و B008` | score_hint=12 | discovery_hint=12 | themes=communication, memory_attention | keywords=communication, memory | q2=—
- `ذ ك ر B009` ↔ `ر ب ب B003` | score_hint=12 | discovery_hint=12 | themes=cognition, knowledge_learning | keywords=education, pedagogy | q2=—
- `س م و B003` ↔ `ح ي ي B011` | score_hint=12 | discovery_hint=14 | themes=reproduction_birth, sexuality | keywords=reproduction, sexuality | q2=—
- `س م و B004` ↔ `ح ي ي B002` | score_hint=12 | discovery_hint=14 | themes=agriculture, weather_climate | keywords=agriculture, weather | q2=—

## Per-root candidate activations

### ذ ك ر

- `ذ ك ر B001` — الذكر خلاف الأنثى
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ح ي ي, خ ي ر, د ن و, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: body, gender, kinship, naming_classification, physiology, reasoning_decision, reproduction_birth, sexuality
  - keywords: biology, body, gender, kinship, reproduction, taxonomy
- `ذ ك ر B002` — صلابة الذكر وحدته وشدته
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: agriculture, danger_harm, force_power, material, terrain_desert, value_quality, weaponry, weather_climate
  - keywords: agriculture, danger, material, metal, weapon, weather
- `ذ ك ر B003` — استحضار الشيء بعد النسيان أو مع الحفظ
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, ر ب ب, س م و, ص ح ف
  - themes: cognition, knowledge_learning, memory_attention
  - keywords: attention, cognition, knowledge, learning, memory
- `ذ ك ر B004` — جريان الذكر على اللسان
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: communication, honor_shame, language_speech, rhetoric_discourse, social_relations, value_quality
  - keywords: communication, discourse, evaluation, language, reputation, society, speech
- `ذ ك ر B005` — ذكر الله عبادة وثناء ودعاء
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ذ ك ر B006` — الذكر كتاب منزل أو كتاب دين
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ذ ك ر B007` — ذكر المرء شرف وصيت
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ر ب ب, س م و, ص ل و
  - themes: culture_tradition, hierarchy_status, honor_shame, memory_attention, social_relations, value_quality
  - keywords: evaluation, hierarchy, honor, memory, praise, reputation, society, status
- `ذ ك ر B008` — ذكر الحق صك ووثيقة حق
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: authority_governance, law, obligation_contract, proof_uncertainty, wealth_property, writing_text
  - keywords: administration, contract, evidence, law, property, record
- `ذ ك ر B009` — الذكرى والتذكرة ما يذكّر
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: belief_revelation, cognition, communication, knowledge_learning, memory_attention
  - keywords: communication, education, guidance, memory, pedagogy

### س م و

- `س م و B001` — العلو والارتفاع
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, ص ح ف, ص ل و
  - themes: hierarchy_status, honor_shame, orientation_direction, perception, space
  - keywords: hierarchy, honor, perception, reputation, spatiality, status
- `س م و B002` — الشخص المرتفع الظاهر
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, د ن و, ر ب ب, ص ح ف, ص ل و
  - themes: concealment_disclosure, measurement, orientation_direction, perception, place_location, sky_astronomy, space
  - keywords: distance, orientation, perception, spatiality, visibility
- `س م و B003` — تطاول الفحل على الشول
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, ص ل و
  - themes: animal, authority_governance, hierarchy_status, husbandry, livestock, motion, reproduction_birth, sexuality, violence_warfare
  - keywords: livestock, motion, reproduction, sexuality, zoology
- `س م و B004` — السماء وما علا فأظل
  - activated_by_or_with: ء خ ر, ء و ل, ب ق ي, ح ي ي, د ن و, ذ ك ر, ر ب ب, ص ح ف, ص ل و
  - themes: agriculture, anatomy, architecture_construction, sky_astronomy, terrain_desert, weather_climate
  - keywords: agriculture, anatomy, architecture, cosmology, meteorology, shelter, topography, weather
- `س م و B005` — الاسم تنويه ودلالة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, ص ح ف, ص ل و
  - themes: cognition, communication, identity_personhood, kinship, language_speech, naming_classification, reasoning_decision
  - keywords: classification, identity, kinship, language, recognition, semiotics
- `س م و B006` — الخروج للصيد
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ر ب ب, ص ح ف, ص ل و
  - themes: animal, habitat_ecology, motion, navigation_route, provision_resource, tools_equipment, wildlife
  - keywords: animal, hunting, predation, subsistence, tool, tracking, wildlife
- `س م و B007` — المساماة والمباراة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, ص ح ف, ص ل و
  - themes: agency_action, conflict, hierarchy_status, honor_shame, reasoning_decision, value_quality
  - keywords: comparison, competition, conflict, excellence, honor, status
- `س م و B008` — الصيت الحسن المنتشر
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, ص ح ف, ص ل و
  - themes: communication, concealment_disclosure, ethics_morality, honor_shame, memory_attention, social_relations
  - keywords: communication, ethics, memory, praise, reputation, sociality

### ر ب ب

- `ر ب ب B001` — ربوبية وملك وسيادة
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, س م و, ص ح ف, ص ل و
  - themes: authority_governance, belief_revelation, force_power, hierarchy_status, religion_worship, support_dependence, wealth_property
  - keywords: authority, devotion, governance, hierarchy, patronage, power, property
- `ر ب ب B002` — إصلاح وتربية وإتمام
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, س م و, ص ح ف, ص ل و
  - themes: agriculture, authority_governance, belief_revelation, craft, family, knowledge_learning, life_stage_aging, stability_endurance
  - keywords: agriculture, craft, education, maturation, stewardship
- `ر ب ب B003` — علم رباني
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, س م و, ص ح ف, ص ل و
  - themes: cognition, ethics_morality, knowledge_learning, religion_worship
  - keywords: education, ethics, expertise, learning, pedagogy, religion, scholarship
- `ر ب ب B004` — ربة وجماعات كثيرة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, د ن و, ذ ك ر, س م و, ص ح ف, ص ل و
  - themes: household_community, kinship, quantity_number, social_relations, violence_warfare
  - keywords: collectivity, demography, kinship, society, tribe
- `ر ب ب B005` — ربيب وربيبة ورابة
  - activated_by_or_with: ء ث ر, ء و ل, ح ي ي, خ ي ر, د ن و, ذ ك ر, س م و, ص ح ف, ص ل و
  - themes: authority_governance, family, hospitality_welfare, household_community, kinship, reproduction_birth, support_dependence
  - keywords: dependency, family, household, kinship
- `ر ب ب B006` — رُبّ خاثر وإصلاح به
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, ذ ك ر, س م و, ص ح ف, ص ل و
  - themes: agency_action, food_nutrition, health_medicine, material, stability_endurance, substance_texture
  - keywords: food, leather, material, preparation, preservation, substance
- `ر ب ب B007` — لزوم وإقامة ودوام
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, س م و, ص ح ف, ص ل و
  - themes: animal, geography_landscape, motion, place_location, time, weather_climate
  - keywords: animal, geography, motion, movement, temporality, time, weather
- `ر ب ب B008` — رباب السحاب
  - activated_by_or_with: ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, س م و, ص ح ف, ص ل و
  - themes: agriculture, habitat_ecology, reproduction_birth, sky_astronomy, water_hydrology, weather_climate
  - keywords: agriculture, ecology, fertility, meteorology, water, weather
- `ر ب ب B009` — شاة رُبّى وحداثة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, س م و, ص ح ف, ص ل و
  - themes: animal, food_nutrition, household_community, life_stage_aging, livestock, reproduction_birth, time
  - keywords: animal, birth, dairy, household, livestock, reproduction, temporality, time
- `ر ب ب B010` — ربابة تجمع القداح
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, ذ ك ر, س م و, ص ح ف, ص ل و
  - themes: abundance_scarcity, belief_revelation, material, proof_uncertainty, ritual, storage_vessels, tools_equipment, weaponry
  - keywords: fortune, leather, ritual, storage, tool, weapon
- `ر ب ب B011` — ربابة عهد وميثاق
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, ذ ك ر, ص ح ف, ص ل و
  - themes: finance_debt, household_community, law, obligation_contract, politics_order, protection_security, trust_loyalty
  - keywords: community, contract, law, protection, trust
- `ر ب ب B012` — ربة نبات
  - activated_by_or_with: ء ث ر, ء و ل, ح ي ي, خ ي ر, د ن و, ذ ك ر, س م و, ص ح ف, ص ل و
  - themes: agriculture, food_nutrition, geography_landscape, habitat_ecology, physiology, plant_vegetation, visual_appearance
  - keywords: agriculture, botany, ecology, food, landscape, life
- `ر ب ب B013` — ماء رَبَب كثير
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, س م و, ص ح ف, ص ل و
  - themes: abundance_scarcity, cooking_drink, geography_landscape, habitat_ecology, provision_resource, water_hydrology
  - keywords: abundance, drink, ecology, geography, nature, resource, sustenance
- `ر ب ب B014` — رَبْرَب قطيع
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, س م و, ص ح ف, ص ل و
  - themes: animal, habitat_ecology, household_community, husbandry, livestock, quantity_number, terrain_desert, wildlife
  - keywords: collectivity, desert, ecology, hunting, livestock, pastoralism, zoology
- `ر ب ب B015` — حرف رب وربما
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, س م و, ص ح ف, ص ل و
  - themes: form_structure, grammar_expression, language_speech, quantity_number, rhetoric_discourse
  - keywords: discourse, morphology, semantics
- `ر ب ب B016` — رُبَى حاجة وعقدة ونعمة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, س م و, ص ل و
  - themes: control_restraint, ethics_morality, hospitality_welfare, material, obligation_contract, social_relations, support_dependence
  - keywords: charity, dependency, ethics, gift, material, obligation, relation, welfare
- `ر ب ب B017` — رباني الملاحين
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, س م و, ص ح ف, ص ل و
  - themes: authority_governance, hierarchy_status, navigation_route, transport, travel, water_hydrology
  - keywords: authority, hierarchy, navigation, transport, travel, water

### ص ل و

- `ص ل و B001` — ملاقاة النار وحرها
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, د ن و, ذ ك ر, ر ب ب
  - themes: cooking_drink, danger_harm, force_power, justice_judgment, material
  - keywords: material
- `ص ل و B002` — الدعاء والثناء والرحمة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف
  - themes: belief_revelation, communication, ethics_morality, language_speech, religion_worship, ritual, social_relations
  - keywords: blessing, communication, devotion, forgiveness, mercy, relation, ritual, speech
- `ص ل و B003` — العبادة المخصوصة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف
  - themes: authority_governance, body, control_restraint, household_community, law, religion_worship, ritual
  - keywords: body, community, devotion, law, liturgy, religion, ritual, worship
- `ص ل و B004` — الشرك المنصوبة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف
  - themes: animal, control_restraint, craft, danger_harm, habitat_ecology, reasoning_decision, tools_equipment, violence_warfare, wildlife
  - keywords: animal, capture, craft, danger, hunting, predation, tool
- `ص ل و B005` — الصَّلا من الظهر والجنب
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف
  - themes: anatomy, animal, body, orientation_direction, physiology, reproduction_birth
  - keywords: anatomy, animal, birth, body, orientation, reproduction
- `ص ل و B006` — تلو السابق في السباق
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف
  - themes: animal, conflict, hierarchy_status, measurement, motion, sequence_cycle
  - keywords: animal, competition, motion, ranking, sequence
- `ص ل و B007` — مواضع الصلاة ودور العبادة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف
  - themes: architecture_construction, authority_governance, culture_tradition, household_community, identity_personhood, religion_worship, ritual, space
  - keywords: architecture, community, heritage, identity, religion, ritual, space, worship
- `ص ل و B008` — الصَّلاية حجر الدق
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, ر ب ب, س م و, ص ح ف
  - themes: agency_action, craft, food_nutrition, household_community, perception, plant_vegetation, tools_equipment
  - keywords: craft, domesticity, food, plant, preparation, processing, tool
- `ص ل و B009` — الصِّليان نبت ترعاه الإبل
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف
  - themes: animal, food_nutrition, habitat_ecology, livestock, pasture_forage, plant_vegetation, provision_resource, terrain_desert
  - keywords: animal, botany, desert, ecology, food, forage, livestock, pasture, plant, subsistence

### ء ث ر

- `ء ث ر B001` — تقديم الشيء في البدء أو الاختيار
  - activated_by_or_with: ء خ ر, ء و ل, ب ق ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: agency_action, intention_character, reasoning_decision, sequence_cycle, time
  - keywords: agency, decision, priority, selection, sequence, temporality
- `ء ث ر B002` — نقل الخبر حتى يصير مأثورا
  - activated_by_or_with: ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: belief_revelation, communication, culture_tradition, knowledge_learning, memory_attention, time, writing_text
  - keywords: communication, education, heritage, memory, scholarship, scripture, text
- `ء ث ر B003` — علامة باقية تدل على ما كان
  - activated_by_or_with: ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: agency_action, communication, knowledge_learning, material, memory_attention, proof_uncertainty, sequence_cycle
  - keywords: evidence, memory, semiotics
- `ء ث ر B004` — السير على إثر سابق
  - activated_by_or_with: ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: belief_revelation, motion, navigation_route, religion_worship, sequence_cycle, stability_endurance
  - keywords: guidance, motion, movement, navigation, tracking
- `ء ث ر B005` — تفضيل الغير أو الشيء بالاختيار
  - activated_by_or_with: ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: ethics_morality, hierarchy_status, hospitality_welfare, social_relations, value_quality
  - keywords: ethics, hierarchy
- `ء ث ر B006` — استبداد المرء بالشيء لنفسه
  - activated_by_or_with: ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: abundance_scarcity, authority_governance, boundary, control_restraint, force_power, justice_judgment, wealth_property
  - keywords: power, scarcity
- `ء ث ر B007` — أثر السيف في لمعانه أو ضربته
  - activated_by_or_with: ء و ل, ب ق ي, ح ي ي, د ن و, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: craft, danger_harm, disease_injury, material, violence_warfare, weaponry
  - keywords: craft, craftsmanship, metal, violence, warfare
- `ء ث ر B008` — وسم خف البعير ليتبع أثره
  - activated_by_or_with: ء خ ر, ء و ل, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: animal, husbandry, navigation_route, tools_equipment, writing_text
  - keywords: animal, husbandry, navigation, pastoralism, tool, tracking
- `ء ث ر B009` — بقية دسم قديم أو خلاصة سمن
  - activated_by_or_with: ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: agency_action, animal, food_nutrition, husbandry, quantity_number, substance_texture
  - keywords: animal, food, pastoralism, processing, residue, substance
- `ء ث ر B010` — ما يتبع العمر من أجل أو عمل
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ء ث ر B011` — حذق الشيء بالممارسة
  - activated_by_or_with: ء و ل, ب ق ي, ح ي ي, خ ي ر, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: agency_action, cognition, craft, knowledge_learning, perception
  - keywords: cognition, craft, craftsmanship, education, expertise, learning, perception
- `ء ث ر B012` — كيس يشد على ضرع العنز
  - activated_by_or_with: ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: animal, food_nutrition, health_medicine, husbandry, protection_security, storage_vessels, tools_equipment
  - keywords: animal, container, dairy, husbandry, protection

### ح ي ي

- `ح ي ي B001` — الحياة في مقابل الموت
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ح ي ي B002` — حياة الأرض بالمطر والنبات
  - activated_by_or_with: ء و ل, ب ق ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: agriculture, change_transition, habitat_ecology, provision_resource, reproduction_birth, weather_climate
  - keywords: agriculture, ecology, fertility, sustenance, weather
- `ح ي ي B003` — ذو الروح والحيوان
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: animal, belief_revelation, mortality_death, physiology, posture_embodiment
  - keywords: biology, embodiment, life, mortality, zoology
- `ح ي ي B004` — الحية من جنس الحياة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: animal, culture_tradition, danger_harm, habitat_ecology, language_speech, naming_classification, wildlife
  - keywords: animal, danger, nature, taxonomy, zoology
- `ح ي ي B005` — الحياء وانقباض النفس
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ح ي ي B006` — استبقاء الحياة وترك القتل
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, خ ي ر, د ن و, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: ethics_morality, household_community, protection_security, stability_endurance, violence_warfare
  - keywords: demography, mercy, preservation, protection, survival, violence, warfare
- `ح ي ي B007` — التحية دعاء بالحياة والسلام
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: belief_revelation, communication, ethics_morality, prayer_supplication, protection_security, religion_worship, ritual, social_relations
  - keywords: blessing, communication, prayer, ritual, society, worship
- `ح ي ي B008` — التحية بمعنى الملك والسلطان
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ح ي ي B009` — حي على بمعنى هلم وأقبل
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, خ ي ر, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: authority_governance, communication, motion, religion_worship, ritual
  - keywords: communication, motion, movement, ritual, worship
- `ح ي ي B010` — الحي جماعة النسب والقبيلة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: household_community, identity_personhood, kinship, marriage_genealogy, politics_order, social_relations
  - keywords: community, genealogy, identity, kinship, politics, society, tribe
- `ح ي ي B011` — الحياء العضو المستور
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: anatomy, containment_access, ethics_morality, gender, honor_shame, reproduction_birth, rhetoric_discourse, sexuality
  - keywords: anatomy, gender, reproduction, sexuality
- `ح ي ي B012` — المحيا وجه الإنسان
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: anatomy, body, cognition, grammar_expression, identity_personhood, perception, posture_embodiment, visual_appearance
  - keywords: anatomy, appearance, body, embodiment, identity, perception, recognition
- `ح ي ي B013` — الحياة بمعنى النفع والخير
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: ethics_morality, hospitality_welfare, justice_judgment, law, protection_security
  - keywords: ethics, justice, law, protection, welfare
- `ح ي ي B014` — أسماء الأعلام من الحياة
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### د ن و

- `د ن و B001` — القرب والمقاربة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: containment_access, family, measurement, orientation_direction, social_relations, space
  - keywords: distance, family, orientation, relation, space
- `د ن و B002` — الدنيا والأدنى
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: ethics_morality, hierarchy_status, measurement, orientation_direction, place_location, reasoning_decision, sequence_cycle, sky_astronomy, time
  - keywords: comparison, cosmology, hierarchy, orientation, proximity, sequence, temporality
- `د ن و B003` — الدناءة والضعة
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: ethics_morality, hierarchy_status, honor_shame, justice_judgment, value_quality
  - keywords: ethics, hierarchy, honor, morality, quality, status, value
- `د ن و B004` — قرب النتاج
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: animal, body, boundary, husbandry, life_stage_aging, physiology, reproduction_birth, time
  - keywords: animal, biology, body, husbandry, reproduction, time
- `د ن و B005` — دنو الأعلى من الوسط
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ح ي ي, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: anatomy, body, disease_injury, form_structure, orientation_direction, place_location, posture_embodiment, surface_shape
  - keywords: anatomy, body, orientation, proximity

### ء خ ر

- `ء خ ر B001` — الآخرية بعد الأول أو غيره
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: identity_personhood, measurement, naming_classification, reasoning_decision, sequence_cycle, social_relations
  - keywords: classification, comparison, distance, identity, relation, sequence
- `ء خ ر B002` — التأخير إلى وقت لاحق
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, ص ل و
  - themes: commerce_exchange, intention_character, obligation_contract, sequence_cycle, time
  - keywords: obligation, process, time
- `ء خ ر B003` — المؤخر والخلف
  - activated_by_or_with: ء ث ر, ء و ل, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: anatomy, animal, body, boundary, orientation_direction, space, transport
  - keywords: anatomy, animal, body, orientation, space
- `ء خ ر B004` — الدار الآخرة
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### خ ي ر

- `خ ي ر B001` — الميل إلى الخير النافع
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: ethics_morality, hospitality_welfare, language_speech, protection_security, value_quality
  - keywords: ethics, morality, protection, value, welfare
- `خ ي ر B002` — فضل الصلاح والاصطفاء
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: ethics_morality, hierarchy_status, identity_personhood, intention_character, reasoning_decision, value_quality
  - keywords: ethics, excellence, identity, ranking, selection, status
- `خ ي ر B003` — طلب الخير بالاختيار والاستخارة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: agency_action, belief_revelation, communication, prayer_supplication, proof_uncertainty, reasoning_decision, trust_loyalty
  - keywords: agency, decision, guidance, prayer, selection, trust
- `خ ي ر B004` — المال المسمى خيرا
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `خ ي ر B005` — الكرم والهبة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, د ن و, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: abundance_scarcity, commerce_exchange, ethics_morality, hospitality_welfare, support_dependence, wealth_property
  - keywords: abundance, charity, gift, patronage
- `خ ي ر B006` — استدراج الحيوان من جحره
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, د ن و, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: animal, control_restraint, habitat_ecology, motion, provision_resource, tools_equipment, wildlife
  - keywords: animal, capture, ecology, habitat, hunting, movement, tool

### ب ق ي

- `ب ق ي B001` — دوام الشيء وبقاؤه
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ح ي ي, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: justice_judgment, memory_attention, mortality_death, stability_endurance, time
  - keywords: memory, mortality, preservation, time
- `ب ق ي B002` — البقية وما يبقى من الشيء
  - activated_by_or_with: ء ث ر, ء و ل, ح ي ي, خ ي ر, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: belief_revelation, economy, finance_debt, provision_resource, quantity_number, stability_endurance, substance_texture, wealth_property
  - keywords: blessing, economy, property, residue, survival
- `ب ق ي B003` — الإبقاء عفوا واستحياء
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: conflict, ethics_morality, justice_judgment, social_relations, stability_endurance, violence_warfare
  - keywords: conflict, forgiveness, justice, mercy, survival, violence
- `ب ق ي B004` — حبس بعض الشيء وادخاره
  - activated_by_or_with: ء ث ر, ء و ل, ح ي ي, خ ي ر, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: abundance_scarcity, agency_action, control_restraint, economy, motion, provision_resource, stability_endurance, storage_vessels, wealth_property
  - keywords: economy, motion, preparation, resource, scarcity, storage
- `ب ق ي B005` — ترقب الشيء وانتظاره بالبصر
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: memory_attention, motion, perception, time, travel, weather_climate
  - keywords: attention, movement, perception, time, travel, weather

### ص ح ف

- `ص ح ف B001` — انبساط وسعة
  - activated_by_or_with: ء خ ر, ء و ل, ح ي ي, د ن و, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: body, geography_landscape, measurement, space, surface_shape, terrain_desert, visual_appearance
  - keywords: appearance, body, space, topography
- `ص ح ف B002` — صحيفة مكتوبة
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: belief_revelation, communication, knowledge_learning, writing_text
  - keywords: archive, communication, knowledge, record, scripture, text
- `ص ح ف B003` — جمع الصحف في مصحف
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: belief_revelation, communication, ritual, stability_endurance, writing_text
  - keywords: archive, liturgy, preservation, scripture, text, transmission
- `ص ح ف B004` — صَحفة عريضة
  - activated_by_or_with: ء ث ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, ر ب ب, س م و, ص ل و
  - themes: food_nutrition, household_community, storage_vessels, tools_equipment, water_hydrology
  - keywords: container, domesticity, food, storage, water
- `ص ح ف B005` — تصحيف القراءة
  - activated_by_or_with: ء ث ر, ء خ ر, ء و ل, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: communication, language_speech, perception, proof_uncertainty, reasoning_decision, writing_text
  - keywords: perception, text, transmission

### ء و ل

- `ء و ل B001` — ابتداء الشيء وتقدمه
  - activated_by_or_with: ء ث ر, ء خ ر, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: hierarchy_status, motion, orientation_direction, sequence_cycle, time
  - keywords: hierarchy, motion, orientation, priority, process, sequence, temporality
- `ء و ل B002` — رجوع الشيء إلى مآله وعاقبته
  - activated_by_or_with: ء ث ر, ء خ ر, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: belief_revelation, change_transition, intention_character, language_speech, motion, reasoning_decision
  - keywords: semantics, transformation
- `ء و ل B003` — آل الرجل من يرجع إليهم ويرجعون إليه
  - activated_by_or_with: ء ث ر, ء خ ر, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: household_community, identity_personhood, kinship, marriage_genealogy, social_relations, support_dependence
  - keywords: community, genealogy, household, identity, kinship, patronage, sociality
- `ء و ل B004` — إيالة الأمر بإصلاحه وسياسته
  - activated_by_or_with: ء ث ر, ب ق ي, ح ي ي, خ ي ر, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: authority_governance, change_transition, craft, economy, politics_order, protection_security
  - keywords: administration, authority, economy, governance, politics, stewardship
- `ء و ل B005` — خثور السائل وانعقاده في آخر أمره
  - activated_by_or_with: ء ث ر, ء خ ر, ب ق ي, ح ي ي, د ن و, ذ ك ر, ر ب ب, ص ح ف, ص ل و
  - themes: change_transition, food_nutrition, material, physiology, sequence_cycle, substance_texture
  - keywords: food, material, process, transformation
- `ء و ل B006` — الشخص المترائي والطرف الظاهر
  - activated_by_or_with: ء ث ر, ء خ ر, ب ق ي, ح ي ي, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: boundary, form_structure, geography_landscape, orientation_direction, perception, terrain_desert, visual_appearance
  - keywords: appearance, landscape, morphology, orientation, perception, topography, visibility
- `ء و ل B007` — آلة الحال التي يكون عليها الشيء
  - activated_by_or_with: ء ث ر, ء خ ر, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ل و
  - themes: abundance_scarcity, cognition, grammar_expression, hierarchy_status, naming_classification, rhetoric_discourse, value_quality
  - keywords: classification, evaluation, fortune, quality, status
- `ء و ل B008` — الآلة الحاملة أو الأداة
  - activated_by_or_with: ء ث ر, ء خ ر, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: architecture_construction, material, mortality_death, ritual, support_dependence, tools_equipment, transport, value_quality
  - keywords: material, shelter, tool, transport
- `ء و ل B009` — الأيل الذي يأوي إلى الجبل
  - activated_by_or_with: ء ث ر, ء خ ر, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: animal, geography_landscape, habitat_ecology, protection_security, terrain_desert, wildlife
  - keywords: habitat, topography, wildlife, zoology
- `ء و ل B010` — الإيال وعاء الشراب حتى يجود
  - activated_by_or_with: ء ث ر, ء خ ر, ب ق ي, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: cooking_drink, craft, life_stage_aging, stability_endurance, storage_vessels, time, value_quality
  - keywords: container, craft, drink, maturation, preservation, quality, storage, time
- `ء و ل B011` — التأويل اسم بقلة معزول
  - activated_by_or_with: ء ث ر, ء خ ر, ح ي ي, خ ي ر, د ن و, ذ ك ر, ر ب ب, س م و, ص ح ف, ص ل و
  - themes: agriculture, animal, food_nutrition, habitat_ecology, husbandry, naming_classification, pasture_forage, plant_vegetation
  - keywords: agriculture, botany, ecology, forage, pasture, taxonomy

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
