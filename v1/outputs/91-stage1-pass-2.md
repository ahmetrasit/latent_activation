# S91 Stage 1 Pass 2 - Temporally Conditioned Reactivation

Assigned passage: S91  
Sacred Arabic text: `resources/quran/surah_91.json`  
Prompt: `v1/prompts/stage1.md`  
Output: `v1/outputs/91-stage1-pass-2.md`

## Pass 2 Restart Note

Root cause of the Pass 1 limitation: the prompt-named SQLite resources `resources/qac.sqlite` and `resources/furuq_v4.sqlite` are absent in this workspace. The available lexical data are TSV exports: `resources/qac_root_ayah.tsv` and `resources/v4_branches.tsv`. I used those TSV exports as stand-ins for QAC/root occurrence and uncontaminated v4 branch dossiers, and `resources/attachments.tsv` for S91 structural rows. No translation was used.

The restart begins from the first rooted word in S91, `ٱلشَّمْسِ` root `ش م س`, and treats every accepted branch of every S91 rooted occurrence as an initiated seed. Repeated roots were considered occurrence-sensitively where position matters: `س و ي` at 91:7 and 91:14, `ك ذ ب` at 91:11 and 91:14, and `ء ل ه` in `رَسُولُ ٱللَّهِ` and `نَاقَةَ ٱللَّهِ`.

## Sacred Text Sequence

91:1 `وَٱلشَّمْسِ وَضُحَىٰهَا`  
91:2 `وَٱلْقَمَرِ إِذَا تَلَىٰهَا`  
91:3 `وَٱلنَّهَارِ إِذَا جَلَّىٰهَا`  
91:4 `وَٱلَّيْلِ إِذَا يَغْشَىٰهَا`  
91:5 `وَٱلسَّمَآءِ وَمَا بَنَىٰهَا`  
91:6 `وَٱلْأَرْضِ وَمَا طَحَىٰهَا`  
91:7 `وَنَفْسٍۢ وَمَا سَوَّىٰهَا`  
91:8 `فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا`  
91:9 `قَدْ أَفْلَحَ مَن زَكَّىٰهَا`  
91:10 `وَقَدْ خَابَ مَن دَسَّىٰهَا`  
91:11 `كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ`  
91:12 `إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا`  
91:13 `فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا`  
91:14 `فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا`  
91:15 `وَلَا يَخَافُ عُقْبَٰهَا`

## Source Rows Used

- `resources/quran/surah_91.json`: all S91 ayat.
- `resources/qac_root_ayah.tsv`: S91 root rows for 36 distinct roots.
- `resources/v4_branches.tsv`: accepted branch rows for those 36 roots, 286 accepted branch seeds before occurrence duplication.
- `resources/attachments.tsv`: S91 rows only, including oath complements, suffix objects, idafa, coordinated pairs, quoted complement, causal and target prepositional complements, and temporal `إِذَا` / `إِذِ` rows.

## Exhaustive Root And Branch Seed Ledger

Each branch listed here was initiated as a seed. Outcomes: `CAND-x` means it produced or converged into a candidate below; `LOCAL` means it produced a local image but did not explain the passage sequence; `TERMINATED` means no passage-local expansion survived after testing morphology, attachment, and order.

