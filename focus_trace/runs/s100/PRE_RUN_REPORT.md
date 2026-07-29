# S100 Hermetic Focus Trace Pre-Run Report

Status: packets compacted and validated; primary `reader_hft_a` outputs are now
generated and validated.

This file began as the pre-run report. It has been updated after the compact
JSON optimization so its packet sizes and input estimates match the current
files.

## Packet Contract

- packet protocol: `focus-trace-hermetic-packet-v2`
- response protocol expected by prompt/schema: `focus-trace-hermetic-response-v4`
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
reader prompt + compact schema cost is 12,045 bytes, about 3,011 tokens.

Existing `reader_hft_a` outputs are response-v3. New comparison outputs should
use response-v4. The Python validator accepts both protocols.

| focus | packet bytes | estimated input tokens |
| --- | ---: | ---: |
| 100:1 | 113,200 | 31,311 |
| 100:2 | 97,787 | 27,458 |
| 100:3 | 95,870 | 26,978 |
| 100:4 | 108,644 | 30,172 |
| 100:5 | 101,685 | 28,432 |
| 100:6 | 120,465 | 33,127 |
| 100:7 | 89,063 | 25,277 |
| 100:8 | 102,243 | 28,572 |
| 100:9 | 95,529 | 26,893 |
| 100:10 | 94,378 | 26,605 |
| 100:11 | 115,701 | 31,936 |

Total packet bytes: 1,134,565. Estimated total input for one reader across all
11 S100 ayat: about 316,761 tokens.

Compared with the original pretty-printed JSON packets, compact JSON removes
532,252 packet bytes, about 31.9% of packet storage/input overhead.

## Reader_M Baseline

The comparison target is recorded in
[`READER_M_BASELINE.md`](READER_M_BASELINE.md). In short, `reader_m` is stronger
than the regular and 11-ayah S100 reader walks because it preserves more
coexisting readings, more explicit changed-reading language, and more odd but
anchored latent motifs. The later quality review should compare Hermetic Focus
Trace against that standard, not merely against a generic surah-wide summary.

## Commentary Integration State

`prose_generation` now loads this run as `v12_focus_trace_hermetic`. With
validated reader JSON present, rebuilt ayah bundles should record
`packet_present: true`, `present: true`, and load reader outputs under
`v12_focus_trace_hermetic.readers`.

To keep Layer 2 prompts cost-effective, `root_lexicon` lists every mapped split
root target in coverage but inlines full dictionary/gloss payload only for the
dominant target. Secondary split-root branch images and activations are expected
to enter through Hermetic Focus Trace packets/responses.
