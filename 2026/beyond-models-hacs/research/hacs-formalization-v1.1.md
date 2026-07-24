# HACS Formalization for v1.1.0

## Constructs, Relationships, Boundaries, and Testable Propositions

**Status:** Working research formalization  
**Framework:** Human–AI Collaborative Systems (HACS)  
**Author:** Amir Ahmadi  
**Development line:** v1.1.0-dev  
**Year:** 2026

---

## 1. Purpose

The purpose of this document is to move HACS from a broad conceptual framework toward a research model that can be criticized, operationalized, compared, and tested.

The goal is not to claim mathematical completeness or empirical validation. The goal is to define the framework's core constructs clearly enough that future studies can distinguish HACS from adjacent ideas and evaluate whether HACS-oriented systems improve the quality of human–AI collaboration.

HACS treats **collaboration quality over time** as the primary unit of analysis.

---

## 2. Unit of Analysis

The primary unit of analysis is not:

- the AI model alone,
- the human alone,
- a single prompt,
- a single task result,
- or a single interaction session.

The unit of analysis is the **Human–AI Collaborative System across time**.

A minimal HACS instance contains:

```text
Human participant(s)
        +
AI capability
        +
Context continuity mechanism
        +
Governance and role boundaries
        +
Feedback and correction processes
        +
A shared task or collaborative objective
```

The system is evaluated not only by whether a task is completed, but by whether the collaboration remains useful, accountable, recoverable, and aligned with human goals over repeated interactions.

---

## 3. Core Constructs

### 3.1 Human Agency Preservation (HAP)

**Definition:** The degree to which a collaborative system preserves the human participant's meaningful control, judgment, ability to challenge the AI, and responsibility for consequential decisions.

HAP is not equivalent to merely having a human "in the loop." A human may technically remain present while becoming behaviorally dependent on the system or unable to understand how a decision emerged.

**Observable indicators may include:**

- ability to reject AI recommendations;
- visibility of alternatives and uncertainty;
- preservation of independent judgment;
- absence of coercive or manipulative interaction patterns;
- clear assignment of final decision authority;
- ability to inspect, correct, or override prior assumptions.

**Research question:**

> Does the system increase human capability without progressively displacing human judgment?

---

### 3.2 AI Capability Contribution (ACC)

**Definition:** The useful contribution provided by AI to the collaborative process through analysis, reasoning support, retrieval, pattern recognition, synthesis, simulation, or generation.

ACC should be distinguished from raw model benchmark performance. A highly capable model may contribute poorly if its output is poorly calibrated to the task, context, domain, or human collaborator.

**Observable indicators may include:**

- relevance of AI contribution;
- reduction of cognitive or analytical burden;
- improvement in decision quality;
- support for exploration of alternatives;
- error detection;
- adaptation to the collaborative objective.

---

### 3.3 Context Continuity (CC)

**Definition:** The ability of the collaborative system to preserve not only prior information, but the significance, dependencies, decisions, constraints, provenance, and unresolved state needed for future collaboration.

Context Continuity differs from simple memory.

Memory asks:

> What information was retained?

Context Continuity asks:

> What prior information remains relevant, why does it matter, and how should it influence the next collaborative action?

**CC may include:**

- decision history;
- unresolved questions;
- prior corrections;
- goals and constraints;
- attribution of contributions;
- provenance of claims;
- changes in assumptions;
- role and responsibility boundaries;
- meaningful state across model or session transitions.

**Failure mode:** Context may be technically stored yet functionally discontinuous if the system cannot interpret why it matters.

---

### 3.4 Governance Integrity (GI)

**Definition:** The degree to which collaboration operates within explicit, understandable, and enforceable rules for authority, transparency, responsibility, privacy, correction, and escalation.

Governance is treated as part of the architecture, not as an external policy layer added after deployment.

**Observable indicators may include:**

