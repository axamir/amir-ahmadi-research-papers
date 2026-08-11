# Living Decision Governance (LDG)

## An Executable Architecture for Continuous Human–AI Decision Governance

**Author:** Amir Ahmadi  
**Affiliation:** Independent Researcher  
**Status:** Public Working Paper / Executable Research Artifact v0.2.0-draft  
**Date:** August 2026  
**Repository:** `axamir/amir-ahmadi-research-papers`  

> **Core thesis:** A consequential decision should not be treated as a one-time event. It should remain observable, challengeable, signed, monitored, reversible where possible, and continuously corrected by real-world evidence.

![LDG Cover](assets/ldg-cover.svg)

---

# 1. Why this document exists

The LDG repository contains separate files for the paper, specification, machine-readable protocol, source code, tests, and landing page. Those modular artifacts are useful for implementation and maintenance, but they fragment the conceptual whole.

This file is the **single comprehensive reference** for the project. It brings together:

- the intellectual origin of the inquiry,
- the core argument,
- definitions,
- architecture,
- decision lifecycle,
- human/AI accountability,
- distributed review,
- stakeholder sensing,
- adaptive authority,
- warning/slowdown/stop controls,
- testable propositions,
- related research,
- implementation logic,
- executable examples,
- falsification criteria,
- limitations,
- and a concrete scenario that can be understood without specialist knowledge.

The modular files remain authoritative for implementation details; this document is the integrated map.

---

# 2. Intellectual origin and attribution

The immediate trigger for this inquiry was a public LinkedIn post by **Christopher J. Skinner** discussing a blind spot in enterprise AI: systems can increasingly represent transactions, documents, workflows, and code while still struggling to represent human thinking, communication, decision quality, and leadership.

Source post supplied at the beginning of this inquiry:

- Christopher J. Skinner, LinkedIn, 2026: public observation on enterprise AI and decision quality.
- Profile: https://www.linkedin.com/in/christopherjskinner/

The post is treated here as an **intellectual trigger**, not as the source of the LDG framework and not as empirical evidence for LDG.

The framework emerged by pushing the initiating question several levels further:

1. What if the missing layer is not only better representation of human thinking?
2. What if the decision itself remains governable after deployment?
3. What if AI agents, responsible humans, collective review, stakeholder signals, and outcome monitoring form one closed loop?
4. What if authority itself expands or contracts according to measured performance?
5. What if every consequential decision has predefined warning, slowdown, pause, and stop conditions?
6. What if disagreement must introduce a testable alternative rather than merely block action?

That chain of questions produced the working concept of **Living Decision Governance**.

### Attribution principle

LDG explicitly distinguishes:

- **Trigger:** the observation that initiated the inquiry.
- **Adjacent research:** prior work that overlaps with parts of the problem.
- **Contribution:** the synthesis, terminology, lifecycle, control model, decision object, adaptive-authority logic, stakeholder feedback loop, signed human/agent accountability, and executable reference model developed here.
- **Evidence:** empirical or experimental results, which v0.2.0 does **not yet claim** to provide beyond illustrative simulation behavior.

---

# 3. The central reframing

A conventional organizational decision is often implicitly modeled as:

```text
Analyze -> Approve -> Execute
```

LDG models it as a persistent governed object:

```text
PROPOSE
  -> CHALLENGE
  -> VERIFY
  -> HUMAN SIGN
  -> COLLECTIVE RATIFY
  -> EXECUTE
  -> OBSERVE
  -> STAKEHOLDER FEEDBACK
  -> RE-SCORE
  -> ADAPT AUTHORITY
  -> CONTINUE / SLOW / RESTRICT / PAUSE / STOP
  -> LEARN
```

The decision therefore remains **alive** after approval.

The unit of governance is not only:

- the AI model,
- the organization,
- the policy,
- or the manager.

It is also the **decision object itself across time**.

![LDG Architecture](assets/ldg-architecture.svg)

---

# 4. The billiard effect

