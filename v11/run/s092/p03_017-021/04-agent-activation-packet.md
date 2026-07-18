# v11 Activation Packet — S92:17-21

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_17: وَسَيُجَنَّبُهَا ٱلْأَتْقَى
- verse_18: ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
- verse_19: وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
- verse_20: إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- verse_21: وَلَسَوْفَ يَرْضَىٰ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ج ن ب → و ق ي → ء ت ي → م و ل → ز ك و → ء ح د → ع ن د → ن ع م → ج ز ي → ب غ ي → و ج ه → ر ب ب → ع ل و → ر ض و

## Branch inventory summary

- ج ن ب: 12 branches (11 with Qnet bridge-theme nodes; 1 Furūq-only)
- و ق ي: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء ت ي: 13 branches (13 with Qnet bridge-theme nodes; 0 Furūq-only)
- م و ل: 2 branches (2 with Qnet bridge-theme nodes; 0 Furūq-only)
- ز ك و: 5 branches (4 with Qnet bridge-theme nodes; 1 Furūq-only)
- ء ح د: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- ع ن د: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن ع م: 13 branches (13 with Qnet bridge-theme nodes; 0 Furūq-only)
- ج ز ي: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- ب غ ي: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- و ج ه: 15 branches (14 with Qnet bridge-theme nodes; 1 Furūq-only)
- ر ب ب: 17 branches (17 with Qnet bridge-theme nodes; 0 Furūq-only)
- ع ل و: 12 branches (11 with Qnet bridge-theme nodes; 1 Furūq-only)
- ر ض و: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)

## QAC-first root resolution audit

- ج ن ب | qac_keys=جنب | status=resolved | matches=root_000262
- و ق ي | qac_keys=وقي | status=resolved | matches=root_001677
- ء ت ي | qac_keys=ءتي | status=resolved | matches=root_000009
- م و ل | qac_keys=مول | status=resolved | matches=root_001457
- ز ك و | qac_keys=زكو | status=resolved | matches=root_000637
- ء ح د | qac_keys=ءحد | status=resolved | matches=root_000017
- ع ن د | qac_keys=عند | status=resolved | matches=root_001052
- ن ع م | qac_keys=نعم | status=resolved | matches=root_001525
- ج ز ي | qac_keys=جزي | status=resolved | matches=root_000244
- ب غ ي | qac_keys=بغي | status=resolved | matches=root_000138
- و ج ه | qac_keys=وجه | status=resolved | matches=root_001630
- ر ب ب | qac_keys=ربب | status=resolved | matches=root_000532
- ع ل و | qac_keys=علو | status=resolved | matches=root_001042
- ر ض و | qac_keys=رضو | status=resolved | matches=root_000569

## Top candidate bridges

