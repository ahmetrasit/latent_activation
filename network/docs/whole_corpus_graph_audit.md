# Whole-corpus graph feasibility audit

## How the S1 graph is built in `quran-slm`

The S1 graph uses three inputs:

1. `resources/source/quranic_branches_ar.tsv`
   - global branch inventory;
   - 10,820 branch rows;
   - required fields include `node_id`, `source_root_id`, `surface_root_key`,
     `branch_id`, `branch_image_ar`, `what_is_ar`, and `source_phrase_ar`.

2. `resources/derived/s1_branches_ar.tsv`
   - S1 subset of the global branch inventory;
   - 144 branches for the 18 S1 roots.

3. `resources/derived/s1_root_occurrences.tsv`
   - ordered root occurrences in S1;
   - 23 occurrence rows with ayah, root position, word index, surface root,
     surface form, lemma, POS, ayah text, and ayah root sequence.

The semantic branch graph is built by scoring S1 branches against S1 branches
and against the global branch inventory.

The scorer fuses seven relation families:

- `image_image`
- `image_to_scope`
- `reverse_image_to_scope`
- `image_to_source`
- `reverse_image_to_source`
- `whole_scope`
- `source_source`

Each family has lexical and dense ranks, and the final edge score is a
reciprocal-rank fusion with `combined_rank` and `combined_rrf`.

The sparse branch edge license is:

- keep a cross-root branch pair when either direction is inside the configured
  top-k neighborhood;
- current S1 config uses `ks = [3, 5, 8, 12, 20]`;
- same-root edges are excluded.

The occurrence graph is then materialized by taking the Cartesian product of:

- root occurrences in textual order;
- all branch senses for that root;
- licensed cross-root branch edges.

Edges are emitted only within the same surah and only if the target is in the
same ayah or within the configured ayah skip window.

For S1 the graph builder uses `skip_n ∈ {0,1,2}` in search configs, meaning
same-ayah, adjacent-ish, or up to two intervening ayahs.

## What we have for a local whole-corpus build

Available:

- global SLM branch inventory:
  `../quran-slm/resources/source/quranic_branches_ar.tsv`
- Qnet keyword/theme inventory:
  `../quran-roots/_corpus/activation/Qnet/v2/network/incidence_full/branch_keywords.tsv`
  and
  `../quran-roots/_corpus/activation/Qnet/v2/network/bridge_theme_full/branch_theme_inventory.tsv`
- Qnet covers 11,275 branch keys;
- SLM branch inventory covers 10,820 of those keys;
- Qnet-only extra branch keys: 455;
- SLM-only branch keys: 0;
- local dense model exists:
  `../quran-slm/models/multilingual-e5-small`.

Partially available:

- `../quran-roots/_corpus/contextual/sources/noun_occurrences.tsv`
  has 30,558 noun occurrence rows;
- this is not enough for a whole-root graph if verbs/adjectives/other rooted
  tokens should be included.

Available for all surahs:

- surah text JSONs under `../quran-roots/quran/surah_###.json`;
- contextual extraction JSONs for S001–S114.

Missing or not yet confirmed:

- one corpus-wide rooted-token occurrence table equivalent to
  `s1_root_occurrences.tsv`;
- canonical `ayah_root_position` for every rooted token, not just nouns;
- a decision whether to use the SLM 10,820 branch inventory or Qnet's 11,275
  expanded branch inventory as the canonical branch universe.

## Feasibility

We can build our own version here.

The safest first implementation should not copy the full dense SLM scorer.
It should build a corpus-wide occurrence graph from Qnet facets first, because
Qnet already has global branch-level keyword/theme labels.

Recommended local build sequence:

1. Build `network/corpus/v0/resources/branch_inventory.tsv`
   from the SLM branch inventory, optionally enriched with Qnet labels.

2. Build `network/corpus/v0/resources/root_occurrences.tsv`
   from a full rooted-token source.

3. Build `network/corpus/v0/resources/semantic_edges.tsv`
   using Qnet facet overlap with rarity and support thresholds.

4. Materialize per-surah occurrence graphs:
   `network/corpus/v0/output/s###/occurrence_edges.jsonl`.

5. Run the existing v1/v2 compression idea per surah.

6. Only after this works, add an optional dense/lexical SLM-style scorer.

## Main risk

The graph itself is easy.

The hard part is the occurrence layer: if the occurrence table is noun-only, the
whole-corpus graph will silently miss many Qur'anic roots.

## Decision

Proceed, but start with a local `network/corpus/v0` Qnet-facet graph builder and
make the first milestone an occurrence-source audit.
