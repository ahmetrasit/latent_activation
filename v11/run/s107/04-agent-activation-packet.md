# v11 Activation Packet — S107:1-None

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_1: أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ
- verse_2: فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ
- verse_3: وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- verse_4: فَوَيْلٌۭ لِّلْمُصَلِّينَ
- verse_5: ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ
- verse_6: ٱلَّذِينَ هُمْ يُرَآءُونَ
- verse_7: وَيَمْنَعُونَ ٱلْمَاعُونَ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ر ء ي → ك ذ ب → د ي ن → د ع ع → ي ت م → ح ض ض → ط ع م → س ك ن → ص ل و → س ه و → م ن ع → م ع ن

## Branch inventory summary

- ر ء ي: 13 branches (13 with Qnet bridge-theme nodes; 0 Furūq-only)
- ك ذ ب: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- د ي ن: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- د ع ع: 10 branches (10 with Qnet bridge-theme nodes; 0 Furūq-only)
- ي ت م: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- ح ض ض: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- ط ع م: 14 branches (13 with Qnet bridge-theme nodes; 1 Furūq-only)
- س ك ن: 10 branches (9 with Qnet bridge-theme nodes; 1 Furūq-only)
- ص ل و: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- س ه و: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- م ن ع: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- م ع ن: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)

## QAC-first root resolution audit

- ر ء ي | qac_keys=رءي | status=resolved | matches=root_000531
- ك ذ ب | qac_keys=كذب | status=resolved | matches=root_001290
- د ي ن | qac_keys=دين | status=resolved | matches=root_000504
- د ع ع | qac_keys=دعع | status=resolved | matches=root_000477
- ي ت م | qac_keys=يتم | status=resolved | matches=root_001692
- ح ض ض | qac_keys=حضض | status=resolved | matches=root_000334
- ط ع م | qac_keys=طعم | status=resolved | matches=root_000934
- س ك ن | qac_keys=سكن | status=resolved | matches=root_000726
- ص ل و | qac_keys=صلو | status=resolved | matches=root_000879
- س ه و | qac_keys=سهو | status=resolved | matches=root_003249
- م ن ع | qac_keys=منع | status=resolved | matches=root_001448
- م ع ن | qac_keys=معن | status=resolved | matches=root_004706

## Top candidate bridges

