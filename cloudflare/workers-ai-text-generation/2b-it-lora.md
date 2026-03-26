# Execute @cf/google/gemma-2b-it-lora model.

`POST /accounts/{account_id}/ai/run/@cf/google/gemma-2b-it-lora`

Runs inference on the @cf/google/gemma-2b-it-lora model.

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