A useful analogy is a billiard shot.

The table may be visible. The balls may be mapped. AI may calculate many plausible trajectories. The available information may be excellent. Yet a small change in:

- angle,
- force,
- timing,
- contact point,
- surface condition,
- or an unmodeled interaction

can produce a materially different outcome.

In organizational systems, the corresponding variables include:

- framing of the question,
- missing context,
- incentive structure,
- risk tolerance,
- timing,
- stakeholder interpretation,
- implementation fidelity,
- leadership judgment,
- and downstream interaction effects.

This does **not** imply that AI is inherently unreliable. It implies that increasing predictive power does not remove sensitivity at the point of intervention.

A paradox follows:

> The more powerful the decision-support system becomes, the more leverage may be concentrated in the final act of authorization.

That can make experienced leadership more valuable rather than less valuable.

---

# 5. Core architecture

LDG is organized as five interacting layers.

## 5.1 Data and world layer

Contains internal and external signals:

- operational metrics,
- financial metrics,
- customer behavior,
- employee signals,
- regulatory changes,
- market conditions,
- safety events,
- model telemetry,
- environmental constraints,
- and external evidence.

## 5.2 AI / agent layer

Specialized agents can:

- generate options,
- challenge assumptions,
- detect missing variables,
- identify contradictions,
- estimate risks,
- run counterfactuals,
- compare scenarios,
- and verify internal consistency.

Agent outputs must be traceable to:

- agent/model identity,
- version,
- input evidence,
- assumptions,
- uncertainty,
- recommended action,
- alternatives,
- and timestamp.

## 5.3 Human accountability layer

Responsible humans:

- interpret context,
- evaluate non-quantified constraints,
- sign or reject agent recommendations,
- introduce testable dissent,
- accept responsibility for authorization,
- and define escalation thresholds.

A signature does not mean the human manually recreated the model's analysis. It means the human accepted accountability for authorizing its use.

## 5.4 Collective review layer

For sufficiently consequential decisions, LDG permits distributed review by multiple qualified humans and agents.

The system should not reduce this layer to simple majority voting.

Possible weights may include:

- domain relevance,
- historical decision quality,
- uncertainty calibration,
- evidence quality,
- reasoning quality,
- recency,
- and conflict-of-interest adjustments.

Participation and authority are therefore distinct.

## 5.5 Stakeholder sensing layer

Affected people continuously or periodically contribute signals.

Potential stakeholder groups include:

- employees,
- customers,
- partners,
- suppliers,
- communities,
- regulators,
- and other materially affected parties.

The goal is not endless voting. The goal is to prevent the governance system from observing only what executives already chose to measure.

---

# 6. Decision object

A minimal LDG decision object should contain:

```yaml
decision_id: LDG-2026-001
question: "Should the company deploy the new AI-assisted process?"
owner: executive_committee
risk_class: high
expected_outcomes:
  revenue_change: "+12%"
  cycle_time_change: "-20%"
stakeholder_metrics:
  employee_trust_floor: 0.65
  customer_satisfaction_floor: 0.70
thresholds:
  warning_deviation: 0.10
  restrict_deviation: 0.20
  pause_deviation: 0.30
  terminate_deviation: 0.45
human_signatories:
  - role: COO
  - role: Quality Lead
agent_reviews:
  - risk_agent_v3
  - operations_agent_v2
review_cadence: daily
state: ACTIVE
authority_level: 1.0
reputation_links: enabled
```

A decision is therefore both a **record** and a **state machine**.

---

# 7. Disagreement protocol

A governance system can fail by acting too quickly, but it can also fail by never deciding.

If any objection forces unlimited re-analysis, decision-making approaches an impossible search for certainty.

LDG therefore proposes:

> Dissent earns a right to re-evaluation when it contributes a testable hypothesis, missing variable, evidence claim, explicit alternative, or bounded uncertainty that can be checked.

Examples of actionable dissent:

