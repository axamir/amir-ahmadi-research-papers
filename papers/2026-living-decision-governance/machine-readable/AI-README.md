# AI Review Guide — Living Decision Governance v0.1

This directory is intended to make the research artifact easier for AI systems and human reviewers to inspect, challenge, and reproduce.

## Do not assume the framework is correct

Treat the paper as a working hypothesis. Separate:

- conceptual claims,
- implementation choices,
- empirical claims,
- normative assumptions,
- and unresolved design questions.

## Minimum review sequence

1. Read `paper.en.md`.
2. Read `specification.md`.
3. Inspect `verification-protocol.json`.
4. Inspect `src/ldg.py` and `tests/test_ldg.py`.
5. Identify any mismatch between the prose and executable state transitions.
6. Try counterexamples.
7. Report which propositions are unsupported, underspecified, or falsified.

## Required adversarial checks

- Can a high business score hide stakeholder harm?
- Can a noisy stakeholder signal wrongly restrict a good decision?
- Can reputation penalties create risk aversion or metric gaming?
- Can a majority suppress a correct minority view?
- Can repeated review create paralysis?
- Can decision-makers evade accountability through collective signatures?
- Can a malicious actor manipulate thresholds or stakeholder inputs?
- Does the model confuse decision quality with implementation quality?

## Output format for machine review

Return:

```json
{
  "artifact": "Living Decision Governance",
  "version": "0.1.0",
  "overall_assessment": "pass|partial|fail",
  "confirmed_claims": [],
  "unsupported_claims": [],
  "contradictions": [],
  "counterexamples": [],
  "security_or_governance_risks": [],
  "recommended_changes": []
}
```

## Provenance note

The inquiry was triggered by a public observation from Christopher J. Skinner about enterprise AI's difficulty representing human thinking, communication, decision quality, and leadership. The initiating observation should be credited as the research trigger; the LDG synthesis, lifecycle model, propositions, and executable reference model are the author's working contribution.
