from src.ldg import Decision, DecisionState, Observation


def test_healthy_decision_stays_active():
    d = Decision("t1")
    state = d.review(Observation(1.02, 0.90, 0.10))
    assert state == DecisionState.ACTIVE


def test_hidden_stakeholder_harm_restricts_even_with_good_business_outcome():
    d = Decision("t2")
    state = d.review(Observation(1.08, 0.40, 0.20))
    assert state == DecisionState.RESTRICTED
    assert d.authority_level <= 0.50


def test_high_risk_terminates():
    d = Decision("t3")
    state = d.review(Observation(0.95, 0.80, 0.80))
    assert state == DecisionState.TERMINATED
    assert d.authority_level == 0.0
