# v11 Activation Packet — S106:1-None

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_1: لِإِيلَٰفِ قُرَيْشٍ
- verse_2: إِۦلَٰفِهِمْ رِحْلَةَ ٱلشِّتَآءِ وَٱلصَّيْفِ
- verse_3: فَلْيَعْبُدُوا۟ رَبَّ هَٰذَا ٱلْبَيْتِ
- verse_4: ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ء ل ف → ر ح ل → ش ت و → ص ي ف → ع ب د → ر ب ب → ب ي ت → ط ع م → ج و ع → ء م ن → خ و ف

## Branch inventory summary

- ء ل ف: 6 branches (4 with Qnet bridge-theme nodes; 2 Furūq-only)
- ر ح ل: 12 branches (12 with Qnet bridge-theme nodes; 0 Furūq-only)
- ش ت و: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص ي ف: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- ع ب د: 12 branches (11 with Qnet bridge-theme nodes; 1 Furūq-only)
- ر ب ب: 17 branches (17 with Qnet bridge-theme nodes; 0 Furūq-only)
- ب ي ت: 10 branches (9 with Qnet bridge-theme nodes; 1 Furūq-only)
- ط ع م: 14 branches (13 with Qnet bridge-theme nodes; 1 Furūq-only)
- ج و ع: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء م ن: 3 branches (3 with Qnet bridge-theme nodes; 0 Furūq-only)
- خ و ف: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)

## QAC-first root resolution audit

- ء ل ف | qac_keys=ءلف | status=resolved | matches=root_000045
- ر ح ل | qac_keys=رحل | status=resolved | matches=root_000551
- ش ت و | qac_keys=شتو | status=resolved | matches=root_000776
- ص ي ف | qac_keys=صيف | status=resolved | matches=root_000899
- ع ب د | qac_keys=عبد | status=resolved | matches=root_000973
- ر ب ب | qac_keys=ربب | status=resolved | matches=root_000532
- ب ي ت | qac_keys=بيت | status=resolved | matches=root_000166
- ط ع م | qac_keys=طعم | status=resolved | matches=root_000934
- ج و ع | qac_keys=جوع | status=resolved | matches=root_000278
- ء م ن | qac_keys=ءمن | status=resolved | matches=root_000054
- خ و ف | qac_keys=خوف | status=resolved | matches=root_000447

## Top candidate bridges

