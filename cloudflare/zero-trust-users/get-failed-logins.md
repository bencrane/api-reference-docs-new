# Get failed logins

`GET /accounts/{account_id}/access/users/{user_id}/failed_logins`

Get all failed login attempts for a single user.

## Parameters

- **user_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get failed logins response

_Empty object_

### 4XX

Get failed logins response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
