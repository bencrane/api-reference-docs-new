# Execute @cf/openai/gpt-oss-20b model.

`POST /accounts/{account_id}/ai/run/@cf/openai/gpt-oss-20b`

Runs inference on the @cf/openai/gpt-oss-20b model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

One of: object, Responses, Responses_Async

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
