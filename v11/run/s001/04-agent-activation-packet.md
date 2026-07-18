# v11 Activation Packet — S1:1-None

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_1 (basmala; part of analysis): ﻿بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- verse_2: ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- verse_3: ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- verse_4: مَٰلِكِ يَوْمِ ٱلدِّينِ
- verse_5: إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- verse_6: ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- verse_7: صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

س م و → ء ل ه → ر ح م → ح م د → ر ب ب → ع ل م → م ل ك → ي و م → د ي ن → ع ب د → ع و ن → ه د ي → ص ر ط → ق و م → ن ع م → غ ي ر → غ ض ب → ض ل ل

## Branch inventory summary

- س م و: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء ل ه: 2 branches (2 with Qnet bridge-theme nodes; 0 Furūq-only)
- ر ح م: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- ح م د: 6 branches (5 with Qnet bridge-theme nodes; 1 Furūq-only)
- ر ب ب: 17 branches (17 with Qnet bridge-theme nodes; 0 Furūq-only)
- ع ل م: 7 branches (6 with Qnet bridge-theme nodes; 1 Furūq-only)
- م ل ك: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- ي و م: 5 branches (3 with Qnet bridge-theme nodes; 2 Furūq-only)
- د ي ن: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- ع ب د: 12 branches (11 with Qnet bridge-theme nodes; 1 Furūq-only)
- ع و ن: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ه د ي: 11 branches (11 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص ر ط: 3 branches (3 with Qnet bridge-theme nodes; 0 Furūq-only)
- ق و م: 21 branches (20 with Qnet bridge-theme nodes; 1 Furūq-only)
- ن ع م: 13 branches (13 with Qnet bridge-theme nodes; 0 Furūq-only)
- غ ي ر: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- غ ض ب: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ض ل ل: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)

## QAC-first root resolution audit

- س م و | qac_keys=سمو | status=resolved | matches=root_000745
- ء ل ه | qac_keys=ءله | status=resolved | matches=root_000047
- ر ح م | qac_keys=رحم | status=resolved | matches=root_000552
- ح م د | qac_keys=حمد | status=resolved | matches=root_000355
- ر ب ب | qac_keys=ربب | status=resolved | matches=root_000532
- ع ل م | qac_keys=علم | status=resolved | matches=root_001040
- م ل ك | qac_keys=ملك | status=resolved | matches=root_001444
- ي و م | qac_keys=يوم | status=resolved | matches=root_001700
- د ي ن | qac_keys=دين | status=resolved | matches=root_000504
- ع ب د | qac_keys=عبد | status=resolved | matches=root_000973
- ع و ن | qac_keys=عون | status=resolved | matches=root_001064
- ه د ي | qac_keys=هدي | status=resolved | matches=root_001583
- ص ر ط | qac_keys=صرط | status=resolved | matches=root_000858
- ق و م | qac_keys=قوم | status=resolved | matches=root_001273
- ن ع م | qac_keys=نعم | status=resolved | matches=root_001525
- غ ي ر | qac_keys=غير | status=resolved | matches=root_001119
- غ ض ب | qac_keys=غضب | status=resolved | matches=root_001092
- ض ل ل | qac_keys=ضلل | status=resolved | matches=root_000913

## Top candidate bridges

