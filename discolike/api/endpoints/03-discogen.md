# DiscoGen API [Starter]

DiscoGen is an AI research agent that runs your prompt against rich company or contact data at scale. Each record gets its own isolated context window — company profile, homepage text, or contact details — so the model sees focused, accurate information rather than a polluted batch. Optionally enable web search for live data enrichment.

Requires an [LLM provider](../llm-providers/) integration. Optionally pair with a [search provider](../search-providers/) integration for BYOS (Bring Your Own Search) web search.

## Endpoints

```
POST   https://api.discolike.com/v1/discogen/process
POST   https://api.discolike.com/v1/discogen/process-personas
GET    https://api.discolike.com/v1/discogen/models
GET    https://api.discolike.com/v1/discogen/status/{task_id}
DELETE https://api.discolike.com/v1/discogen/cancel/{task_id}
```

## Common Parameters

Both `/process` and `/process-personas` share these parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| query | String | Yes | The prompt to run against each record |
| integration_id | String | No | LLM provider integration UUID. Uses your default LLM provider if omitted |
| web_search | Boolean | No | Enable web search enrichment (default: `false`). Returns 400 if no search provider is available and the model lacks built-in web search |
| search_provider_id | String | No | Search provider integration UUID for BYOS web search. Uses your default search provider if omitted |
| search_context_size | String | No | Number of search queries per record: `low` (default), `medium`, or `high` |
| include_x_search | Boolean | No | Include X (Twitter) search results for xAI models (default: `false`) |

## Process Domains

Run an LLM prompt against each domain with company context.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| domains | Array | Yes | Domains to process (max 10,000) |
| context_mode | String | No | What data the model sees per domain (default: `website`) |
| previous_discogen_data | Object | No | Previous DiscoGen results keyed by domain, appended to context for iterative enrichment |

### Domain Context Modes

Controls what data is included in each domain's context window. Richer context produces better results but costs more. Credits are only charged for new domains — any domain you've already discovered in the last 90 days is free.

| Mode | Context Included | Cost |
|------|------------------|------|
| `website` | Company profile (firmographics, keywords, categories) **+** homepage text | Credits (new domains only) + model fees |
| `profile` | Company profile only (firmographics, keywords, categories, summary) | Credits (new domains only) + model fees |
| `domain` | Domain name only — model relies on its own knowledge and web search if enabled | Model fees only |

### Example Request

```bash
curl -X POST "https://api.discolike.com/v1/discogen/process" \
  -H "x-discolike-key: API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What products or services does this company offer?",
    "domains": ["acmecorp.com", "globex.com"],
    "context_mode": "website"
  }'
```

### Example Response

```json
{
  "task_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "column_name": "Products and Services",
  "status": "in_progress",
  "total_domains": 2
}
```

## Process Personas

Run an LLM prompt against contact records. Same async task model as domain processing.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| persona_ids | Array | Yes | Persona IDs to process (max 10,000) |
| context_mode | String | No | What data the model sees per persona (default: `profile`) |
| previous_discogen_data | Object | No | Previous results keyed by persona ID for iterative enrichment |

### Persona Context Modes

Credits are only charged for new contacts — any contact you've already discovered in the last 90 days is free.

| Mode | Context Included | Cost |
|------|------------------|------|
| `full` | Contact profile + employer company profile + company homepage text | Credits (new contacts only) + model fees |
| `company` | Contact profile + employer company profile | Credits (new contacts only) + model fees |
| `profile` | Full contact profile (title, department, seniority, skills) | Credits (new contacts only) + model fees |
| `name_only` | Contact name and LinkedIn URL only — model relies on its own knowledge and web search | Model fees only |

### Example Request

```bash
curl -X POST "https://api.discolike.com/v1/discogen/process-personas" \
  -H "x-discolike-key: API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Is this person likely a decision-maker for software purchases?",
    "persona_ids": [12345, 67890],
    "context_mode": "full"
  }'
```

## List Models

Returns available LLM models grouped by provider, with web search support flags.

```bash
curl "https://api.discolike.com/v1/discogen/models" \
  -H "x-discolike-key: API_KEY"
```

```json
{
  "models": {
    "openai": [
      { "name": "gpt-4o", "supports_web_search": true },
      { "name": "gpt-4o-mini", "supports_web_search": false }
    ],
    "anthropic": [
      { "name": "claude-sonnet-4-6-20250514", "supports_web_search": false }
    ]
  }
}
```

## Task Lifecycle

Both process endpoints return a task that can be polled and cancelled.

### Check Status

```bash
curl "https://api.discolike.com/v1/discogen/status/{task_id}" \
  -H "x-discolike-key: API_KEY"
```

```json
{
  "status": "in_progress",
  "progress": 45,
  "interim_results": {
    "acmecorp.com": "Enterprise cloud security platform offering..."
  },
  "estimated_cost": 0.0032
}
```

### Final Response

```json
{
  "status": "completed",
  "progress": 100,
  "results": {
    "acmecorp.com": "Enterprise cloud security platform offering threat detection, SIEM, and compliance tools.",
    "globex.com": "Industrial supply chain management with logistics optimization and warehouse automation."
  },
  "estimated_cost": 0.0058,
  "response_format": {
    "response_type": "free_text",
    "description": "Products and services description",
    "field_labels": { "answer": "Products and Services" }
  }
}
```

### Cancel Task

```bash
curl -X DELETE "https://api.discolike.com/v1/discogen/cancel/{task_id}" \
  -H "x-discolike-key: API_KEY"
```

```json
{
  "success": true,
  "message": "Task cancellation requested",
  "task_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "status": "cancelling"
}
```
