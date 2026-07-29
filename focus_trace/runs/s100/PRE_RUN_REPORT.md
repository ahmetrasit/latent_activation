# S100 Hermetic Focus Trace Pre-Run Report

Status: packets generated and validated; reader agents not run yet.

Reason reader outputs are absent: the coordinator was instructed not to spawn
agents yet. The S100 packet layer is ready for `gpt-5.6-sol` max readers once
agent execution is re-enabled.

## Packet Contract

- packet protocol: `focus-trace-hermetic-packet-v2`
- response protocol expected by prompt/schema: `focus-trace-hermetic-response-v3`
- model profile: `gpt-5.6-sol`, `reasoning_effort: max`
- root identity source:
  `../quran-data/data/bridges/qac-furuq-v4-root-map.sqlite.gz`
- root bridge SHA-256:
  `415d0f14f3f1d6b49fd2fd574d24495090ece1af3f01210998b0bc1eb7b11296`
- split-root citation rule: every branch citation must pair `mapped_root_id`
  with root-local `branch_id`

## Split Roots In S100

| QAC root | mapped Furuq targets | accepted branch counts in packet |
| --- | --- | --- |
| `ع د و` | `root_000993` / `ع د و` dominant; `root_000989` / `ع د د`; `root_001058` / `ع و د` | 12; 6; 11 |
| `ث و ر` | `root_000210` / `ث و ر` dominant; `root_000011` / `ء ث ر` | 7; 11 |
| `ر ب ب` | `root_000532` / `ر ب ب` dominant; `root_000537` / `ر ب و` | 17; 7 |

This corrects the earlier packet build, which loaded branches by QAC Arabic root
string and therefore missed non-dominant split targets.

All eleven S100 packets were checked against the same root bridge hash above.
Each packet contains the three S100 split-root mappings and records
`focus-trace-hermetic-packet-v2`.

## Packet Size / Input Estimate

The estimate uses the local commentary tooling convention of bytes / 4. Fixed
reader prompt + schema cost is 12,931 bytes, about 3,232 tokens.

| focus | packet bytes | estimated input tokens |
| --- | ---: | ---: |
| 100:1 | 163,430 | 44,090 |
| 100:2 | 145,121 | 39,513 |
| 100:3 | 142,661 | 38,898 |
| 100:4 | 157,607 | 42,634 |
| 100:5 | 149,200 | 40,532 |
| 100:6 | 173,769 | 46,675 |
| 100:7 | 134,267 | 36,799 |
| 100:8 | 150,259 | 40,797 |
| 100:9 | 141,916 | 38,711 |
| 100:10 | 140,445 | 38,344 |
| 100:11 | 168,142 | 45,268 |

Total packet bytes: 1,666,817. Estimated total input for one reader across all
11 S100 ayat: about 452,264 tokens.

## Reader_M Baseline

The comparison target is recorded in
[`READER_M_BASELINE.md`](READER_M_BASELINE.md). In short, `reader_m` is stronger
than the regular and 11-ayah S100 reader walks because it preserves more
coexisting readings, more explicit changed-reading language, and more odd but
anchored latent motifs. The later quality review should compare Hermetic Focus
Trace against that standard, not merely against a generic surah-wide summary.

## Commentary Integration State

`prose_generation` now loads this run as `v12_focus_trace_hermetic`. While only
packets exist, ayah bundles record `packet_present: true` and `present: false`.
After reader JSON is generated, the bundle will load reader outputs under
`v12_focus_trace_hermetic.readers`.

To keep Layer 2 prompts cost-effective, `root_lexicon` lists every mapped split
root target in coverage but inlines full dictionary/gloss payload only for the
dominant target. Secondary split-root branch images and activations are expected
to enter through Hermetic Focus Trace packets/responses.