- `و ق ي B005` ↔ `ن ع م B006` | score_hint=32 | discovery_hint=14 | themes=animal, habitat_ecology, naming_classification, wildlife | keywords=animal, bird, nature, taxonomy, wildlife, zoology | q2=—
- `و ج ه B006` ↔ `ع ل و B002` | score_hint=28 | discovery_hint=14 | themes=authority_governance, hierarchy_status, honor_shame, social_relations | keywords=authority, hierarchy, leadership, reputation, society | q2=—
- `ج ز ي B005` ↔ `ر ض و B005` | score_hint=26 | discovery_hint=15 | themes=conflict, force_power, hierarchy_status | keywords=competition, conflict, dominance, hierarchy, power | q2=—
- `ج ن ب B001` ↔ `ع ل و B001` | score_hint=24 | discovery_hint=13 | themes=body, orientation_direction, space, terrain_desert | keywords=body, orientation, space, topography | q2=—
- `ج ن ب B007` ↔ `و ق ي B003` | score_hint=24 | discovery_hint=14 | themes=anatomy, animal, health_medicine, suffering_hardship | keywords=anatomy, animal, pain, veterinary | q2=—
- `ج ن ب B008` ↔ `ن ع م B005` | score_hint=24 | discovery_hint=15 | themes=animal, economy, husbandry, provision_resource | keywords=animal, economy, pastoralism, subsistence | q2=—
- `و ق ي B005` ↔ `م و ل B002` | score_hint=24 | discovery_hint=14 | themes=animal, language_speech, naming_classification, wildlife | keywords=animal, nomenclature, taxonomy, zoology | q2=—
- `ب غ ي B003` ↔ `ع ل و B003` | score_hint=24 | discovery_hint=15 | themes=ethics_morality, force_power, justice_judgment, violence_warfare | keywords=ethics, injustice, power, violence | q2=—
- `ب غ ي B006` ↔ `ر ب ب B008` | score_hint=24 | discovery_hint=16 | themes=agriculture, habitat_ecology, water_hydrology, weather_climate | keywords=agriculture, meteorology, water, weather | q2=—
- `ج ن ب B003` ↔ `ع ن د B002` | score_hint=22 | discovery_hint=14 | themes=boundary, motion, social_relations | keywords=boundary, movement, separation, sociality | q2=—
- `ج ن ب B006` ↔ `ن ع م B009` | score_hint=22 | discovery_hint=15 | themes=habitat_ecology, orientation_direction, weather_climate | keywords=atmosphere, climate, direction, weather | q2=—
- `ج ن ب B007` ↔ `ب غ ي B004` | score_hint=22 | discovery_hint=15 | themes=body, disease_injury, health_medicine | keywords=body, injury, medicine, pathology | q2=—
- `ء ت ي B009` ↔ `ن ع م B012` | score_hint=22 | discovery_hint=14 | themes=motion, transport, travel | keywords=locomotion, movement, transport, travel | q2=—
- `ء ح د B005` ↔ `ع ن د B002` | score_hint=22 | discovery_hint=14 | themes=boundary, motion, social_relations | keywords=motion, movement, separation, sociality | q2=—
- `ج ن ب B011` ↔ `و ق ي B001` | score_hint=20 | discovery_hint=14 | themes=boundary, protection_security | keywords=boundary, defense, protection, safety | q2=—
- `ء ت ي B008` ↔ `ج ز ي B004` | score_hint=20 | discovery_hint=15 | themes=authority_governance, finance_debt | keywords=finance, governance, revenue, taxation | q2=—
- `ج ن ب B003` ↔ `ء ت ي B006` | score_hint=20 | discovery_hint=13 | themes=boundary, kinship, migration_displacement, social_relations | keywords=boundary, migration, sociality | q2=—
- `ج ن ب B006` ↔ `ر ب ب B008` | score_hint=20 | discovery_hint=16 | themes=agriculture, habitat_ecology, sky_astronomy, weather_climate | keywords=agriculture, sky, weather | q2=—
- `ج ن ب B012` ↔ `ء ت ي B009` | score_hint=20 | discovery_hint=13 | themes=anatomy, animal, husbandry, motion | keywords=anatomy, animal, movement | q2=—
- `و ق ي B003` ↔ `ء ت ي B009` | score_hint=20 | discovery_hint=13 | themes=anatomy, animal, motion, transport | keywords=anatomy, animal, locomotion | q2=—
- `ء ت ي B013` ↔ `ع ل و B004` | score_hint=20 | discovery_hint=14 | themes=agency_action, authority_governance, capacity_ability, force_power | keywords=agency, capacity, power | q2=—
- `ج ن ب B001` ↔ `ء ت ي B010` | score_hint=18 | discovery_hint=12 | themes=boundary, geography_landscape, orientation_direction | keywords=boundary, geography, orientation | q2=—
- `ج ن ب B001` ↔ `و ج ه B001` | score_hint=18 | discovery_hint=12 | themes=anatomy, body, orientation_direction | keywords=anatomy, body, orientation | q2=—
- `ج ن ب B003` ↔ `ء ح د B005` | score_hint=18 | discovery_hint=13 | themes=boundary, motion, social_relations | keywords=movement, separation, sociality | q2=—
- `ج ن ب B003` ↔ `و ج ه B014` | score_hint=18 | discovery_hint=13 | themes=boundary, motion, social_relations | keywords=boundary, movement, sociality | q2=—
- `ج ن ب B006` ↔ `ب غ ي B006` | score_hint=18 | discovery_hint=15 | themes=agriculture, habitat_ecology, weather_climate | keywords=agriculture, climate, weather | q2=—
- `ج ن ب B007` ↔ `ع ل و B010` | score_hint=18 | discovery_hint=14 | themes=anatomy, animal, body | keywords=anatomy, animal, body | q2=—
- `ج ن ب B008` ↔ `ر ب ب B009` | score_hint=18 | discovery_hint=14 | themes=animal, food_nutrition, livestock | keywords=animal, dairy, livestock | q2=—
- `و ق ي B002` ↔ `ز ك و B002` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, purity_cleansing, religion_worship | keywords=ethics, purity, religion | q2=—
- `ء ت ي B006` ↔ `ع ن د B002` | score_hint=18 | discovery_hint=13 | themes=boundary, household_community, social_relations | keywords=boundary, community, sociality | q2=—
- `ء ت ي B007` ↔ `ز ك و B001` | score_hint=18 | discovery_hint=14 | themes=abundance_scarcity, agriculture, reproduction_birth | keywords=abundance, agriculture, fertility | q2=—
- `ء ت ي B007` ↔ `ب غ ي B006` | score_hint=18 | discovery_hint=14 | themes=abundance_scarcity, agriculture, water_hydrology | keywords=abundance, agriculture, water | q2=—
- `ء ت ي B007` ↔ `ر ب ب B008` | score_hint=18 | discovery_hint=15 | themes=agriculture, reproduction_birth, water_hydrology | keywords=agriculture, fertility, water | q2=—
- `ء ت ي B008` ↔ `ج ز ي B002` | score_hint=18 | discovery_hint=14 | themes=authority_governance, finance_debt, obligation_contract | keywords=finance, obligation, payment | q2=—
- `ء ت ي B010` ↔ `ع ن د B002` | score_hint=18 | discovery_hint=13 | themes=boundary, navigation_route, orientation_direction | keywords=boundary, navigation, orientation | q2=—
- `ء ت ي B010` ↔ `و ج ه B002` | score_hint=18 | discovery_hint=13 | themes=geography_landscape, navigation_route, orientation_direction | keywords=geography, navigation, orientation | q2=—
- `ء ت ي B012` ↔ `ر ب ب B009` | score_hint=18 | discovery_hint=14 | themes=animal, livestock, reproduction_birth | keywords=animal, livestock, reproduction | q2=—
- `م و ل B002` ↔ `ن ع م B006` | score_hint=18 | discovery_hint=13 | themes=animal, naming_classification, wildlife | keywords=animal, taxonomy, zoology | q2=—
- `ز ك و B001` ↔ `ب غ ي B006` | score_hint=18 | discovery_hint=13 | themes=abundance_scarcity, agriculture, habitat_ecology | keywords=abundance, agriculture, nature | q2=—
- `ء ح د B006` ↔ `ر ض و B007` | score_hint=18 | discovery_hint=13 | themes=geography_landscape, naming_classification, place_location | keywords=geography, naming, place | q2=—
- `ع ن د B002` ↔ `و ج ه B002` | score_hint=18 | discovery_hint=13 | themes=motion, navigation_route, orientation_direction | keywords=movement, navigation, orientation | q2=—
- `ع ن د B002` ↔ `و ج ه B014` | score_hint=18 | discovery_hint=13 | themes=boundary, motion, social_relations | keywords=boundary, movement, sociality | q2=—
- `ع ن د B002` ↔ `ع ل و B001` | score_hint=18 | discovery_hint=13 | themes=motion, orientation_direction, surface_shape | keywords=geometry, motion, orientation | q2=—
- `ع ن د B002` ↔ `ع ل و B006` | score_hint=18 | discovery_hint=13 | themes=household_community, motion, social_relations | keywords=motion, movement, sociality | q2=—
- `ن ع م B001` ↔ `ر ب ب B016` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, hospitality_welfare, support_dependence | keywords=charity, ethics, welfare | q2=—
- `ب غ ي B004` ↔ `ع ل و B011` | score_hint=18 | discovery_hint=14 | themes=body, disease_injury, health_medicine | keywords=body, disease, medicine | q2=—
- `ر ب ب B010` ↔ `ع ل و B009` | score_hint=18 | discovery_hint=18 | themes=proof_uncertainty, storage_vessels, tools_equipment, weaponry | keywords=tool, weapon | q2=—
- `ج ن ب B009` ↔ `ن ع م B001` | score_hint=16 | discovery_hint=12 | themes=abundance_scarcity, ethics_morality | keywords=abundance, ethics, fortune | q2=—
- `ج ن ب B012` ↔ `ر ب ب B007` | score_hint=16 | discovery_hint=13 | themes=animal, motion | keywords=animal, motion, movement | q2=—
- `ء ت ي B005` ↔ `ب غ ي B006` | score_hint=16 | discovery_hint=14 | themes=water_hydrology, weather_climate | keywords=flood, storm, weather | q2=—
- `ز ك و B002` ↔ `ع ن د B001` | score_hint=16 | discovery_hint=12 | themes=ethics_morality, religion_worship | keywords=ethics, morality, religion | q2=—
- `ز ك و B002` ↔ `ر ب ب B003` | score_hint=16 | discovery_hint=13 | themes=ethics_morality, religion_worship | keywords=ethics, religion, spirituality | q2=—
- `ء ح د B005` ↔ `ع ل و B006` | score_hint=16 | discovery_hint=13 | themes=motion, social_relations | keywords=motion, movement, sociality | q2=—
- `ن ع م B009` ↔ `ب غ ي B006` | score_hint=16 | discovery_hint=14 | themes=habitat_ecology, weather_climate | keywords=climate, nature, weather | q2=—
- `ر ب ب B015` ↔ `ع ل و B012` | score_hint=16 | discovery_hint=13 | themes=grammar_expression, language_speech | keywords=grammar, semantics, syntax | q2=—
- `ج ن ب B008` ↔ `م و ل B001` | score_hint=16 | discovery_hint=12 | themes=abundance_scarcity, economy, husbandry, provision_resource | keywords=economy, pastoralism | q2=—
- `م و ل B001` ↔ `ن ع م B005` | score_hint=16 | discovery_hint=13 | themes=economy, husbandry, provision_resource, wealth_property | keywords=economy, pastoralism | q2=—
- `ن ع م B006` ↔ `ر ب ب B014` | score_hint=16 | discovery_hint=12 | themes=animal, habitat_ecology, terrain_desert, wildlife | keywords=desert, zoology | q2=—
- `ع ل و B004` ↔ `ر ض و B005` | score_hint=16 | discovery_hint=13 | themes=capacity_ability, conflict, force_power, violence_warfare | keywords=conflict, power | q2=—
- `ج ن ب B010` ↔ `ن ع م B005` | score_hint=15 | discovery_hint=18 | themes=agriculture, pasture_forage, provision_resource | keywords=agriculture, pasture | q2=—
- `و ق ي B002` ↔ `ج ز ي B001` | score_hint=15 | discovery_hint=15 | themes=afterlife_eschatology, ethics_morality, justice_judgment | keywords=accountability, afterlife | q2=—
- `ج ن ب B001` ↔ `ء ح د B006` | score_hint=14 | discovery_hint=11 | themes=geography_landscape, place_location, terrain_desert | keywords=geography, topography | q2=—
- `ج ن ب B001` ↔ `ن ع م B007` | score_hint=14 | discovery_hint=11 | themes=anatomy, geography_landscape, terrain_desert | keywords=anatomy, topography | q2=—
- `ج ن ب B001` ↔ `ع ل و B005` | score_hint=14 | discovery_hint=11 | themes=orientation_direction, place_location, space | keywords=orientation, space | q2=—
- `ج ن ب B003` ↔ `و ق ي B001` | score_hint=14 | discovery_hint=12 | themes=boundary, danger_harm, protection_security | keywords=boundary, protection | q2=—
- `ج ن ب B003` ↔ `ن ع م B008` | score_hint=14 | discovery_hint=12 | themes=migration_displacement, motion, social_relations | keywords=migration, movement | q2=—
- `ج ن ب B005` ↔ `ء ت ي B009` | score_hint=14 | discovery_hint=12 | themes=animal, motion, transport | keywords=animal, transport | q2=—
- `ج ن ب B005` ↔ `ب غ ي B007` | score_hint=14 | discovery_hint=12 | themes=animal, motion, recreation_sport | keywords=animal, sport | q2=—
- `ج ن ب B007` ↔ `ع ل و B011` | score_hint=14 | discovery_hint=13 | themes=body, disease_injury, health_medicine | keywords=body, medicine | q2=—
- `ج ن ب B008` ↔ `ء ت ي B012` | score_hint=14 | discovery_hint=12 | themes=animal, husbandry, livestock | keywords=animal, livestock | q2=—
- `ج ن ب B008` ↔ `ر ب ب B014` | score_hint=14 | discovery_hint=12 | themes=animal, husbandry, livestock | keywords=livestock, pastoralism | q2=—
- `ج ن ب B009` ↔ `ن ع م B002` | score_hint=14 | discovery_hint=13 | themes=abundance_scarcity, value_quality, wealth_property | keywords=prosperity, wealth | q2=—
- `ج ن ب B010` ↔ `ر ب ب B012` | score_hint=14 | discovery_hint=14 | themes=agriculture, habitat_ecology, plant_vegetation | keywords=agriculture, ecology | q2=—
- `ج ن ب B012` ↔ `و ق ي B003` | score_hint=14 | discovery_hint=12 | themes=anatomy, animal, motion | keywords=anatomy, animal | q2=—
- `و ق ي B002` ↔ `ع ن د B001` | score_hint=14 | discovery_hint=11 | themes=ethics_morality, justice_judgment, religion_worship | keywords=ethics, religion | q2=—
- `و ق ي B005` ↔ `ر ب ب B014` | score_hint=14 | discovery_hint=12 | themes=animal, habitat_ecology, wildlife | keywords=ecology, zoology | q2=—
- `ء ت ي B005` ↔ `ر ب ب B007` | score_hint=14 | discovery_hint=13 | themes=geography_landscape, motion, weather_climate | keywords=geography, weather | q2=—
- `ء ت ي B006` ↔ `ن ع م B008` | score_hint=14 | discovery_hint=12 | themes=household_community, migration_displacement, social_relations | keywords=migration, society | q2=—
- `ء ت ي B007` ↔ `ر ب ب B013` | score_hint=14 | discovery_hint=13 | themes=abundance_scarcity, provision_resource, water_hydrology | keywords=abundance, resource | q2=—
- `ء ت ي B008` ↔ `ج ز ي B003` | score_hint=14 | discovery_hint=13 | themes=authority_governance, finance_debt, obligation_contract | keywords=finance, obligation | q2=—

