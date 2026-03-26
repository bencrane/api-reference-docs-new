# Execute @cf/mistral/mistral-7b-instruct-v0.2-lora model.

`POST /accounts/{account_id}/ai/run/@cf/mistral/mistral-7b-instruct-v0.2-lora`

Runs inference on the @cf/mistral/mistral-7b-instruct-v0.2-lora model.

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
