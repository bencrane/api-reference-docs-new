# Update a blocked email sender

`PATCH /accounts/{account_id}/email-security/settings/block_senders/{pattern_id}`

Modifies a blocked sender entry, updating its pattern or block reason.

## Parameters

- **account_id** (string, required) [path]: 
- **pattern_id** (string, required) [path]: 

## Request Body

- **comments** (string, optional): 
- **is_regex** (boolean, optional): 
- **pattern** (string, optional): 
- **pattern_type** (object, optional): 

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
