# Create a new Signing Key

`PUT /accounts/{account_id}/images/v1/keys/{signing_key_name}`

Create a new signing key with specified name. Returns all keys available.

## Parameters

- **signing_key_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Add Signing Key response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Add Signing Key response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
