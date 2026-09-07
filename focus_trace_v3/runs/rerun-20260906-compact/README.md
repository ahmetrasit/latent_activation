# Compact-context 29:38 rerun

Requested by the user after the scope-rich comparison, with an explicit commit
before either new model call. These fresh Sol/max and Luna/max readers use a
context inventory byte-identical to legacy v1: 171,474 bytes. Their complete
346,065-byte packets retain all 69 ayat, all 1,993 branches, and complete focus
scopes. Integration stays on and English stays off.

The only intended workflow changes from the preceding v3 run are the compact
context projection and its necessary citation instructions: context branch keys
are formed from the target ID and branch ID instead of being repeated on every
branch. The final reader and ledger schemas are unchanged. This introduces a
small identifier-composition difference as well as removing context scopes;
the rerun is not a perfectly isolated scope-only ablation.

The full source snapshot remains coordinator-only. No previous findings or
comparison hints are sent to the readers. `launch.py` records the commit and
working-tree status before either run. No fallback, follow-up, semantic repair,
service-tier override, or automatic retry is configured.

Prepared jobs:
- [Sol](../rerun-20260906-compact-sol-max/29_38/job.json)
- [Luna](../rerun-20260906-compact-luna-max/29_38/job.json)

Both readers completed and passed without repair. See the
[comparison](comparison.md), [runtime audit](runtime.json),
[input audit](input-audit.json), and [validation](validation.json).
