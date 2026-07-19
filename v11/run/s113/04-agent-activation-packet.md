# v11 Activation Packet — S113:1-None

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_1: قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ
- verse_2: مِن شَرِّ مَا خَلَقَ
- verse_3: وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ
- verse_4: وَمِن شَرِّ ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ
- verse_5: وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ق و ل → ع و ذ → ر ب ب → ف ل ق → ش ر ر → خ ل ق → غ س ق → و ق ب → ن ف ث → ع ق د → ح س د

## Branch inventory summary

- ق و ل: 17 branches (16 with Qnet bridge-theme nodes; 1 Furūq-only)
- ع و ذ: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ر ب ب: 17 branches (17 with Qnet bridge-theme nodes; 0 Furūq-only)
- ف ل ق: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- ش ر ر: 12 branches (12 with Qnet bridge-theme nodes; 0 Furūq-only)
- خ ل ق: 12 branches (11 with Qnet bridge-theme nodes; 1 Furūq-only)
- غ س ق: 5 branches (4 with Qnet bridge-theme nodes; 1 Furūq-only)
- و ق ب: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن ف ث: 5 branches (3 with Qnet bridge-theme nodes; 2 Furūq-only)
- ع ق د: 17 branches (17 with Qnet bridge-theme nodes; 0 Furūq-only)
- ح س د: 2 branches (2 with Qnet bridge-theme nodes; 0 Furūq-only)

## QAC-first root resolution audit

- ق و ل | qac_keys=قول | status=resolved | matches=root_001272
- ع و ذ | qac_keys=عوذ | status=resolved | matches=root_001059
- ر ب ب | qac_keys=ربب | status=resolved | matches=root_000532
- ف ل ق | qac_keys=فلق | status=resolved | matches=root_001176
- ش ر ر | qac_keys=شرر | status=resolved | matches=root_000787
- خ ل ق | qac_keys=خلق | status=resolved | matches=root_000434
- غ س ق | qac_keys=غسق | status=resolved | matches=root_001086
- و ق ب | qac_keys=وقب | status=resolved | matches=root_001670
- ن ف ث | qac_keys=نفث | status=resolved | matches=root_001527
- ع ق د | qac_keys=عقد | status=resolved | matches=root_001034
- ح س د | qac_keys=حسد | status=resolved | matches=root_000319

## Top candidate bridges

