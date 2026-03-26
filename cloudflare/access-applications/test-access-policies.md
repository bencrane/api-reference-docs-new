# Test Access policies

`GET /accounts/{account_id}/access/apps/{app_id}/user_policy_checks`

Tests if a specific user has permission to access an application.

## Parameters

- **app_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Test Access policies response

_Empty object_

### 4XX

Test Access policies response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
