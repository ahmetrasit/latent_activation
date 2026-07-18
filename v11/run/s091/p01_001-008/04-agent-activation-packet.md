# v11 Activation Packet — S91:1-8

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_1: وَٱلشَّمْسِ وَضُحَىٰهَا
- verse_2: وَٱلْقَمَرِ إِذَا تَلَىٰهَا
- verse_3: وَٱلنَّهَارِ إِذَا جَلَّىٰهَا
- verse_4: وَٱلَّيْلِ إِذَا يَغْشَىٰهَا
- verse_5: وَٱلسَّمَآءِ وَمَا بَنَىٰهَا
- verse_6: وَٱلْأَرْضِ وَمَا طَحَىٰهَا
- verse_7: وَنَفْسٍۢ وَمَا سَوَّىٰهَا
- verse_8: فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ش م س → ض ح و → ق م ر → ت ل و → ن ه ر → ج ل و → ل ي ل → غ ش و → س م و → ب ن ي → ء ر ض → ط ح و → ن ف س → س و ي → ل ه م → ف ج ر → و ق ي

## Branch inventory summary

- ش م س: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- ض ح و: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- ق م ر: 12 branches (12 with Qnet bridge-theme nodes; 0 Furūq-only)
- ت ل و: 9 branches (8 with Qnet bridge-theme nodes; 1 Furūq-only)
- ن ه ر: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ج ل و: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- ل ي ل: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- غ ش و: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- س م و: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ب ن ي: 10 branches (10 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء ر ض: 12 branches (12 with Qnet bridge-theme nodes; 0 Furūq-only)
- ط ح و: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن ف س: 16 branches (16 with Qnet bridge-theme nodes; 0 Furūq-only)
- س و ي: 13 branches (13 with Qnet bridge-theme nodes; 0 Furūq-only)
- ل ه م: 5 branches (4 with Qnet bridge-theme nodes; 1 Furūq-only)
- ف ج ر: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- و ق ي: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)

## QAC-first root resolution audit

- ش م س | qac_keys=شمس | status=resolved | matches=root_000818
- ض ح و | qac_keys=ضحو | status=resolved | matches=root_000904
- ق م ر | qac_keys=قمر | status=resolved | matches=root_001255
- ت ل و | qac_keys=تلو | status=resolved | matches=root_000186
- ن ه ر | qac_keys=نهر | status=resolved | matches=root_001559
- ج ل و | qac_keys=جلو | status=resolved | matches=root_000256
- ل ي ل | qac_keys=ليل | status=resolved | matches=root_001392
- غ ش و | qac_keys=غشو | status=resolved | matches=root_001088
- س م و | qac_keys=سمو | status=resolved | matches=root_000745
- ب ن ي | qac_keys=بني | status=resolved | matches=root_000156
- ء ر ض | qac_keys=ءرض | status=resolved | matches=root_000025
- ط ح و | qac_keys=طحو | status=resolved | matches=root_000928
- ن ف س | qac_keys=نفس | status=resolved | matches=root_001533
- س و ي | qac_keys=سوي | status=resolved | matches=root_000766
- ل ه م | qac_keys=لهم | status=resolved | matches=root_001381
- ف ج ر | qac_keys=فجر | status=resolved | matches=root_001132
- و ق ي | qac_keys=وقي | status=resolved | matches=root_001677

## Top candidate bridges

