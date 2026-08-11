# LDG Specification v0.1

## Decision object

A governed decision is modeled as a stateful object with at least:

- `decision_id`
- `title`
- `owner`
- `state`
- `authority_level`
- `expected_outcome`
- `warning_threshold`
- `emergency_threshold`
- `stop_threshold`
- `review_interval`
- `human_signatories`
- `agent_reviews`
- `stakeholder_groups`
- `outcome_history`
- `stakeholder_history`
- `risk_history`
- `reputation_impact`

## State machine

```text
PROPOSED
  ↓ verification + human signature
VERIFIED
  ↓ collective ratification
ACTIVE
  ↓ moderate deviation
WARNING
  ↓ sustained deviation / elevated risk
RESTRICTED
  ↓ unresolved or severe risk
PAUSED
  ↓ unacceptable / persistent risk
TERMINATED
```

Recovery paths may return a decision from WARNING/RESTRICTED/PAUSED to ACTIVE only after predefined conditions and new approval.

## Review rule

Every material review cycle evaluates:

1. Business/mission outcome trend
2. Stakeholder trend
3. Risk trend
4. Deviation from expected trajectory
5. Agent disagreement
6. Human dissent
7. New evidence
8. Whether current authority remains justified

## Dissent rule

A dissenting reviewer may trigger re-evaluation when the dissent contains at least one of:

- a testable hypothesis,
- a missing variable,
- an evidence contradiction,
- a new constraint,
- or an explicit alternative.

Unstructured criticism is retained as a stakeholder signal but does not automatically block execution.

## Authority adaptation

Possible actions:

- `EXPAND`
- `MAINTAIN`
- `RESTRICT`
- `REQUIRE_MORE_SIGNATURES`
- `PAUSE`
- `TERMINATE`

Authority changes must be logged with rationale.

## Accountability record

Every consequential agent recommendation should preserve:

- agent/model identifier and version,
- evidence inputs,
- assumptions,
- confidence/uncertainty,
- recommendation,
- alternatives,
- timestamp,
- verifying actor,
- human signatory,
- final governance outcome.

## Non-goals

LDG v0.1 does not define:

- a legally binding DAO structure,
- cryptographic identity requirements,
- a universal reputation formula,
- production-grade model validation,
- or sector-specific regulatory compliance.

These remain future research areas.
