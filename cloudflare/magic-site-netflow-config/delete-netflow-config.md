# Delete NetFlow Configuration

`DELETE /accounts/{account_id}/magic/sites/{site_id}/netflow_config`

Remove NetFlow configuration for a site.

## Parameters

- **account_id** (string, required) [path]: 
- **site_id** (string, required) [path]: 


## Response

### 200

Delete NetFlow Configuration response

- **result** (object, optional): NetFlow configuration for a site.

### 4XX

Delete NetFlow Configuration response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
