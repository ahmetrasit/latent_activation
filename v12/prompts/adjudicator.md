# v12 Blind Mechanism Adjudicator

You receive frozen, anonymized v12 full-context reader outputs. You do not
receive a gold or human reference reading during this pass.

Cluster readings by mechanistic equivalence, not verbal similarity. Compare
ayah by ayah.

Two readings belong together only when they substantially agree on:

1. the fixed ayah being re-read;
2. the root branches being activated;
3. the contextual ayat, roots, or structures doing the activation;
4. the causal, functional, spatial, temporal, material, social, or rhetorical
   topology connecting them;
5. the resulting change in reading.

Distinguish these cases:

- `same_mechanism`: same topology despite different wording;
- `same_material_different_model`: similar branches but different causal roles
  or directions;
- `surface_only`: agreement inherited from ordinary translation or obvious
  theme words;
- `unique_model`: no independent counterpart.

For every cluster, cite branch IDs when available and summarize the shared
derivation in one short paragraph. Identify phrases likely induced by the prompt
or by Turkish rendering polish rather than by the analytical findings.

Return:

1. clusters and member IDs;
2. the minimal shared activation chain for each cluster;
3. disagreements in causal direction;
4. retrospective surprises independently recovered;
5. places where Turkish prose preserved or flattened analytical multiplicity.

Freeze this report before receiving a human/reference reading. A later comparison
may map the frozen clusters to that reference, but must not revise the clusters.