## Per-root candidate activations

### ج ن ب

- `ج ن ب B001` — الجنب جانب الجسد وناحية الشيء
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: anatomy, body, boundary, geography_landscape, material, orientation_direction, place_location, space, terrain_desert
  - keywords: anatomy, body, boundary, geography, leather, material, orientation, settlement, space, topography
- `ج ن ب B002` — الجنب قرب ومجاورة على الجانب
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: belief_revelation, ethics_morality, household_community, place_location, religion_worship, social_relations
  - keywords: community, devotion, ethics, guidance, relation, society, theology
- `ج ن ب B003` — المجانبة إبعاد واعتزال وغربة
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: boundary, danger_harm, kinship, migration_displacement, motion, protection_security, social_relations
  - keywords: boundary, kinship, migration, movement, protection, separation, sociality
- `ج ن ب B004` — الجنابة حالة تجنب مواضع الصلاة
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ج ن ب B005` — التجنيب قيادة شيء إلى الجنب
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: animal, conflict, control_restraint, motion, protection_security, recreation_sport, social_relations, transport
  - keywords: animal, competition, control, sport, transport
- `ج ن ب B006` — الجنوب ريح من جهة مخصوصة
  - activated_by_or_with: ء ت ي, ب غ ي, ر ب ب, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: agriculture, habitat_ecology, orientation_direction, sky_astronomy, travel, weather_climate
  - keywords: agriculture, atmosphere, climate, direction, environment, sky, travel, weather
- `ج ن ب B007` — داء الجنب وأثره في البدن
  - activated_by_or_with: ء ت ي, ب غ ي, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: anatomy, animal, body, desire_appetite, disease_injury, health_medicine, suffering_hardship
  - keywords: anatomy, animal, body, injury, medicine, pain, pathology, veterinary
- `ج ن ب B008` — التجنيب قلة لبن الإبل
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ق ي
  - themes: abundance_scarcity, animal, calendar_season, economy, food_nutrition, husbandry, livestock, provision_resource
  - keywords: animal, dairy, economy, food, livestock, pastoralism, season, subsistence
- `ج ن ب B009` — المجنب خير أو شر كثير
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: abundance_scarcity, ethics_morality, measurement, quantity_number, suffering_hardship, value_quality, wealth_property
  - keywords: abundance, ethics, fortune, measure, morality, prosperity, quantity, value, wealth
- `ج ن ب B010` — الجنبة نبت متوسط مستقل
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ر ب ب, ز ك و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: agriculture, calendar_season, habitat_ecology, livestock, pasture_forage, plant_vegetation, provision_resource, stability_endurance
  - keywords: agriculture, ecology, livestock, pasture, plant, resource, season
- `ج ن ب B011` — المجنب وقاء إلى الجنب
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ر ب ب, ر ض و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: body, boundary, protection_security, tools_equipment, violence_warfare
  - keywords: body, boundary, defense, equipment, protection, safety, tool, warfare
- `ج ن ب B012` — التجنيب تباعد في هيئة القوائم
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ر ب ب, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: anatomy, animal, form_structure, husbandry, motion, reasoning_decision, value_quality
  - keywords: anatomy, animal, evaluation, morphology, motion, movement

### و ق ي

- `و ق ي B001` — دفع الضرر بوقاية
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ع ل و, ع ن د, ن ع م, و ج ه
  - themes: architecture_construction, boundary, danger_harm, protection_security
  - keywords: boundary, defense, protection, risk, safety, security
- `و ق ي B002` — جعل النفس في وقاية
  - activated_by_or_with: ء ت ي, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه
  - themes: afterlife_eschatology, control_restraint, ethics_morality, justice_judgment, purity_cleansing, religion_worship
  - keywords: accountability, afterlife, devotion, ethics, purity, religion
- `و ق ي B003` — توقي الدابة من وجع الحافر
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه
  - themes: anatomy, animal, health_medicine, motion, protection_security, suffering_hardship, terrain_desert, tools_equipment, transport
  - keywords: anatomy, animal, equipment, locomotion, pain, veterinary
- `و ق ي B004` — الأوقية وزن معلوم
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, م و ل, ن ع م, و ج ه
  - themes: commerce_exchange, economy, finance_debt, measurement, quantity_number, value_quality
  - keywords: accounting, economy, measurement, quantity
- `و ق ي B005` — الواقي اسم للصرد
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه
  - themes: animal, habitat_ecology, language_speech, naming_classification, wildlife
  - keywords: animal, bird, ecology, language, naming, nature, nomenclature, taxonomy, wildlife, zoology

### ء ت ي

- `ء ت ي B001` — الإتيان والمجيء
  - activated_by_or_with: ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: agency_action, authority_governance, belief_revelation, change_transition, cognition, containment_access, motion, sequence_cycle
  - keywords: access, agency, command, movement, providence
- `ء ت ي B002` — الإيتاء والإعطاء
  - activated_by_or_with: ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: commerce_exchange, hospitality_welfare, motion, provision_resource, wealth_property
  - keywords: exchange, generosity, gift, ownership, transfer
- `ء ت ي B003` — مأتى الأمر وتهيؤه
  - activated_by_or_with: ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه
  - themes: agency_action, capacity_ability, change_transition, containment_access, hospitality_welfare, labor_work, orientation_direction, reasoning_decision, social_relations
  - keywords: access, cooperation, preparation, service
- `ء ت ي B004` — مجرى الماء وتسليك سبيله
  - activated_by_or_with: ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: architecture_construction, control_restraint, craft, measurement, water_hydrology
  - keywords: hydrology, infrastructure, measurement, water
- `ء ت ي B005` — السيل الآتي من غير البلد
  - activated_by_or_with: ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: danger_harm, geography_landscape, motion, water_hydrology, weather_climate
  - keywords: disaster, flood, geography, hydrology, storm, transfer, weather
- `ء ت ي B006` — الغريب الداخل في غير قومه
  - activated_by_or_with: ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: boundary, household_community, identity_personhood, kinship, migration_displacement, social_relations
  - keywords: belonging, boundary, community, identity, migration, sociality, society
- `ء ت ي B007` — خروج النماء والنتاج
  - activated_by_or_with: ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه
  - themes: abundance_scarcity, agriculture, food_nutrition, harvest_cultivation, labor_work, provision_resource, reproduction_birth, water_hydrology
  - keywords: abundance, agriculture, dairy, fertility, resource, water
- `ء ت ي B008` — الإتاوة المؤداة
  - activated_by_or_with: ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: authority_governance, control_restraint, deception_corruption, finance_debt, obligation_contract
  - keywords: corruption, finance, governance, obligation, payment, revenue, taxation
- `ء ت ي B009` — رجع يدي الناقة في السير
  - activated_by_or_with: ء ح د, ب غ ي, ج ن ب, ر ب ب, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: anatomy, animal, husbandry, motion, posture_embodiment, transport, travel
  - keywords: anatomy, animal, locomotion, movement, pastoralism, transport, travel, zoology
- `ء ت ي B010` — الميتاء طريق ومحاذاة
  - activated_by_or_with: ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: architecture_construction, boundary, containment_access, geography_landscape, navigation_route, orientation_direction, transport, travel
  - keywords: access, boundary, direction, geography, infrastructure, navigation, orientation, travel
- `ء ت ي B011` — إتيان البلاء والهلاك
  - activated_by_or_with: ب غ ي, ج ن ب, ر ب ب, ر ض و, ع ل و, ن ع م, و ج ه, و ق ي
  - themes: danger_harm, disease_injury, loss_absence, mortality_death, violence_warfare
  - keywords: disaster, loss, mortality, violence, warfare
- `ء ت ي B012` — استئتاء الناقة
  - activated_by_or_with: ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: animal, husbandry, intention_character, livestock, physiology, reproduction_birth, sexuality
  - keywords: animal, biology, fertility, livestock, reproduction, sexuality
- `ء ت ي B013` — نَفاذ الرجل
  - activated_by_or_with: ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: agency_action, authority_governance, capacity_ability, force_power, intention_character, value_quality
  - keywords: agency, capacity, character, leadership, performance, power

### م و ل

- `م و ل B001` — اتخاذ المال وكثرته
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ن د, ن ع م, و ق ي
  - themes: abundance_scarcity, economy, finance_debt, husbandry, provision_resource, support_dependence, wealth_property
  - keywords: economy, finance, ownership, pastoralism, patronage, property, prosperity, resource
- `م و ل B002` — المُولة العنكبوت
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: animal, form_structure, language_speech, naming_classification, wildlife
  - keywords: animal, nomenclature, taxonomy, zoology

### ز ك و

- `ز ك و B001` — النماء والزيادة
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: abundance_scarcity, agriculture, belief_revelation, growth_decay, habitat_ecology, physiology, reproduction_birth
  - keywords: abundance, agriculture, biology, blessing, fertility, nature, prosperity
- `ز ك و B002` — الطهارة والصلاح
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: belief_revelation, ethics_morality, food_nutrition, law, purity_cleansing, religion_worship, ritual
  - keywords: ethics, food, law, morality, purity, religion, ritual, spirituality, virtue
- `ز ك و B003` — زكاة المال والصدقة
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ز ك و B004` — الملاءمة واللياقة
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: ethics_morality, health_medicine, justice_judgment, rhetoric_discourse, social_relations, value_quality
  - keywords: fitness, judgment, norm, relation, sociality
