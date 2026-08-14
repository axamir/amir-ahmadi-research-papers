# Publication QA — ARP-WCB-2026-01

**Paper:** We Are Code That Breathes  
**Version:** RC v0.3  
**QA date:** 2026-08-14

## Deployment verification

- GitHub Pages build: passed
- Source validation: passed
- WCB publication renderer: passed
- Visual identity/social preview step: passed
- Artifact upload: passed
- GitHub Pages deploy: passed

## Generated artifact inspection

The deployed Pages artifact was downloaded from the successful workflow run and inspected directly.

### English publication page

- Path generated: `papers/we-are-code-that-breathes/index.html`
- `<html lang="en">`: present
- canonical URL points to English publication route: passed
- Open Graph image: present
- JSON-LD `ScholarlyArticle`: present
- H1 title: correct
- full manuscript sections rendered: passed
- GitHub/source links present: passed

### Persian publication page

- Path generated: `fa/papers/we-are-code-that-breathes/index.html`
- `<html lang="fa" dir="rtl">`: present
- canonical points to the English research record in accordance with Research Hub policy: passed
- Persian social preview: present
- JSON-LD: present
- H1 title: correct
- aligned Persian manuscript rendered: passed

### Landing integration

- English landing contains WCB publication link: passed
- Persian landing contains WCB Persian route: passed
- sitemap contains English route: passed
- sitemap contains Persian route: passed

## Metadata

- Document ID: `ARP-WCB-2026-01`
- `CITATION.cff`: present
- ORCID metadata: present in publication renderer
- citation meta tags: present
- Open Graph/Twitter metadata: present
- social preview assets: present in EN and FA

## Scientific boundary checks

- page identifies PRCEP as a protocol candidate rather than validated protocol: passed
- case is described as protocol construction / case demonstration: passed
- English page remains canonical research record: passed
- Persian edition remains an aligned interpretation/research edition: passed
- unresolved archival quote/permalink states remain qualified in the evidence layer: passed

## QA conclusion

**Publication-layer QA: PASS.**

This result verifies generation, metadata, bilingual routing, landing integration, sitemap inclusion, and successful deployment of the release-candidate publication artifact. It does **not** constitute empirical validation of PRCEP or independent scientific review of the manuscript.