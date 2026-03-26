# Role Details

`GET /accounts/{account_id}/roles/{role_id}`

Get information about a specific role for an account.

## Parameters

- **role_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Role Details response

- **result** (object, optional): 

### 4XX

Role Details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
