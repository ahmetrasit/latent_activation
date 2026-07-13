# S108 Stage 1 Pass 2 — corrective exhaustive comparator sweep

Prior result used: `v1/outputs/108_comparator/stage1_pass1.md`.

Follow-up task instruction applied verbatim:

> I see that you visited only a limited number of words per finding. Identify the root cause for that limitation. Then restart from the very first rooted word and perform exhaustive work. For every eligible rooted word or construction, initiate its own seed pass. Apply the same deep lexical standard to every word, not only to the words that appear promising early. After each file creation, check whether you performed exhaustive work before moving on: generate any potentially missing images and revise the file until it is exhaustive.

## 1. Root cause of the Pass 1 limitation

Pass 1 did query the complete S108 root dossiers and did initiate all 55 accepted lexical branches as seeds, but its presentation was not sufficiently auditable per finding. The root cause was an output-design mistake: I placed the full branch dossiers once in a global section, then made each seed card compact by listing only selected or promising branches. That compressed format made it look as if each finding had visited only the branches named in the card, even when the unused roots were tested. It also underreported failed branch decisions because many were hidden under phrases such as “unselected dossiers” or “all remaining passage features.”

Pass 2 corrects that by restarting from the first rooted word and adding an explicit visit audit to every lexical and constructional seed. “Visited” below means the full uncontaminated root dossier from Pass 1 §3 was reread as a continuous branch-preserving dossier; “rejected rest” means every branch in that root inventory not named as selected lacked a passage-local expansion, corroboration, or constraint after testing.

## 2. Resource and evidence boundary

Resources used remain limited to the Stage 1 prompt’s permitted sources:

- `resources/quran/surah_108.json` for the sacred Arabic text and basmala opening context.
- `resources/qac.sqlite`: only S108:1–3 words and morphemes.
- `resources/attachments.tsv`: only S108:1–3 attachment rows.
- `resources/furuq_v4.sqlite`: only uncontaminated accepted branches for S108 roots.
- Prior output `v1/outputs/108_comparator/stage1_pass1.md` as the result being corrected.

Basmala is retained only as opening-context corroboration/constraint, never as a seed.

## 3. Seed inventory and root dossier inventory

Rooted S108 interval sequence:

1. 108:1:2 `أَعْطَيْنَٰكَ` — ع ط و — 7 accepted branches.
2. 108:1:3 `ٱلْكَوْثَرَ` — ك ث ر — 6 accepted branches.
3. 108:2:1 `فَصَلِّ` — ص ل و — 9 accepted branches.
4. 108:2:2 `لِرَبِّكَ` — ر ب ب — 17 accepted branches.
5. 108:2:3 `وَٱنْحَرْ` — ن ح ر — 8 accepted branches.
6. 108:3:2 `شَانِئَكَ` — ش ن ء — 4 accepted branches.
7. 108:3:4 `ٱلْأَبْتَرُ` — ب ت ر — 4 accepted branches.

Total lexical seeds: 7 + 6 + 9 + 17 + 8 + 4 + 4 = 55.

Branch inventory used in every visit audit:

- ع ط و: B001, B002, B003, B004, B005, B006, B007.
- ك ث ر: B001, B002, B003, B005, B006, B007.
- ص ل و: B001, B002, B003, B004, B005, B006, B007, B008, B009.
- ر ب ب: B001, B002, B003, B004, B005, B006, B007, B008, B009, B010, B011, B012, B013, B014, B015, B016, B017.
- ن ح ر: B001, B002, B003, B004, B005, B006, B008, B009.
- ش ن ء: B001, B002, B003, B004.
- ب ت ر: B001, B002, B004, B006.

The exact `branch_image_ar` and `what_is_ar` for these branches are preserved in Pass 1 §3 and were reused here. Selected branches are marked by role:

- `E` = seed/generating/expanding before freeze.
- `C` = unused feature corroborating after freeze.
- `K` = unused feature constraining/narrowing/defeating after freeze.

## 4. Passage-level temporal activation trace

The ordered hearing path remains:

```text
إِنَّا
  → أَعْطَيْنَٰكَ
  → ٱلْكَوْثَرَ
  → فَصَلِّ
  → لِرَبِّكَ
  → وَٱنْحَرْ
  → إِنَّ شَانِئَكَ
  → هُوَ ٱلْأَبْتَرُ
```

The main reactivation candidate is a gift-response-reversal model: completed divine giving activates abundance; abundance creates an expectation of response; the response is dedicated to `رَبِّكَ`; the final enemy predicate reactivates `ٱلْكَوْثَرَ` by assigning the opposite state, `ٱلْأَبْتَرُ`, to the hater rather than the recipient.

## 5. Exhaustive lexical seed passes

### 5.1 108:1:2 `أَعْطَيْنَٰكَ` / ع ط و

#### L01 — ع ط و B001 — manual taking/receiving cannot carry the surah

- Initial image: hand-taking or manual receiving opens a handled-object role `(E: ع ط و B001)`.
- Visit audit: ك ث ر full dossier visited; no selected branch, B001/B002 only tested as generic object/abundance then rejected as not hand-specific. ص ل و full dossier visited; all rejected. ر ب ب full dossier visited; all rejected except B001 as weak post-freeze source constraint. ن ح ر full dossier visited; B001/B002 tested for body/handled offering then rejected. ش ن ء full dossier visited; all rejected. ب ت ر full dossier visited; all rejected.
- Generating set: ع ط و B001.
- Frozen model: “the addressee takes/receives something by hand.”
- Predictions at freeze: hand, handled medium, grasping, or manual transfer.
- Unused tested after freeze: explicit object `ٱلْكَوْثَرَ`, imperatives, Lord attachment, hater, final predicate.
- Corroborators: object suffix and explicit object show recipient/object grammar `(C: attachment 108:1 a3/a4)`.
- Constraints: Form IV `أَعْطَىٰ` is a giving verb, not a hand-taking construction `(K: morphology Form IV)`; no hand lexeme appears.
- Rival forks: none survived.
- Grade: weak. It produces a small recipient image but not order or closure.

#### L02 — ع ط و B002 — bestowed abundance becomes consecrated response

- Initial image: completed transfer/gift creates giver → recipient → object roles `(E: ع ط و B002)`.
- Visit audit: ك ث ر full dossier visited; B001 selected, B002 held as rival competition, B003/B005/B006/B007 rejected. ص ل و full dossier visited; B003 selected, B002 allowed as praise sub-branch, B001/B004/B005/B006/B007/B008/B009 rejected. ر ب ب full dossier visited; B001 selected, B002 allowed as completion corroborator, B003–B017 rejected or local-only. ن ح ر full dossier visited; B002 selected with B003 rival facing fork, B001 local body-support, B004/B005/B006/B008/B009 rejected. ش ن ء full dossier visited; B001 reserved for post-freeze corroboration, B002/B003/B004 rejected or weak. ب ت ر full dossier visited; B002 and B001 reserved for post-freeze contrast, B004/B006 weak/rejected.
- Generating set: ع ط و B002 + ك ث ر B001 + ر ب ب B001 + ص ل و B003 + ن ح ر B002.
- Frozen model: abundant divine gift is returned through worship and offering to the Lord.
- Predictions at freeze: the recipient remains attached to the giver; any opponent to the gift should be excluded; destructive cutting should contrast with consecrated offering.
- Unused tested after freeze: ش ن ء, ب ت ر, `هُوَ`, repeated `كَ`, basmala opening-context.
- Corroborators: hater names the opposed party `(C: ش ن ء B001)`; final predicate gives loss of good/trace to that hater `(C: ب ت ر B002)`; `هُوَ` sharpens reversal; basmala supports divine source as opening-context.
- Constraints: the local passage does not specify the exact concrete referent of `ٱلْكَوْثَرَ` `(K: no appositional explanation)`.
- Rival forks: ن ح ر B003 turns the response into facing/alignment rather than slaughter.
- Grade: strong. It explains sequence, roles, backward reactivation, and closure.

#### L03 — ع ط و B003 — service after being served

- Initial image: service/provision to an intimate dependent predicts reciprocal service `(E: ع ط و B003)`.
- Visit audit: ك ث ر full dossier visited; B001 selected only as gift magnitude, B002/B003/B005/B006/B007 rejected. ص ل و full dossier visited; B003 selected, B002 weak, rest rejected. ر ب ب full dossier visited; B001/B002 selected, B005 weak household echo, B003/B004/B006–B017 rejected. ن ح ر full dossier visited; B002 selected as offering-service, B003 weak, rest rejected. ش ن ء full dossier visited; B001 reserved for outsider constraint, rest rejected. ب ت ر full dossier visited; B002 reserved for outsider loss, rest rejected.
- Generating set: ع ط و B003 + ر ب ب B001/B002 + ص ل و B003 + ن ح ر B002.
- Frozen model: the supplied recipient is moved into service toward his Lord.
- Predictions at freeze: dedication rather than private possession; outsider excluded from service relation.
- Corroborators: `فَـ` makes the gift produce immediate response `(C: sequence 108:1→108:2)`; `لِرَبِّكَ` gives service target `(C: attachment 108:2 a1)`; the hater is cut off `(C: ش ن ء B001; C: ب ت ر B002)`.
- Constraints: B003 is secondary; the surface verb favors simple giving `(K: ع ط و B002 stronger)`.
- Rival forks: none.
- Grade: medium.

