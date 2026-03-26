# Custom Hostname Details

`GET /zones/{zone_id}/custom_hostnames/{custom_hostname_id}`

Retrieves detailed information about a specific custom hostname, including SSL certificate status, ownership verification, and origin configuration.

## Parameters

- **custom_hostname_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Custom Hostname Details response

- **result** (object, optional): 

### 4XX

Custom Hostname Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
