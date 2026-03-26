# Security

## Webhook Signature Verification

Every webhook and its metadata are signed with a unique key for each endpoint to prevent attackers from impersonating services.

### Implementation

Signature validation uses HMAC-SHA-256 with three components:

- **Webhook ID** - via `HTTP_SVIX_ID` header
- **Timestamp** - via `HTTP_SVIX_TIMESTAMP` header
- **Request body**

These are concatenated and signed, then compared against received signatures using constant-time comparison to prevent timing attacks.

## Replay Attack Mitigation

The system includes timestamp validation to block old or future webhook attempts. Webhooks with a timestamp that are more than five minutes away from the current time are automatically rejected. This requires synchronized server clocks using NTP.

## IP Allowlist (US)

For firewalled endpoints, allow traffic from:

- `44.228.126.217`
- `50.112.21.217`
- `52.24.126.164`
- `54.148.139.208`
- `2600:1f24:64:8000::/52`
