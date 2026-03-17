# Company Search

## Overview
The Company Search endpoint enables discovery of companies matching specific ICP criteria including industry, size, location, and keywords, returning LinkedIn URLs for enrichment.

## Endpoint Details

| Property | Value |
|----------|-------|
| **Path** | `/v2/search/companies` |
| **Method** | POST |
| **Base URL** | `https://api.blitz-api.ai` |
| **Authentication** | Required via `x-api-key` header |
| **Rate Limit** | 5 requests per second (all plans) |

## Key Features

- **Pagination**: Cursor-based navigation where `cursor: null` indicates the first page. The next cursor value from responses enables paginated results.
- **Filter Logic**: All filters use AND logic between categories; multiple values within a single filter use OR logic.

## Request Parameters

### Company Search Criteria

| Parameter | Description |
|-----------|-------------|
| **Name** | Keyword-based search in company names (include/exclude arrays) |
| **Industry** | Exact matches from 500+ industry categories (include/exclude) |
| **Type** | Company classification (Public Company, Privately Held, Nonprofit, etc.) |
| **Employee Range** | Predefined brackets (1-10, 11-50, 51-200, etc.) |
| **Employee Count** | Numeric range search on LinkedIn employee data |
| **Keywords** | Description text search (include/exclude) |
| **Founded Year** | Numeric range filtering |
| **Headquarters** | City, country code, continent, and sales region filters |

### Response Configuration

| Parameter | Description |
|-----------|-------------|
| `max_results` | 1-50 (default: 10) |
| `cursor` | For pagination |

## Response Fields

Each company result includes:
- LinkedIn metadata (URL, ID, followers)
- Company details (name, type, size, industry)
- Location information (HQ city, state, country, region, continent)
- Additional data (domain, website, founded year, employee count)

## Example Request

```json
{
  "company": {
    "industry": {
      "include": ["Computer Software", "Information Technology"]
    },
    "employee_range": ["51-200", "201-500"],
    "hq": {
      "country_code": ["FR", "DE"]
    }
  },
  "max_results": 25,
  "cursor": null
}
```
