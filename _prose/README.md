# Prose Architecture

This folder documents the target prose model for turning lexical, dictionary,
ayah-level, and network findings into Turkish user-facing reading layers.

The core principle is:

```text
Ayah first, channel later, evidence underneath.
```

Do not treat the final prose as one monolithic essay, and do not merge every
source into one undifferentiated finding pool. Build a canonical integration
model first, then render different prose layers for different use cases.

## Problem

Current Turkish prose often has two failure modes:

1. It becomes inventory-heavy:

   ```text
   this root shows this, this branch has that...
   ```

   This is traceable, but it disrupts listening and makes the reading feel like
   a lexical report.

2. It becomes too smooth:

   ```text
   a coherent narrative summary
   ```

   This is readable, but it can hide where the secondary reading came from and
   silently drop surprising findings.

The target architecture must preserve discoveries without forcing the listener
to hear root/branch bookkeeping in the primary audio path.

## User-Facing Layers

### 1. Dinle — ayah orientation

Default first-listening layer for a focused ayah.

Purpose:

- make the ayah intelligible on first hearing;
- stabilize the primary reading;
- name the likely point of confusion;
- use only the immediate secondary context needed to clarify or reframe that
  ayah;
- return explicitly to the focused ayah.

This layer should usually avoid root names, branch IDs, technical provenance,
and lexical inventory language.

Target length: roughly 30–60 seconds of spoken Turkish.

Style:

```text
The ayah does X.
The confusing image is doing Y.
Nearby context/secondary activation helps us hear it as Z.
So the focused ayah now reads as...
```

Example style:

```text
“Taş veya demir olun” sözü, insana bunlara dönüşmesini söyleyen bağımsız
bir emir değildir. Önceki itirazı en uç noktaya taşır: Kendinizi canlılığa
en uzak taş kadar, katı ve güçlü demir kadar erişilmez saysanız bile yaratıcı
kudretin dışında kalamazsınız. Böylece ayetin sert imgesi diriliş fikrini
dağıtmaz; itirazın dayanağını ortadan kaldırır.
```

### 2. Derinleş — ayah exploration

Expandable ayah-level prose. Optional audio.

Purpose:

- preserve important secondary readings that are too much for first listening;
- explain how each secondary reading changes the primary reading;
- keep the fixed ayah as the center;
- link the ayah to broader channels when relevant.

Every secondary reading must have an explicit function:

- clarifies an obscure expression;
- reinforces the primary reading;
- adds nuance;
- materially reframes the reading;
- connects the ayah to a broader channel.

This layer should still avoid repetitive root-inventory prose. Several lexical
observations may support one interpretive sentence.

### 3. Kanallar — pericope/surah channels

Surah- or pericope-level narrative section served after individual ayah
readings.

Purpose:

- reveal longer many-ayah-spanning axes;
- show how individual ayat contribute to a broader channel;
- let users navigate from ayah-level readings into surah-level synthesis.

Each channel should have:

- a plain-language title, not a root-based title;
- explicit scope, such as `17:49–52` or `sûre geneli`;
- one-sentence thesis;
- narrated movement through ayat;
- one contribution statement per participating ayah;
- links back to ayah-level claims.

Example structure:

```text
49. ayet itirazı ortaya koyar.
50. ayet onu taş ve demir imgeleriyle en uç katılığa taşır.
51. ayet kaçış için düşünülebilecek başka ihtimalleri de kapsar.
```

### 4. İzini Sür — evidence ledger

Expandable evidence layer.

Purpose:

- preserve traceability;
- keep roots, branches, provenance, confidence, and rejected alternatives
  available;
- prevent the prose layer from becoming a silent filter.

Two levels are useful:

1. Human-readable evidence:

   ```text
   Bu yorum neye dayanıyor?
   ```

   Include focused phrase, supporting ayat, semantic relation, and interpretive
   effect.

