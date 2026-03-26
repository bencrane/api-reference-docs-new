# List App Configs

`GET /accounts/{account_id}/magic/sites/{site_id}/app_configs`

Lists App Configs associated with a site.

## Parameters

- **account_id** (string, required) [path]: 
- **site_id** (string, required) [path]: 

## Response

### 200

List App Configs response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

List App Configs response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
