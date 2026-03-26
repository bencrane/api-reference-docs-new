# Patch a secret

`PATCH /accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}`

Updates a single secret

## Parameters

- **account_id** (string, required) [path]: 
- **store_id** (string, required) [path]: 
- **secret_id** (string, required) [path]: 

## Request Body

- **comment** (string, optional): Freeform text describing the secret
- **scopes** (array, optional): The list of services that can use this secret.

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
