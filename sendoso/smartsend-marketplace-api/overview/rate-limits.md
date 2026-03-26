# Rate Limits

The Sendoso Marketplace and SmartSend APIs implement rate limiting to ensure equitable resource distribution and prevent misuse.

## Rate Limit Details

**Current Threshold:** 100 requests per minute per user

When users exceed this limit, the system responds with a `429 Too Many Requests` HTTP status code, temporarily preventing further API calls from that user.

## Response Headers

The API includes an `X-Rate-Limit-Reset` header in responses that shows when the rate limit window will refresh. This timestamp helps developers plan retry logic and understand when their quota resets.
