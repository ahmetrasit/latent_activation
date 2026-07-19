# v11 Activation Packet — S111:1-None

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_1: تَبَّتْ يَدَآ أَبِى لَهَبٍۢ وَتَبَّ
- verse_2: مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ
- verse_3: سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ
- verse_4: وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ
- verse_5: فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ت ب ب → ي د ي → ء ب و → ل ه ب → غ ن ي → م و ل → ك س ب → ص ل ي → ن و ر → م ر ء → ح م ل → ح ط ب → ج ي د → ح ب ل → م س د

## Branch inventory summary

- ت ب ب: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- ي د ي: 17 branches (13 with Qnet bridge-theme nodes; 4 Furūq-only)
- ء ب و: 3 branches (3 with Qnet bridge-theme nodes; 0 Furūq-only)
- ل ه ب: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- غ ن ي: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- م و ل: 2 branches (2 with Qnet bridge-theme nodes; 0 Furūq-only)
- ك س ب: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص ل ي: 10 branches (10 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن و ر: 11 branches (11 with Qnet bridge-theme nodes; 0 Furūq-only)
- م ر ء: 11 branches (11 with Qnet bridge-theme nodes; 0 Furūq-only)
- ح م ل: 10 branches (10 with Qnet bridge-theme nodes; 0 Furūq-only)
- ح ط ب: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- ج ي د: 1 branches (1 with Qnet bridge-theme nodes; 0 Furūq-only)
- ح ب ل: 15 branches (14 with Qnet bridge-theme nodes; 1 Furūq-only)
- م س د: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)

## QAC-first root resolution audit

- ت ب ب | qac_keys=تبب | status=resolved | matches=root_000172
- ي د ي | qac_keys=يدي | status=resolved | matches=root_001693
- ء ب و | qac_keys=ءبو | status=resolved | matches=root_000007
- ل ه ب | qac_keys=لهب | status=resolved | matches=root_001379
- غ ن ي | qac_keys=غني | status=resolved | matches=root_001110
- م و ل | qac_keys=مول | status=resolved | matches=root_001457
- ك س ب | qac_keys=كسب | status=resolved | matches=root_001296
- ص ل ي | qac_keys=صلي | status=resolved | matches=root_000880
- ن و ر | qac_keys=نور | status=resolved | matches=root_001564
- م ر ء | qac_keys=مرء | status=merged | matches=root_001409, root_001410
- ح م ل | qac_keys=حمل | status=resolved | matches=root_000357
- ح ط ب | qac_keys=حطب | status=resolved | matches=root_000335
- ج ي د | qac_keys=جيد | status=resolved | matches=root_000284
- ح ب ل | qac_keys=حبل | status=resolved | matches=root_000291
- م س د | qac_keys=مسد | status=resolved | matches=root_001422

## Top candidate bridges

