# Get API Key Details

## Overview
The **Get API Key Details** endpoint serves as a health check for API key validity and account status before executing batch operations.

## Endpoint Details

| Property | Value |
|----------|-------|
| **Path** | `/v2/account/key-info` |
| **Method** | GET |
| **Base URL** | `https://api.blitz-api.ai` |
| **Authentication** | Required via `x-api-key` header |
| **Rate Limit** | 5 requests per second (all plans) |

## Response Information

### Success Response (200 OK)
Returns account status including:
- API key validity status
- Account ID
- Remaining credits balance
- Next credit reset timestamp
- Maximum requests per second allowance
- List of enabled API endpoints
- Active subscription plan details with start dates

### Error Responses

| Status | Description |
|--------|-------------|
| **401 Unauthorized** | Missing or invalid API key in header |
| **404 Not Found** | API key does not exist |
| **500 Internal Server Error** | Server-side processing failure |

## Security Scheme
Authentication mechanism: API Key passed via `x-api-key` header. Keys are obtainable from https://app.blitz-api.ai

## Pricing Context
All endpoints are unlimited on paid plans ($399+/mo). Free trial accounts receive 1,000 credits.