- `د ي ن B001` ↔ `ع ب د B003` | score_hint=31 | discovery_hint=20 | themes=authority_governance, religion_worship, ritual | keywords=authority, devotion, religion, ritual, submission | q2=S001-BR0037
- `ر ب ب B014` ↔ `ع و ن B006` | score_hint=27 | discovery_hint=20 | themes=animal, habitat_ecology, household_community, husbandry, wildlife | keywords=collectivity, ecology, zoology | q2=S001-BR0019
- `ن ع م B005` ↔ `ض ل ل B005` | score_hint=19 | discovery_hint=20 | themes=animal, husbandry, wealth_property | keywords=animal, pastoralism | q2=S001-BR0034
- `ه د ي B001` ↔ `ض ل ل B001` | score_hint=35 | discovery_hint=19 | themes=ethics_morality, navigation_route, orientation_direction, proof_uncertainty, religion_worship | keywords=ethics, navigation, orientation, religion, truth | q2=S001-BR0023
- `د ي ن B005` ↔ `ه د ي B002` | score_hint=23 | discovery_hint=19 | themes=agency_action, culture_tradition, identity_personhood | keywords=behavior, custom, identity, practice | q2=—
- `ي و م B001` ↔ `ي و م B002` | score_hint=25 | discovery_hint=18 | themes=measurement, sequence_cycle, sky_astronomy, time | keywords=measure, time | q2=S001-BR0014, S001-BR0084
- `ص ر ط B001` ↔ `ق و م B008` | score_hint=21 | discovery_hint=18 | themes=belief_revelation, ethics_morality, orientation_direction, politics_order | keywords=ethics, order | q2=S001-BR0024
- `د ي ن B002` ↔ `د ي ن B003` | score_hint=16 | discovery_hint=18 | themes=commerce_exchange, measurement | keywords=exchange, measure | q2=S001-BR0001
- `ر ب ب B001` ↔ `ق و م B004` | score_hint=15 | discovery_hint=18 | themes=authority_governance | keywords=authority, governance | q2=S001-BR0020
- `ر ب ب B014` ↔ `ن ع م B005` | score_hint=13 | discovery_hint=18 | themes=animal, husbandry | keywords=pastoralism | q2=S001-BR0046
- `ي و م B001` ↔ `ق و م B017` | score_hint=21 | discovery_hint=18 | themes=light_darkness, measurement, sky_astronomy, time | keywords=astronomy, measurement, time | q2=—
- `ر ح م B001` ↔ `ن ع م B001` | score_hint=19 | discovery_hint=17 | themes=belief_revelation, ethics_morality, hospitality_welfare | keywords=charity, ethics | q2=S001-BR0036
- `ق و م B002` ↔ `ق و م B016` | score_hint=18 | discovery_hint=17 | themes=animal, motion, physiology | keywords=animal, motion | q2=S001-BR0015
- `غ ض ب B004` ↔ `غ ض ب B008` | score_hint=16 | discovery_hint=17 | themes=material, substance_texture | keywords=hardness, material | q2=S001-BR0069
- `ع ب د B008` ↔ `غ ض ب B001` | score_hint=11 | discovery_hint=17 | themes=emotion | keywords=emotion | q2=S001-BR0027
- `ه د ي B005` ↔ `ه د ي B007` | score_hint=15 | discovery_hint=16 | themes=religion_worship | keywords=sanctuary | q2=S001-BR0003, S001-BR0028
- `م ل ك B006` ↔ `م ل ك B008` | score_hint=16 | discovery_hint=16 | themes=motion, navigation_route | keywords=movement, navigation | q2=S001-BR0013
- `ر ب ب B005` ↔ `ر ب ب B016` | score_hint=12 | discovery_hint=16 | themes=hospitality_welfare, support_dependence | keywords=dependency | q2=S001-BR0054
- `ر ب ب B001` ↔ `غ ض ب B001` | score_hint=11 | discovery_hint=16 | themes=belief_revelation | keywords=theology | q2=S001-BR0042
- `س م و B004` ↔ `ر ب ب B008` | score_hint=18 | discovery_hint=16 | themes=agriculture, sky_astronomy, weather_climate | keywords=agriculture, meteorology, weather | q2=—
- `ع ب د B007` ↔ `غ ض ب B008` | score_hint=15 | discovery_hint=16 | themes=animal, material, textile_clothing | keywords=animal, material | q2=—
- `ع ب د B008` ↔ `غ ض ب B002` | score_hint=13 | discovery_hint=16 | themes=fear_grief, honor_shame | keywords=honor, mourning | q2=—
- `ر ب ب B010` ↔ `ع ب د B012` | score_hint=9 | discovery_hint=16 | themes=ritual, storage_vessels | keywords=ritual | q2=—
- `ع و ن B007` ↔ `ص ر ط B002` | score_hint=9 | discovery_hint=16 | themes=body, containment_access | keywords=body | q2=—
- `م ل ك B001` ↔ `م ل ك B005` | score_hint=16 | discovery_hint=15 | themes=form_structure, stability_endurance | keywords=stability, structure | q2=S001-BR0004
- `ر ب ب B012` ↔ `ر ب ب B013` | score_hint=12 | discovery_hint=15 | themes=geography_landscape, habitat_ecology | keywords=ecology | q2=S001-BR0056
- `م ل ك B003` ↔ `م ل ك B008` | score_hint=12 | discovery_hint=15 | themes=authority_governance, hierarchy_status | keywords=hierarchy | q2=S001-BR0013
- `ي و م B002` ↔ `ي و م B003` | score_hint=12 | discovery_hint=15 | themes=sequence_cycle, time | keywords=history | q2=S001-BR0014
- `ر ب ب B003` ↔ `ر ب ب B016` | score_hint=10 | discovery_hint=15 | themes=ethics_morality | keywords=ethics | q2=S001-BR0002
- `م ل ك B002` ↔ `م ل ك B004` | score_hint=10 | discovery_hint=15 | themes=law | keywords=law | q2=S001-BR0075
- `د ي ن B004` ↔ `د ي ن B006` | score_hint=10 | discovery_hint=15 | themes=authority_governance | keywords=authority | q2=S001-BR0049
- `ه د ي B004` ↔ `ه د ي B006` | score_hint=10 | discovery_hint=15 | themes=kinship | keywords=kinship | q2=S001-BR0030
- `ق و م B011` ↔ `ق و م B012` | score_hint=10 | discovery_hint=15 | themes=anatomy | keywords=anatomy | q2=S001-BR0073
- `ر ب ب B013` ↔ `ع ل م B005` | score_hint=30 | discovery_hint=15 | themes=abundance_scarcity, geography_landscape, habitat_ecology, provision_resource, water_hydrology | keywords=abundance, geography, hydrology, nature, resource | q2=—
- `د ي ن B004` ↔ `ع ب د B004` | score_hint=30 | discovery_hint=15 | themes=control_restraint, force_power, hierarchy_status, justice_judgment, violence_warfare | keywords=control, hierarchy, oppression, power, violence | q2=—
- `ح م د B005` ↔ `ن ع م B001` | score_hint=24 | discovery_hint=15 | themes=commerce_exchange, ethics_morality, hospitality_welfare, support_dependence | keywords=charity, gratitude, patronage, reciprocity | q2=—
- `ر ب ب B012` ↔ `ع و ن B004` | score_hint=18 | discovery_hint=15 | themes=agriculture, habitat_ecology, plant_vegetation | keywords=agriculture, botany, ecology | q2=—
- `د ي ن B003` ↔ `ق و م B010` | score_hint=18 | discovery_hint=15 | themes=commerce_exchange, economy, measurement | keywords=commerce, economy, exchange | q2=—
- `د ي ن B003` ↔ `ه د ي B004` | score_hint=16 | discovery_hint=15 | themes=commerce_exchange, wealth_property | keywords=commerce, exchange, property | q2=—
- `ء ل ه B001` ↔ `ه د ي B005` | score_hint=15 | discovery_hint=15 | themes=pilgrimage_sacrifice, religion_worship, ritual | keywords=religion, sacrifice | q2=—
- `ر ب ب B002` ↔ `ع و ن B004` | score_hint=14 | discovery_hint=15 | themes=agriculture, growth_decay, life_stage_aging | keywords=agriculture, growth | q2=—
- `ر ب ب B013` ↔ `ع و ن B008` | score_hint=9 | discovery_hint=15 | themes=cooking_drink, geography_landscape | keywords=geography | q2=—
- `ء ل ه B002` ↔ `ن ع م B013` | score_hint=7 | discovery_hint=15 | themes=prayer_supplication | keywords=prayer | q2=—
- `ع ل م B006` ↔ `ع ب د B009` | score_hint=7 | discovery_hint=15 | themes=speed | keywords=speed | q2=—
- `ح م د B001` ↔ `ح م د B003` | score_hint=12 | discovery_hint=14 | themes=ethics_morality, value_quality | keywords=evaluation | q2=S001-BR0022
- `ه د ي B001` ↔ `ه د ي B005` | score_hint=10 | discovery_hint=14 | themes=religion_worship | keywords=religion | q2=S001-BR0003
- `ه د ي B001` ↔ `ه د ي B010` | score_hint=10 | discovery_hint=14 | themes=ethics_morality | keywords=ethics | q2=S001-BR0003
- `ر ب ب B001` ↔ `م ل ك B003` | score_hint=24 | discovery_hint=14 | themes=authority_governance, belief_revelation, force_power, hierarchy_status | keywords=governance, hierarchy, power, theology | q2=—
- `ق و م B019` ↔ `غ ض ب B006` | score_hint=24 | discovery_hint=14 | themes=anatomy, disease_injury, health_medicine, perception | keywords=anatomy, disease, medicine, symptom | q2=—
- `ع و ن B003` ↔ `ق و م B014` | score_hint=20 | discovery_hint=14 | themes=conflict, violence_warfare | keywords=conflict, struggle, violence, warfare | q2=—
- `س م و B005` ↔ `غ ي ر B005` | score_hint=20 | discovery_hint=14 | themes=identity_personhood, language_speech, naming_classification, reasoning_decision | keywords=classification, identity, language | q2=—
- `ر ب ب B001` ↔ `د ي ن B004` | score_hint=20 | discovery_hint=14 | themes=authority_governance, force_power, hierarchy_status, wealth_property | keywords=authority, hierarchy, power | q2=—
- `ر ب ب B013` ↔ `م ل ك B007` | score_hint=18 | discovery_hint=14 | themes=habitat_ecology, provision_resource, water_hydrology | keywords=ecology, hydrology, resource | q2=—
- `م ل ك B005` ↔ `ق و م B009` | score_hint=18 | discovery_hint=14 | themes=form_structure, stability_endurance, support_dependence | keywords=organization, stability, structure | q2=—
- `د ي ن B002` ↔ `غ ي ر B002` | score_hint=18 | discovery_hint=14 | themes=commerce_exchange, justice_judgment, punishment_sanction | keywords=exchange, justice, punishment | q2=—
- `د ي ن B003` ↔ `ق و م B018` | score_hint=18 | discovery_hint=14 | themes=commerce_exchange, economy, obligation_contract | keywords=commerce, economy, exchange | q2=—
- `ع و ن B007` ↔ `ق و م B019` | score_hint=18 | discovery_hint=14 | themes=anatomy, body, health_medicine | keywords=anatomy, body, medicine | q2=—
- `ه د ي B008` ↔ `ن ع م B012` | score_hint=18 | discovery_hint=14 | themes=body, motion, transport | keywords=body, locomotion, transport | q2=—
- `غ ي ر B004` ↔ `غ ض ب B002` | score_hint=18 | discovery_hint=14 | themes=honor_shame, kinship, protection_security | keywords=honor, kinship, protection | q2=—
- `ص ر ط B003` ↔ `ق و م B014` | score_hint=16 | discovery_hint=14 | themes=force_power, violence_warfare | keywords=force, violence, warfare | q2=—
- `ر ح م B003` ↔ `ع و ن B002` | score_hint=12 | discovery_hint=14 | themes=growth_decay, physiology | keywords=biology, development | q2=—
- `د ي ن B003` ↔ `ق و م B015` | score_hint=10 | discovery_hint=14 | themes=commerce_exchange, finance_debt, measurement | keywords=commerce | q2=—
- `ي و م B001` ↔ `ن ع م B009` | score_hint=9 | discovery_hint=14 | themes=calendar_season, habitat_ecology | keywords=nature | q2=—
- `ر ب ب B005` ↔ `ع و ن B002` | score_hint=5 | discovery_hint=13 | themes=— | keywords=— | q2=S001-BR0043
- `ر ب ب B005` ↔ `ن ع م B007` | score_hint=5 | discovery_hint=13 | themes=— | keywords=— | q2=S001-BR0047
- `ق و م B007` ↔ `ض ل ل B003` | score_hint=5 | discovery_hint=13 | themes=— | keywords=— | q2=S001-BR0029
- `ء ل ه B001` ↔ `ع ب د B003` | score_hint=24 | discovery_hint=13 | themes=authority_governance, belief_revelation, religion_worship, ritual | keywords=authority, religion, submission, theology | q2=—
- `س م و B006` ↔ `ع و ن B006` | score_hint=20 | discovery_hint=13 | themes=animal, habitat_ecology, motion, wildlife | keywords=mobility, wilderness, wildlife | q2=—
- `ر ح م B002` ↔ `م ل ك B004` | score_hint=20 | discovery_hint=13 | themes=family, law, obligation_contract, social_relations | keywords=family, law, society | q2=—
- `ر ب ب B014` ↔ `ض ل ل B005` | score_hint=20 | discovery_hint=13 | themes=animal, husbandry, livestock, terrain_desert | keywords=desert, livestock, pastoralism | q2=—
- `ع ل م B006` ↔ `ن ع م B006` | score_hint=20 | discovery_hint=13 | themes=animal, habitat_ecology, naming_classification, wildlife | keywords=taxonomy, wildlife, zoology | q2=—
- `ع ل م B007` ↔ `ن ع م B006` | score_hint=20 | discovery_hint=13 | themes=animal, habitat_ecology, naming_classification, wildlife | keywords=taxonomy, wildlife, zoology | q2=—
- `م ل ك B002` ↔ `ع ب د B001` | score_hint=20 | discovery_hint=13 | themes=hierarchy_status, labor_work, law, wealth_property | keywords=labor, law, property | q2=—
- `ق و م B021` ↔ `غ ض ب B006` | score_hint=20 | discovery_hint=13 | themes=anatomy, disease_injury, health_medicine, perception | keywords=anatomy, medicine, vision | q2=—
- `س م و B006` ↔ `ع ل م B006` | score_hint=18 | discovery_hint=13 | themes=animal, habitat_ecology, wildlife | keywords=hunting, predation, wildlife | q2=—
- `ر ح م B002` ↔ `ق و م B001` | score_hint=18 | discovery_hint=13 | themes=household_community, identity_personhood, social_relations | keywords=community, identity, society | q2=—
- `ر ح م B004` ↔ `ق و م B019` | score_hint=18 | discovery_hint=13 | themes=anatomy, disease_injury, health_medicine | keywords=anatomy, medicine, pathology | q2=—
- `ر ح م B004` ↔ `ق و م B020` | score_hint=18 | discovery_hint=13 | themes=animal, disease_injury, health_medicine | keywords=animal, medicine, veterinary | q2=—
- `ح م د B002` ↔ `ن ع م B003` | score_hint=18 | discovery_hint=13 | themes=honor_shame, justice_judgment, value_quality | keywords=evaluation, judgment, quality | q2=—
- `ر ب ب B005` ↔ `ه د ي B006` | score_hint=18 | discovery_hint=13 | themes=family, household_community, kinship | keywords=family, household, kinship | q2=—

