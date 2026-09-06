# Hermetic Focus Trace v2

An isolated replacement candidate, not a change to `../focus_trace/`. The workflow
is still **one packet → one reader → one response**. No ensemble, staged reveals,
automatic frontier escalation, or automatic corpus rerun. Preparation, validation,
and export are offline, standard-library Python commands; none launches a model.

## What changed

- One source projection for focus AND context: full Arabic images/scopes, paired
  source variants, all mapped targets, and brief missing-inventory notices.
  English glosses are retained. Each mapped inventory appears once, and only
  exactly repeated source rows are deduplicated. Distinct root forms are preserved;
  identical root labels and normalized duplicates of ayah text are not repeated.
- Reader inputs contain linguistic evidence and the minimal citation identifiers,
  not source paths, mapping ranks/dominance flags, match totals, coverage counts,
  technical failure codes, hashes, or reader/run IDs. The complete source snapshot
  and all audit metadata remain available to the coordinator, not to the reader.
- Text-backed baselines and structural-only context deltas are legal. All retained
  findings need an exact focus-text anchor. Exploratory and competing readings
  remain first-class; deterministic validation does not judge semantic quality.
- The coordinator freezes and hashes packet, prompt, schema, and source snapshot.
  It attaches input identity and reader/run bookkeeping to the evidence export;
  the reader neither receives nor echoes that metadata.
  Every retained citation is resolved in the export, including context branches,
  with no ranking or pruning. Old responses are not retroactively bound or repaired.
- Coordinator default: `gpt-5.6-luna`, `max`. Sol max and Astra max are explicit
  comparison options, never automatic fallbacks. Profiles are outside the semantic
  prompt and packet so comparisons can use identical inputs.

This reuses only the old read-only source loaders (and their `v12` resource loader),
not old packet projection, response validation, prompts, or run orchestration.
Source and builder file hashes are recorded for provenance. Source files must
remain stable during preparation. Keep these shared loaders available while using
v2; this is an isolated workflow, not a standalone distribution of the databases.

## Prepare

From the repository root:

```bash
python3 focus_trace_v2/workflow.py prepare --ayah 29:38 --run pilot-luna-clean
python3 focus_trace_v2/workflow.py validate focus_trace_v2/runs/pilot-luna-clean/29_38 --inputs-only
```

By default, preparation reads only the corresponding legacy packet's window and
optional non-citable remote orientation snapshot. It rebuilds all citable evidence
from current resources. It never reads legacy reader responses. The old window
source is hashed and recorded; remote snapshots are not newly validated lexical
evidence. Alternatively supply `--window-from PATH` or an explicit window:

```bash
python3 focus_trace_v2/workflow.py prepare --ayah 83:1 --window 83:1-36 --run pilot-luna-clean
python3 focus_trace_v2/workflow.py prepare --ayah 29:38 --run pilot-sol-clean --model gpt-5.6-sol
```

Use the same window and source versions for comparisons. `--window` accepts
comma-separated refs and same-surah ranges. Synthetic `S:0` basmalah is allowed
inside windows for surahs other than 1 and 9, never as the focus. Out-of-window
Arabic remains orientation-only. An explicit window does not import old remote
orientation cues; use the same selection mode across compared jobs.

Each new job has three reader files: `packet.json`, `prompt.md`, and
`response.schema.json`. Two other files are coordinator-only: `job.json` and the
complete `source.packet.json`. There is no reader assignment/hash-copying file.
All outputs live under `focus_trace_v2/runs/<run>/<surah>_<ayah>/`. Preparation
refuses an existing job, including a partial one: use a new run name. There is no
overwrite flag. Missing source inventories are visible gaps, not fatal conditions;
missing files, malformed coverage, or inconsistent resources fail preparation.
The flat remote-orientation shape used by existing lean packets is projected
without audit labels. Unrecognized remote fields stop preparation for review
instead of being silently dropped.

Original `runs/pilot-luna/` jobs are preserved with their frozen prompt/schema
and remain valid. Their job protocol is `hft-v2-job-v1`; newly prepared jobs use
`hft-v2-job-v2`. Use `pilot-luna-clean` for the metadata-free reader inputs.

## Run one reader (only when generation is approved)

