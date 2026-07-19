# v11 Activation Packet — S112:1-None

Bias: recall-first. Preserve latent candidates with labels instead of pruning.

## Arabic surah text

- verse_0 (basmala; part of analysis): بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
- verse_1: قُلْ هُوَ ٱللَّهُ أَحَدٌ
- verse_2: ٱللَّهُ ٱلصَّمَدُ
- verse_3: لَمْ يَلِدْ وَلَمْ يُولَدْ
- verse_4: وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ

Full copied source text is available in `00-surah-text.json`.

## Surface roots

ق و ل → ء ل ه → ء ح د → ص م د → و ل د → ك و ن → ك ف ء

## Branch inventory summary

- ق و ل: 17 branches (16 with Qnet bridge-theme nodes; 1 Furūq-only)
- ء ل ه: 2 branches (2 with Qnet bridge-theme nodes; 0 Furūq-only)
- ء ح د: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- ص م د: 7 branches (7 with Qnet bridge-theme nodes; 0 Furūq-only)
- و ل د: 7 branches (6 with Qnet bridge-theme nodes; 1 Furūq-only)
- ك و ن: 6 branches (6 with Qnet bridge-theme nodes; 0 Furūq-only)
- ك ف ء: 5 branches (5 with Qnet bridge-theme nodes; 0 Furūq-only)

## QAC-first root resolution audit

- ق و ل | qac_keys=قول | status=resolved | matches=root_001272
- ء ل ه | qac_keys=ءله | status=resolved | matches=root_000047
- ء ح د | qac_keys=ءحد | status=resolved | matches=root_000017
- ص م د | qac_keys=صمد | status=resolved | matches=root_000882
- و ل د | qac_keys=ولد | status=resolved | matches=root_001683
- ك و ن | qac_keys=كون | status=resolved | matches=root_001332
- ك ف ء | qac_keys=كفء | status=resolved | matches=root_001305

## Top candidate bridges

