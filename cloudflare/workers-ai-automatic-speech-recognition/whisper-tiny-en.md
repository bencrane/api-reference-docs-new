# Execute @cf/openai/whisper-tiny-en model.

`POST /accounts/{account_id}/ai/run/@cf/openai/whisper-tiny-en`

Runs inference on the @cf/openai/whisper-tiny-en model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 


## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
