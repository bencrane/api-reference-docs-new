# Execute @cf/ibm-granite/granite-4.0-h-micro model.

`POST /accounts/{account_id}/ai/run/@cf/ibm-granite/granite-4.0-h-micro`

Runs inference on the @cf/ibm-granite/granite-4.0-h-micro model.

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
