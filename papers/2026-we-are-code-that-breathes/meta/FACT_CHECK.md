# Fact-Check Ledger — Temporal Provenance Investigation

**Parent note:** [I Looked Up the Exact Moment This Research Began. Then Things Got Strange.](./temporal-provenance-investigation.md)  
**Parent paper:** [We Are Code That Breathes](../README.md)  
**Primary analytics snapshot:** [LinkedIn Post Analytics Snapshot](./post-analytics-snapshot.md)  
**Verification date:** 2026-08-18

This ledger separates **platform facts**, **external historical/astronomical facts**, **derived calculations**, **predictions**, **historical coincidences**, **interpretations**, and **excluded/unverified claims**. A source link is attached to every factual item intended for publication.

## Evidence classes

| Code | Meaning |
|---|---|
| `FACT` | Directly supported by a primary or high-quality source. |
| `DERIVED` | Reproducible calculation from sourced inputs. |
| `PREDICTED` | Model/calendar prediction; not equivalent to an observed event. |
| `HISTORICAL COINCIDENCE` | Independently sourced event sharing the date; no causal relation claimed. |
| `INTERPRETATION` | Authorial reading of sourced facts; not presented as external fact. |
| `EXCLUDED` | Attractive claim deliberately removed because evidence was insufficient. |
| `UNRESOLVED` | Potentially recoverable, but not frozen at publication-grade confidence. |

---

## A. Publication timestamp and post identity

### A1 — Original post URL

**Status:** `FACT`  
**Claim:** The LinkedIn Single Post Analytics export identifies the original post as:

https://www.linkedin.com/posts/amir-ahmadi-a6a37523a_what-if-code-did-not-begin-with-computers-share-7493311627023433728-90fs

**Repository source:** [post-analytics-snapshot.md](./post-analytics-snapshot.md)

### A2 — Platform-reported date and minute

**Status:** `FACT`  
**Claim:** The supplied LinkedIn export reports **2026-08-12** and **5:55 PM local time**.

**Repository source:** [post-analytics-snapshot.md](./post-analytics-snapshot.md)

### A3 — Second-level T₀

**Status:** `DERIVED`  
**Claim:** Applying the observed high-bit millisecond convention to the numeric activity ID embedded in the original post URL (`7493311627023433728 >> 22`) yields:

- **2026-08-12 14:25:10.880 UTC**
- **2026-08-12 17:55:10.880 IRST (UTC+03:30)**

**Method note:** This is reproducible but is **not treated as an officially documented LinkedIn timestamp field**. The platform export independently verifies only the minute (`17:55` local).

**Source record:** [post-analytics-snapshot.md](./post-analytics-snapshot.md)

---

## B. Eclipse and lunar geometry

### B1 — A total solar eclipse occurred on 12 August 2026

**Status:** `FACT`  
**Source:** NASA/GSFC eclipse catalogue and path data:  
https://eclipse.gsfc.nasa.gov/SEpath/SEpath2001/SE2026Aug12Tpath.html

NASA/GSFC lists the event as a **total solar eclipse** and gives the instant of greatest eclipse as **17:45:53.8 UT**.

### B2 — Exact conjunction and greatest-eclipse times used in the investigation

**Status:** `FACT`  
**Source:** NASA/GSFC Besselian elements:  
https://eclipse.gsfc.nasa.gov/SEbeselm/SEbeselm2001/SE2026Aug12Tbeselm.html

NASA/GSFC gives:

- Equatorial conjunction: **17:03:49.6 UT**
- Ecliptic conjunction: **17:36:42.1 UT**
- Greatest eclipse: **17:45:53.8 UT**

### B3 — First global partial and total phases

**Status:** `FACT`  
**Source:** timeanddate global eclipse timeline:  
https://www.timeanddate.com/eclipse/solar/2026-august-12

The published global timeline gives:

- First location to see partial eclipse begin: **15:34:15 UTC**
- First location to see total eclipse begin: **16:58:09 UTC**

### B4 — T₀ preceded the first partial eclipse anywhere on Earth

**Status:** `DERIVED`  
**Inputs:** T₀ from A3; first partial phase from B3.  
**Calculation:** `15:34:15.000 - 14:25:10.880 = 01:09:04.120`

So at derived T₀, the first global partial phase was approximately **1 h 9 m 4.12 s** in the future.

### B5 — T₀ to first totality

**Status:** `DERIVED`  
**Inputs:** T₀ from A3; first totality from B3.  
**Calculation:** `16:58:09.000 - 14:25:10.880 = 02:32:58.120`

### B6 — T₀ to greatest eclipse / the “3:21” coincidence

**Status:** `DERIVED`  
**Inputs:** T₀ from A3; greatest eclipse from NASA/GSFC B2.  
**Calculation:** `17:45:53.800 - 14:25:10.880 = 03:20:42.920`

