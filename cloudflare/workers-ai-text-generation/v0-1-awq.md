# Execute @hf/thebloke/mistral-7b-instruct-v0.1-awq model.

`POST /accounts/{account_id}/ai/run/@hf/thebloke/mistral-7b-instruct-v0.1-awq`

Runs inference on the @hf/thebloke/mistral-7b-instruct-v0.1-awq model.

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
