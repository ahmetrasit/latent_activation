# v12 Cross-Run Whole-Surah Publication Specification

This is the normative target workflow for combining canonical regular v12 and
±5 v12 findings. The root orchestrator follows this document, prepares files,
and spawns whole-surah agents. Scripts never spawn agents and there is no
workflow CLI.

The current staged extract/normalize/grade/publish prompts, schemas, and task
helpers are legacy calibration machinery. They do not define production after
this specification.

## 1. Objective

For one surah, consolidate the two already-generated and already-audited v12
readings into a compact publication structure:

- one or more primary contextual findings per ayah;
- one or more secondary contextual findings per ayah;
- exact `root_id` + `branch_id` anchors for every finding;
- one finding-level grade for every secondary: `strong`, `weak`, or `reject`.

There is no translation-eligibility task, lexical-status classification,
branch-level grade, unlicensed category, exploratory output category, or
separate rejected collection.

Every non-primary finding becomes a secondary finding. A secondary graded
`reject` remains fully stored as an ordinary secondary row; the grade is a
recommendation, not deletion.

## 2. Source Status and Authority

The source families are complete:

- canonical regular v12: S001-S114;
- ±5 v12: S001-S114.

No new v12 reader runs are required for this integration workflow.

The agent may use only the assigned whole-surah package:

- the selected canonical regular v12 analytical output;
- the selected ±5 v12 analytical output;
- the matching `full_context_packet.json`;
- the deterministic QAC/attachment linguistic cache;
- the publication prompt and output contract.

Do not add tafsir, translations, web material, older project analyses, or other
surahs' unpublished work.

## 3. Whole-Surah File Access

Mirror the successful v12 input pattern. Give the agent paths to the complete
surah files; do not serialize their contents into a giant task envelope and do
not create one agent task per ayah.

A package index may record paths and hashes, but it is only an index. The agent
opens the whole files and reads the sections it needs whenever it needs them.
File size is not equivalent to initial prompt tokens.

Typical package paths are:

```text
v12/runs/s###/full_context_packet.json
v12/runs/s###/full_context_control/<selected-reader-output>.md
v12/runs_11ayah/s###/full_context_control/<selected-reader-output>.md
_status/v12_cross_run/s###/linguistic/manifest.json
_status/v12_cross_run/s###/linguistic/words.tsv
_status/v12_cross_run/s###/linguistic/morphemes.tsv
_status/v12_cross_run/s###/linguistic/attachment_units.tsv
_status/v12_cross_run/s###/linguistic/syntax_edges.tsv
```

The agent owns the entire surah and processes ayat in surah order. It may write
its surah output incrementally, as v12 did, but it may not delegate individual
ayat to other agents.

## 4. Deterministic Preparation

Before spawning the publisher, the orchestrator performs only mechanical work:

1. select the two canonical reader outputs and record their hashes;
2. verify that both outputs and the packet belong to the same surah;
3. build or refresh the linguistic cache;
4. resolve and validate the already-assigned `root_id` + `branch_id` anchors;
5. create the small package index containing file paths and hashes.

Run the existing binder:

```bash
python3 _status/v12_cross_run/scripts/build_linguistic_bindings.py \
  _status/v12_cross_run/s###
```

`build_linguistic_bindings.py` is the authority for:

- stable QAC word IDs;
- QAC morpheme IDs and morphology;
- mapping synthetic packet refs to QAC refs;
- attachment-unit to QAC word/morpheme alignment;
- attachment syntax-edge endpoints;
- binding status and unresolved warnings.

Attachment indices are never treated as QAC indices. The script cross-walks
them through position, normalized surface, root, sequence, and clitic evidence.
The publication agent does not perform, repair, or reinterpret this alignment.

## 5. Agent Roles

### Agent A — whole-surah publisher

Agent A reads the complete package and directly writes the final publication
structure. It performs the necessary consolidation internally; extraction,
normalization, and branch grading are not separate stages or outputs.

For every ayah, Agent A must:

1. retain the existing primary contextual readings as primary;
2. merge only genuinely duplicate contextual readings;
3. convert every non-primary or exploratory reading into secondary;
4. preserve distinct contextual readings as distinct findings;
5. copy or combine the already-assigned root/branch anchors;
6. grade every secondary `strong`, `weak`, or `reject`;
7. write the complete surah output.

Agent A does not emit source-finding IDs, lexical labels, translation roles,
branch roles, evidentiary scores, or intermediate claims.

### Agent B — whole-surah integration reviewer