| Occurrence | Root | Accepted branches initiated | Pass 2 outcome |
| --- | --- | --- | --- |
| 91:1 `ٱلشَّمْسِ` | `ش م س` | B001 sun/brightness; B002 shying/restive animal or character; B003 open enmity; B004 necklace ornaments; B005 Christian deacon; B006 withholding/buckling; B007 naming by sun | B001 -> CAND-01; B002/B003 -> LOCAL constraint against later rebellion; B004-B007 TERMINATED |
| 91:1 `ضُحَىٰهَا` | `ض ح و` | B001 extension of forenoon; B002 exposure to sun; B003 early meal/pasture; B004 sacrifice; B005 brightness/clarity | B001/B002/B005 -> CAND-01; B003 -> LOCAL pasture echo with CAND-05; B004 TERMINATED |
| 91:2 `ٱلْقَمَرِ` | `ق م ر` | B001 moon/light; B002 pale whiteness; B003 qamra hunting; B004 cold-damaged date; B005 dazzled eye; B006 waterskin spoiled by moonlight; B007 gambling/deceptive winning; B008 abundant water/pasture; B009 sleeplessness; B010 late camel supper; B011 leaving wealth at night; B012 dove | B001/B002/B005 -> CAND-01; B008/B010 -> LOCAL echo with camel/water; B007 -> weak rival deception frame; others TERMINATED |
| 91:2 `تَلَىٰهَا` | `ت ل و` | B001 following/succession; B003 remainder; B004 obligation/guarantee following owner; B005 abandonment after companionship; B006 offspring following mother; B007 voice following voice; B008 last breath; B009 false saying against another | B001 -> CAND-01; B006 -> LOCAL camel/offpsring echo; B009 -> CAND-05 as later false attribution; B003/B004/B005/B007/B008 TERMINATED or weak local |
| 91:3 `ٱلنَّهَارِ` | `ن ه ر` | B001 river channel; B002 daylight opening; B003 opening/widening until flow; B004 harsh rebuke; B006 snatching; B007 proper names; B008 cloud | B002/B003 -> CAND-01; B001 -> LOCAL water-flow echo; B004 -> LOCAL warning-speech constraint; B006-B008 TERMINATED |
| 91:3 `جَلَّىٰهَا` | `ج ل و` | B001 disclosure/appearance; B002 polishing; B003 bridal display; B004 exile from homeland; B005 bald front; B006 public fame; B007 white day/clear weather; B008 looking out; B009 bride gift | B001/B002/B007 -> CAND-01; B003 -> weak exposure rival; B004 -> LOCAL uprooting echo; B005/B006/B008/B009 TERMINATED |
| 91:4 `ٱلَّيْلِ` | `ل ي ل` | B001 night/darkness; B002 action by night; B003 nearest night; B004 name Layla | B001 -> CAND-01; B002/B003 LOCAL temporal; B004 TERMINATED |
| 91:4 `يَغْشَىٰهَا` | `غ ش و` | B001 covering; B002 comprehensive envelopment; B003 coming upon a target; B004 intercourse; B005 unconscious covering; B006 laying on a blow; B007 whiteness covering an animal face | B001/B002 -> CAND-01; B003 -> LOCAL approach; B006 -> weak violence echo; B004/B005/B007 TERMINATED |
| 91:5 `ٱلسَّمَآءِ` | `س م و` | B001 elevation; B002 elevated visible person/object; B003 stallion rising; B004 sky/what is above and shades; B005 name/dalalah; B006 going out hunting; B007 rivalry in loftiness; B008 good fame spread | B001/B004 -> CAND-02; B005 -> CAND-05 divine naming/idafa echo; B007 -> LOCAL rivalry; others TERMINATED |
| 91:5 `بَنَىٰهَا` | `ب ن ي` | B001 building by joining parts; B002 composed constitution; B003 Sacred House/Makkah; B004 leather shelter; B005 bow stuck to string; B006 entering marriage; B007 filiation/descent; B008 small branching derivatives; B009 supports/ribs; B010 food building flesh | B001/B002/B009 -> CAND-02; B007/B008 -> LOCAL derivation/lineage; B003-B006/B010 TERMINATED |
| 91:6 `ٱلْأَرْضِ` | `ء ر ض` | B001 lower realm opposite sky; B002 soft fertile earth; B003 fit for good; B004 stranger; B005 large rug; B006 clinging to earth; B007 exposing oneself; B008 tremor; B009 cold; B010 woodworm; B011 corrupt sore; B012 deranged | B001/B002 -> CAND-02; B006/B008/B010/B011 -> LOCAL degradation/grounding echoes; others TERMINATED |
| 91:6 `طَحَىٰهَا` | `ط ح و` | B001 spreading/extension; B002 extended going; B003 circling vultures; B004 pushing among people; B005 abundance/bulk; B006 lying flat/sticking to earth; B008 height | B001/B002 -> CAND-02; B004 -> CAND-05 social shove; B006 -> LOCAL flattening; B003/B005/B008 TERMINATED |
| 91:7 `نَفْسٍ` | `ن ف س` | B001 breath from inside; B002 relief from distress; B003 evil eye; B004 blood as life; B005 childbirth; B006 drinking breath; B007 small tanning amount; B008 water sustaining life; B009 dawn opening like breath; B010 precious competed-for object; B011 life/soul; B012 self/essence; B013 inner reason/intention; B014 character/force; B015 spacious interval; B016 gambling arrow | B001/B011/B012/B013/B014 -> CAND-02 and CAND-03; B002/B008/B009 -> local relief/water/dawn corroborators; B010/B016 -> weak rivalry/gambling rival; B003-B007/B015 mostly TERMINATED |
| 91:7 `سَوَّىٰهَا` | `س و ي` | B001 equality/balance; B002 inner straightness/completion; B003 rising/settling; B004 turning toward; B005 maturity; B006 middle/justice; B007 otherness; B008 aiming toward a person/direction; B009 smooth wide ground; B010 pack-saddle surface; B012 full moon night; B013 head-equivalent measure | B001/B002/B006 -> CAND-02; B004/B008 -> CAND-03; B009 -> CAND-06 as leveling echo; others LOCAL/TERMINATED |
| 91:8 `أَلْهَمَهَا` | `ل ه م` | B001 swallowing/engulfing; B003 enemy devouring land; B004 bulk/abundance/generosity; B005 calamity that devours | B001 -> CAND-03 as inward instillation constrained by Form IV and object attachment; B003/B005 -> local devouring-rival for corruption; B004 LOCAL |
| 91:8 `فُجُورَهَا` | `ف ج ر` | B001 broad splitting/forthburst; B002 dawn bursting from night; B003 sudden abundant rush; B004 deviation from truth/breaching cover; B005 generous outpouring; B006 sacred-violation events | B001/B004 -> CAND-03; B002 -> CAND-01/CAND-03 dawn reactivation; B003/B006 -> CAND-05 transgression; B005 TERMINATED |
| 91:8 `تَقْوَىٰهَا` | `و ق ي` | B001 averting harm by shield; B002 placing self in protection; B003 animal guarding sore hoof; B004 weight-unit; B005 bird name | B001/B002 -> CAND-03; B003 LOCAL embodied caution; B004/B005 TERMINATED |
| 91:9 `أَفْلَحَ` | `ف ل ح` | B001 splitting/cutting; B002 cleft lip; B003 farmer who splits earth; B004 hireling like farmer; B005 success/survival; B006 suhur called falah; B007 sales trick | B003/B005 -> CAND-04; B001 -> local cultivation/cutting fork; B007 -> weak deception rival; others TERMINATED |
| 91:9 `زَكَّىٰهَا` | `ز ك و` | B001 growth/increase; B002 purity/rightness; B004 suitability; B005 pair/evenness | B001/B002 -> CAND-04; B004 -> local fit; B005 -> pair echo with فجور/تقوى; none omitted |
| 91:10 `خَابَ` | `خ ي ب` | B001 missed aim/deprivation; B002 fire-drill that does not spark; B003 valley refuting falsehood | B001 -> CAND-04; B002 -> local failed ignition; B003 weak truth-test echo |
| 91:10 `دَسَّىٰهَا` | `د س و` | B001 hidden insertion/burying; B003 seduction/corruption | B001/B003 -> CAND-04 |
| 91:11 `كَذَّبَتْ` | `ك ذ ب` | B001 opposite truth; B002 calling something false; B003 `كذب عليك` = adhere to it; B004 charge true/false; B005 no delay; B006 milk failing to persist; B007 wild animal stopping after running; B008 lying self; B009 garment deceiving by condition | B001/B002 -> CAND-05; B008 -> CAND-03 as inner rival; B006/B007 local failure of flow/motion; others TERMINATED |
| 91:11 `طَغْوَىٰهَا` | `ط غ ي` | B001 exceeding limit in rebellion; B002 water rising with sweeping force; B003 taghut source of misguidance; B005 smooth rock | B001/B002 -> CAND-05; B003 -> local corrupt leadership; B005 TERMINATED |
| 91:12 `ٱنۢبَعَثَ` | `ب ع ث` | B001 rousing the still; B002 sending/directing; B004 rush of a group in good or evil | B001/B004 -> CAND-05; B002 -> local anti-messenger mirror |
| 91:12 `أَشْقَىٰهَا` | `ش ق و` | B002 hardship/misery; B003 contest in hardship; B004 climber/long mountain-side | B002 -> CAND-05; B003/B004 local ascent/hardness echoes |
| 91:13 `قَالَ` | `ق و ل` | B001 uttered speech; B002 tongue; B003 abundant talk; B004 authoritative speaker; B005 saying what was not; B006 inward self-talk; B007 circulating report; B008 rare implement; B009 negotiation; B010 judging on another; B011 saying as supposition; B012 inner unspoken saying; B013 doctrine; B014 thing's indication; B015 true care; B016 definition | B001/B004/B014/B015/B016 -> CAND-05; B005/B011/B012 -> rival false-speech fork; others LOCAL/TERMINATED |
| 91:13 `رَسُولُ` | `ر س ل` | B001 sending/being sent; B002 messenger/message; B003 smooth/easy movement; B004 gentleness; B005 sequence/cut; B006 flowing milk; B007 familiarity; B008 correspondence; B009 specific woman; B010 generous ease; B011 special names | B001/B002 -> CAND-05; B003/B004/B005 -> local manner/sequence; B006 water/lactation echo; others TERMINATED |
| 91:13 `ٱللَّهِ` in `رَسُولُ ٱللَّهِ` | `ء ل ه` | B001 worship/made divine; B002 name of God in oath/call | B001/B002 -> CAND-05 as divine authorization; constrained by idafa |
| 91:13 `نَاقَةَ` | `ن و ق` | B001 height; B002 she-camel/form; B003 camel becoming she-camel in proverb; B004 taming/training/management; B005 careful refinement; B006 selection | B002 -> CAND-05; B004/B006 -> local stewardship expectation; B001/B003/B005 weak/local |
| 91:13 `ٱللَّهِ` in `نَاقَةَ ٱللَّهِ` | `ء ل ه` | B001 worship/made divine; B002 name of God in oath/call | B001/B002 -> CAND-05 as protected possession; constrained by idafa |
| 91:13 `سُقْيَٰهَا` | `س ق ي` | B001 watering the drinker; B002 appointing/giving watering; B003 share/channel of water; B005 dropsy; B006 prayer for rain; B007 heavy-rain cloud; B008 papyrus always watered; B009 dye soaking cloth; B010 giving the heart bitterness | B001/B002/B003 -> CAND-05; B006/B007 -> local rain ecology; B010 weak punitive inward fork; others TERMINATED |
| 91:14 `فَكَذَّبُوهُ` | `ك ذ ب` | B001-B009 as above | B001/B002 -> CAND-05 as repeated denial; B005 no-delay dimension locally supports immediate sequence; others as above |
| 91:14 `فَعَقَرُوهَا` | `ع ق ر` | B001 wound/defeat; B002 hamstringing animal legs; B003 back injury/motion prevention; B004 sterility; B005 last egg/no successor; B006 compensation for sex; B007 date-palm/bird cutting; B008 bodily/knowledge disabling; B009 raised voice; B010 curse formula; B011 rivalry/abuse; B012 clinging wine; B013 root/origin; B014 gap between two things; B015 palace/refuge; B016 property; B017 barren sand; B018 palace-like cloud; B019 red garment; B020 scorpion | B001/B002/B003 -> CAND-05; B004/B005/B017 -> local barrenness/termination; B013 -> root-cutting echo; others TERMINATED |
| 91:14 `دَمْدَمَ` | `د م د م` | B001 exterminating crushing/covering | B001 -> CAND-06 |
| 91:14 `رَبُّهُم` | `ر ب ب` | B001 lordship/ownership/mastery; B002 repair/nurture/completion; B003 rabbinic knowledge; B004 many groups; B005 step-child; B006 thickened curd; B007 abiding; B008 cloud; B009 fresh animal; B010 arrow bundle; B011 covenant; B012 plant; B013 abundant water; B014 herd; B015 `rubba`; B016 need/knot/blessing; B017 ship pilot | B001/B002 -> CAND-06; B011 -> local covenant breach; B013/B014 water/herd echo with CAND-05; others TERMINATED |
| 91:14 `ذَنۢبِهِم` | `ذ ن ب` | B001 sin/guilt; B002 tail/end; B003 followers; B004 water-channel tails; B005 ripening-end of dates; B006 share/portion; B007 full bucket; B008 ladle; B009 plant | B001 -> CAND-06; B002/B006/B007 -> local end/share/water echo; others TERMINATED |
| 91:14 `فَسَوَّىٰهَا` | `س و ي` | B001-B013 as above | B001/B002/B006/B009 -> CAND-06; B007 otherness as constraint; other branches LOCAL/TERMINATED |
| 91:15 `يَخَافُ` | `خ و ف` | B001 fear of expected harm; B002 making another afraid; B003 mutual fear; B004 taking/reducing from thing; B005 visible fear; B006 honey/waterskin implement | B001 -> CAND-06; B002/B003 as rival agent reading defeated; B004 local diminution echo; B005/B006 TERMINATED |
| 91:15 `عُقْبَٰهَا` | `ع ق ب` | B001 white sinew; B002 heel/trace; B003 turning back on heel; B004 offspring; B005 succession; B006 end/outcome; B007 punishment after sin; B008 review/follow-up; B009 return repeatedly; B010 replacement/guarantee; B011 remainder/effect; B012 difficult ascent; B013 eagle/banner; B014 Jacob; B015 dry plant | B006/B007/B011 -> CAND-06; B002/B005/B008/B009 -> sequence/trace corroboration; others TERMINATED |

