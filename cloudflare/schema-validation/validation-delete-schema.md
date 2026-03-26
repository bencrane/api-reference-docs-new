# Delete a schema

`DELETE /zones/{zone_id}/schema_validation/schemas/{schema_id}`

Permanently removes an uploaded OpenAPI schema from API Shield. Operations using this schema will lose their validation rules.

## Response

### 200

Success

- **result** (object, optional): 

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
