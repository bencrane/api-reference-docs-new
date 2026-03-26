# Execute @cf/qwen/qwen2.5-coder-32b-instruct model.

`POST /accounts/{account_id}/ai/run/@cf/qwen/qwen2.5-coder-32b-instruct`

Runs inference on the @cf/qwen/qwen2.5-coder-32b-instruct model.

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
