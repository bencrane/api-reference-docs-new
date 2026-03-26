# Delete Site WAN

`DELETE /accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}`

Remove a specific Site WAN.

## Parameters

- **site_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **wan_id** (string, required) [path]: 


## Response

### 200

Delete Site WAN response

- **result** (object, optional): 

### 4XX

Delete Site WAN response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
