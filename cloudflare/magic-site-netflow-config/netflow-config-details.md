# NetFlow Configuration Details

`GET /accounts/{account_id}/magic/sites/{site_id}/netflow_config`

Get NetFlow configuration for a site.

## Parameters

- **account_id** (string, required) [path]: 
- **site_id** (string, required) [path]: 

## Response

### 200

Get NetFlow Configuration response

- **result** (object, optional): NetFlow configuration for a site.

### 4XX

Get NetFlow Configuration response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