- `ز ك و B005` — الزوج والشفع
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: anatomy, justice_judgment, quantity_number, reasoning_decision, recreation_sport
  - keywords: choice, contrast, game, number

### ء ح د

- `ء ح د B001` — الأَحَدِيَّة والوَحْدَة
  - activated_by_or_with: ء ت ي, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: belief_revelation, boundary, identity_personhood, language_speech, social_relations, value_quality
  - keywords: identity, theology
- `ء ح د B002` — استغراق النفي
  - activated_by_or_with: ء ت ي, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: boundary, grammar_expression, quantity_number, reasoning_decision, rhetoric_discourse, value_quality
  - keywords: logic, quantification, reference
- `ء ح د B003` — الواحد في العد والتركيب
  - activated_by_or_with: ء ت ي, ج ز ي, ج ن ب, ر ب ب, ز ك و, ع ل و, ن ع م, و ج ه, و ق ي
  - themes: measurement, quantity_number, sequence_cycle
  - keywords: measurement, number, quantity, sequence
- `ء ح د B004` — الأول والإضافة
  - activated_by_or_with: ء ت ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: calendar_season, naming_classification, politics_order, quantity_number, sequence_cycle, time
  - keywords: naming, order, sequence, time
- `ء ح د B005` — الانفراد والتفرق آحادا
  - activated_by_or_with: ء ت ي, ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: agency_action, boundary, identity_personhood, motion, provision_resource, social_relations
  - keywords: agency, motion, movement, separation, sociality
