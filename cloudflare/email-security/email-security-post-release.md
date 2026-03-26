# Release messages from quarantine

`POST /accounts/{account_id}/email-security/investigate/release`

Releases a quarantined email message, allowing it to be delivered to the recipient.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

Array of string

## Response

### 200



- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): 
- **result** (array, optional): 

### 4XX

Client Error

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
