The two `pilot-20260906-*-max/83_1` directories are prepared, unrun jobs for
Sol/max and Luna/max. Both use all 36 ayat of S83, identical Arabic packets with
full available scopes and paired variants, the same reader schema, and integration
enabled. The frozen prompts differ only in the model profile. Reader assignments
name the respective profile. English glosses are off in both jobs.

The ط ف ف inventory contains all ten branches resolved through quran-data's
accepted QAC/MASAQ alignment. No reader response, model usage, quality result,
or acceptance is claimed for these preparations. Source snapshots and frozen
implementation hashes are coordinator records; give readers only the rendered
input or the three specified reader files plus their assigned reader ID.

The `compare-20260906-*-max/29_38` jobs completed with the original scope-rich
v3 input. Both passed; see [the comparison](compare-20260906/comparison.md).

The `rerun-20260906-compact-*-max/29_38` jobs are the user-requested compact
rerun. Their context inventory is byte-identical to legacy v1 (171,474 bytes),
and their complete packets are 346,065 bytes. Focus scopes, 69-ayah window,
branch identities, model/effort, and integration-on setting are preserved.
The implementation and prepared jobs must be committed before launching them.
Earlier jobs without a `context_scopes` option retain their frozen scope-rich
behavior and continue to validate.
