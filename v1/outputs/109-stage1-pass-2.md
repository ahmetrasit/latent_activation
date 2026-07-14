# S109 Stage 1 Pass 2: Temporally Conditioned Reactivation

Assigned passage: S109  
Sacred Arabic text source: `resources/quran/surah_109.json`  
Prompt: `v1/prompts/stage1.md`

## Root Cause For Pass 1 Limitation

The root cause was procedural and resource-related, not lexical selectivity. I visited the main roots and some promising branches in context, but I did not write an occurrence-by-occurrence, branch-by-branch seed audit. The required SQLite resources are also empty in this checkout:

- `resources/qac.sqlite`: zero bytes, so the prompted QAC schema and morpheme queries return no tables.
- `resources/furuq_v4.sqlite`: zero bytes, so the prompted furuq branch query cannot run against SQLite.

For this recovery pass I restarted at the first rooted word and used the available local TSV mirrors for the same data:

- `resources/qac_root_ayah.tsv` for rooted occurrence rows, surfaces, lemmas, POS, measures, and ayah root sequence.
- `resources/v4_branches.tsv` for accepted branch dossiers, restricted to S109 roots and basmala opening-context roots.
- `resources/attachments.tsv` for S109 structural evidence.
- `resources/quran/surah_109.json` for sacred Arabic text.

This substitution is a constraint on auditability. No translation is used as evidence. The basmala is opening context only and never initiates a seed.

## Sacred Text and Progressive Exposure

```text
109:0 بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
109:1 قُلْ يَٰٓأَيُّهَا ٱلْكَٰفِرُونَ
109:2 لَآ أَعْبُدُ مَا تَعْبُدُونَ
109:3 وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ
109:4 وَلَآ أَنَا۠ عَابِدٌۭ مَّا عَبَدتُّمْ
109:5 وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ
109:6 لَكُمْ دِينُكُمْ وَلِىَ دِينِ
```

Temporal state:

1. `قُلْ` first activates an instructed utterance rather than a private thought. The passage begins as a quoted speech act.
2. `يَٰٓأَيُّهَا ٱلْكَٰفِرُونَ` fixes the addressee by a participial identity before any worship relation is denied.
3. `لَآ أَعْبُدُ مَا تَعْبُدُونَ` gives the first relation: first-person singular subject, negated worship action, object defined by the addressees' worship.
4. `وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ` reverses subject roles and changes into nominal/active-participle predication.
5. `وَلَآ أَنَا۠ عَابِدٌۭ مَّا عَبَدتُّمْ` returns to first-person singular but keeps active-participle predication and points to the addressees' prior worship by perfect `عَبَدتُّمْ`.
6. `وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ` repeats the second negation, reactivating the reciprocal non-participation as stable rather than momentary.
7. `لَكُمْ دِينُكُمْ وَلِىَ دِينِ` closes by replacing verbal worship-relations with possessed/assigned `دين` domains under fronted `لـ` predicates.

## Rooted Occurrence Inventory

Recovered from `qac_root_ayah.tsv`. Pronouns, `مَا`, particles, and lām predicates are used as structural evidence through attachment rows, but the rooted lexical seed inventory from this QAC mirror contains only the rows below.

| Occurrence | Root | Surface(s) | Lemma/POS/measure | Seed treatment |
| --- | --- | --- | --- | --- |
| 109:1:1 | ق و ل | قُلْ | قَالَ, V | all 16 accepted branches initiated |
| 109:1:3 | ك ف ر | كَٰفِرُونَ | كَٰفِرُون, N | all 15 accepted branches initiated |
| 109:2:2 | ع ب د | أَعْبُدُ | عَبَدَ, V | 10 accepted branches initiated at this occurrence |
| 109:2:4 | ع ب د | تَعْبُدُونَ | عَبَدَ, V | 10 accepted branches initiated at this occurrence |
| 109:3:3 | ع ب د | عَٰبِدُونَ | عَابِد, N | 10 accepted branches initiated at this occurrence |
| 109:3:5 | ع ب د | أَعْبُدُ | عَبَدَ, V | 10 accepted branches initiated at this occurrence |
| 109:4:3 | ع ب د | عَابِدٌ | عَابِد, N | 10 accepted branches initiated at this occurrence |
| 109:4:5 | ع ب د | عَبَدتُّمْ | عَبَدَ, V | 10 accepted branches initiated at this occurrence |
| 109:5:3 | ع ب د | عَٰبِدُونَ | عَابِد, N | 10 accepted branches initiated at repeated occurrence |
| 109:5:5 | ع ب د | أَعْبُدُ | عَبَدَ, V | 10 accepted branches initiated at repeated occurrence |
| 109:6:2 | د ي ن | دِينُ | دِين, N | all 7 accepted branches initiated |
| 109:6:4 | د ي ن | دِينِ | دِين, N | all 7 accepted branches initiated |

Total lexical occurrence-branch seeds initiated: 125.

## Attachment Evidence Used

- `(C/K: 109:1 a1)` `أَيُّهَا` is the vocative expression introduced by `يَٰٓ`.
- `(C: 109:1 a2)` `ٱلْكَٰفِرُونَ` specifies the addressees in the vocative construction.
- `(C: 109:1 a3)` the vocative content is governed by `قُلْ`.
- `(C: 109:2 a1)` `مَا تَعْبُدُونَ` is object of `أَعْبُدُ`.
- `(C: 109:2 a2)` `مَا` is the fronted object inside the relative clause of `تَعْبُدُونَ`.
- `(C: 109:3 a1)` `عَٰبِدُونَ` predicates over `أَنتُمْ`.
- `(C: 109:3 a2)` `مَا أَعْبُدُ` is object of active participle `عَٰبِدُونَ`.
- `(C: 109:3 a3)` `مَا` is the fronted object inside the relative clause of `أَعْبُدُ`.
- `(C: 109:4 a1)` `عَابِدٌ` predicates over `أَنَا`.
- `(C: 109:4 a2)` `مَّا عَبَدتُّمْ` is object of active participle `عَابِدٌ`.
- `(C: 109:4 a3)` `مَّا` is the fronted object inside the relative clause of perfect `عَبَدتُّمْ`.
- `(C: 109:5 a1-a3)` repeats the 109:3 predication and object structure.
- `(C: 109:6 a1/a4)` suffixes in `لَكُمْ` and `لِيَ` are governed by the fronted lām predicates.
- `(C: 109:6 a2/a5)` `لَكُمْ` and `وَلِيَ` are fronted predicates of `دِينُكُمْ` and `دِينِ`.
- `(C: 109:6 a3/a6)` possessive suffixes attach to the two `دِين` nouns.

## Branch Dossier Index

All accepted branches below were read as continuous root dossiers before seed selection.

