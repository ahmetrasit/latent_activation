# Global Anchor-Exception Repair Contract

Run only after semantic drafts are complete. Read the collected exception
ledger, cited source excerpts, and the hash-bound complete branch database
snapshot. Resolve only citation identity; do not grade, rewrite, merge, or
reclassify findings.

For each stable `anchor_key`, emit exactly one resolution under
`anchor_repair.json`:

- `resolved` only when one exact existing `root_id` + `branch_id` is justified;
- `unresolved` when identity remains absent or ambiguous;
- `meaning_change` when repair would alter the finding rather than identify its
  citation.

Never invent a root, branch, or database row. A purely identifying `resolved`
repair proceeds to deterministic materialization. `unresolved` blocks final
materialization only for affected surahs. `meaning_change` returns only the
affected ayah to Agent A.

Compute the SHA-256 of the complete assigned exception ledger and copy its
hash-bound branch-database SHA-256 into the two required top-level fields. Do
not repair against a different database snapshot.

Serialize the repair output as canonical compact UTF-8 JSON: one complete
document on one line, separators `,` and `:`, no insignificant whitespace, and
one trailing newline.
