# Execute @cf/zai-org/glm-4.7-flash model.

`POST /accounts/{account_id}/ai/run/@cf/zai-org/glm-4.7-flash`

Runs inference on the @cf/zai-org/glm-4.7-flash model.

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
