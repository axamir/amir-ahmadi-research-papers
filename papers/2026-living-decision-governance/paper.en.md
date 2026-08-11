# Living Decision Governance

## A Closed-Loop Architecture for Human–AI Organizational Decision Making

**Author:** Amir Ahmadi  
**Affiliation:** Independent Researcher  
**Status:** Public Working Paper v0.1.0  
**Date:** August 2026

---

## Abstract

Enterprise AI increasingly supports transactions, documents, workflows, code, prediction, and recommendation. Yet consequential organizational decisions remain difficult to govern because decision quality is not only a property of the model or the information available at decision time. It emerges from a dynamic interaction among data, interpretation, judgment, authority, stakeholder response, changing context, and post-deployment consequences.

This paper proposes **Living Decision Governance (LDG)**, a closed-loop architecture in which high-impact decisions are treated as governed, continuously monitored objects rather than one-time approvals. LDG combines AI-agent analysis, challenge and verification, accountable human signatures, collective review, measurable deployment thresholds, stakeholder sensing, adaptive authority, and explicit slowdown, suspension, and stop mechanisms. The central claim is that the future of decision intelligence may depend less on producing better isolated answers and more on building better feedback loops around decisions after they enter the world.

The framework is presented as a conceptual and executable research artifact, not as a validated safety standard. A small reference implementation is included to make its assumptions inspectable and falsifiable.

---

## 1. Origin of the inquiry

This work was triggered by a public observation from **Christopher J. Skinner** concerning a blind spot in enterprise AI: systems can increasingly represent transactions, documents, workflows, and code, while still struggling to represent human thinking, communication, decision quality, and leadership.

Rather than treating that observation as a conclusion, this paper uses it as a research question:

> What if the missing layer is not only better representation of the decision-maker, but continuous governance of the decision itself after it enters the world?

The contribution developed here is independent of the initiating observation and should be evaluated on its own assumptions, mechanisms, and evidence.

---

## 2. The decision is not an event

Most organizational governance models implicitly treat a decision as an event:

```text
Analyze → Approve → Execute
```

LDG instead treats a consequential decision as a **stateful object with a lifecycle**:

```text
Propose → Challenge → Verify → Human Sign → Collective Ratification
→ Execute → Observe → Stakeholder Feedback → Re-score
→ Slow / Restrict / Pause / Stop / Expand Authority → Learn
```

A decision therefore remains governable after deployment.

This reframing matters because the quality of an initial decision cannot fully determine the quality of its real-world consequences. Context changes. Stakeholders respond. Hidden variables emerge. The same policy can behave differently across environments. A decision that was reasonable at time *t0* may become harmful at time *t1*.

---

## 3. The billiard effect

A useful metaphor is a billiard shot.

The table may be visible. The balls may be mapped. AI may calculate plausible trajectories. The available information may even be excellent. Yet a small difference in angle, force, timing, contact point, or unmodeled condition can produce a materially different path.

In organizational systems, the equivalent variables include:

- framing of the question,
- missing context,
- timing,
- risk tolerance,
- incentive structure,
- stakeholder interpretation,
- implementation fidelity,
- leadership judgment,
- and downstream interaction effects.

The implication is not that AI is unreliable by definition. The implication is that **increasing predictive power does not eliminate sensitivity at the point of intervention**.

In some settings, better AI may make experienced leadership more valuable because the system can act faster and at greater scale. The final human intervention therefore may carry more leverage, not less.

---

## 4. From single decision-maker to distributed judgment

LDG does not assume that one superior human should sit above an AI system.

For sufficiently consequential decisions, the architecture can include a **distributed decision network** composed of qualified human reviewers and specialized AI agents.

AI agents may:

- generate alternatives,
- identify missing variables,
- challenge assumptions,
- estimate risks,
- compare scenarios,
- and test internal consistency.

Human reviewers may:

- evaluate context,
- identify non-quantified constraints,
- sign judgments,
- dissent with reasons,
- and accept accountable responsibility for specific recommendations.

Collective review should not be reduced to simple majority voting. Expertise, decision history, domain relevance, uncertainty, and reasoning quality may justify differentiated weight.

The framework therefore distinguishes **participation** from **authority**.

---

## 5. Disagreement must be testable

A governance system can fail in the opposite direction by never deciding.

If every objection creates an indefinite requirement for more analysis, the system approaches an impossible search for certainty. In practice, this resembles trying to resolve an unbounded calculation before acting.

LDG therefore proposes a rule:

> Dissent earns a right to re-evaluation when it introduces a testable hypothesis, missing variable, evidence claim, or explicit alternative.

