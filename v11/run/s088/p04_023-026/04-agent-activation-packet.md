# v11 Activation Packet — S88:23-26

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_23: إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- verse_24: فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- verse_25: إِنَّ إِلَيْنَآ إِيَابَهُمْ
- verse_26: ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم

Full copied source text is available in `00-surah-text.json`.

## Surface roots

و ل ي → ك ف ر → ع ذ ب → ء ل ه → ك ب ر → ء و ب → ح س ب

## Branch inventory summary

- و ل ي: 16 branches (15 with Qnet bridge-theme nodes; 1 Furūq-only)
- ك ف ر: 15 branches (15 with Qnet bridge-theme nodes; 0 Furūq-only)
- ع ذ ب: 9 branches (9 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء ل ه: 2 branches (2 with Qnet bridge-theme nodes; 0 Furūq-only)
- ك ب ر: 13 branches (12 with Qnet bridge-theme nodes; 1 Furūq-only)
- ء و ب: 7 branches (5 with Qnet bridge-theme nodes; 2 Furūq-only)
- ح س ب: 10 branches (8 with Qnet bridge-theme nodes; 2 Furūq-only)

## QAC-first root resolution audit

- و ل ي | qac_keys=ولي | status=resolved | matches=root_001684
- ك ف ر | qac_keys=كفر | status=resolved | matches=root_001307
- ع ذ ب | qac_keys=عذب | status=resolved | matches=root_000994
- ء ل ه | qac_keys=ءله | status=resolved | matches=root_000047
- ك ب ر | qac_keys=كبر | status=resolved | matches=root_001281
- ء و ب | qac_keys=ءوب | status=resolved | matches=root_000065
- ح س ب | qac_keys=حسب | status=resolved | matches=root_000318

## Top candidate bridges

- `و ل ي B005` ↔ `ك ب ر B008` | score_hint=25 | discovery_hint=20 | themes=family, hierarchy_status, support_dependence, wealth_property | keywords=family, inheritance, patronage, status | q2=—
- `ك ف ر B009` ↔ `ك ب ر B007` | score_hint=24 | discovery_hint=14 | themes=ethics_morality, justice_judgment, law, religion_worship | keywords=accountability, ethics, law, religion | q2=—
- `ك ب ر B013` ↔ `ء و ب B007` | score_hint=24 | discovery_hint=15 | themes=light_darkness, sequence_cycle, sky_astronomy, time | keywords=astronomy, cycle, daylight, time | q2=—
- `ك ب ر B008` ↔ `ح س ب B004` | score_hint=20 | discovery_hint=14 | themes=hierarchy_status, kinship, marriage_genealogy, wealth_property | keywords=genealogy, kinship, status | q2=—
- `و ل ي B005` ↔ `ك ف ر B006` | score_hint=18 | discovery_hint=13 | themes=hierarchy_status, household_community, law | keywords=community, law, status | q2=—
- `ك ف ر B006` ↔ `ك ب ر B007` | score_hint=18 | discovery_hint=13 | themes=justice_judgment, law, religion_worship | keywords=judgment, law, religion | q2=—
- `ك ف ر B009` ↔ `ح س ب B006` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, justice_judgment, law | keywords=accountability, ethics, law | q2=—
- `ك ف ر B015` ↔ `ك ب ر B005` | score_hint=18 | discovery_hint=14 | themes=authority_governance, force_power, hierarchy_status | keywords=authority, kingship, power | q2=—
- `ع ذ ب B008` ↔ `ح س ب B004` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, hierarchy_status, honor_shame | keywords=ethics, reputation, status | q2=—
- `ك ب ر B007` ↔ `ح س ب B006` | score_hint=18 | discovery_hint=13 | themes=ethics_morality, justice_judgment, law | keywords=accountability, ethics, law | q2=—
- `و ل ي B003` ↔ `ك ب ر B002` | score_hint=16 | discovery_hint=13 | themes=authority_governance, obligation_contract | keywords=governance, responsibility, stewardship | q2=—
- `و ل ي B003` ↔ `ك ف ر B007` | score_hint=14 | discovery_hint=13 | themes=authority_governance, force_power, obligation_contract | keywords=power, responsibility | q2=—
- `ك ف ر B003` ↔ `ء ل ه B001` | score_hint=14 | discovery_hint=11 | themes=authority_governance, belief_revelation, religion_worship | keywords=religion, theology | q2=—
- `ك ف ر B006` ↔ `ء ل ه B001` | score_hint=14 | discovery_hint=11 | themes=authority_governance, belief_revelation, religion_worship | keywords=authority, religion | q2=—
- `ك ف ر B011` ↔ `ع ذ ب B001` | score_hint=14 | discovery_hint=11 | themes=perception, purity_cleansing, water_hydrology | keywords=purity, water | q2=—
- `ء ل ه B001` ↔ `ك ب ر B006` | score_hint=14 | discovery_hint=11 | themes=authority_governance, belief_revelation, religion_worship | keywords=authority, theology | q2=—
- `و ل ي B001` ↔ `ع ذ ب B004` | score_hint=13 | discovery_hint=15 | themes=boundary, space | keywords=boundary, space | q2=—
- `و ل ي B004` ↔ `ك ف ر B005` | score_hint=13 | discovery_hint=17 | themes=conflict, trust_loyalty | keywords=alliance, conflict | q2=—
- `ك ب ر B001` ↔ `ح س ب B001` | score_hint=13 | discovery_hint=16 | themes=measurement, quantity_number | keywords=measurement, quantity | q2=—
- `و ل ي B002` ↔ `ك ب ر B004` | score_hint=12 | discovery_hint=12 | themes=stability_endurance, time | keywords=continuity, time | q2=—
- `و ل ي B002` ↔ `ح س ب B001` | score_hint=12 | discovery_hint=11 | themes=politics_order, sequence_cycle | keywords=chronology, order | q2=—
- `و ل ي B003` ↔ `ح س ب B006` | score_hint=12 | discovery_hint=12 | themes=authority_governance, law | keywords=governance, law | q2=—
- `و ل ي B006` ↔ `ء و ب B001` | score_hint=12 | discovery_hint=11 | themes=motion, orientation_direction | keywords=movement, orientation | q2=—
- `و ل ي B010` ↔ `ك ف ر B008` | score_hint=12 | discovery_hint=14 | themes=agriculture, reproduction_birth | keywords=agriculture, fertility | q2=—
- `و ل ي B011` ↔ `ء و ب B003` | score_hint=12 | discovery_hint=12 | themes=animal, travel | keywords=animal, travel | q2=—
- `و ل ي B012` ↔ `ك ب ر B011` | score_hint=12 | discovery_hint=13 | themes=conflict, force_power | keywords=competition, power | q2=—
- `و ل ي B013` ↔ `ك ف ر B007` | score_hint=12 | discovery_hint=12 | themes=agency_action, ethics_morality | keywords=agency, morality | q2=—
- `و ل ي B015` ↔ `ك ف ر B008` | score_hint=12 | discovery_hint=14 | themes=agriculture, growth_decay | keywords=agriculture, growth | q2=—
- `و ل ي B015` ↔ `ع ذ ب B003` | score_hint=12 | discovery_hint=12 | themes=boundary, control_restraint | keywords=discipline, separation | q2=—
- `و ل ي B016` ↔ `ك ف ر B010` | score_hint=12 | discovery_hint=14 | themes=growth_decay, plant_vegetation | keywords=botany, fruit | q2=—
- `ك ف ر B002` ↔ `ء و ب B006` | score_hint=12 | discovery_hint=12 | themes=calendar_season, light_darkness | keywords=darkness, night | q2=—
- `ك ف ر B003` ↔ `ك ب ر B007` | score_hint=12 | discovery_hint=12 | themes=justice_judgment, religion_worship | keywords=judgment, religion | q2=—
- `ك ف ر B004` ↔ `ع ذ ب B008` | score_hint=12 | discovery_hint=12 | themes=ethics_morality, hospitality_welfare | keywords=ethics, virtue | q2=—
- `ك ف ر B006` ↔ `ح س ب B004` | score_hint=12 | discovery_hint=13 | themes=hierarchy_status, identity_personhood | keywords=identity, status | q2=—
- `ك ف ر B008` ↔ `ك ب ر B013` | score_hint=12 | discovery_hint=13 | themes=growth_decay, sequence_cycle | keywords=cycle, growth | q2=—
- `ك ف ر B013` ↔ `ع ذ ب B004` | score_hint=12 | discovery_hint=12 | themes=architecture_construction, boundary | keywords=architecture, boundary | q2=—
- `ك ب ر B003` ↔ `ح س ب B002` | score_hint=12 | discovery_hint=12 | themes=cognition, perception | keywords=cognition, perception | q2=—
- `ك ف ر B001` ↔ `ع ذ ب B004` | score_hint=11 | discovery_hint=15 | themes=boundary, containment_access, protection_security | keywords=protection | q2=—
- `و ل ي B006` ↔ `ء و ب B003` | score_hint=10 | discovery_hint=12 | themes=motion | keywords=motion, movement | q2=—
- `ك ف ر B009` ↔ `ح س ب B004` | score_hint=10 | discovery_hint=12 | themes=ethics_morality | keywords=ethics, morality | q2=—
- `و ل ي B001` ↔ `ك ف ر B012` | score_hint=10 | discovery_hint=10 | themes=boundary, place_location, social_relations | keywords=boundary | q2=—
- `و ل ي B004` ↔ `ك ف ر B006` | score_hint=10 | discovery_hint=11 | themes=belief_revelation, household_community, religion_worship | keywords=community | q2=—
- `و ل ي B008` ↔ `ح س ب B006` | score_hint=10 | discovery_hint=11 | themes=ethics_morality, justice_judgment, law | keywords=justice | q2=—
- `و ل ي B010` ↔ `ك ف ر B002` | score_hint=10 | discovery_hint=11 | themes=calendar_season, geography_landscape, water_hydrology | keywords=water | q2=—
- `و ل ي B013` ↔ `ك ف ر B004` | score_hint=10 | discovery_hint=12 | themes=commerce_exchange, ethics_morality, hospitality_welfare | keywords=gift | q2=—
- `و ل ي B016` ↔ `ك ف ر B008` | score_hint=10 | discovery_hint=14 | themes=agriculture, growth_decay, plant_vegetation | keywords=agriculture | q2=—
- `ك ف ر B003` ↔ `ك ب ر B006` | score_hint=10 | discovery_hint=11 | themes=authority_governance, belief_revelation, religion_worship | keywords=theology | q2=—
- `ك ف ر B006` ↔ `ك ب ر B006` | score_hint=10 | discovery_hint=11 | themes=authority_governance, belief_revelation, religion_worship | keywords=authority | q2=—
- `ك ف ر B006` ↔ `ح س ب B006` | score_hint=10 | discovery_hint=11 | themes=authority_governance, justice_judgment, law | keywords=law | q2=—
- `ك ف ر B007` ↔ `ك ب ر B002` | score_hint=10 | discovery_hint=11 | themes=agency_action, authority_governance, obligation_contract | keywords=responsibility | q2=—
- `ك ف ر B014` ↔ `ء ل ه B001` | score_hint=10 | discovery_hint=10 | themes=authority_governance, religion_worship, ritual | keywords=submission | q2=—
- `ك ب ر B013` ↔ `ء و ب B006` | score_hint=10 | discovery_hint=11 | themes=calendar_season, light_darkness, time | keywords=time | q2=—
- `ك ب ر B013` ↔ `ح س ب B001` | score_hint=10 | discovery_hint=12 | themes=measurement, sequence_cycle, sky_astronomy | keywords=astronomy | q2=—
- `ك ف ر B013` ↔ `ء و ب B004` | score_hint=9 | discovery_hint=15 | themes=geography_landscape, navigation_route | keywords=geography | q2=—
- `ع ذ ب B005` ↔ `ك ب ر B007` | score_hint=9 | discovery_hint=15 | themes=justice_judgment, punishment_sanction | keywords=punishment | q2=—
- `و ل ي B002` ↔ `ك ب ر B008` | score_hint=8 | discovery_hint=11 | themes=politics_order, sequence_cycle | keywords=order | q2=—
- `و ل ي B002` ↔ `ك ب ر B013` | score_hint=8 | discovery_hint=11 | themes=sequence_cycle, time | keywords=time | q2=—
- `و ل ي B002` ↔ `ء و ب B007` | score_hint=8 | discovery_hint=11 | themes=sequence_cycle, time | keywords=time | q2=—
- `و ل ي B003` ↔ `ك ف ر B006` | score_hint=8 | discovery_hint=11 | themes=authority_governance, law | keywords=law | q2=—
- `و ل ي B003` ↔ `ك ف ر B015` | score_hint=8 | discovery_hint=12 | themes=authority_governance, force_power | keywords=power | q2=—
- `و ل ي B003` ↔ `ك ب ر B005` | score_hint=8 | discovery_hint=12 | themes=authority_governance, force_power | keywords=power | q2=—
- `و ل ي B004` ↔ `ك ف ر B003` | score_hint=8 | discovery_hint=11 | themes=belief_revelation, religion_worship | keywords=faith | q2=—
- `و ل ي B004` ↔ `ك ب ر B003` | score_hint=8 | discovery_hint=11 | themes=emotion, religion_worship | keywords=emotion | q2=—
- `و ل ي B004` ↔ `ك ب ر B010` | score_hint=8 | discovery_hint=11 | themes=conflict, emotion | keywords=emotion | q2=—
- `و ل ي B004` ↔ `ح س ب B008` | score_hint=8 | discovery_hint=12 | themes=household_community, support_dependence | keywords=support | q2=—
- `و ل ي B005` ↔ `ك ف ر B012` | score_hint=8 | discovery_hint=11 | themes=household_community, place_location | keywords=community | q2=—
- `و ل ي B005` ↔ `ء و ب B001` | score_hint=8 | discovery_hint=10 | themes=household_community, place_location | keywords=residence | q2=—
- `و ل ي B005` ↔ `ح س ب B004` | score_hint=8 | discovery_hint=12 | themes=hierarchy_status, wealth_property | keywords=status | q2=—
- `و ل ي B006` ↔ `ك ف ر B005` | score_hint=8 | discovery_hint=11 | themes=obligation_contract, social_relations | keywords=relation | q2=—
- `و ل ي B006` ↔ `ك ف ر B007` | score_hint=8 | discovery_hint=11 | themes=authority_governance, obligation_contract | keywords=obedience | q2=—
- `و ل ي B006` ↔ `ء و ب B004` | score_hint=8 | discovery_hint=11 | themes=motion, orientation_direction | keywords=orientation | q2=—
- `و ل ي B007` ↔ `ك ف ر B007` | score_hint=8 | discovery_hint=11 | themes=authority_governance, control_restraint | keywords=obedience | q2=—
- `و ل ي B007` ↔ `ك ف ر B012` | score_hint=8 | discovery_hint=12 | themes=measurement, social_relations | keywords=distance | q2=—
- `و ل ي B007` ↔ `ك ف ر B014` | score_hint=8 | discovery_hint=11 | themes=authority_governance, communication | keywords=obedience | q2=—
- `و ل ي B008` ↔ `ك ب ر B002` | score_hint=8 | discovery_hint=12 | themes=provision_resource, value_quality | keywords=allocation | q2=—
- `و ل ي B011` ↔ `ع ذ ب B006` | score_hint=8 | discovery_hint=11 | themes=textile_clothing, tools_equipment | keywords=textile | q2=—
- `و ل ي B011` ↔ `ح س ب B008` | score_hint=8 | discovery_hint=11 | themes=textile_clothing, tools_equipment | keywords=textile | q2=—
- `و ل ي B012` ↔ `ك ف ر B007` | score_hint=8 | discovery_hint=12 | themes=control_restraint, force_power | keywords=power | q2=—
- `و ل ي B012` ↔ `ء و ب B001` | score_hint=8 | discovery_hint=10 | themes=change_transition, motion | keywords=movement | q2=—
- `و ل ي B015` ↔ `ك ب ر B013` | score_hint=8 | discovery_hint=13 | themes=growth_decay, life_stage_aging | keywords=growth | q2=—

## Per-root candidate activations

### و ل ي

- `و ل ي B001` — قرب ودنو بلا فاصل
  - activated_by_or_with: ء و ب, ع ذ ب, ك ف ر
  - themes: boundary, place_location, social_relations, space
  - keywords: boundary, relation, space
- `و ل ي B002` — تتابع شيء بعد شيء
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ب ر, ك ف ر
  - themes: politics_order, sequence_cycle, stability_endurance, time
  - keywords: chronology, continuity, order, rhythm, time
- `و ل ي B003` — تولي الأمر والقيام عليه
  - activated_by_or_with: ء ل ه, ء و ب, ح س ب, ع ذ ب, ك ب ر, ك ف ر
  - themes: authority_governance, force_power, hospitality_welfare, law, obligation_contract
  - keywords: governance, law, power, responsibility, stewardship
- `و ل ي B004` — محبة ونصرة وموالاة
  - activated_by_or_with: ء ل ه, ء و ب, ح س ب, ع ذ ب, ك ب ر, ك ف ر
  - themes: belief_revelation, conflict, emotion, household_community, religion_worship, support_dependence, trust_loyalty
  - keywords: alliance, community, conflict, devotion, emotion, faith, support
- `و ل ي B005` — ولاء قرابة وعتق وجوار
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ب ر, ك ف ر
  - themes: control_restraint, family, hierarchy_status, household_community, law, place_location, support_dependence, wealth_property
  - keywords: community, family, inheritance, law, patronage, residence, status
- `و ل ي B006` — تولية الوجه والإقبال
  - activated_by_or_with: ء ل ه, ء و ب, ح س ب, ع ذ ب, ك ب ر, ك ف ر
  - themes: authority_governance, memory_attention, motion, obligation_contract, orientation_direction, perception, social_relations
  - keywords: attention, motion, movement, obedience, orientation, perception, relation
- `و ل ي B007` — الإدبار والإعراض
  - activated_by_or_with: ء ل ه, ء و ب, ح س ب, ع ذ ب, ك ب ر, ك ف ر
  - themes: authority_governance, communication, control_restraint, loss_absence, measurement, memory_attention, motion, social_relations
  - keywords: attention, distance, movement, obedience
- `و ل ي B008` — الأولوية والاستحقاق
  - activated_by_or_with: ح س ب, ع ذ ب, ك ب ر, ك ف ر
  - themes: ethics_morality, hierarchy_status, justice_judgment, law, provision_resource, value_quality
  - keywords: allocation, hierarchy, justice, value
- `و ل ي B009` — أولى لك تهديد ووعيد
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `و ل ي B010` — مطر يلي الوسمي
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ب ر, ك ف ر
  - themes: agriculture, calendar_season, geography_landscape, reproduction_birth, water_hydrology, weather_climate
  - keywords: agriculture, fertility, water, weather
- `و ل ي B011` — ولية تحت الرحل
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ب ر, ك ف ر
  - themes: animal, textile_clothing, tools_equipment, transport, travel
  - keywords: animal, textile, travel
- `و ل ي B012` — استيلاء وبلوغ غاية
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ب ر, ك ف ر
  - themes: change_transition, conflict, control_restraint, force_power, motion, value_quality, wealth_property
  - keywords: competition, control, movement, ownership, power
- `و ل ي B013` — إيلاء وإسناد معروف أو شر
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ب ر, ك ف ر
  - themes: agency_action, commerce_exchange, danger_harm, ethics_morality, hospitality_welfare, motion
  - keywords: agency, exchange, gift, harm, morality
- `و ل ي B014` — تولية البيع
  - activated_by_or_with: ء ل ه, ح س ب, ك ب ر, ك ف ر
  - themes: commerce_exchange, obligation_contract, value_quality, wealth_property
  - keywords: exchange, ownership, value
- `و ل ي B015` — موالاة صغار النعم عن كبارها
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ب ر, ك ف ر
  - themes: agriculture, animal, boundary, control_restraint, growth_decay, knowledge_learning, life_stage_aging
  - keywords: agriculture, animal, discipline, growth, maturation, separation
- `و ل ي B016` — ولي الرطب وتولى إذا هاج
  - activated_by_or_with: ح س ب, ع ذ ب, ك ب ر, ك ف ر
  - themes: agriculture, growth_decay, life_stage_aging, plant_vegetation, substance_texture, visual_appearance
  - keywords: agriculture, botany, color, fruit, maturation

### ك ف ر

- `ك ف ر B001` — ستر وتغطية
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ب ر, و ل ي
  - themes: boundary, concealment_disclosure, containment_access, perception, protection_security, textile_clothing
  - keywords: barrier, concealment, protection
- `ك ف ر B002` — غمر ساتر
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ب ر, و ل ي
  - themes: boundary, calendar_season, concealment_disclosure, geography_landscape, habitat_ecology, light_darkness, sky_astronomy, water_hydrology
  - keywords: boundary, concealment, darkness, night, water
- `ك ف ر B003` — حجب الحق
  - activated_by_or_with: ء ل ه, ح س ب, ع ذ ب, ك ب ر, و ل ي
  - themes: authority_governance, belief_revelation, justice_judgment, proof_uncertainty, religion_worship
  - keywords: doctrine, faith, judgment, obedience, religion, theology
- `ك ف ر B004` — ستر النعمة
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ب ر, و ل ي
  - themes: commerce_exchange, ethics_morality, finance_debt, hospitality_welfare
  - keywords: ethics, gift, virtue
- `ك ف ر B005` — تبرؤ وتنصل
  - activated_by_or_with: ء ل ه, ء و ب, ح س ب, ع ذ ب, ك ب ر, و ل ي
  - themes: conflict, identity_personhood, language_speech, obligation_contract, social_relations, trust_loyalty
  - keywords: alliance, conflict, identity, relation, responsibility, sociality, speech
- `ك ف ر B006` — نسبة إلى الكفر
  - activated_by_or_with: ء ل ه, ء و ب, ح س ب, ع ذ ب, ك ب ر, و ل ي
  - themes: authority_governance, belief_revelation, hierarchy_status, household_community, identity_personhood, justice_judgment, language_speech, law, religion_worship
  - keywords: authority, community, doctrine, identity, judgment, law, religion, speech, status
- `ك ف ر B007` — إلجاء إلى العصيان
  - activated_by_or_with: ء ل ه, ح س ب, ع ذ ب, ك ب ر, و ل ي
  - themes: agency_action, authority_governance, control_restraint, desire_appetite, ethics_morality, force_power, obligation_contract
  - keywords: agency, morality, obedience, power, responsibility
- `ك ف ر B008` — تغطية البذر
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ب ر, و ل ي
  - themes: agriculture, concealment_disclosure, earth_geology, food_nutrition, growth_decay, plant_vegetation, reproduction_birth, sequence_cycle
  - keywords: agriculture, concealment, cycle, fertility, growth
- `ك ف ر B009` — محو الإثم بتغطيته
  - activated_by_or_with: ء ل ه, ء و ب, ح س ب, ع ذ ب, ك ب ر, و ل ي
  - themes: change_transition, ethics_morality, health_medicine, justice_judgment, law, purity_cleansing, religion_worship
  - keywords: accountability, ethics, law, morality, purity, religion, restoration
- `ك ف ر B010` — كمام الثمر
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ب ر, و ل ي
  - themes: growth_decay, plant_vegetation, protection_security, reproduction_birth
  - keywords: botany, fertility, fruit, growth, plant, protection
- `ك ف ر B011` — كافور طيب
  - activated_by_or_with: ح س ب, ع ذ ب, ك ب ر, و ل ي
  - themes: perception, plant_vegetation, purity_cleansing, water_hydrology, wealth_property
  - keywords: botany, plant, purity, water
- `ك ف ر B012` — موضع منقطع
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ب ر, و ل ي
  - themes: boundary, geography_landscape, household_community, measurement, mortality_death, place_location, social_relations
  - keywords: boundary, community, distance, geography
- `ك ف ر B013` — ثنية مستورة
  - activated_by_or_with: ء و ب, ع ذ ب, و ل ي
  - themes: architecture_construction, boundary, concealment_disclosure, geography_landscape, navigation_route
  - keywords: architecture, barrier, boundary, concealment, geography
- `ك ف ر B014` — خضوع متطامن
  - activated_by_or_with: ء ل ه, ح س ب, ع ذ ب, ك ب ر, و ل ي
  - themes: authority_governance, body, communication, hierarchy_status, religion_worship, ritual
  - keywords: body, hierarchy, obedience, status, submission
- `ك ف ر B015` — تاج يغطي
  - activated_by_or_with: ء ل ه, ح س ب, ع ذ ب, ك ب ر, و ل ي
  - themes: authority_governance, force_power, hierarchy_status, ornament_beauty, ritual, textile_clothing
  - keywords: authority, kingship, power, status

### ع ذ ب

- `ع ذ ب B001` — العذوبة والطيب في الماء والمطعوم
  - activated_by_or_with: ح س ب, ك ب ر, ك ف ر, و ل ي
  - themes: desire_appetite, food_nutrition, perception, purity_cleansing, water_hydrology
  - keywords: consumption, purity, water
- `ع ذ ب B002` — العذوب امتناع الجسد عن الأكل والشرب
  - activated_by_or_with: ء ل ه, ء و ب, ح س ب, ك ب ر, ك ف ر, و ل ي
  - themes: desire_appetite, food_nutrition, loss_absence, physiology, religion_worship, stability_endurance
  - keywords: consumption, endurance, physiology
- `ع ذ ب B003` — الكف والمنع والفطام عن الشيء
  - activated_by_or_with: ح س ب, ك ب ر, ك ف ر, و ل ي
  - themes: boundary, control_restraint, law, rhetoric_discourse
  - keywords: boundary, control, discipline, separation
- `ع ذ ب B004` — العذوب المكشوف للسماء
  - activated_by_or_with: ء و ب, ح س ب, ك ف ر, و ل ي
  - themes: architecture_construction, boundary, containment_access, danger_harm, habitat_ecology, protection_security, space, weather_climate
  - keywords: architecture, boundary, protection, space, weather
- `ع ذ ب B005` — العذاب إيلام وعقوبة
  - activated_by_or_with: ح س ب, ك ب ر, ك ف ر, و ل ي
  - themes: control_restraint, danger_harm, justice_judgment, punishment_sanction, suffering_hardship, violence_warfare
  - keywords: harm, justice, punishment, suffering
- `ع ذ ب B006` — العذبة طرف أو علاقة متدلية
  - activated_by_or_with: ء و ب, ح س ب, ك ب ر, ك ف ر, و ل ي
  - themes: anatomy, ornament_beauty, social_relations, textile_clothing, tools_equipment
  - keywords: anatomy, textile
- `ع ذ ب B007` — العذبة شوائب الماء أو سطحه
  - activated_by_or_with: ك ب ر, ك ف ر, و ل ي
  - themes: earth_geology, habitat_ecology, purity_cleansing, stability_endurance, substance_texture, water_hydrology
  - keywords: water
- `ع ذ ب B008` — العذبي كريم الأخلاق
  - activated_by_or_with: ء و ب, ح س ب, ك ب ر, ك ف ر, و ل ي
  - themes: ethics_morality, hierarchy_status, honor_shame, hospitality_welfare, social_relations
  - keywords: ethics, generosity, reputation, sociality, status, virtue
- `ع ذ ب B009` — العذابة والرحم والخرج بعد الولد
  - activated_by_or_with: ء و ب, ح س ب, ك ب ر, ك ف ر, و ل ي
  - themes: anatomy, change_transition, health_medicine, kinship, physiology, reproduction_birth, substance_texture
  - keywords: anatomy, kinship, medicine, physiology

### ء ل ه

- `ء ل ه B001` — التعبد والمعبود
  - activated_by_or_with: ح س ب, ع ذ ب, ك ب ر, ك ف ر, و ل ي
  - themes: authority_governance, belief_revelation, religion_worship, ritual
  - keywords: authority, religion, submission, theology
- `ء ل ه B002` — اسم الله في القسم والنداء
  - activated_by_or_with: ع ذ ب, ك ب ر, ك ف ر, و ل ي
  - themes: language_speech, naming_classification, obligation_contract, religion_worship
  - keywords: devotion, speech

### ك ب ر

- `ك ب ر B001` — العظم خلاف الصغر
  - activated_by_or_with: ح س ب, ك ف ر, و ل ي
  - themes: growth_decay, measurement, quantity_number
  - keywords: growth, measurement, quantity
- `ك ب ر B002` — معظم الأمر
  - activated_by_or_with: ء ل ه, ء و ب, ح س ب, ع ذ ب, ك ف ر, و ل ي
  - themes: agency_action, authority_governance, economy, obligation_contract, provision_resource, sequence_cycle, suffering_hardship, value_quality
  - keywords: allocation, burden, governance, obligation, responsibility, stewardship
- `ك ب ر B003` — إعظام الشيء في الصدر
  - activated_by_or_with: ء ل ه, ح س ب, ع ذ ب, ك ف ر, و ل ي
  - themes: cognition, emotion, honor_shame, perception, religion_worship, value_quality
  - keywords: cognition, emotion, honor, perception
- `ك ب ر B004` — كبر السن والقدم
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ف ر, و ل ي
  - themes: growth_decay, health_medicine, life_stage_aging, mortality_death, stability_endurance, time, tools_equipment
  - keywords: artifact, continuity, medicine, time
- `ك ب ر B005` — رفعة الشرف والرئاسة
  - activated_by_or_with: ء ل ه, ح س ب, ع ذ ب, ك ف ر, و ل ي
  - themes: authority_governance, force_power, hierarchy_status, honor_shame, knowledge_learning, marriage_genealogy, politics_order
  - keywords: authority, hierarchy, honor, kingship, power
- `ك ب ر B006` — العظمة والكبرياء
  - activated_by_or_with: ء ل ه, ح س ب, ع ذ ب, ك ف ر, و ل ي
  - themes: authority_governance, belief_revelation, conflict, ethics_morality, honor_shame, religion_worship
  - keywords: authority, ethics, theology
- `ك ب ر B007` — الإثم الكبير والذنوب الكبائر
  - activated_by_or_with: ء ل ه, ح س ب, ع ذ ب, ك ف ر, و ل ي
  - themes: ethics_morality, justice_judgment, law, punishment_sanction, religion_worship
  - keywords: accountability, ethics, judgment, law, punishment, religion
- `ك ب ر B008` — كبر النسب والولادة
  - activated_by_or_with: ء و ب, ح س ب, ع ذ ب, ك ف ر, و ل ي
  - themes: family, hierarchy_status, kinship, marriage_genealogy, politics_order, sequence_cycle, support_dependence, wealth_property
  - keywords: family, genealogy, inheritance, kinship, order, patronage, status
- `ك ب ر B009` — التكبير بقول الله أكبر
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ك ب ر B010` — الكبر مشقة وثقل
  - activated_by_or_with: ء ل ه, ح س ب, ع ذ ب, ك ف ر, و ل ي
  - themes: cognition, communication, conflict, emotion, obligation_contract, stability_endurance, suffering_hardship, transport
  - keywords: burden, emotion, endurance, obligation, psychology, suffering
- `ك ب ر B011` — المكابرة والغلبة
  - activated_by_or_with: ع ذ ب, ك ف ر, و ل ي
  - themes: conflict, force_power, rhetoric_discourse, violence_warfare
  - keywords: competition, conflict, power
- `ك ب ر B012` — الكَبَر طبل
  - activated_by_or_with: ء ل ه, ء و ب, ح س ب, ع ذ ب, ك ف ر, و ل ي
  - themes: agency_action, naming_classification, perception, sequence_cycle, tools_equipment
  - keywords: artifact, rhythm
- `ك ب ر B013` — أكبر النهار
  - activated_by_or_with: ء و ب, ح س ب, ك ف ر, و ل ي
  - themes: calendar_season, growth_decay, life_stage_aging, light_darkness, measurement, sequence_cycle, sky_astronomy, time
  - keywords: astronomy, cycle, daylight, growth, time

### ء و ب

- `ء و ب B001` — الرجوع إلى المآب والموضع
  - activated_by_or_with: ح س ب, ع ذ ب, ك ف ر, و ل ي
  - themes: architecture_construction, change_transition, household_community, migration_displacement, motion, orientation_direction, place_location, protection_security, travel
  - keywords: movement, orientation, residence, restoration, return
- `ء و ب B002` — الرجوع إلى الله بالتوبة
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ء و ب B003` — تردد الجوارح في السير والتأويب
  - activated_by_or_with: ح س ب, ع ذ ب, ك ب ر, ك ف ر, و ل ي
  - themes: anatomy, animal, motion, sequence_cycle, travel
  - keywords: anatomy, animal, motion, movement, rhythm, travel
- `ء و ب B004` — الأوب ناحية يؤتى منها
  - activated_by_or_with: ح س ب, ك ب ر, ك ف ر, و ل ي
  - themes: geography_landscape, migration_displacement, motion, navigation_route, orientation_direction, sequence_cycle, travel
  - keywords: geography, orientation, travel
- `ء و ب B005` — ترجيع التسبيح
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ء و ب B006` — الإتيان ليلا والعودة مع الليل
  - activated_by_or_with: ح س ب, ع ذ ب, ك ب ر, ك ف ر, و ل ي
  - themes: calendar_season, hospitality_welfare, light_darkness, motion, social_relations, time, travel
  - keywords: darkness, night, return, time, travel
- `ء و ب B007` — غروب الشمس إلى مآبها
  - activated_by_or_with: ح س ب, ع ذ ب, ك ب ر, ك ف ر, و ل ي
  - themes: change_transition, light_darkness, loss_absence, orientation_direction, sequence_cycle, sky_astronomy, time
  - keywords: astronomy, cycle, daylight, time

### ح س ب

- `ح س ب B001` — العد والحساب
  - activated_by_or_with: ء و ب, ع ذ ب, ك ب ر, ك ف ر, و ل ي
  - themes: finance_debt, justice_judgment, measurement, politics_order, quantity_number, sequence_cycle, sky_astronomy
  - keywords: accountability, astronomy, chronology, measurement, order, quantity
- `ح س ب B002` — الحسبان والظن
  - activated_by_or_with: ع ذ ب, ك ب ر, ك ف ر, و ل ي
  - themes: cognition, justice_judgment, knowledge_learning, perception, proof_uncertainty, weather_climate
  - keywords: cognition, judgment, perception, psychology
- `ح س ب B003` — الكفاية والإغناء
  - activated_by_or_with: ء و ب, ع ذ ب, ك ب ر, ك ف ر, و ل ي
  - themes: change_transition, economy, hospitality_welfare, provision_resource, support_dependence, value_quality, wealth_property
  - keywords: generosity, support, wealth
- `ح س ب B004` — الحسب والمآثر
  - activated_by_or_with: ع ذ ب, ك ب ر, ك ف ر, و ل ي
  - themes: ethics_morality, hierarchy_status, honor_shame, identity_personhood, kinship, marriage_genealogy, wealth_property
  - keywords: ethics, genealogy, identity, kinship, morality, reputation, status, wealth
- `ح س ب B005` — الاحتساب عند الله
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ح س ب B006` — الحسبة والنظر في الأمر
  - activated_by_or_with: ء ل ه, ع ذ ب, ك ب ر, ك ف ر, و ل ي
  - themes: authority_governance, ethics_morality, justice_judgment, law, politics_order
  - keywords: accountability, ethics, governance, justice, law
- `ح س ب B007` — المرامي والحسبان النازل
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —
- `ح س ب B008` — المحسبة والوسادة
  - activated_by_or_with: ء و ب, ع ذ ب, ك ب ر, ك ف ر, و ل ي
  - themes: health_medicine, household_community, physiology, support_dependence, textile_clothing, tools_equipment
  - keywords: support, textile
- `ح س ب B009` — لون الأحسب والأحسبية
  - activated_by_or_with: ء و ب, ع ذ ب, ك ب ر, ك ف ر, و ل ي
  - themes: anatomy, animal, body, health_medicine, visual_appearance
  - keywords: animal, body, color
- `ح س ب B010` — التحسب والاستخبار
  - activated_by_or_with: ء و ب, ع ذ ب, ك ب ر, ك ف ر, و ل ي
  - themes: cognition, communication, knowledge_learning, proof_uncertainty, protection_security
  - keywords: —

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
