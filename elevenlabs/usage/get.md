# Get character usage metrics

**GET** `https://api.elevenlabs.io/v1/usage/character-stats`

## Overview

This endpoint retrieves usage metrics for the current user or their workspace. It provides a time-based axis with aggregated usage data broken down by specified categories.

## Required Parameters

- **start_unix** (integer): UTC Unix timestamp in milliseconds marking the window start at 00:00:00
- **end_unix** (integer): UTC Unix timestamp in milliseconds marking the window end at 23:59:59

## Optional Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| include_workspace_metrics | boolean | Include entire workspace statistics (default: false) |
| breakdown_type | string | Category for breakdown: none, voice, voice_multiplier, user, groups, api_keys, all_api_keys, product_type, model, resource, request_queue, region, subresource_id, reporting_workspace_id, has_api_key, request_source |
| aggregation_interval | string | Time aggregation: hour, day, week, month, or cumulative (default: day) |
| aggregation_bucket_size | integer | Override aggregation interval with bucket size in seconds |
| metric | string | Metric to aggregate: credits, tts_characters, minutes_used, request_count, ttfb_avg, ttfb_p95, fiat_units_spent, concurrency, concurrency_average |
| xi-api-key | string | API key header (optional) |

## Response

Success (200):
```json
{
  "time": [array of unix timestamps],
  "usage": {object with breakdown categories and usage arrays}
}
```

Error (422): Validation error details

## Available Servers

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`