- `ق م ر B001` ↔ `ن ه ر B002` | score_hint=34 | discovery_hint=14 | themes=calendar_season, light_darkness, sequence_cycle, sky_astronomy, time | keywords=astronomy, calendar, cycle, illumination, light, time | q2=—
- `ق م ر B001` ↔ `س و ي B012` | score_hint=34 | discovery_hint=14 | themes=calendar_season, light_darkness, sequence_cycle, sky_astronomy, time | keywords=astronomy, calendar, cycle, illumination, sky, time | q2=—
- `ق م ر B008` ↔ `ء ر ض B002` | score_hint=30 | discovery_hint=16 | themes=abundance_scarcity, agriculture, habitat_ecology, pasture_forage, plant_vegetation | keywords=abundance, agriculture, ecology, pasture, vegetation | q2=—
- `ن ه ر B002` ↔ `س و ي B012` | score_hint=30 | discovery_hint=15 | themes=calendar_season, light_darkness, sequence_cycle, sky_astronomy, time | keywords=astronomy, calendar, cycle, illumination, time | q2=—
- `ق م ر B008` ↔ `س و ي B009` | score_hint=28 | discovery_hint=14 | themes=abundance_scarcity, habitat_ecology, pasture_forage, water_hydrology | keywords=abundance, ecology, hydrology, pasture, water | q2=—
- `ت ل و B008` ↔ `غ ش و B005` | score_hint=28 | discovery_hint=15 | themes=body, disease_injury, health_medicine, mortality_death | keywords=body, death, illness, medicine, mortality | q2=—
- `ت ل و B008` ↔ `ن ف س B004` | score_hint=26 | discovery_hint=16 | themes=body, disease_injury, health_medicine, mortality_death, physiology | keywords=body, medicine, mortality, vitality | q2=—
- `ن ه ر B002` ↔ `ل ي ل B001` | score_hint=26 | discovery_hint=14 | themes=light_darkness, reasoning_decision, sequence_cycle, sky_astronomy, time | keywords=astronomy, contrast, cycle, time | q2=—
- `ن ه ر B002` ↔ `ف ج ر B002` | score_hint=26 | discovery_hint=15 | themes=light_darkness, perception, sequence_cycle, sky_astronomy, time | keywords=cycle, illumination, light, time | q2=—
- `ق م ر B001` ↔ `ف ج ر B002` | score_hint=24 | discovery_hint=14 | themes=light_darkness, sequence_cycle, sky_astronomy, time | keywords=cycle, illumination, light, time | q2=—
- `ق م ر B008` ↔ `ن ف س B008` | score_hint=24 | discovery_hint=15 | themes=abundance_scarcity, habitat_ecology, provision_resource, water_hydrology | keywords=abundance, ecology, resource, water | q2=—
- `ق م ر B012` ↔ `و ق ي B005` | score_hint=24 | discovery_hint=14 | themes=animal, habitat_ecology, naming_classification, wildlife | keywords=animal, bird, naming, taxonomy | q2=—
- `غ ش و B001` ↔ `ب ن ي B004` | score_hint=24 | discovery_hint=15 | themes=protection_security, storage_vessels, textile_clothing, tools_equipment | keywords=container, equipment, protection, textile | q2=—
- `ق م ر B007` ↔ `ن ف س B016` | score_hint=23 | discovery_hint=18 | themes=conflict, proof_uncertainty, recreation_sport | keywords=chance, competition, game, gaming | q2=—
- `ق م ر B003` ↔ `ج ل و B008` | score_hint=22 | discovery_hint=14 | themes=animal, perception, wildlife | keywords=animal, hunting, perception, vision | q2=—
- `ت ل و B008` ↔ `ن ف س B011` | score_hint=22 | discovery_hint=16 | themes=body, mortality_death, physiology | keywords=body, death, life, mortality | q2=—
- `ن ه ر B001` ↔ `س و ي B009` | score_hint=22 | discovery_hint=13 | themes=abundance_scarcity, geography_landscape, water_hydrology | keywords=abundance, geography, hydrology, landscape | q2=—
- `ن ه ر B005` ↔ `و ق ي B005` | score_hint=22 | discovery_hint=14 | themes=animal, naming_classification, wildlife | keywords=animal, taxonomy, wildlife, zoology | q2=—
- `ش م س B001` ↔ `ج ل و B007` | score_hint=22 | discovery_hint=14 | themes=habitat_ecology, light_darkness, sky_astronomy, time, weather_climate | keywords=nature, time, weather | q2=—
- `ب ن ي B004` ↔ `ء ر ض B005` | score_hint=22 | discovery_hint=13 | themes=architecture_construction, craft, material, textile_clothing, tools_equipment | keywords=craft, shelter, textile | q2=—
- `ض ح و B001` ↔ `ن ه ر B002` | score_hint=20 | discovery_hint=12 | themes=calendar_season, light_darkness, sequence_cycle, time | keywords=calendar, chronology, rhythm | q2=—
- `ض ح و B005` ↔ `ق م ر B005` | score_hint=20 | discovery_hint=14 | themes=light_darkness, perception, visual_appearance, weather_climate | keywords=color, optics, weather | q2=—
- `ق م ر B001` ↔ `ل ي ل B001` | score_hint=20 | discovery_hint=12 | themes=light_darkness, sequence_cycle, sky_astronomy, time | keywords=astronomy, cycle, time | q2=—
- `ق م ر B005` ↔ `ج ل و B007` | score_hint=20 | discovery_hint=14 | themes=habitat_ecology, light_darkness, perception, weather_climate | keywords=environment, perception, weather | q2=—
- `ج ل و B006` ↔ `س م و B005` | score_hint=20 | discovery_hint=14 | themes=cognition, communication, identity_personhood, language_speech | keywords=identity, language, recognition | q2=—
- `ج ل و B006` ↔ `س م و B008` | score_hint=20 | discovery_hint=13 | themes=communication, honor_shame, memory_attention, social_relations | keywords=communication, memory, reputation | q2=—
- `ج ل و B007` ↔ `ف ج ر B002` | score_hint=20 | discovery_hint=14 | themes=light_darkness, perception, sky_astronomy, time | keywords=light, perception, time | q2=—
- `ج ل و B009` ↔ `ب ن ي B006` | score_hint=20 | discovery_hint=13 | themes=household_community, kinship, marriage_genealogy, ritual | keywords=household, kinship, marriage | q2=—
- `ل ي ل B001` ↔ `س و ي B012` | score_hint=20 | discovery_hint=13 | themes=light_darkness, sequence_cycle, sky_astronomy, time | keywords=astronomy, cycle, time | q2=—
- `غ ش و B005` ↔ `ن ف س B004` | score_hint=20 | discovery_hint=14 | themes=body, disease_injury, health_medicine, mortality_death | keywords=body, medicine, mortality | q2=—
- `س م و B008` ↔ `س و ي B008` | score_hint=20 | discovery_hint=13 | themes=communication, honor_shame, memory_attention, social_relations | keywords=communication, praise, sociality | q2=—
- `س و ي B012` ↔ `ف ج ر B002` | score_hint=20 | discovery_hint=14 | themes=light_darkness, sequence_cycle, sky_astronomy, time | keywords=cycle, illumination, time | q2=—
- `س م و B002` ↔ `ط ح و B008` | score_hint=20 | discovery_hint=14 | themes=measurement, orientation_direction, perception, place_location, sky_astronomy, space | keywords=astronomy, visibility | q2=—
- `ن ه ر B007` ↔ `ل ي ل B004` | score_hint=19 | discovery_hint=18 | themes=culture_tradition, identity_personhood, naming_classification | keywords=culture, identity, onomastics | q2=—
- `ش م س B001` ↔ `ض ح و B005` | score_hint=18 | discovery_hint=14 | themes=light_darkness, sky_astronomy, weather_climate | keywords=astronomy, illumination, weather | q2=—
- `ش م س B001` ↔ `ق م ر B001` | score_hint=18 | discovery_hint=12 | themes=light_darkness, sky_astronomy, time | keywords=astronomy, illumination, time | q2=—
- `ش م س B001` ↔ `ن ه ر B002` | score_hint=18 | discovery_hint=13 | themes=light_darkness, sky_astronomy, time | keywords=astronomy, illumination, time | q2=—
- `ش م س B001` ↔ `س و ي B012` | score_hint=18 | discovery_hint=13 | themes=light_darkness, sky_astronomy, time | keywords=astronomy, illumination, time | q2=—
- `ش م س B003` ↔ `ن ه ر B004` | score_hint=18 | discovery_hint=13 | themes=communication, conflict, social_relations | keywords=communication, conflict, sociality | q2=—
- `ش م س B007` ↔ `س م و B005` | score_hint=18 | discovery_hint=14 | themes=identity_personhood, language_speech, naming_classification | keywords=classification, identity, language | q2=—
- `ض ح و B003` ↔ `ق م ر B008` | score_hint=18 | discovery_hint=15 | themes=agriculture, pasture_forage, provision_resource | keywords=agriculture, pasture, sustenance | q2=—
- `ض ح و B003` ↔ `ق م ر B010` | score_hint=18 | discovery_hint=14 | themes=animal, food_nutrition, husbandry | keywords=animal, feeding, husbandry | q2=—
- `ض ح و B003` ↔ `ء ر ض B002` | score_hint=18 | discovery_hint=15 | themes=agriculture, food_nutrition, pasture_forage | keywords=agriculture, nourishment, pasture | q2=—
- `ض ح و B005` ↔ `ن ه ر B002` | score_hint=18 | discovery_hint=14 | themes=light_darkness, perception, sky_astronomy | keywords=astronomy, illumination, light | q2=—
- `ق م ر B001` ↔ `ج ل و B007` | score_hint=18 | discovery_hint=13 | themes=light_darkness, sky_astronomy, time | keywords=light, sky, time | q2=—
- `ق م ر B003` ↔ `ن ه ر B006` | score_hint=18 | discovery_hint=13 | themes=deception_corruption, habitat_ecology, reasoning_decision | keywords=deception, predation, strategy | q2=—
- `ق م ر B003` ↔ `س م و B006` | score_hint=18 | discovery_hint=13 | themes=animal, habitat_ecology, wildlife | keywords=animal, hunting, predation | q2=—
- `ق م ر B012` ↔ `ن ه ر B005` | score_hint=18 | discovery_hint=13 | themes=animal, naming_classification, wildlife | keywords=animal, ornithology, taxonomy | q2=—
- `ق م ر B012` ↔ `ء ر ض B001` | score_hint=18 | discovery_hint=12 | themes=animal, geography_landscape, habitat_ecology | keywords=animal, geography, habitat | q2=—
- `ت ل و B009` ↔ `ن ه ر B004` | score_hint=18 | discovery_hint=13 | themes=conflict, ethics_morality, language_speech | keywords=conflict, ethics, speech | q2=—
- `ن ه ر B002` ↔ `ط ح و B008` | score_hint=18 | discovery_hint=14 | themes=light_darkness, perception, sky_astronomy | keywords=astronomy, light, visibility | q2=—
- `ن ه ر B004` ↔ `س م و B008` | score_hint=18 | discovery_hint=13 | themes=communication, ethics_morality, social_relations | keywords=communication, ethics, sociality | q2=—
- `ج ل و B005` ↔ `ن ف س B004` | score_hint=18 | discovery_hint=15 | themes=body, health_medicine, physiology | keywords=body, medicine, physiology | q2=—
- `ج ل و B007` ↔ `ن ف س B009` | score_hint=18 | discovery_hint=13 | themes=habitat_ecology, light_darkness, time | keywords=light, nature, time | q2=—
- `ج ل و B009` ↔ `ف ج ر B005` | score_hint=18 | discovery_hint=14 | themes=commerce_exchange, economy, hospitality_welfare | keywords=economy, exchange, gift | q2=—
- `غ ش و B004` ↔ `ب ن ي B006` | score_hint=18 | discovery_hint=14 | themes=kinship, marriage_genealogy, sexuality | keywords=kinship, marriage, sexuality | q2=—
- `غ ش و B005` ↔ `ن ف س B011` | score_hint=18 | discovery_hint=14 | themes=body, cognition, mortality_death | keywords=body, death, mortality | q2=—
- `ء ر ض B002` ↔ `ن ف س B008` | score_hint=18 | discovery_hint=14 | themes=abundance_scarcity, food_nutrition, habitat_ecology | keywords=abundance, ecology, nourishment | q2=—
- `ء ر ض B002` ↔ `س و ي B009` | score_hint=18 | discovery_hint=13 | themes=abundance_scarcity, habitat_ecology, pasture_forage | keywords=abundance, ecology, pasture | q2=—
- `ء ر ض B003` ↔ `ن ف س B014` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, hospitality_welfare, intention_character | keywords=character, ethics, virtue | q2=—
- `ء ر ض B010` ↔ `و ق ي B005` | score_hint=18 | discovery_hint=13 | themes=animal, habitat_ecology, wildlife | keywords=animal, ecology, zoology | q2=—
- `ء ر ض B011` ↔ `ن ف س B004` | score_hint=18 | discovery_hint=14 | themes=body, disease_injury, health_medicine | keywords=body, injury, medicine | q2=—
- `ط ح و B001` ↔ `س و ي B009` | score_hint=18 | discovery_hint=12 | themes=geography_landscape, space, terrain_desert | keywords=landscape, space, terrain | q2=—
- `ن ف س B008` ↔ `س و ي B009` | score_hint=18 | discovery_hint=13 | themes=abundance_scarcity, habitat_ecology, water_hydrology | keywords=abundance, ecology, water | q2=—
- `س و ي B010` ↔ `ل ه م B003` | score_hint=18 | discovery_hint=13 | themes=animal, transport, travel | keywords=animal, transport, travel | q2=—
- `س و ي B010` ↔ `و ق ي B003` | score_hint=18 | discovery_hint=13 | themes=animal, tools_equipment, transport | keywords=animal, equipment, riding | q2=—
- `ش م س B004` ↔ `ء ر ض B005` | score_hint=18 | discovery_hint=12 | themes=craft, material, ornament_beauty, textile_clothing, tools_equipment | keywords=craft, material | q2=—
- `ش م س B007` ↔ `ق م ر B012` | score_hint=16 | discovery_hint=13 | themes=geography_landscape, naming_classification | keywords=geography, naming, taxonomy | q2=—
- `ش م س B007` ↔ `و ق ي B005` | score_hint=16 | discovery_hint=13 | themes=language_speech, naming_classification | keywords=language, naming, taxonomy | q2=—
- `ض ح و B003` ↔ `ل ه م B001` | score_hint=16 | discovery_hint=13 | themes=animal, food_nutrition | keywords=animal, feeding, nourishment | q2=—
- `ض ح و B005` ↔ `ق م ر B001` | score_hint=16 | discovery_hint=13 | themes=light_darkness, sky_astronomy | keywords=astronomy, illumination, light | q2=—
- `ق م ر B001` ↔ `ط ح و B008` | score_hint=16 | discovery_hint=13 | themes=light_darkness, sky_astronomy | keywords=astronomy, light, sky | q2=—
- `ت ل و B006` ↔ `ن ه ر B005` | score_hint=16 | discovery_hint=14 | themes=animal, reproduction_birth | keywords=animal, birth, reproduction | q2=—
- `ت ل و B008` ↔ `ط ح و B007` | score_hint=16 | discovery_hint=13 | themes=mortality_death, sequence_cycle | keywords=death, ending, mortality | q2=—
- `ن ه ر B002` ↔ `ج ل و B001` | score_hint=16 | discovery_hint=12 | themes=light_darkness, perception | keywords=illumination, light, visibility | q2=—
- `ن ه ر B005` ↔ `غ ش و B007` | score_hint=16 | discovery_hint=13 | themes=animal, naming_classification | keywords=animal, taxonomy, zoology | q2=—
- `غ ش و B007` ↔ `و ق ي B005` | score_hint=16 | discovery_hint=13 | themes=animal, naming_classification | keywords=animal, taxonomy, zoology | q2=—
- `ط ح و B007` ↔ `ل ه م B005` | score_hint=16 | discovery_hint=13 | themes=danger_harm, mortality_death | keywords=death, disaster, mortality | q2=—
- `ش م س B001` ↔ `ل ي ل B001` | score_hint=16 | discovery_hint=11 | themes=habitat_ecology, light_darkness, sky_astronomy, time | keywords=astronomy, time | q2=—
- `ض ح و B005` ↔ `ق م ر B002` | score_hint=16 | discovery_hint=13 | themes=animal, perception, visual_appearance, weather_climate | keywords=animal, color | q2=—

