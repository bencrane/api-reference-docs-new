# Member Details

`GET /accounts/{account_id}/members/{member_id}`

Get information about a specific member of an account.

## Parameters

- **member_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Member Details response

- **result** (object, optional): 

### 4XX

Member Details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