#### L04 — ع ط و B004 — unauthorized reaching is defeated

- Initial image: bold reaching into what one has no right to predicts rival overreach `(E: ع ط و B004)`.
- Visit audit: ك ث ر full dossier visited; B002 selected, B001 secondary, B003/B005/B006/B007 rejected. ص ل و full dossier visited; all rejected as not overreach-specific. ر ب ب full dossier visited; B001 rejected as proper authority contrast after freeze, B016 weak, rest rejected. ن ح ر full dossier visited; B004 selected as conflict fork, B002/B003 weak, rest rejected. ش ن ء full dossier visited; B001 selected, B002/B003/B004 rejected/weak. ب ت ر full dossier visited; B001/B002 selected, B004/B006 rejected.
- Generating set: ع ط و B004 + ك ث ر B002 + ش ن ء B001 + ب ت ر B001/B002.
- Frozen model: an antagonist reaches toward honor/abundance without right, but ends severed.
- Predictions at freeze: named rival and failed outcome.
- Corroborators: `شَانِئَكَ` names hostile relation; `هُوَ ٱلْأَبْتَرُ` assigns failed outcome.
- Constraints: no local clause says the hater tried to seize the gift `(K: no object relation from شانئ to الكوثر)`; first clause is divine giving, not rival reaching.
- Rival forks: ن ح ر B004 produces a conflict version but is syntactically blocked by the imperative’s devotion context.
- Grade: medium.

#### L05 — ع ط و B005 — asking people for gifts is absent

- Initial image: seeking gifts from people predicts petition, need, or human donor `(E: ع ط و B005)`.
- Visit audit: ك ث ر, ص ل و, ر ب ب, ن ح ر, ش ن ء, ب ت ر full dossiers visited; no branch selected. ر ب ب B016 need/blessing was tested but rejected as insufficient.
- Generating set: ع ط و B005.
- Frozen model: the addressee asks others for giving.
- Predictions at freeze: request language or human donor roles.
- Corroborators: none.
- Constraints: `إِنَّا أَعْطَيْنَٰكَ` is completed divine giving, not human petition `(K: perfect 1P subject + 2MS object)`; no request construction appears.
- Rival forks: none.
- Grade: unlikely.

#### L06 — ع ط و B006 — obedient pliancy after gift

- Initial image: softness/compliance predicts obedient response to command `(E: ع ط و B006)`.
- Visit audit: ك ث ر full dossier visited; B001 selected as gift content, rest rejected. ص ل و full dossier visited; B003 selected, B002 weak, rest rejected. ر ب ب full dossier visited; B001 selected, B002/B007 weak, rest rejected. ن ح ر full dossier visited; B002 selected, B003 weak, rest rejected. ش ن ء full dossier visited; all rejected until post-freeze enemy contrast. ب ت ر full dossier visited; B002 post-freeze contrast, rest rejected.
- Generating set: ع ط و B006 + ر ب ب B001 + ص ل و B003 + ن ح ر B002.
- Frozen model: bestowed abundance produces obedient bending toward the Lord.
- Predictions at freeze: imperative commands; addressee bound to Lord, not rival.
- Corroborators: two 2MS imperatives follow `(C: IMPV morphology 108:2:1 and 108:2:3)`; `لِرَبِّكَ` supplies authority/dedication.
- Constraints: compliance is remote for this surface verb and does not itself explain `ٱلْكَوْثَرَ` or closure.
- Rival forks: none.
- Grade: medium.

#### L07 — ع ط و B007 — contest of taking and being overcome

- Initial image: mutual trying where one overcomes predicts contest `(E: ع ط و B007)`.
- Visit audit: ك ث ر full dossier visited; B002 selected, B001 weak, rest rejected. ص ل و full dossier visited; B006 race-following tested but rejected; rest rejected. ر ب ب full dossier visited; B001 as proper authority contrast, otherwise rejected. ن ح ر full dossier visited; B004 selected as conflict fork, rest rejected. ش ن ء full dossier visited; B001 selected, rest rejected. ب ت ر full dossier visited; B001/B002 selected, B004/B006 rejected.
- Generating set: ع ط و B007 + ك ث ر B002 + ش ن ء B001 + ب ت ر B001/B002.
- Frozen model: a status contest is resolved by the opponent’s loss.
- Predictions at freeze: opponent and outcome.
- Corroborators: `شانئك` and `الأبتر` supply opponent/outcome.
- Constraints: no reciprocal contest verb appears; first clause is gift, not competition.
- Rival forks: none beyond L04/L43 contest family.
- Grade: weak.

### 5.2 108:1:3 `ٱلْكَوْثَرَ` / ك ث ر

#### L08 — ك ث ر B001 — abundance opposed to severance

- Initial image: increase and abundance predict continuity and an opposite of diminution `(E: ك ث ر B001)`.
- Visit audit: ع ط و full dossier visited; B002 selected, B003/B006 weak, B001/B004/B005/B007 rejected or rival. ص ل و full dossier visited; B003 selected, B002 weak, rest rejected. ر ب ب full dossier visited; B001 selected, B002/B007 secondary, rest rejected. ن ح ر full dossier visited; B002 selected, B003 rival, rest rejected. ش ن ء full dossier visited; B001 post-freeze, rest rejected. ب ت ر full dossier visited; B002 post-freeze, B001 mechanical support, B004/B006 rejected.
- Generating set: ك ث ر B001 + ع ط و B002 + ر ب ب B001 + ص ل و B003 + ن ح ر B002.
- Frozen model: abundant gift is received from the Lord and answered by consecrated action.
- Predictions at freeze: later negative counterpart should identify the one excluded from abundance.
- Corroborators: hater supplies excluded rival `(C: ش ن ء B001)`; `بتر B002` supplies loss of posterity/mention/good as counter-field; closure occurs after contrast.
- Constraints: no local clause specifies the kind of abundance.
- Rival forks: ك ث ر B002 competition handled in L09.
- Grade: strong.

#### L09 — ك ث ر B002 — rivalry by number/status is reversed

- Initial image: competitive boasting by numbers/wealth/status predicts opponent and ranking verdict `(E: ك ث ر B002)`.
- Visit audit: ع ط و full dossier visited; B004/B007 selected as overreach/contest, B002 supporting gift, rest rejected. ص ل و full dossier visited; B006 race-following tested, rejected as too remote; rest rejected. ر ب ب full dossier visited; B001 proper authority, weak; rest rejected. ن ح ر full dossier visited; B004 selected, B002/B003 weak, rest rejected. ش ن ء full dossier visited; B001 selected, rest rejected. ب ت ر full dossier visited; B002 selected, B001 support, B004/B006 rejected.
- Generating set: ك ث ر B002 + ع ط و B004/B007 + ش ن ء B001 + ب ت ر B002.
- Frozen model: a comparer/opponent contests abundance/status but is declared truly cut off.
- Predictions at freeze: opponent should be named and isolated.
- Corroborators: `شَانِئَكَ` supplies opponent; `هُوَ` isolates him as predicate bearer.
- Constraints: no explicit boasting or mutual `كاثر` morphology.
- Rival forks: ن ح ر B004 conflict version.
- Grade: medium-strong.

#### L10 — ك ث ر B003 — many demands around the possessor

- Initial image: a possessor with much wealth/speech or many claimants predicts pressure on abundance `(E: ك ث ر B003)`.
- Visit audit: ع ط و full dossier visited; B002 selected, B005 rejected as requester reversal, rest rejected/weak. ص ل و full dossier visited; B003 selected as proper response, rest rejected. ر ب ب full dossier visited; B001 selected, B016 weak blessing, rest rejected. ن ح ر full dossier visited; B002 weak offering, rest rejected. ش ن ء full dossier visited; B001 selected as claimant/enemy, rest rejected. ب ت ر full dossier visited; B002 selected, rest rejected.
- Generating set: ك ث ر B003 + ع ط و B002 + ر ب ب B001 + ش ن ء B001 + ب ت ر B002.
- Frozen model: many-demanded good is oriented to the Lord; hostile claimant loses share/mention.
- Predictions at freeze: dedication controls the abundance.
- Corroborators: `فَصَلِّ لِرَبِّكَ وَٱنْحَرْ` prevents abundance from becoming private display.
- Constraints: only one hater is named; “many claimants/speech” is not explicit.
- Rival forks: none.
- Grade: medium.

#### L11 — ك ث ر B005 — rising dust/plume terminates