## Per-root candidate activations

### س م و

- `س م و B001` — العلو والارتفاع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `س م و B002` — الشخص المرتفع الظاهر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `س م و B003` — تطاول الفحل على الشول
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `س م و B004` — السماء وما علا فأظل
  - activated_by_or_with: ر ب ب
  - themes: agriculture, sky_astronomy, weather_climate
  - keywords: agriculture, meteorology, weather
- `س م و B005` — الاسم تنويه ودلالة
  - activated_by_or_with: غ ي ر
  - themes: identity_personhood, language_speech, naming_classification, reasoning_decision
  - keywords: classification, identity, language
- `س م و B006` — الخروج للصيد
  - activated_by_or_with: ع ل م, ع و ن
  - themes: animal, habitat_ecology, motion, wildlife
  - keywords: hunting, mobility, predation, wilderness, wildlife
- `س م و B007` — المساماة والمباراة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `س م و B008` — الصيت الحسن المنتشر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ء ل ه

- `ء ل ه B001` — التعبد والمعبود
  - activated_by_or_with: ع ب د, ه د ي
  - themes: authority_governance, belief_revelation, pilgrimage_sacrifice, religion_worship, ritual
  - keywords: authority, religion, sacrifice, submission, theology
- `ء ل ه B002` — اسم الله في القسم والنداء
  - activated_by_or_with: ن ع م
  - themes: prayer_supplication
  - keywords: prayer

