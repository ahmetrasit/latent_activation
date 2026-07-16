#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import re
from pathlib import Path


PROMPT = (
    "Speak as a warm, low-mid Turkish narrator for long-form theological and "
    "linguistic commentary. Keep the voice reflective, easy on the ears, and "
    "gently forward-moving so the listener can follow the argument. Use clear "
    "Istanbul Turkish diction, natural pauses, and subtle emphasis on key "
    "insight sentences. The tone should feel like a thoughtful teacher "
    "revealing structure step by step: calm, dignified, engaged, and quietly "
    "compelling. Pronounce Arabic script naturally, not as Turkish spelling."
)

AUDIO_CONFIG = {
    "audioEncoding": "LINEAR16",
    "pitch": 0,
    "speakingRate": 1,
}

VOICE = {
    "languageCode": "tr-TR",
    "modelName": "gemini-3.1-flash-tts-preview",
    "name": "Rasalgethi",
}


def normalize_surah_id(value):
    match = re.search(r"s0*(\d{1,3})\b", value, re.IGNORECASE)
    if not match:
        raise ValueError(f"Could not infer surah id from: {value}")
    return f"S{int(match.group(1)):03d}"


def validate_v3_source(source):
    parts = source.as_posix().split("/")
    if len(parts) < 4 or parts[0] != "v3" or parts[1] != "run" or parts[-1] != "publication.md":
        raise ValueError(
            f"Invalid source {source}. TTS generation only accepts "
            "v3/run/<surah-run>/publication.md files."
        )