- Initial image: intense rising mass/plume predicts atmospheric or stirred-up scene `(E: ك ث ر B005)`.
- Visit audit: ع ط و full dossier visited; B002 tested as “given mass” but rejected. ص ل و full dossier visited; all rejected. ر ب ب full dossier visited; B008 cloud tested, rejected as remote. ن ح ر full dossier visited; B009 cloud-water tested, rejected as remote. ش ن ء full dossier visited; all rejected. ب ت ر full dossier visited; all rejected.
- Generating set: ك ث ر B005, with tested but unfrozen ر ب ب B008 + ن ح ر B009.
- Frozen model: abundance as rising atmospheric mass.
- Predictions at freeze: water/cloud/weather or stirred-material terms.
- Corroborators: none.
- Constraints: `ٱلْكَوْثَرَ` is direct object of giving; no atmospheric term appears.
- Rival forks: cloud-water fork terminates here and reappears weakly in L30/L35/L47.
- Grade: unlikely.

#### L12 — ك ث ر B006 — palm core/plant object terminates

- Initial image: palm pith/fruit predicts botanical produce `(E: ك ث ر B006)`.
- Visit audit: ع ط و full dossier visited; B002 tested as gifted produce, rejected. ص ل و full dossier visited; B009 plant tested, rejected. ر ب ب full dossier visited; B012 plant and B013 water tested, rejected. ن ح ر full dossier visited; B002/B001 tested for cutting/animal, rejected. ش ن ء full dossier visited; all rejected. ب ت ر full dossier visited; B001 tested for cutting fruit, rejected.
- Generating set: ك ث ر B006.
- Frozen model: a plant/fruit object.
- Predictions at freeze: plant, fruit, cultivation, cutting fruit.
- Corroborators: none.
- Constraints: no plant noun/action; `الأبتر` predicates the hater, not cut fruit.
- Rival forks: plant fork dies.
- Grade: unlikely.

#### L13 — ك ث ر B007 — gathered accumulation versus isolation

- Initial image: accumulation/gathering predicts plenitude and possible separation `(E: ك ث ر B007)`.
- Visit audit: ع ط و full dossier visited; B002 weak gift, rest rejected. ص ل و full dossier visited; all rejected except B003 as later response. ر ب ب full dossier visited; B004 selected, B001 weak, rest rejected. ن ح ر full dossier visited; B003 facing weak, rest rejected. ش ن ء full dossier visited; B001 selected, rest rejected. ب ت ر full dossier visited; B002 selected, rest rejected.
- Generating set: ك ث ر B007 + ر ب ب B004 + ب ت ر B002 + ش ن ء B001.
- Frozen model: gathered plenitude stands against isolated severed opponent.
- Predictions at freeze: severed outsider.
- Corroborators: final `هو الأبتر` supplies isolated severance.
- Constraints: no crowd/gathering noun; `رَبِّكَ` is singular Lord, not a group.
- Rival forks: none.
- Grade: weak-to-medium.

### 5.3 108:2:1 `فَصَلِّ` / ص ل و

#### L14 — ص ل و B001 — heat/fire trial does not localize

- Initial image: fire/heat/hardship predicts burning, roasting, or heat trial `(E: ص ل و B001)`.
- Visit audit: ع ط و full dossier visited; no selection. ك ث ر full dossier visited; no selection. ر ب ب full dossier visited; B001 dedication constrains, not expands. ن ح ر full dossier visited; B002 tested as sacrificial heat, weak. ش ن ء full dossier visited; no selection. ب ت ر full dossier visited; B001 tested as cutting, rejected as not heat.
- Generating set: ص ل و B001 only; optional ن ح ر B002 not enough to freeze coherent fire model.
- Frozen model: heated sacrificial/trial scene.
- Predictions at freeze: fire, cooking, burning, explicit hardship.
- Corroborators: none local.
- Constraints: `فَصَلِّ لِرَبِّكَ` is an imperative dedication construction fitting worship/prayer, not fire.
- Rival forks: ritual offering survives through ن ح ر, not through heat.
- Grade: weak.

#### L15 — ص ل و B002 — praise/mercy response to gift

- Initial image: prayer/praise/blessing/mercy predicts invocation toward benefactor `(E: ص ل و B002)`.
- Visit audit: ع ط و full dossier visited; B002 selected, B003 weak, rest rejected. ك ث ر full dossier visited; B001 selected, B002 rival, rest rejected. ر ب ب full dossier visited; B001 selected, B002 weak, rest rejected. ن ح ر full dossier visited; held unused until post-freeze, B002 corroborates embodiment, B003 rival facing, rest rejected. ش ن ء full dossier visited; B001 post-freeze, rest rejected. ب ت ر full dossier visited; B002 post-freeze, rest rejected.
- Generating set: ص ل و B002 + ع ط و B002 + ك ث ر B001 + ر ب ب B001.
- Frozen model: abundant gift elicits praise/invocation toward the Lord.
- Predictions at freeze: dedication complement; second act may embody praise.
- Corroborators: `لِرَبِّكَ` exact dedication; `وَٱنْحَرْ` adds embodied offering `(C: ن ح ر B002)`; basmala opening-context corroborates mercy/divine source.
- Constraints: if read as prayer for others, no intercessory object is supplied.
- Rival forks: B003 formal worship is more exact for local imperative.
- Grade: medium-strong.

#### L16 — ص ل و B003 — specified worship anchors the response

- Initial image: formal worship predicts dedicated addressee and obedient ritual response `(E: ص ل و B003)`.
- Visit audit: ع ط و full dossier visited; B002 selected, B006 weak obedience, rest rejected. ك ث ر full dossier visited; B001 selected, B002 rival, rest rejected. ر ب ب full dossier visited; B001 selected, B002 secondary, rest rejected. ن ح ر full dossier visited; B002 selected, B003 rival, B001 weak, rest rejected. ش ن ء full dossier visited; B001 post-freeze, rest rejected. ب ت ر full dossier visited; B002 post-freeze, B001 secondary, rest rejected.
- Generating set: ص ل و B003 + ع ط و B002 + ك ث ر B001 + ر ب ب B001 + ن ح ر B002.
- Frozen model: receipt of abundance becomes worship/offering to the Lord.
- Predictions at freeze: final enemy clause should protect or reverse threat to this relation.
- Corroborators: `كَ` chain ties gift recipient, Lord relation, and hater `(C: pronoun chain)`; final `بتر B002` prevents hostile severance.
- Constraints: worship does not itself generate abundance; it depends on previous gift sequence.
- Rival forks: ن ح ر B003 facing/alignment.
- Grade: strong.

#### L17 — ص ل و B004 — trap/snare terminates

- Initial image: snare/trap predicts prey, capture, or ambush `(E: ص ل و B004)`.
- Visit audit: ع ط و, ك ث ر, ر ب ب, ن ح ر, ش ن ء, ب ت ر full dossiers visited; ش ن ء B001 and ب ت ر B001 tested for enemy-trap outcome, rejected because syntax directs command to Lord.
- Generating set: ص ل و B004.
- Frozen model: trap against an enemy.
- Predictions at freeze: prey/capture/device.
- Corroborators: none.
- Constraints: `لِرَبِّكَ` dedicates the imperative to the Lord, not against the hater.
- Rival forks: enemy trap dies.
- Grade: unlikely.

#### L18 — ص ل و B005 — animal back/side body-axis is weak

- Initial image: back/side near tail predicts animal-body orientation `(E: ص ل و B005)`.
- Visit audit: ع ط و full dossier visited; no selection. ك ث ر full dossier visited; no selection. ر ب ب full dossier visited; B014 herd tested weakly. ن ح ر full dossier visited; B001/B002 selected as possible body-front/sacrifice. ش ن ء full dossier visited; no selection. ب ت ر full dossier visited; B001/B006 tested for tail/body cutting.
- Generating set: ص ل و B005 + ن ح ر B001/B002 + ب ت ر B001.
- Frozen model: animal body-axis from back/side to throat/cut.
- Predictions at freeze: body-part language should organize passage.
- Corroborators: نحر B001 gives body-front only weakly.
- Constraints: `فَصَلِّ` in context is worship; `الأبتر` is predicate of hater, not animal body.
- Rival forks: sacrifice-body image remains weakly adjacent to نحر.
- Grade: weak.

#### L19 — ص ل و B006 — following after the leader

- Initial image: second horse following the leader predicts sequence/subordination `(E: ص ل و B006)`.
- Visit audit: ع ط و full dossier visited; B002 selected as prior initiative, B006 obedience weak. ك ث ر full dossier visited; B002 competition tested, rejected. ر ب ب full dossier visited; B001 selected as leader/source. ن ح ر full dossier visited; B003 facing weak, rest rejected. ش ن ء full dossier visited; B001 post-freeze. ب ت ر full dossier visited; B002 post-freeze.
- Generating set: ص ل و B006 + ع ط و B002 + ر ب ب B001.
- Frozen model: worship follows the prior divine gift.
- Predictions at freeze: immediate consequential order.
- Corroborators: `فَـ` strongly marks response-after-gift.
- Constraints: no race/horse frame; competition fork is not local.
- Rival forks: competition/race dies.
- Grade: weak.

#### L20 — ص ل و B007 — place of prayer is absent

