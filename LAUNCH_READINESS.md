# Research Hub — Launch Readiness Record

**Project:** Amir Ahmadi Research  
**Public URL:** https://axamir.github.io/amir-ahmadi-research-papers/  
**Review date:** 2026-08-12  
**Scope:** 11 research works × English/Persian publication routes

## Launch standard

The Research Hub is considered ready for professional introduction only when its public website functions as an independent research publication layer rather than a GitHub file index. The repository remains the source of truth; the website provides discovery, reading, presentation, provenance and verification.

## Readiness checklist

- [x] Chronological Research Hub with professional paper cards
- [x] Responsive desktop, tablet and smartphone layouts
- [x] Separate English and Persian hubs
- [x] Full-paper web reading from canonical Markdown sources
- [x] Strict EN → English manuscript / FA → Persian manuscript separation
- [x] 11 explicit bilingual canonical source pairs
- [x] Source integrity checks that reject placeholders or missing manuscripts
- [x] Restored bilingual record for *Before the First Chapter* with transparent recovery provenance
- [x] Explicit HACS canonical-version policy
- [x] Persian typography upgraded to **Vazirmatn** with local system fallbacks
- [x] RTL reading typography, spacing and code-direction handling
- [x] Individual paper identity: title, date, version, status and topics
- [x] Canonical URLs and `hreflang` EN / FA / x-default
- [x] `ScholarlyArticle` JSON-LD for every paper edition
- [x] Citation metadata and suggested citation block
- [x] One-click citation copy interaction
- [x] Direct links to canonical Markdown, GitHub research folder and revision history
- [x] Paper-specific OpenGraph/Twitter preview images generated at build time
- [x] Reading-progress indicator on full-paper pages
- [x] Sitemap covering both hubs and all bilingual paper routes
- [x] Robots, favicon and web manifest
- [x] Contact / research-correspondence section
- [x] Hidden-style language command layer (`@@fa` / `@@en`) preserving the current paper route
- [x] LDG executable model, tests and machine-verification artifacts linked from its publication page
- [x] HACS framework artifacts linked from its publication page
- [x] CI validation for all 22 paper pages, full-text markup, metadata and OG assets
- [x] GitHub Pages deployment workflow

## Publication architecture

```text
GitHub canonical archive
        ↓
source integrity validation
        ↓
publication build
        ├── English Research Hub
        │     └── 11 full paper pages
        ├── Persian Research Hub
        │     └── 11 full paper pages
        ├── scholarly metadata
        ├── per-paper social previews
        └── sitemap / provenance / artifacts
        ↓
GitHub Pages
```

## Integrity principles

1. The website never invents a missing paper silently.
2. A higher version number does not replace a complete canonical manuscript unless deliberately promoted.
3. English and Persian sources remain independently traceable.
4. Supporting code, diagrams and PDFs supplement rather than overwrite canonical text.
5. Recovery or reconstruction of archival material must be disclosed in the source record.
6. Public status labels distinguish published research, working papers, drafts, essays and executable artifacts.

## Final automated gate

The `Research Hub validation` workflow must pass before a public build is considered launch-ready. The gate verifies every registered English and Persian paper page, full-text rendering, scholarly metadata, language links, absence of placeholder warnings, social preview images, Persian typography assets and sitemap generation.

The `Deploy Research Hub to Pages` workflow must then complete successfully for the same source state.