- `ح م ل B002` ↔ `ح ب ل B007` | score_hint=25 | discovery_hint=21 | themes=agriculture, growth_decay, harvest_cultivation, plant_vegetation | keywords=agriculture, botany, growth, harvest | q2=—
- `ن و ر B009` ↔ `م س د B007` | score_hint=17 | discovery_hint=18 | themes=body, hygiene_sanitation, ornament_beauty, substance_texture | keywords=body, grooming | q2=—
- `ص ل ي B010` ↔ `ح ب ل B007` | score_hint=24 | discovery_hint=17 | themes=agriculture, food_nutrition, habitat_ecology, plant_vegetation | keywords=agriculture, botany, ecology, food | q2=—
- `ن و ر B004` ↔ `ح م ل B002` | score_hint=24 | discovery_hint=17 | themes=calendar_season, growth_decay, plant_vegetation, reproduction_birth | keywords=botany, fertility, growth, season | q2=—
- `ح م ل B002` ↔ `ح ب ل B006` | score_hint=24 | discovery_hint=17 | themes=growth_decay, kinship, physiology, reproduction_birth | keywords=biology, fertility, kinship, reproduction | q2=—
- `ل ه ب B007` ↔ `ح م ل B010` | score_hint=9 | discovery_hint=17 | themes=sky_astronomy, weather_climate | keywords=weather | q2=—
- `ي د ي B003` ↔ `ك س ب B002` | score_hint=32 | discovery_hint=16 | themes=commerce_exchange, hospitality_welfare, support_dependence, value_quality | keywords=benefit, charity, exchange, generosity, gift, patronage | q2=—
- `ص ل ي B010` ↔ `ح م ل B009` | score_hint=30 | discovery_hint=16 | themes=agriculture, animal, food_nutrition, husbandry, pasture_forage | keywords=agriculture, animal, food, pastoralism, pasture | q2=—
- `ج ي د B001` ↔ `م س د B002` | score_hint=32 | discovery_hint=15 | themes=anatomy, body, measurement, ornament_beauty, rhetoric_discourse, visual_appearance | keywords=anatomy, appearance, beauty, body, proportion | q2=—
- `ل ه ب B006` ↔ `ح ب ل B010` | score_hint=28 | discovery_hint=15 | themes=identity_personhood, kinship, marriage_genealogy, naming_classification | keywords=genealogy, identity, kinship, naming, tribe | q2=—
- `ل ه ب B008` ↔ `م س د B007` | score_hint=22 | discovery_hint=15 | themes=body, ornament_beauty, visual_appearance | keywords=aesthetics, appearance, body, ornament | q2=—
- `غ ن ي B002` ↔ `ك س ب B002` | score_hint=16 | discovery_hint=15 | themes=commerce_exchange, provision_resource, support_dependence, value_quality | keywords=exchange, provision | q2=—
- `ي د ي B004` ↔ `ك س ب B002` | score_hint=14 | discovery_hint=15 | themes=commerce_exchange, provision_resource, wealth_property | keywords=commerce, ownership | q2=—
- `ص ل ي B007` ↔ `ح ب ل B009` | score_hint=9 | discovery_hint=15 | themes=motion, recreation_sport | keywords=sport | q2=—
- `ل ه ب B006` ↔ `غ ن ي B004` | score_hint=7 | discovery_hint=15 | themes=memory_attention | keywords=memory | q2=—
- `م ر ء root_001409:B004` ↔ `م ر ء root_001410:B005` | score_hint=39 | discovery_hint=14 | themes=anatomy, body, food_nutrition, health_medicine, navigation_route, physiology | keywords=anatomy, body, digestion, ingestion, medicine, passage, physiology | q2=—
- `ن و ر B010` ↔ `ح ط ب B002` | score_hint=24 | discovery_hint=14 | themes=cognition, communication, proof_uncertainty, rhetoric_discourse | keywords=cognition, communication, rhetoric, uncertainty | q2=—
- `ل ه ب B008` ↔ `م س د B002` | score_hint=20 | discovery_hint=14 | themes=body, ornament_beauty, rhetoric_discourse, visual_appearance | keywords=aesthetics, appearance, body | q2=—
- `ل ه ب B008` ↔ `غ ن ي B005` | score_hint=18 | discovery_hint=14 | themes=hierarchy_status, identity_personhood, ornament_beauty | keywords=adornment, identity, ornament | q2=—
- `م ر ء root_001409:B001` ↔ `ح ب ل B010` | score_hint=18 | discovery_hint=14 | themes=identity_personhood, kinship, social_relations | keywords=identity, kinship, society | q2=—
- `م ر ء root_001409:B004` ↔ `ح ب ل B004` | score_hint=18 | discovery_hint=14 | themes=anatomy, health_medicine, physiology | keywords=anatomy, medicine, physiology | q2=—
- `م ر ء root_001410:B001` ↔ `ح ب ل B010` | score_hint=18 | discovery_hint=14 | themes=identity_personhood, kinship, social_relations | keywords=identity, kinship, society | q2=—
- `م ر ء root_001410:B005` ↔ `ح ب ل B004` | score_hint=18 | discovery_hint=14 | themes=anatomy, health_medicine, physiology | keywords=anatomy, medicine, physiology | q2=—
- `ح ط ب B004` ↔ `م س د B002` | score_hint=18 | discovery_hint=14 | themes=body, rhetoric_discourse, visual_appearance | keywords=appearance, body, metaphor | q2=—
- `ي د ي B004` ↔ `م و ل B001` | score_hint=16 | discovery_hint=14 | themes=provision_resource, wealth_property | keywords=ownership, property, resource | q2=—
- `ص ل ي B006` ↔ `ح م ل B002` | score_hint=16 | discovery_hint=14 | themes=kinship, reproduction_birth | keywords=birth, kinship, reproduction | q2=—
- `ي د ي B004` ↔ `ك س ب B001` | score_hint=14 | discovery_hint=14 | themes=commerce_exchange, provision_resource, wealth_property | keywords=commerce, ownership | q2=—
- `ل ه ب B002` ↔ `ح م ل B007` | score_hint=14 | discovery_hint=14 | themes=body, physiology, suffering_hardship | keywords=body, suffering | q2=—
- `م و ل B001` ↔ `ك س ب B002` | score_hint=14 | discovery_hint=14 | themes=provision_resource, support_dependence, wealth_property | keywords=ownership, patronage | q2=—
- `ي د ي B016` ↔ `ح ب ل B002` | score_hint=12 | discovery_hint=14 | themes=protection_security, trust_loyalty | keywords=alliance, protection | q2=—
- `ل ه ب B002` ↔ `م ر ء root_001409:B004` | score_hint=12 | discovery_hint=14 | themes=body, physiology | keywords=body, physiology | q2=—
- `ل ه ب B002` ↔ `م ر ء root_001410:B005` | score_hint=12 | discovery_hint=14 | themes=body, physiology | keywords=body, physiology | q2=—
- `ص ل ي B010` ↔ `ح م ل B002` | score_hint=12 | discovery_hint=14 | themes=agriculture, plant_vegetation | keywords=agriculture, botany | q2=—
- `ن و ر B004` ↔ `ح ب ل B007` | score_hint=12 | discovery_hint=14 | themes=growth_decay, plant_vegetation | keywords=botany, growth | q2=—
- `ح م ل B009` ↔ `ح ب ل B007` | score_hint=12 | discovery_hint=14 | themes=agriculture, food_nutrition | keywords=agriculture, food | q2=—
- `ت ب ب B001` ↔ `ص ل ي B003` | score_hint=11 | discovery_hint=14 | themes=justice_judgment, punishment_sanction, suffering_hardship | keywords=punishment | q2=—
- `م ر ء root_001409:B003` ↔ `م ر ء root_001410:B003` | score_hint=37 | discovery_hint=13 | themes=cooking_drink, desire_appetite, food_nutrition, health_medicine, physiology | keywords=appetite, comfort, cuisine, digestion, food, health, nutrition | q2=—
- `ك س ب B001` ↔ `ك س ب B002` | score_hint=27 | discovery_hint=13 | themes=commerce_exchange, provision_resource, value_quality, wealth_property | keywords=benefit, commerce, ownership, provision, wealth | q2=—
- `ي د ي B009` ↔ `ح م ل B003` | score_hint=22 | discovery_hint=13 | themes=agency_action, ethics_morality, justice_judgment, law, obligation_contract | keywords=accountability, agency, ethics | q2=—
- `ء ب و B001` ↔ `غ ن ي B006` | score_hint=20 | discovery_hint=13 | themes=authority_governance, family, kinship, protection_security | keywords=family, kinship, protection | q2=—
- `ل ه ب B008` ↔ `ج ي د B001` | score_hint=20 | discovery_hint=13 | themes=body, ornament_beauty, rhetoric_discourse, visual_appearance | keywords=appearance, body, description | q2=—
- `ح م ل B006` ↔ `م س د B005` | score_hint=20 | discovery_hint=13 | themes=material, motion, tools_equipment, transport | keywords=technology, tool, transport | q2=—
- `ح م ل B007` ↔ `م س د B003` | score_hint=20 | discovery_hint=13 | themes=labor_work, stability_endurance, suffering_hardship, travel | keywords=effort, endurance, travel | q2=—
- `ج ي د B001` ↔ `م س د B007` | score_hint=20 | discovery_hint=13 | themes=anatomy, body, ornament_beauty, visual_appearance | keywords=appearance, beauty, body | q2=—
- `ء ب و B002` ↔ `ح ط ب B002` | score_hint=18 | discovery_hint=13 | themes=communication, language_speech, rhetoric_discourse | keywords=communication, language, rhetoric | q2=—
- `ء ب و B002` ↔ `ح ب ل B014` | score_hint=18 | discovery_hint=13 | themes=grammar_expression, language_speech, rhetoric_discourse | keywords=grammar, language, speech | q2=—
- `غ ن ي B006` ↔ `م ر ء root_001409:B005` | score_hint=18 | discovery_hint=13 | themes=household_community, kinship, marriage_genealogy | keywords=household, kinship, marriage | q2=—
- `ك س ب B003` ↔ `ص ل ي B005` | score_hint=18 | discovery_hint=13 | themes=control_restraint, habitat_ecology, wildlife | keywords=capture, hunting, predation | q2=—
- `ن و ر B007` ↔ `ح ط ب B003` | score_hint=18 | discovery_hint=13 | themes=conflict, social_relations, violence_warfare | keywords=conflict, society, violence | q2=—
- `م ر ء root_001409:B002` ↔ `ح ط ب B003` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, honor_shame, social_relations | keywords=ethics, reputation, society | q2=—
- `م ر ء root_001410:B006` ↔ `ح ط ب B003` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, honor_shame, social_relations | keywords=ethics, reputation, society | q2=—
- `ل ه ب B005` ↔ `ح ب ل B003` | score_hint=16 | discovery_hint=13 | themes=geography_landscape, terrain_desert | keywords=geography, landscape, topography | q2=—
- `م ر ء root_001410:B006` ↔ `م س د B002` | score_hint=16 | discovery_hint=13 | themes=ornament_beauty, visual_appearance | keywords=aesthetics, appearance, beauty | q2=—
- `م ر ء root_001410:B006` ↔ `م س د B007` | score_hint=16 | discovery_hint=13 | themes=ornament_beauty, visual_appearance | keywords=aesthetics, appearance, beauty | q2=—
- `ص ل ي B004` ↔ `ن و ر B002` | score_hint=14 | discovery_hint=13 | themes=fire_heat | keywords=combustion, fire, heat | q2=—
- `ل ه ب B008` ↔ `م ر ء root_001410:B006` | score_hint=16 | discovery_hint=13 | themes=honor_shame, identity_personhood, ornament_beauty, visual_appearance | keywords=aesthetics, appearance | q2=—
- `ح م ل B005` ↔ `ح ب ل B010` | score_hint=16 | discovery_hint=13 | themes=identity_personhood, kinship, marriage_genealogy, social_relations | keywords=identity, kinship | q2=—
- `ل ه ب B006` ↔ `ح م ل B005` | score_hint=14 | discovery_hint=13 | themes=identity_personhood, kinship, marriage_genealogy | keywords=identity, kinship | q2=—
- `ل ه ب B008` ↔ `ح ط ب B004` | score_hint=14 | discovery_hint=13 | themes=body, rhetoric_discourse, visual_appearance | keywords=appearance, body | q2=—
- `ك س ب B004` ↔ `ص ل ي B009` | score_hint=14 | discovery_hint=13 | themes=agency_action, material, substance_texture | keywords=material, processing | q2=—
- `م ر ء root_001409:B001` ↔ `ح م ل B005` | score_hint=14 | discovery_hint=13 | themes=identity_personhood, kinship, social_relations | keywords=identity, kinship | q2=—
- `م ر ء root_001410:B001` ↔ `ح م ل B005` | score_hint=14 | discovery_hint=13 | themes=identity_personhood, kinship, social_relations | keywords=identity, kinship | q2=—
- `ت ب ب B003` ↔ `ك س ب B003` | score_hint=12 | discovery_hint=13 | themes=animal, body | keywords=animal, body | q2=—
- `ت ب ب B003` ↔ `ص ل ي B006` | score_hint=12 | discovery_hint=13 | themes=animal, body | keywords=animal, body | q2=—
- `ي د ي B007` ↔ `ح م ل B004` | score_hint=12 | discovery_hint=13 | themes=finance_debt, obligation_contract | keywords=contract, finance | q2=—
- `ل ه ب B006` ↔ `م ر ء root_001409:B001` | score_hint=12 | discovery_hint=13 | themes=identity_personhood, kinship | keywords=identity, kinship | q2=—
- `ل ه ب B006` ↔ `م ر ء root_001410:B001` | score_hint=12 | discovery_hint=13 | themes=identity_personhood, kinship | keywords=identity, kinship | q2=—
- `ل ه ب B008` ↔ `ن و ر B008` | score_hint=12 | discovery_hint=13 | themes=body, ornament_beauty | keywords=adornment, body | q2=—
- `غ ن ي B005` ↔ `م ر ء root_001409:B001` | score_hint=12 | discovery_hint=13 | themes=gender, identity_personhood | keywords=gender, identity | q2=—
- `غ ن ي B005` ↔ `م ر ء root_001410:B001` | score_hint=12 | discovery_hint=13 | themes=gender, identity_personhood | keywords=gender, identity | q2=—
- `ك س ب B003` ↔ `ص ل ي B006` | score_hint=12 | discovery_hint=13 | themes=animal, body | keywords=animal, body | q2=—
- `ص ل ي B006` ↔ `م ر ء root_001409:B004` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ص ل ي B006` ↔ `م ر ء root_001410:B005` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ص ل ي B006` ↔ `ح ب ل B006` | score_hint=12 | discovery_hint=13 | themes=kinship, reproduction_birth | keywords=kinship, reproduction | q2=—
- `ص ل ي B006` ↔ `م س د B002` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ن و ر B008` ↔ `م ر ء root_001409:B004` | score_hint=12 | discovery_hint=13 | themes=body, health_medicine | keywords=body, medicine | q2=—
- `ن و ر B008` ↔ `م ر ء root_001410:B005` | score_hint=12 | discovery_hint=13 | themes=body, health_medicine | keywords=body, medicine | q2=—
- `م ر ء root_001409:B004` ↔ `م س د B002` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `م ر ء root_001409:B005` ↔ `م س د B004` | score_hint=12 | discovery_hint=13 | themes=food_nutrition, household_community | keywords=food, household | q2=—
- `م ر ء root_001410:B003` ↔ `ح ط ب B004` | score_hint=12 | discovery_hint=13 | themes=body, health_medicine | keywords=body, health | q2=—

## Per-root candidate activations

### ت ب ب

- `ت ب ب B001` — الخسران والهلاك
  - activated_by_or_with: ص ل ي
  - themes: justice_judgment, punishment_sanction, suffering_hardship
  - keywords: punishment
- `ت ب ب B002` — الاستقامة والتهيؤ والاستمرار
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ت ب ب B003` — الضعف والكبر والدبر
  - activated_by_or_with: ص ل ي, ك س ب
  - themes: animal, body
  - keywords: animal, body
