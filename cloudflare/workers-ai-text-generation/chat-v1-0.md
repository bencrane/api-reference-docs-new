# Execute @cf/tinyllama/tinyllama-1.1b-chat-v1.0 model.

`POST /accounts/{account_id}/ai/run/@cf/tinyllama/tinyllama-1.1b-chat-v1.0`

Runs inference on the @cf/tinyllama/tinyllama-1.1b-chat-v1.0 model.

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
