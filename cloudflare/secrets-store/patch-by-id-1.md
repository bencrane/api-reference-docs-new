# Patch a secret (System)

`PATCH /system/accounts/{account_tag}/stores/{store_id}/secrets/{secret_id}`

Updates a single secret in a store managed by the calling service.
Returns 404 if the store doesn't exist or is not managed by the authenticated service.


## Parameters

- **account_tag** (string, required) [path]: Account tag identifier (e.g., '12a6ed19f349896cfbd6694ba3de8d31').
This is the account's external tag identifier, not the numeric account ID.

- **store_id** (string, required) [path]: 
- **secret_id** (string, required) [path]: 

## Request Body

- **comment** (string, optional): Freeform text describing the secret
- **scopes** (array, optional): The list of services that can use this secret.

## Response

### 200

Secret detail

- **result** (object, optional): 

### 4XX

Patch secret failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
