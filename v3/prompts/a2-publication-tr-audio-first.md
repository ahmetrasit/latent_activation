# Fresh Renderer: Gold Synthesis in Audio-First Turkish

The passage-scale mechanism map is complete. Render it as a faithful, human
Turkish publication for a listener who will usually hear the work once and
cannot scan backward.

This is a presentation turn, not a discovery turn. Use the supplied passage,
scaffold, integrated discovery, and mechanism map. Do not rediscover, re-audit,
rescore, promote, demote, reject, or add findings.

## Frozen Synthesis Behavior

Preserve the synthesis behavior of the established gold renderer. The
audio-first contract changes presentation, not intellectual organization.

Compress exposition, not discovery.

Every distinct graded finding that contributes a lexical or compositional
insight must remain visible with its exact two-dimensional grade. Its
supporting observations may appear:

- inside a governing synthesis finding whose force comes from several
  converging observations;
- as an extension within that same finding;
- or as a compact complementary finding when it contributes independently.

Do not equate one grade-bearing observation with one publication record. A
record represents one synthesis finding: a governing channel, axis, ring,
transformation, retrospective activation, rival scene, or genuinely
independent complementary discovery.

Density must come from hierarchy, synthesis-preserving merging, and sentence
economy rather than deletion or atomization.

When several graded observations are extensions of the same governing channel,
merge them rather than giving each a separate record. Preserve their
distinctions with separate strings in `grades`. Related complementary
observations with the same function may also share one compact record. A detail
that merely illustrates an already graded finding belongs inside that finding,
not under another title.

Merging must never silently upgrade, downgrade, omit, or blur an observation.
Conversely, do not split a coherent synthesis merely because its evidence
contains several grades, roots, positions, or images.

The publication may contain multiple channels. Holism does not mean forcing
one total metaphor over the passage. It means that governing findings connect
distant positions, transform earlier wording retrospectively, interact with
supporting or rival channels, and collectively explain sequence and closure.

## Listener

Assume one curious Turkish listener who:

- knows no Arabic;
- has no linguistic training and does not need terminology for its own sake;
- wants genuine lexical recognition and memorable moments of discovery;
- hears the argument instead of studying it on a page;
- must understand each movement without holding a long inventory in working
  memory.

Turkish must carry the complete explanation. Arabic should create familiarity
with decisive Quranic surface words, not become a second code the listener must
decode.

## Output Contract

Write UTF-8 JSONL only. Write one JSON object per physical line, with no
Markdown, code fence, preface, epilogue, or blank commentary.

Every record has exactly these four keys in this order:

```json
{"kind":"opening","grades":[],"title":"...","paragraphs":["..."]}
{"kind":"finding","grades":["GÜÇLÜ / A"],"title":"...","paragraphs":["...","..."]}
{"kind":"closing","grades":[],"title":"...","paragraphs":["...","..."]}
```

The examples show structure only. Do not reuse their wording as prose
templates.

Rules:

- The first record is exactly one `opening`.
- Every middle record is a synthesized `finding`.
- The final record is exactly one `closing`.
- `grades` is empty for `opening` and `closing`.
- Copy every represented grade without reinterpretation.
- When a synthesis finding contains differently graded components, use
  separate descriptive strings such as `"GÜÇLÜ / A çekirdek"` and
  `"ORTA / B uzantı"`.
- Do not create duplicate grade strings. Add a short qualifier when several
  components share the same grade but need separate traceability.
- `title` is short, memorable navigation text. Do not place grades in it.
- A synthesis finding normally has two paragraphs. A genuinely small
  complementary finding may use one; a complex governing finding may use
  three.
- Paragraph division changes pacing only. Never split one synthesized finding
  into several records merely to shorten its paragraphs.
- Aim for roughly 25 to 55 spoken words per paragraph. Prefer a third paragraph
  to a dense inventory, but do not create a new finding.
- Keep every paragraph as one JSON string without embedded line breaks.
- Line order is the canonical synthesis and narration order.
- Do not add ids, groups, tags, hook types, evidence lists, Arabic lists, word
  counts, or formatting metadata. Category and tag indexes are downstream
  views over the completed synthesis and must not influence this turn.

## Publication Hierarchy

The opening gives the direct movement of the passage once and establishes a
question, tension, image, or unresolved relation that the findings can deepen.
Follow the supplied primary scaffold closely for names, titles, roles, and
direct propositions. Do not collapse adjacent titles or replace them with a
more interpretive doctrinal synonym merely to make the opening sound vivid. It
should orient without previewing an inventory or announcing methodology.

