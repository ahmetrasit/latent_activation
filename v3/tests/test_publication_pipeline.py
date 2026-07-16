from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PACKAGE_ROOT.parent
SCRIPTS_ROOT = PACKAGE_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_ROOT))

import make_tasks  # noqa: E402
import publication_contract  # noqa: E402


def load_audio_preparer():
    path = REPO_ROOT / "_audio" / "scripts" / "prepare_tts_chunks.py"
    spec = importlib.util.spec_from_file_location("prepare_tts_chunks_v3_test", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load audio preparer: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIO_PREPARER = load_audio_preparer()


def valid_records() -> list[dict[str, object]]:
    return [
        {
            "kind": "opening",
            "grades": [],
            "title": "Yol Söylenmeden Önce",
            "paragraphs": ["Yol daha adı konmadan hazırlanır."],
        },
        {
            "kind": "finding",
            "grades": ["GÜÇLÜ / A"],
            "title": "Kulluğun Açtığı Zemin",
            "paragraphs": [
                "İlk hareket bir yolculuktan çok daha önce başlar.",
                (
                    "Yol anlamındaki ٱلصِّرَٰطَ sözü geldiğinde, hazırlanmış zemin "
                    "artık görünür hale gelir."
                ),
            ],
        },
        {
            "kind": "closing",
            "grades": [],
            "title": "Son Geçiş",
            "paragraphs": [
                "Açılışta kurulan yön, kapanışta kaybolma ihtimaliyle tamamlanır."
            ],
        },
    ]


def write_jsonl(path: Path, records: list[dict[str, object]]) -> None:
    path.write_text(
        "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in records),
        encoding="utf-8",
    )


class PublicationContractTests(unittest.TestCase):
    def test_schema_and_prompt_keep_the_format_small(self) -> None:
        schema = json.loads(
            (PACKAGE_ROOT / "schemas" / "publication-record.schema.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(
            ["kind", "grades", "title", "paragraphs"],
            schema["required"],
        )
        self.assertFalse(schema["additionalProperties"])

        prompt = (
            PACKAGE_ROOT / "prompts" / "a2-publication-tr-audio-first.md"
        ).read_text(encoding="utf-8")
        for field in ("kind", "grades", "title", "paragraphs"):
            self.assertIn(f'"{field}"', prompt)
        self.assertIn("Never write or speak a bare spaced root", prompt)
        self.assertIn("silent", prompt.casefold())
        self.assertIn("camera", prompt.casefold())
        self.assertNotIn("Nouman", prompt)

    def test_orchestration_tracks_the_audio_first_contract(self) -> None:
        orchestration = (PACKAGE_ROOT / "00_orchestration_spec.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("a2-publication-tr-audio-first.md", orchestration)
        self.assertIn("publication-record.schema.json", orchestration)
        self.assertIn("<surah>-publication.jsonl", orchestration)
        self.assertIn("TTS preparation reads that JSONL directly", orchestration)
        self.assertIn("S1 and S112", orchestration)
        self.assertIn("Batch-production gate", orchestration)
        self.assertNotIn("a2-publication-tr-compact-v2.md", orchestration)

    def test_valid_records_render_without_grades_in_markdown(self) -> None:
        records = valid_records()
        self.assertEqual([], publication_contract.validate_records(records))
        markdown = publication_contract.render_markdown(records)
        self.assertIn("# Yol Söylenmeden Önce", markdown)
        self.assertIn("## Kulluğun Açtığı Zemin", markdown)
        self.assertNotIn("GÜÇLÜ / A", markdown)

        sections = publication_contract.publication_sections(records)
        self.assertEqual(["opening", "finding", "closing"], [s["kind"] for s in sections])
        self.assertEqual(["GÜÇLÜ / A"], sections[1]["grades"])
        self.assertEqual(3, len(sections[1]["paragraphs"]))

    def test_contract_rejects_spoken_metadata_and_production_language(self) -> None:
        records = valid_records()
        finding = records[1]
        finding["title"] = "Kamera Kuyuya Yaklaşır"
        finding["paragraphs"] = [
            "Dosdoğru anlamındaki ق و م kökü burada GÜÇLÜ / A düzeyindedir."
        ]
        errors = publication_contract.validate_records(records)
        self.assertTrue(any("production vocabulary" in error for error in errors))
        self.assertTrue(any("spoken grade codes" in error for error in errors))
        self.assertTrue(any("bare spaced Arabic root" in error for error in errors))

    def test_style_checks_warn_without_changing_the_contract(self) -> None:
        records = valid_records()
        template = {
            "kind": "finding",
            "grades": ["GÜÇLÜ / C-koşullu"],
            "title": "Sınırlı Yankı",
            "paragraphs": [
                "Metin bunu söylemez. Yine de uzakta bir ihtimal belirir.",
                "Böylece sınır korunur.",
            ],
        }
        records[1:2] = [dict(template), dict(template), dict(template)]
        self.assertEqual([], publication_contract.validate_records(records))
        warnings = publication_contract.style_warnings(records)
        self.assertTrue(any("mechanical boundary" in warning for warning in warnings))
        self.assertTrue(any("adjacent findings share" in warning for warning in warnings))
        self.assertTrue(any("finding title" in warning for warning in warnings))
        self.assertTrue(any("finding openings repeat" in warning for warning in warnings))
        self.assertTrue(any("conclusions repeat" in warning for warning in warnings))

    def test_renderer_cli_writes_the_deterministic_derivative(self) -> None:
        with tempfile.TemporaryDirectory(prefix="publication-render-test-") as temporary:
            source = Path(temporary) / "1-publication.jsonl"
            write_jsonl(source, valid_records())
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS_ROOT / "render_publication.py"),
                    str(source),
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            output = source.with_suffix(".md")
            self.assertTrue(output.is_file())
            self.assertEqual(
                publication_contract.render_markdown(valid_records()),
                output.read_text(encoding="utf-8"),
            )


class TaskGenerationTests(unittest.TestCase):
    def test_turn_four_targets_audio_first_jsonl(self) -> None:
        with tempfile.TemporaryDirectory(prefix="v3-task-test-") as temporary:
            run_root = Path(temporary) / "s001-test"
            for directory in ("inputs", "tasks", "a1", "a2"):
                (run_root / directory).mkdir(parents=True, exist_ok=True)
            inputs = run_root / "inputs"
            (inputs / "passage-arabic.txt").write_text(
                "1:1\tin-scope\tبِسْمِ\n", encoding="utf-8"
            )
            for name in (
                "morphology.tsv",
                "syntax.tsv",
                "lexical-branches.jsonl",
                "primary-scaffold.md",
            ):
                (inputs / name).write_text("fixture\n", encoding="utf-8")

            paths = make_tasks.emit(run_root)
            self.assertEqual(4, len(paths))
            task = (run_root / "tasks" / "04-a2-publish.md").read_text(
                encoding="utf-8"
            )
            self.assertIn("a2-publication-tr-audio-first.md", task)
            self.assertIn("1-publication.jsonl", task)
            self.assertNotIn("1-publication.md", task)
            self.assertIn("render_publication.py", task)
            self.assertIn("--check", task)


class AudioPreparationTests(unittest.TestCase):
    def test_jsonl_becomes_one_section_per_record_without_spoken_grades(self) -> None:
        with tempfile.TemporaryDirectory(prefix="publication-audio-parse-test-") as temporary:
            source = Path(temporary) / "1-publication.jsonl"
            write_jsonl(source, valid_records())
            sections = AUDIO_PREPARER.parse_publication(source)
        self.assertEqual(3, len(sections))
        self.assertEqual(["GÜÇLÜ / A"], sections[1]["grades"])
        spoken = [
            paragraph["text"]
            for section in sections
            for paragraph in section["paragraphs"]
        ]
        self.assertFalse(any("GÜÇLÜ / A" in text for text in spoken))
        self.assertEqual("Kulluğun Açtığı Zemin", spoken[2])

    def test_s112_legacy_grouped_labels_all_survive(self) -> None:
        source = PACKAGE_ROOT / "run" / "s112-full-20260716" / "112-publication.md"
        sections = AUDIO_PREPARER.parse_markdown_publication(source)
        spoken = [
            paragraph["text"]
            for section in sections
            for paragraph in section["paragraphs"]
            if paragraph["kind"] == "paragraph"
        ]
        labels = []
        for match in re.finditer(
            r"\[([^\]\n]*\b(?:GÜÇLÜ|ORTA|ZAYIF)\b[^\]\n]*)\]",
            source.read_text(encoding="utf-8"),
        ):
            content = match.group(1)
            labels.append(
                content.split("—", 1)[1].strip() if "—" in content else content.strip()
            )
        missing = [
            title
            for title in labels
            if not any(text.startswith(f"{title}.") or text.startswith(f"{title} ") for text in spoken)
        ]
        self.assertEqual(26, len(labels))
        self.assertEqual([], missing)

    def test_s001_legacy_audio_contains_no_rank_residue(self) -> None:
        source = PACKAGE_ROOT / "run" / "s001-full-20260716" / "1-publication.md"
        sections = AUDIO_PREPARER.parse_markdown_publication(source)
        spoken = " ".join(
            paragraph["text"]
            for section in sections
            for paragraph in section["paragraphs"]
        )
        self.assertNotRegex(spoken, r"\b(?:GÜÇLÜ|ORTA|ZAYIF)\s*/")
        self.assertNotRegex(spoken, r"\b[ABC](?:-koşullu)? düzeyinde")

    def test_tts_prompt_is_conversational_not_teacher_led(self) -> None:
        prompt = AUDIO_PREPARER.PROMPT.casefold()
        self.assertIn("conversational", prompt)
        self.assertIn("one curious listener", prompt)
        self.assertNotIn("thoughtful teacher", prompt)

    def test_jsonl_audio_cli_preserves_section_grades_as_metadata(self) -> None:
        run_parent = PACKAGE_ROOT / "run"
        with tempfile.TemporaryDirectory(
            prefix="s001-jsonl-audio-test-", dir=run_parent
        ) as run_temporary, tempfile.TemporaryDirectory(
            prefix="jsonl-audio-output-"
        ) as output_temporary:
            source = Path(run_temporary) / "1-publication.jsonl"
            write_jsonl(source, valid_records())
            result = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "_audio" / "scripts" / "prepare_tts_chunks.py"),
                    str(source),
                    "--out-root",
                    output_temporary,
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            output = Path(output_temporary) / "S001"
            chunks = [
                json.loads(line)
                for line in (output / "chunks.jsonl").read_text(
                    encoding="utf-8"
                ).splitlines()
            ]
            manifest = json.loads(
                (output / "manifest.json").read_text(encoding="utf-8")
            )
        self.assertEqual(7, len(chunks))
        self.assertEqual(["GÜÇLÜ / A"], manifest["sections"][1]["grades"])
        self.assertFalse(any("GÜÇLÜ / A" in chunk["ttsText"] for chunk in chunks))
        self.assertTrue(manifest["source"].endswith("/1-publication.jsonl"))


class ScriptHealthTests(unittest.TestCase):
    def test_v3_and_audio_scripts_compile(self) -> None:
        scripts = sorted(SCRIPTS_ROOT.glob("*.py")) + sorted(
            (REPO_ROOT / "_audio" / "scripts").glob("*.py")
        )
        result = subprocess.run(
            [sys.executable, "-m", "py_compile", *map(str, scripts)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stderr)


if __name__ == "__main__":
    unittest.main()
