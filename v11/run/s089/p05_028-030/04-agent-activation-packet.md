# v11 Activation Packet — S89:28-30

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_28: ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- verse_29: فَٱدْخُلِى فِى عِبَٰدِى
- verse_30: وَٱدْخُلِى جَنَّتِى

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ر ج ع → ر ب ب → ر ض و → د خ ل → ع ب د → ج ن ن

## Branch inventory summary

- ر ج ع: 15 branches (14 with Qnet bridge-theme nodes; 1 Furūq-only)
- ر ب ب: 17 branches (17 with Qnet bridge-theme nodes; 0 Furūq-only)
- ر ض و: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- د خ ل: 10 branches (10 with Qnet bridge-theme nodes; 0 Furūq-only)
- ع ب د: 12 branches (11 with Qnet bridge-theme nodes; 1 Furūq-only)
- ج ن ن: 17 branches (16 with Qnet bridge-theme nodes; 1 Furūq-only)

## QAC-first root resolution audit

- ر ج ع | qac_keys=رجع | status=resolved | matches=root_000544
- ر ب ب | qac_keys=ربب | status=resolved | matches=root_000532
- ر ض و | qac_keys=رضو | status=resolved | matches=root_000569
- د خ ل | qac_keys=دخل | status=resolved | matches=root_000464
- ع ب د | qac_keys=عبد | status=resolved | matches=root_000973
- ج ن ن | qac_keys=جنن | status=resolved | matches=root_000266

## Top candidate bridges

