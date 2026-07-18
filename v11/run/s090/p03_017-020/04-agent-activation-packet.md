# v11 Activation Packet — S90:17-20

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_17: ثُمَّ كَانَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ وَتَوَاصَوْا۟ بِٱلصَّبْرِ وَتَوَاصَوْا۟ بِٱلْمَرْحَمَةِ
- verse_18: أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْمَيْمَنَةِ
- verse_19: وَٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا هُمْ أَصْحَٰبُ ٱلْمَشْـَٔمَةِ
- verse_20: عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ك و ن → ء م ن → و ص ي → ص ب ر → ر ح م → ص ح ب → ي م ن → ك ف ر → ء ي ي → ش ء م → ن و ر → و ص د

## Branch inventory summary

- ك و ن: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء م ن: 3 branches (3 with Qnet bridge-theme nodes; 0 Furūq-only)
- و ص ي: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص ب ر: 18 branches (15 with Qnet bridge-theme nodes; 3 Furūq-only)
- ر ح م: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص ح ب: 8 branches (8 with Qnet bridge-theme nodes; 0 Furūq-only)
- ي م ن: 7 branches (6 with Qnet bridge-theme nodes; 1 Furūq-only)
- ك ف ر: 15 branches (15 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء ي ي: 10 branches (10 with Qnet bridge-theme nodes; 0 Furūq-only)
- ش ء م: 3 branches (3 with Qnet bridge-theme nodes; 0 Furūq-only)
- ن و ر: 11 branches (11 with Qnet bridge-theme nodes; 0 Furūq-only)
- و ص د: 4 branches (4 with Qnet bridge-theme nodes; 0 Furūq-only)

## QAC-first root resolution audit

- ك و ن | qac_keys=كون | status=resolved | matches=root_001332
- ء م ن | qac_keys=ءمن | status=resolved | matches=root_000054
- و ص ي | qac_keys=وصي | status=resolved | matches=root_001656
- ص ب ر | qac_keys=صبر | status=resolved | matches=root_000840
- ر ح م | qac_keys=رحم | status=resolved | matches=root_000552
- ص ح ب | qac_keys=صحب | status=resolved | matches=root_000844
- ي م ن | qac_keys=يمن | status=resolved | matches=root_001698
- ك ف ر | qac_keys=كفر | status=resolved | matches=root_001307
- ء ي ي | qac_keys=ءيي | status=resolved | matches=root_000074
- ش ء م | qac_keys=شءم | status=resolved | matches=root_000772
- ن و ر | qac_keys=نور | status=resolved | matches=root_001564
- و ص د | qac_keys=وصد | status=resolved | matches=root_001653

## Top candidate bridges

- `ء م ن B002` ↔ `ك ف ر B003` | score_hint=28 | discovery_hint=14 | themes=authority_governance, belief_revelation, proof_uncertainty, religion_worship | keywords=belief, faith, obedience, religion, truth | q2=—
- `ي م ن B003` ↔ `ء ي ي B010` | score_hint=26 | discovery_hint=14 | themes=language_speech, law, obligation_contract, religion_worship, testimony_witness | keywords=law, religion, speech, testimony | q2=—
- `ي م ن B005` ↔ `ش ء م B002` | score_hint=25 | discovery_hint=19 | themes=geography_landscape, identity_personhood, migration_displacement, place_location | keywords=geography, identity, migration, place | q2=—
- `ك و ن B003` ↔ `ص ب ر B003` | score_hint=24 | discovery_hint=16 | themes=obligation_contract, social_relations, support_dependence, trust_loyalty | keywords=liability, obligation, patronage, trust | q2=—
- `ء م ن B002` ↔ `ي م ن B003` | score_hint=24 | discovery_hint=15 | themes=obligation_contract, religion_worship, testimony_witness, trust_loyalty | keywords=covenant, religion, testimony, trust | q2=—
- `ي م ن B002` ↔ `ش ء م B001` | score_hint=24 | discovery_hint=14 | themes=body, navigation_route, orientation_direction, space | keywords=body, navigation, orientation, space | q2=—
- `ء م ن B001` ↔ `ر ح م B001` | score_hint=22 | discovery_hint=13 | themes=emotion, ethics_morality, protection_security | keywords=emotion, ethic, ethics, protection | q2=—
- `ص ب ر B003` ↔ `ي م ن B003` | score_hint=22 | discovery_hint=15 | themes=law, obligation_contract, trust_loyalty | keywords=contract, law, obligation, trust | q2=—
- `ي م ن B003` ↔ `ك ف ر B006` | score_hint=20 | discovery_hint=13 | themes=language_speech, law, religion_worship, testimony_witness | keywords=law, religion, speech | q2=—
- `ك ف ر B006` ↔ `ء ي ي B010` | score_hint=20 | discovery_hint=13 | themes=language_speech, law, religion_worship, testimony_witness | keywords=law, religion, speech | q2=—
- `ك و ن B003` ↔ `ء م ن B001` | score_hint=18 | discovery_hint=14 | themes=obligation_contract, protection_security, trust_loyalty | keywords=obligation, protection, trust | q2=—
- `ك و ن B003` ↔ `و ص ي B002` | score_hint=18 | discovery_hint=14 | themes=agency_action, obligation_contract, trust_loyalty | keywords=agency, obligation, trust | q2=—
- `و ص ي B001` ↔ `ص ح ب B007` | score_hint=18 | discovery_hint=14 | themes=growth_decay, habitat_ecology, plant_vegetation | keywords=growth, nature, vegetation | q2=—
- `و ص ي B001` ↔ `ك ف ر B002` | score_hint=18 | discovery_hint=12 | themes=boundary, geography_landscape, habitat_ecology | keywords=boundary, landscape, nature | q2=—
- `و ص ي B002` ↔ `ص ب ر B003` | score_hint=18 | discovery_hint=14 | themes=law, obligation_contract, trust_loyalty | keywords=law, obligation, trust | q2=—
- `و ص ي B002` ↔ `ر ح م B002` | score_hint=18 | discovery_hint=14 | themes=law, obligation_contract, wealth_property | keywords=inheritance, law, obligation | q2=—
- `و ص ي B002` ↔ `ي م ن B003` | score_hint=18 | discovery_hint=14 | themes=law, obligation_contract, trust_loyalty | keywords=law, obligation, trust | q2=—
- `ص ب ر B003` ↔ `ر ح م B002` | score_hint=18 | discovery_hint=13 | themes=law, obligation_contract, social_relations | keywords=law, obligation, society | q2=—
- `ر ح م B002` ↔ `ك ف ر B006` | score_hint=18 | discovery_hint=14 | themes=household_community, identity_personhood, law | keywords=community, identity, law | q2=—
- `ص ح ب B007` ↔ `و ص د B004` | score_hint=18 | discovery_hint=15 | themes=growth_decay, habitat_ecology, plant_vegetation | keywords=ecology, growth, vegetation | q2=—
- `ك ف ر B010` ↔ `ن و ر B004` | score_hint=18 | discovery_hint=16 | themes=growth_decay, plant_vegetation, reproduction_birth | keywords=botany, fertility, growth | q2=—
- `ر ح م B001` ↔ `ص ح ب B002` | score_hint=18 | discovery_hint=12 | themes=belief_revelation, emotion, ethics_morality, hospitality_welfare, protection_security | keywords=care, protection | q2=—
- `ك ف ر B012` ↔ `ش ء م B002` | score_hint=18 | discovery_hint=12 | themes=boundary, geography_landscape, household_community, place_location, social_relations | keywords=geography, settlement | q2=—
- `ص ب ر B001` ↔ `ر ح م B001` | score_hint=16 | discovery_hint=11 | themes=emotion, ethics_morality | keywords=emotion, ethics, virtue | q2=—
- `ص ح ب B001` ↔ `ك ف ر B005` | score_hint=16 | discovery_hint=13 | themes=social_relations, trust_loyalty | keywords=loyalty, relation, sociality | q2=—
- `ك ف ر B012` ↔ `و ص د B002` | score_hint=16 | discovery_hint=13 | themes=boundary, place_location | keywords=boundary, habitation, settlement | q2=—
- `ك ف ر B013` ↔ `و ص د B003` | score_hint=16 | discovery_hint=13 | themes=architecture_construction, terrain_desert | keywords=architecture, shelter, terrain | q2=—
- `ك و ن B004` ↔ `ك ف ر B007` | score_hint=16 | discovery_hint=13 | themes=authority_governance, control_restraint, ethics_morality, force_power | keywords=obedience, power | q2=—
- `ء م ن B002` ↔ `ء ي ي B010` | score_hint=16 | discovery_hint=12 | themes=obligation_contract, proof_uncertainty, religion_worship, testimony_witness | keywords=religion, testimony | q2=—
- `و ص ي B001` ↔ `و ص د B004` | score_hint=16 | discovery_hint=13 | themes=growth_decay, habitat_ecology, plant_vegetation, social_relations | keywords=growth, vegetation | q2=—
- `ك ف ر B013` ↔ `ن و ر B005` | score_hint=16 | discovery_hint=12 | themes=architecture_construction, boundary, geography_landscape, navigation_route | keywords=architecture, boundary | q2=—
- `ص ب ر B009` ↔ `ك ف ر B010` | score_hint=14 | discovery_hint=14 | themes=plant_vegetation | keywords=botany, fruit, plant | q2=—
- `ك و ن B001` ↔ `ء ي ي B001` | score_hint=14 | discovery_hint=10 | themes=cognition, sequence_cycle, time | keywords=temporality, time | q2=—
- `ك و ن B001` ↔ `ء ي ي B006` | score_hint=14 | discovery_hint=11 | themes=grammar_expression, sequence_cycle, time | keywords=grammar, time | q2=—
- `ك و ن B003` ↔ `ص ح ب B002` | score_hint=14 | discovery_hint=14 | themes=hospitality_welfare, protection_security, support_dependence | keywords=care, protection | q2=—
- `ك و ن B006` ↔ `ش ء م B003` | score_hint=14 | discovery_hint=12 | themes=abundance_scarcity, danger_harm, suffering_hardship | keywords=adversity, fortune | q2=—
- `ء م ن B003` ↔ `ي م ن B003` | score_hint=14 | discovery_hint=12 | themes=language_speech, religion_worship, ritual | keywords=ritual, speech | q2=—
- `و ص ي B003` ↔ `ر ح م B002` | score_hint=14 | discovery_hint=12 | themes=ethics_morality, household_community, social_relations | keywords=community, ethics | q2=—
- `و ص ي B003` ↔ `ء ي ي B003` | score_hint=14 | discovery_hint=12 | themes=belief_revelation, communication, household_community | keywords=communication, community | q2=—
- `ص ب ر B002` ↔ `ك ف ر B006` | score_hint=14 | discovery_hint=12 | themes=authority_governance, law, testimony_witness | keywords=authority, law | q2=—
- `ص ب ر B009` ↔ `ك ف ر B008` | score_hint=14 | discovery_hint=15 | themes=agriculture, food_nutrition, plant_vegetation | keywords=agriculture, food | q2=—
- `ص ب ر B012` ↔ `ك ف ر B006` | score_hint=14 | discovery_hint=12 | themes=authority_governance, justice_judgment, law | keywords=authority, law | q2=—
- `ي م ن B001` ↔ `ش ء م B003` | score_hint=14 | discovery_hint=11 | themes=abundance_scarcity, belief_revelation, religion_worship | keywords=fortune, religion | q2=—
- `ي م ن B004` ↔ `ك ف ر B007` | score_hint=14 | discovery_hint=13 | themes=agency_action, authority_governance, force_power | keywords=agency, power | q2=—
- `ك ف ر B001` ↔ `و ص د B001` | score_hint=14 | discovery_hint=11 | themes=boundary, containment_access, protection_security | keywords=enclosure, protection | q2=—
- `ك ف ر B006` ↔ `ء ي ي B003` | score_hint=14 | discovery_hint=13 | themes=belief_revelation, household_community, identity_personhood | keywords=community, identity | q2=—
- `ك ف ر B008` ↔ `ن و ر B004` | score_hint=14 | discovery_hint=15 | themes=growth_decay, plant_vegetation, reproduction_birth | keywords=fertility, growth | q2=—
- `ك ف ر B008` ↔ `و ص د B004` | score_hint=14 | discovery_hint=14 | themes=earth_geology, growth_decay, plant_vegetation | keywords=earth, growth | q2=—
- `و ص ي B004` ↔ `ص ب ر B011` | score_hint=13 | discovery_hint=18 | themes=food_nutrition, provision_resource | keywords=food, provision | q2=—
- `و ص ي B004` ↔ `ن و ر B002` | score_hint=13 | discovery_hint=16 | themes=animal, livestock | keywords=animal, livestock | q2=—
- `ك و ن B002` ↔ `ش ء م B001` | score_hint=12 | discovery_hint=11 | themes=place_location, space | keywords=location, space | q2=—
- `ك و ن B003` ↔ `ر ح م B001` | score_hint=12 | discovery_hint=12 | themes=hospitality_welfare, protection_security | keywords=care, protection | q2=—
- `ك و ن B003` ↔ `ي م ن B003` | score_hint=12 | discovery_hint=13 | themes=obligation_contract, trust_loyalty | keywords=obligation, trust | q2=—
- `ك و ن B003` ↔ `ي م ن B004` | score_hint=12 | discovery_hint=13 | themes=agency_action, protection_security | keywords=agency, protection | q2=—
- `ك و ن B004` ↔ `ك ف ر B014` | score_hint=12 | discovery_hint=12 | themes=authority_governance, religion_worship | keywords=obedience, submission | q2=—
- `ك و ن B005` ↔ `ك ف ر B005` | score_hint=12 | discovery_hint=13 | themes=identity_personhood, language_speech | keywords=identity, speech | q2=—
- `ك و ن B005` ↔ `ك ف ر B006` | score_hint=12 | discovery_hint=13 | themes=identity_personhood, language_speech | keywords=identity, speech | q2=—
- `ك و ن B006` ↔ `ص ب ر B006` | score_hint=12 | discovery_hint=12 | themes=danger_harm, suffering_hardship | keywords=adversity, suffering | q2=—
- `ء م ن B001` ↔ `و ص ي B002` | score_hint=12 | discovery_hint=12 | themes=obligation_contract, trust_loyalty | keywords=obligation, trust | q2=—
- `ء م ن B001` ↔ `ص ب ر B001` | score_hint=12 | discovery_hint=10 | themes=emotion, ethics_morality | keywords=emotion, ethics | q2=—
- `ء م ن B001` ↔ `ص ب ر B003` | score_hint=12 | discovery_hint=12 | themes=obligation_contract, trust_loyalty | keywords=obligation, trust | q2=—
- `ء م ن B001` ↔ `ر ح م B002` | score_hint=12 | discovery_hint=11 | themes=ethics_morality, obligation_contract | keywords=ethics, obligation | q2=—
- `ء م ن B001` ↔ `ي م ن B003` | score_hint=12 | discovery_hint=12 | themes=obligation_contract, trust_loyalty | keywords=obligation, trust | q2=—
- `ء م ن B001` ↔ `و ص د B003` | score_hint=12 | discovery_hint=12 | themes=architecture_construction, protection_security | keywords=protection, shelter | q2=—
- `ء م ن B002` ↔ `ش ء م B003` | score_hint=12 | discovery_hint=12 | themes=belief_revelation, religion_worship | keywords=belief, religion | q2=—
- `و ص ي B002` ↔ `ص ب ر B002` | score_hint=12 | discovery_hint=12 | themes=authority_governance, law | keywords=authority, law | q2=—
- `و ص ي B002` ↔ `ص ب ر B012` | score_hint=12 | discovery_hint=12 | themes=authority_governance, law | keywords=authority, law | q2=—
- `و ص ي B002` ↔ `ي م ن B004` | score_hint=12 | discovery_hint=12 | themes=agency_action, authority_governance | keywords=agency, authority | q2=—
- `و ص ي B002` ↔ `ك ف ر B006` | score_hint=12 | discovery_hint=12 | themes=authority_governance, law | keywords=authority, law | q2=—
- `و ص ي B003` ↔ `ك ف ر B004` | score_hint=12 | discovery_hint=13 | themes=commerce_exchange, ethics_morality | keywords=ethics, reciprocity | q2=—
- `و ص ي B003` ↔ `ء ي ي B009` | score_hint=12 | discovery_hint=12 | themes=communication, knowledge_learning | keywords=communication, instruction | q2=—
- `و ص ي B004` ↔ `ص ب ر B009` | score_hint=12 | discovery_hint=14 | themes=agriculture, food_nutrition | keywords=agriculture, food | q2=—
- `و ص ي B004` ↔ `ك ف ر B008` | score_hint=12 | discovery_hint=14 | themes=agriculture, food_nutrition | keywords=agriculture, food | q2=—
- `ص ب ر B002` ↔ `ي م ن B003` | score_hint=12 | discovery_hint=12 | themes=law, testimony_witness | keywords=law, testimony | q2=—
- `ص ب ر B002` ↔ `ء ي ي B010` | score_hint=12 | discovery_hint=12 | themes=law, testimony_witness | keywords=law, testimony | q2=—
- `ص ب ر B003` ↔ `ص ح ب B001` | score_hint=12 | discovery_hint=12 | themes=social_relations, trust_loyalty | keywords=association, society | q2=—
- `ص ب ر B005` ↔ `ص ح ب B006` | score_hint=12 | discovery_hint=13 | themes=material, substance_texture | keywords=material, texture | q2=—
- `ص ب ر B006` ↔ `ش ء م B003` | score_hint=12 | discovery_hint=12 | themes=danger_harm, suffering_hardship | keywords=adversity, disaster | q2=—
- `ص ب ر B008` ↔ `ك ف ر B011` | score_hint=12 | discovery_hint=13 | themes=perception, plant_vegetation | keywords=botany, plant | q2=—
- `ص ب ر B009` ↔ `ك ف ر B011` | score_hint=12 | discovery_hint=13 | themes=perception, plant_vegetation | keywords=botany, plant | q2=—

## Per-root candidate activations

### ك و ن

- `ك و ن B001` — وقوع الشيء وحضوره في زمان
  - activated_by_or_with: ء م ن, ء ي ي, ص ب ر, ص ح ب, ك ف ر, ن و ر, و ص ي, ي م ن
  - themes: cognition, grammar_expression, language_speech, sequence_cycle, stability_endurance, time
  - keywords: grammar, temporality, time
- `ك و ن B002` — المكان والمكانة من الكون
  - activated_by_or_with: ء ي ي, ش ء م, ص ب ر, ص ح ب, ك ف ر, ن و ر, و ص د, ي م ن
  - themes: capacity_ability, hierarchy_status, place_location, space
  - keywords: hierarchy, location, place, settlement, space, status
- `ك و ن B003` — الكفالة والقيام على فلان
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ن و ر, و ص د, و ص ي, ي م ن
  - themes: agency_action, hospitality_welfare, obligation_contract, protection_security, social_relations, support_dependence, trust_loyalty
  - keywords: agency, care, liability, obligation, patronage, protection, trust
- `ك و ن B004` — الخضوع بالاستكانة
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ن و ر, و ص د, و ص ي, ي م ن
  - themes: authority_governance, control_restraint, danger_harm, ethics_morality, force_power, religion_worship, support_dependence
  - keywords: obedience, power, submission
- `ك و ن B005` — الشيخ المنسوب إلى كُنْتُ
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ن و ر, ي م ن
  - themes: identity_personhood, language_speech, life_stage_aging, memory_attention, physiology, time, writing_text
  - keywords: identity, life, speech, time
- `ك و ن B006` — حالة السوء بكينة
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ن و ر, و ص ي, ي م ن
  - themes: abundance_scarcity, danger_harm, ethics_morality, perception, suffering_hardship, value_quality
  - keywords: adversity, fortune, suffering

### ء م ن

- `ء م ن B001` — سكون القلب في أمن وثقة
  - activated_by_or_with: ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: architecture_construction, emotion, ethics_morality, obligation_contract, protection_security, trust_loyalty
  - keywords: custody, emotion, ethic, ethics, obligation, protection, shelter, trust
- `ء م ن B002` — تصديق يطمئن إليه القلب
  - activated_by_or_with: ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: authority_governance, belief_revelation, knowledge_learning, obligation_contract, proof_uncertainty, religion_worship, testimony_witness, trust_loyalty
  - keywords: belief, covenant, epistemology, faith, obedience, religion, testimony, trust, truth
- `ء م ن B003` — قول آمين طلبا للاستجابة
  - activated_by_or_with: ء ي ي, ر ح م, ش ء م, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: belief_revelation, grammar_expression, language_speech, reasoning_decision, religion_worship, ritual
  - keywords: ritual, speech, theology, worship

### و ص ي

- `و ص ي B001` — وصل الشيء بالشيء
  - activated_by_or_with: ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, ي م ن
  - themes: boundary, change_transition, geography_landscape, growth_decay, habitat_ecology, plant_vegetation, sequence_cycle, social_relations, stability_endurance
  - keywords: boundary, continuity, growth, landscape, nature, relation, sequence, transition, vegetation
- `و ص ي B002` — عهد موصول إلى غيره
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, ي م ن
  - themes: agency_action, authority_governance, law, mortality_death, obligation_contract, sequence_cycle, trust_loyalty, wealth_property
  - keywords: agency, authority, inheritance, law, mortality, obligation, succession, trust
- `و ص ي B003` — تبادل الوصية بين القوم
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, ي م ن
  - themes: belief_revelation, commerce_exchange, communication, ethics_morality, household_community, knowledge_learning, social_relations
  - keywords: communication, community, ethics, guidance, instruction, reciprocity
- `و ص ي B004` — موافقة المرعى للسائمة
  - activated_by_or_with: ر ح م, ص ب ر, ص ح ب, ك ف ر, ن و ر, و ص د
  - themes: agriculture, animal, food_nutrition, habitat_ecology, livestock, provision_resource
  - keywords: agriculture, animal, ecology, food, livestock, provision

### ص ب ر

- `ص ب ر B001` — حبس النفس عن الجزع
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي
  - themes: cognition, control_restraint, emotion, ethics_morality, stability_endurance, suffering_hardship
  - keywords: discipline, emotion, ethics, suffering, virtue
- `ص ب ر B002` — حبس القهر للقتل أو اليمين
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: authority_governance, control_restraint, law, protection_security, punishment_sanction, testimony_witness, violence_warfare
  - keywords: authority, custody, law, punishment, testimony, violence
- `ص ب ر B003` — تحمل الكفالة والملازمة
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: kinship, law, obligation_contract, social_relations, support_dependence, trust_loyalty
  - keywords: association, contract, kinship, law, liability, obligation, patronage, society, trust
- `ص ب ر B004` — أعلى الشيء وجوانبه
  - activated_by_or_with: ء ي ي, ش ء م, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: boundary, measurement, orientation_direction, space, storage_vessels, surface_shape
  - keywords: boundary, container, measure, orientation, surface, topology
- `ص ب ر B005` — حجر غليظ وأرض حصباء
  - activated_by_or_with: ء ي ي, ش ء م, ص ح ب, ك ف ر, ن و ر, و ص د, و ص ي, ي م ن
  - themes: earth_geology, geography_landscape, material, substance_texture, terrain_desert
  - keywords: earth, geology, landscape, material, terrain, texture
- `ص ب ر B006` — الوقوع في شدة لا منفذ منها
  - activated_by_or_with: ش ء م, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د
  - themes: conflict, control_restraint, danger_harm, suffering_hardship
  - keywords: adversity, conflict, constraint, disaster, suffering
- `ص ب ر B007` — شدة برد الشتاء
  - activated_by_or_with: ء ي ي, ش ء م, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي
  - themes: calendar_season, fire_heat, habitat_ecology, stability_endurance, suffering_hardship, weather_climate
  - keywords: season, weather
- `ص ب ر B008` — الصبر المر وعصارته
  - activated_by_or_with: ء ي ي, ر ح م, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: health_medicine, perception, plant_vegetation, substance_texture
  - keywords: botany, flavor, medicine, plant, taste
- `ص ب ر B009` — الصبار حمل الشجرة الحامض
  - activated_by_or_with: ء ي ي, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي
  - themes: agriculture, food_nutrition, perception, plant_vegetation
  - keywords: agriculture, botany, flavor, food, fruit, plant, taste
- `ص ب ر B010` — سحاب أبيض متراكم
  - activated_by_or_with: ش ء م, ك ف ر, ك و ن, و ص د, ي م ن
  - themes: abundance_scarcity, form_structure, sky_astronomy, weather_climate
  - keywords: accumulation, weather
- `ص ب ر B011` — رقاقة الخوان وكومة الطعام
  - activated_by_or_with: ء ي ي, ش ء م, ك ف ر, ك و ن, و ص ي, ي م ن
  - themes: abundance_scarcity, commerce_exchange, food_nutrition, measurement, provision_resource, quantity_number, storage_vessels
  - keywords: accumulation, container, food, provision, quantity
- `ص ب ر B012` — الإقصاص والقود
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي, ي م ن
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
  - activated_by_or_with: ء ي ي, ر ح م, ش ء م, ص ح ب, ك ف ر, ك و ن, ن و ر, ي م ن
  - themes: identity_personhood, kinship, naming_classification, time
  - keywords: ethnicity, identity, kinship
- `ص ب ر B017` — الجبل ووسطه
  - activated_by_or_with: ء ي ي, ش ء م, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: earth_geology, geography_landscape, orientation_direction, place_location, terrain_desert
  - keywords: geography, geology, landscape, orientation, place, terrain
- `ص ب ر B018` — سداد القارورة والبئر
  - activated_by_or_with: ش ء م, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: boundary, containment_access, pattern_marking, storage_vessels, tools_equipment, value_quality
  - keywords: barrier, container, utility

### ر ح م

- `ر ح م B001` — الرَّحْمَة والرقة
  - activated_by_or_with: ء م ن, ء ي ي, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: belief_revelation, emotion, ethics_morality, hospitality_welfare, protection_security
  - keywords: care, emotion, ethic, ethics, forgiveness, protection, virtue
- `ر ح م B002` — الرَّحِم والقرابة
  - activated_by_or_with: ء م ن, ء ي ي, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: ethics_morality, family, household_community, identity_personhood, law, obligation_contract, social_relations, wealth_property
  - keywords: community, ethics, family, identity, inheritance, law, obligation, society
- `ر ح م B003` — رَحِم الأنثى
  - activated_by_or_with: ء ي ي, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: body, growth_decay, health_medicine, physiology, reproduction_birth
  - keywords: body, childbirth, fertility, medicine
- `ر ح م B004` — وجع الرَّحِم بعد الولادة
  - activated_by_or_with: ص ب ر, ص ح ب, ك ف ر, ن و ر, و ص ي, ي م ن
  - themes: animal, health_medicine, reproduction_birth
  - keywords: animal, childbirth, medicine

### ص ح ب

- `ص ح ب B001` — الصُّحبة والملازمة
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: authority_governance, place_location, protection_security, social_relations, trust_loyalty
  - keywords: association, belonging, custody, loyalty, proximity, relation, sociality, society
- `ص ح ب B002` — الحفظ بالمصاحبة
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: belief_revelation, emotion, ethics_morality, health_medicine, hospitality_welfare, protection_security, religion_worship, support_dependence
  - keywords: care, guidance, protection
- `ص ح ب B003` — الإصحاب والانقياد
  - activated_by_or_with: ء م ن, ء ي ي, ص ب ر, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: authority_governance, change_transition, control_restraint, husbandry, knowledge_learning, motion
  - keywords: authority, discipline, motion, obedience
- `ص ح ب B004` — جعل الشيء مصاحبا واستصحابه
  - activated_by_or_with: ء ي ي, ر ح م, ش ء م, ص ب ر, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: social_relations, stability_endurance, transport, value_quality, wealth_property
  - keywords: association, continuity, transport, utility
- `ص ح ب B005` — بلوغ الابن صاحبا
  - activated_by_or_with: ء ي ي, ر ح م, ش ء م, ص ب ر, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: family, kinship, life_stage_aging, physiology, reproduction_birth, sequence_cycle, social_relations
  - keywords: family, kinship, life, sociality, succession
- `ص ح ب B006` — أديم مُصحَب عليه الشعر
  - activated_by_or_with: ء ي ي, ر ح م, ص ب ر, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: animal, material, stability_endurance, substance_texture, textile_clothing
  - keywords: animal, covering, material, textile, texture
- `ص ح ب B007` — طُحلب يعلو الماء
  - activated_by_or_with: ر ح م, ص ب ر, ك ف ر, ن و ر, و ص د, و ص ي, ي م ن
  - themes: growth_decay, habitat_ecology, plant_vegetation, surface_shape, textile_clothing, water_hydrology
  - keywords: covering, ecology, growth, nature, plant, surface, vegetation, water
- `ص ح ب B008` — لون أَصحَب إلى الحمرة
  - activated_by_or_with: ء ي ي, ر ح م, ص ب ر, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: animal, naming_classification, perception, substance_texture, textile_clothing
  - keywords: animal, classification, perception, pigment

### ي م ن

- `ي م ن B001` — اليمن والبركة
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي
  - themes: abundance_scarcity, belief_revelation, health_medicine, religion_worship, ritual, value_quality
  - keywords: fortune, religion, ritual
- `ي م ن B002` — اليد اليمنى والجهة اليمنى
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي
  - themes: body, commerce_exchange, hospitality_welfare, motion, navigation_route, orientation_direction, ritual, space
  - keywords: body, navigation, orientation, ritual, space
- `ي م ن B003` — يمين الحلف
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي
  - themes: language_speech, law, obligation_contract, religion_worship, ritual, testimony_witness, trust_loyalty
  - keywords: contract, covenant, law, obligation, religion, ritual, speech, testimony, trust
- `ي م ن B004` — يمين القوة والحق
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي
  - themes: agency_action, authority_governance, force_power, justice_judgment, protection_security, reasoning_decision
  - keywords: agency, authority, causality, justice, power, protection
- `ي م ن B005` — اليمن البلد والانتساب
  - activated_by_or_with: ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي
  - themes: commerce_exchange, geography_landscape, identity_personhood, kinship, migration_displacement, place_location, textile_clothing
  - keywords: ethnicity, geography, identity, migration, place, textile
- `ي م ن B006` — ملك اليمين وعقده
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ي م ن B007` — التيمن الموت
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ح ب, ك ف ر, ن و ر, و ص ي
  - themes: body, change_transition, mortality_death, posture_embodiment, ritual
  - keywords: body, burial, death, mortality, ritual, transition

### ك ف ر

- `ك ف ر B001` — ستر وتغطية
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: boundary, concealment_disclosure, containment_access, perception, protection_security, textile_clothing
  - keywords: barrier, concealment, covering, enclosure, protection, visibility
- `ك ف ر B002` — غمر ساتر
  - activated_by_or_with: ء ي ي, ش ء م, ص ب ر, ص ح ب, ن و ر, و ص د, و ص ي, ي م ن
  - themes: boundary, calendar_season, concealment_disclosure, geography_landscape, habitat_ecology, light_darkness, sky_astronomy, water_hydrology
  - keywords: boundary, concealment, landscape, nature, water
- `ك ف ر B003` — حجب الحق
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: authority_governance, belief_revelation, justice_judgment, proof_uncertainty, religion_worship
  - keywords: belief, doctrine, faith, judgment, obedience, religion, theology, truth
- `ك ف ر B004` — ستر النعمة
  - activated_by_or_with: ء م ن, ر ح م, ص ب ر, ص ح ب, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: commerce_exchange, ethics_morality, hospitality_welfare
  - keywords: ethics, reciprocity, virtue
- `ك ف ر B005` — تبرؤ وتنصل
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: conflict, identity_personhood, language_speech, obligation_contract, social_relations, trust_loyalty
  - keywords: conflict, identity, loyalty, relation, responsibility, sociality, speech
- `ك ف ر B006` — نسبة إلى الكفر
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: authority_governance, belief_revelation, hierarchy_status, household_community, identity_personhood, justice_judgment, language_speech, law, religion_worship, testimony_witness
  - keywords: authority, community, doctrine, identity, judgment, law, religion, speech, status
- `ك ف ر B007` — إلجاء إلى العصيان
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ص ب ر, ص ح ب, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: agency_action, authority_governance, control_restraint, ethics_morality, force_power, obligation_contract
  - keywords: agency, constraint, morality, obedience, power, responsibility
- `ك ف ر B008` — تغطية البذر
  - activated_by_or_with: ء ي ي, ر ح م, ص ب ر, ص ح ب, ك و ن, ن و ر, و ص د, و ص ي
  - themes: agriculture, concealment_disclosure, earth_geology, food_nutrition, growth_decay, plant_vegetation, reproduction_birth, sequence_cycle
  - keywords: agriculture, concealment, earth, fertility, food, growth
- `ك ف ر B009` — محو الإثم بتغطيته
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: change_transition, ethics_morality, health_medicine, justice_judgment, law, purity_cleansing, religion_worship
  - keywords: accountability, ethics, forgiveness, law, morality, purity, religion
- `ك ف ر B010` — كمام الثمر
  - activated_by_or_with: ء م ن, ر ح م, ص ب ر, ص ح ب, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: growth_decay, plant_vegetation, protection_security, reproduction_birth, storage_vessels
  - keywords: botany, container, fertility, fruit, growth, plant, protection
- `ك ف ر B011` — كافور طيب
  - activated_by_or_with: ء ي ي, ر ح م, ص ب ر, ص ح ب, ك و ن, ن و ر, و ص د, و ص ي
  - themes: perception, plant_vegetation, purity_cleansing, water_hydrology, wealth_property
  - keywords: botany, plant, purity, water
- `ك ف ر B012` — موضع منقطع
  - activated_by_or_with: ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: boundary, geography_landscape, household_community, measurement, mortality_death, place_location, social_relations
  - keywords: boundary, burial, community, death, geography, habitation, settlement
- `ك ف ر B013` — ثنية مستورة
  - activated_by_or_with: ء م ن, ش ء م, ص ب ر, ن و ر, و ص د, و ص ي, ي م ن
  - themes: architecture_construction, boundary, concealment_disclosure, geography_landscape, navigation_route, terrain_desert
  - keywords: architecture, barrier, boundary, concealment, geography, shelter, terrain
- `ك ف ر B014` — خضوع متطامن
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: authority_governance, body, communication, hierarchy_status, religion_worship, ritual
  - keywords: body, hierarchy, obedience, ritual, status, submission
- `ك ف ر B015` — تاج يغطي
  - activated_by_or_with: ء م ن, ص ب ر, ص ح ب, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: authority_governance, force_power, hierarchy_status, ornament_beauty, pattern_marking, ritual, textile_clothing
  - keywords: adornment, authority, power, status

### ء ي ي

- `ء ي ي B001` — تمهل وانتظار
  - activated_by_or_with: ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: capacity_ability, cognition, motion, physiology, place_location, sequence_cycle, time
  - keywords: motion, settlement, temporality, time
- `ء ي ي B002` — تعمد آية الشخص
  - activated_by_or_with: ء م ن, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: agency_action, identity_personhood, memory_attention, motion, orientation_direction, perception, posture_embodiment, reasoning_decision, rhetoric_discourse
  - keywords: agency, attention, identity, orientation, perception, reference
- `ء ي ي B003` — علامة ظاهرة
  - activated_by_or_with: ء م ن, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: belief_revelation, communication, household_community, identity_personhood, light_darkness, proof_uncertainty
  - keywords: communication, community, identity, revelation
- `ء ي ي B004` — أي للسؤال والتعيين
  - activated_by_or_with: ء م ن, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: grammar_expression, knowledge_learning, language_speech, naming_classification, proof_uncertainty, reasoning_decision, rhetoric_discourse
  - keywords: classification, deixis, grammar, reference, uncertainty
- `ء ي ي B005` — إيا عماد للضمير
  - activated_by_or_with: ء م ن, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: communication, grammar_expression, identity_personhood, material, rhetoric_discourse
  - keywords: address, deixis, grammar, reference
- `ء ي ي B006` — أيان للزمان
  - activated_by_or_with: ء م ن, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي
  - themes: calendar_season, communication, grammar_expression, knowledge_learning, naming_classification, proof_uncertainty, rhetoric_discourse, sequence_cycle, time
  - keywords: classification, grammar, reference, sequence, time, uncertainty
- `ء ي ي B007` — كأين لعدد كثير
  - activated_by_or_with: ء م ن, ص ب ر, ك ف ر, ك و ن
  - themes: grammar_expression, measurement, quantity_number
  - keywords: grammar, measure, quantity
- `ء ي ي B008` — أي وأيا للنداء
  - activated_by_or_with: ء م ن, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: communication, grammar_expression, language_speech, memory_attention, social_relations
  - keywords: address, attention, communication, deixis, sociality, speech
- `ء ي ي B009` — أي مفسرة
  - activated_by_or_with: ء م ن, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: communication, knowledge_learning, language_speech, naming_classification, reasoning_decision, rhetoric_discourse
  - keywords: communication, discourse, instruction
- `ء ي ي B010` — إي افتتاح للقسم
  - activated_by_or_with: ء م ن, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: communication, emotion, language_speech, law, obligation_contract, proof_uncertainty, religion_worship, rhetoric_discourse, testimony_witness
  - keywords: discourse, law, religion, speech, testimony

### ش ء م

- `ش ء م B001` — جانب الشمال والميسرة
  - activated_by_or_with: ء ي ي, ر ح م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, ي م ن
  - themes: body, navigation_route, orientation_direction, place_location, space
  - keywords: body, location, navigation, orientation, space
- `ش ء م B002` — الشأم جهة وبلاد
  - activated_by_or_with: ء ي ي, ر ح م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص د, و ص ي, ي م ن
  - themes: boundary, geography_landscape, household_community, identity_personhood, migration_displacement, place_location, social_relations
  - keywords: belonging, geography, identity, migration, place, settlement
- `ش ء م B003` — الشؤم والنحس
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: abundance_scarcity, belief_revelation, danger_harm, emotion, reasoning_decision, religion_worship, suffering_hardship
  - keywords: adversity, belief, causality, disaster, emotion, fortune, religion

### ن و ر

- `ن و ر B001` — الضياء والإضاءة
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, و ص ي, ي م ن
  - themes: belief_revelation, perception, proof_uncertainty
  - keywords: guidance, perception, revelation, visibility
- `ن و ر B002` — النار المتقدة والسمة بها
  - activated_by_or_with: ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, و ص ي, ي م ن
  - themes: animal, fire_heat, identity_personhood, livestock, naming_classification, pattern_marking
  - keywords: animal, identity, livestock, marking
- `ن و ر B003` — تنور النار من بعيد
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, و ص د, و ص ي, ي م ن
  - themes: communication, knowledge_learning, navigation_route, perception, protection_security
  - keywords: navigation, perception
- `ن و ر B004` — نور الشجر وزهره
  - activated_by_or_with: ء ي ي, ر ح م, ص ب ر, ص ح ب, ك ف ر, و ص د, و ص ي, ي م ن
  - themes: calendar_season, change_transition, growth_decay, ornament_beauty, plant_vegetation, reproduction_birth
  - keywords: botany, fertility, growth, season
- `ن و ر B005` — المنار والمنارة الظاهرة
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, و ص د, و ص ي, ي م ن
  - themes: architecture_construction, belief_revelation, boundary, communication, geography_landscape, navigation_route, religion_worship
  - keywords: architecture, boundary, guidance, navigation, worship
- `ن و ر B006` — النِّفار وقلة الثبات
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ص ب ر, ص ح ب, ك ف ر, ك و ن, و ص د, و ص ي, ي م ن
  - themes: agency_action, animal, control_restraint, ethics_morality
  - keywords: animal, ethics
- `ن و ر B007` — النائرة بين القوم
  - activated_by_or_with: ء م ن, ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, و ص د, و ص ي, ي م ن
  - themes: conflict, emotion, kinship, social_relations, violence_warfare
  - keywords: conflict, emotion, society, violence
- `ن و ر B008` — دخان الوشم والكحل
  - activated_by_or_with: ء م ن, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, و ص د, ي م ن
  - themes: body, fire_heat, health_medicine, ornament_beauty, ritual, substance_texture, writing_text
  - keywords: adornment, body, cosmetic, cosmetics, medicine, pigment, ritual
- `ن و ر B009` — النُّورَة المطلية
  - activated_by_or_with: ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, و ص د, ي م ن
  - themes: body, ornament_beauty, substance_texture
  - keywords: body, cosmetic, cosmetics
- `ن و ر B010` — التلبيس على الغير
  - activated_by_or_with: ء م ن, ء ي ي, ص ب ر, ص ح ب, ك ف ر, ك و ن, و ص ي
  - themes: cognition, communication, knowledge_learning, perception, proof_uncertainty, rhetoric_discourse
  - keywords: communication, epistemology, perception, uncertainty
- `ن و ر B011` — وضوح النِّير وبروزه
  - activated_by_or_with: ء ي ي, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, و ص ي, ي م ن
  - themes: agriculture, navigation_route, pattern_marking, perception, space, textile_clothing, tools_equipment, transport
  - keywords: agriculture, marking, textile, topology, transport, visibility

### و ص د

- `و ص د B001` — إطباق الباب وإحكام إغلاقه
  - activated_by_or_with: ء م ن, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: architecture_construction, boundary, containment_access, control_restraint, protection_security
  - keywords: access, architecture, boundary, enclosure, protection
- `و ص د B002` — فناء البيت أو بابه المتصل بالربع
  - activated_by_or_with: ء م ن, ء ي ي, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: architecture_construction, boundary, containment_access, place_location
  - keywords: access, architecture, boundary, habitation, proximity, settlement
- `و ص د B003` — وصيدة حجرية للمال في الجبل
  - activated_by_or_with: ء م ن, ر ح م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: architecture_construction, containment_access, husbandry, protection_security, terrain_desert, wealth_property
  - keywords: architecture, enclosure, protection, shelter, terrain
- `و ص د B004` — نبات متقارب الأصول
  - activated_by_or_with: ء ي ي, ر ح م, ش ء م, ص ب ر, ص ح ب, ك ف ر, ك و ن, ن و ر, و ص ي, ي م ن
  - themes: earth_geology, form_structure, growth_decay, habitat_ecology, place_location, plant_vegetation, social_relations, substance_texture
  - keywords: botany, earth, ecology, growth, proximity, vegetation

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
