# Get Fallback Origin for Custom Hostnames

`GET /zones/{zone_id}/custom_hostnames/fallback_origin`

Retrieves the current fallback origin configuration for custom hostnames on a zone. The fallback origin handles traffic when specific custom hostname origins are unavailable.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Fallback Origin for Custom Hostnames response

- **result** (object, optional): 

### 4XX

Get Fallback Origin for Custom Hostnames response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
