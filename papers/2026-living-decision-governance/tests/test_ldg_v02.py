from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ldg_v02 import (  # noqa: E402
    AgentReview,
    Decision,
    DecisionState,
    HumanSignature,
    Observation,
    StakeholderSignal,
)


def make_decision() -> Decision:
    d = Decision("TEST-001", "Deploy high-impact AI workflow?")
    d.add_agent_review(AgentReview("agent", 0.8, 0.2, "APPROVE"))
    d.sign(HumanSignature("manager", "Manager", "APPROVE", 0.8, "bounded pilot"))
    d.activate()
    return d


def test_human_signature_required():
    d = Decision("TEST-002", "Unsigned decision")
    d.add_agent_review(AgentReview("agent", 0.9, 0.1, "APPROVE"))
    try:
        d.activate()
        assert False, "activation should require a human signature"
    except ValueError:
        assert True


def test_healthy_cycle_remains_active():
    d = make_decision()
    state = d.review(
        Observation(
            1,
            outcome_score=1.03,
            risk_score=0.15,
            stakeholder_signals=[StakeholderSignal("employees", 0.78, evidence_strength=0.9)],
        )
    )
    assert state == DecisionState.ACTIVE
    assert d.authority_level == 1.0


def test_hidden_harm_restricts_even_when_outcome_is_good():
    d = make_decision()
    state = d.review(
        Observation(
            1,
            outcome_score=1.03,
            risk_score=0.20,
            stakeholder_signals=[StakeholderSignal("employees", 0.35, evidence_strength=1.0)],
        )
    )
    assert state in {DecisionState.RESTRICTED, DecisionState.PAUSED, DecisionState.TERMINATED}
    assert d.authority_level <= 0.50


def test_high_risk_can_pause_independently_of_business_outcome():
    d = make_decision()
    state = d.review(
        Observation(
            1,
            outcome_score=1.0,
            risk_score=0.75,
            stakeholder_signals=[StakeholderSignal("customers", 0.80, evidence_strength=1.0)],
        )
    )
    assert state == DecisionState.PAUSED
    assert d.authority_level <= 0.20


def test_terminated_decision_cannot_continue():
    d = make_decision()
    d.review(
        Observation(
            1,
            outcome_score=0.45,
            risk_score=0.92,
            stakeholder_signals=[StakeholderSignal("customers", 0.30, evidence_strength=1.0)],
        )
    )
    assert d.state == DecisionState.TERMINATED
    try:
        d.review(
            Observation(
                2,
                outcome_score=1.0,
                risk_score=0.1,
                stakeholder_signals=[StakeholderSignal("customers", 0.9)],
            )
        )
        assert False, "terminated decisions should require a new decision object"
    except RuntimeError:
        assert True