- `ص ي ف B002` ↔ `ر ب ب B008` | score_hint=30 | discovery_hint=17 | themes=agriculture, habitat_ecology, reproduction_birth, water_hydrology, weather_climate | keywords=agriculture, ecology, fertility, water, weather | q2=—
- `ش ت و B003` ↔ `ص ي ف B002` | score_hint=24 | discovery_hint=17 | themes=agriculture, reproduction_birth, water_hydrology, weather_climate | keywords=agriculture, fertility, water, weather | q2=—
- `ش ت و B003` ↔ `ر ب ب B008` | score_hint=24 | discovery_hint=17 | themes=agriculture, reproduction_birth, water_hydrology, weather_climate | keywords=agriculture, fertility, water, weather | q2=—
- `ع ب د B009` ↔ `ط ع م B009` | score_hint=16 | discovery_hint=17 | themes=motion, recreation_sport, speed | keywords=motion, speed | q2=—
- `ر ب ب B006` ↔ `ب ي ت B006` | score_hint=11 | discovery_hint=17 | themes=food_nutrition, stability_endurance, substance_texture | keywords=preservation | q2=—
- `ش ت و B004` ↔ `ج و ع B002` | score_hint=40 | discovery_hint=16 | themes=abundance_scarcity, danger_harm, habitat_ecology, provision_resource, stability_endurance, weather_climate | keywords=crisis, disaster, ecology, poverty, scarcity, survival, sustenance | q2=—
- `ر ح ل B009` ↔ `ع ب د B004` | score_hint=15 | discovery_hint=16 | themes=control_restraint, justice_judgment, violence_warfare | keywords=oppression, violence | q2=—
- `ر ب ب B011` ↔ `ط ع م B004` | score_hint=7 | discovery_hint=16 | themes=finance_debt | keywords=taxation | q2=—
- `ط ع م B001` ↔ `ج و ع B001` | score_hint=24 | discovery_hint=15 | themes=body, desire_appetite, food_nutrition, support_dependence | keywords=appetite, body, need, nutrition | q2=—
- `ب ي ت B005` ↔ `ط ع م B001` | score_hint=18 | discovery_hint=15 | themes=food_nutrition, provision_resource, support_dependence | keywords=food, need, subsistence | q2=—
- `ط ع م B007` ↔ `ج و ع B001` | score_hint=18 | discovery_hint=15 | themes=body, food_nutrition, physiology | keywords=body, nutrition, physiology | q2=—
- `ر ح ل B001` ↔ `ص ي ف B005` | score_hint=15 | discovery_hint=15 | themes=motion, navigation_route, orientation_direction | keywords=navigation, orientation | q2=—
- `ر ب ب B014` ↔ `ط ع م B006` | score_hint=11 | discovery_hint=15 | themes=animal, habitat_ecology, wildlife | keywords=hunting | q2=—
- `ط ع م B012` ↔ `خ و ف B003` | score_hint=7 | discovery_hint=15 | themes=conflict | keywords=conflict | q2=—
- `ر ح ل B002` ↔ `ع ب د B005` | score_hint=24 | discovery_hint=14 | themes=animal, material, transport, travel | keywords=animal, material, transport, travel | q2=—
- `ب ي ت B005` ↔ `ج و ع B001` | score_hint=20 | discovery_hint=14 | themes=abundance_scarcity, food_nutrition, stability_endurance, support_dependence | keywords=need, scarcity, survival | q2=—
- `ر ح ل B011` ↔ `ط ع م B007` | score_hint=18 | discovery_hint=14 | themes=anatomy, animal, body | keywords=anatomy, animal, body | q2=—
- `ش ت و B004` ↔ `ب ي ت B005` | score_hint=18 | discovery_hint=14 | themes=abundance_scarcity, provision_resource, stability_endurance | keywords=scarcity, survival, sustenance | q2=—
- `ب ي ت B005` ↔ `ج و ع B002` | score_hint=18 | discovery_hint=14 | themes=abundance_scarcity, provision_resource, stability_endurance | keywords=scarcity, survival, sustenance | q2=—
- `ب ي ت B005` ↔ `ط ع م B004` | score_hint=16 | discovery_hint=14 | themes=economy, provision_resource, stability_endurance, support_dependence | keywords=economy, subsistence | q2=—
- `ر ح ل B008` ↔ `ط ع م B002` | score_hint=14 | discovery_hint=14 | themes=hospitality_welfare, provision_resource, support_dependence | keywords=charity, hospitality | q2=—
- `ر ح ل B008` ↔ `ط ع م B004` | score_hint=14 | discovery_hint=14 | themes=hospitality_welfare, provision_resource, support_dependence | keywords=hospitality, patronage | q2=—
- `ص ي ف B002` ↔ `ج و ع B002` | score_hint=14 | discovery_hint=14 | themes=agriculture, habitat_ecology, weather_climate | keywords=agriculture, ecology | q2=—
- `ع ب د B007` ↔ `ط ع م B007` | score_hint=14 | discovery_hint=14 | themes=animal, body, physiology | keywords=animal, body | q2=—
- `ر ب ب B008` ↔ `ج و ع B002` | score_hint=14 | discovery_hint=14 | themes=agriculture, habitat_ecology, weather_climate | keywords=agriculture, ecology | q2=—
- `ب ي ت B002` ↔ `ب ي ت B008` | score_hint=14 | discovery_hint=14 | themes=identity_personhood, kinship, marriage_genealogy | keywords=genealogy, identity | q2=—
- `ش ت و B003` ↔ `ط ع م B005` | score_hint=12 | discovery_hint=14 | themes=agriculture, reproduction_birth | keywords=agriculture, fertility | q2=—
- `ش ت و B003` ↔ `ج و ع B002` | score_hint=12 | discovery_hint=14 | themes=agriculture, weather_climate | keywords=agriculture, climate | q2=—
- `ص ي ف B002` ↔ `ط ع م B005` | score_hint=12 | discovery_hint=14 | themes=agriculture, reproduction_birth | keywords=agriculture, fertility | q2=—
- `ص ي ف B004` ↔ `ر ب ب B009` | score_hint=12 | discovery_hint=14 | themes=life_stage_aging, reproduction_birth | keywords=birth, reproduction | q2=—
- `ر ب ب B008` ↔ `ط ع م B005` | score_hint=12 | discovery_hint=14 | themes=agriculture, reproduction_birth | keywords=agriculture, fertility | q2=—
- `ر ب ب B012` ↔ `ط ع م B005` | score_hint=12 | discovery_hint=14 | themes=agriculture, plant_vegetation | keywords=agriculture, botany | q2=—
- `ع ب د B010` ↔ `ب ي ت B001` | score_hint=9 | discovery_hint=14 | themes=household_community, space | keywords=space | q2=—
- `ع ب د B001` ↔ `ر ب ب B011` | score_hint=7 | discovery_hint=14 | themes=law | keywords=law | q2=—
- `ش ت و B001` ↔ `ص ي ف B001` | score_hint=32 | discovery_hint=13 | themes=calendar_season, habitat_ecology, time, weather_climate | keywords=calendar, climate, nature, seasonality, time, weather | q2=—
- `ر ح ل B005` ↔ `ع ب د B005` | score_hint=20 | discovery_hint=13 | themes=animal, stability_endurance, transport, travel | keywords=animal, transport, travel | q2=—
- `ش ت و B002` ↔ `ص ي ف B003` | score_hint=20 | discovery_hint=13 | themes=calendar_season, migration_displacement, place_location, travel | keywords=migration, settlement, travel | q2=—
- `ع ب د B005` ↔ `خ و ف B006` | score_hint=20 | discovery_hint=13 | themes=craft, husbandry, material, transport | keywords=craft, material, transport | q2=—
- `ر ح ل B004` ↔ `ش ت و B002` | score_hint=18 | discovery_hint=13 | themes=architecture_construction, migration_displacement, place_location | keywords=habitation, settlement, shelter | q2=—
- `ر ح ل B005` ↔ `ع ب د B011` | score_hint=18 | discovery_hint=13 | themes=animal, stability_endurance, travel | keywords=animal, endurance, travel | q2=—
- `ر ح ل B010` ↔ `خ و ف B006` | score_hint=18 | discovery_hint=13 | themes=craft, material, textile_clothing | keywords=clothing, craft, material | q2=—
- `ر ب ب B005` ↔ `ب ي ت B010` | score_hint=18 | discovery_hint=13 | themes=family, household_community, kinship | keywords=family, household, kinship | q2=—
- `ع ب د B006` ↔ `ب ي ت B008` | score_hint=16 | discovery_hint=13 | themes=hierarchy_status, honor_shame | keywords=hierarchy, honor, status | q2=—
- `ع ب د B009` ↔ `ر ب ب B007` | score_hint=16 | discovery_hint=13 | themes=motion, time | keywords=motion, movement, time | q2=—
- `ع ب د B003` ↔ `ء م ن B002` | score_hint=16 | discovery_hint=13 | themes=authority_governance, belief_revelation, religion_worship, trust_loyalty | keywords=faith, religion | q2=—
- `ر ح ل B005` ↔ `ع ب د B007` | score_hint=14 | discovery_hint=13 | themes=animal, force_power, stability_endurance | keywords=animal, endurance | q2=—
- `ش ت و B004` ↔ `ر ب ب B013` | score_hint=14 | discovery_hint=13 | themes=abundance_scarcity, habitat_ecology, provision_resource | keywords=ecology, sustenance | q2=—
- `ص ي ف B004` ↔ `ر ب ب B005` | score_hint=14 | discovery_hint=13 | themes=family, kinship, reproduction_birth | keywords=family, kinship | q2=—
- `ع ب د B004` ↔ `ر ب ب B001` | score_hint=14 | discovery_hint=13 | themes=force_power, hierarchy_status, support_dependence | keywords=hierarchy, power | q2=—
- `ر ب ب B009` ↔ `ط ع م B007` | score_hint=14 | discovery_hint=13 | themes=animal, food_nutrition, livestock | keywords=animal, livestock | q2=—
- `ر ب ب B011` ↔ `ء م ن B001` | score_hint=14 | discovery_hint=13 | themes=obligation_contract, protection_security, trust_loyalty | keywords=protection, trust | q2=—
- `ر ب ب B013` ↔ `ج و ع B002` | score_hint=14 | discovery_hint=13 | themes=abundance_scarcity, habitat_ecology, provision_resource | keywords=ecology, sustenance | q2=—
- `ر ح ل B011` ↔ `ع ب د B007` | score_hint=12 | discovery_hint=13 | themes=animal, body | keywords=animal, body | q2=—
- `ر ح ل B011` ↔ `ج و ع B004` | score_hint=12 | discovery_hint=13 | themes=body, visual_appearance | keywords=appearance, body | q2=—
- `ر ح ل B012` ↔ `ب ي ت B010` | score_hint=12 | discovery_hint=13 | themes=kinship, sexuality | keywords=kinship, sexuality | q2=—
- `ش ت و B004` ↔ `ط ع م B002` | score_hint=12 | discovery_hint=13 | themes=abundance_scarcity, provision_resource | keywords=poverty, sustenance | q2=—
- `ص ي ف B002` ↔ `ر ب ب B012` | score_hint=12 | discovery_hint=13 | themes=agriculture, habitat_ecology | keywords=agriculture, ecology | q2=—
- `ص ي ف B003` ↔ `ب ي ت B005` | score_hint=12 | discovery_hint=13 | themes=economy, provision_resource | keywords=economy, provisioning | q2=—
- `ع ب د B004` ↔ `ط ع م B011` | score_hint=12 | discovery_hint=13 | themes=control_restraint, force_power | keywords=control, power | q2=—
- `ع ب د B004` ↔ `خ و ف B002` | score_hint=12 | discovery_hint=13 | themes=control_restraint, force_power | keywords=coercion, control | q2=—
- `ر ب ب B001` ↔ `ط ع م B004` | score_hint=12 | discovery_hint=13 | themes=support_dependence, wealth_property | keywords=patronage, property | q2=—
- `ر ب ب B009` ↔ `ب ي ت B006` | score_hint=12 | discovery_hint=13 | themes=food_nutrition, time | keywords=dairy, time | q2=—
- `ر ب ب B009` ↔ `ط ع م B014` | score_hint=12 | discovery_hint=13 | themes=reproduction_birth, time | keywords=temporality, time | q2=—
- `ر ب ب B012` ↔ `ج و ع B002` | score_hint=12 | discovery_hint=13 | themes=agriculture, habitat_ecology | keywords=agriculture, ecology | q2=—
- `ر ب ب B016` ↔ `ط ع م B002` | score_hint=12 | discovery_hint=13 | themes=hospitality_welfare, support_dependence | keywords=charity, welfare | q2=—
- `ط ع م B002` ↔ `ج و ع B002` | score_hint=12 | discovery_hint=13 | themes=abundance_scarcity, provision_resource | keywords=poverty, sustenance | q2=—
- `ب ي ت B005` ↔ `ط ع م B002` | score_hint=10 | discovery_hint=13 | themes=abundance_scarcity, provision_resource, support_dependence | keywords=sustenance | q2=—
- `ص ي ف B004` ↔ `ط ع م B005` | score_hint=8 | discovery_hint=13 | themes=life_stage_aging, reproduction_birth | keywords=fertility | q2=—
- `ر ب ب B002` ↔ `ط ع م B005` | score_hint=8 | discovery_hint=13 | themes=agriculture, life_stage_aging | keywords=agriculture | q2=—
- `ر ب ب B012` ↔ `ط ع م B010` | score_hint=8 | discovery_hint=13 | themes=agriculture, plant_vegetation | keywords=botany | q2=—
- `ر ح ل B004` ↔ `ب ي ت B001` | score_hint=18 | discovery_hint=12 | themes=architecture_construction, household_community, place_location | keywords=domesticity, settlement, shelter | q2=—
- `ع ب د B003` ↔ `ر ب ب B001` | score_hint=18 | discovery_hint=12 | themes=authority_governance, belief_revelation, religion_worship | keywords=authority, devotion, theology | q2=—
- `ر ح ل B003` ↔ `ع ب د B005` | score_hint=14 | discovery_hint=12 | themes=animal, transport, travel | keywords=animal, transport | q2=—
- `ر ح ل B005` ↔ `ر ب ب B014` | score_hint=14 | discovery_hint=12 | themes=animal, livestock, terrain_desert | keywords=desert, livestock | q2=—
- `ر ح ل B006` ↔ `ش ت و B002` | score_hint=14 | discovery_hint=12 | themes=architecture_construction, place_location, travel | keywords=settlement, travel | q2=—
- `ر ح ل B006` ↔ `ص ي ف B003` | score_hint=14 | discovery_hint=12 | themes=place_location, transport, travel | keywords=settlement, travel | q2=—
- `ص ي ف B004` ↔ `ب ي ت B002` | score_hint=14 | discovery_hint=12 | themes=family, kinship, marriage_genealogy | keywords=family, kinship | q2=—
- `ص ي ف B004` ↔ `ب ي ت B010` | score_hint=14 | discovery_hint=12 | themes=family, kinship, marriage_genealogy | keywords=family, kinship | q2=—
- `ع ب د B003` ↔ `ء م ن B003` | score_hint=14 | discovery_hint=12 | themes=belief_revelation, religion_worship, ritual | keywords=ritual, theology | q2=—
- `ع ب د B006` ↔ `ر ب ب B017` | score_hint=14 | discovery_hint=12 | themes=authority_governance, hierarchy_status, labor_work | keywords=authority, hierarchy | q2=—

