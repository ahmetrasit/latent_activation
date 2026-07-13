# Stage 1 Pass 1 — S100 comparator test lane

Assigned passage: S100  
Sacred Arabic source: `resources/quran/surah_100.json`  
Prompt followed: `v1/prompts/stage1.md`  
Output: `v1/outputs/100_comparator/stage1_test_pass1.md`

## Boundary and source note

Only the sacred Arabic JSON, QAC rows for S100:1–11, S100 attachment rows, and uncontaminated furuq v4 branch dossiers for S100 roots were used. No translations, tafsir, hadith, other output files, web sources, or external interpretation were used.

The sacred JSON contains the basmala as `verse_0`. QAC had no S100 ayah-0 rows, so the basmala is treated only as visible opening-context Arabic from the sacred JSON and is not used to initiate or corroborate any seed below.

First rooted word in the seed interval: `100:1:1 وَٱلْعَٰدِيَٰتِ`, root `ع د و`.

Global lexical sweep roots, visited as dossiers for seed passes: `ع د و، ض ب ح، و ر ي، ق د ح، غ ي ر، ص ب ح، ث و ر، ن ق ع، و س ط، ج م ع، ء ن س، ر ب ب، ك ن د، ش ه د، ح ب ب، خ ي ر، ش د د، ع ل م، ب ع ث ر، ق ب ر، ح ص ل، ص د ر، خ ب ر`.

Lexical seed count: 190 occurrence × branch seeds. This is 173 root branches across distinct roots, plus the second occurrence of `ر ب ب` at 100:11:2, which receives its own 17 branch seed turns.

Evidence labels:

- `E`: generating or expanding before freeze.
- `C`: corroborating after freeze.
- `K`: constraining, narrowing, or defeating after freeze.

Unless a seed row names selected branches, its seed image terminated after the global sweep: the other S100 dossiers and permitted structural features supplied no passage-local role that transformed or completed it.

## Sacred Arabic sequence used

Opening context: `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`

1. `وَٱلْعَٰدِيَٰتِ ضَبْحًا`
2. `فَٱلْمُورِيَٰتِ قَدْحًا`
3. `فَٱلْمُغِيرَٰتِ صُبْحًا`
4. `فَأَثَرْنَ بِهِۦ نَقْعًا`
5. `فَوَسَطْنَ بِهِۦ جَمْعًا`
6. `إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌ`
7. `وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌ`
8. `وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ`
9. `أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ`
10. `وَحُصِّلَ مَا فِى ٱلصُّدُورِ`
11. `إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍ لَّخَبِيرٌ`

## Detailed synthesis units that survived freeze

### F1 — Ordered kinetic incursion into a gathered center

Seed occurrences that independently regenerate the model: `100:1:1 ع د و B002`, `100:1:2 ض ب ح B001/B002`, `100:2:1 و ر ي B002`, `100:2:2 ق د ح B001`, `100:3:2 ص ب ح B001/B004`, `100:4:1 ث و ر B001/B002`, `100:4:3 ن ق ع B004`, `100:5:1 و س ط B002/B003`, `100:5:3 ج م ع B001/B002/B010`.

Initial image: rapid forward motion begins audibly, intensifies into ignition-by-striking, appears at morning, throws up particulate matter, and enters the middle of a gathered mass.

Roots visited: all global S100 dossiers.  
Selected expanding branches: `(E: ع د و B002 العَدْو والحَضْر)`, `(E: ض ب ح B001 صوت الضباح)`, `(E: ض ب ح B002 عدو ممدود الضبعين)`, `(E: و ر ي B002 نار كامنة تخرج من الزند)`, `(E: ق د ح B001 إيراء النار بالقدح)`, `(E: ص ب ح B001 الصبح وأول النهار)`, `(E: ص ب ح B004 يوم الصباح)`, `(E: ث و ر B001 انبعاث الشيء وانتشاره ظاهرا)`, `(E: ث و ر B002 إثارة الشيء وتحريكه من موضعه)`, `(E: ن ق ع B004 نقع الغبار المثار)`, `(E: و س ط B002 موضع الوسط بين الأطراف)`, `(E: و س ط B003 الدخول أو الجعل في الوسط)`, `(E: ج م ع B001 ضم المتفرق)`, `(E: ج م ع B002 جماعة اجتمعت)`, `(E: ج م ع B010 استجماع القوة أو السير)`.

Frozen model: a sequential force-system: running/panting agents → struck ignition → dawn onset → stirred dust → entry into the middle of a gathered body.

Predictions at freeze: continued same-agent sequence; manner nouns and time/object attachments should support the steps; later material may reactivate center-entry, disturbance, and disclosure.

Unused features tested after freeze:

- QAC morphology: first three rooted words are feminine plural active participial nouns, with `و/ف` sequence.
- Attachment rows: `ضبحا` manner of `العاديات`; `قدحا` manner of `الموريات`; `صبحا` time of `المغيرات`; `نقعا` object of `أثرن`; `جمعا` object entered by `وسطن`.
- Repeated `بِهِ` in 100:4–5.
- Later `فِي القبور / فِي الصدور` containment and passive disclosure.

Corroborators: `(C: morphology FP active participles in 100:1–3)`, `(C: sequence وَ → فَ → فَ → فَ → فَ)`, `(C: attachment 100:1 ضبحا circumstantial)`, `(C: attachment 100:2 قدحا circumstantial)`, `(C: attachment 100:3 صبحا adverbial)`, `(C: attachment 100:4 نقعا direct object)`, `(C: attachment 100:5 جمعا direct object)`, `(C: repeated بِهِ in 100:4–5)`.

Constraints: `(K: غ ي ر dossier does not by itself supply a clean uncontaminated “raid” branch; the local role of 100:3 is supported by Form-IV active-participle sequencing and the attachment row, not by importing an unstated lexical scene)`. `(K: no explicit horse noun occurs in the sacred Arabic; horse-language is branch imagery from عدو/ضبح/صبح and remains secondary simulation)`.

Rival forks: `ع د و B001` moral overstepping moves toward F4 rather than the kinetic chain; `و ر ي B005` hiding moves toward F2/F3 rather than physical ignition.

Final grade: strong. The model explains the ordered activation of the first five ayahs, the role of manner/time/object expressions, repeated agent morphology, and the closure of the kinetic sequence at `جمعا`.

### F2 — Hidden ignition becomes later exposure

Seed occurrences that regenerate the model: `و ر ي B002/B005`, `ق د ح B001`, `ث و ر B001/B002`, `ن ق ع B004`, `ب ع ث ر B001`, `ح ص ل B001/B002`, `خ ب ر B001`.

Initial image: something latent is struck or stirred until it becomes manifest; the early spark/dust scene later reappears as burial and chest contents being exposed and known.

Roots visited: all global S100 dossiers.  
Selected expanding branches: `(E: و ر ي B002 نار كامنة تخرج من الزند)`, `(E: و ر ي B005 ستر الشيء وجعله وراء الظهور)`, `(E: ق د ح B001 إيراء النار بالقدح)`, `(E: ث و ر B001 انبعاث الشيء وانتشاره ظاهرا)`, `(E: ث و ر B002 إثارة الشيء وتحريكه من موضعه)`, `(E: ن ق ع B004 نقع الغبار المثار)`, `(E: ب ع ث ر B001 قلب التراب وكشف المدفون)`, `(E: ح ص ل B001 جمع الشيء حتى يظهر حاصله)`, `(E: ح ص ل B002 استخراج اللب أو النفيس من غلافه)`, `(E: خ ب ر B001 العلم بالخبر وباطن الأمر)`.