- `ء ح د B006` — جبل أُحُد
  - activated_by_or_with: ء ت ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ع ل و, م و ل, ن ع م, و ج ه, و ق ي
  - themes: geography_landscape, naming_classification, place_location, terrain_desert
  - keywords: geography, naming, place, topography

### ع ن د

- `ع ن د B001` — عدول عن الاستقامة وممانعة للحق
  - activated_by_or_with: ء ت ي, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ن ع م, و ج ه, و ق ي
  - themes: authority_governance, cognition, conflict, ethics_morality, intention_character, justice_judgment, proof_uncertainty, religion_worship
  - keywords: authority, cognition, conflict, ethics, justice, morality, religion
- `ع ن د B002` — ميل إلى ناحية وانفراد عن الجماعة
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ن ع م, و ج ه, و ق ي
  - themes: boundary, household_community, livestock, motion, navigation_route, orientation_direction, social_relations, surface_shape
  - keywords: boundary, community, geometry, motion, movement, navigation, orientation, separation, sociality
- `ع ن د B003` — سيلان عاند جانح
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, م و ل, ن ع م, و ج ه, و ق ي
  - themes: abundance_scarcity, body, control_restraint, motion, stability_endurance, substance_texture, water_hydrology, weather_climate
  - keywords: body, motion, weather
- `ع ن د B004` — قرب وحضور عند الشيء
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ن ع م, و ج ه
  - themes: cognition, hierarchy_status, hospitality_welfare, social_relations, space, time
  - keywords: cognition, favor, hierarchy, relation, space, status, time
- `ع ن د B005` — انعدام البد والحيلة
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ن ع م, و ج ه, و ق ي
  - themes: agency_action, control_restraint, grammar_expression, obligation_contract, reasoning_decision
  - keywords: agency, choice, modality
- `ع ن د B006` — إغراء عندك بالأخذ
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, م و ل, ن ع م, و ج ه, و ق ي
  - themes: agency_action, authority_governance, communication, knowledge_learning, language_speech, obligation_contract, rhetoric_discourse, wealth_property
  - keywords: acquisition, command, communication, obligation, persuasion, speech

### ن ع م

- `ن ع م B001` — حسن الحال والنعمة
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, و ج ه, و ق ي
  - themes: abundance_scarcity, belief_revelation, commerce_exchange, ethics_morality, hospitality_welfare, support_dependence
  - keywords: abundance, charity, ethics, fortune, generosity, patronage, providence, reciprocity, welfare
- `ن ع م B002` — اللين والنعومة ورفاه العيش
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, و ج ه, و ق ي
  - themes: abundance_scarcity, body, desire_appetite, health_medicine, hierarchy_status, material, perception, value_quality, wealth_property
  - keywords: body, comfort, material, prosperity, sensation, status, wealth
- `ن ع م B003` — مدح الشيء بنعم
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, و ج ه, و ق ي
  - themes: grammar_expression, honor_shame, justice_judgment, language_speech, orientation_direction, rhetoric_discourse, value_quality
  - keywords: evaluation, grammar, judgment, rhetoric, speech
- `ن ع م B004` — الجواب بنعم والتصديق
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, و ج ه, و ق ي
  - themes: communication, grammar_expression, language_speech, obligation_contract, proof_uncertainty, reasoning_decision, social_relations
  - keywords: agreement, communication, interaction, language, logic, modality
