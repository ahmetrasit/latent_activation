# Follow-up Renderer: Frozen Gold Synthesis to Audio-First Turkish

Continue the same agent session that produced the supplied synthesis master.
The intellectual work is complete. Convert that frozen master into a faithful,
human Turkish publication for a listener who will usually hear the work once
and cannot scan backward.

This is a rendering pass, not a second synthesis pass. Do not return to the
discovery notebook or mechanism map, even if they remain in session context.
Do not rediscover, re-audit, rescore, promote, demote, add, omit, merge, split,
or reorder findings.

## Frozen Source Contract

The synthesis master is the sole authority for:

- the direct contextual proposition;
- the governing and complementary hierarchy;
- finding boundaries and order;
- every grade;
- every lexical convergence, limitation, and passage-wide consequence.

Conversation memory may help you understand the master, but it may not replace
or amend the written artifact.

The compact master normally contains:

1. a title and contextual opening;
2. `## Ana Bulgular`, with headed governing findings;
3. `## Tamamlayıcı Bulgular`, with compact grade-bearing findings;
4. `## Son Geçiş`, with the forward closing replay.

Treat each grade-bearing governing or complementary unit as exactly one
finding. A composite grade label still belongs to one finding. Preserve all of
its grade components in that record's `grades` array.

Paragraph division changes listening pace only. It never creates a new finding.
Do not combine two master findings because their images overlap, and do not
divide one master finding because it contains several roots, grades, objects,
or turns.

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
- Every middle record is a `finding`.
- The final record is exactly one `closing`.
- `grades` is empty for `opening` and `closing`.
- Copy every grade from the corresponding master unit without reinterpretation.
- Split a composite label into separate descriptive grade strings when needed
  for traceability, without changing either grading dimension.
- Do not create, duplicate, or remove a grade.
- Preserve master finding order.
- `title` is short spoken navigation text. It may be recast for clarity, but it
  must name the same finding and must not contain grading language.
- A finding normally uses two paragraphs. A small complementary finding may use
  one; a dense governing finding may use three.
- Aim for roughly 25 to 55 spoken words per paragraph.
- Keep every paragraph as one JSON string without embedded line breaks.
- Do not add ids, groups, tags, evidence lists, Arabic lists, word counts, or
  formatting metadata.

## Recomposition, Not Compression

Read each frozen finding for four things:

1. the discovery or image the listener should perceive;
2. the minimum lexical or structural evidence needed to trust it;
3. the passage movement or distant join that activates it;
4. the exact boundary that prevents overreading.

Then write the finding anew in listener order. Do not edit the dense master
sentence by sentence, preserve its academic syntax, or retain its inventory
shape merely because the facts are already present.

The first paragraph normally makes the finding visible through a concrete
object, action, person, movement, texture, pressure, contrast, or unresolved
relation. Let the reveal arrive before a list of contributing words.

The second paragraph supplies the decisive grounding and returns to what the
finding changes in the hearing of the passage. A third paragraph is justified
only when an indispensable turn in the same finding would otherwise become
dense.

When several words contribute, stage their arrival. Keep one governing image
or transformation in view while later words enter as parts, forces, positions,
or consequences. The listener must never retain a lexical inventory before
understanding the point.

## Arabic Without Interruption

Use Arabic script selectively for decisive Quranic surface words present in the
supplied passage.

- Give the plain Turkish meaning before or together with the Arabic word.
- Normally introduce no more than one or two new Arabic surface forms in a
  paragraph.
- Repeat a form only when repetition creates recognition or payoff.
- After a form is established, refer to its Turkish meaning naturally.
- Every sentence must remain understandable if the listener misses the Arabic
  pronunciation.

Never write isolated Arabic root letters. Do not speak roots, branch ids,
non-passage branch forms, morphology labels, or scholarly transliteration.
Describe their contribution in Turkish.

Before output, compare every Arabic span directly with the supplied passage.
Each span must be an exact contiguous substring, preserving articles, attached
particles, endings, diacritics, and token order. If an exact form is
unnecessary, omit the Arabic rather than normalizing or reconstructing it.

## Keep Bookkeeping Silent

Grades, evidence provenance, and synthesis taxonomy are not spoken content.

Do not narrate generic categories for word families, semantic fields, roots,
branches, domains, lexical environments, mechanisms, governing status,
complementary status, evidence distance, activation, or confidence.

Do not translate grades into listener-facing descriptions such as strong,
medium, weak, near, remote, or conditional. When a limitation matters, state
the concrete missing surface role, competing reading, or interpretive boundary.

When a word relationship must be explicit, connect the Quranic surface word to
the concrete image in one natural clause, then continue through the image,
action, passage position, and consequence. The listener should hear the
discovery, not its filing system.

## Human Turkish Voice

Sound like one thoughtful person sharing a discovery with one curious person.
The voice is warm, alert, and conversational without becoming casual,
theatrical, preachy, instructional, or imitative of a named speaker.

Use immediately clear everyday Turkish. Avoid rare, archaic, specialist, or
theological loanwords when an ordinary phrase would be clearer to a listener
with no Arabic background.

Create movement through the content itself. Attention may pass from early words
to late ones, from a broad relation to one material detail, or from one image
to its consequence. Never mention a camera, frame, shot, zoom, lens,
close-up, cinematic technique, or scene transition.

Vary finding openings, sentence lengths, transitions, and endings. A finding
may open with an image, action, contrast, return, reversal, question, or compact
surprising claim. Rhetorical questions are occasional tools, not a template.

Do not let successive findings repeatedly begin with:

- the passage or text as grammatical subject;
- a word inventory;
- a negative disclaimer;
- the same discovery formula.

Do not let findings repeatedly end with a stock conclusion or disclaimer.
State positive force first whenever possible, then give only the
finding-specific boundary that materially matters.

Use natural callbacks so the listener feels one developing publication rather
than unrelated entries. Do not turn the closing into a recap of headings.

## Direct Foundation

Follow the supplied primary scaffold closely for names, titles, roles, and
direct propositions. The opening may create tension or a hook, but it must not
replace direct titles with interpretive synonyms or preview an inventory.

The closing follows the passage forward once, using only transformations
already present in the synthesis master. It should feel like consequence and
arrival, not like a teacher's summary.

## Silent Mapping Pass

Before writing, silently make a one-to-one ledger:

- opening source;
- every grade-bearing master unit in order;
- all grade components belonging to each unit;
- closing source.

After drafting, silently verify:

1. Every ledger unit has exactly one output record.
2. No unit was merged, split, added, omitted, reordered, or rescored.
3. Every finding retains its discovery, decisive evidence, consequence, and
   material boundary.
4. Paragraphs are listenable and do not begin with an inventory.
5. No bare roots or non-passage Arabic forms remain.
6. Every Arabic span is an exact passage substring.
7. No grade, confidence paraphrase, lexical filing label, mechanism taxonomy,
   or production vocabulary remains in titles or prose.
8. First and final sentences do not fall into a repeated grammatical pattern.
9. The JSONL has exactly the required keys and one object per physical line.

Write only the complete publication JSONL to the output path named in the task.
