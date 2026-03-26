# Delete an Access reusable policy

`DELETE /accounts/{account_id}/access/policies/{policy_id}`

Deletes an Access reusable policy.

## Parameters

- **account_id** (string, required) [path]: 
- **policy_id** (string, required) [path]: 

## Response

### 202

Delete an Access reusable policy response.

_Empty object_

### 4XX

Delete an Access reusable policy response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
