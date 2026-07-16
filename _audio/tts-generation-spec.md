# TTS Generation Spec

This spec defines how to turn a canonical `v3/run/<surah-run>/<surah>-publication.jsonl` file into paragraph-level Google Gemini TTS requests and app-ready audio chunks.

Only `v3` sources are valid for this pipeline. Do not use `v1`, `v2`, `v2.1`, `v4`, or `v5` publication files for production audio generation, pilots, cost estimates, or app manifests.

## Current TTS Backend

Endpoint:

```text
https://texttospeech.googleapis.com/v1beta1/text:synthesize
```

Voice configuration:

```json
{
  "languageCode": "tr-TR",
  "modelName": "gemini-3.1-flash-tts-preview",
  "name": "Rasalgethi"
}
```

Audio configuration:

```json
{
  "audioEncoding": "LINEAR16",
  "pitch": 0,
  "speakingRate": 1
}
```

Observed output from the canary calls:

```text
WAVE audio, Microsoft PCM, 16 bit, mono 24000 Hz
```

Mono is preferred for this project. The content is spoken narration, not spatial music, so stereo does not add meaningful quality. Mono also reduces storage, bandwidth, and decoding work. If an app or player needs stereo later, create a delivery derivative from the mono master rather than requesting or storing stereo masters.

Working prompt:

```text
Speak as a warm, conversational Turkish narrator addressing one curious listener. Sound like a thoughtful person sharing a discovery as it becomes clear, with natural human cadence, varied sentence energy, and quiet curiosity. Let short reveal sentences land, then slow slightly for explanation. Use clear Istanbul Turkish diction and natural pauses. Avoid sermon, classroom lecture, documentary-announcer delivery, exaggerated drama, and a repeated rhetorical rise-and-fall. Do not give every section the same cadence. Pronounce Arabic Quranic words naturally as Arabic, then return smoothly to Turkish.
```

Do not use `input.ssml` with this voice/model. The canary test failed with:

```text
This voice does not support SSML input. Please try again with text only input.
```

Use `input.text`. The response may include a `timepoints` key, but it is empty for plain text.

## Source File

For a given surah, read:

```text
v3/run/<surah-run>/<surah>-publication.jsonl
```

Example:

```text
v3/run/s096-full-20260716/96-publication.jsonl
```

The source path must match:

```text
^v3/run/[^/]+/[0-9]{1,3}-publication\.jsonl$
```

Legacy numbered `{surah}-publication.md` and `publication.md` files remain accepted only when the same run has no numbered publication JSONL. Once `<surah>-publication.jsonl` exists, TTS preparation must use it.

If a requested surah does not have a matching `v3` publication file, stop and report that no valid v3 source exists. Do not fall back to `v4`, `v5`, or any other version.

The source JSONL is the canonical publication structure. Each line is one `opening`, `finding`, or `closing` record with:

```text
kind
grades
title
paragraphs
```

Grades are app and audit metadata. They are never sent to TTS.

## Section Model

Each publication record becomes one audio section.

### Opening

The `opening` record is the first section. Its `title` is spoken as the first chunk, followed by each item in `paragraphs` as its own chunk.

Example:

```json
{"kind":"opening","grades":[],"title":"Yol Söylenmeden Önce","paragraphs":["Sure doğrudan hareketini kurar."]}
```

### Findings

Every `finding` record becomes an independent section. The section preserves its `grades` in `chunks.jsonl` and `manifest.json`, but audio contains only the title and prose.

```json
{"kind":"finding","grades":["GÜÇLÜ / A"],"title":"Kulluğun Önceden Açtığı Yol","paragraphs":["İlk anlatım bölümü.","İkinci anlatım bölümü."]}
```

Generated chunks:

```text
Kulluğun Önceden Açtığı Yol.
İlk anlatım bölümü.
İkinci anlatım bölümü.
```

### Closing

The final `closing` record is its own section:

```text
Son Geçiş.
```

The closing title is followed by its one or two prose paragraphs.