- `ر ج ع B004` ↔ `د خ ل B002` | score_hint=27 | discovery_hint=19 | themes=household_community, kinship, marriage_genealogy, sexuality, social_relations | keywords=household, kinship, sexuality, union | q2=—
- `د خ ل B003` ↔ `ج ن ن B001` | score_hint=26 | discovery_hint=13 | themes=concealment_disclosure, containment_access, textile_clothing | keywords=clothing, concealment, interiority, privacy, secrecy | q2=—
- `ر ج ع B004` ↔ `ر ب ب B005` | score_hint=24 | discovery_hint=14 | themes=authority_governance, family, household_community, kinship | keywords=family, guardianship, household, kinship | q2=—
- `ر ج ع B006` ↔ `ر ب ب B008` | score_hint=24 | discovery_hint=16 | themes=habitat_ecology, reproduction_birth, water_hydrology, weather_climate | keywords=ecology, fertility, water, weather | q2=—
- `ر ب ب B012` ↔ `ج ن ن B011` | score_hint=24 | discovery_hint=16 | themes=agriculture, geography_landscape, habitat_ecology, plant_vegetation | keywords=agriculture, botany, ecology, landscape | q2=—
- `ر ج ع B008` ↔ `ع ب د B005` | score_hint=20 | discovery_hint=13 | themes=animal, stability_endurance, transport, travel | keywords=animal, transport, travel | q2=—
- `ر ج ع B014` ↔ `ع ب د B011` | score_hint=20 | discovery_hint=14 | themes=animal, physiology, stability_endurance, travel | keywords=animal, endurance, travel | q2=—
- `ر ج ع B008` ↔ `ع ب د B011` | score_hint=18 | discovery_hint=13 | themes=animal, stability_endurance, travel | keywords=animal, endurance, travel | q2=—
- `ر ج ع B012` ↔ `ر ب ب B007` | score_hint=18 | discovery_hint=13 | themes=animal, geography_landscape, motion | keywords=animal, geography, movement | q2=—
- `ر ج ع B014` ↔ `ع ب د B007` | score_hint=18 | discovery_hint=14 | themes=animal, physiology, stability_endurance | keywords=animal, endurance, vitality | q2=—
- `ر ج ع B015` ↔ `د خ ل B010` | score_hint=18 | discovery_hint=14 | themes=craft, food_nutrition, material | keywords=craft, food, material | q2=—
- `ر ب ب B001` ↔ `ع ب د B003` | score_hint=18 | discovery_hint=12 | themes=authority_governance, belief_revelation, religion_worship | keywords=authority, devotion, theology | q2=—
- `ر ب ب B013` ↔ `ج ن ن B011` | score_hint=18 | discovery_hint=13 | themes=abundance_scarcity, geography_landscape, habitat_ecology | keywords=abundance, ecology, nature | q2=—
- `د خ ل B003` ↔ `ج ن ن B010` | score_hint=18 | discovery_hint=13 | themes=cognition, concealment_disclosure, containment_access | keywords=cognition, interiority, secrecy | q2=—
- `د خ ل B009` ↔ `ج ن ن B003` | score_hint=18 | discovery_hint=14 | themes=architecture_construction, habitat_ecology, plant_vegetation | keywords=habitat, shelter, vegetation | q2=—
- `ر ج ع B011` ↔ `د خ ل B006` | score_hint=17 | discovery_hint=19 | themes=commerce_exchange, economy, finance_debt, wealth_property | keywords=economy, property | q2=—
- `ر ج ع B008` ↔ `ر ب ب B007` | score_hint=16 | discovery_hint=13 | themes=animal, motion | keywords=animal, motion, movement | q2=—
- `ر ج ع B008` ↔ `ع ب د B009` | score_hint=16 | discovery_hint=13 | themes=motion, travel | keywords=motion, movement, travel | q2=—
- `ر ج ع B013` ↔ `ر ب ب B009` | score_hint=16 | discovery_hint=14 | themes=animal, reproduction_birth | keywords=animal, birth, reproduction | q2=—
- `ر ج ع B013` ↔ `ج ن ن B007` | score_hint=16 | discovery_hint=15 | themes=physiology, reproduction_birth | keywords=biology, birth, reproduction | q2=—
- `ر ب ب B007` ↔ `ع ب د B009` | score_hint=16 | discovery_hint=13 | themes=motion, time | keywords=motion, movement, time | q2=—
- `ر ب ب B012` ↔ `ج ن ن B003` | score_hint=16 | discovery_hint=14 | themes=agriculture, geography_landscape, habitat_ecology, plant_vegetation | keywords=agriculture, landscape | q2=—
- `ر ب ب B014` ↔ `د خ ل B007` | score_hint=16 | discovery_hint=12 | themes=animal, household_community, husbandry, livestock | keywords=livestock, pastoralism | q2=—
- `ر ج ع B001` ↔ `د خ ل B001` | score_hint=14 | discovery_hint=10 | themes=agency_action, change_transition, motion | keywords=causation, motion | q2=—
- `ر ج ع B006` ↔ `ج ن ن B003` | score_hint=14 | discovery_hint=13 | themes=geography_landscape, habitat_ecology, reproduction_birth | keywords=fertility, landscape | q2=—
- `ر ج ع B008` ↔ `ع ب د B007` | score_hint=14 | discovery_hint=13 | themes=animal, force_power, stability_endurance | keywords=animal, endurance | q2=—
- `ر ج ع B012` ↔ `د خ ل B009` | score_hint=14 | discovery_hint=12 | themes=animal, habitat_ecology, motion | keywords=animal, movement | q2=—
- `ر ج ع B012` ↔ `ع ب د B010` | score_hint=14 | discovery_hint=12 | themes=geography_landscape, motion, navigation_route | keywords=geography, movement | q2=—
- `ر ج ع B013` ↔ `ع ب د B011` | score_hint=14 | discovery_hint=13 | themes=animal, loss_absence, physiology | keywords=animal, loss | q2=—
- `ر ج ع B014` ↔ `ع ب د B005` | score_hint=14 | discovery_hint=12 | themes=animal, stability_endurance, travel | keywords=animal, travel | q2=—
- `ر ج ع B015` ↔ `ع ب د B007` | score_hint=14 | discovery_hint=13 | themes=material, physiology, textile_clothing | keywords=material, textile | q2=—
- `ر ب ب B001` ↔ `ع ب د B004` | score_hint=14 | discovery_hint=13 | themes=force_power, hierarchy_status, support_dependence | keywords=hierarchy, power | q2=—
- `ر ب ب B001` ↔ `ع ب د B006` | score_hint=14 | discovery_hint=11 | themes=authority_governance, hierarchy_status, religion_worship | keywords=authority, hierarchy | q2=—
- `ر ب ب B005` ↔ `د خ ل B002` | score_hint=14 | discovery_hint=13 | themes=household_community, kinship, reproduction_birth | keywords=household, kinship | q2=—
- `ر ب ب B008` ↔ `ج ن ن B003` | score_hint=14 | discovery_hint=14 | themes=agriculture, habitat_ecology, reproduction_birth | keywords=agriculture, fertility | q2=—
- `ر ب ب B009` ↔ `د خ ل B007` | score_hint=14 | discovery_hint=12 | themes=animal, household_community, livestock | keywords=animal, livestock | q2=—
- `ر ب ب B013` ↔ `ج ن ن B003` | score_hint=14 | discovery_hint=12 | themes=abundance_scarcity, geography_landscape, habitat_ecology | keywords=abundance, nature | q2=—
- `ر ب ب B016` ↔ `ر ض و B001` | score_hint=14 | discovery_hint=11 | themes=ethics_morality, obligation_contract, social_relations | keywords=ethics, relation | q2=—
- `ر ب ب B017` ↔ `ع ب د B006` | score_hint=14 | discovery_hint=12 | themes=authority_governance, hierarchy_status, labor_work | keywords=authority, hierarchy | q2=—
- `ر ض و B005` ↔ `ع ب د B004` | score_hint=14 | discovery_hint=13 | themes=force_power, hierarchy_status, violence_warfare | keywords=hierarchy, power | q2=—
- `ر ض و B006` ↔ `ع ب د B003` | score_hint=14 | discovery_hint=13 | themes=authority_governance, religion_worship, trust_loyalty | keywords=devotion, loyalty | q2=—
- `ر ج ع B005` ↔ `ر ب ب B015` | score_hint=13 | discovery_hint=16 | themes=language_speech, rhetoric_discourse | keywords=discourse, rhetoric | q2=—
- `ر ب ب B010` ↔ `ج ن ن B008` | score_hint=13 | discovery_hint=16 | themes=tools_equipment, weaponry | keywords=tool, weapon | q2=—
- `ر ب ب B012` ↔ `د خ ل B008` | score_hint=13 | discovery_hint=17 | themes=plant_vegetation, visual_appearance | keywords=botany, color | q2=—
- `د خ ل B008` ↔ `ج ن ن B016` | score_hint=13 | discovery_hint=16 | themes=anatomy, form_structure | keywords=anatomy, structure | q2=—
- `ر ج ع B003` ↔ `ر ب ب B003` | score_hint=12 | discovery_hint=12 | themes=ethics_morality, religion_worship | keywords=ethics, religion | q2=—
- `ر ج ع B006` ↔ `ر ب ب B012` | score_hint=12 | discovery_hint=12 | themes=geography_landscape, habitat_ecology | keywords=ecology, landscape | q2=—
- `ر ج ع B006` ↔ `ج ن ن B002` | score_hint=12 | discovery_hint=13 | themes=sequence_cycle, weather_climate | keywords=cycle, weather | q2=—
- `ر ج ع B006` ↔ `ج ن ن B011` | score_hint=12 | discovery_hint=12 | themes=geography_landscape, habitat_ecology | keywords=ecology, landscape | q2=—
- `ر ج ع B008` ↔ `ر ب ب B017` | score_hint=12 | discovery_hint=12 | themes=transport, travel | keywords=transport, travel | q2=—
- `ر ج ع B008` ↔ `د خ ل B009` | score_hint=12 | discovery_hint=12 | themes=animal, motion | keywords=animal, movement | q2=—
- `ر ج ع B011` ↔ `ع ب د B001` | score_hint=12 | discovery_hint=13 | themes=commerce_exchange, wealth_property | keywords=commerce, property | q2=—
- `ر ج ع B012` ↔ `ر ب ب B013` | score_hint=12 | discovery_hint=12 | themes=geography_landscape, habitat_ecology | keywords=ecology, geography | q2=—
- `ر ج ع B013` ↔ `د خ ل B007` | score_hint=12 | discovery_hint=12 | themes=animal, husbandry | keywords=animal, husbandry | q2=—
- `ر ج ع B014` ↔ `ر ب ب B009` | score_hint=12 | discovery_hint=12 | themes=animal, livestock | keywords=animal, livestock | q2=—
- `ر ج ع B014` ↔ `د خ ل B007` | score_hint=12 | discovery_hint=12 | themes=animal, livestock | keywords=animal, livestock | q2=—
- `ر ج ع B015` ↔ `ر ب ب B006` | score_hint=12 | discovery_hint=13 | themes=food_nutrition, material | keywords=food, material | q2=—
- `ر ج ع B015` ↔ `ع ب د B005` | score_hint=12 | discovery_hint=12 | themes=craft, material | keywords=craft, material | q2=—
- `ر ب ب B001` ↔ `ر ض و B005` | score_hint=12 | discovery_hint=12 | themes=force_power, hierarchy_status | keywords=hierarchy, power | q2=—
- `ر ب ب B001` ↔ `ع ب د B001` | score_hint=12 | discovery_hint=11 | themes=hierarchy_status, wealth_property | keywords=hierarchy, property | q2=—
- `ر ب ب B002` ↔ `د خ ل B010` | score_hint=12 | discovery_hint=13 | themes=agriculture, craft | keywords=agriculture, craft | q2=—
- `ر ب ب B002` ↔ `ع ب د B005` | score_hint=12 | discovery_hint=12 | themes=craft, stability_endurance | keywords=craft, maintenance | q2=—
- `ر ب ب B002` ↔ `ج ن ن B011` | score_hint=12 | discovery_hint=14 | themes=agriculture, growth_decay | keywords=agriculture, growth | q2=—
- `ر ب ب B004` ↔ `د خ ل B005` | score_hint=12 | discovery_hint=12 | themes=kinship, social_relations | keywords=kinship, society | q2=—
- `ر ب ب B004` ↔ `ج ن ن B013` | score_hint=12 | discovery_hint=12 | themes=household_community, social_relations | keywords=demography, society | q2=—
- `ر ب ب B006` ↔ `د خ ل B010` | score_hint=12 | discovery_hint=13 | themes=food_nutrition, material | keywords=food, material | q2=—
- `ر ب ب B007` ↔ `د خ ل B009` | score_hint=12 | discovery_hint=12 | themes=animal, motion | keywords=animal, movement | q2=—
- `ر ب ب B007` ↔ `ع ب د B010` | score_hint=12 | discovery_hint=12 | themes=geography_landscape, motion | keywords=geography, movement | q2=—
- `ر ب ب B007` ↔ `ج ن ن B002` | score_hint=12 | discovery_hint=13 | themes=time, weather_climate | keywords=time, weather | q2=—
- `ر ب ب B008` ↔ `ج ن ن B011` | score_hint=12 | discovery_hint=13 | themes=agriculture, habitat_ecology | keywords=agriculture, ecology | q2=—
- `ر ب ب B009` ↔ `د خ ل B002` | score_hint=12 | discovery_hint=13 | themes=household_community, reproduction_birth | keywords=household, reproduction | q2=—
- `ر ب ب B011` ↔ `ر ض و B003` | score_hint=12 | discovery_hint=12 | themes=household_community, obligation_contract | keywords=community, contract | q2=—
- `ر ب ب B012` ↔ `د خ ل B010` | score_hint=12 | discovery_hint=14 | themes=agriculture, food_nutrition | keywords=agriculture, food | q2=—
- `ر ب ب B017` ↔ `ع ب د B005` | score_hint=12 | discovery_hint=12 | themes=transport, travel | keywords=transport, travel | q2=—
- `ر ض و B001` ↔ `ع ب د B008` | score_hint=12 | discovery_hint=11 | themes=desire_appetite, emotion | keywords=affect, emotion | q2=—
- `ر ض و B003` ↔ `ج ن ن B013` | score_hint=12 | discovery_hint=12 | themes=household_community, social_relations | keywords=community, society | q2=—
- `د خ ل B001` ↔ `ع ب د B009` | score_hint=12 | discovery_hint=11 | themes=agency_action, motion | keywords=motion, movement | q2=—
- `د خ ل B001` ↔ `ع ب د B010` | score_hint=12 | discovery_hint=11 | themes=motion, space | keywords=movement, space | q2=—
- `د خ ل B002` ↔ `ج ن ن B007` | score_hint=12 | discovery_hint=13 | themes=kinship, reproduction_birth | keywords=kinship, reproduction | q2=—
- `د خ ل B009` ↔ `ج ن ن B012` | score_hint=12 | discovery_hint=12 | themes=animal, wildlife | keywords=animal, wildlife | q2=—

