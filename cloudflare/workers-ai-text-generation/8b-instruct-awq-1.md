# Execute @cf/meta/llama-3.1-8b-instruct-awq model.

`POST /accounts/{account_id}/ai/run/@cf/meta/llama-3.1-8b-instruct-awq`

Runs inference on the @cf/meta/llama-3.1-8b-instruct-awq model.

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
