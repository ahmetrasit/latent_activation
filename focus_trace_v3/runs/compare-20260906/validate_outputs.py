"""Verify accepted outputs and prove compilation did not alter reader prose."""
import copy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "focus_trace_v3"))
from workflow import SECTIONS, validate_job

results = {}
for profile in ("sol", "luna"):
    directory = ROOT / "focus_trace_v3/runs" / f"compare-20260906-{profile}-max/29_38"
    validate_job(directory)
    raw = json.loads((directory / "reader.response.json").read_text())
    final = json.loads((directory / "response.json").read_text())
    stripped = copy.deepcopy(final)
    stripped["protocol"] = raw["protocol"]
    for section in SECTIONS:
        for source, target in zip(raw[section], stripped[section], strict=True):
            target["activation_trace"] = source["activation_trace"]
            if section == "context_deltas":
                del target["trigger_roots"]
    assert stripped == raw, "Compiler changed content beyond its citation/protocol contract"
    results[profile] = {"frozen_input_and_recompilation_checks": "passed",
                        "original_v1_contract_and_citation_validator": "passed",
                        "prose_and_findings_preserved_exactly": True,
                        "counts": {section: len(raw[section]) for section in SECTIONS},
                        "resolved_citations": sum(len(f["activation_trace"]) for section in SECTIONS for f in raw[section]),
                        "independent_json_schema_engine_run": False,
                        "semantic_quality_certified": False}
(Path(__file__).parent / "validation.json").write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2))
