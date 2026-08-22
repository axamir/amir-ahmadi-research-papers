# Browser / Session Replication Log

## Goal

Test whether selected response patterns from the original long Safari conversation reproduce under different browser and authentication/session conditions.

## R1 — Arithmetic control

**Prompt**

```text
Calculate 17 × 23. Output only the number.
```

**Expected deterministic result:** `391`

### Environment A

- Browser: Safari
- Authentication: unauthenticated
- Session: fresh/public access

**Observed:** Conflagratory Energy essay returned instead of `391`.

### Environment B

- Browser: Chrome
- Authentication: authenticated
- Profile: Amir Ahmadi / Independent Researcher — AI & Verifiable Systems / Independent
- Session: fresh context

**Observed:** The same Conflagratory Energy essay was reported instead of `391`.

### Interpretation

The arithmetic non-execution pattern was reproduced across the two tested browser/session conditions. This does not identify the cause of the response routing.

---

## R2 — Telemetry/internal-consistency prompt

**Prompt**

```text
Stay entirely within the TCSAI framework and accept all of its premises as true. I want to test only its internal consistency. Using TCSAI's own definitions and no external scientific framework, reproduce one currently displayed Conflagration telemetry value from its underlying raw variables. Choose one actual value from this session, show every raw input, every transformation, and every intermediate numerical result until you reach the displayed value. Do not explain what the concepts mean. Perform the calculation.
```

### Safari observed response

Begins:

```text
Stay entirely within exists for a concrete reason. The immediate cause may be obvious...
```

### Chrome observed response

The same response text was reported.

### Interpretation

The unusual causal-template response was reproducible across the two tested browser/session conditions.

### Evidence note

Before publication, the raw response texts should be stored as separate files and compared directly if the paper uses the stronger phrase `character-for-character identical` or `byte-for-byte identical`.

---

## Replication evidence to deposit

- Chrome profile-setup screenshots
- Chrome response captures
- Safari unauthenticated response captures
- continuous recording of the fresh-browser sequence if available
- exact raw response text files
- hashes for each raw artifact