## Paragraph Unit

Generate TTS one title or prose paragraph at a time.

A paragraph unit is:

- One record title, or
- One string from that record's `paragraphs` array.

Paragraph units are the app playback and resume boundaries. Sentence-level timestamps are not available with this model because SSML marks are unsupported.

For section titles, keep two text fields:

- `text`: display/audit text without artificial punctuation.
- `ttsText`: spoken text sent to Google TTS.

If a title does not already end in sentence punctuation, append a period in `ttsText` only. This prevents the title from sounding like it runs into the next paragraph while keeping the visible title clean.

Example:

```json
{
  "text": "Adla Başlayan Yol",
  "ttsText": "Adla Başlayan Yol."
}
```

The app should store playback progress as:

```json
{
  "surah": "s096",
  "sectionIndex": 2,
  "paragraphIndex": 4,
  "offsetSeconds": 12.3
}
```

## Text Cleaning

Canonical JSONL prose is already plain text. Apply no Markdown inference or label parsing.

1. Use `title` and `paragraphs` exactly as validated.
2. Never concatenate `grades` into spoken text.
3. Preserve Arabic script and Turkish punctuation exactly.
4. Add final sentence punctuation to `ttsText` for a title only when it has none.
5. Do not combine adjacent publication records or paragraphs.
6. Reject malformed JSONL, spoken grade codes, bare spaced Arabic roots, or explicit cinematic production vocabulary before request creation.

Legacy Markdown sources continue through the old cleaning path only when no canonical JSONL exists. That compatibility parser removes collector headings and all confidence codes from speech.

## Request Shape

For each paragraph unit, send one request:

```json
{
  "audioConfig": {
    "audioEncoding": "LINEAR16",
    "pitch": 0,
    "speakingRate": 1
  },
  "input": {
    "prompt": "Speak as a warm, conversational Turkish narrator addressing one curious listener. Sound like a thoughtful person sharing a discovery as it becomes clear, with natural human cadence, varied sentence energy, and quiet curiosity. Let short reveal sentences land, then slow slightly for explanation. Use clear Istanbul Turkish diction and natural pauses. Avoid sermon, classroom lecture, documentary-announcer delivery, exaggerated drama, and a repeated rhetorical rise-and-fall. Do not give every section the same cadence. Pronounce Arabic Quranic words naturally as Arabic, then return smoothly to Turkish.",
    "text": "<cleaned paragraph text>"
  },
  "voice": {
    "languageCode": "tr-TR",
    "modelName": "gemini-3.1-flash-tts-preview",
    "name": "Rasalgethi"
  }
}
```

Do not include `enableTimePointing` for plain text requests. It does not produce sentence timings here.

Example request for one finding paragraph of `S096`:

```json
{
  "audioConfig": {
    "audioEncoding": "LINEAR16",
    "pitch": 0,
    "speakingRate": 1
  },
  "input": {
    "prompt": "Speak as a warm, conversational Turkish narrator addressing one curious listener. Sound like a thoughtful person sharing a discovery as it becomes clear, with natural human cadence, varied sentence energy, and quiet curiosity. Let short reveal sentences land, then slow slightly for explanation. Use clear Istanbul Turkish diction and natural pauses. Avoid sermon, classroom lecture, documentary-announcer delivery, exaggerated drama, and a repeated rhetorical rise-and-fall. Do not give every section the same cadence. Pronounce Arabic Quranic words naturally as Arabic, then return smoothly to Turkish.",
    "text": "Tehdit önce soyut bir ceza gibi duyulur. Ardından perçem anlamındaki بِالنَّاصِيَةِ sözü belirir ve hareket bedenin en görünür yerine taşınır. Yanlış artık yalnızca hüküm verilen bir davranış değildir; insanın önünde okunabilen bir yöne dönüşür."
  },
  "voice": {
    "languageCode": "tr-TR",
    "modelName": "gemini-3.1-flash-tts-preview",
    "name": "Rasalgethi"
  }
}
```

## Output Layout

