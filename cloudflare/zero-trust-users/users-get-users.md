# Get users

`GET /accounts/{account_id}/access/users`

Gets a list of users for an account.

## Parameters

- **account_id** (string, required) [path]: 
- **name** (string, optional) [query]: 
- **email** (string, optional) [query]: 
- **search** (string, optional) [query]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

Get users response

_Empty object_

### 4XX

Get users response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
