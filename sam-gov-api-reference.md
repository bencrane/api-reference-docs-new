# SAM.gov API Reference

> Search entity registrations and download bulk entity extract files for companies registered to do business with the US government.

## Overview

The System for Award Management (SAM) APIs provide access to entity registrations. Use these APIs to search for registered contractors using NAICS codes, UEI, or registration date, and download monthly/daily bulk extract files.

**Base URL:** `https://api.sam.gov`

### Authentication

API Key is required. Pass it as a query parameter `api_key`.

| Header/Param  | Type   | Required | Description |
|---------------|--------|----------|-------------|
| `api_key`     | string | Yes      | Pass in the URL query string: `?api_key=YOUR_KEY` |

> *Note: Keys are obtained from your SAM.gov profile page (Workspace → Profile → Public API Key). Keys expire every 90 days and must be rotated.*

---

## Rate Limits

| Metric | Value | Reset Period |
|--------|-------|--------------|
| **Requests** | 1,000 | Daily (per non-federal individual account) |

If you hit limits while scraping, you will receive `429 Too Many Requests`. To sidestep limits on continuous sync operations, leverage the **Extracts API** to process bulk files instead of paginating the Entity Management Search API.

---

## APIs & Endpoints

### 1. Entity Management API
```http
GET /entity-information/v3/entities
```
Search entities by UEI, business name, NAICS code, registration date, state, business type, etc.

**Query Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | string | Yes | Your SAM.gov API Key. |
| `ueiSAM` | string | No | Unique Entity Identifier. |
| `legalBusinessName` | string | No | Filter by official business name. |
| `naicsCode` | string | No | Filter string for NAICS. |
| `registrationDate` | string | No | Filter by registration date. Supports ranges, e.g. `[2026-01-01, 2026-01-31]`. |
| `physicalAddressStateCode`| string| No| State code (e.g., `VA`, `TX`). |
| `purposeOfRegistrationCode`| string| No| Code corresponding to registration purpose (e.g. Z2 = All Awards). |
| `includeSections` | string | No | Comma-separated list of data sections (e.g. `entityRegistration,coreData`). |
| `format` | string | No | `json` or `csv`. (Default is JSON). |
| `offset` | integer| No | Pagination cursor/offset index. |

**Example Request**
```bash
curl -X GET 'https://api.sam.gov/entity-information/v3/entities?api_key=YOUR_API_KEY&naicsCode=33&registrationDate=[2026-02-13,2026-03-13]'
```

**Example Response**
```json
{
  "totalRecords": 1,
  "entityData": [
    {
      "entityRegistration": {
        "ueiSAM": "ABC123XYZ456",
        "legalBusinessName": "ACME MANUFACTURING",
        "registrationDate": "2026-02-15",
        "expirationDate": "2027-02-15",
        "purposeOfRegistrationCode": "Z2",
        "purposeOfRegistrationDesc": "All Awards"
      },
      "coreData": {
        "physicalAddress": {
          "addressLine1": "123 MAIN ST",
          "city": "AUSTIN",
          "stateOrProvinceCode": "TX",
          "zipCode": "78701",
          "countryCode": "USA"
        },
        "businessTypes": [
          {
            "businessTypeCode": "2X",
            "businessTypeDesc": "For Profit Organization"
          }
        ]
      }
    }
  ]
}
```

If requesting CSV format, the data payload will be comma-separated, which is favorable for streaming but trickier to parse nested sections.

---

### 2. Entity Extracts API
```http
GET /data-services/v1/extracts
```
Download bulk entity extract files. Available as daily deltas or monthly full dumps. Use this over standard API paginated requests to save your 1,000/day limit ceiling.

**Query Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | string | Yes | Your SAM.gov API Key. |
| `fileType` | string | Yes | Must be `ENTITY`. |
| `sensitivity` | string | Yes | Must be `PUBLIC`. |
| `frequency` | string | Yes | `DAILY` or `MONTHLY`. |
| `date` | string | No | Specific target date in `MM/DD/YYYY` format. |

#### Delta vs Monthly Extract Flow

- **Daily Deltas:** Processed Tuesday through Saturday. They contain any entities that were created or updated in the previous day. To ingest daily changes, poll this with `frequency=DAILY` and the current date (adjusting for timezones/weekends).
- **Monthly Full Dumps:** Generated on the 1st Sunday of each month. Contains ALL active records. Used for seeding a database from scratch.

#### Extract File Format (.dat)
The files returned are **pipe-delimited (.dat)**.
- Top-level separator: `|` (Pipe)
- Internal array separator: `~` (Tilde). 
  - *Example:* An entity might have multiple NAICS listed as `111110~222220~333330`.

You must implement a parser that splits by pipe, and then conditionally splits by tilde for repeating fields. Refer to the V2 Extract Layout PDF mapping for column indexes.

---

### 3. Get Opportunities API (Secondary)
```http
GET /opportunities/v2/search
```
Search active contract solicitations and RFPs. Useful to identify what companies are bidding on or what solicitations are available for your clients.

**Query Parameters (Highlights)**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | string | Yes | Your SAM.gov API Key. |
| `postedFrom` | string | No | `MM/DD/YYYY`. |
| `postedTo` | string | No | `MM/DD/YYYY`. |
| `ptype` | string | No | Procurement type (e.g. `p` for Presolicitation, `o` for Source Sought). |

---

## Best Practices

### Pagination (Entity Management)
Use `offset` limits to navigate standard JSON result sets when running lightweight queries. Since there is a cap of 1,000 requests per day, **do not** write ingestion scripts that aggressively paginate this endpoint without rate-limit awareness. 

### Data Ingestion Strategy
1. **Seed:** Pull the `MONTHLY` full dump from the Extracts API via `fileType=ENTITY`.
2. **Sync:** Run a daily chron job fetching the `DAILY` delta to upsert existing records or insert new registrations.
3. **Parse:** Implement a robust `.dat` pipe-delimited parser catering exactly to the V2 Extract Layout, handling `~` separations.
