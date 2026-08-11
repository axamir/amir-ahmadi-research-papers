"""Concrete LDG scenario: AI-assisted customer support transformation.

Run from repository root:
    python papers/2026-living-decision-governance/examples/customer_support_demo.py
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ldg_v02 import demo  # noqa: E402


def main() -> None:
    decision = demo()
    print("\nLDG CUSTOMER SUPPORT DEMO")
    print("=" * 64)
    print(f"Decision: {decision.question}")
    print(f"Final state: {decision.state.value}")
    print(f"Authority level: {decision.authority_level:.2f}")
    print("Reputation:")
    for actor, score in sorted(decision.reputation.items()):
        print(f"  - {actor}: {score:.2f}")
    print("\nLifecycle:")
    for obs in decision.history:
        print(
            f"  cycle {obs.cycle}: outcome={obs.outcome_score:.2f}, "
            f"stakeholders={obs.stakeholder_score:.2f}, risk={obs.risk_score:.2f}"
        )
    print("\nAudit log:")
    for row in decision.audit_log:
        print(f"  {row}")


if __name__ == "__main__":
    main()
