# Rate Limiting

To prevent misuse, we enforce a rate limit on an API Key and endpoint basis, similar to the way many other APIs enforce rate limits. By default, all accounts and their corresponding Test and Live API Keys have a rate limit of 150 requests per 5 seconds per endpoint. The `POST /v1/us_verifications` and `POST /v1/us_autocompletions` endpoints have a limit of 300 requests per 5 seconds for all accounts.

When your application exceeds the rate limit for a given API endpoint, the Lob API will return an HTTP 429 "Too Many Requests" response code instead of the variety of codes you would find across the other API endpoints.

## HTTP Headers

HTTP headers are returned on each request to a rate limited endpoint. Ensure that you inspect these headers during your requests as they provide relevant data on how many more requests your application is allowed to make for the endpoint you just utilized.

While the headers are documented here in titlecase, HTTP headers are case insensitive and certain libraries may transform them to lowercase. Please inspect your headers carefully to see how they will be represented in your chosen development scenario.

| Header | Description |
|--------|-------------|
| `X-Rate-Limit-Limit` | The rate limit ceiling for a given request. |
| `X-Rate-Limit-Remaining` | The number of requests remaining in this window. |
| `X-Rate-Limit-Reset` | The time at which the rate limit window resets (in UTC epoch seconds). |

## Example HTTP Headers

```
X-Rate-Limit-Limit:150
X-Rate-Limit-Remaining:100
X-Rate-Limit-Reset:1528749846
```

## Example Response

If you hit the rate limit on a given endpoint, this is the body of the HTTP 429 message that you will see:

```json
{
  "error": {
    "message": "Rate limit exceeded. Please wait 5 seconds and try your request again.",
    "code": "rate_limit_exceeded",
    "status_code": 429
  }
}
```