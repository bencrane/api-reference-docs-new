# Create an entry in impersonation registry

`POST /accounts/{account_id}/email-security/settings/impersonation_registry`

Creates a display name entry for email security impersonation protection.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **email** (string, required): 
- **is_email_regex** (boolean, required): 
- **name** (string, required): 

## Response

### 201



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