`ق و ل`: B001 utterance by speech; B002 tongue as instrument; B003 one characterized by much speech; B004 authoritative `قيل` whose word is effective; B005 saying what was not or falsely attributing; B006 drawing a saying to oneself; B007 circulating public talk; B008 stick used to strike a game-piece; B009 negotiation/conversation in an affair; B010 imposing judgment/control; B011 saying functioning like supposing; B012 inner saying not yet manifested; B013 saying as belief/madhhab; B014 a thing's indication; B015 sincere concern for a thing; B016 logical definition/limit.

`ك ف ر`: B001 covering/veiling; B002 overwhelming cover such as night/sea; B003 covering truth, unbelief, denial, opposition; B004 covering/denying blessing; B005 disavowal or repudiation; B006 declaring someone a kafir; B007 forcing an obedient one into disobedience; B008 farmer covering seed; B009 expiation by covering sin; B010 fruit casing/spathe; B011 camphor/perfume; B012 remote/isolated place; B013 mountain pass or low wall; B014 bowed/tucked posture of subservience; B015 crown covering a king.

`ع ب د`: B001 slave/owned person; B003 worship and obedient submission with humility; B004 enslaving/subjugating; B005 made-smooth/trodden road, tarred camel/ship; B006 honored/served person; B007 strength/hardness; B008 pride, anger, grief at loss; B009 little delay or quick running; B010 dispersed groups/paths; B011 breakdown, being stranded, or difficult animal; B012 perfume mortar.

`د ي ن`: B001 obedience, submission, worship, religion, law; B002 reckoning, judgment, repayment; B003 debt/credit dealing; B004 subjugation, ownership, making a slave; B005 habit, custom, recurring state; B006 city where authority is obeyed; B007 certifying or entrusting someone to his own dīn.

Opening context dossiers inspected only when needed: `ء ل ه B001/B002`, `ر ح م B001-B004`, `س م و B001-B008`. They are not seed sources.

### Exact Passage Branch Dossiers

These are the exact `branch_image_ar` plus `what_is_ar` fields used from the local `v4_branches.tsv` recovery source.

- `د ي ن B001`: الطاعة والانقياد — الدين بمعنى الطاعة والانقياد والتعبد والملة والشريعة وما يتدين به
- `د ي ن B002`: الحساب والجزاء — الدين بمعنى الحكم والحساب والجزاء والمكافأة والقضاء
- `د ي ن B003`: الدين المالي — الدين المالي والقرض والاستقراض والمداينة والبيع إلى أجل وما يؤخذ أو يعطى دينا
- `د ي ن B004`: الإذلال والملك — الإذلال والقهر والملك والاستعباد والحمل على المكروه والعبد المدين والأمة المدينة
- `د ي ن B005`: العادة والشأن — الدين بمعنى العادة والشأن والحال المعهود والدأب
- `د ي ن B006`: مدينة الطاعة — المدينة بمعنى المصر والموضع الذي تقام فيه طاعة ذوي الأمر
- `د ي ن B007`: التصديق والتفويض — التديين بمعنى تصديق الرجل في القضاء أو الحلف أو تفويضه إلى دينه
- `ع ب د B001`: الرق والملك — يدخل فيه العبد المملوك وخلاف الحر ومن يصح بيعه وابتياعه وجموع العبيد والأعبد والعبدى والمعبدة
- `ع ب د B003`: العبادة والطاعة الخاضعة — يدخل فيه عبادة الله والتنسك والطاعة مع الخضوع والتوحيد وعبادة الطاغوت بمعنى طاعته والخضوع لملك أو دنيا
- `ع ب د B004`: التعبيد والاستعباد — يدخل فيه عبدت الرجل واستعبدته وأعبدته وتعبدت فلانا إذا اتخذته عبدا أو صيرته كالعبد أو ذللته حتى يعمل عمل العبد
- `ع ب د B005`: التذليل والتسوية — يدخل فيه الطريق المعبد المسلوك المذلل والبعير أو الجمل المعبد المهنوء بالقطران والسفينة المعبدة المقيرة
- `ع ب د B006`: التكريم والتعظيم — يدخل فيه المعبد بمعنى المكرم والمعظم والمخدوم
- `ع ب د B007`: القوة والصلابة — يدخل فيه العبدة بمعنى القوة والصلابة والشدة والبقاء والسمن في الناقة وقوة الثوب
- `ع ب د B008`: الأنفة والغضب — يدخل فيه العبد والعبدة بمعنى الأنفة والحمية والغضب والحزن والوجد والندم عند فوات الشيء
- `ع ب د B009`: قلة اللبث وسرعة العدو — يدخل فيه ما عبد أن فعل أي ما لبث وعبد يعدو إذا أسرع بعض الإسراع
- `ع ب د B010`: التفرق في الوجوه — يدخل فيه العباديد والعبابيد للفرق من الناس أو الأشياء أو الطرق المتفرقة الذاهبة في كل وجه
- `ع ب د B011`: العطب والانقطاع — يدخل فيه أعبد بفلان أو أعبد به بمعنى أبدع به إذا كلت راحلته أو عطبت أو ذهبت ويدخل فيه البعير المتعبد الممتنع صعوبة
- `ع ب د B012`: صَلاءة الطيب — يدخل فيه العبدة اسما لصَلاءة الطيب
- `ق و ل B001`: إخراج القول بالنطق — يدخل فيه قال يقول قولا، والقول والقيل، والكلام المركب من الحروف إذا أبرز بالنطق، مفردا كان أو جملة أو قصيدة أو خطبة.
- `ق و ل B002`: اللسان آلة القول — يدخل فيه المقول بمعنى اللسان.
- `ق و ل B003`: كثرة القول في صاحبه — يدخل فيه قولة وقوال وقوالة وتقوالة وقؤول ومقوال ومقول إذا وصفت الإنسان بأنه لسن أو كثير القول أو منطيق.
- `ق و ل B004`: القيل صاحب القول النافذ — يدخل فيه المقول أو القيل بلغة أهل اليمن، والواحد القيل، والجمع المقاولة والأقيال والأقوال، وملك حمير دون الملك الأعظم، والمرأة قيلة.
- `ق و ل B005`: قول ما لم يكن أو نسبته — يدخل فيه تقول باطلا، وتقول عليه أي كذب عليه، وقولتني أو أقولتني ما لم أقل.
- `ق و ل B006`: اجترار القول إلى النفس — يدخل فيه اقتال قولا إذا اجتر إلى نفسه قولا من خير أو شر.
- `ق و ل B007`: القول الفاشي بين الناس — يدخل فيه القالة الحسنة أو القبيحة المنتشرة في الناس، وكثرة قالة الناس، والقيل والقال بوصفهما حديثا دائرا.
- `ق و ل B008`: عود القال لضرب القلة — يدخل فيه القال، الخشبة التي تضرب بها القلة.
- `ق و ل B009`: المقاولة في الأمر — يدخل فيه قاولته في أمره وتقاولنا إذا تفاوضنا.
- `ق و ل B010`: اقتالة الحكم على غيره — يدخل فيه اقتال عليه إذا كان بمعنى تحكم.
- `ق و ل B011`: قول يجري مجرى الظن — يدخل فيه تقول إذا أجري مجرى تظن في العمل، وخاصة في الاستفهام، وما ذكر عن بني سليم من إجراء متصرف قلت مجرى الظن في غير الاستفهام.
- `ق و ل B012`: قول في النفس لم يظهر — يدخل فيه المتصور في النفس قبل الإبراز باللفظ، كما في قول في نفسي لم أظهره.
- `ق و ل B013`: القول اعتقاد ومذهب — يدخل فيه القول بمعنى الاعتقاد، نحو فلان يقول بقول أبي حنيفة.
- `ق و ل B014`: قول الشيء دلالته — يدخل فيه القول للدلالة على الشيء، مثل امتلأ الحوض وقال قطني.
- `ق و ل B015`: العناية الصادقة بالشيء — يدخل فيه فلان يقول بكذا إذا كان معناه العناية الصادقة بالشيء.
- `ق و ل B016`: قول الشيء حده — يدخل فيه استعمال المنطقيين القول بمعنى الحد، كقول الجوهر وقول العرض أي حدهما.
- `ك ف ر B001`: ستر وتغطية — يدخل فيه ستر الشيء وتغطيته وكفر الدرع بثوب وتغطية السلاح والرماد المكفور وستر الشمس النجوم والسحاب الشمس
- `ك ف ر B002`: غمر ساتر — يدخل فيه الكافر للليل المظلم والبحر والنهر العظيم ومغيب الشمس وما يستر بظلمته أو سعته
- `ك ف ر B003`: حجب الحق — يدخل فيه الكفر نقيض الإيمان وجحود الوحدانية أو الشريعة أو النبوة والإنكار والجحود والمعاندة والنفاق والشرك والتكذيب
- `ك ف ر B004`: ستر النعمة — يدخل فيه كفر النعمة وكفرانها وجحودها وترك شكرها والكفور في كفران النعمة
- `ك ف ر B005`: تبرؤ وتنصل — يدخل فيه الكفر بمعنى البراءة والتنصل من الشيء أو بعضهم من بعض
- `ك ف ر B006`: نسبة إلى الكفر — يدخل فيه أكفر الرجل بمعنى دعاه كافرا أو حكم بكفره أو نسبه إلى الكفر
- `ك ف ر B007`: إلجاء إلى العصيان — يدخل فيه أكفرته إذا ألجأت المطيع إلى أن يعصي
- `ك ف ر B008`: تغطية البذر — يدخل فيه الكافر للزارع والكفار للزراع لأنهم يغطون الحب أو البذر بالتراب
- `ك ف ر B009`: محو الإثم بتغطيته — يدخل فيه الكفارة لما يكفر الخطيئة أو اليمين والتكفير للسيئات والمعاصي حتى تصير كأن لم تعمل
- `ك ف ر B010`: كمام الثمر — يدخل فيه الكافور والكفرى والكوافير لأكمام العنب أو طلع النخل أو الورقة التي تستر الثمرة
- `ك ف ر B011`: كافور طيب — يدخل فيه الكافور من الطيب وعين ماء في الجنة والنبات المسمى كافورا
- `ك ف ر B012`: موضع منقطع — يدخل فيه الكافر من الأرض البعيد عن الناس والكفور للقرى والكفر للقرية والقبر
- `ك ف ر B013`: ثنية مستورة — يدخل فيه الكفرات والثنايا من الجبال والكفر العظيم من الجبال والحائط الواطئ
- `ك ف ر B014`: خضوع متطامن — يدخل فيه التكفير بمعنى إيماء الذمي برأسه أو وضع اليد على الصدر والتطامن خضوعا
- `ك ف ر B015`: تاج يغطي — يدخل فيه التكفير بمعنى تتويج الملك بتاج أو التاج نفسه

