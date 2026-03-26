# Delete Fallback Origin for Custom Hostnames

`DELETE /zones/{zone_id}/custom_hostnames/fallback_origin`

Removes the fallback origin configuration for custom hostnames on a zone. Custom hostnames without specific origins will no longer have a fallback.

## Parameters

- **zone_id** (string, required) [path]: 


## Response

### 200

Delete Fallback Origin for Custom Hostnames response

- **result** (object, optional): 

### 4XX

Delete Fallback Origin for Custom Hostnames response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
