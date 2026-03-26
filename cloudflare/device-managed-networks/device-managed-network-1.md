# Delete a device managed network

`DELETE /accounts/{account_id}/devices/networks/{network_id}`

Deletes a device managed network and fetches a list of the remaining device managed networks for an account.

## Parameters

- **network_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete a device managed network response.

- **result** (array, optional): 

### 4XX

Delete a device managed network response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