## Candidate Synthesis Units

### S109-S1-001: Commanded Boundary Speech

- `candidate_id`: S109-S1-001
- `ayah_range`: 109:1-6
- `seed_type`: lexical / constructional
- `seed`: 109:1:1 `قُلْ`, especially `ق و ل B001`
- `generating_set`: `(E: ق و ل B001 utterance by speech)`, `(E: 109:1 a3 quoted complement governed by قُلْ)`, `(E: ك ف ر B003 addressee identity as truth-covering denial)`, `(E: ع ب د B003 worship/submissive obedience)`.
- `selected_branches`: `ق و ل B001`, `ك ف ر B003`, `ع ب د B003`, `د ي ن B001`.
- `constructed_model`: The passage is first built as a public utterance whose purpose is to set a boundary. The command to say makes the separation spoken and auditable; the vocative names the addressed party before the worship clauses begin; the repeated worship negations then specify which relations do not cross; the final `دين` line names the resulting domains.
- `freeze_point`: after 109:1 `قُلْ يَٰٓأَيُّهَا ٱلْكَٰفِرُونَ`, before the worship denials.
- `predictions_at_freeze`: a quoted content boundary; addressee differentiation; explicit non-overlap between speaker and addressees; closure by a stable classification rather than by argument.
- `unused_features_tested`: 109:2-5 repeated `لَا` clauses; `مَا` object symmetry; verbal versus nominal worship predication; repeated 109:3/109:5 line; 109:6 fronted `لـ` predicates.
- `corroborators`: `(C: 109:2 a1-a2 first negated worship-object relation)`, `(C: 109:3 a1-a3 reversed subject relation)`, `(C: 109:4 a1-a3 active participle plus perfect of addressees' prior worship)`, `(C: 109:5 repeats 109:3)`, `(C: د ي ن B001 final religion/obedience domain)`, `(C: 109:6 a2/a5 fronted predicates assign domains)`.
- `constraints`: `(K: ق و ل B009 negotiation is not selected; the passage contains no bargaining exchange)`, `(K: ق و ل B005 false attribution is only constraining because the commanded utterance cannot be treated as self-invented slander)`, `(K: basmala opening-context supplies divine naming frame but is not generating evidence)`.
- `temporal_reactivation_notes`: The command `قُلْ` is reactivated at every `لَا`: each denial is not merely inner refusal but recited boundary speech. The closing `لَكُمْ ... وَلِيَ ...` reactivates the original speech act as a final assignment.
- `rival_models`: private inner refusal from `ق و ل B012`; public polemical label from `ق و ل B007`. Both contribute little because the syntax begins with an imperative quoted complement.
- `grade`: strong
- `grade_rationale`: The first rooted word directly governs the whole quoted content, and later structure repeatedly fulfills the predicted boundary function.
- `source_queries_or_rows_used`: `qac_root_ayah.tsv` S109; `v4_branches.tsv` roots `ق و ل`, `ك ف ر`, `ع ب د`, `د ي ن`; attachments 109:1 a1-a3, 109:2-6.

