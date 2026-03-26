# Update an App Config

`PATCH /accounts/{account_id}/magic/sites/{site_id}/app_configs/{app_config_id}`

Updates an App Config for a site

## Parameters

- **account_id** (string, required) [path]: 
- **site_id** (string, required) [path]: 
- **app_config_id** (string, required) [path]: 

## Request Body

- **account_app_id** (string, optional): Magic account app ID.
- **breakout** (boolean, optional): Whether to breakout traffic to the app's endpoints directly. Null preserves default behavior.
- **managed_app_id** (string, optional): Managed app ID.
- **preferred_wans** (array, optional): WAN interfaces to prefer over default WANs, highest-priority first. Can only be specified for breakout rules (breakout must be true).
- **priority** (integer, optional): Priority of traffic. 0 is default, anything greater is prioritized. (Currently only 0 and 1 are supported)

## Response

### 200

Update Site App Config response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): Traffic decision configuration for an app.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Update Site App Config response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
