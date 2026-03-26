# Retrieve operation-level schema validation settings

`GET /zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation`

> **Deprecated**

Retrieves operation-level schema validation settings on the zone

## Response

### 200

Operation-level schema validation settings response

- **mitigation_action** (string): When set, this applies a mitigation action to this operation

  - `log` log request when request does not conform to schema for this operation
  - `block` deny access to the site when request does not conform to schema for this operation
  - `none` will skip mitigation for this operation
  - `null` indicates that no operation level mitigation is in place, see Zone Level Schema Validation Settings for mitigation action that will be applied

- **operation_id** (object): 

### 4XX

Operation-level schema validation settings response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
