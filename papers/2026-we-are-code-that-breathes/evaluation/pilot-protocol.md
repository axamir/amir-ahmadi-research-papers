# PRCEP Pilot Protocol v0.1

**Study family:** PRCEP-EVAL-01  
**Stage:** instrument/stimulus pilot — not protocol validation  
**Target:** prepare a defensible confirmatory preregistration without using confirmatory outcomes to tune the design.

## Pilot objectives

The pilot answers design questions, not the substantive question “does PRCEP work?” Its purposes are to:

1. detect missing or non-equivalent information across P, C1 and C2;
2. estimate completion-time and score dispersion for planning;
3. test whether participants understand the instrument without investigator coaching;
4. test whether the scoring rubric produces reproducible judgments;
5. detect ceiling/floor effects and questions that do not discriminate record comprehension;
6. identify whether condition identity is obvious enough to bias participants;
7. estimate cognitive-load and usability burden;
8. identify accidental semantic leakage in C2 or accidental information loss in C1/C2.

## Pilot sample

Use a small heterogeneous convenience sample sufficient for design debugging rather than hypothesis testing. Record, but do not use post hoc to exclude, participants' familiarity with:

- research methods;
- AI/LLM systems;
- software/version control;
- provenance/data lineage;
- academic English.

Do not advertise the pilot as testing whether PRCEP is superior. Describe it as testing alternative research-record formats.

## Assignment

Randomly assign each participant to one packet only. Use neutral packet labels generated outside the participant-facing materials. Do not expose filenames `condition-p`, `condition-c`, or `condition-c2`.

## Procedure

1. provide study information/consent appropriate to context;
2. collect minimal background variables;
3. assign a neutral packet;
4. record start time;
5. participant reads packet without outside sources;
6. participant answers the full evaluation instrument;
7. record end time and interruptions;
8. collect usability/cognitive-load responses;
9. ask a short post-task diagnostic: “Was any part of the packet confusing, repetitive, missing, or unusually easy to infer from formatting?”;
10. score blinded responses using GS-0.1 and the scoring rubric;
11. compare independent scorer agreement on a prespecified subset;
12. inspect design diagnostics before freezing the confirmatory protocol.

## Pilot diagnostics

### Stimulus diagnostics

Flag for revision if:

- a required substantive concept is absent from any condition;
- one condition contains a unique factual answer to an evaluation question that another condition lacks;
- C2 reproduces explicit transition semantics closely enough that P vs C2 no longer isolates the intended factor;
- P contains repeated answer cues not needed to express provenance semantics;
- word-count/readability differences are large enough to plausibly dominate performance;
- participants reliably identify the hypothesized “better” condition from framing rather than content.

### Instrument diagnostics

Flag an item if it has one or more of:

- near-universal correctness with no useful diagnostic role;
- near-universal failure caused by wording ambiguity rather than record comprehension;
- scorer disagreement caused by an underspecified gold standard;
- answer dependence on outside knowledge;
- materially different interpretation across otherwise competent readers.

Do not remove difficult items merely because they reduce the expected PRCEP advantage.

### Scoring diagnostics

Before full pilot scoring, two scorers should independently score the same subset. Record raw agreement and disagreements by error type. Revise the rubric only where disagreement reveals genuine ambiguity. Preserve the pre-revision rubric and document every change.

## What pilot data may determine

Pilot data may be used to set, before confirmatory recruitment:

- SPME for Reconstruction Accuracy;
- maximum tolerable completion-time/cognitive-load increase;
- confirmatory sample-size rationale;
- exact statistical model appropriate to observed score behavior;
- objective exclusion rules;
- final item wording where ambiguity is demonstrated;
- final stimulus balancing where information parity is demonstrably imperfect.

## What pilot data must not determine

Do not choose confirmatory hypotheses, outcomes, scoring weights, exclusions, or stimulus edits merely because they maximize an observed P advantage. Any design change should be justified by measurement quality, parity, interpretability, ethics, or burden.

## Freeze procedure after pilot

Before confirmatory recruitment:

1. freeze final P/C1/C2 stimuli and record hashes;
2. freeze final instrument;
3. freeze gold standard and scoring rubric;
4. freeze numerical SPME and cost threshold;
5. freeze sample size and analysis model;
6. freeze exclusions;
7. archive pilot deviations and all stimulus/instrument changes;
8. mark `preregistration.md` as final with a version identifier;
9. do not edit confirmatory materials after participant data collection begins except through a documented deviation process.

## Interpretation boundary

Pilot outcomes are design evidence only. Even a large apparent P advantage in the pilot must not be reported as PRCEP validation. Conversely, an apparent null pilot should not be hidden; it may indicate the protocol is unnecessary, the manipulation is weak, the instrument is insensitive, or the hypothesized effect is absent.

**Pilot protocol version:** PP-0.1