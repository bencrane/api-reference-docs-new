# Rate Limits

The Sendoso SCIM API implements rate limiting mechanisms to ensure equitable resource distribution and prevent platform abuse.

## How It Works

Rate limiting operates by tracking the quantity of requests submitted by an application or user within specific time intervals. When a user exceeds their allocated request quota, the API responds with a `429 Too Many Requests` status code, temporarily preventing additional requests from that client.

## Key Points

- Rate limits apply per application/user account
- Exceeded limits trigger a `429` HTTP response
- Access is temporarily suspended following violations
- The system protects platform stability for all users