- “The model assumes stable supply conditions, but the supplier contract expires next month.”
- “Employee trust is falling, but that variable is absent from the dashboard.”
- “This customer cohort is behaving differently from the population used for validation.”
- “The regulatory environment changes before the projected benefit is realized.”

Criticism without a proposed solution should **not be deleted**. A person may correctly detect harm without knowing how to repair it. LDG therefore distinguishes:

- **signal-only criticism** -> recorded with lower decision weight,
- **evidence-backed criticism** -> higher weight,
- **proposal-backed criticism** -> higher actionability,
- **validated counterexample** -> mandatory re-evaluation.

The system should have a defined analysis budget and deadline so that uncertainty does not become paralysis.

---

# 8. Continuous monitoring and control states

Every consequential decision should define monitoring conditions before deployment.

At minimum:

- expected trajectory,
- warning threshold,
- emergency threshold,
- slowdown threshold,
- temporary suspension condition,
- permanent stop condition,
- review cadence,
- responsible signatories,
- affected stakeholder groups,
- and permitted authority range.

A simplified control state model:

```text
ACTIVE
  | deviation / weak signal
  v
WARNING
  | repeated or larger deviation
  v
RESTRICTED
  | unresolved / high-risk
  v
PAUSED
  | unacceptable or compounding risk
  v
TERMINATED
```

Recovery can occur if predefined conditions are satisfied.

The key principle is proportionality:

- low-impact reversible decisions -> lighter monitoring,
- high-impact irreversible decisions -> tighter thresholds, more signatories, stronger verification.

---

# 9. Adaptive authority and reputation

Authority should not be static.

If a decision-maker, team, or agent repeatedly performs well in a specific domain, the system may grant greater autonomy.

If performance degrades, the system may:

- reduce decision scope,
- require additional signatures,
- shorten review intervals,
- increase verification intensity,
- suspend autonomous execution,
- reduce voting weight,
- or remove an actor from the review network.

This creates **reputation-linked authority**.

Reputation must be:

- domain-specific,
- time-bounded,
- evidence-based,
- auditable,
- recoverable,
- resistant to popularity bias,
- and separated from permanent social ranking.

A decision-maker should lose authority because of demonstrated decision degradation, not because of dissent or organizational politics.

---

# 10. Stakeholder participation and the measurement problem

A decision can look successful on an executive dashboard while hidden harm grows elsewhere.

Example:

- revenue: +20%
- processing speed: +30%
- operating cost: -15%
- employee trust: -25%
- customer confidence: -12%

If the organization measured only the first three variables, the decision would appear successful.

LDG therefore requires a **multi-perspective quality envelope**.

Stakeholder feedback can be collected through:

- short recurring pulse surveys,
- structured issue reports,
- customer outcome telemetry,
- complaint categories,
- safety signals,
- privacy incidents,
- employee turnover or absenteeism,
- opt-out behavior,
- qualitative review,
- and domain-specific measures.

Every meaningful percentage change should be able to trigger:

1. an updated dashboard,
2. a list of emerging challenges,
3. agent-generated candidate explanations,
4. agent-generated candidate improvements,
5. human checklist review,
6. signed approval or rejection,
7. collective verification for high-impact changes,
8. and an updated authority/risk state.

This is how the system learns from the people affected by a decision without pretending every opinion has identical epistemic weight.

---

# 11. A concrete example: AI-assisted customer support transformation

Assume a company deploys a new AI-assisted support system.

## Initial decision

The executive objective is:

- reduce average response time by 30%,
- reduce support cost by 15%,
- keep customer satisfaction above 0.75,
- keep employee trust above 0.65,
- keep severe complaint rate below 3%.

The AI agents recommend full deployment.

Two managers sign the recommendation after reviewing:

- benchmark evidence,
- model quality,
- staffing implications,
- legal constraints,
- and rollback options.

The collective review approves deployment.

## Week 1

Results:

- response time: -22%
- cost: -7%
- customer satisfaction: 0.80
- employee trust: 0.72
- severe complaints: 1.4%

