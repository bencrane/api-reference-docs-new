# Execute @cf/microsoft/phi-2 model.

`POST /accounts/{account_id}/ai/run/@cf/microsoft/phi-2`

Runs inference on the @cf/microsoft/phi-2 model.

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
