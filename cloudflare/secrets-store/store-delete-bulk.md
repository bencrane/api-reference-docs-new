# Delete secrets

`DELETE /accounts/{account_id}/secrets_store/stores/{store_id}/secrets`

Deletes one or more secrets

## Parameters

- **account_id** (string, required) [path]: 
- **store_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

secret detail

- **result** (array, optional): 

### 4XX

List store secrets response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