State: `ACTIVE`

## Week 3

Results:

- response time: -35%
- cost: -14%
- customer satisfaction: 0.76
- employee trust: 0.58
- severe complaints: 2.1%

Traditional dashboard conclusion: success.

LDG conclusion: hidden stakeholder degradation detected.

State: `RESTRICTED`

Actions:

- authority reduced from 1.00 to 0.50,
- full automation limited to low-risk cases,
- employee-trust agent generates candidate causes,
- managers review a checklist,
- new training and escalation rules are proposed,
- signatories approve a two-week corrective experiment.

## Week 5

Results:

- response time: -28%
- cost: -11%
- customer satisfaction: 0.79
- employee trust: 0.67
- severe complaints: 1.8%

State: recovery to `WARNING`, then potentially `ACTIVE` after another successful review.

The key lesson is not that employee trust must always outweigh revenue. The lesson is that **the system cannot silently erase a stakeholder dimension simply because it was absent from the first dashboard**.

---

# 12. Why this is different from ordinary AI governance

LDG is complementary to existing governance systems.

## NIST AI RMF

NIST AI RMF organizes AI risk work around **Govern, Map, Measure, Manage** and explicitly treats risk management as continuous across the AI lifecycle. LDG aligns with that continuous-risk orientation but changes the primary unit of attention from the AI system to the **decision and its consequences after authorization**.

## ISO/IEC 42001

ISO/IEC 42001 establishes requirements for an AI Management System and continual improvement. LDG can be interpreted as a possible operational layer beneath such a management system: a concrete way to represent and monitor consequential decision objects.

## EU AI Act

The EU AI Act regulates AI systems according to risk and context. LDG does not replace legal obligations. It provides a possible decision-governance mechanism for organizations operating inside such regulatory constraints.

---

# 13. Adjacent research: related, not claimed as inspiration

The following work overlaps with components of LDG and should be understood as **adjacent prior art**, not as the intellectual origin of this framework.

## 13.1 Algorithmic decision support as a human activity

Joachim Meyer (2024), *Doing AI: Algorithmic decision support as a human activity*, argues that algorithmic decision support necessarily includes multiple human decisions before, during, and after development and use. This is compatible with LDG's insistence that human accountability does not disappear when an AI system enters the loop.

https://arxiv.org/abs/2402.14674

## 13.2 Participatory AI and stakeholder deliberation

Zhang et al. (2023), *Deliberating with AI*, explores using ML tools to help decision-makers and affected stakeholders examine and improve organizational decision processes. This overlaps with LDG's stakeholder-sensing and participatory review layers.

https://arxiv.org/abs/2302.11623

## 13.3 Human/AI collective intelligence

De Liddo, Anastasiou, and Buckingham Shum (2026), *Human/AI Collective Intelligence for Deliberative Democracy*, studies how AI can augment collective intelligence in deliberative processes and emphasizes human-centered orchestration of stakeholder participation.

https://arxiv.org/abs/2603.16260

## 13.4 Agentic AI in decentralized governance

Han, Gliozzo, Lee, and Capponi (2025), *DAO-AI: Evaluating Collective Decision-Making through Agentic AI in Decentralized Governance*, studies AI agents as participants in DAO voting with interpretable and auditable signals. This is adjacent to LDG's distributed review concept, though LDG's focus is not token voting and includes post-deployment monitoring and adaptive authority.

https://arxiv.org/abs/2510.21117

## 13.5 Contestability

Moreira et al. (2025), *Explainable AI Systems Must Be Contestable*, formalizes contestability mechanisms and proposes assessment criteria. This is adjacent to LDG's challenge, dissent, re-evaluation, and recourse logic.

https://arxiv.org/abs/2506.01662

### Positioning statement

LDG does not claim that continuous monitoring, stakeholder participation, human-in-the-loop review, DAO governance, reputation systems, or AI risk management are individually novel.

