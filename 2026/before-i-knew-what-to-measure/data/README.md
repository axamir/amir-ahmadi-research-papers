# Data

This directory will contain structured datasets extracted from the source evidence and external space-weather records.

## Planned files

- `behavioral-daily.csv` — day-level Mac/iPhone activity summary
- `behavioral-hourly.csv` — hourly activity reconstruction where source evidence supports it
- `space-weather.csv` — predefined environmental variables aligned to a common time base
- `analysis-matrix.csv` — joined behavioral/environmental analysis table

## Proposed behavioral schema

Suggested columns include:

- date_local
- device
- total_screen_time_minutes
- productivity_finance_minutes
- social_minutes
- entertainment_minutes
- social_entertainment_fraction
- first_active_hour
- last_active_hour
- active_hours_count
- fragmentation_proxy
- evidence_file
- transcription_confidence
- notes

## Proposed environmental schema

Suggested columns include:

- timestamp_utc
- timestamp_local
- kp
- dst_nt
- imf_bz_nt
- solar_wind_speed_km_s
- solar_wind_density_cm3
- source
- source_status

Forecast values and observed values must be stored separately and never substituted for each other.

## Data status

The current paper contains an initial manual reading of selected screenshots. A complete structured transcription and source-linked audit pass remains pending.
