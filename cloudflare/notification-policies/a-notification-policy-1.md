# Delete a Notification policy

`DELETE /accounts/{account_id}/alerting/v3/policies/{policy_id}`

Delete a Notification policy.

## Parameters

- **account_id** (string, required) [path]: 
- **policy_id** (string, required) [path]: 

## Response

### 200

Delete a Notification policy response

_Empty object_

### 4XX

Delete a Notification policy response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`
