# Stage 1 Pass 2 - S107

Assigned passage: S107  
Sacred Arabic source: `resources/quran/surah_107.json`  
Prompt: `v1/prompts/stage1.md`

## Pass 1 Limitation Root Cause

Pass 1 stopped after in-context discovery and did not write an auditable seed-by-seed artifact. It also sampled the root dossiers enough to hold candidate models, rather than restarting each accepted branch of each rooted occurrence as its own seed. This produced the visible limitation: several findings were built from only the promising words and did not explicitly show that the other branches had been read, tested, and rejected or retained.

This pass restarts from the first rooted word and treats every eligible rooted occurrence and construction as a seed. The SQLite files named in the prompt are zero-byte placeholders in this checkout, so I used the copied local resource TSVs that contain the same bounded resource data: `resources/qac_root_ayah.tsv`, `resources/v4_branches.tsv`, and `resources/attachments.tsv`. No translation was used.

## Sacred Text

Opening context: `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`  
107:1 `أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ`  
107:2 `فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ`  
107:3 `وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ`  
107:4 `فَوَيْلٌۭ لِّلْمُصَلِّينَ`  
107:5 `ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ`  
107:6 `ٱلَّذِينَ هُمْ يُرَآءُونَ`  
107:7 `وَيَمْنَعُونَ ٱلْمَاعُونَ`

## Rooted Occurrences And Dossiers

QAC-rooted occurrence order:

1. 107:1:1 `أَرَءَيْتَ`, root `ر ء ي`, 13 accepted branches.
2. 107:1:3 `يُكَذِّبُ`, root `ك ذ ب`, Form II, 9 accepted branches.
3. 107:1:4 `بِٱلدِّينِ`, root `د ي ن`, 7 accepted branches.
4. 107:2:3 `يَدُعُّ`, root `د ع ع`, 8 accepted branches.
5. 107:2:4 `ٱلْيَتِيمَ`, root `ي ت م`, 5 accepted branches.
6. 107:3:2 `يَحُضُّ`, root `ح ض ض`, 4 accepted branches.
7. 107:3:4 `طَعَامِ`, root `ط ع م`, 13 accepted branches.
8. 107:3:5 `ٱلْمِسْكِينِ`, root `س ك ن`, 9 accepted branches.
9. 107:4:2 `وَيْل`, root recovered from attachment/root dossier `و ي ل`, 2 accepted branches.
10. 107:4:3 `لِّلْمُصَلِّينَ`, QAC root `ص ل و`, 9 accepted branches. Attachment normalizes the same word as `ص ل ي`, whose dossier was also checked as structural corroboration.
11. 107:5:4 `صَلَاتِهِمْ`, root `ص ل و`, 9 accepted branches.
12. 107:5:5 `سَاهُونَ`, QAC root `س ه و`, 5 accepted branches. Attachment prints `س و ه`; no matching branch dossier was found for that spelling, so `س ه و` controls.
13. 107:6:3 `يُرَآءُونَ`, root `ر ء ي`, Form III, 13 accepted branches.
14. 107:7:1 `يَمْنَعُونَ`, root `م ن ع`, 7 accepted branches.
15. 107:7:2 `ٱلْمَاعُونَ`, QAC root `م ع ن`, 5 accepted branches. Attachment normalizes the object as `ع و ن`; that dossier was checked as closure corroboration, especially `ع و ن B001`.

All seed passes below use the full cross-root sweep over these dossiers unless explicitly marked as a supplemental normalization check.

Attachment controls used after freeze:

- 107:1 `ٱلَّذِى` direct object of `أَرَءَيْتَ`; `بِٱلدِّينِ` governed complement of `يُكَذِّبُ`.
- 107:2 `ٱلَّذِى` predicates `ذَٰلِكَ`; `ٱلْيَتِيمَ` direct object of `يَدُعُّ`.
- 107:3 `طَعَامِ` governed by `عَلَىٰ`; `ٱلْمِسْكِينِ` is idafa second term of `طَعَامِ`.
- 107:4 `لِّلْمُصَلِّينَ` is the governed/predicate phrase for `وَيْل`.
- 107:5 `صَلَاتِهِمْ` governed by `عَن`; `سَاهُونَ` predicates `هُمْ`.
- 107:6 `يُرَآءُونَ` predicates `هُمْ`.
- 107:7 `ٱلْمَاعُونَ` direct object of `يَمْنَعُونَ`.

## Exhaustive Seed Ledger

The ledger is deliberately compact. `Selected image` points to a detailed candidate packet below. `Local` means the seed generated a passage-local image but did not control the whole surah. `Dies` means the branch was read and found to have no specific passage-local complement after testing all other dossiers, morphology, attachments, sequence, and repetition.

### 107:1:1 `أَرَءَيْتَ` - `ر ء ي`

| Seed | branch image | result |
| --- | --- | --- |
| RAY1-B001 | رؤية العين والبصيرة | selected image CSU-01; seeing/recognition cue opens the audit. |
| RAY1-B002 | رأي القلب والتفكر | selected image CSU-01; inner judgment/consideration version. |
| RAY1-B003 | الرؤيا في المنام | dies; no sleep/dream frame, no later dream reactivation. |
| RAY1-B004 | تراء وتواجه | local; anticipates later mutual public visibility at `يُرَآءُونَ`, but weak before Form III arrives. |
| RAY1-B005 | رياء الناس | local/forward prediction; cannot generate at 107:1 without later 107:6, but becomes strong corroboration for CSU-09. |
| RAY1-B006 | مرأى ومنظر ومرآة | weak local; appearance/perceived form fits later show-prayer, but no mirror/instrument. |
| RAY1-B007 | ترية الحيض | dies; no menstruation/purity signs. |
| RAY1-B008 | رئي من الجن | dies; no jinn/kahānah frame. |
| RAY1-B009 | الرئة وما يصيبها | dies; no breath/lung injury roles. |
| RAY1-B010 | ظهور حمل الناقة أو الشاة | dies; no pregnancy/udder/animal disclosure. |
| RAY1-B011 | راية منصوبة | weak local; public signal idea fits ostentation but no banner/sign object. |
| RAY1-B012 | إراءة وإظهار | selected image CSU-09 as backward reactivation after `يُرَآءُونَ`; at first occurrence it only predicts disclosure. |
| RAY1-B013 | أرأيتك للتنبيه والاستخبار | selected image CSU-01; strongest exact opening-seed branch. |

### 107:1:3 `يُكَذِّبُ` - `ك ذ ب`

