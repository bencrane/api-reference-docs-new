# Authentication | DiscoLike API

## Base URL

API requests should be directed to:

```
https://api.discolike.com/v1/
```

## OpenAPI Specification

The complete API specification is available at [api.discolike.com/v1/openapi.json](https://api.discolike.com/v1/openapi.json).

## API Keys

DiscoLike employs API keys as the authentication mechanism. You can generate and administer your keys through the [account management dashboard](https://app.discolike.com/account/management/keys).

When making requests, include your API key within the `x-discolike-key` header:

```terminal
curl "https://api.discolike.com/v1/discover?keyword=fintech" \
  -H "x-discolike-key: YOUR_API_KEY"
```

**Important note:** All API keys for the same account share rate limits.