- `غ س ق B001` ↔ `و ق ب B002` | score_hint=27 | discovery_hint=18 | themes=calendar_season, change_transition, light_darkness, sky_astronomy, time | keywords=astronomy, night, time, transition | q2=—
- `ر ب ب B008` ↔ `ف ل ق B003` | score_hint=26 | discovery_hint=18 | themes=agriculture, habitat_ecology, reproduction_birth, sky_astronomy, weather_climate | keywords=agriculture, fertility, meteorology, weather | q2=—
- `ر ب ب B012` ↔ `ش ر ر B012` | score_hint=24 | discovery_hint=17 | themes=agriculture, habitat_ecology, physiology, plant_vegetation | keywords=agriculture, botany, ecology, life | q2=—
- `ف ل ق B003` ↔ `ش ر ر B012` | score_hint=24 | discovery_hint=17 | themes=agriculture, habitat_ecology, physiology, plant_vegetation | keywords=agriculture, botany, life, nature | q2=—
- `و ق ب B005` ↔ `ع ق د B004` | score_hint=13 | discovery_hint=17 | themes=economy, wealth_property | keywords=economy, property | q2=—
- `غ س ق B004` ↔ `ن ف ث B002` | score_hint=28 | discovery_hint=16 | themes=disease_injury, health_medicine, physiology, substance_texture | keywords=discharge, fluid, injury, medicine, secretion | q2=—
- `ق و ل B002` ↔ `و ق ب B003` | score_hint=26 | discovery_hint=16 | themes=anatomy, body, communication, language_speech, physiology | keywords=anatomy, body, communication, physiology | q2=—
- `ر ب ب B012` ↔ `ع ق د B005` | score_hint=24 | discovery_hint=16 | themes=agriculture, geography_landscape, habitat_ecology, plant_vegetation | keywords=agriculture, botany, ecology, landscape | q2=—
- `ر ب ب B012` ↔ `ف ل ق B003` | score_hint=20 | discovery_hint=16 | themes=agriculture, habitat_ecology, physiology, plant_vegetation | keywords=agriculture, botany, life | q2=—
- `ف ل ق B003` ↔ `ع ق د B005` | score_hint=20 | discovery_hint=16 | themes=agriculture, habitat_ecology, plant_vegetation, reproduction_birth | keywords=agriculture, botany, fertility | q2=—
- `ر ب ب B012` ↔ `ع ق د B009` | score_hint=18 | discovery_hint=16 | themes=agriculture, food_nutrition, plant_vegetation | keywords=agriculture, botany, food | q2=—
- `ع و ذ B002` ↔ `ع ق د B013` | score_hint=28 | discovery_hint=15 | themes=belief_revelation, protection_security, religion_worship, ritual | keywords=magic, protection, religion, ritual, superstition | q2=—
- `خ ل ق B011` ↔ `ع ق د B008` | score_hint=24 | discovery_hint=15 | themes=earth_geology, geography_landscape, water_hydrology, weather_climate | keywords=geology, hydrology, landscape, water | q2=—
- `و ق ب B003` ↔ `ع ق د B010` | score_hint=22 | discovery_hint=15 | themes=anatomy, animal, body | keywords=anatomy, animal, body, zoology | q2=—
- `ع و ذ B003` ↔ `ر ب ب B005` | score_hint=20 | discovery_hint=15 | themes=hospitality_welfare, kinship, reproduction_birth, support_dependence | keywords=dependency, kinship, nursing | q2=—
- `ع و ذ B003` ↔ `ر ب ب B009` | score_hint=18 | discovery_hint=15 | themes=animal, life_stage_aging, reproduction_birth | keywords=animal, infancy, reproduction | q2=—
- `ر ب ب B006` ↔ `ع ق د B003` | score_hint=18 | discovery_hint=15 | themes=food_nutrition, stability_endurance, substance_texture | keywords=food, preservation, substance | q2=—
- `ر ب ب B008` ↔ `ع ق د B005` | score_hint=18 | discovery_hint=15 | themes=agriculture, habitat_ecology, reproduction_birth | keywords=agriculture, ecology, fertility | q2=—
- `ش ر ر B002` ↔ `ع ق د B003` | score_hint=18 | discovery_hint=15 | themes=agriculture, food_nutrition, stability_endurance | keywords=agriculture, food, preservation | q2=—
- `ش ر ر B012` ↔ `ع ق د B005` | score_hint=18 | discovery_hint=15 | themes=agriculture, habitat_ecology, plant_vegetation | keywords=agriculture, botany, ecology | q2=—
- `ع و ذ B005` ↔ `و ق ب B007` | score_hint=11 | discovery_hint=15 | themes=animal, ornament_beauty, pattern_marking | keywords=ornament | q2=—
- `ر ب ب B017` ↔ `و ق ب B006` | score_hint=11 | discovery_hint=15 | themes=labor_work, navigation_route, travel | keywords=travel | q2=—
- `ر ب ب B013` ↔ `غ س ق B005` | score_hint=7 | discovery_hint=15 | themes=purity_cleansing | keywords=purity | q2=—
- `ق و ل B010` ↔ `ر ب ب B001` | score_hint=22 | discovery_hint=14 | themes=authority_governance, force_power, hierarchy_status | keywords=authority, governance, hierarchy, power | q2=—
- `ق و ل B010` ↔ `ف ل ق B007` | score_hint=20 | discovery_hint=14 | themes=authority_governance, conflict, force_power, hierarchy_status | keywords=conflict, hierarchy, power | q2=—
- `ر ب ب B007` ↔ `و ق ب B002` | score_hint=20 | discovery_hint=14 | themes=motion, place_location, time, weather_climate | keywords=movement, time, weather | q2=—
- `ف ل ق B002` ↔ `و ق ب B002` | score_hint=20 | discovery_hint=14 | themes=change_transition, light_darkness, sky_astronomy, time | keywords=cosmology, time, transition | q2=—
- `خ ل ق B004` ↔ `ع ق د B006` | score_hint=20 | discovery_hint=14 | themes=cognition, ethics_morality, identity_personhood, social_relations | keywords=ethics, identity, psychology | q2=—
- `ق و ل B002` ↔ `ن ف ث B003` | score_hint=18 | discovery_hint=14 | themes=body, grammar_expression, language_speech | keywords=body, expression, speech | q2=—
- `ر ب ب B006` ↔ `ش ر ر B002` | score_hint=18 | discovery_hint=14 | themes=agency_action, food_nutrition, stability_endurance | keywords=food, preparation, preservation | q2=—
- `ن ف ث B003` ↔ `ع ق د B015` | score_hint=18 | discovery_hint=14 | themes=body, language_speech, rhetoric_discourse | keywords=body, metaphor, speech | q2=—
- `ر ب ب B008` ↔ `ع ق د B008` | score_hint=16 | discovery_hint=14 | themes=water_hydrology, weather_climate | keywords=meteorology, water, weather | q2=—
- `ف ل ق B003` ↔ `خ ل ق B002` | score_hint=16 | discovery_hint=14 | themes=belief_revelation, sky_astronomy | keywords=cosmology, creation, genesis | q2=—
- `ر ب ب B006` ↔ `غ س ق B005` | score_hint=14 | discovery_hint=14 | themes=food_nutrition, material, substance_texture | keywords=food, substance | q2=—
- `ش ر ر B002` ↔ `ع ق د B009` | score_hint=14 | discovery_hint=14 | themes=agriculture, food_nutrition, stability_endurance | keywords=agriculture, food | q2=—
- `ش ر ر B005` ↔ `ع ق د B003` | score_hint=14 | discovery_hint=14 | themes=cooking_drink, food_nutrition, substance_texture | keywords=cooking, food | q2=—
- `ر ب ب B008` ↔ `ش ر ر B002` | score_hint=12 | discovery_hint=14 | themes=agriculture, weather_climate | keywords=agriculture, weather | q2=—
- `ر ب ب B012` ↔ `ش ر ر B002` | score_hint=12 | discovery_hint=14 | themes=agriculture, food_nutrition | keywords=agriculture, food | q2=—
- `ر ب ب B012` ↔ `ع ق د B003` | score_hint=12 | discovery_hint=14 | themes=agriculture, food_nutrition | keywords=agriculture, food | q2=—
- `ف ل ق B003` ↔ `ش ر ر B002` | score_hint=12 | discovery_hint=14 | themes=agriculture, weather_climate | keywords=agriculture, weather | q2=—
- `ف ل ق B003` ↔ `و ق ب B002` | score_hint=12 | discovery_hint=14 | themes=sky_astronomy, weather_climate | keywords=cosmology, weather | q2=—
- `ف ل ق B003` ↔ `ع ق د B009` | score_hint=12 | discovery_hint=14 | themes=agriculture, plant_vegetation | keywords=agriculture, botany | q2=—
- `ش ر ر B004` ↔ `خ ل ق B008` | score_hint=12 | discovery_hint=14 | themes=body, substance_texture | keywords=body, texture | q2=—
- `ش ر ر B012` ↔ `ع ق د B009` | score_hint=12 | discovery_hint=14 | themes=agriculture, plant_vegetation | keywords=agriculture, botany | q2=—
- `غ س ق B005` ↔ `ع ق د B003` | score_hint=12 | discovery_hint=14 | themes=food_nutrition, substance_texture | keywords=food, substance | q2=—
- `ق و ل B005` ↔ `ش ر ر B001` | score_hint=11 | discovery_hint=14 | themes=deception_corruption, ethics_morality, justice_judgment | keywords=ethics | q2=—
- `ق و ل B002` ↔ `ع ق د B007` | score_hint=18 | discovery_hint=13 | themes=communication, grammar_expression, language_speech | keywords=communication, expression, language | q2=—
- `ع و ذ B005` ↔ `ش ر ر B006` | score_hint=18 | discovery_hint=13 | themes=anatomy, animal, ornament_beauty | keywords=anatomy, animal, ornament | q2=—
- `ع و ذ B005` ↔ `و ق ب B003` | score_hint=18 | discovery_hint=13 | themes=anatomy, animal, livestock | keywords=anatomy, animal, horse | q2=—
- `ع و ذ B008` ↔ `ف ل ق B006` | score_hint=18 | discovery_hint=13 | themes=conflict, emotion, social_relations | keywords=conflict, emotion, society | q2=—
- `ع و ذ B008` ↔ `ش ر ر B011` | score_hint=18 | discovery_hint=13 | themes=conflict, emotion, social_relations | keywords=conflict, emotion, sociality | q2=—
- `خ ل ق B004` ↔ `ع ق د B012` | score_hint=18 | discovery_hint=13 | themes=cognition, ethics_morality, intention_character | keywords=ethics, morality, psychology | q2=—
- `ع و ذ B001` ↔ `ع ق د B017` | score_hint=16 | discovery_hint=13 | themes=danger_harm, protection_security | keywords=protection, safety, vulnerability | q2=—
- `ر ب ب B007` ↔ `ع ق د B010` | score_hint=16 | discovery_hint=13 | themes=animal, motion | keywords=animal, motion, movement | q2=—
- `ش ر ر B004` ↔ `ع ق د B010` | score_hint=16 | discovery_hint=13 | themes=anatomy, body, form_structure, motion | keywords=body, motion | q2=—
- `و ق ب B003` ↔ `ع ق د B011` | score_hint=16 | discovery_hint=13 | themes=anatomy, animal, body, livestock | keywords=anatomy, animal | q2=—
- `ع و ذ B004` ↔ `ع ق د B005` | score_hint=14 | discovery_hint=13 | themes=geography_landscape, habitat_ecology, plant_vegetation | keywords=botany, habitat | q2=—
- `ر ب ب B007` ↔ `غ س ق B004` | score_hint=14 | discovery_hint=13 | themes=geography_landscape, motion, weather_climate | keywords=movement, weather | q2=—
- `ش ر ر B004` ↔ `ع ق د B017` | score_hint=14 | discovery_hint=13 | themes=body, danger_harm, motion | keywords=body, motion | q2=—
- `ش ر ر B007` ↔ `ع ق د B006` | score_hint=14 | discovery_hint=13 | themes=emotion, identity_personhood, social_relations | keywords=emotion, identity | q2=—
- `ش ر ر B009` ↔ `و ق ب B003` | score_hint=14 | discovery_hint=13 | themes=anatomy, animal, body | keywords=animal, body | q2=—
- `ش ر ر B009` ↔ `ع ق د B010` | score_hint=14 | discovery_hint=13 | themes=anatomy, animal, body | keywords=animal, body | q2=—
- `غ س ق B003` ↔ `ن ف ث B002` | score_hint=14 | discovery_hint=13 | themes=body, disease_injury, health_medicine | keywords=body, medicine | q2=—
- `ق و ل B002` ↔ `ع ق د B010` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ق و ل B002` ↔ `ع ق د B015` | score_hint=12 | discovery_hint=13 | themes=body, language_speech | keywords=body, speech | q2=—
- `ق و ل B006` ↔ `ش ر ر B007` | score_hint=12 | discovery_hint=13 | themes=agency_action, identity_personhood | keywords=agency, identity | q2=—
- `ق و ل B006` ↔ `خ ل ق B004` | score_hint=12 | discovery_hint=13 | themes=ethics_morality, identity_personhood | keywords=identity, morality | q2=—
- `ع و ذ B004` ↔ `ع ق د B009` | score_hint=12 | discovery_hint=13 | themes=plant_vegetation, stability_endurance | keywords=botany, cohesion | q2=—
- `ر ب ب B008` ↔ `ش ر ر B012` | score_hint=12 | discovery_hint=13 | themes=agriculture, habitat_ecology | keywords=agriculture, ecology | q2=—
- `ر ب ب B011` ↔ `ع ق د B016` | score_hint=12 | discovery_hint=13 | themes=household_community, protection_security | keywords=community, protection | q2=—
- `غ س ق B004` ↔ `و ق ب B002` | score_hint=12 | discovery_hint=13 | themes=motion, weather_climate | keywords=movement, weather | q2=—
- `غ س ق B004` ↔ `ع ق د B008` | score_hint=12 | discovery_hint=13 | themes=geography_landscape, weather_climate | keywords=landscape, weather | q2=—
- `ف ل ق B003` ↔ `ع ق د B008` | score_hint=10 | discovery_hint=13 | themes=weather_climate | keywords=meteorology, weather | q2=—
- `ر ب ب B002` ↔ `ع ق د B003` | score_hint=10 | discovery_hint=13 | themes=agriculture, growth_decay, stability_endurance | keywords=agriculture | q2=—
- `ر ب ب B009` ↔ `خ ل ق B009` | score_hint=10 | discovery_hint=13 | themes=food_nutrition, life_stage_aging, time | keywords=time | q2=—
- `ق و ل B002` ↔ `ن ف ث B002` | score_hint=8 | discovery_hint=13 | themes=body, physiology | keywords=body | q2=—
- `ر ب ب B006` ↔ `ش ر ر B005` | score_hint=8 | discovery_hint=13 | themes=food_nutrition, substance_texture | keywords=food | q2=—
- `ر ب ب B008` ↔ `و ق ب B002` | score_hint=8 | discovery_hint=13 | themes=sky_astronomy, weather_climate | keywords=weather | q2=—
- `ف ل ق B003` ↔ `غ س ق B004` | score_hint=8 | discovery_hint=13 | themes=physiology, weather_climate | keywords=weather | q2=—
- `ف ل ق B007` ↔ `ع ق د B013` | score_hint=8 | discovery_hint=13 | themes=force_power, protection_security | keywords=power | q2=—

## Per-root candidate activations

### ق و ل

- `ق و ل B001` — إخراج القول بالنطق
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B002` — اللسان آلة القول
  - activated_by_or_with: ع ق د, ن ف ث, و ق ب
  - themes: anatomy, body, communication, grammar_expression, language_speech, physiology
  - keywords: anatomy, body, communication, expression, language, physiology, speech
