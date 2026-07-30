# Ayah target lists

`build_ayah_neighbors.py` creates a minimal target-ayah list for every numbered
ayah. It does not read packet or pericope definitions.

The target set is the deduplicated union of:

1. the top 50 same-surah candidates under raw NEO symmetric reciprocal-rank
   affinity;
2. exact normalized repetitions in the same surah; and
3. every canonical ayah retained as `strong` or `medium` by
   `../quran-slm/inter-ayah/outputs`.

NEO scores and review labels are used only to construct the set. They are not
written to the consumer artifact. Targets are sorted in canonical Quran order.

Each output has exactly this shape:

```json
{
  "ayah_ref": "2:2",
  "target_ayat": ["2:3", "2:4", "2:5", "3:102"]
}
```

Generate one ayah:

```bash
../quran-slm/.venv/bin/python inter-ayah/build_ayah_neighbors.py --focus 2:2
```

Generate the complete flat collection:

```bash
../quran-slm/.venv/bin/python inter-ayah/build_ayah_neighbors.py --all
```

Outputs use the flat name `inter-ayah/outputs/ayah_<surah>_<ayah>.neighbors.json`.
`collection_manifest.json` is separate build-integrity metadata. A full run
publishes it only after exactly rederiving and comparing all 6,236 target lists.
