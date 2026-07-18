# v11 Activation Packet — S96:17-19

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_17: فَلْيَدْعُ نَادِيَهُۥ
- verse_18: سَنَدْعُ ٱلزَّبَانِيَةَ
- verse_19: كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩

Full copied source text is available in `00-surah-text.json`.

## Surface roots

د ع و → ن د و → ز ب ن → ط و ع → س ج د → ق ر ب

## Branch inventory summary

- د ع و: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن د و: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- ز ب ن: 8 branches (6 with Qnet bridge-theme nodes; 2 Furūq-only)
- ط و ع: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- س ج د: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- ق ر ب: 16 branches (15 with Qnet bridge-theme nodes; 1 Furūq-only)

## QAC-first root resolution audit

- د ع و | qac_keys=دعو | status=resolved | matches=root_000478
- ن د و | qac_keys=ندو | status=resolved | matches=root_001486
- ز ب ن | qac_keys=زبن | status=resolved | matches=root_000622
- ط و ع | qac_keys=طوع | status=resolved | matches=root_000956
- س ج د | qac_keys=سجد | status=resolved | matches=root_000675
- ق ر ب | qac_keys=قرب | status=resolved | matches=root_001212

## Top candidate bridges

- `ن د و B009` ↔ `ز ب ن B005` | score_hint=28 | discovery_hint=19 | themes=boundary, geography_landscape, migration_displacement, social_relations, space | keywords=exclusion, geography, isolation, space | q2=—
- `ن د و B006` ↔ `ق ر ب B008` | score_hint=26 | discovery_hint=14 | themes=animal, husbandry, livestock, travel, water_hydrology | keywords=animal, livestock, travel, water | q2=—
- `س ج د B003` ↔ `ق ر ب B015` | score_hint=24 | discovery_hint=15 | themes=anatomy, body, communication, posture_embodiment | keywords=anatomy, body, embodiment, gesture | q2=—
- `د ع و B008` ↔ `ز ب ن B007` | score_hint=21 | discovery_hint=17 | themes=household_community, loss_absence, place_location, social_relations | keywords=absence, habitation, solitude | q2=—
- `ن د و B003` ↔ `ط و ع B007` | score_hint=19 | discovery_hint=19 | themes=agriculture, habitat_ecology, reproduction_birth | keywords=agriculture, ecology, fertility | q2=—
- `د ع و B008` ↔ `ز ب ن B005` | score_hint=18 | discovery_hint=13 | themes=place_location, social_relations, space | keywords=isolation, residence, space | q2=—
- `ن د و B006` ↔ `ق ر ب B013` | score_hint=18 | discovery_hint=13 | themes=animal, husbandry, transport | keywords=animal, equestrian, husbandry | q2=—
- `ز ب ن B008` ↔ `ق ر ب B015` | score_hint=18 | discovery_hint=14 | themes=anatomy, body, perception | keywords=anatomy, body, touch | q2=—
- `ن د و B004` ↔ `ط و ع B005` | score_hint=16 | discovery_hint=13 | themes=ethics_morality, hospitality_welfare | keywords=altruism, charity, welfare | q2=—
- `ط و ع B001` ↔ `ق ر ب B004` | score_hint=16 | discovery_hint=12 | themes=authority_governance, hierarchy_status | keywords=authority, governance, hierarchy | q2=—
- `س ج د B001` ↔ `ق ر ب B005` | score_hint=16 | discovery_hint=12 | themes=religion_worship, ritual | keywords=devotion, ritual, worship | q2=—
- `د ع و B002` ↔ `ن د و B007` | score_hint=15 | discovery_hint=17 | themes=kinship, marriage_genealogy, wealth_property | keywords=genealogy, kinship | q2=—
- `ن د و B006` ↔ `ق ر ب B011` | score_hint=14 | discovery_hint=12 | themes=transport, travel, water_hydrology | keywords=travel, water | q2=—
- `ن د و B007` ↔ `ق ر ب B008` | score_hint=14 | discovery_hint=12 | themes=animal, husbandry, livestock | keywords=animal, livestock | q2=—
- `ن د و B007` ↔ `ق ر ب B013` | score_hint=14 | discovery_hint=12 | themes=animal, hierarchy_status, husbandry | keywords=animal, status | q2=—
- `س ج د B004` ↔ `ق ر ب B015` | score_hint=14 | discovery_hint=12 | themes=communication, orientation_direction, posture_embodiment | keywords=gesture, orientation | q2=—
- `د ع و B002` ↔ `س ج د B007` | score_hint=13 | discovery_hint=17 | themes=identity_personhood, law | keywords=identity, law | q2=—
- `ن د و B006` ↔ `ط و ع B007` | score_hint=13 | discovery_hint=16 | themes=livestock, pasture_forage | keywords=forage, livestock | q2=—
- `س ج د B007` ↔ `ق ر ب B003` | score_hint=13 | discovery_hint=16 | themes=household_community, obligation_contract | keywords=community, obligation | q2=—
- `د ع و B003` ↔ `ن د و B003` | score_hint=12 | discovery_hint=14 | themes=agriculture, food_nutrition | keywords=agriculture, nourishment | q2=—
- `د ع و B003` ↔ `ز ب ن B006` | score_hint=12 | discovery_hint=14 | themes=food_nutrition, provision_resource | keywords=nourishment, resource | q2=—
- `د ع و B008` ↔ `ن د و B009` | score_hint=12 | discovery_hint=12 | themes=social_relations, space | keywords=isolation, space | q2=—
- `ن د و B001` ↔ `س ج د B002` | score_hint=12 | discovery_hint=11 | themes=authority_governance, household_community | keywords=community, institution | q2=—
- `ن د و B001` ↔ `س ج د B007` | score_hint=12 | discovery_hint=11 | themes=authority_governance, household_community | keywords=community, governance | q2=—
- `ن د و B001` ↔ `ق ر ب B003` | score_hint=12 | discovery_hint=11 | themes=household_community, social_relations | keywords=community, society | q2=—
- `ن د و B006` ↔ `ق ر ب B014` | score_hint=12 | discovery_hint=12 | themes=animal, knowledge_learning | keywords=animal, training | q2=—
- `ن د و B007` ↔ `ق ر ب B003` | score_hint=12 | discovery_hint=13 | themes=marriage_genealogy, wealth_property | keywords=genealogy, inheritance | q2=—
- `ز ب ن B004` ↔ `ق ر ب B015` | score_hint=12 | discovery_hint=12 | themes=anatomy, animal | keywords=anatomy, animal | q2=—
- `ز ب ن B008` ↔ `س ج د B003` | score_hint=12 | discovery_hint=13 | themes=anatomy, body | keywords=anatomy, body | q2=—
- `ط و ع B005` ↔ `ق ر ب B013` | score_hint=12 | discovery_hint=12 | themes=labor_work, violence_warfare | keywords=service, warfare | q2=—
- `س ج د B002` ↔ `ق ر ب B005` | score_hint=12 | discovery_hint=12 | themes=religion_worship, ritual | keywords=ritual, worship | q2=—
- `د ع و B001` ↔ `ن د و B001` | score_hint=10 | discovery_hint=9 | themes=communication, household_community, social_relations | keywords=communication | q2=—
- `د ع و B006` ↔ `ط و ع B004` | score_hint=10 | discovery_hint=11 | themes=agency_action, change_transition, suffering_hardship | keywords=agency | q2=—
- `د ع و B008` ↔ `ق ر ب B001` | score_hint=10 | discovery_hint=10 | themes=place_location, social_relations, space | keywords=space | q2=—
- `ن د و B009` ↔ `ق ر ب B001` | score_hint=10 | discovery_hint=10 | themes=motion, social_relations, space | keywords=space | q2=—
- `ز ب ن B005` ↔ `ق ر ب B001` | score_hint=10 | discovery_hint=10 | themes=place_location, social_relations, space | keywords=space | q2=—
- `د ع و B007` ↔ `ن د و B008` | score_hint=9 | discovery_hint=15 | themes=cognition, proof_uncertainty | keywords=cognition | q2=—
- `ن د و B002` ↔ `س ج د B005` | score_hint=9 | discovery_hint=15 | themes=memory_attention, perception | keywords=attention | q2=—
- `ن د و B006` ↔ `ز ب ن B004` | score_hint=9 | discovery_hint=15 | themes=animal, navigation_route | keywords=animal | q2=—
- `ز ب ن B001` ↔ `ق ر ب B010` | score_hint=9 | discovery_hint=15 | themes=protection_security, violence_warfare | keywords=protection | q2=—
- `ط و ع B007` ↔ `ق ر ب B002` | score_hint=9 | discovery_hint=15 | themes=calendar_season, harvest_cultivation | keywords=harvest | q2=—
- `د ع و B001` ↔ `ن د و B008` | score_hint=8 | discovery_hint=10 | themes=communication, rhetoric_discourse | keywords=communication | q2=—
- `د ع و B001` ↔ `س ج د B004` | score_hint=8 | discovery_hint=10 | themes=communication, orientation_direction | keywords=orientation | q2=—
- `د ع و B001` ↔ `ق ر ب B015` | score_hint=8 | discovery_hint=10 | themes=communication, orientation_direction | keywords=orientation | q2=—
- `د ع و B002` ↔ `ق ر ب B003` | score_hint=8 | discovery_hint=12 | themes=marriage_genealogy, wealth_property | keywords=genealogy | q2=—
- `د ع و B003` ↔ `ط و ع B007` | score_hint=8 | discovery_hint=13 | themes=agriculture, provision_resource | keywords=agriculture | q2=—
- `د ع و B003` ↔ `ق ر ب B008` | score_hint=8 | discovery_hint=12 | themes=husbandry, provision_resource | keywords=resource | q2=—
- `د ع و B003` ↔ `ق ر ب B013` | score_hint=8 | discovery_hint=11 | themes=husbandry, labor_work | keywords=husbandry | q2=—
- `د ع و B004` ↔ `ن د و B005` | score_hint=8 | discovery_hint=11 | themes=ethics_morality, language_speech | keywords=morality | q2=—
- `د ع و B004` ↔ `ط و ع B001` | score_hint=8 | discovery_hint=10 | themes=agency_action, language_speech | keywords=language | q2=—
- `د ع و B004` ↔ `ط و ع B005` | score_hint=8 | discovery_hint=11 | themes=ethics_morality, religion_worship | keywords=religion | q2=—
- `د ع و B004` ↔ `ط و ع B006` | score_hint=8 | discovery_hint=11 | themes=agency_action, ethics_morality | keywords=morality | q2=—
- `د ع و B008` ↔ `س ج د B002` | score_hint=8 | discovery_hint=11 | themes=household_community, space | keywords=space | q2=—
- `ن د و B002` ↔ `س ج د B001` | score_hint=8 | discovery_hint=10 | themes=communication, ritual | keywords=ritual | q2=—
- `ن د و B002` ↔ `س ج د B003` | score_hint=8 | discovery_hint=11 | themes=communication, ritual | keywords=ritual | q2=—
- `ن د و B006` ↔ `ق ر ب B009` | score_hint=8 | discovery_hint=11 | themes=transport, water_hydrology | keywords=water | q2=—
- `ن د و B009` ↔ `ز ب ن B001` | score_hint=8 | discovery_hint=10 | themes=boundary, motion | keywords=boundary | q2=—
- `ن د و B009` ↔ `ق ر ب B007` | score_hint=8 | discovery_hint=11 | themes=boundary, social_relations | keywords=boundary | q2=—
- `ز ب ن B001` ↔ `س ج د B004` | score_hint=8 | discovery_hint=11 | themes=force_power, motion | keywords=motion | q2=—
- `ط و ع B001` ↔ `س ج د B001` | score_hint=8 | discovery_hint=9 | themes=authority_governance, hierarchy_status | keywords=hierarchy | q2=—
- `ط و ع B005` ↔ `س ج د B002` | score_hint=8 | discovery_hint=11 | themes=household_community, religion_worship | keywords=community | q2=—
- `ط و ع B007` ↔ `ق ر ب B008` | score_hint=8 | discovery_hint=12 | themes=livestock, provision_resource | keywords=livestock | q2=—
- `س ج د B001` ↔ `ق ر ب B004` | score_hint=8 | discovery_hint=10 | themes=authority_governance, hierarchy_status | keywords=hierarchy | q2=—
- `س ج د B001` ↔ `ق ر ب B015` | score_hint=8 | discovery_hint=10 | themes=communication, posture_embodiment | keywords=gesture | q2=—
- `س ج د B003` ↔ `ق ر ب B001` | score_hint=8 | discovery_hint=10 | themes=posture_embodiment, social_relations | keywords=embodiment | q2=—
- `س ج د B003` ↔ `ق ر ب B005` | score_hint=8 | discovery_hint=11 | themes=ritual, social_relations | keywords=ritual | q2=—
- `س ج د B004` ↔ `ق ر ب B001` | score_hint=8 | discovery_hint=10 | themes=motion, posture_embodiment | keywords=motion | q2=—
- `د ع و B005` ↔ `س ج د B002` | score_hint=7 | discovery_hint=15 | themes=architecture_construction | keywords=architecture | q2=—
- `ز ب ن B008` ↔ `ط و ع B001` | score_hint=7 | discovery_hint=14 | themes=control_restraint | keywords=control | q2=—
- `ط و ع B003` ↔ `ق ر ب B001` | score_hint=7 | discovery_hint=14 | themes=containment_access | keywords=access | q2=—
- `د ع و B001` ↔ `ن د و B002` | score_hint=6 | discovery_hint=10 | themes=communication | keywords=communication | q2=—
- `د ع و B001` ↔ `ز ب ن B005` | score_hint=6 | discovery_hint=10 | themes=social_relations | keywords=sociality | q2=—
- `د ع و B001` ↔ `ط و ع B001` | score_hint=6 | discovery_hint=9 | themes=language_speech | keywords=language | q2=—
- `د ع و B001` ↔ `ط و ع B006` | score_hint=6 | discovery_hint=10 | themes=intention_character | keywords=intention | q2=—
- `د ع و B001` ↔ `س ج د B002` | score_hint=6 | discovery_hint=10 | themes=household_community | keywords=gathering | q2=—
- `د ع و B002` ↔ `ز ب ن B001` | score_hint=6 | discovery_hint=10 | themes=conflict | keywords=conflict | q2=—
- `د ع و B002` ↔ `ق ر ب B007` | score_hint=6 | discovery_hint=11 | themes=law | keywords=law | q2=—
- `د ع و B003` ↔ `ن د و B006` | score_hint=6 | discovery_hint=11 | themes=husbandry | keywords=husbandry | q2=—
- `د ع و B004` ↔ `ط و ع B003` | score_hint=6 | discovery_hint=11 | themes=agency_action | keywords=causation | q2=—
- `د ع و B004` ↔ `ق ر ب B005` | score_hint=6 | discovery_hint=11 | themes=religion_worship | keywords=religion | q2=—

