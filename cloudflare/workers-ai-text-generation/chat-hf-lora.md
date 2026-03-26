# Execute @cf/meta-llama/llama-2-7b-chat-hf-lora model.

`POST /accounts/{account_id}/ai/run/@cf/meta-llama/llama-2-7b-chat-hf-lora`

Runs inference on the @cf/meta-llama/llama-2-7b-chat-hf-lora model.

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
