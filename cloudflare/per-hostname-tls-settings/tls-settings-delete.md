# Delete TLS setting for hostname

`DELETE /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}`

Delete the tls setting value for the hostname.

## Parameters

- **zone_id** (string, required) [path]: 
- **setting_id** (string, required) [path]: 
- **hostname** (string, required) [path]: 

## Response

### 200

Delete TLS setting for hostname response

- **result** (object, optional): 

### 4XX

Delete TLS setting for hostname response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
