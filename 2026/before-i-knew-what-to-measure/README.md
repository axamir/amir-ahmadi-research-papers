# Before I Knew What to Measure

## Following an Intuition Through Behavioral Data, Space Weather, and the Search for What Actually Changed

**Author:** Amir Ahmadi  
**Year:** 2026  
**Current audited release:** **v0.1 — 31 August 2026**

This project asks a narrow but difficult question: what is intuition actually good for when it points toward a real external event, but the first controls begin to weaken the causal story?

The investigation began with an unusual period of fatigue, sleepiness, muscular weakness, reduced exercise capacity and difficulty sustaining deep work. Before checking space-weather reports, an intuition directed attention toward solar activity. A real solar/geomagnetic sequence existed in the same broad period—but the behavioral record also contained important counterexamples.

The project therefore treats intuition as a **hypothesis generator**, not as evidence.

> **Anomaly Detection ≠ Causal Identification**

> **Maybe intuition is not a way of knowing. Maybe it is a way of noticing where knowing should begin.**

## Read the audited release

- **English:** [`releases/v0.1/paper.en.md`](releases/v0.1/paper.en.md)
- **فارسی:** [`releases/v0.1/paper.fa.md`](releases/v0.1/paper.fa.md)
- **Release notes:** [`releases/v0.1/RELEASE_NOTES.md`](releases/v0.1/RELEASE_NOTES.md)
- **Source audit:** [`references/audit-sources-v0.1.md`](references/audit-sources-v0.1.md)

The root-level `paper.en.md` and `paper.fa.md` are retained as historical working drafts. **v0.1 is the canonical audited text.** In particular, the initial English draft contained an August 18 Mac Screen Time transcription of `11h02m`; the audited value in the dataset and v0.1 is **11h22m (682 minutes)**.

## Figure 1

![Behavioral timeline with selected space-weather markers](figures/figure-01-behavior-space-weather.svg)

Figure 1 places daily Mac activity beside selected audited space-weather markers. It is descriptive and must not be interpreted as evidence of causality.

## Project structure

- `releases/v0.1/` — canonical audited English and Persian manuscripts
- `paper.en.md`, `paper.fa.md` — historical working drafts
- `evidence/` — evidence manifest, screenshot inventory and package metadata
- `data/` — extracted behavioral and environmental datasets
- `figures/` — article-ready visualizations
- `methods/` — analysis plan, assumptions, controls and limitations
- `references/` — factual audit trail and scientific literature

## Current behavioral finding

Across the extracted Mac dataset, average total Mac activity was approximately **9h29/day during Aug 15–22** and **5h27/day during Aug 23–30**, a decline of roughly **43%**. The Productivity & Finance category declined much less, from roughly **3h46/day to 3h31/day** (~7%).

This does not establish fatigue or impairment, but it is more consistent with a reduction in sustained active engagement than with a complete loss of productive capacity. Screen Time categories remain coarse behavioral proxies.

The iPhone record provides an additional contrast: on Aug 30, roughly 11h24 of 12h54 total Screen Time was Social + Entertainment, while Aug 10 had 16h20 total use with roughly 9h25 categorized as Productivity & Finance. Total device time alone is therefore a poor state proxy in this record.

## Space-weather control logic

The project explicitly preserves counterevidence. SIDC reported minor-storm-level NOAA Kp intervals around Aug 18–19, yet Mac activity remained approximately **11h22** and **11h24** on those days. Conversely, SIDC described the preceding 24 hours on Aug 27 as globally quiet (Kp 1–2) while part of the behavioral anomaly was already present in the broader late-August period.

This weakens the simple hypothesis:

> `higher geomagnetic activity → lower functioning`

It does not rule out every possible environmental hypothesis, but the project does not rescue the original idea by freely changing variables or time lags after seeing the data.

## Locked next-phase analysis

The prospective phase predefines five environmental variables:

`Kp`, `Dst`, `IMF Bz`, `solar-wind speed`, `solar-wind density`

with fixed lag windows:

`0h`, `6h`, `12h`, `24h`

Quiet periods, stronger events with normal behavior, and poor-behavior periods during quiet conditions must remain in the dataset.

## Methodological position

This project is **not** presented as evidence that space weather caused the reported symptoms. The current evidence supports a behavioral state change and confirms that measurable solar/geomagnetic events occurred in the same broad period, but a direct causal relationship has not been established.

Forecasts and watches are kept separate from observations. Planetary Kp is not treated as a local exposure measurement. Screen Time is not treated as a biomarker. Proposed biological mechanisms in the literature are background hypotheses, not explanations of this individual episode.

## Evidence policy

Original screenshots are treated as source records. Numerical values should remain traceable from source screenshot → manifest → extracted dataset → analysis → figure. The SHA-256 source manifest records canonical filename, original capture filename, byte size and digest for the reviewed image set.

The source captures were visually reviewed for unrelated sensitive identifiers. Binary evidence packages have been prepared separately; the repository contains their manifests and integrity metadata. Binary screenshot upload remains a separate publication step from the text/SVG audit trail.

## Status

**v0.1 is ready for public reading as a transparent working research essay.** It is not a medical conclusion and not a causal finding about space weather.

The next meaningful upgrade is prospective blinded observation with better physiological data and complete observed space-weather time series.
