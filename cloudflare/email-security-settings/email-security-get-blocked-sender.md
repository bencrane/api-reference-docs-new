# Get a blocked email sender

`GET /accounts/{account_id}/email-security/settings/block_senders/{pattern_id}`

Gets information about a specific blocked sender entry, including the pattern and
block reason.

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
