# Execute @cf/thebloke/discolm-german-7b-v1-awq model.

`POST /accounts/{account_id}/ai/run/@cf/thebloke/discolm-german-7b-v1-awq`

Runs inference on the @cf/thebloke/discolm-german-7b-v1-awq model.

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
