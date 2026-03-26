# Update a variant

`PATCH /accounts/{account_id}/images/v1/variants/{variant_id}`

Updating a variant purges the cache for all images associated with the variant.

## Parameters

- **variant_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **neverRequireSignedURLs** (boolean, optional): Indicates whether the variant can access an image without a signature, regardless of image access control.
- **options** (object, required): Allows you to define image resizing sizes for different use cases.

## Response

### 200

Update a variant response

- **result** (object, optional): 

### 4XX

Update a variant response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
