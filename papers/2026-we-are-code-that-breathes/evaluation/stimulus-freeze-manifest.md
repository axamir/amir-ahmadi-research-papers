# PRCEP Stimulus Freeze Manifest

**Study family:** PRCEP-EVAL-01  
**Freeze stage:** pilot input v0.1  
**Purpose:** bind pilot interpretation to exact repository artifacts rather than mutable filenames alone.

## Pilot stimuli

| Neutral role | Repository artifact | Blob SHA | Experimental function |
|---|---|---|---|
| Packet A candidate | `condition-p.md` | `0b78b128349787a8af22e9eb0a82bdbd07887546` | substantive information + chunking + explicit PRCEP transition semantics |
| Packet B candidate | `condition-c.md` | `246eb3fef6c68b2d91d2761dd75b38ef26043c29` | conventional-prose matched-information control |
| Packet C candidate | `condition-c2.md` | `80f0c1c23a9cc0211544b2a7da73a2a7313f1c64` | structured/chunked control without explicit PRCEP transition semantics |

Neutral participant-facing labels must be randomized or remapped; the table above is an internal manifest and should not be shown before task completion.

## Evaluation artifacts

The pilot must also bind to the then-current versions of:

- `questions.md`
- `gold-standard.md` — GS-0.1
- `scoring-rubric.md`
- `pilot-protocol.md` — PP-0.1
- `matching-audit.md`
- `parity_audit.py`

Before actual recruitment, record the blob SHA for each of these artifacts in a pilot-run manifest. If any artifact changes, increment the pilot material version and preserve the old hash set.

## Freeze semantics

This manifest does **not** declare the stimuli confirmatory-final. It freezes the exact inputs to the design pilot so that later balancing edits can be reconstructed.

A confirmatory freeze requires a new manifest after:

1. automated parity metrics are generated;
2. human information-unit audit is completed;
3. pilot comprehension/scoring diagnostics are reviewed;
4. SPME and cost threshold are specified;
5. sample-size rationale and statistical model are frozen;
6. preregistration status changes from draft to final.

## Mutation rule

Never overwrite the interpretation of a previous pilot by silently editing a stimulus. Repository history preserves file versions, but each pilot/report should cite an explicit blob SHA or commit SHA.

**Manifest:** SFM-PILOT-0.1