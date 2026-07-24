# Positioning HACS in Existing Research

## Literature Positioning Note for v1.1.0 Development

**Framework:** Human–AI Collaborative Systems (HACS)  
**Author:** Amir Ahmadi  
**Status:** Working research note — literature positioning, not a novelty claim  
**Year:** 2026

---

## 1. Purpose and Caution

HACS should not be presented as though research on human–AI collaboration begins with this framework. It does not.

Human-centered AI, human–AI teaming, hybrid intelligence, distributed cognition, joint cognitive systems, trust calibration, explainable AI, and autonomous-agent research already address substantial parts of the problem space.

The relevant research question is therefore not:

> Has anyone studied humans and AI working together before?

The relevant question is:

> Does HACS provide a useful system-level synthesis or operational emphasis that is not adequately captured when these concerns are treated separately?

At the present stage, HACS should be described as a **proposed integrative research framework**. Any stronger novelty claim requires a systematic literature review and empirical comparison.

---

## 2. Human-Centered AI (HCAI)

Human-Centered AI emphasizes AI systems designed around human values, needs, capabilities, safety, control, and social consequences. This tradition provides a foundational normative commitment for HACS: increasing AI capability should not require surrendering human agency.

### Strong overlap with HACS

- preservation of human control and agency;
- responsible and safe AI design;
- transparency and accountability;
- complementarity between human and machine capability;
- evaluation beyond raw model performance.

### HACS emphasis

HACS adopts these concerns but places particular emphasis on the **durability of collaboration across time**. It asks not only whether an AI system is human-centered at a moment of use, but whether the collaborative architecture preserves context, provenance, correction, role boundaries, calibrated trust, and human agency as interaction develops.

Therefore HACS should be positioned under, beside, or in dialogue with HCAI—not as its replacement.

---

## 3. Human–AI Teaming (HAT)

Human–AI Teaming is one of the closest neighboring research areas.

The National Academies' 2022 consensus report, *Human-AI Teaming: State-of-the-Art and Research Needs*, treats effective human–AI teams as systems that should exploit complementary human and AI capabilities while addressing communication, coordination, shared cognition, situation awareness, transparency, trust, bias, training, and human-systems integration.

This creates substantial overlap with HACS.

### Strong overlap with HACS

- AI as collaborator or teammate rather than only a passive tool;
- complementary capabilities;
- shared cognition and coordination;
- trust and transparency;
- team-level performance;
- human control and responsibility;
- system-level metrics.

### HACS emphasis

HACS currently differs primarily in emphasis rather than proven theoretical territory. Its proposed unit of analysis is an **enduring collaborative system** whose state can extend across sessions, artifacts, model changes, interruptions, and handovers.

This makes **Context Continuity**, provenance, recovery, and versioned collaborative history first-class architectural concerns.

Human–AI Teaming research already provides much of the theoretical foundation needed to test whether this additional emphasis is useful. HACS should therefore explicitly build on HAT rather than claim independence from it.

---

## 4. Human–AI Joint Cognitive Systems and Joint Cognitive Systems

Joint Cognitive Systems approaches shift attention away from isolated human or machine components toward the behavior of the combined system. This is conceptually very close to HACS's decision to change the unit of analysis from model capability to collaborative-system quality.

Recent work applying Human-Centered AI to Human–AI Joint Cognitive Systems also explicitly argues that human–AI teaming can be represented as a joint cognitive system while remaining human-centered.

### Strong overlap with HACS

- system rather than component as unit of analysis;
- coordination between heterogeneous cognitive resources;
- performance emerging from interaction;
- adaptive allocation of roles;
- emphasis on the joint human–machine system.

### HACS emphasis

HACS adds a proposed architectural vocabulary around persistent collaboration:

- Context Continuity;
- Collaborative Commitment;
- Artificial Character as designed behavioral consistency;
- provenance across transitions;
- recovery after interruption or context loss;
- explicit versioning of the collaboration state.

