# v11 Activation Packet — S114:1-None

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_1: قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ
- verse_2: مَلِكِ ٱلنَّاسِ
- verse_3: إِلَٰهِ ٱلنَّاسِ
- verse_4: مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ
- verse_5: ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ
- verse_6: مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ق و ل → ع و ذ → ر ب ب → ن و س → م ل ك → ء ل ه → ش ر ر → و س و س → خ ن س → ص د ر → ج ن ن

## Branch inventory summary

- ق و ل: 17 branches (16 with Qnet bridge-theme nodes; 1 Furūq-only)
- ع و ذ: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ر ب ب: 17 branches (17 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن و س: 3 branches (3 with Qnet bridge-theme nodes; 0 Furūq-only)
- م ل ك: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء ل ه: 2 branches (2 with Qnet bridge-theme nodes; 0 Furūq-only)
- ش ر ر: 12 branches (12 with Qnet bridge-theme nodes; 0 Furūq-only)
- و س و س: 3 branches (3 with Qnet bridge-theme nodes; 0 Furūq-only)
- خ ن س: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص د ر: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- ج ن ن: 17 branches (16 with Qnet bridge-theme nodes; 1 Furūq-only)

## QAC-first root resolution audit

- ق و ل | qac_keys=قول | status=resolved | matches=root_001272
- ع و ذ | qac_keys=عوذ | status=resolved | matches=root_001059
- ر ب ب | qac_keys=ربب | status=resolved | matches=root_000532
- ن و س | qac_keys=نوس | status=resolved | matches=root_004965
- م ل ك | qac_keys=ملك | status=resolved | matches=root_001444
- ء ل ه | qac_keys=ءله | status=resolved | matches=root_000047
- ش ر ر | qac_keys=شرر | status=resolved | matches=root_000787
- و س و س | qac_keys=وسوس | status=resolved | matches=root_001651
- خ ن س | qac_keys=خنس | status=resolved | matches=root_000443
- ص د ر | qac_keys=صدر | status=resolved | matches=root_000849
- ج ن ن | qac_keys=جنن | status=resolved | matches=root_000266

## Top candidate bridges

- `ر ب ب B013` ↔ `م ل ك B007` | score_hint=19 | discovery_hint=18 | themes=habitat_ecology, provision_resource, water_hydrology | keywords=ecology, hydrology, resource | q2=—
- `ر ب ب B012` ↔ `ش ر ر B012` | score_hint=24 | discovery_hint=17 | themes=agriculture, habitat_ecology, physiology, plant_vegetation | keywords=agriculture, botany, ecology, life | q2=—
- `ع و ذ B005` ↔ `ش ر ر B006` | score_hint=19 | discovery_hint=17 | themes=anatomy, animal, ornament_beauty | keywords=anatomy, animal, ornament | q2=—
- `ر ب ب B011` ↔ `ص د ر B005` | score_hint=13 | discovery_hint=17 | themes=finance_debt, law | keywords=law, taxation | q2=—
- `ر ب ب B012` ↔ `ج ن ن B011` | score_hint=24 | discovery_hint=16 | themes=agriculture, geography_landscape, habitat_ecology, plant_vegetation | keywords=agriculture, botany, ecology, landscape | q2=—
- `ش ر ر B012` ↔ `ج ن ن B011` | score_hint=22 | discovery_hint=16 | themes=agriculture, habitat_ecology, plant_vegetation | keywords=agriculture, botany, ecology, nature | q2=—
- `ق و ل B008` ↔ `خ ن س B005` | score_hint=13 | discovery_hint=16 | themes=motion, recreation_sport | keywords=motion, sport | q2=—
- `ر ب ب B010` ↔ `ج ن ن B008` | score_hint=13 | discovery_hint=16 | themes=tools_equipment, weaponry | keywords=tool, weapon | q2=—
- `خ ن س B002` ↔ `ج ن ن B002` | score_hint=30 | discovery_hint=15 | themes=light_darkness, perception, sequence_cycle, sky_astronomy, time | keywords=astronomy, cosmos, cycle, time, visibility | q2=—
- `ع و ذ B003` ↔ `ر ب ب B005` | score_hint=20 | discovery_hint=15 | themes=hospitality_welfare, kinship, reproduction_birth, support_dependence | keywords=dependency, kinship, nursing | q2=—
- `ع و ذ B003` ↔ `ر ب ب B009` | score_hint=18 | discovery_hint=15 | themes=animal, life_stage_aging, reproduction_birth | keywords=animal, infancy, reproduction | q2=—
- `ش ر ر B010` ↔ `ج ن ن B014` | score_hint=14 | discovery_hint=15 | themes=growth_decay, life_stage_aging, physiology | keywords=development, life | q2=—
- `ق و ل B005` ↔ `ش ر ر B001` | score_hint=12 | discovery_hint=15 | themes=deception_corruption, ethics_morality, justice_judgment | keywords=ethics | q2=—
- `ر ب ب B001` ↔ `م ل ك B003` | score_hint=24 | discovery_hint=14 | themes=authority_governance, belief_revelation, force_power, hierarchy_status | keywords=governance, hierarchy, power, theology | q2=—
- `ق و ل B010` ↔ `ر ب ب B001` | score_hint=22 | discovery_hint=14 | themes=authority_governance, force_power, hierarchy_status | keywords=authority, governance, hierarchy, power | q2=—
- `ق و ل B012` ↔ `ج ن ن B010` | score_hint=22 | discovery_hint=14 | themes=cognition, concealment_disclosure, containment_access | keywords=cognition, interiority, psychology, secrecy | q2=—
- `ق و ل B010` ↔ `م ل ك B003` | score_hint=20 | discovery_hint=14 | themes=authority_governance, force_power, hierarchy_status, law | keywords=governance, hierarchy, power | q2=—
- `ر ب ب B006` ↔ `ش ر ر B002` | score_hint=18 | discovery_hint=14 | themes=agency_action, food_nutrition, stability_endurance | keywords=food, preparation, preservation | q2=—
- `م ل ك B002` ↔ `ص د ر B005` | score_hint=18 | discovery_hint=14 | themes=authority_governance, law, wealth_property | keywords=authority, law, property | q2=—
- `ش ر ر B009` ↔ `خ ن س B003` | score_hint=18 | discovery_hint=14 | themes=anatomy, animal, body | keywords=animal, body, face | q2=—
- `ر ب ب B012` ↔ `ج ن ن B003` | score_hint=16 | discovery_hint=14 | themes=agriculture, geography_landscape, habitat_ecology, plant_vegetation | keywords=agriculture, landscape | q2=—
- `ر ب ب B008` ↔ `ج ن ن B003` | score_hint=14 | discovery_hint=14 | themes=agriculture, habitat_ecology, reproduction_birth | keywords=agriculture, fertility | q2=—
- `ش ر ر B012` ↔ `ج ن ن B003` | score_hint=14 | discovery_hint=14 | themes=agriculture, habitat_ecology, plant_vegetation | keywords=agriculture, nature | q2=—
- `ر ب ب B002` ↔ `ج ن ن B011` | score_hint=12 | discovery_hint=14 | themes=agriculture, growth_decay | keywords=agriculture, growth | q2=—
- `ر ب ب B008` ↔ `ش ر ر B002` | score_hint=12 | discovery_hint=14 | themes=agriculture, weather_climate | keywords=agriculture, weather | q2=—
- `ر ب ب B012` ↔ `ش ر ر B002` | score_hint=12 | discovery_hint=14 | themes=agriculture, food_nutrition | keywords=agriculture, food | q2=—
- `ج ن ن B003` ↔ `ج ن ن B011` | score_hint=29 | discovery_hint=13 | themes=abundance_scarcity, agriculture, geography_landscape, habitat_ecology, plant_vegetation | keywords=abundance, agriculture, landscape, nature, vegetation | q2=—
- `ق و ل B012` ↔ `و س و س B001` | score_hint=22 | discovery_hint=13 | themes=cognition, concealment_disclosure, containment_access | keywords=cognition, interiority, psychology, secrecy | q2=—
- `و س و س B001` ↔ `ج ن ن B010` | score_hint=22 | discovery_hint=13 | themes=cognition, concealment_disclosure, containment_access | keywords=cognition, interiority, psychology, secrecy | q2=—
- `ق و ل B004` ↔ `م ل ك B003` | score_hint=18 | discovery_hint=13 | themes=authority_governance, hierarchy_status, politics_order | keywords=governance, hierarchy, politics | q2=—
- `ع و ذ B008` ↔ `ش ر ر B011` | score_hint=18 | discovery_hint=13 | themes=conflict, emotion, social_relations | keywords=conflict, emotion, sociality | q2=—
- `ر ب ب B013` ↔ `ج ن ن B011` | score_hint=18 | discovery_hint=13 | themes=abundance_scarcity, geography_landscape, habitat_ecology | keywords=abundance, ecology, nature | q2=—
- `م ل ك B008` ↔ `خ ن س B005` | score_hint=18 | discovery_hint=13 | themes=animal, motion, navigation_route | keywords=animal, locomotion, navigation | q2=—
- `ش ر ر B009` ↔ `ج ن ن B015` | score_hint=18 | discovery_hint=13 | themes=animal, danger_harm, wildlife | keywords=animal, insect, nuisance | q2=—
- `خ ن س B003` ↔ `ص د ر B001` | score_hint=18 | discovery_hint=13 | themes=anatomy, animal, body | keywords=anatomy, animal, body | q2=—
- `خ ن س B004` ↔ `ج ن ن B003` | score_hint=18 | discovery_hint=13 | themes=architecture_construction, geography_landscape, habitat_ecology | keywords=habitat, landscape, shelter | q2=—
- `ص د ر B001` ↔ `ج ن ن B016` | score_hint=18 | discovery_hint=13 | themes=anatomy, body, health_medicine | keywords=anatomy, body, medicine | q2=—
- `ق و ل B010` ↔ `ص د ر B005` | score_hint=16 | discovery_hint=13 | themes=authority_governance, law | keywords=authority, governance, law | q2=—
- `ر ب ب B001` ↔ `ص د ر B005` | score_hint=16 | discovery_hint=13 | themes=authority_governance, wealth_property | keywords=authority, governance, property | q2=—
- `ن و س B003` ↔ `ج ن ن B013` | score_hint=16 | discovery_hint=13 | themes=household_community, social_relations | keywords=collective, community, society | q2=—
- `م ل ك B008` ↔ `ج ن ن B015` | score_hint=16 | discovery_hint=13 | themes=animal, wildlife | keywords=animal, swarm, zoology | q2=—
- `ق و ل B002` ↔ `ص د ر B001` | score_hint=14 | discovery_hint=13 | themes=anatomy, body, physiology | keywords=anatomy, body | q2=—
- `خ ن س B003` ↔ `ج ن ن B016` | score_hint=14 | discovery_hint=13 | themes=anatomy, body, form_structure | keywords=anatomy, body | q2=—
- `ق و ل B002` ↔ `خ ن س B003` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ق و ل B002` ↔ `ج ن ن B016` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ق و ل B006` ↔ `ش ر ر B007` | score_hint=12 | discovery_hint=13 | themes=agency_action, identity_personhood | keywords=agency, identity | q2=—
- `ع و ذ B003` ↔ `ج ن ن B007` | score_hint=12 | discovery_hint=13 | themes=kinship, reproduction_birth | keywords=kinship, reproduction | q2=—
- `ر ب ب B007` ↔ `ج ن ن B002` | score_hint=12 | discovery_hint=13 | themes=time, weather_climate | keywords=time, weather | q2=—
- `ر ب ب B008` ↔ `ش ر ر B012` | score_hint=12 | discovery_hint=13 | themes=agriculture, habitat_ecology | keywords=agriculture, ecology | q2=—
- `ر ب ب B008` ↔ `ج ن ن B011` | score_hint=12 | discovery_hint=13 | themes=agriculture, habitat_ecology | keywords=agriculture, ecology | q2=—
- `خ ن س B004` ↔ `ج ن ن B017` | score_hint=12 | discovery_hint=13 | themes=architecture_construction, protection_security | keywords=refuge, shelter | q2=—
- `ص د ر B001` ↔ `ج ن ن B008` | score_hint=12 | discovery_hint=13 | themes=body, protection_security | keywords=body, protection | q2=—
- `ر ب ب B009` ↔ `ج ن ن B007` | score_hint=10 | discovery_hint=13 | themes=reproduction_birth | keywords=birth, reproduction | q2=—
- `ق و ل B002` ↔ `ج ن ن B007` | score_hint=8 | discovery_hint=13 | themes=body, physiology | keywords=body | q2=—
- `ر ب ب B006` ↔ `ش ر ر B005` | score_hint=8 | discovery_hint=13 | themes=food_nutrition, substance_texture | keywords=food | q2=—
- `ر ب ب B008` ↔ `ج ن ن B002` | score_hint=8 | discovery_hint=13 | themes=sky_astronomy, weather_climate | keywords=weather | q2=—
- `ش ر ر B010` ↔ `ج ن ن B007` | score_hint=8 | discovery_hint=13 | themes=growth_decay, physiology | keywords=development | q2=—
- `ق و ل B001` ↔ `ر ب ب B015` | score_hint=16 | discovery_hint=12 | themes=language_speech, rhetoric_discourse | keywords=discourse, linguistics, rhetoric | q2=—
- `ق و ل B004` ↔ `ر ب ب B001` | score_hint=16 | discovery_hint=12 | themes=authority_governance, hierarchy_status | keywords=authority, governance, hierarchy | q2=—
- `ق و ل B012` ↔ `ج ن ن B001` | score_hint=16 | discovery_hint=12 | themes=concealment_disclosure, containment_access | keywords=interiority, privacy, secrecy | q2=—
- `ر ب ب B014` ↔ `م ل ك B008` | score_hint=16 | discovery_hint=12 | themes=animal, household_community, husbandry, wildlife | keywords=pastoralism, zoology | q2=—
- `ر ب ب B017` ↔ `ص د ر B003` | score_hint=16 | discovery_hint=12 | themes=navigation_route, transport, travel, water_hydrology | keywords=travel, water | q2=—
- `م ل ك B006` ↔ `ص د ر B003` | score_hint=16 | discovery_hint=12 | themes=motion, navigation_route, place_location, travel | keywords=movement, travel | q2=—
- `ق و ل B003` ↔ `ش ر ر B011` | score_hint=14 | discovery_hint=12 | themes=communication, rhetoric_discourse, social_relations | keywords=communication, sociality | q2=—
- `ق و ل B010` ↔ `م ل ك B002` | score_hint=14 | discovery_hint=12 | themes=authority_governance, hierarchy_status, law | keywords=authority, law | q2=—
- `ق و ل B011` ↔ `ص د ر B004` | score_hint=14 | discovery_hint=12 | themes=grammar_expression, language_speech, reasoning_decision | keywords=grammar, language | q2=—
- `ق و ل B013` ↔ `م ل ك B009` | score_hint=14 | discovery_hint=12 | themes=belief_revelation, religion_worship, social_relations | keywords=religion, theology | q2=—
- `ر ب ب B001` ↔ `م ل ك B002` | score_hint=14 | discovery_hint=12 | themes=authority_governance, hierarchy_status, wealth_property | keywords=authority, property | q2=—
- `ر ب ب B007` ↔ `م ل ك B006` | score_hint=14 | discovery_hint=12 | themes=geography_landscape, motion, place_location | keywords=geography, movement | q2=—
- `ر ب ب B013` ↔ `ج ن ن B003` | score_hint=14 | discovery_hint=12 | themes=abundance_scarcity, geography_landscape, habitat_ecology | keywords=abundance, nature | q2=—
- `ر ب ب B017` ↔ `م ل ك B008` | score_hint=14 | discovery_hint=12 | themes=authority_governance, hierarchy_status, navigation_route | keywords=hierarchy, navigation | q2=—
- `ن و س B002` ↔ `م ل ك B008` | score_hint=14 | discovery_hint=12 | themes=animal, husbandry, motion | keywords=animal, movement | q2=—
- `م ل ك B006` ↔ `خ ن س B005` | score_hint=14 | discovery_hint=12 | themes=motion, navigation_route, travel | keywords=navigation, travel | q2=—
- `م ل ك B007` ↔ `ص د ر B003` | score_hint=14 | discovery_hint=12 | themes=place_location, travel, water_hydrology | keywords=settlement, travel | q2=—
- `م ل ك B008` ↔ `ص د ر B002` | score_hint=14 | discovery_hint=12 | themes=authority_governance, hierarchy_status, household_community | keywords=hierarchy, leadership | q2=—
- `ش ر ر B009` ↔ `ص د ر B001` | score_hint=14 | discovery_hint=12 | themes=anatomy, animal, body | keywords=animal, body | q2=—
- `ق و ل B002` ↔ `ء ل ه B002` | score_hint=12 | discovery_hint=12 | themes=grammar_expression, language_speech | keywords=language, speech | q2=—
- `ق و ل B002` ↔ `ش ر ر B011` | score_hint=12 | discovery_hint=12 | themes=communication, language_speech | keywords=communication, speech | q2=—
- `ق و ل B002` ↔ `ص د ر B004` | score_hint=12 | discovery_hint=12 | themes=grammar_expression, language_speech | keywords=expression, language | q2=—
- `ق و ل B004` ↔ `ر ب ب B017` | score_hint=12 | discovery_hint=12 | themes=authority_governance, hierarchy_status | keywords=authority, hierarchy | q2=—

## Per-root candidate activations

### ق و ل

- `ق و ل B001` — إخراج القول بالنطق
  - activated_by_or_with: ر ب ب
  - themes: language_speech, rhetoric_discourse
  - keywords: discourse, linguistics, rhetoric
- `ق و ل B002` — اللسان آلة القول
  - activated_by_or_with: ء ل ه, ج ن ن, خ ن س, ش ر ر, ص د ر
  - themes: anatomy, body, communication, grammar_expression, language_speech, physiology
  - keywords: anatomy, body, communication, expression, language, speech
- `ق و ل B003` — كثرة القول في صاحبه
  - activated_by_or_with: ش ر ر
  - themes: communication, rhetoric_discourse, social_relations
  - keywords: communication, sociality
- `ق و ل B004` — القيل صاحب القول النافذ
  - activated_by_or_with: ر ب ب, م ل ك
  - themes: authority_governance, hierarchy_status, politics_order
  - keywords: authority, governance, hierarchy, politics
- `ق و ل B005` — قول ما لم يكن أو نسبته
  - activated_by_or_with: ش ر ر
  - themes: deception_corruption, ethics_morality, justice_judgment
  - keywords: ethics
- `ق و ل B006` — اجترار القول إلى النفس
  - activated_by_or_with: ش ر ر
  - themes: agency_action, identity_personhood
  - keywords: agency, identity
- `ق و ل B007` — القول الفاشي بين الناس
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B008` — عود القال لضرب القلة
  - activated_by_or_with: خ ن س
  - themes: motion, recreation_sport
  - keywords: motion, sport
- `ق و ل B009` — المقاولة في الأمر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B010` — اقتالة الحكم على غيره
  - activated_by_or_with: ر ب ب, ص د ر, م ل ك
  - themes: authority_governance, force_power, hierarchy_status, law
  - keywords: authority, governance, hierarchy, law, power
- `ق و ل B011` — قول يجري مجرى الظن
  - activated_by_or_with: ص د ر
  - themes: grammar_expression, language_speech, reasoning_decision
  - keywords: grammar, language
- `ق و ل B012` — قول في النفس لم يظهر
  - activated_by_or_with: ج ن ن, و س و س
  - themes: cognition, concealment_disclosure, containment_access
  - keywords: cognition, interiority, privacy, psychology, secrecy
- `ق و ل B013` — القول اعتقاد ومذهب
  - activated_by_or_with: م ل ك
  - themes: belief_revelation, religion_worship, social_relations
  - keywords: religion, theology
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
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع و ذ B002` — الوقاية بعوذة أو تعويذ
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع و ذ B003` — الأنثى العائذ بعد الولادة
  - activated_by_or_with: ج ن ن, ر ب ب
  - themes: animal, hospitality_welfare, kinship, life_stage_aging, reproduction_birth, support_dependence
  - keywords: animal, dependency, infancy, kinship, nursing, reproduction
- `ع و ذ B004` — اللصوق والملازمة في كنف شيء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع و ذ B005` — معوذ الفرس في موضع القلادة
  - activated_by_or_with: ش ر ر
  - themes: anatomy, animal, ornament_beauty
  - keywords: anatomy, animal, ornament
- `ع و ذ B006` — الإفلات عوذا بتخويف دون تمام الفعل
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع و ذ B007` — تعاوذ القوم في الحرب وتواكلوا
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع و ذ B008` — التحامي كراهة من الشيء
  - activated_by_or_with: ش ر ر
  - themes: conflict, emotion, social_relations
  - keywords: conflict, emotion, sociality

### ر ب ب

- `ر ب ب B001` — ربوبية وملك وسيادة
  - activated_by_or_with: ص د ر, ق و ل, م ل ك
  - themes: authority_governance, belief_revelation, force_power, hierarchy_status, wealth_property
  - keywords: authority, governance, hierarchy, power, property, theology
- `ر ب ب B002` — إصلاح وتربية وإتمام
  - activated_by_or_with: ج ن ن
  - themes: agriculture, growth_decay
  - keywords: agriculture, growth
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
  - activated_by_or_with: ش ر ر
  - themes: agency_action, food_nutrition, stability_endurance, substance_texture
  - keywords: food, preparation, preservation
- `ر ب ب B007` — لزوم وإقامة ودوام
  - activated_by_or_with: ج ن ن, م ل ك
  - themes: geography_landscape, motion, place_location, time, weather_climate
  - keywords: geography, movement, time, weather
- `ر ب ب B008` — رباب السحاب
  - activated_by_or_with: ج ن ن, ش ر ر
  - themes: agriculture, habitat_ecology, reproduction_birth, sky_astronomy, weather_climate
  - keywords: agriculture, ecology, fertility, weather
- `ر ب ب B009` — شاة رُبّى وحداثة
  - activated_by_or_with: ج ن ن, ع و ذ
  - themes: animal, life_stage_aging, reproduction_birth
  - keywords: animal, birth, infancy, reproduction
- `ر ب ب B010` — ربابة تجمع القداح
  - activated_by_or_with: ج ن ن
  - themes: tools_equipment, weaponry
  - keywords: tool, weapon
- `ر ب ب B011` — ربابة عهد وميثاق
  - activated_by_or_with: ص د ر
  - themes: finance_debt, law
  - keywords: law, taxation
- `ر ب ب B012` — ربة نبات
  - activated_by_or_with: ج ن ن, ش ر ر
  - themes: agriculture, food_nutrition, geography_landscape, habitat_ecology, physiology, plant_vegetation
  - keywords: agriculture, botany, ecology, food, landscape, life
- `ر ب ب B013` — ماء رَبَب كثير
  - activated_by_or_with: ج ن ن, م ل ك
  - themes: abundance_scarcity, geography_landscape, habitat_ecology, provision_resource, water_hydrology
  - keywords: abundance, ecology, hydrology, nature, resource
- `ر ب ب B014` — رَبْرَب قطيع
  - activated_by_or_with: م ل ك
  - themes: animal, household_community, husbandry, wildlife
  - keywords: pastoralism, zoology
- `ر ب ب B015` — حرف رب وربما
  - activated_by_or_with: ق و ل
  - themes: language_speech, rhetoric_discourse
  - keywords: discourse, linguistics, rhetoric
- `ر ب ب B016` — رُبَى حاجة وعقدة ونعمة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B017` — رباني الملاحين
  - activated_by_or_with: ص د ر, ق و ل, م ل ك
  - themes: authority_governance, hierarchy_status, navigation_route, transport, travel, water_hydrology
  - keywords: authority, hierarchy, navigation, travel, water

### ن و س

- `ن و س B001` — تذبذب الشيء المتدلّي
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن و س B002` — سوق الإبل
  - activated_by_or_with: م ل ك
  - themes: animal, husbandry, motion
  - keywords: animal, movement
- `ن و س B003` — اسم الناس المختلف في أصله
  - activated_by_or_with: ج ن ن
  - themes: household_community, social_relations
  - keywords: collective, community, society

### م ل ك

- `م ل ك B001` — قوة الشيء وتماسكه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `م ل ك B002` — المِلْك والتصرف
  - activated_by_or_with: ر ب ب, ص د ر, ق و ل
  - themes: authority_governance, hierarchy_status, law, wealth_property
  - keywords: authority, law, property
- `م ل ك B003` — المُلك والسلطان
  - activated_by_or_with: ر ب ب, ق و ل
  - themes: authority_governance, belief_revelation, force_power, hierarchy_status, law, politics_order
  - keywords: governance, hierarchy, politics, power, theology
- `م ل ك B004` — الإملاك والتزويج
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `م ل ك B005` — مِلاك الأمر وعِماده
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `م ل ك B006` — مَلَك الطريق والوادي
  - activated_by_or_with: خ ن س, ر ب ب, ص د ر
  - themes: geography_landscape, motion, navigation_route, place_location, travel
  - keywords: geography, movement, navigation, travel
- `م ل ك B007` — الماء مَلَك الأمر
  - activated_by_or_with: ر ب ب, ص د ر
  - themes: habitat_ecology, place_location, provision_resource, travel, water_hydrology
  - keywords: ecology, hydrology, resource, settlement, travel
- `م ل ك B008` — المتقدم القائد في الحيوان
  - activated_by_or_with: ج ن ن, خ ن س, ر ب ب, ص د ر, ن و س
  - themes: animal, authority_governance, hierarchy_status, household_community, husbandry, motion, navigation_route, wildlife
  - keywords: animal, hierarchy, leadership, locomotion, movement, navigation, pastoralism, swarm, zoology
- `م ل ك B009` — المَلَك من الملائكة
  - activated_by_or_with: ق و ل
  - themes: belief_revelation, religion_worship, social_relations
  - keywords: religion, theology

### ء ل ه

- `ء ل ه B001` — التعبد والمعبود
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ء ل ه B002` — اسم الله في القسم والنداء
  - activated_by_or_with: ق و ل
  - themes: grammar_expression, language_speech
  - keywords: language, speech

### ش ر ر

- `ش ر ر B001` — الشَّرّ والسوء
  - activated_by_or_with: ق و ل
  - themes: deception_corruption, ethics_morality, justice_judgment
  - keywords: ethics
- `ش ر ر B002` — نشر الشيء في الشمس ليجف
  - activated_by_or_with: ر ب ب
  - themes: agency_action, agriculture, food_nutrition, stability_endurance, weather_climate
  - keywords: agriculture, food, preparation, preservation, weather
- `ش ر ر B003` — شَرَر النار المتطاير
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ش ر ر B004` — الشَّرْشَرَة تقطيع ونفض
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ش ر ر B005` — الشواء المتقاطر دسمه
  - activated_by_or_with: ر ب ب
  - themes: food_nutrition, substance_texture
  - keywords: food
- `ش ر ر B006` — الشراشر ذباذب وأثقال
  - activated_by_or_with: ع و ذ
  - themes: anatomy, animal, ornament_beauty
  - keywords: anatomy, animal, ornament
- `ش ر ر B007` — إلقاء الشراشر إلقاء النفس كلها
  - activated_by_or_with: ق و ل
  - themes: agency_action, identity_personhood
  - keywords: agency, identity
- `ش ر ر B008` — إظهار الشيء وإبرازه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ش ر ر B009` — الشَّرّان أذى كالبعوض
  - activated_by_or_with: ج ن ن, خ ن س, ص د ر
  - themes: anatomy, animal, body, danger_harm, wildlife
  - keywords: animal, body, face, insect, nuisance
- `ش ر ر B010` — شِرّة الشباب نشاط وحرص
  - activated_by_or_with: ج ن ن
  - themes: growth_decay, life_stage_aging, physiology
  - keywords: development, life
- `ش ر ر B011` — المشارة مخاصمة
  - activated_by_or_with: ع و ذ, ق و ل
  - themes: communication, conflict, emotion, language_speech, rhetoric_discourse, social_relations
  - keywords: communication, conflict, emotion, sociality, speech
- `ش ر ر B012` — الشِّرْشِر نبت
  - activated_by_or_with: ج ن ن, ر ب ب
  - themes: agriculture, habitat_ecology, physiology, plant_vegetation
  - keywords: agriculture, botany, ecology, life, nature

### و س و س

- `و س و س B001` — حديث النفس الخفي
  - activated_by_or_with: ج ن ن, ق و ل
  - themes: cognition, concealment_disclosure, containment_access
  - keywords: cognition, interiority, psychology, secrecy
- `و س و س B002` — صوت خفي
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `و س و س B003` — الوسواس الشيطان
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### خ ن س

- `خ ن س B001` — الانخناس إلى خفاء أو تأخر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ ن س B002` — الكواكب التي تخفى وترجع
  - activated_by_or_with: ج ن ن
  - themes: light_darkness, perception, sequence_cycle, sky_astronomy, time
  - keywords: astronomy, cosmos, cycle, time, visibility
- `خ ن س B003` — الخَنَس في الأنف
  - activated_by_or_with: ج ن ن, ش ر ر, ص د ر, ق و ل
  - themes: anatomy, animal, body, form_structure
  - keywords: anatomy, animal, body, face
- `خ ن س B004` — مأوى الظباء أو الظباء
  - activated_by_or_with: ج ن ن
  - themes: architecture_construction, geography_landscape, habitat_ecology, protection_security
  - keywords: habitat, landscape, refuge, shelter
- `خ ن س B005` — عدول الفرس في حضره
  - activated_by_or_with: ق و ل, م ل ك
  - themes: animal, motion, navigation_route, recreation_sport, travel
  - keywords: animal, locomotion, motion, navigation, sport, travel

### ص د ر

- `ص د ر B001` — الصدر الجارحة وما يتصل بها
  - activated_by_or_with: ج ن ن, خ ن س, ش ر ر, ق و ل
  - themes: anatomy, animal, body, health_medicine, physiology, protection_security
  - keywords: anatomy, animal, body, medicine, protection
- `ص د ر B002` — المقدّم والأعلى والأول
  - activated_by_or_with: م ل ك
  - themes: authority_governance, hierarchy_status, household_community
  - keywords: hierarchy, leadership
- `ص د ر B003` — الصُّدور عن المورد
  - activated_by_or_with: ر ب ب, م ل ك
  - themes: motion, navigation_route, place_location, transport, travel, water_hydrology
  - keywords: movement, settlement, travel, water
- `ص د ر B004` — الأصل الذي تصدر عنه الأفعال
  - activated_by_or_with: ق و ل
  - themes: grammar_expression, language_speech, reasoning_decision
  - keywords: expression, grammar, language
- `ص د ر B005` — المصادرة على مال
  - activated_by_or_with: ر ب ب, ق و ل, م ل ك
  - themes: authority_governance, finance_debt, law, wealth_property
  - keywords: authority, governance, law, property, taxation
- `ص د ر B006` — الطائفة من الشيء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ج ن ن

- `ج ن ن B001` — الستر والاستتار
  - activated_by_or_with: ق و ل
  - themes: concealment_disclosure, containment_access
  - keywords: interiority, privacy, secrecy
- `ج ن ن B002` — غشيان الليل
  - activated_by_or_with: خ ن س, ر ب ب
  - themes: light_darkness, perception, sequence_cycle, sky_astronomy, time, weather_climate
  - keywords: astronomy, cosmos, cycle, time, visibility, weather
- `ج ن ن B003` — البستان المستور بالشجر
  - activated_by_or_with: خ ن س, ر ب ب, ش ر ر
  - themes: abundance_scarcity, agriculture, architecture_construction, geography_landscape, habitat_ecology, plant_vegetation, reproduction_birth
  - keywords: abundance, agriculture, fertility, habitat, landscape, nature, shelter, vegetation
- `ج ن ن B004` — الجنة الأخروية
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ج ن ن B005` — الجن المستترون
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج ن ن B006` — ستر العقل بالجنون
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج ن ن B007` — الجنين المستور في البطن
  - activated_by_or_with: ر ب ب, ش ر ر, ع و ذ, ق و ل
  - themes: body, growth_decay, kinship, physiology, reproduction_birth
  - keywords: birth, body, development, kinship, reproduction
- `ج ن ن B008` — الجُنّة الواقية
  - activated_by_or_with: ر ب ب, ص د ر
  - themes: body, protection_security, tools_equipment, weaponry
  - keywords: body, protection, tool, weapon
- `ج ن ن B009` — مواراة الميت
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج ن ن B010` — الجنان المستور في الصدر
  - activated_by_or_with: ق و ل, و س و س
  - themes: cognition, concealment_disclosure, containment_access
  - keywords: cognition, interiority, psychology, secrecy
- `ج ن ن B011` — التفاف النبات واندفاعه
  - activated_by_or_with: ر ب ب, ش ر ر
  - themes: abundance_scarcity, agriculture, geography_landscape, growth_decay, habitat_ecology, plant_vegetation
  - keywords: abundance, agriculture, botany, ecology, growth, landscape, nature, vegetation
- `ج ن ن B012` — الجان حية
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج ن ن B013` — سواد الناس وجماعتهم
  - activated_by_or_with: ن و س
  - themes: household_community, social_relations
  - keywords: collective, community, society
- `ج ن ن B014` — جن الشيء في بدايته
  - activated_by_or_with: ش ر ر
  - themes: growth_decay, life_stage_aging, physiology
  - keywords: development, life
- `ج ن ن B015` — جن الذباب وصوت الخازباز
  - activated_by_or_with: ش ر ر, م ل ك
  - themes: animal, danger_harm, wildlife
  - keywords: animal, insect, nuisance, swarm, zoology
- `ج ن ن B016` — الجناجن عظام الصدر
  - activated_by_or_with: خ ن س, ص د ر, ق و ل
  - themes: anatomy, body, form_structure, health_medicine
  - keywords: anatomy, body, medicine
- `ج ن ن B017` — المَجَنَّة موضع الاستتار
  - activated_by_or_with: خ ن س
  - themes: architecture_construction, protection_security
  - keywords: refuge, shelter

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