This does not mean intuition has no value. It means that intuition must be translated into something the system can inspect:

- “The customer segment is behaving differently.”
- “The model assumes stable supply conditions.”
- “The employee-trust metric is missing.”
- “The regulatory environment changes next quarter.”

The system then re-checks the claim within a defined time and decision budget.

---

## 6. Decision monitoring and staged intervention

Every consequential decision should define its monitoring conditions **before deployment**.

At minimum:

- expected outcome trajectory,
- warning threshold,
- emergency threshold,
- slowdown threshold,
- temporary suspension condition,
- permanent stop condition,
- review cadence,
- responsible human signatories,
- affected stakeholder groups,
- and permitted authority range.

A simplified state model is:

```text
ACTIVE
  ↓ deviation
WARNING
  ↓ worsening deviation
RESTRICTED
  ↓ unresolved / high-risk
PAUSED
  ↓ unacceptable risk
TERMINATED
```

Recovery is also possible if predefined conditions are met.

This makes governance proportional to sensitivity. A low-impact reversible decision may require light monitoring. A high-impact irreversible decision should require narrower thresholds and more conservative authority.

---

## 7. Adaptive authority

Authority should not be static.

If a decision-maker, team, or agent consistently produces high-quality outcomes within its authorized domain, the system may allow broader autonomy.

If performance degrades, the system may:

- reduce decision scope,
- require additional signatures,
- shorten review intervals,
- increase verification intensity,
- suspend autonomous execution,
- or remove an actor from the decision network.

This creates a form of **reputation-linked authority**.

However, reputation must not become a permanent social ranking. It should be:

- domain-specific,
- time-bounded,
- evidence-based,
- auditable,
- and recoverable through improved performance.

---

## 8. Stakeholder sensing

Executive dashboards can report improvement while hidden harm grows elsewhere.

A decision may increase revenue and efficiency while reducing:

- employee trust,
- customer confidence,
- privacy,
- safety,
- accessibility,
- community acceptance,
- or long-term resilience.

LDG therefore adds a **stakeholder sensing layer**.

Affected groups may include:

- employees,
- customers,
- partners,
- suppliers,
- communities,
- regulators,
- and other materially affected parties.

Signals can be collected continuously or periodically and compared against the expected decision trajectory.

Criticism without a proposed remedy should not disappear. A stakeholder may correctly identify pain without possessing the expertise to design the solution. LDG therefore treats unsupported criticism as a lower-confidence signal, while evidence-backed or proposal-backed critique may receive greater weight.

The purpose is not to create endless voting. It is to prevent the governance system from seeing only what senior management already chose to measure.

---

## 9. Signed human–agent accountability

Agent recommendations should be traceable.

For consequential decisions, an agent output should record:

- model/agent identity,
- version,
- input evidence,
- assumptions,
- uncertainty,
- recommended action,
- dissenting alternatives,
- and timestamp.

A responsible human may then sign the recommendation, modify it, or reject it.

The signature does not mean the human manually reproduced the analysis. It means the human accepted accountability for authorizing its use within the decision context.

This avoids the accountability failure mode:

> “The AI decided.”

AI can recommend. Organizations authorize.

---

## 10. A closed-loop model of decision quality

LDG proposes that decision quality be evaluated across four interacting layers:

### 10.1 Analytical quality

Were the data, assumptions, models, and alternatives reasonable?

### 10.2 Judgment quality

Did accountable humans interpret the evidence appropriately and challenge critical assumptions?

### 10.3 Execution quality

Was the decision implemented as intended?

### 10.4 Outcome quality

Did the observed consequences remain within acceptable bounds across business, operational, human, and societal dimensions?

A failure in one layer should not automatically be assigned to another.

For example, a strong decision can fail through poor implementation. A weak decision can appear successful because of favorable external conditions. A good model can be used irresponsibly. A poor model can be corrected by strong human judgment.

The governance objective is therefore not merely to identify **who was wrong**, but to locate **where the decision process degraded**.

---

## 11. Relationship to existing governance approaches

LDG is intended to be complementary to existing AI governance and risk-management approaches rather than a replacement for them.

The **NIST AI Risk Management Framework (AI RMF 1.0)** is a voluntary, rights-preserving, use-case-agnostic framework for managing AI risks and promoting trustworthy and responsible use. Its core logic emphasizes governance, mapping, measurement, and management across the AI lifecycle.

**ISO/IEC 42001:2023** specifies requirements for establishing, implementing, maintaining, and continually improving an Artificial Intelligence Management System within an organization. Its management-system orientation is particularly relevant to continuous governance.