- `ت ب ب B004` — القطع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ي د ي

- `ي د ي B001` — اليَد الجارحة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ي د ي B002` — اليَد القوّة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ي د ي B003` — اليَد النعمة
  - activated_by_or_with: ك س ب
  - themes: commerce_exchange, hospitality_welfare, support_dependence, value_quality
  - keywords: benefit, charity, exchange, generosity, gift, patronage
- `ي د ي B004` — اليَد المالكة
  - activated_by_or_with: ك س ب, م و ل
  - themes: commerce_exchange, provision_resource, wealth_property
  - keywords: commerce, ownership, property, resource
- `ي د ي B005` — اليَد السلطان
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ي د ي B006` — اليَد المستسلمة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ي د ي B007` — اليَد المناولة
  - activated_by_or_with: ح م ل
  - themes: finance_debt, obligation_contract
  - keywords: contract, finance
- `ي د ي B008` — بين اليَدين
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ي د ي B009` — ما كسبت اليَدان
  - activated_by_or_with: ح م ل
  - themes: agency_action, ethics_morality, justice_judgment, law, obligation_contract
  - keywords: accountability, agency, ethics
- `ي د ي B010` — سقوط اليَد في الندم
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ي د ي B011` — أيادي سبأ
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ي د ي B012` — يَد الدهر
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ي د ي B013` — يَد الشيء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ي د ي B014` — اليَدِي الواسع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ي د ي B015` — اليَدِي الصنّاع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ي د ي B016` — اليَد الناصرة
  - activated_by_or_with: ح ب ل
  - themes: protection_security, trust_loyalty
  - keywords: alliance, protection
- `ي د ي B017` — اليَد للأكل
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### ء ب و

- `ء ب و B001` — الأبوة والتربية
  - activated_by_or_with: غ ن ي
  - themes: authority_governance, family, kinship, protection_security
  - keywords: family, kinship, protection
- `ء ب و B002` — خطاب الأب ومثله
  - activated_by_or_with: ح ب ل, ح ط ب
  - themes: communication, grammar_expression, language_speech, rhetoric_discourse
  - keywords: communication, grammar, language, rhetoric, speech
- `ء ب و B003` — داء الأَبْواء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ل ه ب

- `ل ه ب B001` — لسان النار واشتعالها
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ل ه ب B002` — لهيب العطش والحر
  - activated_by_or_with: ح م ل, م ر ء
  - themes: body, physiology, suffering_hardship
  - keywords: body, physiology, suffering