## Per-root candidate activations

### ر ج ع

- `ر ج ع B001` — العود والرد إلى ما كان
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ع ب د
  - themes: agency_action, change_transition, health_medicine, motion, sequence_cycle, stability_endurance
  - keywords: causation, cycle, motion, recovery
- `ر ج ع B002` — المعاد والمرجع إلى الله
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ر ج ع B003` — الرجوع عن الذنب أو الأمر
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ض و, ع ب د
  - themes: change_transition, ethics_morality, justice_judgment, purity_cleansing, religion_worship
  - keywords: ethics, forgiveness, religion
- `ر ج ع B004` — رجعة المرأة في النكاح والأهل
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ض و, ع ب د
  - themes: authority_governance, boundary, family, gender, household_community, kinship, law, marriage_genealogy, sexuality, social_relations
  - keywords: family, gender, guardianship, household, kinship, law, sexuality, union
- `ر ج ع B005` — رد الجواب والكلام
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ض و
  - themes: communication, language_speech, reasoning_decision, rhetoric_discourse, social_relations
  - keywords: communication, discourse, rhetoric
- `ر ج ع B006` — المطر والماء الراجع
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ض و, ع ب د
  - themes: change_transition, geography_landscape, habitat_ecology, reproduction_birth, sequence_cycle, water_hydrology, weather_climate
  - keywords: cycle, ecology, fertility, landscape, water, weather
- `ر ج ع B007` — ترديد الصوت والنداء
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ض و, ع ب د
  - themes: agency_action, communication, perception, religion_worship, sequence_cycle, weather_climate
  - keywords: communication, performance, sound
- `ر ج ع B008` — رجع الدابة في السير
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ض و, ع ب د
  - themes: animal, force_power, motion, stability_endurance, transport, travel
  - keywords: animal, endurance, motion, movement, transport, travel
- `ر ج ع B009` — خطوط الوشم والنقش المعادة
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ض و, ع ب د
  - themes: body, craft, form_structure, ornament_beauty
  - keywords: body, craft
- `ر ج ع B010` — إرجاع اليد إلى السلاح
  - activated_by_or_with: ج ن ن, ر ب ب, ر ض و, ع ب د
  - themes: capacity_ability, communication, protection_security, violence_warfare, weaponry
  - keywords: violence, warfare
- `ر ج ع B011` — ارتجاع البيع والبدل
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ض و, ع ب د
  - themes: commerce_exchange, economy, finance_debt, justice_judgment, obligation_contract, physiology, value_quality, wealth_property
  - keywords: commerce, contract, economy, property
- `ر ج ع B012` — رجوع الطير بعد القطاع
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ض و, ع ب د
  - themes: animal, calendar_season, geography_landscape, habitat_ecology, motion, navigation_route, sequence_cycle
  - keywords: animal, cycle, ecology, geography, movement, navigation
- `ر ج ع B013` — راجع الناقة وحملها
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ع ب د
  - themes: animal, husbandry, loss_absence, physiology, proof_uncertainty, reproduction_birth
  - keywords: animal, biology, birth, fertility, husbandry, loss, reproduction
- `ر ج ع B014` — الرجيع من الدواب واسترداد الحال
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ع ب د
  - themes: animal, health_medicine, livestock, physiology, stability_endurance, travel, value_quality
  - keywords: animal, endurance, livestock, recovery, travel, vitality
- `ر ج ع B015` — الرجيع مردودا أو معادا
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ض و, ع ب د
  - themes: change_transition, craft, food_nutrition, growth_decay, loss_absence, material, physiology, textile_clothing
  - keywords: craft, food, material, textile

### ر ب ب

- `ر ب ب B001` — ربوبية وملك وسيادة
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: authority_governance, belief_revelation, force_power, hierarchy_status, religion_worship, support_dependence, wealth_property
  - keywords: authority, devotion, hierarchy, power, property, theology
- `ر ب ب B002` — إصلاح وتربية وإتمام
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: agriculture, authority_governance, belief_revelation, craft, family, growth_decay, knowledge_learning, life_stage_aging, stability_endurance
  - keywords: agriculture, craft, education, growth, maintenance
- `ر ب ب B003` — علم رباني
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: cognition, ethics_morality, knowledge_learning, religion_worship
  - keywords: education, ethics, religion
- `ر ب ب B004` — ربة وجماعات كثيرة
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: household_community, kinship, quantity_number, social_relations, violence_warfare
  - keywords: collectivity, demography, kinship, society
- `ر ب ب B005` — ربيب وربيبة ورابة
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: authority_governance, family, hospitality_welfare, household_community, kinship, reproduction_birth, support_dependence
  - keywords: dependency, family, guardianship, household, kinship
- `ر ب ب B006` — رُبّ خاثر وإصلاح به
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ع ب د
  - themes: agency_action, food_nutrition, health_medicine, material, stability_endurance, substance_texture
  - keywords: food, leather, material, medicine
- `ر ب ب B007` — لزوم وإقامة ودوام
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: animal, geography_landscape, motion, place_location, time, weather_climate
  - keywords: animal, geography, motion, movement, temporality, time, weather
- `ر ب ب B008` — رباب السحاب
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع
  - themes: agriculture, habitat_ecology, reproduction_birth, sky_astronomy, water_hydrology, weather_climate
  - keywords: agriculture, ecology, fertility, water, weather
- `ر ب ب B009` — شاة رُبّى وحداثة
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: animal, food_nutrition, household_community, life_stage_aging, livestock, reproduction_birth, time
  - keywords: animal, birth, household, livestock, reproduction, temporality, time
- `ر ب ب B010` — ربابة تجمع القداح
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: abundance_scarcity, belief_revelation, material, proof_uncertainty, ritual, storage_vessels, tools_equipment, weaponry
  - keywords: leather, ritual, storage, tool, weapon
- `ر ب ب B011` — ربابة عهد وميثاق
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: finance_debt, household_community, law, obligation_contract, politics_order, protection_security, trust_loyalty
  - keywords: community, contract, diplomacy, law, protection, trust
- `ر ب ب B012` — ربة نبات
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: agriculture, food_nutrition, geography_landscape, habitat_ecology, physiology, plant_vegetation, visual_appearance
  - keywords: agriculture, botany, color, ecology, food, landscape, life
- `ر ب ب B013` — ماء رَبَب كثير
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: abundance_scarcity, geography_landscape, habitat_ecology, provision_resource, purity_cleansing, water_hydrology
  - keywords: abundance, ecology, geography, nature, sustenance
- `ر ب ب B014` — رَبْرَب قطيع
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: animal, habitat_ecology, household_community, husbandry, livestock, quantity_number, wildlife
  - keywords: collectivity, ecology, livestock, pastoralism, plurality, zoology
- `ر ب ب B015` — حرف رب وربما
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: form_structure, language_speech, quantity_number, rhetoric_discourse
  - keywords: discourse, morphology, rhetoric
- `ر ب ب B016` — رُبَى حاجة وعقدة ونعمة
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: control_restraint, ethics_morality, hospitality_welfare, material, obligation_contract, social_relations, support_dependence
  - keywords: dependency, ethics, material, relation
- `ر ب ب B017` — رباني الملاحين
  - activated_by_or_with: د خ ل, ر ج ع, ر ض و, ع ب د
  - themes: authority_governance, hierarchy_status, labor_work, navigation_route, transport, travel, water_hydrology
  - keywords: authority, hierarchy, navigation, transport, travel, water

### ر ض و

- `ر ض و B001` — الرضا خلاف السخط
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: authority_governance, desire_appetite, emotion, ethics_morality, justice_judgment, obligation_contract, social_relations
  - keywords: affect, approval, emotion, ethics, relation
- `ر ض و B002` — الرضوان والمرضاة اسم للرضا الكثير أو المطلوب
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: abundance_scarcity, authority_governance, belief_revelation, desire_appetite, hospitality_welfare, justice_judgment, religion_worship
  - keywords: abundance, approval, devotion
- `ر ض و B003` — المراضاة والتراضي رضا متبادل
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: commerce_exchange, household_community, obligation_contract, rhetoric_discourse, social_relations
  - keywords: community, contract, reconciliation, society
- `ر ض و B004` — الإرضاء طلب رضا الغير وإزالة سخطه
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: communication, conflict, craft, emotion, ethics_morality, politics_order, rhetoric_discourse, social_relations
  - keywords: conflict, diplomacy, emotion, forgiveness, reconciliation
- `ر ض و B005` — راضاني فرضوته غلبة في ذلك
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: capacity_ability, conflict, force_power, hierarchy_status, violence_warfare
  - keywords: conflict, hierarchy, power
- `ر ض و B006` — الرضي صفة للمطيع أو المحب أو الضامن
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: authority_governance, emotion, ethics_morality, law, obligation_contract, religion_worship, trust_loyalty
  - keywords: devotion, ethics, law, loyalty
- `ر ض و B007` — رضوى ورضيا أعلام من المادة
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: gender, geography_landscape, identity_personhood, naming_classification, place_location
  - keywords: gender, geography, identity, place

### د خ ل

- `د خ ل B001` — الولوج إلى داخل
  - activated_by_or_with: ج ن ن, ر ب ب, ر ج ع, ر ض و, ع ب د
  - themes: agency_action, boundary, change_transition, containment_access, motion, social_relations, space
  - keywords: boundary, causation, motion, movement, space, transition
- `د خ ل B002` — الإفضاء الزوجي
  - activated_by_or_with: ج ن ن, ر ب ب, ر ج ع, ر ض و, ع ب د
  - themes: containment_access, household_community, kinship, marriage_genealogy, reproduction_birth, sexuality, social_relations
  - keywords: household, kinship, privacy, reproduction, sexuality, union
- `د خ ل B003` — الباطن والسريرة
  - activated_by_or_with: ج ن ن, ر ب ب, ر ج ع, ع ب د
  - themes: cognition, concealment_disclosure, containment_access, knowledge_learning, textile_clothing
  - keywords: clothing, cognition, concealment, interiority, privacy, secrecy
- `د خ ل B004` — فساد مستبطن
  - activated_by_or_with: ج ن ن, ر ب ب, ر ج ع, ر ض و, ع ب د
  - themes: conflict, disease_injury, ethics_morality, proof_uncertainty, trust_loyalty, value_quality
  - keywords: conflict, trust
- `د خ ل B005` — دخيل يخالط القوم أو الأمر
  - activated_by_or_with: ج ن ن, ر ب ب, ر ج ع, ر ض و, ع ب د
  - themes: boundary, containment_access, control_restraint, identity_personhood, kinship, marriage_genealogy, social_relations
  - keywords: boundary, identity, kinship, society
- `د خ ل B006` — ما يدخل من كسب
  - activated_by_or_with: ر ب ب, ر ج ع, ر ض و, ع ب د
  - themes: commerce_exchange, economy, finance_debt, labor_work, provision_resource, wealth_property
  - keywords: economy, property
- `د خ ل B007` — إدخال الإبل في الشرب مرة أخرى
  - activated_by_or_with: ج ن ن, ر ب ب, ر ج ع, ر ض و, ع ب د
  - themes: animal, calendar_season, desire_appetite, household_community, husbandry, livestock, provision_resource, water_hydrology
  - keywords: animal, husbandry, livestock, pastoralism, sustenance, water
- `د خ ل B008` — تداخل الأجزاء وما بين الداخل
  - activated_by_or_with: ج ن ن, ر ب ب, ر ج ع, ع ب د
  - themes: anatomy, form_structure, plant_vegetation, substance_texture, visual_appearance
  - keywords: anatomy, botany, color, morphology, structure, vegetation
- `د خ ل B009` — طائر يدخل الغيران والشجر
  - activated_by_or_with: ج ن ن, ر ب ب, ر ج ع, ع ب د
  - themes: animal, architecture_construction, habitat_ecology, motion, plant_vegetation, wildlife
  - keywords: animal, habitat, movement, shelter, vegetation, wildlife
- `د خ ل B010` — دوخلة الخوص للرطب
  - activated_by_or_with: ج ن ن, ر ب ب, ر ج ع, ر ض و, ع ب د
  - themes: agriculture, craft, food_nutrition, material, storage_vessels
  - keywords: agriculture, container, craft, food, material, storage

### ع ب د

- `ع ب د B001` — الرق والملك
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ر ض و
  - themes: commerce_exchange, control_restraint, hierarchy_status, labor_work, law, wealth_property
  - keywords: coercion, commerce, hierarchy, labor, law, property, status
- `ع ب د B002` — الانتساب إلى الله عبدا
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ع ب د B003` — العبادة والطاعة الخاضعة
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ر ض و
  - themes: authority_governance, belief_revelation, religion_worship, ritual, trust_loyalty
  - keywords: authority, devotion, loyalty, religion, ritual, theology
