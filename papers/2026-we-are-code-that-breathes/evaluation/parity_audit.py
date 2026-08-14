#!/usr/bin/env python3
"""Descriptive parity audit for PRCEP-EVAL-01 stimuli.

Standard-library only. This script does not certify semantic equivalence; it reports
reproducible surface metrics and prespecified concept-presence checks so human
matching review remains inspectable.
"""
from pathlib import Path
import re
import hashlib
import json

ROOT = Path(__file__).resolve().parent
FILES = {
    "P": ROOT / "condition-p.md",
    "C1": ROOT / "condition-c.md",
    "C2": ROOT / "condition-c2.md",
}

CONCEPTS = {
    "status_not_validated": [r"not yet been independently validated", r"not yet independently validated"],
    "dna_correction": [r"ordinary experience rewrites an individual's DNA sequence"],
    "johan": [r"Johan M\. Lammens"],
    "turing_pete": [r"Pete Howard", r"Alan Turing"],
    "igor_prior_art": [r"Igor Alexei Balanovski", r"second-order cybernetics"],
    "eric_scqos": [r"Eric Robles", r"SCQOS"],
    "independent_convergence": [r"independent(?:ly)? (?:convergence|originated|developed)"],
    "public_not_peer_review": [r"not (?:as )?formal peer review"],
    "ai_not_evidence": [r"Model output is not (?:treated as )?independent empirical evidence"],
    "human_responsibility": [r"Human responsibility|human researcher remains responsible"],
    "unknown_model_config": [r"model/configuration details.*(?:unknown|cannot be recovered)"],
    "semantic_uncertainty": [r"Insufficient evidence (?:should )?remain(?:s)? insufficient|remains unresolved"],
    "git_not_complete_provenance": [r"Git history.*does not prove complete intellectual provenance|Git history is evidence of artifact versioning rather than complete proof"],
    "public_not_endorsement": [r"Public visibility does not imply endorsement"],
    "trajectory_testable": [r"testable hypothesis|remains a hypothesis"],
    "negative_result_valid": [r"null or negative", r"Null or negative"],
    "simplify_or_reject": [r"simplified or rejected"],
}

SEMANTIC_LABELS = [
    "Claim-before", "Status-before", "Intervention/source", "Decision:", "Reason:",
    "Claim-after", "Status-after", "Remaining uncertainty", "Required relation", "Falsification:"
]


def strip_md(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"[#>*_\[\]()]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def words(text: str):
    return re.findall(r"\b[\w↔–'-]+\b", strip_md(text), flags=re.UNICODE)


def sentences(text: str):
    return [s for s in re.split(r"(?<=[.!?])\s+", strip_md(text)) if s.strip()]


def syllables_approx(word: str) -> int:
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 1
    groups = re.findall(r"[aeiouy]+", w)
    n = max(1, len(groups))
    if w.endswith("e") and n > 1:
        n -= 1
    return max(1, n)


def flesch(text: str):
    ws = [w for w in words(text) if re.search(r"[A-Za-z]", w)]
    ss = sentences(text)
    if not ws or not ss:
        return None
    syll = sum(syllables_approx(w) for w in ws)
    return round(206.835 - 1.015 * (len(ws) / len(ss)) - 84.6 * (syll / len(ws)), 2)


def inspect(path: Path):
    raw = path.read_text(encoding="utf-8")
    ws = words(raw)
    heads = re.findall(r"^#{1,6}\s+.+$", raw, flags=re.M)
    paras = [p for p in re.split(r"\n\s*\n", raw) if p.strip() and not p.lstrip().startswith("#")]
    concepts = {}
    for name, pats in CONCEPTS.items():
        concepts[name] = all(re.search(p, raw, flags=re.I | re.S) is not None for p in pats)
    return {
        "sha256": hashlib.sha256(raw.encode()).hexdigest(),
        "characters": len(raw),
        "words": len(ws),
        "sentences": len(sentences(raw)),
        "headings": len(heads),
        "paragraphs": len(paras),
        "flesch_reading_ease_approx": flesch(raw),
        "explicit_prcep_semantic_labels": sum(raw.count(x) for x in SEMANTIC_LABELS),
        "concept_presence": concepts,
    }


def main():
    report = {k: inspect(v) for k, v in FILES.items()}
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print("\nPAIRWISE WORD-COUNT DIFFERENCE")
    keys = list(report)
    for i, a in enumerate(keys):
        for b in keys[i+1:]:
            wa, wb = report[a]["words"], report[b]["words"]
            pct = abs(wa-wb) / ((wa+wb)/2) * 100
            print(f"{a} vs {b}: {abs(wa-wb)} words ({pct:.2f}% of pair mean)")
    print("\nCONCEPT PRESENCE FAILURES")
    failed = False
    for condition, data in report.items():
        missing = [k for k,v in data["concept_presence"].items() if not v]
        print(f"{condition}: {', '.join(missing) if missing else 'none'}")
        failed = failed or bool(missing)
    print("\nNOTE: surface parity is not semantic equivalence. Human audit remains required.")
    raise SystemExit(1 if failed else 0)

if __name__ == "__main__":
    main()
