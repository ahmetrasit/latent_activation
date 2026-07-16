# TTS Generation Spec

This spec defines how to turn a `v3/run/<surah-run>/<surah>-publication.md` file into paragraph-level Google Gemini TTS requests and app-ready audio chunks.

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
Speak as a warm, low-mid Turkish narrator for long-form theological and linguistic commentary. Keep the voice reflective, easy on the ears, and gently forward-moving so the listener can follow the argument. Use clear Istanbul Turkish diction, natural pauses, and subtle emphasis on key insight sentences. The tone should feel like a thoughtful teacher revealing structure step by step: calm, dignified, engaged, and quietly compelling. Pronounce Arabic script naturally, not as Turkish spelling.
```

Do not use `input.ssml` with this voice/model. The canary test failed with:

```text
This voice does not support SSML input. Please try again with text only input.
```

Use `input.text`. The response may include a `timepoints` key, but it is empty for plain text.

## Source File

For a given surah, read:

```text
v3/run/<surah-run>/<surah>-publication.md
```

Example:

```text
v3/run/s096-full-20260716/96-publication.md
```

The source path must match:

```text
^v3/run/[^/]+/[0-9]{1,3}-publication\.md$
```

During the current migration, legacy `v3/run/<surah-run>/publication.md` files may still exist for some surahs. Treat numbered `{surah}-publication.md` files as canonical whenever present; use `publication.md` only as a temporary fallback for runs that do not yet have the numbered file.

If a requested surah does not have a matching `v3` publication file, stop and report that no valid v3 source exists. Do not fall back to `v4`, `v5`, or any other version.

The source file is Markdown. The spoken text must be derived from the rendered editorial structure, not from raw Markdown syntax.

## Section Model

Each generated audio unit belongs to a section.

### Intro Section

The first Markdown H1 is the intro section title.

Example:

```md
# Asılı Başlangıçtan Yakınlığa: Alak Suresinde Ölçü, Taşkınlık ve Dönüş
```

The intro section includes all paragraphs after the H1 until the `## Bulgular` heading.

The title itself should be spoken as the first paragraph of the intro section unless explicitly disabled by a later app policy.

Do not speak the `## Bulgular` heading.

### Section Titles

Markdown headings other than `## Bulgular` and `## Ana Bulgular` are section titles. They are standalone TTS chunks and standalone audio files.

Examples:

```md
# Yol Söylenmeden Önce
### Kulluğun Önceden Açtığı Yol
## Son Geçiş
```

Spoken section titles:

```text
Yol Söylenmeden Önce.
Kulluğun Önceden Açtığı Yol.
Son Geçiş.
```

The section title chunk belongs to that section as its first paragraph unit. The following subsection chunks belong to the same section until the next Markdown heading or EOF.

Do not speak structural collector headings:

```md
## Bulgular
## Ana Bulgular
```

### Bulgular Subsections

Inside a section, bracketed labels start subsection paragraph chunks. They do not create new sections and are not standalone title chunks.

Raw example:

```md
[GÜÇLÜ / A — Perçemden meclise uzanan rakip ön ve karşı çağrı]

لَنَسْفَعًا بِالنَّاصِيَةِ tehdidinde iki kök birbirinin eksik rolünü tam olarak doldurur.
```

Spoken paragraph chunk:

```text
Perçemden meclise uzanan rakip ön ve karşı çağrı. لَنَسْفَعًا بِالنَّاصِيَةِ tehdidinde iki kök birbirinin eksik rolünü tam olarak doldurur.
```

Parsing rule:

- Match a line that starts with `[` and ends with `]`.
- Remove the outer brackets.
- If the content contains an em dash `—`, keep only the text after the first em dash.
- Trim surrounding whitespace.
- This cleaned title becomes the opening sentence of the next paragraph chunk.
- The following prose belongs to the same paragraph chunk until the next bracketed label or the next Markdown heading.
- If the bracket label is bolded, such as `**[GÜÇLÜ / A — ...]**`, remove the bold markers and apply the same rule.

Do not speak the strength/rank prefix such as `GÜÇLÜ / A`, `GÜÇLÜ / B`, or `GÜÇLÜ / C-koşullu`.

Also remove inline rank phrases from prose, such as `GÜÇLÜ / B`, `ORTA / A`, and `ZAYIF / C-koşullu`.

## Paragraph Unit

Generate TTS one paragraph at a time.

A paragraph unit is:

- One cleaned section title, or
- One cleaned subsection paragraph that starts with the cleaned bracket title and continues with its prose.

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

Apply these transformations before sending text to TTS:

1. Remove Markdown bold markers:

```text
**لَنَسْفَعًا بِالنَّاصِيَةِ** -> لَنَسْفَعًا بِالنَّاصِيَةِ
```

2. Remove Markdown italic markers if present.

3. Remove Markdown heading syntax from titles:

```text
## Geçişin yeniden duyuluşu -> Geçişin yeniden duyuluşu
```

4. Convert bracket labels into the opening sentence of the following subsection paragraph chunk.

5. Do not speak `## Bulgular`.

6. Preserve Arabic script exactly as written.

7. Preserve Turkish punctuation, semicolons, colons, and quotation marks unless they are Markdown syntax.

8. Collapse internal whitespace runs to single spaces within a paragraph.

9. Use Markdown headings as section-title chunk boundaries and bracket labels as subsection paragraph chunk boundaries.

10. Do not include empty paragraphs.

11. Do not include raw Markdown list markers, code fences, HTML comments, or YAML frontmatter if they appear in future files.

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
    "prompt": "Speak as a warm, low-mid Turkish narrator for long-form theological and linguistic commentary. Keep the voice reflective, easy on the ears, and gently forward-moving so the listener can follow the argument. Use clear Istanbul Turkish diction, natural pauses, and subtle emphasis on key insight sentences. The tone should feel like a thoughtful teacher revealing structure step by step: calm, dignified, engaged, and quietly compelling. Pronounce Arabic script naturally, not as Turkish spelling.",
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

Example request for the first `Bulgular` paragraph of `S096`:

```json
{
  "audioConfig": {
    "audioEncoding": "LINEAR16",
    "pitch": 0,
    "speakingRate": 1
  },
  "input": {
    "prompt": "Speak as a warm, low-mid Turkish narrator for long-form theological and linguistic commentary. Keep the voice reflective, easy on the ears, and gently forward-moving so the listener can follow the argument. Use clear Istanbul Turkish diction, natural pauses, and subtle emphasis on key insight sentences. The tone should feel like a thoughtful teacher revealing structure step by step: calm, dignified, engaged, and quietly compelling. Pronounce Arabic script naturally, not as Turkish spelling.",
    "text": "لَنَسْفَعًا بِالنَّاصِيَةِ tehdidinde iki kök birbirinin eksik rolünü tam olarak doldurur. سفع, başın önünden ya da perçemden zorla tutmayı, bununla birlikte gelen hâkimiyet ve aşağılamayı taşır; ناصية ise hem perçemi hem de ondan tutup çekmeyi adlandırır. Kuvvet, hedef, beden bölgesi ve sonuç tek bir sahnede kilitlenir. Ardından perçemin “yalancı, hatalı” diye nitelenmesi, yanlışı soyut bir hüküm olmaktan çıkarıp bedenin önünde okunur hale getirir."
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
v3/run/s096-full-20260716/96-publication.md
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

- Start from the source `{surah}-publication.md`.
- Apply the same text-cleaning and section-title rules used for TTS.
- Rename the file to the surah id, such as `S096.md`.
- Keep section headings readable as Markdown headings.
- Do not include the `## Bulgular` heading.
- Convert bracket labels into the first sentence of their subsection paragraph.
- Remove strength/rank prefixes from bracket labels and inline prose.
- Remove bold/italic markers.
- Preserve generated TTS chunk boundaries, not necessarily raw Markdown paragraph boundaries.

Example:

```md
# Asılı Başlangıçtan Yakınlığa: Alak Suresinde Ölçü, Taşkınlık ve Dönüş

Sure, ...

## Perçemden meclise uzanan rakip ön ve karşı çağrı

لَنَسْفَعًا بِالنَّاصِيَةِ tehdidinde ...
```

The Markdown copy is for review and editorial traceability. The app should read `chunks.jsonl` or `manifest.json`, not scrape `S096.md`.

## Paragraph Map JSONL

Write a `chunks.jsonl` file in the surah folder. This is the canonical paragraph-level mapping between text and audio.

Each line is one paragraph unit and must be valid JSON:

```json
{"surahId":"S096","source":"v3/run/s096-full-20260716/96-publication.md","chunkId":"sec-001-p-001","sectionIndex":1,"paragraphIndex":1,"kind":"section_title","sectionTitle":"Asılı Başlangıçtan Yakınlığa: Alak Suresinde Ölçü, Taşkınlık ve Dönüş","text":"Asılı Başlangıçtan Yakınlığa: Alak Suresinde Ölçü, Taşkınlık ve Dönüş","request":"requests/sec-001-p-001.json","response":"responses/sec-001-p-001.json","wav":"originals/wav/sec-001-p-001.wav","mp3":"originals/mp3/sec-001-p-001.mp3","durationSeconds":0}
```

Required fields:

- `surahId`: normalized folder id, such as `S096`.
- `source`: original source Markdown path.
- `chunkId`: stable id, such as `sec-003-p-002`.
- `sectionIndex`: 1-based section index.
- `paragraphIndex`: 1-based paragraph index within the section.
- `kind`: `section_title` or `paragraph`.
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
  "source": "v3/run/s096-full-20260716/96-publication.md",
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
