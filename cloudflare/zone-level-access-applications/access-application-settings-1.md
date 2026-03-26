# Update application settings

`PUT /zones/{zone_id}/access/apps/{app_id}/settings`

Updates application settings.

## Parameters

- **app_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **allow_iframe** (boolean, optional): Enables loading application content in an iFrame.
- **skip_interstitial** (boolean, optional): Enables automatic authentication through cloudflared.

## Response

### 202

Update application settings response

_Empty object_

### 4XX

Update application settings response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
