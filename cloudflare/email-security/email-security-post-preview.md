# Preview for non-detection messages

`POST /accounts/{account_id}/email-security/investigate/preview`

Generates a preview of an email message for safe viewing without executing any
embedded content.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **postfix_id** (string, required): The identifier of the message.

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
