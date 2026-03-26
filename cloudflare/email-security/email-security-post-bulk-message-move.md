# Move multiple messages

`POST /accounts/{account_id}/email-security/investigate/move`

Maximum batch size: 1000 messages per request

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **destination** (string, required):  Values: `Inbox`, `JunkEmail`, `DeletedItems`, `RecoverableItemsDeletions`, `RecoverableItemsPurges`
- **ids** (array, optional): List of message IDs to move.
- **postfix_ids** (array, optional): Deprecated: Use `ids` instead. List of message IDs to move.

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