## Per-root candidate activations

### ء ل ف

- `ء ل ف B001` — الألف واجتماع المئين
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ء ل ف B002` — ضم الشيء إلى الشيء والتأليف
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ء ل ف B003` — تأليف القلوب بالمقاربة والعطاء
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ء ل ف B004` — إيلاف قريش ورحلتها
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ء ل ف B005` — الألفة والأنس والملازمة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ء ل ف B006` — الألف حرف من حروف الهجاء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ر ح ل

- `ر ح ل B001` — المضي في سفر
  - activated_by_or_with: ص ي ف
  - themes: motion, navigation_route, orientation_direction
  - keywords: navigation, orientation
- `ر ح ل B002` — الرَّحْل على ظهر البعير
  - activated_by_or_with: ع ب د
  - themes: animal, material, transport, travel
  - keywords: animal, material, transport, travel
- `ر ح ل B003` — شد الرَّحْل
  - activated_by_or_with: ع ب د
  - themes: animal, transport, travel
  - keywords: animal, transport
- `ر ح ل B004` — الرَّحْل موضع النزول
  - activated_by_or_with: ب ي ت, ش ت و
  - themes: architecture_construction, household_community, migration_displacement, place_location
  - keywords: domesticity, habitation, settlement, shelter
- `ر ح ل B005` — راحلة صالحة للرحلة
  - activated_by_or_with: ر ب ب, ع ب د
  - themes: animal, force_power, livestock, stability_endurance, terrain_desert, transport, travel
  - keywords: animal, desert, endurance, livestock, transport, travel
- `ر ح ل B006` — منزل بين رحلتين
  - activated_by_or_with: ش ت و, ص ي ف
  - themes: architecture_construction, place_location, transport, travel
  - keywords: settlement, travel
- `ر ح ل B007` — إظعان من المكان
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ح ل B008` — عون الرحلة
  - activated_by_or_with: ط ع م
  - themes: hospitality_welfare, provision_resource, support_dependence
  - keywords: charity, hospitality, patronage
