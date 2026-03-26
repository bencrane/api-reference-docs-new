# Delete App Config

`DELETE /accounts/{account_id}/magic/sites/{site_id}/app_configs/{app_config_id}`

Deletes specific App Config associated with a site.

## Parameters

- **account_id** (string, required) [path]: 
- **site_id** (string, required) [path]: 
- **app_config_id** (string, required) [path]: 

## Response

### 200

Delete App Config response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): Traffic decision configuration for an app.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Delete App Config response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
