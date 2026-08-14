# Formal Model v0.1 — Provenance-Preserving Relational Transition Model

**Document:** ARP-WCB-2026-01  
**Model ID:** PRTM-0.1  
**Status:** conceptual formalization, not an empirical law

## 1. Objective

Represent persistent Human↔AI interaction without assuming that the human and model become one agent, that the model is conscious, or that causal coupling automatically constitutes cognition.

The model tracks how a research state changes through interaction while preserving provenance, correction, uncertainty, and responsibility.

## 2. Entities

Let:

- **H_t** = human state relevant to the inquiry at time *t*: question framing, remembered context, commitments, interpretations, uncertainty.
- **A_t** = AI-accessible interaction state at time *t*: current prompt/context, model output conditions, available retrieved material, explicit instructions. This is not a claim about private subjective state.
- **R_t** = relational record at time *t*: the traceable interaction history linking H and A for the research task.
- **E_t** = external evidence available at time *t*: literature, public comments, repository artifacts, measurements, source documents.
- **G_t** = governance constraints: attribution rules, consent boundaries, claim classes, authorship responsibility, publication rules.
- **U_t** = uncertainty vector attached to propositions.
- **P_t** = provenance graph: who/what introduced, transformed, corrected, supported, or rejected each proposition.
- **K_t** = current research state: the set of propositions and their statuses, not a claim of total knowledge.

Define the observable research configuration:

**S_t = ⟨H_t, A_t, R_t, E_t, G_t, U_t, P_t, K_t⟩**

## 3. Transition

A research interaction produces a candidate transition:

**T_t : S_t × I_t → S_(t+1)**

where **I_t** may be a human question, AI response, public criticism, new source, correction, experiment, or governance decision.

A transition is admissible for the research record only if it satisfies minimum constraints:

**Admissible(T_t) = Traceable ∧ Attributable ∧ Boundary-consistent ∧ Uncertainty-updated**

For claims presented as evidence-based, add:

**Evidence-linked(T_t)**

For externally consequential actions, additional authorization/governance constraints may be required.

## 4. Proposition state machine

Each proposition **q** moves among explicit states:

```text
PROPOSED
   |
   +--> SUPPORTED --------> RETAINED
   |         |                 |
   |         v                 v
   |      REFINED <-------- CHALLENGED
   |         |
   |         v
   |      CORRECTED
   |
   +--> EXTERNAL / ATTRIBUTED
   |
   +--> METAPHOR / INTERPRETATION
   |
   +--> OPEN HYPOTHESIS
   |
   +--> REJECTED
```

No state change deletes the prior state from provenance history.

## 5. Provenance tuple

For every material proposition q:

**Prov(q) = ⟨origin, first_record, transformations, evidence, challengers, status, responsibility⟩**

This distinguishes:

- origin from influence;
- influence from endorsement;
- criticism from co-authorship;
- conceptual similarity from shared lineage;
- AI mediation from human publication responsibility.

## 6. Relational effect

The weak claim is not that “the relation thinks.” The testable claim is that interaction can alter subsequent states on both observable sides of the task.

Let:

**ΔH_t = H_(t+1) − H_t**

represent observable/reported changes in human framing or commitments, and:

**ΔA_t = A_(t+1) − A_t**

represent changes in the AI-facing interaction state, such as revised context, instructions, retrieved evidence, or subsequent output behavior.

A minimally reciprocal interaction has:

**ΔH_t ≠ 0 and ΔA_t ≠ 0**

across a defined interval, with a reconstructable path through **R_t**.

This is reciprocal task-level transformation, not evidence that both participants possess equivalent cognition or agency.

## 7. Candidate relational contribution measure

For a research outcome **O**, compare explanatory models:

- **M_H:** outcome predicted/explained from human-side variables alone.
- **M_A:** outcome predicted/explained from AI/output variables alone.
- **M_R:** outcome predicted/explained using interaction-trajectory variables in addition to participant variables.