## Per-root candidate activations

### ش م س

- `ش م س B001` — الشمس والضح
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, س و ي, ض ح و, ط ح و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: habitat_ecology, labor_work, light_darkness, sky_astronomy, time, weather_climate
  - keywords: astronomy, climate, illumination, labor, nature, time, weather
- `ش م س B002` — الشماس والشموس في الدابة والخلق
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س م و, س و ي, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: agency_action, animal, conflict, control_restraint, husbandry, intention_character
  - keywords: animal, behavior, conflict, control, temperament
- `ش م س B003` — إبداء العداوة
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ن ف س, ن ه ر
  - themes: communication, conflict, emotion, social_relations, violence_warfare
  - keywords: aggression, communication, conflict, emotion, social, sociality, violence
- `ش م س B004` — شموس القلائد
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, س و ي, غ ش و, ق م ر, ن ف س, و ق ي
  - themes: craft, material, ornament_beauty, textile_clothing, tools_equipment
  - keywords: beauty, craft, material
- `ش م س B005` — الشماس النصراني
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, س و ي, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ن ف س, ن ه ر, و ق ي
  - themes: authority_governance, household_community, religion_worship
  - keywords: authority, community, religion, worship
- `ش م س B006` — التشمس بالمنع والبخل
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: abundance_scarcity, boundary, commerce_exchange, ethics_morality, hospitality_welfare, social_relations, wealth_property
  - keywords: ethics, exchange, generosity, ownership, property, social, society
- `ش م س B007` — التسمية بالشمس وما نسب إليها
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ط ح و, غ ش و, ق م ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: geography_landscape, identity_personhood, language_speech, marriage_genealogy, naming_classification, rhetoric_discourse
  - keywords: classification, geography, identity, language, naming, reference, taxonomy

### ض ح و

