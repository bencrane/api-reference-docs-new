# Execute @hf/thebloke/deepseek-coder-6.7b-base-awq model.

`POST /accounts/{account_id}/ai/run/@hf/thebloke/deepseek-coder-6.7b-base-awq`

Runs inference on the @hf/thebloke/deepseek-coder-6.7b-base-awq model.

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