- `ر ح ل B009` — ركوب بالأذى
  - activated_by_or_with: ع ب د
  - themes: control_restraint, justice_judgment, violence_warfare
  - keywords: oppression, violence
- `ر ح ل B010` — وشي بصورة الرِّحال
  - activated_by_or_with: خ و ف
  - themes: craft, material, textile_clothing
  - keywords: clothing, craft, material
- `ر ح ل B011` — بياض موضع الرَّحْل
  - activated_by_or_with: ج و ع, ط ع م, ع ب د
  - themes: anatomy, animal, body, visual_appearance
  - keywords: anatomy, animal, appearance, body
- `ر ح ل B012` — كناية بأرحل الركبان
  - activated_by_or_with: ب ي ت
  - themes: kinship, sexuality
  - keywords: kinship, sexuality

### ش ت و

- `ش ت و B001` — زمن الشتاء
  - activated_by_or_with: ص ي ف
  - themes: calendar_season, habitat_ecology, time, weather_climate
  - keywords: calendar, climate, nature, seasonality, time, weather
- `ش ت و B002` — حلول الشتاء ومكانه
  - activated_by_or_with: ر ح ل, ص ي ف
  - themes: architecture_construction, calendar_season, migration_displacement, place_location, travel
  - keywords: habitation, migration, settlement, shelter, travel
