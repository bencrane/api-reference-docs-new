# Delete Site LAN

`DELETE /accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}`

Remove a specific Site LAN.

## Parameters

- **site_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **lan_id** (string, required) [path]: 


## Response

### 200

Delete Site LAN response

- **result** (object, optional): 

### 4XX

Delete Site LAN response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
