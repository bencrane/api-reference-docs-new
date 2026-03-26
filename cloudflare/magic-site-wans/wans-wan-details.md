# Site WAN Details

`GET /accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}`

Get a specific Site WAN.

## Parameters

- **site_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **wan_id** (string, required) [path]: 

## Response

### 200

Site WAN Details response

- **result** (object, optional): 

### 4XX

Site WAN Details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
