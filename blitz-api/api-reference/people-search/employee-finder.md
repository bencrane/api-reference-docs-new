# Employee Finder

## Overview
The Employee Finder endpoint enables browsing of all employees at a single company with filtering capabilities by job level, department, location, and seniority.

## Endpoint Details

| Property | Value |
|----------|-------|
| **Path** | `/v2/search/employee-finder` |
| **Method** | POST |
| **Base URL** | `https://api.blitz-api.ai` |
| **Authentication** | Required via `x-api-key` header |
| **Rate Limit** | 5 requests per second (all plans) |

## Request Parameters

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `company_linkedin_url` | string | Company's LinkedIn profile URL |

### Optional Filters

| Parameter | Type | Description |
|-----------|------|-------------|
| `country_code` | array | Country codes (e.g., US, FR) |
| `continent` | array | Africa, Asia, Europe, North America, Oceania, South America |
| `sales_region` | array | NORAM, LATAM, EMEA, APAC |
| `job_level` | array | C-Team, Director, Manager, VP, Staff, Other |
| `job_function` | array | 21 categories from Engineering to Writing/Editing |
| `min_connections_count` | number | 0-500 range |
| `max_results` | number | Results per page (max 50, default 50) |
| `page` | number | Page number for pagination |

## Response Format

Person data appears directly in `results[]` array (not nested). Each person includes:
- Name, location, LinkedIn URL
- Experience history with current job status
- Education credentials
- Skills list
- Profile picture and connections count

### Pagination
Page-based. Increment `page` until `page > total_pages`.

## Example Request

```json
{
  "company_linkedin_url": "https://www.linkedin.com/company/openai",
  "job_level": ["VP", "Director"],
  "job_function": ["Sales & Business Development"],
  "country_code": ["US"],
  "max_results": 10,
  "page": 1
}
```

## Error Responses

| Status | Description |
|--------|-------------|
| **402** | Insufficient credits |
| **422** | Invalid input |
| **500** | Server error |

## Enrichment Integration
Chain Employee Finder results with enrichment endpoints:
- `/v2/enrichment/email` - Get verified emails
- `/v2/enrichment/phone` - Get phone numbers (US only)
