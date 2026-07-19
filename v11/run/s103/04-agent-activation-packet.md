# v11 Activation Packet — S103:1-None

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_1: وَٱلْعَصْرِ
- verse_2: إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ
- verse_3: إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ وَتَوَاصَوْا۟ بِٱلْحَقِّ وَتَوَاصَوْا۟ بِٱلصَّبْرِ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ع ص ر → ء ن س → خ س ر → ء م ن → ع م ل → ص ل ح → و ص ي → ح ق ق → ص ب ر

## Branch inventory summary

- ع ص ر: 16 branches (16 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء ن س: 7 branches (6 with Qnet bridge-theme nodes; 1 Furūq-only)
- خ س ر: 5 branches (4 with Qnet bridge-theme nodes; 1 Furūq-only)
- ء م ن: 3 branches (3 with Qnet bridge-theme nodes; 0 Furūq-only)
- ع م ل: 12 branches (12 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص ل ح: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- و ص ي: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- ح ق ق: 14 branches (13 with Qnet bridge-theme nodes; 1 Furūq-only)
- ص ب ر: 18 branches (15 with Qnet bridge-theme nodes; 3 Furūq-only)

## QAC-first root resolution audit

- ع ص ر | qac_keys=عصر | status=resolved | matches=root_001019
- ء ن س | qac_keys=ءنس | status=resolved | matches=root_000059
- خ س ر | qac_keys=خسر | status=resolved | matches=root_000409
- ء م ن | qac_keys=ءمن | status=resolved | matches=root_000054
- ع م ل | qac_keys=عمل | status=resolved | matches=root_001046
- ص ل ح | qac_keys=صلح | status=resolved | matches=root_000876
- و ص ي | qac_keys=وصي | status=resolved | matches=root_001656
- ح ق ق | qac_keys=حقق | status=resolved | matches=root_000347
- ص ب ر | qac_keys=صبر | status=resolved | matches=root_000840

## Top candidate bridges

- `خ س ر B003` ↔ `ص ب ر B011` | score_hint=23 | discovery_hint=23 | themes=commerce_exchange, measurement, quantity_number | keywords=commerce, measurement, quantity | q2=S103-BR0014
- `ح ق ق B008` ↔ `ح ق ق B013` | score_hint=34 | discovery_hint=21 | themes=animal, husbandry, life_stage_aging, reproduction_birth, wealth_property | keywords=animal, fertility, husbandry, maturity, wealth | q2=S103-BR0013
- `ع ص ر B002` ↔ `ع ص ر B010` | score_hint=17 | discovery_hint=21 | themes=agriculture, harvest_cultivation | keywords=agriculture, harvest | q2=S103-BR0016
- `ح ق ق B011` ↔ `ص ب ر B004` | score_hint=19 | discovery_hint=19 | themes=space, storage_vessels, surface_shape | keywords=container, geometry, topology | q2=—
- `ع م ل B004` ↔ `ع م ل B006` | score_hint=21 | discovery_hint=18 | themes=labor_work, provision_resource | keywords=labor, livelihood | q2=S103-BR0003, S103-BR0036
- `ع ص ر B003` ↔ `ص ب ر B010` | score_hint=13 | discovery_hint=18 | themes=sky_astronomy, weather_climate | keywords=sky, weather | q2=—
- `ع ص ر B006` ↔ `ع ص ر B007` | score_hint=19 | discovery_hint=17 | themes=abundance_scarcity, economy, wealth_property | keywords=economy | q2=S103-BR0002, S103-BR0035
- `ع ص ر B002` ↔ `ع ص ر B007` | score_hint=17 | discovery_hint=17 | themes=agriculture, labor_work | keywords=agriculture | q2=S103-BR0007, S103-BR0030
- `ع ص ر B003` ↔ `ع ص ر B007` | score_hint=15 | discovery_hint=17 | themes=agriculture | keywords=agriculture | q2=S103-BR0007, S103-BR0010
- `ع م ل B008` ↔ `ص ل ح B001` | score_hint=11 | discovery_hint=17 | themes=value_quality | keywords=quality | q2=S103-BR0015
- `ح ق ق B001` ↔ `ح ق ق B005` | score_hint=24 | discovery_hint=16 | themes=knowledge_learning, law, proof_uncertainty, reasoning_decision | keywords=epistemology, law, logic | q2=S103-BR0009
- `ع ص ر B002` ↔ `ع ص ر B003` | score_hint=10 | discovery_hint=16 | themes=agriculture | keywords=agriculture | q2=S103-BR0007
- `ع ص ر B007` ↔ `ع م ل B004` | score_hint=22 | discovery_hint=16 | themes=commerce_exchange, economy, labor_work, provision_resource, wealth_property | keywords=economy, exchange, wealth | q2=—
- `و ص ي B004` ↔ `ح ق ق B008` | score_hint=13 | discovery_hint=16 | themes=animal, livestock | keywords=animal, livestock | q2=—
- `ع ص ر B016` ↔ `ء ن س B005` | score_hint=9 | discovery_hint=16 | themes=body, visual_appearance | keywords=body | q2=—
- `خ س ر B002` ↔ `ع م ل B003` | score_hint=7 | discovery_hint=16 | themes=finance_debt | keywords=finance | q2=—
- `ع ص ر B005` ↔ `ع ص ر B006` | score_hint=10 | discovery_hint=15 | themes=kinship | keywords=kinship | q2=S103-BR0002
- `ع م ل B004` ↔ `ع م ل B008` | score_hint=10 | discovery_hint=15 | themes=labor_work | keywords=labor | q2=S103-BR0003
- `ع م ل B006` ↔ `ع م ل B008` | score_hint=10 | discovery_hint=15 | themes=labor_work | keywords=labor | q2=S103-BR0003
- `و ص ي B002` ↔ `ح ق ق B003` | score_hint=26 | discovery_hint=15 | themes=agency_action, authority_governance, law, obligation_contract, wealth_property | keywords=agency, authority, inheritance, law | q2=—
- `ص ب ر B002` ↔ `ص ب ر B012` | score_hint=24 | discovery_hint=15 | themes=authority_governance, law, punishment_sanction, violence_warfare | keywords=authority, law, punishment, violence | q2=—
- `ء ن س B005` ↔ `ع م ل B010` | score_hint=22 | discovery_hint=15 | themes=anatomy, body, perception | keywords=anatomy, body, perception, vision | q2=—
- `ع ص ر B008` ↔ `ع ص ر B014` | score_hint=20 | discovery_hint=15 | themes=body, desire_appetite, health_medicine, suffering_hardship | keywords=body, medicine, thirst | q2=—
- `ع ص ر B001` ↔ `ء م ن B003` | score_hint=13 | discovery_hint=15 | themes=religion_worship, ritual | keywords=ritual, worship | q2=—
- `ء م ن B002` ↔ `ص ب ر B002` | score_hint=9 | discovery_hint=15 | themes=authority_governance, testimony_witness | keywords=testimony | q2=—
- `ع ص ر B016` ↔ `ح ق ق B010` | score_hint=7 | discovery_hint=15 | themes=textile_clothing | keywords=textile | q2=—
- `ء ن س B001` ↔ `ء ن س B003` | score_hint=12 | discovery_hint=14 | themes=household_community, social_relations | keywords=community | q2=S103-BR0018
- `ص ل ح B001` ↔ `ص ل ح B002` | score_hint=10 | discovery_hint=14 | themes=change_transition | keywords=restoration | q2=S103-BR0026
- `ح ق ق B001` ↔ `ح ق ق B003` | score_hint=10 | discovery_hint=14 | themes=law | keywords=law | q2=S103-BR0004
- `ح ق ق B001` ↔ `ح ق ق B007` | score_hint=10 | discovery_hint=14 | themes=ethics_morality | keywords=ethics | q2=S103-BR0021
- `ع م ل B008` ↔ `ح ق ق B012` | score_hint=24 | discovery_hint=14 | themes=animal, labor_work, motion, stability_endurance | keywords=animal, endurance, labor, mobility | q2=—
- `ع م ل B005` ↔ `ص ب ر B003` | score_hint=22 | discovery_hint=14 | themes=law, obligation_contract, social_relations | keywords=contract, law, obligation, society | q2=—
- `ع ص ر B006` ↔ `و ص ي B002` | score_hint=18 | discovery_hint=14 | themes=law, obligation_contract, wealth_property | keywords=inheritance, law, obligation | q2=—
- `ع ص ر B006` ↔ `ح ق ق B003` | score_hint=18 | discovery_hint=14 | themes=law, obligation_contract, wealth_property | keywords=inheritance, law, property | q2=—
- `ع ص ر B011` ↔ `ص ب ر B016` | score_hint=18 | discovery_hint=14 | themes=identity_personhood, kinship, marriage_genealogy | keywords=genealogy, identity, kinship | q2=—
- `ع م ل B010` ↔ `ح ق ق B012` | score_hint=18 | discovery_hint=14 | themes=animal, body, motion | keywords=animal, body, mobility | q2=—
- `ص ل ح B004` ↔ `ص ب ر B016` | score_hint=18 | discovery_hint=14 | themes=identity_personhood, marriage_genealogy, naming_classification | keywords=genealogy, identity, nomenclature | q2=—
- `و ص ي B002` ↔ `ص ب ر B003` | score_hint=18 | discovery_hint=14 | themes=law, obligation_contract, trust_loyalty | keywords=law, obligation, trust | q2=—
- `ع م ل B010` ↔ `ح ق ق B013` | score_hint=16 | discovery_hint=14 | themes=animal, physiology | keywords=animal, biology, physiology | q2=—
- `ع ص ر B007` ↔ `خ س ر B002` | score_hint=16 | discovery_hint=14 | themes=commerce_exchange, economy, value_quality, wealth_property | keywords=economy, exchange | q2=—
- `ع ص ر B012` ↔ `ص ب ر B003` | score_hint=14 | discovery_hint=14 | themes=social_relations, support_dependence, trust_loyalty | keywords=patronage, society | q2=—
- `ع ص ر B015` ↔ `ع م ل B010` | score_hint=14 | discovery_hint=14 | themes=body, perception, physiology | keywords=body, physiology | q2=—
- `خ س ر B002` ↔ `ع م ل B004` | score_hint=14 | discovery_hint=14 | themes=commerce_exchange, economy, wealth_property | keywords=economy, exchange | q2=—
- `ع ص ر B002` ↔ `و ص ي B004` | score_hint=12 | discovery_hint=14 | themes=agriculture, food_nutrition | keywords=agriculture, food | q2=—
- `ع ص ر B002` ↔ `ص ب ر B009` | score_hint=12 | discovery_hint=14 | themes=agriculture, food_nutrition | keywords=agriculture, food | q2=—
- `ع ص ر B007` ↔ `و ص ي B004` | score_hint=12 | discovery_hint=14 | themes=agriculture, provision_resource | keywords=agriculture, provision | q2=—
- `ع ص ر B010` ↔ `ص ب ر B009` | score_hint=12 | discovery_hint=14 | themes=agriculture, plant_vegetation | keywords=agriculture, botany | q2=—
- `و ص ي B004` ↔ `ص ب ر B009` | score_hint=12 | discovery_hint=14 | themes=agriculture, food_nutrition | keywords=agriculture, food | q2=—
- `و ص ي B004` ↔ `ص ب ر B011` | score_hint=12 | discovery_hint=14 | themes=food_nutrition, provision_resource | keywords=food, provision | q2=—
- `ع ص ر B009` ↔ `ح ق ق B013` | score_hint=10 | discovery_hint=14 | themes=life_stage_aging, physiology, reproduction_birth | keywords=fertility | q2=—
- `ع ص ر B006` ↔ `ص ب ر B003` | score_hint=18 | discovery_hint=13 | themes=kinship, law, obligation_contract | keywords=kinship, law, obligation | q2=—
- `ء م ن B001` ↔ `ح ق ق B007` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, obligation_contract, protection_security | keywords=ethics, obligation, protection | q2=—
- `ع م ل B007` ↔ `ح ق ق B012` | score_hint=18 | discovery_hint=13 | themes=labor_work, stability_endurance, suffering_hardship | keywords=endurance, labor, suffering | q2=—
- `ع م ل B009` ↔ `ح ق ق B009` | score_hint=18 | discovery_hint=13 | themes=anatomy, violence_warfare, weaponry | keywords=anatomy, warfare, weaponry | q2=—
- `ع م ل B010` ↔ `ح ق ق B014` | score_hint=18 | discovery_hint=13 | themes=anatomy, animal, motion | keywords=anatomy, animal, motion | q2=—
- `ع م ل B012` ↔ `ح ق ق B012` | score_hint=18 | discovery_hint=13 | themes=motion, stability_endurance, travel | keywords=endurance, mobility, travel | q2=—
- `ح ق ق B002` ↔ `ص ب ر B012` | score_hint=18 | discovery_hint=13 | themes=authority_governance, justice_judgment, law | keywords=accountability, authority, law | q2=—
- `ح ق ق B003` ↔ `ص ب ر B012` | score_hint=18 | discovery_hint=13 | themes=authority_governance, justice_judgment, law | keywords=authority, justice, law | q2=—
- `ح ق ق B005` ↔ `ص ب ر B012` | score_hint=18 | discovery_hint=13 | themes=authority_governance, justice_judgment, law | keywords=authority, justice, law | q2=—
- `ع ص ر B005` ↔ `ء ن س B006` | score_hint=14 | discovery_hint=13 | themes=kinship, social_relations, trust_loyalty | keywords=kinship, loyalty | q2=—
- `خ س ر B003` ↔ `ح ق ق B003` | score_hint=14 | discovery_hint=13 | themes=commerce_exchange, justice_judgment, obligation_contract | keywords=commerce, justice | q2=—
- `ع م ل B005` ↔ `ح ق ق B003` | score_hint=14 | discovery_hint=13 | themes=commerce_exchange, law, obligation_contract | keywords=commerce, law | q2=—
- `ع ص ر B005` ↔ `ح ق ق B007` | score_hint=12 | discovery_hint=13 | themes=kinship, protection_security | keywords=kinship, protection | q2=—
- `ع ص ر B006` ↔ `خ س ر B002` | score_hint=12 | discovery_hint=13 | themes=economy, wealth_property | keywords=economy, ownership | q2=—
- `ع ص ر B011` ↔ `ء ن س B006` | score_hint=12 | discovery_hint=13 | themes=identity_personhood, kinship | keywords=identity, kinship | q2=—
- `ع ص ر B011` ↔ `ص ل ح B004` | score_hint=12 | discovery_hint=13 | themes=identity_personhood, marriage_genealogy | keywords=genealogy, identity | q2=—
- `ع ص ر B014` ↔ `ح ق ق B012` | score_hint=12 | discovery_hint=13 | themes=body, suffering_hardship | keywords=body, suffering | q2=—
- `ع ص ر B016` ↔ `ح ق ق B007` | score_hint=12 | discovery_hint=13 | themes=protection_security, violence_warfare | keywords=protection, warfare | q2=—
- `ء ن س B006` ↔ `ص ب ر B016` | score_hint=12 | discovery_hint=13 | themes=identity_personhood, kinship | keywords=identity, kinship | q2=—
- `خ س ر B003` ↔ `ع م ل B005` | score_hint=12 | discovery_hint=13 | themes=commerce_exchange, obligation_contract | keywords=commerce, obligation | q2=—
- `ء ن س B004` ↔ `ء ن س B005` | score_hint=12 | discovery_hint=13 | themes=anatomy, posture_embodiment | keywords=anatomy, embodiment | q2=—
- `ع ص ر B003` ↔ `ص ب ر B007` | score_hint=10 | discovery_hint=13 | themes=weather_climate | keywords=climate, weather | q2=—
- `ع ص ر B004` ↔ `ص ب ر B010` | score_hint=10 | discovery_hint=13 | themes=weather_climate | keywords=atmosphere, weather | q2=—
- `ع ص ر B013` ↔ `ص ب ر B008` | score_hint=10 | discovery_hint=13 | themes=plant_vegetation | keywords=botany, plant | q2=—
- `ع ص ر B013` ↔ `ص ب ر B009` | score_hint=10 | discovery_hint=13 | themes=plant_vegetation | keywords=botany, plant | q2=—
- `ع ص ر B007` ↔ `ص ب ر B011` | score_hint=10 | discovery_hint=13 | themes=abundance_scarcity, commerce_exchange, provision_resource | keywords=provision | q2=—
- `ع ص ر B009` ↔ `ع م ل B010` | score_hint=8 | discovery_hint=13 | themes=body, physiology | keywords=body | q2=—
- `ع ص ر B009` ↔ `ح ق ق B008` | score_hint=8 | discovery_hint=13 | themes=life_stage_aging, reproduction_birth | keywords=fertility | q2=—
- `خ س ر B002` ↔ `ح ق ق B003` | score_hint=8 | discovery_hint=13 | themes=commerce_exchange, wealth_property | keywords=commerce | q2=—
- `ع ص ر B011` ↔ `ع ص ر B016` | score_hint=8 | discovery_hint=13 | themes=culture_tradition, identity_personhood | keywords=identity | q2=—

## Per-root candidate activations

### ع ص ر

- `ع ص ر B001` — دهر ووقت متعاقب
  - activated_by_or_with: ء م ن
  - themes: religion_worship, ritual
  - keywords: ritual, worship
- `ع ص ر B002` — ضغط حتى يتحلب
  - activated_by_or_with: ص ب ر, و ص ي
  - themes: agriculture, food_nutrition, harvest_cultivation, labor_work
  - keywords: agriculture, food, harvest
- `ع ص ر B003` — سحاب يمطر ومطر يعصر
  - activated_by_or_with: ص ب ر
  - themes: agriculture, sky_astronomy, weather_climate
  - keywords: agriculture, climate, sky, weather
- `ع ص ر B004` — إعصار وغبار مستدير
  - activated_by_or_with: ص ب ر
  - themes: weather_climate
  - keywords: atmosphere, weather
- `ع ص ر B005` — ملجأ ومنجاة واعتصام
  - activated_by_or_with: ء ن س, ح ق ق
  - themes: kinship, protection_security, social_relations, trust_loyalty
  - keywords: kinship, loyalty, protection
- `ع ص ر B006` — حبس ومنع واسترجاع
  - activated_by_or_with: ح ق ق, خ س ر, ص ب ر, و ص ي
  - themes: abundance_scarcity, economy, kinship, law, obligation_contract, wealth_property
  - keywords: economy, inheritance, kinship, law, obligation, ownership, property
- `ع ص ر B007` — عطاء وغلة مستخرجة
  - activated_by_or_with: خ س ر, ص ب ر, ع م ل, و ص ي
  - themes: abundance_scarcity, agriculture, commerce_exchange, economy, labor_work, provision_resource, value_quality, wealth_property
  - keywords: agriculture, economy, exchange, provision, wealth
- `ع ص ر B008` — شرب قليل لإساغة الغصة
  - activated_by_or_with: same-root only
  - themes: body, desire_appetite, health_medicine, suffering_hardship
  - keywords: body, medicine, thirst
- `ع ص ر B009` — بلوغ الجارية عصر شبابها
  - activated_by_or_with: ح ق ق, ع م ل
  - themes: body, life_stage_aging, physiology, reproduction_birth
  - keywords: body, fertility
- `ع ص ر B010` — زرع يتحرز في أكمامه
  - activated_by_or_with: ص ب ر
  - themes: agriculture, harvest_cultivation, plant_vegetation
  - keywords: agriculture, botany, harvest
- `ع ص ر B011` — أصل وحسب ونسب
  - activated_by_or_with: ء ن س, ص ب ر, ص ل ح
  - themes: culture_tradition, identity_personhood, kinship, marriage_genealogy
  - keywords: genealogy, identity, kinship
- `ع ص ر B012` — دنية في الموالاة
  - activated_by_or_with: ص ب ر
  - themes: social_relations, support_dependence, trust_loyalty
  - keywords: patronage, society
- `ع ص ر B013` — العصرة شجرة
  - activated_by_or_with: ص ب ر
  - themes: plant_vegetation
  - keywords: botany, plant
- `ع ص ر B014` — لسان معصور من العطش
  - activated_by_or_with: ح ق ق
  - themes: body, desire_appetite, health_medicine, suffering_hardship
  - keywords: body, medicine, suffering, thirst
- `ع ص ر B015` — العصار ريح البطن
  - activated_by_or_with: ع م ل
  - themes: body, perception, physiology
  - keywords: body, physiology
- `ع ص ر B016` — معاصر تلبس وتعصر
  - activated_by_or_with: ء ن س, ح ق ق
  - themes: body, culture_tradition, identity_personhood, protection_security, textile_clothing, violence_warfare, visual_appearance
  - keywords: body, identity, protection, textile, warfare

### ء ن س

- `ء ن س B001` — ظهور الإنسان المخالف للتوحش والجن
  - activated_by_or_with: same-root only
  - themes: household_community, social_relations
  - keywords: community
- `ء ن س B002` — إيناس الشيء برؤية أو إحساس أو سماع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ء ن س B003` — الأنس الذي يزيل الوحشة
  - activated_by_or_with: same-root only
  - themes: household_community, social_relations
  - keywords: community
- `ء ن س B004` — الجانب الإنسي المقبل على الإنسان
  - activated_by_or_with: same-root only
  - themes: anatomy, posture_embodiment
  - keywords: anatomy, embodiment
- `ء ن س B005` — إنسان العين وصورة الإنسان في السواد
  - activated_by_or_with: ع ص ر, ع م ل
  - themes: anatomy, body, perception, posture_embodiment, visual_appearance
  - keywords: anatomy, body, embodiment, perception, vision
- `ء ن س B006` — ابن الإنس للنفس والصفوة
  - activated_by_or_with: ص ب ر, ع ص ر
  - themes: identity_personhood, kinship, social_relations, trust_loyalty
  - keywords: identity, kinship, loyalty
- `ء ن س B007` — الاستئناس قبل دخول البيوت
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### خ س ر

- `خ س ر B001` — النقص العام
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ س ر B002` — خسارة التجارة
  - activated_by_or_with: ح ق ق, ع ص ر, ع م ل
  - themes: commerce_exchange, economy, finance_debt, value_quality, wealth_property
  - keywords: commerce, economy, exchange, finance, ownership
- `خ س ر B003` — إخسار الكيل والميزان
  - activated_by_or_with: ح ق ق, ص ب ر, ع م ل
  - themes: commerce_exchange, justice_judgment, measurement, obligation_contract, quantity_number
  - keywords: commerce, justice, measurement, obligation, quantity
- `خ س ر B004` — الضلال والهلاك
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `خ س ر B005` — الخنسرى والخيسرى والخناسر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ء م ن

- `ء م ن B001` — سكون القلب في أمن وثقة
  - activated_by_or_with: ح ق ق
  - themes: ethics_morality, obligation_contract, protection_security
  - keywords: ethics, obligation, protection
- `ء م ن B002` — تصديق يطمئن إليه القلب
  - activated_by_or_with: ص ب ر
  - themes: authority_governance, testimony_witness
  - keywords: testimony
- `ء م ن B003` — قول آمين طلبا للاستجابة
  - activated_by_or_with: ع ص ر
  - themes: religion_worship, ritual
  - keywords: ritual, worship

### ع م ل

- `ع م ل B001` — الفعل المقصود والعمل
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع م ل B002` — إعمال الشيء واستعماله
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع م ل B003` — ولاية العمل والقيام عليه
  - activated_by_or_with: خ س ر
  - themes: finance_debt
  - keywords: finance
- `ع م ل B004` — أجر العمل ورزق العامل
  - activated_by_or_with: خ س ر, ع ص ر
  - themes: commerce_exchange, economy, labor_work, provision_resource, wealth_property
  - keywords: economy, exchange, labor, livelihood, wealth
- `ع م ل B005` — المعاملة بين الناس
  - activated_by_or_with: ح ق ق, خ س ر, ص ب ر
  - themes: commerce_exchange, law, obligation_contract, social_relations
  - keywords: commerce, contract, law, obligation, society
- `ع م ل B006` — العملة العاملون بالأيدي
  - activated_by_or_with: same-root only
  - themes: labor_work, provision_resource
  - keywords: labor, livelihood
- `ع م ل B007` — التعمل بمعنى التعني
  - activated_by_or_with: ح ق ق
  - themes: labor_work, stability_endurance, suffering_hardship
  - keywords: endurance, labor, suffering
- `ع م ل B008` — المطبوع على العمل
  - activated_by_or_with: ح ق ق, ص ل ح
  - themes: animal, labor_work, motion, stability_endurance, value_quality
  - keywords: animal, endurance, labor, mobility, quality
- `ع م ل B009` — عامل الرمح
  - activated_by_or_with: ح ق ق
  - themes: anatomy, violence_warfare, weaponry
  - keywords: anatomy, warfare, weaponry
- `ع م ل B010` — الجارحة العاملة
  - activated_by_or_with: ء ن س, ح ق ق, ع ص ر
  - themes: anatomy, animal, body, motion, perception, physiology
  - keywords: anatomy, animal, biology, body, mobility, motion, perception, physiology, vision
- `ع م ل B011` — الطريق المعمل
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع م ل B012` — بنو العمل من المشاة
  - activated_by_or_with: ح ق ق
  - themes: motion, stability_endurance, travel
  - keywords: endurance, mobility, travel

### ص ل ح

- `ص ل ح B001` — الصلاح ضد الفساد والطلاح
  - activated_by_or_with: ع م ل
  - themes: change_transition, value_quality
  - keywords: quality, restoration
- `ص ل ح B002` — الصلح إزالة النفار بين الناس
  - activated_by_or_with: same-root only
  - themes: change_transition
  - keywords: restoration
- `ص ل ح B003` — الصلاح للشيء ملاءمته
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ص ل ح B004` — صالح وما قاربه علما لشخص
  - activated_by_or_with: ص ب ر, ع ص ر
  - themes: identity_personhood, marriage_genealogy, naming_classification
  - keywords: genealogy, identity, nomenclature
- `ص ل ح B005` — صلاح والصلح علمان لمواضع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### و ص ي

- `و ص ي B001` — وصل الشيء بالشيء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `و ص ي B002` — عهد موصول إلى غيره
  - activated_by_or_with: ح ق ق, ص ب ر, ع ص ر
  - themes: agency_action, authority_governance, law, obligation_contract, trust_loyalty, wealth_property
  - keywords: agency, authority, inheritance, law, obligation, trust
- `و ص ي B003` — تبادل الوصية بين القوم
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `و ص ي B004` — موافقة المرعى للسائمة
  - activated_by_or_with: ح ق ق, ص ب ر, ع ص ر
  - themes: agriculture, animal, food_nutrition, livestock, provision_resource
  - keywords: agriculture, animal, food, livestock, provision

### ح ق ق

- `ح ق ق B001` — ثبات مطابق للواقع ضد الباطل
  - activated_by_or_with: same-root only
  - themes: ethics_morality, knowledge_learning, law, proof_uncertainty, reasoning_decision
  - keywords: epistemology, ethics, law, logic
- `ح ق ق B002` — لزوم واجب واستحقاق ثابت
  - activated_by_or_with: ص ب ر
  - themes: authority_governance, justice_judgment, law
  - keywords: accountability, authority, law
- `ح ق ق B003` — حق مخصوص يملكه صاحبه
  - activated_by_or_with: خ س ر, ص ب ر, ع ص ر, ع م ل, و ص ي
  - themes: agency_action, authority_governance, commerce_exchange, justice_judgment, law, obligation_contract, wealth_property
  - keywords: agency, authority, commerce, inheritance, justice, law, property
- `ح ق ق B004` — محاقة يدعي كل طرف فيها الحق
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح ق ق B005` — إثبات الحق وإظهاره
  - activated_by_or_with: ص ب ر
  - themes: authority_governance, justice_judgment, knowledge_learning, law, proof_uncertainty, reasoning_decision
  - keywords: authority, epistemology, justice, law, logic
- `ح ق ق B006` — الحاقة التي تحقق الجزاء
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ح ق ق B007` — حقيقة يلزم حفظها
  - activated_by_or_with: ء م ن, ع ص ر
  - themes: ethics_morality, kinship, obligation_contract, protection_security, violence_warfare
  - keywords: ethics, kinship, obligation, protection, warfare
- `ح ق ق B008` — ناقة بلغت حق الحمل والانتفاع
  - activated_by_or_with: ع ص ر, و ص ي
  - themes: animal, husbandry, life_stage_aging, livestock, reproduction_birth, wealth_property
  - keywords: animal, fertility, husbandry, livestock, maturity, wealth
- `ح ق ق B009` — طعنة استقامت حتى نفذت
  - activated_by_or_with: ع م ل
  - themes: anatomy, violence_warfare, weaponry
  - keywords: anatomy, warfare, weaponry
- `ح ق ق B010` — إحكام رصين في نسج أو كلام
  - activated_by_or_with: ع ص ر
  - themes: textile_clothing
  - keywords: textile
- `ح ق ق B011` — حق يطابق موضعه كالمفصل والوعاء
  - activated_by_or_with: ص ب ر
  - themes: space, storage_vessels, surface_shape
  - keywords: container, geometry, topology
- `ح ق ق B012` — حقحقة تجهد الظهر في السير
  - activated_by_or_with: ع ص ر, ع م ل
  - themes: animal, body, labor_work, motion, stability_endurance, suffering_hardship, travel
  - keywords: animal, body, endurance, labor, mobility, suffering, travel
- `ح ق ق B013` — تمام حال الحيوان وقوته
  - activated_by_or_with: ع ص ر, ع م ل
  - themes: animal, husbandry, life_stage_aging, physiology, reproduction_birth, wealth_property
  - keywords: animal, biology, fertility, husbandry, maturity, physiology, wealth
- `ح ق ق B014` — أحق من الخيل يطابق خطوه أو يشتد بدنه
  - activated_by_or_with: ع م ل
  - themes: anatomy, animal, motion
  - keywords: anatomy, animal, motion

### ص ب ر

- `ص ب ر B001` — حبس النفس عن الجزع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ص ب ر B002` — حبس القهر للقتل أو اليمين
  - activated_by_or_with: ء م ن
  - themes: authority_governance, law, punishment_sanction, testimony_witness, violence_warfare
  - keywords: authority, law, punishment, testimony, violence
- `ص ب ر B003` — تحمل الكفالة والملازمة
  - activated_by_or_with: ع ص ر, ع م ل, و ص ي
  - themes: kinship, law, obligation_contract, social_relations, support_dependence, trust_loyalty
  - keywords: contract, kinship, law, obligation, patronage, society, trust
- `ص ب ر B004` — أعلى الشيء وجوانبه
  - activated_by_or_with: ح ق ق
  - themes: space, storage_vessels, surface_shape
  - keywords: container, geometry, topology
- `ص ب ر B005` — حجر غليظ وأرض حصباء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ص ب ر B006` — الوقوع في شدة لا منفذ منها
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ص ب ر B007` — شدة برد الشتاء
  - activated_by_or_with: ع ص ر
  - themes: weather_climate
  - keywords: climate, weather
- `ص ب ر B008` — الصبر المر وعصارته
  - activated_by_or_with: ع ص ر
  - themes: plant_vegetation
  - keywords: botany, plant
- `ص ب ر B009` — الصبار حمل الشجرة الحامض
  - activated_by_or_with: ع ص ر, و ص ي
  - themes: agriculture, food_nutrition, plant_vegetation
  - keywords: agriculture, botany, food, plant
- `ص ب ر B010` — سحاب أبيض متراكم
  - activated_by_or_with: ع ص ر
  - themes: sky_astronomy, weather_climate
  - keywords: atmosphere, sky, weather
- `ص ب ر B011` — رقاقة الخوان وكومة الطعام
  - activated_by_or_with: خ س ر, ع ص ر, و ص ي
  - themes: abundance_scarcity, commerce_exchange, food_nutrition, measurement, provision_resource, quantity_number
  - keywords: commerce, food, measurement, provision, quantity
- `ص ب ر B012` — الإقصاص والقود
  - activated_by_or_with: ح ق ق
  - themes: authority_governance, justice_judgment, law, punishment_sanction, violence_warfare
  - keywords: accountability, authority, justice, law, punishment, violence
- `ص ب ر B013` — الجرأة على النار
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ص ب ر B014` — انتظار الحكم
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ص ب ر B015` — الصوم المسمى صبرا
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ص ب ر B016` — بطن من غسان
  - activated_by_or_with: ء ن س, ص ل ح, ع ص ر
  - themes: identity_personhood, kinship, marriage_genealogy, naming_classification
  - keywords: genealogy, identity, kinship, nomenclature
- `ص ب ر B017` — الجبل ووسطه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ص ب ر B018` — سداد القارورة والبئر
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
