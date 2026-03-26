# Rate Limits

Sendoso implements rate limiting to manage platform resources equitably and prevent misuse of their API infrastructure.

## How Rate Limiting Works

The system tracks the volume of requests from an application or user during specific time windows. When usage exceeds thresholds, the API responds with a `429 Too Many Requests` status code, temporarily preventing additional requests from that source.

## Key Points

- Rate limits are enforced per application/user within defined periods
- Exceeding limits triggers a `429` HTTP response
- Access becomes temporarily restricted after limit breach
- The mechanism protects shared resources across all API users
