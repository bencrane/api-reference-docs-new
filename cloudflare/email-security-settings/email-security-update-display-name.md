# Update an entry in impersonation registry

`PATCH /accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}`

Updates a display name entry used for impersonation protection.

## Parameters

- **account_id** (string, required) [path]: 
- **display_name_id** (integer, required) [path]: 

## Request Body

- **email** (string, optional): 
- **is_email_regex** (boolean, optional): 
- **name** (string, optional): 

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
