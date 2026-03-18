# Hypertide - Overview

## Hypertide Standalone API

`1.0.0` | `OAS 3.0`

---

## Overview

The Hypertide Standalone API provides programmatic access to order management, domain configuration, and payment functionality.

## Authentication

All authenticated endpoints require an API key in the `X-API-Key` header.

```
X-API-Key: your-api-key-here
```

## Rate Limits

| Endpoint | Limit |
|---|---|
| `/orders` | 30 requests/minute |
| `/orders/reinstate` | 20 requests/minute |
| `/subscriptions/cancel` | 20 requests/minute |
| `/payments/charge` | 20 requests/minute |
| `/domains/*` | 30-60 requests/minute |
| `/users/*` | 30 requests/minute |

## Dry Run Mode

Add `?dryRun=true` to any endpoint to test without making actual API calls. In dry run mode:

- No Airtable records are created/updated/deleted
- No external API calls (Stripe, DNS providers, etc.) are made
- Response shows what operations would be performed

**Example:**

```
POST /orders?dryRun=true
```

## Error Handling

All errors follow a consistent format:

```json
{
  "success": false,
  "error": "ERROR_CODE",
  "message": "Human readable message",
  "details": [...],
  "requestId": "req_..."
}
```

## Contact

Hypertide Support

## Servers

| Server | Description |
|---|---|
| `/api/v1` | Standalone API v1 |