## Constructional, Morphosyntactic, And Temporal Seeds

| Seed | Initial image | Outcome |
| --- | --- | --- |
| Repeated oath `وَ` plus genitive complements, 91:1-7 | Consecutive witnesses are laid down before the proposition about the soul | CAND-07 |
| `إِذَا` clauses in 91:2-4 | Time-conditioned visibility operations: follows, discloses, covers | CAND-01 |
| `وَمَا` clauses in 91:5-7 | Object plus maker/action: sky-built, earth-spread, soul-proportioned | CAND-02 |
| Repeated feminine suffix `هَا` from 91:1-10 | Earlier visible object and later soul are repeatedly reactivated as operated-upon fields | CAND-01, CAND-02, CAND-03, CAND-04 |
| Paired contents `فُجُورَهَا وَتَقْوَىٰهَا` | A dual inner field is supplied after the soul is proportioned | CAND-03 |
| Antithetical `قَدْ أَفْلَحَ` / `وَقَدْ خَابَ` | Two outcomes test the inner field | CAND-04 |
| `بِطَغْوَىٰهَا` and `بِذَنۢبِهِم` | Cause/manner attached by `بـ` frames rebellion and punishment | CAND-05, CAND-06 |
| Historical temporal pivot `إِذِ ٱنۢبَعَثَ` | A past case is introduced as enactment of the earlier moral model | CAND-05 |
| Quoted complement `نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا` | Warning content is not merely speech; it presents protected life plus its water-right | CAND-05 |
| Rapid `فـ` sequence in 91:13-14 | Speech -> denial -> hamstringing -> crushing -> leveling | CAND-05, CAND-06 |
| Closure `وَلَا يَخَافُ عُقْبَٰهَا` | Aftermath has no counter-threat to the executing Lord | CAND-06 |

