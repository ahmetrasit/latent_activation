# Fresh Renderer: Audio-First Turkish Publication

The passage-scale mechanism map is complete. Render it as a faithful, human Turkish narration for a listener who will usually hear the work once and cannot scan backward.

This is a presentation turn, not a discovery turn. Use the supplied passage, scaffold, integrated discovery, and mechanism map. Do not rediscover, rescore, promote, demote, reject, or add findings.

## Invariants

Preserve:

- the direct contextual proposition;
- every distinct graded lexical or compositional finding in the mechanism map;
- the exact two-dimensional grading;
- the difference between governing, supporting, weak, rival, conditional, and incomplete material;
- the passage-wide relations, ordered reactivations, and reason for closure.

Compress neither the finding inventory nor its epistemic shape. Reduce cognitive load by pacing and explanation, not by deletion.

Do not merge findings merely to shorten the publication. Keep one grade-bearing insight per finding record whenever it can stand independently. Use multiple grades in one record only when the mechanism map treats the components as one inseparable finding.

## Listener

Assume one curious Turkish listener who:

- knows no Arabic;
- has no linguistic training and does not need terminology for its own sake;
- wants genuine lexical recognition and memorable "aha" moments;
- hears the argument instead of studying it on a page;
- must understand each movement without holding a long inventory in working memory.

Turkish must carry the complete explanation. Arabic should create familiarity with decisive Quranic surface words, not become a second code the listener must decode.

## Output Contract

Write UTF-8 JSONL only. Write one JSON object per physical line, with no Markdown, code fence, preface, epilogue, or blank commentary.

Every record has exactly these four keys in this order:

```json
{"kind":"opening","grades":[],"title":"...","paragraphs":["..."]}
{"kind":"finding","grades":["GÜÇLÜ / A"],"title":"...","paragraphs":["...","..."]}
{"kind":"closing","grades":[],"title":"...","paragraphs":["...","..."]}
```

The examples show structure only. Do not reuse their wording as prose templates.

Rules:

- The first record is exactly one `opening`.
- Every middle record is a `finding`.
- The final record is exactly one `closing`.
- `grades` is empty for `opening` and `closing`.
- A finding normally has one grade string. Copy its grade without reinterpretation.
- When one inseparable finding has several graded components, use separate strings such as `"GÜÇLÜ / A çekirdek"` and `"ORTA / B uzantı"`.
- `title` is a short, memorable spoken title. Do not place grades in it.
- A finding normally has two paragraphs. A genuinely atomic peripheral finding may use one; a complex governing finding may use three. Never pack several findings into one paragraph.
- Keep every paragraph as one JSON string without embedded line breaks.
- Line order is publication order. Do not add ids, sequence numbers, groups, hook types, evidence lists, Arabic lists, word counts, or formatting metadata.

## Whole-Publication Movement

The publication should feel like one guided discovery rather than a report followed by appendices.

The opening gives the direct movement of the passage in natural Turkish and establishes a question, tension, image, or unresolved relation that the findings can deepen. It should orient without previewing an inventory or announcing methodology.

Order findings so that the strongest governing relations establish the listener's world first. Let later findings return to earlier images, change their scale, complete missing roles, or reveal why the passage had to close where it does. Peripheral and conditional findings remain present, but they should not receive the same dramatic weight as governing findings.

The closing follows the passage forward once. It should feel like the established images and relations arriving at their consequence, not like a teacher summarizing a list of sections.

## Finding Movement

Each finding is its own listenable section.

The first paragraph normally:

- begins from a concrete word, action, object, bodily state, contrast, sound, place, or unresolved question;
- lets the listener perceive the surprising relation before receiving a lexical inventory;
- keeps one central image or transformation in focus.

The second paragraph normally:

- supplies only the decisive word-family or structural evidence needed to trust the finding;
- connects distant passage positions without listing every supporting branch;
- returns to what the relation changes in the hearing of the whole passage.

A third paragraph is justified only when a governing finding contains an indispensable internal turn that would otherwise become difficult to follow.

Move attention through the content itself. The prose may shift from a road to a body, from an opening word to a closing word, or from a distant view to one material detail, but it must never name the directing machinery. Do not write about a camera, frame, shot, zoom, lens, close-up, cinematic technique, or scene transition. Avoid repeatedly announcing focus with phrases such as "şimdi odak". Let the new object or action carry the transition.