### S109-S1-002: Covering Identity Exposed by Non-Shared Worship

- `candidate_id`: S109-S1-002
- `ayah_range`: 109:1-6
- `seed_type`: lexical
- `seed`: 109:1:3 `ٱلْكَٰفِرُونَ`, `ك ف ر B001/B003`
- `generating_set`: `(E: ك ف ر B001 covering/veiling)`, `(E: ك ف ر B003 covering truth / denial)`, `(E: ق و ل B001 public utterance)`, `(E: ع ب د B003 worship/submissive obedience)`.
- `selected_branches`: `ك ف ر B001`, `ك ف ر B003`, `ق و ل B001`, `ع ب د B003`, `د ي ن B001`.
- `constructed_model`: A covered or truth-concealing identity is addressed publicly. The following denials do not uncover hidden details about their objects; instead they expose a structural fact: the worship relations of the speaker and addressees are mutually non-participating. The covering identity is thus answered by explicit non-commingling rather than by debate.
- `freeze_point`: after the vocative `يَٰٓأَيُّهَا ٱلْكَٰفِرُونَ`.
- `predictions_at_freeze`: a public naming, an exposed contrast, a refusal to merge worship objects, and some final boundary marker.
- `unused_features_tested`: four `ع ب د` clauses, subject alternation `أنا/أنتم`, `مَا` object alternation, final `دين`.
- `corroborators`: `(C: ق و ل B001 makes the address explicit)`, `(C: 109:2-5 repeated negation exposes non-overlap)`, `(C: د ي ن B001 supplies final named obedience/religion domain)`, `(C: 109:6 possession suffixes prevent shared domain)`.
- `constraints`: `(K: ك ف ر B001 physical covering remains secondary; the primary local form is the addressee noun)`, `(K: the passage does not narrate an act of covering)`, `(K: ك ف ر B008 farmer/seed and B010 fruit casing do not find local agricultural complement)`.
- `temporal_reactivation_notes`: The addressee label is heard before any predicate. Later `ما تعبدون` repeatedly reactivates why the label mattered: the addressees are defined by a covered/denying relation to what the speaker worships.
- `rival_models`: generic insult model; agricultural covering model; night/sea engulfment model. These lack local role completion.
- `grade`: medium-strong
- `grade_rationale`: The lexical branch fits the explicit addressee identity and is strongly corroborated by worship-domain separation, but physical covering imagery remains secondary.
- `source_queries_or_rows_used`: `ك ف ر B001/B003`; attachments 109:1 a2 and 109:2-6.

### S109-S1-003: Worship as Non-Transferable Servitude

- `candidate_id`: S109-S1-003
- `ayah_range`: 109:2-6
- `seed_type`: lexical / verified composite
- `seed`: first worship occurrence 109:2:2 `أَعْبُدُ`, `ع ب د B003` with servant/ownership branches tested
- `generating_set`: `(E: ع ب د B003 worship and obedient submission with humility)`, `(E: ع ب د B001 slave/owned person as secondary servitude geometry)`, `(E: د ي ن B001 obedience/religion)`, `(E: د ي ن B004 subjugation/ownership as secondary closure geometry)`.
- `selected_branches`: `ع ب د B003`, `ع ب د B001`, `ع ب د B004`, `د ي ن B001`, `د ي ن B004`.
- `constructed_model`: The worship clauses are not merely denials of ritual actions; they model incompatible servitude relations. The speaker does not enter the addressees' object-domain, and the addressees are not worshippers of the speaker's object-domain. The final `دين` line converts repeated worship relations into each side's obedience/servitude order.
- `freeze_point`: after 109:2 `لَا أَعْبُدُ مَا تَعْبُدُونَ`, before the reciprocal denials.
- `predictions_at_freeze`: a reciprocal denial from the addressees' side; object-domain contrast; final stable relation of obedience or rule; no shared master/object.
- `unused_features_tested`: 109:3 reciprocal nominal denial; 109:4 speaker active-participle denial with addressees' perfect object; 109:5 repetition; 109:6 `دين`.
- `corroborators`: `(C: 109:3 a1-a3 predicted reciprocal denial)`, `(C: 109:4 a1-a3 blocks speaker from being characterized as worshipper of their past object)`, `(C: 109:5 repetition stabilizes non-transferability)`, `(C: د ي ن B001 obedience/religion)`, `(C: د ي ن B004 ownership/subjugation as secondary geometry)`, `(C: 109:6 a2/a5 fronted lām assignment)`.
- `constraints`: `(K: ع ب د B001/B004 do not replace primary worship meaning)`, `(K: no literal slave-sale or coercion event is narrated)`, `(K: د ي ن B004 is secondary because the surface noun here is religion/domain, not explicit enslavement)`.
- `temporal_reactivation_notes`: Each later `ع ب د` occurrence reactivates the first denial with a new grammatical angle: present action, standing characterization, past addressee practice, repeated standing characterization. `دين` then reactivates all worship clauses as durable obedience domains.
- `rival_models`: pure ritual refusal; literal slavery model. The first under-explains `دين`; the second over-literalizes secondary geometry.
- `grade`: strong
- `grade_rationale`: The same root is repeated eight times and closes with a root whose primary branch overlaps obedience/religion. The grammatical alternation supplies independent corroboration.
- `source_queries_or_rows_used`: all S109 `ع ب د` rows; `د ي ن B001/B004`; attachments 109:2-6.

### S109-S1-004: Aspectual Locking Across Present, Standing, and Past Worship

- `candidate_id`: S109-S1-004
- `ayah_range`: 109:2-5
- `seed_type`: morphosyntactic / temporal
- `seed`: sequence of `أَعْبُدُ / تَعْبُدُونَ / عَٰبِدُونَ / عَابِدٌ / عَبَدتُّمْ`
- `generating_set`: `(E: morphology imperfect verb in 109:2)`, `(E: morphology active participle in 109:3)`, `(E: morphology active participle plus perfect verb in 109:4)`, `(E: repeated active participle line in 109:5)`, `(E: ع ب د B003 worship/submission)`.
- `selected_branches`: `ع ب د B003`; structural attachments 109:2 a1-a2, 109:3 a1-a3, 109:4 a1-a3, 109:5 a1-a3.
- `constructed_model`: The passage locks non-participation across temporal/aspectual surfaces: immediate action is denied, standing characterization is denied, prior addressee worship is denied as an object for the speaker, and the addressees' standing non-worship is repeated. This prevents the listener from hearing the denial as temporary, one-sided, or only past-related.
- `freeze_point`: after hearing 109:2-3, where verbal action denial is followed by nominal/active-participle reciprocal denial.
- `predictions_at_freeze`: additional temporal/aspectual clarification; possible return to the speaker; final closure that no side crosses into the other's domain.
- `unused_features_tested`: 109:4 perfect `عَبَدتُّمْ`; 109:5 repeated line; 109:6 `دين`.
- `corroborators`: `(C: 109:4 perfect form tests prior object-domain)`, `(C: 109:5 repetition confirms stable addressee state)`, `(C: 109:6 final possessed domains)`.
- `constraints`: `(K: this is not an independent lexical image; it depends on syntactic ordering and morphology)`, `(K: attachment rows identify objects but do not provide detailed QAC morpheme features because SQLite is empty)`.
- `temporal_reactivation_notes`: The perfect `عَبَدتُّمْ` in 109:4 sends the listener backward: the first `ما تعبدون` was not only present behavior but a worship-history domain. The 109:5 repetition reactivates 109:3 as final and unresolved.
- `rival_models`: simple repetition for emphasis; complete synonymy of all worship clauses. The aspectual changes argue for more than flat repetition.
- `grade`: strong
- `grade_rationale`: This candidate is generated by the passage order itself and is independently corroborated by attachment structure and final `دين` closure.
- `source_queries_or_rows_used`: qac root rows for `ع ب د`; attachments 109:2-5.