Frozen model: impact or stirring brings a concealed interior into outward visibility: hidden fire from a source, hidden dust from ground, hidden contents from graves and chests, hidden inner affair under expertise.

Predictions at freeze: later grammar should contain enclosure, concealment, passive exposure, or knowledge of interior contents.

Unused features tested after freeze: `ما في القبور`, `ما في الصدور`, passive `بُعْثِرَ/حُصِّلَ`, `يعلم`, `خبير`, and the early repeated `فَ` chain.

Corroborators: `(C: construction ما فِي القبور)`, `(C: construction ما فِي الصدور)`, `(C: passive morphology in بُعْثِرَ and حُصِّلَ)`, `(C: ع ل م B001 انكشاف الشيء للعارف)`, `(C: خ ب ر B001 باطن الأمر)`.

Constraints: `(K: the final disclosure is not literally fire; و ر ي/قدح form a secondary activation geometry, while بعثر/حصل supply the actual later operations)`.

Rival forks: `و ر ي B001` disease of the hollow reaches only weak chest resonance; `ح ب ب B011` weak useless sparks constrains rather than strengthens the main spark model.

Final grade: medium-strong. The model has strong backward reactivation from ayahs 9–11 into ayahs 2–4, but the fire element remains secondary rather than primary contextual meaning.

### F3 — Dual container disclosure: graves and chests

Seed occurrences/constructions: construction `ما فِي القبور / ما فِي الصدور`; lexical seeds `ب ع ث ر B001`, `ق ب ر B001/B002`, `ح ص ل B001/B002`, `ص د ر B001/B004`, `خ ب ر B001`, `ع ل م B001`.

Initial image: enclosed contents are first located, then overturned or extracted, then placed under complete knowledge.

Roots visited: all global S100 dossiers.  
Selected expanding branches: `(E: ب ع ث ر B001 قلب التراب وكشف المدفون)`, `(E: ق ب ر B001 مواراة الميت في القبر)`, `(E: ق ب ر B002 غموض الشيء وتطامنه)`, `(E: ح ص ل B001 جمع الشيء حتى يظهر حاصله)`, `(E: ح ص ل B002 استخراج اللب أو النفيس من غلافه)`, `(E: ص د ر B001 الصدر الجارحة وما يتصل بها)`, `(E: ص د ر B004 الأصل الذي تصدر عنه الأفعال)`, `(E: خ ب ر B001 العلم بالخبر وباطن الأمر)`, `(E: ع ل م B001 انكشاف الشيء للعارف)`.

Frozen model: two levels of containment are opened in order: external burial container, then internal chest/source container, then expert knowledge closes the scene.

Predictions at freeze: parallel syntax, passive operations on hidden contents, and a final knower should appear.

Unused features tested after freeze: early `أثرن نقعا` dust, `وسطن جمعا` entry into a collective middle, `ربهم بهم` in 100:11, and temporal `إذا/يومئذ`.

Corroborators: `(C: repeated construction ما فِي X)`, `(C: passive morphology in 100:9–10)`, `(C: attachment 100:9 فِي القبور completes ما)`, `(C: attachment 100:10 فِي الصدور completes ما)`, `(C: temporal إذا → يومئذ)`, `(C: ربهم بهم in 100:11 closes the disclosure on the same human set)`.

Constraints: `(K: ق ب ر B001 is a burial-place branch, not a metaphor for chest; the two containers remain distinct and parallel, not collapsed)`.

Rival forks: `ق ب ر B003/B004` terminate; `ص د ر B002` front/top supports spatial ordering but not the core container disclosure.

Final grade: strong. This is the clearest passage-scale reactivation: later grammar explicitly supplies containment, hidden contents, exposure, extraction, and final knowing.

### F4 — Human relational breach under the Rabb

Seed occurrences that regenerate the model: `100:6:2 ء ن س B001`, `100:6:3 ر ب ب B001/B002/B011`, `100:6:4 ك ن د B001/B002`, `100:7:4 ش ه د B001/B002`, `100:8:2 ح ب ب B002`, `100:8:3 خ ي ر B001/B005`, `100:8:4 ش د د B002/B006`, plus `100:11:2 ر ب ب B001/B002` as closure.

Initial image: a human relation to a master/caretaker is marked by cutting or ingratitude, then self-witnessing, then intense attachment to desired good.

Roots visited: all global S100 dossiers.  
Selected expanding branches: `(E: ء ن س B001 ظهور الإنسان المخالف للتوحش والجن)`, `(E: ر ب ب B001 ربوبية وملك وسيادة)`, `(E: ر ب ب B002 إصلاح وتربية وإتمام)`, `(E: ر ب ب B011 ربابة عهد وميثاق)`, `(E: ك ن د B001 القطع والانفصال)`, `(E: ك ن د B002 كفران النعمة والمودة)`, `(E: ش ه د B001 الحضور مع المشاهدة)`, `(E: ش ه د B002 البيان بعلم)`, `(E: ح ب ب B002 المحبة الملازمة للقلب)`, `(E: خ ي ر B001 الميل إلى الخير النافع)`, `(E: خ ي ر B005 الكرم والهبة)`, `(E: ش د د B002 شدة القوة والصلابة)`, `(E: ش د د B006 شدة البخل)`.

Frozen model: human is positioned under `ربه`; the relation that should imply ownership, care, nurture, or covenant is answered by cutting/ingratitude; the same human is witness to that and tightly attached to desired good.

Predictions at freeze: the passage should later expose inner motives and return to the Rabb relation.

Unused features tested after freeze: `ما في الصدور`, `حصل`, `ربهم`, `بهم`, `خبير`, and the singular-to-plural movement.

Corroborators: `(C: attachment 100:6 لربه specifies the target with respect to which كنود is predicated)`, `(C: attachment 100:7 على ذلك gives the matter over which شهيد applies)`, `(C: attachment 100:8 لحب relates شدّ to حب)`, `(C: attachment 100:8 الخير is idafa complement of حب)`, `(C: ص د ر B001 chest as inner site)`, `(C: ح ص ل B002 extraction from covering)`, `(C: خ ب ر B001 knowledge of inner affair)`, `(C: repeated ر ب ب at 100:11 reactivates 100:6)`.

Constraints: `(K: the early feminine plural oath agents are not grammatically the later الإنسان; the model may compare activation patterns but cannot identify them as the same subject)`. `(K: خ ي ر remains “good/benefit/gift” from furuq; no external specification such as wealth is added)`.

Rival forks: `ك ن د B003` barren-earth imagery offers a weak rival deprivation model; `ر ب ب B006/B008/B013` move into food/cloud/water imagery and do not carry the moral relation.

Final grade: strong. The middle assertion and final closure form a tight relational model, and later chest-disclosure strongly corroborates the predicted inner locus.

### F5 — Cutting, scattering, gathering, and result

Seed occurrences that regenerate the model: `ك ن د B001`, `ج م ع B001/B002/B009/B010`, `و س ط B003`, `ب ع ث ر B002/B003`, `ح ص ل B001/B003`, `ش د د B001`.

Initial image: the passage repeatedly arranges parts: a gathering is penetrated, a relation is cut, buried contents are scattered or overturned, and a final result is collected.

