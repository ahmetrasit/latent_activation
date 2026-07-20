# Methodology notes

## Problem

The S1 semantic network has real signal, but raw traversal produces too many
paths. The task is therefore not only ranking paths; it is consolidating many
paths into reviewable candidate groups.

## Recommended structure

### 1. Weighted graph filter

The occurrence graph stores semantic edges as present/absent. The score artifact
adds numeric strength:

- `combined_rank`
- `dense_rank`
- `lexical_rank`
- `combined_rrf`
- family-level dense/lexical scores

The current default strong-edge rule is:

```text
keep if best combined_rank <= 8
OR mutual combined_rank <= 12
```

This preserves strong asymmetric matches while retaining reciprocal evidence.

### 2. Ayah-span filter

Use two standard packages:

- `min_ayahs = 5`: major full-surah channels.
- `min_ayahs = 3`: secondary/subchannel findings.

A `min_ayahs = 5` package intentionally excludes local findings. It is a
seriousness filter, not a truth filter.

### 3. Candidate consolidation

Review groups, not raw paths.

Candidate types:

- atomic branch relation inventory;
- ordered path-family candidates;
- root-set channel seeds.

The review agent should merge/split these into semantic findings/channels.

### 4. Review questions

For each candidate:

1. Is this a coherent finding, primary-reading support, structural relation, or
   noise?
2. Which branch roles are essential?
3. Which nodes are generic connectors?
4. Should this merge with another candidate?
5. What label applies: `PRIMARY`, `INTERESTING`, `STRUCTURAL`, `WEAK`,
   `REJECT`, `SPLIT`, or `MERGE`?

## Current limitations

- Structural findings such as ring architecture are not fully represented by
  branch proximity.
- Generic high-degree roots can dominate packages.
- A root-signature group is not automatically a semantic finding.
- Small valid local findings may be removed by high ayah-span thresholds.