- `ع ب د B004` — التعبيد والاستعباد
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ر ض و
  - themes: control_restraint, force_power, hierarchy_status, justice_judgment, labor_work, support_dependence, violence_warfare
  - keywords: coercion, dependency, hierarchy, labor, power, violence
- `ع ب د B005` — التذليل والتسوية
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ر ض و
  - themes: animal, architecture_construction, craft, husbandry, material, stability_endurance, transport, travel
  - keywords: animal, craft, maintenance, material, transport, travel
- `ع ب د B006` — التكريم والتعظيم
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ر ض و
  - themes: authority_governance, hierarchy_status, honor_shame, hospitality_welfare, labor_work, religion_worship, ritual
  - keywords: authority, hierarchy, honor, status
- `ع ب د B007` — القوة والصلابة
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ر ض و
  - themes: animal, body, force_power, material, physiology, stability_endurance, textile_clothing
  - keywords: animal, body, endurance, material, textile, vitality
- `ع ب د B008` — الأنفة والغضب
  - activated_by_or_with: ج ن ن, د خ ل, ر ج ع, ر ض و
  - themes: desire_appetite, emotion, honor_shame, loss_absence
  - keywords: affect, emotion, honor, loss
- `ع ب د B009` — قلة اللبث وسرعة العدو
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع
  - themes: agency_action, motion, time, travel
  - keywords: motion, movement, performance, time, travel
