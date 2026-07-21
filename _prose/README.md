# Prose Architecture

This folder documents the target prose model for turning latent activation
findings into Turkish user-facing reading layers.

The core principle is:

```text
Ayah first, channel later, evidence underneath.
```

Do not treat the final prose as one monolithic essay. Build a canonical
claim-and-evidence model first, then render different prose layers for different
use cases.

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
   roots, lemmas, branch IDs, v11/v12/v3 provenance, candidate bridges,
   confidence/status, rejected alternatives
   ```

This layer should not be auto-spoken in the normal listening flow.

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
- explanation of how it supports the claim;
- provenance: `v11`, `v12`, `v3`;
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

### v12

Use as the ayah-attached analytical control.

v12 contributes:

- primary ayah thesis;
- fixed-ayah anchoring;
- secondary readings;
- retrospective surprises;
- local context effects.

v12 should be the primary source for `Dinle` and `Derinleş`.

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

Every accepted finding from v11, v12, or v3 must be assigned one placement:

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

4. Do not let v12 ayah anchoring prevent passage-level discovery.

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
