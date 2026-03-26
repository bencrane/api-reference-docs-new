# Delete an email allow policy

`DELETE /accounts/{account_id}/email-security/settings/allow_policies/{policy_id}`

Removes an email allow policy. Previously allowed senders will be subject to normal
security scanning.

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