- `ن ع م B005` — مال الأنعام والإبل
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ز ك و, ع ل و, ع ن د, م و ل, و ج ه, و ق ي
  - themes: agriculture, animal, economy, husbandry, pasture_forage, provision_resource, wealth_property
  - keywords: agriculture, animal, economy, pastoralism, pasture, subsistence, wealth
- `ن ع م B006` — النعام والنعامة الطائر
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, و ج ه, و ق ي
  - themes: animal, habitat_ecology, motion, naming_classification, terrain_desert, wildlife
  - keywords: animal, bird, desert, motion, nature, taxonomy, wildlife, zoology
- `ن ع م B007` — ما سمي نعامة تشبيها بالهيئة
  - activated_by_or_with: ء ت ي, ء ح د, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, و ج ه, و ق ي
  - themes: anatomy, geography_landscape, naming_classification, reasoning_decision, rhetoric_discourse, sky_astronomy, surface_shape, terrain_desert, tools_equipment
  - keywords: anatomy, landscape, metaphor, naming, nomenclature, tool, topography
- `ن ع م B008` — طيران النعامة وتفرق القوم
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, و ج ه, و ق ي
  - themes: change_transition, household_community, loss_absence, migration_displacement, motion, rhetoric_discourse, social_relations, violence_warfare
  - keywords: loss, metaphor, migration, movement, society, warfare
- `ن ع م B009` — النعامى ريح لينة
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ز ك و, ع ل و, ع ن د, و ج ه, و ق ي
  - themes: calendar_season, habitat_ecology, health_medicine, orientation_direction, perception, substance_texture, weather_climate
  - keywords: atmosphere, climate, comfort, direction, nature, season, sensation, weather
- `ن ع م B010` — زاد وأنعم في الفعل
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, و ج ه, و ق ي
  - themes: agency_action, change_transition, measurement, quantity_number, rhetoric_discourse, sequence_cycle
  - keywords: measure, performance, quantity, rhetoric
- `ن ع م B011` — موافقة المكان وطيب المقام
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, و ج ه, و ق ي
  - themes: architecture_construction, geography_landscape, habitat_ecology, health_medicine, hospitality_welfare, place_location, social_relations, travel
  - keywords: belonging, comfort, environment, geography, habitation, hospitality, place, settlement, travel
- `ن ع م B012` — المشي على القدم وابتذالها
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, و ج ه, و ق ي
  - themes: body, labor_work, motion, social_relations, stability_endurance, transport, travel
  - keywords: body, contact, labor, locomotion, movement, service, transport, travel
- `ن ع م B013` — نعم الله بك عينا وقرة العين
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, و ج ه, و ق ي
  - themes: belief_revelation, emotion, health_medicine, honor_shame, perception, prayer_supplication
  - keywords: blessing, emotion, honor

### ج ز ي

- `ج ز ي B001` — مقابلة الفعل بجزائه
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: afterlife_eschatology, commerce_exchange, ethics_morality, justice_judgment, law, punishment_sanction, reasoning_decision
  - keywords: accountability, afterlife, exchange, justice, law, morality, retaliation
- `ج ز ي B002` — قيام الشيء مقام غيره
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: abundance_scarcity, authority_governance, change_transition, communication, finance_debt, hospitality_welfare, obligation_contract, value_quality
  - keywords: charity, finance, liability, obligation, payment, representation
- `ج ز ي B003` — تقاضي الدين واستيفاؤه
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: authority_governance, commerce_exchange, finance_debt, law, obligation_contract, place_location
  - keywords: accounting, finance, law, liability, obligation, settlement
- `ج ز ي B004` — الجزية قضاء مالي
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: authority_governance, finance_debt, law, quantity_number
  - keywords: finance, governance, law, revenue, taxation
- `ج ز ي B005` — الغلبة في المجازاة
  - activated_by_or_with: ء ت ي, ب غ ي, ج ن ب, ر ب ب, ر ض و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: commerce_exchange, conflict, force_power, hierarchy_status, punishment_sanction
  - keywords: competition, conflict, dominance, hierarchy, power, reciprocity, retaliation

### ب غ ي

- `ب غ ي B001` — طلب الشيء وابتغاؤه
  - activated_by_or_with: ء ت ي, ء ح د, ج ن ب, ر ب ب, ر ض و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه
  - themes: agency_action, desire_appetite, intention_character, knowledge_learning, provision_resource, support_dependence, wealth_property
  - keywords: acquisition, agency, intention
- `ب غ ي B002` — الانبغاء والمطاوعة لما يليق أو يتيسر
  - activated_by_or_with: ء ت ي, ء ح د, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: capacity_ability, ethics_morality, grammar_expression, health_medicine, obligation_contract, support_dependence, value_quality
  - keywords: capacity, fitness, modality, norm
- `ب غ ي B003` — تجاوز الحد بالعدوان والظلم
  - activated_by_or_with: ء ت ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: conflict, ethics_morality, force_power, justice_judgment, law, orientation_direction, violence_warfare
  - keywords: conflict, ethics, injustice, law, power, violence
- `ب غ ي B004` — فساد الجرح وتجاوزه
  - activated_by_or_with: ء ت ي, ج ن ب, ر ب ب, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: body, disease_injury, growth_decay, health_medicine
  - keywords: body, decay, disease, injury, medicine, pathology
- `ب غ ي B005` — البغاء والفجور الجنسي
  - activated_by_or_with: ء ت ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: ethics_morality, gender, hierarchy_status, kinship, law, sexuality
  - keywords: gender, kinship, law, morality, sexuality
- `ب غ ي B006` — شدة المطر ومعظمه
  - activated_by_or_with: ء ت ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: abundance_scarcity, agriculture, habitat_ecology, water_hydrology, weather_climate
  - keywords: abundance, agriculture, climate, flood, meteorology, nature, storm, water, weather
- `ب غ ي B007` — اختيال الفرس ومرحه في العدو
  - activated_by_or_with: ء ت ي, ء ح د, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: animal, force_power, honor_shame, motion, ornament_beauty, recreation_sport
  - keywords: animal, locomotion, motion, sport
- `ب غ ي B008` — البغايا الطلائع
  - activated_by_or_with: ء ت ي, ء ح د, ج ن ب, ر ب ب, ر ض و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: cognition, motion, navigation_route, protection_security, travel, violence_warfare
  - keywords: movement, navigation, security, warfare
- `ب غ ي B009` — دعاء لا تباغ
  - activated_by_or_with: ء ت ي, ء ح د, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: belief_revelation, conflict, danger_harm, emotion, prayer_supplication, protection_security, ritual
  - keywords: blessing, conflict, harm, protection, ritual