### S109-S1-005: Final Domain Partition by Dīn

- `candidate_id`: S109-S1-005
- `ayah_range`: 109:6, replaying 109:1-5
- `seed_type`: lexical / constructional
- `seed`: 109:6 `دِينُكُمْ` and `دِينِ`, especially `د ي ن B001/B005/B007`
- `generating_set`: `(E: د ي ن B001 obedience/religion/law)`, `(E: د ي ن B005 habit/custom/state)`, `(E: 109:6 a2/a5 fronted lām predication)`, `(E: 109:6 a3/a6 possessive suffixes)`.
- `selected_branches`: `د ي ن B001`, `د ي ن B005`, `د ي ن B007`, with constraints from B002/B003/B006.
- `constructed_model`: The close does not introduce a new theme; it names the stable domains produced by the previous denials. `لَكُمْ` and `وَلِيَ` place each `دين` with its holder, while possessive suffixes make the division non-shared. B007 adds a secondary image of leaving/entrusting each party to its own dīn.
- `freeze_point`: after `لَكُمْ دِينُكُمْ`, before `وَلِيَ دِينِ`.
- `predictions_at_freeze`: a balancing first-person counterpart; possessive marking; no further argument after partition.
- `unused_features_tested`: `وَلِيَ دِينِ`; prior repeated worship denials; vocative addressee.
- `corroborators`: `(C: 109:6 a5 gives matching first-person fronted predicate)`, `(C: 109:6 a6 gives first-person possessive relation)`, `(C: ع ب د B003 previous worship domain)`, `(C: ق و ل B001 closure of quoted speech)`, `(C: ك ف ر B003 addressee label explains why domains remain separate)`.
- `constraints`: `(K: د ي ن B002 reckoning/judgment has no explicit day-of-judgment or accounting syntax here)`, `(K: د ي ن B003 debt has no creditor/debtor amount or transaction)`, `(K: د ي ن B006 city has no locality/governance complement)`.
- `temporal_reactivation_notes`: On hearing `دين`, all prior `ع ب د` clauses are reclassified as domain-bound obedience rather than isolated acts. The passage closes because the relation has moved from repeated negation to stable possession.
- `rival_models`: mere tolerance formula; final legal judgment. The syntax supports domain assignment more directly than either.
- `grade`: strong
- `grade_rationale`: Dīn B001 and the lām/possessive construction independently match the accumulated worship separation.
- `source_queries_or_rows_used`: `د ي ن B001/B005/B007`; attachments 109:6 a1-a6.

### S109-S1-006: Disavowal Without Negotiation

- `candidate_id`: S109-S1-006
- `ayah_range`: 109:1-6
- `seed_type`: lexical
- `seed`: `ك ف ر B005` disavowal/repudiation
- `generating_set`: `(E: ك ف ر B005 disavowal)`, `(E: ق و ل B001 commanded speech)`, `(E: repeated لَا clauses)`.
- `selected_branches`: `ك ف ر B005`, `ق و ل B001`, `ع ب د B003`, `د ي ن B007`.
- `constructed_model`: A secondary branch of `كفر` supplies a repudiation image: the speech act repeatedly disavows participation in the addressees' worship domain. The close leaves each side to its own dīn rather than seeking reconciliation or exchange.
- `freeze_point`: after selecting `ك ف ر B005` from the addressee root and hearing 109:2.
- `predictions_at_freeze`: repeated refusal; no negotiated middle; final disengagement.
- `unused_features_tested`: 109:3-5 reciprocal denials; 109:6 `لكم/ولي`; `ق و ل B009` negotiation branch.
- `corroborators`: `(C: four لَا clauses)`, `(C: د ي ن B007 entrusting/leaving to one's dīn)`, `(C: 109:6 fronted lām partition)`.
- `constraints`: `(K: the surface addressee is الكافرون in the primary unbelief sense, not an abstract noun of disavowal)`, `(K: the addressees are not shown disavowing; the speaker's utterance performs the disavowal)`.
- `temporal_reactivation_notes`: The final `لكم دينكم ولي دين` retroactively turns earlier negations into a completed act of separation.
- `rival_models`: negotiated coexistence from `ق و ل B009`; pure truth-covering model from `ك ف ر B003`.
- `grade`: medium
- `grade_rationale`: The branch is lexically accepted and fits the repeated refusal, but it is secondary to the addressee's primary identity and to `ع ب د`.
- `source_queries_or_rows_used`: `ك ف ر B005`; attachments 109:2-6.

### S109-S1-007: Public Naming and Authorized Classification

- `candidate_id`: S109-S1-007
- `ayah_range`: 109:1
- `seed_type`: lexical / constructional
- `seed`: `ق و ل B001` plus `ك ف ر B006` declaring/naming someone kafir
- `generating_set`: `(E: ق و ل B001 spoken utterance)`, `(E: ك ف ر B006 declaring someone kafir)`, `(E: 109:1 a2 apposition to vocative)`.
- `selected_branches`: `ق و ل B001`, `ك ف ر B006`; constrained by `ك ف ر B003`.
- `constructed_model`: The opening can be heard as an authorized classification speech: the speaker is told to address the group by `الكافرون`. The branch B006 does not generate the whole surah, but it highlights that the naming is not incidental; the whole quoted speech flows from a divinely commanded address.
- `freeze_point`: after 109:1.
- `predictions_at_freeze`: classification should be followed by evidence of separateness; the quoted speech should not be a private insult.
- `unused_features_tested`: 109:2-6.
- `corroborators`: `(C: 109:2-5 specify the worship relation underlying the classification)`, `(C: 109:6 closes with separated domains)`, `(C: basmala opening-context names divine source but does not seed the image)`.
- `constraints`: `(K: ك ف ر B006 is causative/naming; surface الكافرون itself is the addressed noun, not the verb أكفر)`, `(K: no general rule about calling people kafir is being constructed here)`.
- `temporal_reactivation_notes`: Later denials provide the relational reason the initial label remains active.
- `rival_models`: label as mere insult; label as agricultural/root metaphor. The quoted-command frame favors authorized classification.
- `grade`: medium
- `grade_rationale`: Good local opening fit, but the exact branch is morphologically one step away from the surface form.
- `source_queries_or_rows_used`: `ق و ل B001`; `ك ف ر B006`; attachments 109:1 a1-a3.

