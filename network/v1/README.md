# network/v1 — Qnet-enriched review index

Legacy note: this was an S1-only experiment and is not the current production
workflow.

For new runs, use `network/slm_local/`.

This layer uses existing Qnet bridge themes and raw keywords as global facets
for the S1 candidate package.

It does not create a new role ontology.

Inputs:

- `network/output/s1_min5_strong_v0/path_family_candidates.jsonl`
- `../quran-roots/_corpus/activation/Qnet/v2/network/bridge_theme_full/branch_theme_inventory.tsv`
- `../quran-roots/_corpus/activation/Qnet/v2/network/incidence_full/branch_keywords.tsv`

Outputs:

- `output/qnet_enriched_path_families.jsonl`
- `output/compact_review_index.{jsonl,tsv,md}` — grouped by top Qnet theme sequence.
- `output/rare_facet_review_index.{jsonl,tsv,md}` — grouped by existing rare themes plus consensus keywords.
- `output/scored_facet_review_index.{jsonl,tsv,md}` — grouped by existing facets ranked by corpus rarity and path-local branch support.
- `output/image_facet_review_index.{jsonl,tsv,md}` — same as scored facets, but direct worship/theology facets are suppressed to surface image channels.
- `output/theme_specificity.tsv`
- `output/summary.json`

Run:

```bash
python3 network/v1/build_qnet_review_index.py
```