- `ش ت و B003` — مطر الشتاء
  - activated_by_or_with: ج و ع, ر ب ب, ص ي ف, ط ع م
  - themes: agriculture, reproduction_birth, water_hydrology, weather_climate
  - keywords: agriculture, climate, fertility, water, weather
- `ش ت و B004` — شتاء المجاعة
  - activated_by_or_with: ب ي ت, ج و ع, ر ب ب, ط ع م
  - themes: abundance_scarcity, danger_harm, habitat_ecology, provision_resource, stability_endurance, weather_climate
  - keywords: crisis, disaster, ecology, poverty, scarcity, survival, sustenance
- `ش ت و B005` — خشونة الموضع وصدر الوادي
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ص ي ف

- `ص ي ف B001` — زمن الصَّيف
  - activated_by_or_with: ش ت و
  - themes: calendar_season, habitat_ecology, time, weather_climate
  - keywords: calendar, climate, nature, seasonality, time, weather
- `ص ي ف B002` — مطر الصَّيف
  - activated_by_or_with: ج و ع, ر ب ب, ش ت و, ط ع م
  - themes: agriculture, habitat_ecology, reproduction_birth, water_hydrology, weather_climate
  - keywords: agriculture, ecology, fertility, water, weather
- `ص ي ف B003` — الصَّيف موضعا وفعلا
  - activated_by_or_with: ب ي ت, ر ح ل, ش ت و
  - themes: calendar_season, economy, migration_displacement, place_location, provision_resource, transport, travel
  - keywords: economy, migration, provisioning, settlement, travel
