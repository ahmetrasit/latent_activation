#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
V3_SCRIPTS_ROOT = REPO_ROOT / "v3" / "scripts"
sys.path.insert(0, str(V3_SCRIPTS_ROOT))

from publication_contract import (  # noqa: E402
    PublicationError,
    load_publication,
    publication_sections,
)


PROMPT = (
    "Speak as a warm, conversational Turkish narrator addressing one curious "
    "listener. Sound like a thoughtful person sharing a discovery as it becomes "
    "clear, with natural human cadence, varied sentence energy, and quiet "
    "curiosity. Let short reveal sentences land, then slow slightly for "
    "explanation. Use clear Istanbul Turkish diction and natural pauses. Avoid "
    "sermon, classroom lecture, documentary-announcer delivery, exaggerated "
    "drama, and a repeated rhetorical rise-and-fall. Do not give every section "
    "the same cadence. Pronounce Arabic Quranic words naturally as Arabic, then "
    "return smoothly to Turkish."
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
    try:
        relative = source.resolve().relative_to(REPO_ROOT)
    except ValueError as error:
        raise ValueError(f"Source must be inside the repository: {source}") from error
    parts = relative.parts
    filename = parts[-1] if parts else ""
    numbered_match = re.match(r"^(\d{1,3})-publication\.(jsonl|md)$", filename)
    valid_publication_name = filename == "publication.md" or numbered_match
    if len(parts) < 4 or parts[0] != "v3" or parts[1] != "run" or not valid_publication_name:
        raise ValueError(
            f"Invalid source {source}. TTS generation only accepts "
            "v3/run/<surah-run>/<surah>-publication.jsonl files, with Markdown "
            "accepted only for legacy runs."
        )
    if numbered_match:
        run_match = re.search(r"s0*(\d{1,3})\b", parts[2], re.IGNORECASE)
        if not run_match or int(run_match.group(1)) != int(numbered_match.group(1)):
            raise ValueError(
                f"Invalid source {source}. Numbered publication file must match "
                "the surah id in v3/run/<surah-run>."
            )
        if numbered_match.group(2) == "md":
            canonical = source.with_suffix(".jsonl")
            if canonical.is_file():
                raise ValueError(
                    f"Canonical JSONL exists for {source}; use {canonical} instead."
                )
    elif filename == "publication.md":
        run_match = re.search(r"s0*(\d{1,3})\b", parts[2], re.IGNORECASE)
        if run_match:
            canonical = source.parent / f"{int(run_match.group(1))}-publication.jsonl"
            if canonical.is_file():
                raise ValueError(
                    f"Canonical JSONL exists for {source}; use {canonical} instead."
                )


def canonical_source_path(source):
    return source.resolve().relative_to(REPO_ROOT).as_posix()


def clean_inline(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = replace_rank_labels(text)
    text = text.replace("**", "")
    text = text.replace("__", "")
    text = re.sub(r"(?<!\*)\*(?!\*)", "", text)
    text = re.sub(r"(?<!_)_(?!_)", "", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = remove_inline_rank_strength(text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    return text.strip()


def sentence_punctuate(text):
    text = text.strip()
    if text.endswith((".", "!", "?", ":", ";", "؛", "؟")):
        return text
    return f"{text}."


def section_title_text(text):
    text = clean_inline(text)
    return re.sub(r"[.!?;:؛؟]+$", "", text).strip()


def rank_label_title(content):
    if "—" in content:
        content = content.split("—", 1)[1]
    return re.sub(r"\s+", " ", content).strip()


def rank_label_text(content):
    return sentence_punctuate(rank_label_title(content))


def replace_rank_labels(text):
    def repl(match):
        content = match.group(1).strip()
        if not re.search(r"\b(GÜÇLÜ|ORTA|ZAYIF)\b", content):
            return match.group(0)
        return rank_label_text(content)

    return re.sub(r"\[([^\]\n]+)\]", repl, text)


def remove_inline_rank_strength(text):
    return re.sub(
        r"\b(?:GÜÇLÜ|ORTA|ZAYIF)\s*/\s*[A-Z](?:-[\wçğıöşüÇĞİÖŞÜ]+)?"
        r"(?:\s+düzeyinde(?:dir)?)?\b",
        "",
        text,
    )


def split_rank_labeled_paragraph(text):
    matches = list(re.finditer(r"\[([^\]\n]+)\]", text))
    rank_matches = [
        match
        for match in matches
        if re.search(r"\b(GÜÇLÜ|ORTA|ZAYIF)\b", match.group(1))
    ]
    if not rank_matches:
        cleaned = clean_inline(text)
        return [cleaned] if cleaned else []

    segments = []
    prefix = text[: rank_matches[0].start()].strip()
    if prefix:
        segments.append(prefix)

    for index, match in enumerate(rank_matches):
        end = rank_matches[index + 1].start() if index + 1 < len(rank_matches) else len(text)
        label = rank_label_text(match.group(1).strip())
        body = text[match.end() : end].strip()
        segments.append(f"{label} {body}".strip())

    cleaned_segments = []
    for segment in segments:
        cleaned = clean_inline(segment)
        if cleaned:
            cleaned_segments.append(cleaned)
    return cleaned_segments


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


def cleanup_unreferenced_files(paths):
    for directory, referenced in paths:
        if not directory.exists():
            continue
        referenced = {path.resolve() for path in referenced}
        for path in directory.glob("*"):
            if path.is_file() and path.resolve() not in referenced:
                path.unlink()


def heading_text(line):
    return clean_inline(re.sub(r"^#{1,6}\s+", "", line).strip())


def bracket_title(line):
    content = line.strip()[1:-1].strip()
    return section_title_text(rank_label_title(content))


def bracket_tts_prefix(line):
    content = line.strip()[1:-1].strip()
    return rank_label_text(content)


def flush_paragraph(lines):
    text = " ".join(strip_list_marker(line).strip() for line in lines)
    return split_rank_labeled_paragraph(text)


def parse_markdown_publication(source):
    raw_lines = source.read_text(encoding="utf-8").splitlines()
    sections = []
    current = None
    paragraph_lines = []
    pending_subsection_title = None
    skip_fenced = False
    skip_html_comment = False
    in_frontmatter = raw_lines[:1] == ["---"]
    frontmatter_open = in_frontmatter

    def ensure_section(title):
        nonlocal current
        title = section_title_text(title)
        current = {"title": title, "paragraphs": []}
        current["paragraphs"].append({"kind": "section_title", "text": title})
        sections.append(current)

    def flush_into_current():
        nonlocal paragraph_lines, pending_subsection_title
        texts = flush_paragraph(paragraph_lines) if paragraph_lines else []
        paragraph_lines = []
        if pending_subsection_title:
            if texts:
                texts[0] = f"{pending_subsection_title} {texts[0]}".strip()
            pending_subsection_title = None
        for text in texts:
            if current is None:
                ensure_section("Anlatım")
            current["paragraphs"].append({"kind": "paragraph", "text": text})

    def start_subsection(title):
        nonlocal pending_subsection_title
        flush_into_current()
        pending_subsection_title = title

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
            if not pending_subsection_title:
                flush_into_current()
            continue
        h_match = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if h_match:
            flush_into_current()
            title = heading_text(stripped)
            if title.casefold() in {
                "bulgular",
                "ana bulgular",
                "tamamlayıcı bulgular",
                "ince kayıtlar",
            }:
                continue
            if re.match(r"^\[[^\n]+\]$", title):
                start_subsection(bracket_tts_prefix(title))
                continue
            ensure_section(title)
            continue

        bold_match = re.match(r"^\*\*(.+?)\*\*\s*(.*)$", stripped)
        if bold_match and re.match(
            r"^\[[^\]\n]*\b(GÜÇLÜ|ORTA|ZAYIF)\b[^\]\n]*\]$",
            bold_match.group(1).strip(),
        ):
            start_subsection(bracket_tts_prefix(bold_match.group(1).strip()))
            rest = bold_match.group(2).strip()
            if rest:
                paragraph_lines.append(rest)
            continue

        bold_prefixed_label_match = re.match(
            r"^\*\*[^*]+?\*\*\s*"
            r"(\[[^\]\n]*\b(?:GÜÇLÜ|ORTA|ZAYIF)\b[^\]\n]*\])\s*(.*)$",
            stripped,
        )
        if bold_prefixed_label_match:
            start_subsection(bracket_tts_prefix(bold_prefixed_label_match.group(1)))
            rest = bold_prefixed_label_match.group(2).strip()
            if rest:
                paragraph_lines.append(rest)
            continue

        if re.match(r"^\[[^\n]+\]$", stripped):
            start_subsection(bracket_tts_prefix(stripped))
            continue

        paragraph_lines.append(line)

    flush_into_current()
    return sections


def parse_publication(source):
    if source.suffix.casefold() == ".jsonl":
        try:
            return publication_sections(load_publication(source))
        except PublicationError as error:
            raise ValueError(str(error)) from error
    return parse_markdown_publication(source)


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
    source_path = canonical_source_path(source)
    surah_id = args.surah_id or normalize_surah_id(str(source))
    out_dir = args.out_root / surah_id
    requests_dir = out_dir / "requests"
    responses_dir = out_dir / "responses"
    originals_wav_dir = out_dir / "originals" / "wav"
    originals_mp3_dir = out_dir / "originals" / "mp3"
    sections_wav_dir = out_dir / "sections" / "wav"
    sections_mp3_dir = out_dir / "sections" / "mp3"

    for directory in (
        requests_dir,
        responses_dir,
        originals_wav_dir,
        originals_mp3_dir,
        sections_wav_dir,
        sections_mp3_dir,
    ):
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
            wav_rel = f"originals/wav/{chunk_id}.wav"
            mp3_rel = f"originals/mp3/{chunk_id}.mp3"
            tts_text = tts_text_for(paragraph)
            request = build_request(tts_text)
            request_sha256 = request_hash(request)
            atomic_write_text(
                request_path,
                json.dumps(request, ensure_ascii=False, indent=2) + "\n",
            )
            record = {
                "surahId": surah_id,
                "source": source_path,
                "chunkId": chunk_id,
                "sectionIndex": section_index,
                "paragraphIndex": paragraph_index,
                "kind": paragraph["kind"],
                "publicationKind": section.get("kind", "legacy"),
                "grades": list(section.get("grades", [])),
                "sectionTitle": section["title"],
                "text": paragraph["text"],
                "ttsText": tts_text,
                "request": f"requests/{chunk_id}.json",
                "response": response_rel,
                "wav": wav_rel,
                "mp3": mp3_rel,
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
        "source": source_path,
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
                "kind": section.get("kind", "legacy"),
                "grades": list(section.get("grades", [])),
                "wav": f"sections/wav/sec-{index:03d}.wav",
                "mp3": f"sections/mp3/sec-{index:03d}.mp3",
                "durationSeconds": None,
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
    cleanup_unreferenced_files(
        [
            (requests_dir, [out_dir / chunk["request"] for chunk in chunks]),
            (responses_dir, [out_dir / chunk["response"] for chunk in chunks]),
            (originals_wav_dir, [out_dir / chunk["wav"] for chunk in chunks]),
            (originals_mp3_dir, [out_dir / chunk["mp3"] for chunk in chunks]),
            (
                sections_wav_dir,
                [out_dir / section["wav"] for section in manifest["sections"]],
            ),
            (
                sections_mp3_dir,
                [out_dir / section["mp3"] for section in manifest["sections"]],
            ),
        ]
    )

    print(json.dumps({"outDir": str(out_dir), "chunks": len(chunks)}, indent=2))


if __name__ == "__main__":
    main()
