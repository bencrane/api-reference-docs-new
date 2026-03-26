# Execute @cf/bytedance/stable-diffusion-xl-lightning model.

`POST /accounts/{account_id}/ai/run/@cf/bytedance/stable-diffusion-xl-lightning`

Runs inference on the @cf/bytedance/stable-diffusion-xl-lightning model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **guidance** (number, optional): Controls how closely the generated image should adhere to the prompt; higher values make the image more aligned with the prompt
- **height** (integer, optional): The height of the generated image in pixels
- **image** (array, optional): For use with img2img tasks. An array of integers that represent the image data constrained to 8-bit unsigned integer values
- **image_b64** (string, optional): For use with img2img tasks. A base64-encoded string of the input image
- **mask** (array, optional): An array representing An array of integers that represent mask image data for inpainting constrained to 8-bit unsigned integer values
- **negative_prompt** (string, optional): Text describing elements to avoid in the generated image
- **num_steps** (integer, optional): The number of diffusion steps; higher values can improve quality but take longer
- **prompt** (string, required): A text description of the image you want to generate
- **seed** (integer, optional): Random seed for reproducibility of the image generation
- **strength** (number, optional): A value between 0 and 1 indicating how strongly to apply the transformation during img2img tasks; lower values make the output closer to the input image
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