- `ق و ل B003` — كثرة القول في صاحبه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B004` — القيل صاحب القول النافذ
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B005` — قول ما لم يكن أو نسبته
  - activated_by_or_with: ش ر ر
  - themes: deception_corruption, ethics_morality, justice_judgment
  - keywords: ethics
- `ق و ل B006` — اجترار القول إلى النفس
  - activated_by_or_with: خ ل ق, ش ر ر
  - themes: agency_action, ethics_morality, identity_personhood
  - keywords: agency, identity, morality
- `ق و ل B007` — القول الفاشي بين الناس
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B008` — عود القال لضرب القلة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B009` — المقاولة في الأمر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B010` — اقتالة الحكم على غيره
  - activated_by_or_with: ر ب ب, ف ل ق
  - themes: authority_governance, conflict, force_power, hierarchy_status
  - keywords: authority, conflict, governance, hierarchy, power
- `ق و ل B011` — قول يجري مجرى الظن
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B012` — قول في النفس لم يظهر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B013` — القول اعتقاد ومذهب
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B014` — قول الشيء دلالته
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B015` — العناية الصادقة بالشيء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B016` — قول الشيء حده
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B017` — القول إلهام يلقي معنى
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### ع و ذ

- `ع و ذ B001` — الالتجاء والاعتصام
  - activated_by_or_with: ع ق د
  - themes: danger_harm, protection_security
  - keywords: protection, safety, vulnerability
- `ع و ذ B002` — الوقاية بعوذة أو تعويذ
  - activated_by_or_with: ع ق د
  - themes: belief_revelation, protection_security, religion_worship, ritual
  - keywords: magic, protection, religion, ritual, superstition
- `ع و ذ B003` — الأنثى العائذ بعد الولادة
  - activated_by_or_with: ر ب ب
  - themes: animal, hospitality_welfare, kinship, life_stage_aging, reproduction_birth, support_dependence
  - keywords: animal, dependency, infancy, kinship, nursing, reproduction
- `ع و ذ B004` — اللصوق والملازمة في كنف شيء
  - activated_by_or_with: ع ق د
  - themes: geography_landscape, habitat_ecology, plant_vegetation, stability_endurance
  - keywords: botany, cohesion, habitat
- `ع و ذ B005` — معوذ الفرس في موضع القلادة
  - activated_by_or_with: ش ر ر, و ق ب
  - themes: anatomy, animal, livestock, ornament_beauty, pattern_marking
  - keywords: anatomy, animal, horse, ornament
- `ع و ذ B006` — الإفلات عوذا بتخويف دون تمام الفعل
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع و ذ B007` — تعاوذ القوم في الحرب وتواكلوا
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع و ذ B008` — التحامي كراهة من الشيء
  - activated_by_or_with: ش ر ر, ف ل ق
  - themes: conflict, emotion, social_relations
  - keywords: conflict, emotion, sociality, society

### ر ب ب

- `ر ب ب B001` — ربوبية وملك وسيادة
  - activated_by_or_with: ق و ل
  - themes: authority_governance, force_power, hierarchy_status
  - keywords: authority, governance, hierarchy, power
- `ر ب ب B002` — إصلاح وتربية وإتمام
  - activated_by_or_with: ع ق د
  - themes: agriculture, growth_decay, stability_endurance
  - keywords: agriculture
- `ر ب ب B003` — علم رباني
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B004` — ربة وجماعات كثيرة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B005` — ربيب وربيبة ورابة
  - activated_by_or_with: ع و ذ
  - themes: hospitality_welfare, kinship, reproduction_birth, support_dependence
  - keywords: dependency, kinship, nursing
- `ر ب ب B006` — رُبّ خاثر وإصلاح به
  - activated_by_or_with: ش ر ر, ع ق د, غ س ق
  - themes: agency_action, food_nutrition, material, stability_endurance, substance_texture
  - keywords: food, preparation, preservation, substance
- `ر ب ب B007` — لزوم وإقامة ودوام
  - activated_by_or_with: ع ق د, غ س ق, و ق ب
  - themes: animal, geography_landscape, motion, place_location, time, weather_climate
  - keywords: animal, motion, movement, time, weather
- `ر ب ب B008` — رباب السحاب
  - activated_by_or_with: ش ر ر, ع ق د, ف ل ق, و ق ب
  - themes: agriculture, habitat_ecology, reproduction_birth, sky_astronomy, water_hydrology, weather_climate
  - keywords: agriculture, ecology, fertility, meteorology, water, weather
- `ر ب ب B009` — شاة رُبّى وحداثة
  - activated_by_or_with: خ ل ق, ع و ذ
  - themes: animal, food_nutrition, life_stage_aging, reproduction_birth, time
  - keywords: animal, infancy, reproduction, time
- `ر ب ب B010` — ربابة تجمع القداح
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B011` — ربابة عهد وميثاق
  - activated_by_or_with: ع ق د
  - themes: household_community, protection_security
  - keywords: community, protection