| Seed | branch image | result |
| --- | --- | --- |
| KDB-B001 | خلاف الصدق | local; negation of truth sets false orientation, selected inside CSU-01/CSU-02 as broad support. |
| KDB-B002 | نسبة الشيء أو صاحبه إلى الكذب | selected image CSU-02; exact Form II denial/rejection of `الدين`. |
| KDB-B003 | كذب عليك بمعنى الزم وعليك به | dies/constraint; the local form with `بِالدِّين` is rejection, not obligation. |
| KDB-B004 | صدق الحملة أو كذبها | weak fork; failed charge can analogize action that does not carry through, but no battle/charge roles. |
| KDB-B005 | ما كذب أن فعل أي ما لبث | dies; no immediacy construction. |
| KDB-B006 | كذب لبن الناقة إذا ذهب ولم يدم | weak terminated; non-durability could picture charity that does not continue, but no milk/sustenance syntax. |
| KDB-B007 | كذب الوحشي إذا جرى ثم وقف | dies; no animal flight/turning scene. |
| KDB-B008 | النفس الكذوب | weak local; inward false self can underlie hypocrisy, but no lexical complement beyond general falsity. |
| KDB-B009 | الكذابة ثوب يكذب بحاله | selected weak image CSU-10; deceptive appearance links to show-prayer, but it is remote and constrained. |

### 107:1:4 `بِٱلدِّينِ` - `د ي ن`

| Seed | branch image | result |
| --- | --- | --- |
| DYN-B001 | الطاعة والانقياد | selected image CSU-02/CSU-07; denial of obedience becomes visible as failure to enact prayer/social obligation. |
| DYN-B002 | الحساب والجزاء | selected image CSU-02; governing accountability frame. |
| DYN-B003 | الدين المالي | local; debt/dues branch predicts owed support and withheld ma`un; selected as secondary in CSU-03/CSU-08. |
| DYN-B004 | الإذلال والملك | weak constraint; the passage shows humiliating the orphan, but `بالدين` attachment is denial-object, not enslavement. |
| DYN-B005 | العادة والشأن | local; habitual pattern becomes behavior profile across ayat 2-7. |
| DYN-B006 | مدينة الطاعة | dies; no city/urban authority role. |
| DYN-B007 | التصديق والتفويض | selected as inversion in CSU-02; denial refuses ratification/trust. |

### 107:2:3 `يَدُعُّ` - `د ع ع`

| Seed | branch image | result |
| --- | --- | --- |
| DAع-B001 | الدَّعّ دفع شديد | selected image CSU-03; exact violent displacement of unsupported dependent. |
| DAع-B002 | الدعدعة تحريك لامتلاء | weak fork CSU-11; vessel/filling image is constrained because the direct object is orphan, not vessel. |
| DAع-B003 | الدعدعة نداء وزجر | local; harsh herding/zajr reinforces repulsion but no animal-herd frame. |
| DAع-B004 | دع دع للعاثر | rival inversion; instead of raising the stumbled, the passage pushes the orphan. Retained as constraint/counter-image. |
| DAع-B005 | الدعدعة عدو ملتف بطيء | dies; no twisted running. |
| DAع-B008 | الدعدع نبت مائي | dies; no plant/water-summer scene. |
| DAع-B009 | الدعاع عيال صغار | local corroborator for orphan/children vulnerability, but not exact verb sense. |
| DAع-B010 | الدعاع حبة برية | dies; no seed/grain famine object beyond remote food association. |

### 107:2:4 `ٱلْيَتِيمَ` - `ي ت م`

| Seed | branch image | result |
| --- | --- | --- |
| YTM-B001 | انقطاع الولد عن كافله | selected image CSU-03/CSU-04; unsupported child role. |
| YTM-B002 | انفراد الشيء وانقطاع نظيره | selected image CSU-04; isolated unit cut off from normal support. |
| YTM-B003 | غفلة وتقصير | local; later `سَاهُونَ` independently reactivates negligence, but the noun here remains orphan. |
| YTM-B004 | إبطاء السير والبر | local; withheld/slow beneficence anticipates failure to feed and ma`un closure. |
| YTM-B005 | انفراد المرأة عن الزوج | dies; no spouse/woman role. |

### 107:3:2 `يَحُضُّ` - `ح ض ض`

| Seed | branch image | result |
| --- | --- | --- |
| HDḌ-B001 | الحَضّ على الشيء | selected image CSU-05; failed social incitement toward feeding. |
| HDḌ-B002 | الحَضيض قرار الأرض | weak local; low/grounded state can thicken miskin humility but no topography. |
| HDḌ-B003 | الحُضُض دواء مر | dies; no medicine/resin/bitter cure role. |
| HDḌ-B004 | استزادة النفس | weak local; internal self-urging is absent under `لا`, but not enough for a candidate. |

### 107:3:4 `طَعَامِ` - `ط ع م`

| Seed | branch image | result |
| --- | --- | --- |
| TʿM-B001 | ذوق الشيء وتناوله | selected image CSU-05; edible nourishment as target. |
| TʿM-B002 | إطعام الغير وطلب الطعام | selected image CSU-05; exact giving/feeding role. |
| TʿM-B004 | رزق ومعاش وحسن حال | local; provision/livelihood expands social-support frame. |
| TʿM-B005 | إدراك الثمر وأخذ الطعم | dies; no fruit/ripening roles. |
| TʿM-B006 | آلة الصيد التي تطعم صاحبها | dies; no bow/raptor/hunting instrument. |
| TʿM-B007 | سمن الحيوان وطعم الشحم | dies; no fattening animal. |
| TʿM-B008 | طعم العقل والقيمة | local weak; moral lack of "taste/value" may fit denial, but no syntactic hook. |
| TʿM-B009 | مستطعم الفرس وطلب جريه | dies; no horse/running request. |
| TʿM-B010 | إطعام الغصن وقبول الوصل | weak fork CSU-12; graft/accepting connection analogizes reattachment of the needy, but remote. |
| TʿM-B011 | القدرة على الشيء | local; capability to help is implied by blame but branch is not generated by local syntax. |
| TʿM-B012 | الأخذ بالمطعمة عند الخنق | dies; no throat/choking combat despite `يدع`. |
| TʿM-B013 | التطاعم بالفم | dies; no mouth-to-mouth scene. |
| TʿM-B014 | تتابع الخلق | weak local; sequence of social behavior, but no created-form chain. |

### 107:3:5 `ٱلْمِسْكِينِ` - `س ك ن`

