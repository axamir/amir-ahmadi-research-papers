# Provenance & Claim-Evolution Gap Audit

**Document:** ARP-WCB-2026-01  
**Audit date:** 2026-08-14  
**Purpose:** test the project's candidate novelty against established provenance, belief-revision, scientific-claim, and recent Human–AI interaction frameworks before manuscript drafting.

## Executive result

The audit narrows the novelty claim substantially.

This project **must not claim novelty** for:

- representing provenance through entities, activities, agents, derivation, attribution, revision, and influence;
- representing an atomic scientific assertion together with provenance and publication metadata;
- representing claim/evidence networks or scientific facts as socially revised over time;
- formal belief revision as addition, removal, and consistency-preserving change;
- treating interaction as a primary unit of analysis in Human–AI co-creation;
- treating long-term Human–AI interaction as a coevolving or self-organizing system;
- treating Human–AI collaboration as an epistemic partnership involving negotiated authority, agency, accountability, and calibration.

The strongest remaining candidate contribution is narrower:

> **A versioned research protocol and public case record for tracking how claims in persistent Human↔Generative-AI collaboration are proposed, challenged, corrected, attributed, revised, rejected, and stabilized across model-mediated drafting and heterogeneous public adversarial input—while preserving enough provenance to reconstruct not merely the final claim, but the transformation path and the independence of participating lineages.**

This remains a candidate contribution, not a proven novelty claim.

---

## 1. W3C PROV: provenance is already a mature formal problem

The W3C PROV family defines a domain-agnostic provenance model centered on **Entities**, **Activities**, and **Agents**. It includes relations for generation, usage, derivation, revision, attribution, association, communication, and influence.

### Consequence for this project

Our terms `claim`, `comment`, `draft`, `revision`, `participant`, `model`, `public post`, and `paper version` should not be treated as if provenance modeling begins here. PRTM should instead be designed as an **application profile / research layer compatible in spirit with PROV**, unless a technical reason for incompatibility is demonstrated.

### Candidate mapping

| ARP-WCB object | PROV-compatible interpretation |
|---|---|
| Original post / comment / claim version / manuscript version | Entity |
| Drafting / commenting / correcting / synthesizing / publishing | Activity |
| Amir / public contributor / software-model role | Agent, with careful responsibility semantics |
| New claim version from earlier claim | wasDerivedFrom / revision-like relation |
| Quotation | quotation/derivation relation |
| Contributor responsibility for public comment | attribution |
| Model participation in drafting activity | association with activity; does not by itself imply authorship or moral agency |
| Comment changing manuscript direction | influence + explicit project-specific relation |

### Important boundary

PROV can record that one entity was influenced by or derived from another. It does **not automatically decide intellectual priority, truth, consent, authorship, or scientific validity**. Those remain separate governance/epistemic layers.

---

## 2. Nanopublications: assertion + provenance is not new

Nanopublications represent small, citable, machine-interpretable assertions together with provenance and publication information. Recent provenance-driven extensions also address **multi-source assertions**, including supporting and conflicting evidence.

### Consequence

Our `claim-source-matrix.md` is useful operationally, but the general idea of binding individual claims to provenance is established prior art.

### Remaining opportunity

The project may differ in treating **claim transformation itself** as a first-class longitudinal object:

```text
C0 proposed
 -> challenged by P1
 -> corrected into C1
 -> compared with prior art L1
 -> challenged by P2
 -> narrowed into C2
 -> tested under ablation
 -> retained/rejected
```

The possible contribution is not “claims have provenance,” but a research protocol that preserves **trajectory + intervention + revision reason + contributor independence + model mediation** in one inspectable artifact.

---

## 3. Micropublications and claim/evidence networks

Micropublication work explicitly models claims, evidence, arguments, annotations, and the fact that scientific assertions become accepted through a social process involving uncertainty, controversy, reassessment, and convergence.

### Consequence

We cannot present “a claim changes through public criticism” as a new theory of science.

### Difference worth testing

Our case involves a hybrid production environment:

- one persistent human researcher;
- one or more generative-model configurations;
- prior longitudinal human–AI records;
- public heterogeneous contributors;
- Git-versioned synthesis;
- explicit separation of contributor claim from author adoption;
- model-assisted transformation of responses into a later manuscript.

The research question becomes whether this hybrid environment creates provenance problems insufficiently captured by article-centered claim/evidence models—not whether scientific claims have social histories.

---

## 4. Belief revision: correction state machines have deep prior art

AGM and subsequent belief-revision research formalize expansion, contraction, revision, consistency, recovery, and repeated change in belief states/bases.

### Consequence

Our state sequence:

`PROPOSED → CHALLENGED → REFINED → CORRECTED / RETAINED / REJECTED`

is **not itself a novel formal theory of belief revision**.

### Distinction

The ARP-WCB state machine is better described as a **research-record workflow** rather than a replacement for AGM-style epistemic logic. If formal semantics are later claimed, they must be compared directly with belief-revision literature.

