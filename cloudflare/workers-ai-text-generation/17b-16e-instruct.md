# Execute @cf/meta/llama-4-scout-17b-16e-instruct model.

`POST /accounts/{account_id}/ai/run/@cf/meta/llama-4-scout-17b-16e-instruct`

Runs inference on the @cf/meta/llama-4-scout-17b-16e-instruct model.

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
