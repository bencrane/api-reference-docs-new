# List Keyless SSL Configurations

`GET /zones/{zone_id}/keyless_certificates`

List all Keyless SSL configurations for a given zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List Keyless SSL Configurations response

- **result** (array, optional): 

### 4XX

List Keyless SSL Configurations response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
