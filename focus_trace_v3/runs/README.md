# Archived HFT v3 experiments

**HFT v3 failed and is retired. Continue with [v1](../../focus_trace/README.md).**
See the [HFT status decision](../../focus_trace/STATUS.md). Prepared, unrun jobs
are archived preparations, not pending work; the reports preserve historical
results and hypotheses.

The final [repeated 29:38 comparison](discovery-control-20260906/comparison.md)
contains two fresh Sol/max samples each for v1, compact v3, and revised v3.
All six usable outputs passed validation, but the revision traded recoveries for
other omissions and did not establish an overall improvement. HFT continues with v1.

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
The implementation and prepared jobs were committed as `4648eb29` before launch.
Both readers completed and passed without repair; see the
[compact rerun comparison](rerun-20260906-compact/comparison.md).
Earlier jobs without a `context_scopes` option retain their frozen scope-rich
behavior and continue to validate.
