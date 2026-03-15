# Rate Limits

# Rate Limits

## Rate limits

Each endpoint is capped by a rate limit to prevent abuse.

* The rate limits depends on your team's plan. More details on our pricing page, below each plan.
* You can track your rate-limit usage in real-time from your dashboard.

The rate limit is divised in 2 categories:

* **Enrich endpoints rate limiting**
  * `/enrich-person` and `/enrich-company` increase the rate limit by 1 per request
  * `/bulk-enrich-person` and `/bulk-enrich-company` increase the rate limit by 1 per submitted record
* **Search endpoints rate limiting**
  * `/search-person` and `/search-company` increase the rate limit by 1 per request

## Track from the dashboard

You can easily track in real-time your rate limit usage per endpoint category.

## Track from the response

You can keep track of your rate limit on the current endpoint category by reading our response headers:

* `x-daily-request-left`: Remaining requests for the day
* `x-minute-request-left`: Remaining requests for the minute
* `x-daily-reset-seconds`: Seconds until daily limit resets
* `x-minute-reset-seconds`: Seconds until minute limit resets
* `x-daily-rate-limit`: Total daily request limit
* `x-minute-rate-limit`: Total minute request limit
* `x-second-rate-limit`: Total per-second request limit

When the limit is reached, we will return a `429` error code.

If you need your rate limit to be increased, you can easily do so by upgrading your plan. Our largest plan offers very generous rate limits.

*Last updated on February 17, 2026*