Whether these constructs constitute genuinely new theory or a new operationalization of established joint-system ideas remains an open research question.

---

## 5. Distributed Cognition

Distributed cognition challenges the assumption that cognition is confined to an individual mind. Cognitive work can be distributed across people, representations, artifacts, procedures, and environments.

This tradition is highly relevant to HACS because HACS similarly treats meaningful performance as something that can emerge from a broader human–AI–artifact system rather than from a model alone.

### Strong overlap with HACS

- cognition distributed across multiple components;
- artifacts and representations as part of cognitive work;
- system-level analysis;
- coordination and transformation of information across components.

### HACS emphasis

HACS narrows this broader insight to contemporary AI collaboration and asks how a distributed human–AI system can remain accountable and coherent longitudinally.

The framework therefore needs to show that terms such as Context Continuity add operational value beyond established concepts of distributed representations, coordination, shared state, and cognitive artifacts.

---

## 6. Hybrid Intelligence and Collaborative Intelligence

Hybrid-intelligence research investigates systems in which human and machine intelligence complement one another to achieve outcomes that neither may achieve as effectively alone.

This is closely aligned with HACS's use of **Collaborative Intelligence**.

### Strong overlap with HACS

- complementary strengths;
- joint problem solving;
- learning through human–machine interaction;
- system performance beyond either component alone.

### HACS emphasis

HACS treats joint capability as only one dimension of collaboration quality. A system should not be considered successful merely because combined performance improves.

The framework also asks whether the collaboration preserves:

- human agency;
- calibrated trust;
- provenance;
- continuity;
- correction mechanisms;
- role stability;
- recoverability.

This distinction may become important empirically: a high-performing hybrid system could still score poorly as a durable HACS if it creates over-reliance, loses decision provenance, or cannot recover safely from context failure.

---

## 7. Trust Calibration Research

Trust calibration research examines whether human reliance on an AI or automated system appropriately reflects the system's actual reliability.

Existing work demonstrates that both over-trust and under-trust can degrade safety and performance, and recent research continues to develop dynamic and quantitative approaches to calibration.

### Strong overlap with HACS

Trust Calibration is already an established research problem. HACS must not present it as a newly invented concept.

### HACS emphasis

HACS treats trust calibration as one dimension within a larger longitudinal collaborative architecture.

The proposed question becomes:

> Can trust remain appropriately calibrated as system capability, task context, model identity, stored context, and human expectations change over time?

This suggests a longitudinal extension that should be tested rather than assumed.

---

## 8. Agentic AI

Agentic AI generally emphasizes systems capable of planning, tool use, multi-step execution, adaptation, and varying degrees of autonomous action toward goals.

The central design question is often:

> How effectively can the AI act?

HACS asks a different but complementary question:

> Under what collaborative architecture should action occur so that context, responsibility, human agency, trust, provenance, and recovery remain governable?

### Relationship

An AI agent may be one component of a HACS.

But agentic capability alone does not create a HACS.

A highly autonomous agent could fail HACS requirements if it:

- obscures responsibility;
- weakens meaningful human control;
- carries forward incorrect context;
- cannot explain provenance;
- encourages inappropriate reliance;
- or cannot recover safely from failure.

Thus HACS should be understood as an architectural and evaluative layer that can include agentic systems without being reducible to agent autonomy.

---

## 9. What HACS May Contribute

Based on this preliminary positioning, the strongest potential contribution of HACS is **not the invention of human–AI collaboration itself**.

Its potential contribution is the integration of several established concerns around a specific object of study:

> the quality and durability of the human–AI collaborative system across time and transition.

The candidate contribution can be expressed through five propositions.

### Proposition 1 — Change the primary unit of evaluation

Evaluate the human–AI collaborative system, not only the model or isolated interaction.

### Proposition 2 — Treat continuity as an architectural property

