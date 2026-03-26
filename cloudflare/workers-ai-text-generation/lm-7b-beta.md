# Execute @hf/nexusflow/starling-lm-7b-beta model.

`POST /accounts/{account_id}/ai/run/@hf/nexusflow/starling-lm-7b-beta`

Runs inference on the @hf/nexusflow/starling-lm-7b-beta model.

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