The **EU AI Act** provides a regulatory framework for AI systems in the European Union and introduces obligations based on system risk and context.

LDG differs in its primary unit of analysis. Instead of focusing principally on the AI system or the organizational management system, LDG focuses on the **decision object and its post-deployment lifecycle**.

This distinction is conceptual and requires further comparison with adjacent research and standards.

---

## 12. Executable reference model

The accompanying Python implementation models a small subset of LDG:

- active decision state,
- outcome score,
- stakeholder score,
- risk,
- deviation,
- authority level,
- warning/restriction/pause/termination transitions,
- and decision-maker reputation.

The simulation is intentionally minimal.

Its purpose is not to claim real-world validity. Its purpose is to expose the logic clearly enough that another researcher or AI system can:

1. inspect the assumptions,
2. run counterexamples,
3. change thresholds,
4. test failure modes,
5. and falsify specific claims.

---

## 13. Propositions for testing

### P1 — Continuous governance proposition

Post-deployment monitoring of high-impact decisions will detect meaningful divergence earlier than one-time approval systems, assuming relevant signals are observable.

### P2 — Stakeholder visibility proposition

Adding stakeholder signals will reveal harms or degradations not observable through executive business KPIs alone.

### P3 — Adaptive authority proposition

Dynamically restricting authority after repeated poor outcomes can reduce repeated decision harm, subject to false-positive controls and recovery mechanisms.

### P4 — Signed accountability proposition

Explicit human sign-off on consequential AI-agent recommendations will improve traceability of responsibility compared with systems that record only model output.

### P5 — Feedback-loop proposition

In complex AI-assisted organizations, the quality of the decision feedback loop may be a stronger determinant of long-run governance quality than the quality of any single recommendation.

These propositions are hypotheses, not established findings.

---

## 14. Risks and open problems

LDG introduces its own risks.

### 14.1 Governance overload

Continuous monitoring can become bureaucratic and slow routine decisions.

### 14.2 Metric gaming

If authority depends on measured outcomes, actors may optimize for the metric rather than the underlying goal.

### 14.3 Participation fatigue

Daily or frequent stakeholder participation may become unrealistic or unrepresentative.

### 14.4 Popularity bias

Collective review can reward consensus over correct minority views.

### 14.5 Surveillance risk

Fine-grained monitoring of employees and stakeholders can violate privacy or create chilling effects.

### 14.6 False confidence

An elaborate governance dashboard may create the illusion that all meaningful variables are observable.

### 14.7 Accountability diffusion

Collective signatures can obscure individual responsibility unless roles are explicit.

These risks should be treated as first-class design constraints.

---

## 15. Research agenda

Future work should evaluate:

- formal models of reputation-weighted decision review,
- bounded disagreement protocols,
- domain-specific authority decay,
- privacy-preserving stakeholder sensing,
- decision provenance standards,
- agent-verification protocols,
- thresholds for reversible versus irreversible decisions,
- longitudinal simulations,
- adversarial manipulation,
- governance capture,
- and empirical case studies in regulated domains.

A particularly important question is whether the LDG decision object can be expressed in a machine-readable standard compatible with existing governance frameworks.

---

## 16. Conclusion

Enterprise AI may not need to “understand leadership” in a human-like sense before organizations can improve decision quality.

A different route is possible: make the decision itself observable, challengeable, signed, monitored, reversible where possible, and continuously corrected by real-world evidence.

The future of decision intelligence may therefore not be better answers alone.

> **It may be better feedback loops.**

---

## References

1. Tabassi, E. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0).* NIST AI 100-1. https://doi.org/10.6028/NIST.AI.100-1
2. Autio, C., Schwartz, R., Dunietz, J., Jain, S., Stanley, M., Tabassi, E., Hall, P., & Roberts, K. (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile.* NIST AI 600-1. https://doi.org/10.6028/NIST.AI.600-1
3. ISO/IEC 42001:2023. *Information technology — Artificial intelligence — Management system.* International Organization for Standardization.
4. Regulation (EU) 2024/1689. *Artificial Intelligence Act.* European Union.
5. Skinner, C. J. (2026). Public LinkedIn observation on enterprise AI, human thinking, communication, decision quality, and leadership. Intellectual trigger acknowledged; formal archival citation to be added if a stable public URL is retained in the release metadata.

---

## Research integrity note

This working paper distinguishes between an **intellectual trigger**, a **conceptual contribution**, and **empirical evidence**. Christopher J. Skinner's public post is acknowledged as the trigger for the inquiry. The LDG architecture, terminology, synthesis, propositions, and reference implementation presented here are the author's working contribution. No claim of empirical validation is made in v0.1.0.