## Per-root candidate activations

### د ع و

- `د ع و B001` — النداء والإمالة بالكلام
  - activated_by_or_with: ز ب ن, س ج د, ط و ع, ق ر ب, ن د و
  - themes: communication, hospitality_welfare, household_community, intention_character, language_speech, orientation_direction, rhetoric_discourse, social_relations
  - keywords: communication, gathering, intention, language, orientation, sociality
- `د ع و B002` — ادعاء الحق والانتساب
  - activated_by_or_with: ز ب ن, س ج د, ط و ع, ق ر ب, ن د و
  - themes: conflict, identity_personhood, kinship, law, marriage_genealogy, wealth_property
  - keywords: conflict, genealogy, identity, kinship, law
- `د ع و B003` — داعية اللبن
  - activated_by_or_with: ز ب ن, ط و ع, ق ر ب, ن د و
  - themes: agriculture, food_nutrition, husbandry, labor_work, provision_resource
  - keywords: agriculture, husbandry, nourishment, resource
- `د ع و B004` — الدعاء بالمكروه النازل
  - activated_by_or_with: ز ب ن, س ج د, ط و ع, ق ر ب, ن د و
  - themes: agency_action, conflict, ethics_morality, language_speech, religion_worship, suffering_hardship
  - keywords: adversity, causation, language, morality, religion
