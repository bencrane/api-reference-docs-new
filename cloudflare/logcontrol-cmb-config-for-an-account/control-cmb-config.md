# Delete CMB config

`DELETE /accounts/{account_id}/logs/control/cmb/config`

Deletes CMB config.

## Parameters

- **account_id** (string, required) [path]: 


## Response

### 200

Delete CMB config response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional):  Values: ``

### 4XX

Delete CMB config response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
