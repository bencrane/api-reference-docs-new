# Site LAN Details

`GET /accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}`

Get a specific Site LAN.

## Parameters

- **site_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **lan_id** (string, required) [path]: 

## Response

### 200

Site LAN Details response

- **result** (object, optional): 

### 4XX

Site LAN Details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
