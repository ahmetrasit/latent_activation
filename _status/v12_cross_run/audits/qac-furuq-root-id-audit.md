# QAC to furuq_v4 root-id audit

Generated UTC: `2026-07-28T13:12:45Z`

## Summary

- QAC rooted rows audited: `1642`
- QAC root keys audited: `1642`
- Rooted morpheme occurrences: `49968`
- Non-ok root rows: `20`
- Non-ok rooted morpheme occurrences: `1103`

## Status Counts

| status | roots | occurrences |
| --- | ---: | ---: |
| `error_legacy_root_norm_overinclude` | 11 | 1007 |
| `error_unresolved` | 8 | 92 |
| `ok_normalized_unique` | 115 | 8767 |
| `ok_source_exact` | 1507 | 40098 |
| `review_canonical_only` | 1 | 4 |

## Audit Class Counts

| class | roots | occurrences |
| --- | ---: | ---: |
| `error` | 19 | 1099 |
| `ok` | 1622 | 48865 |
| `review` | 1 | 4 |

## Non-OK Rows

| class | status | qac root | occ | chosen | source_exact | normalized_exact | canonical | examples | notes |
| --- | --- | --- | ---: | --- | --- | --- | --- | --- | --- |
| `error` | `error_legacy_root_norm_overinclude` | `ش ي ء` | 519 | `root_000831` | `root_000831` | `root_000831;root_000832` | `root_000831;root_000832` | 2:20:15;2:20:24;2:29:18;2:35:11;2:48:8;2:58:9;2:70:15;2:90:18 | root_norm lookup returns different root_id set than source_exact;canonical fallback would return different root_id set |
| `error` | `error_legacy_root_norm_overinclude` | `ج ي ء` | 278 | `root_000281` | `root_000281` | `root_000281;root_000282` | `root_000281;root_000282` | 2:71:19;2:87:18;2:89:2;2:89:18;2:92:2;2:101:2;2:120:21;2:145:26 | root_norm lookup returns different root_id set than source_exact;canonical fallback would return different root_id set |
| `error` | `error_legacy_root_norm_overinclude` | `ق ر ء` | 88 | `root_001210` | `root_001210` | `root_001210;root_001211` | `root_001210;root_001211` | 2:185:6;2:228:5;4:82:3;5:101:17;6:19:14;7:204:2;7:204:3;9:111:23 | root_norm lookup returns different root_id set than source_exact;canonical fallback would return different root_id set |
| `error` | `error_legacy_root_norm_overinclude` | `م ر ء` | 38 | `root_001409` | `root_001409` | `root_001409;root_001410` | `root_001409;root_001410` | 2:102:41;2:282:61;3:35:3;3:40:10;4:4:14;4:12:56;4:128:2;4:176:8 | root_norm lookup returns different root_id set than source_exact;canonical fallback would return different root_id set |
| `error` | `error_legacy_root_norm_overinclude` | `ب ر ء` | 31 | `root_000099` | `root_000099` | `root_000099;root_000100` | `root_000099;root_000100` | 2:54:13;2:54:20;2:166:2;2:167:8;2:167:11;3:49:24;4:112:9;5:110:39 | root_norm lookup returns different root_id set than source_exact;canonical fallback would return different root_id set |
| `error` | `error_legacy_root_norm_overinclude` | `ب و ء` | 17 | `root_000161` | `root_000161` | `root_000161;root_000162` | `root_000161;root_000162` | 2:61:41;2:90:21;3:112:14;3:121:5;3:162:6;5:29:4;7:74:8;8:16:13 | root_norm lookup returns different root_id set than source_exact;canonical fallback would return different root_id set |
| `error` | `error_legacy_root_norm_overinclude` | `ب د ء` | 15 | `root_000090` | `root_000090` | `root_000090;root_000091` | `root_000090;root_000091` | 7:29:15;9:13:10;10:4:8;10:34:6;10:34:12;12:76:1;21:104:8;27:64:2 | root_norm lookup returns different root_id set than source_exact;canonical fallback would return different root_id set |
| `error` | `error_legacy_root_norm_overinclude` | `ب ك ي` | 7 | `root_000147` | `root_000147` | `root_000146;root_000147` | `root_000146;root_000147` | 9:82:3;12:16:4;17:109:3;19:58:29;44:29:2;53:43:4;53:60:3 | root_norm lookup returns different root_id set than source_exact;canonical fallback would return different root_id set |
| `error` | `error_legacy_root_norm_overinclude` | `ض و ء` | 6 | `root_000919` | `root_000919` | `root_000919;root_000920` | `root_000919;root_000920` | 2:17:7;2:20:6;10:5:5;21:48:6;24:35:28;28:71:17 | root_norm lookup returns different root_id set than source_exact;canonical fallback would return different root_id set |
| `error` | `error_legacy_root_norm_overinclude` | `د ر ء` | 5 | `root_000466` | `root_000466` | `root_000466;root_000467` | `root_000466;root_000467` | 2:72:4;3:168:10;13:22:13;24:8:1;28:54:7 | root_norm lookup returns different root_id set than source_exact;canonical fallback would return different root_id set |
| `error` | `error_legacy_root_norm_overinclude` | `ط ف ء` | 3 | `root_000938` | `root_000938` | `root_000938;root_000939` | `root_000938;root_000939` | 5:64:38;9:32:3;61:8:2 | root_norm lookup returns different root_id set than source_exact;canonical fallback would return different root_id set |
| `review` | `review_canonical_only` | `ه ء ت` | 4 | `root_001574` | `` | `` | `root_001574` | 2:111:14;21:24:7;27:64:15;28:75:7 | no root_norm match; canonical fallback only |
| `error` | `error_unresolved` | `ك ي ف` | 83 | `` | `` | `` | `` | 2:28:1;2:259:52;2:260:6;3:6:6;3:25:1;3:86:1;3:101:1;3:137:10 |  |
| `error` | `error_unresolved` | `ل ف و` | 3 | `` | `` | `` | `` | 2:170:12;12:25:7;37:69:2 |  |
| `error` | `error_unresolved` | `ء د د` | 1 | `` | `` | `` | `` | 19:89:4 |  |
| `error` | `error_unresolved` | `ث ب ي` | 1 | `` | `` | `` | `` | 4:71:7 |  |
| `error` | `error_unresolved` | `س ن ه` | 1 | `` | `` | `` | `` | 2:259:42 |  |
| `error` | `error_unresolved` | `ش م ز` | 1 | `` | `` | `` | `` | 39:45:5 |  |
| `error` | `error_unresolved` | `ق ض ض` | 1 | `` | `` | `` | `` | 18:77:17 |  |
| `error` | `error_unresolved` | `ل و ت` | 1 | `` | `` | `` | `` | 38:3:8 |  |

## Interpretation

- `ok_source_exact`: QAC `root_ar` exactly resolves to one furuq `source_root_norm`.
- `ok_normalized_unique`: no exact source root exists, but furuq `root_norm` uniquely matches.
- `error_legacy_root_norm_overinclude`: exact source mapping is known, but a `root_norm`-only lookup pulls extra root_ids.
- `review_canonical_only`: only the lossy canonical fallback matches.
- `error_ambiguous_*`: the resolver returns multiple root_ids at that stage.
- `error_unresolved`: no furuq root_id is reachable from the audited QAC spelling.