Roots visited: all global S100 dossiers.  
Selected expanding branches: `(E: ك ن د B001 القطع والانفصال)`, `(E: ج م ع B001 ضم المتفرق)`, `(E: ج م ع B002 جماعة اجتمعت)`, `(E: ج م ع B009 اكتمال الشيء كله بلا تفرق أو نقص)`, `(E: ج م ع B010 استجماع القوة أو السير)`, `(E: و س ط B003 الدخول أو الجعل في الوسط)`, `(E: ب ع ث ر B002 تبديد المتاع وقلب بعضه على بعض)`, `(E: ب ع ث ر B003 هدم الحوض وقلب أسفله أعلاه)`, `(E: ح ص ل B001 جمع الشيء حتى يظهر حاصله)`, `(E: ح ص ل B003 البقية والحثالة بعد الرفع أو الفصل)`, `(E: ش د د B001 شد العقد والوثاق)`.

Frozen model: forms of collection and disruption alternate: gathered center → cut relation → overturned hidden material → collected result.

Predictions at freeze: syntax should mark objects entered or exposed, and the end should produce a settled remainder or result.

Unused features tested after freeze: `جمعا` direct object, passive `ما`, `حصل`, `خبير`, and the emphatic predications.

Corroborators: `(C: attachment 100:5 جمعا direct object entered by وسطن)`, `(C: passive subject ما in 100:9 and 100:10)`, `(C: ح ص ل B001 result after separation)`, `(C: خ ب ر B001 final knowledge of what remains true)`.

Constraints: `(K: ك ن د B001 physical cutting is not the contextual predicate alone; ك ن د B002 ingratitude is needed for the middle assertion)`.

Rival forks: `ج م ع B008` shackles and `قدح B007` arrows form a weak object-system but lack local grammatical support.

Final grade: medium-strong. The structural alternation is real, but it is more abstract than F1/F3/F4.

### F6 — Witness, knowledge, sign, and expert closure

Seed occurrences that regenerate the model: `ش ه د B001/B002/B005/B008`, `ع ل م B001/B002`, `ح ص ل B001`, `ص د ر B004`, `خ ب ر B001`.

Initial image: knowledge is not merely stated; evidence is present, witnessed, marked, extracted, and finally known in its interior.

Roots visited: all global S100 dossiers.  
Selected expanding branches: `(E: ش ه د B001 الحضور مع المشاهدة)`, `(E: ش ه د B002 البيان بعلم)`, `(E: ش ه د B005 اللسان الشاهد)`, `(E: ش ه د B008 العلامة الشاهدة)`, `(E: ع ل م B001 انكشاف الشيء للعارف)`, `(E: ع ل م B002 أثر يميز الشيء ويهدي إليه)`, `(E: ح ص ل B001 جمع الشيء حتى يظهر حاصله)`, `(E: ص د ر B004 الأصل الذي تصدر عنه الأفعال)`, `(E: خ ب ر B001 العلم بالخبر وباطن الأمر)`.

Frozen model: the passage moves from self-witness over a known matter to exposure of hidden sources and final expert knowledge.

Predictions at freeze: there should be a specified matter of witness, a knowledge question, hidden evidence becoming available, and a final knowing subject.

Unused features tested after freeze: `على ذلك`, interrogative `أفلا`, `يعلم`, `ما في الصدور`, `ربهم بهم`, and emphatic `لـ`.

Corroborators: `(C: attachment 100:7 على ذلك gives the matter over which شهيد applies)`, `(C: ع ل م B001 at 100:9)`, `(C: ص د ر B001/B004 inner source)`, `(C: خ ب ر B001 at 100:11)`, `(C: emphatic لَ in شهيد/شديد/خبير)`.

Constraints: `(K: شهيد is not the final خبير; the model requires sequence from human witness to Rabb expertise rather than treating them as identical roles)`.

Rival forks: `ع ل م B002` sign/mark can over-focus on external signs; F6 is strongest when B002 is subordinate to B001/B001-style knowledge.

Final grade: medium-strong. It explains the second half well and retrospectively organizes the middle assertion.

### F7 — Inner love as tightened binding

Seed occurrences that regenerate the model: `ح ب ب B002/B004`, `ش د د B001/B002/B006`, `خ ي ر B001/B002/B003/B005`, `ص د ر B001`, `ح ص ل B002`.

Initial image: an inner beloved good is tightened into a strong attachment; the final chest-extraction tests what was bound inside.

Roots visited: all global S100 dossiers.  
Selected expanding branches: `(E: ح ب ب B002 المحبة الملازمة للقلب)`, `(E: ح ب ب B004 حبة القلب سويداؤه)`, `(E: ش د د B001 شد العقد والوثاق)`, `(E: ش د د B002 شدة القوة والصلابة)`, `(E: ش د د B006 شدة البخل)`, `(E: خ ي ر B001 الميل إلى الخير النافع)`, `(E: خ ي ر B002 فضل الصلاح والاصطفاء)`, `(E: خ ي ر B003 طلب الخير بالاختيار)`, `(E: خ ي ر B005 الكرم والهبة)`, `(E: ص د ر B001 الصدر الجارحة)`, `(E: ح ص ل B002 استخراج اللب أو النفيس من غلافه)`.

Frozen model: the love of `الخير` is an inner binding or intense orientation whose contents will be drawn out from the chest.

Predictions at freeze: syntax should attach intensity to love, love to good, and later disclosure to inner storage.

Unused features tested after freeze: `لحب الخير`, `لشديد`, `ما في الصدور`, `حصل`, `خبير`.

Corroborators: `(C: attachment 100:8 لحب relates the intensity in شديد to حب)`, `(C: attachment 100:8 الخير idafa complement of حب)`, `(C: ص د ر B001 inner chest)`, `(C: ح ص ل B002 extraction of inner kernel)`, `(C: خ ب ر B001 knowledge of interior)`.

Constraints: `(K: خير is not narrowed beyond furuq’s good/benefit/gift range)`. `(K: ح ب ب B004 heart-core is a branch support, not a claim that the surface word means heart-core in context)`.

Rival forks: `ح ب ب B001/B006` seed/water imagery moves toward F11 and does not strengthen F7.

Final grade: medium. The local syntax is strong, but the image is narrower than the whole passage.

### F8 — Dawn-to-disclosure visibility

Seed occurrences that regenerate the model: `ص ب ح B001/B004/B005/B010`, `ع ل م B001/B002`, `ث و ر B001`, `ن ق ع B004`, `خ ب ر B001`.

Initial image: morning is the first visibility threshold; what begins at dawn later becomes full disclosure and knowledge.

Roots visited: all global S100 dossiers.  
Selected expanding branches: `(E: ص ب ح B001 الصبح وأول النهار)`, `(E: ص ب ح B004 يوم الصباح)`, `(E: ص ب ح B005 المصباح والسراج)`, `(E: ص ب ح B010 أصبح بمعنى صار)`, `(E: ع ل م B001 انكشاف الشيء للعارف)`, `(E: ع ل م B002 أثر يميز الشيء)`, `(E: ث و ر B001 انبعاث الشيء وانتشاره ظاهرا)`, `(E: ن ق ع B004 الغبار المثار)`, `(E: خ ب ر B001 باطن الأمر)`.

Frozen model: the passage begins with an event at the threshold of day and ends with the hidden becoming knowable.

Predictions at freeze: visibility should intensify from partial scene-setting to explicit knowledge.