Distinguish retrieval-oriented memory from the preservation of decision meaning, provenance, constraints, unresolved state, and relevance across future collaboration.

### Proposition 3 — Evaluate longitudinal collaboration quality

Measure not only task performance but how agency, trust, alignment, and recoverability behave across repeated interaction and change.

### Proposition 4 — Join continuity and governance

Persistent context without governance is insufficient; governance without continuity may fail to account for accumulated collaborative state.

### Proposition 5 — Preserve the evolution of the collaboration itself

Versioned records, corrections, transitions, and handovers can become auditable parts of the collaborative architecture rather than invisible implementation history.

These propositions are hypotheses for research development, not established findings.

---

## 10. Preliminary Comparison Matrix

| Research tradition | Primary emphasis | Strong overlap with HACS | HACS proposed additional emphasis |
|---|---|---|---|
| Human-Centered AI | Human values, control, safe and beneficial AI | Agency, governance, responsibility | Longitudinal preservation of these properties |
| Human–AI Teaming | Effective human–AI team processes and performance | Coordination, trust, shared cognition, team metrics | Persistent state across sessions, transitions and handovers |
| Joint Cognitive Systems | Performance of the combined human–machine system | System as unit of analysis | Explicit continuity/provenance/recovery architecture |
| Distributed Cognition | Cognition across people, artifacts and environment | Distributed system perspective | AI-specific longitudinal governance and continuity |
| Hybrid Intelligence | Complementary human + machine capability | Collaborative Intelligence | Collaboration quality beyond joint performance |
| Trust Calibration | Appropriate reliance relative to system reliability | Calibrated trust | Calibration across changing longitudinal context |
| Agentic AI | Autonomous planning and action | AI capability inside collaborative workflows | Governance of persistent human–agent collaboration |

---

## 11. The Current Research Gap

The defensible gap is narrower than saying that existing AI research ignores collaboration.

A better hypothesis is:

> Existing fields contain many of the components required for durable human–AI collaboration, but these components are often studied under different units of analysis, time horizons, and evaluation objectives. HACS investigates whether treating continuity, provenance, human agency, trust calibration, governance, and recovery as jointly persistent properties of one evolving collaborative system yields a useful architecture and evaluation framework.

This formulation is intentionally falsifiable.

If existing frameworks already capture these requirements adequately, HACS should converge with them rather than manufacture novelty through terminology.

If important gaps remain, those gaps should become visible through systematic comparison and empirical testing.

---

## 12. Novelty Standard for v1.1.0

Before v1.1.0 makes a strong novelty claim, the project should be able to answer four questions:

1. Which HACS constructs already exist under different names in prior literature?
2. Which constructs are combinations or extensions of established work?
3. Which constructs, if any, are meaningfully new and operationally distinguishable?
4. Does the integrated HACS framework predict or improve outcomes that existing approaches do not?

Until these questions are answered, the preferred wording is:

> **HACS is a proposed integrative framework for studying enduring human–AI collaboration.**

That statement is strong enough to define a research program and cautious enough to remain scientifically defensible.

---

## 13. Initial Reference Set

The v1.1.0 bibliography should at minimum incorporate and verify primary sources covering:

- National Academies of Sciences, Engineering, and Medicine (2022), *Human-AI Teaming: State-of-the-Art and Research Needs*, DOI: 10.17226/26355.
- Human-Centered AI literature on balancing automation with human control and responsibility.
- Human–AI Joint Cognitive Systems / Joint Cognitive Systems literature.
- Edwin Hutchins's work on distributed cognition, including *Cognition in the Wild*.
- Hybrid Intelligence literature on complementary human–machine intelligence.
- Adaptive and dynamic trust-calibration research in human–AI collaboration.
- Contemporary research on AI agents and agentic systems, particularly human oversight, delegation, and governance.

A systematic literature review remains a future requirement; this document is a positioning map for the v1.1.0 development line, not a substitute for that review.
