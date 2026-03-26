# Delete a store

`DELETE /accounts/{account_id}/secrets_store/stores/{store_id}`

Deletes a single store

## Parameters

- **account_id** (string, required) [path]: 
- **store_id** (string, required) [path]: 

## Response

### 200

store details

- **result** (object, optional): 

### 4XX

failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