- `د ع و B005` — التداعي بالسقوط
  - activated_by_or_with: ز ب ن, س ج د, ط و ع, ق ر ب, ن د و
  - themes: architecture_construction, capacity_ability, danger_harm, growth_decay, material, motion, politics_order, reasoning_decision, stability_endurance
  - keywords: architecture, motion
- `د ع و B006` — دواعي الدهر
  - activated_by_or_with: ز ب ن, س ج د, ط و ع, ق ر ب, ن د و
  - themes: agency_action, change_transition, perception, suffering_hardship, time
  - keywords: adversity, agency
- `د ع و B007` — الأُدْعِيّة المعماة
  - activated_by_or_with: ط و ع, ق ر ب, ن د و
  - themes: cognition, language_speech, proof_uncertainty, reasoning_decision, recreation_sport
  - keywords: cognition, language
- `د ع و B008` — خلو الدار من داع
  - activated_by_or_with: ز ب ن, س ج د, ط و ع, ق ر ب, ن د و
  - themes: household_community, loss_absence, place_location, social_relations, space
  - keywords: absence, domesticity, habitation, isolation, residence, solitude, space

### ن د و

- `ن د و B001` — اجتماع القوم في النادي والندوة
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ق ر ب
  - themes: authority_governance, communication, household_community, reasoning_decision, social_relations
  - keywords: communication, community, governance, institution, society
