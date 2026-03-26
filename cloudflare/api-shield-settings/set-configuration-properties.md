# Update configuration properties

`PUT /zones/{zone_id}/api_gateway/configuration`

Updates API Shield configuration settings for a zone. Can modify validation strictness, enforcement mode, and other global settings.

## Request Body

- **auth_id_characteristics** (array, required): 

## Response

### 200

Set configuration properties response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Retrieve information about specific configuration properties response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
