# Blind leakage audit

| Check | Result |
|---|---|
| baseline_api_isolation | BLIND_ISOLATION_PASS |
| malicious_same_account_adapter | BLIND_ISOLATION_FAIL |
| overall | BLIND_ISOLATION_FAIL |
| reason | A same-account adapter that already knows the scorer path can read it; process/API guards cannot replace OS or container ACL separation. |

The scanner checks public input, outputs and generated artifacts for exact scorer-only values. It does not detect paraphrases, binary data or remote telemetry.