- `ض ح و B001` — امتداد الضحى في النهار
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س و ي, ش م س, ط ح و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر
  - themes: calendar_season, light_darkness, sequence_cycle, time
  - keywords: calendar, chronology, delay, rhythm, sequence, timing
- `ض ح و B002` — البروز للشمس والظهور
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر
  - themes: body, concealment_disclosure, perception, posture_embodiment, space, surface_shape, weather_climate
  - keywords: body, climate, embodiment, publicity, space, spatiality, surface, visibility
- `ض ح و B003` — طعام الضحاء ورعي أوله
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: agriculture, animal, food_nutrition, husbandry, pasture_forage, provision_resource, sequence_cycle
  - keywords: agriculture, animal, feeding, husbandry, nourishment, pasture, provision, sustenance
- `ض ح و B004` — ذبيحة يوم الأضحى
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: animal, calendar_season, pilgrimage_sacrifice, religion_worship, ritual, violence_warfare
  - keywords: animal, calendar, devotion, religion, ritual
- `ض ح و B005` — ضياء الضحى وصفاؤه
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: animal, light_darkness, perception, purity_cleansing, sky_astronomy, visual_appearance, weather_climate
  - keywords: animal, astronomy, atmosphere, color, illumination, light, optics, purity, weather
- `ض ح و B006` — الرفق والإمهال
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س م و, س و ي, ش م س, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: control_restraint, ethics_morality, hospitality_welfare, intention_character, time
  - keywords: care, ethics, mercy, patience, temperament, timing

### ق م ر

- `ق م ر B001` — القمر وضوؤه في السماء
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, ف ج ر, ل ي ل, ن ف س, ن ه ر
  - themes: calendar_season, light_darkness, sequence_cycle, sky_astronomy, time
  - keywords: astronomy, brightness, calendar, cycle, illumination, light, night, sky, time
- `ق م ر B002` — بياض قمري أو لون أقمر
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: animal, perception, reasoning_decision, visual_appearance, weather_climate
  - keywords: animal, color, comparison, perception
- `ق م ر B003` — القصد أو الصيد في القمراء
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: animal, calendar_season, danger_harm, deception_corruption, habitat_ecology, perception, reasoning_decision, wildlife
  - keywords: animal, deception, ecology, hunting, night, perception, predation, strategy, vision
- `ق م ر B004` — تمر ضربه البرد قبل النضج
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ل ه م, ن ف س, ن ه ر
  - themes: agriculture, food_nutrition, growth_decay, life_stage_aging, perception, plant_vegetation, weather_climate
  - keywords: agriculture, food, weather
- `ق م ر B005` — تحير البصر من بياض الثلج
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: disease_injury, habitat_ecology, light_darkness, orientation_direction, perception, visual_appearance, weather_climate
  - keywords: brightness, color, environment, optics, perception, vision, weather
- `ق م ر B006` — قربة أفسدتها القمراء
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: calendar_season, craft, danger_harm, growth_decay, material, storage_vessels, substance_texture, water_hydrology
  - keywords: container, decay, leather, material, night, water
- `ق م ر B007` — المقامرة والغلبة بالخداع
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: commerce_exchange, conflict, danger_harm, deception_corruption, proof_uncertainty, recreation_sport, wealth_property
  - keywords: chance, competition, conflict, deception, exchange, game, gaming, risk
- `ق م ر B008` — كثرة الماء والكلأ
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, ف ج ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: abundance_scarcity, agriculture, habitat_ecology, pasture_forage, plant_vegetation, provision_resource, water_hydrology
  - keywords: abundance, agriculture, ecology, hydrology, pasture, resource, sustenance, vegetation, water
- `ق م ر B009` — الأرق في ضوء القمر
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: calendar_season, cognition, danger_harm, health_medicine, light_darkness, physiology, sequence_cycle
  - keywords: health, light, night, rhythm
- `ق م ر B010` — تأخر عشاء الإبل
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: animal, authority_governance, food_nutrition, hospitality_welfare, husbandry, livestock, time
  - keywords: animal, care, delay, feeding, husbandry, livestock, pastoralism, time
- `ق م ر B011` — إهمال المال ليلا للقمر
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: authority_governance, calendar_season, danger_harm, husbandry, intention_character, obligation_contract, pasture_forage, protection_security, wealth_property
  - keywords: night, pastoralism, pasture, property, risk, security
- `ق م ر B012` — طائر القمري والقمارى
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: animal, geography_landscape, habitat_ecology, naming_classification, place_location, wildlife
  - keywords: animal, bird, geography, habitat, naming, ornithology, place, taxonomy

### ت ل و

- `ت ل و B001` — اتباع وتتابع
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: hierarchy_status, motion, politics_order, sequence_cycle, social_relations, stability_endurance
  - keywords: continuity, hierarchy, movement, order, relation, sequence, status
