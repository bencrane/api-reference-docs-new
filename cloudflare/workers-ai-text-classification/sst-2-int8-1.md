# Execute @cf/huggingface/nonomni-distilbert-sst-2-int8 model.

`POST /accounts/{account_id}/ai/run/@cf/huggingface/nonomni-distilbert-sst-2-int8`

Runs inference on the @cf/huggingface/nonomni-distilbert-sst-2-int8 model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **text** (string, required): The text that you want to classify

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
