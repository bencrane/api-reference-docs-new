# Errors | Geocodio API

## HTTP Status Codes

The Geocodio API employs semantic HTTP status codes.

| Error Code | Meaning |
|---|---|
| 200 OK | Request successful. This status code is also returned when no geocoding results were available |
| 403 Forbidden | Invalid API key, or other reason why access is forbidden |
| 422 Unprocessable Entity | A client error prevented the request from executing successfully (e.g. invalid address provided). A JSON object is returned with an `error` key containing the full error message |
| 429 Too Many Requests | You've reached the Pay as You Go rate limit. Inspect the `X-RateLimit-Remaining`, `X-RateLimit-Limit`, and `X-RateLimit-Period` HTTP headers and stop making requests until the end of the `X-RateLimit-Period` value |
| 500 Server Error | Something went wrong on the Geocodio server |

If you encounter unexpected errors, check [status.geocod.io](https://status.geocod.io) for the latest platform status updates.

### Error Response Format

Errors are returned as JSON with an `error` key.

**422 Unprocessable Entity example:**

```json
{
  "error": "Could not geocode address, zip code or city/state are required"
}
```

**403 Forbidden example (free tier exceeded):**

```json
{
  "error": "You can't make this request as it is above your daily maximum. You can configure billing at https://dash.geocod.io"
}
```

---

## Warnings

The Geocodio API implements warnings to assist developers during implementation. Warnings are represented with a `_warnings` key and can appear on an individual geocoding result or on the overall query.

If no warnings have been triggered, the `_warnings` key is not present in the JSON output.

### Query-Level Warning

Triggered when an unexpected parameter is used (e.g. `postalcode` instead of `postal_code`):

```json
{
  "input": {
    "..."
  },
  "results": [
    "..."
  ],
  "_warnings": [
    "Ignoring parameter \"postalcode\" as it was not expected. Did you mean \"postal_code\"? See full list of valid parameters here: https://www.geocod.io/docs/"
  ]
}
```

### Result-Level Warning

Triggered when a field append cannot be applied to a specific result (e.g. FFIEC on a city-level query):

```json
{
  "input": {
    "..."
  },
  "results": [
    {
      "...",
      "_warnings": [
        "ffiec field was skipped since result is not street-level"
      ]
    }
  ]
}
```

---

## CORS

The Geocodio API supports CORS using the `Access-Control-Allow-Origin` HTTP header. You can make requests directly to the API using JavaScript in the browser.

```html
<script>
const address = '1109 N Highland St, Arlington VA';
const apiKey = 'YOUR_API_KEY';
const url = `https://api.geocod.io/v1.12/geocode?q=${encodeURIComponent(address)}&api_key=${encodeURIComponent(apiKey)}`;

fetch(url)
  .then(response => response.json())
  .then(data => {
    console.log(data.results);
  })
  .catch(error => {
    console.error('Error:', error);
  });
</script>
```

> **Note:** This will expose your API key publicly. Make sure you understand and accept the implications of this approach, and consider setting usage limits on your account if applicable.
