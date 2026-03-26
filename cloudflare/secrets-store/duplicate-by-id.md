# Duplicate Secret

`POST /accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}/duplicate`

Duplicates the secret, keeping the value

## Parameters

- **account_id** (string, required) [path]: 
- **store_id** (string, required) [path]: 
- **secret_id** (string, required) [path]: 

## Request Body

- **comment** (string, optional): Freeform text describing the secret
- **name** (string, required): The name of the secret
- **scopes** (array, required): The list of services that can use this secret.

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