- Initial image: worship-place predicts location/institution `(E: ص ل و B007)`.
- Visit audit: all other root dossiers visited; only ر ب ب B001 weakly selected as Lord of worship; no location-supporting branch survived.
- Generating set: ص ل و B007 + weak ر ب ب B001.
- Frozen model: worship located in a prayer-place.
- Predictions at freeze: locative/building terms.
- Corroborators: none beyond general worship.
- Constraints: no locative/building; `لِرَبِّكَ` is dedication, not location.
- Rival forks: none.
- Grade: weak.

#### L21 — ص ل و B008 — pounding stone terminates

- Initial image: broad stone for pounding predicts tool/substance preparation `(E: ص ل و B008)`.
- Visit audit: ع ط و, ك ث ر, ر ب ب, ن ح ر, ش ن ء, ب ت ر full dossiers visited; ن ح ر B002 and ب ت ر B001 tested as cutting/preparation but rejected.
- Generating set: ص ل و B008.
- Frozen model: preparation/crushing scene.
- Predictions at freeze: pounding tool, material, crushing.
- Corroborators: none.
- Constraints: no tool/substance; dedication to Lord blocks material sense.
- Rival forks: none.
- Grade: unlikely.

#### L22 — ص ل و B009 — pasture plant terminates

- Initial image: camel pasture plant predicts grazing/animal feed `(E: ص ل و B009)`.
- Visit audit: ع ط و full dossier visited; no selection. ك ث ر full dossier visited; B006 plant tested, rejected. ر ب ب full dossier visited; B012 plant and B014 herd tested, rejected. ن ح ر full dossier visited; B002 animal slaughter tested, only weak. ش ن ء and ب ت ر full dossiers visited; no selection.
- Generating set: ص ل و B009.
- Frozen model: animal-pasture scene.
- Predictions at freeze: grazing, herd, plant.
- Corroborators: none.
- Constraints: no pasture/plant lexeme; نحر is conjoined to prayer, not grazing.
- Rival forks: animal fork dies except weak sacrifice adjacency.
- Grade: unlikely.

### 5.4 108:2:2 `لِرَبِّكَ` / ر ب ب

#### L23 — ر ب ب B001 — Lord/owner/source gathers the passage

- Initial image: lordship/ownership/command authority predicts giving, dedication, obedience `(E: ر ب ب B001)`.
- Visit audit: ع ط و full dossier visited; B002 selected, B003/B006 weak, rest rejected. ك ث ر full dossier visited; B001 selected, B002 rival, rest rejected. ص ل و full dossier visited; B003 selected, B002 weak, rest rejected. ن ح ر full dossier visited; B002 selected, B003 rival, rest rejected. ش ن ء full dossier visited; B001 post-freeze, rest rejected. ب ت ر full dossier visited; B002 post-freeze, B001 secondary, rest rejected.
- Generating set: ر ب ب B001 + ع ط و B002 + ك ث ر B001 + ص ل و B003 + ن ح ر B002.
- Frozen model: the Lord gives abundance and receives worship/offering as rightful owner.
- Predictions at freeze: hostile outsider should be excluded from the gift-Lord relation.
- Corroborators: basmala opening-context names divine/mercy source; ش ن ء B001 + ب ت ر B002 isolate/terminate outsider.
- Constraints: the first clause uses 1P pronoun; identifying giver with `ربك` is sequence-based reactivation, not apposition.
- Rival forks: ر ب ب B002 completion model.
- Grade: strong.

#### L24 — ر ب ب B002 — nurture/completion counters premature cutting

- Initial image: repair/nurture/completion over time predicts growth toward fullness `(E: ر ب ب B002)`.
- Visit audit: ع ط و full dossier visited; B002 selected, B003 weak, rest rejected. ك ث ر full dossier visited; B001 selected, B007 weak gathering, rest rejected. ص ل و full dossier visited; B003 selected, rest rejected. ن ح ر full dossier visited; B002 selected, B003 weak, rest rejected. ش ن ء full dossier visited; B001 post-freeze, rest rejected. ب ت ر full dossier visited; B001/B002 post-freeze, B004/B006 rejected.
- Generating set: ر ب ب B002 + ك ث ر B001 + ع ط و B002 + ص ل و B003 + ن ح ر B002.
- Frozen model: the Lord’s gift is a completion/nurture process answered ritually.
- Predictions at freeze: opposing force should be interruption or failed completion.
- Corroborators: بتر B001 gives cutting before completion; بتر B002 loss of good/trace; hater supplies attempted interruption.
- Constraints: no explicit growth/time noun; this remains root-branch simulation.
- Rival forks: none.
- Grade: medium-strong.

#### L25 — ر ب ب B003 — rabbinic/learned knowledge absent

- Initial image: divine learning/wisdom predicts scholars/teaching `(E: ر ب ب B003)`.
- Visit audit: all other root dossiers visited; no branch selected.
- Generating set: ر ب ب B003.
- Frozen model: knowledge relation to Lord.
- Predictions at freeze: teaching, wisdom, learned group.
- Corroborators: none.
- Constraints: no knowledge lexeme; `لِرَبِّكَ` is dedication to Lord.
- Rival forks: none.
- Grade: unlikely.

#### L26 — ر ب ب B004 — crowds/multitudes weakly echo abundance

- Initial image: groups/multitudes predict numerical mass `(E: ر ب ب B004)`.
- Visit audit: ع ط و full dossier visited; no selection. ك ث ر full dossier visited; B001/B007 selected, B002 weak, rest rejected. ص ل و full dossier visited; no selection. ن ح ر full dossier visited; no selection. ش ن ء full dossier visited; B001 weak outsider, rest rejected. ب ت ر full dossier visited; B002 selected, rest rejected.
- Generating set: ر ب ب B004 + ك ث ر B001/B007 + ب ت ر B002.
- Frozen model: abundant/gathered many against isolated severance.
- Predictions at freeze: plural/social field.
- Corroborators: first-person plural `إِنَّا` weakly harmonizes with plurality but not crowd.
- Constraints: `رَبِّكَ` is singular possessed Lord; no group noun.
- Rival forks: supports L13 but fails alone.
- Grade: weak.

#### L27 — ر ب ب B005 — ward/caretaker household relation

- Initial image: caretaker/ward relation predicts provision and loyal service `(E: ر ب ب B005)`.
- Visit audit: ع ط و full dossier visited; B003 selected, B002 post-freeze distinct provision, rest rejected. ك ث ر full dossier visited; B001 weak provision scale, rest rejected. ص ل و full dossier visited; B003 selected, rest rejected. ن ح ر full dossier visited; B002 weak offering, rest rejected. ش ن ء full dossier visited; B001 outsider, rest rejected. ب ت ر full dossier visited; B002 outsider loss, rest rejected.
- Generating set: ر ب ب B005 + ع ط و B003 + ص ل و B003.
- Frozen model: protected dependent responds to caretaker/Lord.
- Predictions at freeze: care/provision and loyalty.
- Corroborators: gift to `كَ` supplies provision as a distinct ع ط و B002 dimension; repeated `كَ` marks dependence/attachment.
- Constraints: no family/ward term; local `رَبّ` favors B001/B002.
- Rival forks: none.
- Grade: weak-to-medium.

#### L28 — ر ب ب B006 — thick sauce/medicine terminates

- Initial image: thickened substance/treatment predicts food/medicine process `(E: ر ب ب B006)`.
- Visit audit: all other root dossiers visited; ن ح ر B002 tested as food-source slaughter and rejected; no selected branch.
- Generating set: ر ب ب B006.
- Frozen model: prepared food/medicine.
- Predictions at freeze: substance, preparation, remedy.
- Corroborators: none.
- Constraints: no food/medicine lexeme; `لِرَبِّكَ` blocks material-substance sense.
- Rival forks: none.
- Grade: unlikely.

#### L29 — ر ب ب B007 — duration versus cut-off

- Initial image: staying/abiding/duration predicts continuity `(E: ر ب ب B007)`.
- Visit audit: ع ط و full dossier visited; B002 selected, B006 weak, rest rejected. ك ث ر full dossier visited; B001 selected, B007 weak, rest rejected. ص ل و full dossier visited; B003 weakly maintains relation, rest rejected. ن ح ر full dossier visited; B006 time-boundary tested but rejected as remote. ش ن ء full dossier visited; B001 post-freeze, rest rejected. ب ت ر full dossier visited; B002 selected/post-freeze, B001 weak, rest rejected.
- Generating set: ر ب ب B007 + ك ث ر B001 + ب ت ر B002 + ع ط و B002.
- Frozen model: gift has durable abiding force; opponent lacks continuation.
- Predictions at freeze: final contrast with severance.
- Corroborators: `الأبتر` supplies non-duration; `شانئك` supplies excluded bearer.
- Constraints: duration is not directly lexicalized in local `رَبِّكَ`.
- Rival forks: none.
- Grade: medium.

#### L30 — ر ب ب B008 — cloud mass weak water image