| Seed | branch image | result |
| --- | --- | --- |
| SKN-B001 | ذهاب الحركة | local; needy one as immobilized/stilled, supports CSU-04/CSU-05. |
| SKN-B002 | استيطان المنزل | local; domestic setting reactivates ma`un household implements. |
| SKN-B003 | أهل الدار | local; household/kin frame supports duty-of-care, not whole model. |
| SKN-B004 | مأنس السكون | weak; comfort/rest is what should be supplied, but not explicit. |
| SKN-B006 | ذل المسكنة | selected image CSU-04/CSU-05; exact poverty/weakness. |
| SKN-B007 | إسكان الذبيحة بالسكين | dies; no slaughter/knife. |
| SKN-B008 | تسكين السفينة بالسكان | dies; no ship/rudder. |
| SKN-B009 | موضع الاستقرار | local; place/stability is a weak support for settled livelihood. |
| SKN-B010 | قوت يثبت المقام | selected secondary in CSU-05; food/provision stabilizes remaining in place. |

### 107:4:2 `وَيْل` - `و ي ل`

| Seed | branch image | result |
| --- | --- | --- |
| WYL-B001 | وقوع الشر والهلاك | selected image CSU-06; doom/harm falls surprisingly on worshippers. |
| WYL-B002 | ندبة الفضيحة والبلية | selected image CSU-06/CSU-09; shame exposure fits public-show reversal. |

### 107:4:3 `لِّلْمُصَلِّينَ` - `ص ل و`

| Seed | branch image | result |
| --- | --- | --- |
| ṢLW4-B001 | ملاقاة النار وحرها | selected as remote secondary in CSU-06; `ويل` + heat/ordeal, but constrained by prayer noun. |
| ṢLW4-B002 | الدعاء والثناء والرحمة | local; prayer as blessing/mercy contrasts with withheld mercy/aid. |
| ṢLW4-B003 | العبادة المخصوصة | selected image CSU-06/CSU-07; exact worshipper/prayer role. |
| ṢLW4-B004 | الشرك المنصوبة | weak terminated; trap image has no syntactic trap target. |
| ṢLW4-B005 | الصَّلا من الظهر والجنب | dies; no body-back/animal-birth. |
| ṢLW4-B006 | تلو السابق في السباق | weak sequence image; worshippers "following" is not passage-local enough. |
| ṢLW4-B007 | مواضع الصلاة ودور العبادة | local; worship-setting possible but no place noun. |
| ṢLW4-B008 | الصَّلاية حجر الدق | dies; no pounding-stone object. |
| ṢLW4-B009 | الصِّليان نبت ترعاه الإبل | dies; no pasture/camel food scene. |

### 107:5:4 `صَلَاتِهِمْ` - `ص ل و`

| Seed | branch image | result |
| --- | --- | --- |
| ṢLW5-B001 | ملاقاة النار وحرها | weak reactivation of CSU-06 only; `عن صلاتهم` constrains it away from literal fire. |
| ṢLW5-B002 | الدعاء والثناء والرحمة | local; prayer should orient mercy, contrasted by neglected dependent/aid. |
| ṢLW5-B003 | العبادة المخصوصة | selected image CSU-07; object from which they are heedless. |
| ṢLW5-B004 | الشرك المنصوبة | dies/constraint; `عن` marks disengagement, not setting a snare. |
| ṢLW5-B005 | الصَّلا من الظهر والجنب | dies. |
| ṢLW5-B006 | تلو السابق في السباق | weak; following without heed is possible but not syntactically anchored. |
| ṢLW5-B007 | مواضع الصلاة ودور العبادة | local weak; no mosque/place word. |
| ṢLW5-B008 | الصَّلاية حجر الدق | dies. |
| ṢLW5-B009 | الصِّليان نبت ترعاه الإبل | dies. |

Supplemental attachment-normalized `ص ل ي` for 107:4 `لِّلْمُصَلِّينَ`: the attachment file normalizes the worshipper word as `ص ل ي` rather than QAC's `ص ل و`. This is not counted as a separate QAC occurrence, but its ten branches were checked because the attachment is structural evidence:

| Supplemental seed | branch image | result |
| --- | --- | --- |
| ṢLY-B001 | الصلاة عبادة لازمة | same successful prayer/worship role as `ص ل و B003`; corroborates CSU-06/CSU-07. |
| ṢLY-B002 | الدعاء والبركة والرحمة | same prayer/mercy contrast as `ص ل و B002`; local support only. |
| ṢLY-B003 | ملاقاة النار وحرها | same remote heat/ordeal branch as `ص ل و B001`; secondary under `ويل`, constrained by prayer syntax. |
| ṢLY-B004 | إيقاد الصلاء وتسوية الشيء بالنار | weak remote fire-shaping image; no kindling/roasting object. |
| ṢLY-B005 | المَصالي أشراك وفخوخ | weak trap image; no trap target or snare syntax. |
| ṢLY-B006 | الصَّلا موضع الظهر والذنب | dies; no back/tail/birth role. |
| ṢLY-B007 | المصلي يتلو السابق | weak sequence echo; no race frame. |
| ṢLY-B008 | الصلوات مواضع عبادة | local worship-place possibility; no place noun. |
| ṢLY-B009 | الصلاية حجر يدق عليه | dies; no pounding stone. |
| ṢLY-B010 | الصِّليان نبت ترعاه الإبل | dies; no pasture/camel plant scene. |

### 107:5:5 `سَاهُونَ` - `س ه و`

| Seed | branch image | result |
| --- | --- | --- |
| SHW-B001 | غفلة القلب وسهوه | selected image CSU-07; exact heedlessness from prayer. |
| SHW-B002 | السهو سكون | local; static stillness after lack of motion links to non-incitement, but secondary. |
| SHW-B003 | المساهاة وحسن المخالقة | weak rival; overlooking another's fault is positive, but passage constrains to heedlessness `عن صلاتهم`. |
| SHW-B004 | السُّهْوَة موضع أو عارضة أمام البيت | weak household shelf image; could meet ma`un household goods, but no local word. |
| SHW-B005 | السُّها كويكب خفيّ | selected weak image CSU-13; hidden/faint thing missed by sight reactivates seeing words, but remote. |

### 107:6:3 `يُرَآءُونَ` - `ر ء ي`

| Seed | branch image | result |
| --- | --- | --- |
| RAY6-B001 | رؤية العين والبصيرة | selected image CSU-09; action tuned to being seen. |
| RAY6-B002 | رأي القلب والتفكر | local; inner judgment absent beneath outer display. |
| RAY6-B003 | الرؤيا في المنام | dies. |
| RAY6-B004 | تراء وتواجه | selected image CSU-09; reciprocal visibility/social facing. |
| RAY6-B005 | رياء الناس | selected image CSU-09; exact riya branch. |
| RAY6-B006 | مرأى ومنظر ومرآة | local; appearance/visible form supports display. |
| RAY6-B007 | ترية الحيض | dies. |
| RAY6-B008 | رئي من الجن | dies. |
| RAY6-B009 | الرئة وما يصيبها | dies. |
| RAY6-B010 | ظهور حمل الناقة أو الشاة | dies. |
| RAY6-B011 | راية منصوبة | weak; display signal but no banner. |
| RAY6-B012 | إراءة وإظهار | selected image CSU-09; making action visible. |
| RAY6-B013 | أرأيتك للتنبيه والاستخبار | selected as backward reactivation of 107:1 in CSU-09; not the Form III sense itself. |

### 107:7:1 `يَمْنَعُونَ` - `م ن ع`

| Seed | branch image | result |
| --- | --- | --- |
| MNʿ-B001 | كف اليد عن العطاء | selected image CSU-08; exact withholding. |
| MNʿ-B002 | حاجز بين المرء وما يريد | selected image CSU-08; barrier between needy/helper and small benefit. |
| MNʿ-B003 | قوة تحمي فلا يخلص إليها | weak local; self-protective guardedness fits refusal, but no fortress. |
| MNʿ-B004 | تعفف يمتنع عن الفاحشة | dies; no chastity/fahisha frame. |
| MNʿ-B005 | مناع صيحة أمر بالمنع | dies; no imperative cry. |
| MNʿ-B006 | ممانعة في الشيء | local; mutual resistance possible but syntax is direct object withholding. |
| MNʿ-B007 | فتاء يقاوم السنة | dies; no young animal/year-resistance scene. |

