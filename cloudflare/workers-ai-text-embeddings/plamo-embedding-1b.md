# Execute @cf/pfnet/plamo-embedding-1b model.

`POST /accounts/{account_id}/ai/run/@cf/pfnet/plamo-embedding-1b`

Runs inference on the @cf/pfnet/plamo-embedding-1b model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **text** (object, required): Input text to embed. Can be a single string or a list of strings.

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