Unused features tested after freeze: `يعلم`, `بعثر`, `حصل`, `خبير`, `يومئذ`.

Corroborators: `(C: attachment 100:3 صبحا adverbial)`, `(C: ع ل م B001)`, `(C: خ ب ر B001)`, `(C: temporal يومئذ)`.

Constraints: `(K: only one explicit dawn word occurs; full disclosure relies on later knowledge/exposure roots, not on صبح alone)`.

Rival forks: `ص ب ح B003/B007/B008` food/sleep/camel branches terminate.

Final grade: medium. It captures a plausible temporal visibility arc, with limited lexical spread.

### F9 — From side/boundary to middle

Seed occurrences that regenerate the model: `ع د و B004/B009/B010`, `و ر ي B006`, `و س ط B002/B003`, `ج م ع B001/B002`, `ص د ر B002`.

Initial image: a boundary or side is crossed, then the motion enters the middle/front of a gathered body.

Roots visited: all global S100 dossiers.  
Selected expanding branches: `(E: ع د و B004 المجاوزة والاستثناء والصرف)`, `(E: ع د و B009 العَداء والعُدوة في الجانب والطوار)`, `(E: ع د و B010 العدواء في صلابة المكان واضطرابه)`, `(E: و ر ي B006 الجانب الوراء)`, `(E: و س ط B002 موضع الوسط بين الأطراف)`, `(E: و س ط B003 الدخول أو الجعل في الوسط)`, `(E: ج م ع B001 ضم المتفرق)`, `(E: ج م ع B002 جماعة اجتمعت)`, `(E: ص د ر B002 المقدّم والأعلى والأول)`.

Frozen model: the early motion has spatial grammar: edge or unstable surface → crossing → center → front/first region.

Predictions at freeze: the passage should mark an object or mass whose middle is entered.

Unused features tested after freeze: `جمعا` object, `فوسطن`, early `بِهِ`, later `في` containers.

Corroborators: `(C: attachment 100:5 جمعا direct object entered by وسطن)`, `(C: و س ط B003 exactly supplies entry into middle)`, `(C: repeated فَ sequence directs movement forward)`.

Constraints: `(K: ع د و side/edge branches do not by themselves explain the moral middle section or final disclosure)`.

Rival forks: `ع د و B001` becomes F4; `ع د و B002` becomes F1.

Final grade: medium. Strong for the local spatial sequence, weaker as a whole-passage model.

### F10 — Audible trace and raised voice

Seed occurrences that regenerate the model: `ض ب ح B001`, `ن ق ع B005`, `ش ه د B005`, with weak support from `ع ل م B002`.

Initial image: the passage begins with sound, can raise sound/dust, and then turns into testimony or expression.

Roots visited: all global S100 dossiers.  
Selected expanding branches: `(E: ض ب ح B001 صوت الضباح)`, `(E: ن ق ع B005 نقع الصوت المرتفع)`, `(E: ش ه د B005 اللسان الشاهد)`, `(E: ع ل م B002 أثر يميز الشيء)`.

Frozen model: audible or expressive traces move from panting/noise to speech-like witness.

Predictions at freeze: later passage should supply explicit tongue, speech, or voice.

Unused features tested after freeze: `شهيد`, `يعلم`, `خبير`, but no explicit speech verb or tongue word.

Corroborators: `(C: ش ه د B005 can make witness linguistically expressive)`.

Constraints: `(K: no explicit speech/tongue construction occurs; ن ق ع B005 is a secondary branch competing with the stronger dust branch B004)`.

Rival forks: F1 absorbs `ضبح` more strongly as kinetic/manner evidence.

Final grade: weak. It is a real local branch resonance but lacks enough syntactic role completion.

### F11 — Water, seed, nurture, and soft-earth rival

Seed occurrences that try this model: `ن ق ع B001/B002/B007`, `ح ب ب B001/B006/B007/B008`, `خ ب ر B002/B003/B005`, `ر ب ب B002/B008/B012/B013`, `ع ل م B005`, `خ ي ر B005`.

Initial image: soaking water, seed/grain, soft ground, nurture, and beneficial gift could form a growth/agriculture scene.

Roots visited: all global S100 dossiers.  
Selected branches before rejection: `(E: ن ق ع B001 استقرار الماء وما ينقع فيه)`, `(E: ن ق ع B002 ماء ينقع الغلة ويروي)`, `(E: ح ب ب B001 الحبة التي تنبت وتحمل الحب)`, `(E: ر ب ب B002 إصلاح وتربية وإتمام)`, `(E: خ ب ر B002 لين الأرض ومائها)`, `(E: خ ب ر B003 إصلاح الأرض بالمخابرة)`, `(E: خ ي ر B005 الكرم والهبة)`.

Frozen model: a rival nurturing field in which water, seed, soft land, and care produce benefit.

Predictions at freeze: the passage should contain planting, watering, land cultivation, or explicit growth roles.

Unused features tested after freeze: the actual S100 sequence instead supplies running, sparks, dust, gathering, human ingratitude, graves, chests, and knowledge.

Corroborators: only `(C: ر ب ب B002 repair/nurture)` and `(C: خ ي ر B005 gift)` weakly touch F4’s benefaction contrast.

Constraints: `(K: no planting/watering/cultivation construction appears)`, `(K: ن قع in 100:4 is directly better fit by B004 raised dust)`, `(K: حب in 100:8 is syntactically love, not seed)`.

Rival forks: F4 uses nurture morally; F1 uses dust physically.

Final grade: unlikely to weak. It is useful mainly as a rejected rival proving that water/seed branches should not be blended into the passage just because several roots permit them.

### F12 — Lot/shaft/container rival

Seed occurrences that try this model: `ق د ح B007`, `ر ب ب B010`, `ج م ع B003/B013`, `ش د د B001`.

Initial image: shafts or lots are gathered in a container, bound by a decision or compact.

Roots visited: all global S100 dossiers.  
Selected branches before rejection: `(E: ق د ح B007 عود السهم والقدح في الميسر)`, `(E: ر ب ب B010 ربابة تجمع القداح)`, `(E: ج م ع B003 عزم محكم)`, `(E: ج م ع B013 ممالأة واجتماع مع غيرك على أمر)`, `(E: ش د د B001 شد العقد والوثاق)`.

Frozen model: a decision/lot mechanism with gathered shafts.

Predictions at freeze: the passage should contain explicit lots, arrows, gaming, decision by drawing, or a container role.

Unused features tested after freeze: no such roles appear; `قدحا` is better captured by fire-striking in F1/F2.

Corroborators: none strong.

Constraints: `(K: no maysir/lot/arrow construction)`, `(K: قدحا attaches as a manner expression to الموريات and is better explained by ق د ح B001)`.

Final grade: unlikely. It is a branch intersection but not a passage-local synthesis.

## Lexical seed audit, in passage order

Each row records the seed occurrence and branch, the image it initially forms, its selected expansion if any, unused features tested after freeze, and grade. “Terminates” means the seed was given a full cross-root sweep but no passage-local model survived.

### 100:1:1 `وَٱلْعَٰدِيَٰتِ` — root `ع د و`