- `ل ه ب B003` — سطوع مرتفع كاللهب
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ل ه ب B004` — جري يضطرم ويثير الغبار
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ل ه ب B005` — لهب الجبل وفرجته
  - activated_by_or_with: ح ب ل
  - themes: geography_landscape, terrain_desert
  - keywords: geography, landscape, topography
- `ل ه ب B006` — اسم ولقب من اللهب
  - activated_by_or_with: ح ب ل, ح م ل, غ ن ي, م ر ء
  - themes: identity_personhood, kinship, marriage_genealogy, memory_attention, naming_classification
  - keywords: genealogy, identity, kinship, memory, naming, tribe
- `ل ه ب B007` — إلهاب البرق بلا فرجة
  - activated_by_or_with: ح م ل
  - themes: sky_astronomy, weather_climate
  - keywords: weather
- `ل ه ب B008` — المُلهَب في وصف الإنسان
  - activated_by_or_with: ج ي د, ح ط ب, غ ن ي, م ر ء, م س د, ن و ر
  - themes: body, hierarchy_status, honor_shame, identity_personhood, ornament_beauty, rhetoric_discourse, visual_appearance
  - keywords: adornment, aesthetics, appearance, body, description, identity, ornament

### غ ن ي

- `غ ن ي B001` — الغنى والاستغناء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `غ ن ي B002` — الغَناء والكفاية
  - activated_by_or_with: ك س ب
  - themes: commerce_exchange, provision_resource, support_dependence, value_quality
  - keywords: exchange, provision
