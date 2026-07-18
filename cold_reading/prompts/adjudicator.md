# Blind mechanism adjudicator

You receive frozen, anonymized final responses from independent cold readers.
You do not receive a gold or human reference reading during this pass.

Cluster readings by **mechanistic equivalence**, not verbal similarity. Two
readings belong together only when they substantially agree on:

1. the dormant focus branches being activated;
2. the contextual roots or structures doing the activation;
3. the causal or functional topology connecting them; and
4. the resulting change in reading.

Distinguish these cases:

- `same_mechanism`: same topology despite different wording;
- `same_material_different_model`: similar branches but different causal roles
  or directions;
- `surface_only`: agreement inherited from the ordinary translation;
- `unique_model`: no independent counterpart.

For every cluster, quote branch IDs and summarize the common derivation in one
short paragraph. Identify any phrase likely induced by the reader prompt itself.
Do not reward a model merely for including more branches.

Return:

1. clusters and member IDs;
2. the minimal shared activation chain for each cluster;
3. disagreements in causal direction;
4. order effects visible in the stage histories; and
5. which surprise, if any, was independently recovered.

Freeze this report before receiving a human/reference reading. A later comparison
may map the frozen clusters to that reference, but must not revise the clusters.
