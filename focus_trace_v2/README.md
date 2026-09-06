# Hermetic Focus Trace v2

An isolated workflow under `focus_trace_v2/`; the original `focus_trace/` and
prose_generation V5 are unchanged. The workflow remains **one packet → one reader
→ one response**. Preparation, validation, and export are offline. They never
launch a model, retry a reader, or automatically promote results.

## Restored v1 reader contract

The working discovery prompt and response schema are byte-for-byte copies of:

- `focus_trace/prompts/focus_trace_hermetic.md`
- `focus_trace/schemas/focus-trace-response.schema.json`

New preparation checks this equality before creating a job. It restores v1's
discovery-first posture, focus-only baseline, root-led contextual activation,
competing readings, outliers, before/after changes, confidence and delta states,
and discovery-oriented summary. There is no v2 semantic rewrite or extra
qualification requirement layered over that contract.

The unchanged template defaults to **gpt-5.6-sol / max**. An explicitly requested
comparison profile changes only the prompt's `model` / `reasoning_effort` block;
all discovery instructions remain identical. The frozen prompt and requested
launch profile must agree. No service tier is specified, and preparation does
not authorize a model run or fallback.

The packet again presents `focus_ayah`, `focus_branch_inventories`,
`context_ayat`, and `context_root_cues`. Focus inventories follow focus-root
order; context cues follow first occurrence in the context, excluding roots
already available through the focus inventory. Every mapped target is retained.

## Data fixes remain

Both focus and context retain full paired Arabic images/scopes, English glosses,
and every distinct non-contaminated source variant. No linguistic data is trimmed
to fit a model. Full QAC occurrences, distinct mapped root forms, and source gaps
are preserved. The original source snapshot remains coordinator-only.

The restored packet uses v1's grouped-target layout, not its old lossy lean
projection. In particular, **do not run the old lean-packet validator**, which
forbids the restored English fields. Use the v2 validator below; it compares the
reader packet against the complete frozen source projection. The response schema
and response semantics are v1, including its branch-backed context requirement.

Source paths, mapping ranks, coverage counters, hashes, and execution records
stay outside the linguistic packet. V1's packet protocol and QAC-gap markers are
retained for compatibility. A QAC gap does not establish morphological
rootlessness. The required response `protocol` and assigned `reader_id` follow
the original response contract; readers are not asked to echo input hashes.

V1 citations name a mapped root and branch, not a selected source variant.
Exports therefore retain **all source variants belonging to that citation** and
the reader's explanation. They never silently select the first variant. V1's
free-text structural cues are preserved verbatim, without inventing exact
machine-resolved quotations or references.

### Known strict-v1 limitation

A rooted focus with no branch inventory cannot satisfy v1's required
branch-backed baseline. Preparation stops explicitly in that case rather than
inventing a branch, borrowing context into the baseline, or calling the focus
rootless. **83:1 currently hits this limit because ط ف ف has no mapped target.**
Furuq already contains its ten non-contaminated branches (`root_000940`), but the
upstream bridge misses the QAC/frozen-corpus surface match. This is disconnected
existing evidence, not an absent lexical entry. Repairing the upstream bridge
needs a separate decision; the completed 83:1 comparison artifacts are unchanged.

## Prepare a new job — offline

From the repository root:

```bash
python3 focus_trace_v2/workflow.py prepare --ayah 29:38 --run v1-compatible-sol
python3 focus_trace_v2/workflow.py validate focus_trace_v2/runs/v1-compatible-sol/29_38 --inputs-only
```

Preparation reuses only the legacy packet's window and non-citable remote
orientation, never its reader response. It rebuilds citable evidence from current
resources. Alternatively supply `--window 29:1-69` or `--window-from PATH`.
Sources must remain stable during preparation. Existing job directories are
never overwritten, including partially prepared jobs; use a new run name.

New jobs use `hft-v2-job-v3` and freeze the paths named by the original prompt:

```text
prompt.md
focus_trace_packet.json
focus_trace/schemas/focus-trace-response.schema.json
```

The coordinator-only files are `job.json` and `source.packet.json`. The output
is `response.json`. The coordinator supplies the assigned `reader_id` from the
job when launching a reader.

## Run only with explicit generation approval

Give a fresh-context reader only its frozen prompt, packet, schema, assigned
reader ID, and output path. Never show prior outputs, gold readings, coordinator
interpretations, or other readers' work. Deliver the complete packet; page
through it with existing read-only tools if necessary. Check actual context fit
including instructions and output allowance. Do not shrink linguistic evidence.

The optional inline launcher delivers the same complete frozen files, pins
the requested model and effort, omits a service tier, and disables unrelated tools:

```bash
python3 focus_trace_v2/run_inline_reader.py focus_trace_v2/runs/v1-compatible-sol/29_38 --inspect
# Omit --inspect only after generation is approved.
```

`--inspect` makes no model call and writes no files. In inline mode the model
returns JSON and the coordinator performs v1's formatting-only compaction.
The original model text remains in the event log. Malformed JSON is not repaired;
there are no automatic semantic retries. Launch settings, input hashes, runtime
events, and completion status remain outside the semantic packet.

After an approved reader finishes:

```bash
python3 focus_trace_v2/workflow.py validate focus_trace_v2/runs/v1-compatible-sol/29_38
python3 focus_trace_v2/workflow.py export focus_trace_v2/runs/v1-compatible-sol/29_38
```

Validation checks the frozen hashes, complete source projection, original response
schema, focus-only baseline citations, real branch-backed context triggers, and
exact occurrence/root/branch identities. It does not grade interpretation.
Export retains the entire response and resolves every branch citation to its
complete source variants. It refuses to replace differing evidence.

The receipt's `execution_verified: false` records that requested settings and
hashes are not proof of model execution. Keep actual runtime records separately.
Do not copy an older response into a new job or relabel an old result as a new run.

## Existing jobs and integration

Frozen `hft-v2-job-v1` and `hft-v2-job-v2` jobs still use their own original
packet, prompt, schema, and response contracts. Changing the working templates
does not rewrite or invalidate them. All 20 completed comparison responses and
their evidence exports remain unchanged. Their findings describe the earlier
v2 prompt, **not** the restored v1 prompt.

The original v1 files, production runs, and V5 loader/defaults are untouched.
The new evidence export is still an opt-in future integration boundary; it is not
automatically consumed by prose_generation V5.

## Offline verification

```bash
python3 -B -m unittest discover -s focus_trace_v2/tests -v
```

Tests cover original prompt/schema equality, new v1-compatible preparation and
responses, full linguistic retention, split targets and variants, rootless
annotation rules, the explicit 83:1 limitation, citation failures, model-profile
conflicts, no-overwrite behavior, original v1 response-validator compatibility,
and byte-identical regeneration of all 20 existing evidence exports. Synthetic
test responses are not model output or quality evidence.
