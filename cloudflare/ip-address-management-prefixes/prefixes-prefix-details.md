# Prefix Details

`GET /accounts/{account_id}/addressing/prefixes/{prefix_id}`

List a particular prefix owned by the account.

## Parameters

- **prefix_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Prefix Details response

- **result** (object, optional): 

### 4XX

Prefix Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
