# Delete Site

`DELETE /accounts/{account_id}/magic/sites/{site_id}`

Remove a specific Site.

## Parameters

- **site_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete Site response

- **result** (object, optional): 

### 4XX

Delete Site response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