---

## 5. Interaction-centered intelligence: our broad relational thesis is already occupied

Nicholas Davis (2026) explicitly proposes **interaction as the primary unit of analysis** for Human–AI co-creation and emphasizes interaction trajectories, coordination patterns, adaptive regulation, and interactional drift.

### Consequence

The statement:

> “Maybe the next state of intelligence is not M3. Maybe it is the relation between the states.”

can remain an important independently reached formulation in the historical discussion record, but the final paper must **not present the general interaction-as-unit-of-analysis idea as novel**.

### Research opportunity

Our narrower object is not “interaction-centered intelligence” in general. It is **epistemic claim transformation with reconstructable provenance inside a persistent Human↔AI/public loop**.

---

## 6. Human–AI Coevolution Dynamics: long-term coupled interaction is also occupied

Recent HACD-H work models long-term Human–AI interaction as a self-organizing social cognitive system with memory, relational organization, adaptation, and multi-timescale dynamics.

### Consequence

We cannot claim novelty merely for:

- long-term Human–AI interaction;
- coevolution;
- relational attractors;
- multi-timescale adaptation;
- emergent social intelligence from repeated interaction.

### Difference

ARP-WCB is presently **not a theory of social intelligence**. Its narrower target is the provenance and epistemic evolution of research claims under persistent interaction.

---

## 7. Human–AI Epistemic Partnership: epistemic collaboration is occupied

Recent Human–AI Epistemic Partnership work treats GenAI as participating in knowledge construction and frames repeated interaction through negotiated epistemic authority, agency, accountability, and calibration cycles.

### Consequence

We cannot claim novelty for the basic idea that Human and GenAI can form an epistemic partnership or that authority/trust are renegotiated over time.

### Difference

ARP-WCB asks a more documentary/forensic question:

> Can the history of a research claim remain inspectable enough that a reader can reconstruct who introduced what, what the model mediated, which criticism caused revision, which lineage remained independent, and why the final statement differs from the original?

---

## 8. Revised novelty hierarchy

### Level A — not novel

- relation matters;
- interaction can be a unit of analysis;
- cognition can be distributed/extended/enactive;
- Human–AI interaction can coevolve;
- claims have provenance;
- beliefs/claims can be revised;
- scientific facts have social/evidential histories.

### Level B — potentially distinctive combination, but not yet demonstrated as novel

- longitudinal Human↔GenAI research interaction;
- public adversarial intervention;
- model-mediated author response;
- explicit contributor-independence ledger;
- claim-level revision reasons;
- Git-versioned evidence record;
- formal ablations designed to distinguish trajectory effects from information-volume effects.

### Level C — strongest candidate contribution

A **Provenance-Preserving Relational Claim Evolution Protocol** for hybrid Human–GenAI/public research workflows, with:

1. claim identity across revisions;
2. source/agent/activity lineage;
3. challenge and correction events;
4. adoption versus non-adoption;
5. uncertainty state;
6. contributor independence;
7. model mediation disclosure;
8. versioned artifacts;
9. falsification/ablation tests;
10. reconstructable reasons for transition.

Working name:

**PRCEP — Provenance-Preserving Relational Claim Evolution Protocol**

PRCEP is not yet asserted as a new standard. It is the protocol instantiated by this case study and must be compared against PROV, nanopublication/micropublication models, argumentation systems, and AI provenance work before stronger claims.

---

## 9. Revised research questions

### RQ1 — Reconstruction
Can an external reader reconstruct the transformation of a claim from the final artifact without relying on the author’s memory?

### RQ2 — Attribution
Can the record distinguish **introduced by**, **influenced by**, **quoted from**, **independently convergent with**, **adopted from**, and **rejected after**?

### RQ3 — Model mediation
Can the record distinguish what a human participant asserted from what a generative model helped formulate, summarize, compare, or synthesize?

### RQ4 — Trajectory effect
Does preserving ordered interaction history improve later claim quality, calibration, or reconstructability beyond simply providing the same information as an unordered bundle?

### RQ5 — Correction integrity
Can a corrected claim retain visible lineage to the inaccurate version without continuing to propagate the inaccurate wording as current truth?

### RQ6 — Independence
Can two independently developed frameworks be compared and allowed to converge conceptually without collapsing provenance or creating false priority claims?

### RQ7 — Public input
What kinds of public contribution materially change a thesis—correction, prior art, counterexample, formalization, reframing, implementation claim—and how should each be represented?

---

## 10. Manuscript consequence

The paper should now be framed less as:

> **A new theory of intelligence emerging between Human and AI**

and more as:

> **A provenance-preserving case study and protocol for the evolution of research claims inside persistent Human–Generative-AI collaboration under public adversarial input.**

The original philosophical question remains valuable as the **event that generated the dataset**. It no longer needs to carry the full novelty burden.

## 11. Strongest methodological principle after audit

> **The paper should be able to show not only what it believes now, but why it no longer says what it said at the beginning.**

That property is the heart of the artifact.