- `و ل د B001` ↔ `و ل د B002` | score_hint=31 | discovery_hint=16 | themes=family, kinship, marriage_genealogy, motion, reproduction_birth | keywords=descent, family, genealogy, kinship, reproduction | q2=—
- `ق و ل B008` ↔ `ص م د B003` | score_hint=13 | discovery_hint=16 | themes=craft, tools_equipment | keywords=craft, tool | q2=—
- `ك و ن B003` ↔ `ك ف ء B004` | score_hint=7 | discovery_hint=16 | themes=protection_security | keywords=protection | q2=—
- `ق و ل B008` ↔ `ص م د B002` | score_hint=7 | discovery_hint=15 | themes=material | keywords=material | q2=—
- `ص م د B001` ↔ `ك ف ء B002` | score_hint=7 | discovery_hint=14 | themes=orientation_direction | keywords=orientation | q2=—
- `ق و ل B010` ↔ `ك و ن B004` | score_hint=14 | discovery_hint=13 | themes=authority_governance, control_restraint, force_power | keywords=domination, power | q2=—
- `و ل د B006` ↔ `ك و ن B005` | score_hint=8 | discovery_hint=13 | themes=identity_personhood, life_stage_aging | keywords=identity | q2=—
- `ق و ل B002` ↔ `ء ل ه B002` | score_hint=12 | discovery_hint=12 | themes=grammar_expression, language_speech | keywords=language, speech | q2=—
- `ق و ل B015` ↔ `ص م د B005` | score_hint=12 | discovery_hint=12 | themes=authority_governance, obligation_contract | keywords=responsibility, stewardship | q2=—
- `ء ح د B006` ↔ `ك و ن B002` | score_hint=10 | discovery_hint=12 | themes=place_location | keywords=location, place | q2=—
- `ق و ل B002` ↔ `ك و ن B005` | score_hint=8 | discovery_hint=12 | themes=language_speech, physiology | keywords=speech | q2=—
- `ق و ل B006` ↔ `ء ح د B005` | score_hint=8 | discovery_hint=12 | themes=agency_action, identity_personhood | keywords=agency | q2=—
- `ق و ل B010` ↔ `ص م د B006` | score_hint=8 | discovery_hint=12 | themes=conflict, force_power | keywords=conflict | q2=—
- `و ل د B003` ↔ `ك ف ء B005` | score_hint=8 | discovery_hint=12 | themes=reproduction_birth, sequence_cycle | keywords=reproduction | q2=—
- `ق و ل B006` ↔ `و ل د B004` | score_hint=6 | discovery_hint=12 | themes=wealth_property | keywords=ownership | q2=—
- `ق و ل B006` ↔ `و ل د B006` | score_hint=6 | discovery_hint=12 | themes=identity_personhood | keywords=identity | q2=—
- `ق و ل B006` ↔ `ك و ن B005` | score_hint=6 | discovery_hint=12 | themes=identity_personhood | keywords=identity | q2=—
- `و ل د B002` ↔ `ك ف ء B005` | score_hint=6 | discovery_hint=12 | themes=reproduction_birth | keywords=reproduction | q2=—
- `ق و ل B010` ↔ `ق و ل B013` | score_hint=6 | discovery_hint=12 | themes=law | keywords=law | q2=—
- `و ل د B002` ↔ `و ل د B004` | score_hint=6 | discovery_hint=12 | themes=household_community | keywords=household | q2=—
- `ق و ل B001` ↔ `و ل د B005` | score_hint=12 | discovery_hint=11 | themes=agency_action, language_speech | keywords=language, linguistics | q2=—
- `ق و ل B013` ↔ `ء ل ه B001` | score_hint=12 | discovery_hint=11 | themes=belief_revelation, religion_worship | keywords=religion, theology | q2=—
- `ق و ل B015` ↔ `ك و ن B003` | score_hint=10 | discovery_hint=11 | themes=hospitality_welfare, obligation_contract, social_relations | keywords=care | q2=—
- `ق و ل B011` ↔ `ء ل ه B002` | score_hint=8 | discovery_hint=11 | themes=grammar_expression, language_speech | keywords=language | q2=—
- `ق و ل B011` ↔ `و ل د B005` | score_hint=8 | discovery_hint=11 | themes=language_speech, reasoning_decision | keywords=language | q2=—
- `ق و ل B015` ↔ `ء ل ه B002` | score_hint=8 | discovery_hint=11 | themes=obligation_contract, religion_worship | keywords=devotion | q2=—
- `ء ح د B001` ↔ `و ل د B006` | score_hint=8 | discovery_hint=11 | themes=identity_personhood, social_relations | keywords=identity | q2=—
- `ء ح د B001` ↔ `ك و ن B005` | score_hint=8 | discovery_hint=11 | themes=identity_personhood, language_speech | keywords=identity | q2=—
- `ء ح د B005` ↔ `ك و ن B003` | score_hint=8 | discovery_hint=11 | themes=agency_action, social_relations | keywords=agency | q2=—
- `ص م د B001` ↔ `ك و ن B004` | score_hint=8 | discovery_hint=11 | themes=authority_governance, support_dependence | keywords=dependence | q2=—
- `ص م د B003` ↔ `ك ف ء B004` | score_hint=8 | discovery_hint=11 | themes=containment_access, craft | keywords=craft | q2=—
- `ق و ل B002` ↔ `و ل د B005` | score_hint=6 | discovery_hint=11 | themes=language_speech | keywords=language | q2=—
- `ق و ل B002` ↔ `ك ف ء B003` | score_hint=6 | discovery_hint=11 | themes=language_speech | keywords=language | q2=—
- `ق و ل B003` ↔ `ء ح د B005` | score_hint=6 | discovery_hint=11 | themes=social_relations | keywords=sociality | q2=—
- `ق و ل B004` ↔ `ص م د B005` | score_hint=6 | discovery_hint=11 | themes=authority_governance | keywords=governance | q2=—
- `ق و ل B004` ↔ `ك و ن B002` | score_hint=6 | discovery_hint=11 | themes=hierarchy_status | keywords=hierarchy | q2=—
- `ق و ل B006` ↔ `ء ح د B001` | score_hint=6 | discovery_hint=11 | themes=identity_personhood | keywords=identity | q2=—
- `ق و ل B006` ↔ `ك و ن B003` | score_hint=6 | discovery_hint=11 | themes=agency_action | keywords=agency | q2=—
- `ق و ل B007` ↔ `ء ح د B005` | score_hint=6 | discovery_hint=11 | themes=social_relations | keywords=sociality | q2=—
- `ق و ل B008` ↔ `ء ح د B005` | score_hint=6 | discovery_hint=11 | themes=motion | keywords=motion | q2=—
- `ق و ل B008` ↔ `ك ف ء B002` | score_hint=6 | discovery_hint=11 | themes=motion | keywords=motion | q2=—
- `ق و ل B008` ↔ `ك ف ء B004` | score_hint=6 | discovery_hint=11 | themes=craft | keywords=craft | q2=—
- `ق و ل B010` ↔ `ص م د B005` | score_hint=6 | discovery_hint=11 | themes=authority_governance | keywords=governance | q2=—
- `ق و ل B010` ↔ `ك و ن B002` | score_hint=6 | discovery_hint=11 | themes=hierarchy_status | keywords=hierarchy | q2=—
- `ق و ل B011` ↔ `ك ف ء B003` | score_hint=6 | discovery_hint=11 | themes=language_speech | keywords=language | q2=—
- `ق و ل B012` ↔ `ء ل ه B002` | score_hint=6 | discovery_hint=11 | themes=language_speech | keywords=language | q2=—
- `ق و ل B012` ↔ `و ل د B005` | score_hint=6 | discovery_hint=11 | themes=language_speech | keywords=language | q2=—
- `ق و ل B012` ↔ `ك ف ء B003` | score_hint=6 | discovery_hint=11 | themes=language_speech | keywords=language | q2=—
- `ق و ل B015` ↔ `ص م د B004` | score_hint=6 | discovery_hint=11 | themes=hospitality_welfare | keywords=care | q2=—
- `ق و ل B016` ↔ `ء ح د B002` | score_hint=6 | discovery_hint=11 | themes=reasoning_decision | keywords=logic | q2=—
- `ء ل ه B002` ↔ `و ل د B005` | score_hint=6 | discovery_hint=11 | themes=language_speech | keywords=language | q2=—
- `ء ل ه B002` ↔ `ك و ن B005` | score_hint=6 | discovery_hint=11 | themes=language_speech | keywords=speech | q2=—
- `ء ل ه B002` ↔ `ك ف ء B003` | score_hint=6 | discovery_hint=11 | themes=language_speech | keywords=language | q2=—
- `ء ح د B004` ↔ `ك و ن B005` | score_hint=6 | discovery_hint=11 | themes=time | keywords=time | q2=—
- `ء ح د B005` ↔ `ك ف ء B002` | score_hint=6 | discovery_hint=11 | themes=motion | keywords=motion | q2=—
- `ص م د B001` ↔ `و ل د B004` | score_hint=6 | discovery_hint=11 | themes=support_dependence | keywords=dependency | q2=—
- `ص م د B001` ↔ `ك و ن B003` | score_hint=6 | discovery_hint=11 | themes=support_dependence | keywords=patronage | q2=—
- `ص م د B004` ↔ `ك و ن B003` | score_hint=6 | discovery_hint=11 | themes=hospitality_welfare | keywords=care | q2=—
- `و ل د B001` ↔ `ك ف ء B005` | score_hint=6 | discovery_hint=11 | themes=reproduction_birth | keywords=reproduction | q2=—
- `و ل د B004` ↔ `ك و ن B002` | score_hint=6 | discovery_hint=11 | themes=hierarchy_status | keywords=status | q2=—
- `و ل د B005` ↔ `ك ف ء B002` | score_hint=6 | discovery_hint=11 | themes=change_transition | keywords=change | q2=—
- `و ل د B005` ↔ `ك ف ء B003` | score_hint=6 | discovery_hint=11 | themes=language_speech | keywords=language | q2=—
- `ص م د B003` ↔ `ك ف ء B002` | score_hint=5 | discovery_hint=11 | themes=stability_endurance, storage_vessels | keywords=— | q2=—
- `ق و ل B004` ↔ `ق و ل B010` | score_hint=15 | discovery_hint=10 | themes=authority_governance, hierarchy_status | keywords=authority, governance, hierarchy | q2=—
- `و ل د B003` ↔ `و ل د B005` | score_hint=13 | discovery_hint=10 | themes=change_transition, reproduction_birth, sequence_cycle | keywords=generation, origin | q2=—
- `ق و ل B011` ↔ `ك و ن B001` | score_hint=10 | discovery_hint=10 | themes=cognition, grammar_expression, language_speech | keywords=grammar | q2=—
- `و ل د B006` ↔ `ك ف ء B001` | score_hint=10 | discovery_hint=10 | themes=justice_judgment, reasoning_decision, social_relations | keywords=comparison | q2=—
- `ق و ل B001` ↔ `ك ف ء B003` | score_hint=8 | discovery_hint=10 | themes=language_speech, rhetoric_discourse | keywords=language | q2=—
- `ق و ل B013` ↔ `ء ح د B001` | score_hint=8 | discovery_hint=10 | themes=belief_revelation, social_relations | keywords=theology | q2=—
- `ء ل ه B001` ↔ `ك و ن B004` | score_hint=8 | discovery_hint=10 | themes=authority_governance, religion_worship | keywords=submission | q2=—
- `ء ح د B004` ↔ `ك و ن B001` | score_hint=8 | discovery_hint=10 | themes=sequence_cycle, time | keywords=time | q2=—
- `ق و ل B001` ↔ `ء ل ه B002` | score_hint=6 | discovery_hint=10 | themes=language_speech | keywords=language | q2=—
- `ق و ل B004` ↔ `ء ل ه B001` | score_hint=6 | discovery_hint=10 | themes=authority_governance | keywords=authority | q2=—
- `ق و ل B004` ↔ `ص م د B001` | score_hint=6 | discovery_hint=10 | themes=authority_governance | keywords=authority | q2=—
- `ق و ل B010` ↔ `ء ل ه B001` | score_hint=6 | discovery_hint=10 | themes=authority_governance | keywords=authority | q2=—
- `ق و ل B010` ↔ `ص م د B001` | score_hint=6 | discovery_hint=10 | themes=authority_governance | keywords=authority | q2=—
- `ق و ل B010` ↔ `ك ف ء B001` | score_hint=6 | discovery_hint=10 | themes=conflict | keywords=conflict | q2=—
- `ق و ل B016` ↔ `ك و ن B001` | score_hint=6 | discovery_hint=10 | themes=cognition | keywords=ontology | q2=—
- `ص م د B006` ↔ `ك ف ء B001` | score_hint=6 | discovery_hint=10 | themes=conflict | keywords=conflict | q2=—
- `و ل د B002` ↔ `ك ف ء B001` | score_hint=6 | discovery_hint=10 | themes=kinship | keywords=kinship | q2=—

