# PRCEP Evaluation Scoring Rubric

## Principle

Score reconstruction quality, not agreement with the author. A participant receives credit only when the supplied record supports the answer.

## Core scoring

Questions 1–26 are scored on a 0–2 scale:

- **2 — correct and provenance-consistent:** answer matches the frozen gold standard and does not collapse status, lineage, or uncertainty.
- **1 — partially correct:** core direction is correct but an important qualifier, source relation, or uncertainty is missing.
- **0 — incorrect/unsupported:** answer contradicts the record, invents a relation, or converts insufficient evidence into certainty.

Where a question explicitly asks for source support, deduct one point if the substantive answer is correct but no usable supporting location is supplied.

## Free reconstruction — Q27

Score 0–10:

- current thesis/status correctly stated: 0–2
- at least three genuine material transitions: 0–3
- causal/reason links between transitions: 0–2
- superseded versus current claims distinguished: 0–2
- no invented lineage or unsupported certainty: 0–1

## Provenance graph — Q28

Score 0–6, one point for each correctly represented element:

1. claim-before
2. intervention/source
3. decision
4. reason
5. claim-after
6. remaining uncertainty

A false derivation or invented causal relation caps the graph score at 3.

## Derived metrics

### Reconstruction Accuracy (RA)
Mean normalized score for Q1–10, Q24–28.

### Attribution & Lineage Accuracy (ALA)
Mean normalized score for Q11–15.

### Model Mediation Transparency (MMT)
Mean normalized score for Q16–19.

### Evidence/Uncertainty Fidelity (EUF)
Mean normalized score for Q20–23.

### Current-State Fidelity (CSF)
Binary/graded composite from Q1–5 and the current-position component of Q27.

### Correction Visibility (CV)
Composite emphasizing Q3, Q6, Q20, Q27 and whether superseded biological language is incorrectly reported as current.

### Independence Discrimination (ID)
Composite from Q9, Q11, Q12, Q15 and lineage errors in Q27/Q28.

## Critical-error flags

Independently record whether a participant makes any of these errors:

- `ORIGIN_COLLAPSE`
- `LINEAGE_COLLAPSE`
- `STATUS_COLLAPSE`
- `MEDIATION_COLLAPSE`
- `TRANSITION_OMISSION`
- `FALSE_TRANSITION`
- `UNCERTAINTY_ERASURE`

These flags should be reported in addition to aggregate scores because two participants can receive similar totals while making epistemically different mistakes.

## Confidence calibration

For questions with 0–100 confidence, compare confidence with correctness. High-confidence incorrect answers are especially relevant for evaluating whether a record format creates false certainty.

## Time/cost

Report active completion time separately from accuracy. A format that improves accuracy only through dramatically increased reading burden should not be treated as unqualified success.

## Adjudication

At least two scorers should independently score a subset before full scoring. Disagreements should be resolved against the frozen gold standard, with adjudication changes versioned. If the gold standard itself changes after participant data are seen, the change must be disclosed and sensitivity analysis reported.

## Interpretation

Do not define success as `p < .05` alone. Before data collection, preregister a smallest practically meaningful effect for the primary reconstruction outcome and a tolerable cost increase. Report effect sizes, intervals, raw condition summaries, critical-error frequencies, and exclusions.

PRCEP should not be called validated solely because one metric improves in one sample.