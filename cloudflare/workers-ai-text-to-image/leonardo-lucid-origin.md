# Execute @cf/leonardo/lucid-origin model.

`POST /accounts/{account_id}/ai/run/@cf/leonardo/lucid-origin`

Runs inference on the @cf/leonardo/lucid-origin model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **guidance** (number, optional): Controls how closely the generated image should adhere to the prompt; higher values make the image more aligned with the prompt
- **height** (integer, optional): The height of the generated image in pixels
- **num_steps** (integer, optional): The number of diffusion steps; higher values can improve quality but take longer
- **prompt** (string, required): A text description of the image you want to generate.
- **seed** (integer, optional): Random seed for reproducibility of the image generation
- **steps** (integer, optional): The number of diffusion steps; higher values can improve quality but take longer
- **width** (integer, optional): The width of the generated image in pixels

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
