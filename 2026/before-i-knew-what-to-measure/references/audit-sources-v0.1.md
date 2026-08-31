# Audit Sources — v0.1

This file records the sources used to audit factual claims in the v0.1 release of **Before I Knew What to Measure**.

## Space-weather event record

1. **SIDC daily bulletin — 18 August 2026**  
   https://www.spaceweatherlive.com/en/archive/2026/08/18/sidc-ursigram.html  
   Used for the August 18 geomagnetic control period and associated solar-wind context.

2. **SIDC daily bulletin — 19 August 2026**  
   https://www.spaceweatherlive.com/en/archive/2026/08/19/sidc-ursigram.html  
   Reports NOAA Kp 5+ during 18:00–21:00 UTC on August 18 and Kp 5 during 03:00–06:00 UTC on August 19. It also reports IMF Bz varying from approximately -10 nT to +12 nT over the preceding 24 hours.

3. **SIDC daily bulletin — 25 August 2026**  
   https://www.spaceweatherlive.com/en/archive/2026/08/25/sidc-ursigram.html  
   Reports five M-class flares in the preceding 24 hours. The largest was M6.9, peaking at 10:02 UTC on August 25 from NOAA Active Region 4513 / SIDC Sunspot Group 929. At bulletin issue time, geomagnetic conditions were still classified as quiet and the associated CME was still being analysed.

4. **SIDC daily bulletin — 27 August 2026**  
   https://www.spaceweatherlive.com/en/archive/2026/08/27/sidc-ursigram.html  
   Reports globally quiet geomagnetic conditions during the preceding 24 hours, NOAA Kp 1–2, while later enhancement remained forecast.

5. **SIDC daily bulletin — 28 August 2026**  
   https://www.spaceweatherlive.com/en/archive/2026/08/28/sidc-ursigram.html  
   Used to preserve the distinction between observed conditions and later/anticipated enhancement. Forecast language must not be rewritten as an observed storm.

## Scientific literature

6. **Krylov V.V. (2017). Biological effects related to geomagnetic activity and possible mechanisms. Bioelectromagnetics, 38(7), 497–510.**  
   DOI: 10.1002/bem.22062  
   PubMed: https://pubmed.ncbi.nlm.nih.gov/28636777/  
   Review of reported biological correlations, simulated geomagnetic-storm studies, and proposed mechanisms including circadian variation, cryptochrome and melatonin. This source supports the statement that the topic has a research literature; it does not establish that a geomagnetic event caused the author's symptoms.

7. **Arnaut F., Kolarski A., Jevremović S. (2026). Solar activity, space weather and human health: can ChatGPT assist systematic literature reviews? International Journal of Biometeorology, 70(5), 143.**  
   DOI: 10.1007/s00484-026-03220-6  
   PubMed: https://pubmed.ncbi.nlm.nih.gov/42047846/  
   Systematic literature review used primarily to characterize the field as active but methodologically heterogeneous and to identify research gaps.

8. **Sethi Y. et al. (2026). Aurora-Associated Geomagnetic Activity and Health: A Review With Focus on Neurological Implications. GeoHealth, 10(6), e2025GH001710.**  
   DOI: 10.1029/2025GH001710  
   PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC13284886/  
   Review reporting observational associations in neurological and neuropsychiatric domains while emphasizing that current evidence remains largely associative and that mechanistic and longitudinal work is needed.

## Audit rules used in this release

- **Forecast ≠ observation.** Watches, forecasts and possible CME arrivals are not recorded as events that definitely occurred.
- **Planetary Kp ≠ local exposure.** Kp is a planetary geomagnetic index and is not a local magnetometer reading for the author's location.
- **Temporal coincidence ≠ causality.** The article does not claim that the August 2026 space-weather sequence caused fatigue, sleepiness, weakness or cognitive change.
- **Screen Time ≠ biomarker.** Device activity is treated only as a behavioral trace and proxy.
- **Counterexamples remain in the record.** August 18–19 are retained because they weaken the simple hypothesis that greater geomagnetic activity automatically predicts lower functioning.
- **No mechanism is claimed.** Proposed biological mechanisms in the literature are hypotheses/background, not an explanation of this individual episode.
