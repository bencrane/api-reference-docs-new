# Execute @cf/meta/llama-guard-3-8b model.

`POST /accounts/{account_id}/ai/run/@cf/meta/llama-guard-3-8b`

Runs inference on the @cf/meta/llama-guard-3-8b model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **max_tokens** (integer, optional): The maximum number of tokens to generate in the response.
- **messages** (array, required): An array of message objects representing the conversation history.
- **response_format** (object, optional): Dictate the output format of the generated response.
- **temperature** (number, optional): Controls the randomness of the output; higher values produce more random results.

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
