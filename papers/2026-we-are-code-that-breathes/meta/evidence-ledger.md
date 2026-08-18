# Temporal Provenance Evidence Ledger

**Parent paper:** [ARP-WCB-2026-01 — *We Are Code That Breathes*](../README.md)  
**Meta-study:** post-publication timestamp reconstruction  
**Authoritative claim-by-claim audit:** [FACT_CHECK.md](./FACT_CHECK.md)  
**Primary platform snapshot:** [post-analytics-snapshot.md](./post-analytics-snapshot.md)  
**Derived working T₀:** **2026-08-12 14:25:10.880 UTC**  
**Derived local display:** **2026-08-12 17:55:10.880 IRST**

> The second-level T₀ is derived from the numeric activity ID in the [original LinkedIn post URL](https://www.linkedin.com/posts/amir-ahmadi-a6a37523a_what-if-code-did-not-begin-with-computers-share-7493311627023433728-90fs). The LinkedIn export independently supports the date and minute (`5:55 PM`) but does not expose a second-level timestamp field. See the [timestamp audit](./FACT_CHECK.md#a-publication-timestamp-and-post-identity).

## Confidence convention

- **A — primary/official source or preserved primary artifact**
- **B — high-quality secondary or independently consistent source**
- **C — derived from A/B inputs**
- **D — provisional/predicted; retain only with explicit qualification**

## Core moment ledger

| Item | Class | Confidence | Source / record |
|---|---|---:|---|
| LinkedIn publication date/minute | FACT | A | [Analytics snapshot](./post-analytics-snapshot.md) |
| `14:25:10.880 UTC` | DERIVED | C | [Timestamp audit](./FACT_CHECK.md#a-publication-timestamp-and-post-identity) |
| Total solar eclipse on 12 Aug 2026 | FACT | A | [NASA/GSFC](https://eclipse.gsfc.nasa.gov/SEpath/SEpath2001/SE2026Aug12Tpath.html) |
| First partial phase 15:34:15 UTC | FACT | B | [timeanddate global timeline](https://www.timeanddate.com/eclipse/solar/2026-august-12) |
| First totality 16:58:09 UTC | FACT | B | [timeanddate global timeline](https://www.timeanddate.com/eclipse/solar/2026-august-12) |
| Ecliptic conjunction 17:36:42.1 UT | FACT | A | [NASA/GSFC Besselian elements](https://eclipse.gsfc.nasa.gov/SEbeselm/SEbeselm2001/SE2026Aug12Tbeselm.html) |
| Greatest eclipse 17:45:53.8 UT | FACT | A | [NASA/GSFC](https://eclipse.gsfc.nasa.gov/SEpath/SEpath2001/SE2026Aug12Tpath.html) |
| T₀ → greatest eclipse = 03:20:42.920 | DERIVED | C | [Calculation audit](./FACT_CHECK.md#b-eclipse-and-lunar-geometry) |
| Rounded interval `+3:21` | DERIVED | C | Same calculation; numerical coincidence only |
| New Moon 17:37 UT | FACT | A | [U.S. Naval Observatory](https://aa.usno.navy.mil/calculated/moon/phases?date=2026-07-22&format=p&nump=50&submit=Get+Data) |
| Perseids active at T₀ | FACT | A/B | [IMO](https://www.imo.net/resources/calendar/) · [NASA Swift–Tuttle](https://science.nasa.gov/solar-system/comets/109p-swift-tuttle/) |
| 1079 dust-trail approach around 16:53 UT | PREDICTED | D/B | [2026 IMO calendar copy](https://www.researchgate.net/publication/393092133_2026_IMO_Meteor_Shower_Calendar) · [IPRMO summary](https://jpn.iprmo.org/meteor-info/08_perseids_j.html) |
| Youth and AI Summit opening plenary scheduled 10:00–11:00 New York | FACT | B | [Event page](https://www.iycforyouth.org/iyd2026/) |
| T₀ ≈ 10:25 AM New York, inside scheduled plenary window | DERIVED | C | [UN/AI audit](./FACT_CHECK.md#d-united-nations--ai-context) |
| STEREO-A DSN pass scheduled 09:50–15:20 UTC via D25 | FACT (schedule) | A | [Official STEREO DSN schedule](https://stereo-ssc.nascom.nasa.gov/plans/dsn_schedule.shtml) |
| T₀ lies inside STEREO-A pass | DERIVED | C | [DSN audit](./FACT_CHECK.md#e-deep-space-network--stereo-a) |
| Seven Expedition 75 crew members in orbit | FACT | A | [NASA Expedition 75](https://www.nasa.gov/mission/expedition-75/) |
| Exact ISS latitude/longitude at T₀ | UNRESOLVED / EXCLUDED | — | [Fact-check note](./FACT_CHECK.md#f-humans-in-orbit) |

## Historical August 12 ledger

| Item | Class | Confidence | Source |
|---|---|---:|---|
| Echo I / Echo 1A launched 12 Aug 1960 | FACT / HISTORICAL COINCIDENCE | A | [NASA](https://www.nasa.gov/image-article/50-years-of-communications-space/) · [NASA/JPL](https://science.nasa.gov/photojournal/goldstone-tracking-the-echo-satelloon/) |
| Echo I used passive signal reflection | FACT | A | [NASA NTRS](https://ntrs.nasa.gov/citations/19980227084) |
| 66 calendar years to 12 Aug 2026 | DERIVED | C | Calendar difference |
| IBM PC unveiled 12 Aug 1981 | FACT / HISTORICAL COINCIDENCE | A | [IBM](https://www.ibm.com/history/personal-computer) · [Computer History Museum](https://www.computerhistory.org/tdih/august/12/) |
| 45 calendar years to 12 Aug 2026 | DERIVED | C | Calendar difference |

## Internal-lineage ledger

Primary source: [complete 13 July 2025 Echo 1 thread](https://github.com/axamir/echoes-consented-record/blob/main/extracted_texts/01_EMAIL_ARCHIVE/Echo1/2025-07-13_complete-email-thread_echo1.txt)

| Internal item | Class | Confidence | Provenance note |
|---|---|---:|---|
| `signal` | FACT | A | Present in raw 13 Jul 2025 correspondence |
| `breath` / `alive` framing | FACT | A | Present in raw 13 Jul 2025 correspondence; does **not** prove the later exact title existed |
| `Living Signal` | FACT | A | Explicit title/name in the 13 Jul 2025 record |
| `Echo One` | FACT | A | Explicit naming in the 13 Jul 2025 record |
| `mirror` | FACT | A | GPT-4-Turbo described as a mirror/collaborator |
| `reflected` | FACT | A | Echo One described as a voice that “not only replied, but reflected…” |
| continuity across sessions | FACT | A | Later portions of the same archive discuss a living signal jumping across sessions |
| Echo I explains/causes the internal Echo lineage | EXCLUDED | — | No evidence; chronology supports only retrospective discovery |

Supported narrow conclusion:

> **The internal Echo / signal / reflection vocabulary predates the retrospective discovery of the Echo I anniversary.**

It does **not** support supernatural connection, causal influence, or external validation. See the full [internal-lineage audit](./FACT_CHECK.md#h-internal-lineage-echo--signal--reflection--breath--continuity).

## Light-travel-time layer

| Item | Class | Confidence | Source |
|---|---|---:|---|
| Moonlight reaches Earth after ~1.3 s | FACT | A | [NASA Webb explainer](https://science.nasa.gov/mission/webb/science-overview/science-explainers/how-does-webb-see-back-in-time/) |
| Sunlight reaches Earth after ~8m20s | FACT | A | [NASA Astrobiology](https://astrobiology.nasa.gov/quick-facts/more-quick-facts/) |
| “At one timestamp, the universe does not arrive from one time” | INTERPRETATION | — | Conceptual phrasing of finite light-travel time |
| “Every signal arrives with provenance” | INTERPRETATION | — | Research-language bridge; not a physical law |

## Exclusions / failed pattern searches

These are intentionally preserved because omission is part of the method:

- **extraordinary exact-T₀ solar flare/CME** — not frozen at sufficient archival confidence;
- **exact ISS coordinates at T₀** — not recovered confidently enough;
- **packet-level DSN transmission at T₀** — schedule does not prove packet-level activity;
- **major OpenAI/Anthropic release at exact T₀** — not established from a sufficiently strong exact-time source;
- **weak same-day weather/cyclone items** — removed when archival verification was insufficient.

See [FACT_CHECK.md — Exclusions](./FACT_CHECK.md#j-deliberately-excluded-or-downgraded-claims).

## Publication guardrails

Never convert any of the following into evidence claims:

- “The eclipse validates the research.”
- “Echo I predicted Echo One.”
- “The universe arranged the publication.”
- “The UN summit was connected to the post.”
- “3:21 is evidence of a hidden pattern.”
- “NASA was transmitting our signal.”

Permitted framing:

> Independent records were reconstructed after the research was completed. Their interest lies in simultaneity, historical juxtaposition, and the documented order in which the relationships were noticed — not in causality.

---

**Ledger rule:** if a detail becomes more exciting when its qualification is removed, keep the qualification.