Use `_audio/audio/` as the canonical generated-audio root. Each surah gets one dedicated folder:

```text
_audio/audio/<surah-id>/
```

Example:

```text
_audio/audio/S096/
```

The folder name uses the normalized surah id, not the run id. Use uppercase `S` plus a 3-digit surah number:

```text
S001
S096
S114
```

Recommended files for each surah:

```text
S096.md
chunks.jsonl
manifest.json
requests/
responses/
originals/
  wav/
  mp3/
sections/
  wav/
  mp3/
```

The source run is still recorded in `manifest.json`, so a regenerated `S096` folder can point back to the exact source file:

```text
v3/run/s096-full-20260716/96-publication.jsonl
```

`manifest.json` must always record a `source` beginning with `v3/run/`. Treat any other source value as non-canonical and invalid for production.

Chunk filenames should be stable and sortable:

```text
sec-001-p-001.wav
sec-001-p-002.wav
sec-002-p-001.wav
```

Store the raw request and response for reproducibility:

```text
requests/sec-001-p-001.json
responses/sec-001-p-001.json
originals/wav/sec-001-p-001.wav
originals/mp3/sec-001-p-001.mp3
sections/wav/sec-001.wav
sections/mp3/sec-001.mp3
```

## Clean Text Copy

Write a cleaned Markdown copy named after the surah:

```text
_audio/audio/S096/S096.md
```

This file is a human-readable narration copy. It is not the canonical app mapping.

Rules:

- Start from the source `{surah}-publication.jsonl`.
- Preserve one section per publication record.
- Rename the file to the surah id, such as `S096.md`.
- Keep section headings readable as Markdown headings.
- Do not include grades.
- Keep each `paragraphs` item as its own Markdown paragraph.
- Preserve generated TTS chunk boundaries exactly.

Example:

```md
# Asılı Başlangıçtan Yakınlığa: Alak Suresinde Ölçü, Taşkınlık ve Dönüş

Sure, ...

## Perçemden meclise uzanan rakip ön ve karşı çağrı

Tehdit önce soyut bir ceza gibi duyulur.

Ardından perçem anlamındaki بِالنَّاصِيَةِ sözü ...
```

The Markdown copy is for review and editorial traceability. The app should read `chunks.jsonl` or `manifest.json`, not scrape `S096.md`.

## Paragraph Map JSONL

Write a `chunks.jsonl` file in the surah folder. This is the canonical paragraph-level mapping between text and audio.

Each line is one paragraph unit and must be valid JSON:

```json
{"surahId":"S096","source":"v3/run/s096-full-20260716/96-publication.jsonl","chunkId":"sec-001-p-001","sectionIndex":1,"paragraphIndex":1,"kind":"section_title","publicationKind":"opening","grades":[],"sectionTitle":"Asılı Başlangıçtan Yakınlığa: Alak Suresinde Ölçü, Taşkınlık ve Dönüş","text":"Asılı Başlangıçtan Yakınlığa: Alak Suresinde Ölçü, Taşkınlık ve Dönüş","request":"requests/sec-001-p-001.json","response":"responses/sec-001-p-001.json","wav":"originals/wav/sec-001-p-001.wav","mp3":"originals/mp3/sec-001-p-001.mp3","durationSeconds":0}
```

Required fields:

- `surahId`: normalized folder id, such as `S096`.
- `source`: canonical source publication JSONL path.
- `chunkId`: stable id, such as `sec-003-p-002`.
- `sectionIndex`: 1-based section index.
- `paragraphIndex`: 1-based paragraph index within the section.
- `kind`: `section_title` or `paragraph`.
- `publicationKind`: `opening`, `finding`, or `closing`.
- `grades`: publication grades for the containing section; never spoken.
- `sectionTitle`: cleaned section title.
- `text`: exact cleaned display/audit text.
- `ttsText`: exact text sent to TTS. For ordinary paragraphs this usually equals `text`; for section titles it may add final punctuation.
- `request`: relative path to the request JSON.
- `response`: relative path to the response JSON.
- `wav`: relative path to the WAV file.
- `mp3`: relative path to the MP3 file, when present.
- `durationSeconds`: measured or estimated duration.