- `ص ي ف B004` — ولد الكبر
  - activated_by_or_with: ب ي ت, ر ب ب, ط ع م
  - themes: family, kinship, life_stage_aging, marriage_genealogy, reproduction_birth
  - keywords: birth, family, fertility, kinship, reproduction
- `ص ي ف B005` — ميل عن القصد
  - activated_by_or_with: ر ح ل
  - themes: motion, navigation_route, orientation_direction
  - keywords: navigation, orientation
- `ص ي ف B006` — مثل الصَّيف
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ع ب د

- `ع ب د B001` — الرق والملك
  - activated_by_or_with: ر ب ب
  - themes: law
  - keywords: law
- `ع ب د B002` — الانتساب إلى الله عبدا
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ع ب د B003` — العبادة والطاعة الخاضعة
  - activated_by_or_with: ء م ن, ر ب ب
  - themes: authority_governance, belief_revelation, religion_worship, ritual, trust_loyalty
  - keywords: authority, devotion, faith, religion, ritual, theology
- `ع ب د B004` — التعبيد والاستعباد
  - activated_by_or_with: خ و ف, ر ب ب, ر ح ل, ط ع م
  - themes: control_restraint, force_power, hierarchy_status, justice_judgment, support_dependence, violence_warfare
  - keywords: coercion, control, hierarchy, oppression, power, violence
- `ع ب د B005` — التذليل والتسوية
  - activated_by_or_with: خ و ف, ر ح ل
  - themes: animal, craft, husbandry, material, stability_endurance, transport, travel
  - keywords: animal, craft, material, transport, travel
- `ع ب د B006` — التكريم والتعظيم
  - activated_by_or_with: ب ي ت, ر ب ب
  - themes: authority_governance, hierarchy_status, honor_shame, labor_work
  - keywords: authority, hierarchy, honor, status
- `ع ب د B007` — القوة والصلابة
  - activated_by_or_with: ر ح ل, ط ع م
  - themes: animal, body, force_power, physiology, stability_endurance
  - keywords: animal, body, endurance
- `ع ب د B008` — الأنفة والغضب
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ب د B009` — قلة اللبث وسرعة العدو
  - activated_by_or_with: ر ب ب, ط ع م
  - themes: motion, recreation_sport, speed, time
  - keywords: motion, movement, speed, time
- `ع ب د B010` — التفرق في الوجوه
  - activated_by_or_with: ب ي ت
  - themes: household_community, space
  - keywords: space
- `ع ب د B011` — العطب والانقطاع
  - activated_by_or_with: ر ح ل
  - themes: animal, stability_endurance, travel
  - keywords: animal, endurance, travel
- `ع ب د B012` — صَلاءة الطيب
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ر ب ب

- `ر ب ب B001` — ربوبية وملك وسيادة
  - activated_by_or_with: ط ع م, ع ب د
  - themes: authority_governance, belief_revelation, force_power, hierarchy_status, religion_worship, support_dependence, wealth_property
  - keywords: authority, devotion, hierarchy, patronage, power, property, theology
- `ر ب ب B002` — إصلاح وتربية وإتمام
  - activated_by_or_with: ط ع م
  - themes: agriculture, life_stage_aging
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
  - activated_by_or_with: ب ي ت, ص ي ف
  - themes: family, household_community, kinship, reproduction_birth
  - keywords: family, household, kinship
- `ر ب ب B006` — رُبّ خاثر وإصلاح به
  - activated_by_or_with: ب ي ت
  - themes: food_nutrition, stability_endurance, substance_texture
  - keywords: preservation
- `ر ب ب B007` — لزوم وإقامة ودوام
  - activated_by_or_with: ع ب د
  - themes: motion, time
  - keywords: motion, movement, time
