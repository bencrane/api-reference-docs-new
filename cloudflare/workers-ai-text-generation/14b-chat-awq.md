# Execute @cf/qwen/qwen1.5-14b-chat-awq model.

`POST /accounts/{account_id}/ai/run/@cf/qwen/qwen1.5-14b-chat-awq`

Runs inference on the @cf/qwen/qwen1.5-14b-chat-awq model.

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
