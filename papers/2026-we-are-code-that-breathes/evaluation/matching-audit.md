# Condition P / Condition C Matching Audit v0.1

**Purpose:** determine whether the first PRCEP evaluation stimuli are fair enough for pilot use.  
**Materials audited:** `condition-p.md` and `condition-c.md`  
**Decision:** **pilot-ready with explicit caveats; not yet confirmatory-study-ready.**

## 1. Experimental contrast

The intended manipulation is **representation structure**, not substantive information.

- **P** exposes claim-transition roles explicitly: claim-before, intervention/source, decision/reason, claim-after, status and uncertainty.
- **C** presents the same research trajectory as ordinary continuous prose and does not label those transition roles.

A valid comparison therefore requires C to retain the facts needed to answer the instrument. It must not be a deliberately degraded summary.

## 2. Information-unit parity

Manual semantic audit shows both packets contain the following core units:

| Information unit | P | C |
|---|:---:|:---:|
| originating question/metaphor | ✓ | ✓ |
| metaphor is non-literal/current boundary | ✓ | ✓ |
| PRCEP is a protocol candidate, not validated | ✓ | ✓ |
| early DNA/experience formulation | ✓ | ✓ |
| Johan correction | ✓ | ✓ |
| sequence vs regulation/epigenetics/plasticity distinction | ✓ | ✓ |
| Pete/Turing historical intervention | ✓ | ✓ |
| formal/theoretical vs physical-computer distinction | ✓ | ✓ |
| Igor prior-art intervention | ✓ | ✓ |
| literature-audit narrowing | ✓ | ✓ |
| interaction-centered intelligence not claimed novel | ✓ | ✓ |
| narrower provenance/reconstruction contribution | ✓ | ✓ |
| earlier author-side continuity/provenance records | ✓ | ✓ |
| Eric/SCQOS independent convergence | ✓ | ✓ |
| similarity does not prove lineage | ✓ | ✓ |
| public discussion is not peer review | ✓ | ✓ |
| participation does not imply co-authorship/endorsement | ✓ | ✓ |
| relational/trajectory idea remains hypothesis | ✓ | ✓ |
| matched-information falsification condition | ✓ | ✓ |
| unresolved compressed contribution | ✓ | ✓ |
| insufficient evidence remains insufficient | ✓ | ✓ |
| material generative-AI workflow roles | ✓ | ✓ |
| model output is not independent evidence | ✓ | ✓ |
| human decision responsibility | ✓ | ✓ |
| unknown historical model configuration remains unknown | ✓ | ✓ |
| quotation-verification boundary | ✓ | ✓ |
| Git ≠ complete intellectual provenance | ✓ | ✓ |
| next step is independent matched-information evaluation | ✓ | ✓ |
| negative/null result is valid | ✓ | ✓ |
| cost can justify simplification/rejection | ✓ | ✓ |

**Finding:** no core gold-standard information unit is intentionally absent from C.

## 3. Structural asymmetry — intended

P contains explicit labels such as `Claim-before`, `Intervention/source`, `Decision`, `Reason`, `Claim-after`, `Status-after`, `Remaining uncertainty`, and `Falsification`. C does not.

This is the treatment itself and must not be “balanced away.” If those labels are removed from P, the experiment no longer tests explicit transition representation.

## 4. Structural asymmetry — possible confounds

P is visually chunked into six named transitions plus separate semantic-uncertainty, model-mediation, evidence and evaluation sections. C uses thematic paragraphs. Consequently, P may benefit from:

1. **navigation/chunking** independent of provenance semantics;
2. **label cueing** that maps directly onto some evaluation questions;
3. **greater repetition** of status/decision vocabulary;
4. **more explicit temporal directionality** (`before`/`after`).

These are not necessarily defects: some may be mechanisms through which PRCEP improves reconstruction. But the first experiment cannot distinguish semantic provenance structure from generic formatting/chunking benefits.

## 5. Instrument leakage audit

The evaluation instrument asks directly about predecessor/successor positions, causes of transition, attribution, current status, model mediation and uncertainty. P uses vocabulary that closely mirrors these tasks. This creates a legitimate but potentially strong treatment cue.

For a confirmatory study, add a second control:

- **C2 — structure-matched non-PRCEP control:** same headings/chunking/visual segmentation as P, but without explicit provenance relation labels or transition semantics.

Recommended future three-arm design:

- **P:** PRCEP semantic structure + chunking;
- **C1:** information-matched continuous prose;
- **C2:** information-matched and layout/chunking-matched, but provenance semantics removed.

P > C1 would test the complete usable representation package. P > C2 would more specifically test PRCEP's semantic transition structure.

## 6. Source parity

Both packets identify the same named intervention sources required by the current gold standard: Johan M. Lammens, Pete Howard, Igor Alexei Balanovski and Eric Robles. Both also identify literature audit, earlier author-side repository evidence, generative-AI mediation and the public thread as relevant source classes.

No additional external authority should be added to only one condition.

## 7. Claim-strength parity

Both packets preserve the same epistemic boundaries:

- metaphor ≠ literal mechanism;
- PRCEP candidate ≠ validated protocol;
- relational/trajectory proposition = hypothesis;
- public discussion ≠ peer review;
- independent convergence ≠ derivation;
- AI mediation ≠ independent evidence;
- Git versioning ≠ complete intellectual provenance;
- unresolved evidence ≠ definite interpretation.

**Finding:** no obvious claim-strength upgrade was found in C relative to P or vice versa.

## 8. Length/readability requirement

Exact word count and standardized readability should be computed from the frozen files in the actual study pipeline rather than estimated manually. Before confirmatory recruitment, record at minimum:

- Markdown-stripped word count;
- sentence count;
- mean sentence length;
- Flesch Reading Ease / Flesch-Kincaid Grade where applicable;
- heading count;
- paragraph count;
- number of explicit status/transition labels;
- named-source count;
- reading-time pilot distribution.

Do **not** force identical word counts by deleting substantive information. Prefer a prespecified tolerance (for example ±10%) and disclose residual differences.

## 9. Pilot decision

The current pair is suitable for a **small cognitive pilot** whose purpose is to detect ambiguity, ceiling/floor effects, obvious information mismatch and participant burden.

It is **not yet sufficient for a strong confirmatory claim** because generic chunking and PRCEP semantics are confounded in P versus C.

## 10. Freeze rule

For any actual participant wave:

1. assign immutable stimulus version IDs;
2. record commit SHAs/hashes;
3. freeze the gold standard before scoring;
4. do not silently edit either condition mid-wave;
5. if a defect requires correction, close the wave, version the stimuli and report the change.

## 11. Next required artifact

Create **Condition C2**, a structure-matched control, then run an automated descriptive parity report over P/C1/C2. Only after that should the package be labeled `evaluation-ready v0.1`.

---

**Audit conclusion:** substantive information parity is strong enough for pilot use. The major remaining threat is **format/chunking confounding**, not missing scientific content.