### S109-S1-008: Trodden Path and Customary Religion

- `candidate_id`: S109-S1-008
- `ayah_range`: 109:2-6
- `seed_type`: lexical
- `seed`: `ع ب د B005` made-smooth/trodden path and `د ي ن B005` habit/custom
- `generating_set`: `(E: ع ب د B005 trodden/made-smooth path)`, `(E: د ي ن B005 habit/custom/state)`.
- `selected_branches`: `ع ب د B005`, `د ي ن B005`, with support from repeated clause sequence.
- `constructed_model`: A secondary simulation treats worship as a worn path: repeated worship makes a way smooth by use, and the close names each party's custom/state. The repeated `ع ب د` clauses create path-like recurrence, and `دينكم/دين` closes as customary course.
- `freeze_point`: after 109:2-3 repetition of worship root.
- `predictions_at_freeze`: repeated track-like practice; final custom or way for each side.
- `unused_features_tested`: 109:4 perfect `عبدتم`; 109:5 repetition; 109:6 `دين`.
- `corroborators`: `(C: 109:4 perfect points to established prior practice)`, `(C: 109:5 repetition)`, `(C: د ي ن B005 habit/custom)`.
- `constraints`: `(K: no road, travel, camel, tar, or ship object appears)`, `(K: the primary contextual meaning remains worship)`, `(K: this image does not explain the vocative label as well as S109-S1-001/002)`.
- `temporal_reactivation_notes`: The final dīn custom branch reactivates the repeated worship clauses as established courses rather than isolated actions.
- `rival_models`: literal path; pure ritual action.
- `grade`: weak-medium
- `grade_rationale`: There is a real lexical bridge through `د ي ن B005`, but the path imagery lacks local material complements.
- `source_queries_or_rows_used`: `ع ب د B005`; `د ي ن B005`; attachments 109:2-6.

### S109-S1-009: Bowed Posture as Rejected Secondary Simulation

- `candidate_id`: S109-S1-009
- `ayah_range`: 109:1-6
- `seed_type`: lexical
- `seed`: `ك ف ر B014` bowed/tucked posture of subservience
- `generating_set`: `(E: ك ف ر B014 bowed/tucked posture)`, tested against `(C/K: ع ب د B003 worship/submission)`.
- `selected_branches`: `ك ف ر B014`; `ع ب د B003` only as post-freeze test.
- `constructed_model`: The branch opens a possible posture image: those addressed by `الكافرون` could be associated with a submissive bodily lowering. When tested, the passage supplies worship language, but it does not describe bodily gesture.
- `freeze_point`: immediately after `الكافرون` under B014.
- `predictions_at_freeze`: posture markers, body lowering, ritual gesture, or explicit object of bowing.
- `unused_features_tested`: all `ع ب د` clauses and final `دين`.
- `corroborators`: `(C: ع ب د B003 broadly overlaps worship/submission)`.
- `constraints`: `(K: no سجود/ركوع/body-part construction)`, `(K: B014 concerns تكفير posture, not the surface active-participle addressee)`, `(K: repeated clauses discuss worship objects/domains, not posture)`.
- `temporal_reactivation_notes`: Later worship clauses momentarily reactivate posture expectations but then narrow them into domain separation.
- `rival_models`: primary truth-covering model; servitude-domain model.
- `grade`: unlikely
- `grade_rationale`: Lexically available but weakly matched and defeated by local syntax.
- `source_queries_or_rows_used`: `ك ف ر B014`; attachments 109:2-6.

### S109-S1-010: Reckoning or Debt Closure Rejected

- `candidate_id`: S109-S1-010
- `ayah_range`: 109:6
- `seed_type`: lexical
- `seed`: `د ي ن B002` reckoning/judgment and `د ي ن B003` debt
- `generating_set`: `(E: د ي ن B002 reckoning/judgment/repayment)`, fork `(E: د ي ن B003 debt/credit dealing)`.
- `selected_branches`: `د ي ن B002`, `د ي ن B003`; no stable expansion selected.
- `constructed_model`: Two possible closure images arise from `دين`: final judgment/accounting, or financial obligation. Both are tested against the passage.
- `freeze_point`: at 109:6 `دينكم`.
- `predictions_at_freeze`: for B002, explicit accounting/day/judgment roles; for B003, creditor/debtor/payment/term roles.
- `unused_features_tested`: prior worship clauses; possessive lām construction.
- `corroborators`: `(C: repeated accountability-like separation is only very general for B002)`.
- `constraints`: `(K: no يوم الدين, حساب, جزاء, قضاء, or payment syntax)`, `(K: no debt transaction, amount, creditor, or deferred sale)`, `(K: possessive fronting favors domain assignment rather than accounting)`.
- `temporal_reactivation_notes`: The final word briefly opens judgment/debt branches but the passage closes before supplying their roles.
- `rival_models`: dīn as obedience/religion; dīn as habit/custom; dīn as entrusting each to own dīn.
- `grade`: unlikely
- `grade_rationale`: Branches are accepted lexically but passage-local role completion is absent.
- `source_queries_or_rows_used`: `د ي ن B002/B003`; attachments 109:6.

## Exhaustive Lexical Seed Ledger

For every entry below, the root dossiers for `ق و ل`, `ك ف ر`, `ع ب د`, and `د ي ن` were treated as the comparison set. `E` means selected before freeze; `C/K` means post-freeze test; `dies` means no passage-local role completion beyond generic association.

### ق و ل occurrence 109:1:1 `قُلْ`

| Seed | Result |
| --- | --- |
| QWL-B001 | productive: generates S109-S1-001 with commanded utterance `(E: ق و ل B001)`; strong. |
| QWL-B002 | terminates: tongue/instrument of saying has no local body/instrument role; `(K: no لسان or speech-organ construction)`; unlikely. |
| QWL-B003 | terminates: much-speech character conflicts with compact commanded utterance; no excessive speech role; unlikely. |
| QWL-B004 | local support only: authoritative word can weakly support command force, but no Yemeni `قيل`/king role; weak. |
| QWL-B005 | constraining: false attribution is resisted by imperative `قُلْ`; no lie/fabrication role; unlikely as seed. |
| QWL-B006 | terminates: drawing a saying to oneself has no local self-appropriation cue; unlikely. |
| QWL-B007 | weak fork: public circulating talk can support announced boundary, but no rumor/circulation language; weak. |
| QWL-B008 | terminates: game-stick image has no struck object except remote metaphor; unlikely. |
| QWL-B009 | rejected rival: negotiation is predicted but not supplied; repeated negations and final partition close without bargaining; unlikely. |
| QWL-B010 | weak constraint: imposed judgment/control is too strong for `قُلْ`; no `اقتالة` form; unlikely. |
| QWL-B011 | terminates: saying-as-supposing has no interrogative/suppositional syntax; unlikely. |
| QWL-B012 | weak rival: inner saying not manifested is reversed by public command; useful only as contrast; unlikely. |
| QWL-B013 | secondary: saying as belief/madhhab correlates with final dīn domains but is not the surface force of imperative `قُلْ`; weak-medium. |
| QWL-B014 | weak local: utterance indicates the boundary, but the branch requires thing-indication rather than speech command; weak. |
| QWL-B015 | terminates: sincere concern has no caring/maintenance role in passage; unlikely. |
| QWL-B016 | local support: definition/limit fits boundary-setting abstractly, but the branch is technical and secondary; weak. |

