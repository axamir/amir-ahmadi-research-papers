from dataclasses import dataclass, field
from enum import Enum
from typing import List


class DecisionState(str, Enum):
    ACTIVE = "ACTIVE"
    WARNING = "WARNING"
    RESTRICTED = "RESTRICTED"
    PAUSED = "PAUSED"
    TERMINATED = "TERMINATED"


@dataclass
class Thresholds:
    warning_deviation: float = 0.10
    restricted_deviation: float = 0.20
    pause_deviation: float = 0.30
    terminate_deviation: float = 0.45
    stakeholder_floor: float = 0.55
    risk_warning: float = 0.45
    risk_pause: float = 0.70


@dataclass
class Observation:
    outcome_score: float
    stakeholder_score: float
    risk_score: float
    note: str = ""


@dataclass
class Decision:
    decision_id: str
    expected_outcome: float = 1.0
    authority_level: float = 1.0
    reputation: float = 1.0
    state: DecisionState = DecisionState.ACTIVE
    thresholds: Thresholds = field(default_factory=Thresholds)
    history: List[Observation] = field(default_factory=list)

    def review(self, observation: Observation) -> DecisionState:
        self.history.append(observation)
        deviation = abs(self.expected_outcome - observation.outcome_score)
        t = self.thresholds

        # Hidden-harm safeguard: business outcome alone cannot keep a decision ACTIVE.
        if observation.stakeholder_score < t.stakeholder_floor:
            deviation = max(deviation, t.restricted_deviation)

        if observation.risk_score >= t.risk_pause or deviation >= t.terminate_deviation:
            self._restrict(0.0, 0.20)
            self.state = DecisionState.TERMINATED
        elif deviation >= t.pause_deviation:
            self._restrict(0.25, 0.12)
            self.state = DecisionState.PAUSED
        elif deviation >= t.restricted_deviation or observation.risk_score >= t.risk_warning:
            self._restrict(0.50, 0.08)
            self.state = DecisionState.RESTRICTED
        elif deviation >= t.warning_deviation:
            self._restrict(0.80, 0.03)
            self.state = DecisionState.WARNING
        else:
            self.authority_level = min(1.0, self.authority_level + 0.03)
            self.reputation = min(1.0, self.reputation + 0.01)
            self.state = DecisionState.ACTIVE

        return self.state

    def _restrict(self, authority_cap: float, reputation_penalty: float) -> None:
        self.authority_level = min(self.authority_level, authority_cap)
        self.reputation = max(0.0, self.reputation - reputation_penalty)


def demo() -> None:
    decision = Decision(decision_id="LDG-DEMO-001")
    observations = [
        Observation(1.02, 0.82, 0.18, "healthy start"),
        Observation(1.08, 0.76, 0.24, "business growth"),
        Observation(1.10, 0.50, 0.28, "hidden stakeholder harm emerges"),
        Observation(0.78, 0.48, 0.52, "continued divergence"),
        Observation(0.62, 0.44, 0.74, "emergency risk"),
    ]

    for i, obs in enumerate(observations, start=1):
        state = decision.review(obs)
        print(
            f"cycle={i} state={state.value} "
            f"authority={decision.authority_level:.2f} "
            f"reputation={decision.reputation:.2f} "
            f"outcome={obs.outcome_score:.2f} "
            f"stakeholder={obs.stakeholder_score:.2f} "
            f"risk={obs.risk_score:.2f} note={obs.note}"
        )


if __name__ == "__main__":
    demo()