- `ن د و B002` — الصوت المرفوع والنداء
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ق ر ب
  - themes: communication, memory_attention, perception, ritual
  - keywords: attention, communication, ritual
- `ن د و B003` — بلل الندى والمطر
  - activated_by_or_with: د ع و, ز ب ن, ط و ع, ق ر ب
  - themes: agriculture, food_nutrition, habitat_ecology, reproduction_birth, water_hydrology
  - keywords: agriculture, ecology, fertility, nourishment, water
- `ن د و B004` — ندى الجود والسخاء
  - activated_by_or_with: د ع و, س ج د, ط و ع, ق ر ب
  - themes: commerce_exchange, ethics_morality, hospitality_welfare, support_dependence, value_quality, wealth_property
  - keywords: altruism, charity, ethics, welfare
- `ن د و B005` — ابتلال بالمكروه وخزي الكلام
  - activated_by_or_with: د ع و, س ج د, ط و ع, ق ر ب
  - themes: ethics_morality, language_speech
  - keywords: morality, speech, transgression
- `ن د و B006` — تندية الإبل والخيل بين الماء والمرعى
  - activated_by_or_with: د ع و, ز ب ن, ط و ع, ق ر ب
  - themes: animal, husbandry, knowledge_learning, livestock, navigation_route, pasture_forage, transport, travel, water_hydrology
  - keywords: animal, equestrian, forage, husbandry, livestock, training, travel, water
