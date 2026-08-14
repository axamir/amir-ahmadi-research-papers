# PRCEP Independent Evaluation Package

**Paper:** ARP-WCB-2026-01 — *We Are Code That Breathes*  
**Protocol:** PRCEP v0.1  
**Purpose:** independent evaluation, not demonstration

## Objective

Test whether explicit provenance-preserving claim-transition structure improves reconstruction of a research trajectory beyond an information-matched control.

The primary comparison is:

- **Condition P — Provenance-rich:** substantive research content plus explicit claim-transition structure.
- **Condition C — Matched-information control:** equivalent substantive information and source content, but without explicit transition labels, lineage relations, decision states, correction links, or model-mediation structure.

The evaluation must not assume that PRCEP works. A null or negative result is valid.

## Primary hypotheses

**H1 — Reconstruction:** Condition P yields higher claim-transition reconstruction accuracy than Condition C.

**H2 — Attribution:** Condition P yields higher accuracy in distinguishing origin, influence, quotation, adoption, rejection, and independent convergence.

**H3 — Correction visibility:** Condition P reduces the probability that a superseded claim is mistaken for the current research position.

**H4 — Mediation transparency:** Condition P improves identification of where generative-model mediation occurred without increasing false attribution of model output as independent evidence.

**H5 — Cost:** Any accuracy benefit must be interpreted against reading time, annotation burden, maintenance cost, and perceived complexity.

## Null hypotheses

For H1–H4, the corresponding null is that Condition P provides no meaningful improvement over the matched-information control. PRCEP should be simplified or rejected if gains are negligible, unstable, or too costly.

## Recommended design

Use a randomized between-subject design for the primary test to avoid participants learning the transition structure from one condition and carrying it into the other. A preregistered within-subject replication may follow using a different research case and counterbalanced order.

Participants should not be told that the study was designed to validate PRCEP. They should be told that the study compares two research-record formats.

## Materials to prepare

1. `condition-p.md` — provenance-rich packet derived from the frozen case record.
2. `condition-c.md` — matched-information packet containing the same substantive facts and source excerpts but stripped of PRCEP transition structure.
3. `questions.md` — reconstruction and attribution instrument.
4. `gold-standard.md` — adjudicated answer key built before participant scoring.
5. `scoring-rubric.md` — scoring and error taxonomy.
6. `report-template.md` — standardized result reporting.

The two conditions must be matched as closely as practical for substantive information, source availability, approximate length, and reading difficulty. Condition C must not be made artificially confusing.

## Primary outcomes

- claim-transition reconstruction accuracy
- origin-attribution accuracy
- current-state fidelity
- correction visibility
- independence-discrimination accuracy
- model-mediation transparency
- evidence-link completeness

## Cost outcomes

- task completion time
- self-reported cognitive load
- perceived record complexity
- evaluator confidence/calibration
- annotation/maintenance time for record creators
- storage/representation overhead

## Error taxonomy

At minimum distinguish:

- **origin collapse:** assigning a claim to the wrong source;
- **lineage collapse:** treating independent convergence as derivation;
- **status collapse:** treating challenged/rejected/superseded material as current;
- **mediation collapse:** treating model-assisted wording as independent evidence or original external source;
- **transition omission:** identifying endpoints but missing why the change occurred;
- **false transition:** inventing a causal or intellectual relation not supported by the record;
- **uncertainty erasure:** converting unresolved evidence into a definite interpretation.

## Analysis principles

Report effect sizes and uncertainty, not only significance tests. Predefine the smallest practically meaningful improvement before data collection. Analyze accuracy and cost jointly. Report exclusions, missing data, disagreements in gold-standard adjudication, and any deviations from the preregistered plan.

Do not claim validation from a single small convenience sample. A positive first study should be described as initial evidence and replicated on at least one research trajectory not authored by the present project.

## Independence safeguards

The strongest evaluation should include:

- at least one evaluator who did not participate in constructing PRCEP;
- blinded condition labels during scoring where practical;
- a frozen gold standard before outcome analysis;
- disclosure of any relationship between evaluators and the author;
- publication of negative and null outcomes;
- preservation of the exact evaluated materials and analysis version.

## Success criterion

PRCEP advances beyond case demonstration only if the provenance-rich condition shows a practically meaningful and reproducible improvement in reconstruction/attribution outcomes that is not explained merely by additional information and is defensible relative to its cost.

## Failure criterion

If information-matched controls perform similarly, if benefits disappear on an independent case, or if maintenance/readability costs dominate the gains, the protocol should be narrowed, simplified, or rejected.

---

**Status:** evaluation protocol scaffold. No participant results exist yet.