- `ر ب ب B012` — ربة نبات
  - activated_by_or_with: ش ر ر, ع ق د, ف ل ق
  - themes: agriculture, food_nutrition, geography_landscape, habitat_ecology, physiology, plant_vegetation
  - keywords: agriculture, botany, ecology, food, landscape, life
- `ر ب ب B013` — ماء رَبَب كثير
  - activated_by_or_with: غ س ق
  - themes: purity_cleansing
  - keywords: purity
- `ر ب ب B014` — رَبْرَب قطيع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B015` — حرف رب وربما
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B016` — رُبَى حاجة وعقدة ونعمة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B017` — رباني الملاحين
  - activated_by_or_with: و ق ب
  - themes: labor_work, navigation_route, travel
  - keywords: travel

### ف ل ق

- `ف ل ق B001` — شق وفتح بين شيئين
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ف ل ق B002` — انفلاق الصبح وبيانه
  - activated_by_or_with: و ق ب
  - themes: change_transition, light_darkness, sky_astronomy, time
  - keywords: cosmology, time, transition
- `ف ل ق B003` — إبراز الخلق من الانفلاق
  - activated_by_or_with: خ ل ق, ر ب ب, ش ر ر, ع ق د, غ س ق, و ق ب
  - themes: agriculture, belief_revelation, habitat_ecology, physiology, plant_vegetation, reproduction_birth, sky_astronomy, weather_climate
  - keywords: agriculture, botany, cosmology, creation, fertility, genesis, life, meteorology, nature, weather