### ر ح م

- `ر ح م B001` — الرَّحْمَة والرقة
  - activated_by_or_with: ن ع م
  - themes: belief_revelation, ethics_morality, hospitality_welfare
  - keywords: charity, ethics
- `ر ح م B002` — الرَّحِم والقرابة
  - activated_by_or_with: ق و م, م ل ك
  - themes: family, household_community, identity_personhood, law, obligation_contract, social_relations
  - keywords: community, family, identity, law, society
- `ر ح م B003` — رَحِم الأنثى
  - activated_by_or_with: ع و ن
  - themes: growth_decay, physiology
  - keywords: biology, development
- `ر ح م B004` — وجع الرَّحِم بعد الولادة
  - activated_by_or_with: ق و م
  - themes: anatomy, animal, disease_injury, health_medicine
  - keywords: anatomy, animal, medicine, pathology, veterinary

### ح م د

- `ح م د B001` — الحمد خلاف الذم
  - activated_by_or_with: same-root only
  - themes: ethics_morality, value_quality
  - keywords: evaluation
- `ح م د B002` — وجود الشيء محمودا
  - activated_by_or_with: ن ع م
  - themes: honor_shame, justice_judgment, value_quality
  - keywords: evaluation, judgment, quality
- `ح م د B003` — المحمود كثير الخصال
  - activated_by_or_with: same-root only
  - themes: ethics_morality, value_quality
  - keywords: evaluation
