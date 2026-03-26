# Pagination

The Sendoso API enables pagination through query parameters for GET endpoints that return multiple resources. This functionality facilitates retrieval of large datasets in manageable portions.

## Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `page` | integer | Specifies which page of results to retrieve. First page starts at 1. |
| `per_page` | integer | Defines how many resources appear per page. |

## Example Request

To fetch campaigns starting from page 2 with 50 items per page:

```
GET https://app.sendoso.com/campaigns?page=2&per_page=50
```

## Response Structure

Paginated responses include metadata fields:

| Field | Type | Description |
|-------|------|-------------|
| `current_page` | integer | The current page number being returned |
| `per_page` | integer | Resources displayed per page |
| `total_{resource}` | integer | Total count of available resources |

### Sample Response

```json
{
  "campaigns": [...],
  "current_page": 2,
  "per_page": 50,
  "total_campaigns": 234
}
```
