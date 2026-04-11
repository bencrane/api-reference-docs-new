# Validate API [Starter]

Validate companies against an Ideal Customer Profile. Uses the DiscoGen pipeline and requires an LLM provider integration.

Results are asynchronous; poll `GET /discogen/status/{task_id}` for completion.

## Endpoint

```
POST https://api.discolike.com/v1/validate/icp
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| icp_text | String | Yes | Your ICP description (e.g., "B2B SaaS companies in HR and payroll with 50-500 employees") |
| domains | Array | Yes | List of domains to validate (max 10,000) |
| context_mode | String | No | What data the LLM sees per domain: `website` (default, profile + homepage), `profile` (firmographics only), `domain` (name only) |
| integration_id | String | No | LLM provider integration UUID. Uses your default if omitted |
| web_search | Boolean | No | Enable web search enrichment (default: `false`) |
| search_provider_id | String | No | Search provider UUID for web search. Uses your default if omitted |

## Response

```json
{
  "task_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "column_name": ["Fit", "Confidence", "Reasoning"],
  "status": "in_progress",
  "total_domains": 3
}
```

## Result Schema (per domain)

| Column | Values | Description |
|--------|--------|-------------|
| Fit | `yes`, `partial`, `no` | Whether the company matches the ICP |
| Confidence | `high`, `medium`, `low` | Assessment confidence level |
| Reasoning | String | 1-2 sentence explanation |

## Example Request

```bash
curl -X POST https://api.discolike.com/v1/validate/icp \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "icp_text": "B2B SaaS companies providing HR and payroll solutions with 50-500 employees",
    "domains": ["gusto.com", "rippling.com", "stripe.com"]
  }'
```

## Polling for Results

```bash
curl https://api.discolike.com/v1/discogen/status/TASK_ID \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Example Completed Result

```json
{
  "task_id": "a1b2c3d4-...",
  "status": "completed",
  "results": {
    "gusto.com": {"Fit": "yes", "Confidence": "high", "Reasoning": "HR and payroll platform for SMBs, directly matches ICP"},
    "rippling.com": {"Fit": "yes", "Confidence": "high", "Reasoning": "HR, payroll, and IT platform for businesses, strong ICP match"},
    "stripe.com": {"Fit": "no", "Confidence": "high", "Reasoning": "Payment processing infrastructure, not HR/payroll"}
  }
}
```
