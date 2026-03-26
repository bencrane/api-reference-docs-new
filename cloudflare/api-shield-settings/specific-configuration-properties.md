# Retrieve information about specific configuration properties

`GET /zones/{zone_id}/api_gateway/configuration`

Gets the current API Shield configuration settings for a zone, including validation behavior and enforcement mode.

## Response

### 200

Retrieve information about specific configuration properties response

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
