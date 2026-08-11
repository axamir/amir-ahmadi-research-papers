# Research Paper Source Audit

**Repository:** `axamir/amir-ahmadi-research-papers`  
**Audit status:** ✅ Launch-ready canonical source map  
**Last reviewed:** 2026-08-12  
**Purpose:** Define the canonical full-text Markdown source used by the Research Hub for each public paper, separately for English and Persian.

## Canonical source policy

The website is a reading and publication layer over the research archive, not a duplicate authoring layer. Every public article page is generated from one explicit canonical Markdown source. English pages render only English sources; Persian pages render only Persian sources. Draft fragments, historical revisions, READMEs, PDFs, diagrams, code and supporting artifacts remain accessible as provenance but cannot silently replace the canonical manuscript.

The build now fails if a registered canonical source is missing, contains placeholder text, or is implausibly short. This turns source integrity into a publication invariant rather than a manual convention.

## Canonical source map

| Paper | English canonical source | Persian canonical source | Audit status |
|---|---|---|---|
| Living Decision Governance | `papers/2026-living-decision-governance/LDG_COMPLETE.md` | `papers/2026-living-decision-governance/LDG_COMPLETE.fa.md` | ✅ Complete pair; executable artifacts are linked as supplements |
| Beyond Intelligence — AI Evolution | `papers/beyond-intelligence-ai-evolution/paper-en.md` | `papers/beyond-intelligence-ai-evolution/paper-fa.md` | ✅ Complete pair; visual assets remain supporting material |
| From Green Personalisation to Relational Co-Evolution | `papers/2026-relational-co-evolution/paper.en.md` | `papers/2026-relational-co-evolution/paper.fa.md` | ✅ Complete pair |
| Reflections and Their Owners | `papers/2026-reflections-and-their-owners/paper.md` | `papers/2026-reflections-and-their-owners/paper.fa.md` | ✅ Complete pair |
| From Stamp to Alliance | `papers/2026-from-stamp-to-alliance/paper.en.md` | `papers/2026-from-stamp-to-alliance/paper.fa.md` | ✅ Complete pair; PDFs are alternate formats |
| From Money to Pledge | `papers/2026-from-pledge-to-sovereignty/paper.en.md` | `papers/2026-from-pledge-to-sovereignty/paper.fa.md` | ✅ Complete pair; repository folder name differs from public title |
| I, You, and We | `papers/2026-human-ai-co-creation-manifesto/paper.en.md` | `papers/2026-human-ai-co-creation-manifesto/paper.fa.md` | ✅ Complete pair |
| Designing Rest | `papers/2026-designing-rest/paper.en.md` | `papers/2026-designing-rest/paper.fa.md` | ✅ Complete pair |
| Before the First Chapter | `papers/2026-before-the-first-chapter/paper.en.md` | `papers/2026-before-the-first-chapter/paper.fa.md` | ✅ Resolved — bilingual record restored; recovery provenance retained |
| From Genesis to Witness | `papers/2026-from-genesis-to-witness/paper.md` | `papers/2026-from-genesis-to-witness/paper.fa.md` | ✅ Complete pair |
| Beyond Models / HACS | `2026/beyond-models-hacs/paper.en.md` | `2026/beyond-models-hacs/paper.fa.md` | ✅ Canonical public v1.0 complete pair |

## Resolved integrity finding — Before the First Chapter

The English canonical Markdown had been reduced to the placeholder `Test content`, while the full Persian manuscript and the original English PDF remained preserved. On 2026-08-12 the English Markdown was restored as a complete bilingual counterpart from the preserved Persian manuscript. The restored file contains an explicit archival recovery note and the original English PDF remains untouched in the same folder as a historical artifact.

This recovery is intentionally transparent: the repository does not present a silently reconstructed text as though the Markdown had never been lost.

## HACS lineage decision

Two HACS-related lineages exist in the repository. `2026/beyond-models-hacs/` is the explicit coherent public release and its `paper.en.md` / `paper.fa.md` files form a complete bilingual manuscript. The separate `papers/2026-enduring-human-ai-collaborative-systems/` directory preserves staged revisions and research components from v0.x through v1.3.

A higher version number does not automatically become the website manuscript. The current site therefore keeps the coherent public v1.0 pair canonical until a later version is deliberately assembled and promoted as a complete bilingual manuscript.

## Public language architecture

- `/` → English Research Hub
- `/fa/` → Persian Research Hub
- `/papers/<slug>/` → English full text only
- `/fa/papers/<slug>/` → Persian full text only

Every paper page links back to its canonical Markdown, research folder, and revision history. Each language page also publishes `hreflang` references to the corresponding edition.

## Promotion rule for future versions

A newer manuscript becomes canonical only when all of the following are true:

1. it is a complete manuscript rather than a revision fragment;
2. the corresponding language pair is defined or the language gap is explicitly documented;
3. `site/build.py` is updated to point to it;
4. this audit is updated;
5. status/version metadata are updated;
6. CI builds and validates both public routes successfully.

This policy protects the public Research Hub from accidental regressions while preserving the full development history in GitHub.