### ك ف ر occurrence 109:1:3 `ٱلْكَٰفِرُونَ`

| Seed | Result |
| --- | --- |
| KFR-B001 | productive with B003: covering image enters S109-S1-002; medium-strong. |
| KFR-B002 | terminates: night/sea/engulfing cover has no darkness, water, or vastness roles; unlikely. |
| KFR-B003 | productive: primary addressee branch in S109-S1-002 and corroborator in S109-S1-001; medium-strong. |
| KFR-B004 | terminates: ingratitude/covered blessing lacks blessing/shukr roles; unlikely. |
| KFR-B005 | productive secondary: disavowal model S109-S1-006; medium. |
| KFR-B006 | productive local: naming/classification model S109-S1-007; medium. |
| KFR-B007 | terminates: forcing obedience into disobedience has no coercive agent causing a former obedient person to disobey; unlikely. |
| KFR-B008 | terminates: farmer/seed cover has no agriculture role; unlikely. |
| KFR-B009 | terminates: expiation/covering sin has no oath, sin-removal, or compensation role; unlikely. |
| KFR-B010 | terminates: fruit casing/spathe has no fruit/plant complement; unlikely. |
| KFR-B011 | terminates: camphor/perfume has no scent, drink, or garden role; unlikely. |
| KFR-B012 | weak remote: isolated place can echo final separation, but no land/place noun appears; weak/unlikely. |
| KFR-B013 | terminates: mountain pass/low wall has no topographic complement; unlikely. |
| KFR-B014 | tested and rejected as S109-S1-009; unlikely. |
| KFR-B015 | terminates: crown/king-cover has no royal/taj role; unlikely. |

### ع ب د occurrence-specific branch passes

Common post-freeze tests for all `ع ب د` seed passes: later or earlier worship clauses, `مَا` object attachments, subject alternation, active participle versus verb, perfect `عَبَدتُّمْ`, final `د ي ن`, and lām/possessive partition.

#### Branch `ع ب د B001` slave/owned person

| Occurrence | Result |
| --- | --- |
| 109:2:2 `أَعْبُدُ` | retained in S109-S1-003 as secondary servitude geometry; predicts non-shared master/object; medium-strong. |
| 109:2:4 `تَعْبُدُونَ` | same model from addressees' side; constrained by object `ما`; medium. |
| 109:3:3 `عَٰبِدُونَ` | standing-characterization angle corroborates durable servitude non-transfer; medium. |
| 109:3:5 `أَعْبُدُ` | relative-clause object of their non-worship; corroborates speaker's separate object-domain; medium. |
| 109:4:3 `عَابِدٌ` | speaker standing-characterization denied toward their past object; medium. |
| 109:4:5 `عَبَدتُّمْ` | prior addressee servitude-domain tested; medium. |
| 109:5:3 `عَٰبِدُونَ` | repetition confirms durable non-transfer; medium. |
| 109:5:5 `أَعْبُدُ` | repeated speaker object-domain; medium. |

#### Branch `ع ب د B003` worship and obedient submission

| Occurrence | Result |
| --- | --- |
| 109:2:2 `أَعْبُدُ` | main productive seed S109-S1-003; strong. |
| 109:2:4 `تَعْبُدُونَ` | productive reciprocal seed; constructs addressee object-domain; strong. |
| 109:3:3 `عَٰبِدُونَ` | productive standing-state seed; enters S109-S1-004; strong. |
| 109:3:5 `أَعْبُدُ` | productive object-domain seed inside relative clause; strong. |
| 109:4:3 `عَابِدٌ` | productive active-participle seed denying speaker's standing relation to their past object; strong. |
| 109:4:5 `عَبَدتُّمْ` | productive past-practice seed reactivating 109:2 object-domain; strong. |
| 109:5:3 `عَٰبِدُونَ` | productive repetition seed; strong corroboration of stability. |
| 109:5:5 `أَعْبُدُ` | productive repetition seed; confirms speaker domain; strong. |

#### Branch `ع ب د B004` enslaving/subjugating

| Occurrence | Result |
| --- | --- |
| all eight occurrences | retained only as secondary geometry in S109-S1-003 when joined to `د ي ن B004`; constrained by absence of explicit coercive event; weak-medium for each occurrence. |

#### Branch `ع ب د B005` trodden/smoothed path

| Occurrence | Result |
| --- | --- |
| 109:2:2, 109:2:4, 109:3:3, 109:3:5, 109:4:3, 109:4:5, 109:5:3, 109:5:5 | retained as weak S109-S1-008 only through repetition plus `د ي ن B005`; no road/camel/ship complement; weak-medium as a cluster, weak individually. |

#### Branch `ع ب د B006` honored/served person

| Occurrence | Result |
| --- | --- |
| all eight occurrences | weak local alternative: worship can involve honoring/serving an object, but the passage does not supply honor, service-retinue, or honored-person roles; dies as independent seed; weak/unlikely. |

#### Branch `ع ب د B007` strength/hardness

| Occurrence | Result |
| --- | --- |
| all eight occurrences | terminates: no hardness, strength, durable cloth/camel role is supplied by S109; unlikely. |

#### Branch `ع ب د B008` pride/anger/grief at loss

| Occurrence | Result |
| --- | --- |
| all eight occurrences | terminates: a polemical emotional scene could be imagined, but the passage supplies no anger/grief lexemes and closes with domain partition, not emotional loss; unlikely. |

#### Branch `ع ب د B009` little delay / quick running

| Occurrence | Result |
| --- | --- |
| all eight occurrences | terminates: no haste, running, delay, or temporal hurry role; unlikely. |

#### Branch `ع ب د B010` dispersed groups or paths

| Occurrence | Result |
| --- | --- |
| all eight occurrences | weakly echoes final separation but no `عباديد/عبابيد` form or dispersal noun appears; rejected as seed; unlikely. |

#### Branch `ع ب د B011` breakdown/stranding/difficult animal

