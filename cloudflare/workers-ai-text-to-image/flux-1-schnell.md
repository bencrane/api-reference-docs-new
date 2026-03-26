# Execute @cf/black-forest-labs/flux-1-schnell model.

`POST /accounts/{account_id}/ai/run/@cf/black-forest-labs/flux-1-schnell`

Runs inference on the @cf/black-forest-labs/flux-1-schnell model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **prompt** (string, required): A text description of the image you want to generate.
- **steps** (integer, optional): The number of diffusion steps; higher values can improve quality but take longer.

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