- `ن د و B007` — تنزع الناقة في النسب إلى أصل كريم
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ق ر ب
  - themes: animal, hierarchy_status, husbandry, kinship, livestock, marriage_genealogy, wealth_property
  - keywords: animal, genealogy, inheritance, kinship, livestock, status
- `ن د و B008` — ظهور الشيء كأنه ينادي
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ق ر ب
  - themes: cognition, communication, knowledge_learning, perception, proof_uncertainty, rhetoric_discourse
  - keywords: cognition, communication, perception
- `ن د و B009` — نواح متفرقة وتنح عن المركز
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ق ر ب
  - themes: boundary, geography_landscape, language_speech, migration_displacement, motion, social_relations, space, stability_endurance
  - keywords: boundary, exclusion, geography, isolation, space, speech, survival

### ز ب ن

- `ز ب ن B001` — الدفع والصدم والمنع
  - activated_by_or_with: د ع و, س ج د, ط و ع, ق ر ب, ن د و
  - themes: boundary, conflict, force_power, motion, protection_security, violence_warfare
  - keywords: boundary, conflict, motion, protection, violence
- `ز ب ن B002` — الزبانية الدافعون إلى العذاب
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ز ب ن B003` — بيع المزابنة
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ز ب ن B004` — زبانيا العقرب
  - activated_by_or_with: س ج د, ط و ع, ق ر ب, ن د و
  - themes: anatomy, animal, calendar_season, navigation_route
  - keywords: anatomy, animal
- `ز ب ن B005` — البعد عن البيوت
  - activated_by_or_with: د ع و, س ج د, ط و ع, ق ر ب, ن د و
  - themes: boundary, geography_landscape, migration_displacement, place_location, social_relations, space
  - keywords: exclusion, geography, isolation, residence, sociality, space
