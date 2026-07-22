# Target-Language Ordinary Baselines

This directory treats the ordinary ayah baseline as a first-class,
language-versioned input to v12 cross-run publication. Turkish is the first
profile, not a hardcoded workflow language.

The layers are independent:

1. `methodology/ordinary_baseline_v1.md` defines the language-neutral
   authorship, alignment, audit, and freeze procedure.
2. `language_profiles/<bcp47>.json` defines tokenizer, orthography, register,
   loanword, and terminology policy for one target language.
3. A baseline artifact conforming to
   `model_schemas/target_language_baseline_v1.json` contains the fixed ayah
   text and compact target-token tuples of the form
   `[surface, [qac_word_ref, ...]]`.

`prompts/author_baseline.md` and `prompts/review_baseline.md` make the authoring
and audit roles reusable across languages. Concrete assignments supply paths,
scope, target language, and output locations without rewriting those prompts.

Adding another language requires a new reviewed profile and baseline artifact.
It does not change the v3 package, publisher, or finalization contracts.

An approved complete artifact is frozen with
`scripts/freeze_target_language_baseline.py`. The freeze manifest binds the
methodology, language profile, Arabic source, QAC database, baseline content,
and structural validation report. Partial pilot manifests are explicitly
noncanonical.

Baseline authors must not read v12 reader outputs, branch inventories, latent
findings, retrospective findings, or existing target-language Quran
translations. The baseline is deliberately ordinary and unsurprising.
Generated artifacts are never hand-edited; corrections change the responsible
workflow input and trigger regeneration.