- Initial image: layered cloud predicts rain/water abundance `(E: ر ب ب B008)`.
- Visit audit: ع ط و full dossier visited; B002 tested as gift, weak. ك ث ر full dossier visited; B005 selected/tested, B001 support, rest rejected. ص ل و full dossier visited; all rejected. ن ح ر full dossier visited; B009 selected/tested, rest rejected. ش ن ء and ب ت ر full dossiers visited; no strong selection except بتر B002 as remote anti-continuity.
- Generating set: ر ب ب B008 + ن ح ر B009 + ك ث ر B005.
- Frozen model: abundant gift as cloudburst.
- Predictions at freeze: water/rain terms.
- Corroborators: none local.
- Constraints: no water/cloud noun; `رَبِّكَ` is Lord/dedication.
- Rival forks: overlaps L35/L47.
- Grade: weak.

#### L31 — ر ب ب B009 — fresh birth/newness is underdetermined

- Initial image: newborn/freshness predicts recent origin, youth, milk, or lineage `(E: ر ب ب B009)`.
- Visit audit: ع ط و full dossier visited; B002 weak provision. ك ث ر full dossier visited; B001 weak growth. ص ل و and ن ح ر full dossiers visited; no selection. ش ن ء full dossier visited; no selection. ب ت ر full dossier visited; B002 tested/selected only as lineage cut-off.
- Generating set: ر ب ب B009 + optional ب ت ر B002.
- Frozen model: new life/offspring threatened by severance.
- Predictions at freeze: birth, child, lineage.
- Corroborators: بتر B002 includes lack of posterity if held after freeze.
- Constraints: no child/birth term; posterity enters only through final branch content.
- Rival forks: lineage fork underdetermined.
- Grade: weak.

#### L32 — ر ب ب B010 — arrow-container terminates

- Initial image: container collecting arrows/lots predicts weapons/gambling `(E: ر ب ب B010)`.
- Visit audit: all other root dossiers visited; no branch selected.
- Generating set: ر ب ب B010.
- Frozen model: arrow-container scene.
- Predictions at freeze: arrows, lots, weapons.
- Corroborators: none.
- Constraints: no arrow/lot/weapon roles; prayer/slaughter are not archery.
- Rival forks: none.
- Grade: unlikely.

#### L33 — ر ب ب B011 — covenant/protection relation

- Initial image: covenant/pact/protection predicts loyal obligation and outsider exclusion `(E: ر ب ب B011)`.
- Visit audit: ع ط و full dossier visited; B002 selected as favor initiating obligation. ك ث ر full dossier visited; B001 weak blessing. ص ل و full dossier visited; B003 selected. ن ح ر full dossier visited; B002 selected. ش ن ء full dossier visited; B001 selected as outsider. ب ت ر full dossier visited; B002 selected. All other branches rejected.
- Generating set: ر ب ب B011 + ص ل و B003 + ن ح ر B002 + ش ن ء B001 + ب ت ر B002.
- Frozen model: gift establishes protected obligation to Lord; hostility is outside and severed.
- Predictions at freeze: possessive/dedication markers.
- Corroborators: `لِرَبِّكَ` supplies dedication/loyalty; basmala opening-context weakly supports divine protection/mercy.
- Constraints: no explicit oath/covenant term.
- Rival forks: none.
- Grade: medium.

#### L34 — ر ب ب B012 — green plant continuity terminates

- Initial image: persistent green plant predicts botanical life `(E: ر ب ب B012)`.
- Visit audit: ك ث ر B006 and ص ل و B009 plant branches tested; ن ح ر and ع ط و full dossiers visited; no selected branch survives. ش ن ء and ب ت ر full dossiers visited; no selection.
- Generating set: ر ب ب B012.
- Frozen model: plant growth.
- Predictions at freeze: plant/water/cultivation.
- Corroborators: none.
- Constraints: no plant terms; worship/hater/predicate do not complete plant roles.
- Rival forks: none.
- Grade: unlikely.

#### L35 — ر ب ب B013 — plentiful water abundance

- Initial image: much/sweet water predicts flowing plenty `(E: ر ب ب B013)`.
- Visit audit: ع ط و full dossier visited; B002 selected. ك ث ر full dossier visited; B001 selected, B005 weak. ص ل و full dossier visited; all rejected. ن ح ر full dossier visited; B009 selected, B002 rejected for different model. ش ن ء full dossier visited; no selection. ب ت ر full dossier visited; B002 post-freeze anti-continuity.
- Generating set: ر ب ب B013 + ك ث ر B001 + ن ح ر B009 + ع ط و B002.
- Frozen model: gift simulated as plentiful water.
- Predictions at freeze: flow/plenty; severance as anti-flow.
- Corroborators: general abundance supports plenty; بتر B002 opposes continuity.
- Constraints: no explicit water word in S108.
- Rival forks: cloud-water image overlaps L30/L47.
- Grade: medium.

#### L36 — ر ب ب B014 — herd and animal sacrifice

- Initial image: herd/group of cattle/camels predicts animal collectivity `(E: ر ب ب B014)`.
- Visit audit: ع ط و full dossier visited; B002 weak. ك ث ر full dossier visited; B001 selected as herd abundance. ص ل و full dossier visited; B003 weak ritual. ن ح ر full dossier visited; B002 selected. ش ن ء and ب ت ر full dossiers visited; no selection except final outsider contrast.
- Generating set: ر ب ب B014 + ن ح ر B002 + ك ث ر B001.
- Frozen model: abundant animals offered in slaughter.
- Predictions at freeze: animal/herd terms.
- Corroborators: نحر B002 supplies animal sacrificial action.
- Constraints: no herd noun; `رَبِّكَ` is Lord, not herd.
- Rival forks: sacrifice branch survives only through نحر.
- Grade: weak.

#### L37 — ر ب ب B015 — particle رب is morphologically blocked

- Initial image: particle `رب/ربما` predicts particle syntax `(E: ر ب ب B015)`.
- Visit audit: all other root dossiers visited; no branch selected.
- Generating set: ر ب ب B015.
- Frozen model: particle of quantity/probability.
- Predictions at freeze: particle syntax.
- Corroborators: none.
- Constraints: QAC parses `رَبِّ` as noun stem with genitive and 2MS suffix governed by `لِ`.
- Rival forks: none.
- Grade: unlikely.

#### L38 — ر ب ب B016 — need/knot/blessing binds response

- Initial image: need/blessing/knot predicts granted favor binding recipient `(E: ر ب ب B016)`.
- Visit audit: ع ط و full dossier visited; B002 selected, B005 rejected. ك ث ر full dossier visited; B001 selected. ص ل و full dossier visited; B003 selected. ن ح ر full dossier visited; B002 weak. ش ن ء full dossier visited; B001 post-freeze. ب ت ر full dossier visited; B002 post-freeze.
- Generating set: ر ب ب B016 + ع ط و B002 + ك ث ر B001 + ص ل و B003.
- Frozen model: abundant blessing creates binding obligation to the Lord.
- Predictions at freeze: dedication and exclusion of anti-blessing.
- Corroborators: imperatives and `لِرَبِّكَ` supply binding dedication; بتر B002 contrasts loss of good.
- Constraints: no explicit need/knot term.
- Rival forks: none.
- Grade: medium.

#### L39 — ر ب ب B017 — chief pilot terminates

- Initial image: leader of sailors predicts navigation/crew `(E: ر ب ب B017)`.
- Visit audit: all other root dossiers visited; no branch selected.
- Generating set: ر ب ب B017.
- Frozen model: nautical leadership.
- Predictions at freeze: ship, sea, pilot, crew.
- Corroborators: none.
- Constraints: no nautical terms; `ربك` is dedication to Lord.
- Rival forks: none.
- Grade: unlikely.

### 5.5 108:2:3 `وَٱنْحَرْ` / ن ح ر

#### L40 — ن ح ر B001 — front/chest orientation

- Initial image: exposed upper chest/front predicts facing or bodily presentation `(E: ن ح ر B001)`.
- Visit audit: ع ط و full dossier visited; B002 weak cause. ك ث ر full dossier visited; B001 weak gift. ص ل و full dossier visited; B003 selected. ر ب ب full dossier visited; B001 selected. ش ن ء full dossier visited; B001 post-freeze orientation opponent. ب ت ر full dossier visited; B002 post-freeze.
- Generating set: ن ح ر B001 + ص ل و B003 + ر ب ب B001.
- Frozen model: addressee presents/fronts himself in worship to Lord.
- Predictions at freeze: directional/dedication relation and opposed orientation.
- Corroborators: `لِرَبِّكَ` supplies direction/dedication; `شَانِئَكَ` supplies adversarial orientation.
- Constraints: local imperative more strongly supports slaughter/facing act than body-place alone.
- Rival forks: B002 ritual cut and B003 facing.
- Grade: medium.

#### L41 — ن ح ر B002 — sacrificial cut without becoming cut off

