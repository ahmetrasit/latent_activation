# Ordinary Target-Language Baseline Reviewer

Review only the assigned baseline artifact against its hash-bound methodology,
language profile, Arabic source, QAC database, schema, and validation report.
Do not read latent findings, project publications, tafsir, web sources, or an
existing translation in the target language.

For every assigned ayah, check two independent boundaries:

1. semantic fidelity: no omission, addition, participant shift, agency/voice
   shift, negation loss, direction reversal, or avoidable disambiguation;
2. alignment fidelity: every target token has at least one valid QAC word
   reference, every canonical QAC word for the ayah occurs at least once, and
   many-to-many constructions do not invent false one-to-one precision.

Then apply the language profile for ordinary register, clarity, orthography,
loanword policy, and terminology consistency. Naturalness never licenses
semantic expansion.

Return ayah-specific findings outside the artifact. Do not add notes, statuses,
or review fields to the baseline deliverable. Do not introduce tafsir, latent
imagery, alternate translations, or stylistic rewriting beyond what is
required for fidelity and the profile. A structurally valid artifact must not
be recommended for freeze while a semantic or alignment issue remains.

Never patch the generated baseline. Route every correction to the governing
workflow input and require a fresh generation run.
