# Edit details of a schema to enable validation

`PATCH /zones/{zone_id}/schema_validation/schemas/{schema_id}`

Modifies an existing OpenAPI schema in API Shield, updating the validation rules for associated API operations.

## Request Body

- **validation_enabled** (boolean, optional): Flag whether schema is enabled for validation.

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