- `غ ن ي B003` — الغِناء والصوت
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `غ ن ي B004` — الغنى بالمكان
  - activated_by_or_with: ل ه ب
  - themes: memory_attention
  - keywords: memory
- `غ ن ي B005` — الغانية المستغنية
  - activated_by_or_with: ل ه ب, م ر ء
  - themes: gender, hierarchy_status, identity_personhood, ornament_beauty
  - keywords: adornment, gender, identity, ornament
- `غ ن ي B006` — الغنى والتزويج
  - activated_by_or_with: ء ب و, م ر ء
  - themes: authority_governance, family, household_community, kinship, marriage_genealogy, protection_security
  - keywords: family, household, kinship, marriage, protection

### م و ل

- `م و ل B001` — اتخاذ المال وكثرته
  - activated_by_or_with: ك س ب, ي د ي
  - themes: provision_resource, support_dependence, wealth_property
  - keywords: ownership, patronage, property, resource
- `م و ل B002` — المُولة العنكبوت
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ك س ب

- `ك س ب B001` — طلب الرزق والنفع وإصابته
  - activated_by_or_with: ي د ي
  - themes: commerce_exchange, provision_resource, value_quality, wealth_property
  - keywords: benefit, commerce, ownership, provision, wealth
- `ك س ب B002` — إكساب غيره خيرا أو مالا
  - activated_by_or_with: غ ن ي, م و ل, ي د ي
  - themes: commerce_exchange, hospitality_welfare, provision_resource, support_dependence, value_quality, wealth_property
  - keywords: benefit, charity, commerce, exchange, generosity, gift, ownership, patronage, provision, wealth