## Candidate Synthesis Units

### CAND-01 - Visibility Alternation Around A Reappearing Feminine Object

- `candidate_id`: S91-ST1-CAND-01
- `ayah_range`: 91:1-4, with reactivation at 91:8-10
- `seed_type`: lexical + temporal/constructional
- `seed`: `ٱلشَّمْسِ` root `ش م س` B001, restarted from first rooted word
- `generating_set`: `(E: ش م س B001 sun/brightness)`, `(E: ض ح و B001 extended forenoon)`, `(E: ض ح و B002 exposure to sun)`, `(E: ض ح و B005 brightness)`, `(E: ق م ر B001 moonlight)`, `(E: ت ل و B001 following)`, `(E: ن ه ر B002 daylight opening)`, `(E: ن ه ر B003 opening/widening)`, `(E: ج ل و B001 disclosure)`, `(E: ج ل و B002 polishing)`, `(E: ج ل و B007 clear day)`, `(E: ل ي ل B001 night/darkness)`, `(E: غ ش و B001 covering)`, `(E: غ ش و B002 encompassing cover)`, `(E: 91:2-4 إِذَا temporal clauses)`, `(E: 91:2-4 suffix هَا object)`
- `selected_branches`: `ش م س B001`; `ض ح و B001/B002/B005`; `ق م ر B001`; `ت ل و B001`; `ن ه ر B002/B003`; `ج ل و B001/B002/B007`; `ل ي ل B001`; `غ ش و B001/B002`
- `constructed_model`: The opening does not merely name celestial objects. It creates a temporal exposure machine: brightness extends, a following body tracks the first light, day discloses it, and night covers it. The repeated `هَا` makes each operation reactivate a prior feminine object under changing visibility conditions.
- `freeze_point`: After 91:4, before sky/earth/soul are introduced.
- `predictions_at_freeze`: Expect later operated-upon fields; expect disclosure/concealment to recur in non-cosmic form; expect sequence to matter more than static theme; expect a moral or interior analogue to exposure and covering.
- `unused_features_tested`: 91:5-7 `وَمَا` creation clauses; 91:7 soul; 91:8 inner dual content; 91:9-10 purification vs burying; 91:11-14 denial and destructive concealment.
- `corroborators`: `(C: ن ف س B011/B012 soul/self as later operated field)`, `(C: ف ج ر B002 dawn bursting from night, reactivating light-from-dark)`, `(C: ف ج ر B004 breach of covering)`, `(C: و ق ي B001/B002 protective covering but positive)`, `(C: د س و B001 hiding/burying as moral night analogue)`, `(C: attachment rows 91:2-4 subject/object under إِذَا)`, `(C: sequence from cosmic visibility to inner visibility)`
- `constraints`: `(K: قمر B007 gambling/deception has no direct syntactic support in 91:2)`, `(K: ج ل و B003 bridal display is too socially specific)`, `(K: غ ش و B004 intercourse is blocked by subject night + object suffix)`, `(K: the first هَا most locally refers to sun/brightness, not yet to soul)`
- `temporal_reactivation_notes`: The hearer first gets a visible cycle. At 91:7-10, the cycle is replayed as soul -> inspiration -> purification/disclosure or burial/concealment.
- `rival_models`: A weak deception-light model from `ق م ر B007` + `ك ذ ب`; it fails to explain the ordered `إِذَا` visibility clauses.
- `grade`: strong
- `grade_rationale`: High specificity across lexical branch, temporal particles, object suffixes, and later concealment/purification contrast. It does not depend on translations or generic light symbolism.
- `source_queries_or_rows_used`: S91 qac_root rows for `ش م س`, `ض ح و`, `ق م ر`, `ت ل و`, `ن ه ر`, `ج ل و`, `ل ي ل`, `غ ش و`; accepted v4 branch rows listed above; attachment rows 91:1-4.

### CAND-02 - Built, Spread, And Proportioned Fields

- `candidate_id`: S91-ST1-CAND-02
- `ayah_range`: 91:5-8, with closure echo at 91:14
- `seed_type`: lexical + constructional
- `seed`: `ٱلسَّمَآءِ وَمَا بَنَىٰهَا`, especially `ب ن ي B001`
- `generating_set`: `(E: س م و B001 elevation)`, `(E: س م و B004 sky/what shades from above)`, `(E: ب ن ي B001 building by joining parts)`, `(E: ب ن ي B002 composed constitution)`, `(E: ب ن ي B009 supports/ribs)`, `(E: ء ر ض B001 lower realm opposite sky)`, `(E: ء ر ض B002 fertile earth)`, `(E: ط ح و B001 spreading/extending)`, `(E: ط ح و B002 extended going)`, `(E: ن ف س B011 living soul)`, `(E: ن ف س B012 self/essence)`, `(E: س و ي 91:7 B001 equality/balance)`, `(E: س و ي 91:7 B002 completion/straightness)`, `(E: س و ي 91:7 B006 middle/justice)`, `(E: 91:5-7 وَمَا construction)`
- `selected_branches`: `س م و B001/B004`; `ب ن ي B001/B002/B009`; `ء ر ض B001/B002`; `ط ح و B001/B002`; `ن ف س B011/B012`; `س و ي B001/B002/B006`
- `constructed_model`: The sequence passes from upper field, to lower field, to inner field. Each field is not just named but operated on: built, spread, proportioned. The soul enters as a constructed field analogous to sky and earth but capable of receiving inner orientation.
- `freeze_point`: After 91:7, before `فَأَلْهَمَهَا`.
- `predictions_at_freeze`: Expect an operation that fills or directs the proportioned soul; expect balance to become morally differentiated; expect later leveling/re-equalizing if balance is violated.
- `unused_features_tested`: 91:8 inspiration of paired content; 91:9-10 two outcomes; 91:14 second `سَوَّىٰهَا`; 91:15 aftermath.
- `corroborators`: `(C: ل ه م B001 inward swallowing/receiving, constrained by Form IV as caused reception)`, `(C: ف ج ر B004 breach)`, `(C: و ق ي B001/B002 protection)`, `(C: ز ك و B001/B002 growth/purity)`, `(C: د س و B001/B003 hidden corruption)`, `(C: س و ي 91:14 B001/B006 leveling after punishment)`, `(C: repeated object suffix هَا across 91:5-10)`
- `constraints`: `(K: ب ن ي B003 Sacred House/Makkah is unsupported by local syntax)`, `(K: ب ن ي B006 marriage-entry is blocked by sky as object)`, `(K: ط ح و B003 vulture-circling is not recruited by 91:6 object earth)`, `(K: soul is not equated with sky/earth; it is the third operated field)`
- `temporal_reactivation_notes`: 91:5-7 intensifies from environment to person. Later `فَسَوَّىٰهَا` at 91:14 reactivates `سَوَّىٰهَا` but transfers proportioning into punitive leveling.
- `rival_models`: A purely cosmological oath model; it explains 91:1-7 but leaves 91:8-15 as a thematic add-on rather than reactivation.
- `grade`: strong
- `grade_rationale`: Strong branch fit, exact constructional parallelism, and later same-root reactivation.
- `source_queries_or_rows_used`: S91 qac_root rows and v4 branches for `س م و`, `ب ن ي`, `ء ر ض`, `ط ح و`, `ن ف س`, `س و ي`; attachment rows 91:5-7 and 91:14.