The relational hypothesis gains empirical support only if, under appropriate controls:

**Performance(M_R) > Performance(M_H, M_A)**

on predeclared outcome measures, with the improvement attributable to interaction structure rather than simple extra information volume.

This supplies falsification pressure to the phrase “intelligence in the relation.”

## 8. Candidate trajectory variables

Potential measurable features:

- correction count and correction depth;
- question reframing distance;
- source diversity;
- provenance completeness;
- contradiction detection rate;
- uncertainty calibration change;
- number of superseded claims retained in audit trail;
- semantic/conceptual novelty relative to initial state;
- convergence after adversarial input;
- time-to-correction;
- human acceptance/rejection rate of model proposals;
- model response change after human correction;
- dependence on long-range interaction history;
- robustness when history/provenance is ablated.

## 9. Ablation tests

The relational hypothesis should be tested by removing components.

### A1 — History ablation
Remove prior interaction history while preserving the current question. Does outcome quality materially change?

### A2 — Provenance ablation
Provide claims without origin/correction history. Does attribution accuracy, contradiction handling, or epistemic calibration degrade?

### A3 — Human-correction ablation
Remove prior human corrections. Does the model reproduce superseded claims?

### A4 — Model-continuity ablation
Replace the ongoing model interaction with fresh isolated sessions. Does the research trajectory become less coherent after controlling for supplied information?

### A5 — Interaction-order permutation
Reorder selected exchanges while preserving content. Does sequence/path dependence affect the resulting synthesis?

### A6 — Volume control
Give an isolated comparator the same amount of information but without the interaction trajectory. If performance matches M_R, relational structure may add little beyond information quantity.

## 10. Truth-table seed

Following Levi Reyes’ methodological suggestion, transitions can be classified by minimum provenance conditions:

| Traceable | Attributable | Evidence-linked* | Boundary-consistent | Research treatment |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 | admissible evidence-based transition |
| 1 | 1 | 0 | 1 | admissible hypothesis/metaphor if labeled |
| 1 | 0 | 1 | 1 | provenance failure; do not publish as settled synthesis |
| 0 | 1 | 1 | 1 | continuity failure; investigate missing path |
| 1 | 1 | 1 | 0 | category/boundary failure; revise claim |
| 0 | 0 | 0 | 0 | exclude from evidentiary chain |

*Evidence-linked is required when the proposition is presented as empirical/historical/scientific fact, not for clearly labeled questions or metaphors.

## 11. Responsibility invariant

Even when AI materially contributes to wording, search strategy, comparison, or synthesis:

**Publication responsibility remains assigned to the human author(s) unless a publication framework explicitly defines otherwise.**

The model therefore preserves AI mediation in provenance without treating the AI as a legal/moral co-author by default.

## 12. Continuity criterion

A later research state **S_j** is continuous with an earlier state **S_i** when a reader can reconstruct an admissible path:

**S_i → T_i → … → T_(j−1) → S_j**

including material corrections, source introductions, attribution changes, and rejected branches.

Continuity does **not** require unchanged wording, unchanged meaning, or unchanged conclusion.

## 13. Non-claims

PRTM-0.1 does not establish that:

- cognition literally resides in the relation;
- AI is conscious or self-aware;
- humans and AI have equivalent agency;
- coupling automatically constitutes a cognitive system;
- provenance guarantees truth;
- traceability guarantees ethical legitimacy;
- more interaction necessarily produces better reasoning.

## 14. Empirical research question

The formal question is now narrower than the original rhetoric:

> **Does a provenance-preserving model of persistent Human↔AI interaction explain or predict research-quality outcomes better than models that treat the same human, AI outputs, and information as isolated components?**

If not, the relational hypothesis should be weakened or rejected.

---

**v0.1 principle:** relation is a candidate explanatory variable, not a metaphysical conclusion.