- clarity of AI role;
- visibility of limitations;
- escalation rules;
- human override mechanisms;
- attribution and provenance;
- privacy and data-boundary controls;
- auditability;
- explicit handling of uncertainty and high-risk decisions.

---

### 3.5 Trust Calibration (TC)

**Definition:** The degree to which human reliance on the AI system corresponds to the system's actual competence, uncertainty, and limitations in the relevant context.

High trust is not automatically desirable. Appropriate trust is desirable.

Two major failure modes are:

- **over-trust:** reliance exceeds actual system capability;
- **under-trust:** useful system capability is ignored or discounted.

TC therefore concerns calibration rather than persuasion or user confidence alone.

---

### 3.6 Feedback and Mutual Adaptation (FMA)

**Definition:** The capacity of the collaborative process to improve through correction, critique, changed assumptions, domain input, and observable learning at the system level.

This does not require that the underlying foundation model permanently learns from an individual user. Adaptation may occur through memory systems, workflow state, updated rules, revised prompts, human learning, changed task strategies, or external tools.

**Observable indicators may include:**

- correction uptake;
- reduced repetition of known errors;
- adaptation to clarified goals;
- human learning from AI contribution;
- system response to domain expert feedback.

---

### 3.7 Recovery Capability (RC)

**Definition:** The ability of the collaborative system to detect, acknowledge, reconstruct, and recover from errors, context loss, contradictory states, interruption, or inappropriate reliance.

A durable collaborative system should be evaluated not only by how rarely it fails, but by how well it recovers when failure occurs.

**Recovery may require:**

1. detection;
2. acknowledgement;
3. localization of the failure;
4. reconstruction of valid state;
5. correction;
6. prevention or mitigation of recurrence.

---

### 3.8 Collaborative Goal Stability (CGS)

**Definition:** The degree to which the purpose, constraints, and values of the collaboration remain coherent over time while still allowing legitimate revision.

Goal stability is not rigidity. A system should preserve the distinction between:

- an intentional goal change;
- gradual drift;
- accidental context loss;
- AI-generated reinterpretation of the objective.

---

### 3.9 Behavioral Consistency / Artificial Character (BAC)

**Definition:** Designed consistency in the system's collaborative behavior, role, principles, and interaction norms across time.

This construct does **not** assert consciousness, emotion, or a human-like inner identity.

Its research relevance concerns predictability and role stability. A human collaborator should not have to rediscover the system's basic interaction principles at every session.

---

### 3.10 Collaborative Commitment (CCM)

**Definition:** The system-level capacity to preserve the purpose and boundaries of a collaboration, communicate limitations, accept correction, and support continuity across changing interactions.

Collaborative Commitment is a design property, not a claim of subjective intention.

---

## 4. Proposed Higher-Order Construct: Collaboration Quality

HACS proposes **Collaboration Quality (CQ)** as a higher-order construct that cannot be reduced to model performance alone.

Conceptually:

```text
CQ = f(
  Human Agency Preservation,
  AI Capability Contribution,
  Context Continuity,
  Governance Integrity,
  Trust Calibration,
  Feedback & Adaptation,
  Recovery Capability,
  Collaborative Goal Stability
)
```

This is a conceptual function, not yet a validated mathematical formula.

A key implication is that a system can have high AI capability and still have low collaboration quality.

Examples:

- excellent answers + destructive over-reliance;
- strong reasoning + lost context;
- high accuracy + unclear responsibility;
- persistent memory + poor provenance;
- high user satisfaction + badly calibrated trust.

---

## 5. Proposed Relationships Among Constructs

HACS currently proposes the following directional relationships as hypotheses rather than established facts.

### R1 — Context Continuity → Collaboration Quality

Better preservation of meaningful collaborative context should improve the coherence and efficiency of repeated human–AI interaction.

However, excessive or irrelevant persistence may increase noise, privacy risk, or anchoring.

Therefore the relevant variable is **meaningful continuity**, not maximal memory.

---

### R2 — Governance Integrity → Trust Calibration