2. Technical details:

   ```text
   roots, lemmas, branch IDs, dictionary gloss choices, word-analysis topic IDs,
   v11/v12_cross_run/v3/network provenance, confidence/status, rejected
   alternatives
   ```

This layer should not be auto-spoken in the normal listening flow.

## Integration Model

Each source keeps a distinct job. The prose layer reconciles them; it does not
let one source silently overwrite another.

```text
dictionary    -> target-language gloss policy and branch-safe wording
word_analysis -> per-word reader payoff from curated CRITICAL topics
v12_cross_run -> curated ayah-level findings and publication anchors
slm_local     -> cheap surah/pericope channel candidates and navigation priors
v11           -> high-recall discovery reservoir
neo_inter_surah -> similar-axis checks across other surahs
v3            -> passage synthesis and prose rhythm support
```

The integrator should produce explicit records before prose:

- word-gloss binding: the selected Turkish render/gloss range for each relevant
  word/root/branch, backed by `../dictionary`;
- word-payoff record: the validated `../word_analysis` word prose/topic payoff
  and any ayah-commentary paragraph available for the ayah;
- ayah claim: the accepted v12_cross_run publication finding or baseline
  reading;
- channel claim: reviewed `slm_local`, v11, neo_inter_surah, or v3
  passage/network movement;
- evidence edge: the exact reason two records are allowed to support the same
  rendered claim.

This prevents a Frankenstein artifact: source material is normalized into typed
records, conflicts are surfaced, and prose is rendered only from accepted records.

## Canonical Content Model

Keep prose separate from findings.

### Claim

Fields:

- stable ID;
- assertion;
- scope: `ayah`, `pericope`, `surah`, or `corpus`;
- function: `clarify`, `reinforce`, `nuance`, `reframe`, or `connect`;
- confidence/status;
- public placement:
  - `spoken_core`;
  - `expanded_ayah`;
  - `channel`;
  - `evidence_only`;
  - `deferred_or_rejected`.

### Evidence

Fields:

- exact word or phrase anchor;
- supporting ayah anchors;
- lexical/root/branch relation;
- selected target-language gloss and dictionary entry/projection pointer when
  available;
- word-analysis topic/commentary pointer when available;
- explanation of how it supports the claim;
- provenance: `dictionary`, `word_analysis`, `v11`, `v12_cross_run`,
  `neo_inter_surah`, `v3`, `slm_local`;
- editorial notes and counterevidence.

### Channel

Fields:

- title;
- thesis;
- scope;
- ordered ayah memberships;
- one contribution statement per ayah;
- supporting claim IDs;
- strength/completeness status.

## Workflow Roles

### Dictionary

Use as the target-language lexical authority.

Dictionary entries and projections contribute:

- language-specific selected glosses and contextual glosses;
- concept definitions, branch images, and what-is / what-is-not boundaries;
- loss/addition/collision notes for Turkish render choices;
- term/loanword handling and transliteration policy.

Do not use dictionary entries to create new ayah claims by themselves. They
control wording and lexical boundaries for claims established by v12_cross_run,
word_analysis, or reviewed network evidence.

### Word Analysis

Use as the per-word reader-payoff layer.

`../word_analysis` contributes:

- validated word-level prose for each critical word;
- surviving, narrowed, rejected, and dropped CRITICAL topic decisions;
- local gloss ranges and root gloss ranges;
- ayah-level commentary generated from the validated word output.

Do not treat word_analysis as the same thing as v12_cross_run anchors, QAC
attachments, or `finding_word_branches.tsv`. Those artifacts bind claims to
words. Word_analysis explains what a reader can notice inside each word once
CRITICAL topics have been curated against QAC, attachment, contextual, and V4
evidence.

### v11

Use as the high-recall discovery reservoir.

v11 contributes:

- surprising branch candidates;
- cross-root bridges;
- possible channels;
- weak or exploratory candidates that should not be silently lost.