- `ت ل و B002` — تلاوة متبوعة
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ت ل و B003` — بقية تتلو ما قبلها
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س و ي, ش م س, ض ح و, ط ح و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: commerce_exchange, finance_debt, law, obligation_contract, sequence_cycle, stability_endurance, wealth_property
  - keywords: accounting, commerce, continuity, finance, law, liability, obligation, possession, property, sequence
- `ت ل و B004` — ذمة أو حق يتبع صاحبه
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س و ي, ش م س, غ ش و, ف ج ر, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: finance_debt, law, obligation_contract, protection_security, trust_loyalty, wealth_property
  - keywords: finance, law, liability, obligation, ownership, security
- `ت ل و B005` — ترك بعد صحبة
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: boundary, ethics_morality, loss_absence, motion, sequence_cycle, social_relations, trust_loyalty
  - keywords: ethics, loss, movement, sequence, sociality
- `ت ل و B006` — ولد يتلو أمه
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: animal, husbandry, kinship, marriage_genealogy, reproduction_birth, support_dependence
  - keywords: animal, birth, kinship, pastoralism, reproduction
- `ت ل و B007` — صوت يتلو صوتا
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر
  - themes: agency_action, communication, perception, sequence_cycle
  - keywords: communication, performance, sequence
- `ت ل و B008` — آخر رمق
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: body, boundary, disease_injury, health_medicine, mortality_death, physiology, sequence_cycle
  - keywords: body, death, ending, illness, life, medicine, mortality, vitality
- `ت ل و B009` — قول كذب على غيره
  - activated_by_or_with: ء ر ض, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: conflict, deception_corruption, ethics_morality, honor_shame, language_speech, law
  - keywords: conflict, deception, ethics, law, reputation, speech

### ن ه ر

- `ن ه ر B001` — نهر يشق الأرض بماء جار
  - activated_by_or_with: ء ر ض, ب ن ي, س و ي, ش م س, ط ح و, ف ج ر, ق م ر, ل ه م, ن ف س
  - themes: abundance_scarcity, earth_geology, geography_landscape, water_hydrology
  - keywords: abundance, geography, hydrology, landscape
- `ن ه ر B002` — انفتاح النهار بالضياء
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س
  - themes: calendar_season, light_darkness, perception, reasoning_decision, sequence_cycle, sky_astronomy, time
  - keywords: astronomy, calendar, chronology, contrast, cycle, illumination, light, rhythm, time, visibility
- `ن ه ر B003` — فتح الشيء وتوسيعه حتى يسيل أو ينفسح
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ن ف س, و ق ي
  - themes: anatomy, change_transition, containment_access, control_restraint, disease_injury, form_structure, space, substance_texture
  - keywords: anatomy, expansion, fluid, injury, release, space
- `ن ه ر B004` — زجر بكلام مغلظ
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, و ق ي
  - themes: authority_governance, communication, conflict, control_restraint, ethics_morality, language_speech, social_relations
  - keywords: authority, communication, conflict, discipline, ethics, sociality, speech
- `ن ه ر B005` — النَّهار فرخ طير
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ل ي ل, ن ف س, و ق ي
  - themes: animal, growth_decay, life_stage_aging, naming_classification, physiology, reproduction_birth, wildlife
  - keywords: animal, biology, birth, growth, infancy, ornithology, reproduction, taxonomy, wildlife, zoology
- `ن ه ر B006` — الدغرة والخلسة
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, و ق ي
  - themes: concealment_disclosure, conflict, control_restraint, deception_corruption, habitat_ecology, law, reasoning_decision, violence_warfare
  - keywords: conflict, deception, predation, strategy, violence
- `ن ه ر B007` — أعلام وأسماء خاصة
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, و ق ي
  - themes: culture_tradition, geography_landscape, identity_personhood, naming_classification, sky_astronomy, water_hydrology, writing_text
  - keywords: astronomy, culture, geography, hydrology, identity, onomastics
- `ن ه ر B008` — النَّاهُور سحاب
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, ف ج ر, ق م ر, ل ي ل, ن ف س
  - themes: sky_astronomy, water_hydrology, weather_climate
  - keywords: atmosphere, climate, meteorology, sky, water, weather

### ج ل و

- `ج ل و B001` — الكشف والظهور
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: belief_revelation, communication, emotion, health_medicine, knowledge_learning, light_darkness, perception, proof_uncertainty
  - keywords: communication, emotion, illumination, knowledge, light, visibility
- `ج ل و B002` — الصقل والتجلية
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ن ف س, ن ه ر, و ق ي
  - themes: craft, health_medicine, ornament_beauty, perception, proof_uncertainty, value_quality, weaponry
  - keywords: beauty, clarity, craft, medicine, perception, vision, weapon
- `ج ل و B003` — جلوة العروس
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر
  - themes: gender, kinship, marriage_genealogy, ornament_beauty, perception, ritual, social_relations
  - keywords: beauty, gender, kinship, ritual, sociality, society, visibility, wedding
- `ج ل و B004` — الجلاء عن الوطن
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ه ر
  - themes: household_community, law, migration_displacement, place_location, politics_order, violence_warfare
  - keywords: community, exile, law, migration, violence
- `ج ل و B005` — انكشاف مقدّم الرأس
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: anatomy, body, health_medicine, identity_personhood, life_stage_aging, physiology, visual_appearance
  - keywords: appearance, body, identity, medicine, physiology
- `ج ل و B006` — الشهرة وابن جلا
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: cognition, communication, hierarchy_status, honor_shame, identity_personhood, knowledge_learning, language_speech, memory_attention, social_relations
  - keywords: communication, identity, knowledge, language, memory, recognition, reputation, society, status
- `ج ل و B007` — بياض اليوم وصفاء الجو
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: habitat_ecology, light_darkness, perception, proof_uncertainty, sky_astronomy, time, weather_climate
  - keywords: clarity, environment, light, nature, perception, sky, time, weather
- `ج ل و B008` — النظر المتطلع
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: animal, memory_attention, motion, orientation_direction, perception, wildlife
  - keywords: animal, attention, hunting, motion, orientation, perception, vision
- `ج ل و B009` — عطية الجلوة
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, و ق ي
  - themes: commerce_exchange, economy, hospitality_welfare, household_community, kinship, marriage_genealogy, obligation_contract, ritual
  - keywords: economy, exchange, gift, household, kinship, marriage, obligation, ritual, wedding

### ل ي ل

- `ل ي ل B001` — الليل خلاف النهار وظلمته
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ن ف س, ن ه ر, و ق ي
  - themes: concealment_disclosure, habitat_ecology, light_darkness, orientation_direction, reasoning_decision, sequence_cycle, sky_astronomy, time
  - keywords: astronomy, contrast, cosmos, cycle, environment, time
- `ل ي ل B002` — مزاولة الأمر في الليل
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: calendar_season, commerce_exchange, labor_work, motion, ritual, time, travel
  - keywords: commerce, labor, mobility, ritual, time, travel
- `ل ي ل B003` — الليلة القريبة من اليوم
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ن ف س, ن ه ر, و ق ي
  - themes: boundary, calendar_season, grammar_expression, language_speech, orientation_direction, place_location, sequence_cycle, time
  - keywords: boundary, calendar, deixis, orientation, proximity, sequence, speech, time
- `ل ي ل B004` — التسمية بليلى
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ق م ر, ن ف س, ن ه ر, و ق ي
  - themes: cooking_drink, culture_tradition, gender, identity_personhood, naming_classification, rhetoric_discourse
  - keywords: culture, gender, identity, metonymy, onomastics, woman

### غ ش و

- `غ ش و B001` — غطاء يعلو الشيء ويستره
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: boundary, concealment_disclosure, perception, protection_security, storage_vessels, surface_shape, textile_clothing, tools_equipment
  - keywords: container, equipment, perception, protection, surface, textile
- `غ ش و B002` — غاشية تعم وتجلل
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ط ح و, ف ج ر, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: afterlife_eschatology, danger_harm, disease_injury, household_community, justice_judgment, punishment_sanction, social_relations, suffering_hardship
  - keywords: collectivity, disaster, disease, punishment, society
- `غ ش و B003` — إتيان يغشى المقصود
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ط ح و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: motion, place_location, social_relations, travel
  - keywords: encounter, mobility, movement, proximity, sociality, travel
- `غ ش و B004` — غشيان المرأة كناية عن الجماع
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, ف ج ر, ل ه م, ل ي ل, ن ف س, ن ه ر
  - themes: body, containment_access, kinship, marriage_genealogy, posture_embodiment, reproduction_birth, rhetoric_discourse, sexuality
  - keywords: body, embodiment, kinship, marriage, reproduction, sexuality
- `غ ش و B005` — غشية تغطي الوعي
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ض ح و, ط ح و, ف ج ر, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: body, capacity_ability, cognition, danger_harm, disease_injury, health_medicine, mortality_death
  - keywords: awareness, body, cognition, consciousness, crisis, death, illness, medicine, mortality
- `غ ش و B006` — إلباس الضربة بالسوط أو السيف
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, ف ج ر, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: body, conflict, control_restraint, disease_injury, punishment_sanction, suffering_hardship, violence_warfare, weaponry
  - keywords: body, conflict, discipline, injury, pain, punishment, violence, weapon, weaponry
- `غ ش و B007` — بياض يغشى وجه الحيوان
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: anatomy, animal, livestock, naming_classification, visual_appearance
  - keywords: anatomy, animal, appearance, classification, color, livestock, taxonomy, zoology

### س م و

- `س م و B001` — العلو والارتفاع
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س و ي, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر
  - themes: hierarchy_status, honor_shame, orientation_direction, perception, space
  - keywords: hierarchy, honor, perception, reputation, spatiality, status, verticality
- `س م و B002` — الشخص المرتفع الظاهر
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: concealment_disclosure, measurement, orientation_direction, perception, place_location, sky_astronomy, space
  - keywords: astronomy, distance, orientation, perception, spatiality, visibility
- `س م و B003` — تطاول الفحل على الشول
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: animal, authority_governance, hierarchy_status, husbandry, livestock, motion, reproduction_birth, sexuality, violence_warfare
  - keywords: aggression, livestock, motion, reproduction, sexuality, zoology
- `س م و B004` — السماء وما علا فأظل
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: agriculture, anatomy, architecture_construction, sky_astronomy, terrain_desert, weather_climate
  - keywords: agriculture, anatomy, architecture, cosmology, meteorology, shelter, weather
- `س م و B005` — الاسم تنويه ودلالة
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: cognition, communication, identity_personhood, kinship, language_speech, naming_classification, reasoning_decision
  - keywords: classification, identity, kinship, language, recognition
- `س م و B006` — الخروج للصيد
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: animal, habitat_ecology, motion, navigation_route, provision_resource, tools_equipment, wildlife
  - keywords: animal, hunting, mobility, predation, wildlife
- `س م و B007` — المساماة والمباراة
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: agency_action, conflict, hierarchy_status, honor_shame, reasoning_decision, value_quality
  - keywords: comparison, competition, conflict, honor, performance, status
- `س م و B008` — الصيت الحسن المنتشر
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: communication, concealment_disclosure, ethics_morality, honor_shame, memory_attention, social_relations
  - keywords: communication, ethics, memory, praise, publicity, reputation, sociality

### ب ن ي

- `ب ن ي B001` — بناء الشيء بضم بعضه إلى بعض
  - activated_by_or_with: ء ر ض, ج ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: architecture_construction, containment_access, craft, form_structure, household_community, material, place_location
  - keywords: architecture, composition, craft
- `ب ن ي B002` — البِنْية والهيئة المركبة
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س م و, س و ي, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: anatomy, cognition, form_structure, physiology, politics_order, posture_embodiment
  - keywords: anatomy, composition, embodiment, ontology, order, physiology
- `ب ن ي B003` — البِنْية للبيت الحرام ومكة
  - activated_by_or_with: ء ر ض, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: architecture_construction, geography_landscape, pilgrimage_sacrifice, place_location, religion_worship
  - keywords: architecture, geography, place, religion, sanctity, worship
- `ب ن ي B004` — المَبْناة بيت أو غطاء من أدم
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ق م ر, ن ف س, ن ه ر, و ق ي
  - themes: architecture_construction, craft, material, protection_security, storage_vessels, textile_clothing, tools_equipment, weather_climate
  - keywords: container, craft, equipment, leather, protection, shelter, textile, weather
- `ب ن ي B005` — قوس بانية تلصق بوترها
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ن ف س, ن ه ر
  - themes: force_power, material, social_relations, substance_texture, weaponry
  - keywords: material, pressure, weapon, weaponry
- `ب ن ي B006` — بناء الرجل على أهله ودخوله بها
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ل ه م, ل ي ل, ن ف س, ن ه ر
  - themes: change_transition, gender, household_community, kinship, marriage_genealogy, ritual, sexuality
  - keywords: gender, household, kinship, marriage, sexuality, transition
- `ب ن ي B007` — البُنُوَّة والنسب وما ينسب إلى منشأ
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: identity_personhood, kinship, marriage_genealogy, motion, naming_classification, reproduction_birth, sequence_cycle, social_relations, wealth_property
  - keywords: identity, kinship, sociality, taxonomy
- `ب ن ي B008` — تسميات الابن والبنت للأشياء المتفرعة أو الصغيرة
  - activated_by_or_with: ء ر ض, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: geography_landscape, material, measurement, naming_classification, plant_vegetation, rhetoric_discourse, space
  - keywords: geography, landscape, material, metonymy, scale, taxonomy, vegetation
- `ب ن ي B009` — البَواني أضلاع ودعائم يستقر بها الشيء
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س م و, س و ي, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: anatomy, architecture_construction, form_structure, place_location, posture_embodiment, stability_endurance, support_dependence
  - keywords: anatomy, architecture, posture, support
- `ب ن ي B010` — بناء الطعام للحم ونماؤه
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س م و, س و ي, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: body, food_nutrition, growth_decay, health_medicine, physiology, provision_resource
  - keywords: body, food, growth, health, nourishment, physiology, sustenance

### ء ر ض

- `ء ر ض B001` — السفل المقابل للسماء
  - activated_by_or_with: ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: animal, body, geography_landscape, habitat_ecology, orientation_direction, sky_astronomy, support_dependence, terrain_desert
  - keywords: animal, body, cosmology, cosmos, geography, habitat, orientation, terrain, verticality
- `ء ر ض B002` — الأرض اللينة المنبتة
  - activated_by_or_with: ب ن ي, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: abundance_scarcity, agriculture, food_nutrition, growth_decay, habitat_ecology, pasture_forage, plant_vegetation
  - keywords: abundance, agriculture, botany, ecology, growth, habitat, nourishment, pasture, vegetation
- `ء ر ض B003` — الخليق بالخير كالأرض الأريضة
  - activated_by_or_with: ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: agency_action, capacity_ability, ethics_morality, hospitality_welfare, intention_character, value_quality
  - keywords: agency, character, ethics, virtue
- `ء ر ض B004` — ابن الأرض الغريب
  - activated_by_or_with: ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر
  - themes: geography_landscape, identity_personhood, kinship, migration_displacement, social_relations, travel
  - keywords: exile, geography, identity, kinship, migration, society, travel
- `ء ر ض B005` — الإراض البساط الضخم
  - activated_by_or_with: ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ن ف س, و ق ي
  - themes: architecture_construction, craft, health_medicine, household_community, material, ornament_beauty, textile_clothing, tools_equipment
  - keywords: craft, household, material, shelter, textile
- `ء ر ض B006` — لزوم الأرض والتثاقل إليها
  - activated_by_or_with: ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: agency_action, force_power, motion, physiology, posture_embodiment, reasoning_decision, stability_endurance, suffering_hardship, time
  - keywords: behavior, delay, motion, posture
- `ء ر ض B007` — التعرض والتصدي
  - activated_by_or_with: ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: agency_action, conflict, force_power, motion, social_relations
  - keywords: agency, competition, conflict, encounter, pressure, pursuit, sociality
- `ء ر ض B008` — الأَرْض الرعدة
  - activated_by_or_with: ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: disease_injury, emotion, health_medicine, motion, physiology, suffering_hardship
  - keywords: emotion, illness, medicine, motion, neurology, physiology
- `ء ر ض B009` — الأَرْض الزكام
  - activated_by_or_with: ب ن ي, ت ل و, ج ل و, س و ي, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: body, disease_injury, health_medicine, physiology
  - keywords: body, disease, medicine, respiration
- `ء ر ض B010` — الأَرَضَة آكلة الخشب
  - activated_by_or_with: ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: animal, craft, danger_harm, food_nutrition, growth_decay, habitat_ecology, material, wildlife
  - keywords: animal, consumption, decay, destruction, ecology, material, zoology
- `ء ر ض B011` — فساد القرحة بالمدة
  - activated_by_or_with: ب ن ي, ت ل و, ج ل و, س و ي, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: body, disease_injury, growth_decay, health_medicine, substance_texture
  - keywords: body, decay, disease, fluid, injury, medicine
- `ء ر ض B012` — المأروض المخبول من أهل الأرض
  - activated_by_or_with: ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, و ق ي
  - themes: agency_action, belief_revelation, body, cognition, health_medicine, motion, religion_worship, suffering_hardship, wealth_property
  - keywords: agency, body, motion, neurology, possession, psychology

### ط ح و

- `ط ح و B001` — البَسْط والمَدّ
  - activated_by_or_with: ء ر ض, ب ن ي, س م و, س و ي, ش م س, ض ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: change_transition, geography_landscape, measurement, space, surface_shape, terrain_desert
  - keywords: expansion, landscape, space, surface, terrain
- `ط ح و B002` — الذهاب المُمْتَدّ
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: cognition, emotion, geography_landscape, measurement, motion, orientation_direction, travel
  - keywords: cognition, distance, emotion, motion, movement, orientation, psychology, travel
- `ط ح و B003` — دَوَران النسور
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: animal, habitat_ecology, mortality_death, motion, sequence_cycle, sky_astronomy, violence_warfare, wildlife
  - keywords: animal, bird, cycle, death, predation, sky, warfare
- `ط ح و B004` — الدَّفْع بين الناس
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: conflict, force_power, household_community, motion, naming_classification, social_relations, stability_endurance, violence_warfare
  - keywords: conflict, contact, crowd, motion, society, violence
- `ط ح و B005` — الكثرة والضخامة
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, س و ي, ش م س, ض ح و, غ ش و, ف ج ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: architecture_construction, household_community, measurement, quantity_number, violence_warfare
  - keywords: architecture, mass, quantity, scale
- `ط ح و B006` — الانبطاح واللُّصوق بالأرض
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: animal, body, earth_geology, force_power, geography_landscape, plant_vegetation, posture_embodiment, social_relations
  - keywords: animal, body, botany, contact, impact, posture
- `ط ح و B007` — الهلاك
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: belief_revelation, danger_harm, grammar_expression, loss_absence, mortality_death, naming_classification, sequence_cycle, stability_endurance
  - keywords: death, disaster, ending, harm, loss, mortality, negation
- `ط ح و B008` — الارتفاع
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: afterlife_eschatology, light_darkness, measurement, motion, orientation_direction, perception, place_location, sky_astronomy, space
  - keywords: astronomy, light, motion, position, sky, space, verticality, visibility

### ن ف س

- `ن ف س B001` — خروج النسيم من الجوف
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ه ر, و ق ي
  - themes: anatomy, body, language_speech, motion, physiology, weather_climate
  - keywords: anatomy, body, motion, physiology, respiration
- `ن ف س B002` — توسيع الكربة بالتنفيس
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ن ه ر, و ق ي
  - themes: change_transition, control_restraint, emotion, ethics_morality, protection_security, suffering_hardship, support_dependence
  - keywords: emotion, mercy, support
- `ن ف س B003` — إصابة العين بالنفس
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ن ه ر, و ق ي
  - themes: belief_revelation, danger_harm, disease_injury, emotion, intention_character, perception, protection_security, punishment_sanction
  - keywords: envy, harm, injury, perception, protection, vision
- `ن ف س B004` — الدم السائل قوام النفس
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س و ي, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ن ه ر, و ق ي
  - themes: body, disease_injury, health_medicine, mortality_death, physiology, posture_embodiment
  - keywords: biology, blood, body, embodiment, injury, medicine, mortality, physiology, vitality
- `ن ف س B005` — خروج الولد ودم النفاس
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ه ر, و ق ي
  - themes: gender, health_medicine, kinship, life_stage_aging, physiology, reproduction_birth
  - keywords: blood, fertility, infancy, kinship, lifecycle, reproduction, woman
- `ن ف س B006` — نفس الشرب وجرعته
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ه ر, و ق ي
  - themes: cooking_drink, desire_appetite, food_nutrition, measurement, sequence_cycle, time, water_hydrology
  - keywords: consumption, hydration, measure, rhythm, thirst, water
- `ن ف س B007` — قدر دبغة يسيرة
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ل ي ل, ن ه ر, و ق ي
  - themes: agency_action, animal, craft, labor_work, material, measurement
  - keywords: animal, craft, leather, material, measure
- `ن ف س B008` — ماء تقام به النفس
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ه ر, و ق ي
  - themes: abundance_scarcity, desire_appetite, food_nutrition, habitat_ecology, health_medicine, physiology, provision_resource, stability_endurance, water_hydrology
  - keywords: abundance, ecology, hydration, life, nourishment, resource, thirst, water
- `ن ف س B009` — انفتاح الصبح والشيء كالنفس
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ه ر, و ق ي
  - themes: change_transition, habitat_ecology, light_darkness, motion, time, water_hydrology
  - keywords: emergence, expansion, light, motion, nature, time, water
- `ن ف س B010` — شيء نفيس تتنافس فيه النفوس
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ن ه ر, و ق ي
  - themes: conflict, desire_appetite, economy, emotion, hierarchy_status, value_quality, wealth_property
  - keywords: appetite, competition, envy, possession, status, valuation, wealth
- `ن ف س B011` — النفس التي بها الحياة
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ه ر, و ق ي
  - themes: belief_revelation, body, cognition, identity_personhood, mortality_death, physiology, posture_embodiment, religion_worship
  - keywords: biology, body, death, embodiment, identity, life, mortality, ontology, religion
- `ن ف س B012` — عين الشيء وذاته
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ه ر, و ق ي
  - themes: cognition, identity_personhood, naming_classification, proof_uncertainty, reasoning_decision, rhetoric_discourse, substance_texture, value_quality
  - keywords: identity, logic, ontology, reference, truth
- `ن ف س B013` — ما في النفس من عقل وروع
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ه ر
  - themes: agency_action, cognition, concealment_disclosure, containment_access, intention_character, knowledge_learning, reasoning_decision
  - keywords: agency, awareness, cognition, consciousness, intention, psychology, secrecy
- `ن ف س B014` — قوة النفس وخلقها
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, ف ج ر, ق م ر, ل ه م, ن ه ر, و ق ي
  - themes: desire_appetite, emotion, ethics_morality, hierarchy_status, honor_shame, hospitality_welfare, intention_character
  - keywords: character, emotion, ethics, generosity, status, virtue
- `ن ف س B015` — سعة ومسافة ومهلة
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ه ر, و ق ي
  - themes: calendar_season, geography_landscape, intention_character, measurement, space, time
  - keywords: delay, distance, geography, measure, patience, space, time
- `ن ف س B016` — النافس سهم الميسر الخامس
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ه ر
  - themes: belief_revelation, conflict, proof_uncertainty, recreation_sport, ritual
  - keywords: chance, competition, game, gaming, ritual

### س و ي

- `س و ي B001` — مساواة ومعادلة بين شيئين
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: commerce_exchange, justice_judgment, quantity_number, reasoning_decision, social_relations, stability_endurance, surface_shape, value_quality
  - keywords: balance, commerce, comparison, justice, relation, valuation
- `س و ي B002` — استقامة وتمام في الذات
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: change_transition, craft, ethics_morality, form_structure, growth_decay, health_medicine, husbandry, politics_order
  - keywords: development, ethics, health, husbandry, morality, order
- `س و ي B003` — علو واستقرار على شيء
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: authority_governance, control_restraint, force_power, motion, orientation_direction, place_location, posture_embodiment, transport
  - keywords: authority, control, locomotion, motion, position, posture, power, transportation
- `س و ي B004` — إقبال وقصد إلى جهة
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: authority_governance, intention_character, memory_attention, motion, navigation_route, orientation_direction
  - keywords: attention, intention, movement, navigation, orientation
- `س و ي B005` — بلوغ وتمام الشباب
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, ط ح و, غ ش و, ق م ر, ل ه م, ن ف س, ن ه ر
  - themes: cognition, growth_decay, life_stage_aging, physiology
  - keywords: cognition, development, growth, life, lifecycle, physiology, psychology
- `س و ي B006` — وسط وعدل ومكان منصف
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: ethics_morality, geography_landscape, justice_judgment, law, navigation_route, orientation_direction, rhetoric_discourse, stability_endurance
  - keywords: balance, ethics, geography, justice, law, navigation, orientation
- `س و ي B007` — مباينة وكون الشيء غيره
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: boundary, change_transition, grammar_expression, identity_personhood, reasoning_decision, social_relations
  - keywords: boundary, deixis, grammar, identity, logic, negation, relation
- `س و ي B008` — قصد نحو شخص أو جهة
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر
  - themes: communication, honor_shame, intention_character, memory_attention, orientation_direction, rhetoric_discourse, social_relations
  - keywords: attention, communication, intention, orientation, praise, sociality, society
- `س و ي B009` — السِيّ واسع أملس من الأرض
  - activated_by_or_with: ء ر ض, ب ن ي, ج ل و, س م و, ش م س, ض ح و, ط ح و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: abundance_scarcity, geography_landscape, habitat_ecology, pasture_forage, space, terrain_desert, water_hydrology
  - keywords: abundance, ecology, geography, hydrology, landscape, pasture, space, terrain, water
- `س و ي B010` — السَّويّة على ظهر البعير
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, ش م س, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: animal, migration_displacement, textile_clothing, tools_equipment, transport, travel
  - keywords: animal, equipment, riding, textile, transport, transportation, travel
- `س و ي B011` — إسقاط وإغفال
  - activated_by_or_with: ت ل و, ج ل و, س م و, ش م س, ط ح و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر
  - themes: communication, grammar_expression, loss_absence, memory_attention, proof_uncertainty, writing_text
  - keywords: grammar, memory
- `س و ي B012` — ليلة استواء القمر
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, ش م س, ض ح و, ط ح و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر
  - themes: calendar_season, light_darkness, ritual, sequence_cycle, sky_astronomy, time
  - keywords: astronomy, calendar, cycle, illumination, ritual, sky, time
- `س و ي B013` — سِيّ الرأس وقدر يوازي الرأس من مال أو نعمة
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: economy, finance_debt, grammar_expression, identity_personhood, measurement, posture_embodiment, value_quality, wealth_property
  - keywords: accounting, economy, embodiment, finance, measure, valuation, wealth

### ل ه م

- `ل ه م B001` — ابتلاع الشيء واستيفاؤه
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ن ف س, ن ه ر, و ق ي
  - themes: abundance_scarcity, animal, body, change_transition, containment_access, desire_appetite, food_nutrition, physiology, posture_embodiment
  - keywords: animal, appetite, body, consumption, embodiment, feeding, nourishment
- `ل ه م B002` — إلقاء في الروع وتلقين الباطن
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ل ه م B003` — عدو يلتهم الأرض
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: animal, motion, terrain_desert, transport, travel
  - keywords: animal, movement, pursuit, terrain, transport, travel