- `د ع ع B008` ↔ `ص ل و B009` | score_hint=33 | discovery_hint=20 | themes=animal, food_nutrition, habitat_ecology, livestock, pasture_forage, plant_vegetation | keywords=animal, botany, ecology, livestock, pasture | q2=—
- `ط ع م B009` ↔ `ص ل و B006` | score_hint=25 | discovery_hint=18 | themes=animal, motion, recreation_sport, speed | keywords=animal, motion, speed, sport | q2=—
- `د ع ع B009` ↔ `س ك ن B003` | score_hint=23 | discovery_hint=18 | themes=family, household_community, kinship | keywords=demography, family, household, kinship | q2=—
- `د ي ن B003` ↔ `ط ع م B004` | score_hint=15 | discovery_hint=18 | themes=economy, finance_debt, wealth_property | keywords=economy, property | q2=—
- `ط ع م B007` ↔ `ص ل و B005` | score_hint=24 | discovery_hint=16 | themes=anatomy, animal, body, physiology | keywords=anatomy, animal, body, physiology | q2=—
- `ط ع م B006` ↔ `س ك ن B007` | score_hint=15 | discovery_hint=16 | themes=animal, tools_equipment, weaponry | keywords=animal, tool | q2=—
- `ط ع م B009` ↔ `س ك ن B008` | score_hint=15 | discovery_hint=16 | themes=control_restraint, motion, transport | keywords=control, motion | q2=—
- `ر ء ي B007` ↔ `م ن ع B004` | score_hint=13 | discovery_hint=16 | themes=gender, purity_cleansing | keywords=gender, purity | q2=—
- `ك ذ ب B005` ↔ `ص ل و B006` | score_hint=13 | discovery_hint=16 | themes=sequence_cycle, speed | keywords=sequence, speed | q2=—
- `ر ء ي B009` ↔ `د ع ع B005` | score_hint=9 | discovery_hint=16 | themes=body, disease_injury | keywords=body | q2=—
- `ك ذ ب B006` ↔ `ص ل و B009` | score_hint=20 | discovery_hint=15 | themes=animal, food_nutrition, livestock, provision_resource | keywords=animal, livestock, subsistence | q2=—
- `ر ء ي B006` ↔ `د ع ع B006` | score_hint=18 | discovery_hint=15 | themes=body, identity_personhood, visual_appearance | keywords=appearance, body, identity | q2=—
- `ر ء ي B010` ↔ `ص ل و B005` | score_hint=18 | discovery_hint=15 | themes=animal, body, reproduction_birth | keywords=animal, body, reproduction | q2=—
- `ط ع م B006` ↔ `ص ل و B004` | score_hint=24 | discovery_hint=14 | themes=animal, habitat_ecology, tools_equipment, wildlife | keywords=animal, hunting, predation, tool | q2=—
- `ك ذ ب B002` ↔ `د ي ن B007` | score_hint=20 | discovery_hint=14 | themes=justice_judgment, proof_uncertainty, testimony_witness, trust_loyalty | keywords=judgment, testimony, trust | q2=—
- `د ع ع B009` ↔ `ي ت م B005` | score_hint=20 | discovery_hint=14 | themes=household_community, kinship, social_relations, support_dependence | keywords=household, kinship, society | q2=—
- `ط ع م B002` ↔ `س ك ن B006` | score_hint=20 | discovery_hint=14 | themes=abundance_scarcity, hospitality_welfare, suffering_hardship, support_dependence | keywords=charity, dependence, poverty | q2=—
- `ر ء ي B010` ↔ `ط ع م B007` | score_hint=18 | discovery_hint=14 | themes=animal, body, husbandry | keywords=animal, body, husbandry | q2=—
- `د ي ن B003` ↔ `م ن ع B001` | score_hint=18 | discovery_hint=14 | themes=commerce_exchange, economy, wealth_property | keywords=economy, exchange, property | q2=—
- `د ي ن B004` ↔ `س ك ن B006` | score_hint=18 | discovery_hint=14 | themes=force_power, hierarchy_status, justice_judgment | keywords=hierarchy, oppression, power | q2=—
- `د ع ع B008` ↔ `ط ع م B007` | score_hint=18 | discovery_hint=14 | themes=animal, food_nutrition, livestock | keywords=animal, livestock, nutrition | q2=—
- `ر ء ي B009` ↔ `ط ع م B007` | score_hint=14 | discovery_hint=14 | themes=anatomy, body, physiology | keywords=anatomy, body | q2=—
- `ر ء ي B009` ↔ `ص ل و B005` | score_hint=14 | discovery_hint=14 | themes=anatomy, body, physiology | keywords=anatomy, body | q2=—
- `ر ء ي B010` ↔ `ط ع م B005` | score_hint=14 | discovery_hint=14 | themes=agriculture, perception, reproduction_birth | keywords=agriculture, fertility | q2=—
- `ط ع م B005` ↔ `م ن ع B007` | score_hint=14 | discovery_hint=14 | themes=agriculture, calendar_season, life_stage_aging | keywords=agriculture, season | q2=—
- `س ك ن B010` ↔ `ص ل و B009` | score_hint=14 | discovery_hint=14 | themes=food_nutrition, habitat_ecology, provision_resource | keywords=ecology, food | q2=—
- `د ي ن B003` ↔ `س ك ن B002` | score_hint=12 | discovery_hint=14 | themes=commerce_exchange, wealth_property | keywords=exchange, property | q2=—
- `د ع ع B007` ↔ `ط ع م B005` | score_hint=12 | discovery_hint=14 | themes=agriculture, plant_vegetation | keywords=agriculture, botany | q2=—
- `د ع ع B010` ↔ `ص ل و B009` | score_hint=12 | discovery_hint=14 | themes=food_nutrition, plant_vegetation | keywords=botany, food | q2=—
- `د ع ع B001` ↔ `م ن ع B002` | score_hint=9 | discovery_hint=14 | themes=boundary, control_restraint | keywords=boundary | q2=—
- `ي ت م B001` ↔ `س ك ن B007` | score_hint=7 | discovery_hint=14 | themes=mortality_death | keywords=death | q2=—
- `س ك ن B004` ↔ `ص ل و B001` | score_hint=7 | discovery_hint=14 | themes=fire_heat | keywords=fire | q2=—
- `د ي ن B001` ↔ `ص ل و B003` | score_hint=30 | discovery_hint=13 | themes=authority_governance, household_community, law, religion_worship, ritual | keywords=community, devotion, law, religion, ritual | q2=—
- `ي ت م B003` ↔ `ط ع م B008` | score_hint=22 | discovery_hint=13 | themes=agency_action, cognition, control_restraint, ethics_morality, value_quality | keywords=cognition, discipline, ethics | q2=—
- `ر ء ي B005` ↔ `ك ذ ب B008` | score_hint=18 | discovery_hint=13 | themes=deception_corruption, ethics_morality, intention_character | keywords=deception, intention, morality | q2=—
- `ك ذ ب B008` ↔ `ح ض ض B004` | score_hint=18 | discovery_hint=13 | themes=cognition, desire_appetite, intention_character | keywords=desire, intention, psychology | q2=—
- `د ع ع B003` ↔ `ط ع م B009` | score_hint=18 | discovery_hint=13 | themes=animal, authority_governance, control_restraint | keywords=animal, command, control | q2=—
- `د ع ع B008` ↔ `م ن ع B007` | score_hint=18 | discovery_hint=13 | themes=animal, calendar_season, habitat_ecology | keywords=animal, ecology, season | q2=—
- `د ع ع B009` ↔ `ي ت م B001` | score_hint=18 | discovery_hint=13 | themes=hospitality_welfare, kinship, life_stage_aging | keywords=care, childhood, kinship | q2=—
- `ح ض ض B002` ↔ `س ك ن B009` | score_hint=18 | discovery_hint=13 | themes=geography_landscape, place_location, stability_endurance | keywords=geography, placement, stability | q2=—
- `ر ء ي B013` ↔ `م ن ع B005` | score_hint=16 | discovery_hint=13 | themes=communication, language_speech | keywords=communication, language, speech | q2=—
- `ك ذ ب B007` ↔ `ص ل و B006` | score_hint=16 | discovery_hint=13 | themes=animal, motion | keywords=animal, motion, pursuit | q2=—
- `ك ذ ب B006` ↔ `د ع ع B008` | score_hint=14 | discovery_hint=13 | themes=animal, food_nutrition, livestock | keywords=animal, livestock | q2=—
- `ك ذ ب B006` ↔ `ط ع م B007` | score_hint=14 | discovery_hint=13 | themes=animal, food_nutrition, livestock | keywords=animal, livestock | q2=—
- `ط ع م B007` ↔ `ص ل و B009` | score_hint=14 | discovery_hint=13 | themes=animal, food_nutrition, livestock | keywords=animal, livestock | q2=—
- `ط ع م B013` ↔ `س ك ن B004` | score_hint=14 | discovery_hint=13 | themes=emotion, ritual, sexuality | keywords=intimacy, ritual | q2=—
- `س ك ن B002` ↔ `م ن ع B001` | score_hint=14 | discovery_hint=13 | themes=commerce_exchange, hospitality_welfare, wealth_property | keywords=exchange, property | q2=—
- `ر ء ي B007` ↔ `ص ل و B003` | score_hint=12 | discovery_hint=13 | themes=body, ritual | keywords=body, ritual | q2=—
- `ر ء ي B009` ↔ `د ع ع B006` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ر ء ي B009` ↔ `ط ع م B012` | score_hint=12 | discovery_hint=13 | themes=anatomy, physiology | keywords=anatomy, breath | q2=—
- `ر ء ي B010` ↔ `ك ذ ب B006` | score_hint=12 | discovery_hint=13 | themes=animal, reproduction_birth | keywords=animal, fertility | q2=—
- `ر ء ي B010` ↔ `س ك ن B007` | score_hint=12 | discovery_hint=13 | themes=animal, body | keywords=animal, body | q2=—
- `ر ء ي B010` ↔ `م ن ع B007` | score_hint=12 | discovery_hint=13 | themes=agriculture, animal | keywords=agriculture, animal | q2=—
- `ك ذ ب B006` ↔ `ط ع م B006` | score_hint=12 | discovery_hint=13 | themes=animal, provision_resource | keywords=animal, provision | q2=—
- `د ي ن B004` ↔ `ط ع م B011` | score_hint=12 | discovery_hint=13 | themes=control_restraint, force_power | keywords=control, power | q2=—
- `د ع ع B006` ↔ `ط ع م B007` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `د ع ع B006` ↔ `ص ل و B005` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `د ع ع B008` ↔ `ح ض ض B003` | score_hint=12 | discovery_hint=13 | themes=animal, plant_vegetation | keywords=animal, botany | q2=—
- `د ع ع B008` ↔ `ط ع م B005` | score_hint=12 | discovery_hint=13 | themes=calendar_season, plant_vegetation | keywords=botany, season | q2=—
- `د ع ع B008` ↔ `س ك ن B010` | score_hint=12 | discovery_hint=13 | themes=food_nutrition, habitat_ecology | keywords=ecology, nutrition | q2=—
- `ي ت م B005` ↔ `س ك ن B006` | score_hint=12 | discovery_hint=13 | themes=hierarchy_status, support_dependence | keywords=dependence, status | q2=—
- `ح ض ض B003` ↔ `ط ع م B010` | score_hint=12 | discovery_hint=13 | themes=health_medicine, plant_vegetation | keywords=botany, healing | q2=—
- `ح ض ض B003` ↔ `ص ل و B009` | score_hint=12 | discovery_hint=13 | themes=animal, plant_vegetation | keywords=animal, botany | q2=—
- `ط ع م B001` ↔ `س ك ن B010` | score_hint=12 | discovery_hint=13 | themes=food_nutrition, provision_resource | keywords=food, nutrition | q2=—
- `ط ع م B001` ↔ `ص ل و B009` | score_hint=12 | discovery_hint=13 | themes=food_nutrition, provision_resource | keywords=food, subsistence | q2=—
- `ط ع م B004` ↔ `س ك ن B002` | score_hint=12 | discovery_hint=13 | themes=hospitality_welfare, wealth_property | keywords=hospitality, property | q2=—
- `ط ع م B007` ↔ `س ك ن B007` | score_hint=12 | discovery_hint=13 | themes=animal, body | keywords=animal, body | q2=—
- `س ك ن B007` ↔ `ص ل و B005` | score_hint=12 | discovery_hint=13 | themes=animal, body | keywords=animal, body | q2=—
- `ك ذ ب B006` ↔ `ط ع م B004` | score_hint=10 | discovery_hint=13 | themes=provision_resource | keywords=resource, subsistence | q2=—
- `د ع ع B007` ↔ `ط ع م B010` | score_hint=10 | discovery_hint=13 | themes=agriculture, form_structure, plant_vegetation | keywords=botany | q2=—
- `ر ء ي B007` ↔ `ص ل و B005` | score_hint=8 | discovery_hint=13 | themes=body, reproduction_birth | keywords=body | q2=—
- `د ع ع B010` ↔ `ص ل و B008` | score_hint=8 | discovery_hint=13 | themes=food_nutrition, plant_vegetation | keywords=food | q2=—
- `د ي ن B001` ↔ `ص ل و B007` | score_hint=20 | discovery_hint=12 | themes=authority_governance, household_community, religion_worship, ritual | keywords=community, religion, ritual | q2=—
- `ح ض ض B001` ↔ `س ك ن B006` | score_hint=16 | discovery_hint=12 | themes=ethics_morality, hospitality_welfare | keywords=charity, ethics, morality | q2=—
- `ك ذ ب B001` ↔ `د ي ن B007` | score_hint=16 | discovery_hint=12 | themes=ethics_morality, proof_uncertainty, testimony_witness, trust_loyalty | keywords=testimony, trust | q2=—
- `ر ء ي B006` ↔ `ك ذ ب B009` | score_hint=14 | discovery_hint=12 | themes=ornament_beauty, perception, visual_appearance | keywords=appearance, perception | q2=—
- `ر ء ي B010` ↔ `د ع ع B003` | score_hint=14 | discovery_hint=12 | themes=animal, husbandry, perception | keywords=animal, herding | q2=—
- `ك ذ ب B003` ↔ `ص ل و B003` | score_hint=14 | discovery_hint=12 | themes=authority_governance, control_restraint, religion_worship | keywords=discipline, religion | q2=—
- `ك ذ ب B008` ↔ `ط ع م B008` | score_hint=14 | discovery_hint=12 | themes=cognition, ethics_morality, intention_character | keywords=character, cognition | q2=—
- `د ي ن B006` ↔ `ص ل و B003` | score_hint=14 | discovery_hint=12 | themes=authority_governance, household_community, law | keywords=community, law | q2=—

## Per-root candidate activations

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
  - activated_by_or_with: ك ذ ب
  - themes: deception_corruption, ethics_morality, intention_character
  - keywords: deception, intention, morality
- `ر ء ي B006` — مرأى ومنظر ومرآة
  - activated_by_or_with: د ع ع, ك ذ ب
  - themes: body, identity_personhood, ornament_beauty, perception, visual_appearance
  - keywords: appearance, body, identity, perception
- `ر ء ي B007` — ترية الحيض
  - activated_by_or_with: ص ل و, م ن ع
  - themes: body, gender, purity_cleansing, reproduction_birth, ritual
  - keywords: body, gender, purity, ritual
- `ر ء ي B008` — رئي من الجن
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ء ي B009` — الرئة وما يصيبها
  - activated_by_or_with: د ع ع, ص ل و, ط ع م
  - themes: anatomy, body, disease_injury, physiology
  - keywords: anatomy, body, breath
