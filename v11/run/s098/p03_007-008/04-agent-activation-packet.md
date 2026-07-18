# v11 Activation Packet — S98:7-8

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_7: إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أُو۟لَٰٓئِكَ هُمْ خَيْرُ ٱلْبَرِيَّةِ
- verse_8: جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ لِمَنْ خَشِىَ رَبَّهُۥ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ء م ن → ع م ل → ص ل ح → خ ي ر → ب ر ء → ج ز ي → ع ن د → ر ب ب → ج ن ن → ج ر ي → ت ح ت → ن ه ر → خ ل د → ء ب د → ر ض و → ء ل ه → خ ش ي

## Branch inventory summary

- ء م ن: 3 branches (3 with Qnet bridge-theme nodes; 0 Furūq-only)
- ع م ل: 12 branches (12 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص ل ح: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- خ ي ر: 6 branches (5 with Qnet bridge-theme nodes; 1 Furūq-only)
- ب ر ء: 14 branches (14 with Qnet bridge-theme nodes; 0 Furūq-only)
- ج ز ي: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- ع ن د: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- ر ب ب: 17 branches (17 with Qnet bridge-theme nodes; 0 Furūq-only)
- ج ن ن: 17 branches (16 with Qnet bridge-theme nodes; 1 Furūq-only)
- ج ر ي: 8 branches (7 with Qnet bridge-theme nodes; 1 Furūq-only)
- ت ح ت: 2 branches (2 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن ه ر: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- خ ل د: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء ب د: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- ر ض و: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء ل ه: 2 branches (2 with Qnet bridge-theme nodes; 0 Furūq-only)
- خ ش ي: 4 branches (3 with Qnet bridge-theme nodes; 1 Furūq-only)

## QAC-first root resolution audit

- ء م ن | qac_keys=ءمن | status=resolved | matches=root_000054
- ع م ل | qac_keys=عمل | status=resolved | matches=root_001046
- ص ل ح | qac_keys=صلح | status=resolved | matches=root_000876
- خ ي ر | qac_keys=خير | status=resolved | matches=root_000452
- ب ر ء | qac_keys=برء | status=merged | matches=root_000099, root_000100
- ج ز ي | qac_keys=جزي | status=resolved | matches=root_000244
- ع ن د | qac_keys=عند | status=resolved | matches=root_001052
- ر ب ب | qac_keys=ربب | status=resolved | matches=root_000532
- ج ن ن | qac_keys=جنن | status=resolved | matches=root_000266
- ج ر ي | qac_keys=جري | status=resolved | matches=root_000240
- ت ح ت | qac_keys=تحت | status=resolved | matches=root_000177
- ن ه ر | qac_keys=نهر | status=resolved | matches=root_001559
- خ ل د | qac_keys=خلد | status=resolved | matches=root_000429
- ء ب د | qac_keys=ءبد | status=resolved | matches=root_000004
- ر ض و | qac_keys=رضو | status=resolved | matches=root_000569
- ء ل ه | qac_keys=ءله | status=resolved | matches=root_000047
- خ ش ي | qac_keys=خشي | status=resolved | matches=root_000413

## Top candidate bridges

- `ج ن ن B002` ↔ `ن ه ر B002` | score_hint=27 | discovery_hint=19 | themes=light_darkness, perception, sequence_cycle, sky_astronomy, time | keywords=astronomy, cycle, time, visibility | q2=—
- `ب ر ء root_000099:B005` ↔ `ب ر ء root_000100:B005` | score_hint=30 | discovery_hint=18 | themes=body, purity_cleansing, reproduction_birth, ritual, sexuality | keywords=body, purity, reproduction, ritual, sexuality | q2=—
- `ع ن د B002` ↔ `ت ح ت B001` | score_hint=21 | discovery_hint=17 | themes=boundary, orientation_direction, social_relations, surface_shape | keywords=boundary, geometry, orientation | q2=—
- `ج ر ي B004` ↔ `ر ض و B007` | score_hint=13 | discovery_hint=17 | themes=gender, identity_personhood | keywords=gender, identity | q2=—
- `ع م ل B010` ↔ `ج ر ي B005` | score_hint=28 | discovery_hint=16 | themes=anatomy, animal, body, physiology | keywords=anatomy, animal, biology, body, zoology | q2=—
- `ب ر ء root_000099:B004` ↔ `ج ز ي B003` | score_hint=24 | discovery_hint=16 | themes=commerce_exchange, finance_debt, law, obligation_contract | keywords=commerce, finance, law, obligation | q2=—
- `ر ب ب B012` ↔ `ج ن ن B011` | score_hint=24 | discovery_hint=16 | themes=agriculture, geography_landscape, habitat_ecology, plant_vegetation | keywords=agriculture, botany, ecology, landscape | q2=—
- `ر ب ب B008` ↔ `ن ه ر B008` | score_hint=22 | discovery_hint=16 | themes=sky_astronomy, water_hydrology, weather_climate | keywords=meteorology, sky, water, weather | q2=—
- `ر ب ب B009` ↔ `ن ه ر B005` | score_hint=22 | discovery_hint=16 | themes=animal, life_stage_aging, reproduction_birth | keywords=animal, birth, infancy, reproduction | q2=—
- `ج ن ن B007` ↔ `ن ه ر B005` | score_hint=18 | discovery_hint=16 | themes=growth_decay, physiology, reproduction_birth | keywords=biology, birth, reproduction | q2=—
- `ج ز ي B005` ↔ `ر ض و B005` | score_hint=26 | discovery_hint=15 | themes=conflict, force_power, hierarchy_status | keywords=competition, conflict, dominance, hierarchy, power | q2=—
- `ع م ل B005` ↔ `ب ر ء root_000099:B004` | score_hint=24 | discovery_hint=15 | themes=commerce_exchange, law, obligation_contract, social_relations | keywords=commerce, contract, law, obligation | q2=—
- `ب ر ء root_000099:B006` ↔ `ن ه ر B002` | score_hint=24 | discovery_hint=15 | themes=calendar_season, sequence_cycle, sky_astronomy, time | keywords=astronomy, calendar, cycle, time | q2=—
- `ر ب ب B011` ↔ `ج ر ي B003` | score_hint=24 | discovery_hint=15 | themes=law, obligation_contract, politics_order, trust_loyalty | keywords=contract, diplomacy, law, trust | q2=—
- `ب ر ء root_000100:B004` ↔ `ج ز ي B003` | score_hint=22 | discovery_hint=15 | themes=finance_debt, law, obligation_contract | keywords=finance, law, liability, obligation | q2=—
- `ب ر ء root_000100:B005` ↔ `ج ن ن B007` | score_hint=18 | discovery_hint=15 | themes=body, kinship, reproduction_birth | keywords=body, kinship, reproduction | q2=—
- `ب ر ء root_000099:B005` ↔ `ج ن ن B007` | score_hint=14 | discovery_hint=15 | themes=body, physiology, reproduction_birth | keywords=body, reproduction | q2=—
- `ر ب ب B012` ↔ `خ ش ي B004` | score_hint=14 | discovery_hint=15 | themes=agriculture, food_nutrition, plant_vegetation | keywords=agriculture, food | q2=—
- `ع م ل B012` ↔ `ء ب د B006` | score_hint=7 | discovery_hint=15 | themes=migration_displacement | keywords=migration | q2=—
- `ب ر ء root_000100:B002` ↔ `ر ض و B006` | score_hint=22 | discovery_hint=14 | themes=ethics_morality, law, obligation_contract | keywords=ethics, law, liability, responsibility | q2=—
- `ر ب ب B007` ↔ `ج ر ي B001` | score_hint=22 | discovery_hint=14 | themes=animal, motion, weather_climate | keywords=animal, motion, movement, weather | q2=—
- `ج ن ن B010` ↔ `خ ل د B004` | score_hint=22 | discovery_hint=14 | themes=cognition, containment_access, emotion | keywords=cognition, emotion, interiority, psychology | q2=—
- `ع م ل B005` ↔ `ج ز ي B003` | score_hint=18 | discovery_hint=14 | themes=commerce_exchange, law, obligation_contract | keywords=commerce, law, obligation | q2=—
- `ع م ل B005` ↔ `ر ض و B003` | score_hint=18 | discovery_hint=14 | themes=commerce_exchange, obligation_contract, social_relations | keywords=contract, reciprocity, society | q2=—
- `ص ل ح B004` ↔ `ن ه ر B007` | score_hint=18 | discovery_hint=14 | themes=identity_personhood, naming_classification, writing_text | keywords=biography, identity, onomastics | q2=—
- `ب ر ء root_000099:B006` ↔ `ج ن ن B002` | score_hint=18 | discovery_hint=14 | themes=sequence_cycle, sky_astronomy, time | keywords=astronomy, cycle, time | q2=—
- `ب ر ء root_000100:B006` ↔ `ن ه ر B002` | score_hint=18 | discovery_hint=14 | themes=calendar_season, sky_astronomy, time | keywords=astronomy, calendar, time | q2=—
- `ن ه ر B007` ↔ `ر ض و B007` | score_hint=18 | discovery_hint=14 | themes=geography_landscape, identity_personhood, naming_classification | keywords=geography, identity, onomastics | q2=—
- `ع م ل B003` ↔ `ج ز ي B004` | score_hint=16 | discovery_hint=14 | themes=authority_governance, finance_debt | keywords=finance, governance, taxation | q2=—
- `ع م ل B010` ↔ `ن ه ر B005` | score_hint=16 | discovery_hint=14 | themes=animal, physiology | keywords=animal, biology, zoology | q2=—
- `ص ل ح B004` ↔ `ر ض و B007` | score_hint=16 | discovery_hint=14 | themes=identity_personhood, naming_classification | keywords=identity, nomenclature, onomastics | q2=—
- `ب ر ء root_000100:B004` ↔ `ج ز ي B002` | score_hint=16 | discovery_hint=14 | themes=finance_debt, obligation_contract | keywords=finance, liability, obligation | q2=—
- `ج ر ي B005` ↔ `ن ه ر B005` | score_hint=16 | discovery_hint=14 | themes=animal, physiology | keywords=animal, biology, zoology | q2=—
- `ر ب ب B012` ↔ `ج ن ن B003` | score_hint=16 | discovery_hint=14 | themes=agriculture, geography_landscape, habitat_ecology, plant_vegetation | keywords=agriculture, landscape | q2=—
- `ع م ل B004` ↔ `ج ر ي B006` | score_hint=14 | discovery_hint=14 | themes=economy, provision_resource, wealth_property | keywords=economy, livelihood | q2=—
- `خ ي ر B005` ↔ `ج ر ي B006` | score_hint=14 | discovery_hint=14 | themes=hospitality_welfare, support_dependence, wealth_property | keywords=charity, patronage | q2=—
- `ر ب ب B006` ↔ `خ ش ي B004` | score_hint=14 | discovery_hint=14 | themes=food_nutrition, stability_endurance, substance_texture | keywords=food, preservation | q2=—
- `ر ب ب B008` ↔ `ج ن ن B003` | score_hint=14 | discovery_hint=14 | themes=agriculture, habitat_ecology, reproduction_birth | keywords=agriculture, fertility | q2=—
- `ج ن ن B007` ↔ `ج ر ي B004` | score_hint=14 | discovery_hint=14 | themes=body, kinship, physiology | keywords=body, kinship | q2=—
- `ع م ل B010` ↔ `ج ن ن B007` | score_hint=12 | discovery_hint=14 | themes=body, physiology | keywords=biology, body | q2=—
- `ر ب ب B002` ↔ `ج ن ن B011` | score_hint=12 | discovery_hint=14 | themes=agriculture, growth_decay | keywords=agriculture, growth | q2=—
- `ر ب ب B008` ↔ `ء ب د B004` | score_hint=12 | discovery_hint=14 | themes=agriculture, reproduction_birth | keywords=agriculture, fertility | q2=—
- `ج ن ن B003` ↔ `ء ب د B004` | score_hint=12 | discovery_hint=14 | themes=agriculture, reproduction_birth | keywords=agriculture, fertility | q2=—
- `ج ن ن B007` ↔ `ج ر ي B005` | score_hint=12 | discovery_hint=14 | themes=body, physiology | keywords=biology, body | q2=—
- `ج ن ن B014` ↔ `ج ر ي B004` | score_hint=12 | discovery_hint=14 | themes=life_stage_aging, physiology | keywords=age, life | q2=—
- `ج ر ي B005` ↔ `خ ش ي B004` | score_hint=12 | discovery_hint=14 | themes=body, food_nutrition | keywords=body, food | q2=—
- `ج ن ن B011` ↔ `خ ش ي B004` | score_hint=10 | discovery_hint=14 | themes=agriculture, growth_decay, plant_vegetation | keywords=agriculture | q2=—
- `ب ر ء root_000099:B001` ↔ `ب ر ء root_000100:B001` | score_hint=33 | discovery_hint=13 | themes=belief_revelation, cognition, physiology, sky_astronomy, stability_endurance | keywords=cosmogony, cosmology, existence, life, ontology, theology | q2=—
- `ج ن ن B003` ↔ `ج ن ن B011` | score_hint=29 | discovery_hint=13 | themes=abundance_scarcity, agriculture, geography_landscape, habitat_ecology, plant_vegetation | keywords=abundance, agriculture, landscape, nature, vegetation | q2=—
- `ء م ن B003` ↔ `ء ل ه B002` | score_hint=20 | discovery_hint=13 | themes=grammar_expression, language_speech, prayer_supplication, religion_worship | keywords=formula, prayer, speech | q2=—
- `ع م ل B009` ↔ `ج ن ن B008` | score_hint=18 | discovery_hint=13 | themes=tools_equipment, violence_warfare, weaponry | keywords=combat, warfare, weapon | q2=—
- `ع م ل B011` ↔ `ر ب ب B017` | score_hint=18 | discovery_hint=13 | themes=navigation_route, transport, travel | keywords=navigation, transport, travel | q2=—
- `ص ل ح B005` ↔ `ر ض و B007` | score_hint=18 | discovery_hint=13 | themes=geography_landscape, naming_classification, place_location | keywords=geography, nomenclature, place | q2=—
- `ب ر ء root_000099:B002` ↔ `ر ض و B006` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, law, obligation_contract | keywords=ethics, law, liability | q2=—
- `ب ر ء root_000099:B007` ↔ `ن ه ر B006` | score_hint=18 | discovery_hint=13 | themes=concealment_disclosure, control_restraint, habitat_ecology | keywords=capture, predation, stealth | q2=—
- `ر ب ب B013` ↔ `ج ن ن B011` | score_hint=18 | discovery_hint=13 | themes=abundance_scarcity, geography_landscape, habitat_ecology | keywords=abundance, ecology, nature | q2=—
- `ء م ن B001` ↔ `ج ن ن B017` | score_hint=16 | discovery_hint=13 | themes=architecture_construction, protection_security | keywords=protection, refuge, shelter | q2=—
- `ع م ل B005` ↔ `ب ر ء root_000100:B004` | score_hint=16 | discovery_hint=13 | themes=law, obligation_contract | keywords=contract, law, obligation | q2=—
- `ع م ل B005` ↔ `ج ر ي B003` | score_hint=16 | discovery_hint=13 | themes=law, obligation_contract | keywords=contract, law, obligation | q2=—
- `ب ر ء root_000099:B004` ↔ `ج ر ي B003` | score_hint=16 | discovery_hint=13 | themes=law, obligation_contract | keywords=contract, law, obligation | q2=—
- `ب ر ء root_000100:B004` ↔ `ج ر ي B003` | score_hint=16 | discovery_hint=13 | themes=law, obligation_contract | keywords=contract, law, obligation | q2=—
- `ج ن ن B012` ↔ `ن ه ر B005` | score_hint=16 | discovery_hint=13 | themes=animal, wildlife | keywords=animal, wildlife, zoology | q2=—
- `ء م ن B001` ↔ `ر ب ب B011` | score_hint=14 | discovery_hint=13 | themes=obligation_contract, protection_security, trust_loyalty | keywords=protection, trust | q2=—
- `ع م ل B003` ↔ `ج ز ي B002` | score_hint=14 | discovery_hint=13 | themes=authority_governance, finance_debt, hospitality_welfare | keywords=charity, finance | q2=—
- `خ ي ر B005` ↔ `ر ب ب B016` | score_hint=14 | discovery_hint=13 | themes=ethics_morality, hospitality_welfare, support_dependence | keywords=charity, gift | q2=—
- `ب ر ء root_000099:B004` ↔ `ر ب ب B011` | score_hint=14 | discovery_hint=13 | themes=finance_debt, law, obligation_contract | keywords=contract, law | q2=—
- `ب ر ء root_000100:B004` ↔ `ر ب ب B011` | score_hint=14 | discovery_hint=13 | themes=finance_debt, law, obligation_contract | keywords=contract, law | q2=—
- `ر ب ب B009` ↔ `ء ب د B004` | score_hint=14 | discovery_hint=13 | themes=animal, livestock, reproduction_birth | keywords=livestock, reproduction | q2=—
- `ع م ل B010` ↔ `ع ن د B003` | score_hint=12 | discovery_hint=13 | themes=body, motion | keywords=body, motion | q2=—
- `ع م ل B010` ↔ `ج ن ن B016` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `خ ي ر B002` ↔ `ب ر ء root_000100:B002` | score_hint=12 | discovery_hint=13 | themes=ethics_morality, identity_personhood | keywords=ethics, identity | q2=—
- `ب ر ء root_000099:B001` ↔ `ج ن ن B014` | score_hint=12 | discovery_hint=13 | themes=physiology, sequence_cycle | keywords=life, origin | q2=—
- `ب ر ء root_000099:B003` ↔ `ج ن ن B016` | score_hint=12 | discovery_hint=13 | themes=body, health_medicine | keywords=body, medicine | q2=—
- `ب ر ء root_000099:B003` ↔ `ء ب د B005` | score_hint=12 | discovery_hint=13 | themes=body, suffering_hardship | keywords=affliction, body | q2=—
- `ب ر ء root_000099:B004` ↔ `ج ز ي B002` | score_hint=12 | discovery_hint=13 | themes=finance_debt, obligation_contract | keywords=finance, obligation | q2=—
- `ب ر ء root_000099:B004` ↔ `ج ز ي B004` | score_hint=12 | discovery_hint=13 | themes=finance_debt, law | keywords=finance, law | q2=—
- `ب ر ء root_000099:B005` ↔ `ج ن ن B009` | score_hint=12 | discovery_hint=13 | themes=body, ritual | keywords=body, ritual | q2=—
- `ب ر ء root_000099:B005` ↔ `خ ل د B003` | score_hint=12 | discovery_hint=13 | themes=body, ritual | keywords=body, ritual | q2=—
- `ب ر ء root_000100:B003` ↔ `ج ن ن B009` | score_hint=12 | discovery_hint=13 | themes=body, mortality_death | keywords=body, mortality | q2=—
- `ب ر ء root_000100:B003` ↔ `ج ن ن B016` | score_hint=12 | discovery_hint=13 | themes=body, health_medicine | keywords=body, medicine | q2=—

## Per-root candidate activations

### ء م ن

- `ء م ن B001` — سكون القلب في أمن وثقة
  - activated_by_or_with: ج ن ن, ر ب ب
  - themes: architecture_construction, obligation_contract, protection_security, trust_loyalty
  - keywords: protection, refuge, shelter, trust
- `ء م ن B002` — تصديق يطمئن إليه القلب
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ء م ن B003` — قول آمين طلبا للاستجابة
  - activated_by_or_with: ء ل ه
  - themes: grammar_expression, language_speech, prayer_supplication, religion_worship
  - keywords: formula, prayer, speech

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
  - activated_by_or_with: ج ز ي
  - themes: authority_governance, finance_debt, hospitality_welfare
  - keywords: charity, finance, governance, taxation
- `ع م ل B004` — أجر العمل ورزق العامل
  - activated_by_or_with: ج ر ي
  - themes: economy, provision_resource, wealth_property
  - keywords: economy, livelihood
- `ع م ل B005` — المعاملة بين الناس
  - activated_by_or_with: ب ر ء, ج ر ي, ج ز ي, ر ض و
  - themes: commerce_exchange, law, obligation_contract, social_relations
  - keywords: commerce, contract, law, obligation, reciprocity, society
- `ع م ل B006` — العملة العاملون بالأيدي
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع م ل B007` — التعمل بمعنى التعني
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع م ل B008` — المطبوع على العمل
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع م ل B009` — عامل الرمح
  - activated_by_or_with: ج ن ن
  - themes: tools_equipment, violence_warfare, weaponry
  - keywords: combat, warfare, weapon
- `ع م ل B010` — الجارحة العاملة
  - activated_by_or_with: ج ر ي, ج ن ن, ع ن د, ن ه ر
  - themes: anatomy, animal, body, motion, physiology
  - keywords: anatomy, animal, biology, body, motion, zoology
- `ع م ل B011` — الطريق المعمل
  - activated_by_or_with: ر ب ب
  - themes: navigation_route, transport, travel
  - keywords: navigation, transport, travel
- `ع م ل B012` — بنو العمل من المشاة
  - activated_by_or_with: ء ب د
  - themes: migration_displacement
  - keywords: migration

### ص ل ح

- `ص ل ح B001` — الصلاح ضد الفساد والطلاح
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ص ل ح B002` — الصلح إزالة النفار بين الناس
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ص ل ح B003` — الصلاح للشيء ملاءمته
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ص ل ح B004` — صالح وما قاربه علما لشخص
  - activated_by_or_with: ر ض و, ن ه ر
  - themes: identity_personhood, naming_classification, writing_text
  - keywords: biography, identity, nomenclature, onomastics
- `ص ل ح B005` — صلاح والصلح علمان لمواضع
  - activated_by_or_with: ر ض و
  - themes: geography_landscape, naming_classification, place_location
  - keywords: geography, nomenclature, place

### خ ي ر

- `خ ي ر B001` — الميل إلى الخير النافع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ ي ر B002` — فضل الصلاح والاصطفاء
  - activated_by_or_with: ب ر ء
  - themes: ethics_morality, identity_personhood
  - keywords: ethics, identity
- `خ ي ر B003` — طلب الخير بالاختيار والاستخارة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ ي ر B004` — المال المسمى خيرا
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `خ ي ر B005` — الكرم والهبة
  - activated_by_or_with: ج ر ي, ر ب ب
  - themes: ethics_morality, hospitality_welfare, support_dependence, wealth_property
  - keywords: charity, gift, patronage
- `خ ي ر B006` — استدراج الحيوان من جحره
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ب ر ء

- `ب ر ء root_000099:B001` — الخَلْق والإيجاد
  - activated_by_or_with: ج ن ن
  - themes: belief_revelation, cognition, physiology, sequence_cycle, sky_astronomy, stability_endurance
  - keywords: cosmogony, cosmology, existence, life, ontology, origin, theology
- `ب ر ء root_000099:B002` — البراءة والتباعد
  - activated_by_or_with: ر ض و
  - themes: ethics_morality, law, obligation_contract
  - keywords: ethics, law, liability
- `ب ر ء root_000099:B003` — بُرْء المرض
  - activated_by_or_with: ء ب د, ج ن ن
  - themes: body, health_medicine, suffering_hardship
  - keywords: affliction, body, medicine
- `ب ر ء root_000099:B004` — إبراء الحق والمفارقة
  - activated_by_or_with: ج ر ي, ج ز ي, ر ب ب, ع م ل
  - themes: commerce_exchange, finance_debt, law, obligation_contract, social_relations
  - keywords: commerce, contract, finance, law, obligation
- `ب ر ء root_000099:B005` — الاستبراء
  - activated_by_or_with: ج ن ن, خ ل د
  - themes: body, physiology, purity_cleansing, reproduction_birth, ritual, sexuality
  - keywords: body, purity, reproduction, ritual, sexuality
- `ب ر ء root_000099:B006` — لَيْلَة بَرَاء
  - activated_by_or_with: ج ن ن, ن ه ر
  - themes: calendar_season, sequence_cycle, sky_astronomy, time
  - keywords: astronomy, calendar, cycle, time
- `ب ر ء root_000099:B007` — بُرْأَة الصائد
  - activated_by_or_with: ن ه ر
  - themes: concealment_disclosure, control_restraint, habitat_ecology
  - keywords: capture, predation, stealth
- `ب ر ء root_000100:B001` — الخَلْق والإيجاد
  - activated_by_or_with: same-root only
  - themes: belief_revelation, cognition, physiology, sky_astronomy, stability_endurance
  - keywords: cosmogony, cosmology, existence, life, ontology, theology
- `ب ر ء root_000100:B002` — البراءة والتباعد
  - activated_by_or_with: خ ي ر, ر ض و
  - themes: ethics_morality, identity_personhood, law, obligation_contract
  - keywords: ethics, identity, law, liability, responsibility
- `ب ر ء root_000100:B003` — بُرْء المرض
  - activated_by_or_with: ج ن ن
  - themes: body, health_medicine, mortality_death
  - keywords: body, medicine, mortality
- `ب ر ء root_000100:B004` — إبراء الحق والمفارقة
  - activated_by_or_with: ج ر ي, ج ز ي, ر ب ب, ع م ل
  - themes: finance_debt, law, obligation_contract
  - keywords: contract, finance, law, liability, obligation
- `ب ر ء root_000100:B005` — الاستبراء بالحيض
  - activated_by_or_with: ج ن ن
  - themes: body, kinship, purity_cleansing, reproduction_birth, ritual, sexuality
  - keywords: body, kinship, purity, reproduction, ritual, sexuality
- `ب ر ء root_000100:B006` — لَيْلَة بَرَاء
  - activated_by_or_with: ن ه ر
  - themes: calendar_season, sky_astronomy, time
  - keywords: astronomy, calendar, time
- `ب ر ء root_000100:B007` — بُرْأَة الصائد
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ج ز ي

- `ج ز ي B001` — مقابلة الفعل بجزائه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج ز ي B002` — قيام الشيء مقام غيره
  - activated_by_or_with: ب ر ء, ع م ل
  - themes: authority_governance, finance_debt, hospitality_welfare, obligation_contract
  - keywords: charity, finance, liability, obligation
- `ج ز ي B003` — تقاضي الدين واستيفاؤه
  - activated_by_or_with: ب ر ء, ع م ل
  - themes: commerce_exchange, finance_debt, law, obligation_contract
  - keywords: commerce, finance, law, liability, obligation
- `ج ز ي B004` — الجزية قضاء مالي
  - activated_by_or_with: ب ر ء, ع م ل
  - themes: authority_governance, finance_debt, law
  - keywords: finance, governance, law, taxation
- `ج ز ي B005` — الغلبة في المجازاة
  - activated_by_or_with: ر ض و
  - themes: conflict, force_power, hierarchy_status
  - keywords: competition, conflict, dominance, hierarchy, power

### ع ن د

- `ع ن د B001` — عدول عن الاستقامة وممانعة للحق
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ن د B002` — ميل إلى ناحية وانفراد عن الجماعة
  - activated_by_or_with: ت ح ت
  - themes: boundary, orientation_direction, social_relations, surface_shape
  - keywords: boundary, geometry, orientation
- `ع ن د B003` — سيلان عاند جانح
  - activated_by_or_with: ع م ل
  - themes: body, motion
  - keywords: body, motion
- `ع ن د B004` — قرب وحضور عند الشيء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ن د B005` — انعدام البد والحيلة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ع ن د B006` — إغراء عندك بالأخذ
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ر ب ب

- `ر ب ب B001` — ربوبية وملك وسيادة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B002` — إصلاح وتربية وإتمام
  - activated_by_or_with: ج ن ن
  - themes: agriculture, growth_decay
  - keywords: agriculture, growth
- `ر ب ب B003` — علم رباني
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B004` — ربة وجماعات كثيرة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B005` — ربيب وربيبة ورابة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B006` — رُبّ خاثر وإصلاح به
  - activated_by_or_with: خ ش ي
  - themes: food_nutrition, stability_endurance, substance_texture
  - keywords: food, preservation
- `ر ب ب B007` — لزوم وإقامة ودوام
  - activated_by_or_with: ج ر ي
  - themes: animal, motion, weather_climate
  - keywords: animal, motion, movement, weather
- `ر ب ب B008` — رباب السحاب
  - activated_by_or_with: ء ب د, ج ن ن, ن ه ر
  - themes: agriculture, habitat_ecology, reproduction_birth, sky_astronomy, water_hydrology, weather_climate
  - keywords: agriculture, fertility, meteorology, sky, water, weather
- `ر ب ب B009` — شاة رُبّى وحداثة
  - activated_by_or_with: ء ب د, ن ه ر
  - themes: animal, life_stage_aging, livestock, reproduction_birth
  - keywords: animal, birth, infancy, livestock, reproduction
- `ر ب ب B010` — ربابة تجمع القداح
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B011` — ربابة عهد وميثاق
  - activated_by_or_with: ء م ن, ب ر ء, ج ر ي
  - themes: finance_debt, law, obligation_contract, politics_order, protection_security, trust_loyalty
  - keywords: contract, diplomacy, law, protection, trust
- `ر ب ب B012` — ربة نبات
  - activated_by_or_with: ج ن ن, خ ش ي
  - themes: agriculture, food_nutrition, geography_landscape, habitat_ecology, plant_vegetation
  - keywords: agriculture, botany, ecology, food, landscape
- `ر ب ب B013` — ماء رَبَب كثير
  - activated_by_or_with: ج ن ن
  - themes: abundance_scarcity, geography_landscape, habitat_ecology
  - keywords: abundance, ecology, nature
- `ر ب ب B014` — رَبْرَب قطيع
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B015` — حرف رب وربما
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ب ب B016` — رُبَى حاجة وعقدة ونعمة
  - activated_by_or_with: خ ي ر
  - themes: ethics_morality, hospitality_welfare, support_dependence
  - keywords: charity, gift
- `ر ب ب B017` — رباني الملاحين
  - activated_by_or_with: ع م ل
  - themes: navigation_route, transport, travel
  - keywords: navigation, transport, travel

### ج ن ن

- `ج ن ن B001` — الستر والاستتار
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج ن ن B002` — غشيان الليل
  - activated_by_or_with: ب ر ء, ن ه ر
  - themes: light_darkness, perception, sequence_cycle, sky_astronomy, time
  - keywords: astronomy, cycle, time, visibility
- `ج ن ن B003` — البستان المستور بالشجر
  - activated_by_or_with: ء ب د, ر ب ب
  - themes: abundance_scarcity, agriculture, geography_landscape, habitat_ecology, plant_vegetation, reproduction_birth
  - keywords: abundance, agriculture, fertility, landscape, nature, vegetation
- `ج ن ن B004` — الجنة الأخروية
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ج ن ن B005` — الجن المستترون
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج ن ن B006` — ستر العقل بالجنون
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج ن ن B007` — الجنين المستور في البطن
  - activated_by_or_with: ب ر ء, ج ر ي, ع م ل, ن ه ر
  - themes: body, growth_decay, kinship, physiology, reproduction_birth
  - keywords: biology, birth, body, kinship, reproduction
- `ج ن ن B008` — الجُنّة الواقية
  - activated_by_or_with: ع م ل
  - themes: tools_equipment, violence_warfare, weaponry
  - keywords: combat, warfare, weapon
- `ج ن ن B009` — مواراة الميت
  - activated_by_or_with: ب ر ء
  - themes: body, mortality_death, ritual
  - keywords: body, mortality, ritual
- `ج ن ن B010` — الجنان المستور في الصدر
  - activated_by_or_with: خ ل د
  - themes: cognition, containment_access, emotion
  - keywords: cognition, emotion, interiority, psychology
- `ج ن ن B011` — التفاف النبات واندفاعه
  - activated_by_or_with: خ ش ي, ر ب ب
  - themes: abundance_scarcity, agriculture, geography_landscape, growth_decay, habitat_ecology, plant_vegetation
  - keywords: abundance, agriculture, botany, ecology, growth, landscape, nature, vegetation
- `ج ن ن B012` — الجان حية
  - activated_by_or_with: ن ه ر
  - themes: animal, wildlife
  - keywords: animal, wildlife, zoology
- `ج ن ن B013` — سواد الناس وجماعتهم
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج ن ن B014` — جن الشيء في بدايته
  - activated_by_or_with: ب ر ء, ج ر ي
  - themes: life_stage_aging, physiology, sequence_cycle
  - keywords: age, life, origin
- `ج ن ن B015` — جن الذباب وصوت الخازباز
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج ن ن B016` — الجناجن عظام الصدر
  - activated_by_or_with: ب ر ء, ع م ل
  - themes: anatomy, body, health_medicine
  - keywords: anatomy, body, medicine
- `ج ن ن B017` — المَجَنَّة موضع الاستتار
  - activated_by_or_with: ء م ن
  - themes: architecture_construction, protection_security
  - keywords: protection, refuge, shelter

### ج ر ي

- `ج ر ي B001` — جريان الشيء وانسياحه
  - activated_by_or_with: ر ب ب
  - themes: animal, motion, weather_climate
  - keywords: animal, motion, movement, weather
- `ج ر ي B002` — العادة والطريقة الجارية
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج ر ي B003` — الجري الوكيل والرسول
  - activated_by_or_with: ب ر ء, ر ب ب, ع م ل
  - themes: law, obligation_contract, politics_order, trust_loyalty
  - keywords: contract, diplomacy, law, obligation, trust
- `ج ر ي B004` — الجارية من النساء وصباها
  - activated_by_or_with: ج ن ن, ر ض و
  - themes: body, gender, identity_personhood, kinship, life_stage_aging, physiology
  - keywords: age, body, gender, identity, kinship, life
- `ج ر ي B005` — الجُرْية الحوصلة
  - activated_by_or_with: ج ن ن, خ ش ي, ع م ل, ن ه ر
  - themes: anatomy, animal, body, food_nutrition, physiology
  - keywords: anatomy, animal, biology, body, food, zoology
- `ج ر ي B006` — دوام الرزق والعطاء
  - activated_by_or_with: خ ي ر, ع م ل
  - themes: economy, hospitality_welfare, provision_resource, support_dependence, wealth_property
  - keywords: charity, economy, livelihood, patronage
- `ج ر ي B007` — مجاراة الشيء والجري معه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ج ر ي B008` — من جرائك أي من أجلك
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### ت ح ت

- `ت ح ت B001` — تحت الشيء
  - activated_by_or_with: ع ن د
  - themes: boundary, orientation_direction, social_relations, surface_shape
  - keywords: boundary, geometry, orientation
- `ت ح ت B002` — التَّحوت من الناس
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ن ه ر

- `ن ه ر B001` — نهر يشق الأرض بماء جار
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن ه ر B002` — انفتاح النهار بالضياء
  - activated_by_or_with: ب ر ء, ج ن ن
  - themes: calendar_season, light_darkness, perception, sequence_cycle, sky_astronomy, time
  - keywords: astronomy, calendar, cycle, time, visibility
- `ن ه ر B003` — فتح الشيء وتوسيعه حتى يسيل أو ينفسح
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن ه ر B004` — زجر بكلام مغلظ
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ن ه ر B005` — النَّهار فرخ طير
  - activated_by_or_with: ج ر ي, ج ن ن, ر ب ب, ع م ل
  - themes: animal, growth_decay, life_stage_aging, physiology, reproduction_birth, wildlife
  - keywords: animal, biology, birth, infancy, reproduction, wildlife, zoology
- `ن ه ر B006` — الدغرة والخلسة
  - activated_by_or_with: ب ر ء
  - themes: concealment_disclosure, control_restraint, habitat_ecology
  - keywords: capture, predation, stealth
- `ن ه ر B007` — أعلام وأسماء خاصة
  - activated_by_or_with: ر ض و, ص ل ح
  - themes: geography_landscape, identity_personhood, naming_classification, writing_text
  - keywords: biography, geography, identity, onomastics
- `ن ه ر B008` — النَّاهُور سحاب
  - activated_by_or_with: ر ب ب
  - themes: sky_astronomy, water_hydrology, weather_climate
  - keywords: meteorology, sky, water, weather

### خ ل د

- `خ ل د B001` — ثبات وبقاء لا يسرع إليه الفناء
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ ل د B002` — ركون ولصوق وملازمة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ ل د B003` — زينة ملازمة للأذن أو اليد
  - activated_by_or_with: ب ر ء
  - themes: body, ritual
  - keywords: body, ritual
- `خ ل د B004` — بال مستقر في القلب
  - activated_by_or_with: ج ن ن
  - themes: cognition, containment_access, emotion
  - keywords: cognition, emotion, interiority, psychology
- `خ ل د B005` — دويبة عمياء تشبه الجرذ
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ء ب د

- `ء ب د B001` — طول المدة والدوام
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ء ب د B002` — التوحش والنفور
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ء ب د B003` — خلو المنزل وإقفاره
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ء ب د B004` — الإبد الولود
  - activated_by_or_with: ج ن ن, ر ب ب
  - themes: agriculture, animal, livestock, reproduction_birth
  - keywords: agriculture, fertility, livestock, reproduction
- `ء ب د B005` — تأبد الوجه وتغيره
  - activated_by_or_with: ب ر ء
  - themes: body, suffering_hardship
  - keywords: affliction, body
- `ء ب د B006` — الإقامة وعدم البراح
  - activated_by_or_with: ع م ل
  - themes: migration_displacement
  - keywords: migration
- `ء ب د B007` — الآبدة الباقية الذكر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ء ب د B008` — الكلمة الوحشية والشاردة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ء ب د B009` — الغضب والغضب عليه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ر ض و

- `ر ض و B001` — الرضا خلاف السخط
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ض و B002` — الرضوان والمرضاة اسم للرضا الكثير أو المطلوب
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ض و B003` — المراضاة والتراضي رضا متبادل
  - activated_by_or_with: ع م ل
  - themes: commerce_exchange, obligation_contract, social_relations
  - keywords: contract, reciprocity, society
- `ر ض و B004` — الإرضاء طلب رضا الغير وإزالة سخطه
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ر ض و B005` — راضاني فرضوته غلبة في ذلك
  - activated_by_or_with: ج ز ي
  - themes: conflict, force_power, hierarchy_status
  - keywords: competition, conflict, dominance, hierarchy, power
- `ر ض و B006` — الرضي صفة للمطيع أو المحب أو الضامن
  - activated_by_or_with: ب ر ء
  - themes: ethics_morality, law, obligation_contract
  - keywords: ethics, law, liability, responsibility
- `ر ض و B007` — رضوى ورضيا أعلام من المادة
  - activated_by_or_with: ج ر ي, ص ل ح, ن ه ر
  - themes: gender, geography_landscape, identity_personhood, naming_classification, place_location
  - keywords: gender, geography, identity, nomenclature, onomastics, place

### ء ل ه

- `ء ل ه B001` — التعبد والمعبود
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ء ل ه B002` — اسم الله في القسم والنداء
  - activated_by_or_with: ء م ن
  - themes: grammar_expression, language_speech, prayer_supplication, religion_worship
  - keywords: formula, prayer, speech

### خ ش ي

- `خ ش ي B001` — الخوف والخشية مع الهيبة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ ش ي B002` — العلم على سبيل المجاز
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `خ ش ي B003` — الكراهة في إسناد الخشية
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `خ ش ي B004` — الحشف واليبس
  - activated_by_or_with: ج ر ي, ج ن ن, ر ب ب
  - themes: agriculture, body, food_nutrition, growth_decay, plant_vegetation, stability_endurance, substance_texture
  - keywords: agriculture, body, food, preservation

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
