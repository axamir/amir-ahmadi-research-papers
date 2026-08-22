# Evidence Index

This directory indexes the evidence preserved for the TCSAI / NeuroSapiens+ verification case study.

## Evidence classes

### E-A — Primary interface record

Preserved locally as original artifacts:

- Safari WebArchive of the NeuroSapiens+ chat page
- continuous screen recording of the primary interface session
- original sequential screenshots of the interface
- raw text transcript export
- a visual PDF derivative made from original screenshots
- a readable text PDF derivative made from the WebArchive

### E-B — LinkedIn context

Preserved locally as original artifacts:

- sequential screenshots of the direct-message exchange with Rafael Antonio (Tony) Cantero Suarez
- visual PDF derivative containing the screenshot sequence

### E-C — Browser/session replication

Preserved locally as original artifacts:

- Safari unauthenticated replication captures
- Chrome authenticated/fresh-profile replication captures
- exact prompts used for the replication tests

### E-D — Hash ledger

`hashes/SHA256SUMS.txt` records cryptographic hashes of key artifacts already captured. Hashing demonstrates integrity after capture; it does **not** by itself prove what an undisclosed remote backend generated before capture.

## Raw vs derivative

- **RAW** = original capture/export as produced by the browser or operating system.
- **DERIVATIVE** = PDF, crop, transcription, annotation, or other human-readable representation produced from a raw artifact.

A derivative must never be represented as the primary raw record.

## Provenance limitation

Client-side screenshots, recordings, HTML/WebArchives, and hashes cannot make local manipulation logically impossible. The study therefore does not ask readers to trust these captures alone. The exact prompts and replication protocol are disclosed so independent observers can reproduce the public-interface tests themselves.

## Publication principle

> These records document what the tested interface displayed under the described conditions. They do not, by themselves, establish the implementation of an undisclosed backend.

## Binary upload status

The repository dossier is being prepared in stages. Textual research records and cryptographic manifests are committed first. Large binary originals (continuous video, full screenshot archives, WebArchive, and visual PDFs) are preserved outside Git history until uploaded through a binary-appropriate route (Git LFS, release assets, or an archival deposit). Once deposited, immutable links and hashes will be added here.
