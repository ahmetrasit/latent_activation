#!/usr/bin/env python3
import argparse
import base64
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
import wave
from pathlib import Path


ENDPOINT = "https://texttospeech.googleapis.com/v1beta1/text:synthesize"
PROJECT_ID = "quran-roots"
SAMPLE_RATE = 24000
BYTES_PER_SAMPLE = 2
CHANNELS = 1
WAV_HEADER_BYTES = 44
MP3_BITRATE_BPS = "64000"
MP3_BITRATE_FFMPEG = "64k"


def atomic_write_bytes(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp")
    tmp_path.write_bytes(payload)
    os.replace(tmp_path, path)


def atomic_write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp")
    tmp_path.write_text(text, encoding="utf-8")
    os.replace(tmp_path, path)


def stable_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(payload):
    return hashlib.sha256(payload).hexdigest()


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_jsonl(path):
    records = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))
    return records


def write_jsonl(path, records):
    atomic_write_text(
        path,
        "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in records),
    )


def get_token():
    result = subprocess.run(
        ["gcloud", "auth", "print-access-token"],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def synthesize(request_path, response_path, token, chunk, generated_at):
    body = request_path.read_bytes()
    request = urllib.request.Request(
        ENDPOINT,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "x-goog-user-project": PROJECT_ID,
            "Content-Type": "application/json; charset=utf-8",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            payload = response.read()
    except urllib.error.HTTPError as error:
        payload = error.read()
    response = json.loads(payload.decode("utf-8"))
    response["_generatedAt"] = generated_at
    write_response(response_path, response, chunk)
    return response


def wav_duration_seconds(path):
    with wave.open(str(path), "rb") as handle:
        if handle.getnchannels() != CHANNELS:
            raise ValueError(f"Unexpected channel count in {path}: {handle.getnchannels()}")
        if handle.getframerate() != SAMPLE_RATE:
            raise ValueError(f"Unexpected sample rate in {path}: {handle.getframerate()}")
        if handle.getsampwidth() != BYTES_PER_SAMPLE:
            raise ValueError(f"Unexpected sample width in {path}: {handle.getsampwidth()}")
        frames = handle.getnframes()
        if frames <= 0:
            raise ValueError(f"No audio frames in {path}")
        return frames / SAMPLE_RATE


def validate_wav_bytes(payload):
    tmp_path = None
    try:
        import tempfile

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp.write(payload)
            tmp_path = Path(tmp.name)
        wav_duration_seconds(tmp_path)
    finally:
        if tmp_path and tmp_path.exists():
            tmp_path.unlink()


def decode_audio_response(response):
    if "error" in response:
        return None
    audio_content = response.get("audioContent")
    if not audio_content:
        raise ValueError("Response has no audioContent")
    payload = base64.b64decode(audio_content)
    validate_wav_bytes(payload)
    return payload


def response_matches_chunk(response, chunk):
    if "error" in response:
        return False
    metadata = response.get("_requestMetadata")
    if not metadata:
        return False
    keys = (
        "requestSha256",
        "textSha256",
        "promptSha256",
        "voiceSha256",
        "audioConfigSha256",
    )
    return all(metadata.get(key) == chunk.get(key) for key in keys)


def request_metadata(chunk):
    return {
        key: chunk.get(key)
        for key in (
            "requestSha256",
            "textSha256",
            "promptSha256",
            "voiceSha256",
            "audioConfigSha256",
        )
    }


def validate_request_file(request_path, chunk):
    request = json.loads(request_path.read_text(encoding="utf-8"))
    request_sha256 = sha256_text(stable_json(request))
    if request_sha256 != chunk.get("requestSha256"):
        raise ValueError(
            f"{chunk['chunkId']} request hash mismatch: file={request_sha256} "
            f"chunk={chunk.get('requestSha256')}"
        )
    expected_text = chunk.get("ttsText", chunk["text"])
    if request.get("input", {}).get("text") != expected_text:
        raise ValueError(f"{chunk['chunkId']} request text does not match chunk ttsText")
    if sha256_text(request.get("input", {}).get("prompt", "")) != chunk.get("promptSha256"):
        raise ValueError(f"{chunk['chunkId']} request prompt hash mismatch")
    if sha256_text(stable_json(request.get("voice"))) != chunk.get("voiceSha256"):
        raise ValueError(f"{chunk['chunkId']} request voice hash mismatch")
    if sha256_text(stable_json(request.get("audioConfig"))) != chunk.get("audioConfigSha256"):
        raise ValueError(f"{chunk['chunkId']} request audioConfig hash mismatch")


def update_manifest(manifest_path, records_by_chunk_id):
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for section in manifest.get("sections", []):
        for paragraph in section.get("paragraphs", []):
            record = records_by_chunk_id.get(paragraph.get("chunkId"))
            if not record:
                continue
            paragraph["wav"] = record.get("wav")
            paragraph["mp3"] = record.get("mp3")
            paragraph["durationSeconds"] = record.get("durationSeconds")
            paragraph["generatedAt"] = record.get("generatedAt")
    atomic_write_text(
        manifest_path,
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
    )


def load_response(path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def write_response(path, response, chunk):
    response = dict(response)
    response["_requestMetadata"] = request_metadata(chunk)
    atomic_write_text(path, json.dumps(response, ensure_ascii=False, indent=2) + "\n")


def materialize_wav_from_response(response, wav_path):
    audio = decode_audio_response(response)
    atomic_write_bytes(wav_path, audio)
    return round(wav_duration_seconds(wav_path), 3), sha256_bytes(audio)


def convert_wav_to_mp3(wav_path, mp3_path):
    ffmpeg = shutil.which("ffmpeg")
    afconvert = shutil.which("afconvert")
    if not ffmpeg and not afconvert:
        raise RuntimeError("ffmpeg or afconvert is required to create MP3 derivatives")
    mp3_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = mp3_path.with_name(f".{mp3_path.stem}.tmp.mp3")
    if tmp_path.exists():
        tmp_path.unlink()
    if ffmpeg:
        subprocess.run(
            [
                ffmpeg,
                "-y",
                "-hide_banner",
                "-loglevel",
                "error",
                "-i",
                str(wav_path),
                "-vn",
                "-codec:a",
                "libmp3lame",
                "-b:a",
                MP3_BITRATE_FFMPEG,
                str(tmp_path),
            ],
            check=True,
            text=True,
            capture_output=True,
        )
    else:
        subprocess.run(
            [
                afconvert,
                str(wav_path),
                str(tmp_path),
                "-f",
                "MPG3",
                "-d",
                ".mp3",
                "-b",
                MP3_BITRATE_BPS,
            ],
            check=True,
            text=True,
            capture_output=True,
        )
    os.replace(tmp_path, mp3_path)
    return sha256_bytes(mp3_path.read_bytes())


def join_wavs(input_paths, output_path):
    if not input_paths:
        return None, None
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = output_path.with_name(f".{output_path.name}.tmp")
    params = None
    with wave.open(str(tmp_path), "wb") as output:
        for input_path in input_paths:
            with wave.open(str(input_path), "rb") as source:
                current_params = source.getparams()
                expected = (CHANNELS, BYTES_PER_SAMPLE, SAMPLE_RATE)
                actual = (
                    source.getnchannels(),
                    source.getsampwidth(),
                    source.getframerate(),
                )
                if actual != expected:
                    raise ValueError(f"Unexpected WAV params in {input_path}: {actual}")
                if params is None:
                    params = current_params
                    output.setparams(current_params)
                elif current_params[:3] != params[:3]:
                    raise ValueError(f"WAV params differ in {input_path}")
                output.writeframes(source.readframes(source.getnframes()))
    os.replace(tmp_path, output_path)
    return round(wav_duration_seconds(output_path), 3), sha256_bytes(output_path.read_bytes())


def materialize_original_mp3(surah_dir, chunk):
    wav_path = surah_dir / chunk["wav"]
    mp3_rel = chunk.get("mp3")
    if not mp3_rel or not wav_path.exists():
        return
    mp3_path = surah_dir / mp3_rel
    chunk["mp3Sha256"] = convert_wav_to_mp3(wav_path, mp3_path)


def remove_file_if_exists(path):
    if path.exists():
        path.unlink()


def section_audio_paths(surah_dir, section):
    section_index = section["sectionIndex"]
    section_wav_rel = section.get("wav") or f"sections/wav/sec-{section_index:03d}.wav"
    section_mp3_rel = section.get("mp3") or f"sections/mp3/sec-{section_index:03d}.mp3"
    return section_wav_rel, section_mp3_rel, surah_dir / section_wav_rel, surah_dir / section_mp3_rel


def clear_section_derivative(surah_dir, section):
    section_wav_rel, section_mp3_rel, section_wav_path, section_mp3_path = section_audio_paths(
        surah_dir, section
    )
    remove_file_if_exists(section_wav_path)
    remove_file_if_exists(section_mp3_path)
    section["wav"] = section_wav_rel
    section["mp3"] = section_mp3_rel
    section["durationSeconds"] = None
    section.pop("wavSha256", None)
    section.pop("mp3Sha256", None)


def chunk_has_verified_audio(chunk, wav_path):
    return (
        wav_path.exists()
        and chunk.get("durationSeconds") is not None
        and bool(chunk.get("audioSha256"))
    )


def build_section_derivatives(surah_dir, manifest_path, chunks, eligible_chunk_ids=None):
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    chunks_by_id = {chunk["chunkId"]: chunk for chunk in chunks}
    for section in manifest.get("sections", []):
        paragraph_ids = [
            paragraph["chunkId"]
            for paragraph in section.get("paragraphs", [])
            if paragraph.get("chunkId")
        ]
        paragraph_chunks = [
            chunks_by_id[paragraph["chunkId"]]
            for paragraph in section.get("paragraphs", [])
            if paragraph.get("chunkId") in chunks_by_id
        ]
        if len(paragraph_chunks) != len(paragraph_ids):
            clear_section_derivative(surah_dir, section)
            continue
        if eligible_chunk_ids is not None and any(
            chunk["chunkId"] not in eligible_chunk_ids for chunk in paragraph_chunks
        ):
            clear_section_derivative(surah_dir, section)
            continue
        wav_paths = [surah_dir / chunk["wav"] for chunk in paragraph_chunks]
        if not wav_paths or any(
            not chunk_has_verified_audio(chunk, path)
            for chunk, path in zip(paragraph_chunks, wav_paths)
        ):
            clear_section_derivative(surah_dir, section)
            continue
        section_wav_rel, section_mp3_rel, section_wav_path, section_mp3_path = section_audio_paths(
            surah_dir, section
        )
        duration_seconds, wav_sha256 = join_wavs(wav_paths, section_wav_path)
        mp3_sha256 = convert_wav_to_mp3(section_wav_path, section_mp3_path)
        section["wav"] = section_wav_rel
        section["mp3"] = section_mp3_rel
        section["durationSeconds"] = duration_seconds
        section["wavSha256"] = wav_sha256
        section["mp3Sha256"] = mp3_sha256
    atomic_write_text(
        manifest_path,
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("surah_dir", type=Path)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    surah_dir = args.surah_dir
    chunks_path = surah_dir / "chunks.jsonl"
    manifest_path = surah_dir / "manifest.json"
    chunks = load_jsonl(chunks_path)
    token = get_token()
    processed = 0
    target_chunks = chunks[: args.limit] if args.limit is not None else chunks
    eligible_chunk_ids = {chunk["chunkId"] for chunk in target_chunks}

    for index, chunk in enumerate(target_chunks, start=1):
        request_path = surah_dir / chunk["request"]
        response_path = surah_dir / chunk["response"]
        wav_path = surah_dir / chunk["wav"]
        validate_request_file(request_path, chunk)

        existing_response = None if args.force else load_response(response_path)
        if existing_response and response_matches_chunk(existing_response, chunk):
            duration_seconds, audio_sha256 = materialize_wav_from_response(
                existing_response, wav_path
            )
            chunk["durationSeconds"] = duration_seconds
            chunk["audioSha256"] = audio_sha256
            materialize_original_mp3(surah_dir, chunk)
            chunk["generatedAt"] = chunk.get("generatedAt") or existing_response.get(
                "_generatedAt"
            )
            processed += 1
            continue

        if wav_path.exists() and not args.force:
            print(
                f"{chunk['chunkId']} has a WAV but no matching response metadata; "
                "use --force to regenerate or remove the stale WAV.",
                file=sys.stderr,
            )
            write_jsonl(chunks_path, chunks)
            update_manifest(manifest_path, {record["chunkId"]: record for record in chunks})
            return 1

        print(f"{index}/{len(chunks)} {chunk['chunkId']}...", flush=True)
        generated_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        response = synthesize(request_path, response_path, token, chunk, generated_at)
        if "error" in response:
            print(json.dumps(response["error"], ensure_ascii=False, indent=2), file=sys.stderr)
            write_jsonl(chunks_path, chunks)
            update_manifest(manifest_path, {record["chunkId"]: record for record in chunks})
            return 1

        audio = decode_audio_response(response)
        atomic_write_bytes(wav_path, audio)
        chunk["durationSeconds"] = round(wav_duration_seconds(wav_path), 3)
        chunk["audioSha256"] = sha256_bytes(audio)
        materialize_original_mp3(surah_dir, chunk)
        chunk["generatedAt"] = generated_at
        processed += 1

    write_jsonl(chunks_path, chunks)
    update_manifest(manifest_path, {record["chunkId"]: record for record in chunks})
    build_section_derivatives(
        surah_dir,
        manifest_path,
        chunks,
        eligible_chunk_ids=eligible_chunk_ids if args.limit is not None else None,
    )
    print(json.dumps({"processed": processed, "chunks": len(chunks)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