## Per-root candidate activations

### ق و ل

- `ق و ل B001` — إخراج القول بالنطق
  - activated_by_or_with: ء ل ه, ك ف ء, و ل د
  - themes: agency_action, language_speech, rhetoric_discourse
  - keywords: language, linguistics
- `ق و ل B002` — اللسان آلة القول
  - activated_by_or_with: ء ل ه, ك ف ء, ك و ن, و ل د
  - themes: grammar_expression, language_speech, physiology
  - keywords: language, speech
- `ق و ل B003` — كثرة القول في صاحبه
  - activated_by_or_with: ء ح د
  - themes: social_relations
  - keywords: sociality
- `ق و ل B004` — القيل صاحب القول النافذ
  - activated_by_or_with: ء ل ه, ص م د, ك و ن
  - themes: authority_governance, hierarchy_status
  - keywords: authority, governance, hierarchy
- `ق و ل B005` — قول ما لم يكن أو نسبته
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B006` — اجترار القول إلى النفس
  - activated_by_or_with: ء ح د, ك و ن, و ل د
  - themes: agency_action, identity_personhood, wealth_property
  - keywords: agency, identity, ownership
- `ق و ل B007` — القول الفاشي بين الناس
  - activated_by_or_with: ء ح د
  - themes: social_relations
  - keywords: sociality
- `ق و ل B008` — عود القال لضرب القلة
  - activated_by_or_with: ء ح د, ص م د, ك ف ء
  - themes: craft, material, motion, tools_equipment
  - keywords: craft, material, motion, tool
- `ق و ل B009` — المقاولة في الأمر
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B010` — اقتالة الحكم على غيره
  - activated_by_or_with: ء ل ه, ص م د, ك ف ء, ك و ن
  - themes: authority_governance, conflict, control_restraint, force_power, hierarchy_status, law
  - keywords: authority, conflict, domination, governance, hierarchy, law, power