- `B001 مجاوزة الحد والظلم` — initial image of overstepping. Selected: F4 with `(E: ك ن د B002)`, `(E: ر ب ب B001)`. Tested: early oath-agent grammar. Grade: medium; it explains moral breach but not the kinetic order.
- `B002 العَدْو والحَضْر` — initial image of running. Selected: F1. Tested: manner/time/object attachments and fā-sequence. Grade: strong.
- `B003 العَدُوّ والعداوة` — hostility seed. Selected weakly into F4 via relational opposition. Tested: no explicit enemy role. Grade: weak.
- `B004 المجاوزة والاستثناء والصرف` — crossing/beyond seed. Selected: F9. Tested: `وسطن جمعا`. Grade: medium.
- `B005 العَدْوى في طلب الإنصاف` — plea for vindication. No selected E; no judge/claim/legal petition role. Grade: unlikely.
- `B006 العَدْوى في انتقال الداء` — contagion. No selected E; no disease-transfer construction. Grade: unlikely.
- `B007 العَوادي والعادية الشاغلة` — distracting calamities. Possible loose pressure on human condition, but no specific role. Grade: weak.
- `B008 العِداء في تعاقب الصيد` — successive hunting. Weakly resembles fā-sequence, but no hunting/prey construction. Grade: weak.
- `B009 العَداء والعُدوة في الجانب والطوار` — side/bank seed. Selected: F9 with `(E: و س ط B002/B003)`. Grade: medium.
- `B010 العَدْواء في صلابة المكان واضطرابه` — hard/uneven ground. Weak support for force crossing terrain; no direct later role. Grade: weak.
- `B011 العَدَوِيّة من نبات الصيف` — summer plant. Only F11 rival; rejected by no growth syntax. Grade: unlikely.
- `B012 العَنْدَأْوَة في الالتواء والعسر` — twisting/difficulty. No selected E. Grade: unlikely.

### 100:1:2 `ضَبْحًا` — root `ض ب ح`

- `B001 صوت الضباح` — audible breath/sound. Selected: F1 and F10. Grade: strong for F1 local, weak as F10 whole-passage.
- `B002 عدو ممدود الضبعين` — running with extended forelegs. Selected: F1 with `(E: ع د و B002)`. Grade: strong.
- `B003 إحراق أعالي العود` — burning tips. Selected: F2 with `(E: و ر ي B002)`, `(E: ق د ح B001)`. Grade: medium.
- `B004 تغير اللون إلى السواد` — darkening by fire/sun. Weak fire afterimage; no color role. Grade: weak.
- `B005 الرماد` — ash. Weak dust/fire rival to `نقع`; no ash word. Grade: weak.

### 100:2:1 `فَٱلْمُورِيَٰتِ` — root `و ر ي`

- `B001 داء يأكل الجوف أو يصيب الرئة` — hollow/lung disease. Weak chest resonance with `صدور`; no sickness predicate. Grade: weak.
- `B002 نار كامنة تخرج من الزند` — hidden fire emerging. Selected: F1/F2. Grade: strong locally, medium-strong passage-wide.
- `B003 زند يقدح نجاحا أو نصرة` — successful/helping flint. No aid/success role. Grade: unlikely.
- `B004 شحم وار وسمن ظاهر` — fat/sleekness. No selected E. Grade: unlikely.
- `B005 ستر الشيء وجعله وراء الظهور` — hiding behind. Selected: F2/F3 with later hidden contents. Grade: medium-strong.
- `B006 الجانب الوراء` — behind/other side. Selected: F9 weakly as side-to-middle geometry. Grade: medium.
- `B007 ولد الولد يأتي من وراء الابن` — descendant. No lineage construction. Grade: unlikely.
- `B008 الورى: الخلق على ظهر الأرض` — creatures on earth. Loose human/creation echo; no specific role. Grade: weak.

### 100:2:2 `قَدْحًا` — root `ق د ح`

- `B001 إيراء النار بالقدح` — striking fire. Selected: F1/F2. Grade: strong.
- `B002 نقر الشيء وعيبه` — notch/defect. Weak moral blemish with `كنود`; no local notch role. Grade: weak.
- `B003 طعن في النسب` — slander in lineage. No lineage/slander role. Grade: unlikely.
- `B004 أكال الشجر والسن` — worm/decay in wood or tooth. No selected E. Grade: unlikely.
- `B005 غرف ما في القدر` — ladling pot contents. Weak extraction analogy but no vessel/ladle. Grade: unlikely.
- `B006 قدح الشرب` — drinking vessel. No selected E. Grade: unlikely.
- `B007 عود السهم والقدح في الميسر` — shaft/lot. Selected only as rejected F12. Grade: unlikely.
- `B008 ضمر الفرس وغؤور العين` — lean horse/sunken eye. Weak animal branch; no eye/leanness role. Grade: weak.
- `B009 رخص أطراف النبت` — tender plant tips. Only rejected F11. Grade: unlikely.
- `B010 اقتداح الأمر بالنظر والتدبير` — deliberating a matter. Weak with `يعلم`; no planning role. Grade: weak.

### 100:3:1 `فَٱلْمُغِيرَٰتِ` — root `غ ي ر`

- `B001 الصلاح والمنفعة بالميرة والسقي والإصلاح` — supply/repair. Weak moral-benefit rival with F4/F11. Grade: weak.
- `B002 الغَيْر في الدية` — blood-money substitute. No compensation role. Grade: unlikely.
- `B003 تغيير الصورة أو إبدال الشيء بغيره` — alteration/change. Selected: F2/F8 as state-change. Grade: medium.
- `B004 الغَيْرة على الأهل` — jealousy. Weak with love/intensity, but no family-jealousy role. Grade: weak.
- `B005 السوى والخلاف والاستثناء والنفي` — otherness/exception/negation. Weak transition support only. Grade: weak.

### 100:3:2 `صُبْحًا` — root `ص ب ح`

- `B001 الصبح وأول النهار` — dawn. Selected: F1/F8. Grade: strong locally.
- `B002 الإتيان صباحا` — coming in morning. Selected: F8 weakly and F1 locally. Grade: medium.
- `B003 الصبوح` — morning drink/food. Only rejected F11. Grade: unlikely.
- `B004 يوم الصباح` — morning raid/call. Selected: F1 with constraint against importing unmarked details. Grade: strong locally.
- `B005 المصباح والسراج` — lamp. Selected: F8 as visibility support. Grade: medium.
- `B006 الصُّبْحة والصباحة` — redness/beauty. No color/beauty role. Grade: weak.
- `B007 الصُّبْحة نوما` — morning sleep. No sleep role. Grade: unlikely.
- `B008 الناقة المصباح` — camel that stays until morning. No selected E. Grade: unlikely.
- `B009 ظروف الصباح` — morning instances. Weak temporal support only. Grade: weak.
- `B010 أصبح بمعنى صار` — becoming. Selected weakly into F8 state-transition. Grade: medium-weak.

### 100:4:1 `فَأَثَرْنَ` — root `ث و ر`

- `B001 انبعاث الشيء وانتشاره ظاهرا` — outbreak/spread into visibility. Selected: F1/F2/F8. Grade: strong.
- `B002 إثارة الشيء وتحريكه من موضعه` — stirring/moving from place. Selected: F1/F2. Grade: strong.
- `B003 هيجان إلى مواجهة أو غضب` — agitation/confrontation. Weak with charge/intensity; no anger predicate. Grade: weak.
- `B004 الثور: ذكر البقر` — bull. No selected E. Grade: unlikely.
- `B005 ثورة الأقط: قطعة جامدة` — curd piece. No selected E. Grade: unlikely.
- `B006 ثور اسما لمكان أو قوم أو برج` — place/people/constellation. No selected E. Grade: unlikely.
- `B007 ثور الماء: طحلب يعلو السطح` — algae on water. Only rejected F11. Grade: unlikely.

