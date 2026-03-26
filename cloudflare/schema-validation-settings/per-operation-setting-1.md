# Get per-operation schema validation setting

`GET /zones/{zone_id}/schema_validation/settings/operations/{operation_id}`

Retrieves the schema validation settings configured for a specific API operation.

## Response

### 200

Success

_Empty object_

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