def clean_inline(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = text.replace("**", "")
    text = text.replace("__", "")
    text = re.sub(r"(?<!\*)\*(?!\*)", "", text)
    text = re.sub(r"(?<!_)_(?!_)", "", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def strip_list_marker(line):
    line = re.sub(r"^\s*[-+*]\s+", "", line)
    line = re.sub(r"^\s*\d+[.)]\s+", "", line)
    return line


def atomic_write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp")
    tmp_path.write_text(text, encoding="utf-8")
    os.replace(tmp_path, path)


def stable_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def heading_text(line):
    return clean_inline(re.sub(r"^#{1,6}\s+", "", line).strip())


def bracket_title(line):
    content = line.strip()[1:-1].strip()
    if "—" in content:
        content = content.split("—", 1)[1]
    return clean_inline(content)


def flush_paragraph(lines):
    text = clean_inline(" ".join(strip_list_marker(line).strip() for line in lines))
    return text or None


def parse_publication(source):
    raw_lines = source.read_text(encoding="utf-8").splitlines()
    sections = []
    current = None
    paragraph_lines = []
    skip_fenced = False
    skip_html_comment = False
    in_frontmatter = raw_lines[:1] == ["---"]
    frontmatter_open = in_frontmatter

    def ensure_section(title):
        nonlocal current
        current = {"title": title, "paragraphs": []}
        current["paragraphs"].append({"kind": "section_title", "text": title})
        sections.append(current)

    def flush_into_current():
        nonlocal paragraph_lines
        text = flush_paragraph(paragraph_lines)
        paragraph_lines = []
        if text:
            if current is None:
                ensure_section("Anlatım")
            current["paragraphs"].append({"kind": "paragraph", "text": text})

    for line in raw_lines:
        stripped = line.strip()

        if in_frontmatter:
            if frontmatter_open:
                frontmatter_open = False
                continue
            if stripped == "---":
                in_frontmatter = False
            continue

        if skip_html_comment:
            if "-->" in stripped:
                skip_html_comment = False
                stripped = stripped.split("-->", 1)[1].strip()
                if not stripped:
                    continue
            else:
                continue

        if stripped.startswith("<!--"):
            if "-->" not in stripped:
                skip_html_comment = True
                continue
            stripped = stripped.split("-->", 1)[1].strip()
            if not stripped:
                continue

        if stripped.startswith("```"):
            skip_fenced = not skip_fenced
            continue
        if skip_fenced:
            continue
        if not stripped:
            flush_into_current()
            continue
        h_match = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if h_match:
            flush_into_current()
            title = heading_text(stripped)
            if title.casefold() == "bulgular":
                continue
            if re.match(r"^\[[^\n]+\]$", title):
                ensure_section(bracket_title(title))
                continue
            ensure_section(title)
            continue

        if re.match(r"^\[[^\n]+\]$", stripped):
            flush_into_current()
            ensure_section(bracket_title(stripped))
            continue

        paragraph_lines.append(line)

    flush_into_current()
    return sections


def write_clean_markdown(path, sections):
    lines = []
    for index, section in enumerate(sections, start=1):
        heading = "#" if index == 1 else "##"
        lines.append(f"{heading} {section['title']}")
        lines.append("")
        for paragraph in section["paragraphs"]:
            if paragraph["kind"] == "section_title":
                continue
            lines.append(paragraph["text"])
            lines.append("")
    atomic_write_text(path, "\n".join(lines).rstrip() + "\n")


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_request(text):
    return {
        "audioConfig": AUDIO_CONFIG,
        "input": {
            "prompt": PROMPT,
            "text": text,
        },
        "voice": VOICE,
    }


def tts_text_for(paragraph):
    text = paragraph["text"]
    if paragraph["kind"] != "section_title":
        return text
    if text.endswith((".", "!", "?", ":", "؛", "؟")):
        return text
    return f"{text}."


def request_hash(request):
    return sha256_text(stable_json(request))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--out-root", type=Path, default=Path("_audio/audio"))
    parser.add_argument("--surah-id")
    args = parser.parse_args()

    source = args.source
    validate_v3_source(source)
    surah_id = args.surah_id or normalize_surah_id(str(source))
    out_dir = args.out_root / surah_id
    requests_dir = out_dir / "requests"
    responses_dir = out_dir / "responses"
    wav_dir = out_dir / "wav"
    mp3_dir = out_dir / "mp3"

    for directory in (requests_dir, responses_dir, wav_dir, mp3_dir):
        directory.mkdir(parents=True, exist_ok=True)

    sections = parse_publication(source)
    write_clean_markdown(out_dir / f"{surah_id}.md", sections)

    chunks = []
    prompt_hash = sha256_text(PROMPT)
    for section_index, section in enumerate(sections, start=1):
        section_chunks = []
        for paragraph_index, paragraph in enumerate(section["paragraphs"], start=1):
            chunk_id = f"sec-{section_index:03d}-p-{paragraph_index:03d}"
            request_path = requests_dir / f"{chunk_id}.json"
            response_rel = f"responses/{chunk_id}.json"
            wav_rel = f"wav/{chunk_id}.wav"
            tts_text = tts_text_for(paragraph)
            request = build_request(tts_text)
            request_sha256 = request_hash(request)
            atomic_write_text(
                request_path,
                json.dumps(request, ensure_ascii=False, indent=2) + "\n",
            )
            record = {
                "surahId": surah_id,
                "source": str(source),
                "chunkId": chunk_id,
                "sectionIndex": section_index,
                "paragraphIndex": paragraph_index,
                "kind": paragraph["kind"],
                "sectionTitle": section["title"],
                "text": paragraph["text"],
                "ttsText": tts_text,
                "request": f"requests/{chunk_id}.json",
                "response": response_rel,
                "wav": wav_rel,
                "mp3": None,
                "durationSeconds": None,
                "charCount": len(paragraph["text"]),
                "wordCount": len(paragraph["text"].split()),
                "textSha256": sha256_text(paragraph["text"]),
                "promptSha256": prompt_hash,
                "voiceSha256": sha256_text(stable_json(VOICE)),
                "audioConfigSha256": sha256_text(stable_json(AUDIO_CONFIG)),
                "requestSha256": request_sha256,
            }
            chunks.append(record)
            section_chunks.append(record)
        section["chunks"] = section_chunks

    atomic_write_text(
        out_dir / "chunks.jsonl",
        "".join(json.dumps(chunk, ensure_ascii=False) + "\n" for chunk in chunks),
    )

    manifest = {
        "source": str(source),
        "surahId": surah_id,
        "surahRun": source.parent.name,
        "cleanMarkdown": f"{surah_id}.md",
        "chunksJsonl": "chunks.jsonl",
        "prompt": PROMPT,
        "promptSha256": prompt_hash,
        "voice": VOICE,
        "audioConfig": AUDIO_CONFIG,
        "chunkCount": len(chunks),
        "sections": [
            {
                "sectionIndex": index,
                "title": section["title"],
                "paragraphs": [
                    {
                        key: chunk[key]
                        for key in (
                            "paragraphIndex",
                            "kind",
                            "chunkId",
                            "text",
                            "ttsText",
                            "request",
                            "response",
                            "wav",
                            "mp3",
                            "durationSeconds",
                        )
                    }
                    for chunk in section["chunks"]
                ],
            }
            for index, section in enumerate(sections, start=1)
        ],
    }
    atomic_write_text(
        out_dir / "manifest.json",
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
    )

    print(json.dumps({"outDir": str(out_dir), "chunks": len(chunks)}, indent=2))


if __name__ == "__main__":
    main()
