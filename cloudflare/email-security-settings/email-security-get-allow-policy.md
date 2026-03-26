# Get an email allow policy

`GET /accounts/{account_id}/email-security/settings/allow_policies/{policy_id}`

Retrieves details for a specific email allow policy, including its matching criteria
and scope.

## Parameters

- **account_id** (string, required) [path]: 
- **policy_id** (string, required) [path]: 

## Response

### 200



- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): 
- **result** (object, optional): 

### 4XX

Client Error

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
