# Delete image

`DELETE /accounts/{account_id}/images/v1/{image_id}`

Delete an image on Cloudflare Images. On success, all copies of the image are deleted and purged from cache.

## Parameters

- **image_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete image response

- **result** (object, optional): 

### 4XX

Delete image response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