- `ر ب ب B008` — رباب السحاب
  - activated_by_or_with: ج و ع, ش ت و, ص ي ف, ط ع م
  - themes: agriculture, habitat_ecology, reproduction_birth, water_hydrology, weather_climate
  - keywords: agriculture, ecology, fertility, water, weather
- `ر ب ب B009` — شاة رُبّى وحداثة
  - activated_by_or_with: ب ي ت, ص ي ف, ط ع م
  - themes: animal, food_nutrition, life_stage_aging, livestock, reproduction_birth, time
  - keywords: animal, birth, dairy, livestock, reproduction, temporality, time
- `ر ب ب B010` — ربابة تجمع القداح
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B011` — ربابة عهد وميثاق
  - activated_by_or_with: ء م ن, ط ع م, ع ب د
  - themes: finance_debt, law, obligation_contract, protection_security, trust_loyalty
  - keywords: law, protection, taxation, trust
- `ر ب ب B012` — ربة نبات
  - activated_by_or_with: ج و ع, ص ي ف, ط ع م
  - themes: agriculture, habitat_ecology, plant_vegetation
  - keywords: agriculture, botany, ecology
- `ر ب ب B013` — ماء رَبَب كثير
  - activated_by_or_with: ج و ع, ش ت و
  - themes: abundance_scarcity, habitat_ecology, provision_resource
  - keywords: ecology, sustenance
- `ر ب ب B014` — رَبْرَب قطيع
  - activated_by_or_with: ر ح ل, ط ع م
  - themes: animal, habitat_ecology, livestock, terrain_desert, wildlife
  - keywords: desert, hunting, livestock
- `ر ب ب B015` — حرف رب وربما
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B016` — رُبَى حاجة وعقدة ونعمة
  - activated_by_or_with: ط ع م
  - themes: hospitality_welfare, support_dependence
  - keywords: charity, welfare
- `ر ب ب B017` — رباني الملاحين
  - activated_by_or_with: ع ب د
  - themes: authority_governance, hierarchy_status, labor_work
  - keywords: authority, hierarchy

### ب ي ت

- `ب ي ت B001` — المأوى والمسكن
  - activated_by_or_with: ر ح ل, ع ب د
  - themes: architecture_construction, household_community, place_location, space
  - keywords: domesticity, settlement, shelter, space
- `ب ي ت B002` — أهل البيت وعياله
  - activated_by_or_with: ص ي ف
  - themes: family, identity_personhood, kinship, marriage_genealogy
  - keywords: family, genealogy, identity, kinship
- `ب ي ت B003` — بيت الشعر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ب ي ت B004` — عمل الليل وتدبيره
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ب ي ت B005` — قوت ليلة
  - activated_by_or_with: ج و ع, ش ت و, ص ي ف, ط ع م
  - themes: abundance_scarcity, economy, food_nutrition, provision_resource, stability_endurance, support_dependence
  - keywords: economy, food, need, provisioning, scarcity, subsistence, survival, sustenance
- `ب ي ت B006` — شيء بات ليلة
  - activated_by_or_with: ر ب ب
  - themes: food_nutrition, stability_endurance, substance_texture, time
  - keywords: dairy, preservation, time
- `ب ي ت B007` — القبر بيت
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ب ي ت B008` — بيت الشرف
  - activated_by_or_with: ع ب د
  - themes: hierarchy_status, honor_shame, identity_personhood, kinship, marriage_genealogy
  - keywords: genealogy, hierarchy, honor, identity, status
- `ب ي ت B009` — جوار بيت بيت
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ب ي ت B010` — بيت الزواج
  - activated_by_or_with: ر ب ب, ر ح ل, ص ي ف
  - themes: family, household_community, kinship, marriage_genealogy, sexuality
  - keywords: family, household, kinship, sexuality

### ط ع م

- `ط ع م B001` — ذوق الشيء وتناوله
  - activated_by_or_with: ب ي ت, ج و ع
  - themes: body, desire_appetite, food_nutrition, provision_resource, support_dependence
  - keywords: appetite, body, food, need, nutrition, subsistence
- `ط ع م B002` — إطعام الغير وطلب الطعام
  - activated_by_or_with: ب ي ت, ج و ع, ر ب ب, ر ح ل, ش ت و
  - themes: abundance_scarcity, hospitality_welfare, provision_resource, support_dependence
  - keywords: charity, hospitality, poverty, sustenance, welfare
