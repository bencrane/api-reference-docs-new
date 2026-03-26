# Get an email domain

`GET /accounts/{account_id}/email-security/settings/domains/{domain_id}`

Gets configuration details for a specific domain in email security.

## Parameters

- **account_id** (string, required) [path]: 
- **domain_id** (integer, required) [path]: 

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
