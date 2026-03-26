# Update Fallback Origin for Custom Hostnames

`PUT /zones/{zone_id}/custom_hostnames/fallback_origin`

Updates the fallback origin configuration for custom hostnames on a zone. Sets the default origin server for custom hostname traffic.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **origin** (string, required): Your origin hostname that requests to your custom hostnames will be sent to.

## Response

### 200

Update Fallback Origin for Custom Hostnames response

- **result** (object, optional): 

### 4XX

Update Fallback Origin for Custom Hostnames response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