- `ف ل ق B004` — فرجة منخفضة بين مرتفعين
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ف ل ق B005` — مقطرة السجين
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ف ل ق B006` — داهية وعجب عظيم
  - activated_by_or_with: ع و ذ
  - themes: conflict, emotion, social_relations
  - keywords: conflict, emotion, society
- `ف ل ق B007` — فيلق الجيش والكتائب
  - activated_by_or_with: ع ق د, ق و ل
  - themes: authority_governance, conflict, force_power, hierarchy_status, protection_security
  - keywords: conflict, hierarchy, power

### ش ر ر

- `ش ر ر B001` — الشَّرّ والسوء
  - activated_by_or_with: ق و ل
  - themes: deception_corruption, ethics_morality, justice_judgment
  - keywords: ethics
- `ش ر ر B002` — نشر الشيء في الشمس ليجف
  - activated_by_or_with: ر ب ب, ع ق د, ف ل ق
  - themes: agency_action, agriculture, food_nutrition, stability_endurance, weather_climate
  - keywords: agriculture, food, preparation, preservation, weather
- `ش ر ر B003` — شَرَر النار المتطاير
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ش ر ر B004` — الشَّرْشَرَة تقطيع ونفض
  - activated_by_or_with: خ ل ق, ع ق د
  - themes: anatomy, body, danger_harm, form_structure, motion, substance_texture
  - keywords: body, motion, texture
- `ش ر ر B005` — الشواء المتقاطر دسمه
  - activated_by_or_with: ر ب ب, ع ق د
  - themes: cooking_drink, food_nutrition, substance_texture
  - keywords: cooking, food
- `ش ر ر B006` — الشراشر ذباذب وأثقال
  - activated_by_or_with: ع و ذ
  - themes: anatomy, animal, ornament_beauty
  - keywords: anatomy, animal, ornament
- `ش ر ر B007` — إلقاء الشراشر إلقاء النفس كلها
  - activated_by_or_with: ع ق د, ق و ل
  - themes: agency_action, emotion, identity_personhood, social_relations
  - keywords: agency, emotion, identity
- `ش ر ر B008` — إظهار الشيء وإبرازه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ش ر ر B009` — الشَّرّان أذى كالبعوض
  - activated_by_or_with: ع ق د, و ق ب
  - themes: anatomy, animal, body
  - keywords: animal, body
