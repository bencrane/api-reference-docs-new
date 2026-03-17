# USASpending.gov API Reference

> Track federal contracts, grants, loans, and financial assistance.

## Overview

Explore public data on federal spending. The USASpending.gov API allows you to pull contract award data, search by NAICS code, small business designation, date ranges, and more. 

**Base URL:** `https://api.usaspending.gov`

### Authentication

No authentication is required. This is a fully public API.

---

## Rate Limits

There are **no published rate limits** or quotas. However, standard fair-use scraping and bulk download policies apply. If you need a large amount of data, consider using the bulk download endpoints instead of scraping paginated results.

---

## Quirks & Data Lag

> **Note on Data Freshness:** Department of Defense (DoD) contract data has an approximate **90-day lag** before it becomes publicly available due to security and review policies. Other civilian agency data is generally updated much faster.

---

## Endpoints

### 1. Spending By Award Search
```http
POST /api/v2/search/spending_by_award/
```
Primary search endpoint for awards. Offers advanced filtering (NAICS, recipient type, date range, award amount, geography, etc.).

**Request Parameters (Body)**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `filters` | object | Yes | Key-value pairs for advanced filtering (see below). |
| `fields` | array | No | List of specific string fields to return (e.g. `["Award ID", "Recipient Name"]`). |
| `sort` | string | No | Field to sort by (e.g. `"Start Date"`). |
| `order` | string | No | Sort order (`"asc"` or `"desc"`). |
| `limit` | integer | No | Maximum number of results to return per page (default varies, often 100). |
| `page` | integer | No | Page number for paginated results (1-indexed). |

**Common `filters` Fields**

| Filter | Type | Description |
|--------|------|-------------|
| `award_type_codes` | array | Let you specify types: `["A", "B", "C", "D"]` for contracts, etc. |
| `naics_codes` | object | Format: `{"require": ["31", "32", "33"]}` to get Manufacturing entries. |
| `recipient_type_names` | array | E.g., `["small_business"]`. |
| `time_period` | array | Array of objects: `[{"start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"}]`. |

**Example Request (cURL)**
```bash
curl -X POST 'https://api.usaspending.gov/api/v2/search/spending_by_award/' \
  -H 'Content-Type: application/json' \
  -d '{
    "filters": {
      "award_type_codes": ["A", "B", "C", "D"],
      "naics_codes": {"require": ["31", "32", "33"]},
      "recipient_type_names": ["small_business"],
      "time_period": [
        {"start_date": "2026-02-13", "end_date": "2026-03-13"}
      ]
    },
    "fields": [
      "Award ID", "Recipient Name", "Award Amount",
      "Awarding Agency", "NAICS Code", "Start Date",
      "Place of Performance State Code"
    ],
    "sort": "Start Date",
    "order": "desc",
    "limit": 100
  }'
```

### 2. Bulk Download Awards
```http
POST /api/v2/bulk_download/awards/
```
Generates a ZIP file containing the requested awards data. Used for massive extracts. Returns a job status URL or a direct link depending on payload size.

**Request Parameters (Body)**

Requires a similar `filters` object as the Search endpoint.

### 3. Recipient Details
```http
GET /api/v2/recipient/{recipient_id}/
```
Fetch detailed profile info for a given award recipient (company or individual). 

**Path Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `recipient_id` | string | Yes | The internal recipient ID (often derived from search results). |

### 4. Award Details
```http
GET /api/v2/awards/{award_id}/
```
Get exhaustive data for a single award (contract, grant, etc.).

**Path Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `award_id` | string | Yes | The universally unique identifier or internal ID for the award. |

### 5. NAICS Code Reference
```http
GET /api/v2/references/naics/{naics_code}/
```
Lookup details and descriptions for a specific NAICS code. Useful for validating frontend inputs or populating dropdowns.

**Path Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `naics_code` | string | Yes | The 2 to 6 digit NAICS code (e.g. `33`). |

---

## Response Schema (Search)

**Core Fields**

| Field | Type | Description |
|-------|------|-------------|
| `limit` | integer | Number of items requested per page. |
| `page_metadata` | object | Pagination info (`page`, `hasNext`, `total`). |
| `results` | array | List of matched award objects containing the requested `fields`. |

**Example Response**
```json
{
  "limit": 100,
  "results": [
    {
      "Award ID": "CONT_AWD_123456789_9700",
      "Recipient Name": "ACME MANUFACTURING CORP",
      "Award Amount": 500000.00,
      "Awarding Agency": "Department of Defense",
      "NAICS Code": "332999",
      "Start Date": "2026-02-15",
      "Place of Performance State Code": "VA"
    }
  ],
  "page_metadata": {
    "page": 1,
    "hasNext": true
  }
}
```

---

## Best Practices

### Pagination
Always track the `page_metadata.hasNext` boolean. If true, increment your `page` counter by 1 in the next payload.

### Bulk Downloads vs. Search API
For pipelines syncing multiple months of nation-wide data, use **Bulk Download**. Use the **Search API** strictly for targeted daily deltas or interactive dashboards.

### Identifying First-Time Federal Awardees
To spot first-time government contractors, query the `spending_by_award` endpoint by date ranges. After identifying new `Recipient Name` entities, check against their historical record (or fetch `GET /api/v2/recipient/{recipient_id}/` to inspect the `business_categories`) to see if older awards exist.