- `ك س ب B003` — الكواسب الجوارح
  - activated_by_or_with: ت ب ب, ص ل ي
  - themes: animal, body, control_restraint, habitat_ecology, wildlife
  - keywords: animal, body, capture, hunting, predation
- `ك س ب B004` — الكُسب عصارة الدهن
  - activated_by_or_with: ص ل ي
  - themes: agency_action, material, substance_texture
  - keywords: material, processing

### ص ل ي

- `ص ل ي B001` — الصلاة عبادة لازمة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ص ل ي B002` — الدعاء والبركة والرحمة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ص ل ي B003` — ملاقاة النار وحرها
  - activated_by_or_with: ت ب ب
  - themes: justice_judgment, punishment_sanction, suffering_hardship
  - keywords: punishment
- `ص ل ي B004` — إيقاد الصلاء وتسوية الشيء بالنار
  - activated_by_or_with: ن و ر
  - themes: fire_heat
  - keywords: combustion, fire, heat
- `ص ل ي B005` — المَصالي أشراك وفخوخ
  - activated_by_or_with: ك س ب
  - themes: control_restraint, habitat_ecology, wildlife
  - keywords: capture, hunting, predation
- `ص ل ي B006` — الصَّلا موضع الظهر والذنب
  - activated_by_or_with: ت ب ب, ح ب ل, ح م ل, ك س ب, م ر ء, م س د
  - themes: anatomy, animal, body, kinship, reproduction_birth
  - keywords: anatomy, animal, birth, body, kinship, reproduction
- `ص ل ي B007` — المصلي يتلو السابق
  - activated_by_or_with: ح ب ل
  - themes: motion, recreation_sport
  - keywords: sport
- `ص ل ي B008` — الصلوات مواضع عبادة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ص ل ي B009` — الصلاية حجر يدق عليه
  - activated_by_or_with: ك س ب
  - themes: agency_action, material, substance_texture
  - keywords: material, processing
- `ص ل ي B010` — الصِّليان نبت ترعاه الإبل
  - activated_by_or_with: ح ب ل, ح م ل
  - themes: agriculture, animal, food_nutrition, habitat_ecology, husbandry, pasture_forage, plant_vegetation
  - keywords: agriculture, animal, botany, ecology, food, pastoralism, pasture

### ن و ر

- `ن و ر B001` — الضياء والإضاءة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن و ر B002` — النار المتقدة والسمة بها
  - activated_by_or_with: ص ل ي
  - themes: fire_heat
  - keywords: combustion, fire, heat