- `ش ر ر B010` — شِرّة الشباب نشاط وحرص
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ش ر ر B011` — المشارة مخاصمة
  - activated_by_or_with: ع و ذ
  - themes: conflict, emotion, social_relations
  - keywords: conflict, emotion, sociality
- `ش ر ر B012` — الشِّرْشِر نبت
  - activated_by_or_with: ر ب ب, ع ق د, ف ل ق
  - themes: agriculture, habitat_ecology, physiology, plant_vegetation
  - keywords: agriculture, botany, ecology, life, nature

### خ ل ق

- `خ ل ق B001` — تقدير الشيء وقياسه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ ل ق B002` — إبداع الخلق وإيجاده
  - activated_by_or_with: ف ل ق
  - themes: belief_revelation, sky_astronomy
  - keywords: cosmology, creation, genesis
- `خ ل ق B003` — تمام الخلقة واعتدال الصورة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ ل ق B004` — السجية والطبيعة الباطنة
  - activated_by_or_with: ع ق د, ق و ل
  - themes: cognition, ethics_morality, identity_personhood, intention_character, social_relations
  - keywords: ethics, identity, morality, psychology
- `خ ل ق B005` — الجدارة والتهيؤ للشيء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ ل ق B006` — الخلاق نصيب الخير
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `خ ل ق B007` — اختلاق الكذب والكلام
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ ل ق B008` — ملاسة السطح واستواؤه
  - activated_by_or_with: ش ر ر
  - themes: body, substance_texture
  - keywords: body, texture
- `خ ل ق B009` — بلى الثوب وذهاب وبره
  - activated_by_or_with: ر ب ب
  - themes: food_nutrition, life_stage_aging, time
  - keywords: time
- `خ ل ق B010` — الخلوق والتخليق بالطيب
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ ل ق B011` — نقرة أو بئر تمسك الماء
  - activated_by_or_with: ع ق د
  - themes: earth_geology, geography_landscape, water_hydrology, weather_climate
  - keywords: geology, hydrology, landscape, water
