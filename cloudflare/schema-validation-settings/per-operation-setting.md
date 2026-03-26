# Delete per-operation schema validation setting

`DELETE /zones/{zone_id}/schema_validation/settings/operations/{operation_id}`

Removes custom schema validation settings for a specific API operation, reverting to zone-level defaults.

## Response

### 200

Successfully deleted

_Empty object_

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