The working contribution is the **integration of these mechanisms around a persistent decision object with explicit lifecycle states, signed human/agent accountability, stakeholder sensing, bounded dissent, adaptive authority, and executable stop/slow/restrict controls**.

Novelty remains a research question that requires deeper prior-art review before any formal novelty claim.

---

# 14. Executable model

The repository contains a Python reference implementation.

Current core file:

```text
src/ldg.py
```

Run:

```bash
python papers/2026-living-decision-governance/src/ldg.py
```

The model tracks:

- decision state,
- outcome score,
- stakeholder score,
- risk score,
- deviation,
- authority level,
- reputation,
- and state transitions.

The purpose is **not** to claim predictive validity.

The purpose is to expose the governance logic in executable form so that another researcher, engineer, or AI system can:

- inspect assumptions,
- change thresholds,
- run counterexamples,
- test failure modes,
- and falsify specific behavior.

Additional scenario scripts are included under `examples/` in v0.2.0.

---

# 15. Falsification and verification

A framework becomes more credible when it states how it could fail.

LDG should be challenged on at least the following dimensions.

## F1. Early detection

If continuous LDG monitoring does not detect meaningful divergence earlier than one-time approval systems under realistic conditions, the monitoring claim is weakened.

## F2. Stakeholder visibility

If stakeholder sensing does not reveal materially relevant information beyond standard business KPIs, the additional participation layer may not justify its cost.

## F3. Adaptive authority

If dynamic authority restriction creates more harm through false positives, delay, or political gaming than it prevents, adaptive authority should be rejected or redesigned.

## F4. Signed accountability

If human signatures become ceremonial and do not improve traceability, responsibility, or challenge behavior, the signature mechanism is insufficient.

## F5. Governance overhead

If the system materially slows low-risk decisions without corresponding benefit, risk-proportional governance must become more aggressive.

## F6. Participation quality

If frequent stakeholder participation produces fatigue, representation bias, manipulation, or noise, sensing must be sampled, weighted, privacy-preserving, or redesigned.

## F7. Reputation gaming

If actors learn to maximize reputation metrics rather than decision quality, the reputation mechanism becomes counterproductive.

---

# 16. Risks and failure modes

LDG introduces its own risks:

- governance overload,
- analysis paralysis,
- metric gaming,
- participation fatigue,
- surveillance risk,
- popularity bias,
- consensus capture,
- authority concentration,
- false confidence from dashboards,
- accountability diffusion,
- politically motivated reputation penalties,
- adversarial stakeholder manipulation,
- model collusion or correlated agent failure,
- and false precision in thresholds.

These are not side notes. They are first-class design constraints.

---

# 17. Design principles

The working principles of LDG are:

1. **Decisions remain governable after deployment.**
2. **AI recommends; accountable organizations authorize.**
3. **Dissent must be preserved, but consequential blocking should be testable.**
4. **No high-impact decision should be fire-and-forget.**
5. **Authority is earned and can be reduced.**
6. **Stakeholder harm can invalidate apparent business success.**
7. **Monitoring intensity should scale with reversibility and consequence.**
8. **A kill switch is a governance primitive, not a failure of innovation.**
9. **Criticism can be a signal even without a solution.**
10. **The system must learn where the process degraded, not merely who lost.**
11. **The quality of the feedback loop may matter more than the quality of any single recommendation.**

---

# 18. Machine-readable research artifact

The repository contains machine-readable files intended to help other AI systems inspect the project.

Goals:

- make assumptions explicit,
- expose threshold logic,
- list expected behaviors,
- define falsification tests,
- separate normative claims from executable behavior,
- and make adversarial review easier.

An AI reviewer should be able to answer:

- What exactly is being claimed?
- Which claims are only hypotheses?
- Which behaviors are encoded in software?
- Which variables are missing?
- What counterexamples break the model?
- What evidence would be required for real-world validation?

---

# 19. Research roadmap

Next research steps:

