# Get All Team Groups

Retrieves information about all active team groups within an organization.

**Endpoint:** `GET /api/v3/groups`

## Request Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `page` | integer | Page number for results (first page = 1) |
| `per_page` | integer | Results per page, maximum 100 |

## Response Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `current_page` | integer | Yes | Current page being returned |
| `per_page` | integer | Yes | Number of results per page |
| `total_groups` | integer | Yes | Total count of team groups |
| `groups` | array | Yes | List of team group objects |

### Team Group Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | Team group identifier |
| `budget` | integer | Yes | Team group budget |
| `created_at` | string | Yes | Creation date (ISO 8601 format) |
| `monthly_budget` | string | Yes | Monthly allocated budget |
| `name` | string | Yes | Team group name |
| `one_time_budget` | integer | Yes | One-time budget amount |
| `rollover` | boolean | Yes | Whether monthly budget carries over |
| `team_id` | integer | Yes | Organization identifier |
| `updated_at` | string | Yes | Last updated date (ISO 8601 format) |

## Example Response

```json
{
  "current_page": 1,
  "per_page": 1,
  "total_groups": 20,
  "groups": [
    {
      "id": 1234,
      "budget": 50,
      "created_at": "2020-05-01T13:53:05.000-07:00",
      "monthly_budget": "50000",
      "name": "Field Marketing",
      "one_time_budget": 0,
      "rollover": true,
      "team_id": 5678,
      "updated_at": "2022-09-26T11:49:50.000-07:00"
    }
  ]
}
```
