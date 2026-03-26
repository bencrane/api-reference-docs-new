# Refresh a service token

`POST /accounts/{account_id}/access/service_tokens/{service_token_id}/refresh`

Refreshes the expiration of a service token.

## Parameters

- **service_token_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Refresh a service token response

_Empty object_

### 4XX

Refresh a service token response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