- `ر ء ي B010` — ظهور حمل الناقة أو الشاة
  - activated_by_or_with: د ع ع, س ك ن, ص ل و, ط ع م, ك ذ ب, م ن ع
  - themes: agriculture, animal, body, husbandry, perception, reproduction_birth
  - keywords: agriculture, animal, body, fertility, herding, husbandry, reproduction
- `ر ء ي B011` — راية منصوبة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ء ي B012` — إراءة وإظهار
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ء ي B013` — أرأيتك للتنبيه والاستخبار
  - activated_by_or_with: م ن ع
  - themes: communication, language_speech
  - keywords: communication, language, speech

### ك ذ ب

- `ك ذ ب B001` — خلاف الصدق
  - activated_by_or_with: د ي ن
  - themes: ethics_morality, proof_uncertainty, testimony_witness, trust_loyalty
  - keywords: testimony, trust
- `ك ذ ب B002` — نسبة الشيء أو صاحبه إلى الكذب
  - activated_by_or_with: د ي ن
  - themes: justice_judgment, proof_uncertainty, testimony_witness, trust_loyalty
  - keywords: judgment, testimony, trust
- `ك ذ ب B003` — كذب عليك بمعنى الزم وعليك به
  - activated_by_or_with: ص ل و
  - themes: authority_governance, control_restraint, religion_worship
  - keywords: discipline, religion
