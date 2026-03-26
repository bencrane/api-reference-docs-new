# Execute @cf/aisingapore/gemma-sea-lion-v4-27b-it model.

`POST /accounts/{account_id}/ai/run/@cf/aisingapore/gemma-sea-lion-v4-27b-it`

Runs inference on the @cf/aisingapore/gemma-sea-lion-v4-27b-it model.

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
