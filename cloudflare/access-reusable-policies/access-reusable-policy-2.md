# Get an Access reusable policy

`GET /accounts/{account_id}/access/policies/{policy_id}`

Fetches a single Access reusable policy.

## Parameters

- **account_id** (string, required) [path]: 
- **policy_id** (string, required) [path]: 

## Response

### 200

Get an Access reusable policy response.

_Empty object_

### 4XX

Get an Access reusable policy response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
