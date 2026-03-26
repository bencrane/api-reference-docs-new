# Execute @cf/baai/bge-reranker-base model.

`POST /accounts/{account_id}/ai/run/@cf/baai/bge-reranker-base`

Runs inference on the @cf/baai/bge-reranker-base model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **contexts** (array, required): List of provided contexts. Note that the index in this array is important, as the response will refer to it.
- **query** (string, required): A query you wish to perform against the provided contexts.
- **top_k** (integer, optional): Number of returned results starting with the best score.

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