- `ط ع م B003` — استطعام الكلام وفتح القراءة
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ط ع م B004` — رزق ومعاش وحسن حال
  - activated_by_or_with: ب ي ت, ر ب ب, ر ح ل
  - themes: economy, finance_debt, hospitality_welfare, provision_resource, stability_endurance, support_dependence, wealth_property
  - keywords: economy, hospitality, patronage, property, subsistence, taxation
- `ط ع م B005` — إدراك الثمر وأخذ الطعم
  - activated_by_or_with: ر ب ب, ش ت و, ص ي ف
  - themes: agriculture, life_stage_aging, plant_vegetation, reproduction_birth
  - keywords: agriculture, botany, fertility
- `ط ع م B006` — آلة الصيد التي تطعم صاحبها
  - activated_by_or_with: ر ب ب
  - themes: animal, habitat_ecology, wildlife
  - keywords: hunting
- `ط ع م B007` — سمن الحيوان وطعم الشحم
  - activated_by_or_with: ج و ع, ر ب ب, ر ح ل, ع ب د
  - themes: anatomy, animal, body, food_nutrition, livestock, physiology
  - keywords: anatomy, animal, body, livestock, nutrition, physiology
- `ط ع م B008` — طعم العقل والقيمة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ط ع م B009` — مستطعم الفرس وطلب جريه
  - activated_by_or_with: ع ب د
  - themes: motion, recreation_sport, speed
  - keywords: motion, speed
- `ط ع م B010` — إطعام الغصن وقبول الوصل
  - activated_by_or_with: ر ب ب
  - themes: agriculture, plant_vegetation
  - keywords: botany
- `ط ع م B011` — القدرة على الشيء
  - activated_by_or_with: ع ب د
  - themes: control_restraint, force_power
  - keywords: control, power
- `ط ع م B012` — الأخذ بالمطعمة عند الخنق
  - activated_by_or_with: خ و ف
  - themes: conflict
  - keywords: conflict
- `ط ع م B013` — التطاعم بالفم
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ط ع م B014` — تتابع الخلق
  - activated_by_or_with: ر ب ب
  - themes: reproduction_birth, time
  - keywords: temporality, time

### ج و ع

- `ج و ع B001` — خلو البطن من الطعام
  - activated_by_or_with: ب ي ت, ط ع م
  - themes: abundance_scarcity, body, desire_appetite, food_nutrition, physiology, stability_endurance, support_dependence
  - keywords: appetite, body, need, nutrition, physiology, scarcity, survival
- `ج و ع B002` — زمن يعم فيه الجوع
  - activated_by_or_with: ب ي ت, ر ب ب, ش ت و, ص ي ف, ط ع م
  - themes: abundance_scarcity, agriculture, danger_harm, habitat_ecology, provision_resource, stability_endurance, weather_climate
  - keywords: agriculture, climate, crisis, disaster, ecology, poverty, scarcity, survival, sustenance
- `ج و ع B003` — إحداث الجوع أو قصده
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج و ع B004` — استعارة الخلو والنحول
  - activated_by_or_with: ر ح ل
  - themes: body, visual_appearance
  - keywords: appearance, body

### ء م ن

- `ء م ن B001` — سكون القلب في أمن وثقة
  - activated_by_or_with: ر ب ب
  - themes: obligation_contract, protection_security, trust_loyalty
  - keywords: protection, trust
- `ء م ن B002` — تصديق يطمئن إليه القلب
  - activated_by_or_with: ع ب د
  - themes: authority_governance, belief_revelation, religion_worship, trust_loyalty
  - keywords: faith, religion
- `ء م ن B003` — قول آمين طلبا للاستجابة
  - activated_by_or_with: ع ب د
  - themes: belief_revelation, religion_worship, ritual
  - keywords: ritual, theology

### خ و ف

- `خ و ف B001` — ذعر يتوقع المكروه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ و ف B002` — إدخال الخوف في الغير
  - activated_by_or_with: ع ب د
  - themes: control_restraint, force_power
  - keywords: coercion, control
- `خ و ف B003` — مغالبة في الخوف
  - activated_by_or_with: ط ع م
  - themes: conflict
  - keywords: conflict
- `خ و ف B004` — نقص يأخذ من الشيء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ و ف B005` — ظهور الخوف على الإنسان
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ و ف B006` — خافة العسال والسقاء
  - activated_by_or_with: ر ح ل, ع ب د
  - themes: craft, husbandry, material, textile_clothing, transport
  - keywords: clothing, craft, material, transport

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