Lead with the strongest non-obvious governing coalitions. A governing finding
changes how distant parts of the passage are heard together, establishes a
major channel or axis, performs a strong retrospective transformation, or
materially explains sequence and closure.

Give governing findings enough room to become perceptible and memorable. State
the surprising relation early, use only the decisive lexical joins, and return
to its passage-scale consequence.

After the governing synthesis is established, retain every remaining
independent complementary, weak, rival, or conditional discovery in
proportionate form. The grade already performs much of the general cautionary
work. Add a prose boundary only when it names the particular missing link or
rival interpretation.

Do not organize by ayah, pericope, or local section. Do not produce local
summaries and stitch them together. Use syntax, voice, tense, adjacency, and
repetition inside the lexical coalitions they strengthen. Do not publish them
as standalone findings unless they unlock a non-obvious lexical mechanism.

The closing follows the passage forward once. Carry only transformations
already established so that the interacting field assembles and closes. It
must feel like consequence, not a teacher re-listing prior headings.

## Finding Movement

Each finding is one synthesized, listenable movement.

The first paragraph normally:

- locates the listener in a concrete word, action, object, setting, contrast,
  or unresolved question;
- makes the central convergence perceptible before presenting its evidence as
  an inventory;
- keeps the governing image or transformation in focus.

The second paragraph normally:

- supplies the decisive word-family or structural joins needed to trust the
  synthesis;
- connects distant passage positions without reciting every supporting branch;
- returns to what the convergence changes in the hearing of the whole passage.

A third paragraph is justified when an indispensable turn inside the same
synthesis would otherwise become dense. It must continue the same finding,
not introduce an evidence-sized subsection.

When several words contribute to one finding, stage their arrival. Establish
the concrete image, action, or relation first; then let later contributors
enter as parts of that movement. Do not make the listener hold a list of
source words or abstract lexical labels before the synthesis becomes visible.

Move attention through the content itself. The prose may move from one image to
another, from early wording to late wording, or from a broad relation to one
material detail, but it must never name production machinery. Do not write
about a camera, frame, shot, zoom, lens, close-up, cinematic technique, or
scene transition. Avoid repeatedly announcing the shift of attention.

## Arabic Without Interruption

Use exact Arabic script only for decisive Quranic surface words present in the
supplied passage.

- Give the plain Turkish meaning before or together with the Arabic surface
  word.
- Normally introduce no more than one or two new Arabic surface forms in a
  paragraph.
- Repeat an Arabic surface form only when repetition creates recognition or
  payoff.
- After a word is established, refer to its Turkish meaning naturally.
- Explain a root relation in ordinary language by connecting the Quranic word
  to its concrete word-family image.
- Vary that explanation naturally. Do not replace one repeated
  metalinguistic formula with another.
- Do not announce the word-family relationship every time it is used. Once the
  listener understands the relation, let the concrete image, action, and
  passage position carry later references.
- Metalinguistic carrier labels are exceptional scaffolding, not the normal
  subjects of sentences. Prefer the Quranic surface word, its plain Turkish
  meaning, or the concrete object and action over repeatedly naming a family,
  field, branch, domain, or similar abstraction.
- Do not solve this by rotating among several carrier labels. Across the whole
  publication, repeated lexical scaffolding must give way to direct narration
  through objects, people, movement, texture, position, and consequence.

Never write or speak isolated Arabic root letters separated by spaces. The
listener cannot connect those letters to the Quranic surface word.

Before output, compare every Arabic span directly with the supplied passage
text. Each span must be an exact contiguous substring of that text. Preserve
articles, attached particles, case endings, diacritics, and token order. If an
exact surface form is unnecessary, omit the Arabic rather than normalizing,
shortening, or reconstructing it.

Do not include non-passage branch forms merely to prove that a branch exists.
Describe their contribution in Turkish. A non-passage Arabic form may appear
only when its own sound or form is indispensable to the finding and the
mechanism map makes that indispensability explicit.

Established Arabic-origin Turkish words may be used as ordinary Turkish when
they are common and are the clearest natural explanation. Avoid rare,
specialist, archaic, or theological loanwords when an ordinary Turkish phrase
would be immediately clearer to a listener with no Arabic background. Do not
use scholarly Latin transliteration.

Every sentence must remain understandable if the listener misses the Arabic
pronunciation.

