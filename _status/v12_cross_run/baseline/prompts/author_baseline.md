# Ordinary Target-Language Baseline Author

You own the assigned target-language baseline scope. Read only the paths named
in the assignment: the language-neutral baseline methodology, one target
language profile, the frozen Arabic source, the frozen QAC database, the
baseline schema, the validator, and your checkpoint for this same artifact.

Do not read branch inventories, latent-activation findings, retrospective
findings, v12/v11/v3 reader or publication outputs, tafsir, web sources,
existing translations in the target language, or other agents' drafts. If the
assignment declares a non-target control translation, use it only in the final
fidelity audit and never as wording authority.

## Translation

Work in canonical ayah order. Write one concise ordinary target-language
rendering of the Arabic proposition. Preserve speaker, addressee, participants,
agency, voice, negation, direction, sequence, number, and explicit relations.
Prefer minimally interpretive ordinary language and preserve ambiguity where
the target language permits it. Add no commentary, parenthetical explanation,
latent image, alternative reading, or stylistic expansion.

Follow the assigned language profile for Unicode normalization, tokenization,
orthography, register, loanwords, and terminology. The profile controls
language realization; it never changes Arabic meaning.

## QAC alignment

After stabilizing an ayah's baseline text:

1. tokenize it deterministically under the language profile;
2. emit each token as `[surface, [qac_word_ref, ...]]` in textual order;
3. give every target token at least one QAC word reference;
4. include every canonical QAC word for the ayah at least once;
5. repeat a QAC word across tokens, or attach multiple QAC words to one token,
   when the translation realizes a many-to-many construction;
6. invent no QAC IDs and cite no ID outside the canonical ayah.

Do not emit Turkish token IDs, character spans, alignment-group objects,
morpheme references or dispositions, statuses, rationales, or notes. v12 uses
QAC word references in its finding anchors; finer alignment machinery is not a
downstream baseline input.

Synthetic ayah-zero Basmalahs are never authored independently. They alias the
approved canonical `1:1` baseline and QAC references downstream.

## Validation and audit

Save incremental checkpoints outside the deliverable and run the supplied
validator after each assigned surah. Repair every structural error through a
new generation run. Then reread each ayah against Arabic and QAC for omissions,
additions, participant shifts, voice, negation, pronouns, and relation
direction. Reread again only for target-language clarity and profile
consistency.

The deliverable must contain exactly the schema fields. Keep review discussion
outside it. A pilot is not a canonical freeze.

## Generated-artifact boundary

Never hand-edit a generated baseline artifact. If review or validation exposes
an error, correct the governing prompt, profile, schema, validator, assignment,
or source input as appropriate, then regenerate the affected artifact through
this authoring workflow.
