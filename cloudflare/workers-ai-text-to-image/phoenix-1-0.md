# Execute @cf/leonardo/phoenix-1.0 model.

`POST /accounts/{account_id}/ai/run/@cf/leonardo/phoenix-1.0`

Runs inference on the @cf/leonardo/phoenix-1.0 model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **guidance** (number, optional): Controls how closely the generated image should adhere to the prompt; higher values make the image more aligned with the prompt
- **height** (integer, optional): The height of the generated image in pixels
- **negative_prompt** (string, optional): Specify what to exclude from the generated images
- **num_steps** (integer, optional): The number of diffusion steps; higher values can improve quality but take longer
- **prompt** (string, required): A text description of the image you want to generate.
- **seed** (integer, optional): Random seed for reproducibility of the image generation
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
