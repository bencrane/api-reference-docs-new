# Get message details

`GET /accounts/{account_id}/email-security/investigate/{postfix_id}`

Retrieves detailed information about a specific email message, including headers,
metadata, and security scan results.

## Parameters

- **account_id** (string, required) [path]: 
- **postfix_id** (string, required) [path]: 

## Response

### 200

Contains the email message details.

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