### 107:7:2 `ٱلْمَاعُونَ` - `م ع ن`

| Seed | branch image | result |
| --- | --- | --- |
| MʿN-B001 | جريان الماء وظهوره | selected secondary in CSU-08; flow of small utility/water is stopped by `يمنعون`. |
| MʿN-B002 | الإبعاد في العدو | dies; no horse/running away. |
| MʿN-B003 | اليسر والقلة وخفة الخطر | selected image CSU-08; small/easy thing. |
| MʿN-B005 | الماعون منفعة قليلة مبذولة | selected image CSU-08; exact closure object. |
| MʿN-B006 | المعان منزلا ومباءة | local; household/home setting supports implements but not whole model. |

Supplemental attachment-normalized `ع و ن` for `ٱلْمَاعُونَ`: `ʿWN-B001 الإعانة والمظاهرة` corroborates aid/help in CSU-08. Branches B002-B008 of `ع و ن` were tested and rejected: age-middle, repeated war, old palm, bodily maturity, wild-ass herd, pubic hair, and place-name do not fit the local object.

## Constructional, Morphosyntactic, And Temporal Seeds

| Seed | result |
| --- | --- |
| C-01 `أَرَءَيْتَ ٱلَّذِى` | selected CSU-01; opening object of attention is a person/profile, not an abstract proposition alone. |
| C-02 `يُكَذِّبُ بِٱلدِّينِ` | selected CSU-02; `بـ` marks governed denial-object; the denied frame generates later behavioral tests. |
| C-03 `فَذَٰلِكَ ٱلَّذِى` | selected CSU-01; deictic identification freezes: "that one" is recognized by subsequent acts. |
| C-04 `يَدُعُّ ٱلْيَتِيمَ` | selected CSU-03; direct-object violent repulsion of dependent. |
| C-05 `لَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ` | selected CSU-05; missing incitement toward the food of the poor. |
| C-06 `فَوَيْلٌ لِّلْمُصَلِّينَ` | selected CSU-06; pivot/surprise: doom attached to worshippers, forcing a narrower class. |
| C-07 `عَن صَلَاتِهِمْ سَاهُونَ` | selected CSU-07; `عن` makes prayer the matter away from which attention drifts. |
| C-08 `ٱلَّذِينَ هُمْ ... ٱلَّذِينَ هُمْ ...` | selected CSU-07/09; repeated relative clauses create profile accumulation after the doom pivot. |
| C-09 `يُرَآءُونَ` Form III | selected CSU-09; reciprocal/public seeing reactivates opening `أرأيت`. |
| C-10 `يَمْنَعُونَ ٱلْمَاعُونَ` | selected CSU-08; final direct-object withholding closes with a minimal aid object. |
| T-01 ayah order 1->2->3 | selected CSU-02/05; denial of accountability is not left abstract but externalized in vulnerable-person and food relations. |
| T-02 ayah order 4->5->6->7 | selected CSU-06/09/08; ritual identity is narrowed by heedlessness, display, and withheld aid. |
| T-03 repetition of seeing root 107:1 and 107:6 | selected CSU-09; audit-seeing becomes ostentatious self-showing. |
| T-04 closure at `الماعون` | selected CSU-08; closes where minimal concrete benefit is withheld after all larger public claims have been tested. |

## Candidate Synthesis Units

### CSU-01 - The Summoned Audit Of A Person

- `candidate_id`: S107-CSU-01
- `ayah_range`: 107:1-2, reactivated through 107:6
- `seed_type`: lexical + constructional
- `seed`: 107:1:1 `أَرَءَيْتَ`, `ر ء ي B013` with `ر ء ي B001/B002`
- `generating_set`: `(E: ر ء ي B013 alerting/inquiry)`, `(E: ر ء ي B001 seeing/recognition)`, `(E: construction أَرَءَيْتَ ٱلَّذِى direct object)`.
- `selected_branches`: RAY1-B013, RAY1-B001, RAY1-B002; later RAY6-B005/RAY6-B012 as corroboration.
- `constructed_model`: The reciter is made to inspect a recognizable human profile. The first cue asks for seeing/considering; the next words identify the person by a denial, then `فَذَٰلِكَ` points back and says the denial can be seen again in concrete acts.
- `freeze_point`: After 107:2 `فَذَٰلِكَ ٱلَّذِى`.
- `predictions_at_freeze`: The passage should give observable behaviors; the denied object should become visible in action; later sight/display vocabulary would be especially relevant.
- `unused_features_tested`: 107:2 pushing; 107:3 non-incitement; 107:4 doom pivot; 107:6 `يراءون`; final withholding.
- `corroborators`: `(C: sequence 107:1->107:2, deictic فذلك)`, `(C: ر ء ي B005 at 107:6 public showing)`, `(C: ر ء ي B012 at 107:6 showing/making visible)`.
- `constraints`: `(K: opening أَرَءَيْتَ does not mean hypocrisy; it only opens inspection)`, `(K: relative pronoun object is a person, not a free-floating visual scene)`.
- `temporal_reactivation_notes`: The opening seeing command fades while social acts accumulate; it is reactivated sharply when the same root returns as `يُرَآءُونَ`, turning the audit outward: the one inspected also acts for inspection.
- `rival_models`: Dream/jinn/lung/pregnancy branches die; banner/appearance branches remain weak display supports only.
- `grade`: strong
- `grade_rationale`: Specific opening construction, deictic identification, later same-root reactivation, and behavior sequence converge independently.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` S107 `ر ء ي`; `v4_branches.tsv` root `ر ء ي`; attachment 107:1 a1, 107:2 a1, 107:6 a1.

### CSU-02 - Denying Accountability Becomes No Social Accounting

- `candidate_id`: S107-CSU-02
- `ayah_range`: 107:1-7
- `seed_type`: lexical + morphosyntactic
- `seed`: 107:1:4 `بِٱلدِّينِ`, `د ي ن B002`; independently reached from `ك ذ ب B002`.
- `generating_set`: `(E: د ي ن B002 judgment/account/recompense)`, `(E: ك ذ ب B002 Form II attribution/rejection as false)`, `(E: attachment 107:1 a2 بِٱلدِّينِ governed complement)`.
- `selected_branches`: DYN-B002, KDB-B002, DYN-B001, DYN-B007.
- `constructed_model`: The denied thing is an order of answerability. Once that account is rejected, vulnerable claims are treated as non-binding: the orphan can be shoved away, the poor person's food need not be socially urged, ritual can be performed as display, and small aid can be withheld.
- `freeze_point`: After 107:1.
- `predictions_at_freeze`: Expect concrete refusal of obligation, failure of obedience, denial of owed dues, and acts that reveal no fear of reckoning.
- `unused_features_tested`: Direct object orphan; `لا يحض`; food/idafa poor; prayer pivot; riya; preventing ma`un.
- `corroborators`: `(C: د ي ن B001 obedience/obedience-denial seen in failed duties)`, `(C: د ي ن B003 debt/dues as secondary support for owed food/aid)`, `(C: م ن ع B001 withholding gift)`, `(C: م ع ن B005 small benefit)`, `(C: sequence from creed-denial to social acts)`.
- `constraints`: `(K: بِٱلدِّينِ is complement of denial, not a literal financial debt in context)`, `(K: د ي ن B004 humiliation is not the main object, though orphan humiliation follows)`.
- `temporal_reactivation_notes`: The first ayah activates judgment/account. The later concrete refusals are heard as the practical shape of refusing account: no care-account for orphan, no food-account for poor, no sincerity-account in prayer, no aid-account at closure.
- `rival_models`: `مدينة الطاعة` dies; financial debt remains secondary, not primary translation.
- `grade`: strong
- `grade_rationale`: The model predicts the passage's movement from denied accountability to failures of obligation and small owed aid; corroboration comes from syntax, sequence, and distinct roots.
- `source_queries_or_rows_used`: `د ي ن`, `ك ذ ب`, `م ن ع`, `م ع ن` branch rows; attachment 107:1 a2, 107:7 a1.