- `ك ذ ب B004` — صدق الحملة أو كذبها
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ك ذ ب B005` — ما كذب أن فعل أي ما لبث
  - activated_by_or_with: ص ل و
  - themes: sequence_cycle, speed
  - keywords: sequence, speed
- `ك ذ ب B006` — كذب لبن الناقة إذا ذهب ولم يدم
  - activated_by_or_with: د ع ع, ر ء ي, ص ل و, ط ع م
  - themes: animal, food_nutrition, livestock, provision_resource, reproduction_birth
  - keywords: animal, fertility, livestock, provision, resource, subsistence
- `ك ذ ب B007` — كذب الوحشي إذا جرى ثم وقف
  - activated_by_or_with: ص ل و
  - themes: animal, motion
  - keywords: animal, motion, pursuit
- `ك ذ ب B008` — النفس الكذوب
  - activated_by_or_with: ح ض ض, ر ء ي, ط ع م
  - themes: cognition, deception_corruption, desire_appetite, ethics_morality, intention_character
  - keywords: character, cognition, deception, desire, intention, morality, psychology
- `ك ذ ب B009` — الكذابة ثوب يكذب بحاله
  - activated_by_or_with: ر ء ي
  - themes: ornament_beauty, perception, visual_appearance
  - keywords: appearance, perception

### د ي ن

- `د ي ن B001` — الطاعة والانقياد
  - activated_by_or_with: ص ل و
  - themes: authority_governance, household_community, law, religion_worship, ritual
  - keywords: community, devotion, law, religion, ritual
- `د ي ن B002` — الحساب والجزاء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `د ي ن B003` — الدين المالي
  - activated_by_or_with: س ك ن, ط ع م, م ن ع
  - themes: commerce_exchange, economy, finance_debt, wealth_property
  - keywords: economy, exchange, property
- `د ي ن B004` — الإذلال والملك
  - activated_by_or_with: س ك ن, ط ع م
  - themes: control_restraint, force_power, hierarchy_status, justice_judgment
  - keywords: control, hierarchy, oppression, power
- `د ي ن B005` — العادة والشأن
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `د ي ن B006` — مدينة الطاعة
  - activated_by_or_with: ص ل و
  - themes: authority_governance, household_community, law
  - keywords: community, law
- `د ي ن B007` — التصديق والتفويض
  - activated_by_or_with: ك ذ ب
  - themes: ethics_morality, justice_judgment, proof_uncertainty, testimony_witness, trust_loyalty
  - keywords: judgment, testimony, trust

### د ع ع

- `د ع ع B001` — الدَّعّ دفع شديد
  - activated_by_or_with: م ن ع
  - themes: boundary, control_restraint
  - keywords: boundary
- `د ع ع B002` — الدعدعة تحريك لامتلاء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `د ع ع B003` — الدعدعة نداء وزجر
  - activated_by_or_with: ر ء ي, ط ع م
  - themes: animal, authority_governance, control_restraint, husbandry, perception
  - keywords: animal, command, control, herding
- `د ع ع B004` — دع دع للعاثر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `د ع ع B005` — الدعدعة عدو ملتف بطيء
  - activated_by_or_with: ر ء ي
  - themes: body, disease_injury
  - keywords: body
- `د ع ع B006` — الدعداع قصر الرجل
  - activated_by_or_with: ر ء ي, ص ل و, ط ع م
  - themes: anatomy, body, identity_personhood, visual_appearance
  - keywords: anatomy, appearance, body, identity
- `د ع ع B007` — الدعاع تفرق النخل
  - activated_by_or_with: ط ع م
  - themes: agriculture, form_structure, plant_vegetation
  - keywords: agriculture, botany
- `د ع ع B008` — الدعدع نبت مائي
  - activated_by_or_with: ح ض ض, س ك ن, ص ل و, ط ع م, ك ذ ب, م ن ع
  - themes: animal, calendar_season, food_nutrition, habitat_ecology, livestock, pasture_forage, plant_vegetation
  - keywords: animal, botany, ecology, livestock, nutrition, pasture, season
- `د ع ع B009` — الدعاع عيال صغار
  - activated_by_or_with: س ك ن, ي ت م
  - themes: family, hospitality_welfare, household_community, kinship, life_stage_aging, social_relations, support_dependence
  - keywords: care, childhood, demography, family, household, kinship, society
- `د ع ع B010` — الدعاع حبة برية
  - activated_by_or_with: ص ل و
  - themes: food_nutrition, plant_vegetation
  - keywords: botany, food

### ي ت م

- `ي ت م B001` — انقطاع الولد عن كافله
  - activated_by_or_with: د ع ع, س ك ن
  - themes: hospitality_welfare, kinship, life_stage_aging, mortality_death
  - keywords: care, childhood, death, kinship
- `ي ت م B002` — انفراد الشيء وانقطاع نظيره
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ي ت م B003` — غفلة وتقصير
  - activated_by_or_with: ط ع م
  - themes: agency_action, cognition, control_restraint, ethics_morality, value_quality
  - keywords: cognition, discipline, ethics
