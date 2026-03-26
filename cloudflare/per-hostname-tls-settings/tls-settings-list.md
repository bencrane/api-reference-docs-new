# List TLS setting for hostnames

`GET /zones/{zone_id}/hostnames/settings/{setting_id}`

List the requested TLS setting for the hostnames under this zone.

## Parameters

- **zone_id** (string, required) [path]: 
- **setting_id** (string, required) [path]: 

## Response

### 200

List per-hostname TLS settings response

- **result** (array, optional): 
- **result_info** (object, optional): 

### 4XX

List per-hostname TLS settings response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