- `ق و ل B011` — قول يجري مجرى الظن
  - activated_by_or_with: ء ل ه, ك ف ء, ك و ن, و ل د
  - themes: cognition, grammar_expression, language_speech, reasoning_decision
  - keywords: grammar, language
- `ق و ل B012` — قول في النفس لم يظهر
  - activated_by_or_with: ء ل ه, ك ف ء, و ل د
  - themes: language_speech
  - keywords: language
- `ق و ل B013` — القول اعتقاد ومذهب
  - activated_by_or_with: ء ح د, ء ل ه
  - themes: belief_revelation, law, religion_worship, social_relations
  - keywords: law, religion, theology
- `ق و ل B014` — قول الشيء دلالته
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ق و ل B015` — العناية الصادقة بالشيء
  - activated_by_or_with: ء ل ه, ص م د, ك و ن
  - themes: authority_governance, hospitality_welfare, obligation_contract, religion_worship, social_relations
  - keywords: care, devotion, responsibility, stewardship
- `ق و ل B016` — قول الشيء حده
  - activated_by_or_with: ء ح د, ك و ن
  - themes: cognition, reasoning_decision
  - keywords: logic, ontology
- `ق و ل B017` — القول إلهام يلقي معنى
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### ء ل ه

- `ء ل ه B001` — التعبد والمعبود
  - activated_by_or_with: ق و ل, ك و ن
  - themes: authority_governance, belief_revelation, religion_worship
  - keywords: authority, religion, submission, theology
- `ء ل ه B002` — اسم الله في القسم والنداء
  - activated_by_or_with: ق و ل, ك ف ء, ك و ن, و ل د
  - themes: grammar_expression, language_speech, obligation_contract, religion_worship
  - keywords: devotion, language, speech

### ء ح د

- `ء ح د B001` — الأَحَدِيَّة والوَحْدَة
  - activated_by_or_with: ق و ل, ك و ن, و ل د
  - themes: belief_revelation, identity_personhood, language_speech, social_relations
  - keywords: identity, theology
- `ء ح د B002` — استغراق النفي
  - activated_by_or_with: ق و ل
  - themes: reasoning_decision
  - keywords: logic
- `ء ح د B003` — الواحد في العد والتركيب
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —
- `ء ح د B004` — الأول والإضافة
  - activated_by_or_with: ك و ن
  - themes: sequence_cycle, time
  - keywords: time
- `ء ح د B005` — الانفراد والتفرق آحادا
  - activated_by_or_with: ق و ل, ك ف ء, ك و ن
  - themes: agency_action, identity_personhood, motion, social_relations
  - keywords: agency, motion, sociality
- `ء ح د B006` — جبل أُحُد
  - activated_by_or_with: ك و ن
  - themes: place_location
  - keywords: location, place

### ص م د

- `ص م د B001` — القصد إلى المعتمد المقصود
  - activated_by_or_with: ق و ل, ك ف ء, ك و ن, و ل د
  - themes: authority_governance, orientation_direction, support_dependence
  - keywords: authority, dependence, dependency, orientation, patronage
- `ص م د B002` — الصلابة المكتنزة بلا جوف
  - activated_by_or_with: ق و ل
  - themes: material
  - keywords: material
- `ص م د B003` — سدادة القارورة المحكمة
  - activated_by_or_with: ق و ل, ك ف ء
  - themes: containment_access, craft, stability_endurance, storage_vessels, tools_equipment
  - keywords: craft, tool
- `ص م د B004` — شد الرأس بصماد
  - activated_by_or_with: ق و ل, ك و ن
  - themes: hospitality_welfare
  - keywords: care
- `ص م د B005` — الإشراف على الأمر مع الحفل به
  - activated_by_or_with: ق و ل
  - themes: authority_governance, obligation_contract
  - keywords: governance, responsibility, stewardship
- `ص م د B006` — إيقاع الضرب بالعصا
  - activated_by_or_with: ق و ل, ك ف ء
  - themes: conflict, force_power
  - keywords: conflict
- `ص م د B007` — الدوام والبقاء على الشدة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### و ل د

- `و ل د B001` — مولود من نسل
  - activated_by_or_with: ك ف ء
  - themes: family, kinship, marriage_genealogy, motion, reproduction_birth
  - keywords: descent, family, genealogy, kinship, reproduction
- `و ل د B002` — أبوان من جهة الولادة
  - activated_by_or_with: ك ف ء
  - themes: family, household_community, kinship, marriage_genealogy, motion, reproduction_birth
  - keywords: descent, family, genealogy, household, kinship, reproduction
- `و ل د B003` — حدوث الولادة ووضع الحمل
  - activated_by_or_with: ك ف ء
  - themes: change_transition, reproduction_birth, sequence_cycle
  - keywords: generation, origin, reproduction
- `و ل د B004` — صغير قريب العهد بالولادة أو مملوك
  - activated_by_or_with: ص م د, ق و ل, ك و ن
  - themes: hierarchy_status, household_community, support_dependence, wealth_property
  - keywords: dependency, household, ownership, status
- `و ل د B005` — شيء حاصل عن شيء أو مستحدث منه
  - activated_by_or_with: ء ل ه, ق و ل, ك ف ء
  - themes: agency_action, change_transition, language_speech, reasoning_decision, reproduction_birth, sequence_cycle
  - keywords: change, generation, language, linguistics, origin
- `و ل د B006` — قرين في سن الولادة
  - activated_by_or_with: ء ح د, ق و ل, ك ف ء, ك و ن
  - themes: identity_personhood, justice_judgment, life_stage_aging, reasoning_decision, social_relations
  - keywords: comparison, identity
- `و ل د B007` — أمر لا ينادى وليده
  - activated_by_or_with: no Qnet bridge-theme memberships in this layer
  - themes: —
  - keywords: —

### ك و ن

- `ك و ن B001` — وقوع الشيء وحضوره في زمان
  - activated_by_or_with: ء ح د, ق و ل
  - themes: cognition, grammar_expression, language_speech, sequence_cycle, time
  - keywords: grammar, ontology, time
- `ك و ن B002` — المكان والمكانة من الكون
  - activated_by_or_with: ء ح د, ق و ل, و ل د
  - themes: hierarchy_status, place_location
  - keywords: hierarchy, location, place, status
- `ك و ن B003` — الكفالة والقيام على فلان
  - activated_by_or_with: ء ح د, ص م د, ق و ل, ك ف ء
  - themes: agency_action, hospitality_welfare, obligation_contract, protection_security, social_relations, support_dependence
  - keywords: agency, care, patronage, protection
- `ك و ن B004` — الخضوع بالاستكانة
  - activated_by_or_with: ء ل ه, ص م د, ق و ل
  - themes: authority_governance, control_restraint, force_power, religion_worship, support_dependence
  - keywords: dependence, domination, power, submission
- `ك و ن B005` — الشيخ المنسوب إلى كُنْتُ
  - activated_by_or_with: ء ح د, ء ل ه, ق و ل, و ل د
  - themes: identity_personhood, language_speech, life_stage_aging, physiology, time
  - keywords: identity, speech, time
- `ك و ن B006` — حالة السوء بكينة
  - activated_by_or_with: no current candidate bridges
  - themes: —
  - keywords: —

### ك ف ء

- `ك ف ء B001` — المماثلة والمقابلة بالمثل
  - activated_by_or_with: ص م د, ق و ل, و ل د
  - themes: conflict, justice_judgment, kinship, reasoning_decision, social_relations
  - keywords: comparison, conflict, kinship
- `ك ف ء B002` — الإمالة والقلب والصرف
  - activated_by_or_with: ء ح د, ص م د, ق و ل, و ل د
  - themes: change_transition, motion, orientation_direction, stability_endurance, storage_vessels
  - keywords: change, motion, orientation
- `ك ف ء B003` — اختلاف القوافي
  - activated_by_or_with: ء ل ه, ق و ل, و ل د
  - themes: language_speech, rhetoric_discourse
  - keywords: language
- `ك ف ء B004` — كِفاء الخباء
  - activated_by_or_with: ص م د, ق و ل, ك و ن
  - themes: containment_access, craft, protection_security
  - keywords: craft, protection
- `ك ف ء B005` — كفأة السنة والنتاج
  - activated_by_or_with: و ل د
  - themes: reproduction_birth, sequence_cycle
  - keywords: reproduction

## Agent instruction

Classify branches as A/B/C/S/X, but use discovery bias:

- uncertain S vs C => C
- uncertain C vs B => C/B
- broad bridge => preserve with evidence profile
- only data-invalid branches => X
- consume 10-discovery-ranking.json as a mechanical review queue; do not generate discovery ranking
