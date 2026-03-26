# Get a Notification policy

`GET /accounts/{account_id}/alerting/v3/policies/{policy_id}`

Get details for a single policy.

## Parameters

- **account_id** (string, required) [path]: 
- **policy_id** (string, required) [path]: 

## Response

### 200

Get a Notification policy response

- **result** (object, optional): 

### 4XX

Get a Notification policy response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `false`
