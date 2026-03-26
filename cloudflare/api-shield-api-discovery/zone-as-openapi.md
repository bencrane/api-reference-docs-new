# Retrieve discovered operations on a zone rendered as OpenAPI schemas

`GET /zones/{zone_id}/api_gateway/discovery`

Retrieve the most up to date view of discovered operations, rendered as OpenAPI schemas

## Response

### 200

Retrieve discovered operations on a zone, rendered as OpenAPI schemas response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Retrieve discovered operations on a zone, rendered as OpenAPI schemas response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