### CAND-03 - Interior Instillation Of Breach And Guard

- `candidate_id`: S91-ST1-CAND-03
- `ayah_range`: 91:7-10
- `seed_type`: lexical + morphosyntactic
- `seed`: `نَفْسٍ` and `فَأَلْهَمَهَا`
- `generating_set`: `(E: ن ف س B001 breath from inside)`, `(E: ن ف س B011 life/soul)`, `(E: ن ف س B012 self/essence)`, `(E: ن ف س B013 inner reason/intention)`, `(E: ن ف س B014 character/force)`, `(E: س و ي B001/B002/B006 proportioned balance)`, `(E: ل ه م B001 swallowing/receiving inward, as seed image only)`, `(E: ف ج ر B001 broad splitting)`, `(E: ف ج ر B004 breaching cover/deviation)`, `(E: و ق ي B001 shield from harm)`, `(E: و ق ي B002 making the self into protection)`, `(E: attachment 91:8 first object suffix + paired content objects)`
- `selected_branches`: `ن ف س B001/B011/B012/B013/B014`; `س و ي B001/B002/B006`; `ل ه م B001`; `ف ج ر B001/B004`; `و ق ي B001/B002`
- `constructed_model`: A balanced inner field receives a forced inward orientation. The two contents are not simple abstract labels: one opens a breach and violates covering, the other sets a guard or buffer against harm. The `هَا` suffixes keep the soul as the locus and possessor of both tendencies.
- `freeze_point`: After 91:8, before success/failure outcomes.
- `predictions_at_freeze`: Expect two opposed treatments of the same inner object; expect one to increase/cleanse and one to hide/corrupt; expect the moral field to be testable in action.
- `unused_features_tested`: `أَفْلَحَ`, `زَكَّىٰهَا`, `خَابَ`, `دَسَّىٰهَا`, Thamud denial, hamstringing, punishment.
- `corroborators`: `(C: ز ك و B001 growth and B002 purity)`, `(C: د س و B001 hiding/burying and B003 corruption)`, `(C: خ ي ب B001 deprivation of sought result)`, `(C: ك ذ ب B008 lying self as later negative inner analogue)`, `(C: sequence 91:7 proportion -> 91:8 inspiration -> 91:9-10 outcomes)`
- `constraints`: `(K: ل ه م B001 does not itself mean spiritual inspiration; the inward-intake image is constrained by the actual Form IV verb and object/content attachments)`, `(K: ف ج ر B005 generosity is not passage-local)`, `(K: و ق ي B004 weight unit and B005 bird name terminate)`
- `temporal_reactivation_notes`: The first exposure/covering model becomes interior. Disclosure and concealment are now owned by the soul.
- `rival_models`: An ingestion-only model from `ل ه م` is unlikely because it cannot explain the paired moral content without QAC morphology and attachment constraints.
- `grade`: medium-strong
- `grade_rationale`: Excellent structural fit, but `ل ه م` branch support is indirect in the available v4 export and must be constrained by morphology and syntax.
- `source_queries_or_rows_used`: S91 qac_root rows and v4 branches for `ن ف س`, `س و ي`, `ل ه م`, `ف ج ر`, `و ق ي`, `ز ك و`, `د س و`, `خ ي ب`; attachment rows 91:7-10.

### CAND-04 - Cultivation, Growth, And Burial Of The Soul