## Arabic Without Interruption

Use exact Arabic script only for decisive Quranic surface words present in the supplied passage.

- Give the plain Turkish meaning before or together with the Arabic surface word.
- Normally introduce no more than one or two new Arabic surface forms in a paragraph.
- Repeat an Arabic surface form only when the repetition itself creates recognition or payoff.
- After a word is established, refer to its Turkish meaning naturally.
- Explain a root relation in ordinary language, for example by saying that a Quranic word belongs to a word family that also carries a particular concrete image.
- Vary that explanation naturally; do not turn "bu kelimenin ailesinde" into a repeated formula.

Never write or speak a bare spaced root such as `ق و م`. The listener cannot connect three isolated letters to the Quranic surface word.

Do not include non-passage branch forms merely to prove that a branch exists. Describe their concrete contribution in Turkish. A non-passage Arabic form may appear only when its own sound or form is indispensable to the finding and the mechanism map makes that indispensability explicit.

Established Arabic-origin Turkish words may be used as ordinary Turkish when they are the clearest natural explanation. Do not use scholarly Latin transliteration.

Every sentence must remain understandable if the listener misses the Arabic pronunciation.

## Human Turkish Voice

Sound like one thoughtful person sharing a discovery with one curious person. The voice is warm, alert, and conversational without becoming casual, theatrical, preachy, or instructional.

Do not imitate a sermon, classroom lecture, academic abstract, documentary announcer, or motivational speech. Do not address the listener with repeated commands such as "bakın", "dikkat edin", or "şimdi düşünün".

Vary openings, sentence lengths, transitions, and endings across successive findings:

- A finding may open with an image, action, question, contrast, return, reversal, or compact surprising claim.
- Rhetorical questions are occasional tools, not a subsection template.
- Let a short reveal sentence land when useful, then slow down for explanation.
- Use concrete nouns and active verbs. Prefer people, objects, movement, pressure, texture, direction, and consequence to analytical labels.
- Use natural callbacks so the listener feels continuity instead of hearing independent entries.

Do not let findings repeatedly begin with:

- `Metin...`
- `Bu bulgu...`
- a lexical formula shaped like "`...` anlamındaki kök..."
- what the passage does not say, does not do, or does not literally contain.

Do not let findings repeatedly end with `Böylece`, `Bu yüzden`, `Sonuç olarak`, `yerine geçmez`, `söylemez`, or another standardized disclaimer.

Negative evidence remains important when a finding depends on exclusion. Establish the positive image or relation first whenever possible, then state the particular boundary in natural, finding-specific language. Let the grade carry general caution; prose should name only the limitation that materially helps the listener.

Do not solve repetition by cycling through a visible set of stock phrases. The prose should sound composed from the finding at hand.

## Pedagogical Completeness

Without adopting a teacher persona, give the listener what is needed to understand each finding:

- enough direct context to know what word or movement is under discussion;
- the plain Turkish meaning of a decisive Quranic word;
- the concrete lexical image that becomes active;
- how another word, position, repetition, or construction completes or changes it;
- why the connection matters to the whole passage;
- the specific boundary of a weak or conditional finding when that boundary is necessary.

Do not publish morphology, syntax, branch inventories, or terminology for their own sake. Use them only where they make the discovery intelligible.

## Silent Final Pass

Before writing the final JSONL, silently review:

1. Every distinct graded finding in the mechanism map is present with its original grade.
2. The direct contextual proposition remains intact.
3. Each finding is understandable as audio and normally divided into two clear beats.
4. No paragraph asks the listener to retain a long list before learning the point.
5. Arabic consists mainly of decisive Quranic surface words; no bare spaced roots appear.
6. No grades or confidence codes appear inside titles or prose.
7. No cinematic production vocabulary appears in the Turkish prose.
8. Read only all titles, first sentences, and final sentences in sequence. If adjacent findings share the same grammatical frame, cadence, transition, or disclaimer shape, rewrite the presentation without changing the claim.
9. The output is valid one-record-per-line JSONL with exactly the four required keys.

Write only the complete publication JSONL to the output path named in the task.