Recommended optional fields:

- `sourceLineStart`
- `sourceLineEnd`
- `charCount`
- `wordCount`
- `textSha256`
- `promptSha256`
- `generatedAt`

Use JSONL because it is append-friendly, streamable, and easy for the app to load without parsing Markdown.

## Manifest

Write a `manifest.json` for app playback and batch metadata. It should summarize the same chunks listed in `chunks.jsonl`.

Suggested shape:

```json
{
  "source": "v3/run/s096-full-20260716/96-publication.jsonl",
  "surahId": "S096",
  "surahRun": "s096-full-20260716",
  "cleanMarkdown": "S096.md",
  "chunksJsonl": "chunks.jsonl",
  "voice": {
    "languageCode": "tr-TR",
    "modelName": "gemini-3.1-flash-tts-preview",
    "name": "Rasalgethi"
  },
  "audioEncoding": "LINEAR16",
  "sections": [
    {
      "sectionIndex": 1,
      "title": "Asılı Başlangıçtan Yakınlığa: Alak Suresinde Ölçü, Taşkınlık ve Dönüş",
      "kind": "opening",
      "grades": [],
      "paragraphs": [
        {
          "paragraphIndex": 1,
          "kind": "section_title",
          "text": "Asılı Başlangıçtan Yakınlığa: Alak Suresinde Ölçü, Taşkınlık ve Dönüş",
          "chunkId": "sec-001-p-001",
          "wav": "originals/wav/sec-001-p-001.wav",
          "mp3": "originals/mp3/sec-001-p-001.mp3",
          "durationSeconds": 0
        }
      ]
    }
  ]
}
```

Fill `durationSeconds` after audio generation by probing the WAV or MP3.

For LINEAR16 WAV returned by the current API, duration can be estimated from file metadata:

```text
durationSeconds = (file_size_bytes - 44) / (24000 samples/sec * 2 bytes/sample * 1 channel)
```

Prefer a real audio probe tool such as `ffprobe` when available.

## MP3 Compression

Yes, WAV can be compressed to MP3 later to reduce file size with minimal practical loss for spoken narration.

Recommended production approach:

- Keep the original LINEAR16 WAV as the archival source.
- Generate MP3 derivatives for app delivery.
- Use mono MP3 because the source is mono narration.
- Use `64k` or `80k` CBR for small, good spoken-word files.
- Use `96k` CBR if Arabic pronunciation and consonant detail need extra preservation.

Example command:

```bash
ffmpeg -i sec-001-p-001.wav -codec:a libmp3lame -b:a 80k -ac 1 sec-001-p-001.mp3
```

Expected reduction:

- Current LINEAR16 WAV is 24 kHz, 16-bit, mono: about 48 KB/sec.
- 80 kbps MP3 is about 10 KB/sec.
- File size becomes roughly 20-25% of WAV.

For app playback, MP3 is broadly compatible. For gapless paragraph sequencing, test on the target platform; MP3 encoder delay can add tiny padding. If exact gapless joins become important, consider AAC/M4A or Opus for delivery while still keeping WAV as source.

## Cost Notes

Gemini 3.1 Flash TTS Preview pricing is token-based:

- Input text tokens: $1.00 per 1M text tokens.
- Output audio tokens: $20.00 per 1M audio tokens.
- Audio tokens correspond to 25 tokens per second.

Output cost dominates. Paragraph-level generation repeats the prompt for every paragraph, but the added input cost is small compared with the audio duration cost.

## Known Constraints

- This Gemini TTS voice/model does not support SSML input.
- Sentence start times cannot be deterministically recovered from a paragraph audio file.
- Paragraph-level audio gives deterministic paragraph starts and resumable offsets within each paragraph.
- If deterministic sentence starts are required later, generate one audio file per sentence instead of per paragraph.