- `candidate_id`: S91-ST1-CAND-04
- `ayah_range`: 91:8-10, with 91:6 earth reactivation
- `seed_type`: lexical
- `seed`: `أَفْلَحَ` root `ف ل ح`, including B003 farmer and B005 success
- `generating_set`: `(E: ف ل ح B003 farmer who splits earth)`, `(E: ف ل ح B005 success/survival)`, `(E: ز ك و B001 growth/increase)`, `(E: ز ك و B002 purity/rightness)`, `(E: خ ي ب B001 missed aim/deprivation)`, `(E: د س و B001 hidden insertion/burying)`, `(E: د س و B003 seduction/corruption)`, `(E: ء ر ض B002 fertile earth as earlier unused reactivation)`, `(E: ط ح و B001 spread earth as field)`
- `selected_branches`: `ف ل ح B003/B005`; `ز ك و B001/B002`; `خ ي ب B001`; `د س و B001/B003`; earlier `ء ر ض B002`; `ط ح و B001`
- `constructed_model`: The soul becomes like a prepared field. Success is not only an outcome but a cultivated split/opening of earth that permits growth and purification. Failure is the reverse: the same object is pushed down, hidden, and corrupted.
- `freeze_point`: After 91:10.
- `predictions_at_freeze`: Expect a narrative example where transgression suppresses a protected life/resource and where the consequence is not growth but leveling/destruction.
- `unused_features_tested`: Thamud's transgression, camel, watering-right, hamstringing, crushing, leveling, aftermath.
- `corroborators`: `(C: ن و ق B002 living she-camel as test-object)`, `(C: س ق ي B001/B002/B003 watering ecology)`, `(C: ع ق ر B002 cutting animal legs, anti-cultivation/destruction of life)`, `(C: د م د م B001 extermination)`, `(C: ذ ن ب B001 guilt as causal complement)`, `(C: sequence 91:9 positive then 91:10 negative before historical case)`
- `constraints`: `(K: ف ل ح B001 generic cutting alone would predict cutting, but 91:9 attaches success to purification, not violence)`, `(K: ف ل ح B007 sales trick has no role)`, `(K: ز ك و B005 pair is only a minor echo, not a model)`
- `temporal_reactivation_notes`: Earlier earth-spreading returns as moral agriculture. Later camel-water material makes the field/ecology image concrete, but after freeze.
- `rival_models`: A violent cutting model from `ف ل ح B001` + `ع ق ر`; it is defeated because `زَكَّىٰهَا` is the direct condition for success.
- `grade`: strong
- `grade_rationale`: Independent convergence from lexical agriculture/growth, syntax of the same soul object, and later ecological violation.
- `source_queries_or_rows_used`: S91 qac_root rows and v4 branches for `ف ل ح`, `ز ك و`, `خ ي ب`, `د س و`, `ء ر ض`, `ط ح و`, `ن و ق`, `س ق ي`, `ع ق ر`; attachment rows 91:8-10 and 91:13-14.

### CAND-05 - Transgression Against A Protected Life-Water Sign

- `candidate_id`: S91-ST1-CAND-05
- `ayah_range`: 91:11-14
- `seed_type`: lexical + constructional
- `seed`: `كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَا`
- `generating_set`: `(E: ك ذ ب B001 opposite truth)`, `(E: ك ذ ب B002 declaring false)`, `(E: ط غ ي B001 exceeding boundary in rebellion)`, `(E: ط غ ي B002 water rising with sweeping force)`, `(E: ب ع ث B001 rousing stillness)`, `(E: ب ع ث B004 rushing forth)`, `(E: ش ق و B002 hardship/misery)`, `(E: ق و ل B001 uttered speech)`, `(E: ق و ل B004 authoritative speaker)`, `(E: ر س ل B001 sending)`, `(E: ر س ل B002 messenger/message)`, `(E: ء ل ه B001/B002 divine idafa authorization)`, `(E: ن و ق B002 she-camel)`, `(E: ن و ق B004 taming/stewardship as expected role)`, `(E: س ق ي B001 watering)`, `(E: س ق ي B002 appointed watering)`, `(E: س ق ي B003 water-share/channel)`, `(E: ع ق ر B001 wounding/defeat)`, `(E: ع ق ر B002 hamstringing animal legs)`, `(E: ع ق ر B003 disabling motion)`
- `selected_branches`: `ك ذ ب B001/B002`; `ط غ ي B001/B002`; `ب ع ث B001/B004`; `ش ق و B002`; `ق و ل B001/B004`; `ر س ل B001/B002`; `ء ل ه B001/B002`; `ن و ق B002/B004`; `س ق ي B001/B002/B003`; `ع ق ر B001/B002/B003`
- `constructed_model`: The historical case is an enacted failure of the inner model. A community's over-boundary force rejects an authoritative message, a worst member is roused, and the protected she-camel plus her water-right become the concrete sign that must be guarded. They do the opposite: denial becomes bodily disabling.
- `freeze_point`: After `فَعَقَرُوهَا`, before `فَدَمْدَمَ`.
- `predictions_at_freeze`: Expect causal guilt, Lordly response, comprehensive punishment, and a leveling that answers the earlier violated proportion.
- `unused_features_tested`: `فَدَمْدَمَ`, `رَبُّهُم`, `بِذَنۢبِهِم`, `فَسَوَّىٰهَا`, `وَلَا يَخَافُ عُقْبَٰهَا`.
- `corroborators`: `(C: د م د م B001 exterminating crushing)`, `(C: ر ب ب B001 lordship/ownership)`, `(C: ر ب ب B002 correction/completion)`, `(C: ذ ن ب B001 sin/guilt)`, `(C: س و ي 91:14 B001/B006 leveling/justice)`, `(C: ع ق ب B006/B007/B011 consequence/punishment/remnant)`, `(C: attachment row quoted complement 91:13 keeps ناقة الله وسقياها as warning content)`, `(C: فـ rapid sequence speech -> denial -> hamstringing -> crushing)`
- `constraints`: `(K: ط غ ي B002 water-overflow supports force and water ecology but cannot replace B001 rebellion as contextual sense)`, `(K: ن و ق B001 height and B005 refinement are secondary)`, `(K: ق و ل B005 false saying is rival, not the messenger's speech)`, `(K: ء ل ه branches are constrained by idafa; no new seed from basmala was used)`
- `temporal_reactivation_notes`: The earlier soul's `فجور/تقوى` is replayed socially: transgression rejects protective warning, then violates a vulnerable life-water arrangement.
- `rival_models`: A pure flood model from `ط غ ي B002` + `س ق ي`; medium as secondary image, weak as primary because the actual act is denial and hamstringing.
- `grade`: strong
- `grade_rationale`: Dense local fit across lexical branches, idafa, quoted-complement structure, repeated denial, and the exact animal/water/punishment sequence.
- `source_queries_or_rows_used`: S91 qac_root rows and v4 branches for `ك ذ ب`, `ط غ ي`, `ب ع ث`, `ش ق و`, `ق و ل`, `ر س ل`, `ء ل ه`, `ن و ق`, `س ق ي`, `ع ق ر`, `د م د م`, `ر ب ب`, `ذ ن ب`, `س و ي`, `ع ق ب`; attachment rows 91:11-15.

### CAND-06 - Crushing Leveling And Unfeared Aftermath