- `ي ت م B004` — إبطاء السير والبر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ي ت م B005` — انفراد المرأة عن الزوج
  - activated_by_or_with: د ع ع, س ك ن
  - themes: hierarchy_status, household_community, kinship, social_relations, support_dependence
  - keywords: dependence, household, kinship, society, status

### ح ض ض

- `ح ض ض B001` — الحَضّ على الشيء
  - activated_by_or_with: س ك ن
  - themes: ethics_morality, hospitality_welfare
  - keywords: charity, ethics, morality
- `ح ض ض B002` — الحَضيض قرار الأرض
  - activated_by_or_with: س ك ن
  - themes: geography_landscape, place_location, stability_endurance
  - keywords: geography, placement, stability
- `ح ض ض B003` — الحُضُض دواء مر
  - activated_by_or_with: د ع ع, ص ل و, ط ع م
  - themes: animal, health_medicine, plant_vegetation
  - keywords: animal, botany, healing
- `ح ض ض B004` — استزادة النفس
  - activated_by_or_with: ك ذ ب
  - themes: cognition, desire_appetite, intention_character
  - keywords: desire, intention, psychology

### ط ع م

- `ط ع م B001` — ذوق الشيء وتناوله
  - activated_by_or_with: س ك ن, ص ل و
  - themes: food_nutrition, provision_resource
  - keywords: food, nutrition, subsistence
- `ط ع م B002` — إطعام الغير وطلب الطعام
  - activated_by_or_with: س ك ن
  - themes: abundance_scarcity, hospitality_welfare, suffering_hardship, support_dependence
  - keywords: charity, dependence, poverty
- `ط ع م B003` — استطعام الكلام وفتح القراءة
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ط ع م B004` — رزق ومعاش وحسن حال
  - activated_by_or_with: د ي ن, س ك ن, ك ذ ب
  - themes: economy, finance_debt, hospitality_welfare, provision_resource, wealth_property
  - keywords: economy, hospitality, property, resource, subsistence
