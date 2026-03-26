# Create a variant

`POST /accounts/{account_id}/images/v1/variants`

Specify variants that allow you to resize images for different use cases.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **id** (string, required): 
- **neverRequireSignedURLs** (boolean, optional): Indicates whether the variant can access an image without a signature, regardless of image access control.
- **options** (object, required): Allows you to define image resizing sizes for different use cases.

## Response

### 200

Create a variant response

- **result** (object, optional): 

### 4XX

Create a variant response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
