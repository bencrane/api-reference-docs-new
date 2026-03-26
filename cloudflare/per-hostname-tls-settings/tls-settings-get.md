# Get TLS setting for hostname

`GET /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}`

Get the requested TLS setting for the hostname.

## Parameters

- **zone_id** (string, required) [path]: 
- **setting_id** (string, required) [path]: 
- **hostname** (string, required) [path]: 

## Response

### 200

Get TLS setting for hostname response

- **result** (object, optional): 

### 4XX

Get TLS setting for hostname response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
