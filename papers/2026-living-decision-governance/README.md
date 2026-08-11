# Living Decision Governance (LDG)

**Status:** Public Working Paper v0.1.0  
**Author:** Amir Ahmadi  
**Affiliation:** Independent Researcher  
**Year:** 2026

## Working thesis

Living Decision Governance (LDG) treats high-impact human–AI decisions as governed, continuously monitored objects rather than one-time approvals.

The framework proposes a closed-loop lifecycle:

```text
Propose → Challenge → Verify → Human Sign → Collective Ratification
→ Execute → Observe → Stakeholder Feedback → Re-score
→ Slow / Restrict / Pause / Stop / Expand Authority → Learn
```

## Research trigger

The inquiry was triggered by a public observation from Christopher J. Skinner about a blind spot in enterprise AI: systems can increasingly represent transactions, documents, workflows, and code, while still struggling to represent human thinking, communication, decision quality, and leadership.

LDG takes that observation as a starting question rather than as evidence for the framework itself:

> What if the missing layer is not only better representation of the decision-maker, but continuous governance of the decision after it enters the world?

## Repository contents

- `paper.en.md` — English working paper
- `specification.md` — executable conceptual specification
- `src/ldg.py` — reference Python simulation
- `tests/test_ldg.py` — basic behavior tests
- `machine-readable/verification-protocol.json` — machine-readable claims and checks
- `machine-readable/AI-README.md` — instructions for AI-assisted review and falsification
- `website/index.html` — standalone landing page
- `CITATION.cff` — citation metadata

## Scope

LDG is a conceptual and executable research artifact. It is **not** presented as a validated governance standard, a production safety system, or evidence that any specific organization should deploy DAO-style governance. The executable model is intentionally small and exists to make assumptions inspectable and testable.

## Core design principles

1. **Decision lifecycle, not decision event** — every consequential decision remains observable after deployment.
2. **Human accountability** — AI recommendations do not erase human responsibility; accountable reviewers sign judgments.
3. **Collective review** — high-impact decisions can aggregate multiple qualified perspectives rather than depend on a single authority.
4. **Adaptive authority** — authority can expand, contract, pause, or terminate based on measured outcomes.
5. **Thresholds from the start** — warning, emergency, slowdown, suspension, and stop conditions are defined before execution.
6. **Stakeholder sensing** — employees, customers, partners, and other affected groups contribute signals to the monitoring loop.
7. **Critique as signal** — criticism without a proposed remedy should not disappear; it can remain a lower-confidence signal, while evidence-backed and proposal-backed critique receives greater decision weight.
8. **No infinite certainty search** — disagreement must introduce a testable hypothesis or missing variable; systems need explicit stopping rules.

## License

Unless superseded by a repository-level license, text is intended for CC BY 4.0 publication. Code is provided as a research reference implementation and should be reviewed before reuse.