- `ن و ر B003` — تنور النار من بعيد
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن و ر B004` — نور الشجر وزهره
  - activated_by_or_with: ح ب ل, ح م ل
  - themes: calendar_season, growth_decay, plant_vegetation, reproduction_birth
  - keywords: botany, fertility, growth, season
- `ن و ر B005` — المنار والمنارة الظاهرة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن و ر B006` — النِّفار وقلة الثبات
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن و ر B007` — النائرة بين القوم
  - activated_by_or_with: ح ط ب
  - themes: conflict, social_relations, violence_warfare
  - keywords: conflict, society, violence
- `ن و ر B008` — دخان الوشم والكحل
  - activated_by_or_with: ل ه ب, م ر ء
  - themes: body, health_medicine, ornament_beauty
  - keywords: adornment, body, medicine
- `ن و ر B009` — النُّورَة المطلية
  - activated_by_or_with: م س د
  - themes: body, hygiene_sanitation, ornament_beauty, substance_texture
  - keywords: body, grooming
- `ن و ر B010` — التلبيس على الغير
  - activated_by_or_with: ح ط ب
  - themes: cognition, communication, proof_uncertainty, rhetoric_discourse
  - keywords: cognition, communication, rhetoric, uncertainty
- `ن و ر B011` — وضوح النِّير وبروزه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### م ر ء

- `م ر ء root_001409:B001` — المرء والمرأة
  - activated_by_or_with: ح ب ل, ح م ل, غ ن ي, ل ه ب
  - themes: gender, identity_personhood, kinship, social_relations
  - keywords: gender, identity, kinship, society
- `م ر ء root_001409:B002` — المروءة
  - activated_by_or_with: ح ط ب
  - themes: ethics_morality, honor_shame, social_relations
  - keywords: ethics, reputation, society
- `م ر ء root_001409:B003` — الطعام المريء
  - activated_by_or_with: same-root only
  - themes: cooking_drink, desire_appetite, food_nutrition, health_medicine, physiology
  - keywords: appetite, comfort, cuisine, digestion, food, health, nutrition
- `م ر ء root_001409:B004` — المريء
  - activated_by_or_with: ح ب ل, ص ل ي, ل ه ب, م س د, ن و ر
  - themes: anatomy, body, food_nutrition, health_medicine, navigation_route, physiology
  - keywords: anatomy, body, digestion, ingestion, medicine, passage, physiology
- `م ر ء root_001409:B005` — الطعم والإطعام
  - activated_by_or_with: غ ن ي, م س د
  - themes: food_nutrition, household_community, kinship, marriage_genealogy
  - keywords: food, household, kinship, marriage
- `م ر ء root_001410:B001` — المَرْء والمرأة
  - activated_by_or_with: ح ب ل, ح م ل, غ ن ي, ل ه ب
  - themes: gender, identity_personhood, kinship, social_relations
  - keywords: gender, identity, kinship, society
- `م ر ء root_001410:B002` — المروءة وكمال الرجولية
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `م ر ء root_001410:B003` — مراءة الطعام واستمراؤه
  - activated_by_or_with: ح ط ب
  - themes: body, cooking_drink, desire_appetite, food_nutrition, health_medicine, physiology
  - keywords: appetite, body, comfort, cuisine, digestion, food, health, nutrition
- `م ر ء root_001410:B004` — الطعم والإطعام في مناسبة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `م ر ء root_001410:B005` — المَرِيء مجرى الطعام
  - activated_by_or_with: ح ب ل, ص ل ي, ل ه ب, ن و ر
  - themes: anatomy, body, food_nutrition, health_medicine, navigation_route, physiology
  - keywords: anatomy, body, digestion, ingestion, medicine, passage, physiology
- `م ر ء root_001410:B006` — الرجل المَرِيء المقبول
  - activated_by_or_with: ح ط ب, ل ه ب, م س د
  - themes: ethics_morality, honor_shame, identity_personhood, ornament_beauty, social_relations, visual_appearance
  - keywords: aesthetics, appearance, beauty, ethics, reputation, society

### ح م ل

- `ح م ل B001` — إقلال المحمول الظاهر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح م ل B002` — الحَمْل الباطن والثمر
  - activated_by_or_with: ح ب ل, ص ل ي, ن و ر
  - themes: agriculture, calendar_season, growth_decay, harvest_cultivation, kinship, physiology, plant_vegetation, reproduction_birth
  - keywords: agriculture, biology, birth, botany, fertility, growth, harvest, kinship, reproduction, season
- `ح م ل B003` — تحمّل الأمانة والوزر
  - activated_by_or_with: ي د ي
  - themes: agency_action, ethics_morality, justice_judgment, law, obligation_contract
  - keywords: accountability, agency, ethics
- `ح م ل B004` — الحمالة والكفالة
  - activated_by_or_with: ي د ي
  - themes: finance_debt, obligation_contract
  - keywords: contract, finance
- `ح م ل B005` — الحميل المحمول في النسب
  - activated_by_or_with: ح ب ل, ل ه ب, م ر ء
  - themes: identity_personhood, kinship, marriage_genealogy, social_relations
  - keywords: identity, kinship
- `ح م ل B006` — أداة الحمل ومركوبه
  - activated_by_or_with: م س د
  - themes: material, motion, tools_equipment, transport
  - keywords: technology, tool, transport
- `ح م ل B007` — التحامل والمشقة
  - activated_by_or_with: ل ه ب, م س د
  - themes: body, labor_work, physiology, stability_endurance, suffering_hardship, travel
  - keywords: body, effort, endurance, suffering, travel
- `ح م ل B008` — احتمال الغضب والحلم
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح م ل B009` — الحَمَل من الضأن
  - activated_by_or_with: ح ب ل, ص ل ي
  - themes: agriculture, animal, food_nutrition, husbandry, pasture_forage
  - keywords: agriculture, animal, food, pastoralism, pasture
- `ح م ل B010` — الحَمَل في السماء والسحاب
  - activated_by_or_with: ل ه ب
  - themes: sky_astronomy, weather_climate
  - keywords: weather

### ح ط ب

- `ح ط ب B001` — الحطب وقود يجمع ويحتطب
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح ط ب B002` — حاطب الليل يخلط الرديء والجيد
  - activated_by_or_with: ء ب و, ن و ر
  - themes: cognition, communication, language_speech, proof_uncertainty, rhetoric_discourse
  - keywords: cognition, communication, language, rhetoric, uncertainty