- `ع ب د B010` — التفرق في الوجوه
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ر ض و
  - themes: form_structure, geography_landscape, household_community, motion, navigation_route, provision_resource, quantity_number, space
  - keywords: crowd, geography, movement, plurality, space
- `ع ب د B011` — العطب والانقطاع
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ر ض و
  - themes: animal, capacity_ability, control_restraint, loss_absence, physiology, stability_endurance, travel
  - keywords: animal, endurance, loss, travel
- `ع ب د B012` — صَلاءة الطيب
  - activated_by_or_with: ج ن ن, د خ ل, ر ب ب, ر ج ع, ر ض و
  - themes: craft, household_community, ornament_beauty, perception, ritual, storage_vessels, wealth_property
  - keywords: container, craft, ritual

### ج ن ن

- `ج ن ن B001` — الستر والاستتار
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: concealment_disclosure, containment_access, perception, protection_security, textile_clothing
  - keywords: clothing, concealment, interior, interiority, privacy, protection, secrecy
- `ج ن ن B002` — غشيان الليل
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: perception, sequence_cycle, sky_astronomy, textile_clothing, time, weather_climate
  - keywords: cycle, time, weather
- `ج ن ن B003` — البستان المستور بالشجر
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ر ض و, ع ب د
  - themes: abundance_scarcity, agriculture, architecture_construction, geography_landscape, habitat_ecology, plant_vegetation, reproduction_birth
  - keywords: abundance, agriculture, fertility, habitat, landscape, nature, shelter, vegetation
