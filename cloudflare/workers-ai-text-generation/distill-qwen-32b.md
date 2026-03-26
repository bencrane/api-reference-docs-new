# Execute @cf/deepseek-ai/deepseek-r1-distill-qwen-32b model.

`POST /accounts/{account_id}/ai/run/@cf/deepseek-ai/deepseek-r1-distill-qwen-32b`

Runs inference on the @cf/deepseek-ai/deepseek-r1-distill-qwen-32b model.

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