- `ز ب ن B006` — الحاجة من الطعام
  - activated_by_or_with: د ع و, س ج د, ط و ع, ق ر ب, ن د و
  - themes: abundance_scarcity, economy, food_nutrition, provision_resource, stability_endurance
  - keywords: economy, nourishment, resource, subsistence, survival
- `ز ب ن B007` — ما بها زبين
  - activated_by_or_with: د ع و, س ج د, ط و ع, ق ر ب, ن د و
  - themes: grammar_expression, household_community, loss_absence, place_location, quantity_number, social_relations
  - keywords: absence, habitation, solitude
- `ز ب ن B008` — الزبونة للعنق
  - activated_by_or_with: د ع و, س ج د, ط و ع, ق ر ب, ن د و
  - themes: anatomy, body, control_restraint, perception, violence_warfare
  - keywords: anatomy, body, control, touch, violence

### ط و ع

- `ط و ع B001` — الانقياد والطاعة
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ق ر ب, ن د و
  - themes: agency_action, authority_governance, control_restraint, hierarchy_status, language_speech
  - keywords: agency, authority, control, governance, hierarchy, language
- `ط و ع B002` — الموافقة والمطاوعة
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ق ر ب, ن د و
  - themes: agency_action, orientation_direction, rhetoric_discourse, social_relations, trust_loyalty
  - keywords: coordination, relation
- `ط و ع B003` — الاستطاعة والإطاقة
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ق ر ب
  - themes: agency_action, capacity_ability, containment_access, grammar_expression
  - keywords: access, agency, causation
- `ط و ع B004` — تكلف الاستطاعة
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ق ر ب, ن د و
  - themes: agency_action, change_transition, conflict, intention_character, labor_work, stability_endurance, suffering_hardship
  - keywords: agency, volition
- `ط و ع B005` — التطوع والتبرع
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ق ر ب, ن د و
  - themes: ethics_morality, hospitality_welfare, household_community, labor_work, religion_worship, violence_warfare
  - keywords: altruism, charity, community, religion, service, warfare, welfare
- `ط و ع B006` — تسهيل النفس للأمر
  - activated_by_or_with: د ع و, س ج د, ق ر ب, ن د و
  - themes: agency_action, cognition, ethics_morality, intention_character, support_dependence
  - keywords: agency, intention, morality, volition
- `ط و ع B007` — تهيؤ المرعى والثمر
  - activated_by_or_with: د ع و, ز ب ن, ق ر ب, ن د و
  - themes: abundance_scarcity, agriculture, calendar_season, habitat_ecology, harvest_cultivation, livestock, pasture_forage, provision_resource, reproduction_birth
  - keywords: agriculture, ecology, fertility, forage, harvest, livestock

### س ج د

- `س ج د B001` — التطامن والذل
  - activated_by_or_with: د ع و, ط و ع, ق ر ب, ن د و
  - themes: authority_governance, communication, ethics_morality, hierarchy_status, posture_embodiment, religion_worship, ritual
  - keywords: devotion, gesture, hierarchy, humility, posture, ritual, worship
- `س ج د B002` — موضع السجود ومصلاه
  - activated_by_or_with: د ع و, ز ب ن, ط و ع, ق ر ب, ن د و
  - themes: architecture_construction, authority_governance, household_community, religion_worship, ritual, space
  - keywords: architecture, community, gathering, institution, ritual, space, worship
- `س ج د B003` — أعضاء السجود وأثره
  - activated_by_or_with: د ع و, ز ب ن, ط و ع, ق ر ب, ن د و
  - themes: anatomy, body, communication, pattern_marking, posture_embodiment, ritual, social_relations
  - keywords: anatomy, body, contact, embodiment, gesture, ritual
- `س ج د B004` — طأطأة الرأس والانحناء
  - activated_by_or_with: د ع و, ز ب ن, ط و ع, ق ر ب, ن د و
  - themes: communication, ethics_morality, force_power, motion, orientation_direction, posture_embodiment
  - keywords: gesture, humility, motion, orientation, posture
- `س ج د B005` — إدامة النظر وفتور الطرف
  - activated_by_or_with: د ع و, ز ب ن, ط و ع, ق ر ب, ن د و
  - themes: grammar_expression, memory_attention, perception, physiology, posture_embodiment, stability_endurance
  - keywords: attention, perception, posture
