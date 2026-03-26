# Delete a secret

`DELETE /accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}`

Deletes a single secret

## Parameters

- **account_id** (string, required) [path]: 
- **store_id** (string, required) [path]: 
- **secret_id** (string, required) [path]: 

## Response

### 200

secret detail

- **result** (object, optional): 

### 4XX

failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
