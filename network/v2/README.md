# network/v2 — channel stability scorer

Legacy note: this was an S1-only consolidation experiment and is not the current
production workflow.

For new runs, use `network/slm_local/`.

This layer tests whether v1 review groups compress into stable channel
candidates.

It is not another broad candidate generator.

Inputs:

- `network/v1/output/image_facet_review_index.jsonl`

Outputs:

- `output/channel_candidates.jsonl`
- `output/channel_candidates.tsv`
- `output/domain_channel_candidates.jsonl`
- `output/domain_channel_candidates.tsv`
- `output/low_stability_or_noise.tsv`
- `output/summary.json`

Core rule:

- build channels from existing Qnet facets only;
- require multi-branch facet support before a facet can anchor a channel;
- score each candidate by coverage, coherence, ayah span, root diversity,
  root-ablation stability, facet-ablation stability, and noise penalty.

Two views are produced:

- `channel_candidates.*` is the raw unsupervised facet-component view; it is
  kept mainly as a failure diagnostic because broad co-occurrence can still
  over-merge.
- `domain_channel_candidates.*` is the stricter review input; it uses existing
  Qnet facet strings grouped by transparent term gates, then applies the same
  stability tests.

Run:

```bash
python3 network/v2/score_channel_stability.py
```