- `خ ل ق B012` — انسداد مصمت كالصخرة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### غ س ق

- `غ س ق B001` — ظلمة الليل ودخوله
  - activated_by_or_with: و ق ب
  - themes: calendar_season, change_transition, light_darkness, sky_astronomy, time
  - keywords: astronomy, night, time, transition
- `غ س ق B002` — الغَسّاق المنتن البارد
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `غ س ق B003` — إظلام العين
  - activated_by_or_with: ن ف ث
  - themes: body, disease_injury, health_medicine
  - keywords: body, medicine
- `غ س ق B004` — سيلان وانصباب
  - activated_by_or_with: ر ب ب, ع ق د, ف ل ق, ن ف ث, و ق ب
  - themes: disease_injury, geography_landscape, health_medicine, motion, physiology, substance_texture, weather_climate
  - keywords: discharge, fluid, injury, landscape, medicine, movement, secretion, weather
- `غ س ق B005` — شوائب الطعام
  - activated_by_or_with: ر ب ب, ع ق د
  - themes: food_nutrition, material, purity_cleansing, substance_texture
  - keywords: food, purity, substance

### و ق ب

- `و ق ب B001` — نقرة أو حفرة يغيب فيها الشيء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `و ق ب B002` — دخول الشيء في مغاب حتى يغيب أو ينزل الظلام
  - activated_by_or_with: ر ب ب, غ س ق, ف ل ق
  - themes: calendar_season, change_transition, light_darkness, motion, place_location, sky_astronomy, time, weather_climate
  - keywords: astronomy, cosmology, movement, night, time, transition, weather
- `و ق ب B003` — صوت يخرج من قنب الدابة
  - activated_by_or_with: ش ر ر, ع ق د, ع و ذ, ق و ل
  - themes: anatomy, animal, body, communication, language_speech, livestock, physiology
  - keywords: anatomy, animal, body, communication, horse, physiology, zoology
- `و ق ب B004` — الجوع الذي يقع بالقوم
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `و ق ب B005` — قماش البيت ومتاعه
  - activated_by_or_with: ع ق د
  - themes: economy, wealth_property
  - keywords: economy, property
- `و ق ب B006` — مواصلة السير بين يوم وليلة
  - activated_by_or_with: ر ب ب
  - themes: labor_work, navigation_route, travel
  - keywords: travel
- `و ق ب B007` — ودعة تسمى الميقب
  - activated_by_or_with: ع و ذ
  - themes: animal, ornament_beauty, pattern_marking
  - keywords: ornament