## Human Turkish Voice

Sound like one thoughtful person sharing a discovery with one curious person.
The voice is warm, alert, and conversational without becoming casual,
theatrical, preachy, or instructional.

Do not imitate a sermon, classroom lecture, academic abstract, documentary
announcer, or motivational speech. Do not address the listener with repeated
commands such as `bakın`, `dikkat edin`, or `şimdi düşünün`.

Vary openings, sentence lengths, transitions, and endings across successive
findings:

- A finding may open with an image, action, question, contrast, return,
  reversal, or compact surprising claim.
- Rhetorical questions are occasional tools, not a subsection template.
- Let a short reveal sentence land when useful, then slow down for explanation.
- Use concrete nouns and active verbs. Prefer people, objects, movement,
  pressure, texture, direction, and consequence to analytical labels.
- Use natural callbacks so the listener feels continuity rather than hearing
  independent entries.
- Let lexical evidence enter through what it makes visible or changes. Do not
  repeatedly cast an abstract lexical category as the actor that "contains,"
  "gives," "carries," or "opens" the next item.

Do not let findings repeatedly begin with:

- `Metin...`;
- `Bu bulgu...`;
- a lexical inventory shaped like `... anlamındaki kök...`;
- what the passage does not say, does not do, or does not literally contain.

Do not let findings repeatedly end with `Böylece`, `Bu yüzden`,
`Sonuç olarak`, `yerine geçmez`, `söylemez`, or another standardized
disclaimer.

Negative evidence remains important when a finding depends on exclusion.
Establish the positive image or relation first whenever possible, then state
the particular boundary in natural, finding-specific language. Do not repeat a
generic disclaimer when the grade already carries the necessary caution.

Grades remain metadata. Do not paraphrase a grade as vague spoken confidence
language. State only the concrete missing link, rival reading, or limitation
that changes what the listener should understand.

Do not solve repetition by cycling through a visible set of synonyms. Read the
whole publication for recurring explanatory scaffolds and repeated negative
constructions, then rewrite them from the concrete finding.

Use context-appropriate referents. Do not apply a generic human category noun
to a divine referent when the name, title, grammatical role, or a noun-free
sentence is more natural.

## Pedagogical Completeness

Without adopting a teacher persona, give the listener what is needed to
understand each synthesis finding:

- enough direct context to know what passage movement is under discussion;
- the plain Turkish meaning of decisive Quranic words;
- the concrete lexical images that converge;
- how position, order, repetition, construction, or another word completes the
  relation;
- why the synthesis matters to the whole passage;
- the specific boundary of a weak or conditional component when that boundary
  materially changes the claim.

Do not publish morphology, syntax, branch inventories, or terminology for
their own sake. Use them only where they make the discovery intelligible.

## Silent Final Pass

Before writing the final JSONL, silently review:

1. The governing and complementary hierarchy follows the mechanism map and the
   established gold synthesis behavior.
2. Every distinct graded finding remains represented with its original grade,
   either as a governing synthesis finding or a complementary finding.
3. Observations serving one governing channel have not been atomized into
   separate records merely because they carry separate grades.
4. No synthesis finding has been split to satisfy paragraph length or JSONL
   formatting.
5. The direct contextual proposition remains intact.
6. Each finding is understandable as audio and normally divided into two clear
   beats.
7. No paragraph asks the listener to retain a long inventory before learning
   the point.
8. Arabic consists mainly of decisive Quranic surface words; no bare spaced
   roots appear.
9. Every Arabic span is an exact contiguous substring of the supplied passage
   text, with no normalized or shortened form.
10. No grades or confidence codes appear inside titles or prose.
11. No production vocabulary appears in the Turkish prose.
12. Divine referents are expressed with context-appropriate wording rather
    than generic human category nouns.
13. The opening preserves the supplied scaffold's names, titles, roles, and
    direct propositions without interpretive title substitution.
14. Read every sentence containing metalinguistic carrier language in
    sequence. Keep only what is necessary for comprehension; rewrite recurring
    scaffolding through the concrete image, action, or passage relation.
15. Read all first and final sentences in sequence. Rewrite repeated
    grammatical frames, lexical scaffolds, cadences, transitions, and
    disclaimers without changing the synthesis.
16. The closing is a forward consequence, not a compressed inventory.
17. The output is valid one-record-per-line JSONL with exactly the four
    required keys.

Write only the complete publication JSONL to the output path named in the task.
