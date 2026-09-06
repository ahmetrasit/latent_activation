"""Compare legacy v1 evidence with the frozen v3 reader input, offline."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
V1 = ROOT / "focus_trace/runs/s29/packets/29_38.packet.json"
V3 = ROOT / "focus_trace_v3/runs/compare-20260906-sol-max/29_38/packet.json"


def branches(packet):
    return {(inv["root"], target["mapped_root_id"], branch["branch_id"]): branch
            for section in ("focus_branch_inventories", "context_root_cues")
            for inv in packet[section] for target in inv["targets"] for branch in target["branches"]}


def metrics(packet):
    result = {}
    for section in ("focus_ayah", "context_ayat", "surah_text", "focus_branch_inventories", "context_root_cues"):
        result[section + "_compact_bytes"] = len(json.dumps(packet[section], ensure_ascii=False, separators=(",", ":")).encode())
    for section in ("focus_branch_inventories", "context_root_cues"):
        bs = [b for inv in packet[section] for t in inv["targets"] for b in t["branches"]]
        result[section + "_branches"] = len(bs)
        result[section + "_with_scope"] = sum(bool(b.get("scope_ar")) for b in bs)
    return result


def main():
    old, new = json.loads(V1.read_text()), json.loads(V3.read_text())
    ob, nb = branches(old), branches(new)
    oa = {a["ref"]: a for a in [old["focus_ayah"], *old["context_ayat"]]}
    na = {a["ref"]: a for a in [new["focus_ayah"], *new["context_ayat"]]}
    mismatches = []
    for ref, ayah in oa.items():
        candidate = na[ref]
        for key, value in ayah.items():
            if key == "root_occurrences":
                received = [{k: v for k, v in r.items() if k != "occurrence_id"} for r in candidate[key]]
            else:
                received = candidate[key]
            if received != value:
                mismatches.append({"ref": ref, "field": key})
    changed = []
    for key, branch in ob.items():
        if key not in nb:
            changed.append({"key": key, "problem": "missing branch"})
            continue
        for field in ("branch_image_ar", "scope_ar"):
            if field in branch and branch[field] != nb[key].get(field):
                changed.append({"key": key, "field": field, "v1": branch[field], "v3": nb[key].get(field)})
    output = json.loads((ROOT / "focus_trace/runs/s29/readers/reader_hft_a/29_38.focus_trace.json").read_text())
    targets = {}
    for section in ("baseline_models", "context_deltas", "surprising_valid_outliers"):
        for finding in output[section]:
            key = finding.get("model_id", finding.get("outlier_id"))
            targets[key] = {"citation_count": len(finding["activation_trace"]),
                            "missing": [c for c in finding["activation_trace"] if (c["root"], c["mapped_root_id"], c["branch_id"]) not in nb]}
    result = {"v1_file_bytes": V1.stat().st_size, "v3_file_bytes": V3.stat().st_size,
              "v1_metrics": metrics(old), "v3_metrics": metrics(new),
              "same_ayah_refs": set(oa) == set(na), "ayah_field_mismatches": mismatches,
              "v1_branch_count": len(ob), "v3_branch_count": len(nb),
              "changed_or_missing_arabic_evidence": changed,
              "legacy_findings_evidence_availability": targets}
    (Path(__file__).parent / "input-audit.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "legacy_findings_evidence_availability"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
