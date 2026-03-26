# Update per-operation schema validation setting

`PUT /zones/{zone_id}/schema_validation/settings/operations/{operation_id}`

Fully updates schema validation settings for a specific API operation.

## Request Body

_Empty object_

## Response

### 200

Successfully updated

_Empty object_

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
