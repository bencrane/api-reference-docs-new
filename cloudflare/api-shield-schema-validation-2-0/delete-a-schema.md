# Delete a schema

`DELETE /zones/{zone_id}/api_gateway/user_schemas/{schema_id}`

> **Deprecated**

Permanently removes an uploaded OpenAPI schema from API Shield schema validation. Operations using this schema will lose their validation rules.

## Response

### 200

Delete a schema response

_Empty object_

### 4XX

Delete a schema response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