### CSU-03 - Pushing Away The Cut-Off Dependent

- `candidate_id`: S107-CSU-03
- `ayah_range`: 107:2 with links to 107:3 and 107:7
- `seed_type`: lexical
- `seed`: 107:2:3 `يَدُعُّ`, `د ع ع B001`
- `generating_set`: `(E: د ع ع B001 harsh pushing/repulsion)`, `(E: ي ت م B001 child cut off from guardian)`, `(E: attachment 107:2 a2 direct object)`.
- `selected_branches`: DAع-B001, YTM-B001, YTM-B002; DAع-B004 as inverted rival.
- `constructed_model`: A person lacking ordinary support is met not with replacement support but with a force that increases distance. The direct object relation makes the vulnerable person the target of repulsion.
- `freeze_point`: After 107:2.
- `predictions_at_freeze`: Expect further failures to supply or mobilize support; expect small aid to be blocked rather than given.
- `unused_features_tested`: `لا يحض` toward food; `مسكين`; `يمنعون الماعون`; prayer/riya pivot.
- `corroborators`: `(C: ي ت م B002 isolated/single)`, `(C: ح ض ض B001 missing incitement)`, `(C: ط ع م B002 feeding others)`, `(C: م ن ع B001 withholding)`.
- `constraints`: `(K: د ع ع B002 vessel-filling is syntactically blocked because the object is اليتيم)`, `(K: د ع ع B003 herd-zajr lacks animal frame)`.
- `temporal_reactivation_notes`: The initial denial becomes visible as bodily/social force. Later non-feeding and withholding reactivate the same failure of support in less violent but still withholding forms.
- `rival_models`: DAع-B004 "raise the stumbled" is a counter-image: the passage shows the opposite action.
- `grade`: strong
- `grade_rationale`: Exact branch and direct-object syntax fit, then later food and aid failures independently complete the support-withholding model.
- `source_queries_or_rows_used`: `د ع ع`, `ي ت م`, `ح ض ض`, `ط ع م`, `م ن ع`; attachment 107:2 a2.

### CSU-04 - The Isolated/Still Needy Person

- `candidate_id`: S107-CSU-04
- `ayah_range`: 107:2-3
- `seed_type`: lexical
- `seed`: 107:2:4 `ٱلْيَتِيمَ`, `ي ت م B001/B002`
- `generating_set`: `(E: ي ت م B001 cut off from guardian)`, `(E: ي ت م B002 isolated/singular)`, `(E: س ك ن B006 poverty/weakness/humility)`.
- `selected_branches`: YTM-B001, YTM-B002, SKN-B006, SKN-B001, SKN-B010.
- `constructed_model`: The passage moves from one cut-off dependent to another socially immobilized figure. The orphan is missing a protector; the poor person is marked by weakness and need; both require motion from others.
- `freeze_point`: After 107:3 `المسكين`.
- `predictions_at_freeze`: Expect either feeding, urging, aid, or their negation; expect closure on whether small help moves toward the needy.
- `unused_features_tested`: `لا يحض`, `طعام`, `يمنعون`, `الماعون`.
- `corroborators`: `(C: ح ض ض B001 under negation, no mobilization)`, `(C: ط ع م B001/B002 food and feeding)`, `(C: م ع ن B005 small household benefit)`, `(C: ع و ن B001 attachment-normalized help)`.
- `constraints`: `(K: س ك ن B007 knife/slaughter and B008 ship-rudder die)`, `(K: orphan and poor are not collapsed into one lexical meaning; they converge as roles needing support)`.
- `temporal_reactivation_notes`: 107:2 activates severed dependency; 107:3 generalizes it into social poverty and food. The final ma`un closure reactivates both as missing small supports.
- `rival_models`: YTM-B003 negligence is tempting because of `ساهون`, but for `اليتيم` it remains only a later echo, not the noun's primary image.
- `grade`: medium-strong
- `grade_rationale`: Strong local role convergence, but broader synthesis depends on social-support modeling rather than a single exact root chain.
- `source_queries_or_rows_used`: `ي ت م`, `س ك ن`, `ط ع م`, `م ع ن`, `ع و ن`; attachments 107:2 a2, 107:3 a2.

### CSU-05 - No Social Incitement Toward Nourishment

- `candidate_id`: S107-CSU-05
- `ayah_range`: 107:3 and 107:7
- `seed_type`: constructional + lexical
- `seed`: 107:3 `لَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ`
- `generating_set`: `(E: ح ض ض B001 urging/incitement)`, `(E: negation لا)`, `(E: ط ع م B001 food/tasting/nourishment)`, `(E: ط ع م B002 feeding another)`, `(E: س ك ن B006 poor/weak)`, `(E: attachment 107:3 a1 على طعام)`.
- `selected_branches`: HDḌ-B001, TʿM-B001, TʿM-B002, SKN-B006, SKN-B010.
- `constructed_model`: Not only is aid absent; the social mechanism that would stir others toward feeding is absent. The passage moves from violent removal of one dependent to failure to mobilize provision for another.
- `freeze_point`: After 107:3.
- `predictions_at_freeze`: Later evidence should show continued blockage of small assistance; the failure may become inward/ritual rather than only social.
- `unused_features_tested`: prayer pivot, heedlessness, riya, ma`un.
- `corroborators`: `(C: م ن ع B001 final withholding)`, `(C: م ع ن B003 easy/little thing)`, `(C: م ع ن B005 small household benefit)`, `(C: attachment 107:7 direct object)`.
- `constraints`: `(K: ح ض ض B002 ground/topography, B003 bitter medicine, B004 self-increase do not fit the governed على طعام construction)`, `(K: ط ع م remote hunting/horse/choking branches die)`.
- `temporal_reactivation_notes`: The missing `حض` leaves an unfilled social-force role. The final `يمنعون` fills that role negatively: not only no urging toward food, but active prevention of even small utility.
- `rival_models`: A private self-urging model from HDḌ-B004 remains weak because the surface construction is public/social urging toward an object.
- `grade`: strong
- `grade_rationale`: Exact construction, exact food/feeding branches, clear negative social mechanism, and final withholding converge.
- `source_queries_or_rows_used`: `ح ض ض`, `ط ع م`, `س ك ن`, `م ن ع`, `م ع ن`; attachment 107:3 a1-a2, 107:7 a1.

