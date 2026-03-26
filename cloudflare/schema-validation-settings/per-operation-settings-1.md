# Bulk edit per-operation schema validation settings

`PATCH /zones/{zone_id}/schema_validation/settings/operations`

Updates schema validation settings for multiple API operations in a single request. Efficient for applying consistent validation rules across endpoints.

## Request Body

_Empty object_

## Response

### 200

Update multiple operation-level schema validation settings response

_Empty object_

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