- `ح م د B004` — حماداك الغاية المحمودة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ح م د B005` — يتحمد بالمنة
  - activated_by_or_with: ن ع م
  - themes: commerce_exchange, ethics_morality, hospitality_welfare, support_dependence
  - keywords: charity, gratitude, patronage, reciprocity
- `ح م د B006` — أحمد إليك الله
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### ر ب ب

- `ر ب ب B001` — ربوبية وملك وسيادة
  - activated_by_or_with: د ي ن, غ ض ب, ق و م, م ل ك
  - themes: authority_governance, belief_revelation, force_power, hierarchy_status, wealth_property
  - keywords: authority, governance, hierarchy, power, theology
- `ر ب ب B002` — إصلاح وتربية وإتمام
  - activated_by_or_with: ع و ن
  - themes: agriculture, growth_decay, life_stage_aging
  - keywords: agriculture, growth
- `ر ب ب B003` — علم رباني
  - activated_by_or_with: same-root only
  - themes: ethics_morality
  - keywords: ethics
- `ر ب ب B004` — ربة وجماعات كثيرة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B005` — ربيب وربيبة ورابة
  - activated_by_or_with: ع و ن, ن ع م, ه د ي
  - themes: family, hospitality_welfare, household_community, kinship, support_dependence
  - keywords: dependency, family, household, kinship
- `ر ب ب B006` — رُبّ خاثر وإصلاح به
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B007` — لزوم وإقامة ودوام
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B008` — رباب السحاب
  - activated_by_or_with: س م و
  - themes: agriculture, sky_astronomy, weather_climate
  - keywords: agriculture, meteorology, weather
- `ر ب ب B009` — شاة رُبّى وحداثة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B010` — ربابة تجمع القداح
  - activated_by_or_with: ع ب د
  - themes: ritual, storage_vessels
  - keywords: ritual
- `ر ب ب B011` — ربابة عهد وميثاق
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B012` — ربة نبات
  - activated_by_or_with: ع و ن
  - themes: agriculture, geography_landscape, habitat_ecology, plant_vegetation
  - keywords: agriculture, botany, ecology
- `ر ب ب B013` — ماء رَبَب كثير
  - activated_by_or_with: ع ل م, ع و ن, م ل ك
  - themes: abundance_scarcity, cooking_drink, geography_landscape, habitat_ecology, provision_resource, water_hydrology
  - keywords: abundance, ecology, geography, hydrology, nature, resource
- `ر ب ب B014` — رَبْرَب قطيع
  - activated_by_or_with: ض ل ل, ع و ن, ن ع م
  - themes: animal, habitat_ecology, household_community, husbandry, livestock, terrain_desert, wildlife
  - keywords: collectivity, desert, ecology, livestock, pastoralism, zoology
- `ر ب ب B015` — حرف رب وربما
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B016` — رُبَى حاجة وعقدة ونعمة
  - activated_by_or_with: same-root only
  - themes: ethics_morality, hospitality_welfare, support_dependence
  - keywords: dependency, ethics
- `ر ب ب B017` — رباني الملاحين
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ع ل م

- `ع ل م B001` — انكشاف الشيء للعارف
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ل م B002` — أثر يميز الشيء ويهدي إليه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ل م B003` — الخلق عالم يدل على صانعه
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ع ل م B004` — شق ظاهر في الشفة العليا
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ل م B005` — ماء كثير مجتمع في عيلم
  - activated_by_or_with: ر ب ب
  - themes: abundance_scarcity, geography_landscape, habitat_ecology, provision_resource, water_hydrology
  - keywords: abundance, geography, hydrology, nature, resource
- `ع ل م B006` — طائر جارح يسمى العلام
  - activated_by_or_with: س م و, ع ب د, ن ع م
  - themes: animal, habitat_ecology, naming_classification, speed, wildlife
  - keywords: hunting, predation, speed, taxonomy, wildlife, zoology
- `ع ل م B007` — ذكر الضباع يسمى العيلام
  - activated_by_or_with: ن ع م
  - themes: animal, habitat_ecology, naming_classification, wildlife
  - keywords: taxonomy, wildlife, zoology

### م ل ك

- `م ل ك B001` — قوة الشيء وتماسكه
  - activated_by_or_with: same-root only
  - themes: form_structure, stability_endurance
  - keywords: stability, structure
- `م ل ك B002` — المِلْك والتصرف
  - activated_by_or_with: ع ب د
  - themes: hierarchy_status, labor_work, law, wealth_property
  - keywords: labor, law, property
- `م ل ك B003` — المُلك والسلطان
  - activated_by_or_with: ر ب ب
  - themes: authority_governance, belief_revelation, force_power, hierarchy_status
  - keywords: governance, hierarchy, power, theology
- `م ل ك B004` — الإملاك والتزويج
  - activated_by_or_with: ر ح م
  - themes: family, law, obligation_contract, social_relations
  - keywords: family, law, society
- `م ل ك B005` — مِلاك الأمر وعِماده
  - activated_by_or_with: ق و م
  - themes: form_structure, stability_endurance, support_dependence
  - keywords: organization, stability, structure
- `م ل ك B006` — مَلَك الطريق والوادي
  - activated_by_or_with: same-root only
  - themes: motion, navigation_route
  - keywords: movement, navigation
- `م ل ك B007` — الماء مَلَك الأمر
  - activated_by_or_with: ر ب ب
  - themes: habitat_ecology, provision_resource, water_hydrology
  - keywords: ecology, hydrology, resource
- `م ل ك B008` — المتقدم القائد في الحيوان
  - activated_by_or_with: same-root only
  - themes: authority_governance, hierarchy_status, motion, navigation_route
  - keywords: hierarchy, movement, navigation
- `م ل ك B009` — المَلَك من الملائكة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ي و م

- `ي و م B001` — وقت النهار المحدود
  - activated_by_or_with: ق و م, ن ع م
  - themes: calendar_season, habitat_ecology, light_darkness, measurement, sequence_cycle, sky_astronomy, time
  - keywords: astronomy, measure, measurement, nature, time
- `ي و م B002` — مدة من الزمان
  - activated_by_or_with: same-root only
  - themes: measurement, sequence_cycle, sky_astronomy, time
  - keywords: history, measure, time
- `ي و م B003` — كائنة اليوم وشدته
  - activated_by_or_with: same-root only
  - themes: sequence_cycle, time
  - keywords: history
- `ي و م B004` — أيام النعم والوقائع الإلهية
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ي و م B005` — يوم مضاف إلى إذ
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### د ي ن

