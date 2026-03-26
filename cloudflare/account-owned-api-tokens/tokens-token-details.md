# Token Details

`GET /accounts/{account_id}/tokens/{token_id}`

Get information about a specific Account Owned API token.

## Parameters

- **account_id** (string, required) [path]: 
- **token_id** (string, required) [path]: 

## Response

### 200

Token Details response

- **result** (object, optional): 

### 4XX

Token Details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