- Initial image: throat/chest slaughter predicts controlled dedicated cutting `(E: ن ح ر B002)`.
- Visit audit: ع ط و full dossier visited; B002 selected. ك ث ر full dossier visited; B001 selected. ص ل و full dossier visited; B003 selected. ر ب ب full dossier visited; B001 selected. ش ن ء full dossier visited; B001 post-freeze. ب ت ر full dossier visited; B001/B002 post-freeze contrast, B004/B006 rejected.
- Generating set: ن ح ر B002 + ص ل و B003 + ر ب ب B001 + ع ط و B002 + ك ث ر B001.
- Frozen model: abundance answered by consecrated cutting/offering to Lord.
- Predictions at freeze: another cutting field may appear as destructive contrast.
- Corroborators: بتر B001 gives destructive/incomplete cutting; بتر B002 assigns lost good/trace to hater.
- Constraints: `نحر` must not be redirected against the hater because it is conjoined to prayer before the enemy clause.
- Rival forks: B003 orientation instead of slaughter.
- Grade: medium-strong.

#### L42 — ن ح ر B003 — facing the Lord, opposed by the hater

- Initial image: face-to-face orientation predicts alignment/opposition `(E: ن ح ر B003)`.
- Visit audit: ع ط و full dossier visited; B002 post-freeze cause. ك ث ر full dossier visited; B001 post-freeze gift. ص ل و full dossier visited; B003 selected. ر ب ب full dossier visited; B001 selected. ش ن ء full dossier visited; B001 selected. ب ت ر full dossier visited; B002 post-freeze.
- Generating set: ن ح ر B003 + ص ل و B003 + ر ب ب B001 + ش ن ء B001.
- Frozen model: addressee turns toward Lord while hater turns against him.
- Predictions at freeze: verdict decides which orientation has continuity.
- Corroborators: gift/abundance provides reason for turning to Lord; بتر B002 cuts off hostile orientation.
- Constraints: B003 is secondary to the ritual-sacrifice reading in the paired imperative.
- Rival forks: B002 sacrificial action.
- Grade: medium-strong.

#### L43 — ن ح ر B004 — mutual conflict over abundance is syntactically blocked

- Initial image: fierce تناحر over a thing predicts reciprocal conflict `(E: ن ح ر B004)`.
- Visit audit: ع ط و full dossier visited; B004/B007 selected as contest support. ك ث ر full dossier visited; B002 selected. ص ل و full dossier visited; all rejected/constraint. ر ب ب full dossier visited; B001 constraint. ش ن ء full dossier visited; B001 selected. ب ت ر full dossier visited; B001/B002 selected.
- Generating set: ن ح ر B004 + ش ن ء B001 + ك ث ر B002 + ب ت ر B001/B002.
- Frozen model: conflict over abundance resolves with hostile party cut off.
- Predictions at freeze: enemy and verdict.
- Corroborators: `شانئك` and `الأبتر` fit conflict/outcome.
- Constraints: `وانحر` is a 2MS imperative joined to prayer, not reciprocal fight.
- Rival forks: rivalry family L04/L09.
- Grade: weak-to-medium.

#### L44 — ن ح ر B005 — self-slaughter defeated

- Initial image: self-slaughter/suicide predicts reflexive destruction `(E: ن ح ر B005)`.
- Visit audit: all other root dossiers visited; no branch selected.
- Generating set: ن ح ر B005.
- Frozen model: self-destruction.
- Predictions at freeze: reflexive/self object.
- Corroborators: none.
- Constraints: imperative is conjoined with prayer and directed to Lord; final destruction belongs to hater.
- Rival forks: none.
- Grade: unlikely.

#### L45 — ن ح ر B006 — temporal boundary facing boundary

- Initial image: time-edge facing time-edge predicts boundary/transition `(E: ن ح ر B006)`.
- Visit audit: ع ط و full dossier visited; B002 selected as first state. ك ث ر full dossier visited; B001 selected as state content. ص ل و full dossier visited; B003 selected as second state. ر ب ب full dossier visited; B001 selected as target. ش ن ء full dossier visited; B001 selected as third-state entrant. ب ت ر full dossier visited; B001 selected as closure, B002 support.
- Generating set: ن ح ر B006 + ب ت ر B001 + sequence structure.
- Frozen model: ayah 2 is a threshold between gift and verdict.
- Predictions at freeze: ayah-boundary role and sharp close.
- Corroborators: surah pivots gift→response→verdict; closure after `الأبتر` is sharp.
- Constraints: no explicit temporal noun; branch remote from imperative surface.
- Rival forks: none.
- Grade: weak.

#### L46 — ن ح ر B008 — expert mastery absent

- Initial image: expert/experienced mastery predicts skill/knowledge `(E: ن ح ر B008)`.
- Visit audit: all other root dossiers visited; no branch selected.
- Generating set: ن ح ر B008.
- Frozen model: skilled expert action.
- Predictions at freeze: knowledge/mastery vocabulary.
- Corroborators: none.
- Constraints: no expert term; imperative asks an act, not expertise.
- Rival forks: none.
- Grade: unlikely.

#### L47 — ن ح ر B009 — cloudburst abundance

- Initial image: cloud pouring abundant water predicts descending plenty `(E: ن ح ر B009)`.
- Visit audit: ع ط و full dossier visited; B002 selected as gift. ك ث ر full dossier visited; B001/B005 selected, rest rejected. ص ل و full dossier visited; all rejected. ر ب ب full dossier visited; B008/B013 selected, rest rejected. ش ن ء full dossier visited; no selection. ب ت ر full dossier visited; B002 post-freeze anti-continuity.
- Generating set: ن ح ر B009 + ك ث ر B001/B005 + ر ب ب B008/B013 + ع ط و B002.
- Frozen model: gift as descending/pouring abundance.
- Predictions at freeze: water/cloud/flow imagery and blocked severance.
- Corroborators: abundance supports overflowing plenty; abtar opposes continuity.
- Constraints: no local water/cloud term; `انحر` is conjoined to prayer and likely an act.
- Rival forks: overlaps L30/L35.
- Grade: weak-to-medium.

### 5.6 108:3:2 `شَانِئَكَ` / ش ن ء

#### L48 — ش ن ء B001 — the hater is the excluded cut-off

- Initial image: hatred/enmity predicts an opposed agent directed at the addressee `(E: ش ن ء B001)`.
- Visit audit: ع ط و full dossier visited; B002 selected as prior gift target, B004/B007 rival support, rest rejected. ك ث ر full dossier visited; B001 selected, B002 rivalry support, rest rejected. ص ل و full dossier visited; B003 post-freeze relation protection, rest rejected. ر ب ب full dossier visited; B001 post-freeze relation protection, B002 weak, rest rejected. ن ح ر full dossier visited; B002/B003 post-freeze relation/action, B004 rivalry support, rest rejected. ب ت ر full dossier visited; B002 selected, B001 support, B004/B006 rejected.
- Generating set: ش ن ء B001 + ب ت ر B002 + ك ث ر B001 + ع ط و B002.
- Frozen model: enemy of the recipient of abundance is himself severed from good/trace.
- Predictions at freeze: emphatic identification of enemy as bearer of severance; backward reactivation of gift.
- Corroborators: `هُوَ` isolates the hater; worship/sacrifice/Lord relation shows addressee’s stable attachment.
- Constraints: seed starts late, so it explains the opening only by retrospective reactivation.
- Rival forks: ش ن ء B004 character-judgment model weaker.
- Grade: strong.

#### L49 — ش ن ء B002 — revulsion/distance is weak

- Initial image: disgusted distancing from impurity predicts separation from what is considered defiled `(E: ش ن ء B002)`.
- Visit audit: ع ط و full dossier visited; no selection. ك ث ر full dossier visited; B001 weak as good being rejected. ص ل و full dossier visited; B003 selected as purity/opposed field weakly. ر ب ب full dossier visited; B001 selected as pure Lord-relation weakly. ن ح ر full dossier visited; no selection. ب ت ر full dossier visited; B002 selected as separation.
- Generating set: ش ن ء B002 + ب ت ر B002 + ر ب ب B001 + ص ل و B003.
- Frozen model: opponent distances himself and becomes separated from abundance/good.
- Predictions at freeze: purity/impurity or distance markers.
- Corroborators: final severance fits distancing.
- Constraints: no impurity/disgust vocabulary; active participle context favors hatred.
- Rival forks: none.
- Grade: weak.

#### L50 — ش ن ء B003 — acknowledging/extracting a right absent

- Initial image: acknowledging a right and bringing it out predicts confession/payment/removal `(E: ش ن ء B003)`.
- Visit audit: ع ط و full dossier visited; B002 tested as transfer, rejected. ك ث ر full dossier visited; no selection. ص ل و, ر ب ب, ن ح ر full dossiers visited; no selection. ب ت ر full dossier visited; B001/B002 tested as removal/loss, rejected.
- Generating set: ش ن ء B003.
- Frozen model: someone acknowledges or disgorges a right.
- Predictions at freeze: confession/right/object extraction.
- Corroborators: none.
- Constraints: `شَانِئَكَ` is active participle in enemy slot; following predicate is `الأبتر`, not confession.
- Rival forks: no explicit حق, so dies.
- Grade: unlikely.

#### L51 — ش ن ء B004 — repulsive/ugly opponent as condemnation

