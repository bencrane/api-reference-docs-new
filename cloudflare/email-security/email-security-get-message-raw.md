# Get raw email content

`GET /accounts/{account_id}/email-security/investigate/{postfix_id}/raw`

Returns the raw eml of any non-benign message.

## Parameters

- **account_id** (string, required) [path]: 
- **postfix_id** (string, required) [path]: 

## Response

### 200

Contains the raw content of the email.

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
