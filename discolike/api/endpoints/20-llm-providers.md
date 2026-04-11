# LLM Providers API [Starter]

Manage LLM provider integrations used by DiscoGen. Connect OpenAI, Anthropic, or any OpenAI-compatible endpoint (self-hosted models via LiteLLM, Ollama, etc.). See the Self-Hosting guide for setting up your own model.

## Endpoints

```
GET    https://api.discolike.com/v1/llm-providers/config
POST   https://api.discolike.com/v1/llm-providers/config
GET    https://api.discolike.com/v1/llm-providers/config/{integration_id}
PUT    https://api.discolike.com/v1/llm-providers/config/{integration_id}
DELETE https://api.discolike.com/v1/llm-providers/config/{integration_id}
POST   https://api.discolike.com/v1/llm-providers/test-connection
POST   https://api.discolike.com/v1/llm-providers/config/{integration_id}/set-default
```

## Integration Fields

| Field | Type | Description |
|-------|------|-------------|
| integration_id | UUID | Auto-generated unique identifier |
| integration_name | String | Human-readable name for this integration |
| provider | String | `openai`, `anthropic`, or `custom` (for self-hosted / BYOM) |
| api_key | String | Provider API key (masked as `*****` in responses) |
| model_name | String | Model identifier (e.g., `gpt-4o`, `claude-sonnet-4-6-20250514`, `openai/llama4:scout`) |
| base_url | String | Required for `custom` provider — your endpoint URL |
| supports_web_search | Boolean | Whether the model supports built-in web search |
| is_default | Boolean | Whether this is the default integration |
| model_deprecated | Boolean | Whether the model is no longer available |

## List Integrations

```shell
curl "https://api.discolike.com/v1/llm-providers/config" \
  -H "x-discolike-key: API_KEY"
```

```json
{
  "providers": [
    {
      "integration_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "integration_name": "GPT-4o",
      "provider": "openai",
      "api_key": "*****",
      "model_name": "gpt-4o",
      "base_url": null,
      "supports_web_search": true,
      "is_default": true,
      "model_deprecated": false
    }
  ],
  "mtime": "2026-03-28T12:00:00Z"
}
```

## Create Integration

```shell
curl -X POST "https://api.discolike.com/v1/llm-providers/config" \
  -H "x-discolike-key: API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "integration_name": "Claude Sonnet",
    "provider": "anthropic",
    "api_key": "sk-ant-...",
    "model_name": "claude-sonnet-4-6-20250514"
  }'
```

```json
{
  "message": "LLM integration 'Claude Sonnet' created successfully",
  "integration_id": "b2c3d4e5-f6a7-8901-bcde-f23456789012"
}
```

For custom/self-hosted providers, include `base_url`:

```shell
curl -X POST "https://api.discolike.com/v1/llm-providers/config" \
  -H "x-discolike-key: API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "integration_name": "Self-hosted Llama",
    "provider": "custom",
    "api_key": "your-litellm-key",
    "model_name": "openai/llama4:scout",
    "base_url": "https://your-tunnel.trycloudflare.com"
  }'
```

## Update Integration

Omit `api_key` to keep the existing key.

```shell
curl -X PUT "https://api.discolike.com/v1/llm-providers/config/{integration_id}" \
  -H "x-discolike-key: API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "integration_name": "GPT-4o (Updated)",
    "provider": "openai",
    "model_name": "gpt-4o"
  }'
```

## Delete Integration

Requires admin role.

```shell
curl -X DELETE "https://api.discolike.com/v1/llm-providers/config/{integration_id}" \
  -H "x-discolike-key: API_KEY"
```

## Test Connection

Validate a provider configuration before saving.

```shell
curl -X POST "https://api.discolike.com/v1/llm-providers/test-connection" \
  -H "x-discolike-key: API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "openai",
    "api_key": "sk-...",
    "model_name": "gpt-4o"
  }'
```

```json
{
  "status": "success",
  "message": "Connection to openai successful"
}
```

## Set Default

Sets an integration as the organization default. Requires admin role.

```shell
curl -X POST "https://api.discolike.com/v1/llm-providers/config/{integration_id}/set-default" \
  -H "x-discolike-key: API_KEY"
```
