# Create a store

`POST /accounts/{account_id}/secrets_store/stores`

Creates a store in the account

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

store details

- **result** (array, optional): 

### 4XX

List store secrets response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
