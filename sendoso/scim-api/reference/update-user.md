# Update User

Modifies an existing user's information within the Sendoso platform.

**Endpoint:** `PATCH /api/scim/v2/Users/{user_id}`

## Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | integer | Yes | The user's identifier |

## Request Body Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | object | No | Contains the user's name information |
| `name.givenName` | string | No | The user's new first name |
| `name.familyName` | string | No | The user's new last name |
| `active` | boolean | No | Whether or not the user needs to be activated or deactivated from the Sendoso platform |
| `userType` | string | No | User role assignment. Permitted values: `sender`, `manager`, `admin` |
| `division` | string | No | The user's new team. This value needs to match the exact team group name in Sendoso |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `schemas` | array | Always returns `urn:ietf:params:scim:schemas:core:2.0:User` |
| `id` | string | User identifier |
| `userName` | string | User's email address |
| `active` | boolean | Account status on platform |
| `name` | object | Contains `givenName` and `familyName` |
| `emails` | array | Email objects with `value` field |
| `userType` | string | Role designation |
| `division` | string | Team assignment |

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
