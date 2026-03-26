# Update multiple operation-level schema validation settings

`PATCH /zones/{zone_id}/api_gateway/operations/schema_validation`

> **Deprecated**

Updates multiple operation-level schema validation settings on the zone

## Request Body

_Empty object_

## Response

### 200

Update multiple operation-level schema validation settings response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update multiple operation-level schema validation settings response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
