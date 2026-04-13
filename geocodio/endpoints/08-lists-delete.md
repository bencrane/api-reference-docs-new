# Delete a List | Geocodio API

## Overview

Permanently delete a previously uploaded geocoding list and its underlying spreadsheet data. This can also be used to cancel and delete a list that is currently processing.

## Endpoint

```
DELETE https://api.geocod.io/v1.12/lists/{id}
```

## URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | integer | Yes | The list ID (path parameter) |
| `api_key` | string | Yes | Your Geocodio API key |

## Example Request

```bash
curl -X DELETE "https://api.geocod.io/v1.12/lists/42?api_key=YOUR_API_KEY"
```

## Example Response

```json
{
  "success": true
}
```

## Notes

- Geocodio Unlimited customers can cancel a list at any time.
- Pay as You Go customers can only cancel a list if it was recently started.
- Spreadsheet data is automatically deleted after 72 hours if not deleted manually first.
