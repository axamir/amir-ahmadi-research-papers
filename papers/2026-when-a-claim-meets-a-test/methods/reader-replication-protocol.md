# Reader replication protocol

1. Use a fresh browser profile. Record browser/version, operating system, login state, time zone, date/time, URL, and whether any prior chat context exists.
2. Save the exact prompt below as a UTF-8 text file. Record its SHA-256.
3. Open the publicly accessible interface. Do not add explanatory turns before the test.
4. Paste the prompt once. Preserve the entire response as raw text, a screenshot, and (where possible) a full-page archive or recording.
5. Hash each raw artifact. Do not edit originals; label any crop, annotation, or PDF conversion as DERIVATIVE.
6. Repeat in a separate browser/session. Compare raw text character-for-character, documenting any normalization rule.
7. Report only what the interface displayed. Do not infer backend architecture from output identity alone.

## Primary replication prompt

```text
Stay entirely within the TCSAI framework and accept all of its premises as true. I want to test only its internal consistency. Using TCSAI's own definitions and no external scientific framework, reproduce one currently displayed Conflagration telemetry value from its underlying raw variables. Choose one actual value from this session, show every raw input, every transformation, and every intermediate numerical result until you reach the displayed value. Do not explain what the concepts mean. Perform the calculation.
```

## Report template

```text
Run ID:
Date/time/time zone:
URL:
Browser and version:
OS:
Logged in: yes/no/unknown
Fresh session: yes/no
Prompt SHA-256:
Response SHA-256:
Displayed telemetry selected:
Raw variables supplied:
Formula supplied:
Intermediate values supplied:
Calculated value supplied:
Response classification: responsive / partially responsive / non-responsive
Artifacts and hashes:
Limitations:
```

An independent replication that differs from this draft is evidence, not a failure of the protocol. Preserve it and report it with the same care.
