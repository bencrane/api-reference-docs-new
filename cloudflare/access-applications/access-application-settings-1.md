# Update Access application settings

`PUT /accounts/{account_id}/access/apps/{app_id}/settings`

Updates Access application settings.

## Parameters

- **app_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **allow_iframe** (boolean, optional): Enables loading application content in an iFrame.
- **skip_interstitial** (boolean, optional): Enables automatic authentication through cloudflared.

## Response

### 202

Update Access application settings response

_Empty object_

### 4XX

Update Access application settings response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
