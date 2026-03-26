# Execute @hf/thebloke/neural-chat-7b-v3-1-awq model.

`POST /accounts/{account_id}/ai/run/@hf/thebloke/neural-chat-7b-v3-1-awq`

Runs inference on the @hf/thebloke/neural-chat-7b-v3-1-awq model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

_Empty object_

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
