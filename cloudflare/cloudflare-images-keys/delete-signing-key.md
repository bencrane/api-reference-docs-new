# Delete Signing Key

`DELETE /accounts/{account_id}/images/v1/keys/{signing_key_name}`

Delete signing key with specified name. Returns all keys available.
When last key is removed, a new default signing key will be generated.


## Parameters

- **signing_key_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Delete Signing Key response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Delete Signing Key response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