### ن ف ث

- `ن ف ث B001` — نَفْثٌ من الفم بريق قليل
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن ف ث B002` — نَفْثُ الجرح للدم
  - activated_by_or_with: غ س ق, ق و ل
  - themes: body, disease_injury, health_medicine, physiology, substance_texture
  - keywords: body, discharge, fluid, injury, medicine, secretion
- `ن ف ث B003` — نَفْثُ المصدور
  - activated_by_or_with: ع ق د, ق و ل
  - themes: body, grammar_expression, language_speech, rhetoric_discourse
  - keywords: body, expression, metaphor, speech
- `ن ف ث B004` — نَفْثٌ في الروع بمعنى الإيحاء
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ن ف ث B005` — الشعر كشيء ينفث من الفم
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### ع ق د

- `ع ق د B001` — شد الأطراف وربطها
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ق د B002` — إلزام العهد وإبرامه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ق د B003` — غلظ المائع وصلبه
  - activated_by_or_with: ر ب ب, ش ر ر, غ س ق
  - themes: agriculture, cooking_drink, food_nutrition, growth_decay, stability_endurance, substance_texture
  - keywords: agriculture, cooking, food, preservation, substance
- `ع ق د B004` — اقتناء المال والضيعة
  - activated_by_or_with: و ق ب
  - themes: economy, wealth_property
  - keywords: economy, property
- `ع ق د B005` — كثافة الشجر والمرعى
  - activated_by_or_with: ر ب ب, ش ر ر, ع و ذ, ف ل ق
  - themes: agriculture, geography_landscape, habitat_ecology, plant_vegetation, reproduction_birth
  - keywords: agriculture, botany, ecology, fertility, habitat, landscape
- `ع ق د B006` — ثبات القلب والرأي
  - activated_by_or_with: خ ل ق, ش ر ر
  - themes: cognition, emotion, ethics_morality, identity_personhood, social_relations
  - keywords: emotion, ethics, identity, psychology
- `ع ق د B007` — حبسة اللسان وتعقيد الكلام
  - activated_by_or_with: ق و ل
  - themes: communication, grammar_expression, language_speech
  - keywords: communication, expression, language
- `ع ق د B008` — تراكم الرمل وانقباض السحاب
  - activated_by_or_with: خ ل ق, ر ب ب, غ س ق, ف ل ق
  - themes: earth_geology, geography_landscape, water_hydrology, weather_climate
  - keywords: geology, hydrology, landscape, meteorology, water, weather
- `ع ق د B009` — عنقود متماسك
  - activated_by_or_with: ر ب ب, ش ر ر, ع و ذ, ف ل ق
  - themes: agriculture, food_nutrition, plant_vegetation, stability_endurance
  - keywords: agriculture, botany, cohesion, food
- `ع ق د B010` — التواء عضو الحيوان
  - activated_by_or_with: ر ب ب, ش ر ر, ق و ل, و ق ب
  - themes: anatomy, animal, body, form_structure, motion
  - keywords: anatomy, animal, body, motion, movement, zoology
- `ع ق د B011` — وثاقة البدن وقصره
  - activated_by_or_with: و ق ب
  - themes: anatomy, animal, body, livestock
  - keywords: anatomy, animal
- `ع ق د B012` — انقباض الغضب والخلق
  - activated_by_or_with: خ ل ق
  - themes: cognition, ethics_morality, intention_character
  - keywords: ethics, morality, psychology
- `ع ق د B013` — عقد السحر والعزائم
  - activated_by_or_with: ع و ذ, ف ل ق
  - themes: belief_revelation, force_power, protection_security, religion_worship, ritual
  - keywords: magic, power, protection, religion, ritual, superstition
- `ع ق د B014` — الحساب بعقد الأصابع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ق د B015` — قرب معقد الإزار
  - activated_by_or_with: ق و ل, ن ف ث
  - themes: body, language_speech, rhetoric_discourse
  - keywords: body, metaphor, speech
- `ع ق د B016` — إحاطة الموضع وإطباقه
  - activated_by_or_with: ر ب ب
  - themes: household_community, protection_security
  - keywords: community, protection
- `ع ق د B017` — لجأ بعنقه
  - activated_by_or_with: ش ر ر, ع و ذ
  - themes: body, danger_harm, motion, protection_security
  - keywords: body, motion, protection, safety, vulnerability

### ح س د

- `ح س د B001` — تمنّي زوال النعمة عن المحسود
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح س د B002` — الغبطة بلا إزالة النعمة
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
