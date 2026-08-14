# PRCEP Evaluation Preregistration Draft v0.1

**Study family:** PRCEP-EVAL-01  
**Target protocol:** PRCEP v0.1  
**Case:** ARP-WCB-2026-01  
**Status:** draft to be frozen before participant recruitment/data collection

## 1. Research question

Does explicit provenance-preserving claim-transition semantics improve a reader's ability to reconstruct the evolution, attribution, status, and uncertainty of research claims when substantive information is held approximately constant?

## 2. Conditions

Participants are randomly assigned to one of three between-subject conditions:

- **P — provenance-semantic:** matched substantive information plus explicit PRCEP transition fields such as claim-before, intervention/source, decision/reason, claim-after, status and remaining uncertainty.
- **C1 — prose control:** matched substantive information presented as conventional continuous research prose.
- **C2 — structured control:** matched substantive information presented with comparable topic segmentation/headings but without explicit PRCEP transition semantics.

C2 is the critical control for separating semantic-transition effects from generic chunking/formatting effects.

## 3. Primary contrast

**P vs C2** is the primary confirmatory contrast.

**P vs C1** is secondary and estimates the effect of the broader provenance-rich presentation package relative to conventional prose.

**C2 vs C1** estimates generic structuring/chunking benefit.

## 4. Primary outcome

**Reconstruction Accuracy (RA)** as defined in `scoring-rubric.md`.

## 5. Secondary outcomes

- Attribution & Lineage Accuracy (ALA)
- Current-State Fidelity (CSF)
- Correction Visibility (CV)
- Independence Discrimination (ID)
- Model Mediation Transparency (MMT)
- Evidence/Uncertainty Fidelity (EUF)
- critical-error frequencies
- confidence calibration
- active task time
- cognitive load / perceived complexity

## 6. Directional hypotheses

H1: RA(P) > RA(C2).  
H2: ALA(P) > ALA(C2).  
H3: CV(P) > CV(C2).  
H4: ID(P) > ID(C2).  
H5: P reduces high-confidence lineage/status/uncertainty errors relative to C2.

P vs C1 and C2 vs C1 are secondary contrasts and should not substitute for the primary P vs C2 test.

## 7. Smallest practically meaningful effect

Before recruitment, investigators must freeze a numerical smallest practically meaningful effect (SPME) for RA and a maximum tolerable cost increase for completion time/cognitive load. These values are intentionally not invented in this draft. They should be justified from pilot dispersion, measurement reliability, or an explicit decision-theoretic rationale rather than chosen after seeing confirmatory outcomes.

## 8. Participants

The first pilot may use a convenience sample to test comprehension, timing, scoring reliability and stimulus parity. Pilot data must not be represented as independent protocol validation.

A confirmatory study should recruit participants capable of reading research-oriented English and should record relevant experience with research methods, AI systems, software/version control and provenance concepts. Expertise variables may be used for preregistered exploratory moderation but not post-hoc exclusion unless specified before analysis.

## 9. Randomization and blinding

Use randomized between-subject allocation. Participants should see neutral packet identifiers rather than `P`, `C1`, `C2`, `PRCEP-rich`, or `control` labels.

Where practical, scorers should receive participant responses without condition labels. The gold standard must be frozen before outcome analysis.

## 10. Procedure

1. consent/eligibility as required by the study context;
2. collect minimal preregistered background variables;
3. randomly assign one packet;
4. record task start time;
5. participant reads only assigned packet;
6. participant completes `questions.md` without outside sources;
7. record end time, interruptions and usability/cognitive-load items;
8. score against frozen `gold-standard.md` using `scoring-rubric.md`;
9. analyze according to the frozen plan.

## 11. Exclusions

Before confirmatory recruitment, define objective exclusion rules such as duplicate participation, failure to access/read the assigned packet, substantial use of prohibited outside sources, or unusable/incomplete response data. Do not exclude participants because their answers weaken the hypothesis.

## 12. Analysis

Report condition means/distributions, effect sizes and uncertainty intervals for all preregistered outcomes. The primary inferential analysis targets P vs C2 on RA. The exact statistical model must be frozen before confirmatory data collection after pilot inspection of scale behavior, without using confirmatory outcomes.

Report critical-error rates separately even when aggregate scores are similar. Analyze completion time and cognitive load jointly with accuracy.

Correct or hierarchically account for multiplicity across secondary confirmatory outcomes; do not turn exploratory findings into preregistered hypotheses retrospectively.

## 13. Cost-benefit interpretation

A higher accuracy score is not sufficient by itself. Interpretation must consider whether the gain is practically meaningful relative to additional reading time, cognitive load, annotation burden, maintenance complexity, storage/representation overhead and privacy/redaction burden.

## 14. Failure and revision rules

Evidence against PRCEP includes any of the following:

- negligible P–C2 reconstruction difference;
- benefit explained mainly by C2–C1 chunking effects;
- failure to replicate on a trajectory independent of the construction case;
- increased high-confidence false lineage/status interpretations;
- costs that dominate practical accuracy gains.

Such outcomes should trigger narrowing, simplification or rejection rather than post-hoc redefinition of success.

## 15. Open-science record

Preserve and version:

- exact stimuli;
- instrument;
- frozen gold standard;
- scoring rubric;
- preregistration;
- analysis code, if used;
- anonymized/de-identified results where ethically and legally appropriate;
- deviations and adjudication changes;
- null and negative results.

## 16. Replication boundary

Even a successful confirmatory test on ARP-WCB-2026-01 is not sufficient for broad validation. At least one replication should use a research trajectory not authored or constructed by the present project team.

---

**Freeze gate:** do not mark this preregistration final until stimulus parity metrics, pilot procedure, SPME, cost threshold, sample-size rationale, exact statistical model, and exclusion rules are numerically specified.