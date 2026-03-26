# Get Single User

Retrieves information for a single user from the Sendoso platform using SCIM RFC standards.

**Endpoint:** `GET /api/scim/v2/Users`

## Request Body Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `userName` | string | Yes | The user's email address |
| `name` | object | Yes | Contains user name details |
| `name.givenName` | string | Yes | The user's first name |
| `name.familyName` | string | Yes | The user's last name |
| `userType` | string | Yes | The user's role. Values can be `sender`, `manager`, `admin` |
| `division` | string | Yes | The user's team. This value needs to match the exact team group name in Sendoso |

## Response Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `schemas` | array | Yes | The SCIM RFC schema - always `urn:ietf:params:scim:schemas:core:2.0:User` |
| `id` | string | Yes | The user's identifier |
| `userName` | string | Yes | The user's email address |
| `active` | boolean | Yes | Indicates if user is active on the platform |
| `name` | object | Yes | User name object with `givenName` and `familyName` |
| `emails` | array | Yes | Array containing user email address(es) |
| `emails[].value` | string | Yes | The user's email address |
| `userType` | string | Yes | User role (`sender`, `manager`, or `admin`) |
| `division` | string | Yes | The user's team |

## Example Response

```json
{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
  "id": "1000",
  "userName": "john.doe@sendoso.com",
  "active": true,
  "name": {
    "givenName": "John",
    "familyName": "Doe"
  },
  "emails": [
    { "value": "john.doe@sendoso.com" }
  ],
  "userType": "sender",
  "division": "Marketing Ops"
}
```