### CSU-06 - Doom At The Prayer Pivot

- `candidate_id`: S107-CSU-06
- `ayah_range`: 107:4-5
- `seed_type`: lexical + temporal
- `seed`: 107:4 `فَوَيْلٌ لِّلْمُصَلِّينَ`, `و ي ل B001`
- `generating_set`: `(E: و ي ل B001 doom/harm)`, `(E: ص ل و B003 prayer/worship)`, `(E: attachment 107:4 a1/a2 لِّلْمُصَلِّينَ governed/predicate phrase)`.
- `selected_branches`: WYL-B001, WYL-B002, ṢLW4-B003; ṢLW4-B001 as remote heat ordeal.
- `constructed_model`: The passage pivots unexpectedly: doom is not placed on overt deniers only but on a class named by prayer, then narrowed by heedlessness and display. This creates a test of whether ritual surface repairs the social/accountability failure.
- `freeze_point`: After 107:4.
- `predictions_at_freeze`: Expect qualification of which worshippers; expect defect in relation to prayer; expect public appearance may matter.
- `unused_features_tested`: `عن صلاتهم ساهون`, `يراءون`, `يمنعون الماعون`.
- `corroborators`: `(C: attachment 107:5 a1 عن marks disengagement from prayer)`, `(C: س ه و B001 heedlessness)`, `(C: ر ء ي B005 riya)`, `(C: م ن ع B001 withholding shows ritual does not become aid)`.
- `constraints`: `(K: ص ل و B001 fire/heat is secondary; local noun is worshippers/prayer)`, `(K: trap, back, race, stone, plant branches do not fit the syntactic prayer profile)`.
- `temporal_reactivation_notes`: The `فـ` pivot after social failures shocks the listener: the issue now reappears inside religious performance. Subsequent clauses explain the doomed subset.
- `rival_models`: Literal fire/heat model is possible as secondary doom imagery but cannot replace primary prayer meaning.
- `grade`: medium-strong
- `grade_rationale`: Strong syntax and sequence; the remote fire branch is constrained, so grade rests on the pivot logic and subsequent narrowing.
- `source_queries_or_rows_used`: `و ي ل`, `ص ل و`, supplemental `ص ل ي`; attachments 107:4 a1-a2, 107:5 a1.

### CSU-07 - Prayer Detached From Attention

- `candidate_id`: S107-CSU-07
- `ayah_range`: 107:5
- `seed_type`: constructional + lexical
- `seed`: 107:5 `عَن صَلَاتِهِمْ سَاهُونَ`, `س ه و B001`
- `generating_set`: `(E: س ه و B001 heedlessness/heart going away)`, `(E: ص ل و B003 ritual prayer)`, `(E: attachment 107:5 a1 عن صلاتهم governed matter)`.
- `selected_branches`: SHW-B001, ṢLW5-B003, ṢLW5-B002 as mercy-prayer contrast.
- `constructed_model`: The prayer is present as a named possession, but attention is displaced away from it. The relation is not mere accidental lapse inside a ritual; `عن` frames the prayer itself as the matter from which they are heedless.
- `freeze_point`: After 107:5.
- `predictions_at_freeze`: Expect outwardness without inward attention; expect visible performance and blocked aid to follow.
- `unused_features_tested`: 107:6 `يراءون`; 107:7 `يمنعون الماعون`.
- `corroborators`: `(C: ر ء ي B005 riya, action for others' sight)`, `(C: م ن ع B001 withholding, showing prayer did not move into mercy/aid)`, `(C: ص ل و B002 prayer as prayer/mercy contrast)`.
- `constraints`: `(K: س ه و B003 good-natured overlooking is blocked by عن صلاتهم and doom context)`, `(K: س ه و B004 shelf and B005 hidden star remain secondary/remote)`.
- `temporal_reactivation_notes`: Prayer first seemed to mark religious identity; the next ayah reconditions it as an unattended object. The listener revises `للمصلين` from honorable label to exposed defect.
- `rival_models`: Positive indulgent-overlooking from SHW-B003 is defeated by `فويل` and `عن صلاتهم`.
- `grade`: strong
- `grade_rationale`: Exact lexical branch, exact attachment, and immediate sequence to public display produce a specific model.
- `source_queries_or_rows_used`: `س ه و`, `ص ل و`, `ر ء ي`, `م ن ع`; attachment 107:5 a1-a2.

### CSU-08 - Blocking The Small Flow Of Help

- `candidate_id`: S107-CSU-08
- `ayah_range`: 107:7 with backward links to 107:2-3
- `seed_type`: lexical + closure
- `seed`: 107:7 `وَيَمْنَعُونَ ٱلْمَاعُونَ`, `م ن ع B001` and `م ع ن B005`
- `generating_set`: `(E: م ن ع B001 withholding from giving)`, `(E: م ن ع B002 barrier between person and desired thing)`, `(E: م ع ن B005 small household benefit/known aid/ma`un)`, `(E: م ع ن B003 easy/little thing)`, `(E: attachment 107:7 a1 direct object)`.
- `selected_branches`: MNʿ-B001, MNʿ-B002, MʿN-B005, MʿN-B003, MʿN-B001; supplemental `ع و ن B001`.
- `constructed_model`: The surah closes on active prevention of a small, easy, useful benefit. After large claims of religion and prayer, the decisive final test is tiny concrete help.
- `freeze_point`: After 107:7.
- `predictions_at_freeze`: Closure should reactivate earlier failures of support: the orphan pushed away and poor not fed.
- `unused_features_tested`: Earlier orphan/poor/food/incitement roots and sequence.
- `corroborators`: `(C: ط ع م B002 feeding another)`, `(C: ح ض ض B001 missing urging)`, `(C: ي ت م B001 unsupported child)`, `(C: س ك ن B006 poor/weak)`, `(C: ع و ن B001 attachment-normalized help)`, `(C: م ع ن B001 flow/water as secondary: help that should run is stopped)`.
- `constraints`: `(K: م ع ن B002 running far, B006 place-name/home are not primary)`, `(K: م ن ع fortress/chastity/imperative branches do not fit direct object withholding)`.
- `temporal_reactivation_notes`: The final word makes earlier social failures concrete again. The passage closes not with an abstract verdict but with a blocked object small enough that refusal itself exposes the inner denial.
- `rival_models`: Water-flow image from MʿN-B001 is retained only as secondary motion/flow; exact ma`un benefit branch controls.
- `grade`: strong
- `grade_rationale`: Exact final verb-object syntax, exact ma`un branch, and powerful backward reactivation of orphan/food failures.
- `source_queries_or_rows_used`: `م ن ع`, `م ع ن`, supplemental `ع و ن`; attachment 107:7 a1.

### CSU-09 - Seeing Reverses Into Being Seen

- `candidate_id`: S107-CSU-09
- `ayah_range`: 107:1 and 107:6
- `seed_type`: verified composite
- `seed`: repeated `ر ء ي`: 107:1 `أَرَءَيْتَ` and 107:6 `يُرَآءُونَ`
- `generating_set`: `(E: ر ء ي B005 at 107:6 riya/showing for people)`, `(E: ر ء ي B012 showing/making visible)`, `(E: Form III/attachment 107:6 predication)`.
- `selected_branches`: RAY6-B005, RAY6-B012, RAY6-B004; opening RAY1-B013/RAY1-B001 as corroborating reactivation.
- `constructed_model`: The passage begins by asking the listener to see/consider someone; later the defective worshippers perform so that people see them. The object of audit tries to manage visibility.
- `freeze_point`: After 107:6.
- `predictions_at_freeze`: A final act should reveal whether public religious visibility becomes concrete aid; if not, display is exposed as empty.
- `unused_features_tested`: 107:7 withholding ma`un.
- `corroborators`: `(C: opening ر ء ي B013 alerting/inquiry)`, `(C: ر ء ي B001 seeing)`, `(C: و ي ل B002 shame/exposure)`, `(C: م ن ع B001 final withholding exposes display)`.
- `constraints`: `(K: RAY1 does not itself mean riya; riya is generated only at 107:6)`, `(K: mirror/banner branches are secondary display supports, not primary)`.
- `temporal_reactivation_notes`: This is the clearest reactivation event in the surah. The listener's seeing at 107:1 is inverted into the hypocritical actor's desire to be seen at 107:6.
- `rival_models`: RAY-B006 mirror and B011 banner produce display imagery but lack exact Form III support.
- `grade`: strong
- `grade_rationale`: Same root at structurally distant points, exact riya branch, and final behavioral exposure create high specificity.
- `source_queries_or_rows_used`: `ر ء ي` branch rows; attachments 107:1 a1, 107:6 a1.