- `ط ع م B005` — إدراك الثمر وأخذ الطعم
  - activated_by_or_with: د ع ع, ر ء ي, م ن ع
  - themes: agriculture, calendar_season, life_stage_aging, perception, plant_vegetation, reproduction_birth
  - keywords: agriculture, botany, fertility, season
- `ط ع م B006` — آلة الصيد التي تطعم صاحبها
  - activated_by_or_with: س ك ن, ص ل و, ك ذ ب
  - themes: animal, habitat_ecology, provision_resource, tools_equipment, weaponry, wildlife
  - keywords: animal, hunting, predation, provision, tool
- `ط ع م B007` — سمن الحيوان وطعم الشحم
  - activated_by_or_with: د ع ع, ر ء ي, س ك ن, ص ل و, ك ذ ب
  - themes: anatomy, animal, body, food_nutrition, husbandry, livestock, physiology
  - keywords: anatomy, animal, body, husbandry, livestock, nutrition, physiology
- `ط ع م B008` — طعم العقل والقيمة
  - activated_by_or_with: ك ذ ب, ي ت م
  - themes: agency_action, cognition, control_restraint, ethics_morality, intention_character, value_quality
  - keywords: character, cognition, discipline, ethics
- `ط ع م B009` — مستطعم الفرس وطلب جريه
  - activated_by_or_with: د ع ع, س ك ن, ص ل و
  - themes: animal, authority_governance, control_restraint, motion, recreation_sport, speed, transport
  - keywords: animal, command, control, motion, speed, sport
