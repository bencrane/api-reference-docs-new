# Execute @cf/black-forest-labs/flux-2-dev model.

`POST /accounts/{account_id}/ai/run/@cf/black-forest-labs/flux-2-dev`

Runs inference on the @cf/black-forest-labs/flux-2-dev model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **multipart** (object, required): 

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
