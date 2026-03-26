# Get All Users

Retrieves all users from the Sendoso platform using SCIM RFC standards.

**Endpoint:** `GET /api/scim/v2/Users`

## Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `startIndex` | integer | The 1-based index of the first query result (default: 1) |
| `count` | integer | Non-negative integer. Specifies the desired maximum number of query results per page (default: 100, max: 100) |

## Response Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `schemas` | array | Yes | Always `urn:ietf:params:scim:api:messages:2.0:ListResponse` |
| `itemsPerPage` | integer | Yes | Number of results returned in current page |
| `startIndex` | integer | Yes | The 1-based index of the first result in the current set |
| `totalResults` | integer | Yes | Total matching results across all pages |
| `Resources` | array | Yes | Array of user objects |

### User Object

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | User identifier |
| `userName` | string | User's email address |
| `active` | boolean | Active status on Sendoso platform |
| `name.givenName` | string | First name |
| `name.familyName` | string | Last name |
| `emails` | array | Array with `value` property containing email |
| `userType` | string | Role: `sender`, `manager`, or `admin` |
| `division` | string | User's team assignment |

## Example Response

```json
{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
  "itemsPerPage": 2,
  "startIndex": 1,
  "totalResults": 100,
  "Resources": [
    {
      "id": "1000",
      "userName": "john.doe@sendoso.com",
      "active": false,
      "name": {
        "givenName": "John",
        "familyName": "Doe"
      },
      "emails": [{"value": "john.doe@sendoso.com"}],
      "userType": "sender",
      "division": "Marketing Ops"
    },
    {
      "id": "2000",
      "userName": "jane.doe@sendoso.com",
      "active": true,
      "name": {
        "givenName": "Jane",
        "familyName": "Doe"
      },
      "emails": [{"value": "jane.doe@sendoso.com"}],
      "userType": "admin",
      "division": "Sales"
    }
  ]
}
```
