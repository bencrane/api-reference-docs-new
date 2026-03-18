# Hypertide - Reupload Orders

### `POST /orders/reupload`

**Reupload completed orders**

Marks completed orders for reupload by updating their status.

**Validation checks:**

- Record must exist in Airtable (valid `recordId`)
- Record must belong to the authenticated client
- Record Status must be `"Done"` (completed orders only)

**On success, updates:**

- Status = `"In progress"`
- Item Status = `"Users Created"`

#### Parameters

No parameters.

#### Request Body

**Media type:** `application/json`

```json
{
  "recordIds": [
    "recXXXXXXXXXXXXXX",
    "recYYYYYYYYYYYYYY"
  ]
}
```

#### Responses

| Code | Description |
|---|---|
| `200` | Reupload processed successfully |
| `400` | Validation failed or all records failed |
| `401` | API key required |
| `403` | Permission denied |

**`200` - Reupload processed successfully**

**Media type:** `application/json`

```json
{
  "success": true,
  "message": "Successfully marked 2 order(s) for reupload",
  "results": {
    "success": [
      {
        "recordId": "string",
        "domain": "string",
        "message": "string"
      }
    ],
    "failed": [
      {
        "recordId": "string",
        "domain": "string",
        "error": "INVALID_RECORD_ID",
        "message": "string"
      }
    ]
  },
  "requestId": "string"
}
```

**`400` - Validation failed or all records failed**

**Media type:** `application/json`

```json
{
  "success": false,
  "error": "MISSING_RECORD_IDS",
  "message": "string",
  "results": {}
}
```
