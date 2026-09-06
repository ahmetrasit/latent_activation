Continue in this same conversation with the same sealed packet. Discovery is
complete; this is the reporting pass. No new evidence or target readings are
being supplied. Your discovery notes are a record of candidates, not an additional
evidentiary source. Use the original packet to verify the final citations.

Convert the notes into the v1 ledger specified below. Preserve each distinct
candidate's meaning and ID, including competing and exploratory readings. Use
the candidate's `id` as its `model_id` or `outlier_id`. Do not silently merge,
drop, rank down, or replace candidates, and do not start a new discovery round.
Use the existing fields to qualify interpretations without erasing their change
to the focus reading.

If a candidate cannot survive v1's anchoring or changed-reading requirements,
record it in `discarded_or_unchanged` as `ID: specific reason`. Every discovery ID
must occur exactly once, either as a retained finding or in such a withdrawal.
Do not invent a citation to retain a candidate. An unconventional but grounded
reading is not a reason for withdrawal. Put other uncertainties in `summary`.

Return only the final response JSON. The coordinator saves `response.json` and
performs formatting-only compaction; do not call tools or modify files yourself.
The following original v1 reporting sections govern this pass, with compaction
handled by the coordinator as stated above.
