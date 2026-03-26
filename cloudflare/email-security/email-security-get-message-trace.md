# Get email trace

`GET /accounts/{account_id}/email-security/investigate/{postfix_id}/trace`

Gets the delivery trace for an email message, showing its path through email
security processing.

## Parameters

- **account_id** (string, required) [path]: 
- **postfix_id** (string, required) [path]: 

## Response

### 200

Contains the email trace.

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
