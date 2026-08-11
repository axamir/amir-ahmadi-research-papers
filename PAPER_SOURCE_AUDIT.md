# Research Paper Source Audit

**Repository:** `axamir/amir-ahmadi-research-papers`  
**Purpose:** Define the canonical full-text Markdown source used by the Research Hub for each public paper, separately for English and Persian.

## Canonical source policy

The website is a reading layer, not a duplicate authoring layer. Each public article page must be generated from one explicit canonical Markdown file in the repository. English pages render only the English source. Persian pages render only the Persian source. Draft fragments, historical revisions, README files, supplements, code, PDFs and diagrams may remain available in the repository but are not substituted for the canonical full paper unless explicitly promoted.

## Audit table

| Paper | English canonical source | Persian canonical source | Audit status |
|---|---|---|---|
| Living Decision Governance | `papers/2026-living-decision-governance/LDG_COMPLETE.md` | `papers/2026-living-decision-governance/LDG_COMPLETE.fa.md` | ✅ Canonical complete pair; executable artifacts remain supplementary |
| Beyond Intelligence — AI Evolution | `papers/beyond-intelligence-ai-evolution/paper-en.md` | `papers/beyond-intelligence-ai-evolution/paper-fa.md` | ✅ Canonical bilingual pair; covers and Figure 1 are supporting assets |
| From Green Personalisation to Relational Co-Evolution | `papers/2026-relational-co-evolution/paper.en.md` | `papers/2026-relational-co-evolution/paper.fa.md` | ✅ Canonical bilingual pair; LinkedIn cover is a presentation asset |
| Reflections and Their Owners | `papers/2026-reflections-and-their-owners/paper.md` | `papers/2026-reflections-and-their-owners/paper.fa.md` | ✅ Canonical bilingual pair |
| From Stamp to Alliance | `papers/2026-from-stamp-to-alliance/paper.en.md` | `papers/2026-from-stamp-to-alliance/paper.fa.md` | ✅ Canonical bilingual pair; PDFs remain alternate reading formats |
| From Money to Pledge | `papers/2026-from-pledge-to-sovereignty/paper.en.md` | `papers/2026-from-pledge-to-sovereignty/paper.fa.md` | ✅ Canonical bilingual pair; repository folder name differs from public card title |
| I, You, and We | `papers/2026-human-ai-co-creation-manifesto/paper.en.md` | `papers/2026-human-ai-co-creation-manifesto/paper.fa.md` | ✅ Canonical bilingual pair |
| Designing Rest | `papers/2026-designing-rest/paper.en.md` | `papers/2026-designing-rest/paper.fa.md` | ✅ Canonical bilingual pair |
| Before the First Chapter | `papers/2026-before-the-first-chapter/paper.en.md` | `papers/2026-before-the-first-chapter/paper.fa.md` | ⚠️ English Markdown is currently corrupted/placeholder (`Test content`); Persian Markdown is complete; English PDF exists and should be used only for recovery, not silently substituted |
| From Genesis to Witness | `papers/2026-from-genesis-to-witness/paper.md` | `papers/2026-from-genesis-to-witness/paper.fa.md` | ✅ Canonical bilingual pair; PDF is an alternate format |
| Beyond Models / HACS | `2026/beyond-models-hacs/paper.en.md` | `2026/beyond-models-hacs/paper.fa.md` | ✅ Canonical public v1.0 bilingual release. The `papers/2026-enduring-human-ai-collaborative-systems/` versioned files are development/revision artifacts, not one cumulative final manuscript |

## Important findings

### 1. Before the First Chapter — English integrity issue

The current English Markdown contains only placeholder text while a substantive English PDF exists. The Research Hub should therefore show an integrity notice rather than inventing or silently replacing the missing manuscript. Recovery should reconstruct the Markdown from the authoritative historical source/PDF and then replace the placeholder file.

### 2. HACS has two research lineages in the repository

`2026/beyond-models-hacs/` is the explicit public v1.0 release and its README identifies `paper.en.md` and `paper.fa.md` as the research manuscripts. The separate `papers/2026-enduring-human-ai-collaborative-systems/` directory contains staged version artifacts such as theoretical core, evaluation framework, system architecture, domain validation, scientific positioning, formal framework, white paper, publication-quality revision, final-research-edition and architecture-visual-model. These are valuable provenance artifacts, but their filenames and sizes indicate staged research components rather than a single cumulative full paper. The public website therefore keeps the coherent v1.0 bilingual manuscript as canonical until a deliberately assembled v1.1+ full manuscript is promoted.

### 3. Language separation

The public architecture is strict:

- `/papers/<slug>/` → English full text only
- `/fa/papers/<slug>/` → Persian full text only
- `/` → English research hub
- `/fa/` → Persian research hub

The GitHub repository remains accessible from every article as source/provenance, but it is not required for reading the article.

## Promotion rule for future versions

A newer file becomes canonical only when it is explicitly a complete manuscript rather than a fragment or revision note. Promotion should update:

1. `site/build.py` source registry,
2. this audit file,
3. article version/status metadata,
4. bilingual alignment status,
5. CI validation.

This prevents a file with a higher version number but partial content from accidentally replacing a complete public paper.
