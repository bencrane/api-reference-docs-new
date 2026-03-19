# US Verifications Test Env

When verifying US addresses, you'll likely want to test against a wide array of addresses to ensure you're handling responses correctly. With your test API key, requests that use specific values for `address` or `primary_line` and (if using `primary_line`) an arbitrary five digit number for `zip_code` (e.g. "11111") let you explore the responses to many types of addresses:

| ADDRESS TYPE FOR SAMPLE RESPONSE | DELIVERABILITY | SET `primary_line` OR `address` TO |
|---|---|---|
| Commercial highrise | `deliverable` | `commercial highrise` |
| Residential highrise | `deliverable` | `residential highrise` |
| Residential house | `deliverable` | `residential house` |
| PO Box | `deliverable` | `po box` |
| Rural route | `deliverable` | `rural route` |
| Puerto Rico address w/ urbanization | `deliverable` | `puerto rico` |
| Military address | `deliverable` | `military` |
| Department of state | `deliverable` | `department of state` |
| Generic deliverable | `deliverable` | `deliverable` |
| Missing a suite number | `deliverable_missing_unit` | `missing unit` |
| Suite number doesn't exist | `deliverable_incorrect_unit` | `incorrect unit` |
| Residential house with unnecessary suite number | `deliverable_unnecessary_unit` | `unnecessary unit` |
| Undeliverable and block matched | `undeliverable` | `undeliverable block match` |
| Undeliverable and no block matched | `undeliverable` | `undeliverable no match` |

See the `test` request & response examples under US Verification Examples within the "Verify a US or US territory address" section in US Verifications.

You can rely on the response from these examples generally matching the response you'd see in the live environment with an address of that type (excluding the `recipient` field).

The test API key does not perform any verification, automatic correction, or standardization for addresses. If you wish to try these features out, use our live demo or the free plan (see our pricing for details).