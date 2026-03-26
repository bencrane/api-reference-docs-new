# Execute @cf/qwen/qwen3-embedding-0.6b model.

`POST /accounts/{account_id}/ai/run/@cf/qwen/qwen3-embedding-0.6b`

Runs inference on the @cf/qwen/qwen3-embedding-0.6b model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **documents** (object, optional): 
- **instruction** (string, optional): Optional instruction for the task
- **queries** (object, optional): 
- **text** (object, optional): 

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