- `د ي ن B001` — الطاعة والانقياد
  - activated_by_or_with: ع ب د
  - themes: authority_governance, religion_worship, ritual
  - keywords: authority, devotion, religion, ritual, submission
- `د ي ن B002` — الحساب والجزاء
  - activated_by_or_with: غ ي ر
  - themes: commerce_exchange, justice_judgment, measurement, punishment_sanction
  - keywords: exchange, justice, measure, punishment
- `د ي ن B003` — الدين المالي
  - activated_by_or_with: ق و م, ه د ي
  - themes: commerce_exchange, economy, finance_debt, measurement, obligation_contract, wealth_property
  - keywords: commerce, economy, exchange, measure, property
- `د ي ن B004` — الإذلال والملك
  - activated_by_or_with: ر ب ب, ع ب د
  - themes: authority_governance, control_restraint, force_power, hierarchy_status, justice_judgment, violence_warfare, wealth_property
  - keywords: authority, control, hierarchy, oppression, power, violence
- `د ي ن B005` — العادة والشأن
  - activated_by_or_with: ه د ي
  - themes: agency_action, culture_tradition, identity_personhood
  - keywords: behavior, custom, identity, practice
- `د ي ن B006` — مدينة الطاعة
  - activated_by_or_with: same-root only
  - themes: authority_governance
  - keywords: authority
- `د ي ن B007` — التصديق والتفويض
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ع ب د

- `ع ب د B001` — الرق والملك
  - activated_by_or_with: م ل ك
  - themes: hierarchy_status, labor_work, law, wealth_property
  - keywords: labor, law, property
- `ع ب د B002` — الانتساب إلى الله عبدا
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ع ب د B003` — العبادة والطاعة الخاضعة
  - activated_by_or_with: ء ل ه, د ي ن
  - themes: authority_governance, belief_revelation, religion_worship, ritual
  - keywords: authority, devotion, religion, ritual, submission, theology
- `ع ب د B004` — التعبيد والاستعباد
  - activated_by_or_with: د ي ن
  - themes: control_restraint, force_power, hierarchy_status, justice_judgment, violence_warfare
  - keywords: control, hierarchy, oppression, power, violence
- `ع ب د B005` — التذليل والتسوية
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ب د B006` — التكريم والتعظيم
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ب د B007` — القوة والصلابة
  - activated_by_or_with: غ ض ب
  - themes: animal, material, textile_clothing
  - keywords: animal, material
- `ع ب د B008` — الأنفة والغضب
  - activated_by_or_with: غ ض ب
  - themes: emotion, fear_grief, honor_shame
  - keywords: emotion, honor, mourning
- `ع ب د B009` — قلة اللبث وسرعة العدو
  - activated_by_or_with: ع ل م
  - themes: speed
  - keywords: speed
- `ع ب د B010` — التفرق في الوجوه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ب د B011` — العطب والانقطاع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ب د B012` — صَلاءة الطيب
  - activated_by_or_with: ر ب ب
  - themes: ritual, storage_vessels
  - keywords: ritual

### ع و ن

- `ع و ن B001` — الإعانة والمظاهرة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع و ن B002` — العَوان بين السنين
  - activated_by_or_with: ر ب ب, ر ح م
  - themes: growth_decay, physiology
  - keywords: biology, development
- `ع و ن B003` — الحرب العَوان
  - activated_by_or_with: ق و م
  - themes: conflict, violence_warfare
  - keywords: conflict, struggle, violence, warfare
- `ع و ن B004` — النخلة العَوانة القديمة
  - activated_by_or_with: ر ب ب
  - themes: agriculture, growth_decay, habitat_ecology, life_stage_aging, plant_vegetation
  - keywords: agriculture, botany, ecology, growth
