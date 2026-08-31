# Initial Analysis Notes

## Scope

These notes summarize the first reconstruction from Apple Screen Time screenshots and verified public space-weather bulletins. They are exploratory and should not be treated as causal results.

## Behavioral change

Using Mac Screen Time as a coarse behavioral proxy:

- Aug 15–22 average total Mac activity: approximately **9 h 29 min/day**.
- Aug 23–30 average total Mac activity: approximately **5 h 27 min/day**.
- Approximate decline: **42.6%**.

By contrast, Productivity & Finance time declined much less over the same windows:

- Aug 15–22 average: approximately **3 h 46 min/day**.
- Aug 23–30 average: approximately **3 h 31 min/day**.
- Approximate decline: **6.7%**.

This pattern is more consistent with a reduction in sustained engagement or endurance than a complete disappearance of productive capacity. Screen Time categories are coarse, however, and cannot establish cognitive state.

## iPhone composition matters more than total time

On Aug 30, total iPhone Screen Time was approximately **12 h 54 min**. Social plus Entertainment accounted for approximately **11 h 24 min (88.4%)**.

On Aug 10, total iPhone Screen Time was even higher at approximately **16 h 20 min**, but approximately **9 h 25 min** was categorized as Productivity & Finance.

Therefore total Screen Time alone is a poor proxy for cognitive function. Behavioral composition, fragmentation, timing, and persistence are likely more informative.

## Counterexample to the simple geomagnetic hypothesis

The simple hypothesis `higher geomagnetic activity -> lower functioning` is weakened by Aug 18–19.

Public SIDC bulletins report minor-storm intervals around Kp 5 / G1 during Aug 18–19, while reconstructed Mac activity remained high:

- Aug 18: approximately **11 h 22 min** total Mac activity.
- Aug 19: approximately **11 h 24 min** total Mac activity.

This demonstrates that geomagnetic activity at approximately G1 levels was **not sufficient** to produce the later observed behavioral pattern.

## Timing problem

The notable Aug 25 solar flare sequence and possible CME effects do not align cleanly with the retrospective onset of the behavioral anomaly. SIDC reported quiet global geomagnetic conditions for the preceding 24 hours in bulletins issued Aug 27 and Aug 28, while the behavioral change appears to have begun earlier.

This weakens a simple direct temporal-causality account.

## Current interpretation

The present evidence supports three separate statements:

1. A behavioral state change appears in the device-use record.
2. Real solar and geomagnetic events occurred during the same broad period.
3. The available evidence does **not** establish that those events caused the behavioral change.

The central methodological distinction remains:

> **Anomaly Detection != Causal Identification**

## Next tests

Future analysis should pre-register exposure variables (Kp, Dst, IMF Bz, solar-wind speed and density), use fixed lag windows (0, 6, 12, 24 h), preserve negative controls, and avoid adding variables or lags after inspecting correlations.
