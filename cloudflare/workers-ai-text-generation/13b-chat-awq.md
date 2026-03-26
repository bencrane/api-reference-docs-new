# Execute @hf/thebloke/llama-2-13b-chat-awq model.

`POST /accounts/{account_id}/ai/run/@hf/thebloke/llama-2-13b-chat-awq`

Runs inference on the @hf/thebloke/llama-2-13b-chat-awq model.

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
