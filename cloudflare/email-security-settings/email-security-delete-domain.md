# Unprotect an email domain

`DELETE /accounts/{account_id}/email-security/settings/domains/{domain_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **domain_id** (integer, required) [path]: 

## Response

### 200

Deletes the domain with the provided id.

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
