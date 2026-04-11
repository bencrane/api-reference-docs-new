# Search Providers API [Starter]

Manage search provider integrations used by DiscoGen for web search enrichment (BYOS — Bring Your Own Search). When web search is enabled in DiscoGen, search queries are run against your configured provider to supplement domain data with live web results. Supported providers include Tavily, Serper, Parallel AI, and Linkup.

## Endpoints

```
GET    https://api.discolike.com/v1/search-providers
POST   https://api.discolike.com/v1/search-providers
PUT    https://api.discolike.com/v1/search-providers/{integration_id}
DELETE https://api.discolike.com/v1/search-providers/{integration_id}
PUT    https://api.discolike.com/v1/search-providers/{integration_id}/default
DELETE https://api.discolike.com/v1/search-providers/{integration_id}/default
GET    https://api.discolike.com/v1/search-providers/models
```

## Integration Fields

| Field | Type | Description |
|-------|------|-------------|
| integration_id | UUID | Auto-generated unique identifier |
| integration_name | String | Human-readable name for this integration |
| provider | String | Provider identifier (e.g., `tavily`, `serper`) |
| search_model | String | LiteLLM model key (e.g., `tavily/search`, `serper/search`) |
| api_key | String | Provider API key (masked as `*****` in responses) |
| base_url | String | Custom endpoint URL (for LiteLLM Proxy setups) |
| is_default | Boolean | Whether this is the default search provider |
| cost_per_query | Float | Cost per search query in USD |

## List Integrations

```shell
curl "https://api.discolike.com/v1/search-providers" \
  -H "x-discolike-key: API_KEY"
```

```json
{
  "providers": [
    {
      "integration_id": "c3d4e5f6-a7b8-9012-cdef-345678901234",
      "integration_name": "Serper",
      "provider": "serper",
      "search_model": "serper/search",
      "api_key": "*****",
      "base_url": null,
      "is_default": true,
      "cost_per_query": 0.001
    }
  ]
}
```

## Create Integration

The provider is validated with a test search before saving.

```shell
curl -X POST "https://api.discolike.com/v1/search-providers" \
  -H "x-discolike-key: API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "integration_name": "Tavily Search",
    "provider": "tavily",
    "search_model": "tavily/search",
    "api_key": "tvly-..."
  }'
```

## Update Integration

Omit `api_key` to keep the existing key. Re-validates if provider, model, or base URL changes.

```shell
curl -X PUT "https://api.discolike.com/v1/search-providers/{integration_id}" \
  -H "x-discolike-key: API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "integration_name": "Tavily (Renamed)",
    "provider": "tavily",
    "search_model": "tavily/search"
  }'
```

## Delete Integration

Requires admin role.

```shell
curl -X DELETE "https://api.discolike.com/v1/search-providers/{integration_id}" \
  -H "x-discolike-key: API_KEY"
```

## Set Default

Sets a search provider as the organization default. Requires admin role.

```shell
curl -X PUT "https://api.discolike.com/v1/search-providers/{integration_id}/default" \
  -H "x-discolike-key: API_KEY"
```

## Clear Default

Removes the default flag from a search provider, leaving the organization with no default. Only works if the specified integration is currently the default. Requires admin role.

```shell
curl -X DELETE "https://api.discolike.com/v1/search-providers/{integration_id}/default" \
  -H "x-discolike-key: API_KEY"
```

## List Available Models

Returns all search models supported by the platform, grouped by provider with cost info.

```shell
curl "https://api.discolike.com/v1/search-providers/models" \
  -H "x-discolike-key: API_KEY"
```

```json
{
  "models": {
    "serper": [
      { "name": "serper/search", "cost_per_query": 0.001 }
    ],
    "tavily": [
      { "name": "tavily/search", "cost_per_query": 0.005 }
    ]
  }
}
```
