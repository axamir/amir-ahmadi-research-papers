"""Living Decision Governance (LDG) v0.2 reference model.

This is an executable research model, not a production governance system.
It encodes the paper's core claims as inspectable state transitions using only
Python's standard library.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from enum import Enum
from statistics import fmean
from typing import Dict, List, Optional
import json


class DecisionState(str, Enum):
    PROPOSED = "PROPOSED"
    ACTIVE = "ACTIVE"
    WARNING = "WARNING"
    RESTRICTED = "RESTRICTED"
    PAUSED = "PAUSED"
    TERMINATED = "TERMINATED"


@dataclass
class Thresholds:
    warning_deviation: float = 0.10
    restrict_deviation: float = 0.20
    pause_deviation: float = 0.30
    terminate_deviation: float = 0.45
    stakeholder_floor: float = 0.60
    risk_warning: float = 0.45
    risk_pause: float = 0.70
    risk_terminate: float = 0.88
    min_collective_confidence: float = 0.60


@dataclass
class StakeholderSignal:
    group: str
    score: float
    weight: float = 1.0
    evidence_strength: float = 0.5
    note: str = ""

    def weighted_score(self) -> float:
        return self.score * self.weight * max(0.1, self.evidence_strength)

    def effective_weight(self) -> float:
        return self.weight * max(0.1, self.evidence_strength)


@dataclass
class AgentReview:
    agent_id: str
    confidence: float
    risk_score: float
    recommendation: str
    assumptions: List[str] = field(default_factory=list)
    challenge: Optional[str] = None


@dataclass
class HumanSignature:
    signer_id: str
    role: str
    decision: str  # APPROVE / MODIFY / REJECT / ABSTAIN
    confidence: float
    rationale: str


@dataclass
class Observation:
    cycle: int
    outcome_score: float
    risk_score: float
    stakeholder_signals: List[StakeholderSignal]
    note: str = ""

    @property
    def stakeholder_score(self) -> float:
        total_weight = sum(x.effective_weight() for x in self.stakeholder_signals)
        if total_weight == 0:
            return 0.5
        return sum(x.weighted_score() for x in self.stakeholder_signals) / total_weight


@dataclass
class Decision:
    decision_id: str
    question: str
    expected_outcome: float = 1.0
    thresholds: Thresholds = field(default_factory=Thresholds)
    state: DecisionState = DecisionState.PROPOSED
    authority_level: float = 1.0
    reputation: Dict[str, float] = field(default_factory=dict)
    agent_reviews: List[AgentReview] = field(default_factory=list)
    signatures: List[HumanSignature] = field(default_factory=list)
    history: List[Observation] = field(default_factory=list)
    audit_log: List[str] = field(default_factory=list)

    def add_agent_review(self, review: AgentReview) -> None:
        self.agent_reviews.append(review)
        self.audit_log.append(
            f"AGENT_REVIEW {review.agent_id} confidence={review.confidence:.2f} "
            f"risk={review.risk_score:.2f} recommendation={review.recommendation}"
        )

    def sign(self, signature: HumanSignature) -> None:
        self.signatures.append(signature)
        self.reputation.setdefault(signature.signer_id, 0.75)
        self.audit_log.append(
            f"HUMAN_SIGN {signature.signer_id} role={signature.role} "
            f"decision={signature.decision} confidence={signature.confidence:.2f}"
        )

    def collective_confidence(self) -> float:
        human = [s.confidence for s in self.signatures if s.decision == "APPROVE"]
        agents = [r.confidence for r in self.agent_reviews if r.recommendation == "APPROVE"]
        values = human + agents
        return fmean(values) if values else 0.0

    def activate(self) -> DecisionState:
        if not any(s.decision == "APPROVE" for s in self.signatures):
            raise ValueError("At least one accountable human approval is required.")
        confidence = self.collective_confidence()
        if confidence < self.thresholds.min_collective_confidence:
            self.state = DecisionState.WARNING
            self.authority_level = min(self.authority_level, 0.70)
            self.audit_log.append(
                f"ACTIVATE_WARNING collective_confidence={confidence:.2f}"
            )
        else:
            self.state = DecisionState.ACTIVE
            self.audit_log.append(
                f"ACTIVATE collective_confidence={confidence:.2f}"
            )
        return self.state

    def review(self, obs: Observation) -> DecisionState:
        if self.state == DecisionState.TERMINATED:
            raise RuntimeError("A terminated decision cannot continue without a new decision object.")

        self.history.append(obs)
        t = self.thresholds
        outcome_deviation = abs(self.expected_outcome - obs.outcome_score)
        stakeholder_score = obs.stakeholder_score

        # Hidden-harm rule: strong business outcomes cannot mask stakeholder collapse.
        effective_deviation = outcome_deviation
        if stakeholder_score < t.stakeholder_floor:
            harm_gap = t.stakeholder_floor - stakeholder_score
            effective_deviation = max(
                effective_deviation,
                t.restrict_deviation + harm_gap,
            )

        # Risk can independently trigger escalation.
        if obs.risk_score >= t.risk_terminate or effective_deviation >= t.terminate_deviation:
            self._transition(DecisionState.TERMINATED, authority=0.0, penalty=0.20, obs=obs)
        elif obs.risk_score >= t.risk_pause or effective_deviation >= t.pause_deviation:
            self._transition(DecisionState.PAUSED, authority=0.20, penalty=0.12, obs=obs)
        elif obs.risk_score >= t.risk_warning or effective_deviation >= t.restrict_deviation:
            self._transition(DecisionState.RESTRICTED, authority=0.50, penalty=0.08, obs=obs)
        elif effective_deviation >= t.warning_deviation:
            self._transition(DecisionState.WARNING, authority=0.80, penalty=0.03, obs=obs)
        else:
            self.state = DecisionState.ACTIVE
            self.authority_level = min(1.0, self.authority_level + 0.05)
            self._reward_signers(0.01)
            self.audit_log.append(
                f"CYCLE {obs.cycle} ACTIVE outcome={obs.outcome_score:.2f} "
                f"stakeholder={stakeholder_score:.2f} risk={obs.risk_score:.2f}"
            )

        return self.state

    def _transition(
        self,
        state: DecisionState,
        authority: float,
        penalty: float,
        obs: Observation,
    ) -> None:
        self.state = state
        self.authority_level = min(self.authority_level, authority)
        self._penalize_signers(penalty)
        self.audit_log.append(
            f"CYCLE {obs.cycle} {state.value} outcome={obs.outcome_score:.2f} "
            f"stakeholder={obs.stakeholder_score:.2f} risk={obs.risk_score:.2f} "
            f"authority={self.authority_level:.2f}"
        )

    def _penalize_signers(self, penalty: float) -> None:
        for s in self.signatures:
            if s.decision == "APPROVE":
                current = self.reputation.get(s.signer_id, 0.75)
                self.reputation[s.signer_id] = max(0.0, current - penalty)

    def _reward_signers(self, reward: float) -> None:
        for s in self.signatures:
            if s.decision == "APPROVE":
                current = self.reputation.get(s.signer_id, 0.75)
                self.reputation[s.signer_id] = min(1.0, current + reward)

    def export(self) -> Dict[str, object]:
        return {
            "decision_id": self.decision_id,
            "question": self.question,
            "state": self.state.value,
            "authority_level": round(self.authority_level, 4),
            "reputation": {k: round(v, 4) for k, v in self.reputation.items()},
            "collective_confidence": round(self.collective_confidence(), 4),
            "agent_reviews": [asdict(x) for x in self.agent_reviews],
            "signatures": [asdict(x) for x in self.signatures],
            "history": [
                {
                    "cycle": x.cycle,
                    "outcome_score": x.outcome_score,
                    "risk_score": x.risk_score,
                    "stakeholder_score": round(x.stakeholder_score, 4),
                    "signals": [asdict(s) for s in x.stakeholder_signals],
                    "note": x.note,
                }
                for x in self.history
            ],
            "audit_log": list(self.audit_log),
        }


def demo() -> Decision:
    d = Decision(
        decision_id="LDG-DEMO-002",
        question="Deploy AI-assisted customer support across all customer tiers?",
    )
    d.add_agent_review(
        AgentReview(
            agent_id="ops-agent-v2",
            confidence=0.82,
            risk_score=0.28,
            recommendation="APPROVE",
            assumptions=["support volume stable", "human escalation remains available"],
        )
    )
    d.add_agent_review(
        AgentReview(
            agent_id="risk-agent-v3",
            confidence=0.74,
            risk_score=0.35,
            recommendation="APPROVE",
            challenge="Monitor employee trust and severe complaint rate independently of cost savings.",
        )
    )
    d.sign(
        HumanSignature(
            signer_id="manager-operations",
            role="Operations Director",
            decision="APPROVE",
            confidence=0.78,
            rationale="Benefits are material and rollback remains available.",
        )
    )
    d.sign(
        HumanSignature(
            signer_id="manager-quality",
            role="Quality Lead",
            decision="APPROVE",
            confidence=0.70,
            rationale="Approve with tight stakeholder and risk thresholds.",
        )
    )
    d.activate()

    cycles = [
        Observation(
            cycle=1,
            outcome_score=1.04,
            risk_score=0.18,
            stakeholder_signals=[
                StakeholderSignal("customers", 0.82, 1.0, 0.8),
                StakeholderSignal("employees", 0.74, 1.0, 0.8),
            ],
            note="healthy start",
        ),
        Observation(
            cycle=2,
            outcome_score=1.10,
            risk_score=0.25,
            stakeholder_signals=[
                StakeholderSignal("customers", 0.78, 1.0, 0.8),
                StakeholderSignal("employees", 0.54, 1.2, 0.9, "trust decline"),
            ],
            note="business performance improves while employee trust falls",
        ),
        Observation(
            cycle=3,
            outcome_score=0.86,
            risk_score=0.50,
            stakeholder_signals=[
                StakeholderSignal("customers", 0.68, 1.0, 0.9),
                StakeholderSignal("employees", 0.50, 1.2, 0.9),
            ],
            note="complaints and operational risk rise",
        ),
    ]

    for obs in cycles:
        d.review(obs)

    return d


if __name__ == "__main__":
    decision = demo()
    print(json.dumps(decision.export(), indent=2))