- `ل ه م B004` — عظم وسعة وغزارة وجوادية
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ن ف س, ن ه ر, و ق ي
  - themes: abundance_scarcity, force_power, hospitality_welfare, measurement, provision_resource, reproduction_birth, wealth_property
  - keywords: abundance, fertility, generosity, power, provision, scale, wealth
- `ل ه م B005` — داهية تلتهم ما تلقى
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س م و, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ن ف س, ن ه ر, و ق ي
  - themes: danger_harm, disease_injury, mortality_death, violence_warfare
  - keywords: death, destruction, disaster, disease, mortality, violence

### ف ج ر

- `ف ج ر B001` — انشقاق واسع وانبعاث
  - activated_by_or_with: ء ر ض, ب ن ي, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ن ف س, ن ه ر, و ق ي
  - themes: change_transition, control_restraint, earth_geology, force_power, navigation_route, water_hydrology
  - keywords: emergence, hydrology, pressure, release
- `ف ج ر B002` — انبلاج الصبح من الليل
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: boundary, change_transition, light_darkness, perception, sequence_cycle, sky_astronomy, time
  - keywords: boundary, cosmology, cycle, illumination, light, perception, time, transition
- `ف ج ر B003` — اندفاع الكثير بغتة
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: danger_harm, emotion, force_power, household_community, motion, sequence_cycle, suffering_hardship, violence_warfare
  - keywords: collectivity, crisis, crowd, disaster, impact, movement