### CSU-10 - Deceptive Surface / False Textile

- `candidate_id`: S107-CSU-10
- `ayah_range`: 107:1, 107:4-7
- `seed_type`: lexical weak
- `seed`: `ك ذ ب B009` false-looking decorated cloth
- `generating_set`: `(E: ك ذ ب B009 thing that lies by its appearance)`, `(E: ر ء ي B005 riya/show)`, `(E: ص ل و B003 prayer surface)`.
- `selected_branches`: KDB-B009, RAY6-B005, RAY6-B006.
- `constructed_model`: Public prayer can be heard as a surface whose appearance "lies" about the actor's inner/accountable state, exposed by withheld aid.
- `freeze_point`: After 107:6.
- `predictions_at_freeze`: Expect contradiction between appearance and concrete giving.
- `unused_features_tested`: 107:7 `يمنعون الماعون`.
- `corroborators`: `(C: م ن ع B001 refusal after display)`, `(C: د ي ن B002 accountability denied beneath surface)`.
- `constraints`: `(K: no cloth/garment word, no textile syntax)`, `(K: ك ذ ب B002 remains the contextual denial branch)`.
- `temporal_reactivation_notes`: The remote branch gains relevance only after display vocabulary appears; it does not generate the primary meaning.
- `rival_models`: None retained.
- `grade`: weak
- `grade_rationale`: The appearance/deception geometry is coherent but remote and lacks concrete textile roles.
- `source_queries_or_rows_used`: `ك ذ ب`, `ر ء ي`, `م ن ع`.

### CSU-11 - Empty Vessel / Refused Filling

- `candidate_id`: S107-CSU-11
- `ayah_range`: 107:2-3
- `seed_type`: lexical weak
- `seed`: `د ع ع B002` shaking/filling a measure or vessel
- `generating_set`: `(E: د ع ع B002 vessel/moving to fill)`, `(E: ط ع م B001 food)`, `(E: س ك ن B006 poor person)`.
- `selected_branches`: DAع-B002, TʿM-B001, TʿM-B002.
- `constructed_model`: A weak secondary image tries to form around a container that should be filled with food for the poor, but the actual verb object is the orphan, not a vessel.
- `freeze_point`: After 107:3.
- `predictions_at_freeze`: Expect vessel/measure/portion language.
- `unused_features_tested`: ma`un household implements; food; miskin.
- `corroborators`: `(C: ط ع م B001/B002 food/feeding)`, `(C: م ع ن B005 household benefit, weak)`.
- `constraints`: `(K: attachment 107:2 a2 makes اليتيم direct object of يدع)`, `(K: no vessel/measure word)`.
- `temporal_reactivation_notes`: The image is triggered by proximity to food but is defeated by syntax.
- `rival_models`: DAع-B001 harsh pushing is the successful rival.
- `grade`: unlikely
- `grade_rationale`: Passage-local food supports are insufficient against direct-object syntax.
- `source_queries_or_rows_used`: `د ع ع`, `ط ع م`, attachments 107:2 a2, 107:3 a1.

### CSU-12 - Graft / Failed Reconnection

- `candidate_id`: S107-CSU-12
- `ayah_range`: 107:2-3, 107:7
- `seed_type`: lexical weak
- `seed`: `ط ع م B010` graft accepting a joined branch
- `generating_set`: `(E: ط ع م B010 graft/accepting connection)`, `(E: ي ت م B001 cut off)`, `(E: م ع ن B005 small aid)`.
- `selected_branches`: TʿM-B010, YTM-B001, MʿN-B005.
- `constructed_model`: The cut-off dependent should be rejoined to support, as a graft takes connection; the passage instead shows repulsion, no feeding, and blocked small aid.
- `freeze_point`: After 107:3.
- `predictions_at_freeze`: Expect joining/support/acceptance language.
- `unused_features_tested`: ma`un and preventing.
- `corroborators`: `(C: م ن ع B002 barrier)`, `(C: ح ض ض B001 missing social urging)`.
- `constraints`: `(K: no plant/grafting lexeme)`, `(K: طعام in context is food, not graft)`.
- `temporal_reactivation_notes`: Remote branch turns the support failure into a connection failure but remains subordinate.
- `rival_models`: Direct food/feeding model CSU-05.
- `grade`: weak
- `grade_rationale`: Good relational geometry but branch is remote from the contextual noun.
- `source_queries_or_rows_used`: `ط ع م`, `ي ت م`, `م ن ع`, `م ع ن`.

### CSU-13 - Hidden Small Thing Missed By Sight

