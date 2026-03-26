# Delete Token

`DELETE /accounts/{account_id}/tokens/{token_id}`

Destroy an Account Owned API token.

## Parameters

- **account_id** (string, required) [path]: 
- **token_id** (string, required) [path]: 


## Response

### 200

Delete Token response

_Empty object_

### 4XX

Delete Token response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
