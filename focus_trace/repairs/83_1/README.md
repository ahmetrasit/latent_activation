The 2026-09-06 repair supplies the missing ط ف ف focus inventory in the saved v1
83:1 packet: root_000940 and all ten non-contaminated branches, with full v1 focus
scopes. `original.packet.json` preserves the exact input used by the historical
reader. That historical response has not been regenerated or reclassified.

QAC 83:1:2:3 and frozen-corpus 83:1:3 both assign ط ف ف. The surface bridge failed
because مطففين did not exactly intersect لمطففين, للمطففين, or singular مطفف.
The correction is now derived from quran-data's accepted QAC/MASAQ bridge rather
than a local hand-authored alignment. Its accepted edge connects MASAQ 83:1:3 to
QAC 83:1:2:3; the lexical target is resolved by exact source-root identity.
`build_alignment_repairs.py` verifies CHECKSUMS.sha256, SQLite user_version 4,
the release manifest, the accepted audit, and QAC source identity before producing
[the correction record](../../data/root_mapping_repairs.json). The record pins
the occurrence and source hashes. The packet builders apply it only to the expected unmapped
record and verify the QAC occurrence. Existing mapped/split targets are preserved;
changed unmapped state requires review. This is an HFT-local correction; the
shared quran-data bridge is unchanged.

Run `python3 -B focus_trace/scripts/build_alignment_repairs.py`, then
`python3 -B focus_trace/scripts/repair_83_1_input.py` to reproduce the saved
packet repair. It changes only the affected inventory, mapping, missing-root
entry, and provenance. Sibling historical packets remain frozen; new packets
built through either v1 builder receive the correction automatically.

The separate QAC annotation gap on ويل is not filled by inventing a QAC root.
The context gap on غ م ز at 83:30 also remains explicitly recorded. Neither gap
prevents a branch-backed focus baseline now that ط ف ف is available.
