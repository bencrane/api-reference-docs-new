# Move a message

`POST /accounts/{account_id}/email-security/investigate/{postfix_id}/move`

Moves a single email message to a different folder or changes its quarantine status.

## Parameters

- **account_id** (string, required) [path]: 
- **postfix_id** (string, required) [path]: 

## Request Body

- **destination** (string, required):  Values: `Inbox`, `JunkEmail`, `DeletedItems`, `RecoverableItemsDeletions`, `RecoverableItemsPurges`

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