### 100:4:3 `نَقْعًا` — root `ن ق ع`

- `B001 استقرار الماء وما ينقع فيه` — settled/soaking water. Rejected F11 rival. Grade: weak.
- `B002 ماء ينقع الغلة ويروي` — water that quenches. Rejected F11 rival. Grade: weak.
- `B003 نقيعة طعام أو نحر أو لبن` — food/slaughter/milk. No selected E. Grade: unlikely.
- `B004 نقع الغبار المثار` — raised dust. Selected: F1/F2/F8. Grade: strong.
- `B005 نقع الصوت المرتفع` — raised sound. Selected: F10 only. Grade: weak.
- `B006 سم ناقع ثابت أو قاتل` — fixed/deadly venom. No poison/death-agent construction beyond graves, not enough. Grade: unlikely.
- `B007 نقاع الأرض القيعان السهلة` — easy earth basins. Rejected F11; weak earth resonance. Grade: weak.
- `B008 شراب بأنقع مجرب للموارد` — experienced in watering places. Weak with `خبير`; no proverb role. Grade: unlikely.
- `B009 نقعه بالشتم القبيح` — ugly insult. No insult/speech role. Grade: unlikely.

### 100:5:1 `فَوَسَطْنَ` — root `و س ط`

- `B001 العدل والخيار في موضع الوسط` — just/excellent middle. Weak moral resonance with F4; local verb prefers entry. Grade: medium-weak.
- `B002 موضع الوسط بين الأطراف` — middle place. Selected: F1/F9. Grade: strong locally.
- `B003 الدخول أو الجعل في الوسط` — entering or making middle. Selected: F1/F9. Grade: strong.
- `B004 مرتبة وسطى بين الجيد والرديء` — intermediate quality. Weak with `خير/كنود`; no grading construction. Grade: weak.
- `B005 الوساطة بين الناس` — mediation. No mediation role. Grade: unlikely.
- `B006 قطع الشيء نصفين` — cutting in halves. Weak F5 support. Grade: weak.
- `B007 الوسوط: بيت أو ناقة مخصوصة` — special tent/camel. No selected E. Grade: unlikely.

### 100:5:3 `جَمْعًا` — root `ج م ع`

- `B001 ضم المتفرق حتى يصير شيئا مجموعا` — joining the scattered. Selected: F1/F5/F3. Grade: strong.
- `B002 جماعة اجتمعت أو أخلاط ضمتها الجهة` — gathered group/army. Selected: F1/F9. Grade: strong.
- `B003 عزم محكم جمع الرأي` — firm resolve. Selected only weakly in rejected F12. Grade: weak.
- `B004 موضع أو يوم أو نداء يجمع الناس` — gathering place/day/call. Weak final-day resonance; no explicit call/place except `يومئذ`. Grade: medium-weak.
- `B005 قبضة الكف` — fist. No selected E. Grade: unlikely.
- `B006 اتصال الجماع` — intercourse. No selected E. Grade: unlikely.
- `B007 حال المرأة أو الأنثى التي بقي حملها أو عذرها معها` — pregnancy/virgin state. No selected E. Grade: unlikely.
- `B008 القيد الذي يجمع اليدين إلى العنق` — shackle. Weak with `شدد B001`; no shackle role. Grade: weak.
- `B009 اكتمال الشيء كله بلا تفرق أو نقص` — completeness. Selected: F5/F3 as result-wholeness. Grade: medium.
- `B010 استجماع القوة أو السير` — gathered strength/motion. Selected: F1. Grade: medium-strong.
- `B011 نخل دقل اجتمع من النوى` — date palms from seeds. Rejected F11. Grade: unlikely.
- `B012 عظم الشيء كأنه جامع ممتلئ` — great vessel. No selected E. Grade: unlikely.
- `B013 ممالأة واجتماع مع غيرك على أمر` — siding together on an affair. Weak social alignment; no explicit coalition. Grade: weak.

### 100:6:2 `ٱلْإِنسَٰنَ` — root `ء ن س`

- `B001 ظهور الإنسان المخالف للتوحش والجن` — human being. Selected: F4. Grade: strong.
- `B002 إيناس الشيء برؤية أو إحساس أو سماع` — seeing/sensing/hearing. Selected: F6 weakly as perception. Grade: medium.
- `B003 الأنس الذي يزيل الوحشة` — intimacy removing loneliness. No companionship/comfort role. Grade: weak.
- `B004 الجانب الإنسي المقبل على الإنسان` — human-facing side. Weak F9/F3 side-interiority resonance. Grade: weak.
- `B005 إنسان العين وصورة الإنسان في السواد` — pupil/image in eye. Weak witness/seeing echo; no eye role. Grade: weak.
- `B006 ابن الإنس للنفس والصفوة` — self/close companion. Weak support for inner self in F4. Grade: medium-weak.

### 100:6:3 `لِرَبِّهِۦ` — root `ر ب ب`

- `B001 ربوبية وملك وسيادة` — lordship/mastery. Selected: F4. Grade: strong.
- `B002 إصلاح وتربية وإتمام` — nurture/repair/completion. Selected: F4 and weakly F11. Grade: medium-strong.
- `B003 علم رباني` — rabbinic/learned knowledge. Weak F6 anticipation. Grade: weak.
- `B004 ربة وجماعات كثيرة` — many groups. Weak with `جمع`; no role. Grade: weak.
- `B005 ربيب وربيبة ورابة` — fostered child/caretaker. Weak relation variant, not text-specific. Grade: weak.
- `B006 رُبّ خاثر وإصلاح به` — thick syrup/repair. No selected E. Grade: unlikely.
- `B007 لزوم وإقامة ودوام` — staying/duration. Weak continuity; no local role. Grade: weak.
- `B008 رباب السحاب` — clouds. Rejected F11. Grade: unlikely.
- `B009 شاة رُبّى وحداثة` — ewe/recent birth. No selected E. Grade: unlikely.
- `B010 ربابة تجمع القداح` — container for lots/arrows. Rejected F12. Grade: unlikely.
- `B011 ربابة عهد وميثاق` — covenant/protection. Selected: F4 as relational undertone. Grade: medium.
- `B012 ربة نبات` — plant. Rejected F11. Grade: unlikely.
- `B013 ماء رَبَب كثير` — abundant water. Rejected F11. Grade: unlikely.
- `B014 رَبْرَب قطيع` — herd. Weak animal collective; no role. Grade: unlikely.
- `B015 حرف رب وربما` — particle. No selected E. Grade: unlikely.
- `B016 رُبَى حاجة وعقدة ونعمة` — need/knot/blessing. Weak F4/F7 support. Grade: weak.
- `B017 رباني الملاحين` — sailors’ chief. No selected E. Grade: unlikely.

### 100:6:4 `لَكَنُودٌ` — root `ك ن د`

- `B001 القطع والانفصال` — cutting/separation. Selected: F5 and F4. Grade: medium-strong.
- `B002 كفران النعمة والمودة` — ingratitude. Selected: F4. Grade: strong.
- `B003 الأرض التي لا تنبت` — barren land. Rejected F11; weak moral barrenness. Grade: weak.
- `B004 اسم كندة` — name Kinda. No selected E. Grade: unlikely.