| Occurrence | Result |
| --- | --- |
| all eight occurrences | terminates: no travel, mount, breakdown, or difficult animal role; unlikely. |

#### Branch `ع ب د B012` perfume mortar

| Occurrence | Result |
| --- | --- |
| all eight occurrences | terminates immediately: no perfume, mortar, pounding, scent, or ritual implement; unlikely. |

### د ي ن occurrence-specific branch passes

| Branch | 109:6:2 `دِينُكُمْ` | 109:6:4 `دِينِ` |
| --- | --- | --- |
| DYN-B001 obedience/religion | productive first half of S109-S1-005; predicts matching first-person domain; strong | productive closure; reactivates all `ع ب د` clauses; strong |
| DYN-B002 reckoning/judgment | rejected in S109-S1-010; no accounting/day syntax; unlikely | same rejection; unlikely |
| DYN-B003 debt | rejected in S109-S1-010; no debt roles; unlikely | same rejection; unlikely |
| DYN-B004 subjugation/ownership | secondary support for S109-S1-003; medium | secondary support for speaker's distinct obedience domain; medium |
| DYN-B005 habit/custom | retained in S109-S1-008 and S109-S1-005; medium | retained as the speaker's distinct custom/domain; medium |
| DYN-B006 city of obedience | terminates: no city/locality/governance noun; unlikely | same; unlikely |
| DYN-B007 certifying/entrusting to one's dīn | productive secondary in S109-S1-005/S109-S1-006; medium-strong | productive secondary: `ولي دين` completes leave-each-to-own-domain image; medium-strong |

## Constructional, Morphosyntactic, and Temporal Seed Ledger

| Seed | Construction | Result |
| --- | --- | --- |
| CON-001 | 109:1 `قُلْ` governing quoted vocative | productive in S109-S1-001; strong. |
| CON-002 | vocative `يَٰٓأَيُّهَا ٱلْكَٰفِرُونَ` | productive address/classification seed; strong. |
| CON-003 | 109:2 negated verbal clause `لا أعبد ما تعبدون` | productive first worship-relation seed; strong. |
| CON-004 | 109:2 internal relative object `ما تعبدون` | productive object-domain seed; strong. |
| CON-005 | 109:3 nominal negation `ولا أنتم عابدون` | productive standing-state reciprocal seed; strong. |
| CON-006 | 109:3 object `ما أعبد` | productive reciprocal object-domain seed; strong. |
| CON-007 | 109:4 nominal first-person negation `ولا أنا عابد` | productive speaker-characterization seed; strong. |
| CON-008 | 109:4 object `ما عبدتم` with perfect | productive past-practice seed; strong. |
| CON-009 | 109:5 repetition of 109:3 | productive reactivation/stabilization seed; strong. |
| CON-010 | 109:6 `لكم دينكم` fronted predicate plus possession | productive final partition seed; strong. |
| CON-011 | 109:6 `ولي دين` fronted predicate plus first-person possession | productive final balancing seed; strong. |
| CON-012 | fourfold `لا` sequence | productive temporal/acoustic seed: denial accumulates before closure; strong. |
| CON-013 | subject alternation I/you/I/you | productive morphosyntactic seed: prevents one-sided reading; strong. |
| CON-014 | `ما` object symmetry | productive structural seed: worship objects remain defined by each side; strong. |
| CON-015 | active participle versus imperfect/perfect alternation | productive in S109-S1-004; strong. |
| CON-016 | final rhyme/repetition of `دين` | local temporal closure; supports S109-S1-005 but does not independently generate lexical content; medium. |

## Image Packet Catalog

### IMAGE-S109-001

Starting seed: `قُلْ` / `ق و ل B001`  
Complete image: a commanded public boundary utterance  
Passage-order assembly: command -> named addressees -> repeated non-participation clauses -> final domain assignment  
Participants and roles: speaker as commanded declarer; addressees as covered/denying group; worship objects/domains as non-shared  
Operation / mechanism: spoken declaration separates domains  
Direction / force / medium: speech projects boundary outward  
Temporal development: first public address, then reciprocal denials, then closure by possessed `دين`  
Outcome / closure: each side has its own dīn  
Exact branch constituents: `ق و ل B001`, `ك ف ر B003`, `ع ب د B003`, `د ي ن B001`  
Unfilled roles: none for the speech-boundary image  
Status: COMPLETE

### IMAGE-S109-002

Starting seed: `ع ب د B003` at 109:2:2  
Complete image: non-transferable worship/servitude relation  
Passage-order assembly: I do not worship your object -> you are not worshippers of my object -> I am not a worshipper of your prior object -> you are not worshippers of my object -> your dīn / my dīn  
Participants and roles: speaker, addressees, object-domains, dīn domains  
Operation / mechanism: repeated negation blocks crossover  
Direction / force / medium: relation from subject to worship object is denied in both directions  
Temporal development: present action, standing characterization, past practice, repeated standing state  
Outcome / closure: durable separation of obedience domains  
Exact branch constituents: `ع ب د B003`, secondary `ع ب د B001/B004`, `د ي ن B001/B004`  
Unfilled roles: no literal ownership transaction; secondary only  
Status: COMPLETE

### IMAGE-S109-003

Starting seed: `د ي ن B001/B007` at 109:6  
Complete image: partition and release to separate domains  
Passage-order assembly: accumulated worship denials -> `لكم دينكم` -> `ولي دين`  
Participants and roles: addressees with their dīn; speaker with his dīn  
Operation / mechanism: lām predicates assign each domain to its holder  
Direction / force / medium: final boundary is possessive/relational, not argumentative  
Temporal development: repeated denials mature into settled partition  
Outcome / closure: no further clause needed after domain assignment  
Exact branch constituents: `د ي ن B001`, `د ي ن B005`, `د ي ن B007`, structural 109:6 a1-a6  
Unfilled roles: none for domain partition  
Status: COMPLETE

### IMAGE-S109-004

Starting seed: `ع ب د B005` and `د ي ن B005`  
Complete image: worn worship path / customary course  
Passage-order assembly: repeated worship root -> prior practice -> repeated denial -> custom/domain closure  
Participants and roles: each side as walker of its own established course  
Operation / mechanism: repetition makes practice feel path-like  
Direction / force / medium: no crossing between courses  
Temporal development: present and past practice become final custom  
Outcome / closure: each retains its customary dīn  
Exact branch constituents: `ع ب د B005`, `د ي ن B005`  
Unfilled roles: no road/camel/ship complement  
Status: FRAGMENT

## Brief Interpretation

The strongest Stage 1 synthesis is not a hidden alternative translation but a secondary relational geometry: a commanded utterance publicly establishes that worship relations do not cross between the speaker and the addressed coverers/deniers. Repetition tests the boundary across action, standing characterization, and prior practice. The final `دين` line closes the avalanche by converting repeated negated worship relations into stable, possessed domains: `لَكُمْ دِينُكُمْ وَلِيَ دِينِ`.
