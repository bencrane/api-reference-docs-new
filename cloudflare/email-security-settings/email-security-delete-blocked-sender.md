# Delete a blocked email sender

`DELETE /accounts/{account_id}/email-security/settings/block_senders/{pattern_id}`

Removes a sender from the email block list, allowing their messages to be delivered
normally.

## Parameters

- **account_id** (string, required) [path]: 
- **pattern_id** (string, required) [path]: 

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
