# Create a blocked email sender

`POST /accounts/{account_id}/email-security/settings/block_senders`

Adds a sender pattern to the email block list, preventing messages from matching
senders from being delivered.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **comments** (string, optional): 
- **is_regex** (boolean, required): 
- **pattern** (string, required): 
- **pattern_type** (string, required):  Values: `EMAIL`, `DOMAIN`, `IP`, `UNKNOWN`

## Response

### 201

Contains the newly created pattern.

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
