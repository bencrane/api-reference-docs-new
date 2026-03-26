# Execute @cf/myshell-ai/melotts model.

`POST /accounts/{account_id}/ai/run/@cf/myshell-ai/melotts`

Runs inference on the @cf/myshell-ai/melotts model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **lang** (string, optional): The speech language (e.g., 'en' for English, 'fr' for French). Defaults to 'en' if not specified
- **prompt** (string, required): A text description of the audio you want to generate

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