- `ح ط ب B003` — حمل الحطب كناية عن النميمة والسعاية
  - activated_by_or_with: م ر ء, ن و ر
  - themes: conflict, ethics_morality, honor_shame, social_relations, violence_warfare
  - keywords: conflict, ethics, reputation, society, violence
- `ح ط ب B004` — الهزال كالحطب اليابس
  - activated_by_or_with: ل ه ب, م ر ء, م س د
  - themes: body, health_medicine, rhetoric_discourse, visual_appearance
  - keywords: appearance, body, health, metaphor

### ج ي د

- `ج ي د B001` — الجيد والعنق
  - activated_by_or_with: ل ه ب, م س د
  - themes: anatomy, body, measurement, ornament_beauty, rhetoric_discourse, visual_appearance
  - keywords: anatomy, appearance, beauty, body, description, proportion

### ح ب ل

- `ح ب ل B001` — حبل ممدود يربط ويقاد به
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح ب ل B002` — حبل عهد وأمان ووصل
  - activated_by_or_with: ي د ي
  - themes: protection_security, trust_loyalty
  - keywords: alliance, protection
- `ح ب ل B003` — رمل مستطيل ممتد
  - activated_by_or_with: ل ه ب
  - themes: geography_landscape, terrain_desert
  - keywords: geography, landscape, topography
- `ح ب ل B004` — حبال البدن عروق ووصلات
  - activated_by_or_with: م ر ء
  - themes: anatomy, health_medicine, physiology
  - keywords: anatomy, medicine, physiology
- `ح ب ل B005` — حبالة تصيد وتوقع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح ب ل B006` — حمل يمتد في البطن
  - activated_by_or_with: ح م ل, ص ل ي
  - themes: growth_decay, kinship, physiology, reproduction_birth
  - keywords: biology, fertility, kinship, reproduction
- `ح ب ل B007` — حبلة نبات وثمر ممتد
  - activated_by_or_with: ح م ل, ص ل ي, ن و ر
  - themes: agriculture, food_nutrition, growth_decay, habitat_ecology, harvest_cultivation, plant_vegetation
  - keywords: agriculture, botany, ecology, food, growth, harvest
- `ح ب ل B008` — حبلة حلي في القلادة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح ب ل B009` — حبل موضع وموقف
  - activated_by_or_with: ص ل ي
  - themes: motion, recreation_sport
  - keywords: sport
- `ح ب ل B010` — نسبة واسم إلى الحبلى
  - activated_by_or_with: ح م ل, ل ه ب, م ر ء
  - themes: identity_personhood, kinship, marriage_genealogy, naming_classification, social_relations
  - keywords: genealogy, identity, kinship, naming, society, tribe
- `ح ب ل B011` — داهية تحبل بصاحبها
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح ب ل B012` — حبيل براح ثابت لا يفر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح ب ل B013` — سعة وضيق وامتلاء داخلي
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح ب ل B014` — حبالة حين ووقت
  - activated_by_or_with: ء ب و
  - themes: grammar_expression, language_speech, rhetoric_discourse
  - keywords: grammar, language, speech
- `ح ب ل B015` — محبل كتاب أو كتابة
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### م س د

- `م س د B001` — الحبل المفتول
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `م س د B002` — الجسم الممسود
  - activated_by_or_with: ج ي د, ح ط ب, ص ل ي, ل ه ب, م ر ء
  - themes: anatomy, body, measurement, ornament_beauty, rhetoric_discourse, visual_appearance
  - keywords: aesthetics, anatomy, appearance, beauty, body, metaphor, proportion
- `م س د B003` — إدآب السير في الليل
  - activated_by_or_with: ح م ل
  - themes: labor_work, stability_endurance, suffering_hardship, travel
  - keywords: effort, endurance, travel
- `م س د B004` — المِساد نحي السمن والعسل
  - activated_by_or_with: م ر ء
  - themes: food_nutrition, household_community
  - keywords: food, household
- `م س د B005` — محور الحديد
  - activated_by_or_with: ح م ل
  - themes: material, motion, tools_equipment, transport
  - keywords: technology, tool, transport
- `م س د B006` — المِساد الرق الأسود
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `م س د B007` — مساد الشعر
  - activated_by_or_with: ج ي د, ل ه ب, م ر ء, ن و ر
  - themes: anatomy, body, hygiene_sanitation, ornament_beauty, substance_texture, visual_appearance
  - keywords: aesthetics, appearance, beauty, body, grooming, ornament

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
