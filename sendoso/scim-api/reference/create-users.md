# Create User

Establishes a new user in the system and assigns them a specific role and team.

**Endpoint:** `POST /api/scim/v2/Users`

## Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `userName` | string | Yes | The user's email address used as their unique identifier |
| `name` | object | Yes | Contains the user's name information |
| `name.givenName` | string | Yes | First name |
| `name.familyName` | string | Yes | Last name |
| `userType` | string | Yes | The user's role. Values can be `sender`, `manager`, `admin` |
| `division` | string | Yes | The user's team. This value needs to match the exact team group name in Sendoso |

## Response Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `schemas` | array | Yes | The SCIM RFC schema - always `urn:ietf:params:scim:schemas:core:2.0:User` |
| `id` | string | Yes | The system-generated user identifier |
| `userName` | string | Yes | The registered email address |
| `active` | boolean | Yes | Platform activation status indicator |
| `name` | object | Yes | Contains `givenName` and `familyName` fields |
| `emails` | array | Yes | Array containing email objects with a `value` field |
| `userType` | string | Yes | Assigned role category |
| `division` | string | Yes | Team affiliation |

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
  "emails": [{ "value": "john.doe@sendoso.com" }],
  "userType": "sender",
  "division": "Marketing Ops"
}
```
