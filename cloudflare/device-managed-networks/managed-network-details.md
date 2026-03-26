# Get device managed network details

`GET /accounts/{account_id}/devices/networks/{network_id}`

Fetches details for a single managed network.

## Parameters

- **network_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get device managed network details response.

- **result** (object, optional): 

### 4XX

Get device managed network details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