- `ع و ن B005` — استواء الخلقة وتلاحق القوة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع و ن B006` — العانة قطيع الحمر
  - activated_by_or_with: ر ب ب, س م و
  - themes: animal, habitat_ecology, household_community, husbandry, motion, wildlife
  - keywords: collectivity, ecology, mobility, wilderness, wildlife, zoology
- `ع و ن B007` — عانة الرجل
  - activated_by_or_with: ص ر ط, ق و م
  - themes: anatomy, body, containment_access, health_medicine
  - keywords: anatomy, body, medicine
- `ع و ن B008` — النسبة إلى عانة
  - activated_by_or_with: ر ب ب
  - themes: cooking_drink, geography_landscape
  - keywords: geography

### ه د ي

- `ه د ي B001` — دلالة بلطف إلى الطريق والحق
  - activated_by_or_with: ض ل ل
  - themes: ethics_morality, navigation_route, orientation_direction, proof_uncertainty, religion_worship
  - keywords: ethics, navigation, orientation, religion, truth
- `ه د ي B002` — جهة الأمر وسيرته وقصده
  - activated_by_or_with: د ي ن
  - themes: agency_action, culture_tradition, identity_personhood
  - keywords: behavior, custom, identity, practice
- `ه د ي B003` — المتقدم الهادي وأوائل الشيء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ه د ي B004` — بعثة لطف وهدية إلى ذي مودة
  - activated_by_or_with: د ي ن
  - themes: commerce_exchange, kinship, wealth_property
  - keywords: commerce, exchange, kinship, property
- `ه د ي B005` — الهدي المهدى إلى الحرم
  - activated_by_or_with: ء ل ه
  - themes: pilgrimage_sacrifice, religion_worship, ritual
  - keywords: religion, sacrifice, sanctuary
- `ه د ي B006` — العروس المهدية إلى زوجها
  - activated_by_or_with: ر ب ب
  - themes: family, household_community, kinship
  - keywords: family, household, kinship
- `ه د ي B007` — هدي الحرمة والأسير
  - activated_by_or_with: same-root only
  - themes: religion_worship
  - keywords: sanctuary
- `ه د ي B008` — مشي التهادي مع الاعتماد والتمايل
  - activated_by_or_with: ن ع م
  - themes: body, motion, transport
  - keywords: body, locomotion, transport
- `ه د ي B009` — الهداء البليد الضعيف
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ه د ي B010` — هدي السكون وحسن الهيئة
  - activated_by_or_with: same-root only
  - themes: ethics_morality
  - keywords: ethics
- `ه د ي B011` — إهداء الشعر ومهاداته
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ص ر ط

- `ص ر ط B001` — الطريق المستقيم
  - activated_by_or_with: ق و م
  - themes: belief_revelation, ethics_morality, orientation_direction, politics_order
  - keywords: ethics, order
- `ص ر ط B002` — الغيبة في المرور والبلع
  - activated_by_or_with: ع و ن
  - themes: body, containment_access
  - keywords: body
- `ص ر ط B003` — السيف القاطع الماضي في الضربة
  - activated_by_or_with: ق و م
  - themes: force_power, violence_warfare
  - keywords: force, violence, warfare

### ق و م

- `ق و م B001` — جماعة الناس والرجال
  - activated_by_or_with: ر ح م
  - themes: household_community, identity_personhood, social_relations
  - keywords: community, identity, society
- `ق و م B002` — انتصاب وقيام بالبدن
  - activated_by_or_with: same-root only
  - themes: animal, motion, physiology
  - keywords: animal, motion
- `ق و م B003` — عزم ونهوض إلى الأمر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و م B004` — رعاية وحفظ وولاية
  - activated_by_or_with: ر ب ب
  - themes: authority_governance
  - keywords: authority, governance
- `ق و م B005` — إقامة وإدامة وتوفية حق
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ق و م B006` — مقام وإقامة في موضع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و م B007` — نيابة وقيام مقام غيره
  - activated_by_or_with: ض ل ل
  - themes: —
  - keywords: —
- `ق و م B008` — استقامة واعتدال واستواء
  - activated_by_or_with: ص ر ط
  - themes: belief_revelation, ethics_morality, orientation_direction, politics_order
  - keywords: ethics, order
- `ق و م B009` — قوام وعماد ومعاش
  - activated_by_or_with: م ل ك
  - themes: form_structure, stability_endurance, support_dependence
  - keywords: organization, stability, structure
- `ق و م B010` — قيمة وتقويم وتسعير
  - activated_by_or_with: د ي ن
  - themes: commerce_exchange, economy, measurement
  - keywords: commerce, economy, exchange
- `ق و م B011` — قامة وقوام الجسم والطول
  - activated_by_or_with: same-root only
  - themes: anatomy
  - keywords: anatomy
- `ق و م B012` — آلة قائمة وجزء قائم
  - activated_by_or_with: same-root only
  - themes: anatomy
  - keywords: anatomy