Do not use v11 Turkish prose as the source of truth. Use source artifacts such
as final reports, mechanism files, secondary expansion files, and discovery
ranking.

### Neo Inter-Surah

Use as the inter-surah similar-axis checker.

Neo inter-surah analysis contributes:

- whether a target surah/pericope channel has similar branch/root/path axes in
  other surahs;
- cross-surah corroboration for a reviewed channel;
- warnings when a proposed local channel is probably a generic corpus pattern;
- navigation candidates from one surah channel to comparable axes elsewhere.

Do not use Neo inter-surah similarity as standalone proof for an ayah reading.
It checks whether an already local claim has corpus relatives. It may strengthen
`Kanallar`, provide `İzini Sür` evidence, or create cross-surah navigation, but
it must not overwrite dictionary wording, word_analysis payoff, or
v12_cross_run ayah claims.

### v12_cross_run

Use as the ayah-attached analytical control.

v12_cross_run contributes:

- primary ayah thesis;
- fixed-ayah anchoring;
- secondary readings;
- retrospective surprises;
- local context effects.

v12_cross_run should be the primary source for `Dinle` and `Derinleş`.

### v3

Use as passage-synthesis and Turkish composition architecture.

v3 contributes:

- pericope/surah channel shape;
- ordering of ayah contributions;
- stronger Turkish rhythm and publication prose;
- whole-passage closure.

Do not use v3 publication prose as an exhaustive discovery source. Prefer
`a2/mechanism-map.md` and `a1/discovery-integrated.md`.

## Coverage Rule

Every accepted finding or source topic from dictionary, word_analysis, v11,
v12_cross_run, neo_inter_surah, v3, or `slm_local` must be assigned one
placement:

```text
spoken_core
expanded_ayah
channel
evidence_only
deferred_or_rejected
```

No finding should disappear merely because it does not fit the first-listening
audio layer.

## Prose Rules

Avoid:

```text
Bu kök şunu gösterir; şu kökte de bu vardır.
```

Prefer:

```text
Ayet bu imgeyle itirazı en uç noktaya taşır.
Bu ifade önceki sorunun sınırını genişletir.
Bu karşılık sûre boyunca süren kanala bağlanır.
```

Rules:

- stabilize the primary reading before introducing surprise;
- begin and end with the focused ayah in ayah layers;
- make scope explicit: `bu ayette`, `yakın bağlamda`, `sûrenin ilerleyen
  bölümünde`;
- give every secondary observation an interpretive job;
- keep root/branch evidence expandable unless it is essential for the listener;
- use uncertainty language consistently:
  - `gösterir`;
  - `destekler`;
  - `çağrıştırabilir`;
  - `olası bir yankı`;
- preserve surprising findings by moving them to the right layer, not by
  deleting them.

## Pushback / Risks

1. Do not try to make the first-listening ayah prose exhaustive.

   If `Dinle` tries to preserve every surprise, it will become disorienting.
   Completeness belongs in `Derinleş`, `Kanallar`, and `İzini Sür`.

2. Do not let v3-style smoothness erase evidence.

   v3 is useful for synthesis and Turkish flow, but every accepted finding must
   still receive an explicit placement.

3. Do not let v11 novelty automatically enter spoken prose.

   A v11 surprise should enter `Dinle` only if it helps the user understand the
   focused ayah. Otherwise it belongs in a channel or evidence layer.

4. Do not let v12_cross_run ayah anchoring prevent passage-level discovery.

   Some findings are real only at pericope/surah scale. They should be served as
   channels, not forced into one ayah.

5. Navigation is not another long prose layer.

   Navigation should be bidirectional linking:

   - ayah → relevant channels;
   - channel → participating ayat and claim IDs;
   - claim → evidence.

6. Coverage must be auditable.

   The system needs a coverage audit that checks whether each accepted finding
   has been surfaced, linked, or deliberately deferred/rejected with a reason.
