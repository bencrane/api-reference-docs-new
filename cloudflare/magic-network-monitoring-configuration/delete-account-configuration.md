# Delete account configuration

`DELETE /accounts/{account_id}/mnm/config`

Delete an existing network monitoring configuration.

## Parameters

- **account_id** (string, required) [path]: 


## Response

### 200

Delete account configuration response

- **result** (object, optional): 

### 4XX

Delete account configuration response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