- `ق و م B013` — قيامة وبعث وقيام الساعة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و م B014` — مقاومة ومنازلة
  - activated_by_or_with: ص ر ط, ع و ن
  - themes: conflict, force_power, violence_warfare
  - keywords: conflict, force, struggle, violence, warfare
- `ق و م B015` — وزن سواء ومقدار معتدل
  - activated_by_or_with: د ي ن
  - themes: commerce_exchange, finance_debt, measurement
  - keywords: commerce
- `ق و م B016` — جمود ووقوف وكلال
  - activated_by_or_with: same-root only
  - themes: animal, motion, physiology
  - keywords: animal, motion
- `ق و م B017` — انتصاف النهار وقائم الظهيرة
  - activated_by_or_with: ي و م
  - themes: light_darkness, measurement, sky_astronomy, time
  - keywords: astronomy, measurement, time
- `ق و م B018` — نفاق السوق
  - activated_by_or_with: د ي ن
  - themes: commerce_exchange, economy, obligation_contract
  - keywords: commerce, economy, exchange
- `ق و م B019` — وجع قائم بالعضو
  - activated_by_or_with: ر ح م, ع و ن, غ ض ب
  - themes: anatomy, body, disease_injury, health_medicine, perception
  - keywords: anatomy, body, disease, medicine, pathology, symptom
- `ق و م B020` — قوام في قوائم الشاة
  - activated_by_or_with: ر ح م
  - themes: animal, disease_injury, health_medicine
  - keywords: animal, medicine, veterinary
- `ق و م B021` — عين قائمة ذاهبة البصر
  - activated_by_or_with: غ ض ب
  - themes: anatomy, disease_injury, health_medicine, perception
  - keywords: anatomy, medicine, vision

### ن ع م

- `ن ع م B001` — حسن الحال والنعمة
  - activated_by_or_with: ح م د, ر ح م
  - themes: belief_revelation, commerce_exchange, ethics_morality, hospitality_welfare, support_dependence
  - keywords: charity, ethics, gratitude, patronage, reciprocity
- `ن ع م B002` — اللين والنعومة ورفاه العيش
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن ع م B003` — مدح الشيء بنعم
  - activated_by_or_with: ح م د
  - themes: honor_shame, justice_judgment, value_quality
  - keywords: evaluation, judgment, quality
- `ن ع م B004` — الجواب بنعم والتصديق
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن ع م B005` — مال الأنعام والإبل
  - activated_by_or_with: ر ب ب, ض ل ل
  - themes: animal, husbandry, wealth_property
  - keywords: animal, pastoralism
- `ن ع م B006` — النعام والنعامة الطائر
  - activated_by_or_with: ع ل م
  - themes: animal, habitat_ecology, naming_classification, wildlife
  - keywords: taxonomy, wildlife, zoology
- `ن ع م B007` — ما سمي نعامة تشبيها بالهيئة
  - activated_by_or_with: ر ب ب
  - themes: —
  - keywords: —
- `ن ع م B008` — طيران النعامة وتفرق القوم
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن ع م B009` — النعامى ريح لينة
  - activated_by_or_with: ي و م
  - themes: calendar_season, habitat_ecology
  - keywords: nature
- `ن ع م B010` — زاد وأنعم في الفعل
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن ع م B011` — موافقة المكان وطيب المقام
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن ع م B012` — المشي على القدم وابتذالها
  - activated_by_or_with: ه د ي
  - themes: body, motion, transport
  - keywords: body, locomotion, transport
- `ن ع م B013` — نعم الله بك عينا وقرة العين
  - activated_by_or_with: ء ل ه
  - themes: prayer_supplication
  - keywords: prayer

### غ ي ر

- `غ ي ر B001` — الصلاح والمنفعة بالميرة والسقي والإصلاح
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `غ ي ر B002` — الغَيْر في الدية
  - activated_by_or_with: د ي ن
  - themes: commerce_exchange, justice_judgment, punishment_sanction
  - keywords: exchange, justice, punishment
- `غ ي ر B003` — تغيير الصورة أو إبدال الشيء بغيره
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `غ ي ر B004` — الغَيْرة على الأهل
  - activated_by_or_with: غ ض ب
  - themes: honor_shame, kinship, protection_security
  - keywords: honor, kinship, protection
- `غ ي ر B005` — السوى والخلاف والاستثناء والنفي
  - activated_by_or_with: س م و
  - themes: identity_personhood, language_speech, naming_classification, reasoning_decision
  - keywords: classification, identity, language

### غ ض ب

- `غ ض ب B001` — اشتداد السخط وثورانه للانتقام
  - activated_by_or_with: ر ب ب, ع ب د
  - themes: belief_revelation, emotion
  - keywords: emotion, theology
- `غ ض ب B002` — الغضب لشخص حي أو به بعد موته
  - activated_by_or_with: ع ب د, غ ي ر
  - themes: fear_grief, honor_shame, kinship, protection_security
  - keywords: honor, kinship, mourning, protection
- `غ ض ب B003` — المراغمة والمخالفة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `غ ض ب B004` — صلابة الصخرة وتماسكها
  - activated_by_or_with: same-root only
  - themes: material, substance_texture
  - keywords: hardness, material
- `غ ض ب B005` — غلظ الجسم وشدة الحمرة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `غ ض ب B006` — تورم العين وما حولها
  - activated_by_or_with: ق و م
  - themes: anatomy, disease_injury, health_medicine, perception
  - keywords: anatomy, disease, medicine, symptom, vision
- `غ ض ب B007` — العبوس والضجر والعظم في وصف الحيوان أو الشخص
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `غ ض ب B008` — جلد صلب أو مطوي كدرقة
  - activated_by_or_with: ع ب د
  - themes: animal, material, substance_texture, textile_clothing
  - keywords: animal, hardness, material

### ض ل ل

- `ض ل ل B001` — الضلال عن الهدى والقصد
  - activated_by_or_with: ه د ي
  - themes: ethics_morality, navigation_route, orientation_direction, proof_uncertainty, religion_worship
  - keywords: ethics, navigation, orientation, religion, truth
- `ض ل ل B002` — الغيبوبة والخفاء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ض ل ل B003` — فقدان الشيء
  - activated_by_or_with: ق و م
  - themes: —
  - keywords: —
- `ض ل ل B004` — ضياع الحفظ
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ض ل ل B005` — الضالّة في المضيعة
  - activated_by_or_with: ر ب ب, ن ع م
  - themes: animal, husbandry, livestock, terrain_desert, wealth_property
  - keywords: animal, desert, livestock, pastoralism

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
