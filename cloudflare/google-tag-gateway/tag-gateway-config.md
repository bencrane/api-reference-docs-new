# Get Google Tag Gateway configuration

`GET /zones/{zone_id}/settings/google-tag-gateway/config`

Gets the Google Tag Gateway configuration for a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Google Tag Gateway configuration response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): Google Tag Gateway configuration for a zone.

### 4XX

Get Google Tag Gateway configuration response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