- `ج ن ن B004` — الجنة الأخروية
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ج ن ن B005` — الجن المستترون
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ر ض و, ع ب د
  - themes: belief_revelation, concealment_disclosure, household_community, place_location, rhetoric_discourse, sky_astronomy
  - keywords: community, place
- `ج ن ن B006` — ستر العقل بالجنون
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: agency_action, cognition, disease_injury, reasoning_decision
  - keywords: cognition, mind, psychology
- `ج ن ن B007` — الجنين المستور في البطن
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: body, growth_decay, kinship, physiology, reproduction_birth
  - keywords: biology, birth, body, development, kinship, reproduction
- `ج ن ن B008` — الجُنّة الواقية
  - activated_by_or_with: ر ب ب, ر ج ع, ر ض و, ع ب د
  - themes: body, protection_security, tools_equipment, violence_warfare, weaponry
  - keywords: body, protection, security, tool, warfare, weapon
- `ج ن ن B009` — مواراة الميت
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: body, concealment_disclosure, ritual
  - keywords: body, concealment, ritual
- `ج ن ن B010` — الجنان المستور في الصدر
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ر ض و, ع ب د
  - themes: body, cognition, concealment_disclosure, containment_access, emotion
  - keywords: body, cognition, emotion, interior, interiority, mind, psychology, secrecy
- `ج ن ن B011` — التفاف النبات واندفاعه
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ر ض و, ع ب د
  - themes: abundance_scarcity, agriculture, geography_landscape, growth_decay, habitat_ecology, plant_vegetation
  - keywords: abundance, agriculture, botany, ecology, growth, landscape, nature, vegetation
- `ج ن ن B012` — الجان حية
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: animal, danger_harm, wildlife
  - keywords: animal, wildlife, zoology
- `ج ن ن B013` — سواد الناس وجماعتهم
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ر ض و, ع ب د
  - themes: household_community, naming_classification, social_relations
  - keywords: community, crowd, demography, society
- `ج ن ن B014` — جن الشيء في بدايته
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: change_transition, growth_decay, life_stage_aging, physiology, sequence_cycle, time
  - keywords: development, life, time, transition
- `ج ن ن B015` — جن الذباب وصوت الخازباز
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: animal, danger_harm, perception, wildlife
  - keywords: animal, sound, zoology
- `ج ن ن B016` — الجناجن عظام الصدر
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ع ب د
  - themes: anatomy, body, form_structure, health_medicine
  - keywords: anatomy, body, medicine, structure
- `ج ن ن B017` — المَجَنَّة موضع الاستتار
  - activated_by_or_with: د خ ل, ر ب ب, ر ج ع, ر ض و, ع ب د
  - themes: architecture_construction, concealment_disclosure, place_location, protection_security, space
  - keywords: concealment, place, protection, security, shelter, space

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
