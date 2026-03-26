# Enable validation for a schema

`PATCH /zones/{zone_id}/api_gateway/user_schemas/{schema_id}`

> **Deprecated**

Activates schema validation for an uploaded OpenAPI schema. Requests to matching endpoints will be validated against the schema definitions.

## Request Body

- **validation_enabled** (object, optional): 

## Response

### 200

Enable validation for a schema response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Enable validation for a schema response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
