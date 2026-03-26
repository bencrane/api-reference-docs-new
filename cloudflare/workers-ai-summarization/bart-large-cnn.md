# Execute @cf/facebook/bart-large-cnn model.

`POST /accounts/{account_id}/ai/run/@cf/facebook/bart-large-cnn`

Runs inference on the @cf/facebook/bart-large-cnn model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **input_text** (string, required): The text that you want the model to summarize
- **max_length** (integer, optional): The maximum length of the generated summary in tokens

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