- Initial image: bad/repulsive descriptor predicts negative character judgment `(E: ش ن ء B004)`.
- Visit audit: ع ط و full dossier visited; B002 prior gift weak. ك ث ر full dossier visited; B001 contrast weak. ص ل و, ر ب ب, ن ح ر full dossiers visited; no pre-freeze selection. ب ت ر full dossier visited; B002 selected. ش ن ء B001 held as distinct hatred dimension after freeze.
- Generating set: ش ن ء B004 + ب ت ر B002.
- Frozen model: repulsive opponent is marked by loss of good/mention.
- Predictions at freeze: predicative condemnation.
- Corroborators: `هو الأبتر` is predicative condemnation; B001 hatred dimension corroborates enemy relation if held unused.
- Constraints: B004 is secondary; B001 is local active-participle sense.
- Rival forks: none.
- Grade: medium.

### 5.7 108:3:4 `ٱلْأَبْتَرُ` / ب ت ر

#### L52 — ب ت ر B001 — destructive cutting versus consecrated cutting

- Initial image: cutting before completion predicts truncation/destructive severance `(E: ب ت ر B001)`.
- Visit audit: ع ط و full dossier visited; B002 post-freeze gift, rest rejected. ك ث ر full dossier visited; B001 selected, rest rejected. ص ل و full dossier visited; B003 post-freeze devotion, rest rejected. ر ب ب full dossier visited; B002 selected, B001 post-freeze target, rest rejected. ن ح ر full dossier visited; B002 selected as controlled cutting, B003 weak, rest rejected. ش ن ء full dossier visited; B001 selected, rest rejected.
- Generating set: ب ت ر B001 + ر ب ب B002 + ك ث ر B001 + ن ح ر B002 + ش ن ء B001.
- Frozen model: hostile one receives destructive cut; addressee’s cut, if any, is consecrated.
- Predictions at freeze: distinction between cut-as-offering and cut-as-loss.
- Corroborators: `وانحر` is conjoined to prayer and directed to Lord, not enemy; gift/abundance gives completion field threatened by cutting.
- Constraints: `الأبتر` is predicate of `شانئك`, not a command to cut.
- Rival forks: B002 is closer to surface adjective.
- Grade: medium-strong.

#### L53 — ب ت ر B002 — loss of posterity/mention/good closes the surah

- Initial image: being cut off from posterity/mention/good predicts final verdict and abundance contrast `(E: ب ت ر B002)`.
- Visit audit: ع ط و full dossier visited; B002 selected, B003/B006 weak, rest rejected. ك ث ر full dossier visited; B001 selected, B002 rival, rest rejected. ص ل و full dossier visited; B003 post-freeze relation, B002 weak, rest rejected. ر ب ب full dossier visited; B001/B002 post-freeze continuity, rest rejected. ن ح ر full dossier visited; B002/B003 post-freeze ritual/orientation, B004 rival conflict, rest rejected. ش ن ء full dossier visited; B001 selected, B004 weak, rest rejected.
- Generating set: ب ت ر B002 + ك ث ر B001 + ع ط و B002 + ش ن ء B001.
- Frozen model: addressee has bestowed abundance; enemy is deprived of continuing good/trace.
- Predictions at freeze: emphatic assignment to enemy and closure after verdict.
- Corroborators: `هُوَ` focuses predicate on hater; prayer/sacrifice/Lord relation maintains recipient’s continuity.
- Constraints: posterity/mention is branch content, not locally specified by explicit lineage noun.
- Rival forks: B001 mechanical cut.
- Grade: strong.

#### L54 — ب ت ر B004 — kinship severance as relational geometry

- Initial image: cutting kinship predicts relational rupture `(E: ب ت ر B004)`.
- Visit audit: ع ط و full dossier visited; B002 selected as relation giver→you. ك ث ر full dossier visited; B001 weak. ص ل و full dossier visited; B003 relation to Lord. ر ب ب full dossier visited; B001 selected. ن ح ر full dossier visited; no selection. ش ن ء full dossier visited; B001 selected. Other branches rejected.
- Generating set: ب ت ر B004 + ش ن ء B001 + ر ب ب B001.
- Frozen model: hater is cut from the relational network around the addressee and Lord.
- Predictions at freeze: relational suffixes should matter.
- Corroborators: `كَ` chain organizes given-to-you, your Lord, your hater; predicate severs hater.
- Constraints: no kinship/رحم term; `ربك` is not kinship.
- Rival forks: none.
- Grade: medium.

#### L55 — ب ت ر B006 — shortened/truncated body is weak

- Initial image: shortened body/form predicts physical truncation `(E: ب ت ر B006)`.
- Visit audit: ع ط و, ك ث ر, ر ب ب, ش ن ء full dossiers visited; no selection. ص ل و full dossier visited; B005 tested weakly. ن ح ر full dossier visited; B001 tested weakly.
- Generating set: ب ت ر B006 + optional ن ح ر B001 + optional ص ل و B005.
- Frozen model: bodily truncation image.
- Predictions at freeze: body shape, stature, tail/limb.
- Corroborators: نحر B001 offers body location only weakly.
- Constraints: `الأبتر` is a moral/social verdict predicate of hater; no bodily shortness is described.
- Rival forks: animal-body fork overlaps L18 but weak.
- Grade: weak.

## 6. Exhaustive constructional, morphosyntactic, temporal, and acoustic seeds

The following are the eligible non-lexical seeds detected from QAC, attachment rows, word order, ayah boundaries, repetition, and surface recurrence. They do not initiate from basmala. Each construction seed tested all seven interval root dossiers listed in §3.

#### C01 — construction: `إِنَّا أَعْطَيْنَٰكَ ٱلْكَوْثَرَ`

- Initial image: emphatic completed gift: divine/plural subject → addressee → abundant object.
- Full-root visit audit: all seven root dossiers tested; selected `(E: ع ط و B002; E: ك ث ر B001)`.
- Generating set: `إنّا` predication + ع ط و B002 + ك ث ر B001.
- Frozen model: recipient is secured by completed abundance transfer.
- Predictions at freeze: next material should answer or protect the gift.
- Corroborators: `فَصَلِّ` answers gift; final `الأبتر` protects by contrast `(C: ب ت ر B002)`.
- Constraints: exact referent of `الكوثر` remains unspecified.
- Grade: strong.

#### C02 — construction: direct-object completion `أَعْطَيْنَٰكَ` → `ٱلْكَوْثَرَ`

- Initial image: `أَعْطَيْنَٰكَ` leaves an object slot open; `ٱلْكَوْثَرَ` completes it.
- Full-root visit audit: all root dossiers tested; selected `(E: ع ط و B002; E: ك ث ر B001)`.
- Generating set: attachment 108:1 a3/a4 + gift root + abundance root.
- Frozen model: the recitation moves from unresolved transfer to specified abundance.
- Predictions at freeze: consequence should follow completed object.
- Corroborators: `فَـ` at 108:2 gives consequence; final `الأبتر` reactivates object by polarity.
- Constraints: object completion is structural, not a new lexical branch.
- Grade: strong.

#### C03 — construction: `فَصَلِّ لِرَبِّكَ وَٱنْحَرْ`

- Initial image: consequential paired imperatives after gift.
- Full-root visit audit: all root dossiers tested; selected `(E: ص ل و B003; E: ر ب ب B001; E: ن ح ر B002)` with ن ح ر B003 as rival facing fork.
- Generating set: فـ response + two imperatives + Lord complement.
- Frozen model: gift-response system: worship and offering/facing act to Lord.
- Predictions at freeze: final clause should resolve opposition, not add another command.
- Corroborators: hater is outside imperative relation and receives cut-off predicate.
- Constraints: نحر cannot be enemy-directed violence.
- Grade: strong.

#### C04 — construction: `صَلِّ` + `لِرَبِّكَ` prepositional attachment

- Initial image: prayer/worship is specifically dedicated to the Lord.
- Full-root visit audit: all root dossiers tested; selected `(E: ص ل و B003/B002; E: ر ب ب B001)`.
- Generating set: attachment 108:2 a1 + prayer + Lordship.
- Frozen model: the response to abundance is not generic gratitude but directed devotion.
- Predictions at freeze: the other imperative should share or follow this dedication field.
- Corroborators: attachment 108:2 a3 joins `وانحر` to `صل`; final hater clause is separate.
- Constraints: no locative reading of `لـ`; it is dedication/complement.
- Grade: medium-strong.

#### C05 — construction: conjoined imperative pair `فَصَلِّ ... وَٱنْحَرْ`

- Initial image: two coordinated 2MS commands make a paired response.
- Full-root visit audit: all root dossiers tested; selected `(E: ص ل و B003; E: ن ح ر B002/B003; E: ر ب ب B001)`.
- Generating set: imperative morphology + conjunction + Lord complement.
- Frozen model: response has two modes: worship and offering/facing.
- Predictions at freeze: enemy clause should not govern either imperative.
- Corroborators: attachment row confirms `وانحر` is conjoined to `صل`, while `الأبتر` predicates the hater.
- Constraints: blocks fight/self-harm branches of نحر.
- Grade: medium-strong.

#### C06 — construction: `إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ`

