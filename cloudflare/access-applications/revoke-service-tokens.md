# Revoke application tokens

`POST /accounts/{account_id}/access/apps/{app_id}/revoke_tokens`

Revokes all tokens issued for an application.

## Parameters

- **app_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 202

Revoke application tokens response

_Empty object_

### 4XX

Revoke application tokens response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