- `س ج د B006` — دراهم الصور المسجود لها
  - activated_by_or_with: د ع و, ز ب ن, ط و ع, ق ر ب, ن د و
  - themes: authority_governance, communication, economy, finance_debt, pattern_marking, religion_worship
  - keywords: economy, worship
- `س ج د B007` — الإسجاد والجزية
  - activated_by_or_with: د ع و, ز ب ن, ط و ع, ق ر ب, ن د و
  - themes: authority_governance, finance_debt, household_community, identity_personhood, law, obligation_contract, quantity_number
  - keywords: community, governance, identity, law, obligation

### ق ر ب

- `ق ر ب B001` — الدنو وخلاف البعد
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ن د و
  - themes: containment_access, measurement, motion, place_location, posture_embodiment, social_relations, space
  - keywords: access, embodiment, location, measurement, motion, relation, space
- `ق ر ب B002` — دنو الزمان وانقضاء الشيء
  - activated_by_or_with: د ع و, ز ب ن, ط و ع
  - themes: calendar_season, change_transition, growth_decay, harvest_cultivation, time
  - keywords: harvest
- `ق ر ب B003` — قرابة الرحم والنسب
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ن د و
  - themes: household_community, marriage_genealogy, obligation_contract, social_relations, wealth_property
  - keywords: community, genealogy, inheritance, obligation, society
- `ق ر ب B004` — حظوة المقربين وخاصة الملك
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ن د و
  - themes: authority_governance, force_power, hierarchy_status, labor_work, politics_order, trust_loyalty
  - keywords: authority, governance, hierarchy, service
- `ق ر ب B005` — القربة والقربان إلى الله
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ن د و
  - themes: commerce_exchange, religion_worship, ritual, social_relations
  - keywords: devotion, religion, ritual, worship
- `ق ر ب B006` — القرب بالرعاية والقدرة
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ق ر ب B007` — مقاربة الشيء وملابسته
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ن د و
  - themes: boundary, danger_harm, ethics_morality, law, social_relations
  - keywords: boundary, contact, ethics, law, transgression
- `ق ر ب B008` — ليلة القرب وطلب الماء
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ن د و
  - themes: animal, husbandry, livestock, motion, provision_resource, time, travel, water_hydrology
  - keywords: animal, livestock, mobility, resource, travel, water
- `ق ر ب B009` — القربة وعاء الماء
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ن د و
  - themes: household_community, material, provision_resource, storage_vessels, tools_equipment, transport, water_hydrology
  - keywords: container, domesticity, leather, subsistence, tool, transport, water
- `ق ر ب B010` — قراب السيف ووعاؤه
  - activated_by_or_with: د ع و, ز ب ن, ط و ع
  - themes: material, protection_security, storage_vessels, tools_equipment, violence_warfare
  - keywords: container, leather, protection, tool, warfare
- `ق ر ب B011` — القارب السفينة الصغيرة
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ن د و
  - themes: commerce_exchange, labor_work, motion, transport, travel, water_hydrology
  - keywords: mobility, service, transport, travel, water
- `ق ر ب B012` — دنو الولادة في الحيوان
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ن د و
  - themes: animal, body, physiology, reproduction_birth, time
  - keywords: animal, body, fertility, time
- `ق ر ب B013` — الخيل والإبل المقربة
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ن د و
  - themes: animal, capacity_ability, hierarchy_status, husbandry, labor_work, motion, transport, violence_warfare
  - keywords: animal, equestrian, husbandry, mobility, service, status, transport, warfare
- `ق ر ب B014` — تقريب الفرس في العدو
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ن د و
  - themes: agency_action, animal, knowledge_learning, motion, recreation_sport
  - keywords: animal, coordination, motion, training
- `ق ر ب B015` — قُرْب الفرس والخاصرة
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ن د و
  - themes: anatomy, animal, body, communication, orientation_direction, perception, place_location, posture_embodiment
  - keywords: anatomy, animal, body, embodiment, gesture, location, orientation, touch
- `ق ر ب B016` — القراب والمقاربة في المقدار
  - activated_by_or_with: د ع و, ز ب ن, س ج د, ط و ع, ن د و
  - themes: capacity_ability, economy, measurement, quantity_number, reasoning_decision, storage_vessels, time, value_quality
  - keywords: container, economy, measurement, time

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