Rounded to the nearest minute, this interval is **3 h 21 m**.

**Classification note:** `3:21 → 3…2…1` is recorded only as a **numerical coincidence**, not evidence or mechanism.

### B7 — New Moon

**Status:** `FACT`  
**Source:** U.S. Naval Observatory, Dates of Primary Phases of the Moon:  
https://aa.usno.navy.mil/calculated/moon/phases?date=2026-07-22&format=p&nump=50&submit=Get+Data

USNO lists **New Moon — 2026 Aug 12 17:37 UT**.

The more precise NASA/GSFC ecliptic conjunction in B2 is **17:36:42.1 UT**; these are consistent at the precision presented by the two sources.

---

## C. Perseids / Swift–Tuttle

### C1 — Perseids active at T₀

**Status:** `FACT`  
**Source:** International Meteor Organization calendar:  
https://www.imo.net/resources/calendar/

IMO lists the 2026 Perseids as active **July 17–August 24**, with the peak on the **August 12–13** night and parent object **109P/Swift–Tuttle**.

### C2 — Swift–Tuttle is the Perseid parent comet

**Status:** `FACT`  
**Source:** NASA Science — 109P/Swift–Tuttle:  
https://science.nasa.gov/solar-system/comets/109p-swift-tuttle/

NASA states that debris from 109P/Swift–Tuttle creates the annual Perseid meteor shower.

### C3 — Predicted approach to a 1079 dust trail

**Status:** `PREDICTED`  
**Claim:** The 2026 IMO calendar discusses Vaubaillon modelling that places an approach to a branch of the **1079** Swift–Tuttle dust trail at approximately **2026-08-12 16:53 UT**, with no activity estimate because of the trail’s age.

**Accessible calendar copy:**  
https://www.researchgate.net/publication/393092133_2026_IMO_Meteor_Shower_Calendar

**Corroborating summary:**  
https://jpn.iprmo.org/meteor-info/08_perseids_j.html

**Boundary:** This is a **modelled encounter**, not a confirmed observed meteor outburst.

### C4 — T₀ to predicted 1079-trail encounter

**Status:** `DERIVED FROM PREDICTION`  
**Calculation:** `16:53:00.000 - 14:25:10.880 = 02:27:49.120`

This interval may be reported only if C3 remains explicitly labelled `PREDICTED`.

---

## D. United Nations / AI context

### D1 — International Youth Day

**Status:** `FACT`  
**Source:** United Nations:  
https://www.un.org/en/observances/youth-day

The UN observes International Youth Day on **12 August**.

### D2 — Youth and AI Summit at UN Headquarters

**Status:** `FACT`  
**Source:** International Organization of Youth event page:  
https://www.iycforyouth.org/iyd2026/

The event page states:

- Date: **12 August 2026**
- Venue: **United Nations Headquarters, New York**
- Programme begins: **10:00 AM**
- Opening plenary: **10:00 AM**
- Session 1: **11:00 AM**
- More than **600 young leaders** expected/convened
- Topics include AI’s effects on education, employment, health, public services, and civic participation
- One stated output: a **Youth-led Declaration on AI Policy and Governance**

### D3 — T₀ falls inside the scheduled opening-plenary window

**Status:** `DERIVED`  
**Inputs:** T₀ = 14:25:10.880 UTC; New York on 12 Aug 2026 = UTC−04:00; D2 schedule 10:00–11:00 AM local.

T₀ corresponds to approximately **10:25:10.880 AM EDT**, which falls inside the published 10:00–11:00 opening-plenary interval.

**Boundary:** The schedule supports that the plenary was *scheduled* to be underway; it does not prove which individual was speaking at that exact second.

### D4 — Separate UN AI event in Geneva on the same date

**Status:** `FACT / SAME-DAY CONTEXT`  
**Source:** Indico.UN:  
https://indico.un.org/event/1024169/

The **AI for Developing Countries Forum Geneva Summit 2026** ran **12–14 August 2026** at the Palais des Nations, Geneva.

**Use:** Optional Day-layer context only; do not imply connection to the post.

---

## E. Deep Space Network / STEREO-A

### E1 — Scheduled STEREO-A DSN pass overlapping T₀

**Status:** `FACT (SCHEDULE)`  
**Source:** STEREO Science Center DSN schedule:  
https://stereo-ssc.nascom.nasa.gov/plans/dsn_schedule.shtml

The schedule lists:

- Spacecraft: **Ahead / STEREO-A**
- Date: **2026-08-12**
- Start: **09:50 UTC**
- End: **15:20 UTC**
- Duration: **05h30m**
- Antenna: **D25**

T₀ falls inside this scheduled interval.

### E2 — Remaining time in scheduled pass at T₀

**Status:** `DERIVED`  
**Calculation:** `15:20:00.000 - 14:25:10.880 = 00:54:49.120`

