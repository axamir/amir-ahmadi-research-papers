# PRCEP Operational Schema v0.1

PRCEP — Provenance-Preserving Relational Claim Evolution Protocol

## Scope
PRCEP is an application-level protocol for recording material claim evolution in hybrid Human–Generative-AI/public research workflows. It does not replace W3C PROV, belief-revision theory, argumentation models, or scholarly provenance standards.

## Core objects

### Claim
`claim_id`, `text`, `status`, `evidence_class`, `uncertainty`, `version_created`, `supersedes`

### Intervention
`intervention_id`, `actor_id`, `actor_type`, `intervention_type`, `content_reference`, `timestamp_or_order`, `verification_state`

### Transition
`transition_id`, `claim_before`, `intervention_id`, `decision`, `decision_reason`, `claim_after`, `uncertainty_after`, `artifact_version`

### Actor
Types: `human_author`, `public_contributor`, `generative_model`, `literature_source`, `external_system`.

### Artifact
`artifact_id`, `path_or_uri`, `version`, `content_hash_if_available`, `created_at`

## Intervention types
`correction`, `counterexample`, `prior_art`, `clarification`, `formalization`, `reframing`, `independent_convergence`, `implementation_claim`, `representation_critique`, `question`, `model_synthesis`, `model_translation`, `model_comparison`.

## Decision types
`accept`, `partially_accept`, `refine`, `correct`, `reject`, `record_without_adoption`, `defer_pending_evidence`.

## Lineage relations
PRCEP distinguishes `derived_from`, `adopted_from`, `influenced_by`, `quoted_from`, `independently_convergent_with`, `coauthored_with`, and `no_lineage_claim`.

Conceptual similarity alone is never sufficient evidence of lineage.

## Model mediation
Where a generative model materially participates, record the workflow function: drafting, summarization, translation, reframing, comparison, counterargument generation, literature-query formulation, synthesis, structural organization, or claim audit.

These labels describe workflow function, not consciousness, moral agency, authorship, or independent intellectual ownership.

## Minimal transition tuple

```text
T = (claim_before, intervention, source, independence,
     model_mediation, evidence_class, decision, reason,
     claim_after, uncertainty_after, artifact_version)
```

## Proposed reconstruction metrics

- **M1 Origin attribution accuracy:** can an evaluator identify who/what introduced a material proposition?
- **M2 Transition reconstruction accuracy:** can the evaluator explain why C0 became C1?
- **M3 Correction visibility:** can superseded claims be identified without confusing them with current claims?
- **M4 Independence discrimination:** can independent convergence be distinguished from adoption or derivation?
- **M5 Mediation transparency:** can material model assistance be located?
- **M6 Current-state fidelity:** can the evaluator identify what the manuscript claims now?
- **M7 Evidence-link completeness:** what fraction of material transitions point to inspectable evidence or an explicit unresolved marker?

## Evaluation design
Compare two representations of the same research trajectory:

- **Condition P:** manuscript + PRCEP record.
- **Condition F:** final manuscript + conventional references only.

Independent evaluators answer identical reconstruction questions. Additional controls must prevent a simple information-volume advantage from being mistaken for a provenance advantage.

## Integrity rules
1. Never silently overwrite a materially corrected claim.
2. Never convert public contribution into implied co-authorship.
3. Never infer common lineage from similar vocabulary.
4. Never promote model synthesis into independent evidence.
5. Never present unresolved external implementation claims as verified.
6. Preserve uncertainty when source evidence is incomplete.
7. Keep current claims distinguishable from historical predecessors.
8. Permit privacy/legal redaction while retaining a minimal audit marker where appropriate.

## Success criterion
PRCEP is useful only if a competent external reader can answer, with materially greater accuracy than from the final paper alone: **What changed, who or what caused the change, why was it accepted or rejected, and what does the project believe now?**