- Initial image: emphatic verdict: enemy-of-you = he himself the cut-off.
- Full-root visit audit: all root dossiers tested; selected `(E: ش ن ء B001; E: ب ت ر B002)`.
- Generating set: `إنّ` + active participle + focus pronoun + definite predicate.
- Frozen model: late enemy clause reverses threat to addressee.
- Predictions at freeze: it should reactivate earlier gift-to-you structure.
- Corroborators: `كَ` in `شانئك` reactivates `أعطيناك` and `ربك`; ك ث ر B001 supplies polarity.
- Constraints: by itself does not generate the middle imperative pair.
- Grade: strong.

#### C07 — construction: final predicate focus `هُوَ ٱلْأَبْتَرُ`

- Initial image: `هُوَ` separates/focuses the predicate on the hater.
- Full-root visit audit: all root dossiers tested; selected `(E: ش ن ء B001; E: ب ت ر B002/B001)`.
- Generating set: attachment 108:3 a3 + focus pronoun + abtar.
- Frozen model: closure occurs when the correct bearer of severance is identified.
- Predictions at freeze: no further action is required after verdict.
- Corroborators: polarity with `الكوثر`; attachment prevents severance from attaching to the addressee.
- Constraints: focus is structural, not a separate lexical root.
- Grade: medium-strong.

#### C08 — polarity construction: `ٱلْكَوْثَرَ` ↔ `ٱلْأَبْتَرُ`

- Initial image: surplus/increase versus severance/loss.
- Full-root visit audit: all root dossiers tested; selected `(E: ك ث ر B001; E: ب ت ر B002)`.
- Generating set: gift object + final predicate.
- Frozen model: abundance assigned to addressee; severance assigned to hater.
- Predictions at freeze: middle command should show proper inhabiting of abundance rather than boasting.
- Corroborators: worship/offering to Lord channels abundance; `شانئك` supplies excluded bearer.
- Constraints: polarity alone is static; middle ayah supplies response mechanism.
- Grade: strong.

#### C09 — pronoun-chain seed: repeated `كَ`

- Initial image: same addressee recurs as gift recipient, Lord-possessor, and hater’s object.
- Full-root visit audit: all root dossiers tested; selected `(E: ع ط و B002; E: ر ب ب B001; E: ش ن ء B001; E: ب ت ر B002)`.
- Generating set: 2MS suffix in `أعطيناك`, `ربك`, `شانئك`.
- Frozen model: addressee is relational hub: secured by gift, obligated to Lord, opposed by hater.
- Predictions at freeze: final predicate should attach to hater, not addressee.
- Corroborators: `هُوَ` + attachment row 108:3 a3 force predicate onto `شانئك`.
- Constraints: suffix chain alone cannot specify abundance/prayer content.
- Grade: medium-strong.

#### C10 — temporal seed: ayah sequence gift → response → verdict

- Initial image: three state transition: secured gift, required response, hostile closure.
- Full-root visit audit: all root dossiers tested; selected `(E: ع ط و B002; E: ك ث ر B001; E: ص ل و B003; E: ر ب ب B001; E: ن ح ر B002; E: ش ن ء B001; E: ب ت ر B002)`.
- Generating set: ordered clauses and ayah boundaries.
- Frozen model: abundance is activated into worship, then defended by verdict.
- Predictions at freeze: shuffled order would weaken backward reactivation of gift by final predicate.
- Corroborators: basmala opening-context supports divine-source opening; `هُوَ` sharpens final stop.
- Constraints: temporal seed is structural, not lexical meaning.
- Grade: strong.

#### C11 — repetition seed: two `إِنَّ` frames

- Initial image: the surah is framed by two emphatic assertions: first about divine giving, then about enemy severance.
- Full-root visit audit: all root dossiers tested; selected `(E: ع ط و B002; E: ك ث ر B001; E: ش ن ء B001; E: ب ت ر B002)`.
- Generating set: 108:1 `إِنَّا` + 108:3 `إِنَّ`.
- Frozen model: emphasis brackets the gift and the verdict.
- Predictions at freeze: middle imperative should stand as consequence between two certainties.
- Corroborators: `فَصَلِّ` as consequence; `هُوَ` intensifies second frame.
- Constraints: `إنّ` is unrooted structural evidence, not lexical branch.
- Grade: medium-strong.

#### C12 — definiteness seed: `ٱلْكَوْثَرَ` and `ٱلْأَبْتَرُ`

- Initial image: two definite marked nouns/adjectives create a determinate polarity: the abundance, the cut-off.
- Full-root visit audit: all root dossiers tested; selected `(E: ك ث ر B001; E: ب ت ر B002)`.
- Generating set: DET morphology on object and final predicate.
- Frozen model: the passage establishes two determinate states and assigns them to different parties.
- Predictions at freeze: grammar should separate bearers.
- Corroborators: object attachment assigns `الكوثر` to addressee through giving; predicate attachment assigns `الأبتر` to hater.
- Constraints: definiteness alone does not identify referents beyond local grammar.
- Grade: medium.

#### C13 — consequence seed: `فَـ` in `فَصَلِّ`

- Initial image: the imperative is temporally/logically consequent on the prior gift.
- Full-root visit audit: all root dossiers tested; selected `(E: ع ط و B002; E: ك ث ر B001; E: ص ل و B003; E: ر ب ب B001)`.
- Generating set: فـ + gift clause + worship command.
- Frozen model: abundance produces commanded dedication.
- Predictions at freeze: no boasting/competition should be needed for the addressee.
- Corroborators: final hater clause bears cut-off, not the recipient; كثر B002 competition is displaced to the enemy-side only.
- Constraints: فـ is structural evidence, not lexical branch.
- Grade: medium-strong.

#### C14 — acoustic/phonological recurrence seed: terminal `-ar` resonance (`كوثر/انحر/أبتر`)

- Initial image: surface recurrence of emphatic final-r-like cadence links abundance, nahr action, and abtar verdict as auditory anchors.
- Full-root visit audit: all root dossiers tested; selected as semantic anchors `(E: ك ث ر B001; E: ن ح ر B002/B003; E: ب ت ر B002)`.
- Generating set: acoustic recurrence plus the three rooted words.
- Frozen model: sound recurrence helps maintain temporary activation from `الكوثر` through `انحر` to `الأبتر`.
- Predictions at freeze: later `الأبتر` should reactivate earlier `الكوثر` more strongly than an unrelated ending would.
- Corroborators: semantic polarity confirms the sound link is not merely rhyme.
- Constraints: acoustic recurrence cannot by itself generate doctrine or lexical content; it is temporal-memory support only.
- Grade: medium.

## 7. Potentially missing images generated in Pass 2

Compared with Pass 1, the lexical seed inventory was already complete, but Pass 2 makes three image families more explicit because they were under-audited:

1. Consequence and object-slot completion: `أَعْطَيْنَٰكَ` creates an unresolved object slot that `ٱلْكَوْثَرَ` fills, then `فَـ` converts completion into response.
2. Emphatic bracketing: the two `إنّ` frames bracket the surah as certainty of gift and certainty of opponent’s severance.
3. Acoustic recurrence: `الكوثر / انحر / الأبتر` forms a temporal memory chain that supports, but does not replace, the semantic reactivation.

No additional lexical seeds were found beyond the 55 accepted uncontaminated branch seeds listed above.

## 8. Convergence judgment

Strongest convergent model:

```text
completed divine gift
  → abundant object assigned to the addressee
  → consequential worship/offering to the Lord
  → hostile third party appears
  → final focus assigns severance to the hater
  → abundance is retrospectively reactivated by its opposite
```

Independent seed families converging on this model:

- Gift/transfer seeds: L02, C01, C02.
- Abundance/polarity seeds: L08, C08, C12.
- Worship/response seeds: L16, C03, C04, C05, C13.
- Lord/source/completion seeds: L23, L24.
- Offering/facing/cutting seeds: L41, L42, L52.
- Enemy/verdict seeds: L48, L53, C06, C07.
- Temporal/repetition/acoustic seeds: C09, C10, C11, C14.

Remote or failed images are preserved rather than omitted: petition, trap, pounding stone, pasture plant, food/medicine, arrow-container, nautical leadership, self-slaughter, expert mastery, plant, cloud-water, body truncation, and others terminate because local syntax, morphology, or role structure fails to support them.

## 9. Exhaustiveness self-check

Expected lexical seed count: 55.

Lexical seed headings present:

- ع ط و: L01–L07 = 7.
- ك ث ر: L08–L13 = 6.
- ص ل و: L14–L22 = 9.
- ر ب ب: L23–L39 = 17.
- ن ح ر: L40–L47 = 8.
- ش ن ء: L48–L51 = 4.
- ب ت ر: L52–L55 = 4.

Expected construction/morphosyntactic/temporal/acoustic seeds: at least all actual S108 constructions detected from QAC/attachments/order/repetition. Present: C01–C14 = 14.

Every lexical seed card now has an explicit visit audit naming the full other-root dossier sweep and selected/rejected status. Every construction seed states that all seven interval root dossiers were tested. No Stage 1 Pass 2 output files outside `v1/outputs/108_comparator/` were created.