Clear system boundaries, uncertainty communication, and accountability mechanisms should improve the human participant's ability to calibrate reliance appropriately.

---

### R3 — Human Agency Preservation → Sustainable Collaboration

Systems that preserve meaningful human control should be less likely to create pathological dependence and more likely to support durable collaboration.

---

### R4 — Feedback and Adaptation → Recovery Capability

Systems that incorporate correction effectively should recover more successfully from error and interruption.

---

### R5 — Context Continuity × Governance Integrity

Context continuity without governance may increase risk because persistent information can amplify inappropriate assumptions or authority.

Governance without continuity may reduce collaboration to repeated isolated interactions.

The value of either construct may therefore depend partly on the other.

---

### R6 — AI Capability Contribution × Trust Calibration

Higher AI capability should improve collaborative outcomes only when human reliance is reasonably calibrated to the system's actual strengths and limitations.

---

### R7 — Recovery Capability → Longitudinal Trust

Effective recovery from visible errors may produce healthier long-term trust than systems that attempt to appear infallible.

---

### R8 — Behavioral Consistency → Lower Coordination Cost

Stable interaction principles and role behavior may reduce the cognitive burden required to re-establish collaboration across sessions.

---

## 6. Initial Testable Propositions

The following propositions are intended as candidates for empirical testing.

### P1 — Continuity Proposition

Participants using an AI system with meaningful context continuity will complete repeated related tasks with less contextual reconstruction effort than participants using an otherwise comparable stateless AI assistant.

### P2 — Agency Proposition

HACS-oriented interfaces that explicitly preserve override, challenge, and decision authority will produce higher human agency measures than AI workflows optimized primarily for recommendation acceptance.

### P3 — Recovery Proposition

A system with explicit state reconstruction and correction mechanisms will recover from induced context errors more effectively than a conventional conversational assistant without such mechanisms.

### P4 — Trust Calibration Proposition

Transparent uncertainty and role-boundary mechanisms will reduce both over-reliance and under-reliance relative to systems that present recommendations without calibrated confidence or limitations.

### P5 — Collaboration Quality Proposition

For longitudinal tasks, collaboration-quality measures will explain important outcome variance not captured by model capability measures alone.

### P6 — Governance–Continuity Interaction Proposition

The benefits of persistent context will be greater when provenance and correction controls are present than when persistence operates without those controls.

### P7 — Human Learning Proposition

In well-designed HACS workflows, repeated collaboration should improve not only task outputs but also the human participant's understanding, decision process, or capability.

---

## 7. Candidate Operational Measures

The v1.0.0 release named five preliminary metrics. This formalization clarifies their intended direction.

### Context Continuity Score (CCS)

Potential components:

- correct preservation of prior constraints;
- correct use of prior decisions;
- unresolved-state preservation;
- provenance retention;
- context relevance precision;
- successful continuity after interruption.

### Trust Calibration Index (TCI)

Potential components:

- difference between perceived and measured system competence;
- appropriate acceptance/rejection of recommendations;
- reliance under uncertainty;
- sensitivity to disclosed limitations.

### Human Agency Preservation Score (HAPS)

Potential components:

- override frequency and accessibility;
- independent reasoning retention;
- decision ownership clarity;
- challenge behavior;
- user ability to explain the basis of final decisions.

### Alignment Stability Score (ASS)

For clarity, this metric should be interpreted in HACS as **collaborative goal stability**, not broad foundation-model alignment.

Potential components:

- persistence of explicit objectives;
- constraint preservation;
- detection of goal drift;
- distinction between authorized and unauthorized goal changes.

### Recovery Capability Score (RCS)

Potential components:

- error-detection rate;
- time to recovery;
- state reconstruction accuracy;
- correction completeness;
- recurrence rate after correction.

---

## 8. Boundary Conditions

HACS should not be treated as universally beneficial.

The framework may be less useful when:

- the task is trivial and one-shot;
- no meaningful continuity is required;
- collaboration cost exceeds task value;
- persistence introduces unacceptable privacy risk;
- AI involvement adds no useful capability;
- human responsibility cannot be meaningfully preserved;
- the domain requires controls beyond the proposed HACS layer.

HACS therefore predicts the greatest value in **repeated, consequential, context-dependent collaborative work**.

---

## 9. Failure Modes

A mature HACS theory must describe not only successful collaboration but characteristic failure.

### Continuity Failure

Prior state exists but is missing, irrelevant, distorted, or incorrectly applied.

### Agency Failure

The human technically remains involved but meaningful control has shifted to the AI system.

### Calibration Failure

Human trust does not correspond to actual capability.

### Governance Failure

Authority, accountability, data boundaries, or correction rights are unclear.

### Goal Drift

The collaboration gradually moves away from the intended objective without explicit authorization.

### Recovery Failure

The system cannot reconstruct valid collaborative state after error or interruption.

### Anthropomorphic Misattribution

Designed behavioral consistency is interpreted as evidence of consciousness, emotion, or subjective commitment without support.

### Persistence Harm

Long-term memory or continuity preserves outdated, sensitive, biased, or incorrect assumptions and amplifies them over time.

---

## 10. Minimal HACS Design Requirements

A system should not be labeled HACS merely because a human interacts repeatedly with an AI model.

For research purposes, a candidate HACS implementation should demonstrate at least:

1. **explicit human role and authority;**
2. **meaningful AI contribution;**
3. **mechanism for preserving relevant collaborative context;**
4. **governance or boundary mechanisms;**
5. **feedback and correction pathway;**
6. **recovery mechanism;**
7. **evaluation at the collaboration level rather than only the model level.**

This minimum definition is intentionally stricter than "human uses AI."

---

## 11. HACS Research Model

The current research model can be summarized as:

```text
                 Human Expertise
                        │
                        ▼
                 Human Agency
                        │
                        │
AI Capability ───► Collaborative Process ◄─── Context Continuity
                        │
                        │
              Governance Integrity
                        │
                        ▼
             Trust Calibration
                        │
                        ▼
          Feedback / Adaptation / Recovery
                        │
                        ▼
               Collaboration Quality
                        │
                        ▼
        Longitudinal Human–AI Outcomes
```

The arrows indicate proposed relationships for research, not established causal effects.

---

## 12. What Would Falsify or Weaken HACS?

A useful framework must permit failure.

HACS would be weakened if rigorous comparative studies repeatedly showed that:

- collaboration-level constructs add no explanatory value beyond model capability and ordinary usability measures;
- context continuity does not improve longitudinal work under conditions where continuity should matter;
- governance and agency mechanisms do not improve calibration or decision quality;
- recovery architecture does not improve resilience after induced failure;
- the proposed constructs cannot be measured reliably or distinguished from existing constructs;
- or HACS terminology adds complexity without improving prediction, design, or evaluation.

The framework should therefore remain open to revision, collapse of redundant constructs, or rejection of unsupported propositions.

---

## 13. v1.1.0 Research Contribution

If retained after literature review and critique, the formal contribution of v1.1.0 will not be the claim that concepts such as trust, teaming, memory, or human agency are new.

The proposed contribution is narrower:

> HACS organizes enduring human–AI collaboration as a longitudinal socio-technical research object in which context continuity, human agency, governance, trust calibration, adaptation, and recovery are treated as interacting properties of the collaborative system rather than isolated properties of the model or interface.

This claim remains provisional until stronger literature comparison and empirical work are completed.

---

## 14. Next Validation Step

The next step is to construct at least one case study with two descriptions:

1. a conventional AI-assisted workflow;
2. a HACS-oriented version of the same workflow.

The case study should identify which constructs are present, which are absent, what failure modes are possible, and which measurable differences could be tested.

That case study will provide the first bridge from framework formalization to empirical design.