### 100:7:4 `لَشَهِيدٌ` — root `ش ه د`

- `B001 الحضور مع المشاهدة` — presence with witnessing. Selected: F6/F4. Grade: strong.
- `B002 البيان بعلم` — testimony/statement with knowledge. Selected: F6/F4. Grade: strong.
- `B005 اللسان الشاهد` — witnessing tongue/expression. Selected: F10/F6. Grade: medium.
- `B006 الخارج عند الولادة والإدراك` — birth discharge/sign of maturity. No birth/maturity role. Grade: unlikely.
- `B007 الشَّهْد في الشمع` — honey in wax. Rejected F11 by lack of honey/wax. Grade: unlikely.
- `B008 العلامة الشاهدة` — indicating sign. Selected: F6. Grade: medium.

### 100:8:2 `لِحُبِّ` — root `ح ب ب`

- `B001 الحبة التي تنبت وتحمل الحب` — seed/grain. Rejected F11. Grade: weak.
- `B002 المحبة الملازمة للقلب` — love in heart. Selected: F4/F7. Grade: strong.
- `B003 صيغة المدح وغاية الرغبة` — praise/desire formula. Weak F7 support. Grade: weak.
- `B004 حبة القلب سويداؤه` — heart core. Selected: F7 as secondary interior support. Grade: medium-strong.
- `B005 البعير يلزم مكانه من عجز` — camel stuck from exhaustion. No selected E. Grade: unlikely.
- `B006 الري حتى الامتلاء` — fullness from drinking. Rejected F11. Grade: weak.
- `B007 الحب جرة عظيمة أو موضعها` — large jar. Rejected F11. Grade: unlikely.
- `B008 حباب الماء فقاقيعه وطرائقه` — water bubbles/waves. Rejected F11. Grade: unlikely.
- `B009 حبب الأسنان انتظام كالدرر` — arranged teeth. No selected E. Grade: unlikely.
- `B010 الحبحاب الصغير القصير` — small/short. No selected E. Grade: unlikely.
- `B011 نار الحباحب شرر لا ينتفع به` — useless sparks. Weak constraint on F2; not selected as generator. Grade: weak.
- `B012 الحباب الحية أو الشيطان` — snake/devil. No selected E. Grade: unlikely.

### 100:8:3 `ٱلْخَيْرِ` — root `خ ي ر`

- `B001 الميل إلى الخير النافع` — beneficial good. Selected: F4/F7. Grade: strong.
- `B002 فضل الصلاح والاصطفاء` — excellence/choice. Selected: F7. Grade: medium.
- `B003 طلب الخير بالاختيار والاستخارة` — choosing/seeking good. Selected weakly: F7. Grade: weak.
- `B005 الكرم والهبة` — generosity/gift. Selected: F4 as benefaction contrast. Grade: medium.
- `B006 استدراج الحيوان من جحره` — luring animal from burrow. Weak exposure analogy with F3 but no animal/burrow construction. Grade: weak.

### 100:8:4 `لَشَدِيدٌ` — root `ش د د`

- `B001 شد العقد والوثاق` — tying/binding. Selected: F7/F5. Grade: medium.
- `B002 شدة القوة والصلابة` — strength/intensity. Selected: F4/F7. Grade: strong.
- `B003 شد الحملة والعدو` — charge/attack. Weak bridge back to F1. Grade: medium-weak.
- `B004 بلوغ الأشد` — maturity. Weak with knowledge; no maturity role. Grade: weak.
- `B005 شد النهار وارتفاعه` — height of day. Weak F8 temporal echo; no explicit noon/high-day. Grade: weak.
- `B006 شدة البخل` — miserliness. Selected: F4/F7 as possible narrowing of love-of-good intensity. Grade: medium.

### 100:9:2 `يَعْلَمُ` — root `ع ل م`

- `B001 انكشاف الشيء للعارف` — knowledge/disclosure to knower. Selected: F3/F6/F8. Grade: strong.
- `B002 أثر يميز الشيء ويهدي إليه` — sign/mark. Selected: F6/F8. Grade: medium.
- `B004 شق ظاهر في الشفة العليا` — cleft lip. No selected E. Grade: unlikely.
- `B005 ماء كثير مجتمع في عيلم` — much gathered water. Rejected F11. Grade: unlikely.
- `B006 طائر جارح يسمى العلام` — raptor. No selected E. Grade: unlikely.
- `B007 ذكر الضباع يسمى العيلام` — male hyena. No selected E. Grade: unlikely.

### 100:9:4 `بُعْثِرَ` — root `ب ع ث ر`

- `B001 قلب التراب وكشف المدفون` — overturning earth/exposing buried. Selected: F3/F2. Grade: strong.
- `B002 تبديد المتاع وقلب بعضه على بعض` — scattering baggage. Selected: F5. Grade: medium.
- `B003 هدم الحوض وقلب أسفله أعلاه` — overturning a trough. Selected weakly F5; no trough role. Grade: weak.

### 100:9:7 `ٱلْقُبُورِ` — root `ق ب ر`

- `B001 مواراة الميت في القبر` — burial/grave. Selected: F3. Grade: strong.
- `B002 غموض الشيء وتطامنه` — hiddenness/sunkenness. Selected: F3. Grade: medium-strong.
- `B003 القُبَّرة الطائر` — bird. No selected E. Grade: unlikely.
- `B004 طرف الأنف في الغضب` — nose-tip in anger. No selected E. Grade: unlikely.

### 100:10:1 `وَحُصِّلَ` — root `ح ص ل`

- `B001 جمع الشيء حتى يظهر حاصله` — collecting until result appears. Selected: F3/F5/F6. Grade: strong.
- `B002 استخراج اللب أو النفيس من غلافه` — extracting kernel/precious thing. Selected: F3/F2/F7. Grade: strong.
- `B003 البقية والحثالة بعد الرفع أو الفصل` — residue after separation. Selected: F5. Grade: medium.
- `B004 موضع يجتمع فيه الطعام في جوف الطائر` — bird crop. Weak container analogy; no bird/food role. Grade: weak.
- `B005 بلح حصل من النخلة قبل اشتداده` — unripe dates. Rejected F11. Grade: unlikely.
- `B006 وجع بطن الفرس من أكل التراب` — horse belly pain from dirt. Weak early animal/dust echo but no pain role. Grade: unlikely.

### 100:10:4 `ٱلصُّدُورِ` — root `ص د ر`

- `B001 الصدر الجارحة وما يتصل بها` — chest. Selected: F3/F7/F4. Grade: strong.
- `B002 المقدّم والأعلى والأول` — front/top/first. Selected: F9 weakly. Grade: medium.
- `B003 الصُّدور عن المورد` — departing from water/source. Rejected F11. Grade: weak.
- `B004 الأصل الذي تصدر عنه الأفعال` — source/origin of acts. Selected: F3/F6. Grade: medium.
- `B005 المصادرة على مال` — confiscation of money. Weak with `خير`; no fiscal act. Grade: unlikely.
- `B006 الطائفة من الشيء` — portion. No selected E. Grade: weak.

### 100:11:2 `رَبَّهُم` — root `ر ب ب`, second occurrence

