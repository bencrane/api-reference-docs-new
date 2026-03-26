# Create a secret

`POST /accounts/{account_id}/secrets_store/stores/{store_id}/secrets`

Creates a secret in the account

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
