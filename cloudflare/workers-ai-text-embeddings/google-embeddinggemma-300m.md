# Execute @cf/google/embeddinggemma-300m model.

`POST /accounts/{account_id}/ai/run/@cf/google/embeddinggemma-300m`

Runs inference on the @cf/google/embeddinggemma-300m model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **text** (object, required): 

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
