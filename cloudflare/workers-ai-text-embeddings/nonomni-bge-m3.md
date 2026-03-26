# Execute @cf/baai/nonomni-bge-m3 model.

`POST /accounts/{account_id}/ai/run/@cf/baai/nonomni-bge-m3`

Runs inference on the @cf/baai/nonomni-bge-m3 model.

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
