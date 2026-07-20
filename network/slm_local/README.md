# SLM-local + Qnet surah adapter

This adapter reads `quran-slm` `surah-local-ar-conditional-v1` bundles and
combines them with existing Qnet branch facets.

It is for S100/S103/S48-style artifacts:

- `../quran-slm/resources/surahs/s###/branches_ar.tsv`
- `../quran-slm/resources/surahs/s###/root_occurrences.tsv`
- `../quran-slm/artifacts/surah_networks/s###/catalog.json`
- `../quran-slm/artifacts/surah_networks/s###/affinity.npy`

It does not modify `quran-slm`.

Run:

```bash
python3 network/slm_local/build_surah_channel_package.py --surah 100
```

Outputs:

- `network/slm_local/output/s###/slm_edges.jsonl`
- `network/slm_local/output/s###/domain_channel_candidates.jsonl`
- `network/slm_local/output/s###/domain_channel_candidates.tsv`
- `network/slm_local/output/s###/summary.json`