- `candidate_id`: S107-CSU-13
- `ayah_range`: 107:5-7 with backward link to 107:1
- `seed_type`: lexical weak
- `seed`: `س ه و B005` the faint hidden star overlooked by sight
- `generating_set`: `(E: س ه و B005 hidden/faint thing missed)`, `(E: ر ء ي B001 seeing)`, `(E: م ع ن B003 small/easy thing)`.
- `selected_branches`: SHW-B005, RAY1-B001, MʿN-B003.
- `constructed_model`: The hearer is asked to see what is easy to miss: the small withheld thing exposes the large religious display. This is attractive because the surah closes on the little ma`un.
- `freeze_point`: After 107:7.
- `predictions_at_freeze`: Expect hidden/faint object or star vocabulary.
- `unused_features_tested`: none after closure; backward test only.
- `corroborators`: `(C: م ع ن B003 little/easy)`, `(C: ر ء ي repeated sight root)`.
- `constraints`: `(K: no star/night/sky lexeme)`, `(K: س ه و B001 is the exact contextual branch)`.
- `temporal_reactivation_notes`: The image is a useful auditory/cognitive analogy for missed smallness but not a primary lexical synthesis.
- `rival_models`: CSU-07 exact heedlessness model.
- `grade`: weak
- `grade_rationale`: It explains smallness and seeing, but lacks scene roles and is remote.
- `source_queries_or_rows_used`: `س ه و`, `ر ء ي`, `م ع ن`.

## Failed Seed Classes

These branches were restarted as seeds and terminated after the full sweep because they lacked passage-local participants, mechanisms, or syntax:

- Dream, jinn, lung, pregnancy, menstrual sign branches of `ر ء ي`.
- Obligation idiom, charge-courage, immediacy, milk, wild animal pause, soul-name branches of `ك ذ ب`, except the weak false-surface branch.
- City branch of `د ي ن`.
- Twisted running, water plant, black seed/grain branches of `د ع ع`; child-dependents branch survived only as a weak corroborator.
- Woman-without-spouse branch of `ي ت م`.
- Ground-bottom, bitter medicine, self-increase branches of `ح ض ض`, except weak low-state/self-urge echoes.
- Fruit ripening, hunting bow, animal fat, horse-mouth/running, ability, choking, mouth-contact, and created-form sequence branches of `ط ع م`, except weak graft and value/capacity echoes.
- Knife, ship-rudder, stone, plant, animal-back, race, trap branches of `ص ل و`/`ص ل ي`, except remote heat and weak trap notes.
- Good-natured overlooking, shelf/house-front, and hidden-star branches of `س ه و`, except weak CSU-13.
- Fortress, chastity, imperative cry, mutual resistance, young-animal/year resistance branches of `م ن ع`, except local guardedness.
- Running far and place/home branches of `م ع ن`, except home as household setting.
- All non-help branches of supplemental `ع و ن`.

## Consolidated Image

The strongest synthesis is a sequence of exposure:

1. The listener is cued to inspect a person.
2. The person denies accountability/obedience.
3. That denial is reactivated as concrete social force: pushing away the cut-off dependent and failing to mobilize food for the poor.
4. The passage pivots to worshippers, preventing a shallow split between "denier" and "religious performer."
5. Prayer is exposed as unattended and public-facing.
6. The final test is minimal concrete aid: the small benefit that should flow easily is withheld.

This is not an alternative translation. The primary surface remains: the one who denies the dīn pushes away the orphan, does not urge feeding the poor, and the threatened worshippers are heedless of their prayer, show off, and withhold ma`un. The secondary simulation is an accountability-audit in which public visibility, social support, and tiny aid repeatedly expose whether the inward claim has become actual obligation.

## Image Packet Catalog

IMAGE_ID: IMG-01  
Starting seed: `ر ء ي B013`, 107:1 `أَرَءَيْتَ`  
Complete image: summoned audit of a visible human profile.  
Passage-order assembly: seeing -> denial -> deictic identification -> visible acts -> riya reactivation.  
Participants and roles: listener/auditor; profiled denier; vulnerable recipients; public viewers.  
Operation / mechanism: attention is directed, then the person is identified by behavior.  
Direction / force / medium: sight/consideration moves from listener toward person; later the person redirects action toward public sight.  
Temporal development: first cue fades, returns at 107:6.  
Outcome / closure: final withholding exposes the show.  
Exact branch constituents: `ر ء ي B013`, `B001`, later `B005`, `B012`; `ك ذ ب B002`; `م ن ع B001`.  
Unfilled roles, if any: none.  
Status: COMPLETE

IMAGE_ID: IMG-02  
Starting seed: `د ي ن B002`, 107:1 `بِٱلدِّينِ`  
Complete image: denied accountability becoming social non-accounting.  
Passage-order assembly: denial of dīn -> orphan pushed -> poor not fed -> prayer hollowed -> ma`un withheld.  
Participants and roles: accountable actor; vulnerable claimants; ritual performance; small aid object.  
Operation / mechanism: rejecting account removes felt obligation.  
Direction / force / medium: obligation should move outward as care; it is blocked.  
Temporal development: abstract denial is progressively embodied.  
Outcome / closure: minimal aid is refused.  
Exact branch constituents: `د ي ن B002/B001/B003/B007`, `ك ذ ب B002`, `د ع ع B001`, `ح ض ض B001`, `م ن ع B001`, `م ع ن B005`.  
Unfilled roles, if any: none.  
Status: COMPLETE

IMAGE_ID: IMG-03  
Starting seed: `د ع ع B001`, 107:2 `يَدُعُّ`  
Complete image: force applied against the unsupported dependent.  
Passage-order assembly: denial -> harsh repulsion -> no feeding mobilization -> small aid blocked.  
Participants and roles: pusher; orphan; poor person; withheld helper.  
Operation / mechanism: support is replaced by repelling force.  
Direction / force / medium: force moves the vulnerable person away; later aid is prevented from moving toward need.  
Temporal development: direct bodily act becomes broader withholding pattern.  
Outcome / closure: aid remains blocked.  
Exact branch constituents: `د ع ع B001`, `ي ت م B001/B002`, `ح ض ض B001`, `ط ع م B002`, `م ن ع B001`.  
Unfilled roles, if any: none.  
Status: COMPLETE

IMAGE_ID: IMG-04  
Starting seed: `س ه و B001`, 107:5 `سَاهُونَ`  
Complete image: prayer present as identity but absent as attended obligation.  
Passage-order assembly: doom to worshippers -> away from prayer -> riya -> withheld aid.  
Participants and roles: worshipper; prayer; public viewers; needy recipient.  
Operation / mechanism: attention detaches from prayer and attaches to public seeing.  
Direction / force / medium: `عن` moves attention away; riya moves visibility outward.  
Temporal development: prayer label is narrowed by defects.  
Outcome / closure: unattended prayer does not produce small aid.  
Exact branch constituents: `ص ل و B003`, `س ه و B001`, `ر ء ي B005`, `م ن ع B001`, `م ع ن B005`.  
Unfilled roles, if any: none.  
Status: COMPLETE

IMAGE_ID: IMG-05  
Starting seed: `م ن ع B001` + `م ع ن B005`, 107:7  
Complete image: final barrier against small useful help.  
Passage-order assembly: orphan and poor activate need -> prayer/display tested -> ma`un withheld.  
Participants and roles: withholders; small aid object; needy implied recipients.  
Operation / mechanism: giving/flow is stopped.  
Direction / force / medium: aid should move outward; preventing blocks it.  
Temporal development: closes the earlier food/support failures in a minimal concrete object.  
Outcome / closure: the small, easy benefit is refused.  
Exact branch constituents: `م ن ع B001/B002`, `م ع ن B005/B003`, supplemental `ع و ن B001`, `ط ع م B002`, `ح ض ض B001`.  
Unfilled roles, if any: none.  
Status: COMPLETE
