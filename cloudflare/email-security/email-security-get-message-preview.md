# Get email preview

`GET /accounts/{account_id}/email-security/investigate/{postfix_id}/preview`

Returns a preview of the message body as a base64 encoded PNG image for non-benign messages.

## Parameters

- **account_id** (string, required) [path]: 
- **postfix_id** (string, required) [path]: 

## Response

### 200

Contains a preview of the email.

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
