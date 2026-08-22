# Publication readiness

## Release decision

**Current state: public, bounded research draft.** This release contains only the public-safe text record, the preserved exact prompt/output pair, methods, ledger, and correction protocol. It does not represent completion of independent replication or validation of any claimed mechanism.

## Completed

- English manuscript, chronology, test registry, reader protocol, data-freeze rule, claim–evidence ledger, right-of-reply standard, and human–AI disclosure.
- Eight accessible original screenshot exhibits imported as unedited PNGs with SHA-256 hashes.
- Exact primary telemetry prompt and paired response preserved.
- Great Library implementation-like self-description and operational follow-ups preserved.
- Public claims separated from evidence of mechanism.
- Public release uses no raw screenshots, PDF, WebArchive, recording, or unredacted private correspondence.

## Mandatory gates before public release

| Gate | Required completion criterion | Status |
|---|---|---|
| G-01 — raw custody | Import/custody-confirm the primary WebArchive, original recording, and at least one human-readable derivative; generate a fresh manifest and hashes. | Complete by scope decision: WebArchive, recording, and 22-page visual derivative are custodied and hashed. Remaining screenshots and the 42-page readable derivative are intentionally excluded as non-essential duplicates. |
| G-02 — quotation audit | Verify original LinkedIn post, all public-post wording/dates/URLs, Ashley comment, and Tony reply against full captures or independent archives. Remove any item not verified. | Applied to this release: no conditional public-post quotation is reproduced without a complete capture. |
| G-03 — privacy/redaction | Review each DM-derived exhibit. Use only necessary research excerpts; redact non-public personal data and remove unnecessary private conversation. | Complete at package level: a public-safe manifest excludes all raw/private artifacts. Any future public exhibit still requires manual redaction review. |
| G-04 — independent replication | At least one non-author runs T-02 in a separately documented environment and preserves raw artifacts/hashes. A second runner is strongly preferred. | Open |
| G-05 — adoption verification | Either obtain auditable analytics/audit evidence for adoption claims or retain them as unverified creator statements. | Open; publication can proceed only under the latter label if no evidence arrives. |
| G-06 — right of reply | Send the notice in `RIGHT-OF-REPLY.md`, set a reasonable deadline, and record the response/no-response without editing its substance. | Open correction protocol; no delivery or response is claimed in this release. |
| G-07 — release QA | Check every quote, URL, verdict label, artifact hash, and redaction; build a public-only evidence manifest. | Complete for this bounded release; later evidence requires a versioned correction. |

## Non-gates

Tony’s agreement, an admission, a finding of fraud, or validation by a model are **not** requirements for publication. Equally, no statement about unseen code, intent, or backend state may be introduced without direct evidence.

## Release conditions

Do not publish raw private correspondence or original captures by default. Later evidence, a response, independent replication, or any redacted exhibit must be released through a versioned correction.
