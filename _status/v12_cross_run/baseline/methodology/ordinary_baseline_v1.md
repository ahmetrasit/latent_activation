# Ordinary Target-Language Baseline Methodology v1

## Objective

Create one fixed, concise, ordinary target-language rendering for every
canonical Quran ayah. The baseline stabilizes the direct proposition against
which v12 contextual root activations are expressed as additions or changes.
It is not tafsir, lexical exploration, or a destination for latent findings.

## Separation boundary

The author may use only the frozen Arabic source, its QAC word/morpheme record,
the reviewed target-language profile, and ordinary competence in Arabic and
the target language. A separately declared non-target control translation may
be used during fidelity audit only; it is never wording authority.

The author must not read branch inventories, v12/v11/v3 findings, retrospective
surprises, prior project publications, tafsir, web sources, or existing
target-language Quran translations. A baseline produced across that boundary
is invalid rather than merely lower confidence.

## Rendering standard

For each ayah:

1. preserve speaker, addressee, participants, agency, voice, negation,
   direction, sequence, number, and explicit relations;
2. state only the ordinary contextual proposition;
3. prefer minimally interpretive, ordinary modern language;
4. preserve ambiguity when the target language permits it;
5. when unavoidable, choose the least committal fluent construction and mark
   it for editorial review;
6. add no commentary, explanatory parenthesis, latent image, or alternative
   reading;
7. follow the target-language profile rather than a universal loanword policy.

The baseline should be deliberately unsurprising. Stylistic elegance never
licenses an addition or omission.

## Target tokenization and QAC mapping

Normalize baseline text to Unicode NFC. Tokenize deterministically under the
language profile. Target tokens cover orthographic words; punctuation remains
in `baseline_text` but is excluded from `target_tokens`. Internal apostrophes
or hyphens follow the profile. Array position is the token index, so no target
token ID, index, or character span is stored.

Each token is the compact tuple `[surface, [qac_word_ref, ...]]`. The first
member is copied from the baseline text. The second contains one or more
canonical QAC word references that license that Turkish word in context.
Many-to-many alignment is represented directly: a QAC word may recur on
several target tokens, and one target token may cite several QAC words. Do not
force a one-to-one gloss.

Do not store alignment groups, QAC morpheme references or dispositions,
statuses, rationales, or notes. They are not consumed by v12 publication,
whose anchors use QAC word references, root IDs, and branch IDs.

## No-orphan QAC invariant

For every canonical ayah, derive the complete expected QAC word set from the
frozen database. The union of token tuples must equal that set—no omitted or
foreign QAC word reference. Every target token has at least one reference.
Duplicate use across different target tokens is valid when a construction is
distributed. Duplicate IDs inside one token tuple are invalid.

Morpheme coverage is intentionally not encoded here. Morphology remains in the
QAC source and v12's mechanical linguistic bindings; copying it into the
translation baseline would add tokens without serving a downstream consumer.

## Synthetic Basmalah

QAC has no ayah-zero identifiers. The canonical Basmalah baseline and alignment
are authored once at `1:1`. Synthetic `N:0` package rows explicitly alias that
baseline and its canonical `1:1:*` QAC references. No `N:0` QAC ID is invented.
S9 has no synthetic Basmalah row.

## Authorship and audit passes

1. Author ayat in surah order and save incremental checkpoints outside the
   deliverable.
2. Run structural validation after every checkpoint: target token identity,
   referential integrity, exact QAC word coverage, and no-orphan rules.
3. Reread each ayah against Arabic/QAC for omissions, additions, participants,
   voice, negation, pronouns, and relation direction.
4. Apply the language profile for clarity, consistency, and register without
   expanding meaning.
5. Resolve every review finding outside the artifact before canonical freeze.
6. Freeze the Arabic, QAC database, language profile, artifact, and methodology
   hashes together. A change to any one creates a new baseline treatment.

Mechanical validity is necessary but not sufficient. A generated baseline is
not canonical until its pilot wording and editorial policy are approved.

## Generated-artifact boundary

Generated baseline artifacts are immutable outputs. Never repair one by hand.
When review or validation finds a problem, correct the responsible workflow
input—prompt, language profile, schema, validator, assignment, or frozen
source—and regenerate the affected scope. The regenerated artifact replaces
the rejected output as a whole.