- `ط ع م B010` — إطعام الغصن وقبول الوصل
  - activated_by_or_with: ح ض ض, د ع ع
  - themes: agriculture, form_structure, health_medicine, plant_vegetation
  - keywords: botany, healing
- `ط ع م B011` — القدرة على الشيء
  - activated_by_or_with: د ي ن
  - themes: control_restraint, force_power
  - keywords: control, power
- `ط ع م B012` — الأخذ بالمطعمة عند الخنق
  - activated_by_or_with: ر ء ي
  - themes: anatomy, physiology
  - keywords: anatomy, breath
- `ط ع م B013` — التطاعم بالفم
  - activated_by_or_with: س ك ن
  - themes: emotion, ritual, sexuality
  - keywords: intimacy, ritual
- `ط ع م B014` — تتابع الخلق
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### س ك ن

- `س ك ن B001` — ذهاب الحركة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `س ك ن B002` — استيطان المنزل
  - activated_by_or_with: د ي ن, ط ع م, م ن ع
  - themes: commerce_exchange, hospitality_welfare, wealth_property
  - keywords: exchange, hospitality, property
- `س ك ن B003` — أهل الدار
  - activated_by_or_with: د ع ع
  - themes: family, household_community, kinship
  - keywords: demography, family, household, kinship
- `س ك ن B004` — مأنس السكون
  - activated_by_or_with: ص ل و, ط ع م
  - themes: emotion, fire_heat, ritual, sexuality
  - keywords: fire, intimacy, ritual
- `س ك ن B005` — طمأنينة الوقار
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `س ك ن B006` — ذل المسكنة
  - activated_by_or_with: ح ض ض, د ي ن, ط ع م, ي ت م
  - themes: abundance_scarcity, ethics_morality, force_power, hierarchy_status, hospitality_welfare, justice_judgment, suffering_hardship, support_dependence
  - keywords: charity, dependence, ethics, hierarchy, morality, oppression, poverty, power, status
- `س ك ن B007` — إسكان الذبيحة بالسكين
  - activated_by_or_with: ر ء ي, ص ل و, ط ع م, ي ت م
  - themes: animal, body, mortality_death, tools_equipment, weaponry
  - keywords: animal, body, death, tool
- `س ك ن B008` — تسكين السفينة بالسكان
  - activated_by_or_with: ط ع م
  - themes: control_restraint, motion, transport
  - keywords: control, motion