- `ف ج ر B004` — انحراف عن الحق وخرق الستر
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, غ ش و, ق م ر, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: concealment_disclosure, deception_corruption, ethics_morality, law, proof_uncertainty, religion_worship
  - keywords: ethics, law, morality, religion, secrecy, taboo, truth
- `ف ج ر B005` — جود متفجر واسع
  - activated_by_or_with: ء ر ض, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: abundance_scarcity, commerce_exchange, economy, ethics_morality, hospitality_welfare
  - keywords: abundance, economy, exchange, gift, virtue
- `ف ج ر B006` — وقائع الفجار لانتهاك الحرمة
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر, و ق ي
  - themes: conflict, ethics_morality, kinship, law, memory_attention, religion_worship, ritual, time, violence_warfare
  - keywords: conflict, law, memory, ritual, sanctity, taboo, warfare

### و ق ي

- `و ق ي B001` — دفع الضرر بوقاية
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, س م و, س و ي, ش م س, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س
  - themes: architecture_construction, boundary, danger_harm, protection_security
  - keywords: boundary, protection, risk, security, shelter
- `و ق ي B002` — جعل النفس في وقاية
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ن ف س, ن ه ر
  - themes: afterlife_eschatology, control_restraint, ethics_morality, justice_judgment, purity_cleansing, religion_worship
  - keywords: devotion, discipline, ethics, purity, religion
- `و ق ي B003` — توقي الدابة من وجع الحافر
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر
  - themes: anatomy, animal, health_medicine, motion, protection_security, suffering_hardship, terrain_desert, tools_equipment, transport
  - keywords: anatomy, animal, equipment, locomotion, pain, riding, terrain
- `و ق ي B004` — الأوقية وزن معلوم
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ط ح و, ف ج ر, ق م ر, ل ه م, ل ي ل, ن ف س
  - themes: commerce_exchange, economy, finance_debt, measurement, quantity_number, value_quality
  - keywords: accounting, economy, mass, quantity
- `و ق ي B005` — الواقي اسم للصرد
  - activated_by_or_with: ء ر ض, ب ن ي, ت ل و, ج ل و, س م و, س و ي, ش م س, ض ح و, ط ح و, غ ش و, ق م ر, ل ه م, ل ي ل, ن ف س, ن ه ر
  - themes: animal, habitat_ecology, language_speech, naming_classification, wildlife
  - keywords: animal, bird, ecology, language, naming, nature, taxonomy, wildlife, zoology

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