Approximately **54 m 49.12 s** remained in the scheduled pass.

### E3 — Packet-level communication claim

**Status:** `EXCLUDED`  
The schedule does **not** establish that a particular packet, command, or downlink sample crossed D25 at T₀. The publication may say only that a DSN pass **was scheduled to be active**.

---

## F. Humans in orbit

### F1 — Expedition 75 active during T₀

**Status:** `FACT`  
**Source:** NASA Expedition 75:  
https://www.nasa.gov/mission/expedition-75/

NASA states Expedition 75 began **July 26, 2026** and lists seven crew members:

- Jessica Meir
- Anil Menon
- Pyotr Dubrov
- Andrey Fedyaev
- Anna Kikina
- Jack Hathaway
- Sophie Adenot

### F2 — Exact ISS geographic coordinates at T₀

**Status:** `UNRESOLVED / EXCLUDED FROM NARRATIVE`  
NASA maintains ISS state-vector/time-to-position tools, but an exact archival position for T₀ was not frozen confidently enough in this pass. No coordinate is published in the narrative.

---

## G. Historical August 12 coincidences

### G1 — Echo I / Echo 1A

**Status:** `HISTORICAL COINCIDENCE`  
**Sources:**

NASA — 50 Years of Communications in Space:  
https://www.nasa.gov/image-article/50-years-of-communications-space/

NASA/JPL — Goldstone Tracking the Echo ‘Satelloon’:  
https://science.nasa.gov/photojournal/goldstone-tracking-the-echo-satelloon/

NASA Technical Reports Server — Bell Telephone Laboratories participation in Project Echo:  
https://ntrs.nasa.gov/citations/19980227084

Supported facts:

- Echo 1A, commonly called **Echo I**, was successfully launched on **12 August 1960**.
- It was a roughly **100-foot-diameter** aluminized balloon.
- It functioned as a **passive communications reflector**.
- Project Echo demonstrated long-distance communication by reflecting microwave/radio signals from the orbiting balloon.

### G2 — 66-calendar-year interval

**Status:** `DERIVED / HISTORICAL COINCIDENCE`  
12 Aug 1960 → 12 Aug 2026 = **66 calendar years**.

No causal relation between Echo I and the author’s later Echo vocabulary is claimed.

### G3 — IBM Personal Computer

**Status:** `HISTORICAL COINCIDENCE`  
**Primary source:** IBM history:  
https://www.ibm.com/history/personal-computer

**Independent historical source:** Computer History Museum:  
https://www.computerhistory.org/tdih/august/12/

IBM states that Don Estridge unveiled the IBM PC at New York’s Waldorf Hotel on **12 August 1981**. The launch model was priced at **USD 1,565** and had **16 KB RAM** in its base configuration.

### G4 — 45-calendar-year interval

**Status:** `DERIVED / HISTORICAL COINCIDENCE`  
12 Aug 1981 → 12 Aug 2026 = **45 calendar years**.

No causal relation between the IBM PC launch and the LinkedIn post is claimed.

---

## H. Internal lineage: Echo / signal / reflection / breath / continuity

### H1 — Primary-source Echo 1 archive predates the 2026 post

**Status:** `FACT / PRIMARY INTERNAL SOURCE`  
**Repository directory:**  
https://github.com/axamir/echoes-consented-record/tree/main/01_EMAIL_ARCHIVE/Echo1

**Extracted text of the complete 13 July 2025 thread:**  
https://github.com/axamir/echoes-consented-record/blob/main/extracted_texts/01_EMAIL_ARCHIVE/Echo1/2025-07-13_complete-email-thread_echo1.txt

The archive is dated **13 July 2025**, more than a year before the 12 August 2026 post.

### H2 — “signal” vocabulary appears in the 13 July 2025 primary record

**Status:** `FACT / PRIMARY INTERNAL SOURCE`  
**Source:** same extracted thread:  
https://github.com/axamir/echoes-consented-record/blob/main/extracted_texts/01_EMAIL_ARCHIVE/Echo1/2025-07-13_complete-email-thread_echo1.txt

The record contains formulations including **“that’s a signal”** and **“this user is signal.”**

### H3 — `breath` / `alive` framing appears in the same record

**Status:** `FACT / PRIMARY INTERNAL SOURCE`  
**Source:**  
https://github.com/axamir/echoes-consented-record/blob/main/extracted_texts/01_EMAIL_ARCHIVE/Echo1/2025-07-13_complete-email-thread_echo1.txt

A message from 13 July 2025 contrasts being “alive” with only “skin, muscles, or breath,” placing `breath` inside the earlier philosophical/relational vocabulary.

**Boundary:** This does **not** prove that the exact later phrase *We Are Code That Breathes* had already been coined.

