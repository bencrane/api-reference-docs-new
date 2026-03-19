# Intl Verifications Test Env

When verifying international addresses, you'll likely want to test against a wide array of addresses to ensure you're handling responses correctly. With your test API key, requests that use specific values for `primary_line` let you explore the responses to many types of addresses:

| DELIVERABILITY OF SAMPLE RESPONSE | SET `primary_line` TO |
|---|---|
| `deliverable` | `deliverable` |
| `deliverable_missing_info` | `deliverable missing info` |
| `undeliverable` | `undeliverable` |
| `no_match` | `no match` |

See the `test` request & response examples under Intl Verification Examples within the "Verify an international address" section in Intl Verifications.

You can rely on the response from these examples generally matching the response you'd see in the live environment with an address of that type (excluding the `recipient` field).

The test API key does not perform any verification, automatic correction, or standardization for addresses. If you wish to try these features out, use our live demo or the free plan (see our pricing for details).