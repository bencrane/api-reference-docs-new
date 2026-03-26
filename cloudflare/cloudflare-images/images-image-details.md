# Image details

`GET /accounts/{account_id}/images/v1/{image_id}`

Fetch details for a single image.

## Parameters

- **image_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Image details response

- **result** (object, optional): 

### 4XX

Image details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