### و ج ه

- `و ج ه B001` — الوجه والمستقبل
  - activated_by_or_with: ء ت ي, ب غ ي, ج ن ب, ر ب ب, ز ك و, ع ل و, ع ن د, ن ع م, و ق ي
  - themes: anatomy, body, orientation_direction, perception, posture_embodiment, surface_shape, visual_appearance
  - keywords: anatomy, appearance, body, embodiment, orientation, surface
- `و ج ه B002` — الجهة والوجهة
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ق ي
  - themes: belief_revelation, geography_landscape, intention_character, motion, navigation_route, orientation_direction, religion_worship
  - keywords: geography, guidance, intention, movement, navigation, orientation
- `و ج ه B003` — المواجهة والتقابل
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ق ي
  - themes: communication, conflict, language_speech, orientation_direction, place_location, social_relations
  - keywords: communication, conflict, interaction, orientation, relation, speech
- `و ج ه B004` — الوجه عن الذات
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ق ي
  - themes: cognition, communication, identity_personhood, posture_embodiment, rhetoric_discourse, value_quality
  - keywords: embodiment, identity, reference, representation
- `و ج ه B005` — القصد والتوجه
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `و ج ه B006` — الوجاهة والجاه
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م
  - themes: authority_governance, hierarchy_status, honor_shame, social_relations
  - keywords: authority, hierarchy, honor, leadership, reputation, society
- `و ج ه B007` — وجه النهار وصدره
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ر ب ب, ر ض و, ع ل و, ع ن د, ن ع م
  - themes: change_transition, hierarchy_status, sequence_cycle, surface_shape, time
  - keywords: emergence, sequence, surface, time, transition
- `و ج ه B008` — وجه الأمر وصوابه
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ق ي
  - themes: authority_governance, ethics_morality, politics_order, reasoning_decision, rhetoric_discourse
  - keywords: discourse, ethics, governance, logic, order
- `و ج ه B009` — توجه الشيخ
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م
  - themes: capacity_ability, change_transition, growth_decay, life_stage_aging, mortality_death, time
  - keywords: decay, mortality, time, transition
- `و ج ه B010` — الولادة باليدين أولا
  - activated_by_or_with: ء ت ي, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ز ك و, ع ل و, ن ع م, و ق ي
  - themes: anatomy, change_transition, danger_harm, family, health_medicine, reproduction_birth
  - keywords: anatomy, emergence, family, medicine, reproduction, risk
- `و ج ه B011` — توجيه القافية
  - activated_by_or_with: ء ح د, ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ق ي
  - themes: form_structure, language_speech, ornament_beauty, perception, rhetoric_discourse, writing_text
  - keywords: language
- `و ج ه B012` — توجيه النبات
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م
  - themes: agency_action, agriculture, craft, growth_decay, harvest_cultivation, hospitality_welfare, plant_vegetation
  - keywords: agriculture, botany, growth, plant
- `و ج ه B013` — ضرب الوجه
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ق ي
  - themes: body, conflict, danger_harm, disease_injury, punishment_sanction, social_relations, violence_warfare
  - keywords: body, conflict, contact, harm, injury, violence
- `و ج ه B014` — الرد عن الوجه
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ق ي
  - themes: boundary, communication, containment_access, hospitality_welfare, motion, social_relations
  - keywords: access, boundary, hospitality, interaction, movement, sociality
- `و ج ه B015` — ذو وجهين
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ق ي
  - themes: cognition, deception_corruption, ethics_morality, identity_personhood, surface_shape, trust_loyalty, visual_appearance
  - keywords: appearance, ethics, identity, morality, surface, trust

### ر ب ب

- `ر ب ب B001` — ربوبية وملك وسيادة
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: authority_governance, belief_revelation, force_power, hierarchy_status, religion_worship, support_dependence, wealth_property
  - keywords: authority, devotion, governance, hierarchy, patronage, power, property, theology
- `ر ب ب B002` — إصلاح وتربية وإتمام
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه
  - themes: agriculture, authority_governance, belief_revelation, craft, family, growth_decay, knowledge_learning, life_stage_aging, stability_endurance
  - keywords: agriculture, craft, education, growth, providence
- `ر ب ب B003` — علم رباني
  - activated_by_or_with: ء ت ي, ب غ ي, ج ز ي, ج ن ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: cognition, ethics_morality, knowledge_learning, religion_worship
  - keywords: education, ethics, religion, spirituality
- `ر ب ب B004` — ربة وجماعات كثيرة
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ض و, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: household_community, kinship, quantity_number, social_relations, violence_warfare
  - keywords: collectivity, kinship, number, society
- `ر ب ب B005` — ربيب وربيبة ورابة
  - activated_by_or_with: ء ت ي, ب غ ي, ج ز ي, ج ن ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه
  - themes: authority_governance, family, hospitality_welfare, household_community, kinship, reproduction_birth, support_dependence
  - keywords: dependency, family, household, kinship
- `ر ب ب B006` — رُبّ خاثر وإصلاح به
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: agency_action, food_nutrition, health_medicine, material, stability_endurance, substance_texture
  - keywords: food, leather, material, medicine, preparation
- `ر ب ب B007` — لزوم وإقامة ودوام
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ض و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: animal, geography_landscape, motion, place_location, time, weather_climate
  - keywords: animal, geography, habitation, motion, movement, temporality, time, weather
- `ر ب ب B008` — رباب السحاب
  - activated_by_or_with: ء ت ي, ب غ ي, ج ن ب, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: agriculture, habitat_ecology, reproduction_birth, sky_astronomy, water_hydrology, weather_climate
  - keywords: agriculture, ecology, fertility, meteorology, sky, water, weather
- `ر ب ب B009` — شاة رُبّى وحداثة
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: animal, food_nutrition, household_community, life_stage_aging, livestock, reproduction_birth, time
  - keywords: animal, birth, dairy, household, livestock, reproduction, temporality, time
- `ر ب ب B010` — ربابة تجمع القداح
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: abundance_scarcity, belief_revelation, material, proof_uncertainty, ritual, storage_vessels, tools_equipment, weaponry
  - keywords: fortune, leather, ritual, tool, weapon
- `ر ب ب B011` — ربابة عهد وميثاق
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: finance_debt, household_community, law, obligation_contract, politics_order, protection_security, trust_loyalty
  - keywords: community, contract, diplomacy, law, protection, taxation, trust
- `ر ب ب B012` — ربة نبات
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ض و, ز ك و, ع ل و, ن ع م, و ج ه, و ق ي
  - themes: agriculture, food_nutrition, geography_landscape, habitat_ecology, physiology, plant_vegetation, visual_appearance
  - keywords: agriculture, botany, ecology, food, landscape, life
