# Evidence custody search log

**Date:** 22 August 2026  
**Purpose:** Locate the reported raw WebArchive, continuous screen recording, original PDF derivatives, and remaining screenshots before any public release.

## Scope searched

The accessible `/Users/x/Documents/Codex` workspace was searched for `.webarchive`, `.mov`, `.mp4`, and `.pdf` artifacts. No file could be confidently identified as the reported NeuroSapiens+/TCSAI Safari WebArchive or continuous recording. Existing unrelated PDFs were not adopted into this case-study archive.

## Result after supplied artifacts

| Artifact | Result | Action |
|---|---|---|
| Safari WebArchive | Supplied after search. | Imported as RAW-001; hash matches the reported historic hash. |
| Continuous screen recording | Supplied after search. | Retained as RAW-002 in private local custody; Git-ignored because of size. |
| 42-page readable derivative PDF | Not supplied. | Deliberately excluded from release scope: it duplicates the archived source and the visual derivative. |
| 22-page visual-capture derivative PDF | Supplied after search. | Imported as DER-002; 22 pages confirmed visually; hash matches reported historic hash. |
| 20 original screenshots | Eight accessible originals imported and hashed; remaining 12 not located. | Eight exhibits retained as contextual excerpts. The remaining 12 are deliberately excluded from release scope because RAW-001 and RAW-002 preserve the primary record. |

## Integrity rule

This absence is not filled with substitutions, reconstructions, or similarly named files. Any later supplied artifact will receive a new custody ID, SHA-256 hash, byte size, source path/custodian, acquisition time, and relationship to the prior manifest.