- deeper systematic prior-art review,
- formal definition of the decision object,
- reputation-weighted review models,
- bounded dissent protocols,
- privacy-preserving stakeholder sensing,
- cryptographic decision provenance,
- simulation of correlated agent failure,
- adversarial stakeholder attacks,
- governance capture simulations,
- reversible vs. irreversible decision classes,
- longitudinal decision portfolios,
- case studies in regulated domains,
- and empirical comparison against existing approval workflows.

Potential domains:

- healthcare,
- financial services,
- aerospace,
- public-sector policy,
- high-risk enterprise automation,
- AI model deployment,
- manufacturing quality,
- and autonomous operations.

---

# 20. Research identity

LDG is intentionally published as a **versioned, inspectable working artifact**.

The project is not presented as a finished universal standard.

Its identity comes from three commitments:

### 20.1 Traceable origin

The initiating public observation is acknowledged rather than absorbed invisibly.

### 20.2 Independent development

The framework is judged by its mechanisms and evidence, not by the status of the person who triggered the inquiry.

### 20.3 Executability

The project should be runnable, inspectable, falsifiable, and improvable by others.

This is the intended co-creation paradigm:

```text
Public idea / observation
        ↓
Independent questioning
        ↓
Conceptual expansion
        ↓
Literature comparison
        ↓
Executable model
        ↓
Open criticism and testing
        ↓
Versioned refinement
```

The community is therefore not used as a source of uncredited ideas; it is treated as an ecosystem of traceable intellectual triggers, adjacent work, critique, and verification.

---

# 21. Conclusion

Enterprise AI may not need to reproduce human leadership internally before organizations can improve decision quality.

A different route is possible:

- make consequential decisions persistent,
- require traceable AI analysis,
- require accountable human authorization,
- allow structured collective review,
- preserve stakeholder signals,
- monitor outcomes continuously,
- slow or stop harmful trajectories,
- adapt authority according to evidence,
- and preserve a record of why the system changed course.

The future of decision intelligence may therefore not be better answers alone.

> **It may be better feedback loops around decisions that remain accountable after they enter the world.**

---

# References

1. Skinner, C. J. (2026). Public LinkedIn observation on enterprise AI, human thinking, communication, decision quality, and leadership. Intellectual trigger for this inquiry. Profile: https://www.linkedin.com/in/christopherjskinner/
2. Tabassi, E. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0).* NIST AI 100-1. https://doi.org/10.6028/NIST.AI.100-1
3. ISO/IEC 42001:2023. *Information technology — Artificial intelligence — Management system.* International Organization for Standardization. https://www.iso.org/standard/81230.html
4. Meyer, J. (2024). *Doing AI: Algorithmic decision support as a human activity.* arXiv:2402.14674. https://arxiv.org/abs/2402.14674
5. Zhang, A., Walker, O., Nguyen, K., Dai, J., Chen, A., & Lee, M. K. (2023). *Deliberating with AI: Improving Decision-Making for the Future through Participatory AI Design and Stakeholder Deliberation.* arXiv:2302.11623. https://arxiv.org/abs/2302.11623
6. De Liddo, A., Anastasiou, L., & Buckingham Shum, S. (2026). *Human/AI Collective Intelligence for Deliberative Democracy: A Human-Centred Design Approach.* arXiv:2603.16260. https://arxiv.org/abs/2603.16260
7. Han, C., Gliozzo, A., Lee, J., & Capponi, A. (2025). *DAO-AI: Evaluating Collective Decision-Making through Agentic AI in Decentralized Governance.* arXiv:2510.21117. https://arxiv.org/abs/2510.21117
8. Moreira, C., Palatkina, A., Braca, D., Walsh, D. M., Leihn, P. J., Chen, F., & Hubig, N. C. (2025). *Explainable AI Systems Must Be Contestable: Here's How to Make It Happen.* arXiv:2506.01662. https://arxiv.org/abs/2506.01662

---

## License and citation

Unless otherwise stated, this research artifact follows the repository's CC BY 4.0 policy.

See `CITATION.cff` for citation metadata.