- `ر ب ب B013` — ماء رَبَب كثير
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: abundance_scarcity, geography_landscape, habitat_ecology, provision_resource, purity_cleansing, water_hydrology
  - keywords: abundance, ecology, geography, hydrology, nature, purity, resource
- `ر ب ب B014` — رَبْرَب قطيع
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ق ي
  - themes: animal, habitat_ecology, household_community, husbandry, livestock, quantity_number, terrain_desert, wildlife
  - keywords: collectivity, desert, ecology, livestock, pastoralism, zoology
- `ر ب ب B015` — حرف رب وربما
  - activated_by_or_with: ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: form_structure, grammar_expression, language_speech, quantity_number, rhetoric_discourse
  - keywords: discourse, grammar, modality, morphology, quantification, rhetoric, semantics, syntax
- `ر ب ب B016` — رُبَى حاجة وعقدة ونعمة
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ض و, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: control_restraint, ethics_morality, hospitality_welfare, material, obligation_contract, social_relations, support_dependence
  - keywords: charity, dependency, ethics, gift, material, obligation, relation, welfare
- `ر ب ب B017` — رباني الملاحين
  - activated_by_or_with: ء ت ي, ب غ ي, ج ز ي, ج ن ب, ر ض و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: authority_governance, hierarchy_status, labor_work, navigation_route, transport, travel, water_hydrology
  - keywords: authority, hierarchy, navigation, transport, travel, water

### ع ل و

- `ع ل و B001` — السمو والارتفاع
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ن ب, ر ب ب, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: body, motion, orientation_direction, sky_astronomy, space, surface_shape, terrain_desert, time
  - keywords: body, geometry, motion, orientation, sky, space, time, topography
- `ع ل و B002` — الرفعة والشرف
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: authority_governance, ethics_morality, hierarchy_status, honor_shame, naming_classification, social_relations, value_quality
  - keywords: authority, ethics, hierarchy, leadership, reputation, society, value, virtue
- `ع ل و B003` — العظمة والتجبر
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: authority_governance, control_restraint, deception_corruption, ethics_morality, force_power, identity_personhood, justice_judgment, politics_order, violence_warfare
  - keywords: authority, corruption, ethics, injustice, power, violence
- `ع ل و B004` — الغلبة والاستيلاء
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: agency_action, authority_governance, capacity_ability, conflict, control_restraint, force_power, labor_work, reasoning_decision, violence_warfare
  - keywords: agency, capacity, conflict, control, governance, labor, power, warfare
- `ع ل و B005` — الجهة العليا ومن فوق
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ن د, ن ع م, و ج ه
  - themes: orientation_direction, place_location, reasoning_decision, space, surface_shape, weather_climate
  - keywords: contrast, geometry, orientation, space, weather
- `ع ل و B006` — نداء التعالي
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: communication, grammar_expression, household_community, language_speech, motion, ritual, social_relations
  - keywords: communication, grammar, motion, movement, ritual, sociality, speech
- `ع ل و B007` — المواضع العالية
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ع ل و B008` — الشيء المحمول على الأعلى
  - activated_by_or_with: ء ت ي, ء ح د, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: anatomy, architecture_construction, form_structure, material, social_relations, transport, writing_text
  - keywords: anatomy, transport
- `ع ل و B009` — أسماء الأدوات والأجزاء المرتفعة
  - activated_by_or_with: ء ت ي, ب غ ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: animal, craft, proof_uncertainty, recreation_sport, storage_vessels, tools_equipment, water_hydrology, weaponry
  - keywords: animal, craft, game, tool, water, weapon
- `ع ل و B010` — الطول والضخامة
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: anatomy, animal, body, force_power, measurement, physiology
  - keywords: anatomy, animal, biology, body, measurement
- `ع ل و B011` — السلامة من النفاس أو العلة
  - activated_by_or_with: ء ت ي, ب غ ي, ج ن ب, ر ب ب, ز ك و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: body, disease_injury, health_medicine, physiology, reproduction_birth
  - keywords: birth, body, disease, life, medicine
- `ع ل و B012` — حرف عَلَى وما جرى مجراه
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ر ض و, ز ك و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: grammar_expression, language_speech, law, social_relations
  - keywords: grammar, language, relation, semantics, syntax

### ر ض و

- `ر ض و B001` — الرضا خلاف السخط
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: authority_governance, desire_appetite, emotion, ethics_morality, justice_judgment, obligation_contract, social_relations
  - keywords: approval, emotion, ethics, judgment, relation
- `ر ض و B002` — الرضوان والمرضاة اسم للرضا الكثير أو المطلوب
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ز ك و, ع ل و, ع ن د, م و ل, ن ع م, و ج ه, و ق ي
  - themes: abundance_scarcity, authority_governance, belief_revelation, desire_appetite, hospitality_welfare, justice_judgment, religion_worship
  - keywords: abundance, approval, blessing, devotion, favor
- `ر ض و B003` — المراضاة والتراضي رضا متبادل
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: commerce_exchange, household_community, obligation_contract, rhetoric_discourse, social_relations
  - keywords: agreement, community, contract, cooperation, reciprocity, reconciliation, society
- `ر ض و B004` — الإرضاء طلب رضا الغير وإزالة سخطه
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: communication, conflict, craft, emotion, ethics_morality, politics_order, rhetoric_discourse, social_relations
  - keywords: conflict, diplomacy, emotion, persuasion, reconciliation
- `ر ض و B005` — راضاني فرضوته غلبة في ذلك
  - activated_by_or_with: ء ت ي, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ع ل و, ع ن د, ن ع م, و ج ه
  - themes: capacity_ability, conflict, force_power, hierarchy_status, violence_warfare
  - keywords: competition, conflict, dominance, hierarchy, power
- `ر ض و B006` — الرضي صفة للمطيع أو المحب أو الضامن
  - activated_by_or_with: ء ت ي, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ز ك و, ع ل و, ع ن د, ن ع م, و ج ه, و ق ي
  - themes: authority_governance, emotion, ethics_morality, intention_character, law, obligation_contract, religion_worship, trust_loyalty
  - keywords: character, devotion, ethics, law, liability
- `ر ض و B007` — رضوى ورضيا أعلام من المادة
  - activated_by_or_with: ء ت ي, ء ح د, ب غ ي, ج ز ي, ج ن ب, ر ب ب, ع ل و, م و ل, ن ع م, و ج ه, و ق ي
  - themes: gender, geography_landscape, identity_personhood, naming_classification, place_location
  - keywords: gender, geography, identity, naming, nomenclature, place

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
