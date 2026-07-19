# v11 Activation Packet — S110:1-None

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_1: إِذَا جَآءَ نَصْرُ ٱللَّهِ وَٱلْفَتْحُ
- verse_2: وَرَأَيْتَ ٱلنَّاسَ يَدْخُلُونَ فِى دِينِ ٱللَّهِ أَفْوَاجًۭا
- verse_3: فَسَبِّحْ بِحَمْدِ رَبِّكَ وَٱسْتَغْفِرْهُ ۚ إِنَّهُۥ كَانَ تَوَّابًۢا

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ج ي ء → ن ص ر → ء ل ه → ف ت ح → ر ء ي → ن و س → د خ ل → د ي ن → ف و ج → س ب ح → ح م د → ر ب ب → غ ف ر → ك و ن → ت و ب

## Branch inventory summary

- ج ي ء: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن ص ر: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء ل ه: 2 branches (2 with Qnet bridge-theme nodes; 0 Furūq-only)
- ف ت ح: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- ر ء ي: 13 branches (13 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن و س: 3 branches (3 with Qnet bridge-theme nodes; 0 Furūq-only)
- د خ ل: 10 branches (10 with Qnet bridge-theme nodes; 0 Furūq-only)
- د ي ن: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- ف و ج: 2 branches (2 with Qnet bridge-theme nodes; 0 Furūq-only)
- س ب ح: 8 branches (7 with Qnet bridge-theme nodes; 1 Furūq-only)
- ح م د: 6 branches (5 with Qnet bridge-theme nodes; 1 Furūq-only)
- ر ب ب: 17 branches (17 with Qnet bridge-theme nodes; 0 Furūq-only)
- غ ف ر: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ك و ن: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- ت و ب: 4 branches (1 with Qnet bridge-theme nodes; 3 Furūq-only)

## QAC-first root resolution audit

- ج ي ء | qac_keys=جيء | status=merged | matches=root_000281, root_000282
- ن ص ر | qac_keys=نصر | status=resolved | matches=root_001510
- ء ل ه | qac_keys=ءله | status=resolved | matches=root_000047
- ف ت ح | qac_keys=فتح | status=resolved | matches=root_001124
- ر ء ي | qac_keys=رءي | status=resolved | matches=root_000531
- ن و س | qac_keys=نوس | status=resolved | matches=root_004965
- د خ ل | qac_keys=دخل | status=resolved | matches=root_000464
- د ي ن | qac_keys=دين | status=resolved | matches=root_000504
- ف و ج | qac_keys=فوج | status=resolved | matches=root_001184
- س ب ح | qac_keys=سبح | status=resolved | matches=root_000666
- ح م د | qac_keys=حمد | status=resolved | matches=root_000355
- ر ب ب | qac_keys=ربب | status=resolved | matches=root_000532
- غ ف ر | qac_keys=غفر | status=resolved | matches=root_001096
- ك و ن | qac_keys=كون | status=resolved | matches=root_001332
- ت و ب | qac_keys=توب | status=resolved | matches=root_000189

## Top candidate bridges

- `ن ص ر B004` ↔ `ف ت ح B005` | score_hint=26 | discovery_hint=18 | themes=agriculture, provision_resource, reproduction_birth, water_hydrology, weather_climate | keywords=agriculture, fertility, water, weather | q2=—
- `ن ص ر B004` ↔ `ر ب ب B008` | score_hint=30 | discovery_hint=17 | themes=agriculture, habitat_ecology, reproduction_birth, water_hydrology, weather_climate | keywords=agriculture, ecology, fertility, water, weather | q2=—
- `ف ت ح B005` ↔ `ر ب ب B008` | score_hint=24 | discovery_hint=17 | themes=agriculture, reproduction_birth, water_hydrology, weather_climate | keywords=agriculture, fertility, water, weather | q2=—
- `ن ص ر B002` ↔ `د ي ن B002` | score_hint=15 | discovery_hint=17 | themes=commerce_exchange, justice_judgment, punishment_sanction | keywords=justice, punishment | q2=—
- `د خ ل B006` ↔ `د ي ن B003` | score_hint=20 | discovery_hint=16 | themes=commerce_exchange, economy, finance_debt, wealth_property | keywords=economy, exchange, property | q2=—
- `ر ء ي B005` ↔ `د خ ل B004` | score_hint=13 | discovery_hint=16 | themes=deception_corruption, ethics_morality | keywords=deception, morality | q2=—
- `ج ي ء root_000282:B003` ↔ `ر ء ي B009` | score_hint=24 | discovery_hint=15 | themes=anatomy, body, disease_injury, health_medicine | keywords=anatomy, body, disease, medicine | q2=—
- `ن ص ر B005` ↔ `د خ ل B006` | score_hint=16 | discovery_hint=15 | themes=commerce_exchange, economy, provision_resource, wealth_property | keywords=economy, exchange | q2=—
- `ن ص ر B003` ↔ `ف و ج B001` | score_hint=13 | discovery_hint=15 | themes=migration_displacement, motion | keywords=migration, movement | q2=—
- `ج ي ء root_000281:B004` ↔ `ر ب ب B017` | score_hint=9 | discovery_hint=15 | themes=labor_work, transport | keywords=transport | q2=—
- `ر ء ي B013` ↔ `ر ب ب B015` | score_hint=9 | discovery_hint=15 | themes=language_speech, rhetoric_discourse | keywords=discourse | q2=—
- `د ي ن B002` ↔ `غ ف ر B002` | score_hint=9 | discovery_hint=15 | themes=afterlife_eschatology, justice_judgment | keywords=accountability | q2=—
- `ج ي ء root_000282:B003` ↔ `غ ف ر B004` | score_hint=20 | discovery_hint=14 | themes=disease_injury, health_medicine | keywords=healing, injury, medicine, pathology | q2=—
- `ن ص ر B001` ↔ `ف ت ح B004` | score_hint=20 | discovery_hint=14 | themes=conflict, force_power, protection_security, violence_warfare | keywords=conflict, power, warfare | q2=—
- `د ي ن B004` ↔ `ر ب ب B001` | score_hint=20 | discovery_hint=14 | themes=authority_governance, force_power, hierarchy_status, wealth_property | keywords=authority, hierarchy, power | q2=—
- `ج ي ء root_000281:B005` ↔ `د ي ن B004` | score_hint=18 | discovery_hint=14 | themes=control_restraint, force_power, violence_warfare | keywords=control, power, violence | q2=—
- `ج ي ء root_000281:B006` ↔ `غ ف ر B004` | score_hint=18 | discovery_hint=14 | themes=disease_injury, growth_decay, health_medicine | keywords=injury, medicine, pathology | q2=—
- `ن ص ر B005` ↔ `ف ت ح B007` | score_hint=18 | discovery_hint=14 | themes=abundance_scarcity, economy, wealth_property | keywords=abundance, economy, wealth | q2=—
- `ج ي ء root_000281:B001` ↔ `ج ي ء root_000282:B001` | score_hint=18 | discovery_hint=14 | themes=change_transition, loss_absence, motion | keywords=movement, presence, transition | q2=—
- `ج ي ء root_000281:B006` ↔ `ر ء ي B009` | score_hint=16 | discovery_hint=14 | themes=body, disease_injury, health_medicine, physiology | keywords=body, medicine | q2=—
- `ن ص ر B005` ↔ `د ي ن B003` | score_hint=14 | discovery_hint=14 | themes=commerce_exchange, economy, wealth_property | keywords=economy, exchange | q2=—
- `ن ص ر B005` ↔ `ح م د B005` | score_hint=14 | discovery_hint=14 | themes=commerce_exchange, hospitality_welfare, support_dependence | keywords=charity, patronage | q2=—
- `ر ب ب B011` ↔ `ك و ن B003` | score_hint=14 | discovery_hint=14 | themes=obligation_contract, protection_security, trust_loyalty | keywords=protection, trust | q2=—
- `ن ص ر B004` ↔ `ر ء ي B010` | score_hint=12 | discovery_hint=14 | themes=agriculture, reproduction_birth | keywords=agriculture, fertility | q2=—
- `ف ت ح B005` ↔ `ر ء ي B010` | score_hint=12 | discovery_hint=14 | themes=agriculture, reproduction_birth | keywords=agriculture, fertility | q2=—
- `ر ء ي B010` ↔ `ر ب ب B008` | score_hint=12 | discovery_hint=14 | themes=agriculture, reproduction_birth | keywords=agriculture, fertility | q2=—
- `د خ ل B010` ↔ `ر ب ب B012` | score_hint=12 | discovery_hint=14 | themes=agriculture, food_nutrition | keywords=agriculture, food | q2=—
- `ر ب ب B006` ↔ `غ ف ر B007` | score_hint=12 | discovery_hint=14 | themes=food_nutrition, substance_texture | keywords=food, substance | q2=—
- `ر ب ب B012` ↔ `غ ف ر B007` | score_hint=12 | discovery_hint=14 | themes=food_nutrition, plant_vegetation | keywords=botany, food | q2=—
- `ء ل ه B001` ↔ `س ب ح B008` | score_hint=11 | discovery_hint=14 | themes=pilgrimage_sacrifice, religion_worship, ritual | keywords=sacredness | q2=—
- `ج ي ء root_000281:B006` ↔ `غ ف ر B003` | score_hint=10 | discovery_hint=14 | themes=body, growth_decay, substance_texture | keywords=body | q2=—
- `ج ي ء root_000281:B003` ↔ `ج ي ء root_000282:B002` | score_hint=37 | discovery_hint=13 | themes=geography_landscape, place_location, protection_security, stability_endurance, storage_vessels, terrain_desert, water_hydrology | keywords=defense, hydrology, landscape, settlement, stagnation, topography | q2=—
- `ج ي ء root_000281:B006` ↔ `ج ي ء root_000282:B003` | score_hint=31 | discovery_hint=13 | themes=body, disease_injury, health_medicine, substance_texture | keywords=body, fluid, inflammation, injury, medicine, pathology | q2=—
- `ج ي ء root_000282:B002` ↔ `ن ص ر B007` | score_hint=18 | discovery_hint=13 | themes=geography_landscape, terrain_desert, water_hydrology | keywords=hydrology, terrain, topography | q2=—
- `ن ص ر B002` ↔ `ف ت ح B003` | score_hint=18 | discovery_hint=13 | themes=conflict, justice_judgment, law | keywords=conflict, justice, law | q2=—
- `ن ص ر B003` ↔ `ر ب ب B007` | score_hint=18 | discovery_hint=13 | themes=geography_landscape, motion, place_location | keywords=geography, motion, movement | q2=—
- `ن و س B002` ↔ `د خ ل B007` | score_hint=18 | discovery_hint=13 | themes=animal, husbandry, livestock | keywords=animal, herding, livestock | q2=—
- `ف و ج B001` ↔ `ر ب ب B004` | score_hint=18 | discovery_hint=13 | themes=household_community, quantity_number, social_relations | keywords=assembly, collectivity, society | q2=—
- `س ب ح B007` ↔ `غ ف ر B001` | score_hint=18 | discovery_hint=13 | themes=material, protection_security, textile_clothing | keywords=clothing, material, protection | q2=—
- `غ ف ر B002` ↔ `ت و ب B003` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, justice_judgment, religion_worship | keywords=accountability, ethics, religion | q2=—
- `ج ي ء root_000282:B002` ↔ `ف و ج B002` | score_hint=16 | discovery_hint=13 | themes=geography_landscape, terrain_desert | keywords=landscape, terrain, topography | q2=—
- `ن ص ر B007` ↔ `ف و ج B002` | score_hint=16 | discovery_hint=13 | themes=geography_landscape, terrain_desert | keywords=geography, terrain, topography | q2=—
- `ف ت ح B003` ↔ `د ي ن B006` | score_hint=16 | discovery_hint=13 | themes=authority_governance, law | keywords=authority, governance, law | q2=—
- `ر ء ي B010` ↔ `د خ ل B007` | score_hint=16 | discovery_hint=13 | themes=animal, husbandry | keywords=animal, herding, husbandry | q2=—
- `د خ ل B010` ↔ `غ ف ر B001` | score_hint=16 | discovery_hint=13 | themes=material, storage_vessels | keywords=container, material, storage | q2=—
- `ح م د B005` ↔ `ر ب ب B016` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, hospitality_welfare, obligation_contract, social_relations, support_dependence | keywords=charity, obligation | q2=—
- `ح م د B005` ↔ `ك و ن B003` | score_hint=16 | discovery_hint=13 | themes=hospitality_welfare, obligation_contract, social_relations, support_dependence | keywords=obligation, patronage | q2=—
- `ج ي ء root_000282:B003` ↔ `ر ء ي B007` | score_hint=14 | discovery_hint=13 | themes=body, health_medicine, purity_cleansing | keywords=body, medicine | q2=—
- `ن ص ر B001` ↔ `ك و ن B003` | score_hint=14 | discovery_hint=13 | themes=agency_action, protection_security, trust_loyalty | keywords=agency, protection | q2=—
- `ن ص ر B004` ↔ `ر ب ب B013` | score_hint=14 | discovery_hint=13 | themes=habitat_ecology, provision_resource, water_hydrology | keywords=ecology, sustenance | q2=—
- `ن ص ر B006` ↔ `ن و س B003` | score_hint=14 | discovery_hint=13 | themes=household_community, identity_personhood, social_relations | keywords=community, identity | q2=—
- `ن ص ر B006` ↔ `د ي ن B005` | score_hint=14 | discovery_hint=13 | themes=culture_tradition, identity_personhood, social_relations | keywords=identity, tradition | q2=—
- `د خ ل B002` ↔ `ر ب ب B005` | score_hint=14 | discovery_hint=13 | themes=household_community, kinship, reproduction_birth | keywords=household, kinship | q2=—
- `د خ ل B008` ↔ `غ ف ر B003` | score_hint=14 | discovery_hint=13 | themes=anatomy, form_structure, substance_texture | keywords=morphology, texture | q2=—
- `د ي ن B007` ↔ `ر ب ب B011` | score_hint=14 | discovery_hint=13 | themes=law, obligation_contract, trust_loyalty | keywords=law, trust | q2=—
- `د ي ن B007` ↔ `ك و ن B003` | score_hint=14 | discovery_hint=13 | themes=agency_action, obligation_contract, trust_loyalty | keywords=agency, trust | q2=—
- `س ب ح B007` ↔ `ر ب ب B002` | score_hint=14 | discovery_hint=13 | themes=craft, life_stage_aging, stability_endurance | keywords=childhood, craft | q2=—
- `ج ي ء root_000281:B006` ↔ `ر ء ي B007` | score_hint=12 | discovery_hint=13 | themes=body, health_medicine | keywords=body, medicine | q2=—
- `ن ص ر B002` ↔ `ر ب ب B011` | score_hint=12 | discovery_hint=13 | themes=law, protection_security | keywords=law, protection | q2=—
- `ن ص ر B004` ↔ `د خ ل B007` | score_hint=12 | discovery_hint=13 | themes=provision_resource, water_hydrology | keywords=sustenance, water | q2=—
- `ن ص ر B004` ↔ `ر ب ب B012` | score_hint=12 | discovery_hint=13 | themes=agriculture, habitat_ecology | keywords=agriculture, ecology | q2=—
- `ن ص ر B005` ↔ `ف ت ح B008` | score_hint=12 | discovery_hint=13 | themes=hospitality_welfare, support_dependence | keywords=charity, welfare | q2=—
- `ن ص ر B005` ↔ `ر ب ب B016` | score_hint=12 | discovery_hint=13 | themes=hospitality_welfare, support_dependence | keywords=charity, welfare | q2=—
- `ف ت ح B005` ↔ `ر ب ب B013` | score_hint=12 | discovery_hint=13 | themes=provision_resource, water_hydrology | keywords=hydrology, resource | q2=—
- `ف ت ح B007` ↔ `د خ ل B006` | score_hint=12 | discovery_hint=13 | themes=economy, wealth_property | keywords=economy, property | q2=—
- `ف ت ح B007` ↔ `د ي ن B003` | score_hint=12 | discovery_hint=13 | themes=economy, wealth_property | keywords=economy, property | q2=—
- `ف ت ح B008` ↔ `ر ب ب B016` | score_hint=12 | discovery_hint=13 | themes=hospitality_welfare, support_dependence | keywords=charity, welfare | q2=—
- `ف ت ح B009` ↔ `ح م د B005` | score_hint=12 | discovery_hint=13 | themes=hierarchy_status, identity_personhood | keywords=ego, status | q2=—
- `ر ء ي B010` ↔ `ر ب ب B009` | score_hint=12 | discovery_hint=13 | themes=animal, reproduction_birth | keywords=animal, reproduction | q2=—
- `ر ء ي B010` ↔ `غ ف ر B005` | score_hint=12 | discovery_hint=13 | themes=animal, reproduction_birth | keywords=animal, reproduction | q2=—
- `ن و س B003` ↔ `د خ ل B005` | score_hint=12 | discovery_hint=13 | themes=identity_personhood, social_relations | keywords=identity, society | q2=—
- `د خ ل B002` ↔ `ر ب ب B009` | score_hint=12 | discovery_hint=13 | themes=household_community, reproduction_birth | keywords=household, reproduction | q2=—
- `د خ ل B002` ↔ `غ ف ر B005` | score_hint=12 | discovery_hint=13 | themes=kinship, reproduction_birth | keywords=kinship, reproduction | q2=—
- `د خ ل B006` ↔ `س ب ح B005` | score_hint=12 | discovery_hint=13 | themes=economy, provision_resource | keywords=economy, livelihood | q2=—
- `د خ ل B008` ↔ `ر ب ب B012` | score_hint=12 | discovery_hint=13 | themes=plant_vegetation, visual_appearance | keywords=botany, color | q2=—
- `د خ ل B010` ↔ `ر ب ب B002` | score_hint=12 | discovery_hint=13 | themes=agriculture, craft | keywords=agriculture, craft | q2=—
- `د خ ل B010` ↔ `ر ب ب B006` | score_hint=12 | discovery_hint=13 | themes=food_nutrition, material | keywords=food, material | q2=—
- `س ب ح B004` ↔ `غ ف ر B006` | score_hint=12 | discovery_hint=13 | themes=navigation_route, sky_astronomy | keywords=astronomy, navigation | q2=—
- `ر ب ب B009` ↔ `غ ف ر B005` | score_hint=12 | discovery_hint=13 | themes=animal, reproduction_birth | keywords=animal, reproduction | q2=—
- `ف ت ح B007` ↔ `د خ ل B010` | score_hint=10 | discovery_hint=13 | themes=storage_vessels | keywords=container, storage | q2=—

## Per-root candidate activations

### ج ي ء

- `ج ي ء root_000281:B001` — المجيء والحصول
  - activated_by_or_with: same-root only
  - themes: change_transition, loss_absence, motion
  - keywords: movement, presence, transition
- `ج ي ء root_000281:B002` — المغالبة بكثرة المجيء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج ي ء root_000281:B003` — مجتمع الماء في هبطة أو حول حصن
  - activated_by_or_with: same-root only
  - themes: geography_landscape, place_location, protection_security, stability_endurance, storage_vessels, terrain_desert, water_hydrology
  - keywords: defense, hydrology, landscape, settlement, stagnation, topography
- `ج ي ء root_000281:B004` — الإتيان بالشيء واستحضاره
  - activated_by_or_with: ر ب ب
  - themes: labor_work, transport
  - keywords: transport
- `ج ي ء root_000281:B005` — الإلجاء والاضطرار
  - activated_by_or_with: د ي ن
  - themes: control_restraint, force_power, violence_warfare
  - keywords: control, power, violence
- `ج ي ء root_000281:B006` — الجائية من الجراح
  - activated_by_or_with: ر ء ي, غ ف ر
  - themes: body, disease_injury, growth_decay, health_medicine, physiology, substance_texture
  - keywords: body, fluid, inflammation, injury, medicine, pathology
- `ج ي ء root_000282:B001` — المجيء والغلبة بالمجيء
  - activated_by_or_with: same-root only
  - themes: change_transition, loss_absence, motion
  - keywords: movement, presence, transition
- `ج ي ء root_000282:B002` — الجِيأة مجتمع الماء
  - activated_by_or_with: ف و ج, ن ص ر
  - themes: geography_landscape, place_location, protection_security, stability_endurance, storage_vessels, terrain_desert, water_hydrology
  - keywords: defense, hydrology, landscape, settlement, stagnation, terrain, topography
- `ج ي ء root_000282:B003` — جائية الجراح
  - activated_by_or_with: ر ء ي, غ ف ر
  - themes: anatomy, body, disease_injury, health_medicine, purity_cleansing, substance_texture
  - keywords: anatomy, body, disease, fluid, healing, inflammation, injury, medicine, pathology

### ن ص ر

- `ن ص ر B001` — النصرة عون وإظهار
  - activated_by_or_with: ف ت ح, ك و ن
  - themes: agency_action, conflict, force_power, protection_security, trust_loyalty, violence_warfare
  - keywords: agency, conflict, power, protection, warfare
- `ن ص ر B002` — انتصاف المظلوم
  - activated_by_or_with: د ي ن, ر ب ب, ف ت ح
  - themes: commerce_exchange, conflict, justice_judgment, law, protection_security, punishment_sanction
  - keywords: conflict, justice, law, protection, punishment
- `ن ص ر B003` — إتيان البلد
  - activated_by_or_with: ر ب ب, ف و ج
  - themes: geography_landscape, migration_displacement, motion, place_location
  - keywords: geography, migration, motion, movement
- `ن ص ر B004` — النصر مطر وإغاثة
  - activated_by_or_with: د خ ل, ر ء ي, ر ب ب, ف ت ح
  - themes: agriculture, habitat_ecology, provision_resource, reproduction_birth, water_hydrology, weather_climate
  - keywords: agriculture, ecology, fertility, sustenance, water, weather
- `ن ص ر B005` — النصر عطاء
  - activated_by_or_with: ح م د, د خ ل, د ي ن, ر ب ب, ف ت ح
  - themes: abundance_scarcity, commerce_exchange, economy, hospitality_welfare, provision_resource, support_dependence, wealth_property
  - keywords: abundance, charity, economy, exchange, patronage, wealth, welfare
- `ن ص ر B006` — النصرانية نسبة وملة
  - activated_by_or_with: د ي ن, ن و س
  - themes: culture_tradition, household_community, identity_personhood, social_relations
  - keywords: community, identity, tradition
- `ن ص ر B007` — ناصرة الماء
  - activated_by_or_with: ج ي ء, ف و ج
  - themes: geography_landscape, terrain_desert, water_hydrology
  - keywords: geography, hydrology, terrain, topography

### ء ل ه

- `ء ل ه B001` — التعبد والمعبود
  - activated_by_or_with: س ب ح
  - themes: pilgrimage_sacrifice, religion_worship, ritual
  - keywords: sacredness
- `ء ل ه B002` — اسم الله في القسم والنداء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ف ت ح

- `ف ت ح B001` — انفراج المغلق واتساع المدخل
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ف ت ح B002` — فاتحة الشيء ومبدؤه الذي يفتح ما بعده
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ف ت ح B003` — فصل الإغلاق بالحكم والقضاء
  - activated_by_or_with: د ي ن, ن ص ر
  - themes: authority_governance, conflict, justice_judgment, law
  - keywords: authority, conflict, governance, justice, law
- `ف ت ح B004` — انفتاح الغلبة والظفر
  - activated_by_or_with: ن ص ر
  - themes: conflict, force_power, protection_security, violence_warfare
  - keywords: conflict, power, warfare
- `ف ت ح B005` — انبعاث الماء من منفذه
  - activated_by_or_with: ر ء ي, ر ب ب, ن ص ر
  - themes: agriculture, provision_resource, reproduction_birth, water_hydrology, weather_climate
  - keywords: agriculture, fertility, hydrology, resource, water, weather
- `ف ت ح B006` — آلة الوصول إلى المغلق
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ف ت ح B007` — الخزانة المنفتحة على ما فيها
  - activated_by_or_with: د خ ل, د ي ن, ن ص ر
  - themes: abundance_scarcity, economy, storage_vessels, wealth_property
  - keywords: abundance, container, economy, property, storage, wealth
- `ف ت ح B008` — انكشاف الانغلاق المعنوي بالبصيرة أو التفريج
  - activated_by_or_with: ر ب ب, ن ص ر
  - themes: hospitality_welfare, support_dependence
  - keywords: charity, welfare
- `ف ت ح B009` — تفتح المتطاول بما يظهره من مال أو أدب
  - activated_by_or_with: ح م د
  - themes: hierarchy_status, identity_personhood
  - keywords: ego, status

### ر ء ي

- `ر ء ي B001` — رؤية العين والبصيرة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ء ي B002` — رأي القلب والتفكر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ء ي B003` — الرؤيا في المنام
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ء ي B004` — تراء وتواجه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ء ي B005` — رياء الناس
  - activated_by_or_with: د خ ل
  - themes: deception_corruption, ethics_morality
  - keywords: deception, morality
- `ر ء ي B006` — مرأى ومنظر ومرآة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ء ي B007` — ترية الحيض
  - activated_by_or_with: ج ي ء
  - themes: body, health_medicine, purity_cleansing
  - keywords: body, medicine
- `ر ء ي B008` — رئي من الجن
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ء ي B009` — الرئة وما يصيبها
  - activated_by_or_with: ج ي ء
  - themes: anatomy, body, disease_injury, health_medicine, physiology
  - keywords: anatomy, body, disease, medicine
- `ر ء ي B010` — ظهور حمل الناقة أو الشاة
  - activated_by_or_with: د خ ل, ر ب ب, غ ف ر, ف ت ح, ن ص ر
  - themes: agriculture, animal, husbandry, reproduction_birth
  - keywords: agriculture, animal, fertility, herding, husbandry, reproduction
- `ر ء ي B011` — راية منصوبة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ء ي B012` — إراءة وإظهار
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ء ي B013` — أرأيتك للتنبيه والاستخبار
  - activated_by_or_with: ر ب ب
  - themes: language_speech, rhetoric_discourse
  - keywords: discourse

### ن و س

- `ن و س B001` — تذبذب الشيء المتدلّي
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن و س B002` — سوق الإبل
  - activated_by_or_with: د خ ل
  - themes: animal, husbandry, livestock
  - keywords: animal, herding, livestock
- `ن و س B003` — اسم الناس المختلف في أصله
  - activated_by_or_with: د خ ل, ن ص ر
  - themes: household_community, identity_personhood, social_relations
  - keywords: community, identity, society

### د خ ل

- `د خ ل B001` — الولوج إلى داخل
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `د خ ل B002` — الإفضاء الزوجي
  - activated_by_or_with: ر ب ب, غ ف ر
  - themes: household_community, kinship, reproduction_birth
  - keywords: household, kinship, reproduction
- `د خ ل B003` — الباطن والسريرة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `د خ ل B004` — فساد مستبطن
  - activated_by_or_with: ر ء ي
  - themes: deception_corruption, ethics_morality
  - keywords: deception, morality
- `د خ ل B005` — دخيل يخالط القوم أو الأمر
  - activated_by_or_with: ن و س
  - themes: identity_personhood, social_relations
  - keywords: identity, society
- `د خ ل B006` — ما يدخل من كسب
  - activated_by_or_with: د ي ن, س ب ح, ف ت ح, ن ص ر
  - themes: commerce_exchange, economy, finance_debt, provision_resource, wealth_property
  - keywords: economy, exchange, livelihood, property
- `د خ ل B007` — إدخال الإبل في الشرب مرة أخرى
  - activated_by_or_with: ر ء ي, ن ص ر, ن و س
  - themes: animal, husbandry, livestock, provision_resource, water_hydrology
  - keywords: animal, herding, husbandry, livestock, sustenance, water
- `د خ ل B008` — تداخل الأجزاء وما بين الداخل
  - activated_by_or_with: ر ب ب, غ ف ر
  - themes: anatomy, form_structure, plant_vegetation, substance_texture, visual_appearance
  - keywords: botany, color, morphology, texture
- `د خ ل B009` — طائر يدخل الغيران والشجر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `د خ ل B010` — دوخلة الخوص للرطب
  - activated_by_or_with: ر ب ب, غ ف ر, ف ت ح
  - themes: agriculture, craft, food_nutrition, material, storage_vessels
  - keywords: agriculture, container, craft, food, material, storage

### د ي ن

- `د ي ن B001` — الطاعة والانقياد
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `د ي ن B002` — الحساب والجزاء
  - activated_by_or_with: غ ف ر, ن ص ر
  - themes: afterlife_eschatology, commerce_exchange, justice_judgment, punishment_sanction
  - keywords: accountability, justice, punishment
- `د ي ن B003` — الدين المالي
  - activated_by_or_with: د خ ل, ف ت ح, ن ص ر
  - themes: commerce_exchange, economy, finance_debt, wealth_property
  - keywords: economy, exchange, property
- `د ي ن B004` — الإذلال والملك
  - activated_by_or_with: ج ي ء, ر ب ب
  - themes: authority_governance, control_restraint, force_power, hierarchy_status, violence_warfare, wealth_property
  - keywords: authority, control, hierarchy, power, violence
- `د ي ن B005` — العادة والشأن
  - activated_by_or_with: ن ص ر
  - themes: culture_tradition, identity_personhood, social_relations
  - keywords: identity, tradition
- `د ي ن B006` — مدينة الطاعة
  - activated_by_or_with: ف ت ح
  - themes: authority_governance, law
  - keywords: authority, governance, law
- `د ي ن B007` — التصديق والتفويض
  - activated_by_or_with: ر ب ب, ك و ن
  - themes: agency_action, law, obligation_contract, trust_loyalty
  - keywords: agency, law, trust

### ف و ج

- `ف و ج B001` — الجماعة من الناس
  - activated_by_or_with: ر ب ب, ن ص ر
  - themes: household_community, migration_displacement, motion, quantity_number, social_relations
  - keywords: assembly, collectivity, migration, movement, society
- `ف و ج B002` — الفائجة الواسعة
  - activated_by_or_with: ج ي ء, ن ص ر
  - themes: geography_landscape, terrain_desert
  - keywords: geography, landscape, terrain, topography

### س ب ح

- `س ب ح B001` — العبادة بالتسبيح والصلاة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `س ب ح B002` — التنزيه والتبرئة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `س ب ح B003` — سبحات الجلال والنور
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `س ب ح B004` — السبح في الجري والعوم
  - activated_by_or_with: غ ف ر
  - themes: navigation_route, sky_astronomy
  - keywords: astronomy, navigation
- `س ب ح B005` — السعة للذهاب والمعاش
  - activated_by_or_with: د خ ل
  - themes: economy, provision_resource
  - keywords: economy, livelihood
- `س ب ح B006` — خرز التسبيح
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `س ب ح B007` — سباح الجلود والكساء
  - activated_by_or_with: ر ب ب, غ ف ر
  - themes: craft, life_stage_aging, material, protection_security, stability_endurance, textile_clothing
  - keywords: childhood, clothing, craft, material, protection
- `س ب ح B008` — سبوحة الموضع
  - activated_by_or_with: ء ل ه
  - themes: pilgrimage_sacrifice, religion_worship, ritual
  - keywords: sacredness

### ح م د

- `ح م د B001` — الحمد خلاف الذم
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح م د B002` — وجود الشيء محمودا
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح م د B003` — المحمود كثير الخصال
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح م د B004` — حماداك الغاية المحمودة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح م د B005` — يتحمد بالمنة
  - activated_by_or_with: ر ب ب, ف ت ح, ك و ن, ن ص ر
  - themes: commerce_exchange, ethics_morality, hierarchy_status, hospitality_welfare, identity_personhood, obligation_contract, social_relations, support_dependence
  - keywords: charity, ego, obligation, patronage, status
- `ح م د B006` — أحمد إليك الله
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### ر ب ب

- `ر ب ب B001` — ربوبية وملك وسيادة
  - activated_by_or_with: د ي ن
  - themes: authority_governance, force_power, hierarchy_status, wealth_property
  - keywords: authority, hierarchy, power
- `ر ب ب B002` — إصلاح وتربية وإتمام
  - activated_by_or_with: د خ ل, س ب ح
  - themes: agriculture, craft, life_stage_aging, stability_endurance
  - keywords: agriculture, childhood, craft
- `ر ب ب B003` — علم رباني
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B004` — ربة وجماعات كثيرة
  - activated_by_or_with: ف و ج
  - themes: household_community, quantity_number, social_relations
  - keywords: assembly, collectivity, society
- `ر ب ب B005` — ربيب وربيبة ورابة
  - activated_by_or_with: د خ ل
  - themes: household_community, kinship, reproduction_birth
  - keywords: household, kinship
- `ر ب ب B006` — رُبّ خاثر وإصلاح به
  - activated_by_or_with: د خ ل, غ ف ر
  - themes: food_nutrition, material, substance_texture
  - keywords: food, material, substance
- `ر ب ب B007` — لزوم وإقامة ودوام
  - activated_by_or_with: ن ص ر
  - themes: geography_landscape, motion, place_location
  - keywords: geography, motion, movement
- `ر ب ب B008` — رباب السحاب
  - activated_by_or_with: ر ء ي, ف ت ح, ن ص ر
  - themes: agriculture, habitat_ecology, reproduction_birth, water_hydrology, weather_climate
  - keywords: agriculture, ecology, fertility, water, weather
- `ر ب ب B009` — شاة رُبّى وحداثة
  - activated_by_or_with: د خ ل, ر ء ي, غ ف ر
  - themes: animal, household_community, reproduction_birth
  - keywords: animal, household, reproduction
- `ر ب ب B010` — ربابة تجمع القداح
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B011` — ربابة عهد وميثاق
  - activated_by_or_with: د ي ن, ك و ن, ن ص ر
  - themes: law, obligation_contract, protection_security, trust_loyalty
  - keywords: law, protection, trust
- `ر ب ب B012` — ربة نبات
  - activated_by_or_with: د خ ل, غ ف ر, ن ص ر
  - themes: agriculture, food_nutrition, habitat_ecology, plant_vegetation, visual_appearance
  - keywords: agriculture, botany, color, ecology, food
- `ر ب ب B013` — ماء رَبَب كثير
  - activated_by_or_with: ف ت ح, ن ص ر
  - themes: habitat_ecology, provision_resource, water_hydrology
  - keywords: ecology, hydrology, resource, sustenance
- `ر ب ب B014` — رَبْرَب قطيع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B015` — حرف رب وربما
  - activated_by_or_with: ر ء ي
  - themes: language_speech, rhetoric_discourse
  - keywords: discourse
- `ر ب ب B016` — رُبَى حاجة وعقدة ونعمة
  - activated_by_or_with: ح م د, ف ت ح, ن ص ر
  - themes: ethics_morality, hospitality_welfare, obligation_contract, social_relations, support_dependence
  - keywords: charity, obligation, welfare
- `ر ب ب B017` — رباني الملاحين
  - activated_by_or_with: ج ي ء
  - themes: labor_work, transport
  - keywords: transport

### غ ف ر

- `غ ف ر B001` — ستر يصون الشيء ويغطيه
  - activated_by_or_with: د خ ل, س ب ح
  - themes: material, protection_security, storage_vessels, textile_clothing
  - keywords: clothing, container, material, protection, storage
- `غ ف ر B002` — ستر الذنب وصون صاحبه من أثره
  - activated_by_or_with: ت و ب, د ي ن
  - themes: afterlife_eschatology, ethics_morality, justice_judgment, religion_worship
  - keywords: accountability, ethics, religion
- `غ ف ر B003` — زئبر أو شعر يغطي السطح
  - activated_by_or_with: ج ي ء, د خ ل
  - themes: anatomy, body, form_structure, growth_decay, substance_texture
  - keywords: body, morphology, texture
- `غ ف ر B004` — نكس المرض أو الجرح
  - activated_by_or_with: ج ي ء
  - themes: disease_injury, growth_decay, health_medicine
  - keywords: healing, injury, medicine, pathology
- `غ ف ر B005` — ولد الأروية وأمه
  - activated_by_or_with: د خ ل, ر ء ي, ر ب ب
  - themes: animal, kinship, reproduction_birth
  - keywords: animal, kinship, reproduction
- `غ ف ر B006` — منزل قمري من ثلاثة أنجم
  - activated_by_or_with: س ب ح
  - themes: navigation_route, sky_astronomy
  - keywords: astronomy, navigation
- `غ ف ر B007` — مغافير الشجر الحلوة
  - activated_by_or_with: ر ب ب
  - themes: food_nutrition, plant_vegetation, substance_texture
  - keywords: botany, food, substance
- `غ ف ر B008` — جماء الغفير: الجماعة كلها
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ك و ن

- `ك و ن B001` — وقوع الشيء وحضوره في زمان
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ك و ن B002` — المكان والمكانة من الكون
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ك و ن B003` — الكفالة والقيام على فلان
  - activated_by_or_with: ح م د, د ي ن, ر ب ب, ن ص ر
  - themes: agency_action, hospitality_welfare, obligation_contract, protection_security, social_relations, support_dependence, trust_loyalty
  - keywords: agency, obligation, patronage, protection, trust
- `ك و ن B004` — الخضوع بالاستكانة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ك و ن B005` — الشيخ المنسوب إلى كُنْتُ
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ك و ن B006` — حالة السوء بكينة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ت و ب

- `ت و ب B001` — الرجوع من الذنب إلى الله
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ت و ب B002` — عود الله على العبد بالتوبة والقبول
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ت و ب B003` — استدعاء التوبة من غيره
  - activated_by_or_with: غ ف ر
  - themes: ethics_morality, justice_judgment, religion_worship
  - keywords: accountability, ethics, religion
- `ت و ب B004` — رجوع الله بالعبد إلى التخفيف والإباحة
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
