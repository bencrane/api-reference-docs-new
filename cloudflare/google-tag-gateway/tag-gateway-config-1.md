# Update Google Tag Gateway configuration

`PUT /zones/{zone_id}/settings/google-tag-gateway/config`

Updates the Google Tag Gateway configuration for a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **enabled** (boolean, required): Enables or disables Google Tag Gateway for this zone.
- **endpoint** (string, required): Specifies the endpoint path for proxying Google Tag Manager requests. Use an absolute path starting with '/', with no nested paths and alphanumeric characters only (e.g. /metrics).
- **hideOriginalIp** (boolean, required): Hides the original client IP address from Google when enabled.
- **measurementId** (string, required): Specify the Google Tag Manager container or measurement ID (e.g. GTM-XXXXXXX or G-XXXXXXXXXX).
- **setUpTag** (boolean, optional): Set up the associated Google Tag on the zone automatically when enabled.

## Response

### 200

Update Google Tag Gateway configuration response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): Google Tag Gateway configuration for a zone.

### 4XX

Update Google Tag Gateway configuration response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