- `س ك ن B009` — موضع الاستقرار
  - activated_by_or_with: ح ض ض
  - themes: geography_landscape, place_location, stability_endurance
  - keywords: geography, placement, stability
- `س ك ن B010` — قوت يثبت المقام
  - activated_by_or_with: د ع ع, ص ل و, ط ع م
  - themes: food_nutrition, habitat_ecology, provision_resource
  - keywords: ecology, food, nutrition

### ص ل و

- `ص ل و B001` — ملاقاة النار وحرها
  - activated_by_or_with: س ك ن
  - themes: fire_heat
  - keywords: fire
- `ص ل و B002` — الدعاء والثناء والرحمة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ص ل و B003` — العبادة المخصوصة
  - activated_by_or_with: د ي ن, ر ء ي, ك ذ ب
  - themes: authority_governance, body, control_restraint, household_community, law, religion_worship, ritual
  - keywords: body, community, devotion, discipline, law, religion, ritual
- `ص ل و B004` — الشرك المنصوبة
  - activated_by_or_with: ط ع م
  - themes: animal, habitat_ecology, tools_equipment, wildlife
  - keywords: animal, hunting, predation, tool
- `ص ل و B005` — الصَّلا من الظهر والجنب
  - activated_by_or_with: د ع ع, ر ء ي, س ك ن, ط ع م
  - themes: anatomy, animal, body, physiology, reproduction_birth
  - keywords: anatomy, animal, body, physiology, reproduction
- `ص ل و B006` — تلو السابق في السباق
  - activated_by_or_with: ط ع م, ك ذ ب
  - themes: animal, motion, recreation_sport, sequence_cycle, speed
  - keywords: animal, motion, pursuit, sequence, speed, sport
- `ص ل و B007` — مواضع الصلاة ودور العبادة
  - activated_by_or_with: د ي ن
  - themes: authority_governance, household_community, religion_worship, ritual
  - keywords: community, religion, ritual
- `ص ل و B008` — الصَّلاية حجر الدق
  - activated_by_or_with: د ع ع
  - themes: food_nutrition, plant_vegetation
  - keywords: food
- `ص ل و B009` — الصِّليان نبت ترعاه الإبل
  - activated_by_or_with: ح ض ض, د ع ع, س ك ن, ط ع م, ك ذ ب
  - themes: animal, food_nutrition, habitat_ecology, livestock, pasture_forage, plant_vegetation, provision_resource
  - keywords: animal, botany, ecology, food, livestock, pasture, subsistence

### س ه و

- `س ه و B001` — غفلة القلب وسهوه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `س ه و B002` — السهو سكون
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `س ه و B003` — المساهاة وحسن المخالقة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `س ه و B004` — السُّهْوَة موضع أو عارضة أمام البيت
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `س ه و B005` — السُّها كويكب خفيّ
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `س ه و B006` — حمل المرأة على حيض
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### م ن ع

- `م ن ع B001` — كف اليد عن العطاء
  - activated_by_or_with: د ي ن, س ك ن
  - themes: commerce_exchange, economy, hospitality_welfare, wealth_property
  - keywords: economy, exchange, property
- `م ن ع B002` — حاجز بين المرء وما يريد
  - activated_by_or_with: د ع ع
  - themes: boundary, control_restraint
  - keywords: boundary
- `م ن ع B003` — قوة تحمي فلا يخلص إليها
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `م ن ع B004` — تعفف يمتنع عن الفاحشة
  - activated_by_or_with: ر ء ي
  - themes: gender, purity_cleansing
  - keywords: gender, purity
- `م ن ع B005` — مناع صيحة أمر بالمنع
  - activated_by_or_with: ر ء ي
  - themes: communication, language_speech
  - keywords: communication, language, speech
- `م ن ع B006` — ممانعة في الشيء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `م ن ع B007` — فتاء يقاوم السنة
  - activated_by_or_with: د ع ع, ر ء ي, ط ع م
  - themes: agriculture, animal, calendar_season, habitat_ecology, life_stage_aging
  - keywords: agriculture, animal, ecology, season

### م ع ن

- `م ع ن B001` — جريان الماء وظهوره
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `م ع ن B002` — الإبعاد في العدو
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `م ع ن B003` — اليسر والقلة وخفة الخطر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `م ع ن B004` — إمعان الحق بين الإذهاب والإقرار
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `م ع ن B005` — الماعون منفعة قليلة مبذولة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `م ع ن B006` — المعان منزلا ومباءة
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