Agent B reviews the complete proposed publication, not the original findings
from scratch. Its narrow checks are:

- all ayat with source findings are represented;
- distinct contextual readings were not over-merged;
- true contextual duplicates were not needlessly repeated;
- every anchor resolves to an assigned `root_id` + `branch_id`;
- primary findings have no grade;
- every secondary has exactly one allowed grade;
- `reject` secondaries remain fully present.

Agent B returns a concise issue list. If a material issue exists, Agent A gets
one repair pass over the whole surah. Agent B does not invent new readings or
reclassify branches.

## 6. Publication Output

The logical output for each ayah is:

```json
{
  "ayah_ref": "1:6",
  "primary": [
    {
      "text": "contextual reading",
      "anchors": [
        {"root_id": "root_000000", "branch_id": "B001"}
      ]
    }
  ],
  "secondary": [
    {
      "text": "distinct contextual reading",
      "grade": "strong",
      "anchors": [
        {"root_id": "root_000000", "branch_id": "B005"}
      ]
    },
    {
      "text": "retained but not recommended for default display",
      "grade": "reject",
      "anchors": [
        {"root_id": "root_000001", "branch_id": "B003"}
      ]
    }
  ]
}
```

Rules:

- multiple primary and multiple secondary findings are allowed;
- primary findings do not have a grade;
- every secondary has exactly one grade;
- a `reject` secondary has the same full structure as `strong` and `weak`;
- anchors contain only `root_id` and `branch_id`;
- branch anchors receive no context-independent labels;
- no source-finding IDs are copied into the publication output;
- original v12 files remain the source provenance;
- downstream row IDs, if needed, are assigned mechanically after publication.

## 7. Contextual Deduplication

Deduplication is based on contextual-reading equivalence, never branch overlap.

Merge only when two findings express the same:

- fixed-ayah reading;
- contextual mechanism;
- structural or causal relationship;
- substantive change in how the ayah is understood.

Consequences:

- same branches + different contextual readings = separate findings;
- different branches + the same contextual reading = merge is allowed, with
  the anchors combined;
- similar topic + different mechanism = separate findings;
- paraphrase or compatible elaboration of the same mechanism = merge.

When uncertain, preserve separate findings. Avoiding semantic loss is more
important than minimizing row count.

## 8. Secondary Grades

The grade belongs to the complete contextual finding, not to any branch.

- `strong`: clear anchored mechanism that materially organizes or changes the
  reading;
- `weak`: distinct anchored reading with limited, indirect, or tentative force;
- `reject`: retained in full, but Agent A recommends that it not appear in the
  default publication layer.

`Reject` never authorizes deletion and never creates a third output category.

## 9. Mechanical Close

After Agent A and, when used, Agent B finish, deterministic checks verify only:

1. the output has the assigned surah and valid ordered ayah refs;
2. primary and secondary structures match the publication contract;
3. every secondary grade is `strong`, `weak`, or `reject`;
4. primary findings contain no grade;
5. every anchor resolves in the assigned packet/inventory snapshot;
6. every QAC/attachment binding warning is resolved or explicitly surfaced;
7. no forbidden source IDs, translation roles, or branch labels appear.

The orchestrator then commits the complete surah output atomically and derives
any downstream TSV/database views mechanically. No separate lexical audit or
translation audit is part of this workflow.

## 10. Parallelism and Resume

- The independently owned unit is one whole surah.
- Never spawn separate workers for its ayat.
- Different surahs may run in parallel.
- One publisher owns a surah from its first ayah through its final ayah.
- Incremental writes are recovery checkpoints, not separate agent tasks.
- If the publisher dies, a replacement receives the whole package and the
  partial output, reviews the existing work, and owns completion of the surah.

## 11. Legacy S1 Calibration

The existing S1 TSV ledger and ayah-scoped task artifacts document the earlier
calibration design. Preserve them as history, but do not resume the prepared
ayah-level normalization or grading tasks.

The first production test is a fresh whole-surah S1 direct-publication pass
under this specification. It may consult the canonical v12 inputs, not the
legacy classifications, as its analytical source.

## 12. Completion

A surah is complete when:

- Agent A has processed the whole surah;
- each contextual reading is represented as primary or secondary;
- contextual duplicates are consolidated without collapsing distinct readings;
- every finding has valid root/branch anchors;
- every secondary has a grade, including fully retained `reject` findings;
- the mechanical QAC/attachment cache has no unresolved blocking warning;
- the final surah output passes the compact structural checks.
