# v11 Activation Packet — S96:9-16

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_9: أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ
- verse_10: عَبْدًا إِذَا صَلَّىٰٓ
- verse_11: أَرَءَيْتَ إِن كَانَ عَلَى ٱلْهُدَىٰٓ
- verse_12: أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ
- verse_13: أَرَءَيْتَ إِن كَذَّبَ وَتَوَلَّىٰٓ
- verse_14: أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ
- verse_15: كَلَّا لَئِن لَّمْ يَنتَهِ لَنَسْفَعًۢا بِٱلنَّاصِيَةِ
- verse_16: نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ر ء ي → ن ه ي → ع ب د → ص ل و → ك و ن → ه د ي → ء م ر → و ق ي → ك ذ ب → و ل ي → ع ل م → ء ل ه → س ف ع → ن ص ي → خ ط ء

## Branch inventory summary

- ر ء ي: 13 branches (13 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن ه ي: 10 branches (10 with Qnet bridge-theme nodes; 0 Furūq-only)
- ع ب د: 12 branches (11 with Qnet bridge-theme nodes; 1 Furūq-only)
- ص ل و: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- ك و ن: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- ه د ي: 11 branches (11 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء م ر: 11 branches (10 with Qnet bridge-theme nodes; 1 Furūq-only)
- و ق ي: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- ك ذ ب: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- و ل ي: 16 branches (15 with Qnet bridge-theme nodes; 1 Furūq-only)
- ع ل م: 7 branches (6 with Qnet bridge-theme nodes; 1 Furūq-only)
- ء ل ه: 2 branches (2 with Qnet bridge-theme nodes; 0 Furūq-only)
- س ف ع: 7 branches (6 with Qnet bridge-theme nodes; 1 Furūq-only)
- ن ص ي: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- خ ط ء: 3 branches (3 with Qnet bridge-theme nodes; 0 Furūq-only)

## QAC-first root resolution audit

- ر ء ي | qac_keys=رءي | status=resolved | matches=root_000531
- ن ه ي | qac_keys=نهي | status=resolved | matches=root_001560
- ع ب د | qac_keys=عبد | status=resolved | matches=root_000973
- ص ل و | qac_keys=صلو | status=resolved | matches=root_000879
- ك و ن | qac_keys=كون | status=resolved | matches=root_001332
- ه د ي | qac_keys=هدي | status=resolved | matches=root_001583
- ء م ر | qac_keys=ءمر | status=resolved | matches=root_000051
- و ق ي | qac_keys=وقي | status=resolved | matches=root_001677
- ك ذ ب | qac_keys=كذب | status=resolved | matches=root_001290
- و ل ي | qac_keys=ولي | status=resolved | matches=root_001684
- ع ل م | qac_keys=علم | status=resolved | matches=root_001040
- ء ل ه | qac_keys=ءله | status=resolved | matches=root_000047
- س ف ع | qac_keys=سفع | status=resolved | matches=root_000713
- ن ص ي | qac_keys=نصي | status=resolved | matches=root_001512
- خ ط ء | qac_keys=خطء | status=resolved | matches=root_000420

## Top candidate bridges

- `ص ل و B009` ↔ `ن ص ي B004` | score_hint=25 | discovery_hint=20 | themes=habitat_ecology, pasture_forage, plant_vegetation, provision_resource | keywords=botany, ecology, forage, pasture | q2=—
- `ع ب د B003` ↔ `ء ل ه B001` | score_hint=24 | discovery_hint=13 | themes=authority_governance, belief_revelation, religion_worship, ritual | keywords=authority, religion, submission, theology | q2=—
- `و ق ي B005` ↔ `ع ل م B007` | score_hint=24 | discovery_hint=14 | themes=animal, habitat_ecology, naming_classification, wildlife | keywords=ecology, taxonomy, wildlife, zoology | q2=—
- `و ل ي B010` ↔ `خ ط ء B003` | score_hint=24 | discovery_hint=16 | themes=agriculture, geography_landscape, water_hydrology, weather_climate | keywords=agriculture, climate, water, weather | q2=—
- `ن ه ي B004` ↔ `ع ل م B005` | score_hint=22 | discovery_hint=14 | themes=geography_landscape, habitat_ecology, water_hydrology | keywords=geography, hydrology, nature, water | q2=—
- `ن ه ي B004` ↔ `خ ط ء B003` | score_hint=22 | discovery_hint=14 | themes=geography_landscape, habitat_ecology, water_hydrology | keywords=geography, landscape, nature, water | q2=—
- `ك ذ ب B007` ↔ `س ف ع B005` | score_hint=22 | discovery_hint=14 | themes=habitat_ecology, motion, navigation_route | keywords=motion, predation, pursuit, tracking | q2=—
- `ك ذ ب B009` ↔ `س ف ع B007` | score_hint=22 | discovery_hint=14 | themes=ornament_beauty, textile_clothing, visual_appearance | keywords=adornment, appearance, clothing, textile | q2=—
- `ص ل و B009` ↔ `ك ذ ب B006` | score_hint=20 | discovery_hint=15 | themes=animal, food_nutrition, livestock, provision_resource | keywords=animal, livestock, subsistence | q2=—
- `ء م ر B005` ↔ `ع ل م B002` | score_hint=20 | discovery_hint=13 | themes=communication, navigation_route, orientation_direction, pattern_marking | keywords=navigation, orientation, semiotics | q2=—
- `و ق ي B005` ↔ `ع ل م B006` | score_hint=20 | discovery_hint=13 | themes=animal, habitat_ecology, naming_classification, wildlife | keywords=taxonomy, wildlife, zoology | q2=—
- `ع ل م B005` ↔ `خ ط ء B003` | score_hint=20 | discovery_hint=13 | themes=abundance_scarcity, geography_landscape, habitat_ecology, water_hydrology | keywords=geography, nature, water | q2=—
- `ن ه ي B010` ↔ `و ق ي B004` | score_hint=19 | discovery_hint=20 | themes=finance_debt, measurement, quantity_number | keywords=accounting, measurement, quantity | q2=—
- `ه د ي B001` ↔ `و ق ي B002` | score_hint=19 | discovery_hint=16 | themes=afterlife_eschatology, ethics_morality, religion_worship | keywords=ethics, religion, salvation | q2=—
- `ر ء ي B005` ↔ `ك ذ ب B008` | score_hint=18 | discovery_hint=13 | themes=deception_corruption, ethics_morality, intention_character | keywords=deception, intention, morality | q2=—
- `ر ء ي B006` ↔ `ن ص ي B002` | score_hint=18 | discovery_hint=14 | themes=body, ornament_beauty, visual_appearance | keywords=appearance, beauty, body | q2=—
- `ر ء ي B010` ↔ `ص ل و B005` | score_hint=18 | discovery_hint=15 | themes=animal, body, reproduction_birth | keywords=animal, body, reproduction | q2=—
- `ر ء ي B010` ↔ `و ل ي B015` | score_hint=18 | discovery_hint=14 | themes=agriculture, animal, husbandry | keywords=agriculture, animal, husbandry | q2=—
- `ن ه ي B001` ↔ `ء م ر B002` | score_hint=18 | discovery_hint=12 | themes=ethics_morality, language_speech, law | keywords=law, norm, speech | q2=—
- `ن ه ي B003` ↔ `خ ط ء B001` | score_hint=18 | discovery_hint=12 | themes=cognition, ethics_morality, justice_judgment | keywords=cognition, judgment, morality | q2=—
- `ن ه ي B006` ↔ `ص ل و B009` | score_hint=18 | discovery_hint=14 | themes=animal, food_nutrition, livestock | keywords=animal, food, livestock | q2=—
- `ن ه ي B008` ↔ `ع ل م B005` | score_hint=18 | discovery_hint=14 | themes=habitat_ecology, measurement, water_hydrology | keywords=hydrology, nature, water | q2=—
- `ع ب د B003` ↔ `ص ل و B003` | score_hint=18 | discovery_hint=13 | themes=authority_governance, religion_worship, ritual | keywords=devotion, religion, ritual | q2=—
- `ع ب د B003` ↔ `و ل ي B004` | score_hint=18 | discovery_hint=14 | themes=belief_revelation, religion_worship, trust_loyalty | keywords=allegiance, devotion, faith | q2=—
- `ع ب د B005` ↔ `و ل ي B011` | score_hint=18 | discovery_hint=13 | themes=animal, transport, travel | keywords=animal, transport, travel | q2=—
- `ع ب د B007` ↔ `س ف ع B004` | score_hint=18 | discovery_hint=15 | themes=animal, body, force_power | keywords=animal, body, force | q2=—
- `ع ب د B009` ↔ `ك ذ ب B005` | score_hint=18 | discovery_hint=13 | themes=agency_action, speed, time | keywords=speed, time, urgency | q2=—
- `ص ل و B002` ↔ `ء م ر B002` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, language_speech, ritual | keywords=ethic, ritual, speech | q2=—
- `ص ل و B003` ↔ `ء م ر B002` | score_hint=18 | discovery_hint=13 | themes=authority_governance, law, ritual | keywords=law, obedience, ritual | q2=—
- `ص ل و B006` ↔ `ه د ي B003` | score_hint=18 | discovery_hint=13 | themes=animal, motion, sequence_cycle | keywords=animal, motion, sequence | q2=—
- `ه د ي B008` ↔ `س ف ع B004` | score_hint=18 | discovery_hint=14 | themes=animal, body, motion | keywords=animal, body, motion | q2=—
- `ه د ي B010` ↔ `س ف ع B002` | score_hint=18 | discovery_hint=14 | themes=body, emotion, visual_appearance | keywords=appearance, body, emotion | q2=—
- `ء م ر B003` ↔ `و ل ي B003` | score_hint=18 | discovery_hint=14 | themes=authority_governance, force_power, law | keywords=governance, power, rule | q2=—
- `و ق ي B002` ↔ `خ ط ء B002` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, justice_judgment, religion_worship | keywords=accountability, ethics, religion | q2=—
- `و ق ي B003` ↔ `و ل ي B011` | score_hint=18 | discovery_hint=13 | themes=animal, tools_equipment, transport | keywords=animal, equipment, riding | q2=—
- `ك ذ ب B005` ↔ `و ل ي B002` | score_hint=18 | discovery_hint=13 | themes=sequence_cycle, stability_endurance, time | keywords=continuity, sequence, time | q2=—
- `ك ذ ب B007` ↔ `و ل ي B006` | score_hint=18 | discovery_hint=13 | themes=memory_attention, motion, perception | keywords=attention, motion, perception | q2=—
- `ك ذ ب B008` ↔ `خ ط ء B001` | score_hint=18 | discovery_hint=12 | themes=cognition, ethics_morality, intention_character | keywords=cognition, intention, morality | q2=—
- `س ف ع B001` ↔ `ن ص ي B001` | score_hint=18 | discovery_hint=12 | themes=anatomy, body, control_restraint, force_power, honor_shame | keywords=body, domination | q2=—
- `ر ء ي B005` ↔ `خ ط ء B002` | score_hint=16 | discovery_hint=13 | themes=ethics_morality, religion_worship | keywords=ethics, morality, religion | q2=—
- `ن ه ي B003` ↔ `ك ذ ب B008` | score_hint=16 | discovery_hint=13 | themes=cognition, ethics_morality | keywords=cognition, morality, psychology | q2=—
- `ن ه ي B003` ↔ `خ ط ء B002` | score_hint=16 | discovery_hint=13 | themes=ethics_morality, justice_judgment | keywords=ethics, judgment, morality | q2=—
- `ع ب د B009` ↔ `ك ذ ب B004` | score_hint=16 | discovery_hint=13 | themes=agency_action, motion | keywords=motion, movement, performance | q2=—
- `ص ل و B003` ↔ `ه د ي B005` | score_hint=16 | discovery_hint=13 | themes=religion_worship, ritual | keywords=religion, ritual, worship | q2=—
- `ص ل و B003` ↔ `و ق ي B002` | score_hint=16 | discovery_hint=13 | themes=control_restraint, religion_worship | keywords=devotion, discipline, religion | q2=—
- `ص ل و B006` ↔ `ك ذ ب B007` | score_hint=16 | discovery_hint=13 | themes=animal, motion | keywords=animal, motion, pursuit | q2=—
- `ص ل و B006` ↔ `س ف ع B005` | score_hint=16 | discovery_hint=13 | themes=conflict, motion | keywords=competition, motion, pursuit | q2=—
- `ص ل و B007` ↔ `ه د ي B005` | score_hint=16 | discovery_hint=13 | themes=religion_worship, ritual | keywords=religion, ritual, worship | q2=—
- `ه د ي B004` ↔ `و ل ي B014` | score_hint=16 | discovery_hint=15 | themes=commerce_exchange, wealth_property | keywords=commerce, exchange, property | q2=—
- `ك ذ ب B004` ↔ `س ف ع B004` | score_hint=16 | discovery_hint=13 | themes=motion, violence_warfare | keywords=combat, motion, violence | q2=—
- `ر ء ي B009` ↔ `ع ل م B004` | score_hint=16 | discovery_hint=13 | themes=anatomy, body, disease_injury, health_medicine | keywords=anatomy, body | q2=—
- `ن ه ي B006` ↔ `ك ذ ب B006` | score_hint=16 | discovery_hint=13 | themes=abundance_scarcity, animal, food_nutrition, livestock | keywords=animal, livestock | q2=—
- `ع ب د B001` ↔ `و ل ي B005` | score_hint=16 | discovery_hint=12 | themes=control_restraint, hierarchy_status, law, wealth_property | keywords=law, status | q2=—
- `ء م ر B006` ↔ `خ ط ء B001` | score_hint=16 | discovery_hint=12 | themes=ethics_morality, justice_judgment, measurement, value_quality | keywords=judgment, morality | q2=—
- `ع ب د B009` ↔ `ص ل و B006` | score_hint=15 | discovery_hint=16 | themes=motion, recreation_sport, speed | keywords=motion, speed | q2=—
- `ه د ي B005` ↔ `ء ل ه B001` | score_hint=15 | discovery_hint=15 | themes=pilgrimage_sacrifice, religion_worship, ritual | keywords=religion, sacrifice | q2=—
- `ر ء ي B001` ↔ `ع ل م B001` | score_hint=14 | discovery_hint=10 | themes=cognition, knowledge_learning, memory_attention | keywords=awareness, epistemology | q2=—
- `ر ء ي B002` ↔ `ء م ر B007` | score_hint=14 | discovery_hint=12 | themes=cognition, communication, reasoning_decision | keywords=decision, planning | q2=—
- `ر ء ي B002` ↔ `خ ط ء B001` | score_hint=14 | discovery_hint=11 | themes=cognition, justice_judgment, proof_uncertainty | keywords=cognition, judgment | q2=—
- `ر ء ي B004` ↔ `و ل ي B001` | score_hint=14 | discovery_hint=11 | themes=place_location, social_relations, space | keywords=relation, space | q2=—
- `ر ء ي B006` ↔ `ه د ي B010` | score_hint=14 | discovery_hint=13 | themes=body, ornament_beauty, visual_appearance | keywords=appearance, body | q2=—
- `ر ء ي B006` ↔ `ك ذ ب B009` | score_hint=14 | discovery_hint=12 | themes=ornament_beauty, perception, visual_appearance | keywords=appearance, perception | q2=—
- `ر ء ي B009` ↔ `ص ل و B005` | score_hint=14 | discovery_hint=14 | themes=anatomy, body, physiology | keywords=anatomy, body | q2=—
- `ر ء ي B009` ↔ `ن ص ي B006` | score_hint=14 | discovery_hint=14 | themes=body, health_medicine, physiology | keywords=body, medicine | q2=—
- `ر ء ي B011` ↔ `ع ل م B002` | score_hint=14 | discovery_hint=13 | themes=communication, identity_personhood, pattern_marking | keywords=identity, symbol | q2=—
- `ر ء ي B012` ↔ `ه د ي B001` | score_hint=14 | discovery_hint=11 | themes=belief_revelation, knowledge_learning, proof_uncertainty | keywords=revelation, teaching | q2=—
- `ن ه ي B003` ↔ `ء م ر B008` | score_hint=14 | discovery_hint=12 | themes=authority_governance, cognition, justice_judgment | keywords=judgment, psychology | q2=—
- `ن ه ي B003` ↔ `و ق ي B002` | score_hint=14 | discovery_hint=12 | themes=control_restraint, ethics_morality, justice_judgment | keywords=discipline, ethics | q2=—
- `ع ب د B003` ↔ `ص ل و B002` | score_hint=14 | discovery_hint=12 | themes=belief_revelation, religion_worship, ritual | keywords=devotion, ritual | q2=—
- `ع ب د B003` ↔ `ص ل و B007` | score_hint=14 | discovery_hint=12 | themes=authority_governance, religion_worship, ritual | keywords=religion, ritual | q2=—
- `ع ب د B004` ↔ `س ف ع B001` | score_hint=14 | discovery_hint=12 | themes=control_restraint, force_power, violence_warfare | keywords=power, violence | q2=—
- `ع ب د B007` ↔ `ص ل و B005` | score_hint=14 | discovery_hint=14 | themes=animal, body, physiology | keywords=animal, body | q2=—
- `ص ل و B003` ↔ `ك ذ ب B003` | score_hint=14 | discovery_hint=12 | themes=authority_governance, control_restraint, religion_worship | keywords=discipline, religion | q2=—
- `ص ل و B003` ↔ `و ل ي B005` | score_hint=14 | discovery_hint=12 | themes=control_restraint, household_community, law | keywords=community, law | q2=—
- `ص ل و B003` ↔ `ء ل ه B001` | score_hint=14 | discovery_hint=11 | themes=authority_governance, religion_worship, ritual | keywords=liturgy, religion | q2=—
- `ص ل و B004` ↔ `ء م ر B011` | score_hint=14 | discovery_hint=12 | themes=craft, tools_equipment, violence_warfare | keywords=craft, tool | q2=—
- `ص ل و B004` ↔ `ع ل م B006` | score_hint=14 | discovery_hint=12 | themes=animal, habitat_ecology, wildlife | keywords=hunting, predation | q2=—
- `ص ل و B006` ↔ `س ف ع B004` | score_hint=14 | discovery_hint=12 | themes=animal, conflict, motion | keywords=animal, motion | q2=—
- `ك و ن B004` ↔ `س ف ع B001` | score_hint=14 | discovery_hint=12 | themes=control_restraint, force_power, honor_shame | keywords=domination, power | q2=—
- `ك و ن B004` ↔ `ن ص ي B001` | score_hint=14 | discovery_hint=12 | themes=control_restraint, force_power, honor_shame | keywords=domination, humiliation | q2=—

## Per-root candidate activations

### ر ء ي

- `ر ء ي B001` — رؤية العين والبصيرة
  - activated_by_or_with: ء م ر, خ ط ء, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: cognition, knowledge_learning, memory_attention, perception
  - keywords: attention, awareness, cognition, epistemology, knowledge, perception, sensation
- `ر ء ي B002` — رأي القلب والتفكر
  - activated_by_or_with: ء م ر, خ ط ء, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: cognition, communication, justice_judgment, knowledge_learning, proof_uncertainty, reasoning_decision
  - keywords: cognition, decision, judgment, knowledge, planning, strategy
- `ر ء ي B003` — الرؤيا في المنام
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: belief_revelation, cognition, pattern_marking, physiology
  - keywords: psychology, symbol
- `ر ء ي B004` — تراء وتواجه
  - activated_by_or_with: ء م ر, س ف ع, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: conflict, household_community, perception, place_location, social_relations, space
  - keywords: conflict, encounter, gathering, relation, settlement, space, visibility
- `ر ء ي B005` — رياء الناس
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, س ف ع, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: deception_corruption, ethics_morality, honor_shame, intention_character, religion_worship, social_relations
  - keywords: deception, ethics, intention, morality, motivation, religion, sociality, society
- `ر ء ي B006` — مرأى ومنظر ومرآة
  - activated_by_or_with: ء م ر, خ ط ء, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: body, cognition, identity_personhood, ornament_beauty, perception, proof_uncertainty, visual_appearance
  - keywords: appearance, beauty, body, identity, perception
- `ر ء ي B007` — ترية الحيض
  - activated_by_or_with: ء ل ه, ء م ر, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: body, gender, health_medicine, purity_cleansing, reproduction_birth, ritual
  - keywords: body, fertility, gender, medicine, purity, ritual
- `ر ء ي B008` — رئي من الجن
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ه د ي, و ق ي, و ل ي
  - themes: belief_revelation, culture_tradition, health_medicine, perception, social_relations
  - keywords: encounter
- `ر ء ي B009` — الرئة وما يصيبها
  - activated_by_or_with: ء م ر, س ف ع, ص ل و, ع ب د, ع ل م, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي
  - themes: anatomy, body, disease_injury, health_medicine, physiology
  - keywords: anatomy, body, illness, medicine, vitality
- `ر ء ي B010` — ظهور حمل الناقة أو الشاة
  - activated_by_or_with: ء م ر, خ ط ء, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: agriculture, animal, body, husbandry, perception, reproduction_birth
  - keywords: agriculture, animal, body, fertility, husbandry, reproduction, visibility
- `ر ء ي B011` — راية منصوبة
  - activated_by_or_with: ء ل ه, ء م ر, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: authority_governance, communication, household_community, identity_personhood, pattern_marking, perception, violence_warfare
  - keywords: authority, gathering, identity, symbol, visibility, warfare
- `ر ء ي B012` — إراءة وإظهار
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: belief_revelation, communication, knowledge_learning, ornament_beauty, perception, proof_uncertainty
  - keywords: communication, perception, revelation, teaching, visibility
- `ر ء ي B013` — أرأيتك للتنبيه والاستخبار
  - activated_by_or_with: ء ل ه, ء م ر, س ف ع, ص ل و, ع ل م, ك ذ ب, ك و ن, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: communication, language_speech, memory_attention, rhetoric_discourse
  - keywords: attention, communication, information, language, speech

### ن ه ي

- `ن ه ي B001` — الزجر والكف عن الفعل
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ه د ي, و ق ي, و ل ي
  - themes: control_restraint, ethics_morality, language_speech, law
  - keywords: control, discipline, ethics, law, norm, speech
- `ن ه ي B002` — الغاية التي ينتهي إليها الشيء
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ه د ي, و ق ي, و ل ي
  - themes: boundary, change_transition, communication, containment_access, intention_character, measurement, motion, orientation_direction, space
  - keywords: boundary, communication, completion, measure, motion, space
- `ن ه ي B003` — العقل الناهي عن القبيح
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ه د ي, و ق ي, و ل ي
  - themes: authority_governance, cognition, control_restraint, ethics_morality, justice_judgment
  - keywords: cognition, discipline, ethics, governance, judgment, morality, psychology
- `ن ه ي B004` — مستقر الماء عند منتهى السيل
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, و ق ي, و ل ي
  - themes: containment_access, geography_landscape, habitat_ecology, physiology, quantity_number, storage_vessels, terrain_desert, water_hydrology
  - keywords: geography, hydrology, landscape, nature, storage, water
- `ن ه ي B005` — الكفاية التي تنهي طلب غيرها
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ه د ي, و ق ي, و ل ي
  - themes: change_transition, desire_appetite, economy, emotion, measurement, reasoning_decision, support_dependence, value_quality
  - keywords: completion, desire, economy, evaluation, measure, need, value
- `ن ه ي B006` — التناهي في السمن
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ه د ي, و ق ي, و ل ي
  - themes: abundance_scarcity, animal, body, food_nutrition, growth_decay, livestock, measurement, quantity_number
  - keywords: abundance, animal, body, food, growth, livestock, measure, quantity
- `ن ه ي B007` — الانقطاع عن طلب الحاجة
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ه د ي, و ق ي, و ل ي
  - themes: agency_action, desire_appetite, labor_work, loss_absence, motion, reasoning_decision, support_dependence, travel
  - keywords: agency, desire, need, pursuit
- `ن ه ي B008` — ارتفاع النهار أو الماء إلى النهاء
  - activated_by_or_with: ء م ر, خ ط ء, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ه د ي, و ق ي, و ل ي
  - themes: change_transition, habitat_ecology, measurement, orientation_direction, time, water_hydrology
  - keywords: change, hydrology, measurement, nature, time, water
- `ن ه ي B009` — النَّهاء القوارير والزجاج
  - activated_by_or_with: ء م ر, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ه د ي, و ق ي, و ل ي
  - themes: communication, craft, material, storage_vessels, substance_texture, tools_equipment
  - keywords: container, craft, material, storage
- `ن ه ي B010` — مقدار العدد ومبلغه
  - activated_by_or_with: ء م ر, خ ط ء, ص ل و, ع ب د, ع ل م, ن ص ي, و ق ي, و ل ي
  - themes: boundary, finance_debt, measurement, quantity_number
  - keywords: accounting, boundary, measurement, quantity

### ع ب د

- `ع ب د B001` — الرق والملك
  - activated_by_or_with: ء م ر, خ ط ء, س ف ع, ص ل و, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: commerce_exchange, control_restraint, hierarchy_status, labor_work, law, wealth_property
  - keywords: captivity, coercion, commerce, hierarchy, labor, law, property, status
- `ع ب د B002` — الانتساب إلى الله عبدا
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ع ب د B003` — العبادة والطاعة الخاضعة
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, ص ل و, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: authority_governance, belief_revelation, religion_worship, ritual, trust_loyalty
  - keywords: allegiance, authority, devotion, faith, religion, ritual, submission, theology
- `ع ب د B004` — التعبيد والاستعباد
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: control_restraint, force_power, hierarchy_status, justice_judgment, labor_work, support_dependence, violence_warfare
  - keywords: coercion, control, dependency, hierarchy, labor, power, violence
- `ع ب د B005` — التذليل والتسوية
  - activated_by_or_with: ء م ر, ر ء ي, س ف ع, ص ل و, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: animal, architecture_construction, craft, husbandry, material, stability_endurance, transport, travel
  - keywords: animal, craft, domestication, material, transport, travel
- `ع ب د B006` — التكريم والتعظيم
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: authority_governance, hierarchy_status, honor_shame, hospitality_welfare, labor_work, religion_worship, ritual
  - keywords: authority, ceremony, hierarchy, honor, hospitality, status
- `ع ب د B007` — القوة والصلابة
  - activated_by_or_with: ء م ر, ر ء ي, س ف ع, ص ل و, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: animal, body, force_power, material, physiology, stability_endurance, textile_clothing
  - keywords: animal, body, endurance, force, material, textile, vitality
- `ع ب د B008` — الأنفة والغضب
  - activated_by_or_with: ء م ر, ر ء ي, س ف ع, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: desire_appetite, emotion, honor_shame, loss_absence
  - keywords: desire, emotion, honor, loss
- `ع ب د B009` — قلة اللبث وسرعة العدو
  - activated_by_or_with: ء م ر, خ ط ء, س ف ع, ص ل و, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: agency_action, motion, recreation_sport, speed, time, travel
  - keywords: motion, movement, performance, speed, time, travel, urgency
- `ع ب د B010` — التفرق في الوجوه
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: form_structure, geography_landscape, household_community, motion, navigation_route, provision_resource, quantity_number, space
  - keywords: geography, movement, route, space
- `ع ب د B011` — العطب والانقطاع
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: animal, capacity_ability, control_restraint, loss_absence, physiology, stability_endurance, suffering_hardship, travel
  - keywords: animal, endurance, loss, misfortune, travel
- `ع ب د B012` — صَلاءة الطيب
  - activated_by_or_with: ء ل ه, ء م ر, ر ء ي, س ف ع, ص ل و, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: craft, fire_heat, household_community, ornament_beauty, perception, ritual, storage_vessels, wealth_property
  - keywords: container, craft, fire, ritual

### ص ل و

- `ص ل و B001` — ملاقاة النار وحرها
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, و ق ي, و ل ي
  - themes: danger_harm, fire_heat, force_power, justice_judgment, material, suffering_hardship
  - keywords: fire, material, pain, suffering, trial
- `ص ل و B002` — الدعاء والثناء والرحمة
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: belief_revelation, communication, ethics_morality, language_speech, religion_worship, ritual, social_relations
  - keywords: blessing, communication, devotion, ethic, relation, ritual, speech
- `ص ل و B003` — العبادة المخصوصة
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: authority_governance, body, control_restraint, household_community, law, religion_worship, ritual
  - keywords: body, community, devotion, discipline, law, liturgy, obedience, religion, ritual, worship
- `ص ل و B004` — الشرك المنصوبة
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: animal, control_restraint, craft, danger_harm, habitat_ecology, reasoning_decision, tools_equipment, violence_warfare, wildlife
  - keywords: animal, craft, hunting, predation, strategy, tool
- `ص ل و B005` — الصَّلا من الظهر والجنب
  - activated_by_or_with: ء م ر, ر ء ي, س ف ع, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: anatomy, animal, body, orientation_direction, physiology, reproduction_birth
  - keywords: anatomy, animal, body, orientation, physiology, reproduction
- `ص ل و B006` — تلو السابق في السباق
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: animal, conflict, hierarchy_status, measurement, motion, recreation_sport, sequence_cycle, speed
  - keywords: animal, competition, measurement, motion, pursuit, rank, sequence, speed
- `ص ل و B007` — مواضع الصلاة ودور العبادة
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: architecture_construction, authority_governance, culture_tradition, household_community, identity_personhood, religion_worship, ritual, space
  - keywords: community, identity, institution, religion, ritual, space, worship
- `ص ل و B008` — الصَّلاية حجر الدق
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: agency_action, craft, earth_geology, food_nutrition, household_community, perception, plant_vegetation, tools_equipment
  - keywords: craft, domesticity, food, plant, tool
- `ص ل و B009` — الصِّليان نبت ترعاه الإبل
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ع ب د, ع ل م, ك ذ ب, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: animal, food_nutrition, habitat_ecology, livestock, pasture_forage, plant_vegetation, provision_resource, terrain_desert
  - keywords: animal, botany, desert, ecology, food, forage, livestock, pasture, plant, subsistence

### ك و ن

- `ك و ن B001` — وقوع الشيء وحضوره في زمان
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, ص ل و, ع ب د, ع ل م, ك ذ ب, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: cognition, grammar_expression, language_speech, sequence_cycle, stability_endurance, time
  - keywords: ontology, time
- `ك و ن B002` — المكان والمكانة من الكون
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: capacity_ability, hierarchy_status, place_location, space
  - keywords: hierarchy, location, place, settlement, space, status
- `ك و ن B003` — الكفالة والقيام على فلان
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: agency_action, hospitality_welfare, obligation_contract, protection_security, social_relations, support_dependence, trust_loyalty
  - keywords: agency, care, obligation, patronage, protection, trust
- `ك و ن B004` — الخضوع بالاستكانة
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: authority_governance, control_restraint, danger_harm, ethics_morality, force_power, honor_shame, religion_worship, support_dependence
  - keywords: domination, humiliation, obedience, power, submission
- `ك و ن B005` — الشيخ المنسوب إلى كُنْتُ
  - activated_by_or_with: ء ل ه, ء م ر, ر ء ي, ص ل و, ع ب د, ع ل م, ك ذ ب, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: identity_personhood, language_speech, life_stage_aging, memory_attention, physiology, time, writing_text
  - keywords: identity, memory, speech, time
- `ك و ن B006` — حالة السوء بكينة
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, ص ل و, ع ب د, ع ل م, ك ذ ب, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: abundance_scarcity, danger_harm, ethics_morality, perception, suffering_hardship, value_quality
  - keywords: harm, misfortune, suffering

### ه د ي

- `ه د ي B001` — دلالة بلطف إلى الطريق والحق
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ه ي, و ق ي, و ل ي
  - themes: afterlife_eschatology, belief_revelation, ethics_morality, knowledge_learning, navigation_route, orientation_direction, proof_uncertainty, religion_worship
  - keywords: ethics, knowledge, navigation, orientation, religion, revelation, salvation, teaching, truth
- `ه د ي B002` — جهة الأمر وسيرته وقصده
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, و ل ي
  - themes: agency_action, culture_tradition, identity_personhood, intention_character, pattern_marking, reasoning_decision
  - keywords: behavior, identity, practice
- `ه د ي B003` — المتقدم الهادي وأوائل الشيء
  - activated_by_or_with: ء ل ه, ء م ر, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, و ق ي, و ل ي
  - themes: anatomy, animal, authority_governance, livestock, motion, sequence_cycle, weaponry
  - keywords: anatomy, animal, leadership, livestock, motion, sequence, weapon, weaponry
- `ه د ي B004` — بعثة لطف وهدية إلى ذي مودة
  - activated_by_or_with: ء م ر, ر ء ي, س ف ع, ص ل و, ع ب د, ك و ن, ن ص ي, ن ه ي, و ق ي, و ل ي
  - themes: commerce_exchange, emotion, hospitality_welfare, kinship, social_relations, wealth_property
  - keywords: commerce, emotion, exchange, hospitality, kinship, property, sociality
- `ه د ي B005` — الهدي المهدى إلى الحرم
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, و ق ي, و ل ي
  - themes: economy, livestock, pilgrimage_sacrifice, religion_worship, ritual, travel
  - keywords: economy, livestock, religion, ritual, sacrifice, sanctuary, worship
- `ه د ي B006` — العروس المهدية إلى زوجها
  - activated_by_or_with: ء ل ه, ء م ر, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ن ص ي, ن ه ي, و ق ي, و ل ي
  - themes: change_transition, family, gender, household_community, kinship, marriage_genealogy, motion, ritual
  - keywords: ceremony, domesticity, family, gender, kinship, transfer, transition
- `ه د ي B007` — هدي الحرمة والأسير
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, و ق ي, و ل ي
  - themes: authority_governance, control_restraint, law, obligation_contract, protection_security, religion_worship, violence_warfare
  - keywords: authority, captivity, law, protection, sanctuary, security, warfare
- `ه د ي B008` — مشي التهادي مع الاعتماد والتمايل
  - activated_by_or_with: ء م ر, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, و ق ي, و ل ي
  - themes: animal, body, disease_injury, gender, motion, support_dependence, transport
  - keywords: animal, body, gender, illness, locomotion, motion, transport
- `ه د ي B009` — الهداء البليد الضعيف
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, و ق ي, و ل ي
  - themes: body, capacity_ability, cognition, honor_shame, intention_character, value_quality
  - keywords: body, character, cognition, defect
- `ه د ي B010` — هدي السكون وحسن الهيئة
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, و ق ي, و ل ي
  - themes: body, control_restraint, emotion, ethics_morality, intention_character, motion, ornament_beauty, visual_appearance
  - keywords: appearance, body, discipline, emotion, ethics, motion, movement
- `ه د ي B011` — إهداء الشعر ومهاداته
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, و ق ي, و ل ي
  - themes: agency_action, commerce_exchange, communication, conflict, honor_shame, support_dependence, writing_text
  - keywords: communication, conflict, exchange, patronage, performance

### ء م ر

- `ء م ر B001` — الشأن والحال
  - activated_by_or_with: ء ل ه, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: cognition, emotion, naming_classification, rhetoric_discourse, social_relations, value_quality
  - keywords: classification, ontology, relation
- `ء م ر B002` — الطلب والإلزام
  - activated_by_or_with: ء ل ه, خ ط ء, ر ء ي, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: authority_governance, ethics_morality, language_speech, law, obligation_contract, ritual
  - keywords: authority, duty, ethic, governance, law, norm, obedience, ritual, speech
- `ء م ر B003` — الولاية وصاحب السلطان
  - activated_by_or_with: ء ل ه, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: authority_governance, force_power, hierarchy_status, law, politics_order
  - keywords: governance, hierarchy, leadership, power, rule
- `ء م ر B004` — النماء والبركة
  - activated_by_or_with: ء ل ه, خ ط ء, ر ء ي, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: abundance_scarcity, belief_revelation, economy, kinship, marriage_genealogy, physiology, reproduction_birth
  - keywords: abundance, blessing, economy, fertility, kinship, vitality
- `ء م ر B005` — العلامة والموعد
  - activated_by_or_with: ء ل ه, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ه ي, ه د ي, و ل ي
  - themes: calendar_season, communication, navigation_route, obligation_contract, orientation_direction, pattern_marking, time
  - keywords: navigation, orientation, promise, route, semiotics, time
- `ء م ر B006` — الأمر العظيم المنكر
  - activated_by_or_with: خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: danger_harm, emotion, ethics_morality, justice_judgment, measurement, suffering_hardship, value_quality
  - keywords: judgment, morality
- `ء م ر B007` — المشاورة وتدبير الرأي
  - activated_by_or_with: ء ل ه, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: agency_action, authority_governance, cognition, communication, reasoning_decision
  - keywords: agency, decision, governance, planning, psychology
- `ء م ر B008` — ضعيف الرأي التابع
  - activated_by_or_with: ء ل ه, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: authority_governance, cognition, force_power, intention_character, justice_judgment, knowledge_learning, reasoning_decision, social_relations, support_dependence
  - keywords: character, dependency, judgment, obedience, psychology
- `ء م ر B009` — ولد الضأن الصغير
  - activated_by_or_with: ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: animal, husbandry, kinship, life_stage_aging, livestock
  - keywords: animal, domestication, kinship, livestock
- `ء م ر B010` — الإبداع الإلهي
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ء م ر B011` — تسليح القناة بسنان
  - activated_by_or_with: ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: craft, tools_equipment, violence_warfare, weaponry
  - keywords: craft, tool, violence, warfare, weapon, weaponry

### و ق ي

- `و ق ي B001` — دفع الضرر بوقاية
  - activated_by_or_with: ء م ر, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: architecture_construction, boundary, danger_harm, protection_security
  - keywords: boundary, protection, security
- `و ق ي B002` — جعل النفس في وقاية
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: afterlife_eschatology, control_restraint, ethics_morality, justice_judgment, purity_cleansing, religion_worship
  - keywords: accountability, devotion, discipline, ethics, purity, religion, salvation
- `و ق ي B003` — توقي الدابة من وجع الحافر
  - activated_by_or_with: ء م ر, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: anatomy, animal, health_medicine, motion, protection_security, suffering_hardship, terrain_desert, tools_equipment, transport
  - keywords: anatomy, animal, caution, equipment, locomotion, pain, riding, veterinary
- `و ق ي B004` — الأوقية وزن معلوم
  - activated_by_or_with: ء م ر, خ ط ء, ص ل و, ع ب د, ع ل م, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: commerce_exchange, economy, finance_debt, measurement, quantity_number, value_quality
  - keywords: accounting, economy, measurement, quantity
- `و ق ي B005` — الواقي اسم للصرد
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: animal, habitat_ecology, language_speech, naming_classification, wildlife
  - keywords: animal, ecology, language, nature, nomenclature, taxonomy, wildlife, zoology

### ك ذ ب

- `ك ذ ب B001` — خلاف الصدق
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك و ن, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: communication, deception_corruption, ethics_morality, proof_uncertainty, rhetoric_discourse, testimony_witness, trust_loyalty
  - keywords: communication, deception, ethics, testimony, trust, truth
- `ك ذ ب B002` — نسبة الشيء أو صاحبه إلى الكذب
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك و ن, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: communication, conflict, justice_judgment, knowledge_learning, proof_uncertainty, rhetoric_discourse, testimony_witness, trust_loyalty
  - keywords: communication, epistemology, judgment, testimony, trust
- `ك ذ ب B003` — كذب عليك بمعنى الزم وعليك به
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: agency_action, authority_governance, control_restraint, intention_character, motion, obligation_contract, reasoning_decision, religion_worship
  - keywords: discipline, duty, motivation, obligation, practice, pursuit, religion, resolve
- `ك ذ ب B004` — صدق الحملة أو كذبها
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: agency_action, honor_shame, intention_character, justice_judgment, motion, reasoning_decision, violence_warfare
  - keywords: combat, honor, motion, movement, performance, resolve, trial, violence, warfare
- `ك ذ ب B005` — ما كذب أن فعل أي ما لبث
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: agency_action, change_transition, communication, sequence_cycle, speed, stability_endurance, time
  - keywords: action, completion, continuity, sequence, speed, time, transition, urgency
- `ك ذ ب B006` — كذب لبن الناقة إذا ذهب ولم يدم
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: abundance_scarcity, animal, change_transition, cognition, food_nutrition, livestock, provision_resource, reproduction_birth
  - keywords: animal, change, fertility, livestock, resource, scarcity, subsistence
- `ك ذ ب B007` — كذب الوحشي إذا جرى ثم وقف
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: agency_action, animal, habitat_ecology, memory_attention, motion, navigation_route, perception, protection_security
  - keywords: animal, attention, behavior, caution, motion, perception, predation, pursuit, tracking
- `ك ذ ب B008` — النفس الكذوب
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, ص ل و, ع ب د, ع ل م, ك و ن, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: cognition, deception_corruption, desire_appetite, ethics_morality, identity_personhood, intention_character, trust_loyalty
  - keywords: character, cognition, deception, desire, identity, intention, morality, psychology, trust
- `ك ذ ب B009` — الكذابة ثوب يكذب بحاله
  - activated_by_or_with: ء م ر, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: craft, deception_corruption, material, ornament_beauty, perception, textile_clothing, visual_appearance
  - keywords: adornment, appearance, clothing, coloration, craft, material, ornament, perception, textile

### و ل ي

- `و ل ي B001` — قرب ودنو بلا فاصل
  - activated_by_or_with: ء م ر, ر ء ي, س ف ع, ص ل و, ع ب د, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي
  - themes: boundary, place_location, social_relations, space
  - keywords: boundary, contact, location, relation, space
- `و ل ي B002` — تتابع شيء بعد شيء
  - activated_by_or_with: ء م ر, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي
  - themes: politics_order, sequence_cycle, stability_endurance, time
  - keywords: continuity, sequence, time
- `و ل ي B003` — تولي الأمر والقيام عليه
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي
  - themes: authority_governance, force_power, hospitality_welfare, law, obligation_contract
  - keywords: care, governance, institution, law, power, rule
- `و ل ي B004` — محبة ونصرة وموالاة
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي
  - themes: belief_revelation, conflict, emotion, household_community, religion_worship, support_dependence, trust_loyalty
  - keywords: allegiance, community, conflict, devotion, emotion, faith
- `و ل ي B005` — ولاء قرابة وعتق وجوار
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي
  - themes: control_restraint, family, hierarchy_status, household_community, law, place_location, support_dependence, wealth_property
  - keywords: community, family, law, patronage, status
- `و ل ي B006` — تولية الوجه والإقبال
  - activated_by_or_with: ء ل ه, ء م ر, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي
  - themes: authority_governance, memory_attention, motion, obligation_contract, orientation_direction, perception, social_relations
  - keywords: attention, motion, movement, obedience, orientation, perception, relation
- `و ل ي B007` — الإدبار والإعراض
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي
  - themes: authority_governance, communication, control_restraint, loss_absence, measurement, memory_attention, motion, social_relations
  - keywords: attention, movement, obedience
- `و ل ي B008` — الأولوية والاستحقاق
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي
  - themes: ethics_morality, hierarchy_status, justice_judgment, law, provision_resource, value_quality
  - keywords: hierarchy, justice, merit, norm, rank, value
- `و ل ي B009` — أولى لك تهديد ووعيد
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `و ل ي B010` — مطر يلي الوسمي
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ن ص ي, ن ه ي
  - themes: agriculture, calendar_season, geography_landscape, reproduction_birth, water_hydrology, weather_climate
  - keywords: agriculture, climate, fertility, water, weather
- `و ل ي B011` — ولية تحت الرحل
  - activated_by_or_with: ء م ر, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ن ص ي, ن ه ي, ه د ي, و ق ي
  - themes: animal, textile_clothing, tools_equipment, transport, travel
  - keywords: animal, equipment, riding, textile, transport, travel
- `و ل ي B012` — استيلاء وبلوغ غاية
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي
  - themes: change_transition, conflict, control_restraint, force_power, motion, value_quality, wealth_property
  - keywords: competition, completion, control, movement, ownership, power
- `و ل ي B013` — إيلاء وإسناد معروف أو شر
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي
  - themes: agency_action, commerce_exchange, danger_harm, ethics_morality, hospitality_welfare, motion
  - keywords: agency, exchange, harm, morality, transfer
- `و ل ي B014` — تولية البيع
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي
  - themes: commerce_exchange, obligation_contract, value_quality, wealth_property
  - keywords: commerce, exchange, ownership, property, value
- `و ل ي B015` — موالاة صغار النعم عن كبارها
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي
  - themes: agriculture, animal, boundary, control_restraint, growth_decay, husbandry, knowledge_learning, life_stage_aging
  - keywords: agriculture, animal, discipline, growth, husbandry, maturation
- `و ل ي B016` — ولي الرطب وتولى إذا هاج
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي
  - themes: agriculture, growth_decay, life_stage_aging, plant_vegetation, substance_texture, visual_appearance
  - keywords: agriculture, botany, color, maturation

### ع ل م

- `ع ل م B001` — انكشاف الشيء للعارف
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ل ي
  - themes: cognition, communication, knowledge_learning, memory_attention, proof_uncertainty, reasoning_decision
  - keywords: awareness, communication, epistemology, information, memory, truth
- `ع ل م B002` — أثر يميز الشيء ويهدي إليه
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: communication, geography_landscape, identity_personhood, naming_classification, navigation_route, orientation_direction, ornament_beauty, pattern_marking
  - keywords: geography, identity, navigation, orientation, ornament, semiotics, symbol
- `ع ل م B003` — الخلق عالم يدل على صانعه
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ع ل م B004` — شق ظاهر في الشفة العليا
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: anatomy, body, disease_injury, form_structure, health_medicine, naming_classification, pattern_marking, value_quality
  - keywords: anatomy, body, classification, defect, veterinary
- `ع ل م B005` — ماء كثير مجتمع في عيلم
  - activated_by_or_with: ء م ر, خ ط ء, س ف ع, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, و ق ي, و ل ي
  - themes: abundance_scarcity, geography_landscape, habitat_ecology, measurement, provision_resource, water_hydrology
  - keywords: abundance, geography, hydrology, nature, resource, water
- `ع ل م B006` — طائر جارح يسمى العلام
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: animal, cognition, habitat_ecology, naming_classification, speed, wildlife
  - keywords: hunting, predation, speed, taxonomy, wildlife, zoology
- `ع ل م B007` — ذكر الضباع يسمى العيلام
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ك ذ ب, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: animal, gender, habitat_ecology, naming_classification, wildlife
  - keywords: ecology, gender, predation, taxonomy, wildlife, zoology

### ء ل ه

- `ء ل ه B001` — التعبد والمعبود
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: authority_governance, belief_revelation, pilgrimage_sacrifice, religion_worship, ritual
  - keywords: authority, liturgy, religion, sacrifice, submission, theology
- `ء ل ه B002` — اسم الله في القسم والنداء
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: grammar_expression, language_speech, naming_classification, obligation_contract, religion_worship
  - keywords: devotion, language, nomenclature, promise, speech

### س ف ع

- `س ف ع B001` — الأخذ بالناصية
  - activated_by_or_with: ء م ر, ر ء ي, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: anatomy, body, communication, control_restraint, force_power, honor_shame, violence_warfare
  - keywords: body, captivity, domination, power, violence
- `س ف ع B002` — السواد المشرب بحمرة
  - activated_by_or_with: ء م ر, ر ء ي, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: animal, body, earth_geology, emotion, place_location, substance_texture, visual_appearance
  - keywords: animal, appearance, body, color, emotion, place
- `س ف ع B003` — لفح النار والسموم
  - activated_by_or_with: خ ط ء, ر ء ي, ص ل و, ع ب د, ع ل م, ك ذ ب, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: anatomy, body, containment_access, disease_injury, fire_heat, visual_appearance, weather_climate
  - keywords: body, color, coloration, fire, weather
- `س ف ع B004` — اللطم والضرب
  - activated_by_or_with: ء م ر, ر ء ي, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: animal, body, conflict, force_power, motion, social_relations, violence_warfare
  - keywords: animal, body, combat, conflict, contact, force, motion, violence
- `س ف ع B005` — المطاردة والمسافعة
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: conflict, control_restraint, habitat_ecology, motion, navigation_route, travel
  - keywords: competition, conflict, motion, predation, pursuit, tracking, travel
- `س ف ع B006` — سفعة الشيطان
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `س ف ع B007` — لبس الثياب المصبوغة
  - activated_by_or_with: ر ء ي, ص ل و, ع ب د, ع ل م, ك ذ ب, ن ص ي, ه د ي, و ل ي
  - themes: culture_tradition, gender, ornament_beauty, textile_clothing, visual_appearance
  - keywords: adornment, appearance, clothing, color, gender, textile

### ن ص ي

- `ن ص ي B001` — الناصية والأخذ بها
  - activated_by_or_with: ء م ر, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: anatomy, body, control_restraint, force_power, honor_shame
  - keywords: anatomy, body, control, domination, force, hair, humiliation
- `ن ص ي B002` — تسريح الشعر وطوله
  - activated_by_or_with: ء ل ه, ء م ر, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: anatomy, body, hospitality_welfare, ornament_beauty, ritual, visual_appearance
  - keywords: adornment, appearance, beauty, body, care, hair, ritual
- `ن ص ي B003` — النَّصِيَّة والصفوة
  - activated_by_or_with: ء ل ه, ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: authority_governance, hierarchy_status, household_community, reasoning_decision, social_relations, value_quality
  - keywords: community, hierarchy, leadership, merit, society, status
- `ن ص ي B004` — نبات النَّصِي
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ن ه ي, و ق ي, و ل ي
  - themes: agriculture, geography_landscape, habitat_ecology, pasture_forage, plant_vegetation, provision_resource, reproduction_birth
  - keywords: agriculture, botany, ecology, fertility, forage, landscape, pasture
- `ن ص ي B005` — مفازة تناصي مفازة
  - activated_by_or_with: ء م ر, خ ط ء, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: boundary, geography_landscape, social_relations, space, stability_endurance, terrain_desert, travel
  - keywords: continuity, desert, geography, landscape, relation, space, travel
- `ن ص ي B006` — نَصْو البطن المزعج
  - activated_by_or_with: ء م ر, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: body, health_medicine, motion, perception, physiology, suffering_hardship
  - keywords: body, medicine, motion, pain, physiology, sensation

### خ ط ء

- `خ ط ء B001` — مجاوزة الصواب وعدم إصابته
  - activated_by_or_with: ء م ر, ر ء ي, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: agency_action, capacity_ability, cognition, ethics_morality, intention_character, justice_judgment, measurement, proof_uncertainty, value_quality
  - keywords: action, agency, cognition, evaluation, intention, judgment, morality
- `خ ط ء B002` — الخطيئة ذنب وإثم
  - activated_by_or_with: ء ل ه, ء م ر, ر ء ي, ص ل و, ع ب د, ك ذ ب, ك و ن, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: agency_action, ethics_morality, justice_judgment, law, religion_worship
  - keywords: accountability, agency, ethics, judgment, justice, law, morality, religion
- `خ ط ء B003` — أرض أخطأها المطر
  - activated_by_or_with: ء ل ه, ء م ر, ر ء ي, س ف ع, ص ل و, ع ب د, ع ل م, ك ذ ب, ك و ن, ن ص ي, ن ه ي, ه د ي, و ق ي, و ل ي
  - themes: abundance_scarcity, agriculture, belief_revelation, geography_landscape, habitat_ecology, water_hydrology, weather_climate
  - keywords: agriculture, climate, geography, landscape, nature, scarcity, water, weather

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
