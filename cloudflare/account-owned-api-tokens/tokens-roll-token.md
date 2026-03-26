# Roll Token

`PUT /accounts/{account_id}/tokens/{token_id}/value`

Roll the Account Owned API token secret.

## Parameters

- **account_id** (string, required) [path]: 
- **token_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 200

Roll Token response

- **result** (string, optional): The token value.

### 4XX

Roll Token response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