The coordinator launches one fresh-context worker per job with the exact model
and `max` effort in `job.json`. Give it only the three reader files listed above
(exclude `job.json` and `source.packet.json`) and ownership of that job's
`response.json`. Do not fork the
coordinator's conversation or show old outputs, target interpretations, or model
comparison hints. If the requested model/effort is unavailable, stop; do not
silently substitute. Do not ask the reader to manage files beyond its response.

Deliver the complete frozen packet, not a truncated shell preview. When using
file-reading tools, instruct the worker to page through all ayat, mappings, and
inventory variants with read-only commands (for example `jq` slices), checking
array lengths so nothing is skipped. Reading with existing commands is allowed;
writing helper scripts is not. Check that complete input plus output allowance
fits the selected model's context. Do not silently trim inventories or summarize
away scopes to make a job fit; stop and resolve the scope explicitly instead.

The receipt records the **requested** profile, not proof of which model ran:
`execution_verified: false` is intentional. The coordinator must keep actual
runtime/session metadata separately and verify it before drawing model-quality
conclusions. Input hashes detect changed sealed files; citation checks reject
incompatible evidence. Neither proves honest metadata or that a model truly read
every source. This is a reconstructed trace,
not a blind staged experiment.
The coordinator owns the response path and binds that response to the sealed job
when exporting. Do not copy an unrelated response into a job: without reader-echoed
hashes, a same-focus response from another job is not distinguishable by content
validation alone. Keep actual launch/session metadata to establish execution;
the export's `binding: coordinator_job_directory` is not proof of model execution.

After the worker finishes:

```bash
python3 focus_trace_v2/workflow.py validate focus_trace_v2/runs/pilot-luna-clean/29_38
python3 focus_trace_v2/workflow.py export focus_trace_v2/runs/pilot-luna-clean/29_38
```

Validation checks JSON shape, frozen file hashes, ayah/root/target/variant coverage
in the coordinator source snapshot, exact equality with its reader projection,
all citation identities, exact quotations and occurrence indices, focus-only
baseline evidence, and actual context triggers. It fails if a response is absent
unless `--inputs-only` is specified; even then, an existing response is checked.
The small built-in schema checker supports only the keywords used in the supplied
schema and fails on unknown keywords. It is not a general JSON Schema library.

If a response is invalid or a worker is interrupted, preserve the artifact and
diagnostic. Do not automatically pay for another semantic run. Investigate the
smallest repair; never relabel the response or its coordinator binding to pretend
it used a different packet. Frozen inputs should not be edited, reformatted, or replaced. Changing
working prompt/schema templates does not invalidate previously frozen jobs.

`evidence.json` retains the entire response and resolves every retained branch
to the exact source variant, mapping target, full source ayah, and QAC occurrence
from the verified coordinator snapshot; structural cues
receive their full source ayah too. Export is idempotent for identical content
and refuses to replace differing evidence. The export is an explicit future
integration boundary, **not yet an input understood by prose_generation V5**.
No V5 loader, defaults, legacy runs, or existing artifacts are changed. Do not
copy this new protocol into legacy reader directories. Promotion requires a
separate opt-in V5 adapter after the pilot; rollback today is simply not using v2.

## Verify and decide

```bash
python3 -m unittest discover -s focus_trace_v2/tests -v
```

Tests cover missing inventories, split mappings, distinct variants, corruption,
branchless reasoning, source resolution, metadata exclusion, full Arabic/English
retention, original frozen-job compatibility, and existing-resource 29:38 / 83:1
regressions. The latter use local data only and skip if resources are unavailable.
Synthetic test findings are not model outputs or semantic-quality evidence.

Next, with approval, run a small paired Luna-max/Sol-max pilot on identical sealed
inputs. Include 29:38, 83:1, split/variant-heavy cases, and some ordinary ayat. Judge
anchored discovery recall, competing readings, scope fidelity, inference limits,
and actual cost—not just JSON validity. Do not assume corrected data proves Luna
matches Sol or that legacy reader outputs recover omissions without rereading.
Complete packets are larger than legacy lean packets; shared inventories reduce
duplication, but actual end-to-end token cost still needs measurement in the pilot.

The short, model-independent prompt follows the emphasis on lean instructions
without dropping task requirements in [OpenAI's GPT-5.6 prompting guidance](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6).
The configured candidate follows the user's requested profile;
[Luna's model documentation](https://developers.openai.com/api/docs/models/gpt-5.6-luna)
lists `max` effort support. These docs do not establish quality parity for HFT.
