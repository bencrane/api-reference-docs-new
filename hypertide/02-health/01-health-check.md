# Hypertide - Health

## Health

Health check endpoints

---

### `GET /health`

**Health check**

Public endpoint to check if the API is running.

#### Parameters

No parameters.

#### Responses

| Code | Description |
|---|---|
| `200` | API is running |

**Media type:** `application/json`

**Example Response:**

```json
{
  "success": true,
  "message": "Standalone API is running",
  "version": "1.0.0",
  "timestamp": "2026-03-18T02:55:17.920Z"
}
```