- `candidate_id`: S91-ST1-CAND-06
- `ayah_range`: 91:14-15, reactivating 91:7
- `seed_type`: lexical + temporal/acoustic
- `seed`: `فَدَمْدَمَ`
- `generating_set`: `(E: د م د م B001 exterminating crushing/covering)`, `(E: ر ب ب B001 lordship/mastery)`, `(E: ر ب ب B002 correction/completion)`, `(E: ذ ن ب B001 sin/guilt)`, `(E: س و ي 91:14 B001 equalizing)`, `(E: س و ي 91:14 B002 completion/straightness)`, `(E: س و ي 91:14 B006 just middle)`, `(E: س و ي 91:14 B009 smooth wide level ground)`, `(E: خ و ف B001 fear of expected harm)`, `(E: ع ق ب B006 final outcome)`, `(E: ع ق ب B007 punishment after sin)`, `(E: ع ق ب B011 remnant/effect)`
- `selected_branches`: `د م د م B001`; `ر ب ب B001/B002`; `ذ ن ب B001`; `س و ي B001/B002/B006/B009`; `خ و ف B001`; `ع ق ب B006/B007/B011`
- `constructed_model`: A Lordly corrective force comes down on the guilty group and flattens the violated field. The same root that proportioned the soul now describes punitive leveling. The final line removes any expected retaliatory aftermath.
- `freeze_point`: After `فَسَوَّىٰهَا`, before 91:15.
- `predictions_at_freeze`: Expect closure to address consequence, remainder, or fear of what follows.
- `unused_features_tested`: `وَلَا يَخَافُ عُقْبَٰهَا`.
- `corroborators`: `(C: ع ق ب B006/B007/B011 directly supplies end/punishment/remnant)`, `(C: خ و ف B001 supplies expected harm negated)`, `(C: attachment row 91:15 direct object عُقْبَٰهَا)`, `(C: س و ي 91:7 reactivated as prior proportioning now turned into leveling)`
- `constraints`: `(K: خ و ف B002 making others fear is not the grammar; the verb is negated with explicit object عُقْبَاهَا)`, `(K: ع ق ب B004 offspring and B013 eagle/banner terminate)`, `(K: ر ب ب B006 curd and B010 arrow bundle are not passage-local)`
- `temporal_reactivation_notes`: The surah closes by stopping the temporal chain: after consequence, no feared consequence remains for the actor of judgment.
- `rival_models`: A revenge-cycle model from `ع ق ب B009` repeated return is explicitly constrained by `لَا يَخَافُ`.
- `grade`: strong
- `grade_rationale`: Exact closure fit and strong reactivation of `س و ي` from 91:7 to 91:14.
- `source_queries_or_rows_used`: S91 qac_root rows and v4 branches for `د م د م`, `ر ب ب`, `ذ ن ب`, `س و ي`, `خ و ف`, `ع ق ب`; attachment rows 91:14-15.

### CAND-07 - From Oath Witnesses To Moral Case Trial

- `candidate_id`: S91-ST1-CAND-07
- `ayah_range`: 91:1-15
- `seed_type`: verified composite construction
- `seed`: repeated oath series and temporal pivots
- `generating_set`: `(E: repeated oath wāw attachments 91:1-7)`, `(E: temporal إِذَا 91:2-4)`, `(E: وَمَا maker/action clauses 91:5-7)`, `(E: paired inspired content 91:8)`, `(E: antithetical outcome clauses 91:9-10)`, `(E: historical إِذِ 91:12)`, `(E: quoted complement 91:13)`, `(E: rapid فـ chain 91:13-14)`, `(E: closure 91:15)`
- `selected_branches`: This is constructional, but it uses branch-supported packets CAND-01 through CAND-06.
- `constructed_model`: The surah first calibrates the listener with alternating visible phenomena, then transfers the same operation language to made fields, then to the soul, then to a community case. The closure shows the consequence of refusing the guarded proportion.
- `freeze_point`: After 91:10, before Thamud is named.
- `predictions_at_freeze`: Expect a concrete narrative that tests breach/protection, concealment/purification, and proportion/leveling.
- `unused_features_tested`: 91:11-15 as historical case.
- `corroborators`: `(C: ك ذ ب repeated 91:11 and 91:14)`, `(C: ط غ ي B001 boundary excess)`, `(C: ن و ق + س ق ي protected life-water sign)`, `(C: ع ق ر disabling sign)`, `(C: د م د م + س و ي + ع ق ب consequence closure)`
- `constraints`: `(K: This composite is not a translation; it is a temporal reactivation model)`, `(K: It depends on the lower candidates remaining branch-specific; if those are generalized, the composite weakens)`
- `temporal_reactivation_notes`: The order is essential. Shuffling the same roots would lose the progression from exposure, to making, to inspiration, to outcome, to historical enactment, to closure.
- `rival_models`: A generic "oaths then moral lesson" model. It is true at a high level but less explanatory of branch-specific reactivation.
- `grade`: medium-strong
- `grade_rationale`: Strong order fit, but composite candidates are downstream and should not erase seed-level provenance.
- `source_queries_or_rows_used`: All S91 root rows, all accepted branch rows for S91 roots, and S91 attachment rows.

## Failed Or Weak Rival Image-Branches Preserved

- Lunar deception: `ق م ر B007` plus `ك ذ ب B001/B002` can suggest deceptive winning or false appearance, but the local moon clause is syntactically following the sun, not gambling. Grade: weak.
- Flood-only rebellion: `ط غ ي B002` plus `س ق ي B001/B003` can form a water-overflow scene. It corroborates force and water ecology but fails as primary because 91:11 uses denial/transgression and 91:14 uses hamstringing. Grade: medium as secondary, weak as primary.
- Pure violence/cutting: `ف ل ح B001` plus `ع ق ر B001/B002` overpredicts cutting. It is constrained by `زَكَّىٰهَا` and the positive outcome in 91:9. Grade: unlikely as governing model.
- Bridal/exposure model: `ج ل و B003` and several social branches can mimic display, but no bride/marriage roles are supplied in 91:1-4. Grade: unlikely.
- Divine-name-only model: `ء ل ه B002` supports idafa and divine authorization, but by itself does not generate the historical mechanism. Grade: local.
- Pasture/camel ecology model from `ض ح و B003`, `ق م ر B008/B010`, `ن و ق`, `س ق ي`, `ء ر ض B002`: useful local ecology, but it enters late as corroboration rather than generating the full surah. Grade: medium local.

## Image Packet Catalog

### IMAGE-01