- `B001 ربوبية وملك وسيادة` — final lordship/mastery. Selected: F4/F3 closure. Grade: strong.
- `B002 إصلاح وتربية وإتمام` — final caretaker/completer. Selected: F4 closure. Grade: strong.
- `B003 علم رباني` — knowledge branch. Selected weakly F6 with `خبير`. Grade: medium.
- `B004 ربة وجماعات كثيرة` — groups. Weak with plural `هم`, no model. Grade: weak.
- `B005 ربيب وربيبة ورابة` — foster relation. Weak relation variant. Grade: weak.
- `B006 رُبّ خاثر وإصلاح به` — thick syrup/repair. No selected E. Grade: unlikely.
- `B007 لزوم وإقامة ودوام` — staying/duration. Weak final permanence. Grade: weak.
- `B008 رباب السحاب` — clouds. Rejected F11. Grade: unlikely.
- `B009 شاة رُبّى وحداثة` — ewe/recent birth. No selected E. Grade: unlikely.
- `B010 ربابة تجمع القداح` — arrow/lot container. Rejected F12. Grade: unlikely.
- `B011 ربابة عهد وميثاق` — covenant/protection. Selected: F4 closure as relational return. Grade: medium.
- `B012 ربة نبات` — plant. Rejected F11. Grade: unlikely.
- `B013 ماء رَبَب كثير` — abundant water. Rejected F11. Grade: unlikely.
- `B014 رَبْرَب قطيع` — herd. No selected E. Grade: unlikely.
- `B015 حرف رب وربما` — particle. No selected E. Grade: unlikely.
- `B016 رُبَى حاجة وعقدة ونعمة` — need/knot/blessing. Weak F4/F7 closure. Grade: weak.
- `B017 رباني الملاحين` — sailors’ chief. No selected E. Grade: unlikely.

### 100:11:5 `لَّخَبِيرٌ` — root `خ ب ر`

- `B001 العلم بالخبر وباطن الأمر` — knowledge of report/inner affair. Selected: F2/F3/F4/F6/F7. Grade: strong.
- `B002 لين الأرض ومائها` — soft/moist land. Rejected F11. Grade: weak.
- `B003 إصلاح الأرض بالمخابرة` — agricultural cultivation. Rejected F11. Grade: weak.
- `B004 الغزر في المزادة والناقة` — wide/gushing vessel/camel. Rejected F11; no vessel/camel closure. Grade: unlikely.
- `B005 اللين في النبات والوبر والزبد` — soft plant/froth. Rejected F11. Grade: unlikely.
- `B006 القسمة في الشاة واللحم` — division/share of meat. Weak distribution branch; no division role. Grade: weak.

## Constructional, morphosyntactic, and temporal seed audit

- Construction seed `opening oath chain 100:1–3`: `و` oath particle plus genitive active participles. Model: solemn kinetic sequence. Selected: F1. Corroborators: attachment row 100:1 particle-complement; QAC FP active participles. Grade: strong.
- Construction seed `three accusative early modifiers`: `ضبحا، قدحا، صبحا`. Model: manner → manner → time. Selected: F1/F8. Grade: medium-strong.
- Temporal/acoustic seed `early -an accusative cadence`: `ضبحا/قدحا/صبحا/نقعا/جمعا`. Model: rapid staged impacts. Selected: F1. Constraint: sound/case cadence is structural support only, not lexical meaning. Grade: medium.
- Morphosyntactic seed `fā-chain 100:2–5`: sequential `فَ` progression. Model: cumulative event chain. Selected: F1. Grade: strong.
- Morphosyntactic seed `feminine plural agents 100:1–5`: active participles and 3FP perfect verbs. Model: same agent-set continues through the early kinetic scene. Selected: F1. Constraint: no explicit noun identifying the agents. Grade: strong.
- Construction seed `repeated بِهِ in 100:4–5`: same pronominal instrument/path is reactivated. Model: dust and center-entry happen by the same prior force. Selected: F1/F2. Constraint: antecedent remains locally pronominal, not lexically named. Grade: medium-strong.
- Discourse seed `إِنَّ الإنسان` at 100:6: abrupt assertion after kinetic oath. Model: early external force opens onto human moral predicate. Selected: F4. Constraint: not grammatical identity with early feminine plural agents. Grade: strong.
- Construction seed `three emphatic predications 100:6–8`: `لكَنود / لشهيد / لشديد`. Model: human state is layered: relation breach, witness, intense attachment. Selected: F4/F6/F7. Grade: strong.
- Attachment seed `لربه` with `كنود`: target of predicate. Model: ingratitude is defined with respect to Rabb. Selected: F4. Grade: strong.
- Attachment seed `على ذلك` with `شهيد`: specified matter of witness. Model: witness refers back to the stated breach. Selected: F6/F4. Grade: strong.
- Attachment seed `لحب الخير` with `شديد`: intensity is attached to love, and love to good. Model: inner attachment. Selected: F7. Grade: strong.
- Construction seed `أفلا يعلم إذا`: knowledge-question plus temporal condition. Model: present failure of knowing is answered by future disclosure. Selected: F3/F6/F8. Grade: strong.
- Construction seed `ما فِي القبور / ما فِي الصدور`: parallel hidden contents. Model: external and internal containers opened in sequence. Selected: F3. Grade: strong.
- Morphosyntactic seed `passive بُعثر / حُصّل`: contents undergo exposure/extraction without an explicit human agent. Model: disclosure happens to the hidden contents. Selected: F3/F6. Grade: strong.
- Temporal seed `إذا / يومئذ`: condition and closure day. Model: disclosure sequence is temporally bounded and closes when Rabb is خبير. Selected: F3/F6. Grade: medium-strong.
- Reactivation seed `ربه → ربهم`: singular human relation returns as plural final accountability. Model: middle predicate and final knowledge share the Rabb relation. Selected: F4/F6. Grade: strong.
- Pronoun seed `هِ/ه/ه/هم/بهم`: recurring reference chain. Model: personhood and relation are carried through assertion, witness, love, and final knowing. Selected: F4/F6. Constraint: pronoun resolution cannot override explicit syntax. Grade: medium.
- Opening-context seed `بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`: visible in sacred JSON only; not used as lexical seed, corroborator, or constraint because QAC opening-context rows were unavailable and no synthesis required it. Grade: not initiated.

## Convergence summary

Strong convergences:

- F1 is independently regenerated by motion, breath, spark, stirring, dust, middle-entry, and gathering branches.
- F3 is independently regenerated by burial, hiddenness, extraction, chest, knowledge, and expert-interior branches.
- F4 is independently regenerated by human, Rabb, cutting/ingratitude, witness, love, good, and intensity branches, then reactivated by the final `ربهم ... خبير`.

Medium convergences:

- F2 bridges the early spark/dust scene and the final hidden-content disclosure.
- F5 abstracts the passage as repeated disruption and recomposition.
- F6 organizes the second half as witness → knowledge → expert closure.
- F7 explains the local 100:8 inner-attachment structure and is corroborated by 100:10.

Rejected or weak rivals:

- F10 sound-only cannot explain enough of the passage.
- F11 water/seed/nurture has several branch contacts but is defeated by the actual syntax of dust, love, graves, chests, and disclosure.
- F12 lot/shaft/container is a branch intersection without passage-local grammatical support.

Very short interpretation: S100 produces a strong two-stage reactivation. The first five ayahs build an ordered kinetic incursion into a gathered center. The middle ayahs redirect that force into the human relation with Rabb, marked by ingratitude, witness, and intense inner love of good. The final ayahs reactivate the early disturbance image as a disclosure system: what is buried and what is in the chests is opened, gathered, and known by Rabb as `خبير`.
