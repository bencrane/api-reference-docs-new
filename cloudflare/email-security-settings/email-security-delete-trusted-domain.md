# Delete a trusted email domain

`DELETE /accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}`

Removes a domain from the trusted domains list, subjecting it to normal security
scanning.

## Parameters

- **account_id** (string, required) [path]: 
- **trusted_domain_id** (string, required) [path]: 

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