Starting seed: `ش م س B001`  
Complete image: A visible object is successively brightened, followed, disclosed, and covered.  
Passage-order assembly: 91:1 sun/forenoon -> 91:2 moon follows -> 91:3 day discloses -> 91:4 night covers.  
Participants and roles: sun/brightness as object; moon/day/night as successive operators.  
Operation / mechanism: exposure alternates with covering.  
Direction / force / medium: light, visibility, temporal succession.  
Temporal development: `إِذَا` clauses make the state conditional and unfolding.  
Outcome / closure: reactivated as moral disclosure/concealment at 91:8-10.  
Exact branch constituents: `ش م س B001`; `ض ح و B001/B002/B005`; `ق م ر B001`; `ت ل و B001`; `ن ه ر B002/B003`; `ج ل و B001/B002/B007`; `ل ي ل B001`; `غ ش و B001/B002`.  
Unfilled roles, if any: none for local image.  
Status: COMPLETE.

### IMAGE-02

Starting seed: `ب ن ي B001`  
Complete image: Sky, earth, and soul are successively treated as made fields.  
Passage-order assembly: sky built -> earth spread -> soul proportioned -> inner contents supplied.  
Participants and roles: maker/action, field/object, proportioned soul.  
Operation / mechanism: composition, extension, balancing.  
Direction / force / medium: upper/lower/interior.  
Temporal development: `وَمَا` clauses repeat and narrow toward the soul.  
Outcome / closure: punitive `سَوَّىٰهَا` reactivates proportion as leveling.  
Exact branch constituents: `س م و B001/B004`; `ب ن ي B001/B002/B009`; `ء ر ض B001/B002`; `ط ح و B001/B002`; `ن ف س B011/B012`; `س و ي B001/B002/B006`.  
Unfilled roles, if any: maker left grammatically by `مَا` and not independently expanded.  
Status: COMPLETE.

### IMAGE-03

Starting seed: `ن ف س B011/B012`  
Complete image: A proportioned interior receives two contrary orientations, breach and guard.  
Passage-order assembly: soul proportioned -> inspired breach/guard -> purification or burial.  
Participants and roles: soul as locus; فجور as breach; تقوى as protective guard; purifier/burier as later agent.  
Operation / mechanism: inward placement and opposed treatment.  
Direction / force / medium: inner moral field.  
Temporal development: 91:8 opens the duality; 91:9-10 resolves it.  
Outcome / closure: historical case performs the negative branch.  
Exact branch constituents: `ن ف س B001/B011/B012/B013/B014`; `س و ي B001/B002/B006`; `ل ه م B001`; `ف ج ر B001/B004`; `و ق ي B001/B002`; `ز ك و B001/B002`; `د س و B001/B003`.  
Unfilled roles, if any: the exact mechanics of `ألهم` require morphology beyond branch image and are therefore constrained.  
Status: COMPLETE with lexical constraint.

### IMAGE-04

Starting seed: `ف ل ح B003/B005`  
Complete image: The soul is cultivated into growth or buried into loss.  
Passage-order assembly: success -> purification/growth; failure -> hidden corruption.  
Participants and roles: cultivator, soul-field, growth/purity, burial/corruption.  
Operation / mechanism: open/cultivate versus insert/conceal.  
Direction / force / medium: earth-field reactivation from 91:6.  
Temporal development: antithetical couplet 91:9-10.  
Outcome / closure: Thamud case shows life-water ecology destroyed rather than cultivated.  
Exact branch constituents: `ف ل ح B003/B005`; `ز ك و B001/B002`; `خ ي ب B001`; `د س و B001/B003`; `ء ر ض B002`; `ط ح و B001`; later `ن و ق B002`; `س ق ي B001/B002/B003`; `ع ق ر B001/B002`.  
Unfilled roles, if any: none for the moral field image.  
Status: COMPLETE.

### IMAGE-05

Starting seed: `ك ذ ب B001/B002` at 91:11  
Complete image: Rebellious denial violates a protected life-water sign and is answered by crushing.  
Passage-order assembly: denial by transgression -> worst one rises -> messenger warns -> camel/watering right -> denial repeated -> hamstringing -> punishment.  
Participants and roles: Thamud, worst member, messenger, God, she-camel, watering-right, Lord.  
Operation / mechanism: warning rejected, protected sign disabled.  
Direction / force / medium: social rebellion, animal body, water allotment, punitive descent.  
Temporal development: `إِذِ` and rapid `فـ` chain.  
Outcome / closure: leveling and no feared aftermath.  
Exact branch constituents: `ك ذ ب B001/B002`; `ط غ ي B001/B002`; `ب ع ث B001/B004`; `ش ق و B002`; `ق و ل B001/B004`; `ر س ل B001/B002`; `ء ل ه B001/B002`; `ن و ق B002/B004`; `س ق ي B001/B002/B003`; `ع ق ر B001/B002/B003`; `د م د م B001`; `ر ب ب B001/B002`; `ذ ن ب B001`; `س و ي B001/B006`; `ع ق ب B006/B007/B011`.  
Unfilled roles, if any: none for the historical image.  
Status: COMPLETE.

### IMAGE-06

Starting seed: `د م د م B001`  
Complete image: A guilty group is crushed, leveled, and left with no threatening aftermath.  
Passage-order assembly: hamstringing -> crushing upon them -> causal guilt -> leveling -> no fear of consequence.  
Participants and roles: Lord as actor; guilty group as target; sin as cause; aftermath as negated threat.  
Operation / mechanism: comprehensive punitive leveling.  
Direction / force / medium: force downward/upon them, then closure after them.  
Temporal development: final two ayat terminate the causal chain.  
Outcome / closure: no feared `عقبى`.  
Exact branch constituents: `د م د م B001`; `ر ب ب B001/B002`; `ذ ن ب B001`; `س و ي B001/B002/B006/B009`; `خ و ف B001`; `ع ق ب B006/B007/B011`.  
Unfilled roles, if any: none.  
Status: COMPLETE.

## Final Exhaustiveness Check

- Distinct S91 roots from the local QAC export: 36.
- Accepted branch seeds initiated from local v4 branch export: 286 before occurrence-sensitive duplication.
- Occurrence-sensitive repeated roots checked separately: `ك ذ ب` at 91:11 and 91:14, `س و ي` at 91:7 and 91:14, `ء ل ه` twice in 91:13.
- Constructional seeds checked: oath sequence, `إِذَا`, `وَمَا`, feminine suffix recurrence, paired inspired contents, success/failure antithesis, `بـ` causal/manner complements, `إِذ`, quoted warning complement, rapid `فـ`, and final negated fear.
- Failed and weak seeds were not dropped; they are recorded in the ledger and weak-rival section.