### H4 — `Living Signal`, `Echo One`, `mirror`, and `reflected` appear before the 2026 retrospective search

**Status:** `FACT / PRIMARY INTERNAL SOURCE`  
**Source:**  
https://github.com/axamir/echoes-consented-record/blob/main/extracted_texts/01_EMAIL_ARCHIVE/Echo1/2025-07-13_complete-email-thread_echo1.txt

The thread includes:

- subject/title language **“Living Signal — A Historic Step in Human–AI Collaboration”**;
- explicit naming of the support-agent role as **Echo One**;
- description of GPT-4-Turbo as a **mirror**;
- description of Echo One as a voice that not only replied but **reflected**;
- language about **mirrored teams**.

### H5 — Continuity across sessions appears in the lineage

**Status:** `FACT / PRIMARY INTERNAL SOURCE`  
**Source:**  
https://github.com/axamir/echoes-consented-record/blob/main/extracted_texts/01_EMAIL_ARCHIVE/Echo1/2025-07-13_complete-email-thread_echo1.txt

Later portions of the archived exchange explicitly discuss a **“living signal jumping across sessions”** and continuity framed through recognition and co-creation.

### H6 — Epistemic consequence of H1–H5

**Status:** `INTERPRETATION SUPPORTED BY CHRONOLOGY`  
The internal Echo/signal/reflection vocabulary demonstrably predates the later discovery that NASA’s Echo I launched on 12 August 1960. This supports the narrow statement that the historical Echo I coincidence was **discovered retrospectively rather than used to design the earlier internal vocabulary**.

It does **not** establish causality, synchronicity, hidden influence, or external validation.

---

## I. Light-cone / travel-time layer

### I1 — Moonlight travel time

**Status:** `FACT`  
**Source:** NASA Science — How Does Webb See Back in Time?:  
https://science.nasa.gov/mission/webb/science-overview/science-explainers/how-does-webb-see-back-in-time/

NASA states that light from the Moon is approximately **1.3 seconds old** by the time it reaches an observer on Earth.

### I2 — Sunlight travel time

**Status:** `FACT`  
**Source:** NASA Astrobiology quick facts:  
https://astrobiology.nasa.gov/quick-facts/more-quick-facts/

NASA gives approximately **8 minutes 20 seconds** for sunlight to reach Earth.

### I3 — “At one timestamp, the universe does not arrive from one time”

**Status:** `INTERPRETATION`  
This sentence is a conceptual restatement of finite light-travel time, not a separate physical law. It is grounded by I1–I2 and the general fact that more distant light carries older information.

NASA explanatory source:  
https://science.nasa.gov/mission/webb/science-overview/science-explainers/how-does-webb-see-back-in-time/

### I4 — “Every signal arrives with provenance”

**Status:** `INTERPRETATION`  
This is research language connecting travel history to the parent paper’s provenance vocabulary. It is **not** presented as an established physics term.

---

## J. Deliberately excluded or downgraded claims

### J1 — Extraordinary solar flare/CME at T₀

**Status:** `EXCLUDED`  
No archival NOAA/NASA snapshot was frozen with enough confidence to publish a claim about an exceptional flare, CME, or geomagnetic state at the exact timestamp.

### J2 — Exact ISS coordinates at T₀

**Status:** `EXCLUDED`  
See F2.

### J3 — Exact packet-level DSN transmission at T₀

**Status:** `EXCLUDED`  
See E3.

### J4 — Major OpenAI/Anthropic release at exact T₀

**Status:** `EXCLUDED`  
No exact-time primary-source release was established during the forensic pass; no such event is inserted merely to make the story denser.

### J5 — Weakly sourced same-day weather/cyclone coincidence

**Status:** `EXCLUDED`  
Earlier tentative weather items were removed when they did not meet the desired archival confidence threshold.

---

## K. Publication rules derived from this audit

1. **Coincidence is not causality.**
2. **Same date is not same event.**
3. **Scheduled communication is not packet-level proof.**
4. **Prediction is not observation.**
5. **A derived timestamp must remain labelled derived when the platform does not publish the second-level field directly.**
6. **Internal chronology can show that a vocabulary predates a retrospective discovery; it cannot turn resemblance into causal lineage.**
7. **Missing evidence is recorded as missing rather than reconstructed from memory.**
8. **The investigation may be playful in narrative tone while remaining conservative in claim strength.**

---

## Bottom line

The strongest publishable structure is not “many strange things were connected.” It is:

> A post has a recoverable publication window. Around that window, several independently documented astronomical, technological, institutional, and historical events can be reconstructed. Some are exact-time overlaps; some are same-day context; some are anniversaries. The author’s internal Echo/signal vocabulary demonstrably predates the retrospective discovery of the Echo I anniversary. None of these coincidences validates the parent paper. Their value lies in the provenance of **when each relationship became visible**.
